# Decisões do Guilherme: Argentino (arg-1) e Uruguaio (uru-1)

Revisor QU, 22/11/2026. Todas ainda sem resposta (coleta/comum-sulamerica/COMECE-AQUI.md, seção 3, item 4: "esperam").

### AR-044 Título de 1891: só o Saint Andrew's ou dividido com o Old Caledonians?
- opções: (a) só Saint Andrew's (como a AFA cita hoje; é o que está no painel); (b) título dividido (os dois campeões em 1891).
- prova: a liga da época declarou os dois campeões empatados e o Saint Andrew's ficou com as medalhas no desempate (coleta,
  coleta/arg-1/explicacoes.py EXPLICACOES['1891']); https://en.wikipedia.org/wiki/List_of_Argentine_football_champions e
  https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_de_Argentina listam os dois.
- recomendação: (a), mantendo a observação da edição. A lista oficial da AFA é a referência do projeto para títulos (como a AUF no
  Uruguai); o painel já explica o empate na observação.

### AR-043 Apertura 2026 (Belgrano campeão, River vice): entra agora ou só quando a temporada 2026 fechar?
- opções: (a) entrar já como edição "2026 Apertura" (o torneio terminou; o BDFA já o lista entre os campeões);
  (b) esperar o fim de 2026 e entrar com o Clausura e a tabela anual.
- prova: https://www.bdfa.com.ar/argentina-campeones-primera-division.html (primeiro da lista: "2026 Torneo Apertura");
  https://en.wikipedia.org/wiki/List_of_Argentine_football_champions.
- recomendação: (b). O pacote trata a temporada inteira de uma vez (como a "2025 Liga", que soma Apertura e Clausura) e as coletas só
  pegam campeonatos novos quando o Guilherme manda.

### AR-032 Quilmes de 1893-1895 (Quilmes Club / Quilmes Rovers) é o mesmo Quilmes de hoje?
- opções: (a) o mesmo clube (como está: os nomes antigos no nomes_fonte do Quilmes); (b) clube à parte ("Quilmes Rovers").
- prova: es (https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_de_Argentina, nota de 1893): "El Quilmes Atlético Club, sin evidencias,
  infiere ser la misma entidad que el Quilmes Rowers Athletic Club, aunque historiadores afirman que se trata de dos entidades distintas".
  Nenhuma fonte nova ajudou (o historiadeboca só tem o Boca; o BDFA não cobre 1893).
- recomendação: (b) clube à parte. O critério da casa é "o mais fiel à história", e a própria es diz que a ligação não tem prova. Mexer
  em coleta/arg-1/clubes_arg.py (REGRA 'quilmes' de 1893 a 1895 -> 'Quilmes Rovers').

### AR-033 Fusões de 1934 (Atlanta + Argentinos Juniors; Talleres + Lanús)
- opções: (a) como está: Atlanta-Argentinos entra como "Argentinos Juniors" e Talleres-Lanús como clube à parte "Unión Talleres-Lanús";
  (b) as duas como clubes à parte ("Atlanta-Argentinos Juniors" e "Unión Talleres-Lanús"); (c) as duas no clube de maior peso.
- prova: RSSSF arg34 (tabela com "Atlanta/Argentinos Jrs" e "Talleres/Lanús"); docs/coleta/pedidos-sulamerica.md item 4.
- recomendação: (b). As duas foram fusões só daquele campeonato; tratar igual evita dar a um clube um ano que foi de dois.

### Copa de Oro de 1936: manter como título?
- opções: (a) manter (como está: título reconhecido pela AFA em 04/07/2013); (b) tirar.
- prova: observação da edição (coleta/arg-1/edicoes.py); https://en.wikipedia.org/wiki/List_of_Argentine_football_champions (nota de que
  historiadores contestam). O historiadeboca não ajuda (o Boca não jogou).
- recomendação: (a). É decisão oficial da AFA, e o projeto segue a lista da federação.

### UY-001 1923 FUF, 1924 FUF e 1926 (Consejo Provisorio) contam como título?
- opções: (a) seguir a AUF (122 campeonatos): as três edições ficam, sem campeão, com a nota "não reconhecido pela AUF" (Peñarol 52,
  Wanderers 3); (b) seguir a RSSSF (como está: Peñarol 54, Wanderers 4).
- prova: https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_de_Uruguay#T%C3%ADtulos_de_liga_por_a%C3%B1o (lista da AUF); o site da AUF não
  publica a lista histórica de campeões (só seleções e temporadas desde 2013/14: https://www.auf.org.uy/historico-torneos/).
- recomendação: (a). O painel já aceita edição sem campeão (1948, UY-002).

### UY-020 O "Atlético Wanderers" da FUF (1923-1924) é o Montevideo Wanderers? (o mesmo para Lito e Charley)
- opções: (a) o mesmo clube (como está); (b) clubes à parte ("Atlético Wanderers", "Lito (FUF)", "Charley (FUF)").
- prova: https://www.rsssf.org/tablesu/uruhist.html (1923 FUF: "Atlético Wanderers"); es, seção Cisma (1922-1925): era um equipo alternativo
  do Wanderers, que seguia na AUF. Hoje o Wanderers joga AUF e FUF no mesmo ano.
- recomendação: (b). Um clube não pode jogar duas ligas rivais no mesmo ano; com (b), a "melhor campanha" e os gols de 1923 FUF deixam de
  ir para o Wanderers. Mexer em coleta/uru-1/clubes_uru.py (REGRAS de 1923-1924 na FUF).

### UY-007 Vice de 1954: Nacional (RSSSF, en) ou Danubio (es)?
- opções: (a) Nacional (como está; tabela da RSSSF, Nacional e Danubio com 22 pts); (b) Danubio (es: 10-4-4, 31-21, 24 pts).
- prova: https://www.rsssf.org/tablesu/uru54.html; https://es.wikipedia.org/wiki/Campeonato_Uruguayo_de_Primera_Divisi%C3%B3n_1954; a AUF
  não tem 1954; nenhuma fonte nova achada.
- recomendação: (a) até aparecer terceira fonte: a tabela da RSSSF fecha com os jogos do banco e a en concorda; registrar a es na
  observação da edição.

### UY-008 Vice de 1947: Peñarol ou nenhum?
- opções: (a) Peñarol (como está; en); (b) sem vice ("no se definió": o triangular pelo 2º lugar entre Peñarol, Defensor e Rampla não
  terminou, es).
- prova: https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_de_Uruguay#T%C3%ADtulos_de_liga_por_a%C3%B1o (linha 1947); o banco tem o 3º
  jogo do triangular como "não jogado" (coleta/uru-1/explicacoes.py, CORRIGE uru47:179).
- recomendação: (b), com observação. O próprio pacote mostra que o desempate não terminou.

### UY-004 (parte) Vice quando não houve final (2011/12, 2021): o 2º da tabela anual ou o perdedor da semifinal?
- opções: (a) 2º da tabela anual (es, en, e a tabela anual oficial da AUF em 2021); (b) perdedor da semifinal.
- prova: https://www.auf.org.uy/url.php?id=ajaxapp&tabla_anual=1&id1=3&id2=8 (2021); https://en.wikipedia.org/wiki/Uruguayan_Primera_Divisi%C3%B3n.
- recomendação: (a), como as listas oficiais.
