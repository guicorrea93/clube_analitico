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
| Campeonato Grego | 90 (1927/28–2025/26) | 18689 | 8900 | 20025 | 69 | 163 / 32 | 0 | [gre-1](gre-1.md) |
| Campeonato Tcheco | 33 (1993/94–2025/26) | 8234 | 7121 | 0 | 35 | 75 / 1 | 0 | [cze-1](cze-1.md) |
| Campeonato Tchecoslovaco | 68 (1925–1992/93) | 11791 | 0 | 0 | 66 | 120 / 18 | 0 | [tch-1](tch-1.md) |
| Campeonato Polonês | 98 (1921–2025/26) | 19667 | 0 | 0 | 103 | 139 / 74 | 0 | [pol-1](pol-1.md) |
| Campeonato Norueguês | 80 (1937/38–2025) | 12368 | 14830 | 11950 | 128 | 116 / 4 | 0 | [nor-1](nor-1.md) |
| Campeonato Dinamarquês | 112 (1912/13–2025/26) | 14016 | 11661 | 12026 | 72 | 166 / 13 | 0 | [den-1](den-1.md) |
| Campeonato Cipriota | 86 (1934/35–2025/26) | 13465 | 231 | 0 | 46 | 126 / 38 | 0 | [cyp-1](cyp-1.md) |

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
- **gre-1:** 1959/60 a 1992/93: jogos sem data nem rodada (só a matriz da RSSSF e a da Wikipédia; o ogol não tem esses jogos). Rodadas de 1994/95 a 1996/97: o ogol não traz.
- **gre-1:** Era antiga (1927/28-1958/59, em antigo.py): só a fase nacional entre os campeões regionais; as ligas regionais, a fase semifinal de 1955/56 e as eliminatórias inter-regionais ficam de fora. Datas só nas finais e em 1929/30 e 1945/46.
- **gre-1:** Era antiga: em 1954/55 e 1955/56 as tabelas da RSSSF e da Wikipédia concordam entre si e não fecham com nenhuma matriz (diferenças de 1 a 4 gols); só o jornal da época decidiria.
- **gre-1:** Autores dos gols e cartões: só com a ESPN (2006/07+), que quase não tem lances de 2011/12 a 2014/15; antes, só as fichas dos jogos-desempate da Wikipédia.
- **gre-1:** Jogos de acesso e rebaixamento contra clubes da 2ª divisão ficam de fora (1959/60, 1967/68, 1968/69, 2000/01 a 2003/04, 2013/14, 2018/19 a 2021/22).
- **gre-1:** Play-off europeu de 2015/16: a tabela da Wikipédia dá 1 gol a menos a AEK (pró) e Panionios (contra) que os jogos do ogol; sem terceira fonte (a ESPN e o football-data não têm os play-offs), fica o ogol.
- **cze-1:** Autores dos gols só de 1998/99 a 2011/12 (página da RSSSF, quando a conta fecha com o placar: 7.121 gols); antes e depois, nenhuma fonte em lote (a ESPN e o football-data não cobrem a Tchéquia). Sem cartões, público, estádio e árbitro: só a ficha de cada jogo no ogol, jogo a jogo.
- **cze-1:** Jogos de acesso e rebaixamento contra clubes da 2ª divisão ficam de fora.
- **cze-1:** A liga tchecoslovaca (1925-1993) e a do Protetorado (1938/39-1943/44) ficam na competição da Tchecoslováquia (decisão do Guilherme, 25/11/2026).
- **tch-1:** Sem datas, rodadas, autores dos gols, cartões e público: a base é a matriz da Wikipédia (en); o ogol, a ESPN e o football-data não têm esta liga.
- **tch-1:** 10 temporadas em que a matriz da Wikipédia não fecha com as tabelas (que concordam entre si): a classificação fica com os números publicados; só um jornal da época diria qual jogo está errado.
- **tch-1:** Fora do escopo (decisão do Guilherme, 25/11/2026): Boêmia Central antes de 1925, campeonato amador, 1944/45 e liga eslovaca da guerra.
- **pol-1:** Sem datas e rodadas de 1921 a 1962 (só as matrizes de resultados da Wikipédia e da RSSSF, fora as fichas das finais e do mata-mata de 1946); sem autores dos gols, cartões e público em toda a liga (sem ESPN; o football-data não traz cartões da Polônia).
- **pol-1:** Grupo final de 1926 sem os jogos em nenhuma fonte (RSSSF, Wikipédia em inglês e em polonês): fica a tabela publicada.
- **pol-1:** 9 temporadas antigas em que a matriz não fecha com as tabelas (que concordam entre si): a classificação fica com os números publicados.
- **pol-1:** Fora do escopo (decisão do Guilherme, 25/11/2026): 1920 (abandonado), 1924 (não disputado), 1939 (interrompido) e as ligas municipais da guerra; os jogos de acesso contra a 2ª divisão.
- **nor-1:** Norgesserien (1937/38, 1938/39, 1947/48): só um grupo por temporada tem os jogos (Distrito V, grupo B, na Wikipédia em norueguês); os outros ficam com a tabela publicada.
- **nor-1:** Sem datas e rodadas até 1960/61 (só matrizes e tabelas do mata-mata). Autores dos gols e cartões só com a ESPN (2008-2025) e, para os gols, com as páginas da RSSSF (1999-2003 e 2005); antes, nenhuma fonte em lote.
- **nor-1:** Fora do escopo (decisão do Guilherme, 25/11/2026): Prøveligaen de 1914-16, 1939/40 (interrompida) e a copa (fase 2); 2026 entra quando a temporada terminar.
- **den-1:** Sem os jogos das ligas de Copenhague (até 1927), da liga de 1928/29 a 1939/40 e das séries da guerra: só as tabelas (Wikipédia e RSSSF); o banco Haslund não é baixável em lote. 1928/29 só pela RSSSF (a Wikipédia não tem o artigo).
- **den-1:** Sem datas e rodadas até 1990; autores dos gols e cartões só com a ESPN (desde 2006/07; quase sem lances de 2011/12 a 2013/14) e, para os gols, com as páginas da RSSSF.
- **den-1:** Fora do escopo (decisão do Guilherme, 25/11/2026): Copenhague de 1889 a 1912, 1914/15 (suspenso), 1927/28 (sem campeão) e 2026/27 (em andamento).
- **cyp-1:** Sem autores dos gols e cartões: nenhuma fonte em lote cobre Chipre (sem ESPN e sem football-data). Sem datas e rodadas até 1995/96 (só a matriz da Wikipédia).
- **cyp-1:** Matrizes antigas incompletas (anos 1930 a 1950 e algumas depois): a classificação fica com os números publicados quando a matriz não fecha (observação na linha).
- **cyp-1:** Fora do escopo (decisão do Guilherme, 27/11/2026): os campeonatos não oficiais de 1931/32 a 1933/34 e as temporadas sem campeão (1941/42 a 1943/44, 1958/59, 1963/64 e 2019/20).

## Com o agente de revisão

Decisões da coleta que a revisão confere.

- **ita-1:** Era antiga: as 37 classificações de grupo que diferem dos jogos e a identidade dos clubes antigos (clubes_ita.py, _ANTIGOS).
- **ned-1:** Identidade de clubes em fusões (GVAV x FC Groningen, SC Enschede x FC Twente, Rapid JC x Roda JC, Alkmaar '54 x AZ, BVV x FC Den Bosch): separados como clubes diferentes, contra o ogol, que junta alguns na ficha do sucessor.
- **sco-1:** Temporadas em que as duas tabelas publicadas erram em clubes diferentes: o ogol fecha com uma delas em cada clube; conferir com uma terceira fonte (jornais da época, fitbastats.com, statto.com).
- **tur-1:** Kayseri: o Kayserispor de 1966 a 2004 está como Kayseri Erciyesspor (troca de nomes de 2004, como na Wikipédia); o ogol e boa parte da imprensa contam a história no Kayserispor de hoje.
- **gdr-1:** Identidade dos clubes (coleta/comum-europa/clubes_gdr.py), sobretudo Chemie Leipzig, e o título de 1952/53 (Dynamo Dresden, como a RSSSF); as 19 tabelas que diferem dos jogos.
- **gre-1:** 1959/60 a 1992/93: onde a matriz da RSSSF e a da Wikipédia discordam, ficou o placar que fecha com as duas tabelas publicadas (a maioria é da Wikipédia; trocas jogo a jogo e em pares, anotadas no relatório e na observação do jogo).
- **gre-1:** Era antiga: o mesmo critério na fase nacional (1930/31, 1931/32, 1953/54, 1956/57, 1957/58, 1958/59 com trocas).
- **gre-1:** Identidade: Chalkidona em 2004/05 (o ogol põe no Atromitos, que absorveu o clube em 2005); Rodos x AE Rodos e AO Kerkyra x PAE Kerkyra separados como na Wikipédia; Megas Alexandros (1959/60) como Pierikos.
- **gre-1:** Desempates de posição que só estão nas notas da Wikipédia (1959/60 a 1966/67, 1973/74, 1982/83, 1983/84), sem data.
- **cze-1:** Identidade: o Dukla Praha histórico (1993/94) separado do 1. FK Příbram (o ogol usa o mesmo código) e do FK Dukla Praha de hoje; Bohemians 1905 x Bohemians de Střížkov (2008/09 e 2009/10).
- **cze-1:** Classificação com grupos (2018/19, 2019/20, desde 2021/22): do 7º ao 10º pela fase regular (o play-off europeu não muda a posição).
- **tch-1:** Identidade pelos links da Wikipédia através das trocas de nome da era comunista; o Dukla Praha histórico é o mesmo do `cze-1` em 1993/94, mas a RSSSF diz que ele é hoje o Marila Příbram (no `cze-1`, Příbram ficou à parte, pela Wikipédia).
- **tch-1:** Classificação de 1945/46: a final (Sparta x Slavia) e depois a posição nos grupos; títulos do Protetorado contados (Sparta 21, Slavia 13 no total).
- **pol-1:** Identidade pelos links da Wikipédia: o PKS Szczecin de 1946-47 como o Pogoń Szczecin, o Motor Białystok (1947) como o Jagiellonia, o Grochów (1947) como o Gwardia Varsóvia, o RKU Sosnowiec como o Zagłębie; o Olimpia/Lechia Gdańsk de 1995/96 à parte do Lechia (o ogol junta) e o Sokół Tychy como o GKS Tychy; o 22 pp Siedlce e o Strzelec Siedlce como um clube só (a RSSSF diz que mudou de nome).
- **pol-1:** 1922: a RSSSF trocou as matrizes dos dois grupos; os jogos vêm da matriz certa, e os números fecham com a Wikipédia polonesa. 1951: campeão o Ruch (6º na liga, pela Copa); 1992/93: os dois jogos anulados ficam fora.
- **pol-1:** Placares do ogol trocados pela matriz da Wikipédia só quando ela fecha melhor com as tabelas, ou empatada com o football-data ou a RSSSF a favor (2004/05, 2006/07, 2007/08, 2022/23, 2025/26); o ogol rotula o Zagłębie Sosnowiec de 1985/86 como Zagłębie Wałbrzych (os 30 placares são os do Sosnowiec).
- **nor-1:** Identidade: clube e departamento de futebol com artigos separados na Wikipédia como um clube só (Vålerengens IF e Vålerenga Fotball, como a RSSSF; Mjøndalen, Sogndal, Ranheim, Strømsgodset, Kongsvinger, Lyn); refundados à parte (Sarpsborg FK x Sarpsborg 08, Kristiansund FK x BK, Sandefjord BK x Sandefjord Fotball, que o ogol junta num código).
- **nor-1:** Norgesserien: classificação pelo mata-mata e depois pela posição no grupo, com os números da tabela do grupo; jogos extras do mata-mata sem o mando (a Wikipédia não diz).
- **nor-1:** 1987: o vencedor dos pênaltis de Molde x Lillestrøm (0-0) saiu da contagem da tabela da Wikipédia (o placar dos pênaltis não está nas fontes).
- **den-1:** Identidade: KB, B 1903 e FC København separados (como a RSSSF); pelos links, Horsens fS = AC Horsens, Farum = Nordsjælland, Haderslev = SønderjyskE, B 1901 = Nykøbing FC, Helsingør IF = FC Helsingør; em 1976 a matriz da Wikipédia liga o Randers Freja ao Randers FC (fica o Freja, pela tabela); o BK Viktoria de 1928/29 sem cidade confirmada.
- **den-1:** Antes de 1945: ordem pela final e pelo mata-mata, depois pela tabela; números da tabela mais os do mata-mata.
- **den-1:** Superliga com grupos (1991/92-1994/95 e desde 2016/17): fase regular pelo primeiro encontro de cada par (o ogol não numera as rodadas); 2016/17 completado pelo football-data nos grupos de classificação; do 7º ao 14º de 2016/17 a 2019/20 pela fase regular.
- **cyp-1:** Pontos 3-2-1 de 1960/61 a 1969/70, como a RSSSF anota (a Wikipédia calcula com 2-1-0).
- **cyp-1:** Identidade: AEK Larnaca separado do EPA e do Pezoporikos; AEP Paphos separado do Evagoras e do APOP Paphos; APOEL, AEL Limassol, EPA Larnaca e Olympiakos Nicosia com o mesmo nome do gre-1.
- **cyp-1:** 2008/09: APOEL x Omonia suspenso, como derrota para os dois (a tabela da Wikipédia); 2007/08 e 2008/09: grupos intermediário e de rebaixamento pela matriz da Wikipédia (o ogol não tem).

## Próximas ligas

- Na ordem do ranking de coeficientes da UEFA (foto de 24/11/2026), da mais bem colocada à menos: a tabela está em `COMECE-AQUI.md`, seção 3. Prontas desde a nova ordem: Grécia (`gre-1`), Tchéquia (`cze-1`), Tchecoslováquia (`tch-1`), Polônia (`pol-1`), Noruega (`nor-1`) e Dinamarca (`den-1`) e Chipre (`cyp-1`); a próxima é a Suíça. Uma por vez, com o escopo antes.
