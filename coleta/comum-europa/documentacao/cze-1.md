# Campeonato Tcheco (`cze-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/cze-1/pacote/` e do importador `coleta/cze-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/cze-1.md`.

## 1. O que temos

- **Edições:** 33, de 1993/94 a 2025/26.
- **Jogos:** 8234; **gols:** 21097; **gols com autor:** 7121 (34%); **cartões:** 0; **jogos com estatísticas** (chutes, faltas, escanteios): 0.
- **Clubes:** 35; **artilheiros:** 33 temporadas com artilheiro (36 linhas, com empates).
- **Classificação final:** 33 temporadas; **rodada a rodada:** 33 temporadas.
- **Tabelas publicadas guardadas para conferência:** 1080 linhas, de 62 tabelas.
- **Observação da competição:** Liga da República Tcheca desde a separação da Tchecoslováquia (1993/94): 1. liga, Gambrinus liga, Fortuna liga e Chance liga. Pontos corridos; em 2018/19, 2019/20 e desde 2021/22, fase regular e grupos (título, rebaixamento e, desde 2022/23, play-off europeu em mata-mata). A liga tchecoslovaca (1925-1993) e a do Protetorado da Boêmia e Morávia (1938/39-1943/44) estão na competição da Tchecoslováquia. Não inclui os jogos de acesso contra clubes da 2ª divisão.

## 2. Fontes e regras

**Fontes:**

- ogol (zerozero): base dos jogos, com data e rodada; o clube pelo código do ogol; calendários em `data/cache/ogol-cze-1/` para os escudos;
- Wikipédia (en): tabelas da fase regular e dos grupos (ordem oficial, punições), matriz de resultados (conferência e placar dos jogos decididos fora de campo);
- RSSSF: tabela final e jogos de cada temporada (conferência; autores dos gols de 1998/99 a 2011/12), lista de campeões e de artilheiros.

**Regras da importação:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a da Wikipédia. Com grupos (2018/19, 2019/20 e desde 2021/22), a classificação final é o grupo do título, depois do 7º ao 10º pela fase regular, depois o grupo de rebaixamento, com os números de todos os jogos da liga (o play-off europeu fica fora da conta). 2 pontos por vitória em 1993/94 e 3 depois. Rebaixado = clube que não está na 1ª divisão na temporada seguinte.

**Desempate:** o critério calculado que reproduz a ordem oficial (confronto direto em 33, saldo em 0, vitórias em 0).

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 75 tabelas fecham com os jogos e 1 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: nenhuma.
- Temporadas com alguma tabela divergente: 2009/10.
- Temporadas com número de jogos diferente do turno e returno completo: 2018/19 (276 de 240), 2019/20 (271 de 240), 2021/22 (276 de 240), 2022/23 (276 de 240), 2023/24 (277 de 240), 2024/25 (276 de 240), 2025/26 (276 de 240).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1990s | 1680 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 26% | 0.0 |
| 2000s | 2400 | 100% | 59% | 100% | 0% | 0% | 0% | 0% | 95% | 0.0 |
| 2010s | 2467 | 100% | 99% | 97% | 0% | 0% | 0% | 0% | 9% | 0.0 |
| 2020s | 1687 | 100% | 100% | 91% | 0% | 0% | 0% | 0% | 0% | 0.0 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1993/94 a 2019/20: 16 clubes
- 2020/21: 18 clubes
- 2021/22 a 2025/26: 16 clubes

**Pontos por vitória:**

- 1993/94 a 2025/26: 3

**Nome oficial:**

- 1993/94 a 1996/97: 1. liga
- 1997/98 a 2013/14: Gambrinus liga
- 2014/15 a 2023/24: Fortuna liga
- 2024/25 a 2025/26: Chance liga

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- 2018/19: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta)
- 2019/20: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta)
- 2021/22: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta)
- 2022/23: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta)
- 2023/24: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta)
- 2024/25: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta)
- 2025/26: Fase regular (liga, pontos_corridos); Grupo do título (grupos, pontos_corridos); Grupo de rebaixamento (grupos, pontos_corridos); Play-off europeu (mata_mata, ida_volta)

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos, confronto direto, saldo de gols, gols pró: 33 temporadas
- pontos acumulados com a fase regular: 14 temporadas
- soma dos placares, com prorrogação: 7 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 2004/05: punições: Slovan Liberec -6 pontos; Slovácko -12 pontos; Opava -6 pontos
- 2009/10: punições: Bohemians Střížkov -15 pontos
- 2011/12: punições: Sigma Olomouc -9 pontos

## 6. Campeões, rebaixados e punições

**Títulos:**

- Sparta Praga: 14
- Slavia Praga: 9
- Viktoria Plzeň: 6
- Slovan Liberec: 3
- Baník Ostrava: 1

**Rebaixamentos:** 62 no total; quem mais caiu: Dynamo České Budějovice (6), Bohemians 1905 (5), Hradec Králové (5), Karviná (4), Opava (4).

**Punições em pontos:**

- 2004/05: Slovan Liberec -6
- 2004/05: Slovácko -12
- 2004/05: Opava -6
- 2009/10: Bohemians Střížkov -15
- 2011/12: Sigma Olomouc -9

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/cze-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Placares corrigidos (`CORRECOES`)

- **2015/16 · FK Dukla Praga · Slovan Liberec:** [2, 0] o ogol dá 1-0; a matriz da Wikipédia, a página da RSSSF e as tabelas da RSSSF e da Wikipédia dão 2-0

### Jogos decididos fora de campo, com o placar oficial dado à mão (`DECIDIDOS`)

- **2025/26 · Slavia Praga · Sparta Praga:** [0, 3] abandonado nos acréscimos com 3-2 para o Slavia, depois da invasão de campo da torcida do Slavia; em 12/05/2026 a liga deu 3-0 ao Sparta (nota da matriz da Wikipédia)

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1995/96:** a matriz da Wikipédia dá Baník Ostrava 0-1 Viktoria Žižkov e 3-1 Dynamo České Budějovice; o ogol dá 2-2 e 0-1, e as tabelas da RSSSF e da Wikipédia fecham com o ogol: erro da matriz

## 8. O que não deu para coletar

- **Autores dos gols fora de 1998/99-2011/12, cartões, público, estádio e árbitro:** a ESPN e o football-data não cobrem a Tchéquia, e a RSSSF só traz os autores nessas temporadas; o resto, só a ficha de cada jogo no ogol (jogo a jogo).
- **Jogos de acesso e rebaixamento contra clubes da 2ª divisão:** ficam de fora.

## 9. Pendências

- nenhuma em aberto na coleta.

**Limites de fonte (fechados):** nenhuma fonte em lote tem o dado; só volta com uma fonte nova.

- Autores dos gols só de 1998/99 a 2011/12 (página da RSSSF, quando a conta fecha com o placar: 7.121 gols); antes e depois, nenhuma fonte em lote (a ESPN e o football-data não cobrem a Tchéquia). Sem cartões, público, estádio e árbitro: só a ficha de cada jogo no ogol, jogo a jogo.
- Jogos de acesso e rebaixamento contra clubes da 2ª divisão ficam de fora.
- A liga tchecoslovaca (1925-1993) e a do Protetorado (1938/39-1943/44) ficam na competição da Tchecoslováquia (decisão do Guilherme, 25/11/2026).

**Com o agente de revisão:** decisões da coleta que ele confere.

- Identidade: o Dukla Praha histórico (1993/94) separado do 1. FK Příbram (o ogol usa o mesmo código) e do FK Dukla Praha de hoje; Bohemians 1905 x Bohemians de Střížkov (2008/09 e 2009/10).
- Classificação com grupos (2018/19, 2019/20, desde 2021/22): do 7º ao 10º pela fase regular (o play-off europeu não muda a posição).

## 10. Arquivos

- Código: `coleta/cze-1/` (`edicoes.py`, `baixar.py`, `importar.py`, leitor da RSSSF); cadastro dos clubes em `coleta/comum-europa/clubes_cze.py`.
- Fontes baixadas: `data/coleta/cze-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-cze-1/`.
- Pacote: `data/coleta/cze-1/pacote/`; relatório: `docs/coleta/cze-1.md`.
- Refazer do zero: `python coleta/cze-1/baixar.py ...` (ver o docstring), `python coleta/cze-1/importar.py`, `python coleta/comum-europa/testar_carga.py cze-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

