# Revisão — Campeonato Peruano, 1ª divisão (`per-1`)

Revisor PE, 22/11/2026 (3ª rodada, revisão profunda). Achados: `PE-001` a `PE-028`. Scripts em `revisao/PE/`.

**Resumo.** Campeões batem nas 109 edições; vices em 107 (1918 e 1921 apontam o Jorge Chávez N°1 em vez do Jorge Chávez do Callao, o Nr. 2).
O ponto fraco é a classificação final: 13 edições usam a tabela errada (uma fase só, ou a 1ª fase nos anos sem jogos), 2020 está antes da decisão do TAS e 2021 não tem a final nem os descontos; 8 edições marcam rebaixado quem só jogou o playoff.
Os placares batem com a Wikipédia es, a ESPN e o transfermarkt; o problema dos jogos são as datas: 86 finais e desempates herdam a data da última rodada. O per-1 está no banco e no painel local, ainda não no site.

## Estado

- Banco (`db/futebol.db`): 109 edições e 17.316 jogos, iguais ao pacote; campeão e vice do banco e do painel local iguais ao pacote nas 109.
- Site: `https://clubeanalitico.pages.dev/dados/per-1.js` devolve a página inicial: **não publicado** (PE-024). Telas vistas no painel local.

## A. Edições e títulos

- Conferido: lista de 109 edições, campeão e vice de todas, contra a Wikipédia es (Palmarés de "Primera División del Perú") e a RSSSF (`peruchamp`, `peru1912`-`peru1921`).
- Resultado: 109 campeões certos; 107 vices certos. **PE-001** (alta): vice de 1918 e 1921. **PE-026** (não é erro): vice de 1914, RSSSF diz Jorge Chávez No. 1, es e en dizem Sport Alianza. **PE-027** (não é erro): 1934 é do Universitario para FPF e ADFP (o Alianza reclama).
- 1912-1921: a RSSSF tem a classificação completa de 1912-1917 e a es tem tabelas; o pacote diz que não existe (**PE-019**, **PE-023**). Decisão PE-D1.

## B. Classificação final

- Conferido: todas as 109 classificações quanto à tabela usada (`revisao/PE/classif_parcial.py`), as tabelas acumuladas da Wikipédia es de 1927-2008 (`tabelas_es.py`), os anos sem jogos contra a `peruhist` da RSSSF, os ajustes de pontos de 2018-2025 e os rebaixados de 83 edições contra a seção "Ascensos y descensos" da es (`descensos_es.py`, `rebaixados.py`).
- Resultado:
  - **PE-008** (alta): 1998, 2000, 2001, 2004 e 2005 usam só o Clausura; 2009 e 2012, só a 1ª fase. O importador descarta a tabela acumulada.
  - **PE-002** (alta): 1970, 1972, 1973, 1974, 1977 e 1979 (sem jogos) usam a tabela da 1ª fase. Em 1970 o campeão aparece com 49 pontos e o vice com 56.
  - **PE-004** (alta): 2020 é a tabela anterior ao TAS. O Alianza aparece rebaixado; caíram Atlético Grau, Carlos Stein (-3) e Llacuabamba.
  - **PE-006** (alta): 2021 tem a tabela calculada, sem os descontos, com o Carlos Stein com 0 jogos e sem rebaixados. Pelo TAS, caíram Cusco FC e Alianza Universidad.
  - **PE-003** (alta): 8 edições marcam rebaixado quem só foi ao grupo ou ao playoff do rebaixamento (1938, 1970, 1977, 1979, 2002, 2006, 2008, 2014).
  - **PE-014** (media): cerca de 45 edições sem marca de rebaixado.
  - **PE-018** (media): pontos de 2022 diferem da es.
  - No painel, a queda é deduzida pela presença no ano seguinte, então PE-003 e PE-014 só aparecem no banco.
- Ajustes de 2023 (Garcilaso -1, Sport Boys -4, Municipal -5) batem com a es.

## C. Jogos

- Placares: 8.747 resultados da Wikipédia es (1930-2008, anos em que a coleta não a usou) casados com o pacote, 7.736 iguais. O resto são liguillas fora do escopo e anos incompletos (1984, 1986, 1991). Sobram cerca de 12 divergências reais sem terceira fonte (**PE-017**).
- Anos em que a fonte foi a es: 2.291 resultados da Wikipédia en, 2.172 iguais. As diferenças são outros torneios na mesma página.
- ESPN: 6.418 jogos de 2005-2025, 54 placares diferentes. Nos 4 testados no transfermarkt, o pacote está certo (**PE-028**).
- Amostra por década:
  - 1920: 193 jogos (en);
  - 1930: cerca de 400 (es);
  - 1940-1960: 2.000 (en) e 410 (es 1968-69);
  - 1970: 650 (es);
  - 1980: cerca de 2.000 (es);
  - 1990: cerca de 1.800 (es);
  - 2000: 2.500 (es) e a ESPN;
  - 2010 e 2020: ESPN e transfermarkt.
- Datas:
  - **PE-009** (media): 86 jogos de mata-mata com a data e a rodada do último jogo de liga. Contra a ESPN, 87 datas diferentes, 30 por mais de 1 dia.
  - **PE-010** (media): 1990 tem jogos de janeiro de 1991 gravados em 1990, e a final nacional (3/2/1991) aparece como "Final do Regional II".
- Fases:
  - **PE-005** (alta): falta a final nacional de 2021.
  - **PE-013** (media): a final do Torneo de Verano de 2017 e 2018 aparece como "Final".
  - **PE-011** (media): a "Regional Final" de 1987 e 1988 aparece como grupo Sul.
  - **PE-012** (media): em 1988, a liguilla está dentro da "Final".
  - **PE-007** (media): Cusco 3-0 Cienciano (2021) foi revertido pelo TAS para 2-2.
- Varredura de tela (`revisao/PE/varredura.py`): os achados estão acima. Os "2 jogos no mesmo dia" são as datas herdadas de PE-009.

## D. Gols e artilheiros

- Conferido: artilheiro de 97 edições contra a Wikipédia es e a en.
- Resultado:
  - 87 iguais;
  - **PE-015** (media): 1996 tem dois artilheiros com 20 gols (Czornomaz e Sáenz);
  - **PE-016** (baixa): 7 anos divergem por critério (a es parece somar Regional e Descentralizado);
  - 1972 e 1973: só a grafia (Gonzales x Gonzalez).
- A maior goleada (Unión Comercio 0-12 Sporting Cristal, 27/10/2024) bate com a ESPN.

## E. Clubes e escudos

- Conferido: os 153 clubes do cadastro (147 no painel): nomes, fusões e cidades.
- Resultado:
  - vice de 1918 e 1921 ligado ao clube errado (PE-001);
  - **PE-021**: Sporting Tabaco é do Rímac (Lima), não do Callao;
  - **PE-022**: Deportivo Bancos está sem cidade;
  - sem duplicados nem homônimos juntados na amostra.
- Escudos: 33 de 147 clubes têm escudo; olhei os 33 numa folha de contato e todos estão certos. **PE-020**: 114 clubes sem escudo, entre eles 8 campeões (Atlético Chalaco, Mariscal Sucre, Unión Huaral...).

## F. Painel

- Telas (Chrome sem janela, painel local):
  - História: Pódio e Curiosidades;
  - Por campeonato: Classificação 1970 e 2021, Resumo 2017, Jogos 2017 e 2023, Participantes 2020;
  - celular, Jogos 2017.
- Resultado:
  - a tela de 1970 mostra o campeão com menos pontos que o vice (PE-002);
  - a de 2021 mostra o Carlos Stein com zeros (PE-006);
  - em 2017, "Como foi a disputa" e "Jogos" mostram a final do Verano como final do campeonato (PE-013);
  - no celular, a página fica mais larga que a tela (PE-025, já conhecido);
  - a ficha da coleta diz "No banco: sim" e "Ainda não carregado" ao mesmo tempo (PE-023).

## Fontes

- RSSSF:
  - https://www.rsssf.org/tablesp/peruhist.html
  - https://www.rsssf.org/tablesp/peru1912.html a peru1921.html
  - https://www.rsssf.org/tablesp/peru2020.html , peru2021.html , peru90.html , peru87.html , peru88.html
- Wikipédia es: https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_del_Per%C3%BA e as 110 páginas de temporada (cache em `data/cache/revisao/PE/`).
- Wikipédia en: páginas de temporada de 1926-1965.
- transfermarkt: https://www.transfermarkt.com/liga-1-clausura/gesamtspielplan/wettbewerb/TDeC/saison_id/2013
- ESPN `per.1`: `data/coleta/per-1/espn/`.
- Avaliação das fontes: `fontes_PE.md`; plano de correção: `plano_PE.md` (no scratchpad da revisão).

## Perguntas ao Guilherme

1. **1912-1921 (Liga Peruana amadora):** manter e completar com a classificação da RSSSF/es, com a etiqueta "Liga Peruana" (recomendado: é a conta da FPF, da ADFP e dos clubes, com Alianza 25); deixar só campeão e vice; ou tirar (conta da RSSSF, Alianza 23)? Detalhe em `decisoes_PE.md` (PE-D1).
