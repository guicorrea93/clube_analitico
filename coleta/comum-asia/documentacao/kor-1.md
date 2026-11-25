# Campeonato Sul-Coreano (`kor-1`) — documentação

Gerado por `python coleta/comum-asia/documentar.py` a partir do pacote `data/coleta/kor-1/pacote/`, do código `coleta/kor-1/` e do relatório `docs/coleta/kor-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 43, de 1983 a 2025; 0 sem jogos.
- **Jogos:** 7163 (7161 com placar); **gols:** 18111; **gols com autor:** 17984 (99%); **cartões:** 24627.
- **Clubes:** 25; **artilheiros:** 43 edições com artilheiro (43 linhas, com empates).
- **Classificação final:** 43 edições; **tabelas publicadas guardadas para conferência:** 0 linhas.
- **No banco:** sim; **último commit do pacote:** e04507f1.
- **Observação da competição:** K League (1983-2012) e K League 1 (2013 em diante)

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições do Campeonato Sul-Coreano (K League, 1ª divisão), uma por título, como na lista de campeões da K League, da
RSSSF (skorchamp.html) e da Wikipédia em inglês (List of South Korean football champions): 1983 a 2025, 43 edições.
2026 fica para quando acabar.

Fases: o boletim do portal não traz rodada nem fase, mas o número do jogo (gameId) segue o calendário (conferido nas
datas), então as fases saem da ordem dos jogos: FASES[ano] = lista de (fase, quantos jogos). De 2013 em diante a fase e
a rodada vêm do site oficial (codeName e roundId da lista de jogos).
- 1984, 1986, 1995, 1996, 2004-2006: dois turnos (전기/후기 리그) e a decisão entre os campeões dos turnos (1984, 1986,
  1995, 1996: competição à parte no portal) ou playoff (2004-2006, com os melhores da tabela anual);
- 1998-2000 e 2007-2011: liga e playoff do título;
- 2012 em diante: liga e depois a divisão em grupo do título e grupo de baixo (스플릿), sem playoff (o campeão é o 1º do
  grupo do título; os pontos seguem da 1ª fase).

Pontos (conferidos na tabela de cada ano da RSSSF, skorhist.html, e nas tabelas das páginas de cada ano):
- 1983 e 1985-1992: 2 por vitória, 1 pelo empate;
- 1984: 3 por vitória, 2 pelo empate com gols e 1 pelo 0-0;
- 1993: empate decidido nos pênaltis; 4 pela vitória, 2 pela vitória nos pênaltis, 1 pela derrota nos pênaltis;
- 1994-1997 e 2001 em diante: 3, 1 e 0;
- 1998 e 1999: empate vai à prorrogação com gol de ouro e aos pênaltis; 3 pela vitória no tempo normal, 2 pela vitória na
  prorrogação, 1 pela vitória nos pênaltis;
- 2000: 3 pela vitória no tempo normal ou na prorrogação, 1 pela vitória nos pênaltis.
```

**Edições:** 43, uma por título, de 1983 a 2025, como na lista de campeões da K League, da RSSSF (`skorchamp.html`) e da Wikipédia em inglês (List of South Korean football champions): K League (Super League em 1983-1986) e, de 2013 em diante, K League 1 (K League Classic até 2017). 2026 entra quando acabar. A liga semiprofissional de antes de 1983 não entra (era outra competição, de clubes de empresa e do Exército; a K League conta a sua história a partir de 1983).

**Fontes:** portal de dados oficial da K League (portal.kleague.com, acesso de convidado): lista de jogos de cada ano (`data/coleta/kor-1/portal/calendario_<ano>.json`; de 2013 em diante a lista vem do site oficial, www.kleague.com, com fase e rodada) e o boletim de cada jogo (data, hora, estádio, público, árbitro, autores dos gols com minuto, pênalti, gol contra, cartões, disputa de pênaltis), no cache `data/cache/kleague-asia/jogos/`; site oficial da K League (www.kleague.com): linha do tempo de cada jogo de 2013 em diante, em coreano e em inglês (`data/cache/kleague-asia/oficial/`: conferência do placar e nome dos jogadores em inglês) e a classificação final oficial de 2013 em diante (`data/coleta/kor-1/oficial/tabela_<ano>.json`); RSSSF (uma página por ano e a `skorhist.html`, com a tabela de cada ano de 1983 a 2009, em `data/coleta/kor-1/rsssf/`: conferência dos placares e das tabelas); Wikipédia em inglês (lista de campeões e lista de artilheiros, "K League Top Scorer Award", em `data/coleta/kor-1/wikipedia/`) e em coreano (tabela e resultados de cada ano, consultada nas divergências); ogol (calendário de 2008 a 2025, para os escudos e a conferência: `data/coleta/kor-1/ogol/` e `data/cache/ogol-kor-1/`).

**Clubes:** 25. Um clube por código do portal oficial (K01, K04...), que é o mesmo nas mudanças de nome e de cidade, como a própria K League conta: Yukong Elephants/Bucheon SK = Jeju United; Daewoo Royals = Busan IPark; Ilhwa Chunma = Seongnam FC; Lucky-Goldstar/LG Cheetahs = FC Seoul; Hyundai Horang-i = Ulsan Hyundai; POSCO = Pohang Steelers. Os times militares têm códigos diferentes e ficam separados: Sangmu (1985), Gwangju Sangmu (2003-2010), Sangju Sangmu (2011-2020) e Gimcheon Sangmu (2022 em diante). O Chonbuk Buffalo (1994) não é o Jeonbuk Hyundai. Nome de exibição: o de hoje, como o ogol escreve. Os nomes de cada fonte estão no `nomes_fonte` do `clubes.csv` (regras em `coleta/kor-1/clubes_kor.py`).

**Regras:** placar oficial, com a prorrogação. O total de gols do boletim do portal não conta o gol contra (em nenhuma época): o placar é a soma dos gols do boletim, conferida com o total (mais os gols contra), com o site oficial (2013 em diante), com a RSSSF e com o ogol; quando não batem, vale o que as outras fontes e as tabelas confirmam, e os autores dos gols do jogo ficam de fora. Pontos: 2 por vitória em 1983 e 1985-1992; em 1984, 3 pela vitória, 2 pelo empate com gols e 1 pelo 0-0; em 1993, empate decidido nos pênaltis (4 pela vitória, 2 pela vitória nos pênaltis, 1 pela derrota nos pênaltis); 3/1/0 em 1994-1997 e de 2001 em diante; em 1998-1999, prorrogação com gol de ouro e pênaltis (3 no tempo normal, 2 na prorrogação, 1 nos pênaltis); em 2000, 3 no tempo normal ou na prorrogação e 1 nos pênaltis. Fases: dois turnos em 1984, 1986, 1995, 1996 e 2004-2006; decisão do título entre os campeões dos turnos (1984, 1986, 1995, 1996) ou playoff (1998-2000, 2004-2011); de 2012 em diante a liga se divide em grupo do título (A) e grupo de baixo (B) nas últimas rodadas, com os pontos acumulados (fase única "Liga", como no Escocês; a observação do jogo diz o grupo). Classificação final: de 2013 em diante, a oficial da K League; antes, a soma dos jogos, com o campeão e o vice da decisão em 1º e 2º, depois os eliminados do playoff pela fase em que caíram e o resto pela tabela (os números de jogos, vitórias, gols e pontos são só da liga, sem playoff nem final, como a tabela da RSSSF). Rebaixado: de 2012 em diante, o clube que não está na edição seguinte (antes de 2012 não havia rebaixamento). Nome dos jogadores: coreanos pela grafia oficial em inglês do site da K League quando há (2013 em diante: "Lee Dong-gook") e, se não, pela romanização revisada do hangul do portal ("Jeong Hae-won"); estrangeiros pelo nome de jogo, tirado do nome em inglês do site oficial (o hangul é o nome de jogo: "호벨손" Roberson); estrangeiros de antes de 2013 sem nome em inglês ficam com o hangul romanizado (aproximação). Cartões de técnico e comissão (sem número de camisa) ficam de fora. Artilheiro: o da lista da Wikipédia em inglês (contagem oficial), conferido com a soma dos gols dos boletins.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 37.
- **Edições com alguma tabela divergente** (6; motivo no relatório, na edição): 1987, 1989, 1991, 1997, 2007, 2016.
- **Edições sem tabela para conferir** (0): nenhuma.
- **Edições com menos jogos que o esperado:** nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1980s | 7 | 560 | 100% | 100% | 80% | 100% | 0% | 100% | 99% | 1.5 |
| 1990s | 10 | 1081 | 100% | 100% | 73% | 100% | 0% | 100% | 97% | 3.1 |
| 2000s | 10 | 1772 | 100% | 100% | 75% | 100% | 0% | 100% | 100% | 3.6 |
| 2010s | 10 | 2448 | 100% | 100% | 95% | 100% | 0% | 99% | 100% | 3.8 |
| 2020s | 6 | 1302 | 100% | 100% | 100% | 100% | 0% | 100% | 100% | 3.5 |

Árbitro: só onde a fonte tem (na J1, na observação de cada jogo). Estatísticas (chutes, faltas, escanteios) não são coletadas.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1983: 5 clubes
- 1984 a 1985: 8 clubes
- 1986: 6 clubes
- 1987 a 1988: 5 clubes
- 1989 a 1993: 6 clubes
- 1994: 7 clubes
- 1995: 8 clubes
- 1996: 9 clubes
- 1997 a 2002: 10 clubes
- 2003: 12 clubes
- 2004 a 2005: 13 clubes
- 2006 a 2008: 14 clubes
- 2009 a 2010: 15 clubes
- 2011 a 2012: 16 clubes
- 2013: 14 clubes
- 2014 a 2025: 12 clubes

**Pontos por vitória:**

- 1983: 2
- 1984: 3
- 1985 a 1992: 2
- 1993: 4
- 1994 a 2025: 3

**Nome oficial:**

- 1983 a 1986: Korean Super League <ano>
- 1987 a 1993: Korean Professional Football League <ano>
- 1994 a 1997: Korean League <ano>
- 1998 a 2012: K League <ano>
- 2013 a 2017: K League Classic <ano>
- 2018 a 2025: K League 1 <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1983: pontos corridos, 5 clubes
- 1984: dois turnos de pontos corridos (8 clubes) e decisão do título entre os campeões dos turnos
- 1985: pontos corridos, 8 clubes
- 1986: dois turnos de pontos corridos (6 clubes) e decisão do título entre os campeões dos turnos
- 1987 a 1988: pontos corridos, 5 clubes
- 1989 a 1993: pontos corridos, 6 clubes
- 1994: pontos corridos, 7 clubes
- 1995: dois turnos de pontos corridos (8 clubes) e decisão do título entre os campeões dos turnos
- 1996: dois turnos de pontos corridos (9 clubes) e decisão do título entre os campeões dos turnos
- 1997: pontos corridos, 10 clubes
- 1998 a 2000: pontos corridos (10 clubes) e playoff do título
- 2001 a 2002: pontos corridos, 10 clubes
- 2003: pontos corridos, 12 clubes
- 2004 a 2005: dois turnos de pontos corridos (13 clubes) e decisão do título em playoff
- 2006: dois turnos de pontos corridos (14 clubes) e decisão do título em playoff
- 2007 a 2008: pontos corridos (14 clubes) e playoff do título
- 2009 a 2010: pontos corridos (15 clubes) e playoff do título
- 2011: pontos corridos (16 clubes) e playoff do título
- 2012: pontos corridos (16 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados
- 2013: pontos corridos (14 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados
- 2014 a 2025: pontos corridos (12 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados

**Fases e grupos de cada edição com mais de uma fase:**

- 1984: 1º turno (liga); 2º turno (liga); Final (mata_mata, ida_volta)
- 1986: 1º turno (liga); 2º turno (liga); Final (mata_mata, ida_volta)
- 1995: 1º turno (liga); 2º turno (liga); Final (mata_mata, ida_volta)
- 1996: 1º turno (liga); 2º turno (liga); Final (mata_mata, ida_volta)
- 1998: Liga (liga); Segunda fase (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1999: Liga (liga); Segunda fase (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2000: Liga (liga); Segunda fase (mata_mata, jogo_unico); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2004: 1º turno (liga); 2º turno (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 2005: 1º turno (liga); 2º turno (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 2006: 1º turno (liga); 2º turno (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 2007: Liga (liga); Primeira fase (mata_mata, jogo_unico); Segunda fase (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 2008: Liga (liga); Primeira fase (mata_mata, jogo_unico); Segunda fase (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 2009: Liga (liga); Primeira fase (mata_mata, jogo_unico); Segunda fase (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 2010: Liga (liga); Primeira fase (mata_mata, jogo_unico); Segunda fase (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 2011: Liga (liga); Primeira fase (mata_mata, jogo_unico); Segunda fase (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- K League: 23 edições
- soma dos jogos: 13 edições
- soma dos jogos da liga; campeão e vice pela decisão, depois os eliminados por fase e a tabela: 7 edições

**Observações das edições:**

- nenhuma

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Jeonbuk Hyundai Motors: 10
- Seongnam FC: 7
- FC Seoul: 6
- Pohang Steelers: 5
- Ulsan Hyundai: 5
- Busan IPark: 4
- Suwon Samsung Bluewings: 4
- Hallelujah FC: 1
- Jeju United: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1983 | Hallelujah FC | Busan IPark |
| 1984 | Busan IPark | Jeju United |
| 1985 | FC Seoul | Pohang Steelers |
| 1986 | Pohang Steelers | FC Seoul |
| 1987 | Busan IPark | Pohang Steelers |
| 1988 | Pohang Steelers | Ulsan Hyundai |
| 1989 | Jeju United | FC Seoul |
| 1990 | FC Seoul | Busan IPark |
| 1991 | Busan IPark | Ulsan Hyundai |
| 1992 | Pohang Steelers | Seongnam FC |
| 1993 | Seongnam FC | FC Seoul |
| 1994 | Seongnam FC | Jeju United |
| 1995 | Seongnam FC | Pohang Steelers |
| 1996 | Ulsan Hyundai | Suwon Samsung Bluewings |
| 1997 | Busan IPark | Jeonnam Dragons |
| 1998 | Suwon Samsung Bluewings | Ulsan Hyundai |
| 1999 | Suwon Samsung Bluewings | Busan IPark |
| 2000 | FC Seoul | Jeju United |
| 2001 | Seongnam FC | FC Seoul |
| 2002 | Seongnam FC | Ulsan Hyundai |
| 2003 | Seongnam FC | Ulsan Hyundai |
| 2004 | Suwon Samsung Bluewings | Pohang Steelers |
| 2005 | Ulsan Hyundai | Incheon United |
| 2006 | Seongnam FC | Suwon Samsung Bluewings |
| 2007 | Pohang Steelers | Seongnam FC |
| 2008 | Suwon Samsung Bluewings | FC Seoul |
| 2009 | Jeonbuk Hyundai Motors | Seongnam FC |
| 2010 | FC Seoul | Jeju United |
| 2011 | Jeonbuk Hyundai Motors | Ulsan Hyundai |
| 2012 | FC Seoul | Jeonbuk Hyundai Motors |
| 2013 | Pohang Steelers | Ulsan Hyundai |
| 2014 | Jeonbuk Hyundai Motors | Suwon Samsung Bluewings |
| 2015 | Jeonbuk Hyundai Motors | Suwon Samsung Bluewings |
| 2016 | FC Seoul | Jeonbuk Hyundai Motors |
| 2017 | Jeonbuk Hyundai Motors | Jeju United |
| 2018 | Jeonbuk Hyundai Motors | Gyeongnam FC |
| 2019 | Jeonbuk Hyundai Motors | Ulsan Hyundai |
| 2020 | Jeonbuk Hyundai Motors | Ulsan Hyundai |
| 2021 | Jeonbuk Hyundai Motors | Ulsan Hyundai |
| 2022 | Ulsan Hyundai | Jeonbuk Hyundai Motors |
| 2023 | Ulsan Hyundai | Pohang Steelers |
| 2024 | Ulsan Hyundai | Gangwon FC |
| 2025 | Jeonbuk Hyundai Motors | Daejeon Hana Citizen |

**Rebaixados marcados na classificação:** 24 em 14 edições (só onde a tabela publicada marca a queda); quem mais caiu: Gwangju FC (3), Sangju Sangmu (3), Daegu FC (2), Daejeon Hana Citizen (2), Gyeongnam FC (2).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 2016: Jeonbuk Hyundai Motors -9

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/kor-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Jogos dados por W.O. (sem placar; o vencedor na observação) (`WO`, 16)

- **1987_1_79:** [wo, vencedor = m] o Hyundai Horang-i não jogou ("현대 호랑이 기권패"; a K League dá 2-0, sem contar os gols na tabela; Wikipédia em coreano, 1987년 K리그의 경기 결과); no portal, 0-0 sem lances
- **1987_1_80:** [wo, vencedor = m] o Hyundai Horang-i não jogou ("현대 호랑이 기권패"; a K League dá 2-0, sem contar os gols na tabela; Wikipédia em coreano, 1987년 K리그의 경기 결과); no portal, 0-0 sem lances
- **2012_1_247:** [wo, placar oficial 2-0, vencedor = m] o Sangju Sangmu se recusou a jogar o resto de 2012 depois de ser rebaixado à força (o time do Exército não cumpria as regras de clube da K League); a K League deu 2-0 ao adversário e conta os gols (tabela oficial do Sangju: 7-6-31, 29-74); no portal, 0-0 sem lances, público nem árbitro
- **2012_1_256:** [wo, placar oficial 0-2, vencedor = v] o Sangju Sangmu se recusou a jogar o resto de 2012 depois de ser rebaixado à força (o time do Exército não cumpria as regras de clube da K League); a K League deu 2-0 ao adversário e conta os gols (tabela oficial do Sangju: 7-6-31, 29-74); no portal, 0-0 sem lances, público nem árbitro
- **2012_1_262:** [wo, placar oficial 0-2, vencedor = v] o Sangju Sangmu se recusou a jogar o resto de 2012 depois de ser rebaixado à força (o time do Exército não cumpria as regras de clube da K League); a K League deu 2-0 ao adversário e conta os gols (tabela oficial do Sangju: 7-6-31, 29-74); no portal, 0-0 sem lances, público nem árbitro
- **2012_1_270:** [wo, placar oficial 2-0, vencedor = m] o Sangju Sangmu se recusou a jogar o resto de 2012 depois de ser rebaixado à força (o time do Exército não cumpria as regras de clube da K League); a K League deu 2-0 ao adversário e conta os gols (tabela oficial do Sangju: 7-6-31, 29-74); no portal, 0-0 sem lances, público nem árbitro
- **2012_1_278:** [wo, placar oficial 0-2, vencedor = v] o Sangju Sangmu se recusou a jogar o resto de 2012 depois de ser rebaixado à força (o time do Exército não cumpria as regras de clube da K League); a K League deu 2-0 ao adversário e conta os gols (tabela oficial do Sangju: 7-6-31, 29-74); no portal, 0-0 sem lances, público nem árbitro
- **2012_1_286:** [wo, placar oficial 2-0, vencedor = m] o Sangju Sangmu se recusou a jogar o resto de 2012 depois de ser rebaixado à força (o time do Exército não cumpria as regras de clube da K League); a K League deu 2-0 ao adversário e conta os gols (tabela oficial do Sangju: 7-6-31, 29-74); no portal, 0-0 sem lances, público nem árbitro
- **2012_1_294:** [wo, placar oficial 0-2, vencedor = v] o Sangju Sangmu se recusou a jogar o resto de 2012 depois de ser rebaixado à força (o time do Exército não cumpria as regras de clube da K League); a K League deu 2-0 ao adversário e conta os gols (tabela oficial do Sangju: 7-6-31, 29-74); no portal, 0-0 sem lances, público nem árbitro
- **2012_1_302:** [wo, placar oficial 2-0, vencedor = m] o Sangju Sangmu se recusou a jogar o resto de 2012 depois de ser rebaixado à força (o time do Exército não cumpria as regras de clube da K League); a K League deu 2-0 ao adversário e conta os gols (tabela oficial do Sangju: 7-6-31, 29-74); no portal, 0-0 sem lances, público nem árbitro
- **2012_1_312:** [wo, placar oficial 0-2, vencedor = v] o Sangju Sangmu se recusou a jogar o resto de 2012 depois de ser rebaixado à força (o time do Exército não cumpria as regras de clube da K League); a K League deu 2-0 ao adversário e conta os gols (tabela oficial do Sangju: 7-6-31, 29-74); no portal, 0-0 sem lances, público nem árbitro
- **2012_1_320:** [wo, placar oficial 2-0, vencedor = m] o Sangju Sangmu se recusou a jogar o resto de 2012 depois de ser rebaixado à força (o time do Exército não cumpria as regras de clube da K League); a K League deu 2-0 ao adversário e conta os gols (tabela oficial do Sangju: 7-6-31, 29-74); no portal, 0-0 sem lances, público nem árbitro
- **2012_1_326:** [wo, placar oficial 0-2, vencedor = v] o Sangju Sangmu se recusou a jogar o resto de 2012 depois de ser rebaixado à força (o time do Exército não cumpria as regras de clube da K League); a K League deu 2-0 ao adversário e conta os gols (tabela oficial do Sangju: 7-6-31, 29-74); no portal, 0-0 sem lances, público nem árbitro
- **2012_1_333:** [wo, placar oficial 2-0, vencedor = m] o Sangju Sangmu se recusou a jogar o resto de 2012 depois de ser rebaixado à força (o time do Exército não cumpria as regras de clube da K League); a K League deu 2-0 ao adversário e conta os gols (tabela oficial do Sangju: 7-6-31, 29-74); no portal, 0-0 sem lances, público nem árbitro
- **2012_1_344:** [wo, placar oficial 2-0, vencedor = m] o Sangju Sangmu se recusou a jogar o resto de 2012 depois de ser rebaixado à força (o time do Exército não cumpria as regras de clube da K League); a K League deu 2-0 ao adversário e conta os gols (tabela oficial do Sangju: 7-6-31, 29-74); no portal, 0-0 sem lances, público nem árbitro
- **2012_1_351:** [wo, placar oficial 0-2, vencedor = v] o Sangju Sangmu se recusou a jogar o resto de 2012 depois de ser rebaixado à força (o time do Exército não cumpria as regras de clube da K League); a K League deu 2-0 ao adversário e conta os gols (tabela oficial do Sangju: 7-6-31, 29-74); no portal, 0-0 sem lances, público nem árbitro

### Gols que faltam no boletim da fonte, acrescentados com a prova (`GOL_FALTANDO`, 1)

- **1990_1_76:** o 3º gol do Ulsan Hyundai (Byeon Byeong-ju, 90+1) não está no boletim do portal (que dá 2-2); 2-3 na RSSSF e na Wikipédia em coreano (1990년 K리그의 경기 결과), e as duas tabelas do ano fecham com 2-3

### Linhas da tabela da RSSSF que não fecham com os jogos (e a prova) (`TABELA_RSSSF`, 6)

- **1987:** A Wikipédia em coreano (1987년 K리그) dá os mesmos números daqui para o FC Seoul (Lucky-Goldstar): 7-7-18, 26-55, 21 pontos; a RSSSF tem 56 gols sofridos e um placar diferente (Pohang 2-1 Lucky-Goldstar em 31/10; o portal e a Wikipédia em coreano dão 2-3).
- **1989:** A Wikipédia em coreano (1989년 K리그) dá 47 pontos ao FC Seoul (Lucky-Goldstar), como aqui (15 vitórias e 17 empates); os 42 da RSSSF são erro de conta.
- **1991:** A Wikipédia em coreano (1991년 K리그) dá ao Jeju United (Yukong) 10-17-13, 38-40, 37 pontos, como aqui.
- **1997:** Sem explicação: a RSSSF dá ao Jeju United (Puchon SK) 18-35 e aqui são 19-36 (mesmos pontos); a RSSSF não tem os jogos de 1997 e a Wikipédia em coreano não tem a tabela; os outros 9 clubes fecham.
- **2007:** Erro de digitação da skorhist.html: 27-53 para o Jeju United; a página de 2007 da RSSSF dá 27-35, como aqui e como a tabela oficial da K League.
- **2016:** O Jeonbuk Hyundai perdeu 9 pontos (suborno de árbitros por um olheiro do clube, em 2013): 69 nos jogos, 60 na RSSSF e na tabela oficial (ajuste_pontos -9).

### Empate nos pênaltis decidido no sorteio (`SORTEIO`, 1)

- **1998_1_29:** 1-1 na prorrogação e 5-5 nos pênaltis; o estádio de Cheonan não tinha refletores para seguir com as cobranças e o jogo foi decidido no sorteio, que o Chunan Ilhwa Chunma (Seongnam FC) ganhou (Wikipédia em coreano, 1998년 K리그 e 1998년 K리그의 경기 결과; RSSSF: "5TK5", e a tabela dá a vitória ao Chunan)

### Saídas da liga que não foram rebaixamento comum (`OBS_CLASSIFICACAO`, 8)

- **1984 · Kookmin Bank:** saiu da liga depois de 1984 (time amador de banco)
- **1985 · Hallelujah FC:** saiu da liga depois de 1985 (virou amador)
- **1985 · Sangmu:** saiu da liga depois de 1985 (time do Exército)
- **1986 · Hanil Bank:** saiu da liga depois de 1986 (time amador de banco)
- **1994 · Chonbuk Buffalo:** fechou no fim de 1994
- **2010 · Gwangju Sangmu:** o time do Exército mudou para Sangju em 2011 (Sangju Sangmu, outro código na K League)
- **2012 · Sangju Sangmu:** rebaixado por decisão da liga (o time do Exército não cumpria as regras de clube); abandonou o resto da temporada (14 derrotas por W.O.)
- **2020 · Sangju Sangmu:** rebaixado por decisão da liga: o time do Exército mudou para Gimcheon e recomeçou na K League 2 (Gimcheon Sangmu, outro código na K League)

### Jogos decididos fora de campo (placar oficial; o de campo no gols_texto) (`AWD`, 2)

- **1996_1_111:** [decidido fora de campo, placar oficial 3-0, campo = 1-1, parado aos 68'] o Suwon Samsung escalou um estrangeiro a mais que o permitido; o jogo parou aos 68' com 1-1 e a K League deu 3-0 ao Pohang ("수원 삼성 몰수패"; RSSSF e Wikipédia em coreano, 1996년 K리그의 경기 결과); o portal registra 1-0, só com o gol do Hwang Seon-hong
- **2021_1_176:** [decidido fora de campo, placar oficial 0-3, campo = 1-1] o Gwangju FC fez mais substituições que o permitido; a K League deu 3-0 ao Jeju United ("교체 횟수 초과", News1, 24/09/2021; Wikipédia em inglês e em coreano; o site oficial dá 0-3)

### Identidade dos clubes

Regras em `coleta/kor-1/clubes_kor.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes da K League: um clube por código do portal oficial (K01, K04...), que é o mesmo ao longo das
mudanças de nome e de cidade, como a própria K League conta a história. Nome de exibição: o pelo qual o clube é conhecido
no Brasil (o do ogol, por extenso).

- K04: Yukong Elephants (1983) -> Puchon Yukong -> Bucheon SK -> Jeju United (2006; Jeju SK desde 2025);
- K06: Daewoo Royals -> Pusan Daewoo -> Pusan/Busan Icons -> Busan IPark;
- K08: Ilhwa Chunma (Seul) -> Chunan Ilhwa -> Seongnam Ilhwa Chunma -> Seongnam FC;
- K09: Lucky-Goldstar Hwangso -> LG Cheetahs -> Anyang LG Cheetahs -> FC Seoul (2004);
- K01: Hyundai Horang-i -> Ulsan Hyundai -> Ulsan HD; K03: POSCO Dolphins/Atoms -> Pohang Steelers;
- os clubes militares têm códigos diferentes no portal e ficam separados: Gwangju Sangmu (K14), Sangju Sangmu (K23) e
  Gimcheon Sangmu (K35); o Sangmu de 1985 (K24, time do Exército, sem sede fixa: cidade em branco) também;
- K16: Chonbuk Buffalo (1994, fechou no fim do ano; não é o Jeonbuk Hyundai, K05).

CLUBES: código -> (nome de exibição, cidade, província). Código que falta aqui para a importação (erro de propósito).
```

## 8. O que não deu para coletar

- **Fora do pacote:** a copa da liga (아디다스컵, 리그컵 etc.; o patrocínio pôs "copa" no nome da própria liga em 1996-1999, mas essas são a liga), a repescagem contra a K League 2 (승강 플레이오프, 2013 em diante: entra com a 2ª divisão), a Copa da Coreia (FA Cup) e a Supercopa.
- **Edições sem jogos:** nenhuma.
- **Edições com jogos incompletos:** nenhuma: todos os jogos da 1ª divisão estão no portal. 23 jogos ficaram sem os autores dos gols (o boletim não fecha com o placar; lista em cada edição).
- **Edições sem jogos** (0): nenhuma.
- **Décadas com menos da metade dos gols com autor:** nenhuma.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): nenhuma.
- Estatísticas de jogo (chutes, faltas, escanteios): não coletadas.

## 9. Pendências e próximos passos

- 23 jogos sem os autores dos gols (o boletim do portal não fecha com o placar; os autores que ele tem estão no gols_texto). Fonte que resolveria: as páginas 'NNNN년 K리그의 경기 결과' da Wikipédia em coreano (têm os autores de cada jogo; serviram para 1987 e 1990).
- 197 estrangeiros de antes de 2013 com o nome romanizado do hangul (aproximação; a maioria só com cartões): sem nome em inglês no site oficial nem autor na RSSSF. Lista no relatório. Fonte que resolveria: a página de jogador do site da K League (não achei a chamada de dados) ou a Wikipédia em coreano.
- Coreanos: grafia oficial em inglês do site da K League para quem jogou de 2013 em diante, romanização revisada para os outros (Park Yun-gi, e não Park Yoon-ki, como a Wikipédia escreve). Uns poucos cortes de sílaba esquisitos vêm da grafia do próprio site ("Jeewong").
- 1997: a linha do Jeju United (Puchon SK) da RSSSF (18-35) não fecha com os jogos (19-36); a RSSSF não tem os jogos de 1997 e a Wikipédia em coreano não tem a tabela.
- Artilheiro: a soma dos boletins fica 1 gol abaixo da lista oficial em 1984, 1993, 1997, 1999, 2005, 2006 e 2021 (gols em jogos sem autores; em 2005 a K League parece contar o playoff); em 2013, 2022 e 2023 a soma dá empate e a lista oficial desempata pelo número de jogos. Vale a lista oficial (Wikipédia).
- 958 jogos de antes de 2013 sem rodada (o portal não dá; a rodada sai da ordem dos jogos de cada clube quando os dois batem); classificacao_rodada só de 2013 em diante.
- Estádios: nome traduzido por regra do hangul do portal (cidade + tipo: 월드컵 World Cup Stadium, 종합 Sports Complex...); cidade dos jogos em branco. O Sangmu de 1985 fica sem cidade (time do Exército, sem sede).
- 2026: entra quando acabar (em 24/11 faltavam 12 jogos).

## 10. Arquivos e comandos

Código em `coleta/kor-1/`:

| Arquivo | O que faz |
|---|---|
| `baixar_oficial.py` | Baixa do site oficial da K League (www.kleague.com) a linha do tempo de cada jogo da K League 1 de 2013 a 2025 |
| `baixar_ogol.py` | Baixa o calendário de cada edição da K League (2008-2025; o ogol não tem os jogos de 1983 a 2007) no ogol para data/coleta/kor-1/ogol/<ano>.json. |
| `baixar_portal.py` | Baixa do portal de dados oficial da K League (portal.kleague.com, acesso de convidado) os jogos da 1ª divisão sul-coreana |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão sul-coreana para data/coleta/kor-1/rsssf/: a lista de campeões (skorchamp.html), |
| `baixar_tabelas.py` | Baixa do site oficial da K League (www.kleague.com, /record/teamRank.do) a classificação final de cada ano |
| `baixar_wikipedia.py` | Baixa da Wikipédia em inglês a lista de campeões sul-coreanos ("List of South Korean football champions": campeão e |
| `campeoes_wiki.py` | Campeão e vice de cada ano da K League pela Wikipédia em inglês (List of South Korean football champions, |
| `clubes_kor.py` | Identidade dos clubes da K League: um clube por código do portal oficial (K01, K04...), que é o mesmo ao longo das |
| `competicoes.py` | Quais competições do portal da K League são a 1ª divisão de cada ano. |
| `edicoes.py` | Edições do Campeonato Sul-Coreano (K League, 1ª divisão), uma por título, como na lista de campeões da K League, da |
| `explicacoes.py` | Correções e casos especiais da K League, com a prova de cada um (chave: "<ano>_<meetSeq>_<gameId>" do portal). |
| `importar.py` | Monta o pacote do Campeonato Sul-Coreano (kor-1) em data/coleta/kor-1/pacote/ e o relatório docs/coleta/kor-1.md. |
| `ler_oficial.py` | Lê a linha do tempo dos jogos de 2013 em diante baixada do site oficial da K League (baixar_oficial.py), em coreano e |
| `ler_portal.py` | Lê o boletim de um jogo da K League baixado do portal oficial (baixar_portal.py). |
| `ler_rsssf.py` | Lê os jogos das páginas da RSSSF da Coreia do Sul (data/coleta/kor-1/rsssf/skorYY.html e skorYYYY.html), para a |
| `nomes_kor.py` | Nome de exibição dos jogadores da K League. |
| `relatorio.py` | Escreve o relatório da coleta (docs/coleta/kor-1.md), chamado pelo importar.py. |

- Fontes baixadas: `data/coleta/kor-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-asia/`, do ogol em `data/cache/ogol-kor-1/`.
- Pacote: `data/coleta/kor-1/pacote/`; relatório: `docs/coleta/kor-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/kor-1/baixar_oficial.py
python coleta/kor-1/baixar_ogol.py
python coleta/kor-1/baixar_portal.py
python coleta/kor-1/baixar_rsssf.py
python coleta/kor-1/baixar_tabelas.py
python coleta/kor-1/baixar_wikipedia.py
python coleta/kor-1/importar.py
python coleta/kor-1/conferir.py [-v temporada]   # divergências
python coleta/comum-asia/testar_carga.py kor-1 <scratchpad>
python coleta/comum-asia/documentar.py
```

