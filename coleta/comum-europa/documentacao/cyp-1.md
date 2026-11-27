# Campeonato Cipriota (`cyp-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/cyp-1/pacote/` e do importador `coleta/cyp-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/cyp-1.md`.

## 1. O que temos

- **Edições:** 86, de 1934/35 a 2025/26.
- **Jogos:** 13465; **gols:** 40239; **gols com autor:** 231 (1%); **cartões:** 0; **jogos com estatísticas** (chutes, faltas, escanteios): 0.
- **Clubes:** 46; **artilheiros:** 70 temporadas com artilheiro (83 linhas, com empates).
- **Classificação final:** 86 temporadas; **rodada a rodada:** 25 temporadas.
- **Tabelas publicadas guardadas para conferência:** 1653 linhas, de 122 tabelas.
- **Observação da competição:** Os 86 títulos que a federação (CFA) reconhece, desde 1934/35 (A' Katigoria). Não inclui os campeonatos não oficiais de 1931/32 a 1933/34 nem as temporadas sem campeão (1941/42 a 1943/44, 1958/59, 1963/64 e 2019/20). De 1967/68 a 1973/74, o campeão também jogou o Campeonato Grego (competição gre-1).

## 2. Fontes e regras

**Fontes:**

- Wikipédia (en): tabelas e matriz de resultados (base dos jogos até 1995/96, conferência depois);
- ogol (zerozero): base dos jogos desde 1996/97, com data, hora e rodada; calendários em `data/cache/ogol-cyp-1/`;
- RSSSF: página de cada temporada (tabela; jogos por rodada desde 2009/10), lista de campeões e de artilheiros.

**Regras da importação:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a oficial (Wikipédia; com grupos, o grupo do título, depois os outros). Pontos 2-1-0 até 1990/91 e 3-1-0 depois. Rebaixado = clube que não está na 1ª divisão na temporada seguinte (antes de uma temporada sem campeão, a marca da tabela).

**Desempate:** o critério calculado que reproduz a ordem oficial (média de gols em 22 tabelas, saldo em 90, confronto direto em 16).

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 126 tabelas fecham com os jogos e 38 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: 1935/36, 1936/37, 1937/38, 1938/39, 1940/41, 1944/45, 1947/48, 1948/49, 1952/53, 1954/55, 1955/56, 1956/57, 1957/58, 1959/60, 1965/66, 1966/67, 1977/78, 1978/79, 1979/80, 1980/81, 1982/83, 1983/84, 1985/86, 1986/87.
- Temporadas com alguma tabela divergente: 1935/36, 1936/37, 1937/38, 1938/39, 1940/41, 1944/45, 1947/48, 1948/49, 1952/53, 1954/55, 1955/56, 1956/57, 1957/58, 1959/60, 1965/66, 1966/67, 1977/78, 1978/79, 1979/80, 1980/81, 1982/83, 1983/84, 1985/86, 1986/87.
- Temporadas com número de jogos diferente do turno e returno completo: nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1930s | 217 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 229 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 669 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 1192 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 1950 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 1964 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 1836 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 1927 | 97% | 57% | 97% | 0% | 0% | 0% | 0% | 4% | 0.0 |
| 2010s | 2006 | 100% | 99% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2020s | 1475 | 100% | 100% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1934/35 a 1935/36: 8 clubes
- 1936/37: 7 clubes
- 1937/38: 5 clubes
- 1938/39: 7 clubes
- 1939/40: 6 clubes
- 1940/41: 5 clubes
- 1944/45 a 1945/46: 6 clubes
- 1946/47: 7 clubes
- 1947/48: 5 clubes
- 1948/49 a 1952/53: 8 clubes
- 1953/54: 9 clubes
- 1954/55: 10 clubes
- 1955/56 a 1956/57: 9 clubes
- 1957/58: 10 clubes
- 1959/60: 11 clubes
- 1960/61 a 1961/62: 13 clubes
- 1962/63: 12 clubes
- 1964/65 a 1965/66: 11 clubes
- 1966/67 a 1971/72: 12 clubes
- 1972/73 a 1974/75: 14 clubes
- 1975/76: 15 clubes
- 1976/77 a 1978/79: 16 clubes
- 1979/80: 15 clubes
- 1980/81 a 1985/86: 14 clubes
- 1986/87 a 1987/88: 16 clubes
- 1988/89: 15 clubes
- 1989/90 a 1993/94: 14 clubes
- 1994/95: 12 clubes
- 1995/96 a 2013/14: 14 clubes
- 2014/15: 12 clubes
- 2015/16 a 2017/18: 14 clubes
- 2018/19: 12 clubes
- 2020/21: 14 clubes
- 2021/22: 12 clubes
- 2022/23 a 2025/26: 14 clubes

**Pontos por vitória:**

- 1934/35 a 1959/60: 2
- 1960/61 a 1969/70: 3
- 1970/71 a 1990/91: 2
- 1991/92 a 2025/26: 3

**Nome oficial:**

- 1934/35 a 2025/26: A' Katigoria

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- 2007/08: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo intermediário (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2008/09: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo intermediário (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2009/10: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo intermediário (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2010/11: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo intermediário (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2011/12: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo intermediário (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2012/13: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo intermediário (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2013/14: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2014/15: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2015/16: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2016/17: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2017/18: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2018/19: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2020/21: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2021/22: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2022/23: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2023/24: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2024/25: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)
- 2025/26: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos)

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, saldo de gols: 52 temporadas
- pontos, saldo de gols; pontos acumulados com a fase regular: 38 temporadas
- pontos, média de gols (goal average): 22 temporadas
- pontos, confronto direto, saldo de gols: 12 temporadas
- pontos, confronto direto, saldo de gols; pontos acumulados com a fase regular: 4 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 1961/62: punições: Olympiakos Nicosia -1 pontos
- 1962/63: punições: Orfeas Nicosia -1 pontos
- 1965/66: punições: AEL Limassol -1 pontos
- 1967/68: o campeão também jogou o Campeonato Grego (competição gre-1)
- 1968/69: o campeão também jogou o Campeonato Grego (competição gre-1)
- 1969/70: punições: Anorthosis -1 pontos; Apollon Limassol -1 pontos; o campeão também jogou o Campeonato Grego (competição gre-1)
- 1970/71: o campeão também jogou o Campeonato Grego (competição gre-1)
- 1971/72: o campeão também jogou o Campeonato Grego (competição gre-1)
- 1972/73: o campeão também jogou o Campeonato Grego (competição gre-1)
- 1973/74: o campeão também jogou o Campeonato Grego (competição gre-1)
- 1990/91: punições: APEP -4 pontos
- 1993/94: punições: APEP -4 pontos
- 2001/02: punições: Alki Larnaca -3 pontos
- 2008/09: punições: APOP Kinyras -6 pontos
- 2009/10: punições: APEP -6 pontos
- 2012/13: punições: Olympiakos Nicosia -3 pontos; AEP Paphos -12 pontos
- 2013/14: punições: Nea Salamina -3 pontos; Enosis Paralimni -3 pontos; Alki Larnaca -41 pontos
- 2015/16: punições: AEL Limassol -2 pontos
- 2016/17: punições: AEZ Zakakiou -6 pontos; Ermis Aradippou -6 pontos
- 2018/19: punições: Anorthosis -6 pontos; Pafos FC -6 pontos

## 6. Campeões, rebaixados e punições

**Títulos:**

- APOEL: 29
- Omonia: 22
- Anorthosis: 13
- AEL Limassol: 6
- Apollon Limassol: 4
- EPA Larnaca: 3
- Olympiakos Nicosia: 3
- Pezoporikos Larnaca: 2
- Enosis Neon Trust: 1
- Çetinkaya: 1
- Aris Limassol: 1
- Pafos FC: 1

**Rebaixamentos:** 146 no total; quem mais caiu: Aris Limassol (15), APOP Paphos (9), Evagoras Paphos (8), Alki Larnaca (8), Olympiakos Nicosia (7).

**Punições em pontos:**

- 1961/62: Olympiakos Nicosia -1
- 1962/63: Orfeas Nicosia -1
- 1965/66: AEL Limassol -1
- 1969/70: Anorthosis -1
- 1969/70: Apollon Limassol -1
- 1990/91: APEP -4
- 1993/94: APEP -4
- 2001/02: Alki Larnaca -3
- 2008/09: APOP Kinyras -6
- 2009/10: APEP -6
- 2012/13: Olympiakos Nicosia -3
- 2012/13: AEP Paphos -12
- 2013/14: Nea Salamina -3
- 2013/14: Enosis Paralimni -3
- 2013/14: Alki Larnaca -41
- 2015/16: AEL Limassol -2
- 2016/17: Ermis Aradippou -6
- 2016/17: AEZ Zakakiou -6
- 2018/19: Anorthosis -6
- 2018/19: Pafos FC -6

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/cyp-1/importar.py`; cada uma também aparece no relatório, na temporada.

- nenhuma

## 8. O que não deu para coletar

- **Datas e rodadas até 1995/96** (só as matrizes).
- **Autores dos gols e cartões:** nenhuma fonte em lote cobre Chipre.
- **Jogos que faltam nas matrizes antigas** (temporadas dos anos 1930 e 1940).

## 9. Pendências

- nenhuma em aberto na coleta.

**Limites de fonte (fechados):** nenhuma fonte em lote tem o dado; só volta com uma fonte nova.

- Sem autores dos gols e cartões: nenhuma fonte em lote cobre Chipre (sem ESPN e sem football-data). Sem datas e rodadas até 1995/96 (só a matriz da Wikipédia).
- Matrizes antigas incompletas (anos 1930 a 1950 e algumas depois): a classificação fica com os números publicados quando a matriz não fecha (observação na linha).
- Fora do escopo (decisão do Guilherme, 27/11/2026): os campeonatos não oficiais de 1931/32 a 1933/34 e as temporadas sem campeão (1941/42 a 1943/44, 1958/59, 1963/64 e 2019/20).

**Com o agente de revisão:** decisões da coleta que ele confere.

- Pontos 3-2-1 de 1960/61 a 1969/70, como a RSSSF anota (a Wikipédia calcula com 2-1-0).
- Identidade: AEK Larnaca separado do EPA e do Pezoporikos; AEP Paphos separado do Evagoras e do APOP Paphos; APOEL, AEL Limassol, EPA Larnaca e Olympiakos Nicosia com o mesmo nome do gre-1.
- 2008/09: APOEL x Omonia suspenso, como derrota para os dois (a tabela da Wikipédia); 2007/08 e 2008/09: grupos intermediário e de rebaixamento pela matriz da Wikipédia (o ogol não tem).

## 10. Arquivos

- Código: `coleta/cyp-1/` (`edicoes.py`, `baixar.py`, `importar.py`); cadastro dos clubes em `coleta/comum-europa/clubes_cyp.py`.
- Fontes baixadas: `data/coleta/cyp-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-cyp-1/`.
- Pacote: `data/coleta/cyp-1/pacote/`; relatório: `docs/coleta/cyp-1.md`.
- Refazer do zero: `python coleta/cyp-1/baixar.py ...` (ver o docstring), `python coleta/cyp-1/importar.py`, `python coleta/comum-europa/testar_carga.py cyp-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

