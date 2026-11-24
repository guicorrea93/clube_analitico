# Campeonato Sul-Coreano (1ª divisão) — coleta de dados

Gerado por `python coleta/kor-1/importar.py`. Pacote em `data/coleta/kor-1/pacote/`.

**Edições:** 43, uma por título, de 1983 a 2025, como na lista de campeões da K League, da RSSSF (`skorchamp.html`) e da
Wikipédia em inglês (List of South Korean football champions): K League (Super League em 1983-1986) e, de 2013 em diante,
K League 1 (K League Classic até 2017). 2026 entra quando acabar. A liga semiprofissional de antes de 1983 não entra
(era outra competição, de clubes de empresa e do Exército; a K League conta a sua história a partir de 1983).

**Fora do pacote:** a copa da liga (아디다스컵, 리그컵 etc.; o patrocínio pôs "copa" no nome da própria liga em 1996-1999, mas
essas são a liga), a repescagem contra a K League 2 (승강 플레이오프, 2013 em diante: entra com a 2ª divisão), a Copa da
Coreia (FA Cup) e a Supercopa.

**Fontes:** portal de dados oficial da K League (portal.kleague.com, acesso de convidado): lista de jogos de cada ano
(`data/coleta/kor-1/portal/calendario_<ano>.json`; de 2013 em diante a lista vem do site oficial, www.kleague.com, com
fase e rodada) e o boletim de cada jogo (data, hora, estádio, público, árbitro, autores dos gols com minuto, pênalti, gol
contra, cartões, disputa de pênaltis), no cache `data/cache/kleague-asia/jogos/`; site oficial da K League
(www.kleague.com): linha do tempo de cada jogo de 2013 em diante, em coreano e em inglês (`data/cache/kleague-asia/oficial/`:
conferência do placar e nome dos jogadores em inglês) e a classificação final oficial de 2013 em diante
(`data/coleta/kor-1/oficial/tabela_<ano>.json`); RSSSF (uma página por ano e a `skorhist.html`, com a tabela de cada ano de
1983 a 2009, em `data/coleta/kor-1/rsssf/`: conferência dos placares e das tabelas); Wikipédia em inglês (lista de campeões e
lista de artilheiros, "K League Top Scorer Award", em `data/coleta/kor-1/wikipedia/`) e em coreano (tabela e resultados de
cada ano, consultada nas divergências); ogol (calendário de 2008 a 2025, para os escudos e a conferência:
`data/coleta/kor-1/ogol/` e `data/cache/ogol-kor-1/`).

**Clubes:** 25. Um clube por código do portal oficial (K01, K04...), que é o mesmo nas mudanças de nome e de cidade, como
a própria K League conta: Yukong Elephants/Bucheon SK = Jeju United; Daewoo Royals = Busan IPark; Ilhwa Chunma = Seongnam
FC; Lucky-Goldstar/LG Cheetahs = FC Seoul; Hyundai Horang-i = Ulsan Hyundai; POSCO = Pohang Steelers. Os times militares
têm códigos diferentes e ficam separados: Sangmu (1985), Gwangju Sangmu (2003-2010), Sangju Sangmu (2011-2020) e Gimcheon
Sangmu (2022 em diante). O Chonbuk Buffalo (1994) não é o Jeonbuk Hyundai. Nome de exibição: o de hoje, como o ogol escreve.
Os nomes de cada fonte estão no `nomes_fonte` do `clubes.csv` (regras em `coleta/kor-1/clubes_kor.py`).

**Regras:** placar oficial, com a prorrogação. O total de gols do boletim do portal não conta o gol contra (em nenhuma
época): o placar é a soma dos gols do boletim, conferida com o total (mais os gols contra), com o site oficial (2013 em
diante), com a RSSSF e com o ogol; quando não batem, vale o que as outras fontes e as tabelas confirmam, e os autores dos
gols do jogo ficam de fora. Pontos: 2 por vitória em 1983 e 1985-1992; em 1984, 3 pela vitória, 2 pelo empate com gols e
1 pelo 0-0; em 1993, empate decidido nos pênaltis (4 pela vitória, 2 pela vitória nos pênaltis, 1 pela derrota nos
pênaltis); 3/1/0 em 1994-1997 e de 2001 em diante; em 1998-1999, prorrogação com gol de ouro e pênaltis (3 no tempo normal,
2 na prorrogação, 1 nos pênaltis); em 2000, 3 no tempo normal ou na prorrogação e 1 nos pênaltis. Fases: dois turnos em
1984, 1986, 1995, 1996 e 2004-2006; decisão do título entre os campeões dos turnos (1984, 1986, 1995, 1996) ou playoff
(1998-2000, 2004-2011); de 2012 em diante a liga se divide em grupo do título (A) e grupo de baixo (B) nas últimas rodadas,
com os pontos acumulados (fase única "Liga", como no Escocês; a observação do jogo diz o grupo). Classificação final: de
2013 em diante, a oficial da K League; antes, a soma dos jogos, com o campeão e o vice da decisão em 1º e 2º, depois os
eliminados do playoff pela fase em que caíram e o resto pela tabela (os números de jogos, vitórias, gols e pontos são só da
liga, sem playoff nem final, como a tabela da RSSSF). Rebaixado: de 2012 em diante, o clube que não está na edição
seguinte (antes de 2012 não havia rebaixamento). Nome dos jogadores: coreanos pela grafia oficial em inglês do site da K
League quando há (2013 em diante: "Lee Dong-gook") e, se não, pela romanização revisada do hangul do portal ("Jeong
Hae-won"); estrangeiros pelo nome de jogo, tirado do nome em inglês do site oficial (o hangul é o nome de jogo: "호벨손"
Roberson); estrangeiros de antes de 2013 sem nome em inglês ficam com o hangul romanizado (aproximação). Cartões de técnico e
comissão (sem número de camisa) ficam de fora. Artilheiro: o da lista da Wikipédia em inglês (contagem oficial),
conferido com a soma dos gols dos boletins.

**Conferência:** placares com a RSSSF (1983-2010; a RSSSF não tem os jogos de 1997, 2011, 2012 e 2025) e o ogol (2008-2025); a
tabela da liga com a da RSSSF (jogos, gols pró, gols contra e pontos de cada clube); de 2013 em diante, a tabela oficial da K
League contra a soma dos jogos; campeão e vice com a Wikipédia. Nas divergências com a RSSSF a Wikipédia em coreano decidiu.

**Edições sem jogos:** nenhuma.

**Edições com jogos incompletos:** nenhuma: todos os jogos da 1ª divisão estão no portal. 23 jogos ficaram sem os autores
dos gols (o boletim não fecha com o placar; lista em cada edição).

**Resumo:** 7163 jogos, 17984 gols com autor, 24627 cartões.

| Temporada | Clubes | Jogos | Gols | c/ autor | Tabela RSSSF (linhas iguais) | Campeão | Classificação |
|---|---|---|---|---|---|---|---|
| 1983 | 5 | 40 | 107 | 107 | 5 de 5 | Hallelujah FC | soma dos jogos |
| 1984 | 8 | 114 | 304 | 301 | 8 de 8 | Busan IPark | soma dos jogos da liga; campeão e vice pela decisão, depois os eliminados por fase e a tabela |
| 1985 | 8 | 84 | 189 | 184 | 8 de 8 | FC Seoul | soma dos jogos |
| 1986 | 6 | 62 | 143 | 139 | 6 de 6 | Pohang Steelers | soma dos jogos da liga; campeão e vice pela decisão, depois os eliminados por fase e a tabela |
| 1987 | 5 | 80 | 199 | 199 | 4 de 5 | Busan IPark | soma dos jogos |
| 1988 | 5 | 60 | 133 | 133 | 5 de 5 | Pohang Steelers | soma dos jogos |
| 1989 | 6 | 120 | 275 | 268 | 5 de 6 | Jeju United | soma dos jogos |
| 1990 | 6 | 90 | 186 | 181 | 6 de 6 | FC Seoul | soma dos jogos |
| 1991 | 6 | 120 | 269 | 264 | 5 de 6 | Busan IPark | soma dos jogos |
| 1992 | 6 | 90 | 186 | 186 | 6 de 6 | Pohang Steelers | soma dos jogos |
| 1993 | 6 | 90 | 166 | 157 | 6 de 6 | Seongnam FC | soma dos jogos |
| 1994 | 7 | 105 | 296 | 296 | 7 de 7 | Seongnam FC | soma dos jogos |
| 1995 | 8 | 115 | 272 | 264 | 8 de 8 | Seongnam FC | soma dos jogos da liga; campeão e vice pela decisão, depois os eliminados por fase e a tabela |
| 1996 | 9 | 146 | 453 | 444 | 9 de 9 | Ulsan Hyundai | soma dos jogos da liga; campeão e vice pela decisão, depois os eliminados por fase e a tabela |
| 1997 | 10 | 90 | 232 | 202 | 9 de 10 | Busan IPark | soma dos jogos |
| 1998 | 10 | 95 | 284 | 284 | 10 de 10 | Suwon Samsung Bluewings | soma dos jogos da liga; campeão e vice pela decisão, depois os eliminados por fase e a tabela |
| 1999 | 10 | 140 | 426 | 422 | 10 de 10 | Suwon Samsung Bluewings | soma dos jogos da liga; campeão e vice pela decisão, depois os eliminados por fase e a tabela |
| 2000 | 10 | 140 | 388 | 388 | 10 de 10 | FC Seoul | soma dos jogos da liga; campeão e vice pela decisão, depois os eliminados por fase e a tabela |
| 2001 | 10 | 135 | 310 | 305 | 10 de 10 | Seongnam FC | soma dos jogos |
| 2002 | 10 | 135 | 331 | 329 | 10 de 10 | Seongnam FC | soma dos jogos |
| 2003 | 12 | 264 | 675 | 675 | 12 de 12 | Seongnam FC | K League (classificação oficial, www.kleague.com) |
| 2004 | 13 | 160 | 299 | 299 | 13 de 13 | Suwon Samsung Bluewings | K League (classificação oficial, www.kleague.com) |
| 2005 | 13 | 160 | 387 | 387 | 13 de 13 | Ulsan Hyundai | K League (classificação oficial, www.kleague.com) |
| 2006 | 14 | 186 | 409 | 409 | 14 de 14 | Seongnam FC | K League (classificação oficial, www.kleague.com) |
| 2007 | 14 | 188 | 437 | 437 | 13 de 14 | Pohang Steelers | K League (classificação oficial, www.kleague.com) |
| 2008 | 14 | 188 | 500 | 500 | 14 de 14 | Suwon Samsung Bluewings | K League (classificação oficial, www.kleague.com) |
| 2009 | 15 | 216 | 564 | 564 | 15 de 15 | Jeonbuk Hyundai Motors | K League (classificação oficial, www.kleague.com) |
| 2010 | 15 | 216 | 619 | 619 | 15 de 15 | FC Seoul | K League (classificação oficial, www.kleague.com) |
| 2011 | 16 | 246 | 669 | 669 | 16 de 16 | Jeonbuk Hyundai Motors | K League (classificação oficial, www.kleague.com) |
| 2012 | 16 | 352 | 896 | 868 | 16 de 16 | FC Seoul | K League (classificação oficial, www.kleague.com) |
| 2013 | 14 | 266 | 677 | 677 | 14 de 14 | Pohang Steelers | K League (classificação oficial, www.kleague.com) |
| 2014 | 12 | 228 | 507 | 507 | 12 de 12 | Jeonbuk Hyundai Motors | K League (classificação oficial, www.kleague.com) |
| 2015 | 12 | 228 | 546 | 546 | 12 de 12 | Jeonbuk Hyundai Motors | K League (classificação oficial, www.kleague.com) |
| 2016 | 12 | 228 | 618 | 618 | 11 de 12 | FC Seoul | K League (classificação oficial, www.kleague.com) |
| 2017 | 12 | 228 | 626 | 626 | 12 de 12 | Jeonbuk Hyundai Motors | K League (classificação oficial, www.kleague.com) |
| 2018 | 12 | 228 | 620 | 620 | 12 de 12 | Jeonbuk Hyundai Motors | K League (classificação oficial, www.kleague.com) |
| 2019 | 12 | 228 | 593 | 593 | 12 de 12 | Jeonbuk Hyundai Motors | K League (classificação oficial, www.kleague.com) |
| 2020 | 12 | 162 | 425 | 425 | 12 de 12 | Jeonbuk Hyundai Motors | K League (classificação oficial, www.kleague.com) |
| 2021 | 12 | 228 | 564 | 561 | 12 de 12 | Jeonbuk Hyundai Motors | K League (classificação oficial, www.kleague.com) |
| 2022 | 12 | 228 | 590 | 590 | 12 de 12 | Ulsan Hyundai | K League (classificação oficial, www.kleague.com) |
| 2023 | 12 | 228 | 567 | 567 | 12 de 12 | Ulsan Hyundai | K League (classificação oficial, www.kleague.com) |
| 2024 | 12 | 228 | 596 | 596 | 12 de 12 | Ulsan Hyundai | K League (classificação oficial, www.kleague.com) |
| 2025 | 12 | 228 | 578 | 578 | 12 de 12 | Jeonbuk Hyundai Motors | K League (classificação oficial, www.kleague.com) |

**Estrangeiros com o nome romanizado do hangul** (197; antes de 2013, sem nome em inglês no site oficial nem autor na RSSSF; aproximação, a conferir): Ruiseu (루이스, 1984-2015); Renseubereugen (렌스베르겐, 1984-1985); Alhatsan (알핫산, 1984); Sejareu (세자르, 1984); Wolsinyo (월신요, 1984); Jinjangsanggon (진장상곤, 1985-1989); Syaheuteu (샤흐트, 1985); Iseuteuban (이스트반, 1990); Mejoi (메조이, 1990); Achel (아첼, 1991); Peurangkeu (프랑크, 1992); Pilrip (필립, 1992-1999); Alrekseu (알렉스, 1993-2021); Ppireseu (삐레스, 1994); Boro (보로, 1994); Hikareudo (히카르도, 1994-2015); Sinuison(syarichepeu) (신의손(샤리체프), 1995-2003); Deuragan (드라간, 1995-2008); Syasya (샤샤, 1995-1996); Deurajen (드라젠, 1996); Beurangko (브랑코, 1996-1999); Rankobichi (란코비치, 1996); Alreksei (알렉세이, 1996); Peteuro (페트로, 1996); Salramsyo (살람쇼, 1996); Konol (코놀, 1997); Ilrichi (일리치, 1997); Ssandeo (싼더, 1997); Abora (아보라, 1997); Seukachenko (스카첸코, 1997); Mikael (미카엘, 1997); Mutamba (무탐바, 1997-1998); Kasonggo (카송고, 1997); Babarade (바바라데, 1997); Tumu (투무, 1997); Baha (바하, 1997-1998); Rui (루이, 1998); Boriseu (보리스, 1998-2003); Yulrian (율리안, 1999); Hojerio (호제리오, 1999-2009); Jolri (졸리, 2000-2001); Santoseu (산토스, 2000-2008); Naemanya (내마냐, 2000); Akinseun (아킨슨, 2001); Arinelsong (아리넬송, 2001); Bitalri (비탈리, 2001); Alren (알렌, 2001); Gaimoto (가이모토, 2001); Miteuro (미트로, 2002); Olribe (올리베, 2002); Reomareu (레오마르, 2002); Dao (다오, 2002); Kkorea (꼬레아, 2002); Batiseuta (바티스타, 2003); Maejono (마에조노, 2003); Reo (레오, 2003-2017); Jon (존, 2003); Hodeurigo (호드리고, 2003-2013); Alpai (알파이, 2004); Keuriseu (크리스, 2004); Ssouja (쏘우자, 2004); Henaudo (헤나우도, 2004); Alran (알란, 2004); Atom (아톰, 2004); Santiago (산티아고, 2004-2005); Pumagalri (푸마갈리, 2004); Tomichi (토미치, 2004); Mareuselro (마르셀로, 2004); Peulrama (플라마, 2004); Hikaldo (히칼도, 2005-2007); Peurangko (프랑코, 2005); Selmireu (셀미르, 2005-2008); Dasilba (다실바, 2005-2006); Agoseu (아고스, 2005); Netto (네또, 2005); Pelrikseu (펠릭스, 2005); Sejio (세지오, 2005); Im Ho (임 호, 2005); Ittamareu (이따마르, 2005-2007); Jjiago (찌아고, 2005); Musa (무사, 2005); Pabeurisio (파브리시오, 2005-2010); Sebaseutian (세바스티안, 2005); Pabio (파비오, 2005-2016); Welringteon (웰링턴, 2005); Milton (밀톤, 2005-2006); Bilra (빌라, 2005); Sandeuro (산드로, 2006-2023); Peurontini (프론티니, 2006); Reandeurong (레안드롱, 2006-2007); Ateu (아트, 2006); Rusiano (루시아노, 2006); Edyu (에듀, 2006); Gabeuriel (가브리엘, 2006-2025); Somalria (소말리아, 2006); Enrikki (엔리끼, 2006); Binisiuseu (비니시우스, 2006); SandeuroC (산드로C, 2006-2007); Neaga (네아가, 2006-2007); Dudu (두두, 2006-2007); Olribera (올리베라, 2006); Nikolra (니콜라, 2006-2007); Bajo (바조, 2006-2010); Denilson (데닐손, 2006-2009); Heopseun (헙슨, 2006); Silba (실바, 2006); Kkabore (까보레, 2007); Pereunando (페르난도, 2007); Maurisio (마우리시오, 2007); Toni (토니, 2007); Syubengkeu (슈벵크, 2007); Kalre (칼레, 2007); Hikaldingyo (히칼딩요, 2007); Ssiel (씨엘, 2007); Beurajilria (브라질리아, 2007-2009); Boreuko (보르코, 2008-2009); Ppajji (빠찌, 2008); Pereira (페레이라, 2008); Heinaldo (헤이날도, 2008); Edeuson (에드손, 2008); Erik (에릭, 2008); Pinggu (핑구, 2008); Jiobani (지오바니, 2008); Areuche (아르체, 2008); Daichi (다이치, 2008); Bautel (바우텔, 2008); Henatto (헤나또, 2008); Alreksandeo (알렉산더, 2008-2009); Chyadi (챠디, 2009); Riweipeong (리웨이펑, 2009-2010); Kebin (케빈, 2009-2022); Hikado (히카도, 2009); Peongsyaoting (펑샤오팅, 2009-2010); Sasya (사샤, 2009-2012); Babel (바벨, 2009); Weseulri (웨슬리, 2009-2017); Seulrabeuko (슬라브코, 2009); Bikera (비케라, 2009); Popobichi (포포비치, 2009); Toda (토다, 2009); Albeseu (알베스, 2009); Koroman (코로만, 2009-2010); Tiago (티아고, 2009-2025); Seuteban (스테반, 2009); Baul (바울, 2009); Wanhouryang (완호우량, 2009); Andereuson (안데르손, 2009); Okkayama (오까야마, 2009-2010); Bageuneo (바그너, 2009-2011); Robeurek (로브렉, 2010-2011); Eseutebejeu (에스테베즈, 2010); Rusio (루시오, 2010-2011); Alre (알레, 2010); Oreutigosa (오르티고사, 2010); Alreksandeuro (알렉산드로, 2010-2012); Kkareumelro (까르멜로, 2010); Neko (네코, 2010); Pelripi (펠리피, 2010); Bekeurichi (베크리치, 2010); Richunyu (리춘유, 2010); Mareusio (마르시오, 2010); Dakahara (다카하라, 2010); Beuruno (브루노, 2010); Geinrihi (게인리히, 2011); Kapaje (카파제, 2011); Diego (디에고, 2011); Jakeumichi (자크미치, 2011-2012); Kkirino (끼리노, 2011); Oeseul (외슬, 2011); Baiya (바이야, 2011); Ebeljjingyo (에벨찡요, 2011-2012); Mateuseu (마테우스, 2011-2025); Elrio (엘리오, 2011); Edel (에델, 2011-2012); Saimeon (사이먼, 2012); EbeltonC (에벨톤C, 2012); Yobanchichi (요반치치, 2012); Bogeudan (보그단, 2012); Nando (난도, 2012); Maekkai (맥카이, 2012); Aki (아키, 2012); Ppaulro (빠울로, 2012); Teha (테하, 2012); Jael (자엘, 2012); Reonareudo (레오나르도, 2012-2022); Mareukeseu (마르케스, 2012); Kaio (카이오, 2014-2025); Adeuriano (아드리아노, 2015-2018); Tomi (토미, 2016-2017); Ebandeuro (에반드로, 2017-2018); Henri (헨리, 2020-2024); Guseutabo (구스타보, 2020-2023); Heiseu (헤이스, 2021-2025); Tomaseu (토마스, 2023-2025); Yago (야고, 2024); Rukaseu (루카스, 2024); Ruan (루안, 2025).

## Conferência e correções, edição a edição

### 1983

- campeão Hallelujah FC (igual à Wikipédia).
- Formato: pontos corridos, 5 clubes.
- RSSSF: 38 placares iguais.
- Artilheiro (Wikipédia): Park Yoon-ki (Jeju United), 9.

### 1984

- campeão Busan IPark (igual à Wikipédia).
- Formato: dois turnos de pontos corridos (8 clubes) e decisão do título entre os campeões dos turnos.
- Placar do boletim conferido: 1984-04-29 Jeju United x Ulsan Hyundai: total do boletim 2-1, gols do boletim 1-1, outra fonte 2-1 (vale 2-1); 1984-10-27 Jeju United x FC Seoul: total do boletim 1-1, gols do boletim 2-1 (vale este, como a RSSSF/ogol).
- Jogos sem os autores dos gols (o boletim não fecha com o placar): Jeju United 2-1 Ulsan Hyundai: 1+1 autores no boletim.
- RSSSF: 114 placares iguais.
- Artilheiro (Wikipédia): Baek Jong-chul (Ulsan Hyundai), 16.
- Artilheiro: diferença com a soma dos boletins (Wikipédia: Baek Jong-chul (Ulsan Hyundai) 16; soma dos boletins: Baek Jong-cheol (Ulsan Hyundai) 15); vale a Wikipédia.

### 1985

- campeão FC Seoul (igual à Wikipédia).
- Formato: pontos corridos, 8 clubes.
- Placar do boletim conferido: 1985-04-14 Hallelujah FC x Jeju United: total do boletim 2-3, gols do boletim 1-3, outra fonte 2-3 (vale 2-3); 1985-04-27 Ulsan Hyundai x Pohang Steelers: total do boletim 0-2, gols do boletim 1-2 (vale este, como a RSSSF/ogol); 1985-06-23 Hallelujah FC x FC Seoul: total do boletim 0-1, gols do boletim 0-2 (vale este, como a RSSSF/ogol); 1985-07-18 Hallelujah FC x Sangmu: total do boletim 1-3, gols do boletim 2-3 (vale este, como a RSSSF/ogol).
- Jogos sem os autores dos gols (o boletim não fecha com o placar): Hallelujah FC 2-3 Jeju United: 1+3 autores no boletim.
- RSSSF: 84 placares iguais.
- Artilheiro (Wikipédia): Piyapong Pue-on (FC Seoul), 12.

### 1986

- campeão Pohang Steelers (igual à Wikipédia).
- Formato: dois turnos de pontos corridos (6 clubes) e decisão do título entre os campeões dos turnos.
- Placar do boletim conferido: 1986-04-06 Busan IPark x FC Seoul: total do boletim 0-1, gols do boletim 2-1 (vale este, como a RSSSF/ogol); 1986-04-20 Jeju United x Ulsan Hyundai: total do boletim 1-3, gols do boletim 1-2, outra fonte 1-3 (vale 1-3); 1986-11-08 Hanil Bank x Busan IPark: total do boletim 1-1, gols do boletim 1-2 (vale este, como a RSSSF/ogol).
- Jogos sem os autores dos gols (o boletim não fecha com o placar): Jeju United 1-3 Ulsan Hyundai: 1+2 autores no boletim.
- RSSSF: 61 placares iguais.
- Artilheiro (Wikipédia): Chung Hae-won (Busan IPark), 10.

### 1987

- campeão Busan IPark (igual à Wikipédia).
- Formato: pontos corridos, 5 clubes.
- Tabela: diferenças com a RSSSF: FC Seoul: 32 jogos, 26-55, 21 pontos não está na RSSSF. A Wikipédia em coreano (1987년 K리그) dá os mesmos números daqui para o FC Seoul (Lucky-Goldstar): 7-7-18, 26-55, 21 pontos; a RSSSF tem 56 gols sofridos e um placar diferente (Pohang 2-1 Lucky-Goldstar em 31/10; o portal e a Wikipédia em coreano dão 2-3).
- Placar do boletim conferido: 1987-05-04 Pohang Steelers x Ulsan Hyundai: total do boletim 0-3, gols do boletim 2-3 (vale este, como a RSSSF/ogol); 1987-05-09 Ulsan Hyundai x FC Seoul: total do boletim 0-1, gols do boletim 1-1 (vale este, como a RSSSF/ogol); 1987-09-05 Busan IPark x Jeju United: total do boletim 1-2, gols do boletim 2-2 (vale este, como a RSSSF/ogol); 1987-10-10 FC Seoul x Pohang Steelers: total do boletim 1-5, gols do boletim 1-7 (vale este, como a RSSSF/ogol); 1987-10-11 Jeju United x Busan IPark: total do boletim 2-1, gols do boletim 2-2 (vale este, como a RSSSF/ogol).
- RSSSF: 75 placares iguais; diferentes: 1987-10-31 Pohang Steelers 2-3 FC Seoul (RSSSF 2-1).
- Artilheiro (Wikipédia): Choi Sang-kook (Pohang Steelers), 15.

### 1988

- campeão Pohang Steelers (igual à Wikipédia).
- Formato: pontos corridos, 5 clubes.
- Placar do boletim conferido: 1988-09-03 Jeju United x FC Seoul: total do boletim 0-2, gols do boletim 1-2 (vale este, como a RSSSF/ogol); 1988-11-12 FC Seoul x Busan IPark: total do boletim 3-0, gols do boletim 3-1 (vale este, como a RSSSF/ogol); 1988-11-12 Jeju United x Pohang Steelers: total do boletim 2-0, gols do boletim 2-1 (vale este, como a RSSSF/ogol).
- RSSSF: 59 placares iguais.
- Artilheiro (Wikipédia): Lee Kee-keun (Pohang Steelers), 12.

### 1989

- campeão Jeju United (igual à Wikipédia).
- Formato: pontos corridos, 6 clubes.
- Tabela: diferenças com a RSSSF: FC Seoul: pontos 47 aqui, 42 na RSSSF (jogos e gols iguais). A Wikipédia em coreano (1989년 K리그) dá 47 pontos ao FC Seoul (Lucky-Goldstar), como aqui (15 vitórias e 17 empates); os 42 da RSSSF são erro de conta.
- Placar do boletim conferido: 1989-03-25 Jeju United x Pohang Steelers: total do boletim 0-2, gols do boletim 1-2 (vale este, como a RSSSF/ogol); 1989-04-09 Ulsan Hyundai x Seongnam FC: total do boletim 2-0, gols do boletim 2-1, sem outra fonte (vale 2-1: a tabela da RSSSF fecha com ele); 1989-06-30 Busan IPark x FC Seoul: total do boletim 0-1, gols do boletim 1-1 (vale este, como a RSSSF/ogol); 1989-08-15 Seongnam FC x FC Seoul: total do boletim 2-2, gols do boletim 2-1, outra fonte 2-2 (vale 2-2); 1989-10-01 Busan IPark x FC Seoul: total do boletim 0-2, gols do boletim 1-2 (vale este, como a RSSSF/ogol); 1989-10-18 Pohang Steelers x Ulsan Hyundai: total do boletim 2-1, gols do boletim 1-1, outra fonte 2-1 (vale 2-1); 1989-10-21 Ulsan Hyundai x Pohang Steelers: total do boletim 3-3, gols do boletim 3-4 (vale este, como a RSSSF/ogol).
- Jogos sem os autores dos gols (o boletim não fecha com o placar): Seongnam FC 2-2 FC Seoul: 2+1 autores no boletim; Pohang Steelers 2-1 Ulsan Hyundai: 1+1 autores no boletim.
- RSSSF: 119 placares iguais.
- Artilheiro (Wikipédia): Cho Keung-yeon (Pohang Steelers), 20.

### 1990

- campeão FC Seoul (igual à Wikipédia).
- Formato: pontos corridos, 6 clubes.
- Placar do boletim conferido: 1990-05-23 FC Seoul x Pohang Steelers: total do boletim 1-0, gols do boletim 1-1 (vale este, como a RSSSF/ogol); 1990-05-30 Jeju United x Seongnam FC: total do boletim 2-3, gols do boletim 1-3, outra fonte 2-3 (vale 2-3); 1990-06-02 Ulsan Hyundai x FC Seoul: total do boletim 0-3, gols do boletim 2-3 (vale este, como a RSSSF/ogol); 1990-07-14 Pohang Steelers x FC Seoul: total do boletim 1-2, gols do boletim 3-2 (vale este, como a RSSSF/ogol); 1990-08-18 Ulsan Hyundai x Pohang Steelers: total do boletim 1-0, gols do boletim 1-1 (vale este, como a RSSSF/ogol); 1990-10-17 Busan IPark x Ulsan Hyundai: total do boletim 2-2, gols do boletim 2-3 (vale este, como a RSSSF/ogol).
- Jogos sem os autores dos gols (o boletim não fecha com o placar): Jeju United 2-3 Seongnam FC: 1+3 autores no boletim.
- RSSSF: 89 placares iguais.
- Artilheiro (Wikipédia): Yoon Sang-chul (FC Seoul), 12.

### 1991

- campeão Busan IPark (igual à Wikipédia).
- Formato: pontos corridos, 6 clubes.
- Tabela: diferenças com a RSSSF: Jeju United: 40 jogos, 38-40, 37 pontos não está na RSSSF. A Wikipédia em coreano (1991년 K리그) dá ao Jeju United (Yukong) 10-17-13, 38-40, 37 pontos, como aqui.
- Placar do boletim conferido: 1991-05-11 Ulsan Hyundai x FC Seoul: total do boletim 3-2, gols do boletim 3-1, outra fonte 3-2 (vale 3-2).
- Jogos sem os autores dos gols (o boletim não fecha com o placar): Ulsan Hyundai 3-2 FC Seoul: 3+1 autores no boletim.
- RSSSF: 120 placares iguais.
- Artilheiro (Wikipédia): Lee Kee-keun (Pohang Steelers), 16.

### 1992

- campeão Pohang Steelers (igual à Wikipédia).
- Formato: pontos corridos, 6 clubes.
- Placar do boletim conferido: 1992-11-11 FC Seoul x Jeju United: total do boletim 0-1, gols do boletim 1-1 (vale este, como a RSSSF/ogol); 1992-11-21 FC Seoul x Pohang Steelers: total do boletim 1-1, gols do boletim 1-2 (vale este, como a RSSSF/ogol).
- RSSSF: 88 placares iguais.
- Artilheiro (Wikipédia): Lim Keun-jae (FC Seoul), 10.

### 1993

- campeão Seongnam FC (igual à Wikipédia).
- Formato: pontos corridos, 6 clubes.
- Placar do boletim conferido: 1993-08-07 Busan IPark x Pohang Steelers: total do boletim 1-1, gols do boletim 1-0, outra fonte 1-1 (vale 1-1); 1993-08-28 Busan IPark x Seongnam FC: total do boletim 0-2, gols do boletim 0-1, outra fonte 0-2 (vale 0-2); 1993-09-08 Jeju United x Pohang Steelers: total do boletim 0-0, gols do boletim 0-2 (vale este, como a RSSSF/ogol); 1993-09-14 Busan IPark x Jeju United: total do boletim 2-3, gols do boletim 1-3, outra fonte 2-3 (vale 2-3).
- Jogos sem os autores dos gols (o boletim não fecha com o placar): Busan IPark 1-1 Pohang Steelers: 1+0 autores no boletim; Busan IPark 0-2 Seongnam FC: 0+1 autores no boletim; Busan IPark 2-3 Jeju United: 1+3 autores no boletim.
- RSSSF: 89 placares iguais.
- Artilheiro (Wikipédia): Cha Sang-hae (Pohang Steelers), 10.
- Artilheiro: diferença com a soma dos boletins (Wikipédia: Cha Sang-hae (Pohang Steelers) 10; soma dos boletins: Yoon Sang-cheol (FC Seoul) 9; Cha Sang-hae (Pohang Steelers) 9); vale a Wikipédia.

### 1994

- campeão Seongnam FC (igual à Wikipédia).
- Formato: pontos corridos, 7 clubes.
- Placar do boletim conferido: 1994-04-13 Ulsan Hyundai x Chonbuk Buffalo: total do boletim 2-1, gols do boletim 3-1 (vale este, como a RSSSF/ogol); 1994-07-30 Ulsan Hyundai x Chonbuk Buffalo: total do boletim 0-1, gols do boletim 1-1 (vale este, como a RSSSF/ogol); 1994-08-13 Seongnam FC x Busan IPark: total do boletim 2-2, gols do boletim 3-2 (vale este, como a RSSSF/ogol); 1994-09-24 Chonbuk Buffalo x Jeju United: total do boletim 1-1, gols do boletim 1-2 (vale este, como a RSSSF/ogol).
- RSSSF: 103 placares iguais.
- Artilheiro (Wikipédia): Yoon Sang-chul (FC Seoul), 21.

### 1995

- campeão Seongnam FC (igual à Wikipédia).
- Formato: dois turnos de pontos corridos (8 clubes) e decisão do título entre os campeões dos turnos.
- Placar do boletim conferido: 1995-05-10 Ulsan Hyundai x FC Seoul: total do boletim 4-1, gols do boletim 3-1, outra fonte 4-1 (vale 4-1); 1995-07-26 FC Seoul x Jeju United: total do boletim 1-2, gols do boletim 1-1, outra fonte 1-2 (vale 1-2).
- Jogos sem os autores dos gols (o boletim não fecha com o placar): Ulsan Hyundai 4-1 FC Seoul: 3+1 autores no boletim; FC Seoul 1-2 Jeju United: 1+1 autores no boletim.
- RSSSF: 108 placares iguais.
- Artilheiro (Wikipédia): Roh Sang-rae (Jeonnam Dragons), 15.

### 1996

- campeão Ulsan Hyundai (igual à Wikipédia).
- Formato: dois turnos de pontos corridos (9 clubes) e decisão do título entre os campeões dos turnos.
- Placar do boletim conferido: 1996-07-28 Jeju United x Suwon Samsung Bluewings: total do boletim 2-4, gols do boletim 2-3, outra fonte 2-4 (vale 2-4).
- Jogos sem os autores dos gols (o boletim não fecha com o placar): Jeju United 2-4 Suwon Samsung Bluewings: 2+3 autores no boletim.
- RSSSF: 142 placares iguais.
- Artilheiro (Wikipédia): Shin Tae-yong (Seongnam FC), 18.

### 1997

- campeão Busan IPark (igual à Wikipédia).
- Formato: pontos corridos, 10 clubes.
- Tabela: diferenças com a RSSSF: Jeju United: 18 jogos, 19-36, 11 pontos não está na RSSSF. Sem explicação: a RSSSF dá ao Jeju United (Puchon SK) 18-35 e aqui são 19-36 (mesmos pontos); a RSSSF não tem os jogos de 1997 e a Wikipédia em coreano não tem a tabela; os outros 9 clubes fecham.
- Placar do boletim conferido: 1997-05-11 Daejeon Hana Citizen x Busan IPark: total do boletim 0-2, gols do boletim 0-3, sem outra fonte (vale 0-3: a tabela da RSSSF fecha com ele); 1997-05-18 FC Seoul x Jeonnam Dragons: total do boletim 2-2, gols do boletim 1-2, sem outra fonte (vale 2-2); 1997-06-22 FC Seoul x Pohang Steelers: total do boletim 2-2, gols do boletim 1-2, sem outra fonte (vale 2-2); 1997-06-22 Daejeon Hana Citizen x Ulsan Hyundai: total do boletim 2-2, gols do boletim 2-1, sem outra fonte (vale 2-2); 1997-08-16 FC Seoul x Jeju United: total do boletim 2-2, gols do boletim 1-2, sem outra fonte (vale 2-2); 1997-09-27 Pohang Steelers x Suwon Samsung Bluewings: total do boletim 2-2, gols do boletim 1-2, sem outra fonte (vale 2-2); 1997-09-27 Ulsan Hyundai x Seongnam FC: total do boletim 4-2, gols do boletim 4-1, sem outra fonte (vale 4-2); 1997-10-12 Suwon Samsung Bluewings x Ulsan Hyundai: total do boletim 2-2, gols do boletim 1-2, sem outra fonte (vale 2-2).
- Jogos sem os autores dos gols (o boletim não fecha com o placar): FC Seoul 2-2 Jeonnam Dragons: 1+2 autores no boletim; FC Seoul 2-2 Pohang Steelers: 1+2 autores no boletim; Daejeon Hana Citizen 2-2 Ulsan Hyundai: 2+1 autores no boletim; FC Seoul 2-2 Jeju United: 1+2 autores no boletim; Pohang Steelers 2-2 Suwon Samsung Bluewings: 1+2 autores no boletim; Ulsan Hyundai 4-2 Seongnam FC: 4+1 autores no boletim; Suwon Samsung Bluewings 2-2 Ulsan Hyundai: 1+2 autores no boletim.
- Artilheiro (Wikipédia): Kim Hyun-seok (Ulsan Hyundai), 9.
- Artilheiro: diferença com a soma dos boletins (Wikipédia: Kim Hyun-seok (Ulsan Hyundai) 9; soma dos boletins: Radivoje Manic (Busan IPark) 7); vale a Wikipédia.

### 1998

- campeão Suwon Samsung Bluewings (igual à Wikipédia).
- Formato: pontos corridos (10 clubes) e playoff do título.
- Placar do boletim conferido: 1998-09-19 Jeonnam Dragons x Jeonbuk Hyundai Motors: total do boletim 0-0, gols do boletim 1-0 (vale este, como a RSSSF/ogol); 1998-10-10 Busan IPark x Seongnam FC: total do boletim 2-2, gols do boletim 3-2 (vale este, como a RSSSF/ogol); 1998-10-21 Pohang Steelers x Ulsan Hyundai: total do boletim 2-2, gols do boletim 3-2 (vale este, como a RSSSF/ogol).
- RSSSF: 94 placares iguais.
- Artilheiro (Wikipédia): Yoo Sang-chul (Ulsan Hyundai), 14.

### 1999

- campeão Suwon Samsung Bluewings (igual à Wikipédia).
- Formato: pontos corridos (10 clubes) e playoff do título.
- Placar do boletim conferido: 1999-07-07 Busan IPark x Ulsan Hyundai: total do boletim 4-0, gols do boletim 3-0, outra fonte 4-0 (vale 4-0).
- Jogos sem os autores dos gols (o boletim não fecha com o placar): Busan IPark 4-0 Ulsan Hyundai: 3+0 autores no boletim.
- RSSSF: 112 placares iguais.
- Artilheiro (Wikipédia): Saša Drakulić (Suwon Samsung Bluewings), 18.
- Artilheiro: diferença com a soma dos boletins (Wikipédia: Saša Drakulić (Suwon Samsung Bluewings) 18; soma dos boletins: Sasa Drakulic (Suwon Samsung Bluewings) 17); vale a Wikipédia.

### 2000

- campeão FC Seoul (igual à Wikipédia).
- Formato: pontos corridos (10 clubes) e playoff do título.
- RSSSF: 125 placares iguais.
- Artilheiro (Wikipédia): Kim Do-hoon (Jeonbuk Hyundai Motors), 12.

### 2001

- campeão Seongnam FC (igual à Wikipédia).
- Formato: pontos corridos, 10 clubes.
- Placar do boletim conferido: 2001-08-01 Jeonnam Dragons x Jeju United: total do boletim 3-2, gols do boletim 2-2, sem outra fonte (vale 3-2).
- Jogos sem os autores dos gols (o boletim não fecha com o placar): Jeonnam Dragons 3-2 Jeju United: 2+2 autores no boletim.
- RSSSF: 54 placares iguais; diferentes: 2001-09-02 FC Seoul 2-1 Jeonbuk Hyundai Motors (RSSSF 1-0).
- Artilheiro (Wikipédia): Sandro Cardoso (Suwon Samsung Bluewings), 13.

### 2002

- campeão Seongnam FC (igual à Wikipédia).
- Formato: pontos corridos, 10 clubes.
- Placar do boletim conferido: 2002-11-13 Jeonnam Dragons x Jeju United: total do boletim 0-2, gols do boletim 0-1, outra fonte 0-2 (vale 0-2).
- Jogos sem os autores dos gols (o boletim não fecha com o placar): Jeonnam Dragons 0-2 Jeju United: 0+1 autores no boletim.
- RSSSF: 130 placares iguais.
- Artilheiro (Wikipédia): Edmilson (Jeonbuk Hyundai Motors), 14.

### 2003

- campeão Seongnam FC (igual à Wikipédia).
- Formato: pontos corridos, 12 clubes.
- Placar do boletim conferido: 2003-03-23 Daegu FC x Suwon Samsung Bluewings: total do boletim 0-0, gols do boletim 0-1 (vale este, como a RSSSF/ogol).
- RSSSF: 220 placares iguais.
- Artilheiro (Wikipédia): Kim Do-hoon (Seongnam FC), 28.

### 2004

- campeão Suwon Samsung Bluewings (igual à Wikipédia).
- Formato: dois turnos de pontos corridos (13 clubes) e decisão do título em playoff.
- RSSSF: 136 placares iguais.
- Artilheiro (Wikipédia): Mota (Jeonnam Dragons), 14.

### 2005

- campeão Ulsan Hyundai (igual à Wikipédia).
- Formato: dois turnos de pontos corridos (13 clubes) e decisão do título em playoff.
- RSSSF: 136 placares iguais.
- 1 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Artilheiro (Wikipédia): Leandro Machado (Ulsan Hyundai), 13.
- Artilheiro: diferença com a soma dos boletins (Wikipédia: Leandro Machado (Ulsan Hyundai) 13; soma dos boletins: Park Ju-yeong (FC Seoul) 12); vale a Wikipédia.

### 2006

- campeão Seongnam FC (igual à Wikipédia).
- Formato: dois turnos de pontos corridos (14 clubes) e decisão do título em playoff.
- RSSSF: 158 placares iguais.
- 8 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Artilheiro (Wikipédia): Woo Sung-yong (Seongnam FC), 16.
- Artilheiro: diferença com a soma dos boletins (Wikipédia: Woo Sung-yong (Seongnam FC) 16; soma dos boletins: Woo Seong-yong (Seongnam FC) 15); vale a Wikipédia.

### 2007

- campeão Pohang Steelers (igual à Wikipédia).
- Formato: pontos corridos (14 clubes) e playoff do título.
- Tabela: diferenças com a RSSSF: Jeju United: 26 jogos, 27-35, 30 pontos não está na RSSSF. Erro de digitação da skorhist.html: 27-53 para o Jeju United; a página de 2007 da RSSSF dá 27-35, como aqui e como a tabela oficial da K League.
- RSSSF: 148 placares iguais.
- 3 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Artilheiro (Wikipédia): Caboré (Gyeongnam FC), 17.

### 2008

- campeão Suwon Samsung Bluewings (igual à Wikipédia).
- Formato: pontos corridos (14 clubes) e playoff do título.
- RSSSF: 150 placares iguais.
- ogol: 181 placares iguais.
- 4 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Artilheiro (Wikipédia): Dudu (Seongnam FC), 15.

### 2009

- campeão Jeonbuk Hyundai Motors (igual à Wikipédia).
- Formato: pontos corridos (15 clubes) e playoff do título.
- RSSSF: 174 placares iguais.
- ogol: 215 placares iguais; diferentes: 2009-09-12 Busan IPark 1-2 Seongnam FC (ogol 1-3).
- 13 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Artilheiro (Wikipédia): Lee Dong-gook (Jeonbuk Hyundai Motors), 20.

### 2010

- campeão FC Seoul (igual à Wikipédia).
- Formato: pontos corridos (15 clubes) e playoff do título.
- RSSSF: 188 placares iguais.
- ogol: 216 placares iguais.
- 6 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Artilheiro (Wikipédia): Yoo Byung-soo (Incheon United), 22.

### 2011

- campeão Jeonbuk Hyundai Motors (igual à Wikipédia).
- Formato: pontos corridos (16 clubes) e playoff do título.
- RSSSF: 6 placares iguais.
- ogol: 243 placares iguais; diferentes: 2011-04-03 Gangwon FC 0-3 Daejeon Hana Citizen (ogol 0-2).
- 9 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Artilheiro (Wikipédia): Dejan Damjanović (FC Seoul), 23.

### 2012

- campeão FC Seoul (igual à Wikipédia).
- Formato: pontos corridos (16 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados.
- Placar do boletim conferido: 2012-10-27 Jeju United x Busan IPark: total do boletim 1-1, gols do boletim 2-1 (vale este, como a RSSSF/ogol).
- ogol: 331 placares iguais.
- 10 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Rebaixados: Gwangju FC, Sangju Sangmu.
- Artilheiro (Wikipédia): Dejan Damjanović (FC Seoul), 31.

### 2013

- campeão Pohang Steelers (igual à Wikipédia).
- Formato: pontos corridos (14 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados.
- RSSSF: 266 placares iguais.
- ogol: 266 placares iguais.
- 10 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Rebaixados: Gangwon FC, Daegu FC, Daejeon Hana Citizen.
- Artilheiro (Wikipédia): Dejan Damjanović (FC Seoul), 19.
- Artilheiro: diferença com a soma dos boletins (Wikipédia: Dejan Damjanović (FC Seoul) 19; soma dos boletins: Dejan (FC Seoul) 19; Kim Shin-wook (Ulsan Hyundai) 19); vale a Wikipédia.

### 2014

- campeão Jeonbuk Hyundai Motors (igual à Wikipédia).
- Formato: pontos corridos (12 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados.
- RSSSF: 228 placares iguais.
- ogol: 228 placares iguais.
- 6 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Rebaixados: Gyeongnam FC, Sangju Sangmu.
- Artilheiro (Wikipédia): Júnior Santos (Suwon Samsung Bluewings), 14.

### 2015

- campeão Jeonbuk Hyundai Motors (igual à Wikipédia).
- Formato: pontos corridos (12 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados.
- RSSSF: 190 placares iguais.
- ogol: 228 placares iguais.
- 4 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Rebaixados: Busan IPark, Daejeon Hana Citizen.
- Artilheiro (Wikipédia): Kim Shin-wook (Ulsan Hyundai), 18.

### 2016

- campeão FC Seoul (igual à Wikipédia).
- Formato: pontos corridos (12 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados.
- Tabela: diferenças com a RSSSF: Jeonbuk Hyundai Motors: pontos 69 aqui, 60 na RSSSF (jogos e gols iguais). O Jeonbuk Hyundai perdeu 9 pontos (suborno de árbitros por um olheiro do clube, em 2013): 69 nos jogos, 60 na RSSSF e na tabela oficial (ajuste_pontos -9).
- Pontos tirados ou dados (tabela oficial): Jeonbuk Hyundai Motors -9.
- RSSSF: 190 placares iguais.
- ogol: 227 placares iguais.
- 9 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Rebaixados: Seongnam FC, Suwon FC.
- Artilheiro (Wikipédia): Jung Jo-gook (Gwangju FC), 20.

### 2017

- campeão Jeonbuk Hyundai Motors (igual à Wikipédia).
- Formato: pontos corridos (12 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados.
- RSSSF: 190 placares iguais.
- ogol: 228 placares iguais.
- 5 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Rebaixados: Gwangju FC.
- Artilheiro (Wikipédia): Johnathan Goiano (Suwon Samsung Bluewings), 22.

### 2018

- campeão Jeonbuk Hyundai Motors (igual à Wikipédia).
- Formato: pontos corridos (12 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados.
- RSSSF: 228 placares iguais.
- ogol: 225 placares iguais.
- 1 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Rebaixados: Jeonnam Dragons.
- Artilheiro (Wikipédia): Marcão (Gyeongnam FC), 26.

### 2019

- campeão Jeonbuk Hyundai Motors (igual à Wikipédia).
- Formato: pontos corridos (12 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados.
- RSSSF: 228 placares iguais.
- ogol: 228 placares iguais.
- 6 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Rebaixados: Gyeongnam FC, Jeju United.
- Artilheiro (Wikipédia): Adam Taggart (Suwon Samsung Bluewings), 20.

### 2020

- campeão Jeonbuk Hyundai Motors (igual à Wikipédia).
- Formato: pontos corridos (12 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados.
- RSSSF: 135 placares iguais.
- ogol: 162 placares iguais.
- 18 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Rebaixados: Sangju Sangmu, Busan IPark.
- Artilheiro (Wikipédia): Júnior Negrão (Ulsan Hyundai), 26.

### 2021

- campeão Jeonbuk Hyundai Motors (igual à Wikipédia).
- Formato: pontos corridos (12 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados.
- RSSSF: 190 placares iguais.
- ogol: 227 placares iguais; diferentes: 2021-09-18 Gwangju FC 0-3 Jeju United (ogol 1-1).
- 22 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Rebaixados: Gwangju FC.
- Artilheiro (Wikipédia): Joo Min-kyu (Jeju United), 22.
- Artilheiro: diferença com a soma dos boletins (Wikipédia: Joo Min-kyu (Jeju United) 22; soma dos boletins: Joo Min-kyu (Jeju United) 21); vale a Wikipédia.

### 2022

- campeão Ulsan Hyundai (igual à Wikipédia).
- Formato: pontos corridos (12 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados.
- RSSSF: 228 placares iguais.
- ogol: 228 placares iguais.
- 26 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Rebaixados: Gimcheon Sangmu, Seongnam FC.
- Artilheiro (Wikipédia): Cho Gue-sung (Gimcheon Sangmu), 17.
- Artilheiro: diferença com a soma dos boletins (Wikipédia: Cho Gue-sung (Gimcheon Sangmu) 17; soma dos boletins: Cho Gue-sung (Gimcheon Sangmu) 17; Joo Min-kyu (Jeju United) 17); vale a Wikipédia.

### 2023

- campeão Ulsan Hyundai (igual à Wikipédia).
- Formato: pontos corridos (12 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados.
- RSSSF: 190 placares iguais.
- ogol: 228 placares iguais.
- 52 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Rebaixados: Suwon Samsung Bluewings.
- Artilheiro (Wikipédia): Joo Min-kyu (Ulsan Hyundai), 17.
- Artilheiro: diferença com a soma dos boletins (Wikipédia: Joo Min-kyu (Ulsan Hyundai) 17; soma dos boletins: Tiago (Daejeon Hana Citizen) 17; Joo Min-kyu (Ulsan Hyundai) 17); vale a Wikipédia.

### 2024

- campeão Ulsan Hyundai (igual à Wikipédia).
- Formato: pontos corridos (12 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados.
- RSSSF: 155 placares iguais.
- ogol: 228 placares iguais.
- 51 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Rebaixados: Incheon United.
- Artilheiro (Wikipédia): Stefan Mugoša (Incheon United), 15.

### 2025

- campeão Jeonbuk Hyundai Motors (igual à Wikipédia).
- Formato: pontos corridos (12 clubes) e depois divisão em grupo do título e grupo de baixo, com os pontos acumulados.
- ogol: 228 placares iguais.
- 69 cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.
- Rebaixados: Suwon FC, Daegu FC.
- Artilheiro (Wikipédia): Pablo Sabbag (Suwon FC), 17.
