# Campeonato Argelino (`alg-1`) — documentação

Gerado por `python coleta/comum-africa/documentar.py` a partir do pacote `data/coleta/alg-1/pacote/`, do código `coleta/alg-1/` e do relatório `docs/coleta/alg-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 64, de 1962/63 a 2025/26; 0 sem jogos.
- **Jogos:** 15210 (15196 com placar); **gols:** 33855; **gols com autor:** 3829 (11%); **cartões:** 0.
- **Clubes:** 81; **artilheiros:** 58 edições com artilheiro (65 linhas, com empates).
- **Classificação final:** 64 edições; **tabelas publicadas guardadas para conferência:** 1033 linhas.
- **No banco:** sim; **último commit do pacote:** b09bbaa5.
- **Observação da competição:** 1ª divisão argelina (hoje Ligue Professionnelle 1) desde a independência, de 1962/63 a 2025/26. 1962/63 e 1963/64: ligas regionais e fase final. 2019/20 parado pela Covid-19, com o campeão declarado pela federação. Pontos 3-2-1 (vitória, empate, derrota) até 1985/86, 2-1-0 de 1986/87 a 1994/95 e 3-1-0 desde 1995/96.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão argelina (alg-1): o campeonato nacional, de 1962/63 a 2025/26.

Lista de campeões: RSSSF (algchamp.html), conferida com a Wikipédia em inglês ("List of Algerian football champions").
Escopo (pesquisa de 24/11/2026, aprovada pelo Guilherme; registrada em coleta/comum-africa/COMECE-AQUI.md): só desde a
independência, como a RSSSF ("64 títulos; desde a independência"), a Wikipédia e a contagem dos clubes. A era colonial
(ligas regionais de Argel, Orã e Constantine; "campeonato da Argélia" de 1957/58 a 1960/61) fica de fora, como as copas e
a 2ª divisão.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)]; página algAA (ou algAAAA desde 2009/10): a do ano em que a
  temporada termina (alg63 = 1962/63; alg00 = 1999/00; alg2010 = 2009/10). Linha inicial 0: a 1ª divisão é a primeira
  seção depois do índice do topo; linha final None: vai até a seção seguinte do índice (ler_rsssf.secao()).
- ogol: o calendário do ogol, quando a RSSSF não tem os jogos.
Pontos: 3-2-1 (vitória, empate, derrota) até 1985/86, 2-1-0 de 1986/87 a 1994/95 e 3-1-0 desde 1995/96, como as
tabelas da RSSSF contam ("NB: 3-2-1 points system").
```

**Edições:** 64, uma por temporada, de 1962/63 a 2025/26, como na lista de campeões da RSSSF (`algchamp.html`, "64 títulos; desde a independência") e na Wikipédia em inglês. A era colonial fica de fora (pesquisa de 24/11/2026, aprovada pelo Guilherme): não havia campeonato único (ligas regionais de Argel, Orã e Constantine) e ninguém conta esses títulos. 1962/63 e 1963/64: ligas regionais e fase final (jogos incompletos). 2019/20: parado pela Covid-19; a federação declarou o CR Belouizdad campeão.

**Fontes:** RSSSF (páginas por temporada, `data/coleta/alg-1/rsssf/`: base dos jogos de todas as temporadas); ogol (1985/86 em diante, com os mesmos placares da RSSSF: conferência, rodada e data); Wikipédia em inglês (lista de campeões com vice e artilheiro e a tabela de cada temporada, terceira fonte nas divergências). A ESPN não tem a liga argelina.

**Clubes:** o nome pelo qual o clube é conhecido, com a sigla francesa (MC Alger, USM Alger, JS Kabylie...). Mesmo clube com outro nome é um só, com o nome atual: os nomes da reforma esportiva de 1977 a 1989 (MP Alger, JE Tizi Ouzou, EP Sétif, CM Belcourt...) e os mais antigos (JS Kawkabi, CR Belcourt). O USM Annaba dos anos 1960 e 1970 é o atual Hamra Annaba. Regras em `coleta/alg-1/clubes_alg.py`.

**Regras:** o placar é o da RSSSF. A classificação é a tabela publicada (ordem oficial e pontos); quando uma linha dela não fecha com os jogos e a tabela da Wikipédia confirma os jogos, a linha fica com os números dos jogos. Placar só muda com outra fonte (o ogol) que feche com as tabelas. Pontos como as tabelas contam: 3-2-1 (vitória, empate, derrota) até 1985/86, 2-1-0 de 1986/87 a 1994/95 e 3-1-0 desde 1995/96.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 22.
- **Edições com alguma tabela divergente** (39; motivo no relatório, na edição): 1964/65, 1965/66, 1966/67, 1967/68, 1968/69, 1969/70, 1970/71, 1971/72, 1972/73, 1973/74, 1974/75, 1975/76, 1976/77, 1977/78, 1978/79, 1979/80, 1980/81, 1981/82, 1982/83, 1983/84, 1984/85, 1985/86, 1986/87, 1987/88, 1988/89, 1989/90, 1990/91, 1991/92, 1992/93, 1993/94, 1994/95, 1995/96, 1996/97, 1997/98, 1998/99, 2000/01, 2001/02, 2009/10, 2020/21.
- **Edições sem tabela para conferir** (3): 1962/63, 1963/64, 2019/20.
- **Edições com menos jogos que o esperado:** 1974/75 (232 de 240), 1975/76 (232 de 240), 1979/80 (240 de 246), 1982/83 (239 de 240), 1985/86 (379 de 380), 1988/89 (238 de 240), 1990/91 (239 de 240).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1960s | 8 | 1482 | 99% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 10 | 2100 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 10 | 2858 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 10 | 2292 | 100% | 0% | 100% | 0% | 0% | 0% | 20% | 0.0 |
| 2000s | 10 | 2499 | 100% | 0% | 100% | 0% | 0% | 0% | 53% | 0.0 |
| 2010s | 10 | 2333 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2020s | 6 | 1646 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na África: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1962/63: 16 clubes
- 1963/64: 42 clubes
- 1964/65 a 1965/66: 16 clubes
- 1966/67 a 1970/71: 12 clubes
- 1971/72 a 1975/76: 16 clubes
- 1976/77: 15 clubes
- 1977/78 a 1978/79: 14 clubes
- 1979/80 a 1983/84: 16 clubes
- 1984/85: 21 clubes
- 1985/86 a 1986/87: 20 clubes
- 1987/88: 18 clubes
- 1988/89 a 1997/98: 16 clubes
- 1998/99: 28 clubes
- 1999/00: 12 clubes
- 2000/01: 16 clubes
- 2001/02: 17 clubes
- 2002/03 a 2007/08: 16 clubes
- 2008/09: 17 clubes
- 2009/10: 18 clubes
- 2010/11 a 2019/20: 16 clubes
- 2020/21: 20 clubes
- 2021/22: 18 clubes
- 2022/23 a 2025/26: 16 clubes

**Pontos por vitória:**

- 1962/63 a 1985/86: 3
- 1986/87 a 1994/95: 2
- 1995/96 a 2025/26: 3

**Nome oficial:**

- 1962/63 a 1963/64: Championnat d'Algérie (Critérium d'Honneur)
- 1964/65 a 1998/99: Championnat National de 1ère Division
- 1999/00 a 2001/02: Super Division
- 2002/03 a 2009/10: Championnat National de 1ère Division
- 2010/11 a 2025/26: Ligue Professionnelle 1

**Formato** (fases na ordem, do edicoes.csv):

- 1962/63: jogos incompletos (só a 2ª fase das ligas regionais e a fase final)
- 1963/64: jogos incompletos (resultados conhecidos das ligas regionais e a fase final)
- 1964/65 a 1996/97: pontos corridos
- 1997/98: 2 grupos + desempate + jogos de classificação + mata-mata
- 1998/99: 2 grupos + mata-mata
- 1999/00 a 2018/19: pontos corridos
- 2019/20: temporada interrompida (Covid-19)
- 2020/21 a 2025/26: pontos corridos

**Fases e grupos de cada edição com mais de uma fase:**

- 1962/63: Primeira fase (liga); Jogos de classificação (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1963/64: Primeira fase (liga); Desempate da Liga de Constantine (mata_mata, jogo_unico); Jogos de classificação (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1997/98: Primeira fase (grupos, 2 grupos); Desempate do rebaixamento (mata_mata, jogo_unico); Jogos de classificação (liga); Final (mata_mata, jogo_unico)
- 1998/99: Primeira fase (grupos, 2 grupos); Final (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 60 edições
- calculada: 4 edições

**Observações das edições:**

- 1962/63: a RSSSF não traz a 1ª fase das ligas regionais; a semifinal USM Alger 2-2 USM Annaba foi decidida pelos escanteios (7-6); pontos 3-2-1 (vitória, empate, derrota)
- 1963/64: pontos 3-2-1 (vitória, empate, derrota)
- 1964/65: pontos 3-2-1 (vitória, empate, derrota)
- 1965/66: pontos 3-2-1 (vitória, empate, derrota)
- 1966/67: pontos 3-2-1 (vitória, empate, derrota)
- 1967/68: pontos 3-2-1 (vitória, empate, derrota)
- 1968/69: pontos 3-2-1 (vitória, empate, derrota)
- 1969/70: pontos 3-2-1 (vitória, empate, derrota)
- 1970/71: pontos 3-2-1 (vitória, empate, derrota)
- 1971/72: pontos 3-2-1 (vitória, empate, derrota)
- 1972/73: pontos 3-2-1 (vitória, empate, derrota)
- 1973/74: pontos 3-2-1 (vitória, empate, derrota)
- 1974/75: pontos 3-2-1 (vitória, empate, derrota)
- 1975/76: pontos 3-2-1 (vitória, empate, derrota)
- 1976/77: pontos 3-2-1 (vitória, empate, derrota)
- 1977/78: pontos 3-2-1 (vitória, empate, derrota)
- 1978/79: pontos 3-2-1 (vitória, empate, derrota)
- 1979/80: pontos 3-2-1 (vitória, empate, derrota)
- 1980/81: pontos 3-2-1 (vitória, empate, derrota)
- 1981/82: pontos 3-2-1 (vitória, empate, derrota)
- 1982/83: pontos 3-2-1 (vitória, empate, derrota)
- 1983/84: pontos 3-2-1 (vitória, empate, derrota)
- 1984/85: pontos 3-2-1 (vitória, empate, derrota)
- 1985/86: pontos 3-2-1 (vitória, empate, derrota)
- 1997/98: ninguém caiu: a 1ª divisão de 1998/99 passou a dois grupos de 14 (os desempates de rebaixamento não valeram)
- 2019/20: parada em 15/03/2020 pela Covid-19; a federação declarou o CR Belouizdad campeão pela média de pontos por jogo, sem rebaixamento

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- JS Kabylie: 14
- CR Belouizdad: 10
- MC Alger: 10
- USM Alger: 8
- ES Sétif: 8
- MC Oran: 4
- CS Constantine: 2
- Hamra Annaba: 1
- NA Hussein Dey: 1
- RC Kouba: 1
- GC Mascara: 1
- MO Constantine: 1
- US Chaouia: 1
- USM El Harrach: 1
- ASO Chlef: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1962/63 | USM Alger | MC Alger |
| 1963/64 | Hamra Annaba | NA Hussein Dey |
| 1964/65 | CR Belouizdad | MSP Batna |
| 1965/66 | CR Belouizdad | ES Guelma |
| 1966/67 | NA Hussein Dey | RC Kouba |
| 1967/68 | ES Sétif | MC Oran |
| 1968/69 | CR Belouizdad | MC Oran |
| 1969/70 | CR Belouizdad | MC Alger |
| 1970/71 | MC Oran | CS Constantine |
| 1971/72 | MC Alger | CR Belouizdad |
| 1972/73 | JS Kabylie | NA Hussein Dey |
| 1973/74 | JS Kabylie | MO Constantine |
| 1974/75 | MC Alger | RC Kouba |
| 1975/76 | MC Alger | NA Hussein Dey |
| 1976/77 | JS Kabylie | CR Belouizdad |
| 1977/78 | MC Alger | JS Kabylie |
| 1978/79 | MC Alger | JS Kabylie |
| 1979/80 | JS Kabylie | CR Belouizdad |
| 1980/81 | RC Kouba | JS Kabylie |
| 1981/82 | JS Kabylie | NA Hussein Dey |
| 1982/83 | JS Kabylie | ES Sétif |
| 1983/84 | GC Mascara | USM El Harrach |
| 1984/85 | JS Kabylie | MC Oran |
| 1985/86 | JS Kabylie | ES Sétif |
| 1986/87 | ES Sétif | MC Oran |
| 1987/88 | MC Oran | JS Kabylie |
| 1988/89 | JS Kabylie | MC Alger |
| 1989/90 | JS Kabylie | MC Oran |
| 1990/91 | MO Constantine | ASM Oran |
| 1991/92 | MC Oran | USM El Harrach |
| 1992/93 | MC Oran | NA Hussein Dey |
| 1993/94 | US Chaouia | JS Bordj Ménaïel |
| 1994/95 | JS Kabylie | MC Oran |
| 1995/96 | USM Alger | MC Oran |
| 1996/97 | CS Constantine | MC Oran |
| 1997/98 | USM El Harrach | USM Alger |
| 1998/99 | MC Alger | JS Kabylie |
| 1999/00 | CR Belouizdad | MC Oran |
| 2000/01 | CR Belouizdad | USM Alger |
| 2001/02 | USM Alger | JS Kabylie |
| 2002/03 | USM Alger | USM Blida |
| 2003/04 | JS Kabylie | USM Alger |
| 2004/05 | USM Alger | JS Kabylie |
| 2005/06 | JS Kabylie | USM Alger |
| 2006/07 | ES Sétif | JS Kabylie |
| 2007/08 | JS Kabylie | ASO Chlef |
| 2008/09 | ES Sétif | JS Kabylie |
| 2009/10 | MC Alger | ES Sétif |
| 2010/11 | ASO Chlef | JSM Béjaïa |
| 2011/12 | ES Sétif | JSM Béjaïa |
| 2012/13 | ES Sétif | USM El Harrach |
| 2013/14 | USM Alger | JS Kabylie |
| 2014/15 | ES Sétif | MO Béjaïa |
| 2015/16 | USM Alger | JS Saoura |
| 2016/17 | ES Sétif | MC Alger |
| 2017/18 | CS Constantine | JS Saoura |
| 2018/19 | USM Alger | JS Kabylie |
| 2019/20 | CR Belouizdad | ES Sétif |
| 2020/21 | CR Belouizdad | ES Sétif |
| 2021/22 | CR Belouizdad | JS Kabylie |
| 2022/23 | CR Belouizdad | CS Constantine |
| 2023/24 | MC Alger | CR Belouizdad |
| 2024/25 | MC Alger | JS Kabylie |
| 2025/26 | MC Alger | JS Saoura |

**Rebaixados marcados na classificação:** 158 em 56 edições (só onde a tabela publicada marca a queda); quem mais caiu: ASM Oran (8), USM Bel-Abbès (7), USM Blida (6), WA Tlemcen (6), CS Constantine (6).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1962/63: MSP Batna -2
- 1963/64: JSM Tiaret -1
- 1963/64: SCM Oran -6
- 1963/64: US Biskra +2
- 1963/64: OM Saint-Eugène +1
- 1970/71: USM Bel-Abbès -2
- 1972/73: MC Oran -1
- 1979/80: GC Mascara -1
- 1981/82: CR Belouizdad -1
- 1981/82: ASO Chlef -1
- 1982/83: MC Oran -1
- 1982/83: NA Hussein Dey -2
- 1985/86: USM Aïn Beïda -1
- 1985/86: DNC Alger -2
- 1987/88: RC Relizane -1
- 1988/89: USM Annaba +1
- 1988/89: MO Constantine -1
- 1991/92: USM Bel-Abbès -1
- 1994/95: CS Constantine -1
- 1995/96: ASM Oran -2
- 1996/97: USM Aïn Beïda -3
- 1997/98: CS Constantine -2
- 2001/02: CR Belouizdad -1
- 2001/02: USM Blida -2
- 2001/02: MC Alger -1
- 2003/04: MC Oran -1
- 2004/05: US Chaouia -3
- 2005/06: USM Alger -3
- 2007/08: ES Sétif -1
- 2008/09: CA Bordj Bou Arréridj -1
- 2012/13: MC Alger -3
- 2016/17: RC Relizane -6
- 2016/17: MO Béjaïa -1
- 2017/18: USM Bel-Abbès -6
- 2018/19: CR Belouizdad -3
- 2020/21: RC Relizane -3
- 2020/21: AS Aïn M'lila -3

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/alg-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 3)

- **alg99 · 65:** «Teams 7-11» → «Teams 7 to 11»: nota sobre a temporada seguinte; "7-11" era lido como placar
- **alg99 · 909:** «Teams 7-11» → «Teams 7 to 11»: nota sobre a temporada seguinte; "7-11" era lido como placar
- **alg03 · 345:** «temporarily awarded 0-3» → «temporarily given to RC Kouba»: o 0-3 foi revogado depois ("later revoked"): vale o 1-0 de campo, como a tabela conta

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 28)

- **1972/73 · alg73:151:** [descartado] a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista
- **1972/73 · alg73:152:** [descartado] a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista
- **1972/73 · alg73:153:** [descartado] a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista
- **1972/73 · alg73:154:** [descartado] a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista
- **1972/73 · alg73:155:** [descartado] a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista
- **1972/73 · alg73:156:** [descartado] a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista
- **1972/73 · alg73:157:** [descartado] a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista
- **1972/73 · alg73:158:** [descartado] a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista
- **1974/75 · alg75:79:** [descartado] a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são conhecidos
- **1974/75 · alg75:80:** [descartado] a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são conhecidos
- **1974/75 · alg75:81:** [descartado] a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são conhecidos
- **1974/75 · alg75:82:** [descartado] a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são conhecidos
- **1974/75 · alg75:83:** [descartado] a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são conhecidos
- **1974/75 · alg75:84:** [descartado] a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são conhecidos
- **1974/75 · alg75:85:** [descartado] a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são conhecidos
- **1974/75 · alg75:86:** [descartado] a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são conhecidos
- **1975/76 · alg76:220:** [descartado] a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são conhecidos
- **1975/76 · alg76:221:** [descartado] a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são conhecidos
- **1975/76 · alg76:222:** [descartado] a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são conhecidos
- **1975/76 · alg76:223:** [descartado] a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são conhecidos
- **1975/76 · alg76:224:** [descartado] a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são conhecidos
- **1975/76 · alg76:225:** [descartado] a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são conhecidos
- **1975/76 · alg76:226:** [descartado] a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são conhecidos
- **1975/76 · alg76:227:** [descartado] a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são conhecidos
- **1969/70 · alg70:123:** [descartado] USM Bel-Abbès 0-0 NA Hussein Dey aparece duas vezes na rodada 10
- **1988/89 · alg89:204:** [descartado] MC Alger 2-1 MO Constantine aparece duas vezes na rodada 16
- **2025/26 · alg2026:93:** [gm = 0, gv = 1] Olympique Akbou 0-1 MC Alger (ogol; as tabelas da RSSSF e da Wikipédia só fecham assim); a lista da RSSSF dá 1-0
- **2025/26 · alg2026:310:** [gm = 2, gv = 0] CS Constantine 2-0 ES Sétif (ogol; as tabelas da RSSSF e da Wikipédia só fecham assim); a lista da RSSSF dá 1-0

### Divergências entre fontes já explicadas (`EXPLICACOES`, 47)

- **1964/65:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1965/66:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1966/67:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1967/68:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1968/69:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1969/70:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1970/71:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1971/72:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1972/73:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1972/73:** a rodada 10 aparece duas vezes na página: a cópia foi descartada
- **1973/74:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1974/75:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1974/75:** a rodada 4 da página é cópia da rodada 3: os oito jogos verdadeiros da rodada 4 faltam
- **1975/76:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1975/76:** a rodada 18 da página é cópia da rodada 17: os oito jogos verdadeiros da rodada 18 faltam
- **1976/77:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1977/78:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1978/79:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1979/80:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1980/81:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1981/82:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1982/83:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1983/84:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1984/85:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1985/86:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1986/87:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1987/88:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1988/89:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1989/90:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1990/91:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1991/92:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1992/93:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1993/94:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1994/95:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1995/96:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1996/97:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1996/97:** "US Constantine" (rodadas 15 e 22) é o US Chaouia (erro de digitação da página)
- **1997/98:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1997/98:** ninguém caiu: os desempates de rebaixamento não valeram, porque a 1ª divisão de 1998/99 passou a dois grupos de 14
- **1998/99:** a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório aponta o jogo provável
- **1962/63:** a 1ª fase das ligas regionais não está na página; a ordem dos quatro primeiros é a da fase final
- **1963/64:** ligas regionais só com os resultados conhecidos ("Known Results") e o grupo Leste da Liga de Constantine sem números; os jogos de acesso à 1ª divisão do ano seguinte ficam de fora; dois jogos com siglas que não deu para identificar ("R.S.O" e "C.S.S", da Liga de Orã) ficam de fora
- **2000/01:** USM Blida x CS Constantine: a página corrigiu o placar para 1-0 ("correction from 2-0"), mas a tabela ainda conta o 2-0; fica o 1-0 corrigido
- **2001/02:** a tabela da RSSSF (e a da Wikipédia) não fecha com os jogos em quatro clubes; nenhum placar foi mudado
- **2009/10:** CA Bordj Bou Arréridj x MC Alger (14/08/2009): abandonado aos 72' com 1-0 e "awarded loss to both" (derrota dada aos dois); a tabela da RSSSF conta derrota para os dois, a da Wikipédia a vitória do CA Bordj Bou Arréridj; o jogo fica sem placar e a classificação é a tabela publicada
- **2020/21:** a tabela da RSSSF, a da Wikipédia e os jogos não fecham entre si em três clubes; nenhum placar foi mudado
- **2025/26:** dois placares da lista da RSSSF corrigidos pelo ogol (as tabelas da RSSSF e da Wikipédia só fecham com eles)

### Identidade dos clubes

Regras em `coleta/alg-1/clubes_alg.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes argelinos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4) e do recado do agente 1:
- nome pelo qual o clube é conhecido, com a sigla francesa ("MC Alger", "USM Alger", "JS Kabylie", "ES Sétif");
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte. As tabelas da RSSSF
  trazem o nome atual e o da época entre colchetes ("[as Mouloudia Pétroliers d'Alger]"); os da reforma esportiva de
  1977 (nomes de empresas estatais) voltaram aos antigos por volta de 1989:
  - MC Alger = MP Alger; MC Oran = MP Oran; CR Belouizdad = CR Belcourt = CM Belcourt; JS Kabylie = JS Kawkabi = JE (JET)
    Tizi Ouzou; ES Sétif = EP Sétif; USM Alger = USK Alger; NA Hussein Dey = NAA Hussein Dey = MA Hussein Dey;
    RC Kouba = CCS (CSS) Kouba = RS Kouba; USM El Harrach = USM Maison-Carrée; CS Constantine = CM Constantine;
  - ASO Chlef = AS Orléansville (1962-64) = ASTO El Asnam = DNC Asnam = Chlef SO = CSO Chlef (a cidade mudou de nome);
  - RC Kouba é o "NAR Alger" (Naphte Riadhi Alger) dos jogos de 1972/73; ES Sétif é o "WR Sétif" de 1971/72 e 1972/73
    (a tabela dá ES Sétif e nenhum WR Sétif); o "IRB Relizane" dos jogos de 1985/86 é o RCM Relizane da tabela;
  - ASM Oran = ASC Oran; CA Batna = CN Batna; ES Guelma = ESM Guelma; GC Mascara = GCR Mascara; WA Boufarik = WO Boufarik;
    WA Tlemcen = WM Tlemcen; USM Bel-Abbès = ESM Bel-Abbès; USM Aïn Beïda = ISM Aïn Beïda; RC Relizane = RCM Relizane;
    MC Saïda = MB Saïda; AS Aïn M'lila = AM Aïn M'lila; WKF Collo = Entente Collo; OMR El Annasser = OM Ruisseau;
  - DNC Alger = OC Alger = CS DNC Alger = JH Djazaïr (1985: "JH Djazaïr aka DNC Alger"): o nome mais usado;
  - o USM Annaba dos anos 1960 e 1970 é o atual Hamra Annaba ("Team founded in 1944 now known as HAMR Annaba. Not to be
    confused with the current USM Annaba ... founded in 1983"): até 1979 é "Hamra Annaba".

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
```

## 8. O que não deu para coletar

- **Fora do pacote:** a Copa da Argélia e as outras copas, a 2ª divisão e os jogos de acesso.
- **Edições sem jogos** (0): nenhuma.
- **Décadas com menos da metade dos gols com autor:** 1960s, 1970s, 1980s, 1990s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1960s, 1970s, 1980s, 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 1964/65 a 1998/99: a lista de jogos da RSSSF não fecha com a tabela da mesma página em vários clubes por ano (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a Wikipédia quase sempre confirma a tabela. Nenhum placar mudado; jogo provável no relatório. Fonte que resolveria: jornais argelinos da época (El Moudjahid) ou o arquivo da federação.
- 1974/75 e 1975/76: uma rodada inteira copiada na página (os jogos verdadeiros das rodadas 4 e 18 faltam); 1972/73: rodada 10 repetida (cópia descartada).
- Mando provavelmente trocado: o mesmo mandante x visitante duas vezes na temporada, com placares diferentes (1964/65, 1966/67, 1973/74, 1976/77, 1979/80, 1980/81, 1983/84, 1986/87, 1988/89...): ficou como na página.
- 1962/63 e 1963/64: ligas regionais incompletas (1962/63 sem a 1ª fase; 1963/64 só os resultados conhecidos, grupo Leste de Constantine sem números).
- 2009/10: CA Bordj Bou Arréridj x MC Alger com "derrota para os dois" (o formato do pacote não representa; jogo sem placar).
- Identidade a conferir: DNC Alger = OC Alger = CS DNC Alger = JH Djazaïr (nome de exibição "DNC Alger"); WKF Collo = Entente Collo; o USM Annaba até 1979 é o Hamra Annaba; "US Constantine" de 1996/97 = US Chaouia; MB Rouissat = Olympique Rouissat (2025/26).

## 10. Arquivos e comandos

Código em `coleta/alg-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_ogol.py` | Baixa o calendário de cada edição da 1ª divisão argelina no ogol para data/coleta/alg-1/ogol/<id>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão argelina para data/coleta/alg-1/rsssf/: a lista de campeões (algchamp.html) e as |
| `baixar_wikipedia.py` | Baixa da Wikipédia em inglês (wikitexto, pela API) a lista de campeões ("List of Algerian football champions", com o |
| `clubes_alg.py` | Identidade dos clubes argelinos: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão argelina (alg-1): o campeonato nacional, de 1962/63 a 2025/26. |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão argelina, edição a edição (entram no relatório). |
| `importar.py` | Junta as fontes da 1ª divisão argelina e grava o pacote em data/coleta/alg-1/pacote/ e o relatório em docs/coleta/alg-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/alg-1/rsssf/) com o leitor comum (rsssf_africa), |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol (copiado de coleta/chi-1/outras_fontes.py, sem a ESPN, que não tem a liga egípcia). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |
| `wiki_tabelas.py` | Tabelas finais dos artigos de temporada da Wikipédia em inglês (data/coleta/alg-1/wikipedia/en_<temporada>.txt) e a |

- Fontes baixadas: `data/coleta/alg-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-africa/`, do ogol em `data/cache/ogol-alg-1/`.
- Pacote: `data/coleta/alg-1/pacote/`; relatório: `docs/coleta/alg-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/alg-1/baixar_ogol.py
python coleta/alg-1/baixar_rsssf.py
python coleta/alg-1/baixar_wikipedia.py
python coleta/alg-1/importar.py
python coleta/alg-1/conferir.py [-v temporada]   # divergências
python coleta/comum-africa/testar_carga.py alg-1 <scratchpad>
python coleta/comum-africa/documentar.py
```

