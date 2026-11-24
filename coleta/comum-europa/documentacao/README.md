# Coleta Europa — documentação

Gerado por `python coleta/comum-europa/documentar.py`. Uma ficha por liga, com tudo o que o pacote tem, a cobertura de cada campo década a década, o formato do campeonato ao longo do tempo, campeões, punições, todas as correções e decisões com o motivo, o que não deu para coletar e as pendências.

Regras de trabalho, ordem das pendências e como fazer uma liga nova: `coleta/comum-europa/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-europa.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-europa`).

| Liga | Temporadas | Jogos | Gols c/ autor | Cartões | Clubes | Tabelas ok / div. | Pendências | Ficha |
|---|---|---|---|---|---|---|---|---|
| Campeonato Inglês | 127 (1888/89–2025/26) | 51330 | 25878 | 33166 | 65 | 226 / 1 | 0 | [eng-1](eng-1.md) |
| Campeonato Espanhol | 95 (1928/29–2025/26) | 27716 | 25072 | 51662 | 63 | 180 / 11 | 0 | [esp-1](esp-1.md) |
| Campeonato Italiano | 124 (1898–2025/26) | 34732 | 24598 | 43962 | 191 | 268 / 42 | 0 | [ita-1](ita-1.md) |
| Campeonato Alemão | 124 (1902/03–2025/26) | 20303 | 56842 | 30251 | 194 | 181 / 7 | 0 | [ger-1](ger-1.md) |
| Campeonato Francês | 88 (1932/33–2025/26) | 30466 | 22613 | 35434 | 77 | 153 / 21 | 0 | [fra-1](fra-1.md) |
| Campeonato Português | 92 (1934/35–2025/26) | 20978 | 18958 | 30915 | 73 | 171 / 13 | 0 | [por-1](por-1.md) |
| Campeonato Holandês | 138 (1888/89–2025/26) | 21878 | 23019 | 24431 | 93 | 191 / 3 | 0 | [ned-1](ned-1.md) |
| Campeonato Escocês | 129 (1890/91–2025/26) | 33076 | 14565 | 19812 | 46 | 197 / 60 | 0 | [sco-1](sco-1.md) |
| Campeonato Belga | 123 (1895/96–2025/26) | 28712 | 12031 | 18167 | 81 | 185 / 83 | 0 | [bel-1](bel-1.md) |
| Campeonato Turco | 97 (1924 (Şampiyonası)–2025/26) | 20971 | 13891 | 23395 | 168 | 128 / 30 | 0 | [tur-1](tur-1.md) |
| Campeonato da Alemanha Oriental | 44 (1948–1990/91) | 8062 | 0 | 0 | 52 | 65 / 19 | 0 | [gdr-1](gdr-1.md) |

## Pendências de todas as ligas

Nenhuma em aberto na coleta (rodada de 24/11/2026). O que sobrou está abaixo.

## Limites de fonte (fechados)

Nenhuma fonte em lote tem o dado; só volta com uma fonte nova.

- **eng-1:** Autores dos gols e cartões antes de 2001/02: nenhuma fonte em lote; seria jogo a jogo (ficha do ogol).
- **eng-1:** Nomes de jogadores da ESPN: os casos em formato de documento (sobrenomes na frente) que repetem um jogador com o nome de jogo no mesmo clube e temporada foram trocados (coleta/comum-europa/nomes_jogadores.py, aplicado em todas as ligas; varredura de 24/11/2026). Os outros ~2 mil nomes de 3 palavras ou mais são quase todos nomes de verdade ("Kevin De Bruyne"); a ESPN não dá o código do jogador para conferir um a um.
- **esp-1:** Autores dos gols e cartões antes de 2001/02: a RSSSF tem de 2000/01 em diante; antes, jogo a jogo (ficha do ogol).
- **ita-1:** Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).
- **ita-1:** Era antiga (1898 a 1928/29, IT-017, em antigo.py): 29 edições pela Wikipédia em italiano. 713 jogos vêm só do Tabellone (sem data); 37 classificações de grupo diferem dos jogos (quase todas em 1 ou 2 gols, ou um jogo que o calendário não traz), listadas no relatório. A RSSSF (italhist98-25.html e ital24-29.html, em data/coleta/ita-1/rsssf-antigo/) só tem tabelas a partir de 1909/10; o próximo passo seria o Almanacco Illustrato.
- **ita-1:** Era antiga: a classificação final de cada edição é montada (campeão do albo d'oro, depois a fase alcançada e a posição no grupo); não há classificação oficial além do campeão.
- **ger-1:** Autores dos gols: RSSSF (1963/64-1998/99, só os jogos em que a soma fecha, cerca de 97%), ficha do ogol (1999/00, 2000/01 e os jogos em que a ESPN falta ou não fecha) e ESPN (2001/02+). Os jogos que nenhuma das três fecha ficam sem autor; cartões só pela ESPN.
- **ger-1:** Era antiga (1902/03-1962/63, em antigo.py): entra só a fase final; as ligas regionais (Oberligen, Gauligen e as ligas de antes) ficam de fora (são outras competições, por região).
- **ger-1:** Era antiga: gols com autor só nas partidas com ficha (football box) na Wikipédia, quase sempre a final; não há lista de artilheiros da fase final.
- **ger-1:** Era antiga: a classificação final é o campeão, o vice e depois a fase alcançada (na mesma fase, posição no grupo e campanha); não existe classificação oficial além do campeão e do vice.
- **fra-1:** Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).
- **fra-1:** Datas dos 356 jogos dos anos 1930 que nenhuma fonte tem.
- **fra-1:** Revisão FR-009: 99 jogos (1948/49-1998/99) em que o transfermarkt e o ogol diferem da base por 1 ou 2 dias; só os 41 de 3 dias ou mais foram corrigidos. Os outros só com o jornal (L'Équipe na Gallica), jogo a jogo.
- **fra-1:** Revisão FR-017: 4 pares de jogos em que a Wikipédia fr dá outro mando ou placar (1935/36, 1937/38, 1945/46, 1950/51); fica a base, que fecha com as tabelas (anotado em EXPLICACOES). Só o jornal da época decidiria.
- **fra-1:** Revisão FR-005: a vitória do Marseille sobre o Bordeaux em 27/10/1946 (0-0 no tribunal) vem das tabelas das Wikipédias e fecha com elas; só o L'Équipe de 28/10/1946 decidiria.
- **fra-1:** Árbitro: os arquivos do football-data da França não trazem (revisão FR-022); seria jogo a jogo pelo transfermarkt.
- **por-1:** Autores dos gols: RSSSF (1999/00-2005/06, onde a soma fecha), ficha do ogol (2001/02, que a RSSSF não traz, e os jogos em que a ESPN falta ou não fecha) e ESPN (2006/07+). Antes de 1999/00, nenhuma fonte em lote. Sem autor ficam 103 jogos de 2001/02 e 27 de 2010/11 (a ficha do ogol também não fecha).
- **por-1:** Revisão PT-020: árbitro e público só jogo a jogo (transfermarkt, ~11 mil páginas, ou a ficha do ogol); o football-data de Portugal não traz árbitro.
- **por-1:** Revisão PT-010: Belenenses x Sporting (1938/39) e os dois jogos do Académico do Porto em 04/02/1940 (1939/40) ficam com a data do ogol; o transfermarkt repete o ogol e não há terceira fonte (anotado em EXPLICACOES).
- **ned-1:** Era antiga (1888/89-1955/56, em antigo.py): de 1888/89 a 1896/97 e nas temporadas sem a fase final legível na RSSSF, só o campeão e a tabela da Eerste Klasse, sem jogos; os jogos da fase final vêm da matriz da RSSSF, sem data (datados só em 1954/55 e 1955/56). As ligas regionais ficam de fora.
- **ned-1:** Era antiga: tabelas da fase final que não fecham com os jogos por erro de digitação da RSSSF (1906/07, 1922/23, 1923/24); ficam anotadas no relatório.
- **ned-1:** Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).
- **sco-1:** Autores dos gols e cartões antes da ESPN (2001/02): jogo a jogo (ficha do ogol).
- **sco-1:** Rodada vazia até os anos 1930 em várias temporadas: não havia rodadas fixas (como no Inglês) e o ogol não traz.
- **bel-1:** Antes de 1960/61: jogos só pela matriz da Wikipédia, sem data nem rodada (o ogol não tem); quando a soma não fecha com a tabela da RSSSF, a classificação final fica com os números publicados (observação na linha).
- **bel-1:** 1898/99, 1899/00, 1901/02, 1902/03 e 1903/04 (grupos): só as tabelas da RSSSF e os jogos finais e de desempate; sem os jogos dos grupos e sem classificação oficial além do campeão e do torneio final.
- **bel-1:** Autores dos gols e cartões: só com a ESPN (2006/07+), que não tem lances de 2011/12 a 2014/15 nem dos play-offs; antes e nesses anos, jogo a jogo (ficha do ogol).
- **bel-1:** Jogos de play-off de acesso e rebaixamento contra clubes da 2ª divisão (até 2008/09) ficam de fora; desde 2016/17 os clubes da 2ª divisão no play-off europeu entram nos jogos, mas não na classificação final.
- **bel-1:** Artilheiros só desde 1945/46 (lista da RSSSF).
- **tur-1:** Era antiga (antes de 1959, em antigo.py): os jogos do Şampiyonası de 1924 a 1935 e as matrizes da Millî Küme não têm data (só as fichas trazem).
- **tur-1:** 1962/63: os jogos do grupo de classificação (7º a 9º de cada grupo) não estão no ogol nem na Wikipédia (en e tr); entra a tabela.
- **tur-1:** Autores dos gols e cartões: só com a ESPN (2006/07+), que quase não tem lances de 2011/12 a 2014/15 nem dos play-offs de 2011/12; antes e nesses anos, jogo a jogo (ficha do ogol).
- **tur-1:** Placares do ogol que só a matriz da Wikipédia contesta nas temporadas antigas (sem football-data nem engsoccerdata antes de 1994/95): ficam os do ogol, que fecham com as tabelas.
- **gdr-1:** Autores dos gols, público e estádio dos jogos da Oberliga: a RSSSF traz só o placar; fonte possível: as fichas do weltfussball.de ou o arquivo do jornal Neues Deutschland, jogo a jogo.
- **gdr-1:** 1948 e 1949: só a fase final (mata-mata entre os campeões estaduais); os campeonatos estaduais ficam de fora.
- **gdr-1:** Punições de pontos que só a tabela da RSSSF traz (1966/67, 1967/68, 1973/74, 1990/91): os pontos oficiais vão para a classificação e a diferença para ajuste_pontos; o motivo de cada uma não está nas fontes.

## Com o agente de revisão

Decisões da coleta que a revisão confere.

- **ita-1:** Era antiga: as 37 classificações de grupo que diferem dos jogos e a identidade dos clubes antigos (clubes_ita.py, _ANTIGOS).
- **ned-1:** Identidade de clubes em fusões (GVAV x FC Groningen, SC Enschede x FC Twente, Rapid JC x Roda JC, Alkmaar '54 x AZ, BVV x FC Den Bosch): separados como clubes diferentes, contra o ogol, que junta alguns na ficha do sucessor.
- **sco-1:** Temporadas em que as duas tabelas publicadas erram em clubes diferentes: o ogol fecha com uma delas em cada clube; conferir com uma terceira fonte (jornais da época, fitbastats.com, statto.com).
- **tur-1:** Kayseri: o Kayserispor de 1966 a 2004 está como Kayseri Erciyesspor (troca de nomes de 2004, como na Wikipédia); o ogol e boa parte da imprensa contam a história no Kayserispor de hoje.
- **gdr-1:** Identidade dos clubes (coleta/comum-europa/clubes_gdr.py), sobretudo Chemie Leipzig, e o título de 1952/53 (Dynamo Dresden, como a RSSSF); as 19 tabelas que diferem dos jogos.

## Próximas ligas

- A combinar com o Guilherme (guia geral `docs/agentes-internacionais-COMECE-AQUI.md`), uma por vez e só com o ok dele.
