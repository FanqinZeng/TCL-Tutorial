"""Validate original course sources using a genuine native Tcl interpreter."""
import argparse,json,os,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def native(spec):
    # Prefer tclsh on normal installations; --tk uses Python's native Tcl library.
    if os.environ.get('WORKSHOP_USE_TK')=='1':
        r=subprocess.run([sys.executable,str(ROOT/'scripts/native_worker.py')],input=json.dumps(spec),text=True,capture_output=True,timeout=6)
        if r.returncode:raise RuntimeError(r.stderr or 'Native Tcl worker exited without result')
        return json.loads(r.stdout)
    with tempfile.TemporaryDirectory(prefix='workshop-') as d:
        p=Path(d)
        for name,value in spec.get('files',{}).items():
            q=p/name
            if Path(name).is_absolute() or '..' in Path(name).parts:raise ValueError('Unsafe fixture path')
            q.parent.mkdir(parents=True,exist_ok=True);q.write_text(value)
        (p/'main.tcl').write_text(spec['code'])
        if spec.get('after'):(p/'after.tcl').write_text(spec['after'])
        wrapper='set __out [open stdout.txt w]\nset __err [open stderr.txt w]\n'
        # Tcl 8.6 channel reflection is unnecessary: child Tcl runs authored code then
        # captures its stdout through exec and performs checks in the same interpreter.
        wrapper='rename puts __native_puts\nset __captured {}\nproc puts {args} {\n global __captured\n if {[llength $args]==1} {append __captured [lindex $args 0] "\\n"; return}\n if {[llength $args]==2 && [lindex $args 0] eq "-nonewline"} {append __captured [lindex $args 1];return}\n if {[llength $args]==2 && [lindex $args 0] eq "stdout"} {append __captured [lindex $args 1] "\\n";return}\n uplevel 1 [linsert $args 0 __native_puts]\n}\n'
        args=spec.get('argv',[])
        def word(s):return '{'+s.replace('\\','\\\\').replace('{','\\{').replace('}','\\}')+'}'
        wrapper+='set argv [list '+ ' '.join(word(a) for a in args)+']\nset argc '+str(len(args))+'\n'
        wrapper+='if {[catch {source main.tcl} __error]} {__native_puts stderr $__error;exit 1}\n'
        if spec.get('after'):wrapper+='set __captured {}\nif {[catch {source after.tcl} __error]} {__native_puts stderr $__error;exit 1}\n'
        wrapper+='set workshop_stdout [string trimright $__captured "\\n"]\n__native_puts $__captured\n'
        for i,c in enumerate(spec.get('checks',[])):wrapper+=f'if {{[catch {{{c["script"]}}} __v]}} {{set __v FAIL}}\n__native_puts stderr "CHECK:{i}:$__v"\n'
        wrapper+='__native_puts stderr "VERSION:[info patchlevel]"\n'
        (p/'runner.tcl').write_text(wrapper)
        r=subprocess.run([os.environ.get('TCLSH','tclsh'),'runner.tcl'],cwd=p,text=True,capture_output=True,timeout=6)
        return {'output':r.stdout.rstrip('\n'),'error':r.stderr if r.returncode else None,'tests':[{'label':c['label'],'ok':f'CHECK:{i}:1' in r.stderr.splitlines()} for i,c in enumerate(spec.get('checks',[]))],'version':next((x[8:] for x in r.stderr.splitlines() if x.startswith('VERSION:')),'unknown')}

def all_specs():
    for f in sorted((ROOT/'lessons').glob('*.json')):
        l=json.loads(f.read_text())
        for i,e in enumerate(l['examples']):yield f'L{l["id"]:02}/example{i+1}',e
        for i,e in enumerate(l['exercises']):yield f'L{l["id"]:02}/exercise{i+1}',dict(e,code=e['solution'])
    for f in sorted((ROOT/'projects').glob('*.json')):
        p=json.loads(f.read_text());yield f'P{p["id"]}/solution',dict(p,code=p['solution'])
        for i,c in enumerate(p['cases']):yield f'P{p["id"]}/case{i+1}',dict(c,code=p['solution'],after=c['code'],files={**p.get('files',{}),**c.get('files',{})},argv=c.get('argv',p.get('argv',[])))

def main():
    a=argparse.ArgumentParser();a.add_argument('--all',action='store_true');a.add_argument('--tk',action='store_true');a.add_argument('--lesson',type=int);a.add_argument('--exercise',type=int,default=1);a.add_argument('file',nargs='?');args=a.parse_args()
    if args.tk:os.environ['WORKSHOP_USE_TK']='1'
    cases=list(all_specs()) if args.all else []
    if args.lesson and args.file:
        l=json.loads((ROOT/'lessons'/f'{args.lesson:02}.json').read_text());e=l['exercises'][args.exercise-1];cases=[('your solution',dict(e,code=Path(args.file).read_text()))]
    if not cases:a.error('Use --all or --lesson N --exercise N solution.tcl')
    failures=[];versions=set()
    for name,spec in cases:
        try:r=native(spec);ok=not r['error'] and r['output']==spec['expected'] and all(c['ok'] for c in r['tests']);versions.add(r['version'])
        except Exception as e:r={'error':str(e)};ok=False
        print(('PASS ' if ok else 'FAIL ')+name)
        if not ok:failures.append({'name':name,'expected':spec['expected'],'actual':r});print(json.dumps(failures[-1],ensure_ascii=False))
    print(f'{len(cases)-len(failures)}/{len(cases)} passed; native Tcl {", ".join(sorted(versions))}')
    report={'total':len(cases),'passed':len(cases)-len(failures),'versions':sorted(versions),'failures':failures}
    (ROOT/'tests/native-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    raise SystemExit(bool(failures))
if __name__=='__main__':main()
