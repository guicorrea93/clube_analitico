# Coleta Brasil (agente 2) — documentação

Gerado por `python coleta/comum/documentar.py`. Uma ficha por competição, com tudo o que o pacote tem, a cobertura de cada campo década a década, o formato ao longo do tempo, campeões, acessos, rebaixados e punições, todas as correções e decisões com o motivo, o que não deu para coletar, as pendências e os comandos para refazer.

Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-brasil`).

| Competição | Temporadas | Jogos | Gols c/ autor | Cartões | Clubes | Tabelas ok / div. | No banco | Pendências | Ficha |
|---|---|---|---|---|---|---|---|---|---|
| Campeonato Brasileiro Série C | 39 (1981–2026) | 8705 | 6051 | 0 | 379 | 418 / 30 | sim (39 edições, 8705 jogos) | 2 | [bra-serie-c](bra-serie-c.md) |
| Campeonato Brasileiro Série D | 18 (2009–2026) | 6032 | 11227 | 0 | 333 | 431 / 4 | sim (18 edições, 6032 jogos) | 2 | [bra-serie-d](bra-serie-d.md) |
| Copa do Brasil | 37 (1989–2025) | 4010 | 5764 | 0 | 399 | 61 / 0 | sim (37 edições, 4010 jogos) | 4 | [bra-copa-do-brasil](bra-copa-do-brasil.md) |
| Campeonato Paulista | 135 (1902–2026) | 21849 | 6405 | 0 | 112 | 222 / 120 | sim (135 edições, 21849 jogos) | 3 | [bra-sp-1](bra-sp-1.md) |
| Campeonato Paulista Série A2 | 80 (1947–2026) | 9214 | 4526 | 0 | 184 | 134 / 31 | sim (80 edições, 9214 jogos) | 4 | [bra-sp-2](bra-sp-2.md) |
| Campeonato Carioca | 129 (1906–2026) | 14144 | 3383 | 0 | 83 | 223 / 127 | sim (129 edições, 14144 jogos) | 3 | [bra-rj-1](bra-rj-1.md) |
| Campeonato Mineiro | 113 (1915–2026) | 11521 | 24324 | 0 | 96 | 285 / 196 | sim (113 edições, 11521 jogos) | 4 | [bra-mg-1](bra-mg-1.md) |
| Campeonato Gaúcho | 107 (1918–2026) | 13393 | 3843 | 0 | 136 | 230 / 159 | sim (106 edições, 13393 jogos) | 5 | [bra-rs-1](bra-rs-1.md) |
| Campeonato Paranaense | 113 (1915–2026) | 14315 | 2410 | 0 | 142 | 209 / 225 | sim (113 edições, 14315 jogos) | 6 | [bra-pr-1](bra-pr-1.md) |
| Campeonato Cearense | 112 (1915–2026) | 8501 | 2821 | 0 | 57 | 185 / 95 | sim (112 edições, 8501 jogos) | 5 | [bra-ce-1](bra-ce-1.md) |
| Campeonato Goiano | 83 (1944–2026) | 8682 | 2965 | 0 | 62 | 180 / 99 | não | 4 | [bra-go-1](bra-go-1.md) |

Fora das fichas: `bra-serie-a-artilheiros` (artilheiros oficiais da Série A, 1937-2025, pedido do agente 1; `coleta/bra-serie-a-artilheiros/montar.py`, relatório `docs/coleta/bra-serie-a-artilheiros.md`). A Série A e a Série B são do agente 1 (`serie_b/`).

## Pendências de todas as competições

- **bra-serie-c:** Achados da revisão SC-001 a SC-023 e CL-002/CL-004/CL-005/CL-012: tratados (docs/coleta/pedidos.md, partes 2 e 4, edições de 2026 e identidade). A revisão ainda não reconferiu (docs/revisao/achados.csv segue com 'aberto').
- **bra-serie-c:** Autores dos gols antes de 2012 e cartões: só jogo a jogo, pela ficha do ogol (~8 mil pedidos, ~3 h). Prioridade baixa (cartões, mais baixa ainda), decisão do Guilherme (20/11/2026).
- **bra-serie-d:** Achados da revisão SD-001 a SD-021: tratados (docs/coleta/pedidos.md, parte 3, parte 4 e edições de 2026). A revisão ainda não reconferiu.
- **bra-serie-d:** Cartões: só jogo a jogo, pela ficha do ogol (prioridade baixa).
- **bra-copa-do-brasil:** Achados da revisão CB-001 a CB-015: tratados (docs/coleta/pedidos.md, partes 1 e 4). Plano da revisão (24/11): QC-005, QC-004 (datas_corrigidas.csv), CB-007 e QC-008 (D-14 C), CL-028 (Alegrense). A revisão ainda não reconferiu.
- **bra-copa-do-brasil:** Jogo preliminar de 1999: entrou Náutico 0-1 Santa Cruz em 28/01/1999, pelo Futebol Nacional (D-14 C); a Wikipédia pt dá o mando ao contrário (Santa Cruz 1-0). Conferir no Diario de Pernambuco de 29/01/1999 só se o Guilherme pedir.
- **bra-copa-do-brasil:** CB-005 (D-13): 1990 (volta Santa Cruz x América-RN) e 1991 (Vitória x Remo) ficam como estão até um jornal da época.
- **bra-copa-do-brasil:** Autores dos gols antes de 2013 e cartões: jogo a jogo, pela ficha do ogol (prioridade baixa).
- **bra-sp-1:** Plano da revisão (docs/revisao/plano-coleta-brasil.md) concluído em 24/11, em 5 commits (ERRADO NO AR, jogos, FPF e 2026, pacote.py, pódio); detalhes em docs/coleta/pedidos.md.
- **bra-sp-1:** Ficam como estão, com o motivo: 3º lugar de 1917 e 1954 (o FN confirma o pacote; a Wikipédia diverge), 1927 LAF, 1928 LAF e 1930 (3º dividido na RSSSF), 1959 (empate sem regra da época); 44 casos de clube com dois jogos no mesmo dia de 1906 a 1983 (conferir com o Futebol Nacional); artilheiro de 1927 APEA, 1928 LAF e 1936 LPF.
- **bra-sp-1:** Autores dos gols e cartões nos anos sem RSSSF com autores: jogo a jogo, pela ficha do ogol (prioridade baixa).
- **bra-sp-2:** Plano da revisão concluído em 24/11 (ERRADO NO AR, A2-001 e as partes A, B e C); detalhes em docs/coleta/pedidos.md.
- **bra-sp-2:** 1967-1984: só os jogos que a Wikipédia traz (finais e fases finais); os jogos dos campeões nas páginas da RSSSF de 1968, 1969, 1971, 1976, 1980 e 1984 ainda não entraram. Clubes novos a conferir pela revisão: Vasco da Gama (1969) e Americana (1976), os dois de Americana; Presidente Prudente FC (1974).
- **bra-sp-2:** Datas que a própria página dá impossíveis (1985, 1986, 1987 e 1988, A2-027): sem 2ª fonte; ficam anotadas.
- **bra-sp-2:** Jogos que faltam (1947-1966 fora o que a Wikipédia traz; 1988: 69 sem placar; 1989: 2ª e 3ª fases; 1990: 1ª a 3ª; 1991: 1ª fase; 1992: 1ª fase; 1993 e 1994): só em jornais da época (Hemeroteca Digital, acervos do Estadão e da Folha), em imagem. Só se o Guilherme pedir.
- **bra-rj-1:** Autores dos gols: só 3.383 (quase todos de 2010 em diante). Nas outras décadas a página não traz os autores ou traz num formato que o leitor ainda não junta ao jogo ("Gols: ..." na linha de baixo, nos anos 1900).
- **bra-rj-1:** 127 tabelas divergentes a explicar (ou corrigir) uma a uma no relatório; jogos avulsos do fim das páginas (súmulas sem par na lista: 1915, 1917-1919, 1924 AMEA, 1925, 1938, 1944, 1959, 1976) a conferir.
- **bra-rj-1:** Artilheiros de 2015 em diante: a lista da RSSSF (rjtops.htm) parou em 2014; a Wikipédia em português tem a tabela ano a ano (pt_lista.txt), ainda não lida.
- **bra-mg-1:** 196 tabelas divergentes a explicar no relatório. Boa parte não é erro de jogo: a tabela publicada conta o W.O. com gols (D-15: sem gols), traz um turno por tabela quando a página junta os jogos (1983-1987), ou erra a soma (RSSSF e ogol com os mesmos placares).
- **bra-mg-1:** Vices em que as fontes discordam: 1934 (pacote Tupynambás, que perdeu a final estadual; RSSSF Palestra Itália; Wikipédia Tupynambás no estadual e Atlético na cidade), 1942 (RSSSF América; Wikipédia e pacote Palestra Mineiro, o Cruzeiro) e 1950 (RSSSF Cruzeiro; Wikipédia e pacote Siderúrgica).
- **bra-mg-1:** 1924 e 1925 incompletos na própria fonte (1924: "Incomplete scores"; 1925: 4 jogos, campeonato anulado na época e título homologado pela FMF em 2012). Pontos extras de 1975 (Atlético e Cruzeiro, +1 na fase final) não entram na classificação calculada.
- **bra-mg-1:** Autores dos gols: 24.324 de 31.081; cartões: só jogo a jogo, pela ficha do ogol (prioridade baixa).
- **bra-rs-1:** 1918 (campeonato suspenso pela gripe espanhola): edição sem jogos, com os três campeões honoríficos que a FGF reconheceu em 2021 (Brasil de Pelotas em campeao; Cruzeiro e 14 de Julho em co_campeao, que o carregador ainda não aceita com dois clubes). Decisão do Guilherme em 25/11, a mesma das edições sem jogos do Cearense.
- **bra-rs-1:** De 1925 a 1976 o ogol não tem os jogos: a identidade dos clubes vem dos nomes (importar.NOME_CODIGO e NOME_ANO; "Riograndense", "Guarany", "Guarani", "Cruzeiro" e "Nacional" sem cidade mudam de clube conforme a época). As páginas dos anos 1960-1990 vêm de texto escaneado (grafias em rsssf_rs1.GRAFIAS).
- **bra-rs-1:** Identidade a revisar: SE São Borja (241325, antes de 2009) x AE São Borja (70071) - as fontes discordam se é a mesma linhagem; Flamengo de Alegrete com ficha de 1963 e jogos em 1961-1962; AE Santo Ângelo (antes da fusão de 1989) separado da SER Santo Ângelo.
- **bra-rs-1:** Vices de 1986 e 1993: o pacote segue a classificação publicada/final; a Wikipédia dá o Internacional.
- **bra-rs-1:** Tabelas divergentes a explicar no relatório (muitas nos anos de página escaneada, 1963-1996). Autores dos gols: as páginas quase não trazem (cerca de 12% dos gols). Cartões: só jogo a jogo, pela ficha do ogol.
- **bra-pr-1:** 2002 Supercampeonato: edição não oficial (coluna oficial = "não"), com os clubes da Copa Sul-Minas; o Athletico conta o título, mas a lista oficial da FPF não foi achada. 1980: título dividido (Colorado e Cascavel, co_campeao).
- **bra-pr-1:** De 1915 a 2000 o ogol não tem os jogos (só 1965 e 1967): a identidade dos clubes vem dos nomes (importar.NOME_CODIGO e NOME_ANO). "Paraná" (Paraná SC até 1926, Paraná EC de Londrina em 1968-1969, Paraná Clube de 1990), "Cascavel" (Cascavel FC em 1971-1972, Cascavel EC de 1980 a 2000, Cascavel CR de 2003), "Maringá" (Grêmio Maringá até 1996, Maringá FC 1995 em 1997-1998, Maringá FC de 2010), "Toledo", "Foz do Iguaçu", "Arapongas", "Cianorte" (CAFE até 2001) e "Nacional" mudam de clube conforme a época.
- **bra-pr-1:** Identidade a revisar: o EC Água Verde (39780: Savóia, Savóia Água Verde, EC Brasil e Água Verde, 1916-1971) e o EC Pinheiros (17224, 1972-1989) são a mesma linhagem (RSSSF, prcamp.htm), mas o ogol, o cadastro comum e o banco os separam; o pacote segue o cadastro. O Palestra Itália leva os nomes da II Guerra (Paranaense 1942, Comercial 1943-1945, Palmeiras 1946-1949). Cambaraense (1952-1962) e Cambará (1963-1965) ficam separados.
- **bra-pr-1:** Vices diferentes da Wikipédia: 1923-1926 e 1940 (a Wikipédia dá o Operário Ferroviário; as páginas da RSSSF não têm jogo com ele) e 1941 (a página dá a final Coritiba 6-1 Antoninense; a Wikipédia, Jacarezinho). Fica o da página.
- **bra-pr-1:** Fora do pacote: o jogo de 24/08/1924 "Atlético 2-1 Atlético" (a página não diz o adversário) e a Final do Interior de 2015 e 2016 (título à parte, como o Troféu do Interior do Gaúcho).
- **bra-pr-1:** Tabelas divergentes a explicar no relatório (225, contra 209 que batem). Autores dos gols: as páginas quase não trazem (6% dos gols; 2021-2026 sem autor). Cartões: só jogo a jogo, pela ficha do ogol.
- **bra-ce-1:** 17 edições sem jogos em nenhuma fonte (1916-1919, 1924-1927, 1929-1932, 1934-1938) entram só com campeão e vice (importar.PODIO_SEM_JOGOS; decisão do Guilherme em 25/11). 1915 tem só a final. O Orion, campeão de 1930, só aparece nessas edições.
- **bra-ce-1:** 1992: título dividido entre Fortaleza, Ceará, Tiradentes e Icasa. `co_campeao` traz os três outros separados por " / "; o carregador aceita um clube só (pedido ao agente 1). 2004: sem final (liminar; o STJD deu o título ao Fortaleza); a linha "n/p" da página fica fora.
- **bra-ce-1:** A RSSSF Brasil parou de responder em 25/11: 87 páginas vieram do Internet Archive (rsssfbrasil/origem.json). Sem página: 2025 e 2026 (jogos só do ogol). As páginas de 1988-1990 perderam os acentos (rsssf_ce1._acentos).
- **bra-ce-1:** Identidade a revisar: "Iguatu 1996" (o Iguatu de 1996-1997; a ficha do ogol é de 2010), "América-R" (1996) e "Russas" (1997), talvez o mesmo clube; Esporte Clube Limoeiro (1995-2000) separado do Limoeiro do ogol (2001).
- **bra-ce-1:** Fora do pacote: a Taça Padre Cícero de 2012 (título à parte). Tabelas divergentes a explicar no relatório (95, contra 185 que batem). Autores dos gols: 11% (as páginas quase não trazem). Cartões: só jogo a jogo, pela ficha do ogol.
- **bra-go-1:** 8 edições sem jogos (1945, 1946, 1950, 1951, 1960, 1963, 1965, 1966) entram só com campeão e vice (importar.PODIO_SEM_JOGOS). Ficam fora os campeonatos de Goiânia de 1940 e 1943 e o "Campeonato Estadual de Goiás" amador, que a FGF não reconhece.
- **bra-go-1:** Vices diferentes da Wikipédia: 1958 (pacote Vila Nova, pela tabela; Wikipédia Atlético) e 2000 (pacote Vila Nova, que perdeu as duas finais de turno para o Goiás; Wikipédia Anapolina, talvez pela campanha geral).
- **bra-go-1:** Jogos corrigidos pela tabela de confrontos (a página dá o mesmo clube aos dois lados): 1978 Anápolis 1-0 Anapolina e 1993 Mineiros 2-1 Anapolina. Outros confrontos trocados na 1ª fase de 1993 (CRAC x Goiânia duas vezes, Itumbiara x Mineiros duas vezes) ficam como a página traz.
- **bra-go-1:** Fora do pacote: os dois amistosos de 1995 e a repetição sem data da final de 2021. Tabelas divergentes a explicar no relatório (99, contra 180 que batem). Autores dos gols: 13%. Cartões: só jogo a jogo, pela ficha do ogol.

## Próximas competições

- Ordem dada pelo Guilherme (22/11/2026): Mineiro (`bra-mg-1`), Gaúcho (`bra-rs-1`), Paulista A3 (`bra-sp-3`). Cada uma com o ok dele.
