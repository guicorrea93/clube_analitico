# Revisão: Brasileirão Série A (bra-serie-a)

Revisor: subagente SA · 20/11/2026 · scripts em `revisao/SA/`, páginas baixadas em `data/cache/revisao/SA/`.

**Resumo.** Placares, totais de jogos e campeões estão certos. O erro sério é na classificação de 2003+: punições e
decisões do STJD não entram (2003, 2004, 2005, 2013, 2018); em 2013 o Fluminense aparece na zona e a Portuguesa em 12º.
Há ainda o vice de 1968 (Robertão), artilharia ausente antes de 2003 e números da classificação antiga que somam jogos de desempate.
30 achados: 6 altos, 16 médios, 8 baixos (`SA-001` a `SA-030`).

## A. Edições e títulos

- **Lista de edições:** 70 (1937, Taça Brasil 1959–1968, Robertão 1967–1970, 1971–2025). Bate com a lista oficial
  (CBF: unificação de 2010 e reconhecimento de 1937 em 2023). 2026 ainda está em andamento. OK.
- **Campeão, vice e 3º:** 210 posições contra a lista da Wikipédia en (campeão, vice, 3º), conferidas também com as tabelas
  finais en/pt. 207 certas. Erros: **SA-007** (1968 Robertão: vice é o Internacional, 3º o Vasco; o painel põe Palmeiras vice)
  e **SA-008** (1992: 3º Vasco ou Bragantino; as fontes divergem).
- Contagem de títulos (Pódio por clube) bate com a CBF: Palmeiras 12, Santos 8, Flamengo 8, Corinthians 7 etc.
- Nomes de época: certos, menos 2000, chamado "Campeonato Brasileiro" em vez de Copa João Havelange (**SA-027**).
- Fontes: https://en.wikipedia.org/wiki/List_of_Brazilian_football_champions e as páginas de cada edição (en e pt).

## B. Classificação final

- **2003–2025 (todas as 23):** contra a tabela da Wikipédia en (módulo de classificação). 17 certas.
  Com erro: 2003 **SA-003**, 2004 **SA-002**, 2005 **SA-004**, 2013 **SA-001**, 2018 **SA-005** (punições e decisões do STJD
  não aplicadas, posições trocadas) e 2010 **SA-006** (só os pontos).
  Causa comum: o painel calcula `Pts = 3×V + E` sem ajuste, e a posição vem da última rodada do banco antigo.
  As diferenças de gols em 2006, 2008, 2012 e 2025 são erro da Wikipédia: a RSSSF confirma o painel.
- **1937–2002 (47 edições):** contra as tabelas finais da Wikipédia en (45 edições) e pt (44). Só registrei o que en e pt dizem
  igual e o painel diferente, ou o que tem prova no jogo:
  1972 (**SA-009**), 1979/1984 (**SA-017**), 1980/82/83/84 com jogos de desempate e repescagem somados (**SA-015**),
  1986 (**SA-016**), 1999 caso Sandro Hiroshi (**SA-014**) e a coluna Pts calculada (**SA-018**).
  Em 1990, 1993 e 2001 as fontes divergem entre si nos empates: não registrei.
- **Punições e tribunal:** 1972 (ABC x Botafogo), 1979, 1980, 1986 e 1991 estão aplicados no placar, com observação.
  1999 (Sandro Hiroshi), 2003, 2004, 2010, 2013 e 2018 não estão aplicados (achados acima).
  2005 (Máfia do Apito): os 11 jogos refeitos estão certos (o banco tem só os replays), mas sem aviso (**SA-024**).
- **Rebaixados, 2003–2025:** a sub-aba Participantes ("caiu para a Série B") bate com a Wikipédia en em todos os anos.
  A faixa da Corrida está errada em 2013 (dentro de SA-001), e as faixas de Libertadores e Sul-Americana são fixas (**SA-026**).

## C. Jogos

- **Total de jogos:** 21.468, igual entre o banco e o painel em todas as 70 edições. 2003–2025 batem com o formato de cada ano
  (2016 tem 379: Chapecoense x Atlético-MG não foi disputado, como na RSSSF).
  Antigas: as diferenças com as fontes vêm dos desempates contados (SA-015), do recorte de 1986 (SA-016) e de um jogo
  faltando em 1959 (**SA-013**).
- **Placares 2003–2025:** 7.771 jogos contra a matriz de resultados da Wikipédia en (2003, 2006, 2007 e 2009–2025) e
  1.394 contra a RSSSF (2004, 2005, 2008). Deram 26 diferenças. Em 24 delas o erro é da fonte: a RSSSF ou a tabela final
  confirmam o painel. As outras 2 são o mesmo erro, **SA-010** (2009, mando invertido em Flamengo x Botafogo).
- **Placares antigos:** 1979, edição antiga, 203 jogos (196 iguais; os outros 7 são erro da matriz en, confirmado pela RSSSF);
  1993, do meio, 58/58; Robertão 1967–1970, 29/30; 1987: a ida da final CBF está errada (**SA-011**).
  Prorrogação fora do placar em 2001 (**SA-012**).
- **W.O., anulados e tribunal:** nenhum jogo da Série A tem `resultado_especial` (**SA-024**). Datas de jogos remarcados
  de 1996–1998 só aparecem na observação (**SA-025**).
- Fontes: https://www.rsssf.org/tablesb/braz03.html … braz2025.html e as páginas da Wikipédia en de cada ano.

## D. Gols e artilheiros

- **Soma dos gols com autor ≤ placar:** conferido nos 21.468 jogos: 0 jogos acima do placar.
  De 2003 a 2025, os jogos têm todos os gols com autor; há 158 gols sem nome do jogador.
- **Artilheiro de cada edição:** 23 edições com dados (2003–2025): 20 certas.
  Erros: 2007 (**SA-021**), 2008 (**SA-020**) e 2016 (**SA-022**: o painel conta os gols por jogador e clube, e o Fred se divide).
  Há também nomes fora do padrão (**SA-023**).
  As 47 edições de 1937 a 2002 não têm artilharia (**SA-019**).
- Fonte: https://en.wikipedia.org/wiki/List_of_Brazilian_football_champions (coluna Top scorer) e o infobox das páginas pt.

## F. Painel

- Abri 19 rotas no Chrome sem janela (1400 px): as 7 sub-abas de História, as 6 de Por campeonato
  (anos 1937, 1959, 1968, 1987, 1999, 2008, 2013, 2016) e as 5 de Por clube. Também 4 rotas no celular (420 px).
  Nenhum erro de JavaScript em 14 rotas testadas com log.
- Os cards do topo batem com o banco (70 edições, 21.468 jogos, 53.238 gols, 161 participantes, 17 campeões).
  As curiosidades principais estão certas: 10×1 Corinthians x Tiradentes-PI (1983), 0×7 Bahia x Cruzeiro (2003),
  7×5 Ceará x River-PI (1962), 5×5 Portuguesa x Figueirense (2008).
- Achados: **SA-026** (faixas da Corrida), **SA-028** ("Copa Uniao" sem acento), **SA-029** ("mais edições seguidas"
  quebra nos anos com duas edições) e **SA-030** (celular mais largo que a tela, já conhecido).

## Perguntas ao Guilherme

1. **1987:** o painel segue a CBF (Sport campeão, com nota). Fica assim, ou mostra também o Flamengo (Copa União)?
2. **1967 e 1968:** contar dois campeões no ano (Taça Brasil e Robertão), como a CBF? Hoje o painel conta os dois.
3. **1992, 3º lugar:** Vasco (Wikipédia en) ou Bragantino (Wikipédia pt e painel)?
4. **Classificação antiga:** os números devem seguir a tabela oficial (sem desempates e repescagens) ou somar todos os
   jogos, como hoje? E a coluna Pts deve ser a pontuação oficial da época?
5. **Tribunal:** aplicar os resultados do tribunal nos jogos e na tabela, como em 1999 (Sandro Hiroshi), em 2016 (W.O. duplo
   na Wikipédia en, "não disputado" na RSSSF) e em 1986 (Joinville x Sergipe: 1-0 de W.O. ou 1-1)?

## 3ª rodada (22/11/2026)

Revisor QA. Foco: fontes que nenhuma etapa usou, conferidas por década contra o banco (`db/futebol.db`, só leitura). Scripts em `revisao/QA/`, páginas em `data/cache/revisao/QA/`, listas de datas em `revisao/QA/saida/`. O painel local e o publicado são iguais (mesmo md5 de `dados/bra-serie-a.js`).

**Fontes novas e amostra por década** (jogos casados; placar igual / data igual):

| Década | Fonte | Edições | Jogos | Placar | Data |
|---|---|---|---|---|---|
| 1930 | Campeões do Futebol | 1937 | 14 | 13 | 11 (os 4 erros são da fonte: a pt confirma o banco) |
| 1950 | Bola na Área | 1959 | 35 | 28 | 27 (erros do banco: QA-002) |
| 1960 | Campeões do Futebol; BNA | Robertão 1967; Taça 1960 | 133 | 133 | 133 |
| 1970 | Bola na Área | 1971, 1974, 1975, 1979 | 1.620 | 1.603 | 1.570 |
| 1980 | Bola na Área; Transfermarkt | 1980, 1984-1989 | 1.396; 1.114 | 1.370; 1.017* | 1.350; 1.040 |
| 1990 | Bola na Área; Transfermarkt | 1990-1999 | 1.538; 2.498 | 1.524; 2.493 | 1.294; 2.138 |
| 2000 | Transfermarkt; BNA | 2000, 2001, 2005, 2008 | 1.558; 1.224 | 1.556; 1.202 | 1.554; 1.192 |
| 2010 | Transfermarkt; BNA | 2015 | 380; 379 | 380; 379 | 380; 379 |
| 2020 | Transfermarkt; BNA | 2022 | 380; 379 | 380; 379 | 363; 369 |

\* o Transfermarkt soma os pênaltis ao placar nos 96 empates de 1988.

Cada diferença foi conferida: quase todas são erro da própria fonte (ou ida e volta trocadas). Viraram achado só as que duas fontes independentes confirmam:
- **QA-001** (média): 2001, Bahia 3x2 Ponte Preta e Fluminense 3x2 Ponte Preta (banco 3x1 e 2x1). Fecha a diferença de gols que sobrou no SA-012.
- **QA-002** (média): Taça Brasil 1959, Atlético-MG 2x1 Rio Branco-ES (103 gols na edição, banco 102), 3º jogo da final em 29/03/1960 (banco 03/03), desempate Ceará x ABC sem data e mando/data trocados em 6 jogos.
- **QA-003** (média): datas: 1995 com 89 jogos sem data (81 achadas), 1974 com 12; datas erradas em 1991 (18), 1999 (14), 1995 (12), 1988, 1993 e 1994. Com elas, o conflito de 1991 zera e os de 1999 caem de 7 para 4.
- **QA-004** (baixa): 1988, pênaltis dos 96 empates só na observação.
- SA-017 ganhou explicação: 1979 Central 0x1 Vasco; 1984 Portuguesa 0x1 Botafogo (BNA e tabelas en/pt). SA-009: a BNA dá a mesma ordem do banco (sugestão: `nao-e-erro`). SA-025: datas reais de 1996-1998 por TM + BNA.

**Buracos de cobertura (seção 4):** o banco não tem autores antes de 2003, nem público e árbitro em nenhum ano. As fichas do Transfermarkt têm autores completos desde 1985 (37 de 38 gols na amostra) e público e árbitro em 2015 e 2022 (antes, só em parte); o ogol tem autores e árbitro em parte dos anos 1970; a Bola na Área tem público em boa parte de 2008 e 2015. Custo e caminho em `fontes_QA.md` e `plano_QA.md` (scratchpad).

**Varredura de tela e datas repetidas** (`revisao/QA/varredura.py`, `datas_repetidas.py`): clube com 2 jogos no mesmo dia em 1963 (3), 1989 (2), 1991 (2), 1994 (4), 1997 (3) e 1999 (12); 1961 com fase fora de ordem e 1987 com semifinalistas em 5º e 6º (já conhecidos). 2008-2010 zeraram.

**Outras fontes testadas:** CBF (jogos só por API; súmula antiga dá 404), Futebol Interior (2006+ por API), Hemeroteca (só jogo a jogo, à mão), RSSSF Brasil (não respondeu em 22/11).

Entregas no scratchpad: `achados_QA.csv` (QA-001 a QA-012; 4 desta competição), `sugestoes_QA.csv` (SA-009, SA-016, SA-017, SA-025, CL-025, CL-029, TL-002), `fontes_QA.md`, `decisoes_QA.md` (QA-D3 e perguntas antigas de 1987, 1967/68 e 2016), `plano_QA.md`.
