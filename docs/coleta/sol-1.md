# Coleta: Campeonato Salomonense (`sol-1`)

Gerado por `python coleta/sol-1/importar.py`. Pacote em `data/coleta/sol-1/pacote/`.

## Resumo

- 25 edições (2000 a 2025), 21 com jogos; 1464 jogos, 5857 gols, 104 com autor.
- Escopo aprovado pelo Guilherme em 25/11/2026, depois de pesquisa a fundo (docstrings de `coleta/sol-1/edicoes.py` e `coleta/sol-1/clubes_sol.py`):
  - o campeonato nacional de clubes (2000 a 2009/10) e a S-League (2010/11 a 2025), como a lista de campeões da RSSSF; ficam de fora a liga de Honiara (1947-1999), a "S-League" de franquias de Honiara (2004 e 2005), a Solomon Cup e o Interprovincial (seleções de província), o Knockout Championship, os playoffs da OFC e 2026 (título pendente);
  - 2015/16 = Western United (playoff final; a Wikipédia dá o Solomon Warriors, 1º da fase regular); 2024 = Central Coast (o ogol dá o Real Kakamora);
  - clubes: "Solomon Warriors" (Uncles), "Marist" (Marist Fire), "KOSSA", "Real Kakamora", "Laugu United", "Central Coast"; homônimos do banco com a cidade ou a província ("Southern United Honiara", "Northern United Malaita", "Kula FC (Ilhas Salomão)").
- Pontuação: 3 por vitória, 1 por empate.

## Fontes

- **RSSSF** (`data/coleta/sol-1/rsssf/`, `baixar_rsssf.py`): lista de campeões e uma página por temporada.
- **Wikipédia em inglês** (`data/coleta/sol-1/wikipedia/`, `baixar_wikipedia.py`): segunda fonte do campeão.
- **ogol** (`data/coleta/sol-1/ogol/`, cache em `data/cache/ogol-sol-1/`, `baixar_ogol.py`): datas dos jogos sem data e a grafia dos times para os escudos.

## Correções e decisões

- `solom07`, linha 85: "Koloale  FC" -> "Koloale FC": espaço duplo no meio do nome (o leitor lia só "FC").
- `solom2013`, linha 32: "-.Marist" -> "9.Marist": o desclassificado vem sem posição ("-.") e o leitor pulava a linha.
- `solom2013`, linha 133: "-.Marist" -> "9.Marist": o desclassificado vem sem posição ("-.") e o leitor pulava a linha.
- `solom2013`, linha 208: "-.Marist" -> "9.Marist": o desclassificado vem sem posição ("-.") e o leitor pulava a linha.
- `solom2013`, linha 33: "disqualified; playing record;      4   1  2  1   2- 2   5" -> "[playing record before disqualification: 4 games, 1 win, 2 draws, 1 loss, goals 2-2]": a campanha do Marist antes da desclassificação, numa linha sem nome, era lida como linha de tabela.
- `solom2013`, linha 134: "disqualified; playing record;      4   1  2  1   2- 2   5" -> "[playing record before disqualification: 4 games, 1 win, 2 draws, 1 loss, goals 2-2]": a campanha do Marist antes da desclassificação, numa linha sem nome, era lida como linha de tabela.
- `solom2013`, linha 209: "disqualified; playing record;      4   1  2  1   2- 2   5" -> "[playing record before disqualification: 4 games, 1 win, 2 draws, 1 loss, goals 2-2]": a campanha do Marist antes da desclassificação, numa linha sem nome, era lida como linha de tabela.
- `solom2010`, linha 86: "[awarded to Rendova Devon as" -> "[awarded to Rendova Devon as Northern United used Koloale players who had not been released]": a nota continua nas três linhas de baixo, ao lado de outros jogos.
- `solom2010`, linha 87: "Northern United used Koloale" -> "": pedaço da nota do jogo de cima.
- `solom2010`, linha 88: "players who had not been" -> "": pedaço da nota do jogo de cima.
- `solom2010`, linha 89: "released]" -> "": fim da nota do jogo de cima.
- `solom2011`, linha 69: "[awarded 0-3; originally 3-1;" -> "[awarded 0-3; originally 3-1; KOSSA used an unregistered player]": a nota continua nas duas linhas de baixo.
- `solom2011`, linha 70: "KOSSA used an unregistered" -> "": pedaço da nota do jogo de cima, ao lado da data.
- `solom2011`, linha 71: "player]" -> "": fim da nota do jogo de cima.
- `solom2025`, linha 215: "[match postponed on Sep 28 due to weather" -> "[match postponed on Sep 28 due to weather conditions and not refixtured but awarded as 0-0 in the standings]": a nota continua nas duas linhas de baixo.
- `solom2025`, linha 216: "conditions and not refixtured but awarded" -> "": pedaço da nota do jogo de cima.
- `solom2025`, linha 217: "as 0-0 in the standings]" -> "": fim da nota do jogo de cima, ao lado do "Round 17".
- `solom04 / 28`: final por W.O.: o Makuru, de dono adventista, não joga aos sábados.
- `solom2010 / 86`: 5-1 em campo, mas os pontos foram dados ao Rendova Devon (o Northern United usou jogadores do Koloale que não tinham sido liberados); a tabela conta vitória sem gols.
- `solom06 / 82`: semifinal abandonada (chuva forte) e jogada de novo em 01/03 (Koloale 2-1).
- `solom09 / 80`: abandonado aos 72' com 3-2 (briga na torcida); não entra na tabela.
- `solom2025 / 108`: abandonado aos 24' (chuva forte) e jogado de novo no dia seguinte (Malaita Kingz 1-0).
- 2015/16: 3º lugar KOSSA: a disputa do 3º lugar está na página como "KOSSA bt Solomon Warriors" (vitória, placar desconhecido).

## Divergências que ficam

- **2005/06:** seis jogos da fase de grupos estão na página sem placar ("drw" e "bt": Tematangi x Mafi, Tematangi x Kuara, Camp United x Ngaube, Marist x Kuara, Koloale x Camp United, Aimela x Ngaube); as tabelas os contam e eles ficam de fora dos jogos (a página avisa: "missing goals of various matches").
- **2006/07:** a tabela do grupo A é de antes da última rodada (Koloale 2-1 Marist vem depois dela), e os jogos com "-" (sem placar) não estão em nenhuma das duas.
- **2009/10:** um jogo do grupo B está na página só como vitória sem placar ("Rendova Devon bt Ka'arua"); a tabela o conta ("w/o goals") e ele fica de fora dos jogos.
- **2010/11:** os 4 jogos da 12ª rodada estão na página só com o resultado, sem placar ("drw", "lt"); a tabela os conta ("w/o goals round 12") e eles ficam de fora dos jogos.

## Edição a edição

| Temporada | Formato | Jogos | Esperados | Gols | Com autor | Campeão | Vice | Observação |
|---|---|---|---|---|---|---|---|---|
| 2000 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Laugu United |  | só o campeão na RSSSF |
| 2001 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Koloale |  | só o campeão na RSSSF |
| 2002 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Koloale |  | só o campeão na RSSSF |
| 2003 | fase de grupos (8 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 16 | 16 | 87 | 0 | Koloale | Auki Kingz | em Yandina, em novembro |
| 2004 | jogos incompletos: final; 3 pontos por vitória, 1 por empate e 0 por derrota | 1 | 1 | 0 | 0 | Central Realas | Makuru | a RSSSF dá os 9 inscritos (2 grupos) e a final, vencida por W.O.: o Makuru, de dono adventista, não joga aos sábados; só a final na RSSSF |
| 2005/06 | jogos incompletos: fase de grupos (11 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 24 | 30 | 123 | 1 | Marist | Koloale | em Honiara, de 20/02 a 01/03/2006; a página dá alguns jogos da fase de grupos sem placar (só "drw" ou "bt") |
| 2006/07 | jogos incompletos: fase de grupos (9 clubes) + semifinais + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 13 | 12 | 75 | 0 | KOSSA | Koloale | em maio de 2007; a página não traz o placar de 4 jogos da fase de grupos (as tabelas são parciais) |
| 2007/08 | fase de grupos (12 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 34 | 34 | 151 | 80 | Koloale | Makuru | em junho de 2008 |
| 2008/09 | fase de grupos (12 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 35 | 35 | 162 | 13 | Marist | Koloale | em junho de 2009 |
| 2009/10 | fase de grupos (14 clubes) + quartas de final + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 33 | 34 | 117 | 10 | Koloale | Solomon Warriors | em maio de 2010 |
| 2010/11 | jogos incompletos: pontos corridos (8 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 52 | 56 | 177 | 0 | Koloale | Solomon Warriors | 1ª Telekom S-League (fevereiro a maio de 2011); a página não traz o placar dos 4 jogos da 12ª rodada |
| 2011/12 | só a tabela final (sem jogos); 3 pontos por vitória | 0 | 0 | 0 | 0 | Solomon Warriors | Western United | a RSSSF só tem a tabela final |
| 2013/14 | pontos corridos (9 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 64 | 64 | 253 | 0 | Solomon Warriors | KOSSA | Marist desclassificado em 08/11 (não pagou a inscrição): os jogos do 1º turno viraram 0-3 |
| 2014/15 | pontos corridos (9 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 72 | 72 | 255 | 0 | Western United | Solomon Warriors |  |
| 2015/16 | jogos incompletos: fase regular (9 clubes) + quartas de final + semifinais + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 82 | 82 | 325 | 0 | Western United | Koloale | fase regular (1º o Solomon Warriors) e playoff dos 8 primeiros; o campeão é o do playoff (RSSSF; a Wikipédia dá o Solomon Warriors); o jogo de volta Western United x Real Kakamora (quartas) está na página sem placar ("unk", 2-1 no intervalo); Wikipédia: Solomon Warriors |
| 2016 | pontos corridos (9 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 72 | 72 | 345 | 0 | Marist | Western United | Koloale suspenso em 04/12 ("non-compliance"): os 5 jogos restantes viraram 0-3 |
| 2017/18 | fase regular (8 clubes) + quartas de final + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 68 | 68 | 295 | 0 | Solomon Warriors | Marist | fase regular (agosto a novembro de 2017) e o playoff dos 8 primeiros ("TSL Championship", março de 2018); o Solomon Warriors ganhou os dois |
| 2018 | pontos corridos (8 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 56 | 56 | 252 | 0 | Solomon Warriors | Henderson Eels |  |
| 2019/20 | pontos corridos (9 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 71 | 71 | 364 | 0 | Solomon Warriors | Henderson Eels |  |
| 2020/21 | pontos corridos (11 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 110 | 110 | 476 | 0 | Henderson Eels | Solomon Warriors |  |
| 2021 | pontos corridos (12 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 132 | 132 | 408 | 0 | Central Coast | Solomon Warriors |  |
| 2022/23 | pontos corridos (12 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 132 | 132 | 527 | 0 | Solomon Warriors | KOSSA |  |
| 2023 | pontos corridos (12 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 132 | 132 | 475 | 0 | Solomon Warriors | Central Coast |  |
| 2024 | pontos corridos (12 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 132 | 132 | 503 | 0 | Central Coast | Solomon Warriors |  |
| 2025 | pontos corridos (12 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 133 | 133 | 487 | 0 | Central Coast | Malaita Kingz | a liga passa a se chamar só "S-League" |

## O que não deu para coletar

- 2000-2002: só o campeão; 2004: só a final (W.O.); 2011/12: só a tabela final.
- Jogos sem placar na página (2005/06, 2006/07, 2009/10, 2010/11, 2015/16: ver as divergências).
- Autores dos gols (poucos), artilheiros, cartões, estádio e público.
