# Coleta: Campeonato Neocaledônio (`ncl-1`)

Gerado por `python coleta/ncl-1/importar.py`. Pacote em `data/coleta/ncl-1/pacote/`.

## Resumo

- 76 edições (1950 a 2026; sem 1955 e 2024), 36 com jogos; 2472 jogos, 9956 gols, 188 com autor.
- Escopo aprovado pelo Guilherme em 24/11/2026, depois de pesquisa a fundo (docstring de `coleta/ncl-1/edicoes.py` e de `coleta/ncl-1/clubes_ncl.py`):
  - 2024 fica de fora: a Super Ligue parou nos distúrbios de maio de 2024 e a federação encerrou as competições em 12/08 sem declarar campeão (o AS Tiga Sport, líder, só foi indicado à Liga dos Campeões da OFC);
  - 1963 e 1964: Club Sportif Militaire, como a RSSSF atual (corrigida no fim de 2025 por recorte de jornal da época); a versão antiga da RSSSF, copiada pela Wikipédia e pelo ogol, dava USC (1963) e JS Vallée du Tir (1964, que ganhou a copa naquele ano);
  - AS Le Nickel = AS Magenta (mesmo clube com outro nome); Gaïtcha FCN = Gaïtcha FC; ASC Gaïca (Lifou) separado; "Île des Pins" (1961) = AS Kunié;
  - até 2001 só a fase nacional; 2002-2011 a liga da Grande Terre como 1ª fase e o playoff nacional; 2012 em diante a Super Ligue.
- Pontuação: 4 por vitória, 2 por empate e 1 por derrota; a classificação traz os pontos oficiais (`ajuste_pontos` = bônus e punições).

## Fontes

- **RSSSF** (`data/coleta/ncl-1/rsssf/`, `baixar_rsssf.py`): lista de campeões e páginas por temporada (1984, 1985, 1997-2026).
- **Wikipédia em inglês** (`data/coleta/ncl-1/wikipedia/`, `baixar_wikipedia.py`): segunda fonte do campeão.
- **ogol** (`data/coleta/ncl-1/ogol/`, cache em `data/cache/ogol-ncl-1/`, `baixar_ogol.py`): datas e grafia dos clubes nas temporadas em que tem os jogos.

## Correções e decisões

- `newcal03 / 194`: a página traz Olympique 1-0 AS Magenta, mas a tabela da mesma página dá vitória do Magenta e 9 gols a mais para ele (e sofridos pelo Olympique): só este jogo explica (o outro entre os dois foi 3-0 para o Magenta); placar provável 1-9.
- `newcal08 / 49`: vitória dada ao Kirikitr (o Mont-Dore escalou jogador suspenso); em campo, 1-1, e a tabela conta esses gols.
- `newcal2011 / 139`: vitória dada ao Hienghène sem gols ("awarded 0-0 win"); em campo, 0-4.
- tabela `newcal09`, linha 68, fora da conferência: tabela do playoff com os resultados de campo (antes da decisão da comissão que deu o jogo ao Lössi).

## Divergências que ficam (erro ou falta na própria página)

- **2004/05:** Grande Terre: dois jogos só com o vencedor na página (ACB Poya "bt" ASLN Kouaoua, AS Poum "bt" CA Saint-Louis), que ficam de fora; falta também um jogo USC Nouméa x ASLN Kouaoua (3-2 pela tabela) e o JS Baco tem um gol a mais a favor e contra; a classificação é a tabela da página.
- **2013:** AS Lössi x AS Mont-Dore só com "drw" (empate sem placar) na página: fica de fora; a tabela conta o empate.
- **2015:** jogos sem placar na página (Gaïtcha "drw" Lössi; Auteuil "lt" Baco, "by 1 goal") ficam de fora; a tabela é a de antes das punições do fim da temporada e conta o 2-2 de campo de Lössi x Gaïtcha (dado 3-0 ao Lössi); a classificação é essa tabela.
- **2018:** um gol de diferença: o Trio Kedeigne tem um gol a mais a favor e o SC Ne Drehu um a mais contra na tabela do que nos jogos entre os dois (1-3 e 5-1); não dá para saber em qual; fica o placar da página.

## Edição a edição

| Temporada | Formato | Jogos | Esperados | Gols | Com autor | Campeão | Vice | Observação |
|---|---|---|---|---|---|---|---|---|
| 1950 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Impassible |  | só o campeão na lista da RSSSF |
| 1951 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Impassible |  | só o campeão na lista da RSSSF |
| 1952 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | SS Indépendante |  | só o campeão na lista da RSSSF |
| 1953 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Impassible |  | só o campeão na lista da RSSSF |
| 1954 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | SS Indépendante |  | só o campeão na lista da RSSSF |
| 1956 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Impassible |  | só o campeão na lista da RSSSF |
| 1957 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | PLGC |  | só o campeão na lista da RSSSF |
| 1958 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | PLGC |  | só o campeão na lista da RSSSF |
| 1959 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | PLGC |  | só o campeão na lista da RSSSF |
| 1960 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Impassible |  | só o campeão na lista da RSSSF |
| 1961 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Kunié |  | só o campeão na lista da RSSSF |
| 1962 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | USC Nouméa |  | só o campeão na lista da RSSSF |
| 1963 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Club Sportif Militaire | UAC Yaté | só o campeão na lista da RSSSF; Wikipédia: USC Nouméa |
| 1964 | só a final (da lista de campeões) | 1 | 1 | 3 | 0 | Club Sportif Militaire | Essor de Canala | só o campeão na lista da RSSSF; Wikipédia: JS Vallée du Tir |
| 1965 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Frégate |  | só o campeão na lista da RSSSF; Wikipédia: JS Vallée du Tir |
| 1966 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Frégate |  | só o campeão na lista da RSSSF |
| 1967 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | JS Vallée du Tir | UAC Yaté | só o campeão na lista da RSSSF |
| 1968 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | JS Vallée du Tir |  | só o campeão na lista da RSSSF |
| 1969 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Magenta |  | só o campeão na lista da RSSSF |
| 1970 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Magenta |  | só o campeão na lista da RSSSF |
| 1971 | só a final (da lista de campeões) | 1 | 1 | 1 | 0 | Stade Français de Tadine | JS Vallée du Tir | só o campeão na lista da RSSSF |
| 1972 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Saint Jean-Baptiste Nathalo |  | só o campeão na lista da RSSSF |
| 1973 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Groupement Sportif Ouvéa |  | só o campeão na lista da RSSSF |
| 1974 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Gaïtcha FC |  | só o campeão na lista da RSSSF |
| 1975 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | UAC Yaté | Croix Bleue | só o campeão na lista da RSSSF |
| 1976 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Magenta |  | só o campeão na lista da RSSSF |
| 1977 | só a final (da lista de campeões) | 1 | 1 | 3 | 0 | Kehdek de Koumac | AS Magenta | só o campeão na lista da RSSSF |
| 1978 | só a final (da lista de campeões) | 1 | 1 | 5 | 0 | USL Gélima | JS Maré | só o campeão na lista da RSSSF |
| 1979 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | JS Baco |  | só o campeão na lista da RSSSF |
| 1980 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | RS Koumac |  | só o campeão na lista da RSSSF |
| 1981 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | USL Gélima |  | só o campeão na lista da RSSSF |
| 1982 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | JS Baco |  | só o campeão na lista da RSSSF |
| 1983 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | CA Saint-Louis |  | só o campeão na lista da RSSSF |
| 1984 | final | 1 | 1 | 3 | 0 | AS Frégate | AS Païta |  |
| 1985 | rodada preliminar + semifinais + final | 5 | 5 | 18 | 0 | AS Kunié | CA Saint-Louis |  |
| 1986 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS 6e km |  | só o campeão na lista da RSSSF |
| 1987 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | CA Saint-Louis |  | só o campeão na lista da RSSSF |
| 1988 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | CA Saint-Louis |  | só o campeão na lista da RSSSF |
| 1989 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Wé-Luécilla | Entente Gélima | só o campeão na lista da RSSSF |
| 1990 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Gaïtcha FC |  | só o campeão na lista da RSSSF |
| 1991 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Wé-Luécilla | AS Kunié | só o campeão na lista da RSSSF |
| 1992 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Kunié |  | só o campeão na lista da RSSSF |
| 1993 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Wé-Luécilla | AS Magenta | só o campeão na lista da RSSSF |
| 1994 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | JS Baco | AS Magenta | só o campeão na lista da RSSSF |
| 1995 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | JS Baco | JS Traput | só o campeão na lista da RSSSF |
| 1996 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | JS Traput | JS Baco | só o campeão na lista da RSSSF |
| 1997 | jogos incompletos: final | 1 | 1 | 3 | 0 | JS Baco | CA Saint-Louis | a página da RSSSF traz só parte dos jogos do mata-mata |
| 1998 | semifinais + final | 4 | 4 | 10 | 0 | AS Poum | JS Traput |  |
| 1999 | quartas de final + semifinais + final; 4 pontos por vitória, 2 por empate e 1 por derrota | 11 | 11 | 36 | 0 | Gaïtcha FC | AS Auteuil |  |
| 2000 | quartas de final + semifinais + final; 4 pontos por vitória, 2 por empate e 1 por derrota | 13 | 13 | 35 | 0 | JS Baco | JS Traput |  |
| 2001 | quartas de final + semifinais + final; 4 pontos por vitória, 2 por empate e 1 por derrota | 12 | 12 | 32 | 0 | JS Baco | AS Mont-Dore |  |
| 2002 | liga da Grande Terre (8 clubes) + semifinais + final; 4 pontos por vitória, 2 por empate e 1 por derrota | 61 | 61 | 224 | 0 | AS Mont-Dore | JS Baco |  |
| 2002/03 | liga da Grande Terre (10 clubes) + semifinais + final; 4 pontos por vitória, 2 por empate e 1 por derrota | 92 | 92 | 368 | 0 | AS Magenta | JS Baco |  |
| 2003/04 | liga da Grande Terre (10 clubes) + semifinais + final; 4 pontos por vitória, 2 por empate e 1 por derrota | 95 | 95 | 389 | 0 | AS Magenta | AS Mont-Dore |  |
| 2004/05 | liga da Grande Terre (11 clubes) + semifinais + final; 4 pontos por vitória, 2 por empate e 1 por derrota | 113 | 115 | 438 | 0 | AS Magenta | AS Mont-Dore |  |
| 2005/06 | pontos corridos (8 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 55 | 55 | 290 | 0 | AS Mont-Dore | JS Baco | não houve playoff nacional: o campeão da Grande Terre é o campeão |
| 2006/07 | liga da Grande Terre (8 clubes) + grupo do rebaixamento (Grande Terre) (5 clubes) + playoff do título (4 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 87 | 87 | 342 | 0 | JS Baco | AS Lössi |  |
| 2007/08 | liga da Grande Terre (8 clubes) + grupo do rebaixamento (Grande Terre) (5 clubes) + playoff do título (4 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 78 | 78 | 335 | 47 | AS Magenta | AS Mont-Dore | no grupo do rebaixamento da Grande Terre os clubes levam um bônus da fase regular |
| 2008/09 | liga da Grande Terre (8 clubes) + grupo do rebaixamento (Grande Terre) (5 clubes) + playoff do título (4 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 78 | 78 | 392 | 75 | AS Magenta | AS Mont-Dore |  |
| 2009 | pontos corridos (8 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 56 | 56 | 251 | 26 | AS Magenta | Hienghène Sport | não houve playoff nacional: o campeão da Super Ligue (Grande Terre) é o campeão (o calendário passou a ser o ano civil) |
| 2010 | liga da Grande Terre (8 clubes) + playoff do título (5 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 76 | 76 | 364 | 29 | AS Mont-Dore | AS Magenta |  |
| 2011 | liga da Grande Terre (8 clubes) + playoff do título (5 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 74 | 74 | 278 | 11 | AS Mont-Dore | Thio Sport |  |
| 2012 | pontos corridos (11 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 110 | 110 | 512 | 0 | AS Magenta | Hienghène Sport |  |
| 2013 | pontos corridos (11 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 109 | 110 | 453 | 0 | Gaïtcha FC | Hienghène Sport |  |
| 2014 | pontos corridos (12 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 132 | 132 | 556 | 0 | AS Magenta | AS Lössi |  |
| 2015 | pontos corridos (12 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 131 | 133 | 540 | 0 | AS Magenta | Hienghène Sport |  |
| 2016 | pontos corridos (13 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 156 | 156 | 667 | 0 | AS Magenta | AS Lössi |  |
| 2017 | pontos corridos (12 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 132 | 132 | 562 | 0 | Hienghène Sport | AS Magenta |  |
| 2018 | pontos corridos (12 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 132 | 132 | 490 | 0 | AS Magenta | Hienghène Sport |  |
| 2019 | pontos corridos (10 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 90 | 90 | 350 | 0 | Hienghène Sport | AS Magenta |  |
| 2020 | pontos corridos (10 clubes) + playoff do título (4 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 51 | 51 | 191 | 0 | AS Tiga Sport | AS Horizon Patho |  |
| 2021 | pontos corridos (13 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 109 | 109 | 444 | 0 | Hienghène Sport | SC Ne Drehu |  |
| 2022 | pontos corridos (12 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 131 | 131 | 452 | 0 | AS Tiga Sport | Hienghène Sport |  |
| 2023 | pontos corridos (12 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 133 | 133 | 427 | 0 | AS Magenta | ASC Gaïca |  |
| 2025 | fase de grupos (10 clubes) + rodada preliminar + quartas de final + semifinais + disputa do 3º lugar + final; 4 pontos por vitória, 2 por empate e 1 por derrota | 50 | 50 | 184 | 0 | AS Tiga Sport | ASC Gaïca | a liga voltou em maio de 2025, depois de um ano parada pelos distúrbios civis, num formato adaptado (grupos e mata-mata) |
| 2026 | pontos corridos (10 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 90 | 90 | 308 | 0 | AS Magenta | AS Tiga Sport |  |

## O que não deu para coletar

- Jogos de 1950-1983 e 1986-1996 (só o campeão; a final em 1964, 1971, 1977 e 1978; vice e 3º em parte dos anos).
- 1997 e 1998 com parte do mata-mata; jogos sem placar ("bt", "drw", "lt") em 2004/05, 2013 e 2015.
- Ligas das províncias (até 2001) e torneio das ilhas: fora do escopo.
- Hora, estádio, público, cartões e artilheiros.
