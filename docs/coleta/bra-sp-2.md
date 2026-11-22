# Campeonato Paulista Série A2 (2ª divisão) — coleta de dados

Gerado por `python coleta/bra-sp-2/importar.py`. Pacote em `data/coleta/bra-sp-2/pacote/`. Mesmo código do Paulista
(`docs/coleta/bra-sp-1.md`), com as fontes da 2ª divisão.

**Temporadas:** as que têm os jogos em alguma fonte: 1979, 1985-1988 e 1995-2026. Nome oficial de cada época na
lista da RSSSF (Segunda Divisão, Divisão Intermediária, Divisão Especial; Série A2 desde 1994). Campeões conferidos
na lista da RSSSF (`sp2camp.htm`).

**Fontes:** RSSSF Brasil (`sp{ano}l2.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada edição,
de 1998 em diante, e o código de cada clube; confere placares, traz a rodada e completa os jogos que a página não traz).
Artilheiros pela lista da RSSSF (`sp2tops.htm`). 2026 vem só do ogol (a RSSSF ainda não tem a página).

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,
fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` ou nos
outros pacotes usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`). Acesso: o clube que joga a 1ª
divisão do ano seguinte (pacote `bra-sp-1`).

**Ficam de fora** (decisão pendente com o Guilherme) as temporadas sem os jogos: 1947-1966 (a RSSSF traz só a
classificação final em pontos e os jogos do campeão), 1989 (só a 1ª fase; a final está no ogol), 1991 (só a 2ª fase),
1992-1994 (só a classificação), os anos sem página (1965, 1967-1978, 1980-1984, 1990) e a fase amadora (1916-1946,
só a lista de campeões).

| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|---|
| 1979 | RSSSF | 21 | 267 (0) | 540 | 0 | 1 / 3 | Taubaté | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1985 | RSSSF | 52 | 684 (0) | 1401 | 0 | 5 / 4 | Mogi Mirim | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1986 | RSSSF | 55 | 820 (0) | 1463 | 0 | 11 / 2 | Bandeirante-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1987 | RSSSF | 54 | 594 (0) | 1072 | 0 | 0 / 0 | União São João | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1988 | RSSSF + ogol | 28 | 359 (2) | 648 | 0 | 0 / 6 | Bragantino | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1995 | RSSSF | 16 | 345 (0) | 788 | 0 | 2 / 0 | Mogi Mirim | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1996 | RSSSF | 16 | 252 (0) | 658 | 0 | 3 / 1 | Inter de Limeira | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1997 | RSSSF | 16 | 188 (0) | 578 | 0 | 2 / 2 | Matonense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1998 | RSSSF + ogol | 16 | 200 (200) | 569 | 0 | 2 / 1 | União Barbarense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1999 | RSSSF + ogol | 16 | 214 (214) | 630 | 0 | 8 / 2 | América-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2000 | RSSSF + ogol | 18 | 188 (188) | 528 | 0 | 10 / 0 | São Caetano | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2001 | RSSSF + ogol | 16 | 240 (240) | 774 | 0 | 0 / 0 | Paulista | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2002 | RSSSF + ogol | 17 | 128 (126) | 409 | 0 | 2 / 0 | Marília | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2003 | RSSSF + ogol | 17 | 120 (118) | 348 | 0 | 4 / 0 | Oeste | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2004 | RSSSF + ogol | 16 | 148 (148) | 419 | 0 | 3 / 2 | Inter de Limeira | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2005 | RSSSF + ogol | 20 | 205 (205) | 564 | 0 | 3 / 1 | Juventus-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2006 | RSSSF + ogol | 20 | 206 (205) | 645 | 0 | 3 / 1 | Barueri | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2007 | RSSSF + ogol | 20 | 216 (216) | 602 | 0 | 3 / 1 | Portuguesa | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2008 | RSSSF + ogol | 20 | 217 (216) | 613 | 0 | 4 / 3 | Santo André | RSSSF (classificação geral publicada) |
| 2009 | RSSSF + ogol | 20 | 216 (216) | 577 | 0 | 6 / 0 | Monte Azul | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2010 | RSSSF + ogol | 20 | 214 (214) | 644 | 0 | 7 / 0 | Linense | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2011 | RSSSF + ogol | 20 | 205 (205) | 566 | 0 | 9 / 0 | XV de Piracicaba | RSSSF (classificação geral publicada) |
| 2012 | RSSSF + ogol | 20 | 216 (216) | 616 | 0 | 1 / 0 | São Bernardo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2013 | RSSSF + ogol | 20 | 216 (216) | 516 | 283 | 4 / 0 | Portuguesa | RSSSF (classificação geral publicada) |
| 2014 | RSSSF + ogol | 20 | 190 (190) | 463 | 428 | 0 / 0 | Capivariano | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2015 | RSSSF + ogol | 20 | 190 (190) | 502 | 486 | 1 / 0 | Ferroviária-SP | RSSSF (classificação geral publicada) |
| 2016 | RSSSF + ogol | 20 | 203 (203) | 462 | 452 | 7 / 0 | Santo André | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2017 | RSSSF + ogol | 20 | 195 (195) | 508 | 504 | 2 / 0 | São Caetano | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2018 | RSSSF + ogol | 16 | 125 (125) | 336 | 331 | 3 / 0 | Guarani | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2019 | RSSSF + ogol | 16 | 134 (134) | 310 | 305 | 8 / 0 | Santo André | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2020 | RSSSF + ogol | 16 | 134 (134) | 311 | 305 | 8 / 0 | São Caetano | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2021 | RSSSF + ogol | 16 | 134 (134) | 272 | 268 | 1 / 0 | São Bernardo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2022 | RSSSF + ogol | 16 | 134 (134) | 271 | 271 | 0 / 0 | Portuguesa | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2023 | RSSSF + ogol | 16 | 134 (134) | 327 | 318 | 0 / 0 | Ponte Preta | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2024 | RSSSF + ogol | 16 | 134 (134) | 317 | 301 | 0 / 0 | Velo Clube | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2025 | RSSSF + ogol | 16 | 134 (134) | 288 | 274 | 1 / 1 | Capivariano | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2026 | ogol | 16 | 150 (150) | 352 | 0 | 0 / 0 | Juventus-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |

## Conferência e correções, ano a ano

### 1979

- tabela publicada x jogos — Primeira fase / Grupo B: Rio Claro tabela [18, 7, 5, 6, 17, 19] jogos [18, 7, 5, 6, 18, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo B: Rio Branco-SP tabela [18, 5, 9, 4, 17, 16] jogos [18, 6, 8, 4, 19, 16] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo B: Sãocarlense tabela [18, 5, 9, 4, 16, 11] jogos [18, 5, 9, 4, 16, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo B: Barretos tabela [18, 5, 9, 4, 15, 13] jogos [18, 8, 3, 7, 15, 13] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo B: Corinthians Prudente tabela [18, 7, 3, 8, 11, 13] jogos [18, 7, 2, 9, 11, 15] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo B: Catanduvense tabela [18, 5, 6, 7, 21, 19] jogos [18, 5, 5, 8, 16, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo B: Araçatuba tabela [18, 5, 6, 7, 17, 19] jogos [18, 5, 6, 7, 21, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / Grupo A-B: Esportiva Guaratinguetá tabela [12, 5, 7, 0, 14, 8] jogos [12, 6, 6, 0, 15, 8] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / Grupo A-B: Santo André tabela [12, 6, 4, 2, 20, 10] jogos [12, 6, 4, 2, 19, 9] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / Grupo A-B: Portuguesa Santista tabela [12, 5, 5, 2, 16, 11] jogos [12, 5, 5, 2, 17, 10] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / Grupo A-B: Ginásio Pinhalense tabela [12, 4, 4, 4, 14, 15] jogos [12, 4, 4, 4, 12, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / Grupo A-B: Sãocarlense tabela [12, 2, 5, 5, 10, 14] jogos [12, 2, 5, 5, 8, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / Grupo A-B: Votuporanguense tabela [12, 2, 5, 5, 8, 14] jogos [12, 2, 4, 6, 7, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / Grupo A-B: Barretos tabela [12, 1, 4, 7, 13, 24] jogos [12, 1, 5, 6, 13, 22] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / Grupo A-B: Rio Branco-SP tabela [12, 1, 4, 7, 7, 19] jogos [12, 1, 3, 8, 7, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase final / -: Taubaté tabela [6, 4, 1, 1, 8, 8] jogos [6, 4, 1, 1, 8, 4] — há jogo do clube sem conferência no ogol
- Aliança — clube que o ogol não tem; entra só pela RSSSF
- Araçatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Araçatuba)
- Barretos — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Barretos)
- Catanduvense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Catanduvense)
- Corinthians — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Corinthians Prudente)
- Esportiva — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Esportiva Guaratinguetá)
- Ginásio Pinhalense — clube que o ogol não tem; entra só pela RSSSF
- Independente — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Independente de Limeira)
- Linense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Linense)
- Marília — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marília)
- Nacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-SP)
- Paulista — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paulista)
- Pinhalense — clube que o ogol não tem; entra só pela RSSSF
- Portuguesa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Portuguesa Santista)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-SP)
- Rio Claro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Claro)
- Saad — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Saad S. Caetano)
- Santo André — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santo André)
- São José — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São José-SP)
- Sãocarlense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sãocarlense)
- Taubaté — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Taubaté)
- Votuporanguense — clube que o ogol não tem; entra só pela RSSSF

### 1985

- Nacional x São Bernardo (31/08): a vitória foi dada ao São Bernardo no tribunal, sem placar (o jogo terminou 0 a 0 e o Nacional escalou jogador irregular); Barretos x Sãocarlense (18/08): vitória dada ao Barretos (1 a 1 em campo)
- tabela publicada x jogos — Primeira fase / Grupo Verde: EC São Bernardo tabela [24, 14, 8, 2, 29, 13] jogos [23, 13, 8, 2, 29, 13] — a tabela conta 24 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / Grupo Verde: Bragantino tabela [24, 9, 9, 6, 24, 22] jogos [24, 9, 9, 6, 24, 23] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo Verde: Nacional-SP tabela [24, 6, 9, 9, 22, 27] jogos [23, 6, 9, 8, 22, 27] — a tabela conta 24 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / Grupo Verde: Saltense tabela [24, 3, 7, 14, 14, 30] jogos [23, 3, 7, 13, 14, 29] — a tabela conta 24 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / Grupo Amarelo: Barretos tabela [24, 12, 5, 7, 24, 21] jogos [23, 11, 5, 7, 23, 20] — a tabela conta 24 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / Grupo Amarelo: Sãocarlense tabela [24, 11, 7, 6, 27, 13] jogos [23, 11, 7, 5, 26, 12] — a tabela conta 24 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / Grupo Preto: Dracena tabela [24, 4, 6, 14, 16, 40] jogos [24, 4, 6, 14, 16, 42] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / Grupo Preto: Tanabi tabela [6, 3, 2, 1, 5, 3] jogos [5, 2, 2, 1, 5, 3] — a tabela conta 6 jogos e as fontes trazem 5
- tabela publicada x jogos — Segunda fase / Grupo Preto: Araçatuba tabela [6, 2, 3, 1, 5, 2] jogos [5, 2, 3, 0, 5, 2] — a tabela conta 6 jogos e as fontes trazem 5
- Aparecida — clube que o ogol não tem; entra só pela RSSSF
- Araçatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Araçatuba)
- Bandeirante — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bandeirante-SP)
- Barretos — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Barretos)
- Batatais — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Batatais)
- Bragantino — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bragantino)
- Candidomotense — clube que o ogol não tem; entra só pela RSSSF
- Capivariano — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Capivariano)
- Catanduvense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Catanduvense)
- Corinthians — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Corinthians Prudente)
- Cruzeiro — clube que o ogol não tem; entra só pela RSSSF
- DERAC — clube que o ogol não tem; entra só pela RSSSF
- Dracena — clube que o ogol não tem; entra só pela RSSSF
- Fernandópolis — clube que o ogol não tem; entra só pela RSSSF
- Francana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Francana)
- Garça — clube que o ogol não tem; entra só pela RSSSF
- Guaçuano — clube que o ogol não tem; entra só pela RSSSF
- Independente — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Independente de Limeira)
- Internacional — clube que o ogol não tem; entra só pela RSSSF
- Jaboticabal — clube que o ogol não tem; entra só pela RSSSF
- Jalesense — clube que o ogol não tem; entra só pela RSSSF
- Lemense (Leme) — não é o Lemense, de outra cidade
- Lemense — clube que o ogol não tem; entra só pela RSSSF
- Linense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Linense)
- Mogi Mirim — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mogi Mirim)
- Nacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-SP)
- Novorizontino — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (GE Novorizontino)
- Palmeiras (São João Da Boa Vista) — não é o Palmeiras, de outra cidade
- Palmeiras — clube que o ogol não tem; entra só pela RSSSF
- Penapolense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Penapolense)
- Pinhalense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ginásio Pinhalense)
- Portuguesa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Portuguesa Santista)
- Primavera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Primavera-SP)
- Radium — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Radium)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-SP)
- Rio Claro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Claro)
- Rio Preto — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Preto)
- Saad — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Saad S. Caetano)
- Saltense — clube que o ogol não tem; entra só pela RSSSF
- Santa Fé — clube que o ogol não tem; entra só pela RSSSF
- Sertãozinho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sertãozinho)
- São Bernardo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (EC São Bernardo)
- São José — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São José-SP)
- Sãocarlense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sãocarlense)
- Tanabi — clube que o ogol não tem; entra só pela RSSSF
- Taquaritinga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Taquaritinga)
- Taubaté — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Taubaté)
- União — clube que o ogol não tem; entra só pela RSSSF
- União Agrícola — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União Barbarense)
- União São João — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União São João)
- VOCEM — clube que o ogol não tem; entra só pela RSSSF
- Velo Clube — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Velo Clube)
- Votuporanguense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Votuporanguense)

### 1986

- tabela publicada x jogos — Primeira fase / Grupo Branco: EC Lemense tabela [26, 11, 8, 7, 22, 22] jogos [26, 11, 8, 7, 23, 21] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo Branco: Guaçuano tabela [26, 6, 7, 13, 25, 35] jogos [25, 6, 7, 12, 25, 32] — a tabela conta 26 jogos e as fontes trazem 25
- tabela publicada x jogos — Primeira fase / Grupo Preto: Jalesense tabela [26, 8, 13, 5, 20, 16] jogos [26, 7, 14, 5, 20, 16] — há jogo do clube sem conferência no ogol
- Aparecida — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aparecida)
- Araçatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Araçatuba)
- Bandeirante — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bandeirante-SP)
- Barretos — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Barretos)
- Batatais — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Batatais)
- Bragantino — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bragantino)
- Candidomotense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Candidomotense)
- Capivariano — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Capivariano)
- Catanduvense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Catanduvense)
- Corinthians — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Corinthians Prudente)
- Cruzeiro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cruzeiro-SP)
- DERAC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (DERAC)
- Fernandópolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fernandópolis)
- Francana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Francana)
- Garça — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Garça)
- Guaratinguetá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Esportiva Guaratinguetá)
- Guaçuano — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guaçuano)
- Independente — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Independente de Limeira)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional de Bebedouro)
- Jalesense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jalesense)
- Lemense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (EC Lemense)
- Lençoense — clube que o ogol não tem; entra só pela RSSSF
- Linense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Linense)
- Marília — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marília)
- Mauaense — clube que o ogol não tem; entra só pela RSSSF
- Mirassol — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mirassol)
- Nacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-SP)
- Noroeste — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Noroeste)
- Orlândia — clube que o ogol não tem; entra só pela RSSSF
- Palmeiras — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Palmeiras (São João da Boa Vista))
- Penapolense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Penapolense)
- Pinhalense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ginásio Pinhalense)
- Portuguesa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Portuguesa Santista)
- Primavera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Primavera-SP)
- Radium — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Radium)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-SP)
- Rio Claro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Claro)
- Rio Preto — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Preto)
- Saad — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Saad S. Caetano)
- Saltense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Saltense)
- Santa Fé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Fé)
- Sertãozinho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sertãozinho)
- São Bernardo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (EC São Bernardo)
- São José — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São José-SP)
- Sãocarlense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sãocarlense)
- Tanabi — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tanabi)
- Taquaritinga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Taquaritinga)
- Taubaté — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Taubaté)
- União — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União Mogi)
- União Agrícola — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União Barbarense)
- União São João — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União São João)
- VOCEM — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (VOCEM)
- Velo Clube — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Velo Clube)
- Votuporanguense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Votuporanguense)

### 1987

- Aparecida — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Aparecida)
- Araçatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Araçatuba)
- Barretos — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Barretos)
- Batatais — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Batatais)
- Bragantino — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bragantino)
- Candidomotense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Candidomotense)
- Capivariano — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Capivariano)
- Catanduvense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Catanduvense)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-RP)
- Corinthians — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Corinthians Prudente)
- Cruzeiro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Cruzeiro-SP)
- DERAC — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (DERAC)
- Esportiva Guaratinguetá — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Esportiva Guaratinguetá)
- Fernandópolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fernandópolis)
- Francana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Francana)
- Garça — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Garça)
- Ginásio Pinhalense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ginásio Pinhalense)
- Guaçuano — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Guaçuano)
- Independente — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Independente de Limeira)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Internacional de Bebedouro)
- Jalesense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Jalesense)
- Lemense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (EC Lemense)
- Lençoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Lençoense)
- Linense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Linense)
- Marília — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marília)
- Mauaense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mauaense)
- Mirassol — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mirassol)
- Nacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-SP)
- Palmeiras — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Palmeiras (São João da Boa Vista))
- Paulista — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paulista)
- Penapolense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Penapolense)
- Portuguesa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Portuguesa Santista)
- Primavera — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Primavera-SP)
- Radium — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Radium)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-SP)
- Rio Claro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Claro)
- Rio Preto — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Preto)
- Saad — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Saad S. Caetano)
- Saltense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Saltense)
- Santa Fé — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santa Fé)
- Sertãozinho — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sertãozinho)
- São Bernardo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (EC São Bernardo)
- São José — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São José-SP)
- Sãocarlense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sãocarlense)
- Tanabi — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tanabi)
- Taquaritinga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Taquaritinga)
- Taubaté — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Taubaté)
- União — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União Mogi)
- União Agrícola Barbarense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União Barbarense)
- União São João — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União São João)
- VOCEM — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (VOCEM)
- Velo Club — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Velo Clube)
- Votuporanguense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Votuporanguense)

### 1988

- 69 jogos vêm na página só com o resultado ("venceu", "empatou", "perdeu" ou "-"), sem placar, e ficam fora do pacote; por isso as tabelas da 1ª fase não fecham. O ogol não tem esses jogos
- tabela publicada x jogos — Segunda fase / Grupo A: EC São Bernardo tabela [24, 10, 9, 5, 14, 12] jogos [9, 3, 2, 4, 6, 8] — a tabela conta 24 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / Grupo A: Taubaté tabela [24, 10, 8, 6, 25, 11] jogos [10, 5, 3, 2, 13, 5] — a tabela conta 24 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / Grupo A: Nacional-SP tabela [24, 6, 9, 9, 15, 18] jogos [8, 3, 2, 3, 9, 7] — a tabela conta 24 jogos e as fontes trazem 8
- tabela publicada x jogos — Segunda fase / Grupo A: União Mogi tabela [23, 5, 7, 11, 13, 25] jogos [8, 4, 2, 2, 9, 6] — a tabela conta 23 jogos e as fontes trazem 8
- tabela publicada x jogos — Segunda fase / Grupo A: Saad S. Caetano tabela [23, 5, 5, 13, 9, 33] jogos [8, 2, 2, 4, 3, 11] — a tabela conta 23 jogos e as fontes trazem 8
- tabela publicada x jogos — Segunda fase / Grupo A: Esportiva Guaratinguetá tabela [24, 3, 9, 12, 9, 24] jogos [9, 2, 3, 4, 4, 7] — a tabela conta 24 jogos e as fontes trazem 9
- tabela publicada x jogos — Segunda fase / Grupo B: Bragantino tabela [24, 14, 6, 4, 22, 7] jogos [10, 8, 1, 1, 11, 3] — a tabela conta 24 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / Grupo B: Paulista tabela [24, 11, 7, 6, 31, 16] jogos [10, 3, 2, 5, 14, 14] — a tabela conta 24 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / Grupo B: Ituano tabela [24, 9, 11, 4, 27, 16] jogos [10, 3, 4, 3, 12, 12] — a tabela conta 24 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / Grupo B: Palmeiras (São João da Boa Vista) tabela [24, 11, 6, 7, 20, 17] jogos [10, 4, 2, 4, 9, 9] — a tabela conta 24 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / Grupo B: Rio Branco-SP tabela [23, 10, 7, 6, 20, 13] jogos [11, 4, 3, 4, 9, 8] — a tabela conta 23 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / Grupo B: EC Lemense tabela [24, 5, 12, 7, 15, 18] jogos [10, 3, 4, 3, 8, 9] — a tabela conta 24 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / Grupo B: Radium tabela [24, 4, 7, 13, 13, 23] jogos [11, 2, 2, 7, 6, 14] — a tabela conta 24 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / Grupo C: Comercial-RP tabela [27, 12, 9, 6, 26, 15] jogos [12, 9, 1, 2, 18, 5] — a tabela conta 27 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / Grupo C: Taquaritinga tabela [28, 8, 12, 8, 13, 16] jogos [12, 4, 4, 4, 7, 6] — a tabela conta 28 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / Grupo C: Francana tabela [26, 11, 5, 10, 28, 30] jogos [12, 5, 1, 6, 12, 14] — a tabela conta 26 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / Grupo C: Rio Preto tabela [26, 10, 7, 9, 19, 21] jogos [12, 6, 2, 4, 9, 9] — a tabela conta 26 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / Grupo C: Tanabi tabela [28, 10, 6, 12, 23, 24] jogos [12, 5, 2, 5, 11, 11] — a tabela conta 28 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / Grupo C: Votuporanguense tabela [26, 8, 10, 8, 17, 19] jogos [12, 3, 4, 5, 10, 11] — a tabela conta 26 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / Grupo C: Fernandópolis tabela [27, 6, 14, 7, 18, 14] jogos [12, 2, 8, 2, 9, 7] — a tabela conta 27 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / Grupo C: Mirassol tabela [28, 10, 3, 15, 21, 34] jogos [12, 3, 0, 9, 10, 23] — a tabela conta 28 jogos e as fontes trazem 12
- tabela publicada x jogos — Segunda fase / Grupo D: Marília tabela [27, 13, 8, 6, 30, 15] jogos [10, 4, 3, 3, 8, 5] — a tabela conta 27 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / Grupo D: Corinthians Prudente tabela [28, 11, 12, 5, 25, 9] jogos [10, 3, 5, 2, 5, 4] — a tabela conta 28 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / Grupo D: Catanduvense tabela [26, 9, 11, 6, 22, 14] jogos [10, 6, 3, 1, 15, 4] — a tabela conta 26 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / Grupo D: Lençoense tabela [26, 9, 10, 7, 19, 18] jogos [11, 5, 3, 3, 12, 10] — a tabela conta 26 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / Grupo D: VOCEM tabela [28, 8, 10, 10, 16, 22] jogos [10, 2, 3, 5, 4, 7] — a tabela conta 28 jogos e as fontes trazem 10
- tabela publicada x jogos — Segunda fase / Grupo D: Linense tabela [24, 5, 8, 11, 16, 26] jogos [11, 2, 4, 5, 8, 14] — a tabela conta 24 jogos e as fontes trazem 11
- tabela publicada x jogos — Segunda fase / Grupo D: Araçatuba tabela [28, 5, 8, 15, 17, 33] jogos [10, 2, 3, 5, 6, 14] — a tabela conta 28 jogos e as fontes trazem 10
- tabela publicada x jogos — Terceira fase / Grupo III: Catanduvense tabela [10, 6, 3, 1, 8, 1] jogos [9, 5, 3, 1, 8, 1] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Terceira fase / Grupo III: Taubaté tabela [10, 5, 4, 1, 12, 6] jogos [9, 4, 4, 1, 12, 6] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Terceira fase / Grupo III: EC São Bernardo tabela [10, 3, 5, 2, 7, 7] jogos [9, 3, 4, 2, 7, 7] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Terceira fase / Grupo III: Rio Branco-SP tabela [10, 3, 2, 5, 10, 11] jogos [9, 3, 1, 5, 10, 11] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Terceira fase / Grupo III: Comercial-RP tabela [10, 3, 1, 6, 10, 15] jogos [9, 3, 1, 5, 10, 15] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Terceira fase / Grupo III: Rio Preto tabela [10, 2, 1, 7, 5, 12] jogos [9, 2, 1, 6, 5, 12] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Terceira fase / Grupo IV: Bragantino tabela [10, 7, 2, 1, 7, 2] jogos [9, 5, 3, 1, 7, 2] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Terceira fase / Grupo IV: Lençoense tabela [10, 3, 5, 2, 9, 8] jogos [9, 3, 4, 2, 9, 8] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Terceira fase / Grupo IV: Paulista tabela [10, 3, 5, 2, 7, 5] jogos [9, 3, 5, 1, 7, 5] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Terceira fase / Grupo IV: Ituano tabela [10, 3, 4, 3, 12, 9] jogos [9, 3, 3, 3, 12, 9] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Terceira fase / Grupo IV: Marília tabela [10, 2, 4, 4, 8, 11] jogos [9, 2, 3, 4, 8, 11] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Terceira fase / Grupo IV: Corinthians Prudente tabela [10, 1, 2, 7, 5, 13] jogos [9, 1, 2, 6, 5, 13] — a tabela conta 10 jogos e as fontes trazem 9
- Araçatuba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Araçatuba)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-RP)
- Corinthians — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Corinthians Prudente)
- Esportiva — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Esportiva Guaratinguetá)
- Fernandópolis — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Fernandópolis)
- Francana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Francana)
- Lemense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (EC Lemense)
- Lençoense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Lençoense)
- Linense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Linense)
- Marília — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Marília)
- Mirassol — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mirassol)
- Nacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Nacional-SP)
- Palmeiras — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Palmeiras (São João da Boa Vista))
- Paulista — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paulista)
- Radium — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Radium)
- Rio Branco — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Branco-SP)
- Rio Preto — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Preto)
- Saad — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Saad S. Caetano)
- São Bernardo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (EC São Bernardo)
- Tanabi — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Tanabi)
- Taquaritinga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Taquaritinga)
- Taubaté — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Taubaté)
- União — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (União Mogi)
- VOCEM — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (VOCEM)
- Votuporanguense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Votuporanguense)

### 1995

- a página não tem a lista de participantes: Internacional (de Limeira), Botafogo (de Ribeirão Preto), Nacional (da capital) e Catanduva (o GE Catanduvense, que mudou de nome em 1994) foram casados à mão
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-RP)
- Ituano — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ituano)
- Mogi-Mirim — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Mogi Mirim)
- Olímpia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Olímpia)
- Paraguaçuense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paraguaçuense)
- Portuguesa Santista — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Portuguesa Santista)
- Rio Preto — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Preto)
- Santo André — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santo André)
- São José — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São José-SP)
- Sãocarlense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sãocarlense)
- Taquaritinga — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Taquaritinga)
- XV de Jaú — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (XV de Jaú)
- campeão pela lista oficial, Mogi Mirim; o 1º pela soma dos jogos da última fase é Ituano (desempate, jogo extra ou pontos tirados fora de campo)

### 1996

- tabela publicada x jogos — Segunda fase / -: XV de Piracicaba tabela [30, 13, 5, 12, 46, 43] jogos [30, 14, 5, 11, 46, 43] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Santo André tabela [30, 12, 6, 12, 50, 37] jogos [30, 13, 4, 13, 50, 37] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Portuguesa Santista tabela [30, 11, 8, 11, 18, 33] jogos [30, 11, 8, 11, 28, 33] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Bandeirante-SP tabela [30, 6, 6, 18, 35, 65] jogos [30, 6, 6, 18, 34, 64] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Rio Preto tabela [30, 6, 4, 20, 28, 62] jogos [30, 6, 4, 20, 24, 59] — há jogo do clube sem conferência no ogol
- Bandeirante — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bandeirante-SP)
- Bragantino — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bragantino)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-RP)
- Internacional — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Inter de Limeira)
- Ituano — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ituano)
- Noroeste — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Noroeste)
- Olimpia — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Olímpia)
- Paraguaçuense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paraguaçuense)
- Paulista — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paulista)
- Ponte Preta — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ponte Preta)
- Portuguesa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Portuguesa Santista)
- Rio Preto — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Rio Preto)
- Santo André — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santo André)
- São José — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (São José-SP)
- Sãocarlense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sãocarlense)

### 1997

- Ferroviária 1x1 Noroeste (23/02): jogo inacabado; a FPF deu a vitória à Ferroviária, e a tabela conta 1 a 0. A 1ª fase vai do jogo entre grupos (8 rodadas) ao turno e returno dentro dos grupos (14 rodadas), como nas tabelas da página (22 jogos por clube)
- tabela publicada x jogos — Primeira fase / Grupo 1: Santo André tabela [22, 11, 11, 0, 43, 23] jogos [22, 11, 11, 0, 45, 23] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo 2: Francana tabela [22, 8, 5, 9, 38, 43] jogos [22, 8, 5, 9, 38, 42] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo 2: Comercial-RP tabela [22, 6, 9, 7, 32, 28] jogos [22, 6, 9, 7, 32, 30] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo 2: Paraguaçuense tabela [22, 6, 6, 10, 30, 37] jogos [22, 6, 6, 10, 31, 37] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Primeira fase / Grupo 2: XV de Jaú tabela [22, 1, 8, 13, 34, 61] jogos [22, 1, 8, 13, 33, 60] — há jogo do clube sem conferência no ogol
- Bragantino — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bragantino)
- Comercial — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-RP)
- Corinthians-PP — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Corinthians Prudente)
- Ferroviaria — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ferroviária-SP)
- Francana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Francana)
- Ituano — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ituano)
- Matonense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Matonense)
- Noroeste — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Noroeste)
- Novorizontino — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (GE Novorizontino)
- Paraguacuense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paraguaçuense)
- Paulista — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paulista)
- Ponte Preta — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ponte Preta)
- Santo Andre — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santo André)
- Saocarlense — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Sãocarlense)
- XV de Jau — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (XV de Jaú)

### 1998

- tabela publicada x jogos — Torneio de rebaixamento / -: Corinthians Prudente tabela [6, 2, 3, 1, 12, 10] jogos [6, 2, 3, 1, 13, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Corintians-PP
- Corintians-PP — clube que o ogol não tem; entra só pela RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Mirassol x GE Novorizontino, ogol 1998-04-01); fica a do ogol

### 1999

- tabela publicada x jogos — Torneio de rebaixamento / -: Paraguaçuense tabela [6, 3, 1, 2, 10, 8] jogos [6, 3, 1, 2, 10, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Torneio de rebaixamento / -: Paraguaçuense tabela [6, 3, 1, 2, 10, 8] jogos [6, 3, 1, 2, 10, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 16 jogos (ex.: Francana x XV de Piracicaba, ogol 1999-04-04); fica a do ogol
- jogo só no ogol, incluído em First Phase: Corinthians Prudente 0-0 Ponte Preta (1999-02-28)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, América-SP

### 2000

- a 1ª fase tem semifinal e final próprias: o Botafogo venceu e subiu para a 1ª divisão no meio do ano (não joga a 2ª fase); o título da A2 é do vencedor da 2ª fase em diante

### 2001

- campeão: Etti Jundiaí, nome do Paulista FC de 1999 a 2001 (patrocínio)
- placar diferente no ogol — Nacional-SP x Ituano (2001-03-03): RSSSF 1-0, ogol 0-1; fica o da RSSSF

### 2002

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Portuguesa
- Portuguesa — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Portuguesa)
- só na RSSSF (não achado no ogol): Francana 2-2 Portuguesa (2002-06-02)
- só na RSSSF (não achado no ogol): Portuguesa 2-2 Francana (2002-06-05)

### 2003

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Botafogo
- Botafogo — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Botafogo-SP)
- placar diferente no ogol — Rio Preto x Francana (2003-02-26): RSSSF 1-3, ogol 1-2; fica o da RSSSF
- só na RSSSF (não achado no ogol): Atlético Sorocaba 2-1 Botafogo-SP (2003-04-02)
- só na RSSSF (não achado no ogol): Botafogo-SP 0-0 Atlético Sorocaba (2003-04-05)

### 2004

- tabela publicada x jogos — Primeira fase / Grupo 3: Taubaté tabela [6, 2, 3, 1, 7, 6] jogos [8, 4, 3, 1, 14, 6] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / Grupo 3: Taquaritinga tabela [6, 2, 3, 1, 7, 6] jogos [8, 2, 3, 3, 7, 9] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / Grupo 3: Nacional-SP tabela [6, 2, 2, 2, 9, 7] jogos [8, 2, 2, 4, 9, 14] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / Grupo 3: Francana tabela [6, 1, 2, 3, 6, 10] jogos [8, 3, 2, 3, 9, 10] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / Grupo 4: Flamengo-SP tabela [6, 4, 1, 1, 10, 7] jogos [8, 5, 2, 1, 12, 8] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / Grupo 4: Inter de Limeira tabela [6, 2, 3, 1, 7, 6] jogos [8, 2, 4, 2, 8, 8] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / Grupo 4: Botafogo-SP tabela [6, 1, 3, 2, 11, 11] jogos [8, 2, 3, 3, 13, 13] — a tabela conta 6 jogos e as fontes trazem 8
- tabela publicada x jogos — Primeira fase / Grupo 4: Bandeirante-SP tabela [6, 0, 3, 3, 12, 16] jogos [8, 1, 3, 4, 14, 18] — a tabela conta 6 jogos e as fontes trazem 8

### 2005

- tabela publicada x jogos — Primeira fase / Grupo 2: São Bento tabela [18, 13, 4, 1, 33, 12] jogos [18, 13, 4, 1, 35, 12] — placar diverge entre RSSSF e ogol em Matonense x São Bento (0-3 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Primeira fase / Grupo 2: Matonense tabela [18, 1, 1, 16, 13, 66] jogos [18, 1, 1, 16, 13, 68] — placar diverge entre RSSSF e ogol em Matonense x São Bento (0-3 x None-None) e nenhuma das versões fecha com a tabela; fica a RSSSF

### 2006

- tabela publicada x jogos — Primeira fase / Grupo 1: União São João tabela [18, 9, 6, 3, 29, 18] jogos [19, 10, 6, 3, 30, 18] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / Grupo 1: Bandeirante-SP tabela [18, 7, 4, 7, 26, 25] jogos [19, 7, 4, 8, 26, 26] — a tabela conta 18 jogos e as fontes trazem 19
- só na RSSSF (não achado no ogol): Bandeirante-SP 0-1 União São João (2006-04-02)

### 2007

- tabela publicada x jogos — Primeira fase / -: Portuguesa tabela [19, 5, 7, 7, 28, 30] jogos [19, 11, 5, 3, 36, 21] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 2008

- tabela publicada x jogos — Segunda fase / Grupo 3: Oeste tabela [6, 3, 2, 1, 7, 5] jogos [7, 4, 2, 1, 10, 7] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — Segunda fase / Grupo 3: Mogi Mirim tabela [6, 2, 2, 2, 6, 6] jogos [7, 2, 2, 3, 8, 9] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — Segunda fase / Grupo 3: Oeste tabela [6, 4, 1, 1, 10, 7] jogos [7, 4, 2, 1, 10, 7] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — Segunda fase / Grupo 3: Mogi Mirim tabela [6, 2, 1, 3, 8, 9] jogos [7, 2, 2, 3, 8, 9] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase final / -: Oeste tabela [27, 11, 8, 8, 32, 28] jogos [28, 12, 8, 8, 35, 30] — a tabela conta 27 jogos e as fontes trazem 28
- tabela publicada x jogos — Fase final / -: Mogi Mirim tabela [25, 13, 6, 6, 36, 23] jogos [26, 13, 6, 7, 38, 26] — a tabela conta 25 jogos e as fontes trazem 26
- placar diferente no ogol — Mogi Mirim x Oeste (2008-05-24): RSSSF 0-0, ogol 2-3; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Mogi Mirim x Oeste, ogol 2008-05-24); fica a do ogol
- só na RSSSF (não achado no ogol): Mogi Mirim 2-3 Oeste (2008-05-24)

### 2009

- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Monte Azul

### 2010

- jogo só no ogol, incluído em FIRST STAGE:: São Bernardo 3-0 Flamengo-SP (2010-02-20)
- jogo só no ogol, incluído em FIRST STAGE:: Rio Preto 1-0 São José-SP (2010-02-20)
- jogo só no ogol, incluído em FIRST STAGE:: Catanduvense 3-2 Grêmio Osasco (2010-02-20)

### 2011

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Guarani x Palmeiras (B), ogol 2011-03-01); fica a do ogol
- jogo só no ogol, incluído em FIRST STAGE: / Group 1: América-SP 3-2 Marília (2011-02-19)
- jogo só no ogol, incluído em FIRST STAGE: / Group 1: União São João 2-3 Ferroviária-SP (2011-02-19)
- jogo só no ogol, incluído em FIRST STAGE: / Group 2: Palmeiras (B) 2-3 Rio Branco-SP (2011-02-26)
- jogo só no ogol, incluído em FIRST STAGE: / Group 2: Osasco Audax 6-0 União Barbarense (2011-02-26)
- jogo só no ogol, incluído em FIRST STAGE: / Group 2: Guarani 1-1 Atlético Sorocaba (2011-02-26)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, XV de Piracicaba

### 2012

- jogo só no ogol, incluído em FIRST STAGE:: São José-SP 1-0 Penapolense (2012-04-01)
- jogo só no ogol, incluído em FIRST STAGE:: Red Bull Bragantino II 1-1 Ferroviária-SP (2012-04-01)
- jogo só no ogol, incluído em FIRST STAGE:: Rio Preto 0-4 Velo Clube (2012-04-01)
- jogo só no ogol, incluído em FIRST STAGE:: Santo André 1-0 União Barbarense (2012-04-01)
- jogo só no ogol, incluído em FIRST STAGE:: Noroeste 0-1 União São João (2012-04-01)
- jogo só no ogol, incluído em FIRST STAGE:: Atlético Sorocaba 3-2 São Carlos (2012-04-01)
- jogo só no ogol, incluído em FIRST STAGE:: Monte Azul 1-1 América-SP (2012-04-01)
- jogo só no ogol, incluído em FIRST STAGE:: Osasco Audax 1-2 Santacruzense (2012-04-01)
- jogo só no ogol, incluído em FIRST STAGE:: São Bernardo 4-0 Palmeiras (B) (2012-04-01)
- jogo só no ogol, incluído em FIRST STAGE:: Barueri 1-3 Rio Claro (2012-04-01)
- jogo só no ogol, incluído em Segunda fase / Grupo 2: União Barbarense 4-1 Atlético Sorocaba (2012-04-07)
- jogo só no ogol, incluído em Segunda fase / Grupo 2: Ferroviária-SP 1-2 Osasco Audax (2012-04-07)
- jogo só no ogol, incluído em Segunda fase / Grupo 3: Noroeste 1-0 São Bernardo (2012-04-07)
- jogo só no ogol, incluído em Segunda fase / Grupo 3: Penapolense 0-0 Red Bull Bragantino II (2012-04-08)
- jogo só no ogol, incluído em Segunda fase / Grupo 2: Osasco Audax 2-2 União Barbarense (2012-04-11)
- jogo só no ogol, incluído em Segunda fase / Grupo 2: Atlético Sorocaba 5-0 Ferroviária-SP (2012-04-11)
- jogo só no ogol, incluído em Segunda fase / Grupo 3: Red Bull Bragantino II 1-1 Noroeste (2012-04-11)
- jogo só no ogol, incluído em Segunda fase / Grupo 3: São Bernardo 1-3 Penapolense (2012-04-11)
- jogo só no ogol, incluído em Segunda fase / Grupo 2: Osasco Audax 2-3 Atlético Sorocaba (2012-04-14)
- jogo só no ogol, incluído em Segunda fase / Grupo 3: Red Bull Bragantino II 1-2 São Bernardo (2012-04-14)
- jogo só no ogol, incluído em Segunda fase / Grupo 2: Ferroviária-SP 0-2 União Barbarense (2012-04-14)
- jogo só no ogol, incluído em Segunda fase / Grupo 3: Penapolense 4-1 Noroeste (2012-04-15)
- jogo só no ogol, incluído em Segunda fase / Grupo 2: União Barbarense 2-1 Ferroviária-SP (2012-04-21)
- jogo só no ogol, incluído em Segunda fase / Grupo 3: São Bernardo 4-1 Red Bull Bragantino II (2012-04-21)
- jogo só no ogol, incluído em Segunda fase / Grupo 3: Noroeste 1-1 Penapolense (2012-04-21)
- jogo só no ogol, incluído em Segunda fase / Grupo 2: Atlético Sorocaba 1-0 Osasco Audax (2012-04-21)
- jogo só no ogol, incluído em Segunda fase / Grupo 3: Penapolense 0-1 São Bernardo (2012-04-25)
- jogo só no ogol, incluído em Segunda fase / Grupo 2: União Barbarense 0-2 Osasco Audax (2012-04-25)
- jogo só no ogol, incluído em Segunda fase / Grupo 3: Noroeste 1-2 Red Bull Bragantino II (2012-04-25)
- jogo só no ogol, incluído em Segunda fase / Grupo 2: Ferroviária-SP 1-0 Atlético Sorocaba (2012-04-26)
- jogo só no ogol, incluído em Segunda fase / Grupo 3: São Bernardo 2-0 Noroeste (2012-04-28)
- jogo só no ogol, incluído em Segunda fase / Grupo 3: Red Bull Bragantino II 1-1 Penapolense (2012-04-28)
- jogo só no ogol, incluído em Segunda fase / Grupo 2: Osasco Audax 3-1 Ferroviária-SP (2012-04-29)
- jogo só no ogol, incluído em Segunda fase / Grupo 2: Atlético Sorocaba 2-2 União Barbarense (2012-04-29)
- jogo só no ogol, incluído em Final: União Barbarense 1-1 São Bernardo (2012-05-05)
- jogo só no ogol, incluído em Final: São Bernardo 2-2 União Barbarense (2012-05-12)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, São Bernardo

### 2013

- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Portuguesa

### 2014

- data diferente entre RSSSF e ogol (mais de 3 dias) em 10 jogos (ex.: São Bento x Monte Azul, ogol 2014-02-16); fica a do ogol
- jogo só no ogol, incluído em Phase: Barueri 2-1 Mirassol (2014-02-05)
- jogo só no ogol, incluído em Phase: Mirassol 3-1 Monte Azul (2014-03-16)

### 2015

- sem ocorrências

### 2016

- 1 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência

### 2017

- 1 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência

### 2018

- 1 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência

### 2019

- jogo só no ogol, incluído em First Phase: Nacional-SP 0-0 Rio Claro (2019-01-31)

### 2020

- sem ocorrências

### 2021

- data diferente entre RSSSF e ogol (mais de 3 dias) em 8 jogos (ex.: Portuguesa Santista x XV de Piracicaba, ogol 2021-04-23); fica a do ogol

### 2022

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): XV de Novembro
- XV de Novembro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (XV de Piracicaba)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 8 jogos (ex.: Portuguesa x Monte Azul, ogol 2022-01-31); fica a do ogol

### 2023

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paulista
- Paulista — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paulista)
- jogo só no ogol, incluído em STAGE:: Lemense 3-1 Velo Clube (2023-01-18)
- jogo só no ogol, incluído em STAGE:: Linense 0-0 Juventus-SP (2023-01-18)
- jogo só no ogol, incluído em STAGE:: Primavera-SP 1-1 Linense (2023-02-26)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Ponte Preta

### 2024

- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Noroeste x Portuguesa Santista na Semi-finals sempre na mesma ordem) — ogol Portuguesa Santista 1-1 Noroeste (2024-04-07)

### 2025

- tabela publicada x jogos — Primeira fase / -: Taubaté tabela [15, 7, 2, 6, 19, 18] jogos [19, 7, 3, 9, 20, 23] — a tabela conta 15 jogos e as fontes trazem 19
- placar diferente no ogol — Taubaté x São Bento (2025-02-02): RSSSF 0-1, ogol 1-0; fica o da RSSSF
- jogo só no ogol, incluído em Phase: Portuguesa Santista 0-3 São José-SP (2025-02-20)
- jogo só no ogol, incluído em Phase: Oeste 2-2 Portuguesa Santista (2025-03-01)
- jogo só no ogol, incluído em Quarters-finals: Ituano 3-1 Ferroviária-SP (2025-03-19)
- Capivariano x Primavera-SP (2025-04-02) vem na página em "Semifinal"; o ogol diz "Final", que fica
- Primavera-SP x Capivariano (2025-04-05) vem na página em "Semifinal"; o ogol diz "Final", que fica

### 2026

- sem página da RSSSF: os jogos vêm do ogol

## Identidade dos clubes

- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.
- Antes de 1998 o ogol não tem os jogos: o nome da página é casado com as fichas do ogol (da A2 e da A1) pela **cidade**
  da lista de participantes da mesma página ("AA Portuguesa (Santos)" é a Portuguesa Santista; "EC Corinthians
  (Presidente Prudente)" é o Corinthians Prudente). Ficha de clube fundado depois da edição não vale (a AA
  Votuporanguense dos anos 1980 não é o CA Votuporanguense, de 2009; o EC Lemense não é o Lemense FC, de 2005).
- Clube que o ogol não tem entra pela RSSSF, com código "rs-<nome>-<cidade>". Nunca com o nome exato de outro clube
  (regra 6b): "Palmeiras (São João da Boa Vista)", "Internacional de Bebedouro", "União Mogi", "EC Lemense".
- Ferroviário Atlético Ituano é o Ituano de hoje (mesmo clube, nome antigo).

## O que não deu para coletar

- **Edições sem os jogos:** veja "Ficam de fora" acima.
- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).
- **Autores dos gols:** só onde a RSSSF traz (a partir de 2013) e a soma fecha com o placar.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;
  torneio de rebaixamento e repescagem não contam como fase alcançada.
