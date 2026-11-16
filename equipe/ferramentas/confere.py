#!/usr/bin/env python3
"""Confere questões contra o texto oficial. Uso: python3 equipe/ferramentas/confere.py arquivo.json
arquivo.json = lista de {text, options[4], correct, explanation, base:[[lei, artigo, trecho literal]], ausentes:[[lei, artigo, termo]]}
lei = lo | ri | est ; artigo como em equipe/fontes/leis.json (ex.: "Art. 9º", "Art. 44", "Art. 20-A").
Sai com código 1 se qualquer trecho de 'base' não existir literalmente no artigo, se um termo de 'ausentes'
aparecer no artigo, se a questão não tiver base, ou se já existir no conteudo.json (texto repetido)."""
import json,re,sys,os
R=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
norm=lambda s: re.sub(r'\s+',' ',str(s).replace('\n',' ')).strip()
leis=json.load(open(os.path.join(R,'equipe/fontes/leis.json'),encoding='utf-8'))
idx={k:{a['num']:norm(a['texto']) for a in v if a['tipo']=='artigo'} for k,v in leis.items()}
ja=set()
for p in json.load(open(os.path.join(R,'conteudo.json'),encoding='utf-8')):
    for q in p.get('questoes',[]): ja.add(norm(q.get('text','')).lower())
qs=json.load(open(sys.argv[1],encoding='utf-8')); bad=0
for i,q in enumerate(qs):
    e=[]
    if len(q.get('options',[]))!=4 or q.get('correct') not in (0,1,2,3): e.append('precisa de 4 alternativas e correct 0-3')
    if len(set(norm(o).lower() for o in q.get('options',[])))!=len(q.get('options',[])): e.append('alternativas repetidas')
    if not q.get('base'): e.append('sem base')
    if norm(q.get('text','')).lower() in ja: e.append('enunciado já existe no app')
    for lei,art,tre in q.get('base',[]):
        t=idx.get(lei,{}).get(art)
        if t is None: e.append(f'artigo não encontrado: {lei} {art}')
        elif norm(tre) not in t: e.append(f'trecho não está em {lei} {art}: {tre[:80]}')
    for lei,art,termo in q.get('ausentes',[]):
        t=idx.get(lei,{}).get(art,'')
        if norm(termo).lower() in t.lower(): e.append(f'termo do distrator aparece em {lei} {art}: {termo}')
    if e: bad+=1; print(f'[{i}] REPROVADA: '+' | '.join(e)+'\n     '+q.get('text','')[:110])
dist=[sum(1 for q in qs if q.get('correct')==k) for k in range(4)]
print(f'{len(qs)} questões · reprovadas {bad} · gabarito A-D {dist}')
sys.exit(1 if bad else 0)
