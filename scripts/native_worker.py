"""One isolated native Tcl interpreter. Used only to validate our authored examples."""
import json, os, sys, tempfile
from pathlib import Path

def main():
    spec=json.load(sys.stdin)
    import tkinter
    with tempfile.TemporaryDirectory(prefix='tcl-workshop-') as directory:
        os.chdir(directory)
        for name,value in spec.get('files',{}).items():
            p=Path(name)
            if p.is_absolute() or '..' in p.parts: raise ValueError('Fixture path must be relative')
            p.parent.mkdir(parents=True,exist_ok=True);p.write_text(value,encoding='utf-8')
        t=tkinter.Tcl()
        t.call('set','argv',t.call('list',*spec.get('argv',[])));t.call('set','argc',len(spec.get('argv',[])))
        def execute(code):
            saved=[os.dup(1),os.dup(2)];result='';error=None
            with tempfile.TemporaryFile() as out,tempfile.TemporaryFile() as err:
                os.dup2(out.fileno(),1);os.dup2(err.fileno(),2)
                try: result=t.eval(code)
                except tkinter.TclError as e: error=str(e)
                finally:
                    try:t.eval('flush stdout; flush stderr')
                    except tkinter.TclError:pass
                    os.dup2(saved[0],1);os.dup2(saved[1],2)
                    for fd in saved:os.close(fd)
                out.seek(0);err.seek(0)
                return {'output':out.read().decode('utf-8').rstrip('\n'),'stderr':err.read().decode('utf-8'),'result':result,'error':error}
        r=execute(spec['code'])
        if spec.get('after') and not r['error']:r=execute(spec['after'])
        t.call('set','workshop_stdout',r['output'])
        tests=[]
        if not r['error']:
            for check in spec.get('checks',[]):
                try: value=t.eval(check['script']);tests.append({'label':check['label'],'ok':value=='1','value':value})
                except tkinter.TclError as e:tests.append({'label':check['label'],'ok':False,'error':str(e)})
        r.update(tests=tests,version=t.eval('info patchlevel'))
        print(json.dumps(r,ensure_ascii=False))
if __name__=='__main__':main()
