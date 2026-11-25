# Campeonato Salomonense (`sol-1`) — documentação

Gerado por `python coleta/comum-oceania/documentar.py` a partir do pacote `data/coleta/sol-1/pacote/`, do código `coleta/sol-1/` e do relatório `docs/coleta/sol-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 25, de 2000 a 2025; 4 sem jogos.
- **Jogos:** 1464 (1459 com placar); **gols:** 5857; **gols com autor:** 97 (2%); **cartões:** 0.
- **Clubes:** 62; **artilheiros:** 0 edições com artilheiro (0 linhas, com empates).
- **Classificação final:** 25 edições; **tabelas publicadas guardadas para conferência:** 214 linhas.
- **No banco:** ainda não; **último commit do pacote:** nenhum (pacote ainda não commitado).
- **Observação da competição:** 1ª divisão das Ilhas Salomão desde 2000, uma edição por título, como na lista de campeões da RSSSF: o campeonato nacional de clubes (2000 a 2009/10: grupos e mata-mata, com os melhores de Honiara e os campeões das províncias) e a Telekom S-League (2010/11 em diante, pontos corridos; S-League em 2025). 2000-2002 só com o campeão; 2012/13 não houve. A liga de Honiara (1947-1999) não entra.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão das Ilhas Salomão (sol-1), uma por título, como na lista de campeões da RSSSF (solomchamp.html):
o campeonato nacional de clubes (National Club Championship, 2000 a 2009/10: torneio curto com os melhores de Honiara e os
campeões das províncias) e a Telekom S-League (2010/11 a 2024; "S-League" em 2025). Escopo aprovado pelo Guilherme em
25/11/2026, depois de pesquisa a fundo:
- fora: a liga de Honiara (1947-1999, regional, só campeões), a "S-League" de franquias de Honiara (2004 e 2005), a Solomon
  Cup e o Interprovincial (seleções de província), o Knockout Championship e os playoffs da OFC;
- 2000-2002 só com o campeão; 2004 só com a final (por W.O.); 2011/12 só a tabela; 2012/13 não houve; 2026 fica de fora até
  o título sair (depende de punições ainda pendentes na federação);
- 2015/16: campeão o Western United, que ganhou o playoff final (RSSSF); o Solomon Warriors, campeão pela Wikipédia, foi o
  1º da fase regular. 2017/18: o Solomon Warriors ganhou a fase regular e o playoff ("TSL Championship 2018").

A RSSSF nomeia a página pelo ano em que a temporada termina (solom2016 = 2015/16, solom2017 = 2016); a de 2006 (solom06) traz o
campeonato de fevereiro de 2006, que a lista chama de 2005/06. Pontuação 3-1-0.

Cada trecho é (página, linha inicial, linha final, fase, grupo), em linhas do texto puro (rsssf_oce.texto).
```

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 16.
- **Edições com alguma tabela divergente** (4; motivo no relatório, na edição): 2005/06, 2006/07, 2009/10, 2010/11.
- **Edições sem tabela para conferir** (5): 2000, 2001, 2002, 2004, 2011/12.
- **Edições com menos jogos que o esperado:** 2005/06 (24 de 30), 2006/07 (13 de 12), 2009/10 (33 de 34), 2010/11 (52 de 56).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 2000s | 10 | 156 | 98% | 0% | 6% | 0% | 0% | 0% | 14% | 0.0 |
| 2010s | 9 | 537 | 100% | 0% | 96% | 0% | 0% | 0% | 0% | 0.0 |
| 2020s | 6 | 771 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na Oceania: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 2000 a 2002: 1 clubes
- 2003: 8 clubes
- 2004: 2 clubes
- 2005/06: 11 clubes
- 2006/07: 9 clubes
- 2007/08 a 2008/09: 12 clubes
- 2009/10: 14 clubes
- 2010/11 a 2011/12: 8 clubes
- 2013/14 a 2016: 9 clubes
- 2017/18 a 2018: 8 clubes
- 2019/20: 9 clubes
- 2020/21: 11 clubes
- 2021 a 2025: 12 clubes

**Pontos por vitória:**

- 2000 a 2002: 
- 2003 a 2025: 3

**Nome oficial:**

- 2000 a 2009/10: National Club Championship <ano>
- 2010/11 a 2024: Telekom S-League <ano>
- 2025: S-League <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 2000 a 2002: só o campeão (sem jogos nem tabela)
- 2003: fase de grupos (8 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2004: jogos incompletos: final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2005/06: jogos incompletos: fase de grupos (11 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2006/07: jogos incompletos: fase de grupos (9 clubes) + semifinais + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2007/08 a 2008/09: fase de grupos (12 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2009/10: fase de grupos (14 clubes) + quartas de final + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2010/11: jogos incompletos: pontos corridos (8 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2011/12: só a tabela final (sem jogos); 3 pontos por vitória
- 2013/14 a 2014/15: pontos corridos (9 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2015/16: jogos incompletos: fase regular (9 clubes) + quartas de final + semifinais + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2016: pontos corridos (9 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2017/18: fase regular (8 clubes) + quartas de final + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2018: pontos corridos (8 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2019/20: pontos corridos (9 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2020/21: pontos corridos (11 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota
- 2021 a 2025: pontos corridos (12 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota

**Fases e grupos de cada edição com mais de uma fase:**

- 2003: Fase de grupos (liga); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2005/06: Fase de grupos (liga); Semifinal (mata_mata, ida_volta); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2006/07: Fase de grupos (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2007/08: Fase de grupos (liga); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2008/09: Fase de grupos (liga); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2009/10: Fase de grupos (liga); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2015/16: Fase regular (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2017/18: Fase regular (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 21 edições
- lista de campeões da RSSSF: 4 edições

**Observações das edições:**

- 2000: só o campeão na RSSSF
- 2001: só o campeão na RSSSF
- 2002: só o campeão na RSSSF
- 2003: em Yandina, em novembro
- 2004: a RSSSF dá os 9 inscritos (2 grupos) e a final, vencida por W.O.: o Makuru, de dono adventista, não joga aos sábados; só a final na RSSSF
- 2005/06: em Honiara, de 20/02 a 01/03/2006; a página dá alguns jogos da fase de grupos sem placar (só "drw" ou "bt")
- 2006/07: em maio de 2007; a página não traz o placar de 4 jogos da fase de grupos (as tabelas são parciais)
- 2007/08: em junho de 2008
- 2008/09: em junho de 2009
- 2009/10: em maio de 2010
- 2010/11: 1ª Telekom S-League (fevereiro a maio de 2011); a página não traz o placar dos 4 jogos da 12ª rodada
- 2011/12: a RSSSF só tem a tabela final
- 2013/14: Marist desclassificado em 08/11 (não pagou a inscrição): os jogos do 1º turno viraram 0-3
- 2015/16: fase regular (1º o Solomon Warriors) e playoff dos 8 primeiros; o campeão é o do playoff (RSSSF; a Wikipédia dá o Solomon Warriors); o jogo de volta Western United x Real Kakamora (quartas) está na página sem placar ("unk", 2-1 no intervalo)
- 2016: Koloale suspenso em 04/12 ("non-compliance"): os 5 jogos restantes viraram 0-3
- 2017/18: fase regular (agosto a novembro de 2017) e o playoff dos 8 primeiros ("TSL Championship", março de 2018); o Solomon Warriors ganhou os dois
- 2025: a liga passa a se chamar só "S-League"

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Solomon Warriors: 7
- Koloale: 6
- Marist: 3
- Central Coast: 3
- Western United: 2
- Laugu United: 1
- Central Realas: 1
- KOSSA: 1
- Henderson Eels: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 2000 | Laugu United | — |
| 2001 | Koloale | — |
| 2002 | Koloale | — |
| 2003 | Koloale | Auki Kingz |
| 2004 | Central Realas | Makuru |
| 2005/06 | Marist | Koloale |
| 2006/07 | KOSSA | Koloale |
| 2007/08 | Koloale | Makuru |
| 2008/09 | Marist | Koloale |
| 2009/10 | Koloale | Solomon Warriors |
| 2010/11 | Koloale | Solomon Warriors |
| 2011/12 | Solomon Warriors | Western United |
| 2013/14 | Solomon Warriors | KOSSA |
| 2014/15 | Western United | Solomon Warriors |
| 2015/16 | Western United | Koloale |
| 2016 | Marist | Western United |
| 2017/18 | Solomon Warriors | Marist |
| 2018 | Solomon Warriors | Henderson Eels |
| 2019/20 | Solomon Warriors | Henderson Eels |
| 2020/21 | Henderson Eels | Solomon Warriors |
| 2021 | Central Coast | Solomon Warriors |
| 2022/23 | Solomon Warriors | KOSSA |
| 2023 | Solomon Warriors | Central Coast |
| 2024 | Central Coast | Solomon Warriors |
| 2025 | Central Coast | Malaita Kingz |

**Rebaixados marcados na classificação:** 0 em 0 edições (só onde a tabela publicada marca a queda).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 2013/14: KOSSA -2
- 2013/14: X-Beam -2

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/sol-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 17)

- **solom07 · 85:** «Koloale  FC» → «Koloale FC»: espaço duplo no meio do nome (o leitor lia só "FC")
- **solom2013 · 32:** «-.Marist» → «9.Marist»: o desclassificado vem sem posição ("-.") e o leitor pulava a linha
- **solom2013 · 133:** «-.Marist» → «9.Marist»: o desclassificado vem sem posição ("-.") e o leitor pulava a linha
- **solom2013 · 208:** «-.Marist» → «9.Marist»: o desclassificado vem sem posição ("-.") e o leitor pulava a linha
- **solom2013 · 33:** «disqualified; playing record;      4   1  2  1   2- 2   5» → «[playing record before disqualification: 4 games, 1 win, 2 draws, 1 loss, goals 2-2]»: a campanha do Marist antes da desclassificação, numa linha sem nome, era lida como linha de tabela
- **solom2013 · 134:** «disqualified; playing record;      4   1  2  1   2- 2   5» → «[playing record before disqualification: 4 games, 1 win, 2 draws, 1 loss, goals 2-2]»: a campanha do Marist antes da desclassificação, numa linha sem nome, era lida como linha de tabela
- **solom2013 · 209:** «disqualified; playing record;      4   1  2  1   2- 2   5» → «[playing record before disqualification: 4 games, 1 win, 2 draws, 1 loss, goals 2-2]»: a campanha do Marist antes da desclassificação, numa linha sem nome, era lida como linha de tabela
- **solom2010 · 86:** «[awarded to Rendova Devon as» → «[awarded to Rendova Devon as Northern United used Koloale players who had not been released]»: a nota continua nas três linhas de baixo, ao lado de outros jogos
- **solom2010 · 87:** «Northern United used Koloale» → «»: pedaço da nota do jogo de cima
- **solom2010 · 88:** «players who had not been» → «»: pedaço da nota do jogo de cima
- **solom2010 · 89:** «released]» → «»: fim da nota do jogo de cima
- **solom2011 · 69:** «[awarded 0-3; originally 3-1;» → «[awarded 0-3; originally 3-1; KOSSA used an unregistered player]»: a nota continua nas duas linhas de baixo
- **solom2011 · 70:** «KOSSA used an unregistered» → «»: pedaço da nota do jogo de cima, ao lado da data
- **solom2011 · 71:** «player]» → «»: fim da nota do jogo de cima
- **solom2025 · 215:** «[match postponed on Sep 28 due to weather» → «[match postponed on Sep 28 due to weather conditions and not refixtured but awarded as 0-0 in the standings]»: a nota continua nas duas linhas de baixo
- **solom2025 · 216:** «conditions and not refixtured but awarded» → «»: pedaço da nota do jogo de cima
- **solom2025 · 217:** «as 0-0 in the standings]» → «»: fim da nota do jogo de cima, ao lado do "Round 17"

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 5)

- **solom04 · 28:** ({'especial': 'wo_m'}, 'final por W.O.: o Makuru, de dono adventista, não joga aos sábados')
- **solom2010 · 86:** ({'especial': 'wo_v'}, '5-1 em campo, mas os pontos foram dados ao Rendova Devon (o Northern United usou jogadores do Koloale que não tinham sido liberados); a tabela conta vitória sem gols')
- **solom06 · 82:** ({}, 'semifinal abandonada (chuva forte) e jogada de novo em 01/03 (Koloale 2-1)')
- **solom09 · 80:** ({'gm': 3, 'gv': 2}, "abandonado aos 72' com 3-2 (briga na torcida); não entra na tabela")
- **solom2025 · 108:** ({}, "abandonado aos 24' (chuva forte) e jogado de novo no dia seguinte (Malaita Kingz 1-0)")

### 3º lugar de disputa sem placar na página (`TERCEIROS`, 1)

- **2015/16:** ('KOSSA', 'a disputa do 3º lugar está na página como "KOSSA bt Solomon Warriors" (vitória, placar desconhecido)')

### Divergências entre fontes já explicadas (`EXPLICACOES`, 4)

- **2005/06:** seis jogos da fase de grupos estão na página sem placar ("drw" e "bt": Tematangi x Mafi, Tematangi x Kuara, Camp United x Ngaube, Marist x Kuara, Koloale x Camp United, Aimela x Ngaube); as tabelas os contam e eles ficam de fora dos jogos (a página avisa: "missing goals of various matches")
- **2006/07:** a tabela do grupo A é de antes da última rodada (Koloale 2-1 Marist vem depois dela), e os jogos com "-" (sem placar) não estão em nenhuma das duas
- **2009/10:** um jogo do grupo B está na página só como vitória sem placar ("Rendova Devon bt Ka'arua"); a tabela o conta ("w/o goals") e ele fica de fora dos jogos
- **2010/11:** os 4 jogos da 12ª rodada estão na página só com o resultado, sem placar ("drw", "lt"); a tabela os conta ("w/o goals round 12") e eles ficam de fora dos jogos

### Identidade dos clubes

Regras em `coleta/sol-1/clubes_sol.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes das Ilhas Salomão (sol-1): cada grafia da RSSSF vira um clube, com cidade e província (região).

Decisões aprovadas pelo Guilherme em 25/11/2026, depois de pesquisa a fundo (RSSSF, inclusive a lista de fundação dos
clubes, Wikipédia e ogol):
- "Solomon Warriors": fundado em 1981 como Uncles FC (no campeonato nacional até 2008/09), Solomon Warriors desde maio de
  2010 (na "S-League" de franquias de 2004 e 2005, que não entra, jogou como Wantoks);
- "Marist": Marist Fire FC na S-League de 2010/11 a 2015/16 (Systek Kingz nas franquias de 2004 e 2005);
- "KOSSA" (Kossa FC; Fair West nas franquias); "Makuru" (JP Su'uria nas franquias); "Real Kakamora" (Kakamora FC até 2010;
  a seleção de Makira de mesmo nome, na Solomon Cup, é outra equipe); "Laugu United" (Blue Boys de 2009 a 2018); "Central
  Coast" (CY Strikers até 2019); "Ghupo" (Ghupo Wantoks em 2026, sem relação com o Wantoks de 2004);
- grafias da mesma equipe: "Kokohale" ("Kohohale", "FK Kokohale FC"), "Paritasi" ("Paratasi"), "FC Guadalcanal"
  ("Guadalcanal"), "Isabel United" ("FC Isabel United"), "Juniper Tree" ("FC Juniper Tree"), "Camp United" (o "Central
  United FC" de Gizo: a tabela de 2005/06 dá os dois nomes; fica o de uso, que não se confunde com o da Nova Zelândia);
- Malaita Kingz (S-League) e Auki Kingz (campeonato nacional de 2003 e 2006/07) ficam separados (nenhuma fonte liga os dois);
- homônimos de clubes de outros países já no banco levam a cidade ou a província: "Southern United Honiara" (o Southern
  United é da Nova Zelândia), "Northern United Malaita" (o Northern United é de Gana) e "Kula FC (Ilhas Salomão)" (o Kula é
  de Papua-Nova Guiné; a cidade do clube não foi achada). Western United e Central Coast não colidem com nada no banco e
  ficam sem a cidade.

A região é a província ("Honiara" para a capital, que é território à parte); a cidade fica vazia quando nenhuma fonte a dá.

Uso: clube(nome, ano) -> nome de exibição (ou None).
```

## 8. O que não deu para coletar

- **Edições sem jogos** (4): 2000, 2001, 2002, 2011/12.
- **Décadas com menos da metade dos gols com autor:** 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 2000-2002 só com o campeão; 2004 só com a final (W.O.); 2011/12 só a tabela final; 2012/13 não houve.
- 2026 fora até o título sair (depende de punições pendentes na federação: Green Shield ou Central Coast).
- 2015/16: campeão Western United pela RSSSF (playoff final); a Wikipédia dá o Solomon Warriors (1º da fase regular).
- Jogos sem placar na página ("drw", "bt", "lt", "unk") em 2005/06, 2006/07, 2009/10, 2010/11 e 2015/16, explicados na conferência.
- Cidade desconhecida da maioria dos clubes das províncias (fica só a província); a do Kula FC também.
- Autores dos gols só em parte de 2005/06-2009/10; artilheiros, cartões, estádio e público não coletados.

## 10. Arquivos e comandos

Código em `coleta/sol-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Separa os autores dos gols do texto da RSSSF ("Mark Elrick 78', 95' - Jeremy Seales 1'") em gols, um por linha. |
| `baixar_ogol.py` | Baixa os calendários do ogol da liga das Ilhas Salomão ("Liga Ilhas Salomão", competição 759) para |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF das Ilhas Salomão para data/coleta/sol-1/rsssf/ (lista de campeões, lista de fundação dos clubes |
| `baixar_wikipedia.py` | Baixa o wikitexto da página "Solomon Islands S-League" da Wikipédia em inglês (lista de campeões) para |
| `clubes_sol.py` | Identidade dos clubes das Ilhas Salomão (sol-1): cada grafia da RSSSF vira um clube, com cidade e província (região). |
| `conferir.py` | Confere a soma dos jogos de cada fase (e grupo) com as tabelas publicadas pela RSSSF no mesmo trecho. |
| `edicoes.py` | Edições da 1ª divisão das Ilhas Salomão (sol-1), uma por título, como na lista de campeões da RSSSF (solomchamp.html): |
| `explicacoes.py` | Correções e decisões da coleta das Ilhas Salomão (sol-1), sempre com o motivo. |
| `importar.py` | Junta as fontes da 1ª divisão das Ilhas Salomão e grava o pacote em data/coleta/sol-1/pacote/ e o relatório em |
| `ler.py` | Lê os jogos e as tabelas de cada edição nas páginas da RSSSF (data/coleta/sol-1/rsssf/), trecho a trecho (edicoes.py), |

- Fontes baixadas: `data/coleta/sol-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-oceania/`, do ogol em `data/cache/ogol-sol-1/`.
- Pacote: `data/coleta/sol-1/pacote/`; relatório: `docs/coleta/sol-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/sol-1/baixar_ogol.py
python coleta/sol-1/baixar_rsssf.py
python coleta/sol-1/baixar_wikipedia.py
python coleta/sol-1/importar.py
python coleta/sol-1/conferir.py [-v temporada]   # divergências
python coleta/comum-oceania/testar_carga.py sol-1 <scratchpad>
python coleta/comum-oceania/documentar.py
```

