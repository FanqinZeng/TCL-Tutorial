"""Generate website data and readable/runnable artifacts from one source."""
import hashlib,json,shutil,shlex
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
UNITS=['第一次让电脑帮忙','选择与重复','文本与结构化数据','可复用的脚本','组织稍大的项目','走向 VLSI 脚本应用']
def write(path,text):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding='utf-8')
def block(code,lang='tcl'):return f'```{lang}\n{code}\n```\n'
def details(title,text):return f'<details><summary>{title}</summary>\n\n{text}\n\n</details>\n'
def project_files(files,base):
 """Expose the exact teaching inputs, including executable helper scripts."""
 if not files:return '没有额外预置文件。\n\n'
 md=''
 for name,text in files.items():
  rel=f'../../data/{base}/{name}'
  md+=f'- 虚拟路径 `{name}` → [本地输入文件]({rel})\n\n'
  md+=details(f'查看 {name} 的完整内容',block(text.rstrip('\n'),'tcl' if name.endswith('.tcl') else 'text'))+'\n'
 return md
def arguments(spec):
 args=spec.get('argv',[])
 return '默认模拟参数（JSON 数组表示）：\n\n'+block('argv = '+json.dumps(args,ensure_ascii=False)+'\nargc = '+str(len(args)),'text')+'\n'
def lesson_run(spec,script,data_base):
 """Prepare the same input files and argument vector as a single lesson run."""
 commands=['# 从本仓库根目录执行；文件读写发生在新建的临时练习目录。','workshop_repo="$PWD"','practice_dir="$(mktemp -d)"']
 for name in spec.get('files',{}):
  parent=Path(name).parent.as_posix()
  if parent!='.':commands.append('mkdir -p "$practice_dir"/'+shlex.quote(parent))
  commands.append('cp "$workshop_repo"/'+shlex.quote(f'data/{data_base}/{name}')+' "$practice_dir"/'+shlex.quote(name))
 commands.append('cd "$practice_dir"')
 invocation='tclsh "$workshop_repo"/'+shlex.quote(script)
 if spec.get('argv'):invocation+=' '+' '.join(shlex.quote(arg) for arg in spec['argv'])
 commands += [invocation,'# 生成文件留在 practice_dir；执行后回到仓库。','cd "$workshop_repo"']
 return details('本地准备与运行（Tcl 8.6+）',block('\n'.join(commands),'sh'))
def project_run(project,case_index=None):
 """Give each copied local run the same fresh files and argv as the browser."""
 n=project['id'];case=project['cases'][case_index] if case_index is not None else {}
 commands=['# 从本仓库根目录执行；每组运行使用一个新的临时练习目录。','workshop_repo="$PWD"','practice_dir="$(mktemp -d)"']
 fixtures=[(f'data/project-{n}/{name}',name) for name in project.get('files',{})]
 if case_index is not None:fixtures += [(f'data/project-{n}/case-{case_index+1}/{name}',name) for name in case.get('files',{})]
 for source,destination in fixtures:
  parent=Path(destination).parent.as_posix()
  if parent!='.':commands.append('mkdir -p "$practice_dir"/'+shlex.quote(parent))
  commands.append('cp "$workshop_repo"/'+shlex.quote(source)+' "$practice_dir"/'+shlex.quote(destination))
 commands.append('cd "$practice_dir"')
 script=f'projects/{n}/solution.tcl'
 if case_index is not None:
  commands.append('cat "$workshop_repo"/'+shlex.quote(script)+' "$workshop_repo"/'+shlex.quote(f'projects/{n}/case-{case_index+1}.tcl')+' > run.tcl')
  script='run.tcl'
  invocation='tclsh '+shlex.quote(script)
 else:invocation='tclsh "$workshop_repo"/'+shlex.quote(script)
 args=case.get('argv',project.get('argv',[]))
 if args:invocation+=' '+' '.join(shlex.quote(arg) for arg in args)
 commands += [invocation,'# 结果文件保存在上面的 practice_dir；运行结束后回到仓库。','cd "$workshop_repo"']
 return details('本地准备与运行（Tcl 8.6+）',block('\n'.join(commands),'sh'))
def main():
 lessons=[json.loads(p.read_text()) for p in sorted((ROOT/'lessons').glob('*.json'))]
 projects=[json.loads(p.read_text()) for p in sorted((ROOT/'projects').glob('*.json'))]
 if len(lessons)!=18 or len(projects)!=6:raise SystemExit(f'Need 18 lessons and 6 projects, found {len(lessons)} and {len(projects)}')
 for l in lessons:
  n=f'{l["id"]:02}';md=f'# {n} · {l["title"]}\n\n{l["summary"]}\n\n约 {l["minutes"]} 分钟。前置知识：'+'、'.join(l['prerequisites'])+'\n\n## 要解决的问题\n\n'+l['problem']+'\n\n## 学习目标\n\n'+'\n'.join('- '+x for x in l['objectives'])+f'\n\n![{l["title"]}示意图](../../site/{l["diagram"]})\n\n'
  for step in l['steps']:md+='## '+step['title']+'\n\n'+step['body']+'\n\n'
  for i,e in enumerate(l['examples'],1):
   base=f'lesson-{n}/example-{i}'
   md+=f'## 示例 {i} · {e["title"]}\n\n'+block(e['code'])+arguments(e)+project_files(e.get('files',{}),base)+'预期输出：\n\n'+block(e['expected'],'text')+lesson_run(e,f'examples/{n}/{i:02}.tcl',base)
   write(ROOT/f'examples/{n}/{i:02}.tcl',f'# {l["title"]} / {e["title"]}\n'+e['code']+'\n')
   for file,text in e.get('files',{}).items():write(ROOT/f'data/lesson-{n}/example-{i}'/file,text)
  md+='## 修改一个条件\n\n'+l['exploration']+'\n\n## 常见错误\n\n'
  for m in l['mistakes']:md+='- **'+m['problem']+'**：'+m['fix']+'\n'
  for i,e in enumerate(l['exercises'],1):
   base=f'lesson-{n}/exercise-{i}'
   md+=f'\n## 练习 {i} · {e["title"]}\n\n'+e['prompt']+'\n\n'+block(e['starter'])+arguments(e)+project_files(e.get('files',{}),base)+'目标输出：\n\n'+block(e['expected'],'text')+details('逐层提示','\n\n'.join(e['hints']))+details('参考答案',block(e['solution'])+lesson_run(e,f'solutions/{n}/{i:02}.tcl',base))
   write(ROOT/f'exercises/{n}/{i:02}.tcl',e['starter']+'\n');write(ROOT/f'solutions/{n}/{i:02}.tcl',e['solution']+'\n')
   for file,text in e.get('files',{}).items():write(ROOT/f'data/lesson-{n}/exercise-{i}'/file,text)
  md+='\n## 理解检查\n\n'
  for q in l['quiz']:md+=q['question']+'\n\n'+'\n'.join(f'{i+1}. {x}' for i,x in enumerate(q['options']))+'\n\n'+details('答案与解释',q['options'][q['answer']]+'。'+q['explanation'])
  md+='\n## 速查\n\n'+'\n'.join('- '+x for x in l['cheatsheet'])+'\n\n下一节：'+l['next']+'\n'
  write(ROOT/f'lessons/{n}/README.md',md)
 for p in projects:
  n=p['id'];md=f'# 项目 {n} · {p["title"]}\n\n{p["summary"]}\n\n## 需求\n\n'+'\n'.join('- '+x for x in p['requirements'])+'\n\n## 输入\n\n'+p['input']+'\n\n'
  md+='模拟参数（JSON 数组表示）：'+block('argv = '+json.dumps(p.get('argv',[]),ensure_ascii=False)+'\nargc = '+str(len(p.get('argv',[]))),'text')
  md+=project_files(p.get('files',{}),f'project-{n}')+project_run(p)+'\n## 起始代码\n\n'+block(p['starter'])+'## 输出样例\n\n'+block(p['expected'],'text')+details('分步提示','\n\n'.join(p['hints']))+details('完整参考实现',block(p['solution']))+'\n## 验证用例\n\n'
  md+='每个用例在新的解释器中先运行完整参考实现，再运行下列用例代码；下列预期输出仅对应第二段用例代码。本地运行命令会先显示参考实现的默认演示输出，再显示该用例的输出。用例继承上面的主预置文件，并添加或覆盖本节列出的文件。\n\n'
  for i,c in enumerate(p['cases']):
   md+='### '+c['title']+'\n\n'
   args=c.get('argv',p.get('argv',[]))
   md+='本组模拟参数：'+block('argv = '+json.dumps(args,ensure_ascii=False)+'\nargc = '+str(len(args)),'text')
   md+=project_files(c.get('files',{}),f'project-{n}/case-{i+1}')+block(c['code'])+'本组预期输出：\n\n'+block(c['expected'],'text')+project_run(p,i)+'\n'
   write(ROOT/f'projects/{n}/case-{i+1}.tcl',f'# Execute after the project implementation: {c["title"]}\n'+c['code']+'\n')
   for file,text in c.get('files',{}).items():write(ROOT/f'data/project-{n}/case-{i+1}'/file,text)
  md+='\n## 可以继续扩展\n\n'+'\n'.join('- '+x for x in p['extensions'])+'\n'
  write(ROOT/f'projects/{n}/README.md',md);write(ROOT/f'projects/{n}/starter.tcl',p['starter']+'\n');write(ROOT/f'projects/{n}/solution.tcl',p['solution']+'\n')
  for file,text in p.get('files',{}).items():write(ROOT/f'data/project-{n}'/file,text)
 docs={p.stem:p.read_text() for p in sorted((ROOT/'docs').glob('*.md')) if p.stem!='CONTENT_SCHEMA'}
 write(ROOT/'site/course.json',json.dumps({'units':UNITS,'lessons':lessons,'projects':projects,'docs':docs},ensure_ascii=False,indent=2)+'\n')
 hashes={p.relative_to(ROOT/'site').as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'site').rglob('*')) if p.is_file() and p.name not in {'assets.json','index.html'} and 'vendor' not in p.parts}
 write(ROOT/'site/assets.json',json.dumps(hashes,indent=2)+'\n')
 version=hashlib.sha256(json.dumps(hashes,sort_keys=True).encode()).hexdigest()[:12]
 template=(ROOT/'site/index.template.html').read_text();write(ROOT/'site/index.html',template.replace('@VERSION@',version))
 print(f'Generated {len(lessons)} lessons, {len(projects)} projects; assets {version}')
if __name__=='__main__':main()
