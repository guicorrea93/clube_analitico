# Revisão: Campeonato Inglês, 1ª divisão (eng-1)

Revisor EN, 21/11/2026. Conferido o painel publicado (https://clubeanalitico.pages.dev/?c=eng-1; `dados/eng-1.js` e `index.html` do site iguais aos locais), o `db/futebol.db` (21/11 09:24, só leitura) e o pacote `data/coleta/eng-1/pacote/`.

**Resumo.** Os dados de jogo estão muito bons: os 50.950 placares batem com as matrizes de resultados da Wikipédia (1 diferença, erro da Wikipédia) e as 126 classificações finais batem linha a linha com o 11v11 (posição, J, V, E, D, GP, GC e pontos com punição); campeão, vice, 3º e rebaixados certos nas 126 temporadas.
O achado alto é a temporada 2025/26 (terminada em 24/05/2026, campeão Arsenal), que não está no banco. Na coleta: 1937/38 com Lawton 34 gols (são 28), 33 jogos com data errada (ex.: a última rodada de 1995/96, que foi em 05/05/1996) e a "rodada" do ogol, que não é rodada em 94 temporadas antigas.
No painel: a sub-aba Participantes fica vazia nas temporadas vizinhas às guerras e não mostra quem caiu; as curiosidades de campeões usam 3 pontos por vitória em todas as épocas ("título mais apertado" e "maior vantagem" errados); punições sem explicação.

Achados: `EN-001` a `EN-021` (18 abertos: 1 alto, 6 médios, 11 baixos; mais 3 `nao-e-erro`). Scripts em `revisao/EN/`, páginas em `data/cache/revisao/EN/`.

Fontes usadas (diferentes da base da coleta, que foi engsoccerdata, football-data, ogol, ESPN, RSSSF engpaul e tabelas finais da Wikipédia en):
- **11v11.com**: tabela de fim de temporada de todas as 126 temporadas (`/league-tables/league-division-one/31-july-AAAA/`, `/league-tables/premier-league/...`) e páginas de jogos por clube e temporada (`/teams/<clube>/tab/matches/season/AAAA/`), com data e placar;
- **Wikipédia en, matriz de resultados** (módulo "sports results") do artigo de cada temporada (`AAAA–AA Football League`, `... Football League First Division`, `... FA Premier League`, `... Premier League`); a coleta usou só a tabela final desses artigos;
- **RSSSF**: lista de campeões (https://www.rsssf.org/tablese/engchamp.html) e de artilheiros (https://www.rsssf.org/tablese/engtops.html), que a coleta não usou;
- páginas de temporada de clubes e de jogadores na Wikipédia en (artilheiros e o jogo Wolverhampton x Everton de 1889).

## A. Edições e títulos

- **Lista de edições:** 126, de 1888/89 a 2024/25, sem 1915/16-1918/19 e 1939/40-1945/46 (1939/40 anulada após 3 rodadas, fora do banco, como deve ser). Número de clubes por época certo: 12 (1888-91), 14 (1891/92), 16 (1892-98), 18 (1898-1905), 20 (1905-15), 22 (1919-87), 21 (1987/88), 20 (1988-91), 22 (1991-95), 20 (1995 em diante). Pontos por vitória: 2 até 1980/81 e 3 desde 1981/82, certo.
- **Falta 2025/26** (`EN-001`, alta): terminou em 24/05/2026, campeão Arsenal (14º título), vice Manchester City; rebaixados West Ham, Burnley e Wolverhampton. Com ela, o cartão de títulos e a Corrida mudam (Arsenal 14).
- **Campeões:** 126 de 126 iguais à lista da RSSSF. **Campeão, vice e 3º:** 126 de 126 iguais à tabela do 11v11 (378 posições). Corrida dos títulos: Manchester United e Liverpool 20, Arsenal 13, Manchester City 10, Everton 9... 24 campeões diferentes, certo.
- **Nomes de época:** o banco tem `nome_oficial` certo (Football League 1888/89-1891/92, Football League First Division 1892/93-1991/92, FA Premier League 1992/93-2006/07, Premier League 2007/08+), mas o painel mostra "Inglês" em todas (`EN-015`, baixa).
- Títulos controversos: não há na 1ª divisão inglesa.

## B. Classificação final

- **Todas as 126 temporadas, tabela inteira contra o 11v11** (`revisao/EN/cmp_11v11.py`): posição, J, V, E, D, GP, GC e pontos iguais em todas as linhas (2.583 clubes-temporada), menos estas:
  - 1888/89: Wolverhampton GP 50 (11v11 51) e Everton GC 46 (11v11 47), o jogo de `EN-006`;
  - 1956/57: Birmingham 12º e Chelsea 13º (média 1,000 os dois); o 11v11 inverte, a ordem oficial é a do painel (`EN-020`, nao-e-erro);
  - 1891/92, 1892/93 e 1905/06: o 11v11 separa um jogo do Stoke (e do Newton Heath) num clube à parte; somando, bate com o banco. Não é erro do painel.
- **Conferência interna** (`revisao/EN/interno.py`): a tabela do banco é igual à calculada dos jogos em todas as temporadas (com as punições); a ordem segue pontos, média de gols (até 1975/76) e saldo (depois); só 1956/57 foge, pela ordem oficial. A tabela do painel (`EDS.tab`) é igual ao banco.
- **Punições:** todas no banco e nos pontos do painel: 1890/91 Sunderland -2; 1990/91 Arsenal -2 e Manchester United -1; 1996/97 Middlesbrough -3; 2009/10 Portsmouth -9; 2023/24 Everton -8 e Nottingham Forest -4. O painel não avisa nem explica (`EN-010`, baixa).
- **Rebaixados:** 126 temporadas conferidas contra o artigo de cada temporada na Wikipédia en (`revisao/EN/rebaixados_wiki.py`, 111 automáticas e 15 olhadas à mão): todos certos, inclusive 1914/15 (só Tottenham; Chelsea ficou com a ampliação), 1938/39 (Birmingham e Leicester), 1986/87 (Charlton salvo nos play-offs), 1987/88 (Chelsea caiu nos play-offs) e as temporadas sem rebaixamento (1888/89, 1890/91, 1897/98, 1904/05). Stoke 1889/90 e Darwen 1891/92 não foram reeleitos: contar como "rebaixado" é decisão (`EN-018`, baixa).
- **Sub-aba Participantes:** em 1914/15 e 1938/39 a coluna "No ano seguinte" fica vazia e em 1946/47 a "Chegou" (1919/20 pela mesma regra) (o painel procura o ano ±1, que não existe por causa das guerras; `EN-008`, media). Nas outras, quem caiu aparece como "—", porque não há 2ª divisão no banco, embora a situação "rebaixado" esteja lá (`EN-009`, baixa).

## C. Jogos

- **Total:** 50.950 jogos, n×(n-1) em todas as 126 temporadas; nenhum confronto repetido ou faltando, nenhum sem placar ou data, nenhuma data fora da temporada. Varredura de tela (`revisao/EN/varredura.py`) e datas repetidas (`revisao/EN/datas_repetidas.py`): nada.
- **Placares, todos os jogos de todas as temporadas** contra a matriz da Wikipédia en (`revisao/EN/cmp_matriz_wiki.py`): 50.950 conferidos, 1 diferença: 1926/27 Arsenal x West Ham, Wikipédia 8-2, banco 2-2; a tabela do 11v11 fecha com 2-2, erro da Wikipédia (`EN-019`, nao-e-erro).
- **1888/89 Wolverhampton x Everton:** o banco tem 4-0 (escolha da coleta); 11v11, ogol, tabela da Wikipédia e as páginas da temporada dos dois clubes (5 autores de gol) dão 5-0 (`EN-006`, media).
- **Datas e placares, 31 temporadas inteiras (13.082 jogos: 1888/89, 1925/26, 1960/61, 2024/25 e as 27 em que a coleta viu data diferente no ogol)** contra as páginas de jogos por clube do 11v11 (`revisao/EN/cmp_datas_11v11.py`, saída em `revisao/EN/datas_11v11_saida.txt`): placares todos iguais (fora o 1888/89 acima); 33 datas erradas no banco, em que o 11v11 concorda com o ogol e não com a base: 1995/96 os 10 jogos da última rodada (04/05 no banco, foi domingo 05/05/1996) e West Ham x Manchester United (22/01/1996); 1899/00 9 jogos em 29/12/1899 (sexta; foi sábado 30/12); 1895/96 1; 1934/35 1; 1936/37 2; 1938/39 2; 1993/94 3; 1994/95 2; 1998/99 1; 2015/16 Manchester United x Bournemouth (17/05/2016). Nas outras 18 temporadas apontadas pela coleta o 11v11 confirma a data da base (o ogol é que erra) (`EN-005`, media).
- **Rodadas:** em 94 temporadas (1888/89-1991/92 e 1994/95) a rodada do ogol não é rodada: clubes com 2 ou 3 jogos na mesma rodada (`EN-007`, media; lista em `revisao/EN/rodadas_saida.txt`). Isso aparece na sub-aba Jogos (ex.: 1888/89 Rodada 22 com 12 jogos) e mexe na Corrida por rodada.
- Sem W.O., jogos anulados ou de tribunal no período.

## D. Gols e artilheiros

- **Artilheiro oficial, 126 temporadas, contra a RSSSF** (`revisao/EN/artilheiros.py`): 118 iguais e 4 só com grafia diferente (Southwarth, Steel, Davies, H.M. Son). Diferenças:
  - 1937/38: Lawton 34 no painel; são 28 (artigo da temporada, Everton 1937-38 e carreira do jogador; a RSSSF traz 38) (`EN-002`, media);
  - 1889/90: Jimmy Ross 22 x 24 (RSSSF e artigo da temporada) (`EN-003`, baixa);
  - 1905/06: Albert Shepherd 26 x Walter White 26 (RSSSF e artigo da temporada) (`EN-004`, baixa).
- **Gols com autor ≤ placar:** nenhum jogo com mais gols com autor que o placar, nenhum gol de clube que não jogou. 24.796 gols com autor (2001/02+). 12 jogos de 2002/03 a 2016/17 ficaram sem autores (ESPN descartada); por isso a artilharia calculada de 2014/15 dá Agüero 25 (oficial 26) (`EN-016`, baixa). Jogos: 2002/03 West Bromwich 1-0 Southampton, Sunderland 1-3 Charlton, Fulham 2-1 Aston Villa; 2003/04 Leeds 2-1 Manchester City; 2004/05 Tottenham 2-3 Charlton; 2006/07 West Ham 0-2 Wigan; 2010/11 Everton 1-4 West Bromwich; 2011/12 Everton 2-0 West Bromwich; 2013/14 Manchester City 4-1 Manchester United; 2014/15 Manchester City 1-0 Manchester United; 2016/17 Liverpool 2-2 West Ham, Stoke 1-1 Everton.
- Artilharia calculada x oficial, 2001/02-2024/25: igual em 23 de 24 (só 2014/15).

## E. Clubes e escudos

- 65 clubes, todos com um cadastro só; país certo (Cardiff e Swansea `WAL`, os outros `ENG`); cidades certas. Sem homônimos juntados: Accrington é o Accrington FC (1888-1893), Wimbledon o Wimbledon FC. Nomes repetidos em outros países (Liverpool, Arsenal) não colidem.
- Nomes de época juntados no clube certo: Small Heath = Birmingham, Woolwich Arsenal = Arsenal, The Wednesday = Sheffield Wednesday, Leicester Fosse = Leicester, Stoke = Stoke City, Glossop North End = Glossop. Falta "Newton Heath" no `clube_nome` do Manchester United, que o relatório de coleta diz ter (`EN-017`, baixa).
- **Escudos:** os 65, um a um, numa folha de contato (`SCRATCH/EN/folha_escudos.png`): todos certos (`EN-021`, nao-e-erro). Darwen usa o escudo do AFC Darwen (sucessor) e Accrington o brasão do Accrington FC.

## F. Painel, aba por aba

- **Números do painel x banco** (`revisao/EN/painel_x_banco.py`): pódio, jogos e gols de cada edição, maior goleada, pontos por vitória, Jogos e vitórias (65 clubes), participações: tudo igual. Cartões do topo certos (126 edições, 24 campeões, 65 clubes, 50.950 jogos, 151.493 gols).
- **Telas no site**, computador (1400 px) e celular (420 px): 39 rotas (História: as 7 sub-abas e as 4 partes de Curiosidades; Por campeonato: as 6 sub-abas em 1888/89 e 2024/25, Classificação de 1890/91, 1990/91 e 2023/24, Participantes de 1889/90, 1914/15, 1938/39, 1946/47 e 1987/88, Resumo de 1956/57 e de "1939/40", Corrida 2023/24; Por clube: as 5 sub-abas do Arsenal, Birmingham, Manchester United, Cardiff, Accrington). Sem erro nem tela quebrada. Prints em `SCRATCH/EN/telas/`.
- **Curiosidades conferidas:** maior goleada West Bromwich 12-0 Darwen (1891/92) e Nottingham Forest 12-0 Leicester (1908/09); fora Southampton 0-9 Leicester (2019/20); mais gols Aston Villa 12-2 Accrington (1891/92); empate Leicester 6-6 Arsenal (1929/30); Arsenal 99 temporadas seguidas; Bolton 73 sem título; Aston Villa 128 gols (1930/31); Liverpool 16 sofridos (1978/79); Derby 11 pontos (2007/08); Manchester City 4 títulos seguidos (2020/21-2023/24); Blackburn 81 anos de jejum; invictos Preston 1888/89 e Arsenal 2003/04; Manchester City 100 pontos. Todas certas.
- **Erros:**
  - "Título mais apertado", "Maior vantagem sobre o vice" e os aproveitamentos (Curiosidades e Campanhas) usam 3 pontos por vitória também até 1980/81 (`EN-011`, media);
  - "Títulos por estado" com uma linha "?" (`EN-012`) e texto do "Título mais apertado" saindo do cartão (`EN-013`), baixas;
  - celular mais largo que a tela, já conhecido (`EN-014`, baixa).
- A "Pontuação histórica" também usa 3 pontos por vitória, mas diz isso na legenda; não registrei.

## Perguntas ao Guilherme

1. **2025/26:** entra no `eng-1` (já terminou; Arsenal campeão)? O briefing desta revisão falava em 1888/89-2024/25 (`EN-001`).
2. **Stoke 1889/90 e Darwen 1891/92:** não foram reeleitos (não havia rebaixamento). Contam como "rebaixado"/"caiu" no painel? (`EN-018`)
3. **1888/89 Wolverhampton x Everton:** fica 4-0 (engsoccerdata e RSSSF) ou 5-0 (11v11, ogol, Wikipédia e páginas dos clubes)? (`EN-006`)
