# Coleta: Campeonato Taitiano (`tah-1`)

Gerado por `python coleta/tah-1/importar.py`. Pacote em `data/coleta/tah-1/pacote/`.

## Resumo

- 79 edições (1948 a 2025/26), 31 com jogos; 2647 jogos, 11748 gols, 113 com autor.
- Escopo aprovado pelo Guilherme em 24/11/2026 (docstring de `coleta/tah-1/edicoes.py`): desde 1948, até 2025/26, "2025/26" nas temporadas que cruzam o ano, nomes com "AS", em 1956, 1957 e 1961 vale a RSSSF.
- Pontuação: 4-2-1 (vitória, empate, derrota) na maior parte dos anos recentes, 3-2-1 em 1969-1971 e 2007/08, 3-1-0 de 1998/99 a 2002/03. A classificação traz os pontos oficiais; `ajuste_pontos` = bônus e punições.
- Classificação final: playoff do título, grupo do rebaixamento e o resto pela fase regular; campeão e vice no topo.

## Fontes

- **RSSSF** (`data/coleta/tah-1/rsssf/`, `baixar_rsssf.py`): lista de campeões e páginas por temporada (1968-1971, 1985, 1998/99 em diante).
- **Wikipédia em inglês** (`data/coleta/tah-1/wikipedia/`, `baixar_wikipedia.py`): segunda fonte do campeão (lista da página "Tahiti Ligue 1", que copia uma versão antiga da RSSSF).
- **ogol** (`data/coleta/tah-1/ogol/`, cache em `data/cache/ogol-tah-1/`, `baixar_ogol.py`): jogos de 2012/13 e 2013/14 (playoff), 2021/22 e 2023/24; nas outras edições só o campeão.

## Correções e decisões

- `tahiti71 / 159`: resultado não homologado por erro do árbitro; o jogo foi repetido (0-6).
- `tahiti2022 / 99`: a federação deu derrota aos dois clubes ("awarded 0-0 loss to both"); em campo, 3-0.
- Jogos anulados e repetidos: a página lista os dois; o anulado entra como não disputado (`n/p`), com o placar na observação.

## Edição a edição

| Temporada | Formato | Jogos | Esperados | Gols | Com autor | Campeão | Vice | Observação |
|---|---|---|---|---|---|---|---|---|
| 1948 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Fei Pi |  | só o campeão na lista da RSSSF |
| 1949 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Fei Pi |  | só o campeão na lista da RSSSF |
| 1950 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Fei Pi |  | só o campeão na lista da RSSSF |
| 1951 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Fei Pi |  | só o campeão na lista da RSSSF |
| 1952 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Excelsior |  | só o campeão na lista da RSSSF |
| 1953 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Vénus |  | só o campeão na lista da RSSSF |
| 1954 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Jeunes Tahitiens |  | só o campeão na lista da RSSSF |
| 1955 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1956 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Vénus |  | só o campeão na lista da RSSSF; Wikipédia: AS Excelsior |
| 1957 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Jeunes Tahitiens |  | só o campeão na lista da RSSSF; Wikipédia: AS Excelsior |
| 1958 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1959 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Excelsior |  | só o campeão na lista da RSSSF |
| 1960 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Excelsior |  | só o campeão na lista da RSSSF |
| 1961 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Excelsior |  | só o campeão na lista da RSSSF; Wikipédia: AS Jeunes Tahitiens |
| 1962 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1963 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1964 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1965 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1966 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1967 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1968 | jogos incompletos: pontos corridos | 5 | 5 | 22 | 0 | AS Fei Pi | AS Tamarii Punaruu | só 5 resultados e a classificação sem números (Journal de Tahiti) |
| 1969 | pontos corridos (7 clubes); 3 pontos por vitória, 2 por empate e 1 por derrota | 42 | 42 | 180 | 0 | AS Tamarii Punaruu | AS Fei Pi |  |
| 1970 | pontos corridos (8 clubes); 3 pontos por vitória, 2 por empate e 1 por derrota | 55 | 55 | 178 | 0 | AS Fei Pi | AS Vénus |  |
| 1971 | pontos corridos (8 clubes); 3 pontos por vitória, 2 por empate e 1 por derrota | 57 | 57 | 236 | 0 | AS Fei Pi | AS Vaiete |  |
| 1972 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1973 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1974 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1975 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1976 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1977 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1978 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1979 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1980 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Arue |  | só o campeão na lista da RSSSF |
| 1981 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1982 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1983 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1984 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS PTT |  | só o campeão na lista da RSSSF |
| 1985 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Central Sport |  | só o campeão na lista da RSSSF |
| 1986 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Excelsior |  | só o campeão na lista da RSSSF |
| 1987 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Jeunes Tahitiens |  | só o campeão na lista da RSSSF |
| 1988 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Excelsior |  | só o campeão na lista da RSSSF |
| 1989 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Pirae |  | só o campeão na lista da RSSSF |
| 1990 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Vénus | AS Pirae | só o campeão na lista da RSSSF (e o vice, AS Pirae) |
| 1991 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Pirae |  | só o campeão na lista da RSSSF |
| 1992 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Vénus | AS Pirae | só o campeão na lista da RSSSF (e o vice, AS Pirae) |
| 1993 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Pirae |  | só o campeão na lista da RSSSF |
| 1994 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Pirae |  | só o campeão na lista da RSSSF |
| 1995 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Vénus | AS Pirae | só o campeão na lista da RSSSF (e o vice, AS Pirae) |
| 1996 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Manu-Ura | AS Pirae | só o campeão na lista da RSSSF (e o vice, AS Pirae) |
| 1997 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Vénus | AS Pirae | só o campeão na lista da RSSSF (e o vice, AS Pirae) |
| 1998 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | AS Vénus | AS Pirae | só o campeão na lista da RSSSF (e o vice, AS Pirae) |
| 1998/99 | jogos incompletos: pontos corridos; 3 pontos por vitória, 1 por empate e 0 por derrota | 6 | 6 | 22 | 0 | AS Vénus | AS Pirae | a página da RSSSF traz só parte dos jogos (muitos só com "venceu"/"perdeu", sem placar, que ficam de fora) e tabelas às vezes parciais |
| 1999/00 | jogos incompletos: pontos corridos (10 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 18 | 18 | 48 | 0 | AS Vénus | AS Pirae | a página da RSSSF traz só parte dos jogos (muitos só com "venceu"/"perdeu", sem placar, que ficam de fora) e tabelas às vezes parciais |
| 2000/01 | jogos incompletos: pontos corridos; 3 pontos por vitória, 1 por empate e 0 por derrota | 19 | 19 | 71 | 0 | AS Pirae |  | a página da RSSSF traz só parte dos jogos (muitos só com "venceu"/"perdeu", sem placar, que ficam de fora) e tabelas às vezes parciais |
| 2001/02 | jogos incompletos: fase regular + playoff do título (5 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 27 | 27 | 96 | 0 | AS Vénus | AS Pirae | o Juventus abandonou o campeonato no meio da temporada; a página da RSSSF traz só parte dos jogos (muitos só com "venceu"/"perdeu", sem placar, que ficam de fora) e tabelas às vezes parciais |
| 2002/03 | jogos incompletos: fase regular (10 clubes) + playoff do título (5 clubes) + grupo do rebaixamento (5 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 86 | 86 | 300 | 32 | AS Pirae | AS Manu-Ura | a página da RSSSF traz só parte dos jogos (muitos só com "venceu"/"perdeu", sem placar, que ficam de fora) e tabelas às vezes parciais |
| 2003/04 | jogos incompletos: fase regular (8 clubes) + playoff do título (4 clubes) + grupo do rebaixamento (4 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 73 | 73 | 274 | 11 | AS Manu-Ura | AS Pirae | a página da RSSSF traz só parte dos jogos (muitos só com "venceu"/"perdeu", sem placar, que ficam de fora) e tabelas às vezes parciais |
| 2004/05 | jogos incompletos: fase regular + playoff do título + grupo do rebaixamento; 4 pontos por vitória, 2 por empate e 1 por derrota | 19 | 19 | 87 | 0 | AS Tefana | AS Pirae | a página da RSSSF traz só parte dos jogos (muitos só com "venceu"/"perdeu", sem placar, que ficam de fora) e tabelas às vezes parciais |
| 2005/06 | fase regular (9 clubes) + playoff do título (5 clubes) + grupo do rebaixamento (4 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 106 | 106 | 354 | 0 | AS Pirae | AS Tefana |  |
| 2006/07 | fase regular (9 clubes) + playoff do título (5 clubes) + grupo do rebaixamento (4 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 104 | 104 | 389 | 0 | AS Manu-Ura | AS Tefana |  |
| 2007/08 | fase regular (10 clubes) + playoff do título (4 clubes) + grupo do rebaixamento (6 clubes); 3 pontos por vitória, 2 por empate e 1 por derrota | 117 | 117 | 353 | 35 | AS Manu-Ura | AS Tefana |  |
| 2008/09 | fase regular (10 clubes) + playoff do título (7 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 132 | 132 | 478 | 33 | AS Manu-Ura | AS Tefana | a seleção sub-20 do Taiti ("Tahiti U-20") jogou a fase regular no lugar de um clube |
| 2009/10 | fase regular (9 clubes) + playoff do título (7 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 115 | 115 | 374 | 0 | AS Tefana | AS Vaiete |  |
| 2010/11 | jogos incompletos: fase regular (10 clubes) + playoff do título (7 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 90 | 90 | 322 | 0 | AS Tefana | AS Dragon | o playoff do título só tem a tabela na RSSSF |
| 2011/12 | jogos incompletos: fase regular (11 clubes) + playoff do título (8 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 0 | 0 | 0 | 0 | AS Dragon | AS Tamarii Faa'a | a RSSSF só tem as tabelas da fase regular e do playoff do título |
| 2012/13 | fase regular (11 clubes) + playoff do título (6 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 85 | 85 | 337 | 0 | AS Dragon | AS Tamarii Faa'a |  |
| 2013/14 | fase regular (10 clubes) + playoff do título (6 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 75 | 75 | 358 | 0 | AS Pirae | AS Tefana |  |
| 2014/15 | fase regular (10 clubes) + playoff do título (6 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 75 | 75 | 442 | 0 | AS Tefana | AS Pirae |  |
| 2015/16 | fase regular (8 clubes) + semifinais + final; 4 pontos por vitória, 2 por empate e 1 por derrota | 87 | 87 | 418 | 0 | AS Tefana | Central Sport |  |
| 2016/17 | fase regular (10 clubes) + semifinais + final; 4 pontos por vitória, 2 por empate e 1 por derrota | 138 | 138 | 624 | 2 | AS Dragon | AS Vénus |  |
| 2017/18 | pontos corridos (10 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 135 | 135 | 803 | 0 | Central Sport | AS Tefana |  |
| 2018/19 | pontos corridos (10 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 136 | 136 | 630 | 0 | AS Vénus | AS Tiare Tahiti |  |
| 2019/20 | pontos corridos (10 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 75 | 75 | 333 | 0 | AS Pirae | AS Vénus | temporada interrompida pela covid-19; o AS Pirae, 1º da tabela, foi declarado campeão |
| 2020/21 | fase regular (13 clubes) + playoff do título (7 clubes) + grupo do rebaixamento (6 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 129 | 129 | 636 | 0 | AS Pirae | AS Vénus | covid-19: turno único na fase regular, depois os playoffs |
| 2021/22 | pontos corridos (12 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 132 | 132 | 670 | 0 | AS Pirae | AS Dragon |  |
| 2022/23 | fase regular (12 clubes) + playoff do título (6 clubes) + grupo do rebaixamento (6 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 126 | 126 | 668 | 0 | AS Tefana | AS Pirae |  |
| 2023/24 | fase regular (12 clubes) + playoff do título (6 clubes) + grupo do rebaixamento (6 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 127 | 127 | 692 | 0 | AS Pirae | AS Vénus |  |
| 2024/25 | pontos corridos (10 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 136 | 136 | 720 | 0 | AS Vénus | AS Pirae |  |
| 2025/26 | fase regular (10 clubes) + playoff do título (6 clubes) + grupo do rebaixamento (5 clubes); 4 pontos por vitória, 2 por empate e 1 por derrota | 120 | 120 | 633 | 0 | AS Tefana | AS Pirae |  |

## O que não deu para coletar

- Jogos e tabelas de 1948-1967, 1972-1998 (só o campeão; o vice em 8 anos): nenhuma fonte aberta.
- Jogos de 1998/99 a 2004/05 só em parte (muitos só com "venceu"/"perdeu"), de 2010/11 (playoff) e de 2011/12.
- Hora, estádio, público, cartões e artilheiros.
