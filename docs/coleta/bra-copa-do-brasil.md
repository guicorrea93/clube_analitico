# Copa do Brasil — coleta de dados

Gerado por `python coleta/bra-copa-do-brasil/importar.py`. Pacote em `data/coleta/bra-copa-do-brasil/pacote/`. Método e
código iguais aos da Série C (`docs/coleta/bra-serie-c.md`).

**Edições:** 37, de 1989 a 2025, conferidas na RSSSF Brasil (cbrcamp.htm) e na Wikipédia em português (artigo da Copa do
Brasil). A Taça Brasil (1959-1968) não entra: já está no banco como parte da Série A.

**Fontes:** RSSSF Brasil (`cbr{ano}.htm`: jogos, fases, datas e autores; tabelas, quando há fase de grupos); ogol
(calendário de todas as edições e o código de cada clube; confere placares e completa jogos); Wikipédia (lista de campeões).

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,
fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` ou nos pacotes
das Séries C e D usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).

**Fases (revisão CB-001 a CB-003, CB-014):** a Copa é mata-mata, e as fases saem da própria chave, não dos títulos das
páginas: a final é o último confronto; a fase anterior são os confrontos anteriores de cada clube da fase seguinte. Nomes de
trás para frente (Final, Semifinal, Quartas e Oitavas de final); as fases antes delas contam do começo (Primeira fase,
Segunda fase...), e a primeira, quando tem até um quarto dos confrontos da seguinte, é a Fase preliminar. Sem grupos.

**Mando (revisão CB-006):** quando RSSSF e ogol têm o mesmo jogo com o mando invertido e o placar espelhado (mesmo dia, ou
até 10 dias de diferença), vale o ogol: a RSSSF escreve o confronto do ponto de vista de um dos clubes, nem sempre o mandante.

| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|---|
| 1989 | RSSSF + ogol | 32 | 61 (62) | 137 | 7 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1990 | RSSSF + ogol | 32 | 62 (62) | 119 | 0 | 0 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1991 | RSSSF + ogol | 32 | 62 (62) | 128 | 0 | 0 / 0 | Criciúma | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1992 | RSSSF + ogol | 32 | 62 (62) | 165 | 0 | 0 / 0 | Internacional | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1993 | RSSSF + ogol | 32 | 62 (62) | 180 | 0 | 0 / 0 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1994 | RSSSF + ogol | 32 | 62 (62) | 149 | 0 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1995 | RSSSF + ogol | 36 | 69 (70) | 167 | 0 | 0 / 0 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1996 | RSSSF + ogol | 40 | 70 (78) | 187 | 0 | 0 / 0 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1997 | RSSSF + ogol | 44 | 78 (86) | 267 | 0 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1998 | RSSSF + ogol | 41 | 75 (82) | 233 | 0 | 0 / 0 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1999 | RSSSF + ogol | 65 | 117 (126) | 371 | 0 | 0 / 0 | Juventude | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2000 | RSSSF + ogol | 69 | 129 (136) | 385 | 0 | 0 / 0 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2001 | RSSSF + ogol | 64 | 117 (126) | 371 | 0 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2002 | RSSSF + ogol | 64 | 117 (126) | 369 | 0 | 0 / 0 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2003 | RSSSF + ogol | 64 | 117 (126) | 350 | 230 | 0 / 0 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2004 | RSSSF + ogol | 64 | 114 (126) | 325 | 209 | 0 / 0 | Santo André | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2005 | RSSSF + ogol | 64 | 117 (126) | 331 | 235 | 0 / 0 | Paulista | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2006 | RSSSF + ogol | 64 | 113 (126) | 350 | 226 | 0 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2007 | RSSSF + ogol | 64 | 115 (126) | 327 | 252 | 0 / 0 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2008 | RSSSF + ogol | 64 | 110 (126) | 342 | 225 | 0 / 0 | Sport | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2009 | RSSSF + ogol | 64 | 115 (126) | 315 | 227 | 0 / 0 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2010 | RSSSF + ogol | 64 | 116 (126) | 340 | 238 | 0 / 0 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2011 | RSSSF + ogol | 64 | 111 (126) | 315 | 223 | 0 / 0 | Vasco | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2012 | RSSSF + ogol | 64 | 112 (126) | 319 | 213 | 0 / 0 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2013 | RSSSF + ogol | 87 | 158 (172) | 364 | 257 | 0 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2014 | RSSSF + ogol | 87 | 159 (172) | 435 | 262 | 0 / 0 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2015 | RSSSF + ogol | 87 | 158 (172) | 417 | 278 | 0 / 0 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2016 | RSSSF + ogol | 86 | 162 (170) | 370 | 256 | 0 / 0 | Grêmio | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2017 | RSSSF + ogol | 91 | 120 (120) | 282 | 228 | 0 / 0 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2018 | RSSSF + ogol | 91 | 120 (120) | 253 | 220 | 0 / 0 | Cruzeiro | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2019 | RSSSF + ogol | 91 | 120 (120) | 270 | 258 | 30 / 0 | Athletico-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2020 | RSSSF + ogol | 91 | 120 (120) | 265 | 265 | 0 / 0 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2021 | RSSSF + ogol | 92 | 122 (122) | 299 | 299 | 0 / 0 | Atlético-MG | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2022 | RSSSF + ogol | 92 | 122 (122) | 281 | 281 | 0 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2023 | RSSSF + ogol | 92 | 122 (122) | 304 | 291 | 0 / 0 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2024 | RSSSF + ogol | 92 | 122 (122) | 267 | 252 | 0 / 0 | Flamengo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2025 | RSSSF + ogol | 92 | 122 (122) | 290 | 286 | 31 / 0 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |

## Conferência e correções, ano a ano

### 1989

- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Flamengo 3-1 Blumenau, ogol Blumenau 1-3 Flamengo (1989-07-26)
- mando invertido no ogol — RSSSF Blumenau 1-3 Flamengo (1989-07-26), ogol Flamengo 3-1 Blumenau (1989-07-29); fica o ogol
- jogo só no ogol, incluído em Primeira fase: Internacional 0-0 CSA (1989-07-19)
- jogo só no ogol, incluído em Primeira fase: CSA 0-2 Internacional (1989-07-22)
- jogo só no ogol, incluído em First Round: Corinthians 5-0 Tiradentes-DF (1989-07-26)
- jogo só no ogol, incluído em First Round: Mixto 0-5 Grêmio (1989-07-26)
- jogo só no ogol, incluído em First Round: Tiradentes-DF 1-0 Corinthians (1989-07-29)
- jogo só no ogol, incluído em Semifinals: Sport 0-0 Grêmio (1989-08-26)
- jogo só no ogol, incluído em Semifinals: Grêmio 2-1 Sport (1989-09-02)
- fases pela chave do mata-mata (Primeira fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round → Primeira fase (30); Segunda fase → Oitavas de final (12); First Round → Oitavas de final (3); Semifinal → Final (2)

### 1990

- volta Santa Cruz x América-RN (27/06): a RSSSF e o ogol dão América-RN 1-0; o Bola n@ Área, o Futebol Nacional e a Wikipédia (que cita o Bola) dão 0-1; fica o do pacote até um jornal da época (decisão D-13, revisão CB-005)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Goiás x Criciúma, ogol 1990-09-26); fica a do ogol
- jogo só no ogol, incluído em First Round: Santa Cruz 0-0 Remo (1990-07-11)
- jogo só no ogol, incluído em First Round: Remo 1-0 Santa Cruz (1990-08-10)
- jogo só no ogol, incluído em Semi-Finals: Flamengo 1-0 Goiás (1990-11-01)
- jogo só no ogol, incluído em Semi-Finals: Goiás 0-0 Flamengo (1990-11-08)
- 3 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- jogo corrigido à mão — Goiás x Flamengo: o ogol dá o dia seguinte (jogo à noite no Brasil); data da Wikipédia pt e en (revisão CB-010)
- fases pela chave do mata-mata (Primeira fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round → Primeira fase (32); Segunda fase → Oitavas de final (14); First Round → Oitavas de final (2); Semifinal → Final (2)

### 1991

- quartas Vitória x Remo (25/04): o pacote, a RSSSF, o ogol e a Wikipédia en dão 0-0; o Bola, o FN e a pt dão 2-2; fica o do pacote até um jornal da época (D-13, CB-005)
- o Grêmio venceu o Auto Esporte e o Fluminense de Feira pelos mesmos placares; o Fluminense(BA) da página é ligado à mão ao Fluminense de Feira do ogol
- placar diferente no ogol — Remo x Vasco (1991-03-14): RSSSF 1-1, ogol 0-0; fica o do ogol
- placar diferente no ogol — Vasco x Remo (1991-03-21): RSSSF 0-0, ogol 1-1; fica o do ogol
- data diferente entre RSSSF e ogol (mais de 3 dias) em 10 jogos (ex.: Botafogo x Santa Cruz, ogol 1991-03-17); fica a do ogol
- jogo só no ogol, incluído em First Round: Corinthians 3-1 Cruzeiro (1991-03-22)
- jogo só no ogol, incluído em First Round: Cruzeiro 0-1 Corinthians (1991-04-11)
- jogo só no ogol, incluído em Semi-Finals: Grêmio 1-1 Criciúma (1991-05-30)
- jogo só no ogol, incluído em Semi-Finals: Criciúma 0-0 Grêmio (1991-06-02)
- 1 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round → Primeira fase (32); Segunda fase → Oitavas de final (14); First Round → Oitavas de final (2); Semifinal → Final (2)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Criciúma

### 1992

- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Internacional 1-1 Grêmio, ogol Grêmio 1-1 Internacional (1992-11-06)
- mando invertido no ogol — RSSSF Grêmio 1-1 Internacional (1992-11-17), ogol Internacional 1-1 Grêmio (1992-11-20); fica o ogol
- jogo só no ogol, incluído em Semi-Finals: Fluminense 2-1 Internacional (1992-12-10)
- jogo só no ogol, incluído em Semi-Finals: Internacional 1-0 Fluminense (1992-12-13)
- 2 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round → Primeira fase (32); Segunda fase → Oitavas de final (16); Semifinal → Final (2)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Internacional

### 1993

- placar diferente no ogol — 4 de Julho x Palmeiras (1993-03-02): RSSSF 0-3, ogol 0-2; fica o do ogol
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Londrina x Operário-MS, ogol 1993-03-19); fica a do ogol
- jogo só no ogol, incluído em Primeira fase: Taguatinga 1-4 Sport (1993-03-05)
- jogo só no ogol, incluído em Primeira fase: Sport 3-0 Taguatinga (1993-03-12)
- jogo só no ogol, incluído em Primeira fase: Desportiva-ES 1-1 Cruzeiro (1993-03-16)
- jogo só no ogol, incluído em Primeira fase: Cruzeiro 5-0 Desportiva-ES (1993-03-19)
- jogo só no ogol, incluído em First Round: Palmeiras 3-0 4 de Julho (1993-04-06)
- jogo só no ogol, incluído em Semi-Finals: Grêmio 0-0 Cruzeiro (1993-05-30)
- jogo só no ogol, incluído em Semi-Finals: Cruzeiro 2-1 Grêmio (1993-06-03)
- 1 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round → Primeira fase (28); Segunda fase → Oitavas de final (16); Semifinal → Final (2)

### 1994

- vários jogos da página vêm com a data do título da fase (março), quando foram jogados em maio; casados com o ogol pelo par de clubes e pelo placar, e vale a data do ogol
- placar diferente no ogol — 4 de Julho x Palmeiras (1994-02-08): RSSSF 2-5, ogol 1-3; fica o do ogol
- data diferente entre RSSSF e ogol (mais de 3 dias) em 8 jogos (ex.: Vitória x SE Ariquemes, ogol 1994-04-26); fica a do ogol
- jogo só no ogol, incluído em Primeira fase: Fluminense 2-2 Linhares EC (1994-02-18)
- jogo só no ogol, incluído em First Round: Palmeiras 5-2 4 de Julho (1994-02-25)
- jogo só no ogol, incluído em Primeira fase: Taguatinga 0-2 Bahia (1994-03-15)
- jogo só no ogol, incluído em Primeira fase: Linhares EC 1-1 Fluminense (1994-03-18)
- jogo só no ogol, incluído em Primeira fase: Bahia 2-1 Taguatinga (1994-03-25)
- jogo só no ogol, incluído em First Round: Santa Cruz 1-0 Vasco (1994-05-10)
- jogo só no ogol, incluído em First Round: Vasco 3-1 Santa Cruz (1994-05-27)
- jogo só no ogol, incluído em Second Round(1/8 Finals): Linhares EC 1-0 Comercial-MS (1994-06-05)
- jogo só no ogol, incluído em Second Round(1/8 Finals): Comercial-MS 1-1 Linhares EC (1994-06-12)
- jogo só no ogol, incluído em Semi-Finals: Ceará 0-0 Grêmio (1994-08-07)
- jogo só no ogol, incluído em Semi-Finals: Grêmio 1-0 Ceará (1994-08-10)
- 2 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round → Primeira fase (28); Segunda fase → Oitavas de final (14); First Round → Oitavas de final (2); Segunda fase → Quartas de final (2); Semifinal → Final (2)

### 1995

- placar diferente no ogol — Nacional-AM x Cristal (1995-03-19): RSSSF 1-0, ogol 2-0; fica o do ogol
- data diferente entre RSSSF e ogol (mais de 3 dias) em 12 jogos (ex.: Remo x São Paulo, ogol 1995-04-18); fica a do ogol
- jogo só no ogol, incluído em Primeira fase: Desportiva-ES 0-1 Grêmio (1995-02-14)
- jogo só no ogol, incluído em Primeira fase: Maranhão 0-0 Kaburé (1995-02-15)
- jogo só no ogol, incluído em Primeira fase / Grupo 1PE: Democrata-GV 2-0 Goiás (1995-02-17)
- jogo só no ogol, incluído em Primeira fase: Kaburé 2-0 Maranhão (1995-02-21)
- jogo só no ogol, incluído em Primeira fase / Grupo 1PE: Goiás 1-0 Democrata-GV (1995-03-03)
- jogo só no ogol, incluído em Primeira fase: CEOV Operário 1-1 Corinthians (1995-03-03)
- jogo só no ogol, incluído em Primeira fase: Democrata-GV 3-2 Vitória (1995-03-10)
- jogo só no ogol, incluído em Primeira fase: Flamengo-PI 1-2 Vasco (1995-03-10)
- jogo só no ogol, incluído em Primeira fase: Atlético-MG 1-0 Sport (1995-03-17)
- jogo só no ogol, incluído em Primeira fase: Pontaporanense 0-2 Internacional (1995-03-21)
- jogo só no ogol, incluído em Primeira fase: Internacional 5-0 Pontaporanense (1995-03-24)
- jogo só no ogol, incluído em Primeira fase: Grêmio 2-1 Desportiva-ES (1995-03-28)
- jogo só no ogol, incluído em Primeira fase: Sport 2-2 Atlético-MG (1995-03-28)
- jogo só no ogol, incluído em Primeira fase: Corinthians 4-0 CEOV Operário (1995-03-28)
- jogo só no ogol, incluído em Primeira fase: Vitória 2-0 Democrata-GV (1995-03-28)
- jogo só no ogol, incluído em Primeira fase: Vasco 4-1 Flamengo-PI (1995-03-30)
- jogo só no ogol, incluído em Semi-Finals: Corinthians 2-1 Grêmio (1995-06-14)
- jogo só no ogol, incluído em Semi-Finals: Grêmio 0-1 Corinthians (1995-06-21)
- 2 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- jogo corrigido à mão — Nacional-AM x Cristal: RSSSF, Bola n@ Área e Wikipédias pt e en: 1-0 (o ogol dá 2-0; revisão QC-005)
- fases pela chave do mata-mata (Fase preliminar 4 / Primeira fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round → Primeira fase (17); Segunda fase → Oitavas de final (16); Preliminary Round → Fase preliminar (6); Primeira fase → Fase preliminar (2); Semifinal → Final (2)

### 1996

- data diferente entre RSSSF e ogol (mais de 3 dias) em 17 jogos (ex.: Grêmio x Operário-MS, ogol 1996-03-05); fica a do ogol
- jogo só no ogol, incluído em First Round (1/16 Finals): Vasco 2-6 Cruzeiro (1996-03-28)
- jogo só no ogol, incluído em First Round (1/16 Finals): Cruzeiro 1-1 Vasco (1996-04-17)
- 1 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 8 / Segunda fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: Final → Segunda fase (27); Preliminary Round → Primeira fase (14); Final → Oitavas de final (2)

### 1997

- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Palmeiras x Flamengo, ogol 1997-05-13); fica a do ogol
- 2 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 12 / Segunda fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: Final → Segunda fase (29); Preliminary Round → Primeira fase (19); Segunda fase → Oitavas de final (16)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Grêmio

### 1998

- placar diferente no ogol — Bahia x Botafogo-PB (1998-02-18): RSSSF 1-2, ogol 2-1; fica o do ogol
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: EC Operário-MT x Vitória, ogol 1998-02-04); fica a do ogol
- adversário diferente no ogol — RSSSF EC Operário-MT 0-0 Flamengo, ogol Operário-MS 0-0 Flamengo (1998-01-20); fica a RSSSF
- adversário diferente no ogol — RSSSF Flamengo 4-0 EC Operário-MT, ogol Flamengo 4-0 Operário-MS (1998-02-06); fica a RSSSF
- 1 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- jogo corrigido à mão — Bahia x Botafogo-PB: RSSSF, Bola n@ Área e Wikipédias pt e en: 1-2; o Bahia passou pelo gol fora (4-4) (o ogol dá 2-1; revisão QC-005)
- fases pela chave do mata-mata (Primeira fase 10 / Segunda fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round → Segunda fase (26); Preliminary Round → Primeira fase (19); Segunda fase → Oitavas de final (16)

### 1999

- data com dia e mês trocados na RSSSF em 14 jogos (ex.: Comercial-MS x Criciúma); fica a data do ogol
- data diferente entre RSSSF e ogol (mais de 3 dias) em 15 jogos (ex.: CSA x São Paulo, ogol 1999-02-18); fica a do ogol
- 4 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 32 / Segunda fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round → Primeira fase (56); Third Round → Oitavas de final (16)
- jogo que faltava: Náutico 0-1 Santa Cruz (1999-01-28, Fase preliminar) — preliminar Náutico 0-1 Santa Cruz, pelo Futebol Nacional (data e mando; a Wikipédia pt dá Santa Cruz 1-0); a RSSSF, o ogol e o Bola n@ Área não têm o jogo (decisão D-14 C, revisão CB-007)

### 2000

- as oitavas vêm com uma letra antes de cada confronto ('E ABC (RN) x Palmeiras (SP)'); a letra sai
- placar diferente no ogol — Nacional-AM x Rio Negro-AM (2000-03-22): RSSSF 1-1, ogol 2-2; fica o do ogol
- placar diferente no ogol — Fluminense x Santa Cruz (2000-04-27): RSSSF 3-2, ogol 3-1; fica o do ogol
- jogo só no ogol, incluído em Primeira fase: 4 de Julho 2-1 Fortaleza (2000-03-22)
- jogo só no ogol, incluído em First Round: Sport 0-1 América-RN (2000-03-29)
- jogo só no ogol, incluído em Primeira fase: Fortaleza 3-1 4 de Julho (2000-03-29)
- jogo só no ogol, incluído em First Round: Rio Negro-AM 1-1 Nacional-AM (2000-03-30)
- jogo só no ogol, incluído em Second Round: Goiás 1-1 Náutico (2000-04-19)
- jogo só no ogol, incluído em Third Round: Goiás 1-1 ABC (2000-05-03)
- jogo só no ogol, incluído em 1/8 Finals: Atlético-MG 0-0 Portuguesa (2000-05-31)
- 5 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 20 / Segunda fase 22 / Terceira fase 11 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round → Primeira fase (36); Third Round → Terceira fase (22); Quartas de final → Semifinal (4)

### 2001

- a página começa com a seletiva do Espírito Santo, que não é Copa do Brasil; esse trecho fica de fora
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Remo 1-0 Santos-AP, ogol Santos-AP 0-1 Remo (2001-03-14)
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Santos-AP 0-3 Remo, ogol Remo 3-0 Santos-AP (2001-03-22)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 12 jogos (ex.: Mixto x URT, ogol 2001-03-14); fica a do ogol
- ida e volta de URT x Mixto vinham com a mesma data (2001-03-14); ficam 2001-03-14, 2001-03-21 (da página)
- ida e volta de Comercial-MS x Juventude vinham com a mesma data (2001-03-14); ficam 2001-03-14, 2001-03-21 (da página)
- ida e volta de Villa Nova-MG x Grêmio vinham com a mesma data (2001-03-14); ficam 2001-03-14, 2001-03-21 (da página)
- ida e volta de Guajará x Rio Branco-AC vinham com a mesma data (2001-03-14); ficam 2001-03-14, 2001-03-21 (da página)
- ida e volta de Ceará x Paraná vinham com a mesma data (2001-03-14); ficam 2001-03-14, 2001-03-21 (da página)
- ida e volta de Goiânia x América-MG vinham com a mesma data (2001-03-14); ficam 2001-03-14, 2001-03-21 (da página)
- ida e volta de Rio Negro-RR x São Raimundo vinham com a mesma data (2001-03-14); ficam 2001-03-14, 2001-03-21 (da página)
- ida e volta de Sergipe x Botafogo vinham com a mesma data (2001-03-14); ficam 2001-03-14, 2001-03-21 (da página)
- ida e volta de Palmas x Gama vinham com a mesma data (2001-03-14); ficam 2001-03-14, 2001-03-21 (da página)
- ida e volta de Castanhal x Ponte Preta vinham com a mesma data (2001-03-14); ficam 2001-03-14, 2001-03-21 (da página)
- 2 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 32 / Segunda fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round → Primeira fase (58); Third Round → Oitavas de final (16)

### 2002

- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Náutico 2-2 Remo, ogol Remo 2-2 Náutico (2002-01-23)
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Remo 3-4 Náutico, ogol Náutico 4-3 Remo (2002-02-06)
- placar diferente no ogol — América-RN x São Raimundo (2002-02-20): RSSSF 4-0, ogol 3-0; fica o do ogol
- fases pela chave do mata-mata (Primeira fase 32 / Segunda fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: Terceira fase → Oitavas de final (16); Terceira fase → Quartas de final (8)

### 2003

- a página começa com o jogo seletivo Paraná x Coritiba, que não é Copa do Brasil; fica de fora
- 3 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 32 / Segunda fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round → Primeira fase (56); Third Round → Oitavas de final (16)

### 2004

- jogo só no ogol, incluído em Primeira fase: 15 de Novembro 1-1 Portuguesa Santista (2004-02-18)
- jogo só no ogol, incluído em Primeira fase: CENE 1-0 União Barbarense (2004-02-18)
- jogo só no ogol, incluído em Primeira fase: Portuguesa Santista 2-2 15 de Novembro (2004-03-03)
- jogo só no ogol, incluído em Primeira fase: União Barbarense 1-0 CENE (2004-03-03)
- jogo só no ogol, incluído em Segunda fase: 15 de Novembro 1-1 Vasco (2004-03-17)
- jogo só no ogol, incluído em Segunda fase: Vasco 0-3 15 de Novembro (2004-04-07)
- jogo só no ogol, incluído em Oitavas de final: Americano-RJ 1-2 15 de Novembro (2004-04-14)
- jogo só no ogol, incluído em Oitavas de final: 15 de Novembro 3-2 Americano-RJ (2004-05-05)
- jogo só no ogol, incluído em Quartas de final: 15 de Novembro 3-0 Palmas (2004-05-12)
- jogo só no ogol, incluído em Quartas de final: Palmas 0-1 15 de Novembro (2004-05-19)
- jogo só no ogol, incluído em Semifinal: Santo André 3-4 15 de Novembro (2004-05-27)
- jogo só no ogol, incluído em Semifinal: 15 de Novembro 1-3 Santo André (2004-06-10)
- 1 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 32 / Segunda fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: Terceira fase → Oitavas de final (14); Semifinal → Final (2)

### 2005

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Palmas x Náutico, ogol 2005-02-16); fica a do ogol
- jogo só no ogol, incluído em Primeira fase: 4 de Julho 0-0 Ceará (2005-02-02)
- jogo só no ogol, incluído em Primeira fase: Hermann Aichinger 0-0 Ituano (2005-02-16)
- jogo só no ogol, incluído em Primeira fase: Ceará 3-2 4 de Julho (2005-02-16)
- jogo só no ogol, incluído em First Round: América-MG 2-1 Baraúnas (2005-02-16)
- 1 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 32 / Segunda fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round → Primeira fase (55); Third Round → Oitavas de final (16)

### 2006

- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Potiguar x Santo André, ogol 2006-02-22); fica a do ogol
- jogo só no ogol, incluído em Primeira fase: 15 de Novembro 4-1 Noroeste (2006-02-22)
- jogo só no ogol, incluído em Primeira fase: Noroeste 2-0 15 de Novembro (2006-03-08)
- jogo só no ogol, incluído em Segunda fase: 15 de Novembro 1-0 Grêmio (2006-03-16)
- jogo só no ogol, incluído em Segunda fase: Grêmio 1-0 15 de Novembro (2006-03-23)
- jogo só no ogol, incluído em Oitavas de final: Volta Redonda 1-0 15 de Novembro (2006-04-12)
- jogo só no ogol, incluído em Oitavas de final: 15 de Novembro 2-1 Volta Redonda (2006-04-19)
- 3 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 32 / Segunda fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round → Primeira fase (53); First Round → Segunda fase (26); Third Round → Oitavas de final (14)

### 2007

- jogo anulado fica de fora (1): Rio Branco(PR) 3-0 Villa Nova(MG) — erro da página: na 2ª fase o Villa Nova enfrentou o Avaí (revisão CB-007)
- placar diferente no ogol — Baré x América-RN (2007-02-14): RSSSF 0-1, ogol 1-0; fica o do ogol
- 4 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 32 / Segunda fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round (14/02 to 01/03) → Primeira fase (55); Third Round → Oitavas de final (16)

### 2008

- data diferente entre RSSSF e ogol (mais de 3 dias) em 6 jogos (ex.: CENE x Palmeiras, ogol 2008-02-13); fica a do ogol
- jogo só no ogol, incluído em First Round (13/02 to 05/03): Juventude 0-0 Linhares FC (2008-02-28)
- jogo só no ogol, incluído em First Round (13/02 to 05/03): ABC 1-1 Madureira (2008-03-06)
- jogo só no ogol, incluído em First Round (13/02 to 05/03): Athletico-PR 1-1 Corinthians-AL (2008-03-07)
- jogo só no ogol, incluído em Second Round (19/03 to 09/04): Grêmio 2-1 Atlético-GO (2008-04-10)
- jogo só no ogol, incluído em Second Round (19/03 to 09/04): Corinthians 2-1 Botafogo (2008-05-29)
- jogo só no ogol, incluído em Second Round (19/03 to 09/04): Vasco 2-0 Sport (2008-05-29)
- 6 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 32 / Segunda fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round (13/02 to 05/03) → Primeira fase (53); Segunda fase → Oitavas de final (16); Segunda fase → Quartas de final (8); Segunda fase → Semifinal (4)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Sport
- 1 datas corrigidas (datas_corrigidas.csv; ex.: Corinthians x Botafogo 2008-05-29 -> 2008-05-28, Bola n@ Área e transfermarkt (QC-004))

### 2009

- 6 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 32 / Segunda fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round (18/02 to 19/03) → Primeira fase (56); First Round (18/02 to 19/03) → Segunda fase (29); First Round (18/02 to 19/03) → Oitavas de final (16); First Round (18/02 to 19/03) → Quartas de final (8)

### 2010

- 2 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 32 / Segunda fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round (10/02 to 10/03) → Primeira fase (56); Segunda fase → Oitavas de final (16)

### 2011

- jogo só no ogol, incluído em First Round (16/02 to 03/03): Botafogo 1-0 River Plate-SE (2011-03-02)
- 1 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 32 / Segunda fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round (16/02 to 03/03) → Primeira fase (54); First Round (16/02 to 03/03) → Segunda fase (27); First Round (16/02 to 03/03) → Oitavas de final (16); First Round (16/02 to 03/03) → Quartas de final (8)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Vasco

### 2012

- jogo só no ogol, incluído em Primeira fase: 4 de Julho 0-2 Sport (2012-03-15)
- 3 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 32 / Segunda fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round (07/03 to 22/03) → Primeira fase (52); First Round (07/03 to 22/03) → Segunda fase (29); First Round (07/03 to 22/03) → Oitavas de final (16); First Round (07/03 to 22/03) → Quartas de final (8); First Round (07/03 to 22/03) → Semifinal (4); First Round (07/03 to 22/03) → Final (2)

### 2013

- placar diferente no ogol — ASA x Flamengo (2013-07-10): RSSSF 0-1, ogol 0-2; fica o do ogol
- 7 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Fase preliminar 1 / Primeira fase 40 / Segunda fase 20 / Terceira fase 10 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round (03/04 to 25/04) → Primeira fase (69); First Round (03/04 to 25/04) → Segunda fase (37); First Round (03/04 to 25/04) → Terceira fase (20); First Round (03/04 to 25/04) → Oitavas de final (16); First Round (03/04 to 25/04) → Quartas de final (8); First Round (03/04 to 25/04) → Semifinal (4); Preliminary Phase → Fase preliminar (2)

### 2014

- placar diferente no ogol — Treze x Vasco (2014-04-30): RSSSF 2-1, ogol 1-2; fica o do ogol
- placar diferente no ogol — América-RN x Fluminense (2014-08-06): RSSSF 0-2, ogol 0-3; fica o do ogol
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Londrina x Criciúma, ogol 2014-03-19); fica a do ogol
- jogo só no ogol, incluído em Primeira fase: Princesa 3-1 Brasiliense (2014-04-17)
- jogo só no ogol, incluído em Primeira fase: Brasiliense 4-2 Princesa (2014-04-24)
- jogo só no ogol, incluído em Third Round: Atlético-MG 2-0 Cruzeiro (2014-11-13)
- jogo só no ogol, incluído em Third Round: Cruzeiro 0-1 Atlético-MG (2014-11-27)
- 5 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- jogo corrigido à mão — Atlético-MG x Cruzeiro: o ogol dá o dia seguinte (jogo à noite no Brasil); data da Wikipédia pt e en (revisão CB-010)
- jogo corrigido à mão — Cruzeiro x Atlético-MG: o ogol dá o dia seguinte (jogo à noite no Brasil); data da Wikipédia pt e en (revisão CB-010)
- fases pela chave do mata-mata (Fase preliminar 1 / Primeira fase 40 / Segunda fase 20 / Terceira fase 10 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round (03/04 to 25/04) → Primeira fase (69); First Round (03/04 to 25/04) → Segunda fase (37); Third Round → Terceira fase (20); Third Round → Oitavas de final (15); Third Round → Quartas de final (8); Third Round → Semifinal (4); Preliminary Phase → Fase preliminar (2); Third Round → Final (2)
- 5 datas corrigidas (datas_corrigidas.csv; ex.: Naviraiense x Avaí 2014-04-02 -> 2014-04-03, Bola n@ Área e transfermarkt (QC-004))

### 2015

- nesta página o primeiro clube de cada confronto costuma mandar a volta, mas não sempre (na final, Santos mandou a ida); o leitor inverte o mando, e onde o ogol tem o mesmo jogo com o mando ao contrário vale o ogol (quartas, semifinal e final)
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Vasco 0-3 São Paulo, ogol São Paulo 3-0 Vasco (2015-09-24)
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF São Paulo 1-1 Vasco, ogol Vasco 1-1 São Paulo (2015-10-01)
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Santos 1-0 Figueirense, ogol Figueirense 0-1 Santos (2015-09-23)
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Figueirense 2-3 Santos, ogol Santos 3-2 Figueirense (2015-10-02)
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Palmeiras 1-1 Internacional, ogol Internacional 1-1 Palmeiras (2015-09-23)
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Internacional 2-3 Palmeiras, ogol Palmeiras 3-2 Internacional (2015-10-01)
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Grêmio 0-0 Fluminense, ogol Fluminense 0-0 Grêmio (2015-09-24)
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Fluminense 1-1 Grêmio, ogol Grêmio 1-1 Fluminense (2015-10-01)
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Santos 3-1 São Paulo, ogol São Paulo 1-3 Santos (2015-10-22)
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF São Paulo 1-3 Santos, ogol Santos 3-1 São Paulo (2015-10-29)
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Palmeiras 1-2 Fluminense, ogol Fluminense 2-1 Palmeiras (2015-10-22)
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Fluminense 1-2 Palmeiras, ogol Palmeiras 2-1 Fluminense (2015-10-29)
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Palmeiras 0-1 Santos, ogol Santos 1-0 Palmeiras (2015-11-26)
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Santos 1-2 Palmeiras, ogol Palmeiras 2-1 Santos (2015-12-03)
- placar diferente no ogol — Paysandu x Águia Negra (2015-04-01): RSSSF 0-2, ogol 2-0; fica o do ogol
- placar diferente no ogol — Tupi x Ceará (2015-07-22): RSSSF 2-1, ogol 1-2; fica o do ogol
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Independente Tucuruí x Goiás, ogol 2015-05-07); fica a do ogol
- jogo só no ogol, incluído em Primeira fase: Princesa 2-2 Figueirense (2015-03-19)
- jogo só no ogol, incluído em Primeira fase: Figueirense 2-1 Princesa (2015-04-01)
- 9 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- jogo corrigido à mão — Santos x Palmeiras: o ogol dá o dia seguinte (jogo à noite no Brasil); data da Wikipédia pt e en (revisão CB-010)
- jogo corrigido à mão — Palmeiras x Santos: o ogol dá o dia seguinte (jogo à noite no Brasil); data da Wikipédia pt e en (revisão CB-010)
- fases pela chave do mata-mata (Fase preliminar 1 / Primeira fase 40 / Segunda fase 20 / Terceira fase 10 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round → Primeira fase (68); First Round → Segunda fase (36); Third Round → Terceira fase (20); Third Round → Oitavas de final (16); Quartas de final → Semifinal (4); Preliminary Phase → Fase preliminar (2)
- 12 datas corrigidas (datas_corrigidas.csv; ex.: Princesa x Figueirense 2015-03-19 -> 2015-03-18, Bola n@ Área e transfermarkt (QC-004))

### 2016

- mesmo caso de 2015; na final, a volta vem na página em 30/11 e no ogol em 07/12 (Grêmio 1-1 Atlético-MG): vale o ogol
- mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF Grêmio 3-1 Atlético-MG, ogol Atlético-MG 1-3 Grêmio (2016-11-23)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Juazeirense x Cuiabá, ogol 2016-04-07); fica a do ogol
- mando invertido no ogol — RSSSF Atlético-MG 1-1 Grêmio (2016-11-30), ogol Grêmio 1-1 Atlético-MG (2016-12-07); fica o ogol
- jogo só no ogol, incluído em Primeira fase: Princesa 1-2 Chapecoense (2016-04-06)
- jogo só no ogol, incluído em Primeira fase: Chapecoense 2-0 Princesa (2016-04-15)
- 6 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 40 / Segunda fase 20 / Terceira fase 10 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round (16/03 to 25/05) → Primeira fase (73); First Round (16/03 to 25/05) → Segunda fase (37); Third Round (06 to 27/07) → Terceira fase (20); Third Round (06 to 27/07) → Oitavas de final (16); Third Round (06 to 27/07) → Quartas de final (8)

### 2017

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Sinop x Fluminense, ogol 2017-03-01); fica a do ogol
- 12 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 40 / Segunda fase 20 / Terceira fase 10 / Quarta fase 5 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round (08 to 15/02) → Primeira fase (40); First Round (08 to 15/02) → Segunda fase (20); First Round (08 to 15/02) → Terceira fase (20); First Round (08 to 15/02) → Quarta fase (10)

### 2018

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Grêmio x Goiás, ogol 2018-05-09); fica a do ogol
- jogo só no ogol, incluído em 1/8 Finals: Palmeiras 1-1 América-MG (2018-05-24)
- 11 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 40 / Segunda fase 20 / Terceira fase 10 / Quarta fase 5 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: First Round → Primeira fase (40); First Round → Segunda fase (20); Third Round → Terceira fase (20); Fourth Round → Quarta fase (10)
- 1 datas corrigidas (datas_corrigidas.csv; ex.: Palmeiras x América-MG 2018-05-24 -> 2018-05-23, Bola n@ Área e transfermarkt (QC-004))

### 2019

- jogo anulado fica de fora (1): Aparecidense/GO 1-0 Ponte Preta/SP — jogo anulado pelo STJD; vale o 2-0 de 03/04 (revisão CB-007)
- 60 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência
- fases pela chave do mata-mata (Primeira fase 40 / Segunda fase 20 / Terceira fase 10 / Quarta fase 5 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: Fifth Phase → Oitavas de final (16); Sixth Phase → Quartas de final (8)

### 2020

- fases pela chave do mata-mata (Primeira fase 40 / Segunda fase 20 / Terceira fase 10 / Quarta fase 5 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: 5a Fase → Oitavas de final (16); 4a Fase → Quarta fase (10)

### 2021

- jogo da página corrigido — CRB-AL 0-0 Cuiabá-MT (2021-03-16) vira Sergipe-SE 0-0 Cuiabá-MT: o jogo foi Sergipe 0-0 Cuiabá, como no ogol; o CRB jogou a 1ª fase com o Goianésia (revisão CB-007)
- fases pela chave do mata-mata (Primeira fase 40 / Segunda fase 20 / Terceira fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: 4a Fase → Oitavas de final (16); 5a Fase → Quartas de final (8)

### 2022

- 1 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)

### 2023

- jogo só no ogol, incluído em 2a Fase: Botafogo-SP 0-2 Santos (2023-04-11)
- 15 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 40 / Segunda fase 20 / Terceira fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: Segunda fase → Terceira fase (32); Quartas de final → Semifinal (4)

### 2024

- 12 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- fases pela chave do mata-mata (Primeira fase 40 / Segunda fase 20 / Terceira fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: Quarta fase → Oitavas de final (16); FIFTH STAGE → Quartas de final (8)
- 1 datas corrigidas (datas_corrigidas.csv; ex.: Fluminense-PI x Fortaleza 2024-03-04 -> 2024-03-03, Bola n@ Área e transfermarkt (QC-004))

### 2025

- 60 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência
- fases pela chave do mata-mata (Primeira fase 40 / Segunda fase 20 / Terceira fase 16 / Oitavas de final 8 / Quartas de final 4 / Semifinal 2 / Final 1 confrontos); mudaram: Final → Oitavas de final (16)

## Identidade dos clubes

- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.
- Clube do `futebol.db` usa o nome de lá; clube das Séries C e D usa o nome daqueles pacotes; os outros seguem o nome curto
  do ogol, com "-UF" só quando outro clube de outro estado tem o mesmo nome.

## O que não deu para coletar

- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade, combinado com o Guilherme).
- **Autores dos gols:** só onde a RSSSF traz e a soma fecha com o placar.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com campeão e vice em cima.
