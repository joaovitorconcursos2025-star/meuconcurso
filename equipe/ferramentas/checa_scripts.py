import re,sys,subprocess
s=open(sys.argv[1],encoding='utf-8').read()
for i,(attrs,body) in enumerate(re.findall(r'<script([^>]*)>(.*?)</script>',s,re.S)):
    if 'src=' in attrs or 'application/json' in attrs or not body.strip(): continue
    ext='.mjs' if 'module' in attrs else '.js'
    f=f'/tmp/s{i}{ext}'; open(f,'w',encoding='utf-8').write(body)
    r=subprocess.run(['node','--check',f],capture_output=True,text=True)
    print(i,attrs.strip()[:30],len(body),'OK' if r.returncode==0 else 'ERRO '+r.stderr[:300])
