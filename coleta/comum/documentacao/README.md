# Coleta Brasil (agente 2) — documentação

Gerado por `python coleta/comum/documentar.py`. Uma ficha por competição, com tudo o que o pacote tem, a cobertura de cada campo década a década, o formato ao longo do tempo, campeões, acessos, rebaixados e punições, todas as correções e decisões com o motivo, o que não deu para coletar, as pendências e os comandos para refazer.

Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-brasil`).

| Competição | Temporadas | Jogos | Gols c/ autor | Cartões | Clubes | Tabelas ok / div. | No banco | Pendências | Ficha |
|---|---|---|---|---|---|---|---|---|---|
| Campeonato Brasileiro Série C | 36 (1981–2026) | 8123 | 6051 | 0 | 373 | 389 / 29 | sim (36 edições, 8123 jogos) | 2 | [bra-serie-c](bra-serie-c.md) |
| Campeonato Brasileiro Série D | 18 (2009–2026) | 6032 | 11227 | 0 | 333 | 431 / 4 | sim (18 edições, 6032 jogos) | 2 | [bra-serie-d](bra-serie-d.md) |
| Copa do Brasil | 37 (1989–2025) | 4009 | 5718 | 0 | 399 | 61 / 0 | sim (37 edições, 4009 jogos) | 3 | [bra-copa-do-brasil](bra-copa-do-brasil.md) |
| Campeonato Paulista | 134 (1902–2025) | 21791 | 6405 | 0 | 112 | 213 / 129 | sim (134 edições, 21791 jogos) | 3 | [bra-sp-1](bra-sp-1.md) |
| Campeonato Paulista Série A2 | 80 (1947–2026) | 9223 | 4526 | 0 | 183 | 132 / 33 | sim (63 edições, 9142 jogos) | 3 | [bra-sp-2](bra-sp-2.md) |
| Campeonato Carioca | 129 (1906–2026) | 14144 | 3383 | 0 | 83 | 223 / 127 | sim (129 edições, 14144 jogos) | 4 | [bra-rj-1](bra-rj-1.md) |

Fora das fichas: `bra-serie-a-artilheiros` (artilheiros oficiais da Série A, 1937-2025, pedido do agente 1; `coleta/bra-serie-a-artilheiros/montar.py`, relatório `docs/coleta/bra-serie-a-artilheiros.md`). A Série A e a Série B são do agente 1 (`serie_b/`).

## Pendências de todas as competições

- **bra-serie-c:** Achados da revisão SC-001 a SC-023 e CL-002/CL-004/CL-005/CL-012: tratados (docs/coleta/pedidos.md, partes 2 e 4, edições de 2026 e identidade). A revisão ainda não reconferiu (docs/revisao/achados.csv segue com 'aberto').
- **bra-serie-c:** Autores dos gols antes de 2012 e cartões: só jogo a jogo, pela ficha do ogol (~8 mil pedidos, ~3 h). Prioridade baixa (cartões, mais baixa ainda), decisão do Guilherme (20/11/2026).
- **bra-serie-d:** Achados da revisão SD-001 a SD-021: tratados (docs/coleta/pedidos.md, parte 3, parte 4 e edições de 2026). A revisão ainda não reconferiu.
- **bra-serie-d:** Cartões: só jogo a jogo, pela ficha do ogol (prioridade baixa).
- **bra-copa-do-brasil:** Achados da revisão CB-001 a CB-015: tratados (docs/coleta/pedidos.md, partes 1 e 4). A revisão ainda não reconferiu.
- **bra-copa-do-brasil:** Jogo preliminar de 1999 (Santa Cruz 1-0 Náutico, CB-007): entrou sem data; nenhuma fonte achada dá o dia.
- **bra-copa-do-brasil:** Autores dos gols antes de 2013 e cartões: jogo a jogo, pela ficha do ogol (prioridade baixa).
- **bra-sp-1:** Corrigidos em 23/11 ("ERRADO NO AR" do plano docs/revisao/plano-coleta-brasil.md): SP-011 (jogo falso de 1928 LAF), SP-002, SP-007 e SP-008 (ORDEM completo, FASE_ANO e FASE_JOGO, vice do quadrangular final, desempate pela Fase final; menos 2024 e 2025, que esperam as fases da FPF), QS-001 e SP-010 (CLUBES_FORA), QS-006 e QS-005 (JOGOS_FORA, JOGOS_EXTRA_WO, VICE_OFICIAL), QS-015 e SP-013 (PONTOS_FORA_DE_CAMPO; W.O. conta na campanha, SP-016), SP-009 (Corinthians de Santo André) e SP-012 (1942). SP-001: 1973 com co_campeao Santos e vice Palmeiras (D-07).
- **bra-sp-1:** Resto do plano (docs/revisao/plano-coleta-brasil.md, seção do Paulista): SP-003 (3º lugar à mão), SP-004 (2026), SP-008 em 2024 e 2025 (fases pela API da FPF), SP-014, SP-015 (rebaixados), SP-017 a SP-024, QS-002 a QS-014, SP-026 e SP-027 (D-23). Só quando o Guilherme mandar.
- **bra-sp-1:** Autores dos gols e cartões nos anos sem RSSSF com autores: jogo a jogo, pela ficha do ogol (prioridade baixa).
- **bra-sp-2:** Corrigidos em 23/11 ("ERRADO NO AR" do plano da revisão): A2-002 a A2-006 (vice pela fase final e pelo finalista), A2-007 (REBAIXADOS_WIKI), A2-008 ("Relegation Playoff" não é queda), A2-009 (acesso só de quem jogou a A1), A2-010 (Portuguesa Santista em 2002), A2-011 e A2-017 (2001: regra dos pênaltis, -5 do Sãocarlense, sem rebaixado). A2-001 feito em 23/11: as 17 edições de 1967-1978 e 1980-1984 (participantes da RSSSF, tabelas e jogos da Wikipédia, pódio da predefinição).
- **bra-sp-2:** 1967-1984: só os jogos que a Wikipédia traz (finais e fases finais); os jogos dos campeões nas páginas da RSSSF de 1968, 1969, 1971, 1976, 1980 e 1984 ainda não entraram. Clubes novos a conferir pela revisão: Vasco da Gama (1969) e Americana (1976), os dois de Americana; Presidente Prudente FC (1974).
- **bra-sp-2:** Jogos que faltam (1947-1966 fora o que a Wikipédia traz; 1988: 69 sem placar; 1989: 2ª e 3ª fases; 1990: 1ª a 3ª; 1991: 1ª fase; 1992: 1ª fase; 1993 e 1994): só em jornais da época (Hemeroteca Digital, acervos do Estadão e da Folha), em imagem. Só se o Guilherme pedir.
- **bra-rj-1:** Autores dos gols: só 3.383 (quase todos de 2010 em diante). Nas outras décadas a página não traz os autores ou traz num formato que o leitor ainda não junta ao jogo ("Gols: ..." na linha de baixo, nos anos 1900).
- **bra-rj-1:** 127 tabelas divergentes a explicar (ou corrigir) uma a uma no relatório; jogos avulsos do fim das páginas (súmulas sem par na lista: 1915, 1917-1919, 1924 AMEA, 1925, 1938, 1944, 1959, 1976) a conferir.
- **bra-rj-1:** Artilheiros de 2015 em diante: a lista da RSSSF (rjtops.htm) parou em 2014; a Wikipédia em português tem a tabela ano a ano (pt_lista.txt), ainda não lida.
- **bra-rj-1:** Mesma correção dos artilheiros no Paulista: lá a lista da RSSSF nunca era usada (chave pelo ano em número), o que deve explicar o SP-024.

## Próximas competições

- Ordem dada pelo Guilherme (22/11/2026): Mineiro (`bra-mg-1`), Gaúcho (`bra-rs-1`), Paulista A3 (`bra-sp-3`). Cada uma com o ok dele.
