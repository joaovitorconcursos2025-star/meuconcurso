import re,json,sys
F='/home/claude/fontes/'
HEAD=re.compile(r'^(T[ÍI]TULO|CAP[ÍI]TULO|SE[ÇC][ÃA]O|Se[çc][ãa]o|LIVRO|SUBSE[ÇC][ÃA]O|Subse[çc][ãa]o)\s+([IVXLC]+|[ÚU]NIC[AO]|Única|Único)\b\s*(.*)$')
ART=re.compile(r'^Art\.\s?(\d+)(?:[ºo°]|\.(?=\s)|(?=\s?[-–][A-Z]\b)|(?=\s[A-ZÉÀÁÓ]))\s?([-–][A-Z]\b)?\.?\s*(.*)$')
NIV={'LIVRO':0,'TITULO':1,'CAPITULO':2,'SECAO':3,'SUBSECAO':4}
def nk(s):
    s=s.upper().replace('Í','I').replace('Ç','C').replace('Ã','A'); return s
def parse(raw,prefix,start_pat,end_pat=None,first=False):
    lines=open(F+raw,encoding='utf-8').read().replace('\f','\n').split('\n')
    # start: last occurrence index of start pattern line (after sumário)
    idxs=[i for i,l in enumerate(lines) if re.match(start_pat,l.strip())]
    s=idxs[0] if first else idxs[-1]
    lines=lines[s:]
    if end_pat:
        e=[i for i,l in enumerate(lines) if re.match(end_pat,l.strip())]
        if e: lines=lines[:e[0]]
    itens=[]; stack=[]; cur=None; pend=None; n=0; last_art=0; adt=''
    def push(tipo,num,pai):
        nonlocal n; n+=1; it={'ref':f'{prefix}_{n}','tipo':tipo,'num':num,'texto':'','paiRef':pai}; itens.append(it); return it
    for l in lines:
        t=l.strip()
        if not t or re.fullmatch(r'\d{1,3}',t): continue
        if re.match(r'^(ATO DAS DISPOSI[ÇC][ÕO]ES|DAS DISPOSI[ÇC][ÕO]ES GERAIS E TRANSIT)',t) and last_art>100:
            stack=[]; it=push('titulo','ATO DAS DISPOSIÇÕES TRANSITÓRIAS',None); stack.append((0,it['ref'])); last_art=0; adt='ADT · '; cur=None; pend=None; continue
        m=HEAD.match(t)
        if m and (len(t)<90):
            kind=nk(m.group(1)); lv=NIV[kind]
            while stack and stack[-1][0]>=lv: stack.pop()
            it=push('titulo',(m.group(1).upper()+' '+m.group(2)).strip(), stack[-1][1] if stack else None)
            if m.group(3): it['num']+=' — '+m.group(3).strip(); pend=None
            else: pend=it
            stack.append((lv,it['ref'])); cur=None; continue
        a=ART.match(t)
        if a and int(a.group(1))>=1 and ((last_art<=int(a.group(1))<=last_art+12 and last_art>0 and (int(a.group(1))>last_art or a.group(2))) or (last_art==0 and int(a.group(1))==1)):
            last_art=int(a.group(1)); pend=None
            num=adt+'Art. '+a.group(1)+('º' if int(a.group(1))<10 else '')+(a.group(2) or '').replace('–','-')
            cur=push('artigo',num, stack[-1][1] if stack else None); cur['texto']=a.group(3); continue
        if pend is not None and not re.match(r'^(§|Par[áa]grafo|[IVXLC]+\s*[-–]|[a-z]\))',t):
            pend['num']+=(' — ' if '—' not in pend['num'] else ' ')+t
            if 'ransit' in t and last_art>100 and prefix=='lo': last_art=0; adt='Disp. Transitórias · '
            continue
        pend=None
        if cur is None: continue
        if re.match(r'^(§\s?\d|Par[áa]grafo [úu]nico|[IVXLC]+\s*[-–—]\s|[a-z]\)\s)',t): cur['texto']+='\n'+t
        else: cur['texto']+=(' ' if cur['texto'] and not cur['texto'].endswith('-') else '')+t
    for it in itens: it['texto']=re.sub(r'[ \t]+',' ',it['texto']).strip()
    return itens
out={}
out['lo']=parse('lo.clean.txt','lo',r'^T[ÍI]TULO I$',r'^Sala das Sess',first=False)
out['ri']=parse('ri.clean.txt','ri',r'^T[ÍI]TULO I$',r'^(Sala das Sess|CERTID[ÃA]O)',first=False)
out['est']=parse('est.clean.txt','est',r'^T[ÍI]TULO I$',r'^Sala das Sess',first=True)
for k,v in out.items():
    arts=[i for i in v if i['tipo']=='artigo']; tit=[i for i in v if i['tipo']=='titulo']
    nums=[int(re.search(r'\d+',a['num']).group()) for a in arts]
    print(k,'itens',len(v),'artigos',len(arts),'titulos',len(tit),'ultimo',arts[-1]['num'],'chars',sum(len(i['texto']) for i in v),'vazios',sum(1 for a in arts if len(a['texto'])<15))
    print('  primeiros titulos:',[t['num'][:60] for t in tit[:6]])
    print('  ', arts[0]['num'], arts[0]['texto'][:150].replace('\n',' / '))
    print('  ', arts[-1]['num'], arts[-1]['texto'][:200].replace('\n',' / '))
json.dump(out,open('/home/claude/work/leis.json','w'),ensure_ascii=False)
