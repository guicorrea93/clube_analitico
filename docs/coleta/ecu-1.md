# Campeonato Equatoriano (1ª divisão) — coleta de dados

Gerado por `python coleta/ecu-1/importar.py`. Pacote em `data/coleta/ecu-1/pacote/`.

**Edições:** 68, uma por título de campeão equatoriano, de 1957 a 2025, como na lista de campeões da RSSSF (`ecuachamp.html`) e na Wikipédia em inglês (página "LigaPro Serie A", seção "Champions by year"). Um campeão por ano; sem campeonato em 1958 e 1959; em 2005 houve dois campeões (Apertura e Clausura), uma edição cada. Apertura, Clausura, etapas, liguillas, hexagonais e finais são fases da edição anual.

**Até 1967:** o campeonato nacional era um torneio curto entre os melhores dos campeonatos regionais (o Interandino, de Quito e Ambato, e o de Guayaquil); clubes da mesma associação não se enfrentavam. Os regionais são outras competições e ficam de fora. Em 1964 os clubes de Guayaquil não jogaram.

**Fora do pacote:** os campeonatos regionais, a Serie B e as divisões de baixo, a Copa Ecuador, a Supercopa de 1969 e os playoffs da Copa Sudamericana e da Copa Conmebol.

**Fontes:** RSSSF (uma página por temporada, `ecua57` e `ecua60` a `ecua2025`, em `data/coleta/ecu-1/rsssf/`: base de jogos de todos os anos, com fases, grupos, rodadas, datas e autores dos gols; de 1960 a 1974 parte das fases vem em tabela de confrontos, sem rodada nem data, com o mandante na linha); ESPN (liga `ecu.1`, 2005 em diante: os jogos de 2011, 2012 e 2025, que a RSSSF só traz em tabela, e nos outros anos hora, estádio, público, gols com minuto e cartões); Wikipédia em inglês (segunda fonte do campeão e do vice).

**Clubes:** nome pelo qual o clube é conhecido no Brasil (Emelec, LDU de Quito, Independiente del Valle). Homônimos de outros países levam a cidade: Barcelona de Guayaquil, Universidad Católica de Quito, River Plate de Manta (1963, 1966) e de Riobamba (1987, 1988), dois clubes diferentes, Libertad de Loja, Santos de El Guabo, Juventus de Esmeraldas, Santa Rita de Vinces; os Américas de Quito, Ambato e Manta também. O mesmo clube com outro nome fica com o atual: Independiente José Terán = Independiente del Valle; River Ecuador = Guayaquil City; Cuniburo = Vinotinto; Manta SC = Manta Sport (outro clube que o Manta FC, de 1998). "LDU" e "Deportivo" sozinhos, nas páginas de 1997-2002, dependem do ano (conferido com as tabelas): em 2001 a LDU da Serie A é a de Portoviejo (a de Quito jogou a Serie B).

**Regras:** o placar é o da RSSSF (ou da ESPN, nos jogos que vêm só dela). Jogo decidido no tribunal leva o placar dado (`awd`), com o de campo na observação. Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos: 2 por vitória até 1994 e 3 a partir de 1995; as liguillas e hexagonais finais começam com pontos de bônus da fase anterior (o `ajuste_pontos` da classificação). Em 1998 o empate ia para os pênaltis (2 pontos para quem ganhava, 1 para quem perdia): a tabela da página separa os empates ("5/1"), aqui somados.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1957 | 4 | 8 (8) | 28 | 0 | 1 / 0 | Emelec | RSSSF (ecua57) |
| 1960 | 8 | 32 (32) | 124 | 0 | 1 / 0 | Barcelona de Guayaquil | RSSSF (ecua60) |
| 1961 | 8 | 32 (32) | 118 | 0 | 1 / 0 | Emelec | RSSSF (ecua61) |
| 1962 | 8 | 33 (33) | 107 | 0 | 1 / 0 | Everest | RSSSF (ecua62) |
| 1963 | 11 | 37 (37) | 104 | 0 | 3 / 0 | Barcelona de Guayaquil | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1964 | 8 | 31 (31) | 87 | 0 | 2 / 0 | Deportivo Quito | RSSSF (ecua64) |
| 1965 | 8 | 33 (33) | 80 | 0 | 0 / 1 | Emelec | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1966 | 16 | 104 (104) | 323 | 0 | 5 / 0 | Barcelona de Guayaquil | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1967 | 10 | 91 (91) | 224 | 0 | 1 / 0 | El Nacional | RSSSF (ecua67) |
| 1968 | 12 | 182 (182) | 490 | 0 | 1 / 2 | Deportivo Quito | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1969 | 14 | 182 (182) | 543 | 0 | 1 / 0 | LDU de Quito | RSSSF (ecua69) |
| 1970 | 13 | 228 (228) | 569 | 0 | 2 / 1 | Barcelona de Guayaquil | RSSSF (ecua70) |
| 1971 | 16 | 224 (224) | 614 | 0 | 3 / 1 | Barcelona de Guayaquil | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1972 | 10 | 119 (119) | 346 | 0 | 3 / 0 | Emelec | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1973 | 12 | 217 (217) | 555 | 0 | 2 / 2 | El Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1974 | 10 | 116 (116) | 307 | 0 | 2 / 0 | LDU de Quito | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1975 | 12 | 242 (242) | 642 | 0 | 3 / 0 | LDU de Quito | RSSSF (ecua75) |
| 1976 | 12 | 194 (194) | 522 | 2 | 3 / 0 | El Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1977 | 12 | 210 (210) | 561 | 0 | 2 / 1 | El Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1978 | 12 | 194 (194) | 483 | 0 | 3 / 0 | El Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1979 | 12 | 210 (210) | 529 | 0 | 3 / 0 | Emelec | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1980 | 12 | 203 (203) | 496 | 6 | 3 / 0 | Barcelona de Guayaquil | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1981 | 12 | 188 (188) | 507 | 0 | 2 / 1 | Barcelona de Guayaquil | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1982 | 12 | 237 (237) | 655 | 6 | 1 / 2 | El Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1983 | 14 | 298 (298) | 853 | 0 | 4 / 0 | El Nacional | RSSSF (ecua83) |
| 1984 | 14 | 264 (264) | 742 | 0 | 6 / 0 | El Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1985 | 16 | 296 (296) | 827 | 0 | 2 / 0 | Barcelona de Guayaquil | RSSSF (ecua85) |
| 1986 | 16 | 320 (320) | 816 | 0 | 6 / 3 | El Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1987 | 18 | 378 (378) | 969 | 0 | 4 / 0 | Barcelona de Guayaquil | RSSSF (ecua87) |
| 1988 | 18 | 332 (332) | 819 | 0 | 3 / 0 | Emelec | RSSSF (ecua88) |
| 1989 | 13 | 234 (234) | 597 | 0 | 3 / 2 | Barcelona de Guayaquil | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1990 | 13 | 242 (242) | 626 | 0 | 5 / 2 | LDU de Quito | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1991 | 13 | 242 (242) | 684 | 0 | 6 / 1 | Barcelona de Guayaquil | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1992 | 13 | 227 (227) | 580 | 0 | 4 / 0 | El Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1993 | 12 | 184 (184) | 489 | 1 | 4 / 2 | Emelec | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1994 | 12 | 238 (238) | 649 | 0 | 3 / 1 | Emelec | RSSSF (ecua94) |
| 1995 | 12 | 289 (289) | 781 | 3 | 6 / 2 | Barcelona de Guayaquil | RSSSF (ecua95) |
| 1996 | 12 | 230 (230) | 603 | 3 | 5 / 1 | El Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 1997 | 12 | 234 (234) | 679 | 0 | 6 / 0 | Barcelona de Guayaquil | RSSSF (ecua97) |
| 1998 | 12 | 266 (266) | 768 | 0 | 9 / 1 | LDU de Quito | RSSSF (ecua98) |
| 1999 | 12 | 254 (254) | 691 | 1 | 5 / 0 | LDU de Quito | RSSSF (ecua99) |
| 2000 | 10 | 210 (210) | 556 | 0 | 3 / 1 | Olmedo | RSSSF (ecua00) |
| 2001 | 10 | 210 (210) | 543 | 0 | 4 / 0 | Emelec | RSSSF (ecua01) |
| 2002 | 10 | 210 (210) | 568 | 0 | 4 / 0 | Emelec | RSSSF (ecua02) |
| 2003 | 10 | 210 (210) | 631 | 380 | 2 / 2 | LDU de Quito | RSSSF (ecua03) |
| 2004 | 10 | 210 (210) | 581 | 342 | 4 / 0 | Deportivo Cuenca | RSSSF (ecua04) |
| 2005 Apertura | 10 | 104 (104) | 333 | 167 | 0 / 1 | LDU de Quito | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2005 Clausura | 10 | 120 (120) | 342 | 342 | 2 / 0 | El Nacional | RSSSF (ecua05) |
| 2006 | 11 | 210 (210) | 587 | 587 | 4 / 0 | El Nacional | calculada (fase alcançada, pontos, saldo, gols pró) |
| 2007 | 10 | 210 (210) | 529 | 518 | 4 / 0 | LDU de Quito | RSSSF (ecua07) |
| 2008 | 12 | 222 (222) | 520 | 508 | 5 / 0 | Deportivo Quito | RSSSF (ecua08) |
| 2009 | 12 | 232 (232) | 527 | 521 | 5 / 1 | Deportivo Quito | RSSSF (ecua09) |
| 2010 | 12 | 268 (268) | 644 | 633 | 3 / 0 | LDU de Quito | RSSSF (ecua2010) |
| 2011 | 12 | 268 (268) | 679 | 679 | 3 / 0 | Deportivo Quito | RSSSF (ecua2011) |
| 2012 | 12 | 268 (268) | 626 | 624 | 3 / 0 | Barcelona de Guayaquil | RSSSF (ecua2012) |
| 2013 | 12 | 264 (264) | 645 | 641 | 3 / 0 | Emelec | RSSSF (ecua2013) |
| 2014 | 12 | 266 (266) | 625 | 1 | 3 / 0 | Emelec | RSSSF (ecua2014) |
| 2015 | 12 | 266 (266) | 697 | 0 | 3 / 0 | Emelec | RSSSF (ecua2015) |
| 2016 | 12 | 264 (264) | 693 | 6 | 3 / 0 | Barcelona de Guayaquil | RSSSF (ecua2016) |
| 2017 | 12 | 266 (266) | 696 | 14 | 3 / 0 | Emelec | RSSSF (ecua2017) |
| 2018 | 12 | 266 (266) | 689 | 0 | 3 / 0 | LDU de Quito | RSSSF (ecua2018) |
| 2019 | 16 | 254 (254) | 682 | 6 | 1 / 0 | Delfín | RSSSF (ecua2019) |
| 2020 | 16 | 242 (242) | 669 | 19 | 3 / 0 | Barcelona de Guayaquil | RSSSF (ecua2020) |
| 2021 | 16 | 242 (242) | 658 | 641 | 3 / 0 | Independiente del Valle | RSSSF (ecua2021) |
| 2022 | 16 | 242 (242) | 587 | 583 | 3 / 0 | Aucas | RSSSF (ecua2022) |
| 2023 | 16 | 242 (242) | 598 | 581 | 3 / 0 | LDU de Quito | RSSSF (ecua2023) |
| 2024 | 16 | 242 (242) | 636 | 631 | 3 / 0 | LDU de Quito | RSSSF (ecua2024) |
| 2025 | 16 | 312 (312) | 794 | 794 | 4 / 0 | Independiente del Valle | RSSSF (ecua2025) |

## Conferência e correções, edição a edição

### 1957

- sem ocorrências

### 1960

- sem ocorrências

### 1961

- decidido fora de campo — Deportivo Quito Patria (s/d)

### 1962

- sem ocorrências

### 1963

- sem ocorrências

### 1964

- sem ocorrências

### 1965

- tabela publicada x jogos — ecua65:21: Barcelona de Guayaquil tabela [8, 4, 3, 1, 14, 10] jogos [8, 2, 5, 1, 14, 10] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — ecua65:21: 9 de Octubre tabela [8, 5, 1, 2, 10, 7] jogos [8, 4, 1, 3, 10, 7] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — ecua65:21: Patria tabela [8, 5, 1, 2, 9, 5] jogos [8, 4, 2, 2, 9, 5] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — ecua65:21: Aucas tabela [8, 0, 1, 7, 1, 15] jogos [8, 1, 4, 3, 4, 9] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1966

- sem ocorrências

### 1967

- sem ocorrências

### 1968

- tabela publicada x jogos — ecua68:33: Estibadores Navales tabela [22, 5, 5, 12, 31, 49] jogos [22, 5, 5, 12, 31, 50] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — ecua68:63: Estibadores Navales tabela [22, 5, 5, 12, 31, 49] jogos [22, 5, 5, 12, 31, 50] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1969

- sem ocorrências

### 1970

- tabela publicada x jogos — ecua70:67: Universidad Católica de Quito tabela [36, 12, 13, 11, 46, 34] jogos [36, 11, 14, 11, 46, 35] — a outra tabela publicada (ecua70) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua70:67: Aucas tabela [36, 11, 14, 11, 50, 44] jogos [36, 11, 15, 10, 51, 44] — a outra tabela publicada (ecua70) fecha com os jogos: o erro é desta tabela

### 1971

- tabela publicada x jogos — ecua71:31: El Nacional tabela [14, 8, 3, 3, 27, 15] jogos [14, 8, 3, 3, 29, 16] — a outra tabela publicada (ecua71) fecha com os jogos: o erro é desta tabela

### 1972

- sem ocorrências

### 1973

- tabela publicada x jogos — ecua73:35: América de Quito tabela [22, 9, 4, 9, 30, 24] jogos [22, 9, 3, 10, 29, 24] — a outra tabela publicada (ecua73) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua73:35: Atlético Riobamba tabela [22, 3, 8, 11, 20, 44] jogos [22, 4, 7, 11, 20, 43] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — ecua73:65: Deportivo Cuenca tabela [12, 7, 3, 2, 21, 5] jogos [12, 7, 3, 2, 21, 6] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1974

- sem ocorrências

### 1975

- sem ocorrências

### 1976

- sem ocorrências

### 1977

- tabela publicada x jogos — ecua77:354: El Nacional tabela [10, 6, 4, 0, 17, 0] jogos [10, 6, 4, 0, 17, 4] — a outra tabela publicada (ecua77) fecha com os jogos: o erro é desta tabela

### 1978

- sem ocorrências

### 1979

- sem ocorrências

### 1980

- sem ocorrências

### 1981

- tabela publicada x jogos — ecua81:355: LDU de Quito tabela [4, 2, 1, 1, 9, 6] jogos [4, 1, 1, 2, 8, 11] — a outra tabela publicada (ecua81) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua81:355: El Nacional tabela [4, 1, 1, 2, 8, 11] jogos [4, 2, 1, 1, 9, 6] — a outra tabela publicada (ecua81) fecha com os jogos: o erro é desta tabela

### 1982

- tabela publicada x jogos — ecua82:19: LDU de Quito tabela [18, 5, 3, 10, 14, 24] jogos [18, 5, 4, 9, 14, 24] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — ecua82:217: Aucas tabela [22, 6, 5, 11, 27, 44] jogos [22, 6, 5, 11, 27, 45] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1983

- sem ocorrências

### 1984

- sem ocorrências

### 1985

- sem ocorrências

### 1986

- tabela publicada x jogos — ecua86:34: 9 de Octubre tabela [14, 2, 1, 11, 13, 16] jogos [14, 2, 1, 11, 13, 26] — a outra tabela publicada (ecua86) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua86:270: Esmeraldas Petrolero tabela [14, 5, 3, 6, 14, 14] jogos [14, 6, 3, 5, 14, 14] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — ecua86:517: Esmeraldas Petrolero tabela [10, 1, 3, 6, 6, 13] jogos [10, 1, 3, 6, 6, 14] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 1987

- sem ocorrências

### 1988

- sem ocorrências

### 1989

- tabela publicada x jogos — ecua89:291: Deportivo Cuenca tabela [10, 4, 0, 6, 11, 17] jogos [10, 4, 0, 6, 11, 16] — a outra tabela publicada (ecua89) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua89:501: Emelec tabela [10, 6, 1, 3, 17, 15] jogos [10, 6, 1, 3, 20, 13] — a outra tabela publicada (ecua89) fecha com os jogos: o erro é desta tabela

### 1990

- tabela publicada x jogos — ecua90:302: Aucas tabela [10, 3, 3, 4, 15, 29] jogos [10, 3, 3, 4, 15, 22] — a outra tabela publicada (ecua90) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua90:302: Técnico Universitario tabela [10, 3, 2, 5, 11, 13] jogos [10, 4, 2, 4, 14, 13] — a outra tabela publicada (ecua90) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua90:585: Barcelona de Guayaquil tabela [6, 3, 2, 1, 10, 8] jogos [6, 1, 4, 1, 10, 8] — a outra tabela publicada (ecua90) fecha com os jogos: o erro é desta tabela

### 1991

- tabela publicada x jogos — ecua91:572: El Nacional tabela [6, 1, 3, 2, 8, 12] jogos [6, 2, 1, 3, 9, 12] — a outra tabela publicada (ecua91) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua91:572: Valdez SC tabela [6, 2, 1, 3, 7, 11] jogos [6, 1, 3, 2, 6, 11] — a outra tabela publicada (ecua91) fecha com os jogos: o erro é desta tabela

### 1992

- sem ocorrências

### 1993

- tabela publicada x jogos — ecua93:184: Aucas tabela [10, 4, 4, 2, 13, 19] jogos [10, 4, 4, 2, 13, 9] — a outra tabela publicada (ecua93) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua93:327: Deportivo Cuenca tabela [14, 2, 3, 9, 13, 29] jogos [14, 5, 3, 6, 14, 23] — a outra tabela publicada (ecua93) fecha com os jogos: o erro é desta tabela

### 1994

- tabela publicada x jogos — ecua94:287: Deportivo Quito tabela [12, 6, 4, 2, 24, 13] jogos [12, 6, 4, 2, 23, 12] — a outra tabela publicada (ecua94) fecha com os jogos: o erro é desta tabela

### 1995

- tabela publicada x jogos — ecua95:534: LDU de Portoviejo tabela [9, 2, 3, 4, 15, 9] jogos [9, 2, 3, 4, 15, 19] — a outra tabela publicada (ecua95) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua95:627: Espoli tabela [10, 6, 3, 1, 12, 6] jogos [10, 6, 3, 1, 13, 6] — a outra tabela publicada (ecua95) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua95:627: Barcelona de Guayaquil tabela [10, 5, 3, 2, 16, 8] jogos [10, 4, 4, 2, 16, 9] — a outra tabela publicada (ecua95) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua95:627: LDU de Quito tabela [10, 3, 2, 5, 9, 12] jogos [10, 3, 2, 5, 9, 13] — a outra tabela publicada (ecua95) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua95:627: Aucas tabela [10, 1, 1, 8, 6, 17] jogos [10, 1, 2, 7, 7, 17] — a outra tabela publicada (ecua95) fecha com os jogos: o erro é desta tabela

### 1996

- tabela publicada x jogos — ecua96:23: El Nacional tabela [22, 15, 5, 2, 42, 16] jogos [22, 15, 5, 2, 40, 14] — a outra tabela publicada (ecua96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua96:23: Emelec tabela [22, 14, 4, 4, 50, 19] jogos [22, 14, 4, 4, 50, 18] — a outra tabela publicada (ecua96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua96:23: Deportivo Quito tabela [22, 9, 8, 5, 39, 26] jogos [22, 9, 8, 5, 40, 26] — a outra tabela publicada (ecua96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua96:23: Deportivo Cuenca tabela [22, 9, 7, 6, 25, 20] jogos [22, 9, 7, 6, 23, 20] — a outra tabela publicada (ecua96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua96:23: Olmedo tabela [22, 9, 4, 9, 22, 27] jogos [22, 9, 4, 9, 22, 28] — a outra tabela publicada (ecua96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua96:23: Espoli tabela [22, 7, 8, 7, 23, 26] jogos [22, 8, 7, 7, 24, 23] — a outra tabela publicada (ecua96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua96:23: LDU de Quito tabela [22, 7, 4, 11, 30, 32] jogos [22, 7, 5, 10, 29, 30] — a outra tabela publicada (ecua96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua96:23: Técnico Universitario tabela [22, 7, 4, 11, 25, 42] jogos [22, 7, 4, 11, 25, 43] — a outra tabela publicada (ecua96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua96:23: Green Cross tabela [22, 6, 2, 14, 18, 41] jogos [22, 5, 3, 14, 16, 40] — a outra tabela publicada (ecua96) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua96:23: Aucas tabela [22, 3, 6, 13, 16, 29] jogos [22, 3, 5, 14, 16, 31] — a outra tabela publicada (ecua96) fecha com os jogos: o erro é desta tabela

### 1997

- não jogado — Calvi Deportivo Quevedo (1998-12-21)

### 1998

- tabela publicada x jogos — ecua98:377: Técnico Universitario tabela [10, 1, 6, 3, 10, 17] jogos [10, 1, 6, 3, 6, 14] — a outra tabela publicada (ecua98) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua98:377: Delfín tabela [10, 2, 3, 5, 16, 22] jogos [10, 2, 3, 5, 13, 18] — a outra tabela publicada (ecua98) fecha com os jogos: o erro é desta tabela
- corrigido — Delfín x Barcelona de Guayaquil (1998-05-09): jogo interrompido por invasão de campo aos 81 minutos, com 1-2, e terminado em 16 de maio (nota da página): vale o 1-2, como a tabela conta
- corrigido — Deportivo Quito x Emelec (1998-10-09): jogo abandonado no intervalo com 2-0 (o Emelec não voltou para o 2º tempo) e dado ao Deportivo Quito por 2-0 (nota da página), como a tabela do Hexagonal 1 conta
- decidido fora de campo — Deportivo Quito Emelec (1998-10-09): abandoned at 2-0 at half-time; Emelec dns for 2nd half; apparently awarded 2-0

### 1999

- sem ocorrências

### 2000

- tabela publicada x jogos — ecua00:393: Barcelona de Guayaquil tabela [36, 12, 12, 12, 44, 45] jogos [36, 12, 12, 12, 44, 44] — a outra tabela publicada (ecua00) fecha com os jogos: o erro é desta tabela

### 2001

- sem ocorrências

### 2002

- sem ocorrências

### 2003

- tabela publicada x jogos — ecua03:590: El Nacional tabela [10, 6, 0, 4, 21, 13] jogos [10, 6, 0, 4, 23, 13] — a outra tabela publicada (ecua03) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua03:737: Aucas tabela [36, 11, 8, 17, 45, 55] jogos [36, 11, 7, 18, 45, 55] — a outra tabela publicada (ecua03) fecha com os jogos: o erro é desta tabela
- tabela publicada x jogos — ecua03:737: Espoli tabela [36, 9, 8, 19, 49, 72] jogos [36, 9, 9, 18, 49, 72] — a outra tabela publicada (ecua03) fecha com os jogos: o erro é desta tabela
- corrigido — Deportivo Quito x Barcelona de Guayaquil (2003-03-02): jogo interrompido e completado depois: a página traz as duas linhas ("abd" e a do restante do jogo, com o placar final); fica a segunda

### 2004

- sem ocorrências

### 2005 Apertura

- tabela publicada x jogos — ecua05:23: LDU de Quito tabela [18, 13, 2, 3, 48, 22] jogos [18, 14, 1, 3, 48, 20] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)
- tabela publicada x jogos — ecua05:23: Emelec tabela [18, 5, 5, 8, 24, 31] jogos [18, 5, 4, 9, 22, 31] — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)

### 2005 Clausura

- ESPN: 120 jogos casados

### 2006

- ESPN: 209 jogos casados
- corrigido — Emelec x Barcelona de Guayaquil (2006-04-30): jogo interrompido e completado depois: a página traz as duas linhas ("abd" e a do restante do jogo, com o placar final); fica a segunda

### 2007

- ESPN: 210 jogos casados

### 2008

- ESPN: 220 jogos casados

### 2009

- ESPN: 229 jogos casados
- tabela publicada x jogos — ecua09:682: Emelec tabela [34, 18, 7, 9, 48, 30] jogos [34, 18, 7, 9, 47, 29] — a outra tabela publicada (ecua09) fecha com os jogos: o erro é desta tabela

### 2010

- ESPN: 262 jogos casados

### 2011

- ESPN: 268 jogos casados

### 2012

- ESPN: 266 jogos casados

### 2013

- ESPN: 264 jogos casados

### 2014

- ESPN: 266 jogos casados
- decidido fora de campo — Emelec Deportivo Quito (2014-10-19): awarded 3-0

### 2015

- ESPN: 266 jogos casados
- decidido fora de campo — LDU de Loja El Nacional (2015-07-04): awarded 0-3; match not played as
- decidido fora de campo — Deportivo Quito Guayaquil City (2015-11-22): awarded 0-3; Dep. Quito suspended

### 2016

- ESPN: 264 jogos casados

### 2017

- ESPN: 266 jogos casados
- decidido fora de campo — Fuerza Amarilla Guayaquil City (2017-10-14): awarded 0-3, Fuerza Amarilla suspended

### 2018

- ESPN: 266 jogos casados

### 2019

- ESPN: 253 jogos casados
- decidido fora de campo — Emelec América de Quito (2019-04-28): awarded 3-0; originally 0-0, América fielded Apr 29]                                         suspended player
- decidido fora de campo — América de Quito Deportivo Cuenca (2019-07-29): awarded 3-0; Cuenca were suspended
- decidido fora de campo — América de Quito Fuerza Amarilla (2019-10-20): awarded 3-0

### 2020

- ESPN: 242 jogos casados
- decidido fora de campo — Deportivo Cuenca Olmedo (2020-10-02): awarded 0-3; Cuenca suspended
- decidido fora de campo — El Nacional Guayaquil City (2020-11-29): awarded 0-3, Nacional suspended

### 2021

- ESPN: 240 jogos casados
- decidido fora de campo — Universidad Católica de Quito Olmedo (2021-02-19): awarded 3-0, Olmedo dns
- decidido fora de campo — Barcelona de Guayaquil Aucas (2021-04-12): awarded 3-0; abandoned at 2-0 in 17'

### 2022

- ESPN: 240 jogos casados
- decidido fora de campo — Guayaquil City Deportivo Cuenca (2022-02-20): awarded 3-0; abandoned at 2-0

### 2023

- ESPN: 241 jogos casados

### 2024

- ESPN: 241 jogos casados
- corrigido — El Nacional x Deportivo Cuenca (2024-03-23): jogo interrompido e completado depois: a página traz as duas linhas ("abd" e a do restante do jogo, com o placar final); fica a segunda

### 2025

- ESPN: 312 jogos casados
- corrigido — El Nacional x Delfín (2025-12-19): último jogo do Hexagonal 2 (El Nacional x Delfín, 19/12): a RSSSF diz que não foi disputado e as tabelas contam 39 jogos para os dois; a ESPN registra 0-3 (provável W.O. do El Nacional, rebaixado por dívidas)
- não jogado — El Nacional 0-3 Delfín (2025-12-19)

