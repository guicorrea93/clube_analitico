# Revisão: Campeonato Espanhol, 1ª divisão (esp-1)

Revisor ES, 21/11/2026 (2ª rodada). Conferido o painel publicado (https://clubeanalitico.pages.dev/?c=esp-1), o arquivo
`painel/dados/esp-1.js` (igual ao publicado, byte a byte) e o `db/futebol.db` (21/11, 09:24).

**Resumo.** Edições, campeões, vices, 3º lugares e a classificação final completa das 94 temporadas batem com a es.wikipedia (1.622 linhas de tabela; a única diferença real é o W.O. de 1979/80);
os 27.336 jogos foram comparados um a um com as matrizes de resultados da es.wikipedia e todas as diferenças são erro da própria Wikipédia.
Os problemas estão nas bordas: 1986/87 sem o triangular de rebaixamento (Racing rebaixado acima do Cádiz), Oviedo "rebaixado" em 1935/36 no banco, o W.O. de 1979/80 contado nos gols e dois cartões de Curiosidades que refazem os pontos com 3 por vitória (Athletic campeão com "-2 pontos à frente").

Achados: `ES-001` a `ES-020` (14 abertos: 1 alto, 4 médios e 9 baixos; mais 6 conferências que deram certo, como `nao-e-erro`).
Scripts em `revisao/ES/`, páginas em `data/cache/revisao/ES/`, prints e saídas em `SCRATCH/ES/`.

Fontes usadas (diferentes da base da coleta, que foi engsoccerdata, ogol, football-data, ESPN, RSSSF e en.wikipedia): **es.wikipedia**, uma página por
temporada ("Primera División de España AAAA-AA": ficha, tabela no Módulo Football/Sports table com `estado_X` e notas, e matriz de resultados),
"Trofeo Pichichi" e "Anexo:Estadísticas de la Primera División de España". en.wikipedia só para desempatar (1986/87 e recordes).
bdfutbol.com e worldfootball.net responderam 403; linguasport não resolve.

## A. Edições e títulos

- **Lista de edições:** 94, de 1928/29 a 2024/25, sem 1936/37-1938/39 (Guerra Civil). Igual à es.wikipedia. Temporadas como "1992/93". Ok.
- **Campeão, vice e 3º:** 94 de 94 certos (282 posições), pela tabela completa de cada temporada (bloco B). Títulos: Real Madrid 36, Barcelona 28,
  Atlético 11, Athletic 8, Valencia 6, Real Sociedad 2, Deportivo, Sevilla e Betis 1. Nenhum título controverso na liga espanhola.
- **Pontos por vitória:** 2 até 1994/95 e 3 de 1995/96 em diante, no banco e no painel ("Pontos por vitória" do Resumo). Ok.
- **Rebaixados (todas as temporadas)**, banco (`situacao`) x `estado_X = D` das tabelas da es.wikipedia (1959/60 e 1960/61 pela cor da tabela; 1986/87 pelo texto): 93 de 94 iguais, inclusive os casos de promoción
  (1965/66 CD Málaga 13º, 1989/90, 1992/93, 1993/94, 1997/98, 1998/99), 1994/95 (só o Logroñés; Valladolid e Albacete salvos pela ampliação para 22 no caso Celta/Sevilla)
  e 2014/15 (Elche 13º rebaixado por dívidas, Eibar 18º fica). Diferenças:
  - 1935/36: Real Oviedo (3º) marcado como rebaixado; ele teve dispensa e voltou em 1940/41 (`ES-001`).
  - 1986/87: o rebaixado (Racing) está certo, mas aparece em 17º, acima do Cádiz, que ficou (`ES-002`).
- **Corrida (faixa de rebaixamento):** pinta as últimas N posições, e não quem caiu, em 1965/66, 1989/90, 1993/94, 1997/98 e 2014/15 (`ES-004`).
- Fontes: https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_de_Espa%C3%B1a_1935-36 (e as demais temporadas); script `compara_podio_rebaixados.py` e `zonas_wiki.py`.

## B. Classificação final

- **Todas as 94 temporadas, tabela inteira** (posição, J, V, E, D, GP, GC e ajuste de pontos; 1.622 linhas), painel (`EDS.tab`) x es.wikipedia: 1.609 linhas iguais.
  Diferenças:
  - 1979/80: o painel soma os gols do W.O. CD Málaga 0-1 AD Almería (Almería 42 GP, Málaga 59 GC); a tabela oficial e o próprio banco têm 41 e 58 (`ES-003`).
  - 1979/80: a es.wikipedia ainda desconta 2 pontos do Salamanca, mas a nota dela diz que a sanção foi revogada em 1981. Painel certo (`ES-018`).
  - 2018/19: a es.wikipedia põe o Celta em 16º; o confronto direto dá o Valladolid. Painel certo (`ES-017`).
  - 1932/33, 1952/53 e 2006/07: erros da própria es.wikipedia (um gol a menos no 9-5, 28 jogos para o Racing, gols de 4 clubes); o painel fecha com os jogos e com a RSSSF.
- **Painel x banco:** `EDS.tab` igual a `classificacao_final` em todas as linhas, menos as duas do W.O. de 1979/80 (`ES-003`). Pódio do painel = banco nas 94.
- **Punições:** 1979/80 CD Málaga -3, 2003/04 Racing -1 e 2014/15 Almería -3 estão aplicadas (coluna Pts), mas sem nenhuma explicação no painel (`ES-011`).
- **Desempate:** como as 94 tabelas batem com a es.wikipedia, a ordem dos empatados em pontos está certa (inclusive 1954/55, 1969/70, 1972/73, 1981/82 e 1995/96, em que a coleta ficou com a ordem oficial).
- **1986/87:** duas fases (Liga e Fase final com 3 grupos), sem a coluna Pts (já explicado pelo agente 1). Falta o triangular de rebaixamento (`ES-002`).
- **Participantes:** 1935/36 e 2014/15 olhados na tela: estreias, "já estava", "ficou" e "—" coerentes. Sem a 2ª divisão no banco, quem subiu aparece como "—" (limitação conhecida).
- Script: `revisao/ES/compara_classificacao.py`, `revisao/ES/painel_x_banco.py`.

## C. Jogos

- **Total por temporada:** 94 de 94 iguais a n×(n−1) (1986/87: 306 + 90). Total 27.336. Nenhum jogo sem data, fora da temporada, repetido, nem clube com 2 jogos no mesmo dia ou na mesma rodada.
- **Placares: todos os 27.336 jogos** contra a matriz de resultados da es.wikipedia (todas as temporadas têm): 27.320 iguais. As 16 diferenças:
  - 11 jogos do Atlético em 1928/29, Oviedo 4-4 Valencia (1934/35), Atlético 1-0 Levante e Gimnàstic 1-3 Real Sociedad (2006/07): a matriz da es.wikipedia
    não fecha com a tabela dela; o banco fecha (`ES-016`);
  - Athletic 9-5 Racing (1932/33): a página da temporada traz 9-4, mas o anexo de estatísticas da es.wikipedia e a en.wikipedia confirmam 9-5 (`ES-015`);
  - CD Málaga 0-1 AD Almería (1979/80): W.O., sem placar na es.wikipedia. Ok.
- **Datas:** 12.324 jogos de 1993/94 a 2024/25 contra o football-data (que a coleta não usou para data): 12.230 iguais; 94 com um dia de diferença,
  68 deles em 1993/94. Conferido um: Barcelona 5-0 Real Madrid em 08/01/1994 (banco certo; o football-data diz 09/01).
- **W.O. e tribunal:** 1979/80 W.O. (0-1, `resultado_especial = wo`) e Málaga 0-3 Salamanca mantido (sanção revogada). Ok.
- Scripts: `compara_jogos.py`, `totais_datas.py`, `datas_footballdata.py`.

## D. Gols e artilheiros

- **Artilheiro (Pichichi), todas as 94 temporadas** contra a lista "Trofeo Pichichi" da es.wikipedia: 89 iguais (nome e gols, com os empates de 1957/58, 1968/69, 1969/70, 1970/71 e 1983/84).
  5 com número de gols diferente: 1929/30, 1934/35, 1935/36, 1954/55 e 2003/04 (`ES-005`). Em 1935/36 a es.wikipedia diz que o Marca dá 27 e a LFP 28; a coleta pôs 28 dizendo ser do Marca.
- **Gols com autor ≤ placar:** 27.336 jogos, nenhum com mais gols de autor que o placar. 24.048 gols com autor (2001/02+).
- **Nomes de jogadores:** nomes da ESPN de 2001 a 2008 fora de ordem e um jogador partido em dois (`ES-006`).
- **Painel:** a sub-aba Artilharia da edição mostra só o artilheiro oficial e esconde o ranking de gols por jogador (`ES-007`).
- Script: `compara_pichichi.py`.

## E. Clubes e escudos

- **63 clubes**, todos `ESP`, com cidade. Nenhum nome repetido com outro país (só "Barcelona de Ilhéus" parecido, que é outro clube). Nenhum duplicado dentro do esp-1.
- **Separações:** CD Málaga x Málaga, AD Almería x Almería, Burgos x Real Burgos: a es.wikipedia também separa (`ES-019`).
- **Nomes de época:** o painel mostra sempre o nome atual (Atlético Aviación, Atlético de Bilbao, Madrid FC, Español não aparecem); os nomes estão no `clube_nome` (`ES-013`, pergunta abaixo).
- **Atlético Tetuán** (1951/52) com país Espanha: o clube era do protetorado e filiado à federação espanhola. Ok.
- **Escudos:** folha de contato com os 63 (`SCRATCH/ES/folha.png`), todos olhados. Errados: CD Málaga (escudo do Málaga CF atual) e AD Almería (escudo da UD Almería) (`ES-012`). Os outros 61 conferem.

## F. Painel, aba por aba

- **Site x arquivo local:** `dados/esp-1.js` publicado é igual ao `painel/dados/esp-1.js`.
- **Varredura de tela** (`revisao/ES/varredura.py` e `datas_repetidas.py`): nada encontrado (sem clube contra ele mesmo, jogo repetido, posição repetida, campeão fora do 1º).
- **Telas abertas no site** (1400 px): História (as 7 sub-abas), Por campeonato (as 6 sub-abas em 1935/36, 1986/87 e 2014/15, mais 2003/04 e 2024/25), Por clube (Resumo do Real Oviedo, Campanhas do Atlético, Confrontos do Real Madrid, Jogos do CD Málaga, Artilharia do Alavés) e as 4 partes de Curiosidades. Celular (420 px): História, Pódio, Classificação, Jogos e Por clube.
- **Números conferidos com a es.wikipedia:** 94 edições, 9 campeões, 63 clubes; Real Madrid 1.846 vitórias, Athletic 731 empates, Espanyol 1.170 derrotas;
  Barcelona 6.579 e Real Madrid 6.561 gols; participações (Valencia 90, Espanyol e Atlético 88); maior goleada Athletic 12-1 Barcelona (1930/31);
  jogo com mais gols 9-5 (1932/33); 100 pontos (Real Madrid 2011/12); campeões invictos 1929/30 e 1931/32. Todos certos.
- **Erros:** "Título mais apertado: Athletic -2 pontos à frente" (`ES-008`), "Maior vantagem: 21 pontos" em 1962/63 (`ES-009`), cartão "Títulos por estado" com "?" (`ES-010`),
  punições sem nota (`ES-011`), anos de início nos textos (`ES-014`, já conhecido).
- **Celular:** o Chrome sem janela não desce de 504 px; medido, a página não transborda nessa largura (`ES-020`). O corte que aparece nos prints de 420 px é do Chrome, não do painel.

## Perguntas ao Guilherme

1. **1935/36, Atlético de Madrid (11º):** caiu em campo e voltou na repescagem com o Osasuna pela vaga do Oviedo (1939). Marcar como rebaixado (como um perdedor de promoción ao contrário) ou não? O Oviedo, com certeza, não caiu (`ES-001`).
2. **1986/87:** pôr o triangular de rebaixamento (3 jogos entre Osasuna, Cádiz e Racing) como uma fase da edição, com a ordem final Osasuna, Cádiz e Racing (`ES-002`)?
3. **Artilheiros:** quando o Marca e a LFP discordam (1929/30, 1934/35, 1935/36, 1954/55, 2003/04), qual contagem vale (`ES-005`)?
4. **Nomes de época:** mostrar o nome da época (ex.: "Atlético Aviación" nos títulos de 1939/40 e 1940/41) ou manter sempre o nome atual (`ES-013`)?

## 3ª rodada (22/11/2026)

Revisor QE. Fonte nova principal: **BDFutbol** (bdfutbol.com), que nem a coleta nem as revisões usaram; terceira opinião pelo
transfermarkt (ES1) e pelo ogol. Scripts em `revisao/QE/`, páginas em `data/cache/revisao/QE/`.

- **Placares e datas, todas as décadas, todos os jogos:** os 27.716 jogos das 95 temporadas (inclusive 2025/26) contra a
  página de cada temporada do BDFutbol (`revisao/QE/cmp_bdfutbol.py esp`): placar igual em 27.714 (1932/33 9-5 x 9-4, já visto
  no ES-015, e o jogo anulado de 1979/80) e data igual em 27.693. Nas 23 datas diferentes, a terceira opinião (ogol,
  transfermarkt) confirma o pacote em 19; erro do pacote: 2003/04 Barcelona x Sevilla, jogado à 00:05 de 03/09/2003 (`QE-003`);
  2 jogos suspensos e completados noutro dia, sem observação (`QE-004`); 1 dividido (1932/33 Alavés x Betis).
- **Classificação final x BDFutbol:** 1.614 de 1.624 linhas iguais (fora 1986/87). Única diferença real: **1960/61, 6º e 7º**
  (`QE-002`): RSSSF e BDFutbol dão Athletic 6º e Betis 7º; o painel segue a Wikipédia (Betis 6º).
- **Desempate (o DE-002 do Alemão):** o confronto direto é a regra espanhola desde 1928/29 (class_rules da Wikipédia en em
  todas as temporadas; nos dados, em 1930/31, 1931/32, 1933/34, 1934/35... só ele reproduz a ordem). Mas a coleta usa um
  confronto sem a volta entre os que seguem empatados: em 1963/64 escolheu "média de gols" por coincidência e em 1954/55,
  1969/70, 1972/73, 1981/82 e 1995/96 nenhum critério fechava (a última rodada da Corrida difere da Classificação). O confronto
  recursivo reproduz 92 das 93 temporadas de fase única (todas menos 1960/61, o `QE-002`). E na Corrida o confronto entra com só
  um dos dois jogos disputados: 11.351 posições de rodada mudam com a regra da liga (confronto só depois dos dois jogos), 202 com
  troca de líder (`QE-001`, código de referência em `revisao/QE/desempate_esp.py`).
- **2025/26 (entrou depois da 2ª rodada):** pacote, banco e painel local certos (campeão Barcelona, vice Real Madrid;
  rebaixados Mallorca, Girona e Real Oviedo; Mbappé 25; 380 jogos e a tabela inteira iguais ao BDFutbol; 1.024 gols, todos com
  autor). O site ainda tem 94 edições (`QE-009`, `nao-e-erro`: falta publicar).
- **Fichas de jogo (amostra por década, 34 fichas, `revisao/QE/amostra_fichas.py`):** todas com autores e minuto desde
  1928/29, somando o placar (34 de 34); de 2001/02 em diante, 52 de 55 autores iguais aos da ESPN (o resto é grafia e um gol
  contra de Ximo Navarro que a ESPN dá a Franco Cervi, Celta 4-0 Alavés, 2021/22). Árbitro em 100% dos jogos de todas as
  décadas (o pacote tem 0%); estádio de época em todos. Sem público.
- **Outros:** observações da classificação em inglês (13 linhas; `QE-007`). Varredura de tela (`revisao/QE/varredura.py`):
  nada. Sugestões prontas para ES-011, ES-012 e ES-013 (`SCRATCH/sugestoes_QE.csv`); o escudo certo do CD Málaga e da AD
  Almería está no BDFutbol.
- **Buracos de cobertura e caminho:** árbitro e estádio, em lote, pelas 95 páginas do BDFutbol (já baixadas); autores antes
  de 2001/02 pela ficha do BDFutbol ou do transfermarkt (~19.700 páginas, ~11 h cada); cartões antigos só no transfermarkt;
  público antes de 2000: nenhuma fonte testada tem.
- Achados novos: `QE-001` (média), `QE-002` (alta, no ar), `QE-003` (média), `QE-004` (baixa), `QE-007` (baixa), `QE-009`
  (`nao-e-erro`), `QE-010` (`nao-e-erro`). Pergunta ao Guilherme: ordem de 1960/61 (`QE-002`) e ES-013 (nome de época).
