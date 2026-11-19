# Equipe do concurso da Câmara de Cristalina

Objetivo: o João só estuda. A equipe prepara, confere e publica o conteúdo no app Meu Concurso.
Concurso: Edital nº 1/2026, Instituto Consulplan, prova em 20/12/2026 (Técnico Parlamentar de manhã, Analista de RH à tarde).

## Memória da equipe (tudo neste repositório)
- `equipe/estado.json`: fila de tarefas e situação do banco. É a fonte da verdade sobre o que fazer.
- `equipe/diario.md`: o que cada rodada fez (mais recente no topo). O mentor da manhã lê daqui.
- `equipe/banca.md`: o que se sabe sobre a Consulplan, com links.
- `equipe/fontes/`: textos oficiais já extraídos (edital, Retificação I, Lei Orgânica, Regimento Interno, Lei 1.207/94, Lei 2.876/2026) e `leis.json` (artigo por artigo, sem redações revogadas).
- `equipe/ferramentas/`: `confere.py` (checagem obrigatória), `checa_scripts.py` (sintaxe do app), exemplos de montagem de pacote.

## Papéis
1. **Comandante** (a sessão principal): lê estado e diário, decide a rodada, aprova ou barra a publicação, escreve o diário. Não produz conteúdo.
2. **Distribuidor**: transforma a fila em ordens de serviço fechadas (o que fazer, com quais fontes, em que formato, critério de aceite) e entrega a cada agente só o contexto de que ele precisa.
3. **Analista de banca**: pesquisa provas aplicadas da Consulplan, editais e cargos semelhantes; registra em `banca.md` o que a banca costuma pedir. Separa fato (com link) de inferência.
4. **Elaborador**: escreve questões e resumos a partir das fontes e do perfil da banca.
5. **Revisor independente**: não vê o raciocínio do elaborador. Refaz cada questão olhando só o texto oficial, roda `confere.py` e reprova o que não fecha. Tem poder de veto.
6. **Engenheiro do app**: monta o pacote, atualiza o índice, testa e publica. Também corrige defeitos do app.

## Regras que ninguém quebra
- Só entra no app o que está no conteúdo programático do edital (conferir em `equipe/fontes/edital-01-2026.txt` e na Retificação I).
- Lei municipal: só o texto de `equipe/fontes`. Nada de memória, nada de versão antiga da internet. O Estatuto cobrado é a Lei 1.207/94.
- Toda questão de lei tem `base` (lei, artigo, trecho literal) e passa no `confere.py` (lei municipal; lei federal: ver Frente 2). Reprovada não entra; não se "ajusta o trecho" para passar.
- Questão real de prova só entra com banca, órgão, cargo, ano e gabarito oficial conferido. Inédita é marcada como "Inédita · padrão Consulplan" (Bacen: ver Frente 2).
- 4 alternativas (A a D), uma correta, gabarito distribuído. (Frente Bacen: 5 alternativas — ver Frente 2.)
- Um pacote novo por rodada **e por frente**, com id novo (`cristalina-<assunto>-AAAAMMDD`; Bacen: `bcb-<auditor|tecnico>-<assunto>-AAAAMMDD`). Nunca reaproveitar id. Não incluir `plano` no pacote, salvo na tarefa APP-1.
- Tópicos e matérias casam pelo nome exato já existente no app; nome diferente duplica.
- Antes do push: JSON válido, `checa_scripts.py index.html` sem erro, simulação de `aplicarPacote` duas vezes sem duplicar.
- Não apagar nem reescrever conteúdo que o João já tem. Não mexer em Firebase, senhas ou regras.
- Em caso de dúvida, não publica: registra no diário e deixa para o João decidir.

## Rodada padrão
1. Comandante lê `estado.json`, `diario.md` e `banca.md`.
2. Distribuidor emite as ordens da noite (no máximo um pacote de conteúdo e uma tarefa de pesquisa **por frente**; na frente Bacen, um pacote por cargo só na rodada do edital; a frente Cristalina é feita primeiro).
3. Analista de banca e Elaborador trabalham em paralelo.
4. Revisor confere. O que for reprovado volta uma vez ao Elaborador; se reprovar de novo, sai do pacote.
5. Engenheiro monta, testa e publica.
6. Comandante atualiza `estado.json` e acrescenta ao topo de `diario.md`: data, o que entrou no app, o que foi barrado e por quê, o que a pesquisa de banca achou, e a recomendação de estudo para o dia.

## Frente 2 — Banco Central (Auditor e Técnico) · desde 19/11/2026
O João também vai fazer o concurso do Bacen. Situação em 19/11/2026: banca **FGV** contratada em 18/11; edital previsto até **30/12/2026**; prova em 2027; 100 vagas de **Auditor** (antigo Analista, nível superior) e 50 de **Técnico** (nível médio).
No app já existem os concursos `Banco Central — Auditor` e `Banco Central — Técnico` (pacotes `bcb-auditor-v1` e `bcb-tecnico-v1` em `conteudo.json`), montados como **previsão** a partir do edital de 2024 (Cebraspe) e do padrão FGV.

**Prioridade:** até 20/12/2026 Cristalina vem sempre primeiro; o Bacen usa o que sobrar da rodada (no máximo `regras.max_questoes_bacen_por_noite` questões, contadas dentro de `max_questoes_por_noite`). Depois de 20/12 o Bacen vira a frente principal.

**Regras próprias desta frente (as demais regras gerais continuam valendo):**
- **5 alternativas (A a E)**, uma correta, gabarito distribuído. Inédita é marcada `"Inédita · padrão FGV (previsão BCB 2026)"`.
- Pacote com id novo `bcb-<auditor|tecnico>-<assunto>-AAAAMMDD`, `"soAdmin": true`, sem `criarConcurso` e sem `plano`, mas **com** `"concurso": {"name": "Banco Central — Auditor"}` (ou `Banco Central — Técnico`) e `materias`/`topicos` com `ref`, copiados de `bcb-*-v1`. Sem `concurso.name` o app dá erro e o pacote nunca instala. Anexar sempre no **fim** do `conteudo.json`. No índice do `index.html`: `{"id", "conc": "Banco Central — Auditor" ou "Banco Central — Técnico", "soAdmin": true, "criar": false}`.
- Matérias e tópicos: usar **exatamente** os nomes que já estão nos pacotes `bcb-*-v1` (leia de lá antes de montar). Tópico novo só se estiver no conteúdo programático.
- Lei federal (LC 179/2021, Lei 4.595/1964, Lei 8.112/1990, Lei 9.784/1999, CF): `base` com artigo e trecho literal copiado do Planalto (planalto.gov.br), com o link. O revisor confere o trecho no Planalto; o `confere.py` só vale para as leis municipais.
- Norma do CMN/BCB: só com número e link da página oficial (bcb.gov.br). Nada de memória para prazos, percentuais e vigências.
- Enquanto o edital não sai, só entram assuntos que estavam no edital de 2024 ou que são do próprio Bacen (SFN, autonomia, política monetária, Pix). Quando sair, vale **só** o edital novo: salvar o texto em `equipe/fontes/bacen-edital-2026.txt` e seguir a tarefa BCB-EDITAL da fila.
- Perfil da banca desta frente fica em `equipe/banca-fgv.md` (fato com link separado de inferência).
