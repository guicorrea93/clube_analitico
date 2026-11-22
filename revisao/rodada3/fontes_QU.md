# Fontes avaliadas: Argentino (arg-1) e Uruguaio (uru-1)

Revisor QU, 22/11/2026. A coleta usou RSSSF, ogol, ESPN e Wikipédia es (Uruguai); as revisões anteriores usaram Wikipédia es e en.
Tudo abaixo foi testado por curl/Python com 1 pedido a cada 2-3 s, cache em `data/cache/revisao/QU/`. Scripts em `revisao/QU/`.

### historiadeboca.com.ar (Historia de Boca Juniors)
- endereço: https://historiadeboca.com.ar/campeonato-1928/1928/1012.html (campanha de um torneio); ficha de jogo:
  https://historiadeboca.com.ar/partido/newell_s-0-boca-2-temporada-1989-90/2321/1990/36/29.html. A lista de torneios de um ano vem de
  `anios-campeonatos.php?anios=<ano>` e o endereço da campanha do redirecionamento de `validarcamp.php` (POST anios, comboCampeonato).
- cobre: todos os jogos do Boca Juniors de 1905 a 2026, por torneio: data, rodada (Fecha N), placar, estádio, mando; na ficha do
  jogo: árbitro, escalações, substituições e autores dos gols. Separa o que o banco mistura: "Campeonato (Anulado)" de 1919, os desempates
  ("Desempate 1er. Puesto 1ra. Rueda" de 1937), as copas.
- como baixar: em lote por torneio (1 página por campanha, ~35 jogos; mais 2 pedidos para achar o endereço); fichas jogo a jogo.
  HTML. Baixador: `revisao/QU/baixar_hdb.py <anos>`; comparador: `revisao/QU/cmp_hdb.py`.
- amostra: 1.278 jogos do Boca em 54 edições (1913 a 2025) casados com o banco. Placar: 1.270 iguais (99,4%); as 8 diferenças são 4 jogos
  anulados de 1926 (n/p no banco, certo), 3 jogos suspensos que o banco guarda como abd (1931 Boca x River, 1939 Boca x Ferro, 2010 Boca x
  River) e 1 divergência real (1989/90 Newell's 1-2 x 0-2, QU-004). Datas: 964 iguais (75,4%), 272 só com o ano diferente (AR-022) e 42 com
  outro dia. Por década (placar igual / data igual / só o ano errado, em jogos do Boca):

  | Década | Jogos | Placar igual | Data igual | Só o ano |
  |---|---|---|---|---|
  | 1910s | 28 | 28 | 25 | 3 |
  | 1920s | 144 | 140 | 55 | 71 |
  | 1930s | 144 | 142 | 70 | 67 |
  | 1940s | 30 | 30 | 28 | 0 |
  | 1950s | 30 | 30 | 29 | 0 |
  | 1960s | 34 | 34 | 34 | 0 |
  | 1970s | 111 | 111 | 98 | 10 |
  | 1980s | 180 | 180 | 136 | 41 |
  | 1990s | 114 | 113 | 104 | 4 |
  | 2000s | 155 | 155 | 143 | 7 |
  | 2010s | 212 | 211 | 154 | 56 |
  | 2020s | 96 | 96 | 88 | 7 |

  Não cobre 1890s e 1900s (o Boca chegou à 1ª divisão em 1913).
- serve a: coleta-sulamerica; buscar: (1) a data de cada rodada nas temporadas amadoras e dos anos 1920-1930 (o Boca joga todas as
  rodadas: a data do jogo dele dá a data da rodada para os outros jogos, 1 página por edição) para o AR-022 e o AR-023; (2) os jogos do
  Boca que faltam (1926 Asociación, AR-007); (3) árbitro e escalações dos jogos do Boca (buraco "árbitro: nenhuma fonte em lote"), jogo a
  jogo, ~4.000 fichas de 1913 a 2025. Risco: site de torcedor (muito detalhado e com fonte em jornais da época, mas de um clube só).

### AUF: histórico oficial de temporadas (auf.org.uy)
- endereço: https://www.auf.org.uy/historico-temporadas/3/12/ (2025; ids: 2 = 2013/14, 6 = 2014/15, 4 = 2015/16 e Uruguayo Especial 2016,
  1 = 2017, 5 = 2018, 3 = 2019, 7 = 2020, 8 = 2021, 9 = 2022, 10 = 2023, 11 = 2024, 12 = 2025, 13 = 2026); tabela anual:
  https://www.auf.org.uy/url.php?id=ajaxapp&tabla_anual=1&id1=3&id2=12
- cobre: 2013/14 a 2026: todos os jogos (Apertura, Intermedio, Clausura, semifinal, finais, desempates e a SUPERCOPA em seção própria), com
  data, hora e estádio; tabela de cada torneio e a TABELA ANUAL oficial (pontos com punições); "Goleadores de la Temporada" (artilharia
  oficial, com minutos jogados). Não tem autores por jogo nem árbitro (as designações de árbitros estão em PDF à parte).
- como baixar: em lote, 1 página por temporada (~2 MB, HTML em cp1252) + 1 pedido para a tabela anual. Leitor e comparador:
  `revisao/QU/auf.py`.
- amostra: 3.357 jogos casados. 2010s: 1.615 jogos, placar igual em 1.578 e data igual em 1.564; 2020s: 1.738 jogos, placar igual em
  1.724 e data igual em 1.523. Todas as diferenças de placar são W.O./decisões de tribunal (El Tanque Sisley 2018, abd/awd) ou a Supercopa
  (UY-013): nenhum placar de campo errado. As datas diferentes são as decisões (UY-014), o 2020 (UY-015, 179 jogos com o ano +1) e poucos
  adiamentos. Cuidado: a AUF erra a contagem de pênaltis em 5 decisões (QU-007; a RSSSF lista cobrança a cobrança e fecha).
- serve a: coleta-sulamerica; buscar: tabela anual oficial 2013/14-2025 (UY-006, UY-004, UY-005), datas das decisões (UY-014), Supercopa
  separada (UY-013), artilharia oficial (UY-017, QU-008), datas do 2020 (UY-015). Serve também a banco-painel: escudos dos clubes atuais
  (UY-022, River Plate de Montevideo). Risco baixo (fonte oficial), mas só a partir de 2013/14.

### transfermarkt (tabela completa da temporada)
- endereço: https://www.transfermarkt.com/primera-division/gesamtspielplan/wettbewerb/AR1N/saison_id/2018 (Argentina 2018/19);
  https://www.transfermarkt.com/primera-division/gesamtspielplan/wettbewerb/URU1/saison_id/2007 (Uruguai 2007/08). Ficha de jogo:
  /index/spielbericht/<id>.
- cobre: data, hora e placar de cada rodada; na ficha: árbitro, público, autores com minuto, cartões, escalações. Argentina: completa nos
  anos 2010 (2018/19: 325 jogos), quase vazia antes de 2000 (1990: 14 jogos). Uruguai: 2005/06 em diante (2005/06: 71 jogos; 2007/08: 120,
  só o Apertura); antes, ~8 jogos por ano.
- como baixar: em lote por temporada (1 página); fichas jogo a jogo. Leitor: `revisao/QU/tm.py`.
- amostra: Argentina 2018/19: 300 jogos, placar igual em 298, ano +1 no banco em todos (confirma o AR-022; 27 com o dia -1, fuso UTC).
  Uruguai 2000s: 190 jogos (2005/06 e 2007/08), placar igual em 187 (as 3 diferenças: 1 W.O. e 2 jogos casados com o turno errado), data
  igual em 171 (16 com 1 dia de diferença, fuso).
- serve a: coleta-sulamerica; buscar: público e árbitro (buraco da seção 4: público 0% de 2010 em diante na Argentina e no Uruguai) e
  autores dos gols onde a ESPN falha (Uruguai 2020s, 59% com autor), jogo a jogo (~380 fichas por temporada). Risco: datas em UTC (±1 dia).

### ESPN (já baixada pela coleta, usada aqui como terceira opinião de datas)
- endereço: data/coleta/arg-1/espn/arg1_<ano>.json e data/coleta/uru-1/espn/uru1_<ano>.json (liga arg.1 e uru.1).
- cobre: 2001+ (Argentina), 2005+ (Uruguai): data/hora UTC, placar, lances.
- como baixar: já está no disco. Script: `revisao/QU/espn_sem_par.py`.
- amostra: 73 jogos sem par na ESPN que a ESPN tem, com o mesmo placar, em outra data (36 arg-1, 37 uru-1): jogos adiados gravados na
  data da rodada (QU-003), o mês trocado do 2005/06 uruguaio (QU-006) e as decisões (UY-014).
- serve a: coleta-sulamerica; buscar: casar pelo par de clubes dentro da edição e usar a data da ESPN (QU-003).

### BDFA (bdfa.com.ar, Base de Datos del Fútbol Argentino)
- endereço: https://www.bdfa.com.ar/argentina-campeones-primera-division.html (lista de campeões, com o id de cada torneio no atributo
  title do escudo); https://www.bdfa.com.ar/resumen-campeonato-5615.html (2018/19).
- cobre: o resumo (tabela final, descensos, punições, artilheiros) só dos torneios com link "Resumen" (de 2012/13 a 2021); escudo pequeno
  de todos os clubes argentinos (/imagenes/<clube>_p.gif); fichas de jogadores. Não tem a lista de jogos. Resumo de 1931 e de 2025: erro do
  servidor.
- como baixar: 1 página por torneio; HTML em latin-1.
- amostra: 2018/19: tabela igual à da RSSSF (Racing 57 ... Argentinos 22); cita a punição de -6 de San Lorenzo e Huracán, que a
  tabela não aplica (a RSSSF diz que foi suspensa); artilheiro Lisandro López 17 (igual ao banco).
- serve a: coleta-sulamerica (descensos por temporada, AR-021) e banco-painel (escudos que faltam, AR-035). Risco: cobertura curta.

### Wikipédia em italiano
- endereço: https://it.wikipedia.org/wiki/Primera_Divisi%C3%B3n_1896_(Argentina)
- cobre: tabela final, artilheiros e período de cada temporada argentina de 1891 em diante; não traz os jogos nos anos amadores; não tem
  páginas das temporadas uruguaias antigas (1951: não existe).
- como baixar: 1 página por temporada (a API deu "too many requests" em 22/11: os revisores dividem o IP; usar o HTML).
- amostra: 1896: Lomas Academy 12, Flores 10, Lomas Athletic 9, Belgrano 8, Retiro 1, 20 jogos: igual à es (confirma o AR-013).
- serve a: coleta-sulamerica; terceira opinião de tabela e artilheiro no amadorismo argentino. Risco: cita a RSSSF e a IFFHS, então não é
  independente.

### Testadas e sem uso
- afa.com.ar: só notícias e efemérides ("boca-campeon-1965"), sem base histórica.
- padreydecano.com (Peñarol), nacional.uy, decano.com (Nacional): sem base de jogos.
- historiayfutbol.com, historiadelfutbolargentino.com, estadisticasfutbol.com.ar, museodelfutbol.uy: não abriram; iffhs.com: página vazia.
- worldfootball.net e livefutbol.com: 403. footballdatabase.eu: limite diário esgotado em 22/11 (testar outro dia para o Uruguai antigo).
- soccerway.com: responde, não testado por amostra (cobre a partir dos anos 2000, como o transfermarkt).

### Décadas sem fonte nova
- Argentina 1890s e 1900s: nenhuma fonte independente com os jogos (a it cita a RSSSF/IFFHS).
- Uruguai 1900s, 1910s, 1930s a 1970s e 1990s: nenhuma fonte nova com jogos ou datas. O banco não tem data em 1910-1979 (seção 4 da
  ficha) e nenhuma das fontes testadas cobre; a melhor aposta é o footballdatabase.eu (limite diário) e, para Peñarol e Nacional, livros
  dos clubes (fora da internet).
