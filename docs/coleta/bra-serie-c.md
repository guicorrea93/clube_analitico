# Série C — coleta de dados

Gerado por `python coleta/bra-serie-c/importar.py`. Pacote em `data/coleta/bra-serie-c/pacote/`.

**Edições:** 36 oficiais, de 1981 a 2026 (1981, 1988, 1990, 1992, 1994-1999 e 2001-2026), conferidas na RSSSF Brasil
(lista de campeões da 3ª divisão) e na Wikipédia em português (artigo da Série C). As duas trazem os mesmos anos e os mesmos
campeões. Ficam de fora 1987 (módulos Azul e Branco da Copa União: a CBF disse que nenhum módulo seria a 3ª divisão) e 2000
(Módulo Verde e Branco da Copa João Havelange, equivalente à 3ª divisão, mas sem título oficial). Nome oficial: Taça de Bronze
em 1981; Campeonato Brasileiro Série C nas outras.

**Fontes:** RSSSF Brasil (`br{ano}l3.htm`, base de jogos, fases, grupos, datas e autores; as tabelas publicadas são a conferência);
ogol (calendário de todas as edições e o código de cada clube, que dá a identidade entre anos e mudanças de nome; completa os
jogos que faltam na RSSSF e é a base de 2019); ESPN (liga `bra.3`, 2017 em diante: hora e estádio; a ESPN não traz gols,
cartões nem público da Série C); Wikipédia (punições de pontos e lista de campeões).

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,
fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` usa o nome de lá.

**Classificação final (revisão SC-002, SC-003):** campeão e vice em cima; depois a fase alcançada; na mesma fase, a posição
no grupo dela (ou no quadrangular/octogonal final) e a campanha toda (pontos, vitórias, saldo, gols pró). A ordem geral da RSSSF,
quando existe, só desempata dentro da mesma fase. As últimas fases de mata-mata levam o nome pelo número de confrontos
(1 = Final, 2 = Semifinal, 4 = Quartas de final).

**Acesso e rebaixamento (revisão SC-004, SC-005):** acesso = promovidos da Wikipédia e quem jogou a Série B do ano seguinte
(em 1981 só o Olaria; em 1988, 1990 e 1992 ninguém, porque a Série B seguinte foi por convite; em 1999 Fluminense e São
Raimundo). Rebaixado = rebaixados da RSSSF e da Wikipédia e, desde 2009, quem jogou a Série D do ano seguinte (mais
Guaratinguetá em 2016 e Luverdense em 2019, que não jogaram a D).

| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|---|
| 1981 | RSSSF + ogol | 24 | 52 (52) | 108 | 29 | 2 / 0 | Olaria | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1988 | RSSSF + ogol | 43 | 202 (202) | 414 | 36 | 19 / 1 | União São João | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1990 | RSSSF + ogol | 30 | 74 (74) | 143 | 38 | 7 / 0 | Atlético-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1992 | RSSSF + ogol | 31 | 122 (122) | 254 | 25 | 10 / 6 | Tuna Luso | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1994 | RSSSF + ogol | 41 | 178 (178) | 397 | 0 | 11 / 1 | GE Novorizontino | RSSSF (classificação geral publicada) |
| 1995 | RSSSF + ogol | 107 | 384 (384) | 863 | 0 | 32 / 2 | XV de Piracicaba | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1996 | RSSSF + ogol | 59 | 227 (227) | 598 | 0 | 15 / 1 | Vila Nova-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1997 | RSSSF + ogol | 64 | 260 (259) | 634 | 0 | 17 / 2 | Sampaio Corrêa | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1998 | RSSSF + ogol | 65 | 388 (387) | 1035 | 0 | 15 / 0 | Avaí | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1999 | RSSSF + ogol | 36 | 226 (224) | 618 | 174 | 5 / 2 | Fluminense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2001 | RSSSF + ogol | 65 | 412 (412) | 1124 | 0 | 15 / 0 | Paulista | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2002 | RSSSF + ogol | 61 | 244 (244) | 595 | 28 | 16 / 1 | Brasiliense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2003 | RSSSF + ogol | 93 | 340 (340) | 825 | 169 | 27 / 2 | Ituano | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2004 | RSSSF + ogol | 60 | 238 (238) | 603 | 57 | 17 / 0 | União Barbarense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2005 | RSSSF + ogol | 63 | 254 (254) | 696 | 81 | 16 / 1 | Remo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2006 | RSSSF + ogol | 63 | 386 (386) | 1059 | 37 | 27 / 2 | Criciúma | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2007 | RSSSF + ogol | 64 | 392 (392) | 1025 | 29 | 26 / 3 | Bragantino | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2008 | RSSSF + ogol | 63 | 386 (386) | 1068 | 0 | 29 / 1 | Atlético-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2009 | RSSSF + ogol | 20 | 94 (94) | 264 | 207 | 5 / 0 | América-MG | RSSSF (classificação geral publicada) |
| 2010 | RSSSF + ogol | 20 | 94 (94) | 208 | 208 | 7 / 2 | ABC | RSSSF (classificação geral publicada) |
| 2011 | RSSSF + ogol | 20 | 106 (106) | 289 | 0 | 8 / 2 | Joinville | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2012 | RSSSF + ogol | 20 | 194 (194) | 493 | 2 | 5 / 0 | Oeste | RSSSF (classificação geral publicada) |
| 2013 | RSSSF + ogol | 21 | 214 (214) | 514 | 459 | 4 / 0 | Santa Cruz | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2014 | RSSSF + ogol | 20 | 194 (194) | 424 | 421 | 5 / 0 | Macaé | RSSSF (classificação geral publicada) |
| 2015 | RSSSF + ogol | 20 | 194 (194) | 461 | 461 | 5 / 0 | Vila Nova-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2016 | RSSSF + ogol | 20 | 194 (194) | 435 | 431 | 8 / 0 | Boa Esporte | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2017 | RSSSF + ogol + ESPN | 20 | 194 (194) | 418 | 408 | 8 / 0 | CSA | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2018 | RSSSF + ogol + ESPN | 20 | 194 (194) | 456 | 445 | 9 / 0 | Operário-PR | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2019 | ogol + ESPN | 20 | 194 (194) | 439 | 0 | 0 / 0 | Náutico | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2020 | RSSSF + ogol + ESPN | 20 | 206 (206) | 498 | 497 | 2 / 0 | Vila Nova-GO | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2021 | RSSSF + ogol + ESPN | 20 | 206 (206) | 423 | 423 | 5 / 0 | Ituano | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2022 | RSSSF + ogol + ESPN | 20 | 216 (216) | 501 | 497 | 4 / 0 | Mirassol | RSSSF (classificação geral publicada) |
| 2023 | RSSSF + ogol + ESPN | 20 | 216 (216) | 465 | 464 | 1 / 0 | Amazonas | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2024 | RSSSF + ogol + ESPN | 20 | 216 (216) | 522 | 0 | 3 / 0 | Volta Redonda | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2025 | RSSSF + ogol + ESPN | 20 | 216 (216) | 432 | 425 | 4 / 0 | Ponte Preta | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2026 | ogol | 20 | 216 (216) | 488 | 0 | 0 / 0 | Maringá | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |

## Conferência e correções, ano a ano

### 1981

- o ogol liga o Matsubara (Cambará-PR) ao J. Malucelli, fundado em 1994; corrigido no código (CORRIGE_OGOL): fica a SE Matsubara, como na RSSSF

### 1988

- a final (Esportivo-MG x União São João, 1-1 e 2-2) foi decidida pela campanha (número de vitórias): campeão pela lista oficial
- vitória valia 3 pontos e o empate ia para os pênaltis: 2 para quem vencia, 1 para quem perdia (revisão SC-007). No grupo 18 da 2ª fase o ogol põe a Desportiva Ferroviária no lugar da Ferroviária-SP; corrigido (revisão SC-008)
- tabela publicada x jogos — Primeira fase / Grupo 11: Figueirense tabela [6, 3, 2, 1, 8, 4] jogos [6, 3, 1, 2, 8, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo 11: Inter de Santa Maria tabela [6, 0, 3, 3, 4, 4] jogos [6, 1, 2, 3, 4, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar da página corrigido — Internacional 0-0 Figueirense (1988-11-03) vira Internacional 2-0 Figueirense: ogol e Wikipédia: 2-0 (revisão SC-014)
- placar diferente no ogol — Fabril x Esportivo-MG (1988-10-30): RSSSF 1-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Iguaçu x Guarany-RS (1988-11-06): RSSSF 2-2, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — ABC x Botafogo-PB (1988-11-27): RSSSF 1-1, ogol 0-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Paulistano-PE x Botafogo-PB, ogol 1988-11-06); fica a do ogol
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, União São João

### 1990

- data diferente entre RSSSF e ogol (mais de 3 dias) em 39 jogos (ex.: Lagarto EC x América-MG, ogol 1990-09-30); fica a do ogol
- a fase "Mata-mata" é mata-mata com 4 confronto(s): vira "Quartas de final"

### 1992

- 5 placares da página trocados pelos do ogol e da Wikipédia (revisão SC-014); as tabelas publicadas pela RSSSF seguem os placares antigos da página e por isso não fecham nos grupos 1 e 6 e no grupo A da 2ª fase. Com os placares novos o 3º é o Nacional-AM, como na Wikipédia. Dois jogos do grupo B vêm na página depois do título da final e voltam para a 2ª fase
- tabela publicada x jogos — Primeira fase / Grupo 1: Nacional-AM tabela [8, 3, 4, 1, 6, 3] jogos [8, 5, 2, 1, 8, 2] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo 1: Macapá tabela [8, 1, 7, 0, 7, 5] jogos [8, 1, 6, 1, 7, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo 1: Ji-Paraná tabela [8, 2, 2, 4, 6, 13] jogos [8, 2, 1, 5, 5, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo 1: Nacional-AM tabela [8, 3, 4, 1, 6, 3] jogos [8, 5, 2, 1, 8, 2] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo 1: Macapá tabela [8, 1, 7, 0, 7, 5] jogos [8, 1, 6, 1, 7, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo 1: Ji-Paraná tabela [8, 2, 2, 4, 6, 13] jogos [8, 2, 1, 5, 5, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo 6: São Bento tabela [6, 3, 2, 1, 8, 8] jogos [6, 3, 1, 2, 7, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo 6: Rio Branco-MG tabela [6, 1, 1, 4, 5, 7] jogos [6, 2, 0, 4, 5, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo 6: São Bento tabela [6, 3, 2, 1, 8, 8] jogos [6, 3, 1, 2, 7, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo 6: Rio Branco-MG tabela [6, 1, 1, 4, 5, 7] jogos [6, 2, 0, 4, 5, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / Grupo A: Auto Esporte tabela [4, 2, 0, 2, 4, 3] jogos [4, 1, 0, 3, 1, 5] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / Grupo A: Nacional-AM tabela [4, 0, 2, 2, 3, 6] jogos [4, 1, 2, 1, 5, 3] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Auto Esporte tabela [12, 6, 3, 3, 16, 9] jogos [12, 5, 3, 4, 13, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Nacional-AM tabela [12, 3, 6, 3, 9, 9] jogos [12, 6, 4, 2, 13, 5] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Macapá tabela [8, 1, 7, 0, 7, 5] jogos [8, 1, 6, 1, 7, 7] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: São Bento tabela [6, 3, 2, 1, 8, 8] jogos [6, 3, 1, 2, 7, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Ji-Paraná tabela [8, 2, 2, 4, 6, 13] jogos [8, 2, 1, 5, 5, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Rio Branco-MG tabela [6, 1, 1, 4, 5, 7] jogos [6, 2, 0, 4, 5, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar da página corrigido — Nacional-AM 1-1 Ji-Paraná (1992-04-01) vira Nacional-AM 1-0 Ji-Paraná: ogol e Wikipédia: 1-0 (revisão SC-014)
- placar da página corrigido — Nacional-AM 0-0 Macapá (1992-04-16) vira Macapá 0-2 Nacional-AM: ogol e Wikipédia: Macapá 0-2 Nacional-AM (revisão SC-014)
- placar da página corrigido — Rio Branco-MG 2-2 São Bento (1992-03-29) vira Rio Branco-MG 2-1 São Bento: ogol e Wikipédia: 2-1 (revisão SC-014)
- placar da página corrigido — Nacional-AM 1-3 Auto Esporte (1992-05-24) vira Nacional-AM 3-0 Auto Esporte: ogol e Wikipédia (Placar): 3-0 (revisão SC-014)
- mando invertido no ogol — RSSSF Nacional-AM 2-1 Atlético-AC, ogol Atlético-AC 1-2 Nacional-AM (1992-04-09); fica a RSSSF
- mando invertido no ogol — RSSSF Rio Negro-AM 0-1 Ji-Paraná, ogol Ji-Paraná 1-0 Rio Negro-AM (1992-04-09); fica a RSSSF
- mando invertido no ogol — RSSSF Rio Negro-AM 1-0 Atlético-AC, ogol Atlético-AC 0-1 Rio Negro-AM (1992-04-20); fica a RSSSF
- mando invertido no ogol — RSSSF Nacional-AM 1-0 Ji-Paraná, ogol Ji-Paraná 0-1 Nacional-AM (1992-04-23); fica a RSSSF
- mando invertido no ogol — RSSSF Rio Negro-AM 0-0 Macapá, ogol Macapá 0-0 Rio Negro-AM (1992-04-23); fica a RSSSF
- 2 jogos do Grupo B da Segunda fase vêm na página depois do título da Final; voltam para a Segunda fase
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Tuna Luso

### 1994

- nas oitavas, o 'Vitória' sem estado da página é o Vitória-ES (o Vitória-PE caiu para o ABC na mesma fase); corrigido no texto da página
- o ogol põe o Vitória-ES contra o ABC no jogo de volta das oitavas; a RSSSF e a classificação final mostram o Vitória-PE (fica a RSSSF)
- tabela publicada x jogos — Primeira fase / Grupo 7: Taguatinga tabela [6, 3, 1, 2, 6, 5] jogos [6, 3, 1, 2, 7, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — Vitória-PE x América-PB (1994-10-30): RSSSF 0-2, ogol 3-0; fica o da RSSSF
- placar diferente no ogol — América-PB x Vitória-PE (1994-10-23): RSSSF 0-3, ogol 2-0; fica o da RSSSF
- placar corrigido pelo ogol — Valeriodoce x América-RJ (1994-10-30): RSSSF 1-1, ogol 1-0; fica o do ogol, que fecha com a tabela publicada
- placar corrigido pelo ogol — Caldas x Vila Nova-GO (1994-10-23): RSSSF 0-3, ogol 1-3; fica o do ogol, que fecha com a tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 28 jogos (ex.: Vitória-ES x Villa Nova-MG, ogol 1994-10-30); fica a do ogol
- adversário diferente no ogol — RSSSF ABC 3-0 Vitória-PE, ogol ABC 3-0 Vitória-ES (1994-11-10); fica a RSSSF
- ida e volta de Sousa x CSA vinham com a mesma data (1994-10-27); ficam 1994-10-28, 1994-10-30 (do ogol)
- ida e volta de Valeriodoce x Juventus-SP vinham com a mesma data (1994-11-06); ficam 1994-11-06, 1994-11-09 (do ogol)
- ida e volta de Vitória-PE x ABC vinham com a mesma data (1994-11-06); ficam 1994-11-06, 1994-11-10 (do ogol)

### 1995

- página com 108 clubes e a 2ª e a 3ª fases em confrontos colados uns nos outros; o leitor separa cada jogo (rsssf_c.py, _1995)
- erros de digitação da página corrigidos no código: 'Coríntians 3x1 3x1 Santa Cruz-PB' (placar repetido) e 'Ypranga'
- tabela publicada x jogos — Primeira fase / Grupo 21: Baré tabela [4, 1, 2, 1, 4, 4] jogos [4, 1, 2, 1, 3, 3] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Progresso-RR tabela [4, 1, 1, 2, 5, 8] jogos [4, 1, 1, 2, 4, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Itumbiara tabela [6, 0, 3, 3, 3, 6] jogos [6, 1, 3, 2, 3, 4] — placar diverge entre RSSSF e ogol em Itumbiara x Gama (1-0 x 1-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- placar da página corrigido — Itumbiara 1-2 Gama (1995-09-02) vira Itumbiara 1-0 Gama (resultado dado no tribunal): em campo 1-2; o jogo foi dado ao Itumbiara (1-0): a tabela do grupo 8 na RSSSF e na Wikipédia fecha assim (revisão SC-015)
- jogo do ogol ignorado — grupo 12: Botafogo-PB x Coríntians foi cancelado (nota da RSSSF: '*x*'); o ogol traz 0-0, e a tabela do grupo não conta o jogo
- jogo do ogol ignorado — grupo 12: Santa Cruz-PB x ABC foi cancelado (nota da RSSSF: '*x*'); o ogol traz 0-0, e a tabela do grupo não conta o jogo
- placar diferente no ogol — CSA x Sporting FC (1995-09-11): RSSSF 0-0, ogol 5-4; fica o da RSSSF
- placar diferente no ogol — Uberlândia x Botafogo-SP (1995-09-03): RSSSF 1-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Itumbiara x Planaltina (1995-09-04): RSSSF 0-0, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Sporting FC x CSA (1995-08-27): RSSSF 4-5, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Atlético Sorocaba x Joinville (1995-09-10): RSSSF 1-0, ogol 0-1; fica o da RSSSF
- placar corrigido pelo ogol — Rio Branco-AC x Atlético-AC (1995-09-12): RSSSF 2-0, ogol 1-0; fica o do ogol, que fecha com a tabela publicada
- placar diferente no ogol — Flamengo-PI x Fortaleza (1995-10-15): RSSSF 0-1, ogol 0-0; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 3 jogos (ex.: Caldas x Itumbiara, ogol 1995-08-28); fica a do ogol
- 1 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)
- a fase "Quarta fase" é mata-mata com 8 confronto(s): vira "Oitavas de final"

### 1996

- a página traz 'GAS 2-3 GAS' no grupo 2; é GAS 2-3 Baré (ogol e tabela do grupo); corrigido no texto da página
- tabela publicada x jogos — Primeira fase / Grupo 3: Sampaio Corrêa tabela [4, 2, 0, 2, 8, 6] jogos [5, 3, 0, 2, 10, 7] — a tabela conta 4 jogos e as fontes trazem 5
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Potiguar x Pauferrense, ogol 1996-09-01); fica a do ogol
- mando invertido no ogol — RSSSF Sobradinho 3-0 Planaltina, ogol Planaltina 0-3 Sobradinho (1996-09-15); fica a RSSSF
- mando invertido no ogol — RSSSF Botafogo-SP 2-0 Comercial-RP, ogol Comercial-RP 0-2 Botafogo-SP (1996-09-15); fica a RSSSF
- a fase "Terceira fase" é mata-mata com 8 confronto(s): vira "Oitavas de final"

### 1997

- tabela publicada x jogos — Primeira fase / Grupo 1: Ji-Paraná tabela [6, 3, 1, 2, 8, 5] jogos [6, 3, 1, 2, 10, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo 7: Goiânia tabela [6, 3, 2, 1, 8, 5] jogos [6, 3, 2, 1, 8, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo 7: Operário-MS tabela [6, 3, 0, 3, 4, 6] jogos [6, 3, 0, 3, 5, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo do ogol ignorado — 2ª fase: o ogol tem Operário-MS 0-0 Itumbiara na volta; o confronto foi com o Ji-Paraná (ida 1-0 no ogol e na RSSSF); o Itumbiara já tinha caído na 1ª fase
- placar diferente no ogol — Palmas x Tocantinópolis (1997-09-21): RSSSF 0-1, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Tocantinópolis x Palmas (1997-08-31): RSSSF 0-2, ogol 1-0; fica o da RSSSF
- só na RSSSF (não achado no ogol): Operário-MS 0-0 Ji-Paraná (None)
- 3 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)

### 1998

- 3 jogos do Itumbiara ficam de fora: eliminado por não pagar a taxa de arbitragem; todos os seus jogos foram anulados (nota da RSSSF; o ogol e a tabela do grupo 5 não os trazem)
- jogo do ogol ignorado — grupo 10: o ogol tem União Bandeirante 5-0 Figueirense em 27/09; a RSSSF traz União Bandeirante 3-0 São José-RS, e as tabelas de Figueirense e São José só fecham com a RSSSF
- placar diferente no ogol — Icasa x EC Limoeiro (1998-08-26): RSSSF 2-1, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Rio Branco-SP x Villa Nova-MG (1998-10-07): RSSSF 3-0, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Santo André x Tupi (1998-10-11): RSSSF 1-0, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — América-SP x Anápolis (1998-10-07): RSSSF 0-0, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — América-RJ x Anapolina (1998-10-24): RSSSF 1-2, ogol 2-1; fica o da RSSSF
- placar diferente no ogol — Santo André x Avaí (1998-10-24): RSSSF 1-1, ogol 3-3; fica o da RSSSF
- placar diferente no ogol — Noroeste x Brasil de Pelotas (1998-10-24): RSSSF 3-3, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Rioverdense x Ubiratan (1998-08-12): RSSSF 2-0, ogol 3-2; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 4 jogos (ex.: Rio Branco-SP x Matonense, ogol 1998-08-19); fica a do ogol
- mando invertido no ogol — RSSSF Nacional-AM 2-2 São Raimundo, ogol São Raimundo 2-2 Nacional-AM (1998-08-16); fica a RSSSF
- só na RSSSF (não achado no ogol): União Bandeirante 3-0 São José-RS (1998-09-27)
- ida e volta de Anápolis x América-SP vinham com a mesma data (1998-10-07); ficam 1998-10-07, 1998-10-11 (da página)
- 5 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)

### 1999

- a página traz, antes da Série C, as seletivas estaduais (RS, PR, MG, PB, PE, PI); esse trecho fica de fora
- tabela publicada x jogos — Primeira fase / Grupo C: Náutico tabela [10, 8, 2, 0, 25, 7] jogos [10, 8, 2, 0, 25, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo C: Fluminense-BA tabela [10, 1, 1, 8, 8, 25] jogos [10, 1, 1, 8, 7, 25] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo D: Villa Nova-MG tabela [10, 5, 3, 2, 13, 10] jogos [10, 5, 3, 2, 13, 7] — placar diverge entre RSSSF e ogol em Villa Nova-MG x Anapolina (1-0 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / Grupo D: Anapolina tabela [10, 4, 2, 4, 11, 9] jogos [10, 4, 2, 4, 8, 9] — placar diverge entre RSSSF e ogol em Villa Nova-MG x Anapolina (1-0 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- placar diferente no ogol — Ji-Paraná x Ypiranga-AP (1999-09-09): RSSSF 1-2, ogol 1-1; fica o da RSSSF
- jogo só no ogol, incluído em First Phase / Grupo A: Ji-Paraná 0-2 São Raimundo (1999-10-03)
- só na RSSSF (não achado no ogol): Anapolina 2-0 São Raimundo (1999-11-07)
- só na RSSSF (não achado no ogol): Brasil de Pelotas 0-1 Serra (1999-11-07)

### 2001

- jogo só no ogol, incluído em First Phase / Grupo B: Guarany 2-1 Tocantinópolis (2001-09-19)

### 2002

- dúvida em aberto: o ogol liga o 'SER São Gabriel' da RSSSF ao 'EC São Gabriel', que a ficha do ogol diz fundado em 2013; pode ser erro do ogol. Fica como está (decisão do agente principal, 20/11/2026)
- tabela publicada x jogos — Primeira fase / Grupo 2: Tuna Luso tabela [6, 3, 2, 1, 8, 5] jogos [6, 3, 2, 1, 9, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo 2: Águia tabela [6, 1, 1, 4, 6, 9] jogos [6, 1, 1, 4, 7, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 2003

- tabela publicada x jogos — Primeira fase / Grupo 17: Uberaba tabela [4, 1, 1, 2, 3, 5] jogos [4, 1, 1, 2, 2, 4] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo 19: Tupi tabela [6, 3, 1, 2, 9, 5] jogos [6, 3, 1, 2, 8, 4] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar da página corrigido — Atlético Roraima 1-3 Rio Branco-AC (2003-10-16) vira Atlético Roraima 1-2 Rio Branco-AC: ogol e Wikipédia: 1-2 (revisão SC-014)
- placar diferente no ogol — Uberlândia x Francana (2003-09-17): RSSSF 1-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Taveirópolis x CENE (2003-09-21): RSSSF 0-2, ogol 1-2; fica o da RSSSF
- placar diferente no ogol — Rio Negro-AM x CFA (2003-10-05): RSSSF 3-0, ogol 3-1; fica o da RSSSF
- placar diferente no ogol — Rio Branco-AC x Atlético Roraima (2003-10-12): RSSSF 1-0, ogol 2-1; fica o da RSSSF
- mando invertido no ogol — RSSSF Ituano 0-0 Santo André, ogol Santo André 0-0 Ituano (2003-11-30); fica a RSSSF
- ida e volta de Goytacaz x Americano-RJ vinham com a mesma data (2003-10-12); ficam 2003-10-12, 2003-10-15 (do ogol)

### 2004

- placar diferente no ogol — Porto-PE x Coruripe (2004-08-15): RSSSF 0-1, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Hermann Aichinger x Cianorte (2004-08-15): RSSSF 1-1, ogol 0-0; fica o da RSSSF
- placar diferente no ogol — Gama x Cuiabá (2004-09-19): RSSSF 2-1, ogol 1-2; fica o da RSSSF

### 2005

- a página traz o público no fim da linha dos jogos das fases finais ('att: 18.865'); o leitor lê o público (12 jogos)
- tabela publicada x jogos — Primeira fase / Grupo 16: Atlético Sorocaba tabela [6, 2, 2, 2, 5, 4] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- placar diferente no ogol — Operário-MS x Cianorte (2005-08-21): RSSSF 1-3, ogol 1-1; fica o da RSSSF

### 2006

- tabela publicada x jogos — Primeira fase / Grupo 11: Vitória-ES tabela [6, 1, 2, 3, 5, 9] jogos [6, 1, 1, 4, 5, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Terceira fase / Grupo 25: Rio Negro-AM tabela [6, 0, 0, 6, 2, 15] jogos [6, 0, 0, 6, 2, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 2007

- tabela publicada x jogos — Primeira fase / Grupo 3: Ananindeua tabela [6, 2, 3, 1, 6, 5] jogos [6, 2, 3, 1, 6, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo 16: Esportivo-RS tabela [6, 3, 1, 2, 6, 9] jogos [6, 3, 0, 3, 6, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / Grupo 21: Itumbiara tabela [6, 1, 1, 4, 4, 7] jogos [6, 1, 1, 4, 3, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — ABC x Vera Cruz-PE (2007-07-14): RSSSF 3-0, ogol 4-0; fica o da RSSSF
- placar diferente no ogol — Atlético-PB x Central (2007-07-29): RSSSF 2-0, ogol 3-0; fica o da RSSSF
- placar diferente no ogol — Volta Redonda x América-RJ (2007-08-29): RSSSF 3-1, ogol 3-0; fica o da RSSSF
- placar diferente no ogol — Rio Branco-AC x Sampaio Corrêa (2007-09-02): RSSSF 1-0, ogol 2-0; fica o da RSSSF

### 2008

- tabela publicada x jogos — Primeira fase / Grupo 10: Itumbiara tabela [6, 2, 2, 2, 6, 5] jogos [6, 2, 2, 2, 6, 4] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo da página que fica de fora (1): Inter/SM 3-2 Engenheiro Beltrão — jogo repetido na página (o grupo 15 fica com 7 jogos por clube; a tabela fecha com o 3-0 de 17/08) (revisão SC-010)
- jogo da página que fica de fora (1): Toledo CW 1-1 Marcílio Dias — o mesmo jogo da 2ª fase (24/08), repetido na 1ª (revisão SC-010)
- placar diferente no ogol — Barras x Sampaio Corrêa (2008-07-27): RSSSF 2-1, ogol 0-3; fica o da RSSSF
- placar corrigido pelo ogol — Toledo x Marcílio Dias (2008-08-17): RSSSF 0-0, ogol 1-1; fica o do ogol, que fecha com a tabela publicada
- placar corrigido pelo ogol — Rio Branco-AC x Duque de Caxias (2008-10-08): RSSSF 2-2, ogol 3-0; fica o do ogol, que fecha com a tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Toledo x Marcílio Dias, ogol 2008-08-17); fica a do ogol

### 2009

- jogo só no ogol, incluído em FIRST STAGE: / Grupo 3: Boa Esporte 3-0 Guaratinguetá (2009-05-24)
- jogo só no ogol, incluído em FIRST STAGE: / Grupo 2: Salgueiro 1-0 CRB (2009-05-24)
- jogo só no ogol, incluído em FOURTH STAGE:: América-MG 1-0 ASA (2009-09-19)
- a fase "Quarta fase" é mata-mata com 1 confronto(s): vira "Final"
- a fase "Terceira fase" é mata-mata com 2 confronto(s): vira "Semifinal"
- a fase "Segunda fase" é mata-mata com 4 confronto(s): vira "Quartas de final"

### 2010

- tabela publicada x jogos — Primeira fase / Grupo B: CRB tabela [8, 3, 2, 3, 9, 11] jogos [8, 3, 2, 3, 8, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo B: CRB tabela [8, 3, 2, 3, 9, 11] jogos [8, 3, 2, 3, 8, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Marília x Gama, ogol 2010-08-15); fica a do ogol

### 2011

- o Rio Branco-AC foi eliminado pelo STJD depois de recorrer à Justiça comum; a RSSSF mantém 3 jogos dele na 2ª fase, que o ogol não tem (ficam, com a fonte RSSSF)
- sem os 3 jogos do Rio Branco-AC na 2ª fase (eliminado pelo STJD; o grupo E recomeçou com o Luverdense), o 3º é o Ipatinga, como na Wikipédia (revisão SC-003, SC-013). A edição fica com 106 jogos; o infobox da Wikipédia diz 105 (diferença não achada, revisão SC-021)
- tabela publicada x jogos — Primeira fase / Grupo D: Chapecoense tabela [8, 5, 1, 2, 13, 6] jogos [8, 5, 1, 2, 13, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo D: Joinville tabela [8, 4, 3, 1, 16, 11] jogos [8, 4, 3, 1, 17, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo D: Chapecoense tabela [8, 5, 1, 2, 13, 6] jogos [8, 5, 1, 2, 13, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo D: Joinville tabela [8, 4, 3, 1, 16, 11] jogos [8, 4, 3, 1, 17, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo da página que fica de fora (1): CRB 0-0 Rio Branco — Rio Branco-AC eliminado pelo STJD: os jogos da 2ª fase não contam (revisão SC-013)
- jogo da página que fica de fora (1): Rio Branco 1-2 Paysandu — Rio Branco-AC eliminado pelo STJD: os jogos da 2ª fase não contam (revisão SC-013)
- jogo da página que fica de fora (1): América 3-0 Rio Branco — Rio Branco-AC eliminado pelo STJD: os jogos da 2ª fase não contam (revisão SC-013)

### 2012

- sem ocorrências

### 2013

- o Rio Branco-AC entrou na competição por decisão judicial; a página da RSSSF não traz os 20 jogos dele no grupo A, que entram pelo ogol (a tabela do grupo fecha)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Rio Branco-AC 0-2 Fortaleza (2013-06-14)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Luverdense 4-0 Rio Branco-AC (2013-07-03)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Rio Branco-AC 1-3 Baraúnas (2013-07-06)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Rio Branco-AC 1-2 Águia (2013-07-11)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Brasiliense 1-0 Rio Branco-AC (2013-07-18)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Rio Branco-AC 0-3 Sampaio Corrêa (2013-07-21)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Rio Branco-AC 1-0 CRB (2013-07-25)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Santa Cruz 4-0 Rio Branco-AC (2013-08-01)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Rio Branco-AC 0-2 Cuiabá (2013-08-04)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Treze 3-0 Rio Branco-AC (2013-08-15)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Fortaleza 6-0 Rio Branco-AC (2013-08-22)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Rio Branco-AC 1-2 Treze (2013-08-29)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Baraúnas 2-1 Rio Branco-AC (2013-09-01)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Águia 1-0 Rio Branco-AC (2013-09-05)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Rio Branco-AC 1-2 Brasiliense (2013-09-12)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Rio Branco-AC 1-0 Luverdense (2013-09-18)
- jogo só no ogol, incluído em Primeira fase / Grupo A: CRB 2-0 Rio Branco-AC (2013-09-22)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Cuiabá 3-0 Rio Branco-AC (2013-09-26)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Rio Branco-AC 0-2 Santa Cruz (2013-10-03)
- jogo só no ogol, incluído em Primeira fase / Grupo A: Sampaio Corrêa 2-1 Rio Branco-AC (2013-10-10)

### 2014

- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Macaé

### 2015

- a página da RSSSF trocou dia e mês em 37 datas ('06/jan/15' em vez de 02/06); vale a data do ogol
- data com dia e mês trocados na RSSSF em 37 jogos (ex.: Cuiabá x Fortaleza); fica a data do ogol

### 2016

- sem ocorrências

### 2017

- Mogi Mirim x Ypiranga-RS (grupo B) foi W.O. ('0-WO' na página): entra 0-3, como conta a tabela do grupo
- placar diferente na ESPN — Mogi Mirim x Ypiranga-RS (2017-08-12): aqui 0-3, ESPN 0-0; fica o daqui
- placar diferente na ESPN — Volta Redonda x Sampaio Corrêa (2017-09-16): aqui 0-1, ESPN 0-0; fica o daqui

### 2018

- sem ocorrências

### 2019

- a página da RSSSF parou na 1ª rodada (40 jogos): a base dos jogos é o ogol (194), sem autores de gols
- a página da RSSSF parou na 1ª rodada (40 jogos): a base dos jogos é o ogol (194 jogos)
- placar diferente na ESPN — ABC x Imperatriz (2019-06-08): aqui 2-4, ESPN 2-3; fica o daqui
- 2 disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)

### 2020

- placar diferente na ESPN — São Bento x Brusque (2020-08-13): aqui 0-1, ESPN 0-0; fica o daqui
- a final (Vila Nova-GO x Remo) vem na página dentro de um grupo da Segunda fase; vira a fase Final

### 2021

- sem ocorrências

### 2022

- sem ocorrências

### 2023

- placar diferente na ESPN — Aparecidense x Confiança (2023-08-12): aqui 1-0, ESPN 1-1; fica o daqui
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Amazonas

### 2024

- a página da RSSSF traz os autores dos gols sem dizer de que time é cada um ('18' (25-Pedro Henrique)'): ficam só no texto (gols_texto)

### 2025

- sem ocorrências

### 2026

- a RSSSF ainda não tem a página de 2026: os jogos, as fases e os grupos vêm do ogol, e o campeão, os acessos e os rebaixados da Wikipédia (revisão SC-001). Sem autores de gols
- a RSSSF ainda não tem a página de 2026: a base dos jogos é o ogol (revisão SC-001)

## Identidade dos clubes

- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol (`data/coleta/bra-serie-c/ogol/clubes.json`).
- 168 clubes já estavam no `futebol.db` e usam o nome de lá; os outros seguem o nome curto do ogol, com "-UF" só quando outro
  clube tem o mesmo nome. Clubes que mudaram de nome aparecem com o nome atual (Intercap = Paraíso; Santo Amaro = Manchete;
  Ituiutaba = Boa Esporte); os nomes de cada fonte e ano estão em `clubes.csv` (`nomes_fonte`).
- Decisões à mão (em `clubes_c.py` e `importar.py`, com o motivo): EC Corinthians de Presidente Prudente não é o Corinthians
  do banco (vira "Corinthians Prudente"); o Maringá FC de 2010 e o de 1995 não são o GE Maringá do banco; "JMalucelli" é o
  J.Malucelli do banco.
- Novorizontino separado em dois (decisão do Guilherme, 20/11/2026): "GE Novorizontino" (1973-1999, campeão da Série C de
  1994; Série C 1988 e 1994) e "Novorizontino" (Grêmio Novorizontino, fundado em 2010; Série C 2021). O banco ainda junta os
  dois; o pedido para separar está em `docs/coleta/pedidos.md`.

## O que não deu para coletar

- **Cartões:** nenhuma das fontes lidas traz cartões da Série C (a RSSSF não traz; a ESPN não tem lances da Série C).
  O ogol tem cartões e autores dos gols na página de cada jogo, mas seriam uns 8 mil pedidos (cerca de 3 horas);
  fica como próximo passo, se aprovado.
- **Autores dos gols:** só onde a RSSSF traz e a soma fecha com o placar. Faltam (quase) todos em 1994-2001, 2008, 2011,
  2012, 2019 e 2024.
- **Público:** a ESPN traz 0 na Série C e a RSSSF só em poucas fichas de final.
- **Hora e estádio:** RSSSF (2013-2015, 2020, 2023, 2024), ogol (hora) e ESPN (2017 em diante).
- **Classificação final:** a ordem oficial existe só quando a RSSSF publica a classificação geral (7 edições); nas outras ela é
  calculada (fase alcançada, pontos, vitórias, saldo, gols pró), com campeão e vice em cima.
- **Acesso:** marcado quando o clube jogou a Série B no ano seguinte (pelo `futebol.db`) ou está nos "promovidos" do infobox
  da Wikipédia. **Rebaixamento:** marcas "Relegated" das tabelas da RSSSF e "rebaixados" do infobox.
