# Campeonato Tchecoslovaco (`tch-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/tch-1/pacote/` e do importador `coleta/tch-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/tch-1.md`.

## 1. O que temos

- **Edições:** 68, de 1925 a 1992/93.
- **Jogos:** 11791; **gols:** 39181; **gols com autor:** 0 (0%); **cartões:** 0; **jogos com estatísticas** (chutes, faltas, escanteios): 0.
- **Clubes:** 66; **artilheiros:** 0 temporadas com artilheiro (0 linhas, com empates).
- **Classificação final:** 68 temporadas; **rodada a rodada:** 0 temporadas.
- **Tabelas publicadas guardadas para conferência:** 1854 linhas, de 136 tabelas.
- **Observação da competição:** Campeonato da Tchecoslováquia, de 1925 (primeiro título oficial) a 1992/93, com a liga do Protetorado da Boêmia e Morávia (Národní liga, 1938/39-1943/44). O outono de 1948 é edição não oficial. Não inclui o campeonato da Boêmia Central antes de 1925, o campeonato amador, 1944/45 (abandonado) nem a liga eslovaca da guerra. Depois de 1993: Campeonato Tcheco e Campeonato Eslovaco.

## 2. Fontes e regras

**Fontes:**

- Wikipédia (en): matriz de resultados de cada temporada (base dos jogos), tabela final (ordem oficial, punições);
- RSSSF: tabelas finais (tsjslhist.html, casadas pela posição com as da Wikipédia), lista de campeões, final de 1945/46.

**Regras da importação:** (ver relatório)

**Desempate:** o critério calculado que reproduz a ordem oficial (confronto direto em 21, saldo em 41, média de gols em 7).

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 120 tabelas fecham com os jogos e 18 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: 1927, 1941/42, 1943/44, 1957/58, 1960/61, 1963/64, 1969/70, 1984/85.
- Temporadas com alguma tabela divergente: 1927, 1939/40, 1941/42, 1943/44, 1957/58, 1960/61, 1961/62, 1963/64, 1969/70, 1984/85.
- Temporadas com número de jogos diferente do turno e returno completo: nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1920s | 345 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1930s | 1128 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 1325 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 1595 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 1878 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 2400 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 2400 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 720 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1925: 10 clubes
- 1925/26: 12 clubes
- 1927: 8 clubes
- 1927/28 a 1928/29: 7 clubes
- 1929/30 a 1930/31: 8 clubes
- 1931/32: 9 clubes
- 1932/33 a 1933/34: 10 clubes
- 1934/35: 12 clubes
- 1935/36: 14 clubes
- 1936/37 a 1937/38: 12 clubes
- 1938/39: 11 clubes
- 1939/40 a 1942/43: 12 clubes
- 1943/44: 14 clubes
- 1945/46: 20 clubes
- 1946/47: 14 clubes
- 1947/48: 11 clubes
- 1948 a 1953: 14 clubes
- 1954 a 1957/58: 12 clubes
- 1958/59 a 1968/69: 14 clubes
- 1969/70 a 1992/93: 16 clubes

**Pontos por vitória:**

- 1925 a 1992/93: 2

**Nome oficial:**

- 1925 a 1933/34: Asociační liga
- 1934/35 a 1937/38: Státní liga
- 1938/39 a 1943/44: Národní liga (Česko-moravská liga)
- 1945/46 a 1992/93: 1. liga

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- 1945/46: Grupos (grupos, pontos_corridos); Final (mata_mata, ida_volta)

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, saldo de gols: 41 temporadas
- pontos, confronto direto, saldo de gols: 20 temporadas
- pontos, média de gols (goal average): 7 temporadas
- soma dos placares: 1 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1938/39: liga do Protetorado da Boêmia e Morávia (Národní liga), durante a ocupação; temporada interrompida em 1938/39 e continuada como liga do Protetorado
- 1939/40: liga do Protetorado da Boêmia e Morávia (Národní liga), durante a ocupação
- 1940/41: liga do Protetorado da Boêmia e Morávia (Národní liga), durante a ocupação
- 1941/42: liga do Protetorado da Boêmia e Morávia (Národní liga), durante a ocupação
- 1942/43: liga do Protetorado da Boêmia e Morávia (Národní liga), durante a ocupação
- 1943/44: liga do Protetorado da Boêmia e Morávia (Národní liga), durante a ocupação
- 1948: campeonato de outono de 1948, na passagem para o calendário de ano civil; não é título oficial (RSSSF: "fall championship; not official")
- 1964/65: punições: Sparta Praga -2 pontos
- 1968/69: punições: Dukla Banská Bystrica -2 pontos
- 1992/93: última temporada antes da separação: sem rebaixados (1993/94: Campeonato Tcheco e Campeonato Eslovaco)

## 6. Campeões, rebaixados e punições

**Títulos:**

- Sparta Praga: 21
- Slavia Praga: 14
- Dukla Praga: 11
- Slovan Bratislava: 8
- Spartak Trnava: 5
- Baník Ostrava: 3
- Viktoria Žižkov: 1
- Inter Bratislava: 1
- Hradec Králové: 1
- Zbrojovka Brno: 1
- Bohemians 1905: 1
- Vítkovice: 1

**Rebaixamentos:** 157 no total; quem mais caiu: Viktoria Plzeň (9), Čechie Karlín (7), SK Libeň (6), Bohemians 1905 (6), Žilina (6).

**Punições em pontos:**

- 1964/65: Sparta Praga -2
- 1968/69: Dukla Banská Bystrica -2

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/tch-1/importar.py`; cada uma também aparece no relatório, na temporada.

- nenhuma

## 8. O que não deu para coletar

- **Datas, rodadas, autores dos gols, cartões, público:** a matriz da Wikipédia não traz; o ogol, a ESPN e o football-data não têm esta liga.
- **Campeonato da Boêmia Central antes de 1925, campeonato amador, 1944/45 e liga eslovaca da guerra:** fora do escopo.

## 9. Pendências

- nenhuma em aberto na coleta.

**Limites de fonte (fechados):** nenhuma fonte em lote tem o dado; só volta com uma fonte nova.

- Sem datas, rodadas, autores dos gols, cartões e público: a base é a matriz da Wikipédia (en); o ogol, a ESPN e o football-data não têm esta liga.
- 10 temporadas em que a matriz da Wikipédia não fecha com as tabelas (que concordam entre si): a classificação fica com os números publicados; só um jornal da época diria qual jogo está errado.
- Fora do escopo (decisão do Guilherme, 25/11/2026): Boêmia Central antes de 1925, campeonato amador, 1944/45 e liga eslovaca da guerra.

**Com o agente de revisão:** decisões da coleta que ele confere.

- Identidade pelos links da Wikipédia através das trocas de nome da era comunista; o Dukla Praha histórico é o mesmo do `cze-1` em 1993/94, mas a RSSSF diz que ele é hoje o Marila Příbram (no `cze-1`, Příbram ficou à parte, pela Wikipédia).
- Classificação de 1945/46: a final (Sparta x Slavia) e depois a posição nos grupos; títulos do Protetorado contados (Sparta 21, Slavia 13 no total).

## 10. Arquivos

- Código: `coleta/tch-1/` (`edicoes.py`, `baixar.py`, `importar.py`); cadastro dos clubes em `coleta/comum-europa/clubes_tch.py`.
- Fontes baixadas: `data/coleta/tch-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-tch-1/`.
- Pacote: `data/coleta/tch-1/pacote/`; relatório: `docs/coleta/tch-1.md`.
- Refazer do zero: `python coleta/tch-1/baixar.py ...` (ver o docstring), `python coleta/tch-1/importar.py`, `python coleta/comum-europa/testar_carga.py tch-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

