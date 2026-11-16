import json,re,sys,hashlib,random
sys.path.insert(0,'/home/claude/work'); from questoes_leg import Q
R='/home/claude/meuconcurso/'
leis=json.load(open('/home/claude/work/leis.json'))
TOP={'lo':'ttop_416','ri':'ttop_417','est':'ttop_418'}
NOME={'ttop_416':'Lei Orgânica do Município de Cristalina (nº 1/1990)','ttop_417':'Regimento Interno da Câmara Municipal de Cristalina','ttop_418':'Estatuto dos Servidores de Cristalina (Anexo I cita Lei 475/1971; item 1.4 cita Lei 1.207/1994)'}
RES={}
RES['ttop_416']="""### Lei Orgânica de Cristalina (nº 1/1990)
**Fonte:** texto consolidado publicado pela Câmara na página do concurso, atualizado até a **Emenda nº 31, de 11/08/2026**. Use só este texto: versões antigas na internet estão desatualizadas.

**Câmara Municipal**
| Ponto | Regra | Artigo |
|---|---|---|
| Número de Vereadores | **15** | 18 |
| Períodos de reunião | **2/fev a 30/jun** e **1º/ago a 15/dez** | 19 |
| Deliberações | maioria dos membros, salvo disposição em contrário | 20 |
| Sessões públicas | salvo deliberação de **2/3**, por motivo relevante | 23 |
| Abertura da sessão | presença mínima de **1/3** | 24 |
| Comissão especial de inquérito | requerimento de **1/3**, fato determinado, prazo certo | 27 |

- O **art. 26** (Mesa com mandato de 1 ano) foi **revogado**. O mandato da Mesa hoje está no Regimento Interno (2 anos).

**Processo legislativo (arts. 43 a 53)**
- Espécies: emendas à Lei Orgânica, leis complementares, leis ordinárias, leis delegadas, decretos legislativos e resoluções. **Não há medida provisória.**
- **Emenda à Lei Orgânica (art. 44):** proposta de **1/3** dos Vereadores, do **Prefeito** ou de **5% do eleitorado**; **dois turnos**, interstício mínimo de **10 dias**, aprovação por **2/3**. Promulgada pela Mesa da Câmara.
- **Iniciativa popular de lei (art. 45):** no mínimo **5%** dos eleitores do Município.
- **Sanção e veto (art. 50):** projeto enviado ao Prefeito em **5 dias úteis**; sanção em **15 dias corridos**; veto em **15 dias úteis**, com motivos comunicados em **48 horas**; silêncio importa sanção.
- Projeto rejeitado só volta na mesma sessão legislativa por proposta da **maioria absoluta** (art. 53).

**Prefeito (arts. 57 a 64)**
- Posse em **1º de janeiro**, em sessão solene da Câmara.
- Substituição: Vice-Prefeito; depois, **Presidente da Câmara**.
- Vacância sem Vice: nos **3 primeiros anos**, eleição em **90 dias**; no **último ano**, assume o Presidente da Câmara e completa o período (art. 62).
- Ausência do Município por mais de **15 dias** exige licença da Câmara (art. 64).

**Servidores:** estabilidade após **3 anos** de efetivo exercício (art. 83).

**Como a banca erra você:** troca 1/3 por maioria absoluta, 2/3 por 3/5 (quórum da CF), e usa o calendário do Congresso (17/jul e 22/dez) no lugar do de Cristalina."""
RES['ttop_417']="""### Regimento Interno da Câmara de Cristalina
**Fonte:** **Resolução nº 226, de 3 de julho de 2026**, publicada pela Câmara na página do concurso. É um regimento **novo**: material anterior a julho de 2026 não serve.

**Legislatura e posse**
- Legislatura de quatro anos, dividida em quatro sessões legislativas (art. 3º).
- Posse dos Vereadores com **1/3** da edilidade presente, sob a presidência do **mais votado** entre os presentes (art. 4º).
- Quem não tomou posse tem **15 dias**, contados do início do funcionamento normal da Câmara (art. 6º).

**Mesa Diretora (arts. 8º a 13)**
- Cargos: Presidente, Vice-Presidente, Primeiro e Segundo Secretário, que se substituem na **ordem inversa**.
- Mandato de **2 anos** (biênio); **vedada a reeleição para o mesmo cargo**, ressalvado o Ato das Disposições Transitórias.
- Eleição por votação **pública e nominal, cargo a cargo**, por **maioria absoluta** no 1º escrutínio; no 2º, entre os dois mais votados, por maioria simples. Empate: **mais idoso**.
- Suplente de Vereador não pode ser eleito para a Mesa, salvo substituição em caráter definitivo (art. 12).

**Comissões Permanentes (art. 37): são três**
1. Constituição, Legislação, Justiça e Redação Final;
2. Orçamento, Finanças e Tributação;
3. Obras, Bens e Serviços Públicos.

**Reuniões ordinárias (art. 143)**
- No mínimo **5 por mês**, até **3 horas**, início às **9 horas**, preferencialmente às **quintas-feiras**.

**Discussão e votação**
- Discussão só com **maioria absoluta** presente (art. 162, § 1º).
- **Turno único:** urgência, vetos, requerimentos, emendas e subemendas, moções, decretos legislativos e resoluções, entre outros (art. 162, § 2º).
- O segundo turno **nunca** ocorre na mesma reunião do primeiro (art. 163).
- O Vereador presente não pode se recusar a votar, mas deve **abster-se** se tiver interesse pessoal; sua presença conta para o quórum (art. 169).
- O voto é **sempre público** (art. 170, parágrafo único).
- Deliberações por maioria simples, maioria absoluta ou 2/3 (art. 171).

**Como a banca erra você:** troca "mais votado" por "mais idoso" na posse, "pública e nominal" por "secreta" na eleição da Mesa, e 2 anos por 1 ano no mandato."""
RES['ttop_418']="""### Estatuto dos Servidores de Cristalina (Lei nº 1.207/1994)
**Atenção ao edital:** o Anexo I citava a Lei nº 475/1971, mas a **Retificação I** trocou para a **Lei Municipal nº 1.207/94**. É ela que cai. O texto do app é o publicado pela Câmara, já sem as redações revogadas.

**Provimento e vacância**
| Tema | Regra | Artigo |
|---|---|---|
| Requisitos de ingresso | brasileiro, direitos políticos, **18 anos**, obrigações militares e eleitorais, saúde física e mental, condições legais do cargo | 6º |
| Formas de provimento | nomeação, recondução, readaptação, reversão, reintegração, aproveitamento, promoção, **transferência** | 7º |
| Validade do concurso | **até 2 anos**, prorrogável uma vez por igual período | 9º |
| Posse | **até 15 dias** da publicação da nomeação, prorrogável por igual período | 12 |
| Exercício | **5 dias**, contados da posse | 13 |
| Estabilidade | **3 anos** de efetivo exercício + avaliação especial de desempenho | 18 |
| Estágio probatório | **3 anos**; regras detalhadas nos arts. 20-A a 20-Y | 20 |
| Vacância | exoneração, demissão, readaptação, recondução, aposentadoria, falecimento, promoção | 33 |

- O servidor estável só perde o cargo por sentença judicial transitada em julgado, processo administrativo disciplinar com ampla defesa ou avaliação periódica de desempenho (art. 19).

**Licenças**
- Gestante: **180 dias** consecutivos (art. 220).
- Adotante: **90 dias** para criança de até 1 ano (art. 221).
- Paternidade: **5 dias** (art. 222).
- A licença para tratamento de saúde saiu do Estatuto: os arts. 215 a 219 foram revogados pela Lei nº 1.842/2007.

**Regime disciplinar**
- Penalidades (art. 148): advertência, suspensão, demissão, cassação de aposentadoria e disponibilidade, destituição de cargo ou função de confiança.
- Prescrição (art. 165): **5 anos** para demissão, cassação e destituição; **180 dias** para advertência ou suspensão. Conta da data em que a autoridade toma conhecimento da falta.

**Diferenças para a Lei federal 8.112/1990 (a banca explora):**
| Tema | Cristalina (1.207/94) | Federal (8.112/90) |
|---|---|---|
| Posse | 15 dias | 30 dias |
| Exercício | 5 dias | 15 dias |
| Prescrição de advertência | 180 dias | 180 dias |
| Prescrição de suspensão | 180 dias | 2 anos |"""
# leis: marca artigos revogados cuja nota ficou no artigo anterior
def stubs(itens,prefix):
    out=[]; seq=[i for i in itens]
    for i,it in enumerate(seq):
        out.append(it)
    return out
META={'lo':dict(ref='lo',nome='Lei Orgânica do Município de Cristalina',desc='Lei Orgânica nº 1/1990 · consolidada até a Emenda nº 31/2026 · cai inteira (Legislação Específica)',icon='🏛️',ordem=8,
        fonte='Texto consolidado publicado pela Câmara Municipal na página do concurso (cristalina.go.leg.br/concurso-publico), arquivo LEI-ORGANICA-CONSOLIDADA.pdf, obtido em 16/11/2026, sem as redações riscadas (revogadas).'),
      'ri':dict(ref='ri',nome='Regimento Interno da Câmara de Cristalina',desc='Resolução nº 226, de 3/7/2026 · cai inteiro (Legislação Específica)',icon='📕',ordem=9,
        fonte='Texto publicado pela Câmara Municipal na página do concurso (cristalina.go.leg.br/concurso-publico), arquivo REGIMENTO-INTERNO-1-atualizado-2026.pdf, obtido em 16/11/2026.'),
      'est':dict(ref='est',nome='Estatuto dos Servidores de Cristalina (Lei 1.207/1994)',desc='Lei Municipal nº 1.207/1994 · indicada pela Retificação I · cai inteira (Legislação Específica)',icon='👔',ordem=10,
        fonte='Texto publicado pela Câmara Municipal na página do concurso (cristalina.go.leg.br/concurso-publico), arquivo Lei1207.pdf, obtido em 16/11/2026, sem as redações riscadas (revogadas).')}
pl=[]
for k in ('lo','ri','est'):
    m=dict(META[k]); m['materiaRef']='mmat_37'; m['topicoRefs']=[TOP[k]]
    m['itens']=[dict(ref=i['ref'],tipo=i['tipo'],num=i['num'],texto=i['texto'],paiRef=i['paiRef']) for i in leis[k]]
    pl.append(m)
qs=[]
for n,q in enumerate(Q):
    rnd=random.Random(1000+n); opts=[q['certa']]+q['erradas']; order=[0,1,2,3]; rnd.shuffle(order)
    options=[opts[i] for i in order]; correct=order.index(0)
    exp=q['exp']
    if 'Confira o rol completo no leitor de leis.' in exp: exp=exp.replace('gozar de boa saúde física e mental. Confira o rol completo no leitor de leis.','gozar de boa saúde física e mental, comprovada mediante exame médico; e ter atendido as condições legais exigidas para o cargo.')
    qs.append(dict(materiaRef='mmat_37',topicoRef=TOP[q['lei']],subtopicoRef='',tipo='abcd',text=q['text'],options=options,correct=correct,veCorrect=1,
        explanation=exp,banca='Inédita · padrão Consulplan · conferida no texto oficial',ano=2026,nivel='medio',assunto={'lo':'Lei Orgânica de Cristalina','ri':'Regimento Interno da Câmara','est':'Estatuto dos Servidores (Lei 1.207/1994)'}[q['lei']]))
pack=dict(formato='meu-concurso-pacote',versao=3,id='cristalina-legislacao-especifica-v1',titulo='Legislação Específica de Cristalina (leis oficiais, resumos e questões)',
  concurso=dict(name='Câmara de Cristalina — Analista de RH',icon='🏛️',desc='Edital nº 1/2026 · Instituto Consulplan · prova à tarde (portões 14h)',dataProva='2026-12-20'),
  materias=[dict(ref='mmat_37',name='Legislação Específica',icon='🏛️',desc='10 questões · 10 pts')],
  topicos=[dict(ref=r,materiaRef='mmat_37',nome=NOME[r],subtopicos=[],resumo=RES[r]) for r in ('ttop_416','ttop_417','ttop_418')],
  questoes=qs,leis=pl)
d=json.load(open(R+'conteudo.json',encoding='utf-8'))
d=[p for p in d if p['id']!=pack['id']]+[pack]
txt=json.dumps(d,ensure_ascii=False,separators=(',',':'))
open(R+'conteudo.json','w',encoding='utf-8').write(txt)
h=hashlib.md5(txt.encode()).hexdigest()[:10]
html=open(R+'index.html',encoding='utf-8').read()
m=re.search(r'(<script type="application/json" id="mc-conteudo-idx" data-v=")([0-9a-f]+)(">)(.*?)(</script>)',html,re.S)
idx=json.loads(m.group(4)); idx=[x for x in idx if x['id']!=pack['id']]+[dict(id=pack['id'],conc=pack['concurso']['name'],soAdmin=False,criar=False)]
html=html[:m.start()]+m.group(1)+h+m.group(3)+json.dumps(idx,ensure_ascii=False)+m.group(5)+html[m.end():]
open(R+'index.html','w',encoding='utf-8').write(html)
print('pacote ok:',len(qs),'questões,',len(pl),'leis,',sum(len(l['itens']) for l in pl),'itens; conteudo.json',len(txt)//1024,'KB; data-v',h, 'dist gabarito',[sum(1 for q in qs if q['correct']==i) for i in range(4)])
