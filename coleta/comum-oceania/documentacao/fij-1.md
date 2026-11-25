# Campeonato Fijiano (`fij-1`) — documentação

Gerado por `python coleta/comum-oceania/documentar.py` a partir do pacote `data/coleta/fij-1/pacote/`, do código `coleta/fij-1/` e do relatório `docs/coleta/fij-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 50, de 1977 a 2026; 22 sem jogos.
- **Jogos:** 2177 (2172 com placar); **gols:** 6722; **gols com autor:** 194 (3%); **cartões:** 0.
- **Clubes:** 17; **artilheiros:** 0 edições com artilheiro (0 linhas, com empates).
- **Classificação final:** 50 edições; **tabelas publicadas guardadas para conferência:** 390 linhas.
- **No banco:** sim; **último commit do pacote:** 8fa059a3.
- **Observação da competição:** 1ª divisão de Fiji de 1977 a 2026: a liga das associações dos distritos (National Football League, hoje Fiji Premier League), uma edição por ano, como na lista de campeões da RSSSF. Até 1997 quase só o campeão ou a tabela final; jogos de 1998 em diante (parte deles até 2004; 2011 e 2012 só a tabela). Seleções de base de Fiji jogaram a liga em vários anos (Fiji Olympians, Fiji U-20).

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão de Fiji (fij-1): a liga das associações dos distritos ("League Championship", hoje Fiji Premier
League), uma por ano, como na lista de campeões da RSSSF (fijichamp.html), de 1977 a 2026. Escopo aprovado pelo Guilherme
em 24/11/2026, depois de pesquisa a fundo:
- RSSSF e Wikipédia batem em todos os anos; 2003 = Ba (a federação deu o título em 2006: os Olympians, 1º na tabela, já não
  existiam); 2010 = Ba (o título dado ao Lautoka no tribunal foi revogado);
- ficam de fora o Inter-District Championship, o National Club Championship, a Club Franchise League (2004/05-2006), as copas
  (Battle of the Giants, FACT, Champion vs Champion), a 2ª divisão e as repescagens com ela.

O que a RSSSF traz da liga:
- 1977-1982, 1987, 1989-1992, 1995, 1996: só o campeão (às vezes o vice: "Runners-Up");
- 1983-1986, 1988, 1993, 1994, 1997: a tabela final (1993 só a ordem), sem jogos;
- 1998 em diante: as rodadas e a tabela (2005, 2007 e 2008 com grupo do título e grupo do rebaixamento; 2011 e 2012 só a
  tabela: os jogos de 2011 vêm do ogol, conferidos com ela; o de 2012 não fecha e fica de fora).

Pontuação: 2 por vitória até 1986 (conta das tabelas), 3 a partir de 1988 (1987 sem tabela).

Cada trecho é (página, linha inicial, linha final, fase, grupo), em linhas do texto puro (rsssf_oce.texto).
```

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 20.
- **Edições com alguma tabela divergente** (1; motivo no relatório, na edição): 2005.
- **Edições sem tabela para conferir** (29): 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2012.
- **Edições com menos jogos que o esperado:** 2005 (79 de 81).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970s | 3 | 0 | — | — | — | — | — | — | — | — |
| 1980s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1990s | 10 | 74 | 93% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 10 | 895 | 99% | 0% | 80% | 1% | 0% | 0% | 5% | 0.0 |
| 2010s | 10 | 646 | 100% | 0% | 39% | 0% | 0% | 0% | 2% | 0.0 |
| 2020s | 7 | 562 | 100% | 0% | 100% | 2% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na Oceania: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1977 a 1978: 1 clubes
- 1979: 2 clubes
- 1980 a 1982: 1 clubes
- 1983 a 1986: 8 clubes
- 1987: 1 clubes
- 1988: 8 clubes
- 1989 a 1993: 1 clubes
- 1994: 10 clubes
- 1995 a 1996: 1 clubes
- 1997: 10 clubes
- 1998 a 1999: 9 clubes
- 2000: 10 clubes
- 2001 a 2003: 11 clubes
- 2004 a 2005: 10 clubes
- 2006: 11 clubes
- 2007 a 2009: 10 clubes
- 2010 a 2011: 11 clubes
- 2012 a 2013: 10 clubes
- 2014 a 2021: 8 clubes
- 2022 a 2026: 10 clubes

**Pontos por vitória:**

- 1977 a 1982: 
- 1983 a 1986: 2
- 1987: 
- 1988: 3
- 1989 a 1993: 
- 1994: 3
- 1995 a 1996: 
- 1997 a 2026: 3

**Nome oficial:**

- 1977 a 2014: National Football League <ano>
- 2015 a 2026: Fiji Premier League <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1977 a 1982: só o campeão (sem jogos nem tabela)
- 1983 a 1986: só a tabela final (sem jogos); 2 pontos por vitória
- 1987: só o campeão (sem jogos nem tabela)
- 1988: só a tabela final (sem jogos); 3 pontos por vitória
- 1989 a 1993: só o campeão (sem jogos nem tabela)
- 1994: só a tabela final (sem jogos); 3 pontos por vitória
- 1995 a 1996: só o campeão (sem jogos nem tabela)
- 1997: só a tabela final (sem jogos); 3 pontos por vitória
- 1998 a 1999: jogos incompletos: pontos corridos (9 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2000: jogos incompletos: pontos corridos (10 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2001 a 2003: jogos incompletos: pontos corridos (11 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2004: jogos incompletos: pontos corridos (10 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2005: fase de grupos (10 clubes) + grupo do título (6 clubes) + grupo do rebaixamento (4 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2006: pontos corridos (11 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2007 a 2008: fase regular (10 clubes) + grupo do título (6 clubes) + grupo do rebaixamento (4 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2009: pontos corridos (10 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2010 a 2011: pontos corridos (11 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2012: só a tabela final (sem jogos); 3 pontos por vitória
- 2013: pontos corridos (10 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2014 a 2021: pontos corridos (8 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2022 a 2026: pontos corridos (10 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota

**Fases e grupos de cada edição com mais de uma fase:**

- 2005: Fase de grupos (liga); Grupo do título (liga); Grupo do rebaixamento (liga)
- 2007: Fase regular (liga); Grupo do título (liga); Grupo do rebaixamento (liga)
- 2008: Fase regular (liga); Grupo do título (liga); Grupo do rebaixamento (liga)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 36 edições
- lista de campeões da RSSSF: 14 edições

**Observações das edições:**

- 1977: só o campeão na RSSSF
- 1978: só o campeão na RSSSF
- 1979: só o campeão na RSSSF
- 1980: só o campeão na RSSSF
- 1981: só o campeão na RSSSF
- 1982: só o campeão na RSSSF
- 1983: só a tabela final na RSSSF
- 1984: só a tabela final na RSSSF
- 1985: só a tabela final na RSSSF
- 1986: só a tabela final na RSSSF
- 1987: só o campeão na RSSSF
- 1988: só a tabela final na RSSSF
- 1989: só o campeão na RSSSF
- 1990: só o campeão na RSSSF
- 1991: só o campeão na RSSSF
- 1992: só o campeão na RSSSF
- 1993: só o campeão na RSSSF
- 1994: só a tabela final na RSSSF
- 1995: só o campeão na RSSSF
- 1996: só o campeão na RSSSF
- 1997: só a tabela final na RSSSF
- 1998: a página da RSSSF traz só parte dos jogos (a tabela é a publicada)
- 1999: a página da RSSSF traz só parte dos jogos (a tabela é a publicada)
- 2000: a página da RSSSF traz só parte dos jogos (a tabela é a publicada)
- 2001: a página da RSSSF traz só parte dos jogos (a tabela é a publicada)
- 2002: a página da RSSSF traz só parte dos jogos (a tabela é a publicada)
- 2003: a página da RSSSF traz só parte dos jogos (a tabela é a publicada)
- 2004: a página da RSSSF traz só parte dos jogos (a tabela é a publicada)
- 2005: grupos, depois o Super 6 (título) e o Pepsi 4 (rebaixamento)
- 2012: a RSSSF só tem a tabela; o calendário do ogol diverge dela em 7 clubes e falta um jogo, por isso não entra

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Ba FC: 22
- Nadi: 9
- Lautoka: 7
- Suva: 4
- Nadroga: 3
- Rewa: 3
- Labasa: 2

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1977 | Ba FC | — |
| 1978 | Nadi | — |
| 1979 | Ba FC | Nadroga |
| 1980 | Nadi | — |
| 1981 | Nadi | — |
| 1982 | Nadi | — |
| 1983 | Nadi | Lautoka |
| 1984 | Lautoka | Ba FC |
| 1985 | Nadi | Suva |
| 1986 | Ba FC | Lautoka |
| 1987 | Ba FC | — |
| 1988 | Lautoka | Rewa |
| 1989 | Nadroga | — |
| 1990 | Nadroga | — |
| 1991 | Labasa | — |
| 1992 | Ba FC | — |
| 1993 | Nadroga | — |
| 1994 | Ba FC | Labasa |
| 1995 | Ba FC | — |
| 1996 | Suva | — |
| 1997 | Suva | Labasa |
| 1998 | Nadi | Ba FC |
| 1999 | Ba FC | Nadi |
| 2000 | Nadi | Ba FC |
| 2001 | Ba FC | Fiji Olympians |
| 2002 | Ba FC | Lautoka |
| 2003 | Ba FC | Fiji Olympians |
| 2004 | Ba FC | Lautoka |
| 2005 | Ba FC | Navua |
| 2006 | Ba FC | Nadi |
| 2007 | Labasa | Lautoka |
| 2008 | Ba FC | Labasa |
| 2009 | Lautoka | Navua |
| 2010 | Ba FC | Lautoka |
| 2011 | Ba FC | Labasa |
| 2012 | Ba FC | Suva |
| 2013 | Ba FC | Nadi |
| 2014 | Suva | Ba FC |
| 2015 | Nadi | Suva |
| 2016 | Ba FC | Rewa |
| 2017 | Lautoka | Ba FC |
| 2018 | Lautoka | Ba FC |
| 2019 | Ba FC | Lautoka |
| 2020 | Suva | Rewa |
| 2021 | Lautoka | Rewa |
| 2022 | Rewa | Suva |
| 2023 | Lautoka | Rewa |
| 2024 | Rewa | Labasa |
| 2025 | Rewa | Labasa |
| 2026 | Ba FC | Labasa |

**Rebaixados marcados na classificação:** 0 em 0 edições (só onde a tabela publicada marca a queda).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1983: Nadi +2
- 1983: Ba FC -4
- 1983: Suva +2
- 1986: Suva +4
- 1997: Tavua +1
- 1998: Lautoka -2
- 1998: Rewa +1
- 2000: Labasa -1
- 2002: Lautoka -1
- 2002: Rewa -1
- 2002: Labasa -1
- 2002: Nasinu -1

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/fij-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 6)

- **fiji00 · 56:** None
- **fiji00 · 57:** None
- **fiji00 · 167:** None
- **fiji00 · 168:** None
- **fiji09 · 134:** ({'gm_of': None, 'gv_of': None, 'especial': ''}, 'a página traz Tavua 1-1 Labasa "possibly awarded 2-0"; a tabela conta o empate')
- **fiji2010 · 228:** ({'gm_of': None, 'gv_of': None, 'especial': ''}, 'Lautoka 1-1 Rewa: dado 2-0 ao Lautoka em 11/03/2011 e revogado em 10/07/2011 (o título voltou ao Ba); vale o 1-1, que é o que a tabela conta')

### Tabelas da página que não são da edição (`TABELAS_FORA`, 1)

- **fiji2025 · 128:** tabela do meio da temporada ("Hakfway Table", com erro de digitação)

### Divergências entre fontes já explicadas (`EXPLICACOES`, 1)

- **2005:** grupo do rebaixamento (Pepsi 4): três jogos só com "drw" (empate sem placar) na página ficam de fora; a tabela conta os empates

### Identidade dos clubes

Regras em `coleta/fij-1/clubes_fij.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos times de Fiji (fij-1): os times da liga são as associações dos distritos; cada grafia vira um time, com
cidade e ilha (região).

Decisões aprovadas pelo Guilherme em 24/11/2026 (pesquisa em docs/coleta/fij-1.md):
- nome do distrito puro, como a RSSSF e a própria liga escrevem ("Nadi", "Lautoka", "Rewa", "Tailevu Naitasiri"...); só o
  "Ba FC" leva o "FC" (o nome curto demais se confunde com outras coisas, como a sigla da Bahia);
- nenhum distrito mudou de identidade: "FC", "FA" e "Football Association" são formas do mesmo nome; "Tailevu-Naitasiri",
  "Tailevu/Naitasiri" = Tailevu Naitasiri; Tailevu North (Northland Tailevu) é outro time e não jogou a 1ª divisão;
- seleções de base que jogaram a liga: "Fiji Olympians" (a seleção olímpica: um time só, 1998-2006, como "Olympians",
  "U-21", "U-23" ou "Fiji U-20" nas páginas), "Fiji U-20" (2010) e "Fiji Youth Teams" (2011: a RSSSF soma numa linha a
  campanha de várias seleções de base).

Uso: clube(nome, ano) -> nome de exibição (ou None).
```

## 8. O que não deu para coletar

- **Edições sem jogos** (22): 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 2012.
- **Décadas com menos da metade dos gols com autor:** 1990s, 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 1977-1982, 1987, 1989-1993, 1995 e 1996 só com o campeão (vice em poucos anos); 1983-1988, 1994 e 1997 só a tabela.
- 1998-2004 com parte dos jogos (as tabelas da página são as publicadas, algumas "based on known results"); 2011 e 2012 só a tabela na RSSSF.
- Tabelas com erro de digitação na própria página (vitórias + empates + derrotas diferente de jogos) entram com nota.
- Autores dos gols só em parte de 2001-2010; artilheiros, cartões, estádio e público não coletados.

## 10. Arquivos e comandos

Código em `coleta/fij-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Separa os autores dos gols do texto da RSSSF ("Mark Elrick 78', 95' - Jeremy Seales 1'") em gols, um por linha. |
| `baixar_ogol.py` | Baixa os calendários do ogol da liga de Fiji ("Liga Ilhas Fiji", competição 590) para data/cache/ogol-fij-1/ e grava o resumo |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF de Fiji para data/coleta/fij-1/rsssf/ (lista de campeões, lista de finais da copa e |
| `baixar_wikipedia.py` | Baixa o wikitexto da página "Fiji Premier League" da Wikipédia em inglês (lista de campeões) para |
| `clubes_fij.py` | Identidade dos times de Fiji (fij-1): os times da liga são as associações dos distritos; cada grafia vira um time, com |
| `conferir.py` | Confere a soma dos jogos de cada fase (e grupo) com as tabelas publicadas pela RSSSF no mesmo trecho. |
| `edicoes.py` | Edições da 1ª divisão de Fiji (fij-1): a liga das associações dos distritos ("League Championship", hoje Fiji Premier |
| `explicacoes.py` | Correções e decisões da coleta de Fiji (fij-1), sempre com o motivo. |
| `importar.py` | Junta as fontes da 1ª divisão de Fiji e grava o pacote em data/coleta/fij-1/pacote/ e o relatório em docs/coleta/fij-1.md. |
| `ler.py` | Lê os jogos e as tabelas de cada edição nas páginas da RSSSF (data/coleta/fij-1/rsssf/), trecho a trecho (edicoes.py), |

- Fontes baixadas: `data/coleta/fij-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-oceania/`, do ogol em `data/cache/ogol-fij-1/`.
- Pacote: `data/coleta/fij-1/pacote/`; relatório: `docs/coleta/fij-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/fij-1/baixar_ogol.py
python coleta/fij-1/baixar_rsssf.py
python coleta/fij-1/baixar_wikipedia.py
python coleta/fij-1/importar.py
python coleta/fij-1/conferir.py [-v temporada]   # divergências
python coleta/comum-oceania/testar_carga.py fij-1 <scratchpad>
python coleta/comum-oceania/documentar.py
```

