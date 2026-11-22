# Campeonato Francês (1ª divisão) — coleta de dados

Gerado por `python coleta/fra-1/importar.py`. Pacote em `data/coleta/fra-1/pacote/`.

**Edições:** 88, de 1932/33 a 2025/26 (Division 1 até 2001/02, Ligue 1 depois). Sem 1939/40-1944/45 (campeonatos de guerra, não reconhecidos).

**Total:** 30466 jogos, 84823 gols, 22613 gols com autor (ESPN), 35434 cartões, 76 clubes.

**Fontes:**
- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1932/33-2024/25, menos 1937/38, 1994/95 e 2025/26 (que vêm do ogol) e 1932/33 (errada);
- football-data.co.uk: de 1993/94 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;
- ogol: rodada oficial de cada jogo e conferência de placar; completa as temporadas em que a base falha; calendários guardados em `data/cache/ogol-fra-1/` para os escudos;
- ESPN (liga `fra.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;
- RSSSF: matriz de resultados e tabela final de 1932/33 a 1997/98 (conferência jogo a jogo), tabela final das temporadas seguintes e lista de artilheiros (com o clube);
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições) e lista de campeões (com os gols do artilheiro).

**Regras:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local (Paris). Rebaixado = clube que não está na 1ª divisão na temporada seguinte. 2 pontos por vitória até 1993/94 (menos 1988/89, que teve 3), 3 a partir de 1994/95 (de 1973/74 a 1975/76, 1 ponto a mais para quem marcava 3 gols ou mais no jogo). Placar diferente no ogol, no football-data ou na ESPN numa temporada em que as tabelas publicadas fecham com a base é erro da outra fonte e fica só anotado; quando a outra fonte e a tabela publicada concordam contra a base, o placar é corrigido (CORRECOES, TRIBUNAL e INVERTIDOS em `importar.py`, com o motivo).

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 9, saldo de gols em 72, média de gols em 7); é ele que ordena a classificação rodada a rodada.

| Temporada | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|---|---|
| 1932/33 | engsoccerdata + ogol | 20 | 181 (181) | 718 | 0 | 2 / 0 | Olympique Lillois | — |
| 1933/34 | engsoccerdata + ogol + RSSSF + Wikipédia | 14 | 182 (182) | 820 | 0 | 2 / 0 | Sète | — |
| 1934/35 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 940 | 0 | 2 / 0 | Sochaux | — |
| 1935/36 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 913 | 0 | 2 / 0 | Racing Paris | — |
| 1936/37 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 870 | 0 | 2 / 0 | Olympique de Marseille | — |
| 1937/38 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 793 | 0 | 1 / 1 | Sochaux | — |
| 1938/39 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 766 | 0 | 2 / 0 | Sète | — |
| 1945/46 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1082 | 0 | 0 / 2 | Lille | — |
| 1946/47 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1343 | 0 | 0 / 2 | CO Roubaix-Tourcoing | — |
| 1947/48 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1126 | 0 | 2 / 0 | Olympique de Marseille | — |
| 1948/49 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1138 | 0 | 2 / 0 | Reims | — |
| 1949/50 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1082 | 0 | 2 / 0 | Bordeaux | — |
| 1950/51 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1016 | 0 | 2 / 0 | Nice | — |
| 1951/52 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1051 | 0 | 1 / 1 | Nice | — |
| 1952/53 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 962 | 0 | 1 / 1 | Reims | — |
| 1953/54 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 949 | 0 | 1 / 1 | Lille | — |
| 1954/55 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1052 | 0 | 2 / 0 | Reims | — |
| 1955/56 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1010 | 0 | 1 / 1 | Nice | — |
| 1956/57 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1030 | 0 | 2 / 0 | Saint-Étienne | — |
| 1957/58 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1024 | 0 | 2 / 0 | Reims | — |
| 1958/59 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1257 | 0 | 2 / 0 | Nice | — |
| 1959/60 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1277 | 0 | 2 / 0 | Reims | — |
| 1960/61 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1196 | 0 | 2 / 0 | Monaco | — |
| 1961/62 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1192 | 0 | 2 / 0 | Reims | — |
| 1962/63 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1186 | 0 | 2 / 0 | Monaco | — |
| 1963/64 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 977 | 0 | 1 / 1 | Saint-Étienne | — |
| 1964/65 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 869 | 0 | 2 / 0 | Nantes | — |
| 1965/66 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1190 | 0 | 1 / 1 | Nantes | — |
| 1966/67 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1003 | 0 | 2 / 0 | Saint-Étienne | — |
| 1967/68 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1002 | 0 | 2 / 0 | Saint-Étienne | — |
| 1968/69 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 816 | 0 | 2 / 0 | Saint-Étienne | — |
| 1969/70 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 973 | 0 | 2 / 0 | Saint-Étienne | — |
| 1970/71 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1108 | 0 | 2 / 0 | Olympique de Marseille | — |
| 1971/72 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1087 | 0 | 1 / 1 | Olympique de Marseille | — |
| 1972/73 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1050 | 0 | 2 / 0 | Nantes | — |
| 1973/74 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1151 | 0 | 2 / 0 | Saint-Étienne | — |
| 1974/75 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1075 | 0 | 2 / 0 | Saint-Étienne | Saint-Étienne -5 pontos; Olympique de Marseille -7 pontos; Lyon -2 pontos; Nîmes -4 pontos; Nantes -6 pontos; Bastia -3 pontos; Lens -6 pontos; Metz -2 pontos; Strasbourg -2 pontos; Monaco -11 pontos; Reims -4 pontos; Bordeaux -3 pontos; Lille -2 pontos; Nice -2 pontos; PSG -5 pontos; Troyes AF -1 pontos; Sochaux -2 pontos; Angers -1 pontos; Rennes -1 pontos; Red Star -2 pontos |
| 1975/76 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1145 | 0 | 1 / 1 | Saint-Étienne | Saint-Étienne -3 pontos; Nice -1 pontos; Sochaux -3 pontos; Nantes -3 pontos; Reims -7 pontos; Metz -4 pontos; Nancy -6 pontos; Bastia -4 pontos; Olympique de Marseille -9 pontos; Bordeaux -5 pontos; Nîmes -3 pontos; Valenciennes -2 pontos; Lille -5 pontos; PSG -4 pontos; Lens -6 pontos; Lyon -3 pontos; Troyes AF -2 pontos; Monaco -5 pontos; Avignon -2 pontos |
| 1976/77 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1125 | 0 | 2 / 0 | Nantes | — |
| 1977/78 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1135 | 0 | 2 / 0 | Monaco | — |
| 1978/79 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1141 | 0 | 2 / 0 | Strasbourg | — |
| 1979/80 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1073 | 0 | 1 / 1 | Nantes | — |
| 1980/81 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1064 | 0 | 2 / 0 | Saint-Étienne | — |
| 1981/82 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 982 | 0 | 2 / 0 | Monaco | — |
| 1982/83 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 1090 | 0 | 2 / 0 | Nantes | — |
| 1983/84 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 911 | 0 | 2 / 0 | Bordeaux | — |
| 1984/85 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 979 | 0 | 1 / 1 | Bordeaux | — |
| 1985/86 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 931 | 0 | 2 / 0 | PSG | — |
| 1986/87 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 796 | 0 | 1 / 1 | Bordeaux | — |
| 1987/88 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 854 | 0 | 2 / 0 | Monaco | — |
| 1988/89 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 900 | 0 | 2 / 0 | Olympique de Marseille | — |
| 1989/90 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 863 | 0 | 2 / 0 | Olympique de Marseille | — |
| 1990/91 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 805 | 0 | 2 / 0 | Olympique de Marseille | — |
| 1991/92 | engsoccerdata + ogol + RSSSF | 20 | 380 (380) | 796 | 0 | 1 / 0 | Olympique de Marseille | — |
| 1992/93 | engsoccerdata + ogol + RSSSF + Wikipédia | 20 | 380 (380) | 886 | 0 | 1 / 1 | — | Olympique de Marseille -1 pontos; Valenciennes -1 pontos |
| 1993/94 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 20 | 380 (380) | 850 | 0 | 2 / 0 | PSG | — |
| 1994/95 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 20 | 380 (380) | 951 | 0 | 2 / 0 | Nantes | — |
| 1995/96 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 20 | 380 (380) | 867 | 0 | 2 / 0 | Auxerre | — |
| 1996/97 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 20 | 380 (380) | 884 | 0 | 2 / 0 | Monaco | — |
| 1997/98 | engsoccerdata + ogol + football-data + Wikipédia | 18 | 306 (306) | 722 | 0 | 1 / 0 | Lens | — |
| 1998/99 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 723 | 0 | 2 / 0 | Bordeaux | — |
| 1999/00 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 787 | 0 | 2 / 0 | Monaco | — |
| 2000/01 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 764 | 0 | 2 / 0 | Nantes | — |
| 2001/02 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 716 | 702 | 2 / 0 | Lyon | — |
| 2002/03 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 837 | 829 | 2 / 0 | Lyon | — |
| 2003/04 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 884 | 876 | 2 / 0 | Lyon | — |
| 2004/05 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 826 | 826 | 2 / 0 | Lyon | — |
| 2005/06 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 811 | 808 | 2 / 0 | Lyon | — |
| 2006/07 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 855 | 840 | 2 / 0 | Lyon | — |
| 2007/08 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 868 | 866 | 2 / 0 | Lyon | — |
| 2008/09 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 858 | 846 | 1 / 1 | Bordeaux | Le Havre -1 pontos |
| 2009/10 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 916 | 906 | 2 / 0 | Olympique de Marseille | — |
| 2010/11 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 890 | 882 | 2 / 0 | Lille | — |
| 2011/12 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 956 | 954 | 2 / 0 | Montpellier | — |
| 2012/13 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 967 | 964 | 2 / 0 | PSG | Ajaccio -2 pontos |
| 2013/14 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 931 | 928 | 2 / 0 | PSG | — |
| 2014/15 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 947 | 947 | 2 / 0 | PSG | — |
| 2015/16 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 960 | 960 | 2 / 0 | PSG | — |
| 2016/17 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 991 | 991 | 2 / 0 | Monaco | — |
| 2017/18 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1033 | 1033 | 2 / 0 | PSG | — |
| 2018/19 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 972 | 972 | 2 / 0 | PSG | — |
| 2019/20 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 279 (279) | 704 | 702 | 2 / 0 | PSG | — |
| 2020/21 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1049 | 1049 | 2 / 0 | Lille | — |
| 2021/22 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1067 | 1067 | 2 / 0 | PSG | Nice -1 pontos; Lyon -1 pontos |
| 2022/23 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 20 | 380 (380) | 1067 | 1067 | 2 / 0 | PSG | — |
| 2023/24 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 826 | 824 | 2 / 0 | PSG | Montpellier -1 pontos |
| 2024/25 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 911 | 911 | 2 / 0 | PSG | — |
| 2025/26 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 863 | 863 | 2 / 0 | PSG | — |

## Conferência e ocorrências, temporada a temporada

### 1932/33

- o engsoccerdata junta os dois grupos de 1932/33 num só, de 14 clubes, todos os jogos em 01/07/1933
- a base não fecha nesta temporada (0 jogos): montada pelo calendário do ogol (181 jogos), com 0 jogos da base
- 181 jogos só no ogol, que entram com o placar do ogol: OGC Nice 2-3 SC Nimes (1932-09-11); Excelsior Roubaix 0-3 FC Sete (1932-09-11); Racing Club de France 2-1 Hyeres FC (1932-09-11); FC Mulhouse 2-3 Club Francais (1932-09-11); FC Metz 1-2 Stade Rennes (1932-09-11); Stade Olympique Montpellierain 2-0 Olympique Ales (1932-09-11) ...
- placar corrigido: Stade Olympique Montpellierain x SC Fives Lille de 3-2 para 4-2 — o ogol traz outro placar; a matriz e a tabela do grupo da RSSSF e a tabela do grupo da Wikipédia fecham com este
- placar corrigido: CA Paris (alt) x SC Fives Lille de 2-1 para 1-2 — o ogol traz outro placar; a matriz e a tabela do grupo da RSSSF e a tabela do grupo da Wikipédia fecham com este
- placar corrigido: FC Mulhouse x Olympique Lillois Lille de 0-2 para 1-2 — o ogol traz outro placar; a matriz e a tabela do grupo da RSSSF e a tabela do grupo da Wikipédia fecham com este
- placar corrigido: SC Fives Lille x Stade Olympique Montpellierain de 2-4 para 2-3 — o ogol traz outro placar; a matriz e a tabela do grupo da RSSSF e a tabela do grupo da Wikipédia fecham com este
- placar corrigido: SC Fives Lille x CA Paris (alt) de 2-1 para 0-2 — o ogol traz outro placar; a matriz e a tabela do grupo da RSSSF e a tabela do grupo da Wikipédia fecham com este
- placar diferente no ogol — Stade Olympique Montpellierain x SC Fives Lille (1932-09-18): base 4-2, ogol 3-2
- placar diferente no ogol — CA Paris (alt) x SC Fives Lille (1932-10-02): base 1-2, ogol 2-1
- placar diferente no ogol — FC Mulhouse x Olympique Lillois Lille (1932-10-16): base 1-2, ogol 0-2
- placar diferente no ogol — SC Fives Lille x Stade Olympique Montpellierain (1932-12-25): base 2-3, ogol 2-4
- placar diferente no ogol — SC Fives Lille x CA Paris (alt) (1933-01-28): base 0-2, ogol 2-1
- 181 jogos sem rodada do ogol (ex.: OGC Nice x SC Nimes)
- sem tabela publicada legível (RSSSF e Wikipédia)

### 1933/34

- o engsoccerdata traz clubes que não estavam na 1ª divisão nesta temporada (a RSSSF e a Wikipédia têm outros)
- a base não fecha nesta temporada (0 jogos): montada pelo calendário do ogol (182 jogos), com 0 jogos da base
- 182 jogos só no ogol, que entram com o placar do ogol: Olympique Marseille 4-0 OGC Nice (1933-07-01); Excelsior Roubaix 2-1 FC Sochaux (1933-07-01); FC Sete 6-2 CA Paris (alt) (1933-07-01); Stade Rennes 2-6 Stade Olympique Montpellierain (1933-07-01); OGC Nice 3-3 Excelsior Roubaix (1933-07-01); Olympique Marseille 3-3 FC Sete (1933-07-01) ...
- 6 jogos sem rodada do ogol (ex.: SC Fives Lille x FC Antibes)
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF FC Antibes, Wikipédia Stade Rennes); fica a da Wikipédia
- 58 jogos sem data conhecida (o ogol traz 01/07 ou 01/08, data provisória): data vazia

### 1934/35

- o engsoccerdata traz clubes que não estavam na 1ª divisão nesta temporada (a RSSSF e a Wikipédia têm outros)
- a base não fecha nesta temporada (0 jogos): montada pelo calendário do ogol (240 jogos), com 0 jogos da base
- 240 jogos só no ogol, que entram com o placar do ogol: Red Star FC 2-1 Stade Rennes (1934-07-01); Olympique Lillois Lille 2-0 FC Sete (1934-07-01); FC Sochaux 2-1 Stade Rennes (1934-07-01); Stade Rennes 4-0 Olympique Lillois Lille (1934-07-01); FC Sete 2-2 Red Star FC (1934-07-01); FC Sete 1-1 FC Sochaux (1934-07-01) ...
- 8 jogos sem rodada do ogol (ex.: FC Antibes x Stade Rennes)
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Olympique Marseille, Wikipédia Excelsior Roubaix); fica a da Wikipédia
- 70 jogos sem data conhecida (o ogol traz 01/07 ou 01/08, data provisória): data vazia

### 1935/36

- o engsoccerdata traz clubes que não estavam na 1ª divisão nesta temporada (a RSSSF e a Wikipédia têm outros)
- a base não fecha nesta temporada (0 jogos): montada pelo calendário do ogol (240 jogos), com 0 jogos da base
- 240 jogos só no ogol, que entram com o placar do ogol: Olympique Marseille 2-0 Olympique Ales (1935-07-01); FC Sete 1-1 Valenciennes FC (1935-07-01); Racing Club de France 2-1 Valenciennes FC (1935-07-01); Olympique Marseille 1-4 Red Star FC (1935-07-01); Olympique Lillois Lille 0-0 Stade Rennes (1935-08-01); FC Sochaux 0-0 SC Fives Lille (1935-08-01) ...
- 7 jogos sem rodada do ogol (ex.: Olympique Lillois Lille x Stade Rennes)
- 19 jogos sem data conhecida (o ogol traz 01/07 ou 01/08, data provisória): data vazia

### 1936/37

- o engsoccerdata traz clubes que não estavam na 1ª divisão nesta temporada (a RSSSF e a Wikipédia têm outros)
- a base não fecha nesta temporada (0 jogos): montada pelo calendário do ogol (240 jogos), com 0 jogos da base
- 240 jogos só no ogol, que entram com o placar do ogol: FC Sochaux 2-1 Excelsior Roubaix (1936-07-01); FC Sete 2-1 Red Star FC (1936-07-01); Red Star FC 2-2 RC Roubaix (1936-07-01); Red Star FC 2-2 FC Sochaux (1936-07-01); FC Sochaux 2-0 FC Antibes (1936-07-01); FC Sete 2-0 Excelsior Roubaix (1936-07-01) ...
- 10 jogos sem rodada do ogol (ex.: AS Cannes x SC Fives Lille)
- 72 jogos sem data conhecida (o ogol traz 01/07 ou 01/08, data provisória): data vazia

### 1937/38

- a RSSSF chama de "AMIENS" o clube que o ogol e a Wikipédia dão como Antibes (os resultados são os mesmos)
- o ogol não tem a data de mais da metade dos jogos (traz 01/07/1937): ficam sem data
- a tabela da Wikipédia erra gols, vitórias ou empates de alguns clubes; a da RSSSF fecha com os jogos e dá a ordem
- o engsoccerdata não traz esta temporada
- a base não fecha nesta temporada (0 jogos): montada pelo calendário do ogol (240 jogos), com 0 jogos da base
- 240 jogos só no ogol, que entram com o placar do ogol: FC Metz 1-0 Olympique Lillois Lille (1937-07-01); SC Fives Lille 3-1 FC Antibes (1937-07-01); Red Star FC 2-2 Excelsior Roubaix (1937-07-01); FC Sochaux 6-2 SC Fives Lille (1937-07-01); Excelsior Roubaix 1-1 RC Lens (1937-07-01); FC Antibes 1-1 FC Sete (1937-07-01) ...
- 12 jogos sem rodada do ogol (ex.: FC Sete x FC Antibes)
- tabela publicada x jogos (Wikipédia) — Excelsior Roubaix tabela [30, 10, 11, 9, 59, 57, 31] jogos [30, 10, 12, 8, 59, 57, 32]
- tabela publicada x jogos (Wikipédia) — Valenciennes FC tabela [30, 6, 6, 18, 30, 77, 18] jogos [30, 5, 7, 18, 30, 77, 17]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- 137 jogos sem data conhecida (o ogol traz 01/07 ou 01/08, data provisória): data vazia

### 1938/39

- data diferente no ogol em 14 jogos (ex.: RC Strasbourg x FC Sete: base 1938-09-04, ogol 1938-08-01); fica a da base

### 1945/46

- Red Star x Cannes: a base traz 1-1 e o ogol 0-0. A tabela da RSSSF e a da Wikipédia fecham com 0-0, mas a nota da RSSSF diz "possibly Red Star - Cannes 1-1; off. goal averages 63-60 (RS) resp. 52-56 (C)", que é o 1-1 da base. Fica a base
- placar diferente no ogol — Red Star FC x AS Cannes (1946-05-26): base 1-1, ogol 0-0
- tabela publicada x jogos (RSSSF) — AS Cannes tabela [34, 12, 10, 12, 51, 55, 34] jogos [34, 12, 10, 12, 52, 56, 34]
- tabela publicada x jogos (RSSSF) — Red Star FC tabela [34, 12, 9, 13, 62, 59, 33] jogos [34, 12, 9, 13, 63, 60, 33]
- tabela publicada x jogos (Wikipédia) — AS Cannes tabela [34, 12, 10, 12, 51, 55, 34] jogos [34, 12, 10, 12, 52, 56, 34]
- tabela publicada x jogos (Wikipédia) — Red Star FC tabela [34, 12, 9, 13, 62, 59, 33] jogos [34, 12, 9, 13, 63, 60, 33]

### 1946/47

- a tabela da RSSSF dá ao CO Roubaix-Tourcoing 11 derrotas (os números não somam 38 jogos; são 9)
- a tabela da Wikipédia erra gols, vitórias ou empates de alguns clubes; a da RSSSF fecha com os jogos e dá a ordem
- a base não fecha nesta temporada (340 jogos): montada pelo calendário do ogol (380 jogos), com 331 jogos da base
- 49 jogos só no ogol, que entram com o placar do ogol: FC Rouen 6-0 FC Sete (1946-08-18); CO Roubaix-Tourcoing 4-1 RC Lens (1946-09-15); Olympique Marseille 1-3 Girondins Bordeaux (1946-10-27); Stade Olympique Montpellierain 2-6 Stade Francais FC (1946-10-27); CO Roubaix-Tourcoing 5-2 Stade Olympique Montpellierain (1946-11-03); RC Lens 8-1 Le Havre AC (1946-11-10) ...
- 9 jogos com data errada na base, trocada pela do ogol: RC Strasbourg x Red Star FC (1946-03-10 -> 1946-11-10); Lille OSC x FC Rouen (1946-03-10 -> 1946-11-10); Stade Francais FC x Racing Club de France (1946-03-10 -> 1946-11-10); Olympique Marseille x CO Roubaix-Tourcoing (1946-03-10 -> 1946-11-10) ...
- 9 jogos da base fora do calendário do ogol, descartados: RC Lens 8-0 Le Havre AC (1946-03-10); FC Rouen 6-1 FC Sete (1946-08-18); CO Roubaix-Tourcoing 5-2 RC Lens (1946-09-15); Stade Olympique Montpellierain 1-3 Stade Francais FC (1946-10-27); Olympique Marseille 0-0 Girondins Bordeaux (1946-10-27); CO Roubaix-Tourcoing 2-1 Stade Olympique Montpellierain (1946-11-03)
- data diferente no ogol em 2 jogos (ex.: Racing Club de France x CO Roubaix-Tourcoing: base 1946-09-01, ogol 1946-08-31); fica a da base
- tabela publicada x jogos (RSSSF) — CO Roubaix-Tourcoing tabela [38, 24, 5, 11, 70, 46, 53] jogos [38, 24, 5, 9, 70, 46, 53]
- tabela publicada x jogos (Wikipédia) — CO Roubaix-Tourcoing tabela [38, 24, 5, 9, 71, 47, 53] jogos [38, 24, 5, 9, 70, 46, 53]
- tabela publicada x jogos (Wikipédia) — RC Strasbourg tabela [38, 21, 7, 10, 79, 50, 49] jogos [38, 21, 7, 10, 80, 50, 49]
- tabela publicada x jogos (Wikipédia) — Lille OSC tabela [38, 20, 7, 11, 89, 52, 47] jogos [38, 20, 7, 11, 91, 52, 47]
- tabela publicada x jogos (Wikipédia) — Stade Francais FC tabela [38, 19, 8, 11, 72, 58, 46] jogos [38, 19, 8, 11, 75, 59, 46]
- tabela publicada x jogos (Wikipédia) — Olympique Marseille tabela [38, 17, 11, 10, 69, 55, 45] jogos [38, 16, 11, 11, 70, 58, 43]
- tabela publicada x jogos (Wikipédia) — FC Sete tabela [38, 12, 11, 15, 65, 79, 35] jogos [38, 12, 11, 15, 64, 79, 35]
- tabela publicada x jogos (Wikipédia) — Stade Olympique Montpellierain tabela [38, 14, 5, 19, 59, 71, 33] jogos [38, 14, 5, 19, 61, 77, 33]
- tabela publicada x jogos (Wikipédia) — RC Lens tabela [38, 12, 7, 19, 67, 72, 31] jogos [38, 12, 7, 19, 66, 72, 31]
- tabela publicada x jogos (Wikipédia) — Girondins Bordeaux tabela [38, 12, 7, 19, 58, 81, 31] jogos [38, 13, 7, 18, 60, 79, 33]
- tabela publicada x jogos (Wikipédia) — Le Havre AC tabela [38, 9, 7, 22, 44, 83, 25] jogos [38, 9, 7, 22, 45, 85, 25]
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Girondins Bordeaux, Wikipédia RC Lens); fica a da Wikipédia
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 2 posições (ex.: ['RC Lens', 'Girondins Bordeaux'])

### 1947/48

- placar diferente no ogol — Racing Club de France x Stade Francais FC (1947-11-30): base 0-1, ogol 5-1
- placar diferente no ogol — Stade Francais FC x Racing Club de France (1948-04-25): base 1-5, ogol 1-0
- data diferente no ogol em 1 jogos (ex.: FC Metz x AS Saint-Etienne: base 1948-03-11, ogol 1948-08-22); fica a da base
- placar diferente na matriz da RSSSF — Stade Francais FC x Racing Club de France: base 1-5, RSSSF 1-0
- placar diferente na matriz da RSSSF — Racing Club de France x Stade Francais FC: base 0-1, RSSSF 5-1

### 1948/49

- data diferente no ogol em 2 jogos (ex.: FC Sochaux x Stade Olympique Montpellierain: base 1949-01-02, ogol 1949-02-28); fica a da base

### 1949/50

- sem ocorrências

### 1950/51

- data diferente no ogol em 4 jogos (ex.: FC Sochaux x Stade Francais FC: base 1950-11-26, ogol 1950-12-28); fica a da base
- placar diferente na matriz da RSSSF — Lille OSC x Toulouse FC: base 1-2, RSSSF 2-0
- placar diferente na matriz da RSSSF — Toulouse FC x Lille OSC: base 0-2, RSSSF 2-1

### 1951/52

- a tabela da Wikipédia erra gols, vitórias ou empates de alguns clubes; a da RSSSF fecha com os jogos e dá a ordem
- data diferente no ogol em 3 jogos (ex.: Olympique Lyon x Nimes Olympique: base 1951-12-16, ogol 1952-01-24); fica a da base
- tabela publicada x jogos (Wikipédia) — Racing Club de France tabela [34, 13, 5, 16, 60, 71, 31] jogos [34, 12, 6, 16, 60, 71, 30]
- tabela publicada x jogos (Wikipédia) — Olympique Marseille tabela [34, 9, 9, 16, 52, 76, 27] jogos [34, 9, 10, 15, 52, 76, 28]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1952/53

- a tabela da RSSSF tem erro de digitação em um clube (gols ou V-E-D que não somam); a da Wikipédia fecha com os jogos
- tabela publicada x jogos (RSSSF) — Racing Club de France tabela [34, 11, 6, 17, 40, 66, 28] jogos [34, 11, 6, 17, 40, 64, 28]

### 1953/54

- a tabela da Wikipédia erra gols, vitórias ou empates de alguns clubes; a da RSSSF fecha com os jogos e dá a ordem
- 12 jogos sem rodada no ogol ficam com a rodada dos outros jogos do mesmo dia
- data diferente no ogol em 12 jogos (ex.: Olympique Marseille x Nimes Olympique: base 1953-08-23, ogol 1953-08-01); fica a da base
- tabela publicada x jogos (Wikipédia) — Le Havre AC tabela [34, 10, 6, 18, 53, 69, 26] jogos [34, 10, 6, 18, 54, 69, 26]
- tabela publicada x jogos (Wikipédia) — FC Sete tabela [34, 6, 10, 18, 38, 70, 22] jogos [34, 6, 10, 18, 38, 71, 22]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1954/55

- data diferente no ogol em 3 jogos (ex.: Nimes Olympique x FC Sochaux: base 1954-11-28, ogol 1954-12-16); fica a da base

### 1955/56

- a tabela da Wikipédia erra gols, vitórias ou empates de alguns clubes; a da RSSSF fecha com os jogos e dá a ordem
- data diferente no ogol em 3 jogos (ex.: AS Saint-Etienne x AS Monaco: base 1956-04-02, ogol 1956-04-01); fica a da base
- tabela publicada x jogos (Wikipédia) — Olympique Marseille tabela [34, 16, 8, 10, 55, 49, 40] jogos [34, 15, 9, 10, 54, 49, 39]
- tabela publicada x jogos (Wikipédia) — AS Nancy tabela [34, 13, 6, 15, 51, 61, 32] jogos [34, 13, 7, 14, 51, 60, 33]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1956/57

- data diferente no ogol em 1 jogos (ex.: Toulouse FC x Olympique Marseille: base 1956-12-02, ogol 1956-08-01); fica a da base

### 1957/58

- data diferente no ogol em 1 jogos (ex.: Valenciennes FC x Olympique Marseille: base 1958-01-26, ogol 1958-02-27); fica a da base
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Angers SCO, Wikipédia AS Monaco); fica a da Wikipédia

### 1958/59

- placar corrigido: FC Sochaux x Stade Rennes de 4-3 para 2-1 — a base e o ogol trazem 4-3; a matriz e a tabela da RSSSF e a tabela da Wikipédia fecham com 2-1
- placar diferente no ogol — FC Sochaux x Stade Rennes (1959-05-24): base 2-1, ogol 4-3
- data diferente no ogol em 3 jogos (ex.: AS Monaco x Stade Reims: base 1958-07-21, ogol 1958-09-21); fica a da base

### 1959/60

- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Sporting Toulon Var, Wikipédia RC Strasbourg); fica a da Wikipédia

### 1960/61

- data diferente no ogol em 8 jogos (ex.: RC Lens x AS Monaco: base 1960-08-21, ogol 1960-08-20); fica a da base
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Stade Rennes, Wikipédia OGC Nice); fica a da Wikipédia

### 1961/62

- data diferente no ogol em 1 jogos (ex.: Stade Francais FC x FC Rouen: base 1962-04-22, ogol 1962-04-21); fica a da base

### 1962/63

- sem ocorrências

### 1963/64

- Toulouse x Reims: a base e a tabela da Wikipédia trazem 0-0; o ogol e a matriz da RSSSF trazem 2-2 (e a tabela da RSSSF tem 8 gols a menos para o Toulouse). Fica a base
- placar diferente no ogol — Toulouse FC x Stade Reims (1964-05-17): base 0-0, ogol 2-2
- data diferente no ogol em 1 jogos (ex.: Olympique Lyon x RC Lens: base 1964-01-19, ogol 1964-01-30); fica a da base
- placar diferente na matriz da RSSSF — Toulouse FC x Stade Reims: base 0-0, RSSSF 2-2
- tabela publicada x jogos (RSSSF) — Toulouse FC tabela [34, 13, 11, 10, 56, 46, 37] jogos [34, 13, 11, 10, 56, 54, 37]

### 1964/65

- sem ocorrências

### 1965/66

- a tabela da RSSSF tem erro de digitação em um clube (gols ou V-E-D que não somam); a da Wikipédia fecha com os jogos
- data diferente no ogol em 1 jogos (ex.: Lille OSC x Valenciennes FC: base 1966-04-23, ogol 1966-04-24); fica a da base
- tabela publicada x jogos (RSSSF) — OGC Nice tabela [38, 16, 14, 18, 66, 59, 36] jogos [38, 16, 4, 18, 66, 59, 36]

### 1966/67

- sem ocorrências

### 1967/68

- data diferente no ogol em 6 jogos (ex.: AS Aixoise x AS Saint-Etienne: base 1968-02-17, ogol 1968-02-18); fica a da base

### 1968/69

- placar diferente no ogol — SC Bastia x CS Sedan (1968-11-11): base 0-0, ogol 1-5
- placar diferente no ogol — CS Sedan x SC Bastia (1969-05-21): base 5-1, ogol 0-0
- placar diferente na matriz da RSSSF — CS Sedan x SC Bastia: base 5-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — SC Bastia x CS Sedan: base 0-0, RSSSF 1-5
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Nimes Olympique, Wikipédia RC Strasbourg); fica a da Wikipédia

### 1969/70

- data diferente no ogol em 2 jogos (ex.: Angers SCO x AS Saint-Etienne: base 1970-06-06, ogol 1969-12-28); fica a da base

### 1970/71

- data diferente no ogol em 11 jogos (ex.: Nimes Olympique x Girondins Bordeaux: base 1970-11-12, ogol 1970-10-12); fica a da base

### 1971/72

- Nice x Lille: a base, o ogol e a tabela da Wikipédia trazem 3-1; a RSSSF traz 3-0. Fica a base
- placar diferente na matriz da RSSSF — OGC Nice x Lille OSC: base 3-1, RSSSF 3-0
- tabela publicada x jogos (RSSSF) — OGC Nice tabela [38, 15, 12, 11, 58, 43, 42] jogos [38, 15, 12, 11, 58, 44, 42]
- tabela publicada x jogos (RSSSF) — Lille OSC tabela [38, 8, 10, 20, 42, 68, 26] jogos [38, 8, 10, 20, 43, 68, 26]

### 1972/73

- data diferente no ogol em 1 jogos (ex.: AS Nancy x Nimes Olympique: base 1973-05-02, ogol 1973-05-03); fica a da base

### 1973/74

- sem ocorrências

### 1974/75

- sem ocorrências

### 1975/76

- a tabela da Wikipédia erra gols, vitórias ou empates de alguns clubes; a da RSSSF fecha com os jogos e dá a ordem
- data diferente no ogol em 1 jogos (ex.: Nimes Olympique x FC Nantes: base 1975-08-08, ogol 1975-07-08); fica a da base
- tabela publicada x jogos (Wikipédia) — AS Saint-Etienne tabela [38, 18, 15, 5, 69, 38, 57] jogos [38, 18, 15, 5, 68, 39, 57]
- tabela publicada x jogos (Wikipédia) — Stade Reims tabela [38, 17, 8, 13, 67, 49, 47] jogos [38, 17, 8, 13, 68, 49, 47]
- tabela publicada x jogos (Wikipédia) — Troyes AF tabela [38, 9, 16, 13, 48, 55, 37] jogos [38, 9, 16, 13, 48, 54, 37]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1976/77

- data diferente no ogol em 1 jogos (ex.: Paris Saint-Germain x FC Metz: base 1976-11-20, ogol 1976-11-21); fica a da base
- ordem diferente entre RSSSF e Wikipédia em 4 posições (ex.: RSSSF OGC Nice, Wikipédia Olympique Lyon); fica a da Wikipédia

### 1977/78

- data diferente no ogol em 1 jogos (ex.: AS Nancy x FC Nantes: base 1977-10-14, ogol 1977-12-14); fica a da base
- placar diferente na matriz da RSSSF — Girondins Bordeaux x OGC Nice: base 3-5, RSSSF 0-1
- placar diferente na matriz da RSSSF — Olympique Lyon x Paris Saint-Germain: base 2-3, RSSSF 3-2
- placar diferente na matriz da RSSSF — Olympique Lyon x Valenciennes FC: base 1-2, RSSSF 0-1
- placar diferente na matriz da RSSSF — Olympique Marseille x FC Metz: base 4-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — Olympique Marseille x FC Rouen: base 4-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — FC Metz x Olympique Marseille: base 0-2, RSSSF 0-4
- placar diferente na matriz da RSSSF — OGC Nice x Girondins Bordeaux: base 1-0, RSSSF 5-3
- placar diferente na matriz da RSSSF — Paris Saint-Germain x Olympique Lyon: base 2-3, RSSSF 3-2
- placar diferente na matriz da RSSSF — Paris Saint-Germain x FC Metz: base 2-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x Troyes AF: base 8-2, RSSSF 7-2
- placar diferente na matriz da RSSSF — FC Rouen x Olympique Marseille: base 0-2, RSSSF 1-4
- placar diferente na matriz da RSSSF — FC Sochaux x FC Metz: base 4-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — FC Sochaux x Troyes AF: base 5-2, RSSSF 6-2
- placar diferente na matriz da RSSSF — Valenciennes FC x Olympique Lyon: base 1-0, RSSSF 2-1

### 1978/79

- data diferente no ogol em 4 jogos (ex.: Olympique Lyon x Stade Reims: base 1978-07-25, ogol 1978-07-01); fica a da base
- placar diferente na matriz da RSSSF — Stade Laval x Paris Saint-Germain: base 2-3, RSSSF 2-1
- placar diferente na matriz da RSSSF — Olympique Lyon x AS Monaco: base 0-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — Olympique Marseille x Stade Reims: base 0-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — AS Monaco x Olympique Lyon: base 0-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — Paris FC x Stade Reims: base 2-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x Stade Laval: base 1-2, RSSSF 3-2
- placar diferente na matriz da RSSSF — Stade Reims x Olympique Marseille: base 0-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — Stade Reims x Paris FC: base 0-2, RSSSF 1-2

### 1979/80

- a RSSSF chama de "GRENOBLE" o Bastia (o Grenoble não estava na 1ª divisão)
- a tabela da Wikipédia erra gols, vitórias ou empates de alguns clubes; a da RSSSF fecha com os jogos e dá a ordem
- tabela publicada x jogos (Wikipédia) — FC Sochaux tabela [38, 24, 6, 8, 76, 36, 54] jogos [38, 24, 6, 8, 77, 36, 54]
- tabela publicada x jogos (Wikipédia) — RC Lens tabela [38, 14, 10, 14, 51, 51, 38] jogos [38, 14, 10, 14, 51, 52, 38]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1980/81

- data diferente no ogol em 6 jogos (ex.: AS Monaco x Olympique Lyon: base 1980-12-06, ogol 1980-12-07); fica a da base

### 1981/82

- data diferente no ogol em 2 jogos (ex.: Stade Brest x AS Saint-Etienne: base 1981-09-01, ogol 1981-09-29); fica a da base

### 1982/83

- data diferente no ogol em 2 jogos (ex.: FC Sochaux x Toulouse FC: base 1982-08-17, ogol 1982-07-01); fica a da base
- placar diferente na matriz da RSSSF — AS Nancy x FC Sochaux: base 1-3, RSSSF 1-2

### 1983/84

- data diferente no ogol em 1 jogos (ex.: Stade Brest x RC Strasbourg: base 1984-03-24, ogol 1984-03-23); fica a da base
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Stade Laval, Wikipédia SC Bastia); fica a da Wikipédia

### 1984/85

- a tabela da Wikipédia erra gols, vitórias ou empates de alguns clubes; a da RSSSF fecha com os jogos e dá a ordem
- tabela publicada x jogos (Wikipédia) — FC Sochaux tabela [38, 12, 14, 12, 55, 43, 38] jogos [38, 12, 14, 12, 56, 43, 38]
- tabela publicada x jogos (Wikipédia) — Racing Club de France tabela [38, 9, 8, 21, 32, 55, 26] jogos [38, 9, 8, 21, 32, 56, 26]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF

### 1985/86

- data diferente no ogol em 1 jogos (ex.: RC Strasbourg x AS Monaco: base 1985-12-07, ogol 1985-12-08); fica a da base

### 1986/87

- a tabela da RSSSF tem erro de digitação em um clube (gols ou V-E-D que não somam); a da Wikipédia fecha com os jogos
- data diferente no ogol em 12 jogos (ex.: AS Nancy x Stade Brest: base 1986-08-12, ogol 1986-07-01); fica a da base
- tabela publicada x jogos (RSSSF) — Racing Club de France tabela [38, 14, 7, 16, 41, 45, 35] jogos [38, 14, 8, 16, 41, 45, 36]
- tabela publicada x jogos (RSSSF) — AS Nancy tabela [38, 8, 12, 17, 28, 40, 28] jogos [38, 8, 13, 17, 28, 40, 29]

### 1987/88

- data diferente no ogol em 2 jogos (ex.: Chamois Niortais x AS Saint-Etienne: base 1987-08-19, ogol 1987-08-18); fica a da base

### 1988/89

- data diferente no ogol em 11 jogos (ex.: AS Cannes x AS Saint-Etienne: base 1988-09-10, ogol 1988-09-09); fica a da base

### 1989/90

- data diferente no ogol em 3 jogos (ex.: SM Caen x FC Nantes: base 1989-09-09, ogol 1989-07-01); fica a da base

### 1990/91

- resultado do tribunal: Sporting Toulon Var x Paris Saint-Germain fica 0-0 com vitória do PSG (base 0-0) — empate em campo mudado em vitória do PSG (RSSSF: "changed in win for Paris St. Germain"; a tabela da RSSSF e a da Wikipédia contam a vitória)

### 1991/92

- placar diferente na matriz da RSSSF — AJ Auxerre x AS Nancy: base 3-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — AJ Auxerre x FC Nantes: base 2-2, RSSSF 3-1
- placar diferente na matriz da RSSSF — AJ Auxerre x Nimes Olympique: base 0-0, RSSSF 2-2
- placar diferente na matriz da RSSSF — AJ Auxerre x Paris Saint-Germain: base 2-2, RSSSF 0-0
- placar diferente na matriz da RSSSF — AJ Auxerre x Stade Rennes: base 3-1, RSSSF 2-2
- placar diferente na matriz da RSSSF — AJ Auxerre x AS Saint-Etienne: base 2-0, RSSSF 3-1
- placar diferente na matriz da RSSSF — AJ Auxerre x FC Sochaux: base 4-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — AJ Auxerre x Sporting Toulon Var: base 1-0, RSSSF 4-0
- placar diferente na matriz da RSSSF — AJ Auxerre x Toulouse FC: base 3-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — SM Caen x AS Nancy: base 5-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — SM Caen x FC Nantes: base 1-1, RSSSF 5-1
- placar diferente na matriz da RSSSF — SM Caen x Nimes Olympique: base 2-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — SM Caen x Stade Rennes: base 0-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — SM Caen x AS Saint-Etienne: base 1-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — SM Caen x FC Sochaux: base 1-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — SM Caen x Sporting Toulon Var: base 4-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — SM Caen x Toulouse FC: base 1-0, RSSSF 4-1
- placar diferente na matriz da RSSSF — AS Cannes x AS Nancy: base 1-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — AS Cannes x FC Nantes: base 2-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — AS Cannes x Nimes Olympique: base 0-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — AS Cannes x Paris Saint-Germain: base 1-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — AS Cannes x Stade Rennes: base 3-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — AS Cannes x AS Saint-Etienne: base 0-2, RSSSF 3-1
- placar diferente na matriz da RSSSF — AS Cannes x FC Sochaux: base 2-1, RSSSF 0-2
- placar diferente na matriz da RSSSF — AS Cannes x Sporting Toulon Var: base 0-1, RSSSF 2-1
- placar diferente na matriz da RSSSF — AS Cannes x Toulouse FC: base 2-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — Le Havre AC x AS Nancy: base 1-2, RSSSF 3-1
- placar diferente na matriz da RSSSF — Le Havre AC x FC Nantes: base 1-1, RSSSF 1-2
- placar diferente na matriz da RSSSF — Le Havre AC x Stade Rennes: base 0-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Le Havre AC x AS Saint-Etienne: base 2-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — Le Havre AC x FC Sochaux: base 1-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — Le Havre AC x Sporting Toulon Var: base 3-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — Le Havre AC x Toulouse FC: base 1-1, RSSSF 3-0
- placar diferente na matriz da RSSSF — RC Lens x AS Nancy: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — RC Lens x FC Nantes: base 0-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — RC Lens x Paris Saint-Germain: base 1-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — RC Lens x Stade Rennes: base 0-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — RC Lens x AS Saint-Etienne: base 1-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — RC Lens x Sporting Toulon Var: base 2-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — RC Lens x Toulouse FC: base 4-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — Lille OSC x AS Nancy: base 2-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Lille OSC x FC Nantes: base 0-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — Lille OSC x Nimes Olympique: base 1-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — Lille OSC x Paris Saint-Germain: base 0-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Lille OSC x Stade Rennes: base 1-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — Lille OSC x AS Saint-Etienne: base 2-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Lille OSC x FC Sochaux: base 0-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — Lille OSC x Sporting Toulon Var: base 1-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — Lille OSC x Toulouse FC: base 3-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — Olympique Lyon x AS Nancy: base 2-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Olympique Lyon x FC Nantes: base 0-1, RSSSF 2-1
- placar diferente na matriz da RSSSF — Olympique Lyon x Nimes Olympique: base 1-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — Olympique Lyon x Paris Saint-Germain: base 0-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Olympique Lyon x Stade Rennes: base 3-1, RSSSF 0-1
- placar diferente na matriz da RSSSF — Olympique Lyon x AS Saint-Etienne: base 0-0, RSSSF 3-1
- placar diferente na matriz da RSSSF — Olympique Lyon x FC Sochaux: base 0-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — Olympique Lyon x Sporting Toulon Var: base 1-1, RSSSF 0-1
- placar diferente na matriz da RSSSF — Olympique Lyon x Toulouse FC: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Olympique Marseille x AS Nancy: base 4-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — Olympique Marseille x Nimes Olympique: base 4-2, RSSSF 4-0
- placar diferente na matriz da RSSSF — Olympique Marseille x Paris Saint-Germain: base 0-0, RSSSF 4-2
- placar diferente na matriz da RSSSF — Olympique Marseille x Stade Rennes: base 5-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — Olympique Marseille x AS Saint-Etienne: base 2-0, RSSSF 5-1
- placar diferente na matriz da RSSSF — Olympique Marseille x FC Sochaux: base 2-2, RSSSF 2-0
- placar diferente na matriz da RSSSF — Olympique Marseille x Sporting Toulon Var: base 0-1, RSSSF 2-2
- placar diferente na matriz da RSSSF — Olympique Marseille x Toulouse FC: base 2-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — FC Metz x AS Nancy: base 0-1, RSSSF 1-3
- placar diferente na matriz da RSSSF — FC Metz x FC Nantes: base 1-1, RSSSF 0-1
- placar diferente na matriz da RSSSF — FC Metz x Nimes Olympique: base 4-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Metz x Paris Saint-Germain: base 0-0, RSSSF 4-0
- placar diferente na matriz da RSSSF — FC Metz x AS Saint-Etienne: base 1-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — FC Metz x FC Sochaux: base 3-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — FC Metz x Sporting Toulon Var: base 4-1, RSSSF 3-1
- placar diferente na matriz da RSSSF — FC Metz x Toulouse FC: base 4-0, RSSSF 4-1
- placar diferente na matriz da RSSSF — AS Monaco x AS Nancy: base 4-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — AS Monaco x FC Nantes: base 1-0, RSSSF 4-1
- placar diferente na matriz da RSSSF — AS Monaco x Nimes Olympique: base 1-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — AS Monaco x Paris Saint-Germain: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — AS Monaco x Stade Rennes: base 3-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — AS Monaco x AS Saint-Etienne: base 2-0, RSSSF 3-1
- placar diferente na matriz da RSSSF — AS Monaco x Sporting Toulon Var: base 3-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — AS Monaco x Toulouse FC: base 0-2, RSSSF 3-0
- placar diferente na matriz da RSSSF — AS Nancy x Nimes Olympique: base 2-3, RSSSF 3-1
- placar diferente na matriz da RSSSF — AS Nancy x Paris Saint-Germain: base 0-0, RSSSF 2-3
- placar diferente na matriz da RSSSF — AS Nancy x Stade Rennes: base 1-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — AS Nancy x AS Saint-Etienne: base 0-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — AS Nancy x FC Sochaux: base 3-1, RSSSF 0-2
- placar diferente na matriz da RSSSF — AS Nancy x Sporting Toulon Var: base 0-0, RSSSF 3-1
- placar diferente na matriz da RSSSF — AS Nancy x Toulouse FC: base 1-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — FC Nantes x Paris Saint-Germain: base 0-0, RSSSF 3-2
- placar diferente na matriz da RSSSF — FC Nantes x Stade Rennes: base 1-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — FC Nantes x FC Sochaux: base 0-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — FC Nantes x Sporting Toulon Var: base 1-2, RSSSF 0-0
- placar diferente na matriz da RSSSF — FC Nantes x Toulouse FC: base 1-1, RSSSF 1-2
- placar diferente na matriz da RSSSF — Nimes Olympique x AS Nancy: base 1-2, RSSSF 2-1
- placar diferente na matriz da RSSSF — Nimes Olympique x FC Nantes: base 0-0, RSSSF 1-2
- placar diferente na matriz da RSSSF — Nimes Olympique x Stade Rennes: base 1-2, RSSSF 0-1
- placar diferente na matriz da RSSSF — Nimes Olympique x AS Saint-Etienne: base 1-1, RSSSF 1-2
- placar diferente na matriz da RSSSF — Nimes Olympique x FC Sochaux: base 2-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — Nimes Olympique x Sporting Toulon Var: base 1-0, RSSSF 2-2
- placar diferente na matriz da RSSSF — Nimes Olympique x Toulouse FC: base 2-2, RSSSF 1-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x AS Nancy: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Paris Saint-Germain x FC Nantes: base 1-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x Nimes Olympique: base 2-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Paris Saint-Germain x AS Saint-Etienne: base 0-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x FC Sochaux: base 2-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x Sporting Toulon Var: base 2-3, RSSSF 2-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x Toulouse FC: base 0-0, RSSSF 2-3
- placar diferente na matriz da RSSSF — Stade Rennes x AS Nancy: base 3-1, RSSSF 0-2
- placar diferente na matriz da RSSSF — Stade Rennes x FC Nantes: base 0-1, RSSSF 3-1
- placar diferente na matriz da RSSSF — Stade Rennes x Nimes Olympique: base 1-1, RSSSF 0-1
- placar diferente na matriz da RSSSF — Stade Rennes x Paris Saint-Germain: base 0-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Stade Rennes x FC Sochaux: base 2-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — Stade Rennes x Sporting Toulon Var: base 0-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — Stade Rennes x Toulouse FC: base 1-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — AS Saint-Etienne x AS Nancy: base 3-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — AS Saint-Etienne x FC Nantes: base 2-1, RSSSF 3-0
- placar diferente na matriz da RSSSF — AS Saint-Etienne x Nimes Olympique: base 3-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — AS Saint-Etienne x Stade Rennes: base 0-1, RSSSF 3-0
- placar diferente na matriz da RSSSF — AS Saint-Etienne x Sporting Toulon Var: base 3-1, RSSSF 2-1
- placar diferente na matriz da RSSSF — AS Saint-Etienne x Toulouse FC: base 2-1, RSSSF 3-1
- placar diferente na matriz da RSSSF — FC Sochaux x AS Nancy: base 2-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Sochaux x FC Nantes: base 3-1, RSSSF 2-2
- placar diferente na matriz da RSSSF — FC Sochaux x Nimes Olympique: base 1-1, RSSSF 3-1
- placar diferente na matriz da RSSSF — FC Sochaux x Paris Saint-Germain: base 0-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Sochaux x Stade Rennes: base 0-0, RSSSF 0-2
- placar diferente na matriz da RSSSF — FC Sochaux x AS Saint-Etienne: base 1-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — FC Sochaux x Toulouse FC: base 0-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — Sporting Toulon Var x AS Nancy: base 4-2, RSSSF 0-1
- placar diferente na matriz da RSSSF — Sporting Toulon Var x FC Nantes: base 0-2, RSSSF 4-2
- placar diferente na matriz da RSSSF — Sporting Toulon Var x Nimes Olympique: base 5-0, RSSSF 0-2
- placar diferente na matriz da RSSSF — Sporting Toulon Var x Paris Saint-Germain: base 2-5, RSSSF 5-0
- placar diferente na matriz da RSSSF — Sporting Toulon Var x Stade Rennes: base 1-0, RSSSF 2-5
- placar diferente na matriz da RSSSF — Sporting Toulon Var x AS Saint-Etienne: base 1-2, RSSSF 1-0
- placar diferente na matriz da RSSSF — Sporting Toulon Var x FC Sochaux: base 2-0, RSSSF 1-2
- placar diferente na matriz da RSSSF — Toulouse FC x AS Nancy: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Toulouse FC x FC Nantes: base 2-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Toulouse FC x Nimes Olympique: base 0-1, RSSSF 2-1
- placar diferente na matriz da RSSSF — Toulouse FC x Paris Saint-Germain: base 3-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — Toulouse FC x Stade Rennes: base 2-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — Toulouse FC x AS Saint-Etienne: base 1-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — Toulouse FC x FC Sochaux: base 2-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — Toulouse FC x Sporting Toulon Var: base 3-0, RSSSF 2-1

### 1992/93

- o título foi tirado do Marseille (suborno no jogo com o Valenciennes) e ninguém foi declarado campeão
- Valenciennes x Marseille (20/05/1993, o jogo do caso VA-OM): o ogol e a matriz da RSSSF trazem 0-1; a base e a tabela da Wikipédia, 0-0 (a tabela da RSSSF não fecha com nenhum dos dois). Fica a base, que fecha com uma tabela publicada
- placar diferente no ogol — Valenciennes FC x Olympique Marseille (1993-05-20): base 0-0, ogol 0-1
- placar diferente na matriz da RSSSF — Valenciennes FC x Olympique Marseille: base 0-0, RSSSF 0-1
- tabela publicada x jogos (RSSSF) — Olympique Marseille tabela [38, 22, 9, 7, 71, 36, 53] jogos [38, 22, 10, 6, 71, 36, 53]
- tabela publicada x jogos (RSSSF) — Valenciennes FC tabela [38, 9, 11, 18, 42, 57, 29] jogos [38, 9, 12, 17, 42, 56, 29]
- título não atribuído (lista de campeões da Wikipédia); Olympique de Marseille terminou em 1º

### 1993/94

- placar diferente na matriz da RSSSF — Angers SCO x RC Lens: base 1-2, RSSSF 0-0
- placar diferente na matriz da RSSSF — Angers SCO x Olympique Lyon: base 3-1, RSSSF 1-2
- placar diferente na matriz da RSSSF — Angers SCO x Olympique Marseille: base 0-1, RSSSF 3-1
- placar diferente na matriz da RSSSF — Angers SCO x FC Martigues: base 1-3, RSSSF 0-1
- placar diferente na matriz da RSSSF — Angers SCO x FC Metz: base 1-2, RSSSF 1-3
- placar diferente na matriz da RSSSF — Angers SCO x AS Monaco: base 1-1, RSSSF 1-2
- placar diferente na matriz da RSSSF — Angers SCO x Montpellier HSC: base 2-3, RSSSF 1-1
- placar diferente na matriz da RSSSF — Angers SCO x FC Nantes: base 0-0, RSSSF 2-3
- placar diferente na matriz da RSSSF — Angers SCO x Paris Saint-Germain: base 1-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — Angers SCO x FC Sochaux: base 1-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — Angers SCO x RC Strasbourg: base 1-3, RSSSF 1-2
- placar diferente na matriz da RSSSF — Angers SCO x Toulouse FC: base 0-0, RSSSF 1-3
- placar diferente na matriz da RSSSF — AJ Auxerre x RC Lens: base 1-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — AJ Auxerre x Lille OSC: base 5-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — AJ Auxerre x Olympique Lyon: base 3-2, RSSSF 5-0
- placar diferente na matriz da RSSSF — AJ Auxerre x Olympique Marseille: base 2-2, RSSSF 3-2
- placar diferente na matriz da RSSSF — AJ Auxerre x FC Martigues: base 3-0, RSSSF 2-2
- placar diferente na matriz da RSSSF — AJ Auxerre x FC Metz: base 2-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — AJ Auxerre x AS Monaco: base 4-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — AJ Auxerre x Montpellier HSC: base 3-1, RSSSF 4-0
- placar diferente na matriz da RSSSF — AJ Auxerre x Paris Saint-Germain: base 0-0, RSSSF 3-1
- placar diferente na matriz da RSSSF — AJ Auxerre x AS Saint-Etienne: base 3-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — AJ Auxerre x FC Sochaux: base 1-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — AJ Auxerre x RC Strasbourg: base 2-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — AJ Auxerre x Toulouse FC: base 5-1, RSSSF 2-1
- placar diferente na matriz da RSSSF — Girondins Bordeaux x RC Lens: base 4-2, RSSSF 2-1
- placar diferente na matriz da RSSSF — Girondins Bordeaux x Lille OSC: base 2-1, RSSSF 4-2
- placar diferente na matriz da RSSSF — Girondins Bordeaux x Olympique Lyon: base 2-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — Girondins Bordeaux x Olympique Marseille: base 1-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — Girondins Bordeaux x FC Martigues: base 1-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Girondins Bordeaux x FC Metz: base 2-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Girondins Bordeaux x AS Monaco: base 1-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — Girondins Bordeaux x Montpellier HSC: base 1-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Girondins Bordeaux x FC Nantes: base 2-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Girondins Bordeaux x Paris Saint-Germain: base 1-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — Girondins Bordeaux x AS Saint-Etienne: base 1-2, RSSSF 1-0
- placar diferente na matriz da RSSSF — Girondins Bordeaux x FC Sochaux: base 4-1, RSSSF 1-2
- placar diferente na matriz da RSSSF — Girondins Bordeaux x RC Strasbourg: base 2-0, RSSSF 4-1
- placar diferente na matriz da RSSSF — SM Caen x RC Lens: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — SM Caen x Lille OSC: base 2-3, RSSSF 1-0
- placar diferente na matriz da RSSSF — SM Caen x Olympique Lyon: base 1-0, RSSSF 2-3
- placar diferente na matriz da RSSSF — SM Caen x FC Martigues: base 4-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — SM Caen x FC Metz: base 1-1, RSSSF 4-1
- placar diferente na matriz da RSSSF — SM Caen x AS Monaco: base 0-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — SM Caen x Montpellier HSC: base 0-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — SM Caen x Paris Saint-Germain: base 0-2, RSSSF 0-0
- placar diferente na matriz da RSSSF — SM Caen x AS Saint-Etienne: base 1-0, RSSSF 0-2
- placar diferente na matriz da RSSSF — SM Caen x FC Sochaux: base 2-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — SM Caen x RC Strasbourg: base 3-1, RSSSF 2-1
- placar diferente na matriz da RSSSF — SM Caen x Toulouse FC: base 1-0, RSSSF 3-1
- placar diferente na matriz da RSSSF — AS Cannes x RC Lens: base 3-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — AS Cannes x Lille OSC: base 2-1, RSSSF 3-1
- placar diferente na matriz da RSSSF — AS Cannes x Olympique Lyon: base 1-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — AS Cannes x Olympique Marseille: base 2-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — AS Cannes x FC Metz: base 2-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — AS Cannes x AS Monaco: base 0-2, RSSSF 2-0
- placar diferente na matriz da RSSSF — AS Cannes x Montpellier HSC: base 2-0, RSSSF 0-2
- placar diferente na matriz da RSSSF — AS Cannes x FC Nantes: base 4-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — AS Cannes x Paris Saint-Germain: base 0-1, RSSSF 4-0
- placar diferente na matriz da RSSSF — AS Cannes x AS Saint-Etienne: base 0-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — AS Cannes x FC Sochaux: base 1-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — AS Cannes x Toulouse FC: base 2-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — RC Lens x Olympique Lyon: base 2-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — RC Lens x Olympique Marseille: base 2-3, RSSSF 2-0
- placar diferente na matriz da RSSSF — RC Lens x FC Martigues: base 1-1, RSSSF 2-3
- placar diferente na matriz da RSSSF — RC Lens x FC Metz: base 2-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — RC Lens x AS Monaco: base 3-3, RSSSF 2-0
- placar diferente na matriz da RSSSF — RC Lens x Montpellier HSC: base 2-1, RSSSF 3-3
- placar diferente na matriz da RSSSF — RC Lens x FC Nantes: base 1-1, RSSSF 2-1
- placar diferente na matriz da RSSSF — RC Lens x Paris Saint-Germain: base 1-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — RC Lens x AS Saint-Etienne: base 3-1, RSSSF 1-2
- placar diferente na matriz da RSSSF — RC Lens x FC Sochaux: base 2-0, RSSSF 3-1
- placar diferente na matriz da RSSSF — RC Lens x RC Strasbourg: base 0-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — RC Lens x Toulouse FC: base 4-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — Lille OSC x RC Lens: base 0-0, RSSSF 2-2
- placar diferente na matriz da RSSSF — Lille OSC x Olympique Marseille: base 1-2, RSSSF 2-1
- placar diferente na matriz da RSSSF — Lille OSC x FC Martigues: base 1-1, RSSSF 1-2
- placar diferente na matriz da RSSSF — Lille OSC x FC Metz: base 0-4, RSSSF 1-1
- placar diferente na matriz da RSSSF — Lille OSC x AS Monaco: base 1-1, RSSSF 0-4
- placar diferente na matriz da RSSSF — Lille OSC x Montpellier HSC: base 0-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Lille OSC x Paris Saint-Germain: base 0-2, RSSSF 0-0
- placar diferente na matriz da RSSSF — Lille OSC x FC Sochaux: base 3-1, RSSSF 0-2
- placar diferente na matriz da RSSSF — Lille OSC x RC Strasbourg: base 1-1, RSSSF 3-1
- placar diferente na matriz da RSSSF — Lille OSC x Toulouse FC: base 3-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Olympique Lyon x RC Lens: base 1-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — Olympique Lyon x Lille OSC: base 0-0, RSSSF 1-2
- placar diferente na matriz da RSSSF — Olympique Lyon x FC Martigues: base 0-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — Olympique Lyon x FC Metz: base 2-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — Olympique Lyon x AS Monaco: base 1-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — Olympique Lyon x Montpellier HSC: base 3-2, RSSSF 1-0
- placar diferente na matriz da RSSSF — Olympique Lyon x FC Nantes: base 2-1, RSSSF 3-2
- placar diferente na matriz da RSSSF — Olympique Lyon x Paris Saint-Germain: base 1-3, RSSSF 2-1
- placar diferente na matriz da RSSSF — Olympique Lyon x AS Saint-Etienne: base 1-0, RSSSF 1-3
- placar diferente na matriz da RSSSF — Olympique Lyon x RC Strasbourg: base 2-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Olympique Lyon x Toulouse FC: base 1-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — Olympique Marseille x RC Lens: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Olympique Marseille x Lille OSC: base 3-2, RSSSF 1-0
- placar diferente na matriz da RSSSF — Olympique Marseille x Olympique Lyon: base 3-0, RSSSF 3-2
- placar diferente na matriz da RSSSF — Olympique Marseille x FC Metz: base 0-3, RSSSF 0-0
- placar diferente na matriz da RSSSF — Olympique Marseille x AS Monaco: base 2-1, RSSSF 0-3
- placar diferente na matriz da RSSSF — Olympique Marseille x Montpellier HSC: base 1-1, RSSSF 2-1
- placar diferente na matriz da RSSSF — Olympique Marseille x FC Nantes: base 3-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — Olympique Marseille x Paris Saint-Germain: base 1-0, RSSSF 3-1
- placar diferente na matriz da RSSSF — Olympique Marseille x AS Saint-Etienne: base 3-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Olympique Marseille x FC Sochaux: base 1-1, RSSSF 3-1
- placar diferente na matriz da RSSSF — Olympique Marseille x RC Strasbourg: base 2-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — Olympique Marseille x Toulouse FC: base 5-1, RSSSF 2-1
- placar diferente na matriz da RSSSF — FC Martigues x RC Lens: base 1-2, RSSSF 3-0
- placar diferente na matriz da RSSSF — FC Martigues x Lille OSC: base 2-2, RSSSF 1-2
- placar diferente na matriz da RSSSF — FC Martigues x Olympique Lyon: base 0-1, RSSSF 2-2
- placar diferente na matriz da RSSSF — FC Martigues x Olympique Marseille: base 0-3, RSSSF 0-1
- placar diferente na matriz da RSSSF — FC Martigues x AS Monaco: base 1-3, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Martigues x Montpellier HSC: base 1-1, RSSSF 1-3
- placar diferente na matriz da RSSSF — FC Martigues x FC Nantes: base 1-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Martigues x Paris Saint-Germain: base 1-1, RSSSF 1-2
- placar diferente na matriz da RSSSF — FC Martigues x AS Saint-Etienne: base 2-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Martigues x FC Sochaux: base 1-1, RSSSF 2-1
- placar diferente na matriz da RSSSF — FC Martigues x RC Strasbourg: base 0-3, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Martigues x Toulouse FC: base 1-1, RSSSF 0-3
- placar diferente na matriz da RSSSF — FC Metz x RC Lens: base 2-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — FC Metz x Lille OSC: base 1-1, RSSSF 2-1
- placar diferente na matriz da RSSSF — FC Metz x Olympique Lyon: base 0-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Metz x Olympique Marseille: base 0-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — FC Metz x FC Nantes: base 2-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Metz x Paris Saint-Germain: base 0-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — FC Metz x FC Sochaux: base 1-1, RSSSF 0-1
- placar diferente na matriz da RSSSF — FC Metz x RC Strasbourg: base 2-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Metz x Toulouse FC: base 1-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — AS Monaco x RC Lens: base 0-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — AS Monaco x Lille OSC: base 1-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — AS Monaco x Olympique Lyon: base 1-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — AS Monaco x Olympique Marseille: base 0-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — AS Monaco x FC Martigues: base 7-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — AS Monaco x FC Metz: base 1-1, RSSSF 7-0
- placar diferente na matriz da RSSSF — AS Monaco x FC Nantes: base 1-0, RSSSF 1-2
- placar diferente na matriz da RSSSF — AS Monaco x Paris Saint-Germain: base 1-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — AS Monaco x FC Sochaux: base 2-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — AS Monaco x RC Strasbourg: base 2-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — AS Monaco x Toulouse FC: base 3-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — Montpellier HSC x RC Lens: base 0-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — Montpellier HSC x Lille OSC: base 1-3, RSSSF 0-0
- placar diferente na matriz da RSSSF — Montpellier HSC x Olympique Lyon: base 1-1, RSSSF 1-3
- placar diferente na matriz da RSSSF — Montpellier HSC x Olympique Marseille: base 0-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — Montpellier HSC x FC Martigues: base 1-0, RSSSF 0-2
- placar diferente na matriz da RSSSF — Montpellier HSC x FC Metz: base 3-2, RSSSF 1-0
- placar diferente na matriz da RSSSF — Montpellier HSC x AS Monaco: base 0-3, RSSSF 3-2
- placar diferente na matriz da RSSSF — Montpellier HSC x Paris Saint-Germain: base 0-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — Montpellier HSC x AS Saint-Etienne: base 3-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — Montpellier HSC x FC Sochaux: base 1-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — Montpellier HSC x RC Strasbourg: base 4-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — Montpellier HSC x Toulouse FC: base 3-1, RSSSF 4-0
- placar diferente na matriz da RSSSF — FC Nantes x RC Lens: base 2-1, RSSSF 3-1
- placar diferente na matriz da RSSSF — FC Nantes x Lille OSC: base 2-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — FC Nantes x Olympique Lyon: base 1-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — FC Nantes x Olympique Marseille: base 0-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — FC Nantes x FC Martigues: base 2-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — FC Nantes x FC Metz: base 2-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — FC Nantes x AS Monaco: base 1-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — FC Nantes x Montpellier HSC: base 0-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — FC Nantes x AS Saint-Etienne: base 1-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — FC Nantes x FC Sochaux: base 2-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — FC Nantes x RC Strasbourg: base 2-2, RSSSF 2-0
- placar diferente na matriz da RSSSF — FC Nantes x Toulouse FC: base 4-0, RSSSF 2-2
- placar diferente na matriz da RSSSF — Paris Saint-Germain x RC Lens: base 1-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x Lille OSC: base 2-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x Olympique Lyon: base 0-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — Paris Saint-Germain x Olympique Marseille: base 1-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x FC Martigues: base 2-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — Paris Saint-Germain x FC Metz: base 1-0, RSSSF 2-2
- placar diferente na matriz da RSSSF — Paris Saint-Germain x AS Monaco: base 1-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x Montpellier HSC: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Paris Saint-Germain x RC Strasbourg: base 2-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x Toulouse FC: base 1-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — AS Saint-Etienne x Lille OSC: base 2-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — AS Saint-Etienne x Olympique Lyon: base 3-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — AS Saint-Etienne x Olympique Marseille: base 0-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — AS Saint-Etienne x FC Martigues: base 1-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — AS Saint-Etienne x FC Metz: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — AS Saint-Etienne x AS Monaco: base 2-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — AS Saint-Etienne x FC Nantes: base 1-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — AS Saint-Etienne x Paris Saint-Germain: base 1-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — AS Saint-Etienne x Toulouse FC: base 2-2, RSSSF 0-0
- placar diferente na matriz da RSSSF — FC Sochaux x RC Lens: base 1-1, RSSSF 4-2
- placar diferente na matriz da RSSSF — FC Sochaux x Lille OSC: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Sochaux x Olympique Lyon: base 0-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — FC Sochaux x Olympique Marseille: base 1-1, RSSSF 0-1
- placar diferente na matriz da RSSSF — FC Sochaux x FC Martigues: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Sochaux x FC Metz: base 2-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — FC Sochaux x AS Monaco: base 2-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — FC Sochaux x Montpellier HSC: base 2-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — FC Sochaux x FC Nantes: base 1-1, RSSSF 2-1
- placar diferente na matriz da RSSSF — FC Sochaux x Paris Saint-Germain: base 1-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Sochaux x AS Saint-Etienne: base 3-2, RSSSF 1-2
- placar diferente na matriz da RSSSF — FC Sochaux x Toulouse FC: base 0-0, RSSSF 1-3
- placar diferente na matriz da RSSSF — RC Strasbourg x RC Lens: base 2-0, RSSSF 0-3
- placar diferente na matriz da RSSSF — RC Strasbourg x Lille OSC: base 1-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — RC Strasbourg x Olympique Lyon: base 0-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — RC Strasbourg x Olympique Marseille: base 1-1, RSSSF 0-1
- placar diferente na matriz da RSSSF — RC Strasbourg x FC Martigues: base 3-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — RC Strasbourg x FC Metz: base 0-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — RC Strasbourg x AS Monaco: base 1-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — RC Strasbourg x Montpellier HSC: base 0-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — RC Strasbourg x FC Nantes: base 0-3, RSSSF 0-1
- placar diferente na matriz da RSSSF — RC Strasbourg x Paris Saint-Germain: base 2-2, RSSSF 0-3
- placar diferente na matriz da RSSSF — RC Strasbourg x AS Saint-Etienne: base 2-0, RSSSF 2-2
- placar diferente na matriz da RSSSF — Toulouse FC x RC Lens: base 1-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — Toulouse FC x Olympique Lyon: base 2-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Toulouse FC x Olympique Marseille: base 0-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — Toulouse FC x FC Martigues: base 2-2, RSSSF 0-0
- placar diferente na matriz da RSSSF — Toulouse FC x AS Monaco: base 2-1, RSSSF 2-2
- placar diferente na matriz da RSSSF — Toulouse FC x Montpellier HSC: base 0-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — Toulouse FC x FC Nantes: base 0-3, RSSSF 0-0
- placar diferente na matriz da RSSSF — Toulouse FC x Paris Saint-Germain: base 1-2, RSSSF 0-3
- placar diferente na matriz da RSSSF — Toulouse FC x FC Sochaux: base 3-2, RSSSF 1-2
- placar diferente na matriz da RSSSF — Toulouse FC x RC Strasbourg: base 0-0, RSSSF 3-2

### 1994/95

- o engsoccerdata não traz esta temporada
- a base não fecha nesta temporada (0 jogos): montada pelo calendário do ogol (380 jogos), com 0 jogos da base
- 380 jogos só no ogol, que entram com o placar do ogol: Girondins Bordeaux 1-0 OGC Nice (1994-07-28); FC Sochaux 2-0 SM Caen (1994-07-29); AS Monaco 0-1 FC Metz (1994-07-29); AS Cannes 0-0 SC Bastia (1994-07-29); FC Nantes 1-1 Olympique Lyon (1994-07-29); RC Strasbourg 1-1 AJ Auxerre (1994-07-29) ...
- placar diferente no football-data — AS Saint-Etienne x Girondins Bordeaux: base 2-1, football-data 4-1
- placar diferente na matriz da RSSSF — AJ Auxerre x RC Lens: base 3-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — AJ Auxerre x Lille OSC: base 2-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — AJ Auxerre x Olympique Lyon: base 0-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — AJ Auxerre x FC Martigues: base 3-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — AJ Auxerre x FC Metz: base 1-1, RSSSF 3-0
- placar diferente na matriz da RSSSF — AJ Auxerre x AS Monaco: base 2-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — AJ Auxerre x Montpellier HSC: base 0-1, RSSSF 2-2
- placar diferente na matriz da RSSSF — AJ Auxerre x FC Nantes: base 1-2, RSSSF 0-1
- placar diferente na matriz da RSSSF — AJ Auxerre x OGC Nice: base 3-0, RSSSF 1-2
- placar diferente na matriz da RSSSF — AJ Auxerre x Paris Saint-Germain: base 1-1, RSSSF 3-0
- placar diferente na matriz da RSSSF — AJ Auxerre x Stade Rennes: base 2-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — AJ Auxerre x AS Saint-Etienne: base 3-0, RSSSF 2-2
- placar diferente na matriz da RSSSF — AJ Auxerre x FC Sochaux: base 4-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — AJ Auxerre x RC Strasbourg: base 1-0, RSSSF 4-0
- placar diferente na matriz da RSSSF — SC Bastia x RC Lens: base 1-3, RSSSF 3-2
- placar diferente na matriz da RSSSF — SC Bastia x Lille OSC: base 3-1, RSSSF 1-3
- placar diferente na matriz da RSSSF — SC Bastia x Olympique Lyon: base 0-1, RSSSF 3-1
- placar diferente na matriz da RSSSF — SC Bastia x FC Martigues: base 2-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — SC Bastia x FC Metz: base 0-3, RSSSF 2-0
- placar diferente na matriz da RSSSF — SC Bastia x AS Monaco: base 0-2, RSSSF 0-3
- placar diferente na matriz da RSSSF — SC Bastia x Montpellier HSC: base 1-1, RSSSF 0-2
- placar diferente na matriz da RSSSF — SC Bastia x FC Nantes: base 2-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — SC Bastia x OGC Nice: base 1-1, RSSSF 2-2
- placar diferente na matriz da RSSSF — SC Bastia x Paris Saint-Germain: base 1-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — SC Bastia x AS Saint-Etienne: base 2-1, RSSSF 1-2
- placar diferente na matriz da RSSSF — SC Bastia x FC Sochaux: base 1-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — SC Bastia x RC Strasbourg: base 0-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Girondins Bordeaux x RC Lens: base 1-2, RSSSF 0-1
- placar diferente na matriz da RSSSF — Girondins Bordeaux x Lille OSC: base 1-0, RSSSF 1-2
- placar diferente na matriz da RSSSF — Girondins Bordeaux x Olympique Lyon: base 1-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Girondins Bordeaux x FC Metz: base 4-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — Girondins Bordeaux x AS Monaco: base 0-3, RSSSF 4-2
- placar diferente na matriz da RSSSF — Girondins Bordeaux x Montpellier HSC: base 2-0, RSSSF 0-3
- placar diferente na matriz da RSSSF — Girondins Bordeaux x FC Nantes: base 1-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — Girondins Bordeaux x OGC Nice: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Girondins Bordeaux x Paris Saint-Germain: base 3-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — Girondins Bordeaux x Stade Rennes: base 2-1, RSSSF 3-0
- placar diferente na matriz da RSSSF — Girondins Bordeaux x RC Strasbourg: base 2-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — SM Caen x RC Lens: base 0-0, RSSSF 2-2
- placar diferente na matriz da RSSSF — SM Caen x Lille OSC: base 2-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — SM Caen x Olympique Lyon: base 0-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — SM Caen x FC Metz: base 2-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — SM Caen x AS Monaco: base 0-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — SM Caen x Montpellier HSC: base 1-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — SM Caen x FC Nantes: base 0-2, RSSSF 1-0
- placar diferente na matriz da RSSSF — SM Caen x OGC Nice: base 0-0, RSSSF 0-2
- placar diferente na matriz da RSSSF — SM Caen x Paris Saint-Germain: base 1-2, RSSSF 0-0
- placar diferente na matriz da RSSSF — SM Caen x Stade Rennes: base 5-1, RSSSF 1-2
- placar diferente na matriz da RSSSF — SM Caen x AS Saint-Etienne: base 3-0, RSSSF 5-1
- placar diferente na matriz da RSSSF — SM Caen x FC Sochaux: base 3-1, RSSSF 3-0
- placar diferente na matriz da RSSSF — SM Caen x RC Strasbourg: base 4-0, RSSSF 3-1
- placar diferente na matriz da RSSSF — AS Cannes x RC Lens: base 2-0, RSSSF 2-2
- placar diferente na matriz da RSSSF — AS Cannes x Lille OSC: base 0-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — AS Cannes x Olympique Lyon: base 5-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — AS Cannes x FC Martigues: base 0-1, RSSSF 5-1
- placar diferente na matriz da RSSSF — AS Cannes x FC Metz: base 1-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — AS Cannes x AS Monaco: base 2-2, RSSSF 1-0
- placar diferente na matriz da RSSSF — AS Cannes x Montpellier HSC: base 3-0, RSSSF 2-2
- placar diferente na matriz da RSSSF — AS Cannes x FC Nantes: base 0-1, RSSSF 3-0
- placar diferente na matriz da RSSSF — AS Cannes x OGC Nice: base 2-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — AS Cannes x Paris Saint-Germain: base 3-2, RSSSF 2-0
- placar diferente na matriz da RSSSF — AS Cannes x Stade Rennes: base 0-1, RSSSF 3-2
- placar diferente na matriz da RSSSF — AS Cannes x AS Saint-Etienne: base 4-1, RSSSF 0-1
- placar diferente na matriz da RSSSF — AS Cannes x FC Sochaux: base 0-0, RSSSF 4-1
- placar diferente na matriz da RSSSF — AS Cannes x RC Strasbourg: base 2-2, RSSSF 0-0
- placar diferente na matriz da RSSSF — RC Lens x Olympique Lyon: base 4-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — RC Lens x FC Martigues: base 2-1, RSSSF 4-0
- placar diferente na matriz da RSSSF — RC Lens x FC Metz: base 2-2, RSSSF 2-1
- placar diferente na matriz da RSSSF — RC Lens x AS Monaco: base 0-0, RSSSF 2-2
- placar diferente na matriz da RSSSF — RC Lens x Montpellier HSC: base 1-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — RC Lens x OGC Nice: base 2-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — RC Lens x Paris Saint-Germain: base 1-2, RSSSF 2-1
- placar diferente na matriz da RSSSF — RC Lens x Stade Rennes: base 5-0, RSSSF 1-2
- placar diferente na matriz da RSSSF — RC Lens x AS Saint-Etienne: base 0-0, RSSSF 5-0
- placar diferente na matriz da RSSSF — RC Lens x FC Sochaux: base 1-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — Lille OSC x RC Lens: base 3-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — Lille OSC x FC Martigues: base 1-0, RSSSF 1-4
- placar diferente na matriz da RSSSF — Lille OSC x Montpellier HSC: base 0-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — Lille OSC x FC Nantes: base 1-2, RSSSF 0-0
- placar diferente na matriz da RSSSF — Lille OSC x OGC Nice: base 1-0, RSSSF 1-2
- placar diferente na matriz da RSSSF — Olympique Lyon x RC Lens: base 1-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — Olympique Lyon x Lille OSC: base 3-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — Olympique Lyon x FC Metz: base 1-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — Olympique Lyon x AS Monaco: base 3-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Olympique Lyon x Montpellier HSC: base 2-1, RSSSF 3-1
- placar diferente na matriz da RSSSF — Olympique Lyon x FC Nantes: base 1-1, RSSSF 2-1
- placar diferente na matriz da RSSSF — Olympique Lyon x Paris Saint-Germain: base 2-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Olympique Lyon x Stade Rennes: base 3-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — Olympique Lyon x AS Saint-Etienne: base 1-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — Olympique Lyon x FC Sochaux: base 4-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — Olympique Lyon x RC Strasbourg: base 1-0, RSSSF 4-0
- placar diferente na matriz da RSSSF — FC Martigues x RC Lens: base 0-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — FC Martigues x Lille OSC: base 1-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — FC Martigues x Olympique Lyon: base 2-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — FC Martigues x Montpellier HSC: base 2-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Martigues x FC Nantes: base 3-3, RSSSF 2-1
- placar diferente na matriz da RSSSF — FC Martigues x OGC Nice: base 0-1, RSSSF 3-3
- placar diferente na matriz da RSSSF — FC Martigues x Paris Saint-Germain: base 1-1, RSSSF 0-1
- placar diferente na matriz da RSSSF — FC Martigues x Stade Rennes: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Martigues x AS Saint-Etienne: base 1-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — FC Martigues x FC Sochaux: base 2-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Martigues x RC Strasbourg: base 0-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — FC Metz x RC Lens: base 3-1, RSSSF 2-1
- placar diferente na matriz da RSSSF — FC Metz x Lille OSC: base 1-1, RSSSF 3-1
- placar diferente na matriz da RSSSF — FC Metz x Olympique Lyon: base 2-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Metz x FC Martigues: base 0-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — FC Metz x Montpellier HSC: base 0-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — FC Metz x FC Nantes: base 0-2, RSSSF 0-0
- placar diferente na matriz da RSSSF — FC Metz x OGC Nice: base 0-0, RSSSF 0-2
- placar diferente na matriz da RSSSF — FC Metz x Paris Saint-Germain: base 2-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — FC Metz x Stade Rennes: base 1-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — FC Metz x FC Sochaux: base 3-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — FC Metz x RC Strasbourg: base 3-2, RSSSF 3-0
- placar diferente na matriz da RSSSF — AS Monaco x RC Lens: base 6-0, RSSSF 1-2
- placar diferente na matriz da RSSSF — AS Monaco x Lille OSC: base 2-0, RSSSF 6-0
- placar diferente na matriz da RSSSF — AS Monaco x Olympique Lyon: base 1-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — AS Monaco x FC Martigues: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — AS Monaco x FC Metz: base 0-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — AS Monaco x FC Nantes: base 2-2, RSSSF 2-0
- placar diferente na matriz da RSSSF — AS Monaco x OGC Nice: base 0-2, RSSSF 2-2
- placar diferente na matriz da RSSSF — AS Monaco x Paris Saint-Germain: base 2-1, RSSSF 0-2
- placar diferente na matriz da RSSSF — AS Monaco x Stade Rennes: base 0-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — AS Monaco x FC Sochaux: base 3-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — Montpellier HSC x RC Lens: base 1-2, RSSSF 2-1
- placar diferente na matriz da RSSSF — Montpellier HSC x Lille OSC: base 1-0, RSSSF 1-2
- placar diferente na matriz da RSSSF — Montpellier HSC x Olympique Lyon: base 2-2, RSSSF 1-0
- placar diferente na matriz da RSSSF — Montpellier HSC x FC Martigues: base 0-1, RSSSF 2-2
- placar diferente na matriz da RSSSF — Montpellier HSC x FC Metz: base 2-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — Montpellier HSC x AS Monaco: base 2-2, RSSSF 2-0
- placar diferente na matriz da RSSSF — Montpellier HSC x OGC Nice: base 0-0, RSSSF 2-2
- placar diferente na matriz da RSSSF — Montpellier HSC x Paris Saint-Germain: base 0-3, RSSSF 0-0
- placar diferente na matriz da RSSSF — Montpellier HSC x Stade Rennes: base 0-1, RSSSF 0-3
- placar diferente na matriz da RSSSF — Montpellier HSC x AS Saint-Etienne: base 3-2, RSSSF 0-1
- placar diferente na matriz da RSSSF — Montpellier HSC x FC Sochaux: base 1-0, RSSSF 3-2
- placar diferente na matriz da RSSSF — Montpellier HSC x RC Strasbourg: base 1-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — FC Nantes x RC Lens: base 3-0, RSSSF 3-2
- placar diferente na matriz da RSSSF — FC Nantes x Olympique Lyon: base 1-1, RSSSF 3-0
- placar diferente na matriz da RSSSF — FC Nantes x FC Martigues: base 3-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Nantes x FC Metz: base 3-1, RSSSF 3-0
- placar diferente na matriz da RSSSF — FC Nantes x AS Monaco: base 3-3, RSSSF 3-1
- placar diferente na matriz da RSSSF — FC Nantes x Montpellier HSC: base 3-2, RSSSF 3-3
- placar diferente na matriz da RSSSF — FC Nantes x Paris Saint-Germain: base 1-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — FC Nantes x Stade Rennes: base 2-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — FC Nantes x AS Saint-Etienne: base 3-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — FC Nantes x FC Sochaux: base 2-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — FC Nantes x RC Strasbourg: base 3-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — OGC Nice x RC Lens: base 1-1, RSSSF 0-2
- placar diferente na matriz da RSSSF — OGC Nice x Lille OSC: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — OGC Nice x Olympique Lyon: base 1-2, RSSSF 1-0
- placar diferente na matriz da RSSSF — OGC Nice x FC Martigues: base 1-1, RSSSF 1-2
- placar diferente na matriz da RSSSF — OGC Nice x FC Metz: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — OGC Nice x AS Monaco: base 3-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — OGC Nice x Montpellier HSC: base 0-0, RSSSF 3-1
- placar diferente na matriz da RSSSF — OGC Nice x FC Nantes: base 1-3, RSSSF 0-0
- placar diferente na matriz da RSSSF — OGC Nice x Stade Rennes: base 1-0, RSSSF 0-4
- placar diferente na matriz da RSSSF — OGC Nice x AS Saint-Etienne: base 3-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — OGC Nice x FC Sochaux: base 1-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — OGC Nice x RC Strasbourg: base 3-4, RSSSF 1-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x RC Lens: base 1-0, RSSSF 2-2
- placar diferente na matriz da RSSSF — Paris Saint-Germain x Lille OSC: base 3-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x Olympique Lyon: base 4-1, RSSSF 3-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x FC Martigues: base 3-0, RSSSF 4-1
- placar diferente na matriz da RSSSF — Paris Saint-Germain x AS Monaco: base 1-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x Montpellier HSC: base 3-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x FC Nantes: base 0-3, RSSSF 3-1
- placar diferente na matriz da RSSSF — Paris Saint-Germain x OGC Nice: base 2-3, RSSSF 0-3
- placar diferente na matriz da RSSSF — Paris Saint-Germain x AS Saint-Etienne: base 1-0, RSSSF 2-1
- placar diferente na matriz da RSSSF — Paris Saint-Germain x FC Sochaux: base 1-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Paris Saint-Germain x RC Strasbourg: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Stade Rennes x RC Lens: base 0-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — Stade Rennes x Lille OSC: base 1-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — Stade Rennes x Olympique Lyon: base 1-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Stade Rennes x FC Martigues: base 5-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — Stade Rennes x FC Metz: base 1-2, RSSSF 5-1
- placar diferente na matriz da RSSSF — Stade Rennes x AS Monaco: base 1-3, RSSSF 1-2
- placar diferente na matriz da RSSSF — Stade Rennes x Montpellier HSC: base 2-2, RSSSF 1-3
- placar diferente na matriz da RSSSF — Stade Rennes x FC Nantes: base 1-1, RSSSF 2-2
- placar diferente na matriz da RSSSF — Stade Rennes x OGC Nice: base 3-1, RSSSF 1-1
- placar diferente na matriz da RSSSF — Stade Rennes x Paris Saint-Germain: base 4-0, RSSSF 3-1
- placar diferente na matriz da RSSSF — Stade Rennes x FC Sochaux: base 2-1, RSSSF 2-2
- placar diferente na matriz da RSSSF — Stade Rennes x RC Strasbourg: base 1-1, RSSSF 2-1
- placar diferente na matriz da RSSSF — AS Saint-Etienne x RC Lens: base 1-2, RSSSF 4-1
- placar diferente na matriz da RSSSF — AS Saint-Etienne x Lille OSC: base 3-3, RSSSF 1-2
- placar diferente na matriz da RSSSF — AS Saint-Etienne x Olympique Lyon: base 1-1, RSSSF 3-3
- placar diferente na matriz da RSSSF — AS Saint-Etienne x FC Martigues: base 3-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — AS Saint-Etienne x FC Metz: base 0-1, RSSSF 3-0
- placar diferente na matriz da RSSSF — AS Saint-Etienne x AS Monaco: base 1-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — AS Saint-Etienne x Montpellier HSC: base 4-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — AS Saint-Etienne x FC Nantes: base 1-1, RSSSF 4-0
- placar diferente na matriz da RSSSF — AS Saint-Etienne x OGC Nice: base 3-3, RSSSF 1-1
- placar diferente na matriz da RSSSF — AS Saint-Etienne x Paris Saint-Germain: base 1-3, RSSSF 3-3
- placar diferente na matriz da RSSSF — AS Saint-Etienne x Stade Rennes: base 1-1, RSSSF 1-3
- placar diferente na matriz da RSSSF — AS Saint-Etienne x RC Strasbourg: base 2-0, RSSSF 4-0
- placar diferente na matriz da RSSSF — FC Sochaux x RC Lens: base 1-1, RSSSF 0-1
- placar diferente na matriz da RSSSF — FC Sochaux x Lille OSC: base 3-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Sochaux x Olympique Lyon: base 1-2, RSSSF 3-0
- placar diferente na matriz da RSSSF — FC Sochaux x FC Martigues: base 1-1, RSSSF 1-2
- placar diferente na matriz da RSSSF — FC Sochaux x FC Metz: base 4-2, RSSSF 1-1
- placar diferente na matriz da RSSSF — FC Sochaux x AS Monaco: base 0-5, RSSSF 4-2
- placar diferente na matriz da RSSSF — FC Sochaux x Montpellier HSC: base 2-0, RSSSF 0-5
- placar diferente na matriz da RSSSF — FC Sochaux x FC Nantes: base 0-0, RSSSF 2-0
- placar diferente na matriz da RSSSF — FC Sochaux x OGC Nice: base 0-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — FC Sochaux x Paris Saint-Germain: base 1-2, RSSSF 0-1
- placar diferente na matriz da RSSSF — FC Sochaux x Stade Rennes: base 1-3, RSSSF 1-2
- placar diferente na matriz da RSSSF — FC Sochaux x AS Saint-Etienne: base 2-0, RSSSF 1-3
- placar diferente na matriz da RSSSF — RC Strasbourg x RC Lens: base 0-0, RSSSF 3-0
- placar diferente na matriz da RSSSF — RC Strasbourg x Lille OSC: base 1-1, RSSSF 0-0
- placar diferente na matriz da RSSSF — RC Strasbourg x Olympique Lyon: base 1-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — RC Strasbourg x FC Martigues: base 5-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — RC Strasbourg x FC Metz: base 1-0, RSSSF 5-0
- placar diferente na matriz da RSSSF — RC Strasbourg x Montpellier HSC: base 0-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — RC Strasbourg x FC Nantes: base 2-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — RC Strasbourg x OGC Nice: base 3-2, RSSSF 2-0
- placar diferente na matriz da RSSSF — RC Strasbourg x Paris Saint-Germain: base 2-0, RSSSF 3-2
- placar diferente na matriz da RSSSF — RC Strasbourg x Stade Rennes: base 2-2, RSSSF 2-0
- placar diferente na matriz da RSSSF — RC Strasbourg x AS Saint-Etienne: base 1-1, RSSSF 2-2
- placar diferente na matriz da RSSSF — RC Strasbourg x FC Sochaux: base 3-2, RSSSF 1-1

### 1995/96

- sem ocorrências

### 1996/97

- data diferente no ogol em 39 jogos (ex.: SC Bastia x Stade Rennes: base 1996-08-11, ogol 1996-08-10); fica a da base
- placar diferente na matriz da RSSSF — AJ Auxerre x Stade Rennes: base 4-1, RSSSF 2-1
- placar diferente na matriz da RSSSF — AJ Auxerre x RC Strasbourg: base 0-1, RSSSF 4-1
- placar diferente na matriz da RSSSF — SC Bastia x Stade Rennes: base 2-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — SC Bastia x RC Strasbourg: base 3-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — Girondins Bordeaux x Stade Rennes: base 2-0, RSSSF 5-3
- placar diferente na matriz da RSSSF — Girondins Bordeaux x RC Strasbourg: base 1-2, RSSSF 2-0
- placar diferente na matriz da RSSSF — SM Caen x Stade Rennes: base 0-0, RSSSF 1-3
- placar diferente na matriz da RSSSF — SM Caen x RC Strasbourg: base 3-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — AS Cannes x Stade Rennes: base 1-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — AS Cannes x RC Strasbourg: base 2-2, RSSSF 1-0
- placar diferente na matriz da RSSSF — EA Guingamp x Stade Rennes: base 1-0, RSSSF 2-2
- placar diferente na matriz da RSSSF — EA Guingamp x RC Strasbourg: base 2-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Le Havre AC x Stade Rennes: base 1-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Le Havre AC x RC Strasbourg: base 2-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — RC Lens x Stade Rennes: base 2-0, RSSSF 1-2
- placar diferente na matriz da RSSSF — RC Lens x RC Strasbourg: base 1-2, RSSSF 2-0
- placar diferente na matriz da RSSSF — Lille OSC x Stade Rennes: base 3-1, RSSSF 0-1
- placar diferente na matriz da RSSSF — Lille OSC x RC Strasbourg: base 2-4, RSSSF 3-1
- placar diferente na matriz da RSSSF — Olympique Lyon x Stade Rennes: base 2-0, RSSSF 1-1
- placar diferente na matriz da RSSSF — Olympique Marseille x Stade Rennes: base 3-1, RSSSF 1-0
- placar diferente na matriz da RSSSF — Olympique Marseille x RC Strasbourg: base 0-1, RSSSF 3-1
- placar diferente na matriz da RSSSF — FC Metz x Stade Rennes: base 2-0, RSSSF 0-1
- placar diferente na matriz da RSSSF — FC Metz x RC Strasbourg: base 3-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — AS Monaco x Stade Rennes: base 3-1, RSSSF 2-0
- placar diferente na matriz da RSSSF — AS Monaco x RC Strasbourg: base 2-0, RSSSF 3-1
- placar diferente na matriz da RSSSF — Montpellier HSC x Stade Rennes: base 0-0, RSSSF 0-3
- placar diferente na matriz da RSSSF — Montpellier HSC x RC Strasbourg: base 1-4, RSSSF 0-0
- placar diferente na matriz da RSSSF — AS Nancy x Stade Rennes: base 1-0, RSSSF 0-0
- placar diferente na matriz da RSSSF — AS Nancy x RC Strasbourg: base 2-0, RSSSF 1-0
- placar diferente na matriz da RSSSF — FC Nantes x Stade Rennes: base 3-3, RSSSF 0-0
- placar diferente na matriz da RSSSF — FC Nantes x RC Strasbourg: base 3-0, RSSSF 3-3
- placar diferente na matriz da RSSSF — OGC Nice x Stade Rennes: base 3-1, RSSSF 0-1
- placar diferente na matriz da RSSSF — OGC Nice x RC Strasbourg: base 1-1, RSSSF 3-1
- placar diferente na matriz da RSSSF — RC Strasbourg x Stade Rennes: base 3-0, RSSSF 0-1

### 1997/98

- data diferente no ogol em 27 jogos (ex.: Toulouse FC x Stade Rennes: base 1997-08-01, ogol 1997-08-02); fica a da base

### 1998/99

- data diferente no ogol em 2 jogos (ex.: Stade Rennes x AJ Auxerre: base 1998-08-07, ogol 1998-08-08); fica a da base

### 1999/00

- sem ocorrências

### 2000/01

- resultado do tribunal: AS Saint-Etienne x Toulouse FC fica 0-0 com vitória do Toulouse (base 1-0) — o Saint-Étienne escalou jogador com passaporte falso: vitória dada ao Toulouse com 0-0 (RSSSF)
- resultado do tribunal: FC Metz x Stade Rennes fica 0-2 (base 2-2) — o Metz escalou o goleiro Mondragón irregularmente: 0-2 para o Rennes (RSSSF)
- placar diferente no football-data — AS Saint-Etienne x Toulouse FC: base 0-0, football-data 1-0
- placar diferente no football-data — FC Metz x Stade Rennes: base 0-2, football-data 2-2

### 2001/02

- ESPN com 305 de 306 jogos (ex. sem ESPN: Montpellier HSC x ESTAC Troyes, 2001-10-27)
- gols da ESPN não batem com o placar — AJ Auxerre 1-1 Paris Saint-Germain: ESPN 1-2 (descartados)
- gols da ESPN não batem com o placar — CS Sedan 1-1 RC Lens: ESPN 2-1 (descartados)
- gols da ESPN não batem com o placar — Lille OSC 2-3 AJ Auxerre: ESPN 2-4 (descartados)

### 2002/03

- gols da ESPN não batem com o placar — Paris Saint-Germain 2-0 Olympique Lyon: ESPN 3-0 (descartados)

### 2003/04

- data diferente no ogol em 1 jogos (ex.: Olympique Lyon x RC Strasbourg: base 2003-11-21, ogol 2003-11-22); fica a da base
- placar diferente na ESPN — Paris Saint-Germain x AS Monaco (2003-08-24): base 2-4, ESPN 3-4
- ESPN com 379 de 380 jogos (ex. sem ESPN: Girondins Bordeaux x FC Nantes, 2004-02-06)
- gols da ESPN não batem com o placar — Paris Saint-Germain 2-4 AS Monaco: ESPN 3-4 (descartados)

### 2004/05

- sem ocorrências

### 2005/06

- placar diferente na ESPN — Paris Saint-Germain x OGC Nice (2005-08-27): base 1-2, ESPN 1-4
- gols da ESPN não batem com o placar — Paris Saint-Germain 1-2 OGC Nice: ESPN 1-4 (descartados)

### 2006/07

- jogo acrescentado: FC Nantes 0-0 Toulouse FC (2007-05-19) — falta no engsoccerdata; o ogol o marca como W.O.: invasão de campo da torcida do Nantes, a liga deu a vitória ao Toulouse e manteve o 0-0 (RSSSF: "awarded 0-0 win to Toulouse"; a tabela da Wikipédia conta a vitória)
- placar diferente na ESPN — Girondins Bordeaux x Stade Rennes (2006-12-09): base 1-2, ESPN 0-1
- placar diferente na ESPN — Girondins Bordeaux x Lille OSC (2007-01-27): base 0-1, ESPN 0-0
- placar diferente na ESPN — FC Sochaux x FC Nantes (2007-03-04): base 1-2, ESPN 1-1
- gols da ESPN não batem com o placar — Paris Saint-Germain 4-2 CS Sedan: ESPN 4-3 (descartados)
- gols da ESPN não batem com o placar — FC Nantes 2-5 Valenciennes FC: ESPN 2-6 (descartados)

### 2007/08

- gols da ESPN não batem com o placar — SM Caen 1-0 OGC Nice: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Olympique Lyon 1-0 AS Nancy: ESPN 2-0 (descartados)

### 2008/09

- Le Havre: 1 ponto a menos; a RSSSF desconta, a Wikipédia não
- punição tirada da tabela da RSSSF: Le Havre -1 pontos
- tabela publicada x jogos (Wikipédia) — Le Havre AC tabela [38, 7, 5, 26, 30, 67, 26] jogos [38, 7, 5, 26, 30, 67, 25]
- a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF
- gols da ESPN não batem com o placar — Le Mans UC 72 2-0 AS Nancy: ESPN 3-0 (descartados)
- gols da ESPN não batem com o placar — AS Saint-Etienne 3-2 SM Caen: ESPN 3-3 (descartados)
- gols da ESPN não batem com o placar — Lille OSC 3-2 FC Sochaux: ESPN 4-2 (descartados)

### 2009/10

- ESPN com 379 de 380 jogos (ex. sem ESPN: Olympique Lyon x Grenoble Foot 38, 2010-03-27)
- gols da ESPN não batem com o placar — FC Sochaux 2-3 Girondins Bordeaux: ESPN 2-4 (descartados)
- gols da ESPN não batem com o placar — AS Monaco 1-2 AS Saint-Etienne: ESPN 2-4 (descartados)

### 2010/11

- data diferente no ogol em 1 jogos (ex.: AS Monaco x Girondins Bordeaux: base 2010-11-02, ogol 2010-10-31); fica a da base
- gols da ESPN não batem com o placar — Paris Saint-Germain 2-2 Montpellier HSC: ESPN 3-2 (descartados)
- gols da ESPN não batem com o placar — AS Nancy 4-0 RC Lens: ESPN 5-0 (descartados)

### 2011/12

- sem ocorrências

### 2012/13

- sem ocorrências

### 2013/14

- resultado do tribunal: FC Nantes x SC Bastia fica 0-0 com vitória do Bastia (base 0-0) — vitória dada ao Bastia com 0-0 (RSSSF: "awarded 0-0 win to Bastia; originally 2-0")
- placar diferente no football-data — FC Nantes x SC Bastia: base 0-0, football-data 2-0
- gols da ESPN não batem com o placar — Evian Thonon Gaillard 1-2 Stade Rennes: ESPN 2-2 (descartados)

### 2014/15

- sem ocorrências

### 2015/16

- sem ocorrências

### 2016/17

- resultado do tribunal: SC Bastia x Olympique Lyon fica 0-0 com vitória do Lyon (base 0-3) — abandonado no intervalo por invasão de campo; vitória dada ao Lyon com 0-0 (RSSSF; as tabelas não contam os gols)
- placar diferente no football-data — SC Bastia x Olympique Lyon: base 0-0, football-data 0-3
- ESPN com 379 de 380 jogos (ex. sem ESPN: SC Bastia x Olympique Lyon, 2017-04-16)

### 2017/18

- sem ocorrências

### 2018/19

- sem ocorrências

### 2019/20

- temporada interrompida em março de 2020 pela pandemia de covid-19 (279 de 380 jogos); a classificação final é pela média de pontos por jogo
- jogo do ogol sem par na base: Lyon ANU Stade de Reims (2020-03-13, R29)
- jogo do ogol sem par na base: Montpellier ANU Marseille (2020-03-14, R29)
- jogo do ogol sem par na base: Nantes ANU Nimes (2020-03-14, R29)
- jogo do ogol sem par na base: Toulouse ANU Metz (2020-03-14, R29)
- jogo do ogol sem par na base: Strasbourg ANU Dijon (2020-03-14, R29)
- jogo do ogol sem par na base: Amiens SC ANU Angers (2020-03-14, R29)
- jogo do ogol sem par na base: Brest ANU Lille (2020-03-14, R29)
- jogo do ogol sem par na base: Bordeaux ANU Rennes (2020-03-15, R29)
- jogo do ogol sem par na base: Monaco ANU Saint-Étienne (2020-03-15, R29)
- jogo do ogol sem par na base: PSG ANU Nice (2020-03-15, R29)
- jogo do ogol sem par na base: Strasbourg ANU PSG (2020-03-18, R28)
- jogo do ogol sem par na base: Lille ANU Monaco (2020-03-20, R30)
- jogo do ogol sem par na base: Rennes ANU Lyon (2020-03-21, R30)
- jogo do ogol sem par na base: Dijon ANU Amiens SC (2020-03-21, R30)
- jogo do ogol sem par na base: Metz ANU Brest (2020-03-21, R30)
- jogo do ogol sem par na base: Nice ANU Montpellier (2020-03-21, R30)
- jogo do ogol sem par na base: Nimes ANU Bordeaux (2020-03-21, R30)
- jogo do ogol sem par na base: Angers ANU Toulouse (2020-03-21, R30)
- jogo do ogol sem par na base: Saint-Étienne ANU Strasbourg (2020-03-22, R30)
- jogo do ogol sem par na base: Stade de Reims ANU Nantes (2020-03-22, R30)
- jogo do ogol sem par na base: Marseille ANU PSG (2020-03-22, R30)
- jogo do ogol sem par na base: Montpellier ANU Lille (2020-04-04, R31)
- jogo do ogol sem par na base: Toulouse ANU Saint-Étienne (2020-04-04, R31)
- jogo do ogol sem par na base: Lyon ANU Nimes (2020-04-05, R31)
- jogo do ogol sem par na base: PSG ANU Metz (2020-04-05, R31)
- jogo do ogol sem par na base: Monaco ANU Nantes (2020-04-05, R31)
- jogo do ogol sem par na base: Dijon ANU Nice (2020-04-05, R31)
- jogo do ogol sem par na base: Bordeaux ANU Stade de Reims (2020-04-05, R31)
- jogo do ogol sem par na base: Strasbourg ANU Angers (2020-04-05, R31)
- jogo do ogol sem par na base: Amiens SC ANU Rennes (2020-04-05, R31)
- jogo do ogol sem par na base: Brest ANU Marseille (2020-04-05, R31)
- jogo do ogol sem par na base: Saint-Étienne ANU Rennes (2020-04-11, R32)
- jogo do ogol sem par na base: Metz ANU Lille (2020-04-11, R32)
- jogo do ogol sem par na base: Nantes ANU Lyon (2020-04-11, R32)
- jogo do ogol sem par na base: Bordeaux ANU Amiens SC (2020-04-11, R32)
- jogo do ogol sem par na base: Nice ANU Strasbourg (2020-04-11, R32)
- jogo do ogol sem par na base: Marseille ANU Dijon (2020-04-11, R32)
- jogo do ogol sem par na base: Nimes ANU Montpellier (2020-04-11, R32)
- jogo do ogol sem par na base: Angers ANU PSG (2020-04-11, R32)
- jogo do ogol sem par na base: Brest ANU Monaco (2020-04-11, R32)
- jogo do ogol sem par na base: Stade de Reims ANU Toulouse (2020-04-11, R32)
- jogo do ogol sem par na base: Monaco ANU Bordeaux (2020-04-18, R33)
- jogo do ogol sem par na base: Dijon ANU Angers (2020-04-18, R33)
- jogo do ogol sem par na base: Toulouse ANU Nantes (2020-04-18, R33)
- jogo do ogol sem par na base: Montpellier ANU Stade de Reims (2020-04-18, R33)
- jogo do ogol sem par na base: Lille ANU Nice (2020-04-18, R33)
- jogo do ogol sem par na base: PSG ANU Saint-Étienne (2020-04-18, R33)
- jogo do ogol sem par na base: Strasbourg ANU Brest (2020-04-18, R33)
- jogo do ogol sem par na base: Amiens SC ANU Nimes (2020-04-18, R33)
- jogo do ogol sem par na base: Rennes ANU Metz (2020-04-18, R33)
- jogo do ogol sem par na base: Lyon ANU Marseille (2020-04-19, R33)
- jogo do ogol sem par na base: Saint-Étienne ANU Angers (2020-04-26, R34)
- jogo do ogol sem par na base: Metz ANU Dijon (2020-04-26, R34)
- jogo do ogol sem par na base: Nantes ANU Amiens SC (2020-04-26, R34)
- jogo do ogol sem par na base: Bordeaux ANU Toulouse (2020-04-26, R34)
- jogo do ogol sem par na base: Lyon ANU Monaco (2020-04-26, R34)
- jogo do ogol sem par na base: Marseille ANU Nice (2020-04-26, R34)
- jogo do ogol sem par na base: Nimes ANU Lille (2020-04-26, R34)
- jogo do ogol sem par na base: Brest ANU Montpellier (2020-04-26, R34)
- jogo do ogol sem par na base: Stade de Reims ANU PSG (2020-04-26, R34)
- jogo do ogol sem par na base: Rennes ANU Strasbourg (2020-04-26, R34)
- jogo do ogol sem par na base: Monaco ANU Metz (2020-05-02, R35)
- jogo do ogol sem par na base: Dijon ANU Lyon (2020-05-02, R35)
- jogo do ogol sem par na base: Toulouse ANU Nimes (2020-05-02, R35)
- jogo do ogol sem par na base: Montpellier ANU Bordeaux (2020-05-02, R35)
- jogo do ogol sem par na base: Nice ANU Nantes (2020-05-02, R35)
- jogo do ogol sem par na base: Lille ANU Stade de Reims (2020-05-02, R35)
- jogo do ogol sem par na base: PSG ANU Brest (2020-05-02, R35)
- jogo do ogol sem par na base: Strasbourg ANU Marseille (2020-05-02, R35)
- jogo do ogol sem par na base: Amiens SC ANU Saint-Étienne (2020-05-02, R35)
- jogo do ogol sem par na base: Angers ANU Rennes (2020-05-02, R35)
- jogo do ogol sem par na base: Metz ANU Nice (2020-05-09, R36)
- jogo do ogol sem par na base: Saint-Étienne ANU Lille (2020-05-09, R36)
- jogo do ogol sem par na base: Nantes ANU Brest (2020-05-09, R36)
- jogo do ogol sem par na base: Toulouse ANU PSG (2020-05-09, R36)
- jogo do ogol sem par na base: Bordeaux ANU Angers (2020-05-09, R36)
- jogo do ogol sem par na base: Marseille ANU Monaco (2020-05-09, R36)
- jogo do ogol sem par na base: Lyon ANU Montpellier (2020-05-09, R36)
- jogo do ogol sem par na base: Nimes ANU Strasbourg (2020-05-09, R36)
- jogo do ogol sem par na base: Stade de Reims ANU Amiens SC (2020-05-09, R36)
- jogo do ogol sem par na base: Rennes ANU Dijon (2020-05-09, R36)
- jogo do ogol sem par na base: Monaco ANU Toulouse (2020-05-16, R37)
- jogo do ogol sem par na base: Dijon ANU Stade de Reims (2020-05-16, R37)
- jogo do ogol sem par na base: Montpellier ANU Nantes (2020-05-16, R37)
- jogo do ogol sem par na base: Nice ANU Saint-Étienne (2020-05-16, R37)
- jogo do ogol sem par na base: Marseille ANU Metz (2020-05-16, R37)
- jogo do ogol sem par na base: Lille ANU Amiens SC (2020-05-16, R37)
- jogo do ogol sem par na base: PSG ANU Rennes (2020-05-16, R37)
- jogo do ogol sem par na base: Strasbourg ANU Bordeaux (2020-05-16, R37)
- jogo do ogol sem par na base: Angers ANU Lyon (2020-05-16, R37)
- jogo do ogol sem par na base: Brest ANU Nimes (2020-05-16, R37)
- jogo do ogol sem par na base: Saint-Étienne ANU Dijon (2020-05-23, R38)
- jogo do ogol sem par na base: Metz ANU Angers (2020-05-23, R38)
- jogo do ogol sem par na base: Nantes ANU Strasbourg (2020-05-23, R38)
- jogo do ogol sem par na base: Toulouse ANU Montpellier (2020-05-23, R38)
- jogo do ogol sem par na base: Bordeaux ANU Lille (2020-05-23, R38)
- jogo do ogol sem par na base: Nimes ANU PSG (2020-05-23, R38)
- jogo do ogol sem par na base: Lyon ANU Brest (2020-05-23, R38)
- jogo do ogol sem par na base: Amiens SC ANU Nice (2020-05-23, R38)
- jogo do ogol sem par na base: Stade de Reims ANU Marseille (2020-05-23, R38)
- jogo do ogol sem par na base: Rennes ANU Monaco (2020-05-23, R38)
- nenhum critério calculado reproduz a ordem oficial; o mais próximo (saldo) difere em 4 posições (ex.: ['OGC Nice', 'Stade Reims'])
- gols da ESPN não batem com o placar — Montpellier HSC 1-1 FC Metz: ESPN 2-2 (descartados)

### 2020/21

- sem ocorrências

### 2021/22

- sem ocorrências

### 2022/23

- sem ocorrências

### 2023/24

- nenhum critério calculado reproduz a ordem oficial; o mais próximo (confronto) difere em 2 posições (ex.: ['FC Metz', 'FC Lorient'])
- gols da ESPN não batem com o placar — Montpellier HSC 1-1 Clermont Foot 63: ESPN 5-3 (descartados)

### 2024/25

- sem ocorrências

### 2025/26

- o engsoccerdata não traz esta temporada
- a base não fecha nesta temporada (0 jogos): montada pelo calendário do ogol (306 jogos), com 0 jogos da base
- 306 jogos só no ogol, que entram com o placar do ogol: Stade Rennes 1-0 Olympique Marseille (2025-08-15); RC Lens 0-1 Olympique Lyon (2025-08-16); AS Monaco 3-1 Le Havre AC (2025-08-16); OGC Nice 0-1 Toulouse FC (2025-08-16); Stade Brest 3-3 Lille OSC (2025-08-17); AJ Auxerre 1-0 FC Lorient (2025-08-17) ...
- ESPN com 305 de 306 jogos (ex. sem ESPN: FC Nantes x Toulouse FC, 2026-05-17)

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_fra.py` (serve para todas as divisões francesas): nome de exibição como o clube é conhecido no Brasil ("PSG", "Olympique de Marseille", "Lyon", "Saint-Étienne"), cidade e país. O Monaco é de Mônaco (`MON`, em `paises.csv`). As grafias de época do engsoccerdata viram um clube só (Red Star; Racing Paris e Matra Racing; Montpellier La Paillade e Montpellier; Brest Armorique e Brest; Sedan; Valenciennes; Troyes; Cannes).
- ogol e ESPN são casados pelo código do clube, por votação jogo a jogo (mesma data e placar): 73 códigos do ogol e 41 da ESPN.
- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.

## O que não deu para coletar

- **Autores dos gols e cartões antes de 2001/02:** nenhuma fonte em lote traz.
- **Público e estádio antes de 2001/02:** nenhuma fonte em lote.
- **Barrages (jogos de acesso e rebaixamento contra clubes da 2ª divisão):** ficam de fora (entram com a 2ª divisão).
- **Campeonatos de guerra (1939/40-1944/45)** e os campeonatos amadores de antes de 1932: ficam de fora.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.
