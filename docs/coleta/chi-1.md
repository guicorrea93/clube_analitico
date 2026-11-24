# Campeonato Chileno (1ª divisão) — coleta de dados

Gerado por `python coleta/chi-1/importar.py`. Pacote em `data/coleta/chi-1/pacote/`.

**Edições:** 109, uma por torneio que deu título de campeão chileno da 1ª divisão, de 1933 a 2025, como na lista de campeões da RSSSF (`chilechamp.html`) e na Wikipédia em inglês (as duas trazem os mesmos campeões). Apertura e Clausura deram título cada um em 1997, de 2002 a 2009, em 2011, 2012 e de 2013/14 a 2016/17: uma edição por torneio, como no arg-1; os torneios de Transición de 2013 e 2017 também. "2020" é a temporada 2020/21 (pandemia); 2019 foi encerrado na 24ª rodada pelos protestos de outubro.

**Fora do pacote:** a Copa Chile (e as copas de começo e de fim de ano dos anos 1930-1980, "Campeonato de Apertura" e "Campeonato de Clausura"), as liguillas pré-Libertadores e pré-Sudamericana e os jogos de promoção contra clubes da 2ª divisão.

**Fontes:** RSSSF (uma página por temporada, `data/coleta/chi-1/rsssf/`: base de jogos de 1933 a 1983 e de 1996 a 2024, com fases, grupos, rodadas, datas e autores dos gols; as tabelas da própria página e a lista de tabelas finais `chilehist.html`, de 1933 a 1996, são a conferência); ogol (base dos jogos de 1984 a 1995 e de 2025, anos em que a RSSSF só traz a tabela final; nos outros anos, rodada e data que faltam, conferência de placar e o nome de cada clube no ogol); ESPN (liga `chi.1`, 2001 em diante: base da fase de pontos corridos do Clausura 2011 e de 2012, que a RSSSF não traz; hora, estádio, público, gols com minuto e cartões); Wikipédia em inglês (lista de campeões, segunda fonte do campeão).

**Clubes:** Green Cross (Santiago, campeão em 1945), Green Cross-Temuco (1965) e Deportes Temuco (1985) são um clube só, como a RSSSF conta; Ferroviarios e Badminton (até 1949) e Ferrobádminton (fusão de 1950) ficam separados. Homônimos de clubes do banco levam a cidade: Everton de Viña del Mar, Rangers de Talca, Naval de Talcahuano, Metropolitano de Santiago.

**Regras:** o placar é o da RSSSF (ou do ogol e da ESPN, nos anos em que são a base); o ogol entra como conferência nos outros anos. Jogo decidido no tribunal leva o placar dado (`awd`) ou, sem placar, a vitória (`wo`, com o placar de campo na observação). Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos por vitória: 2 até 1994 e 3 a partir de 1995 (várias temporadas tiveram pontos de bônus, que a tabela publicada mostra; a diferença vai em `ajuste_pontos`).

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1933 | 8 | 29 (29) | 131 | 0 | 1 / 0 | Magallanes | RSSSF (chile33) |
| 1934 | 12 | 66 (66) | 402 | 0 | 2 / 0 | Magallanes | RSSSF (chile34) |
| 1935 | 6 | 30 (30) | 165 | 0 | 1 / 0 | Magallanes | RSSSF (chile35) |
| 1936 | 6 | 30 (30) | 157 | 0 | 1 / 0 | Audax Italiano | RSSSF (chile36) |
| 1937 | 7 | 42 (42) | 196 | 0 | 1 / 1 | Colo Colo | RSSSF (chile37) |
| 1938 | 7 | 42 (42) | 250 | 0 | 1 / 0 | Magallanes | RSSSF (chile38) |
| 1939 | 10 | 109 (173) | 583 | 0 | 4 / 0 | Colo Colo | RSSSF (chile39) |
| 1940 | 10 | 90 (90) | 417 | 0 | 1 / 0 | Universidad de Chile | RSSSF (chile40) |
| 1941 | 10 | 90 (88) | 409 | 0 | 1 / 1 | Colo Colo | RSSSF (chile41) |
| 1942 | 10 | 90 (90) | 349 | 0 | 1 / 0 | Santiago Morning | RSSSF (chile42) |
| 1943 | 10 | 90 (90) | 387 | 0 | 1 / 0 | Unión Española | RSSSF (chile43) |
| 1944 | 12 | 132 (132) | 572 | 0 | 1 / 0 | Colo Colo | RSSSF (chile44) |
| 1945 | 12 | 132 (132) | 534 | 0 | 1 / 0 | Green Cross de Santiago | RSSSF (chile45) |
| 1946 | 13 | 192 (192) | 778 | 0 | 3 / 3 | Audax Italiano | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1947 | 13 | 156 (156) | 588 | 0 | 0 / 1 | Colo Colo | RSSSF (chile47:40) |
| 1948 | 13 | 156 (156) | 638 | 0 | 0 / 1 | Audax Italiano | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1949 | 12 | 132 (132) | 510 | 0 | 1 / 0 | Universidad Católica | RSSSF (chile49) |
| 1950 | 12 | 133 (133) | 551 | 0 | 1 / 0 | Everton de Viña del Mar | RSSSF (chile50) |
| 1951 | 12 | 163 (163) | 633 | 0 | 2 / 4 | Unión Española | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1952 | 12 | 198 (198) | 763 | 0 | 1 / 0 | Everton de Viña del Mar | RSSSF (chile52) |
| 1953 | 14 | 182 (182) | 697 | 0 | 0 / 1 | Colo Colo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1954 | 14 | 225 (225) | 849 | 0 | 5 / 0 | Universidad Católica | RSSSF (chile54:356+chile54:412) |
| 1955 | 14 | 225 (225) | 815 | 0 | 5 / 0 | Palestino | RSSSF (chile55:356+chile55:412) |
| 1956 | 14 | 182 (182) | 586 | 0 | 1 / 0 | Colo Colo | RSSSF (chile56) |
| 1957 | 14 | 185 (185) | 671 | 0 | 2 / 0 | Audax Italiano | RSSSF (chile57) |
| 1958 | 14 | 182 (182) | 646 | 0 | 1 / 0 | Santiago Wanderers | RSSSF (chile58) |
| 1959 | 14 | 183 (183) | 620 | 0 | 1 / 0 | Universidad de Chile | RSSSF (chile59) |
| 1960 | 14 | 182 (182) | 577 | 0 | 1 / 0 | Colo Colo | RSSSF (chile60) |
| 1961 | 14 | 184 (184) | 685 | 0 | 0 / 1 | Universidad Católica | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1962 | 18 | 306 (306) | 1052 | 0 | 0 / 1 | Universidad de Chile | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1963 | 18 | 306 (306) | 1037 | 0 | 0 / 1 | Colo Colo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1964 | 18 | 306 (306) | 966 | 0 | 0 / 1 | Universidad de Chile | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1965 | 18 | 306 (306) | 1027 | 0 | 0 / 1 | Universidad de Chile | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1966 | 18 | 306 (306) | 933 | 0 | 1 / 0 | Universidad Católica | RSSSF (chile66) |
| 1967 | 18 | 306 (306) | 943 | 0 | 1 / 0 | Universidad de Chile | RSSSF (chile67) |
| 1968 | 18 | 324 (324) | 1015 | 0 | 8 / 1 | Santiago Wanderers | RSSSF (chile68:505) |
| 1969 | 18 | 325 (325) | 990 | 0 | 5 / 1 | Universidad de Chile | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1970 | 18 | 339 (339) | 965 | 0 | 5 / 3 | Colo Colo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1971 | 18 | 307 (307) | 853 | 0 | 1 / 0 | Unión San Felipe | RSSSF (chile71:16) |
| 1972 | 18 | 306 (306) | 874 | 0 | 1 / 0 | Colo Colo | RSSSF (chile72) |
| 1973 | 18 | 306 (306) | 853 | 0 | 0 / 1 | Unión Española | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1974 | 18 | 306 (306) | 962 | 0 | 1 / 0 | Huachipato | RSSSF (chile74) |
| 1975 | 18 | 307 (307) | 933 | 0 | 1 / 0 | Unión Española | RSSSF (chile75) |
| 1976 | 18 | 308 (308) | 965 | 0 | 0 / 1 | Everton de Viña del Mar | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1977 | 18 | 307 (307) | 857 | 0 | 0 / 1 | Unión Española | RSSSF (chile77:16) |
| 1978 | 18 | 306 (306) | 857 | 0 | 1 / 0 | Palestino | RSSSF (chile78) |
| 1979 | 18 | 306 (306) | 835 | 0 | 0 / 1 | Colo Colo | RSSSF (chile79:220) |
| 1980 | 18 | 306 (306) | 783 | 0 | 3 / 0 | Cobreloa | RSSSF (chilehist) |
| 1981 | 16 | 240 (240) | 663 | 0 | 1 / 0 | Colo Colo | RSSSF (chile81:240) |
| 1982 | 16 | 240 (240) | 688 | 0 | 0 / 1 | Cobreloa | RSSSF (chile82:255) |
| 1983 | 22 | 462 (462) | 1294 | 0 | 1 / 0 | Colo Colo | RSSSF (chile83:515) |
| 1984 | 26 | 319 (319) | 785 | 0 | 0 / 0 | Universidad Católica | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1985 | 20 | 380 (380) | 955 | 0 | 0 / 1 | Cobreloa | RSSSF (chilehist:1348) |
| 1986 | 18 | 307 (307) | 768 | 0 | 0 / 1 | Colo Colo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1987 | 16 | 240 (240) | 579 | 0 | 0 / 1 | Universidad Católica | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1988 | 16 | 240 (240) | 599 | 0 | 0 / 1 | Cobreloa | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1989 | 16 | 240 (240) | 604 | 0 | 0 / 1 | Colo Colo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1990 | 16 | 240 (240) | 686 | 0 | 0 / 1 | Colo Colo | RSSSF (chilehist:1476) |
| 1991 | 16 | 240 (240) | 658 | 0 | 0 / 1 | Colo Colo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1992 | 16 | 240 (240) | 684 | 0 | 1 / 0 | Cobreloa | RSSSF (chilehist) |
| 1993 | 16 | 240 (240) | 588 | 0 | 0 / 1 | Colo Colo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1994 | 16 | 240 (240) | 727 | 0 | 1 / 0 | Universidad de Chile | RSSSF (chilehist) |
| 1995 | 16 | 240 (240) | 718 | 0 | 1 / 0 | Universidad de Chile | RSSSF (chilehist) |
| 1996 | 16 | 240 (240) | 769 | 0 | 1 / 0 | Colo Colo | RSSSF (chile96) |
| 1997 Apertura | 16 | 122 (122) | 362 | 0 | 1 / 0 | Universidad Católica | RSSSF (chile97:20) |
| 1997 Clausura | 16 | 120 (120) | 338 | 0 | 1 / 0 | Colo Colo | RSSSF (chile97) |
| 1998 | 16 | 240 (240) | 695 | 0 | 1 / 0 | Colo Colo | RSSSF (chile98) |
| 1999 | 16 | 352 (352) | 1127 | 0 | 1 / 2 | Universidad de Chile | RSSSF (chile99) |
| 2000 | 16 | 240 (240) | 715 | 617 | 1 / 0 | Universidad de Chile | RSSSF (chile00) |
| 2001 | 16 | 240 (240) | 719 | 710 | 0 / 1 | Santiago Wanderers | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2002 Apertura | 16 | 147 (147) | 480 | 474 | 4 / 0 | Universidad Católica | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2002 Clausura | 16 | 146 (146) | 407 | 398 | 4 / 0 | Colo Colo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2003 Apertura | 16 | 147 (147) | 489 | 485 | 4 / 0 | Cobreloa | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2003 Clausura | 16 | 147 (147) | 509 | 493 | 4 / 0 | Cobreloa | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2004 Apertura | 18 | 182 (182) | 606 | 592 | 4 / 0 | Universidad de Chile | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2004 Clausura | 18 | 180 (180) | 563 | 553 | 3 / 1 | Cobreloa | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2005 Apertura | 20 | 207 (207) | 591 | 575 | 4 / 0 | Unión Española | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2005 Clausura | 20 | 205 (205) | 558 | 555 | 4 / 0 | Universidad Católica | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2006 Apertura | 19 | 188 (188) | 571 | 570 | 4 / 0 | Colo Colo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2006 Clausura | 19 | 186 (186) | 548 | 548 | 4 / 0 | Colo Colo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2007 Apertura | 21 | 210 (210) | 617 | 617 | 1 / 0 | Colo Colo | RSSSF (chile07) |
| 2007 Clausura | 21 | 225 (225) | 656 | 656 | 4 / 0 | Colo Colo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2008 Apertura | 20 | 205 (205) | 613 | 610 | 4 / 0 | Everton de Viña del Mar | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2008 Clausura | 20 | 188 (188) | 605 | 605 | 4 / 0 | Colo Colo | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2009 Apertura | 18 | 155 (155) | 466 | 466 | 1 / 0 | Universidad de Chile | RSSSF (chile09) |
| 2009 Clausura | 18 | 168 (167) | 467 | 461 | 1 / 0 | Colo Colo | RSSSF (chile09) |
| 2010 | 18 | 307 (306) | 901 | 901 | 1 / 0 | Universidad Católica | RSSSF (chile2010) |
| 2011 Apertura | 18 | 167 (167) | 492 | 489 | 1 / 0 | Universidad de Chile | RSSSF (chile2011:34) |
| 2011 Clausura | 18 | 167 (167) | 499 | 499 | 1 / 0 | Universidad de Chile | RSSSF (chile2011) |
| 2012 Apertura | 18 | 167 (167) | 475 | 464 | 1 / 0 | Universidad de Chile | RSSSF (chile2012) |
| 2012 Clausura | 18 | 167 (167) | 467 | 463 | 0 / 1 | Huachipato | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2013 Transición | 18 | 153 (153) | 463 | 456 | 1 / 0 | Unión Española | RSSSF (chile2013) |
| 2013/14 Apertura | 18 | 154 (154) | 395 | 388 | 1 / 0 | O'Higgins | RSSSF (chile2014) |
| 2013/14 Clausura | 18 | 153 (153) | 428 | 184 | 1 / 0 | Colo Colo | RSSSF (chile2014) |
| 2014/15 Apertura | 18 | 153 (153) | 425 | 316 | 1 / 0 | Universidad de Chile | RSSSF (chile2015) |
| 2014/15 Clausura | 18 | 153 (153) | 469 | 434 | 1 / 0 | Cobresal | RSSSF (chile2015) |
| 2015/16 Apertura | 16 | 120 (120) | 347 | 341 | 1 / 0 | Colo Colo | RSSSF (chile2016) |
| 2015/16 Clausura | 16 | 120 (120) | 356 | 352 | 1 / 0 | Universidad Católica | RSSSF (chile2016) |
| 2016/17 Apertura | 16 | 120 (120) | 347 | 347 | 1 / 0 | Universidad Católica | RSSSF (chile2017) |
| 2016/17 Clausura | 16 | 120 (120) | 329 | 329 | 1 / 0 | Universidad de Chile | RSSSF (chile2017) |
| 2017 Transición | 16 | 120 (120) | 276 | 272 | 1 / 0 | Colo Colo | RSSSF (chile2017a) |
| 2018 | 16 | 240 (240) | 621 | 621 | 1 / 0 | Universidad Católica | RSSSF (chile2018) |
| 2019 | 16 | 195 (194) | 514 | 512 | 1 / 0 | Universidad Católica | RSSSF (chile2019) |
| 2020 | 18 | 308 (307) | 791 | 687 | 1 / 0 | Universidad Católica | RSSSF (chile2020) |
| 2021 | 17 | 272 (272) | 683 | 679 | 1 / 0 | Universidad Católica | RSSSF (chile2021) |
| 2022 | 16 | 240 (240) | 616 | 613 | 1 / 0 | Colo Colo | RSSSF (chile2022) |
| 2023 | 16 | 241 (240) | 654 | 640 | 1 / 0 | Huachipato | RSSSF (chile2023) |
| 2024 | 16 | 240 (239) | 661 | 661 | 1 / 0 | Colo Colo | RSSSF (chile2024) |
| 2025 | 16 | 240 (240) | 635 | 631 | 1 / 0 | Coquimbo Unido | RSSSF (chile2025) |

## Conferência e correções, edição a edição

### 1933

- ogol: 23 jogos casados (edição 37111 do ogol, 29 jogos)

### 1934

- sem ocorrências

### 1935

- sem ocorrências

### 1936

- ogol: 30 jogos casados (edição 37108 do ogol, 30 jogos)
- placar diferente no ogol — Unión Española x Colo Colo (None): RSSSF 2-3, ogol 3-3; fica o da RSSSF
- placar diferente no ogol — Magallanes x Colo Colo (None): RSSSF 1-3, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Unión Española (None): RSSSF 3-3, ogol 3-2; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Magallanes (None): RSSSF 1-2, ogol 3-1; fica o da RSSSF

### 1937

- tabela publicada x jogos — chile37:159: Universidad de Chile tabela [9, 8, 1, 0, 47, 10] jogos [0, 0, 0, 0, 0, 0] — faltam 9 jogo(s) do clube na página
- W.O./pontos para o mandante — Badminton 3-4 Santiago Wanderers (s/d): (win awarded to Badminton)
- W.O./pontos para o visitante — Santiago Wanderers 2-1 Magallanes (s/d): (win awarded to Magallanes)
- W.O./pontos para o visitante — Santiago Wanderers 2-1 Unión Española (s/d): (win awarded to Unión Española)
- W.O./pontos para o visitante — Audax Italiano 2-1 Unión Española (s/d): (win awarded to Unión Española)
- W.O./pontos para o visitante — Badminton 6-6 Magallanes (s/d): (win awarded to Magallanes)
- W.O./pontos para o visitante — Unión Española 1-1 Magallanes (s/d): (win awarded to Magallanes)

### 1938

- ogol: 42 jogos casados (edição 37106 do ogol, 42 jogos)

### 1939

- ogol: 100 jogos casados (edição 37105 do ogol, 109 jogos)

### 1940

- ogol: 90 jogos casados (edição 36397 do ogol, 90 jogos)

### 1941

- ogol: 90 jogos casados (edição 37104 do ogol, 90 jogos)
- tabela publicada x jogos — chilehist:143: Santiago National tabela [18, 6, 4, 8, 36, 48] jogos [18, 5, 4, 9, 36, 48] — a outra tabela publicada (chile41) fecha com os jogos: o erro é desta tabela
- placar diferente no ogol — Green Cross de Santiago x Universidad Católica (None): RSSSF 2-3, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x Universidad Católica (None): RSSSF 1-2, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Universidad Católica x Universidad de Chile (None): RSSSF 2-3, ogol 0-3; fica o da RSSSF
- não jogado — Green Cross de Santiago Unión Española (s/d)
- não jogado — Badminton Colo Colo (s/d)

### 1942

- ogol: 90 jogos casados (edição 37103 do ogol, 90 jogos)
- placar diferente no ogol — Magallanes x Colo Colo (None): RSSSF 1-1, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Green Cross de Santiago x Badminton (None): RSSSF 3-2, ogol 4-2; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Magallanes (None): RSSSF 0-2, ogol 1-1; fica o da RSSSF
- decidido fora de campo — Santiago National Colo Colo (s/d): awarded 0-1, originally 2-1

### 1943

- ogol: 90 jogos casados (edição 37102 do ogol, 90 jogos)

### 1944

- ogol: 131 jogos casados (edição 37101 do ogol, 132 jogos)
- placar diferente no ogol — Santiago Wanderers x Green Cross de Santiago (None): RSSSF 3-2, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — Everton de Viña del Mar x Colo Colo (None): RSSSF 0-3, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Universidad Católica (None): RSSSF 1-2, ogol 6-2; fica o da RSSSF
- placar diferente no ogol — Everton de Viña del Mar x Santiago National (None): RSSSF 2-1, ogol 0-3; fica o da RSSSF
- placar diferente no ogol — Unión Española x Santiago Wanderers (None): RSSSF 2-1, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Audax Italiano (None): RSSSF 0-3, ogol 3-3; fica o da RSSSF
- placar diferente no ogol — Green Cross de Santiago x Santiago Wanderers (None): RSSSF 2-2, ogol 2-3; fica o da RSSSF
- placar diferente no ogol — Universidad Católica x Santiago Wanderers (None): RSSSF 2-6, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Unión Española (None): RSSSF 2-2, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Audax Italiano x Santiago Wanderers (None): RSSSF 3-3, ogol 3-0; fica o da RSSSF
- W.O./pontos para o visitante — Everton de Viña del Mar 2-1 Santiago National (s/d): (win awarded to Santiago National)

### 1945

- ogol: 132 jogos casados (edição 37100 do ogol, 132 jogos)
- placar diferente no ogol — Santiago Wanderers x Everton de Viña del Mar (None): RSSSF 2-2, ogol 1-4; fica o da RSSSF
- placar diferente no ogol — Universidad Católica x Santiago Wanderers (None): RSSSF 1-1, ogol 6-3; fica o da RSSSF
- placar diferente no ogol — Audax Italiano x Universidad Católica (None): RSSSF 9-2, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Colo Colo (None): RSSSF 0-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Santiago Morning x Santiago Wanderers (None): RSSSF 1-4, ogol 4-1; fica o da RSSSF
- placar diferente no ogol — Badminton x Santiago Wanderers (None): RSSSF 0-2, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Universidad de Chile (None): RSSSF 1-4, ogol 3-2; fica o da RSSSF
- placar diferente no ogol — Everton de Viña del Mar x Santiago Wanderers (None): RSSSF 4-1, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Universidad Católica (None): RSSSF 3-6, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Santiago Wanderers (None): RSSSF 1-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Universidad Católica x Audax Italiano (None): RSSSF 0-1, ogol 2-9; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Santiago Morning (None): RSSSF 1-4, ogol 4-1; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Badminton (None): RSSSF 1-0, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x Santiago Wanderers (None): RSSSF 2-3, ogol 4-1; fica o da RSSSF

### 1946

- ogol: 150 jogos casados (edição 37099 do ogol, 192 jogos)
- tabela publicada x jogos — chile46:18: Santiago Morning tabela [24, 8, 6, 10, 50, 52] jogos [24, 7, 6, 11, 48, 52] — a outra tabela publicada (chile46) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile46:18: Santiago National tabela [24, 4, 6, 14, 47, 79] jogos [24, 5, 6, 13, 47, 77] — a outra tabela publicada (chile46) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile46:407: Santiago Morning tabela [30, 8, 8, 14, 60, 69] jogos [30, 7, 8, 15, 58, 69] — a outra tabela publicada (chile46) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile46:407: Santiago National tabela [30, 6, 6, 18, 59, 98] jogos [30, 7, 6, 17, 59, 96] — a outra tabela publicada (chile46) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chilehist:232: Santiago Morning tabela [24, 8, 6, 10, 50, 52] jogos [24, 7, 6, 11, 48, 52] — a outra tabela publicada (chile46) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chilehist:232: Santiago National tabela [24, 4, 6, 14, 47, 79] jogos [24, 5, 6, 13, 47, 77] — a outra tabela publicada (chile46) fecha com os jogos: o erro é desta tabela
- placar diferente no ogol — Santiago Wanderers x Audax Italiano (None): RSSSF 2-1, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Santiago Morning x Colo Colo (None): RSSSF 1-0, ogol 5-1; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Badminton (None): RSSSF 5-2, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Everton de Viña del Mar x Colo Colo (None): RSSSF 1-2, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Unión Española (None): RSSSF 2-5, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Santiago National x Colo Colo (None): RSSSF 1-5, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — Green Cross de Santiago x Santiago Wanderers (None): RSSSF 2-2, ogol 4-3; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Universidad de Chile (None): RSSSF 2-2, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Santiago Morning (None): RSSSF 1-5, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Badminton x Santiago Wanderers (None): RSSSF 0-1, ogol 2-5; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Everton de Viña del Mar (None): RSSSF 0-2, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Audax Italiano (None): RSSSF 3-3, ogol 0-2; fica o da RSSSF
- placar diferente no ogol — Unión Española x Santiago Wanderers (None): RSSSF 0-2, ogol 5-2; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Santiago National (None): RSSSF 2-2, ogol 5-1; fica o da RSSSF

### 1947

- ogol: 132 jogos casados (edição 37098 do ogol, 156 jogos)
- tabela publicada x jogos — chile47:40: Universidad Católica tabela [24, 9, 8, 7, 47, 39] jogos [24, 9, 8, 7, 45, 39] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile47:40: Green Cross de Santiago tabela [24, 10, 3, 11, 45, 51] jogos [24, 10, 3, 11, 45, 49] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- placar diferente no ogol — Santiago Wanderers x Unión Española (None): RSSSF 1-4, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Santiago National (None): RSSSF 4-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Badminton x Colo Colo (None): RSSSF 1-1, ogol 2-4; fica o da RSSSF
- placar diferente no ogol — Badminton x Santiago Wanderers (None): RSSSF 1-1, ogol 4-2; fica o da RSSSF
- placar diferente no ogol — Magallanes x Santiago Wanderers (None): RSSSF 1-1, ogol 2-4; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Santiago National (None): RSSSF 3-1, ogol 5-0; fica o da RSSSF
- placar diferente no ogol — Everton de Viña del Mar x Colo Colo (None): RSSSF 0-2, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x Santiago Wanderers (None): RSSSF 1-1, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Magallanes (None): RSSSF 1-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Audax Italiano x Santiago Wanderers (None): RSSSF 0-1, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Unión Española x Santiago Wanderers (None): RSSSF 1-3, ogol 4-1; fica o da RSSSF
- placar diferente no ogol — Santiago National x Santiago Wanderers (None): RSSSF 0-1, ogol 1-4; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Badminton (None): RSSSF 4-2, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Badminton (None): RSSSF 2-4, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Santiago National x Colo Colo (None): RSSSF 0-5, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Magallanes (None): RSSSF 4-2, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Universidad de Chile (None): RSSSF 0-2, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Magallanes x Colo Colo (None): RSSSF 0-1, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Audax Italiano (None): RSSSF 1-2, ogol 1-0; fica o da RSSSF

### 1948

- ogol: 132 jogos casados (edição 37097 do ogol, 156 jogos)
- tabela publicada x jogos — chile48:16: Santiago Morning tabela [24, 11, 5, 8, 47, 40] jogos [24, 10, 6, 8, 46, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile48:16: Santiago National tabela [24, 4, 0, 20, 39, 80] jogos [24, 4, 1, 19, 39, 79] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- placar diferente no ogol — Santiago Wanderers x Colo Colo (None): RSSSF 1-3, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Everton de Viña del Mar x Colo Colo (None): RSSSF 1-1, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Santiago Wanderers (None): RSSSF 0-2, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Everton de Viña del Mar (None): RSSSF 2-1, ogol 1-1; fica o da RSSSF

### 1949

- ogol: 110 jogos casados (edição 37096 do ogol, 132 jogos)
- placar diferente no ogol — Magallanes x Santiago Wanderers (None): RSSSF 0-2, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Green Cross de Santiago x Santiago Wanderers (None): RSSSF 0-2, ogol 0-4; fica o da RSSSF
- placar diferente no ogol — Universidad Católica x Santiago Wanderers (None): RSSSF 0-0, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Colo Colo (None): RSSSF 1-1, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Santiago Morning x Santiago Wanderers (None): RSSSF 3-3, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Magallanes (None): RSSSF 1-3, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Green Cross de Santiago (None): RSSSF 4-0, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Universidad Católica (None): RSSSF 0-2, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Santiago Wanderers (None): RSSSF 1-2, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Santiago Morning (None): RSSSF 3-1, ogol 3-3; fica o da RSSSF

### 1950

- ogol: 111 jogos casados (edição 37095 do ogol, 133 jogos)
- placar diferente no ogol — Santiago Morning x Colo Colo (None): RSSSF 1-3, ogol 3-0; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Everton de Viña del Mar (None): RSSSF 0-2, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Unión Española (None): RSSSF 0-4, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — Santiago Morning x Santiago Wanderers (None): RSSSF 1-2, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Santiago Morning (None): RSSSF 0-3, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Everton de Viña del Mar x Santiago Wanderers (None): RSSSF 1-3, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Unión Española x Colo Colo (None): RSSSF 2-2, ogol 4-0; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Santiago Morning (None): RSSSF 1-1, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Santiago Morning x Universidad Católica (None): RSSSF 4-1, ogol 1-4; fica o da RSSSF

### 1951

- ogol: 1 jogos casados (edição 37094 do ogol, 1 jogos)
- tabela publicada x jogos — chile51:18: Colo Colo tabela [22, 11, 6, 5, 45, 35] jogos [22, 11, 6, 5, 45, 34] — a outra tabela publicada (chile51) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile51:18: Santiago Wanderers tabela [22, 6, 6, 10, 35, 39] jogos [22, 6, 6, 10, 34, 39] — a outra tabela publicada (chile51) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile51:273: Colo Colo tabela [27, 13, 6, 8, 52, 42] jogos [27, 13, 6, 8, 52, 41] — a outra tabela publicada (chile51) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile51:332: Santiago Wanderers tabela [27, 8, 8, 11, 42, 46] jogos [27, 8, 8, 11, 41, 46] — a outra tabela publicada (chile51) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chilehist:318: Unión Española tabela [27, 15, 6, 6, 72, 54] jogos [22, 11, 5, 6, 53, 44] — a outra tabela publicada (chile51) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chilehist:318: Audax Italiano tabela [27, 16, 4, 7, 55, 42] jogos [22, 13, 4, 5, 44, 29] — a outra tabela publicada (chile51) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chilehist:318: Colo Colo tabela [27, 13, 6, 8, 52, 42] jogos [22, 11, 6, 5, 45, 34] — a outra tabela publicada (chile51) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chilehist:318: Everton de Viña del Mar tabela [27, 13, 5, 9, 63, 50] jogos [22, 12, 5, 5, 54, 36] — a outra tabela publicada (chile51) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chilehist:318: Santiago Morning tabela [27, 13, 4, 10, 61, 42] jogos [22, 11, 4, 7, 50, 30] — a outra tabela publicada (chile51) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chilehist:318: Universidad de Chile tabela [27, 10, 10, 7, 38, 38] jogos [22, 8, 9, 5, 33, 32] — a outra tabela publicada (chile51) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chilehist:318: Santiago Wanderers tabela [22, 6, 6, 10, 35, 39] jogos [22, 6, 6, 10, 34, 39] — a outra tabela publicada (chile51) fecha com os jogos: o erro é desta tabela

### 1952

- sem ocorrências

### 1953

- tabela publicada x jogos — chile53:16: Green Cross de Santiago tabela [26, 11, 5, 10, 49, 49] jogos [26, 10, 7, 9, 49, 49] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1954

- sem ocorrências

### 1955

- sem ocorrências

### 1956

- sem ocorrências

### 1957

- sem ocorrências

### 1958

- ogol: 182 jogos casados (edição 37087 do ogol, 182 jogos)
- placar diferente no ogol — Everton de Viña del Mar x Green Cross de Santiago (None): RSSSF 2-1, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Deportes La Serena x Colo Colo (None): RSSSF 2-4, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Palestino x Colo Colo (None): RSSSF 2-2, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Deportes La Serena (None): RSSSF 1-3, ogol 4-2; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Palestino (None): RSSSF 1-1, ogol 2-2; fica o da RSSSF

### 1959

- ogol: 1 jogos casados (edição 36398 do ogol, 1 jogos)

### 1960

- ogol: 181 jogos casados (edição 37086 do ogol, 182 jogos)
- placar diferente no ogol — Everton de Viña del Mar x Universidad de Chile (None): RSSSF 3-2, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x San Luis de Quillota (None): RSSSF 1-0, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — Everton de Viña del Mar x Colo Colo (None): RSSSF 1-2, ogol 4-0; fica o da RSSSF
- placar diferente no ogol — O'Higgins x Universidad Católica (None): RSSSF 1-1, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Everton de Viña del Mar x Unión Española (None): RSSSF 3-4, ogol 5-1; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x Everton de Viña del Mar (None): RSSSF 1-2, ogol 2-3; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Everton de Viña del Mar (None): RSSSF 0-4, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Universidad Católica x O'Higgins (None): RSSSF 0-2, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Unión Española x Everton de Viña del Mar (None): RSSSF 1-5, ogol 4-3; fica o da RSSSF
- placar diferente no ogol — Santiago Morning x Rangers de Talca (None): RSSSF 1-2, ogol 2-1; fica o da RSSSF

### 1961

- ogol: 184 jogos casados (edição 37085 do ogol, 184 jogos)
- tabela publicada x jogos — chile61:16: Palestino tabela [26, 11, 3, 12, 47, 60] jogos [26, 11, 3, 12, 49, 60] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile61:16: Ferrobádminton tabela [26, 7, 8, 11, 38, 52] jogos [26, 7, 8, 11, 38, 53] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — chile61:16: San Luis de Quillota tabela [26, 5, 5, 16, 36, 58] jogos [26, 5, 5, 16, 36, 59] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- placar diferente no ogol — Palestino x San Luis de Quillota (None): RSSSF 4-1, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Universidad Católica x O'Higgins (None): RSSSF 2-1, ogol 3-1; fica o da RSSSF

### 1962

- ogol: 305 jogos casados (edição 36399 do ogol, 307 jogos)
- tabela publicada x jogos — chile62:16: Santiago Wanderers tabela [34, 12, 11, 11, 49, 50] jogos [34, 12, 11, 11, 50, 51] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile62:16: Palestino tabela [34, 7, 14, 13, 44, 59] jogos [34, 7, 14, 13, 45, 60] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- placar diferente no ogol — Deportes La Serena x Colo Colo (None): RSSSF 3-2, ogol 3-3; fica o da RSSSF
- placar diferente no ogol — San Luis de Quillota x Santiago Wanderers (None): RSSSF 2-2, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Santiago Morning x Colo Colo (None): RSSSF 2-2, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Deportes La Serena x Santiago Wanderers (None): RSSSF 4-2, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Unión San Felipe x Santiago Wanderers (None): RSSSF 0-1, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Palestino (None): RSSSF 2-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x O'Higgins (None): RSSSF 0-2, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — Santiago Morning x Santiago Wanderers (None): RSSSF 2-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Ferrobádminton x Santiago Wanderers (None): RSSSF 2-0, ogol 2-3; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Deportes La Serena (None): RSSSF 3-3, ogol 2-3; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x San Luis de Quillota (None): RSSSF 1-1, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Santiago Morning (None): RSSSF 1-2, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Deportes La Serena (None): RSSSF 0-1, ogol 2-4; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Unión San Felipe (None): RSSSF 3-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Palestino x Santiago Wanderers (None): RSSSF 0-0, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — O'Higgins x Santiago Wanderers (None): RSSSF 2-2, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Santiago Morning (None): RSSSF 0-1, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Ferrobádminton (None): RSSSF 3-2, ogol 0-2; fica o da RSSSF

### 1963

- ogol: 306 jogos casados (edição 37084 do ogol, 306 jogos)
- tabela publicada x jogos — chile63:16: Deportes La Serena tabela [34, 18, 7, 9, 64, 54] jogos [34, 18, 7, 9, 63, 53] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile63:16: O'Higgins tabela [34, 10, 4, 20, 41, 58] jogos [34, 10, 4, 20, 40, 57] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- placar diferente no ogol — San Luis de Quillota x Colo Colo (None): RSSSF 2-6, ogol 0-3; fica o da RSSSF
- placar diferente no ogol — Unión Española x Colo Colo (None): RSSSF 2-3, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Rangers de Talca x Santiago Wanderers (None): RSSSF 1-1, ogol 2-3; fica o da RSSSF
- placar diferente no ogol — Everton de Viña del Mar x Santiago Wanderers (None): RSSSF 1-0, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Ferrobádminton (None): RSSSF 0-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x Deportes La Serena (None): RSSSF 1-1, ogol 2-3; fica o da RSSSF
- placar diferente no ogol — Palestino x Colo Colo (None): RSSSF 2-5, ogol 1-4; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Universidad Católica (None): RSSSF 2-2, ogol 0-3; fica o da RSSSF
- placar diferente no ogol — Everton de Viña del Mar x Universidad de Chile (None): RSSSF 2-7, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — O'Higgins x Universidad de Chile (None): RSSSF 1-3, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Colo Colo x San Luis de Quillota (None): RSSSF 3-0, ogol 6-2; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Unión Española (None): RSSSF 2-1, ogol 3-2; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Rangers de Talca (None): RSSSF 3-2, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Everton de Viña del Mar (None): RSSSF 1-0, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Ferrobádminton x Santiago Wanderers (None): RSSSF 1-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Deportes La Serena x Universidad de Chile (None): RSSSF 3-2, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Palestino (None): RSSSF 4-1, ogol 5-2; fica o da RSSSF
- placar diferente no ogol — Universidad Católica x Santiago Wanderers (None): RSSSF 3-0, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x Everton de Viña del Mar (None): RSSSF 1-0, ogol 7-2; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x O'Higgins (None): RSSSF 2-1, ogol 3-1; fica o da RSSSF

### 1964

- ogol: 306 jogos casados (edição 36400 do ogol, 306 jogos)
- tabela publicada x jogos — chile64:16: Colo Colo tabela [34, 18, 4, 12, 75, 52] jogos [34, 18, 4, 12, 75, 51] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile64:16: Unión San Felipe tabela [34, 8, 10, 16, 51, 70] jogos [34, 8, 10, 16, 50, 70] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — Unión La Calera x Santiago Wanderers (None): RSSSF 1-2, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — Rangers de Talca x Colo Colo (None): RSSSF 2-5, ogol 2-3; fica o da RSSSF
- placar diferente no ogol — Everton de Viña del Mar x Unión Española (None): RSSSF 3-2, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Unión La Calera (None): RSSSF 3-1, ogol 2-1; fica o da RSSSF

### 1965

- ogol: 306 jogos casados (edição 36401 do ogol, 306 jogos)
- tabela publicada x jogos — chile65:16: Unión Española tabela [34, 12, 7, 15, 73, 65] jogos [34, 12, 7, 15, 74, 66] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile65:16: San Luis de Quillota tabela [34, 5, 13, 16, 45, 66] jogos [34, 5, 13, 16, 46, 67] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — Audax Italiano x Colo Colo (None): RSSSF 3-1, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — Santiago Morning x Colo Colo (None): RSSSF 0-1, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Unión Española x Colo Colo (None): RSSSF 2-4, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Audax Italiano (None): RSSSF 3-1, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Santiago Morning (None): RSSSF 1-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Unión Española (None): RSSSF 1-1, ogol 4-2; fica o da RSSSF

### 1966

- ogol: 305 jogos casados (edição 37083 do ogol, 306 jogos)
- placar diferente no ogol — Magallanes x Universidad de Chile (None): RSSSF 1-0, ogol 2-4; fica o da RSSSF
- placar diferente no ogol — Santiago Morning x Universidad Católica (None): RSSSF 0-7, ogol 2-3; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x Palestino (None): RSSSF 1-3, ogol 0-3; fica o da RSSSF
- placar diferente no ogol — Santiago Morning x Palestino (None): RSSSF 1-0, ogol 0-4; fica o da RSSSF
- placar diferente no ogol — Palestino x Magallanes (None): RSSSF 1-2, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Palestino x Universidad Católica (None): RSSSF 1-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Ferrobádminton x Universidad de Chile (None): RSSSF 0-3, ogol 0-2; fica o da RSSSF
- placar diferente no ogol — Audax Italiano x Ferrobádminton (None): RSSSF 0-0, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x Colo Colo (None): RSSSF 2-0, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — Ferrobádminton x Santiago Morning (None): RSSSF 1-3, ogol 0-2; fica o da RSSSF
- placar diferente no ogol — Santiago Morning x Colo Colo (None): RSSSF 1-1, ogol 0-2; fica o da RSSSF
- placar diferente no ogol — Palestino x Colo Colo (None): RSSSF 1-2, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Universidad Católica x Universidad de Chile (None): RSSSF 3-5, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x Magallanes (None): RSSSF 4-2, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Universidad Católica x Santiago Morning (None): RSSSF 3-2, ogol 7-0; fica o da RSSSF
- placar diferente no ogol — Palestino x Universidad de Chile (None): RSSSF 3-0, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Palestino x Santiago Morning (None): RSSSF 4-0, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Magallanes x Palestino (None): RSSSF 1-0, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Universidad Católica x Palestino (None): RSSSF 1-1, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x Ferrobádminton (None): RSSSF 2-0, ogol 3-0; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Universidad de Chile (None): RSSSF 3-1, ogol 0-2; fica o da RSSSF
- placar diferente no ogol — Ferrobádminton x Audax Italiano (None): RSSSF 2-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Santiago Morning x Ferrobádminton (None): RSSSF 2-0, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Santiago Morning (None): RSSSF 2-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Palestino (None): RSSSF 1-3, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x Universidad Católica (None): RSSSF 1-1, ogol 5-3; fica o da RSSSF

### 1967

- sem ocorrências

### 1968

- ogol: 308 jogos casados (edição 37082 do ogol, 327 jogos)
- tabela publicada x jogos — chilehist:727: O'Higgins tabela [18, 4, 3, 11, 22, 30] jogos [18, 5, 3, 10, 22, 30] — a outra tabela publicada (chile68) fecha com os jogos: o erro é desta tabela
- corrigido — Deportes La Serena x Everton de Viña del Mar (None): quadrangular do 5º lugar do Provincial ("Fifth Place Playoff:"), não a 1ª fase (CH-022)
- corrigido — Rangers de Talca x Unión La Calera (None): quadrangular do 5º lugar do Provincial ("Fifth Place Playoff:"), não a 1ª fase (CH-022)
- corrigido — Everton de Viña del Mar x Unión La Calera (None): quadrangular do 5º lugar do Provincial ("Fifth Place Playoff:"), não a 1ª fase (CH-022)
- corrigido — Deportes La Serena x Rangers de Talca (None): quadrangular do 5º lugar do Provincial ("Fifth Place Playoff:"), não a 1ª fase (CH-022)
- corrigido — Everton de Viña del Mar x Rangers de Talca (None): quadrangular do 5º lugar do Provincial ("Fifth Place Playoff:"), não a 1ª fase (CH-022)
- corrigido — Deportes La Serena x Unión La Calera (None): quadrangular do 5º lugar do Provincial ("Fifth Place Playoff:"), não a 1ª fase (CH-022)
- placar diferente no ogol — Universidad Católica x Magallanes (None): RSSSF 0-0, ogol 2-2; fica o da RSSSF

### 1969

- ogol: 8 jogos casados (edição 36403 do ogol, 11 jogos)
- tabela publicada x jogos — chile69:297: Deportes La Serena tabela [18, 6, 5, 7, 24, 25] jogos [18, 6, 5, 7, 25, 29] — a outra tabela publicada (chile69) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile69:297: Magallanes tabela [18, 5, 5, 8, 27, 34] jogos [18, 5, 5, 8, 26, 30] — a outra tabela publicada (chile69) fecha com os jogos: o erro é desta tabela

### 1970

- tabela publicada x jogos — chile70:293: Universidad Católica tabela [18, 10, 2, 6, 32, 27] jogos [18, 10, 2, 6, 35, 27] — a outra tabela publicada (chile70) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile70:293: Audax Italiano tabela [18, 7, 2, 9, 18, 21] jogos [18, 6, 4, 8, 18, 21] — a outra tabela publicada (chile70) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile70:304: Everton de Viña del Mar tabela [18, 11, 3, 4, 34, 22] jogos [18, 11, 3, 4, 33, 19] — a outra tabela publicada (chile70) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile70:304: Deportes Temuco tabela [18, 6, 6, 6, 24, 21] jogos [18, 6, 6, 6, 22, 21] — a outra tabela publicada (chile70) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile70:304: Magallanes tabela [18, 6, 5, 7, 29, 30] jogos [18, 6, 5, 7, 28, 29] — a outra tabela publicada (chile70) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chilehist:909: Everton de Viña del Mar tabela [18, 11, 3, 4, 34, 22] jogos [18, 11, 3, 4, 33, 19] — a outra tabela publicada (chile70) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chilehist:909: Deportes Temuco tabela [18, 6, 6, 6, 24, 21] jogos [18, 6, 6, 6, 22, 21] — a outra tabela publicada (chile70) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chilehist:909: Magallanes tabela [18, 6, 5, 7, 29, 30] jogos [18, 6, 5, 7, 28, 29] — a outra tabela publicada (chile70) fecha com os jogos: o erro é desta tabela

### 1971

- ogol: 296 jogos casados (edição 37080 do ogol, 307 jogos)
- placar diferente no ogol — Unión Española x Universidad Católica (None): RSSSF 2-1, ogol 4-1; fica o da RSSSF
- placar diferente no ogol — Magallanes x Unión Española (None): RSSSF 1-2, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x Magallanes (None): RSSSF 3-0, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Universidad Católica x Audax Italiano (None): RSSSF 1-1, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Magallanes (None): RSSSF 1-2, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x Audax Italiano (None): RSSSF 5-2, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — O'Higgins x Deportes Antofagasta (None): RSSSF 2-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Deportes Antofagasta x Huachipato (None): RSSSF 0-2, ogol 2-0; fica o da RSSSF

### 1972

- ogol: 302 jogos casados (edição 37079 do ogol, 306 jogos)
- placar diferente no ogol — Naval de Talcahuano x Huachipato (None): RSSSF 1-1, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — Unión Española x Universidad de Chile (None): RSSSF 0-1, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Universidad Católica x Unión San Felipe (None): RSSSF 1-1, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Magallanes x Deportes Antofagasta (None): RSSSF 5-2, ogol 5-3; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Magallanes (None): RSSSF 5-0, ogol 5-1; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Unión Española (None): RSSSF 0-0, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x Unión Española (None): RSSSF 0-2, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — O'Higgins x Santiago Wanderers (None): RSSSF 3-2, ogol 0-2; fica o da RSSSF

### 1973

- ogol: 306 jogos casados (edição 37078 do ogol, 306 jogos)
- tabela publicada x jogos — chile73:16: Huachipato tabela [34, 17, 9, 8, 52, 28] jogos [34, 17, 9, 8, 53, 28] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile73:16: O'Higgins tabela [34, 14, 15, 5, 50, 33] jogos [34, 14, 15, 5, 50, 32] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile73:16: Deportes La Serena tabela [34, 13, 10, 11, 43, 33] jogos [34, 13, 10, 11, 42, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile73:16: Deportes Antofagasta tabela [34, 12, 10, 12, 47, 46] jogos [34, 12, 10, 12, 47, 47] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile73:16: Universidad de Chile tabela [34, 10, 8, 16, 54, 64] jogos [34, 10, 8, 16, 52, 63] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile73:16: Palestino tabela [34, 8, 10, 16, 37, 58] jogos [34, 8, 10, 16, 38, 58] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile73:16: Naval de Talcahuano tabela [34, 7, 11, 16, 30, 53] jogos [34, 7, 11, 16, 29, 51] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile73:16: Unión San Felipe tabela [34, 10, 4, 20, 45, 72] jogos [34, 10, 4, 20, 44, 71] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile73:16: Universidad Católica tabela [34, 5, 11, 18, 43, 62] jogos [34, 5, 11, 18, 43, 63] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — Deportes La Serena x Unión San Felipe (None): RSSSF 2-0, ogol 3-0; fica o da RSSSF
- placar diferente no ogol — Palestino x Deportes La Serena (None): RSSSF 1-2, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Unión San Felipe x O'Higgins (None): RSSSF 1-5, ogol 2-5; fica o da RSSSF
- placar diferente no ogol — Deportes Antofagasta x Deportes La Serena (None): RSSSF 1-0, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Santiago Wanderers x Colo Colo (None): RSSSF 3-3, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Huachipato x Deportes Concepción (None): RSSSF 1-0, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Magallanes (None): RSSSF 2-2, ogol 3-3; fica o da RSSSF
- placar diferente no ogol — Universidad de Chile x Naval de Talcahuano (None): RSSSF 3-1, ogol 5-2; fica o da RSSSF
- placar diferente no ogol — Deportes La Serena x Deportes Antofagasta (None): RSSSF 2-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Deportes Concepción x Huachipato (None): RSSSF 0-0, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Colo Colo x Santiago Wanderers (None): RSSSF 1-2, ogol 3-3; fica o da RSSSF
- placar diferente no ogol — Deportes Antofagasta x Huachipato (None): RSSSF 0-2, ogol 0-1; fica o da RSSSF

### 1974

- ogol: 304 jogos casados (edição 37077 do ogol, 306 jogos)
- placar diferente no ogol — Deportes Temuco x Deportes La Serena (None): RSSSF 4-1, ogol 1-1; fica o da RSSSF

### 1975

- ogol: 307 jogos casados (edição 37076 do ogol, 307 jogos)
- placar diferente no ogol — Deportes Concepción x Deportes Aviación (None): RSSSF 3-2, ogol 2-2; fica o da RSSSF
- placar diferente no ogol — Unión Española x Everton de Viña del Mar (None): RSSSF 4-2, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Rangers de Talca x Palestino (None): RSSSF 0-3, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — Naval de Talcahuano x Magallanes (None): RSSSF 1-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Magallanes x O'Higgins (None): RSSSF 0-2, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Rangers de Talca x Magallanes (None): RSSSF 3-2, ogol 3-1; fica o da RSSSF

### 1976

- ogol: 307 jogos casados (edição 37075 do ogol, 308 jogos)
- tabela publicada x jogos — chile76:16: Deportes Temuco tabela [34, 16, 9, 9, 57, 38] jogos [34, 16, 9, 9, 57, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile76:16: Santiago Wanderers tabela [34, 11, 11, 12, 53, 61] jogos [34, 11, 11, 12, 53, 60] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile76:16: Lota Schwager tabela [34, 7, 13, 14, 48, 62] jogos [34, 7, 13, 14, 46, 62] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile76:16: Naval de Talcahuano tabela [34, 7, 8, 19, 39, 56] jogos [34, 7, 8, 19, 38, 56] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- placar diferente no ogol — Naval de Talcahuano x Santiago Wanderers (None): RSSSF 0-2, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Deportes Temuco x Lota Schwager (None): RSSSF 6-0, ogol 6-2; fica o da RSSSF

### 1977

- ogol: 306 jogos casados (edição 37074 do ogol, 307 jogos)
- tabela publicada x jogos — chile77:16: Deportes Aviación tabela [34, 12, 10, 12, 46, 51] jogos [34, 12, 10, 12, 45, 51] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile77:16: Deportes Temuco tabela [34, 10, 10, 14, 46, 62] jogos [34, 9, 12, 13, 46, 62] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — chile77:16: Deportes Ovalle tabela [34, 6, 15, 13, 42, 52] jogos [34, 9, 9, 16, 42, 51] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile77:16: Santiago Morning tabela [34, 9, 9, 16, 37, 50] jogos [34, 6, 15, 13, 37, 50] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- placar diferente no ogol — Deportes Aviación x Deportes Ovalle (None): RSSSF 0-3, ogol 1-3; fica o da RSSSF

### 1978

- ogol: 306 jogos casados (edição 37073 do ogol, 306 jogos)
- placar diferente no ogol — Rangers de Talca x Palestino (None): RSSSF 0-6, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Palestino x Rangers de Talca (None): RSSSF 2-1, ogol 6-0; fica o da RSSSF

### 1979

- ogol: 301 jogos casados (edição 37072 do ogol, 307 jogos)
- tabela publicada x jogos — chile79:220: Cobreloa tabela [34, 18, 8, 8, 61, 36] jogos [34, 18, 8, 8, 60, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile79:220: O'Higgins tabela [34, 18, 7, 9, 47, 40] jogos [34, 18, 7, 9, 46, 39] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- placar diferente no ogol — Universidad Católica x Unión Española (None): RSSSF 1-1, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — O'Higgins x Cobreloa (None): RSSSF 2-1, ogol 3-2; fica o da RSSSF
- placar diferente no ogol — Unión Española x Universidad Católica (None): RSSSF 1-0, ogol 1-1; fica o da RSSSF

### 1980

- ogol: 306 jogos casados (edição 36436 do ogol, 306 jogos)

### 1981

- ogol: 240 jogos casados (edição 37071 do ogol, 240 jogos)
- placar diferente no ogol — Universidad Católica x Palestino (None): RSSSF 0-2, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Palestino x Universidad Católica (None): RSSSF 1-1, ogol 2-0; fica o da RSSSF

### 1982

- ogol: 239 jogos casados (edição 36435 do ogol, 240 jogos)
- tabela publicada x jogos — chile82:255: Colo Colo tabela [30, 14, 11, 5, 41, 21] jogos [30, 14, 11, 5, 43, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile82:255: Universidad de Chile tabela [30, 15, 9, 6, 58, 38] jogos [30, 14, 10, 6, 58, 38] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile82:255: Regional Atacama tabela [30, 10, 8, 12, 36, 43] jogos [30, 10, 8, 12, 34, 41] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile82:255: Palestino tabela [30, 6, 12, 12, 30, 44] jogos [30, 6, 12, 12, 32, 46] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile82:255: Rangers de Talca tabela [30, 5, 5, 20, 25, 74] jogos [30, 5, 5, 20, 23, 72] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- placar diferente no ogol — Palestino x Colo Colo (None): RSSSF 2-2, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Rangers de Talca x Regional Atacama (None): RSSSF 0-0, ogol 2-2; fica o da RSSSF

### 1983

- ogol: 462 jogos casados (edição 37070 do ogol, 462 jogos)

### 1984

- duas zonas (Norte e Sul) de 13 clubes e um quadrangular final. As tabelas das zonas (chilehist.html) dão 26 jogos por clube: os 24 da zona e 2 interzonais. O calendário do ogol, a base deste ano, não tem os 26 jogos interzonais; nenhuma outra fonte que baixamos os traz. A classificação é calculada com os jogos que há
- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: 319 jogos casados (edição 37069 do ogol, 319 jogos)

### 1985

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: 380 jogos casados (edição 36434 do ogol, 380 jogos)
- tabela publicada x jogos — chilehist:1348: Everton de Viña del Mar tabela [38, 19, 12, 7, 43, 33] jogos [38, 18, 13, 7, 43, 33] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — chilehist:1348: San Luis de Quillota tabela [38, 8, 12, 18, 30, 48] jogos [38, 9, 11, 18, 30, 48] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — chilehist:1348: San Marcos de Arica tabela [38, 7, 13, 18, 40, 58] jogos [38, 7, 14, 17, 40, 58] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — chilehist:1348: O'Higgins tabela [38, 5, 11, 22, 40, 67] jogos [38, 5, 10, 23, 40, 67] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1986

- Everton e Rangers: a tabela da chilehist dá ao Everton 2 gols a mais contra o Rangers (33-38 e 33-42); só cabe no Everton 1-0 Rangers de 09/11/1986 (3-0 não muda vitórias, empates e derrotas), mas sem 3ª fonte fica o placar do ogol
- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: 305 jogos casados (edição 37068 do ogol, 307 jogos)
- tabela publicada x jogos — chilehist:1376: Everton de Viña del Mar tabela [34, 6, 17, 11, 33, 38] jogos [34, 6, 17, 11, 31, 38] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — chilehist:1376: Rangers de Talca tabela [34, 6, 17, 11, 33, 42] jogos [34, 6, 17, 11, 33, 40] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- corrigido — Cobreloa x San Luis de Quillota (1987-01-25): Cobreloa 1-1 San Luis: adversários trocados no ogol na última rodada de 1986 (25/01/1987); com os jogos dos rounds 5/22 e 7/24, os que faltam são o returno do round 17 (Cobreloa x San Luis e Rangers x Cobresal), e a tabela da chilehist decide o placar (Cobreloa 53-28 e Cobresal 53-35 só fecham assim) (CH-014)
- corrigido — Rangers de Talca x Cobresal (1987-01-25): Rangers 0-0 Cobresal: adversários trocados no ogol na última rodada de 1986 (25/01/1987); com os jogos dos rounds 5/22 e 7/24, os que faltam são o returno do round 17 (Cobreloa x San Luis e Rangers x Cobresal), e a tabela da chilehist decide o placar (Cobreloa 53-28 e Cobresal 53-35 só fecham assim) (CH-014)

### 1987

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: 240 jogos casados (edição 37067 do ogol, 240 jogos)
- tabela publicada x jogos — chilehist:1404: Everton de Viña del Mar tabela [30, 9, 11, 10, 33, 32] jogos [30, 9, 11, 10, 32, 32] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1988

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: 239 jogos casados (edição 36433 do ogol, 240 jogos)
- tabela publicada x jogos — chilehist:1428: Deportes Iquique tabela [30, 13, 8, 9, 46, 35] jogos [30, 13, 8, 9, 46, 34] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — chilehist:1428: Deportes Concepción tabela [30, 11, 7, 12, 30, 32] jogos [30, 11, 7, 12, 29, 32] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — chilehist:1428: Everton de Viña del Mar tabela [30, 10, 8, 12, 32, 39] jogos [30, 10, 8, 12, 31, 39] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — chilehist:1428: Unión Española tabela [30, 9, 8, 13, 34, 41] jogos [30, 9, 8, 13, 34, 40] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- corrigido — Naval de Talcahuano x O'Higgins (1988-08-28): o ogol repete O'Higgins 0-2 Naval; o jogo que falta é Naval 1-1 O'Higgins (CH-014)

### 1989

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: 240 jogos casados (edição 37066 do ogol, 240 jogos)
- tabela publicada x jogos — chilehist:1452: Unión Española tabela [30, 9, 12, 9, 45, 45] jogos [30, 9, 12, 9, 44, 44] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — chilehist:1452: Fernández Vial tabela [30, 5, 13, 12, 31, 44] jogos [30, 5, 13, 12, 30, 43] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1990

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: 240 jogos casados (edição 37065 do ogol, 240 jogos)
- tabela publicada x jogos — chilehist:1476: O'Higgins tabela [30, 15, 4, 11, 52, 45] jogos [30, 16, 3, 11, 53, 45] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — chilehist:1476: Cobresal tabela [30, 9, 11, 10, 34, 38] jogos [30, 9, 10, 11, 34, 39] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- corrigido — Universidad Católica x Everton de Viña del Mar (1990-07-22): Universidad Católica 2-1 Everton: o ogol erra; Transfermarkt e a tabela da RSSSF concordam (CH-013)
- corrigido — Unión Española x Deportes La Serena (1990-09-29): Unión Española 1-1 La Serena: o ogol erra; Transfermarkt e a tabela da RSSSF concordam (CH-013)
- corrigido — Huachipato x Palestino (1990-11-01): Huachipato 0-0 Palestino: o ogol erra; Transfermarkt e a tabela da RSSSF concordam (CH-013)

### 1991

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: 240 jogos casados (edição 37064 do ogol, 240 jogos)
- tabela publicada x jogos — chilehist:1503: Colo Colo tabela [30, 18, 8, 4, 57, 25] jogos [30, 17, 8, 5, 56, 26] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — chilehist:1503: Fernández Vial tabela [30, 13, 6, 11, 28, 33] jogos [30, 14, 6, 10, 29, 32] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- corrigido — O'Higgins x Deportes Concepción (1991-11-28): O'Higgins 4-2 Deportes Concepción: o ogol erra; Transfermarkt e a tabela da RSSSF concordam (CH-013)

### 1992

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: 240 jogos casados (edição 36432 do ogol, 240 jogos)

### 1993

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: 240 jogos casados (edição 37063 do ogol, 240 jogos)
- tabela publicada x jogos — chilehist:1563: Deportes La Serena tabela [30, 8, 11, 11, 23, 31] jogos [30, 8, 11, 11, 24, 32] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — chilehist:1563: Provincial Osorno tabela [30, 9, 8, 13, 23, 33] jogos [30, 9, 8, 13, 24, 34] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — chilehist:1563: Palestino tabela [30, 10, 6, 14, 28, 42] jogos [30, 10, 6, 14, 27, 41] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- corrigido — Everton de Viña del Mar x Unión Española (1993-11-13): Everton 2-1 Unión Española: o ogol erra; Transfermarkt e a tabela da RSSSF concordam (CH-013)

### 1994

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: 240 jogos casados (edição 36404 do ogol, 240 jogos)
- corrigido — Universidad Católica x Universidad de Chile (1994-08-21): Universidad Católica 1-0 Universidad de Chile: o ogol erra; Transfermarkt e a tabela da RSSSF concordam (CH-013)

### 1995

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: 240 jogos casados (edição 36405 do ogol, 240 jogos)
- corrigido — Palestino x Deportes La Serena (1995-06-11): Palestino 2-0 La Serena: o ogol erra; Transfermarkt e a tabela da RSSSF concordam (CH-013)

### 1996

- ogol: 239 jogos casados (edição 37062 do ogol, 240 jogos)
- placar diferente no ogol — Colo Colo x Deportes Temuco (None): RSSSF 4-1, ogol 0-0; fica o da RSSSF

### 1997 Apertura

- sem ocorrências

### 1997 Clausura

- sem ocorrências

### 1998

- ogol: 240 jogos casados (edição 37061 do ogol, 240 jogos)
- data diferente no ogol — Provincial Osorno x Coquimbo Unido: RSSSF 1998-05-05, ogol 1998-05-09; fica a da RSSSF
- data diferente no ogol — Santiago Wanderers x Deportes Iquique: RSSSF 1998-05-05, ogol 1998-05-09; fica a da RSSSF
- data diferente no ogol — Rangers de Talca x Deportes Puerto Montt: RSSSF 1998-05-05, ogol 1998-05-10; fica a da RSSSF
- placar diferente no ogol — Rangers de Talca x Audax Italiano (1998-08-15): RSSSF 0-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Provincial Osorno x Rangers de Talca (1998-08-23): RSSSF 4-1, ogol 4-0; fica o da RSSSF
- data diferente no ogol — Rangers de Talca x Cobreloa: RSSSF 1998-09-18, ogol 1998-09-13; fica a da RSSSF
- data diferente no ogol — Deportes Puerto Montt x Deportes Concepción: RSSSF 1998-09-18, ogol 1998-09-13; fica a da RSSSF
- decidido fora de campo — Deportes Temuco Deportes Concepción (1998-11-28): awarded 0-2; Temuco players on strike

### 1999

- o octogonal final ("Championship Playoff") somou aos clubes um quarto dos pontos e todos os gols da 1ª fase: a tabela publicada mostra esses gols acumulados. Vitórias, empates e derrotas fecham com os jogos
- ogol: 349 jogos casados (edição 36406 do ogol, 352 jogos)
- tabela publicada x jogos — chile99:429: Universidad de Chile tabela [14, 8, 4, 2, 90, 43] jogos [14, 8, 4, 2, 24, 16] — a outra tabela publicada (chile99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile99:429: Universidad Católica tabela [14, 8, 4, 2, 102, 50] jogos [14, 8, 4, 2, 35, 19] — a outra tabela publicada (chile99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile99:429: Cobreloa tabela [14, 8, 2, 4, 94, 49] jogos [14, 8, 2, 4, 32, 20] — a outra tabela publicada (chile99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile99:429: Colo Colo tabela [14, 5, 3, 6, 62, 57] jogos [14, 5, 3, 6, 17, 20] — a outra tabela publicada (chile99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile99:429: Santiago Morning tabela [14, 3, 6, 5, 65, 66] jogos [14, 3, 6, 5, 24, 25] — a outra tabela publicada (chile99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile99:429: Palestino tabela [14, 4, 3, 7, 73, 88] jogos [14, 4, 3, 7, 25, 35] — a outra tabela publicada (chile99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile99:429: Audax Italiano tabela [14, 3, 4, 7, 59, 60] jogos [14, 3, 4, 7, 17, 23] — a outra tabela publicada (chile99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile99:429: Huachipato tabela [14, 2, 4, 8, 62, 79] jogos [14, 2, 4, 8, 16, 32] — a outra tabela publicada (chile99) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — chile99:578: Deportes La Serena tabela [44, 7, 12, 25, 53, 97] jogos [44, 7, 12, 25, 54, 97] — a outra tabela publicada (chile99) fecha com os jogos: o erro é desta tabela
- placar diferente no ogol — Cobreloa x Huachipato (1999-09-01): RSSSF 3-0, ogol 3-1; fica o da RSSSF
- data diferente no ogol — Palestino x Deportes La Serena: RSSSF 1999-09-22, ogol 1999-09-12; fica a da RSSSF
- placar diferente no ogol — Cobresal x Deportes La Serena (1999-11-28): RSSSF 5-3, ogol 5-2; fica o da RSSSF

### 2000

- sem ocorrências

### 2001

- ogol: 240 jogos casados (edição 37060 do ogol, 240 jogos)
- tabela publicada x jogos — chile01:14: O'Higgins tabela [30, 7, 4, 19, 39, 64] jogos [30, 7, 4, 19, 39, 65] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile01:14: Deportes Puerto Montt tabela [30, 4, 9, 17, 31, 66] jogos [30, 4, 9, 17, 31, 65] — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — Deportes Concepción x O'Higgins (2001-05-06): RSSSF 1-0, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Santiago Morning x Audax Italiano (2001-06-09): RSSSF 0-3, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — Audax Italiano x Rangers de Talca (2001-09-09): RSSSF 2-1, ogol 2-0; fica o da RSSSF
- decidido fora de campo — O'Higgins Universidad de Chile (2001-05-26): awarded 0-2, originally 1-5 (?!)

### 2002 Apertura

- abandonado/suspenso, sem valer — Rangers de Talca Colo Colo (2002-06-19): abandoned at 1-0 in 45'

### 2002 Clausura

- sem ocorrências

### 2003 Apertura

- sem ocorrências

### 2003 Clausura

- sem ocorrências

### 2004 Apertura

- linha lida como jogo e descartada (clube não reconhecido): chile04:106 «José Rojas 41; abandoned at x in 87' due to crowd trouble; result stood]»
- abandonado/suspenso, sem valer — Huachipato Cobreloa (2004-06-16): in Concepción

### 2004 Clausura

- tabela publicada x jogos — chile04:787: Colo Colo tabela [17, 9, 5, 3, 28, 18] jogos [17, 9, 5, 3, 29, 19] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 2005 Apertura

- abandonado/suspenso, sem valer — Universidad de Chile Rangers de Talca (2005-05-22): abandoned at 0-1 in 6'

### 2005 Clausura

- ESPN: 205 jogos casados

### 2006 Apertura

- ESPN: 186 jogos casados
- abandonado/suspenso, sem valer — Deportes La Serena Coquimbo Unido (2006-05-28): abandoned at 2-1 in 77'

### 2006 Clausura

- ESPN: 186 jogos casados

### 2007 Apertura

- ESPN: 210 jogos casados

### 2007 Clausura

- ESPN: 225 jogos casados

### 2008 Apertura

- ESPN: 205 jogos casados
- decidido fora de campo — Deportes Concepción Santiago Morning (2008-02-02): awarded 0-3; originally 2-1, Feb 3]                                      deducted

### 2008 Clausura

- ESPN: 185 jogos casados
- não jogado — Deportes Concepción Universidad de Chile (2008-07-16)
- abandonado/suspenso, sem valer — Colo Colo Unión Española (2008-08-15): abandoned at 0-0 in 18'

### 2009 Apertura

- ESPN: 155 jogos casados

### 2009 Clausura

- ESPN: 167 jogos casados
- abandonado/suspenso, sem valer — Everton de Viña del Mar O'Higgins (2009-08-14): abandoned at 0-0 at half-time
- decidido fora de campo — Universidad de Concepción Curicó Unido (2009-10-04): in Yumbel; awarded 3-0;
- decidido fora de campo — Cobreloa Rangers de Talca (2009-11-08): awarded 3-0; originally 1-0;

### 2010

- ogol: 305 jogos casados (edição 12812 do ogol, 306 jogos)
- ESPN: 295 jogos casados
- data diferente no ogol — Universidad de Concepción x Unión Española: RSSSF 2010-04-14, ogol 2010-04-20; fica a da RSSSF
- abandonado/suspenso, sem valer — Deportes La Serena Audax Italiano (2010-03-14): abandoned at 1-2 in 53'

### 2011 Apertura

- ESPN: 167 jogos casados
- corrigido — Ñublense x Santiago Wanderers (2011-01-29): Ñublense 2-0 Wanderers: a decisão do tribunal foi revogada ("award revoked") (CH-015)
- decidido fora de campo — Colo Colo Cobresal (2011-01-30): awarded 0-3, originally 2-2, Colo Rodrigo Jara 45+3og, Esteban Paredes 86;    Colo have 1 point deducted for using

### 2011 Clausura

- a página da RSSSF traz só os mata-matas: a fase de pontos corridos vem da ESPN
- ESPN: 167 jogos casados

### 2012 Apertura

- a página da RSSSF traz só os mata-matas: a fase de pontos corridos vem da ESPN
- ESPN: 167 jogos casados

### 2012 Clausura

- a página da RSSSF traz só os mata-matas: a fase de pontos corridos vem da ESPN
- ESPN: 167 jogos casados
- tabela publicada x jogos — chile2012:99: Unión Española tabela [17, 7, 3, 7, 28, 28] jogos [17, 7, 4, 6, 29, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — chile2012:99: Universidad Católica tabela [17, 6, 5, 6, 24, 23] jogos [17, 5, 6, 6, 22, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 2013 Transición

- torneio de transição para o calendário europeu
- ESPN: 153 jogos casados

### 2013/14 Apertura

- ESPN: 153 jogos casados
- decidido fora de campo — Santiago Wanderers O'Higgins (2013-08-24): awarded 0-3, originally 2-2; Wanderers

### 2013/14 Clausura

- ESPN: 152 jogos casados

### 2014/15 Apertura

- ESPN: 153 jogos casados
- decidido fora de campo — San Marcos de Arica Deportes Iquique (2014-11-22): awarded 1-0

### 2014/15 Clausura

- ESPN: 153 jogos casados

### 2015/16 Apertura

- ESPN: 119 jogos casados
- decidido fora de campo — Santiago Wanderers Unión La Calera (2015-09-26): awarded 3-0, originally 1-0

### 2015/16 Clausura

- ESPN: 120 jogos casados

### 2016/17 Apertura

- ESPN: 120 jogos casados

### 2016/17 Clausura

- ESPN: 120 jogos casados

### 2017 Transición

- torneio de transição de volta ao calendário anual
- ESPN: 120 jogos casados

### 2018

- ogol: 240 jogos casados (edição 121802 do ogol, 240 jogos)
- ESPN: 240 jogos casados

### 2019

- campeonato encerrado na 24ª rodada pelos protestos de outubro de 2019; a ANFP declarou campeão o líder
- ogol: 194 jogos casados (edição 131219 do ogol, 240 jogos)
- ESPN: 194 jogos casados
- abandonado/suspenso, sem valer — Deportes Iquique Colo Colo (2019-11-22): abandoned at 0-0 in 67' due to

### 2020

- temporada esticada até fevereiro de 2021 pela pandemia (a RSSSF chama de 2020/21)
- ogol: 280 jogos casados (edição 141527 do ogol, 307 jogos)
- ESPN: 280 jogos casados
- abandonado/suspenso, sem valer — Curicó Unido Universidad Católica (2020-10-15): abandoned at 2-0 in 50' due to power cut

### 2021

- ogol: 272 jogos casados (edição 154255 do ogol, 272 jogos)
- ESPN: 272 jogos casados

### 2022

- ogol: 240 jogos casados (edição 161941 do ogol, 240 jogos)
- ESPN: 240 jogos casados
- decidido fora de campo — Deportes Antofagasta Palestino (2022-10-15): awarded 0-3; Antofagasta had no stadium

### 2023

- ogol: 239 jogos casados (edição 170869 do ogol, 240 jogos)
- ESPN: 239 jogos casados
- decidido fora de campo — Coquimbo Unido Cobresal (2023-03-13): awarded 0-3, originally 2-1;
- abandonado/suspenso, sem valer — Universidad de Chile Universidad Católica (2023-04-30): abandoned at 0-0 in 31' due to crowd

### 2024

- ogol: 240 jogos casados (edição 182422 do ogol, 240 jogos)
- ESPN: 240 jogos casados
- abandonado/suspenso, sem valer — Unión La Calera Cobresal (2024-11-10): abandoned at 3-0 in 89' due to

### 2025

- a RSSSF só traz a tabela final: os jogos vêm do calendário do ogol
- ogol: 240 jogos casados (edição 194624 do ogol, 240 jogos)
- ESPN: 240 jogos casados

