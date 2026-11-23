# Campeonato Venezuelano (1ª divisão) — coleta de dados

Gerado por `python coleta/ven-1/importar.py`. Pacote em `data/coleta/ven-1/pacote/`.

**Edições:** 106, uma por título de 1921 (temporada 1920/21) a 2025, como na lista de campeões da RSSSF (`venezchamp.html`, 106 títulos). A Wikipédia em inglês (página "Liga FUTVE") tem os mesmos campeões, menos o Torneo de Adecuación 2015, que ela não conta como temporada; aqui ele entra, como na RSSSF. Era amadora (1921-1956), profissional em ano fechado (1957-1986), calendário europeu de 1986/87 a 2014/15 (Apertura, Clausura, liguillas e finais são fases do ano), Adecuación 2015 e Liga FUTVE (2016 em diante, Apertura e Clausura com final entre os vencedores).

**Fora do pacote:** a 2ª e a 3ª divisões, a Copa Venezuela (salvo quando foi a 1ª fase da temporada: 1993/94, 1994/95, 1995/96 e 2000/01), as outras copas (Copa Caracas, Liga Mayor, de las Naciones, Cuatricentenario, Valencia, de Campeones, Bicentenario), os jogos de promoção e os playoffs da Sudamericana e da Conmebol.

**Edições sem jogos (7):** 1922, 1924, 1931, 1938, 1939, 1949 e 1950: a RSSSF não tem página desses anos; entram com o campeão e o vice da lista.

**Edições com jogos incompletos:** a era amadora (1921-1956), salvo 1940, 1955 e 1956: a RSSSF traz só parte dos jogos da liga (ou só o campeão e a classificação; os jogos das copas da mesma página ficam de fora); 1993/94 (o Apertura, que era a Copa Venezuela, só tem as tabelas dos grupos, e 8 jogos da liga estão sem placar); 1994/95 (o Torneo Iniciación só tem as tabelas). Nelas a classificação é a tabela publicada, sem conferência; o que falta está na observação da edição.

**Fontes:** RSSSF (uma página por temporada, `venezYY.html` / `venezAAAA.html`, em `data/coleta/ven-1/rsssf/`: base de jogos, com fases, grupos, rodadas, datas e autores dos gols; lista de campeões `venezchamp.html`; artilheiros `veneztops.html`, 1957-2007/08); ESPN (liga `ven.1`, 2005 em diante: hora, estádio, público, gols com minuto e cartões; jogos do Clausura 2011, de 2011/12 e de 2025, que a RSSSF tem só em parte ou só nas tabelas); Wikipédia em inglês (lista de campeões: segunda fonte do campeão e do vice e fonte dos artilheiros depois de 2007/08).

**Clubes:** nome pelo qual o clube é conhecido (Caracas FC, Deportivo Táchira, Estudiantes de Mérida, Mineros de Guayana). O mesmo clube com outro nome, como na lista de campeões da RSSSF: Unión Atlético Táchira (1985-1999) é o Deportivo Táchira; ItalChacao e Deportivo Petare são o Deportivo Italia; o Atlético Zulia (1996/97 e 1997/98) é a Universidad de Los Andes (ULA); o Internacional de Lara (1998/99) é o Trujillanos; UE Lara e UD Lara são a Unión Deportiva Lara; Internacional de Barinas é o Hermanos Colmenárez. Clubes diferentes com nome parecido ficam separados: Atlético Zamora (até 2005) e Zamora FC; Lara FC (1965-1985), Unión Deportiva Lara (1986-2002) e Deportivo Lara (2009 em diante); Anzoátegui FC (1967), Atlético Anzoátegui (1986-1990), Deportivo Anzoátegui (2007 em diante) e o Anzoátegui FC de 2025; Atlético Monagas (2000) e Monagas SC; Estudiantes de Caracas (era amadora) e Estudiantes de Caracas SC (2015-2019). Homônimos de clubes de outros países levam a cidade ou o país (Deportivo Español de Caracas, Celta de Caracas, Danubio de Caracas, América de Caracas).

**Regras:** o placar é o da fonte de base (RSSSF; ESPN onde a RSSSF não tem). Jogo decidido no tribunal leva o placar dado (`awd`), com o de campo na observação; "bt" / "lt" (venceu / perdeu sem placar conhecido) viram W.O. (vitória sem gols, como a tabela conta); "drw" (empate sem placar, 1994/95) fica de fora. Ida e volta numa linha só ("A 1-0 0-4 B") vira dois jogos, com os gols de A primeiro e o mando da volta presumido. Pontos: 2 por vitória até 1994/95 e 3 a partir de 1995/96. Nas edições sem jogos, campeão e vice da lista ficam em 1º e 2º.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1921 | 0 | 0 (0) | 0 | 0 | 0 / 0 | América de Caracas | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1922 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Centro Atlético | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1923 | 0 | 0 (0) | 0 | 0 | 0 / 0 | América de Caracas | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1924 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Centro Atlético | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1925 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Loyola | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1926 | 2 | 1 (1) | 9 | 0 | 0 / 0 | Centro Atlético | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1927 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Venzóleo | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1928 | 2 | 1 (1) | 5 | 0 | 0 / 0 | Deportivo Venezuela | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1929 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Deportivo Venezuela | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1930 | 2 | 1 (1) | 2 | 0 | 0 / 0 | Centro Atlético | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1931 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Deportivo Venezuela | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1932 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Unión SC | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1933 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Deportivo Venezuela | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1934 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Unión SC | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1935 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Unión SC | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1936 | 2 | 1 (1) | 3 | 0 | 0 / 0 | Dos Caminos | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1937 | 2 | 1 (1) | 8 | 0 | 0 / 0 | Dos Caminos | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1938 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Dos Caminos | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1939 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Unión SC | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1940 | 6 | 45 (45) | 172 | 0 | 1 / 0 | Unión SC | RSSSF (venez40) |
| 1941 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Litoral | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1942 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Dos Caminos | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1943 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Loyola | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1944 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Loyola | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1945 | 8 | 16 (16) | 54 | 1 | 0 / 0 | Dos Caminos | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1946 | 6 | 9 (9) | 27 | 0 | 0 / 0 | Deportivo Español de Caracas | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1947 | 7 | 10 (10) | 46 | 0 | 0 / 0 | Unión SC | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1948 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Loyola | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1949 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Dos Caminos | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1950 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Unión SC | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1951 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Universidad Central | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1952 | 0 | 0 (0) | 0 | 0 | 0 / 0 | La Salle | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1953 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Universidad Central | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1954 | 0 | 0 (0) | 0 | 0 | 0 / 0 | Deportivo Vasco | lista de campeões da Wikipédia em inglês (campeão e vice) |
| 1955 | 5 | 30 (28) | 88 | 0 | 1 / 0 | La Salle | RSSSF (venez55) |
| 1956 | 5 | 30 (30) | 87 | 0 | 1 / 0 | Banco Obrero | RSSSF (venez56) |
| 1957 | 6 | 45 (45) | 191 | 0 | 1 / 0 | Universidad Central | RSSSF (venez57) |
| 1958 | 5 | 20 (20) | 52 | 0 | 1 / 0 | Deportivo Portugués | RSSSF (venez58) |
| 1959 | 5 | 30 (30) | 115 | 0 | 1 / 0 | Deportivo Español de Caracas | RSSSF (venez59) |
| 1960 | 4 | 15 (15) | 50 | 0 | 1 / 1 | Deportivo Portugués | RSSSF (venez60) |
| 1961 | 5 | 40 (39) | 139 | 0 | 1 / 0 | Deportivo Italia | RSSSF (venez61) |
| 1962 | 6 | 62 (55) | 181 | 0 | 1 / 0 | Deportivo Portugués | RSSSF (venez62) |
| 1963 | 6 | 37 (37) | 136 | 0 | 2 / 0 | Deportivo Italia | RSSSF (venez63) |
| 1964 | 6 | 62 (62) | 188 | 0 | 0 / 2 | Deportivo Galicia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1965 | 8 | 112 (112) | 337 | 0 | 1 / 0 | Lara FC | RSSSF (venez65) |
| 1966 | 9 | 108 (108) | 314 | 0 | 1 / 0 | Deportivo Italia | RSSSF (venez66) |
| 1967 | 9 | 128 (128) | 383 | 0 | 1 / 0 | Deportivo Portugués | RSSSF (venez67) |
| 1968 | 10 | 120 (120) | 400 | 0 | 2 / 0 | Unión Deportiva Canarias | RSSSF (venez68) |
| 1969 | 9 | 144 (144) | 413 | 0 | 1 / 0 | Deportivo Galicia | RSSSF (venez69) |
| 1970 | 8 | 114 (114) | 286 | 0 | 3 / 0 | Deportivo Galicia | RSSSF (venez70) |
| 1971 | 8 | 112 (112) | 293 | 0 | 1 / 0 | Valencia FC | RSSSF (venez71) |
| 1972 | 9 | 159 (159) | 335 | 0 | 3 / 0 | Deportivo Italia | RSSSF (venez72) |
| 1973 | 9 | 145 (144) | 322 | 0 | 0 / 1 | Portuguesa FC | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1974 | 8 | 126 (126) | 333 | 0 | 2 / 0 | Deportivo Galicia | RSSSF (venez74) |
| 1975 | 8 | 124 (123) | 289 | 0 | 2 / 0 | Portuguesa FC | RSSSF (venez75) |
| 1976 | 8 | 124 (124) | 301 | 0 | 2 / 0 | Portuguesa FC | RSSSF (venez76) |
| 1977 | 12 | 169 (169) | 428 | 0 | 2 / 1 | Portuguesa FC | RSSSF (venez77) |
| 1978 | 12 | 162 (162) | 396 | 0 | 2 / 0 | Portuguesa FC | RSSSF (venez78) |
| 1979 | 12 | 162 (162) | 350 | 0 | 2 / 0 | Deportivo Táchira | RSSSF (venez79) |
| 1980 | 11 | 140 (140) | 266 | 0 | 1 / 1 | Estudiantes de Mérida | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1981 | 12 | 168 (168) | 332 | 0 | 4 / 0 | Deportivo Táchira | RSSSF (venez81) |
| 1982 | 12 | 162 (162) | 329 | 0 | 1 / 1 | Atlético San Cristóbal | RSSSF (venez82) |
| 1983 | 10 | 90 (89) | 199 | 0 | 1 / 0 | Universidad de Los Andes | RSSSF (venez83) |
| 1984 | 11 | 166 (166) | 334 | 0 | 1 / 1 | Deportivo Táchira | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1985 | 10 | 120 (120) | 257 | 0 | 0 / 2 | Estudiantes de Mérida | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1986 | 11 | 80 (80) | 154 | 0 | 2 / 1 | Deportivo Táchira | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1986/87 | 14 | 224 (224) | 430 | 0 | 3 / 0 | CS Marítimo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1987/88 | 14 | 238 (238) | 596 | 0 | 1 / 1 | CS Marítimo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1988/89 | 16 | 240 (240) | 641 | 0 | 0 / 1 | Mineros de Guayana | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1989/90 | 16 | 241 (241) | 560 | 0 | 1 / 0 | CS Marítimo | RSSSF (venez90) |
| 1990/91 | 16 | 240 (240) | 536 | 0 | 0 / 1 | Universidad de Los Andes | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1991/92 | 16 | 240 (240) | 602 | 0 | 0 / 1 | Caracas FC | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1992/93 | 16 | 241 (242) | 664 | 0 | 0 / 1 | CS Marítimo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1993/94 | 16 | 231 (231) | 608 | 0 | 0 / 0 | Caracas FC | RSSSF (venez94) |
| 1994/95 | 23 | 203 (203) | 548 | 0 | 0 / 0 | Caracas FC | RSSSF (venez95) |
| 1995/96 | 18 | 236 (236) | 683 | 0 | 3 / 2 | Minervén | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1996/97 | 12 | 226 (226) | 548 | 9 | 1 / 1 | Caracas FC | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1997/98 | 12 | 266 (266) | 745 | 1 | 1 / 1 | Universidad de Los Andes | RSSSF (venez98) |
| 1998/99 | 13 | 224 (224) | 608 | 9 | 2 / 0 | Deportivo Italia | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1999/00 | 12 | 275 (275) | 746 | 0 | 2 / 2 | Deportivo Táchira | RSSSF (venez00) |
| 2000/01 | 17 | 204 (204) | 528 | 7 | 3 / 0 | Caracas FC | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2001/02 | 10 | 182 (182) | 532 | 0 | 3 / 0 | Nacional Táchira | RSSSF (venez02) |
| 2002/03 | 10 | 182 (182) | 403 | 312 | 3 / 0 | Caracas FC | RSSSF (venez03) |
| 2003/04 | 10 | 180 (180) | 427 | 255 | 2 / 1 | Caracas FC | RSSSF (venez04) |
| 2004/05 | 10 | 180 (180) | 460 | 320 | 3 / 0 | Unión Atlético Maracaibo | RSSSF (venez05) |
| 2005/06 | 10 | 183 (182) | 465 | 456 | 3 / 0 | Caracas FC | RSSSF (venez06) |
| 2006/07 | 10 | 182 (182) | 438 | 438 | 3 / 0 | Caracas FC | RSSSF (venez07) |
| 2007/08 | 18 | 308 (308) | 826 | 774 | 3 / 1 | Deportivo Táchira | RSSSF (venez08) |
| 2008/09 | 18 | 310 (308) | 776 | 758 | 1 / 2 | Caracas FC | RSSSF (venez09) |
| 2009/10 | 18 | 309 (308) | 823 | 716 | 3 / 0 | Caracas FC | RSSSF (venez2010) |
| 2010/11 | 18 | 307 (307) | 775 | 736 | 1 / 1 | Deportivo Táchira | RSSSF (venez2011) |
| 2011/12 | 18 | 304 (306) | 699 | 627 | 0 / 2 | Deportivo Lara | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2012/13 | 18 | 308 (308) | 738 | 654 | 3 / 0 | Zamora FC | RSSSF (venez2013) |
| 2013/14 | 18 | 308 (308) | 790 | 327 | 2 / 0 | Zamora FC | RSSSF (venez2014) |
| 2014/15 | 18 | 308 (308) | 737 | 0 | 2 / 0 | Deportivo Táchira | RSSSF (venez2015) |
| 2015 | 20 | 204 (204) | 503 | 0 | 1 / 0 | Zamora FC | RSSSF (venez2016) |
| 2016 | 20 | 410 (410) | 1027 | 0 | 2 / 0 | Zamora FC | RSSSF (venez2016) |
| 2017 | 18 | 336 (336) | 825 | 0 | 2 / 0 | Monagas SC | RSSSF (venez2017) |
| 2018 | 18 | 337 (337) | 776 | 0 | 3 / 0 | Zamora FC | RSSSF (venez2018) |
| 2019 | 20 | 391 (391) | 999 | 0 | 4 / 0 | Caracas FC | RSSSF (venez2019) |
| 2020 | 19 | 185 (185) | 438 | 0 | 3 / 0 | Deportivo La Guaira | RSSSF (venez2020) |
| 2021 | 21 | 303 (303) | 808 | 0 | 5 / 0 | Deportivo Táchira | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2022 | 16 | 253 (253) | 610 | 0 | 2 / 0 | Metropolitanos | RSSSF (venez2022) |
| 2023 | 15 | 223 (223) | 546 | 0 | 2 / 0 | Deportivo Táchira | RSSSF (venez2023) |
| 2024 | 14 | 234 (234) | 565 | 0 | 7 / 0 | Deportivo Táchira | RSSSF (venez2024) |
| 2025 | 14 | 233 (233) | 556 | 0 | 6 / 0 | Universidad Central | RSSSF (venez2025) |

## Conferência e correções, edição a edição

### 1921

- sem ocorrências

### 1922

- sem jogos: a RSSSF não tem página deste ano (só o campeão e o vice da lista)

### 1923

- sem ocorrências

### 1924

- sem jogos: a RSSSF não tem página deste ano (só o campeão e o vice da lista)

### 1925

- sem ocorrências

### 1926

- sem ocorrências

### 1927

- sem ocorrências

### 1928

- sem ocorrências

### 1929

- sem ocorrências

### 1930

- sem ocorrências

### 1931

- sem jogos: a RSSSF não tem página deste ano (só o campeão e o vice da lista)

### 1932

- sem ocorrências

### 1933

- sem ocorrências

### 1934

- sem ocorrências

### 1935

- sem ocorrências

### 1936

- sem ocorrências

### 1937

- sem ocorrências

### 1938

- sem jogos: a RSSSF não tem página deste ano (só o campeão e o vice da lista)

### 1939

- sem jogos: a RSSSF não tem página deste ano (só o campeão e o vice da lista)

### 1940

- corrigido — Deportivo Español de Caracas x Loyola (None): quarto Deportivo Español x Loyola num turno triplo (as rodadas 11-15 listam 16 jogos para 15); sem ele a tabela final fecha com os jogos
- W.O./pontos para o visitante — Loyola Deportivo Venezuela (s/d)
- W.O./pontos para o visitante — Deportivo Español de Caracas Loyola (s/d)

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

- sem ocorrências

### 1948

- sem ocorrências

### 1949

- sem jogos: a RSSSF não tem página deste ano (só o campeão e o vice da lista)

### 1950

- sem jogos: a RSSSF não tem página deste ano (só o campeão e o vice da lista)

### 1951

- sem ocorrências

### 1952

- sem ocorrências

### 1953

- sem ocorrências

### 1954

- sem ocorrências

### 1955

- não jogado — Loyola Dos Caminos (s/d)
- não jogado — Deportivo Español de Caracas Deportivo Vasco (s/d)

### 1956

- sem ocorrências

### 1957

- sem ocorrências

### 1958

- sem ocorrências

### 1959

- sem ocorrências

### 1960

- tabela publicada x jogos — venez60:38: Deportivo Portugués tabela [3, 2, 1, 0, 10, 2] jogos [3, 2, 1, 0, 9, 2] — a outra tabela publicada (venez60) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — venez60:38: Deportivo Español de Caracas tabela [3, 2, 1, 0, 6, 4] jogos [3, 2, 1, 0, 6, 3] — a outra tabela publicada (venez60) fecha com os jogos: o erro é desta tabela

### 1961

- não jogado — Universidad Católica de Caracas Banco Agrícola y Pecuario (s/d)

### 1962

- não jogado — Universidad Central Banco Francés-Italiano (s/d)
- não jogado — Deportivo Portugués Universidad Central (s/d)
- não jogado — Universidad Central Deportivo Vasco (s/d)
- não jogado — Deportivo Portugués Banco Francés-Italiano (s/d)
- não jogado — Deportivo Portugués Dos Caminos (s/d)
- não jogado — Dos Caminos La Salle (s/d)
- não jogado — Deportivo Vasco La Salle (s/d)

### 1963

- sem ocorrências

### 1964

- tabela publicada x jogos — venez64:17: Unión Deportiva Canarias tabela [10, 4, 2, 4, 12, 12] jogos [10, 4, 2, 4, 11, 11] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez64:72: Unión Deportiva Canarias tabela [10, 3, 5, 2, 11, 12] jogos [10, 3, 5, 2, 12, 13] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1965

- sem ocorrências

### 1966

- a lista de campeões da RSSSF dá o vice Deportivo Galicia e a da Wikipédia em inglês, o Deportivo Portugués; fica o da RSSSF (fonte de base)

### 1967

- decidido fora de campo — Litoral Aragua FC (1966) (1967-05-17): 1] [awarded 1-0
- decidido fora de campo — Aragua FC (1966) Anzoátegui FC (1967) (1967-05-20): 2] [awarded 0-1
- decidido fora de campo — Valencia FC Aragua FC (1966) (1967-06-11): 3] [awarded 1-0
- decidido fora de campo — Aragua FC (1966) Litoral (1967-06-17): 4] [awarded 0-1

### 1968

- sem ocorrências

### 1969

- sem ocorrências

### 1970

- sem ocorrências

### 1971

- sem ocorrências

### 1972

- sem ocorrências

### 1973

- tabela publicada x jogos — venez73:14: Unión Deportiva Canarias tabela [32, 8, 10, 14, 30, 40] jogos [32, 9, 10, 13, 30, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- não jogado — Anzoátegui FC (1967) Deportivo Portugués (1973-12-08)

### 1974

- sem ocorrências

### 1975

- a lista de campeões da RSSSF dá o vice Deportivo Galicia e a da Wikipédia em inglês, o Estudiantes de Mérida; fica o da RSSSF (fonte de base)
- não jogado — Universitarios de Oriente Portuguesa FC (1975-11-12)

### 1976

- sem ocorrências

### 1977

- tabela publicada x jogos — venez77:209: Portuguesa FC tabela [10, 6, 2, 2, 18, 9] jogos [10, 5, 2, 3, 17, 10] — a outra tabela publicada (venez77) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — venez77:209: Deportivo Italia tabela [10, 4, 1, 5, 14, 15] jogos [10, 5, 1, 4, 15, 14] — a outra tabela publicada (venez77) fecha com os jogos: o erro é desta tabela

### 1978

- sem ocorrências

### 1979

- sem ocorrências

### 1980

- tabela publicada x jogos — venez80:16: Deportivo Táchira tabela [20, 6, 9, 5, 18, 15] jogos [20, 5, 10, 5, 17, 15] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez80:16: Deportivo Portugués tabela [20, 1, 7, 12, 8, 27] jogos [20, 1, 8, 11, 8, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1981

- não jogado — Deportivo Galicia Valencia FC (1981-11-06)

### 1982

- tabela publicada x jogos — venez82:187: Atlético San Cristóbal tabela [10, 3, 6, 1, 9, 9] jogos [9, 3, 5, 1, 9, 9] — a outra tabela publicada (venez82) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — venez82:187: Deportivo Táchira tabela [10, 3, 5, 2, 9, 6] jogos [11, 3, 6, 2, 9, 6] — a outra tabela publicada (venez82) fecha com os jogos: o erro é desta tabela

### 1983

- não jogado — Atlético San Cristóbal Estudiantes de Mérida (1983-06-24)

### 1984

- Petroleros del Zulia x Universidad de Los Andes (15/08) está como "awd" sem placar: a tabela conta derrota por 0-1 para os dois clubes
- tabela publicada x jogos — venez84:16: Universidad de Los Andes tabela [20, 7, 7, 6, 16, 13] jogos [19, 7, 7, 5, 16, 12] — a outra tabela publicada (venez84) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — venez84:16: Petroleros del Zulia tabela [20, 4, 4, 12, 10, 32] jogos [19, 4, 4, 11, 10, 31] — a diferença vem de Petroleros del Zulia x Universidad de Los Andes (1984-08-15), decidido fora de campo ou abandonado: a tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)
- decidido fora de campo — Petroleros del Zulia Universidad de Los Andes (1984-08-15)
- não jogado — Estudiantes de Mérida Deportivo Portugués (1984-11-18)

### 1985

- tabela publicada x jogos — venez85:16: Portuguesa FC tabela [18, 6, 6, 6, 25, 23] jogos [18, 6, 6, 6, 22, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez85:16: Universidad Central tabela [18, 3, 4, 11, 11, 31] jogos [18, 3, 4, 11, 11, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez85:140: Nacional Carabobo tabela [10, 5, 2, 3, 13, 10] jogos [10, 4, 3, 3, 13, 11] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez85:140: Mineros de Guayana tabela [10, 1, 4, 5, 9, 15] jogos [10, 1, 5, 4, 10, 15] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1986

- tabela publicada x jogos — venez86:137: Estudiantes de Mérida tabela [10, 6, 2, 2, 12, 6] jogos [10, 5, 3, 2, 11, 6] — a outra tabela publicada (venez86) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — venez86:137: Caracas FC tabela [10, 1, 2, 7, 8, 17] jogos [10, 1, 3, 6, 8, 16] — a outra tabela publicada (venez86) fecha com os jogos: o erro é desta tabela

### 1986/87

- sem ocorrências

### 1987/88

- tabela publicada x jogos — venez88:18: Mineros de Guayana tabela [26, 11, 9, 6, 38, 35] jogos [26, 10, 10, 6, 38, 35] — a outra tabela publicada (venez88) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — venez88:18: Universidad de Los Andes tabela [26, 9, 9, 8, 36, 34] jogos [26, 9, 9, 8, 38, 34] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez88:18: Atlético Anzoátegui tabela [26, 7, 10, 9, 29, 42] jogos [26, 8, 9, 9, 29, 42] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez88:18: Estudiantes de Mérida tabela [26, 7, 7, 12, 31, 36] jogos [26, 7, 7, 12, 31, 38] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez88:18: Deportivo Italia tabela [26, 7, 7, 12, 24, 34] jogos [26, 7, 7, 12, 24, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez88:18: Universidad Central tabela [26, 1, 6, 19, 17, 53] jogos [26, 1, 6, 19, 17, 54] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1988/89

- tabela publicada x jogos — venez89:14: Portuguesa FC tabela [30, 12, 6, 12, 36, 35] jogos [30, 12, 6, 12, 37, 34] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez89:14: Atlético Anzoátegui tabela [30, 7, 8, 15, 20, 45] jogos [30, 7, 8, 15, 20, 47] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1989/90

- sem ocorrências

### 1990/91

- tabela publicada x jogos — venez91:14: Mineros de Guayana tabela [30, 15, 4, 11, 43, 30] jogos [30, 15, 5, 10, 43, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez91:14: Unión Deportiva Lara tabela [30, 11, 10, 9, 36, 29] jogos [30, 11, 11, 8, 36, 29] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez91:14: Deportivo Italia tabela [30, 10, 10, 10, 27, 29] jogos [30, 10, 11, 9, 27, 29] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez91:14: Estudiantes de Mérida tabela [30, 9, 11, 10, 27, 31] jogos [30, 9, 10, 11, 27, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez91:14: Monagas SC tabela [30, 9, 11, 10, 33, 39] jogos [30, 8, 12, 10, 33, 39] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez91:14: Portuguesa FC tabela [30, 9, 7, 14, 27, 41] jogos [30, 8, 9, 13, 27, 41] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez91:14: Maracaibo FC tabela [30, 9, 2, 19, 28, 43] jogos [30, 8, 3, 19, 28, 43] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez91:14: Valencia FC tabela [30, 9, 1, 20, 33, 60] jogos [30, 8, 3, 19, 33, 60] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1991/92

- tabela publicada x jogos — venez92:16: CS Marítimo tabela [30, 13, 13, 4, 46, 21] jogos [30, 13, 13, 4, 47, 22] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez92:16: Deportivo Táchira tabela [30, 15, 8, 7, 45, 23] jogos [30, 15, 8, 7, 46, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez92:16: Universidad de Los Andes tabela [30, 14, 8, 8, 40, 28] jogos [30, 14, 8, 8, 41, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez92:16: Anzoátegui FC (1967) tabela [30, 9, 12, 9, 43, 36] jogos [30, 9, 13, 8, 43, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez92:16: Portuguesa FC tabela [30, 9, 8, 13, 30, 41] jogos [30, 9, 8, 13, 31, 41] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1992/93

- falta um Unión Deportiva Lara x Atlético Zamora (a página só lista o de 13/12, 0-0); pela tabela final, o Zamora venceu o que falta por 1-0
- tabela publicada x jogos — venez93:16: Deportivo Táchira tabela [30, 17, 5, 8, 53, 34] jogos [30, 17, 5, 8, 54, 34] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez93:16: Unión Deportiva Lara tabela [30, 11, 12, 7, 32, 25] jogos [29, 11, 12, 6, 32, 24] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — venez93:16: Universidad de Los Andes tabela [30, 5, 10, 15, 27, 55] jogos [30, 4, 11, 15, 25, 56] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez93:16: Atlético Zamora tabela [30, 6, 6, 18, 21, 61] jogos [29, 5, 6, 18, 20, 61] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — venez93:16: Portuguesa FC tabela [30, 4, 4, 22, 19, 68] jogos [30, 4, 5, 21, 19, 66] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1993/94

- decidido fora de campo — CS Marítimo Atlético Zamora (s/d): awarded to Zamora, suspended due to
- decidido fora de campo — Mineros de Guayana Llaneros de Guanare (s/d): awarded to Mineros, suspended due to

### 1994/95

- 5 jogos do Apertura (Copa Venezuela) estão na página como "drw" (empate sem placar, decidido nos pênaltis) e ficam de fora; "bt" / "lt" (venceu / perdeu sem placar) entram como W.O.
- W.O./pontos para o mandante — Maracaibo FC San Cristóbal FC (s/d): 1-0 or 2-1
- W.O./pontos para o visitante — Mineros de Guayana Minervén (s/d): 2-4 or 3-5
- W.O./pontos para o visitante — Industriales del Caroní Monagas SC (s/d): 0-1 or 1-2
- W.O./pontos para o visitante — Deportivo Italia CS Marítimo (s/d): 1-3 or 0-2
- W.O./pontos para o mandante — Trujillanos San Cristóbal FC (s/d): 3-2 or 2-1
- W.O./pontos para o visitante — Industriales del Caroní Mineros de Guayana (s/d): 1-2 or 0-1
- W.O./pontos para o visitante — Valencia FC CS Marítimo (s/d): 0-1 or 1-2
- W.O./pontos para o mandante — Deportivo Italia Deportivo Tuy (s/d): 2-0 or 3-1

### 1995/96

- tabela publicada x jogos — venez96:21: Minervén tabela [16, 8, 3, 5, 30, 17] jogos [16, 7, 4, 5, 30, 17] — a outra tabela publicada (venez96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — venez96:21: Mineros de Guayana tabela [16, 5, 5, 6, 21, 18] jogos [16, 5, 6, 5, 21, 18] — a outra tabela publicada (venez96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — venez96:227: Minervén tabela [10, 4, 3, 3, 18, 10] jogos [10, 5, 2, 3, 18, 10] — a outra tabela publicada (venez96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — venez96:227: Deportivo Italia tabela [10, 4, 3, 3, 9, 11] jogos [10, 4, 2, 4, 9, 11] — a outra tabela publicada (venez96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — venez96:227: Valencia FC tabela [10, 2, 7, 1, 12, 13] jogos [10, 2, 6, 2, 12, 13] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez96:227: Universidad de Los Andes tabela [10, 2, 3, 5, 12, 13] jogos [10, 3, 2, 5, 12, 13] — a outra tabela publicada (venez96) fecha com os jogos: o erro é desta tabela

### 1996/97

- o Atlético Zulia (Maracaibo) entra como Universidad de Los Andes, como na lista de campeões da RSSSF ("ULA relocated and renamed Atlético Zulia during the 1996/97 and 1997/98 seasons"); a página da temporada 1996/97 diz que o Atlético Zulia era o Unicol (Lagunillas). Decisão a confirmar com o Guilherme
- tabela publicada x jogos — venez97:18: Valencia FC tabela [22, 4, 6, 12, 15, 29] jogos [22, 4, 6, 12, 15, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- decidido fora de campo — Mineros de Guayana El Vigía FC (1997-04-13): awarded 2-0, Vigia did not show up

### 1997/98

- o Atlético Zulia (Maracaibo) entra como Universidad de Los Andes, como na lista de campeões da RSSSF ("ULA relocated and renamed Atlético Zulia during the 1996/97 and 1997/98 seasons"); a página da temporada 1996/97 diz que o Atlético Zulia era o Unicol (Lagunillas). Decisão a confirmar com o Guilherme; o título do Apertura e o do ano ficam com a Universidad de Los Andes
- tabela publicada x jogos — venez98:18: Carabobo FC tabela [22, 8, 7, 7, 26, 25] jogos [22, 8, 8, 6, 27, 23] — a outra tabela publicada (venez98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — venez98:18: Nacional Táchira tabela [22, 9, 2, 11, 35, 35] jogos [22, 8, 3, 11, 33, 36] — a outra tabela publicada (venez98) fecha com os jogos: o erro é desta tabela
- decidido fora de campo — Nacional Táchira 3-0 Carabobo FC (1997-08-31): awarded; originally 1-1

### 1998/99

- o Internacional de Lara entra como Trujillanos ("Trujillanos were relocated and renamed Internacional de Lara", RSSSF); no ano seguinte o Internacional foi para El Vigía e virou El Vigía FC, e o Trujillanos voltou

### 1999/00

- tabela publicada x jogos — venez00:18: Nacional Táchira tabela [22, 5, 7, 10, 19, 36] jogos [22, 4, 8, 10, 19, 36] — a outra tabela publicada (venez00) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — venez00:478: Nacional Táchira tabela [44, 9, 15, 20, 36, 67] jogos [44, 8, 16, 20, 36, 67] — a outra tabela publicada (venez00) fecha com os jogos: o erro é desta tabela
- decidido fora de campo — Deportivo Italia Nacional Táchira (2000-12-22): awarded 2-0
- decidido fora de campo — Deportivo Táchira El Vigía FC (2001-03-08): awarded 3-0
- decidido fora de campo — Deportivo Italia Trujillanos (2001-04-30): awarded 1-0

### 2000/01

- a 1ª fase foi a Copa Venezuela 2000 (Apertura, com final Caracas x Táchira) e a 2ª, o Torneo Nacional 2001, que deu o título; o "Monagas" da 1ª fase é o Atlético Monagas e o do Torneo Nacional, o Monagas SC (que comprou a vaga do El Vigía; "different from Atlético Monagas", RSSSF)
- decidido fora de campo — Deportivo Táchira Universidad de Los Andes (2001-04-01): awarded 0-2; originally 2-1

### 2001/02

- decidido fora de campo — Mineros de Guayana Deportivo Galicia (2002-01-27): awarded 0-2, originally 1-1

### 2002/03

- decidido fora de campo — Monagas SC Nacional Táchira (2003-01-22): awarded 2-0
- não jogado — Deportivo Táchira Nacional Táchira (2003-03-02)
- não jogado — Nacional Táchira Unión Atlético Maracaibo (2003-03-09)
- não jogado — Deportivo Italia Nacional Táchira (2003-03-12)
- não jogado — Trujillanos Nacional Táchira (2003-03-16)
- não jogado — Nacional Táchira Monagas SC (2003-03-19)
- não jogado — Caracas FC Nacional Táchira (2003-03-23)
- não jogado — Nacional Táchira Carabobo FC (2003-04-06)
- não jogado — Mineros de Guayana Nacional Táchira (2003-04-09)
- não jogado — Nacional Táchira Estudiantes de Mérida (2003-04-13)
- não jogado — Nacional Táchira Deportivo Táchira (2003-04-20)
- não jogado — Unión Atlético Maracaibo Nacional Táchira (2003-04-27)
- não jogado — Nacional Táchira Trujillanos (2003-05-04)
- não jogado — Monagas SC Nacional Táchira (2003-05-07)
- não jogado — Nacional Táchira Caracas FC (2003-05-11)
- não jogado — Nacional Táchira Deportivo Italia (2003-05-14)
- não jogado — Carabobo FC Nacional Táchira (2003-05-18)
- não jogado — Nacional Táchira Mineros de Guayana (2003-05-21)
- não jogado — Estudiantes de Mérida Nacional Táchira (2003-05-25)

### 2003/04

- tabela publicada x jogos — venez04:530: Deportivo Táchira tabela [36, 20, 10, 6, 61, 40] jogos [36, 20, 10, 6, 60, 39] — a outra tabela publicada (venez04) fecha com os jogos: o erro é desta tabela

### 2004/05

- sem ocorrências

### 2005/06

- ESPN: 172 jogos casados
- abandonado/suspenso, sem valer — Carabobo FC Aragua FC (2005-12-18): abandoned at 2-0 in 64'

### 2006/07

- ESPN: 181 jogos casados

### 2007/08

- ESPN: 308 jogos casados
- tabela publicada x jogos — venez08:902: Monagas SC tabela [34, 11, 6, 17, 45, 52] jogos [34, 11, 6, 17, 46, 52] — a outra tabela publicada (venez08) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — venez08:902: Estudiantes de Mérida tabela [34, 9, 11, 14, 39, 53] jogos [34, 9, 11, 14, 39, 54] — a outra tabela publicada (venez08) fecha com os jogos: o erro é desta tabela
- decidido fora de campo — Monagas SC Caracas FC (2007-11-10): awarded 0-3; originally 1-0,

### 2008/09

- ESPN: 307 jogos casados
- tabela publicada x jogos — venez09:16: Deportivo Táchira tabela [17, 8, 5, 4, 35, 18] jogos [17, 7, 7, 3, 35, 18] — a outra tabela publicada (venez09) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — venez09:919: Deportivo Táchira tabela [34, 18, 11, 5, 64, 33] jogos [34, 17, 13, 4, 64, 33] — a outra tabela publicada (venez09) fecha com os jogos: o erro é desta tabela
- abandonado/suspenso, sem valer — Deportivo Italia Estrella Roja (2008-10-05): abandoned at 0-1 in 46'
- abandonado/suspenso, sem valer — Carabobo FC Caracas FC (2008-10-26): abandoned at 2-2 in 45'

### 2009/10

- ESPN: 307 jogos casados
- abandonado/suspenso, sem valer — Deportivo Táchira Caracas FC (2009-11-04): abandoned at 0-0 at half-time

### 2010/11

- o Clausura 2011 tem 82 jogos sem placar na RSSSF: 81 vêm da ESPN; o Caroní x Zulia não está em nenhuma das duas (pela tabela final, o Zulia venceu por 3-0)
- ESPN: 305 jogos casados
- tabela publicada x jogos — venez2011:525: Zulia FC tabela [17, 6, 1, 10, 17, 34] jogos [16, 5, 1, 10, 14, 34] — a outra tabela publicada (venez2011) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — venez2011:525: Caroní FC tabela [17, 1, 4, 12, 9, 35] jogos [16, 1, 4, 11, 9, 32] — a outra tabela publicada (venez2011) fecha com os jogos: o erro é desta tabela
- corrigido — Atlético Venezuela x Mineros de Guayana (2011-05-01): a ESPN dá 0-0 e a RSSSF lista o jogo sem placar; a tabela final da RSSSF conta vitória do Mineros por 3-0 (provável W.O.)
- corrigido — Atlético El Vigía x Caroní FC (2011-05-08): a ESPN dá 15-0; a tabela final da RSSSF só fecha com 3-0 (gols pró do El Vigía e contra do Caroní)

### 2011/12

- a página da RSSSF só tem as tabelas: os jogos vêm da ESPN, que não tem dois do Apertura (Mineros x Zamora, 2-1 para o Mineros pela tabela, e Carabobo x Aragua, 1-1 pela tabela)
- ESPN: 304 jogos casados
- tabela publicada x jogos — venez2012:26: Mineros de Guayana tabela [17, 8, 4, 5, 21, 22] jogos [16, 7, 4, 5, 19, 21] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — venez2012:26: Zamora FC tabela [17, 5, 8, 4, 23, 19] jogos [16, 5, 8, 3, 22, 17] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — venez2012:26: Aragua FC tabela [17, 5, 8, 4, 15, 19] jogos [16, 5, 7, 4, 14, 18] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — venez2012:26: Carabobo FC tabela [17, 1, 6, 10, 17, 27] jogos [16, 1, 5, 10, 16, 26] — faltam 1 jogo(s) do clube na página
- tabela publicada x jogos — venez2012:53: Deportivo Lara tabela [17, 13, 3, 1, 32, 12] jogos [17, 13, 3, 1, 31, 11] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez2012:53: Mineros de Guayana tabela [17, 9, 6, 2, 29, 15] jogos [17, 9, 6, 2, 29, 14] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez2012:53: Trujillanos tabela [17, 5, 8, 4, 17, 16] jogos [17, 5, 7, 5, 16, 17] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez2012:53: Estudiantes de Mérida tabela [17, 4, 7, 6, 17, 19] jogos [17, 4, 8, 5, 17, 18] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — venez2012:53: Tucanes de Amazonas tabela [17, 2, 2, 13, 15, 36] jogos [17, 2, 2, 13, 14, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 2012/13

- ESPN: 308 jogos casados
- decidido fora de campo — Deportivo Táchira Atlético Venezuela (2012-10-28): awarded 0-3; pitch invasion by home fans

### 2013/14

- ESPN: 290 jogos casados

### 2014/15

- ESPN: 308 jogos casados
- decidido fora de campo — Deportivo Italia Trujillanos (2014-12-14): awarded 0-3

### 2015

- o Torneo de Adecuación 2015 conta como título na RSSSF (Zamora); a Wikipédia em inglês não o conta como temporada
- ESPN: 204 jogos casados

### 2016

- ESPN: 410 jogos casados
- decidido fora de campo — Deportivo Italia Portuguesa FC (2016-05-04): awarded 0-3; not played due to

### 2017

- ESPN: 336 jogos casados
- decidido fora de campo — Atlético Venezuela Mineros de Guayana (2017-04-23): awarded 3-0; originally 2-1,
- decidido fora de campo — Mineros de Guayana Portuguesa FC (2017-04-26): awarded 0-3; originally 1-0,
- decidido fora de campo — Zulia FC Deportivo Táchira (2017-05-19): awarded 0-3; originally 2-0,

### 2018

- ESPN: 336 jogos casados
- abandonado/suspenso, sem valer — Atlético Venezuela Trujillanos (2018-10-17): abandoned at 1-0 at half-time

### 2019

- ESPN: 391 jogos casados
- decidido fora de campo — Trujillanos Mineros de Guayana (2019-03-20): awarded 0-3; not played because
- decidido fora de campo — Caracas FC Deportivo Lara (2019-07-28): awarded 0-3; abandoned at 1-1
- decidido fora de campo — Portuguesa FC Academia Puerto Cabello (2019-09-28): awarded 0-3, originally 0-0; Portuguesa

### 2020

- ESPN: 183 jogos casados
- abandonado/suspenso, sem valer — Aragua FC Caracas FC (2020-12-07): abandoned at 0-0 in 74' due

### 2021

- ESPN: 302 jogos casados

### 2022

- ESPN: 253 jogos casados

### 2023

- ESPN: 219 jogos casados

### 2024

- ESPN: 232 jogos casados

### 2025

- ESPN: 233 jogos casados

