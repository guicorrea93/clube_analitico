# Campeonato Tanzaniano (1ª divisão) — coleta de dados

Gerado por `python coleta/tan-1/importar.py`. Pacote em `data/coleta/tan-1/pacote/`.

**Edições:** 62, de 1965 a 2025/26: a liga do continente (Tanganica), hoje Ligi Kuu Tanzania Bara, com o campeão do continente em todos os anos. É a lista que a federação (TFF) e os clubes contam (o título de 2024 foi o "30º" do Young Africans). Ano civil até 2007 (a mini-liga de transição de 2007 incluída); duas metades de 2007/08 em diante. Pesquisa de 25/11/2026, aprovada pelo Guilherme.

**Fora do pacote:** a liga de Dar es Salaam (1921 a 1964); a "Union League" de 1982 a 2003, que decidia o título entre os melhores do continente e de Zanzibar (é o campeão que a lista da RSSSF dá nesses anos); a liga de Zanzibar (membro associado da CAF); as copas; as divisões de baixo.

**Fontes:** RSSSF (lista de campeões `tanzchamp.html`; páginas por ano de 1965, de 1982 a 1991 e de 1995/96 em diante: os primeiros colocados, a tabela ou parte dos jogos até 1998, os jogos de 1999 em diante); ogol (jogos de 2007/08 em diante: base de 2011/12, conferência, rodada e data nos outros); Wikipédia em inglês (tabela das temporadas que têm artigo). A ESPN não tem a liga.

**Clubes:** o nome pelo qual o clube é conhecido (Young Africans, Simba, Azam...). Mesmo clube com outro nome na mesma cidade é um só (Simba = Sunderland; Moro United = Kajumulo = Sigara; Kahama United = KJ82 Rangers); mudança de cidade gera outro clube (Singida Black Stars não é o Ihefu). Regras em `coleta/tan-1/clubes_tan.py`.

**Regras:** o placar é o da RSSSF (ou do ogol em 2011/12). A classificação é a tabela publicada (ordem oficial e pontos); nos anos de grupos e fase final (2000 a 2004), a tabela da fase final dá as primeiras posições. Pontos 2-1-0 (vitória, empate, derrota) até 1995 (pelas tabelas até 1989) e 3-1-0 desde 1995/96 (pelas tabelas desde 1996/97).

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Formato |
|---|---|---|---|---|---|---|---|
| 1965 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Simba | sem jogos (só a classificação incompleta) |
| 1966 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Simba | sem jogos (só o campeão) |
| 1967 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Cosmopolitans | sem jogos (só o campeão) |
| 1968 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só o campeão) |
| 1969 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só o campeão) |
| 1970 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só o campeão) |
| 1971 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só o campeão) |
| 1972 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só o campeão) |
| 1973 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Simba | sem jogos (só o campeão) |
| 1974 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só o campeão) |
| 1975 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Mseto Sports | sem jogos (só o campeão) |
| 1976 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Simba | sem jogos (só o campeão) |
| 1977 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Simba | sem jogos (só o campeão) |
| 1978 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Simba | sem jogos (só o campeão) |
| 1979 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Simba | sem jogos (só o campeão) |
| 1980 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Simba | sem jogos (só o campeão) |
| 1981 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só o campeão) |
| 1982 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Pan African | sem jogos (só o campeão) |
| 1983 | 2 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só a classificação incompleta) |
| 1984 | 8 | 56 (56) | 108 | 0 | 1 / 0 | Simba | pontos corridos |
| 1985 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só a tabela final) |
| 1986 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Tukuyu Stars | sem jogos (só a tabela final) |
| 1987 | 10 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só a tabela final) |
| 1988 | 12 | 66 (66) | 120 | 0 | 0 / 0 | Coastal Union | jogos incompletos (só os resultados que a página traz) |
| 1989 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só a tabela final) |
| 1990 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Simba | sem jogos (só o campeão) |
| 1991 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só o campeão) |
| 1992 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só o campeão) |
| 1993 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só o campeão) |
| 1994 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Simba | sem jogos (só o campeão) |
| 1995 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Simba | sem jogos (só o campeão) |
| 1996 | 3 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só a classificação incompleta) |
| 1997 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só a tabela final) |
| 1998 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Young Africans | sem jogos (só a tabela final) |
| 1999 | 16 | 236 (236) | 503 | 0 | 1 / 0 | Mtibwa Sugar | pontos corridos |
| 2000 | 20 | 133 (133) | 305 | 0 | 0 / 0 | Mtibwa Sugar | jogos incompletos (três jogos dos grupos sem resultado na página) |
| 2001 | 24 | 273 (273) | 600 | 2 | 0 / 0 | Simba | jogos incompletos (faltam resultados da 1ª fase) |
| 2002 | 24 | 148 (148) | 302 | 1 | 0 / 0 | Young Africans | jogos incompletos (faltam resultados da 1ª fase e três do "Super 8") |
| 2003 | 24 | 127 (127) | 242 | 4 | 0 / 0 | Simba | jogos incompletos (faltam resultados da 1ª fase e gols do "Super Eight") |
| 2004 | 20 | 165 (165) | 229 | 98 | 0 / 0 | Simba | jogos incompletos (faltam resultados da 1ª fase e do "Super Eight") |
| 2005 | 16 | 195 (195) | 421 | 212 | 0 / 0 | Young Africans | jogos incompletos (só os resultados que a página traz) |
| 2006 | 16 | 161 (161) | 375 | 4 | 0 / 0 | Young Africans | jogos incompletos (só os resultados que a página traz) |
| 2007 | 13 | 57 (57) | 121 | 80 | 5 / 0 | Simba | 3 grupos + fase final + mata-mata |
| 2007/08 | 14 | 183 (183) | 345 | 249 | 1 / 0 | Young Africans | pontos corridos |
| 2008/09 | 12 | 134 (134) | 318 | 128 | 1 / 0 | Young Africans | pontos corridos |
| 2009/10 | 12 | 132 (132) | 307 | 146 | 1 / 0 | Simba | pontos corridos |
| 2010/11 | 12 | 132 (132) | 274 | 66 | 1 / 0 | Young Africans | pontos corridos |
| 2011/12 | 14 | 182 (182) | 411 | 0 | 0 / 1 | Simba | pontos corridos |
| 2012/13 | 14 | 182 (182) | 369 | 0 | 1 / 0 | Young Africans | pontos corridos |
| 2013/14 | 14 | 182 (182) | 407 | 0 | 1 / 0 | Azam | pontos corridos |
| 2014/15 | 14 | 183 (183) | 348 | 0 | 1 / 0 | Young Africans | pontos corridos |
| 2015/16 | 16 | 241 (241) | 495 | 0 | 1 / 0 | Young Africans | pontos corridos |
| 2016/17 | 16 | 240 (240) | 474 | 0 | 1 / 0 | Young Africans | pontos corridos |
| 2017/18 | 16 | 241 (241) | 470 | 0 | 1 / 0 | Simba | pontos corridos |
| 2018/19 | 20 | 381 (381) | 746 | 0 | 1 / 0 | Simba | pontos corridos |
| 2019/20 | 20 | 382 (382) | 767 | 0 | 1 / 0 | Simba | pontos corridos |
| 2020/21 | 18 | 306 (306) | 610 | 201 | 1 / 0 | Simba | pontos corridos |
| 2021/22 | 16 | 242 (242) | 476 | 15 | 1 / 0 | Young Africans | pontos corridos + desempate |
| 2022/23 | 16 | 242 (242) | 566 | 38 | 1 / 0 | Young Africans | pontos corridos + desempate |
| 2023/24 | 16 | 243 (243) | 521 | 12 | 1 / 0 | Young Africans | pontos corridos + desempate |
| 2024/25 | 16 | 242 (242) | 578 | 43 | 1 / 0 | Young Africans | pontos corridos + desempate |
| 2025/26 | 16 | 242 (242) | 524 | 0 | 1 / 0 | Young Africans | pontos corridos + desempate |

## Conferência e correções, edição a edição

### 1965

- a RSSSF só traz os primeiros colocados

### 1966

- a RSSSF só traz o campeão

### 1967

- a RSSSF só traz o campeão

### 1968

- a RSSSF só traz o campeão

### 1969

- a RSSSF só traz o campeão

### 1970

- a RSSSF só traz o campeão

### 1971

- a RSSSF só traz o campeão

### 1972

- a RSSSF só traz o campeão

### 1973

- a RSSSF só traz o campeão

### 1974

- a RSSSF só traz o campeão

### 1975

- a RSSSF só traz o campeão

### 1976

- a RSSSF só traz o campeão

### 1977

- a RSSSF só traz o campeão

### 1978

- a RSSSF só traz o campeão

### 1979

- a RSSSF só traz o campeão

### 1980

- a RSSSF só traz o campeão

### 1981

- a RSSSF só traz o campeão

### 1982

- a RSSSF só traz o campeão do continente

### 1983

- a RSSSF só traz os primeiros colocados

### 1984

- sem ocorrências

### 1985

- a RSSSF só traz a tabela final

### 1986

- a RSSSF só traz a tabela final

### 1987

- a RSSSF só traz a tabela final

### 1988

- jogos incompletos (só os resultados que a página traz)

### 1989

- a RSSSF só traz a tabela final

### 1990

- a RSSSF só traz o campeão do continente

### 1991

- a RSSSF só traz o campeão do continente

### 1992

- a RSSSF só traz o campeão

### 1993

- a RSSSF só traz o campeão

### 1994

- a RSSSF só traz o campeão

### 1995

- a RSSSF só traz o campeão

### 1996

- a RSSSF só traz os primeiros colocados

### 1997

- a RSSSF só traz a tabela final

### 1998

- a RSSSF só traz a tabela final

### 1999

- corrigido — Young Africans x Pamba (1999-04-14): a nota diz que o jogo ainda podia ser dado ao Young Africans ("may yet be awarded 2-0"), mas a tabela conta o 1-1 de campo
- corrigido — Tanzania Prisons x Kariakoo (1999-09-11): "abandoned in 78' at 2-0; awarded 2-0": não é abandono sem valer; a tabela conta o jogo
- decidido fora de campo — Arusha FC Milambo (1999-03-06): awarded 2-0, abd 75'
- decidido fora de campo — Kagera Stars Milambo (1999-03-31): awarded 2-0, Milambo dns
- decidido fora de campo — Milambo Mtibwa Sugar (1999-04-03): awarded 0-2, Milambo dns
- decidido fora de campo — Kariakoo Pamba (1999-04-10): awarded 2-0, Pamba attacked referee
- decidido fora de campo — Kariakoo Kagera Stars (1999-04-16): awarded 2-0, Kagera walked off the pitch
- decidido fora de campo — Tanzania Prisons Toto Africans (1999-04-21): awarded 2-0, Toto Africans dns
- decidido fora de campo — Maji Maji Toto Africans (1999-04-23): awarded 2-0, Toto Africans dns
- decidido fora de campo — Toto Africans Pamba (1999-05-08): awarded 0-2, Toto Africans walked off the pitch
- decidido fora de campo — Milambo Young Africans (1999-05-15): awarded 2-0, abandoned in 89' after goal Milambo
- decidido fora de campo — Milambo Maji Maji (1999-05-19): awarded 2-0, Maji Maji dns
- decidido fora de campo — Toto Africans Kariakoo (1999-05-03): awarded 2-0, abandoned in 88' after goal Toto Africans
- decidido fora de campo — Tukuyu Stars Young Africans (1999-06-16): awarded 2-0, Yanga dns
- decidido fora de campo — Maji Maji Kagera Stars (1999-06-19): awarded 2-0, Kagera Stars dns
- decidido fora de campo — Tukuyu Stars Kagera Stars (1999-06-23): awarded 2-0, Kagera Stars dns
- decidido fora de campo — Kariakoo Simba (1999-07-10): awarded 2-0, abandoned in 51' after Kariakoo goal
- decidido fora de campo — Kariakoo Coastal Union (1999-07-14): awarded 2-0, Coastal Union dns
- decidido fora de campo — Toto Africans Mtibwa Sugar (1999-07-14): awarded 0-2, Toto Africans dns
- decidido fora de campo — Maji Maji Milambo (1999-07-17): awarded 2-0, Milambo dns
- decidido fora de campo — Kagera Stars Mtibwa Sugar (1999-07-21): awarded 2-0, abandoned in 81' after Kagera Stars goal
- decidido fora de campo — Kariakoo Reli Morogoro (1999-07-21): awarded 2-0, Reli dns
- decidido fora de campo — Lipuli Milambo (1999-07-22): awarded 2-0, Milambo dns
- decidido fora de campo — Kariakoo Arusha FC (1999-07-24): awarded 2-0, AFC dns
- decidido fora de campo — Arusha FC Lipuli (1999-08-02): awarded 2-0, Lipuli dns
- decidido fora de campo — Tukuyu Stars Milambo (1999-08-04): awarded 2-0
- decidido fora de campo — Simba Pamba (1999-08-21): awarded 2-0; abandoned in 26' after Pamba
- decidido fora de campo — Tanzania Prisons Pamba (1999-09-03): awarded 2-0; Pamba dns
- decidido fora de campo — Mtibwa Sugar Simba (1999-09-11): awarded 2-0; abandoned in 38' when 2 Simba
- decidido fora de campo — Tanzania Prisons Kariakoo (1999-09-11): abandonado aos 78' com 2-0
- decidido fora de campo — Tanzania Prisons Milambo (1999-09-18): awarded 2-0

### 2000

- jogos incompletos (três jogos dos grupos sem resultado na página)
- corrigido — Tukuyu Stars x Maji Maji (None): "Tukuyu-Majimaji abandoned at 2-1 in 89', awarded 2-0"
- corrigido — Mji Mpwapwa x Mtibwa Sugar (None): "Mji vs Mtibwa awarded 0-2, Mji dns"
- decidido fora de campo — Mtibwa Sugar Kagera Stars (2000-07-22): awarded 2-0; Kagera dns
- decidido fora de campo — Kagera Stars Tanzania Prisons (2000-08-05): awarded 0-2, Kagera dns
- decidido fora de campo — Tanzania Prisons Mtibwa Sugar (2000-08-10): awarded 0-2
- decidido fora de campo — Tukuyu Stars Maji Maji (s/d): abandonado aos 89' com 2-1
- decidido fora de campo — Mji Mpwapwa Mtibwa Sugar (s/d): o Mji não compareceu

### 2001

- jogos incompletos (faltam resultados da 1ª fase)
- jogos do Kagera Stars anulados: o Kagera Stars foi excluído por não comparecer a 3 jogos; todos os seus jogos foram anulados
- tabela tanz01:35 fora da conferência: linha da campanha anulada de um clube excluído (não conta na classificação)
- tabela tanz01:500 fora da conferência: linha da campanha anulada de um clube excluído (não conta na classificação)
- anulado — Kagera Stars 2-3 Moro United (2001-02-21): annulled; o Kagera Stars foi excluído por não comparecer a 3 jogos; todos os seus jogos foram anulados
- anulado — Kagera Stars 1-1 Kahama United (2001-02-24): annulled; o Kagera Stars foi excluído por não comparecer a 3 jogos; todos os seus jogos foram anulados
- anulado — Kagera Stars 0-2 Reli Morogoro (2001-02-28): annulled; o Kagera Stars foi excluído por não comparecer a 3 jogos; todos os seus jogos foram anulados
- anulado — Kagera Stars 0-1 Lipuli (2001-03-03): annulled; o Kagera Stars foi excluído por não comparecer a 3 jogos; todos os seus jogos foram anulados
- decidido fora de campo — Bandari Arusha FC (2001-03-03): awarded 2-0 in April
- anulado — Tanzania Prisons 6-0 Kagera Stars (2001-03-07): annulled; o Kagera Stars foi excluído por não comparecer a 3 jogos; todos os seus jogos foram anulados
- abandonado/suspenso, sem valer — Mtibwa Sugar Nazareth (2001-03-07): abd at 0-0 in 58' due to rain
- anulado — CDA Dodoma Kagera Stars (2001-03-10): awarded 2-0; abd at 0-1 in 70', four; o Kagera Stars foi excluído por não comparecer a 3 jogos; todos os seus jogos foram anulados
- anulado — Moro United 2-1 Reli Morogoro (2001-03-10): Kagera players sent off - annulled]
- decidido fora de campo — Mji Mpwapwa Milambo (2001-03-10): abd at 4-1, awarded 2-0 (inferred)
- anulado — Young Africans 4-0 Kagera Stars (2001-03-15): annulled; o Kagera Stars foi excluído por não comparecer a 3 jogos; todos os seus jogos foram anulados
- decidido fora de campo — Arusha FC Milambo (2001-03-15): Milambo dns, awarded 2-0
- anulado — Singida United 6-0 Kagera Stars (2001-03-25): annulled; o Kagera Stars foi excluído por não comparecer a 3 jogos; todos os seus jogos foram anulados
- anulado — Kagera Stars 1-1 Pamba (2001-04-04): annulled; o Kagera Stars foi excluído por não comparecer a 3 jogos; todos os seus jogos foram anulados
- decidido fora de campo — Toto Africans Maji Maji (2001-04-04): Majimaji dns, awarded 2-0
- anulado — Kariakoo Kagera Stars (2001-04-04): Kagera dns, awarded 2-0 - annulled; o Kagera Stars foi excluído por não comparecer a 3 jogos; todos os seus jogos foram anulados
- anulado — KJ977 Meru Warriors Kagera Stars (2001-04-07): Kagera dns, awarded 2-0 - annulled; o Kagera Stars foi excluído por não comparecer a 3 jogos; todos os seus jogos foram anulados
- decidido fora de campo — KJ44 Karume Rangers Milambo (2001-04-07): awarded 2-0
- decidido fora de campo — Coastal Union Arusha FC (2001-04-29): awarded 2-0, originally 1-2
- anulado — Young Africans 5-1 Kagera Stars (2001-04-29): annulled; o Kagera Stars foi excluído por não comparecer a 3 jogos; todos os seus jogos foram anulados
- decidido fora de campo — Bandari Milambo (2001-05-05): Milambo dns, awd 2-0
- anulado — Reli Morogoro Kagera Stars (2001-05-07): Kagera dns, awarded 2-0 - annulled; o Kagera Stars foi excluído por não comparecer a 3 jogos; todos os seus jogos foram anulados
- abandonado/suspenso, sem valer — Arusha FC KJ44 Karume Rangers (2001-05-07)
- abandonado/suspenso, sem valer — Mtibwa Sugar Nazareth (2001-05-17): abd at 0-0 in 58' due to rain
- decidido fora de campo — Tanzania Prisons Singida United (2001-06-13): Singida dns; awarded 2-0
- decidido fora de campo — Tanzania Prisons CDA Dodoma (2001-06-16): CDA dns; awarded 2-0
- decidido fora de campo — Coastal Union Mtibwa Sugar (2001-06-16): Mtibwa dns; awarded 2-0
- decidido fora de campo — Maji Maji Arusha FC (2001-06-16): awarded 0-2, originally 2-1
- decidido fora de campo — Coastal Union Nazareth (2001-06-20): Nazareth dns; awd 2-0
- decidido fora de campo — Arusha FC Mtibwa Sugar (2001-07-01): awarded 2-0, Mtibwa dns
- decidido fora de campo — Coastal Union Mtibwa Sugar (2001-07-04): awarded 2-0, Mtibwa dns
- decidido fora de campo — Singida United Lipuli (2001-07-04): awarded 2-0, Lipuli dns
- decidido fora de campo — Arusha FC Coastal Union (2001-07-04): awarded 0-2, originally 2-1
- decidido fora de campo — Tanzania Prisons CDA Dodoma (2001-07-17): awarded 2-0, CDA dns
- decidido fora de campo — Coastal Union Tanzania Prisons (2001-08-18): awarded 2-0, Prisons arrived late
- decidido fora de campo — KJ977 Meru Warriors Tanzania Prisons (2001-08-22): awarded 2-0; abd at 1-0 in 87' after
- decidido fora de campo — Coastal Union Bandari (2001-09-30): awarded 2-0, Bandari dns

### 2002

- jogos incompletos (faltam resultados da 1ª fase e três do "Super 8")
- W.O./pontos para o visitante — KJ977 Meru Warriors Polisi Morogoro (2002-04-27): by 1 goal]  [lt
- W.O./pontos para o mandante — Polisi Morogoro Bandari (2002-05-08): by 1 goal]  [bt
- W.O./pontos para o mandante — Arusha FC Nazareth (2002-05-08): bt
- W.O./pontos para o mandante — Mji Mpwapwa Kariakoo (2002-05-08): by 1 goal]  [bt
- W.O./pontos para o mandante — Simba Polisi Morogoro (2002-05-11): May 25; by 1 goal]  [bt
- W.O./pontos para o mandante — Arusha FC Reli Morogoro (2002-06-01): bt
- W.O./pontos para o visitante — KJ44 Karume Rangers Vijana (2002-06-01): lt
- W.O./pontos para o mandante — KJ977 Meru Warriors CDA Dodoma (2002-06-07): by 1 goal]  [bt
- W.O./pontos para o mandante — Nazareth Kariakoo (2002-06-07): bt
- decidido fora de campo — Tukuyu Stars Coastal Union (2002-06-10): awarded 2-0, Coastal U. dns
- decidido fora de campo — Bandari Polisi Morogoro (2002-06-15): abd in 88' due to referee attack by Jun 16]                               Police players, awarded 2-0 to Bandari?
- decidido fora de campo — Kahama United KJ44 Karume Rangers (2002-06-23): awarded 2-0, KJ44 dns
- W.O./pontos para o mandante — Reli Morogoro Kahama United (2002-09-21): bt

### 2003

- jogos incompletos (faltam resultados da 1ª fase e gols do "Super Eight")
- W.O./pontos para o mandante — Tanzania Prisons Mmbanga (2003-06-14): bt
- W.O./pontos para o mandante — Moro United Kahama United (2003-06-14): bt
- decidido fora de campo — Tanzania Prisons Reli Morogoro (2003-07-01): awarded 2-0, Reli dns
- abandonado/suspenso, sem valer — Nazareth Mtibwa Sugar (2003-07-02): abandoned at 1-1 in 85', replay Aug 2
- decidido fora de campo — Reli Morogoro Kahama United (2003-07-06): awarded 0-2, Reli disbanded
- decidido fora de campo — Polisi Mara Twiga Sports (2003-07-10): awarded 0-2, Police Mara dns
- não jogado — JKT Tanzania Reli Morogoro (2003-07-12): Reli disbanded
- não jogado — Young Africans Pallsons (2003-07-13): Pallsons dns as match moved from Arusha to Jul 14]                            Dodoma at short notice, replay Aug 2
- decidido fora de campo — Kahama United Moro United (2003-07-13): awarded 2-0, Moro withdrew at 1-1 in 81'
- W.O./pontos para o visitante — Polisi Kagera Young Africans (2003-07-17): lt
- W.O./pontos para o mandante — Mji Mpwapwa Arusha FC (2003-07-19): bt
- W.O./pontos para o mandante — Pallsons Vijana (2003-07-19): bt
- não jogado — Nazareth Mtibwa Sugar (2003-08-02)
- W.O./pontos para o visitante — Kahama United Mtibwa Sugar (2003-11-02): lt
- W.O./pontos para o mandante — Tanzania Prisons Kahama United (2003-11-02): bt
- W.O./pontos para o mandante — Pallsons Tanzania Prisons (2003-11-02): bt
- W.O./pontos para o visitante — Twiga Sports Tanzania Prisons (2003-11-02): lt
- W.O./pontos para o mandante — Tanzania Prisons Arusha FC (2003-11-02): bt
- W.O./pontos para o visitante — Kahama United Twiga Sports (2003-11-02): lt
- W.O./pontos para o mandante — Arusha FC Twiga Sports (2003-11-02): probably awarded 2-0]  [bt
- W.O./pontos para o mandante — Pallsons Twiga Sports (2003-11-02): probably awarded 2-0]  [bt
- W.O./pontos para o mandante — Mtibwa Sugar Pallsons (2003-11-02): bt
- W.O./pontos para o visitante — Pallsons Arusha FC (2003-11-02): lt
- W.O./pontos para o visitante — Kahama United Arusha FC (2003-11-06): lt
- W.O./pontos para o visitante — Kahama United Pallsons (2003-11-20): lt
- W.O./pontos para o mandante — Simba Twiga Sports (2003-11-22): bt

### 2004

- jogos incompletos (faltam resultados da 1ª fase e do "Super Eight")
- jogos do Reli Kigoma anulados: o Reli foi desclassificado em 5/7; a campanha foi anulada
- jogos do Kariakoo anulados: o Kariakoo foi desclassificado em 5/7; a campanha foi anulada
- jogos do Pallsons anulados: o Pallsons desistiu em 3/6; a campanha foi anulada
- linha de nota que repete o jogo Moro United x None (tanz04:63): fica de fora
- linha de nota que repete o jogo Moro United x None (tanz04:493): fica de fora
- tabela tanz04:31 fora da conferência: linha da campanha anulada de um clube excluído (não conta na classificação)
- tabela tanz04:51 fora da conferência: linha da campanha anulada de um clube excluído (não conta na classificação)
- tabela tanz04:53 fora da conferência: linha da campanha anulada de um clube excluído (não conta na classificação)
- tabela tanz04:461 fora da conferência: linha da campanha anulada de um clube excluído (não conta na classificação)
- tabela tanz04:481 fora da conferência: linha da campanha anulada de um clube excluído (não conta na classificação)
- tabela tanz04:483 fora da conferência: linha da campanha anulada de um clube excluído (não conta na classificação)
- anulado — Reli Kigoma 0-1 Vijana (2004-04-17): annulled; o Reli foi desclassificado em 5/7; a campanha foi anulada
- anulado — Twiga Sports 1-0 Kariakoo (2004-04-17): annulled; o Kariakoo foi desclassificado em 5/7; a campanha foi anulada
- anulado — Pallsons 1-2 Moro United (2004-04-19): in Shinyanga; annulled; o Pallsons desistiu em 3/6; a campanha foi anulada
- anulado — Reli Kigoma 0-2 Tanzania Prisons (2004-04-21): annulled; o Reli foi desclassificado em 5/7; a campanha foi anulada
- anulado — Simba 5-1 Pallsons (2004-04-21): in Shinyanga; annulled; o Pallsons desistiu em 3/6; a campanha foi anulada
- anulado — Kariakoo 1-0 Tukuyu Stars (2004-04-21): annulled; o Kariakoo foi desclassificado em 5/7; a campanha foi anulada
- anulado — Reli Kigoma 1-2 Polisi Dodoma (2004-04-25): annulled; o Reli foi desclassificado em 5/7; a campanha foi anulada
- anulado — Pallsons 1-1 JKT Tanzania (2004-04-25): annulled; o Pallsons desistiu em 3/6; a campanha foi anulada
- anulado — Kariakoo 0-0 Mji Mpwapwa (2004-04-25): annulled; o Kariakoo foi desclassificado em 5/7; a campanha foi anulada
- anulado — Transit Camp 2-1 Reli Kigoma (2004-04-28): in Kigoma; annulled; o Reli foi desclassificado em 5/7; a campanha foi anulada
- anulado — Mji Mpwapwa 3-2 Pallsons (2004-04-28): annulled; o Pallsons desistiu em 3/6; a campanha foi anulada
- anulado — Mtibwa Sugar 3-0 Kariakoo (2004-04-29): annulled; o Kariakoo foi desclassificado em 5/7; a campanha foi anulada
- anulado — Moro United 2-0 Kariakoo (2004-05-01): annulled; o Kariakoo foi desclassificado em 5/7; a campanha foi anulada
- anulado — Twiga Sports 2-1 Pallsons (2004-05-01): in Tanga; annulled; o Pallsons desistiu em 3/6; a campanha foi anulada
- anulado — Arusha FC 2-0 Reli Kigoma (2004-05-05): inferred; 2-1?; annulled; o Reli foi desclassificado em 5/7; a campanha foi anulada
- anulado — Kahama United 0-1 Pallsons (2004-05-05): annulled; o Pallsons desistiu em 3/6; a campanha foi anulada
- anulado — KJ44 Karume Rangers 3-0 Reli Kigoma (2004-05-08): inferred; 3-1?; annulled; o Reli foi desclassificado em 5/7; a campanha foi anulada
- anulado — JKT Tanzania 2-0 Kariakoo (2004-05-23): annulled; o Kariakoo foi desclassificado em 5/7; a campanha foi anulada
- anulado — Tukuyu Stars 3-1 Pallsons (2004-05-09): annulled; o Pallsons desistiu em 3/6; a campanha foi anulada
- anulado — Bandari 2-0 Reli Kigoma (2004-05-12): 2-1?; annulled; o Reli foi desclassificado em 5/7; a campanha foi anulada
- anulado — Kariakoo 0-1 Simba (2004-06-06): annulled; o Kariakoo foi desclassificado em 5/7; a campanha foi anulada
- anulado — Reli Kigoma 2-0 Maji Maji (2004-05-18): annulled; o Reli foi desclassificado em 5/7; a campanha foi anulada
- anulado — Pallsons Kariakoo (2004-05-19): neither team showed; o Kariakoo foi desclassificado em 5/7; a campanha foi anulada; o Pallsons desistiu em 3/6; a campanha foi anulada
- anulado — Kahama United Kariakoo (2004-05-15): awarded 2-0, Kariakoo dns; annulled; o Kariakoo foi desclassificado em 5/7; a campanha foi anulada
- anulado — Pallsons Mtibwa Sugar (2004-05-22): awarded 0-2, Pallsons dns; annulled; o Pallsons desistiu em 3/6; a campanha foi anulada
- anulado — Reli Kigoma 0-2 Young Africans (2004-05-23): annulled; o Reli foi desclassificado em 5/7; a campanha foi anulada
- anulado — Reli Kigoma 2-1 Arusha FC (2004-05-26): annulled; o Reli foi desclassificado em 5/7; a campanha foi anulada
- anulado — Pallsons Kahama United (2004-06-05): in Shinyanga; o Pallsons desistiu em 3/6; a campanha foi anulada
- anulado — Reli Kigoma 1-0 KJ44 Karume Rangers (2004-05-31): annulled; o Reli foi desclassificado em 5/7; a campanha foi anulada
- anulado — Moro United Pallsons (2004-06-13): o Pallsons desistiu em 3/6; a campanha foi anulada
- anulado — Mji Mpwapwa Kariakoo (2004-06-16): o Kariakoo foi desclassificado em 5/7; a campanha foi anulada
- anulado — Reli Kigoma Bandari (2004-06-05): Reli dns; o Reli foi desclassificado em 5/7; a campanha foi anulada
- anulado — Mtibwa Sugar Pallsons (2004-06-19): o Pallsons desistiu em 3/6; a campanha foi anulada
- anulado — Simba Kariakoo (2004-06-20): in Shinyanga; o Kariakoo foi desclassificado em 5/7; a campanha foi anulada
- anulado — Tanzania Prisons Reli Kigoma (2004-06-30): o Reli foi desclassificado em 5/7; a campanha foi anulada
- anulado — Polisi Dodoma 3-1 Reli Kigoma (2004-06-24): annulled; o Reli foi desclassificado em 5/7; a campanha foi anulada
- anulado — Maji Maji Reli Kigoma (2004-06-27): Reli dns; o Reli foi desclassificado em 5/7; a campanha foi anulada
- anulado — Kariakoo Twiga Sports (2004-07-04): Kariakoo dns; o Kariakoo foi desclassificado em 5/7; a campanha foi anulada
- anulado — Vijana Reli Kigoma (2004-07-03): Reli dns; in Tanga; o Reli foi desclassificado em 5/7; a campanha foi anulada
- W.O./pontos para o mandante — Kahama United Twiga Sports (2004-07-21): bt
- decidido fora de campo — Twiga Sports Moro United (2004-07-25): in Tanga; Twiga dns; awarded 0-2

### 2005

- jogos incompletos (só os resultados que a página traz)
- tabela tanz05:347 fora da conferência: tabela do meio da temporada (a final vem depois)
- tabela tanz05:352 fora da conferência: tabela do meio da temporada (a final vem depois)
- tabela tanz05:355 fora da conferência: tabela do meio da temporada (a final vem depois)
- tabela tanz05:454 fora da conferência: tabela do meio da temporada (a final vem depois)
- tabela tanz05:461 fora da conferência: tabela do meio da temporada (a final vem depois)
- decidido fora de campo — Bandari Arusha FC (2005-05-25): awarded 2-0, AFC dns
- decidido fora de campo — Kagera Sugar Maji Maji (2005-06-01): awarded 2-0, Majimaji dns
- decidido fora de campo — Kagera Sugar Twiga Sports (2005-06-09): awarded 2-0, Twiga dns
- W.O./pontos para o visitante — Tanzania Prisons Ashanti United (2005-06-12): lt
- W.O./pontos para o mandante — Kagera Sugar Kahama United (2005-07-20): ?]  [bt
- decidido fora de campo — Tanzania Prisons Mji Mpwapwa (2005-09-10): awarded 2-0, Mji dns

### 2006

- jogos incompletos (só os resultados que a página traz)
- W.O./pontos para o mandante — Kagera Sugar Ashanti United (2006-02-25): bt
- W.O./pontos para o mandante — Kahama United Polisi Dodoma (2006-02-25): bt
- W.O./pontos para o mandante — Kagera Sugar Polisi Dodoma (2006-03-01): bt
- W.O./pontos para o mandante — JKT Tanzania Kahama United (2006-03-15): inferred]  [bt
- decidido fora de campo — Kagera Sugar Simba (2006-06-03): awarded 2-0 on Oct 30, originally 1-0
- W.O./pontos para o mandante — JKT Tanzania Mtibwa Sugar (2006-06-18): bt
- W.O./pontos para o visitante — Bandari Twiga Sports (2006-06-21): lt
- W.O./pontos para o visitante — Kahama United Mtibwa Sugar (2006-10-22): lt
- W.O./pontos para o mandante — Twiga Sports Polisi Morogoro (2006-11-21): bt

### 2007

- mini-liga de transição ("Ligi Ndogo") antes da mudança para temporadas de duas metades; a final (Simba x Young Africans, 1-1 e pênaltis) deu as vagas da CAF de 2008
- decidido fora de campo — Simba Ashanti United (2007-04-21): awarded 0-2; abandoned in 42'
- W.O./pontos para o mandante — JKT Tanzania Pan African (2007-05-02): bt

### 2007/08

- ogol: 180 jogos casados (edição 53179 do ogol, 182 jogos)
- decidido fora de campo — Simba Coastal Union (2008-01-27): awarded 0-2; originally 2-1, Nico Nyagawa 26, Musa Hassam 49;           Simba fielded suspended Uhuru Selemani 37]                         players
- abandonado/suspenso, sem valer — Manyema Rangers Young Africans (2008-04-09): abandoned at 1-3 in 67'

### 2008/09

- ogol: 132 jogos casados (edição 53177 do ogol, 132 jogos)
- abandonado/suspenso, sem valer — Tanzania Prisons Kagera Sugar (2009-03-24): abandoned at 1-1 in 30' due
- abandonado/suspenso, sem valer — Polisi Dodoma Young Africans (2009-04-11): abandoned at 0-1 in 70'

### 2009/10

- ogol: 132 jogos casados (edição 53174 do ogol, 132 jogos)

### 2010/11

- ogol: 131 jogos casados (edição 53164 do ogol, 132 jogos)

### 2011/12

- ogol: base dos jogos (182 jogos)
- tabela publicada x jogos — tanz2012:22: JKT Oljoro tabela [26, 9, 8, 9, 21, 26] jogos [26, 9, 8, 9, 20, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — tanz2012:22: African Lyon tabela [26, 6, 9, 11, 23, 30] jogos [26, 6, 9, 11, 23, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — tanz2012:22: Villa Squad tabela [26, 7, 5, 14, 29, 46] jogos [26, 7, 5, 14, 30, 46] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — tanz2012:22: Polisi Dodoma tabela [26, 3, 8, 15, 19, 36] jogos [26, 3, 8, 15, 18, 35] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- provável jogo da diferença: Polisi Dodoma 0-0 JKT Oljoro (2011-10-29, ogol:2138111); com 1-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: JKT Oljoro 1-0 Polisi Dodoma (2012-05-06, ogol:2138208); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: African Lyon 3-2 Villa Squad (2011-10-24, ogol:2138105); com 3-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 2012/13

- ogol: 180 jogos casados (edição 53154 do ogol, 182 jogos)
- placar diferente no ogol — Kagera Sugar x JKT Oljoro (2012-09-19): RSSSF 0-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Kagera Sugar x Polisi Morogoro (2012-11-10): RSSSF 1-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — JKT Oljoro x Ruvu Shooting (2012-11-10): RSSSF 2-3, ogol 1-3; fica o da RSSSF
- placar diferente no ogol — Polisi Morogoro x Kagera Sugar (2013-05-01): RSSSF 1-0, ogol 2-0; fica o da RSSSF

### 2013/14

- ogol: 180 jogos casados (edição 65032 do ogol, 182 jogos)
- placar diferente no ogol — Tanzania Prisons x Rhino Rangers (2014-04-13): RSSSF 4-3, ogol 3-2; fica o da RSSSF

### 2014/15

- ogol: 182 jogos casados (edição 73167 do ogol, 182 jogos)
- data diferente no ogol — Ruvu Shooting x Coastal Union: RSSSF 2015-03-14, ogol 2015-03-21; fica a da RSSSF
- data diferente no ogol — Kagera Sugar x Mtibwa Sugar: RSSSF 2015-04-01, ogol 2015-03-28; fica a da RSSSF
- abandonado/suspenso, sem valer — Stand United Mtibwa Sugar (2015-04-05): abandoned at 1-0 in 39'

### 2015/16

- ogol: 240 jogos casados (edição 92221 do ogol, 240 jogos)
- placar diferente no ogol — Kagera Sugar x Coastal Union (2016-03-13): RSSSF 3-0, ogol 4-0; fica o da RSSSF
- abandonado/suspenso, sem valer — Mtibwa Sugar Stand United (2016-01-30): abandoned at 1-0 due to heavy rain
- decidido fora de campo — Mbeya City Azam (2016-02-20): awarded 3-0; originally 0-3, Azam fielded

### 2016/17

- ogol: 238 jogos casados (edição 100051 do ogol, 240 jogos)
- placar diferente no ogol — Ruvu Shooting x Maji Maji (2017-04-15): RSSSF 4-1, ogol 4-2; fica o da RSSSF

### 2017/18

- ogol: 235 jogos casados (edição 113579 do ogol, 240 jogos)
- placar diferente no ogol — Njombe Mji x Tanzania Prisons (2017-08-26): RSSSF 1-2, ogol 0-2; fica o da RSSSF
- abandonado/suspenso, sem valer — Tanzania Prisons Mbao (2018-03-03): abandoned at 1-0 in 41'

### 2018/19

- ogol: 346 jogos casados (edição 134130 do ogol, 380 jogos)
- data diferente no ogol — Mbeya City x Alliance: RSSSF 2018-09-16, ogol 2018-09-12; fica a da RSSSF
- data diferente no ogol — Young Africans x Stand United: RSSSF 2018-09-16, ogol 2018-09-12; fica a da RSSSF
- data diferente no ogol — Mbao x African Lyon: RSSSF 2018-12-11, ogol 2018-12-07; fica a da RSSSF
- data diferente no ogol — Lipuli x JKT Tanzania: RSSSF 2019-01-12, ogol 2019-01-08; fica a da RSSSF
- data diferente no ogol — Biashara United x Coastal Union: RSSSF 2019-01-13, ogol 2019-01-08; fica a da RSSSF
- data diferente no ogol — Mbao x Stand United: RSSSF 2019-01-13, ogol 2019-01-08; fica a da RSSSF
- data diferente no ogol — Mtibwa Sugar x Ndanda: RSSSF 2019-01-31, ogol 2019-01-25; fica a da RSSSF
- data diferente no ogol — Singida United x African Lyon: RSSSF 2019-01-31, ogol 2019-01-25; fica a da RSSSF
- data diferente no ogol — Kagera Sugar x Tanzania Prisons: RSSSF 2019-02-01, ogol 2019-01-25; fica a da RSSSF
- data diferente no ogol — Stand United x KMC: RSSSF 2019-02-01, ogol 2019-01-25; fica a da RSSSF
- data diferente no ogol — JKT Tanzania x Mwadui: RSSSF 2019-02-01, ogol 2019-01-25; fica a da RSSSF
- data diferente no ogol — Ruvu Shooting x Mbeya City: RSSSF 2019-02-01, ogol 2019-01-25; fica a da RSSSF
- data diferente no ogol — Alliance x Lipuli: RSSSF 2019-02-02, ogol 2019-01-25; fica a da RSSSF
- data diferente no ogol — Coastal Union x Young Africans: RSSSF 2019-02-03, ogol 2019-01-25; fica a da RSSSF
- data diferente no ogol — Biashara United x Ndanda: RSSSF 2019-03-11, ogol 2019-03-07; fica a da RSSSF
- data diferente no ogol — Simba x Ruvu Shooting: RSSSF 2019-03-19, ogol 2019-03-15; fica a da RSSSF
- data diferente no ogol — Mbao x Ndanda: RSSSF 2019-05-04, ogol 2019-04-30; fica a da RSSSF
- data diferente no ogol — KMC x Mwadui: RSSSF 2019-05-06, ogol 2019-04-30; fica a da RSSSF
- data diferente no ogol — Stand United x Azam: RSSSF 2019-05-06, ogol 2019-04-30; fica a da RSSSF
- data diferente no ogol — Simba x Coastal Union: RSSSF 2019-05-08, ogol 2019-04-30; fica a da RSSSF
- data diferente no ogol — Mbeya City x Coastal Union: RSSSF 2019-05-15, ogol 2019-05-08; fica a da RSSSF
- data diferente no ogol — Kagera Sugar x Stand United: RSSSF 2019-05-16, ogol 2019-05-12; fica a da RSSSF
- data diferente no ogol — JKT Tanzania x Kagera Sugar: RSSSF 2019-05-25, ogol 2019-05-20; fica a da RSSSF
- abandonado/suspenso, sem valer — Lipuli Biashara United (2018-12-02): abandoned at 0-0 in 26' due to waterlogged pitch

### 2019/20

- ogol: 342 jogos casados (edição 145642 do ogol, 380 jogos)
- decidido fora de campo — Ruvu Shooting Tanzania Prisons (2020-02-11): awarded 0-3; Ruvu failed to provide
- abandonado/suspenso, sem valer — KMC JKT Tanzania (2020-03-04): abandoned at 0-0 in 11' due to waterlogged pitch
- abandonado/suspenso, sem valer — Polisi Tanzania Mtibwa Sugar (2020-03-10): abandoned at 0-0 due to rain

### 2020/21

- ogol: 272 jogos casados (edição 161139 do ogol, 306 jogos)

### 2021/22

- ogol: 210 jogos casados (edição 166148 do ogol, 240 jogos)
- decidido fora de campo — Namungo Mbeya Kwanza (2022-05-13): awarded 3-0; Mbeya Kwanza forfeited

### 2022/23

- ogol: 210 jogos casados (edição 170641 do ogol, 240 jogos)

### 2023/24

- ogol: 240 jogos casados (edição 182070 do ogol, 240 jogos)
- placar diferente no ogol — Namungo x Simba (2024-04-30): RSSSF 2-2, ogol 3-3; fica o da RSSSF
- placar diferente no ogol — Tabora United x Mashujaa (2024-05-12): RSSSF 1-0, ogol 2-0; fica o da RSSSF
- abandonado/suspenso, sem valer — Kagera Sugar Geita Gold (2023-09-16): abandoned at 0-0 in 39' due to power cut

### 2024/25

- ogol: 240 jogos casados (edição 188989 do ogol, 240 jogos)
- placar diferente no ogol — Simba x JKT Tanzania (2024-12-24): RSSSF 1-0, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — JKT Tanzania x Singida Fountain Gate (2025-05-13): RSSSF 3-1, ogol 2-0; fica o da RSSSF

### 2025/26

- ogol: 210 jogos casados (edição 205179 do ogol, 240 jogos)
- decidido fora de campo — Dodoma Jiji Pamba (2025-10-25): awarded 0-3; abandoned at 1-0 in first half due to power cut

