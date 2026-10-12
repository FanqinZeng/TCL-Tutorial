import argparse,http.server,os
from pathlib import Path
a=argparse.ArgumentParser();a.add_argument('--port',type=int,default=8765);a.add_argument('--host',default='127.0.0.1');args=a.parse_args()
os.chdir(Path(__file__).resolve().parents[1]/'site')
print(f'Local: http://{args.host}:{args.port}/',flush=True)
http.server.ThreadingHTTPServer((args.host,args.port),http.server.SimpleHTTPRequestHandler).serve_forever()
