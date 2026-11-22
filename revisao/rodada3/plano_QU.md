# Plano de correção: Argentino (arg-1) e Uruguaio (uru-1)

Revisor QU, 22/11/2026. Todos os ids abertos das duas competições (AR, UY) e os novos (QU), por prioridade (gravidade x tamanho x custo),
agrupados por quem corrige e pelo arquivo do código. [NO AR] = alto e visível no site hoje. A sugestão de cada id está em
`SCRATCH/sugestoes_QU.csv` (ou no `o_que_a_fonte_diz` do achados.csv / `SCRATCH/achados_QU.csv`). Depois de cada bloco: reimportar
(`python coleta/arg-1/importar.py`, `python coleta/uru-1/importar.py`), `conferir.py`, teste de carga e `documentar.py`.

## coleta-sulamerica: Argentino (`coleta/arg-1/`)

### 1. Pódio e campeão (altos, NO AR; custo baixo, tudo com dado já no disco)
1. `edicoes.py`, `_EST_LP` e trecho da 1913 Federación: **AR-001 [NO AR]**, **QU-001**, **AR-011 [NO AR]**. Acrescentar 'CA Estudiantes' e
   'Club Atlético Estudiantes' ao `_EST_LP`; trecho ('arg13', 377, 585). Resolve campeão (Estudiantes LP), vice (GEBA), 3º, o cartão
   "29 campeões" e o 6/7 títulos do Estudiantes. Fonte: RSSSF arg13 (linhas 385-394, 574-607), es.
2. `campeoes_wiki.py` (+ `importar.montar()`): vices e 3º da lista oficial (en_campeoes.txt, já baixado): **AR-002, AR-003, AR-004, AR-005,
   AR-006, AR-007, AR-008, AR-009, AR-010, AR-012, AR-013 [todos NO AR]**, AR-014, AR-015. Uma mudança só acerta os 12 vices e os 3º.
3. `importar.py`, `classificacao()` com TABELA_OFICIAL (tabela publicada da RSSSF arghist/es quando os jogos não fecham): AR-006, AR-007,
   AR-008, AR-009, AR-010, AR-012, AR-013, AR-020 (tabelas do amadorismo, 1895-1931, e 1965). Custo baixo (`conferir._hist()` já lê as
   tabelas). Junto: `conferir.soma()` dar o W.O. sem lado (AR-012) e não somar 'Desempate do rebaixamento' (AR-016, AR-003).
4. Casos pontuais: **AR-016 [NO AR]** (`explicacoes.CONSERTA_TEXTO` arg49:246, Gimnasia x Estudiantes LP; desempate fora da tabela);
   AR-004 (punições -2 de 1989/90: AJUSTES ou tabela publicada) e QU-004 (Newell's x Boca 08/04/1990: conferir 1-2 x 0-2); AR-003
   (CORRIGE Instituto x San Lorenzo 08/05/1988); AR-005 (mini-tabela do triangular de 2008/09 Apertura); AR-002 (fases= da 1976 Nacional,
   'Desempate do grupo').

### 2. Datas (médio, grande: ~3.900 jogos; custo médio)
5. `importar.py` (pós-processamento `acerta_ano`) ou `comum-sulamerica/rsssf_sul.py` (`fixa_data`): **AR-022** com o escopo do **QU-002**.
   Regra validada em `revisao/QU/sim_ano.py` (95,5% de acerto contra o historiadeboca, 3.495 datas; lista pronta em
   `revisao/QU/sim_ano_mudancas.tsv`). Fontes: historiadeboca (campanhas 1919-2025), transfermarkt 2018/19, ESPN. Se mexer no
   rsssf_sul.py, reimportar e comparar as 7 competições (regra do COMECE-AQUI).
6. `comum-sulamerica/rsssf_sul.py`, `ler()`: data no título da fase/rodada e linha "[data, estádio]": **AR-023** (e UY-014 no Uruguai).
   Datas certas do historiadeboca para os jogos do Boca (1920, 1926, 1929) e da ESPN (2003/04 Clausura, 2006/07 desempate).
7. `outras_fontes.py` (casar a ESPN pelo par de clubes, data da ESPN prevalece): **QU-003** (jogos adiados com a data da rodada, 2003-2025,
   entre eles o Boca 2-0 River de 09/11/2025). AR-024 (2005-09-31 pela ESPN; 2021-02-29 sai com o AR-022). QU-005 (datas do Boca de 1945,
   1954, 1977: trocar só com terceira fonte).

### 3. Jogos, fases e artilheiros (médio; custo baixo)
8. `edicoes.py` (trechos) e `ler_rsssf.py` (FASES): AR-026 (1929 até a linha 586; 1970 Nacional até 920; relegation tournament de 1979
   como 'Grupo do rebaixamento'; 'Third Position' -> 'Disputa do 3º lugar'), AR-025 ('Desempate do 1º turno' em 1937 e 1939; 1923
   Asociación; 1931 Asociación; 1979 Metropolitano).
9. `edicoes.py`/`explicacoes.EXTRAS`: AR-018 (4 jogos de 2016/17 que só a ESPN tem: ids 462770, 462744, 462710, 462684), AR-014 (River 1-3
   Rosario Central, 31/08/1997: CONSERTA_TEXTO arg98:61), AR-007 (jogos do Boca de 1926 do historiadeboca).
10. `explicacoes.CONSERTA_TEXTO`: AR-019 (1975 Metropolitano: Estudiantes x River e Banfield x Huracán, conferir com a es).
11. `importar.artilheiros_rsssf()` + ARTILHEIROS_CORRIGE: AR-027 (1894 Gifford 7), AR-028 (1934 Asociación Maseda e Tarasconi 16), AR-029
    (2025 Apertura Molina 10; 1932 Asociación Irurieta 23; 1997/98 Clausura Sosa 16), AR-030 (1936 e 1988/89).
12. `conferir.soma()`/`importar.classificacao()`: AR-017 (1988/89 com 3/2/1 pontos; os pênaltis já estão no banco).

### 4. Clubes e rebaixados (baixo)
13. `clubes_arg.py`: AR-031 (Atlético Cipolletti = Cipolletti), AR-034 (nomes colados de 1926: CONSERTA_TEXTO na arg26 e tirar a REGRA
    'estudiantes batigre'). Decisões: AR-032 (Quilmes 1893-1895), AR-033 (fusões de 1934).
14. `importar.situacao()`: AR-021 (lista de rebaixados por temporada; BDFA 'Descensos' de 2012/13 em diante, es).
15. Decisões sem código até a resposta: AR-043 (Apertura 2026), AR-044 (1891), Copa de Oro 1936.

## coleta-sulamerica: Uruguaio (`coleta/uru-1/`)

### 1. Classificação e pódio (altos, NO AR; custo baixo)
1. `importar.py`, `classificacao()` e `situacao()`: **UY-006 [NO AR]** (tabela anual em vez do Apertura, 28 edições), **UY-004 [NO AR]**
   (vice = perdedor da final ou 2º da anual), UY-005 (3º), UY-003 (1948 sem vice). Fonte: tabela anual oficial da AUF 2013/14-2025
   (`url.php?id=ajaxapp&tabla_anual=1&id1=3&id2=<id>`), RSSSF 'Tabla Anual' 1994-2012/13.
2. `edicoes.py`: **UY-001 [NO AR]** (decisão: recomendado seguir a AUF, edições sem campeão).

### 2. Jogos e datas (médio; custo baixo a médio)
3. `edicoes.py`, `FIM_PADRAO` + 'Supercopa': UY-013 (8 jogos, lista com a data oficial na sugestão).
4. `comum-sulamerica/rsssf_sul.py`, `_linha_de_data()`/`ler()`: UY-014 (datas das decisões; lista oficial da AUF 2013/14-2025 e ESPN
   2007/08-2008/09) — o mesmo conserto do AR-023.
5. `edicoes.py`/`rsssf_sul.fixa_data`: UY-015 (2020 com o ano +1, 179 jogos).
6. `explicacoes.CONSERTA_TEXTO`: QU-006 (2005/06, rodadas 13 e 14 em abril em vez de maio, uru06:838/855/860); UY-023 (nome com
   autores, final de 1996).
7. `wikipedia_jogos.py`/`explicacoes.CORRIGE`: UY-010 (1908, W.O. para o Bristol).
8. `importar.classificacao()`: UY-011 (1951: usar a tabela publicada; nenhum jogo único explica a diferença).

### 3. Artilheiros (médio/baixo)
9. `importar.artilheiros_rsssf()` + ARTILHEIROS_AUF: UY-017 (12 edições, lista oficial da AUF), QU-008 (2017 e 2023: AUF x es), UY-018
   (1900-1931 pela es), UY-019 (grafias).

### 4. Decisões e o que fica
10. Decisões: UY-020 (Atlético Wanderers da FUF), UY-007 (vice de 1954), UY-008 (vice de 1947), parte do UY-004 (vice sem final).
11. Sem correção (registrar em EXPLICACOES): UY-012 (tabelas sem jogos, RSSSF x es), UY-016 (a AUF confirma o banco em 2013/14-2015/16;
    1933-1959 sem terceira fonte), QU-007 (pênaltis da AUF, não é erro).

## banco-painel
1. `painel/index.html` e `gerar_dashboard_v2.py`: UY-025 (textos de Jogos e vitórias e Gols, parcial), AR-041 (torneio no selo e nome
   da época no seletor), UY-027 (eixo da Corrida dos títulos).
2. `baixar_escudos.py` e `painel/escudos/`: UY-021 (Deportivo Colonia e Independencia), UY-022 (escudos da AUF para os clubes atuais, ex.
   River Plate de Montevideo), AR-035 (escudos do BDFA, /imagenes/<clube>_p.gif, para os 114 clubes argentinos sem escudo).

## Fontes novas a usar (detalhe em SCRATCH/fontes_QU.md)
- historiadeboca.com.ar: datas das rodadas 1913-1966 (AR-022, AR-023), jogos do Boca que faltam (AR-007), árbitro e escalações (jogo a jogo).
- AUF (auf.org.uy, histórico de temporadas): tabela anual, decisões, Supercopa e artilharia oficial de 2013/14 a 2025 (UY-004 a UY-017).
- transfermarkt: árbitro, público e autores (jogo a jogo), terceira opinião de datas nos anos 2000-2020.
- ESPN já baixada: datas dos jogos adiados (QU-003), jogos de 2016/17 (AR-018).
- BDFA: escudos argentinos (AR-035) e descensos 2012/13-2021 (AR-021).
