# Campeonato Turco (`tur-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/tur-1/pacote/` e do importador `coleta/tur-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/tur-1.md`.

## 1. O que temos

- **Edições:** 97, de 1924 (Şampiyonası) a 2025/26.
- **Jogos:** 20971; **gols:** 54296; **gols com autor:** 13891 (26%); **cartões:** 23395; **jogos com estatísticas** (chutes, faltas, escanteios): 3057.
- **Clubes:** 168; **artilheiros:** 68 temporadas com artilheiro (72 linhas, com empates).
- **Classificação final:** 97 temporadas; **rodada a rodada:** 66 temporadas.
- **Tabelas publicadas guardadas para conferência:** 2185 linhas, de 148 tabelas.
- **Observação da competição:** 1ª divisão turca desde a criação da liga nacional (1959): Millî Lig, 1. Lig (1963/64) e Süper Lig (2001/02). Em 1959, dois grupos e final; em 1962/63, dois grupos, grupo final e grupo de classificação; em 2011/12, fase regular e play-offs. Os campeonatos anteriores (Türkiye Futbol Şampiyonası, 1924-1951, e Millî Küme, 1937-1950) não são contados pela federação e ficam de fora.

## 2. Fontes e regras

**Fontes:**

- ogol (zerozero): base dos jogos, com data e rodada; o clube pelo código do ogol (os nomes do calendário não são confiáveis nas temporadas antigas); calendários em `data/cache/ogol-tur-1/` para os escudos;
- RSSSF: tabelas finais de 1959 a 1996/97 (turkhist.html, com os grupos de 1959 e 1962/63), lista de campeões e de artilheiros;
- Wikipédia (en): tabelas e matriz de resultados de cada temporada (conferência jogo a jogo);
- engsoccerdata e football-data: conferência de placar de 1994/95 em diante; hora, árbitro e estatísticas do football-data;
- ESPN (liga `tur.1`): hora, estádio, público, gols e cartões com minuto, nas temporadas que ela cobre.

**Regras da importação:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a oficial (Wikipédia; sem ela, RSSSF). 2 pontos por vitória até 1986/87, 3 a partir de 1987/88. Rebaixado = clube que não está na 1ª divisão na temporada seguinte.

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 34, saldo em 28, vitórias em 1, média de gols em 3).

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 128 tabelas fecham com os jogos e 30 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: 1959/60, 1960/61, 1965/66, 1977/78, 2002/03, 2016/17, 1924 (Şampiyonası), 1927 (Şampiyonası), 1932 (Şampiyonası), 1933 (Şampiyonası), 1934 (Şampiyonası), 1935 (Şampiyonası), 1938 (Millî Küme), 1939 (Millî Küme), 1940 (Şampiyonası), 1941 (Şampiyonası), 1946 (Şampiyonası), 1956/57 (Federasyon Kupası).
- Temporadas com alguma tabela divergente: 1959, 1959/60, 1960/61, 1962/63, 1965/66, 1977/78, 1988/89, 2002/03, 2011/12, 2016/17, 1938 (Millî Küme), 1939 (Millî Küme), 1940 (Millî Küme), 1945 (Millî Küme), 1946 (Millî Küme), 1946 (Şampiyonası), 1947 (Millî Küme), 1956/57 (Federasyon Kupası).
- Temporadas com número de jogos diferente do turno e returno completo: 2011/12 (330 de 306).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1920s | 35 | 100% | 0% | 0% | 100% | 0% | 11% | 0% | 0% | 0.0 |
| 1930s | 245 | 31% | 0% | 0% | 22% | 0% | 22% | 0% | 3% | 0.0 |
| 1940s | 447 | 11% | 0% | 0% | 10% | 0% | 4% | 0% | 3% | 0.0 |
| 1950s | 670 | 77% | 0% | 57% | 3% | 0% | 2% | 0% | 0% | 0.0 |
| 1960s | 2922 | 100% | 0% | 88% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 2400 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 3142 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 2796 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 3060 | 100% | 38% | 100% | 39% | 0% | 0% | 0% | 32% | 1.6 |
| 2010s | 3084 | 100% | 98% | 99% | 96% | 16% | 0% | 30% | 61% | 2.8 |
| 2020s | 2170 | 100% | 100% | 100% | 100% | 73% | 0% | 99% | 98% | 4.6 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1959: 16 clubes
- 1959/60 a 1961/62: 20 clubes
- 1962/63: 22 clubes
- 1963/64: 18 clubes
- 1964/65 a 1965/66: 16 clubes
- 1966/67 a 1967/68: 17 clubes
- 1968/69 a 1980/81: 16 clubes
- 1981/82: 17 clubes
- 1982/83 a 1984/85: 18 clubes
- 1985/86 a 1986/87: 19 clubes
- 1987/88: 20 clubes
- 1988/89: 19 clubes
- 1989/90: 18 clubes
- 1990/91 a 1993/94: 16 clubes
- 1994/95 a 2019/20: 18 clubes
- 2020/21: 21 clubes
- 2021/22: 20 clubes
- 2022/23: 19 clubes
- 2023/24: 20 clubes
- 2024/25: 19 clubes
- 2025/26: 18 clubes
- 1924 (Şampiyonası): 14 clubes
- 1927 (Şampiyonası): 17 clubes
- 1932 (Şampiyonası): 20 clubes
- 1933 (Şampiyonası): 18 clubes
- 1934 (Şampiyonası): 20 clubes
- 1935 (Şampiyonası): 22 clubes
- 1937 (Millî Küme) a 1940 (Millî Küme): 8 clubes
- 1940 (Şampiyonası): 2 clubes
- 1941 (Millî Küme): 10 clubes
- 1941 (Şampiyonası): 7 clubes
- 1942 (Şampiyonası): 4 clubes
- 1943 (Millî Küme) a 1944 (Millî Küme): 8 clubes
- 1944 (Şampiyonası): 4 clubes
- 1945 (Millî Küme): 8 clubes
- 1945 (Şampiyonası): 7 clubes
- 1946 (Millî Küme): 8 clubes
- 1946 (Şampiyonası): 4 clubes
- 1947 (Millî Küme): 8 clubes
- 1947 (Şampiyonası): 3 clubes
- 1949 (Şampiyonası): 6 clubes
- 1950 (Millî Küme): 8 clubes
- 1950 (Şampiyonası): 4 clubes
- 1951 (Şampiyonası): 9 clubes
- 1956/57 (Federasyon Kupası): 27 clubes
- 1957/58 (Federasyon Kupası): 38 clubes

**Pontos por vitória:**

- 1959 a 1986/87: 2
- 1987/88 a 1942 (Şampiyonası): 3
- 1943 (Millî Küme) a 1944 (Şampiyonası): 2
- 1945 (Millî Küme) a 1947 (Millî Küme): 3
- 1947 (Şampiyonası): 2
- 1949 (Şampiyonası) a 1951 (Şampiyonası): 3
- 1956/57 (Federasyon Kupası) a 1957/58 (Federasyon Kupası): 2

**Nome oficial:**

- 1959 a 1962/63: Millî Lig
- 1963/64 a 2000/01: 1. Lig
- 2001/02 a 2025/26: Süper Lig
- 1924 (Şampiyonası) a 1935 (Şampiyonası): Türkiye Futbol Şampiyonası
- 1937 (Millî Küme) a 1940 (Millî Küme): Millî Küme
- 1940 (Şampiyonası): Türkiye Futbol Şampiyonası
- 1941 (Millî Küme): Millî Küme
- 1941 (Şampiyonası) a 1942 (Şampiyonası): Türkiye Futbol Şampiyonası
- 1943 (Millî Küme) a 1944 (Millî Küme): Millî Küme
- 1944 (Şampiyonası): Türkiye Futbol Şampiyonası
- 1945 (Millî Küme): Millî Küme
- 1945 (Şampiyonası): Türkiye Futbol Şampiyonası
- 1946 (Millî Küme): Millî Küme
- 1946 (Şampiyonası): Türkiye Futbol Şampiyonası
- 1947 (Millî Küme): Millî Küme
- 1947 (Şampiyonası) a 1949 (Şampiyonası): Türkiye Futbol Şampiyonası
- 1950 (Millî Küme): Millî Küme
- 1950 (Şampiyonası) a 1951 (Şampiyonası): Türkiye Futbol Şampiyonası
- 1956/57 (Federasyon Kupası) a 1957/58 (Federasyon Kupası): Federasyon Kupası

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- 1959: Grupos (grupos, pontos_corridos); Final (mata_mata, ida_volta)
- 1962/63: Grupos (grupos, pontos_corridos); Grupo final (grupos, pontos_corridos); Grupo de classificação (grupos, pontos_corridos)
- 2011/12: Fase regular (liga, pontos_corridos); Play-off do título (grupos, pontos_corridos); Play-off europeu (grupos, pontos_corridos)
- 1924 (Şampiyonası): First round (mata_mata, jogo_unico); First round · Resumed matches (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Disputa de 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1927 (Şampiyonası): Eliminatória prévia (mata_mata, jogo_unico); First round (mata_mata, jogo_unico); First round · Resumed match (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Quartas de final · Desempate (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Disputa de 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1932 (Şampiyonası): Fase de grupos · 1ª eliminatória (grupos, jogo_unico); Fase de grupos · Final do grupo (grupos, jogo_unico); Fase de grupos · Semifinal (grupos, jogo_unico); Fase final · 1ª eliminatória (mata_mata, jogo_unico); Fase final · Semifinal (mata_mata, jogo_unico); Fase final · Final (mata_mata, jogo_unico)
- 1933 (Şampiyonası): Fase de grupos · 1ª eliminatória (grupos, jogo_unico); Fase de grupos · Final do grupo (grupos, jogo_unico); Fase final · 1ª eliminatória (mata_mata, jogo_unico); Fase final · Semifinal (mata_mata, jogo_unico); Fase final · Final (mata_mata, jogo_unico)
- 1934 (Şampiyonası): Fase de grupos · 1ª eliminatória (grupos, jogo_unico); Fase de grupos · Final do grupo (grupos, jogo_unico); Fase de grupos · Semifinal (grupos, jogo_unico); Fase final · 1ª eliminatória (mata_mata, jogo_unico); Fase final · Semifinal (mata_mata, jogo_unico); Fase final · Final (mata_mata, jogo_unico)
- 1935 (Şampiyonası): Fase de grupos · 1ª eliminatória (grupos, jogo_unico); Fase de grupos · Final do grupo (grupos, jogo_unico); Fase de grupos · Semifinal (grupos, jogo_unico); Fase final · 1ª eliminatória (mata_mata, jogo_unico); Fase final · Semifinal (mata_mata, jogo_unico); Fase final · Final (mata_mata, jogo_unico)
- 1937 (Millî Küme): Liga (grupos, pontos_corridos)
- 1938 (Millî Küme): Liga (grupos, pontos_corridos)
- 1939 (Millî Küme): Liga (grupos, pontos_corridos)
- 1940 (Millî Küme): Liga (grupos, pontos_corridos)
- 1940 (Şampiyonası): Final (mata_mata, jogo_unico)
- 1941 (Millî Küme): Liga (grupos, pontos_corridos)
- 1941 (Şampiyonası): 1ª eliminatória (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1942 (Şampiyonası): Grupo final (grupos, pontos_corridos)
- 1943 (Millî Küme): Liga (grupos, pontos_corridos)
- 1944 (Millî Küme): Liga (grupos, pontos_corridos)
- 1944 (Şampiyonası): Grupo final (grupos, pontos_corridos)
- 1945 (Millî Küme): Liga (grupos, pontos_corridos)
- 1945 (Şampiyonası): Qualification play-off · 1ª eliminatória (mata_mata, jogo_unico); Qualification play-off · Final (mata_mata, jogo_unico); Grupo final (grupos, pontos_corridos)
- 1946 (Millî Küme): Liga (grupos, pontos_corridos)
- 1946 (Şampiyonası): Grupo final (grupos, pontos_corridos)
- 1947 (Millî Küme): Liga (grupos, pontos_corridos)
- 1947 (Şampiyonası): Grupo final (grupos, pontos_corridos)
- 1949 (Şampiyonası): Qualification play-off · First round (mata_mata, jogo_unico); Qualification play-off · Play-off final (mata_mata, jogo_unico); Grupo final (grupos, pontos_corridos)
- 1950 (Millî Küme): Liga (grupos, pontos_corridos)
- 1950 (Şampiyonası): Grupo final (grupos, pontos_corridos)
- 1951 (Şampiyonası): Qualification play-off · First round (mata_mata, jogo_unico); Qualification play-off · Semifinal (mata_mata, jogo_unico); Qualification play-off · Final (mata_mata, jogo_unico); Grupo final (grupos, pontos_corridos)
- 1956/57 (Federasyon Kupası): 1ª eliminatória (grupos, jogo_unico); 2ª eliminatória (grupos, jogo_unico); 3ª eliminatória (grupos, jogo_unico); Grupo final (grupos, pontos_corridos)
- 1957/58 (Federasyon Kupası): First round (grupos, jogo_unico); Second round (grupos, jogo_unico); Fase de grupos (grupos, jogo_unico)

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- resultado: 54 temporadas
- pontos, confronto direto, saldo de gols, gols pró: 34 temporadas
- pontos, saldo de gols, gols pró: 28 temporadas
- pontos: 21 temporadas
- pontos, média de gols: 4 temporadas
- pontos, média de gols (goal average): 3 temporadas
- pontos, saldo: 1 temporadas
- pontos, vitórias, saldo de gols, gols pró: 1 temporadas
- pontos, com a metade dos pontos da fase regular de partida: 1 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1962/63: grupo de classificação sem os jogos (só a tabela)
- 1988/89: o ônibus do Samsunspor sofreu um acidente grave em 20/01/1989 e o clube não pôde jogar o resto da temporada: os 18 jogos que faltavam foram dados por 3-0 aos adversários, e o Samsunspor não caiu
- 2009/10: a federação rebaixou o Ankaraspor em 07/10/2009, com efeito imediato, pela ligação dos dirigentes com os do Ankaragücü; todos os 34 jogos dele valeram 3-0 para os adversários
- 2022/23: punições: Kayserispor -3 pontos
- 2023/24: punições: Kayserispor -3 pontos; İstanbulspor -3 pontos
- 2024/25: punições: Adana Demirspor -12 pontos
- 1924 (Şampiyonası): Türkiye Futbol Şampiyonası: vencedor Harp Okulu; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1927 (Şampiyonası): Türkiye Futbol Şampiyonası: vencedor Muhafızgücü; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1932 (Şampiyonası): Türkiye Futbol Şampiyonası: vencedor İstanbulspor; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1933 (Şampiyonası): Türkiye Futbol Şampiyonası: vencedor Fenerbahçe; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1934 (Şampiyonası): Türkiye Futbol Şampiyonası: vencedor Beşiktaş; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1935 (Şampiyonası): Türkiye Futbol Şampiyonası: vencedor Fenerbahçe; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1937 (Millî Küme): Millî Küme: vencedor Fenerbahçe; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1938 (Millî Küme): Millî Küme: vencedor Güneş; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1939 (Millî Küme): Millî Küme: vencedor Galatasaray; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1940 (Millî Küme): Millî Küme: vencedor Fenerbahçe; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1940 (Şampiyonası): Türkiye Futbol Şampiyonası: vencedor Eskişehir Demirspor; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1941 (Millî Küme): Millî Küme: vencedor Beşiktaş; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1941 (Şampiyonası): Türkiye Futbol Şampiyonası: vencedor Gençlerbirliği; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1942 (Şampiyonası): Türkiye Futbol Şampiyonası: vencedor Harp Okulu; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1943 (Millî Küme): Millî Küme: vencedor Fenerbahçe; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1944 (Millî Küme): Millî Küme: vencedor Beşiktaş; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1944 (Şampiyonası): Türkiye Futbol Şampiyonası: vencedor Fenerbahçe; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1945 (Millî Küme): Millî Küme: vencedor Fenerbahçe; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1945 (Şampiyonası): Türkiye Futbol Şampiyonası: vencedor Harp Okulu; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1946 (Millî Küme): Millî Küme: vencedor Fenerbahçe; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1946 (Şampiyonası): Türkiye Futbol Şampiyonası: vencedor Gençlerbirliği; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1947 (Millî Küme): Millî Küme: vencedor Beşiktaş; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1947 (Şampiyonası): Türkiye Futbol Şampiyonası: vencedor Ankara Demirspor; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1949 (Şampiyonası): Türkiye Futbol Şampiyonası: vencedor Ankaragücü; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1950 (Millî Küme): Millî Küme: vencedor Fenerbahçe; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1950 (Şampiyonası): Türkiye Futbol Şampiyonası: vencedor Göztepe; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1951 (Şampiyonası): Türkiye Futbol Şampiyonası: vencedor Beşiktaş; título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)
- 1956/57 (Federasyon Kupası): Federasyon Kupası: título reconhecido pela federação desde 2002
- 1957/58 (Federasyon Kupası): Federasyon Kupası: título reconhecido pela federação desde 2002

## 6. Campeões, rebaixados e punições

**Títulos:**

- Fenerbahçe: 28
- Galatasaray: 27
- Beşiktaş: 21
- Trabzonspor: 7
- Harp Okulu: 3
- Gençlerbirliği: 2
- Bursaspor: 1
- İstanbul Başakşehir: 1
- Muhafızgücü: 1
- İstanbulspor: 1
- Güneş: 1
- Eskişehir Demirspor: 1
- Ankara Demirspor: 1
- Ankaragücü: 1
- Göztepe: 1

**Rebaixamentos:** 181 no total; quem mais caiu: Samsunspor (7), Kayseri Erciyesspor (7), Adana Demirspor (6), Karşıyaka (6), Ankaragücü (6).

**Punições em pontos:**

- 2011/12: Galatasaray -38
- 2011/12: Fenerbahçe -34
- 2011/12: Trabzonspor -28
- 2011/12: Beşiktaş -27
- 2011/12: Eskişehirspor -11
- 2011/12: İstanbul Başakşehir -7
- 2011/12: Sivasspor -4
- 2011/12: Bursaspor -12
- 2022/23: Kayserispor -3
- 2023/24: Kayserispor -3
- 2023/24: İstanbulspor -3
- 2024/25: Adana Demirspor -12
- 1938 (Millî Küme): Altay -1
- 1938 (Millî Küme): Fenerbahçe -10
- 1939 (Millî Küme): Galatasaray -1
- 1946 (Millî Küme): Vefa 11
- 1946 (Millî Küme): Galatasaray 8

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/tur-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Placares corrigidos (`CORRECOES`)

- **1199753:** [Samsunspor, Gençlerbirliği, 2, 2] o ogol dá 0-2; football-data e engsoccerdata; com os três jogos corrigidos, as linhas de Samsunspor, Gençlerbirliği e Kocaelispor na tabela da Wikipédia fecham
- **1199833:** [Kocaelispor, Samsunspor, 0, 1] o ogol dá Samsunspor 0-0 Kocaelispor; football-data e engsoccerdata; com os três jogos corrigidos, as linhas de Samsunspor, Gençlerbirliği e Kocaelispor na tabela da Wikipédia fecham
- **1199908:** [Gençlerbirliği, Samsunspor, 2, 0] o ogol dá Samsunspor 0-2 Gençlerbirliği (mando invertido); football-data e engsoccerdata; com os três jogos corrigidos, as linhas de Samsunspor, Gençlerbirliği e Kocaelispor na tabela da Wikipédia fecham
- **196346:** [Trabzonspor, Diyarbakırspor, 3, 0] o ogol dá 2-1; matriz da Wikipédia, football-data e engsoccerdata dão 3-0, e a tabela da Wikipédia fecha
- **196378:** [Gaziantepspor, Malatyaspor, 1, 0] o ogol dá 0-1; matriz da Wikipédia, football-data e engsoccerdata dão 1-0, e a tabela da Wikipédia fecha
- **196380:** [Samsunspor, Diyarbakırspor, 1, 0] o ogol dá 0-1; matriz da Wikipédia, football-data e engsoccerdata dão 1-0, e a tabela da Wikipédia fecha

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1959:** a matriz de resultados da Wikipédia de 1959 difere do ogol em 16 pares (parece ter mandos trocados); o ogol fecha com as tabelas dos grupos, menos 1 gol do Beşiktaş e 1 do Hacettepe na RSSSF
- **1959/60:** o ogol e a matriz da Wikipédia concordam jogo a jogo; as tabelas da RSSSF e da Wikipédia (que a copia) têm 1 ou 2 gols a mais ou a menos em 6 clubes, sem mudar pontos nem posições
- **1960/61:** a tabela da RSSSF de 1960/61 tem erros em 8 clubes (números de um clube em outro); a da Wikipédia fecha com os jogos, menos os gols contra do Feriköy e os gols do Altınordu (17-31 em vez de 31-53, erro de digitação), e dá a ordem
- **1962/63:** o ogol tem alguns jogos dos grupos com o mando trocado em relação à matriz da Wikipédia (os totais dos grupos fecham com as tabelas, menos 1 gol do Ankara Demirspor e 1 do Beykoz); no grupo final, as tabelas da RSSSF e da Wikipédia diferem dos jogos em 6 clubes, sem outra fonte para decidir: ficam os jogos do ogol / o grupo de classificação (7º a 9º de cada grupo) não tem os jogos no ogol nem na Wikipédia: entra a tabela
- **1965/66:** Altay (gols pró) e Şekerspor (gols contra): 2 gols a mais nas tabelas que nos jogos do ogol e da matriz
- **1977/78:** Samsunspor e Mersin İdmanyurdu: 1 gol de diferença nas tabelas (o ogol e a matriz concordam)
- **1988/89:** a RSSSF separa o Samsunspor em duas linhas: os 18 jogos disputados e os 18 dados por 0-3 depois do acidente; os jogos e a Wikipédia somam os 36
- **2002/03:** İstanbulspor: 1 gol contra a mais na tabela da Wikipédia (o ogol e a matriz concordam)
- **2011/12:** Trabzonspor x Gaziantepspor (10/02/2012): a matriz e a tabela da Wikipédia dão 4-0; o ogol, o football-data e o engsoccerdata, 4-1: fica 4-1
- **2016/17:** Adanaspor x Kasımpaşa (30/01/2017): a matriz e a tabela da Wikipédia dão 3-0; o ogol, o football-data e o engsoccerdata, 2-0: fica 2-0

### Jogos dados pela federação (o ogol traz o placar; marcados awd) (`DADOS_FORA`)

- **1988/89 · Samsunspor:** [1989-01-01] o ônibus do Samsunspor sofreu um acidente grave em 20/01/1989 e o clube não pôde jogar o resto da temporada: os 18 jogos que faltavam foram dados por 3-0 aos adversários, e o Samsunspor não caiu
- **2009/10 · Ankaraspor:** [2009-01-01] a federação rebaixou o Ankaraspor em 07/10/2009, com efeito imediato, pela ligação dos dirigentes com os do Ankaragücü; todos os 34 jogos dele valeram 3-0 para os adversários

## 8. O que não deu para coletar

- **Jogos do grupo de classificação de 1962/63:** nem o ogol nem a Wikipédia têm; entra a tabela.
- **Autores dos gols antes da ESPN:** nenhuma fonte em lote (ficha do ogol, jogo a jogo).
- **Campeonatos anteriores a 1959** (Türkiye Futbol Şampiyonası e Millî Küme): fora do escopo; a federação não os conta.

## 9. Pendências

- nenhuma em aberto na coleta.

**Limites de fonte (fechados):** nenhuma fonte em lote tem o dado; só volta com uma fonte nova.

- Era antiga (antes de 1959, em antigo.py): os jogos do Şampiyonası de 1924 a 1935 e as matrizes da Millî Küme não têm data (só as fichas trazem).
- 1962/63: os jogos do grupo de classificação (7º a 9º de cada grupo) não estão no ogol nem na Wikipédia (en e tr); entra a tabela.
- Autores dos gols e cartões: só com a ESPN (2006/07+), que quase não tem lances de 2011/12 a 2014/15 nem dos play-offs de 2011/12; antes e nesses anos, jogo a jogo (ficha do ogol).
- Placares do ogol que só a matriz da Wikipédia contesta nas temporadas antigas (sem football-data nem engsoccerdata antes de 1994/95): ficam os do ogol, que fecham com as tabelas.

**Com o agente de revisão:** decisões da coleta que ele confere.

- Kayseri: o Kayserispor de 1966 a 2004 está como Kayseri Erciyesspor (troca de nomes de 2004, como na Wikipédia); o ogol e boa parte da imprensa contam a história no Kayserispor de hoje.

## 10. Arquivos

- Código: `coleta/tur-1/` (`edicoes.py`, `baixar.py`, `importar.py`, leitor da RSSSF); cadastro dos clubes em `coleta/comum-europa/clubes_tur.py`.
- Fontes baixadas: `data/coleta/tur-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-tur-1/`.
- Pacote: `data/coleta/tur-1/pacote/`; relatório: `docs/coleta/tur-1.md`.
- Refazer do zero: `python coleta/tur-1/baixar.py ...` (ver o docstring), `python coleta/tur-1/importar.py`, `python coleta/comum-europa/testar_carga.py tur-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

