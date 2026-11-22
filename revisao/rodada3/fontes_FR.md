# Fontes avaliadas: Campeonato Francês (fra-1), revisor FR, 22/11/2026

### Wikipédia fr: páginas por temporada
- endereço: https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_1974-1975 (API: https://fr.wikipedia.org/w/api.php?action=parse&page=Championnat_de_France_de_football_1974-1975&prop=wikitext&format=json)
- cobre: as 88 temporadas (1932/33-2025/26):
  - tabela final ("foot classement", com bônus e cor de rebaixado, barrage e rebaixamento administrativo);
  - grade de resultados ("Foot résultat"), com notas dos jogos decididos no tribunal ("tapis vert");
  - infobox "relégué fin";
  - seções de barrages e de artilheiros;
  - texto sobre as regras (bônus, 3 pontos, média de gols).
- como baixar: em lote; wikitexto pela API, 1 página por temporada. A API dá 429 com frequência: esperar 45 s e tentar de novo.
  O leitor está em `revisao/FR/frwiki.py`.
- amostra:
  - tabelas: 1.638 de 1.666 linhas batem com o pacote; as 28 diferenças são erros do pacote ou casos explicados;
  - grade: 29.026 de 29.087 placares batem;
  - nos anos 2010 a grade tem linhas desalinhadas (Lyon 2012/13, Nantes 2013/14, Bastia 2016/17) e 4 erros. Ali o
    transfermarkt e o football-data são melhores.
- serve a: coleta-europa. Buscar:
  - jogos do tribunal (procurar "tapis vert" e "fc|perdu");
  - regra do bônus e rebaixados (cores e infobox);
  - fusões e rebaixamentos administrativos ("rétrogradé");
  - a tabela de cada temporada como terceira opinião.

### Wikipédia fr: "Meilleurs buteurs du championnat de France de football"
- endereço: https://fr.wikipedia.org/wiki/Meilleurs_buteurs_du_championnat_de_France_de_football
- cobre: artilheiro(s) e gols de cada temporada, 1932/33-2025/26. Cita a ligue1.fr ("Historique et records du classement des
  buteurs") e o maxifoot.
- como baixar: em lote; 1 página, tabela "Palmarès par édition".
- amostra: 76 de 88 batem com o pacote (RSSSF). Faltam 2 artilheiros empatados (1979/80 Onnis; 1983/84 Garande), Bokšić tem
  23 e não 22, e há 9 diferenças de grafia.
- serve a: coleta-europa. Buscar: artilheiros pela contagem oficial da LFP e nomes usuais.

### transfermarkt: calendário completo da temporada
- endereço: https://www.transfermarkt.com/ligue-1/gesamtspielplan/wettbewerb/FR1?saison_id=1977
- cobre: data, hora, placar e rodada de todos os jogos.
  - **De 1948/49 em diante:** completo.
  - **Antes de 1948/49:** incompleto e errado (grupos misturados, clube contra ele mesmo); não usar.
  - **Páginas:** abriram as 88.
- como baixar: em lote; 1 página HTML por temporada. Os clubes vêm pelo código (`verein/<id>`), casado por votação. Leitor:
  `revisao/FR/comparar_tm.py`.
- amostra:
  - placares: 27.900 jogos de 1948/49 em diante, 17 diferenças; 3 são erros do pacote (FR-003, FR-004, FR-008), 3 são W.O. dados
    como 0-3 e os outros são erros do transfermarkt;
  - datas: 140 jogos em que o transfermarkt e o ogol concordam contra o pacote (FR-009).
- serve a: coleta-europa. Buscar: datas (terceira opinião entre a base e o ogol) e placares de 1948/49 em diante.

### transfermarkt: ficha do jogo
- endereço: https://www.transfermarkt.com/sporting-etoile-club-bastia-_as-monaco/index/spielbericht/3808478
- cobre: árbitro, público, estádio, gols com autor e minuto, cartões e placar do intervalo, mesmo em jogos antigos. Testei
  1977/78 Bastia 0-2 Monaco: árbitro Michel Vautrot, público 5.850, 2 gols de Onnis e cartão de Krimau.
- como baixar: jogo a jogo, cerca de 27 mil páginas. O id da ficha está no calendário já baixado (`ergebnis-link id=`).
- amostra: 1 de 1 com todos os campos; falta testar uma amostra maior por década.
- serve a: coleta-europa. Buscar: árbitro (hoje 0% em todas as décadas) e, antes de 2001/02, gols com autor, cartões, público e
  estádio.

### footballdatabase.eu
- endereço: https://www.footballdatabase.eu/en/competition/overall/111-division_1/1977-1978 (a lista de temporadas está em
  `revisao/FR/fdb_temporadas.txt`)
- cobre: as 88 temporadas, com resultados por rodada (data e autores dos gols com minuto, mesmo nos anos 1970), tabela,
  promovidos e rebaixados.
- como baixar: por rodada, uma página com cerca de 10 jogos. **Limite de 50 páginas por dia por IP sem conta**, e os
  revisores dividem o IP; esgotou nesta rodada.
- amostra: 1 temporada vista (1977/78): tabela e rebaixados batem com o pacote.
- serve a: coleta-europa. Buscar: datas e rodadas dos anos 1930 (356 jogos sem data, 224 sem rodada) e autores dos gols antigos.
  Pede uma conta grátis ou vários dias.

### football-data.co.uk
- endereço: https://www.football-data.co.uk/francem.php (arquivos F1_9394.csv...)
- cobre: placar e estatísticas de 1993/94 em diante. **Não traz árbitro para a França**; a ficha da coleta diz que traz.
- como baixar: em lote; CSV.
- amostra: já usado pela coleta. Nas datas de 1996/97 repete a data da base (domingo), enquanto o ogol e o transfermarkt dão
  sábado.
- serve a: coleta-europa. Buscar: nada novo.

### ligue1.com
- endereço: https://ligue1.com/fr/competitions/ligue1mcdonalds/standings?season=2008-2009
- cobre: só a temporada atual. A página é montada por JavaScript e ignora o parâmetro `season`.
- como baixar: não serve.
- amostra: 0 de 1.
- serve a: nenhum.

### RSSSF (por temporada, anos 1930-40)
- endereço: https://www.rsssf.org/tablesf/fran34.html
- cobre: não existe (404). Só há a página histórica `franfullhist.html`, já usada pela coleta.
- serve a: nenhum.

### 11v11, statto
- 11v11: não tem a liga francesa (redireciona para 404). statto: redireciona (301), não testei mais.
- serve a: nenhum.
