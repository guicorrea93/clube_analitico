# Campeonato Papua-Nova-Guineense (`png-1`) — documentação

Gerado por `python coleta/comum-oceania/documentar.py` a partir do pacote `data/coleta/png-1/pacote/`, do código `coleta/png-1/` e do relatório `docs/coleta/png-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 19, de 2006 a 2026; 0 sem jogos.
- **Jogos:** 1336 (1329 com placar); **gols:** 4701; **gols com autor:** 503 (11%); **cartões:** 0.
- **Clubes:** 78; **artilheiros:** 0 edições com artilheiro (0 linhas, com empates).
- **Classificação final:** 19 edições; **tabelas publicadas guardadas para conferência:** 200 linhas.
- **No banco:** sim; **último commit do pacote:** 60aaa017.
- **Observação da competição:** 1ª divisão de Papua-Nova Guiné desde 2006: a National Soccer League, semiprofissional, rebatizada Premier Soccer League em 2023, uma edição por título, como na lista de campeões da RSSSF (2021, abandonada, fica de fora). Fase regular (ou conferências regionais) e o mata-mata dos primeiros. O campeonato amador de clubes (1976-2005) não entra.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão de Papua-Nova Guiné (png-1): a National Soccer League (2006-2022), rebatizada Premier Soccer League
em 2023, uma edição por título, como na lista de campeões da RSSSF (pngchamp.html). Escopo aprovado pelo Guilherme em
24/11/2026, depois de pesquisa a fundo:
- só a NSL/PSL, desde 2006 (o campeonato amador de clubes de 1976-2005 fica de fora; continuou depois, abaixo da NSL);
- 2021 fica de fora (abandonada, sem campeão; o playoff que houve valeu só a vaga na OFC); a "National Premier League"
  rebelde de 2017-2018 (federação FFPNG, dissolvida na reunificação) também;
- 2008/09 e 2017: a final não foi jogada, o campeão é o 1º da fase regular; 2014: a final foi abandonada com 3-0 para o
  Hekari, que ficou com o título; 2026: sem playoff (o 1º da fase regular é o campeão).

A RSSSF tem uma página por temporada (a lista de campeões não liga quase nenhuma): fase regular (ou conferências regionais
em 2015/16, 2019 e 2022) e o mata-mata dos primeiros; 2011/12 só a tabela e o mata-mata. Pontuação 3-1-0.

Cada trecho é (página, linha inicial, linha final, fase, grupo), em linhas do texto puro (rsssf_oce.texto).
```

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 15.
- **Edições com alguma tabela divergente** (3; motivo no relatório, na edição): 2023, 2025, 2026.
- **Edições sem tabela para conferir** (1): 2011/12.
- **Edições com menos jogos que o esperado:** 2023 (58 de 60), 2025 (112 de 113), 2026 (130 de 132).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 2000s | 4 | 204 | 100% | 0% | 93% | 0% | 0% | 0% | 24% | 0.0 |
| 2010s | 10 | 612 | 100% | 0% | 94% | 0% | 0% | 0% | 15% | 0.0 |
| 2020s | 5 | 520 | 100% | 0% | 96% | 0% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na Oceania: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 2006: 5 clubes
- 2007/08: 7 clubes
- 2008/09: 8 clubes
- 2009/10: 9 clubes
- 2010/11 a 2011/12: 7 clubes
- 2013: 8 clubes
- 2014 a 2015: 7 clubes
- 2015/16: 12 clubes
- 2017: 6 clubes
- 2018: 7 clubes
- 2019: 27 clubes
- 2019/20: 10 clubes
- 2022: 30 clubes
- 2023 a 2024: 8 clubes
- 2025: 11 clubes
- 2026: 12 clubes

**Pontos por vitória:**

- 2006 a 2026: 3

**Nome oficial:**

- 2006 a 2022: National Soccer League <ano>
- 2023 a 2026: Premier Soccer League <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 2006: fase regular (5 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2007/08: fase regular (7 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2008/09: fase regular (8 clubes) + semifinais; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2009/10: fase regular (9 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2010/11: fase regular (7 clubes) + semifinais + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2011/12: jogos incompletos: fase regular (7 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2013: fase regular (8 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2014: fase regular (7 clubes) + semifinais + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2015: fase regular (7 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2015/16: conferências regionais (12 clubes) + grupo do título (4 clubes) + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2017: fase regular (6 clubes) + semifinais; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2018: fase regular (7 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2019: conferências regionais (27 clubes) + quartas de final + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2019/20: fase regular (10 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2022: conferências regionais (30 clubes) + playoff das conferências + quartas de final + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2023 a 2024: fase regular (8 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2025: fase regular (11 clubes) + semifinais + 3º lugar + final; 3 pontos por vitória, 1 por empate e 0 por derrota
- 2026: pontos corridos (12 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota

**Fases e grupos de cada edição com mais de uma fase:**

- 2006: Fase regular (liga); Semifinal (mata_mata, ida_volta); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2007/08: Fase regular (liga); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2008/09: Fase regular (liga); Semifinal (mata_mata, jogo_unico)
- 2009/10: Fase regular (liga); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2010/11: Fase regular (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2011/12: Fase regular (liga); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2013: Fase regular (liga); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2014: Fase regular (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2015: Fase regular (liga); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2015/16: Fase regional (liga); Grupo do título (liga); Final (mata_mata, jogo_unico)
- 2017: Fase regular (liga); Semifinal (mata_mata, jogo_unico)
- 2018: Fase regular (liga); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2019: Fase regional (liga); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2019/20: Fase regular (liga); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2022: Fase regional (liga); Playoff da conferência (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2023: Fase regular (liga); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2024: Fase regular (liga); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2025: Fase regular (liga); Semifinal (mata_mata, jogo_unico); Disputa do 3º lugar (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 19 edições

**Observações das edições:**

- 2008/09: a final (Hekari Souths United x CMSS Rapatona Tigers) não foi jogada: o Hekari, 1º da fase regular, foi declarado campeão
- 2011/12: a RSSSF só tem a tabela da fase regular e o mata-mata
- 2014: a final foi abandonada aos 70' com 3-0 para o Hekari United (violência da torcida); o título ficou com o Hekari
- 2015/16: duas zonas de 6; os 2 primeiros de cada zona num grupo de 4 ("National Champions League") e depois a final
- 2017: a final (Lae City Dwellers x Madang FC) foi cancelada: o Lae City Dwellers, 1º da fase regular, foi declarado campeão
- 2018: em 3 de maio os jogos restantes da fase regular viraram W.O. (só 4 clubes tinham pago a taxa)
- 2019: quatro conferências regionais e o mata-mata
- 2019/20: parada de 19/03 a 08/08/2020 (covid-19)
- 2022: cinco conferências regionais (nas duas das ilhas, playoff entre o 1º e o 2º pela vaga) e o mata-mata (de outubro de 2022 a fevereiro de 2023)
- 2023: a liga passa a se chamar Premier Soccer League
- 2026: sem playoff: o 1º da fase regular é o campeão

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Hekari United: 10
- Lae City: 7
- Gulf Komara: 2

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 2006 | Hekari United | Gelle Hills United |
| 2007/08 | Hekari United | Gelle Hills United |
| 2008/09 | Hekari United | Rapatona |
| 2009/10 | Hekari United | Morobe United |
| 2010/11 | Hekari United | Eastern Stars |
| 2011/12 | Hekari United | Eastern Stars |
| 2013 | Hekari United | FC Port Moresby |
| 2014 | Hekari United | Lae FC |
| 2015 | Lae City | Madang FC |
| 2015/16 | Lae City | Hekari United |
| 2017 | Lae City | Madang FC |
| 2018 | Lae City | Besta PNG United |
| 2019 | Lae City | Hekari United |
| 2019/20 | Lae City | Vitiaz United |
| 2022 | Lae City | Hekari United |
| 2023 | Hekari United | Lae City Dwellers |
| 2024 | Hekari United | Gulf Komara |
| 2025 | Gulf Komara | Morobe Wawens |
| 2026 | Gulf Komara | Hekari United |

**Rebaixados marcados na classificação:** 0 em 0 edições (só onde a tabela publicada marca a queda).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- nenhum

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/png-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 2)

- **png2014 · 89:** «[abandoned at 1-0 in 89' due to» → «[abandoned at 1-0 in 89' due to crowd trouble]»: a nota continua na linha de baixo, ao lado do jogo seguinte
- **png2014 · 90:** «crowd trouble]» → «»: o fim da nota de cima (não é nota deste jogo)

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 9)

- **png2018 · 95:** ({'especial': 'derrota_ambos', 'gc_ambos': 3}, 'jogo não disputado: a federação deu derrota por 0-3 aos dois clubes ("awarded 0-3 against both clubs"; a tabela da página conta os 3 gols contra para cada um)')
- **png2018 · 146:** ({'especial': 'derrota_ambos', 'gc_ambos': 3}, 'jogo não disputado: a federação deu derrota por 0-3 aos dois clubes ("awarded 0-3 against both clubs"; a tabela da página conta os 3 gols contra para cada um)')
- **png06 · 171:** ({'gm': 0, 'gv': 0}, 'semifinal abandonada com 0-0 por falta de luz e jogada de novo no dia seguinte (5-6 na prorrogação)')
- **png06 · 174:** ({'nota': 'aet; jogo repetido (o de 18/11 foi abandonado com 0-0 por falta de luz)'}, 'nota da página ("[aet] [replay]") reescrita')
- **png2014 · 89:** ({'gm': 1, 'gv': 0}, "abandonado aos 89' com 1-0 (briga na torcida); não foi jogado de novo nem entrou na tabela")
- **png2019 · 471:** ({'gm': 0, 'gv': 0}, "quartas de final abandonadas aos 48' com 0-0 (campo alagado) e jogadas de novo em 16/05")
- **png2022 · 88:** ({'gm': 2, 'gv': 0}, "abandonado aos 57' com 2-0 (falta de luz) e jogado de novo em 23/11 (4-2)")
- **png2025 · 291:** ({'especial': 'wo_m'}, 'o Hekari United não se apresentou ("dns"): W.O. para o Lae City, 3º lugar')
- **png2014 · 152:** ({'gm': 0, 'gv': 3, 'especial': ''}, "a final foi abandonada aos 70' com 0-3 (violência da torcida); o resultado ficou e o Hekari United foi o campeão (lista de campeões da RSSSF)")

### 3º lugar de disputa sem placar na página (`TERCEIROS`, 1)

- **2014:** ('Morobe United', 'a disputa do 3º lugar está na página como "Gigira Laitepo Morobe bt Oro [aet]" (vitória na prorrogação, placar desconhecido)')

### Tabelas da página que não são da edição (`TABELAS_FORA`, 1)

- **png2023 · 133:** tabela depois da 11ª rodada (a final vem no fim da fase)

### Divergências entre fontes já explicadas (`EXPLICACOES`, 3)

- **2023:** dois jogos da 12ª rodada (United Highlands x Lae City e Lae City Dwellers x Morobe Wawens, este abandonado no 2º tempo) estão na página como empate sem placar ("drw"); a tabela os conta como empates e eles ficam de fora dos jogos
- **2025:** um jogo remarcado da 15ª rodada (Morobe Wawens x Hekari United, 1-0 no intervalo) está na página como empate sem placar; a tabela o conta como empate e ele fica de fora dos jogos
- **2026:** dois jogos do Lae City (Lae City Dwellers x Lae City, 17ª rodada, "possivelmente 1-3"; Finschhafen Bavarians x Lae City, 18ª) estão na página só como derrota do mandante, sem placar ("lt"); a tabela os conta e eles ficam de fora dos jogos

### Identidade dos clubes

Regras em `coleta/png-1/clubes_png.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes de Papua-Nova Guiné (png-1): cada grafia da RSSSF vira um clube, com cidade e província (região).

Decisões aprovadas pelo Guilherme em 24/11/2026, depois de pesquisa a fundo (RSSSF, Wikipédia, ogol, imprensa de PNG):
- "Lae City": o Lae City Dwellers fundado em 2014 (na NSL desde 2015), rebatizado Toti City em 2018 e Lae City em 2019/20 é
  um clube só, o dos 7 títulos (2015, 2015/16, 2017, 2018, 2019, 2019/20, 2022); o "Lae City Dwellers" que aparece desde
  2022, ao lado do Lae City, é outro clube (fundado em 2021);
- "Hekari United": PRK Souths United (2006), Hekari Souths United (2007/08-2009/10), Hekari United, PNG Hekari (2026);
- "Gulf Komara": Erema FC (2015/16) e PRK Gulf Komara (2019, 2019/20);
- "Madang FC": Madang Flying Fox (2006), Madang Fox / Madang Niupetro Fox (2007/08-2010/11), Madang FC, Madang United (2026);
- "Rapatona": Inspac Rapatona, CMSS Rapatona Tigers (2007/08-2009/10), Rapatona FC (2015/16);
- "Morobe United": Tuguba Laitepo Blue Kumuls (2006), Morobe Kumuls (2007/08, "formerly Tuguba Laitepo Blue Kumuls"),
  Gigira Laitepo Morobe (2008/09-2014; "KTB = Kikira Tuguba Laitepo"; em 2011/12 Gigira Laitepo Central Coast), Welgris
  Morobe United (2015/16) e Morobe United (2019 e 2019/20);
- "Welgris Highlanders": Welgris Momads (2006; a RSSSF de 2007/08: "formerly Welgris Momads");
- "Besta PNG United": entrou na NSL em 2009/10 como a seleção sub-20 ("Besta PNG FA Under-20", até 2010/11; Wikipédia), PNG
  Besta United em 2013; "Eastern Stars" (Huawei Eastern Stars em 2014); "Port Moresby Strikers" (Southern Strikers em 2018-2019; Wikipédia:
  "also known as Southern Strikers", fundado em 2017); "PS United" (PS Huawei em
  2015/16, Huawei PS United em 2017); "Buang" (Prima Buang em 2017); "Morobe Wawens" (FC Morobe Wawens, Agmark FC Morobe
  Wawens); "Oro FC" (NC Civil Works Oro em 2013; "Oro" sozinho é o clube do México); "Tavur" (West New Britain Tavur em 2013); "Lahi" (Lahi Snax em 2019);
  "Greengold" (NBPOL Greengold Liners em 2019); "Rabaul Radazz"; "FC Kutubu"; "NCD" (National Capital District FC);
- separados: Lae FC (2014), Morobe Wawens, Besta PNG United, Besta Madang Fighters ("Madang Besta" na RSSSF, 2007/08), Gigira Laitepo United (2015/16, zona
  sul: franquia nova "com nome parecido", Gigira Amoana em 2017; Wikipédia), Admiralty Palaiau (2014-2015/16) e Admiralty Island (2024-2026), Goroka Gosiha (2015/16) e Goroka FC (2022), Mount Hagen FC (2019) e
  Hagen FC (2022), Markham FC (2019) e Radza FC (Markham, 2022), Aporro Mai (Kutubu, 2019) e FC Kutubu (2019/20); Blue Kumuls
  (Mount Hagen, 2019; não confundir com o Blue Kumuls de Lae, hoje Morobe United) e Ape Aporo (2022: fusão dele com o Aporro Mai);
- "Central United Port Moresby": o Central United de 2019 (a NZ tem o Central United de Auckland).

Uso: clube(nome, ano) -> nome de exibição (ou None).
```

## 8. O que não deu para coletar

- **Edições sem jogos** (0): nenhuma.
- **Décadas com menos da metade dos gols com autor:** 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 2011/12 só com a tabela da fase regular e o mata-mata (a RSSSF não tem as rodadas).
- Jogos sem placar na página ("drw", "lt", "bt") ficam de fora: 2 em 2023, 1 em 2025, 2 em 2026 e a disputa do 3º lugar de 2014 (o 3º entra na classificação).
- 2021 fora (abandonada, sem campeão); o campeonato amador de clubes (1976-2005) e a National Premier League rebelde (2017-2018) não entram: podem virar competições à parte.
- Autores dos gols em poucas temporadas (a RSSSF quase não traz); artilheiros, cartões, estádio e público não coletados.
- Cidade desconhecida de alguns clubes regionais de 2019 e 2022 (fica só a província).

## 10. Arquivos e comandos

Código em `coleta/png-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Separa os autores dos gols do texto da RSSSF ("Mark Elrick 78', 95' - Jeremy Seales 1'") em gols, um por linha. |
| `baixar_ogol.py` | Baixa os calendários do ogol da liga de Papua-Nova Guiné ("Liga Papua-Nova Guiné", competição 2828) para |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF de Papua-Nova Guiné para data/coleta/png-1/rsssf/ (lista de campeões, lista de finais da copa e |
| `baixar_wikipedia.py` | Baixa o wikitexto da página "Papua New Guinea Premier Soccer League" (a antiga National Soccer League) da Wikipédia em inglês (lista de campeões) para |
| `clubes_png.py` | Identidade dos clubes de Papua-Nova Guiné (png-1): cada grafia da RSSSF vira um clube, com cidade e província (região). |
| `conferir.py` | Confere a soma dos jogos de cada fase (e grupo) com as tabelas publicadas pela RSSSF no mesmo trecho. |
| `edicoes.py` | Edições da 1ª divisão de Papua-Nova Guiné (png-1): a National Soccer League (2006-2022), rebatizada Premier Soccer League |
| `explicacoes.py` | Correções e decisões da coleta de Papua-Nova Guiné (png-1), sempre com o motivo. |
| `importar.py` | Junta as fontes da 1ª divisão de Papua-Nova Guiné e grava o pacote em data/coleta/png-1/pacote/ e o relatório em |
| `ler.py` | Lê os jogos e as tabelas de cada edição nas páginas da RSSSF (data/coleta/png-1/rsssf/), trecho a trecho (edicoes.py), |

- Fontes baixadas: `data/coleta/png-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-oceania/`, do ogol em `data/cache/ogol-png-1/`.
- Pacote: `data/coleta/png-1/pacote/`; relatório: `docs/coleta/png-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/png-1/baixar_ogol.py
python coleta/png-1/baixar_rsssf.py
python coleta/png-1/baixar_wikipedia.py
python coleta/png-1/importar.py
python coleta/png-1/conferir.py [-v temporada]   # divergências
python coleta/comum-oceania/testar_carga.py png-1 <scratchpad>
python coleta/comum-oceania/documentar.py
```

