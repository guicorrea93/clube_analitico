# Campeonato Nigeriano (1ª divisão) — coleta de dados

Gerado por `python coleta/nga-1/importar.py`. Pacote em `data/coleta/nga-1/pacote/`.

**Edições:** 55, de 1972 a 2025/26, como a lista de campeões da RSSSF (`nigchamp.html`), sem a Amachree Gold Cup de 1971 (torneio anterior à liga, que a liga e a imprensa não contam: o título de 2025/26 foi o "9º" do Enugu Rangers). Pesquisa de 24/11/2026, aprovada pelo Guilherme. 2018 e 2019/20 foram abandonados e entram sem campeão.

**Fora do pacote:** a Federation Cup e as outras copas, as ligas regionais, a 2ª divisão e os jogos de acesso.

**Fontes:** RSSSF (páginas por ano, `data/coleta/nga-1/rsssf/`: a tabela final de 1972 e de 1989 a 1997; só o campeão nos outros anos até 1988; jogos de 1998 em diante, parte da temporada até 2003 e em 2007/08); ogol (jogos de 2008/09 em diante, com os mesmos placares da RSSSF: base de 2009/10 a 2011/12, conferência, rodada e data nos outros); Wikipédia em inglês (a tabela de cada temporada desde 2009/10). A ESPN não tem a liga.

**Clubes:** o nome pelo qual o clube é conhecido (Enugu Rangers, Enyimba, Kano Pillars, Shooting Stars...). Mesmo clube com outro nome é um só (Iwuanyanwu Nationale = Heartland; Eagle Cement = Dolphin; Gabros = Ifeanyi Ubah; NPA = Nigerian Ports Authority). Regras em `coleta/nga-1/clubes_nga.py`.

**Regras:** o placar é o da RSSSF (ou do ogol de 2009/10 a 2011/12). A classificação é a tabela publicada (ordem oficial e pontos, com as punições). Pontos 2-1-0 (vitória, empate, derrota) até 1989; de 1990 a 1994, 3 por vitória, 2 por empate com gols e 1 por empate sem gols (o ponto a mais vai no `ajuste_pontos`); 3-1-0 desde 1995.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Formato |
|---|---|---|---|---|---|---|---|
| 1972 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Mighty Jets | sem jogos (só a tabela final) |
| 1973 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Bendel Insurance | sem jogos (só o campeão) |
| 1974 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Enugu Rangers | sem jogos (só o campeão) |
| 1975 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Enugu Rangers | sem jogos (só o campeão) |
| 1976 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Shooting Stars | sem jogos (só o campeão) |
| 1977 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Enugu Rangers | sem jogos (só o campeão) |
| 1978 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Racca Rovers | sem jogos (só o campeão) |
| 1979 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Bendel Insurance | sem jogos (só o campeão) |
| 1980 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Shooting Stars | sem jogos (só o campeão) |
| 1981 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Enugu Rangers | sem jogos (só o campeão) |
| 1982 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Enugu Rangers | sem jogos (só o campeão) |
| 1983 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Shooting Stars | sem jogos (só o campeão) |
| 1984 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Enugu Rangers | sem jogos (só o campeão) |
| 1985 | 0 | 0 (0) | 0 | 0 | 0 / 0 | — | sem jogos (só o campeão) |
| 1986 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Leventis United | sem jogos (só o campeão) |
| 1987 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Heartland | sem jogos (só o campeão) |
| 1988 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Heartland | sem jogos (só o campeão) |
| 1989 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Heartland | sem jogos (só a tabela final) |
| 1990 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Heartland | sem jogos (só o campeão) |
| 1991 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Julius Berger | sem jogos (só a tabela final) |
| 1992 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Stationery Stores | sem jogos (só a tabela final) |
| 1993 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Heartland | sem jogos (só a tabela final) |
| 1994 | 17 | 0 (0) | 0 | 0 | 0 / 0 | BCC Lions | sem jogos (só a tabela final) |
| 1995 | 15 | 0 (0) | 0 | 0 | 0 / 0 | — | sem jogos (só a tabela final) |
| 1996 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Udoji United | sem jogos (só a tabela final) |
| 1997 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Dolphin | sem jogos (só a tabela final) |
| 1998 | 20 | 116 (116) | 250 | 0 | 0 / 0 | — | jogos incompletos (só os resultados que a página traz) |
| 1999 | 18 | 186 (186) | 341 | 0 | 0 / 0 | Lobi Stars | jogos incompletos (só os resultados que a página traz) |
| 2000 | 17 | 210 (210) | 393 | 4 | 0 / 0 | Julius Berger | jogos incompletos (só os resultados que a página traz) |
| 2001 | 17 | 251 (251) | 488 | 0 | 0 / 0 | Enyimba | jogos incompletos (só os resultados que a página traz) |
| 2002 | 18 | 272 (272) | 533 | 0 | 0 / 0 | Enyimba | jogos incompletos (só os resultados que a página traz) |
| 2003 | 18 | 155 (155) | 270 | 0 | 0 / 0 | Enyimba | jogos incompletos (só os resultados que a página traz) |
| 2004 | 18 | 306 (306) | 613 | 57 | 1 / 0 | Dolphin | pontos corridos |
| 2005 | 20 | 389 (389) | 755 | 0 | 1 / 0 | Enyimba | pontos corridos |
| 2006 | 20 | 187 (187) | 379 | 0 | 3 / 0 | Ocean Boys | 2 grupos + fase final |
| 2007 | 20 | 188 (188) | 343 | 12 | 3 / 0 | Enyimba | 2 grupos + fase final |
| 2007/08 | 20 | 363 (363) | 687 | 0 | 0 / 0 | Kano Pillars | jogos incompletos (só os resultados que a página traz) |
| 2008/09 | 20 | 381 (381) | 702 | 0 | 1 / 0 | Bayelsa United | pontos corridos |
| 2009/10 | 20 | 380 (380) | 751 | 0 | 0 / 1 | Enyimba | pontos corridos |
| 2010/11 | 20 | 380 (380) | 778 | 0 | 0 / 1 | Dolphin | pontos corridos |
| 2011/12 | 20 | 380 (380) | 751 | 0 | 0 / 1 | Kano Pillars | pontos corridos |
| 2013 | 20 | 383 (383) | 764 | 0 | 1 / 0 | Kano Pillars | pontos corridos |
| 2014 | 20 | 380 (380) | 836 | 0 | 1 / 0 | Kano Pillars | pontos corridos |
| 2015 | 20 | 383 (383) | 817 | 0 | 1 / 0 | Enyimba | pontos corridos |
| 2016 | 20 | 363 (363) | 735 | 0 | 1 / 0 | Enugu Rangers | pontos corridos |
| 2017 | 20 | 382 (382) | 764 | 0 | 1 / 0 | Plateau United | pontos corridos |
| 2018 | 20 | 240 (240) | 445 | 0 | 1 / 0 | — | temporada não terminada |
| 2019 | 25 | 280 (280) | 543 | 0 | 2 / 1 | Enyimba | 2 grupos + fase final |
| 2019/20 | 22 | 246 (246) | 494 | 0 | 0 / 0 | — | temporada não terminada (jogos incompletos (só os resultados que a página traz)) |
| 2020/21 | 20 | 380 (380) | 791 | 0 | 1 / 0 | Akwa United | pontos corridos |
| 2021/22 | 20 | 382 (382) | 779 | 0 | 1 / 0 | Rivers United | pontos corridos |
| 2023 | 20 | 197 (197) | 411 | 0 | 2 / 1 | Enyimba | 2 grupos + fase final |
| 2023/24 | 20 | 381 (381) | 851 | 0 | 0 / 1 | Enugu Rangers | pontos corridos |
| 2024/25 | 20 | 382 (382) | 784 | 0 | 0 / 1 | Remo Stars | pontos corridos |
| 2025/26 | 20 | 383 (383) | 772 | 0 | 0 / 1 | Enugu Rangers | pontos corridos |

## Conferência e correções, edição a edição

### 1972

- a RSSSF só traz a tabela final

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

- a RSSSF só traz o campeão (sem página do ano)

### 1981

- a RSSSF só traz o campeão (sem página do ano)

### 1982

- a RSSSF só traz o campeão (sem página do ano)

### 1983

- a RSSSF só traz o campeão

### 1984

- a RSSSF só traz o campeão

### 1985

- a RSSSF só traz o campeão
- clube da lista de campeões da RSSSF não reconhecido: New Nigeria Bank

### 1986

- a RSSSF só traz o campeão

### 1987

- a RSSSF só traz o campeão

### 1988

- a RSSSF só traz o campeão

### 1989

- a RSSSF só traz a tabela final

### 1990

- a RSSSF só traz o campeão (e a lista dos participantes)

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
- clube da lista de campeões da RSSSF não reconhecido: 3SC Shooting Stars

### 1996

- a RSSSF só traz a tabela final

### 1997

- a RSSSF só traz a tabela final

### 1998

- jogos incompletos (só os resultados que a página traz)
- clube da lista de campeões da RSSSF não reconhecido: 3SC Shooting Stars

### 1999

- jogos incompletos (só os resultados que a página traz)
- decidido fora de campo — Shooting Stars Enyimba (1999-02-10): awarded 0-3
- W.O./pontos para o mandante — Shooting Stars Plateau United (1999-03-03): bt
- abandonado/suspenso, sem valer — Gombe United Julius Berger (1999-03-17): abd at 1-1
- decidido fora de campo — Enugu Rangers Katsina United (s/d): awarded 3-0
- decidido fora de campo — Plateau United Katsina United (1999-07-24): awarded 3-0

### 2000

- jogos incompletos (só os resultados que a página traz)
- decidido fora de campo — Enyimba 0-3 Julius Berger (2000-05-27): awarded; originally 0-0
- decidido fora de campo — Ifeanyi Ubah Plateau United (2000-06-14): awarded 0-3; originally 0-0 on June 7; Ejide Austin

### 2001

- jogos incompletos (só os resultados que a página traz)
- decidido fora de campo — Jasper United 1-0 El-Kanemi Warriors (2001-02-18): awarded, 0-3?
- decidido fora de campo — Plateau United El-Kanemi Warriors (2001-02-03): temporarily awarded 0-3; originally 2-0
- não jogado — Ifeanyi Ubah El-Kanemi Warriors (2001-03-11): annulled; finished 1-0
- decidido fora de campo — Ifeanyi Ubah Heartland (2001-04-12): abandoned at 1-1; apparently awarded 3-0 to Gabros
- W.O./pontos para o mandante — Nigerian Ports Authority Julius Berger (2001-04-18): bt
- decidido fora de campo — Jasper United Enyimba (2001-05-06): awarded 0-3 (inferred); abandoned at 0-1
- W.O./pontos para o mandante — Plateau United Ifeanyi Ubah (2001-06-02): bt
- decidido fora de campo — Ifeanyi Ubah Katsina United (2001-06-10): awarded 3-0; Katsina dns
- W.O./pontos para o mandante — Plateau United Jasper United (2001-06-17): bt

### 2002

- jogos incompletos (só os resultados que a página traz)
- abandonado/suspenso, sem valer — Heartland Lobi Stars (2002-03-16): abandoned at 1-0 in 65' after referee was
- abandonado/suspenso, sem valer — Wikki Tourists Gombe United (2002-03-24): abandoned at 0-0 in 75'
- abandonado/suspenso, sem valer — Jigawa Golden Stars Kano Pillars (2002-06-30): abandoned at 0-0
- decidido fora de campo — Lobi Stars Enyimba (2002-06-30): awarded 0-3? to Enyimba; originally 1-0 but
- decidido fora de campo — Sharks Gombe United (2002-07-03): abandoned at 2-0 in 30' when Gombe withdrew
- decidido fora de campo — Nigerian Ports Authority 1-1 Enyimba (2002-07-03): in protest to refereeing, awarded 3-0?]
- W.O./pontos para o mandante — Julius Berger Plateau United (2002-07-03): bt
- W.O./pontos para o mandante — Julius Berger Ifeanyi Ubah (2002-07-30): bt
- W.O./pontos para o mandante — El-Kanemi Warriors Plateau United (2002-07-30): bt
- W.O./pontos para o mandante — Wikki Tourists Sharks (2002-07-14): bt
- W.O./pontos para o mandante — El-Kanemi Warriors Wikki Tourists (2002-07-28): bt
- W.O./pontos para o mandante — Enyimba Julius Berger (2002-07-31): bt

### 2003

- jogos incompletos (só os resultados que a página traz)
- abandonado/suspenso, sem valer — Enyimba Delta United (2003-03-02): 1-0 abd due rain at 60'; to replay
- decidido fora de campo — Dolphin Lobi Stars (2003-03-02): awarded 3-0, Lobi walked off in 70'
- abandonado/suspenso, sem valer — Kano Pillars Lobi Stars (2003-03-12): abandoned at 2-1 in 70' after police fired

### 2004

- decidido fora de campo — Julius Berger Kano Pillars (2004-06-23): awarded 0-3
- decidido fora de campo — El-Kanemi Warriors Wikki Tourists (2004-06-05): awarded 0-3; abandoned at 1-1 around 75' when
- decidido fora de campo — Gombe United Plateau United (2004-06-20): awarded 3-0; abandoned at 0-1 the appeal committee of NFA have awarded Gombe United the match 3-0
- decidido fora de campo — Bendel Insurance El-Kanemi Warriors (2004-06-26): awarded 3-0; originally abandoned at
- decidido fora de campo — Niger Tornadoes Mighty Jets (2004-06-27): awarded 3-0; Jets dns
- decidido fora de campo — Bendel Insurance Kwara United (2004-07-24): awarded 3-0; abandoned at 2-0
- decidido fora de campo — Mighty Jets Bendel Insurance (2004-08-29): awarded 0-3; Jets refused to play its home game

### 2005

- a rodada 20 de julho foi anulada e jogada de novo em novembro; Gateway x Sharks de setembro (0-2 dado e depois revogado) foi repetido em novembro
- corrigido — Kwara United x Bendel Insurance (2005-07-16): a rodada 20 de julho foi anulada e jogada de novo em novembro ("Replay Round 20"); vale o jogo de novembro
- corrigido — Nigerian Ports Authority x Julius Berger (2005-07-16): a rodada 20 de julho foi anulada e jogada de novo em novembro ("Replay Round 20"); vale o jogo de novembro
- corrigido — Shooting Stars x Kano Pillars (2005-07-16): a rodada 20 de julho foi anulada e jogada de novo em novembro ("Replay Round 20"); vale o jogo de novembro
- corrigido — Gateway x El-Kanemi Warriors (2005-07-16): a rodada 20 de julho foi anulada e jogada de novo em novembro ("Replay Round 20"); vale o jogo de novembro
- corrigido — Zamfara United x Nasarawa United (2005-07-16): a rodada 20 de julho foi anulada e jogada de novo em novembro ("Replay Round 20"); vale o jogo de novembro
- corrigido — Ifeanyi Ubah x Wikki Tourists (2005-07-17): a rodada 20 de julho foi anulada e jogada de novo em novembro ("Replay Round 20"); vale o jogo de novembro
- corrigido — Lobi Stars x Heartland (2005-07-17): a rodada 20 de julho foi anulada e jogada de novo em novembro ("Replay Round 20"); vale o jogo de novembro
- corrigido — Gateway x Sharks (2005-09-03): o 0-2 dado foi revogado ("later revoked") e o jogo repetido em 16/11
- decidido fora de campo — Bendel Insurance Gateway (2005-05-22): awarded 0-3; originally 1-1
- abandonado/suspenso, sem valer — Niger Tornadoes Julius Berger (2005-05-28): abd at 1-1
- anulado — Kwara United 1-1 Bendel Insurance (2005-07-16)
- anulado — Nigerian Ports Authority 3-1 Julius Berger (2005-07-16)
- anulado — Shooting Stars 1-0 Kano Pillars (2005-07-16)
- anulado — Gateway 1-0 El-Kanemi Warriors (2005-07-16)
- anulado — Zamfara United 2-1 Nasarawa United (2005-07-16)
- anulado — Ifeanyi Ubah 0-0 Wikki Tourists (2005-07-17)
- anulado — Lobi Stars 1-1 Heartland (2005-07-17)
- decidido fora de campo — Gombe United Enyimba (2005-11-20): awarded 3-0; Enyimba walkover
- decidido fora de campo — Kwara United Bendel Insurance (2005-11-23): awarded 0-3; Kwara walkover
- abandonado/suspenso, sem valer — Gateway Sharks (2005-09-03): abandonado com 1-1 (os oficiais foram ameaçados com uma arma); o 0-2 dado ao Sharks foi revogado e o jogo, repetido em 16/11 (0-4)
- decidido fora de campo — Enyimba Ifeanyi Ubah (2005-12-18): awarded 3-0; Gabros walkover

### 2006

- corrigido — Ranchers Bees x Kano Pillars (2006-08-13): "n/p" na página, mas com "awarded 0-3; Ranchers Bees dns": o resultado dado vale
- decidido fora de campo — Ranchers Bees Kano Pillars (2006-08-13): 0-3 dado ao Kano Pillars: o Ranchers Bees não compareceu
- não jogado — Gombe United Sharks (2006-08-17): awarded 3-0; Sharks dns; later revoked

### 2007

- decidido fora de campo — Niger Tornadoes Kwara United (2007-04-28): awarded 0-3; abandoned at 1-2 in 80'
- abandonado/suspenso, sem valer — Akwa United Enyimba (2007-03-25): abandoned at 2-1 due to crowd trouble,
- abandonado/suspenso, sem valer — Akwa United Enyimba (2007-03-25): abandoned after 30' due to torrential rain May 14, replay; jogo repetido (o primeiro foi suspenso)
- decidido fora de campo — Enyimba El-Kanemi Warriors (2007-05-16): awarded 3-0, El-Kanemi dns

### 2007/08

- jogos incompletos (só os resultados que a página traz)
- decidido fora de campo — Bendel Insurance Heartland (2007-09-23): awarded 0-3
- não jogado — Wikki Tourists Nasarawa United (2007-10-06)
- decidido fora de campo — Lobi Stars Zamfara United (2007-10-07): awarded 3-0, Zamfara dns
- decidido fora de campo — Ocean Boys Prime (2007-10-08): awarded 3-0, Prime dns
- decidido fora de campo — Heartland Enyimba (2007-10-24): awarded 0-3; originally 1-1
- decidido fora de campo — JUTH Lobi Stars (2007-10-27): awarded 3-0; abandoned at 2-0
- abandonado/suspenso, sem valer — Gombe United Jigawa Golden Stars (2008-04-09): abandoned at 1-0; replay
- decidido fora de campo — Heartland Bendel Insurance (2008-03-12): awarded 3-0, originally 1-0
- decidido fora de campo — Sunshine Stars Sharks (2008-04-05): awarded 3-0; originally 0-0,
- decidido fora de campo — Kwara United Niger Tornadoes (2008-04-19): awarded 3-0, Tornadoes walked May 15]                                          off at 1-1; later replay ordered

### 2008/09

- ogol: 368 jogos casados (edição 4392 do ogol, 380 jogos)
- data diferente no ogol — Warri Wolves x Kano Pillars: RSSSF 2009-05-13, ogol 2009-05-07; fica a da RSSSF
- decidido fora de campo — Nasarawa United Bayelsa United (2008-12-14): awarded 0-3; abandoned at
- decidido fora de campo — Lobi Stars Enugu Rangers (2009-02-15): awarded 3-0, originally 1-1;
- decidido fora de campo — Lobi Stars Sunshine Stars (2009-03-08): awarded 3-0; originally 1-1
- anulado — Kano Pillars 0-0 Ocean Boys (2009-03-28): annulled?!

### 2009/10

- os jogos vêm do ogol e não fecham com a tabela da RSSSF (que a Wikipédia confirma) em vários clubes: o ogol deve trazer o placar de campo de jogos que a liga decidiu de outro jeito; nenhum placar foi mudado e a classificação é a tabela publicada
- os jogos vêm do calendário do ogol (a RSSSF só traz a tabela)
- ogol: base dos jogos (380 jogos)
- tabela publicada x jogos — nig2010:26: Niger Tornadoes tabela [38, 16, 7, 15, 42, 38] jogos [38, 17, 7, 14, 43, 37] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2010:26: Dolphin tabela [38, 13, 12, 13, 39, 39] jogos [38, 13, 12, 13, 39, 38] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2010:26: Ocean Boys tabela [38, 14, 8, 16, 32, 36] jogos [38, 13, 8, 17, 30, 37] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2010:26: Wikki Tourists tabela [38, 13, 8, 17, 40, 38] jogos [38, 13, 8, 17, 39, 38] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2010:26: Bayelsa United tabela [38, 13, 8, 17, 40, 46] jogos [38, 13, 8, 17, 40, 45] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: Wikki Tourists 2-0 Bayelsa United (2010-05-16, ogol:1029630); com 3-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 2010/11

- os jogos vêm do ogol e não fecham com a tabela da RSSSF (que a Wikipédia confirma) em vários clubes: o ogol deve trazer o placar de campo de jogos que a liga decidiu de outro jeito; nenhum placar foi mudado e a classificação é a tabela publicada
- os jogos vêm do calendário do ogol (a RSSSF só traz parte deles)
- ogol: base dos jogos (380 jogos)
- tabela publicada x jogos — nig2011:24: Dolphin tabela [38, 23, 4, 11, 49, 30] jogos [38, 23, 5, 10, 49, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2011:24: Sunshine Stars tabela [38, 22, 5, 11, 55, 35] jogos [38, 22, 6, 10, 55, 35] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2011:24: Warri Wolves tabela [38, 19, 9, 10, 44, 29] jogos [38, 19, 9, 10, 43, 28] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2011:24: Sharks tabela [38, 17, 12, 9, 43, 37] jogos [38, 17, 12, 9, 42, 37] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2011:24: Enugu Rangers tabela [38, 19, 5, 14, 47, 30] jogos [38, 19, 6, 13, 46, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2011:24: Kaduna United tabela [38, 16, 8, 14, 42, 40] jogos [38, 16, 8, 14, 42, 39] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2011:24: Kwara United tabela [38, 16, 5, 17, 40, 45] jogos [38, 15, 6, 17, 39, 45] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2011:24: Lobi Stars tabela [38, 15, 8, 15, 34, 40] jogos [38, 15, 7, 16, 33, 42] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2011:24: Heartland tabela [38, 16, 4, 18, 39, 35] jogos [38, 16, 5, 17, 38, 34] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2011:24: ABS tabela [38, 15, 6, 17, 35, 37] jogos [38, 16, 6, 16, 35, 35] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2011:24: Gombe United tabela [38, 14, 8, 16, 34, 37] jogos [38, 13, 9, 16, 33, 37] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2011:24: Niger Tornadoes tabela [38, 13, 11, 14, 35, 43] jogos [38, 12, 12, 14, 34, 43] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2011:24: Ocean Boys tabela [38, 13, 8, 17, 37, 44] jogos [38, 14, 8, 16, 39, 41] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2011:24: Plateau United tabela [38, 12, 8, 18, 42, 49] jogos [38, 11, 9, 18, 42, 49] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2011:24: Zamfara United tabela [38, 11, 6, 21, 26, 58] jogos [38, 10, 7, 21, 25, 58] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2011:24: JUTH tabela [38, 8, 8, 22, 26, 51] jogos [38, 8, 6, 24, 25, 51] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: Sharks 1-0 Dolphin (2010-11-20, ogol:1539089); com 2-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Kwara United 1-1 Dolphin (2011-06-18, ogol:1539335); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Niger Tornadoes 0-0 Dolphin (2010-12-04, ogol:1539105); com 1-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Warri Wolves 1-0 Enugu Rangers (2011-07-27, ogol:1539398); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Warri Wolves 2-2 Heartland (2010-11-21, ogol:1539090); com 3-3 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Sharks 2-1 Kaduna United (2011-02-12, ogol:1539216); com 3-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Kwara United 1-1 Kaduna United (2010-11-13, ogol:1539076); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Kaduna United 3-0 Kwara United (2011-05-18, ogol:1539281); com 3-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Kaduna United 3-0 Gombe United (2011-02-20, ogol:1539231); com 3-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Niger Tornadoes 0-0 Kaduna United (2011-02-26, ogol:1539240); com 1-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Kaduna United 3-1 Niger Tornadoes (2011-07-05, ogol:1539434); com 3-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Kaduna United 2-0 Zamfara United (2011-07-03, ogol:1539362); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 2011/12

- os jogos vêm do ogol e não fecham com a tabela da RSSSF (que a Wikipédia confirma) em vários clubes: o ogol deve trazer o placar de campo de jogos que a liga decidiu de outro jeito; nenhum placar foi mudado e a classificação é a tabela publicada
- os jogos vêm do calendário do ogol (a RSSSF só traz a tabela)
- ogol: base dos jogos (380 jogos)
- tabela publicada x jogos — nig2012:22: Kano Pillars tabela [36, 17, 10, 9, 45, 26] jogos [36, 18, 7, 11, 40, 25] — a Wikipédia traz [36, 17, 10, 9, 46, 26]
- tabela publicada x jogos — nig2012:22: Enugu Rangers tabela [36, 17, 7, 12, 45, 27] jogos [36, 17, 6, 13, 43, 25] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2012:22: Lobi Stars tabela [36, 18, 3, 15, 38, 30] jogos [36, 19, 2, 15, 36, 28] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2012:22: Enyimba tabela [36, 16, 6, 14, 37, 28] jogos [36, 15, 6, 15, 35, 29] — a Wikipédia traz [36, 16, 6, 14, 38, 30]
- tabela publicada x jogos — nig2012:22: Sunshine Stars tabela [36, 15, 7, 14, 41, 35] jogos [36, 14, 8, 14, 37, 32] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2012:22: Kwara United tabela [36, 16, 4, 16, 35, 36] jogos [36, 16, 4, 16, 33, 32] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2012:22: Sharks tabela [36, 16, 4, 16, 43, 46] jogos [36, 17, 3, 16, 40, 43] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2012:22: Heartland tabela [36, 14, 9, 13, 32, 31] jogos [36, 15, 5, 16, 27, 27] — a Wikipédia traz [36, 14, 9, 13, 32, 30]
- tabela publicada x jogos — nig2012:22: Gombe United tabela [36, 15, 6, 15, 38, 43] jogos [36, 16, 6, 14, 36, 39] — a Wikipédia traz [36, 15, 6, 15, 40, 45]
- tabela publicada x jogos — nig2012:22: Wikki Tourists tabela [36, 16, 3, 17, 34, 46] jogos [36, 16, 3, 17, 32, 42] — a Wikipédia traz [36, 16, 3, 17, 33, 46]
- tabela publicada x jogos — nig2012:22: Dolphin tabela [36, 15, 5, 16, 38, 40] jogos [36, 16, 3, 17, 36, 36] — a Wikipédia traz [36, 15, 5, 16, 37, 39]
- tabela publicada x jogos — nig2012:22: Akwa United tabela [36, 15, 5, 16, 30, 34] jogos [36, 14, 6, 16, 26, 30] — a Wikipédia traz [36, 15, 5, 16, 27, 31]
- tabela publicada x jogos — nig2012:22: Shooting Stars tabela [36, 14, 7, 15, 30, 33] jogos [36, 16, 4, 16, 29, 31] — a Wikipédia traz [36, 14, 7, 15, 31, 34]
- tabela publicada x jogos — nig2012:22: Kaduna United tabela [36, 15, 4, 17, 38, 43] jogos [36, 16, 5, 15, 35, 38] — a Wikipédia traz [36, 15, 4, 17, 37, 42]
- tabela publicada x jogos — nig2012:22: ABS tabela [36, 14, 6, 16, 43, 40] jogos [36, 14, 4, 18, 38, 38] — a Wikipédia traz [36, 14, 6, 16, 42, 40]
- tabela publicada x jogos — nig2012:22: Warri Wolves tabela [36, 13, 9, 14, 32, 30] jogos [36, 14, 6, 16, 29, 27] — a Wikipédia traz [36, 13, 9, 14, 32, 29]
- tabela publicada x jogos — nig2012:22: Niger Tornadoes tabela [36, 14, 6, 16, 39, 43] jogos [36, 16, 3, 17, 35, 40] — a Wikipédia traz [36, 14, 6, 16, 38, 42]
- tabela publicada x jogos — nig2012:22: Jigawa Golden Stars tabela [36, 14, 6, 16, 30, 43] jogos [36, 14, 6, 16, 28, 42] — a Wikipédia traz [36, 14, 6, 16, 29, 42]
- tabela publicada x jogos — nig2012:22: Rising Stars tabela [36, 10, 9, 17, 23, 37] jogos [36, 11, 9, 16, 22, 33] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: Jigawa Golden Stars 2-0 Shooting Stars (2012-07-11, ogol:2196832); com 4-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 2013

- ogol: 380 jogos casados (edição 55403 do ogol, 380 jogos)
- placar diferente no ogol — Heartland x Kaduna United (2013-03-24): RSSSF 4-1, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — El-Kanemi Warriors x Sharks (2013-05-23): RSSSF 2-1, ogol 2-0; fica o da RSSSF
- data diferente no ogol — Kwara United x Warri Wolves: RSSSF 2013-09-01, ogol 2013-09-05; fica a da RSSSF
- data diferente no ogol — Nasarawa United x Bayelsa United: RSSSF 2013-09-18, ogol 2013-09-12; fica a da RSSSF
- abandonado/suspenso, sem valer — Kano Pillars Heartland (2013-04-24): abandoned at 0-0 in 28' due
- decidido fora de campo — Wikki Tourists Enugu Rangers (2013-05-09): awarded 3-0, Rangers dns
- abandonado/suspenso, sem valer — Akwa United Warri Wolves (2013-06-05): abandoned at 2-0 in 45' after
- decidido fora de campo — Wikki Tourists El-Kanemi Warriors (2013-07-21): awarded 0-3; abandoned at 0-1 in 85'
- decidido fora de campo — Kwara United Warri Wolves (2013-09-01): awarded 0-3; abandoned at 0-0
- decidido fora de campo — Sunshine Stars Shooting Stars (2013-09-08): awarded 3-0; abandoned at 2-1 at half-time
- abandonado/suspenso, sem valer — Kano Pillars Enyimba (2013-09-11): abandoned at 1-0 in 87'

### 2014

- ogol: 215 jogos casados (edição 75055 do ogol, 380 jogos)
- data diferente no ogol — Warri Wolves x El-Kanemi Warriors: RSSSF 2014-03-13, ogol 2014-03-09; fica a da RSSSF
- data diferente no ogol — Sunshine Stars x Enyimba: RSSSF 2014-03-13, ogol 2014-03-09; fica a da RSSSF
- data diferente no ogol — El-Kanemi Warriors x Abia Warriors: RSSSF 2014-03-26, ogol 2014-03-16; fica a da RSSSF
- data diferente no ogol — Kaduna United x Bayelsa United: RSSSF 2014-04-09, ogol 2014-03-30; fica a da RSSSF
- data diferente no ogol — Dolphin x Warri Wolves: RSSSF 2014-04-23, ogol 2014-04-27; fica a da RSSSF
- data diferente no ogol — Nembe City x Heartland: RSSSF 2014-04-23, ogol 2014-04-27; fica a da RSSSF
- data diferente no ogol — El-Kanemi Warriors x Crown: RSSSF 2014-04-23, ogol 2014-04-27; fica a da RSSSF
- data diferente no ogol — Kaduna United x Sharks: RSSSF 2014-04-23, ogol 2014-04-27; fica a da RSSSF
- data diferente no ogol — Nasarawa United x Gombe United: RSSSF 2014-04-23, ogol 2014-04-27; fica a da RSSSF
- data diferente no ogol — Giwa x Akwa United: RSSSF 2014-04-23, ogol 2014-04-27; fica a da RSSSF
- data diferente no ogol — Sunshine Stars x FC Taraba: RSSSF 2014-04-23, ogol 2014-04-27; fica a da RSSSF
- data diferente no ogol — Enyimba x Lobi Stars: RSSSF 2014-04-23, ogol 2014-04-27; fica a da RSSSF
- data diferente no ogol — Enugu Rangers x Abia Warriors: RSSSF 2014-04-23, ogol 2014-04-27; fica a da RSSSF
- data diferente no ogol — Heartland x Enyimba: RSSSF 2014-04-26, ogol 2014-05-04; fica a da RSSSF
- data diferente no ogol — FC Taraba x Enugu Rangers: RSSSF 2014-04-27, ogol 2014-05-04; fica a da RSSSF
- data diferente no ogol — Abia Warriors x Warri Wolves: RSSSF 2014-04-27, ogol 2014-05-04; fica a da RSSSF
- data diferente no ogol — Akwa United x Sunshine Stars: RSSSF 2014-04-27, ogol 2014-05-04; fica a da RSSSF
- data diferente no ogol — Crown x Nembe City: RSSSF 2014-04-27, ogol 2014-05-04; fica a da RSSSF
- data diferente no ogol — Gombe United x Kaduna United: RSSSF 2014-04-27, ogol 2014-05-04; fica a da RSSSF
- data diferente no ogol — Lobi Stars x Kano Pillars: RSSSF 2014-04-27, ogol 2014-05-04; fica a da RSSSF
- data diferente no ogol — Nasarawa United x Dolphin: RSSSF 2014-04-27, ogol 2014-05-04; fica a da RSSSF
- data diferente no ogol — Sharks x El-Kanemi Warriors: RSSSF 2014-04-27, ogol 2014-05-04; fica a da RSSSF
- data diferente no ogol — Gombe United x Nembe City: RSSSF 2014-05-08, ogol 2014-05-18; fica a da RSSSF
- data diferente no ogol — Lobi Stars x Heartland: RSSSF 2014-07-27, ogol 2014-07-20; fica a da RSSSF
- data diferente no ogol — Enugu Rangers x El-Kanemi Warriors: RSSSF 2014-07-27, ogol 2014-07-20; fica a da RSSSF
- data diferente no ogol — Abia Warriors x Nasarawa United: RSSSF 2014-07-27, ogol 2014-07-20; fica a da RSSSF
- data diferente no ogol — Akwa United x Sharks: RSSSF 2014-07-27, ogol 2014-07-20; fica a da RSSSF
- data diferente no ogol — Giwa x Enyimba: RSSSF 2014-07-27, ogol 2014-07-20; fica a da RSSSF
- data diferente no ogol — Warri Wolves x Kaduna United: RSSSF 2014-07-27, ogol 2014-07-20; fica a da RSSSF
- data diferente no ogol — Sunshine Stars x Nembe City: RSSSF 2014-07-27, ogol 2014-07-20; fica a da RSSSF
- data diferente no ogol — Bayelsa United x Crown: RSSSF 2014-07-27, ogol 2014-07-20; fica a da RSSSF
- data diferente no ogol — FC Taraba x Gombe United: RSSSF 2014-07-27, ogol 2014-07-20; fica a da RSSSF
- data diferente no ogol — Dolphin x Kano Pillars: RSSSF 2014-07-27, ogol 2014-07-20; fica a da RSSSF
- data diferente no ogol — Dolphin x Heartland: RSSSF 2014-08-06, ogol 2014-07-27; fica a da RSSSF
- data diferente no ogol — Crown x Lobi Stars: RSSSF 2014-08-06, ogol 2014-07-27; fica a da RSSSF
- data diferente no ogol — Gombe United x Akwa United: RSSSF 2014-08-06, ogol 2014-07-27; fica a da RSSSF
- data diferente no ogol — Nasarawa United x FC Taraba: RSSSF 2014-08-06, ogol 2014-07-27; fica a da RSSSF
- data diferente no ogol — Kaduna United x Abia Warriors: RSSSF 2014-08-06, ogol 2014-07-27; fica a da RSSSF
- data diferente no ogol — El-Kanemi Warriors x Warri Wolves: RSSSF 2014-08-06, ogol 2014-07-27; fica a da RSSSF
- data diferente no ogol — Nembe City x Enugu Rangers: RSSSF 2014-08-06, ogol 2014-07-27; fica a da RSSSF
- data diferente no ogol — Sharks x Bayelsa United: RSSSF 2014-08-06, ogol 2014-07-27; fica a da RSSSF
- data diferente no ogol — Kano Pillars x Giwa: RSSSF 2014-08-06, ogol 2014-07-27; fica a da RSSSF
- data diferente no ogol — Enyimba x Sunshine Stars: RSSSF 2014-08-06, ogol 2014-07-27; fica a da RSSSF
- data diferente no ogol — Bayelsa United x Gombe United: RSSSF 2014-08-10, ogol 2014-08-03; fica a da RSSSF
- data diferente no ogol — Warri Wolves x Nembe City: RSSSF 2014-08-10, ogol 2014-08-03; fica a da RSSSF
- data diferente no ogol — Enugu Rangers x Enyimba: RSSSF 2014-08-10, ogol 2014-08-03; fica a da RSSSF
- data diferente no ogol — Akwa United x Nasarawa United: RSSSF 2014-08-10, ogol 2014-08-03; fica a da RSSSF
- data diferente no ogol — Heartland x Crown: RSSSF 2014-08-10, ogol 2014-08-03; fica a da RSSSF
- data diferente no ogol — Lobi Stars x Sharks: RSSSF 2014-08-10, ogol 2014-08-03; fica a da RSSSF
- data diferente no ogol — Sunshine Stars x Kano Pillars: RSSSF 2014-08-10, ogol 2014-08-03; fica a da RSSSF
- data diferente no ogol — Abia Warriors x El-Kanemi Warriors: RSSSF 2014-08-10, ogol 2014-08-03; fica a da RSSSF
- data diferente no ogol — FC Taraba x Kaduna United: RSSSF 2014-08-10, ogol 2014-08-03; fica a da RSSSF
- data diferente no ogol — Giwa x Dolphin: RSSSF 2014-08-10, ogol 2014-08-03; fica a da RSSSF
- data diferente no ogol — Bayelsa United x Kano Pillars: RSSSF 2014-09-24, ogol 2014-09-14; fica a da RSSSF
- data diferente no ogol — Gombe United x Nasarawa United: RSSSF 2014-09-24, ogol 2014-09-14; fica a da RSSSF
- data diferente no ogol — FC Taraba x Sunshine Stars: RSSSF 2014-09-24, ogol 2014-09-14; fica a da RSSSF
- data diferente no ogol — Crown x El-Kanemi Warriors: RSSSF 2014-09-24, ogol 2014-09-14; fica a da RSSSF
- data diferente no ogol — Sharks x Kaduna United: RSSSF 2014-09-24, ogol 2014-09-14; fica a da RSSSF
- data diferente no ogol — Abia Warriors x Enugu Rangers: RSSSF 2014-09-24, ogol 2014-09-14; fica a da RSSSF
- data diferente no ogol — Akwa United x Giwa: RSSSF 2014-09-24, ogol 2014-09-14; fica a da RSSSF
- data diferente no ogol — Heartland x Nembe City: RSSSF 2014-09-24, ogol 2014-09-14; fica a da RSSSF
- data diferente no ogol — Lobi Stars x Enyimba: RSSSF 2014-09-24, ogol 2014-09-14; fica a da RSSSF
- data diferente no ogol — Warri Wolves x Dolphin: RSSSF 2014-09-24, ogol 2014-09-14; fica a da RSSSF
- data diferente no ogol — Sunshine Stars x Akwa United: RSSSF 2014-09-28, ogol 2014-09-21; fica a da RSSSF
- data diferente no ogol — Kano Pillars x Lobi Stars: RSSSF 2014-09-28, ogol 2014-09-21; fica a da RSSSF
- data diferente no ogol — El-Kanemi Warriors x Sharks: RSSSF 2014-09-28, ogol 2014-09-21; fica a da RSSSF
- data diferente no ogol — Dolphin x Nasarawa United: RSSSF 2014-09-28, ogol 2014-09-21; fica a da RSSSF
- data diferente no ogol — Enugu Rangers x FC Taraba: RSSSF 2014-09-28, ogol 2014-09-21; fica a da RSSSF
- data diferente no ogol — Giwa x Bayelsa United: RSSSF 2014-09-28, ogol 2014-09-21; fica a da RSSSF
- data diferente no ogol — Nembe City x Crown: RSSSF 2014-09-28, ogol 2014-09-21; fica a da RSSSF
- data diferente no ogol — Kaduna United x Gombe United: RSSSF 2014-09-28, ogol 2014-09-21; fica a da RSSSF
- data diferente no ogol — Enyimba x Heartland: RSSSF 2014-09-28, ogol 2014-09-21; fica a da RSSSF
- data diferente no ogol — Warri Wolves x Abia Warriors: RSSSF 2014-09-29, ogol 2014-09-21; fica a da RSSSF
- data diferente no ogol — Bayelsa United x Sunshine Stars: RSSSF 2014-10-05, ogol 2014-09-28; fica a da RSSSF
- data diferente no ogol — Gombe United x El-Kanemi Warriors: RSSSF 2014-10-05, ogol 2014-09-28; fica a da RSSSF
- data diferente no ogol — FC Taraba x Warri Wolves: RSSSF 2014-10-05, ogol 2014-09-28; fica a da RSSSF
- data diferente no ogol — Crown x Enyimba: RSSSF 2014-10-05, ogol 2014-09-28; fica a da RSSSF
- data diferente no ogol — Sharks x Nembe City: RSSSF 2014-10-05, ogol 2014-09-28; fica a da RSSSF
- data diferente no ogol — Nasarawa United x Kaduna United: RSSSF 2014-10-05, ogol 2014-09-28; fica a da RSSSF
- data diferente no ogol — Abia Warriors x Dolphin: RSSSF 2014-10-05, ogol 2014-09-28; fica a da RSSSF
- data diferente no ogol — Akwa United x Enugu Rangers: RSSSF 2014-10-05, ogol 2014-09-28; fica a da RSSSF
- data diferente no ogol — Heartland x Kano Pillars: RSSSF 2014-10-05, ogol 2014-09-28; fica a da RSSSF
- data diferente no ogol — Lobi Stars x Giwa: RSSSF 2014-10-05, ogol 2014-09-28; fica a da RSSSF
- data diferente no ogol — Nembe City x Gombe United: RSSSF 2014-10-09, ogol 2014-10-05; fica a da RSSSF
- data diferente no ogol — Kaduna United x Enyimba: RSSSF 2014-10-19, ogol 2014-10-26; fica a da RSSSF
- data diferente no ogol — Nasarawa United x Kano Pillars: RSSSF 2014-10-19, ogol 2014-10-26; fica a da RSSSF
- data diferente no ogol — El-Kanemi Warriors x Nembe City: RSSSF 2014-10-19, ogol 2014-10-26; fica a da RSSSF
- data diferente no ogol — Crown x Enugu Rangers: RSSSF 2014-10-19, ogol 2014-10-26; fica a da RSSSF
- data diferente no ogol — Sharks x Sunshine Stars: RSSSF 2014-10-19, ogol 2014-10-26; fica a da RSSSF
- data diferente no ogol — Bayelsa United x FC Taraba: RSSSF 2014-10-19, ogol 2014-10-26; fica a da RSSSF
- data diferente no ogol — Gombe United x Giwa: RSSSF 2014-10-19, ogol 2014-10-26; fica a da RSSSF
- data diferente no ogol — Akwa United x Dolphin: RSSSF 2014-10-19, ogol 2014-10-26; fica a da RSSSF
- data diferente no ogol — Lobi Stars x Abia Warriors: RSSSF 2014-10-19, ogol 2014-10-26; fica a da RSSSF
- data diferente no ogol — Heartland x Warri Wolves: RSSSF 2014-10-19, ogol 2014-10-26; fica a da RSSSF
- decidido fora de campo — Nembe City Lobi Stars (2014-09-21): awarded 0-3, originally 2-1
- decidido fora de campo — Nembe City Gombe United (2014-10-09): awarded 0-3; abandoned at 2-2 in 89'

### 2015

- ogol: 375 jogos casados (edição 89082 do ogol, 380 jogos)
- placar diferente no ogol — Ifeanyi Ubah x Sharks (2015-05-17): RSSSF 1-0, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — El-Kanemi Warriors x Ifeanyi Ubah (2015-06-21): RSSSF 1-4, ogol 0-2; fica o da RSSSF
- placar diferente no ogol — Kwara United x Lobi Stars (2015-06-21): RSSSF 1-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Sunshine Stars x Kano Pillars (2015-06-21): RSSSF 3-0, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Enugu Rangers x Lobi Stars (2015-07-12): RSSSF 3-1, ogol 3-0; fica o da RSSSF
- placar diferente no ogol — Heartland x Enugu Rangers (2015-09-06): RSSSF 2-0, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Ifeanyi Ubah x El-Kanemi Warriors (2015-11-04): RSSSF 2-1, ogol 3-0; fica o da RSSSF
- não jogado — Ifeanyi Ubah El-Kanemi Warriors (2015-10-11): El-Kanemi dns
- abandonado/suspenso, sem valer — FC Taraba Nasarawa United (2015-10-28): abandoned at 0-0 in 81'
- decidido fora de campo — Nasarawa United Sharks (2015-11-01): awarded 3-0; abandoned at 2-2 in 55' after
- abandonado/suspenso, sem valer — Sunshine Stars Lobi Stars (2015-11-01): abandoned at 0-1 in 77'
- decidido fora de campo — Nasarawa United Giwa (2015-11-15): awarded 3-0; abandoned at 2-0 in 35' after

### 2016

- ogol: 357 jogos casados (edição 95931 do ogol, 380 jogos)
- jogos do Giwa anulados: Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- tabela nig2016:43 fora da conferência: campanha do clube expulso até a expulsão ("record at expulsion"), não é tabela da edição
- tabela nig2016:636 fora da conferência: campanha do clube expulso até a expulsão (repetida no fim da página)
- anulado — Giwa 0-1 Ifeanyi Ubah (2016-02-21): annulled; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Niger Tornadoes 1-1 Giwa (2016-02-24): annulled; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Nasarawa United 3-1 Giwa (2016-04-13): annulled; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Giwa 2-1 Rivers United (2016-03-02): annulled; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Shooting Stars 2-1 Giwa (2016-03-06): annulled; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Giwa 1-0 Sunshine Stars (2016-03-13): annulled; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Ikorodu United 1-2 Giwa (2016-03-20): annulled; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Giwa 1-1 El-Kanemi Warriors (2016-03-23): annulled; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Heartland 2-0 Giwa (2016-03-27): annulled; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Giwa 2-0 Kano Pillars (2016-04-06): annulled; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- abandonado/suspenso, sem valer — Abia Warriors Lobi Stars (2016-04-10): abandoned at 1-0 in 35' due to heavy rain
- anulado — Plateau United 2-0 Giwa (2016-04-10): annulled; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Giwa Enugu Rangers (2016-04-17): abandoned at 0-1 in 74' due to; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Giwa 0-1 Enugu Rangers (2016-04-27): annulled; remaining 16'; Giwa failed to show; Jun 22]                                             originally result at abandonment Apr 17 stood; jogo repetido (o primeiro foi suspenso); Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Warri Wolves 2-0 Giwa (2016-04-24): annulled; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Giwa Wikki Tourists (2016-05-01): awarded 0-3; later annulled; Giwa failed; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Abia Warriors 1-0 Giwa (2016-05-07): annulled; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Giwa Akwa United (2016-05-11): awarded 0-3; later annulled; Giwa failed; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Lobi Stars 2-0 Giwa (2016-05-15): annulled; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — Giwa Enyimba (2016-05-18): awarded 0-3; later annulled; Giwa failed; Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- anulado — MFM Giwa (2016-05-22): Giwa FC expulso por não comparecer a três jogos; todos os seus resultados anulados
- decidido fora de campo — Plateau United Heartland (2016-10-02): awarded 3-0; abandoned at 1-1 in 80';

### 2017

- ogol: 349 jogos casados (edição 102964 do ogol, 380 jogos)
- data diferente no ogol — Rivers United x ABS: RSSSF 2017-04-06, ogol 2017-03-29; fica a da RSSSF
- placar diferente no ogol — Rivers United x Abia Warriors (2017-04-09): RSSSF 1-0, ogol 2-0; fica o da RSSSF
- decidido fora de campo — Kano Pillars Ifeanyi Ubah (2017-01-14): awarded 3-0; abandoned at 1-0 in 50'
- abandonado/suspenso, sem valer — Enugu Rangers MFM (2017-07-19): abandoned at 1-0 at half-time due to heavy rain
- abandonado/suspenso, sem valer — Niger Tornadoes Ifeanyi Ubah (2017-08-27): abandoned at 0-1 at half-time due to heavy rain

### 2018

- temporada abandonada pela crise interna da federação nigeriana ("league abandoned following internal crisis at Nigerian Football Federation"); a tabela é a do abandono
- ogol: 237 jogos casados (edição 121449 do ogol, 380 jogos)
- placar diferente no ogol — Rivers United x Ifeanyi Ubah (2018-03-04): RSSSF 1-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — El-Kanemi Warriors x Niger Tornadoes (2018-03-04): RSSSF 0-0, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — Niger Tornadoes x Sunshine Stars (2018-03-25): RSSSF 1-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Yobe Desert Stars x Enyimba (2018-03-25): RSSSF 1-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Wikki Tourists x Yobe Desert Stars (2018-05-20): RSSSF 3-1, ogol 3-0; fica o da RSSSF

### 2019

- o Delta Force tem só 11 dos 22 jogos na página; a classificação é a tabela publicada
- ogol: 268 jogos casados (edição 133611 do ogol, 279 jogos)
- tabela publicada x jogos — nig2019:283: Delta Force tabela [22, 9, 4, 9, 19, 26] jogos [11, 4, 3, 4, 8, 11] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- placar diferente no ogol — Rivers United x Enugu Rangers (2019-05-02): RSSSF 3-0, ogol 1-0; fica o da RSSSF
- data diferente no ogol — Rivers United x Enugu Rangers: RSSSF 2019-05-02, ogol 2019-05-08; fica a da RSSSF
- abandonado/suspenso, sem valer — Kano Pillars Enyimba (2019-06-06): abandoned at 0-0 in 45+1' due to heavy rain

### 2019/20

- temporada abandonada (Covid-19); a página só traz parte dos jogos; no meio da temporada o Delta Force vendeu a vaga ao Akwa Starlets
- temporada abandonada pela Covid-19, sem campeão; a tabela é a do abandono (pela média de pontos por jogo)
- jogos incompletos (só os resultados que a página traz)
- ogol: 220 jogos casados (edição 140618 do ogol, 380 jogos)

### 2020/21

- ogol: 379 jogos casados (edição 149643 do ogol, 380 jogos)

### 2021/22

- ogol: 380 jogos casados (edição 161314 do ogol, 380 jogos)
- data diferente no ogol — Kano Pillars x Sunshine Stars: RSSSF 2022-04-27, ogol 2022-05-04; fica a da RSSSF
- abandonado/suspenso, sem valer — Kano Pillars Katsina United (2022-04-16): abandoned at 0-0 in 79' due to crowd
- abandonado/suspenso, sem valer — Niger Tornadoes Lobi Stars (2022-05-28): abandoned at 0-0 at half-time due to crowd

### 2023

- Bayelsa United com 3 gols a mais nos jogos que na tabela (a Wikipédia confirma a tabela); nenhum placar mudado
- ogol: 195 jogos casados (edição 171344 do ogol, 195 jogos)
- tabela publicada x jogos — nig2023:240: Bayelsa United tabela [18, 6, 6, 6, 24, 24] jogos [18, 6, 6, 6, 27, 24] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- abandonado/suspenso, sem valer — Remo Stars Gombe United (2023-04-02): abandoned at 0-0 at half-time due
- abandonado/suspenso, sem valer — Rivers United Dakkada (2023-04-16): abandoned at 1-0 in 52'

### 2023/24

- Gombe United: punição de 3 pontos e 3 gols ("3 points and 3 goals deducted"): a tabela desconta os gols, os jogos não; a classificação é a tabela publicada (duas vezes)
- ogol: 372 jogos casados (edição 179826 do ogol, 380 jogos)
- tabela publicada x jogos — nig2024:24: Gombe United tabela [38, 8, 7, 23, 21, 78] jogos [38, 8, 7, 23, 27, 78] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- corrigido — Sporting Lagos x Remo Stars (2024-03-10): a nota ("... committee annulled a change of decision ...") é do Enyimba x Doma United, na linha de cima; o jogo vale (as tabelas da RSSSF e da Wikipédia o contam)
- placar diferente no ogol — Enyimba x Bendel Insurance (2023-11-22): RSSSF 2-1, ogol 2-2; fica o da RSSSF
- abandonado/suspenso, sem valer — Bayelsa United Rivers United (2024-04-29): abandoned at 1-0 in 7' due
- decidido fora de campo — Enugu Rangers Enyimba (2024-06-09): awarded 3-0; abandoned at 0-0 in injury

### 2024/25

- Plateau United com 3 gols a mais nos jogos que na tabela (provável punição como as de 2023/24 e 2025/26)
- ogol: 380 jogos casados (edição 188261 do ogol, 380 jogos)
- tabela publicada x jogos — nig2025:22: Plateau United tabela [38, 16, 9, 13, 40, 38] jogos [38, 16, 9, 13, 43, 38] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- abandonado/suspenso, sem valer — Enyimba Katsina United (2024-10-06): abandoned at 3-0 in 72' due
- abandonado/suspenso, sem valer — Rivers United Katsina United (2025-02-27): abandoned at 1-0 at half-time

### 2025/26

- Kano Pillars e Kwara United: punição de 3 pontos e 3 gols ("3 points and 3 goals deducted"): a tabela desconta os gols, os jogos não; a classificação é a tabela publicada
- ogol: 379 jogos casados (edição 203428 do ogol, 380 jogos)
- tabela publicada x jogos — nig2026:24: Kano Pillars tabela [38, 15, 6, 17, 34, 39] jogos [38, 15, 6, 17, 37, 39] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — nig2026:24: Kwara United tabela [38, 13, 11, 14, 32, 36] jogos [38, 13, 11, 14, 35, 36] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- abandonado/suspenso, sem valer — Enugu Rangers Katsina United (2025-10-05): abandoned at 0-0 at half-time due to heavy rain
- decidido fora de campo — El-Kanemi Warriors Kun Khalifat (2026-02-02): awarded 3-0, Kun Khalifat dns
- abandonado/suspenso, sem valer — Wikki Tourists Katsina United (2026-02-08): abandoned at 3-3 in 78' due to poor light
- abandonado/suspenso, sem valer — Bendel Insurance Katsina United (2026-05-03): abandoned at 0-0 in 62' due to heavy rain

