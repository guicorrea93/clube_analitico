# Revisão: Brasileirão Série D (`bra-serie-d`)

Revisor SD, 20/11/2026. Achados SD-001 a SD-021 (CSV entregue ao agente principal).

**Resumo.** Os placares estão quase todos certos (4.183 jogos de grupos e 408 confrontos de mata-mata iguais à Wikipédia; só 1 placar diferente).
O problema está na estrutura das fases de 2020, 2021 e 2022 e nas classificações calculadas: **2020 tem o vice errado** e **2020 e 2021 têm o pódio errado**.
Faltam ainda a edição de 2026 (já terminada) e 12 punições de pontos; o painel mostra artilheiros parciais em vez dos oficiais.

A Série D está no banco (`competicao_id` 6, 17 edições, 5.422 jogos, 13.148 gols, 11.228 com autor) e no seletor do painel. Fontes da coleta:
RSSSF e ogol. Conferi com a Wikipédia pt e en (páginas de cada edição e a página da competição). A API de busca da Wikipédia deu 429, então
baixei o texto das páginas com `action=raw`. Cópias em `data/cache/revisao/SD/`; scripts em `revisao/SD/`.

## A. Edições e títulos

- **Conferido:** a lista de edições (17); o campeão, o vice e os dois semifinalistas de todas as edições; os 4 que subiram em todas (sub-aba
  Participantes, que olha a Série C do ano seguinte, e o campo `situacao` do banco). Fontes: as tabelas de campeões, promovidos e artilheiros
  da página en e o texto e as predefinições da página pt.
- **Resultado:**
  - campeões: 17 de 17 certos;
  - vices: 16 de 17 (**SD-002**: 2020 é Floresta-CE, não Brasiliense);
  - semifinalistas: 15 de 17 (2020 e 2021 errados, SD-002 e SD-003);
  - quem subiu: os clubes estão certos em 2009–2024 (2011 com o Treze pelo tribunal, 2010 com o Joinville; ver SD-021). Mas em 2020 e 2021
    os promovidos aparecem em 10º a 14º. O `situacao` do banco está errado em 2025 e 2020 (SD-017). Em 2025 o painel não mostra quem subiu,
    porque a Série C 2026 não está no banco.
  - **SD-001:** falta a Série D 2026, que terminou em 13/09/2026 (campeão Uberlândia).
- Nenhum título controverso.

## B. Classificação final

- **Conferido:** todas as linhas das 17 edições (944 linhas) contra a "Classificação geral" da Wikipédia pt. Em 2012–2015 a fonte é a
  predefinição "Tabela do Campeonato Brasileiro da Série D - ano". Comparei a posição, J, V, E, D, GP, GC e os pontos. Script:
  `revisao/SD/classif.py`.
- **Resultado:**
  - batem inteiras (fora erros de digitação da própria Wikipédia): 2011, 2016, 2018, 2022 e 2023;
  - **2020 e 2021:** posições quase todas erradas, mas os números de cada clube batem (SD-002, SD-003);
  - **punições do STJD que faltam** em 2009, 2010, 2012, 2013, 2014, 2015 e 2019, num total de 12 casos (SD-014);
  - **punição no clube errado:** 2017 (São Raimundo-RR em vez do São Raimundo-PA, SD-015) e 2025 (Maricá em vez do Maracanã-CE, SD-016);
  - 2024: Manaus e Princesa estão fora do lugar por causa do placar de SD-010;
  - empates de pontos em ordem diferente, sem importância: 2009 (posições 28–31) e 2011 (38–39).
- **Casos de tribunal conferidos e certos (SD-021):** América-AM e Joinville em 2010, Treze em 2011, jogo anulado de 2011 e Aparecidense
  excluída em 2013.

## C. Jogos

- **Total de jogos por edição:** os 17 batem com o infobox da Wikipédia. A exceção é 2014: o banco tem 200 e a pt diz 199, porque não conta
  os W.O. (SD-013).
- **Placares da fase de grupos:** 2009 e 2012–2019 pelas matrizes de resultados da pt; 2020–2025 pelo módulo de resultados da en. São
  4.183 jogos iguais. As poucas diferenças que restaram vieram de matrizes da pt com erro, desmentidas pela tabela do grupo na en, ou de
  nomes que o script não casou. Uma é real: **Princesa x Manaus 2024**, que a en e o ogol dão 3-3 e o banco dá 0-1 (SD-010). Script:
  `revisao/SD/jogos_grupos.py`.
- **Mata-mata:** 408 confrontos iguais (ida e volta) em todas as edições, pelo `TwoLegResult` e pelas chaves da en e da pt. Os que não
  casaram são nomes que o script não reconheceu, menos os 4 jogos de 2021 (SD-004). Script: `revisao/SD/jogos_matamata.py`.
- **Datas:** 311 jogos com data e placar iguais, tirados das tabelas da pt com data (maiores públicos, hat-tricks, finais), de todas as
  edições. Script: `revisao/SD/datas.py`. Duas datas estão erradas de verdade: a semifinal de 2013 aparece antes das quartas (SD-011) e a
  data da final de 2016 está errada (SD-012). As outras diferenças são linhas de outras tabelas da Wikipédia ou erros dela.
- **Estrutura das fases:**
  - 2020 sem grupos e sem mata-mata separado (SD-005);
  - 2022 sem grupos (SD-006);
  - grupos perdidos em 2016, 2017 e 2018 (SD-007);
  - final rotulada errado em 2011 e 2013 (SD-008);
  - nomes em inglês e observações cruas (SD-009).
- **W.O.:** 2009, 2010 e 2020 estão marcados (`awd`). Os 3 de 2014 não estão (SD-013).

## D. Gols e artilheiros

- **Artilheiro oficial de todas as edições:** o banco e a Wikipédia pt e en conferem nos 21 nomes (com os empates), nos clubes e nos gols.
  Os nomes vêm com "- " na frente em 13 linhas (SD-018).
- **Painel:** o cartão "Artilheiro" e a Artilharia usam só os gols com autor. Saem errados em 7 edições e vazios em 2012 (SD-019,
  banco-painel).
- **Gols com autor ≤ placar:** conferido em todos os 5.422 jogos, nenhum passa do placar. Também não há jogo com autoria parcial: ou todos os
  gols têm autor, ou nenhum.

## F. Painel

- **Telas abertas** no Chrome sem janela, a 1400 px e no celular (420 px):
  - História: corrida, pódio, participações, jogos e vitórias, gols, pontos e curiosidades;
  - Por campeonato: resumo e classificação de 2020, resumo de 2013 e 2018, participantes, corrida, jogos, artilharia e classificação de 2021;
  - Por clube: as 5 sub-abas, no clube padrão (Central);
  - celular: 4 telas.
- **Erros de JavaScript:** nenhum, em 6 rotas.
- **Números conferidos com o banco:** os cartões do topo (17 edições, 312 clubes, 5.422 jogos, 13.148 gols) e a ficha do Central (116 jogos,
  42 V, 39 E, 35 D, 138 gols pró e 115 contra, posições ano a ano). Os recordes (10-0 Brasiliense x Interporto, 0-9 São Caetano x Pelotas,
  10-2 Trem x Náutico-RR) conferem com a página pt da competição.
- **Erros que aparecem no painel:**
  - pódio e corrida de vices com Brasiliense (vice em 2020 e 3º em 2021), por SD-002 e SD-003;
  - "Como foi a disputa" errado em 2011, 2013, 2018, 2020 e 2022 (SD-005 a SD-008);
  - fases em inglês (SD-009);
  - artilheiro (SD-019);
  - celular mais largo que a tela, já conhecido (SD-020).
- **Observação para o revisor de clubes (bloco E), não registrada aqui:** clubes renomeados aparecem com o nome atual. Exemplos: Uniclinic
  (2016–2017) como "Atlético Cearense", Betim (2014) como "Ipatinga", Corinthians Paranaense (2009) como "J.Malucelli".

## Perguntas ao Guilherme

1. A Série D 2026 já terminou (campeão Uberlândia, 96 clubes, 6 acessos). Quer que a coleta inclua agora (SD-001)?

## Quem corrige

- **coleta-brasil:** SD-001 a SD-018. O pacote é a origem de tudo isto: fases, grupos e classificações calculadas (`partidas.csv`,
  `fases.csv`, `classificacao_final.csv`) e punições e nomes (`classificacao_final.csv`, `artilheiros.csv`). Conferi que o banco e o
  `painel/dados/bra-serie-d.js` repetem o pacote.
- **banco-painel:** SD-019 (usar a tabela `artilheiro` no cartão e na Artilharia) e SD-020.
