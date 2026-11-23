# Campeonato Uruguaio (1ª divisão) — coleta de dados

Gerado por `python coleta/uru-1/importar.py`. Pacote em `data/coleta/uru-1/pacote/`.

**Edições:** 126, uma por título de campeão uruguaio da 1ª divisão, de 1900 a 2025, como na lista de campeões da RSSSF (`uruchamp.html`). Os cismas de 1923 e 1924 dão duas edições cada ("1923 AUF" e "1923 FUF"), como a RSSSF conta; 1926 é o Torneo del Consejo Provisorio. Sem edição: 1904 e 1930 (não houve campeonato) e 1925 (AUF e FUF não terminaram). 1948 entra sem campeão (abandonado na greve dos jogadores). De 2005/06 a 2015/16 as temporadas seguem o calendário europeu; "2005" é o Torneo Uruguay Especial e "2016" a Transición. Apertura, Intermedio e Clausura não davam título de campeão uruguaio: são fases da edição, com as finais de cada um, a tabela anual e as finais do campeonato.

**Edições sem jogos (45):** 1902-1903, 1906-1907, 1909-1915, 1917-1931 (com AUF e FUF) e 1975-1993. Nenhuma fonte pública que achamos tem os jogos desses anos (RSSSF, ogol e Wikipédias em espanhol e inglês trazem só a tabela final; para 1975-1993 a RSSSF tem só a liguilla pré-Libertadores). Elas entram com a tabela final da RSSSF (`uruhist.html`) como classificação e o campeão, sem jogos.

**Fora do pacote:** as liguillas pré-Libertadores, o Torneo Integración (1994), o Torneo Nacional (1996), a Copa Artigas, o Torneo Permanencia (2001-2002), o Reclasificatorio (2004), a Copa AUF Uruguay, a Supercopa e os jogos de promoção contra clubes da 2ª divisão.

**Fontes:** RSSSF (uma página por temporada, `data/coleta/uru-1/rsssf/`: base de jogos de 1932-1959, 1965 e 1994 em diante, com fases, grupos, rodadas, datas e autores dos gols; as tabelas da própria página e a lista de tabelas finais `uruhist.html`, de 1900 a 2000, são a conferência); Wikipédia em espanhol (páginas "Campeonato Uruguayo de Primera División <ano>": jogos de 1900, 1901, 1905, 1908, 1916, 1960-1964 e 1966-1974, por rodada, sem autores; em 1969 no lugar da RSSSF, que tem só 18 das 20 rodadas); ogol (calendários de 2005/06 em diante: rodada e data que faltam, conferência de placar e o nome de cada clube no ogol); ESPN (liga `uru.1`, 2005 em diante: hora, estádio e público; gols com minuto e cartões de 2005 a 2013); Wikipédia em inglês (lista de campeões da AUF, segunda fonte do campeão; não traz a FUF nem 1926).

**Clubes:** C.U.R.C.C. (1900-1913) entra como Peñarol, como a RSSSF e a Wikipédia contam (a seção de futebol do C.U.R.C.C. virou o Peñarol; o Nacional contesta). Defensor e Defensor Sporting são um clube só; Miramar, Misiones e Miramar Misiones (fusão de 1980) ficam separados; o River Plate amador (River Plate FC, até 1929) não é o atual (River Plate de Montevideo, de 1932). Homônimos de clubes do banco levam a cidade (Liverpool de Montevideo, Racing de Montevideo, River Plate de Montevideo...).

**Regras:** o placar é o da RSSSF (ou da Wikipédia, nos anos dela); o ogol só completa rodada e data e entra como conferência. Jogo decidido no tribunal leva o placar dado (`awd`) ou, quando o tribunal só deu a vitória ("awarded win to X; goal records unchanged"), fica sem placar como `awd`, com o placar de campo na observação (a tabela conta a vitória com os gols de campo). Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos por vitória: 2 até 1994 e 3 a partir de 1995.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1900 | 4 | 12 (12) | 65 | 0 | 0 / 1 | Peñarol | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1901 | 5 | 20 (20) | 65 | 0 | 0 / 1 | Peñarol | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1902 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Nacional | RSSSF (uruhist) |
| 1903 | 7 | 0 (0) | 0 | 0 | 0 / 0 | Nacional | RSSSF (uruhist) |
| 1905 | 5 | 20 (20) | 35 | 0 | 0 / 1 | Peñarol | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1906 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Montevideo Wanderers | RSSSF (uruhist) |
| 1907 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Peñarol | RSSSF (uruhist) |
| 1908 | 10 | 89 (89) | 257 | 0 | 0 / 1 | River Plate FC | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1909 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Montevideo Wanderers | RSSSF (uruhist) |
| 1910 | 9 | 0 (0) | 0 | 0 | 0 / 0 | River Plate FC | RSSSF (uruhist) |
| 1911 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Peñarol | RSSSF (uruhist) |
| 1912 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Nacional | RSSSF (uruhist) |
| 1913 | 8 | 0 (0) | 0 | 0 | 0 / 0 | River Plate FC | RSSSF (uruhist) |
| 1914 | 8 | 0 (0) | 0 | 0 | 0 / 0 | River Plate FC | RSSSF (uruhist) |
| 1915 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Nacional | RSSSF (uruhist) |
| 1916 | 9 | 72 (72) | 154 | 0 | 0 / 1 | Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1917 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Nacional | RSSSF (uruhist) |
| 1918 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Peñarol | RSSSF (uruhist) |
| 1919 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Nacional | RSSSF (uruhist) |
| 1920 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Nacional | RSSSF (uruhist) |
| 1921 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Peñarol | RSSSF (uruhist) |
| 1922 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Nacional | RSSSF (uruhist) |
| 1923 AUF | 12 | 0 (0) | 0 | 0 | 0 / 0 | Nacional | RSSSF (uruhist) |
| 1923 FUF | 32 | 0 (0) | 0 | 0 | 0 / 0 | None | RSSSF (uruhist) |
| 1924 AUF | 12 | 0 (0) | 0 | 0 | 0 / 0 | Nacional | RSSSF (uruhist) |
| 1924 FUF | 17 | 0 (0) | 0 | 0 | 0 / 0 | None | RSSSF (uruhist) |
| 1926 | 10 | 0 (0) | 0 | 0 | 0 / 0 | None | RSSSF (uruhist) |
| 1927 | 20 | 0 (0) | 0 | 0 | 0 / 0 | Rampla Juniors | RSSSF (uruhist) |
| 1928 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Peñarol | RSSSF (uruhist) |
| 1929 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Peñarol | RSSSF (uruhist) |
| 1931 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Montevideo Wanderers | RSSSF (uruhist) |
| 1932 | 10 | 135 (135) | 396 | 0 | 0 / 1 | Peñarol | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1933 | 10 | 138 (138) | 404 | 0 | 0 / 1 | Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1934 | 10 | 135 (135) | 375 | 0 | 0 / 1 | Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1935 | 10 | 90 (90) | 274 | 0 | 1 / 0 | Peñarol | RSSSF (uru35) |
| 1936 | 10 | 90 (90) | 287 | 0 | 1 / 0 | Peñarol | RSSSF (uru36) |
| 1937 | 10 | 91 (91) | 333 | 0 | 1 / 0 | Peñarol | RSSSF (uru37) |
| 1938 | 11 | 110 (110) | 380 | 0 | 1 / 0 | Peñarol | RSSSF (uru38) |
| 1939 | 11 | 111 (111) | 380 | 0 | 1 / 0 | Nacional | RSSSF (uru39) |
| 1940 | 11 | 110 (110) | 421 | 0 | 1 / 0 | Nacional | RSSSF (uru40) |
| 1941 | 11 | 110 (110) | 419 | 0 | 1 / 0 | Nacional | RSSSF (uru41) |
| 1942 | 10 | 90 (90) | 324 | 0 | 1 / 0 | Nacional | RSSSF (uru42) |
| 1943 | 10 | 90 (90) | 343 | 0 | 1 / 0 | Nacional | RSSSF (uru43) |
| 1944 | 10 | 92 (92) | 329 | 0 | 1 / 0 | Peñarol | RSSSF (uru44) |
| 1945 | 10 | 90 (90) | 352 | 0 | 1 / 0 | Peñarol | RSSSF (uru45) |
| 1946 | 10 | 90 (90) | 350 | 0 | 1 / 0 | Nacional | RSSSF (uru46) |
| 1947 | 10 | 93 (93) | 325 | 0 | 1 / 0 | Nacional | RSSSF (uru47) |
| 1948 | 10 | 50 (50) | 190 | 0 | 1 / 0 | None | RSSSF (uru48) |
| 1949 | 10 | 90 (90) | 323 | 0 | 1 / 0 | Peñarol | RSSSF (uru49) |
| 1950 | 10 | 93 (93) | 330 | 0 | 1 / 0 | Nacional | RSSSF (uru50) |
| 1951 | 10 | 90 (90) | 319 | 0 | 0 / 1 | Peñarol | RSSSF (uru51) |
| 1952 | 10 | 91 (91) | 335 | 0 | 1 / 0 | Nacional | RSSSF (uru52) |
| 1953 | 10 | 90 (90) | 290 | 0 | 1 / 0 | Peñarol | RSSSF (uru53) |
| 1954 | 10 | 90 (90) | 264 | 0 | 1 / 0 | Peñarol | RSSSF (uru54) |
| 1955 | 10 | 90 (90) | 294 | 0 | 1 / 0 | Nacional | RSSSF (uru55) |
| 1956 | 10 | 90 (90) | 315 | 0 | 1 / 0 | Nacional | RSSSF (uru56) |
| 1957 | 10 | 90 (90) | 293 | 0 | 1 / 0 | Nacional | RSSSF (uru57) |
| 1958 | 10 | 90 (90) | 271 | 0 | 1 / 0 | Peñarol | RSSSF (uru58) |
| 1959 | 10 | 91 (91) | 287 | 0 | 1 / 0 | Peñarol | RSSSF (uru59) |
| 1960 | 10 | 91 (91) | 273 | 0 | 0 / 1 | Peñarol | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1961 | 10 | 92 (92) | 309 | 0 | 0 / 1 | Peñarol | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1962 | 10 | 90 (90) | 290 | 0 | 0 / 1 | Peñarol | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1963 | 10 | 90 (90) | 268 | 0 | 1 / 0 | Nacional | RSSSF (uruhist) |
| 1964 | 10 | 90 (90) | 254 | 0 | 1 / 0 | Peñarol | RSSSF (uruhist) |
| 1965 | 10 | 90 (90) | 256 | 0 | 0 / 1 | Peñarol | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1966 | 10 | 90 (90) | 220 | 0 | 1 / 0 | Nacional | RSSSF (uruhist) |
| 1967 | 10 | 90 (90) | 204 | 0 | 0 / 1 | Peñarol | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1968 | 10 | 90 (90) | 185 | 0 | 1 / 0 | Peñarol | RSSSF (uruhist) |
| 1969 | 11 | 125 (125) | 297 | 0 | 2 / 0 | Nacional | RSSSF (uruhist) |
| 1970 | 11 | 135 (135) | 307 | 0 | 2 / 0 | Nacional | RSSSF (uruhist) |
| 1971 | 12 | 162 (162) | 403 | 0 | 2 / 0 | Nacional | RSSSF (uruhist) |
| 1972 | 12 | 132 (132) | 308 | 0 | 1 / 0 | Nacional | RSSSF (uruhist) |
| 1973 | 12 | 132 (132) | 282 | 0 | 1 / 0 | Peñarol | RSSSF (uruhist) |
| 1974 | 12 | 132 (132) | 367 | 0 | 1 / 0 | Peñarol | RSSSF (uruhist) |
| 1975 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Peñarol | RSSSF (uruhist) |
| 1976 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Defensor Sporting | RSSSF (uruhist) |
| 1977 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Nacional | RSSSF (uruhist) |
| 1978 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Peñarol | RSSSF (uruhist) |
| 1979 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Peñarol | RSSSF (uruhist) |
| 1980 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Nacional | RSSSF (uruhist) |
| 1981 | 15 | 0 (0) | 0 | 0 | 0 / 0 | Peñarol | RSSSF (uruhist) |
| 1982 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Peñarol | RSSSF (uruhist) |
| 1983 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Nacional | RSSSF (uruhist) |
| 1984 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Central Español | RSSSF (uruhist) |
| 1985 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Peñarol | RSSSF (uruhist) |
| 1986 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Peñarol | RSSSF (uruhist) |
| 1987 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Defensor Sporting | RSSSF (uruhist) |
| 1988 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Danubio | RSSSF (uruhist) |
| 1989 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Progreso | RSSSF (uruhist) |
| 1990 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Bella Vista | RSSSF (uruhist) |
| 1991 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Defensor Sporting | RSSSF (uruhist) |
| 1992 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Nacional | RSSSF (uruhist) |
| 1993 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Peñarol | RSSSF (uruhist) |
| 1994 | 13 | 159 (159) | 384 | 0 | 3 / 3 | Peñarol | RSSSF (uru94) |
| 1995 | 13 | 161 (161) | 412 | 35 | 3 / 1 | Peñarol | RSSSF (uruhist) |
| 1996 | 12 | 134 (134) | 310 | 0 | 3 / 2 | Peñarol | RSSSF (uruhist) |
| 1997 | 13 | 137 (137) | 371 | 0 | 1 / 3 | Peñarol | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1998 | 12 | 132 (132) | 331 | 0 | 1 / 2 | Nacional | RSSSF (uru98) |
| 1999 | 15 | 214 (214) | 617 | 287 | 3 / 0 | Peñarol | RSSSF (uru99) |
| 2000 | 18 | 293 (292) | 926 | 624 | 1 / 2 | Nacional | RSSSF (uru00) |
| 2001 | 18 | 245 (245) | 717 | 450 | 6 / 0 | Nacional | RSSSF (uru01) |
| 2002 | 18 | 246 (246) | 788 | 532 | 6 / 1 | Nacional | RSSSF (uru02) |
| 2003 | 18 | 307 (307) | 868 | 527 | 4 / 0 | Peñarol | RSSSF (uru03) |
| 2004 | 18 | 252 (251) | 657 | 428 | 4 / 1 | Danubio | RSSSF (uru04) |
| 2005 | 18 | 155 (155) | 445 | 237 | 1 / 0 | Nacional | RSSSF (uru05) |
| 2005/06 | 20 | 293 (293) | 801 | 764 | 3 / 0 | Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2006/07 | 16 | 245 (245) | 691 | 684 | 3 / 0 | Danubio | RSSSF (uru07) |
| 2007/08 | 16 | 244 (243) | 726 | 694 | 3 / 0 | Defensor Sporting | RSSSF (uru08) |
| 2008/09 | 16 | 233 (233) | 639 | 620 | 3 / 0 | Nacional | RSSSF (uru09) |
| 2009/10 | 16 | 243 (243) | 711 | 690 | 3 / 0 | Peñarol | RSSSF (uru2010) |
| 2010/11 | 16 | 241 (241) | 668 | 657 | 3 / 0 | Nacional | RSSSF (uru2011) |
| 2011/12 | 16 | 243 (242) | 665 | 660 | 3 / 0 | Nacional | RSSSF (uru2012) |
| 2012/13 | 16 | 241 (241) | 633 | 633 | 3 / 0 | Peñarol | RSSSF (uru2013) |
| 2013/14 | 16 | 246 (246) | 700 | 580 | 3 / 0 | Danubio | RSSSF (uru2014) |
| 2014/15 | 16 | 241 (241) | 690 | 489 | 3 / 0 | Nacional | RSSSF (uru2015) |
| 2015/16 | 16 | 241 (241) | 637 | 491 | 3 / 0 | Peñarol | RSSSF (uru2016) |
| 2016 | 16 | 120 (120) | 289 | 228 | 1 / 0 | Nacional | RSSSF (uru2016a) |
| 2017 | 16 | 304 (304) | 797 | 596 | 5 / 0 | Peñarol | RSSSF (uru2017) |
| 2018 | 16 | 292 (292) | 705 | 463 | 6 / 0 | Peñarol | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2019 | 16 | 299 (299) | 802 | 501 | 5 / 0 | Nacional | RSSSF (uru2019) |
| 2020 | 16 | 302 (301) | 774 | 419 | 5 / 0 | Nacional | RSSSF (uru2020) |
| 2021 | 16 | 241 (241) | 608 | 356 | 3 / 0 | Peñarol | RSSSF (uru2021) |
| 2022 | 16 | 300 (299) | 647 | 393 | 5 / 0 | Nacional | RSSSF (uru2022) |
| 2023 | 16 | 301 (300) | 684 | 418 | 5 / 0 | Liverpool de Montevideo | RSSSF (uru2023) |
| 2024 | 16 | 297 (297) | 723 | 404 | 5 / 0 | Peñarol | RSSSF (uru2024) |
| 2025 | 16 | 300 (300) | 700 | 459 | 5 / 0 | Nacional | RSSSF (uru2025) |

## Conferência e correções, edição a edição

### 1900

- tabela publicada x jogos — uruhist:14: Albion de Montevideo tabela [6, 4, 0, 2, 22, 6] jogos [6, 4, 0, 2, 22, 8] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uruhist:14: Montevideo FC tabela [6, 1, 0, 5, 3, 31] jogos [6, 1, 0, 5, 4, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1901

- tabela publicada x jogos — uruhist:32: Peñarol tabela [8, 7, 1, 0, 30, 4] jogos [8, 7, 1, 0, 29, 4] — a diferença vem de Peñarol x Albion de Montevideo (1901-08-11), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — uruhist:32: Montevideo FC tabela [8, 1, 1, 6, 5, 19] jogos [8, 1, 1, 6, 5, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uruhist:32: Albion de Montevideo tabela [8, 1, 1, 6, 3, 17] jogos [8, 1, 1, 6, 5, 16] — a diferença vem de Peñarol x Albion de Montevideo (1901-08-11), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- W.O./pontos para o mandante — Peñarol Albion de Montevideo (1901-08-11)

### 1902

- sem ocorrências

### 1903

- sem ocorrências

### 1905

- tabela publicada x jogos — uruhist:88: Peñarol tabela [8, 8, 0, 0, 21, 0] jogos [8, 8, 0, 0, 8, 0] — a diferença vem de Albion de Montevideo x Peñarol (1905-06-01), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — uruhist:88: Montevideo FC tabela [8, 2, 1, 5, 6, 18] jogos [8, 2, 1, 5, 6, 12] — a diferença vem de Albion de Montevideo x Montevideo FC (1905-05-28), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — uruhist:88: Albion de Montevideo tabela [8, 0, 0, 8, 0, 14] jogos [8, 0, 0, 8, 0, 7] — a diferença vem de Albion de Montevideo x Montevideo FC (1905-05-28), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- W.O./pontos para o visitante — Albion de Montevideo Montevideo FC (1905-05-28)
- W.O./pontos para o visitante — Albion de Montevideo Peñarol (1905-06-01)
- W.O./pontos para o mandante — Peñarol Albion de Montevideo (1905-06-25)
- W.O./pontos para o visitante — Albion de Montevideo Nacional (1905-06-29)
- W.O./pontos para o mandante — Montevideo Wanderers Albion de Montevideo (1905-08-25)
- W.O./pontos para o mandante — Montevideo FC Albion de Montevideo (1905-09-17)
- W.O./pontos para o mandante — Peñarol Montevideo FC (1905-10-08)

### 1906

- sem ocorrências

### 1907

- sem ocorrências

### 1908

- tabela publicada x jogos — uruhist:138: Nacional tabela [17, 11, 2, 4, 34, 16] jogos [17, 11, 2, 4, 33, 14] — a diferença vem de Albion de Montevideo x Nacional (1908-10-18), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — uruhist:138: Bristol tabela [18, 8, 1, 9, 33, 25] jogos [18, 7, 1, 10, 34, 25] — a diferença vem de Intrépido x Bristol (1908-08-24), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — uruhist:138: Albion de Montevideo tabela [18, 7, 3, 8, 18, 36] jogos [18, 7, 3, 8, 16, 35] — a diferença vem de Albion de Montevideo x Nacional (1908-10-18), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — uruhist:138: Intrépido tabela [18, 0, 0, 18, 5, 42] jogos [18, 1, 0, 17, 5, 43] — a diferença vem de Intrépido x Bristol (1908-08-24), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- W.O./pontos para o mandante — Peñarol Intrépido (1908-04-19): Intrépido no se presentó
- W.O./pontos para o mandante — Montevideo Wanderers Nacional (1908-11-15): Postergado originalmente, para el 15 de noviembre Nacional se había retirado.
- W.O./pontos para o mandante — Montevideo FC Peñarol (1908-10-18): Postergado originalmente, para el 18 de octubre C.U.R.C.C. se había retirado
- W.O./pontos para o mandante — River Plate FC Albion de Montevideo (1908-09-20): Albion no se presentó
- W.O./pontos para o mandante — Albion de Montevideo Nacional (1908-10-18): Partido ganado por Nacional 3-1 el 31 de mayo, posteriormente anulado. Para el 18 de octubre Nacional se había retirado.
- W.O./pontos para o mandante — Montevideo Wanderers Intrépido (1908-07-05)
- W.O./pontos para o visitante — Peñarol Bristol (1908-07-26): C.U.R.C.C. debía jugar un desempate con Albion por Copa Competencia, luego al desafiliarse el 16 de septiembre se le daría por perdido este encuentro
- W.O./pontos para o visitante — Peñarol Montevideo Wanderers (1908-09-06): C.U.R.C.C. debía jugar un desempate con Dublín por Copa de Honor, no se presentó y posteriormente se desafiliaría
- W.O./pontos para o mandante — Montevideo FC Nacional (1908-10-25): Encuentro postergado originalmente, para el 25 de octubre se había retirado
- W.O./pontos para o mandante — Intrépido Bristol (1908-08-24): Intrépido no se presentó
- W.O./pontos para o visitante — Intrépido Albion de Montevideo (s/d): Intrépido no se presentó
- W.O./pontos para o mandante — Dublin Peñarol (1908-10-04): C.U.R.C.C. estaba desafiliado
- W.O./pontos para o visitante — Intrépido Nacional (1908-10-04): Intrépido no se presentó. Al poco tiempo se retira Nacional
- W.O./pontos para o mandante — Montevideo Wanderers Montevideo FC (1908-10-04): Montevideo no se presentó
- W.O./pontos para o visitante — Peñarol Montevideo FC (1908-07-19): Postergado por el choque de C.U.R.C.C. vs. Albion por Copa Competencia, posteriormente al desafiliarse C.U.R.C.C. perdió este encuentro.
- W.O./pontos para o visitante — Peñarol Albion de Montevideo (1908-10-25): C.U.R.C.C. estaba desafiliado
- W.O./pontos para o visitante — Intrépido French (s/d): Luego de sucesivas ausencias, Intrépido fue descalificado
- W.O./pontos para o visitante — Peñarol River Plate FC (1908-11-15): C.U.R.C.C. estaba desafiliado
- W.O./pontos para o mandante — Nacional Albion de Montevideo (1908-06-18): El partido fue ganado por Albion 2-1, pero lo perdió en la liga por alinear indebidamente a un futbolista
- W.O./pontos para o visitante — Intrépido Montevideo FC (1908-08-09): Intrépido fue descalificado

### 1909

- sem ocorrências

### 1910

- sem ocorrências

### 1911

- 3º pela lista oficial: Nacional (a tabela o punha em 5º)

### 1912

- sem ocorrências

### 1913

- tabela da RSSSF (uruhist) e da Wikipédia em espanhol diferem um pouco; fica a da RSSSF, base da coleta (UY-012)

### 1914

- sem ocorrências

### 1915

- sem ocorrências

### 1916

- tabela publicada x jogos — uruhist:303: Montevideo Wanderers tabela [16, 7, 3, 6, 13, 20] jogos [16, 7, 3, 6, 14, 20] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uruhist:303: River Plate FC tabela [16, 4, 5, 7, 18, 17] jogos [16, 4, 5, 7, 18, 18] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uruhist:303: Universal de Montevideo tabela [16, 3, 7, 6, 16, 19] jogos [16, 4, 5, 7, 16, 19] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uruhist:303: Reformers tabela [16, 5, 2, 9, 10, 22] jogos [16, 4, 4, 8, 10, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1917

- tabela da RSSSF (uruhist) e da Wikipédia em espanhol diferem um pouco; fica a da RSSSF (UY-012)

### 1918

- sem ocorrências

### 1919

- tabela da RSSSF (uruhist) e da Wikipédia em espanhol diferem um pouco; fica a da RSSSF (UY-012)

### 1920

- tabela da RSSSF (uruhist) e da Wikipédia em espanhol diferem um pouco; fica a da RSSSF (UY-012)

### 1921

- sem ocorrências

### 1922

- sem ocorrências

### 1923 AUF

- sem ocorrências

### 1923 FUF

- cisma do futebol uruguaio (1922-1925): a FUF foi fundada por Peñarol e Central depois de expulsos da AUF; as duas ligas tiveram campeonato; título não reconhecido pela AUF: edição sem campeão (D-09)

### 1924 AUF

- sem ocorrências

### 1924 FUF

- cisma do futebol uruguaio (1922-1925): a FUF foi fundada por Peñarol e Central depois de expulsos da AUF; as duas ligas tiveram campeonato; título não reconhecido pela AUF: edição sem campeão (D-09)

### 1926

- torneio de unificação depois da dissolução da FUF, com clubes das duas ligas (RSSSF); título não reconhecido pela AUF: edição sem campeão (D-09)

### 1927

- sem ocorrências

### 1928

- sem ocorrências

### 1929

- sem ocorrências

### 1931

- sem ocorrências

### 1932

- tabela publicada x jogos — uru32:23: Rampla Juniors tabela [27, 14, 7, 6, 66, 32] jogos [27, 14, 8, 5, 66, 32] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uru32:23: Defensor Sporting tabela [27, 12, 7, 8, 51, 41] jogos [27, 12, 7, 8, 50, 41] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uru32:23: Bella Vista tabela [27, 8, 7, 12, 30, 35] jogos [27, 8, 7, 12, 30, 34] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uru32:23: Sud América tabela [27, 7, 6, 14, 28, 47] jogos [27, 6, 7, 14, 28, 47] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1933

- tabela publicada x jogos — uru33:16: Defensor Sporting tabela [27, 12, 5, 10, 50, 39] jogos [27, 13, 4, 10, 51, 39] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uru33:16: River Plate de Montevideo tabela [27, 6, 6, 15, 19, 45] jogos [27, 5, 7, 15, 18, 45] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1934

- tabela publicada x jogos — uru34:16: Nacional tabela [27, 17, 7, 3, 51, 17] jogos [27, 17, 7, 3, 51, 18] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uru34:16: Montevideo Wanderers tabela [27, 15, 5, 7, 47, 28] jogos [27, 14, 7, 6, 46, 27] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uru34:16: Rampla Juniors tabela [27, 10, 8, 9, 42, 37] jogos [27, 10, 8, 9, 43, 37] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1935

- sem ocorrências

### 1936

- sem ocorrências

### 1937

- sem ocorrências

### 1938

- sem ocorrências

### 1939

- corrigido — Nacional x Racing de Montevideo (None): Nacional 6-1 Racing em campo; pontos dados ao Racing (jogador irregular do Nacional); a tabela conta os gols de campo
- W.O./pontos para o visitante — Nacional Racing de Montevideo (s/d): *, awarded to Racing

### 1940

- sem ocorrências

### 1941

- sem ocorrências

### 1942

- sem ocorrências

### 1943

- sem ocorrências

### 1944

- sem ocorrências

### 1945

- sem ocorrências

### 1946

- sem ocorrências

### 1947

- sem vice: o triangular pelo 2º lugar não terminou (D-22 c)
- corrigido — Defensor Sporting x Peñarol (None): jogo do triangular pelo 2º lugar (a página abre rodadas dentro do desempate)
- corrigido — Peñarol x Rampla Juniors (None): jogo do triangular pelo 2º lugar
- corrigido — Defensor Sporting x Rampla Juniors (None): jogo do triangular pelo 2º lugar (não jogado)
- não jogado — Defensor Sporting Rampla Juniors (s/d)

### 1948

- campeonato abandonado na 10ª rodada pela greve dos jogadores; sem campeão (RSSSF)

### 1949

- sem ocorrências

### 1950

- sem ocorrências

### 1951

- a tabela publicada (RSSSF e es concordam) não fecha com nenhum jogo da página (Nacional e Danubio com 1 vitória trocada); a classificação é a tabela publicada (UY-011)
- tabela publicada x jogos — uru51:16: Nacional tabela [18, 12, 3, 3, 50, 21] jogos [18, 11, 3, 4, 49, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uru51:16: Danubio tabela [18, 6, 4, 8, 30, 36] jogos [18, 7, 4, 7, 31, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1952

- sem ocorrências

### 1953

- sem ocorrências

### 1954

- vice Nacional (RSSSF e Wikipédia em inglês); a es dá o Danubio. Fica o da RSSSF até uma 3ª fonte (D-22 b, UY-007)

### 1955

- a es dá Sud América 15 e Liverpool 13 pontos; a RSSSF, 16 e 12 (ajustes de +1/-1); fica a RSSSF (UY-012)

### 1956

- sem ocorrências

### 1957

- sem ocorrências

### 1958

- sem ocorrências

### 1959

- sem ocorrências

### 1960

- tabela publicada x jogos — uruhist:1369: Cerro tabela [18, 13, 2, 3, 43, 21] jogos [18, 13, 2, 3, 42, 20] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uruhist:1369: Nacional tabela [18, 10, 4, 4, 45, 22] jogos [18, 10, 4, 4, 45, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uruhist:1369: Fénix tabela [18, 5, 6, 7, 20, 31] jogos [18, 5, 6, 7, 19, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uruhist:1369: Racing de Montevideo tabela [18, 7, 1, 10, 26, 32] jogos [18, 7, 1, 10, 25, 32] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uruhist:1369: Rampla Juniors tabela [18, 5, 5, 8, 20, 32] jogos [18, 5, 5, 8, 19, 32] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uruhist:1369: Montevideo Wanderers tabela [18, 5, 5, 8, 19, 27] jogos [18, 5, 5, 8, 19, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uruhist:1369: Liverpool de Montevideo tabela [18, 6, 2, 10, 25, 36] jogos [18, 6, 2, 10, 24, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1961

- tabela publicada x jogos — uruhist:1394: Defensor Sporting tabela [18, 9, 5, 4, 35, 27] jogos [18, 9, 5, 4, 34, 27] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uruhist:1394: Rampla Juniors tabela [18, 6, 3, 9, 25, 28] jogos [18, 6, 3, 9, 25, 27] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1962

- tabela publicada x jogos — uruhist:1418: Fénix tabela [18, 8, 2, 8, 25, 36] jogos [18, 8, 2, 8, 26, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uruhist:1418: Racing de Montevideo tabela [18, 4, 9, 5, 30, 33] jogos [18, 4, 9, 5, 30, 34] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1963

- sem ocorrências

### 1964

- sem ocorrências

### 1965

- tabela publicada x jogos — uru65:14: Nacional tabela [18, 12, 3, 3, 33, 14] jogos [18, 11, 4, 3, 33, 14] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uru65:14: Cerro tabela [18, 11, 3, 4, 31, 18] jogos [18, 11, 4, 3, 31, 18] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1966

- sem ocorrências

### 1967

- tabela publicada x jogos — uruhist:1528: Nacional tabela [18, 11, 5, 2, 26, 16] jogos [18, 11, 4, 3, 25, 16] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — uruhist:1528: Fénix tabela [18, 3, 5, 10, 15, 29] jogos [18, 4, 4, 10, 15, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1968

- sem ocorrências

### 1969

- sem ocorrências

### 1970

- sem ocorrências

### 1971

- sem ocorrências

### 1972

- W.O./pontos para o mandante — Huracán Buceo Peñarol (s/d)

### 1973

- sem ocorrências

### 1974

- sem ocorrências

### 1975

- sem ocorrências

### 1976

- sem ocorrências

### 1977

- sem ocorrências

### 1978

- sem ocorrências

### 1979

- sem ocorrências

### 1980

- sem ocorrências

### 1981

- sem ocorrências

### 1982

- sem ocorrências

### 1983

- sem ocorrências

### 1984

- sem ocorrências

### 1985

- sem ocorrências

### 1986

- sem ocorrências

### 1987

- sem ocorrências

### 1988

- sem ocorrências

### 1989

- sem ocorrências

### 1990

- sem ocorrências

### 1991

- tabela da RSSSF (uruhist) e da Wikipédia em espanhol diferem um pouco; fica a da RSSSF (UY-012)

### 1992

- sem ocorrências

### 1993

- sem ocorrências

### 1994

- tabela publicada x jogos — uru94:294: Progreso tabela [24, 7, 3, 14, 24, 28] jogos [24, 7, 3, 14, 24, 38] — a outra tabela publicada (uru94) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2273: Cerro tabela [24, 10, 9, 5, 31, 24] jogos [24, 9, 10, 5, 29, 23] — a outra tabela publicada (uru94) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2273: Central Español tabela [24, 7, 6, 11, 23, 36] jogos [24, 7, 7, 10, 22, 34] — a outra tabela publicada (uru94) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2301: Cerro tabela [12, 6, 3, 3, 16, 11] jogos [12, 5, 4, 3, 14, 10] — a outra tabela publicada (uru94) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2301: Central Español tabela [12, 2, 3, 7, 8, 20] jogos [12, 2, 4, 6, 7, 18] — a outra tabela publicada (uru94) fecha com os jogos: o erro é desta tabela
- corrigido — Peñarol x None (None): linha com os dois primeiros jogos da final ("1-1 1-1"): vira dois jogos escritos à mão (EXTRAS)

### 1995

- tabela publicada x jogos — uru95:166: Montevideo Wanderers tabela [12, 4, 1, 7, 11, 18] jogos [12, 4, 1, 7, 11, 20] — a outra tabela publicada (uru95) fecha com os jogos: o erro é desta tabela

### 1996

- tabela publicada x jogos — uruhist:2422: Nacional tabela [22, 14, 4, 4, 48, 23] jogos [22, 14, 4, 4, 50, 23] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2422: Danubio tabela [22, 10, 6, 6, 29, 26] jogos [22, 10, 6, 6, 31, 26] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2422: Huracán Buceo tabela [22, 9, 9, 4, 21, 17] jogos [22, 9, 9, 4, 23, 17] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2422: Rampla Juniors tabela [22, 7, 11, 4, 18, 15] jogos [22, 7, 11, 4, 20, 15] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2422: Montevideo Wanderers tabela [22, 6, 6, 10, 15, 31] jogos [22, 6, 6, 10, 17, 31] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2422: River Plate de Montevideo tabela [22, 5, 9, 8, 25, 26] jogos [22, 5, 9, 8, 27, 26] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2422: Liverpool de Montevideo tabela [22, 4, 10, 8, 17, 27] jogos [22, 4, 10, 8, 19, 27] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2422: Central Español tabela [22, 4, 8, 10, 16, 24] jogos [22, 4, 8, 10, 18, 24] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2422: Sud América tabela [22, 1, 5, 16, 5, 26] jogos [22, 1, 5, 16, 5, 42] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2469: Nacional tabela [11, 8, 1, 2, 23, 12] jogos [11, 8, 1, 2, 25, 12] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2469: Rampla Juniors tabela [11, 4, 6, 1, 9, 6] jogos [11, 4, 6, 1, 11, 6] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2469: Huracán Buceo tabela [11, 4, 6, 1, 8, 6] jogos [11, 4, 6, 1, 10, 6] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2469: Danubio tabela [11, 5, 2, 4, 17, 17] jogos [11, 5, 2, 4, 19, 17] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2469: Central Español tabela [11, 3, 5, 3, 8, 9] jogos [11, 3, 5, 3, 10, 9] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2469: River Plate de Montevideo tabela [11, 3, 4, 4, 14, 13] jogos [11, 3, 4, 4, 16, 13] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2469: Montevideo Wanderers tabela [11, 3, 4, 4, 8, 14] jogos [11, 3, 4, 4, 10, 14] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2469: Liverpool de Montevideo tabela [11, 2, 6, 3, 9, 14] jogos [11, 2, 6, 3, 11, 14] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2469: Sud América tabela [11, 0, 0, 11, 0, 9] jogos [11, 0, 0, 11, 0, 25] — a outra tabela publicada (uru96) fecha com os jogos: o erro é desta tabela
- decidido fora de campo — Sud América Montevideo Wanderers (s/d): 0-2 to Wanderers
- decidido fora de campo — Huracán Buceo Sud América (s/d): 2-0 to Huracán
- decidido fora de campo — Rampla Juniors Sud América (s/d): 2-0 to Rampla
- decidido fora de campo — Central Español Sud América (s/d): 2-0 to Central
- decidido fora de campo — Sud América River Plate de Montevideo (s/d): 0-2 to River
- decidido fora de campo — Nacional Sud América (s/d): 2-0 to Nacional
- decidido fora de campo — Liverpool de Montevideo Sud América (s/d): 2-0 to Liverpool
- decidido fora de campo — Danubio Sud América (s/d): 2-0 to Danubio

### 1997

- tabela publicada x jogos — uru97:144: Peñarol tabela [11, 7, 2, 2, 29, 15] jogos [11, 8, 2, 1, 31, 13] — a outra tabela publicada (uru97) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uru97:144: Rampla Juniors tabela [11, 2, 3, 6, 12, 14] jogos [11, 1, 3, 7, 10, 16] — a outra tabela publicada (uru97) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uru97:264: Peñarol tabela [22, 13, 5, 4, 51, 26] jogos [22, 14, 5, 3, 53, 24] — a outra tabela publicada (uru97) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uru97:264: Rampla Juniors tabela [22, 6, 5, 11, 24, 32] jogos [22, 5, 5, 12, 22, 34] — a outra tabela publicada (uru97) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2490: Peñarol tabela [22, 13, 5, 4, 51, 24] jogos [22, 14, 5, 3, 53, 24] — a outra tabela publicada (uru97) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uruhist:2490: Rampla Juniors tabela [22, 6, 5, 11, 22, 32] jogos [22, 5, 5, 12, 22, 34] — a outra tabela publicada (uru97) fecha com os jogos: o erro é desta tabela
- 3º pela lista oficial: River Plate de Montevideo (a tabela o punha em 4º)
- decidido fora de campo — Peñarol Rampla Juniors (1997-07-26): abandoned at 0-0 in 48'; awarded 2-0 to Rampla

### 1998

- tabela publicada x jogos — uru98:18: Rampla Juniors tabela [11, 3, 4, 4, 10, 14] jogos [11, 3, 4, 4, 10, 16] — a outra tabela publicada (uru98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uru98:283: Rampla Juniors tabela [22, 6, 6, 10, 20, 32] jogos [22, 6, 6, 10, 20, 34] — a outra tabela publicada (uru98) fecha com os jogos: o erro é desta tabela
- decidido fora de campo — Montevideo Wanderers Rampla Juniors (1998-03-14): awarded 4-2 due to ineligible player; originally 1-2

### 1999

- abandonado/suspenso, sem valer — Cerro Frontera Rivera (1999-10-10): abandoned at 0-1 in 45' due to crowd violence

### 2000

- tabela publicada x jogos — uru00:496: Cerro tabela [16, 5, 5, 6, 21, 24] jogos [16, 5, 5, 6, 23, 24] — a outra tabela publicada (uru00) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uru00:496: Racing de Montevideo tabela [16, 5, 5, 6, 20, 24] jogos [16, 5, 5, 6, 21, 24] — a outra tabela publicada (uru00) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uru00:496: Liverpool de Montevideo tabela [16, 2, 7, 7, 12, 24] jogos [16, 2, 7, 7, 12, 25] — a outra tabela publicada (uru00) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uru00:912: Racing de Montevideo tabela [33, 10, 8, 15, 45, 57] jogos [33, 10, 8, 15, 46, 57] — a outra tabela publicada (uru00) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uru00:912: Liverpool de Montevideo tabela [33, 7, 10, 16, 31, 54] jogos [33, 7, 10, 16, 31, 55] — a outra tabela publicada (uru00) fecha com os jogos: o erro é desta tabela
- abandonado/suspenso, sem valer — Racing de Montevideo Villa Española (2000-06-18): abandoned at 0-2 in 85' due to crowd violence
- abandonado/suspenso, sem valer — Liverpool de Montevideo River Plate de Montevideo (2000-09-08): abandoned at 1-1 at half-time due to thunderstorm

### 2001

- sem ocorrências

### 2002

- tabela publicada x jogos — uru02:904: Fénix tabela [35, 20, 7, 8, 86, 55] jogos [35, 19, 8, 8, 86, 55] — a outra tabela publicada (uru02) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — uru02:904: Danubio tabela [35, 18, 7, 10, 65, 46] jogos [35, 19, 6, 10, 65, 46] — a outra tabela publicada (uru02) fecha com os jogos: o erro é desta tabela
- vice pela lista oficial: Danubio (a tabela o punha em 4º)
- abandonado/suspenso, sem valer — Central Español Montevideo Wanderers (2002-10-06): abandoned at 0-1 in 66' due to rain

### 2003

- sem ocorrências

### 2004

- tabela publicada x jogos — uru04:849: Defensor Sporting tabela [27, 13, 10, 4, 43, 29] jogos [27, 13, 10, 4, 40, 26] — a outra tabela publicada (uru04) fecha com os jogos: o erro é desta tabela
- 3º pela lista oficial: Defensor Sporting (a tabela o punha em 9º)
- abandonado/suspenso, sem valer — Danubio Cerro (2004-05-19): abandoned at 1-0 in 22' after

### 2005

- torneio de transição para o calendário europeu; o Defensor não jogou a final e o título ficou com o Nacional
- decidido fora de campo — Peñarol Miramar Misiones (2005-07-02): awarded 1-3; abandoned at 1-1
- não jogado — Defensor Sporting Nacional (2005-07-03)
- não jogado — Nacional Defensor Sporting (2005-07-03)

### 2005/06

- ogol: 289 jogos casados (edição 37188 do ogol, 308 jogos)
- ESPN: 288 jogos casados
- tabela uru06:494 fora da conferência: "Annual Table 2005": soma o Torneo Especial 2005 e o Apertura 2005/06 (ano civil, para rebaixamento e vagas), não é tabela desta edição
- data diferente no ogol — Nacional x Rocha FC: RSSSF 2006-06-19, ogol 2006-06-24; fica a da RSSSF
- decidido fora de campo — Peñarol Miramar Misiones (2005-09-11): awarded 0-2; abandoned at 2-1 in 82'
- abandonado/suspenso, sem valer — Danubio Nacional (2005-12-10): abandoned at 2-3 in 44', ballboy was
- decidido fora de campo — Deportivo Colonia River Plate de Montevideo (2006-03-05): awarded 0-2; originally 3-2, Colonia
- abandonado/suspenso, sem valer — Rocha FC Miramar Misiones (2006-06-10): abandoned at 1-2 in 49'

### 2006/07

- ogol: 231 jogos casados (edição 8996 do ogol, 241 jogos)
- ESPN: 242 jogos casados
- placar diferente no ogol — Rampla Juniors x River Plate de Montevideo (2006-09-09): RSSSF 0-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Montevideo Wanderers x Central Español (2006-12-09): RSSSF 2-1, ogol 1-1; fica o da RSSSF
- data diferente no ogol — River Plate de Montevideo x Defensor Sporting: RSSSF 2007-03-24, ogol 2007-03-14; fica a da RSSSF
- placar diferente no ogol — Defensor Sporting x Rentistas (2007-03-21): RSSSF 2-2, ogol 2-0; fica o da RSSSF
- data diferente no ogol — Defensor Sporting x Rentistas: RSSSF 2007-03-21, ogol 2007-03-17; fica a da RSSSF
- placar diferente no ogol — Rampla Juniors x Nacional (2007-04-15): RSSSF 1-3, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Central Español x Defensor Sporting (2007-04-22): RSSSF 0-3, ogol 0-2; fica o da RSSSF
- placar diferente no ogol — Bella Vista x Liverpool de Montevideo (2007-05-19): RSSSF 2-1, ogol 1-2; fica o da RSSSF
- data diferente no ogol — Bella Vista x Liverpool de Montevideo: RSSSF 2007-05-19, ogol 2007-05-12; fica a da RSSSF
- data diferente no ogol — Nacional x Rentistas: RSSSF 2007-05-19, ogol 2007-05-12; fica a da RSSSF
- abandonado/suspenso, sem valer — Defensor Sporting Progreso (2007-04-14): abandoned at 3-1 in 52' due to storm
- abandonado/suspenso, sem valer — Peñarol Cerrito (2007-04-14): abandoned at 1-0 in 48' due to storm

### 2007/08

- ogol: 240 jogos casados (edição 1999 do ogol, 259 jogos)
- ESPN: 238 jogos casados
- 3º pela lista oficial: River Plate de Montevideo (a tabela o punha em 5º)
- placar diferente no ogol — Tacuarembó x Miramar Misiones (2007-09-09): RSSSF 1-0, ogol 0-0; fica o da RSSSF
- data diferente no ogol — River Plate de Montevideo x Peñarol: RSSSF 2008-06-01, ogol 2008-06-08; fica a da RSSSF
- abandonado/suspenso, sem valer — Miramar Misiones Progreso (2007-08-19): abandoned at 1-0 in 83' due to crowd
- decidido fora de campo — Defensor Sporting Liverpool de Montevideo (2008-03-23): awarded 3-5; originally 3-2;

### 2008/09

- ogol: 197 jogos casados (edição 3300 do ogol, 216 jogos)
- ESPN: 225 jogos casados
- 3º pela lista oficial: Cerro (a tabela o punha em 7º)
- data diferente no ogol — Juventud de Las Piedras x Nacional: RSSSF 2008-08-23, ogol 2008-08-31; fica a da RSSSF
- data diferente no ogol — Tacuarembó x Bella Vista: RSSSF 2008-08-24, ogol 2008-08-31; fica a da RSSSF
- data diferente no ogol — Montevideo Wanderers x Peñarol: RSSSF 2008-08-24, ogol 2008-08-31; fica a da RSSSF
- data diferente no ogol — Rampla Juniors x Central Español: RSSSF 2008-08-24, ogol 2008-08-31; fica a da RSSSF
- data diferente no ogol — Racing de Montevideo x River Plate de Montevideo: RSSSF 2008-08-24, ogol 2008-08-31; fica a da RSSSF
- data diferente no ogol — Cerro Largo x Danubio: RSSSF 2008-08-23, ogol 2008-08-31; fica a da RSSSF
- data diferente no ogol — Defensor Sporting x Cerro: RSSSF 2008-08-23, ogol 2008-08-31; fica a da RSSSF
- data diferente no ogol — Bella Vista x Defensor Sporting: RSSSF 2008-08-31, ogol 2008-09-07; fica a da RSSSF
- data diferente no ogol — Peñarol x Racing de Montevideo: RSSSF 2008-08-30, ogol 2008-09-07; fica a da RSSSF
- data diferente no ogol — Central Español x Cerro Largo: RSSSF 2008-08-30, ogol 2008-09-07; fica a da RSSSF
- data diferente no ogol — River Plate de Montevideo x Rampla Juniors: RSSSF 2008-08-31, ogol 2008-09-07; fica a da RSSSF
- data diferente no ogol — Danubio x Montevideo Wanderers: RSSSF 2008-08-31, ogol 2008-09-07; fica a da RSSSF
- data diferente no ogol — Cerro x Tacuarembó: RSSSF 2008-08-30, ogol 2008-09-07; fica a da RSSSF
- data diferente no ogol — Liverpool de Montevideo x Juventud de Las Piedras: RSSSF 2008-08-31, ogol 2008-09-07; fica a da RSSSF
- placar diferente no ogol — Liverpool de Montevideo x Rampla Juniors (2008-10-05): RSSSF 2-2, ogol 1-1; fica o da RSSSF
- data diferente no ogol — Bella Vista x Cerro Largo: RSSSF 2008-11-09, ogol 2008-11-02; fica a da RSSSF
- data diferente no ogol — River Plate de Montevideo x Juventud de Las Piedras: RSSSF 2008-11-09, ogol 2008-11-02; fica a da RSSSF
- data diferente no ogol — Danubio x Defensor Sporting: RSSSF 2008-11-09, ogol 2008-11-02; fica a da RSSSF
- data diferente no ogol — Cerro x Racing de Montevideo: RSSSF 2008-11-09, ogol 2008-11-02; fica a da RSSSF
- data diferente no ogol — Liverpool de Montevideo x Montevideo Wanderers: RSSSF 2008-11-09, ogol 2008-11-02; fica a da RSSSF
- data diferente no ogol — Nacional x Rampla Juniors: RSSSF 2008-11-08, ogol 2008-11-02; fica a da RSSSF
- data diferente no ogol — Central Español x Tacuarembó: RSSSF 2008-11-08, ogol 2008-11-02; fica a da RSSSF
- data diferente no ogol — Danubio x Nacional: RSSSF 2009-02-08, ogol 2009-02-15; fica a da RSSSF
- abandonado/suspenso, sem valer — Racing de Montevideo Peñarol (2009-03-01): abandoned at 0-0 in 46' due
- decidido fora de campo — Rampla Juniors River Plate de Montevideo (2009-03-01): awarded 0-2; originally 2-1,
- não jogado — Defensor Sporting Nacional (2009-06-14)

### 2009/10

- ogol: 238 jogos casados (edição 9584 do ogol, 243 jogos)
- ESPN: 238 jogos casados

### 2010/11

- ogol: 237 jogos casados (edição 15962 do ogol, 241 jogos)
- ESPN: 236 jogos casados

### 2011/12

- ogol: 237 jogos casados (edição 25175 do ogol, 241 jogos)
- ESPN: 238 jogos casados
- data diferente no ogol — Fénix x Racing de Montevideo: RSSSF 2012-05-24, ogol 2012-05-16; fica a da RSSSF
- W.O./pontos para o mandante — Danubio 1-1 Racing de Montevideo (2011-10-09): awarded 1-1 win to Danubio; Racing used
- abandonado/suspenso, sem valer — Montevideo Wanderers Defensor Sporting (2011-10-15): abandoned at 0-2 in 62'
- abandonado/suspenso, sem valer — Fénix Racing de Montevideo (2012-04-07): abandoned at 1-3 in 72' due to incidents

### 2012/13

- ogol: 235 jogos casados (edição 48833 do ogol, 241 jogos)
- ESPN: 240 jogos casados

### 2013/14

- ogol: 236 jogos casados (edição 60015 do ogol, 243 jogos)
- ESPN: 236 jogos casados
- data diferente no ogol — El Tanque Sisley x Juventud de Las Piedras: RSSSF 2013-08-24, ogol 2013-08-18; fica a da RSSSF
- data diferente no ogol — Rentistas x Nacional: RSSSF 2013-08-24, ogol 2013-08-18; fica a da RSSSF
- data diferente no ogol — Montevideo Wanderers x Liverpool de Montevideo: RSSSF 2013-08-24, ogol 2013-08-18; fica a da RSSSF
- data diferente no ogol — Racing de Montevideo x Miramar Misiones: RSSSF 2013-08-24, ogol 2013-08-18; fica a da RSSSF
- data diferente no ogol — Sud América x Fénix: RSSSF 2013-08-24, ogol 2013-08-18; fica a da RSSSF
- abandonado/suspenso, sem valer — River Plate de Montevideo Cerro (2014-02-15): abandoned at 1-0 in 39' due to
- abandonado/suspenso, sem valer — Juventud de Las Piedras Fénix (2014-03-30): abandoned at 1-1 in 33' due to bad weather
- abandonado/suspenso, sem valer — Rentistas River Plate de Montevideo (2014-03-30): abandoned at 0-0 in 37' due to bad weather

### 2014/15

- ogol: 240 jogos casados (edição 70900 do ogol, 241 jogos)
- ESPN: 240 jogos casados
- data diferente no ogol — Nacional x Peñarol: RSSSF 2015-06-07, ogol 2015-06-14; fica a da RSSSF
- decidido fora de campo — Cerro Peñarol (2015-02-14): awarded 0-3; abandoned at 0-3 in 83' due to crowd

### 2015/16

- ogol: 241 jogos casados (edição 88309 do ogol, 241 jogos)
- ESPN: 241 jogos casados
- data diferente no ogol — Peñarol x Plaza Colonia: RSSSF 2016-06-05, ogol 2016-06-12; fica a da RSSSF

### 2016

- torneio de transição de volta ao calendário anual (turno único)
- ogol: 120 jogos casados (edição 99181 do ogol, 120 jogos)
- ESPN: 120 jogos casados
- decidido fora de campo — Peñarol Nacional (2016-11-27): awarded 0-3; match not started due to crowd trouble

### 2017

- artilheiro pela AUF: Maureen Franco 25; a es dá Cristian Palacios 29 (QU-008)
- ogol: 297 jogos casados (edição 103310 do ogol, 298 jogos)
- ESPN: 299 jogos casados
- data diferente no ogol — Peñarol x Defensor Sporting: RSSSF 2017-12-03, ogol 2017-12-10; fica a da RSSSF
- W.O./pontos para o visitante — Sud América 1-1 Danubio (s/d): awarded 1-1 win to Danubio as suspended coach of
- abandonado/suspenso, sem valer — El Tanque Sisley Liverpool de Montevideo (2017-09-10): abandoned at 0-3 in 65' due to bad weather
- abandonado/suspenso, sem valer — Racing de Montevideo Boston River (2017-09-12): abandoned at 1-1 in 87' due to stone throwing

### 2018

- ogol: 276 jogos casados (edição 122004 do ogol, 291 jogos)
- ESPN: 276 jogos casados
- corrigido — Peñarol x Nacional (2018-11-04): Supercopa 2019 (03/02/2019) entre o campeão e o vencedor da tabela anual: outra competição, não a final do campeonato (UY-013)
- data diferente no ogol — Montevideo City Torque x El Tanque Sisley: RSSSF 2018-03-25, ogol 2018-03-21; fica a da RSSSF
- data diferente no ogol — Nacional x Peñarol: RSSSF 2018-11-04, ogol 2018-11-11; fica a da RSSSF
- W.O./pontos para o mandante — Montevideo Wanderers 0-0 El Tanque Sisley (2018-02-04): awarded 0-0 win to Wanderers
- W.O./pontos para o mandante — Liverpool de Montevideo 0-0 El Tanque Sisley (2018-02-11): awarded 0-0 win to Liverpool
- W.O./pontos para o mandante — Liverpool de Montevideo 2-2 Boston River (2018-02-17): awarded 2-2 win to Liverpool
- W.O./pontos para o mandante — Cerro 0-0 El Tanque Sisley (2018-02-18): awarded 0-0 win to Cerro
- W.O./pontos para o mandante — Boston River 0-0 El Tanque Sisley (2018-02-25): awarded 0-0 win to Boston River
- W.O./pontos para o mandante — Peñarol 0-0 El Tanque Sisley (2018-03-04): awarded 0-0 win to Peñarol
- W.O./pontos para o mandante — Atenas de San Carlos 0-0 El Tanque Sisley (2018-03-11): awarded 0-0 win to Atenas
- W.O./pontos para o mandante — Danubio 0-0 El Tanque Sisley (2018-03-22): awarded 0-0 win to Danubio
- W.O./pontos para o mandante — Montevideo City Torque 0-0 El Tanque Sisley (2018-03-25): awarded 0-0 win to Torque
- W.O./pontos para o mandante — Rampla Juniors 0-0 El Tanque Sisley (2018-03-28): awarded 0-0 win to Rampla Juniors
- W.O./pontos para o mandante — Fénix 0-0 El Tanque Sisley (2018-04-01): awarded 0-0 win to Fénix
- W.O./pontos para o mandante — Nacional 0-0 El Tanque Sisley (2018-04-08): awarded 0-0 win to Nacional
- W.O./pontos para o mandante — Progreso 0-0 El Tanque Sisley (2018-04-15): awarded 0-0 win to Progreso
- W.O./pontos para o mandante — Defensor Sporting 0-0 El Tanque Sisley (2018-04-22): awarded 0-0 win to Defensor Sporting
- W.O./pontos para o mandante — Racing de Montevideo 0-0 El Tanque Sisley (2018-04-30): awarded 0-0 win to Racing
- W.O./pontos para o mandante — River Plate de Montevideo 0-0 El Tanque Sisley (2018-05-06): awarded 0-0 win to River Plate
- W.O./pontos para o mandante — Montevideo Wanderers 0-0 El Tanque Sisley (2018-07-22): awarded 0-0 win to Wanderers
- W.O./pontos para o mandante — Liverpool de Montevideo 0-0 El Tanque Sisley (2018-07-29): awarded 0-0 win to Liverpool
- W.O./pontos para o mandante — Cerro 0-0 El Tanque Sisley (2018-08-05): awarded 0-0 win to Cerro
- W.O./pontos para o mandante — Boston River 0-0 El Tanque Sisley (2018-08-12): awarded 0-0 win to Boston River
- W.O./pontos para o mandante — Peñarol 0-0 El Tanque Sisley (2018-08-19): awarded 0-0 win to Peñarol
- W.O./pontos para o mandante — Atenas de San Carlos 0-0 El Tanque Sisley (2018-08-26): awarded 0-0 win to Atenas
- W.O./pontos para o mandante — Danubio 0-0 El Tanque Sisley (2018-09-02): awarded 0-0 win to Danubio
- W.O./pontos para o mandante — Montevideo City Torque 0-0 El Tanque Sisley (2018-09-09): awarded 0-0 win to Torque
- W.O./pontos para o mandante — Rampla Juniors 0-0 El Tanque Sisley (2018-09-16): awarded 0-0 win to Rampla Juniors
- abandonado/suspenso, sem valer — Liverpool de Montevideo Nacional (2018-09-22): abandoned at 0-1 in 58'
- W.O./pontos para o mandante — Fénix 0-0 El Tanque Sisley (2018-09-23): awarded 0-0 win to Fénix
- W.O./pontos para o mandante — Nacional 0-0 El Tanque Sisley (2018-10-07): awarded 0-0 win to Nacional
- W.O./pontos para o mandante — Progreso 0-0 El Tanque Sisley (2018-10-14): awarded 0-0 win to Progreso
- W.O./pontos para o mandante — Defensor Sporting 0-0 El Tanque Sisley (2018-10-21): awarded 0-0 win to Defensor
- W.O./pontos para o mandante — Racing de Montevideo 0-0 El Tanque Sisley (2018-10-28): awarded 0-0 win to Racing
- W.O./pontos para o mandante — River Plate de Montevideo 0-0 El Tanque Sisley (2018-11-04): awarded 0-0 win to River Plate

### 2019

- ogol: 296 jogos casados (edição 131573 do ogol, 298 jogos)
- ESPN: 296 jogos casados
- corrigido — Nacional x Liverpool de Montevideo (2019-12-05): Supercopa 2020 (01/02/2020) entre o campeão e o vencedor da tabela anual: outra competição, não a final do campeonato (UY-013)
- W.O./pontos para o mandante — Progreso 1-1 Cerro (2019-11-03): awarded 1-1 win to Progreso because Cerro

### 2020

- temporada esticada até abril de 2021 pela pandemia (a RSSSF chama de 2020/21)
- ogol: 299 jogos casados (edição 142292 do ogol, 301 jogos)
- ESPN: 300 jogos casados
- corrigido — Nacional x Montevideo Wanderers (2021-03-29): Supercopa 2021 (02/05/2021) entre o campeão e o vencedor da tabela anual: outra competição, não a final do campeonato (UY-013)
- data diferente no ogol — Nacional x Rentistas: RSSSF 2020-10-11, ogol 2020-10-15; fica a da RSSSF
- data diferente no ogol — Nacional x Rentistas: RSSSF 2021-03-29, ogol 2021-04-05; fica a da RSSSF
- data diferente no ogol — Rentistas x Nacional: RSSSF 2021-03-29, ogol 2021-04-07; fica a da RSSSF
- abandonado/suspenso, sem valer — Rentistas River Plate de Montevideo (2020-08-26): abandoned at 0-0 in 20' due to bad weather
- W.O./pontos para o visitante — Fénix 1-1 River Plate de Montevideo (2021-01-17): awarded 1-1 win to River Plate; Fénix fielded
- W.O./pontos para o mandante — Montevideo Wanderers 1-3 Progreso (2021-03-21): awarded 1-3 win to Wanderers; Progreso fielded

### 2021

- ogol: 241 jogos casados (edição 155076 do ogol, 241 jogos)
- ESPN: 241 jogos casados
- corrigido — Peñarol x Plaza Colonia (2021-12-05): Supercopa 2022 (30/01/2022) entre o campeão e o vencedor da tabela anual: outra competição, não a final do campeonato (UY-013)
- W.O./pontos para o visitante — Cerro Largo 1-1 Nacional (2021-09-11): originally 1-1, but awarded a win to Nacional

### 2022

- ogol: 298 jogos casados (edição 161992 do ogol, 298 jogos)
- ESPN: 298 jogos casados
- corrigido — Nacional x Liverpool de Montevideo (2022-10-24): Supercopa 2023 (29/01/2023) entre o campeão e o vencedor da tabela anual: outra competição, não a final do campeonato (UY-013)
- data diferente no ogol — Liverpool de Montevideo x Nacional: RSSSF 2022-10-24, ogol 2022-10-30; fica a da RSSSF
- abandonado/suspenso, sem valer — Nacional Liverpool de Montevideo (2022-02-20): abandoned at 0-0 in 32' due to unplayable pitch
- W.O./pontos para o visitante — Cerrito 2-1 Rentistas (2022-03-11): win awarded to Rentistas; goal records unchanged
- abandonado/suspenso, sem valer — Peñarol Rentistas (2022-07-20): abandoned at 0-0 at half-time due
- W.O./pontos para o mandante — Boston River 2-1 Peñarol (2022-10-12): win awarded to Boston River; abandoned at 2-1 in

### 2023

- artilheiro pela AUF: Juan Ignacio Ramírez 18; a es dá 19 (QU-008)
- ogol: 298 jogos casados (edição 171854 do ogol, 300 jogos)
- ESPN: 298 jogos casados
- corrigido — Liverpool de Montevideo x Defensor Sporting (2023-12-08): Supercopa 2024 (31/01/2024) entre o campeão e o vencedor da tabela anual: outra competição, não a final do campeonato (UY-013)
- data diferente no ogol — Defensor Sporting x Liverpool de Montevideo: RSSSF 2023-07-24, ogol 2023-07-30; fica a da RSSSF
- placar diferente no ogol — Liverpool de Montevideo x Peñarol (2023-12-08): RSSSF 2-0, ogol 0-1; fica o da RSSSF
- W.O./pontos para o visitante — La Luz 1-1 Montevideo City Torque (2023-02-27): awarded win to Torque as La Luz fielded
- abandonado/suspenso, sem valer — Racing de Montevideo Plaza Colonia (2023-04-30): abandoned at 1-0 in 31'

### 2024

- ogol: 296 jogos casados (edição 183556 do ogol, 297 jogos)
- ESPN: 296 jogos casados
- corrigido — Peñarol x Nacional (2024-12-02): Supercopa 2025 (26/01/2025) entre o campeão e o vencedor da tabela anual: outra competição, não a final do campeonato (UY-013)

### 2025

- ogol: 297 jogos casados (edição 194917 do ogol, 300 jogos)
- ESPN: 299 jogos casados
- corrigido — Nacional x Peñarol (2025-11-16): Supercopa 2026 entre o campeão e o vencedor da tabela anual: outra competição, não a final do campeonato (UY-013)
- data diferente no ogol — Peñarol x Nacional: RSSSF 2025-11-16, ogol 2025-11-23; fica a da RSSSF

