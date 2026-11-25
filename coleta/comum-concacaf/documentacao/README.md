# Coleta CONCACAF — documentação

Gerado por `python coleta/comum-concacaf/documentar.py`. Uma ficha por competição, com tudo o que o pacote tem, como as edições foram definidas, fontes e regras, a conferência, a cobertura de cada campo década a década, o formato ao longo do tempo, campeões e vices, ajustes de pontos, todas as correções e decisões com o motivo, o que não deu para coletar e as pendências.

Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum-concacaf/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-concacaf.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-concacaf`).

| Competição | Edições | Sem jogos | Jogos | Gols c/ autor | Cartões | Clubes | Edições ok / div. | No banco | Commit | Achados abertos | Ficha |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Campeonato Mexicano | 158 (1902/03–2026 Clausura) | 2 | 26606 | 56671 | 42633 | 92 | 116 / 33 | sim | cb0355f8 | 0 | [mex-1](mex-1.md) |
| Campeonato Norte-Americano | 63 (1921/22–2025) | 35 | 8708 | 21918 | 30061 | 134 | 25 / 1 | sim | bb8432b4 | 0 | [usa-1](usa-1.md) |
| Campeonato Costarriquenho | 123 (1921–2026 Clausura) | 74 | 7065 | 2813 | 0 | 65 | 40 / 4 | sim | 17766bf6 | 0 | [crc-1](crc-1.md) |
| Campeonato Hondurenho | 89 (1965/66–2026 Clausura) | 35 | 5391 | 2529 | 0 | 55 | 47 / 5 | sim | 6e59e93f | 0 | [hon-1](hon-1.md) |
| Campeonato Guatemalteco | 101 (1942/43–2026 Clausura) | 48 | 6836 | 2954 | 0 | 73 | 48 / 3 | sim | 7fd2f616 | 0 | [gua-1](gua-1.md) |
| Campeonato Salvadorenho | 111 (1926–2026 Clausura) | 52 | 6026 | 2682 | 0 | 71 | 51 / 1 | não | — | 0 | [slv-1](slv-1.md) |

## Pendências de todas as competições

- **mex-1:** Decidido em 24/11 (pesquisa aprovada pelo Guilherme): o Pachuca AC da era amadora (1902-1922) é o Pachuca de hoje, como o clube conta a própria história; a RSSSF diz que o Pachuca AC se dissolveu em 1920. Se forem clubes diferentes, separar em clubes_mex.py (regra 'pachuca').
- **mex-1:** Decidido em 24/11 (pesquisa aprovada pelo Guilherme): Atlético Español (1971-1982) = Necaxa (o clube vendido e renomeado, que voltou a se chamar Necaxa); a temporada 1930/31, cancelada, entra sem campeão, com a tabela do cancelamento.
- **mex-1:** Edições sem jogos: 1911/12 e 1916/17 (a RSSSF não tem página; só a tabela final de mexhist.html). Jogos incompletos: 1915/16, 1924/25, 1920/21 e 1921/22 (as duas ligas). Fonte que resolveria: jornais da época (Hemeroteca Nacional Digital da UNAM, a fonte dos autores das páginas da RSSSF).
- **mex-1:** 1995/96: falta o Guadalajara x Pumas do 1º turno (não está na página); pela tabela, o Guadalajara venceu por 3-0.
- **mex-1:** Estádio só de 2002 em diante (ESPN) e nos jogos com "at X": as linhas de estádio das páginas da RSSSF ("Estadio Jalisco, Guadalajara", acima do jogo) ainda não são lidas.
- **mex-1:** Divergências de um gol ou de um resultado entre a página e a tabela dela em cerca de 30 edições: ficam como erro da página (o relatório diz qual clube e qual tabela).
- **usa-1:** ASL I (1921/22-1932/33), 1967 e NASL (1968-1984) só com as tabelas: a RSSSF não tem os jogos (os playoffs só em texto). Fonte que resolveria: os livros de Colin Jose ("NASL: A Complete Record", "The American Soccer League 1921-1931") ou jornais da época.
- **usa-1:** MLS 1997 e 1998 só com as tabelas: a RSSSF não tem os jogos e a ESPN começa em 2002. Fonte que resolveria: os arquivos de jogos da MLS (mlssoccer.com) ou a Wikipédia de cada temporada.
- **usa-1:** 2004: falta um DC United x New York Red Bulls (a ESPN não tem; a RSSSF só tem as tabelas).
- **usa-1:** Temporada 2026 da MLS: entra depois da final (18/12/2026).
- **usa-1:** Identidades a conferir pela revisão: Philadelphia Field Club de 1921/22 = Bethlehem Steel; os dois New York Giants da ASL (New York Soccer Club e New York Giants); os clubes da NASL separados dos da MLS com o mesmo nome.
- **crc-1:** 1921 a 1995/96 só com as tabelas (a RSSSF não tem os jogos; os poucos jogos de final ficaram de fora); 1991/92 e 1993/94 sem página (só campeão e vice). Fonte que resolveria: jornais da época (La Nación, Diario de Costa Rica) ou a UNAFUT.
- **crc-1:** Apertura 2010 a Clausura 2012: fase regular só com a tabela; a ESPN desses anos tem jogos adiados repetidos e jogos faltando.
- **crc-1:** Autores dos gols e cartões: a RSSSF quase não traz autores e a ESPN (crc.1) só traz gols, e em poucos anos; não há cartões. Fonte que resolveria: o site da UNAFUT ou o ogol.
- **crc-1:** Erros de um resultado na própria página em 1998/99 e 2000/01; derrota para os dois clubes em 2002/03 (San Carlos x Herediano); um jogo faltando em 2003/04: explicados no relatório.
- **hon-1:** 1965/66 a 1995/96 só com as tabelas finais (hondhist.html): a RSSSF não tem os jogos. Fonte que resolveria: jornais da época (La Prensa, El Heraldo) ou a Liga Nacional.
- **hon-1:** Apertura 2010 a Clausura 2012 só com as tabelas (a página da RSSSF não tem a fase regular).
- **hon-1:** Erros de um resultado na própria página em 1997 Apertura, 2002 Apertura, 2002 Clausura, 2005 Apertura e 2007 Clausura: explicados no relatório.
- **hon-1:** Liga Amateur de Honduras (1947-1964) fora do hon-1 (decisão de 24/11); se o Guilherme quiser, entra como competição própria.
- **gua-1:** 1942/43 a 1995/96 só com as tabelas (a RSSSF quase não tem os jogos). Fonte que resolveria: jornais da época (Prensa Libre, El Imparcial) ou a Liga Nacional.
- **gua-1:** Apertura 2010 a Clausura 2012 só com as tabelas (a página da RSSSF não tem a fase regular).
- **gua-1:** A lista de campeões não traz o vice: o vice é o 2º da classificação (conferir com outra fonte).
- **gua-1:** 1998/99: parte dos jogos do grupo do rebaixamento só com o resultado (sem placar).
- **slv-1:** 1942, 1943, 1946 e 1948/49 a 1995/96 só com as tabelas (e o campeão e o vice da lista); as finais desses anos que a RSSSF traz não entram. Fonte que resolveria: jornais da época (La Prensa Gráfica, El Diario de Hoy) ou a FESFUT.
- **slv-1:** Apertura 2010 a Clausura 2012 só com as tabelas (a página da RSSSF não tem a fase regular). A ESPN tem os Aperturas de 2010 e 2011 quase inteiros, mas não fecha com as tabelas (placares diferentes, um jogo faltando, um repetido): não foi usada; os Clausuras ela quase não tem.
- **slv-1:** 2002 Clausura: um gol de diferença entre os jogos e a tabela do Atlético Balboa (explicado no relatório).
- **slv-1:** Títulos só da Zona Central (1931-36, 1939-41, 1944-45) fora do slv-1 (decisão de 24/11); a tradição às vezes os conta como nacionais.
- **slv-1:** 2020/21 (pandemia, duas fases de grupos): a classificação junta os dois grupos da segunda fase (10 jogos por clube).

## Próximas competições

- 1ªs divisões da CONCACAF, na ordem do guia geral: usa-1, crc-1, hon-1, gua-1, slv-1, pan-1, jam-1, tri-1, can-1, hai-1; depois as outras. Antes de cada uma, as decisões de escopo ao Guilherme. Como fazer: `COMECE-AQUI.md`, seção 4.
