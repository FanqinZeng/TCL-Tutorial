/* Exercise exactly the browser Worker and its real WASM, with local-only I/O. */
import fs from 'node:fs';import path from 'node:path';import vm from 'node:vm';import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../site');
const data=JSON.parse(fs.readFileSync(path.join(root,'course.json'),'utf8'));
function local(url){const p=path.resolve(root,new URL(String(url),'https://local.test/').pathname.slice(1));if(!p.startsWith(root+path.sep))throw Error('Nonlocal resource');return p;}
export function run(spec){return new Promise((resolve,reject)=>{
 let done=false;const timer=setTimeout(()=>{done=true;reject(Error('Runtime test timed out'));},15000);
 class LocalXHR{open(method,url){this.url=url;}send(){try{const b=fs.readFileSync(local(this.url));this.status=200;this.response=this.responseType==='arraybuffer'?b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength):b.toString();this.responseText=this.responseType==='arraybuffer'?'':b.toString();queueMicrotask(()=>this.onload?.());}catch(e){this.status=404;this.onerror?.(e)}}setRequestHeader(){}}
 const context={URL,WebAssembly,Uint8Array,Int8Array,Uint16Array,Int16Array,Uint32Array,Int32Array,Float32Array,Float64Array,ArrayBuffer,TextDecoder,TextEncoder,XMLHttpRequest:LocalXHR,console:{log(){},warn(){},error(){}},setTimeout:(...a)=>setTimeout(...a).unref(),clearTimeout,setInterval:(...a)=>setInterval(...a).unref(),clearInterval,location:{href:'https://local.test/worker.js',pathname:'/worker.js'},fetch:async url=>({ok:true,text:async()=>fs.readFileSync(local(url),'utf8')}),postMessage(m){if(done)return;if(m.type==='ready')setTimeout(()=>context.onmessage({data:spec}),0);else if(m.type==='result'){done=true;clearTimeout(timer);resolve(m)}else if(m.type==='failure'){done=true;clearTimeout(timer);reject(Error(m.message));}}};
 context.self=context;vm.createContext(context);context.importScripts=(...urls)=>urls.forEach(url=>vm.runInContext(fs.readFileSync(local(url),'utf8'),context,{filename:local(url)}));vm.runInContext(fs.readFileSync(path.join(root,'worker.js'),'utf8'),context,{filename:'worker.js'});
 });}
const cases=[];for(const l of data.lessons){l.examples.forEach((e,i)=>cases.push([`L${l.id}/example${i+1}`,e]));l.exercises.forEach((e,i)=>cases.push([`L${l.id}/exercise${i+1}`,{...e,code:e.solution}]));}
for(const p of data.projects){cases.push([`P${p.id}/solution`,{...p,code:p.solution}]);p.cases.forEach((c,i)=>cases.push([`P${p.id}/case${i+1}`,{...c,code:p.solution,after:c.code,files:{...p.files,...c.files},argv:c.argv||p.argv}]));}
let failed=0;const errors=[],versions=new Set();for(const [name,s]of cases){try{const r=await run({...s,trace:false});versions.add(r.version);const ok=!r.error&&r.output===s.expected&&r.tests.every(t=>t.ok);console.log(`${ok?'PASS':'FAIL'} WASM ${name}`);if(!ok){failed++;errors.push({name,expected:s.expected,result:r});console.log(JSON.stringify(errors.at(-1)));}}catch(e){failed++;errors.push({name,error:String(e)});console.log('FAIL',name,e)}}
const observed=await run({code:'set total 0\nforeach n {3 5 9} {incr total $n}\nputs $total'});
if(observed.output!=='17'||observed.variables.find(v=>v.name==='total')?.value!=='17'||!observed.events.some(e=>e.command==='incr total 9'&&e.result==='17'))throw Error('Real execution/data observation failed');
const dead=await run({code:'# incr value 99\nset value 0\nif {0} {incr value 99}\nputs $value'});if(dead.events.some(e=>e.command==='incr value 99'))throw Error('Unexecuted code produced an event');
const chinese=await run({code:'puts "你好，Tcl！"'});if(chinese.output!=='你好，Tcl！')throw Error('Chinese output failed');
const bad=await run({code:'puts $missing'});if(!bad.error)throw Error('Real errors swallowed');
const first=await run({code:'set f [open sample.txt w];puts $f "record";close $f'});if(!first.files.some(f=>f.content==='record\n'))throw Error('Virtual files unavailable');
const fresh=await run({code:'puts [file exists sample.txt]'});if(fresh.output!=='0')throw Error('Run state leaked');
const retained=await run({code:'set c {learner state}\nputs $c',checks:[{label:'Observer leaves learner c unchanged',script:'expr {$c eq {learner state}}'}]});
if(retained.output!=='learner state'||retained.variables.find(v=>v.name==='c')?.value!=='learner state'||!retained.tests.every(t=>t.ok))throw Error('Observation overwrote the learner variable c');
const objects=await run({code:`oo::class create ObservedMeter {
 variable readings
 constructor {} {set readings {}}
 method add {value} {lappend readings $value}
 method values {} {return $readings}
}
set first [ObservedMeter new]
set second [ObservedMeter new]
$first add 1.2
$first add 1.5
$second add 8
puts [info object namespace $first]
puts [info object namespace $second]`,checks:[{label:'Two instances retain separate actual readings',script:'expr {[$first values] eq {1.2 1.5} && [$second values] eq {8}}'}]});
const objectSpaces=objects.output.split('\n');
if(objects.error||objectSpaces.length!==2||objectSpaces[0]===objectSpaces[1]||objects.variables.find(v=>v.name===objectSpaces[0]+'::readings')?.value!=='1.2 1.5'||objects.variables.find(v=>v.name===objectSpaces[1]+'::readings')?.value!=='8'||!objects.tests.every(t=>t.ok))throw Error('Result view did not observe independent TclOO instance state');
const namespaced=await run({code:`set total 999
namespace eval measurements {
 variable total 20
 namespace eval day {variable count 3;variable label {morning group}}
}
puts "$total / $::measurements::total / $::measurements::day::count"`});
if(namespaced.error||namespaced.output!=='999 / 20 / 3'||namespaced.variables.find(v=>v.name==='total')?.value!=='999'||namespaced.variables.find(v=>v.name==='::measurements::total')?.value!=='20'||namespaced.variables.find(v=>v.name==='::measurements::day::count')?.value!=='3'||namespaced.variables.find(v=>v.name==='::measurements::day::label')?.value!=='morning group')throw Error('Nested namespace state was lost or conflated with global state');
const traced=await run({code:`set reads 0
set guarded secret
array set slots {safe ok guarded private}
namespace eval tracked {variable hidden payload}
proc unexpectedRead {args} {incr ::reads;error {Snapshot triggered a read trace}}
trace add variable guarded read unexpectedRead
trace add variable slots(guarded) read unexpectedRead
trace add variable ::tracked::hidden read unexpectedRead
puts ready`,checks:[{label:'Snapshot has not run any learner read trace',script:'expr {$reads == 0}'}]});
if(traced.error||traced.output!=='ready'||traced.variables.find(v=>v.name==='reads')?.value!=='0'||traced.variables.some(v=>v.name==='guarded'||v.name==='::tracked::hidden')||traced.variables.find(v=>v.name==='slots')?.value!=='safe ok'||!traced.tests.every(t=>t.ok))throw Error('Snapshot triggered read traces or exposed traced values');
const report={total:cases.length,passed:cases.length-failed,versions:[...versions],regressions:['execution events','dead branches','Chinese','errors','virtual files','fresh state','learner variable preservation','TclOO instance state','nested namespace state','read trace isolation'],failures:errors};fs.writeFileSync(path.join(root,'../tests/runtime-results.json'),JSON.stringify(report,null,2)+'\n');console.log(`${report.passed}/${report.total} WASM cases; Tcl ${[...versions].join(', ')}`);if(failed)process.exitCode=1;
