# Campeonato Japonês (1ª divisão) — coleta de dados

Gerado por `python coleta/jpn-1/importar.py`. Pacote em `data/coleta/jpn-1/pacote/`.

**Edições:** 60, uma por título, de 1965 a 2025, como na lista de campeões da RSSSF (`japchamp.html`, 60 títulos) e da
Wikipédia em inglês (List of Japanese football champions). Japan Soccer League (JSL, amadora: 1965 a 1984 em ano fechado,
1985/86 a 1991/92 no calendário europeu) e J.League (J1, profissional, de 1993 em diante). Em 1992 não houve liga (só a
Copa da J.League). Nos anos de dois turnos (1993-1995, 1997-2004, 2015 e 2016), o campeão é o vencedor da final entre os
campeões dos turnos (o campeão oficial); os turnos entram como fases.

**Fora do pacote:** a repescagem entre a J1 e a 2ª divisão (JSL: "Promotion/Relegation Playoffs"; J1: 1998, 2004-2008, 2018,
2019 e 2022), como no Alemão: entra com a 2ª divisão. A JSL Division 2, a Copa do Imperador, a Copa da J.League e a
Supercopa.

**Fontes:** RSSSF (uma página por temporada da JSL, `jap65.html` a `jap92.html`, em `data/coleta/jpn-1/rsssf/`: tabela final,
tabela de confrontos com todos os jogos, rodadas com data em 1988/89 e artilheiros); J.League Data Site
(data.j-league.or.jp, o site oficial de dados da J.League, em inglês: lista de jogos de cada ano em
`data/coleta/jpn-1/jleague/lista_<ano>.json`, página de cada jogo, com autores dos gols e minuto, cartões, árbitro, estádio e
público, no cache `data/cache/jleague-asia/`, e as tabelas oficiais de cada turno e anual em `tabelas_<ano>.json`);
Wikipédia em inglês (lista de campeões: campeão, vice e 3º, segunda fonte); ESPN (liga `jpn.1`, 2006 em diante,
`data/coleta/jpn-1/espn/`: conferência dos placares); ogol (calendário da J1, 1993-2025, para os escudos:
`data/cache/ogol-jpn-1/`).

**Clubes:** 40. Nome pelo qual o clube é conhecido hoje (o do ogol, quase sempre). Os clubes de empresa da JSL que viraram
clubes da J.League são o mesmo clube, como a J.League, os clubes e a lista de campeões da RSSSF contam: Toyo Industries/Mazda =
Sanfrecce Hiroshima, Mitsubishi = Urawa Reds, Furukawa = JEF United Chiba, Hitachi = Kashiwa Reysol, Yanmar = Cerezo Osaka,
Towa Estate/Fujita = Shonan Bellmare, Toyota = Nagoya Grampus, Fujitsu = Kawasaki Frontale, Nissan = Yokohama F. Marinos,
Yomiuri = Tokyo Verdy, Sumitomo = Kashima Antlers, All Nippon Airways = Yokohama Flügels, Matsushita = Gamba Osaka,
Yamaha = Júbilo Iwata, Toshiba = Consadole Sapporo. O Yokohama Flügels (fechado em 1998, fundido ao Marinos) é um clube
separado do Yokohama F. Marinos. Os nomes de cada fonte estão no `nomes_fonte` do `clubes.csv` (regras em
`coleta/jpn-1/clubes_jpn.py`).

**Regras:** placar oficial, com a prorrogação. De 1993 a 1998 não havia empate: prorrogação com gol de ouro e, empatado, pênaltis
(`penaltis_mandante`/`penaltis_visitante`); de 1999 a 2002, prorrogação com gol de ouro e empate se ela terminasse sem gol.
Pontos por vitória: JSL 2 (1965-1976 e 1980-1987/88), 4 (1977-1979, com 2 para a vitória nos pênaltis e 1 para a derrota
nos pênaltis) e 3 (1988/89 em diante); J1 sem pontos em 1993-1994 (ordem por vitórias), 3 por vitória (também nos pênaltis) e 1 pela derrota nos pênaltis em
1995-1996, 3/2/1 (tempo normal, prorrogação, pênaltis) em 1997-1998, 3/2/1 (tempo normal, prorrogação, empate) em
1999-2002, 3/1/0 de 2003 em diante. A classificação final é a tabela oficial (J1: J.League; JSL: RSSSF); nos anos de turnos, a
tabela anual oficial (1999-2004, 2015, 2016) ou a soma das tabelas dos turnos (1993-1998), com o campeão e o vice da final em
1º e 2º. Rebaixado: o clube que não está na edição seguinte (fora os que fecharam: Eidai Industries em 1976, Yokohama
Flügels em 1998) e, na J1, o marcado "J2" na tabela oficial. Em 1991/92 ninguém caiu: a JSL acabou e os clubes foram para a
J.League ou para a nova JFL. Gol contra: a J.League escreve "Own-Goal" sem o nome do jogador (`jogador` vazio, `tipo`
`contra`). A J.League não marca os gols de pênalti (ficam como `normal`). Artilheiro: o da lista de campeões da Wikipédia em inglês (a contagem oficial),
conferido com a RSSSF (JSL) e com a soma dos gols da J.League (J1).

**Conferência:** JSL: soma dos jogos da tabela de confrontos contra a tabela final da RSSSF (pontos pela regra de cada ano);
a tabela final é a mesma da Wikipédia em japonês, que cita o livro oficial da JSL. J1: cada tabela oficial de turno e anual
da J.League contra a soma dos jogos, com jogos, vitórias, empates, derrotas, gols e pontos (pela regra de cada época): todas
fecham. Placares conferidos também com o ogol (1993-1996 e 2004-2025; o ogol não tem os jogos de 1997 a 2003) e com a ESPN
(2006-2025). As diferenças listadas nas edições são erros dessas fontes: a ESPN tem placares parciais (o ogol e a tabela
oficial confirmam a J.League); o ogol de 1996 soma a disputa de pênaltis ao placar; no jogo de 2005 a J.League fecha com a
tabela oficial. Um jogo decidido fora de campo (2021, Urawa Reds x Shonan Bellmare: 2-3 em campo, 0-3 oficial) entra como
`awd`.

**Edições sem jogos:** nenhuma.

**Edições com jogos incompletos:** nenhuma. Na JSL os jogos vêm da tabela de confrontos: sem data, rodada nem autores dos gols
(menos 1988/89, que tem rodada e data); de 1977 a 1979 os empates eram decididos nos pênaltis e a página não diz quem
ganhou cada disputa (os jogos ficam como empate; as vitórias e derrotas nos pênaltis de cada clube estão na classificação).

**Resumo:** 12190 jogos, 27554 gols com autor, 31272 cartões.

| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1965 | 8 | 56 (56) | 216 | 0 | 1 / 0 | Sanfrecce Hiroshima | RSSSF (jap65.html) |
| 1966 | 8 | 56 (56) | 179 | 0 | 0 / 1 | Sanfrecce Hiroshima | RSSSF (jap66.html) |
| 1967 | 8 | 56 (56) | 225 | 0 | 1 / 0 | Sanfrecce Hiroshima | RSSSF (jap67.html) |
| 1968 | 8 | 56 (56) | 185 | 0 | 1 / 0 | Sanfrecce Hiroshima | RSSSF (jap68.html) |
| 1969 | 8 | 56 (56) | 176 | 0 | 1 / 0 | Urawa Reds | RSSSF (jap69.html) |
| 1970 | 8 | 56 (56) | 179 | 0 | 1 / 0 | Sanfrecce Hiroshima | RSSSF (jap70.html) |
| 1971 | 8 | 56 (56) | 170 | 0 | 0 / 1 | Cerezo Osaka | RSSSF (jap71.html) |
| 1972 | 8 | 56 (56) | 177 | 0 | 1 / 0 | Kashiwa Reysol | RSSSF (jap72.html) |
| 1973 | 10 | 90 (90) | 262 | 0 | 0 / 1 | Urawa Reds | RSSSF (jap73.html) |
| 1974 | 10 | 90 (90) | 262 | 0 | 1 / 0 | Cerezo Osaka | RSSSF (jap74.html) |
| 1975 | 10 | 90 (90) | 268 | 0 | 1 / 0 | Cerezo Osaka | RSSSF (jap75.html) |
| 1976 | 10 | 90 (90) | 238 | 0 | 1 / 0 | JEF United Chiba | RSSSF (jap76.html) |
| 1977 | 10 | 90 (90) | 315 | 0 | 1 / 0 | Shonan Bellmare | RSSSF (jap77.html) |
| 1978 | 10 | 90 (90) | 245 | 0 | 1 / 0 | Urawa Reds | RSSSF (jap78.html) |
| 1979 | 10 | 90 (90) | 248 | 0 | 1 / 0 | Shonan Bellmare | RSSSF (jap79.html) |
| 1980 | 10 | 90 (90) | 265 | 0 | 1 / 0 | Cerezo Osaka | RSSSF (jap80.html) |
| 1981 | 10 | 90 (90) | 215 | 0 | 1 / 0 | Shonan Bellmare | RSSSF (jap81.html) |
| 1982 | 10 | 90 (90) | 214 | 0 | 1 / 0 | Urawa Reds | RSSSF (jap82.html) |
| 1983 | 10 | 90 (90) | 193 | 0 | 1 / 0 | Tokyo Verdy | RSSSF (jap83.html) |
| 1984 | 10 | 90 (90) | 252 | 0 | 1 / 0 | Tokyo Verdy | RSSSF (jap84.html) |
| 1985/86 | 12 | 132 (132) | 323 | 0 | 1 / 0 | JEF United Chiba | RSSSF (jap86.html) |
| 1986/87 | 12 | 132 (132) | 278 | 0 | 1 / 0 | Tokyo Verdy | RSSSF (jap87.html) |
| 1987/88 | 12 | 132 (132) | 238 | 0 | 1 / 0 | Júbilo Iwata | RSSSF (jap88.html) |
| 1988/89 | 12 | 132 (132) | 292 | 0 | 1 / 0 | Yokohama F. Marinos | RSSSF (jap89.html) |
| 1989/90 | 12 | 132 (132) | 305 | 0 | 1 / 0 | Yokohama F. Marinos | RSSSF (jap90.html) |
| 1990/91 | 12 | 132 (132) | 287 | 0 | 1 / 0 | Tokyo Verdy | RSSSF (jap91.html) |
| 1991/92 | 12 | 132 (132) | 318 | 0 | 1 / 0 | Tokyo Verdy | RSSSF (jap92.html) |
| 1993 | 10 | 182 (182) | 536 | 536 | 2 / 0 | Tokyo Verdy | soma das tabelas oficiais dos dois turnos (J.League Data Site), ordenada por vitórias, saldo e gols pró |
| 1994 | 12 | 266 (266) | 843 | 843 | 2 / 0 | Tokyo Verdy | soma das tabelas oficiais dos dois turnos (J.League Data Site), ordenada por vitórias, saldo e gols pró |
| 1995 | 14 | 366 (366) | 1216 | 1216 | 2 / 0 | Yokohama F. Marinos | soma das tabelas oficiais dos dois turnos (J.League Data Site), ordenada por pontos, saldo e gols pró |
| 1996 | 16 | 240 (240) | 778 | 778 | 1 / 0 | Kashima Antlers | J.League Data Site (tabela oficial: J.LEAGUE) |
| 1997 | 17 | 274 (274) | 904 | 904 | 2 / 0 | Júbilo Iwata | soma das tabelas oficiais dos dois turnos (J.League Data Site), ordenada por pontos, saldo e gols pró |
| 1998 | 18 | 308 (308) | 1080 | 1080 | 2 / 0 | Kashima Antlers | soma das tabelas oficiais dos dois turnos (J.League Data Site), ordenada por pontos, saldo e gols pró |
| 1999 | 16 | 242 (242) | 763 | 763 | 2 / 0 | Júbilo Iwata | J.League Data Site (tabela anual oficial: Overall table for the season) |
| 2000 | 16 | 242 (242) | 715 | 715 | 2 / 0 | Kashima Antlers | J.League Data Site (tabela anual oficial: Overall table for the season) |
| 2001 | 16 | 242 (242) | 793 | 793 | 2 / 0 | Kashima Antlers | J.League Data Site (tabela anual oficial: Overall table for the season) |
| 2002 | 16 | 240 (240) | 683 | 683 | 2 / 0 | Júbilo Iwata | J.League Data Site (tabela anual oficial: Overall table for the season) |
| 2003 | 16 | 240 (240) | 718 | 718 | 2 / 0 | Yokohama F. Marinos | J.League Data Site (tabela anual oficial: Overall table for the season) |
| 2004 | 16 | 242 (242) | 746 | 746 | 2 / 0 | Yokohama F. Marinos | J.League Data Site (tabela anual oficial: Overall table for the season) |
| 2005 | 18 | 306 (306) | 873 | 873 | 1 / 0 | Gamba Osaka | J.League Data Site (tabela oficial: J.LEAGUE Division 1) |
| 2006 | 18 | 306 (306) | 976 | 976 | 1 / 0 | Urawa Reds | J.League Data Site (tabela oficial: J.LEAGUE Division 1) |
| 2007 | 18 | 306 (306) | 867 | 867 | 1 / 0 | Kashima Antlers | J.League Data Site (tabela oficial: J.LEAGUE Division 1) |
| 2008 | 18 | 306 (306) | 783 | 783 | 1 / 0 | Kashima Antlers | J.League Data Site (tabela oficial: J.LEAGUE Division 1) |
| 2009 | 18 | 306 (306) | 791 | 791 | 1 / 0 | Kashima Antlers | J.League Data Site (tabela oficial: J.LEAGUE Division 1) |
| 2010 | 18 | 306 (306) | 813 | 813 | 1 / 0 | Nagoya Grampus | J.League Data Site (tabela oficial: J.LEAGUE Division 1) |
| 2011 | 18 | 306 (306) | 869 | 869 | 1 / 0 | Kashiwa Reysol | J.League Data Site (tabela oficial: J.LEAGUE Division 1) |
| 2012 | 18 | 306 (306) | 855 | 855 | 1 / 0 | Sanfrecce Hiroshima | J.League Data Site (tabela oficial: J.LEAGUE Division 1) |
| 2013 | 18 | 306 (306) | 879 | 879 | 1 / 0 | Sanfrecce Hiroshima | J.League Data Site (tabela oficial: J.LEAGUE Division 1) |
| 2014 | 18 | 306 (306) | 774 | 774 | 1 / 0 | Gamba Osaka | J.League Data Site (tabela oficial: J.LEAGUE Division 1) |
| 2015 | 18 | 309 (309) | 831 | 831 | 2 / 0 | Sanfrecce Hiroshima | J.League Data Site (tabela anual oficial: Overall table for the season) |
| 2016 | 18 | 309 (309) | 810 | 810 | 2 / 0 | Kashima Antlers | J.League Data Site (tabela anual oficial: Overall table for the season) |
| 2017 | 18 | 306 (306) | 793 | 793 | 1 / 0 | Kawasaki Frontale | J.League Data Site (tabela oficial: MEIJI YASUDA J1 LEAGUE) |
| 2018 | 18 | 306 (306) | 813 | 813 | 1 / 0 | Kawasaki Frontale | J.League Data Site (tabela oficial: MEIJI YASUDA J1 LEAGUE) |
| 2019 | 18 | 306 (306) | 797 | 797 | 1 / 0 | Yokohama F. Marinos | J.League Data Site (tabela oficial: MEIJI YASUDA J1 LEAGUE) |
| 2020 | 18 | 306 (306) | 866 | 866 | 1 / 0 | Kawasaki Frontale | J.League Data Site (tabela oficial: MEIJI YASUDA J1 LEAGUE) |
| 2021 | 20 | 380 (380) | 920 | 917 | 1 / 0 | Kawasaki Frontale | J.League Data Site (tabela oficial: MEIJI YASUDA J1 LEAGUE) |
| 2022 | 18 | 306 (306) | 771 | 771 | 1 / 0 | Yokohama F. Marinos | J.League Data Site (tabela oficial: MEIJI YASUDA J1 LEAGUE) |
| 2023 | 18 | 306 (306) | 777 | 777 | 1 / 0 | Vissel Kobe | J.League Data Site (tabela oficial: MEIJI YASUDA J1 LEAGUE) |
| 2024 | 20 | 380 (380) | 1013 | 1013 | 1 / 0 | Vissel Kobe | J.League Data Site (tabela oficial: MEIJI YASUDA J1 LEAGUE) |
| 2025 | 20 | 380 (380) | 911 | 911 | 1 / 0 | Kashima Antlers | J.League Data Site (tabela oficial: MEIJI YASUDA J1 LEAGUE) |

## Conferência e correções, edição a edição

### 1965

- campeão Sanfrecce Hiroshima (Wikipédia, lista de campeões: Toyo Industries).
- Formato: pontos corridos, 8 clubes, turno e returno.
- Artilheiro: Mutsuhiko Nomura (Kashiwa Reysol), 15.

### 1966

- campeão Sanfrecce Hiroshima (Wikipédia, lista de campeões: Toyo Industries); divergências explicadas no relatório.
- Formato: pontos corridos, 8 clubes, turno e returno.
- Divergências com a tabela publicada: Nippon Steel Yawata: tabela [14, 10, 1, 3, 33, 16], jogos [14, 10, 1, 3, 29, 16]; Kashiwa Reysol: tabela [14, 5, 3, 6, 24, 28], jogos [14, 5, 3, 6, 24, 24].
- Rebaixados: Nagoya Bank.
- Artilheiro: Aritatsu Ogi (Sanfrecce Hiroshima), 14.

### 1967

- campeão Sanfrecce Hiroshima (Wikipédia, lista de campeões: Toyo Industries).
- Formato: pontos corridos, 8 clubes, turno e returno.
- Rebaixados: Toyoda ALW.
- Artilheiro: Takeo Kimura (JEF United Chiba), 15.

### 1968

- campeão Sanfrecce Hiroshima (Wikipédia, lista de campeões: Toyo Industries).
- Formato: pontos corridos, 8 clubes, turno e returno.
- Artilheiro: Kunishige Kamamoto (Cerezo Osaka), 14.

### 1969

- campeão Urawa Reds (Wikipédia, lista de campeões: Mitsubishi Heavy Industries).
- Formato: pontos corridos, 8 clubes, turno e returno.
- Artilheiro: Hiroshi Ochiai (Urawa Reds), 12.

### 1970

- campeão Sanfrecce Hiroshima (Wikipédia, lista de campeões: Toyo Industries).
- Formato: pontos corridos, 8 clubes, turno e returno.
- Artilheiro: Kunishige Kamamoto (Cerezo Osaka), 16.

### 1971

- campeão Cerezo Osaka (Wikipédia, lista de campeões: Yanmar Diesel); divergências explicadas no relatório.
- Formato: pontos corridos, 8 clubes, turno e returno.
- Divergências com a tabela publicada: Cerezo Osaka: tabela [14, 9, 4, 1, 32, 13], jogos [14, 9, 4, 1, 32, 12]; Kashiwa Reysol: tabela [14, 7, 4, 3, 18, 17], jogos [14, 7, 4, 3, 18, 16]; JEF United Chiba: tabela [14, 5, 5, 4, 24, 24], jogos [14, 5, 5, 4, 23, 24]; NKK: tabela [14, 2, 4, 8, 11, 23], jogos [14, 2, 4, 8, 10, 23].
- Rebaixados: Nagoya Bank.
- Artilheiro: Kunishige Kamamoto (Cerezo Osaka), 11.

### 1972

- campeão Kashiwa Reysol (Wikipédia, lista de campeões: Hitachi SC).
- Formato: pontos corridos, 8 clubes, turno e returno.
- Artilheiro: Akira Matsunaga (Kashiwa Reysol), 12.
- Artilheiro: diferença entre as fontes (artilheiro na Wikipédia: Akira Matsunaga (Kashiwa Reysol) 12; pela RSSSF: ); vale a Wikipédia (contagem oficial).

### 1973

- campeão Urawa Reds (Wikipédia, lista de campeões: Mitsubishi Heavy Industries); divergências explicadas no relatório.
- Formato: pontos corridos, 10 clubes, turno e returno.
- Divergências com a tabela publicada: Cerezo Osaka: tabela [18, 10, 3, 5, 40, 17], jogos [18, 10, 3, 5, 39, 16]; JEF United Chiba: tabela [18, 9, 3, 6, 31, 27], jogos [18, 9, 3, 6, 30, 26].
- Rebaixados: Tanabe Pharmaceuticals.
- Artilheiro: Akira Matsunaga (Kashiwa Reysol), 11.

### 1974

- campeão Cerezo Osaka (Wikipédia, lista de campeões: Yanmar Diesel).
- Formato: pontos corridos, 10 clubes, turno e returno.
- Artilheiro: Kunishige Kamamoto (Cerezo Osaka), 21.

### 1975

- campeão Cerezo Osaka (Wikipédia, lista de campeões: Yanmar Diesel).
- Formato: pontos corridos, 10 clubes, turno e returno.
- Artilheiro: Kunishige Kamamoto (Cerezo Osaka), 17.

### 1976

- campeão JEF United Chiba (Wikipédia, lista de campeões: Furukawa Electric).
- Formato: pontos corridos, 10 clubes, turno e returno.
- Artilheiro: Kunishige Kamamoto (Cerezo Osaka), 15.

### 1977

- campeão Shonan Bellmare (Wikipédia, lista de campeões: Fujita Industries).
- Formato: pontos corridos, 10 clubes, turno e returno.
- empates decididos nos pênaltis (4 pontos a vitória, 2 a vitória nos pênaltis, 1 a derrota nos pênaltis); a tabela de confrontos não diz quem ganhou cada disputa: os jogos ficam como empate.
- Rebaixados: Nagoya Grampus.
- Artilheiro: Carvalho (Shonan Bellmare), 23.

### 1978

- campeão Urawa Reds (Wikipédia, lista de campeões: Mitsubishi Heavy Industries).
- Formato: pontos corridos, 10 clubes, turno e returno.
- empates decididos nos pênaltis (4 pontos a vitória, 2 a vitória nos pênaltis, 1 a derrota nos pênaltis); a tabela de confrontos não diz quem ganhou cada disputa: os jogos ficam como empate.
- Rebaixados: Kawasaki Frontale.
- Artilheiro: Kunishige Kamamoto (Cerezo Osaka), 15; Carvalho (Shonan Bellmare), 15.

### 1979

- campeão Shonan Bellmare (Wikipédia, lista de campeões: Fujita Industries).
- Formato: pontos corridos, 10 clubes, turno e returno.
- empates decididos nos pênaltis (4 pontos a vitória, 2 a vitória nos pênaltis, 1 a derrota nos pênaltis); a tabela de confrontos não diz quem ganhou cada disputa: os jogos ficam como empate.
- Rebaixados: NKK.
- Artilheiro: Ruy Ramos (Tokyo Verdy), 14.

### 1980

- campeão Cerezo Osaka (Wikipédia, lista de campeões: Yanmar Diesel).
- Formato: pontos corridos, 10 clubes, turno e returno.
- Rebaixados: Yokohama F. Marinos.
- Artilheiro: Hiroyuki Usui (Kashiwa Reysol), 14.

### 1981

- campeão Shonan Bellmare (Wikipédia, lista de campeões: Fujita Industries).
- Formato: pontos corridos, 10 clubes, turno e returno.
- Rebaixados: Nippon Steel Yawata, Júbilo Iwata.
- Artilheiro: Hiroshi Yoshida (JEF United Chiba), 14.

### 1982

- campeão Urawa Reds (Wikipédia, lista de campeões: Mitsubishi Heavy Industries).
- Formato: pontos corridos, 10 clubes, turno e returno.
- Rebaixados: NKK.
- Artilheiro: Hiroyuki Usui (Kashiwa Reysol), 13.

### 1983

- campeão Tokyo Verdy (Wikipédia, lista de campeões: Yomiuri SC).
- Formato: pontos corridos, 10 clubes, turno e returno.
- Rebaixados: Sanfrecce Hiroshima.
- Artilheiro: Ruy Ramos (Tokyo Verdy), 10.

### 1984

- campeão Tokyo Verdy (Wikipédia, lista de campeões: Yomiuri SC).
- Formato: pontos corridos, 10 clubes, turno e returno.
- Artilheiro: Tetsuya Totsuka (Tokyo Verdy), 14.

### 1985/86

- campeão JEF United Chiba (Wikipédia, lista de campeões: Furukawa Electric).
- Formato: pontos corridos, 12 clubes, turno e returno.
- Rebaixados: Kashima Antlers, Yokohama Flügels.
- Artilheiro: Hiroshi Yoshida (JEF United Chiba), 16.

### 1986/87

- campeão Tokyo Verdy (Wikipédia, lista de campeões: Yomiuri SC).
- Formato: pontos corridos, 12 clubes, turno e returno.
- Rebaixados: Gamba Osaka, Kashiwa Reysol.
- Artilheiro: Toshio Matsuura (NKK), 17.
- Artilheiro: diferença entre as fontes (artilheiro na Wikipédia: Toshio Matsuura (NKK) 17; pela RSSSF: Matsuura Toshio (NKK) 14); vale a Wikipédia (contagem oficial).

### 1987/88

- campeão Júbilo Iwata (Wikipédia, lista de campeões: Yamaha Motors).
- Formato: pontos corridos, 12 clubes, turno e returno.
- Rebaixados: Sanfrecce Hiroshima, Nagoya Grampus.
- Artilheiro: Toshio Matsuura (NKK), 11.

### 1988/89

- campeão Yokohama F. Marinos (Wikipédia, lista de campeões: Nissan Motors).
- Formato: pontos corridos, 12 clubes, turno e returno.
- rodada e data dos 132 jogos pela lista de rodadas da página.
- mando invertido na lista de rodadas, vale o da tabela de confrontos (que fecha com a tabela final): Yomiuri Nippon 2-0 Honda (rodada 9): na tabela de confrontos o mandante é o Honda FC.
- Rebaixados: Kashima Antlers, Urawa Reds.
- Artilheiro: Adílson (Júbilo Iwata), 11.

### 1989/90

- campeão Yokohama F. Marinos (Wikipédia, lista de campeões: Nissan Motors).
- Formato: pontos corridos, 12 clubes, turno e returno.
- Rebaixados: Shonan Bellmare, Kashiwa Reysol.
- Artilheiro: Renato (Yokohama F. Marinos), 17.

### 1990/91

- campeão Tokyo Verdy (Wikipédia, lista de campeões: Yomiuri SC).
- Formato: pontos corridos, 12 clubes, turno e returno.
- Rebaixados: Cerezo Osaka, NKK.
- Artilheiro: Tetsuya Totsuka (Tokyo Verdy), 10; Tsuyoshi Kitazawa (Honda FC), 10; Renato (Yokohama F. Marinos), 10.

### 1991/92

- campeão Tokyo Verdy (Wikipédia, lista de campeões: Yomiuri SC).
- Formato: pontos corridos, 12 clubes, turno e returno.
- Artilheiro: Toninho (Tokyo Verdy), 18.

### 1993

- campeão Tokyo Verdy (Wikipédia, lista de campeões: Verdy Kawasaki).
- Formato: dois turnos de pontos corridos (10 clubes, turno único em cada um); final entre os campeões dos turnos (ida e volta).
- ogol: 182 placares iguais.
- Artilheiro: Ramón Díaz (Yokohama F. Marinos), 28.

### 1994

- campeão Tokyo Verdy (Wikipédia, lista de campeões: Verdy Kawasaki).
- Formato: dois turnos de pontos corridos (12 clubes, turno único em cada um); final entre os campeões dos turnos (ida e volta).
- ogol: 264 placares iguais.
- Artilheiro: Frank Ordenewitz (JEF United Chiba), 30.
- Artilheiro: diferença entre as fontes (artilheiro na Wikipédia: Frank Ordenewitz (JEF United Chiba) 30; pela soma dos gols da J.League: Alcindo (Kashima Antlers) 28); vale a Wikipédia (contagem oficial).

### 1995

- campeão Yokohama F. Marinos (Wikipédia, lista de campeões: Yokohama Marinos).
- Formato: dois turnos de pontos corridos (14 clubes, turno único em cada um); final entre os campeões dos turnos (ida e volta).
- ogol: 366 placares iguais.
- Artilheiro: Masahiro Fukuda (Urawa Reds), 32.

### 1996

- campeão Kashima Antlers (Wikipédia, lista de campeões: Kashima Antlers).
- Formato: pontos corridos, 16 clubes, turno e returno.
- ogol: 229 placares iguais; diferentes: 1996-03-30 Júbilo Iwata 1-1 Urawa Reds (ogol 4-5); 1996-03-30 Gamba Osaka 2-2 Shimizu S-Pulse (ogol 6-5); 1996-04-17 Júbilo Iwata 2-2 Kashima Antlers (ogol 6-5); 1996-05-01 Urawa Reds 0-0 Cerezo Osaka (ogol 4-5); 1996-05-18 Yokohama Flügels 1-1 Kashima Antlers (ogol 7-6); 1996-09-14 Yokohama F. Marinos 0-0 Avispa Fukuoka (ogol 3-1); 1996-09-28 Urawa Reds 1-1 Avispa Fukuoka (ogol 4-3); 1996-09-28 Kashima Antlers 1-1 Sanfrecce Hiroshima (ogol 9-10); 1996-10-30 Kashima Antlers 2-2 Júbilo Iwata (ogol 6-5); 1996-11-02 Urawa Reds 0-0 Kashima Antlers (ogol 4-5); 1996-11-02 Nagoya Grampus 1-1 JEF United Chiba (ogol 5-3).
- Artilheiro: Kazuyoshi Miura (Tokyo Verdy), 23.

### 1997

- campeão Júbilo Iwata (Wikipédia, lista de campeões: Júbilo Iwata).
- Formato: dois turnos de pontos corridos (17 clubes, turno único em cada um); final entre os campeões dos turnos (ida e volta).
- Artilheiro: Patrick M'Boma (Gamba Osaka), 25.

### 1998

- campeão Kashima Antlers (Wikipédia, lista de campeões: Kashima Antlers).
- Formato: dois turnos de pontos corridos (18 clubes, turno único em cada um); final entre os campeões dos turnos (ida e volta).
- Rebaixados: Consadole Sapporo.
- Artilheiro: Masashi Nakayama (Júbilo Iwata), 36.

### 1999

- campeão Júbilo Iwata (Wikipédia, lista de campeões: Júbilo Iwata).
- Formato: dois turnos de pontos corridos (16 clubes, turno único em cada um); final entre os campeões dos turnos (ida e volta).
- Rebaixados: Urawa Reds, Shonan Bellmare.
- Artilheiro: Hwang Sun-hong (Cerezo Osaka), 24.

### 2000

- campeão Kashima Antlers (Wikipédia, lista de campeões: Kashima Antlers).
- Formato: dois turnos de pontos corridos (16 clubes, turno único em cada um); final entre os campeões dos turnos (ida e volta).
- Rebaixados: Kyoto Sanga, Kawasaki Frontale.
- Artilheiro: Masashi Nakayama (Júbilo Iwata), 20.

### 2001

- campeão Kashima Antlers (Wikipédia, lista de campeões: Kashima Antlers).
- Formato: dois turnos de pontos corridos (16 clubes, turno único em cada um); final entre os campeões dos turnos (ida e volta).
- Rebaixados: Avispa Fukuoka, Cerezo Osaka.
- Artilheiro: Will (Consadole Sapporo), 24.
- Artilheiro: diferença entre as fontes (gols corrigidos: a lista de campeões da Wikipédia dá 20 gols ao Will (Consadole Sapporo); os jogos oficiais da J.League somam 24, como a página da temporada na Wikipédia em inglês e a ficha dele na Wikipédia em japonês); vale a Wikipédia (contagem oficial).

### 2002

- campeão Júbilo Iwata (Wikipédia, lista de campeões: Júbilo Iwata).
- Formato: dois turnos de pontos corridos (16 clubes, turno único em cada um); sem final: o mesmo clube ganhou os dois turnos.
- Rebaixados: Sanfrecce Hiroshima, Consadole Sapporo.
- Artilheiro: Naohiro Takahara (Júbilo Iwata), 26.

### 2003

- campeão Yokohama F. Marinos (Wikipédia, lista de campeões: Yokohama F.&nbsp;Marinos).
- Formato: dois turnos de pontos corridos (16 clubes, turno único em cada um); sem final: o mesmo clube ganhou os dois turnos.
- Rebaixados: Vegalta Sendai, Kyoto Sanga.
- Artilheiro: Ueslei (Nagoya Grampus), 22.

### 2004

- campeão Yokohama F. Marinos (Wikipédia, lista de campeões: Yokohama F.&nbsp;Marinos).
- Formato: dois turnos de pontos corridos (16 clubes, turno único em cada um); final entre os campeões dos turnos (ida e volta).
- fora do pacote: 2 jogo(s) da repescagem J1/J2 (entram com a 2ª divisão).
- ogol: 241 placares iguais.
- Artilheiro: Emerson (Urawa Reds), 27.

### 2005

- campeão Gamba Osaka (Wikipédia, lista de campeões: Gamba Osaka).
- Formato: pontos corridos, 18 clubes, turno e returno.
- fora do pacote: 2 jogo(s) da repescagem J1/J2 (entram com a 2ª divisão).
- ogol: 305 placares iguais; diferentes: 2005-05-04 Yokohama F. Marinos 1-1 Shimizu S-Pulse (ogol 2-1).
- Rebaixados: Kashiwa Reysol, Tokyo Verdy, Vissel Kobe.
- Artilheiro: Araújo (Gamba Osaka), 33.

### 2006

- campeão Urawa Reds (Wikipédia, lista de campeões: Urawa Red Diamonds).
- Formato: pontos corridos, 18 clubes, turno e returno.
- fora do pacote: 2 jogo(s) da repescagem J1/J2 (entram com a 2ª divisão).
- ESPN: 306 placares iguais.
- ogol: 306 placares iguais.
- Rebaixados: Avispa Fukuoka, Cerezo Osaka, Kyoto Sanga.
- Artilheiro: Washington (Urawa Reds), 26; Magno Alves (Gamba Osaka), 26.

### 2007

- campeão Kashima Antlers (Wikipédia, lista de campeões: Kashima Antlers).
- Formato: pontos corridos, 18 clubes, turno e returno.
- fora do pacote: 2 jogo(s) da repescagem J1/J2 (entram com a 2ª divisão).
- ESPN: 306 placares iguais.
- ogol: 306 placares iguais.
- Rebaixados: Sanfrecce Hiroshima, Ventforet Kofu, Yokohama FC.
- Artilheiro: Juninho (Kawasaki Frontale), 22.

### 2008

- campeão Kashima Antlers (Wikipédia, lista de campeões: Kashima Antlers).
- Formato: pontos corridos, 18 clubes, turno e returno.
- fora do pacote: 2 jogo(s) da repescagem J1/J2 (entram com a 2ª divisão).
- ESPN: 306 placares iguais.
- ogol: 306 placares iguais.
- Rebaixados: Tokyo Verdy, Consadole Sapporo.
- Artilheiro: Marquinhos (Kashima Antlers), 21.

### 2009

- campeão Kashima Antlers (Wikipédia, lista de campeões: Kashima Antlers).
- Formato: pontos corridos, 18 clubes, turno e returno.
- ESPN: 305 placares iguais; diferentes: 2009-07-12 FC Tokyo 3-0 Nagoya Grampus (ESPN 2-0).
- ogol: 306 placares iguais.
- Rebaixados: Kashiwa Reysol, Oita Trinita, JEF United Chiba.
- Artilheiro: Ryoichi Maeda (Júbilo Iwata), 20.

### 2010

- campeão Nagoya Grampus (Wikipédia, lista de campeões: Nagoya Grampus).
- Formato: pontos corridos, 18 clubes, turno e returno.
- ESPN: 297 placares iguais.
- ogol: 306 placares iguais.
- Rebaixados: FC Tokyo, Kyoto Sanga, Shonan Bellmare.
- Artilheiro: Joshua Kennedy (Nagoya Grampus), 17; Ryoichi Maeda (Júbilo Iwata), 17.

### 2011

- campeão Kashiwa Reysol (Wikipédia, lista de campeões: Kashiwa Reysol).
- Formato: pontos corridos, 18 clubes, turno e returno.
- ESPN: 301 placares iguais; diferentes: 2011-05-03 Kawasaki Frontale 1-0 Júbilo Iwata (ESPN 0-0); 2011-05-07 Sanfrecce Hiroshima 1-1 Ventforet Kofu (ESPN 0-1); 2011-08-14 Albirex Niigata 2-3 Urawa Reds (ESPN 0-0); 2011-08-14 Júbilo Iwata 6-1 Kashiwa Reysol (ESPN 0-0); 2011-08-14 Avispa Fukuoka 2-1 Kawasaki Frontale (ESPN 0-0).
- ogol: 304 placares iguais.
- Rebaixados: Ventforet Kofu, Avispa Fukuoka, Montedio Yamagata.
- Artilheiro: Joshua Kennedy (Nagoya Grampus), 19.

### 2012

- campeão Sanfrecce Hiroshima (Wikipédia, lista de campeões: Sanfrecce Hiroshima).
- Formato: pontos corridos, 18 clubes, turno e returno.
- ESPN: 225 placares iguais; diferentes: 2012-04-14 Nagoya Grampus 3-1 Consadole Sapporo (ESPN 2-0); 2012-04-14 Shimizu S-Pulse 3-2 Júbilo Iwata (ESPN 2-1); 2012-04-21 Vissel Kobe 3-1 Kashiwa Reysol (ESPN 1-1); 2012-04-21 Sanfrecce Hiroshima 1-1 Nagoya Grampus (ESPN 0-1); 2012-04-21 Kashima Antlers 3-2 Cerezo Osaka (ESPN 1-2); 2012-04-21 Vegalta Sendai 4-0 FC Tokyo (ESPN 1-0); 2012-04-22 Gamba Osaka 3-1 Shimizu S-Pulse (ESPN 2-0); 2012-04-28 Kawasaki Frontale 1-4 Sanfrecce Hiroshima (ESPN 1-1); 2012-05-03 Shimizu S-Pulse 3-0 Kashima Antlers (ESPN 1-0); 2012-05-06 Omiya Ardija 1-0 Gamba Osaka (ESPN 0-0); 2012-05-06 Albirex Niigata 0-2 FC Tokyo (ESPN 0-1); 2012-05-12 Sanfrecce Hiroshima 1-3 Yokohama F. Marinos (ESPN 1-0); 2012-05-12 Shimizu S-Pulse 1-1 Cerezo Osaka (ESPN 0-1); 2012-05-12 Urawa Reds 1-1 Albirex Niigata (ESPN 1-0); 2012-05-19 Albirex Niigata 1-6 Júbilo Iwata (ESPN 1-5); 2012-05-26 Consadole Sapporo 1-3 Sanfrecce Hiroshima (ESPN 0-2); 2012-05-26 Kawasaki Frontale 3-2 Vegalta Sendai (ESPN 1-2); 2012-05-26 Júbilo Iwata 4-0 Omiya Ardija (ESPN 3-0); 2012-05-26 Vissel Kobe 1-2 Kashima Antlers (ESPN 0-2); 2012-05-26 Kashiwa Reysol 2-0 Albirex Niigata (ESPN 1-0); 2012-06-16 Vegalta Sendai 4-1 Consadole Sapporo (ESPN 3-1); 2012-06-16 Kashima Antlers 2-3 Nagoya Grampus (ESPN 1-2); 2012-06-16 Gamba Osaka 1-2 Urawa Reds (ESPN 1-1); 2012-06-16 Cerezo Osaka 1-4 Sanfrecce Hiroshima (ESPN 1-1); 2012-06-23 Consadole Sapporo 0-4 Gamba Osaka (ESPN 0-3); 2012-06-23 Kashiwa Reysol 1-1 Kashima Antlers (ESPN 0-0); 2012-06-23 Nagoya Grampus 2-0 Júbilo Iwata (ESPN 1-0); 2012-06-30 Júbilo Iwata 3-1 FC Tokyo (ESPN 3-0); 2012-06-30 Cerezo Osaka 1-1 Urawa Reds (ESPN 0-1); 2012-06-30 Gamba Osaka 2-6 Kashiwa Reysol (ESPN 2-3); 2012-07-07 FC Tokyo 3-2 Gamba Osaka (ESPN 3-1); 2012-07-14 Shimizu S-Pulse 3-5 Kashiwa Reysol (ESPN 2-1); 2012-07-14 Omiya Ardija 2-2 Vissel Kobe (ESPN 0-1); 2012-07-14 Gamba Osaka 1-2 Yokohama F. Marinos (ESPN 0-1); 2012-07-14 Júbilo Iwata 4-1 Consadole Sapporo (ESPN 3-1); 2012-10-06 Nagoya Grampus 0-0 Omiya Ardija (ESPN 1-0).
- ogol: 306 placares iguais.
- Rebaixados: Vissel Kobe, Gamba Osaka, Consadole Sapporo.
- Artilheiro: Hisato Satō (Sanfrecce Hiroshima), 22.

### 2013

- campeão Sanfrecce Hiroshima (Wikipédia, lista de campeões: Sanfrecce Hiroshima).
- Formato: pontos corridos, 18 clubes, turno e returno.
- ESPN: 306 placares iguais.
- ogol: 306 placares iguais.
- Rebaixados: Shonan Bellmare, Júbilo Iwata, Oita Trinita.
- Artilheiro: Yoshito Ōkubo (Kawasaki Frontale), 26.

### 2014

- campeão Gamba Osaka (Wikipédia, lista de campeões: Gamba Osaka).
- Formato: pontos corridos, 18 clubes, turno e returno.
- ESPN: 304 placares iguais; diferentes: 2014-03-01 Sagan Tosu 5-0 Tokushima Vortis (ESPN 3-0); 2014-10-05 Kashima Antlers 2-3 Gamba Osaka (ESPN 1-3).
- ogol: 306 placares iguais.
- Rebaixados: Omiya Ardija, Cerezo Osaka, Tokushima Vortis.
- Artilheiro: Yoshito Ōkubo (Kawasaki Frontale), 18.

### 2015

- campeão Sanfrecce Hiroshima (Wikipédia, lista de campeões: Sanfrecce Hiroshima).
- Formato: dois turnos de pontos corridos (18 clubes, turno único em cada um); semifinal (jogo único) e final (ida e volta) entre os campeões dos turnos e o melhor da tabela anual.
- ESPN: 153 placares iguais.
- ogol: 308 placares iguais.
- Rebaixados: Matsumoto Yamaga, Shimizu S-Pulse, Montedio Yamagata.
- Artilheiro: Yoshito Ōkubo (Kawasaki Frontale), 23.

### 2016

- campeão Kashima Antlers (Wikipédia, lista de campeões: Kashima Antlers).
- Formato: dois turnos de pontos corridos (18 clubes, turno único em cada um); semifinal (jogo único) e final (ida e volta) entre os campeões dos turnos e o melhor da tabela anual.
- ESPN: 309 placares iguais.
- ogol: 308 placares iguais.
- Rebaixados: Nagoya Grampus, Shonan Bellmare, Avispa Fukuoka.
- Artilheiro: Leandro (Vissel Kobe), 19; Peter Utaka (Sanfrecce Hiroshima), 19.

### 2017

- campeão Kawasaki Frontale (Wikipédia, lista de campeões: Kawasaki Frontale).
- Formato: pontos corridos, 18 clubes, turno e returno.
- ESPN: 306 placares iguais.
- ogol: 306 placares iguais.
- Rebaixados: Ventforet Kofu, Albirex Niigata, Omiya Ardija.
- Artilheiro: Yū Kobayashi (Kawasaki Frontale), 23.

### 2018

- campeão Kawasaki Frontale (Wikipédia, lista de campeões: Kawasaki Frontale).
- Formato: pontos corridos, 18 clubes, turno e returno.
- fora do pacote: 3 jogo(s) da repescagem J1/J2 (entram com a 2ª divisão).
- ESPN: 306 placares iguais.
- ogol: 306 placares iguais.
- Rebaixados: Kashiwa Reysol, V-Varen Nagasaki.
- Artilheiro: Jô (Nagoya Grampus), 24.

### 2019

- campeão Yokohama F. Marinos (Wikipédia, lista de campeões: Yokohama F.&nbsp;Marinos).
- Formato: pontos corridos, 18 clubes, turno e returno.
- fora do pacote: 4 jogo(s) da repescagem J1/J2 (entram com a 2ª divisão).
- ESPN: 306 placares iguais.
- ogol: 306 placares iguais.
- Rebaixados: Matsumoto Yamaga, Júbilo Iwata.
- Artilheiro: Teruhito Nakagawa (Yokohama F. Marinos), 15; Marcos Júnior (Yokohama F. Marinos), 15.

### 2020

- campeão Kawasaki Frontale (Wikipédia, lista de campeões: Kawasaki Frontale).
- Formato: pontos corridos, 18 clubes, turno e returno.
- ESPN: 306 placares iguais.
- ogol: 306 placares iguais.
- Artilheiro: Michael Olunga (Kashiwa Reysol), 28.

### 2021

- campeão Kawasaki Frontale (Wikipédia, lista de campeões: Kawasaki Frontale).
- Formato: pontos corridos, 20 clubes, turno e returno.
- ESPN: 380 placares iguais.
- ogol: 379 placares iguais.
- Rebaixados: Tokushima Vortis, Oita Trinita, Vegalta Sendai, Yokohama FC.
- Artilheiro: Leandro Damião (Kawasaki Frontale), 23; Daizen Maeda (Yokohama F. Marinos), 23.

### 2022

- campeão Yokohama F. Marinos (Wikipédia, lista de campeões: Yokohama F. Marinos).
- Formato: pontos corridos, 18 clubes, turno e returno.
- fora do pacote: 4 jogo(s) da repescagem J1/J2 (entram com a 2ª divisão).
- ESPN: 306 placares iguais.
- ogol: 306 placares iguais.
- Rebaixados: Shimizu S-Pulse, Júbilo Iwata.
- Artilheiro: Thiago Santana (Shimizu S-Pulse), 14.

### 2023

- campeão Vissel Kobe (Wikipédia, lista de campeões: Vissel Kobe).
- Formato: pontos corridos, 18 clubes, turno e returno.
- ESPN: 306 placares iguais.
- ogol: 306 placares iguais.
- Rebaixados: Yokohama FC.
- Artilheiro: Anderson Lopes (Yokohama F. Marinos), 22; Yuya Osako (Vissel Kobe), 22.

### 2024

- campeão Vissel Kobe (Wikipédia, lista de campeões: Vissel Kobe).
- Formato: pontos corridos, 20 clubes, turno e returno.
- ESPN: 380 placares iguais.
- ogol: 380 placares iguais.
- Rebaixados: Júbilo Iwata, Consadole Sapporo, Sagan Tosu.
- Artilheiro: Anderson Lopes (Yokohama F. Marinos), 24.

### 2025

- campeão Kashima Antlers (Wikipédia, lista de campeões: Kashima Antlers).
- Formato: pontos corridos, 20 clubes, turno e returno.
- ESPN: 380 placares iguais.
- ogol: 380 placares iguais.
- Rebaixados: Yokohama FC, Shonan Bellmare, Albirex Niigata.
- Artilheiro: Léo Ceará (Kashima Antlers), 21.
