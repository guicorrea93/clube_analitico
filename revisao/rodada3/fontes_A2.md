# Fontes avaliadas — Paulista Série A2 (bra-sp-2), revisão de 22/11/2026

### FPF — lista oficial de campeões (API do site)
- endereço: https://futebolpaulista.com.br/Handlers/Clube/ListarCampeoes.ashx?IdCategoria=2 (A2; A1 = IdCategoria=1, A3 = 3)
- cobre: campeão oficial de cada ano, 1916-2026, inclusive 1967-1978 e 1980-1984 (que faltam no pacote)
- como baixar: em lote; JSON (1 pedido)
- amostra: bateu 63 de 63 campeões do pacote (inclui 1991 AE Araçatuba)
- serve a: coleta-brasil; buscar: campeão oficial das 17 edições que faltam; distinguir EC São José (1972) de São José EC (1980)

### FPF — jogos por rodada (API do site)
- endereço: https://futebolpaulista.com.br/Handlers/Competicoes/ListarTabela.ashx?IdCampeonato=74&Ano=2015&Rodada=4
- cobre: 2007 (só datas), 2008-2026: data, hora, placar, estádio, município, link da súmula em PDF; nada antes de 2007
- como baixar: em lote por rodada (1 pedido por rodada, ~20 por ano); JSON. Nomes atuais dos clubes ("Osasco Sporting" = Oeste, "Lemense SAF", "AA Portuguesa" = Portuguesa Santista)
- amostra: 180 jogos de 2008, 2010, 2012, 2014, 2015, 2017, 2018, 2021, 2024, 2025, 2026: placar 180 de 180; data 164 de 180 (os 16 que diferem são erros do pacote: 2021 r7 e 2025 r8)
- serve a: coleta-brasil; buscar: datas (desempate RSSSF x ogol), estádio, cidade e público (0% no pacote), súmulas (cartões e autores dos gols 2008-2012)

### Wikipédia pt — páginas de cada edição
- endereço: https://pt.wikipedia.org/wiki/Campeonato_Paulista_de_Futebol_de_1985_-_Segunda_Divisão (nome da época: Segunda Divisão, Primeira Divisão, Divisão Intermediária, Divisão Especial, Série A2)
- cobre: 1947-2026 menos 1972, 2008 e 2009 (sem página com esse nome): infobox (campeão, vice, artilheiro, promovidos, rebaixados), tabelas de cada fase, finais em footballbox; 1967-1984 com tabelas e finais
- como baixar: em lote; código-fonte (index.php?action=raw), 1 pedido por edição
- amostra: tabelas 326 linhas batem e 65 diferem (quase todas nomes antigos ou as divergências já explicadas pela coleta, porque a Wikipédia copia a RSSSF); jogos em footballbox 20 de 20; artilheiros 36 de 36 nos anos com os dois
- serve a: coleta-brasil; buscar: rebaixados e promovidos (infobox), artilheiros que faltam (1998, 2003, 2026), edições 1967-1984

### Wikipédia pt — predefinição de campeões da A2
- endereço: https://pt.wikipedia.org/wiki/Predefinição:Campeões_do_Campeonato_Paulista_de_Futebol_-_Série_A2
- cobre: 1947-2026: campeão, placares da final, vice, 3º, 4º e número de participantes
- como baixar: em lote; 1 pedido
- amostra: campeões 63 de 63; vices 58 de 63 (os 5 que diferem são erros do pacote: 1979, 1986, 1996, 1997, 2013)
- serve a: coleta-brasil; buscar: vice, 3º e 4º de cada edição; 1972 (sem página própria)

### RSSSF Brasil — páginas não linkadas na lista de campeões
- endereço: https://rsssfbrasil.com/tablessz/sp1980l2.htm (existem também sp1968l2, sp1969l2, sp1971l2, sp1976l2, sp1984l2)
- cobre: 1968 e 1969 (participantes e jogos do campeão), 1971 (~100 jogos), 1976 (quadrangular final), 1980 (~40 jogos), 1984 (parcial)
- como baixar: em lote; HTML, 1 pedido por ano (o baixar_rsssf.py só baixa os anos linkados no sp2camp.htm)
- amostra: as 6 páginas abrem e trazem jogos; não comparadas jogo a jogo (a edição não está no pacote)
- serve a: coleta-brasil; buscar: jogos das edições 1968-1984 que faltam

### RSSSF Brasil — "Matches of the winner" das páginas 1947-1966
- endereço: https://rsssfbrasil.com/tablessz/sp1959l2.htm
- cobre: jogos do campeão (sem data em parte dos anos), finais com prorrogação
- como baixar: já baixadas pela coleta (data/coleta/bra-sp-2/rsssfbrasil/)
- amostra: 1959, 10 jogos do Corinthians Prudente: 10 de 10; finais de 1961 e 1962 mostram a prorrogação que o pacote não tem
- serve a: coleta-brasil; buscar: prorrogações das finais; terceira opinião sobre os jogos que vieram da Wikipédia

### transfermarkt, footballdatabase.eu
- endereço: https://www.transfermarkt.com.br/ (código da A2 não achado na busca); https://www.footballdatabase.eu/en/competition/overall/16285-paulista_a2/2014-2015 (o número devolveu outra competição)
- cobre: não avaliado
- como baixar: —
- amostra: nenhuma
- serve a: —; buscar: só se faltar fonte para 2000-2007 (a FPF não tem placar antes de 2008)
