# Campeonato Equatoriano (`ecu-1`) — documentação

Gerado por `python coleta/comum-sulamerica/documentar.py` a partir do pacote `data/coleta/ecu-1/pacote/`, do código `coleta/ecu-1/` e do relatório `docs/coleta/ecu-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 68, de 1957 a 2025; 0 sem jogos.
- **Jogos:** 14195 (14193 com placar); **gols:** 37522; **gols com autor:** 9240 (25%); **cartões:** 15824.
- **Clubes:** 63; **artilheiros:** 68 edições com artilheiro (72 linhas, com empates).
- **Classificação final:** 68 edições; **tabelas publicadas guardadas para conferência:** 2069 linhas.
- **No banco:** sim; **último commit do pacote:** 0b793ba.
- **Observação da competição:** 1ª divisão equatoriana (Serie A, hoje LigaPro) de 1957 a 2025, um campeão por ano (sem campeonato em 1958 e 1959; dois em 2005, Apertura e Clausura). Até 1967, torneio nacional entre os melhores dos campeonatos regionais de Guayaquil e de Quito/Ambato.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão equatoriana (ecu-1): uma por título de campeão equatoriano, como na lista da RSSSF (ecuachamp.html).

1957 e 1960-2025: um campeão por ano (sem campeonato nacional em 1958 e 1959); 2005 deu dois títulos (Apertura e Clausura),
uma edição cada. Até 1967 o campeonato nacional era um torneio curto entre os melhores dos campeonatos regionais
(Interandino, de Quito e Ambato, e o de Guayaquil); os regionais são outras competições e ficam de fora. Apertura,
Clausura, liguillas, hexagonais e finais são fases da edição anual. Ficam de fora a Serie B e as divisões de baixo, a Copa
Ecuador e os playoffs da Copa Sudamericana e da Copa Conmebol.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], linhas do texto puro (rsssf_sul.texto); linha final None: até o
  primeiro título de outra competição (FIM_PADRAO). Todos os anos; de 1960 a 1974 parte das fases vem em tabela de confrontos
  (ler_rsssf.confrontos).
- espn: (início, fim) das datas dos jogos que a página não traz (2011, 2012 e 2025: a RSSSF só tem as tabelas e as finais).
```

**Edições:** 68, uma por título de campeão equatoriano, de 1957 a 2025, como na lista de campeões da RSSSF (`ecuachamp.html`) e na Wikipédia em inglês (página "LigaPro Serie A", seção "Champions by year"). Um campeão por ano; sem campeonato em 1958 e 1959; em 2005 houve dois campeões (Apertura e Clausura), uma edição cada. Apertura, Clausura, etapas, liguillas, hexagonais e finais são fases da edição anual.

**Até 1967:** o campeonato nacional era um torneio curto entre os melhores dos campeonatos regionais (o Interandino, de Quito e Ambato, e o de Guayaquil); clubes da mesma associação não se enfrentavam. Os regionais são outras competições e ficam de fora. Em 1964 os clubes de Guayaquil não jogaram.

**Fontes:** RSSSF (uma página por temporada, `ecua57` e `ecua60` a `ecua2025`, em `data/coleta/ecu-1/rsssf/`: base de jogos de todos os anos, com fases, grupos, rodadas, datas e autores dos gols; de 1960 a 1974 parte das fases vem em tabela de confrontos, sem rodada nem data, com o mandante na linha); ESPN (liga `ecu.1`, 2005 em diante: os jogos de 2011, 2012 e 2025, que a RSSSF só traz em tabela, e nos outros anos hora, estádio, público, gols com minuto e cartões); Wikipédia em inglês (segunda fonte do campeão e do vice).

**Clubes:** nome pelo qual o clube é conhecido no Brasil (Emelec, LDU de Quito, Independiente del Valle). Homônimos de outros países levam a cidade: Barcelona de Guayaquil, Universidad Católica de Quito, River Plate de Manta (1963, 1966) e de Riobamba (1987, 1988), dois clubes diferentes, Libertad de Loja, Santos de El Guabo, Juventus de Esmeraldas, Santa Rita de Vinces; os Américas de Quito, Ambato e Manta também. O mesmo clube com outro nome fica com o atual: Independiente José Terán = Independiente del Valle; River Ecuador = Guayaquil City; Cuniburo = Vinotinto; Manta SC = Manta Sport (outro clube que o Manta FC, de 1998). "LDU" e "Deportivo" sozinhos, nas páginas de 1997-2002, dependem do ano (conferido com as tabelas): em 2001 a LDU da Serie A é a de Portoviejo (a de Quito jogou a Serie B).

**Regras:** o placar é o da RSSSF (ou da ESPN, nos jogos que vêm só dela). Jogo decidido no tribunal leva o placar dado (`awd`), com o de campo na observação. Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos: 2 por vitória até 1994 e 3 a partir de 1995; as liguillas e hexagonais finais começam com pontos de bônus da fase anterior (o `ajuste_pontos` da classificação). Em 1998 o empate ia para os pênaltis (2 pontos para quem ganhava, 1 para quem perdia): a tabela da página separa os empates ("5/1"), aqui somados.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 47.
- **Edições com alguma tabela divergente** (21; motivo no relatório, na edição): 1965, 1968, 1970, 1971, 1973, 1977, 1981, 1982, 1986, 1989, 1990, 1991, 1993, 1994, 1995, 1996, 1998, 2000, 2003, 2005 Apertura, 2009.
- **Edições sem tabela para conferir** (0): nenhuma.
- **Edições com menos jogos que o esperado:** nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1950s | 1 | 8 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 10 | 757 | 5% | 0% | 40% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 10 | 1954 | 0% | 0% | 54% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 10 | 2750 | 84% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 10 | 2406 | 90% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 11 | 2148 | 100% | 46% | 100% | 46% | 35% | 0% | 59% | 1.3 |
| 2010s | 10 | 2650 | 100% | 100% | 80% | 100% | 94% | 0% | 39% | 2.3 |
| 2020s | 6 | 1522 | 100% | 100% | 80% | 100% | 100% | 1% | 82% | 4.6 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na América do Sul: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1957: 4 clubes
- 1960 a 1962: 8 clubes
- 1963: 11 clubes
- 1964 a 1965: 8 clubes
- 1966: 16 clubes
- 1967: 10 clubes
- 1968: 12 clubes
- 1969: 14 clubes
- 1970: 13 clubes
- 1971: 16 clubes
- 1972: 10 clubes
- 1973: 12 clubes
- 1974: 10 clubes
- 1975 a 1982: 12 clubes
- 1983 a 1984: 14 clubes
- 1985 a 1986: 16 clubes
- 1987 a 1988: 18 clubes
- 1989 a 1992: 13 clubes
- 1993 a 1999: 12 clubes
- 2000 a 2005 Clausura: 10 clubes
- 2006: 11 clubes
- 2007: 10 clubes
- 2008 a 2018: 12 clubes
- 2019 a 2025: 16 clubes

**Pontos por vitória:**

- 1957 a 1994: 2
- 1995 a 2025: 3

**Nome oficial:**

- 1957 a 1970: Campeonato Ecuatoriano de Fútbol <ano>
- 1971 a 2004: Campeonato Ecuatoriano de Fútbol Serie A <ano>
- 2005 Apertura: Campeonato Ecuatoriano de Fútbol Serie A <ano> – Apertura
- 2005 Clausura: Campeonato Ecuatoriano de Fútbol Serie A <ano> – Clausura
- 2006 a 2017: Campeonato Ecuatoriano de Fútbol Serie A <ano>
- 2018 a 2025: LigaPro Serie A <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1957 a 1961: pontos corridos
- 1962: pontos corridos + desempate
- 1963: 2 grupos + mata-mata
- 1964 a 1965: pontos corridos + desempate
- 1966: 2 grupos + mata-mata
- 1967: pontos corridos + desempate
- 1968 a 1970: pontos corridos
- 1971: 2 grupos + pontos corridos
- 1972: pontos corridos + desempate + pontos corridos
- 1973 a 1974: pontos corridos + mata-mata
- 1975: pontos corridos
- 1976: pontos corridos + desempate + pontos corridos
- 1977: pontos corridos
- 1978: pontos corridos + desempate + pontos corridos
- 1979: pontos corridos
- 1980: pontos corridos + mata-mata
- 1981: pontos corridos + desempate + pontos corridos
- 1982: pontos corridos + mata-mata
- 1983: pontos corridos
- 1984: 2 grupos + pontos corridos + 2 grupos + pontos corridos
- 1985: pontos corridos
- 1986: 2 grupos + pontos corridos + 2 grupos + pontos corridos
- 1987: pontos corridos + 2 grupos + pontos corridos
- 1988: pontos corridos + 2 grupos + mata-mata
- 1989: pontos corridos + 2 grupos + pontos corridos
- 1990 a 1991: pontos corridos + 2 grupos + desempate + pontos corridos
- 1992: pontos corridos + 2 grupos + pontos corridos + mata-mata
- 1993: 2 grupos + desempate + pontos corridos
- 1994: pontos corridos + 2 grupos + pontos corridos
- 1995: pontos corridos + 2 grupos + pontos corridos + mata-mata
- 1996: pontos corridos + 3 grupos + pontos corridos
- 1997: 2 grupos + pontos corridos + desempate + mata-mata
- 1998: pontos corridos + mata-mata
- 1999: pontos corridos + 2 grupos + pontos corridos + mata-mata
- 2000 a 2004: pontos corridos
- 2005 Apertura: pontos corridos + mata-mata
- 2005 Clausura a 2007: pontos corridos
- 2008: pontos corridos + 2 grupos + pontos corridos
- 2009: pontos corridos + 2 grupos + desempate + mata-mata
- 2010: pontos corridos + desempate + mata-mata
- 2011: pontos corridos + desempate + pontos corridos + mata-mata
- 2012: pontos corridos + desempate + pontos corridos
- 2013: pontos corridos
- 2014 a 2015: pontos corridos + mata-mata
- 2016: pontos corridos
- 2017 a 2024: pontos corridos + mata-mata
- 2025: pontos corridos

**Fases e grupos de cada edição com mais de uma fase:**

- 1962: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1963: Primeira fase (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 1964: Primeira fase (liga); Desempate do título (mata_mata, jogo_unico)
- 1965: Primeira fase (liga); Desempate do 2º lugar (mata_mata, jogo_unico)
- 1966: Primeira fase (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 1967: Primeira fase (liga); Desempate do rebaixamento (mata_mata, jogo_unico)
- 1968: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga)
- 1970: Primeira fase (liga); Grupo do rebaixamento (liga); Fase final (liga)
- 1971: Primeira fase (grupos, 2 grupos); Grupo do rebaixamento (liga); Fase final (liga)
- 1972: Primeira fase (liga); Desempate do 2º lugar (mata_mata, jogo_unico); Segunda fase (liga); Fase final (liga)
- 1973: Primeira fase (liga); Grupo do rebaixamento (liga); Segunda fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1974: Primeira fase (liga); Segunda fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1975: Primeira fase (liga); Segunda fase (liga); Fase final (liga)
- 1976: Primeira fase (liga); Segunda fase (liga); Desempate do 2º lugar (mata_mata, ida_volta); Fase final (liga)
- 1977: Primeira fase (liga); Segunda fase (liga); Fase final (liga)
- 1978: Primeira fase (liga); Segunda fase (liga); Desempate do 2º lugar (mata_mata, ida_volta); Fase final (liga)
- 1979: Primeira fase (liga); Segunda fase (liga); Fase final (liga)
- 1980: Primeira fase (liga); Segunda fase (liga); Fase final (liga); Final (mata_mata, ida_volta)
- 1981: Primeira fase (liga); Segunda fase (liga); Desempate do 2º lugar (mata_mata, ida_volta); Fase final (liga)
- 1982: Primeira fase (liga); Segunda fase (liga); Fase final (liga); Final (mata_mata, ida_volta)
- 1983: Apertura (liga); Grupo do rebaixamento (liga); Segunda fase (liga); Fase final (liga)
- 1984: Primeira fase (grupos, 2 grupos); Grupo do rebaixamento (liga); Segunda fase (grupos, 2 grupos); Fase final (liga)
- 1985: Primeira fase (liga); Fase final (liga)
- 1986: Primeira fase (grupos, 2 grupos); Grupo do rebaixamento (liga); Segunda fase (grupos, 2 grupos); Terceira fase (grupos, 2 grupos); Fase final (liga)
- 1987: Primeira fase (liga); Segunda fase (grupos, 2 grupos); Fase final (liga)
- 1988: Primeira fase (liga); Segunda fase (grupos, 2 grupos); Final (mata_mata, ida_volta)
- 1989: Primeira fase (liga); Grupo do rebaixamento (liga); Segunda fase (grupos, 2 grupos); Fase final (liga)
- 1990: Primeira fase (liga); Grupo do rebaixamento (grupos, 2 grupos); Segunda fase (grupos, 2 grupos); Desempate do 2º lugar (mata_mata, ida_volta); Fase final (liga)
- 1991: Primeira fase (liga); Grupo do rebaixamento (grupos, 2 grupos); Segunda fase (grupos, 2 grupos); Desempate do 2º lugar (mata_mata, ida_volta); Fase final (liga)
- 1992: Primeira fase (liga); Grupo do rebaixamento (liga); Segunda fase (grupos, 2 grupos); Fase final (liga); Final (mata_mata, ida_volta)
- 1993: Primeira fase (grupos, 2 grupos); Segunda fase (grupos, 2 grupos); Desempate do 2º lugar (mata_mata, ida_volta); Triangular do 2º lugar (liga); Fase final (liga)
- 1994: Primeira fase (liga); Grupo do rebaixamento (liga); Segunda fase (grupos, 2 grupos); Fase final (liga)
- 1995: Primeira fase (liga); Grupo do rebaixamento (liga); Liguillas (liga); Segunda fase (grupos, 2 grupos); Fase final (liga); Final (mata_mata, ida_volta)
- 1996: Apertura (liga); Clausura (grupos, 3 grupos); Grupo do rebaixamento (liga); Liguillas (liga)
- 1997: Apertura (grupos, 2 grupos); Clausura (liga); Desempate do rebaixamento (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1998: Apertura (liga); Liguillas do Apertura (liga); Grupo do rebaixamento do Apertura (liga); Clausura (liga); Liguillas do Clausura (liga); Grupo do rebaixamento do Clausura (liga); Final (mata_mata, ida_volta)
- 1999: Apertura (liga); Segunda fase (grupos, 2 grupos); Fase final (liga); Final (mata_mata, ida_volta)
- 2000: Apertura (liga); Clausura (liga); Fase final (liga)
- 2001: Apertura (liga); Clausura (liga); Fase final (liga)
- 2002: Apertura (liga); Clausura (liga); Fase final (liga)
- 2003: Apertura (liga); Finalización (liga); Fase final (liga)
- 2004: Apertura (liga); Finalización (liga); Fase final (liga)
- 2005 Apertura: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2005 Clausura: Primeira fase (liga); Fase final (liga)
- 2006: Apertura (liga); Clausura (liga); Fase final (liga)
- 2007: Primeira fase (liga); Segunda fase (liga); Fase final (liga)
- 2008: Primeira fase (liga); Segunda fase (grupos, 2 grupos); Fase final (liga)
- 2009: Primeira fase (liga); Segunda fase (grupos, 2 grupos); Terceira fase (grupos, 2 grupos); Desempate do 2º lugar (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2010: Primeira fase (liga); Segunda fase (liga); Desempate do 2º lugar (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2011: Primeira fase (liga); Desempate do 2º lugar (mata_mata, ida_volta); Segunda fase (liga); Final (mata_mata, ida_volta)
- 2012: Primeira fase (liga); Desempate do 2º lugar (mata_mata, ida_volta); Segunda fase (liga)
- 2013: Primeira fase (liga); Segunda fase (liga)
- 2014: Primeira fase (liga); Segunda fase (liga); Final (mata_mata, ida_volta)
- 2015: Primeira fase (liga); Segunda fase (liga); Final (mata_mata, ida_volta)
- 2016: Primeira fase (liga); Segunda fase (liga)
- 2017: Primeira fase (liga); Segunda fase (liga); Final (mata_mata, ida_volta)
- 2018: Primeira fase (liga); Segunda fase (liga); Final (mata_mata, ida_volta)
- 2019: Primeira fase (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2020: Primeira fase (liga); Segunda fase (liga); Final (mata_mata, ida_volta)
- 2021: Primeira fase (liga); Segunda fase (liga); Final (mata_mata, ida_volta)
- 2022: Primeira fase (liga); Segunda fase (liga); Final (mata_mata, ida_volta)
- 2023: Primeira fase (liga); Segunda fase (liga); Final (mata_mata, ida_volta)
- 2024: Primeira fase (liga); Segunda fase (liga); Final (mata_mata, ida_volta)
- 2025: Primeira fase (liga); Grupo do rebaixamento (liga); Hexagonal 2 (liga); Fase final (liga)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 43 edições
- calculada: 25 edições

**Observações das edições:**

- nenhuma

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Barcelona de Guayaquil: 16
- Emelec: 14
- El Nacional: 13
- LDU de Quito: 13
- Deportivo Quito: 5
- Independiente del Valle: 2
- Everest: 1
- Olmedo: 1
- Deportivo Cuenca: 1
- Delfín: 1
- Aucas: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1957 | Emelec | Barcelona de Guayaquil |
| 1960 | Barcelona de Guayaquil | Emelec |
| 1961 | Emelec | Patria |
| 1962 | Everest | Barcelona de Guayaquil |
| 1963 | Barcelona de Guayaquil | Emelec |
| 1964 | Deportivo Quito | El Nacional |
| 1965 | Emelec | 9 de Octubre |
| 1966 | Barcelona de Guayaquil | Emelec |
| 1967 | El Nacional | Emelec |
| 1968 | Deportivo Quito | Barcelona de Guayaquil |
| 1969 | LDU de Quito | América de Quito |
| 1970 | Barcelona de Guayaquil | Emelec |
| 1971 | Barcelona de Guayaquil | América de Quito |
| 1972 | Emelec | El Nacional |
| 1973 | El Nacional | Universidad Católica de Quito |
| 1974 | LDU de Quito | El Nacional |
| 1975 | LDU de Quito | Deportivo Cuenca |
| 1976 | El Nacional | Deportivo Cuenca |
| 1977 | El Nacional | LDU de Quito |
| 1978 | El Nacional | Técnico Universitario |
| 1979 | Emelec | Universidad Católica de Quito |
| 1980 | Barcelona de Guayaquil | Técnico Universitario |
| 1981 | Barcelona de Guayaquil | LDU de Quito |
| 1982 | El Nacional | Barcelona de Guayaquil |
| 1983 | El Nacional | 9 de Octubre |
| 1984 | El Nacional | 9 de Octubre |
| 1985 | Barcelona de Guayaquil | Deportivo Quito |
| 1986 | El Nacional | Barcelona de Guayaquil |
| 1987 | Barcelona de Guayaquil | Filanbanco |
| 1988 | Emelec | Deportivo Quito |
| 1989 | Barcelona de Guayaquil | Emelec |
| 1990 | LDU de Quito | Barcelona de Guayaquil |
| 1991 | Barcelona de Guayaquil | Valdez SC |
| 1992 | El Nacional | Barcelona de Guayaquil |
| 1993 | Emelec | Barcelona de Guayaquil |
| 1994 | Emelec | El Nacional |
| 1995 | Barcelona de Guayaquil | Espoli |
| 1996 | El Nacional | Emelec |
| 1997 | Barcelona de Guayaquil | Deportivo Quito |
| 1998 | LDU de Quito | Emelec |
| 1999 | LDU de Quito | El Nacional |
| 2000 | Olmedo | El Nacional |
| 2001 | Emelec | El Nacional |
| 2002 | Emelec | Barcelona de Guayaquil |
| 2003 | LDU de Quito | Barcelona de Guayaquil |
| 2004 | Deportivo Cuenca | Olmedo |
| 2005 Apertura | LDU de Quito | Barcelona de Guayaquil |
| 2005 Clausura | El Nacional | Deportivo Cuenca |
| 2006 | El Nacional | Emelec |
| 2007 | LDU de Quito | Deportivo Cuenca |
| 2008 | Deportivo Quito | LDU de Quito |
| 2009 | Deportivo Quito | Deportivo Cuenca |
| 2010 | LDU de Quito | Emelec |
| 2011 | Deportivo Quito | Emelec |
| 2012 | Barcelona de Guayaquil | Emelec |
| 2013 | Emelec | Independiente del Valle |
| 2014 | Emelec | Barcelona de Guayaquil |
| 2015 | Emelec | LDU de Quito |
| 2016 | Barcelona de Guayaquil | Emelec |
| 2017 | Emelec | Delfín |
| 2018 | LDU de Quito | Emelec |
| 2019 | Delfín | LDU de Quito |
| 2020 | Barcelona de Guayaquil | LDU de Quito |
| 2021 | Independiente del Valle | Emelec |
| 2022 | Aucas | Barcelona de Guayaquil |
| 2023 | LDU de Quito | Independiente del Valle |
| 2024 | LDU de Quito | Independiente del Valle |
| 2025 | Independiente del Valle | LDU de Quito |

**Rebaixados marcados na classificação:** 52 em 27 edições (só onde a tabela publicada marca a queda); quem mais caiu: Macará (5), Olmedo (4), Imbabura (3), Manta FC (3), Manta Sport (2).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1964: Macará -1
- 1964: América de Ambato +2
- 1998: LDU de Quito +5
- 1998: Emelec +4
- 1998: Aucas +5
- 1998: Olmedo +5
- 1998: Espoli +2
- 1998: Barcelona de Guayaquil +3
- 1998: Delfín +3
- 1998: El Nacional +2
- 1998: Deportivo Quito +2
- 1998: Técnico Universitario +4
- 1998: Panamá +2
- 2015: Barcelona de Guayaquil -2
- 2015: El Nacional -1
- 2015: LDU de Loja -4
- 2015: Deportivo Quito -8
- 2017: Barcelona de Guayaquil -6
- 2017: Fuerza Amarilla -5
- 2019: El Nacional -1
- 2019: Deportivo Cuenca -1
- 2019: Fuerza Amarilla -5
- 2024: El Nacional -3
- 2024: Emelec -3
- 2024: Deportivo Cuenca -3
- 2024: Libertad de Loja -4

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/ecu-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 22)

- **ecua64 · 46:** «Deportivo Quito 1 0 LDU Quito» → «Deportivo Quito 1-0 LDU Quito»: placar sem o hífen ("1 0")
- **ecua64 · 37:** «4.Amèrica» → «4.América de Manta»: "Amèrica" [Manta] na tabela: o América de Manta ("AmM" na tabela de confrontos)
- **ecua64 · 41:** «8.América» → «8.América de Ambato»: "América" [Ambato] na tabela: o América de Ambato ("AmA")
- **ecua66 · 32:** «4.América» → «4.América de Ambato»: "América" [Ambato] na tabela do grupo A: o América de Ambato ("AmA" na tabela de confrontos)
- **ecua66 · 65:** «Patria                5» → «Patria                6»: grupo A da Costa com 5 jogos por clube na tabela; são 6 (turno e returno entre 4 clubes, como a tabela de confrontos e V+E+D)
- **ecua66 · 66:** «Emelec                5» → «Emelec                6»: grupo A da Costa com 5 jogos por clube na tabela; são 6 (turno e returno entre 4 clubes, como a tabela de confrontos e V+E+D)
- **ecua66 · 67:** «9 de Octubre          5» → «9 de Octubre          6»: grupo A da Costa com 5 jogos por clube na tabela; são 6 (turno e returno entre 4 clubes, como a tabela de confrontos e V+E+D)
- **ecua66 · 68:** «4.América               5» → «4.América de Manta       6»: "América" [Manta] na tabela do grupo A da Costa: o América de Manta ("AmM"); são 6 jogos, não 5
- **ecua73 · 114:** «LDU de Quito» → «Barcelona»: a LDU de Quito não jogou a Serie A de 1973; o terceiro jogo da semifinal foi El Nacional 2-0 Barcelona, em Cuenca (Wikipédia em espanhol)
- **ecua05 · 563:** «Deportivo Quevedo» → «Olmedo»: o Deportivo Quevedo caiu no Apertura; os três gols do visitante são de Celso Cuero, do Olmedo, e a tabela do Clausura conta esse jogo para o Olmedo
- **ecua85 · 19:** «30 18  8  8» → «30 18  8  4»: Filanbanco com 18 vitórias, 8 empates e 8 derrotas em 30 jogos (dá 34); são 4 derrotas, como os 44 pontos (2 x 18 + 8) e os jogos da página
- **ecua85 · 403:** «30 18  8  8» → «30 18  8  4»: Filanbanco com 18 vitórias, 8 empates e 8 derrotas em 30 jogos (dá 34); são 4 derrotas, como os 44 pontos (2 x 18 + 8) e os jogos da página
- **ecua85 · 438:** «9 de octubre» → «9 de Octubre»: nome em minúscula (o leitor de tabela espera "9 de Octubre")
- **ecua85 · 558:** «9 de octubre» → «9 de Octubre»: nome em minúscula (o leitor de tabela espera "9 de Octubre")
- **ecua99 · 407:** «Championship Final:» → «Liguilla Final:»: o título "Championship Final" abre a liguilla final de pontos corridos (a final de ida e volta vem depois, na linha 489)
- **ecua05 · 333:** «» → «Quarterfinals»: as quartas de final do Apertura não têm título (só a nota "top-8 qualify for knock-out stage (quarterfinals)"): a linha em branco antes dos jogos vira o título
- **ecua06 · 227:** «Olmedo                1-0 Emelec» → «Olmedo                1-0 Deportivo Cuenca»: o Emelec aparece duas vezes na 13ª rodada do Apertura e o Deportivo Cuenca nenhuma; a tabela do Apertura conta a derrota por 0-1 para o Cuenca
- **ecua06 · 556:** «Aucas                  -  Deportivo Azogues» → «Aucas                 2-0 Deportivo Azogues»: jogo sem placar; os dois gols listados são do Aucas (Palacios, Rodríguez) e a tabela do Clausura conta o 2-0
- **ecua07 · 222:** «Deportivo Quito        -  Macará» → «Deportivo Quito       1-0 Macará»: jogo sem placar; um gol listado (Vinces, do Deportivo Quito) e a tabela da 1ª etapa conta o 1-0
- **ecua98 · 418:** «Emelec dns for 2nd half;» → «Emelec dns for 2nd half; apparently awarded 2-0]»: a nota do jogo dado continua na linha de baixo, junto do jogo seguinte
- **ecua98 · 419:** «Espoli       apparently awarded 2-0]» → «Espoli»: fim da nota do jogo de cima (linha 418), não deste
- **ecua98 · 624:** «Championship» → «Championship Final»: título da final entre os campeões do Apertura e do Clausura ("Playoffs: / Championship")

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 6)

- **1998 · ecua98:129:** [vale o placar de campo] jogo interrompido por invasão de campo aos 81 minutos, com 1-2, e terminado em 16 de maio (nota da página): vale o 1-2, como a tabela conta
- **2003 · ecua03:46:** [descartado] jogo interrompido e completado depois: a página traz as duas linhas ("abd" e a do restante do jogo, com o placar final); fica a segunda
- **2006 · ecua06:260:** [descartado] jogo interrompido e completado depois: a página traz as duas linhas ("abd" e a do restante do jogo, com o placar final); fica a segunda
- **2024 · ecua2024:106:** [descartado] jogo interrompido e completado depois: a página traz as duas linhas ("abd" e a do restante do jogo, com o placar final); fica a segunda
- **2025 · espn:759348:** [não jogado] último jogo do Hexagonal 2 (El Nacional x Delfín, 19/12): a RSSSF diz que não foi disputado e as tabelas contam 39 jogos para os dois; a ESPN registra 0-3 (provável W.O. do El Nacional, rebaixado por dívidas)
- **1998 · ecua98:418:** [decidido fora de campo, placar oficial 2-0] jogo abandonado no intervalo com 2-0 (o Emelec não voltou para o 2º tempo) e dado ao Deportivo Quito por 2-0 (nota da página), como a tabela do Hexagonal 1 conta

### Identidade dos clubes

Regras em `coleta/ecu-1/clubes_ecu.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes equatorianos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido no Brasil ("Emelec", "LDU de Quito", "Independiente del Valle", "El Nacional");
- homônimo de clube do banco ou de outro pacote leva a cidade: "Barcelona de Guayaquil" (o Barcelona é o espanhol),
  "Universidad Católica de Quito" (a Universidad Católica é a chilena), "River Plate de Manta" (1963, 1966) e "River Plate
  de Riobamba" (1987, 1988), dois clubes diferentes (Wikipédia em espanhol), "Libertad de Loja",
  "Santos de El Guabo", "Juventus de Esmeraldas", "Santa Rita de Vinces"; os Américas de Quito, Ambato e Manta levam a cidade;
- o mesmo clube com outro nome em outra época fica com o nome atual: Independiente José Terán (até 2014) é o Independiente
  del Valle; River Ecuador (2015-2016) é o Guayaquil City; Cuniburo (até 2025) é o Vinotinto; Manta Sport Club ("Manta SC",
  "Manta Sport") é um só clube, diferente do Manta FC (fundado em 1998);
- clubes diferentes com o mesmo nome: LDU de Quito, LDU de Portoviejo, LDU de Cuenca e LDU de Loja; UD Valdez (Milagro, 1978)
  e Valdez SC (Milagro, 1991-1994, que recebeu a vaga do Filanbanco); "LDU" e "Deportivo" sozinhos, nas páginas de
  1997-2002, dependem do ano (regras abaixo, conferidas com as tabelas da página).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
```

## 8. O que não deu para coletar

- **Fora do pacote:** os campeonatos regionais, a Serie B e as divisões de baixo, a Copa Ecuador, a Supercopa de 1969 e os playoffs da Copa Sudamericana e da Copa Conmebol.
- **Edições sem jogos** (0): nenhuma.
- **Décadas com menos da metade dos gols com autor:** 1950s, 1960s, 1970s, 1980s, 1990s, 2010s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1950s, 1960s, 1970s, 1980s, 1990s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- ESPN sem lances de 2014 a 2020: gols com minuto e cartões desses anos só jogo a jogo (outra fonte).

**Achados da revisão em aberto** (`docs/revisao/achados.csv`, provas em `docs/revisao/ecu-1.md`):

- EC-001 (alta) B classificação (tabela de uma fase só) — 1970, 1975, 1983, 1985, 1987, 1988, 1994, 1995, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005 Clausura, 2007, 2008, 2009, 2019, 2025: Wikipédia es (Historial, campeão/vice/3º/4º) e a tabela da fase final da própria RSSSF (no tabelas_publicadas.csv do pacote) dão outra ordem: 2000 Emelec 3º, Aucas 4º; 1975 Aucas 3º, Barcelona 4º; 1987 Audaz Octubrino 3º
- EC-002 (alta) B classificação (calculada ignora a fase final) — 1966, 1977, 1979, 1984, 1986, 1989, 1990, 1992, 2006: Tabela da fase final (RSSSF, no tabelas_publicadas.csv) e Wikipédia es: 1977 Universidad Católica 3º, Barcelona 4º; 1990 Emelec 3º (perdeu o desempate do 2º), El Nacional 4º; 2006 LDU de Quito 3º, Olmedo 4º; 1966 Politéc
- EC-003 (alta) B classificação / C fases (disputa de 3º e 4º lugar) — 2009, 2010, 2011, 2012: RSSSF ecua2010 linha 784 'Third Place Matches' (Deportivo Quito 2-0 e 1-3 Barcelona: Deportivo Quito 3º pelo gol fora); ecua2011 linha 76 (El Nacional 2-1 e 1-1 LDU); ecua2012 linha 77 'Fourth Place Matches' [Dec 8] LDU 
- EC-004 (alta) B rebaixados (faltam) — 1967, 1968, 1970-1981, 1983, 1984, 1986, 1988-2000, 2003, 2005 Apertura, 2006, 2009: Wikipédia es, seção 'Ascensos y descensos a la Serie A' (tabela ano a ano), e as próprias páginas da RSSSF (linhas 'Relegated' das tabelas de fase e notas 'X relegated', ex.: ecua00 linhas 402-403, ecua94 linha 465, ecua
- EC-005 (alta) B rebaixados e punição (2025) — 2025: RSSSF ecua2025 (Relegation Group, linhas 81-85): Manta FC 13º e Mushuc Runa 14º se salvaram; Hexagonal 2 (linha 70): El Nacional [-9] Relegated, 'relegated for third failure to meet payment deadline'. Wikipédia es 'Serie
- EC-006 (media) C fases (1999: 'No Descenso' dentro da Final) — 1999: RSSSF ecua99 linha 501 'No Descenso:' (tabela e 10 rodadas, linhas 503-579; Delfín, Deportivo Cuenca e Audaz Octubrino rebaixados). | SUGESTÃO: os 30 jogos na fase 'Grupo do rebaixamento' (liga); fonte: https://www.rsssf
- EC-007 (media) C fases (liguilla final tratada como mata-mata) — 1963, 1966, 1997: RSSSF: ecua63 linha 64 'Final' + 'Cross-Table' de 4 clubes em turno e returno (Barcelona campeão por pontos); ecua66 linha 90 'Final' + tabela de confrontos de 8 clubes; ecua97 linha 393 'Championship Playoff' = hexagona
- EC-008 (media) C jogos repetidos (20) — 1984, 1986, 1994: A página da RSSSF traz esses jogos dentro das rodadas da fase final E na seção do rebaixamento (ecua84 linhas 483/617 etc.; ecua86 541/688 etc.; ecua94 484/460 e 494/463). Wikipédia es: 1984 3º LDU de Quito, 4º Universid
- EC-009 (media) C datas (finais e mata-mata com a data da rodada anterior) — 1998, 1999, 2005 Apertura, 2009, 2010, 2012, 2014, 2015, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024: A própria página traz a data no título do bloco ('First Leg [Dec 17]', 'Second Legs [Jul 10]'): ex.: ecua2014 linhas 561/564 = 17/12 e 21/12/2014 (ESPN 410587 e 410586 também); ecua98 linhas 626/629 = 23/12 e 27/12/1998 
- EC-010 (media) C datas e fase (1997 rebaixamento) — 1997: RSSSF ecua97 linhas 467-498: 'Playoff Descenso', tabela de 4 clubes, Round 2 [Dec 7] ... Round 6 [Dec 21], disputado junto com o hexagonal final de dez/1997 (que vai a jan/1998). | SUGESTÃO: datas 1997-12-07 a 1997-12-21
- EC-011 (media) C placar (2005 Apertura, Emelec x LDU de Quito) — 2005 Apertura: A linha da RSSSF (ecua05 linha 53) diz 0-2, mas a lista de autores logo abaixo tem 2 gols de cada lado: 'Rubén FORESTELLO 88, 90+1; Ariel GRAZIANI 30, 39'. Com 2-2, LDU [18,13,2,3,48,22] e Emelec [18,5,5,8,24,31] fecham 
- EC-012 (media) C jogos decididos fora de campo (1965, Aucas) — 1965: RSSSF ecua65 linhas 39, 46, 53 e 72: '(Aucas lost match by player(s) not elegible)'. Com as 4 derrotas do Aucas, a tabela (linhas 21-28) fecha: Aucas 0V 1E 7D, Barcelona 4V 3E 1D, 9 de Octubre 5V, Patria 5V. | SUGESTÃO: 
- EC-013 (media) D gols (gol a mais) — 2007: Placar 4-0 na RSSSF (ecua07 linha 283) e na ESPN (evento 214438); o 'Luis Escalada' do Cuenca é repetição do 'Luis Miguel Escalada' da LDU (61'). | SUGESTÃO: tirar o gol do Deportivo Cuenca; aplicar também aos gols da ES
- EC-014 (media) D artilheiros (número de gols) — 1988, 1996, 1999: Wikipédia es (Goleadores por temporada): 1988 Janio Pinto 19; 1996 Ariel Graziani 30; 1999 Cristian Bottero 24. Os outros 65 batem. | SUGESTÃO: conferir numa 3ª fonte (RSSSF ecuatops x Wikipédia es) e, se for o caso, cor
- EC-015 (media) C placar (2025, El Nacional x Delfín) — 2025: ESPN (evento 759348) dá 0-3 e a Wikipédia es 'Serie A de Ecuador 2025' conta o jogo (Delfín 33 gols pró = 30 da RSSSF + 3); só a RSSSF diz 'remaining match not played'. El Nacional já estava rebaixado administrativamente
- EC-016 (baixa) C ordem das fases — 1983, 1984, 1986, 1989, 1990, 1991, 1992, 1994, 1995, 1997: Datas do próprio pacote (varredura: ex.: 1984 Segunda fase 16/06-19/08, Grupo do rebaixamento 26/08-30/09). | SUGESTÃO: ordenar as fases pela data do 1º jogo (ou linha da página), não por NIVEL_FASE; fonte: https://www.r
- EC-017 (baixa) C datas (página com data trocada) — 1988, 2006: ESPN (2006): Barcelona 1-0 Liga de Quito em 29/10/2006. 1988: a página (ecua88 linha 174) dá [Apr 20] para um jogo da rodada 11 (rodada 10 foi 23-24/04): provável 30/04. | SUGESTÃO: 2006 = 2006-10-29 (ESPN); 1988 conferi
- EC-024 (baixa) F maior goleada (1969) — 1969: Wikipédia es (Liga Deportiva Universitaria de Quito, Datos del club): 11-0 contra América de Ambato em 26/10/1969. | SUGESTÃO: pôr a data 1969-10-26; fonte: https://es.wikipedia.org/wiki/Liga_Deportiva_Universitaria_de_Q

## 10. Arquivos e comandos

Código em `coleta/ecu-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga ecu.1) de 2001 a 2025 para data/coleta/ecu-1/espn/ecu1_<ano>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão equatoriana para data/coleta/ecu-1/rsssf/. |
| `baixar_wikipedia.py` | Baixa da Wikipédia em inglês a página da liga ("LigaPro Serie A", com a lista de campeões) para |
| `campeoes_wiki.py` | Lista de campeões da Wikipédia em inglês (página "LigaPro Serie A", seção "Champions by year"), segunda fonte do campeão e |
| `clubes_ecu.py` | Identidade dos clubes equatorianos: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão equatoriana (ecu-1): uma por título de campeão equatoriano, como na lista da RSSSF (ecuachamp.html). |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão equatoriana, edição a edição (entram no relatório). |
| `importar.py` | Junta as fontes da 1ª divisão equatoriana e grava o pacote em data/coleta/ecu-1/pacote/ e o relatório em docs/coleta/ecu-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição nas páginas da RSSSF (data/coleta/ecu-1/rsssf/) com o leitor comum (rsssf_sul) e, de 1960 a |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol e com a ESPN. |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |

- Fontes baixadas: `data/coleta/ecu-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-sulamerica/`.
- Pacote: `data/coleta/ecu-1/pacote/`; relatório: `docs/coleta/ecu-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/ecu-1/baixar_espn.py
python coleta/ecu-1/baixar_rsssf.py
python coleta/ecu-1/baixar_wikipedia.py
python coleta/ecu-1/importar.py
python coleta/ecu-1/conferir.py [-v temporada]   # divergências
python coleta/comum-sulamerica/testar_carga.py ecu-1 <scratchpad>
python coleta/comum-sulamerica/documentar.py
```

