# Coleta América do Sul — documentação

Gerado por `python coleta/comum-sulamerica/documentar.py`. Uma ficha por competição, com tudo o que o pacote tem, como as edições foram definidas, fontes e regras, a conferência, a cobertura de cada campo década a década, o formato ao longo do tempo, campeões e vices, ajustes de pontos, todas as correções e decisões com o motivo, o que não deu para coletar e as pendências.

Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum-sulamerica/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-sulamerica.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-sulamerica`).

| Competição | Edições | Sem jogos | Jogos | Gols c/ autor | Cartões | Clubes | Edições ok / div. | No banco | Commit | Achados abertos | Ficha |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Campeonato Argentino | 197 (1891–2026 Apertura) | 1 | 43726 | 36043 | 41255 | 173 | 142 / 51 | sim | 415911b | 41 | [arg-1](arg-1.md) |
| Campeonato Uruguaio | 126 (1900–2025) | 45 | 12456 | 14335 | 9481 | 84 | 59 / 22 | sim | 415911b | 21 | [uru-1](uru-1.md) |
| Campeonato Chileno | 109 (1933–2025) | 0 | 22586 | 19548 | 26607 | 53 | 76 / 32 | sim | 415911b | 26 | [chi-1](chi-1.md) |
| Campeonato Colombiano | 101 (1948–2025 Finalización) | 6 | 22512 | 22041 | 40519 | 42 | 48 / 38 | sim | 415911b | 22 | [col-1](col-1.md) |
| Campeonato Paraguaio | 134 (1906–2026 Apertura) | 76 | 7823 | 13239 | 14271 | 50 | 43 / 7 | sim | 415911b | 24 | [par-1](par-1.md) |
| Campeonato Peruano | 109 (1912–2025) | 18 | 17318 | 20236 | 21067 | 167 | 51 / 39 | sim | 415911b | 22 | [per-1](per-1.md) |
| Campeonato Equatoriano | 68 (1957–2025) | 0 | 14175 | 9259 | 15883 | 63 | 48 / 20 | sim | 415911b | 18 | [ecu-1](ecu-1.md) |
| Campeonato Boliviano | 94 (1950–2025) | 22 | 8563 | 13666 | 4996 | 77 | 42 / 10 | sim | 415911b | 0 | [bol-1](bol-1.md) |
| Campeonato Venezuelano | 106 (1921–2025) | 25 | 13580 | 6400 | 6744 | 108 | 48 / 23 | sim | 415911b | 0 | [ven-1](ven-1.md) |

## Pendências de todas as competições

- **arg-1:** Correções da revisão feitas em 23/11 (ids em docs/coleta/pedidos-sulamerica.md): campeão e pódio (AR-001 a AR-016, QU-001), datas (AR-022, QU-002, AR-024), fases (AR-025, AR-026), jogos (AR-018, AR-034: o 1926 Amateurs passou de 43 para 325 jogos), artilheiros (AR-027 a AR-030), clubes (AR-031, AR-032, AR-033) e o Apertura 2026 (AR-043).
- **arg-1:** Ainda abertos: AR-020 (1929, W.O. que dão pontos na tabela do grupo), AR-021 (rebaixados por lista: BDFA e es), QU-003 (casar a ESPN pelo par de clubes nos jogos adiados), QU-005 (datas do Boca só com 3ª fonte).
- **arg-1:** Decisão do Guilherme pedida pela revisão e já respondida: 1891 só Saint Andrew's (D-07 b; o pacote já era assim).
- **uru-1:** Correções da revisão feitas em 23/11 (ids em docs/coleta/pedidos-sulamerica.md): classificação pela tabela anual de 1994 em diante, pódio pela lista da AUF, Supercopa fora, títulos da FUF e de 1926 sem campeão (D-09), clubes da FUF à parte (D-25 f), 2020 no ano certo, artilheiros (AUF 2013/14-2025; es 1900-1931).
- **chi-1:** Correções da revisão feitas em 23/11 (ids em docs/coleta/pedidos-sulamerica.md): coluna de bônus das tabelas de 1979-1983, 1988 e 1989, vice pela lista oficial, tabela publicada como classificação em 14 edições, desempates, liguillas pré-Libertadores fora, 2020 no ano certo, placares de 1990-1995, clubes (D-25 a e b) e artilheiros.
- **chi-1:** Ainda abertos: CH-006 (1984: 3º e 4º pelo quadrangular), CH-022 (grupos herdados), CH-023 (7 datas do ogol de 1969), CH-028 (baixar de novo o calendário do ogol de 1964, 1971, 1977 e 1982) e a 2ª parte do CH-014 (1986, adversários trocados: 3ª fonte).
- **col-1:** 1987 e 1991-1995 sem jogos: nenhuma fonte pública tem (só tabela final e campeão).
- **col-1:** Correções da revisão feitas em 23/11 (ids em docs/coleta/pedidos-sulamerica.md): vice pela colchamp, ordem por fase alcançada (D-02 A), tabelas finais de 1987 e 1991-1995 só com a Primera A, rebaixados pela es, 1964 sem jogos repetidos, Finalización e quadrangulares como fase de pontos, finais do Apertura em nível 0, datas de 1957 e 1971, artilheiros de 1971, 1977 e 1978.
- **col-1:** Ainda abertos: CO-004 e CO-006 (ler as 4 voltas e as listas 'Fecha N' da Wikipédia: 1955-1966, 1976, 1986, 1988, 1989), CO-009, CO-012, CO-013, CO-015, CO-016, CO-017 (2008 em diante pela es), CO-020, CO-022.
- **par-1:** 76 edições sem jogos (1906-1959, 1968-1980, 1982-1995 sem fonte pública): campeão, vice e tabela parcial quando há.
- **par-1:** Correções da revisão feitas em 23/11 (ids em docs/coleta/pedidos-sulamerica.md): campeão e vice da lista sempre em 1º e 2º (vice da es nos anos de vice duplo, D-22 a), tabelas parciais inteiras, 1982-1995 sem tabela de uma fase só, pré-temporada de 1962-1966 e copas de 2000, 2004 e 2005 fora, clubes (D-25 c e d), ESPN (gol sem lado, jogador '2', estádio sem patrocinador) e o Apertura 2026 (D-01).
- **par-1:** Ainda abertos: PY-008 (fases do Apertura e do Clausura de 1996-2007), PY-012 (rebaixados por ano), PY-018 (artilheiros de 2014 em diante), PY-019, PY-031 (textos da ficha).
- **per-1:** 1912-1921 (Liga Peruana): pela D-06 (A), as edições ficam com a ordem e os participantes das páginas peru1912-1921 (sem jogos, salvo os poucos de 1912 que não entram).
- **per-1:** Correções da revisão feitas em 23/11 (ids em docs/coleta/pedidos-sulamerica.md): tabela do ano inteiro como classificação (1970-1979, 1998, 2000, 2009, 2012, 2020 pós-TAS, 2021 com o TAS; soma em 2001, 2004, 2005), final de 2021, Jorge Chávez N°1 x do Callao, rebaixado só com 'Relegated', finais do Torneo de Verano, datas de 1990.
- **per-1:** Ainda abertos: PE-010 (a final nacional de 1990 como 'Final'), PE-012 (liguilla final de 1988), PE-014 (rebaixados por ano, pela es), PE-015 (artilheiros de 1996), PE-017 (placares só com 3ª fonte), PE-022 (cidade do Deportivo Bancos).
- **ecu-1:** ESPN sem lances de 2014 a 2020: gols com minuto e cartões desses anos só jogo a jogo (outra fonte).
- **ecu-1:** Correções da revisão feitas em 23/11 (ids em docs/coleta/pedidos-sulamerica.md): classificação com a soma de todos os jogos e a ordem da última fase de liga (D-02 A), disputa de 3º/4º lugar, rebaixados pela es (EC-004, EC-005), fases de 1963, 1966, 1997 e 1999, jogos repetidos de 1984, 1986 e 1994, W.O. de 1965 e de 2025 (D-20 c), datas.
- **ecu-1:** Abertos fechados em 23/11: EC-013 (gol da ESPN sem lado não entra) e EC-014 (artilheiro de 1988 com 19 gols, pela página do ano; 1996 e 1999 confirmados pelo El Universo).
- **bol-1:** Pedido do agente 1 (22/11, para quando o Guilherme mandar revisar): a classificação final de 1960, 1976, 1990, 1993 e 1994 deve trazer todos os clubes com jogos (eliminados com a posição da fase em que caíram), como no bra-sp-2.
- **bol-1:** 22 edições sem jogos (1952, 1954-1959 com o 1957 Mixto, 1961, 1963-1965, 1967, 1969, 1970, 1972-1975, 1980, 1981, 1984): nenhuma fonte pública tem; o nacional de 1960-1964 não tem nem tabela (só campeão e vice). Fonte que resolveria: jornais da época ou um almanaque boliviano (ex.: historiadelfutbolboliviano.com, de Carlos Mesa).
- **bol-1:** Jogos incompletos em 1951, 1960, 1966, 1968, 1971, 1976, 1978, 1979, 1982, 1983, 1985-1994: só as fases finais (ou jogos sem a divisão em fases, em 1990-1991). A tabela de confrontos parcial de 1992 ('Partial results', com células vazias) não foi lida: precisaria de leitura por coluna.
- **bol-1:** Vice de 1961, 1963, 1964 e 1968: RSSSF e Wikipédia em inglês divergem; ficou o da RSSSF (decisão do agente, explicada no relatório). Conferir numa terceira fonte.
- **bol-1:** Nomes que dependem do ano, a conferir: 'Universitario' sozinho de 1971 a 1994 = Universitario de Potosí; 'Litoral' de 1992 (a tabela da RSSSF diz [Oruro]) = Litoral de La Paz.
- **ven-1:** Ainda não carregado no banco (no GitHub desde o 35dc0a2).
- **ven-1:** Decisão do Guilherme: o Atlético Zulia (1996/97 e 1997/98, campeão de 1997/98) entrou como Universidad de Los Andes, como na lista de campeões da RSSSF; a página de 1996/97 diz que era o Unicol. Se valer a página, o título vai para o Unicol (ou para um 'Atlético Zulia' separado).
- **ven-1:** Era amadora (1921-1956): só 1940, 1955 e 1956 têm todos os jogos; 7 anos sem página (1922, 1924, 1931, 1938, 1939, 1949, 1950) e 26 com jogos parciais ou só a classificação. Fonte que resolveria: jornais de Caracas da época (El Universal, La Esfera) ou o livro de Eliézer Pérez, autor das páginas da RSSSF.
- **ven-1:** 1993/94 e 1994/95: a Copa Venezuela (Apertura de 1993/94) e o Torneo Iniciación (1994/95) só têm tabelas; 8 jogos da liga de 1993/94 sem placar e 5 'drw' (empate sem placar) em 1994/95.
- **ven-1:** Jogos que nenhuma fonte tem: Lara x Zamora (1992/93), Caroní x Zulia (Clausura 2011), Mineros x Zamora e Carabobo x Aragua (Apertura 2011); a tabela final dá o resultado de cada um (explicado no relatório).
- **ven-1:** Vice de 1966 e 1975: RSSSF e Wikipédia em inglês divergem; ficou o da RSSSF.
- **ven-1:** Artilheiros de 1974 e depois de 2007/08 só pela Wikipédia em inglês (a lista da RSSSF não tem).

## Próximas competições

- 2ªs divisões, na ordem do guia geral, só quando o Guilherme pedir. Como fazer: `COMECE-AQUI.md`, seção 4.
