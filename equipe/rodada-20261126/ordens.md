# Ordens da noite · 26/11/2026 (Esteira, ESTEIRA-1)

Distribuidor. Uma ordem por matéria, sete matérias. Contagem feita em `conteudo.json` (pacotes do concurso "Câmara de Cristalina — Analista de RH"; mTP e tópicos tp* incluídos) pelo script `conta.py` no scratchpad da sessão.

## Regra de escolha
- **(a) acerto < 50%:** o último relatório do mentor no diário é o de 17/11/2026; pior tópico "RH › Gestão de pessoas nas organizações", 58%. **Nenhum tópico fura a fila.**
- **(b) ordem da lista `topicos` de ESTEIRA-1** para Português, RLM e Direito.
- **(c) item do edital com menos questões no app** para as demais (e desempate).
- Edital: Anexo I do Edital 1/2026; a Retificação I só trocou o Estatuto (Lei 475/1971 → Lei 1.207/94) e incluiu conteúdo dos cargos de nível fundamental; os itens usados abaixo não mudaram.
- Pasta `equipe/fontes/federal/` **não existe ainda**: o Pesquisador cria `cf.txt`, `lc101.txt` e `l9784.txt` com o texto do Planalto antes de o Elaborador começar.

## Resumo

| # | Matéria | Item (cargo) | topicoRef · tópico | no app | base |
|---|---|---|---|---|---|
| 1 | Língua Portuguesa (`mmat_33`) | ambos | `ttop_374` · Concordância verbal e nominal | 3 | regra |
| 2 | Raciocínio Lógico Matemático (`mmat_34`) | ambos | `ttop_378` · Princípio da regressão ou reversão | 3 | conta |
| 3 | Informática Básica (`mmat_35`) | ambos | `ttop_395` · Windows | 3 | regra |
| 4 | Direito Administrativo e Constitucional (`mmat_36`) | ambos | `ttop_406` · CF: organização do Estado | 4 | lei |
| 5 | Legislação Específica (`mmat_37`) | ambos | `ttop_417` · Regimento Interno da Câmara Municipal de Cristalina | 57 | lei |
| 6 | Conhecimentos do Cargo · Analista de RH (`mmat_38`) | Analista de RH | `ttop_425` · 7 · Lei de Responsabilidade Fiscal | 4 | lei |
| 7 | Conhecimentos do Cargo · Técnico Parlamentar (`mTP`) | Técnico Parlamentar | `tp1` · 1 · Direito Administrativo (Técnico) | 21 | lei |

## 1. Língua Portuguesa · `mmat_33`

- **Item do edital (ambos):** Quadro II: "concordância verbal e nominal" (em "Sintaxe: termos da oração; período composto; conceito e classificação das orações; concordância verbal e nominal; regência verbal e nominal; crase e pontuação.") · Quadro III: "concordância verbal e nominal"
- **Tópico:** `ttop_374` — "Concordância verbal e nominal" · **3 questões no app** · subtópico: nenhum
- **Arquivo de banca:** `equipe/banca/portugues-concordancia.md` (já existe)
- **Tipo de base:** regra
- **Fontes:**
  - equipe/banca/portugues-concordancia.md (13 questões reais Consulplan com gabarito pós-recursos e links)
  - Manual de Redação da Presidência da República, 3ª ed. (2018), concordância com pronomes de tratamento: https://www4.planalto.gov.br/centrodeestudos/assuntos/manual-de-redacao-da-presidencia-da-republica/manual-de-redacao.pdf
  - Gramática normativa (Bechara, Moderna Gramática Portuguesa; Cunha & Cintra, Nova Gramática do Português Contemporâneo) citada com capítulo/seção no campo regra
- **Formato:** 4 alternativas (A a D), uma única correta; gabarito distribuído (em 20: 5/5/5/5, tolerância ±1, sem ciclo); mistura de formatos como na banca (diretas, "INCORRETA/EXCETO" ~1/5, assertivas I–IV ~1/4, casos práticos); banca "Inédita · gêmea de prova Consulplan", ano "2026", nivel; modelo {orgao,cargo,ano,url}; explanation com a regra, por que cada distrator erra e no fim "Modelo: <órgão> · <cargo> · <ano> — <link>"; pacote cristalina-<materia>-20261126, sem plano, materiaRef/topicoRef existentes, modelo/base/ausentes fora do pacote. Distribuir pelas regras da pesquisa: sujeito composto/posposto/"uma das… que" (~5), haver/fazer impessoais e haver→existir (~4), "se" apassivador (~3), meio/bastante/muito/anexo/incluso (~3), pronome de tratamento (~2), questão-isca em que o erro é de crase/regência (~3). Pelo menos 6 no formato lista de frases "INCORRETA"/"NÃO há erro".
- **Critério de aceite:** Mínimo 20 questões; 0 reprovadas em equipe/ferramentas/confere_esteira.py; revisor às cegas confirma 100% dos gabaritos (questão com duas defensáveis sai); toda questão cabe no item_edital literal; topicoRef/subtopicoRef exatamente os indicados; nenhuma repete questão já existente no tópico; modelo com link de prova Consulplan real e gabarito oficial conferido; JSON válido, checa_scripts.py OK, aplicarPacote 2x sem duplicar e 0 tópicos novos. Nada de pontuação (tópico ttop_373 já tem 23).
- **Justificativa / observações:** Escolha pela regra (b) com desempate: a lista ESTEIRA-1 põe Pontuação (23, concluída) e depois Compreensão e interpretação (3) e Concordância (3), empatadas em 3; Concordância vai hoje porque é comum aos dois cargos e a pesquisa de banca já está pronta (diário 22/11). ATENÇÃO: o diário de 22/11 diz "hoje 11 questões", mas a contagem em conteudo.json dá 3 (estudo-v1); as 11 não existem. Próxima de Português: Compreensão e interpretação de textos (ttop_365, 3), que precisa de pesquisa e de textos de domínio público.

<details><summary>Contagem por tópico da matéria</summary>

| topicoRef | tópico (nome exato) | questões |
|---|---|---|
| `ttop_366` | Denotação e conotação | 2 |
| `ttop_369` | Tipologia e gênero textual | 2 |
| `ttop_375` | Regência verbal e nominal | 2 |
| `ttop_365` | Compreensão e interpretação de textos | 3 |
| `ttop_367` | Figuras de linguagem | 3 |
| `ttop_370` | Significação das palavras | 3 |
| `ttop_371` | Emprego das classes de palavras | 3 |
| `ttop_372` | Sintaxe da oração e do período | 3 |
| `ttop_374` | Concordância verbal e nominal | 3 |
| `ttop_376` | Crase | 3 |
| `ttop_377` | Semântica e estilística | 3 |
| `ttop_368` | Coesão e coerência | 4 |
| `pt_morf` | Estrutura e formação das palavras (nível médio) | 5 |
| `pt_fon` | Fonologia, acentuação e ortografia (nível médio) | 6 |
| `ttop_373` | Pontuação | 23 |

</details>

## 2. Raciocínio Lógico Matemático · `mmat_34`

- **Item do edital (ambos):** "Princípio da Regressão ou Reversão."
- **Tópico:** `ttop_378` — "Princípio da regressão ou reversão" · **3 questões no app** · subtópico: nenhum
- **Arquivo de banca:** `equipe/banca/rlm-regressao-reversao.md` (a criar)
- **Tipo de base:** conta
- **Fontes:**
  - Provas Consulplan 2021–2026 (Câmaras/Prefeituras) com gabarito oficial: a localizar pelo Pesquisador (PCI Concursos, Qconcursos, TecConcursos, site da Consulplan)
  - Base de cada questão: {"tipo":"conta","expr":...} — a expressão da volta (operações inversas na ordem inversa) tem de dar o número da correta e de nenhuma errada
- **Formato:** 4 alternativas (A a D), uma única correta; gabarito distribuído (em 20: 5/5/5/5, tolerância ±1, sem ciclo); mistura de formatos como na banca (diretas, "INCORRETA/EXCETO" ~1/5, assertivas I–IV ~1/4, casos práticos); banca "Inédita · gêmea de prova Consulplan", ano "2026", nivel; modelo {orgao,cargo,ano,url}; explanation com a regra, por que cada distrator erra e no fim "Modelo: <órgão> · <cargo> · <ano> — <link>"; pacote cristalina-<materia>-20261126, sem plano, materiaRef/topicoRef existentes, modelo/base/ausentes fora do pacote. Problemas de "volta ao início": gastos sucessivos em frações do que restou, "pensei num número", jogos que dobram/perdem, heranças/partilhas, estoques, idades. Respostas inteiras; nenhum distrator igual ao resultado de erro de ordem não previsto.
- **Critério de aceite:** Mínimo 20 questões; 0 reprovadas em equipe/ferramentas/confere_esteira.py; revisor às cegas confirma 100% dos gabaritos (questão com duas defensáveis sai); toda questão cabe no item_edital literal; topicoRef/subtopicoRef exatamente os indicados; nenhuma repete questão já existente no tópico; modelo com link de prova Consulplan real e gabarito oficial conferido; JSON válido, checa_scripts.py OK, aplicarPacote 2x sem duplicar e 0 tópicos novos. Toda base é conta recalculável; nenhum enunciado igual aos 3 existentes (1/3 do salário; ×3−12÷2=15; dobra e perde 10).
- **Justificativa / observações:** Regra (b): primeiro item de RLM na lista ESTEIRA-1. Pela regra (c) o mínimo seria 2 (Regra de três ttop_382, Trigonometria ttop_388, Funções ttop_391, Geometria analítica ttop_392, Polinômios ttop_394); Regra de três é a próxima da lista e deve vir na rodada seguinte.

<details><summary>Contagem por tópico da matéria</summary>

| topicoRef | tópico (nome exato) | questões |
|---|---|---|
| `ttop_382` | Regra de três simples e composta | 2 |
| `ttop_388` | Trigonometria | 2 |
| `ttop_391` | Funções de 1º e 2º grau | 2 |
| `ttop_392` | Geometria analítica | 2 |
| `ttop_394` | Polinômios | 2 |
| `ttop_378` | Princípio da regressão ou reversão | 3 |
| `ttop_380` | Lógica matemática qualitativa | 3 |
| `ttop_381` | Sequências lógicas (números, letras, figuras) | 3 |
| `ttop_383` | Razões especiais | 3 |
| `ttop_384` | Análise combinatória e probabilidade | 3 |
| `ttop_385` | Progressões aritmética e geométrica | 3 |
| `ttop_386` | Conjuntos: pertinência, inclusão, operações | 3 |
| `ttop_387` | Geometria plana e espacial | 3 |
| `ttop_389` | Conjuntos numéricos | 3 |
| `ttop_390` | Equações e inequações de 1º e 2º grau | 3 |
| `ttop_393` | Matrizes, determinantes e sistemas lineares | 3 |
| `ttop_379` | Lógica dedutiva, argumentativa e quantitativa | 4 |

</details>

## 3. Informática Básica · `mmat_35`

- **Item do edital (ambos):** "Noções de sistema operacional (ambiente Windows)."
- **Tópico:** `ttop_395` — "Windows" · **3 questões no app** · subtópico: nenhum
- **Arquivo de banca:** `equipe/banca/informatica-windows.md` (a criar)
- **Tipo de base:** regra
- **Fontes:**
  - Suporte Microsoft (pt-BR), Windows: https://support.microsoft.com/pt-br/windows
  - Atalhos de teclado no Windows: https://support.microsoft.com/pt-br/windows/atalhos-de-teclado-no-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec (Pesquisador confirma que abre; se não, usar a página equivalente achada a partir do hub acima)
  - Provas Consulplan 2021–2026 com questões de Windows 10/11 e gabarito oficial (a localizar)
- **Formato:** 4 alternativas (A a D), uma única correta; gabarito distribuído (em 20: 5/5/5/5, tolerância ±1, sem ciclo); mistura de formatos como na banca (diretas, "INCORRETA/EXCETO" ~1/5, assertivas I–IV ~1/4, casos práticos); banca "Inédita · gêmea de prova Consulplan", ano "2026", nivel; modelo {orgao,cargo,ano,url}; explanation com a regra, por que cada distrator erra e no fim "Modelo: <órgão> · <cargo> · <ano> — <link>"; pacote cristalina-<materia>-20261126, sem plano, materiaRef/topicoRef existentes, modelo/base/ausentes fora do pacote. Windows 10/11 apenas: atalhos (Win+E, Win+D, Win+L, Alt+Tab, Ctrl+Shift+Esc, Win+V…), Explorador de Arquivos (copiar×mover entre unidades, Lixeira, Shift+Delete), Configurações/Painel de Controle, Gerenciador de Tarefas, contas de usuário, área de transferência, área de trabalho virtual.
- **Critério de aceite:** Mínimo 20 questões; 0 reprovadas em equipe/ferramentas/confere_esteira.py; revisor às cegas confirma 100% dos gabaritos (questão com duas defensáveis sai); toda questão cabe no item_edital literal; topicoRef/subtopicoRef exatamente os indicados; nenhuma repete questão já existente no tópico; modelo com link de prova Consulplan real e gabarito oficial conferido; JSON válido, checa_scripts.py OK, aplicarPacote 2x sem duplicar e 0 tópicos novos. Cada atalho/comportamento comprovado em página oficial da Microsoft (url no campo base.url); nada de LibreOffice, Linux, macOS ou navegador fora de Edge/Firefox/Chrome; não repetir as 3 existentes (Win+L, Shift+Delete, arrastar entre pastas da mesma unidade).
- **Justificativa / observações:** Regra (c): 6 tópicos empatados com 3 (Windows, Redes, Navegadores, Busca, Redes sociais, Arquivos). Desempate: Windows é o 1º item do edital, é o assunto de Informática que a Consulplan mais cobra (inferência) e tem fonte oficial (Suporte Microsoft). Próximos: Navegadores (ttop_398) e Arquivos, pastas e programas (ttop_401).

<details><summary>Contagem por tópico da matéria</summary>

| topicoRef | tópico (nome exato) | questões |
|---|---|---|
| `ttop_395` | Windows | 3 |
| `ttop_397` | Redes, Internet e intranet | 3 |
| `ttop_398` | Navegadores: Edge, Firefox, Chrome | 3 |
| `ttop_399` | Sites de busca e pesquisa | 3 |
| `ttop_400` | Redes sociais | 3 |
| `ttop_401` | Arquivos, pastas e programas | 3 |
| `ttop_402` | Segurança: malware, antivírus, firewall, anti-spyware | 4 |
| `ttop_396` | Microsoft 365: Word, Excel e PowerPoint | 5 |

</details>

## 4. Direito Administrativo e Constitucional · `mmat_36`

- **Item do edital (ambos):** "Constituição Federal de 1988: Princípios Fundamentais, Direitos e Garantias Fundamentais, Direitos Sociais, Organização do Estado, Administração Pública, Organização dos Poderes e Ordem Social." — parte "Organização do Estado"
- **Tópico:** `ttop_406` — "CF: organização do Estado" · **4 questões no app** · subtópico: nenhum
- **Arquivo de banca:** `equipe/banca/direito-cf-organizacao-estado.md` (a criar)
- **Tipo de base:** lei
- **Fontes:**
  - federal id "cf" → equipe/fontes/federal/cf.txt (CRIAR: a pasta equipe/fontes/federal/ ainda não existe) com o texto copiado de https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm
  - Artigos-alvo (Título III, arts. 18 a 36): 18 (organização político-administrativa; criação de Municípios §4º), 19 (vedações), 20 e 21 (bens e competências da União), 22 (privativa), 23 (comum), 24 (concorrente — Município fora do caput), 25 (Estados), 29 (Lei Orgânica; nº de Vereadores; subsídios; inviolabilidade), 29-A (limites de despesa e folha da Câmara; crime de responsabilidade), 30 (competência municipal), 32 (DF), 34 a 36 (intervenção)
- **Formato:** 4 alternativas (A a D), uma única correta; gabarito distribuído (em 20: 5/5/5/5, tolerância ±1, sem ciclo); mistura de formatos como na banca (diretas, "INCORRETA/EXCETO" ~1/5, assertivas I–IV ~1/4, casos práticos); banca "Inédita · gêmea de prova Consulplan", ano "2026", nivel; modelo {orgao,cargo,ano,url}; explanation com a regra, por que cada distrator erra e no fim "Modelo: <órgão> · <cargo> · <ano> — <link>"; pacote cristalina-<materia>-20261126, sem plano, materiaRef/topicoRef existentes, modelo/base/ausentes fora do pacote. base {"tipo":"lei","lei":"cf","artigo":"Art. 29-A","trecho":"literal"}; usar "ausentes" quando o distrator troca competência (ex.: "concorrente" atribuída ao Município). Peso maior para 29, 29-A e 30 (Câmara Municipal).
- **Critério de aceite:** Mínimo 20 questões; 0 reprovadas em equipe/ferramentas/confere_esteira.py; revisor às cegas confirma 100% dos gabaritos (questão com duas defensáveis sai); toda questão cabe no item_edital literal; topicoRef/subtopicoRef exatamente os indicados; nenhuma repete questão já existente no tópico; modelo com link de prova Consulplan real e gabarito oficial conferido; JSON válido, checa_scripts.py OK, aplicarPacote 2x sem duplicar e 0 tópicos novos. Trecho literal conferido no cf.txt do Planalto; nada dos arts. 37 a 43 (são do ttop_407); não repetir as 4 existentes (art. 29 caput/LO, art. 22 XXVII, art. 23 meio ambiente/saúde, art. 31 fiscalização).
- **Justificativa / observações:** Regra (b): único item de Direito na lista ESTEIRA-1 ("CF: organização do Estado", 4 questões), cobrável por letra de lei. Pela regra (c) o mínimo seria 3 (Licitações ttop_412, LAI ttop_414, LGPD ttop_415); Licitações (Lei 14.133, id l14133, https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm) é a próxima.

<details><summary>Contagem por tópico da matéria</summary>

| topicoRef | tópico (nome exato) | questões |
|---|---|---|
| `ttop_412` | Licitações e contratos (Lei 14.133/2021) | 3 |
| `ttop_414` | Acesso à informação (Lei 12.527/2011) | 3 |
| `ttop_415` | LGPD (Lei 13.709/2018) | 3 |
| `ttop_403` | CF: princípios fundamentais | 4 |
| `ttop_404` | CF: direitos e garantias fundamentais | 4 |
| `ttop_406` | CF: organização do Estado | 4 |
| `ttop_408` | CF: organização dos Poderes | 4 |
| `ttop_409` | CF: ordem social | 4 |
| `ttop_410` | Organização administrativa: centralização, descentralização, autarquia, fundação, EP, SEM | 4 |
| `ttop_411` | Improbidade administrativa (Lei 8.429/1992) | 4 |
| `ttop_413` | Processo administrativo federal (Lei 9.784/1999) | 4 |
| `ttop_405` | CF: direitos sociais | 5 |
| `ttop_407` | CF: administração pública (arts. 37 a 41) | 5 |

</details>

## 5. Legislação Específica · `mmat_37`

- **Item do edital (ambos):** "Regimento Interno da Câmara Municipal de Cristalina-GO."
- **Tópico:** `ttop_417` — "Regimento Interno da Câmara Municipal de Cristalina" · **57 questões no app** · subtópico: nenhum
- **Arquivo de banca:** `equipe/banca/legislacao-regimento-interno.md` (a criar)
- **Tipo de base:** lei
- **Fontes:**
  - lei "ri" em equipe/fontes/leis.json (texto: equipe/fontes/regimento-interno.txt, Resolução 226/2026)
  - Artigos candidatos NÃO cobertos (prioritários, 32): Art. 5º, Art. 7º, Art. 14, Art. 18, Art. 20, Art. 21, Art. 22, Art. 25, Art. 26, Art. 27, Art. 68, Art. 69, Art. 72, Art. 73, Art. 77, Art. 78, Art. 80, Art. 82, Art. 87, Art. 141, Art. 142, Art. 145, Art. 146, Art. 148, Art. 152, Art. 153, Art. 167, Art. 170, Art. 201, Art. 206, Art. 214, Art. 215
  - Reserva (21): Art. 17, Art. 19, Art. 67, Art. 75, Art. 76, Art. 83, Art. 86, Art. 88, Art. 90, Art. 147, Art. 158, Art. 166, Art. 199, Art. 200, Art. 203, Art. 208, Art. 211, Art. 212, Art. 216, Art. 220, Art. 221
  - Modelos de banca: banca.md (Cotia 2024, Araraquara 2025, BH 2024 Técnico Legislativo II, Mariana 2025) — questões de Regimento de Câmaras
- **Formato:** 4 alternativas (A a D), uma única correta; gabarito distribuído (em 20: 5/5/5/5, tolerância ±1, sem ciclo); mistura de formatos como na banca (diretas, "INCORRETA/EXCETO" ~1/5, assertivas I–IV ~1/4, casos práticos); banca "Inédita · gêmea de prova Consulplan", ano "2026", nivel; modelo {orgao,cargo,ano,url}; explanation com a regra, por que cada distrator erra e no fim "Modelo: <órgão> · <cargo> · <ano> — <link>"; pacote cristalina-<materia>-20261126, sem plano, materiaRef/topicoRef existentes, modelo/base/ausentes fora do pacote. base {"tipo":"lei","lei":"ri","artigo":"Art. 20","trecho":"literal"}; "ausentes" nos distratores de número/quórum/prazo. Blocos: Mesa, Presidente e Secretário (5, 7, 14, 18, 20-22, 25); Plenário (26, 27); Vereador — direitos, deveres, extinção, ética e representação (68, 69, 72, 73, 77, 78, 80, 82, 87); reuniões, atas, quórum, Tribuna Livre e lideranças (141, 142, 145, 146, 148, 152, 153, 167, 170); contas e pedido de informações (201, 206); questão de ordem e aparte (214, 215).
- **Critério de aceite:** Mínimo 20 questões; 0 reprovadas em equipe/ferramentas/confere_esteira.py; revisor às cegas confirma 100% dos gabaritos (questão com duas defensáveis sai); toda questão cabe no item_edital literal; topicoRef/subtopicoRef exatamente os indicados; nenhuma repete questão já existente no tópico; modelo com link de prova Consulplan real e gabarito oficial conferido; JSON válido, checa_scripts.py OK, aplicarPacote 2x sem duplicar e 0 tópicos novos. Passa também em equipe/ferramentas/confere.py; nenhum artigo de banco_atual.artigos_ja_cobertos.ri nem de artigos_usados_tp6.ri; nenhum vetado (RI 28, 29, 30, 31, 99 §1º VIII, 124, 150, 178 §2º, 192, 193, 202, 213) nem a reserva do TP (RI 32, 39, 165, 168, 188, 189). Atualizar estado.json (artigos_ja_cobertos.ri e contagem regimento_interno).
- **Justificativa / observações:** Regra (c): RI 57 < LO 62 < Estatuto 64 no app. Todos os 53 candidatos conferidos: existem em leis.json["ri"] e não estão cobertos/vetados/reservados. Cuidados: art. 77 remete aos incisos do art. 74 (ler os dois); art. 145 deve casar com o art. 139 (1/3 para abrir); art. 205 ficou de fora (remete a "incisos I e II do parágrafo anterior", que o artigo não traz). Lembrar a divergência já registrada: sanção RI 193 × LO 50 (não cobrar).

<details><summary>Contagem por tópico da matéria</summary>

| topicoRef | tópico (nome exato) | questões |
|---|---|---|
| `ttop_417` | Regimento Interno da Câmara Municipal de Cristalina | 57 |
| `ttop_416` | Lei Orgânica do Município de Cristalina (nº 1/1990) | 62 |
| `ttop_418` | Estatuto dos Servidores de Cristalina (Anexo I cita Lei 475/1971; item 1.4 cita Lei 1.207/1994) | 64 |

</details>

## 6. Conhecimentos do Cargo · Analista de RH · `mmat_38`

- **Item do edital (Analista de RH):** "7. Lei Complementar Federal nº 101/2000."
- **Tópico:** `ttop_425` — "7 · Lei de Responsabilidade Fiscal" · **4 questões no app** · subtópico `ssub_top_425_1`
- **Arquivo de banca:** `equipe/banca/rh-lrf.md` (a criar)
- **Tipo de base:** lei
- **Fontes:**
  - federal id "lc101" → equipe/fontes/federal/lc101.txt (CRIAR) copiado de https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp101.htm
  - Artigos-alvo: 1º §1º e §3º, 2º IV (RCL), 18 (despesa total com pessoal; terceirização §1º; apuração §2º), 19 (60% Municípios; exclusões §1º), 20 III (Legislativo 6% / Executivo 54%), 21 (nulidade; 180 dias finais do mandato), 22 (verificação quadrimestral; limite prudencial 95% e vedações), 23 (recondução em 2 quadrimestres; sanções §3º), 59 §1º II (alerta 90%), 65 (calamidade)
  - Complementar: CF art. 169 (id "cf", https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm) só quando a questão for de despesa com pessoal
- **Formato:** 4 alternativas (A a D), uma única correta; gabarito distribuído (em 20: 5/5/5/5, tolerância ±1, sem ciclo); mistura de formatos como na banca (diretas, "INCORRETA/EXCETO" ~1/5, assertivas I–IV ~1/4, casos práticos); banca "Inédita · gêmea de prova Consulplan", ano "2026", nivel; modelo {orgao,cargo,ano,url}; explanation com a regra, por que cada distrator erra e no fim "Modelo: <órgão> · <cargo> · <ano> — <link>"; pacote cristalina-<materia>-20261126, sem plano, materiaRef/topicoRef existentes, modelo/base/ausentes fora do pacote. nivel "superior"; base {"tipo":"lei","lei":"lc101","artigo":"Art. 22","trecho":"literal"}; casos práticos com a Câmara Municipal (6% da RCL), cálculo simples de limite com base {"tipo":"conta"} opcional.
- **Critério de aceite:** Mínimo 20 questões; 0 reprovadas em equipe/ferramentas/confere_esteira.py; revisor às cegas confirma 100% dos gabaritos (questão com duas defensáveis sai); toda questão cabe no item_edital literal; topicoRef/subtopicoRef exatamente os indicados; nenhuma repete questão já existente no tópico; modelo com link de prova Consulplan real e gabarito oficial conferido; JSON válido, checa_scripts.py OK, aplicarPacote 2x sem duplicar e 0 tópicos novos. Trecho literal conferido no lc101.txt do Planalto (redação vigente, incluindo LC 178/2021); não repetir as 4 existentes (alerta 90%, nulidade art. 21, Executivo 54%, CF 169 §3º).
- **Justificativa / observações:** Regra (c): item 7 é o de menos questões em RH (4); itens 4, 5 e 6 têm 9; base é lei federal (fonte pública oficial). O pior tópico do mentor (1 · Gestão de pessoas, 58%) não fura a fila (≥ 50%).

<details><summary>Contagem por tópico da matéria</summary>

| topicoRef | tópico (nome exato) | questões |
|---|---|---|
| `ttop_425` | 7 · Lei de Responsabilidade Fiscal | 4 |
| `ttop_422` | 4 · Saúde do trabalhador | 9 |
| `ttop_423` | 5 · Planejamento de pessoal e cargos | 9 |
| `ttop_424` | 6 · Educação corporativa e equipes | 9 |
| `ttop_421` | 3 · Desempenho, conhecimento e competências | 13 |
| `ttop_420` | 2 · Desenvolvimento organizacional e de pessoas | 18 |
| `ttop_419` | 1 · Gestão de pessoas nas organizações | 29 |

</details>

## 7. Conhecimentos do Cargo · Técnico Parlamentar · `mTP`

- **Item do edital (Técnico Parlamentar):** "1. Direito Administrativo: Noções de organização administrativa. Administração direta e indireta, centralizada e descentralizada. Desconcentração. Princípios expressos e implícitos da administração pública. Órgãos públicos. Agentes públicos. Processo Administrativo. Poderes administrativos. Ato administrativo. Controle e responsabilização da administração: controle administrativo; controle judicial; controle legislativo. Improbidade Administrativa. Responsabilidade civil do Estado. Licitações e contratos conforme a Lei Federal nº 14.133/2021."
- **Tópico:** `tp1` — "1 · Direito Administrativo (Técnico)" · **21 questões no app** · subtópico `tp1_3`
- **Arquivo de banca:** `equipe/banca/tp-direito-administrativo.md` (a criar)
- **Tipo de base:** lei
- **Fontes:**
  - federal id "l9784" → equipe/fontes/federal/l9784.txt (CRIAR) de https://www.planalto.gov.br/ccivil_03/leis/l9784.htm — arts. 1º §2º (órgão/entidade/autoridade), 2º (princípios), 11 a 17 (competência, delegação, avocação), 18 a 21 (impedimento e suspeição), 50 (motivação), 53 a 55 (anulação, revogação, convalidação; decadência 5 anos), 56 a 65 (recurso administrativo: controle administrativo)
  - federal id "cf" → equipe/fontes/federal/cf.txt de https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm — art. 37 caput e §6º (princípios expressos; responsabilidade objetiva)
  - opcional: id "l8429" (https://www.planalto.gov.br/ccivil_03/leis/l8429.htm) e "l14133" (https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm), só para itens literais "Improbidade Administrativa" e "Licitações e contratos"
- **Formato:** 4 alternativas (A a D), uma única correta; gabarito distribuído (em 20: 5/5/5/5, tolerância ±1, sem ciclo); mistura de formatos como na banca (diretas, "INCORRETA/EXCETO" ~1/5, assertivas I–IV ~1/4, casos práticos); banca "Inédita · gêmea de prova Consulplan", ano "2026", nivel; modelo {orgao,cargo,ano,url}; explanation com a regra, por que cada distrator erra e no fim "Modelo: <órgão> · <cargo> · <ano> — <link>"; pacote cristalina-<materia>-20261126, sem plano, materiaRef/topicoRef existentes, modelo/base/ausentes fora do pacote. nivel "médio"; casos práticos na Câmara (Presidente, Mesa, Diretor-Geral, servidor). subtopicoRef por questão: tp1_3 (Ato administrativo) para 50/53-55/11-17; tp1_4 (Controle da administração) para recursos 56-65; tp1_1 (Órgãos e agentes públicos) para art. 1º §2º; tp1_5 (Responsabilidade civil do Estado) para CF 37 §6º; null para improbidade/licitações.
- **Critério de aceite:** Mínimo 20 questões; 0 reprovadas em equipe/ferramentas/confere_esteira.py; revisor às cegas confirma 100% dos gabaritos (questão com duas defensáveis sai); toda questão cabe no item_edital literal; topicoRef/subtopicoRef exatamente os indicados; nenhuma repete questão já existente no tópico; modelo com link de prova Consulplan real e gabarito oficial conferido; JSON válido, checa_scripts.py OK, aplicarPacote 2x sem duplicar e 0 tópicos novos. Trecho literal conferido nos .txt do Planalto; nenhuma questão de doutrina sem letra de lei; não repetir as 21 existentes (ex.: anulação em 5 anos já existe — variar o enfoque: convalidação, revogação, delegação vedada do art. 13, efeito suspensivo do art. 61).
- **Justificativa / observações:** Regra (c) por item do Quadro II: item 1 = 21 (tp1); item 2 = 122 (tp2); item 3 = 30 (tp3 12 + tp4 18); item 4 = 34 (tp5); item 5 = 55 (tp6); item 6 (Regimento Interno) não tem tópico próprio em mTP — o RI está em Legislação Específica (ttop_417) e não se cria tópico novo. Item 1 tem menos e base em lei federal (Planalto). Isoladamente, o tópico com menos questões é tp3 (12; 3.1 Rotinas administrativas e apoio parlamentar), mas a base é doutrina sem fonte pública oficial; fica para a próxima rodada. Sem sobreposição com Direito (mmat_36), que hoje faz CF arts. 18-36.

<details><summary>Contagem por tópico da matéria</summary>

| topicoRef | tópico (nome exato) | questões |
|---|---|---|
| `tp3` | 3.1 · Rotinas administrativas e apoio parlamentar | 12 |
| `tp4` | 3.2 · Arquivo, protocolo e fluxo documental | 18 |
| `tp1` | 1 · Direito Administrativo (Técnico) | 21 |
| `tp5` | 4 · Redação oficial e expedientes parlamentares | 34 |
| `tp6` | 5 · Processo legislativo municipal (LOM e RI: ver Legislação Específica) | 55 |
| `tp2` | 2 · Administração Pública | 122 |

</details>
