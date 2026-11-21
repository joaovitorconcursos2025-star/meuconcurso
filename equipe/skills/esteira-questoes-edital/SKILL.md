---
name: esteira-questoes-edital
description: Use para encher o app Meu Concurso do João com questões de TODAS as matérias do edital (Câmara de Cristalina, Consulplan, prova 20/12/2026) com a mesma qualidade da Legislação Específica — pesquisa provas reais da banca, escreve questões gêmeas, revisor às cegas, conferidor automático e pacote no tópico certo. Mínimo 20 questões por matéria por rodada.
---

# Esteira de questões do edital (todas as matérias)

O João estuda; a equipe enche o app. Esta skill faz em **todas as matérias** o que já funciona na Legislação Específica: **nenhuma questão entra sem prova do gabarito**, conferida por máquina e por um revisor que não viu a resposta.

## Meta por rodada
- **Mínimo 20 questões por matéria** objetiva: Língua Portuguesa, Raciocínio Lógico Matemático, Informática Básica, Direito Administrativo e Constitucional, Legislação Específica, Conhecimentos do Cargo · Analista de RH e Conhecimentos do Cargo · Técnico Parlamentar.
- **Qualidade vem antes da meta.** Se o revisor ou o conferidor barrar, a questão sai; registre no diário quantas faltaram e complete na rodada seguinte. Nunca afrouxe uma regra para bater número.
- Trabalhe as matérias **em paralelo** (um pesquisador + um elaborador por matéria; revisores separados).

## Escolha do tópico de cada matéria
1. Tópico com acerto **abaixo de 50%** no último relatório do mentor (está no topo de `equipe/diario.md`) fura a fila.
2. Senão, o tópico do edital com **menos questões** no app (conte em `conteudo.json`; concurso `Câmara de Cristalina — Analista de RH`).
3. Só tópicos que estão no conteúdo programático (`equipe/fontes/edital-01-2026.txt`). Tópico concluído = 10+ questões; depois disso ele só volta pela regra 1.

## Os 4 papéis (cada um só faz a sua parte)
**1. Pesquisador de banca** — acha **provas reais do Instituto Consulplan** (2021–2026; Câmaras e Prefeituras primeiro; nível médio e superior) que cobram o tópico: PCI Concursos, Qconcursos, TecConcursos, site da Consulplan. Registra em `equipe/banca/<materia>-<topico>.md`, para cada questão real: órgão, cargo, ano, **link da prova**, gabarito, regra cobrada, formato do enunciado e pegadinha. **Não copia o texto integral** (direito autoral da banca): descreve com as próprias palavras. Fecha com o quadro "como a Consulplan cobra este tópico".

**2. Elaborador** — escreve **questões gêmeas**: mesmo assunto, mesmo formato de enunciado e mesma pegadinha da prova real, com texto próprio. Cada questão leva:
- 4 alternativas (A a D), uma correta, gabarito distribuído;
- `banca: "Inédita · gêmea de prova Consulplan"`, `ano: "2026"`, `nivel`;
- `modelo: {orgao, cargo, ano, url}` da prova real que inspirou;
- `base` que **prova** o gabarito, conforme a matéria:

  | Matéria | `base` |
  |---|---|
  | Leis (Legislação Específica, CF, Lei 8.112, 8.429, 9.784, 14.133…) | `{"tipo":"lei","lei":"lo\|ri\|est\|<id federal>","artigo":"Art. 37","trecho":"literal"}` — lei federal: salvar antes o texto do Planalto em `equipe/fontes/federal/<id>.txt` |
  | Raciocínio Lógico (contas) | `{"tipo":"conta","expr":"2000*0.015*8"}` — a conta tem de dar o número da correta |
  | Português, Informática, Cargo (doutrina) | `{"tipo":"regra","fonte":"gramática/manual/norma","url":"https://…","regra":"…"}` |
- `ausentes` (opcional, leis): termo usado no distrator que **não** pode aparecer no artigo;
- `explanation`: a regra, por que cada distrator está errado e, no fim, `Modelo: <órgão> · <cargo> · <ano> — <link>`.

**3. Revisor independente** — recebe só enunciado e alternativas (sem gabarito, sem comentário), resolve e grava `revisor.json` = `{"<id>": índice}`. Depois confere se há duas corretas, se o link do modelo abre e se o assunto está no edital. Tem veto.

**4. Engenheiro do app** — roda o conferidor e só empacota o que passou:
```
python equipe/ferramentas/confere_esteira.py questoes.json revisor.json
```
(Legislação Específica continua passando também no `confere.py`.) Depois, um pacote por matéria: id `cristalina-<materia>-AAAAMMDD`, `materiaRef`/`topicoRef` **dos tópicos já existentes** (mesmo nome; refs abaixo), sem `plano`, entrada no `mc-conteudo-idx` com `criar:false`, `data-v` = md5 do `conteudo.json` (10 primeiros hex), JSON compacto, simulação do `aplicarPacote` 2× sem duplicar, `checa_scripts.py`, commit em português e push na main. Os campos `modelo`, `base` e `ausentes` ficam fora do pacote (o app não usa); o link do modelo já está no fim da `explanation`.

## Refs das matérias (concurso "Câmara de Cristalina — Analista de RH")
`mmat_33` Língua Portuguesa · `mmat_34` Raciocínio Lógico Matemático · `mmat_35` Informática Básica · `mmat_36` Direito Administrativo e Constitucional · `mmat_37` Legislação Específica · `mmat_38` Conhecimentos do Cargo · Analista de RH · `mTP` Conhecimentos do Cargo · Técnico Parlamentar. Refs de tópicos: leia os pacotes em `conteudo.json` (ex.: Pontuação = `ttop_373`).

## Diário (topo de `equipe/diario.md`)
Por matéria: tópico, provas reais analisadas (com links), questões que entraram, quantas o revisor/conferidor barrou e por quê, e quantas faltaram para as 20.
