# Campeonato Holandês (Eredivisie) — coleta de dados

Gerado por `python coleta/ned-1/importar.py`. Pacote em `data/coleta/ned-1/pacote/`.

**Edições:** 70, de 1956/57 a 2025/26 (Eredivisie). Os campeonatos holandeses de antes (ligas regionais com fase final, 1888/89-1953/54, e a Hoofdklasse profissional de 1954/55 e 1955/56) ficam de fora.

**Total:** 21082 jogos, 64928 gols, 23019 gols com autor (ESPN), 24431 cartões, 54 clubes.

**Fontes:**
- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1956/57-2024/25;
- football-data.co.uk: de 1993/94 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;
- ogol: rodada oficial de cada jogo e conferência de placar (só os jogos de rodada: os play-offs da mesma edição ficam de fora); base de 2025/26, que o engsoccerdata não traz; calendários guardados em `data/cache/ogol-ned-1/` para os escudos (com 2026/27, baixado só para saber quem caiu em 2025/26);
- ESPN (liga `ned.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;
- RSSSF: matriz de resultados e tabela final de 1956/57 a 2003/04 (conferência jogo a jogo), tabela final das temporadas seguintes, lista de campeões e de artilheiros (com o clube);
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições).

**Regras:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local (Amsterdã). Rebaixado = clube que não está na 1ª divisão na temporada seguinte (inclui quem caiu na nacompetitie). 2 pontos por vitória até 1994/95, 3 a partir de 1995/96. Placar diferente no ogol, no football-data ou na ESPN numa temporada em que as tabelas publicadas fecham com a base é erro da outra fonte e fica só anotado; quando a outra fonte e a tabela publicada concordam contra a base, o placar é corrigido (CORRECOES, TRIBUNAL e INVERTIDOS em `importar.py`, com o motivo).

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 18, saldo de gols em 52, média de gols em 0); é ele que ordena a classificação rodada a rodada.

| Temporada | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |
|---|---|---|---|---|---|---|---|---|
| 1956/57 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1139 | 0 | 2 / 0 | Ajax | — |
| 1957/58 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1135 | 0 | 2 / 0 | DOS Utrecht | — |
| 1958/59 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1188 | 0 | 2 / 0 | Sparta Rotterdam | — |
| 1959/60 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1132 | 0 | 2 / 0 | Ajax | — |
| 1960/61 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1083 | 0 | 2 / 0 | Feyenoord | — |
| 1961/62 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1075 | 0 | 2 / 0 | Feyenoord | — |
| 1962/63 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 822 | 0 | 2 / 0 | PSV | — |
| 1963/64 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 825 | 0 | 2 / 0 | DWS Amsterdam | — |
| 1964/65 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 681 | 0 | 2 / 0 | Feyenoord | — |
| 1965/66 | engsoccerdata + ogol + RSSSF + Wikipédia | 16 | 240 (240) | 779 | 0 | 2 / 0 | Ajax | — |
| 1966/67 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 963 | 0 | 2 / 0 | Ajax | — |
| 1967/68 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 880 | 0 | 2 / 0 | Ajax | — |
| 1968/69 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 797 | 0 | 2 / 0 | Feyenoord | — |
| 1969/70 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 820 | 0 | 2 / 0 | Ajax | — |
| 1970/71 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 809 | 0 | 2 / 0 | Feyenoord | — |
| 1971/72 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 812 | 0 | 2 / 0 | Ajax | — |
| 1972/73 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 849 | 0 | 2 / 0 | Ajax | — |
| 1973/74 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 907 | 0 | 2 / 0 | Feyenoord | — |
| 1974/75 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 875 | 0 | 2 / 0 | PSV | — |
| 1975/76 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 866 | 0 | 2 / 0 | PSV | — |
| 1976/77 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 862 | 0 | 2 / 0 | Ajax | — |
| 1977/78 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 899 | 0 | 2 / 0 | PSV | — |
| 1978/79 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 873 | 0 | 2 / 0 | Ajax | — |
| 1979/80 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 883 | 0 | 2 / 0 | Ajax | — |
| 1980/81 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1059 | 0 | 2 / 0 | AZ Alkmaar | — |
| 1981/82 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1014 | 0 | 2 / 0 | Ajax | — |
| 1982/83 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 965 | 0 | 2 / 0 | Ajax | — |
| 1983/84 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 1079 | 0 | 2 / 0 | Feyenoord | — |
| 1984/85 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 983 | 0 | 2 / 0 | Ajax | — |
| 1985/86 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 952 | 0 | 2 / 0 | PSV | — |
| 1986/87 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 917 | 0 | 2 / 0 | PSV | — |
| 1987/88 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 963 | 0 | 2 / 0 | PSV | — |
| 1988/89 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 906 | 0 | 2 / 0 | PSV | — |
| 1989/90 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 842 | 0 | 2 / 0 | Ajax | — |
| 1990/91 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 830 | 0 | 2 / 0 | PSV | — |
| 1991/92 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 831 | 0 | 2 / 0 | PSV | — |
| 1992/93 | engsoccerdata + ogol + RSSSF + Wikipédia | 18 | 306 (306) | 898 | 0 | 2 / 0 | Feyenoord | — |
| 1993/94 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 901 | 0 | 2 / 0 | Ajax | — |
| 1994/95 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 981 | 0 | 2 / 0 | Ajax | — |
| 1995/96 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 920 | 0 | 2 / 0 | Ajax | — |
| 1996/97 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 864 | 0 | 2 / 0 | PSV | — |
| 1997/98 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 1002 | 0 | 2 / 0 | Ajax | — |
| 1998/99 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 964 | 0 | 2 / 0 | Feyenoord | — |
| 1999/00 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 997 | 0 | 2 / 0 | PSV | — |
| 2000/01 | engsoccerdata + ogol + football-data + RSSSF + Wikipédia | 18 | 306 (306) | 922 | 0 | 2 / 0 | PSV | — |
| 2001/02 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 869 | 849 | 2 / 0 | Ajax | — |
| 2002/03 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 903 | 896 | 2 / 0 | PSV | — |
| 2003/04 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 911 | 899 | 2 / 0 | Ajax | — |
| 2004/05 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 948 | 948 | 2 / 0 | PSV | — |
| 2005/06 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 912 | 912 | 2 / 0 | PSV | — |
| 2006/07 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 915 | 899 | 2 / 0 | PSV | — |
| 2007/08 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 956 | 956 | 2 / 0 | PSV | — |
| 2008/09 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 870 | 857 | 2 / 0 | AZ Alkmaar | — |
| 2009/10 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 892 | 892 | 2 / 0 | Twente | — |
| 2010/11 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 987 | 932 | 2 / 0 | Ajax | NAC Breda -1 pontos |
| 2011/12 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 997 | 997 | 2 / 0 | Ajax | — |
| 2012/13 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 964 | 964 | 2 / 0 | Ajax | — |
| 2013/14 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 978 | 978 | 2 / 0 | Ajax | — |
| 2014/15 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 942 | 942 | 2 / 0 | PSV | Twente -6 pontos |
| 2015/16 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 912 | 904 | 2 / 0 | PSV | Twente -3 pontos |
| 2016/17 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 884 | 879 | 2 / 0 | Feyenoord | — |
| 2017/18 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 960 | 945 | 2 / 0 | PSV | — |
| 2018/19 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 1061 | 1057 | 2 / 0 | Ajax | — |
| 2019/20 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 232 (232) | 715 | 715 | 2 / 0 | — | — |
| 2020/21 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 920 | 920 | 2 / 0 | Ajax | — |
| 2021/22 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 875 | 872 | 2 / 0 | Ajax | — |
| 2022/23 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 935 | 930 | 2 / 0 | Feyenoord | — |
| 2023/24 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 992 | 992 | 2 / 0 | PSV | Vitesse -18 pontos |
| 2024/25 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 914 | 914 | 2 / 0 | PSV | — |
| 2025/26 | engsoccerdata + ogol + football-data + ESPN + RSSSF + Wikipédia | 18 | 306 (306) | 972 | 970 | 2 / 0 | PSV | — |

## Conferência e ocorrências, temporada a temporada

### 1956/57

- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Feyenoord, Wikipédia PSV); fica a da Wikipédia

### 1957/58

- o título foi decidido num jogo extra (DOS e Ajax empatados em pontos), e o último lugar também (Elinkwijk 2-1 GVAV, em campo neutro): os jogos extras ficam de fora, como os play-offs; a ordem é a oficial (Wikipédia)
- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF Elinkwijk, Wikipédia GVAV); fica a da Wikipédia

### 1958/59

- sem ocorrências

### 1959/60

- o título foi decidido num jogo extra (Ajax 5-1 Feyenoord, empatados em pontos): fica de fora, como os play-offs; a ordem é a oficial (Wikipédia)

### 1960/61

- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF ADO Den Haag, Wikipédia Willem II); fica a da Wikipédia

### 1961/62

- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF SC Enschede, Wikipédia GVAV); fica a da Wikipédia

### 1962/63

- sem ocorrências

### 1963/64

- sem ocorrências

### 1964/65

- SC Enschede não está na temporada seguinte, mas não foi rebaixado: fundiu-se com o Enschedese Boys no FC Twente (1965), que ficou com o lugar na Eredivisie

### 1965/66

- sem ocorrências

### 1966/67

- sem ocorrências

### 1967/68

- Fortuna '54 não está na temporada seguinte, mas não foi rebaixado: fundiu-se com o Sittardia no Fortuna SC (1968), que ficou com o lugar na Eredivisie; ninguém caiu em 1967/68 (Wikipédia)
- Sittardia não está na temporada seguinte, mas não foi rebaixado: fundiu-se com o Fortuna '54 no Fortuna SC (1968); ninguém caiu em 1967/68 (Wikipédia)
- Xerxes não está na temporada seguinte, mas não foi rebaixado: o Xerxes/DHC faliu ao fim da temporada; ninguém caiu em 1967/68 (Wikipédia)

### 1968/69

- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF DOS Utrecht, Wikipédia Volendam); fica a da Wikipédia

### 1969/70

- placar corrigido: Sparta Rotterdam x ADO Den Haag de 1-3 para 1-2 — a base traz 1-3; o ogol e a matriz da RSSSF trazem 1-2, e as tabelas da RSSSF e da Wikipédia só fecham com 1-2
- data diferente no ogol em 17 jogos (ex.: PSV x Telstar: base 1969-08-17, ogol 1969-12-28); fica a da base
- DOS Utrecht não está na temporada seguinte, mas não foi rebaixado: fundiu-se com o Elinkwijk e o Velox no FC Utrecht (1970), que ficou com o lugar na Eredivisie

### 1970/71

- Holland Sport não está na temporada seguinte, mas não foi rebaixado: fundiu-se com o ADO no FC Den Haag (1971), que ficou com o lugar na Eredivisie

### 1971/72

- DWS Amsterdam não está na temporada seguinte, mas não foi rebaixado: fundiu-se com o Blauw-Wit e o De Volewijckers no FC Amsterdam (1972), que ficou com o lugar na Eredivisie

### 1972/73

- sem ocorrências

### 1973/74

- sem ocorrências

### 1974/75

- sem ocorrências

### 1975/76

- sem ocorrências

### 1976/77

- sem ocorrências

### 1977/78

- sem ocorrências

### 1978/79

- sem ocorrências

### 1979/80

- data diferente no ogol em 1 jogos (ex.: Go Ahead Eagles x ADO Den Haag: base 1979-12-16, ogol 1980-02-13); fica a da base

### 1980/81

- data diferente no ogol em 1 jogos (ex.: Ajax x NEC Nijmegen: base 1980-11-02, ogol 1980-10-29); fica a da base

### 1981/82

- data diferente no ogol em 37 jogos (ex.: AZ Alkmaar x NAC Breda: base 1981-08-16, ogol 1981-08-15); fica a da base

### 1982/83

- sem ocorrências

### 1983/84

- ordem diferente entre RSSSF e Wikipédia em 2 posições (ex.: RSSSF AZ Alkmaar, Wikipédia Sparta Rotterdam); fica a da Wikipédia

### 1984/85

- sem ocorrências

### 1985/86

- sem ocorrências

### 1986/87

- sem ocorrências

### 1987/88

- data diferente no ogol em 81 jogos (ex.: PEC Zwolle x VVV-Venlo: base 1987-08-14, ogol 1987-08-16); fica a da base

### 1988/89

- data diferente no ogol em 83 jogos (ex.: MVV Maastricht x Haarlem: base 1988-08-20, ogol 1988-08-21); fica a da base

### 1989/90

- data diferente no ogol em 94 jogos (ex.: Twente x Roda JC: base 1989-08-12, ogol 1989-08-13); fica a da base

### 1990/91

- data diferente no ogol em 112 jogos (ex.: Roda JC x Twente: base 1990-08-24, ogol 1990-08-26); fica a da base
- SVV Schiedam não está na temporada seguinte, mas não foi rebaixado: fundiu-se com o Dordrecht '90 (SVV/Dordrecht '90, 1991), que ficou com o lugar na Eredivisie

### 1991/92

- data diferente no ogol em 85 jogos (ex.: MVV Maastricht x Fortuna Sittard: base 1991-08-17, ogol 1991-08-18); fica a da base

### 1992/93

- data diferente no ogol em 112 jogos (ex.: Fortuna Sittard x MVV Maastricht: base 1992-08-14, ogol 1992-08-16); fica a da base

### 1993/94

- data diferente no ogol em 97 jogos (ex.: Go Ahead Eagles x Vitesse: base 1993-08-14, ogol 1993-08-15); fica a da base

### 1994/95

- data diferente no ogol em 4 jogos (ex.: Willem II x NAC Breda: base 1994-08-28, ogol 1994-08-27); fica a da base

### 1995/96

- data diferente no ogol em 4 jogos (ex.: NAC Breda x Vitesse: base 1995-11-05, ogol 1995-11-04); fica a da base

### 1996/97

- data diferente no ogol em 11 jogos (ex.: PSV x Vitesse: base 1996-09-22, ogol 1996-09-21); fica a da base

### 1997/98

- data diferente no ogol em 1 jogos (ex.: Utrecht x Groningen: base 1997-11-08, ogol 1997-11-09); fica a da base

### 1998/99

- sem ocorrências

### 1999/00

- placar corrigido: Heerenveen x Willem II de 2-3 para 2-4 — a base traz 2-3; o football-data e a matriz da RSSSF trazem 2-4, e as tabelas da RSSSF e da Wikipédia só fecham com 2-4
- placar diferente no ogol — Heerenveen x Willem II (1999-09-11): base 2-4, ogol 2-3

### 2000/01

- data diferente no ogol em 33 jogos (ex.: Feyenoord x AZ Alkmaar: base 2000-08-19, ogol 2000-08-20); fica a da base

### 2001/02

- placar diferente na ESPN — Twente x Willem II (2001-10-09): base 0-0, ESPN 1-2
- placar diferente na ESPN — Vitesse x Feyenoord (2002-02-17): base 2-1, ESPN 3-2
- placar diferente na ESPN — Feyenoord x Vitesse (2001-11-17): base 3-2, ESPN 1-2
- ESPN com 305 de 306 jogos (ex. sem ESPN: Heerenveen x Utrecht, 2001-10-10)
- gols da ESPN não batem com o placar — Feyenoord 3-2 Vitesse: ESPN 1-2 (descartados)
- gols da ESPN não batem com o placar — Utrecht 4-2 Sparta Rotterdam: ESPN 5-2 (descartados)

### 2002/03

- placar diferente na ESPN — De Graafschap x Feyenoord (2003-04-05): base 3-4, ESPN 5-5
- gols da ESPN não batem com o placar — De Graafschap 3-4 Feyenoord: ESPN 5-5 (descartados)

### 2003/04

- placar diferente na ESPN — Volendam x AZ Alkmaar (2003-12-14): base 0-6, ESPN 0-7
- ESPN com 304 de 306 jogos (ex. sem ESPN: RBC Roosendaal x RKC Waalwijk, 2004-02-06)
- gols da ESPN não batem com o placar — Volendam 0-6 AZ Alkmaar: ESPN 0-7 (descartados)

### 2004/05

- data diferente no ogol em 6 jogos (ex.: Heerenveen x Utrecht: base 2004-10-24, ogol 2004-10-23); fica a da base

### 2005/06

- data diferente no ogol em 2 jogos (ex.: Heracles Almelo x NEC Nijmegen: base 2005-10-21, ogol 2006-04-19); fica a da base

### 2006/07

- ESPN com 305 de 306 jogos (ex. sem ESPN: ADO Den Haag x Vitesse, 2006-11-19)
- gols da ESPN não batem com o placar — Ajax 2-0 ADO Den Haag: ESPN 1-0 (descartados)
- gols da ESPN não batem com o placar — Excelsior Rotterdam 2-2 Vitesse: ESPN 2-1 (descartados)
- gols da ESPN não batem com o placar — Willem II 2-1 ADO Den Haag: ESPN 1-1 (descartados)
- gols da ESPN não batem com o placar — ADO Den Haag 1-3 Groningen: ESPN 1-0 (descartados)

### 2007/08

- data diferente no ogol em 11 jogos (ex.: Feyenoord x PSV: base 2008-01-12, ogol 2008-01-13); fica a da base

### 2008/09

- gols da ESPN não batem com o placar — Feyenoord 5-0 Volendam: ESPN 6-0 (descartados)
- gols da ESPN não batem com o placar — NAC Breda 2-1 PSV: ESPN 3-1 (descartados)
- gols da ESPN não batem com o placar — PSV 2-3 Roda JC: ESPN 2-4 (descartados)

### 2009/10

- sem ocorrências

### 2010/11

- gols da ESPN não batem com o placar — Groningen 2-2 Ajax: ESPN 4-4 (descartados)
- gols da ESPN não batem com o placar — Ajax 3-0 Roda JC: ESPN 6-0 (descartados)
- gols da ESPN não batem com o placar — Groningen 2-1 De Graafschap: ESPN 4-2 (descartados)
- gols da ESPN não batem com o placar — Groningen 2-0 Excelsior Rotterdam: ESPN 4-0 (descartados)
- gols da ESPN não batem com o placar — Excelsior Rotterdam 1-2 Roda JC: ESPN 2-4 (descartados)
- gols da ESPN não batem com o placar — Groningen 1-0 Heerenveen: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — AZ Alkmaar 3-0 Willem II: ESPN 6-0 (descartados)
- gols da ESPN não batem com o placar — Willem II 1-3 Twente: ESPN 2-6 (descartados)
- gols da ESPN não batem com o placar — Ajax 0-1 ADO Den Haag: ESPN 0-2 (descartados)
- gols da ESPN não batem com o placar — AZ Alkmaar 2-0 Ajax: ESPN 4-0 (descartados)
- gols da ESPN não batem com o placar — Roda JC 1-0 Groningen: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — Groningen 4-1 Vitesse: ESPN 8-2 (descartados)
- gols da ESPN não batem com o placar — Excelsior Rotterdam 1-3 NAC Breda: ESPN 2-6 (descartados)
- gols da ESPN não batem com o placar — De Graafschap 1-1 Groningen: ESPN 2-2 (descartados)
- gols da ESPN não batem com o placar — Ajax 1-0 VVV-Venlo: ESPN 2-0 (descartados)
- gols da ESPN não batem com o placar — ADO Den Haag 5-1 NEC Nijmegen: ESPN 10-2 (descartados)
- gols da ESPN não batem com o placar — Groningen 3-1 NEC Nijmegen: ESPN 6-2 (descartados)
- gols da ESPN não batem com o placar — ADO Den Haag 2-4 Groningen: ESPN 4-8 (descartados)

### 2011/12

- data diferente no ogol em 1 jogos (ex.: NAC Breda x Ajax: base 2012-02-11, ogol 2012-02-12); fica a da base

### 2012/13

- sem ocorrências

### 2013/14

- data diferente no ogol em 1 jogos (ex.: Go Ahead Eagles x Heracles Almelo: base 2013-12-04, ogol 2013-11-03); fica a da base

### 2014/15

- sem ocorrências

### 2015/16

- ESPN com 304 de 306 jogos (ex. sem ESPN: Excelsior Rotterdam x PEC Zwolle, 2016-05-01)

### 2016/17

- gols da ESPN não batem com o placar — Willem II 1-4 Vitesse: ESPN 1-5 (descartados)

### 2017/18

- gols da ESPN não batem com o placar — Vitesse 4-1 NAC Breda: ESPN 9-3 (descartados)
- gols da ESPN não batem com o placar — Twente 2-3 ADO Den Haag: ESPN 3-3 (descartados)
- gols da ESPN não batem com o placar — Vitesse 5-0 Twente: ESPN 6-0 (descartados)

### 2018/19

- sem ocorrências

### 2019/20

- temporada cancelada em abril de 2020 pela pandemia de covid-19, depois de 25 ou 26 rodadas (232 de 306 jogos): sem campeão, sem rebaixamento e sem acesso; a classificação é a do momento da parada
- título não atribuído (temporada cancelada (covid-19): a federação não deu o título); Ajax estava em 1º

### 2020/21

- sem ocorrências

### 2021/22

- gols da ESPN não batem com o placar — AZ Alkmaar 1-1 NEC Nijmegen: ESPN 2-2 (descartados)
- gols da ESPN não batem com o placar — Vitesse 0-1 Sparta Rotterdam: ESPN 0-2 (descartados)

### 2022/23

- data diferente no ogol em 1 jogos (ex.: Groningen x Ajax: base 2023-05-14, ogol 2023-05-16); fica a da base
- ESPN com 305 de 306 jogos (ex. sem ESPN: Groningen x Ajax, 2023-05-14)

### 2023/24

- data diferente no ogol em 2 jogos (ex.: Ajax x Feyenoord: base 2023-09-27, ogol 2023-09-24); fica a da base

### 2024/25

- sem ocorrências

### 2025/26

- o engsoccerdata não traz esta temporada
- a base não fecha nesta temporada (0 jogos): montada pelo calendário do ogol (306 jogos), com 0 jogos da base
- 306 jogos só no ogol, que entram com o placar do ogol: Fortuna Sittard 2-2 Go Ahead Eagles (2025-08-08); NEC Nijmegen 5-0 Excelsior Rotterdam (2025-08-09); Feyenoord 2-0 NAC Breda (2025-08-09); Heerenveen 1-1 Volendam (2025-08-09); PSV 6-1 Sparta Rotterdam (2025-08-09); PEC Zwolle 1-0 Twente (2025-08-10) ...
- ESPN com 305 de 306 jogos (ex. sem ESPN: NAC Breda x Heerenveen, 2026-05-11)

## Identidade dos clubes

- Cadastro em `coleta/comum-europa/clubes_ned.py` (serve para todas as divisões holandesas): nome de exibição como o clube é conhecido no Brasil, cidade e país. A identidade segue o código do clube no ogol: mudança de nome é o mesmo clube (Feijenoord e Feyenoord; ADO, FC Den Haag e ADO Den Haag; AZ '67 e AZ; PEC Zwolle e FC Zwolle); fusão que criou clube novo é outro clube (FC Twente, FC Utrecht, FC Amsterdam, Roda JC e Fortuna Sittard ficam separados dos clubes que os formaram).
- ogol e ESPN são casados pelo código do clube, por votação jogo a jogo (mesma data e placar): 53 códigos do ogol e 30 da ESPN.
- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.

## O que não deu para coletar

- **Autores dos gols e cartões antes de 2001/02:** nenhuma fonte em lote traz.
- **Público e estádio antes de 2001/02:** nenhuma fonte em lote.
- **Nacompetitie e play-offs de vaga europeia:** ficam de fora (entram com a 2ª divisão e as copas).
- **Campeonatos de antes da Eredivisie (1888/89-1955/56):** ficam de fora, à espera de decisão do Guilherme.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.
