# Coleta Brasil (agente 2) — documentação

Gerado por `python coleta/comum/documentar.py`. Uma ficha por competição, com tudo o que o pacote tem, a cobertura de cada campo década a década, o formato ao longo do tempo, campeões, acessos, rebaixados e punições, todas as correções e decisões com o motivo, o que não deu para coletar, as pendências e os comandos para refazer.

Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-brasil`).

| Competição | Temporadas | Jogos | Gols c/ autor | Cartões | Clubes | Tabelas ok / div. | No banco | Pendências | Ficha |
|---|---|---|---|---|---|---|---|---|---|
| Campeonato Brasileiro Série C | 36 (1981–2026) | 8123 | 6051 | 0 | 373 | 389 / 29 | sim (36 edições, 8123 jogos) | 2 | [bra-serie-c](bra-serie-c.md) |
| Campeonato Brasileiro Série D | 18 (2009–2026) | 6032 | 11227 | 0 | 333 | 431 / 4 | sim (18 edições, 6032 jogos) | 2 | [bra-serie-d](bra-serie-d.md) |
| Copa do Brasil | 37 (1989–2025) | 4009 | 5718 | 0 | 399 | 61 / 0 | sim (37 edições, 4009 jogos) | 3 | [bra-copa-do-brasil](bra-copa-do-brasil.md) |
| Campeonato Paulista | 134 (1902–2025) | 21855 | 6405 | 0 | 115 | 207 / 135 | sim (134 edições, 21855 jogos) | 3 | [bra-sp-1](bra-sp-1.md) |
| Campeonato Paulista Série A2 | 63 (1947–2026) | 9142 | 4526 | 0 | 167 | 128 / 31 | não | 3 | [bra-sp-2](bra-sp-2.md) |

Fora das fichas: `bra-serie-a-artilheiros` (artilheiros oficiais da Série A, 1937-2025, pedido do agente 1; `coleta/bra-serie-a-artilheiros/montar.py`, relatório `docs/coleta/bra-serie-a-artilheiros.md`). A Série A e a Série B são do agente 1 (`serie_b/`).

## Pendências de todas as competições

- **bra-serie-c:** Achados da revisão SC-001 a SC-023 e CL-002/CL-004/CL-005/CL-012: tratados (docs/coleta/pedidos.md, partes 2 e 4, edições de 2026 e identidade). A revisão ainda não reconferiu (docs/revisao/achados.csv segue com 'aberto').
- **bra-serie-c:** Autores dos gols antes de 2012 e cartões: só jogo a jogo, pela ficha do ogol (~8 mil pedidos, ~3 h). Prioridade baixa (cartões, mais baixa ainda), decisão do Guilherme (20/11/2026).
- **bra-serie-d:** Achados da revisão SD-001 a SD-021: tratados (docs/coleta/pedidos.md, parte 3, parte 4 e edições de 2026). A revisão ainda não reconferiu.
- **bra-serie-d:** Cartões: só jogo a jogo, pela ficha do ogol (prioridade baixa).
- **bra-copa-do-brasil:** Achados da revisão CB-001 a CB-015: tratados (docs/coleta/pedidos.md, partes 1 e 4). A revisão ainda não reconferiu.
- **bra-copa-do-brasil:** Jogo preliminar de 1999 (Santa Cruz 1-0 Náutico, CB-007): entrou sem data; nenhuma fonte achada dá o dia.
- **bra-copa-do-brasil:** Autores dos gols antes de 2013 e cartões: jogo a jogo, pela ficha do ogol (prioridade baixa).
- **bra-sp-1:** ALTA: achados da revisão SP-001 a SP-032 (docs/coleta/pedidos.md, 'Pedidos da revisão (21/11/2026): Paulista'; provas em docs/revisao/bra-sp-1.md) ainda NÃO tratados: jogo falso de 1928 LAF (SP-011), vice e ordem final (SP-002, SP-003, SP-007, SP-008), dados que mudam o vice (SP-009, SP-010, SP-012, SP-013, SP-014), rebaixados (SP-015), W.O., datas, totais, observações em inglês (SP-016 a SP-022) e artilheiros (SP-023, SP-024).
- **bra-sp-1:** Decisões do Guilherme pedidas pela revisão: SP-001 (título de 1973 dividido), SP-004 (edição de 2026), SP-005 (amadores da FPF 1933-1934), SP-006 ('Paulistinha' 1970 e 1972-1974), SP-026 e SP-027 (juntar clubes).
- **bra-sp-1:** Autores dos gols e cartões nos anos sem RSSSF com autores: jogo a jogo, pela ficha do ogol (prioridade baixa).
- **bra-sp-2:** Commit das edições antigas e da documentação (22/11/2026): pedir o ok do Guilherme. Depois, o agente 1 carregar a A2 no banco (recados no fim de docs/coleta/pedidos.md).
- **bra-sp-2:** Jogos que faltam (1947-1966 fora o que a Wikipédia traz; 1988: 69 sem placar; 1989: 2ª e 3ª fases; 1990: 1ª a 3ª; 1991: 1ª fase; 1992: 1ª fase; 1993 e 1994): só em jornais da época (Hemeroteca Digital, acervos do Estadão e da Folha), em imagem. Só se o Guilherme pedir.
- **bra-sp-2:** Os mesmos achados de vice e ordem final do Paulista (SP-002, SP-007, SP-008) podem valer na A2: conferir quando tratar o bra-sp-1 (o importador é cópia do dele).

## Próximas competições

- Nenhuma em andamento. Não começar outra sem o Guilherme pedir (decisão de 20/11/2026). Candidatas, se ele pedir: Paulista A3 (`bra-sp-3`, RSSSF `sp{ano}l3.htm`) e outros estaduais (Carioca, Mineiro, Gaúcho).
