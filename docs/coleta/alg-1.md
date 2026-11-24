# Campeonato Argelino (1ª divisão) — coleta de dados

Gerado por `python coleta/alg-1/importar.py`. Pacote em `data/coleta/alg-1/pacote/`.

**Edições:** 64, uma por temporada, de 1962/63 a 2025/26, como na lista de campeões da RSSSF (`algchamp.html`, "64 títulos; desde a independência") e na Wikipédia em inglês. A era colonial fica de fora (pesquisa de 24/11/2026, aprovada pelo Guilherme): não havia campeonato único (ligas regionais de Argel, Orã e Constantine) e ninguém conta esses títulos. 1962/63 e 1963/64: ligas regionais e fase final (jogos incompletos). 2019/20: parado pela Covid-19; a federação declarou o CR Belouizdad campeão.

**Fora do pacote:** a Copa da Argélia e as outras copas, a 2ª divisão e os jogos de acesso.

**Fontes:** RSSSF (páginas por temporada, `data/coleta/alg-1/rsssf/`: base dos jogos de todas as temporadas); ogol (1985/86 em diante, com os mesmos placares da RSSSF: conferência, rodada e data); Wikipédia em inglês (lista de campeões com vice e artilheiro e a tabela de cada temporada, terceira fonte nas divergências). A ESPN não tem a liga argelina.

**Clubes:** o nome pelo qual o clube é conhecido, com a sigla francesa (MC Alger, USM Alger, JS Kabylie...). Mesmo clube com outro nome é um só, com o nome atual: os nomes da reforma esportiva de 1977 a 1989 (MP Alger, JE Tizi Ouzou, EP Sétif, CM Belcourt...) e os mais antigos (JS Kawkabi, CR Belcourt). O USM Annaba dos anos 1960 e 1970 é o atual Hamra Annaba. Regras em `coleta/alg-1/clubes_alg.py`.

**Regras:** o placar é o da RSSSF. A classificação é a tabela publicada (ordem oficial e pontos); quando uma linha dela não fecha com os jogos e a tabela da Wikipédia confirma os jogos, a linha fica com os números dos jogos. Placar só muda com outra fonte (o ogol) que feche com as tabelas. Pontos como as tabelas contam: 3-2-1 (vitória, empate, derrota) até 1985/86, 2-1-0 de 1986/87 a 1994/95 e 3-1-0 desde 1995/96.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Formato |
|---|---|---|---|---|---|---|---|
| 1962/63 | 16 | 42 (42) | 137 | 3 | 0 / 0 | USM Alger | jogos incompletos (só a 2ª fase das ligas regionais e a fase final) |
| 1963/64 | 42 | 432 (432) | 1312 | 7 | 0 / 0 | Hamra Annaba | jogos incompletos (resultados conhecidos das ligas regionais e a fase final) |
| 1964/65 | 16 | 240 (240) | 610 | 0 | 0 / 1 | CR Belouizdad | pontos corridos |
| 1965/66 | 16 | 240 (240) | 647 | 0 | 0 / 1 | CR Belouizdad | pontos corridos |
| 1966/67 | 12 | 132 (132) | 373 | 0 | 0 / 1 | NA Hussein Dey | pontos corridos |
| 1967/68 | 12 | 132 (132) | 347 | 0 | 0 / 1 | ES Sétif | pontos corridos |
| 1968/69 | 12 | 132 (132) | 321 | 0 | 0 / 1 | CR Belouizdad | pontos corridos |
| 1969/70 | 12 | 132 (132) | 359 | 0 | 0 / 1 | CR Belouizdad | pontos corridos |
| 1970/71 | 12 | 132 (132) | 347 | 0 | 0 / 1 | MC Oran | pontos corridos |
| 1971/72 | 16 | 240 (240) | 596 | 0 | 0 / 1 | MC Alger | pontos corridos |
| 1972/73 | 16 | 240 (240) | 607 | 0 | 0 / 1 | JS Kabylie | pontos corridos |
| 1973/74 | 16 | 240 (240) | 597 | 0 | 0 / 1 | JS Kabylie | pontos corridos |
| 1974/75 | 16 | 232 (240) | 556 | 0 | 0 / 1 | MC Alger | pontos corridos |
| 1975/76 | 16 | 232 (240) | 677 | 0 | 0 / 1 | MC Alger | pontos corridos |
| 1976/77 | 15 | 180 (180) | 511 | 0 | 0 / 1 | JS Kabylie | pontos corridos |
| 1977/78 | 14 | 182 (182) | 456 | 0 | 0 / 1 | MC Alger | pontos corridos |
| 1978/79 | 14 | 182 (182) | 380 | 0 | 0 / 1 | MC Alger | pontos corridos |
| 1979/80 | 16 | 240 (246) | 518 | 0 | 0 / 1 | JS Kabylie | pontos corridos |
| 1980/81 | 16 | 216 (216) | 542 | 0 | 0 / 1 | RC Kouba | pontos corridos |
| 1981/82 | 16 | 240 (240) | 519 | 0 | 0 / 1 | JS Kabylie | pontos corridos |
| 1982/83 | 16 | 239 (240) | 466 | 0 | 0 / 1 | JS Kabylie | pontos corridos |
| 1983/84 | 16 | 240 (240) | 481 | 0 | 0 / 1 | GC Mascara | pontos corridos |
| 1984/85 | 21 | 380 (380) | 754 | 0 | 0 / 1 | JS Kabylie | pontos corridos |
| 1985/86 | 20 | 379 (380) | 782 | 0 | 0 / 1 | JS Kabylie | pontos corridos |
| 1986/87 | 20 | 380 (380) | 717 | 0 | 0 / 1 | ES Sétif | pontos corridos |
| 1987/88 | 18 | 306 (306) | 563 | 3 | 0 / 1 | MC Oran | pontos corridos |
| 1988/89 | 16 | 238 (240) | 480 | 1 | 0 / 1 | JS Kabylie | pontos corridos |
| 1989/90 | 16 | 240 (240) | 457 | 0 | 0 / 1 | JS Kabylie | pontos corridos |
| 1990/91 | 16 | 239 (240) | 498 | 0 | 0 / 1 | MO Constantine | pontos corridos |
| 1991/92 | 16 | 240 (240) | 509 | 0 | 0 / 1 | MC Oran | pontos corridos |
| 1992/93 | 16 | 240 (240) | 464 | 0 | 0 / 1 | MC Oran | pontos corridos |
| 1993/94 | 16 | 240 (240) | 459 | 0 | 0 / 1 | US Chaouia | pontos corridos |
| 1994/95 | 16 | 240 (240) | 506 | 0 | 0 / 1 | JS Kabylie | pontos corridos |
| 1995/96 | 16 | 240 (240) | 502 | 0 | 0 / 1 | USM Alger | pontos corridos |
| 1996/97 | 16 | 240 (240) | 562 | 0 | 0 / 1 | CS Constantine | pontos corridos |
| 1997/98 | 16 | 116 (116) | 220 | 182 | 0 / 2 | USM El Harrach | 2 grupos + desempate + jogos de classificação + mata-mata |
| 1998/99 | 28 | 365 (365) | 751 | 659 | 0 / 2 | MC Alger | 2 grupos + mata-mata |
| 1999/00 | 12 | 132 (132) | 316 | 120 | 1 / 0 | CR Belouizdad | pontos corridos |
| 2000/01 | 16 | 240 (240) | 553 | 501 | 0 / 1 | CR Belouizdad | pontos corridos |
| 2001/02 | 17 | 240 (240) | 516 | 409 | 0 / 1 | USM Alger | pontos corridos |
| 2002/03 | 16 | 240 (240) | 479 | 439 | 1 / 0 | USM Alger | pontos corridos |
| 2003/04 | 16 | 240 (240) | 506 | 470 | 1 / 0 | JS Kabylie | pontos corridos |
| 2004/05 | 16 | 241 (241) | 542 | 525 | 1 / 0 | USM Alger | pontos corridos |
| 2005/06 | 16 | 240 (240) | 520 | 510 | 1 / 0 | JS Kabylie | pontos corridos |
| 2006/07 | 16 | 240 (240) | 480 | 0 | 1 / 0 | ES Sétif | pontos corridos |
| 2007/08 | 16 | 240 (240) | 492 | 0 | 1 / 0 | JS Kabylie | pontos corridos |
| 2008/09 | 17 | 272 (272) | 567 | 0 | 1 / 0 | ES Sétif | pontos corridos |
| 2009/10 | 18 | 306 (306) | 683 | 0 | 0 / 1 | MC Alger | pontos corridos |
| 2010/11 | 16 | 240 (240) | 514 | 0 | 1 / 0 | ASO Chlef | pontos corridos |
| 2011/12 | 16 | 240 (240) | 565 | 0 | 1 / 0 | ES Sétif | pontos corridos |
| 2012/13 | 16 | 240 (240) | 480 | 0 | 1 / 0 | ES Sétif | pontos corridos |
| 2013/14 | 16 | 240 (240) | 507 | 0 | 1 / 0 | USM Alger | pontos corridos |
| 2014/15 | 16 | 240 (240) | 475 | 0 | 1 / 0 | ES Sétif | pontos corridos |
| 2015/16 | 16 | 240 (240) | 512 | 0 | 1 / 0 | USM Alger | pontos corridos |
| 2016/17 | 16 | 240 (240) | 504 | 0 | 1 / 0 | ES Sétif | pontos corridos |
| 2017/18 | 16 | 240 (240) | 528 | 0 | 1 / 0 | CS Constantine | pontos corridos |
| 2018/19 | 16 | 240 (240) | 476 | 0 | 1 / 0 | USM Alger | pontos corridos |
| 2019/20 | 16 | 173 (173) | 378 | 0 | 0 / 0 | CR Belouizdad | temporada interrompida (Covid-19) |
| 2020/21 | 20 | 380 (380) | 903 | 0 | 0 / 1 | CR Belouizdad | pontos corridos |
| 2021/22 | 18 | 306 (306) | 693 | 0 | 1 / 0 | CR Belouizdad | pontos corridos |
| 2022/23 | 16 | 240 (240) | 516 | 0 | 1 / 0 | CR Belouizdad | pontos corridos |
| 2023/24 | 16 | 240 (240) | 556 | 0 | 1 / 0 | MC Alger | pontos corridos |
| 2024/25 | 16 | 240 (240) | 467 | 0 | 1 / 0 | MC Alger | pontos corridos |
| 2025/26 | 16 | 240 (240) | 544 | 0 | 1 / 0 | MC Alger | pontos corridos |

## Conferência e correções, edição a edição

### 1962/63

- a 1ª fase das ligas regionais não está na página; a ordem dos quatro primeiros é a da fase final
- jogos incompletos (só a 2ª fase das ligas regionais e a fase final)
- a RSSSF não traz a 1ª fase das ligas regionais; a semifinal USM Alger 2-2 USM Annaba foi decidida pelos escanteios (7-6)
- decidido fora de campo — SC Perrégaux 1-0 CR Témouchent (1963-05-26): ?! - possibly awarded 0-0 win to Perrégaux
- abandonado/suspenso, sem valer — MSP Batna MO Constantine (s/d): abandoned at 3-2 in 83' due to pitch invasion

### 1963/64

- ligas regionais só com os resultados conhecidos ("Known Results") e o grupo Leste da Liga de Constantine sem números; os jogos de acesso à 1ª divisão do ano seguinte ficam de fora; dois jogos com siglas que não deu para identificar ("R.S.O" e "C.S.S", da Liga de Orã) ficam de fora
- jogos incompletos (resultados conhecidos das ligas regionais e a fase final)
- linha lida como jogo e descartada (clube não reconhecido): alg64:523 «R.S.O x CA Planteurs»
- linha lida como jogo e descartada (clube não reconhecido): alg64:775 «C.S.S x OM Arzew»
- decidido fora de campo — MC Alger USM Marengo (1963-12-22): awarded 3-0
- decidido fora de campo — OM Saint-Eugène USM Marengo (1964-02-20): awarded 3-0
- decidido fora de campo — RC Arbaâ USM Marengo (1964-02-16): awarded 3-0
- decidido fora de campo — USM Marengo JS Kabylie (1964-03-08): awarded 0-3
- decidido fora de campo — USM Marengo MC Alger (1964-05-10): awarded 0-3
- decidido fora de campo — GC Mascara WA Tlemcen (1963-10-13): awarded 3-0, forfait WAT
- decidido fora de campo — WA Tlemcen GS Perrégaux (1963-12-29): awarded 0-3, WAT suspended
- decidido fora de campo — EM Oran CA Planteurs (1964-01-05): awarded 3-0
- decidido fora de campo — WA Tlemcen CR Témouchent (1964-01-26): awarded 0-3, abandoned at 1-2 in 80' due to pitch invasion,
- decidido fora de campo — WA Tlemcen CA Planteurs (1964-02-09): awarded 0-3
- decidido fora de campo — RC Oran WA Tlemcen (1964-02-16): awarded 3-0
- decidido fora de campo — WA Tlemcen 0-3 CC Sig (1964-03-01): awarded 0-3
- decidido fora de campo — WA Tlemcen MC Oran (1964-03-08): awarded 0-3
- decidido fora de campo — OM Arzew WA Tlemcen (1964-03-15): awarded 3-0
- decidido fora de campo — WA Tlemcen MC Saïda (1964-03-21): awarded 0-3
- decidido fora de campo — MC Oran CR Témouchent (1964-04-05): awarded 3-0, Apparently CRT Suspended for a few matchs ?
- decidido fora de campo — ASM Oran WA Tlemcen (1964-04-05): awarded 3-0
- decidido fora de campo — WA Tlemcen GC Mascara (1964-04-12): awarded 0-3
- decidido fora de campo — WA Tlemcen JSM Tiaret (1964-04-19): awarded 0-3
- decidido fora de campo — MC Oran JSM Tiaret (1964-04-22): awarded 3-0, abandoned at 1-1 due to pitch invasion
- decidido fora de campo — USM Bel-Abbès WA Tlemcen (1964-04-22): awarded 0-3
- decidido fora de campo — CR Témouchent MC Saïda (1964-04-22): awarded 0-3
- decidido fora de campo — ES Mostaganem CR Témouchent (1964-04-26): awarded 3-0
- decidido fora de campo — EM Oran CR Témouchent (1964-05-03): awarded 3-0
- decidido fora de campo — WA Tlemcen RC Relizane (1964-05-03): awarded 0-3
- decidido fora de campo — WA Tlemcen EM Oran (1964-05-10): awarded 0-3
- decidido fora de campo — CR Témouchent GS Perrégaux (1964-05-10): awarded 0-3
- decidido fora de campo — OM Arzew CR Témouchent (1964-05-17): awarded 3-0
- decidido fora de campo — GS Perrégaux WA Tlemcen (1964-05-17): awarded 3-0
- decidido fora de campo — RC Oran MC Oran (1964-05-21): awarded 1-3 !
- decidido fora de campo — ES Mostaganem WA Tlemcen (1964-05-21): awarded 3-0
- decidido fora de campo — CR Témouchent USM Bel-Abbès (1964-05-21): awarded 0-3
- decidido fora de campo — JSM Tiaret CR Témouchent (1964-05-24): awarded 3-0
- decidido fora de campo — WA Tlemcen SCM Oran (1964-05-24): awarded 3-0
- decidido fora de campo — MC Saïda OM Arzew (1964-05-31): awarded 3-0, abondoned at 60'

### 1964/65

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg65:27: CR Belouizdad tabela [30, 19, 4, 7, 66, 22] jogos [30, 19, 4, 7, 69, 24] — a Wikipédia traz [30, 19, 4, 7, 68, 25]
- tabela publicada x jogos — alg65:27: MSP Batna tabela [30, 16, 7, 7, 40, 18] jogos [30, 17, 6, 7, 43, 20] — a Wikipédia traz [30, 16, 7, 7, 40, 19]
- tabela publicada x jogos — alg65:27: ES Sétif tabela [30, 12, 7, 11, 29, 27] jogos [30, 12, 8, 10, 30, 26] — a Wikipédia traz [30, 12, 8, 10, 30, 27]
- tabela publicada x jogos — alg65:27: USM Sétif tabela [30, 9, 11, 10, 30, 33] jogos [30, 9, 10, 11, 29, 34] — a Wikipédia traz [30, 9, 10, 11, 29, 32]
- tabela publicada x jogos — alg65:27: USM Blida tabela [30, 8, 12, 10, 36, 40] jogos [30, 8, 12, 10, 36, 39] — a Wikipédia traz [30, 8, 12, 10, 36, 37]
- tabela publicada x jogos — alg65:27: MO Constantine tabela [30, 9, 8, 13, 33, 50] jogos [30, 9, 7, 14, 34, 53] — a Wikipédia traz [30, 9, 8, 13, 34, 51]
- tabela publicada x jogos — alg65:27: USM Alger tabela [30, 8, 8, 14, 36, 43] jogos [30, 8, 8, 14, 38, 45] — a Wikipédia traz [30, 8, 8, 14, 35, 44]
- tabela publicada x jogos — alg65:27: MC Alger tabela [30, 8, 8, 14, 33, 42] jogos [30, 9, 8, 13, 33, 42] — a Wikipédia traz [30, 8, 8, 14, 39, 46]
- tabela publicada x jogos — alg65:27: JSM Tiaret tabela [30, 7, 10, 13, 30, 39] jogos [30, 7, 10, 13, 30, 40] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- decidido fora de campo — MO Constantine NA Hussein Dey (1965-01-17): awarded 0-3, originally 0-0
- decidido fora de campo — MC Alger MO Constantine (1965-02-07): awarded 0-3, MCA suspended
- decidido fora de campo — MC Oran MSP Batna (1965-02-07): awarded 0-3, MCO suspended
- decidido fora de campo — ES Guelma MC Alger (1965-02-21): awarded 3-0, MCA suspended
- decidido fora de campo — CR Belouizdad MC Oran (1965-02-21): awarded 3-0, MCO suspended
- decidido fora de campo — MC Alger USM Alger (1965-02-28): awarded 0-3, MCA suspended
- decidido fora de campo — MC Oran Hamra Annaba (1965-02-28): awarded 0-3, MCO suspended
- decidido fora de campo — MSP Batna USM Blida (1965-05-30): awarded 3-0

### 1965/66

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg66:28: ES Guelma tabela [30, 15, 10, 5, 48, 29] jogos [30, 16, 9, 5, 45, 28] — a Wikipédia traz [30, 15, 10, 5, 45, 29]
- tabela publicada x jogos — alg66:28: SCM Oran tabela [30, 12, 12, 6, 41, 36] jogos [30, 12, 12, 6, 42, 36] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg66:28: RC Kouba tabela [30, 11, 9, 10, 45, 56] jogos [30, 11, 9, 10, 44, 52] — a Wikipédia traz [30, 11, 9, 10, 46, 52]
- tabela publicada x jogos — alg66:28: NA Hussein Dey tabela [30, 10, 9, 11, 46, 43] jogos [30, 10, 9, 11, 47, 42] — a Wikipédia traz [30, 10, 9, 11, 46, 40]
- tabela publicada x jogos — alg66:28: MO Constantine tabela [30, 10, 9, 11, 32, 36] jogos [30, 10, 9, 11, 32, 37] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg66:28: Hamra Annaba tabela [30, 9, 10, 11, 41, 38] jogos [30, 9, 10, 11, 40, 38] — a Wikipédia traz [30, 8, 11, 11, 40, 37]
- tabela publicada x jogos — alg66:28: USM Blida tabela [30, 10, 8, 12, 34, 37] jogos [30, 10, 8, 12, 33, 37] — a Wikipédia traz [30, 10, 8, 12, 34, 38]
- tabela publicada x jogos — alg66:28: MSP Batna tabela [30, 11, 5, 14, 40, 41] jogos [30, 11, 5, 14, 39, 41] — a Wikipédia traz [30, 9, 9, 12, 40, 40]
- tabela publicada x jogos — alg66:28: JSM Skikda tabela [30, 9, 8, 13, 29, 39] jogos [30, 9, 7, 14, 28, 39] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg66:28: USM Sétif tabela [30, 6, 6, 18, 29, 59] jogos [30, 6, 6, 18, 25, 54] — a Wikipédia traz [30, 7, 6, 17, 26, 53]
- tabela publicada x jogos — alg66:28: ES Mostaganem tabela [30, 6, 6, 18, 25, 55] jogos [30, 6, 6, 18, 29, 59] — a Wikipédia traz [30, 6, 6, 18, 29, 61]
- provável jogo da diferença: MO Constantine 0-2 SCM Oran (1966-03-13, alg66:229); com 0-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1966/67

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg67:28: RC Kouba tabela [22, 10, 7, 5, 39, 31] jogos [23, 10, 7, 6, 40, 35] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg67:28: CR Belouizdad tabela [22, 12, 3, 7, 43, 36] jogos [21, 12, 3, 6, 42, 32] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg67:28: Hamra Annaba tabela [22, 9, 8, 5, 38, 27] jogos [23, 9, 8, 6, 38, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg67:28: ES Sétif tabela [22, 8, 8, 6, 26, 15] jogos [21, 9, 6, 6, 28, 14] — a Wikipédia traz [22, 8, 8, 6, 26, 14]
- tabela publicada x jogos — alg67:28: USM Blida tabela [22, 3, 7, 12, 23, 36] jogos [22, 3, 7, 12, 23, 37] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos

### 1967/68

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg68:28: ES Sétif tabela [22, 9, 9, 4, 31, 21] jogos [22, 8, 10, 4, 32, 23] — a Wikipédia traz [22, 9, 9, 4, 32, 22]
- tabela publicada x jogos — alg68:28: MC Oran tabela [22, 10, 7, 5, 26, 21] jogos [22, 10, 7, 5, 28, 21] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg68:28: NA Hussein Dey tabela [22, 9, 7, 6, 37, 29] jogos [22, 10, 7, 5, 37, 26] — a Wikipédia traz [22, 9, 7, 6, 37, 28]
- tabela publicada x jogos — alg68:28: ES Guelma tabela [22, 10, 3, 9, 37, 30] jogos [22, 8, 3, 11, 30, 34] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg68:28: RC Kouba tabela [22, 7, 8, 7, 32, 26] jogos [22, 7, 8, 7, 32, 25] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg68:28: ASM Oran tabela [22, 8, 4, 10, 22, 38] jogos [22, 9, 4, 9, 26, 35] — a Wikipédia traz [22, 8, 4, 10, 23, 41]
- tabela publicada x jogos — alg68:28: MC Saïda tabela [22, 7, 6, 9, 31, 32] jogos [22, 7, 6, 9, 31, 33] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg68:28: Hamra Annaba tabela [22, 7, 7, 8, 20, 24] jogos [22, 7, 7, 8, 23, 25] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg68:28: JSM Skikda tabela [22, 7, 5, 10, 23, 30] jogos [22, 7, 6, 9, 23, 31] — a Wikipédia traz [22, 7, 5, 10, 23, 32]
- tabela publicada x jogos — alg68:28: MO Constantine tabela [22, 6, 3, 13, 26, 49] jogos [22, 6, 3, 13, 25, 49] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- decidido fora de campo — ES Guelma ASM Oran (1968-06-16): awarded 1-3

### 1968/69

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg69:28: USM Bel-Abbès tabela [22, 10, 5, 7, 22, 16] jogos [22, 10, 5, 7, 23, 17] — a Wikipédia traz [22, 10, 5, 7, 23, 18]
- tabela publicada x jogos — alg69:28: MC Alger tabela [22, 11, 2, 9, 28, 27] jogos [22, 11, 2, 9, 28, 28] — a Wikipédia traz [22, 11, 2, 9, 28, 24]
- tabela publicada x jogos — alg69:28: Hamra Annaba tabela [22, 10, 2, 10, 37, 38] jogos [22, 10, 2, 10, 37, 37] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg69:28: ES Guelma tabela [22, 10, 2, 10, 31, 36] jogos [22, 10, 2, 10, 31, 35] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg69:28: ES Sétif tabela [22, 7, 6, 9, 22, 24] jogos [22, 7, 7, 8, 23, 24] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg69:28: RC Kouba tabela [22, 8, 4, 10, 26, 29] jogos [22, 7, 5, 10, 25, 30] — a Wikipédia traz [22, 8, 4, 10, 25, 29]
- tabela publicada x jogos — alg69:28: JS Djijel tabela [22, 7, 6, 9, 17, 20] jogos [22, 7, 7, 8, 18, 20] — a Wikipédia traz [22, 7, 6, 9, 17, 28]
- tabela publicada x jogos — alg69:28: NA Hussein Dey tabela [22, 7, 6, 9, 28, 36] jogos [22, 6, 7, 9, 29, 38] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: MC Alger 2-1 ES Sétif (1969-03-02, alg69:160); com 2-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: MC Alger 0-2 JS Djijel (1969-05-25, alg69:205); com 0-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- decidido fora de campo — MC Alger NA Hussein Dey (1968-09-22): awarded 3-1, originally 1-1
- decidido fora de campo — MC Saïda CR Belouizdad (1969-06-15): awarded 3-0

### 1969/70

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg70:28: RC Kouba tabela [22, 9, 4, 9, 41, 33] jogos [22, 9, 4, 9, 39, 32] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg70:28: USM Alger tabela [22, 7, 7, 8, 34, 30] jogos [22, 7, 7, 8, 34, 32] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg70:28: MC Oran tabela [22, 8, 4, 10, 26, 32] jogos [22, 8, 4, 10, 25, 31] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg70:28: NA Hussein Dey tabela [22, 6, 7, 9, 24, 28] jogos [22, 6, 7, 9, 23, 26] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg70:28: USM Bel-Abbès tabela [22, 7, 5, 10, 20, 24] jogos [22, 7, 5, 10, 21, 24] — a Wikipédia traz [22, 7, 5, 10, 20, 23]
- tabela publicada x jogos — alg70:28: ES Sétif tabela [22, 7, 5, 10, 26, 35] jogos [22, 7, 5, 10, 25, 34] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg70:28: JS Djijel tabela [22, 8, 3, 11, 24, 36] jogos [22, 8, 3, 11, 26, 37] — a Wikipédia traz [22, 8, 3, 11, 26, 35]
- tabela publicada x jogos — alg70:28: Hamra Annaba tabela [22, 7, 4, 11, 26, 30] jogos [22, 7, 4, 11, 27, 31] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- corrigido — USM Bel-Abbès x NA Hussein Dey (1970-02-22): USM Bel-Abbès 0-0 NA Hussein Dey aparece duas vezes na rodada 10

### 1970/71

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg71:27: NA Hussein Dey tabela [22, 9, 6, 7, 24, 20] jogos [22, 8, 7, 7, 23, 20] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg71:27: ES Guelma tabela [22, 7, 5, 10, 30, 35] jogos [22, 7, 5, 10, 30, 37] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg71:27: JSM Tiaret tabela [22, 6, 6, 10, 21, 22] jogos [22, 6, 6, 10, 22, 23] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg71:27: USM Bel-Abbès tabela [22, 8, 4, 10, 20, 26] jogos [22, 8, 5, 9, 22, 25] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- decidido fora de campo — ES Guelma USM Bel-Abbès (1971-02-21): awarded 3-1, USMBA forfeit
- decidido fora de campo — USM Bel-Abbès MC Oran (1971-02-28): awarded 1-3, USMBA forfeit

### 1971/72

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg72:27: CR Belouizdad tabela [30, 15, 8, 7, 57, 30] jogos [30, 15, 7, 8, 57, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg72:27: MO Constantine tabela [30, 14, 10, 6, 46, 32] jogos [30, 14, 10, 6, 47, 33] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg72:27: MC Oran tabela [30, 12, 13, 5, 36, 29] jogos [30, 12, 13, 5, 37, 30] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg72:27: ES Sétif tabela [30, 11, 9, 10, 36, 37] jogos [30, 11, 9, 10, 35, 37] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — alg72:27: RC Kouba tabela [30, 11, 8, 11, 51, 39] jogos [30, 11, 7, 12, 50, 41] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg72:27: ASM Oran tabela [30, 11, 8, 11, 37, 37] jogos [30, 11, 8, 11, 38, 37] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg72:27: NA Hussein Dey tabela [30, 11, 7, 12, 31, 20] jogos [30, 11, 7, 12, 32, 21] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg72:27: JSM Tiaret tabela [30, 10, 9, 11, 34, 44] jogos [30, 10, 9, 11, 36, 45] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg72:27: Hamra Annaba tabela [30, 7, 15, 8, 26, 32] jogos [30, 7, 15, 8, 25, 33] — a Wikipédia traz [30, 7, 15, 8, 25, 32]
- tabela publicada x jogos — alg72:27: CS Constantine tabela [30, 10, 8, 12, 26, 31] jogos [30, 10, 9, 11, 29, 32] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — alg72:27: USM Bel-Abbès tabela [30, 6, 15, 9, 24, 30] jogos [30, 7, 14, 9, 24, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg72:27: ES Guelma tabela [30, 3, 7, 20, 25, 63] jogos [30, 3, 7, 20, 23, 61] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: MC Oran 1-1 MO Constantine (1972-01-30, alg72:192); com 0-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: MO Constantine 3-1 MC Oran (1972-06-18, alg72:342); com 2-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: NA Hussein Dey 2-1 MO Constantine (1972-04-23, alg72:276); com 1-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: NA Hussein Dey 1-2 MC Oran (1971-10-03, alg72:82); com 0-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: ES Sétif 3-1 USM Bel-Abbès (1972-06-18, alg72:347); com 4-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1972/73

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- a rodada 10 aparece duas vezes na página: a cópia foi descartada
- tabela publicada x jogos — alg73:27: JS Kabylie tabela [30, 13, 13, 4, 42, 28] jogos [30, 13, 13, 4, 42, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg73:27: MC Oran tabela [30, 11, 8, 11, 48, 40] jogos [30, 11, 8, 11, 47, 40] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg73:27: GC Mascara tabela [30, 7, 9, 14, 26, 57] jogos [30, 7, 9, 14, 27, 57] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg73:27: CS Constantine tabela [30, 5, 11, 14, 28, 48] jogos [30, 5, 11, 14, 28, 47] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- provável jogo da diferença: MC Oran 2-1 CS Constantine (1972-10-01, alg73:81); com 3-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: CS Constantine 1-2 MC Oran (1973-03-11, alg73:241); com 1-3 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- corrigido — RC Kouba x CS Constantine (1972-11-26): a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista
- corrigido — ASM Oran x ES Sétif (1972-11-26): a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista
- corrigido — JS Djijel x JS Kabylie (1972-11-26): a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista
- corrigido — MC Alger x CR Belouizdad (1972-11-26): a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista
- corrigido — MO Constantine x NA Hussein Dey (1972-11-26): a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista
- corrigido — USM Blida x USM Bel-Abbès (1972-11-26): a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista
- corrigido — Hamra Annaba x MC Oran (1972-11-26): a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista
- corrigido — JSM Tiaret x GC Mascara (1972-11-26): a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista
- decidido fora de campo — JS Djijel MC Oran (1973-07-01): awarded 3-0

### 1973/74

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg74:25: JS Kabylie tabela [30, 17, 7, 6, 43, 32] jogos [30, 17, 6, 7, 42, 30] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg74:25: MO Constantine tabela [30, 18, 3, 9, 39, 30] jogos [30, 18, 3, 9, 39, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg74:25: NA Hussein Dey tabela [30, 14, 8, 8, 45, 31] jogos [30, 13, 8, 9, 44, 32] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg74:25: CR Belouizdad tabela [30, 13, 8, 9, 40, 26] jogos [30, 13, 7, 10, 41, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg74:25: RC Kouba tabela [30, 11, 10, 9, 35, 29] jogos [30, 12, 10, 8, 35, 23] — a Wikipédia traz [30, 11, 10, 9, 35, 39]
- tabela publicada x jogos — alg74:25: ES Sétif tabela [30, 11, 10, 9, 33, 29] jogos [30, 11, 10, 9, 33, 30] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg74:25: MC Oran tabela [30, 11, 8, 11, 49, 48] jogos [30, 11, 9, 10, 49, 49] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg74:25: USM Bel-Abbès tabela [30, 10, 8, 12, 32, 33] jogos [30, 11, 7, 12, 31, 34] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos

### 1974/75

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- a rodada 4 da página é cópia da rodada 3: os oito jogos verdadeiros da rodada 4 faltam
- tabela publicada x jogos — alg75:25: MC Alger tabela [30, 16, 10, 4, 49, 22] jogos [29, 15, 10, 4, 44, 21] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg75:25: RC Kouba tabela [30, 15, 11, 4, 51, 23] jogos [29, 15, 10, 4, 51, 22] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg75:25: MC Oran tabela [30, 14, 9, 7, 53, 42] jogos [29, 14, 9, 6, 51, 37] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg75:25: NA Hussein Dey tabela [30, 12, 10, 8, 42, 29] jogos [29, 11, 9, 9, 39, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg75:25: CR Belouizdad tabela [30, 9, 15, 6, 41, 27] jogos [29, 8, 15, 6, 34, 25] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg75:25: USM Alger tabela [30, 13, 7, 10, 48, 36] jogos [29, 12, 7, 10, 42, 32] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg75:25: JS Kabylie tabela [30, 11, 10, 9, 39, 27] jogos [29, 11, 10, 8, 38, 25] — a Wikipédia traz [29, 10, 10, 9, 39, 27]
- tabela publicada x jogos — alg75:25: ES Sétif tabela [30, 8, 13, 9, 27, 23] jogos [29, 8, 13, 8, 27, 22] — a Wikipédia traz [30, 8, 13, 9, 29, 24]
- tabela publicada x jogos — alg75:25: MO Constantine tabela [30, 11, 6, 13, 38, 36] jogos [29, 9, 7, 13, 34, 36] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg75:25: Hamra Annaba tabela [30, 8, 12, 10, 39, 40] jogos [29, 9, 13, 7, 39, 34] — a Wikipédia traz [30, 8, 13, 9, 39, 40]
- tabela publicada x jogos — alg75:25: WA Boufarik tabela [30, 8, 11, 11, 27, 37] jogos [29, 7, 11, 11, 26, 37] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg75:25: USM Khenchela tabela [30, 11, 5, 14, 24, 40] jogos [29, 10, 6, 13, 23, 39] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg75:25: USM Bel-Abbès tabela [30, 8, 11, 11, 29, 54] jogos [29, 8, 11, 10, 28, 50] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg75:25: MC Saïda tabela [30, 8, 8, 14, 32, 44] jogos [29, 7, 8, 14, 25, 41] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg75:25: USM Sétif tabela [30, 6, 8, 16, 37, 63] jogos [29, 6, 7, 16, 34, 55] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg75:25: USM Blida tabela [30, 7, 4, 19, 20, 53] jogos [29, 7, 4, 18, 21, 51] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- corrigido — USM Alger x JS Kabylie (1974-09-29): a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são conhecidos
- corrigido — USM Sétif x MC Oran (1974-09-29): a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são conhecidos
- corrigido — Hamra Annaba x CR Belouizdad (1974-09-29): a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são conhecidos
- corrigido — MO Constantine x NA Hussein Dey (1974-09-29): a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são conhecidos
- corrigido — USM Blida x ES Sétif (1974-09-29): a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são conhecidos
- corrigido — RC Kouba x MC Saïda (1974-09-29): a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são conhecidos
- corrigido — USM Bel-Abbès x USM Khenchela (1974-09-29): a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são conhecidos
- corrigido — WA Boufarik x MC Alger (1974-09-29): a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são conhecidos

### 1975/76

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- a rodada 18 da página é cópia da rodada 17: os oito jogos verdadeiros da rodada 18 faltam
- tabela publicada x jogos — alg76:26: MC Alger tabela [30, 18, 7, 5, 63, 32] jogos [29, 18, 7, 4, 63, 32] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg76:26: NA Hussein Dey tabela [30, 18, 6, 6, 43, 20] jogos [29, 17, 7, 5, 43, 19] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg76:26: JS Kabylie tabela [30, 16, 7, 7, 42, 23] jogos [29, 14, 8, 7, 38, 26] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg76:26: USM Alger tabela [30, 14, 8, 8, 52, 29] jogos [29, 11, 8, 10, 47, 31] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg76:26: RC Kouba tabela [30, 15, 6, 9, 46, 28] jogos [29, 12, 6, 11, 42, 34] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg76:26: ES Sétif tabela [30, 12, 11, 7, 55, 35] jogos [29, 11, 11, 7, 54, 35] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg76:26: USM El Harrach tabela [30, 12, 9, 9, 39, 42] jogos [29, 13, 10, 6, 42, 38] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg76:26: CA Batna tabela [30, 13, 6, 11, 43, 42] jogos [29, 13, 5, 11, 42, 42] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg76:26: MC Oran tabela [30, 12, 7, 11, 56, 51] jogos [29, 12, 7, 10, 56, 50] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg76:26: MO Constantine tabela [30, 12, 7, 11, 45, 47] jogos [29, 12, 7, 10, 48, 47] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg76:26: CR Belouizdad tabela [30, 9, 11, 10, 43, 44] jogos [29, 9, 12, 8, 44, 40] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg76:26: WA Boufarik tabela [30, 10, 7, 13, 36, 43] jogos [29, 10, 7, 12, 36, 40] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg76:26: Hamra Annaba tabela [30, 9, 6, 15, 33, 49] jogos [29, 9, 6, 14, 32, 48] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg76:26: USM Khenchela tabela [30, 4, 9, 17, 28, 53] jogos [29, 5, 6, 18, 27, 52] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg76:26: USM Bel-Abbès tabela [30, 4, 6, 20, 29, 64] jogos [29, 4, 6, 19, 29, 62] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg76:26: ASM Oran tabela [30, 3, 5, 22, 35, 86] jogos [29, 3, 5, 21, 34, 81] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- corrigido — CA Batna x ES Sétif (1976-02-22): a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são conhecidos
- corrigido — ASM Oran x Hamra Annaba (1976-02-22): a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são conhecidos
- corrigido — RC Kouba x JS Kabylie (1976-02-22): a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são conhecidos
- corrigido — NA Hussein Dey x CR Belouizdad (1976-02-22): a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são conhecidos
- corrigido — USM Bel-Abbès x USM El Harrach (1976-02-22): a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são conhecidos
- corrigido — MO Constantine x MC Oran (1976-02-22): a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são conhecidos
- corrigido — USM Alger x USM Khenchela (1976-02-22): a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são conhecidos
- corrigido — WA Boufarik x MC Alger (1976-02-22): a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são conhecidos
- decidido fora de campo — CA Batna ASM Oran (1976-03-21): awarded 3-0

### 1976/77

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg77:26: JS Kabylie tabela [26, 17, 6, 3, 57, 27] jogos [26, 17, 6, 3, 57, 28] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg77:26: CR Belouizdad tabela [26, 15, 7, 4, 40, 19] jogos [26, 15, 7, 4, 39, 19] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg77:26: NA Hussein Dey tabela [26, 16, 5, 5, 60, 26] jogos [25, 15, 6, 4, 57, 20] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg77:26: MC Oran tabela [26, 13, 10, 3, 53, 36] jogos [26, 13, 10, 3, 53, 37] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg77:26: MC Alger tabela [26, 11, 6, 9, 50, 51] jogos [26, 11, 6, 9, 49, 51] — a Wikipédia traz [25, 11, 6, 8, 50, 48]
- tabela publicada x jogos — alg77:26: ASO Chlef tabela [26, 10, 5, 11, 28, 28] jogos [25, 9, 5, 11, 23, 27] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg77:26: CA Batna tabela [26, 9, 7, 10, 38, 44] jogos [26, 8, 8, 10, 36, 44] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg77:26: USM El Harrach tabela [26, 8, 8, 10, 29, 35] jogos [26, 9, 7, 10, 33, 35] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg77:26: ES Sétif tabela [26, 4, 15, 7, 28, 30] jogos [25, 3, 15, 7, 26, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg77:26: MO Constantine tabela [26, 7, 4, 15, 35, 52] jogos [24, 7, 5, 12, 29, 45] — a Wikipédia traz [25, 6, 4, 15, 32, 52]
- tabela publicada x jogos — alg77:26: RCG Oran tabela [26, 4, 6, 16, 22, 42] jogos [26, 3, 6, 17, 19, 45] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg77:26: ES Guelma tabela [26, 4, 4, 18, 25, 67] jogos [25, 4, 4, 17, 25, 58] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- decidido fora de campo — CA Batna USM El Harrach (1976-12-03): awarded 0-3
- decidido fora de campo — MO Constantine MC Alger (1977-07-01): awarded 3-0

### 1977/78

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg78:26: MC Alger tabela [26, 15, 6, 5, 47, 27] jogos [26, 15, 6, 5, 45, 27] — a Wikipédia traz [26, 15, 6, 5, 47, 28]
- tabela publicada x jogos — alg78:26: JS Kabylie tabela [26, 13, 9, 4, 45, 23] jogos [26, 14, 8, 4, 45, 22] — a Wikipédia traz [26, 13, 9, 4, 45, 24]
- tabela publicada x jogos — alg78:26: NA Hussein Dey tabela [26, 9, 12, 5, 35, 30] jogos [26, 10, 11, 5, 35, 30] — a Wikipédia traz [26, 9, 12, 5, 35, 31]
- tabela publicada x jogos — alg78:26: USM Alger tabela [26, 11, 6, 9, 39, 26] jogos [26, 11, 7, 8, 39, 26] — a Wikipédia traz [26, 11, 6, 9, 40, 26]
- tabela publicada x jogos — alg78:26: ASO Chlef tabela [26, 9, 9, 8, 26, 23] jogos [26, 9, 8, 9, 26, 23] — a Wikipédia traz [26, 9, 9, 8, 29, 25]
- tabela publicada x jogos — alg78:26: RC Kouba tabela [26, 9, 8, 9, 38, 35] jogos [26, 9, 6, 11, 38, 35] — a Wikipédia traz [26, 9, 8, 9, 39, 34]
- tabela publicada x jogos — alg78:26: MC Oran tabela [26, 8, 10, 8, 32, 28] jogos [26, 8, 9, 9, 32, 28] — a Wikipédia traz [26, 8, 10, 8, 32, 27]
- tabela publicada x jogos — alg78:26: CR Belouizdad tabela [26, 8, 9, 9, 31, 33] jogos [26, 9, 6, 11, 31, 33] — a Wikipédia traz [26, 8, 9, 9, 32, 31]
- tabela publicada x jogos — alg78:26: USM El Harrach tabela [26, 9, 7, 10, 24, 30] jogos [26, 9, 6, 11, 24, 30] — a Wikipédia traz [26, 9, 7, 10, 23, 30]
- tabela publicada x jogos — alg78:26: ASM Oran tabela [26, 6, 9, 11, 25, 41] jogos [26, 6, 10, 10, 28, 43] — a Wikipédia traz [26, 6, 9, 11, 28, 46]
- tabela publicada x jogos — alg78:26: DNC Alger tabela [26, 5, 6, 15, 22, 38] jogos [26, 6, 6, 14, 22, 38] — a Wikipédia traz [26, 5, 6, 15, 21, 37]

### 1978/79

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg79:26: DNC Alger tabela [26, 9, 6, 11, 25, 34] jogos [26, 8, 7, 11, 24, 34] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg79:26: NA Hussein Dey tabela [26, 7, 10, 9, 31, 29] jogos [26, 6, 10, 10, 31, 29] — a Wikipédia traz [26, 7, 10, 9, 29, 27]
- tabela publicada x jogos — alg79:26: RC Kouba tabela [26, 8, 6, 12, 26, 25] jogos [26, 8, 7, 11, 26, 25] — a Wikipédia traz [26, 8, 6, 12, 25, 26]
- tabela publicada x jogos — alg79:26: USM Alger tabela [26, 7, 8, 11, 27, 38] jogos [26, 6, 9, 11, 27, 38] — a Wikipédia traz [26, 7, 8, 11, 30, 40]
- tabela publicada x jogos — alg79:26: CA Batna tabela [26, 6, 9, 11, 18, 23] jogos [26, 7, 9, 10, 18, 21] — a Wikipédia traz [26, 6, 9, 11, 17, 30]
- tabela publicada x jogos — alg79:26: CS Constantine tabela [26, 5, 10, 11, 21, 35] jogos [26, 5, 11, 10, 20, 35] — a Wikipédia traz [26, 5, 10, 11, 21, 32]
- decidido fora de campo — CA Batna USM El Harrach (1979-01-19): Apr 20; awarded 0-3, originally 1-0

### 1979/80

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg80:27: JS Kabylie tabela [30, 15, 13, 2, 48, 22] jogos [29, 12, 14, 3, 41, 21] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg80:27: CR Belouizdad tabela [30, 14, 11, 5, 40, 24] jogos [29, 15, 10, 4, 41, 22] — a Wikipédia traz [30, 14, 11, 5, 41, 24]
- tabela publicada x jogos — alg80:27: ES Sétif tabela [30, 14, 6, 10, 50, 30] jogos [30, 14, 6, 10, 50, 31] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg80:27: RC Kouba tabela [30, 14, 5, 11, 38, 47] jogos [28, 12, 6, 10, 33, 29] — a Wikipédia traz [30, 14, 5, 11, 38, 32]
- tabela publicada x jogos — alg80:27: GC Mascara tabela [30, 13, 7, 10, 41, 27] jogos [30, 13, 7, 10, 41, 47] — a Wikipédia traz [30, 13, 7, 10, 41, 37]
- tabela publicada x jogos — alg80:27: NA Hussein Dey tabela [30, 11, 10, 9, 43, 32] jogos [26, 9, 10, 7, 33, 22] — a Wikipédia traz [30, 12, 10, 8, 45, 27]
- tabela publicada x jogos — alg80:27: MC Alger tabela [30, 9, 12, 9, 35, 33] jogos [30, 9, 12, 9, 35, 34] — a Wikipédia traz [30, 10, 11, 9, 37, 33]
- tabela publicada x jogos — alg80:27: ES Guelma tabela [30, 11, 4, 15, 31, 46] jogos [30, 11, 5, 14, 31, 43] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg80:27: CA Batna tabela [30, 6, 14, 10, 27, 46] jogos [28, 5, 15, 8, 24, 37] — a Wikipédia traz [30, 6, 14, 10, 23, 46]
- tabela publicada x jogos — alg80:27: USM Alger tabela [30, 7, 11, 12, 32, 37] jogos [30, 6, 12, 12, 28, 36] — a Wikipédia traz [30, 7, 11, 12, 30, 35]
- tabela publicada x jogos — alg80:27: IR Saha tabela [30, 5, 6, 19, 18, 50] jogos [28, 5, 6, 17, 17, 43] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- não jogado — CA Batna NA Hussein Dey (1980-02-22)
- não jogado — NA Hussein Dey RC Kouba (1980-02-28)
- não jogado — NA Hussein Dey IR Saha (1980-03-14)
- não jogado — JS Kabylie NA Hussein Dey (1980-05-16)
- não jogado — CR Belouizdad IR Saha (1980-05-30)
- não jogado — RC Kouba CA Batna (1980-05-30)

### 1980/81

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg81:26: RC Kouba tabela [28, 15, 7, 6, 46, 27] jogos [28, 15, 7, 6, 46, 26] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg81:26: JS Kabylie tabela [28, 15, 6, 7, 44, 28] jogos [28, 15, 6, 7, 44, 29] — a Wikipédia traz [28, 15, 6, 7, 50, 28]
- tabela publicada x jogos — alg81:26: USM El Harrach tabela [28, 13, 7, 8, 32, 22] jogos [28, 13, 7, 8, 31, 22] — a Wikipédia traz [28, 13, 7, 8, 33, 22]
- tabela publicada x jogos — alg81:26: NA Hussein Dey tabela [28, 12, 5, 11, 36, 36] jogos [28, 12, 5, 11, 36, 35] — a Wikipédia traz [29, 12, 6, 11, 36, 35]
- tabela publicada x jogos — alg81:26: DNC Alger tabela [28, 8, 12, 8, 40, 36] jogos [28, 8, 12, 8, 38, 36] — a Wikipédia traz [28, 8, 12, 8, 39, 35]
- tabela publicada x jogos — alg81:26: USM Bel-Abbès tabela [28, 10, 8, 10, 34, 37] jogos [28, 9, 8, 11, 34, 38] — a Wikipédia traz [28, 10, 8, 10, 35, 36]
- tabela publicada x jogos — alg81:26: ASM Oran tabela [28, 8, 9, 11, 27, 37] jogos [28, 7, 10, 11, 27, 39] — a Wikipédia traz [28, 8, 9, 11, 26, 36]
- tabela publicada x jogos — alg81:26: GC Mascara tabela [28, 7, 10, 11, 33, 42] jogos [30, 7, 11, 12, 34, 46] — a Wikipédia traz [28, 7, 10, 11, 33, 45]
- tabela publicada x jogos — alg81:26: CR Belouizdad tabela [28, 6, 12, 10, 36, 45] jogos [28, 7, 12, 9, 38, 43] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg81:26: ES Guelma tabela [28, 3, 11, 14, 27, 41] jogos [26, 3, 11, 12, 27, 37] — a Wikipédia traz [28, 8, 1, 19, 27, 38]
- provável jogo da diferença: USM El Harrach 1-0 NA Hussein Dey (1980-11-07, alg81:123); com 2-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: NA Hussein Dey 0-1 USM El Harrach (1981-03-27, alg81:270); com 0-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1981/82

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg82:27: ES Sétif tabela [30, 12, 10, 8, 38, 32] jogos [30, 12, 10, 8, 39, 32] — a Wikipédia traz [30, 13, 8, 9, 39, 32]
- tabela publicada x jogos — alg82:27: USM El Harrach tabela [30, 12, 8, 10, 29, 21] jogos [30, 12, 8, 10, 29, 22] — a Wikipédia traz [30, 12, 8, 10, 39, 20]
- tabela publicada x jogos — alg82:27: WKF Collo tabela [30, 11, 9, 10, 24, 20] jogos [30, 12, 9, 9, 30, 22] — a Wikipédia traz [30, 10, 11, 9, 25, 21]
- tabela publicada x jogos — alg82:27: CR Belouizdad tabela [30, 10, 11, 9, 35, 33] jogos [30, 10, 12, 8, 35, 32] — a Wikipédia traz [30, 12, 6, 12, 35, 33]
- tabela publicada x jogos — alg82:27: USM Aïn Beïda tabela [30, 11, 7, 12, 31, 37] jogos [30, 11, 7, 12, 30, 39] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg82:27: MC Alger tabela [30, 9, 10, 11, 35, 36] jogos [30, 9, 10, 11, 36, 36] — a Wikipédia traz [30, 9, 10, 11, 37, 36]
- tabela publicada x jogos — alg82:27: GC Mascara tabela [30, 10, 8, 12, 39, 46] jogos [30, 10, 7, 13, 39, 48] — a Wikipédia traz [30, 10, 7, 13, 40, 44]
- tabela publicada x jogos — alg82:27: ASM Oran tabela [30, 7, 14, 9, 27, 36] jogos [30, 6, 15, 9, 27, 37] — a Wikipédia traz [30, 7, 14, 9, 28, 27]
- tabela publicada x jogos — alg82:27: RC Kouba tabela [30, 7, 13, 10, 26, 27] jogos [30, 7, 13, 10, 27, 29] — a Wikipédia traz [30, 8, 11, 11, 35, 35]
- tabela publicada x jogos — alg82:27: USM Bel-Abbès tabela [30, 7, 13, 10, 28, 34] jogos [30, 6, 13, 11, 28, 38] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg82:27: USM Alger tabela [30, 8, 11, 11, 25, 35] jogos [30, 8, 12, 10, 25, 32] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg82:27: DNC Alger tabela [30, 6, 15, 9, 31, 27] jogos [31, 6, 16, 9, 31, 25] — a Wikipédia traz [30, 6, 15, 9, 30, 24]
- tabela publicada x jogos — alg82:27: ASO Chlef tabela [30, 4, 12, 14, 23, 54] jogos [29, 4, 11, 14, 23, 54] — a Wikipédia traz [30, 4, 12, 14, 24, 54]
- decidido fora de campo — CR Belouizdad MC Oran (1982-02-12): awarded 0-3

### 1982/83

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg83:26: JS Kabylie tabela [30, 17, 7, 6, 41, 21] jogos [29, 16, 7, 6, 38, 22] — a Wikipédia traz [30, 17, 7, 6, 41, 22]
- tabela publicada x jogos — alg83:26: ES Sétif tabela [30, 14, 10, 6, 40, 19] jogos [30, 14, 10, 6, 40, 18] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg83:26: NA Hussein Dey tabela [30, 11, 8, 11, 33, 30] jogos [30, 11, 8, 11, 34, 30] — a Wikipédia traz [30, 11, 8, 11, 32, 31]
- tabela publicada x jogos — alg83:26: ASM Oran tabela [30, 7, 14, 9, 19, 23] jogos [29, 7, 14, 8, 19, 20] — a Wikipédia traz [30, 8, 13, 9, 27, 25]
- tabela publicada x jogos — alg83:26: RC Kouba tabela [30, 11, 5, 14, 39, 37] jogos [30, 10, 7, 13, 38, 37] — a Wikipédia traz [30, 10, 7, 13, 30, 34]
- tabela publicada x jogos — alg83:26: USM Aïn Beïda tabela [30, 10, 7, 13, 27, 38] jogos [30, 10, 7, 13, 27, 37] — a Wikipédia traz [30, 10, 7, 13, 25, 33]
- tabela publicada x jogos — alg83:26: USM Alger tabela [30, 9, 8, 13, 26, 34] jogos [30, 8, 10, 12, 25, 34] — a Wikipédia traz [30, 8, 10, 12, 21, 31]
- provável jogo da diferença: ES Sétif 2-0 USM Alger (1983-01-28, alg83:202); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- decidido fora de campo — RC Kouba NA Hussein Dey (1982-09-17): awarded 3-0
- decidido fora de campo — ES Sétif MC Oran (1982-09-24): awarded 3-0
- decidido fora de campo — MC Oran NA Hussein Dey (1982-10-01): awarded 3-0

### 1983/84

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg84:26: GC Mascara tabela [30, 15, 6, 9, 44, 36] jogos [31, 15, 6, 10, 44, 39] — a Wikipédia traz [30, 15, 6, 9, 44, 26]
- tabela publicada x jogos — alg84:26: ASO Chlef tabela [30, 12, 8, 10, 33, 24] jogos [29, 12, 7, 10, 33, 24] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg84:26: ES Sétif tabela [30, 12, 7, 11, 28, 30] jogos [30, 11, 7, 12, 27, 31] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg84:26: USM Bel-Abbès tabela [30, 11, 8, 11, 29, 25] jogos [30, 12, 7, 11, 29, 24] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg84:26: ASM Oran tabela [30, 10, 10, 10, 29, 30] jogos [31, 10, 11, 10, 29, 30] — a Wikipédia traz [30, 10, 10, 10, 32, 28]
- tabela publicada x jogos — alg84:26: MC Oran tabela [30, 9, 10, 11, 23, 23] jogos [30, 9, 10, 11, 24, 24] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg84:26: CR Belouizdad tabela [30, 10, 8, 12, 30, 35] jogos [30, 10, 7, 13, 29, 35] — a Wikipédia traz [30, 10, 8, 12, 30, 36]
- tabela publicada x jogos — alg84:26: RC Kouba tabela [30, 9, 10, 11, 28, 33] jogos [30, 9, 10, 11, 29, 33] — a Wikipédia traz [30, 9, 10, 11, 29, 34]
- tabela publicada x jogos — alg84:26: WKF Collo tabela [30, 9, 9, 12, 26, 31] jogos [30, 8, 10, 12, 25, 32] — a Wikipédia traz [30, 9, 9, 12, 25, 30]
- tabela publicada x jogos — alg84:26: JS Bordj Ménaïel tabela [30, 7, 13, 10, 23, 32] jogos [30, 7, 14, 9, 25, 33] — a Wikipédia traz [30, 7, 13, 10, 23, 33]
- tabela publicada x jogos — alg84:26: ES Guelma tabela [30, 8, 8, 14, 25, 50] jogos [29, 8, 10, 11, 26, 46] — a Wikipédia traz [30, 8, 8, 14, 24, 48]
- provável jogo da diferença: USM Bel-Abbès 1-0 CR Belouizdad (1983-09-02, alg84:48); com 1-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1984/85

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- tabela publicada x jogos — alg85:27: MC Oran tabela [38, 17, 10, 11, 38, 34] jogos [38, 18, 10, 10, 42, 32] — a Wikipédia traz [38, 17, 10, 11, 38, 35]
- tabela publicada x jogos — alg85:27: WKF Collo tabela [38, 18, 8, 12, 36, 30] jogos [37, 17, 8, 12, 34, 31] — a Wikipédia traz [38, 17, 10, 11, 43, 35]
- tabela publicada x jogos — alg85:27: ES Sétif tabela [38, 13, 15, 10, 38, 38] jogos [38, 12, 16, 10, 38, 39] — a Wikipédia traz [38, 12, 16, 10, 39, 39]
- tabela publicada x jogos — alg85:27: WA Tlemcen tabela [38, 16, 8, 14, 41, 34] jogos [38, 16, 9, 13, 42, 34] — a Wikipédia traz [38, 16, 9, 13, 41, 34]
- tabela publicada x jogos — alg85:27: ASM Oran tabela [38, 12, 15, 11, 34, 28] jogos [38, 11, 15, 12, 31, 31] — a Wikipédia traz [38, 12, 15, 11, 33, 27]
- tabela publicada x jogos — alg85:27: WA Boufarik tabela [38, 12, 15, 11, 37, 37] jogos [38, 12, 15, 11, 37, 36] — a Wikipédia traz [38, 12, 15, 11, 39, 35]
- tabela publicada x jogos — alg85:27: USM El Harrach tabela [38, 11, 16, 11, 38, 32] jogos [38, 11, 16, 11, 38, 33] — a Wikipédia traz [38, 11, 16, 11, 38, 31]
- tabela publicada x jogos — alg85:27: ASO Chlef tabela [38, 11, 16, 11, 25, 27] jogos [38, 11, 16, 11, 26, 27] — a Wikipédia traz [38, 11, 15, 12, 36, 40]
- tabela publicada x jogos — alg85:27: USM Annaba tabela [38, 10, 16, 12, 45, 48] jogos [38, 10, 16, 12, 46, 49] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg85:27: GC Mascara tabela [38, 13, 10, 15, 51, 55] jogos [38, 13, 11, 14, 51, 55] — a Wikipédia traz [38, 13, 10, 15, 50, 56]
- tabela publicada x jogos — alg85:27: AS Aïn M'lila tabela [38, 11, 14, 13, 25, 34] jogos [38, 11, 14, 13, 26, 34] — a Wikipédia traz [38, 11, 14, 13, 26, 33]
- tabela publicada x jogos — alg85:27: USM Bel-Abbès tabela [38, 12, 11, 15, 37, 40] jogos [37, 12, 11, 14, 37, 37] — a Wikipédia traz [38, 12, 11, 15, 46, 49]
- tabela publicada x jogos — alg85:27: RC Kouba tabela [38, 8, 13, 17, 31, 42] jogos [38, 7, 14, 17, 31, 44] — a Wikipédia traz [38, 8, 13, 17, 32, 44]
- provável jogo da diferença: WA Tlemcen 1-1 ES Sétif (1984-09-14, alg85:82); com 0-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: ES Sétif 1-1 WA Tlemcen (1985-01-04, alg85:310); com 1-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: ASO Chlef 2-0 USM El Harrach (1985-03-22, alg85:414); com 1-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- decidido fora de campo — MC Oran ASM Oran (1985-03-29): awarded 3-0

### 1985/86

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- ogol: 379 jogos casados (edição 27450 do ogol, 380 jogos)
- tabela publicada x jogos — alg86:26: JS Kabylie tabela [38, 27, 6, 5, 83, 20] jogos [38, 27, 6, 5, 89, 22] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg86:26: ASO Chlef tabela [38, 15, 12, 11, 39, 35] jogos [38, 15, 12, 11, 39, 36] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg86:26: CR Belouizdad tabela [38, 14, 13, 11, 45, 39] jogos [37, 14, 12, 11, 44, 38] — a Wikipédia traz [38, 14, 13, 11, 45, 37]
- tabela publicada x jogos — alg86:26: MC Oran tabela [38, 14, 11, 13, 39, 31] jogos [38, 14, 11, 13, 40, 31] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg86:26: RC Relizane tabela [38, 13, 13, 12, 38, 50] jogos [38, 13, 13, 12, 39, 50] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg86:26: ASM Oran tabela [38, 12, 13, 13, 34, 32] jogos [38, 12, 13, 13, 35, 32] — a Wikipédia traz [38, 12, 13, 13, 36, 30]
- tabela publicada x jogos — alg86:26: WA Tlemcen tabela [38, 14, 9, 15, 39, 47] jogos [38, 14, 9, 15, 39, 46] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg86:26: WA Boufarik tabela [38, 13, 10, 15, 37, 48] jogos [38, 13, 10, 15, 36, 48] — a Wikipédia traz [38, 13, 10, 15, 37, 49]
- tabela publicada x jogos — alg86:26: AS Aïn M'lila tabela [38, 12, 12, 14, 21, 35] jogos [38, 12, 12, 14, 21, 41] — a Wikipédia traz [38, 12, 12, 14, 22, 37]
- tabela publicada x jogos — alg86:26: USM Bel-Abbès tabela [38, 12, 8, 18, 42, 56] jogos [38, 12, 8, 18, 43, 57] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg86:26: DNC Alger tabela [38, 8, 15, 15, 38, 50] jogos [37, 8, 14, 15, 36, 48] — a Wikipédia traz [38, 11, 8, 19, 45, 58]

### 1986/87

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- ogol: 342 jogos casados (edição 27429 do ogol, 380 jogos)
- tabela publicada x jogos — alg87:26: ES Sétif tabela [38, 19, 10, 9, 40, 22] jogos [38, 19, 10, 9, 39, 24] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg87:26: MC Oran tabela [38, 13, 17, 8, 44, 32] jogos [38, 13, 17, 8, 38, 30] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg87:26: ASO Chlef tabela [38, 14, 15, 9, 43, 40] jogos [38, 14, 15, 9, 37, 40] — a Wikipédia traz [38, 14, 15, 9, 43, 34]
- tabela publicada x jogos — alg87:26: CR Belouizdad tabela [38, 15, 11, 12, 44, 35] jogos [38, 15, 11, 12, 45, 33] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg87:26: USM Annaba tabela [38, 15, 11, 12, 44, 32] jogos [38, 16, 10, 12, 44, 32] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg87:26: JS Kabylie tabela [38, 14, 13, 11, 45, 30] jogos [38, 14, 13, 11, 46, 30] — a Wikipédia traz [38, 14, 13, 11, 45, 31]
- tabela publicada x jogos — alg87:26: USM Aïn Beïda tabela [38, 14, 13, 11, 38, 37] jogos [38, 14, 12, 12, 38, 37] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg87:26: JS Bordj Ménaïel tabela [38, 14, 12, 12, 41, 42] jogos [38, 14, 12, 12, 38, 36] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg87:26: AS Aïn M'lila tabela [38, 14, 11, 13, 36, 37] jogos [38, 15, 9, 14, 35, 37] — a Wikipédia traz [38, 15, 10, 13, 36, 37]
- tabela publicada x jogos — alg87:26: MC Alger tabela [38, 13, 13, 12, 42, 37] jogos [38, 13, 13, 12, 40, 37] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg87:26: USM El Harrach tabela [38, 12, 14, 12, 41, 36] jogos [38, 12, 14, 12, 42, 33] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg87:26: RC Relizane tabela [38, 12, 14, 12, 44, 40] jogos [38, 11, 14, 13, 45, 47] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg87:26: WKF Collo tabela [38, 16, 6, 16, 34, 39] jogos [38, 17, 6, 15, 35, 38] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg87:26: WA Tlemcen tabela [38, 13, 12, 13, 32, 31] jogos [38, 11, 17, 10, 34, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg87:26: ASM Oran tabela [38, 10, 17, 11, 29, 29] jogos [38, 10, 17, 11, 30, 31] — a Wikipédia traz [38, 10, 17, 11, 29, 31]
- tabela publicada x jogos — alg87:26: ES Guelma tabela [38, 12, 13, 13, 33, 36] jogos [38, 13, 12, 13, 31, 33] — a Wikipédia traz [38, 12, 13, 13, 33, 32]
- tabela publicada x jogos — alg87:26: GC Mascara tabela [38, 10, 12, 16, 36, 43] jogos [38, 10, 11, 17, 34, 43] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg87:26: CS Constantine tabela [38, 8, 15, 15, 20, 41] jogos [38, 8, 14, 16, 22, 39] — a Wikipédia traz [38, 5, 18, 15, 22, 42]
- tabela publicada x jogos — alg87:26: MC Saïda tabela [38, 5, 18, 15, 22, 42] jogos [38, 5, 18, 15, 22, 41] — a Wikipédia traz [38, 8, 15, 15, 20, 38]
- tabela publicada x jogos — alg87:26: WA Boufarik tabela [38, 6, 15, 17, 22, 49] jogos [38, 6, 15, 17, 22, 47] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- decidido fora de campo — WA Tlemcen CS Constantine (1986-10-31): awarded 3-0; ineligible player Benabderrahmane Adlane; originally 2-2
- decidido fora de campo — CS Constantine WA Tlemcen (1987-03-26): awarded 0-3, CMC didn't appear on the field in protest

### 1987/88

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- ogol: 306 jogos casados (edição 27428 do ogol, 306 jogos)
- tabela publicada x jogos — alg88:27: JS Kabylie tabela [34, 10, 17, 7, 32, 23] jogos [34, 11, 16, 7, 33, 24] — a Wikipédia traz [34, 12, 13, 9, 31, 26]
- tabela publicada x jogos — alg88:27: USM Annaba tabela [34, 14, 7, 13, 40, 35] jogos [34, 14, 7, 13, 41, 38] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — alg88:27: USM El Harrach tabela [34, 8, 19, 7, 31, 26] jogos [34, 9, 19, 6, 34, 26] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — alg88:27: JS Bordj Ménaïel tabela [34, 12, 11, 11, 32, 28] jogos [34, 11, 12, 11, 32, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — alg88:27: JSM Tiaret tabela [34, 15, 5, 14, 38, 36] jogos [34, 14, 6, 14, 41, 39] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — alg88:27: RC Relizane tabela [34, 14, 8, 12, 36, 38] jogos [34, 12, 10, 12, 31, 39] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — alg88:27: AS Aïn M'lila tabela [34, 13, 9, 12, 26, 28] jogos [34, 13, 11, 10, 28, 25] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — alg88:27: USM Aïn Beïda tabela [34, 14, 7, 13, 30, 35] jogos [34, 14, 8, 12, 30, 32] — a Wikipédia traz [34, 13, 9, 12, 27, 27]
- tabela publicada x jogos — alg88:27: MC Alger tabela [34, 11, 12, 11, 27, 26] jogos [34, 11, 12, 11, 27, 25] — a Wikipédia traz [34, 11, 12, 11, 35, 26]
- tabela publicada x jogos — alg88:27: ES Sétif tabela [34, 11, 12, 11, 34, 25] jogos [34, 11, 12, 11, 35, 26] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg88:27: CR Belouizdad tabela [34, 5, 19, 10, 29, 38] jogos [34, 4, 20, 10, 28, 39] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — alg88:27: ASO Chlef tabela [34, 9, 11, 14, 26, 36] jogos [34, 9, 12, 13, 27, 34] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — alg88:27: WA Tlemcen tabela [34, 8, 13, 13, 20, 37] jogos [34, 7, 13, 14, 18, 38] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — alg88:27: JSM Skikda tabela [34, 8, 12, 14, 22, 37] jogos [34, 8, 12, 14, 22, 36] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)

### 1988/89

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- ogol: 237 jogos casados (edição 27449 do ogol, 240 jogos)
- tabela publicada x jogos — alg89:26: JS Kabylie tabela [30, 14, 9, 7, 36, 23] jogos [30, 14, 9, 7, 36, 22] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg89:26: MC Alger tabela [30, 14, 8, 8, 26, 20] jogos [30, 14, 8, 8, 26, 21] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg89:26: RC Relizane tabela [30, 12, 10, 8, 32, 28] jogos [30, 13, 8, 9, 29, 27] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — alg89:26: USM Bel-Abbès tabela [30, 12, 8, 10, 37, 32] jogos [29, 12, 8, 9, 36, 30] — faltam 1 jogo(s) do clube na fonte dos jogos
- tabela publicada x jogos — alg89:26: ASM Oran tabela [30, 11, 8, 11, 33, 28] jogos [29, 11, 5, 13, 31, 28] — faltam 1 jogo(s) do clube na fonte dos jogos
- tabela publicada x jogos — alg89:26: JS Bordj Ménaïel tabela [30, 12, 6, 12, 34, 32] jogos [30, 11, 6, 13, 32, 33] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — alg89:26: MC Oran tabela [30, 11, 7, 12, 35, 31] jogos [30, 12, 8, 10, 35, 28] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg89:26: JSM Tiaret tabela [30, 11, 7, 12, 35, 35] jogos [30, 12, 6, 12, 36, 37] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — alg89:26: RC Kouba tabela [30, 11, 7, 12, 26, 36] jogos [29, 11, 6, 12, 27, 36] — a Wikipédia traz [30, 11, 7, 12, 27, 37]
- tabela publicada x jogos — alg89:26: USM Annaba tabela [30, 9, 10, 11, 28, 28] jogos [29, 10, 8, 11, 28, 27] — faltam 1 jogo(s) do clube na fonte dos jogos
- tabela publicada x jogos — alg89:26: AS Aïn M'lila tabela [30, 8, 12, 10, 23, 23] jogos [30, 8, 11, 11, 23, 23] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — alg89:26: USM Alger tabela [30, 9, 10, 11, 26, 34] jogos [30, 12, 10, 8, 31, 30] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- tabela publicada x jogos — alg89:26: MO Constantine tabela [30, 9, 10, 11, 35, 32] jogos [30, 9, 8, 13, 34, 32] — a Wikipédia traz [30, 9, 9, 12, 35, 33]
- tabela publicada x jogos — alg89:26: USM Aïn Beïda tabela [30, 11, 5, 14, 34, 41] jogos [30, 10, 6, 14, 34, 41] — a Wikipédia traz [30, 11, 5, 14, 35, 41]
- tabela publicada x jogos — alg89:26: WKF Collo tabela [30, 8, 10, 12, 27, 36] jogos [30, 6, 10, 14, 23, 38] — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)
- corrigido — MC Alger x MO Constantine (1989-02-02): MC Alger 2-1 MO Constantine aparece duas vezes na rodada 16

### 1989/90

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- ogol: 240 jogos casados (edição 27445 do ogol, 240 jogos)
- tabela publicada x jogos — alg90:26: JS Kabylie tabela [30, 17, 5, 8, 40, 16] jogos [30, 17, 5, 8, 41, 16] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg90:26: MC Oran tabela [30, 14, 8, 8, 47, 27] jogos [30, 14, 8, 8, 46, 27] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg90:26: ES Sétif tabela [30, 12, 8, 10, 34, 31] jogos [30, 12, 8, 10, 33, 31] — a Wikipédia traz [30, 12, 8, 10, 33, 30]
- tabela publicada x jogos — alg90:26: JS Bordj Ménaïel tabela [30, 11, 10, 9, 31, 33] jogos [30, 11, 10, 9, 32, 33] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg90:26: RC Kouba tabela [30, 10, 9, 11, 27, 27] jogos [30, 11, 8, 11, 27, 26] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg90:26: CR Belouizdad tabela [30, 9, 11, 10, 16, 21] jogos [30, 9, 11, 10, 17, 21] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg90:26: JSM Tiaret tabela [30, 10, 8, 12, 29, 33] jogos [30, 10, 8, 12, 29, 32] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg90:26: USM Bel-Abbès tabela [30, 9, 10, 11, 19, 23] jogos [30, 9, 10, 11, 19, 24] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg90:26: USM Annaba tabela [30, 9, 10, 11, 27, 35] jogos [30, 9, 10, 11, 28, 35] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg90:26: USM El Harrach tabela [30, 10, 8, 12, 28, 34] jogos [30, 10, 8, 12, 28, 35] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg90:26: MO Constantine tabela [30, 11, 5, 14, 23, 32] jogos [30, 11, 5, 14, 24, 33] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg90:26: RC Relizane tabela [30, 7, 12, 11, 33, 31] jogos [30, 7, 11, 12, 32, 31] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg90:26: USM Alger tabela [30, 8, 7, 15, 23, 40] jogos [30, 8, 7, 15, 23, 41] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: JSM Tiaret 4-1 ES Sétif (1990-06-14, alg90:337); com 4-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: USM Alger 4-1 JS Bordj Ménaïel (1990-05-31, alg90:325); com 4-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: RC Kouba 1-0 RC Relizane (1990-04-26, alg90:279); com 1-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: USM Bel-Abbès 3-1 CR Belouizdad (1989-10-19, alg90:98); com 3-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: CR Belouizdad 1-2 USM El Harrach (1990-01-05, alg90:180); com 0-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: CR Belouizdad 3-0 USM Alger (1989-12-22, alg90:155); com 2-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: JSM Tiaret 2-0 RC Relizane (1990-05-24, alg90:319); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: USM El Harrach 3-2 USM Annaba (1990-04-05, alg90:250); com 3-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1990/91

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- ogol: 215 jogos casados (edição 27427 do ogol, 240 jogos)
- tabela publicada x jogos — alg91:29: ASM Oran tabela [30, 13, 10, 7, 33, 30] jogos [30, 13, 10, 7, 35, 31] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg91:29: AS Aïn M'lila tabela [30, 15, 6, 9, 35, 26] jogos [29, 15, 5, 9, 35, 28] — a Wikipédia traz [30, 15, 6, 9, 34, 27]
- tabela publicada x jogos — alg91:29: JS Kabylie tabela [30, 14, 6, 10, 33, 22] jogos [29, 14, 5, 10, 34, 24] — a Wikipédia traz [30, 14, 6, 10, 34, 23]
- tabela publicada x jogos — alg91:29: MC Alger tabela [30, 12, 8, 10, 36, 28] jogos [30, 12, 7, 11, 35, 28] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg91:29: USM El Harrach tabela [30, 10, 9, 11, 30, 28] jogos [30, 11, 9, 10, 31, 28] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg91:29: MC Oran tabela [30, 10, 9, 11, 40, 40] jogos [30, 10, 9, 11, 39, 39] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg91:29: WA Tlemcen tabela [30, 12, 4, 14, 30, 30] jogos [30, 12, 4, 14, 32, 30] — a Wikipédia traz [30, 12, 4, 14, 30, 31]
- tabela publicada x jogos — alg91:29: JSM Tiaret tabela [30, 8, 12, 10, 26, 31] jogos [30, 8, 12, 10, 24, 30] — a Wikipédia traz [30, 8, 12, 10, 26, 29]
- tabela publicada x jogos — alg91:29: USM Bel-Abbès tabela [30, 8, 12, 10, 24, 32] jogos [30, 8, 11, 11, 23, 32] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg91:29: CS Constantine tabela [30, 11, 6, 13, 33, 35] jogos [30, 11, 6, 13, 37, 37] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos

### 1991/92

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- ogol: 199 jogos casados (edição 27426 do ogol, 240 jogos)
- tabela publicada x jogos — alg92:26: MC Oran tabela [30, 16, 7, 7, 55, 33] jogos [30, 16, 7, 7, 55, 34] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg92:26: USM El Harrach tabela [30, 12, 11, 7, 29, 20] jogos [30, 12, 11, 7, 26, 19] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg92:26: WA Tlemcen tabela [30, 15, 5, 10, 34, 26] jogos [30, 14, 6, 10, 36, 26] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg92:26: NA Hussein Dey tabela [30, 12, 11, 7, 25, 17] jogos [30, 11, 12, 7, 24, 19] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg92:26: AS Aïn M'lila tabela [30, 15, 5, 10, 31, 26] jogos [30, 15, 5, 10, 32, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg92:26: ASM Oran tabela [30, 11, 9, 10, 40, 30] jogos [30, 10, 10, 10, 34, 30] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg92:26: ES Sétif tabela [30, 12, 7, 11, 33, 30] jogos [30, 12, 5, 13, 34, 33] — a Wikipédia traz [30, 12, 7, 11, 35, 32]
- tabela publicada x jogos — alg92:26: JS Bordj Ménaïel tabela [30, 11, 9, 10, 33, 32] jogos [30, 11, 9, 10, 33, 31] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg92:26: CR Belouizdad tabela [30, 11, 9, 10, 30, 29] jogos [30, 10, 10, 10, 36, 30] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg92:26: USM Annaba tabela [30, 10, 8, 12, 39, 41] jogos [30, 10, 9, 11, 39, 40] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg92:26: MO Constantine tabela [30, 9, 9, 12, 30, 34] jogos [30, 10, 8, 12, 32, 33] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg92:26: ES Guelma tabela [30, 8, 6, 16, 26, 40] jogos [30, 8, 6, 16, 26, 44] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg92:26: USM Bel-Abbès tabela [30, 7, 8, 15, 26, 45] jogos [30, 9, 7, 14, 27, 42] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg92:26: JSM Tiaret tabela [30, 7, 6, 17, 18, 47] jogos [30, 7, 7, 16, 19, 44] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- decidido fora de campo — WA Tlemcen NA Hussein Dey (1991-11-11): awarded 3-0; originally 1-0
- decidido fora de campo — JS Kabylie WA Tlemcen (1991-11-21): awarded 0-3 because of ineligible player JSK, originally 1-0
- decidido fora de campo — ES Sétif JSM Tiaret (1992-06-18): awarded 3-0; originally 1-0

### 1992/93

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- ogol: 192 jogos casados (edição 27425 do ogol, 240 jogos)
- tabela publicada x jogos — alg93:22: MC Oran tabela [30, 15, 8, 7, 43, 27] jogos [30, 14, 9, 7, 43, 31] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg93:22: NA Hussein Dey tabela [30, 13, 11, 6, 34, 21] jogos [30, 12, 12, 6, 32, 22] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg93:22: JS Kabylie tabela [30, 12, 13, 5, 37, 17] jogos [30, 12, 12, 6, 36, 17] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg93:22: US Chaouia tabela [30, 13, 9, 8, 35, 27] jogos [30, 14, 8, 8, 36, 26] — a Wikipédia traz [30, 14, 8, 8, 35, 26]
- tabela publicada x jogos — alg93:22: USM El Harrach tabela [30, 12, 9, 9, 29, 20] jogos [30, 11, 10, 9, 29, 22] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg93:22: AS Aïn M'lila tabela [30, 10, 11, 9, 26, 27] jogos [30, 10, 11, 9, 26, 26] — a Wikipédia traz [30, 9, 11, 10, 23, 26]
- tabela publicada x jogos — alg93:22: MC Alger tabela [30, 7, 15, 8, 25, 25] jogos [30, 7, 16, 7, 27, 21] — a Wikipédia traz [30, 7, 15, 8, 27, 23]
- tabela publicada x jogos — alg93:22: CR Belouizdad tabela [30, 9, 10, 11, 32, 25] jogos [30, 9, 10, 11, 32, 26] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg93:22: USM Blida tabela [30, 9, 10, 11, 27, 26] jogos [30, 9, 10, 11, 27, 27] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg93:22: ES Sétif tabela [30, 11, 5, 14, 27, 40] jogos [30, 11, 6, 13, 29, 39] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg93:22: MO Constantine tabela [30, 8, 6, 16, 20, 43] jogos [30, 8, 7, 15, 20, 43] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- decidido fora de campo — AS Aïn M'lila WA Tlemcen (1993-03-11): awarded 0-3; originally 2-2
- decidido fora de campo — AS Aïn M'lila USM Annaba (1992-10-14): awarded 3-0; USMAn forfait

### 1993/94

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- ogol: 240 jogos casados (edição 27424 do ogol, 240 jogos)
- tabela publicada x jogos — alg94:28: US Chaouia tabela [30, 15, 5, 10, 37, 30] jogos [30, 15, 5, 10, 36, 29] — a Wikipédia traz [26, 15, 5, 6, 37, 32]
- tabela publicada x jogos — alg94:28: WA Boufarik tabela [30, 13, 5, 12, 37, 32] jogos [30, 13, 5, 12, 38, 33] — a Wikipédia traz [30, 13, 5, 12, 37, 30]
- tabela publicada x jogos — alg94:28: MC Alger tabela [30, 9, 13, 8, 31, 27] jogos [30, 9, 14, 7, 30, 26] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg94:28: ES Sétif tabela [30, 8, 8, 14, 19, 31] jogos [30, 7, 9, 14, 20, 32] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: US Chaouia 0-0 MC Alger (1994-05-23, alg94:299); com 1-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: WA Boufarik 4-2 ES Sétif (1994-06-09, alg94:335); com 3-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar

### 1994/95

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- ogol: 232 jogos casados (edição 27444 do ogol, 240 jogos)
- tabela publicada x jogos — alg95:27: MC Oran tabela [30, 13, 9, 8, 42, 26] jogos [30, 13, 10, 7, 39, 26] — a Wikipédia traz [30, 13, 9, 8, 42, 28]
- tabela publicada x jogos — alg95:27: USM Blida tabela [30, 10, 13, 7, 37, 35] jogos [30, 10, 13, 7, 40, 37] — a Wikipédia traz [30, 10, 13, 7, 38, 36]
- tabela publicada x jogos — alg95:27: US Chaouia tabela [30, 11, 9, 10, 29, 22] jogos [31, 12, 9, 10, 30, 19] — a Wikipédia traz [30, 11, 9, 10, 39, 22]
- tabela publicada x jogos — alg95:27: MC Alger tabela [30, 8, 15, 7, 31, 32] jogos [30, 7, 15, 8, 31, 33] — a Wikipédia traz [30, 8, 15, 7, 34, 32]
- tabela publicada x jogos — alg95:27: JS Bordj Ménaïel tabela [30, 9, 11, 10, 25, 26] jogos [30, 8, 12, 10, 24, 26] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg95:27: AS Aïn M'lila tabela [30, 11, 7, 12, 28, 29] jogos [30, 11, 6, 13, 26, 31] — a Wikipédia traz [30, 11, 7, 12, 28, 31]
- tabela publicada x jogos — alg95:27: CA Batna tabela [30, 11, 7, 12, 22, 29] jogos [30, 11, 7, 12, 22, 28] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg95:27: GC Mascara tabela [30, 11, 5, 14, 33, 46] jogos [30, 11, 5, 14, 33, 43] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg95:27: NA Hussein Dey tabela [30, 8, 9, 13, 32, 48] jogos [30, 8, 9, 13, 32, 49] — a Wikipédia traz [30, 8, 9, 13, 33, 48]
- tabela publicada x jogos — alg95:27: ASO Chlef tabela [30, 6, 9, 15, 31, 39] jogos [29, 6, 10, 13, 30, 37] — a Wikipédia traz [30, 6, 9, 15, 30, 39]
- provável jogo da diferença: JS Bordj Ménaïel 0-0 CA Batna (1994-09-26, alg95:73); com 1-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- decidido fora de campo — NA Hussein Dey CS Constantine (1994-11-03): awarded 3-0 because of ineligible player CSC,
- decidido fora de campo — US Chaouia JS Kabylie (1995-03-30): awarded 3-0 US Chaouia; JSK refused played match for insecurity in the stadium

### 1995/96

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- ogol: 240 jogos casados (edição 27423 do ogol, 240 jogos)
- tabela publicada x jogos — alg96:27: MC Oran tabela [30, 17, 7, 6, 53, 24] jogos [30, 17, 7, 6, 54, 24] — a Wikipédia traz [30, 17, 7, 6, 53, 21]
- tabela publicada x jogos — alg96:27: JS Kabylie tabela [30, 13, 6, 11, 34, 29] jogos [30, 13, 6, 11, 32, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg96:27: CS Constantine tabela [30, 11, 10, 9, 25, 20] jogos [30, 11, 9, 10, 26, 24] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg96:27: USM El Harrach tabela [30, 12, 7, 11, 24, 26] jogos [30, 12, 7, 11, 25, 27] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg96:27: MC Alger tabela [30, 12, 4, 14, 29, 32] jogos [30, 12, 4, 14, 28, 32] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg96:27: US Chaouia tabela [30, 11, 6, 13, 28, 33] jogos [30, 12, 5, 13, 30, 34] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg96:27: CA Batna tabela [30, 12, 3, 15, 35, 44] jogos [30, 14, 3, 13, 40, 36] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg96:27: AS Aïn M'lila tabela [30, 10, 8, 12, 18, 30] jogos [30, 10, 8, 12, 19, 28] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg96:27: CR Belouizdad tabela [30, 10, 8, 12, 27, 34] jogos [30, 10, 9, 11, 29, 35] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg96:27: WA Boufarik tabela [30, 10, 5, 15, 25, 42] jogos [30, 9, 5, 16, 23, 46] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg96:27: USM Blida tabela [30, 9, 7, 14, 34, 36] jogos [30, 9, 6, 15, 33, 38] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg96:27: ASM Oran tabela [30, 8, 9, 13, 23, 31] jogos [30, 8, 9, 13, 26, 30] — a Wikipédia traz [30, 7, 10, 13, 23, 31]
- tabela publicada x jogos — alg96:27: JS Bordj Ménaïel tabela [30, 3, 11, 16, 22, 41] jogos [30, 2, 11, 17, 22, 44] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos

### 1996/97

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- "US Constantine" (rodadas 15 e 22) é o US Chaouia (erro de digitação da página)
- ogol: 240 jogos casados (edição 27422 do ogol, 240 jogos)
- tabela publicada x jogos — alg97:27: MC Oran tabela [30, 17, 4, 9, 49, 26] jogos [30, 17, 4, 9, 48, 26] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg97:27: USM El Harrach tabela [30, 12, 9, 9, 27, 22] jogos [30, 12, 9, 9, 26, 22] — a Wikipédia traz [30, 12, 9, 9, 27, 21]
- tabela publicada x jogos — alg97:27: JS Kabylie tabela [30, 12, 5, 13, 35, 41] jogos [30, 13, 4, 13, 34, 39] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg97:27: MO Constantine tabela [30, 10, 10, 10, 30, 29] jogos [30, 9, 11, 10, 30, 29] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg97:27: CA Batna tabela [30, 11, 6, 13, 28, 35] jogos [30, 11, 6, 13, 29, 35] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg97:27: US Chaouia tabela [30, 11, 5, 14, 27, 45] jogos [30, 11, 5, 14, 28, 46] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg97:27: WA Boufarik tabela [30, 10, 7, 13, 35, 36] jogos [30, 10, 7, 13, 33, 34] — a Wikipédia traz [30, 10, 7, 13, 34, 36]
- decidido fora de campo — NA Hussein Dey CR Belouizdad (1996-10-14): awarded 3-0; ineligible CRB player

### 1997/98

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- ninguém caiu: os desempates de rebaixamento não valeram, porque a 1ª divisão de 1998/99 passou a dois grupos de 14
- ninguém caiu: a 1ª divisão de 1998/99 passou a dois grupos de 14 (os desempates de rebaixamento não valeram)
- ogol: 113 jogos casados (edição 27421 do ogol, 115 jogos)
- tabela publicada x jogos — alg98:32: CS Constantine tabela [14, 7, 4, 3, 16, 11] jogos [13, 7, 4, 2, 16, 8] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg98:32: MC Oran tabela [14, 5, 3, 6, 20, 19] jogos [14, 5, 3, 6, 17, 20] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg98:32: CA Batna tabela [14, 4, 6, 4, 14, 14] jogos [14, 4, 6, 4, 13, 11] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg98:32: CR Belouizdad tabela [14, 5, 2, 7, 17, 19] jogos [14, 5, 2, 7, 18, 20] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg98:44: JS Kabylie tabela [14, 6, 4, 4, 14, 11] jogos [13, 6, 4, 3, 14, 8] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg98:44: USM Blida tabela [14, 1, 9, 4, 9, 13] jogos [13, 0, 9, 4, 6, 13] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- data diferente no ogol — WA Boufarik x USM Blida: RSSSF 1998-06-11, ogol 1998-06-18; fica a da RSSSF
- decidido fora de campo — CS Constantine MO Constantine (1998-01-01): CSC withdrew; awarded 0-3
- decidido fora de campo — MC Oran CS Constantine (1998-01-08): awarded 0-3, because of ineligible players MCO
- decidido fora de campo — MO Constantine CS Constantine (1998-04-16): Apr 17; awarded 0-3, because of ineligible players MOC
- decidido fora de campo — US Chaouia CA Batna (1998-05-14): awarded 0-3 because of ineligible player USC,
- abandonado/suspenso, sem valer — USM El Harrach CS Constantine (1998-06-11): awarded 3-0, abandoned in 80' at 1-0
- abandonado/suspenso, sem valer — USM Blida JS Kabylie (1998-06-11): awarded 3-0 abandoned in 33' at 1-1: Zane 16'; Kherroubi 13'
- não jogado — CS Constantine JS Kabylie (1998-06-11)

### 1998/99

- a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- ogol: 358 jogos casados (edição 27420 do ogol, 365 jogos)
- tabela publicada x jogos — alg99:28: JS Kabylie tabela [26, 16, 4, 6, 49, 17] jogos [26, 16, 4, 6, 49, 16] — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)
- tabela publicada x jogos — alg99:47: CR Belouizdad tabela [26, 16, 5, 5, 44, 22] jogos [26, 16, 5, 5, 44, 20] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg99:47: WA Tlemcen tabela [25, 14, 5, 6, 37, 17] jogos [24, 13, 5, 6, 34, 18] — a Wikipédia traz [26, 15, 5, 6, 40, 17]
- tabela publicada x jogos — alg99:47: MC Oran tabela [26, 12, 7, 7, 44, 25] jogos [26, 12, 7, 7, 42, 25] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg99:47: JSM Tiaret tabela [26, 6, 11, 9, 22, 18] jogos [26, 6, 11, 9, 22, 27] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg99:47: RC Kouba tabela [26, 7, 7, 12, 16, 25] jogos [26, 7, 7, 12, 17, 25] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg99:47: WA Boufarik tabela [25, 3, 7, 15, 16, 46] jogos [24, 3, 7, 14, 16, 43] — a Wikipédia traz [26, 3, 7, 16, 16, 49]
- provável jogo da diferença: MC Oran 2-1 CR Belouizdad (1998-12-03, alg99:387); com 4-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: CR Belouizdad 3-0 MC Oran (1999-04-22, alg99:798); com 3-2 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- decidido fora de campo — WA Boufarik WA Tlemcen (1998-12-17): abandoned at 0-0 in 81' due to attacks by some WA Boufarik players
- decidido fora de campo — CA Batna ES Sétif (1999-02-01): postponed Feb 1 due to bad weather, apparently later awarded 3-0
- decidido fora de campo — JS Kabylie NA Hussein Dey (1999-03-11): abandoned at 1-0 in 55', score: Saib Ramzi, awarded 3-0
- decidido fora de campo — AS Aïn M'lila JS Kabylie (1999-03-18): abandoned at 0-0 in 28', awarded 0-3
- abandonado/suspenso, sem valer — WA Tlemcen WA Boufarik (s/d): awarded 3-0; abandoned at 1-0 in 23'

### 1999/00

- ogol: 132 jogos casados (edição 27419 do ogol, 132 jogos)
- decidido fora de campo — CR Belouizdad CA Batna (2000-05-04): awarded 3-0

### 2000/01

- USM Blida x CS Constantine: a página corrigiu o placar para 1-0 ("correction from 2-0"), mas a tabela ainda conta o 2-0; fica o 1-0 corrigido
- ogol: 240 jogos casados (edição 27418 do ogol, 240 jogos)
- tabela publicada x jogos — alg01:27: USM Blida tabela [30, 14, 5, 11, 42, 30] jogos [30, 14, 5, 11, 41, 30] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg01:27: CS Constantine tabela [30, 4, 7, 19, 17, 45] jogos [30, 4, 7, 19, 17, 44] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- provável jogo da diferença: USM Blida 1-0 CS Constantine (2000-10-16, alg01:108); com 2-0 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- provável jogo da diferença: CS Constantine 2-0 USM Blida (2001-02-08, alg01:375); com 2-1 as linhas dos dois clubes fechariam com a tabela. Não corrigido: só a tabela indica o placar
- decidido fora de campo — CS Constantine MC Oran (2000-10-19): awarded 0-3; originally 3-1
- decidido fora de campo — USM El Harrach 1-0 CS Constantine (2001-02-01): abandoned in 85' due to throwing of projectiles; awarded 1-0
- decidido fora de campo — CR Belouizdad JSM Béjaïa (2001-06-07): awarded 3-0, forfait JSM Bejaia
- decidido fora de campo — USM Alger JS Kabylie (2001-06-21): awarded 3-0, forfait JS Kabylie
- decidido fora de campo — JS Kabylie WA Tlemcen (2001-06-25): awarded 0-3, forfait JS Kabylie

### 2001/02

- a tabela da RSSSF (e a da Wikipédia) não fecha com os jogos em quatro clubes; nenhum placar foi mudado
- ogol: 239 jogos casados (edição 27417 do ogol, 240 jogos)
- tabela publicada x jogos — alg02:27: CR Belouizdad tabela [30, 16, 4, 10, 45, 31] jogos [30, 16, 4, 10, 47, 33] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg02:27: MC Oran tabela [30, 13, 6, 11, 31, 28] jogos [30, 13, 6, 11, 31, 31] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg02:27: ES Sétif tabela [30, 12, 4, 14, 27, 30] jogos [30, 12, 4, 14, 30, 30] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg02:27: JSM Béjaïa tabela [30, 9, 11, 10, 21, 27] jogos [29, 9, 10, 10, 21, 27] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- decidido fora de campo — MC Oran ES Sétif (2001-09-10): awarded 0-3, because of ineligible player MCO
- decidido fora de campo — JS Kabylie CR Belouizdad (2001-09-13): awarded 3-0, CR Bélouizdad dns
- decidido fora de campo — CR Belouizdad AS Aïn M'lila (2001-10-30): awarded 3-0, ASAM showed late
- decidido fora de campo — CA Batna MC Alger (2002-06-24): awarded 3-0; MCA abandoned

### 2002/03

- ogol: 240 jogos casados (edição 27416 do ogol, 240 jogos)
- decidido fora de campo — USM Blida NA Hussein Dey (2003-01-20): awarded 3-0; abandoned at 1-0 in 65'

### 2003/04

- ogol: 239 jogos casados (edição 27443 do ogol, 240 jogos)
- decidido fora de campo — MC Oran NA Hussein Dey (2003-10-09): awarded 0-3; MCO turned up with two teams, led by

### 2004/05

- ogol: 237 jogos casados (edição 1101 do ogol, 240 jogos)
- data diferente no ogol — MC Alger x USM Annaba: RSSSF 2004-11-18, ogol 2004-11-25; fica a da RSSSF
- placar diferente no ogol — NA Hussein Dey x USM Alger (2005-06-02): RSSSF 1-2, ogol 0-1; fica o da RSSSF
- placar diferente no ogol — MC Alger x MC Oran (2005-06-02): RSSSF 2-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — GC Mascara x CA Bordj Bou Arréridj (2005-06-02): RSSSF 3-3, ogol 3-2; fica o da RSSSF
- placar diferente no ogol — WA Tlemcen x JS Kabylie (2005-06-02): RSSSF 3-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — CR Belouizdad x USM Annaba (2005-06-02): RSSSF 4-0, ogol 3-0; fica o da RSSSF
- abandonado/suspenso, sem valer — CS Constantine MC Oran (2005-02-17): 0-0; abd at 46' due to snow
- decidido fora de campo — US Chaouia WA Tlemcen (2005-04-18): awarded 0-3; originally 1-1;

### 2005/06

- ogol: 240 jogos casados (edição 27442 do ogol, 240 jogos)
- placar diferente no ogol — USM Annaba x CA Bordj Bou Arréridj (2005-12-15): RSSSF 2-0, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — USM Alger x MC Oran (2006-05-25): RSSSF 5-2, ogol 4-2; fica o da RSSSF
- placar diferente no ogol — CS Constantine x USM Blida (2006-05-25): RSSSF 2-1, ogol 2-0; fica o da RSSSF
- decidido fora de campo — JS Kabylie USM Alger (2005-10-03): awarded 3-0; 1-0, 45'; USMA dns after half-time and 3 pts deducted

### 2006/07

- ogol: 240 jogos casados (edição 27415 do ogol, 240 jogos)

### 2007/08

- ogol: 240 jogos casados (edição 2056 do ogol, 240 jogos)
- decidido fora de campo — ES Sétif JS Kabylie (2008-04-18): awarded 0-3, ESS dns

### 2008/09

- ogol: 255 jogos casados (edição 2391 do ogol, 272 jogos)
- data diferente no ogol — RC Kouba x USM El Harrach: RSSSF 2009-01-19, ogol 2009-01-09; fica a da RSSSF
- data diferente no ogol — USM Blida x RC Kouba: RSSSF 2009-05-14, ogol 2009-05-08; fica a da RSSSF
- data diferente no ogol — JSM Béjaïa x USM Alger: RSSSF 2009-05-14, ogol 2009-05-08; fica a da RSSSF
- decidido fora de campo — USM El Harrach ES Sétif (2009-01-30): awarded 0-3; abandoned
- decidido fora de campo — ES Sétif CA Bordj Bou Arréridj (2009-03-09): awarded 3-0; CABBA dns
- decidido fora de campo — ASO Chlef JS Kabylie (2009-05-14): awarded 0-3; abandoned

### 2009/10

- CA Bordj Bou Arréridj x MC Alger (14/08/2009): abandonado aos 72' com 1-0 e "awarded loss to both" (derrota dada aos dois); a tabela da RSSSF conta derrota para os dois, a da Wikipédia a vitória do CA Bordj Bou Arréridj; o jogo fica sem placar e a classificação é a tabela publicada
- ogol: 304 jogos casados (edição 9426 do ogol, 306 jogos)
- tabela publicada x jogos — alg2010:67: MC Alger tabela [34, 18, 12, 4, 50, 23] jogos [33, 18, 12, 3, 50, 22] — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos
- tabela publicada x jogos — alg2010:67: CA Bordj Bou Arréridj tabela [34, 12, 10, 12, 41, 45] jogos [33, 12, 10, 11, 40, 45] — a Wikipédia traz [34, 13, 10, 11, 41, 45]
- data diferente no ogol — MC El Eulma x AS Khroub: RSSSF 2009-12-15, ogol 2009-12-19; fica a da RSSSF
- data diferente no ogol — USM Alger x MC Oran: RSSSF 2009-12-15, ogol 2009-12-19; fica a da RSSSF
- decidido fora de campo — CA Bordj Bou Arréridj MC Alger (2009-08-14): awarded loss to both; Aug 15]                                    abandoned at 1-0 in 72'

### 2010/11

- ogol: 233 jogos casados (edição 18871 do ogol, 240 jogos)

### 2011/12

- ogol: 240 jogos casados (edição 27447 do ogol, 240 jogos)
- placar diferente no ogol — AS Khroub x MC Oran (2011-09-17): RSSSF 1-1, ogol 0-0; fica o da RSSSF
- data diferente no ogol — ES Sétif x CR Belouizdad: RSSSF 2012-04-04, ogol 2012-04-10; fica a da RSSSF
- placar diferente no ogol — NA Hussein Dey x USM Alger (2012-05-08): RSSSF 1-2, ogol 1-1; fica o da RSSSF

### 2012/13

- ogol: 240 jogos casados (edição 47638 do ogol, 240 jogos)
- placar diferente no ogol — CA Batna x USM Alger (2012-09-29): RSSSF 0-3, ogol 1-2; fica o da RSSSF
- data diferente no ogol — USM Bel-Abbès x MC Oran: RSSSF 2013-01-26, ogol 2013-02-01; fica a da RSSSF
- decidido fora de campo — JS Saoura USM El Harrach (2012-11-03): awarded 0-3; abd at 1-2
- decidido fora de campo — USM El Harrach MC Alger (2013-05-21): awarded 3-0, MCA dns

### 2013/14

- ogol: 238 jogos casados (edição 59388 do ogol, 240 jogos)
- placar diferente no ogol — JS Saoura x MC El Eulma (2014-02-08): RSSSF 3-2, ogol 3-0; fica o da RSSSF
- decidido fora de campo — CRB Aïn Fakroun USM El Harrach (2013-10-05): awarded 0-3; abandoned at 1-2 in 72'
- decidido fora de campo — MO Béjaïa USM Alger (2014-01-18): awarded 0-3; abandoned at 0-1 in 13' due to

### 2014/15

- ogol: 223 jogos casados (edição 70037 do ogol, 240 jogos)
- data diferente no ogol — NA Hussein Dey x CR Belouizdad: RSSSF 2014-10-17, ogol 2014-10-11; fica a da RSSSF

### 2015/16

- ogol: 240 jogos casados (edição 87506 do ogol, 240 jogos)
- data diferente no ogol — USM Alger x ES Sétif: RSSSF 2015-08-15, ogol 2015-08-25; fica a da RSSSF

### 2016/17

- ogol: 238 jogos casados (edição 98427 do ogol, 240 jogos)
- data diferente no ogol — MC Alger x JS Kabylie: RSSSF 2017-03-25, ogol 2017-04-01; fica a da RSSSF
- data diferente no ogol — CS Constantine x MC Alger: RSSSF 2017-05-20, ogol 2017-05-27; fica a da RSSSF
- decidido fora de campo — RC Relizane NA Hussein Dey (2016-08-20): awarded 0-3; Relizane dns
- decidido fora de campo — JS Saoura MO Béjaïa (2017-06-10): awarded 3-0; abandoned at 3-0 in 52' as

### 2017/18

- ogol: 238 jogos casados (edição 111558 do ogol, 240 jogos)
- data diferente no ogol — DRB Tadjenant x USM Bel-Abbès: RSSSF 2018-04-07, ogol 2018-04-13; fica a da RSSSF
- decidido fora de campo — MC Oran CR Belouizdad (2018-04-13): awarded 0-3, abandoned at 0-2 in 78' due to

### 2018/19

- ogol: 240 jogos casados (edição 125693 do ogol, 240 jogos)
- decidido fora de campo — CR Belouizdad AS Aïn M'lila (2018-08-11): awarded 0-3, CRB suspended due to

### 2019/20

- temporada interrompida (Covid-19)
- parada em 15/03/2020 pela Covid-19; a federação declarou o CR Belouizdad campeão pela média de pontos por jogo, sem rebaixamento
- ogol: 172 jogos casados (edição 138491 do ogol, 240 jogos)
- data diferente no ogol — MC Oran x NC Magra: RSSSF 2019-11-09, ogol 2019-11-02; fica a da RSSSF
- decidido fora de campo — MC Alger USM Alger (2019-10-12): awarded 3-0, USMA forfeited;
- decidido fora de campo — JS Kabylie CR Belouizdad (2019-09-24): awarded 0-3; abandoned at 0-3 in 79'
- decidido fora de campo — US Biskra MC Alger (2019-10-30): awarded 0-3 due to crowd trouble;

### 2020/21

- a tabela da RSSSF, a da Wikipédia e os jogos não fecham entre si em três clubes; nenhum placar foi mudado
- ogol: 380 jogos casados (edição 149614 do ogol, 380 jogos)
- tabela publicada x jogos — alg2021:26: ES Sétif tabela [38, 21, 8, 9, 68, 32] jogos [38, 22, 8, 8, 70, 30] — a Wikipédia traz [38, 21, 9, 8, 69, 32]
- tabela publicada x jogos — alg2021:26: JS Saoura tabela [38, 20, 9, 9, 62, 30] jogos [38, 21, 9, 8, 62, 30] — a Wikipédia traz [38, 20, 9, 9, 60, 30]
- tabela publicada x jogos — alg2021:26: RC Relizane tabela [38, 13, 11, 14, 37, 52] jogos [38, 13, 11, 14, 37, 51] — a Wikipédia traz [38, 13, 12, 13, 35, 49]
- placar diferente no ogol — Olympique Médéa x ES Sétif (2021-07-04): RSSSF 3-0, ogol 3-1; fica o da RSSSF
- decidido fora de campo — RC Relizane ES Sétif (2021-05-16): awarded 0-2 loss against Sétif for
- decidido fora de campo — AS Aïn M'lila JS Kabylie (2021-05-30): awarded 0-3, originally 1-1; ASAM fielded

### 2021/22

- ogol: 306 jogos casados (edição 159498 do ogol, 306 jogos)

### 2022/23

- ogol: 240 jogos casados (edição 166611 do ogol, 240 jogos)

### 2023/24

- ogol: 239 jogos casados (edição 177582 do ogol, 240 jogos)
- decidido fora de campo — US Souf ES Ben Aknoun (2024-03-02): awarded 0-3; abandoned at 0-1 at half-time as

### 2024/25

- ogol: 240 jogos casados (edição 187994 do ogol, 240 jogos)
- data diferente no ogol — US Biskra x CR Belouizdad: RSSSF 2024-10-06, ogol 2024-09-26; fica a da RSSSF
- data diferente no ogol — USM Khenchela x ES Mostaganem: RSSSF 2024-10-06, ogol 2024-09-26; fica a da RSSSF

### 2025/26

- dois placares da lista da RSSSF corrigidos pelo ogol (as tabelas da RSSSF e da Wikipédia só fecham com eles)
- ogol: 213 jogos casados (edição 203482 do ogol, 240 jogos)
- corrigido — Olympique Akbou x MC Alger (2025-10-12): Olympique Akbou 0-1 MC Alger (ogol; as tabelas da RSSSF e da Wikipédia só fecham assim); a lista da RSSSF dá 1-0
- corrigido — CS Constantine x ES Sétif (2026-02-13): CS Constantine 2-0 ES Sétif (ogol; as tabelas da RSSSF e da Wikipédia só fecham assim); a lista da RSSSF dá 1-0
- data diferente no ogol — JS Saoura x MC El Bayadh: RSSSF 2025-12-20, ogol 2025-12-26; fica a da RSSSF
- data diferente no ogol — USM Khenchela x CS Constantine: RSSSF 2025-12-20, ogol 2025-12-26; fica a da RSSSF
- placar diferente no ogol — CS Constantine x ES Sétif (2026-02-13): RSSSF 1-0, ogol 2-0; fica o da RSSSF

