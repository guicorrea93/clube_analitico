# Coleta: Campeonato Papua-Nova-Guineense (`png-1`)

Gerado por `python coleta/png-1/importar.py`. Pacote em `data/coleta/png-1/pacote/`.

## Resumo

- 19 edições (2006 a 2026), 19 com jogos; 1336 jogos, 4701 gols, 541 com autor.
- Escopo aprovado pelo Guilherme em 24/11/2026, depois de pesquisa a fundo (docstrings de `coleta/png-1/edicoes.py` e `coleta/png-1/clubes_png.py`):
  - só a National Soccer League (2006-2022) / Premier Soccer League (2023-), uma edição por título; ficam de fora o campeonato amador de clubes (1976-2005), a temporada 2021 (abandonada, sem campeão) e a National Premier League rebelde (2017-2018);
  - 2008/09 e 2017: a final não foi jogada (campeão o 1º da fase regular); 2014: final abandonada com 0-3, resultado mantido; 2026: sem playoff;
  - clubes: "Lae City" (Lae City Dwellers 2014-2017, Toti City, Lae City: os 7 títulos) e o novo "Lae City Dwellers" (2021) separados; "Hekari United" (PRK Souths, Hekari Souths, PNG Hekari); "Morobe United" (Blue Kumuls, Morobe Kumuls, Gigira Laitepo Morobe, Welgris Morobe United); "Gulf Komara" (Erema); "Madang FC" (Flying Fox, Fox, Madang United); "Rapatona" (CMSS Rapatona Tigers); "Port Moresby Strikers" (Southern Strikers); "Besta PNG United" (a seleção sub-20 de 2009/10 e 2010/11).
- Pontuação: 3 por vitória, 1 por empate.

## Fontes

- **RSSSF** (`data/coleta/png-1/rsssf/`, `baixar_rsssf.py`): lista de campeões e uma página por temporada.
- **Wikipédia em inglês** (`data/coleta/png-1/wikipedia/`, `baixar_wikipedia.py`): segunda fonte do campeão.
- **ogol** (`data/coleta/png-1/ogol/`, cache em `data/cache/ogol-png-1/`, `baixar_ogol.py`): datas dos jogos sem data e a grafia dos times para os escudos (2013 em diante).

## Correções e decisões

- `png2014`, linha 89: "[abandoned at 1-0 in 89' due to" -> "[abandoned at 1-0 in 89' due to crowd trouble]": a nota continua na linha de baixo, ao lado do jogo seguinte.
- `png2014`, linha 90: "crowd trouble]" -> "": o fim da nota de cima (não é nota deste jogo).
- `png2018 / 95`: jogo não disputado: a federação deu derrota por 0-3 aos dois clubes ("awarded 0-3 against both clubs"; a tabela da página conta os 3 gols contra para cada um).
- `png2018 / 146`: jogo não disputado: a federação deu derrota por 0-3 aos dois clubes ("awarded 0-3 against both clubs"; a tabela da página conta os 3 gols contra para cada um).
- `png06 / 171`: semifinal abandonada com 0-0 por falta de luz e jogada de novo no dia seguinte (5-6 na prorrogação).
- `png06 / 174`: nota da página ("[aet] [replay]") reescrita.
- `png2014 / 89`: abandonado aos 89' com 1-0 (briga na torcida); não foi jogado de novo nem entrou na tabela.
- `png2019 / 471`: quartas de final abandonadas aos 48' com 0-0 (campo alagado) e jogadas de novo em 16/05.
- `png2022 / 88`: abandonado aos 57' com 2-0 (falta de luz) e jogado de novo em 23/11 (4-2).
- `png2025 / 291`: o Hekari United não se apresentou ("dns"): W.O. para o Lae City, 3º lugar.
- `png2014 / 152`: a final foi abandonada aos 70' com 0-3 (violência da torcida); o resultado ficou e o Hekari United foi o campeão (lista de campeões da RSSSF).
- 2014: 3º lugar Morobe United: a disputa do 3º lugar está na página como "Gigira Laitepo Morobe bt Oro [aet]" (vitória na prorrogação, placar desconhecido).
- tabela `png2023`, linha 133, fora da conferência: tabela depois da 11ª rodada (a final vem no fim da fase).

## Divergências que ficam

- **2023:** dois jogos da 12ª rodada (United Highlands x Lae City e Lae City Dwellers x Morobe Wawens, este abandonado no 2º tempo) estão na página como empate sem placar ("drw"); a tabela os conta como empates e eles ficam de fora dos jogos.
- **2025:** um jogo remarcado da 15ª rodada (Morobe Wawens x Hekari United, 1-0 no intervalo) está na página como empate sem placar; a tabela o conta como empate e ele fica de fora dos jogos.
- **2026:** dois jogos do Lae City (Lae City Dwellers x Lae City, 17ª rodada, "possivelmente 1-3"; Finschhafen Bavarians x Lae City, 18ª) estão na página só como derrota do mandante, sem placar ("lt"); a tabela os conta e eles ficam de fora dos jogos.

## Edição a edição

| Temporada | Formato | Jogos | Esperados | Gols | Com autor | Campeão | Vice | Observação |
|---|---|---|---|---|---|---|---|---|
| 2006 | fase regular (5 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 25 | 25 | 75 | 4 | Hekari United | Gelle Hills United |  |
| 2007/08 | fase regular (7 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 46 | 46 | 173 | 126 | Hekari United | Gelle Hills United |  |
| 2008/09 | fase regular (8 clubes) + semifinais; 3 pontos por vitória, 1 por empate e 0 por derrota | 58 | 58 | 173 | 4 | Hekari United | Rapatona | a final (Hekari Souths United x CMSS Rapatona Tigers) não foi jogada: o Hekari, 1º da fase regular, foi declarado campeão |
| 2009/10 | fase regular (9 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 75 | 75 | 283 | 57 | Hekari United | Morobe United |  |
| 2010/11 | fase regular (7 clubes) + semifinais + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 44 | 44 | 167 | 0 | Hekari United | Eastern Stars |  |
| 2011/12 | jogos incompletos: fase regular (7 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 4 | 4 | 12 | 7 | Hekari United | Eastern Stars | a RSSSF só tem a tabela da fase regular e o mata-mata |
| 2013 | fase regular (8 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 60 | 60 | 199 | 13 | Hekari United | FC Port Moresby |  |
| 2014 | fase regular (7 clubes) + semifinais + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 45 | 45 | 145 | 10 | Hekari United | Lae FC | a final foi abandonada aos 70' com 3-0 para o Hekari United (violência da torcida); o título ficou com o Hekari |
| 2015 | fase regular (7 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 46 | 46 | 157 | 6 | Lae City | Madang FC |  |
| 2015/16 | conferências regionais (12 clubes) + grupo do título (4 clubes) + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 73 | 73 | 230 | 2 | Lae City | Hekari United | duas zonas de 6; os 2 primeiros de cada zona num grupo de 4 ("National Champions League") e depois a final |
| 2017 | fase regular (6 clubes) + semifinais; 3 pontos por vitória, 1 por empate e 0 por derrota | 30 | 30 | 117 | 0 | Lae City | Madang FC | a final (Lae City Dwellers x Madang FC) foi cancelada: o Lae City Dwellers, 1º da fase regular, foi declarado campeão |
| 2018 | fase regular (7 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 46 | 46 | 179 | 3 | Lae City | Besta PNG United | em 3 de maio os jogos restantes da fase regular viraram W.O. (só 4 clubes tinham pago a taxa) |
| 2019 | conferências regionais (27 clubes) + quartas de final + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 170 | 170 | 658 | 0 | Lae City | Hekari United | quatro conferências regionais e o mata-mata |
| 2019/20 | fase regular (10 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 94 | 94 | 315 | 309 | Lae City | Vitiaz United | parada de 19/03 a 08/08/2020 (covid-19) |
| 2022 | conferências regionais (30 clubes) + playoff das conferências + quartas de final + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 160 | 160 | 649 | 0 | Lae City | Hekari United | cinco conferências regionais (nas duas das ilhas, playoff entre o 1º e o 2º pela vaga) e o mata-mata (de outubro de 2022 a fevereiro de 2023) |
| 2023 | fase regular (8 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 58 | 60 | 170 | 0 | Hekari United | Lae City Dwellers | a liga passa a se chamar Premier Soccer League |
| 2024 | fase regular (8 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 60 | 60 | 183 | 0 | Hekari United | Gulf Komara |  |
| 2025 | fase regular (11 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota | 112 | 113 | 367 | 0 | Gulf Komara | Morobe Wawens |  |
| 2026 | pontos corridos (12 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 130 | 132 | 449 | 0 | Gulf Komara | Hekari United | sem playoff: o 1º da fase regular é o campeão |

## O que não deu para coletar

- 2011/12: só a tabela da fase regular e o mata-mata (a RSSSF não tem as rodadas).
- Jogos sem placar na página (2023, 2025, 2026: ver as divergências).
- Hora, estádio, público, cartões e artilheiros.
