# Campeonato Ganês (`gha-1`) — documentação

Gerado por `python coleta/comum-africa/documentar.py` a partir do pacote `data/coleta/gha-1/pacote/`, do código `coleta/gha-1/` e do relatório `docs/coleta/gha-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 65, de 1958 a 2025/26; 39 sem jogos.
- **Jogos:** 6069 (6038 com placar); **gols:** 12631; **gols com autor:** 294 (2%); **cartões:** 0.
- **Clubes:** 137; **artilheiros:** 0 edições com artilheiro (0 linhas, com empates).
- **Classificação final:** 65 edições; **tabelas publicadas guardadas para conferência:** 1069 linhas.
- **No banco:** sim; **último commit do pacote:** cd02564c.
- **Observação da competição:** 1ª divisão ganesa (hoje Ghana Premier League) de 1958 a 2025/26, como a lista de campeões da RSSSF, sem o campeonato não oficial de 1956 e sem a competição especial de 2019 (não foi liga). 2018 e 2019/20 abandonados, sem campeão. Pontos 2-1-0 (vitória, empate, derrota) até 1993/94 (fora 1989/90) e 3-1-0 desde 1994/95.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão ganesa (gha-1): a liga nacional, de 1958 a 2025/26 (hoje Ghana Premier League).

Escopo (pesquisa de 24/11/2026, aprovada pelo Guilherme; registrada em coleta/comum-africa/COMECE-AQUI.md): como a lista
de campeões da RSSSF (ghachamp.html), sem o campeonato não oficial de 1956 (a RSSSF não conta) e sem a "competição
especial" do Comitê de Normalização de 2019 (não foi liga; a imprensa não a conta: o título de 2021/22 foi o "25º" do
Asante Kotoko). 2018 e 2019/20 foram abandonados e entram sem campeão.

Temporadas como na lista da RSSSF (o rótulo muda: ano civil, duas temporadas, de novo ano civil). "2004/05" é a página
gha04 (temporada de 2004, decidida num jogo em abril de 2005) e "2005" é a gha05 ("Ghana 2005/06").

Fontes dos jogos por edição:
- hist: a tabela final vem da lista de tabelas finais da RSSSF (ghahist.html, 1958 a 2000), seção da temporada.
- trechos: [(página da RSSSF, linha inicial, linha final)]; linha inicial 0: logo depois do cabeçalho; linha final None:
  a primeira copa ou outra divisão (FIM_PADRAO).
- tabelas: anos em que a página só tem a tabela.
- ogol: o calendário do ogol (liga-ganesa), quando a RSSSF não tem os jogos (`ogol` = id da edição no ogol).
Pontos: como as tabelas da RSSSF contam (Edicao.pontos).
```

**Edições:** 65, de 1958 a 2025/26, como a lista de campeões da RSSSF (`ghachamp.html`), sem o campeonato não oficial de 1956 e sem a competição especial do Comitê de Normalização de 2019 (não foi liga; a imprensa não a conta: o título de 2021/22 foi o "25º" do Asante Kotoko). Pesquisa de 24/11/2026, aprovada pelo Guilherme. 2018 e 2019/20 foram abandonados e entram sem campeão.

**Fontes:** RSSSF (lista de tabelas finais `ghahist.html`, de 1958 a 1987; páginas por ano: a tabela de 1989/90 a 1996/97 e os jogos de 1997/98 em diante, parte da temporada em 1997/98 e 2006/07); ogol (jogos de 2008/09 a 2010/11 e de 2015 em diante: base de 2010/11, conferência, rodada e data nos outros); Wikipédia em inglês (tabela das temporadas que têm artigo). A ESPN não tem a liga.

**Clubes:** o nome pelo qual o clube é conhecido (Asante Kotoko, Hearts of Oak, Ashanti Gold...). Mesmo clube com outro nome é um só (Goldfields = Ashanti Gold; Mysterious Dwarfs = Ebusua Dwarfs; RTU = Real Tamale United). Regras em `coleta/gha-1/clubes_gha.py`.

**Regras:** o placar é o da RSSSF (ou do ogol em 2010/11). A classificação é a tabela publicada (ordem oficial e pontos). Pontos 2-1-0 (vitória, empate, derrota) até 1993/94 (fora 1989/90, com 3 por vitória) e 3-1-0 desde 1994/95.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 20.
- **Edições com alguma tabela divergente** (4; motivo no relatório, na edição): 1999, 2000, 2010/11, 2015.
- **Edições sem tabela para conferir** (41): 1958, 1959/60, 1960/61, 1961/62, 1962/63, 1963/64, 1964/65, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988/89, 1989/90, 1990/91, 1991/92, 1992/93, 1993/94, 1994/95, 1995/96, 1996/97, 1997/98, 2006/07, 2011/12.
- **Edições com menos jogos que o esperado:** nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1950s | 2 | 0 | — | — | — | — | — | — | — | — |
| 1960s | 9 | 0 | — | — | — | — | — | — | — | — |
| 1970s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1980s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1990s | 9 | 391 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 10 | 2136 | 100% | 0% | 100% | 0% | 0% | 0% | 7% | 0.0 |
| 2010s | 9 | 1699 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2020s | 6 | 1843 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na África: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1958 a 1960/61: 8 clubes
- 1961/62: 15 clubes
- 1962/63 a 1963/64: 18 clubes
- 1964/65: 20 clubes
- 1966: 11 clubes
- 1967: 20 clubes
- 1968: 19 clubes
- 1969: 36 clubes
- 1970: 50 clubes
- 1971: 20 clubes
- 1972: 12 clubes
- 1973 a 1974: 14 clubes
- 1975: 18 clubes
- 1976 a 1977: 16 clubes
- 1978 a 1980: 18 clubes
- 1981 a 1985: 12 clubes
- 1986 a 1987: 14 clubes
- 1988/89: 1 clubes
- 1989/90: 11 clubes
- 1990/91: 16 clubes
- 1991/92: 14 clubes
- 1992/93 a 1994/95: 12 clubes
- 1995/96 a 1997/98: 14 clubes
- 1999 a 2018: 16 clubes
- 2019/20 a 2025/26: 18 clubes

**Pontos por vitória:**

- 1958 a 1988/89: 2
- 1989/90: 3
- 1990/91 a 1993/94: 2
- 1994/95 a 2025/26: 3

**Nome oficial:**

- 1958 a 2025/26: Ghana Premier League

**Formato** (fases na ordem, do edicoes.csv):

- 1958 a 1987: sem jogos (só a tabela final)
- 1988/89: sem jogos (só o campeão)
- 1989/90: sem jogos (só a classificação incompleta)
- 1990/91 a 1996/97: sem jogos (só a tabela final)
- 1997/98: jogos incompletos (só os resultados que a página traz)
- 1999 a 2003: pontos corridos
- 2004/05: 2 grupos + jogos de classificação + desempate + mata-mata
- 2005: pontos corridos
- 2006/07: jogos incompletos (só os resultados que a página traz)
- 2007/08 a 2010/11: pontos corridos
- 2011/12: sem jogos (só a tabela final)
- 2012/13 a 2017: pontos corridos
- 2018 a 2019/20: temporada não terminada
- 2020/21 a 2025/26: pontos corridos

**Fases e grupos de cada edição com mais de uma fase:**

- 2004/05: Primeira fase (grupos, 2 grupos); Jogos de classificação (liga); Desempate do rebaixamento (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 64 edições
- lista de campeões da RSSSF: 1 edições

**Observações das edições:**

- 1958: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1959/60: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1960/61: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1961/62: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1962/63: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1963/64: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1964/65: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1966: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1967: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1968: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1969: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1970: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1971: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1972: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1973: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1974: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1975: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1976: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1977: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1978: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1979: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1980: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1981: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1982: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1983: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1984: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1985: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1986: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1987: a RSSSF só traz a tabela final (lista de tabelas finais)
- 1988/89: a RSSSF só traz o campeão ("Final table missing")
- 1989/90: a RSSSF só traz a classificação incompleta (posição, jogos e pontos)
- 1990/91: a RSSSF só traz a tabela final
- 1991/92: a RSSSF só traz a tabela final
- 1992/93: a RSSSF só traz a tabela final
- 1993/94: a RSSSF só traz a tabela final
- 1994/95: a RSSSF só traz a tabela final
- 1995/96: a RSSSF só traz a tabela final
- 1996/97: a RSSSF só traz a tabela final
- 2010/11: os jogos vêm do calendário do ogol (a RSSSF só traz parte deles)
- 2011/12: a RSSSF só traz a tabela final
- 2018: temporada abandonada pelo escândalo de corrupção na federação ganesa ("competition abandoned following corruption scandal within GFA"); a tabela é a do abandono
- 2019/20: temporada abandonada pela Covid-19, sem campeão; a tabela é a do abandono

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Asante Kotoko: 25
- Hearts of Oak: 20
- Ashanti Gold: 4
- Great Olympics: 2
- Aduana Stars: 2
- Medeama: 2
- Eleven Wise: 1
- Real Republicans: 1
- Ebusua Dwarfs: 1
- Hasaacas: 1
- Berekum Chelsea: 1
- Wa All Stars: 1
- Samartex: 1
- Bibiani Gold Stars: 1
- Sem campeão: 2018, 2019/20

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1958 | Hearts of Oak | Cornerstones |
| 1959/60 | Asante Kotoko | Cornerstones |
| 1960/61 | Eleven Wise | Asante Kotoko |
| 1961/62 | Hearts of Oak | Asante Kotoko |
| 1962/63 | Real Republicans | Asante Kotoko |
| 1963/64 | Asante Kotoko | Hearts of Oak |
| 1964/65 | Asante Kotoko | Hearts of Oak |
| 1966 | Ebusua Dwarfs | Brong Ahafo United |
| 1967 | Asante Kotoko | Great Olympics |
| 1968 | Asante Kotoko | Hearts of Oak |
| 1969 | Asante Kotoko | Tano Bofoakwa |
| 1970 | Great Olympics | Hearts of Oak |
| 1971 | Hearts of Oak | Brong Ahafo United |
| 1972 | Asante Kotoko | Tano Bofoakwa |
| 1973 | Hearts of Oak | Cornerstones |
| 1974 | Great Olympics | Hearts of Oak |
| 1975 | Asante Kotoko | Eleven Wise |
| 1976 | Hearts of Oak | Asante Kotoko |
| 1977 | Hasaacas | Great Olympics |
| 1978 | Hearts of Oak | Hasaacas |
| 1979 | Hearts of Oak | Asante Kotoko |
| 1980 | Asante Kotoko | Hasaacas |
| 1981 | Asante Kotoko | Hearts of Oak |
| 1982 | Asante Kotoko | Great Olympics |
| 1983 | Asante Kotoko | Hasaacas |
| 1984 | Hearts of Oak | Eleven Wise |
| 1985 | Hearts of Oak | Asante Kotoko |
| 1986 | Asante Kotoko | Cornerstones |
| 1987 | Asante Kotoko | Great Olympics |
| 1988/89 | Asante Kotoko | — |
| 1989/90 | Hearts of Oak | Asante Kotoko |
| 1990/91 | Asante Kotoko | Hearts of Oak |
| 1991/92 | Asante Kotoko | Hearts of Oak |
| 1992/93 | Asante Kotoko | Ashanti Gold |
| 1993/94 | Ashanti Gold | Asante Kotoko |
| 1994/95 | Ashanti Gold | Real Tamale United |
| 1995/96 | Ashanti Gold | Asante Kotoko |
| 1996/97 | Hearts of Oak | Ashanti Gold |
| 1997/98 | Hearts of Oak | Asante Kotoko |
| 1999 | Hearts of Oak | Ebusua Dwarfs |
| 2000 | Hearts of Oak | Ashanti Gold |
| 2001 | Hearts of Oak | Asante Kotoko |
| 2002 | Hearts of Oak | Asante Kotoko |
| 2003 | Asante Kotoko | Hearts of Oak |
| 2004/05 | Hearts of Oak | Asante Kotoko |
| 2005 | Asante Kotoko | Hearts of Oak |
| 2006/07 | Hearts of Oak | Ashanti Gold |
| 2007/08 | Asante Kotoko | Heart of Lions |
| 2008/09 | Hearts of Oak | Asante Kotoko |
| 2009/10 | Aduana Stars | Ashanti Gold |
| 2010/11 | Berekum Chelsea | Ashanti Gold |
| 2011/12 | Asante Kotoko | Ashanti Gold |
| 2012/13 | Asante Kotoko | Berekum Chelsea |
| 2013/14 | Asante Kotoko | Heart of Lions |
| 2015 | Ashanti Gold | Aduana Stars |
| 2016 | Wa All Stars | Aduana Stars |
| 2017 | Aduana Stars | WAFA |
| 2018 | — | — |
| 2019/20 | — | — |
| 2020/21 | Hearts of Oak | Asante Kotoko |
| 2021/22 | Asante Kotoko | Medeama |
| 2022/23 | Medeama | Aduana Stars |
| 2023/24 | Samartex | Accra Lions |
| 2024/25 | Bibiani Gold Stars | Heart of Lions |
| 2025/26 | Medeama | Bibiani Gold Stars |

**Rebaixados marcados na classificação:** 136 em 50 edições (só onde a tabela publicada marca a queda); quem mais caiu: Ebusua Dwarfs (6), Brong Ahafo United (6), Great Olympics (6), Swedru All Blacks (5), Hasaacas (5).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1958: Eleven Wise -1
- 1961/62: Asante Kotoko +1
- 1961/62: Venomous Vipers -1
- 1970: Gold Stars -9
- 1975: Swedru All Blacks -1
- 1978: Hasaacas +1
- 1982: Eleven Wise +1
- 1985: Hearts of Oak +5
- 1985: Asante Kotoko +2
- 1985: Eleven Wise +4
- 1985: Great Olympics +4
- 1985: Okwahu United +1
- 1985: Cornerstones +2
- 1985: Arnold Warriors +1
- 1985: Boye Sowahs Zebi +2
- 1985: Hasaacas +3
- 1985: Tano Bofoakwa +1
- 1992/93: Dawu Youngstars +1
- 1995/96: Real Tamale United -6
- 1999: Asante Kotoko -3
- 1999: Swedru All Blacks -3
- 2000: Hearts of Oak -3
- 2000: Asante Kotoko -3
- 2000: Great Olympics -3
- 2001: Asante Kotoko -3
- 2001: King Faisal Babes -3
- 2001: Real Tamale United -9
- 2003: Brong Ahafo United -3
- 2003: Ashanti Gold -12
- 2003: Prestea Mine Stars -6
- 2003: Stay Cool -3
- 2005: Real Tamale United -3
- 2006/07: Berekum Arsenal -3
- 2006/07: King Faisal Babes -3
- 2006/07: Tano Bofoakwa -3
- 2006/07: Power FC -3
- 2007/08: Real Tamale United -3
- 2009/10: Kessben -3
- 2010/11: B.A. Stars -3
- 2012/13: Real Tamale United -3
- 2015: Asante Kotoko -3
- 2016: New Edubiase United -3
- 2019/20: Medeama -3
- 2020/21: Ebusua Dwarfs -3
- 2024/25: Nations FC -3
- 2024/25: Bechem United -3

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/gha-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 8)

- **ghahist · 279:** «27  11  7 10» → «27  11  7  9»: Venomous Vipers: 11+7+10 não dá 27 jogos; 29 pontos = 11 vitórias e 7 empates, logo 9 derrotas
- **ghahist · 493:** «38  17  5 15» → «38  17  5 16»: Bofoakwa: 17+5+15 não dá 38 jogos; 39 pontos = 17 vitórias e 5 empates, logo 16 derrotas
- **ghahist · 516:** «21   8  5  9» → «21   8  5  8»: Great Olympics: 8+5+9 não dá 21 jogos; 21 pontos = 8 vitórias e 5 empates, logo 8 derrotas
- **ghahist · 588:** «34   5  9 17» → «34   8  9 17»: Susu Biribi: 5+9+17 não dá 34 jogos; 25 pontos e 9 empates dão 8 vitórias
- **ghahist · 634:** «15   2  5  7» → «15   2  5  8»: Brong Ahafo United: 2+5+7 não dá 15 jogos; 9 pontos = 2 vitórias e 5 empates, logo 8 derrotas
- **ghahist · 717:** «22  15  2  2» → «22  15  5  2»: Asante Kotoko: 15+2+2 não dá 22 jogos; 35 pontos e 15 vitórias dão 5 empates
- **gha09 · 54:** «30 10 10 13» → «30 10  7 13»: AshantiGold: 10+10+13 não dá 30 jogos; 37 pontos e 10 vitórias dão 7 empates
- **gha09 · 418:** «30 10 10 13» → «30 10  7 13»: AshantiGold (a tabela repetida no fim da página): o mesmo erro

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 18)

- **2003 · gha03:41:** [descartado] linha da nota sobre os resultados dados (não é jogo)
- **2003 · gha03:42:** [descartado] linha da nota sobre os resultados dados (não é jogo)
- **2003 · gha03:43:** [descartado] linha da nota sobre os resultados dados (não é jogo)
- **2003 · gha03:44:** [descartado] linha da nota sobre os resultados dados (não é jogo)
- **2003 · gha03:45:** [descartado] linha da nota sobre os resultados dados (não é jogo)
- **2003 · gha03:436:** [descartado] linha da nota sobre os resultados dados (não é jogo)
- **2003 · gha03:437:** [descartado] linha da nota sobre os resultados dados (não é jogo)
- **2003 · gha03:438:** [descartado] linha da nota sobre os resultados dados (não é jogo)
- **2003 · gha03:439:** [descartado] linha da nota sobre os resultados dados (não é jogo)
- **2003 · gha03:440:** [descartado] linha da nota sobre os resultados dados (não é jogo)
- **2003 · gha03:69:** [oficial = (0, 3), nota = 0-3 dado (1-0 em campo)] resultado dado que a tabela conta (nota da página: "counted as awarded")
- **2003 · gha03:91:** [oficial = (0, 3), nota = 0-3 dado (1-0; revogado? em campo)] resultado dado que a tabela conta (nota da página: "counted as awarded")
- **2003 · gha03:103:** [oficial = (0, 3), nota = 0-3 dado (1-0 em campo)] resultado dado que a tabela conta (nota da página: "counted as awarded")
- **2003 · gha03:123:** [oficial = (3, 0), nota = 3-0 dado (1-1 em campo)] resultado dado que a tabela conta (nota da página: "counted as awarded")
- **2003 · gha03:144:** [oficial = (0, 3), nota = 0-3 dado (4-0 em campo)] resultado dado que a tabela conta (nota da página: "counted as awarded")
- **2003 · gha03:199:** [oficial = (0, 3), nota = 0-3 dado (3-1 em campo)] resultado dado que a tabela conta (nota da página: "counted as awarded")
- **2003 · gha03:282:** [oficial = (3, 0), nota = 3-0 dado (1-1 em campo)] resultado dado que a tabela conta (nota da página: "counted as awarded")
- **2003 · gha03:308:** [oficial = (0, 3), nota = 0-3 dado (1-1 em campo)] resultado dado que a tabela conta (nota da página: "counted as awarded")

### Jogos acrescentados à mão (a página traz em texto corrido) (`EXTRAS`, 1)

- **2009/10:** Asante Kotoko 2-0 New Edubiase United (, ogol:1353495) jogo que falta na página da RSSSF (vem do ogol; a tabela da RSSSF só fecha com ele)

### Divergências entre fontes já explicadas (`EXPLICACOES`, 7)

- **1999:** a lista de jogos da página não fecha com a tabela em dois clubes (sem terceira fonte); nenhum placar foi mudado e o relatório aponta o jogo provável
- **2000:** a lista de jogos da página não fecha com a tabela em dois clubes (sem terceira fonte); nenhum placar foi mudado e o relatório aponta o jogo provável
- **2003:** a tabela conta oito resultados dados (nota da página) e um desconto de 3 pontos de quem perdeu cada decisão; os jogos ficam com o placar dado e o de campo na observação
- **2004/05:** dois grupos, jogo do título (Hearts of Oak 1-0 Asante Kotoko, abril de 2005), 3º lugar e desempate do rebaixamento
- **2009/10:** o returno Asante Kotoko x New Edubiase vem do ogol (falta na página da RSSSF)
- **2010/11:** os jogos vêm do ogol e não fecham com a tabela da RSSSF em sete clubes; nenhum placar foi mudado e a classificação é a tabela publicada
- **2015:** Asante Kotoko com 3 gols a mais nos jogos que na tabela (provável punição de gols, como as da Nigéria); nenhum placar mudado

### Identidade dos clubes

Regras em `coleta/gha-1/clubes_gha.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes ganeses: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido ("Asante Kotoko", "Hearts of Oak", "Ashanti Gold");
- nome que já existe em outro país leva o país ("Mighty Jets (Gana)", "Highlanders (Gana)", "Aston Villa (Gana)"); os de
  Berekum levam a cidade, como são conhecidos ("Berekum Arsenal", "Berekum Chelsea");
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - Ashanti Gold = Goldfields = AshantiGold (a RSSSF conta os títulos juntos); Ebusua Dwarfs = Mysterious Dwarfs;
    Real Tamale United = RTU; Swedru All Blacks = All Blacks = Gamba All Blacks; Tano Bofoakwa = Bofoakwa; Brong Ahafo
    United = BA United; King Faisal Babes = King Faisal; Wa All Stars = All Stars (2007-2011); Inter Allies =
    International Allies; WAFA = West Africa Football Academy; Eleven Wonders = Techiman Eleven Wonders.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
```

## 8. O que não deu para coletar

- **Fora do pacote:** a FA Cup e as outras copas, as ligas regionais da era colonial, a 2ª divisão e os jogos de acesso.
- **Edições sem jogos** (39): 1958, 1959/60, 1960/61, 1961/62, 1962/63, 1963/64, 1964/65, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988/89, 1989/90, 1990/91, 1991/92, 1992/93, 1993/94, 1994/95, 1995/96, 1996/97, 2011/12.
- **Décadas com menos da metade dos gols com autor:** 1990s, 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 1958 a 1996/97: só a tabela final (lista de tabelas finais até 1987; página do ano de 1989/90 a 1996/97); 1988/89 só o campeão ("Final table missing"); 1989/90 só posição, jogos e pontos. 1997/98 e 2006/07: parte dos jogos; 2011/12: só a tabela. O ogol só tem jogos de 2008/09 a 2010/11 e de 2015 em diante. Fonte que resolveria: jornais ganeses (Daily Graphic) ou o arquivo da GFA.
- 2010/11: os jogos do ogol não fecham com a tabela da RSSSF em sete clubes; nenhum placar mudado.
- Rebaixamento marcado onde a tabela ou a nota diz; em vários anos dos 1960 e 1970 a lista não diz.
- Autores dos gols quase nenhum; artilheiros e cartões, nenhum.
- Identidade a conferir: Ashanti Gold = Goldfields; Ebusua Dwarfs = Mysterious Dwarfs; Swedru All Blacks = Gamba All Blacks; Wa All Stars = All Stars (2007-2011); Holy Stars de Techiman (1986) x Basake Holy Stars (2024/25).

## 10. Arquivos e comandos

Código em `coleta/gha-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_ogol.py` | Baixa o calendário de cada edição da 1ª divisão ganesa no ogol para data/coleta/gha-1/ogol/<id>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão ganesa para data/coleta/gha-1/rsssf/: a lista de campeões (ghachamp.html) e |
| `baixar_wikipedia.py` | Baixa da Wikipédia em inglês (wikitexto, pela API) o artigo da liga ("Ghana Premier League") e o de cada temporada |
| `clubes_gha.py` | Identidade dos clubes ganeses: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão ganesa (gha-1): a liga nacional, de 1958 a 2025/26 (hoje Ghana Premier League). |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão ganesa, edição a edição (entram no relatório). |
| `importar.py` | Junta as fontes da 1ª divisão ganesa e grava o pacote em data/coleta/gha-1/pacote/ e o relatório em docs/coleta/gha-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/gha-1/rsssf/) com o leitor comum (rsssf_africa), |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol (copiado de coleta/chi-1/outras_fontes.py, sem a ESPN, que não tem a liga egípcia). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |
| `wiki_tabelas.py` | Tabelas finais dos artigos de temporada da Wikipédia em inglês (data/coleta/gha-1/wikipedia/en_<temporada>.txt). A lista de campeões e a de artilheiros ficam vazias: o artigo da |

- Fontes baixadas: `data/coleta/gha-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-africa/`, do ogol em `data/cache/ogol-gha-1/`.
- Pacote: `data/coleta/gha-1/pacote/`; relatório: `docs/coleta/gha-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/gha-1/baixar_ogol.py
python coleta/gha-1/baixar_rsssf.py
python coleta/gha-1/baixar_wikipedia.py
python coleta/gha-1/importar.py
python coleta/gha-1/conferir.py [-v temporada]   # divergências
python coleta/comum-africa/testar_carga.py gha-1 <scratchpad>
python coleta/comum-africa/documentar.py
```

