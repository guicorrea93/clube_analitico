# Fontes avaliadas: Campeonato Paulista, 1ª divisão (bra-sp-1), revisor QS, 22/11/2026

Fontes que nem a coleta (RSSSF Brasil, ogol, coluna de campeões da Wikipédia pt) nem as revisões anteriores (Wikipédia pt e en) usaram.
Scripts em `revisao/QS/`; páginas em `data/cache/revisao/QS/` (1 pedido a cada 2,5 s, cache, 429 tratado).

### Futebol Nacional (futebolnacional.com.br)
- endereço: https://futebolnacional.com.br/siteapp/controller.jsp?module=championship&code=55BF5B4E3D1767D8F3D8AA42B4ABAE14&lang=pt-br (1925); lista de todas as edições com o código: https://futebolnacional.com.br/siteapp/controller.jsp?module=summary&lang=pt-br&name=A27437D2CE0894275C03A3BAEDA49F41A9C63F1F39F7FF7572315985555EFA80&state=SP&country=BR ; ficha do jogo: controller.jsp?module=matchdetails&code=<código>
- cobre: as 137 edições (1902 a 2026, com 1933/1934 FPF sem jogos): todos os jogos com data, placar, fase e nota (cancelado, W.O., "ganhou os pontos", abandono de clube, desempate); campeão, vice e artilheiro de cada edição; total de jogos registrados e com resultado; fonte de cada edição (ex.: livro "O Caminho da Bola", de Rubens Ribeiro, em 1925). Autores dos gols na nota do jogo: 42% dos jogos nos anos 2000, 68% nos 2010, 84% nos 2020, quase nada antes de 2000. A ficha do jogo traz estádio e hora só nos anos recentes; árbitro e público ficam na parte paga (Premium).
- como baixar: em lote, 1 página HTML por edição (137 páginas, ~6 min); o HTML vem de `controller.jsp` (a `page.jsp` só tem a casca). Nomes de época ("Palestra Itália", "Hespanha", "Ferroviária¹", "Botafogo FC", "Mackenzie" = Portuguesa-Mackenzie em 1920): casar por votos (jogos do mesmo dia e placar), como em `revisao/QS/fn_comparar.py`.
- amostra: TODOS os jogos, por década (casados por par de clubes e data ±45 dias): 1900s placar 207/207, data 215/217; 1910s 563/564 e 569/569; 1920s 1.092/1.099 e 1.104/1.108; 1930s 1.015/1.022 e 1.023/1.028; 1940s 1.115/1.119 e 1.117/1.120; 1950s 2.582/2.589 e 2.585/2.589; 1960s 2.249/2.268 e 2.259/2.269; 1970s 2.385/2.398 e 2.366/2.399; 1980s 3.717/3.738 e 3.733/3.738; 1990s 2.889/2.896 e 2.698/2.896 (1997: o FN dá 1 dia depois em 119 jogos; o infobox pt confirma o pacote, "início 8 de fevereiro"); 2000s 1.614/1.615 e 1.590/1.615; 2010s 1.590/1.594 e 1.548/1.594; 2020s 608/612 e 581/612. Campeão e vice: batem com a Wikipédia nas edições conferidas; artilheiro bate com a RSSSF (sptops.htm) em quase todas as edições em que a Wikipédia pt diverge (ver QS-011). Saídas: `revisao/QS/fn_comparar_saida.txt`, `revisao/QS/fn_diferencas.csv`.
- serve a: coleta-brasil; buscar: (1) jogos cancelados por abandono de clube e jogos anulados (QS-001, QS-006), que a coleta conta na classificação; (2) jogos que faltam (1916 LPF, 1920, 1929 LAF, 1942, 1957, 1966: QS-007) e W.O. sem placar (1906, 1916 LPF, 1920: QS-005, SP-016); (3) terceira opinião de placar/data quando RSSSF e ogol divergem; (4) as fases preliminares de 1970-1972 (SP-006), se o Guilherme decidir incluir; (5) artilheiro de 1902-2026 (confirmação). Risco: o próprio FN erra datas em lote (1997, 1978, 1990) e mistura o Troféu do Interior/Taça Independência nas edições (2007-2013, 2017-2023): usar como terceira opinião, nunca como base única.

### FPF — API pública do site (futebolpaulista.com.br)
- endereço: https://futebolpaulista.com.br/Handlers/Competicoes/ListarTabela.ashx?IdCampeonato=73&Ano=2019&Rodada=1&IdClube=0&IdCategoria=39 (jogos de uma rodada); ListarRodadas.ashx?IdCampeonato=73&Ano=<ano>; ListarArtilharia.ashx?idCampeonato=73&IdClube=&exercicio=<ano>&idCategoria=39&pagina=0&tipoGol= (artilharia completa, 150 por página); ListarDataCampeonatos.ashx?IdCampeonato=73 (anos: 2007 a 2027); súmula em PDF: http://conteudo.fpf.org.br/sumulas/2019/3973/1.pdf; campeões oficiais (Tableau): https://public.tableau.com/static/images/Ca/CampeesSrieA1/Dashboard1/1.png
- cobre: Série A1 de 2007 a 2026: data, hora, rodada, fase e grupo de cada jogo, estádio e município, placar; artilharia oficial com todos os autores (nome de jogo e nome completo); súmula (árbitro, assistentes, cronologia, escalações, gols, cartões, substituições) em PDF desde ~2016 (antes o link volta vazio ou para uma página antiga); boletim financeiro (público e renda) em PDF nos anos recentes. A lista oficial de campeões (Tableau, até 2019) conta 22 títulos do Santos (1973 dividido) e nenhum título para Albion/Fiorentino (1933/1934 FPF).
- como baixar: em lote, JSON: 1 pedido por rodada (19 a 23 por ano; ~400 pedidos para 2007-2026) + 1 por ano para a artilharia; súmula e boletim: 1 PDF por jogo (~2.200 PDFs para 2016-2026; `pdftotext -layout` lê). O site passa por Cloudflare, mas os `.ashx` respondem a curl/Python com User-Agent normal.
- amostra: TODOS os jogos de 2007 a 2025 (377 pedidos): 2.806 casados com o pacote (por década: 2000s 588, 2010s 1.594, 2020s 624); placar igual em 2.805 (a exceção, 26/02/2014 XV de Piracicaba x São Paulo, a FPF dá 1-3 como o FN e o ogol: QS-012); data igual em 2.738 (68 diferentes: QS-008). Nas diferenças pacote x Futebol Nacional de 2007+, a FPF fica com o FN em 64 datas e com o pacote em 23 datas e 7 placares. Os jogos "só FPF" (4 a 11 por ano em 2007-2013 e 2017-2023) são o Troféu do Interior/Taça Independência, que a coleta tira de propósito. Artilheiro 2007-2026: bate com o Futebol Nacional em todos os anos (2010 Ricardo Bueno 16; 2021 Bruno Mezenga 9, a RSSSF diz 10). Saídas: `revisao/QS/fpf_comparar_saida.txt`, `revisao/QS/fpf_jogos.json`, `revisao/QS/fpf_artilharia.json`.
- serve a: coleta-brasil; buscar: (1) a fase e o grupo de cada jogo de 2024 e 2025 (SP-008: o pacote põe tudo em "Fase única"); (2) data oficial dos jogos de 2007 em diante (QS-008); (3) artilheiros 2007-2026 (SP-023, SP-024) e, se o Guilherme quiser, todos os autores dos gols 2007-2026 pela artilharia (sem minuto) ou pela súmula (com minuto); (4) árbitro, cartões e público pelas súmulas/boletins (2016+); (5) a edição de 2026 (SP-004). Risco: `NomePopular` é o nome de HOJE do clube (o Oeste aparece como "Osasco Sporting", o Bragantino como "Red Bull Bragantino" mesmo em 2010): casar pelo id do clube da FPF ou pelo par de clubes + data; o PDF da súmula é texto (não imagem) mas com acentos trocados no `pdftotext`.

### RSSSF Brasil — lista de artilheiros (sptops.htm)
- endereço: https://rsssfbrasil.com/tablessz/sptops.htm (já baixada pela coleta: `data/coleta/bra-sp-1/rsssfbrasil/sptops.htm`)
- cobre: artilheiro de cada edição de 1902 a 2021, com a liga (LPFB, APEA, LAFB, LFESP, FPF) nos anos de duas ligas.
- como baixar: já está no disco; 1 página.
- amostra: 135 edições comparadas com o Futebol Nacional e a Wikipédia pt (`revisao/QS/cmp_artilheiros_saida.txt`): RSSSF e FN batem entre si nas 17 edições em que a Wikipédia pt diverge (1906, 1908, 1909, 1911, 1912, 1917, 1919, 1937, 1943, 1947, 1956, 1959, 1960, 1967, 1975, 1990, 1994).
- serve a: coleta-brasil; buscar: o artilheiro oficial de 1902-2021 (SP-023, SP-024). O `pacote.py` JÁ tenta ler esta página (`artilheiros()`), mas a expressão regular espera "Jogador (Clube) 10" e a página é em colunas: aceita 0 linhas (QS-010). Risco: baixo.

### transfermarkt (transfermarkt.com.br)
- endereço: https://www.transfermarkt.com.br/campeonato-paulista/gesamtspielplan/wettbewerb/BCP1/saison_id/2005 (o código é BCP1, não SPA1; `saison_id` 2005 = Paulista 2006)
- cobre: Paulista de 2006 em diante (190 jogos em 2006, 150 em 2016); 1999 só 8 jogos. Ficha do jogo (spielbericht) com árbitro, público, autores com minuto e cartões.
- como baixar: calendário em lote (1 página por temporada); fichas jogo a jogo (~150-200 por ano; ~3.500 páginas para 2006-2025, ~2,5 h a 1 pedido a cada 2,5 s).
- amostra: calendário de 2006 conferido no olho (1ª rodada: Noroeste 1:0 Corinthians, 11/01/2006); não comparado jogo a jogo nesta rodada.
- serve a: coleta-brasil; buscar: árbitro, público e cartões de 2006-2015 (antes das súmulas em PDF da FPF). Risco: médio (nomes e datas de jogos noturnos às vezes no dia seguinte, como no ogol).

### Clubes: SPFCpédia, Meu Timão (Almanaque do Timão), Palmeiras oficial
- endereço: https://www.saopaulofc.net/enciclopedia-clube-lista-de-jogos/ ; https://www.meutimao.com.br/estatisticas-do-corinthians-em-1930 ; https://www.palmeiras.com.br/derby/todos-os-jogos
- cobre: só os jogos de um clube (São Paulo desde 1930, Corinthians desde 1910, Palmeiras x Corinthians desde 1917), com data, estádio e, em parte, autores dos gols.
- como baixar: jogo a jogo ou por filtro de página; o formato muda por site.
- amostra: só verifiquei que respondem e o tipo de dado (não comparei placares).
- serve a: coleta-brasil; buscar: autores dos gols da era amadora (1902-1935) só se o Guilherme quiser esse nível; custo alto e cobertura parcial (um clube por site). Prioridade baixa.

### Acervos de jornais (Estadão, Folha, Hemeroteca Digital)
- endereço: https://acervo.estadao.com.br/ ; https://acervo.folha.com.br/ ; https://memoria.bn.br/ (Correio Paulistano 1854-1963)
- cobre: tudo (súmulas publicadas, autores, público, árbitro) desde 1902 (Estadão), 1921 (Folha da Noite) e no Correio Paulistano.
- como baixar: página escaneada, jogo a jogo, com busca manual; Estadão e Folha pedem assinatura para a página inteira; a Hemeroteca não respondeu daqui (DNS).
- amostra: não aplicável (só testei se o site abre: Estadão e Folha abrem).
- serve a: ninguém por enquanto. O Guilherme decidiu (A2, 21/11) que "o que só existe em jornal escaneado fica de fora"; no máximo para tirar uma dúvida pontual (um placar de 1906 ou uma data de 1930).

### Livros de história do Paulista
- endereço: "125 Anos de História – A Enciclopédia do Futebol Paulista" (FPF, 2021, ISBN 659960630X); "O Caminho da Bola" (Rubens Ribeiro), citado pelo Futebol Nacional como fonte das edições antigas.
- cobre: campeões, tabelas, jogos e artilheiros da era amadora.
- como baixar: não há versão online; só pela citação na Wikipédia en/Futebol Nacional.
- amostra: não aplicável.
- serve a: referência para decisões (o que a FPF reconhece); não é fonte de carga.
