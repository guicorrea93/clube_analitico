# Coleta Europa — documentação

Gerado por `python coleta/comum-europa/documentar.py`. Uma ficha por liga, com tudo o que o pacote tem, a cobertura de cada campo década a década, o formato do campeonato ao longo do tempo, campeões, punições, todas as correções e decisões com o motivo, o que não deu para coletar e as pendências.

Regras de trabalho, ordem das pendências e como fazer uma liga nova: `coleta/comum-europa/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-europa.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-europa`).

| Liga | Temporadas | Jogos | Gols c/ autor | Cartões | Clubes | Tabelas ok / div. | Pendências | Ficha |
|---|---|---|---|---|---|---|---|---|
| Campeonato Inglês | 127 (1888/89–2025/26) | 51330 | 25841 | 33166 | 65 | 226 / 1 | 2 | [eng-1](eng-1.md) |
| Campeonato Espanhol | 95 (1928/29–2025/26) | 27716 | 25072 | 51662 | 63 | 180 / 11 | 1 | [esp-1](esp-1.md) |
| Campeonato Italiano | 95 (1929/30–2025/26) | 29271 | 24564 | 43962 | 69 | 167 / 5 | 4 | [ita-1](ita-1.md) |
| Campeonato Alemão | 124 (1963/64–1962/63) | 20303 | 22700 | 30251 | 194 | 183 / 5 | 4 | [ger-1](ger-1.md) |
| Campeonato Francês | 88 (1932/33–2025/26) | 30466 | 22613 | 35434 | 76 | 156 / 18 | 2 | [fra-1](fra-1.md) |
| Campeonato Português | 92 (1934/35–2025/26) | 20978 | 13874 | 30915 | 73 | 175 / 9 | 2 | [por-1](por-1.md) |
| Campeonato Holandês | 138 (1956/57–1955/56) | 21878 | 23019 | 24431 | 93 | 191 / 3 | 4 | [ned-1](ned-1.md) |
| Campeonato Escocês | 129 (1890/91–2025/26) | 33076 | 14565 | 19812 | 46 | 197 / 60 | 3 | [sco-1](sco-1.md) |

## Pendências de todas as ligas

- **eng-1:** EN-016 (revisão, baixa): 12 jogos de 2002/03 a 2016/17 sem nenhum gol com autor (a soma dos gols da ESPN não bate com o placar). Precisa de outra fonte jogo a jogo (ficha do ogol ou 11v11).
- **eng-1:** Autores dos gols e cartões antes de 2001/02: nenhuma fonte em lote; seria jogo a jogo (ficha do ogol).
- **esp-1:** Autores dos gols e cartões antes de 2001/02: a RSSSF tem de 2000/01 em diante; antes, jogo a jogo (ficha do ogol).
- **ita-1:** Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).
- **ita-1:** Campeonatos de 1898 a 1928/29 (revisão IT-017; decisão D-05: incluir, com grupos regionais e finais): na fila da coleta, depois de bel-1 e tur-1.
- **ita-1:** Correções da revisão de 23/11 que vivem em arquivos, não em dicionários: 674 datas em data/coleta/ita-1/correcoes/datas.csv (IT-008, IT-009 e o complemento de 37 datas de 1933/34, 1934/35 e 1974/75, sem o qual sobravam clubes com 2 jogos no mesmo dia) e 31 jogos a tavolino em correcoes/tavolino.csv (IT-010).
- **ita-1:** Triangular de rebaixamento de 1953/54 (Udinese, SPAL, Palermo) sem os placares: a Wikipédia it só traz a tabela.
- **ger-1:** Era antiga (1902/03-1962/63, em antigo.py): entra só a fase final; as ligas regionais (Oberligen, Gauligen e as ligas de antes) ficam de fora. Pendência se o painel quiser mostrar as regionais.
- **ger-1:** Era antiga: gols com autor só nas partidas com ficha (football box) na Wikipédia, quase sempre a final; artilheiros da fase final não coletados (a infobox da Wikipédia tem o artilheiro de cada temporada).
- **ger-1:** Era antiga: 1947/48, três placares diferentes entre RSSSF e Wikipédia (en) nas quartas e na semifinal; ficou a RSSSF. Conferir numa terceira fonte (kicker, Wikipédia em alemão).
- **ger-1:** Era antiga: a classificação final é o campeão, o vice e depois a fase alcançada (na mesma fase, posição no grupo e campanha); não existe classificação oficial além do campeão e do vice.
- **fra-1:** Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).
- **fra-1:** Datas dos 356 jogos dos anos 1930 que nenhuma fonte tem.
- **por-1:** Autores dos gols e cartões antes de 2006/07 (a ESPN começa aí): jogo a jogo (ficha do ogol).
- **por-1:** Pontos do Porto em 2007/08 (Apito Final): ficou o desconto de 6, como no fim da temporada; se o Guilherme preferir a situação de hoje (absolvição em 2017), tirar o desconto em importar.py.
- **ned-1:** Era antiga (1888/89-1955/56, em antigo.py): de 1888/89 a 1896/97 e nas temporadas sem a fase final legível na RSSSF, só o campeão e a tabela da Eerste Klasse, sem jogos; os jogos da fase final vêm da matriz da RSSSF, sem data (datados só em 1954/55 e 1955/56). As ligas regionais ficam de fora.
- **ned-1:** Era antiga: tabelas da fase final que não fecham com os jogos por erro de digitação da RSSSF (1906/07, 1922/23, 1923/24); ficam anotadas no relatório, sem explicação escrita.
- **ned-1:** Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).
- **ned-1:** Identidade de clubes em fusões (GVAV x FC Groningen, SC Enschede x FC Twente, Rapid JC x Roda JC, Alkmaar '54 x AZ, BVV x FC Den Bosch): separados como clubes diferentes, contra o ogol, que junta alguns na ficha do sucessor; vale a revisão conferir.
- **sco-1:** Autores dos gols e cartões antes da ESPN (2001/02): jogo a jogo (ficha do ogol).
- **sco-1:** Rodada vazia até os anos 1930 em várias temporadas: não havia rodadas fixas (como no Inglês) e o ogol não traz.
- **sco-1:** Temporadas em que as duas tabelas publicadas erram em clubes diferentes: o ogol fecha com uma delas em cada clube; a revisão pode conferir com uma terceira fonte (jornais da época, fitbastats.com, statto.com).

## Próximas ligas

- `ned-1` (Holanda), depois Escócia, Bélgica e Turquia (guia geral `docs/agentes-internacionais-COMECE-AQUI.md`), uma por vez e só com o ok do Guilherme.
