# Reconferência dos achados do agente 1 (banco e painel)

Revisor RV · 21/11/2026 · saídas em `SCRATCH/reconferencia_RV.csv` e `SCRATCH/achados_RV.csv` · scripts em `revisao/RV/`.

**Resumo.** Dos 80 achados do agente 1, 55 estão corrigidos no banco e no site, 4 são `nao-e-erro` por decisão do Guilherme e 21 continuam abertos (7 deles esperam a coleta).
As correções quebraram 3 coisas: um jogo da 1ª fase da Série B 2001 virou 1-0 "awd" (RV-001), o América-MG aparece em 3º na Série B 2014 (RV-002) e as datas do ogol erraram o mês em 1980 e 1990 e divergem da pt em 1991 (RV-003).
Campeões das 5 competições não mudaram; os totais de jogos mudaram só onde houve correção.

## Como foi feito

- Banco `db/futebol.db` (refeito 21/11 09:24, só leitura), `painel/dados/<slug>.js` e o site. Baixei os 5 `dados/<slug>.js` e o `index.html`
  do site: são **iguais** aos arquivos locais (byte a byte), então os números do site são os do arquivo local.
- 30 prints do site no Chrome sem janela (`SCRATCH/RV/telas/`): classificação 2013 e 2003, corrida 2013, resumo 1959, 1968, 1987 e 2000,
  Flamengo e classificação 1999 (A); resumo 1999 e 2002, classificação 2001 e 2014, participantes 2011, jogos 2001, pódio e Coritiba (B);
  participantes 1988, artilharia 2007, curiosidades e jogos 2009 (C); resumo 2021 (D); resumo, classificação, pontos, artilharia 2013 e
  jogos 2019 (Copa); folha de escudos.
- **Celular:** o Chrome sem janela com `--window-size=420` desenha a página com 504 px (medido com `innerWidth`). Por isso pus o site num
  iframe de 420 px (`SCRATCH/RV/cel.html`): a página cabe. O "mais larga que a tela" da 1ª rodada vinha desse limite do Chrome.
- Mesmas fontes da 1ª rodada (Wikipédia en/pt já guardadas em `data/cache/revisao/SA`, `SB`, `data/serie_a/wikipedia/` e
  `data/coleta/bra-serie-c/wikipedia/`), mais os CSV da Série B do commit `04cb286` (estado da 1ª rodada) para ver o que mudou.

## Tabela

| id | antes | agora | nota |
|---|---|---|---|
| SA-001 | aberto | corrigido | 2013: Fluminense 15º, Flamengo 16º 45 pts, Portuguesa 17º 44 (ajuste -4); Corrida pinta 17º-20º; banco, dados e site |
| SA-002 | aberto | corrigido | 2004: São Caetano 18º com 53 (77-24); Corinthians 5º ... Flamengo 17º; banco e site |
| SA-003 | aberto | aberto | Posições certas (São Caetano 4º, Paysandu 22º com 49), mas os bônus positivos do STJD não entram: São Caetano 71 (en 74), Inter 70 (72), Corinthians 57 (59), Juventude 50 (53), Fluminense 50 (52). No site o 4º tem 71 e o 5º 73. Causa provável: em futebol/oficial_serie_a.py o regex de adjust_points só lê número com '-', não com '+' |
| SA-004 | aberto | corrigido | 2005: Vasco 12º, Fortaleza 13º, Juventude 14º, Flamengo 15º; Paysandu 21º, Brasiliense 22º |
| SA-005 | aberto | corrigido | 2018: América-MG 17º 40, Sport 18º 39 (ajuste -3) |
| SA-006 | aberto | corrigido | 2010: Barueri 20º com 28 (ajuste -3) |
| SA-007 | aberto | corrigido | Robertão 1968: vice Internacional, 3º Vasco, 4º Palmeiras (dados e pódio no site) |
| SA-008 | aberto | nao-e-erro | Decisão do Guilherme: Bragantino 3º, Vasco 4º (como está no painel) |
| SA-009 | aberto | aberto | 1972 sem mudança: 11º Atlético-MG, 12º Ceará, 13º Flamengo (en e pt: Flamengo 12º); o agente 1 não tratou |
| SA-010 | aberto | corrigido | 2009 rodada 12: Flamengo 2-2 Botafogo (mando do Flamengo); returno Botafogo 0-1 Flamengo |
| SA-011 | aberto | corrigido | Final CBF 1987, ida: Guarani 1-1 Sport em 30/01/1988, com autores |
| SA-012 | aberto | corrigido | Quartas 2001: Fluminense 2-1 Ponte Preta; V/E/D batem (Flu 15-9-5, Ponte 13-8-7). Gols ainda 1-2 abaixo da en (Flu 48-33 x 49-34; Ponte 53-50 x 55-51): diferença pequena, sem causa achada |
| SA-013 | aberto | corrigido | 1959: desempate Ceará 2-1 ABC (Claudinho, Doca; Tiquinho), 36 jogos; Ceará 6 J 1-4-1, ABC 3 J. Efeito colateral no cartão Artilheiro: ver RV-004 |
| SA-014 | aberto | corrigido | 1999: SP x Botafogo e SP x Inter 0-1 'awd', placar de campo na observação; SP 13-1-12 45-35, Botafogo 8-2-11 23-37, Inter 7-3-11 18-26; coluna Pts não aparece (várias fases) |
| SA-015 | aberto | nao-e-erro | Decisão do Guilherme: soma de todos os jogos, com a posição oficial |
| SA-016 | aberto | aberto | Erro de dado (decisão): 1986 sem mudança (Criciúma 18 J, Treze e Central 16 J; Joinville 1-0 Sergipe por W.O.) |
| SA-017 | aberto | aberto | Erro de dado (decisão): 1979 Vasco 7-5-2, Central 5-6-5; 1984 Portuguesa 7-9-6, Botafogo 4-6-4; sem mudança |
| SA-018 | aberto | nao-e-erro | Decisão do Guilherme. Conferido: a coluna Pts some nas edições de várias fases (ex.: 1971, 1980, 1988, 1994, 1999, 2001, 2002) |
| SA-019 | aberto | aberto | Sem lista oficial de 1937-2002 no banco; o pedido está com a coleta |
| SA-020 | aberto | aberto | 2008 sem mudança: Keirrison e Washington 21, Kléber Pereira fora (sem lista oficial) |
| SA-021 | aberto | aberto | 2007 sem mudança: Josiel Da Rocha 21 (oficial 20) |
| SA-022 | aberto | aberto | 2016 sem mudança: Fred dividido (12 pelo Atlético-MG e 2 pelo Fluminense) |
| SA-023 | aberto | aberto | Nomes sem mudança (Josiel Da Rocha, Fernandao, Andre Felipe, Luciano da Rocha Neves, Alerrandro Barra Mansa...) |
| SA-024 | aberto | aberto | Só 1999 tem resultado_especial (2 jogos 'awd'). 2005 (11 jogos refeitos; Brasiliense 0-1 Vasco sem marca) e 2016 (379 jogos) seguem sem aviso: nota vazia |
| SA-025 | aberto | aberto | Sem mudança: 1996 com 24 jogos sem data (Santos 2-0 Portuguesa, obs. 'Sep 18'); 1997 Vasco 2-0 Atlético-MG ainda em 05/07, obs. 'Nov 4' |
| SA-026 | aberto | corrigido | Faixas por ano (Wikipédia en): 2004 1º-4º Libertadores e 5º-9º Sul-Americana; 2013 vagas de copa no 8º e 16º; 2018 2º-8º e 9º-14º |
| SA-027 | aberto | corrigido | 2000 chamado 'Copa João Havelange' no seletor, no resumo e no pódio; ainda sem nota sobre os clubes dos módulos Amarelo e Branco |
| SA-028 | aberto | corrigido | 1987: fase 'Final Copa União', com acento |
| SA-029 | aberto | corrigido | Flamengo: 'Mais temporadas seguidas 59, de 1967 a 2025' (site) |
| SA-030 | aberto | corrigido | Em 420 px de verdade (site num iframe de 420 px) a página cabe. O Chrome sem janela com --window-size=420 desenha a 504 px: o corte visto na 1ª rodada vinha do método |
| SB-001 | aberto | corrigido | 1999: vice Santa Cruz, 3º Bahia, 4º Vila Nova-GO (site) |
| SB-002 | aberto | corrigido | 2001: vice Figueirense; jogo de 22/12 Figueirense 1-0 Caxias 'awd'. Mas a correção pegou também o jogo da 1ª fase (19/08): ver RV-001 |
| SB-003 | aberto | corrigido | 2001: Joinville 9º, Fortaleza 10º; os 4 da repescagem nas 4 últimas posições (25º-28º) |
| SB-004 | aberto | corrigido | 2004: vice Fortaleza, 3º Avaí, 4º Bahia |
| SB-005 | aberto | corrigido | 2009: Juventude 17º com 44 (12V 8E, sem ajuste); América-RN 16º; nenhuma posição repetida |
| SB-006 | aberto | corrigido | 7 repetidos fora: final de 1971 com 3 jogos (76 jogos e 179 gols na edição), 1981, 1990, 1992 e 1994; J de Paraná e Vitória 30, Sport 24, Guarani e Anapolina 15, Desportiva e Americano 18 |
| SB-007 | aberto | corrigido | 1998: Volta Redonda 0-2 Santa Cruz, 'wo' |
| SB-008 | aberto | corrigido | 1994: Desportiva-ES 1-0 CRB |
| SB-009 | aberto | corrigido | 2006: Ituano 1-1 Vila Nova-GO; Ituano 49-48; 1.090 gols |
| SB-010 | aberto | corrigido | 2008: Fortaleza 2-1 Criciúma; Fortaleza 56-56, Criciúma 40-54 |
| SB-011 | aberto | corrigido | 2013: gols contra do lado certo em 3 jogos; América-RN 2-2 Oeste ficou sem autores; nenhum lado passa do placar na Série B |
| SB-012 | aberto | corrigido | Cartão e sub-aba usam a lista oficial (1999 Uéslei 25, 2002 Vinícius 22, 2003 Vágner Love 19, 2006 Vanderlei 21, 1980 Osmarzinho 12). 1971 e 1988-1990 seguem parciais por falta de lista (SB-013, RV-004) |
| SB-013 | aberto | aberto | Tabela artilheiro sem 1971, 1988, 1989 e 1990; 2004 Rinaldo 13 e Kuki 13; 2016 'Bil' |
| SB-014 | aberto | corrigido | Pts com o ajuste (2014 América-MG 61, 2020 Cruzeiro 49, 2007 Marília -6, 2006 Guarani -3, 2011 Salgueiro -3). Punições ainda sem nota. A posição de 2014 ficou errada: ver RV-002 |
| SB-015 | aberto | corrigido | classificacao_final: 2007 Ituano 8-9-21; 2008 Juventude 51-48, 56 pts, ajuste 0; 2009 Duque de Caxias GC 55 |
| SB-016 | aberto | corrigido | Decisão aplicada: Brusque 2021 com 48 pts, 13º, ajuste 0 |
| SB-017 | aberto | aberto | 1971, 1985, 1994, 1997 e 1998 sem jogos sem data nem dezenas de jogos na mesma data. Mas 1991 ganhou as datas do ogol: 329 de 420 jogos comparáveis diferem da Wikipédia pt, com 13 jogos em datas impossíveis (RV-003) |
| SB-018 | aberto | aberto | Quadrangulares como 'grupos', 'Repescagem do rebaixamento' e 'Jogo final' ok. Falta: 2002 'Semifinal -finals' (site, Resumo) e os grupos de 2001 'North-Northeastern Group' e 'South-Southeastern Group' |
| SB-019 | aberto | corrigido | Cartão do clube virou 'Maior artilheiro', com os anos do jogador |
| SB-020 | aberto | corrigido | Guaratinguetá 2010-2013 seguido; 2011 'já estava' e 'ficou' (site, Participantes) |
| SB-021 | aberto | corrigido | Cabe em 420 px (iframe); ver SA-030 |
| SC-006 | aberto | corrigido | Só acesso oficial: 1981 Olaria, 1988 União São João, 1990 Atlético-GO (antes 4, 27 e 22). Os 2 últimos são campeões; a en diz 'promoted: none' e também 'originalmente promovidos' (dado do SC-005, coleta) |
| SC-024 | aberto | corrigido | Artilharia e cartão com a lista oficial (2006 Sorato 16, 2007 Túlio 27, 2012 Dênis Marques 11, 2008 Marcão 25, 2025 Iago Teles e Jonas Toró 8) |
| SC-025 | aberto | corrigido | Campeões invictos: Vila Nova-GO 1996 e Sampaio Corrêa 1997 |
| SC-026 | aberto | corrigido | Cabe em 420 px (iframe); ver SA-030 |
| SD-019 | aberto | corrigido | Lista oficial: 2009 Michel 10, 2010 Danilo Pitbull 11, 2012 Nino Guerreiro 13, 2020 Wallace Pernambucano e Zé Love 12, 2021 Gabriel Santos 13, 2023 Eron 14 |
| SD-020 | aberto | corrigido | Cabe em 420 px (iframe); ver SA-030 |
| CB-009 | aberto | corrigido | Pênaltis no placar da sub-aba Jogos ('pên. 1 × 4'), site 2025 |
| CB-012 | aberto | corrigido | Lista oficial: 2013 Hernane 8, 2016 Marinho 6, 2005 Fred 15, 1989 Gérson 7 |
| CB-013 | aberto | aberto | Resumo sem Pts, sem lanterna e sem melhor mandante/visitante, cartão 'Fases' e sub-aba Corrida escondida (site 2025). Falta: História > Pontuação histórica continua (pontos por vitória numa copa) |
| CB-016 | aberto | corrigido | Cabe em 420 px (iframe); ver SA-030 |
| CL-013 | aberto | corrigido | Decisão aplicada: um cadastro 'Guaratinguetá', com 'Americana' nos nomes de fonte; Série B 2010-2013 seguida |
| CL-014 | aberto | corrigido | Decisão aplicada: 'J.Malucelli' com 'Malutrom' nos nomes de fonte; Série B 2001 e Copa 2001 no mesmo cadastro |
| CL-015 | aberto | corrigido | Decisão aplicada: 'Grêmio Maringá' com a Série A 1964-1965; 'Maringá' (2010) à parte |
| CL-016 | aberto | corrigido | Decisão aplicada: 'Ferroviário do Recife', cidade Recife, sem 'Ferroviário do Cabo', com escudo próprio |
| CL-017 | aberto | corrigido | Potiguar com escudo próprio (ACD Potiguar), diferente do ABC |
| CL-018 | aberto | corrigido | América-CE sem escudo (não usa mais o do América-RN) |
| CL-019 | aberto | corrigido | Desportiva-ES com o escudo grená da Desportiva Ferroviária |
| CL-020 | aberto | corrigido | Estrela do Mar-PB sem escudo; a cidade vazia segue no CL-029 |
| CL-021 | aberto | corrigido | Tiradentes-PI com o escudo da SE Tiradentes (Teresina) |
| CL-022 | aberto | corrigido | Água Verde sem escudo (não usa mais o do Pinheiros) |
| CL-023 | aberto | aberto | O escudo errado saiu; o nome 'Rive A.C.' (era Espírito Santo FC em 2016-2018) continua, com a coleta |
| CL-024 | aberto | aberto | Ferroviário do Recife ganhou escudo; seguem sem escudo Oeste, União Bandeirante (Wikimedia), Central-RJ, Rodoviária e Serrano |
| CL-025 | aberto | aberto | 'Brasília EC' sem mudança (com a coleta) |
| CL-026 | aberto | nao-e-erro | Decisão do Guilherme: os 25 nomes ficam; sufixo só para clube novo com homônimo |
| CL-029 | aberto | aberto | 37 clubes das 5 competições ainda sem cidade (eram 42), ex.: Bonsucesso, Santa Cruz-SE, Estrela do Mar-PB, América-CE, Central-RJ |
| CL-030 | aberto | corrigido | Novorizontino (2010) só com nomes de 2020-2025; 1989-1999 no GE Novorizontino |
| TL-001 | aberto | corrigido | O painel não repete 'Grupo' quando o nome já começa por 'Grupo' (index.html); a varredura ainda acha 'Grupo A' no banco, o que é esperado |
| TL-002 | aberto | aberto | Série A: 2009, 2010 e 1977 zeraram; 1999 caiu de 40 para 12 jogos, 1997 de 65 para 37, 1998 de 14 para 8; 2008 segue com 13, e 1963, 1980, 1989, 1991, 1993, 1994 e 1995 sem mudança |
| TL-003 | aberto | aberto | Série B: 2009 (111), 1999, 1982 e 1988 zeraram; seguem 1981 (3), 1989 (9), 1990 (7), 1991 (13), 1997 (2) e 1998 (2); parte dos de 1990-1991 nasceu das datas do ogol (RV-003) |

## Regressões (achados novos)

| id | competição | ano | gravidade | o que |
|---|---|---|---|---|
| RV-001 | Série B | 2001 | média | A correção do SB-002 pegou também Figueirense x Caxias da 1ª fase (19/08): virou 1-0 "awd" (era 3-1, RSSSF). A pt confirma o 3-1 (Figueirense 61-49, Caxias 53-45; o painel mostra 59-48 e 52-43). Causa: `CORRECOES` em `serie_b/importar.py` sem a fase. |
| RV-002 | Série B | 2014 | alta | América-MG em 3º com 61 pts, acima de Vasco (63) e Avaí (62); no pódio e com o Avaí "subindo" em 5º. Na 1ª rodada era 5º. A ordem calculada ignora a punição de -6. |
| RV-003 | Série B | 1980, 1990, 1991 | média | Datas novas do ogol: semifinais de 1980 em abril (pt: 4 e 7 de maio); 1990, 4ª rodada do Grupo D em agosto, antes da 1ª rodada (pt: 04/09 e 08/09); 1991: 329 de 420 jogos com data diferente da pt e 6 conflitos novos (Joinville 2 jogos em 03/03 etc.). |
| RV-004 | Séries A, B e C | A 1959; B 1971, 1988-1990; C 1988 | baixa | Cartão "Artilheiro" do Resumo mostra artilharia parcial sem aviso. Novo desde o SA-013: 1959 "Claudinho, 1 gol" (oficial Léo Briglia, Bahia, 8). |
| RV-005 | Copa do Brasil | 2025 | baixa | Em 420 px, nome longo do mandante na sub-aba Jogos aparece cortado no começo ("ta Cruz de Natal", "io Raimundo-RR"). |

Fora do escopo (só registro): o "Independencia" do `uru-1` (1914-1915) usa o mesmo arquivo de escudo do Independência-AC
(`escudos/independencia.webp`), por causa do mesmo nome sem acento. O escudo do clube do Acre está certo.

## Varreduras e totais contra a 1ª rodada

- **Varredura de tela** (`revisao/RV/varredura.py`, cópia do original; saída em `SCRATCH/RV/varredura_saida.txt`): de 646 linhas para 191.
  Sumiram todos os "fase em inglês", "pódio x final", "jogo repetido", "clube contra ele mesmo", "posição repetida" e quase todos os
  "semifinalista fora do top 4". Sobraram: "Grupo A" no banco (esperado, o painel já não repete), Série A 1961 e Série B 2001 com fase
  fora de ordem (já existiam), Série A 1987 semifinalistas em 5º e 6º (já existia; é a Copa União) e um novo: **Série B 1980, semifinal
  antes da 3ª fase** (RV-003).
- **Datas repetidas** (`revisao/RV/datas_repetidas.py`, só as 5 competições; `SCRATCH/RV/datas_saida.txt`): de 34 edições para 18.
  Série A: 2009, 2010 e 1977 zeraram; 1997 37, 1999 12, 1998 8, 2008 13 (sem mudança). Série B: 2009, 1999, 1982, 1988, 1971, 1992,
  1994 zeraram; ficam 1981 (3), 1989 (9), 1990 (7), 1991 (13), 1997 (2), 1998 (2). Série C: só 1988 (3). Copa: zerou.
- **Campeões** (`revisao/RV/totais.py`, painel do commit 04cb286 x atual): nenhum campeão mudou nas 5 competições.
  Vices que mudaram são os dos achados: A 1968; B 1999, 2001, 2004; C 1999, 2001-2003, 2005, 2006, 2009, 2020; D 2010, 2020;
  Copa 1989, 1993-1997, 2012, 2014, 2025. O 3º da Série B 2014 mudou de Vasco para América-MG (RV-002).
- **Jogos por edição:** Série A 21.468 → 21.469 (1959 +1, desempate); gols mudaram em 1987 (+2), 1999 (-9, STJD) e 2001 (+1).
  Série B 13.094 → 13.088 jogos com placar (−7 repetidos, +1 jogo de 2001 que voltou a ter placar); gols de 2001 −2 por causa do RV-001.
  Série C 7.912 → 7.907 (2008 −2, 2011 −3); Série D 5.422 igual (2024 +5 gols); Copa 4.011 → 4.009 (2007 −1, 2019 −1).
  Todas as mudanças batem com achados corrigidos, menos a de 2001 na Série B.
- **Ordem por pontos** (`revisao/RV/ordem_pts.py`, edições de fase única): só 2 casos de clube com menos pontos acima de outro com mais:
  Série A 2003 (SA-003) e Série B 2014 (RV-002).

## Achados da coleta que já aparecem corrigidos (não mudei a situação)

Olhada rápida no banco e no site (`revisao/RV/coleta.py`), sem conferir com fonte:
- **Série C:** SC-002 (vices das 8 edições), SC-003 (3º mudou em 14 edições), SC-004 (rebaixados marcados), SC-005 (sem acesso falso em
  1981, 1988 e 1990; São Raimundo em 1999), SC-007 (1988 com 3 pontos), SC-008, SC-009 e CL-001 (sem clube contra ele mesmo), SC-010
  (2008 com 386 jogos), SC-011, SC-012, SC-013 (2011 com 106), SC-015, SC-017, SC-019, SC-020, SC-022, SC-023.
- **Série D:** SD-002, SD-003, SD-004 a SD-009 (fases de 2018 e 2020-2022 com grupos e nomes em português), SD-010, SD-012, SD-013,
  SD-014, SD-015, SD-016, SD-017, SD-018.
- **Copa do Brasil:** CB-001, CB-002, CB-003, CB-004, CB-006, CB-008 (218 jogos com pênaltis), CB-010, CB-011, CB-014, CB-015;
  CB-007 em parte (2007, 2019 e 2021 certos; 1999 ainda com 116 jogos).
- **Clubes e outros:** CL-002, CL-003, CL-004, CL-031, TL-004.
- **Ainda não:** SC-001 e SD-001 (2026), SD-011 (datas da semifinal de 2013), CL-005 a CL-012, CL-027 e CL-028.

## Fontes

- Wikipédia en: https://en.wikipedia.org/wiki/2003_Campeonato_Brasileiro_S%C3%A9rie_A (adjust_points), 2004, 2005, 2010, 2013, 2018
  (cópias em `data/serie_a/wikipedia/en_<ano>.txt`); https://en.wikipedia.org/wiki/List_of_Brazilian_football_champions (1959).
- Wikipédia pt: Série B 1980, 1990, 1991, 2001 e 2014 (`data/cache/revisao/SB/`), Série C 1988 e 1990 (`data/coleta/bra-serie-c/wikipedia/`).
- RSSSF Brasil: https://rsssfbrasil.com/tablesae/br2001l2.htm (via `data/serie_b/csv/serie_b_2001_partidas.csv` no commit 04cb286).
- Site: https://clubeanalitico.pages.dev/?c=<slug>#... e https://clubeanalitico.pages.dev/dados/<slug>.js (cópias em `data/cache/revisao/RV/site/`).
