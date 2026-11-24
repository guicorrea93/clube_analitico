# Campeonato Sul-Africano (1ª divisão) — coleta de dados

Gerado por `python coleta/rsa-1/importar.py`. Pacote em `data/coleta/rsa-1/pacote/`.

**Edições:** 55: NPSL de 1971 a 1984, NSL de 1985 a 1995 e PSL de 1996/97 a 2025/26, como a lista de campeões da RSSSF (`zafchamp.html`, "NPSL/NSL/PSL championships, 55, since 1971") e a imprensa contam (pesquisa de 24/11/2026, aprovada pelo Guilherme). Ficam de fora as ligas separadas por raça do apartheid (NFL dos brancos, SASL/FPL), a NPSL que seguiu em paralelo depois de 1985, as NPSL amadoras de 1968 e 1969 e o torneio de transição de 1996.

**Fora do pacote:** as copas (Nedbank, MTN 8, Telkom/Carling Knockout), a 2ª divisão e os jogos de acesso.

**Fontes:** RSSSF (páginas por temporada, `data/coleta/rsa-1/rsssf/`: a tabela final de 1971 a 1995, com parte dos jogos em 1987, 1992 e 1993; jogos de 1996/97 a 2024/25, completos desde 1997/98); ogol (jogos de 2005/06 em diante: base de 2025/26, conferência, rodada e data nos outros anos); Wikipédia em inglês (a tabela de cada temporada, terceira fonte). A ESPN não tem a liga.

**Clubes:** o nome pelo qual o clube é conhecido; nome que já existe em outro país leva "(África do Sul)" (Santos, Rangers, Dynamos, Leeds United...); clube refundado com o nome de um antigo, o ano do antigo (Durban City (1959), Cape Town City (1962), Highlands Park (1959)). Mesmo clube com outro nome é um só (Zulu Royals = AmaZulu; Pretoria City = SuperSport United; Ajax Cape Town = Cape Town Spurs). Regras em `coleta/rsa-1/clubes_rsa.py`.

**Regras:** o placar é o da RSSSF (ou do ogol em 2025/26). A classificação é a tabela publicada (ordem oficial e pontos). Pontos 2-1-0 (vitória, empate, derrota) até 1994 e 3-1-0 desde 1995.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Formato |
|---|---|---|---|---|---|---|---|
| 1971 | 13 | 0 (0) | 0 | 0 | 0 / 0 | Orlando Pirates | sem jogos (só a tabela final) |
| 1972 | 1 | 0 (0) | 0 | 0 | 0 / 0 | AmaZulu | sem jogos (só o campeão) |
| 1973 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Orlando Pirates | sem jogos (só o campeão) |
| 1974 | 15 | 0 (0) | 0 | 0 | 0 / 0 | Kaizer Chiefs | sem jogos (só a tabela final) |
| 1975 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Orlando Pirates | sem jogos (só o campeão) |
| 1976 | 15 | 0 (0) | 0 | 0 | 0 / 0 | Orlando Pirates | sem jogos (só a tabela final) |
| 1977 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Kaizer Chiefs | sem jogos (só o campeão) |
| 1978 | 24 | 0 (0) | 0 | 0 | 0 / 0 | Lusitano | sem jogos (só a tabela final) |
| 1979 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Kaizer Chiefs | sem jogos (só a tabela final) |
| 1980 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Highlands Park (1959) | sem jogos (só a tabela final) |
| 1981 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Kaizer Chiefs | sem jogos (só a tabela final) |
| 1982 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Durban City (1959) | sem jogos (só a tabela final) |
| 1983 | 19 | 0 (0) | 0 | 0 | 0 / 0 | Durban City (1959) | sem jogos (só a tabela final) |
| 1984 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Kaizer Chiefs | sem jogos (só a tabela final) |
| 1985 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Durban Bush Bucks | sem jogos (só a tabela final) |
| 1986 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Rangers (África do Sul) | sem jogos (só a tabela final) |
| 1987 | 18 | 196 (196) | 526 | 0 | 0 / 0 | Jomo Cosmos | jogos incompletos (só os resultados que a página traz) |
| 1988 | 17 | 0 (0) | 0 | 0 | 0 / 0 | Mamelodi Sundowns | sem jogos (só a tabela final) |
| 1989 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Kaizer Chiefs | sem jogos (só a tabela final) |
| 1990 | 17 | 0 (0) | 0 | 0 | 0 / 0 | Mamelodi Sundowns | sem jogos (só a tabela final) |
| 1991 | 24 | 0 (0) | 0 | 0 | 0 / 0 | Kaizer Chiefs | sem jogos (só a tabela final) |
| 1992 | 22 | 202 (202) | 487 | 2 | 0 / 0 | Kaizer Chiefs | jogos incompletos (só os resultados que a página traz) |
| 1993 | 20 | 173 (173) | 377 | 2 | 0 / 0 | Mamelodi Sundowns | jogos incompletos (só os resultados que a página traz) |
| 1994 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Orlando Pirates | sem jogos (só a tabela final) |
| 1995 | 17 | 0 (0) | 0 | 0 | 0 / 0 | Cape Town Spurs | sem jogos (só a tabela final) |
| 1996/97 | 18 | 226 (226) | 490 | 0 | 0 / 0 | Manning Rangers | jogos incompletos (só os resultados que a página traz) |
| 1997/98 | 18 | 306 (306) | 736 | 0 | 1 / 0 | Mamelodi Sundowns | pontos corridos |
| 1998/99 | 18 | 306 (306) | 782 | 0 | 1 / 0 | Mamelodi Sundowns | pontos corridos |
| 1999/00 | 18 | 306 (306) | 822 | 0 | 0 / 1 | Mamelodi Sundowns | pontos corridos |
| 2000/01 | 18 | 309 (309) | 725 | 1 | 1 / 0 | Orlando Pirates | pontos corridos |
| 2001/02 | 18 | 306 (306) | 754 | 0 | 1 / 0 | Santos (África do Sul) | pontos corridos |
| 2002/03 | 16 | 240 (240) | 581 | 469 | 1 / 0 | Orlando Pirates | pontos corridos |
| 2003/04 | 16 | 240 (240) | 566 | 448 | 1 / 0 | Kaizer Chiefs | pontos corridos |
| 2004/05 | 16 | 240 (240) | 574 | 483 | 1 / 0 | Kaizer Chiefs | pontos corridos |
| 2005/06 | 16 | 243 (243) | 549 | 547 | 1 / 0 | Mamelodi Sundowns | pontos corridos |
| 2006/07 | 16 | 243 (243) | 524 | 510 | 1 / 0 | Mamelodi Sundowns | pontos corridos |
| 2007/08 | 16 | 241 (241) | 532 | 528 | 1 / 0 | SuperSport United | pontos corridos |
| 2008/09 | 16 | 242 (242) | 569 | 509 | 1 / 0 | SuperSport United | pontos corridos |
| 2009/10 | 16 | 244 (244) | 499 | 496 | 1 / 0 | SuperSport United | pontos corridos |
| 2010/11 | 16 | 240 (240) | 602 | 579 | 1 / 0 | Orlando Pirates | pontos corridos |
| 2011/12 | 16 | 240 (240) | 582 | 0 | 1 / 0 | Orlando Pirates | pontos corridos |
| 2012/13 | 16 | 240 (240) | 546 | 0 | 1 / 0 | Kaizer Chiefs | pontos corridos |
| 2013/14 | 16 | 240 (240) | 528 | 147 | 1 / 0 | Mamelodi Sundowns | pontos corridos |
| 2014/15 | 16 | 240 (240) | 555 | 0 | 1 / 0 | Kaizer Chiefs | pontos corridos |
| 2015/16 | 16 | 240 (240) | 562 | 0 | 1 / 0 | Mamelodi Sundowns | pontos corridos |
| 2016/17 | 16 | 241 (241) | 538 | 0 | 1 / 0 | Wits University | pontos corridos |
| 2017/18 | 16 | 241 (241) | 490 | 0 | 1 / 0 | Mamelodi Sundowns | pontos corridos |
| 2018/19 | 16 | 240 (240) | 543 | 0 | 1 / 0 | Mamelodi Sundowns | pontos corridos |
| 2019/20 | 16 | 240 (240) | 508 | 0 | 1 / 0 | Mamelodi Sundowns | pontos corridos |
| 2020/21 | 16 | 240 (240) | 507 | 0 | 1 / 0 | Mamelodi Sundowns | pontos corridos |
| 2021/22 | 16 | 241 (241) | 479 | 0 | 1 / 0 | Mamelodi Sundowns | pontos corridos |
| 2022/23 | 16 | 240 (240) | 503 | 0 | 1 / 0 | Mamelodi Sundowns | pontos corridos |
| 2023/24 | 16 | 240 (240) | 488 | 0 | 1 / 0 | Mamelodi Sundowns | pontos corridos |
| 2024/25 | 16 | 242 (242) | 423 | 0 | 1 / 0 | Mamelodi Sundowns | pontos corridos |
| 2025/26 | 16 | 240 (240) | 485 | 0 | 1 / 0 | Orlando Pirates | pontos corridos |

## Conferência e correções, edição a edição

### 1971

- a RSSSF só traz a tabela final

### 1972

- a RSSSF só traz o campeão da NPSL (a página do ano é da NFL)

### 1973

- a RSSSF só traz o campeão da NPSL (a página do ano é da NFL)

### 1974

- a RSSSF só traz a tabela final

### 1975

- a RSSSF só traz o campeão da NPSL (a página do ano é da NFL)

### 1976

- a RSSSF só traz a tabela final

### 1977

- a RSSSF só traz o campeão da NPSL (a página do ano é da NFL)

### 1978

- a RSSSF só traz a tabela final

### 1979

- a RSSSF só traz a tabela final

### 1980

- a RSSSF só traz a tabela final

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

- a RSSSF só traz parte dos jogos da temporada; a classificação é a tabela publicada
- jogos incompletos (só os resultados que a página traz)

### 1988

- a RSSSF só traz a tabela final

### 1989

- a RSSSF só traz a tabela final

### 1990

- a RSSSF só traz a tabela final

### 1991

- a RSSSF só traz a tabela final

### 1992

- a RSSSF só traz parte dos jogos da temporada; a classificação é a tabela publicada
- jogos incompletos (só os resultados que a página traz)

### 1993

- a RSSSF só traz parte dos jogos da temporada; a classificação é a tabela publicada
- quatro clubes mudaram de nome no meio da temporada (notas da página): Score Stars = Qwa Qwa Stars, Ratanang = Chatsworth Rangers, Albany City = Pretoria City, Highlands Park = Welkom Eagles
- jogos incompletos (só os resultados que a página traz)

### 1994

- a RSSSF só traz a tabela final

### 1995

- a RSSSF só traz a tabela final

### 1996/97

- a RSSSF só traz parte dos jogos da temporada; a classificação é a tabela publicada
- jogos incompletos (só os resultados que a página traz)

### 1997/98

- sem ocorrências

### 1998/99

- sem ocorrências

### 1999/00

- a lista de jogos da página não fecha com a tabela em seis clubes (a Wikipédia confirma a tabela da RSSSF); nenhum placar foi mudado e o relatório aponta o jogo provável
- tabela publicada x jogos — zaf00:16: Jomo Cosmos tabela [34, 12, 14, 8, 49, 32] jogos [34, 12, 14, 8, 47, 32] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — zaf00:16: SuperSport United tabela [34, 11, 10, 13, 51, 48] jogos [34, 12, 10, 12, 52, 47] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — zaf00:16: Moroka Swallows tabela [34, 11, 9, 14, 39, 52] jogos [34, 10, 9, 15, 38, 53] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — zaf00:16: Free State Stars tabela [34, 9, 13, 12, 29, 38] jogos [34, 8, 14, 12, 29, 39] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — zaf00:16: AmaZulu tabela [34, 9, 9, 16, 32, 44] jogos [34, 9, 10, 15, 33, 44] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — zaf00:16: Mother City tabela [34, 2, 4, 28, 22, 85] jogos [34, 2, 4, 28, 22, 83] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: Jomo Cosmos 2-1 Mother City (2000-04-11, zaf00:243); com 4-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Mother City 1-2 Jomo Cosmos (2000-04-11, zaf00:507); com 1-4 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: SuperSport United 3-2 Moroka Swallows (2000-03-29, zaf00:493); com 2-3 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: AmaZulu 1-1 Free State Stars (1999-08-20, zaf00:95); com 0-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Free State Stars 1-1 AmaZulu (2000-04-30, zaf00:366); com 1-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 2000/01

- abandonado/suspenso, sem valer — Free State Stars Mamelodi Sundowns (2001-02-18): abandoned
- abandonado/suspenso, sem valer — Moroka Swallows Santos (África do Sul) (2001-02-18): abandoned at 0-1 due to thunderstorm
- abandonado/suspenso, sem valer — Kaizer Chiefs Orlando Pirates (2001-04-11): abandoned at 1-1 in 33' following a stadium

### 2001/02

- Ajax Cape Town x Orlando Pirates: abandonado aos 85' com 1-0 e dado ao Ajax Cape Town por 1-0 (nota da página)
- corrigido — Cape Town Spurs x Orlando Pirates (2001-08-12): 1-0 dado ao Ajax Cape Town (nota da página, na linha de baixo)
- decidido fora de campo — Cape Town Spurs Orlando Pirates (2001-08-12): abandonado aos 85' com 1-0 (jogadores do Orlando Pirates agrediram o árbitro); 1-0 dado ao Ajax Cape Town

### 2002/03

- sem ocorrências

### 2003/04

- decidido fora de campo — Manning Rangers SuperSport United (2003-12-05): awarded 0-2

### 2004/05

- sem ocorrências

### 2005/06

- ogol: 240 jogos casados (edição 51062 do ogol, 240 jogos)
- placar diferente no ogol — Free State Stars x Golden Arrows (2005-08-06): RSSSF 2-2, ogol 2-1; fica o da RSSSF
- abandonado/suspenso, sem valer — Free State Stars Dynamos (África do Sul) (2005-11-26): abandoned at 1-0 in 2nd
- abandonado/suspenso, sem valer — Black Leopards Jomo Cosmos (2005-12-07): abandoned at 1-0 at half
- não jogado — Bloemfontein Celtic Cape Town Spurs (2005-12-18): pitch not properly marked

### 2006/07

- ogol: 239 jogos casados (edição 1459 do ogol, 239 jogos)
- data diferente no ogol — Wits University x Bloemfontein Celtic: RSSSF 2006-10-25, ogol 2006-11-03; fica a da RSSSF
- abandonado/suspenso, sem valer — Maritzburg United SuperSport United (2006-09-16): abandoned at half-time
- abandonado/suspenso, sem valer — Wits University Bloemfontein Celtic (2006-10-20): abandoned at 2-1 at 57'
- abandonado/suspenso, sem valer — Orlando Pirates Black Leopards (2007-01-17): abandoned at 0-0 in 1st

### 2007/08

- o Benoni Premier United mudou de nome para Thanda Royal Zulu no meio da temporada: é um clube só
- ogol: 240 jogos casados (edição 1657 do ogol, 240 jogos)
- data diferente no ogol — Thanda Royal Zulu x Mamelodi Sundowns: RSSSF 2007-09-23, ogol 2007-09-30; fica a da RSSSF
- placar diferente no ogol — AmaZulu x Black Leopards (2008-03-01): RSSSF 2-0, ogol 3-0; fica o da RSSSF
- abandonado/suspenso, sem valer — Mamelodi Sundowns Jomo Cosmos (2007-11-23): abandoned due to hail

### 2008/09

- ogol: 239 jogos casados (edição 4371 do ogol, 240 jogos)
- data diferente no ogol — Thanda Royal Zulu x AmaZulu: RSSSF 2009-01-31, ogol 2009-02-04; fica a da RSSSF
- placar diferente no ogol — Moroka Swallows x Platinum Stars (2009-03-15): RSSSF 1-2, ogol 0-0; fica o da RSSSF
- abandonado/suspenso, sem valer — Platinum Stars Santos (África do Sul) (2008-11-05): abandoned at 0-0 in 25' due
- abandonado/suspenso, sem valer — Platinum Stars Golden Arrows (2009-01-31): abandoned in 13' due

### 2009/10

- ogol: 238 jogos casados (edição 8883 do ogol, 240 jogos)
- abandonado/suspenso, sem valer — Kaizer Chiefs AmaZulu (2009-12-02): abandoned at 0-0
- abandonado/suspenso, sem valer — Mamelodi Sundowns Santos (África do Sul) (2009-12-02): abandoned at 1-0
- abandonado/suspenso, sem valer — Mamelodi Sundowns Moroka Swallows (2010-02-17): abandoned at 0-2 in 35'
- abandonado/suspenso, sem valer — Kaizer Chiefs Mpumalanga Black Aces (2010-02-17): abandoned at 1-0 in 35'

### 2010/11

- ogol: 240 jogos casados (edição 16375 do ogol, 240 jogos)

### 2011/12

- ogol: 240 jogos casados (edição 24862 do ogol, 240 jogos)
- data diferente no ogol — Bloemfontein Celtic x Orlando Pirates: RSSSF 2011-12-08, ogol 2011-12-18; fica a da RSSSF
- data diferente no ogol — Black Leopards x Wits University: RSSSF 2011-12-08, ogol 2011-12-18; fica a da RSSSF

### 2012/13

- ogol: 240 jogos casados (edição 48259 do ogol, 240 jogos)

### 2013/14

- ogol: 240 jogos casados (edição 59557 do ogol, 240 jogos)
- data diferente no ogol — Bloemfontein Celtic x Mpumalanga Black Aces: RSSSF 2014-03-02, ogol 2014-03-12; fica a da RSSSF

### 2014/15

- ogol: 240 jogos casados (edição 70382 do ogol, 240 jogos)

### 2015/16

- ogol: 240 jogos casados (edição 88444 do ogol, 240 jogos)

### 2016/17

- ogol: 238 jogos casados (edição 99140 do ogol, 240 jogos)
- data diferente no ogol — Free State Stars x Highlands Park: RSSSF 2017-03-05, ogol 2017-03-11; fica a da RSSSF
- data diferente no ogol — Golden Arrows x Maritzburg United: RSSSF 2017-03-04, ogol 2017-03-12; fica a da RSSSF
- data diferente no ogol — Free State Stars x Orlando Pirates: RSSSF 2017-04-01, ogol 2017-04-08; fica a da RSSSF
- abandonado/suspenso, sem valer — Mamelodi Sundowns Chippa United (2017-02-28): abandoned at 0-0 in 43' due to power failure

### 2017/18

- ogol: 239 jogos casados (edição 112598 do ogol, 240 jogos)
- data diferente no ogol — SuperSport United x Mamelodi Sundowns: RSSSF 2017-08-29, ogol 2017-08-19; fica a da RSSSF
- data diferente no ogol — Polokwane City x Baroka: RSSSF 2017-08-29, ogol 2017-08-19; fica a da RSSSF
- data diferente no ogol — AmaZulu x Free State Stars: RSSSF 2017-08-29, ogol 2017-08-19; fica a da RSSSF
- data diferente no ogol — Orlando Pirates x Chippa United: RSSSF 2017-08-29, ogol 2017-08-19; fica a da RSSSF
- data diferente no ogol — Cape Town Spurs x Golden Arrows: RSSSF 2017-08-29, ogol 2017-08-19; fica a da RSSSF
- abandonado/suspenso, sem valer — AmaZulu Bloemfontein Celtic (2017-12-06): abandoned at 0-0 in 15' due
- decidido fora de campo — Cape Town Spurs Platinum Stars (2018-01-12): awarded 0-3, originally 3-1; Ajax
- decidido fora de campo — Polokwane City Cape Town Spurs (2018-02-04): awarded 3-0, originally 1-1; Ajax
- decidido fora de campo — Cape Town Spurs SuperSport United (2018-02-28): awarded 0-3, originally 2-0; Ajax

### 2018/19

- ogol: 240 jogos casados (edição 125698 do ogol, 240 jogos)
- placar diferente no ogol — SuperSport United x Highlands Park (2019-05-11): RSSSF 0-2, ogol 0-1; fica o da RSSSF
- decidido fora de campo — Bloemfontein Celtic Cape Town City (2019-04-14): awarded 0-3; abandoned at 0-0 in 23'

### 2019/20

- ogol: 186 jogos casados (edição 135804 do ogol, 240 jogos)

### 2020/21

- ogol: 240 jogos casados (edição 148563 do ogol, 240 jogos)

### 2021/22

- ogol: 232 jogos casados (edição 156785 do ogol, 240 jogos)
- abandonado/suspenso, sem valer — AmaZulu Marumo Gallants (2021-11-03): abandoned at 0-0 in 9' due

### 2022/23

- ogol: 239 jogos casados (edição 166475 do ogol, 240 jogos)

### 2023/24

- ogol: 239 jogos casados (edição 176017 do ogol, 240 jogos)
- placar diferente no ogol — Royal AM x Polokwane City (2024-04-07): RSSSF 3-2, ogol 3-1; fica o da RSSSF
- decidido fora de campo — Mamelodi Sundowns Moroka Swallows (2023-12-27): awarded 3-0
- decidido fora de campo — Moroka Swallows Golden Arrows (2023-12-30): awarded 0-3

### 2024/25

- o Royal AM foi excluído e todos os seus resultados anulados; o Cape Town City perdeu o desempate de acesso
- ogol: 234 jogos casados (edição 189081 do ogol, 240 jogos)
- jogos do Royal AM anulados: Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- tabela zaf2025:42 fora da conferência: campanha do Royal AM até a exclusão (resultados anulados), não é tabela da edição
- tabela zaf2025:473 fora da conferência: campanha do Royal AM até a exclusão (repetida no fim da página)
- anulado — Royal AM 1-1 Cape Town City (2024-09-14): annulled; Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — SuperSport United 0-0 Royal AM (2024-09-21): annulled; Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Royal AM 0-0 Richards Bay (2024-09-24): annulled; Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Magesi 0-0 Royal AM (2024-09-28): annulled; Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Royal AM 2-0 Sekhukhune United (2024-10-26): annulled; Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Royal AM 0-1 Polokwane City (2024-10-30): annulled; Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Royal AM 2-3 Golden Arrows (2024-11-26): annulled; Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Kaizer Chiefs 2-2 Royal AM (2024-11-30): annulled; Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Stellenbosch Royal AM (2025-05-13): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — AmaZulu 2-1 Royal AM (2024-12-13): annulled; Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Royal AM 1-3 TS Galaxy (2024-12-29): annulled; Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Mamelodi Sundowns 2-1 Royal AM (2024-10-23): annulled; Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Chippa United Royal AM (2025-01-12): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Royal AM Orlando Pirates (2025-01-23): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Marumo Gallants Royal AM (2025-02-02): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- abandonado/suspenso, sem valer — Magesi Chippa United (2025-02-04): abandoned at 1-1 in 21' due to power cut
- anulado — Royal AM Stellenbosch (2025-02-05): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Golden Arrows Royal AM (2025-02-09): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Richards Bay Royal AM (2025-05-06): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- abandonado/suspenso, sem valer — SuperSport United Golden Arrows (2025-02-23): abandoned at 1-1 at half-time due to
- anulado — Royal AM Kaizer Chiefs (2025-02-23): load shedding]; Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Sekhukhune United Royal AM (2025-03-02): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Polokwane City Royal AM (2025-03-05): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Royal AM Chippa United (2025-03-12): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Royal AM SuperSport United (2025-03-16): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Orlando Pirates Royal AM (2025-03-30): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Royal AM Magesi (2025-05-11): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Royal AM Mamelodi Sundowns (2025-05-20): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Cape Town City Royal AM (2025-05-28): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Royal AM Marumo Gallants (2025-05-04): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — Royal AM AmaZulu (2025-05-18): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")
- anulado — TS Galaxy Royal AM (2025-05-24): Royal AM excluído do campeonato; todos os seus resultados anulados ("excluded; all results annulled")

### 2025/26

- os jogos vêm do calendário do ogol (a RSSSF só traz a tabela)
- ogol: base dos jogos (240 jogos)

