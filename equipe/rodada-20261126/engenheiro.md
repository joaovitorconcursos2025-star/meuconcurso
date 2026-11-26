# Engenheiro do app · Rodada 26/11/2026

Sete pacotes anexados no fim de `conteudo.json` (21 → 28 pacotes; o prefixo do arquivo ficou byte a byte igual ao do HEAD, só houve acréscimo). Índice `mc-conteudo-idx` do `index.html` com as 7 entradas novas `{id, conc: "Câmara de Cristalina — Analista de RH", soAdmin: false, criar: false}` e `data-v = 7a1a58c9d1` (md5 do `conteudo.json`, 10 primeiros hex). Só uma linha do `index.html` mudou.

Estrutura igual à dos pacotes `cristalina-*-20261121/22`: `formato` meu-concurso-pacote, `versao` 3, `concurso` com name/icon/desc/dataProva (o mesmo de `cristalina-legislacao-especifica-20261122`), matéria e tópico copiados com ref e nome exatos de `cristalina-cronograma-20261121` (sem resumo, para não mexer nos resumos), sem `plano`, sem `criarConcurso`/`soAdmin`. Das questões saíram `id`, `modelo`, `base` e `ausentes`; `tipo` "abcd" e `veCorrect` 1 em todas; `subtopicoRef` "" quando a matéria não tem subtópico.

## Testes gerais
- `confere_esteira.py` (questoes.json + revisor.json): 7/7 slugs com 24 questões, 0 reprovadas, código 0.
- `confere.py` (Legislação Específica, com a base convertida para o formato `[lei, artigo, trecho]`): 24 questões, 0 reprovadas.
- JSON válido (`conteudo.json` e o índice).
- `checa_scripts.py index.html`: scripts 3, 5 e 6 OK, código 0.
- Simulação Node: `aplicarPacote`, `aplicarLeisPacote` e `semAcento` extraídos do `index.html`; estado do usuário montado aplicando os 21 pacotes já publicados (5 concursos, 35 matérias, 218 tópicos, 2.512 questões); cada pacote novo aplicado 2 vezes.

## Por pacote
| Pacote | Matéria · tópico | Questões | Gabarito A-D | Conferidor | 1ª aplicação | 2ª aplicação | Tópicos/matérias novos | Resumos |
|---|---|---|---|---|---|---|---|---|
| cristalina-portugues-20261126 | mmat_33 · ttop_374 Concordância verbal e nominal | 24 | 6/6/6/6 | OK | +24 | +0 (24 dup.) | 0/0 | intactos |
| cristalina-raciocinio-logico-20261126 | mmat_34 · ttop_378 Princípio da regressão ou reversão | 24 | 6/6/6/6 | OK | +24 | +0 (24 dup.) | 0/0 | intactos |
| cristalina-informatica-20261126 | mmat_35 · ttop_395 Windows | 24 | 6/6/6/6 | OK | +24 | +0 (24 dup.) | 0/0 | intactos |
| cristalina-direito-20261126 | mmat_36 · ttop_406 CF: organização do Estado | 24 | 6/6/6/6 | OK | +24 | +0 (24 dup.) | 0/0 | intactos |
| cristalina-legislacao-especifica-20261126 | mmat_37 · ttop_417 Regimento Interno | 24 | 6/6/6/6 | OK (+ confere.py OK) | +24 | +0 (24 dup.) | 0/0 | intactos |
| cristalina-rh-20261126 | mmat_38 · ttop_425 / ssub_top_425_1 (LRF) | 24 | 6/6/6/6 | OK | +24 | +0 (24 dup.) | 0/0 | intactos |
| cristalina-tecnico-parlamentar-20261126 | mTP · tp1 / tp1_3 e tp1_4 | 24 | 6/6/6/6 | OK | +24 | +0 (24 dup.) | 0/0 | intactos |

Em todos: 0 subtópicos novos, toda questão nova ligada a matéria e tópico, subtópico resolvido em todas as que o pedem.

## Observações
- **RH:** entraram as 24. O `revisao.json` ainda lista rh26-11, 14 e 22 como vetadas, mas elas já vêm corrigidas no `questoes.json` (modelo Cotia/SP 2024 Contador; trecho do art. 19 sem a pontuação final) e o conferidor passou.
- **TP:** as questões vieram sem `subtopicoRef`. Apliquei o mapa da ordem e do revisor: `tp1_4` (Controle da administração) para tp26-16 a 21, 23 e 24 (recursos, arts. 56-65); `tp1_3` (Ato administrativo) para as outras 16. O concurso do TP é o mesmo dos demais ("Câmara de Cristalina — Analista de RH", matéria mTP), como no pacote `cristalina-tecnico-parlamentar-20261121`.
- **Pendências do revisor que ficam com o Comandante:** em RLM e TP há a ressalva de que o gabarito pós-recursos dos modelos (Mariana/MG 2025, Vermelho Novo, Patrocínio do Muriaé) não foi conferido. As explanations não dizem "gabarito oficial". Os ajustes opcionais do revisor (portugues26-15/16/17, informatica26-05/07, rh26-13/21 etc.) não foram aplicados: o Engenheiro não altera conteúdo.
- Commit local só com `conteudo.json` e `index.html`, sem push.
