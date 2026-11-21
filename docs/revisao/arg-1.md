# Revisão: Campeonato Argentino, 1ª divisão (arg-1)

Revisor: AR · 21/11/2026 · achados em `SCRATCH/achados_AR.csv` (AR-001 a AR-044) · scripts e saídas em `revisao/AR/`

**Resumo.** As 196 edições batem com a lista da AFA (Wikipédia es e en), e o campeão está certo nas 196 no banco. No painel, o de 1913 Federación sai errado (AR-001).
O vice está errado em 12 edições, quase todas do amadorismo: tabelas calculadas sem os W.O., com jogos anulados ou com jogos faltando. Fora do amadorismo: 1976 Nacional, 1987/88, 1989/90 e 2008/09 Apertura.
O problema mais largo são as datas: ~3.920 jogos de 26 edições têm o ano errado (2018/19 inteiro, 1931 Liga, 1937...). Os placares conferidos estão 100% certos.
Achados: 14 altos, 16 médios e 14 baixos.

Fontes de conferência: Wikipédia es (artigo "Primera División de Argentina", páginas de cada temporada, "Anexo:Goleadores...") e en ("List of Argentine football champions", "List of Argentine Primera División top scorers").
A coleta usou RSSSF, ogol e ESPN. A RSSSF só foi lida para entender a origem de um erro (linhas citadas). Páginas guardadas em `data/cache/revisao/AR/`.

## A. Edições e títulos
- **Conferido:** a lista das 196 edições e o campeão, o vice e o 3º de cada uma, contra a lista da AFA na Wikipédia es. As diferenças foram confirmadas na en. Script: `revisao/AR/cmp_campeoes.py`.
- **Lista de edições:** as 196 batem com a es, inclusive 1936 (3 títulos), Metropolitano/Nacional, Apertura/Clausura, Inicial/Final/Campeonato 2012/13 e 2025 Liga.
  - As Copas de la Liga (2020-2024) ficam de fora, como na es e na en.
  - Falta o Apertura 2026, que já terminou (Belgrano campeão) → AR-043 (pergunta).
- **Campeões:** 196 de 196 certos no banco. Na en, Boca tem 36 títulos porque conta a Liga 2026.
  - No painel, 1913 Federación mostra Estudiantes de Buenos Aires em vez de Estudiantes (LP). Os jogos da FAF foram gravados com o clube errado → AR-001.
  - Por isso o cartão mostra "29 campeões" (são 28) e Estudiantes aparece com 6 títulos (são 7).
- **Vices:** 184 de 196 certos. Erram 1895, 1896, 1912 Asociación, 1913 Federación, 1919 Asociación, 1919 Amateurs, 1926 Asociación, 1926 Amateurs, 1976 Nacional, 1987/88, 1989/90 e 2008/09 Apertura → AR-002 a AR-013.
- **3º lugar:** 181 de 196 certos, contando os casos acima. Erram ainda 1997/98 Apertura (falta River 1-3 Rosario Central), 1974 Nacional e 1929 → AR-014 e AR-015.
- **1891:** o banco tem só o Saint Andrew's (lista da AFA); es e en listam o título dividido com o Old Caledonians → AR-044 (pergunta).

## B. Classificação final
- **Conferido:** tabela completa (posição, J, V, E, D, GP, GC) de 26 edições contra as páginas de temporada da es. Há pelo menos uma por década: 1895, 1896, 1908, 1912 As., 1913 Fed., 1919 As./Am., 1926 As./Am., 1929, 1931 Liga, 1937, 1949, 1955, 1965, 1975 Met., 1987/88, 1989/90, 1997/98 Ap., 2008/09 Ap., 2016/17, 2023 e 2025 Liga.
  - Resultado: 220 de 388 linhas lidas iguais. 1895, 1896 e 1913 Federación foram conferidas à mão e estão erradas.
  - Iguais por inteiro: 1937, 1955 e 2023, e 2025 Liga nas 26 linhas lidas. Saída: `revisao/AR/cmp_tabelas_es_saida.txt`.
- **Causas no amadorismo:** a tabela é calculada dos jogos, sem os pontos dados por W.O., com jogos anulados somados ou com jogos faltando → AR-020.
  - 1926 Amateurs tem só 43 dos 325 jogos → AR-006.
- **Outras:**
  - 1949: há um jogo "Gimnasia x Gimnasia" e os desempates entram na tabela. Lanús, o rebaixado, fica em 16º → AR-016.
  - 1988/89: a regra de pontos dos pênaltis não foi aplicada → AR-017.
  - 2016/17: faltam 4 jogos → AR-018.
  - 1975 Metropolitano: dois placares com 1 gol a menos → AR-019.
  - 1989/90: faltam as punições → AR-004.
- **Pontos por vitória:** 2 até 1994/95 e 3 desde 1995/96: certo. A exceção é 1988/89 (AR-017).
- **Punições:** 20 punições gravadas, vindas das tabelas da RSSSF (1941 Banfield, 1948 Racing, 1958 River, 1972 Banfield...). Faltam as de 1989/90.
- **Rebaixamento:** a situação "rebaixado" só aparece em 19 edições (AR-021). A sub-aba Participantes ("no ano seguinte") está certa no 2010/11 Clausura, conferido com River, Huracán, Quilmes e Gimnasia.

## C. Jogos
- **Placares:** 1.506 jogos de 7 edições contra os resultados das páginas es: 1896 (20), 1997/98 Apertura (169), 2008/09 Apertura (171), 2016/17 (445), 2018/19 (323) e 2023 (378). Os 1.506 placares estão certos. Script: `revisao/AR/cmp_jogos_es.py`.
- **Jogos faltando:** River 1-3 Rosario Central (1997/98 Apertura) e 4 jogos de 2016/17, confirmados na es. Também faltam jogos em 1926 Amateurs (38 de 325 com placar) e em 1926 Asociación (121 de 153).
- **Total de jogos das 196 edições:** conferido com o esperado da coleta e com o J das tabelas es. Diferenças: as citadas acima e os casos de AR-006, AR-007 e AR-013.
- **Datas (o maior problema):**
  - ~3.920 jogos de 26 edições têm o ano errado → AR-022. Lista em `revisao/AR/datas_ano_lista.txt`; prova pelo dia da semana em `revisao/AR/datas_semana_saida.txt`.
    - A causa é a virada de ano na leitura da RSSSF: um jogo adiado ou uma data com ano explícito ("11 Feb 1939" em 1937) empurra o ano de todos os jogos seguintes.
  - ~40 edições têm datas copiadas de outro jogo: ida e volta no mesmo dia, rodadas inteiras numa data → AR-023.
  - Há 5 datas que não existem: 2005-09-31 e 2021-02-29 → AR-024.
  - Dia e mês batem em 1.422 de 1.506 jogos; a maioria das diferenças é ruído de leitura.
- **Fases:**
  - "Desempate do título" está errado em 1931 Asociación (o campeonato inteiro), 1937, 1939, 1976 Nacional e 1979 Metropolitano; o desempate de 1923 está dentro da "Fase única" → AR-025.
  - A fase "Final" tem jogos de outras disputas em 1929, 1970 Nacional e 1979 Metropolitano → AR-026.
- **W.O., anulados e tribunal:** 391 W.O., 51 decididos no tribunal, 102 suspensos e 165 não jogados, todos com a observação da fonte, menos 1 dos não jogados. Amostra lida no relatório da coleta: os tipos batem com o texto da RSSSF.

## D. Gols e artilheiros
- **Artilheiros:** 189 edições conferidas, 171 com a en e 18 com a es. Script: `revisao/AR/cmp_artilheiros.py`.
  - Diferenças reais: 1894, 1934 Asociación, 2025 Apertura, 1932 Asociación e 1997/98 Clausura → AR-027 a AR-029. As outras diferenças da en foram desempatadas pela es e o banco está certo.
  - Faltam os artilheiros de 1936 (Copa de Honor e Campeonato) e de 1988/89 → AR-030.
- **Gols com autor ≤ placar:** 34.264 gols com autor; nenhum jogo passa do placar. Certo.

## E. Clubes e escudos
- **Conferido:** os 170 clubes do arg-1, olhando nome, país, província, cidade, nomes da fonte e participações. Todos são ARG. Os homônimos levam a cidade (Racing de Córdoba, San Martín de Tucumán...).
- **Duplicado:** "Atlético Cipolletti" (1985) é o Cipolletti → AR-031.
- **Para decidir:** o Quilmes de 1893-1895 junto com o Quilmes atual (AR-032) e as fusões de 1934 (AR-033).
- **Nomes colados** no `nomes_fonte` de 1926 → AR-034.
- **Escudos:** folha de contato com todos os clubes (`revisao/AR/folha_escudos.py`, print em `SCRATCH/AR/folha_escudos.png`).
  - Os 56 clubes com escudo estão certos.
  - Faltam 114. Uns 40 são da era do ogol, como Gimnasia de Jujuy (28 edições) → AR-035.

## F. Painel
- **Telas no site** (https://clubeanalitico.pages.dev/?c=arg-1), prints em `SCRATCH/AR/telas/`:
  - História: as 7 sub-abas.
  - Por campeonato: as 6 sub-abas, em 1913 Fed., 1926 Am., 1976 Nac., 2010/11 Cl., 2018/19, 2023, 2025 Ap. e 2025 Liga.
  - Por clube: as 5 sub-abas (River, Estudiantes, Boca, Independiente).
  - Celular (420 px): 5 telas.
  - Nenhum erro de JavaScript em 6 rotas.
- **Site x local:** os dados são iguais, menos o selo, o título e a bandeira, que só estão no local → AR-039.
- **Números do painel x banco:**
  - Os cartões estão certos: 196 edições, 42.546 jogos com placar, 120.669 gols. A exceção é "29 campeões" (AR-001).
  - O pódio do painel bate com o banco em 195 de 196 edições.
  - A tabela de classificação do painel difere da do banco em 71 edições: o painel tira os W.O. e soma os desempates → AR-036.
- **Outros:**
  - O "maior artilheiro" de cada clube conta só os gols com autor. O do River sai "Más 45" → AR-037.
  - Por clube > Jogos abre vazio na 2025 Liga → AR-038.
  - No celular, a página fica mais larga que a tela (já conhecido) → AR-040.
  - Os selos mostram só o ano de início (já conhecido) e o nome da época não aparece → AR-041.
  - Os cartões da 2025 Liga mostram "0 jogos" → AR-042.
- **Varredura de tela:** `revisao/AR/varredura.py` e `datas_repetidas.py`, com saídas em `revisao/AR/*_saida.txt`. Achados: vice que não jogou a final (1976 Nacional), "Final" com jogos demais, fases fora de ordem, clube contra ele mesmo (1949), jogos repetidos (1896) e clube com 2 jogos no mesmo dia.

## Perguntas ao Guilherme
1. **1891:** título só do Saint Andrew's (lista da AFA) ou dividido com o Old Caledonians (decisão da liga da época, como na es e na en)? (AR-044)
2. **Apertura 2026** (Belgrano campeão, já terminado): entra agora ou só quando a temporada 2026 fechar? (AR-043)
3. **Quilmes 1893-1895** (Quilmes Club / Quilmes Rovers): é o mesmo Quilmes de hoje? A es diz que os historiadores os tratam como clubes diferentes. (AR-032)
4. **Fusões de 1934:** Atlanta+Argentinos entrou como "Argentinos Juniors" e Talleres+Lanús como clube à parte. Manter assim ou tratar as duas igual? (AR-033)
5. **Títulos de 1936** (Copa de Honor e Copa de Oro, reconhecidos pela AFA em 2013; a en registra que historiadores contestam a Copa de Oro): manter os dois, como está?
