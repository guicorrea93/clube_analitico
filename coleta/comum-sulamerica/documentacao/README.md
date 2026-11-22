# Coleta América do Sul — documentação

Gerado por `python coleta/comum-sulamerica/documentar.py`. Uma ficha por competição, com tudo o que o pacote tem, como as edições foram definidas, fontes e regras, a conferência, a cobertura de cada campo década a década, o formato ao longo do tempo, campeões e vices, ajustes de pontos, todas as correções e decisões com o motivo, o que não deu para coletar e as pendências.

Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum-sulamerica/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-sulamerica.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-sulamerica`).

| Competição | Edições | Sem jogos | Jogos | Gols c/ autor | Cartões | Clubes | Edições ok / div. | No banco | Commit | Achados abertos | Ficha |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Campeonato Argentino | 196 (1891–2025 Liga) | 1 | 43235 | 34264 | 37037 | 171 | 136 / 54 | sim | 665fe93 | 36 | [arg-1](arg-1.md) |
| Campeonato Uruguaio | 126 (1900–2025) | 45 | 12464 | 14309 | 9396 | 81 | 59 / 22 | sim | 0ead727 | 19 | [uru-1](uru-1.md) |
| Campeonato Chileno | 109 (1933–2025) | 0 | 22601 | 18878 | 25361 | 53 | 65 / 43 | sim | 36e0690 | 0 | [chi-1](chi-1.md) |
| Campeonato Colombiano | 101 (1948–2025 Finalización) | 6 | 22788 | 22020 | 40449 | 42 | 48 / 38 | sim | 3f5c1d0 | 0 | [col-1](col-1.md) |
| Campeonato Paraguaio | 133 (1906–2025 Clausura) | 76 | 7865 | 13108 | 14270 | 43 | 36 / 12 | sim | 0b793ba | 0 | [par-1](par-1.md) |
| Campeonato Peruano | 109 (1912–2025) | 18 | 17316 | 20222 | 20999 | 153 | 52 / 38 | sim | 0b793ba | 0 | [per-1](per-1.md) |
| Campeonato Equatoriano | 68 (1957–2025) | 0 | 14195 | 9240 | 15824 | 63 | 47 / 21 | sim | 0b793ba | 0 | [ecu-1](ecu-1.md) |
| Campeonato Boliviano | 94 (1950–2025) | 22 | 8563 | 13666 | 4970 | 77 | 42 / 10 | não | 9ed3dcd | 0 | [bol-1](bol-1.md) |

## Pendências de todas as competições

- **arg-1:** Achados da revisão em aberto (36, prefixo AR; lista na seção 9): vices errados em 12 edições, campeão de 1913 Federación, datas com ano errado (~3.920 jogos), fases, artilheiros e clubes. Corrigir e citar os ids em docs/coleta/pedidos-sulamerica.md.
- **arg-1:** Decisões do Guilherme pedidas pela revisão: título de 1891 (só Saint Andrew's ou dividido), Apertura 2026, Quilmes de 1893-1895, fusões de 1934, Copa de Oro de 1936.
- **uru-1:** Achados da revisão em aberto (19, prefixo UY; lista na seção 9): a classificação final de 1994-2025 é a tabela do Apertura (UY-006, que puxa vice e 3º errados), Supercopa dentro da Final, datas das decisões, artilheiros. Corrigir e citar os ids em docs/coleta/pedidos-sulamerica.md.
- **uru-1:** Decisões do Guilherme pedidas pela revisão: títulos da FUF (1923, 1924) e do Consejo Provisorio (1926); Atlético Wanderers da FUF = Montevideo Wanderers?; vice de 1954.
- **col-1:** 1987 e 1991-1995 sem jogos: nenhuma fonte pública tem (só tabela final e campeão).
- **par-1:** 76 edições sem jogos (1906-1959, 1968-1980, 1982-1995 sem fonte pública): campeão, vice e tabela parcial quando há.
- **par-1:** Pacote reimportado em 21/11 (leitor comum: clubes com nome de data): +55 jogos de 2005-2014 e ids das partidas mudados; o agente 1 precisa recarregar o pacote inteiro (recado de 21/11, seção do ecu-1).
- **per-1:** Decisão para o agente 1/Guilherme: 1912-1921 (Liga Peruana) entraram como 10 edições só com campeão e vice (conta da Wikipédia); se valer a conta da RSSSF, tirar essas edições.
- **per-1:** 18 edições sem jogos (1912-1921, 1970-1974, 1976, 1977, 1979) e jogos incompletos em 1926, 1982, 1984, 1986, 1988-1991 e 2003: nenhuma fonte pública tem o resto.
- **per-1:** Ainda não carregado no banco.
- **ecu-1:** Ainda não carregado no banco (no GitHub desde o 0b793ba).
- **ecu-1:** ESPN sem lances de 2014 a 2020: gols com minuto e cartões desses anos só jogo a jogo (outra fonte).
- **bol-1:** Ainda não carregado no banco (no GitHub desde o 9ed3dcd).
- **bol-1:** 22 edições sem jogos (1952, 1954-1959 com o 1957 Mixto, 1961, 1963-1965, 1967, 1969, 1970, 1972-1975, 1980, 1981, 1984): nenhuma fonte pública tem; o nacional de 1960-1964 não tem nem tabela (só campeão e vice). Fonte que resolveria: jornais da época ou um almanaque boliviano (ex.: historiadelfutbolboliviano.com, de Carlos Mesa).
- **bol-1:** Jogos incompletos em 1951, 1960, 1966, 1968, 1971, 1976, 1978, 1979, 1982, 1983, 1985-1994: só as fases finais (ou jogos sem a divisão em fases, em 1990-1991). A tabela de confrontos parcial de 1992 ('Partial results', com células vazias) não foi lida: precisaria de leitura por coluna.
- **bol-1:** Vice de 1961, 1963, 1964 e 1968: RSSSF e Wikipédia em inglês divergem; ficou o da RSSSF (decisão do agente, explicada no relatório). Conferir numa terceira fonte.
- **bol-1:** Nomes que dependem do ano, a conferir: 'Universitario' sozinho de 1971 a 1994 = Universitario de Potosí; 'Litoral' de 1992 (a tabela da RSSSF diz [Oruro]) = Litoral de La Paz.

## Próximas competições

- `ven-1` (Venezuela), só com o ok do Guilherme. Como fazer: `COMECE-AQUI.md`, seção 4.
