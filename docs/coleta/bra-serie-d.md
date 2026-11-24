# Série D — coleta de dados

Gerado por `python coleta/bra-serie-d/importar.py`. Pacote em `data/coleta/bra-serie-d/pacote/`. Método e código iguais aos
da Série C (`docs/coleta/bra-serie-c.md`).

**Edições:** 18, de 2009 a 2026, conferidas na RSSSF Brasil (lista de campeões da 4ª divisão, até 2023) e na Wikipédia em
português (artigo da Série D, até 2025). Os campeões de 2009 a 2023 são os mesmos nas duas. Nome oficial: Campeonato
Brasileiro Série D.

**Fontes:** RSSSF Brasil (`br{ano}l4.htm`: base de jogos, fases, grupos, datas e autores; as tabelas publicadas são a
conferência); ogol (calendário de todas as edições e o código de cada clube, que dá a identidade; completa os jogos que faltam
na RSSSF); Wikipédia (punições de pontos, lista de campeões, promovidos e artilheiros). A ESPN não tem a Série D.

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,
fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` usa o nome de lá;
clube que já apareceu na Série C usa o mesmo nome do pacote da Série C (cadastro comum `data/coleta/comum/clubes_ogol.json`).

**Fases e grupos (revisão SD-004 a SD-009):** saem do código de cada jogo no ogol, que tem a estrutura completa da Série D
(grupos numerados; FP, 2F, 3F, 1/8, QF, SF e F para o mata-mata). As páginas da RSSSF perdem grupos (2018, 2020, 2022),
juntam fases (2011) e põem jogos de mata-mata em grupos (2021). O nome do grupo é o da RSSSF quando ela o dá certo.

**Classificação final (revisão SD-002, SD-003):** campeão e vice em cima; depois a fase alcançada; na mesma fase, a
posição no grupo dela e a campanha toda. A ordem geral da RSSSF, quando existe, só desempata dentro da mesma fase.

| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|---|
| 2009 | RSSSF + ogol | 39 | 158 (158) | 421 | 383 | 19 / 2 | São Raimundo-PA | RSSSF (classificação geral publicada) |
| 2010 | RSSSF + ogol | 40 | 164 (164) | 436 | 397 | 10 / 1 | Guarany | RSSSF (classificação geral publicada) |
| 2011 | RSSSF + ogol | 40 | 190 (190) | 493 | 471 | 10 / 0 | Tupi | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2012 | RSSSF + ogol | 40 | 190 (190) | 483 | 0 | 9 / 0 | Sampaio Corrêa | RSSSF (classificação geral publicada) |
| 2013 | RSSSF + ogol | 40 | 190 (190) | 475 | 458 | 17 / 0 | Botafogo-PB | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2014 | RSSSF + ogol | 41 | 200 (200) | 515 | 506 | 23 / 0 | Tombense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2015 | RSSSF + ogol | 40 | 190 (190) | 427 | 419 | 23 / 0 | Botafogo-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2016 | RSSSF + ogol | 68 | 266 (266) | 669 | 650 | 48 / 0 | Volta Redonda | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2017 | RSSSF + ogol | 68 | 266 (266) | 631 | 617 | 48 / 0 | Operário-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2018 | RSSSF + ogol | 68 | 266 (266) | 677 | 677 | 48 / 0 | Ferroviário-CE | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2019 | RSSSF + ogol | 68 | 266 (266) | 639 | 619 | 48 / 0 | Brusque | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2020 | RSSSF + ogol | 68 | 518 (518) | 1392 | 1247 | 12 / 0 | Mirassol | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2021 | RSSSF + ogol | 68 | 518 (518) | 1259 | 271 | 0 / 0 | Aparecidense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2022 | RSSSF + ogol | 64 | 510 (510) | 1154 | 1131 | 39 / 0 | América-RN | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2023 | RSSSF + ogol | 64 | 510 (510) | 1191 | 1117 | 0 / 0 | Ferroviário-CE | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2024 | RSSSF + ogol | 64 | 510 (510) | 1143 | 1130 | 38 / 1 | Retrô FC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2025 | RSSSF + ogol | 64 | 510 (510) | 1148 | 1134 | 39 / 0 | Barra-SC | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2026 | ogol | 96 | 610 (610) | 1389 | 0 | 0 / 0 | Uberlândia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |

## Conferência e correções, ano a ano

### 2009

- tabela publicada x jogos — Primeira fase / Grupo 1: Genus tabela [4, 2, 0, 2, 6, 5] jogos [4, 2, 0, 2, 7, 5] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo 1: Atlético Roraima tabela [4, 1, 0, 3, 3, 6] jogos [4, 1, 0, 3, 3, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Genus tabela [6, 2, 1, 3, 7, 8] jogos [6, 2, 1, 3, 8, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Atlético Roraima tabela [4, 1, 0, 3, 3, 6] jogos [4, 1, 0, 3, 3, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, São Raimundo-PA

### 2010

- tabela publicada x jogos — Segunda fase / -: Metropolitano tabela [8, 3, 3, 2, 11, 8] jogos [8, 3, 2, 3, 11, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- 13 datas corrigidas (datas_corrigidas.csv; ex.: São José-RS x Operário-PR 2010-07-18 -> 2010-07-17, Bola n@ Área e transfermarkt (QC-003))

### 2011

- dois jogos da página foram anulados e ficam de fora (motivo abaixo); com isso, jogos e tabelas batem com o ogol
- jogo anulado fica de fora (1): Anapolina 4-1 Tocantinópolis — 1ª fase: anulado pelo STJD (o Tocantinópolis terminou com 6 jogadores); o jogo foi refeito em 17/10 (6-1), e a tabela do grupo A5 conta só o novo jogo
- jogo anulado fica de fora (1): Itumbiara 3-1 Villa Nova — 2ª fase: jogado em 25/09 e anulado depois que o jogo Anapolina x Tocantinópolis da 1ª fase foi refeito (nota da página da RSSSF)
- jogo corrigido à mão — Oeste x Cianorte: pênaltis 4-3 (Bola n@ Área e transfermarkt; revisão QC-001)
- jogo corrigido à mão — Mirassol x Oeste: pênaltis 3-4 (Bola n@ Área e transfermarkt; revisão QC-001)
- fases e grupos pelo ogol em 18 jogos: Segunda fase/- → Oitavas de final/- (16); Semifinal/- → Final/- (2)

### 2012

- a página da RSSSF não traz os autores dos gols
- jogo corrigido à mão — Cianorte x Mogi Mirim: pênaltis 2-4 (Bola n@ Área e transfermarkt; revisão QC-001)
- fases e grupos pelo ogol em 16 jogos: Segunda fase/- → Oitavas de final/- (16)

### 2013

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Botafogo-PB x Salgueiro, ogol 2013-09-06); fica a do ogol
- jogo corrigido à mão — Botafogo-PB x Salgueiro: volta da semifinal em 06/10 (súmula da CBF, jogo 186; Bola e transfermarkt; revisão SD-011)
- fases e grupos pelo ogol em 30 jogos: Terceira fase/Grupo C1 → Quartas de final/- (4); Segunda fase/Grupo B1 → Oitavas de final/- (2); Segunda fase/Grupo B2 → Oitavas de final/- (2); Segunda fase/Grupo B3 → Oitavas de final/- (2); Segunda fase/Grupo B4 → Oitavas de final/- (2); Segunda fase/Grupo B5 → Oitavas de final/- (2); Segunda fase/Grupo B6 → Oitavas de final/- (2); Segunda fase/Grupo B7 → Oitavas de final/- (2) ...

### 2014

- jogo corrigido à mão — Itaporã x Villa Nova-MG: W.O.: o Itaporã abandonou a competição (revisão SD-013)
- jogo corrigido à mão — Anapolina x Itaporã: W.O.: o Itaporã abandonou a competição (revisão SD-013)
- jogo corrigido à mão — Barueri x CEOV Operário: W.O. (revisão SD-013)
- jogo corrigido à mão — Rio Branco-AC x Anapolina: pênaltis 12-13 (Bola n@ Área e transfermarkt; revisão QC-001)
- fases e grupos pelo ogol em 30 jogos: Segunda fase/Grupo B1 → Oitavas de final/- (2); Segunda fase/Grupo B2 → Oitavas de final/- (2); Segunda fase/Grupo B3 → Oitavas de final/- (2); Segunda fase/Grupo B4 → Oitavas de final/- (2); Segunda fase/Grupo B5 → Oitavas de final/- (2); Segunda fase/Grupo B6 → Oitavas de final/- (2); Segunda fase/Grupo B7 → Oitavas de final/- (2); Segunda fase/Grupo B8 → Oitavas de final/- (2) ...

### 2015

- fases e grupos pelo ogol em 30 jogos: Segunda fase/Grupo B1 → Oitavas de final/- (2); Segunda fase/Grupo B2 → Oitavas de final/- (2); Segunda fase/Grupo B3 → Oitavas de final/- (2); Segunda fase/Grupo B4 → Oitavas de final/- (2); Segunda fase/Grupo B5 → Oitavas de final/- (2); Segunda fase/Grupo B6 → Oitavas de final/- (2); Segunda fase/Grupo B7 → Oitavas de final/- (2); Segunda fase/Grupo B8 → Oitavas de final/- (2) ...

### 2016

- as tabelas desta página (e de 2017 a 2019) têm uma coluna a mais ('PTS J PE V E D'); o leitor reconhece essa ordem
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: CSA x Volta Redonda, ogol 2016-09-29); fica a do ogol
- jogo corrigido à mão — CSA x Volta Redonda: a ida da final foi em 25/09 (borderô da CBF; revisão SD-012)
- fases e grupos pelo ogol em 62 jogos: Primeira fase/- → Primeira fase/Grupo A11 (6); Segunda fase/Grupo B09 → Segunda fase/- (2); Segunda fase/Grupo B14 → Segunda fase/- (2); Segunda fase/Grupo B13 → Segunda fase/- (2); Segunda fase/Grupo B15 → Segunda fase/- (2); Segunda fase/Grupo B07 → Segunda fase/- (2); Segunda fase/Grupo B12 → Segunda fase/- (2); Segunda fase/Grupo B11 → Segunda fase/- (2) ...

### 2017

- fases e grupos pelo ogol em 66 jogos: Primeira fase/- → Primeira fase/Grupo A11 (6); Terceira fase/- → Oitavas de final/- (4); Segunda fase/Grupo B14 → Segunda fase/- (2); Segunda fase/Grupo B09 → Segunda fase/- (2); Segunda fase/Grupo B12 → Segunda fase/- (2); Segunda fase/Grupo B15 → Segunda fase/- (2); Segunda fase/Grupo B10 → Segunda fase/- (2); Segunda fase/Grupo B03 → Segunda fase/- (2) ...

### 2018

- fases e grupos pelo ogol em 266 jogos: Segunda fase/Grupo B0 → Segunda fase/- (18); Terceira fase/Grupo C0 → Oitavas de final/- (16); Segunda fase/Grupo B1 → Segunda fase/- (14); Primeira fase/Grupo A1 → Primeira fase/Grupo A14 (12); Primeira fase/Grupo A1 → Primeira fase/Grupo A10 (12); Primeira fase/Grupo A1 → Primeira fase/Grupo A11 (12); Primeira fase/Grupo A0 → Primeira fase/Grupo A07 (12); Primeira fase/Grupo A1 → Primeira fase/Grupo A17 (12) ...

### 2019

- fases e grupos pelo ogol em 60 jogos: Segunda fase/Grupo B07 → Segunda fase/- (2); Segunda fase/Grupo B12 → Segunda fase/- (2); Segunda fase/Grupo B06 → Segunda fase/- (2); Segunda fase/Grupo B10 → Segunda fase/- (2); Segunda fase/Grupo B15 → Segunda fase/- (2); Segunda fase/Grupo B04 → Segunda fase/- (2); Segunda fase/Grupo B13 → Segunda fase/- (2); Segunda fase/Grupo B08 → Segunda fase/- (2) ...

### 2020

- a página da RSSSF parou no meio da 2ª fase (472 dos 518 jogos); o resto vem do ogol
- 8 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência
- jogo só no ogol, incluído em Second Phase: Bragantino-PA 1-1 Juventude-MA (2020-12-12)
- jogo só no ogol, incluído em Second Phase: Itabaiana 2-2 Floresta-CE (2020-12-12)
- jogo só no ogol, incluído em Second Phase: ABC 1-1 Globo FC (2020-12-12)
- jogo só no ogol, incluído em Second Phase: Brasiliense 3-0 Real Noroeste (2020-12-12)
- jogo só no ogol, incluído em Second Phase: Goiânia 3-2 Atlético-BA (2020-12-12)
- jogo só no ogol, incluído em Second Phase: Novorizontino 3-0 FC Cascavel (2020-12-12)
- jogo só no ogol, incluído em Second Phase: América-RN 5-0 Coruripe (2020-12-13)
- jogo só no ogol, incluído em Second Phase: Mirassol 1-0 Caxias (2020-12-13)
- jogo só no ogol, incluído em Second Phase: Altos 3-1 Rio Branco-AC (2020-12-13)
- jogo só no ogol, incluído em Second Phase: Gama 1-2 Goianésia (2020-12-13)
- jogo só no ogol, incluído em Second Phase: River-PI 0-1 Galvez EC (2020-12-13)
- jogo só no ogol, incluído em Second Phase: Aparecidense 4-0 Tupynambás (2020-12-13)
- jogo só no ogol, incluído em Second Phase: São Luiz 2-0 Cabofriense (2020-12-13)
- jogo só no ogol, incluído em Second Phase: Ferroviária-SP 1-2 Marcílio Dias (2020-12-13)
- jogo só no ogol, incluído em Second Phase: Fast-AM 1-1 Moto Club (2020-12-13)
- jogo só no ogol, incluído em Second Phase: Salgueiro 4-0 Vitória da Conquista (2020-12-13)
- jogo só no ogol, incluído em Second Phase: Marcílio Dias 2-1 Goianésia (2020-12-19)
- jogo só no ogol, incluído em Second Phase: Goiânia 1-1 Novorizontino (2020-12-19)
- jogo só no ogol, incluído em Second Phase: Globo FC 2-1 Fast-AM (2020-12-20)
- jogo só no ogol, incluído em Second Phase: Juventude-MA 2-2 Floresta-CE (2020-12-20)
- jogo só no ogol, incluído em Second Phase: Mirassol 4-0 Brasiliense (2020-12-20)
- jogo só no ogol, incluído em Second Phase: Salgueiro 1-1 Altos (2020-12-20)
- jogo só no ogol, incluído em Second Phase: São Luiz 0-4 Aparecidense (2020-12-20)
- jogo só no ogol, incluído em Second Phase: Galvez EC 1-1 América-RN (2020-12-20)
- jogo só no ogol, incluído em Second Phase: Fast-AM 1-0 Globo FC (2020-12-26)
- jogo só no ogol, incluído em Second Phase: Brasiliense 2-1 Mirassol (2020-12-27)
- jogo só no ogol, incluído em Second Phase: Altos 1-1 Salgueiro (2020-12-27)
- jogo só no ogol, incluído em Second Phase: Floresta-CE 2-0 Juventude-MA (2020-12-27)
- jogo só no ogol, incluído em Second Phase: América-RN 5-1 Galvez EC (2020-12-27)
- jogo só no ogol, incluído em Second Phase: Goianésia 1-1 Marcílio Dias (2020-12-27)
- jogo só no ogol, incluído em Second Phase: Aparecidense 1-2 São Luiz (2020-12-27)
- jogo só no ogol, incluído em Second Phase: Novorizontino 4-0 Goiânia (2020-12-27)
- jogo só no ogol, incluído em Second Phase: Floresta-CE 2-0 América-RN (2021-01-02)
- jogo só no ogol, incluído em Second Phase: Mirassol 2-1 Aparecidense (2021-01-02)
- jogo só no ogol, incluído em Second Phase: Marcílio Dias 1-1 Altos (2021-01-03)
- jogo só no ogol, incluído em Second Phase: Fast-AM 0-1 Novorizontino (2021-01-03)
- jogo só no ogol, incluído em Second Phase: Aparecidense 2-3 Mirassol (2021-01-09)
- jogo só no ogol, incluído em Second Phase: Altos 5-1 Marcílio Dias (2021-01-10)
- jogo só no ogol, incluído em Second Phase: Novorizontino 3-0 Fast-AM (2021-01-10)
- jogo só no ogol, incluído em Second Phase: América-RN 1-1 Floresta-CE (2021-01-10)
- jogo só no ogol, incluído em Second Phase: Floresta-CE 1-1 Novorizontino (2021-01-16)
- jogo só no ogol, incluído em Second Phase: Mirassol 4-0 Altos (2021-01-17)
- jogo só no ogol, incluído em Second Phase: Novorizontino 0-2 Floresta-CE (2021-01-23)
- jogo só no ogol, incluído em Second Phase: Altos 0-1 Mirassol (2021-01-24)
- jogo só no ogol, incluído em Second Phase: Floresta-CE 0-1 Mirassol (2021-01-30)
- jogo só no ogol, incluído em Second Phase: Mirassol 1-0 Floresta-CE (2021-02-06)
- jogo corrigido à mão — Bragantino-PA x Juventude-MA: pênaltis 3-4 (Bola n@ Área e transfermarkt; revisão QC-001)
- jogo corrigido à mão — Mirassol x Caxias: pênaltis 3-0 (Bola n@ Área e transfermarkt; revisão QC-001)
- jogo corrigido à mão — Fast-AM x Moto Club: pênaltis 6-5 (Bola n@ Área e transfermarkt; revisão QC-001)
- jogo corrigido à mão — Fast-AM x Globo FC: pênaltis 6-5 (Bola n@ Área e transfermarkt; revisão QC-001)
- jogo corrigido à mão — Altos x Salgueiro: pênaltis 4-2 (Bola n@ Área e transfermarkt; revisão QC-001)
- fases e grupos pelo ogol em 486 jogos: Primeira fase/Grupo A → Primeira fase/Grupo A6 (56); Primeira fase/Grupo A → Primeira fase/Grupo A5 (56); Primeira fase/Grupo A → Primeira fase/Grupo A8 (56); Primeira fase/Grupo A → Primeira fase/Grupo A1 (56); Primeira fase/Grupo A → Primeira fase/Grupo A3 (56); Primeira fase/Grupo A → Primeira fase/Grupo A7 (56); Primeira fase/Grupo A → Primeira fase/Grupo A2 (56); Primeira fase/Grupo A → Primeira fase/Grupo A4 (56) ...

### 2021

- clubes, grupos e jogos que faltam vêm do ogol; os autores dos gols só existem nos 103 jogos da página
- a página da RSSSF parou na 3ª rodada da 1ª fase (103 dos 518 jogos); as tabelas dela são parciais e não servem de conferência; os jogos que faltam vêm do ogol
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Santo André 1-1 São Bento (2021-06-26)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Marcílio Dias 1-1 Joinville (2021-06-26)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Gama 0-3 Nova Mutum (2021-06-26)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Imperatriz 1-1 Juventude-MA (2021-06-26)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Palmas 1-2 4 de Julho (2021-06-26)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Caucaia 2-2 América-RN (2021-06-26)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Gazin Porto Velho EC 0-1 Goianésia (2021-06-26)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Aparecidense 1-0 Jaraguá (2021-06-26)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Caldense 3-1 Uberlândia (2021-06-26)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: CA Patrocinense 1-3 Boa Esporte (2021-06-26)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: União-MT 2-1 Brasiliense (2021-06-26)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Inter de Limeira 1-1 Portuguesa (2021-06-26)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: GAS 2-2 Castanhal (2021-06-26)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Esportivo-RS 1-1 Caxias (2021-06-26)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Central 0-1 Campinense (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: ABC 0-2 Atlético Cearense (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Bangu 0-2 Boavista-RJ (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Aimoré 1-3 FC Cascavel (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Juventus Jaraguá 0-0 Rio Branco-PR (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Rio Branco-ES 0-3 Ferroviária-SP (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Ypiranga-AP 0-1 São Raimundo-RR (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Penarol-AM 2-0 Galvez EC (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Paragominas 2-2 Moto Club (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Treze 1-1 Sousa (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Bahia de Feira 1-1 Retrô FC (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Juazeirense 1-0 Atlético-BA (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Sergipe 2-1 Murici (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: ASA 0-2 Itabaiana (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Águia Negra 2-2 Rio Branco de Venda Nova (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Cianorte 0-0 Madureira (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Tocantinópolis 4-2 Guarany (2021-06-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Atlético-AC 0-0 Fast-AM (2021-06-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Águia Negra 4-1 CA Patrocinense (2021-06-30)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Castanhal 2-1 Ypiranga-AP (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Guarany 3-1 4 de Julho (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Campinense 0-0 Treze (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: América-RN 2-0 Atlético Cearense (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Boavista-RJ 1-1 Cianorte (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Brasiliense 0-0 Gama (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Juventude-MA 1-3 Paragominas (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Caucaia 3-2 ABC (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Atlético-BA 2-2 Bahia de Feira (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: ASA 1-3 Sergipe (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Aparecidense 0-1 Gazin Porto Velho EC (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: FC Cascavel 2-1 Esportivo-RS (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Tocantinópolis 1-4 Palmas (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Ferroviária-SP 7-0 Águia Negra (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Boa Esporte 2-2 Uberlândia (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Inter de Limeira 1-2 Santo André (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: São Raimundo-RR 1-1 GAS (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Fast-AM 1-2 Galvez EC (2021-07-03)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Madureira 1-0 Bangu (2021-07-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Caxias 2-1 Aimoré (2021-07-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Juventus Jaraguá 2-0 Marcílio Dias (2021-07-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Rio Branco-PR 0-0 Joinville (2021-07-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Rio Branco de Venda Nova 0-0 Rio Branco-ES (2021-07-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Moto Club 1-1 Imperatriz (2021-07-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Jaraguá 0-3 Goianésia (2021-07-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Sousa 0-0 Central (2021-07-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Retrô FC 0-0 Juazeirense (2021-07-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Itabaiana 1-0 Murici (2021-07-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Nova Mutum 1-0 União-MT (2021-07-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Atlético-AC 1-2 Penarol-AM (2021-07-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Portuguesa 2-0 São Bento (2021-07-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: CA Patrocinense 2-3 Caldense (2021-07-05)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Castanhal 3-1 Atlético-AC (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Atlético Cearense 2-3 Campinense (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Bangu 2-1 Portuguesa (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Santo André 1-0 Cianorte (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Marcílio Dias 2-1 Esportivo-RS (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Joinville 2-0 Caxias (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Brasiliense 1-2 Aparecidense (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Imperatriz 1-0 Guarany (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Palmas 0-0 Paragominas (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Sousa 7-0 Caucaia (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Murici 2-3 Atlético-BA (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: União-MT 2-1 Jaraguá (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Goianésia 1-0 Nova Mutum (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Caldense 6-2 Águia Negra (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: São Bento 1-1 Madureira (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: FC Cascavel 1-0 Juventus Jaraguá (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: 4 de Julho 2-0 Moto Club (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Gazin Porto Velho EC 1-1 Gama (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Ferroviária-SP 1-0 CA Patrocinense (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: GAS 3-2 Fast-AM (2021-07-10)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Aimoré 1-0 Rio Branco-PR (2021-07-11)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Rio Branco-ES 1-2 Boa Esporte (2021-07-11)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Juventude-MA 3-3 Tocantinópolis (2021-07-11)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Penarol-AM 1-1 Ypiranga-AP (2021-07-11)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Treze 2-2 América-RN (2021-07-11)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: ABC 2-0 Central (2021-07-11)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Bahia de Feira 0-1 Itabaiana (2021-07-11)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Sergipe 0-1 Juazeirense (2021-07-11)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Retrô FC 3-3 ASA (2021-07-11)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Uberlândia 2-1 Rio Branco de Venda Nova (2021-07-11)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Boavista-RJ 0-1 Inter de Limeira (2021-07-11)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Galvez EC 0-1 São Raimundo-RR (2021-07-11)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Guarany 2-1 Juventude-MA (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: América-RN 4-1 Sousa (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Campinense 0-1 ABC (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Madureira 1-0 Santo André (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Moto Club 1-0 Palmas (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Gama 0-0 Goianésia (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Ypiranga-AP 0-1 Galvez EC (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Caucaia 0-4 Treze (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Juazeirense 2-1 Murici (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Aparecidense 1-1 União-MT (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Cianorte 1-0 São Bento (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Tocantinópolis 0-0 Imperatriz (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Fast-AM 1-2 Castanhal (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: São Raimundo-RR 2-1 Penarol-AM (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Boa Esporte 0-0 Ferroviária-SP (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Inter de Limeira 0-1 Bangu (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Portuguesa 3-0 Boavista-RJ (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Esportivo-RS 0-1 Joinville (2021-07-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Central 1-3 Atlético Cearense (2021-07-18)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Rio Branco de Venda Nova 3-0 Caldense (2021-07-18)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Juventus Jaraguá 1-0 Aimoré (2021-07-18)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Rio Branco-PR 1-4 FC Cascavel (2021-07-18)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Caxias 2-0 Marcílio Dias (2021-07-18)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Jaraguá 0-4 Brasiliense (2021-07-18)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Paragominas 1-2 4 de Julho (2021-07-18)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: ASA 1-1 Bahia de Feira (2021-07-18)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Itabaiana 1-2 Retrô FC (2021-07-18)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Atlético-BA 0-0 Sergipe (2021-07-18)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Nova Mutum 1-1 Gazin Porto Velho EC (2021-07-18)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: CA Patrocinense 0-0 Rio Branco-ES (2021-07-18)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Atlético-AC 3-1 GAS (2021-07-18)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Águia Negra 1-1 Uberlândia (2021-07-19)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Castanhal 2-1 Fast-AM (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Atlético Cearense 0-0 Central (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Goianésia 2-1 Gama (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Bangu 1-1 Inter de Limeira (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: São Bento 0-1 Cianorte (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Boavista-RJ 0-1 Portuguesa (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Santo André 2-0 Madureira (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Joinville 0-0 Esportivo-RS (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Marcílio Dias 0-0 Caxias (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Brasiliense 3-0 Jaraguá (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Juventude-MA 2-0 Guarany (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Palmas 2-1 Moto Club (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Sousa 0-2 América-RN (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: ABC 2-0 Campinense (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Murici 0-3 Juazeirense (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Uberlândia 2-0 Águia Negra (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Caldense 0-0 Rio Branco de Venda Nova (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: FC Cascavel 3-1 Rio Branco-PR (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Imperatriz 3-2 Tocantinópolis (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: 4 de Julho 4-0 Paragominas (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Gazin Porto Velho EC 1-1 Nova Mutum (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: GAS 2-0 Atlético-AC (2021-07-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Ferroviária-SP 2-0 Boa Esporte (2021-07-25)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Aimoré 0-1 Juventus Jaraguá (2021-07-25)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Rio Branco-ES 2-1 CA Patrocinense (2021-07-25)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Penarol-AM 1-1 São Raimundo-RR (2021-07-25)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Treze 3-1 Caucaia (2021-07-25)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Bahia de Feira 1-0 ASA (2021-07-25)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Retrô FC 2-2 Itabaiana (2021-07-25)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Sergipe 1-0 Atlético-BA (2021-07-25)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: União-MT 0-2 Aparecidense (2021-07-25)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Galvez EC 2-0 Ypiranga-AP (2021-07-25)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Guarany 1-1 Imperatriz (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: América-RN 2-2 Treze (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Campinense 3-0 Atlético Cearense (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Gama 1-1 Gazin Porto Velho EC (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Madureira 1-2 São Bento (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Juventus Jaraguá 1-1 FC Cascavel (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Moto Club 1-0 4 de Julho (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Jaraguá 0-2 União-MT (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Caucaia 1-0 Sousa (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Juazeirense 0-0 Sergipe (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Atlético-BA 1-0 Murici (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Esportivo-RS 0-0 Marcílio Dias (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Tocantinópolis 0-1 Juventude-MA (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Aparecidense 1-0 Brasiliense (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: São Raimundo-RR 3-1 Galvez EC (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Inter de Limeira 1-0 Boavista-RJ (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Boa Esporte 1-1 Rio Branco-ES (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Fast-AM 4-0 GAS (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Portuguesa 1-1 Bangu (2021-07-31)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Rio Branco de Venda Nova 1-0 Uberlândia (2021-08-01)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Rio Branco-PR 1-0 Aimoré (2021-08-01)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Caxias 0-0 Joinville (2021-08-01)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Paragominas 1-1 Palmas (2021-08-01)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Central 1-1 ABC (2021-08-01)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Itabaiana 1-2 Bahia de Feira (2021-08-01)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: ASA 0-1 Retrô FC (2021-08-01)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Nova Mutum 2-0 Goianésia (2021-08-01)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Águia Negra 0-6 Caldense (2021-08-01)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: CA Patrocinense 0-2 Ferroviária-SP (2021-08-01)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Cianorte 1-1 Santo André (2021-08-01)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Ypiranga-AP 1-0 Penarol-AM (2021-08-01)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Atlético-AC 0-1 Castanhal (2021-08-01)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Águia Negra 0-1 Ferroviária-SP (2021-08-06)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Atlético Cearense 0-2 América-RN (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Murici 2-2 Itabaiana (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Santo André 2-1 Inter de Limeira (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Marcílio Dias 1-1 Juventus Jaraguá (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Joinville 3-0 Rio Branco-PR (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Gama 0-1 Brasiliense (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Palmas 2-1 Tocantinópolis (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Imperatriz 0-1 Moto Club (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: União-MT 0-1 Nova Mutum (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Goianésia 0-1 Jaraguá (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Caldense 0-0 CA Patrocinense (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Uberlândia 0-0 Boa Esporte (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: São Bento 2-3 Portuguesa (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Esportivo-RS 2-2 FC Cascavel (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: 4 de Julho 0-2 Guarany (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Gazin Porto Velho EC 0-2 Aparecidense (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: GAS 0-2 São Raimundo-RR (2021-08-07)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Central 0-0 Sousa (2021-08-08)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Bangu 3-1 Madureira (2021-08-08)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Aimoré 2-0 Caxias (2021-08-08)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Rio Branco-ES 0-3 Rio Branco de Venda Nova (2021-08-08)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Penarol-AM 5-0 Atlético-AC (2021-08-08)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Paragominas 0-0 Juventude-MA (2021-08-08)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Treze 0-0 Campinense (2021-08-08)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Bahia de Feira 1-2 Atlético-BA (2021-08-08)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Juazeirense 1-0 Retrô FC (2021-08-08)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Sergipe 2-0 ASA (2021-08-08)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Cianorte 2-1 Boavista-RJ (2021-08-08)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Galvez EC 2-2 Fast-AM (2021-08-08)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Ypiranga-AP 0-2 Castanhal (2021-08-08)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: ABC 9-1 Caucaia (2021-08-09)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: América-RN 4-2 Caucaia (2021-08-13)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Campinense 2-1 Central (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Murici 1-1 Sergipe (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Boavista-RJ 2-0 Bangu (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: São Bento 1-0 Santo André (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Portuguesa 0-1 Inter de Limeira (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: FC Cascavel 2-2 Aimoré (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Caxias 0-1 Esportivo-RS (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Joinville 1-1 Marcílio Dias (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Guarany 2-1 Tocantinópolis (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Juventude-MA 1-1 Imperatriz (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Moto Club 1-4 Paragominas (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Jaraguá 1-1 Aparecidense (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Sousa 0-0 Treze (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Atlético-BA 3-3 Juazeirense (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Goianésia 1-1 Gazin Porto Velho EC (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Uberlândia 2-3 Caldense (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Brasiliense 2-3 União-MT (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: 4 de Julho 1-2 Palmas (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: São Raimundo-RR 4-0 Ypiranga-AP (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Boa Esporte 2-0 CA Patrocinense (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Ferroviária-SP 2-0 Rio Branco-ES (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Fast-AM 1-0 Atlético-AC (2021-08-14)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Atlético Cearense 1-0 ABC (2021-08-15)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Rio Branco de Venda Nova 2-2 Águia Negra (2021-08-15)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Madureira 0-0 Cianorte (2021-08-15)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Rio Branco-PR 2-2 Juventus Jaraguá (2021-08-15)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Castanhal 5-0 GAS (2021-08-15)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Retrô FC 1-1 Bahia de Feira (2021-08-15)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Itabaiana 4-1 ASA (2021-08-15)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Nova Mutum 1-1 Gama (2021-08-15)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Galvez EC 1-3 Penarol-AM (2021-08-15)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Caucaia 3-4 Atlético Cearense (2021-08-20)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Campinense 1-0 Sousa (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Gama 0-3 União-MT (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Santo André 2-2 Portuguesa (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Caxias 1-1 FC Cascavel (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Marcílio Dias 2-0 Rio Branco-PR (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Juventus Jaraguá 0-1 Joinville (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Moto Club 3-1 Juventude-MA (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Palmas 0-2 Guarany (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Juazeirense 2-1 Bahia de Feira (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Atlético-BA 1-1 Retrô FC (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Aparecidense 4-1 Goianésia (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Caldense 0-1 Boa Esporte (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Esportivo-RS 2-1 Aimoré (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Tocantinópolis 0-2 4 de Julho (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Gazin Porto Velho EC 1-0 Jaraguá (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: São Raimundo-RR 1-2 Castanhal (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Inter de Limeira 0-2 São Bento (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Paragominas 4-1 Imperatriz (2021-08-21)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Central 2-1 Treze (2021-08-22)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Rio Branco de Venda Nova 0-0 Ferroviária-SP (2021-08-22)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Madureira 1-2 Boavista-RJ (2021-08-22)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Penarol-AM 2-1 Fast-AM (2021-08-22)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: ABC 3-1 América-RN (2021-08-22)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Sergipe 0-1 Itabaiana (2021-08-22)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: ASA 4-2 Murici (2021-08-22)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: CA Patrocinense 0-1 Uberlândia (2021-08-22)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Cianorte 2-0 Bangu (2021-08-22)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Nova Mutum 1-0 Brasiliense (2021-08-22)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Atlético-AC 1-4 Galvez EC (2021-08-22)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Ypiranga-AP 0-0 GAS (2021-08-22)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Águia Negra 2-6 Rio Branco-ES (2021-08-23)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Caucaia 1-1 Central (2021-08-27)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Guarany 4-2 Moto Club (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: América-RN 0-0 Campinense (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Bangu 1-0 São Bento (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Boavista-RJ 0-2 Santo André (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Aimoré 0-0 Joinville (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Juventus Jaraguá 1-0 Esportivo-RS (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: FC Cascavel 2-0 Marcílio Dias (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Rio Branco-ES 0-2 Uberlândia (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Juventude-MA 0-3 Palmas (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Jaraguá 1-2 Nova Mutum (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Imperatriz 0-0 4 de Julho (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Sousa 2-0 ABC (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: União-MT 0-1 Goianésia (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Aparecidense 2-1 Gama (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Tocantinópolis 2-3 Paragominas (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Brasiliense 2-1 Gazin Porto Velho EC (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Ferroviária-SP 3-1 Caldense (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Boa Esporte 3-1 Rio Branco de Venda Nova (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Inter de Limeira 2-1 Cianorte (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Fast-AM 0-0 São Raimundo-RR (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: GAS 0-3 Galvez EC (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Portuguesa 2-0 Madureira (2021-08-28)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Castanhal 1-1 Penarol-AM (2021-08-29)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Rio Branco-PR 1-2 Caxias (2021-08-29)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Treze 1-1 Atlético Cearense (2021-08-29)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Bahia de Feira 6-1 Murici (2021-08-29)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: ASA 1-0 Juazeirense (2021-08-29)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Retrô FC 0-0 Sergipe (2021-08-29)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Itabaiana 3-1 Atlético-BA (2021-08-29)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: CA Patrocinense 1-0 Águia Negra (2021-08-29)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Atlético-AC 3-2 Ypiranga-AP (2021-08-29)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: 4 de Julho 1-0 Juventude-MA (2021-09-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Palmas 0-0 Imperatriz (2021-09-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Paragominas 2-1 Guarany (2021-09-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Santo André 1-2 Bangu (2021-09-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Cianorte 0-0 Portuguesa (2021-09-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: São Bento 0-1 Boavista-RJ (2021-09-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A07: Madureira 1-2 Inter de Limeira (2021-09-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Marcílio Dias 3-2 Aimoré (2021-09-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Esportivo-RS 4-1 Rio Branco-PR (2021-09-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Joinville 3-1 FC Cascavel (2021-09-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A08: Caxias 1-1 Juventus Jaraguá (2021-09-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A02: Moto Club 3-0 Tocantinópolis (2021-09-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Gazin Porto Velho EC 0-2 União-MT (2021-09-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Gama 4-1 Jaraguá (2021-09-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Nova Mutum 1-0 Aparecidense (2021-09-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A05: Goianésia 1-1 Brasiliense (2021-09-04)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: ABC 2-0 Treze (2021-09-05)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Central 2-1 América-RN (2021-09-05)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Atlético Cearense 2-0 Sousa (2021-09-05)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Campinense 5-0 Caucaia (2021-09-05)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Sergipe 4-0 Bahia de Feira (2021-09-05)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Juazeirense 1-1 Itabaiana (2021-09-05)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Murici 2-2 Retrô FC (2021-09-05)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A04: Atlético-BA 1-0 ASA (2021-09-05)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Águia Negra 0-0 Boa Esporte (2021-09-05)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Uberlândia 1-1 Ferroviária-SP (2021-09-05)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Rio Branco de Venda Nova 2-1 CA Patrocinense (2021-09-05)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A06: Caldense 1-2 Rio Branco-ES (2021-09-05)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Ypiranga-AP 1-1 Fast-AM (2021-09-05)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Galvez EC 1-5 Castanhal (2021-09-05)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: São Raimundo-RR 7-1 Atlético-AC (2021-09-05)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A01: Penarol-AM 2-1 GAS (2021-09-05)
- jogo só no ogol, incluído em Segunda fase: Bangu 1-1 Joinville (2021-09-11)
- jogo só no ogol, incluído em Segunda fase: América-RN 1-1 Itabaiana (2021-09-11)
- jogo só no ogol, incluído em Segunda fase: Atlético Cearense 1-1 Juazeirense (2021-09-11)
- jogo só no ogol, incluído em Segunda fase: União-MT 2-0 Boa Esporte (2021-09-11)
- jogo só no ogol, incluído em Segunda fase: Caldense 1-0 Aparecidense (2021-09-11)
- jogo só no ogol, incluído em Segunda fase: Esportivo-RS 0-1 Santo André (2021-09-11)
- jogo só no ogol, incluído em Segunda fase: Caxias 1-0 Portuguesa (2021-09-12)
- jogo só no ogol, incluído em Segunda fase: Brasiliense 0-0 Ferroviária-SP (2021-09-12)
- jogo só no ogol, incluído em Segunda fase: Moto Club 2-0 Castanhal (2021-09-12)
- jogo só no ogol, incluído em Segunda fase: Sergipe 2-2 Campinense (2021-09-12)
- jogo só no ogol, incluído em Segunda fase: Uberlândia 1-1 Nova Mutum (2021-09-12)
- jogo só no ogol, incluído em Segunda fase: Retrô FC 1-1 ABC (2021-09-12)
- jogo só no ogol, incluído em Segunda fase: Cianorte 0-0 FC Cascavel (2021-09-12)
- jogo só no ogol, incluído em Segunda fase: Paragominas 1-0 São Raimundo-RR (2021-09-12)
- jogo só no ogol, incluído em Segunda fase: Penarol-AM 1-0 4 de Julho (2021-09-12)
- jogo só no ogol, incluído em Segunda fase: Galvez EC 0-0 Guarany (2021-09-13)
- jogo só no ogol, incluído em Segunda fase: Aparecidense 3-1 Caldense (2021-09-17)
- jogo só no ogol, incluído em Segunda fase: Joinville 1-1 Bangu (2021-09-18)
- jogo só no ogol, incluído em Segunda fase: Santo André 0-1 Esportivo-RS (2021-09-18)
- jogo só no ogol, incluído em Segunda fase: Campinense 1-1 Sergipe (2021-09-18)
- jogo só no ogol, incluído em Segunda fase: Juazeirense 0-0 Atlético Cearense (2021-09-18)
- jogo só no ogol, incluído em Segunda fase: Portuguesa 1-0 Caxias (2021-09-18)
- jogo só no ogol, incluído em Segunda fase: FC Cascavel 0-3 Cianorte (2021-09-18)
- jogo só no ogol, incluído em Segunda fase: 4 de Julho 3-0 Penarol-AM (2021-09-18)
- jogo só no ogol, incluído em Segunda fase: Boa Esporte 1-1 União-MT (2021-09-18)
- jogo só no ogol, incluído em Segunda fase: Ferroviária-SP 1-0 Brasiliense (2021-09-18)
- jogo só no ogol, incluído em Segunda fase: Castanhal 1-2 Moto Club (2021-09-19)
- jogo só no ogol, incluído em Segunda fase: Itabaiana 0-2 América-RN (2021-09-19)
- jogo só no ogol, incluído em Segunda fase: Nova Mutum 0-2 Uberlândia (2021-09-19)
- jogo só no ogol, incluído em Segunda fase: ABC 3-2 Retrô FC (2021-09-19)
- jogo só no ogol, incluído em Segunda fase: São Raimundo-RR 1-2 Paragominas (2021-09-19)
- jogo só no ogol, incluído em Segunda fase: Guarany 2-0 Galvez EC (2021-09-20)
- jogo só no ogol, incluído em Oitavas de final: Atlético Cearense 2-0 Paragominas (2021-09-25)
- jogo só no ogol, incluído em Oitavas de final: Campinense 2-1 Guarany (2021-09-25)
- jogo só no ogol, incluído em Oitavas de final: Caxias 2-0 União-MT (2021-09-25)
- jogo só no ogol, incluído em Oitavas de final: Esportivo-RS 1-2 Ferroviária-SP (2021-09-25)
- jogo só no ogol, incluído em Oitavas de final: 4 de Julho 1-1 ABC (2021-09-26)
- jogo só no ogol, incluído em Oitavas de final: América-RN 1-0 Moto Club (2021-09-26)
- jogo só no ogol, incluído em Oitavas de final: Cianorte 0-0 Aparecidense (2021-09-26)
- jogo só no ogol, incluído em Oitavas de final: Uberlândia 1-0 Joinville (2021-09-26)
- jogo só no ogol, incluído em Oitavas de final: Joinville 2-1 Uberlândia (2021-10-02)
- jogo só no ogol, incluído em Oitavas de final: Aparecidense 1-0 Cianorte (2021-10-02)
- jogo só no ogol, incluído em Oitavas de final: União-MT 0-2 Caxias (2021-10-02)
- jogo só no ogol, incluído em Oitavas de final: Moto Club 2-4 América-RN (2021-10-03)
- jogo só no ogol, incluído em Oitavas de final: Guarany 0-2 Campinense (2021-10-03)
- jogo só no ogol, incluído em Oitavas de final: ABC 2-0 4 de Julho (2021-10-03)
- jogo só no ogol, incluído em Oitavas de final: Paragominas 2-1 Atlético Cearense (2021-10-03)
- jogo só no ogol, incluído em Oitavas de final: Ferroviária-SP 1-1 Esportivo-RS (2021-10-03)
- jogo só no ogol, incluído em Quartas de final: Uberlândia 0-1 Aparecidense (2021-10-09)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: América-RN 0-0 Campinense (2021-10-09)
- jogo só no ogol, incluído em Quartas de final: Atlético Cearense 1-1 Ferroviária-SP (2021-10-10)
- jogo só no ogol, incluído em Quartas de final: Caxias 0-0 ABC (2021-10-10)
- jogo só no ogol, incluído em Quartas de final: Aparecidense 1-1 Uberlândia (2021-10-16)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Campinense 0-0 América-RN (2021-10-16)
- jogo só no ogol, incluído em Quartas de final: Ferroviária-SP 0-0 Atlético Cearense (2021-10-17)
- jogo só no ogol, incluído em Quartas de final: ABC 3-0 Caxias (2021-10-17)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Atlético Cearense 1-1 Campinense (2021-10-23)
- jogo só no ogol, incluído em Semifinal: Aparecidense 4-2 ABC (2021-10-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo A03: Campinense 3-1 Atlético Cearense (2021-10-30)
- jogo só no ogol, incluído em Semifinal: ABC 1-0 Aparecidense (2021-10-31)
- jogo só no ogol, incluído em Final: Campinense 0-1 Aparecidense (2021-11-06)
- jogo só no ogol, incluído em Final: Aparecidense 1-1 Campinense (2021-11-13)
- jogo corrigido à mão — Joinville x Bangu: pênaltis 4-3 (Bola n@ Área e transfermarkt; revisão QC-001)
- jogo corrigido à mão — Santo André x Esportivo-RS: pênaltis 4-5 (Bola n@ Área e transfermarkt; revisão QC-001)
- jogo corrigido à mão — Campinense x Sergipe: pênaltis 4-2 (Bola n@ Área e transfermarkt; revisão QC-001)
- jogo corrigido à mão — Juazeirense x Atlético Cearense: pênaltis 3-5 (Bola n@ Área e transfermarkt; revisão QC-001)
- jogo corrigido à mão — Portuguesa x Caxias: pênaltis 1-4 (Bola n@ Área e transfermarkt; revisão QC-001)
- jogo corrigido à mão — Joinville x Uberlândia: pênaltis 1-3 (Bola n@ Área e transfermarkt; revisão QC-001)
- jogo corrigido à mão — Campinense x América-RN: pênaltis 4-2 (Bola n@ Área e transfermarkt; revisão QC-001)
- jogo corrigido à mão — Ferroviária-SP x Atlético Cearense: pênaltis 3-4 (Bola n@ Área e transfermarkt; revisão QC-001)
- fases e grupos pelo ogol em 12 jogos: PRELIMINARY STAGE/- → Fase preliminar/- (8); Primeira fase/Grupo A03 → Quartas de final/- (2); Primeira fase/Grupo A03 → Semifinal/- (2)
- 1 datas corrigidas (datas_corrigidas.csv; ex.: Atlético-AC x Fast-AM 2021-06-28 -> 2021-06-27, Bola n@ Área e transfermarkt (QC-003))

### 2022

- fases e grupos pelo ogol em 510 jogos: Primeira fase/Grupo A → Primeira fase/Grupo A7 (56); Primeira fase/Grupo A → Primeira fase/Grupo A8 (56); Primeira fase/Grupo A → Primeira fase/Grupo A6 (56); Primeira fase/Grupo A → Primeira fase/Grupo A5 (56); Primeira fase/Grupo A → Primeira fase/Grupo A4 (56); Primeira fase/Grupo A → Primeira fase/Grupo A3 (56); Primeira fase/Grupo A → Primeira fase/Grupo A2 (56); Primeira fase/Grupo A → Primeira fase/Grupo A1 (56) ...

### 2023

- a página da RSSSF não publica tabelas e parou antes do fim (478 dos 510 jogos): conferência só pelo ogol, que tem o mesmo placar em todos os jogos em comum
- jogo só no ogol, incluído em Segunda fase: Vitória-ES 1-0 Ceilândia (2023-07-29)
- jogo só no ogol, incluído em Segunda fase: Falcon FC 1-1 Sousa (2023-07-29)
- jogo só no ogol, incluído em Segunda fase: Maranhão 2-3 Tuna Luso (2023-07-29)
- jogo só no ogol, incluído em Segunda fase: Inter de Limeira 0-1 Caxias (2023-07-29)
- jogo só no ogol, incluído em Segunda fase: ASA 1-0 Nacional-PB (2023-07-29)
- jogo só no ogol, incluído em Segunda fase: Camboriú 0-0 Maringá (2023-07-29)
- jogo só no ogol, incluído em Segunda fase: Ferroviária-SP 1-1 Hercílio Luz (2023-07-29)
- jogo só no ogol, incluído em Segunda fase: Parnaíba 2-0 Nacional-AM (2023-07-30)
- jogo só no ogol, incluído em Segunda fase: CEOV Operário 1-0 Portuguesa-RJ (2023-07-30)
- jogo só no ogol, incluído em Segunda fase: Brasil de Pelotas 0-0 CA Patrocinense (2023-07-30)
- jogo só no ogol, incluído em Segunda fase: Brasiliense 0-2 Athletic Club (2023-07-30)
- jogo só no ogol, incluído em Segunda fase: Potiguar 1-0 Bahia de Feira (2023-07-30)
- jogo só no ogol, incluído em Segunda fase: Pacajus 1-2 Retrô FC (2023-07-30)
- jogo só no ogol, incluído em Segunda fase: Águia 1-1 Atlético Cearense (2023-08-01)
- jogo só no ogol, incluído em Segunda fase: Democrata-GV 0-0 Anápolis (2023-08-01)
- jogo só no ogol, incluído em Segunda fase: Princesa 1-1 Ferroviário-CE (2023-08-01)
- jogo só no ogol, incluído em Segunda fase: Athletic Club 0-0 Brasiliense (2023-08-05)
- jogo só no ogol, incluído em Segunda fase: Hercílio Luz 2-2 Ferroviária-SP (2023-08-05)
- jogo só no ogol, incluído em Segunda fase: Ceilândia 3-0 Vitória-ES (2023-08-05)
- jogo só no ogol, incluído em Segunda fase: Portuguesa-RJ 4-0 CEOV Operário (2023-08-05)
- jogo só no ogol, incluído em Segunda fase: Bahia de Feira 1-0 Potiguar (2023-08-05)
- jogo só no ogol, incluído em Segunda fase: Ferroviário-CE 3-0 Princesa (2023-08-05)
- jogo só no ogol, incluído em Segunda fase: CA Patrocinense 2-1 Brasil de Pelotas (2023-08-06)
- jogo só no ogol, incluído em Segunda fase: Atlético Cearense 3-0 Águia (2023-08-06)
- jogo só no ogol, incluído em Segunda fase: Caxias 1-1 Inter de Limeira (2023-08-06)
- jogo só no ogol, incluído em Segunda fase: Nacional-AM 3-0 Parnaíba (2023-08-06)
- jogo só no ogol, incluído em Segunda fase: Sousa 2-1 Falcon FC (2023-08-06)
- jogo só no ogol, incluído em Segunda fase: Nacional-PB 3-1 ASA (2023-08-06)
- jogo só no ogol, incluído em Segunda fase: Tuna Luso 0-1 Maranhão (2023-08-06)
- jogo só no ogol, incluído em Segunda fase: Anápolis 3-1 Democrata-GV (2023-08-06)
- jogo só no ogol, incluído em Segunda fase: Retrô FC 2-1 Pacajus (2023-08-06)
- jogo só no ogol, incluído em Segunda fase: Maringá 1-1 Camboriú (2023-08-06)
- fases e grupos pelo ogol em 30 jogos: Quartas de final/Grupo D03 → Quartas de final/- (4); Oitavas de final/Grupo C1 → Oitavas de final/- (2); Oitavas de final/Grupo C2 → Oitavas de final/- (2); Oitavas de final/Grupo C3 → Oitavas de final/- (2); Oitavas de final/Grupo C4 → Oitavas de final/- (2); Oitavas de final/Grupo C5 → Oitavas de final/- (2); Oitavas de final/Grupo C6 → Oitavas de final/- (2); Oitavas de final/Grupo C7 → Oitavas de final/- (2) ...

### 2024

- tabela publicada x jogos — Primeira fase / Grupo A1: Manaus FC tabela [14, 8, 2, 4, 19, 15] jogos [14, 7, 3, 4, 21, 18] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo A1: Princesa tabela [14, 7, 3, 4, 20, 14] jogos [14, 7, 4, 3, 23, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — Princesa x Manaus FC (2024-05-11): RSSSF 0-1, ogol 3-3; fica o da RSSSF
- jogo corrigido à mão — Princesa x Manaus FC: ogol e Wikipédia: 3-3 (revisão SD-010)
- fases e grupos pelo ogol em 62 jogos: Segunda fase/Grupo B08 → Segunda fase/- (2); Segunda fase/Grupo B13 → Segunda fase/- (2); Segunda fase/Grupo B09 → Segunda fase/- (2); Segunda fase/Grupo B01 → Segunda fase/- (2); Segunda fase/Grupo B02 → Segunda fase/- (2); Segunda fase/Grupo B10 → Segunda fase/- (2); Segunda fase/Grupo B03 → Segunda fase/- (2); Segunda fase/Grupo B14 → Segunda fase/- (2) ...

### 2025

- fases e grupos pelo ogol em 60 jogos: Segunda fase/Grupo B12 → Segunda fase/- (2); Segunda fase/Grupo B15 → Segunda fase/- (2); Segunda fase/Grupo B01 → Segunda fase/- (2); Segunda fase/Grupo B09 → Segunda fase/- (2); Segunda fase/Grupo B07 → Segunda fase/- (2); Segunda fase/Grupo B11 → Segunda fase/- (2); Segunda fase/Grupo B10 → Segunda fase/- (2); Segunda fase/Grupo B14 → Segunda fase/- (2) ...

### 2026

- a RSSSF ainda não tem a página de 2026: os jogos, as fases e os grupos vêm do ogol (revisão SD-001). Os perdedores das quartas jogaram uma repescagem pelas duas últimas vagas de acesso (Nacional-AM e Goiatuba subiram). Sem autores de gols
- a RSSSF ainda não tem a página de 2026: a base dos jogos é o ogol (revisão SD-001)
- fases e grupos pelo ogol em 4 jogos: Primeira fase/- → Repescagem/- (4)
- 23 datas corrigidas (datas_corrigidas.csv; ex.: Galvez EC x Araguaína 2026-04-05 -> 2026-04-04, transfermarkt e Futebol Nacional, jogo noturno (QC-003))

## Identidade dos clubes

- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol (`data/coleta/bra-serie-d/ogol/clubes.json`).
- Clube do `futebol.db` usa o nome de lá; clube da Série C usa o nome do pacote da Série C; os outros seguem o nome curto do
  ogol, com "-UF" só quando outro clube tem o mesmo nome. Os nomes de cada fonte e ano estão em `clubes.csv` (`nomes_fonte`).
- O Espírito Santo FC (Alegre-ES, 2016-2018) aparece com o nome com que jogou, e não com o posterior "Rive A.C." (D-03).
  Botafogo-DF no Guará (DF), onde jogava em 2007-2010, e AA Araguaia em Água Boa (MT) (revisão CL-028).

## O que não deu para coletar

- **Cartões:** nenhuma das fontes lidas traz cartões da Série D. O ogol tem na página de cada jogo (fica para depois, se aprovado).
- **Autores dos gols:** só onde a RSSSF traz e a soma fecha com o placar.
- **Hora, estádio e público:** a ESPN não tem a Série D; hora pelo ogol e estádio só nas páginas da RSSSF que trazem.
- **Classificação final:** calculada (fase alcançada, pontos, vitórias, saldo, gols pró) quando a RSSSF não publica a geral.
