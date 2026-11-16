# Cada questão: (lei, topico, enunciado, correta, [erradas], explicação, [(lei, artigo, trecho literal que comprova)])
Q=[]
def q(lei,text,certa,erradas,exp,base): Q.append(dict(lei=lei,text=text,certa=certa,erradas=erradas,exp=exp,base=base))
# ───────── LEI ORGÂNICA
q('lo',"De acordo com a Lei Orgânica do Município de Cristalina, com a redação vigente, o número de Vereadores da Câmara Municipal está fixado em:",
  "15 (quinze).",["9 (nove).","11 (onze).","13 (treze)."],
  "Art. 18 da Lei Orgânica: o número de Vereadores fica fixado em 15 (quinze), observada a proporcionalidade com a população e o limite do art. 29, IV, \"d\", da CF. Atenção: a redação antiga, que só falava em proporcionalidade, foi substituída.",
  [('lo','Art. 18','fica fixado em 15 (quinze)')])
q('lo',"Nos termos da Lei Orgânica de Cristalina, a Câmara Municipal reunir-se-á, anualmente, nos períodos de:",
  "2 de fevereiro a 30 de junho e de 1º de agosto a 15 de dezembro.",
  ["2 de fevereiro a 17 de julho e de 1º de agosto a 22 de dezembro.","15 de fevereiro a 30 de junho e de 1º de agosto a 15 de dezembro.","1º de fevereiro a 30 de junho e de 1º de agosto a 20 de dezembro."],
  "Art. 19 da Lei Orgânica: de 2 de fevereiro a 30 de junho e de 1º de agosto a 15 de dezembro. A alternativa com 17 de julho e 22 de dezembro copia o calendário do Congresso Nacional (CF, art. 57), que não é o de Cristalina.",
  [('lo','Art. 19','de 2 de fevereiro a 30 de junho e de 1º de agosto a 15 de dezembro')])
q('lo',"Sobre as sessões da Câmara Municipal de Cristalina, segundo a Lei Orgânica, assinale a afirmativa correta.",
  "Somente poderão ser abertas com a presença de, no mínimo, um terço dos membros da Câmara Municipal.",
  ["Somente poderão ser abertas com a presença da maioria absoluta dos membros da Câmara Municipal.","Serão secretas, salvo deliberação em contrário da maioria simples dos Vereadores.","Serão públicas, salvo deliberação em contrário da maioria absoluta dos Vereadores, em qualquer hipótese."],
  "Art. 24 da Lei Orgânica: abertura com, no mínimo, um terço (1/3) dos membros. Art. 23: as sessões são públicas, salvo deliberação em contrário de dois terços (2/3) dos Vereadores, em razão de motivo relevante.",
  [('lo','Art. 24','no mínimo, um terço (1/3) dos membros'),('lo','Art. 23','salvo deliberação em contrário de dois terços (2/3) dos Vereadores')])
q('lo',"Conforme a Lei Orgânica de Cristalina, as comissões especiais de inquérito serão criadas pela Câmara Municipal mediante requerimento de:",
  "um terço de seus membros, para a apuração de fato determinado e por prazo certo.",
  ["maioria absoluta de seus membros, para a apuração de qualquer fato de interesse local, sem prazo.","dois terços de seus membros, para a apuração de fato determinado e por prazo certo.","qualquer Vereador, desde que autorizado pela Mesa Diretora, por prazo certo."],
  "Art. 27 da Lei Orgânica: requerimento de um terço dos membros, fato determinado e prazo certo; as conclusões, se for o caso, vão ao Ministério Público.",
  [('lo','Art. 27','mediante requerimento de um terço de seus membros, para a apuração de fato determinado e por prazo certo')])
q('lo',"A Lei Orgânica do Município de Cristalina poderá ser emendada mediante proposta, EXCETO:",
  "da maioria absoluta dos membros da Mesa Diretora da Câmara Municipal.",
  ["de um terço, no mínimo, dos membros da Câmara Municipal.","do Prefeito Municipal.","de cinco por cento, no mínimo, do eleitorado municipal."],
  "Art. 44 da Lei Orgânica: a proposta de emenda cabe a um terço, no mínimo, dos membros da Câmara; ao Prefeito; e a cinco por cento, no mínimo, do eleitorado municipal. Não há legitimidade da Mesa Diretora.",
  [('lo','Art. 44','de um terço, no mínimo, dos membros da Câmara Municipal'),('lo','Art. 44','de cinco por cento, no mínimo, do eleitorado municipal')])
q('lo',"A proposta de emenda à Lei Orgânica de Cristalina será votada em:",
  "dois turnos, com interstício mínimo de 10 dias, e aprovada por dois terços dos membros da Câmara Municipal.",
  ["dois turnos, com interstício mínimo de 10 dias, e aprovada por três quintos dos membros da Câmara Municipal.","turno único, e aprovada por dois terços dos membros da Câmara Municipal.","dois turnos, com interstício mínimo de 30 dias, e aprovada pela maioria absoluta dos membros da Câmara Municipal."],
  "Art. 44, § 1º, da Lei Orgânica: dois turnos, interstício mínimo de 10 (dez) dias, aprovação por dois terços (2/3). Três quintos é o quórum de emenda à Constituição Federal, não o da Lei Orgânica.",
  [('lo','Art. 44','votada em dois turnos, com interstício mínimo de 10 (dez) dias, e aprovada por dois terços (2/3) dos membros')])
q('lo',"Segundo a Lei Orgânica de Cristalina, o processo legislativo municipal compreende a elaboração das espécies a seguir, EXCETO:",
  "medidas provisórias.",["leis delegadas.","decretos legislativos.","resoluções."],
  "Art. 43 da Lei Orgânica: emendas à Lei Orgânica, leis complementares, leis ordinárias, leis delegadas, decretos legislativos e resoluções. Medida provisória não está no rol.",
  [('lo','Art. 43','IV - leis delegadas'),('lo','Art. 43','VI - resoluções')])
q('lo',"O projeto de lei aprovado pela Câmara Municipal de Cristalina foi enviado ao Prefeito. De acordo com a Lei Orgânica, se o Prefeito considerar o projeto contrário ao interesse público, deverá vetá-lo no prazo de:",
  "quinze dias úteis, contados da data do recebimento, comunicando os motivos do veto ao Presidente da Câmara dentro de quarenta e oito horas.",
  ["quinze dias corridos, contados da aprovação, comunicando os motivos do veto ao Presidente da Câmara em dez dias.","dez dias úteis, contados da data do recebimento, comunicando os motivos do veto ao Presidente da Câmara dentro de vinte e quatro horas.","trinta dias úteis, contados da data do recebimento, dispensada a comunicação dos motivos."],
  "Art. 50, § 1º, da Lei Orgânica: veto em quinze dias úteis, contados do recebimento, com comunicação dos motivos em quarenta e oito horas. O caput fala em sanção no prazo de 15 dias corridos e envio do projeto ao Prefeito em 05 dias úteis.",
  [('lo','Art. 50','no prazo de quinze dias úteis, contados da data do recebimento, e comunicará, dentro de quarenta e oito horas')])
q('lo',"Vagou o cargo de Prefeito de Cristalina e não há Vice-Prefeito. Nos termos da Lei Orgânica, se a vacância ocorrer no último ano do mandato:",
  "assumirá o Presidente da Câmara Municipal, que completará o período.",
  ["será realizada eleição direta 90 dias após a abertura da vaga.","será realizada eleição indireta pela Câmara Municipal em 30 dias.","assumirá o Vereador mais votado, que convocará eleição em 90 dias."],
  "Art. 62 da Lei Orgânica: vacância nos três primeiros anos, eleição 90 (noventa) dias após a abertura; vacância no último ano, assume o Presidente da Câmara, que completa o período.",
  [('lo','Art. 62','ocorrendo à vacância no último ano do mandato, assumirá o Presidente da Câmara Municipal que completará o período')])
q('lo',"De acordo com a Lei Orgânica de Cristalina, o Prefeito e o Vice-Prefeito, quando no exercício do cargo, não poderão, sem licença da Câmara Municipal, ausentar-se do Município por período superior a:",
  "15 dias, sob pena de perda do cargo ou do mandato.",
  ["10 dias, sob pena de advertência.","30 dias, sob pena de perda do cargo ou do mandato.","15 dias, sob pena de suspensão do subsídio."],
  "Art. 64 da Lei Orgânica: ausência superior a 15 (quinze) dias exige licença da Câmara, sob pena de perda do cargo ou do mandato.",
  [('lo','Art. 64','por período superior a 15 (quinze) dias, sob pena de perda do cargo ou do mandato')])
# ───────── REGIMENTO INTERNO
q('ri',"Segundo o Regimento Interno da Câmara Municipal de Cristalina (Resolução nº 226/2026), a Mesa Diretora compõe-se dos cargos de:",
  "Presidente, Vice-Presidente, Primeiro e Segundo Secretário, que se substituem na ordem inversa.",
  ["Presidente, Primeiro e Segundo Vice-Presidentes e Secretário-Geral.","Presidente, Vice-Presidente, Secretário e Tesoureiro, que se substituem na ordem direta.","Presidente e três Secretários, eleitos pelo Prefeito Municipal."],
  "Art. 8º do Regimento Interno: Presidente, Vice-Presidente, Primeiro e Segundo Secretário, que se substituem na ordem inversa. O § 1º diz que tomam assento à Mesa o Presidente, o Vice-Presidente e o Primeiro Secretário.",
  [('ri','Art. 8º','compõe-se dos cargos de Presidente, Vice-Presidente, Primeiro e Segundo Secretário, que se substituem na ordem inversa')])
q('ri',"Conforme o Regimento Interno da Câmara de Cristalina, o mandato dos membros da Mesa Diretora terá duração de:",
  "2 anos, equivalente a um biênio, vedada a reeleição para o mesmo cargo, ressalvado o disposto no Ato das Disposições Transitórias.",
  ["1 ano, permitida a reeleição na eleição imediatamente subsequente.","4 anos, coincidindo com a legislatura, vedada a reeleição.","2 anos, permitida uma reeleição para o mesmo cargo na mesma legislatura."],
  "Art. 9º e § 1º do Regimento Interno: mandato de 2 (dois) anos (biênio) e vedação de reeleição para o mesmo cargo, ressalvado o Ato das Disposições Transitórias. O mandato de 1 ano estava no art. 26 da Lei Orgânica, que foi revogado.",
  [('ri','Art. 9º','terá duração de 2 (dois) anos, equivalente a um biênio'),('ri','Art. 9º','É vedada a reeleição para o mesmo cargo da Mesa Diretora')])
q('ri',"Sobre a eleição da Mesa Diretora, de acordo com o Regimento Interno da Câmara de Cristalina, é correto afirmar que será feita por votação:",
  "pública e nominal, cargo a cargo, por maioria absoluta de votos no primeiro escrutínio.",
  ["secreta, por chapa, por maioria simples de votos em escrutínio único.","pública e simbólica, por chapa, por dois terços dos votos no primeiro escrutínio.","secreta, cargo a cargo, por maioria absoluta de votos no primeiro escrutínio."],
  "Art. 10 do Regimento Interno: votação pública e nominal, cargo a cargo, maioria absoluta no 1º escrutínio; não alcançada, 2º escrutínio entre os dois mais votados, por maioria simples. Art. 11: em caso de empate, é eleito o candidato mais idoso.",
  [('ri','Art. 10','far-se-á por votação pública e nominal, cargo a cargo, por maioria absoluta de votos no 1º (primeiro) escrutínio'),('ri','Art. 11','considerar-se-á eleito em cada cargo, o candidato mais idoso')])
q('ri',"São Comissões Permanentes da Câmara Municipal de Cristalina, segundo o Regimento Interno, EXCETO:",
  "Educação, Saúde e Assistência Social.",
  ["Constituição, Legislação, Justiça e Redação Final.","Orçamento, Finanças e Tributação.","Obras, Bens e Serviços Públicos."],
  "Art. 37, parágrafo único, do Regimento Interno: são três as Comissões Permanentes: Constituição, Legislação, Justiça e Redação Final; Orçamento, Finanças e Tributação; Obras, Bens e Serviços Públicos.",
  [('ri','Art. 37','I – Constituição, Legislação, Justiça e Redação Final'),('ri','Art. 37','III – Obras, Bens e Serviços Públicos')])
q('ri',"Nos termos do Regimento Interno da Câmara de Cristalina, as reuniões ordinárias serão realizadas:",
  "em número não inferior a 5 por mês, com duração de até 3 horas, iniciando-se às 9 horas, preferencialmente às quintas-feiras.",
  ["em número não inferior a 4 por mês, com duração de até 4 horas, iniciando-se às 19 horas, preferencialmente às terças-feiras.","em número não inferior a 5 por mês, com duração de até 2 horas, iniciando-se às 14 horas, obrigatoriamente às segundas-feiras.","uma vez por semana, sem duração máxima, em horário fixado pelo Plenário a cada reunião."],
  "Art. 143 do Regimento Interno: não menos que 5 (cinco) reuniões por mês, até 3 (três) horas, início às 9 (nove) horas, preferencialmente às quintas-feiras.",
  [('ri','Art. 143','em número não inferior a 5 (cinco) reuniões por mês'),('ri','Art. 143','iniciando-se às 9 (nove) horas, realizadas preferencialmente às quintas-feiras')])
q('ri',"Quanto à discussão e aos turnos das proposições, o Regimento Interno da Câmara de Cristalina estabelece que:",
  "a discussão da matéria da Ordem do Dia somente poderá ser efetuada com a presença da maioria absoluta dos membros da Câmara.",
  ["o segundo turno de discussão e votação poderá ocorrer na mesma reunião do primeiro, se houver acordo de lideranças.","a discussão da matéria da Ordem do Dia poderá ser efetuada com a presença de um terço dos membros da Câmara.","os vetos são submetidos a dois turnos de discussão e votação."],
  "Art. 162, § 1º: a discussão exige a presença da maioria absoluta. Art. 162, § 2º: vetos e matérias em regime de urgência vão a turno único. Art. 163: em nenhuma hipótese o segundo turno ocorre na mesma reunião do primeiro.",
  [('ri','Art. 162','somente poderá ser efetuada com a presença da maioria absoluta dos membros da Câmara Municipal'),('ri','Art. 163','Em nenhuma hipótese o segundo turno de discussão e votação ocorrerá na mesma reunião')])
q('ri',"Um Vereador presente à reunião tem interesse pessoal na matéria em votação. De acordo com o Regimento Interno da Câmara de Cristalina, ele:",
  "deverá abster-se de votar e comunicar o impedimento ao Presidente, computando-se sua presença para efeito de quórum.",
  ["poderá votar normalmente, pois o Vereador presente não pode se recusar a votar em nenhuma hipótese.","deverá retirar-se do Plenário, e sua presença não será computada para efeito de quórum.","deverá abster-se de votar, e a votação será obrigatoriamente secreta."],
  "Art. 169 e parágrafo único do Regimento Interno: o Vereador presente não pode se recusar a votar, mas deve abster-se quando tiver interesse pessoal, sob pena de nulidade se o voto for decisivo; comunica o impedimento e sua presença conta para o quórum. Art. 170, parágrafo único: o voto será sempre público.",
  [('ri','Art. 169','devendo, porém, abster-se quando tiver interesse pessoal na matéria'),('ri','Art. 169','computando-se, todavia, sua presença para efeito de quórum'),('ri','Art. 170','o voto será sempre público')])
q('ri',"Segundo o Regimento Interno, o Vereador que não tomar posse na reunião de instalação deverá fazê-lo, sob pena de perda do mandato, salvo motivo justo e aceito pela maioria da edilidade, dentro do prazo de:",
  "15 dias, contados do início do funcionamento normal da Câmara Municipal.",
  ["10 dias, contados da diplomação.","30 dias, contados da reunião de instalação.","15 dias, contados da data da eleição da Mesa Diretora."],
  "Art. 6º do Regimento Interno: prazo de 15 (quinze) dias, contados do início do funcionamento normal da Câmara Municipal.",
  [('ri','Art. 6º','dentro do prazo de 15 (quinze) dias, contados do início do funcionamento normal da Câmara Municipal')])
q('ri',"De acordo com o Regimento Interno da Câmara de Cristalina, os Vereadores tomarão posse no primeiro dia de cada legislatura, em sessão solene de instalação, se presente:",
  "um terço da edilidade, sob a presidência do Vereador mais votado dentre os presentes.",
  ["a maioria absoluta da edilidade, sob a presidência do Vereador mais idoso dentre os presentes.","um terço da edilidade, sob a presidência do Vereador mais idoso dentre os presentes.","dois terços da edilidade, sob a presidência do Presidente da legislatura anterior."],
  "Art. 4º do Regimento Interno: posse com a presença de 1/3 (um terço) da edilidade, sob a presidência do Vereador que, dentre os presentes, tiver sido o mais votado. Cuidado: mais votado, e não mais idoso.",
  [('ri','Art. 4º','se presente 1/3 (um terço) da edilidade, sob a presidência do Vereador que dentre os presentes, tiver sido o mais votado')])
# ───────── ESTATUTO (LEI 1.207/1994)
q('est',"Nos termos do Estatuto dos Servidores Públicos do Município de Cristalina (Lei Municipal nº 1.207/1994), são formas de provimento de cargo público, EXCETO:",
  "ascensão.",["recondução.","aproveitamento.","transferência."],
  "Art. 7º da Lei 1.207/1994: nomeação, recondução, readaptação, reversão, reintegração, aproveitamento, promoção e transferência. Ascensão não consta do rol.",
  [('est','Art. 7º','II – recondução'),('est','Art. 7º','VIII – transferência')])
q('est',"De acordo com a Lei Municipal nº 1.207/1994, o prazo de validade do concurso público será de:",
  "até dois anos, prorrogável, uma vez, por igual período.",
  ["até um ano, prorrogável, uma vez, por igual período.","dois anos, improrrogável.","até dois anos, prorrogável por períodos sucessivos, a critério da Administração."],
  "Art. 9º da Lei 1.207/1994: validade de até dois anos, prorrogável, uma vez, por igual período.",
  [('est','Art. 9º','será de até dois anos, prorrogável, uma vez, por igual período')])
q('est',"Sobre posse e exercício no Estatuto dos Servidores de Cristalina (Lei nº 1.207/1994), assinale a afirmativa correta.",
  "A posse dar-se-á em até quinze dias da publicação do ato de nomeação, e o prazo para entrar em exercício é de 5 dias, contados da posse.",
  ["A posse dar-se-á em até trinta dias da publicação do ato de nomeação, e o prazo para entrar em exercício é de 15 dias, contados da posse.","A posse dar-se-á em até quinze dias da publicação do ato de nomeação, e o prazo para entrar em exercício é de 30 dias, contados da nomeação.","A posse dar-se-á em até dez dias da publicação do ato de nomeação, sem possibilidade de prorrogação, e o exercício é imediato."],
  "Art. 12, § 1º: posse em até quinze dias da publicação da nomeação, prorrogável por igual período. Art. 13, § 1º: 5 (cinco) dias para entrar em exercício, contados da posse. A alternativa com 30 e 15 dias reproduz a Lei federal 8.112/1990, que não é a regra de Cristalina.",
  [('est','Art. 12','no prazo de até quinze dias contados da data de publicação do ato de nomeação'),('est','Art. 13','É de 5 (cinco) dias o prazo para o servidor entrar em exercício, contados da data da posse')])
q('est',"Conforme a redação vigente da Lei Municipal nº 1.207/1994, adquire estabilidade o servidor nomeado para cargo de provimento efetivo em virtude de concurso público após:",
  "3 anos de efetivo exercício e aprovação em avaliação especial de desempenho realizada durante o estágio probatório.",
  ["2 anos de efetivo exercício, independentemente de avaliação.","3 anos de efetivo exercício, independentemente de avaliação.","5 anos de efetivo exercício e aprovação em avaliação especial de desempenho."],
  "Art. 18 da Lei 1.207/1994 (redação vigente): 3 (três) anos de efetivo exercício e aprovação em avaliação especial de desempenho. A redação antiga falava em 2 anos e foi substituída.",
  [('est','Art. 18','após 3 (três) anos de efetivo exercício e aprovação em avaliação especial de desempenho')])
q('est',"Segundo a Lei Municipal nº 1.207/1994, a vacância do cargo decorrerá das hipóteses a seguir, EXCETO:",
  "reintegração.",["readaptação.","recondução.","promoção."],
  "Art. 33 da Lei 1.207/1994: exoneração, demissão, readaptação, recondução, aposentadoria, falecimento e promoção. Reintegração é forma de provimento (art. 7º), não de vacância.",
  [('est','Art. 33','III – readaptação'),('est','Art. 33','VII – promoção'),('est','Art. 7º','V – reintegração')])
q('est',"São penalidades disciplinares previstas no art. 148 do Estatuto dos Servidores de Cristalina (Lei nº 1.207/1994), EXCETO:",
  "multa.",["advertência.","cassação de aposentadoria e disponibilidade.","demissão."],
  "Art. 148 da Lei 1.207/1994: advertência; suspensão; demissão; cassação de aposentadoria e disponibilidade; destituição de cargo ou função de confiança. Multa não aparece no rol do artigo.",
  [('est','Art. 148','I – advertência'),('est','Art. 148','IV – cassação de aposentadoria e disponibilidade')])
q('est',"De acordo com a Lei Municipal nº 1.207/1994, a ação disciplinar prescreverá, quanto às infrações punidas com advertência ou suspensão, em:",
  "180 dias, contados da data em que a autoridade tomar conhecimento da existência da falta.",
  ["2 anos, contados da data do fato.","180 dias, contados da data do fato.","5 anos, contados da data em que a autoridade tomar conhecimento da existência da falta."],
  "Art. 165 da Lei 1.207/1994: 5 (cinco) anos para infrações puníveis com demissão, cassação de aposentadoria e disponibilidade ou destituição de função de confiança; 180 (cento e oitenta) dias para advertência ou suspensão. § 2º: o prazo corre da data em que a autoridade tomar conhecimento da falta.",
  [('est','Art. 165','em 180 (cento e oitenta) dias, quanto às infrações punidas com advertência ou suspensão'),('est','Art. 165','começa a correr da data em que a autoridade tomar conhecimento da existência da falta')])
q('est',"Quanto às licenças previstas no Estatuto dos Servidores de Cristalina (Lei nº 1.207/1994, redação vigente), é correto afirmar que:",
  "a licença à servidora gestante é de 180 dias consecutivos e a licença-paternidade é de 5 dias.",
  ["a licença à servidora gestante é de 120 dias consecutivos e a licença-paternidade é de 5 dias.","a licença à servidora gestante é de 180 dias consecutivos e a licença-paternidade é de 20 dias.","a licença à servidora gestante é de 120 dias consecutivos e a licença-paternidade é de 15 dias."],
  "Art. 220 (redação vigente): licença à gestante por 180 (cento e oitenta) dias consecutivos, sem prejuízo da remuneração. Art. 222: licença-paternidade de 5 (cinco) dias a contar do nascimento. O prazo de 120 dias é da redação antiga.",
  [('est','Art. 220','por 180 (cento e'),('est','Art. 222','A licença-paternidade será de 5 (cinco) dias')])
q('est',"É requisito básico para ingresso no serviço público municipal de Cristalina, segundo a Lei nº 1.207/1994:",
  "ter idade mínima de 18 anos.",
  ["ter idade mínima de 21 anos.","residir no Município de Cristalina há pelo menos dois anos.","ter concluído, no mínimo, o ensino médio, qualquer que seja o cargo."],
  "Art. 6º da Lei 1.207/1994: ser brasileiro; estar no gozo dos direitos políticos; ter idade mínima de 18 (dezoito) anos; estar quite com as obrigações militares e eleitorais; gozar de boa saúde física e mental. Confira o rol completo no leitor de leis.",
  [('est','Art. 6º','III – ter idade mínima de 18 (dezoito) anos')])
