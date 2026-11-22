# Plano de correção — coleta Europa

Para: agente de coleta Europa. Revisão profunda de 22/11/2026.
Competições: Italiano (`ita-1`), Espanhol (`esp-1`), Inglês (`eng-1`), Alemão (`ger-1`), Francês (`fra-1`) e
Português (`por-1`).

## Como usar

1. Só comece quando o Guilherme mandar corrigir. Hoje a prioridade dele é coletar (`sco-1`, eras antigas de
   `ned-1` e `ger-1`, `bel-1`, `tur-1`).
2. Corrija na ordem: primeiro "ERRADO NO AR", depois cada competição de cima para baixo.
3. Cada linha é um resumo. A sugestão completa está no `docs/revisao/achados.csv`, coluna `o_que_a_fonte_diz`,
   depois de "SUGESTÃO:".
4. Ids marcados "espera D-xx": o Guilherme respondeu em 22/11 (todas menos a D-10). Corrija pela resposta registrada
   em `docs/revisao/decisoes-guilherme.md` (seção "Respostas do Guilherme").
5. Identifique jogos por competição + data + clubes, nunca pelo `partida_id`.
6. Depois de cada liga: `python coleta/<slug>/importar.py`, `python coleta/comum-europa/testar_carga.py <slug> <scratch>`,
   `python coleta/comum-europa/documentar.py` (a ficha em `documentacao/` é gerada: não editar à mão).
7. No fim: escreva os ids corrigidos em `docs/coleta/pedidos-europa.md` e rode as varreduras
   `python -I revisao/tela/varredura.py` e `python -I revisao/tela/datas_repetidas.py` (copie e troque a lista de
   competições). O agente 1 recarrega o banco e publica.

## ERRADO NO AR (altos já visíveis no site)

> **Atualização de 22/11:** o Português (`por-1`) foi publicado às 11:18 (commit fed171c). Entram no ar: PT-003 (vice de
> 1944/45) e PT-004 (Braga x Benfica 1986/87, que espera a decisão D-20).


- IT-002 (alta, `ita-1`): 1947/48, Napoli em 18º; foi declassado para o último lugar (21º).
- QE-002 (alta, `esp-1`, espera D-19): 1960/61, Betis 6º e Athletic 7º; pela regra das outras temporadas é o contrário.

Só no banco (a tela não mostra a marca "rebaixado"): IT-001.
O Francês e o Português não estão no site.

## Italiano (`ita-1`) — 15 ids

### `coleta/ita-1/importar.py` — classificação e rebaixados (custo baixo)
- IT-002 (alta): dicionário DECLASSADOS; Napoli 21º com observação.
- IT-001 (alta): NAO_REBAIXADOS 1945/46 (fusão na Sampdoria; clubes da Serie B no torneio misto).
- IT-016 (baixa): 1945/46, números do grupo final para os 8 finalistas.
- IT-012 (baixa, espera D-18): READMITIDOS com observação (1942/43, 1954/55, 2005/06).
- IT-014 (baixa, espera D-19): ordem da Wikipédia it em 7 temporadas (`revisao/IT/inversoes.py`).

### `coleta/ita-1/importar.py` — placares (TRIBUNAL e CORRECOES)
- IT-003 (média): 1929/30 Cremonese x Milan 0-2 awd (campo 0-3).
- IT-004 (média): 1930/31 Legnano x Lazio 0-2 awd (campo 0-1).
- IT-005 (média): 1963/64 Bari x Genoa 0-2 awd (campo 1-2).
- IT-006 (média): 1952/53 Torino 3-1 Palermo.
- IT-007 (média): 1962/63 Napoli 3-1 Palermo.
- IT-010 (baixa): marcar awd nos 31 jogos "a tavolino" (`revisao/IT/tavolino_sem_awd.txt`).
  Em IT-003 a IT-007, tirar de EXPLICACOES a frase "a Wikipédia erra gols".

### `coleta/ita-1/importar.py` — datas (maior volume)
- IT-008 (média): 622 datas de `revisao/IT/datas_corrigir.csv`, aplicadas em `carregar_base` (e em `reparar` em 1947/48).
  O ogol não serve para conferir data (repete a base).
- IT-009 (média): 1945/46 (14 jogos) e 2001/02 Brescia x Lecce, pelo mesmo mecanismo.

### Decididos em 22/11 (antes esperavam decisão)
- IT-017 (baixa, espera D-05): campeonatos de 1898 a 1928/29.
- IT-018 (baixa, espera D-04): jogos-desempate (spareggi).

## Espanhol (`esp-1`) — 4 ids (mais o QE-007, que é das duas ligas)

### `coleta/esp-1/importar.py` (um reimport só)
- QE-002 (alta, espera D-19): 1960/61 Athletic 6º, Betis 7º (sai sozinho com o QE-001).
- QE-001 (média): `ordenar()` com confronto direto recursivo + saldo entre empatados; função pronta em
  `revisao/QE/desempate_esp.py`. Muda a Corrida em 95 temporadas.
- QE-003 (média): DATAS, 2003/04 Barcelona x Sevilla em 2003-09-03 (00:05).
- QE-004 (baixa): observação dos 2 jogos suspensos e completados noutro dia (2004/05, 2023/24).

## Inglês (`eng-1`) — 6 ids

### `coleta/eng-1/importar.py`
- QE-005 (média): DATAS, 1953/54 Sheffield Wednesday x Aston Villa em 1953-11-07.
- EN-016 (baixa): GOLS_MANUAIS para 12 jogos sem autor (fichas do BDFutbol; lista no achado).
- QE-006 (baixa): árbitro com o nome completo do BDFutbol.
- EN-004 (baixa, espera D-17): artilheiro de 1905/06.

### `coleta/comum-europa/`
- RC-004 (baixa): levar o NOMES_ESPN do `esp-1` para `espn.py` ("Fernando Morientes", "Sávio"); reimportar eng-1 e fra-1.
- QE-007 (baixa): observações da classificação em inglês (18 no eng-1, 13 no esp-1): traduzir em `wiki_tabela.py`.

## Alemão (`ger-1`) — 14 ids

Nenhum alto. Campeões, vices e rebaixados certos nas 63 temporadas.

### `coleta/ger-1/importar.py` (um commit só)
- DE-003 (média): DATAS com 102 jogos de `revisao/DE/datas_corrigir.csv` (transfermarkt + RSSSF).
- DE-002 (média): critério fixo por época ("média" até 1968/69, "saldo" depois). Muda a Corrida em 15 temporadas.
  Olhar o mesmo vício em esp-1, fra-1, ita-1, ned-1 e por-1.
- DE-001 (média): PUNICOES, Arminia 1971/72 com 0 pontos (-19).
- DE-005 (baixa): awd e placar de campo em 5 jogos de tribunal.
- DE-006 (baixa): nota dos rebaixamentos fora de campo (1964/65, 1971/72, 1994/95).
- DE-007 (baixa): observações em português, sem o "S04".
- DE-008 (baixa): NOMES_ARTILHEIRO (8 nomes da Wikipédia de).
- DE-009 (baixa): NOMES_ESPN + `nome_espn()` (pares em `revisao/DE/nomes_espn.txt`).
- DE-004 (baixa): 3 datas em dúvida: conferir na ficha do transfermarkt antes de mexer.
- DE-012 (baixa, espera D-04): nota da Relegation (28 temporadas).
- DE-013 (baixa, espera D-19): 3º dividido em 1979/80.

### `coleta/ger-1/baixar.py` + `importar.py` (cobertura, quando o Guilherme mandar)
- DE-011 (baixa): autores de 1963/64 a 1998/99 pelos parênteses da RSSSF (já baixada); 1999-2001 pelo transfermarkt.
- DE-010 (baixa): 36 jogos sem autor, pela ficha do transfermarkt.

### Era antiga (já decidida em 22/11)
- DE-014 (baixa): o Guilherme decidiu incluir 1902/03 a 1962/63 no `ger-1`, com os títulos oficiais
  (`coleta/comum-europa/COMECE-AQUI.md`, seção 1.1). Está na fila de coleta, depois da `sco-1`. Com isso o achado fecha.
  A DDR-Oberliga e as Oberligas regionais esperam D-05.

## Francês (`fra-1`) — 22 ids

Não está no site. Corrigir antes de publicar.

### `coleta/fra-1/importar.py`
1. Altos (custo baixo)
   - FR-001 (alta): `prox_clubes` com `clube_ogol()`; FUSOES 1938/39 e 1966/67. Antibes e RC Roubaix esperam D-18.
   - FR-002 (alta): BONUS por época (1973 "gols"; 1974 e 1975 "diferença"); somem 39 punições falsas.
   - FR-003 (alta): TRIBUNAL 1951/52 OM x Racing (0-0 "v"; campo 2-3).
   - FR-004 (alta): TRIBUNAL 1955/56 Nancy x OM (0-0 "v"; campo 2-4).
   - FR-005 (alta): 1946/47, `reparar()` fica com o placar da base e a data do ogol.
2. Placares e pontos
   - FR-006 (média): VA-OM 1992/93, derrota para os dois.
   - FR-008 (média): tirar a correção de 1958/59 (Sochaux 4-3 Rennes).
   - FR-007 (média): 1947/48 Racing 5-1 Stade Français e Stade Français 1-0 Racing.
   - FR-010 (média): Le Havre 2008/09 sem a punição que só a RSSSF tem.
3. Datas
   - FR-009 (média): DATAS com os 41 jogos de 3+ dias; os 99 de 1-2 dias só depois de conferir num jornal.
4. Artilheiros
   - FR-011 (média): incluir Onnis (1979/80) e Garande (1983/84); Bokšić espera D-17.
   - FR-019 (baixa): nomes usuais da Wikipédia fr.
5. Textos e observações
   - FR-014 (baixa): observação da classificação só com a nota, em português.
   - FR-015 (baixa): ADMINISTRATIVOS (1990/91, 1993/94, 2000/01, 2016/17).
   - FR-016 (baixa): texto do tribunal com o placar dado e o de campo.
   - FR-020 (baixa): observação do Antibes em 1932/33.
   - FR-022 (baixa): docstring e relatório: o football-data não traz árbitro.
6. Critério e dúvidas
   - FR-018 (baixa): critério de desempate por época (achar quando a FFF trocou média por saldo).
   - FR-017 (baixa): 4 dúvidas (1935/36, 1937/38, 1945/46, 1950/51): só anotar até ver a Gallica.

### `coleta/comum-europa/clubes_fra.py`
- FR-021 (baixa): "Évian".
- FR-012 (média, espera D-24): Toulouse FC (1937) separado.
- FR-013 (baixa, espera D-24): Lyon OU e SO Montpellier.

## Português (`por-1`) — 19 ids

Não está no site. O pacote já está no banco local.

### `coleta/comum-europa/clubes_por.py`
- ~~PT-001~~ CORRIGIDO (reconferido em 22/11): o pacote tem "AD Sanjoanense" e o `por-1` carregou no banco (22/11).
  A revisão confere e fecha.
- PT-017 (baixa, espera D-24): Estrela da Amadora.
- PT-018 (baixa, espera D-24): SL Elvas e O Elvas.

### `coleta/por-1/importar.py` — ordem e pontos
- PT-003 (alta): 1944/45 com a ordem da RSSSF (vice Sporting).
- PT-004 (alta, espera D-20): 1986/87 Braga x Benfica, derrota para os dois.
- PT-005 (média, espera D-19): 2005/06 Naval 13º.
- PT-006 (média, espera D-20): Porto 2007/08, 75 pontos com observação.

### `coleta/por-1/importar.py` — placares
- PT-002 (média): tirar a correção de 1994/95 (Benfica 1-2 Sporting).
- PT-007 (média): 1980/81 Benfica 2-1 Espinho e Espinho 2-0 Benfica.
- PT-009 (baixa): 1974/75 CUF x Vitória de Setúbal: abrir a ficha do ogol e corrigir o motivo.

### `coleta/por-1/importar.py` — artilheiros e datas
- PT-012 (média): Seferović 2018/19 = 23.
- PT-013 (baixa): tirar o "\x96" do nome do Luis Suárez.
- PT-010 (média): DATAS para 5 datas impossíveis (1938/39, 1939/40, 1979/80, 1993/94, 1997/98).
- PT-011 (baixa): 26 datas pelo football-data + transfermarkt (`revisao/PT/datas_divergentes.txt`).

### `coleta/por-1/importar.py` — textos
- PT-016 (baixa): explicar rebaixamentos fora da zona (1950/51, 1961/62, 1973/74, 1997/98 Leça, 2005/06, 2008/09, 2019/20).
- PT-014 (baixa): tirar os códigos crus ("PAÇ", "BRA") da observação.
- PT-015 (baixa): observações próprias em português no lugar do inglês.

### `coleta/por-1/baixar.py` + `importar.py` (cobertura)
- PT-019 (baixa): autores de 1999/00 a 2005/06 pelas páginas `portNN.html` da RSSSF (7 páginas, em lote).
- PT-020 (baixa): árbitro e público pelo transfermarkt (jogo a jogo, ~11 mil páginas).

## Decididas pelo Guilherme em 22/11 (já podem ser corrigidas)

Resposta: a recomendação de cada uma em `decisoes-guilherme.md`, menos a D-01, que ficou com a opção A: tudo o que
já terminou entra agora, inclusive os Aperturas 2026 da Argentina e do Paraguai. A D-10 ficou com a opção B (edições não oficiais com aviso).


- D-04 (play-offs e desempates fora da liga): IT-018, DE-012.
- D-05 (eras antigas que faltam): IT-017.
- D-17 (artilheiros em dúvida): EN-004, FR-011 (só o Bokšić).
- D-18 (rebaixados fora do padrão): IT-012, FR-001 (só Antibes e RC Roubaix).
- D-19 (ordem entre empatados): IT-014, QE-002, PT-005, DE-013.
- D-20 (tribunal e pontos fora de campo): PT-004, PT-006.
- D-24 (identidade de clubes, Europa): FR-012, FR-013, PT-017, PT-018.

## Fontes novas a usar

Detalhes em `docs/revisao/fontes.md`.
- Wikipédia it: datas (Calendario), "a tavolino", spareggi, ordem da classifica avulsa.
- Wikipédia de: punições (Abzug), tribunal, Relegation; lista de artilheiros.
- Wikipédia fr: tribunal ("tapis vert"), bônus, rebaixamentos administrativos; lista de artilheiros.
- Wikipédia en: artigos de temporada de clube (Benfica), Bola de Prata.
- BDFutbol: árbitro e estádio do Espanhol (em lote); autores antigos da Espanha e da Inglaterra (ficha).
- Transfermarkt: datas do Alemão e do Francês; árbitro, público e autores (ficha); EFD1 para o Inglês antigo.
- RSSSF: datas e motivos de tribunal da Itália; autores do Alemão 1963-1999 e do Português 1999-2006.
- footballdatabase.eu: datas dos anos 1930 da França (limite de 50 páginas por dia).

Cobre 79 de 79 ids abertos de `coleta-europa` no `achados.csv` (22/11/2026; os fechados na conferência final estão riscados).
