"""Check completeness and actual cross-file links; execution tests are separate."""
import hashlib,json,re,xml.etree.ElementTree as ET
from pathlib import Path
R=Path(__file__).resolve().parents[1]
lessons=[json.loads(p.read_text()) for p in sorted((R/'lessons').glob('*.json'))];projects=[json.loads(p.read_text()) for p in sorted((R/'projects').glob('*.json'))]
assert [x['id'] for x in lessons]==list(range(1,19))
assert [x['id'] for x in projects]==list('ABCDEF')
for l in lessons:
 assert len(l['examples'])>=3 and len(l['exercises'])>=3 and len(l['quiz'])>=2 and len(l['mistakes'])>=2
 assert 3<=len(l['objectives'])<=5 and l['problem'] and l['steps'] and l['exploration'] and l['cheatsheet']
 for e in l['examples']:assert e['code'] and 'expected' in e
 for e in l['exercises']:assert e['starter'] and e['solution'] and len(e['hints'])>=2 and e['checks']
 assert (R/f'lessons/{l["id"]:02}/README.md').is_file()
for p in projects:assert p['solution'] and p['starter'] and len(p['cases'])>=3 and len(p['hints'])>=3 and p['requirements']
for x in lessons+projects:
 path=R/'site'/x['diagram'];tree=ET.parse(path);root=tree.getroot();ns={'s':'http://www.w3.org/2000/svg'}
 assert root.find('s:title',ns) is not None and root.find('s:desc',ns) is not None and 'viewBox' in root.attrib
for name,digest in json.loads((R/'site/vendor/SHA256.json').read_text()).items():assert hashlib.sha256((R/'site/vendor'/name).read_bytes()).hexdigest()==digest,name
for n in range(1,7):
 for ext in ['mp4','png','txt','vtt']:assert (R/f'site/media/unit-{n}.{ext}').is_file(),f'video {n} {ext}'
for p in (R/'site').glob('*.js'):
 for rel in re.findall(r"(?:from\s+|importScripts\()['\"]([^'\"]+)['\"]",p.read_text()):
  assert (p.parent/rel).is_file(),rel
assert json.loads((R/'site/course.json').read_text())['lessons']==lessons
assert not re.search(r'(https?://[^\s"\']+\.js)',(R/'site/index.html').read_text())
print(f'PASS: {len(lessons)} complete lessons, {sum(len(l["examples"]) for l in lessons)} examples, {sum(len(l["exercises"]) for l in lessons)} exercises, {len(projects)} projects, 24 SVGs, 6 video sets, local runtime hashes')
