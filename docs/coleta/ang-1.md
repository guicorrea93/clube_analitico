# Campeonato Angolano (1ª divisão) — coleta de dados

Gerado por `python coleta/ang-1/importar.py`. Pacote em `data/coleta/ang-1/pacote/`.

**Edições:** 48, de 1979 a 2025/26: o Girabola, como a federação o numera (2025/26 é o "XLVIII Girabola") e os clubes contam os títulos. Ano civil até 2018; duas metades de 2018/19 em diante. 2019/20 foi abandonado pela pandemia de Covid-19 e entra sem campeão. Pesquisa de 25/11/2026, aprovada pelo Guilherme.

**Fora do pacote:** o Campeonato Provincial da era colonial (1941 a 1974; 1975 abandonado), que a federação não conta; a Taça e a Supertaça; as divisões de baixo.

**Fontes:** RSSSF (lista de campeões `angochamp.html`; páginas por ano: a tabela de 1981 a 1997, os jogos em 1979, 1980 e de 1998 em diante); ogol (jogos de 1999 em diante: conferência, rodada e data). A Wikipédia ficou para depois (a API recusou o download em 25/11/2026). A ESPN não tem a liga.

**Clubes:** o nome pelo qual o clube é conhecido no Brasil (1º de Agosto, Petro de Luanda, Benfica de Luanda...). Mesmo clube com outro nome na mesma cidade é um só (ASA de Luanda = Atlético Sport Aviação; Atlético do Namibe = Desportivo Sonangol do Namibe). Regras em `coleta/ang-1/clubes_ang.py`.

**Regras:** o placar é o da RSSSF. A classificação é a tabela publicada (ordem oficial e pontos). Pontos 2-1-0 (vitória, empate, derrota) até 1994 e 3-1-0 desde 1995 ("introduction of 3-1-0 point system in 1995", RSSSF).

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Formato |
|---|---|---|---|---|---|---|---|
| 1979 | 24 | 126 (126) | 430 | 14 | 4 / 0 | 1º de Agosto | 4 grupos + fase final + mata-mata |
| 1980 | 14 | 182 (182) | 545 | 0 | 0 / 1 | 1º de Agosto | pontos corridos |
| 1981 | 14 | 0 (0) | 0 | 0 | 0 / 0 | 1º de Agosto | sem jogos (só a tabela final) |
| 1982 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Petro de Luanda | sem jogos (só a tabela final) |
| 1983 | 14 | 0 (0) | 0 | 0 | 0 / 0 | 1º de Maio | sem jogos (só a tabela final) |
| 1984 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Petro de Luanda | sem jogos (só a tabela final) |
| 1985 | 14 | 0 (0) | 0 | 0 | 0 / 0 | 1º de Maio | sem jogos (só a tabela final) |
| 1986 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Petro de Luanda | sem jogos (só a tabela final) |
| 1987 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Petro de Luanda | sem jogos (só a tabela final) |
| 1988 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Petro de Luanda | sem jogos (só a tabela final) |
| 1989 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Petro de Luanda | sem jogos (só a tabela final) |
| 1990 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Petro de Luanda | sem jogos (só a tabela final) |
| 1991 | 16 | 0 (0) | 0 | 0 | 0 / 0 | 1º de Agosto | sem jogos (só a tabela final) |
| 1992 | 16 | 0 (0) | 0 | 0 | 0 / 0 | 1º de Agosto | sem jogos (só a tabela final) |
| 1993 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Petro de Luanda | sem jogos (só a tabela final) |
| 1994 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Petro de Luanda | sem jogos (só a tabela final) |
| 1995 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Petro de Luanda | sem jogos (só a tabela final) |
| 1996 | 13 | 0 (0) | 0 | 0 | 0 / 0 | 1º de Agosto | sem jogos (só a tabela final) |
| 1997 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Petro de Luanda | sem jogos (só a tabela final) |
| 1998 | 16 | 163 (163) | 332 | 1 | 0 / 0 | 1º de Agosto | jogos incompletos (só os resultados que a página traz) |
| 1999 | 15 | 211 (211) | 438 | 2 | 1 / 0 | 1º de Agosto | pontos corridos |
| 2000 | 14 | 182 (182) | 444 | 0 | 0 / 1 | Petro de Luanda | pontos corridos |
| 2001 | 14 | 182 (182) | 410 | 128 | 1 / 0 | Petro de Luanda | pontos corridos |
| 2002 | 14 | 182 (182) | 374 | 0 | 1 / 0 | ASA de Luanda | pontos corridos |
| 2003 | 14 | 182 (182) | 369 | 0 | 1 / 0 | ASA de Luanda | pontos corridos |
| 2004 | 14 | 182 (182) | 396 | 0 | 1 / 0 | ASA de Luanda | pontos corridos |
| 2005 | 14 | 182 (182) | 355 | 283 | 1 / 0 | Sagrada Esperança | pontos corridos |
| 2006 | 14 | 182 (182) | 340 | 0 | 1 / 0 | 1º de Agosto | pontos corridos |
| 2007 | 14 | 183 (183) | 372 | 0 | 1 / 1 | Interclube | pontos corridos |
| 2008 | 14 | 182 (182) | 368 | 0 | 1 / 0 | Petro de Luanda | pontos corridos |
| 2009 | 14 | 182 (182) | 455 | 0 | 1 / 0 | Petro de Luanda | pontos corridos |
| 2010 | 16 | 241 (241) | 544 | 0 | 1 / 0 | Interclube | pontos corridos |
| 2011 | 16 | 240 (240) | 533 | 12 | 1 / 0 | Recreativo do Libolo | pontos corridos |
| 2012 | 16 | 240 (240) | 549 | 0 | 1 / 0 | Recreativo do Libolo | pontos corridos |
| 2013 | 16 | 240 (240) | 533 | 0 | 1 / 0 | Kabuscorp | pontos corridos |
| 2014 | 16 | 240 (240) | 509 | 0 | 1 / 0 | Recreativo do Libolo | pontos corridos |
| 2015 | 16 | 240 (240) | 513 | 0 | 1 / 0 | Recreativo do Libolo | pontos corridos |
| 2016 | 16 | 242 (242) | 473 | 0 | 1 / 0 | 1º de Agosto | pontos corridos |
| 2017 | 16 | 240 (240) | 517 | 0 | 1 / 0 | 1º de Agosto | pontos corridos |
| 2018 | 16 | 222 (222) | 392 | 0 | 1 / 0 | 1º de Agosto | pontos corridos |
| 2018/19 | 16 | 244 (244) | 503 | 0 | 1 / 0 | 1º de Agosto | pontos corridos |
| 2019/20 | 16 | 188 (188) | 338 | 0 | 1 / 0 | — | temporada não terminada |
| 2020/21 | 16 | 240 (240) | 507 | 0 | 1 / 0 | Sagrada Esperança | pontos corridos |
| 2021/22 | 16 | 241 (241) | 562 | 0 | 1 / 0 | Petro de Luanda | pontos corridos |
| 2022/23 | 16 | 226 (226) | 458 | 0 | 1 / 0 | Petro de Luanda | pontos corridos |
| 2023/24 | 15 | 215 (215) | 443 | 0 | 1 / 0 | Petro de Luanda | pontos corridos |
| 2024/25 | 16 | 243 (243) | 466 | 0 | 1 / 0 | Petro de Luanda | pontos corridos |
| 2025/26 | 16 | 243 (243) | 516 | 0 | 1 / 0 | Petro de Luanda | pontos corridos |

## Conferência e correções, edição a edição

### 1979

- não jogado — FC Cabinda Construção e Habitação (1979-02-03): cancelled

### 1980

- tabela publicada x jogos — ango80:51: Nacional de Benguela tabela [26, 15, 7, 4, 49, 24] jogos [26, 16, 6, 4, 49, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — ango80:51: Desportivo da Chela tabela [26, 7, 9, 10, 35, 48] jogos [26, 7, 8, 11, 34, 48] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- provável jogo da diferença: Nacional de Benguela 2-1 Desportivo da Chela (None, ango80:82); com 2-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1981

- a RSSSF só traz a tabela final

### 1982

- a RSSSF só traz a tabela final

### 1983

- a RSSSF só traz a tabela final

### 1984

- a RSSSF só traz a tabela final

### 1985

- a RSSSF só traz a tabela final

### 1986

- a RSSSF só traz a tabela final

### 1987

- a RSSSF só traz a tabela final

### 1988

- a RSSSF só traz a tabela final

### 1989

- a RSSSF só traz a tabela final

### 1990

- a RSSSF só traz a tabela final

### 1991

- a RSSSF só traz a tabela final

### 1992

- a RSSSF só traz a tabela final

### 1993

- a RSSSF só traz a tabela final

### 1994

- a RSSSF só traz a tabela final

### 1995

- a RSSSF só traz a tabela final

### 1996

- a RSSSF só traz a tabela final

### 1997

- a RSSSF só traz a tabela final

### 1998

- jogos incompletos (só os resultados que a página traz)
- jogos do Kabuscorp anulados: o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- tabela ango98:122 fora da conferência: tabela do meio da temporada (a final vem depois)
- tabela ango98:196 fora da conferência: tabela do meio da temporada (a final vem depois)
- tabela ango98:266 fora da conferência: tabela do meio da temporada (a final vem depois)
- tabela ango98:388 fora da conferência: tabela do meio da temporada (a final vem depois)
- tabela ango98:392 fora da conferência: tabela do meio da temporada (a final vem depois)
- tabela ango98:395 fora da conferência: tabela do meio da temporada (a final vem depois)
- tabela ango98:399 fora da conferência: tabela do meio da temporada (a final vem depois)
- tabela ango98:403 fora da conferência: tabela do meio da temporada (a final vem depois)
- anulado — Kabuscorp 3-2 Chicoil (1998-04-05): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — ASA de Luanda 2-0 Kabuscorp (1998-04-12): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Kabuscorp 2-1 Progresso do Sambizanga (1998-04-19): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Petro de Luanda 2-0 Kabuscorp (1998-04-26): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Kabuscorp 1-5 1º de Agosto (1998-05-03): also reported 1-6; anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Sagrada Esperança 5-0 Kabuscorp (1998-05-10): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Kabuscorp 3-1 Bravos do Maqui (1998-05-17): also reported 3-0; anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Petro do Huambo 2-1 Kabuscorp (1998-05-24): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Kabuscorp 1-0 Sécil Marítima (1998-05-31): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — FC Cabinda 3-2 Kabuscorp (1998-06-07): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Kabuscorp 3-1 Sporting de Cabinda (1998-06-14): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Atlético do Namibe 2-1 Kabuscorp (1998-06-21): also reported 3-1; anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Kabuscorp 6-4 Independente do Tômbwa (1998-06-28): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Rangol 1-0 Kabuscorp (1998-07-05): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Académica do Lobito 0-1 Kabuscorp (1998-07-12): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Kabuscorp 1-0 ASA de Luanda (1998-08-02): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — 1º de Agosto 4-1 Kabuscorp (1998-09-02): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Kabuscorp 3-1 Sagrada Esperança (1998-09-06): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Kabuscorp 1-1 Petro do Huambo (1998-09-20): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Sécil Marítima 1-1 Kabuscorp (1998-09-27): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Sporting de Cabinda 3-2 Kabuscorp (1998-10-18): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)
- anulado — Kabuscorp 1-1 Atlético do Namibe (1998-10-25): anulled; o Kabuscorp foi desclassificado; os jogos dele foram anulados ("anulled" na página)

### 1999

- ogol: 202 jogos casados (edição 142697 do ogol, 210 jogos)
- corrigido — Sporting de Cabinda x Sagrada Esperança (1999-07-25): a linha repete o Sporting de Cabinda 2-1 Sagrada Esperança da linha 232 (colada na continuação da nota do jogo de cima)
- data diferente no ogol — 1º de Agosto x Rangol: RSSSF 1999-08-25, ogol 1999-08-19; fica a da RSSSF
- data diferente no ogol — Interclube x Petro de Luanda: RSSSF 1999-08-26, ogol 1999-08-19; fica a da RSSSF
- data diferente no ogol — Petro do Huambo x Académica do Lobito: RSSSF 1999-09-26, ogol 1999-09-19; fica a da RSSSF
- data diferente no ogol — Independente do Tômbwa x Cambondo: RSSSF 1999-09-26, ogol 1999-09-19; fica a da RSSSF
- data diferente no ogol — Progresso do Sambizanga x Petro do Huambo: RSSSF 1999-10-06, ogol 1999-10-02; fica a da RSSSF
- data diferente no ogol — ASA de Luanda x Sporting de Cabinda: RSSSF 1999-10-06, ogol 1999-10-02; fica a da RSSSF
- data diferente no ogol — 1º de Agosto x Bravos do Maqui: RSSSF 1999-10-06, ogol 1999-10-02; fica a da RSSSF
- data diferente no ogol — Rangol x Petro de Luanda: RSSSF 1999-10-07, ogol 1999-10-02; fica a da RSSSF
- data diferente no ogol — 1º de Agosto x Sporting de Cabinda: RSSSF 1999-10-21, ogol 1999-10-16; fica a da RSSSF
- data diferente no ogol — 1º de Agosto x Atlético do Namibe: RSSSF 1999-11-03, ogol 1999-10-29; fica a da RSSSF
- data diferente no ogol — Independente do Tômbwa x Petro de Luanda: RSSSF 1999-11-03, ogol 1999-10-29; fica a da RSSSF
- decidido fora de campo — Petro do Huambo Independente do Tômbwa (1999-07-25): awarded 3-0, Independente dns
- abandonado/suspenso, sem valer — Sagrada Esperança Bravos do Maqui (1999-10-31): abandoned at 0-1 in 80' due to bad weather

### 2000

- ogol: 169 jogos casados (edição 142695 do ogol, 169 jogos)
- tabela publicada x jogos — ango00:14: Sagrada Esperança tabela [26, 9, 6, 11, 21, 30] jogos [26, 9, 7, 10, 21, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — ango00:14: Sporting do Bié tabela [26, 5, 3, 18, 20, 50] jogos [26, 5, 4, 17, 20, 50] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- decidido fora de campo — Sporting do Bié Sagrada Esperança (2000-05-28): awarded 0-0 loss against both
- decidido fora de campo — Petro do Huambo ARA da Gabela (2000-08-27): Sep 13; awarded 3-0, ARA dns

### 2001

- ogol: 147 jogos casados (edição 142397 do ogol, 182 jogos)
- data diferente no ogol — Interclube x Sagrada Esperança: RSSSF 2001-03-24, ogol 2001-03-17; fica a da RSSSF
- data diferente no ogol — Petro de Luanda x Benfica do Lubango: RSSSF 2001-04-04, ogol 2001-03-31; fica a da RSSSF
- data diferente no ogol — 1º de Maio x Interclube: RSSSF 2001-04-18, ogol 2001-04-14; fica a da RSSSF
- data diferente no ogol — Benfica de Luanda x ASA de Luanda: RSSSF 2001-04-21, ogol 2001-04-14; fica a da RSSSF
- data diferente no ogol — Bravos do Maqui x Sagrada Esperança: RSSSF 2001-06-16, ogol 2001-06-09; fica a da RSSSF
- data diferente no ogol — Progresso do Sambizanga x Interclube: RSSSF 2001-06-16, ogol 2001-06-09; fica a da RSSSF
- data diferente no ogol — Sagrada Esperança x 1º de Maio: RSSSF 2001-07-29, ogol 2001-07-21; fica a da RSSSF
- data diferente no ogol — 1º de Maio x ASA de Luanda: RSSSF 2001-09-19, ogol 2001-09-15; fica a da RSSSF
- data diferente no ogol — Petro de Luanda x 1º de Agosto: RSSSF 2001-09-19, ogol 2001-09-15; fica a da RSSSF
- data diferente no ogol — Sagrada Esperança x 1º de Agosto: RSSSF 2001-10-03, ogol 2001-09-29; fica a da RSSSF
- data diferente no ogol — ASA de Luanda x FC Cabinda: RSSSF 2001-10-03, ogol 2001-09-29; fica a da RSSSF
- data diferente no ogol — Interclube x Progresso do Sambizanga: RSSSF 2001-10-17, ogol 2001-10-13; fica a da RSSSF
- data diferente no ogol — Petro de Luanda x Benfica de Luanda: RSSSF 2001-10-24, ogol 2001-10-20; fica a da RSSSF
- data diferente no ogol — Interclube x 1º de Agosto: RSSSF 2001-11-06, ogol 2001-10-27; fica a da RSSSF
- decidido fora de campo — Petro do Huambo Sagrada Esperança (2001-04-08): awarded 3-0; Sag. Esperança dns
- decidido fora de campo — Bravos do Maqui FC Cabinda (2001-05-27): awarded 3-0, FC Cabinda dns
- decidido fora de campo — ASA de Luanda Petro do Huambo (2001-07-10): awarded 3-0, ASA dns on May 22;
- decidido fora de campo — Petro de Luanda Atlético do Namibe (2001-06-21): awarded 3-0, Sonangol dns due to
- decidido fora de campo — Petro do Huambo Bravos do Maqui (2001-08-11): awarded 3-0, Onze Bravos dns
- decidido fora de campo — 1º de Agosto 1º de Maio (2001-10-19): awarded 3-0, Primeiro de Maio dns

### 2002

- ogol: 168 jogos casados (edição 142396 do ogol, 182 jogos)
- data diferente no ogol — Académica do Lobito x Petro do Huambo: RSSSF 2002-03-09, ogol 2002-03-05; fica a da RSSSF
- data diferente no ogol — Benfica de Luanda x Sporting de Cabinda: RSSSF 2002-03-09, ogol 2002-03-05; fica a da RSSSF
- data diferente no ogol — 1º de Agosto x Benfica do Lubango: RSSSF 2002-03-11, ogol 2002-03-05; fica a da RSSSF
- data diferente no ogol — Petro de Luanda x ASA de Luanda: RSSSF 2002-03-19, ogol 2002-03-23; fica a da RSSSF
- data diferente no ogol — Sporting de Cabinda x Benfica do Lubango: RSSSF 2002-06-23, ogol 2002-06-19; fica a da RSSSF
- data diferente no ogol — ASA de Luanda x Atlético do Namibe: RSSSF 2002-08-13, ogol 2002-08-09; fica a da RSSSF

### 2003

- ogol: 182 jogos casados (edição 31826 do ogol, 182 jogos)
- decidido fora de campo — Ritondo Sagrada Esperança (2003-09-21): awarded 0-3; Ritondo dns

### 2004

- ogol: 181 jogos casados (edição 558 do ogol, 182 jogos)
- decidido fora de campo — Sporting de Cabinda Bravos do Maqui (2004-08-15): awarded 3-0; Bravos Maquis dns
- decidido fora de campo — Bravos do Maqui Petro de Luanda (2004-09-22): awarded 0-3; Bravos Maquis dns

### 2005

- ogol: 180 jogos casados (edição 872 do ogol, 182 jogos)
- data diferente no ogol — 1º de Maio x Sporting do Bié: RSSSF 2005-08-07, ogol 2005-08-03; fica a da RSSSF
- decidido fora de campo — Sagrada Esperança Atlético do Namibe (2005-04-10): awarded 3-0; Sonangol dns
- decidido fora de campo — 1º de Agosto Sagrada Esperança (2005-06-25): awarded 3-0; originally 1-1, Sagrada
- decidido fora de campo — 1º de Agosto Sporting do Bié (2005-07-23): awarded 3-0; Sporting Bié dns

### 2006

- ogol: 181 jogos casados (edição 1246 do ogol, 182 jogos)
- data diferente no ogol — Académica do Soyo x Petro de Luanda: RSSSF 2006-05-21, ogol 2006-05-14; fica a da RSSSF
- data diferente no ogol — Interclube x Sporting de Cabinda: RSSSF 2006-07-23, ogol 2006-07-16; fica a da RSSSF
- data diferente no ogol — Interclube x Petro de Luanda: RSSSF 2006-08-09, ogol 2006-08-13; fica a da RSSSF
- data diferente no ogol — Atlético do Namibe x Interclube: RSSSF 2006-10-25, ogol 2006-10-18; fica a da RSSSF
- decidido fora de campo — Benfica do Lubango Sporting de Cabinda (2006-10-15): awarded 3-0; Sporting Cabinda dns

### 2007

- ogol: 182 jogos casados (edição 1441 do ogol, 182 jogos)
- tabela publicada x jogos — ango07:35: Sagrada Esperança tabela [26, 10, 10, 6, 37, 27] jogos [26, 10, 10, 6, 36, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — ango07:35: Desportivo da Huíla tabela [26, 10, 8, 8, 26, 25] jogos [26, 10, 8, 8, 25, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- provável jogo da diferença: Sagrada Esperança 1-3 Desportivo da Huíla (2007-05-13, ango07:173); com 2-4 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Desportivo da Huíla 1-1 Sagrada Esperança (2007-09-30, ango07:327); com 2-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- data diferente no ogol — Santos de Luanda x Petro de Luanda: RSSSF 2007-03-14, ogol 2007-03-18; fica a da RSSSF
- data diferente no ogol — Desportivo da Huíla x Interclube: RSSSF 2007-03-14, ogol 2007-03-18; fica a da RSSSF
- não jogado — ASA de Luanda 1º de Agosto (2007-07-14): not played due to light Jul 15]                                       failure; award of 0-3

### 2008

- ogol: 181 jogos casados (edição 1867 do ogol, 182 jogos)
- data diferente no ogol — Petro do Huambo x Kabuscorp: RSSSF 2008-05-11, ogol 2008-05-17; fica a da RSSSF
- data diferente no ogol — 1º de Maio x Benfica do Lubango: RSSSF 2008-05-11, ogol 2008-05-17; fica a da RSSSF
- data diferente no ogol — Sagrada Esperança x Benfica de Luanda: RSSSF 2008-05-12, ogol 2008-05-17; fica a da RSSSF
- data diferente no ogol — Recreativo do Libolo x Petro do Huambo: RSSSF 2008-09-13, ogol 2008-09-09; fica a da RSSSF
- data diferente no ogol — Interclube x Recreativo do Libolo: RSSSF 2008-10-14, ogol 2008-10-19; fica a da RSSSF
- placar diferente no ogol — Petro do Huambo x Benfica do Lubango (2008-10-26): RSSSF 1-1, ogol 0-1; fica o da RSSSF

### 2009

- ogol: 180 jogos casados (edição 5704 do ogol, 182 jogos)
- data diferente no ogol — Desportivo da Huíla x Santos de Luanda: RSSSF 2009-05-21, ogol 2009-05-13; fica a da RSSSF
- data diferente no ogol — Benfica de Luanda x Desportivo da Huíla: RSSSF 2009-05-26, ogol 2009-05-22; fica a da RSSSF

### 2010

- ogol: 240 jogos casados (edição 13622 do ogol, 240 jogos)
- placar diferente no ogol — Interclube x ASA de Luanda (2010-04-17): RSSSF 5-1, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Recreativo do Libolo x Sagrada Esperança (2010-08-17): RSSSF 1-2, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Sagrada Esperança x Petro de Luanda (2010-08-21): RSSSF 1-3, ogol 0-3; fica o da RSSSF
- data diferente no ogol — Bravos do Maqui x 1º de Agosto: RSSSF 2010-08-28, ogol 2010-09-04; fica a da RSSSF
- data diferente no ogol — Petro de Luanda x Recreativo do Libolo: RSSSF 2010-08-28, ogol 2010-09-04; fica a da RSSSF
- data diferente no ogol — Desportivo da Huíla x Académica do Soyo: RSSSF 2010-08-28, ogol 2010-09-04; fica a da RSSSF
- data diferente no ogol — Recreativo da Caála x ASA de Luanda: RSSSF 2010-08-29, ogol 2010-09-04; fica a da RSSSF
- data diferente no ogol — FC Cabinda x Benfica do Lubango: RSSSF 2010-08-29, ogol 2010-09-04; fica a da RSSSF
- data diferente no ogol — Interclube x Sporting de Cabinda: RSSSF 2010-08-28, ogol 2010-09-04; fica a da RSSSF
- data diferente no ogol — Académica do Soyo x Interclube: RSSSF 2010-09-11, ogol 2010-09-15; fica a da RSSSF
- placar diferente no ogol — FC Cabinda x Bravos do Maqui (2010-10-17): RSSSF 3-0, ogol 0-3; fica o da RSSSF
- abandonado/suspenso, sem valer — FC Cabinda Sagrada Esperança (2010-05-02): abandoned at 0-0 in 9'
- decidido fora de campo — Académica do Soyo Interclube (2010-09-11): awarded 0-3, Académica dns

### 2011

- ogol: 237 jogos casados (edição 20746 do ogol, 240 jogos)
- data diferente no ogol — 1º de Agosto x Petro de Luanda: RSSSF 2011-05-11, ogol 2011-05-07; fica a da RSSSF
- decidido fora de campo — Académica do Lobito Académica do Soyo (2011-05-29): awarded 0-3; originally 1-0; Acad.
- decidido fora de campo — Recreativo do Libolo Académica do Lobito (2011-06-11): awarded 3-0; originally 2-0; Acad.
- decidido fora de campo — Académica do Lobito Petro de Luanda (2011-06-19): awarded 0-3; originally 1-3; Acad.

### 2012

- ogol: 240 jogos casados (edição 42140 do ogol, 240 jogos)
- placar diferente no ogol — Kabuscorp x Interclube (2012-10-28): RSSSF 0-2, ogol 0-0; fica o da RSSSF
- decidido fora de campo — Atlético do Namibe Sporting de Cabinda (2012-03-31): awarded 3-0; Sporting Cabinda dns
- decidido fora de campo — ASA de Luanda Atlético do Namibe (2012-08-18): awarded 0-3; ASA dns

### 2013

- ogol: 239 jogos casados (edição 55250 do ogol, 240 jogos)
- data diferente no ogol — Sagrada Esperança x Atlético do Namibe: RSSSF 2013-09-11, ogol 2013-09-07; fica a da RSSSF
- decidido fora de campo — Recreativo da Caála Atlético do Namibe (2013-06-02): awarded 3-0, Atlético Namibe dns
- decidido fora de campo — Sagrada Esperança Atlético do Namibe (2013-09-11): awarded 3-0, Atlético Namibe dns

### 2014

- ogol: 238 jogos casados (edição 67132 do ogol, 240 jogos)
- decidido fora de campo — Sporting de Cabinda União do Uíge (2014-05-24): awarded 3-0; originally 1-1
- decidido fora de campo — Sagrada Esperança Benfica do Lubango (2014-06-14): awarded 3-0, Benfica dns
- decidido fora de campo — União do Uíge Petro de Luanda (2014-07-30): awarded 0-3; originally 2-0,
- decidido fora de campo — Progresso do Sambizanga União do Uíge (2014-08-24): awarded 3-0; originally 1-1,
- decidido fora de campo — União do Uíge Recreativo da Caála (2014-08-28): awarded 0-3; originally 0-0,

### 2015

- ogol: 238 jogos casados (edição 78102 do ogol, 240 jogos)
- placar diferente no ogol — ASA de Luanda x Benfica de Luanda (2015-08-22): RSSSF 1-1, ogol 0-0; fica o da RSSSF
- data diferente no ogol — ASA de Luanda x 1º de Agosto: RSSSF 2015-09-26, ogol 2015-10-04; fica a da RSSSF
- data diferente no ogol — Interclube x Kabuscorp: RSSSF 2015-09-26, ogol 2015-10-04; fica a da RSSSF
- data diferente no ogol — Benfica de Luanda x Recreativo do Libolo: RSSSF 2015-09-27, ogol 2015-10-04; fica a da RSSSF
- data diferente no ogol — Bravos do Maqui x Recreativo da Caála: RSSSF 2015-09-26, ogol 2015-10-04; fica a da RSSSF
- data diferente no ogol — Petro de Luanda x Desportivo da Huíla: RSSSF 2015-09-26, ogol 2015-10-04; fica a da RSSSF
- data diferente no ogol — Sagrada Esperança x Progresso do Sambizanga: RSSSF 2015-09-26, ogol 2015-10-04; fica a da RSSSF
- data diferente no ogol — Sporting de Cabinda x Domant: RSSSF 2015-09-27, ogol 2015-10-04; fica a da RSSSF
- data diferente no ogol — Académica do Lobito x Benfica de Luanda: RSSSF 2015-09-30, ogol 2015-10-07; fica a da RSSSF
- data diferente no ogol — Desportivo da Huíla x Interclube: RSSSF 2015-09-30, ogol 2015-10-07; fica a da RSSSF
- data diferente no ogol — Domant x Petro de Luanda: RSSSF 2015-09-30, ogol 2015-10-07; fica a da RSSSF
- data diferente no ogol — Kabuscorp x ASA de Luanda: RSSSF 2015-09-30, ogol 2015-10-07; fica a da RSSSF
- data diferente no ogol — Progresso do Sambizanga x Sporting de Cabinda: RSSSF 2015-09-30, ogol 2015-10-07; fica a da RSSSF
- data diferente no ogol — Sagrada Esperança x Bravos do Maqui: RSSSF 2015-09-30, ogol 2015-10-07; fica a da RSSSF
- decidido fora de campo — Progresso da Lunda Sul Sporting de Cabinda (2015-03-07): awarded 3-0, Sporting Cabinda dns

### 2016

- ogol: 238 jogos casados (edição 95280 do ogol, 240 jogos)
- data diferente no ogol — Progresso da Lunda Sul x 4 de Abril: RSSSF 2016-04-02, ogol 2016-03-25; fica a da RSSSF
- abandonado/suspenso, sem valer — 4 de Abril Progresso do Sambizanga (2016-03-12): abandoned at 0-1 in 55'
- não jogado — 1º de Maio ASA de Luanda (2016-04-17): ASA dns
- decidido fora de campo — Sagrada Esperança Desportivo da Huíla (2016-07-09): awarded 3-0, Huíla dns

### 2017

- ogol: 240 jogos casados (edição 103877 do ogol, 240 jogos)
- decidido fora de campo — Progresso da Lunda Sul Progresso do Sambizanga (2017-08-29): awarded 0-3; Lunda Sul dns
- decidido fora de campo — Recreativo da Caála Interclube (2017-10-01): awarded 0-3; Caála dns for financial

### 2018

- ogol: 222 jogos casados (edição 122017 do ogol, 240 jogos)
- jogos do JGM anulados: o JGM/Académica do Huambo desistiu por razões financeiras; os resultados foram anulados
- tabela ango2018:64 fora da conferência: linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- tabela ango2018:318 fora da conferência: linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- tabela ango2018:547 fora da conferência: linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- anulado — JGM 1-1 Bravos do Maqui (2018-02-10): annulled; o JGM/Académica do Huambo desistiu por razões financeiras; os resultados foram anulados
- anulado — Académica do Lobito 3-2 JGM (2018-02-17): annulled; o JGM/Académica do Huambo desistiu por razões financeiras; os resultados foram anulados
- anulado — JGM 1-2 Kabuscorp (2018-02-24): annulled; o JGM/Académica do Huambo desistiu por razões financeiras; os resultados foram anulados
- anulado — Sporting de Cabinda 1-0 JGM (2018-03-03): annulled; o JGM/Académica do Huambo desistiu por razões financeiras; os resultados foram anulados
- anulado — Recreativo da Caála 2-1 JGM (2018-03-11): annulled; o JGM/Académica do Huambo desistiu por razões financeiras; os resultados foram anulados
- anulado — JGM 1-1 Recreativo do Libolo (2018-03-14): annulled; o JGM/Académica do Huambo desistiu por razões financeiras; os resultados foram anulados
- anulado — 1º de Agosto JGM (2018-05-09): o JGM/Académica do Huambo desistiu por razões financeiras; os resultados foram anulados
- anulado — JGM 0-1 Petro de Luanda (2018-03-30): annulled; o JGM/Académica do Huambo desistiu por razões financeiras; os resultados foram anulados
- anulado — Domant 4-0 JGM (2018-04-08): annulled; o JGM/Académica do Huambo desistiu por razões financeiras; os resultados foram anulados
- anulado — JGM 1-1 Desportivo da Huíla (2018-04-14): annulled; o JGM/Académica do Huambo desistiu por razões financeiras; os resultados foram anulados
- anulado — Interclube 5-0 JGM (2018-04-21): annulled; o JGM/Académica do Huambo desistiu por razões financeiras; os resultados foram anulados
- anulado — JGM Sagrada Esperança (2018-04-25): awarded 0-3; JGM dns; annulled; o JGM/Académica do Huambo desistiu por razões financeiras; os resultados foram anulados
- decidido fora de campo — Cuando Cubango Sporting de Cabinda (2018-08-01): awarded 3-0; Sporting Cabinda dns

### 2018/19

- ogol: 240 jogos casados (edição 127945 do ogol, 240 jogos)
- decidido fora de campo — Santa Rita de Cássia Recreativo da Caála (2018-11-17): awarded 3-0, Recreativo da Caála dns
- não jogado — Recreativo da Caála Saurimo (2018-12-13): Saurimo dns
- decidido fora de campo — Recreativo da Caála Saurimo (2018-12-26): awarded 3-0, Saurimo dns
- não jogado — Sporting de Cabinda Recreativo da Caála (2018-12-19): Recreativo da Cáala dns
- decidido fora de campo — Recreativo do Libolo Académica do Lobito (2019-01-20): awarded 3-0, Académica dns
- decidido fora de campo — Sagrada Esperança ASA de Luanda (2019-02-27): awarded 3-0, ASA dns
- não jogado — Interclube Saurimo (2019-04-20): Saurimo dns due to breakdown bus
- não jogado — Interclube Saurimo (2019-04-21): Interclube dns

### 2019/20

- abandonado em 14/05/2020 (pandemia de Covid-19), sem campeão
- ogol: 187 jogos casados (edição 135058 do ogol, 240 jogos)
- jogos do 1º de Maio anulados: o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados
- tabela ango2020:69 fora da conferência: linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- tabela ango2020:319 fora da conferência: linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- tabela ango2020:476 fora da conferência: linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- anulado — 1º de Maio Académica do Lobito (2019-08-18): awarded 0-3, Primeiro de Maio dns; annulled; o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados
- decidido fora de campo — Santa Rita de Cássia Recreativo da Caála (2019-08-18): awarded 0-3, Santa Rita dns
- anulado — Recreativo da Caála 1-0 1º de Maio (2019-08-25): annulled; o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados
- anulado — 1º de Maio 0-0 Sporting de Cabinda (2019-08-31): annulled; o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados
- anulado — Cuando Cubango 3-1 1º de Maio (2019-09-18): annulled; o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados
- anulado — 1º de Maio 0-1 Wiliete (2019-09-21): annulled; o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados
- anulado — Interclube 3-1 1º de Maio (2019-09-28): annulled; o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados
- anulado — 1º de Maio 1-1 Progresso do Sambizanga (2019-10-05): annulled; o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados
- anulado — Bravos do Maqui 3-1 1º de Maio (2019-10-12): annulled; o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados
- não jogado — Progresso do Sambizanga Desportivo da Huíla (2019-10-12): no ambulance
- anulado — 1º de Maio 0-0 Desportivo da Huíla (2019-10-23): annulled; o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados
- anulado — 1º de Agosto 3-1 1º de Maio (2019-10-27): annulled; o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados
- anulado — 1º de Maio 1-0 Sagrada Esperança (2019-11-02): annulled; o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados
- anulado — Petro de Luanda 2-0 1º de Maio (2019-11-23): annulled; o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados
- anulado — 1º de Maio 1-1 Ferrovia do Huambo (2019-11-30): annulled; o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados
- anulado — Recreativo do Libolo 0-0 1º de Maio (2019-12-07): annulled; o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados
- anulado — Santa Rita de Cássia 1º de Maio (2019-12-22): awarded 3-0, Primeiro de Maio dns; annulled; o 1º de Maio de Benguela foi excluído; todos os seus resultados foram anulados
- não jogado — Sagrada Esperança Desportivo da Huíla (2020-03-22): Desportivo da Huíla dns
- não jogado — Recreativo da Caála Sporting de Cabinda (2020-03-22): Sporting Cabinda dns

### 2020/21

- ogol: 234 jogos casados (edição 149664 do ogol, 240 jogos)
- data diferente no ogol — Académica do Lobito x Sporting de Cabinda: RSSSF 2021-02-20, ogol 2021-02-24; fica a da RSSSF
- decidido fora de campo — Cuando Cubango Ferrovia do Huambo (2020-12-27): awarded 3-0; originally 1-1,
- decidido fora de campo — Desportivo da Huíla Ferrovia do Huambo (2021-01-03): awarded 3-0; originally 2-2,
- decidido fora de campo — Ferrovia do Huambo Sagrada Esperança (2021-01-10): awarded 0-3; originally 1-0,
- decidido fora de campo — Bravos do Maqui Ferrovia do Huambo (2021-01-16): awarded 3-0; originally 0-0,
- decidido fora de campo — Ferrovia do Huambo Recreativo do Libolo (2021-01-20): awarded 0-3; originally 1-0,
- decidido fora de campo — Baixa de Cassanje Ferrovia do Huambo (2021-01-23): awarded 3-0; originally 2-1,
- decidido fora de campo — Bravos do Maqui Desportivo da Huíla (2021-03-20): awarded 3-0, Huíla dns
- decidido fora de campo — Ferrovia do Huambo Santa Rita de Cássia (2021-01-31): awarded 0-3; originally 1-0,
- decidido fora de campo — Ferrovia do Huambo Wiliete (2021-02-07): awarded 0-3; originally 2-0,
- decidido fora de campo — Recreativo da Caála Ferrovia do Huambo (2021-02-14): awarded 3-0; originally 2-0,
- decidido fora de campo — Santa Rita de Cássia Bravos do Maqui (2021-02-17): awarded 0-3; not played due to positive
- decidido fora de campo — Ferrovia do Huambo Progresso do Sambizanga (2021-02-17): awarded 0-3; originally 0-0,
- decidido fora de campo — Académica do Lobito Sporting de Cabinda (2021-02-20): awarded 3-0; Sporting Cabinda dns
- decidido fora de campo — Ferrovia do Huambo Académica do Lobito (2021-02-28): awarded 0-3; originally 1-0,
- decidido fora de campo — Ferrovia do Huambo 1º de Agosto (2021-03-14): awarded 0-3; originally 1-2,
- decidido fora de campo — Ferrovia do Huambo Cuando Cubango (2021-04-25): awarded 0-3; originally 2-1,
- decidido fora de campo — Ferrovia do Huambo Desportivo da Huíla (2021-05-01): awarded 0-3; originally 2-3,
- decidido fora de campo — Sagrada Esperança Ferrovia do Huambo (2021-05-08): awarded 3-0; originally 1-0,
- decidido fora de campo — Ferrovia do Huambo Bravos do Maqui (2021-05-12): awarded 0-3; originally 2-0,
- decidido fora de campo — Recreativo do Libolo Ferrovia do Huambo (2021-05-15): awarded 3-0; originally 1-0,
- decidido fora de campo — Ferrovia do Huambo Baixa de Cassanje (2021-05-23): awarded 0-3; originally 1-0,
- decidido fora de campo — Cuando Cubango Recreativo do Libolo (2021-07-06): awarded 3-0, Rec. Libolo refused to play after
- decidido fora de campo — Santa Rita de Cássia Ferrovia do Huambo (2021-05-30): awarded 3-0; originally 1-0,
- decidido fora de campo — Ferrovia do Huambo Interclube (2021-06-06): awarded 0-3; originally 0-2,
- decidido fora de campo — Wiliete Ferrovia do Huambo (2021-06-13): awarded 3-0; originally 0-0,
- decidido fora de campo — Ferrovia do Huambo Recreativo da Caála (2021-06-20): awarded 0-3; originally 1-2,
- decidido fora de campo — Sporting de Cabinda Progresso do Sambizanga (2021-06-20): awarded 3-0, Progresso dns
- decidido fora de campo — Progresso do Sambizanga Ferrovia do Huambo (2021-06-26): awarded 3-0; originally 2-2,
- decidido fora de campo — Ferrovia do Huambo Petro de Luanda (2021-06-30): awarded 0-3; originally 0-2,

### 2021/22

- ogol: 240 jogos casados (edição 158412 do ogol, 240 jogos)
- placar diferente no ogol — Académica do Lobito x Bravos do Maqui (2022-02-19): RSSSF 3-2, ogol 3-1; fica o da RSSSF
- decidido fora de campo — Desportivo da Huíla Progresso do Sambizanga (2021-10-03): awarded 3-0; abandoned at 0-0 in 9';
- não jogado — Sporting de Cabinda Recreativo do Libolo (2021-11-06): award of 3-0 revoked
- decidido fora de campo — Académica do Lobito Sporting de Cabinda (2021-11-20): awarded 3-0, Sporting de Cabinda dns
- decidido fora de campo — Sporting de Cabinda Sporting de Benguela (2021-12-09): awarded 3-0, Sporting Benguela dns
- decidido fora de campo — Recreativo da Caála Progresso do Sambizanga (2021-12-15): awarded 3-0; Progresso Covid-19 tests expired
- decidido fora de campo — Petro de Luanda Cuando Cubango (2022-01-22): awarded 3-0, Cuando Cubango dns

### 2022/23

- ogol: 217 jogos casados (edição 167578 do ogol, 240 jogos)
- jogos do Cuando Cubango anulados: o Cuando Cubango desistiu; todos os seus resultados foram anulados
- tabela ango2023:68 fora da conferência: linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- tabela ango2023:318 fora da conferência: linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- tabela ango2023:530 fora da conferência: linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- anulado — 1º de Agosto 0-0 Cuando Cubango (2022-09-28): annulled; o Cuando Cubango desistiu; todos os seus resultados foram anulados
- anulado — Cuando Cubango 0-0 Académica do Lobito (2022-10-02): annulled; o Cuando Cubango desistiu; todos os seus resultados foram anulados
- anulado — Sagrada Esperança 1-0 Cuando Cubango (2022-12-01): annulled; o Cuando Cubango desistiu; todos os seus resultados foram anulados
- anulado — Wiliete 3-1 Cuando Cubango (2022-10-16): annulled; o Cuando Cubango desistiu; todos os seus resultados foram anulados
- anulado — Interclube Cuando Cubango (2022-10-22): annulled; originally awarded 3-0;; o Cuando Cubango desistiu; todos os seus resultados foram anulados
- anulado — Cuando Cubango 1-1 Escolinha Isaac (2022-10-30): annulled; o Cuando Cubango desistiu; todos os seus resultados foram anulados
- anulado — Cuando Cubango 1-0 Bravos do Maqui (2022-11-06): annulled; o Cuando Cubango desistiu; todos os seus resultados foram anulados
- anulado — Santa Rita de Cássia 0-3 Cuando Cubango (2022-11-12): annulled; o Cuando Cubango desistiu; todos os seus resultados foram anulados
- anulado — Cuando Cubango 1-1 Desportivo da Lunda Sul (2022-11-24): annulled; o Cuando Cubango desistiu; todos os seus resultados foram anulados
- decidido fora de campo — Académica do Lobito Sporting de Cabinda (2022-11-24): awarded 3-0; Sporting de Cabinda dns
- anulado — Cuando Cubango 2-0 ASK Dragão (2022-11-27): annulled; o Cuando Cubango desistiu; todos os seus resultados foram anulados
- decidido fora de campo — Bravos do Maqui ASK Dragão (2022-12-03): awarded 3-0; ASK Dragão dns
- anulado — Cuando Cubango 0-1 Desportivo da Huíla (2022-12-04): annulled; o Cuando Cubango desistiu; todos os seus resultados foram anulados
- anulado — Cuando Cubango 0-0 Recreativo do Libolo (2022-12-10): annulled; o Cuando Cubango desistiu; todos os seus resultados foram anulados
- anulado — Cuando Cubango 1-0 Sporting de Cabinda (2022-12-18): annulled; o Cuando Cubango desistiu; todos os seus resultados foram anulados
- anulado — Sporting de Benguela Cuando Cubango (2022-12-22): Cuando Cubango dns; o Cuando Cubango desistiu; todos os seus resultados foram anulados
- anulado — Sporting de Benguela Cuando Cubango (2023-02-01): Cuando Cubango withdrew; o Cuando Cubango desistiu; todos os seus resultados foram anulados
- anulado — Cuando Cubango 1-2 Petro de Luanda (2022-12-14): annulled; o Cuando Cubango desistiu; todos os seus resultados foram anulados

### 2023/24

- ogol: 206 jogos casados (edição 179555 do ogol, 210 jogos)
- placar diferente no ogol — Bravos do Maqui x Sporting de Cabinda (2023-11-18): RSSSF 2-1, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Sporting de Cabinda x Académica do Lobito (2024-03-20): RSSSF 1-1, ogol 2-1; fica o da RSSSF
- decidido fora de campo — 1º de Agosto Petro de Luanda (2023-10-29): awarded 0-3; originally 1-1,
- abandonado/suspenso, sem valer — Kabuscorp Desportivo da Huíla (2023-11-17): abandoned at 0-0 in 53' due to power cuts
- decidido fora de campo — Sporting de Cabinda Santa Rita de Cássia (2023-12-02): awarded 0-3; Sporting de Cabinda dns
- decidido fora de campo — Desportivo da Lunda Sul Sporting de Cabinda (2024-01-09): awarded 3-0; Sporting de Cabinda dns
- não jogado — Interclube Sporting de Cabinda (2024-02-17): Sporting Cabinda dns
- não jogado — Interclube Sporting de Cabinda (2024-02-20): Sporting Cabinda dns
- abandonado/suspenso, sem valer — Desportivo da Lunda Sul União de Malanje (2024-04-13): abandoned at 1-0 in 74' due to heavy rain
- abandonado/suspenso, sem valer — Sporting de Cabinda 1º de Agosto (2024-04-14): abandoned at 1-1 in 90' due to floodlight

### 2024/25

- ogol: 240 jogos casados (edição 189548 do ogol, 240 jogos)
- abandonado/suspenso, sem valer — Desportivo da Lunda Sul Petro de Luanda (2025-02-08): abandoned at 0-1 at half-time
- decidido fora de campo — Desportivo da Lunda Sul Carmona (2025-03-15): awarded 3-0, Carmona dns
- abandonado/suspenso, sem valer — Carmona Escolinha Isaac (2025-05-03): abandoned at 0-0 in 34' due
- abandonado/suspenso, sem valer — Santa Rita de Cássia Interclube (2025-05-11): abandoned at 0-1 in 36' due to

### 2025/26

- ogol: 240 jogos casados (edição 205208 do ogol, 240 jogos)
- abandonado/suspenso, sem valer — Recreativo do Libolo Desportivo da Lunda Sul (2025-10-04): abandoned at 1-0 in 54' due to heavy rain
- abandonado/suspenso, sem valer — Desportivo da Huíla São Salvador (2025-11-02): abandoned at 2-0 in 77' due to heavy rain
- decidido fora de campo — Guelson Desportivo da Huíla (2026-01-30): awarded 0-3; not played due to stage construction
- abandonado/suspenso, sem valer — Desportivo da Lunda Sul Sagrada Esperança (2026-01-30): at Dundo; abandoned at 1-0 in 69' due to heavy rain
- decidido fora de campo — 1º de Agosto Petro de Luanda (2026-03-22): awarded 0-3; Primeiro de Agosto dns
- decidido fora de campo — Desportivo da Lunda Sul Desportivo da Huíla (2026-05-11): awarded 3-0; Desp. Huíla dns; at Dundo

