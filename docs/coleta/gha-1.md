# Campeonato Ganês (1ª divisão) — coleta de dados

Gerado por `python coleta/gha-1/importar.py`. Pacote em `data/coleta/gha-1/pacote/`.

**Edições:** 65, de 1958 a 2025/26, como a lista de campeões da RSSSF (`ghachamp.html`), sem o campeonato não oficial de 1956 e sem a competição especial do Comitê de Normalização de 2019 (não foi liga; a imprensa não a conta: o título de 2021/22 foi o "25º" do Asante Kotoko). Pesquisa de 24/11/2026, aprovada pelo Guilherme. 2018 e 2019/20 foram abandonados e entram sem campeão.

**Fora do pacote:** a FA Cup e as outras copas, as ligas regionais da era colonial, a 2ª divisão e os jogos de acesso.

**Fontes:** RSSSF (lista de tabelas finais `ghahist.html`, de 1958 a 1987; páginas por ano: a tabela de 1989/90 a 1996/97 e os jogos de 1997/98 em diante, parte da temporada em 1997/98 e 2006/07); ogol (jogos de 2008/09 a 2010/11 e de 2015 em diante: base de 2010/11, conferência, rodada e data nos outros); Wikipédia em inglês (tabela das temporadas que têm artigo). A ESPN não tem a liga.

**Clubes:** o nome pelo qual o clube é conhecido (Asante Kotoko, Hearts of Oak, Ashanti Gold...). Mesmo clube com outro nome é um só (Goldfields = Ashanti Gold; Mysterious Dwarfs = Ebusua Dwarfs; RTU = Real Tamale United). Regras em `coleta/gha-1/clubes_gha.py`.

**Regras:** o placar é o da RSSSF (ou do ogol em 2010/11). A classificação é a tabela publicada (ordem oficial e pontos). Pontos 2-1-0 (vitória, empate, derrota) até 1993/94 (fora 1989/90, com 3 por vitória) e 3-1-0 desde 1994/95.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Formato |
|---|---|---|---|---|---|---|---|
| 1958 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Hearts of Oak | sem jogos (só a tabela final) |
| 1959/60 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1960/61 | 8 | 0 (0) | 0 | 0 | 0 / 0 | Eleven Wise | sem jogos (só a tabela final) |
| 1961/62 | 15 | 0 (0) | 0 | 0 | 0 / 0 | Hearts of Oak | sem jogos (só a tabela final) |
| 1962/63 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Real Republicans | sem jogos (só a tabela final) |
| 1963/64 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1964/65 | 20 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1966 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Ebusua Dwarfs | sem jogos (só a tabela final) |
| 1967 | 20 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1968 | 19 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1969 | 36 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1970 | 50 | 0 (0) | 0 | 0 | 0 / 0 | Great Olympics | sem jogos (só a tabela final) |
| 1971 | 20 | 0 (0) | 0 | 0 | 0 / 0 | Hearts of Oak | sem jogos (só a tabela final) |
| 1972 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1973 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Hearts of Oak | sem jogos (só a tabela final) |
| 1974 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Great Olympics | sem jogos (só a tabela final) |
| 1975 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1976 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Hearts of Oak | sem jogos (só a tabela final) |
| 1977 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Hasaacas | sem jogos (só a tabela final) |
| 1978 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Hearts of Oak | sem jogos (só a tabela final) |
| 1979 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Hearts of Oak | sem jogos (só a tabela final) |
| 1980 | 18 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1981 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1982 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1983 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1984 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Hearts of Oak | sem jogos (só a tabela final) |
| 1985 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Hearts of Oak | sem jogos (só a tabela final) |
| 1986 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1987 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1988/89 | 1 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só o campeão) |
| 1989/90 | 11 | 0 (0) | 0 | 0 | 0 / 0 | Hearts of Oak | sem jogos (só a classificação incompleta) |
| 1990/91 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1991/92 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1992/93 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 1993/94 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Ashanti Gold | sem jogos (só a tabela final) |
| 1994/95 | 12 | 0 (0) | 0 | 0 | 0 / 0 | Ashanti Gold | sem jogos (só a tabela final) |
| 1995/96 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Ashanti Gold | sem jogos (só a tabela final) |
| 1996/97 | 14 | 0 (0) | 0 | 0 | 0 / 0 | Hearts of Oak | sem jogos (só a tabela final) |
| 1997/98 | 14 | 150 (150) | 296 | 0 | 0 / 0 | Hearts of Oak | jogos incompletos (só os resultados que a página traz) |
| 1999 | 16 | 241 (241) | 525 | 0 | 0 / 1 | Hearts of Oak | pontos corridos |
| 2000 | 16 | 240 (240) | 528 | 0 | 0 / 1 | Hearts of Oak | pontos corridos |
| 2001 | 16 | 240 (240) | 490 | 0 | 1 / 0 | Hearts of Oak | pontos corridos |
| 2002 | 16 | 240 (240) | 514 | 1 | 1 / 0 | Hearts of Oak | pontos corridos |
| 2003 | 16 | 241 (241) | 474 | 0 | 1 / 0 | Asante Kotoko | pontos corridos |
| 2004/05 | 16 | 117 (117) | 255 | 62 | 2 / 0 | Hearts of Oak | 2 grupos + jogos de classificação + desempate + mata-mata |
| 2005 | 16 | 240 (240) | 500 | 52 | 1 / 0 | Asante Kotoko | pontos corridos |
| 2006/07 | 16 | 97 (97) | 185 | 0 | 0 / 0 | Hearts of Oak | jogos incompletos (só os resultados que a página traz) |
| 2007/08 | 16 | 241 (241) | 556 | 35 | 1 / 0 | Asante Kotoko | pontos corridos |
| 2008/09 | 16 | 240 (240) | 501 | 1 | 1 / 0 | Hearts of Oak | pontos corridos |
| 2009/10 | 16 | 240 (240) | 519 | 143 | 1 / 0 | Aduana Stars | pontos corridos |
| 2010/11 | 16 | 240 (240) | 434 | 0 | 0 / 1 | Berekum Chelsea | pontos corridos |
| 2011/12 | 16 | 0 (0) | 0 | 0 | 0 / 0 | Asante Kotoko | sem jogos (só a tabela final) |
| 2012/13 | 16 | 242 (242) | 511 | 0 | 1 / 0 | Asante Kotoko | pontos corridos |
| 2013/14 | 16 | 240 (240) | 474 | 0 | 1 / 0 | Asante Kotoko | pontos corridos |
| 2015 | 16 | 240 (240) | 514 | 0 | 0 / 1 | Ashanti Gold | pontos corridos |
| 2016 | 16 | 240 (240) | 499 | 0 | 1 / 0 | Wa All Stars | pontos corridos |
| 2017 | 16 | 242 (242) | 530 | 0 | 1 / 0 | Aduana Stars | pontos corridos |
| 2018 | 16 | 120 (120) | 241 | 0 | 1 / 0 | — | temporada não terminada |
| 2019/20 | 18 | 135 (135) | 277 | 0 | 1 / 0 | — | temporada não terminada |
| 2020/21 | 18 | 306 (306) | 694 | 0 | 1 / 0 | Hearts of Oak | pontos corridos |
| 2021/22 | 18 | 306 (306) | 624 | 0 | 1 / 0 | Asante Kotoko | pontos corridos |
| 2022/23 | 18 | 308 (308) | 644 | 0 | 1 / 0 | Medeama | pontos corridos |
| 2023/24 | 18 | 307 (307) | 628 | 0 | 1 / 0 | Samartex | pontos corridos |
| 2024/25 | 18 | 307 (307) | 591 | 0 | 1 / 0 | Bibiani Gold Stars | pontos corridos |
| 2025/26 | 18 | 309 (309) | 627 | 0 | 1 / 0 | Medeama | pontos corridos |

## Conferência e correções, edição a edição

### 1958

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1959/60

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1960/61

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1961/62

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1962/63

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1963/64

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1964/65

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1966

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1967

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1968

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1969

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1970

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1971

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1972

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1973

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1974

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1975

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1976

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1977

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1978

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1979

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1980

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1981

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1982

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1983

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1984

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1985

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1986

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1987

- a RSSSF só traz a tabela final (lista de tabelas finais)

### 1988/89

- a RSSSF só traz o campeão ("Final table missing")

### 1989/90

- a RSSSF só traz a classificação incompleta (posição, jogos e pontos)

### 1990/91

- a RSSSF só traz a tabela final

### 1991/92

- a RSSSF só traz a tabela final

### 1992/93

- a RSSSF só traz a tabela final

### 1993/94

- a RSSSF só traz a tabela final

### 1994/95

- a RSSSF só traz a tabela final

### 1995/96

- a RSSSF só traz a tabela final

### 1996/97

- a RSSSF só traz a tabela final

### 1997/98

- jogos incompletos (só os resultados que a página traz)
- decidido fora de campo — Asante Kotoko Dawu Youngstars (1997-12-07): apparently awarded to Kotoko, originally reported 2-3
- decidido fora de campo — Great Olympics Swedru All Blacks (1997-12-07): apparently home win, originally reported 0-1

### 1999

- a lista de jogos da página não fecha com a tabela em dois clubes (sem terceira fonte); nenhum placar foi mudado e o relatório aponta o jogo provável
- tabela publicada x jogos — gha99:16: Okwahu United tabela [30, 16, 2, 12, 38, 29] jogos [30, 15, 2, 13, 35, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — gha99:16: Swedru All Blacks tabela [30, 10, 5, 15, 32, 42] jogos [30, 11, 5, 14, 33, 39] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- provável jogo da diferença: Swedru All Blacks 1-0 Okwahu United (1999-04-28, gha99:137); com 0-3 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- decidido fora de campo — Swedru All Blacks 0-3 Okwahu United (1999-04-28): awarded after originally 1-0
- abandonado/suspenso, sem valer — Okwahu United Ashanti Gold (1999-09-26): abandoned at 0-0 in 80' when Goldfields

### 2000

- a lista de jogos da página não fecha com a tabela em dois clubes (sem terceira fonte); nenhum placar foi mudado e o relatório aponta o jogo provável
- tabela publicada x jogos — gha00:16: Asante Kotoko tabela [30, 13, 7, 10, 39, 31] jogos [30, 13, 7, 10, 39, 29] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — gha00:16: Okwahu United tabela [30, 10, 11, 9, 31, 27] jogos [30, 10, 11, 9, 29, 27] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- provável jogo da diferença: Okwahu United 1-0 Asante Kotoko (2000-08-06, gha00:251); com 3-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- decidido fora de campo — Okwahu United 3-0 Asante Kotoko (2000-08-06): awarded; abd at 1-0, 88'; Kotoko refused to continue

### 2001

- decidido fora de campo — Tano Bofoakwa King Faisal Babes (2001-04-22): awarded 3-0 to Bofoakwa as Faisal used
- W.O./pontos para o visitante — Adansiman Real Tamale United (2001-07-05): by 2 so 0-2 or 1-3...]  [lt
- W.O./pontos para o mandante — Ashanti Gold King Faisal Babes (2001-07-11): by 3 goals?]  [bt
- W.O./pontos para o mandante — Asante Kotoko Adansiman (2001-07-11): by 1 goal]  [bt
- W.O./pontos para o mandante — Liberty Professionals Ashanti Gold (2001-08-08): by 1 goal]  [bt
- W.O./pontos para o mandante — Ashanti Gold Real Tamale United (2001-08-12): by 1 goal]  [bt
- decidido fora de campo — Tano Bofoakwa Asante Kotoko (2001-09-09): awarded 3-0 to Bofoakwa, Kotoko 3 points deducted; Sep 12]                         abandoned at 0-0 in 75' after a 'fan' attacked
- decidido fora de campo — Okwahu United Ashanti Gold (2001-09-23): awarded 3-0 to Okwawu, forfeit Goldfields
- W.O./pontos para o mandante — Maxbees Berekum Arsenal (2001-10-14): wrongly reported 0-2 (or awarded)]  [bt
- W.O./pontos para o mandante — Asante Kotoko Berekum Arsenal (2001-11-11): wrongly reported 1-1 (or awarded)]  [bt

### 2002

- sem ocorrências

### 2003

- a tabela conta oito resultados dados (nota da página) e um desconto de 3 pontos de quem perdeu cada decisão; os jogos ficam com o placar dado e o de campo na observação
- corrigido — None x Berekum Arsenal (None): linha da nota sobre os resultados dados (não é jogo)
- corrigido — None x Berekum Arsenal (None): linha da nota sobre os resultados dados (não é jogo)
- corrigido — None x Okwahu United (None): linha da nota sobre os resultados dados (não é jogo)
- corrigido — None x Stay Cool (None): linha da nota sobre os resultados dados (não é jogo)
- corrigido — None x Real Tamale United (None): linha da nota sobre os resultados dados (não é jogo)
- corrigido — Ashanti Gold x Berekum Arsenal (2003-05-11): resultado dado que a tabela conta (nota da página: "counted as awarded")
- corrigido — Brong Ahafo United x Berekum Arsenal (2003-05-25): resultado dado que a tabela conta (nota da página: "counted as awarded")
- corrigido — Prestea Mine Stars x Okwahu United (2003-05-28): resultado dado que a tabela conta (nota da página: "counted as awarded")
- corrigido — Tano Bofoakwa x Stay Cool (2003-06-15): resultado dado que a tabela conta (nota da página: "counted as awarded")
- corrigido — Ashanti Gold x Real Tamale United (2003-07-23): resultado dado que a tabela conta (nota da página: "counted as awarded")
- corrigido — Ashanti Gold x Great Olympics (2003-08-06): resultado dado que a tabela conta (nota da página: "counted as awarded")
- corrigido — Great Olympics x Ashanti Gold (2003-09-03): resultado dado que a tabela conta (nota da página: "counted as awarded")
- corrigido — Prestea Mine Stars x Hearts of Oak (2003-09-14): resultado dado que a tabela conta (nota da página: "counted as awarded")
- corrigido — None x Berekum Arsenal (2003-12-07): linha da nota sobre os resultados dados (não é jogo)
- corrigido — None x Berekum Arsenal (2003-12-07): linha da nota sobre os resultados dados (não é jogo)
- corrigido — None x Okwahu United (2003-12-07): linha da nota sobre os resultados dados (não é jogo)
- corrigido — None x Stay Cool (2003-12-07): linha da nota sobre os resultados dados (não é jogo)
- corrigido — None x Real Tamale United (2003-12-07): linha da nota sobre os resultados dados (não é jogo)
- decidido fora de campo — Ashanti Gold Berekum Arsenal (2003-05-11): 0-3 dado (1-0 em campo)
- decidido fora de campo — Brong Ahafo United Berekum Arsenal (2003-05-25): 0-3 dado (1-0; revogado? em campo)
- decidido fora de campo — Prestea Mine Stars Okwahu United (2003-05-28): 0-3 dado (1-0 em campo)
- decidido fora de campo — Tano Bofoakwa Stay Cool (2003-06-15): 3-0 dado (1-1 em campo)
- decidido fora de campo — Ashanti Gold Real Tamale United (2003-07-23): 0-3 dado (4-0 em campo)
- decidido fora de campo — Ashanti Gold Great Olympics (2003-08-06): 0-3 dado (3-1 em campo)
- decidido fora de campo — Great Olympics Ashanti Gold (2003-09-03): 3-0 dado (1-1 em campo)
- decidido fora de campo — Prestea Mine Stars Hearts of Oak (2003-09-14): 0-3 dado (1-1 em campo)
- abandonado/suspenso, sem valer — Ashanti Gold Hearts of Oak (2003-11-09): 0-2 rained off after 76 min

### 2004/05

- dois grupos, jogo do título (Hearts of Oak 1-0 Asante Kotoko, abril de 2005), 3º lugar e desempate do rebaixamento
- abandonado/suspenso, sem valer — Okwahu United Ashanti Gold (2004-09-19): abandoned at 1-0 in 18' due to rain
- abandonado/suspenso, sem valer — King Faisal Babes Okwahu United (2004-10-03): abandoned at 1-0 at half-time due to rain

### 2005

- decidido fora de campo — Real Tamale United Asante Kotoko (2005-11-06): awarded 0-3; abandoned at 0-0 in second

### 2006/07

- jogos incompletos (só os resultados que a página traz)
- decidido fora de campo — King Faisal Babes Tano Bofoakwa (2006-08-20): awarded 0-3; originally 1-0;
- não jogado — Tema Youth Hearts of Oak (2006-10-21): awarded 3-0, Hearts of Oak dns;
- decidido fora de campo — Feyenoord Academy Tano Bofoakwa (2006-10-21): awarded 3-0, originally 0-0

### 2007/08

- decidido fora de campo — Hasaacas Real Tamale United (2007-12-23): awarded 3-0
- decidido fora de campo — Real Sportive Zaytuna United (2008-06-18): awarded 0-3; originally 1-0;
- abandonado/suspenso, sem valer — Wa All Stars Asante Kotoko (2008-06-25): abandoned at 0-0 in 36' due to

### 2008/09

- ogol: 232 jogos casados (edição 5395 do ogol, 248 jogos)
- placar diferente no ogol — Ashanti Gold x Swedru All Blacks (2009-06-17): RSSSF 2-1, ogol 2-0; fica o da RSSSF
- decidido fora de campo — Tema Youth Berekum Arsenal (2009-05-10): awarded 0-3; originally 6-0,
- decidido fora de campo — Tema Youth Eleven Wise (2009-05-17): awarded 0-3; originally 1-0,
- decidido fora de campo — Eleven Wise Wa All Stars (2009-06-14): awarded 0-3; originally 0-0

### 2009/10

- o returno Asante Kotoko x New Edubiase vem do ogol (falta na página da RSSSF)
- ogol: 239 jogos casados (edição 16289 do ogol, 240 jogos)
- jogo acrescentado à mão — Asante Kotoko 2-0 New Edubiase United: jogo que falta na página da RSSSF (vem do ogol; a tabela da RSSSF só fecha com ele)
- placar diferente no ogol — Eleven Wise x Real Tamale United (2009-11-29): RSSSF 4-3, ogol 4-2; fica o da RSSSF
- decidido fora de campo — Kessben Berekum Chelsea (2010-02-28): awarded 0-3; abandoned due

### 2010/11

- os jogos vêm do ogol e não fecham com a tabela da RSSSF em sete clubes; nenhum placar foi mudado e a classificação é a tabela publicada
- os jogos vêm do calendário do ogol (a RSSSF só traz parte deles)
- ogol: base dos jogos (240 jogos)
- tabela publicada x jogos — gha2011:24: Ashanti Gold tabela [30, 13, 8, 9, 24, 14] jogos [30, 13, 8, 9, 23, 13] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — gha2011:24: Aduana Stars tabela [30, 12, 9, 9, 20, 18] jogos [30, 12, 9, 9, 19, 17] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — gha2011:24: New Edubiase United tabela [30, 11, 10, 9, 33, 32] jogos [30, 9, 11, 10, 29, 35] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — gha2011:24: Berekum Arsenal tabela [30, 11, 8, 11, 30, 34] jogos [30, 11, 8, 11, 29, 33] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — gha2011:24: King Faisal Babes tabela [30, 10, 6, 14, 26, 32] jogos [30, 10, 6, 14, 25, 31] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — gha2011:24: Real Tamale United tabela [30, 9, 6, 15, 24, 26] jogos [30, 10, 6, 14, 27, 25] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — gha2011:24: B.A. Stars tabela [30, 7, 4, 19, 16, 44] jogos [30, 7, 5, 18, 16, 41] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: Ashanti Gold 1-0 Aduana Stars (2010-11-28, ogol:1539044); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Aduana Stars 1-0 Ashanti Gold (2011-01-16, ogol:1613395); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Ashanti Gold 1-1 Berekum Arsenal (2010-10-31, ogol:1539014); com 2-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Berekum Arsenal 1-0 Ashanti Gold (2011-03-27, ogol:1613430); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Ashanti Gold 0-0 King Faisal Babes (2010-11-15, ogol:1539030); com 1-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: King Faisal Babes 0-0 Ashanti Gold (2011-03-02, ogol:1613414); com 1-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Berekum Arsenal 1-1 Aduana Stars (2010-12-19, ogol:1539061); com 2-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Aduana Stars 1-0 Berekum Arsenal (2011-01-09, ogol:1613381); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: King Faisal Babes 0-1 Aduana Stars (2010-09-12, ogol:1538952); com 1-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Aduana Stars 2-0 King Faisal Babes (2011-05-29, ogol:1613480); com 3-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: Berekum Arsenal 0-0 King Faisal Babes (2010-11-28, ogol:1539046); com 1-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: King Faisal Babes 1-0 Berekum Arsenal (2011-01-16, ogol:1613397); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 2011/12

- a RSSSF só traz a tabela final

### 2012/13

- abandonado/suspenso, sem valer — King Faisal Babes Berekum Chelsea (2012-12-02): abd (rained-off) at 1-1 in 55'
- decidido fora de campo — Real Tamale United Berekum Arsenal (2013-05-19): awarded 0-3; originally 2-2, RTU
- abandonado/suspenso, sem valer — New Edubiase United Hearts of Oak (2013-06-09): abandoned at 0-1 in 75' due to rain

### 2013/14

- sem ocorrências

### 2015

- Asante Kotoko com 3 gols a mais nos jogos que na tabela (provável punição de gols, como as da Nigéria); nenhum placar mudado
- ogol: 210 jogos casados (edição 92979 do ogol, 240 jogos)
- tabela publicada x jogos — gha2015:24: Asante Kotoko tabela [30, 12, 9, 9, 36, 32] jogos [30, 12, 9, 9, 39, 32] — a Wikipédia traz [30, 13, 9, 8, 41, 30]
- placar diferente no ogol — Berekum Chelsea x Wa All Stars (2015-09-13): RSSSF 2-1, ogol 2-0; fica o da RSSSF
- decidido fora de campo — Hearts of Oak Asante Kotoko (2015-08-02): awarded 3-0, originally 1-2; Kotoko

### 2016

- ogol: 237 jogos casados (edição 95298 do ogol, 240 jogos)
- data diferente no ogol — WAFA x Medeama: RSSSF 2016-07-06, ogol 2016-06-29; fica a da RSSSF
- decidido fora de campo — Techiman City New Edubiase United (2016-08-17): awarded 3-0; originally 1-2; New Edubiase

### 2017

- ogol: 240 jogos casados (edição 103878 do ogol, 240 jogos)
- data diferente no ogol — Liberty Professionals x Wa All Stars: RSSSF 2017-03-18, ogol 2017-03-25; fica a da RSSSF
- data diferente no ogol — Medeama x Great Olympics: RSSSF 2017-03-18, ogol 2017-03-25; fica a da RSSSF
- decidido fora de campo — Bolga All Stars Great Olympics (2017-02-26): awarded 0-3, originally 1-0; Bolga failed to
- abandonado/suspenso, sem valer — Tema Youth Wa All Stars (2017-04-09): abandoned at 0-0 in 18'
- abandonado/suspenso, sem valer — Great Olympics Aduana Stars (2017-04-09): abandoned at 0-0 in 37'

### 2018

- temporada abandonada pelo escândalo de corrupção na federação ganesa ("competition abandoned following corruption scandal within GFA"); a tabela é a do abandono
- ogol: 117 jogos casados (edição 122001 do ogol, 240 jogos)
- abandonado/suspenso, sem valer — Elmina Sharks Medeama (2018-04-18): abandoned at 0-0 in second half due
- não jogado — Aduana Stars Ebusua Dwarfs (2018-04-19)
- não jogado — Wa All Stars Aduana Stars (2018-05-03)
- não jogado — Aduana Stars Hearts of Oak (2018-05-06)

### 2019/20

- temporada abandonada pela Covid-19, sem campeão; a tabela é a do abandono
- ogol: 135 jogos casados (edição 140966 do ogol, 306 jogos)
- decidido fora de campo — Medeama Great Olympics (2020-03-02): awarded 0-3; originally 1-0,
- não jogado — Inter Allies Asante Kotoko (2020-03-15)
- não jogado — King Faisal Babes Hearts of Oak (2020-03-15)

### 2020/21

- ogol: 306 jogos casados (edição 148572 do ogol, 306 jogos)
- decidido fora de campo — Ebusua Dwarfs Legon Cities (2021-05-09): awarded 0-3; abandoned at 0-1 at half-time

### 2021/22

- ogol: 306 jogos casados (edição 159053 do ogol, 306 jogos)

### 2022/23

- ogol: 306 jogos casados (edição 167592 do ogol, 306 jogos)
- abandonado/suspenso, sem valer — Kotoku Royals Samartex (2022-11-16): abandoned at 0-0 in 68' due to heavy rain
- abandonado/suspenso, sem valer — Medeama Bibiani Gold Stars (2023-03-29): abandoned at 0-0 at half-time

### 2023/24

- ogol: 306 jogos casados (edição 188534 do ogol, 306 jogos)
- abandonado/suspenso, sem valer — Medeama Aduana Stars (2024-03-20): abandoned at 0-0 at half-time
- decidido fora de campo — Great Olympics Real Tamale United (2024-06-16): awarded 3-0, RTU forfeited

### 2024/25

- ogol: 306 jogos casados (edição 176681 do ogol, 306 jogos)
- abandonado/suspenso, sem valer — Aduana Stars Medeama (2024-10-27): abandoned at 2-2 in 87' due to
- decidido fora de campo — Basake Holy Stars Bechem United (2024-12-26): awarded 3-0, Bechem dns
- decidido fora de campo — Basake Holy Stars Nsoatreman (2025-03-16): awarded 3-0, Nsoatreman forfeited
- decidido fora de campo — Berekum Chelsea Nsoatreman (2025-03-19): awarded 3-0, Nsoatreman forfeited
- decidido fora de campo — Nsoatreman Heart of Lions (2025-03-24): awarded 0-3, Nsoatreman forfeited
- decidido fora de campo — Nsoatreman Accra Lions (2025-04-02): awarded 0-3, Nsoatreman forfeited
- decidido fora de campo — Bechem United Nsoatreman (2025-04-06): awarded 3-0, Nsoatreman forfeited
- decidido fora de campo — Nsoatreman Nations FC (2025-04-13): awarded 0-3, Nsoatreman forfeited
- decidido fora de campo — Legon Cities Nsoatreman (2025-04-16): awarded 3-0, Nsoatreman forfeited
- decidido fora de campo — Aduana Stars Nsoatreman (2025-04-20): awarded 3-0, Nsoatreman forfeited
- decidido fora de campo — Nsoatreman Hearts of Oak (2025-04-27): awarded 0-3, Nsoatreman forfeited
- decidido fora de campo — Dreams FC Nsoatreman (2025-05-04): awarded 3-0, Nsoatreman forfeited
- decidido fora de campo — Nsoatreman Bibiani Gold Stars (2025-05-18): awarded 0-3, Nsoatreman forfeited
- decidido fora de campo — Medeama Nsoatreman (2025-05-25): awarded 3-0, Nsoatreman forfeited
- decidido fora de campo — Basake Holy Stars Nations FC (2025-06-01): awarded 3-0, abandoned at 1-0 in 73',
- decidido fora de campo — Nsoatreman Vision FC (2025-06-01): awarded 0-3, Nsoatreman forfeited
- decidido fora de campo — Karela United Nsoatreman (2025-06-08): awarded 3-0, Nsoatreman forfeited

### 2025/26

- ogol: 306 jogos casados (edição 203534 do ogol, 306 jogos)
- abandonado/suspenso, sem valer — Young Apostles Dreams FC (2025-09-28): abandoned at 1-0 at half-time due to heavy rain
- abandonado/suspenso, sem valer — Medeama Aduana Stars (2026-02-13): abandoned at 1-1 in 77' due to heavy rain
- decidido fora de campo — Eleven Wonders Hohoe United (2026-04-03): awarded 3-0, Hohoe United withdrew
- abandonado/suspenso, sem valer — Asante Kotoko Samartex (2026-04-06): abandoned at 0-0 at half-time due to heavy rain
- decidido fora de campo — Hohoe United Bechem United (2026-04-12): awarded 0-3, Hohoe United withdrew
- decidido fora de campo — Hohoe United Berekum Chelsea (2026-05-03): awarded 0-3, Hohoe United withdrew
- decidido fora de campo — Asante Kotoko Hohoe United (2026-05-06): awarded 3-0, Hohoe United withdrew
- decidido fora de campo — Bibiani Gold Stars Hohoe United (2026-05-10): awarded 3-0, Hohoe United withdrew
- decidido fora de campo — Hohoe United Basake Holy Stars (2026-05-17): awarded 0-3, Hohoe United withdrew
- decidido fora de campo — Heart of Lions Hohoe United (2026-05-24): awarded 3-0, Hohoe United withdrew

