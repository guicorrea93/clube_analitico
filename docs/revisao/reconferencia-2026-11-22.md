# Reconferência dos achados corrigidos depois de 21/11

Revisor RC · 22/11/2026 · saídas em `SCRATCH/reconferencia_RC.csv`, `SCRATCH/achados_RC.csv` e `SCRATCH/sugestoes_RC.csv` · scripts em `revisao/RC/`.

**Resumo.** Reconferi 116 achados que a coleta Brasil, a coleta Europa e o agente 1 dão como corrigidos ou decididos: 99 corrigidos, 15 abertos e 2 `nao-e-erro` (CL-027 por decisão, ES-002 por prova).
Os 14 de gravidade alta reconferidos estão resolvidos e no ar (SC-002, SC-004, SD-001, SD-002, SD-003, CB-001, CB-002, CB-003, CL-001, RV-002, SA-003, UY-002, EN-001 corrigidos; ES-002 `nao-e-erro`); os abertos são médios e baixos (datas da Série B, um placar e um jogo da Copa, nomes, textos do painel).
Regressões: datas da Série B 1990, 1991 e 1998 pioraram (RC-001); campeões, vices, 3º e totais das 10 competições revisadas só mudaram onde houve correção. Achados novos: RC-001 a RC-005.

## Como foi feito

- **Pacotes** `data/coleta/<slug>/pacote/` (C, D, Copa, eng-1, esp-1), **banco** (cópia de `db/futebol.db` de 22/11 09:13 no scratchpad, só leitura) e **site** (`https://clubeanalitico.pages.dev/dados/<slug>.js` baixados em `data/cache/revisao/RC/site/`). O site é igual ao arquivo local em A, B, C, D, Copa, arg-1 e uru-1; em bra-sp-1, eng-1 e esp-1 o site é a versão do commit 3b41c77 e o local já tem trabalho novo do agente 1 (não publicado).
- Scripts: `revisao/RC/brasil.py` (SC, SD, CB, CL, TL-004), `painel.py` (agente 1), `europa.py` (EN, ES), `totais.py` (campeões e totais x commit 2dbc105, o painel revisado na 2ª rodada), `varredura.py` e `datas_repetidas.py` (cópias com todas as competições), `cmp_varredura.py`, `datas_pt.py` (cópia do RV) e `cb/confrontos.py` (cópia do CB, contra as chaves da Wikipédia pt). Prints do site (`tela.sh`, `tela_copia.sh`, que abre uma cópia do site e clica na parte 'Campeões' das curiosidades) em `SCRATCH/RC/telas/`.

## Tabela

| id | antes | agora | no ar | nota |
|---|---|---|---|---|
| SC-001 | aberto | corrigido | sim | Pacote, banco e site com a Série C 2026: 216 jogos, 20 clubes, Maringá campeão e Ferroviária-SP vice; acesso de Ferroviária-SP, Inter de Limeira, Maringá e Santa Cruz; rebaixados Confiança e Itabaiana. |
| SC-002 | aberto | corrigido | sim | Vices no pacote, no banco e no site: 1999 São Raimundo, 2001 Mogi Mirim, 2002 Marília, 2003 Santo André, 2005 América-RN, 2006 Vitória, 2009 ASA, 2020 Remo. |
| SC-003 | aberto | corrigido | sim | 3º das 13 edições bate: 1992 Nacional-AM, 2001 Guarany, 2002/2005/2006/2011 Ipatinga, 2003 Botafogo-PB, 2007 Vila Nova-GO, 2008 Campinense, 2009 Guaratinguetá, 2020 Londrina, 2023 Operário-PR, 2024 Ferroviária-SP; 2025 4º São Bernardo. Do 5º para baixo a ordem segue a regra da coleta (2025: 5º Guarani, a pt tem Caxias): isso fica no SC-018. |
| SC-004 | aberto | corrigido | sim | Rebaixados de 2009, 2013 e 2016-2021 iguais à lista da fonte no pacote e no banco (2013 com Ipatinga e Rio Branco-AC). |
| SC-005 | aberto | corrigido | sim | Pacote e banco: nenhum 'acesso' em 1981 (só o campeão Olaria), 1988, 1990 e 1992; 1999 São Raimundo com acesso. O site lista o campeão como 'subiu' (1988 União São João, 1990 Atlético-GO, 1992 Tuna Luso), regra do painel já aceita no SC-006. |
| SC-007 | aberto | corrigido | sim | 1988 com pontos_vitoria 3 no pacote, no banco e no site; Marcílio Dias 4º e Tiradentes-PI 5º. O ABC está em 13º (pt: 7º): é a ordem dos eliminados, que fica no SC-018. |
| SC-008 | aberto | corrigido | sim | 1988, grupo 18: Ferroviária-SP com 10 jogos (6 na 2ª fase) e Desportiva-ES com 12, no pacote e no banco. |
| SC-009 | aberto | corrigido | sim | 2007, grupo 17: os 6 jogos do Imperatriz com o clube certo, sem 'Tuna Luso x Tuna Luso' nem jogo duplicado; banco: Imperatriz 12 jogos (-12), Tuna Luso 18 jogos. |
| SC-010 | aberto | corrigido | sim | 2008 com 386 jogos (pacote, banco e site); o grupo 15 tem um jogo Inter de Santa Maria x Engenheiro Beltrão por turno. |
| SC-011 | aberto | corrigido | sim | 2004: Portuguesa Santista 0x1 Atlético Sorocaba (08/08), grupo 13, no pacote e no banco. |
| SC-012 | aberto | corrigido | sim | 2003: um clube só (Boa Esporte) com os 8 jogos; 'Ituiutabana' não aparece. |
| SC-013 | aberto | corrigido | sim | 2011: os 3 jogos do Rio Branco-AC na 2ª fase saíram; Ipatinga 3º e América-RN 4º. A edição tem 106 jogos (pt: 105), diferença que fica no SC-021. |
| SC-014 | aberto | corrigido | sim | 1988 Inter de Santa Maria 2x0 Figueirense; 1992 Rio Branco-MG 2x1 São Bento, Nacional-AM 1x0 Ji-Paraná, Macapá 0x2 Nacional-AM, Nacional-AM 3x0 Auto Esporte; 2003 Atlético Roraima 1x2 Rio Branco-AC (pacote e banco). |
| SC-015 | aberto | corrigido | sim | 1995: Itumbiara 1x0 Gama com resultado_especial awd e o placar de campo (1-2) na observação. |
| SC-016 | aberto | aberto | n/a | A coleta manteve os placares da RSSSF e do ogol, que concordam entre si; só a Wikipédia diverge. Sem prova nova nem decisão do Guilherme. Amostra igual à da 1ª rodada (1981 Izabelense 1x1 Manchete, 1990 Estudantes 1x1 Campinense, 2008 Rio Branco-AC 2x0 Fast-AM, 2013 CRB 2x0 Luverdense). |
| SC-017 | aberto | corrigido | sim | Punições no pacote e no banco: 2005 Nacional-PB -6; 2006 Ananindeua, Ceilândia, Ulbra-RO e Ypiranga-PE -6, Estrela do Norte -18; 2007 Imperatriz -12 e Nacional-PB -6. |
| SC-018 | aberto | aberto | não | A coleta manteve a regra (fase alcançada, posição no grupo dessa fase, campanha). Casos vistos agora: 1988 ABC 13º (pt 7º); 2025 5º Guarani (pt 5º Caxias, 6º Brusque, 7º Guarani); a mesma regra põe na Série D 2012 o Comercial-PI em 29º (pt 34º) e 2014 o River-PI em 24º (pt 27º). |
| SC-019 | aberto | corrigido | sim | 2003 'Quinta fase' (ordem 5, antes da Fase final); 1992 Fluminense-BA x Matsubara na 'Segunda fase / Grupo B'; 2020 Vila Nova x Remo na 'Final'. Nenhum nome de fase em inglês no pacote. |
| SC-020 | aberto | corrigido | sim | Nenhum confronto de ida e volta com as duas partidas na mesma data nos pacotes da C, da D e da Copa. |
| SC-021 | aberto | aberto | n/a | Sem mudança e sem prova nova: jogos 1995 384, 1999 226, 2011 106, 2012 194 (infobox pt 383, 224, 105, 195); gols 2001 1.124, 2002 595, 2008 1.068, 2011 289. A coleta deixou em dúvida. |
| SC-022 | aberto | corrigido | sim | 1998: Kléber Pereira (Moto Club) 25 gols no pacote e no site. |
| SC-023 | aberto | corrigido | sim | artilheiros.csv 2016 'Jones Carioca'; nos gols: Jones Carioca, Assisinho, Leandrão e Júlio César (nenhuma grafia antiga). |
| SD-001 | aberto | corrigido | sim | Série D 2026 no pacote, no banco e no site: 610 jogos, 96 clubes, Uberlândia campeão e ASA vice; acessos Uberlândia, ASA, Gama, ABC, Nacional-AM e Goiatuba EC. |
| SD-002 | aberto | corrigido | sim | 2020: Mirassol, Floresta-CE (vice), Novorizontino, Altos, América-RN, Aparecidense nas 6 primeiras posições (pacote, banco e site). |
| SD-003 | aberto | corrigido | sim | 2021: 3º ABC, 4º Atlético Cearense, 5º Ferroviária-SP, 6º América-RN (pacote, banco e site). |
| SD-004 | aberto | corrigido | sim | 2021: América-RN x Campinense nas Quartas e Atlético Cearense x Campinense na Semifinal; nenhum jogo de mata-mata no grupo A03. |
| SD-005 | aberto | corrigido | sim | 2020: Fase preliminar (8), Primeira fase com 8 grupos (448), Segunda fase (32), oitavas (16), quartas (8), semifinal (4) e final (2). |
| SD-006 | aberto | corrigido | sim | 2022: Primeira fase com 8 grupos (448 jogos), depois o mata-mata. |
| SD-007 | aberto | corrigido | sim | 2016, 2017 e 2018: Primeira fase com 17 grupos e 204 jogos, todos com grupo (o 4 de Julho e o 7 de Setembro-MS nos seus grupos). |
| SD-008 | aberto | corrigido | sim | 2011: Final Tupi 1x0 e 2x0 Santa Cruz; 2013: Final Juventude 2x1 e Botafogo-PB 2x0; as duas na fase 'Final', separadas da Semifinal. |
| SD-009 | aberto | corrigido | sim | Nenhum nome de fase em inglês; as 23 observações estão em português (ex.: 'prorrogação 0-0', 'jogo em Macapá-AP'). |
| SD-010 | aberto | corrigido | sim | 2024: Princesa 3x3 Manaus FC (11/05); gols da edição no site 1.143, como a Wikipédia. |
| SD-011 | aberto | aberto | n/a | A coleta manteve 06/09 e 29/09/2013 (ogol e RSSSF dão essas datas) para a semifinal Botafogo-PB x Salgueiro; as quartas de 15 e 22/09 seguem depois da ida da semifinal. Falta uma terceira fonte. |
| SD-012 | aberto | corrigido | sim | Final de 2016: CSA 0x0 Volta Redonda em 25/09 (pacote e banco). |
| SD-013 | aberto | corrigido | não | Pacote: os 3 W.O. de 2014 com resultado_especial awd e observação. O painel ainda soma os 9 gols (2014: 200 jogos e 515 gols; a Wikipédia dá 199 e 503): ver RC-005 (banco-painel). |
| SD-014 | aberto | corrigido | sim | Pontos com a punição iguais à fonte: 2009 Araguaia 19 e Naviraiense -2; 2010 América-AM 13; 2012 Comercial-PI 5 e Santos-AP 4; 2013 Paragominas 11; 2014 River-PI 9 e Villa Nova-MG -9; 2015 Náutico-RR 4 e Santos-AP 7; 2019 Bahia de Feira 7. As posições de parte dos eliminados na 1ª fase diferem da pt (Comercial-PI 29º x 34º; River-PI 24º x 27º; Bahia de Feira 40º x 41º) pela regra de ordem do SC-018. |
| SD-015 | aberto | corrigido | sim | 2017: -3 no São Raimundo-PA (7 pts, 42º); São Raimundo-RR com 5 pts (49º; a pt diz 57º, regra do SC-018). |
| SD-016 | aberto | corrigido | sim | 2025: -3 no Maracanã (9 pts, 60º; pt 59º); Maricá com 20 pts, 31º. |
| SD-017 | aberto | corrigido | sim | 2025: acesso de Barra-SC, Santa Cruz, Inter de Limeira e Maranhão (Santa Cruz de Natal sem acesso); 2020: Floresta-CE vice. |
| SD-018 | aberto | corrigido | sim | Nenhum artilheiro com '- ' na frente, no pacote nem no banco. |
| CB-001 | aberto | corrigido | sim | Vices no pacote e no site: 1989 Sport, 1993 Grêmio, 1994 Ceará, 1995 Grêmio, 1996 Palmeiras, 1997 Flamengo, 2012 Coritiba, 2014 Cruzeiro, 2025 Vasco. |
| CB-002 | aberto | corrigido | sim | Nas 37 edições os 4 primeiros da classificação são os semifinalistas (conferido pelos jogos de Semifinal e Final do pacote). |
| CB-003 | aberto | corrigido | sim | Fases só em português (Fase preliminar, Primeira a Quarta fase, Oitavas, Quartas, Semifinal, Final); nenhuma Final com mais de 2 jogos; site 2019: 8 fases em ordem. |
| CB-004 | aberto | corrigido | sim | 2014 Treze 1x2 Vasco; 2015 Paysandu 2x0 Águia Negra; 2015 Tupi 1x2 Ceará (pacote e banco). |
| CB-005 | aberto | aberto | sim | 7 dos 8 corrigidos (1993, 1994, 2000 Fluminense 3x1, 2000 Nacional-AM 2x2 Rio Negro-AM, 2007, 2013, 2014) e 2002 São Raimundo x América-RN bate com a pt. Falta 1990, volta: pacote América-RN 1x0 Santa Cruz (27/06); pt e en dão 0x1 (Santa Cruz 3-1 e 1-0); a RSSSF ('3-1 0-1') e o ogol (jogo 652618) dão 1x0 para o América: fontes divididas. 1991 Remo x Vitória: pt 2-0 e 2-2, en e pacote 0-0 e 2-0 (infobox 132 gols x 128). |
| CB-006 | aberto | corrigido | sim | Finais: 2015 Santos 1x0 Palmeiras (25/11) e Palmeiras 2x1 Santos (02/12, pên. 4-3); 2016 Atlético-MG 1x3 Grêmio (23/11) e Grêmio 1x1 Atlético-MG (07/12). |
| CB-007 | aberto | aberto | parcial | 2007 com 115 jogos (Villa Nova-MG x Avaí na 2ª fase), 2019 com 120 (Aparecidense 2x0 Ponte Preta) e 2021 com Sergipe 0x0 Cuiabá e 92 clubes: corrigidos. Falta 1999: 116 jogos e 64 clubes, sem a preliminar Santa Cruz 1x0 Náutico (a coleta não pôs porque só a pt tem o jogo). |
| CB-008 | aberto | corrigido | sim | 218 jogos com pênaltis nos campos próprios; a comparação com as chaves da pt (cópia de revisao/CB/confrontos.py em revisao/RC/cb/) caiu de 124 'pênaltis faltando' para 0. Finais de 2015 (Palmeiras 4-3) e 2017 (Cruzeiro 5-3); 2021 Palmeiras 0x1 CRB, pên. 3-4. |
| CB-010 | aberto | corrigido | sim | 1990 Goiás x Flamengo em 07/11; finais de 2014 em 12/11 e 26/11 e de 2015 em 25/11 e 02/12, com a observação do motivo. |
| CB-011 | aberto | corrigido | sim | Artilheiros: 2007 Dênis Marques no Athletico-PR; 2018 Gabriel, Neilton e Rômulo (4); 2019 Pipico no Santa Cruz; 2023 Alef Manga, Lorran, Pedro e Tiquinho Soares (5); nenhum nome em maiúsculas. |
| CB-014 | aberto | corrigido | sim | Nenhum jogo da Copa com grupo, no pacote e no banco. |
| CB-015 | aberto | corrigido | sim | Saíram 'São Paulo lost 5 points...' (1996) e as datas soltas de 1999. Sobra 1 observação em inglês: 1998-0028 Botafogo 4x0 São Raimundo, "2nd leg abd at 4-0 to Botafogo in 72'" (traduzir no coleta/comum/observacao.py). |
| CL-001 | aberto | corrigido | sim | Mesmo caso do SC-009: os jogos do Imperatriz voltaram ao clube certo em 2007. |
| CL-002 | aberto | corrigido | sim | Série C 2002 com o Tubarão FC (1996-1998, 2001, 2002); o Atlético Tubarão só aparece de 2018 em diante. |
| CL-003 | aberto | corrigido | sim | Copa 2007: Operário-MT 0x5 Palmeiras, com o Operário FC Ltda (decisão do CL-007). |
| CL-004 | aberto | corrigido | sim | Série C 1995 com a SE Ariquemes (que tem também a Copa 1994); o cadastro 'Ariquemes' (FC, 1996) saiu do banco. |
| CL-005 | aberto | corrigido | sim | Decisão aplicada: 'São Gabriel' com a Série C 2002 e a Copa 2004; o 'EC São Gabriel' saiu do banco. |
| CL-006 | aberto | corrigido | sim | Decisão aplicada: 'Goiatuba EC' com Série B 1989 e 1994-1997, Série C 2003, Copa 1993 e Série D 2025-2026; o cadastro 'Goiatuba' saiu. |
| CL-007 | aberto | corrigido | parcial | Decisão aplicada nos pacotes e no banco: CEOV Operário (Série A 1968, 1979, 1984, 1986; B 1980, 1982, 1983, 1992; C 1994-1995; Copa 1995-1996 e 2015+), EC Operário-MT (C 1997, Copa 1998) e Operário-MT = Operário FC Ltda (C 2006, Copa 2003, 2006, 2007). Os escudos ficaram trocados: ver RC-002 (banco-painel). |
| CL-008 | aberto | corrigido | sim | Decisão aplicada: 'Lagarto EC' com Série B 1989 e Série C 1988 e 1990, sem escudo; 'Lagarto' (FC) com a Copa e a D recentes. |
| CL-009 | aberto | corrigido | sim | Decisão aplicada: 'AA Cabofriense' com Série B 1989 e Série C 1988; 'Cabofriense' (AD) com 2003 em diante. |
| CL-010 | aberto | corrigido | sim | Decisão aplicada no banco: 'Foz do Iguaçu EC' com a Série B 1989 (ainda sem UF e cidade, que entram no CL-029). |
| CL-011 | aberto | corrigido | sim | Decisão aplicada: 'EC Limoeiro' na Série C 1998 e 'Limoeiro' (AD) na de 2004. A cidade do EC Limoeiro está como 'Limoeiro Do Norte' (CL-028). |
| CL-012 | aberto | corrigido | sim | Decisão aplicada: Joaçaba EC e SE São Borja (1981) e Guarabira EC (2001), sem escudo; 'Joaçaba', 'São Borja' e 'Desportiva Guarabira' saíram do banco. O 3º de 1981 no site é 'SE São Borja'. |
| CL-027 | aberto | nao-e-erro | sim | Decisão do Guilherme (21/11): os nomes com sufixo '-UF' ficam como estão; o sufixo só é exigido para clube novo com homônimo. |
| CL-028 | aberto | aberto | não | Sem resposta da coleta. Seguem: Botafogo-DF com UF GO e cidade Novo Gama; AA Araguaia em Cuiabá; Alegrense com cidade 'Alegre - Espirito Santo'; grafias 'Teixeira De Freitas', 'Vitória De Santo Antão', 'Divinopolis', e também 'Rio De Janeiro', 'Rolim De Moura' e 'Limoeiro Do Norte'. |
| CL-031 | aberto | corrigido | sim | Matsubara no clubes.csv da C sem 'ogol:JMalucelli:1981'. |
| TL-004 | aberto | corrigido | sim | Nenhum confronto com ida e volta na mesma data na Copa (2001) nem na Série C (1988). |
| RV-001 | aberto | corrigido | sim | Série B 2001: Figueirense 3x1 Caxias na 1ª fase (19/08) sem awd; só o jogo de 22/12 é 1x0 awd. Site: Figueirense 61-49, Caxias 53-45. |
| RV-002 | aberto | corrigido | sim | Série B 2014: 3º Vasco 63, 4º Avaí 62, 5º América-MG 61 (-6), no banco e no site (pódio com Vasco em 3º). |
| RV-003 | aberto | aberto | n/a | 1980 corrigido (semifinais em 04 e 07/05). 1990 não: Moto Club 3x0 Treze segue em 04/08 e Remo 2x0 Ceará em 08/08 (pt 04/09 e 08/09), e 28 de 147 jogos casados com a pt têm outra data. 1991: as datas do ogol saíram (344 de 478 jogos sem data), mas sobram 46 jogos com clube 2 vezes no mesmo dia (eram 13 na 1ª rodada). Ver RC-001. O painel não mostra a data dos jogos. |
| RV-004 | aberto | corrigido | sim | Série A 1959: cartão 'Artilheiro 8 gols, Léo, Bahia'; Série B 1971: o cartão some e a sub-aba avisa 'Parcial: só 15% dos gols...'. |
| SA-003 | aberto | corrigido | sim | Série A 2003 no banco e no site: São Caetano 4º 74 (+3), Coritiba 5º 73, Internacional 6º 72 (+2), Corinthians 15º (+2), Juventude 18º (+3), Fluminense 19º (+2), Ponte Preta 21º (-1), Paysandu 22º 49 (-8). |
| SA-019 | aberto | corrigido | sim | Lista oficial carregada (bra-serie-a-artilheiros): as 70 edições têm artilheiro (ex.: 1937 Paulista 8, 1977 Reinaldo 28, 1997 Edmundo 29). |
| SA-020 | aberto | corrigido | sim | 2008: Keirrison, Kléber Pereira e Washington com 21 na lista oficial. A lista 'Gols registrados jogo a jogo' abaixo ainda tem 'Kleber' 18 (dado da tabela gol: SA-023). |
| SA-021 | aberto | corrigido | sim | 2007: oficial Josiel 20 (cartão e sub-aba). A lista jogo a jogo segue com 'Josiel Da Rocha' 21 (tabela gol: SA-023). |
| SA-022 | aberto | corrigido | sim | 2016: Diego Souza, Fred (Atlético-MG) e William Pottker com 14 na lista oficial. |
| SA-023 | aberto | aberto | sim | A lista oficial usa os nomes de jogo (Josiel, Luciano, Alerrandro). Os nomes da tabela gol continuam e aparecem em 'Gols registrados jogo a jogo' e em Por clube: 'Josiel Da Rocha' (23 gols), 'Fernandao' (25), 'Andre Felipe' (31), 'Luciano da Rocha Neves' (85), 'Alerrandro Barra Mansa Realino de Souza' (33), 'Kleber' (68). |
| SA-024 | aberto | aberto | parcial | Avisos no Resumo de 2005 (11 jogos anulados e refeitos) e de 2016 (Chapecoense x Atlético-MG não disputado). Falta a marca awd e a observação em Brasiliense 0x1 Vasco (24/04/2005; em campo 2-2): só 1999 tem resultado_especial na Série A. |
| SB-018 | aberto | corrigido | sim | Fases em português: 2002 'Semifinal', 2001 'Grupo Sul-Sudeste' e 'Grupo Norte-Nordeste', 'Repescagem do rebaixamento'; quadrangulares de 1985, 1988, 1999 e 2001 como 'grupos'. |
| CB-013 | aberto | corrigido | sim | Na Copa, 'Pontuação histórica' saiu do menu da História. A rota direta #historia/pontos ainda abre a tela com pontos (Flamengo 460), mas não há caminho para ela. |
| SP-025 | aberto | corrigido | sim | Paulista: a sub-aba avisa 'Parcial: só 0% dos gols desta edição têm autor registrado' (1951) antes da lista; o mesmo nas outras edições sem lista oficial. |
| AR-036 | aberto | corrigido | sim | Tabela do site igual à classificacao_final do banco nas 3.775 linhas (0 diferenças); ex.: 1895 Lomas Academicals 8 jogos; 2006/07 Apertura Estudiantes 19 j 14 V. |
| AR-037 | aberto | corrigido | sim | Por clube > River Plate: o cartão 'Maior artilheiro' some quando os gols com autor são poucos (cobertura 26%). |
| AR-038 | aberto | corrigido | sim | Por clube > Jogos do River abre em '2025 · Clausura', com os jogos. |
| AR-039 | aberto | corrigido | sim | Não foi pedido de novo, mas conferido: o dados/arg-1.js do site é igual ao local (selo 'Argentina · 1ª divisão · 1891 a 2025'). |
| AR-041 | aberto | aberto | parcial | Temporadas agora como '96/97' e '16/17'. Falta: o torneio só aparece na dica (selos '1936', '1975', '1979' e '96/97' repetidos sem Metropolitano/Nacional/Apertura/Clausura); o seletor ainda diz '2018/19 · Argentino'. |
| AR-042 | aberto | corrigido | sim | 2025 Liga: cartões '— Jogos: só a tabela final desta edição', '— Gols', '— Maior goleada: sem jogos nesta edição'. |
| UY-002 | aberto | corrigido | sim | 1948 sem campeão no site (nota 'campeonato abandonado na 10ª rodada'); Nacional com 50 títulos na Corrida e no Pódio. O vice Peñarol de 1948 continua (UY-003, coleta). |
| UY-009 | aberto | corrigido | sim | Pódio por clube com '05/06', '09/10', '12/13'... e '2005' separado de '05/06'; a curiosidade de títulos duplos não aparece mais. |
| UY-025 | aberto | aberto | parcial | Cartão do topo: '12.367 Jogos em 81 edições com jogos'. Falta o texto de Jogos e vitórias e de Gols, que ainda diz 'todas as partidas, de 1900 a hoje (12.367 jogos)'. |
| ES-003 | aberto | corrigido | sim | 1979/80 no site: AD Almería 41 GP e CD Málaga 58 GC (-3), como a tabela oficial. |
| ES-007 | aberto | corrigido | sim | 2003/04: oficial 'Ronaldo 24' e, abaixo, 'Gols registrados jogo a jogo' com Ronaldo 24, Júlio Baptista 20, Fernando Torres 19... |
| ES-008 | aberto | corrigido | sim | Título mais apertado com os pontos reais: 8 títulos empatados em pontos (1930/31, 1946/47, 1959/60, 1970/71, 1980/81, 1983/84 Athletic x Real Madrid, 1993/94, 2006/07). |
| ES-009 | aberto | corrigido | sim | Maior vantagem sobre o vice: Barcelona 15 (2012/13, 100 x 85). |
| ES-010 | aberto | corrigido | sim | O cartão 'Títulos por estado' não aparece no Espanhol. |
| ES-014 | aberto | aberto | parcial | Pódio por clube com '31/32', '53/54'... e o selo '1928/29 a 2024/25'. Falta: Curiosidades 'Barcelona · 2012', 'Real Madrid · 2011' e a Corrida dos títulos '2024' seguem com o ano de início (o mesmo no Inglês: 'Manchester City · 2017'). |
| EN-008 | aberto | corrigido | sim | Participantes 1914/15: 'No ano seguinte' preenchido pela edição 1919/20 ('ficou'); 1946/47: 'Chegou' pela 1938/39 ('já estava'). Rebaixados e promovidos ainda com '—' (EN-009, não pedido). |
| EN-011 | aberto | corrigido | sim | No site: Título mais apertado com 1923/24, 1949/50, 1952/53, 1964/65, 1988/89 e 2011/12; maior vantagem Manchester City 19 (2017/18); melhor campanha Preston 90,9%. A versão local não publicada perde os anos antes de 1992/93: ver RC-003. |
| EN-012 | aberto | corrigido | sim | O cartão 'Títulos por estado' não aparece no Inglês. |
| EN-015 | aberto | corrigido | sim | Seletor e título com o nome de época: '1990/91 · Football League First Division', '1992/93 · FA Premier League', '2025/26 · Premier League'. |
| EN-001 | aberto | corrigido | sim | 2025/26 no pacote (127 edições, 51.330 jogos), no banco e no site: Arsenal campeão, Manchester City vice; rebaixados West Ham, Burnley e Wolverhampton; artilheiro Erling Haaland 27. |
| EN-002 | aberto | corrigido | sim | 1937/38: Tommy Lawton 28 (pacote, banco e site). |
| EN-003 | aberto | corrigido | sim | 1889/90: Jimmy Ross 24 (pacote, banco e site), com a fonte explicada. |
| EN-004 | aberto | aberto | n/a | A coleta manteve Albert Shepherd 26 (as fontes divergem: RSSSF e a página da temporada dão Walter White 26). Sem decisão. |
| EN-005 | aberto | corrigido | não visível | As 33 datas da lista do 11v11 estão no pacote; das 35 linhas DIF, uma é o placar do EN-006 e outra é Everton x Arsenal 2015/16, que o 11v11 casou com um amistoso (ficou de fora de propósito). O painel não mostra datas. |
| EN-006 | aberto | corrigido | sim | Wolverhampton 5x0 Everton (26/01/1889) no pacote, no banco e no site (Wolverhampton 51-37, Everton 35-47). |
| EN-007 | aberto | corrigido | não | Pacote e banco: as 94 temporadas sem rodadas fixas (até 1991/92 e 1994/95) com rodada vazia e sem classificacao_rodada (decisão do Guilherme). O site ainda é o anterior: 1990/91 com rodada em 370 jogos e Corrida. A versão local já está certa. |
| EN-016 | aberto | aberto | não | Os 12 jogos seguem sem nenhum gol com autor (ex.: 02/11/2014 Manchester City x Manchester United; 22/09/2013 o mesmo clássico). A coleta deixou para depois. |
| EN-017 | aberto | corrigido | n/a | clubes.csv e banco (clube_nome) com 'rsssf:Newton Heath' 1892-1893 no Manchester United. |
| EN-018 | aberto | corrigido | sim | Stoke City (1889/90) e Darwen (1891/92) sem 'rebaixado', com a observação 'não foi reeleito'. |
| ES-001 | aberto | corrigido | sim | 1935/36: Real Oviedo sem 'rebaixado' (observação da dispensa); Atlético de Madrid e Osasuna rebaixados (decisão do Guilherme); faixa da Corrida no 12º. |
| ES-002 | aberto | nao-e-erro | sim | Prova: a tabela final da Wikipédia es (1986-87) é 16º Osasuna, 17º Racing (descenso), 18º Cádiz (descenso planteado, salvo na liguilla); a liguilla não conta como jogo da Primera e está na observação da edição. A ordem do painel é a oficial. O painel não mostra essa observação (ES-011). |
| ES-004 | aberto | corrigido | sim | Faixa de rebaixamento nas posições de quem caiu: 1965/66 13º e 15º-16º; 1989/90 17º e 19º-20º; 1993/94 17º e 19º-20º; 1997/98 17º e 19º-20º; 2014/15 13º e 19º-20º (pacote e site). |
| ES-005 | aberto | corrigido | sim | Decisão do Guilherme (contagem oficial da LaLiga, Pichichi anotado na fonte): 1929/30 Gorostiza 20, 1934/35 Lángara 27, 1935/36 Lángara 28, 1954/55 Arza 28, 2003/04 Ronaldo 24. |
| ES-006 | aberto | corrigido | sim | esp-1: Nihat Kahveci 76, Fernando Morientes 42, Ismael Urzaiz 61, Rubén Navarro, Magno Mocelin, Raúl Molina, Sávio, Víctor Fernández e Salva Ballesta 43; nenhuma grafia antiga nos gols do esp-1. As mesmas grafias seguem no eng-1 e no fra-1: ver RC-004. |

## Regressões e achados novos

| id | competição | gravidade | quem corrige | o que |
|---|---|---|---|---|
| RC-001 | bra-serie-b (B 1990; B 1991; B 1998; A 1997) | media | banco-painel | Banco: clube com 2 jogos no mesmo dia aumentou desde a reconferência de 21/11: Série B 1990 de 7 para 34 jogos (ex.: 18/08/1990 XV de Piracicaba 1x1 Guarani, rodada 1, e Guarani 2x0 Rio Branco-AC, rodada 2; 01/09/1990 Catuense nas rodadas 3 e 4); 1991 de 13 para 46 (ex.: 03/02/1991 Ubiratan x Grêmio Maringá ida e volta; Joinvill... |
| RC-002 | bra-copa-do-brasil (Copa 1998, 2003, 2006, 2007; Série C 1997, 2006) | baixa | banco-painel | Depois da decisão do CL-007: 'Operário-MT' (Operário FC Ltda, hoje Várzea Grande EC; Copa 2003, 2006, 2007 e Série C 2006) usa o escudo do CEOV (painel/escudos/operario-mt.webp = o mesmo de ceov-operario.webp); 'EC Operário-MT' (EC Operário, 1996-2001; Série C 1997 e Copa 1998) usa o escudo do Várzea Grande EC (ogol 3373, em dat... |
| RC-003 | eng-1 (1888/89-1991/92) | baixa | banco-painel | painel/dados/eng-1.js local (22/11, ainda não publicado): 'Título mais apertado' só com Manchester City 2011/12 e 'pontos corridos, desde 1992' (CUR.campeoes.pc_desde 1992, pc20_desde 1995). No site (versão anterior) a lista tem 1923/24, 1949/50, 1952/53, 1964/65, 1988/89 e 2011/12, 'desde 1888'. Causa: depois do EN-007 o eng-1 ... |
| RC-004 | eng-1 (eng-1 2004/05-2005/06; fra-1 2002/03-2003/04, 2009/10) | baixa | coleta-europa | Banco (tabela gol): 'Fernando Sanchez Morientes' com 8 gols no eng-1 (Liverpool) e 11 no fra-1 (Monaco 10, Marseille 1); 'Bortolini Pimentel Savio' com 7 no fra-1 (Bordeaux). O ES-006 corrigiu só o esp-1 (NOMES_ESPN em coleta/esp-1/importar.py).... |
| RC-005 | bra-serie-d (2014) | baixa | banco-painel | Série D 2014: 200 jogos e 515 gols no Resumo e nos históricos; os 3 W.O. (Itaporã 0x3 Villa Nova-MG, Anapolina 3x0 Itaporã, Barueri 0x3 CEOV Operário), agora com resultado_especial awd no pacote (SD-013), seguem somando 9 gols.... |

- **Campeões, vices, 3º e totais** (`revisao/RC/totais.py`, painel do commit 2dbc105 x site): mudaram só Série B 2014 3º (Vasco, RV-002) e 2001 +3 gols (RV-001), Série C 1981 3º renomeado 'SE São Borja' (CL-012), Uruguaio 1948 sem campeão (UY-002), Inglês 1888/89 +1 gol (EN-006) e as edições novas (Série C e D 2026, Inglês 2025/26; Espanhol 2025/26 só no local). Nenhuma outra mudança em A, B, C, D, Copa, Paulista, Argentino, Uruguaio, Inglês e Espanhol.
- **Varredura de tela** (`revisao/RC/varredura.py`, todas as 19 competições do banco; saída `SCRATCH/RC/varredura_saida.txt`, 1.804 linhas): Paulista (131), Argentino (342), Uruguaio (133) e Espanhol (0) iguais às saídas da 2ª rodada; o Inglês não tem nenhuma linha. Nas 5 brasileiras (191 linhas em 21/11, 194 agora): Série A caiu de 62 para 16 linhas de 'clube 2 jogos no mesmo dia'; Série B subiu de 23 para 69 (RC-001); Série B 2001 segue com a fase fora de ordem (repescagem depois das quartas, real); Série D 2026 tem a Semifinal começando antes do fim da Repescagem (jogadas em paralelo; não é erro).
- **Datas repetidas** (`revisao/RC/datas_repetidas.py`): Série A 1997 de 37 para 3, 2008, 1980, 1993, 1995 e 1998 zeraram; Série B 1990 de 7 para 34, 1991 de 13 para 46, 1998 de 2 para 6 (RC-001).
- **Versão local não publicada:** o eng-1 local perde os títulos empatados antes de 1992/93 nas curiosidades (RC-003). Conferir antes de publicar.
- **Competições ainda não revisadas** (só para os revisores delas, sem achado aqui): a varredura acusa 'clube contra ele mesmo' em col-1 1971 (Independiente Santa Fe), 'campeão não é 1º' em par-1 1917, 1928, 1936 e 1991 (edições com tabela parcial), 'posição repetida' em bra-sp-2 1990, 1992 e 1993 (faixas da fonte, como o pacote avisa) e muitos 'clube 2 jogos no mesmo dia' (col-1 143, bra-sp-2 95, ecu-1 87, chi-1 86, per-1 85, par-1 84). O por-1 não está no banco (nome 'Sanjoanense' repetido; pedido em pedidos-europa.md).

## Fontes

- Site: https://clubeanalitico.pages.dev/?c=<slug>#... e https://clubeanalitico.pages.dev/dados/<slug>.js (cópias em `data/cache/revisao/RC/site/`).
- Wikipédia pt das Copas do Brasil (cache `data/cache/revisao/CB/`), da Série C (`data/coleta/bra-serie-c/wikipedia/pt_1988.txt`, `pt_2025.txt`) e da Série B 1980, 1990 e 1991 (`data/cache/revisao/SB/`).
- Wikipédia es: https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_de_Espa%C3%B1a_1986-87 (tabela final e liguilla; cache `data/cache/revisao/ES/`).
- 11v11 (lista `revisao/EN/datas_11v11_saida.txt` da 2ª rodada) para o EN-005; RSSSF https://rsssfbrasil.com/tablesae/cbr1990.htm e ogol (`data/coleta/bra-copa-do-brasil/ogol/copa_brasil_1990.json`) para o CB-005.
- Código: `coleta/bra-sp-1/importar.py` (ORDEM, classificacao), `coleta/uru-1/importar.py` (classificacao), `coleta/arg-1/edicoes.py` e `explicacoes.py`, `coleta/esp-1/importar.py` (NOMES_ESPN), `baixar_escudos.py`, `gerar_dashboard_v2.py`.
