# Revisor independente · legislacao (RI Cristalina) · rodada 26/11/2026

## Fase 1 — às cegas (só texto do RI em equipe/fontes/leis.json)
- 01: B (I, II, III). Art. 5º caput (I; o item omite "e pelos demais presentes que assim o desejarem", mas não fica falso), §2º (II), §4º (III; IV falso: dispensa registro prévio do art. 10, III). Uma só defensável.
- 02: D. Art. 7º §1º. A falsa (1ª reunião ordinária de fevereiro); C falsa (5 min, §2º). Uma só.
- 03: C (apreciar vetos é do Plenário, art. 27, III). A, B, D = art. 18, II, IV, XII. Uma só.
- 04: A. Art. 20, XIII (Presidente); art. 18, X (Mesa); art. 27, III (Plenário). Uma só.
- 05: A. Art. 21 + art. 26 §4º. Uma só.
- 06: D. Art. 22. Uma só.
- 07: B (ordenar despesas é do Presidente, art. 20, XV). A, C, D = art. 25, VI, VII, IX. Uma só.
- 08: C (II e III). Art. 68, V e VII; I falsa (VI exige relação com o mandato e circunscrição do Município). Uma só.
- 09: B. Art. 69, parágrafo único e incisos I-II (numeração anômala no texto: incisos após o parágrafo único). Art. 139 §2º só como apoio. Uma só.
- 10: C. Art. 73, III "c"; II "b"; I "c". Uma só.
- 11: B. Art. 77, II e III (art. 74 só como apoio). Coerente com art. 171 §6º, XI. Uma só.
- 12: A. Art. 78, parágrafo único. Uma só.
- 13: C. Art. 82; A e B falsas pelo art. 80, parágrafo único. Uma só.
- 14: D (I e IV). Art. 87 §1º e §4º; II falsa (§2º: nenhum Vereador); III falsa (§3º: validade após leitura em Plenário). Uma só.
- 15: C (incorreta: art. 141 §8º diz o contrário). A, B, D = §§4º, 7º, 6º. Uma só.
- 16: A. Art. 142. Uma só.
- 17: C. Art. 145 §§1º-2º e art. 146 (1/3 de 15 = 5; maioria absoluta = 8, art. 150). Art. 139 só como apoio. Uma só.
- 18: A. Art. 148 e art. 153 (§1º veda réplica); art. 167 §8º, V-VI confirma. Uma só.
- 19: B. Art. 152 §§1º-3º (deferimento pelo Presidente, não Plenário; 1 uso por reunião; §6º permite exceção). Uma só.
- 20: D. Art. 214 §2º (vedado criticar); A, B, C = art. 167, VII, VIII, XI. Uma só.
- 21: D. Art. 170 caput. Uma só.
- 22: B. Art. 206 §§2º-3º; D falsa (§4º permite reiterar). Uma só.
- 23: D. Art. 214 §3º; A é o conceito de aparte (art. 215); B falsa (Presidente, §2º); C falsa. Uma só.
- 24: A (incorreta: aparte vedado no encaminhamento de votação e explicação pessoal, art. 215 §3º, IV). B, C, D = caput, §1º, §2º. Uma só.

Nenhuma questão com duas alternativas defensáveis ou nenhuma, na leitura às cegas.

## Fase 2 — conferência
- confere_esteira.py (questoes.json × revisor.json): "24 questões · reprovadas 0 · gabarito A-D [6, 6, 6, 6]".
- confere.py (cópia convertida em /tmp/claude-0/-home-claude-meuconcurso/f1cff680-0af2-501c-a793-2e334ac412ef/scratchpad/legislacao-confere.json, base → [lei, artigo, trecho], ausentes → [lei, artigo, termo]): "24 questões · reprovadas 0 · gabarito A-D [6, 6, 6, 6]" (exit 0; nenhum enunciado repetido no app).
- Gabarito às cegas × gabarito do elaborador: 24/24 iguais. Nenhuma correção em revisor.json.
- (a) Nenhuma questão com duas corretas ou nenhuma correta.
- (b) Todos os trechos de base estão literais no artigo citado e sustentam a explanation.
- (c) Todas cabem no item do edital ("Regimento Interno da Câmara Municipal de Cristalina-GO", ttop_417).
- (d) modelo.url: BH Coordenador do Processo Legislativo 2024 (qconcursos 108321), BH Técnico Legislativo II 2024 (cmbh.mg.gov.br) e Cotia Assistente de Serviço de Pessoal 2024 (qconcursos 123201) — todas listadas na seção 1 (com gabarito) de equipe/banca/legislacao-regimento-interno.md.
- (e) Nenhuma explanation afirma "gabarito oficial" de prova-modelo nem traz afirmação falsa.
- Cobertura (estado.json, artigos_ja_cobertos.ri e artigos_usados_tp6.ri): artigos-alvo todos fora das listas; art. 74 só como apoio (Q11, alvo 77) e art. 139 só como apoio (Q17, alvo 145/146). Nenhum artigo vetado/reservado da ordem (28-31, 32, 39, 99, 124, 150, 165, 168, 178, 188, 189, 192, 193, 202, 213) usado.
- Conflitos com a LO (chave "lo"), conferidos: art. 7º × LO 19 (ok); art. 18 × LO 34 (ok, LO 34 VII também dá à Mesa a promulgação das emendas); art. 20 XIII × LO 35 XIV (ok); art. 21/22 × LO 35 §§3º-4º (iguais); art. 68 VI × LO 39 (iguais); art. 145 × LO 24 (1/3, ok); art. 206 × LO 66 XIV (compatíveis); **art. 20 XV × LO 35 XVI (CONFLITO: co-assinatura dos cheques pelo "servidor designado" no RI × "Secretário" na LO)**.
- VETO legislacao26-07: gabarito depende do art. 20, XV, que conflita com a LO 35, XVI, num ponto que toca exatamente o Secretário (tema da questão). Trocar a alternativa B (ver revisao.json).
- Ajustes opcionais: 01 (item I incompleto), 03 (alternativa A sobrepõe-se a atos do Presidente), 22 (citar LO 66 XIV).

## Segunda leitura (pedido do Comandante)
- 03: A agora = art. 18, IX ("autografar as proposições de lei aprovadas, para sua remessa ao Executivo"), literal no RI; LO 35, XIII (autógrafo pelo Presidente com os demais membros da Mesa) é compatível. Gabarito C mantido. Aprovada.
- 07: B agora = art. 20, VII (reforço policial), literal no RI e idêntico à LO 35, VIII; não está no art. 25. Gabarito B mantido, conflito com a LO eliminado. VETO LEVANTADO, aprovada. (RI 216 fala de "Secretaria Geral", órgão administrativo, e não muda o gabarito.)
- confere_esteira.py e confere.py: "24 questões · reprovadas 0 · gabarito A-D [6, 6, 6, 6]" (confere.py exit 0).
- revisao.json: 24 aprovadas, 0 vetadas.
