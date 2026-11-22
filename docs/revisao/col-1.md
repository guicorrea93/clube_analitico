# Revisão — Campeonato Colombiano (`col-1`)

Revisão profunda (3ª rodada), 22/11/2026. Prefixo dos achados: CO. Scripts em `revisao/CO/`, saídas `revisao/CO/saida_*.txt`.

**Resumo.** Os 101 campeões estão certos, mas o vice está errado em 55 edições (o pacote usa o 2º da tabela da 1ª fase) e a
classificação final é a da 1ª fase em quase todos os torneios com final; 6 edições sem jogos aparecem com tabela zerada.
Faltam ~1.400 jogos (metade de 1955-1963, quase todo 1989, parte de 1976, 1986 e 1988) e 1964 tem 155 jogos duplicados; 45 de 46
rebaixamentos não estão marcados. Tudo isso está no ar. 25 achados abertos: 7 alta, 11 média, 7 baixa (+3 verificados como certos).

Pacote = banco = site: `painel/dados/col-1.js` é idêntico ao publicado (https://clubeanalitico.pages.dev/dados/col-1.js) e campeão/vice
do banco são os do pacote nas 101 edições.

## A. Edições e títulos
- **Conferido:** campeão e vice das 101 edições contra a RSSSF `colchamp.html` (coluna Runners Up, que a coleta não leu) e a
  Wikipédia es (Categoría Primera A, Títulos por temporada) — `revisao/CO/campeoes.py`.
- **Resultado:** campeões 101/101 certos (CO-026). Vices: 46/101 certos — **CO-001** (lista em `revisao/CO/lista_vices.txt`: 1955,
  1957, 1958, 1959, 1961, 1969, 1970, 1976, 1978, 1979, 1981, 1982, 1984, 1989, 1992-1994, 1995/96, 1996/97, 2000, 2001 e 34 dos 47
  torneios curtos de 2002 a 2025). 1989 mostra vice (Atlético Nacional) sem haver campeão. As duas fontes concordam nas 101.
- Nº de clubes: 1986 (8 x 14), 1989 (8 x 15), 1995 (19 x 16) — **CO-019**.
- Fontes: https://www.rsssf.org/tablesc/colchamp.html ; https://es.wikipedia.org/wiki/Categor%C3%ADa_Primera_A

## B. Classificação final
- **Conferido:** origem da classificação de cada edição (código `importar.classificacao()`), tabelas anuais da RSSSF x soma dos jogos
  1948-1967 (`tabela_anual.py`, 20 anos), anos sem jogos (6), rebaixados 1992-2025 (`rebaixados.py`, 46), bônus e punições (grep nas 79 páginas).
- **CO-002** (alta): de 2002 em diante (e 1967, 1976, 1996/97, 1999-2001) a classificação é a tabela da 1ª fase com só o campeão no 1º;
  o vice e o 3º saem errados e semifinalistas aparecem em 5º-8º (ex.: 2002 Ap, Atlético Nacional finalista em 4º; print
  `SCRATCH/CO/telas/c_2002_Apertura_classificacao.png`).
- **CO-003** (alta): 1987 e 1991-1995 com tudo zero e em ordem alfabética; 1995 com 3 clubes da Primeira B (Bucaramanga, Real
  Cartagena, Unicosta). A RSSSF tem as tabelas, mas elas não entram (nenhuma linha em `tabelas_publicadas.csv`).
- Classificação calculada de anos com jogos faltando ou sobrando (1955-1966, 1976, 1986, 1988, 1989, 1964): CO-004, CO-005, CO-006.
- **CO-007** (alta): só 1 rebaixado marcado (Boyacá Chicó, 2021 Ap); faltam 45 (`revisao/CO/saida_rebaixados.txt`).
- **CO-016** (média): bônus das fases finais (1983-1999) não aplicados; Tuluá -2 em 1995. Ajustes certos: 2011 Fi Quindío -3, 1996/97.
- Fontes: https://www.rsssf.org/tablesc/col95.html ; https://es.wikipedia.org/wiki/Anexo:Ascensos_y_descensos_de_la_Categor%C3%ADa_Primera_A

## C. Jogos
- **Amostra por década** (`amostra_wiki.py`), sempre contra fonte que não foi a base da coleta naquele ano:
  - 1940s: Cross-Table RSSSF 1948 (88 de 90 batem) e 1949 (177 de 182);
  - 1950s: sem fonte de jogos independente; conferido o total por clube com a tabela RSSSF (1955, 1958, 1959: faltam jogos);
  - 1960s: Cross-Table RSSSF 1960 (109 de 220 casam: o pacote tem só metade); totais por clube 1960-1967;
  - 1970s: jogos das fases finais RSSSF 1974-1979 (172 de 185; 1976: faltam 10 do hexagonal);
  - 1980s: sem fonte de jogos independente; totais por fase com a RSSSF (1986, 1988, 1989 incompletos);
  - 1990s-2000s: Wikipédia es 1998, 2001, 2005 Ap (171/188); 2010s: 2009 Fi, 2016 Ap (210/213); 2020s: 2022 Fi (224/226);
  - ESPN 2005-2025: 7.968 jogos casados, data igual em 97%.
  - Total: 1.312 jogos batem, 217 diferem (quase todos datas de finais e jogos que faltam).
- **CO-004** (alta): faltam jogos em 1955 (45), 1958 (90), 1959 (134), 1960 (132), 1961 (132), 1963 (156), 1966 (14).
- **CO-005** (alta): 1964 com 467 jogos (312 reais): a matriz e a lista por rodada da Wikipédia foram lidas as duas.
- **CO-006** (alta): 1986 (21 jogos, 8 clubes), 1988 (Finalización com 12 de 28 jogos por clube), 1989 (32 de 318), 1976 (hexagonal 20 de 30).
- **CO-008** (média): ~150 jogos de mata-mata (48 edições, 1995/96-2024) com a data e a rodada herdadas ("First Leg [Dec 18]" não lido).
- **CO-009** (média): 2025 Fi, final ligada a jogos da ESPN do Apertura (data, hora, público e cartões errados).
- **CO-010** (média): datas com o ano errado (final de 1957 e desempate de 1971).
- **CO-011/012/013/014** (média): Finalización e quadrangulares gravados como mata-mata; grupos errados (todos "B"; 425 jogos da 1ª
  fase com grupo, painel diz "2 grupos"); 1957 com o octogonal cancelado como fase válida; finais do Apertura como "Desempate do título".
- **CO-015** (média): placares divergentes (1948-1949 pela Cross-Table; 1974, 1977, 1979, 2001 e 6 jogos com a ESPN).
- **CO-020** (baixa): datas vazias 1952-1988 que a Wikipédia tem no título da rodada; **CO-021** (baixa): jogos suspensos duplicados.
- Varredura de tela: `revisao/CO/saida_varredura.txt` (186 linhas) e `saida_datas_repetidas.txt` (48 edições).
- Seção 7 da ficha: `explicacoes.py` está vazio (nenhuma correção para amostrar); as 38 divergências só têm a frase automática —
  **CO-022** (baixa). As identidades de clube (6 casos) foram conferidas e estão certas (CO-028).

## D. Gols e artilheiros
- **Conferido:** artilheiro de 100 edições contra a Wikipédia es e a RSSSF coltops; soma dos gols com autor x placar em todos os jogos.
- **CO-017** (média): 73/100 batem; faltam 1977, 1978, empate de 1971 e 10 torneios de 2009-2018; 8 com nome/gols diferentes.
- **CO-018** (média): 3 jogos com mais gols com autor que o placar (2007 Ap, 2008 Fi, 2010 Ap).

## E. Clubes e escudos
- **Conferido:** os 42 clubes contra todos os clubes do banco (nomes únicos; homônimos com cidade); folha de contato com todos
  (`SCRATCH/CO/escudos.png`, 34 com escudo).
- Nomes e identidades certos (CO-028). **CO-023** (baixa): Huracán de Medellín com o escudo do Huracán argentino. **CO-024** (baixa):
  8 clubes sem escudo.

## F. Painel (site)
- **Conferido:** 50 prints do site (`revisao/CO/telas.sh`): 7 sub-abas da História, 5 sub-abas de 7 edições (2025 Fi, 2002 Ap, 1964,
  1976, 1995, 1989, 1960), 3 clubes, celular.
- Os erros de A-C aparecem no site: Pódio (Nacional com 15 vices), 2002 Ap pódio com Deportivo Cali em 2º, "Primeira fase: grupos · 2
  grupos", "Quadrangulares: mata-mata", 1964 com J=72, 1995 zerado.
- Recordes (Curiosidades) certos (CO-027). **CO-025** (baixa, já conhecido): celular mais largo que a tela.

## Perguntas ao Guilherme
1. **CO-D1:** o rebaixamento do Deportivo Pereira em 1997 (Torneo Adecuación, fora do pacote): marcar na edição 1996/97 com
   observação (recomendado), incluir o Adecuación como fase, ou não marcar?
2. **CO-D2:** ordem da classificação final dos torneios com fase final: por fase alcançada e depois a tabela da 1ª fase (recomendado),
   só a 1ª fase com campeão e vice no topo, ou a reclasificación?

Detalhes, opções e provas: `decisoes_CO.md`; plano de correção: `plano_CO.md`; fontes: `fontes_CO.md` (scratchpad da revisão).
