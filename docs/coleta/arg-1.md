# Campeonato Argentino (1ª divisão) — coleta de dados

Gerado por `python coleta/arg-1/importar.py`. Pacote em `data/coleta/arg-1/pacote/`.

**Edições:** 196: 195 torneios que deram título de campeão argentino da 1ª divisão, de 1891 a 2025, como na lista de campeões da RSSSF (`argchamp.html`) e na Wikipédia em inglês (*List of Argentine football champions*): as duas trazem os mesmos 195 campeões. Ano com mais de um campeão oficial vira uma edição por torneio: ligas rivais (Asociación x Federación em 1912-1914, Asociación x Amateurs em 1919-1926, Liga profissional x Asociación amadora em 1931-1934), Copa de Honor, Copa Campeonato e Copa de Oro em 1936, Metropolitano e Nacional de 1967 a 1985, Apertura e Clausura de 1991/92 a 2011/12 e em 2025, Inicial, Final e o jogo do Campeonato 2012/13, mais a tabela anual de 2025.

**Fora do pacote:** as copas da liga (Copa de la Superliga 2019, Copa de la Liga Profesional 2020-2024) e a Copa Campeonato 2013/14, que a AFA e a RSSSF tratam como copas; os torneios de reclassificação, os promocionais, as liguillas pré-Libertadores e os jogos de promoção contra clubes da 2ª divisão.

**Tabela anual de 2025:** o Rosario Central foi proclamado "campeão da Liga" pela AFA em 20/11/2025. Entra como a edição "2025 Liga", sem jogos próprios (decisão do Guilherme, 20/11/2026): a classificação é a tabela anual da RSSSF, que fecha com a soma das fases de grupos do Apertura e do Clausura.

**Fontes:** RSSSF (uma página por temporada, `data/coleta/arg-1/rsssf/`: base de jogos, fases, grupos, rodadas, datas, local e autores dos gols; as tabelas da própria página e as dos índices por década, `arghist-*.html`, são a conferência); ogol (calendários de 1931 em diante, com muitos anos vazios: rodada e data que faltam, conferência de placar e o nome de cada clube no ogol); ESPN (liga `arg.1`, 2001 em diante: hora, estádio, público, gols com minuto e cartões); Wikipédia (lista de campeões, segunda fonte do campeão).

**Regras:** o placar é o da RSSSF; o ogol só completa rodada e data e entra como conferência. Jogo decidido no tribunal leva o placar dado (`awd`) ou, sem placar, a vitória (`wo`, com o placar de campo na observação). Jogo suspenso e repetido fica como `abd` e não conta; suspenso e continuado depois vira um jogo só. Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos por vitória: 2 até 1994/95 e 3 a partir do Apertura 1995 (em 1988/89, 3 pela vitória e 2 ou 1 no empate decidido nos pênaltis).

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1891 | 5 | 21 (21) | 106 | 10 | 2 / 0 | Saint Andrew's | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1893 | 5 | 23 (20) | 67 | 0 | 1 / 0 | Lomas Athletic | RSSSF (arg1893) |
| 1894 | 7 | 31 (31) | 92 | 0 | 0 / 0 | Lomas Athletic | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1895 | 6 | 24 (24) | 85 | 0 | 0 / 0 | Lomas Athletic | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1896 | 5 | 22 (20) | 73 | 4 | 0 / 1 | Lomas Academicals | RSSSF (arg1896) |
| 1897 | 7 | 45 (45) | 215 | 1 | 1 / 0 | Lomas Athletic | RSSSF (arg1897) |
| 1898 | 7 | 44 (44) | 126 | 3 | 1 / 0 | Lomas Athletic | RSSSF (arg1898) |
| 1899 | 4 | 12 (12) | 17 | 0 | 1 / 0 | Belgrano Athletic | RSSSF (arg1899) |
| 1900 | 4 | 12 (12) | 44 | 5 | 1 / 0 | Alumni | RSSSF (arg1900) |
| 1901 | 4 | 12 (12) | 36 | 0 | 1 / 0 | Alumni | RSSSF (arg1901) |
| 1902 | 5 | 20 (20) | 52 | 2 | 1 / 0 | Alumni | RSSSF (arg1902) |
| 1903 | 6 | 30 (30) | 115 | 10 | 1 / 0 | Alumni | RSSSF (arg1903) |
| 1904 | 6 | 30 (30) | 90 | 4 | 1 / 0 | Belgrano Athletic | RSSSF (arg1904) |
| 1905 | 7 | 43 (42) | 182 | 2 | 1 / 0 | Alumni | RSSSF (arg1905) |
| 1906 | 11 | 51 (52) | 218 | 4 | 3 / 0 | Alumni | RSSSF (arg1906) |
| 1907 | 11 | 111 (110) | 411 | 5 | 1 / 0 | Alumni | RSSSF (arg1907) |
| 1908 | 11 | 92 (92) | 363 | 0 | 0 / 1 | Belgrano Athletic | RSSSF (arg1908) |
| 1909 | 10 | 90 (90) | 347 | 0 | 0 / 1 | Alumni | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1910 | 9 | 72 (72) | 279 | 0 | 0 / 1 | Alumni | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1911 | 9 | 73 (73) | 248 | 3 | 1 / 0 | Alumni | RSSSF (arg11) |
| 1912 Asociación | 10 | 64 (64) | 149 | 3 | 1 / 0 | Quilmes | RSSSF (arg12) |
| 1912 Federación | 8 | 58 (58) | 187 | 0 | 1 / 1 | Porteño | RSSSF (arg12) |
| 1913 Asociación | 15 | 138 (139) | 478 | 0 | 3 / 2 | Racing Club | RSSSF (arg13) |
| 1913 Federación | 10 | 90 (90) | 338 | 0 | 1 / 1 | Estudiantes | RSSSF (arg13) |
| 1914 Asociación | 14 | 87 (87) | 247 | 54 | 2 / 0 | Racing Club | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1914 Federación | 10 | 77 (77) | 196 | 0 | 2 / 0 | Porteño | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1915 | 25 | 302 (301) | 956 | 1 | 0 / 2 | Racing Club | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1916 | 22 | 231 (231) | 547 | 2 | 2 / 0 | Racing Club | RSSSF (arg16) |
| 1917 | 21 | 211 (210) | 579 | 0 | 2 / 0 | Racing Club | RSSSF (arg17) |
| 1918 | 20 | 191 (190) | 488 | 0 | 2 / 0 | Racing Club | RSSSF (arg18) |
| 1919 Asociación | 6 | 18 (18) | 55 | 0 | 1 / 0 | Boca Juniors | RSSSF (arg19) |
| 1919 Amateurs | 14 | 91 (91) | 276 | 3 | 0 / 1 | Racing Club | RSSSF (arg19) |
| 1920 Asociación | 13 | 153 (153) | 356 | 1 | 1 / 0 | Boca Juniors | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1920 Amateurs | 19 | 306 (306) | 822 | 0 | 1 / 0 | River Plate | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1921 Asociación | 11 | 98 (98) | 225 | 114 | 1 / 0 | Huracán | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1921 Amateurs | 21 | 405 (405) | 963 | 413 | 0 / 1 | Racing Club | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1922 Asociación | 17 | 136 (136) | 361 | 93 | 0 / 1 | Huracán | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1922 Amateurs | 21 | 427 (420) | 1018 | 409 | 0 / 1 | Independiente | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1923 Asociación | 23 | 329 (329) | 861 | 0 | 0 / 0 | Boca Juniors | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1923 Amateurs | 21 | 210 (210) | 473 | 0 | 0 / 1 | San Lorenzo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1924 Asociación | 22 | 226 (226) | 573 | 271 | 0 / 1 | Boca Juniors | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1924 Amateurs | 24 | 282 (276) | 678 | 383 | 0 / 1 | San Lorenzo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1925 Asociación | 23 | 237 (235) | 544 | 167 | 0 / 2 | Huracán | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1925 Amateurs | 25 | 301 (300) | 650 | 230 | 1 / 0 | Racing Club | RSSSF (arg25) |
| 1926 Asociación | 24 | 220 (220) | 431 | 0 | 1 / 2 | Boca Juniors | RSSSF (arghist-ama1920s) |
| 1926 Amateurs | 26 | 325 (325) | 902 | 2 | 1 / 1 | Independiente | RSSSF (arg26) |
| 1927 | 34 | 564 (563) | 1646 | 264 | 0 / 2 | San Lorenzo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1928 | 36 | 631 (630) | 1899 | 249 | 0 / 1 | Huracán | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1929 | 35 | 291 (291) | 760 | 3 | 3 / 2 | Gimnasia La Plata | calculada: tabelas publicadas da 1ª fase (com os W.O.) mais os jogos das outras fases |
| 1930 | 36 | 633 (630) | 1990 | 636 | 0 / 2 | Boca Juniors | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1931 Liga | 18 | 311 (306) | 1093 | 0 | 0 / 1 | Boca Juniors | RSSSF (arg31) |
| 1931 Asociación | 17 | 128 (128) | 402 | 5 | 2 / 0 | Estudiantil Porteño | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1932 Liga | 18 | 311 (307) | 1078 | 3 | 1 / 0 | River Plate | RSSSF (arg32) |
| 1932 Asociación | 17 | 276 (275) | 864 | 793 | 0 / 1 | Sportivo Barracas | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1933 Liga | 18 | 307 (306) | 1075 | 1 | 1 / 0 | San Lorenzo | RSSSF (arg33) |
| 1933 Asociación | 20 | 190 (190) | 586 | 543 | 1 / 0 | Sportivo Dock Sud | RSSSF (arg33a) |
| 1934 Liga | 15 | 276 (276) | 994 | 6 | 0 / 1 | Boca Juniors | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1934 Asociación | 23 | 253 (253) | 812 | 809 | 0 / 1 | Estudiantil Porteño | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1935 | 18 | 306 (306) | 1108 | 0 | 1 / 0 | Boca Juniors | RSSSF (arghist-pro1930s) |
| 1936 Copa de Honor | 18 | 153 (153) | 571 | 5 | 1 / 0 | San Lorenzo | RSSSF (arg-hon36) |
| 1936 Campeonato | 18 | 153 (153) | 592 | 0 | 1 / 0 | River Plate | RSSSF (arghist-pro1930s) |
| 1936 Copa de Oro | 2 | 1 (1) | 6 | 6 | 0 / 0 | River Plate | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1937 | 18 | 307 (307) | 1293 | 0 | 1 / 0 | River Plate | RSSSF (arghist-pro1930s) |
| 1938 | 17 | 272 (272) | 1334 | 0 | 1 / 0 | Independiente | RSSSF (arghist-pro1930s) |
| 1939 | 18 | 309 (308) | 1261 | 2 | 3 / 0 | Independiente | RSSSF (arg39) |
| 1940 | 18 | 306 (306) | 1243 | 0 | 1 / 0 | Boca Juniors | RSSSF (arghist-pro1930s) |
| 1941 | 16 | 241 (240) | 963 | 4 | 1 / 0 | River Plate | RSSSF (arg41) |
| 1942 | 16 | 240 (240) | 895 | 0 | 1 / 0 | River Plate | RSSSF (arghist-pro1940s) |
| 1943 | 16 | 240 (240) | 897 | 0 | 1 / 0 | Boca Juniors | RSSSF (arghist-pro1940s) |
| 1944 | 16 | 240 (240) | 923 | 0 | 1 / 0 | Boca Juniors | RSSSF (arghist-pro1940s) |
| 1945 | 16 | 240 (240) | 948 | 0 | 1 / 0 | River Plate | RSSSF (arghist-pro1940s) |
| 1946 | 16 | 240 (240) | 922 | 4 | 1 / 0 | San Lorenzo | RSSSF (arg46) |
| 1947 | 16 | 240 (240) | 903 | 0 | 1 / 0 | River Plate | RSSSF (arghist-pro1940s) |
| 1948 | 16 | 240 (240) | 878 | 0 | 1 / 0 | Independiente | RSSSF (arg48) |
| 1949 | 18 | 312 (312) | 1092 | 0 | 1 / 0 | Racing Club | RSSSF (arg49) |
| 1950 | 18 | 311 (311) | 1111 | 3 | 2 / 0 | Racing Club | RSSSF (arg50) |
| 1951 | 17 | 274 (274) | 925 | 0 | 1 / 0 | Racing Club | RSSSF (arghist-pro1950s) |
| 1952 | 16 | 240 (240) | 848 | 0 | 1 / 0 | River Plate | RSSSF (arghist-pro1950s) |
| 1953 | 16 | 240 (240) | 731 | 0 | 1 / 0 | River Plate | RSSSF (arg53) |
| 1954 | 16 | 240 (240) | 768 | 0 | 1 / 0 | Boca Juniors | RSSSF (arghist-pro1950s) |
| 1955 | 16 | 243 (240) | 725 | 3 | 1 / 0 | River Plate | RSSSF (arg55) |
| 1956 | 16 | 240 (240) | 753 | 0 | 1 / 0 | River Plate | RSSSF (arg56) |
| 1957 | 16 | 240 (240) | 729 | 0 | 2 / 0 | River Plate | RSSSF (arg57) |
| 1958 | 16 | 242 (242) | 875 | 6 | 3 / 0 | Racing Club | RSSSF (arg58) |
| 1959 | 16 | 240 (240) | 773 | 3 | 2 / 0 | San Lorenzo | RSSSF (arg59) |
| 1960 | 16 | 240 (240) | 812 | 1 | 2 / 0 | Independiente | RSSSF (arg60) |
| 1961 | 16 | 240 (240) | 757 | 5 | 2 / 0 | Racing Club | RSSSF (arg61) |
| 1962 | 15 | 210 (210) | 606 | 4 | 2 / 0 | Boca Juniors | RSSSF (arg62) |
| 1963 | 14 | 182 (182) | 507 | 10 | 2 / 0 | Independiente | RSSSF (arg63) |
| 1964 | 16 | 240 (240) | 583 | 2 | 2 / 0 | Boca Juniors | RSSSF (arg64) |
| 1965 | 18 | 306 (305) | 696 | 676 | 0 / 2 | Boca Juniors | RSSSF (arghist-pro1960s) |
| 1966 | 20 | 380 (380) | 888 | 0 | 2 / 0 | Racing Club | RSSSF (arg66) |
| 1967 Metropolitano | 22 | 245 (245) | 606 | 3 | 5 / 0 | Estudiantes | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1967 Nacional | 16 | 120 (120) | 342 | 4 | 1 / 0 | Independiente | RSSSF (arg67) |
| 1968 Metropolitano | 22 | 246 (246) | 585 | 3 | 4 / 1 | San Lorenzo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1968 Nacional | 16 | 123 (123) | 364 | 6 | 2 / 0 | Vélez Sarsfield | RSSSF (arg68) |
| 1969 Metropolitano | 22 | 247 (247) | 636 | 5 | 5 / 0 | Chacarita Juniors | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1969 Nacional | 18 | 155 (155) | 467 | 4 | 2 / 0 | Boca Juniors | RSSSF (arg69) |
| 1970 Metropolitano | 21 | 210 (210) | 567 | 5 | 1 / 0 | Independiente | RSSSF (arg70) |
| 1970 Nacional | 20 | 205 (205) | 635 | 3 | 3 / 1 | Boca Juniors | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1971 Metropolitano | 19 | 342 (342) | 1004 | 998 | 1 / 0 | Independiente | RSSSF (arg71) |
| 1971 Nacional | 28 | 199 (199) | 644 | 636 | 1 / 1 | Rosario Central | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1972 Metropolitano | 18 | 306 (306) | 878 | 2 | 1 / 0 | San Lorenzo | RSSSF (arg72) |
| 1972 Nacional | 26 | 173 (173) | 576 | 1 | 3 / 2 | San Lorenzo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1973 Metropolitano | 17 | 272 (272) | 783 | 0 | 1 / 0 | Huracán | RSSSF (arghist-pro1970s) |
| 1973 Nacional | 30 | 231 (231) | 718 | 0 | 1 / 0 | Rosario Central | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1974 Metropolitano | 18 | 170 (170) | 543 | 0 | 2 / 2 | Newell's Old Boys | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1974 Nacional | 36 | 354 (354) | 1052 | 5 | 5 / 0 | San Lorenzo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1975 Metropolitano | 20 | 380 (380) | 1168 | 1 | 1 / 0 | River Plate | RSSSF (arg75) |
| 1975 Nacional | 32 | 285 (285) | 917 | 3 | 5 / 0 | River Plate | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1976 Metropolitano | 22 | 355 (355) | 999 | 996 | 4 / 0 | Boca Juniors | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1976 Nacional | 34 | 300 (300) | 818 | 817 | 4 / 0 | Boca Juniors | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1977 Metropolitano | 23 | 513 (507) | 1349 | 1297 | 1 / 0 | River Plate | RSSSF (arg77) |
| 1977 Nacional | 32 | 230 (230) | 674 | 674 | 4 / 0 | Independiente | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1978 Metropolitano | 21 | 420 (420) | 1054 | 0 | 1 / 0 | Quilmes | RSSSF (arg78) |
| 1978 Nacional | 32 | 238 (238) | 699 | 0 | 4 / 0 | Independiente | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1979 Metropolitano | 20 | 199 (199) | 548 | 6 | 8 / 0 | River Plate | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1979 Nacional | 28 | 211 (211) | 593 | 0 | 11 / 0 | River Plate | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1980 Metropolitano | 19 | 342 (342) | 850 | 0 | 1 / 0 | River Plate | RSSSF (arghist-pro1970s) |
| 1980 Nacional | 28 | 210 (210) | 615 | 0 | 1 / 0 | Rosario Central | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1981 Metropolitano | 18 | 305 (305) | 785 | 1 | 1 / 0 | Boca Juniors | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1981 Nacional | 28 | 209 (209) | 520 | 0 | 1 / 0 | River Plate | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1982 Metropolitano | 19 | 343 (343) | 871 | 0 | 1 / 0 | Estudiantes | RSSSF (arg82) |
| 1982 Nacional | 32 | 270 (270) | 782 | 0 | 5 / 1 | Ferro Carril Oeste | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1983 Metropolitano | 19 | 342 (342) | 900 | 0 | 1 / 0 | Independiente | RSSSF (arghist-pro1980s) |
| 1983 Nacional | 32 | 198 (198) | 490 | 0 | 1 / 0 | Estudiantes | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1984 Metropolitano | 19 | 342 (342) | 790 | 0 | 0 / 1 | Argentinos Juniors | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1984 Nacional | 32 | 126 (126) | 353 | 0 | 8 / 1 | Ferro Carril Oeste | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1985 Nacional | 32 | 160 (160) | 420 | 0 | 1 / 0 | Argentinos Juniors | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1985/86 | 19 | 342 (342) | 784 | 0 | 1 / 0 | River Plate | RSSSF (arg86) |
| 1986/87 | 20 | 382 (381) | 922 | 0 | 0 / 1 | Rosario Central | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1987/88 | 20 | 381 (381) | 870 | 0 | 1 / 0 | Newell's Old Boys | RSSSF (arg88) |
| 1988/89 | 20 | 380 (380) | 888 | 0 | 0 / 1 | Independiente | RSSSF (arg89) |
| 1989/90 | 20 | 381 (381) | 803 | 0 | 0 / 2 | River Plate | RSSSF (arg90) |
| 1990/91 | 20 | 382 (382) | 806 | 804 | 0 / 5 | Newell's Old Boys | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1991/92 Apertura | 20 | 190 (190) | 366 | 0 | 1 / 0 | River Plate | RSSSF (arg92) |
| 1991/92 Clausura | 20 | 190 (190) | 371 | 0 | 1 / 0 | Newell's Old Boys | RSSSF (arg92) |
| 1992/93 Apertura | 20 | 190 (190) | 398 | 0 | 1 / 0 | Boca Juniors | RSSSF (arg93) |
| 1992/93 Clausura | 20 | 190 (190) | 389 | 0 | 0 / 2 | Vélez Sarsfield | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1993/94 Apertura | 20 | 190 (190) | 408 | 0 | 1 / 0 | River Plate | RSSSF (arg94) |
| 1993/94 Clausura | 20 | 190 (190) | 421 | 0 | 1 / 0 | Independiente | RSSSF (arg94) |
| 1994/95 Apertura | 20 | 190 (190) | 443 | 0 | 1 / 0 | River Plate | RSSSF (arg95) |
| 1994/95 Clausura | 20 | 190 (190) | 446 | 0 | 1 / 0 | San Lorenzo | RSSSF (arg95) |
| 1995/96 Apertura | 20 | 190 (190) | 456 | 445 | 1 / 0 | Vélez Sarsfield | RSSSF (arghist-pro1990s) |
| 1995/96 Clausura | 20 | 191 (190) | 518 | 502 | 0 / 1 | Vélez Sarsfield | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1996/97 Apertura | 20 | 190 (190) | 545 | 136 | 1 / 1 | River Plate | RSSSF (arg97) |
| 1996/97 Clausura | 20 | 190 (190) | 515 | 0 | 0 / 2 | River Plate | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1997/98 Apertura | 20 | 190 (190) | 574 | 0 | 0 / 1 | River Plate | RSSSF (arg98) |
| 1997/98 Clausura | 20 | 190 (190) | 541 | 0 | 2 / 0 | Vélez Sarsfield | RSSSF (arg98) |
| 1998/99 Apertura | 20 | 190 (190) | 569 | 0 | 0 / 1 | Boca Juniors | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1998/99 Clausura | 20 | 190 (190) | 488 | 0 | 0 / 1 | Boca Juniors | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1999/00 Apertura | 20 | 190 (190) | 540 | 534 | 0 / 1 | River Plate | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1999/00 Clausura | 20 | 191 (190) | 547 | 527 | 1 / 0 | River Plate | RSSSF (arg00) |
| 2000/01 Apertura | 20 | 194 (190) | 504 | 497 | 0 / 1 | Boca Juniors | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2000/01 Clausura | 20 | 190 (190) | 529 | 521 | 1 / 0 | San Lorenzo | RSSSF (arg01) |
| 2001/02 Apertura | 20 | 191 (190) | 528 | 526 | 0 / 1 | Racing Club | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2001/02 Clausura | 20 | 191 (190) | 462 | 460 | 1 / 0 | River Plate | RSSSF (arg02) |
| 2002/03 Apertura | 20 | 192 (190) | 514 | 508 | 1 / 0 | Independiente | RSSSF (arg03) |
| 2002/03 Clausura | 20 | 191 (190) | 469 | 455 | 1 / 0 | River Plate | RSSSF (arg03) |
| 2003/04 Apertura | 20 | 191 (190) | 431 | 429 | 1 / 0 | Boca Juniors | RSSSF (arg04) |
| 2003/04 Clausura | 20 | 190 (190) | 480 | 480 | 1 / 0 | River Plate | RSSSF (arg04) |
| 2004/05 Apertura | 20 | 190 (190) | 417 | 413 | 1 / 0 | Newell's Old Boys | RSSSF (arg05) |
| 2004/05 Clausura | 20 | 191 (190) | 517 | 512 | 0 / 1 | Vélez Sarsfield | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2005/06 Apertura | 20 | 190 (190) | 495 | 495 | 1 / 0 | Boca Juniors | RSSSF (arg06) |
| 2005/06 Clausura | 20 | 191 (190) | 449 | 440 | 1 / 0 | Boca Juniors | RSSSF (arg06) |
| 2006/07 Apertura | 20 | 194 (191) | 506 | 505 | 1 / 0 | Estudiantes | RSSSF (arg07) |
| 2006/07 Clausura | 20 | 192 (190) | 478 | 474 | 1 / 0 | San Lorenzo | RSSSF (arg07) |
| 2007/08 Apertura | 20 | 191 (190) | 485 | 483 | 1 / 0 | Lanús | RSSSF (arg08) |
| 2007/08 Clausura | 20 | 191 (190) | 482 | 480 | 1 / 0 | River Plate | RSSSF (arg08) |
| 2008/09 Apertura | 20 | 194 (193) | 478 | 478 | 3 / 0 | Boca Juniors | RSSSF (arg09) |
| 2008/09 Clausura | 20 | 191 (190) | 477 | 477 | 1 / 0 | Vélez Sarsfield | RSSSF (arg09) |
| 2009/10 Apertura | 20 | 190 (190) | 463 | 463 | 1 / 0 | Banfield | RSSSF (arg2010) |
| 2009/10 Clausura | 20 | 194 (190) | 465 | 465 | 1 / 0 | Argentinos Juniors | RSSSF (arg2010) |
| 2010/11 Apertura | 20 | 190 (190) | 421 | 421 | 1 / 0 | Estudiantes | RSSSF (arg2011) |
| 2010/11 Clausura | 20 | 192 (190) | 458 | 458 | 1 / 0 | Vélez Sarsfield | RSSSF (arg2011) |
| 2011/12 Apertura | 20 | 190 (190) | 376 | 376 | 1 / 0 | Boca Juniors | RSSSF (arg2012) |
| 2011/12 Clausura | 20 | 190 (190) | 439 | 439 | 1 / 0 | Arsenal de Sarandí | RSSSF (arg2012) |
| 2012/13 Inicial | 20 | 191 (190) | 418 | 416 | 1 / 0 | Vélez Sarsfield | RSSSF (arg2013) |
| 2012/13 Final | 20 | 192 (190) | 435 | 435 | 1 / 0 | Newell's Old Boys | RSSSF (arg2013) |
| 2012/13 Campeonato | 2 | 1 (1) | 1 | 1 | 1 / 0 | Vélez Sarsfield | RSSSF (arghist-pro2010s) |
| 2013/14 Inicial | 20 | 190 (190) | 409 | 408 | 1 / 0 | San Lorenzo | RSSSF (arg2014) |
| 2013/14 Final | 20 | 190 (190) | 400 | 400 | 1 / 0 | River Plate | RSSSF (arg2014) |
| 2014 | 20 | 190 (190) | 491 | 475 | 1 / 0 | Racing Club | RSSSF (arg2015) |
| 2015 | 30 | 450 (450) | 994 | 988 | 1 / 0 | Boca Juniors | RSSSF (arg2015a) |
| 2016 | 30 | 242 (483) | 606 | 606 | 3 / 2 | Lanús | RSSSF (arg2016) |
| 2016/17 | 30 | 450 (450) | 1024 | 1021 | 1 / 0 | Boca Juniors | RSSSF (arg2017) |
| 2017/18 | 28 | 378 (378) | 854 | 852 | 1 / 0 | Boca Juniors | RSSSF (arg2018) |
| 2018/19 | 26 | 325 (325) | 719 | 716 | 1 / 0 | Racing Club | RSSSF (arg2019) |
| 2019/20 | 24 | 276 (276) | 631 | 631 | 1 / 0 | Boca Juniors | RSSSF (arg2020) |
| 2021 | 26 | 325 (325) | 796 | 796 | 1 / 0 | River Plate | RSSSF (arg2021) |
| 2022 | 28 | 378 (378) | 826 | 821 | 1 / 0 | Boca Juniors | RSSSF (arg2022) |
| 2023 | 28 | 378 (378) | 778 | 778 | 1 / 0 | River Plate | RSSSF (arg2023) |
| 2024 | 28 | 378 (378) | 769 | 769 | 1 / 0 | Vélez Sarsfield | RSSSF (arg2024) |
| 2025 Apertura | 30 | 255 (255) | 506 | 502 | 8 / 0 | Platense | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2025 Clausura | 30 | 255 (255) | 488 | 486 | 8 / 0 | Estudiantes | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2025 Liga | 30 | 0 (0) | 0 | 0 | 1 / 0 | Rosario Central | RSSSF (arg2025) |
| 2026 Apertura | 30 | 255 (255) | 530 | 0 | 8 / 0 | Belgrano | calculada (fase alcançada, pontos, saldo, gols pró) |

## Conferência e correções, edição a edição

### 1891

- a liga da época deu o título dividido entre Saint Andrew's e Caledonians (empatados); Saint Andrew's venceu o desempate pelas medalhas. A AFA cita só o Saint Andrew's, que fica como campeão no pacote
- título dividido entre Saint Andrew's e Caledonians pela liga da época; a AFA só cita o Saint Andrew's (RSSSF)

### 1893

- Quilmes Club (1893) e Quilmes Rovers (1895) são clubes à parte do Quilmes atual: a ligação não tem prova (D-25 g)
- 3º da lista oficial (Quilmes) não está na classificação
- anulado — Flores Athletic Lomas Athletic (1893-07-16): 1:2, annulled on August 25
- não jogado — Quilmes Club Alumni (1893-07-30): Buenos Aires English High School did not show up
- W.O./pontos para o mandante — Quilmes Club Alumni (1893-07-30)
- anulado — Quilmes Club Flores Athletic (1893-07-30): Quimes did not show up, annulled on August 25

### 1894

- anulado — Lomas Athletic Buenos Aires and Rosario Railway (1894-04-22): 4:1 friendly, official match wp:lp and annulled
- anulado — Rosario Athletic Buenos Aires and Rosario Railway (1894-05-03): wp:lp, annulled
- W.O./pontos para o visitante — Retiro Athletic Lomas Athletic (1894-05-06): result not found
- anulado — Buenos Aires and Rosario Railway Saint Andrew's (1894-05-13): 1:2, annulled
- anulado — Retiro Athletic Buenos Aires and Rosario Railway (1894-05-25): wp:lp, annulled
- anulado — Buenos Aires and Rosario Railway Flores Athletic (1894-05-27): lp:wp, annulled
- anulado — Buenos Aires and Rosario Railway Lobos Athletic (1894-06-03): 1:2 friendly, official match lp:wp and annulled
- W.O./pontos para o mandante — Rosario Athletic Retiro Athletic (1894-06-29): result not found
- W.O./pontos para o mandante — Rosario Athletic Saint Andrew's (1894-07-22): result not found
- W.O./pontos para o mandante — Lobos Athletic Flores Athletic (1894-09-08)

### 1895

- vice pela lista oficial: Lomas Academicals (a tabela o punha em 3º)
- W.O./pontos para o mandante — Retiro Athletic Alumni (1895-05-25): result not found
- W.O./pontos para o mandante — Lomas Academicals Alumni (1895-06-08): result not found
- W.O./pontos para o mandante — Alumni Retiro Athletic (1895-06-15): result not found
- W.O./pontos para o visitante — Retiro Athletic Lomas Academicals (1895-07-13): result not found
- W.O./pontos para o mandante — Lomas Academicals Quilmes Rovers (1895-08-15): result not found

### 1896

- tabela publicada x jogos — arg1896:15: Lomas Athletic tabela [8, 4, 1, 3, 16, 11] jogos [10, 4, 3, 3, 19, 14] — sobram 2 jogo(s) do clube na página
- tabela publicada x jogos — arg1896:15: Belgrano Athletic tabela [8, 3, 2, 3, 10, 15] jogos [10, 3, 4, 3, 13, 18] — sobram 2 jogo(s) do clube na página

### 1897

- sem ocorrências

### 1898

- W.O./pontos para o mandante — Belgrano Athletic Banfield (1898-05-25): not played
- W.O./pontos para o mandante — Lomas Athletic Banfield (1898-06-19): not played
- W.O./pontos para o visitante — Banfield Belgrano Athletic (1898-07-03): awarded
- W.O./pontos para o mandante — Lobos Athletic Banfield (1898-07-03): awarded
- W.O./pontos para o mandante — Palermo Athletic Banfield (1898-07-03): awarded
- W.O./pontos para o mandante — United Banks Banfield (1898-07-03): awarded
- anulado — Lomas Athletic Lobos Athletic (1898-08-28): 1-0 annulled, at Barker Memorial School

### 1899

- W.O./pontos para o mandante — Lobos Athletic Lanús Athletic (1899-06-16): awarded wp:lp
- W.O./pontos para o mandante — Lomas Athletic Lanús Athletic (1899-08-06): awarded wp:lp
- W.O./pontos para o visitante — Lomas Athletic Lobos Athletic (1899-08-15): awarded lp:wp

### 1900

- sem ocorrências

### 1901

- sem ocorrências

### 1902

- W.O./pontos para o visitante — Lomas Athletic Alumni (1902-05-25): awarded lp-wp
- W.O./pontos para o mandante — Alumni Quilmes (1902-07-20): awarded wp-lp
- W.O./pontos para o mandante — Quilmes Belgrano Athletic (1902-07-27): awarded wp-lp
- W.O./pontos para o mandante — Alumni Lomas Athletic (1902-08-30): awarded wp-lp
- W.O./pontos para o mandante — Lomas Athletic Quilmes (1902-09-21): awarded wp-lp

### 1903

- W.O./pontos para o visitante — Flores Athletic Quilmes (1903-05-24): awarded
- W.O./pontos para o mandante — Lomas Athletic Flores Athletic (1903-06-07): awarded
- W.O./pontos para o visitante — Flores Athletic Belgrano Athletic (1903-06-14): awarded
- W.O./pontos para o mandante — Barracas Athletic Flores Athletic (1903-07-26): awarded

### 1904

- W.O./pontos para o mandante — Alumni Quilmes (1904-08-28): n/p, awarded
- W.O./pontos para o mandante — Lomas Athletic Barracas Athletic (1904-08-28): n/p, awarded
- W.O./pontos para o mandante — Barracas Athletic Quilmes (1904-09-24): n/p, awarded

### 1905

- abandonado/suspenso, sem valer — Belgrano Athletic Quilmes (1905-05-28): abandoned at 3:0 in 85
- W.O./pontos para o visitante — Belgrano Athletic Quilmes (1905-06-24): awarded lp:wp; jogo repetido (o primeiro foi suspenso)
- W.O./pontos para o visitante — Barracas Athletic Lomas Athletic (1905-07-30): awarded lp-wp
- W.O./pontos para o visitante — Barracas Athletic Quilmes (1905-08-06): awarded lp-wp
- W.O./pontos para o mandante — Alumni Barracas Athletic (1905-09-03): awarded wp-lp
- W.O./pontos para o visitante — Barracas Athletic Alumni (1905-09-03): awarded lp-wp
- W.O./pontos para o visitante — Barracas Athletic Estudiantes de Buenos Aires (1905-09-03): awarded lp-wp
- W.O./pontos para o visitante — Barracas Athletic Belgrano Athletic (1905-09-03): awarded lp-wp
- W.O./pontos para o mandante — Reformer Barracas Athletic (1905-09-03): awarded wp-lp
- W.O./pontos para o mandante — Reformer Quilmes (1905-09-17): awarded wp-lp
- W.O./pontos para o mandante — Alumni Quilmes (1905-09-24): awarded wp-lp

### 1906

- W.O./pontos para o mandante — Alumni Argentino de Quilmes (1906-09-30): awarded by W.O., at Sociedad Sportiva Argentina

### 1907

- W.O./pontos para o mandante — Reformer Lomas Athletic (1907-05-05): Lomas Athletic withdrew
- W.O./pontos para o mandante — Estudiantes de Buenos Aires San Martín Athletic (1907-05-30): San Martín Athletic withdrew
- não jogado — Lomas Athletic Belgrano Athletic (1907-06-09): 0:2, annulled, see Nov 11
- W.O./pontos para o mandante — Belgrano Athletic Barracas Athletic (1907-06-29): Barracas Athletic withdrew
- W.O./pontos para o mandante — Porteño Barracas Athletic (1907-06-30): Barracas Athletic withdrew
- W.O./pontos para o mandante — Lomas Athletic Barracas Athletic (1907-07-09): Barracas Athletic withdrew
- W.O./pontos para o mandante — Alumni Barracas Athletic (1907-07-09)
- W.O./pontos para o mandante — Estudiantes de Buenos Aires Barracas Athletic (1907-07-09)
- W.O./pontos para o visitante — Barracas Athletic Estudiantes de Buenos Aires (1907-07-09)
- W.O./pontos para o visitante — Barracas Athletic Belgrano Athletic (1907-07-09)
- W.O./pontos para o visitante — Barracas Athletic Porteño (1907-07-09)
- W.O./pontos para o visitante — Barracas Athletic Reformer (1907-07-09)
- W.O./pontos para o visitante — Barracas Athletic Argentino de Quilmes (1907-07-09)
- W.O./pontos para o mandante — Quilmes Barracas Athletic (1907-07-09)
- W.O./pontos para o mandante — San Isidro Barracas Athletic (1907-07-09)
- W.O./pontos para o mandante — San Martín Athletic Barracas Athletic (1907-07-09)
- W.O./pontos para o mandante — Quilmes Reformer (1907-09-22): Reformer withdrew
- W.O./pontos para o visitante — San Martín Athletic Argentino de Quilmes (1907-10-06): not played, awarded lp-wp
- W.O./pontos para o visitante — Quilmes Belgrano Athletic (1907-10-27)
- W.O./pontos para o visitante — Quilmes Estudiantes de Buenos Aires (1907-10-27)
- W.O./pontos para o mandante — Belgrano Athletic Lomas Athletic (1907-11-01): Lomas Athletic withdrew
- W.O./pontos para o mandante — Argentino de Quilmes Belgrano Athletic (1907-11-03): Belgrano Athletic withdrew
- W.O./pontos para o visitante — Lomas Athletic Belgrano Athletic (1907-11-11): Lomas Athletic withdrew, see Jun 9

### 1908

- Nacional de Buenos Aires: eliminado depois de 2 jogos, anulados (nota da página); fica no fim da classificação, fora da tabela publicada (AR-020)
- tabela publicada x jogos — arg1908:31: Belgrano Athletic tabela [18, 15, 1, 2, 51, 22] jogos [18, 14, 2, 2, 51, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg1908:31: Estudiantes de Buenos Aires tabela [18, 11, 2, 5, 39, 22] jogos [18, 11, 3, 4, 39, 22] — a diferença vem de Estudiantes de Buenos Aires x San Martín Athletic (1908-08-09), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg1908:31: Porteño tabela [18, 6, 1, 11, 25, 44] jogos [18, 5, 1, 12, 25, 44] — a diferença vem de Porteño x San Martín Athletic (1908-08-30), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg1908:31: San Martín Athletic tabela [18, 2, 1, 15, 19, 44] jogos [18, 3, 1, 14, 19, 44] — a diferença vem de Estudiantes de Buenos Aires x San Martín Athletic (1908-08-09), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- anulado — Reformer 1-3 Nacional de Buenos Aires (1908-05-10): annulled
- anulado — Lomas Athletic 0-3 Nacional de Buenos Aires (1908-05-17): annulled
- W.O./pontos para o mandante — San Isidro San Martín Athletic (1908-06-18): San Martín Athletic withdrew
- W.O./pontos para o mandante — Belgrano Athletic Reformer (1908-06-28): Refomer withdrew
- W.O./pontos para o visitante — Estudiantes de Buenos Aires Reformer (1908-07-26): Estudiantes withdrew
- W.O./pontos para o mandante — Estudiantes de Buenos Aires San Martín Athletic (1908-08-09): San Martín Athletic withdrew
- W.O./pontos para o mandante — Porteño San Martín Athletic (1908-08-30): San Martín Athletic withdrew
- W.O./pontos para o mandante — San Isidro Reformer (1908-09-27): Reformer withdrew
- W.O./pontos para o visitante — Lomas Athletic Argentino de Quilmes (1908-10-11): Lomas Athletic withdrew
- W.O./pontos para o mandante — Estudiantes de Buenos Aires Quilmes (1908-10-18): Quilmes withdrew
- W.O./pontos para o visitante — Lomas Athletic Estudiantes de Buenos Aires (1908-11-08): Lomas Athletic withdrew

### 1909

- tabela publicada x jogos — arg1909:51: Argentino de Quilmes tabela [18, 5, 4, 9, 19, 40] jogos [18, 5, 4, 9, 20, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg1909:51: Lomas Athletic tabela [18, 1, 6, 11, 17, 48] jogos [18, 1, 6, 11, 17, 49] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- W.O./pontos para o mandante — River Plate Reformer (1909-05-09): Reformer withdrew
- W.O./pontos para o mandante — Argentino de Quilmes San Isidro (1909-11-11): San Isidro withdrew
- W.O./pontos para o mandante — Reformer Argentino de Quilmes (1909-11-21): Argentino de Quilmes withdrew
- W.O./pontos para o mandante — Alumni Reformer (1909-11-21): Reformer withdrew
- W.O./pontos para o mandante — San Isidro Porteño (1909-11-21): Porteño withdrew

### 1910

- tabela publicada x jogos — arg10:34: Estudiantes de Buenos Aires tabela [16, 8, 3, 5, 33, 29] jogos [16, 8, 3, 5, 32, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg10:34: Quilmes tabela [16, 2, 4, 10, 24, 52] jogos [16, 2, 4, 10, 23, 51] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1911

- W.O./pontos para o mandante — Porteño Belgrano Athletic (1911-11-19): Belgrano Athletic withdrew

### 1912 Asociación

- a classificação é a tabela publicada, sem os clubes que saíram para a FAF no meio do campeonato (os jogos deles ficam) (AR-010)
- W.O./pontos para o mandante — Estudiantes de Buenos Aires Alumni (1912-04-14): Alumni withdrew
- não jogado — Estudiantes de Buenos Aires Alumni (1912-04-28): annulled
- não jogado — River Plate Gimnasia de Buenos Aires (1912-07-17): annulled
- não jogado — San Isidro Estudiantes (1912-07-17): annulled
- W.O./pontos para o mandante — Quilmes Alumni (1912-04-21): Alumni withdrew
- não jogado — Quilmes Alumni (1912-04-28): annulled
- não jogado — Racing Club Estudiantes (1912-07-17): annulled
- não jogado — River Plate Porteño (1912-07-17): annulled
- W.O./pontos para o mandante — Racing Club Alumni (1912-04-28): Alumni withdrew and the match was annulled
- não jogado — Porteño Quilmes (1912-07-17): annulled
- não jogado — San Isidro Gimnasia de Buenos Aires (1912-07-17): annulled
- não jogado — Porteño Racing Club (1912-07-17): annulled
- não jogado — Quilmes Estudiantes (1912-07-17): annulled
- não jogado — Belgrano Athletic Porteño (1912-07-17): annulled
- não jogado — Quilmes Gimnasia de Buenos Aires (1912-07-17): annulled
- não jogado — Estudiantes Estudiantes de Buenos Aires (1912-07-17): annulled
- não jogado — Racing Club Gimnasia de Buenos Aires (1912-07-17): annulled
- não jogado — San Isidro Porteño (1912-07-17): annulled
- não jogado — Estudiantes Belgrano Athletic (1912-07-17): annulled
- W.O./pontos para o mandante — Quilmes Belgrano Athletic (1912-09-26): Belgrano Athletic withdrew
- W.O./pontos para o mandante — River Plate Belgrano Athletic (1912-10-06): Belgrano Athletic withdrew
- W.O./pontos para o mandante — Racing Club Quilmes (1912-11-03): Quilmes withdrew
- não jogado — Estudiantes de Buenos Aires San Isidro (1912-11-11): both captains decided not play
- não jogado — Estudiantes de Buenos Aires San Isidro (1912-12-13): it was published as not played

### 1912 Federación

- tabela publicada x jogos — arg12:194: Porteño tabela [1, 1, 0, 0, 1, 1] jogos [1, 1, 0, 0, 0, 0] — a outra tabela publicada (arg12) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg12:194: Independiente tabela [1, 0, 0, 1, 1, 1] jogos [1, 0, 0, 1, 0, 0] — a outra tabela publicada (arg12) fecha com os jogos: o erro é desta tabela
- W.O./pontos para o mandante — Porteño Sportiva Argentina (1912-08-30): Sportiva Argentina withdrew
- W.O./pontos para o mandante — Argentino de Quilmes Sportiva Argentina (1912-10-13): Sportiva Argentina withdrew
- W.O./pontos para o visitante — Sportiva Argentina Kimberley de Buenos Aires (1912-11-01): Sportiva Argentina withdrew
- W.O./pontos para o mandante — Independiente Sportiva Argentina (1912-11-01)
- W.O./pontos para o visitante — Sportiva Argentina Gimnasia de Buenos Aires (1912-11-01)
- W.O./pontos para o visitante — Sportiva Argentina Porteño (1912-11-01)
- W.O./pontos para o visitante — Atlanta Gimnasia de Buenos Aires (1912-11-03)
- abandonado/suspenso, sem valer — Porteño Independiente (1912-12-22): at Gimnasia y Esgrima BUE, abandoned at 1:1 in 87
- W.O./pontos para o mandante — Porteño Independiente (1912-12-23): awarded wp:lp; jogo repetido (o primeiro foi suspenso)

### 1913 Asociación

- tabela publicada x jogos — arg13:218: Racing Club tabela [14, 12, 0, 2, 41, 5] jogos [19, 16, 1, 2, 50, 6] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg13:218: San Isidro tabela [14, 11, 2, 1, 44, 8] jogos [19, 14, 4, 1, 53, 13] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg13:218: River Plate tabela [14, 10, 4, 0, 30, 7] jogos [19, 13, 5, 1, 36, 12] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg13:218: Belgrano Athletic tabela [14, 8, 2, 4, 34, 16] jogos [18, 8, 2, 8, 34, 16] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg13:218: Boca Juniors tabela [14, 8, 2, 4, 29, 16] jogos [19, 12, 3, 4, 35, 19] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg13:218: Platense tabela [14, 8, 2, 4, 36, 25] jogos [18, 9, 3, 6, 38, 32] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg13:218: Quilmes tabela [14, 8, 2, 4, 29, 21] jogos [19, 8, 2, 9, 29, 21] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg13:218: Estudiantes de Buenos Aires tabela [14, 6, 1, 7, 26, 23] jogos [19, 7, 3, 9, 32, 32] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg13:218: Estudiantil Porteño tabela [14, 5, 3, 6, 32, 33] jogos [19, 7, 3, 9, 43, 44] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg13:218: Banfield tabela [14, 5, 3, 6, 23, 31] jogos [18, 6, 4, 8, 24, 36] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg13:218: Comercio tabela [14, 4, 2, 8, 26, 34] jogos [19, 6, 3, 10, 30, 42] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg13:218: Ferro Carril Oeste tabela [14, 1, 4, 9, 16, 31] jogos [17, 2, 5, 10, 22, 36] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg13:218: Ferrocarril Sud tabela [14, 1, 2, 11, 17, 51] jogos [17, 3, 2, 12, 19, 54] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg13:218: Olivos tabela [14, 1, 2, 11, 10, 49] jogos [17, 2, 3, 12, 15, 51] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg13:218: Riachuelo tabela [14, 0, 3, 11, 8, 51] jogos [17, 1, 3, 13, 16, 62] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg13:265: Racing Club tabela [18, 15, 1, 2, 47, 6] jogos [19, 16, 1, 2, 50, 6] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg13:265: River Plate tabela [18, 13, 5, 0, 36, 9] jogos [19, 13, 5, 1, 36, 12] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- W.O./pontos para o visitante — Olivos Boca Juniors (1913-05-18): not played, awarded on May 21
- W.O./pontos para o visitante — Ferrocarril Sud Racing Club (1913-11-02): Ferrocarril Sud did not show up
- W.O./pontos para o mandante — River Plate Belgrano Athletic (1913-10-12): Belgrano gave up points on Oct 10, FC Oeste, Caballito, C
- W.O./pontos para o visitante — Belgrano Athletic Platense (1913-10-15): Belgrano withdrew championship
- W.O./pontos para o visitante — Belgrano Athletic Racing Club (1913-10-15)
- W.O./pontos para o mandante — Banfield Belgrano Athletic (1913-10-15)
- W.O./pontos para o mandante — Boca Juniors Quilmes (1913-10-19): Quilmes gave up points on Oct 17, Estudiantes, Palermo, C
- W.O./pontos para o mandante — Estudiantil Porteño Quilmes (1913-10-22): Quilmes withdrew championship
- W.O./pontos para o mandante — San Isidro Quilmes (1913-10-22)
- W.O./pontos para o mandante — Estudiantes de Buenos Aires Quilmes (1913-10-22)
- W.O./pontos para o mandante — Comercio Quilmes (1913-10-22)
- W.O./pontos para o visitante — Estudiantil Porteño Comercio (1913-11-09): Estudiantil Porteño gave up points.
- W.O./pontos para o mandante — Boca Juniors Estudiantes de Buenos Aires (1913-11-30): Estudiantes did not show up, Riachuelo, Barracas, C
- W.O./pontos para o visitante — Olivos Ferrocarril Sud (1913-10-19): Originally 5:1, awarded on Feb 5
- W.O./pontos para o mandante — Ferrocarril Sud Ferro Carril Oeste (1913-11-09): Ferro Carril Oeste gave up points

### 1913 Federación

- tabela publicada x jogos — arghist-ama1910s:272: Sportiva Argentina tabela [18, 0, 2, 16, 15, 52] jogos [18, 0, 2, 16, 15, 51] — a outra tabela publicada (arg13) fecha com os jogos: o erro é desta tabela
- corrigido — Kimberley de Buenos Aires x Porteño (1913-07-27): Kimberley 3-1 Porteño é o jogo repetido em 15/08 (a nota fala do primeiro, abandonado com 0-0 aos 75' e anulado); vale na tabela
- W.O./pontos para o visitante — Sportiva Argentina Kimberley de Buenos Aires (1913-09-21): SS Argentina forfeited the match, friendly 0:4, lasted 60m
- W.O./pontos para o mandante — Argentino de Quilmes Sportiva Argentina (1913-11-09): Sportiva Argentina gave up points on Nov 7
- W.O./pontos para o mandante — Columbian Atlanta (1913-12-07): played friendly 1:3, awarded on Dec 10, at Atlanta, Parque Chacabuco, C
- W.O./pontos para o visitante — Sportiva Argentina Columbian (1913-12-21): Sociedad Sportiva did not show up

### 1914 Asociación

- anulado — Estudiantes de Buenos Aires 4-2 Ferrocarril Sud (1914-03-29): annulled
- anulado — Ferrocarril Sud 1-4 Boca Juniors (1914-04-05): annulled
- anulado — Quilmes 2-1 Ferrocarril Sud (1914-04-12): annulled
- anulado — Ferrocarril Sud 0-3 Racing Club (1914-05-03): annulled
- anulado — Ferrocarril Sud 2-3 Ferro Carril Oeste (1914-05-21): annulled
- abandonado/suspenso, sem valer — Huracán 0-0 Boca Juniors (1914-05-21): at Ferro Carril Oeste][Suspended in 81; played again Aug 9
- anulado — Ferrocarril Sud 1-1 Comercio (1914-06-07): annulled
- anulado — Belgrano Athletic 4-0 Ferrocarril Sud (1914-07-19): annulled
- abandonado/suspenso, sem valer — Ferro Carril Oeste 0-0 Racing Club (1914-08-09): Suspended in 85; played again Oct 18

### 1914 Federación

- anulado — Argentino de Quilmes 8-0 Tigre (1914-04-05): annulled
- anulado — Tigre 3-2 Atlanta (1914-04-12): annulled
- anulado — Argentino de Quilmes 5-0 Atlanta (1914-04-19): annulled
- anulado — Tigre 1-0 Columbian (1914-04-19): annulled
- abandonado/suspenso, sem valer — Argentino de Quilmes 1-1 Estudiantes (1914-06-07): Suspended in 45; played again Jun 28
- anulado — Tigre 0-0 Floresta (1914-06-07): annulled
- anulado — Tigre 1-0 Gimnasia de Buenos Aires (1914-06-21): annulled
- anulado — Argentino de Quilmes 1-1 Estudiantes (1914-06-28): at Independiente][annulled; jogo repetido (o primeiro foi suspenso)
- anulado — Tigre 1-0 Porteño (1914-06-28): annulled
- anulado — Tigre 0-0 Columbian (1914-07-12): annulled
- anulado — Atlanta 0-6 Argentino de Quilmes (1914-07-12): annulled
- anulado — Gimnasia de Buenos Aires 1-0 Argentino de Quilmes (1914-07-19): at Kimberley][annulled
- anulado — Argentino de Quilmes 2-1 Gimnasia de Buenos Aires (1914-07-26): at Estudiantes LP][annulled
- anulado — Kimberley de Buenos Aires 0-2 Tigre (1914-07-26): annulled
- anulado — Independiente 1-4 Argentino de Quilmes (1914-08-02): annulled
- anulado — Estudiantes 3-2 Tigre (1914-08-02): annulled
- anulado — Independiente 2-0 Tigre (1914-08-09): annulled
- anulado — Tigre 1-5 Gimnasia de Buenos Aires (1914-08-16): annulled
- anulado — Porteño 5-1 Tigre (1914-09-06): at Pabellón de las Rosas][annulled
- anulado — Atlanta 0-1 Tigre (1914-10-04): annulled
- W.O./pontos para o visitante — Floresta 2-3 Kimberley de Buenos Aires (1914-10-04): Suspended in 66; Kimberley won points
- anulado — Tigre 0-3 Independiente (1914-10-11): Suspended in 45; not continued][annulled
- W.O./pontos para o visitante — Floresta Independiente (1914-11-01): Floresta withdrew

### 1915

- tabela publicada x jogos — arg15:32: Racing Club tabela [24, 22, 2, 0, 96, 7] jogos [24, 21, 2, 1, 96, 7] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg15:32: San Isidro tabela [24, 22, 2, 0, 73, 13] jogos [24, 21, 3, 0, 73, 13] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg15:32: Porteño tabela [24, 17, 2, 5, 58, 28] jogos [24, 16, 2, 6, 58, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg15:32: Independiente tabela [24, 11, 5, 8, 42, 23] jogos [24, 12, 5, 7, 42, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg15:32: Banfield tabela [24, 9, 3, 12, 36, 46] jogos [24, 10, 4, 10, 36, 46] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arghist-ama1910s:368: Racing Club tabela [24, 22, 2, 0, 95, 5] jogos [25, 22, 2, 1, 97, 7] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — arghist-ama1910s:368: San Isidro tabela [24, 22, 2, 0, 72, 12] jogos [25, 21, 3, 1, 73, 14] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — arghist-ama1910s:368: Porteño tabela [24, 17, 2, 5, 57, 26] jogos [24, 16, 2, 6, 58, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arghist-ama1910s:368: Independiente tabela [24, 11, 5, 8, 40, 22] jogos [24, 12, 5, 7, 42, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- anulado — Quilmes 0-4 Estudiantes de Buenos Aires (1915-04-18): annuled; played again Nov 1
- W.O./pontos para o mandante — Estudiantil Porteño Comercio (1915-10-17)
- W.O./pontos para o mandante — Argentino de Quilmes Comercio (1915-10-31)
- W.O./pontos para o mandante — Huracán Quilmes (1915-11-11)
- W.O./pontos para o mandante — Tigre Quilmes (1915-11-14)
- W.O./pontos para o mandante — Comercio Floresta (1915-11-28)

### 1916

- W.O./pontos para o mandante — Tigre Quilmes (1916-10-22): Quilmes withdrew
- W.O./pontos para o mandante — San Lorenzo Quilmes (1916-10-29): Quilmes withdrew

### 1917

- abandonado/suspenso, sem valer — Ferro Carril Oeste 2-0 Platense (1917-04-29): Suspended at 40; played again on Dec 30

### 1918

- abandonado/suspenso, sem valer — Estudiantil Porteño 0-0 Boca Juniors (1918-04-21): Suspended at 80; played again on Oct 12
- W.O./pontos para o mandante — Defensores de Belgrano Argentino de Quilmes (1918-11-17): Argentino de Quilmes withdrew

### 1919 Asociación

- o campeonato começado em março foi anulado (clubes desfiliados ou expulsos) e recomeçado em setembro com 6 clubes; só os jogos do recomeçado entram (12 não foram jogados) (AR-008)
- linha de nota que repete o jogo Eureka x Estudiantes (arg19:307): fica de fora
- W.O./pontos para o visitante — Estudiantes Porteño (1919-11-30): friendly 0:0

### 1919 Amateurs

- tabela publicada x jogos — arg19:331: Vélez Sarsfield tabela [13, 8, 2, 3, 21, 10] jogos [12, 7, 2, 3, 18, 8] — a diferença vem de Vélez Sarsfield x Sportivo Barracas (1920-01-03), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg19:331: River Plate tabela [13, 6, 4, 3, 16, 11] jogos [10, 6, 2, 2, 15, 9] — a diferença vem de River Plate x Tigre (1919-10-26), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg19:331: Defensores de Belgrano tabela [13, 6, 4, 3, 20, 18] jogos [12, 6, 3, 3, 18, 16] — a diferença vem de Sportivo Barracas x Defensores de Belgrano (1919-11-30), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg19:331: Gimnasia La Plata tabela [13, 6, 1, 6, 18, 19] jogos [12, 5, 1, 6, 17, 19] — a diferença vem de River Plate x Gimnasia La Plata (1919-11-30), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg19:331: Independiente tabela [13, 5, 2, 6, 22, 20] jogos [12, 5, 1, 6, 22, 20] — a diferença vem de River Plate x Independiente (1919-11-11), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg19:331: Platense tabela [13, 5, 2, 6, 22, 24] jogos [13, 5, 2, 6, 23, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg19:331: Sportivo Barracas tabela [13, 5, 2, 6, 20, 23] jogos [11, 5, 1, 5, 18, 17] — a diferença vem de Vélez Sarsfield x Sportivo Barracas (1920-01-03), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg19:331: Estudiantil Porteño tabela [13, 4, 3, 6, 19, 21] jogos [11, 3, 3, 5, 13, 18] — a diferença vem de Sportivo Barracas x Estudiantil Porteño (1919-11-11), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg19:331: Tigre tabela [13, 4, 1, 8, 17, 23] jogos [12, 4, 0, 8, 16, 22] — a diferença vem de River Plate x Tigre (1919-10-26), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg19:331: San Isidro tabela [13, 2, 1, 10, 14, 27] jogos [13, 2, 1, 10, 14, 28] — a diferença vem de San Isidro x River Plate (1919-11-16), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- 3º pela lista oficial: River Plate (a tabela o punha em 4º)
- W.O./pontos para o mandante — Vélez Sarsfield Sportivo Barracas (1920-01-03): Sportivo Barracas not showed up
- anulado — River Plate 1-1 Tigre (1919-10-26): 1:1 annulled, replayed on Dec 7 at River Plate, Tigre as home
- anulado — River Plate 0-0 Independiente (1919-11-11): abandoned at 0:0 in 54m at River Plate, annulled, replayed on Nov 11 at Independiente
- anulado — Sportivo Barracas 0-4 Estudiantil Porteño (1919-11-11): abandoned at 0:0 in 45m HT at Barracas, annulled, replayed on Dec 14 at Estudiantil
- W.O./pontos para o visitante — Estudiantes de Buenos Aires Defensores de Belgrano (1919-11-16): Estudiantes not showed up
- W.O./pontos para o visitante — San Isidro River Plate (1919-11-16): not played, awarded on Dec 29
- anulado — River Plate 0-1 Gimnasia La Plata (1919-11-30): abandoned at 1:1 in 45m HT at River Plate, annulled, replayed on Nov 30 at Gimnasia
- anulado — Sportivo Barracas 2-2 Defensores de Belgrano (1919-11-30): abd at 0:0 in 45m HT, annulled, replayed on Dec 7, abandoned at 1:2 in 75m, remaining 15 on Jan 6
- anulado — Vélez Sarsfield 3-2 Estudiantil Porteño (1919-11-30): abandoned at 0:0 in 45m HT at Vélez, annulled, replayed on Nov 30 at Estudiantil

### 1920 Asociación

- W.O./pontos para o visitante — Nueva Chicago Porteño (1920-04-01): Nueva Chicago forfeited
- W.O./pontos para o visitante — Lanús Boca Juniors (1920-05-23)
- W.O./pontos para o visitante — Almagro Huracán (1920-06-27)
- W.O./pontos para o mandante — Del Plata Almagro (1920-06-27): Sportivo Almagro forfeited
- W.O./pontos para o mandante — Banfield Estudiantes (1920-07-04): Estudiantes LP forfeited
- W.O./pontos para o mandante — Huracán Porteño (1920-07-04): Porteño forfeited
- W.O./pontos para o visitante — Porteño Sportivo Barracas (1920-07-04): Porteño forfeited, it was played friendly (result: 1-2)
- W.O./pontos para o mandante — Nueva Chicago Banfield (1920-07-04)
- W.O./pontos para o mandante — Nueva Chicago Sportivo Palermo (1920-07-04)
- W.O./pontos para o mandante — Porteño Banfield (1920-07-04)
- W.O./pontos para o mandante — Colegiales Estudiantes (1920-07-04)
- W.O./pontos para o mandante — Colegiales Sportivo Barracas (1920-07-04)
- W.O./pontos para o visitante — Sportivo Palermo Sportivo Barracas (1920-07-04): The following matches were decided by point awarding after Lanús, Sportivo Almagro and
- W.O./pontos para o mandante — Banfield Palermo (1920-07-04)
- W.O./pontos para o mandante — Banfield Almagro (1920-07-04)
- W.O./pontos para o mandante — Boca Juniors Lanús (1920-07-04)
- W.O./pontos para o mandante — Boca Juniors Palermo (1920-07-04)
- W.O./pontos para o mandante — Boca Juniors Almagro (1920-07-04)
- W.O./pontos para o mandante — Del Plata Lanús (1920-07-04)
- W.O./pontos para o mandante — Huracán Almagro (1920-07-04)
- W.O./pontos para o visitante — Lanús Banfield (1920-07-04)
- W.O./pontos para o visitante — Lanús Estudiantes (1920-07-04)
- W.O./pontos para o visitante — Lanús Huracán (1920-07-04)
- W.O./pontos para o visitante — Lanús Nueva Chicago (1920-07-04)
- W.O./pontos para o visitante — Lanús Porteño (1920-07-04)
- W.O./pontos para o visitante — Lanús Sportivo Palermo (1920-07-04)
- W.O./pontos para o mandante — Nueva Chicago Almagro (1920-07-04)
- W.O./pontos para o visitante — Palermo Del Plata (1920-07-04)
- W.O./pontos para o visitante — Palermo Estudiantes (1920-07-04)
- W.O./pontos para o visitante — Palermo Huracán (1920-07-04)
- W.O./pontos para o visitante — Palermo Nueva Chicago (1920-07-04)
- W.O./pontos para o visitante — Palermo Porteño (1920-07-04)
- W.O./pontos para o visitante — Palermo Colegiales (1920-07-04)
- W.O./pontos para o mandante — Porteño Almagro (1920-07-04)
- W.O./pontos para o visitante — Almagro Del Plata (1920-07-04)
- W.O./pontos para o visitante — Almagro Estudiantes (1920-07-04)
- W.O./pontos para o visitante — Almagro Sportivo Palermo (1920-07-04)
- W.O./pontos para o mandante — Sportivo Barracas Lanús (1920-07-04)
- W.O./pontos para o mandante — Sportivo Barracas Almagro (1920-07-04)
- W.O./pontos para o mandante — Colegiales Lanús (1920-07-04)
- W.O./pontos para o mandante — Colegiales Almagro (1920-07-04)
- W.O./pontos para o mandante — Sportivo Palermo Palermo (1920-07-04)

### 1920 Amateurs

- W.O./pontos para o visitante — Tigre Lanús (s/d): Tigre forfeited
- W.O./pontos para o mandante — Atlanta Almagro (s/d)
- W.O./pontos para o mandante — Gimnasia La Plata Sportivo Buenos Aires (s/d)
- W.O./pontos para o mandante — Ferro Carril Oeste Platense (s/d)
- W.O./pontos para o mandante — Vélez Sarsfield Tigre (s/d): Tigre forfeited
- W.O./pontos para o visitante — San Isidro Defensores de Belgrano (s/d): San Isidro forfeited
- W.O./pontos para o visitante — Sportivo Buenos Aires Independiente (s/d): Sportivo Buenos Aires forfeited
- W.O./pontos para o visitante — Estudiantil Porteño Defensores de Belgrano (s/d)
- W.O./pontos para o mandante — Lanús Estudiantes de Buenos Aires (s/d)
- W.O./pontos para o mandante — Quilmes Sportivo Buenos Aires (s/d)
- W.O./pontos para o mandante — Almagro Platense (s/d)
- W.O./pontos para o mandante — Almagro Sportivo Buenos Aires (s/d)

### 1921 Asociación

- abandonado/suspenso, sem valer — Del Plata 0-0 Nueva Chicago (1921-04-03): Suspended in 30; played again on Sep 4
- anulado — Boca Juniors 1-1 Platense (1921-07-17): annulled
- W.O./pontos para o mandante — El Porvenir 0-0 Nueva Chicago (1921-08-07): at Everton (Gerli)][Suspended at 65'; El Porvenir won points
- anulado — Porteño 2-1 Platense (1921-08-21): annulled
- anulado — Platense 1-0 Colegiales (1921-09-04): at Urquiza][annulled
- anulado — Platense 0-2 Porteño (1921-11-06): at Porteño][annulled
- W.O./pontos para o mandante — Estudiantes Colegiales (1921-11-13): Sportivo del Norte withdrew
- anulado — Sportivo Palermo 4-0 Platense (1921-12-04): annulled
- W.O./pontos para o mandante — Nueva Chicago Colegiales (1921-12-04): Sportivo del Norte withdrew
- anulado — Sportivo Barracas 1-1 Platense (1921-12-11): annulled
- W.O./pontos para o mandante — Colegiales Porteño (1921-12-16): Porteño withdrew
- anulado — Huracán 4-0 Platense (1921-12-18): annulled
- W.O./pontos para o visitante — Porteño El Porvenir (1921-12-18)

### 1921 Amateurs

- tabela publicada x jogos — arg21:388: Independiente tabela [38, 22, 9, 7, 62, 28] jogos [39, 23, 9, 7, 65, 28] — a diferença vem de Independiente x Ferro Carril Oeste (1921-05-01), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg21:388: Atlanta tabela [38, 17, 7, 14, 47, 44] jogos [38, 17, 7, 14, 47, 43] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg21:388: Quilmes tabela [38, 8, 9, 21, 42, 65] jogos [39, 8, 9, 22, 42, 68] — a diferença vem de Independiente x Quilmes (1921-12-11), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg21:388: Ferro Carril Oeste tabela [38, 2, 7, 29, 22, 92] jogos [38, 2, 7, 29, 21, 92] — a diferença vem de Independiente x Ferro Carril Oeste (1921-05-01), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- abandonado/suspenso, sem valer — Almagro 0-0 Barracas Central (1921-04-03): Suspended at 7; played again on May 26
- abandonado/suspenso, sem valer — Gimnasia La Plata 0-0 Lanús (1921-04-03): Suspended at 20; played again on Jul 17
- abandonado/suspenso, sem valer — San Lorenzo 1-1 San Isidro (1921-04-03): Suspended at 25; played again on Jul 24
- anulado — Quilmes 3-2 General Mitre (1921-04-10): annulled
- anulado — Ferro Carril Oeste 0-0 General Mitre (1921-04-17): annulled
- anulado — Lanús 1-1 General Mitre (1921-04-24): annulled
- anulado — General Mitre 1-2 Atlanta (1921-05-01): at River Plate][annulled
- W.O./pontos para o mandante — Independiente Ferro Carril Oeste (1921-05-01): Ferro Carril Oeste withdrew
- anulado — Platense 0-3 General Mitre (1921-05-05): annulled
- anulado — Banfield 0-1 General Mitre (1921-05-08): annulled
- anulado — General Mitre 0-1 Barracas Central (1921-05-22): at Vélez Sarsfield][annulled
- anulado — General Mitre 0-1 Defensores de Belgrano (1921-05-29): at Palermo][annulled
- anulado — San Lorenzo 2-0 General Mitre (1921-06-05): annulled
- anulado — General Mitre 1-2 Independiente (1921-06-12): at San Lorenzo de Almagro][annulled
- anulado — Vélez Sarsfield 1-0 General Mitre (1921-06-19): annulled
- W.O./pontos para o mandante — Barracas Central Ferro Carril Oeste (1921-06-26): Ferro Carril Oeste withdrew
- anulado — Tigre 1-2 General Mitre (1921-06-29): annulled
- abandonado/suspenso, sem valer — Platense 2-2 Atlanta (1921-06-29): Suspended at 74; played again on Jan 6, 1922
- anulado — General Mitre 1-2 Sportivo Buenos Aires (1921-07-03): at Vélez Sarsfield][annulled
- anulado — Racing Club 3-0 General Mitre (1921-07-10): annulled
- anulado — General Mitre 0-2 River Plate (1921-07-24): annulled
- anulado — Estudiantes de Buenos Aires 2-1 General Mitre (1921-07-31): annulled
- anulado — Estudiantil Porteño 0-1 General Mitre (1921-08-07): annulled
- anulado — General Mitre 0-2 Estudiantes de Buenos Aires (1921-08-30): annulled
- abandonado/suspenso, sem valer — River Plate 0-1 Gimnasia La Plata (1921-10-02): Suspended at 28; played again on Jan 6, 1922
- W.O./pontos para o mandante — Defensores de Belgrano Estudiantil Porteño (1921-11-13): Estudiantil Porteño withdrew
- W.O./pontos para o mandante — San Lorenzo Ferro Carril Oeste (1921-11-13): Ferro Carril Oeste withdrew
- W.O./pontos para o mandante — Independiente Quilmes (1921-12-11): Quilmes withdrew
- W.O./pontos para o mandante — Barracas Central Banfield (1921-12-11): Banfield withdrew

### 1922 Asociación

- tabela publicada x jogos — arg22:36: Del Plata tabela [16, 10, 0, 6, 27, 15] jogos [16, 10, 0, 6, 26, 15] — a diferença vem de Del Plata x Progresista (1923-01-14), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg22:36: Progresista tabela [16, 2, 5, 9, 19, 32] jogos [16, 2, 5, 9, 19, 31] — a diferença vem de Del Plata x Progresista (1923-01-14), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- W.O./pontos para o mandante — Nueva Chicago Sportivo Barracas (1922-05-14): Sportivo Barracas withdrew
- W.O./pontos para o mandante — Colegiales Sportivo Barracas (1922-11-19)
- W.O./pontos para o mandante — Huracán 1-1 Alvear (1922-12-08): Suspended at 74; Huracán won points
- W.O./pontos para o mandante — Del Plata Progresista (1923-01-14): Suspended at 79; continued on Jan 14, 1923; Progresista withdrew

### 1922 Amateurs

- tabela publicada x jogos — arg22:404: River Plate tabela [40, 25, 11, 4, 58, 18] jogos [40, 26, 10, 4, 58, 17] — a diferença vem de River Plate x San Lorenzo (1923-03-25), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg22:404: San Lorenzo tabela [40, 24, 12, 4, 65, 25] jogos [40, 24, 11, 5, 64, 25] — a diferença vem de River Plate x San Lorenzo (1923-03-25), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg22:404: Racing Club tabela [40, 23, 11, 6, 65, 30] jogos [41, 23, 12, 6, 65, 30] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — arg22:404: Sportivo Buenos Aires tabela [40, 10, 10, 20, 42, 64] jogos [41, 10, 11, 20, 42, 64] — sobram 1 jogo(s) do clube na página
- W.O./pontos para o mandante — Barracas Central 1-1 Atlanta (1922-06-11): Suspended at 74; later Barracas Central won points
- abandonado/suspenso, sem valer — Estudiantes de Buenos Aires 1-1 Quilmes (1922-06-11): Suspended at 45; played again on Sep 24
- abandonado/suspenso, sem valer — San Lorenzo 0-1 Independiente (1922-06-18): Suspended in 73; played again on Sep 17
- abandonado/suspenso, sem valer — Estudiantes de Buenos Aires 0-0 Platense (1922-06-29): Suspended at 5; played again on Apr 22, 1923
- W.O./pontos para o mandante — Lanús Quilmes (1922-07-16): Quilmes withdrew
- W.O./pontos para o visitante — Quilmes Palermo (1922-07-23): Quilmes withdrew
- W.O./pontos para o visitante — Quilmes Sportivo Buenos Aires (1922-07-30): Quilmes withdrew
- W.O./pontos para o mandante — Atlanta 0-0 Palermo (1922-08-20): Suspended at 53; Atlanta won the points
- W.O./pontos para o mandante — Vélez Sarsfield Defensores de Belgrano (1922-10-29): Defensores de Belgrano withdrew
- W.O./pontos para o mandante — Tigre Quilmes (1922-11-19): Quilmes withdrew
- abandonado/suspenso, sem valer — River Plate 1-1 San Lorenzo (1923-03-25): Suspended at 75; played again on May 6
- abandonado/suspenso, sem valer — Estudiantil Porteño 0-0 River Plate (1923-04-01): Suspended at 45; played again on Apr 22
- abandonado/suspenso, sem valer — Ferro Carril Oeste 1-1 Sportivo Buenos Aires (1923-04-01): Suspended at 61; played again on Apr 29
- W.O./pontos para o mandante — Almagro Palermo (1923-05-10): Palermo withdrew
- W.O./pontos para o mandante — Gimnasia La Plata 0-0 San Isidro (1923-05-20): Finished at 37; Gimnasia y Esgrima LP won the points

### 1923 Asociación

- corrigido — Boca Juniors x Huracán (1924-03-16): desempate Boca x Huracán de 1924, sem título na página (AR-025)
- corrigido — Huracán x Boca Juniors (1924-03-30): desempate Boca x Huracán de 1924, sem título na página (AR-025)
- corrigido — Huracán x Boca Juniors (1924-04-06): desempate Boca x Huracán de 1924, sem título na página (AR-025)
- corrigido — Boca Juniors x Huracán (1924-04-27): desempate Boca x Huracán de 1924, sem título na página (AR-025)
- W.O./pontos para o visitante — Boca Alumni Sportivo Dock Sud (1923-06-03): Boca Alumni forfeited
- W.O./pontos para o visitante — Estudiantes General San Martín (1923-07-29): Estudiantes LP forfeited
- W.O./pontos para o mandante — Palermo Boca Alumni (1923-07-29): the match ended 1-1, but Palermo was awarded the points due to life-threatening
- W.O./pontos para o mandante — Sportivo Barracas Del Plata (1923-07-29): the match was suspended at 24' after Del Plata left the field when a penalty

### 1923 Amateurs

- tabela publicada x jogos — arghist-ama1920s:297: Tigre tabela [20, 7, 4, 9, 20, 24] jogos [20, 7, 4, 9, 20, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arghist-ama1920s:297: Lanús tabela [20, 2, 4, 14, 16, 34] jogos [20, 2, 4, 14, 17, 34] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- W.O./pontos para o mandante — Banfield Platense (s/d): Platense forfeited
- W.O./pontos para o mandante — Independiente Defensores de Belgrano (s/d): suspended at 1-1 in only 7f due to unruly behavior of players of away team
- W.O./pontos para o visitante — Independiente River Plate (s/d): abandoned at 0-0 in the second half as the referee was attacked by home player
- W.O./pontos para o mandante — Barracas Central Independiente (s/d): Independiente forfeited in protest for the lost points against River Plate
- W.O./pontos para o mandante — Ferro Carril Oeste Platense (s/d): played friendly (1-0) due to absence of referee, Platense later forfeited
- W.O./pontos para o mandante — Atlanta Barracas Central (s/d): suspended at 1-1, Atlanta was awarded the points
- W.O./pontos para o visitante — Gimnasia La Plata San Lorenzo (s/d): suspended at 2-1 in 70' due to crowd trouble, joined by local players
- W.O./pontos para o mandante — Platense Quilmes (s/d): Quilmes forfeited
- W.O./pontos para o mandante — Tigre Almagro (s/d): Sp. Almagro forfeited
- W.O./pontos para o mandante — Argentino del Sud Platense (s/d): Platense forfeited
- W.O./pontos para o mandante — Gimnasia La Plata Tigre (s/d): Tigre forfeited
- W.O./pontos para o mandante — Sportivo Buenos Aires Atlanta (s/d): Atlanta forfeited
- W.O./pontos para o mandante — Ferro Carril Oeste Argentino del Sud (s/d): Argentino del Sud forfeited

### 1924 Asociación

- tabela publicada x jogos — arg24:37: Sportivo Barracas tabela [21, 10, 5, 6, 31, 27] jogos [21, 10, 5, 6, 31, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg24:37: Progresista tabela [20, 3, 6, 11, 23, 35] jogos [20, 3, 6, 11, 21, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- W.O./pontos para o visitante — Universal Huracán (1924-05-18)
- W.O./pontos para o visitante — Argentinos Juniors Sportivo Barracas (1924-11-23): Argentinos Juniors withdrew
- W.O./pontos para o mandante — Nueva Chicago 0-0 Huracán (1924-12-21): Suspended at 30; Nueva Chicago won points
- W.O./pontos para o mandante — El Porvenir Universal (1924-12-28): Platense II withdrew

### 1924 Amateurs

- tabela publicada x jogos — arg24:577: Atlanta tabela [23, 7, 6, 10, 24, 28] jogos [23, 7, 6, 10, 23, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg24:577: Argentino del Sud tabela [23, 6, 2, 15, 25, 37] jogos [27, 8, 4, 15, 29, 40] — a diferença vem de Argentino del Sud x Ferro Carril Oeste (1925-02-15), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg24:577: Quilmes tabela [23, 3, 6, 14, 20, 40] jogos [27, 3, 8, 16, 22, 45] — sobram 4 jogo(s) do clube na página
- tabela publicada x jogos — arg24:577: Ferro Carril Oeste tabela [23, 4, 4, 15, 16, 43] jogos [27, 5, 6, 16, 19, 43] — a diferença vem de Argentino del Sud x Ferro Carril Oeste (1925-02-15), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- W.O./pontos para o mandante — Independiente 1-1 Argentino del Sud (1924-05-04): Suspended at 74; Independiente won points
- W.O./pontos para o visitante — Argentino del Sud 1-1 Estudiantil Porteño (1924-06-22): Suspended at 70; Estudiantil Porteño won points; Argentino del Sud deducted 2 points
- W.O./pontos para o mandante — Banfield Argentino del Sud (1924-10-19): Argentino del Sud withdrew
- W.O./pontos para o mandante — Argentino del Sud Ferro Carril Oeste (1925-02-15)

### 1925 Asociación

- tabela publicada x jogos — arg25:24: Sportivo Barracas tabela [21, 8, 5, 8, 22, 26] jogos [22, 8, 6, 8, 22, 26] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — arg25:24: Boca Alumni tabela [21, 5, 6, 10, 13, 27] jogos [22, 5, 7, 10, 13, 27] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — arghist-ama1920s:444: El Porvenir tabela [21, 14, 4, 3, 30, 15] jogos [21, 14, 4, 3, 31, 15] — a diferença vem de El Porvenir x Sportivo Barracas (1925-10-11), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arghist-ama1920s:444: Chacarita Juniors tabela [21, 12, 4, 5, 42, 19] jogos [21, 12, 4, 5, 42, 18] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arghist-ama1920s:444: Sportivo Barracas tabela [22, 8, 6, 8, 22, 24] jogos [22, 8, 6, 8, 22, 26] — a diferença vem de El Porvenir x Sportivo Barracas (1925-10-11), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- W.O./pontos para o mandante — Boca Alumni All Boys (1925-05-03): All Boys withdrew
- W.O./pontos para o mandante — Temperley Boca Alumni (1925-06-14): Boca Alumni withdrew
- W.O./pontos para o mandante — Progresista All Boys (1925-07-05)
- W.O./pontos para o visitante — Universal Temperley (1925-08-09): Universal withdrew
- anulado — Argentino de Quilmes 3-1 Chacarita Juniors (1925-08-30): annulled; played again on Oct 4
- W.O./pontos para o mandante — El Porvenir 2-0 Sportivo Barracas (1925-10-11): Suspended at 35; El Porvenir won points
- W.O./pontos para o visitante — All Boys Sportivo Dock Sud (1925-11-08)
- W.O./pontos para o mandante — Alvear Universal (1925-12-27)
- W.O./pontos para o mandante — Argentino de Lomas Argentino de Quilmes (1925-12-27)
- W.O./pontos para o visitante — Boca Alumni El Porvenir (1925-12-27)
- W.O./pontos para o visitante — All Boys El Porvenir (1926-01-03): Suspended at 55; continued on Jan 3, 1926
- W.O./pontos para o mandante — General San Martín Argentinos Juniors (1926-01-10): Argentinos Juniors withdrew
- W.O./pontos para o visitante — Argentinos Juniors Universal (1926-01-10): Argentinos Juniors withdrew
- W.O./pontos para o visitante — Argentinos Juniors El Porvenir (1926-01-10)
- W.O./pontos para o mandante — Sportivo Barracas All Boys (1926-01-10)

### 1925 Amateurs

- W.O./pontos para o visitante — Independiente 1-1 Vélez Sarsfield (1925-10-25): Suspended at 78; Vélez Sarsfield won points
- W.O./pontos para o visitante — Sportivo Buenos Aires San Isidro (1925-10-25): Sportivo Buenos Aires withdrew
- W.O./pontos para o visitante — Argentino del Sud Almagro (1925-10-25): Argentino del Sud withdrew
- W.O./pontos para o mandante — Lanús 1-2 Gimnasia La Plata (1925-06-21): Later Lanús won points
- W.O./pontos para o mandante — Banfield Atlanta (1925-12-08): Atlanta withdrew
- W.O./pontos para o mandante — Barracas Central San Isidro (1925-12-08): San Isidro withdrew
- W.O./pontos para o mandante — Gimnasia La Plata Tigre (1925-12-08): Tigre withdrew
- abandonado/suspenso, sem valer — Estudiantil Porteño 0-0 Sportivo Buenos Aires (1925-08-16): Suspended at 65; played again on Nov 22
- W.O./pontos para o visitante — San Isidro Independiente (1925-09-13): San Isidro withdrew
- W.O./pontos para o visitante — Sportivo Buenos Aires Barracas Central (1925-09-20): Sportivo Buenos Aires withdrew

### 1926 Asociación

- tabela publicada x jogos — arg26:45: Argentinos Juniors tabela [17, 12, 4, 1, 27, 11] jogos [17, 12, 4, 1, 26, 11] — a diferença vem de Argentinos Juniors x Alvear (1927-01-16), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg26:45: Sportsman tabela [17, 6, 4, 7, 17, 22] jogos [18, 7, 4, 7, 17, 22] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — arg26:45: Alvear tabela [17, 5, 5, 7, 13, 21] jogos [17, 5, 5, 7, 13, 20] — a diferença vem de Argentinos Juniors x Alvear (1927-01-16), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arghist-ama1920s:570: Huracán tabela [17, 11, 2, 4, 37, 8] jogos [17, 11, 2, 4, 39, 8] — a diferença vem de Huracán x General San Martín (1927-12-26), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arghist-ama1920s:570: Sportsman tabela [17, 5, 5, 7, 17, 22] jogos [17, 6, 4, 7, 17, 22] — a diferença vem de General San Martín x Sportsman (1926-05-16), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arghist-ama1920s:570: General San Martín tabela [17, 5, 3, 9, 15, 24] jogos [17, 5, 2, 10, 15, 24] — a diferença vem de General San Martín x Sportsman (1926-05-16), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arghist-ama1920s:570: Sportivo Dock Sud tabela [17, 5, 2, 10, 22, 21] jogos [17, 5, 2, 10, 22, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- anulado — Universal 2-3 El Porvenir (1926-04-18): annulled
- anulado — Sportivo Barracas 0-1 Nueva Chicago (1926-04-18): annulled
- anulado — Alvear 0-1 All Boys (1926-04-18): annulled
- anulado — San Fernando 1-1 Temperley (1926-04-18): annulled
- anulado — Colegiales 6-2 Boca Alumni (1926-04-18): annulled
- anulado — All Boys 3-1 Universal (1926-04-25): annulled
- anulado — El Porvenir 2-0 Sportivo Balcarce (1926-04-25): annulled
- anulado — Palermo 2-0 Temperley (1926-04-25): annulled
- anulado — Nueva Chicago 1-0 San Fernando (1926-04-25): annulled
- anulado — Alvear 0-1 Colegiales (1926-04-25): annulled
- W.O./pontos para o visitante — Sportivo Barracas Sportsman (1926-04-25): annulled
- anulado — Colegiales 5-1 Huracán (1926-05-02): annulled
- anulado — Argentino de Lomas 2-2 Sportivo Barracas (1926-05-02): Suspended at 83; not continued][annulled
- anulado — All Boys 0-0 Chacarita Juniors (1926-05-02): at Chacarita Juniors][annulled
- anulado — Alvear 0-0 El Porvenir (1926-05-02): annulled
- anulado — Progresista 2-3 Colegiales (1926-05-09): annulled
- anulado — Alvear 0-1 Temperley (1926-05-09): annulled
- anulado — Del Plata 2-5 Sportivo Barracas (1926-05-09): annulled
- anulado — El Porvenir 0-5 Boca Juniors (1926-05-09): at Boca Juniors][annulled
- anulado — Argentino de Lomas 0-2 Nueva Chicago (1926-05-09): annulled
- anulado — Argentinos Juniors 3-0 All Boys (1926-05-09): annulled
- anulado — Nueva Chicago 1-0 Progresista (1926-05-16): annulled
- anulado — Sportivo Barracas 3-0 San Fernando (1926-05-16): annulled
- anulado — Del Plata 0-1 El Porvenir (1926-05-16): annulled
- anulado — Temperley 2-0 All Boys (1926-05-16): Suspended at 80; not continued][annulled
- W.O./pontos para o visitante — General San Martín 2-2 Sportsman (1926-05-16): on Aug 19, Sportsman won points
- W.O./pontos para o mandante — Universal Sportivo Dock Sud (1926-08-29): Sportivo Dock Sud withdrew
- anulado — Sportivo Barracas 2-1 Huracán (1926-05-30): annulled
- anulado — Sportivo Dock Sud 3-3 Colegiales (1926-05-30): at Colegiales][annulled
- anulado — Temperley 1-1 Chacarita Juniors (1926-05-30): annulled
- anulado — El Porvenir 1-1 Nueva Chicago (1926-05-30): annulled
- anulado — San Fernando 3-1 All Boys (1926-05-30): annulled
- anulado — Colegiales 2-2 Sportivo Barracas (1926-06-06): annulled
- anulado — Nueva Chicago 1-1 Alvear (1926-06-06): annulled
- anulado — General San Martín 1-1 Temperley (1926-06-06): annulled
- anulado — Boca Juniors 0-0 Colegiales (1926-06-13): annulled
- anulado — Sportsman 2-3 El Porvenir (1926-06-13): at El Porvenir][annulled
- anulado — Sportivo Barracas 4-0 Alvear (1926-06-13): annulled
- anulado — Boca Alumni 0-2 Temperley (1926-06-13): at Colegiales][annulled
- anulado — Nueva Chicago 1-0 All Boys (1926-06-13): Suspended at 58; not continued] [annulled
- anulado — Colegiales 2-2 Palermo (1926-06-20): annulled
- anulado — Sportivo Dock Sud 0-2 Sportivo Barracas (1926-06-20): at Sportivo Barracas][annulled
- anulado — Del Plata 1-2 Nueva Chicago (1926-06-20): annulled
- anulado — All Boys 3-2 Argentino de Quilmes (1926-06-20): annulled
- anulado — Boca Alumni 1-1 El Porvenir (1926-06-20): at Progresista][annulled
- anulado — Porteño 2-4 Temperley (1926-06-20): annulled
- W.O./pontos para o visitante — Progresista General San Martín (1926-06-20): Progresista withdrew
- anulado — Sportsman 0-0 Colegiales (1926-07-18): at Del Plata][annulled
- anulado — Palermo 1-2 Nueva Chicago (1926-07-18): annulled
- anulado — All Boys 2-1 Argentino de Lomas (1926-07-18): annulled
- anulado — Colegiales 2-1 San Fernando (1926-07-25): annulled
- anulado — Nueva Chicago 2-1 Argentino de Quilmes (1926-07-25): Finished at 72][annulled
- anulado — Porteño 1-4 Sportivo Barracas (1926-07-25): annulled
- anulado — Temperley 0-0 Sportivo Dock Sud (1926-07-25): annulled
- anulado — General San Martín 0-2 El Porvenir (1926-07-25): annulled
- W.O./pontos para o mandante — Sportivo Balcarce Progresista (1926-07-25)
- W.O./pontos para o mandante — Argentinos Juniors Alvear (1927-01-16): Suspended at 45'; continued on Jan 16, 1927; Alvear withdrew
- anulado — Universal 2-1 Nueva Chicago (1927-08-01): at Argentinos Juniors][annulled
- anulado — Chacarita Juniors 3-1 El Porvenir (1927-08-01): annulled
- anulado — Del Plata 1-3 Temperley (1927-08-01): annulled
- anulado — Sportivo Barracas 0-3 All Boys (1927-08-01): at Huracán][annulled
- W.O./pontos para o visitante — Progresista Huracán (1927-08-01)
- anulado — Boca Juniors 4-0 Sportivo Barracas (1927-08-08): annulled
- anulado — Colegiales 3-1 Universal (1927-08-08): annulled
- anulado — Sportivo Balcarce 1-1 Nueva Chicago (1927-08-08): annulled
- anulado — Temperley 2-1 Argentino de Lomas (1927-08-08): annulled
- anulado — El Porvenir 4-1 All Boys (1927-08-08): annulled
- anulado — Temperley 1-3 Boca Juniors (1927-08-22): annulled
- anulado — Chacarita Juniors 1-0 Colegiales (1927-08-22): annulled
- anulado — Argentino de Quilmes 2-4 Sportivo Barracas (1927-08-22): annulled
- anulado — All Boys 0-0 Sportivo Dock Sud (1927-08-22): annulled
- anulado — Colegiales 7-3 All Boys (1927-04-11): annulled
- anulado — Temperley 2-1 Universal (1927-09-05): annulled
- W.O./pontos para o mandante — Universal Del Plata (1927-11-21): Del Plata withdrew
- W.O./pontos para o mandante — Alvear Progresista (1927-11-28): Progresista withdrew
- W.O./pontos para o visitante — Sportivo Dock Sud Alvear (1927-12-08): Sportivo Dock Sud withdrew
- W.O./pontos para o visitante — Chacarita Juniors Argentino de Quilmes (1927-12-08): Chacarita Juniors withdrew
- W.O./pontos para o visitante — Argentino de Quilmes Alvear (1927-12-12): Argentino de Quilmes withdrew
- W.O./pontos para o mandante — Argentinos Juniors Progresista (1927-12-19): Progresista withdrew
- W.O./pontos para o mandante — Palermo General San Martín (1927-12-19): General San Martín withdrew
- W.O./pontos para o mandante — Argentinos Juniors Boca Alumni (1927-12-26): Boca Alumni withdrew
- W.O./pontos para o mandante — Palermo Sportivo Dock Sud (1927-12-26): Sportivo Dock Sud withdrew
- W.O./pontos para o visitante — Huracán General San Martín (1927-12-26): Huracán withdrew
- W.O./pontos para o mandante — Argentinos Juniors Huracán (1927-01-09): Huracán withdrew
- W.O./pontos para o visitante — Chacarita Juniors Alvear (1927-01-09): Chacarita Juniors withdrew
- W.O./pontos para o mandante — Palermo Boca Alumni (1927-01-16): Boca Alumni withdrew
- W.O./pontos para o mandante — Palermo Progresista (1927-01-16)
- W.O./pontos para o mandante — San Fernando Progresista (1927-01-16)
- W.O./pontos para o mandante — Universal Progresista (1927-01-16)
- W.O./pontos para o visitante — Chacarita Juniors Sportivo Balcarce (1927-01-16)
- W.O./pontos para o mandante — Sportsman Huracán (1927-01-16)

### 1926 Amateurs

- a página arg26 põe cada linha num <PRE> próprio, sem quebra: o texto puro juntava os jogos e só 43 dos 325 eram lidos; com a quebra por <PRE> (ler_rsssf.PRE_POR_LINHA) entram todos (AR-006, AR-034)
- tabela publicada x jogos — arghist-ama1920s:615: Racing Club tabela [25, 16, 2, 7, 51, 36] jogos [25, 16, 2, 7, 55, 38] — a outra tabela publicada (arg26) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arghist-ama1920s:615: Tigre tabela [25, 7, 8, 10, 32, 36] jogos [25, 7, 8, 10, 34, 40] — a outra tabela publicada (arg26) fecha com os jogos: o erro é desta tabela
- W.O./pontos para o mandante — Lanús Liberal Argentino (1926-12-26): Liberal Argentino withdrew
- W.O./pontos para o mandante — Estudiantes de Buenos Aires San Isidro (1927-01-23): San Isidro withdrew
- W.O./pontos para o visitante — Atlanta Excursionistas (1927-07-11): Atlanta withdrew
- W.O./pontos para o mandante — Gimnasia La Plata River Plate (1927-12-08): River Plate withdrew
- W.O./pontos para o mandante — Talleres de Remedios de Escalada 1-0 Tigre (1927-07-25): Suspended at 20; not continued, Talleres RE won points
- W.O./pontos para o visitante — Atlanta 0-0 Banfield (1927-07-25): Suspended at 45; not continued, Banfield won points
- W.O./pontos para o mandante — Barracas Central Platense (1927-01-02): Suspended at 35; continued on Jan 2, 1927; Platense withdrew
- W.O./pontos para o mandante — Estudiantil Porteño Estudiantes (1927-09-05): Estudiantes LP withdrew
- W.O./pontos para o visitante — San Isidro Gimnasia La Plata (1927-12-26): San Isidro withdrew
- W.O./pontos para o mandante — Banfield Estudiantil Porteño (1927-12-26): Estudiantil Porteño withdrew
- W.O./pontos para o mandante — Platense Quilmes (1927-10-24): Quilmes withdrew
- W.O./pontos para o visitante — River Plate Sportivo Buenos Aires (1927-12-08): River Plate withdrew
- W.O./pontos para o mandante — Sportivo Buenos Aires Tigre (1927-10-31): Tigre withdrew
- W.O./pontos para o mandante — Almagro Banfield (1927-10-31): Banfield withdrew
- W.O./pontos para o visitante — San Isidro Ferro Carril Oeste (1927-10-31): San Isidro withdrew
- W.O./pontos para o mandante — Defensores de Belgrano Estudiantes (1927-11-21): Estudiantes LP withdrew
- W.O./pontos para o mandante — Lanús Estudiantil Porteño (1927-11-21): Estudiantil Porteño withdrew

### 1927

- tabela publicada x jogos — arg27:33: Estudiantil Porteño tabela [33, 9, 5, 19, 43, 62] jogos [34, 9, 6, 19, 44, 63] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — arg27:33: Excursionistas tabela [33, 8, 6, 19, 41, 72] jogos [34, 8, 7, 19, 42, 73] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — arghist-ama1920s:661: Banfield tabela [33, 13, 6, 14, 45, 47] jogos [33, 13, 6, 14, 45, 49] — a diferença vem de Banfield x Talleres de Remedios de Escalada (1927-03-20), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arghist-ama1920s:661: Talleres de Remedios de Escalada tabela [33, 10, 9, 14, 30, 38] jogos [33, 10, 9, 14, 32, 38] — a diferença vem de Banfield x Talleres de Remedios de Escalada (1927-03-20), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arghist-ama1920s:661: Estudiantil Porteño tabela [33, 9, 5, 19, 43, 62] jogos [34, 9, 6, 19, 44, 63] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — arghist-ama1920s:661: Excursionistas tabela [33, 8, 6, 19, 40, 69] jogos [34, 8, 7, 19, 42, 73] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — arghist-ama1920s:661: Atlanta tabela [33, 8, 6, 19, 28, 50] jogos [33, 8, 6, 19, 31, 51] — a diferença vem de Banfield x Atlanta (1927-09-18), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- W.O./pontos para o mandante — Banfield 0-2 Talleres de Remedios de Escalada (1927-03-20): Banfield won points
- W.O./pontos para o mandante — Vélez Sarsfield Almagro (1927-05-01): Almagro withdrew
- W.O./pontos para o mandante — Lanús 0-0 Ferro Carril Oeste (1927-05-29): Suspended at 86; Lanús won points
- W.O./pontos para o mandante — Tigre River Plate (1927-08-21): River Plate withdrew
- W.O./pontos para o mandante — Banfield Atlanta (1927-09-18): Atlanta withdrew
- W.O./pontos para o mandante — Estudiantil Porteño Porteño (1927-12-08): Porteño withdrew
- W.O./pontos para o mandante — Talleres de Remedios de Escalada Argentino de Quilmes (1927-12-08): Argentina de Quilmes withdrew
- W.O./pontos para o mandante — Lanús Almagro (1927-10-16): Almagro withdrew
- W.O./pontos para o mandante — Barracas Central Almagro (1927-12-11): Almagro withdrew
- W.O./pontos para o visitante — Atlanta Lanús (1927-12-11): Atlanta withdrew
- W.O./pontos para o mandante — Sportivo Barracas Porteño (1927-12-11): Porteño withdrew
- W.O./pontos para o mandante — Talleres de Remedios de Escalada Atlanta (1927-11-27): Atlanta withdrew
- W.O./pontos para o visitante — Almagro Estudiantil Porteño (1927-11-27): Almagro withdrew
- W.O./pontos para o mandante — San Lorenzo Porteño (1927-11-27): Porteño withdrew
- W.O./pontos para o visitante — Atlanta Argentinos Juniors (1927-12-04): Atlanta withdrew

### 1928

- tabela publicada x jogos — arg28:46: Almagro tabela [35, 12, 10, 13, 44, 53] jogos [34, 12, 10, 12, 44, 53] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — arg28:46: Argentino del Sud tabela [35, 9, 7, 19, 34, 59] jogos [34, 9, 7, 18, 34, 59] — faltam 1 jogo(s) do clube na página
- abandonado/suspenso, sem valer — Excursionistas 0-0 Almagro (1928-11-11): Suspended; played again on Mar 31, 1929
- W.O./pontos para o mandante — Gimnasia La Plata Lanús (1928-12-09): Lanús withdrew
- abandonado/suspenso, sem valer — Barracas Central 0-0 Talleres de Remedios de Escalada (1928-12-30): Suspended; played again on Mar 24, 1929
- W.O./pontos para o mandante — Tigre 1-1 San Lorenzo (1929-06-23): Suspended at 43; not continued, Tigre won points

### 1929

- classificação com os números das tabelas dos grupos (com os pontos dados por W.O.: Tigre x Lanús, Defensores x Barracas Central, Quilmes x Sportivo Barracas) mais os desempates, o 3º lugar e a final (AR-020)
- tabela publicada x jogos — arg29:16: Lanús tabela [17, 8, 8, 1, 31, 17] jogos [16, 7, 8, 1, 31, 16] — a diferença vem de Tigre x Lanús (1929-12-29), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg29:16: San Fernando tabela [17, 6, 5, 6, 31, 20] jogos [16, 6, 5, 5, 31, 20] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — arg29:16: El Porvenir tabela [17, 7, 3, 7, 19, 26] jogos [16, 6, 3, 7, 19, 26] — a diferença vem de Estudiantes x El Porvenir (1929-09-15), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg29:16: Estudiantes tabela [17, 7, 2, 8, 32, 20] jogos [15, 7, 2, 6, 32, 20] — a diferença vem de Estudiantes x El Porvenir (1929-09-15), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg29:16: Tigre tabela [17, 5, 5, 7, 28, 23] jogos [16, 5, 5, 6, 27, 23] — a diferença vem de Tigre x Lanús (1929-12-29), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg29:16: Banfield tabela [17, 5, 4, 8, 18, 23] jogos [16, 5, 4, 7, 18, 23] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — arg29:16: San Isidro tabela [17, 3, 3, 11, 14, 36] jogos [16, 3, 3, 10, 14, 36] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — arg29:43: Barracas Central tabela [16, 7, 1, 8, 16, 30] jogos [15, 6, 1, 8, 15, 29] — a diferença vem de Defensores de Belgrano x Barracas Central (1929-08-25), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg29:43: Defensores de Belgrano tabela [16, 4, 4, 8, 12, 18] jogos [15, 4, 4, 7, 11, 17] — a diferença vem de Excursionistas x Defensores de Belgrano (1929-12-29), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg29:43: Excursionistas tabela [16, 5, 2, 9, 20, 33] jogos [15, 5, 2, 8, 20, 33] — a diferença vem de Excursionistas x Defensores de Belgrano (1929-12-29), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg29:43: Ferro Carril Oeste tabela [16, 2, 6, 8, 23, 25] jogos [15, 2, 6, 7, 23, 25] — faltam 1 jogo(s) do clube na página
- 3º pela lista oficial: River Plate (a tabela o punha em 4º)
- W.O./pontos para o visitante — Huracán Racing Club (1929-12-22): Huracán withdrew
- W.O./pontos para o visitante — Platense Almagro (1929-12-22): Platense withdrew
- decidido fora de campo — Estudiantes El Porvenir (1929-09-15): abandoned at 0-0 in 75', Estudiantes LP lost points
- W.O./pontos para o visitante — Estudiantes Gimnasia La Plata (1929-12-29): Estudiantes LP withdrew
- W.O./pontos para o mandante — Banfield Huracán (1929-12-22): Huracán withdrew
- W.O./pontos para o mandante — Estudiantes de Buenos Aires Huracán (1929-12-22): Huracán withdrew
- W.O./pontos para o mandante — Atlanta Platense (1929-12-22): Platense forfeited
- W.O./pontos para o mandante — River Plate Huracán (1929-12-22): Huracán forfeited
- W.O./pontos para o visitante — Huracán Almagro (1929-12-15): Huracán forfeited
- W.O./pontos para o visitante — Platense Colegiales (1929-12-15): Platense forfeited
- W.O./pontos para o visitante — Huracán Argentino del Sud (1929-12-22): Huracán withdrew
- W.O./pontos para o mandante — San Isidro Platense (1929-12-22): Platense withdrew
- W.O./pontos para o mandante — El Porvenir Atlanta (1929-12-29): Atlanta forfeited
- W.O./pontos para o mandante — Racing Club Estudiantes (1929-12-29): Estudiantes forfeited
- W.O./pontos para o mandante — Talleres de Remedios de Escalada San Fernando (1929-12-29): San Fernando withdrew
- decidido fora de campo — Tigre Lanús (1929-12-29): abandoned at 1-0 in 54'; Tigre lost points
- W.O./pontos para o mandante — El Porvenir Huracán (1929-12-22): Huracán withdrew
- W.O./pontos para o mandante — River Plate Platense (1929-12-22): Platense withdrew
- W.O./pontos para o visitante — Atlanta Banfield (1929-12-29): Atlanta withdrew
- W.O./pontos para o mandante — Almagro San Isidro (1930-01-05): San Isidro forfeited
- W.O./pontos para o visitante — Huracán San Fernando (1929-12-22): Huracán withdrew
- W.O./pontos para o visitante — Platense Argentino del Sud (1929-12-22): Platense wihtdrew
- W.O./pontos para o mandante — Talleres de Remedios de Escalada Estudiantes (1929-12-29): Estudiantes LP withdrew
- W.O./pontos para o mandante — Tigre Atlanta (1929-12-29): Atlanta withdrew
- W.O./pontos para o mandante — Vélez Sarsfield Sportivo Barracas (1930-01-03): Sportivo Barracas was suspended
- W.O./pontos para o mandante — Sportivo Palermo Sportivo Buenos Aires (1929-12-22): Sportivo Buenos Aires withdrew
- W.O./pontos para o visitante — Excursionistas Defensores de Belgrano (1929-12-29): Excursionistas withdrew
- W.O./pontos para o mandante — Chacarita Juniors Argentino de Lomas (1930-01-19): Argentino de Banfield forfeited
- decidido fora de campo — Defensores de Belgrano Barracas Central (1929-08-25): abandoned at 1-1 in 70'; Defensores de Belgrano lost points
- W.O./pontos para o visitante — Sportivo Barracas Chacarita Juniors (1930-01-03): Sportivo Barracas was suspended
- W.O./pontos para o visitante — Sportivo Palermo Quilmes (1929-12-01): Sportivo Palermo forfeited
- W.O./pontos para o mandante — Barracas Central Argentino de Quilmes (1929-12-22): Argentino de Quilmes forfeited
- W.O./pontos para o mandante — Quilmes Sportivo Buenos Aires (1929-12-22): Sportivo Buenos Aires forfeited
- W.O./pontos para o visitante — Sportivo Barracas Quilmes (1929-12-15): Sportivo Barracas forfeited
- W.O./pontos para o mandante — Chacarita Juniors Argentino de Quilmes (1929-12-22): Argentino de Quilmes withdrew
- W.O./pontos para o visitante — Sportivo Buenos Aires Argentinos Juniors (1929-12-22): Sportivo Buenos Aires withdrew
- W.O./pontos para o mandante — Estudiantil Porteño Excursionistas (1929-12-29): Excursionistas forfeited
- W.O./pontos para o mandante — Sportivo Palermo Ferro Carril Oeste (1929-12-29): Ferro Carril Oeste forfeited
- W.O./pontos para o mandante — Vélez Sarsfield Argentino de Quilmes (1929-12-22): Argentino de Quilmes withdrew
- W.O./pontos para o mandante — Argentino de Lomas Sportivo Barracas (1930-01-03): Sportivo Barracas was suspended
- W.O./pontos para o visitante — Defensores de Belgrano Estudiantil Porteño (1930-01-05): Defensores de Belgrano forfeited
- W.O./pontos para o visitante — Quilmes Chacarita Juniors (1930-01-05): Quilmes forfeited
- W.O./pontos para o mandante — Excursionistas Argentino de Quilmes (1929-12-22): Argentino de Quilmes withdrew
- W.O./pontos para o visitante — Sportivo Buenos Aires Barracas Central (1929-12-22): Sportivo Buenos Aires withdrew
- W.O./pontos para o mandante — Quilmes Ferro Carril Oeste (1929-12-29): Ferro Carril Oeste withdrew
- W.O./pontos para o visitante — Sportivo Barracas Boca Juniors (1930-01-03): Sportivo Barracas was suspended
- W.O./pontos para o mandante — Sportivo Palermo Defensores de Belgrano (1930-01-05): Defensores de Belgrano withdrew
- W.O./pontos para o mandante — River Plate San Lorenzo (1930-02-09): at Racing Club San Lorenzo de Almagro forfeited

### 1930

- tabela publicada x jogos — arg30:28: Sportivo Buenos Aires tabela [35, 18, 5, 12, 58, 44] jogos [35, 17, 6, 12, 58, 44] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg30:28: Argentino del Sud tabela [35, 1, 2, 32, 14, 100] jogos [35, 1, 3, 31, 14, 100] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arghist-ama1920s:867: Chacarita Juniors tabela [35, 18, 6, 11, 57, 43] jogos [35, 18, 6, 11, 58, 44] — a diferença vem de Sportivo Palermo x Chacarita Juniors (1930-06-08), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arghist-ama1920s:867: Sportivo Buenos Aires tabela [35, 18, 5, 12, 57, 44] jogos [35, 17, 6, 12, 58, 44] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arghist-ama1920s:867: Huracán tabela [35, 16, 7, 12, 75, 49] jogos [35, 16, 7, 12, 78, 52] — a diferença vem de Huracán x San Fernando (1931-01-03), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arghist-ama1920s:867: Ferro Carril Oeste tabela [35, 13, 8, 14, 45, 55] jogos [35, 13, 8, 14, 46, 56] — a diferença vem de Excursionistas x Ferro Carril Oeste (1930-11-09), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arghist-ama1920s:867: San Fernando tabela [35, 13, 7, 15, 47, 63] jogos [35, 13, 7, 15, 50, 67] — a diferença vem de Huracán x San Fernando (1931-01-03), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arghist-ama1920s:867: Excursionistas tabela [35, 11, 6, 18, 32, 56] jogos [35, 11, 6, 18, 33, 58] — a diferença vem de Excursionistas x Ferro Carril Oeste (1930-11-09), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arghist-ama1920s:867: Sportivo Palermo tabela [35, 7, 11, 17, 46, 65] jogos [35, 7, 11, 17, 47, 66] — a diferença vem de Sportivo Palermo x Chacarita Juniors (1930-06-08), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arghist-ama1920s:867: San Isidro tabela [35, 6, 11, 18, 29, 66] jogos [35, 6, 11, 18, 30, 66] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arghist-ama1920s:867: Argentino del Sud tabela [35, 1, 2, 32, 14, 100] jogos [35, 1, 3, 31, 14, 100] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- W.O./pontos para o visitante — Sportivo Palermo 1-1 Chacarita Juniors (1930-06-08): Suspended at 44; not continued, Chacarita Juniors won points
- W.O./pontos para o mandante — Excursionistas 1-1 Ferro Carril Oeste (1930-11-09): Suspended at 50; not continued, Excursionistas won points
- W.O./pontos para o visitante — Racing Club Talleres de Remedios de Escalada (1930-11-30): Racing Club withdrew
- abandonado/suspenso, sem valer — Quilmes 0-0 Defensores de Belgrano (1930-12-14): Suspended at 42; played again on Dec 28
- abandonado/suspenso, sem valer — Argentinos Juniors 1-1 Chacarita Juniors (1930-12-14): Suspended at 45; played again on Dec 28
- abandonado/suspenso, sem valer — El Porvenir 2-2 San Lorenzo (1930-12-14): Suspended at 55; played again on Dec 28
- W.O./pontos para o mandante — Huracán 3-3 San Fernando (1931-01-03): Suspended at 60; not continued, Huracán won points
- W.O./pontos para o mandante — Sportivo Barracas Argentino del Sud (1931-03-29): Argentino del Sud withdrew
- W.O./pontos para o mandante — Ferro Carril Oeste Honor y Patria (1931-04-12): Honor y Patria withdrew
- W.O./pontos para o mandante — San Fernando Racing Club (1931-04-12): Racing Club withdrew
- W.O./pontos para o visitante — Argentino del Sud Estudiantes de Buenos Aires (1931-04-12): Argentino del Sud withdrew
- W.O./pontos para o mandante — Almagro Gimnasia La Plata (1931-04-12): Gimnasia y Esgrima LP withdrew

### 1931 Liga

- tabela publicada x jogos — arg31:19: Platense tabela [34, 13, 3, 18, 52, 52] jogos [33, 13, 3, 17, 52, 52] — a diferença vem de Lanús x Platense (1931-10-25), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg31:19: Lanús tabela [34, 10, 2, 22, 43, 82] jogos [33, 9, 2, 22, 43, 82] — a diferença vem de Lanús x Platense (1931-10-25), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- abandonado/suspenso, sem valer — Racing Club Estudiantes (1931-08-02): abandoned at 1:1 in 75
- W.O./pontos para o visitante — Racing Club Estudiantes (1931-11-04): awarded lp:wp; jogo repetido (o primeiro foi suspenso)
- abandonado/suspenso, sem valer — Boca Juniors River Plate (1931-09-20): abandoned at 1:1 in 26
- W.O./pontos para o mandante — Boca Juniors River Plate (1931-10-14): awarded wp:lp; jogo repetido (o primeiro foi suspenso)
- abandonado/suspenso, sem valer — Lanús Ferro Carril Oeste (1931-10-11): abandoned at 2:3 in 88
- abandonado/suspenso, sem valer — Lanús Platense (1931-10-25): abandoned at 1:1 in 49
- não jogado — Lanús Platense (1932-01-07): Platense withdrew; jogo repetido (o primeiro foi suspenso)
- não jogado — Tigre Platense (1932-01-06): Platense withdrew
- W.O./pontos para o mandante — Tigre Platense (1932-01-13): awarded wp:lp

### 1931 Asociación

- o campeonato da Asociación Amateurs, começado antes da saída dos clubes profissionais, foi anulado e recomeçado
- não jogado — San Isidro Almagro (1931-06-28): 1:3, annulled
- não jogado — Sportivo Barracas San Isidro (1931-07-05): 2:0, annulled
- não jogado — Estudiantil Porteño San Isidro (1931-07-12): 1:1, annulled
- W.O./pontos para o mandante — Sportivo Buenos Aires Argentino de Lomas (1931-07-12): walk over
- não jogado — San Isidro Sportivo Buenos Aires (1931-07-19): 1:3, annulled
- abandonado/suspenso, sem valer — Barracas Central Sportivo Buenos Aires (1931-09-13): abandoned at 1:4, see Dec 23
- abandonado/suspenso, sem valer — Excursionistas El Porvenir (1931-10-04): abandoned at 3:1 in 75, see Nov 4
- abandonado/suspenso, sem valer — Argentino de Quilmes Estudiantes de Buenos Aires (1931-11-01): abandoned at 4:2 in 30, see Nov 4
- W.O./pontos para o mandante — Colegiales Argentino de Lomas (1931-11-13): Argentino de Lomas forfeited
- W.O./pontos para o visitante — San Fernando Defensores de Belgrano (1931-12-13)
- W.O./pontos para o visitante — Defensores de Belgrano Sportivo Buenos Aires (1931-12-16): Defensores de Belgrano forfeited
- W.O./pontos para o visitante — Sportivo Barracas Sportivo Palermo (1931-12-16): Sportivo Barracas forfeited
- W.O./pontos para o mandante — Estudiantil Porteño Argentino de Quilmes (1931-12-20): walk over

### 1932 Liga

- abandonado/suspenso, sem valer — Gimnasia La Plata Independiente (1932-06-05): abandoned at 1:2 in 67
- abandonado/suspenso, sem valer — River Plate Huracán (1932-06-05): abandoned at 1:1 in 75
- abandonado/suspenso, sem valer — Vélez Sarsfield Boca Juniors (1932-06-05): abandoned at 1:2 in 75
- W.O./pontos para o mandante — Vélez Sarsfield Boca Juniors (1932-06-23): awarded; jogo repetido (o primeiro foi suspenso)
- abandonado/suspenso, sem valer — Huracán Racing Club (1932-06-12): abandoned at 0:1 in 72
- W.O./pontos para o visitante — Huracán Racing Club (1932-06-23): awarded; jogo repetido (o primeiro foi suspenso)
- W.O./pontos para o visitante — Huracán Boca Juniors (1932-07-10): abandoned at 0:3 in 51, at San Lorenzo de Almagro
- W.O./pontos para o mandante — Boca Juniors Atlanta (1932-07-24): abandoned at 2:1 in 70
- W.O./pontos para o visitante — Lanús Independiente (1932-08-14): abandoned at 0:0 in 82
- W.O./pontos para o mandante — Platense Gimnasia La Plata (1932-08-14): abandoned at 2:2 in 73

### 1932 Asociación

- tabela publicada x jogos — arg32a:33: Sportivo Barracas tabela [32, 21, 5, 6, 74, 35] jogos [32, 21, 5, 6, 75, 35] — a diferença vem de Temperley x Sportivo Barracas (1932-12-18), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg32a:33: Defensores de Belgrano tabela [32, 16, 6, 10, 56, 46] jogos [32, 16, 6, 10, 57, 48] — a diferença vem de Temperley x Defensores de Belgrano (1932-11-19), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg32a:33: Almagro tabela [32, 14, 7, 11, 48, 50] jogos [32, 14, 7, 11, 48, 52] — a diferença vem de Sportivo Palermo x Almagro (1932-11-12), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg32a:33: Banfield tabela [32, 12, 6, 14, 44, 49] jogos [32, 12, 6, 14, 45, 50] — a diferença vem de Liberal Argentino x Banfield (1932-10-23), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg32a:33: Liberal Argentino tabela [32, 10, 8, 14, 34, 41] jogos [32, 10, 8, 14, 35, 42] — a diferença vem de Liberal Argentino x Banfield (1932-10-23), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg32a:33: Estudiantil Porteño tabela [32, 10, 7, 15, 45, 61] jogos [32, 10, 7, 15, 45, 62] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg32a:33: Temperley tabela [32, 9, 8, 15, 35, 57] jogos [32, 9, 8, 15, 37, 58] — a diferença vem de Temperley x Defensores de Belgrano (1932-11-19), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg32a:33: Sportivo Palermo tabela [32, 10, 4, 18, 39, 36] jogos [32, 10, 4, 18, 41, 36] — a diferença vem de Sportivo Palermo x Almagro (1932-11-12), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- abandonado/suspenso, sem valer — Colegiales 1-1 Liberal Argentino (1932-10-09): Suspended at 38; played again on Dec 8
- W.O./pontos para o mandante — Liberal Argentino 1-1 Banfield (1932-10-23): Suspended at 42 due to rain; Liberal Argentino won points
- W.O./pontos para o visitante — Sportivo Palermo 2-0 Almagro (1932-11-12): Suspended at 45; not continued][Later Almagro won points
- W.O./pontos para o visitante — Temperley 2-1 Defensores de Belgrano (1932-11-19): Later Defensores de Belgrano won points
- W.O./pontos para o mandante — Banfield Sportivo Buenos Aires (1932-12-11): Sportivo Buenos Aires withdrew
- W.O./pontos para o mandante — Temperley Sportivo Barracas (1932-12-18): Sportivo Barracas withdrew
- W.O./pontos para o mandante — Barracas Central Almagro (1932-12-31): Almagro withdrew
- W.O./pontos para o mandante — Sportivo Buenos Aires Argentino de Quilmes (1932-12-31): Argentino de Quilmes withdrew
- W.O./pontos para o mandante — Defensores de Belgrano Banfield (1932-12-31): Banfield withdrew
- W.O./pontos para o mandante — Liberal Argentino Sportivo Palermo (1933-01-07): Sportivo Palermo forfeited
- W.O./pontos para o mandante — Excursionistas El Porvenir (1933-01-07): El Porvenir withdrew
- W.O./pontos para o visitante — Argentino de Quilmes Defensores de Belgrano (1933-01-08): Argentino de Quilmes withdrew
- W.O./pontos para o visitante — Sportivo Palermo Excursionistas (1933-01-08): Sportivo Palermo forfeited
- W.O./pontos para o mandante — Sportivo Buenos Aires Sportivo Palermo (1933-01-08): Sportivo Palermo forfeited
- W.O./pontos para o visitante — Sportivo Palermo Temperley (1933-01-08): Sportivo Palermo forfeited
- W.O./pontos para o mandante — Barracas Central Sportivo Palermo (1933-01-08): Sportivo Palermo forfeited
- W.O./pontos para o visitante — Sportivo Palermo Colegiales (1933-01-08): Sportivo Palermo forfeited
- W.O./pontos para o visitante — Sportivo Palermo Banfield (1933-01-08): Sportivo Palermo forfeited
- W.O./pontos para o visitante — Estudiantil Porteño Sportivo Buenos Aires (1933-01-08): Estudiantil Porteño withdrew
- W.O./pontos para o mandante — Temperley Estudiantes de Buenos Aires (1933-01-08): Estudiantes BA withdrew
- W.O./pontos para o mandante — El Porvenir All Boys (1933-01-08): All Boys withdrew
- W.O./pontos para o visitante — Sportivo Barracas Liberal Argentino (1933-01-08): Sportivo Barracas withdrew

### 1933 Liga

- abandonado/suspenso, sem valer — Argentinos Juniors Racing Club (1933-10-22): abandoned at 1:0 in 33

### 1933 Asociación

- W.O./pontos para o mandante — Nueva Chicago Defensores de Belgrano (1933-08-20): Defensores de Belgrano withdrew
- W.O./pontos para o mandante — Liberal Argentino Estudiantil Porteño (1933-10-12): Estudiantil Porteño withdrew
- W.O./pontos para o mandante — Estudiantil Porteño Barracas Central (1933-11-05): Barracas Central withdrew
- W.O./pontos para o mandante — Palermo Sportivo Buenos Aires (1933-11-05): Sportivo Buenos Aires withdrew
- W.O./pontos para o mandante — Temperley El Porvenir (1933-11-05): El Porvenir withdrew

### 1934 Liga

- fusões temporárias de 1934 à parte dos clubes (D-25 h): os jogos de "Atlanta/Argentinos Jrs" ficam com o Atlanta-Argentinos Juniors e os de "Talleres/Lanús" com a Unión Talleres-Lanús; a tabela da RSSSF põe a campanha inteira (39 jogos) na linha do Argentinos Juniors, que fica com só os 14 jogos de antes da fusão
- a Liga e a Asociación se fundiram em 3/11/1934, com o campeonato em andamento
- tabela publicada x jogos — arg34:427: Estudiantes tabela [39, 17, 10, 12, 70, 56] jogos [39, 17, 10, 12, 69, 56] — a diferença vem de Gimnasia La Plata x Estudiantes (1934-06-10), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg34:427: Gimnasia La Plata tabela [39, 14, 10, 15, 82, 86] jogos [39, 14, 10, 15, 82, 85] — a diferença vem de Gimnasia La Plata x Estudiantes (1934-06-10), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg34:427: Argentinos Juniors tabela [39, 2, 5, 32, 38, 113] jogos [14, 0, 2, 12, 14, 44] — faltam 25 jogo(s) do clube na página
- abandonado/suspenso, sem valer — Gimnasia La Plata Estudiantes (1934-06-10): abandoned at 0:1 in 15
- abandonado/suspenso, sem valer — Racing Club Chacarita Juniors (1934-06-10): abandoned at 1:2 in 83
- W.O./pontos para o mandante — Gimnasia La Plata Estudiantes (1934-06-10): awarded; jogo repetido (o primeiro foi suspenso)
- abandonado/suspenso, sem valer — Chacarita Juniors Racing Club (1934-12-02): abandoned at 2:2 in 53

### 1934 Asociación

- tabela publicada x jogos — arg34a:26: Estudiantes de Buenos Aires tabela [22, 12, 3, 7, 41, 24] jogos [22, 12, 3, 7, 42, 25] — a diferença vem de Ramsar x Estudiantes de Buenos Aires (1934-05-06), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg34a:26: Ramsar tabela [22, 4, 5, 13, 21, 48] jogos [22, 4, 5, 13, 22, 49] — a diferença vem de Ramsar x Estudiantes de Buenos Aires (1934-05-06), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- W.O./pontos para o mandante — Nueva Chicago Sportivo Acassuso (1934-04-22): Sportivo Acassuso withdrew
- W.O./pontos para o mandante — Sportivo Acassuso Defensores de Belgrano (1934-04-29): Defensores de Belgrano withdrew
- W.O./pontos para o visitante — Ramsar 1-1 Estudiantes de Buenos Aires (1934-05-06): Ramsar lost the points
- W.O./pontos para o mandante — Gutenberg All Boys (1934-07-29): All Boys withdrew
- W.O./pontos para o mandante — Palermo Gutenberg (1934-08-05): Gutenberg withdrew

### 1935

- sem ocorrências

### 1936 Copa de Honor

- título de Primera División reconhecido pela AFA em 4/7/2013
- W.O./pontos para o visitante — Talleres de Remedios de Escalada Platense (1936-06-23): awarded on Jun 23
- W.O./pontos para o mandante — Atlanta Talleres de Remedios de Escalada (1936-06-23): awarded on Jun 23
- W.O./pontos para o mandante — Independiente 1-1 Racing Club (1936-07-05): abandoned at 1:1 in 62m, awarded on Jul 14
- W.O./pontos para o visitante — Talleres de Remedios de Escalada Quilmes (1936-06-23): awarded on Jun 23
- W.O./pontos para o mandante — Independiente Talleres de Remedios de Escalada (1936-06-23): awarded on Jun 23

### 1936 Campeonato

- sem ocorrências

### 1936 Copa de Oro

- jogo único entre os campeões da Copa de Honor (San Lorenzo) e da Copa Campeonato (River Plate), lido à mão da página arg-oro36 da RSSSF (texto corrido)
- jogo entre os campeões da Copa de Honor e da Copa Campeonato; título reconhecido pela AFA em 4/7/2013
- corrigido — River Plate x San Lorenzo (None): a linha do texto corrido vira o jogo escrito à mão (EXTRAS), com data, local e autores dos gols

### 1937

- sem ocorrências

### 1938

- sem ocorrências

### 1939

- abandonado/suspenso, sem valer — Boca Juniors Ferro Carril Oeste (1939-12-02): abandoned at 1:0 in 33, at Chacarita Juniors
- W.O./pontos para o mandante — Boca Juniors Ferro Carril Oeste (1939-12-22): awarded; jogo repetido (o primeiro foi suspenso)

### 1940

- W.O./pontos para o mandante — Vélez Sarsfield Ferro Carril Oeste (1940-04-07)
- W.O./pontos para o mandante — Newell's Old Boys Banfield (1940-04-07)
- W.O./pontos para o visitante — Banfield Vélez Sarsfield (1940-05-02)
- W.O./pontos para o mandante — Huracán Banfield (1940-04-21)
- W.O./pontos para o visitante — Banfield Boca Juniors (1940-04-28)
- W.O./pontos para o mandante — Lanús Banfield (1940-05-05)
- W.O./pontos para o visitante — Chacarita Juniors Boca Juniors (1940-09-22)
- W.O./pontos para o mandante — Lanús Chacarita Juniors (1940-09-29)
- W.O./pontos para o visitante — Chacarita Juniors Atlanta (1940-10-06)
- W.O./pontos para o mandante — Independiente Chacarita Juniors (1940-10-20)
- W.O./pontos para o visitante — Chacarita Juniors Gimnasia La Plata (1940-10-27)
- W.O./pontos para o mandante — Rosario Central Chacarita Juniors (1940-11-03)

### 1941

- abandonado/suspenso, sem valer — Rosario Central Boca Juniors (1941-09-21): abandoned at 1:0 in 70

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

- sem ocorrências

### 1948

- W.O./pontos para o visitante — Racing Club Banfield (1948-12-08): not played, awarded on Dec 16, Racing 2 points deducted, at San Lorenzo de Almagro
- W.O./pontos para o mandante — San Lorenzo Racing Club (1948-12-12): not played, awarded on Dec 22, Racing 2 points deducted

### 1949

- anulado — Huracán Lanús (1950-01-08): ended at 3:3 in 90m, extra time not played, annulled on Jan 12, San Lorenzo de Almagro, Buenos Aires

### 1950

- sem ocorrências

### 1951

- sem ocorrências

### 1952

- sem ocorrências

### 1953

- sem ocorrências

### 1954

- sem ocorrências

### 1955

- ogol: 239 jogos casados (edição 36999 do ogol, 240 jogos)
- abandonado/suspenso, sem valer — River Plate San Lorenzo (1955-08-07): at Huracán, abandoned at 0:0 in 3
- abandonado/suspenso, sem valer — Estudiantes River Plate (1955-11-13): abandoned at 1:2 in 82
- abandonado/suspenso, sem valer — San Lorenzo 0-1 River Plate (1955-11-27): abandoned at 0:1 in 45

### 1956

- ogol: 240 jogos casados (edição 36998 do ogol, 240 jogos)

### 1957

- ogol: 239 jogos casados (edição 36997 do ogol, 240 jogos)

### 1958

- ogol: 242 jogos casados (edição 31226 do ogol, 242 jogos)
- W.O./pontos para o visitante — River Plate Huracán (1958-11-02): not played, River Plate 2 points deducted, at Ferro Carril Oeste

### 1959

- ogol: 238 jogos casados (edição 150081 do ogol, 240 jogos)
- data diferente no ogol — Central Córdoba de Rosario x San Lorenzo: RSSSF 1959-05-31, ogol 1959-06-07; fica a da RSSSF
- data diferente no ogol — River Plate x Atlanta: RSSSF 1959-05-31, ogol 1959-06-07; fica a da RSSSF
- data diferente no ogol — Racing Club x Lanús: RSSSF 1959-05-31, ogol 1959-06-07; fica a da RSSSF
- data diferente no ogol — Estudiantes x Independiente: RSSSF 1959-05-31, ogol 1959-06-07; fica a da RSSSF
- data diferente no ogol — Huracán x Rosario Central: RSSSF 1959-05-31, ogol 1959-06-07; fica a da RSSSF
- data diferente no ogol — Argentinos Juniors x Gimnasia La Plata: RSSSF 1959-05-31, ogol 1959-06-07; fica a da RSSSF
- data diferente no ogol — Ferro Carril Oeste x Boca Juniors: RSSSF 1959-05-31, ogol 1959-06-07; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x Vélez Sarsfield: RSSSF 1959-05-31, ogol 1959-06-07; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Newell's Old Boys: RSSSF 1959-06-07, ogol 1959-06-14; fica a da RSSSF
- data diferente no ogol — Boca Juniors x Huracán: RSSSF 1959-06-07, ogol 1959-06-14; fica a da RSSSF
- data diferente no ogol — Central Córdoba de Rosario x Racing Club: RSSSF 1959-06-07, ogol 1959-06-14; fica a da RSSSF
- placar diferente no ogol — Vélez Sarsfield x River Plate (1959-06-07): RSSSF 1-2, ogol 1-1; fica o da RSSSF
- data diferente no ogol — Vélez Sarsfield x River Plate: RSSSF 1959-06-07, ogol 1959-06-14; fica a da RSSSF
- data diferente no ogol — Independiente x Argentinos Juniors: RSSSF 1959-06-07, ogol 1959-06-14; fica a da RSSSF
- data diferente no ogol — Atlanta x Estudiantes: RSSSF 1959-06-07, ogol 1959-06-14; fica a da RSSSF
- data diferente no ogol — Gimnasia La Plata x Ferro Carril Oeste: RSSSF 1959-06-07, ogol 1959-06-14; fica a da RSSSF
- data diferente no ogol — Rosario Central x Lanús: RSSSF 1959-06-07, ogol 1959-06-14; fica a da RSSSF
- data diferente no ogol — River Plate x San Lorenzo: RSSSF 1959-06-14, ogol 1959-06-21; fica a da RSSSF
- data diferente no ogol — Huracán x Gimnasia La Plata: RSSSF 1959-06-14, ogol 1959-06-21; fica a da RSSSF
- data diferente no ogol — Lanús x Boca Juniors: RSSSF 1959-06-14, ogol 1959-06-21; fica a da RSSSF
- data diferente no ogol — Argentinos Juniors x Atlanta: RSSSF 1959-06-14, ogol 1959-06-21; fica a da RSSSF
- data diferente no ogol — Ferro Carril Oeste x Independiente: RSSSF 1959-06-14, ogol 1959-06-21; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x Central Córdoba de Rosario: RSSSF 1959-06-14, ogol 1959-06-21; fica a da RSSSF
- placar diferente no ogol — Racing Club x Rosario Central (1959-06-14): RSSSF 4-0, ogol 4-1; fica o da RSSSF
- data diferente no ogol — Racing Club x Rosario Central: RSSSF 1959-06-14, ogol 1959-06-21; fica a da RSSSF
- data diferente no ogol — Estudiantes x Vélez Sarsfield: RSSSF 1959-06-14, ogol 1959-06-21; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x Racing Club: RSSSF 1959-06-20, ogol 1959-06-28; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Estudiantes: RSSSF 1959-06-21, ogol 1959-06-28; fica a da RSSSF
- data diferente no ogol — Gimnasia La Plata x Lanús: RSSSF 1959-06-21, ogol 1959-06-28; fica a da RSSSF
- data diferente no ogol — Atlanta x Ferro Carril Oeste: RSSSF 1959-06-21, ogol 1959-06-28; fica a da RSSSF
- data diferente no ogol — Vélez Sarsfield x Argentinos Juniors: RSSSF 1959-06-21, ogol 1959-06-28; fica a da RSSSF
- data diferente no ogol — Independiente x Huracán: RSSSF 1959-06-21, ogol 1959-06-28; fica a da RSSSF
- data diferente no ogol — Boca Juniors x Rosario Central: RSSSF 1959-06-21, ogol 1959-06-28; fica a da RSSSF
- data diferente no ogol — Central Córdoba de Rosario x River Plate: RSSSF 1959-06-22, ogol 1959-06-28; fica a da RSSSF
- data diferente no ogol — Argentinos Juniors x San Lorenzo: RSSSF 1959-06-28, ogol 1959-07-05; fica a da RSSSF
- data diferente no ogol — Racing Club x Boca Juniors: RSSSF 1959-06-28, ogol 1959-07-05; fica a da RSSSF
- data diferente no ogol — Lanús x Independiente: RSSSF 1959-06-28, ogol 1959-07-05; fica a da RSSSF
- data diferente no ogol — River Plate x Newell's Old Boys: RSSSF 1959-06-28, ogol 1959-07-05; fica a da RSSSF
- data diferente no ogol — Estudiantes x Central Córdoba de Rosario: RSSSF 1959-06-28, ogol 1959-07-05; fica a da RSSSF
- data diferente no ogol — Rosario Central x Gimnasia La Plata: RSSSF 1959-06-28, ogol 1959-07-05; fica a da RSSSF
- data diferente no ogol — Huracán x Atlanta: RSSSF 1959-06-28, ogol 1959-07-05; fica a da RSSSF
- data diferente no ogol — Ferro Carril Oeste x Vélez Sarsfield: RSSSF 1959-06-28, ogol 1959-07-05; fica a da RSSSF
- data diferente no ogol — Central Córdoba de Rosario x Argentinos Juniors: RSSSF 1959-07-04, ogol 1959-07-12; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Ferro Carril Oeste: RSSSF 1959-07-05, ogol 1959-07-12; fica a da RSSSF
- data diferente no ogol — Gimnasia La Plata x Boca Juniors: RSSSF 1959-07-05, ogol 1959-07-12; fica a da RSSSF
- data diferente no ogol — River Plate x Racing Club: RSSSF 1959-07-05, ogol 1959-07-12; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x Estudiantes: RSSSF 1959-07-05, ogol 1959-07-12; fica a da RSSSF
- data diferente no ogol — Independiente x Rosario Central: RSSSF 1959-07-05, ogol 1959-07-12; fica a da RSSSF
- data diferente no ogol — Vélez Sarsfield x Huracán: RSSSF 1959-07-05, ogol 1959-07-12; fica a da RSSSF
- data diferente no ogol — Atlanta x Lanús: RSSSF 1959-07-05, ogol 1959-07-12; fica a da RSSSF
- data diferente no ogol — Huracán x San Lorenzo: RSSSF 1959-07-26, ogol 1959-07-19; fica a da RSSSF
- data diferente no ogol — Lanús x Vélez Sarsfield: RSSSF 1959-07-26, ogol 1959-07-19; fica a da RSSSF
- data diferente no ogol — Boca Juniors x Independiente: RSSSF 1959-07-26, ogol 1959-07-19; fica a da RSSSF
- data diferente no ogol — Estudiantes x River Plate: RSSSF 1959-07-26, ogol 1959-07-19; fica a da RSSSF
- data diferente no ogol — Ferro Carril Oeste x Central Córdoba de Rosario: RSSSF 1959-07-26, ogol 1959-07-19; fica a da RSSSF
- data diferente no ogol — Racing Club x Gimnasia La Plata: RSSSF 1959-07-26, ogol 1959-07-19; fica a da RSSSF
- data diferente no ogol — Argentinos Juniors x Newell's Old Boys: RSSSF 1959-07-26, ogol 1959-07-19; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x Ferro Carril Oeste: RSSSF 1959-08-01, ogol 1959-07-26; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Lanús: RSSSF 1959-08-02, ogol 1959-07-26; fica a da RSSSF
- data diferente no ogol — River Plate x Argentinos Juniors: RSSSF 1959-08-02, ogol 1959-07-26; fica a da RSSSF
- data diferente no ogol — Estudiantes x Racing Club: RSSSF 1959-08-02, ogol 1959-07-26; fica a da RSSSF
- data diferente no ogol — Vélez Sarsfield x Rosario Central: RSSSF 1959-08-02, ogol 1959-07-26; fica a da RSSSF
- data diferente no ogol — Independiente x Gimnasia La Plata: RSSSF 1959-08-02, ogol 1959-07-26; fica a da RSSSF
- data diferente no ogol — Central Córdoba de Rosario x Huracán: RSSSF 1959-08-02, ogol 1959-07-26; fica a da RSSSF
- data diferente no ogol — Atlanta x Boca Juniors: RSSSF 1959-08-02, ogol 1959-07-26; fica a da RSSSF
- data diferente no ogol — Rosario Central x San Lorenzo: RSSSF 1959-08-09, ogol 1959-08-02; fica a da RSSSF
- data diferente no ogol — Boca Juniors x Vélez Sarsfield: RSSSF 1959-08-09, ogol 1959-08-02; fica a da RSSSF
- data diferente no ogol — Racing Club x Independiente: RSSSF 1959-08-09, ogol 1959-08-02; fica a da RSSSF
- data diferente no ogol — Ferro Carril Oeste x River Plate: RSSSF 1959-08-09, ogol 1959-08-02; fica a da RSSSF
- data diferente no ogol — Argentinos Juniors x Estudiantes: RSSSF 1959-08-09, ogol 1959-08-02; fica a da RSSSF
- data diferente no ogol — Huracán x Newell's Old Boys: RSSSF 1959-08-09, ogol 1959-08-02; fica a da RSSSF
- data diferente no ogol — Lanús x Central Córdoba de Rosario: RSSSF 1959-08-09, ogol 1959-08-02; fica a da RSSSF
- data diferente no ogol — Gimnasia La Plata x Atlanta: RSSSF 1959-08-09, ogol 1959-08-02; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Boca Juniors: RSSSF 1959-08-16, ogol 1959-08-09; fica a da RSSSF
- data diferente no ogol — Racing Club x Argentinos Juniors: RSSSF 1959-08-16, ogol 1959-08-09; fica a da RSSSF
- data diferente no ogol — River Plate x Huracán: RSSSF 1959-08-16, ogol 1959-08-09; fica a da RSSSF
- data diferente no ogol — Vélez Sarsfield x Gimnasia La Plata: RSSSF 1959-08-16, ogol 1959-08-09; fica a da RSSSF
- data diferente no ogol — Estudiantes x Ferro Carril Oeste: RSSSF 1959-08-16, ogol 1959-08-09; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x Lanús: RSSSF 1959-08-16, ogol 1959-08-09; fica a da RSSSF
- data diferente no ogol — Atlanta x Independiente: RSSSF 1959-08-17, ogol 1959-08-09; fica a da RSSSF
- data diferente no ogol — Central Córdoba de Rosario x Rosario Central: RSSSF 1959-08-17, ogol 1959-08-09; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Gimnasia La Plata: RSSSF 1959-08-23, ogol 1959-08-16; fica a da RSSSF
- data diferente no ogol — Central Córdoba de Rosario x Boca Juniors: RSSSF 1959-08-23, ogol 1959-08-16; fica a da RSSSF
- data diferente no ogol — Racing Club x Atlanta: RSSSF 1959-08-23, ogol 1959-08-16; fica a da RSSSF
- data diferente no ogol — Estudiantes x Huracán: RSSSF 1959-08-23, ogol 1959-08-16; fica a da RSSSF
- data diferente no ogol — River Plate x Lanús: RSSSF 1959-08-23, ogol 1959-08-16; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x Rosario Central: RSSSF 1959-08-23, ogol 1959-08-16; fica a da RSSSF
- data diferente no ogol — Argentinos Juniors x Ferro Carril Oeste: RSSSF 1959-08-23, ogol 1959-08-16; fica a da RSSSF
- data diferente no ogol — Vélez Sarsfield x Independiente: RSSSF 1959-08-23, ogol 1959-08-16; fica a da RSSSF
- data diferente no ogol — Gimnasia La Plata x Central Córdoba de Rosario: RSSSF 1959-08-30, ogol 1959-08-23; fica a da RSSSF
- data diferente no ogol — Boca Juniors x Newell's Old Boys: RSSSF 1959-08-30, ogol 1959-08-23; fica a da RSSSF
- data diferente no ogol — Rosario Central x River Plate: RSSSF 1959-08-30, ogol 1959-08-23; fica a da RSSSF
- data diferente no ogol — Independiente x San Lorenzo: RSSSF 1959-08-30, ogol 1959-08-23; fica a da RSSSF
- data diferente no ogol — Atlanta x Vélez Sarsfield: RSSSF 1959-08-30, ogol 1959-08-23; fica a da RSSSF
- data diferente no ogol — Huracán x Argentinos Juniors: RSSSF 1959-08-30, ogol 1959-08-23; fica a da RSSSF
- data diferente no ogol — Ferro Carril Oeste x Racing Club: RSSSF 1959-08-30, ogol 1959-08-23; fica a da RSSSF
- data diferente no ogol — Lanús x Estudiantes: RSSSF 1959-08-30, ogol 1959-08-23; fica a da RSSSF
- data diferente no ogol — Estudiantes x Rosario Central: RSSSF 1959-09-06, ogol 1959-08-30; fica a da RSSSF
- data diferente no ogol — Central Córdoba de Rosario x Independiente: RSSSF 1959-09-06, ogol 1959-08-30; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x Gimnasia La Plata: RSSSF 1959-09-05, ogol 1959-08-30; fica a da RSSSF
- data diferente no ogol — River Plate x Boca Juniors: RSSSF 1959-09-06, ogol 1959-08-30; fica a da RSSSF
- data diferente no ogol — Argentinos Juniors x Lanús: RSSSF 1959-09-06, ogol 1959-08-30; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Atlanta: RSSSF 1959-09-06, ogol 1959-08-30; fica a da RSSSF
- data diferente no ogol — Racing Club x Vélez Sarsfield: RSSSF 1959-09-06, ogol 1959-08-30; fica a da RSSSF
- data diferente no ogol — Ferro Carril Oeste x Huracán: RSSSF 1959-09-06, ogol 1959-08-30; fica a da RSSSF
- data diferente no ogol — Vélez Sarsfield x San Lorenzo: RSSSF 1959-09-13, ogol 1959-09-06; fica a da RSSSF
- data diferente no ogol — Boca Juniors x Estudiantes: RSSSF 1959-09-13, ogol 1959-09-06; fica a da RSSSF
- data diferente no ogol — Huracán x Racing Club: RSSSF 1959-09-13, ogol 1959-09-06; fica a da RSSSF
- data diferente no ogol — Rosario Central x Argentinos Juniors: RSSSF 1959-09-13, ogol 1959-09-06; fica a da RSSSF
- data diferente no ogol — Atlanta x Central Córdoba de Rosario: RSSSF 1959-09-13, ogol 1959-09-06; fica a da RSSSF
- data diferente no ogol — Lanús x Ferro Carril Oeste: RSSSF 1959-09-13, ogol 1959-09-06; fica a da RSSSF
- data diferente no ogol — Independiente x Newell's Old Boys: RSSSF 1959-09-13, ogol 1959-09-06; fica a da RSSSF
- data diferente no ogol — Gimnasia La Plata x River Plate: RSSSF 1959-09-13, ogol 1959-09-06; fica a da RSSSF
- data diferente no ogol — Racing Club x San Lorenzo: RSSSF 1959-09-20, ogol 1959-09-13; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x Atlanta: RSSSF 1959-09-20, ogol 1959-09-13; fica a da RSSSF
- data diferente no ogol — River Plate x Independiente: RSSSF 1959-09-20, ogol 1959-09-13; fica a da RSSSF
- data diferente no ogol — Ferro Carril Oeste x Rosario Central: RSSSF 1959-09-20, ogol 1959-09-13; fica a da RSSSF
- data diferente no ogol — Argentinos Juniors x Boca Juniors: RSSSF 1959-09-20, ogol 1959-09-13; fica a da RSSSF
- data diferente no ogol — Huracán x Lanús: RSSSF 1959-09-20, ogol 1959-09-13; fica a da RSSSF
- data diferente no ogol — Central Córdoba de Rosario x Vélez Sarsfield: RSSSF 1959-09-20, ogol 1959-09-13; fica a da RSSSF
- data diferente no ogol — Estudiantes x Gimnasia La Plata: RSSSF 1959-09-20, ogol 1959-09-13; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Central Córdoba de Rosario: RSSSF 1959-09-27, ogol 1959-09-20; fica a da RSSSF
- data diferente no ogol — Atlanta x River Plate: RSSSF 1959-09-27, ogol 1959-09-20; fica a da RSSSF
- data diferente no ogol — Lanús x Racing Club: RSSSF 1959-09-27, ogol 1959-09-20; fica a da RSSSF
- data diferente no ogol — Independiente x Estudiantes: RSSSF 1959-09-27, ogol 1959-09-20; fica a da RSSSF
- data diferente no ogol — Rosario Central x Huracán: RSSSF 1959-09-27, ogol 1959-09-20; fica a da RSSSF
- data diferente no ogol — Gimnasia La Plata x Argentinos Juniors: RSSSF 1959-09-27, ogol 1959-09-20; fica a da RSSSF
- data diferente no ogol — Boca Juniors x Ferro Carril Oeste: RSSSF 1959-09-27, ogol 1959-09-20; fica a da RSSSF
- data diferente no ogol — Vélez Sarsfield x Newell's Old Boys: RSSSF 1959-09-27, ogol 1959-09-20; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x San Lorenzo: RSSSF 1959-10-04, ogol 1959-09-27; fica a da RSSSF
- data diferente no ogol — Huracán x Boca Juniors: RSSSF 1959-10-04, ogol 1959-09-27; fica a da RSSSF
- data diferente no ogol — Racing Club x Central Córdoba de Rosario: RSSSF 1959-10-04, ogol 1959-09-27; fica a da RSSSF
- data diferente no ogol — River Plate x Vélez Sarsfield: RSSSF 1959-10-04, ogol 1959-09-27; fica a da RSSSF
- data diferente no ogol — Argentinos Juniors x Independiente: RSSSF 1959-10-04, ogol 1959-09-27; fica a da RSSSF
- data diferente no ogol — Estudiantes x Atlanta: RSSSF 1959-10-04, ogol 1959-09-27; fica a da RSSSF
- data diferente no ogol — Ferro Carril Oeste x Gimnasia La Plata: RSSSF 1959-10-04, ogol 1959-09-27; fica a da RSSSF
- data diferente no ogol — Lanús x Rosario Central: RSSSF 1959-10-04, ogol 1959-09-27; fica a da RSSSF
- data diferente no ogol — San Lorenzo x River Plate: RSSSF 1959-10-12, ogol 1959-10-04; fica a da RSSSF
- data diferente no ogol — Gimnasia La Plata x Huracán: RSSSF 1959-10-12, ogol 1959-10-04; fica a da RSSSF
- data diferente no ogol — Boca Juniors x Lanús: RSSSF 1959-10-12, ogol 1959-10-04; fica a da RSSSF
- data diferente no ogol — Independiente x Ferro Carril Oeste: RSSSF 1959-10-12, ogol 1959-10-04; fica a da RSSSF
- data diferente no ogol — Central Córdoba de Rosario x Newell's Old Boys: RSSSF 1959-10-11, ogol 1959-10-04; fica a da RSSSF
- data diferente no ogol — Rosario Central x Racing Club: RSSSF 1959-10-11, ogol 1959-10-04; fica a da RSSSF
- data diferente no ogol — Racing Club x Newell's Old Boys: RSSSF 1959-10-18, ogol 1959-10-11; fica a da RSSSF
- data diferente no ogol — Estudiantes x San Lorenzo: RSSSF 1959-10-18, ogol 1959-10-11; fica a da RSSSF
- data diferente no ogol — Lanús x Gimnasia La Plata: RSSSF 1959-10-18, ogol 1959-10-11; fica a da RSSSF
- data diferente no ogol — Ferro Carril Oeste x Atlanta: RSSSF 1959-10-18, ogol 1959-10-11; fica a da RSSSF
- data diferente no ogol — Argentinos Juniors x Vélez Sarsfield: RSSSF 1959-10-18, ogol 1959-10-11; fica a da RSSSF
- data diferente no ogol — Huracán x Independiente: RSSSF 1959-10-18, ogol 1959-10-11; fica a da RSSSF
- data diferente no ogol — Rosario Central x Boca Juniors: RSSSF 1959-10-17, ogol 1959-10-11; fica a da RSSSF
- data diferente no ogol — River Plate x Central Córdoba de Rosario: RSSSF 1959-10-18, ogol 1959-10-11; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Argentinos Juniors: RSSSF 1959-10-28, ogol 1959-10-18; fica a da RSSSF
- data diferente no ogol — Boca Juniors x Racing Club: RSSSF 1959-10-27, ogol 1959-10-18; fica a da RSSSF
- data diferente no ogol — Independiente x Lanús: RSSSF 1959-10-28, ogol 1959-10-18; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x River Plate: RSSSF 1959-10-25, ogol 1959-10-18; fica a da RSSSF
- data diferente no ogol — Central Córdoba de Rosario x Estudiantes: RSSSF 1959-10-24, ogol 1959-10-18; fica a da RSSSF
- data diferente no ogol — Gimnasia La Plata x Rosario Central: RSSSF 1959-10-26, ogol 1959-10-18; fica a da RSSSF
- data diferente no ogol — Atlanta x Huracán: RSSSF 1959-10-28, ogol 1959-10-18; fica a da RSSSF
- data diferente no ogol — Vélez Sarsfield x Ferro Carril Oeste: RSSSF 1959-10-27, ogol 1959-10-18; fica a da RSSSF
- data diferente no ogol — Argentinos Juniors x Central Córdoba de Rosario: RSSSF 1959-11-01, ogol 1959-10-25; fica a da RSSSF
- data diferente no ogol — Ferro Carril Oeste x San Lorenzo: RSSSF 1959-11-01, ogol 1959-10-25; fica a da RSSSF
- data diferente no ogol — Boca Juniors x Gimnasia La Plata: RSSSF 1959-11-01, ogol 1959-10-25; fica a da RSSSF
- data diferente no ogol — Racing Club x River Plate: RSSSF 1959-11-01, ogol 1959-10-25; fica a da RSSSF
- data diferente no ogol — Estudiantes x Newell's Old Boys: RSSSF 1959-11-01, ogol 1959-10-25; fica a da RSSSF
- data diferente no ogol — Rosario Central x Independiente: RSSSF 1959-10-31, ogol 1959-10-25; fica a da RSSSF
- data diferente no ogol — Huracán x Vélez Sarsfield: RSSSF 1959-11-01, ogol 1959-10-25; fica a da RSSSF
- data diferente no ogol — Lanús x Atlanta: RSSSF 1959-11-01, ogol 1959-10-25; fica a da RSSSF
- data diferente no ogol — Atlanta x Rosario Central: RSSSF 1959-11-06, ogol 1959-11-01; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Huracán: RSSSF 1959-11-08, ogol 1959-11-01; fica a da RSSSF
- data diferente no ogol — Vélez Sarsfield x Lanús: RSSSF 1959-11-08, ogol 1959-11-01; fica a da RSSSF
- data diferente no ogol — Independiente x Boca Juniors: RSSSF 1959-11-08, ogol 1959-11-01; fica a da RSSSF
- data diferente no ogol — River Plate x Estudiantes: RSSSF 1959-11-08, ogol 1959-11-01; fica a da RSSSF
- data diferente no ogol — Central Córdoba de Rosario x Ferro Carril Oeste: RSSSF 1959-11-08, ogol 1959-11-01; fica a da RSSSF
- data diferente no ogol — Gimnasia La Plata x Racing Club: RSSSF 1959-11-08, ogol 1959-11-01; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x Argentinos Juniors: RSSSF 1959-11-08, ogol 1959-11-01; fica a da RSSSF
- placar diferente no ogol — Newell's Old Boys x Huracán (1959-11-14): RSSSF 1-1, ogol 0-2; fica o da RSSSF
- W.O./pontos para o visitante — Newell's Old Boys 1-1 Huracán (1959-11-14): abandoned at 66m, awarded on Nov 26

### 1960

- ogol: 240 jogos casados (edição 157427 do ogol, 240 jogos)
- data diferente no ogol — Independiente x Newell's Old Boys: RSSSF 1960-07-31, ogol 1960-07-26; fica a da RSSSF
- data diferente no ogol — Lanús x Argentinos Juniors: RSSSF 1960-07-31, ogol 1960-07-26; fica a da RSSSF
- data diferente no ogol — River Plate x Racing Club: RSSSF 1960-07-31, ogol 1960-07-26; fica a da RSSSF
- data diferente no ogol — Estudiantes x Ferro Carril Oeste: RSSSF 1960-07-31, ogol 1960-07-26; fica a da RSSSF
- data diferente no ogol — Atlanta x Chacarita Juniors: RSSSF 1960-07-31, ogol 1960-07-26; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Huracán: RSSSF 1960-07-31, ogol 1960-07-26; fica a da RSSSF
- data diferente no ogol — Vélez Sarsfield x Gimnasia La Plata: RSSSF 1960-07-31, ogol 1960-07-26; fica a da RSSSF
- data diferente no ogol — Rosario Central x Boca Juniors: RSSSF 1960-07-31, ogol 1960-07-26; fica a da RSSSF
- placar diferente no ogol — Gimnasia La Plata x River Plate (1960-08-28): RSSSF 0-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Rosario Central x Newell's Old Boys (1960-09-25): RSSSF 4-1, ogol 4-0; fica o da RSSSF
- placar diferente no ogol — Rosario Central x Argentinos Juniors (1960-10-16): RSSSF 3-3, ogol 3-2; fica o da RSSSF
- placar diferente no ogol — Vélez Sarsfield x Rosario Central (1960-11-27): RSSSF 6-3, ogol 6-0; fica o da RSSSF

### 1961

- ogol: 239 jogos casados (edição 157520 do ogol, 240 jogos)
- placar diferente no ogol — Boca Juniors x Independiente (1961-05-14): RSSSF 2-0, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Chacarita Juniors x Gimnasia La Plata (1961-05-21): RSSSF 5-1, ogol 5-0; fica o da RSSSF
- placar diferente no ogol — Chacarita Juniors x Ferro Carril Oeste (1961-08-06): RSSSF 1-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Ferro Carril Oeste x Vélez Sarsfield (1961-09-03): RSSSF 1-1, ogol 1-0; fica o da RSSSF

### 1962

- ogol: 210 jogos casados (edição 36995 do ogol, 210 jogos)

### 1963

- ogol: 182 jogos casados (edição 36994 do ogol, 182 jogos)

### 1964

- ogol: 240 jogos casados (edição 36993 do ogol, 240 jogos)

### 1965

- Estudiantes e Racing empatam com 36 pontos: a tabela da RSSSF põe o Estudiantes em 5º, a Wikipédia em espanhol, o Racing (saldo de gols); fica a ordem publicada (AR-020)
- ogol: 306 jogos casados (edição 36992 do ogol, 306 jogos)
- tabela publicada x jogos — arg65:19: Racing Club tabela [33, 10, 15, 8, 39, 35] jogos [33, 10, 15, 8, 37, 33] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg65:19: Independiente tabela [33, 8, 14, 11, 30, 31] jogos [33, 8, 14, 11, 28, 29] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arghist-pro1960s:242: Racing Club tabela [34, 10, 16, 8, 39, 35] jogos [33, 10, 15, 8, 37, 33] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arghist-pro1960s:242: Independiente tabela [34, 8, 15, 11, 30, 31] jogos [33, 8, 14, 11, 28, 29] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- corrigido — Independiente x Racing Club (1965-05-13): Independiente 2-2 Racing Club suspenso aos 68' e não continuado; a tabela publicada não conta o jogo (33 jogos para os dois)
- abandonado/suspenso, sem valer — Independiente 2-2 Racing Club (1965-05-13): Suspended at 68m, not continued

### 1966

- ogol: 380 jogos casados (edição 31224 do ogol, 380 jogos)

### 1967 Metropolitano

- sem ocorrências

### 1967 Nacional

- sem ocorrências

### 1968 Metropolitano

- tabela publicada x jogos — arg68:17: Lanús tabela [22, 9, 6, 7, 20, 23] jogos [22, 9, 6, 7, 20, 21] — a diferença vem de Newell's Old Boys x Lanús (1968-06-16), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg68:17: Newell's Old Boys tabela [22, 6, 8, 8, 26, 22] jogos [22, 6, 8, 8, 24, 22] — a diferença vem de Newell's Old Boys x Lanús (1968-06-16), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- decidido fora de campo — Newell's Old Boys Lanús (1968-06-16): originally 2-0, Newell's fielded 1 ineligible player
- W.O./pontos para o visitante — Newell's Old Boys Lanús (1968-07-19): awarded

### 1968 Nacional

- sem ocorrências

### 1969 Metropolitano

- abandonado/suspenso, sem valer — Unión Colón (1969-03-23): abandoned at 0-0 in 51'
- W.O./pontos para o mandante — Unión Colón (1969-04-02): awarded wp-lp; jogo repetido (o primeiro foi suspenso)
- abandonado/suspenso, sem valer — Gimnasia La Plata Estudiantes (1969-04-06): abandoned at 0-0 in 52'

### 1969 Nacional

- sem ocorrências

### 1970 Metropolitano

- sem ocorrências

### 1970 Nacional

- tabela publicada x jogos — arg70:541: Chacarita Juniors tabela [20, 13, 3, 4, 25, 19] jogos [20, 13, 3, 4, 24, 19] — a outra tabela publicada (arg70) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg70:541: San Martín de Tucumán tabela [20, 5, 4, 11, 19, 37] jogos [20, 5, 4, 11, 19, 36] — a diferença vem de San Martín de Tucumán x Chacarita Juniors (1970-11-08), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- abandonado/suspenso, sem valer — San Martín de Tucumán Chacarita Juniors (1970-11-08): abandonded at 0-1 in 86'
- W.O./pontos para o visitante — San Martín de Tucumán Chacarita Juniors (1970-11-19): awarded lp-wp; jogo repetido (o primeiro foi suspenso)
- abandonado/suspenso, sem valer — Banfield Kimberley (1970-12-12): abandoned at 3-0 in 21'

### 1971 Metropolitano

- sem ocorrências

### 1971 Nacional

- tabela publicada x jogos — arg71:1326: Boca Juniors tabela [14, 8, 4, 2, 34, 17] jogos [14, 8, 4, 2, 33, 17] — a diferença vem de Boca Juniors x Huracán de Bahía Blanca (1971-11-14), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg71:1326: Huracán de Bahía Blanca tabela [14, 2, 4, 8, 7, 25] jogos [14, 2, 4, 8, 7, 24] — a diferença vem de Boca Juniors x Huracán de Bahía Blanca (1971-11-14), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- W.O./pontos para o mandante — Boca Juniors Huracán de Bahía Blanca (1971-11-14): Huracán (BB) withdrew

### 1972 Metropolitano

- sem ocorrências

### 1972 Nacional

- tabela publicada x jogos — arg72:550: Huracán tabela [13, 6, 4, 3, 26, 20] jogos [13, 6, 4, 3, 24, 19] — a diferença vem de Newell's Old Boys x Huracán (1972-11-05), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg72:550: Newell's Old Boys tabela [13, 2, 1, 10, 18, 28] jogos [13, 2, 1, 10, 17, 26] — a diferença vem de Newell's Old Boys x Huracán (1972-11-05), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arghist-pro1970s:227: Independiente tabela [13, 0, 3, 10, 10, 46] jogos [13, 4, 5, 4, 24, 20] — a outra tabela publicada (arg72) fecha com os jogos: o erro é desta tabela
- abandonado/suspenso, sem valer — Newell's Old Boys Huracán (1972-11-05): abandoned at 1-2 in 87'
- W.O./pontos para o visitante — Newell's Old Boys Huracán (1972-11-16): awarded lp-wp; jogo repetido (o primeiro foi suspenso)
- abandonado/suspenso, sem valer — Banfield Chacarita Juniors (1972-11-19): abandoned at 0-2 in 70'

### 1973 Metropolitano

- sem ocorrências

### 1973 Nacional

- decidido fora de campo — Kimberley Atlanta (1973-11-25): abandoned at 1-2 and later awarded 0-2

### 1974 Metropolitano

- tabela publicada x jogos — arg74:33: Boca Juniors tabela [18, 10, 3, 5, 37, 21] jogos [19, 11, 3, 5, 39, 21] — a outra tabela publicada (arg74) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg74:33: Ferro Carril Oeste tabela [18, 8, 7, 3, 28, 20] jogos [19, 8, 7, 4, 28, 22] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — arg74:45: Boca Juniors tabela [1, 1, 0, 0, 2, 0] jogos [3, 2, 0, 1, 5, 2] — a outra tabela publicada (arg74) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg74:45: Ferro Carril Oeste tabela [1, 0, 0, 1, 0, 2] jogos [3, 1, 0, 2, 2, 5] — sobram 2 jogo(s) do clube na página
- abandonado/suspenso, sem valer — Rosario Central Newell's Old Boys (1974-06-02): abandoned at 2-2 in 88'
- decidido fora de campo — Rosario Central Newell's Old Boys (1974-06-14): awarded 2-2; jogo repetido (o primeiro foi suspenso)

### 1974 Nacional

- 3º pela lista oficial: Vélez Sarsfield (a tabela o punha em 4º)
- abandonado/suspenso, sem valer — Central Norte Boca Juniors (1974-10-27): at Gimnasia y Tiro,
- abandonado/suspenso, sem valer — Aldosivi Ferro Carril Oeste (1974-10-20): at General San Martín,
- decidido fora de campo — Aldosivi Ferro Carril Oeste (1974-10-31): awarded 0-2

### 1975 Metropolitano

- a tabela da Wikipédia em espanhol tem 1 gol a mais para River (contra), Huracán (contra), Estudiantes (pró) e Banfield (pró): ela conta os gols de campo de Estudiantes 1-2 Huracán (abandonado aos 78', dado 0-2) e Banfield 1-2 River Plate (dado 0-2); a RSSSF e o pacote contam o placar dado (AR-019)

### 1975 Nacional

- sem ocorrências

### 1976 Metropolitano

- decidido fora de campo — Atlanta Estudiantes (1976-02-18): originally 0-1
- decidido fora de campo — Ferro Carril Oeste Vélez Sarsfield (1976-02-15): originally 2-2

### 1976 Nacional

- vice pela lista oficial: River Plate (a tabela o punha em 3º)
- abandonado/suspenso, sem valer — Atlético Tucumán San Martín de Tucumán (1976-11-14): abandoned at 1-0 in 37

### 1977 Metropolitano

- abandonado/suspenso, sem valer — Argentinos Juniors 1-1 Quilmes (1977-02-20): Suspended in 45' because the rain
- abandonado/suspenso, sem valer — Vélez Sarsfield 2-2 Boca Juniors (1977-02-20): Suspended in 45' because the rain
- abandonado/suspenso, sem valer — Banfield 0-1 Huracán (1977-02-20): Suspended in 45' because the rain
- abandonado/suspenso, sem valer — Lanús 0-0 All Boys (1977-02-20): Suspended in 45' because the rain
- abandonado/suspenso, sem valer — Atlanta 1-0 Rosario Central (1977-02-20): Suspended in 36' because the rain
- abandonado/suspenso, sem valer — Boca Juniors 0-0 Estudiantes (1977-09-04): at Racing Club Suspended in 18'

### 1977 Nacional

- ogol: 2 jogos casados (edição 58214 do ogol, 2 jogos)

### 1978 Metropolitano

- sem ocorrências

### 1978 Nacional

- decidido fora de campo — Platense 1-1 Huracán (1978-12-13): Later, awarded 0-1
- decidido fora de campo — San Martín de Tucumán 0-0 Quilmes (1978-11-05): Later awarded 0-1
- decidido fora de campo — San Martín de Mendoza 0-0 San Martín de Tucumán (1978-11-08): San Martín (Mza.) won points; awarded 1-0

### 1979 Metropolitano

- sem ocorrências

### 1979 Nacional

- abandonado/suspenso, sem valer — Independiente Racing Club (1979-10-21): abandoned at 0:1 in 40

### 1980 Metropolitano

- sem ocorrências

### 1980 Nacional

- linha lida como jogo e descartada (clube não reconhecido): arg80:1106 «Rosario Central won x on aggregate score»
- decidido fora de campo — San Lorenzo de Mar del Plata 1-2 Boca Juniors (1980-11-23): awarded 1-0

### 1981 Metropolitano

- sem ocorrências

### 1981 Nacional

- sem ocorrências

### 1982 Metropolitano

- sem ocorrências

### 1982 Nacional

- tabela publicada x jogos — arghist-pro1980s:193: Gimnasia de Jujuy tabela [16, 4, 5, 7, 23, 26] jogos [16, 3, 6, 7, 22, 26] — a outra tabela publicada (arg82) fecha com os jogos: o erro é desta tabela

### 1983 Metropolitano

- sem ocorrências

### 1983 Nacional

- sem ocorrências

### 1984 Metropolitano

- ogol: 333 jogos casados (edição 22775 do ogol, 342 jogos)
- tabela publicada x jogos — arg84:585: Chacarita Juniors tabela [36, 11, 12, 13, 30, 36] jogos [36, 11, 12, 13, 30, 37] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg84:585: Rosario Central tabela [36, 7, 11, 18, 27, 41] jogos [36, 7, 11, 18, 28, 41] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- data diferente no ogol — Estudiantes x Vélez Sarsfield: RSSSF 1984-11-14, ogol 1984-11-07; fica a da RSSSF

### 1984 Nacional

- ogol: 1 jogos casados (edição 22775 do ogol, 342 jogos)
- tabela publicada x jogos — arghist-pro1980s:560: Ferro Carril Oeste tabela [6, 0, 2, 4, 6, 12] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (arg84) fecha com os jogos: o erro é desta tabela
- placar diferente no ogol — Ferro Carril Oeste x Talleres (1984-05-09): RSSSF 1-0, ogol 1-1; fica o da RSSSF
- data diferente no ogol — Ferro Carril Oeste x Talleres: RSSSF 1984-05-09, ogol 1984-04-29; fica a da RSSSF

### 1985 Nacional

- sem ocorrências

### 1985/86

- ogol: 342 jogos casados (edição 22766 do ogol, 342 jogos)

### 1986/87

- ogol: 378 jogos casados (edição 20787 do ogol, 380 jogos)
- tabela publicada x jogos — arg87:553: River Plate tabela [38, 13, 13, 12, 54, 49] jogos [38, 14, 13, 11, 57, 49] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg87:553: Temperley tabela [38, 7, 13, 18, 28, 48] jogos [38, 6, 13, 19, 28, 51] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- placar diferente no ogol — River Plate x Temperley (1986-08-24): RSSSF 3-1, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Estudiantes x Ferro Carril Oeste (1986-11-09): RSSSF 1-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Estudiantes x Boca Juniors (1986-11-30): RSSSF 0-1, ogol 0-3; fica o da RSSSF
- abandonado/suspenso, sem valer — Estudiantes 0-1 Boca Juniors (1986-11-30): Abandoned at 39'

### 1987/88

- ogol: 379 jogos casados (edição 20696 do ogol, 380 jogos)
- corrigido — Instituto x San Lorenzo (1988-05-08): abandonado antes de começar; "later awarded 0-1" (nota da página); vale na tabela (AR-003)
- decidido fora de campo — Instituto San Lorenzo (1988-05-08)

### 1988/89

- empate decidido nos pênaltis: 2 pontos para o vencedor e 1 para o perdedor; vitória no tempo normal, 3 pontos
- tabela publicada x jogos — arg89:20: Boca Juniors tabela [38, 20, 9, 9, 56, 38] jogos [38, 20, 9, 9, 55, 38] — a diferença vem de Racing Club x Boca Juniors (1988-12-22), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg89:20: Racing Club tabela [38, 13, 16, 9, 47, 41] jogos [38, 13, 16, 9, 47, 40] — a diferença vem de Racing Club x Boca Juniors (1988-12-22), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg89:20: Newell's Old Boys tabela [38, 11, 13, 14, 42, 44] jogos [38, 11, 14, 13, 42, 43] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg89:20: Rosario Central tabela [38, 10, 16, 12, 49, 55] jogos [38, 10, 17, 11, 49, 54] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- W.O./pontos para o visitante — Racing Club 0-0 Boca Juniors (1988-12-22): Suspended in 45'; later Racing Club lost the points (0-1)

### 1989/90

- ogol: 380 jogos casados (edição 22764 do ogol, 380 jogos)
- tabela publicada x jogos — arg90:24: Boca Juniors tabela [38, 11, 21, 6, 49, 35] jogos [38, 11, 21, 6, 49, 36] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg90:24: Rosario Central tabela [38, 16, 13, 9, 45, 36] jogos [38, 17, 13, 8, 46, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg90:24: Newell's Old Boys tabela [38, 12, 14, 12, 40, 43] jogos [38, 12, 14, 12, 41, 43] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg90:345: Independiente tabela [19, 9, 8, 2, 33, 20] jogos [38, 16, 14, 8, 54, 36] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg90:345: River Plate tabela [19, 10, 5, 4, 24, 13] jogos [38, 20, 13, 5, 48, 20] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg90:345: Deportivo Español tabela [19, 10, 3, 6, 32, 25] jogos [38, 12, 7, 19, 39, 53] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg90:345: Rosario Central tabela [19, 8, 7, 4, 26, 21] jogos [38, 17, 13, 8, 46, 35] — sobram 19 jogo(s) do clube na página
- tabela publicada x jogos — arg90:345: Gimnasia La Plata tabela [19, 7, 8, 4, 21, 16] jogos [38, 12, 15, 11, 34, 31] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg90:345: Racing Club tabela [19, 6, 10, 3, 27, 25] jogos [38, 11, 17, 10, 34, 34] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg90:345: Boca Juniors tabela [19, 4, 12, 3, 27, 24] jogos [38, 11, 21, 6, 49, 36] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg90:345: Newell's Old Boys tabela [19, 5, 9, 5, 23, 23] jogos [38, 12, 14, 12, 41, 43] — sobram 19 jogo(s) do clube na página
- tabela publicada x jogos — arg90:345: Unión tabela [19, 4, 11, 4, 28, 29] jogos [38, 10, 16, 12, 40, 43] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg90:345: Talleres tabela [19, 4, 10, 5, 24, 25] jogos [38, 12, 14, 12, 45, 46] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg90:345: Estudiantes tabela [19, 4, 10, 5, 23, 25] jogos [38, 7, 20, 11, 34, 39] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg90:345: Argentinos Juniors tabela [19, 6, 5, 8, 27, 27] jogos [38, 13, 12, 13, 42, 40] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg90:345: Vélez Sarsfield tabela [19, 5, 7, 7, 21, 22] jogos [38, 14, 14, 10, 46, 32] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg90:345: Ferro Carril Oeste tabela [19, 4, 9, 6, 13, 14] jogos [38, 11, 17, 10, 24, 20] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg90:345: Instituto tabela [19, 5, 7, 7, 22, 24] jogos [38, 8, 10, 20, 31, 56] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg90:345: Platense tabela [19, 5, 7, 7, 20, 22] jogos [38, 13, 10, 15, 35, 40] — sobram 19 jogo(s) do clube na página
- tabela publicada x jogos — arg90:345: Deportivo Mandiyú tabela [19, 4, 9, 6, 19, 26] jogos [38, 11, 14, 13, 40, 40] — sobram 19 jogo(s) do clube na página
- tabela publicada x jogos — arg90:345: San Lorenzo tabela [19, 3, 9, 7, 22, 31] jogos [38, 10, 15, 13, 44, 50] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg90:345: Racing de Córdoba tabela [19, 4, 6, 9, 20, 28] jogos [38, 11, 10, 17, 32, 48] — sobram 19 jogo(s) do clube na página
- tabela publicada x jogos — arg90:345: Chaco For Ever tabela [19, 4, 6, 9, 26, 38] jogos [38, 10, 12, 16, 40, 56] — sobram 19 jogo(s) do clube na página
- placar diferente no ogol — Deportivo Mandiyú x Platense (1990-04-08): RSSSF 3-1, ogol 2-1; fica o da RSSSF

### 1990/91

- Apertura 1990 (Newell's) e Clausura 1991 (Boca) eram fases; o título saiu da final entre os dois
- ogol: 381 jogos casados (edição 58944 do ogol, 190 jogos)
- tabela publicada x jogos — arg91:20: Newell's Old Boys tabela [19, 11, 6, 2, 30, 13] jogos [10, 4, 4, 2, 12, 9] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg91:20: River Plate tabela [19, 11, 4, 4, 29, 13] jogos [10, 6, 1, 3, 18, 8] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg91:20: Vélez Sarsfield tabela [19, 8, 8, 3, 27, 18] jogos [10, 4, 5, 1, 15, 12] — faltam 9 jogo(s) do clube na página
- tabela publicada x jogos — arg91:20: Argentinos Juniors tabela [19, 9, 5, 5, 25, 17] jogos [10, 4, 4, 2, 13, 11] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg91:20: Rosario Central tabela [19, 9, 5, 5, 26, 21] jogos [10, 4, 2, 4, 12, 13] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg91:20: Ferro Carril Oeste tabela [19, 7, 9, 3, 19, 16] jogos [10, 3, 4, 3, 6, 9] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg91:20: Estudiantes tabela [19, 6, 8, 5, 17, 17] jogos [10, 1, 4, 5, 8, 13] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg91:20: Boca Juniors tabela [19, 6, 7, 6, 18, 16] jogos [10, 3, 3, 4, 10, 11] — faltam 9 jogo(s) do clube na página
- tabela publicada x jogos — arg91:20: Huracán tabela [19, 5, 9, 5, 20, 19] jogos [10, 3, 2, 5, 9, 11] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg91:20: Independiente tabela [19, 6, 6, 7, 21, 22] jogos [10, 3, 2, 5, 11, 13] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg91:20: San Lorenzo tabela [19, 4, 10, 5, 15, 18] jogos [10, 1, 7, 2, 6, 10] — faltam 9 jogo(s) do clube na página
- tabela publicada x jogos — arg91:33: Racing Club tabela [19, 2, 13, 4, 19, 21] jogos [5, 0, 4, 1, 3, 4] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg91:33: Gimnasia La Plata tabela [19, 2, 12, 5, 15, 20] jogos [5, 1, 3, 1, 6, 5] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg91:33: Platense tabela [19, 5, 6, 8, 16, 22] jogos [5, 1, 2, 2, 3, 5] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg91:33: Chaco For Ever tabela [19, 6, 4, 9, 19, 28] jogos [5, 2, 1, 2, 3, 6] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg91:33: Deportivo Mandiyú tabela [19, 4, 7, 8, 17, 21] jogos [5, 2, 1, 2, 6, 5] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg91:33: Deportivo Español tabela [19, 4, 6, 9, 18, 24] jogos [5, 2, 3, 0, 9, 5] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg91:40: Lanús tabela [19, 3, 5, 11, 11, 27] jogos [0, 0, 0, 0, 0, 0] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg91:544: Platense tabela [19, 5, 9, 5, 11, 16] jogos [19, 4, 10, 5, 10, 16] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg91:544: Lanús tabela [19, 5, 8, 6, 15, 16] jogos [19, 5, 9, 5, 15, 15] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arghist-pro1990s:65: San Lorenzo tabela [19, 4, 10, 5, 15, 18] jogos [19, 5, 10, 4, 16, 17] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- 3º pela lista oficial: River Plate (a tabela o punha em 4º)
- placar diferente no ogol — Boca Juniors x San Lorenzo (1990-12-14): RSSSF 0-1, ogol 0-0; fica o da RSSSF

### 1991/92 Apertura

- ogol: 188 jogos casados (edição 20906 do ogol, 190 jogos)
- data diferente no ogol — Belgrano x Ferro Carril Oeste: RSSSF 1991-09-18, ogol 1991-09-10; fica a da RSSSF
- data diferente no ogol — Boca Juniors x Vélez Sarsfield: RSSSF 1991-09-19, ogol 1991-09-10; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Talleres: RSSSF 1991-09-18, ogol 1991-09-10; fica a da RSSSF
- placar diferente no ogol — Racing Club x River Plate (1991-09-15): RSSSF 0-0, ogol 0-1; fica o da RSSSF
- decidido fora de campo — Racing Club 0-0 River Plate (1991-09-15): Suspended at 73' for the agression to River's goalkeeper River won the points (0-1)

### 1991/92 Clausura

- ogol: 188 jogos casados (edição 20912 do ogol, 190 jogos)
- data diferente no ogol — Newell's Old Boys x Talleres: RSSSF 1992-06-24, ogol 1992-06-14; fica a da RSSSF

### 1992/93 Apertura

- ogol: 189 jogos casados (edição 20882 do ogol, 190 jogos)

### 1992/93 Clausura

- ogol: 178 jogos casados (edição 20885 do ogol, 190 jogos)
- tabela publicada x jogos — arg93:430: Gimnasia La Plata tabela [19, 5, 9, 5, 14, 15] jogos [19, 4, 9, 6, 13, 16] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg93:430: Newell's Old Boys tabela [19, 4, 7, 8, 13, 19] jogos [19, 3, 7, 9, 12, 20] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg93:430: Talleres tabela [19, 2, 7, 10, 13, 31] jogos [19, 4, 7, 8, 15, 29] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arghist-pro1990s:429: Gimnasia La Plata tabela [19, 5, 9, 5, 14, 15] jogos [19, 4, 9, 6, 13, 16] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arghist-pro1990s:429: Newell's Old Boys tabela [19, 4, 7, 8, 13, 19] jogos [19, 3, 7, 9, 12, 20] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arghist-pro1990s:429: Talleres tabela [19, 2, 7, 10, 13, 31] jogos [19, 4, 7, 8, 15, 29] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- linha de nota que repete o jogo Vélez Sarsfield x Boca Juniors (arg93:456): fica de fora
- linha de nota que repete o jogo Newell's Old Boys x Talleres (arg93:460): fica de fora
- linha de nota que repete o jogo Talleres x Gimnasia La Plata (arg93:462): fica de fora
- linha de nota que repete o jogo Vélez Sarsfield x Boca Juniors (arg93:803): fica de fora
- linha de nota que repete o jogo Newell's Old Boys x Talleres (arg93:807): fica de fora
- linha de nota que repete o jogo Talleres x Gimnasia La Plata (arg93:809): fica de fora
- placar diferente no ogol — Vélez Sarsfield x Boca Juniors (1993-03-07): RSSSF 1-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Talleres x River Plate (1993-05-23): RSSSF 2-2, ogol 0-2; fica o da RSSSF
- data diferente no ogol — Deportivo Español x Boca Juniors: RSSSF 1993-05-28, ogol 1993-06-05; fica a da RSSSF
- placar diferente no ogol — Newell's Old Boys x Talleres (1993-06-05): RSSSF 0-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Talleres x Gimnasia La Plata (1993-06-08): RSSSF 1-0, ogol 0-1; fica o da RSSSF
- decidido fora de campo — Vélez Sarsfield 1-1 Boca Juniors (1993-03-07): Later Vélez Sarsfield won the points (1-0)
- decidido fora de campo — Talleres 2-2 River Plate (1993-05-23): at Córdoba][Suspended in 72'; River won the points (0-2)

### 1993/94 Apertura

- ogol: 188 jogos casados (edição 20859 do ogol, 190 jogos)
- data diferente no ogol — Ferro Carril Oeste x Argentinos Juniors: RSSSF 1993-10-04, ogol 1993-09-29; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Deportivo Español: RSSSF 1993-10-04, ogol 1993-09-29; fica a da RSSSF
- data diferente no ogol — Argentinos Juniors x Gimnasia La Plata: RSSSF 1994-03-09, ogol 1994-02-27; fica a da RSSSF

### 1993/94 Clausura

- ogol: 180 jogos casados (edição 20862 do ogol, 190 jogos)
- data diferente no ogol — River Plate x Gimnasia La Plata: RSSSF 1994-04-08, ogol 1994-04-12; fica a da RSSSF

### 1994/95 Apertura

- ogol: 171 jogos casados (edição 20853 do ogol, 190 jogos)
- placar diferente no ogol — Belgrano x Huracán (1994-11-29): RSSSF 1-1, ogol 2-0; fica o da RSSSF

### 1994/95 Clausura

- ogol: 170 jogos casados (edição 20854 do ogol, 190 jogos)
- data diferente no ogol — Huracán x Vélez Sarsfield: RSSSF 1995-04-18, ogol 1995-04-09; fica a da RSSSF

### 1995/96 Apertura

- ogol: 167 jogos casados (edição 5591 do ogol, 190 jogos)
- data diferente no ogol — Estudiantes x San Lorenzo: RSSSF 1995-08-30, ogol 1995-08-20; fica a da RSSSF

### 1995/96 Clausura

- ogol: 170 jogos casados (edição 5590 do ogol, 190 jogos)
- tabela publicada x jogos — arghist-pro1990s:749: Gimnasia La Plata tabela [19, 12, 3, 4, 44, 21] jogos [20, 12, 3, 5, 44, 22] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — arghist-pro1990s:749: Racing Club tabela [19, 8, 5, 6, 26, 25] jogos [20, 9, 5, 6, 27, 25] — sobram 1 jogo(s) do clube na página

### 1996/97 Apertura

- ogol: 157 jogos casados (edição 5915 do ogol, 190 jogos)
- tabela publicada x jogos — arghist-pro1990s:821: Huracán tabela [19, 4, 7, 8, 31, 40] jogos [19, 3, 7, 9, 21, 36] — a outra tabela publicada (arg97) fecha com os jogos: o erro é desta tabela
- data diferente no ogol — Colón x Racing Club: RSSSF 1996-10-12, ogol 1996-10-07; fica a da RSSSF
- data diferente no ogol — Lanús x Estudiantes: RSSSF 1996-10-13, ogol 1996-10-07; fica a da RSSSF
- data diferente no ogol — Huracán de Corrientes x Rosario Central: RSSSF 1996-10-13, ogol 1996-10-07; fica a da RSSSF
- data diferente no ogol — River Plate x Platense: RSSSF 1996-10-13, ogol 1996-10-07; fica a da RSSSF
- data diferente no ogol — Ferro Carril Oeste x Boca Juniors: RSSSF 1996-10-13, ogol 1996-10-07; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x Deportivo Español: RSSSF 1996-10-13, ogol 1996-10-07; fica a da RSSSF
- data diferente no ogol — Independiente x Banfield: RSSSF 1996-10-13, ogol 1996-10-07; fica a da RSSSF
- data diferente no ogol — Vélez Sarsfield x Huracán: RSSSF 1996-10-13, ogol 1996-10-07; fica a da RSSSF
- data diferente no ogol — Gimnasia La Plata x Unión: RSSSF 1996-10-14, ogol 1996-10-07; fica a da RSSSF
- data diferente no ogol — Deportivo Español x Vélez Sarsfield: RSSSF 1996-10-20, ogol 1996-10-14; fica a da RSSSF
- data diferente no ogol — Colón x Lanús: RSSSF 1996-10-20, ogol 1996-10-14; fica a da RSSSF
- data diferente no ogol — Rosario Central x River Plate: RSSSF 1996-10-20, ogol 1996-10-14; fica a da RSSSF
- data diferente no ogol — Banfield x Gimnasia La Plata: RSSSF 1996-10-20, ogol 1996-10-14; fica a da RSSSF
- data diferente no ogol — Racing Club x Unión: RSSSF 1996-10-20, ogol 1996-10-14; fica a da RSSSF
- data diferente no ogol — Boca Juniors x Newell's Old Boys: RSSSF 1996-10-20, ogol 1996-10-14; fica a da RSSSF
- data diferente no ogol — Estudiantes x San Lorenzo: RSSSF 1996-10-19, ogol 1996-10-14; fica a da RSSSF
- data diferente no ogol — Platense x Ferro Carril Oeste: RSSSF 1996-10-21, ogol 1996-10-14; fica a da RSSSF
- data diferente no ogol — Gimnasia La Plata x Huracán: RSSSF 1996-10-26, ogol 1996-10-21; fica a da RSSSF
- data diferente no ogol — Independiente x Deportivo Español: RSSSF 1996-10-27, ogol 1996-10-21; fica a da RSSSF
- data diferente no ogol — Lanús x Racing Club: RSSSF 1996-10-27, ogol 1996-10-21; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Colón: RSSSF 1996-10-27, ogol 1996-10-21; fica a da RSSSF
- data diferente no ogol — Huracán de Corrientes x Estudiantes: RSSSF 1996-10-27, ogol 1996-10-21; fica a da RSSSF
- data diferente no ogol — Unión x Banfield: RSSSF 1996-10-27, ogol 1996-10-21; fica a da RSSSF
- data diferente no ogol — Ferro Carril Oeste x Rosario Central: RSSSF 1996-10-27, ogol 1996-10-21; fica a da RSSSF
- data diferente no ogol — Vélez Sarsfield x Boca Juniors: RSSSF 1996-10-27, ogol 1996-10-21; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x Platense: RSSSF 1996-10-28, ogol 1996-10-21; fica a da RSSSF
- data diferente no ogol — Estudiantes x River Plate: RSSSF 1996-11-01, ogol 1996-10-28; fica a da RSSSF
- data diferente no ogol — Racing Club x Banfield: RSSSF 1996-11-02, ogol 1996-10-28; fica a da RSSSF
- data diferente no ogol — Colón x Huracán de Corrientes: RSSSF 1996-11-02, ogol 1996-10-28; fica a da RSSSF
- data diferente no ogol — Lanús x San Lorenzo: RSSSF 1996-11-03, ogol 1996-10-28; fica a da RSSSF
- data diferente no ogol — Rosario Central x Newell's Old Boys: RSSSF 1996-11-03, ogol 1996-10-28; fica a da RSSSF
- data diferente no ogol — Platense x Vélez Sarsfield: RSSSF 1996-11-03, ogol 1996-10-28; fica a da RSSSF
- data diferente no ogol — Deportivo Español x Gimnasia La Plata: RSSSF 1996-11-03, ogol 1996-10-28; fica a da RSSSF
- data diferente no ogol — Huracán x Unión: RSSSF 1996-11-03, ogol 1996-10-28; fica a da RSSSF
- data diferente no ogol — Boca Juniors x Independiente: RSSSF 1996-11-03, ogol 1996-10-28; fica a da RSSSF
- data diferente no ogol — Deportivo Español x Banfield: RSSSF 1996-11-11, ogol 1996-11-07; fica a da RSSSF
- data diferente no ogol — Banfield x Boca Juniors: RSSSF 1996-11-17, ogol 1996-11-11; fica a da RSSSF
- data diferente no ogol — Ferro Carril Oeste x Lanús: RSSSF 1996-11-17, ogol 1996-11-11; fica a da RSSSF
- data diferente no ogol — Gimnasia La Plata x Rosario Central: RSSSF 1996-11-17, ogol 1996-11-11; fica a da RSSSF
- data diferente no ogol — Huracán x Deportivo Español: RSSSF 1996-11-17, ogol 1996-11-11; fica a da RSSSF
- data diferente no ogol — Huracán de Corrientes x Racing Club: RSSSF 1996-11-16, ogol 1996-11-11; fica a da RSSSF
- data diferente no ogol — River Plate x San Lorenzo: RSSSF 1996-11-17, ogol 1996-11-11; fica a da RSSSF
- data diferente no ogol — Unión x Platense: RSSSF 1996-11-17, ogol 1996-11-11; fica a da RSSSF
- data diferente no ogol — Vélez Sarsfield x Estudiantes: RSSSF 1996-11-17, ogol 1996-11-11; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x Colón: RSSSF 1996-11-18, ogol 1996-11-11; fica a da RSSSF
- data diferente no ogol — Boca Juniors x Huracán: RSSSF 1996-11-24, ogol 1996-11-18; fica a da RSSSF
- data diferente no ogol — Racing Club x Deportivo Español: RSSSF 1996-11-24, ogol 1996-11-18; fica a da RSSSF
- data diferente no ogol — Lanús x Newell's Old Boys: RSSSF 1996-11-24, ogol 1996-11-18; fica a da RSSSF
- data diferente no ogol — Platense x Banfield: RSSSF 1996-11-24, ogol 1996-11-18; fica a da RSSSF
- data diferente no ogol — Colón x Vélez Sarsfield: RSSSF 1996-11-23, ogol 1996-11-18; fica a da RSSSF
- data diferente no ogol — Rosario Central x Unión: RSSSF 1996-11-23, ogol 1996-11-18; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Ferro Carril Oeste: RSSSF 1996-11-22, ogol 1996-11-18; fica a da RSSSF
- data diferente no ogol — Estudiantes x Independiente: RSSSF 1996-11-23, ogol 1996-11-18; fica a da RSSSF
- data diferente no ogol — River Plate x Racing Club: RSSSF 1996-12-04, ogol 1996-11-25; fica a da RSSSF

### 1996/97 Clausura

- ogol: 169 jogos casados (edição 5916 do ogol, 190 jogos)
- tabela publicada x jogos — arg97:414: River Plate tabela [19, 12, 5, 2, 36, 20] jogos [19, 12, 5, 2, 37, 20] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg97:414: Vélez Sarsfield tabela [19, 9, 5, 5, 24, 16] jogos [19, 9, 5, 5, 25, 18] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg97:414: Ferro Carril Oeste tabela [19, 5, 9, 5, 23, 21] jogos [19, 5, 9, 5, 24, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arghist-pro1990s:862: Huracán tabela [19, 4, 9, 6, 21, 28] jogos [19, 5, 7, 7, 22, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1997/98 Apertura

- ogol: 171 jogos casados (edição 5564 do ogol, 190 jogos)
- tabela publicada x jogos — arg98:16: San Lorenzo tabela [19, 9, 5, 5, 42, 32] jogos [19, 9, 6, 4, 42, 32] — a diferença vem de San Lorenzo x Huracán (1997-12-21), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg98:16: Huracán tabela [19, 3, 3, 13, 20, 32] jogos [19, 3, 4, 12, 20, 32] — a diferença vem de San Lorenzo x Huracán (1997-12-21), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- decidido fora de campo — San Lorenzo 0-0 Huracán (1997-12-21): Suspended in 22' due to crowd trouble; awarded 0-0 loss against both

### 1997/98 Clausura

- ogol: 163 jogos casados (edição 5545 do ogol, 190 jogos)
- data diferente no ogol — Vélez Sarsfield x Platense: RSSSF 1998-03-06, ogol 1998-03-10; fica a da RSSSF

### 1998/99 Apertura

- ogol: 170 jogos casados (edição 5530 do ogol, 190 jogos)
- tabela publicada x jogos — arg99:16: Boca Juniors tabela [19, 13, 6, 0, 45, 18] jogos [19, 13, 6, 0, 45, 17] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — arg99:16: Newell's Old Boys tabela [19, 6, 7, 6, 22, 21] jogos [19, 6, 7, 6, 21, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- data diferente no ogol — Ferro Carril Oeste x Estudiantes: RSSSF 1998-10-19, ogol 1998-10-23; fica a da RSSSF
- data diferente no ogol — Unión x San Lorenzo: RSSSF 1998-10-18, ogol 1998-10-23; fica a da RSSSF
- data diferente no ogol — Lanús x Talleres: RSSSF 1998-10-18, ogol 1998-10-23; fica a da RSSSF
- data diferente no ogol — Independiente x Rosario Central: RSSSF 1998-10-18, ogol 1998-10-23; fica a da RSSSF
- data diferente no ogol — Boca Juniors x Vélez Sarsfield: RSSSF 1998-10-18, ogol 1998-10-23; fica a da RSSSF
- data diferente no ogol — Gimnasia La Plata x Colón: RSSSF 1998-10-18, ogol 1998-10-23; fica a da RSSSF
- data diferente no ogol — Huracán x Platense: RSSSF 1998-10-16, ogol 1998-10-23; fica a da RSSSF
- data diferente no ogol — Belgrano x Racing Club: RSSSF 1998-10-17, ogol 1998-10-23; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x Argentinos Juniors: RSSSF 1998-10-18, ogol 1998-10-23; fica a da RSSSF

### 1998/99 Clausura

- ogol: 167 jogos casados (edição 5521 do ogol, 190 jogos)
- tabela publicada x jogos — arg99:377: Unión tabela [19, 8, 5, 6, 29, 27] jogos [18, 8, 4, 6, 29, 27] — a diferença vem de Colón x Unión (1999-04-11), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg99:377: Colón tabela [19, 6, 8, 5, 28, 22] jogos [18, 6, 8, 4, 28, 21] — a diferença vem de Colón x Unión (1999-04-11), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- abandonado/suspenso, sem valer — Colón Unión (1999-04-11): Abandoned 0-0 at 62' because of incidents][Awarded 0-0 to Unión SF and 0-1 to Colón SF

### 1999/00 Apertura

- ogol: 167 jogos casados (edição 5519 do ogol, 190 jogos)
- tabela publicada x jogos — arg00:16: Independiente tabela [19, 6, 7, 6, 19, 21] jogos [18, 5, 7, 6, 16, 19] — a diferença vem de Belgrano x Independiente (1999-12-18), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg00:16: Belgrano tabela [19, 5, 5, 9, 25, 37] jogos [18, 5, 5, 8, 23, 34] — a diferença vem de Belgrano x Independiente (1999-12-18), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- data diferente no ogol — Vélez Sarsfield x Belgrano: RSSSF 1999-08-20, ogol 1999-08-25; fica a da RSSSF
- data diferente no ogol — Racing Club x Chacarita Juniors: RSSSF 1999-08-21, ogol 1999-08-25; fica a da RSSSF
- data diferente no ogol — Gimnasia La Plata x San Lorenzo: RSSSF 1999-08-21, ogol 1999-08-25; fica a da RSSSF
- abandonado/suspenso, sem valer — Belgrano Independiente (1999-12-18): abandoned at 2-3 in 81' due to incidents

### 1999/00 Clausura

- ogol: 167 jogos casados (edição 5513 do ogol, 190 jogos)
- data diferente no ogol — Newell's Old Boys x Boca Juniors: RSSSF 2000-06-03, ogol 2000-05-29; fica a da RSSSF
- data diferente no ogol — Unión x Boca Juniors: RSSSF 2000-06-28, ogol 2000-06-19; fica a da RSSSF
- abandonado/suspenso, sem valer — Lanús Vélez Sarsfield (2000-03-12): abd at 13 seconds when Chilavert (Vélez) was hare-brained by a clamour bomb; continued on Apr 19

### 2000/01 Apertura

- ogol: 184 jogos casados (edição 5445 do ogol, 190 jogos)
- tabela publicada x jogos — arg01:16: Independiente tabela [19, 6, 5, 8, 24, 23] jogos [18, 5, 5, 8, 22, 23] — a diferença vem de Racing Club x Independiente (2000-12-16), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg01:16: Racing Club tabela [19, 1, 8, 10, 12, 30] jogos [18, 1, 8, 9, 12, 28] — a diferença vem de Racing Club x Independiente (2000-12-16), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- data diferente no ogol — Boca Juniors x Gimnasia La Plata: RSSSF 2000-08-12, ogol 2000-08-20; fica a da RSSSF
- abandonado/suspenso, sem valer — Estudiantes Newell's Old Boys (2000-09-24): Abandoned 0-0 at 41' because a clamour bomb was dropped into the playground
- abandonado/suspenso, sem valer — Lanús Racing Club (2000-11-11): Abandoned 2-0 at 45' because of rain
- abandonado/suspenso, sem valer — River Plate Newell's Old Boys (2000-11-11): Abandoned 1-0 at 31' because of rain
- abandonado/suspenso, sem valer — Huracán Belgrano (2000-11-11): Abandoned 1-0 at 45' because of rain
- abandonado/suspenso, sem valer — Racing Club Independiente (2000-12-16): abandoned 0-2 at 81' because of incidents

### 2000/01 Clausura

- ogol: 190 jogos casados (edição 5441 do ogol, 190 jogos)
- ESPN: 82 jogos casados
- decidido fora de campo — Huracán Los Andes (2001-03-04): Abandoned 2-1 at 76' because of incidents Moner, Gabrich - Pieters]        Awarded 2-0

### 2001/02 Apertura

- ogol: 187 jogos casados (edição 5415 do ogol, 190 jogos)
- ESPN: 175 jogos casados
- tabela publicada x jogos — arg02:16: Chacarita Juniors tabela [19, 6, 8, 5, 24, 22] jogos [19, 6, 8, 5, 28, 24] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — arg02:16: Banfield tabela [19, 4, 6, 9, 16, 25] jogos [19, 4, 6, 9, 16, 24] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente no ogol — Huracán x Banfield: RSSSF 2001-11-02, ogol 2001-11-11; fica a da RSSSF
- data diferente no ogol — Talleres x Vélez Sarsfield: RSSSF 2001-11-03, ogol 2001-11-11; fica a da RSSSF
- data diferente no ogol — Rosario Central x Independiente: RSSSF 2001-11-03, ogol 2001-11-11; fica a da RSSSF
- data diferente no ogol — Chacarita Juniors x Colón: RSSSF 2001-11-04, ogol 2001-11-11; fica a da RSSSF
- data diferente no ogol — Lanús x Belgrano: RSSSF 2001-11-04, ogol 2001-11-11; fica a da RSSSF
- data diferente no ogol — Argentinos Juniors x Newell's Old Boys: RSSSF 2001-11-04, ogol 2001-11-11; fica a da RSSSF
- data diferente no ogol — Racing Club x Gimnasia La Plata: RSSSF 2001-11-04, ogol 2001-11-11; fica a da RSSSF
- data diferente no ogol — Estudiantes x Nueva Chicago: RSSSF 2001-11-04, ogol 2001-11-11; fica a da RSSSF
- data diferente no ogol — River Plate x San Lorenzo: RSSSF 2001-11-04, ogol 2001-11-11; fica a da RSSSF
- data diferente no ogol — Unión x Boca Juniors: RSSSF 2001-11-04, ogol 2001-11-11; fica a da RSSSF
- data diferente no ogol — Vélez Sarsfield x Huracán: RSSSF 2001-11-09, ogol 2001-11-18; fica a da RSSSF
- data diferente no ogol — Independiente x Talleres: RSSSF 2001-11-10, ogol 2001-11-18; fica a da RSSSF
- data diferente no ogol — Gimnasia La Plata x Chacarita Juniors: RSSSF 2001-11-10, ogol 2001-11-18; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Lanús: RSSSF 2001-11-10, ogol 2001-11-18; fica a da RSSSF
- data diferente no ogol — Nueva Chicago x Racing Club: RSSSF 2001-11-11, ogol 2001-11-18; fica a da RSSSF
- data diferente no ogol — Banfield x Unión: RSSSF 2001-11-11, ogol 2001-11-18; fica a da RSSSF
- data diferente no ogol — Newell's Old Boys x Rosario Central: RSSSF 2001-11-11, ogol 2001-11-18; fica a da RSSSF
- data diferente no ogol — Belgrano x Argentinos Juniors: RSSSF 2001-11-11, ogol 2001-11-18; fica a da RSSSF
- data diferente no ogol — Boca Juniors x Estudiantes: RSSSF 2001-11-11, ogol 2001-11-18; fica a da RSSSF
- data diferente no ogol — Colón x River Plate: RSSSF 2001-11-11, ogol 2001-11-18; fica a da RSSSF
- data diferente no ogol — Unión x Vélez Sarsfield: RSSSF 2001-11-16, ogol 2001-11-25; fica a da RSSSF
- data diferente no ogol — Argentinos Juniors x San Lorenzo: RSSSF 2001-11-16, ogol 2001-11-25; fica a da RSSSF
- data diferente no ogol — River Plate x Gimnasia La Plata: RSSSF 2001-11-18, ogol 2001-11-25; fica a da RSSSF
- data diferente no ogol — Lanús x Colón: RSSSF 2001-11-18, ogol 2001-11-25; fica a da RSSSF
- data diferente no ogol — Rosario Central x Belgrano: RSSSF 2001-11-18, ogol 2001-11-25; fica a da RSSSF
- data diferente no ogol — Talleres x Newell's Old Boys: RSSSF 2001-11-18, ogol 2001-11-25; fica a da RSSSF
- data diferente no ogol — Huracán x Independiente: RSSSF 2001-11-18, ogol 2001-11-25; fica a da RSSSF
- data diferente no ogol — Estudiantes x Banfield: RSSSF 2001-11-18, ogol 2001-11-25; fica a da RSSSF
- data diferente no ogol — Racing Club x Chacarita Juniors: RSSSF 2001-11-18, ogol 2001-11-25; fica a da RSSSF
- data diferente no ogol — Nueva Chicago x Boca Juniors: RSSSF 2001-11-18, ogol 2001-11-25; fica a da RSSSF
- data diferente no ogol — Chacarita Juniors x Talleres: RSSSF 2002-02-01, ogol 2002-02-05; fica a da RSSSF
- abandonado/suspenso, sem valer — Colón Nueva Chicago (2001-08-25): Abandoned 1-0 at 11' because Migliónico (CSF) injured seriously after goal

### 2001/02 Clausura

- ogol: 187 jogos casados (edição 5401 do ogol, 190 jogos)
- placar diferente no ogol — Newell's Old Boys x Talleres (2002-04-17): RSSSF 3-0, ogol 2-0; fica o da RSSSF
- abandonado/suspenso, sem valer — San Lorenzo Argentinos Juniors (2002-04-16): Abandoned 0-1 at 48' because of rain
- decidido fora de campo — Racing Club Boca Juniors (2002-04-20): Abandoned 2-1 at 89' because of incidents. Awarded 2-0

### 2002/03 Apertura

- ogol: 188 jogos casados (edição 5363 do ogol, 190 jogos)
- data diferente no ogol — Rosario Central x San Lorenzo: RSSSF 2002-07-26, ogol 2002-07-30; fica a da RSSSF
- data diferente no ogol — Banfield x Boca Juniors: RSSSF 2002-08-07, ogol 2002-08-11; fica a da RSSSF
- abandonado/suspenso, sem valer — Banfield Lanús (2002-08-24): Abandoned 0-0 at 8' because of incidents
- abandonado/suspenso, sem valer — Nueva Chicago Estudiantes (2002-11-16): Abandoned 1-0 at 48' because of light cut

### 2002/03 Clausura

- ogol: 188 jogos casados (edição 5361 do ogol, 194 jogos)
- ESPN: 187 jogos casados
- abandonado/suspenso, sem valer — Huracán Olimpo (2003-07-06): Abandoned 0-0 at 75' because of incidents

### 2003/04 Apertura

- ogol: 189 jogos casados (edição 515 do ogol, 190 jogos)
- ESPN: 188 jogos casados
- decidido fora de campo — Boca Juniors 2-0 Chacarita Juniors (2003-08-31): Abandoned 2-0 at 68' because of incidents. Awarded 2-0
- abandonado/suspenso, sem valer — Estudiantes Atlético Rafaela (2003-11-26): Abandoned 0-0 at 57' because of a light cut

### 2003/04 Clausura

- ogol: 184 jogos casados (edição 514 do ogol, 190 jogos)
- ESPN: 190 jogos casados
- data diferente no ogol — Arsenal de Sarandí x Atlético Rafaela: RSSSF 2004-02-12, ogol 2004-02-22; fica a da RSSSF
- data diferente no ogol — Colón x Lanús: RSSSF 2004-02-12, ogol 2004-02-22; fica a da RSSSF
- data diferente no ogol — Olimpo x Talleres: RSSSF 2004-02-12, ogol 2004-02-22; fica a da RSSSF
- data diferente no ogol — River Plate x Estudiantes: RSSSF 2004-02-12, ogol 2004-02-22; fica a da RSSSF
- data diferente no ogol — Rosario Central x Boca Juniors: RSSSF 2004-02-12, ogol 2004-02-22; fica a da RSSSF
- data diferente no ogol — San Lorenzo x Racing Club: RSSSF 2004-02-12, ogol 2004-02-22; fica a da RSSSF

### 2004/05 Apertura

- ogol: 171 jogos casados (edição 550 do ogol, 190 jogos)
- ESPN: 171 jogos casados

### 2004/05 Clausura

- ogol: 171 jogos casados (edição 866 do ogol, 190 jogos)
- ESPN: 170 jogos casados
- tabela publicada x jogos — arg05:537: Boca Juniors tabela [19, 6, 4, 9, 26, 30] jogos [19, 7, 4, 8, 27, 29] — a diferença vem de Almagro x Boca Juniors (2005-07-03), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — arg05:537: Almagro tabela [19, 3, 4, 12, 22, 44] jogos [19, 3, 4, 12, 24, 45] — a diferença vem de Almagro x Boca Juniors (2005-07-03), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- linha lida como jogo e descartada (clube não reconhecido): arg05:1044 «Boca and x loss to Almagro]»
- abandonado/suspenso, sem valer — Banfield Instituto (2005-02-11): abandoned at 0-0 in 78'
- decidido fora de campo — Almagro Boca Juniors (2005-07-03): abandoned at 3-2 due to pitch Lucas Sparapani 2, Fabio Nieto 58, 60;            invasion; awarded 2-3 loss to

### 2005/06 Apertura

- ogol: 171 jogos casados (edição 1140 do ogol, 190 jogos)
- ESPN: 190 jogos casados

### 2005/06 Clausura

- ogol: 171 jogos casados (edição 1232 do ogol, 190 jogos)
- ESPN: 190 jogos casados
- decidido fora de campo — Colón Vélez Sarsfield (2006-03-18): abandoned at 1-3 in 90'; Germán Denis; Lucas Castromán (2), Rolando Zárate]      awarded 0-3
- abandonado/suspenso, sem valer — Independiente Banfield (2006-03-26): abandoned at 1-2 in 80'
- decidido fora de campo — Vélez Sarsfield Boca Juniors (2006-04-23): awarded 0-3; abandoned
- decidido fora de campo — Quilmes River Plate (2006-05-14): awarded 0-3; abandoned

### 2006/07 Apertura

- ogol: 172 jogos casados (edição 1303 do ogol, 191 jogos)
- ESPN: 190 jogos casados
- abandonado/suspenso, sem valer — Godoy Cruz Arsenal de Sarandí (2006-08-12): abandoned at 0-0 in 17'
- abandonado/suspenso, sem valer — Gimnasia La Plata Boca Juniors (2006-09-10): abandoned at 1-0 in 45'
- abandonado/suspenso, sem valer — Colón Vélez Sarsfield (2006-09-16): abandoned at 1-0 in 42'

### 2006/07 Clausura

- ogol: 171 jogos casados (edição 1424 do ogol, 190 jogos)
- ESPN: 190 jogos casados
- decidido fora de campo — Newell's Old Boys River Plate (2007-02-17): awarded 0-2; abandoned
- abandonado/suspenso, sem valer — Nueva Chicago Banfield (2007-04-07): abandoned at 2-1 in 29'
- abandonado/suspenso, sem valer — Lanús Quilmes (2007-04-21): abandoned at 0-0 in 9'

### 2007/08 Apertura

- ogol: 170 jogos casados (edição 1589 do ogol, 190 jogos)
- ESPN: 189 jogos casados
- abandonado/suspenso, sem valer — Gimnasia La Plata Colón (2007-09-12): abandoned at 0-0 in 23'

### 2007/08 Clausura

- ogol: 171 jogos casados (edição 1820 do ogol, 194 jogos)
- ESPN: 190 jogos casados
- abandonado/suspenso, sem valer — River Plate San Martín de San Juan (2008-03-02): abandoned at 3-2
- decidido fora de campo — Racing Club Estudiantes (2008-03-22): awarded 0-2; abandoned at 1-2

### 2008/09 Apertura

- ogol: 170 jogos casados (edição 2304 do ogol, 193 jogos)
- ESPN: 193 jogos casados
- vice pela lista oficial: Tigre (a tabela o punha em 3º)
- abandonado/suspenso, sem valer — Huracán San Lorenzo (2008-11-29): abandoned at 1-0 in 16'

### 2008/09 Clausura

- ogol: 171 jogos casados (edição 4924 do ogol, 190 jogos)
- ESPN: 190 jogos casados
- abandonado/suspenso, sem valer — Godoy Cruz San Martín de Tucumán (2009-03-05): abandoned at 1-1 in 61'

### 2009/10 Apertura

- ogol: 190 jogos casados (edição 9026 do ogol, 190 jogos)
- ESPN: 190 jogos casados

### 2009/10 Clausura

- ogol: 187 jogos casados (edição 12955 do ogol, 190 jogos)
- ESPN: 190 jogos casados
- abandonado/suspenso, sem valer — Banfield Argentinos Juniors (2010-02-03): abandoned at 0-0
- abandonado/suspenso, sem valer — Argentinos Juniors Newell's Old Boys (2010-02-15): abandoned at 0-0 in 66'
- abandonado/suspenso, sem valer — Boca Juniors River Plate (2010-03-21): abandoned at 0-0 in 10'
- abandonado/suspenso, sem valer — Atlético Tucumán Racing Club (2010-04-02): abandoned at 0-0 in 22'

### 2010/11 Apertura

- ogol: 190 jogos casados (edição 15597 do ogol, 190 jogos)
- ESPN: 190 jogos casados

### 2010/11 Clausura

- ogol: 190 jogos casados (edição 19832 do ogol, 191 jogos)
- ESPN: 190 jogos casados
- abandonado/suspenso, sem valer — Vélez Sarsfield San Lorenzo (2011-03-20): abandoned at 0-0 in 10'
- abandonado/suspenso, sem valer — Huracán Estudiantes (2011-05-21): abandoned at 0-2 in 32'

### 2011/12 Apertura

- ogol: 189 jogos casados (edição 23683 do ogol, 190 jogos)
- ESPN: 190 jogos casados
- data diferente no ogol — San Martín de San Juan x San Lorenzo: RSSSF 2011-12-12, ogol 2011-12-18; fica a da RSSSF
- data diferente no ogol — Lanús x Newell's Old Boys: RSSSF 2011-12-12, ogol 2011-12-18; fica a da RSSSF
- data diferente no ogol — Estudiantes x Unión: RSSSF 2011-12-11, ogol 2011-12-18; fica a da RSSSF
- data diferente no ogol — Argentinos Juniors x Olimpo: RSSSF 2011-12-11, ogol 2011-12-18; fica a da RSSSF
- data diferente no ogol — Boca Juniors x All Boys: RSSSF 2011-12-11, ogol 2011-12-18; fica a da RSSSF
- data diferente no ogol — Belgrano x Arsenal de Sarandí: RSSSF 2011-12-11, ogol 2011-12-18; fica a da RSSSF
- data diferente no ogol — Colón x Banfield: RSSSF 2011-12-12, ogol 2011-12-18; fica a da RSSSF
- data diferente no ogol — Atlético Rafaela x Godoy Cruz: RSSSF 2011-12-12, ogol 2011-12-18; fica a da RSSSF
- data diferente no ogol — Vélez Sarsfield x Racing Club: RSSSF 2011-12-12, ogol 2011-12-18; fica a da RSSSF
- data diferente no ogol — Independiente x Tigre: RSSSF 2011-12-12, ogol 2011-12-18; fica a da RSSSF

### 2011/12 Clausura

- ogol: 190 jogos casados (edição 39434 do ogol, 190 jogos)
- ESPN: 190 jogos casados

### 2012/13 Inicial

- ogol: 190 jogos casados (edição 47693 do ogol, 190 jogos)
- ESPN: 188 jogos casados
- abandonado/suspenso, sem valer — Independiente Belgrano (2012-11-14): abandoned at 0-1 in 45'

### 2012/13 Final

- ogol: 189 jogos casados (edição 47694 do ogol, 190 jogos)
- ESPN: 190 jogos casados
- abandonado/suspenso, sem valer — Vélez Sarsfield All Boys (2013-06-08): abandoned at 0-0 in 26m
- abandonado/suspenso, sem valer — Estudiantes Lanús (2013-06-10): abandoned at 2-0 in 45m, at Ciudad de La Plata

### 2012/13 Campeonato

- jogo único entre os campeões do Inicial (Vélez Sarsfield) e do Final (Newell's Old Boys)
- ogol: 1 jogos casados (edição 58572 do ogol, 1 jogos)

### 2013/14 Inicial

- ogol: 190 jogos casados (edição 59668 do ogol, 190 jogos)
- ESPN: 189 jogos casados

### 2013/14 Final

- ogol: 190 jogos casados (edição 66178 do ogol, 190 jogos)
- ESPN: 190 jogos casados

### 2014

- ogol: 189 jogos casados (edição 70023 do ogol, 191 jogos)
- ESPN: 190 jogos casados
- data diferente no ogol — Tigre x Lanús: RSSSF 2014-11-02, ogol 2014-11-12; fica a da RSSSF

### 2015

- ogol: 446 jogos casados (edição 75377 do ogol, 468 jogos)
- ESPN: 450 jogos casados

### 2016

- ogol: 241 jogos casados (edição 93413 do ogol, 242 jogos)
- ESPN: 242 jogos casados
- tabela publicada x jogos — arg2016:45: Godoy Cruz tabela [16, 10, 3, 3, 27, 14] jogos [17, 10, 3, 4, 27, 15] — a outra tabela publicada (arg2016) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — arg2016:62: Estudiantes tabela [16, 9, 5, 2, 25, 11] jogos [17, 10, 5, 2, 26, 11] — a outra tabela publicada (arg2016) fecha com os jogos: o erro é desta tabela

### 2016/17

- ogol: 444 jogos casados (edição 98636 do ogol, 450 jogos)
- ESPN: 446 jogos casados

### 2017/18

- ogol: 377 jogos casados (edição 112999 do ogol, 378 jogos)
- ESPN: 378 jogos casados

### 2018/19

- ogol: 324 jogos casados (edição 125452 do ogol, 325 jogos)
- ESPN: 325 jogos casados

### 2019/20

- campeonato de 23 rodadas; a temporada parou na pandemia durante a Copa de la Superliga (fora do pacote)
- ogol: 276 jogos casados (edição 135982 do ogol, 276 jogos)
- ESPN: 276 jogos casados

### 2021

- ogol: 325 jogos casados (edição 156220 do ogol, 325 jogos)
- ESPN: 325 jogos casados

### 2022

- ogol: 377 jogos casados (edição 165536 do ogol, 378 jogos)
- ESPN: 378 jogos casados

### 2023

- ogol: 377 jogos casados (edição 170240 do ogol, 378 jogos)
- ESPN: 378 jogos casados

### 2024

- ogol: 377 jogos casados (edição 186323 do ogol, 378 jogos)
- ESPN: 378 jogos casados

### 2025 Apertura

- ogol: 254 jogos casados (edição 193795 do ogol, 255 jogos)
- ESPN: 255 jogos casados

### 2025 Clausura

- ogol: 254 jogos casados (edição 193925 do ogol, 255 jogos)
- ESPN: 255 jogos casados

### 2025 Liga

- título dado pela AFA em 20/11/2025 ao 1º da tabela anual (soma das fases de grupos do Apertura e do Clausura); sem jogos próprios: os jogos estão nas edições 2025 Apertura e 2025 Clausura

### 2026 Apertura

- edição de 2026 que já terminou, entra agora (D-01); o Clausura 2026 e a tabela anual entram quando acabarem

