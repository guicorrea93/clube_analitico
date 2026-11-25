# Campeonato Japonês (`jpn-1`) — documentação

Gerado por `python coleta/comum-asia/documentar.py` a partir do pacote `data/coleta/jpn-1/pacote/`, do código `coleta/jpn-1/` e do relatório `docs/coleta/jpn-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 60, de 1965 a 2025; 0 sem jogos.
- **Jogos:** 12190 (12190 com placar); **gols:** 34082; **gols com autor:** 27554 (81%); **cartões:** 31272.
- **Clubes:** 40; **artilheiros:** 60 edições com artilheiro (69 linhas, com empates).
- **Classificação final:** 60 edições; **tabelas publicadas guardadas para conferência:** 1038 linhas.
- **No banco:** sim; **último commit do pacote:** 71d50064.
- **Observação da competição:** Japan Soccer League (JSL, amadora, 1965 a 1991/92) e J.League/J1 (1993 em diante); 1992 sem liga

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições do Campeonato Japonês (1ª divisão), uma por título, como na lista de campeões da RSSSF (japchamp.html) e da
Wikipédia em inglês (List of Japanese football champions): 60 edições.

- 1965 a 1984: Japan Soccer League (JSL; a partir de 1972, JSL Division 1), amadora, em ano fechado.
- 1985/86 a 1991/92: JSL Division 1 no calendário europeu (outono a primavera).
- 1992: sem liga. A JSL acabou em 1991/92; a J.League começou em 1993 (em 1992 só houve a Copa da J.League).
- 1993 a 2025: J.League (J1). Nos anos de dois turnos (1993-1995, 1997-2004, 2015 e 2016) o campeão é o vencedor
  da final entre os campeões dos turnos ("Championship"); em 2002 e 2003 o mesmo clube ganhou os dois turnos e não houve
  final; em 2015 e 2016 a final teve semifinal. Os turnos entram como fases; a repescagem contra a J2 (1998, 2004-2008,
  2018, 2019, 2022) fica de fora, como no Alemão (entra com a 2ª divisão).

Pontos por vitória (a classificação vem sempre da tabela publicada):
- JSL: 2 até 1976, 4 de 1977 a 1979 (empate decidido nos pênaltis: 2 para quem ganha, 1 para quem perde), 2 de 1980 a
  1987/88 e 3 de 1988/89 a 1991/92 (conferido na tabela de cada ano);
- J1: 1993 e 1994 sem pontos (sem empate: prorrogação com morte súbita e pênaltis; a tabela ordena por vitórias);
  1995 e 1996: 3 por vitória (no tempo normal, na prorrogação ou nos pênaltis), 1 pela derrota nos pênaltis; 1997 e 1998: 3 no tempo normal, 2 na
  prorrogação, 1 nos pênaltis; 1999 a 2002: 3 no tempo normal, 2 na prorrogação, 1 o empate (sem pênaltis);
  2003 em diante: 3, 1 e 0, sem prorrogação.
```

**Edições:** 60, uma por título, de 1965 a 2025, como na lista de campeões da RSSSF (`japchamp.html`, 60 títulos) e da Wikipédia em inglês (List of Japanese football champions). Japan Soccer League (JSL, amadora: 1965 a 1984 em ano fechado, 1985/86 a 1991/92 no calendário europeu) e J.League (J1, profissional, de 1993 em diante). Em 1992 não houve liga (só a Copa da J.League). Nos anos de dois turnos (1993-1995, 1997-2004, 2015 e 2016), o campeão é o vencedor da final entre os campeões dos turnos (o campeão oficial); os turnos entram como fases.

**Fontes:** RSSSF (uma página por temporada da JSL, `jap65.html` a `jap92.html`, em `data/coleta/jpn-1/rsssf/`: tabela final, tabela de confrontos com todos os jogos, rodadas com data em 1988/89 e artilheiros); J.League Data Site (data.j-league.or.jp, o site oficial de dados da J.League, em inglês: lista de jogos de cada ano em `data/coleta/jpn-1/jleague/lista_<ano>.json`, página de cada jogo, com autores dos gols e minuto, cartões, árbitro, estádio e público, no cache `data/cache/jleague-asia/`, e as tabelas oficiais de cada turno e anual em `tabelas_<ano>.json`); Wikipédia em inglês (lista de campeões: campeão, vice e 3º, segunda fonte); ESPN (liga `jpn.1`, 2006 em diante, `data/coleta/jpn-1/espn/`: conferência dos placares); ogol (calendário da J1, 1993-2025, para os escudos: `data/cache/ogol-jpn-1/`).

**Clubes:** 40. Nome pelo qual o clube é conhecido hoje (o do ogol, quase sempre). Os clubes de empresa da JSL que viraram clubes da J.League são o mesmo clube, como a J.League, os clubes e a lista de campeões da RSSSF contam: Toyo Industries/Mazda = Sanfrecce Hiroshima, Mitsubishi = Urawa Reds, Furukawa = JEF United Chiba, Hitachi = Kashiwa Reysol, Yanmar = Cerezo Osaka, Towa Estate/Fujita = Shonan Bellmare, Toyota = Nagoya Grampus, Fujitsu = Kawasaki Frontale, Nissan = Yokohama F. Marinos, Yomiuri = Tokyo Verdy, Sumitomo = Kashima Antlers, All Nippon Airways = Yokohama Flügels, Matsushita = Gamba Osaka, Yamaha = Júbilo Iwata, Toshiba = Consadole Sapporo. O Yokohama Flügels (fechado em 1998, fundido ao Marinos) é um clube separado do Yokohama F. Marinos. Os nomes de cada fonte estão no `nomes_fonte` do `clubes.csv` (regras em `coleta/jpn-1/clubes_jpn.py`).

**Regras:** placar oficial, com a prorrogação. De 1993 a 1998 não havia empate: prorrogação com gol de ouro e, empatado, pênaltis (`penaltis_mandante`/`penaltis_visitante`); de 1999 a 2002, prorrogação com gol de ouro e empate se ela terminasse sem gol. Pontos por vitória: JSL 2 (1965-1976 e 1980-1987/88), 4 (1977-1979, com 2 para a vitória nos pênaltis e 1 para a derrota nos pênaltis) e 3 (1988/89 em diante); J1 sem pontos em 1993-1994 (ordem por vitórias), 3 por vitória (também nos pênaltis) e 1 pela derrota nos pênaltis em 1995-1996, 3/2/1 (tempo normal, prorrogação, pênaltis) em 1997-1998, 3/2/1 (tempo normal, prorrogação, empate) em 1999-2002, 3/1/0 de 2003 em diante. A classificação final é a tabela oficial (J1: J.League; JSL: RSSSF); nos anos de turnos, a tabela anual oficial (1999-2004, 2015, 2016) ou a soma das tabelas dos turnos (1993-1998), com o campeão e o vice da final em 1º e 2º. Rebaixado: o clube que não está na edição seguinte (fora os que fecharam: Eidai Industries em 1976, Yokohama Flügels em 1998) e, na J1, o marcado "J2" na tabela oficial. Em 1991/92 ninguém caiu: a JSL acabou e os clubes foram para a J.League ou para a nova JFL. Gol contra: a J.League escreve "Own-Goal" sem o nome do jogador (`jogador` vazio, `tipo` `contra`). A J.League não marca os gols de pênalti (ficam como `normal`). Artilheiro: o da lista de campeões da Wikipédia em inglês (a contagem oficial), conferido com a RSSSF (JSL) e com a soma dos gols da J.League (J1).

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 57.
- **Edições com alguma tabela divergente** (3; motivo no relatório, na edição): 1966, 1971, 1973.
- **Edições sem tabela para conferir** (0): nenhuma.
- **Edições com menos jogos que o esperado:** nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1960s | 5 | 280 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 10 | 798 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 10 | 1110 | 12% | 0% | 12% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 9 | 2142 | 88% | 88% | 87% | 88% | 0% | 88% | 91% | 2.9 |
| 2000s | 10 | 2736 | 100% | 100% | 100% | 100% | 0% | 100% | 100% | 4.1 |
| 2010s | 10 | 3066 | 100% | 100% | 100% | 100% | 0% | 100% | 100% | 2.9 |
| 2020s | 6 | 2058 | 100% | 100% | 100% | 100% | 0% | 100% | 100% | 2.4 |

Árbitro: só onde a fonte tem (na J1, na observação de cada jogo). Estatísticas (chutes, faltas, escanteios) não são coletadas.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1965 a 1972: 8 clubes
- 1973 a 1984: 10 clubes
- 1985/86 a 1991/92: 12 clubes
- 1993: 10 clubes
- 1994: 12 clubes
- 1995: 14 clubes
- 1996: 16 clubes
- 1997: 17 clubes
- 1998: 18 clubes
- 1999 a 2004: 16 clubes
- 2005 a 2020: 18 clubes
- 2021: 20 clubes
- 2022 a 2023: 18 clubes
- 2024 a 2025: 20 clubes

**Pontos por vitória:**

- 1965 a 1976: 2
- 1977 a 1979: 4
- 1980 a 1987/88: 2
- 1988/89 a 1991/92: 3
- 1993 a 1994: 
- 1995 a 2025: 3

**Nome oficial:**

- 1965 a 1971: Japan Soccer League <ano>
- 1972 a 1991/92: Japan Soccer League Division 1 <ano>
- 1993 a 1998: J.League <ano>
- 1999 a 2014: J.League Division 1 <ano>
- 2015 a 2025: J1 League <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1965 a 1972: pontos corridos, 8 clubes, turno e returno
- 1973 a 1984: pontos corridos, 10 clubes, turno e returno
- 1985/86 a 1991/92: pontos corridos, 12 clubes, turno e returno
- 1993: dois turnos de pontos corridos (10 clubes, turno único em cada um); final entre os campeões dos turnos (ida e volta)
- 1994: dois turnos de pontos corridos (12 clubes, turno único em cada um); final entre os campeões dos turnos (ida e volta)
- 1995: dois turnos de pontos corridos (14 clubes, turno único em cada um); final entre os campeões dos turnos (ida e volta)
- 1996: pontos corridos, 16 clubes, turno e returno
- 1997: dois turnos de pontos corridos (17 clubes, turno único em cada um); final entre os campeões dos turnos (ida e volta)
- 1998: dois turnos de pontos corridos (18 clubes, turno único em cada um); final entre os campeões dos turnos (ida e volta)
- 1999 a 2001: dois turnos de pontos corridos (16 clubes, turno único em cada um); final entre os campeões dos turnos (ida e volta)
- 2002 a 2003: dois turnos de pontos corridos (16 clubes, turno único em cada um); sem final: o mesmo clube ganhou os dois turnos
- 2004: dois turnos de pontos corridos (16 clubes, turno único em cada um); final entre os campeões dos turnos (ida e volta)
- 2005 a 2014: pontos corridos, 18 clubes, turno e returno
- 2015 a 2016: dois turnos de pontos corridos (18 clubes, turno único em cada um); semifinal (jogo único) e final (ida e volta) entre os campeões dos turnos e o melhor da tabela anual
- 2017 a 2020: pontos corridos, 18 clubes, turno e returno
- 2021: pontos corridos, 20 clubes, turno e returno
- 2022 a 2023: pontos corridos, 18 clubes, turno e returno
- 2024 a 2025: pontos corridos, 20 clubes, turno e returno

**Fases e grupos de cada edição com mais de uma fase:**

- 1993: 1º turno (Suntory Series) (liga); 2º turno (NICOS Series) (liga); Final (mata_mata, ida_volta)
- 1994: 1º turno (Suntory Series) (liga); 2º turno (NICOS Series) (liga); Final (mata_mata, ida_volta)
- 1995: 1º turno (Suntory Series) (liga); 2º turno (NICOS Series) (liga); Final (mata_mata, ida_volta)
- 1997: 1º turno (liga); 2º turno (liga); Final (mata_mata, ida_volta)
- 1998: 1º turno (liga); 2º turno (liga); Final (mata_mata, ida_volta)
- 1999: 1º turno (liga); 2º turno (liga); Final (mata_mata, ida_volta)
- 2000: 1º turno (liga); 2º turno (liga); Final (mata_mata, ida_volta)
- 2001: 1º turno (liga); 2º turno (liga); Final (mata_mata, ida_volta)
- 2002: 1º turno (liga); 2º turno (liga)
- 2003: 1º turno (liga); 2º turno (liga)
- 2004: 1º turno (liga); 2º turno (liga); Final (mata_mata, ida_volta)
- 2015: 1º turno (liga); 2º turno (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 2016: 1º turno (liga); 2º turno (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- J.League Data Site: 28 edições
- RSSSF: 27 edições
- soma das tabelas oficiais dos dois turnos: 5 edições

**Observações das edições:**

- 1966: a tabela de confrontos da RSSSF dá 4 gols a menos ao Yawata (Nippon Steel Yawata) contra o Hitachi (Kashiwa Reysol) do que a tabela final (33-16 e 24-28, iguais na Wikipédia em japonês, que cita o livro oficial da JSL): um dos dois jogos entre eles (Yawata 2-1 Hitachi ou Hitachi 1-2 Yawata) deveria ter 4 gols a mais do Yawata, sem mudar o vencedor. Nenhuma fonte pública tem o placar; os jogos ficam como a RSSSF escreve e a classificação é a tabela final
- 1971: a tabela de confrontos da RSSSF tem 2 gols a menos que a tabela final: um do Furukawa (JEF United Chiba) e um do Nippon Kokan (NKK), sofridos pelo Yanmar (Cerezo Osaka) e pelo Hitachi (Kashiwa Reysol), um cada. Há dois jeitos de encaixar (Furukawa x Yanmar e Nippon Kokan x Hitachi, ou Furukawa x Hitachi e Nippon Kokan x Yanmar), sem mudar vencedor; nenhuma fonte pública tem o placar. Os jogos ficam como a RSSSF escreve e a classificação é a tabela final
- 1973: a tabela de confrontos da RSSSF tem 1 gol a menos para o Yanmar (Cerezo Osaka) e 1 a menos para o Furukawa (JEF United Chiba) do que a tabela final: um dos jogos entre os dois (Furukawa 0-0 Yanmar ou Yanmar 1-2 Furukawa) deveria ter um gol a mais de cada lado, sem mudar o resultado. Nenhuma fonte pública tem o placar; os jogos ficam como a RSSSF escreve e a classificação é a tabela final
- 1977: empates decididos nos pênaltis (4 pontos a vitória, 2 a vitória nos pênaltis, 1 a derrota nos pênaltis); a tabela de confrontos não diz quem ganhou cada disputa: os jogos ficam como empate
- 1978: empates decididos nos pênaltis (4 pontos a vitória, 2 a vitória nos pênaltis, 1 a derrota nos pênaltis); a tabela de confrontos não diz quem ganhou cada disputa: os jogos ficam como empate
- 1979: empates decididos nos pênaltis (4 pontos a vitória, 2 a vitória nos pênaltis, 1 a derrota nos pênaltis); a tabela de confrontos não diz quem ganhou cada disputa: os jogos ficam como empate
- 1988/89: rodada e data dos 132 jogos pela lista de rodadas da página; mando invertido na lista de rodadas, vale o da tabela de confrontos (que fecha com a tabela final): Yomiuri Nippon 2-0 Honda (rodada 9): na tabela de confrontos o mandante é o Honda FC
- 2004: fora do pacote: 2 jogo(s) da repescagem J1/J2 (entram com a 2ª divisão)
- 2005: fora do pacote: 2 jogo(s) da repescagem J1/J2 (entram com a 2ª divisão)
- 2006: fora do pacote: 2 jogo(s) da repescagem J1/J2 (entram com a 2ª divisão)
- 2007: fora do pacote: 2 jogo(s) da repescagem J1/J2 (entram com a 2ª divisão)
- 2008: fora do pacote: 2 jogo(s) da repescagem J1/J2 (entram com a 2ª divisão)
- 2018: fora do pacote: 3 jogo(s) da repescagem J1/J2 (entram com a 2ª divisão)
- 2019: fora do pacote: 4 jogo(s) da repescagem J1/J2 (entram com a 2ª divisão)
- 2022: fora do pacote: 4 jogo(s) da repescagem J1/J2 (entram com a 2ª divisão)

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Kashima Antlers: 9
- Sanfrecce Hiroshima: 8
- Tokyo Verdy: 7
- Yokohama F. Marinos: 7
- Urawa Reds: 5
- Cerezo Osaka: 4
- Júbilo Iwata: 4
- Kawasaki Frontale: 4
- Shonan Bellmare: 3
- Kashiwa Reysol: 2
- JEF United Chiba: 2
- Gamba Osaka: 2
- Vissel Kobe: 2
- Nagoya Grampus: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1965 | Sanfrecce Hiroshima | Nippon Steel Yawata |
| 1966 | Sanfrecce Hiroshima | Nippon Steel Yawata |
| 1967 | Sanfrecce Hiroshima | JEF United Chiba |
| 1968 | Sanfrecce Hiroshima | Cerezo Osaka |
| 1969 | Urawa Reds | Sanfrecce Hiroshima |
| 1970 | Sanfrecce Hiroshima | Urawa Reds |
| 1971 | Cerezo Osaka | Urawa Reds |
| 1972 | Kashiwa Reysol | Cerezo Osaka |
| 1973 | Urawa Reds | Kashiwa Reysol |
| 1974 | Cerezo Osaka | Urawa Reds |
| 1975 | Cerezo Osaka | Urawa Reds |
| 1976 | JEF United Chiba | Urawa Reds |
| 1977 | Shonan Bellmare | Urawa Reds |
| 1978 | Urawa Reds | Cerezo Osaka |
| 1979 | Shonan Bellmare | Tokyo Verdy |
| 1980 | Cerezo Osaka | Shonan Bellmare |
| 1981 | Shonan Bellmare | Tokyo Verdy |
| 1982 | Urawa Reds | Cerezo Osaka |
| 1983 | Tokyo Verdy | Yokohama F. Marinos |
| 1984 | Tokyo Verdy | Yokohama F. Marinos |
| 1985/86 | JEF United Chiba | NKK |
| 1986/87 | Tokyo Verdy | NKK |
| 1987/88 | Júbilo Iwata | NKK |
| 1988/89 | Yokohama F. Marinos | Yokohama Flügels |
| 1989/90 | Yokohama F. Marinos | Tokyo Verdy |
| 1990/91 | Tokyo Verdy | Yokohama F. Marinos |
| 1991/92 | Tokyo Verdy | Yokohama F. Marinos |
| 1993 | Tokyo Verdy | Kashima Antlers |
| 1994 | Tokyo Verdy | Sanfrecce Hiroshima |
| 1995 | Yokohama F. Marinos | Tokyo Verdy |
| 1996 | Kashima Antlers | Nagoya Grampus |
| 1997 | Júbilo Iwata | Kashima Antlers |
| 1998 | Kashima Antlers | Júbilo Iwata |
| 1999 | Júbilo Iwata | Shimizu S-Pulse |
| 2000 | Kashima Antlers | Yokohama F. Marinos |
| 2001 | Kashima Antlers | Júbilo Iwata |
| 2002 | Júbilo Iwata | Yokohama F. Marinos |
| 2003 | Yokohama F. Marinos | Júbilo Iwata |
| 2004 | Yokohama F. Marinos | Urawa Reds |
| 2005 | Gamba Osaka | Urawa Reds |
| 2006 | Urawa Reds | Kawasaki Frontale |
| 2007 | Kashima Antlers | Urawa Reds |
| 2008 | Kashima Antlers | Kawasaki Frontale |
| 2009 | Kashima Antlers | Kawasaki Frontale |
| 2010 | Nagoya Grampus | Gamba Osaka |
| 2011 | Kashiwa Reysol | Nagoya Grampus |
| 2012 | Sanfrecce Hiroshima | Vegalta Sendai |
| 2013 | Sanfrecce Hiroshima | Yokohama F. Marinos |
| 2014 | Gamba Osaka | Urawa Reds |
| 2015 | Sanfrecce Hiroshima | Gamba Osaka |
| 2016 | Kashima Antlers | Urawa Reds |
| 2017 | Kawasaki Frontale | Kashima Antlers |
| 2018 | Kawasaki Frontale | Sanfrecce Hiroshima |
| 2019 | Yokohama F. Marinos | FC Tokyo |
| 2020 | Kawasaki Frontale | Gamba Osaka |
| 2021 | Kawasaki Frontale | Yokohama F. Marinos |
| 2022 | Yokohama F. Marinos | Kawasaki Frontale |
| 2023 | Vissel Kobe | Yokohama F. Marinos |
| 2024 | Vissel Kobe | Sanfrecce Hiroshima |
| 2025 | Kashima Antlers | Kashiwa Reysol |

**Rebaixados marcados na classificação:** 90 em 43 edições (só onde a tabela publicada marca a queda); quem mais caiu: Shonan Bellmare (6), Júbilo Iwata (5), Kashiwa Reysol (5), Consadole Sapporo (5), Sanfrecce Hiroshima (4).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1977: Shonan Bellmare +1
- 1977: Urawa Reds +4
- 1977: Kashiwa Reysol +4
- 1977: Sanfrecce Hiroshima +2
- 1977: Cerezo Osaka +3
- 1977: JEF United Chiba +2
- 1977: Nippon Steel Yawata +2
- 1977: NKK +3
- 1977: Kawasaki Frontale +2
- 1978: Urawa Reds +1
- 1978: Cerezo Osaka +1
- 1978: Shonan Bellmare +3
- 1978: Tokyo Verdy +1
- 1978: Kashiwa Reysol +1
- 1978: Sanfrecce Hiroshima +3
- 1978: Nippon Steel Yawata +2
- 1978: Kawasaki Frontale +1
- 1978: JEF United Chiba +1
- 1979: Shonan Bellmare +1
- 1979: Kashiwa Reysol +5
- 1979: Cerezo Osaka +1
- 1979: JEF United Chiba +5
- 1979: Sanfrecce Hiroshima +4
- 1979: Urawa Reds +5
- 1979: Nippon Steel Yawata +2
- 1979: NKK +1
- 1979: Yokohama F. Marinos +2

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/jpn-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Divergências entre fontes já explicadas (`EXPLICACOES`, 3)

- **1966:** a tabela de confrontos da RSSSF dá 4 gols a menos ao Yawata (Nippon Steel Yawata) contra o Hitachi (Kashiwa Reysol) do que a tabela final (33-16 e 24-28, iguais na Wikipédia em japonês, que cita o livro oficial da JSL): um dos dois jogos entre eles (Yawata 2-1 Hitachi ou Hitachi 1-2 Yawata) deveria ter 4 gols a mais do Yawata, sem mudar o vencedor. Nenhuma fonte pública tem o placar; os jogos ficam como a RSSSF escreve e a classificação é a tabela final
- **1971:** a tabela de confrontos da RSSSF tem 2 gols a menos que a tabela final: um do Furukawa (JEF United Chiba) e um do Nippon Kokan (NKK), sofridos pelo Yanmar (Cerezo Osaka) e pelo Hitachi (Kashiwa Reysol), um cada. Há dois jeitos de encaixar (Furukawa x Yanmar e Nippon Kokan x Hitachi, ou Furukawa x Hitachi e Nippon Kokan x Yanmar), sem mudar vencedor; nenhuma fonte pública tem o placar. Os jogos ficam como a RSSSF escreve e a classificação é a tabela final
- **1973:** a tabela de confrontos da RSSSF tem 1 gol a menos para o Yanmar (Cerezo Osaka) e 1 a menos para o Furukawa (JEF United Chiba) do que a tabela final: um dos jogos entre os dois (Furukawa 0-0 Yanmar ou Yanmar 1-2 Furukawa) deveria ter um gol a mais de cada lado, sem mudar o resultado. Nenhuma fonte pública tem o placar; os jogos ficam como a RSSSF escreve e a classificação é a tabela final

### Jogos decididos fora de campo (placar oficial; o de campo no gols_texto) (`AWD`, 1)

- **25153:** placar de campo 2-3; a J.League registra 0-3 para o Shonan (a tabela oficial conta 0-3, e o ogol marca o jogo como decisão administrativa)

### Identidade dos clubes

Regras em `coleta/jpn-1/clubes_jpn.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes da 1ª divisão japonesa (JSL 1965-1991/92 e J1 1993-2025).

Um cadastro por clube, com o nome atual pelo qual é conhecido no Brasil (o do ogol, quase sempre). Os clubes de
empresa da JSL que viraram clubes da J.League são o mesmo clube com outro nome (a J.League e os clubes contam a
história assim, e a lista de campeões da RSSSF também): os nomes antigos ficam no nomes_fonte.

- Toyo Industries / Toyo Kogyo / Mazda -> Sanfrecce Hiroshima; Mitsubishi (Heavy Industries, depois Motors) -> Urawa Reds;
  Furukawa (Electric, depois JR East Furukawa) -> JEF United Chiba (JEF United Ichihara até 2004); Hitachi -> Kashiwa Reysol;
  Yanmar Diesel -> Cerezo Osaka; Towa Estate Agent / Fujita -> Shonan Bellmare (Bellmare Hiratsuka até 1999);
  Toyota (Motor) -> Nagoya Grampus (Nagoya Grampus Eight até 2008); Fujitsu -> Kawasaki Frontale; Nissan -> Yokohama
  F. Marinos (Yokohama Marinos até 1998); Yomiuri -> Tokyo Verdy (Verdy Kawasaki até 2000); Sumitomo (Metal) -> Kashima
  Antlers; All Nippon Airways -> Yokohama Flügels; Matsushita -> Gamba Osaka; Yamaha (Motors) -> Júbilo Iwata;
  Toshiba -> Consadole Sapporo (o Toshiba de Kawasaki mudou para Sapporo em 1996 e virou o Consadole).
- Yokohama F. Marinos x Yokohama Flügels: em 1999 o Flügels fechou e o Marinos ganhou o "F." no nome. São dois clubes: o
  Flügels fica com a história dele (1993-1998, e o ANA na JSL).
- Clubes da JSL que não chegaram à J.League ficam com o último nome da JSL: Nippon Steel Yawata (Yawata Steel até 1969),
  NKK (Nippon Kokan até 1988), Honda FC, Nagoya Bank, Toyoda ALW (Toyoda Automatic Loom Works), Tanabe Pharmaceuticals,
  Eidai Industries.

REGRAS: (regex sobre a chave do nome, nome de exibição). A chave é o nome em minúsculas, só letras e números.
```

## 8. O que não deu para coletar

- **Fora do pacote:** a repescagem entre a J1 e a 2ª divisão (JSL: "Promotion/Relegation Playoffs"; J1: 1998, 2004-2008, 2018, 2019 e 2022), como no Alemão: entra com a 2ª divisão. A JSL Division 2, a Copa do Imperador, a Copa da J.League e a Supercopa.
- **Edições sem jogos:** nenhuma.
- **Edições com jogos incompletos:** nenhuma. Na JSL os jogos vêm da tabela de confrontos: sem data, rodada nem autores dos gols (menos 1988/89, que tem rodada e data); de 1977 a 1979 os empates eram decididos nos pênaltis e a página não diz quem ganhou cada disputa (os jogos ficam como empate; as vitórias e derrotas nos pênaltis de cada clube estão na classificação).
- **Edições sem jogos** (0): nenhuma.
- **Décadas com menos da metade dos gols com autor:** 1960s, 1970s, 1980s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1960s, 1970s, 1980s.
- Estatísticas de jogo (chutes, faltas, escanteios): não coletadas.

## 9. Pendências e próximos passos

- JSL (1965 a 1991/92): os jogos vêm da tabela de confrontos da RSSSF, sem data, rodada nem autores dos gols (menos 1988/89, com rodada e data). Fonte que resolveria: o livro oficial 'Nihon Soccer League Zenshi' (1993), citado pela Wikipédia em japonês, ou jornais da época.
- 1966, 1971 e 1973: a tabela de confrontos da RSSSF não fecha com a tabela final por 1 a 4 gols num confronto (há duas células possíveis; explicado na edição). A mesma fonte acima resolveria.
- 1977 a 1979: os empates foram decididos nos pênaltis e a página não diz quem ganhou cada disputa.
- J1: a J.League não marca os gols de pênalti (ficam como 'normal') nem dá o nome de quem fez gol contra.
- Artilheiro de 1986/87: a lista de campeões da Wikipédia dá 17 gols a Toshio Matsuura (NKK), a RSSSF dá 14; ficou o da Wikipédia. Fonte que resolveria: o livro oficial da JSL.

## 10. Arquivos e comandos

Código em `coleta/jpn-1/`:

| Arquivo | O que faz |
|---|---|
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga jpn.1) de 2003 a 2025 para data/coleta/jpn-1/espn/jpn1_<ano>.json. |
| `baixar_jleague.py` | Baixa do J.League Data Site (data.j-league.or.jp, o site oficial de dados da J.League), em inglês, os jogos da J1 |
| `baixar_ogol.py` | Baixa o calendário de cada edição da J1 (1993-2025) no ogol para data/coleta/jpn-1/ogol/<ano>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão japonesa para data/coleta/jpn-1/rsssf/: a lista de campeões (japchamp.html), |
| `baixar_tabelas_jleague.py` | Baixa do J.League Data Site as tabelas oficiais da J1 (1993-2025), base da conferência e da classificação final. |
| `baixar_wikipedia.py` | Baixa da Wikipédia em inglês as listas de campeões japoneses ("List of Japanese football champions", com a JSL e a |
| `campeoes_wiki.py` | Campeão, vice e 3º de cada temporada na Wikipédia em inglês (List of Japanese football champions), segunda fonte do |
| `clubes_jpn.py` | Identidade dos clubes da 1ª divisão japonesa (JSL 1965-1991/92 e J1 1993-2025). |
| `edicoes.py` | Edições do Campeonato Japonês (1ª divisão), uma por título, como na lista de campeões da RSSSF (japchamp.html) e da |
| `explicacoes.py` | Correções e decisões da coleta do Campeonato Japonês (jpn-1), sempre com o motivo. |
| `importar.py` | Monta o pacote do Campeonato Japonês (jpn-1) em data/coleta/jpn-1/pacote/ e o relatório docs/coleta/jpn-1.md. |
| `ler_jleague.py` | Lê os jogos da J1 (1993-2025) baixados do J.League Data Site (baixar_jleague.py): a lista de cada ano |
| `ler_jsl.py` | Lê a 1ª divisão da Japan Soccer League (JSL, 1965 a 1991/92) nas páginas de temporada da RSSSF (jap65.html a jap92.html). |
| `relatorio.py` | Escreve o relatório da coleta (docs/coleta/jpn-1.md), chamado pelo importar.py. |

- Fontes baixadas: `data/coleta/jpn-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-asia/`, do ogol em `data/cache/ogol-jpn-1/`.
- Pacote: `data/coleta/jpn-1/pacote/`; relatório: `docs/coleta/jpn-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/jpn-1/baixar_espn.py
python coleta/jpn-1/baixar_jleague.py
python coleta/jpn-1/baixar_ogol.py
python coleta/jpn-1/baixar_rsssf.py
python coleta/jpn-1/baixar_tabelas_jleague.py
python coleta/jpn-1/baixar_wikipedia.py
python coleta/jpn-1/importar.py
python coleta/jpn-1/conferir.py [-v temporada]   # divergências
python coleta/comum-asia/testar_carga.py jpn-1 <scratchpad>
python coleta/comum-asia/documentar.py
```

