import os,re,sys,subprocess,tempfile
s=open(sys.argv[1],encoding='utf-8').read(); erros=0
for i,(attrs,body) in enumerate(re.findall(r'<script([^>]*)>(.*?)</script>',s,re.S)):
    if 'src=' in attrs or 'application/json' in attrs or not body.strip(): continue
    ext='.mjs' if 'module' in attrs else '.js'
    f=os.path.join(tempfile.gettempdir(),f's{i}{ext}'); open(f,'w',encoding='utf-8').write(body)
    r=subprocess.run(['node','--check',f],capture_output=True,text=True)
    erros+=r.returncode!=0
    print(i,attrs.strip()[:30],len(body),'OK' if r.returncode==0 else 'ERRO '+r.stderr[:300])
sys.exit(1 if erros else 0)
