# Campeonato Mexicano (1ª divisão) — coleta de dados

Gerado por `python coleta/mex-1/importar.py`. Pacote em `data/coleta/mex-1/pacote/`.

**Edições:** 158, uma por título, de 1902/03 ao Clausura 2026, como na lista de campeões da RSSSF (`mexchamp.html`) e na da Wikipédia em inglês (1943/44 em diante). Escopo decidido pelo Guilherme em 23/11/2026: a era amadora entra (Primera Fuerza e Liga Mayor do Distrito Federal, 1902/03-1942/43); em 1920/21 e 1921/22, uma edição por liga (Liga Mexicana, a oficial, e Liga Nacional, a do RC España), sem o Torneo del Centenario de 1921; México 70, Prode 85 e México 86 são edições próprias. De 1943/44 a 1995/96, uma edição por temporada (a liguilla e as finais são fases); Invierno e Verano (1996-2002) e Apertura e Clausura (2002 em diante), uma edição cada. A temporada 1930/31 (cancelada no começo e declarada deserta) e o Clausura 2020 (pandemia) entram sem campeão, com a tabela do momento.

**Fora do pacote:** a 2ª e a 3ª divisões, a Copa México e a Copa MX, o Campeón de Campeones, a Interliga, a Liguilla Pre-Libertadores, os playoffs de vaga na Libertadores, o Torneo Presidente López Mateos (1963), a Copa Federación (1983), os jogos de promoção e as copas e amistosos das páginas da era amadora (Copa Tower, Copa Eliminatoria, jogo anual Inglaterra x Escócia).

**Edições sem jogos (2):** 1911/12 e 1916/17: a RSSSF não tem página dessas temporadas; entram com a tabela final de `mexhist.html`.

**Edições com jogos incompletos (6):** 1915/16 e 1924/25 (a página traz só parte dos jogos), 1920/21 e 1921/22 ("known results"; a Liga Nacional de 1921/22 não terminou). Nelas a classificação é a tabela publicada, sem conferência; o que falta está na observação da edição.

**Fontes:** RSSSF (uma página por temporada em `data/coleta/mex-1/rsssf/`: base de jogos, com fases, rodadas, datas, estádios e autores dos gols; tabelas finais `mexhist.html`; lista de campeões `mexchamp.html`; artilheiros `mextops.html`); ESPN (liga `mex.1`, Apertura 2002 em diante: hora, estádio, público, gols com minuto e cartões; a fase regular do Apertura 2025 e do Clausura 2026); Wikipédia em inglês (lista de campeões: segunda fonte do campeão e do vice, 1943/44 em diante).

**Clubes:** nome pelo qual o clube é conhecido (Guadalajara, Cruz Azul, Pumas, Tigres, Tecos, Leones Negros). O mesmo clube com outro nome: Centro Unión (1918-1920) é o América; Atlético Español (1971-1982) é o Necaxa; Atlético Morelia é o Morelia; U.N.A.M. é o Pumas; U.A.N.L. é o Tigres; U.A.G. e Estudiantes Tecos são o Tecos; U. de G. é o Leones Negros; U.A.T. é o Correcaminos; Club México e México FC são o mesmo; o Pachuca AC da era amadora é o Pachuca (o clube conta a história desde 1892, com a refundação de 1960). Clubes diferentes com nome parecido ficam separados (lista no começo de `coleta/mex-1/clubes_mex.py`). Homônimos de clubes de outros países levam a cidade ou o país: América do México, Santos Laguna, Real Club España, Deportivo Español de México, Sporting de México, Nacional de Guadalajara, Laguna de Torreón.

**Regras:** o placar é o da RSSSF (ESPN onde a RSSSF não tem). Jogo decidido fora de campo leva o placar dado (`awd`), com o de campo na observação; "awarded to X" sem placar vira W.O. (vitória sem gols, como a tabela conta); resultado desconhecido ("unk") fica de fora. Pontos: 2 por vitória até 1994/95 e 3 a partir de 1995/96. Os grupos da fase regular (1970-2011) são só de classificação (todos jogam contra todos): os jogos não levam grupo; México 70, Prode 85 e México 86, em que só se jogava dentro do grupo, levam.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1902/03 | 5 | 10 (10) | 26 | 11 | 1 / 0 | Orizaba AC | RSSSF (mex1903) |
| 1903/04 | 5 | 16 (16) | 33 | 33 | 1 / 0 | Mexico Cricket Club | RSSSF (mex1904) |
| 1904/05 | 5 | 19 (20) | 45 | 0 | 0 / 1 | Pachuca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1905/06 | 5 | 20 (20) | 44 | 0 | 0 / 1 | Reforma AC | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1906/07 | 5 | 20 (20) | 42 | 0 | 1 / 0 | Reforma AC | RSSSF (mex1907) |
| 1907/08 | 4 | 12 (12) | 17 | 0 | 1 / 0 | British Club | RSSSF (mex1908) |
| 1908/09 | 3 | 6 (6) | 15 | 2 | 3 / 0 | Reforma AC | RSSSF (mexhist) |
| 1909/10 | 4 | 12 (12) | 46 | 24 | 1 / 0 | Reforma AC | RSSSF (mex1910) |
| 1910/11 | 4 | 11 (11) | 35 | 7 | 2 / 0 | Reforma AC | RSSSF (mex1911) |
| 1911/12 | 3 | 0 (0) | 0 | 0 | 0 / 0 | Reforma AC | RSSSF (mexhist) |
| 1912/13 | 5 | 20 (20) | 55 | 36 | 2 / 0 | Club México | RSSSF (mex1913) |
| 1913/14 | 6 | 30 (30) | 65 | 59 | 0 / 2 | Real Club España | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1914/15 | 4 | 12 (12) | 23 | 18 | 1 / 0 | Real Club España | RSSSF (mex1915) |
| 1915/16 | 6 | 22 (22) | 54 | 11 | 0 / 0 | Real Club España | RSSSF (mexhist) |
| 1916/17 | 6 | 0 (0) | 0 | 0 | 0 / 0 | Real Club España | RSSSF (mexhist) |
| 1917/18 | 7 | 33 (33) | 43 | 23 | 1 / 0 | Pachuca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1918/19 | 8 | 40 (40) | 84 | 22 | 0 / 1 | Real Club España | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1919/20 | 8 | 22 (22) | 46 | 2 | 1 / 0 | Pachuca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1920/21 Liga Mexicana | 5 | 19 (19) | 24 | 6 | 0 / 0 | Asturias | RSSSF (mexhist) |
| 1920/21 Liga Nacional | 5 | 18 (18) | 27 | 14 | 0 / 0 | Real Club España | RSSSF (mexhist) |
| 1921/22 Liga Mexicana | 4 | 15 (15) | 13 | 5 | 0 / 0 | Germania FV | RSSSF (mexhist) |
| 1921/22 Liga Nacional | 3 | 2 (2) | 4 | 0 | 0 / 0 | Real Club España | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1922/23 | 8 | 56 (56) | 135 | 60 | 1 / 0 | Asturias | RSSSF (mex23) |
| 1923/24 | 9 | 73 (73) | 155 | 60 | 1 / 0 | Real Club España | RSSSF (mex24) |
| 1924/25 | 7 | 37 (37) | 93 | 25 | 0 / 0 | América do México | RSSSF (mex25) |
| 1925/26 | 7 | 47 (46) | 157 | 19 | 0 / 1 | América do México | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1926/27 | 7 | 42 (42) | 151 | 46 | 2 / 0 | América do México | RSSSF (mex27) |
| 1927/28 | 8 | 55 (56) | 224 | 0 | 0 / 1 | América do México | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1928/29 | 9 | 37 (36) | 211 | 83 | 1 / 0 | Marte | RSSSF (mex29) |
| 1929/30 | 8 | 57 (56) | 226 | 79 | 1 / 0 | Real Club España | RSSSF (mex30) |
| 1930/31 | 8 | 8 (8) | 36 | 7 | 1 / 0 | None | RSSSF (mexhist) |
| 1931/32 | 8 | 59 (59) | 321 | 3 | 2 / 0 | Atlante | RSSSF (mex32) |
| 1932/33 | 10 | 42 (42) | 227 | 31 | 3 / 0 | Necaxa | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1933/34 | 6 | 32 (33) | 175 | 75 | 2 / 2 | Real Club España | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1934/35 | 6 | 45 (45) | 250 | 6 | 2 / 0 | Necaxa | RSSSF (mexhist) |
| 1935/36 | 5 | 20 (20) | 89 | 60 | 2 / 0 | Real Club España | RSSSF (mexhist) |
| 1936/37 | 5 | 20 (20) | 86 | 52 | 0 / 2 | Necaxa | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1937/38 | 6 | 30 (30) | 147 | 136 | 2 / 0 | Necaxa | RSSSF (mex38) |
| 1938/39 | 7 | 42 (42) | 226 | 211 | 1 / 0 | Asturias | RSSSF (mex39) |
| 1939/40 | 6 | 44 (44) | 199 | 161 | 1 / 0 | Real Club España | RSSSF (mex40) |
| 1940/41 | 8 | 56 (56) | 248 | 178 | 0 / 1 | Atlante | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1941/42 | 8 | 57 (57) | 293 | 262 | 2 / 0 | Real Club España | RSSSF (mexhist) |
| 1942/43 | 8 | 56 (56) | 278 | 221 | 1 / 0 | Marte | RSSSF (mex43) |
| 1943/44 | 10 | 91 (91) | 454 | 423 | 2 / 0 | Asturias | RSSSF (mex44) |
| 1944/45 | 13 | 156 (156) | 713 | 700 | 2 / 0 | Real Club España | RSSSF (mex45) |
| 1945/46 | 16 | 240 (240) | 1182 | 1160 | 1 / 1 | Veracruz | RSSSF (mex46) |
| 1946/47 | 15 | 210 (210) | 905 | 875 | 1 / 0 | Atlante | RSSSF (mex47) |
| 1947/48 | 15 | 212 (212) | 922 | 877 | 1 / 0 | León | RSSSF (mex48) |
| 1948/49 | 15 | 210 (210) | 809 | 782 | 1 / 0 | León | RSSSF (mex49) |
| 1949/50 | 14 | 182 (182) | 734 | 726 | 1 / 0 | Veracruz | RSSSF (mex50) |
| 1950/51 | 12 | 132 (132) | 450 | 448 | 2 / 0 | Atlas | RSSSF (mexhist) |
| 1951/52 | 12 | 132 (132) | 450 | 406 | 2 / 0 | León | RSSSF (mexhist) |
| 1952/53 | 12 | 132 (132) | 397 | 377 | 1 / 0 | Tampico | RSSSF (mex53) |
| 1953/54 | 12 | 132 (132) | 461 | 442 | 1 / 0 | Marte | RSSSF (mex54) |
| 1954/55 | 12 | 132 (132) | 382 | 375 | 3 / 0 | Zacatepec | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1955/56 | 14 | 183 (183) | 574 | 572 | 1 / 1 | León | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1956/57 | 13 | 156 (156) | 451 | 439 | 1 / 1 | Guadalajara | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1957/58 | 14 | 182 (182) | 571 | 549 | 2 / 0 | Zacatepec | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1958/59 | 14 | 182 (182) | 584 | 562 | 1 / 0 | Guadalajara | RSSSF (mex59) |
| 1959/60 | 14 | 182 (182) | 586 | 570 | 1 / 0 | Guadalajara | RSSSF (mex60) |
| 1960/61 | 14 | 182 (182) | 511 | 496 | 0 / 1 | Guadalajara | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1961/62 | 14 | 182 (182) | 568 | 524 | 1 / 0 | Guadalajara | RSSSF (mex62) |
| 1962/63 | 14 | 182 (182) | 533 | 513 | 1 / 0 | Oro | RSSSF (mex63) |
| 1963/64 | 17 | 189 (189) | 548 | 542 | 2 / 0 | Guadalajara | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1964/65 | 16 | 240 (240) | 611 | 583 | 2 / 0 | Guadalajara | RSSSF (mex65) |
| 1965/66 | 16 | 240 (240) | 681 | 662 | 0 / 1 | América do México | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1966/67 | 16 | 240 (240) | 633 | 621 | 2 / 0 | Toluca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1967/68 | 16 | 240 (240) | 635 | 620 | 1 / 0 | Toluca | RSSSF (mex68) |
| 1968/69 | 16 | 243 (243) | 662 | 639 | 1 / 0 | Cruz Azul | RSSSF (mex69) |
| 1969/70 | 16 | 241 (241) | 638 | 630 | 0 / 1 | Guadalajara | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1970 México 70 | 16 | 224 (224) | 550 | 531 | 6 / 0 | Cruz Azul | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1970/71 | 18 | 311 (311) | 717 | 10 | 2 / 0 | América do México | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1971/72 | 18 | 317 (317) | 825 | 814 | 2 / 0 | Cruz Azul | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1972/73 | 18 | 321 (321) | 838 | 831 | 2 / 0 | Cruz Azul | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1973/74 | 18 | 314 (314) | 941 | 920 | 1 / 1 | Cruz Azul | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1974/75 | 20 | 392 (392) | 1125 | 1120 | 3 / 0 | Toluca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1975/76 | 20 | 396 (396) | 1027 | 1012 | 2 / 2 | América do México | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1976/77 | 20 | 408 (408) | 1045 | 1024 | 6 / 0 | Pumas | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1977/78 | 20 | 396 (396) | 1110 | 1104 | 4 / 0 | Tigres | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1978/79 | 20 | 406 (406) | 1147 | 1141 | 6 / 1 | Cruz Azul | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1979/80 | 20 | 408 (408) | 1113 | 1102 | 6 / 0 | Cruz Azul | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1980/81 | 20 | 408 (408) | 1065 | 1052 | 6 / 0 | Pumas | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1981/82 | 20 | 397 (397) | 1029 | 1025 | 4 / 0 | Tigres | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1982/83 | 20 | 397 (397) | 1038 | 1023 | 4 / 0 | Puebla | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1983/84 | 20 | 394 (394) | 1102 | 1049 | 4 / 0 | América do México | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1984/85 | 20 | 397 (397) | 1030 | 1026 | 4 / 0 | América do México | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1985 Prode 85 | 20 | 93 (93) | 266 | 263 | 0 / 0 | América do México | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1986 México 86 | 20 | 194 (194) | 515 | 512 | 4 / 0 | Monterrey | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1986/87 | 21 | 434 (434) | 1026 | 991 | 2 / 2 | Guadalajara | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1987/88 | 20 | 394 (394) | 1176 | 1152 | 4 / 0 | América do México | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1988/89 | 20 | 406 (406) | 1133 | 1115 | 5 / 1 | América do México | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1989/90 | 20 | 394 (394) | 967 | 935 | 3 / 1 | Puebla | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1990/91 | 20 | 394 (394) | 1005 | 987 | 2 / 2 | Pumas | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1991/92 | 20 | 398 (398) | 984 | 961 | 4 / 0 | León | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1992/93 | 20 | 398 (398) | 1062 | 1053 | 2 / 2 | Atlante | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1993/94 | 20 | 398 (398) | 1081 | 1075 | 2 / 2 | Tecos | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1994/95 | 19 | 360 (360) | 1048 | 1039 | 4 / 0 | Necaxa | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1995/96 | 18 | 323 (324) | 863 | 827 | 2 / 3 | Necaxa | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1996 Invierno | 18 | 171 (171) | 498 | 492 | 3 / 1 | Santos Laguna | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1997 Verano | 18 | 169 (169) | 493 | 481 | 4 / 0 | Guadalajara | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1997 Invierno | 18 | 167 (167) | 471 | 469 | 4 / 0 | Cruz Azul | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1998 Verano | 18 | 171 (171) | 487 | 487 | 4 / 0 | Toluca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1998 Invierno | 18 | 167 (167) | 540 | 538 | 4 / 0 | Necaxa | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1999 Verano | 18 | 169 (169) | 551 | 540 | 5 / 0 | Toluca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1999 Invierno | 18 | 169 (169) | 520 | 509 | 4 / 0 | Pachuca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2000 Verano | 18 | 170 (170) | 541 | 530 | 3 / 1 | Toluca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2000 Invierno | 18 | 169 (169) | 532 | 532 | 3 / 1 | Morelia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2001 Verano | 18 | 171 (171) | 500 | 475 | 3 / 1 | Santos Laguna | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2001 Invierno | 19 | 185 (185) | 518 | 516 | 4 / 0 | Pachuca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2002 Verano | 19 | 189 (189) | 568 | 568 | 5 / 0 | América do México | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2002 Apertura | 20 | 204 (204) | 643 | 637 | 6 / 2 | Toluca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2003 Clausura | 20 | 206 (206) | 564 | 564 | 8 / 0 | Monterrey | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2003 Apertura | 20 | 208 (208) | 625 | 625 | 7 / 1 | Pachuca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2004 Clausura | 20 | 206 (206) | 635 | 635 | 6 / 2 | Pumas | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2004 Apertura | 18 | 167 (167) | 535 | 533 | 6 / 0 | Pumas | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2005 Clausura | 18 | 167 (167) | 493 | 493 | 5 / 1 | América do México | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2005 Apertura | 18 | 167 (167) | 516 | 516 | 6 / 0 | Toluca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2006 Clausura | 18 | 167 (167) | 418 | 418 | 6 / 0 | Pachuca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2006 Apertura | 18 | 171 (171) | 443 | 443 | 6 / 0 | Guadalajara | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2007 Clausura | 18 | 171 (171) | 418 | 418 | 6 / 0 | Pachuca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2007 Apertura | 18 | 171 (171) | 493 | 493 | 7 / 0 | Atlante | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2008 Clausura | 18 | 171 (171) | 457 | 457 | 6 / 0 | Santos Laguna | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2008 Apertura | 18 | 167 (167) | 431 | 431 | 6 / 0 | Toluca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2009 Clausura | 18 | 167 (167) | 459 | 459 | 6 / 0 | Pumas | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2009 Apertura | 18 | 167 (167) | 446 | 446 | 6 / 0 | Monterrey | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2010 Clausura | 18 | 167 (167) | 456 | 456 | 7 / 0 | Toluca | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2010 Apertura | 18 | 167 (167) | 425 | 425 | 6 / 0 | Monterrey | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2011 Clausura | 18 | 167 (167) | 435 | 435 | 6 / 0 | Pumas | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2011 Apertura | 18 | 167 (167) | 464 | 464 | 3 / 0 | Tigres | RSSSF (mex2012) |
| 2012 Clausura | 18 | 167 (167) | 416 | 416 | 2 / 0 | Santos Laguna | RSSSF (mex2012) |
| 2012 Apertura | 18 | 167 (167) | 415 | 415 | 2 / 0 | Tijuana | RSSSF (mex2013) |
| 2013 Clausura | 18 | 167 (167) | 410 | 410 | 2 / 0 | América do México | RSSSF (mex2013) |
| 2013 Apertura | 18 | 167 (167) | 440 | 440 | 2 / 0 | León | RSSSF (mex2014) |
| 2014 Clausura | 18 | 167 (167) | 423 | 423 | 2 / 0 | León | RSSSF (mex2014) |
| 2014 Apertura | 18 | 167 (167) | 384 | 384 | 2 / 0 | América do México | RSSSF (mex2015) |
| 2015 Clausura | 18 | 167 (167) | 437 | 437 | 2 / 0 | Santos Laguna | RSSSF (mex2015) |
| 2015 Apertura | 18 | 167 (167) | 497 | 497 | 2 / 0 | Tigres | RSSSF (mex2016) |
| 2016 Clausura | 18 | 167 (167) | 470 | 470 | 2 / 0 | Pachuca | RSSSF (mex2016) |
| 2016 Apertura | 18 | 167 (167) | 466 | 466 | 2 / 0 | Tigres | RSSSF (mex2017) |
| 2017 Clausura | 18 | 167 (167) | 411 | 411 | 2 / 0 | Guadalajara | RSSSF (mex2017) |
| 2017 Apertura | 18 | 167 (167) | 420 | 420 | 3 / 0 | Tigres | RSSSF (mex2018) |
| 2018 Clausura | 18 | 167 (167) | 434 | 434 | 2 / 0 | Santos Laguna | RSSSF (mex2018) |
| 2018 Apertura | 18 | 167 (167) | 446 | 446 | 2 / 0 | América do México | RSSSF (mex2019) |
| 2019 Clausura | 18 | 167 (167) | 449 | 449 | 2 / 0 | Tigres | RSSSF (mex2019) |
| 2019 Apertura | 19 | 185 (185) | 544 | 544 | 2 / 0 | Monterrey | RSSSF (mex2020) |
| 2020 Clausura | 18 | 90 (90) | 260 | 260 | 1 / 0 | None | RSSSF (mexhist) |
| 2020 Apertura | 18 | 171 (171) | 431 | 431 | 2 / 0 | León | RSSSF (mex2021) |
| 2021 Clausura | 18 | 171 (171) | 410 | 407 | 2 / 0 | Cruz Azul | RSSSF (mex2021) |
| 2021 Apertura | 18 | 171 (171) | 375 | 375 | 2 / 0 | Atlas | RSSSF (mex2022) |
| 2022 Clausura | 18 | 171 (171) | 440 | 435 | 2 / 0 | Atlas | RSSSF (mex2022) |
| 2022 Apertura | 18 | 171 (171) | 481 | 481 | 2 / 0 | Pachuca | RSSSF (mex2023) |
| 2023 Clausura | 18 | 171 (171) | 479 | 479 | 2 / 0 | Tigres | RSSSF (mex2023) |
| 2023 Apertura | 18 | 170 (170) | 484 | 484 | 2 / 0 | América do México | RSSSF (mex2024) |
| 2024 Clausura | 18 | 170 (170) | 486 | 486 | 2 / 0 | América do México | RSSSF (mex2024) |
| 2024 Apertura | 18 | 170 (170) | 456 | 456 | 2 / 0 | América do México | RSSSF (mex2025) |
| 2025 Clausura | 18 | 170 (170) | 477 | 477 | 2 / 0 | Toluca | RSSSF (mex2025) |
| 2025 Apertura | 18 | 170 (170) | 521 | 501 | 1 / 0 | Toluca | RSSSF (mex2026) |
| 2026 Clausura | 18 | 167 (167) | 458 | 458 | 1 / 0 | Cruz Azul | RSSSF (mex2026) |

## Conferência e correções, edição a edição

### 1902/03

- linha lida como jogo e descartada (clube não reconhecido): mex1903:160 «England XI x Scotland XI»
- W.O./pontos para o mandante — Orizaba AC Mexico Cricket Club (1903-02-01): Mexico CC dns; awarded match to Orizaba

### 1903/04

- linha lida como jogo e descartada (clube não reconhecido): mex1904:169 «England XI x Scotland XI»

### 1904/05

- tabela publicada x jogos — mex1905:113: Pachuca tabela [8, 5, 2, 1, 9, 3] jogos [7, 5, 1, 1, 9, 3] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — mex1905:113: San Pedro Golf Club tabela [8, 2, 2, 4, 8, 13] jogos [7, 2, 1, 4, 8, 13] — faltam 1 jogo(s) do clube na página
- W.O./pontos para o visitante — Puebla AC San Pedro Golf Club (1904-11-13): postponed and then awarded to San Pedro
- W.O./pontos para o mandante — British Club Puebla AC (1904-11-27): postponed and then awarded to British
- W.O./pontos para o mandante — Reforma AC Puebla AC (1905-01-01): match awarded to Reforma

### 1905/06

- tabela publicada x jogos — mex1906:119: Mexico Country Club tabela [8, 4, 2, 2, 7, 3] jogos [8, 5, 1, 2, 8, 3] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mex1906:119: Pachuca tabela [8, 3, 4, 1, 6, 4] jogos [8, 3, 3, 2, 6, 5] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- linha lida como jogo e descartada (clube não reconhecido): mex1906:130 «England XI x Scotland XI»
- W.O./pontos para o mandante — Mexico Country Club Puebla AC (1905-11-19): Puebla dns; awarded match to México CC
- W.O./pontos para o mandante — Pachuca Puebla AC (1905-12-26): Puebla dns; awarded match to Pachuca

### 1906/07

- linha lida como jogo e descartada (clube não reconhecido): mex1907:130 «England XI x Scotland XI»
- W.O./pontos para o mandante — Mexico Country Club Pachuca (1906-12-08): Pachuca dns; awarded match to Mexico CC
- W.O./pontos para o mandante — British Club Pachuca (1907-02-02): Pachuca dns; awarded match to British Club

### 1907/08

- sem ocorrências

### 1908/09

- sem ocorrências

### 1909/10

- W.O./pontos para o visitante — British Club Popo FC (1910-02-02): British Club dns; awarded match to Popo FC

### 1910/11

- linha lida como jogo e descartada (clube não reconhecido): mex1911:97 «Scotland XI x England XI»

### 1911/12

- sem jogos: a RSSSF não tem página desta temporada (só a tabela final de mexhist.html)

### 1912/13

- sem ocorrências

### 1913/14

- tabela publicada x jogos — mex1914:173: Club México tabela [10, 4, 1, 5, 12, 12] jogos [8, 3, 1, 4, 11, 11] — a diferença vem de Pachuca x Club México (1913-12-07), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — mex1914:173: Pachuca tabela [10, 3, 2, 5, 6, 10] jogos [9, 3, 2, 4, 5, 9] — a diferença vem de Pachuca x Club México (1913-12-07), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — mex1914:173: L'Amicale Française tabela [10, 1, 4, 5, 9, 16] jogos [9, 0, 4, 5, 9, 16] — a diferença vem de Pachuca x L'Amicale Française (1914-01-11), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — mexhist:174: Club México tabela [10, 4, 1, 5, 12, 12] jogos [8, 3, 1, 4, 11, 11] — a diferença vem de Pachuca x Club México (1913-12-07), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — mexhist:174: Pachuca tabela [10, 3, 2, 5, 6, 10] jogos [9, 3, 2, 4, 5, 9] — a diferença vem de Pachuca x Club México (1913-12-07), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — mexhist:174: L'Amicale Française tabela [10, 1, 4, 5, 9, 16] jogos [9, 0, 4, 5, 9, 16] — a diferença vem de Pachuca x L'Amicale Française (1914-01-11), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- decidido fora de campo — Pachuca Club México (1913-12-07): abandoned in 2T
- W.O./pontos para o mandante — Pachuca Rovers FC (1913-12-21): awarded match to Pachuca; Rovers dns FC
- W.O./pontos para o mandante — Real Club España Pachuca (1913-12-28): awarded match to España; Pachuca dns
- W.O./pontos para o mandante — Pachuca L'Amicale Française (1914-01-11): awarded match to Pachuca; L’Amicale Française dns
- decidido fora de campo — L'Amicale Française Club México (1914-01-18)

### 1914/15

- sem ocorrências

### 1915/16

- sem ocorrências

### 1916/17

- sem jogos: a RSSSF não tem página desta temporada (só a tabela final de mexhist.html)

### 1917/18

- linha lida como jogo e descartada (clube não reconhecido): mex1918:110 «On January x España withdrew in protest by refereeing decisions in the match against América on January»
- anulado — Club México 1-1 Real Club España (1917-10-14): annulled
- anulado — Pachuca 3-2 Germania FV (1917-10-21): annulled
- anulado — Real Club España 2-0 Pachuca (1917-11-04): annulled
- anulado — Club México 0-3 Germania FV (1917-11-11): annulled
- anulado — Germania FV 1-0 Real Club España (1917-11-25): annulled
- W.O./pontos para o visitante — Junior Club Deportivo Español de México (1917-12-09): Junior had won 1-0; awarded match to Deportivo Español; undue alignment of Junior
- anulado — Pachuca 0-0 Real Club España (1917-12-16): annulled
- anulado — Germania FV 0-2 Club México (1917-12-23): annulled
- anulado — Junior Club 1-0 Germania FV (1917-12-30): annulled
- anulado — Club México 2-0 Real Club España (1918-01-01): annulled
- anulado — América do México 0-0 Real Club España (1918-01-13): annulled
- anulado — Real Club España 1-0 Deportivo Español de México (1918-01-20): annulled
- anulado — Germania FV 0-0 Deportivo Español de México (1918-02-03): annulled
- anulado — Deportivo Español de México 0-2 Real Club España (1918-02-10): annulled
- decidido fora de campo — Pachuca Junior Club (1918-02-10): Junior Club dns; match awarded to Pachuca AC 1-0

### 1918/19

- tabela publicada x jogos — mex1919:217: Tigres (1918) tabela [12, 5, 5, 2, 9, 7] jogos [8, 3, 3, 2, 5, 6] — faltam 4 jogo(s) do clube na página
- tabela publicada x jogos — mex1919:217: Germania FV tabela [12, 3, 3, 6, 9, 19] jogos [9, 2, 2, 5, 7, 18] — faltam 3 jogo(s) do clube na página
- tabela publicada x jogos — mex1919:217: Pachuca tabela [12, 4, 1, 7, 5, 14] jogos [8, 2, 1, 5, 4, 12] — faltam 4 jogo(s) do clube na página
- tabela publicada x jogos — mex1919:217: Deportivo Español de México tabela [10, 1, 2, 7, 4, 24] jogos [7, 1, 1, 5, 4, 21] — faltam 3 jogo(s) do clube na página
- anulado — Pachuca 3-1 Club México (1918-10-13): annulled
- anulado — Club México 0-1 América do México (1918-11-03): annulled
- anulado — América do México 0-0 Club México (1918-11-10): annulled
- anulado — Real Club España 2-0 Club México (1918-12-01): suspended due to fight and pitch invasion; after annulled
- anulado — Club México 0-0 Deportivo Español de México (1918-12-22): annulled
- anulado — España de Veracruz 1-0 Deportivo Español de México (1919-04-06): apparently annulled, because in the final table published by the league this match did not appear as played
- anulado — Deportivo Español de México 0-0 España de Veracruz (1919-04-13): apparently annulled, by the same reason that the match listed above

### 1919/20

- anulado — Germania FV 2-0 Tigres (1918) (1919-11-23): annulled
- decidido fora de campo — América do México Tigres (1918) (1919-12-21): Tigres dns; awarded match to Centro Unión 1-0; afterwards annulled
- decidido fora de campo — Deportivo Español de México Tigres (1918) (1920-01-04): Tigres dns; awarded match to Deportivo Español 1-0; afterwards annulled
- decidido fora de campo — Club México Tigres (1918) (1920-01-18): Tigres dns, awarded match to Club México 1-0; afterwards annulled

### 1920/21 Liga Mexicana

- liga oficial; o RC España jogou a Liga Nacional, paralela (alguns historiadores dão a temporada como anulada)
- W.O./pontos para o mandante — Asturias Deportivo Internacional (1920-12-26)
- W.O./pontos para o mandante — Germania FV Morelos (1921-01-23)
- W.O./pontos para o visitante — Club México Asturias (1921-01-30)
- W.O./pontos para o visitante — Germania FV Asturias (1921-02-06)
- W.O./pontos para o visitante — Morelos Deportivo Internacional (1921-02-20)
- W.O./pontos para o mandante — Morelos Germania FV (1921-03-06)
- W.O./pontos para o visitante — Morelos Club México (1921-04-03)
- W.O./pontos para o visitante — Asturias Deportivo Internacional (1921-04-10)

### 1920/21 Liga Nacional

- liga paralela, do RC España, que a lista de campeões da RSSSF conta como título (alguns historiadores dão a temporada como anulada)
- W.O./pontos para o mandante — Luz y Fuerza Reforma AC (1920-12-19)
- W.O./pontos para o visitante — Luz y Fuerza L'Amicale Française (1921-02-13)

### 1921/22 Liga Mexicana

- liga oficial; o RC España jogou a Liga Nacional, paralela (alguns historiadores dão a temporada como anulada)
- W.O./pontos para o mandante — Asturias Tranvías (1921-12-04)
- W.O./pontos para o visitante — Asturias Germania FV (1921-12-11)
- W.O./pontos para o mandante — Tranvías Club México (1921-12-18)
- W.O./pontos para o visitante — Tranvías Germania FV (1922-01-08)
- W.O./pontos para o mandante — Club México Germania FV (1922-01-22)
- W.O./pontos para o visitante — Tranvías Asturias (1922-01-29)
- W.O./pontos para o mandante — Germania FV Tranvías (1922-02-19)
- W.O./pontos para o mandante — Asturias Club México (1922-02-26)
- W.O./pontos para o mandante — Asturias Tranvías (1922-03-26)

### 1921/22 Liga Nacional

- liga paralela, do RC España, que a lista de campeões da RSSSF conta como título (alguns historiadores dão a temporada como anulada)
- W.O./pontos para o mandante — Real Club España América do México (1922-03-26)

### 1922/23

- decidido fora de campo — Guerra y Marina América do México (1923-05-06): rescheduled match Round 24; Guerra y Marina dns, awarded match to América 0-1

### 1923/24

- sem ocorrências

### 1924/25

- decidido fora de campo — Germania FV Real Club España (1925-03-08): awarded match to Germania FV 1-0

### 1925/26

- tabela publicada x jogos — mex26:178: América do México tabela [12, 8, 4, 0, 32, 9] jogos [13, 9, 4, 0, 34, 10] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — mex26:178: Asturias tabela [12, 9, 2, 1, 22, 8] jogos [13, 9, 2, 2, 23, 10] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — mex26:178: Necaxa tabela [12, 5, 2, 5, 23, 16] jogos [12, 5, 2, 5, 24, 16] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mex26:178: Germania FV tabela [12, 4, 1, 7, 16, 23] jogos [12, 4, 1, 7, 16, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1926/27

- sem ocorrências

### 1927/28

- tabela publicada x jogos — mex28:221: Aurrerá tabela [14, 5, 1, 8, 24, 40] jogos [13, 5, 1, 7, 23, 37] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — mex28:221: Germania FV tabela [14, 3, 3, 8, 28, 45] jogos [13, 2, 3, 8, 25, 44] — faltam 1 jogo(s) do clube na página
- W.O./pontos para o mandante — Club México Real Club España (1927-09-30): awarded match to Club México
- W.O./pontos para o mandante — América do México Real Club España (1927-10-14): awarded match to América
- W.O./pontos para o mandante — Atlante Real Club España (1927-10-21): awarded match to Atlante
- W.O./pontos para o visitante — Real Club España Necaxa (1927-11-04): awarded match to Necaxa

### 1928/29

- anulado — Atlante 1-1 Asturias (1929-06-02): annulled

### 1929/30

- anulado — Real Club España 2-2 Marte (1929-11-24): annulled

### 1930/31

- sem ocorrências

### 1931/32

- sem ocorrências

### 1932/33

- sem ocorrências

### 1933/34

- tabela publicada x jogos — mex34:159: Atlante tabela [10, 6, 1, 3, 30, 32] jogos [9, 5, 1, 3, 29, 32] — a outra tabela publicada (mex34) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — mexhist:627: Real Club España tabela [10, 6, 1, 3, 27, 22] jogos [9, 6, 1, 2, 27, 21] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — mexhist:627: Atlante tabela [10, 6, 1, 3, 30, 32] jogos [9, 5, 1, 3, 29, 32] — a outra tabela publicada (mex34) fecha com os jogos: o erro é desta tabela

### 1934/35

- sem ocorrências

### 1935/36

- sem ocorrências

### 1936/37

- tabela publicada x jogos — mex37:154: Real Club España tabela [8, 1, 4, 3, 16, 17] jogos [8, 1, 4, 3, 16, 15] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mex37:154: Asturias tabela [8, 2, 1, 5, 16, 24] jogos [8, 2, 1, 5, 14, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mexhist:684: Real Club España tabela [8, 1, 4, 3, 16, 17] jogos [8, 1, 4, 3, 16, 15] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mexhist:684: Asturias tabela [8, 2, 1, 5, 16, 24] jogos [8, 2, 1, 5, 14, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1937/38

- sem ocorrências

### 1938/39

- sem ocorrências

### 1939/40

- sem ocorrências

### 1940/41

- tabela publicada x jogos — mex41:299: Asturias tabela [14, 5, 2, 7, 25, 20] jogos [14, 5, 2, 7, 25, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mex41:299: Moctezuma de Orizaba tabela [14, 4, 3, 7, 25, 37] jogos [14, 4, 3, 7, 26, 37] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela mex41:283 fora da conferência: tabela de campo, de antes da decisão de 5/2/1941 que deu ao Selección Jalisco, ao Atlante e ao América os jogos contra o Asturias (jogador irregular); vale a tabela oficial logo abaixo
- decidido fora de campo — Asturias Selección Jalisco (1940-12-15): originally 2-1; awarded match to Selección Jalisco 0-1
- decidido fora de campo — Asturias Atlante (1940-12-22): originally 1-1; awarded match to Atlante 0-1
- decidido fora de campo — América do México Asturias (1940-12-29): originally 5-5; awarded match to América 1-0

### 1941/42

- sem ocorrências

### 1942/43

- sem ocorrências

### 1943/44

- sem ocorrências

### 1944/45

- sem ocorrências

### 1945/46

- tabela publicada x jogos — mexhist:865: San Sebastián de León tabela [30, 5, 5, 20, 46, 87] jogos [30, 6, 5, 19, 46, 87] — a outra tabela publicada (mex46) fecha com os jogos: o erro é desta tabela
- decidido fora de campo — ADO Orizaba San Sebastián de León (1946-06-10): A.D.O. did not show up; awarded match to San Sebastián 0-1*

### 1946/47

- sem ocorrências

### 1947/48

- sem ocorrências

### 1948/49

- sem ocorrências

### 1949/50

- sem ocorrências

### 1950/51

- sem ocorrências

### 1951/52

- sem ocorrências

### 1952/53

- sem ocorrências

### 1953/54

- sem ocorrências

### 1954/55

- sem ocorrências

### 1955/56

- tabela publicada x jogos — mexhist:1165: Cuautla tabela [26, 6, 9, 11, 28, 46] jogos [26, 6, 9, 11, 28, 47] — a outra tabela publicada (mex56) fecha com os jogos: o erro é desta tabela
- decidido fora de campo — Atlante Atlas (1955-07-27): originally 1-1; however, awarded match to Atlante 1-0 by undue alignment of Atlas’ player Juan Bautista Pérez
- decidido fora de campo — Toluca Atlas (1955-09-25): abandoned at 30’ with the score 0-1, Atlas walked off in protest to refereeing decisions; match awarded to Toluca 1-0

### 1956/57

- tabela publicada x jogos — mexhist:1205: Oro tabela [24, 9, 5, 10, 38, 49] jogos [24, 9, 5, 10, 38, 40] — a outra tabela publicada (mex57) fecha com os jogos: o erro é desta tabela

### 1957/58

- sem ocorrências

### 1958/59

- sem ocorrências

### 1959/60

- decidido fora de campo — Toluca Atlas (1960-06-28): Toluca dns; match awarded to Atlas 0-1*

### 1960/61

- tabela publicada x jogos — mex61:509: Atlas tabela [26, 11, 7, 8, 38, 31] jogos [26, 11, 7, 8, 39, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1961/62

- sem ocorrências

### 1962/63

- sem ocorrências

### 1963/64

- sem ocorrências

### 1964/65

- sem ocorrências

### 1965/66

- tabela publicada x jogos — mex66:682: Guadalajara tabela [30, 17, 6, 7, 47, 33] jogos [30, 17, 6, 7, 47, 34] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mex66:682: Necaxa tabela [30, 10, 9, 11, 35, 42] jogos [30, 10, 9, 11, 35, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1966/67

- sem ocorrências

### 1967/68

- sem ocorrências

### 1968/69

- sem ocorrências

### 1969/70

- tabela publicada x jogos — mex6970:787: Cruz Azul tabela [30, 14, 11, 5, 40, 19] jogos [30, 13, 12, 5, 40, 19] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mex6970:787: América do México tabela [30, 12, 7, 11, 50, 49] jogos [30, 12, 7, 11, 50, 48] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mex6970:787: León tabela [30, 11, 9, 10, 43, 43] jogos [30, 10, 10, 10, 43, 43] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mex6970:787: Pachuca tabela [30, 11, 7, 12, 41, 49] jogos [30, 11, 7, 12, 41, 50] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mex6970:787: Pumas tabela [30, 8, 9, 13, 42, 43] jogos [30, 9, 11, 10, 42, 43] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mex6970:787: Irapuato tabela [30, 8, 8, 14, 26, 36] jogos [30, 7, 8, 15, 26, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1970 México 70

- torneio curto entre 1969/70 e 1970/71, jogado antes e depois da Copa do Mundo de 1970; a federação o conta como título

### 1970/71

- sem ocorrências

### 1971/72

- sem ocorrências

### 1972/73

- sem ocorrências

### 1973/74

- tabela publicada x jogos — mex74:881: Necaxa tabela [34, 15, 11, 8, 66, 47] jogos [34, 14, 13, 7, 66, 47] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mex74:881: Atlante tabela [34, 5, 14, 15, 44, 67] jogos [34, 6, 12, 16, 44, 67] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1974/75

- sem ocorrências

### 1975/76

- tabela publicada x jogos — mex76:1292: Unión de Curtidores tabela [38, 10, 20, 8, 52, 47] jogos [38, 10, 20, 8, 53, 47] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mex76:1311: Laguna de Torreón tabela [38, 12, 15, 11, 53, 46] jogos [38, 12, 15, 11, 53, 47] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1976/77

- sem ocorrências

### 1977/78

- sem ocorrências

### 1978/79

- tabela publicada x jogos — mex79:1549: Tigres tabela [6, 3, 2, 1, 8, 7] jogos [6, 3, 2, 1, 7, 6] — a outra tabela publicada (mex79) fecha com os jogos: o erro é desta tabela
- decidido fora de campo — Tampico Deportivo Neza (1978-09-24): Tampico had won 4-1; awarded to Deportivo Neza 0-1 by undue alignment of Sergio Lira

### 1979/80

- sem ocorrências

### 1980/81

- sem ocorrências

### 1981/82

- sem ocorrências

### 1982/83

- sem ocorrências

### 1983/84

- sem ocorrências

### 1984/85

- sem ocorrências

### 1985 Prode 85

- torneio curto no lugar da temporada 1985/86 (Copa do Mundo de 1986); a federação o conta como título desde outubro de 1986

### 1986 México 86

- torneio curto no lugar da temporada 1985/86 (Copa do Mundo de 1986); a federação o conta como título desde outubro de 1986

### 1986/87

- tabela publicada x jogos — mex87:1108: Deportivo Neza tabela [40, 14, 11, 15, 40, 43] jogos [40, 14, 11, 15, 40, 42] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mex87:1117: Pumas tabela [40, 14, 12, 14, 39, 38] jogos [40, 14, 12, 14, 38, 38] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- decidido fora de campo — Monterrey Tigres (1987-03-21): awarded match to U.A.N.L. 0-2

### 1987/88

- sem ocorrências

### 1988/89

- tabela publicada x jogos — mex89:1502: Tampico Madero tabela [6, 3, 1, 2, 9, 10] jogos [6, 3, 1, 2, 9, 9] — a outra tabela publicada (mex89) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — mex89:1502: Atlante tabela [6, 0, 3, 3, 9, 14] jogos [6, 0, 3, 3, 8, 14] — a outra tabela publicada (mex89) fecha com os jogos: o erro é desta tabela
- decidido fora de campo — Tigres Toluca (1989-04-08): originally 0-0; awarded match To U.A.N.L. 2-0 by undue alignment of two players of Toluca
- decidido fora de campo — Atlético Potosino Tigres (1989-06-09): originally 1-0; awarded match to U.A.N.L. 0-2 by undue alignment of Potosino

### 1989/90

- tabela publicada x jogos — mex90:963: Pumas tabela [38, 15, 16, 7, 58, 38] jogos [38, 15, 16, 7, 59, 38] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1990/91

- tabela publicada x jogos — mex91:1279: Morelia tabela [38, 10, 15, 13, 48, 51] jogos [38, 11, 14, 13, 49, 51] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mex91:1295: Puebla tabela [38, 14, 11, 13, 40, 43] jogos [38, 14, 10, 14, 40, 44] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1991/92

- sem ocorrências

### 1992/93

- tabela publicada x jogos — mex93:978: Veracruz tabela [38, 14, 9, 15, 56, 56] jogos [38, 14, 9, 15, 56, 55] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mex93:987: Tecos tabela [38, 15, 16, 7, 43, 32] jogos [38, 15, 16, 7, 42, 32] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1993/94

- tabela publicada x jogos — mex94:1009: Santos Laguna tabela [38, 16, 13, 9, 58, 56] jogos [38, 15, 13, 10, 56, 58] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — mex94:1037: Toros Neza tabela [38, 10, 11, 17, 46, 69] jogos [38, 11, 11, 16, 48, 67] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- decidido fora de campo — Toros Neza Santos Laguna (1993-10-03): awarded 2-0 to Santos; Estadio Neza 86' was closed by the authorities

### 1994/95

- sem ocorrências

### 1995/96

- tabela publicada x jogos — mex96:815: Guadalajara tabela [34, 11, 10, 13, 37, 42] jogos [33, 10, 10, 13, 34, 42] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — mex96:833: Pumas tabela [34, 13, 11, 10, 50, 41] jogos [33, 13, 11, 9, 50, 38] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — mex96:876: Pumas tabela [34, 13, 11, 10, 50, 41] jogos [33, 13, 11, 9, 50, 38] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — mex96:876: Guadalajara tabela [34, 11, 10, 13, 37, 42] jogos [33, 10, 10, 13, 34, 42] — faltam 1 jogo(s) do clube na página

### 1996 Invierno

- tabela publicada x jogos — mex97:60: Pachuca tabela [17, 3, 6, 8, 25, 26] jogos [17, 3, 6, 8, 25, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1997 Verano

- decidido fora de campo — Cruz Azul Toluca (1997-05-04): originally 3-2; match awarded to Cruz Azul 3-0 by undue alignment of Toluca (5 foreign players in Mexico City)

### 1997 Invierno

- sem ocorrências

### 1998 Verano

- sem ocorrências

### 1998 Invierno

- sem ocorrências

### 1999 Verano

- sem ocorrências

### 1999 Invierno

- sem ocorrências

### 2000 Verano

- tabela publicada x jogos — mex00:668: Tigres tabela [17, 5, 7, 5, 27, 22] jogos [17, 5, 7, 5, 25, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- anulado — Atlante 1-3 Tigres (2000-02-14): annulled as Donizete (Tigres) ineligible
- anulado — Tigres 2-1 Toluca (2000-02-19): annulled as Donizete (Tigres) ineligible
- anulado — Monterrey 3-6 Tigres (2000-02-26): annulled as Donizete (Tigres) ineligible

### 2000 Invierno

- tabela publicada x jogos — mex01:87: América do México tabela [17, 7, 5, 5, 26, 24] jogos [17, 7, 5, 5, 26, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 2001 Verano

- tabela publicada x jogos — mex01:693: América do México tabela [17, 7, 7, 3, 26, 16] jogos [17, 7, 7, 3, 25, 15] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 2001 Invierno

- decidido fora de campo — Pumas 0-2 Atlante (2001-08-19): originally 1-2, awarded match to Atlante 0-2 by undue alignment of Pumas Alejandro Glaría 27 (annulled); José Manuel Abundis 40pen, Oscar Maturín 67

### 2002 Verano

- ESPN: 152 jogos casados

### 2002 Apertura

- ESPN: 204 jogos casados
- tabela publicada x jogos — mexhist:5171: Morelia tabela [19, 9, 6, 4, 35, 23] jogos [19, 9, 5, 5, 35, 23] — a outra tabela publicada (mex03) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — mexhist:5179: Atlante tabela [19, 6, 8, 5, 31, 33] jogos [19, 6, 7, 6, 31, 33] — a outra tabela publicada (mex03) fecha com os jogos: o erro é desta tabela

### 2003 Clausura

- ESPN: 205 jogos casados

### 2003 Apertura

- ESPN: 208 jogos casados
- tabela publicada x jogos — mex04:27: Tigres tabela [19, 11, 4, 4, 38, 20] jogos [19, 11, 5, 3, 38, 20] — a outra tabela publicada (mexhist) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — mex04:27: Morelia tabela [19, 7, 5, 7, 25, 29] jogos [19, 7, 4, 8, 25, 29] — a outra tabela publicada (mexhist) fecha com os jogos: o erro é desta tabela

### 2004 Clausura

- ESPN: 206 jogos casados
- tabela publicada x jogos — mexhist:5408: Pachuca tabela [19, 6, 8, 5, 32, 32] jogos [19, 6, 8, 5, 32, 33] — a outra tabela publicada (mex04) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — mexhist:5417: Tecos tabela [19, 5, 3, 11, 31, 40] jogos [19, 5, 3, 11, 32, 40] — a outra tabela publicada (mex04) fecha com os jogos: o erro é desta tabela

### 2004 Apertura

- ESPN: 167 jogos casados
- decidido fora de campo — Veracruz Jaguares de Chiapas (2004-11-21): awarded 0-2, Veracruz dns

### 2005 Clausura

- ESPN: 167 jogos casados
- tabela publicada x jogos — mexhist:5591: Pachuca tabela [17, 4, 5, 8, 20, 27] jogos [17, 5, 5, 7, 20, 27] — a outra tabela publicada (mex05) fecha com os jogos: o erro é desta tabela

### 2005 Apertura

- ESPN: 167 jogos casados

### 2006 Clausura

- ESPN: 167 jogos casados

### 2006 Apertura

- ESPN: 170 jogos casados
- corrigido — Necaxa x Morelia (2006-10-14): Necaxa x Morelia suspenso aos 40' (1-1) e completado depois (os 50' restantes): fica só a linha da continuação, com o placar final

### 2007 Clausura

- ESPN: 168 jogos casados
- decidido fora de campo — Pachuca Cruz Azul (2007-05-13): Cruz Azul suspended for one match for

### 2007 Apertura

- ESPN: 170 jogos casados

### 2008 Clausura

- ESPN: 171 jogos casados

### 2008 Apertura

- ESPN: 167 jogos casados

### 2009 Clausura

- ESPN: 167 jogos casados

### 2009 Apertura

- ESPN: 167 jogos casados

### 2010 Clausura

- ESPN: 166 jogos casados

### 2010 Apertura

- ESPN: 165 jogos casados

### 2011 Clausura

- ESPN: 167 jogos casados

### 2011 Apertura

- ESPN: 167 jogos casados

### 2012 Clausura

- ESPN: 167 jogos casados

### 2012 Apertura

- ESPN: 166 jogos casados

### 2013 Clausura

- ESPN: 167 jogos casados

### 2013 Apertura

- ESPN: 165 jogos casados

### 2014 Clausura

- ESPN: 167 jogos casados

### 2014 Apertura

- ESPN: 165 jogos casados

### 2015 Clausura

- ESPN: 165 jogos casados

### 2015 Apertura

- ESPN: 165 jogos casados

### 2016 Clausura

- ESPN: 167 jogos casados

### 2016 Apertura

- ESPN: 165 jogos casados

### 2017 Clausura

- ESPN: 165 jogos casados

### 2017 Apertura

- ESPN: 167 jogos casados
- corrigido — Monterrey x Santos Laguna (2017-09-27): Monterrey x Santos suspenso aos 12' (0-0, tempestade) e completado em 9/11 (os 79' restantes): fica só a linha da continuação, com o placar final (1-1)

### 2018 Clausura

- ESPN: 165 jogos casados

### 2018 Apertura

- ESPN: 167 jogos casados

### 2019 Clausura

- ESPN: 167 jogos casados

### 2019 Apertura

- ESPN: 183 jogos casados

### 2020 Clausura

- ESPN: 90 jogos casados

### 2020 Apertura

- ESPN: 171 jogos casados

### 2021 Clausura

- ESPN: 170 jogos casados
- decidido fora de campo — Atlas América do México (2021-02-20): awarded 3-0; originally 0-2, América used ineligible player (Federico Viñas)

### 2021 Apertura

- ESPN: 171 jogos casados

### 2022 Clausura

- ESPN: 171 jogos casados
- decidido fora de campo — Querétaro Atlas (2022-03-05): awarded 0-3; abandoned at 0-1 in 62'
- decidido fora de campo — Tigres Atlas (2022-05-21): awarded 0-2; originally 4-2, Tigres

### 2022 Apertura

- ESPN: 171 jogos casados

### 2023 Clausura

- ESPN: 171 jogos casados

### 2023 Apertura

- ESPN: 167 jogos casados

### 2024 Clausura

- ESPN: 170 jogos casados

### 2024 Apertura

- ESPN: 167 jogos casados

### 2025 Clausura

- ESPN: 169 jogos casados

### 2025 Apertura

- ESPN: 168 jogos casados

### 2026 Clausura

- ESPN: 167 jogos casados

