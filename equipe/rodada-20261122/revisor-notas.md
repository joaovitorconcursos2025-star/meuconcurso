# Revisor independente: rodada 2026-11-22 (le22-01 a le22-30)

## Método
- Fase 1, às cegas: resolvi as 30 questões só com `revisor-entrada.json` e as fontes (estatuto-lei-1207.txt, regimento-interno.txt, lei-organica.txt, leis.json). As respostas estão em `revisor.json`.
- Fase 2, conferência: comparei com o gabarito, olhei se havia duas alternativas defensáveis, se o comentário tinha base nas fontes, se o assunto estava no edital (edital-01-2026 + Retificação I: LO, RI e Lei 1.207/94 constam em "Legislação Específica"), se havia artigos proibidos e se o modelo.url estava em banca.md.
- Resultado: as 30 respostas às cegas são iguais aos 30 gabaritos. O texto e as alternativas de questoes.json são idênticos aos da entrada. Os 30 modelo.url aparecem literalmente em equipe/banca.md. Nenhum artigo proibido é citado em base, comentário ou alternativa (dispositivos usados: Est. 13, 14, 24-26, 33, 35, 81, 82, 87, 88, 100, 101, 103, 105, 110, 115, 119, 132-135, 141, 150, 159-163, 167, 170-173, 180, 188, 194-198; RI 70, 71, 84, 104, 159-161; LO 112).

## Conferidores
- `confere_esteira.py questoes.json revisor.json`: 30 questões, 0 reprovadas, gabarito A-D [8, 7, 8, 7].
- `confere.py questoes_confere.json` (cópia convertida): 30 questões, 0 reprovadas, gabarito A-D [8, 7, 8, 7].

## Parecer por questão

- **le22-01**: APROVADA (Est. 13 §1º + 14).
- **le22-02**: APROVADA (Est. 24, 25, 26).
- **le22-03**: APROVADA (Est. 35).
- **le22-04**: APROVADA (Est. 119, parágrafo único).
- **le22-05**: APROVADA (Est. 82; 81 no comentário).
- **le22-06**: APROVADA, com ressalva não impeditiva. Os percentuais do distrator D ("trinta por cento e vinte por cento") só aparecem no Est. 86 (insalubridade, artigo proibido). O distrator não cita nem cobra o art. 86 e é errado só pelo art. 87, por isso não vetei. Sugestão opcional para afastar o eco: trocar D por "São, respectivamente, de quinze por cento e de cinco por cento, cabendo à Administração escolher qual deles será pago."
- **le22-07**: APROVADA (Est. 100).
- **le22-08**: APROVADA (Est. 101 e 103).
- **le22-09**: VETADA.
  - Motivo: o gabarito (D, a incorreta) depende só da ressalva do Est. 105 §1º sobre o "adicional por tempo de serviço, que será computado sempre integralmente". Esse adicional (Subseção II, art. 84) foi revogado pela Lei 1.507/2000: o art. 84 nem consta em leis.json, e estatuto-lei-1207.txt, linhas 749-752, registra a revogação. A questão cobra a regra de uma vantagem extinta, e o comentário a apresenta como vigente, sem avisar da revogação, o que induz o aluno a erro sobre o direito em vigor. Não há duas alternativas defensáveis pela letra, mas o núcleo cobrado está esvaziado.
  - Correção sugerida: manter A, B e C e reescrever D com um erro sobre parte vigente do §1º, por exemplo "D) O valor de função gratificada não percebido ininterruptamente durante todo o período aquisitivo será computado sempre integralmente." (o §1º manda computar proporcionalmente). Ajustar o comentário: "D é a incorreta: o § 1º do art. 105 manda computar proporcionalmente aos meses de sua ocorrência 'os adicionais, as gratificações e o valor de função gratificada não percebidos ininterruptamente durante todo o período aquisitivo'." Na base, trocar o trecho do ATS por "Os adicionais, as gratificações e o valor de função gratificada não percebidos ininterruptamente durante todo o período aquisitivo, serão computados proporcionalmente aos meses de sua ocorrência". Em ausentes, não usar "sempre integralmente", que existe no art. 105 (na ressalva do ATS). Não citar o ATS em base, alternativa ou comentário.
- **le22-10**: APROVADA (Est. 110).
- **le22-11**: APROVADA (Est. 115).
- **le22-12**: APROVADA (Est. 132 e 133).
- **le22-13**: APROVADA (Est. 135; 134 no comentário).
- **le22-14**: APROVADA (Est. 141).
- **le22-15**: APROVADA (Est. 150, permitido).
- **le22-16**: APROVADA (Est. 159).
- **le22-17**: APROVADA (Est. 161).
- **le22-18**: APROVADA (Est. 160 e 163).
- **le22-19**: APROVADA (Est. 167, 170, 171, 172).
- **le22-20**: APROVADA (Est. 173).
- **le22-21**: APROVADA (Est. 180).
- **le22-22**: APROVADA (Est. 188, permitido).
- **le22-23**: APROVADA (Est. 194).
- **le22-24**: APROVADA (Est. 195, 196, 198).
- **le22-25**: APROVADA (RI 70, II).
- **le22-26**: APROVADA (RI 71, VI e §§ 1º-2º).
- **le22-27**: APROVADA (RI 84).
- **le22-28**: APROVADA (RI 104).
- **le22-29**: APROVADA (RI 159, 160, 161).
- **le22-30**: APROVADA (LO 112; o LO 113, proibido, não é citado).

## Resumo
- Aprovadas: 29 (le22-01 a le22-08 e le22-10 a le22-30), sendo le22-06 com ressalva opcional.
- Vetada: 1 (le22-09: cobra regra de vantagem revogada, o ATS, e o comentário a trata como vigente).

## 2ª leitura (após correção do Elaborador): le22-06 e le22-09

Conferi as duas contra o Est. 87, 88 e 105. As respostas às cegas continuam valendo (le22-06 = C, le22-09 = D), então revisor.json não mudou. Rodei de novo os conferidores, com questoes_confere.json regenerado:
- confere_esteira.py: 30 questões, 0 reprovadas, gabarito A-D [8, 7, 8, 7].
- confere.py: 30 questões, 0 reprovadas, gabarito A-D [8, 7, 8, 7].

- **le22-06**: APROVADA. O novo D ("quinze por cento e cinco por cento", com a escolha pela Administração) erra pelo art. 87 e pelo art. 88 e não ecoa mais o Est. 86. Só C está correta. O comentário tem base no art. 87 e no art. 88 e não cita insalubridade nem o art. 86.
- **le22-09**: REPROVADA.
  - O que melhorou: D (função gratificada computada "sempre integralmente") está errada pelo § 1º do art. 105, e o comentário tem base. Base, alternativas e comentário não citam o adicional por tempo de serviço.
  - Defeito novo, que faz a questão ter duas alternativas defensáveis: a alternativa B passou de "As gratificações..." para "Os adicionais não percebidos ininterruptamente [...] serão computados proporcionalmente". O mesmo § 1º diz que os adicionais são computados proporcionalmente, "exceto o adicional por tempo de serviço, que será computado sempre integralmente". Pela letra da lei, B generaliza uma regra que tem exceção expressa, e cabe recurso sustentando que B também é incorreta. Na prática, a troca trouxe de volta, por omissão, a mesma ressalva do adicional por tempo de serviço que levou ao primeiro veto.
  - Correção, se houver nova rodada: voltar B para "As gratificações não percebidas ininterruptamente durante todo o período aquisitivo serão computadas proporcionalmente aos meses de sua ocorrência", que é a parte do § 1º sem exceção, e ajustar o comentário de B do mesmo jeito. Pela regra do Comandante, a questão sai do pacote nesta rodada.

Resumo atualizado: 29 aprovadas (le22-01 a le22-08 e le22-10 a le22-30) e 1 reprovada, le22-09, que sai do pacote.
