# Campeonato Peruano (1ª divisão) — coleta de dados

Gerado por `python coleta/per-1/importar.py`. Pacote em `data/coleta/per-1/pacote/`.

**Edições:** 109, uma por título de campeão peruano, de 1912 a 2025, como na lista de campeões da RSSSF (`peruchamp.html`) e na Wikipédia em inglês ("List of Peruvian football champions"). Um campeão por ano; sem campeonato de 1922 a 1925 e em 1936 (sem torneio oficial, ano dos Jogos Olímpicos). Apertura, Clausura, Torneo de Verano, Regional, liguillas e finais são fases da edição anual.

**1912-1921 (Liga Peruana de Football):** a liga anterior à Federação Peruana de Futebol (1922). A RSSSF lista esses campeões à parte e não os soma aos títulos nacionais; a Wikipédia em inglês os conta (numera os títulos a partir de 1912). Entram como edições só com o campeão e o vice (da Wikipédia): nenhuma fonte pública tem tabela ou jogos completos (a RSSSF tem 8 jogos soltos de 1912). Se o agente 1 preferir a contagem da RSSSF, basta tirar essas 10 edições.

**Edições sem jogos (18):** 1912-1921, 1970-1974, 1976, 1977 e 1979. Pesquisamos RSSSF, ogol (sem jogos peruanos), Wikipédias em espanhol e inglês (as tabelas de confrontos em inglês desses anos estão incompletas) e ESPN (só de 2005 em diante): nenhuma fonte pública traz os jogos. De 1970 em diante entram com a tabela final de `peruhist.html`.

**Edições com jogos incompletos:** 1926 (torneio suspenso; a Wikipédia tem parte dos jogos), 1982, 1984, 1986, 1988-1991 (anos de Torneo Regional + Descentralizado: a RSSSF tem só as tabelas de parte das fases) e 2003 (as rodadas 16 e 17 do Clausura, jogadas com sub-20 durante a greve, foram anuladas). O que falta está na observação da edição.

**Fora do pacote:** a Copa Perú, a Segunda División e a Intermedia, as ligas de reservas (que davam pontos de bônus de 1931 a 1934), o Torneo del Inca, a Copa Bicentenario, a Supercopa, as liguillas pré-Libertadores e pré-Sudamericana e os jogos de promoção contra clubes de baixo.

**Fontes:** RSSSF (uma página por temporada e a lista de tabelas finais `peruhist.html`, em `data/coleta/per-1/rsssf/`: base de jogos de 1930-1942, 1968, 1969, 1975, 1978, 1980, 1981, 1983, 1984 e 1986 em diante, com fases, grupos, rodadas, datas e autores dos gols); Wikipédia em espanhol (jogos de 1926-1929, 1943-1967, 1982 e 1985, quase sempre em tabela de confrontos, sem rodada nem data; em `data/coleta/per-1/wikipedia/`); ESPN (liga `per.1`, 2005 em diante: hora, estádio, público, gols com minuto e cartões); Wikipédia em inglês (lista de campeões, segunda fonte do campeão e vice de 1912-1921). O ogol não tem jogos peruanos.

**Clubes:** nome pelo qual o clube é conhecido no Brasil (Universitario, Melgar, César Vallejo, Binacional, UTC, CNI, ADT). Homônimos de outros países levam a cidade: Libertad de Trujillo, Internazionale de San Borja. O mesmo clube com outro nome fica com o atual: Federación Universitaria (até 1930) = Universitario; Sport Alianza = Alianza Lima; Sucre FBC = Mariscal Sucre; Inti Gas = Ayacucho; Total Clean = Total Chalaco; Real Garcilaso = Cusco FC; Colegio San Agustín = Deportivo San Agustín; Grau-Estudiantes (2004) = Estudiantes de Medicina. Aurich-Cañaña (fusão de 1994 a 1996) é clube à parte do Juan Aurich.

**Regras:** o placar é o da fonte de base (RSSSF ou Wikipédia). Jogo decidido no tribunal leva o placar dado (`awd`), com o de campo na observação. Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos: 2 por vitória até 1994 e 3 a partir de 1995; de 1931 a 1942 a vitória valia 3, o empate 2 e a derrota 1 (o `ajuste_pontos` desses anos parte dessa conta; de 1931 a 1934 a tabela soma ainda os pontos de bônus da liga de reservas).

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1912 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Lima Cricket | RSSSF (peru1912: ordem) |
| 1913 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Jorge Chávez N°1 | RSSSF (peru1913: ordem) |
| 1914 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Lima Cricket | RSSSF (peru1914: ordem) |
| 1915 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Sport José Gálvez | RSSSF (peru1915: ordem) |
| 1916 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Sport José Gálvez | RSSSF (peru1916: ordem) |
| 1917 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Sport Juan Bielovucic | RSSSF (peru1917: ordem) |
| 1918 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Alianza Lima | RSSSF (peru1918: ordem) |
| 1919 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Alianza Lima | RSSSF (peru1919: ordem) |
| 1920 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Sport Inca | RSSSF (peru1920: ordem) |
| 1921 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Sport Progreso | RSSSF (peru1921: ordem) |
| 1926 | 11 | 27 (27) | 99 | 0 | 0 / 0 | Sport Progreso | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1927 | 8 | 11 (11) | 40 | 0 | 0 / 1 | Alianza Lima | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1928 | 19 | 93 (93) | 369 | 0 | 1 / 2 | Alianza Lima | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1929 | 13 | 75 (75) | 259 | 0 | 0 / 1 | Universitario | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1930 | 12 | 24 (24) | 81 | 26 | 5 / 0 | Atlético Chalaco | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1931 | 12 | 66 (66) | 264 | 0 | 0 / 1 | Alianza Lima | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1932 | 8 | 28 (28) | 116 | 0 | 1 / 0 | Alianza Lima | RSSSF (peru32) |
| 1933 | 10 | 45 (45) | 191 | 0 | 0 / 1 | Alianza Lima | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1934 | 9 | 37 (37) | 98 | 0 | 0 / 1 | Universitario | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1935 | 5 | 9 (6) | 31 | 12 | 1 / 0 | Sport Boys | RSSSF (peru35) |
| 1937 | 10 | 45 (45) | 167 | 0 | 1 / 0 | Sport Boys | RSSSF (peru37) |
| 1938 | 9 | 37 (37) | 133 | 0 | 1 / 0 | Deportivo Municipal | RSSSF (peru38) |
| 1939 | 8 | 56 (56) | 201 | 0 | 1 / 0 | Universitario | RSSSF (peru39) |
| 1940 | 8 | 56 (56) | 201 | 0 | 1 / 0 | Deportivo Municipal | RSSSF (peru40) |
| 1941 | 8 | 56 (56) | 164 | 0 | 1 / 0 | Universitario | RSSSF (peru41) |
| 1942 | 10 | 45 (45) | 157 | 0 | 1 / 0 | Sport Boys | RSSSF (peru42) |
| 1943 | 8 | 56 (56) | 209 | 0 | 1 / 0 | Deportivo Municipal | RSSSF (peruhist) |
| 1944 | 8 | 56 (56) | 235 | 0 | 1 / 0 | Mariscal Sucre | RSSSF (peruhist) |
| 1945 | 8 | 56 (56) | 270 | 0 | 1 / 0 | Universitario | RSSSF (peruhist) |
| 1946 | 8 | 84 (84) | 380 | 0 | 1 / 0 | Universitario | RSSSF (peruhist) |
| 1947 | 8 | 84 (84) | 318 | 0 | 1 / 0 | Atlético Chalaco | RSSSF (peruhist) |
| 1948 | 9 | 108 (108) | 436 | 0 | 0 / 1 | Alianza Lima | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1949 | 8 | 84 (84) | 331 | 0 | 0 / 1 | Universitario | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1950 | 10 | 89 (90) | 357 | 0 | 0 / 1 | Deportivo Municipal | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1951 | 10 | 90 (90) | 414 | 0 | 0 / 1 | Sport Boys | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1952 | 10 | 90 (90) | 391 | 0 | 1 / 0 | Alianza Lima | RSSSF (peruhist) |
| 1953 | 10 | 90 (90) | 326 | 0 | 1 / 0 | Mariscal Sucre | RSSSF (peruhist) |
| 1954 | 10 | 90 (90) | 304 | 0 | 1 / 0 | Alianza Lima | RSSSF (peruhist) |
| 1955 | 10 | 91 (91) | 289 | 0 | 1 / 0 | Alianza Lima | RSSSF (peruhist) |
| 1956 | 10 | 90 (90) | 299 | 0 | 1 / 0 | Sporting Cristal | RSSSF (peruhist) |
| 1957 | 10 | 110 (130) | 352 | 0 | 1 / 0 | Centro Iqueño | RSSSF (peruhist) |
| 1958 | 10 | 110 (130) | 323 | 0 | 0 / 1 | Sport Boys | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1959 | 10 | 110 (130) | 384 | 0 | 0 / 1 | Universitario | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1960 | 10 | 90 (90) | 335 | 0 | 0 / 1 | Universitario | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1961 | 10 | 91 (91) | 277 | 0 | 0 / 1 | Sporting Cristal | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1962 | 10 | 90 (90) | 300 | 0 | 1 / 0 | Alianza Lima | RSSSF (peruhist) |
| 1963 | 10 | 90 (90) | 263 | 0 | 0 / 1 | Alianza Lima | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1964 | 10 | 110 (130) | 303 | 0 | 0 / 1 | Universitario | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1965 | 10 | 110 (130) | 331 | 0 | 0 / 1 | Alianza Lima | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1966 | 14 | 182 (182) | 542 | 0 | 0 / 1 | Universitario | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1967 | 14 | 182 (182) | 468 | 0 | 0 / 1 | Universitario | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1968 | 14 | 186 (186) | 519 | 0 | 1 / 0 | Sporting Cristal | RSSSF (peru68) |
| 1969 | 14 | 135 (135) | 385 | 0 | 3 / 0 | Universitario | RSSSF (peru69) |
| 1970 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Sporting Cristal | RSSSF (peruhist:978+peruhist:988) |
| 1971 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Universitario | RSSSF (peruhist) |
| 1972 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Sporting Cristal | RSSSF (peruhist:1078+peruhist:1059) |
| 1973 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Defensor Lima | RSSSF (peruhist:1120+peruhist:1099) |
| 1974 | 22 | 0 (0) | 0 | 0 | 0 / 0 | Universitario | RSSSF (peruhist:1166+peruhist:1141) |
| 1975 | 18 | 323 (322) | 806 | 0 | 0 / 2 | Alianza Lima | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1976 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Unión Huaral | RSSSF (peruhist) |
| 1977 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Alianza Lima | RSSSF (peruhist:1297+peruhist:1278) |
| 1978 | 16 | 364 (364) | 980 | 0 | 2 / 2 | Alianza Lima | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1979 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Sporting Cristal | RSSSF (peruhist:1404+peruhist:1415+peruhist:1385) |
| 1980 | 17 | 266 (266) | 661 | 592 | 3 / 0 | Sporting Cristal | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1981 | 16 | 307 (307) | 721 | 657 | 5 / 0 | Melgar | RSSSF (peru81) |
| 1982 | 16 | 215 (215) | 445 | 0 | 4 / 3 | Universitario | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1983 | 17 | 287 (287) | 657 | 0 | 2 / 0 | Sporting Cristal | RSSSF (peru83) |
| 1984 | 15 | 186 (186) | 413 | 0 | 1 / 5 | Sport Boys | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1985 | 30 | 528 (528) | 1199 | 0 | 2 / 4 | Universitario | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1986 | 18 | 106 (106) | 260 | 0 | 1 / 6 | Deportivo San Agustín | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1987 | 30 | 542 (542) | 1300 | 0 | 3 / 4 | Universitario | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1988 | 37 | 425 (425) | 984 | 0 | 7 / 2 | Sporting Cristal | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1989 | 14 | 148 (148) | 328 | 0 | 3 / 5 | Unión Huaral | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1990 | 13 | 70 (70) | 185 | 0 | 2 / 2 | Universitario | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1991 | 15 | 28 (28) | 75 | 0 | 0 / 3 | Sporting Cristal | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1992 | 16 | 240 (240) | 641 | 0 | 0 / 1 | Universitario | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1993 | 16 | 240 (240) | 684 | 0 | 0 / 1 | Universitario | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1994 | 16 | 297 (297) | 836 | 0 | 2 / 1 | Sporting Cristal | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1995 | 16 | 296 (296) | 766 | 66 | 2 / 0 | Sporting Cristal | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1996 | 16 | 240 (240) | 636 | 0 | 0 / 1 | Sporting Cristal | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1997 | 14 | 182 (182) | 502 | 0 | 3 / 0 | Alianza Lima | RSSSF (peru97) |
| 1998 | 12 | 267 (267) | 684 | 349 | 4 / 0 | Universitario | RSSSF (peru98:718+peru98:722) |
| 1999 | 13 | 267 (267) | 779 | 31 | 0 / 3 | Universitario | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2000 | 12 | 266 (265) | 769 | 712 | 2 / 2 | Universitario | RSSSF (peru00:784+peru00:795) |
| 2001 | 12 | 268 (268) | 791 | 782 | 2 / 0 | Alianza Lima | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2002 | 12 | 266 (266) | 762 | 753 | 3 / 0 | Sporting Cristal | RSSSF (peru02) |
| 2003 | 12 | 234 (234) | 599 | 592 | 3 / 0 | Alianza Lima | RSSSF (peru03) |
| 2004 | 14 | 366 (365) | 995 | 975 | 2 / 0 | Alianza Lima | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2005 | 13 | 313 (313) | 797 | 776 | 2 / 0 | Sporting Cristal | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2006 | 12 | 268 (268) | 647 | 645 | 3 / 0 | Alianza Lima | RSSSF (peru06) |
| 2007 | 12 | 264 (264) | 653 | 647 | 3 / 0 | Universidad San Martín | RSSSF (peru07) |
| 2008 | 14 | 365 (365) | 896 | 893 | 3 / 0 | Universidad San Martín | RSSSF (peru08) |
| 2009 | 16 | 354 (354) | 886 | 886 | 3 / 0 | Universitario | RSSSF (peru09:714+peru09:909) |
| 2010 | 16 | 354 (354) | 937 | 931 | 4 / 0 | Universidad San Martín | RSSSF (peru2010) |
| 2011 | 16 | 243 (243) | 595 | 565 | 1 / 0 | Juan Aurich | RSSSF (peru2011) |
| 2012 | 16 | 354 (354) | 853 | 846 | 3 / 0 | Sporting Cristal | RSSSF (peru2012:734+peru2012:751) |
| 2013 | 16 | 357 (357) | 871 | 868 | 1 / 2 | Universitario | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2014 | 16 | 245 (245) | 657 | 609 | 3 / 0 | Sporting Cristal | RSSSF (peru2014) |
| 2015 | 17 | 281 (281) | 733 | 695 | 3 / 0 | Melgar | RSSSF (peru2015) |
| 2016 | 16 | 360 (359) | 963 | 880 | 5 / 0 | Sporting Cristal | RSSSF (peru2016) |
| 2017 | 16 | 354 (354) | 943 | 846 | 5 / 0 | Alianza Lima | RSSSF (peru2017) |
| 2018 | 16 | 359 (359) | 985 | 920 | 5 / 0 | Sporting Cristal | RSSSF (peru2018) |
| 2019 | 18 | 310 (310) | 802 | 775 | 3 / 0 | Binacional | RSSSF (peru2019) |
| 2020 | 20 | 285 (285) | 756 | 750 | 5 / 0 | Sporting Cristal | RSSSF (peru2020:919) |
| 2021 | 19 | 238 (238) | 634 | 630 | 2 / 2 | Alianza Lima | RSSSF (peru2021:783) |
| 2022 | 19 | 347 (347) | 937 | 937 | 3 / 0 | Alianza Lima | RSSSF (peru2022) |
| 2023 | 19 | 344 (344) | 873 | 849 | 3 / 0 | Universitario | RSSSF (peru2023) |
| 2024 | 18 | 306 (306) | 813 | 813 | 3 / 0 | Universitario | RSSSF (peru2024) |
| 2025 | 19 | 329 (329) | 853 | 850 | 3 / 0 | Universitario | RSSSF (peru2025) |

## Conferência e correções, edição a edição

### 1912

- sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão

### 1913

- sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão

### 1914

- vice Jorge Chávez N°1 pela página peru1914; a Wikipédia dá o Sport Alianza (2 fontes x 1: fica a RSSSF) (PE-026)
- sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão

### 1915

- sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão

### 1916

- sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão

### 1917

- sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão

### 1918

- sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão

### 1919

- sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão

### 1920

- sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão

### 1921

- sem jogos: campeonato da Liga Peruana (antes da Federação Peruana de Futebol, de 1922); nenhuma fonte pública traz os jogos nem a tabela, só o campeão

### 1926

- sem ocorrências

### 1927

- tabela publicada x jogos — peruhist:90: Atlético Chalaco tabela [3, 2, 0, 1, 5, 4] jogos [3, 2, 0, 1, 4, 4] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:90: Sport Progreso tabela [3, 1, 0, 2, 3, 6] jogos [2, 0, 0, 2, 3, 6] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — peruhist:90: Asociación Alianza tabela [4, 0, 1, 3, 3, 7] jogos [3, 0, 1, 2, 5, 9] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — peruhist:90: Ciclista Lima tabela [2, 0, 0, 2, 2, 6] jogos [0, 0, 0, 0, 0, 0] — faltam 2 jogo(s) do clube na página

### 1928

- tabela publicada x jogos — peruhist:112: Alianza Lima tabela [8, 8, 0, 0, 26, 6] jogos [8, 8, 0, 0, 33, 7] — a outra tabela publicada (peruhist) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peruhist:112: Atlético Chalaco tabela [8, 6, 0, 2, 26, 15] jogos [8, 6, 0, 2, 25, 12] — a outra tabela publicada (peruhist) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peruhist:112: Sportivo Tarapacá Ferrocarril tabela [8, 5, 1, 2, 15, 6] jogos [8, 5, 1, 2, 23, 10] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:112: Sportivo Unión tabela [8, 4, 1, 3, 11, 11] jogos [8, 3, 2, 3, 9, 16] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:112: Alianza Chorrillos tabela [8, 3, 1, 4, 14, 22] jogos [8, 3, 1, 4, 19, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:112: Santa Catalina tabela [8, 3, 0, 5, 11, 13] jogos [8, 3, 0, 5, 15, 18] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:112: Lawn Tennis de la Exposición tabela [8, 2, 1, 5, 12, 15] jogos [8, 2, 1, 5, 15, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:112: Asociación Alianza tabela [8, 1, 2, 5, 10, 17] jogos [8, 1, 3, 4, 10, 15] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:112: Alberto Secada tabela [8, 1, 0, 7, 4, 24] jogos [8, 1, 0, 7, 7, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:124: Sport Progreso tabela [9, 7, 1, 1, 14, 10] jogos [9, 7, 1, 1, 22, 14] — a outra tabela publicada (peruhist) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peruhist:124: Universitario tabela [9, 5, 3, 1, 20, 6] jogos [9, 5, 3, 1, 23, 7] — a outra tabela publicada (peruhist) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peruhist:124: Circolo Sportivo Italiano tabela [9, 5, 3, 1, 15, 8] jogos [9, 5, 3, 1, 18, 9] — a outra tabela publicada (peruhist) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peruhist:124: Ciclista Lima tabela [9, 5, 2, 2, 14, 9] jogos [9, 5, 2, 2, 18, 10] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:124: Unión Buenos Aires tabela [9, 5, 1, 3, 14, 10] jogos [9, 5, 1, 3, 19, 13] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:124: Jorge Washington tabela [9, 4, 1, 4, 21, 9] jogos [9, 4, 1, 4, 23, 16] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:124: Jorge Chávez tabela [9, 4, 1, 4, 12, 10] jogos [9, 4, 1, 4, 15, 15] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:124: Alianza Frigorífico tabela [9, 2, 2, 5, 12, 14] jogos [9, 2, 2, 5, 19, 20] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:124: José Olaya tabela [9, 0, 1, 8, 8, 29] jogos [9, 0, 1, 8, 11, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:124: Unión FC tabela [9, 0, 1, 8, 7, 32] jogos [9, 0, 1, 8, 8, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1929

- a página da Wikipédia traz os jogos duas vezes (lista das rodadas 1-9 e tabela de confrontos); em três confrontos os placares das duas não batem (Universitario x Ciclista Lima, Universitario x Unión Buenos Aires, Hidroaviación x Ciclista Lima) e os dois jogos ficam; falta um jogo do Atlético Chalaco
- tabela publicada x jogos — peruhist:152: Universitario tabela [11, 7, 3, 1, 26, 6] jogos [13, 8, 4, 1, 29, 7] — sobram 2 jogo(s) do clube na página
- tabela publicada x jogos — peruhist:152: Circolo Sportivo Italiano tabela [11, 6, 4, 1, 26, 23] jogos [11, 6, 4, 1, 21, 20] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:152: Hidroaviación tabela [11, 6, 3, 2, 20, 8] jogos [11, 6, 3, 2, 33, 12] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:152: Sportivo Tarapacá Ferrocarril tabela [11, 7, 1, 3, 26, 19] jogos [11, 6, 1, 4, 32, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:152: Ciclista Lima tabela [11, 6, 1, 4, 19, 13] jogos [13, 6, 0, 7, 23, 33] — sobram 2 jogo(s) do clube na página
- tabela publicada x jogos — peruhist:152: Sporting Tabaco tabela [11, 3, 5, 3, 23, 16] jogos [11, 5, 3, 3, 22, 10] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:152: Sport Progreso tabela [11, 4, 3, 4, 19, 23] jogos [11, 3, 4, 4, 18, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:152: Unión Buenos Aires tabela [11, 2, 6, 3, 17, 19] jogos [12, 3, 5, 4, 23, 20] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — peruhist:152: Sportivo Unión tabela [11, 3, 3, 5, 11, 22] jogos [11, 5, 2, 4, 15, 20] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:152: Atlético Chalaco tabela [11, 3, 2, 6, 15, 15] jogos [10, 3, 2, 5, 20, 15] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — peruhist:152: Jorge Chávez tabela [11, 2, 3, 6, 14, 16] jogos [11, 2, 2, 7, 14, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:152: Alianza Chorrillos tabela [11, 0, 0, 11, 8, 44] jogos [11, 0, 0, 11, 9, 51] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- corrigido — Alianza Lima x Alianza Chorrillos (1929-07-07): jogo do Alianza Lima, desclassificado depois da 7ª rodada por não ceder jogadores à seleção (Wikipédia); a tabela final não conta seus jogos
- corrigido — Alianza Lima x Hidroaviación (1929-07-21): jogo do Alianza Lima, desclassificado depois da 7ª rodada por não ceder jogadores à seleção (Wikipédia); a tabela final não conta seus jogos
- corrigido — Alianza Lima x Sportivo Tarapacá Ferrocarril (1929-08-11): jogo do Alianza Lima, desclassificado depois da 7ª rodada por não ceder jogadores à seleção (Wikipédia); a tabela final não conta seus jogos
- corrigido — Alianza Lima x Sport Progreso (1929-08-18): jogo do Alianza Lima, desclassificado depois da 7ª rodada por não ceder jogadores à seleção (Wikipédia); a tabela final não conta seus jogos
- corrigido — Alianza Lima x Unión Buenos Aires (1929-08-25): jogo do Alianza Lima, desclassificado depois da 7ª rodada por não ceder jogadores à seleção (Wikipédia); a tabela final não conta seus jogos
- corrigido — Alianza Lima x Atlético Chalaco (None): jogo do Alianza Lima, desclassificado depois da 7ª rodada por não ceder jogadores à seleção (Wikipédia); a tabela final não conta seus jogos
- corrigido — Circolo Sportivo Italiano x Alianza Lima (None): jogo do Alianza Lima, desclassificado depois da 7ª rodada por não ceder jogadores à seleção (Wikipédia); a tabela final não conta seus jogos
- anulado — Alianza Lima 4-1 Alianza Chorrillos (1929-07-07)
- anulado — Alianza Lima 1-1 Hidroaviación (1929-07-21)
- anulado — Alianza Lima 2-2 Sportivo Tarapacá Ferrocarril (1929-08-11)
- anulado — Alianza Lima 8-0 Sport Progreso (1929-08-18)
- anulado — Alianza Lima 4-0 Unión Buenos Aires (1929-08-25)
- anulado — Alianza Lima 3-2 Atlético Chalaco (s/d)
- anulado — Circolo Sportivo Italiano 1-2 Alianza Lima (s/d)

### 1930

- sem ocorrências

### 1931

- a tabela publicada soma pontos de bônus da liga de reservas (um quarto dos pontos dela); a conferência usa só J V E D GP GC
- tabela publicada x jogos — peru31:18: Atlético Chalaco tabela [11, 6, 2, 3, 27, 25] jogos [11, 6, 2, 3, 26, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru31:18: Sportivo Tarapacá Ferrocarril tabela [11, 4, 2, 5, 20, 25] jogos [11, 4, 2, 5, 19, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru31:18: Unión Buenos Aires tabela [11, 4, 1, 6, 19, 25] jogos [11, 4, 1, 6, 19, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru31:18: Sportivo Unión tabela [11, 4, 1, 6, 18, 20] jogos [11, 4, 1, 6, 18, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- W.O./pontos para o visitante — Universitario Alianza Lima (1931-06-21): awarded, didn’t played, Alianza Lima won 3 pts, Fed. Universitaria loss 1 pt.
- W.O./pontos para o visitante — Ciclista Lima Alianza Frigorífico (1931-07-05): awarded, didn’t played, Alianza Frigorifico won 3 pts, Ciclista Lima loss 1 pt.

### 1932

- placar da RSSSF x Wikipédia em espanhol (PE-017): Ciclista Lima 2-2 Sporting Tabaco (es 0-0): fica a RSSSF, com a qual a tabela publicada fecha

### 1933

- placar da RSSSF x Wikipédia em espanhol (PE-017): Sportivo Unión 1-6 Tarapacá (es 1-3): fica a RSSSF, com a qual a tabela publicada fecha para os dois clubes
- tabela publicada x jogos — peru33:22: Sport Progreso tabela [9, 3, 1, 5, 13, 21] jogos [8, 3, 1, 4, 12, 20] — a diferença vem de Circolo Sportivo Italiano x Sport Progreso (1933-08-13), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — peru33:22: Circolo Sportivo Italiano tabela [9, 1, 3, 5, 11, 14] jogos [8, 1, 3, 4, 10, 13] — a diferença vem de Circolo Sportivo Italiano x Sport Progreso (1933-08-13), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- decidido fora de campo — Circolo Sportivo Italiano Sport Progreso (1933-08-13): originally 1-1, considered W.O. per both

### 1934

- tabela publicada x jogos — peru34:18: Universitario tabela [8, 6, 1, 1, 14, 8] jogos [8, 6, 1, 1, 11, 5] — a diferença vem de Sporting Tabaco x Universitario (1934-09-30), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — peru34:18: Sport Boys tabela [8, 4, 3, 1, 17, 8] jogos [7, 3, 3, 1, 17, 8] — a diferença vem de Sport Boys x Circolo Sportivo Italiano (1934-10-28), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — peru34:18: Sportivo Tarapacá Ferrocarril tabela [8, 3, 3, 2, 11, 7] jogos [7, 2, 3, 2, 11, 7] — a diferença vem de Sportivo Tarapacá Ferrocarril x Circolo Sportivo Italiano (1934-10-07), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — peru34:18: Sporting Tabaco tabela [8, 3, 2, 3, 13, 14] jogos [8, 3, 2, 3, 11, 12] — a diferença vem de Sporting Tabaco x Universitario (1934-09-30), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — peru34:18: Ciclista Lima tabela [8, 1, 1, 6, 6, 20] jogos [8, 1, 1, 6, 5, 19] — a diferença vem de Universitario x Ciclista Lima (1934-11-04), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — peru34:18: Circolo Sportivo Italiano tabela [8, 0, 1, 7, 5, 7] jogos [6, 0, 1, 5, 5, 7] — a diferença vem de Sportivo Tarapacá Ferrocarril x Circolo Sportivo Italiano (1934-10-07), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- W.O./pontos para o visitante — Sporting Tabaco Universitario (1934-09-30): The match finished 2-2, but Universitario were declared winners
- decidido fora de campo — Sportivo Tarapacá Ferrocarril Circolo Sportivo Italiano (1934-10-07): Sportivo Tarapacá FFCC were declared winners
- W.O./pontos para o mandante — Universitario Circolo Sportivo Italiano (1934-10-14): Universitario were declared winners
- W.O./pontos para o mandante — Alianza Lima Circolo Sportivo Italiano (1934-10-21): Alianza Lima were declared winners
- decidido fora de campo — Sport Boys Circolo Sportivo Italiano (1934-10-28)
- W.O./pontos para o mandante — Universitario Ciclista Lima (1934-11-04): The match finished 1-1, but Universitario were declared winners
- W.O./pontos para o mandante — Unión Carbone Circolo Sportivo Italiano (1934-11-18): Unión Carbone were declared winners

### 1935

- corrigido — Alianza Lima x Sportivo Tarapacá Ferrocarril (1935-10-12): vitória dada fora de campo que a FPF não validou: a tabela só conta os jogos disputados (nota da página)
- corrigido — Mariscal Sucre x Universitario (1935-10-13): vitória dada fora de campo que a FPF não validou: a tabela só conta os jogos disputados (nota da página)
- corrigido — Alianza Lima x Universitario (1935-10-27): vitória dada fora de campo que a FPF não validou: a tabela só conta os jogos disputados (nota da página)
- não jogado — Alianza Lima Sportivo Tarapacá Ferrocarril (1935-10-12): Awarded 2-0
- não jogado — Mariscal Sucre Universitario (1935-10-13): Awarded 2-0
- não jogado — Alianza Lima Universitario (1935-10-27): Awarded 2-0

### 1937

- sem ocorrências

### 1938

- sem ocorrências

### 1939

- sem ocorrências

### 1940

- sem ocorrências

### 1941

- placar da RSSSF x Wikipédia em espanhol (PE-017): Telmo Carbajo 0-0 Chalaco (es 1-1): fica a RSSSF, com a qual a tabela publicada fecha

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

- tabela publicada x jogos — peruhist:499: Sporting Tabaco tabela [24, 11, 7, 6, 47, 34] jogos [24, 11, 7, 6, 47, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:499: Ciclista Lima tabela [24, 5, 5, 14, 36, 63] jogos [24, 5, 5, 14, 37, 63] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1949

- tabela publicada x jogos — peruhist:516: Mariscal Sucre tabela [21, 10, 4, 7, 47, 43] jogos [21, 10, 4, 7, 49, 43] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:516: Sporting Tabaco tabela [21, 6, 10, 5, 36, 29] jogos [21, 6, 10, 5, 36, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1950

- tabela publicada x jogos — peruhist:532: Deportivo Municipal tabela [18, 12, 2, 4, 46, 30] jogos [17, 11, 2, 4, 46, 30] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — peruhist:532: Sport Boys tabela [18, 12, 1, 5, 35, 22] jogos [18, 12, 1, 5, 36, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:532: Universitario tabela [18, 9, 2, 7, 30, 25] jogos [17, 9, 2, 6, 30, 25] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — peruhist:532: Atlético Chalaco tabela [18, 7, 3, 8, 33, 31] jogos [18, 7, 3, 8, 34, 32] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1951

- tabela publicada x jogos — peruhist:558: Sport Boys tabela [18, 13, 2, 3, 63, 34] jogos [18, 13, 2, 3, 63, 32] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:558: Mariscal Sucre tabela [18, 9, 2, 7, 45, 40] jogos [18, 9, 2, 7, 44, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:558: Unión Callao tabela [18, 2, 5, 11, 33, 52] jogos [18, 2, 5, 11, 33, 53] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1952

- sem ocorrências

### 1953

- sem ocorrências

### 1954

- sem ocorrências

### 1955

- sem ocorrências

### 1956

- sem ocorrências

### 1957

- sem ocorrências

### 1958

- tabela publicada x jogos — peruhist:685: Sport Boys tabela [22, 10, 6, 6, 31, 25] jogos [22, 10, 6, 6, 31, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:685: Deportivo Municipal tabela [22, 10, 3, 9, 34, 35] jogos [22, 10, 3, 9, 33, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:685: Alianza Lima tabela [22, 8, 6, 8, 40, 29] jogos [22, 8, 6, 8, 41, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1959

- tabela publicada x jogos — peruhist:704: Sport Boys tabela [22, 12, 4, 6, 40, 23] jogos [22, 12, 4, 6, 40, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:704: Centro Iqueño tabela [22, 11, 5, 6, 43, 36] jogos [22, 11, 5, 6, 41, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:704: Mariscal Castilla tabela [22, 6, 7, 9, 36, 41] jogos [22, 6, 7, 9, 36, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1960

- tabela publicada x jogos — peruhist:725: Universitario tabela [18, 11, 3, 4, 39, 26] jogos [18, 11, 3, 4, 39, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:725: Deportivo Municipal tabela [18, 9, 3, 6, 47, 33] jogos [18, 9, 3, 6, 46, 34] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:725: Centro Iqueño tabela [18, 7, 6, 5, 35, 30] jogos [18, 7, 6, 5, 34, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:725: Ciclista Lima tabela [18, 5, 4, 9, 27, 40] jogos [18, 5, 4, 9, 28, 39] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1961

- tabela publicada x jogos — peruhist:742: Alianza Lima tabela [18, 11, 4, 3, 38, 16] jogos [18, 11, 4, 3, 38, 15] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:742: Centro Iqueño tabela [18, 9, 2, 7, 35, 34] jogos [18, 9, 2, 7, 34, 34] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1962

- sem ocorrências

### 1963

- tabela publicada x jogos — peruhist:778: Centro Iqueño tabela [18, 7, 4, 7, 25, 27] jogos [18, 6, 4, 8, 25, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:778: Deportivo Municipal tabela [18, 4, 4, 10, 20, 30] jogos [18, 5, 4, 9, 21, 29] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:778: Mariscal Sucre tabela [18, 5, 1, 12, 21, 41] jogos [18, 5, 1, 12, 21, 42] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1964

- tabela publicada x jogos — peruhist:795: Sporting Cristal tabela [22, 10, 5, 7, 32, 25] jogos [22, 10, 5, 7, 32, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:795: Centro Iqueño tabela [22, 10, 5, 7, 24, 24] jogos [22, 10, 5, 7, 25, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1965

- tabela publicada x jogos — peruhist:816: Alianza Lima tabela [22, 12, 8, 2, 35, 18] jogos [22, 12, 8, 2, 36, 18] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:816: Defensor Lima tabela [22, 10, 5, 7, 44, 28] jogos [22, 10, 5, 7, 43, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:816: Sporting Cristal tabela [22, 10, 5, 7, 41, 31] jogos [22, 10, 5, 7, 41, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:816: Carlos Concha tabela [22, 4, 5, 13, 39, 58] jogos [22, 4, 5, 13, 39, 59] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1966

- tabela publicada x jogos — peruhist:846: Sport Boys tabela [26, 15, 5, 6, 43, 19] jogos [26, 15, 5, 6, 41, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:846: Sporting Cristal tabela [26, 12, 6, 8, 36, 25] jogos [26, 12, 6, 8, 36, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:846: Melgar tabela [26, 12, 4, 10, 41, 32] jogos [26, 12, 4, 10, 43, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:846: Defensor Arica tabela [26, 10, 8, 8, 31, 25] jogos [26, 10, 8, 8, 32, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:846: Mariscal Sucre tabela [26, 7, 7, 12, 30, 40] jogos [26, 7, 7, 12, 29, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:846: Deportivo Municipal tabela [26, 9, 3, 14, 41, 54] jogos [26, 9, 3, 14, 41, 55] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:846: Octavio Espinosa tabela [26, 3, 6, 17, 24, 52] jogos [26, 2, 7, 17, 24, 52] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:846: Carlos Concha tabela [26, 4, 3, 19, 29, 79] jogos [26, 4, 4, 18, 29, 79] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1967

- tabela publicada x jogos — peruhist:872: Alianza Lima tabela [26, 14, 7, 5, 43, 24] jogos [26, 14, 7, 5, 42, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:872: Defensor Lima tabela [26, 14, 5, 7, 41, 27] jogos [26, 14, 5, 7, 40, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:872: Atlético Grau tabela [26, 11, 7, 8, 33, 40] jogos [26, 10, 7, 9, 33, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:872: Juan Aurich tabela [26, 9, 5, 12, 27, 37] jogos [26, 10, 5, 11, 26, 37] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:872: Centro Iqueño tabela [26, 5, 11, 10, 28, 41] jogos [26, 5, 11, 10, 28, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1968

- sem ocorrências

### 1969

- sem ocorrências

### 1970

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)

### 1971

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)

### 1972

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)

### 1973

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)

### 1974

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)

### 1975

- placar da RSSSF x Wikipédia em espanhol (PE-017): Melgar 1-1 Alianza Lima (es 0-1): fica a RSSSF; a tabela publicada também diverge noutros jogos e não decide; falta uma 3ª fonte (jornal da época)
- tabela publicada x jogos — peru75:14: Universitario tabela [34, 16, 10, 8, 43, 38] jogos [35, 15, 10, 10, 44, 41] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — peru75:14: Melgar tabela [34, 12, 14, 8, 48, 39] jogos [34, 12, 15, 7, 48, 39] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru75:14: Juan Aurich tabela [34, 12, 13, 9, 36, 26] jogos [34, 11, 13, 10, 36, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru75:14: Deportivo Junín tabela [34, 15, 7, 12, 57, 52] jogos [33, 15, 7, 11, 57, 52] — a diferença vem de Deportivo Junín x Unión Tumán (1975-10-12), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — peru75:14: Sport Boys tabela [34, 9, 14, 11, 20, 24] jogos [34, 8, 14, 12, 20, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru75:14: Deportivo Municipal tabela [34, 9, 13, 12, 41, 45] jogos [34, 8, 14, 12, 41, 45] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru75:14: Unión Tumán tabela [34, 9, 10, 15, 41, 41] jogos [33, 11, 10, 12, 41, 41] — a diferença vem de Deportivo Junín x Unión Tumán (1975-10-12), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — peru75:14: León de Huánuco tabela [34, 6, 15, 13, 30, 55] jogos [34, 5, 15, 14, 30, 55] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru75:14: Atlético Grau tabela [34, 8, 6, 20, 31, 58] jogos [35, 9, 8, 18, 34, 59] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — peru75:522: Universitario tabela [39, 20, 11, 8, 51, 41] jogos [40, 19, 11, 10, 52, 44] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — peru75:522: Melgar tabela [39, 14, 14, 11, 55, 47] jogos [39, 14, 15, 10, 55, 47] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru75:522: Juan Aurich tabela [39, 14, 13, 12, 41, 35] jogos [39, 13, 13, 13, 41, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru75:522: Deportivo Junín tabela [39, 15, 7, 17, 60, 62] jogos [38, 15, 7, 16, 60, 62] — faltam 1 jogo(s) do clube na página
- decidido fora de campo — Deportivo Junín Unión Tumán (1975-10-12): (1)

### 1976

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)

### 1977

- artilheiros pela lista da RSSSF (perutops), igual à Wikipédia em inglês; a es diverge em alguns anos (1934, 1977, 1980, 1981, 1986-1988): fica a RSSSF até uma 3ª fonte (PE-016)
- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)

### 1978

- tabela publicada x jogos — peru78:16: Universitario tabela [30, 21, 1, 8, 62, 28] jogos [30, 20, 2, 8, 62, 28] — a outra tabela publicada (peru78) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru78:16: CNI tabela [30, 9, 10, 11, 28, 35] jogos [30, 9, 11, 10, 28, 35] — a outra tabela publicada (peru78) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru78:684: Unión Huaral tabela [6, 3, 1, 2, 11, 8] jogos [8, 4, 1, 3, 17, 13] — a outra tabela publicada (peru78) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru78:684: Coronel Bolognesi tabela [6, 3, 1, 2, 10, 8] jogos [8, 4, 1, 3, 12, 12] — a outra tabela publicada (peru78) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru78:684: Juan Aurich tabela [6, 1, 4, 1, 4, 6] jogos [8, 2, 4, 2, 9, 12] — a outra tabela publicada (peru78) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru78:684: Alianza Lima tabela [6, 1, 2, 3, 6, 9] jogos [8, 2, 2, 4, 10, 11] — a outra tabela publicada (peru78) fecha com os jogos: o erro é desta tabela

### 1979

- sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão e a tabela final da RSSSF)

### 1980

- sem ocorrências

### 1981

- placar da RSSSF x Wikipédia em espanhol (PE-017): Torino 0-2 Melgar (es 1-2): fica a RSSSF, com a qual as tabelas publicadas fecham
- decidido fora de campo — Coronel Bolognesi Deportivo Junín (1982-01-31): Awarded 2-0, did not played

### 1982

- tabela publicada x jogos — peruhist:1570: UTC tabela [16, 6, 5, 5, 9, 17] jogos [16, 6, 5, 5, 7, 16] — a outra tabela publicada (peruhist) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peruhist:1570: CNI tabela [16, 5, 2, 9, 17, 19] jogos [16, 5, 2, 9, 16, 17] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:1578: Coronel Bolognesi tabela [16, 8, 7, 1, 24, 10] jogos [16, 8, 7, 1, 24, 9] — a outra tabela publicada (peruhist) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peruhist:1578: Deportivo Junín tabela [16, 2, 5, 9, 11, 25] jogos [16, 2, 5, 9, 10, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:1618: CNI tabela [10, 4, 2, 4, 11, 8] jogos [10, 4, 2, 4, 12, 9] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:1618: Alfonso Ugarte tabela [10, 3, 3, 4, 10, 14] jogos [10, 3, 3, 4, 11, 15] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1983

- decidido fora de campo — Alfonso Ugarte Atlético Torino (1983-05-15): awarded 2-0
- decidido fora de campo — Huancayo FC UTC (1983-07-31): awarded 0-2
- decidido fora de campo — Alfonso Ugarte León de Huánuco (1983-09-03): awarded 2-0
- decidido fora de campo — UTC León de Huánuco (1983-10-30): awarded 2-0
- decidido fora de campo — Juan Aurich Alfonso Ugarte (1983-11-01): awarded 2-0
- decidido fora de campo — UTC Huancayo FC (1983-12-04): awarded 2-0

### 1984

- tabela publicada x jogos — peru84:334: Universitario tabela [2, 0, 2, 0, 1, 1] jogos [3, 1, 2, 0, 3, 2] — a outra tabela publicada (peru84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru84:334: Melgar tabela [2, 0, 2, 0, 1, 1] jogos [3, 0, 2, 1, 2, 3] — a outra tabela publicada (peru84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru84:347: Universitario tabela [18, 10, 6, 2, 28, 14] jogos [10, 2, 4, 4, 11, 13] — a outra tabela publicada (peru84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru84:347: Alianza Lima tabela [18, 8, 8, 2, 28, 16] jogos [10, 3, 4, 3, 7, 8] — a outra tabela publicada (peru84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru84:347: Sporting Cristal tabela [18, 9, 4, 5, 37, 26] jogos [10, 1, 8, 1, 10, 8] — a outra tabela publicada (peru84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru84:347: Sport Boys tabela [18, 8, 5, 5, 31, 22] jogos [10, 4, 5, 1, 14, 7] — a outra tabela publicada (peru84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru84:347: Unión Huaral tabela [18, 6, 4, 8, 17, 22] jogos [10, 3, 2, 5, 10, 20] — a outra tabela publicada (peru84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru84:347: CNI tabela [18, 6, 4, 8, 15, 21] jogos [10, 4, 3, 3, 14, 10] — a outra tabela publicada (peru84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru84:347: Deportivo Municipal tabela [18, 4, 7, 7, 23, 26] jogos [0, 0, 0, 0, 0, 0] — faltam 18 jogo(s) do clube na página
- tabela publicada x jogos — peru84:347: Atlético Chalaco tabela [18, 3, 9, 6, 21, 27] jogos [0, 0, 0, 0, 0, 0] — faltam 18 jogo(s) do clube na página
- tabela publicada x jogos — peru84:347: Juventud La Palma tabela [18, 3, 7, 8, 16, 34] jogos [0, 0, 0, 0, 0, 0] — faltam 18 jogo(s) do clube na página
- tabela publicada x jogos — peru84:347: Octavio Espinosa tabela [18, 3, 6, 9, 10, 18] jogos [0, 0, 0, 0, 0, 0] — faltam 18 jogo(s) do clube na página
- tabela publicada x jogos — peru84:360: Atlético Torino tabela [16, 8, 4, 4, 28, 21] jogos [4, 1, 1, 2, 4, 8] — a outra tabela publicada (peru84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru84:360: Sport Pilsen tabela [16, 7, 5, 4, 28, 25] jogos [4, 2, 1, 1, 6, 5] — a outra tabela publicada (peru84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru84:360: UTC tabela [16, 7, 4, 5, 30, 20] jogos [4, 2, 0, 2, 8, 5] — a outra tabela publicada (peru84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru84:360: Carlos Mannucci tabela [16, 4, 4, 8, 19, 28] jogos [0, 0, 0, 0, 0, 0] — faltam 16 jogo(s) do clube na página
- tabela publicada x jogos — peru84:360: José Gálvez tabela [16, 3, 5, 8, 24, 35] jogos [0, 0, 0, 0, 0, 0] — faltam 16 jogo(s) do clube na página
- tabela publicada x jogos — peru84:368: ADT tabela [16, 9, 4, 3, 26, 12] jogos [2, 1, 1, 0, 3, 2] — a outra tabela publicada (peru84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru84:368: Huancayo FC tabela [16, 6, 5, 5, 18, 15] jogos [2, 0, 1, 1, 2, 3] — a outra tabela publicada (peru84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru84:368: Defensor ANDA tabela [16, 7, 3, 6, 14, 15] jogos [0, 0, 0, 0, 0, 0] — faltam 16 jogo(s) do clube na página
- tabela publicada x jogos — peru84:368: Deportivo Hospital tabela [16, 6, 1, 9, 17, 22] jogos [0, 0, 0, 0, 0, 0] — faltam 16 jogo(s) do clube na página
- tabela publicada x jogos — peru84:376: Melgar tabela [16, 9, 3, 4, 21, 13] jogos [4, 1, 2, 1, 4, 2] — a outra tabela publicada (peru84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru84:376: Diablos Rojos tabela [16, 9, 2, 5, 22, 12] jogos [4, 1, 1, 2, 2, 5] — a outra tabela publicada (peru84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru84:376: Coronel Bolognesi tabela [16, 7, 3, 6, 16, 14] jogos [4, 2, 1, 1, 4, 3] — a outra tabela publicada (peru84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru84:376: Alfonso Ugarte tabela [16, 5, 1, 10, 24, 30] jogos [0, 0, 0, 0, 0, 0] — faltam 16 jogo(s) do clube na página
- tabela publicada x jogos — peru84:376: Cienciano tabela [16, 4, 3, 9, 6, 20] jogos [0, 0, 0, 0, 0, 0] — faltam 16 jogo(s) do clube na página

### 1985

- tabela publicada x jogos — peruhist:1771: Deportivo Municipal tabela [22, 12, 5, 5, 32, 23] jogos [22, 12, 5, 5, 32, 24] — a outra tabela publicada (peruhist) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peruhist:1771: CNI tabela [22, 9, 8, 5, 29, 22] jogos [22, 9, 8, 5, 28, 21] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:1771: Octavio Espinosa tabela [22, 7, 9, 6, 17, 21] jogos [21, 6, 9, 6, 17, 21] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — peruhist:1771: Unión Huaral tabela [22, 4, 12, 6, 23, 24] jogos [22, 4, 12, 6, 24, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:1771: Juventud La Palma tabela [22, 3, 13, 6, 18, 19] jogos [22, 3, 13, 6, 19, 20] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:1771: Deportivo San Agustín tabela [22, 3, 12, 7, 26, 29] jogos [21, 3, 12, 6, 26, 28] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — peruhist:1795: ADT tabela [15, 8, 4, 3, 21, 12] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peruhist:1795: Huancayo FC tabela [15, 6, 3, 6, 13, 13] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peruhist:1795: Deportivo COOPTRIP tabela [15, 5, 5, 5, 11, 13] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peruhist:1795: Defensor ANDA tabela [15, 4, 6, 5, 15, 11] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peruhist:1795: León de Huánuco tabela [15, 3, 7, 5, 14, 15] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peruhist:1795: Chanchamayo FC tabela [15, 4, 5, 6, 13, 23] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peruhist:1804: Alfonso Ugarte tabela [15, 8, 2, 5, 20, 12] jogos [15, 7, 3, 5, 19, 12] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:1804: Cienciano tabela [15, 4, 3, 8, 15, 24] jogos [15, 4, 3, 8, 16, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:1804: Atlético Huracán tabela [15, 3, 4, 8, 16, 27] jogos [15, 3, 4, 8, 16, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:1804: Diablos Rojos tabela [15, 1, 1, 13, 7, 37] jogos [15, 1, 2, 12, 7, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:1848: Universitario tabela [30, 15, 9, 6, 51, 25] jogos [28, 14, 9, 5, 50, 23] — a outra tabela publicada (peruhist) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peruhist:1848: Alianza Lima tabela [30, 15, 9, 6, 36, 18] jogos [28, 14, 9, 5, 34, 17] — a outra tabela publicada (peruhist) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peruhist:1848: Carlos Mannucci tabela [30, 12, 11, 7, 43, 31] jogos [30, 12, 11, 7, 42, 30] — a outra tabela publicada (peruhist) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peruhist:1848: Los Espartanos tabela [30, 11, 13, 6, 33, 21] jogos [30, 11, 13, 6, 31, 20] — a outra tabela publicada (peruhist) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peruhist:1848: Melgar tabela [30, 9, 13, 8, 51, 36] jogos [30, 9, 13, 8, 49, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:1848: Octavio Espinosa tabela [30, 10, 9, 11, 32, 32] jogos [30, 10, 9, 11, 30, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:1848: Coronel Bolognesi tabela [30, 8, 7, 15, 32, 42] jogos [30, 8, 7, 15, 32, 41] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:1848: Deportivo Junín tabela [30, 7, 9, 14, 28, 41] jogos [30, 7, 9, 14, 26, 41] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:1848: ADT tabela [30, 8, 6, 16, 24, 48] jogos [30, 8, 6, 16, 24, 46] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peruhist:1848: Alfonso Ugarte tabela [30, 6, 4, 20, 19, 75] jogos [30, 6, 4, 20, 18, 72] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1986

- tabela publicada x jogos — peru86:34: UTC tabela [15, 10, 2, 3, 31, 11] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (peru86) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru86:34: Hungaritos Agustinos tabela [15, 7, 4, 4, 20, 14] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peru86:34: Atlético Grau tabela [15, 4, 8, 3, 8, 13] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peru86:34: Los Espartanos tabela [15, 4, 5, 6, 14, 23] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peru86:34: Carlos Mannucci tabela [15, 3, 6, 6, 9, 16] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peru86:34: Atlético Torino tabela [15, 3, 3, 9, 17, 22] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peru86:44: Deportivo Pucallpa tabela [15, 9, 2, 4, 20, 15] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peru86:44: ADT tabela [15, 7, 4, 4, 21, 13] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peru86:44: Defensor ANDA tabela [15, 7, 3, 5, 18, 18] jogos [2, 1, 0, 1, 2, 4] — faltam 13 jogo(s) do clube na página
- tabela publicada x jogos — peru86:44: Unión Minas tabela [15, 5, 6, 4, 18, 15] jogos [2, 1, 0, 1, 4, 2] — faltam 13 jogo(s) do clube na página
- tabela publicada x jogos — peru86:44: León de Huánuco tabela [15, 3, 4, 8, 12, 19] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peru86:44: Deportivo Junín tabela [15, 2, 5, 8, 8, 17] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peru86:54: Melgar tabela [15, 12, 2, 1, 24, 6] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peru86:54: Cienciano tabela [15, 6, 4, 5, 21, 16] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peru86:54: Coronel Bolognesi tabela [15, 5, 5, 5, 17, 15] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peru86:54: Alfonso Ugarte tabela [15, 4, 7, 4, 15, 15] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peru86:54: Mariscal Nieto tabela [15, 3, 4, 8, 8, 13] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peru86:54: Atlético Huracán tabela [15, 1, 6, 8, 7, 27] jogos [0, 0, 0, 0, 0, 0] — faltam 15 jogo(s) do clube na página
- tabela publicada x jogos — peru86:107: UTC tabela [10, 6, 1, 3, 14, 14] jogos [10, 5, 3, 2, 15, 14] — a outra tabela publicada (peru86) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru86:107: Juventud La Palma tabela [10, 3, 2, 5, 9, 15] jogos [10, 3, 2, 5, 8, 15] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru86:168: Hungaritos Agustinos tabela [9, 3, 1, 5, 7, 15] jogos [9, 3, 1, 5, 8, 16] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru86:168: Defensor ANDA tabela [9, 1, 4, 4, 5, 18] jogos [9, 1, 4, 4, 4, 17] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru86:228: Atlético Grau tabela [10, 3, 4, 3, 13, 11] jogos [10, 3, 4, 3, 12, 11] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru86:228: Cienciano tabela [10, 3, 2, 5, 11, 18] jogos [10, 3, 2, 5, 12, 18] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- não jogado — Hungaritos Agustinos Defensor ANDA (1987-12-21)

### 1987

- tabela publicada x jogos — peru87:17: Universitario tabela [22, 13, 6, 3, 37, 22] jogos [23, 13, 7, 3, 38, 23] — a outra tabela publicada (peru87) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru87:17: Deportivo San Agustín tabela [22, 11, 6, 5, 33, 27] jogos [23, 11, 7, 5, 34, 28] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — peru87:246: Hungaritos Agustinos tabela [15, 6, 4, 5, 29, 30] jogos [14, 5, 4, 5, 27, 30] — a diferença vem de Hungaritos Agustinos x Atlético Torino (1987-07-26), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — peru87:246: Atlético Torino tabela [15, 4, 5, 6, 18, 23] jogos [14, 4, 5, 5, 18, 21] — a diferença vem de Hungaritos Agustinos x Atlético Torino (1987-07-26), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — peru87:511: Universitario tabela [5, 3, 1, 1, 7, 3] jogos [7, 5, 1, 1, 10, 3] — a outra tabela publicada (peru87) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru87:511: Unión Huaral tabela [5, 3, 1, 1, 8, 4] jogos [7, 3, 1, 3, 8, 7] — a outra tabela publicada (peru87) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru87:562: Alianza Lima tabela [30, 17, 9, 4, 40, 16] jogos [31, 18, 9, 4, 42, 16] — a outra tabela publicada (peru87) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru87:562: Coronel Bolognesi tabela [30, 12, 12, 6, 37, 26] jogos [31, 12, 12, 7, 37, 27] — a outra tabela publicada (peru87) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru87:562: Deportivo Municipal tabela [30, 12, 7, 11, 38, 38] jogos [31, 12, 7, 12, 39, 40] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — peru87:562: Deportivo Pucallpa tabela [30, 8, 6, 16, 24, 48] jogos [30, 8, 6, 16, 24, 49] — a outra tabela publicada (peru87) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru87:562: Hungaritos Agustinos tabela [30, 7, 7, 16, 37, 50] jogos [31, 8, 7, 16, 38, 50] — sobram 1 jogo(s) do clube na página
- decidido fora de campo — Hungaritos Agustinos Atlético Torino (1987-07-26): 2-0 walkover

### 1988

- tabela publicada x jogos — peru88:673: Deportivo Cañaña tabela [3, 2, 0, 1, 3, 3] jogos [1, 0, 0, 1, 0, 2] — a outra tabela publicada (peru88) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru88:673: Alfonso Ugarte tabela [3, 1, 0, 2, 1, 3] jogos [2, 1, 0, 1, 1, 2] — a outra tabela publicada (peru88) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru88:673: Defensor ANDA tabela [3, 0, 0, 3, 1, 5] jogos [2, 0, 0, 2, 0, 3] — a outra tabela publicada (peru88) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru88:699: Deportivo San Agustín tabela [22, 5, 8, 9, 19, 33] jogos [22, 5, 8, 9, 19, 34] — a outra tabela publicada (peru88) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru88:699: Deportivo Municipal tabela [22, 5, 7, 10, 25, 33] jogos [22, 5, 7, 10, 26, 33] — a outra tabela publicada (peru88) fecha com os jogos: o erro é desta tabela
- corrigido — Deportivo Tintaya x None (1988-10-16): linha da tabela de confrontos do Descentralizado "B" (não é jogo)
- corrigido — Diablos Rojos x None (1988-10-16): linha da tabela de confrontos do Descentralizado "B" (não é jogo)

### 1989

- tabela publicada x jogos — peru89:19: Alianza Lima tabela [10, 6, 3, 1, 17, 6] jogos [2, 1, 1, 0, 2, 0] — a outra tabela publicada (peru89) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru89:19: Sporting Cristal tabela [10, 5, 3, 2, 23, 9] jogos [2, 0, 2, 0, 0, 0] — a outra tabela publicada (peru89) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru89:19: Unión Huaral tabela [10, 4, 5, 1, 14, 10] jogos [2, 0, 1, 1, 0, 2] — a outra tabela publicada (peru89) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru89:19: Defensor Lima tabela [10, 3, 5, 2, 17, 12] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru89:19: Universitario tabela [10, 3, 5, 2, 13, 11] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru89:25: Internazionale de San Borja tabela [10, 4, 2, 4, 17, 17] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru89:25: Deportivo San Agustín tabela [10, 3, 3, 4, 10, 15] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru89:25: AELU tabela [10, 2, 2, 6, 10, 21] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru89:25: Octavio Espinosa tabela [10, 1, 4, 5, 7, 19] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru89:25: Deportivo Municipal tabela [10, 1, 3, 6, 10, 20] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru89:275: FBC Aurora tabela [6, 2, 4, 0, 0, 5] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (peru89) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru89:410: Universitario tabela [10, 7, 2, 1, 24, 10] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru89:410: Sporting Cristal tabela [10, 7, 2, 1, 14, 3] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (peru89) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru89:410: Unión Huaral tabela [10, 5, 3, 2, 9, 5] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (peru89) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru89:410: Alianza Lima tabela [10, 4, 3, 3, 13, 9] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (peru89) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru89:410: AELU tabela [10, 5, 1, 4, 14, 14] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru89:410: Defensor Lima tabela [10, 3, 3, 4, 14, 14] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru89:410: Internazionale de San Borja tabela [10, 2, 4, 4, 8, 14] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru89:418: Octavio Espinosa tabela [10, 1, 5, 4, 10, 18] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru89:418: Deportivo Municipal tabela [10, 2, 2, 6, 12, 18] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru89:418: Deportivo San Agustín tabela [10, 1, 4, 5, 6, 18] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- decidido fora de campo — Alfonso Ugarte Deportivo Tintaya (1989-03-23): awarded 2-0
- decidido fora de campo — Diablos Rojos 0-0 Cienciano (1989-04-05): awarded 2-0
- decidido fora de campo — Deportivo Tintaya Alfonso Ugarte (1989-04-16): awarded 2-0

### 1990

- tabela publicada x jogos — peru90:20: Universitario tabela [11, 8, 2, 1, 25, 8] jogos [2, 1, 1, 0, 2, 1] — a outra tabela publicada (peru90) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru90:20: Alianza Lima tabela [11, 5, 5, 1, 16, 8] jogos [0, 0, 0, 0, 0, 0] — a outra tabela publicada (peru90) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru90:20: Unión Huaral tabela [11, 5, 5, 1, 13, 9] jogos [2, 0, 0, 2, 1, 3] — a outra tabela publicada (peru90) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru90:20: Sport Boys tabela [11, 5, 4, 2, 19, 9] jogos [2, 1, 1, 0, 3, 2] — a outra tabela publicada (peru90) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru90:20: Defensor Lima tabela [11, 4, 4, 3, 10, 10] jogos [0, 0, 0, 0, 0, 0] — faltam 11 jogo(s) do clube na página
- tabela publicada x jogos — peru90:20: Sporting Cristal tabela [11, 2, 6, 3, 9, 11] jogos [0, 0, 0, 0, 0, 0] — faltam 11 jogo(s) do clube na página
- tabela publicada x jogos — peru90:20: Deportivo San Agustín tabela [11, 3, 4, 4, 7, 13] jogos [0, 0, 0, 0, 0, 0] — faltam 11 jogo(s) do clube na página
- tabela publicada x jogos — peru90:20: Deportivo Municipal tabela [11, 2, 5, 4, 12, 14] jogos [0, 0, 0, 0, 0, 0] — faltam 11 jogo(s) do clube na página
- tabela publicada x jogos — peru90:20: Internazionale de San Borja tabela [11, 1, 7, 3, 5, 9] jogos [0, 0, 0, 0, 0, 0] — faltam 11 jogo(s) do clube na página
- tabela publicada x jogos — peru90:20: AELU tabela [11, 3, 3, 5, 6, 13] jogos [0, 0, 0, 0, 0, 0] — faltam 11 jogo(s) do clube na página
- tabela publicada x jogos — peru90:20: Octavio Espinosa tabela [11, 1, 4, 6, 11, 22] jogos [0, 0, 0, 0, 0, 0] — faltam 11 jogo(s) do clube na página
- tabela publicada x jogos — peru90:20: Meteor Sport Club tabela [11, 1, 3, 7, 7, 14] jogos [0, 0, 0, 0, 0, 0] — faltam 11 jogo(s) do clube na página
- tabela publicada x jogos — peru90:39: Deportivo Los Ángeles tabela [14, 4, 2, 8, 14, 23] jogos [0, 0, 0, 0, 0, 0] — faltam 14 jogo(s) do clube na página
- decidido fora de campo — Diablos Rojos Atlético Huracán (1990-07-29): awarded 2-0

### 1991

- tabela publicada x jogos — peru91:90: Sport Boys tabela [3, 1, 2, 0, 4, 1] jogos [4, 1, 2, 1, 4, 2] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — peru91:90: Sporting Cristal tabela [3, 1, 2, 0, 2, 1] jogos [4, 2, 2, 0, 3, 1] — sobram 1 jogo(s) do clube na página
- tabela publicada x jogos — peru91:164: León de Huánuco tabela [10, 7, 2, 1, 33, 10] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru91:164: Unión Minas tabela [10, 6, 2, 2, 37, 20] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru91:164: ADT tabela [10, 6, 1, 3, 22, 19] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru91:164: Unión Huayllaspanca tabela [10, 6, 0, 4, 35, 18] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru91:164: Alianza Huánuco tabela [10, 1, 1, 8, 16, 36] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru91:164: Mina San Vicente tabela [10, 1, 0, 9, 10, 50] jogos [0, 0, 0, 0, 0, 0] — faltam 10 jogo(s) do clube na página
- tabela publicada x jogos — peru91:201: Sporting Cristal tabela [3, 2, 0, 1, 5, 3] jogos [3, 2, 0, 1, 4, 3] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru91:201: Sport Boys tabela [3, 1, 1, 1, 3, 3] jogos [3, 1, 1, 1, 4, 3] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- corrigido — Universitario x None (None): confronto de ida e volta numa linha só: entra como dois jogos (EXTRAS)
- corrigido — Alianza Lima x None (None): confronto de ida e volta numa linha só: entra como dois jogos (EXTRAS)
- corrigido — Alianza Atlético x None (1991-11-24): confronto de ida e volta numa linha só: entra como dois jogos (EXTRAS)
- corrigido — Sporting Cristal x None (1991-11-24): confronto de ida e volta numa linha só: entra como dois jogos (EXTRAS)
- corrigido — León de Huánuco x None (1991-11-24): confronto de ida e volta numa linha só: entra como dois jogos (EXTRAS)
- corrigido — Defensor Lima x None (1991-11-24): confronto de ida e volta numa linha só: entra como dois jogos (EXTRAS)
- decidido fora de campo — Unión Minas FBC Aurora (1991-12-22)

### 1992

- tabela publicada x jogos — peru92:16: Sporting Cristal tabela [30, 15, 10, 5, 47, 29] jogos [30, 15, 10, 5, 47, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru92:16: Melgar tabela [30, 14, 9, 7, 48, 28] jogos [30, 14, 9, 7, 49, 29] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru92:16: León de Huánuco tabela [30, 10, 10, 10, 50, 40] jogos [30, 11, 9, 10, 50, 39] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru92:16: UTC tabela [30, 11, 7, 12, 38, 53] jogos [30, 11, 6, 13, 38, 53] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru92:16: Deportivo Municipal tabela [30, 8, 12, 10, 41, 41] jogos [30, 8, 12, 10, 38, 42] — a diferença vem de Deportivo Municipal x Defensor Lima (1992-08-15), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — peru92:16: Alianza Atlético tabela [30, 10, 8, 12, 35, 51] jogos [30, 9, 8, 13, 35, 51] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru92:16: Defensor Lima tabela [30, 7, 12, 11, 38, 46] jogos [30, 7, 11, 12, 40, 44] — a diferença vem de Deportivo Municipal x Defensor Lima (1992-08-15), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — peru92:16: Deportivo San Agustín tabela [30, 7, 12, 11, 34, 45] jogos [30, 7, 12, 11, 33, 44] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru92:16: Carlos Mannucci tabela [30, 6, 13, 11, 26, 31] jogos [30, 7, 13, 10, 26, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru92:16: Deportivo Yurimaguas tabela [30, 2, 7, 21, 30, 56] jogos [30, 2, 7, 21, 31, 57] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- decidido fora de campo — Deportivo Municipal Defensor Lima (1992-08-15): awarded 0-2;

### 1993

- tabela publicada x jogos — peru93:16: Sporting Cristal tabela [30, 16, 5, 9, 68, 33] jogos [30, 16, 5, 9, 67, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru93:16: Alianza Atlético tabela [30, 6, 10, 14, 35, 64] jogos [30, 6, 10, 14, 35, 63] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- decidido fora de campo — Melgar 1-3 Sporting Cristal (s/d): awarded 2-0
- decidido fora de campo — UTC 1-0 Deportivo San Agustín (s/d): awarded 0-2
- decidido fora de campo — UTC 1-1 Alianza Lima (s/d): awarded 0-2

### 1994

- tabela publicada x jogos — peru94:139: Universitario tabela [30, 19, 4, 7, 43, 20] jogos [30, 19, 4, 7, 43, 22] — a outra tabela publicada (peru94) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru94:139: León de Huánuco tabela [30, 17, 4, 9, 43, 36] jogos [30, 17, 4, 9, 45, 36] — a outra tabela publicada (peru94) fecha com os jogos: o erro é desta tabela
- decidido fora de campo — Universitario 0-0 León de Huánuco (1994-05-01): awarded 0-2

### 1995

- placar da RSSSF x Wikipédia em espanhol (PE-017): San Agustín 1-1 Alianza Lima, fase final (es 1-2): fica a RSSSF, com a qual as tabelas publicadas fecham

### 1996

- artilheiros Waldir Sáenz (Alianza Lima) e Adrián Czornomaz (Universitario), 20 gols cada, como as Wikipédias em espanhol e em inglês e o national-football-teams.com; a lista da RSSSF (perutops) dá só Sáenz, com 19 (PE-015)
- tabela publicada x jogos — peru96:14: Alianza Lima tabela [30, 17, 9, 4, 68, 23] jogos [30, 18, 9, 3, 69, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru96:14: Unión Minas tabela [30, 9, 10, 11, 35, 42] jogos [30, 8, 10, 12, 34, 43] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- decidido fora de campo — Universitario Sporting Cristal (s/d): finished 1-1 but awarded 0-2 (after

### 1997

- corrigido — None x None (1997-11-08): nota ("Teams 2-7 qualify for Liguilla Pre-Libertadores"), não é jogo

### 1998

- sem ocorrências

### 1999

- placar da RSSSF x Wikipédia em espanhol (PE-017): Juan Aurich 3-1 Alianza Atlético (es 2-0): fica a RSSSF; a tabela publicada diverge por outro motivo (jogo a menos) e não decide; falta uma 3ª fonte
- tabela publicada x jogos — peru99:34: Alianza Atlético tabela [22, 6, 7, 9, 35, 38] jogos [21, 6, 7, 8, 35, 36] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — peru99:34: Juan Aurich tabela [22, 4, 6, 12, 21, 38] jogos [21, 3, 6, 12, 19, 38] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — peru99:424: Melgar tabela [22, 11, 3, 8, 44, 30] jogos [22, 11, 3, 8, 42, 30] — a diferença vem de Melgar x Juan Aurich (1999-02-13), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — peru99:424: Cienciano tabela [22, 7, 9, 6, 27, 27] jogos [22, 7, 9, 6, 29, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru99:424: Juan Aurich tabela [22, 8, 3, 11, 26, 32] jogos [22, 8, 3, 11, 26, 30] — a diferença vem de Melgar x Juan Aurich (1999-02-13), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — peru99:810: Melgar tabela [44, 20, 9, 15, 79, 57] jogos [44, 20, 9, 15, 77, 57] — a diferença vem de Melgar x Juan Aurich (1999-02-13), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- tabela publicada x jogos — peru99:810: Cienciano tabela [44, 17, 14, 13, 59, 52] jogos [44, 17, 14, 13, 61, 50] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru99:810: Alianza Atlético tabela [44, 13, 13, 18, 71, 66] jogos [43, 13, 13, 17, 71, 64] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — peru99:810: Juan Aurich tabela [44, 12, 9, 23, 47, 70] jogos [43, 11, 9, 23, 45, 68] — a diferença vem de Melgar x Juan Aurich (1999-02-13), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- corrigido — None x None (1999-10-10): nota sobre o jogo anterior (Cienciano 2-0 Sporting Cristal), não é jogo
- decidido fora de campo — Melgar Juan Aurich (1999-02-13): awarded 2-0
- abandonado/suspenso, sem valer — Alianza Lima Sport Boys (1999-10-23): abd at 1-1 in 28'

### 2000

- placar da RSSSF x Wikipédia em espanhol (PE-017): Deportivo Wanka 3-2 Alianza Lima e Wanka 1-0 Universitario (es 0-1 e 0-0): fica a RSSSF, com a qual as tabelas publicadas fecham para o Wanka
- tabela publicada x jogos — peru00:411: Sporting Cristal tabela [22, 15, 5, 2, 48, 24] jogos [22, 15, 5, 2, 48, 25] — a outra tabela publicada (peru00) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru00:411: Unión Minas tabela [22, 9, 4, 9, 33, 37] jogos [22, 9, 4, 9, 35, 37] — a outra tabela publicada (peru00) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru00:411: Juan Aurich tabela [22, 4, 5, 13, 22, 50] jogos [22, 4, 5, 13, 22, 51] — a outra tabela publicada (peru00) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru00:784: Sporting Cristal tabela [44, 22, 12, 10, 88, 55] jogos [44, 22, 12, 10, 88, 56] — a outra tabela publicada (peru00) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru00:784: Unión Minas tabela [44, 19, 7, 18, 61, 60] jogos [44, 19, 7, 18, 63, 60] — a outra tabela publicada (peru00) fecha com os jogos: o erro é desta tabela
- abandonado/suspenso, sem valer — Universitario Unión Minas (2000-04-02): abd in 18´ at 1-0 after fan got killed
- decidido fora de campo — Sport Boys Unión Minas (2000-10-10): awarded 2-0; abandoned at 1-1 in 44' after protests against decision to retake (missed)

### 2001

- sem ocorrências

### 2002

- sem ocorrências

### 2003

- corrigido — Estudiantes de Medicina x Melgar (2003-11-09): rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- corrigido — Universitario x Deportivo Wanka (2003-11-09): rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- corrigido — Unión Huaral x Coronel Bolognesi (2003-11-09): rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- corrigido — Sport Boys x Alianza Atlético (2003-11-14): rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- corrigido — Deportivo Wanka x Cienciano (2003-11-22): rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- corrigido — Alianza Lima x Estudiantes de Medicina (2003-11-22): rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- corrigido — Sporting Cristal x Universitario (2003-11-22): rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- corrigido — Alianza Atlético x Atlético Universidad (2003-11-23): rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- corrigido — Melgar x Unión Huaral (2003-11-23): rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante a greve dos profissionais; o campeonato foi encerrado no fim de novembro e as tabelas publicadas não contam esses jogos
- decidido fora de campo — Deportivo Wanka Alianza Lima (2003-03-02): awarded 0-2; Wanka suspended
- anulado — Estudiantes de Medicina 1-3 Melgar (2003-11-09)
- anulado — Universitario 1-2 Deportivo Wanka (2003-11-09)
- anulado — Unión Huaral 2-1 Coronel Bolognesi (2003-11-09)
- anulado — Sport Boys 1-0 Alianza Atlético (2003-11-14)
- não jogado — Cienciano Alianza Lima (2003-11-14)
- não jogado — Atlético Universidad Sporting Cristal (2003-11-14)
- anulado — Deportivo Wanka 0-1 Cienciano (2003-11-22)
- anulado — Alianza Lima 7-1 Estudiantes de Medicina (2003-11-22)
- anulado — Sporting Cristal 4-0 Universitario (2003-11-22)
- anulado — Alianza Atlético 5-3 Atlético Universidad (2003-11-23)
- anulado — Melgar 0-0 Unión Huaral (2003-11-23)
- não jogado — Coronel Bolognesi Sport Boys (2003-11-23)

### 2004

- placar da RSSSF x Wikipédia em espanhol (PE-017): Cienciano 2-0 Universitario, Clausura (es 1-1): fica a RSSSF, com a qual a tabela do Clausura fecha; o 1-1 da es é o jogo do Apertura (abandonado e mantido, agora contado)
- corrigido — Cienciano x Universitario (2004-05-23): Cienciano 1-1 Universitario, abandonado nos acréscimos (Universitario com 6 jogadores): o resultado ficou, como contam a tabela do Apertura (26 jogos, Cienciano 53-28, Universitario 31-25) e a Wikipédia em espanhol (PE-017)
- abandonado/suspenso, sem valer — Alianza Atlético Cienciano (2004-08-14): abandoned at 1-3 at 46'
- decidido fora de campo — Cienciano Estudiantes de Medicina (2004-11-21): awarded 2-0, Grau dns
- decidido fora de campo — Estudiantes de Medicina Alianza Lima (2004-12-15): awarded 0-2, Grau withdrew
- decidido fora de campo — Deportivo Wanka Universidad San Martín (2004-12-17): awarded 0-2, originally 1-0;
- decidido fora de campo — Unión Huaral Estudiantes de Medicina (2004-12-19): awarded 2-0, Grau withdrew
- decidido fora de campo — Deportivo Wanka Estudiantes de Medicina (2004-12-22): awarded 2-0, Grau withdrew
- decidido fora de campo — Estudiantes de Medicina Melgar (2004-12-26): awarded 0-2, Grau withdrew

### 2005

- ESPN: 153 jogos casados

### 2006

- ESPN: 264 jogos casados
- decidido fora de campo — Unión Huaral Universidad San Martín (2006-08-26): awarded 0-2; Huaral

### 2007

- ESPN: 264 jogos casados
- decidido fora de campo — Sport Áncash Coronel Bolognesi (2007-04-21): awarded 2-0, Bolognesi dns

### 2008

- ESPN: 364 jogos casados
- decidido fora de campo — Atlético Minero Sport Áncash (2008-04-13): awarded 3-0; originally 1-1

### 2009

- ESPN: 353 jogos casados

### 2010

- ESPN: 347 jogos casados
- decidido fora de campo — José Gálvez León de Huánuco (2010-03-21): awarded 0-3 as José Gálvez were suspended for financial reasons
- decidido fora de campo — Cienciano José Gálvez (2010-07-18): awarded 0-3, as Cienciano were suspended for financial reasons

### 2011

- ESPN: 241 jogos casados
- decidido fora de campo — CNI Sport Boys (2011-04-23): awarded 3-0; originally 0-0 but Sport Boys were suspended for financial reasons
- decidido fora de campo — Sporting Cristal Universitario (2011-05-01): awarded 3-0; originally 0-0 but Universitario were suspended for financial reasons
- decidido fora de campo — Sport Boys Sport Huancayo (2011-05-11): awarded 0-3, as Sport Boys were suspended for financial reasons
- decidido fora de campo — Universitario CNI (2011-08-06): awarded 0-3; originally 2-0 but Universitario were suspended for financial reasons
- decidido fora de campo — Sporting Cristal Sport Boys (2011-08-07): awarded 3-0; originally 1-1 but Sport Boys were suspended for financial reasons
- decidido fora de campo — Universitario Melgar (2011-09-11): awarded 0-3, as Universitario were suspended for financial reasons
- decidido fora de campo — Alianza Atlético 0-0 Universitario (2011-10-17): awarded 3-0; originally 0-0 but Universitario were suspended for financial reasons
- decidido fora de campo — CNI Alianza Lima (2011-10-22): awarded 3-0; originally 0-1 but Alianza Lima submitted incomplete payroll of the players
- decidido fora de campo — Unión Comercio Cobresol (2011-10-29): awarded 3-0; originally 1-1 but Cobresol FBC submitted incomplete payroll of the players
- decidido fora de campo — César Vallejo Cobresol (2011-11-05): awarded 3-0; originally 1-0 but Cobresol FBC submitted incomplete payroll of the players

### 2012

- ESPN: 354 jogos casados
- decidido fora de campo — Melgar Universidad San Martín (2012-02-19): awarded 3-0; Melgar won by walk-over; U.San Martin did not show because of disagreements with the FPF, ADFP and SAFAP.

### 2013

- ESPN: 354 jogos casados
- tabela publicada x jogos — peru2013:32: Cusco FC tabela [30, 17, 7, 6, 41, 20] jogos [30, 17, 7, 6, 41, 17] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — peru2013:721: Cusco FC tabela [44, 22, 12, 10, 63, 39] jogos [44, 22, 12, 10, 63, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- decidido fora de campo — Cusco FC Sporting Cristal (2013-07-24): awarded 3-0; Sporting Cristal did not show
- abandonado/suspenso, sem valer — Melgar Sporting Cristal (2013-10-06): abandoned at 0-0 in 65'

### 2014

- ESPN: 243 jogos casados

### 2015

- ESPN: 281 jogos casados

### 2016

- ESPN: 358 jogos casados
- abandonado/suspenso, sem valer — Alianza Lima Universitario (2016-04-01): abandoned at 1-1 in 49' due to crowd trouble
- decidido fora de campo — Melgar 2-1 Deportivo Municipal (2016-09-11): awarded 3-0; Dep. Municipal used 5 foreign players,
- decidido fora de campo — Alianza Lima 1-1 Universitario (2016-09-17): awarded 3-0; Universitario used Juan Pino (the player was
- decidido fora de campo — Universitario Alianza Lima (2016-11-03): awarded 0-3, Alianza Lima won, res.129-CJ/ADFP-2016
- decidido fora de campo — Cusco FC César Vallejo (2016-11-20): awarded 0-3, originally 2-0

### 2017

- ESPN: 354 jogos casados
- corrigido — Melgar x UTC (2017-05-21): final do Torneo de Verano (maio), não a do campeonato (PE-013)
- corrigido — UTC x Melgar (2017-05-31): final do Torneo de Verano (maio), não a do campeonato (PE-013)
- decidido fora de campo — Sport Huancayo Cusco FC (2017-04-23): awarded 0-3; originally 1-0, Huancayo

### 2018

- ESPN: 358 jogos casados
- corrigido — Sport Huancayo x Sporting Cristal (2018-05-06): final do Torneo de Verano (abril), não a do campeonato (PE-013)
- corrigido — Sporting Cristal x Sport Huancayo (2018-05-12): final do Torneo de Verano (abril), não a do campeonato (PE-013)
- decidido fora de campo — UTC Sporting Cristal (2018-02-02): Awarded 0-3, CJ/FPF
- decidido fora de campo — Ayacucho Comerciantes Unidos (2018-05-18): awarded 3-0
- decidido fora de campo — Comerciantes Unidos Ayacucho (2018-09-01): awarded 0-3; abandoned at 0-2 at half-time
- abandonado/suspenso, sem valer — Alianza Lima Sporting Cristal (2018-09-16): abandoned at 1-2 in 65' due to crowd trouble

### 2019

- ESPN: 310 jogos casados
- decidido fora de campo — Universidad San Martín Unión Comercio (2019-08-31): awarded 3-0, originally 1-2}

### 2020

- ESPN: 283 jogos casados
- decidido fora de campo — Alianza Lima Binacional (2020-08-10): awarded 3-0][Nacional Stadium, Lima
- decidido fora de campo — Cienciano Atlético Grau (2020-08-18): awarded 3-0, initially 0-0][Alberto Gallardo Stadium, Lima

### 2021

- ESPN: 237 jogos casados
- tabela publicada x jogos — peru2021:333: Cienciano tabela [17, 6, 7, 4, 25, 21] jogos [17, 6, 8, 3, 27, 20] — a outra tabela publicada (peru2021) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru2021:333: Cusco FC tabela [17, 5, 3, 9, 31, 34] jogos [17, 4, 4, 9, 30, 36] — a outra tabela publicada (peru2021) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru2021:783: Cienciano tabela [26, 10, 9, 7, 39, 33] jogos [26, 10, 10, 6, 41, 32] — a outra tabela publicada (peru2021) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — peru2021:783: Cusco FC tabela [26, 6, 8, 12, 43, 47] jogos [26, 5, 9, 12, 42, 49] — a outra tabela publicada (peru2021) fecha com os jogos: o erro é desta tabela
- corrigido — Alianza Atlético x Carlos Stein (2021-03-15): jogo anulado pela FPF: o FC Carlos Stein foi rebaixado por decisão do CAS (nota da página)
- corrigido — Cusco FC x Cienciano (2021-08-27): Cusco FC 2-2 Cienciano: o TAS (21/01/2022) anulou a vitória dada ao Cusco (PE-007)
- anulado — Alianza Atlético 0-0 Carlos Stein (2021-03-15): Ivan Elias Moreno Stadium, Lima] [**

### 2022

- ajustes de pontos da tabela publicada (Alianza Lima +2, Ayacucho +1, César Vallejo -2) sem terceira fonte que explique a origem; ficam os da tabela (PE-018)
- ESPN: 346 jogos casados
- abandonado/suspenso, sem valer — Universitario Sport Huancayo (2022-10-23): Monumental “U” Stadium, Lima; abd in 30´ at 1-0 because a fan died in the stands

### 2023

- ESPN: 344 jogos casados
- decidido fora de campo — Cusco FC Sport Huancayo (2023-02-03): 0-3][Inca Garcilaso de la Vega Stadium, Cusco (*)
- decidido fora de campo — Atlético Grau Melgar (2023-02-04): 3-0][Municipal Stadium, Bernal (*)
- decidido fora de campo — UTC Cienciano (2023-02-04): 3-0][Héroes de San Ramón Stadium, Cajamarca (*)
- decidido fora de campo — Deportivo Garcilaso Binacional (2023-02-04): 3-0][Inca Garcilaso de la Vega Stadium, Cusco (*)
- decidido fora de campo — Sporting Cristal Alianza Lima (2023-02-05): 3-0][Alberto Gallardo Stadium, Lima (*)
- decidido fora de campo — Deportivo Municipal Carlos Mannucci (2023-02-07): 0-3][Ivan Elias Moreno Stadium, Lima (*)
- decidido fora de campo — Carlos Mannucci Deportivo Municipal (2023-07-10): awarded 3-0][Mansiche Stadium, Trujillo
- decidido fora de campo — Deportivo Municipal Atlético Grau (2023-08-13): awarded 0-3][Ivan Elias Moreno Stadium, Lima

### 2024

- ESPN: 306 jogos casados

### 2025

- ESPN: 328 jogos casados
- corrigido — Binacional x UTC (2025-07-25): jogo do Binacional no Clausura: o clube foi desfiliado pela FPF por ordem judicial e todos os seus jogos do Clausura foram anulados (nota da página)
- corrigido — Cusco FC x Binacional (2025-07-31): jogo do Binacional no Clausura: o clube foi desfiliado pela FPF por ordem judicial e todos os seus jogos do Clausura foram anulados (nota da página)
- corrigido — Binacional x Alianza Atlético (2025-08-06): jogo do Binacional no Clausura: o clube foi desfiliado pela FPF por ordem judicial e todos os seus jogos do Clausura foram anulados (nota da página)
- corrigido — Juan Pablo II x Binacional (2025-08-10): jogo do Binacional no Clausura: o clube foi desfiliado pela FPF por ordem judicial e todos os seus jogos do Clausura foram anulados (nota da página)
- corrigido — Binacional x Sporting Cristal (2025-08-16): jogo do Binacional no Clausura: o clube foi desfiliado pela FPF por ordem judicial e todos os seus jogos do Clausura foram anulados (nota da página)
- corrigido — Ayacucho x Comerciantes Unidos (2025-11-08): Ayacucho 1-0 Comerciantes Unidos em campo; as tabelas publicadas (Clausura e acumulada) contam 0-3, vitória dada ao Comerciantes Unidos (a página não traz a nota)
- anulado — Binacional 0-0 UTC (2025-07-25): Guillermo Briceño Rosamedina Stadium, Juliaca] [*
- anulado — Cusco FC 2-0 Binacional (2025-07-31): Inca Garcilaso de la Vega, Cusco] [*
- anulado — Binacional 2-0 Alianza Atlético (2025-08-06): Guillermo Briceño Rosamedina Stadium, Juliaca] [*
- anulado — Juan Pablo II 0-0 Binacional (2025-08-10): Juan Pablo II Field, Chongoyape] [*
- anulado — Binacional 1-3 Sporting Cristal (2025-08-16): Guillermo Briceño Rosamedina Stadium, Juliaca] [*
- decidido fora de campo — Ayacucho 1-0 Comerciantes Unidos (2025-11-08)

