# Coleta Europa — documentação

Gerado por `python coleta/comum-europa/documentar.py`. Uma ficha por liga, com tudo o que o pacote tem, a cobertura de cada campo década a década, o formato do campeonato ao longo do tempo, campeões, punições, todas as correções e decisões com o motivo, o que não deu para coletar e as pendências.

Regras de trabalho, ordem das pendências e como fazer uma liga nova: `coleta/comum-europa/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-europa.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-europa`).

| Liga | Temporadas | Jogos | Gols c/ autor | Cartões | Clubes | Tabelas ok / div. | Pendências | Ficha |
|---|---|---|---|---|---|---|---|---|
| Campeonato Inglês | 127 (1888/89–2025/26) | 51330 | 25878 | 33166 | 65 | 226 / 1 | 2 | [eng-1](eng-1.md) |
| Campeonato Espanhol | 95 (1928/29–2025/26) | 27716 | 25072 | 51662 | 63 | 180 / 11 | 1 | [esp-1](esp-1.md) |
| Campeonato Italiano | 124 (1929/30–1928/29) | 34729 | 24591 | 43962 | 191 | 268 / 42 | 5 | [ita-1](ita-1.md) |
| Campeonato Alemão | 124 (1963/64–1962/63) | 20303 | 56842 | 30251 | 194 | 181 / 7 | 6 | [ger-1](ger-1.md) |
| Campeonato Francês | 88 (1932/33–2025/26) | 30466 | 22613 | 35434 | 77 | 153 / 21 | 6 | [fra-1](fra-1.md) |
| Campeonato Português | 92 (1934/35–2025/26) | 20978 | 18958 | 30915 | 73 | 171 / 13 | 3 | [por-1](por-1.md) |
| Campeonato Holandês | 138 (1956/57–1955/56) | 21878 | 23019 | 24431 | 93 | 191 / 3 | 4 | [ned-1](ned-1.md) |
| Campeonato Escocês | 129 (1890/91–2025/26) | 33076 | 14565 | 19812 | 46 | 197 / 60 | 3 | [sco-1](sco-1.md) |
| Campeonato Belga | 123 (1895/96–2025/26) | 28712 | 12031 | 18167 | 81 | 185 / 83 | 5 | [bel-1](bel-1.md) |
| Campeonato Turco | 97 (1959–1957/58 (Federasyon Kupası)) | 20971 | 13891 | 23395 | 168 | 128 / 30 | 5 | [tur-1](tur-1.md) |
| Campeonato da Alemanha Oriental | 44 (1948–1990/91) | 8062 | 0 | 0 | 52 | 65 / 19 | 3 | [gdr-1](gdr-1.md) |

## Pendências de todas as ligas

- **eng-1:** Nomes de jogadores da ESPN em formato de documento (sobrenomes na frente, ex.: "Goncalves da Silva Ailton"): os casos mais frequentes estão em coleta/comum-europa/nomes_jogadores.py, aplicado em todas as ligas; a varredura completa dos ~2 mil nomes com 3 palavras ou mais, nas 8 ligas, fica pendente (conferir com o BDFutbol ou a Wikipédia).
- **eng-1:** Autores dos gols e cartões antes de 2001/02: nenhuma fonte em lote; seria jogo a jogo (ficha do ogol).
- **esp-1:** Autores dos gols e cartões antes de 2001/02: a RSSSF tem de 2000/01 em diante; antes, jogo a jogo (ficha do ogol).
- **ita-1:** Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).
- **ita-1:** Era antiga (1898 a 1928/29, IT-017, em antigo.py): 29 edições pela Wikipédia em italiano. 713 jogos vêm só do Tabellone (sem data); 37 classificações de grupo diferem dos jogos (quase todas em 1 ou 2 gols, ou um jogo que o calendário não traz), listadas no relatório. Conferir com a RSSSF (italhist98-25.html e ital24-29.html, já baixadas em data/coleta/ita-1/rsssf-antigo/, só com tabelas a partir de 1909/10) e com o Almanacco Illustrato.
- **ita-1:** Era antiga: a classificação final de cada edição é montada (campeão do albo d'oro, depois a fase alcançada e a posição no grupo); não há classificação oficial além do campeão.
- **ita-1:** Correções da revisão de 23/11 que vivem em arquivos, não em dicionários: 674 datas em data/coleta/ita-1/correcoes/datas.csv (IT-008, IT-009 e o complemento de 37 datas de 1933/34, 1934/35 e 1974/75, sem o qual sobravam clubes com 2 jogos no mesmo dia) e 31 jogos a tavolino em correcoes/tavolino.csv (IT-010).
- **ita-1:** Triangular de rebaixamento de 1953/54 (Udinese, SPAL, Palermo) sem os placares: a Wikipédia it só traz a tabela.
- **ger-1:** Revisão DE-004: 3 datas em que só o transfermarkt discorda da base (Dortmund x Duisburg 1964/65, Colônia x Werder 1969/70, Colônia x Braunschweig 1978/79); conferir na ficha do jogo do transfermarkt ou num jornal antes de mudar.
- **ger-1:** Autores dos gols: RSSSF (1963/64-1998/99, só os jogos em que a soma fecha, cerca de 97%), ficha do ogol (1999/00, 2000/01 e os jogos em que a ESPN falta ou não fecha) e ESPN (2001/02+). Os jogos que nenhuma das três fecha ficam sem autor; cartões só pela ESPN.
- **ger-1:** Era antiga (1902/03-1962/63, em antigo.py): entra só a fase final; as ligas regionais (Oberligen, Gauligen e as ligas de antes) ficam de fora. Pendência se o painel quiser mostrar as regionais.
- **ger-1:** Era antiga: gols com autor só nas partidas com ficha (football box) na Wikipédia, quase sempre a final; artilheiros da fase final não coletados (a infobox da Wikipédia tem o artilheiro de cada temporada).
- **ger-1:** Era antiga: 1947/48, três placares diferentes entre RSSSF e Wikipédia (en) nas quartas e na semifinal; ficou a RSSSF. Conferir numa terceira fonte (kicker, Wikipédia em alemão).
- **ger-1:** Era antiga: a classificação final é o campeão, o vice e depois a fase alcançada (na mesma fase, posição no grupo e campanha); não existe classificação oficial além do campeão e do vice.
- **fra-1:** Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).
- **fra-1:** Datas dos 356 jogos dos anos 1930 que nenhuma fonte tem.
- **fra-1:** Revisão FR-009: 99 jogos (1948/49-1998/99) em que o transfermarkt e o ogol diferem da base por 1 ou 2 dias; só os 41 de 3 dias ou mais foram corrigidos. Conferir uma rodada num jornal (L'Équipe na Gallica) antes de trocar os outros.
- **fra-1:** Revisão FR-017: 4 pares de jogos em que a Wikipédia fr dá outro mando ou placar (1935/36, 1937/38, 1945/46, 1950/51); fica a base até conferir num jornal da época (anotado em EXPLICACOES).
- **fra-1:** Revisão FR-005: a vitória do Marseille sobre o Bordeaux em 27/10/1946 (0-0 no tribunal) vem das tabelas das Wikipédias; conferir no L'Équipe de 28/10/1946.
- **fra-1:** Árbitro: os arquivos do football-data da França não trazem (revisão FR-022); seria jogo a jogo pelo transfermarkt.
- **por-1:** Autores dos gols: RSSSF (1999/00-2005/06, onde a soma fecha), ficha do ogol (2001/02, que a RSSSF não traz, e os jogos em que a ESPN falta ou não fecha) e ESPN (2006/07+). Antes de 1999/00, nenhuma fonte em lote. Sem autor ficam 103 jogos de 2001/02 e 27 de 2010/11 (a ficha do ogol também não fecha).
- **por-1:** Revisão PT-020: árbitro e público pelo transfermarkt (jogo a jogo, ~11 mil páginas) ou pela ficha do ogol: não feito (custo alto); o football-data de Portugal não traz árbitro.
- **por-1:** Revisão PT-010: Belenenses x Sporting (1938/39) e os dois jogos do Académico do Porto em 04/02/1940 (1939/40) seguem com a data do ogol; o transfermarkt repete o ogol e a ficha não decide. Conferir num jornal da época.
- **ned-1:** Era antiga (1888/89-1955/56, em antigo.py): de 1888/89 a 1896/97 e nas temporadas sem a fase final legível na RSSSF, só o campeão e a tabela da Eerste Klasse, sem jogos; os jogos da fase final vêm da matriz da RSSSF, sem data (datados só em 1954/55 e 1955/56). As ligas regionais ficam de fora.
- **ned-1:** Era antiga: tabelas da fase final que não fecham com os jogos por erro de digitação da RSSSF (1906/07, 1922/23, 1923/24); ficam anotadas no relatório, sem explicação escrita.
- **ned-1:** Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).
- **ned-1:** Identidade de clubes em fusões (GVAV x FC Groningen, SC Enschede x FC Twente, Rapid JC x Roda JC, Alkmaar '54 x AZ, BVV x FC Den Bosch): separados como clubes diferentes, contra o ogol, que junta alguns na ficha do sucessor; vale a revisão conferir.
- **sco-1:** Autores dos gols e cartões antes da ESPN (2001/02): jogo a jogo (ficha do ogol).
- **sco-1:** Rodada vazia até os anos 1930 em várias temporadas: não havia rodadas fixas (como no Inglês) e o ogol não traz.
- **sco-1:** Temporadas em que as duas tabelas publicadas erram em clubes diferentes: o ogol fecha com uma delas em cada clube; a revisão pode conferir com uma terceira fonte (jornais da época, fitbastats.com, statto.com).
- **bel-1:** Antes de 1960/61: jogos só pela matriz da Wikipédia, sem data nem rodada (o ogol não tem); quando a soma não fecha com a tabela da RSSSF, a classificação final fica com os números publicados (observação na linha). Conferir a matriz com outra fonte jogo a jogo (jornais da época, nl/fr.wikipedia) seria o próximo passo.
- **bel-1:** 1898/99, 1899/00, 1901/02, 1902/03 e 1903/04 (grupos): só as tabelas da RSSSF e os jogos finais e de desempate; sem os jogos dos grupos e sem classificação oficial além do campeão e do torneio final.
- **bel-1:** Autores dos gols e cartões: só com a ESPN (2006/07+), que não tem lances de 2011/12 a 2014/15 nem dos play-offs; antes e nesses anos, jogo a jogo (ficha do ogol).
- **bel-1:** Jogos de play-off de acesso e rebaixamento contra clubes da 2ª divisão (até 2008/09) ficam de fora; desde 2016/17 os clubes da 2ª divisão no play-off europeu entram nos jogos, mas não na classificação final.
- **bel-1:** Artilheiros só desde 1945/46 (lista da RSSSF).
- **tur-1:** Era antiga (antes de 1959, em antigo.py): Türkiye Futbol Şampiyonası (16 edições), Millî Küme (11) e Federasyon Kupası (2), pela Wikipédia (en) e conferidas com a RSSSF. Só as Federasyon Kupası têm campeão (a federação as reconhece desde 2002); Şampiyonası e Millî Küme ficam com o vencedor na observação (regra D-09). Os jogos do Şampiyonası de 1924 a 1935 e as matrizes da Millî Küme não têm data (só as fichas trazem).
- **tur-1:** 1962/63: os jogos do grupo de classificação (7º a 9º de cada grupo) não estão no ogol nem na Wikipédia; entra a tabela.
- **tur-1:** Autores dos gols e cartões: só com a ESPN (2006/07+), que quase não tem lances de 2011/12 a 2014/15 nem dos play-offs de 2011/12; antes e nesses anos, jogo a jogo (ficha do ogol).
- **tur-1:** Kayseri: o Kayserispor de 1966 a 2004 está como Kayseri Erciyesspor (troca de nomes de 2004, como na Wikipédia); vale a revisão conferir, porque o ogol e boa parte da imprensa contam a história no Kayserispor de hoje.
- **tur-1:** Placares do ogol que só a matriz da Wikipédia contesta nas temporadas antigas (sem football-data nem engsoccerdata antes de 1994/95): ficam os do ogol, que fecham com as tabelas.
- **gdr-1:** Autores dos gols, público e estádio dos jogos da Oberliga: a RSSSF traz só o placar; fonte possível: as fichas do weltfussball.de ou o arquivo do jornal Neues Deutschland.
- **gdr-1:** 1948 e 1949: só a fase final (mata-mata entre os campeões estaduais); os campeonatos estaduais ficam de fora.
- **gdr-1:** Punições de pontos que só a tabela da RSSSF traz (1966/67, 1967/68, 1973/74, 1990/91): os pontos oficiais vão para a classificação e a diferença para ajuste_pontos; o motivo de cada uma não está nas fontes.

## Próximas ligas

- `ned-1` (Holanda), depois Escócia, Bélgica e Turquia (guia geral `docs/agentes-internacionais-COMECE-AQUI.md`), uma por vez e só com o ok do Guilherme.
