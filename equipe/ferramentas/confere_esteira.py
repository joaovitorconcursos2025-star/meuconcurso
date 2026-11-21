#!/usr/bin/env python3
"""Conferidor da Esteira (todas as matérias). Uso:
    python equipe/ferramentas/confere_esteira.py questoes.json revisor.json
    python equipe/ferramentas/confere_esteira.py --teste        (autoteste)

questoes.json = lista de questões:
  {id, materiaRef, topicoRef, text, options[4], correct(0-3), explanation, banca,
   modelo: {orgao, cargo, ano, url},                     # prova real da Consulplan que serviu de modelo
   base: [ ... pelo menos uma prova do gabarito ... ],
   ausentes: [{lei, artigo, termo}]}                     # opcional: termo do distrator que NÃO pode estar no artigo
  Tipos de base:
   {"tipo":"lei",   "lei":"lo|ri|est|<federal>", "artigo":"Art. 37", "trecho":"literal"}
        municipal: equipe/fontes/leis.json · federal: equipe/fontes/federal/<lei>.txt (texto do Planalto)
   {"tipo":"conta", "expr":"2000*0.015*8"}               # recalculada; tem de dar o número da correta e de nenhuma errada
   {"tipo":"regra", "fonte":"...", "url":"https://...", "regra":"..."}   # Português, Cargo, Informática
revisor.json = {"<id>": índice que o revisor marcou SEM ver gabarito nem comentário}

Reprova (código de saída 1) se: formato errado; sem base; sem modelo/link; trecho de lei fora do artigo;
termo de distrator presente no artigo; conta que não fecha; revisor discordou ou não respondeu;
enunciado igual/quase igual a outro do app ou do próprio lote. Também reprova o lote se uma letra concentrar > 40% do gabarito."""
import ast, difflib, json, operator, os, re, sys

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
norm = lambda s: re.sub(r'\s+', ' ', str(s).replace('\n', ' ')).strip()
low = lambda s: norm(re.sub(r'<[^>]+>', '', str(s))).lower()

# ── leis ────────────────────────────────────────────────────────────────
def _municipais():
    p = os.path.join(R, 'equipe/fontes/leis.json')
    if not os.path.exists(p): return {}
    return {k: {a['num']: norm(a['texto']) for a in v if a.get('tipo') == 'artigo'} for k, v in json.load(open(p, encoding='utf-8')).items()}
MUN = _municipais()
_FED = {}
def artigo(lei, art):
    """Texto do artigo, ou None. Federal: corta o .txt do Planalto entre 'Art. N' e o próximo 'Art.'."""
    if not isinstance(lei, str) or not isinstance(art, str) or not re.fullmatch(r'[a-z0-9_-]{1,40}', lei): return None  # nada de ../
    if lei in MUN: return MUN[lei].get(art)
    if lei not in _FED:
        p = os.path.join(R, 'equipe/fontes/federal', lei + '.txt')
        _FED[lei] = open(p, encoding='utf-8').read() if os.path.exists(p) else None
    t = _FED[lei]
    if t is None: return None
    n = re.match(r'Art\.?\s*(\d+)\s*[º°o]?\s*(?:-\s*([A-Z])\b)?', art.strip(), re.I)
    if not n: return None
    suf = r'\s*-\s*' + n.group(2).upper() if n.group(2) else r'(?!\s*-\s*[A-Z])'
    # só "Art." no começo da linha: citação no meio do texto ("conforme o Art. 370") não conta
    m = re.search(r'(?m)^[ \t]*Art\.\s*' + n.group(1) + r'(?!\d)\s*[º°o]?' + suf, t)
    if not m: return None
    fim = re.search(r'(?m)^[ \t]*Art\.\s*\d', t[m.end():])
    return norm(t[m.start(): m.end() + fim.start()] if fim else t[m.start():])

# ── contas ──────────────────────────────────────────────────────────────
OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv,
       ast.Pow: operator.pow, ast.FloorDiv: operator.floordiv, ast.Mod: operator.mod, ast.USub: operator.neg, ast.UAdd: operator.pos}
def calcula(expr):
    """Só aritmética (números, + - * / ** // %, parênteses). Nada de nomes ou chamadas."""
    if not isinstance(expr, str) or len(expr) > 200: raise ValueError('expressão longa demais')
    def cabe(v):
        if isinstance(v, int) and v.bit_length() > 4096: raise ValueError('número grande demais')
        return v
    def ev(n):
        if isinstance(n, ast.Expression): return ev(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool): return n.value
        if isinstance(n, ast.BinOp) and type(n.op) in OPS:
            l, r = ev(n.left), ev(n.right)  # uma vez só: avaliar de novo dobra o custo a cada ** aninhado
            if isinstance(n.op, ast.Pow) and abs(r) > 100: raise ValueError('expoente grande demais')
            return cabe(OPS[type(n.op)](l, r))
        if isinstance(n, ast.UnaryOp) and type(n.op) in OPS: return OPS[type(n.op)](ev(n.operand))
        raise ValueError('expressão não permitida')
    return ev(ast.parse(expr, mode='eval'))
def numero(txt):
    """Primeiro número da alternativa: '1.210,00' → 1210 · '12,68%' → 12.68 · '1/3' → 0.333…"""
    s = re.sub(r'<[^>]+>', '', str(txt))[:300]
    m = re.search(r'-?\d{1,3}(?:\.\d{3})+(?:,\d+)?|-?\d+(?:,\d+)?', s)
    f = re.search(r'(-?\d+\s+)?(-?\d+)\s*/\s*(\d+)(?:\s+de\s+(\d+(?:,\d+)?))?', s)
    if f and (not m or f.start() <= m.start()):
        if int(f.group(3)) == 0: return None
        v = int(f.group(2)) / int(f.group(3))
        if f.group(1): v += int(f.group(1))                       # misto: 3 1/2 → 3,5
        if f.group(4): v *= float(f.group(4).replace(',', '.'))   # 2/3 de 90 → 60
        return v
    return float(m.group(0).replace('.', '').replace(',', '.')) if m else None
igual = lambda a, b: a is not None and b is not None and abs(a - b) <= max(0.005, abs(b) * 0.0005)

# ── banco existente ─────────────────────────────────────────────────────
def banco():
    p = os.path.join(R, 'conteudo.json')
    return [(low(q.get('text', '')), cheio(q)) for pk in json.load(open(p, encoding='utf-8')) for q in pk.get('questoes', [])] if os.path.exists(p) else []

cheio = lambda q: low(q.get('text', '')) + ' || ' + ' | '.join(low(o) for o in q.get('options', []))

def confere(qs, rev, ja):
    """ja = textos (ou pares texto, texto+alternativas) que já estão no app."""
    ja = [x if isinstance(x, tuple) else (x, x) for x in ja]
    bad, vistos, vistos_cheio, jaset = 0, [], [], {t for t, _ in ja}
    for i, q in enumerate(qs):
        e, qid = [], str(q.get('id', i))
        ops = q.get('options', [])
        if len(ops) != 4 or q.get('correct') not in (0, 1, 2, 3): e.append('precisa de 4 alternativas e correct 0-3')
        elif len({low(o) for o in ops}) != 4: e.append('alternativas repetidas')
        for k in ('materiaRef', 'topicoRef', 'text', 'explanation', 'banca'):
            if not q.get(k): e.append('falta ' + k)
        mo = q.get('modelo') or {}
        if not all(mo.get(k) for k in ('orgao', 'cargo', 'ano', 'url')) or not str(mo.get('url', '')).startswith('http'):
            e.append('falta modelo (órgão, cargo, ano e link da prova Consulplan)')
        if not q.get('base'): e.append('sem base que comprove o gabarito')
        for b in q.get('base') or []:
            if not isinstance(b, dict): e.append('base mal formada'); continue
            t = b.get('tipo')
            if t == 'lei':
                a = artigo(b.get('lei', ''), b.get('artigo', ''))
                if not norm(b.get('trecho', '')): e.append('base lei sem trecho literal')
                elif a is None: e.append(f"artigo não encontrado: {b.get('lei')} {b.get('artigo')} (salve o texto oficial em equipe/fontes)")
                elif norm(b.get('trecho', '')) not in a: e.append(f"trecho não está em {b.get('lei')} {b.get('artigo')}: {str(b.get('trecho'))[:70]}")
            elif t == 'conta':
                try:
                    v = calcula(b.get('expr', ''))
                    if len(ops) != 4 or q.get('correct') not in (0, 1, 2, 3): pass
                    elif not igual(numero(ops[q['correct']]), v): e.append(f"conta {b.get('expr')} = {v:.4g} não bate com a correta")
                    elif any(igual(numero(o), v) for j, o in enumerate(ops) if j != q['correct']): e.append('uma alternativa errada também dá o resultado da conta')
                except Exception as x: e.append(f'conta inválida: {x}')
            elif t == 'regra':
                if not (b.get('regra') and b.get('fonte') and str(b.get('url', '')).startswith('http')): e.append('base regra precisa de regra, fonte e url')
            else: e.append(f'tipo de base desconhecido: {t}')
        for a_ in q.get('ausentes') or []:
            a = artigo(a_.get('lei', ''), a_.get('artigo', '')) if isinstance(a_, dict) else None
            if a is None: e.append(f"ausentes: artigo não encontrado: {a_}"); continue
            if low(a_.get('termo', '')) and low(a_.get('termo', '')) in a.lower(): e.append(f"termo do distrator aparece no artigo: {a_.get('termo')}")
        r = rev.get(qid)
        if r is None: e.append('revisor não respondeu')
        elif r != q.get('correct'): e.append(f"revisor marcou {'ABCD'[r] if r in (0,1,2,3) else r}, gabarito {'ABCD'[q['correct']] if q.get('correct') in (0,1,2,3) else '?'}")
        tx = low(q.get('text', ''))
        if tx in jaset or tx in vistos: e.append('enunciado já existe (no app ou no lote)')
        else:
            # quase igual = enunciado E alternativas parecidos (gêmeas de Português repetem a frase de comando)
            c = cheio(q)
            parecida = next((o for o in vistos_cheio + [c_ for _, c_ in ja] if len(tx) > 40 and difflib.SequenceMatcher(None, c, o).ratio() > 0.9), None)
            if parecida: e.append('questão quase igual a outra: ' + parecida[:60])
            vistos_cheio.append(c)
        vistos.append(tx)
        if e: bad += 1; print(f'[{qid}] REPROVADA: ' + ' | '.join(e) + '\n     ' + norm(q.get('text', ''))[:110])
    dist = [sum(1 for q in qs if q.get('correct') == k) for k in range(4)]
    concentrado = len(qs) >= 5 and max(dist) > 0.4 * len(qs)
    print(f"{len(qs)} questões · reprovadas {bad} · gabarito A-D {dist}" + (' · REPROVADO: gabarito concentrado' if concentrado else ''))
    return bad == 0 and not concentrado

def _teste():
    base_ok = {'materiaRef': 'm', 'topicoRef': 't', 'explanation': 'x', 'banca': 'Inédita',
               'modelo': {'orgao': 'Câmara X', 'cargo': 'Técnico', 'ano': '2024', 'url': 'https://exemplo/prova.pdf'}}
    boa = dict(base_ok, id='a', text='Um capital de R$ 2.000,00 a juros simples de 1,5% ao mês por 8 meses rende', options=['R$ 200,00', 'R$ 240,00', 'R$ 260,00', 'R$ 300,00'], correct=1, base=[{'tipo': 'conta', 'expr': '2000*0.015*8'}])
    conta_errada = dict(boa, id='b', text='Outro enunciado de juros bem diferente do primeiro para teste', correct=2)
    regra = dict(base_ok, id='c', text='Assinale a frase corretamente pontuada segundo a norma-padrão vigente', options=['a', 'b', 'c', 'd'], correct=3, base=[{'tipo': 'regra', 'fonte': 'Bechara', 'url': 'https://x', 'regra': 'aposto entre vírgulas'}])
    sem_modelo = dict(regra, id='d', text='Questão sem modelo de prova real para testar a reprovação', modelo={})
    repetida = dict(regra, id='e')
    assert calcula('(1+0.01)**12-1') > 0.1268 and numero('12,68%') == 12.68 and numero('R$ 1.210,00') == 1210 and abs(numero('1/3') - 1/3) < 1e-9
    try: calcula('__import__("os")'); raise AssertionError('deveria barrar nome')
    except ValueError: pass
    rev = {'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 3}
    assert confere([boa], rev, []) is True
    for q, motivo in ((conta_errada, 'conta'), (sem_modelo, 'modelo'), (dict(regra, id='f'), 'revisor')):
        assert confere([q], rev, []) is False, motivo
    assert confere([regra, repetida], rev, []) is False, 'repetida no lote'
    assert confere([regra], {'c': 0}, []) is False, 'revisor discordou'
    assert confere([regra], rev, [low(regra['text'])]) is False, 'já no app'
    if 'lo' in MUN:  # lei municipal real do repositório
        lei = dict(regra, id='g', text='Número de vereadores segundo a Lei Orgânica de Cristalina hoje', base=[{'tipo': 'lei', 'lei': 'lo', 'artigo': 'Art. 18', 'trecho': 'fica fixado em 15 (quinze)'}])
        assert confere([lei], {'g': 3}, []) is True
        assert confere([dict(lei, base=[{'tipo': 'lei', 'lei': 'lo', 'artigo': 'Art. 18', 'trecho': 'fica fixado em 13 (treze)'}])], {'g': 3}, []) is False, 'trecho falso'
    # achados dos revisores (21/11): um caso para cada
    assert numero('2/3 de 90') == 60 and numero('3 1/2') == 3.5 and numero('1/0') is None
    import time; t0 = time.time(); assert calcula('1**(' * 25 + '1' + ')' * 25) == 1 and time.time() - t0 < 1, 'pow aninhado lento'
    for ruim in ('((9**99)**99)**99', '1+' * 150 + '1'):
        try: calcula(ruim); raise AssertionError('deveria barrar: ' + ruim[:20])
        except ValueError: pass
    assert artigo('../../conteudo', 'Art. 1') is None and artigo(['lo'], 'Art. 1') is None
    vazio = dict(regra, id='h', text='Trecho vazio não pode servir de prova do gabarito da questão', base=[{'tipo': 'lei', 'lei': 'lo', 'artigo': 'Art. 18', 'trecho': ''}])
    assert confere([vazio], {'h': 3}, []) is False, 'trecho vazio'
    fantasma = dict(regra, id='i', text='Distrator conferido em artigo que não existe na lei citada', ausentes=[{'lei': 'lo', 'artigo': 'Art. 9999', 'termo': 'x'}])
    assert confere([fantasma], {'i': 3}, []) is False, 'ausentes sem artigo'
    assert confere([dict(regra, id='j', base=['lixo'])], {'j': 3}, []) is False, 'base mal formada'
    gemea = dict(regra, id='k', text=regra['text'] + ' hoje', options=['O diretor, assinou a portaria ontem.', 'Os servidores que faltaram, serão advertidos.', 'Maria, a secretária, protocolou o ofício.', 'Ele disse, que viria amanhã cedo.'])
    assert confere([regra, gemea], {'c': 3, 'k': 3}, []) is True, 'gêmea com alternativas novas passa'
    assert confere([regra, dict(gemea, options=regra['options'])], {'c': 3, 'k': 3}, []) is False, 'cópia quase igual barra'
    fed = os.path.join(R, 'equipe/fontes/federal', '_teste_tmp.txt')
    os.makedirs(os.path.dirname(fed), exist_ok=True)
    open(fed, 'w', encoding='utf-8').write('Art. 1º Conforme o Art. 5º, nada.\nArt. 5º Texto do cinco.\nArt. 5º-A Texto do cinco-A.\nArt. 6º Seis.\n')
    try:
        assert artigo('_teste_tmp', 'Art. 5º') == 'Art. 5º Texto do cinco.', artigo('_teste_tmp', 'Art. 5º')
        assert artigo('_teste_tmp', 'Art. 5º-A') == 'Art. 5º-A Texto do cinco-A.', artigo('_teste_tmp', 'Art. 5º-A')
        assert artigo('_teste_tmp', 'Art. 6') == 'Art. 6º Seis.'
    finally:
        os.remove(fed); _FED.pop('_teste_tmp', None)
    print('autoteste OK')

if __name__ == '__main__':
    if sys.argv[1:] == ['--teste']: _teste(); sys.exit(0)
    if len(sys.argv) != 3: print(__doc__); sys.exit(2)
    ok = confere(json.load(open(sys.argv[1], encoding='utf-8')), {str(k): v for k, v in json.load(open(sys.argv[2], encoding='utf-8')).items()}, banco())
    sys.exit(0 if ok else 1)
