# Coleta América do Sul — documentação

Gerado por `python coleta/comum-sulamerica/documentar.py`. Uma ficha por competição, com tudo o que o pacote tem, como as edições foram definidas, fontes e regras, a conferência, a cobertura de cada campo década a década, o formato ao longo do tempo, campeões e vices, ajustes de pontos, todas as correções e decisões com o motivo, o que não deu para coletar e as pendências.

Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum-sulamerica/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-sulamerica.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-sulamerica`).

| Competição | Edições | Sem jogos | Jogos | Gols c/ autor | Cartões | Clubes | Edições ok / div. | No banco | Commit | Achados abertos | Ficha |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Campeonato Argentino | 197 (1891–2026 Apertura) | 1 | 43726 | 36043 | 41255 | 173 | 142 / 51 | sim | 30f0b00 | 41 | [arg-1](arg-1.md) |
| Campeonato Uruguaio | 126 (1900–2025) | 45 | 12456 | 14319 | 9396 | 84 | 59 / 22 | sim | 0ead727 | 21 | [uru-1](uru-1.md) |
| Campeonato Chileno | 109 (1933–2025) | 0 | 22601 | 18878 | 25361 | 53 | 65 / 43 | sim | 36e0690 | 26 | [chi-1](chi-1.md) |
| Campeonato Colombiano | 101 (1948–2025 Finalización) | 6 | 22788 | 22020 | 40449 | 42 | 48 / 38 | sim | 3f5c1d0 | 22 | [col-1](col-1.md) |
| Campeonato Paraguaio | 133 (1906–2025 Clausura) | 76 | 7865 | 13108 | 14270 | 43 | 36 / 12 | sim | 0b793ba | 24 | [par-1](par-1.md) |
| Campeonato Peruano | 109 (1912–2025) | 18 | 17316 | 20222 | 20999 | 153 | 52 / 38 | sim | 0b793ba | 22 | [per-1](per-1.md) |
| Campeonato Equatoriano | 68 (1957–2025) | 0 | 14195 | 9240 | 15824 | 63 | 47 / 21 | sim | 0b793ba | 18 | [ecu-1](ecu-1.md) |
| Campeonato Boliviano | 94 (1950–2025) | 22 | 8563 | 13666 | 4970 | 77 | 42 / 10 | sim | 9ed3dcd | 0 | [bol-1](bol-1.md) |
| Campeonato Venezuelano | 106 (1921–2025) | 25 | 13582 | 6390 | 6729 | 108 | 48 / 23 | sim | 35dc0a2 | 0 | [ven-1](ven-1.md) |

## Pendências de todas as competições

- **arg-1:** Correções da revisão feitas em 23/11 (ids em docs/coleta/pedidos-sulamerica.md): campeão e pódio (AR-001 a AR-016, QU-001), datas (AR-022, QU-002, AR-024), fases (AR-025, AR-026), jogos (AR-018, AR-034: o 1926 Amateurs passou de 43 para 325 jogos), artilheiros (AR-027 a AR-030), clubes (AR-031, AR-032, AR-033) e o Apertura 2026 (AR-043).
- **arg-1:** Ainda abertos: AR-020 (1929, W.O. que dão pontos na tabela do grupo), AR-021 (rebaixados por lista: BDFA e es), AR-023 (data no título da fase: mudança no leitor comum, junto com UY-014, CH-012, CO-008, PY-009, PE-009, EC-009), QU-003 (casar a ESPN pelo par de clubes nos jogos adiados), QU-005 (datas do Boca só com 3ª fonte).
- **arg-1:** Decisão do Guilherme pedida pela revisão e já respondida: 1891 só Saint Andrew's (D-07 b; o pacote já era assim).
- **uru-1:** Correções da revisão feitas em 23/11 (ids em docs/coleta/pedidos-sulamerica.md): classificação pela tabela anual de 1994 em diante, pódio pela lista da AUF, Supercopa fora, títulos da FUF e de 1926 sem campeão (D-09), clubes da FUF à parte (D-25 f), 2020 no ano certo, artilheiros (AUF 2013/14-2025; es 1900-1931).
- **uru-1:** Ainda aberto: UY-014 (data das decisões no título da fase: leitor comum, junto com as outras ligas no fim).
- **col-1:** 1987 e 1991-1995 sem jogos: nenhuma fonte pública tem (só tabela final e campeão).
- **par-1:** 76 edições sem jogos (1906-1959, 1968-1980, 1982-1995 sem fonte pública): campeão, vice e tabela parcial quando há.
- **per-1:** Decisão para o agente 1/Guilherme: 1912-1921 (Liga Peruana) entraram como 10 edições só com campeão e vice (conta da Wikipédia); se valer a conta da RSSSF, tirar essas edições.
- **per-1:** 18 edições sem jogos (1912-1921, 1970-1974, 1976, 1977, 1979) e jogos incompletos em 1926, 1982, 1984, 1986, 1988-1991 e 2003: nenhuma fonte pública tem o resto.
- **ecu-1:** ESPN sem lances de 2014 a 2020: gols com minuto e cartões desses anos só jogo a jogo (outra fonte).
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
