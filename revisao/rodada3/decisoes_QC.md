# Decisões do Guilherme: Série C, Série D e Copa do Brasil (revisor QC, 22/11/2026)

Quatro novas (QC-D1 a QC-D4) e três antigas ainda sem resposta em `docs/coleta/pedidos.md` e em `coleta/comum/COMECE-AQUI.md` (seção 7).

### QC-D1 Clube que só jogou com outro nome: mostrar o nome da época ou o de hoje? (QC-009, CL-023)
- opções: (a) como hoje: o nome que o ogol dá ao código do clube agora ("Manchete", "Rive A.C."); (b) o nome da época quando TODOS os jogos do clube no banco são com aquele nome ("Santo Amaro-PE" na Série C 1981; "Espírito Santo FC" na Série D 2016-2018), com o nome atual nos nomes de fonte; (c) nome de hoje, com o nome da época entre parênteses só na edição.
- prova: Série C 1981: RSSSF "Santo Amaro (Recife, PE)" (https://rsssfbrasil.com/tablesae/br1981l3.htm), Bola n@ Área "2º Santo Amaro (PE)" (https://www.bolanaarea.com/serie_c_1981.htm), Futebol Nacional "1981 Olaria/RJ Santo Amaro/PE"; Série D 2016-2018: RSSSF e ogol da época "Espírito Santo"; Wikipédia https://pt.wikipedia.org/wiki/Rive_Atl%C3%A9tico_Clube (Espírito Santo FC 2006, Gálatas EC 2025, Rive AC 2026, outra cidade).
- recomendação: (b), só para esses casos (clube que nunca jogou nada no banco com o nome atual). É o que as fontes da época mostram e evita um "Rive A.C." de Alegre num campeonato que ele não jogou. Exige abrir exceção à regra "nome já dado não muda" (data/coleta/comum/clubes_ogol.json) para os dois códigos. Clubes que jogaram com os dois nomes continuam com o atual (decisão de 21/11 sobre nomes).

### QC-D2 Série C: 3 placares em que Bola n@ Área + Wikipédia ficam contra RSSSF + ogol (SC-016)
- opções: (a) manter o pacote (RSSSF e ogol); (b) trocar pelo Bola/Wikipédia; (c) manter e procurar o jornal da época antes de decidir.
- prova: 1992 Nacional-AM x Tuna Luso (27/05, 2ª fase): pacote 2x2, Bola e Wikipédia en 1x1; 1992 Rio Branco-MG x Marília (08-09/04): pacote 0x1, Bola e en 0x2; 1994 Caldas x Vila Nova-GO (23/10): pacote 1x3 (do ogol), Bola e en 0x3. As páginas pt e en de 1992 e 1994 citam o Bola n@ Área como fonte, então não são duas fontes independentes. Nos outros 9 jogos do SC-016 o Bola fica com o pacote. https://www.bolanaarea.com/serie_c_1992_tab.htm; https://rsssfbrasil.com/tablesae/br1992l3.htm; https://en.wikipedia.org/wiki/1992_Campeonato_Brasileiro_S%C3%A9rie_C
- recomendação: (c), e até lá (a). Nenhum dos 3 muda campeão, acesso ou quem passou de fase. Jornal: Hemeroteca Digital (https://memoria.bn.gov.br/hdb/periodico.aspx), um pedido por jogo.

### QC-D3 Copa do Brasil 1990 Santa Cruz x América-RN e 1991 Vitória x Remo (CB-005)
- opções: (a) manter o pacote (RSSSF e ogol: 1990 América-RN 1x0 Santa Cruz; 1991 Vitória 0x0 Remo); (b) Bola + Wikipédia pt (1990 América-RN 0x1 Santa Cruz; 1991 Vitória 2x2 Remo); (c) jornal da época.
- prova: Bola n@ Área https://www.bolanaarea.com/copa_do_brasil_1990_tabela.htm e copa_do_brasil_1991_tabela.htm; o Futebol Nacional também (América 0x1 Santa Cruz; Vitória 2x2 Remo); a Wikipédia pt de 1990 e 1991 cita o Bola; a en de 1991 dá 0x0 (igual ao pacote) e a de 1990 dá 0x1; RSSSF https://rsssfbrasil.com/tablesae/cbr1990.htm ("3-1 0-1"); ogol jogos 652618 e 652712. A infobox pt de 1991 (132 gols) só fecha com o 2x2.
- recomendação: (c). Em 1990 são 3 fontes (Bola, pt, en) contra 2 (RSSSF, ogol), mas pt vem do Bola; em 1991 o total de gols da pt também vem do Bola. Diario de Pernambuco de 28/06/1990 e Jornal do Brasil de 26/04/1991 resolvem. Nenhum dos dois muda quem passou.

### QC-D4 Copa do Brasil 1999: a preliminar Santa Cruz 1x0 Náutico entra? (CB-007)
- opções: (a) fica fora (como RSSSF, ogol e Bola n@ Área: 116 jogos, 64 clubes) e o CB-007 fecha como nao-e-erro; (b) entra sem data, com fonte "Wikipédia (pt)"; (c) entra só com a data de um jornal.
- prova: Futebol Nacional (fonte nova): Náutico 0x1 Santa Cruz em 28/01/1999, 117 jogos na edição (resumo da Copa: https://futebolnacional.com.br/siteapp/controller.jsp?module=summary&lang=pt-br&name=51E612B97CC3E60E6BA884B54CBBEEC7&state=--&country=BR); https://pt.wikipedia.org/wiki/Copa_do_Brasil_de_Futebol_de_1999 (infobox 117 jogos; Santa Cruz 1x0 Náutico, sem data); sem o jogo: https://www.bolanaarea.com/copa_do_brasil_1999_tabela.htm (o regulamento cita a "Fase Preliminar"), https://rsssfbrasil.com/tablesae/cbr1999.htm e ogol.
- recomendação: (c) com a data do Futebol Nacional: incluir 28/01/1999 Náutico 0x1 Santa Cruz (Fase preliminar). Duas fontes têm o jogo e uma dá a data; só o mando diverge (conferir no Diario de Pernambuco de 29/01/1999).

### SC-018 (antiga, de 21/11) Ordem dos eliminados na classificação calculada
- opções: (a) regra da coleta (fase alcançada, posição no grupo dessa fase, campanha); (b) a da "Classificação geral" da Wikipédia pt (fase alcançada, depois pontos da campanha toda).
- prova: 1988 ABC 13º (pt 7º); 2025 5º Guarani (pt 5º Caxias); Série D 2012 Comercial-PI 29º (pt 34º). https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2025_-_S%C3%A9rie_C. O Bola n@ Área publica a "colocação final" de cada edição (ex.: https://www.bolanaarea.com/serie_c_2008.htm), que pode servir de 2ª opinião (não comparada nesta rodada).
- recomendação: (b): é a ordem que a fonte publica. Mexer em coleta/bra-serie-c/importar.py e coleta/bra-serie-d/importar.py (chave de ordenação da classificação).

### RC-005 (antiga, de 22/11) Gols de W.O. entram nos totais? (Série D 2014)
- opções: (a) o jogo de W.O. conta como jogo e os 3 gols contam (hoje: 200 jogos, 515 gols); (b) conta como jogo, sem gols; (c) não conta nem como jogo.
- prova: Wikipédia pt (199 jogos, 503 gols: https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2014_-_S%C3%A9rie_D); Bola n@ Área "200 jogos, 503 gols" (https://www.bolanaarea.com/serie_d_2014.htm).
- recomendação: (b): as duas fontes descontam os gols; o Bola conta o jogo (a tabela de pontos precisa dele). Mexer em gerar_dashboard_v2.py (somas de gols ignoram resultado_especial awd/w.o.).

### SC (antiga, de 20/11) 1987 e 2000 continuam fora da Série C?
- opções: (a) fora, como hoje; (b) incluir 1987 (módulos Azul e Branco) e 2000 (módulos Verde e Branco da Copa João Havelange) como edições à parte.
- prova: a coleta diz que RSSSF e Wikipédia não contam como Série C oficial (coleta/comum/documentacao/bra-serie-c.md, seção 1); o Futebol Nacional lista 2000 sem campeão e não lista 1987 na 3ª Divisão; o Bola n@ Área tem páginas das duas (https://www.bolanaarea.com/serie_c_1987.htm, serie_c_2000.htm) como "Série C".
- recomendação: (a). A CBF não conta; se quiser os jogos, o Bola tem as tabelas.
