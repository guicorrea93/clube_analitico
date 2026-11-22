# Plano de correção — par-1 (revisor PY, 22/11/2026)

Ordem: gravidade x tamanho do erro x custo. Depois de cada bloco: `python coleta/par-1/importar.py`, `conferir.py`,
`testar_carga.py par-1 <scratch>`, `documentar.py`; rodar de novo `python -I revisao/PY/campeoes_3vias.py`,
`wiki_es_campeoes.py`, `tabelas_parciais.py`, `anos60.py` e `varredura.py` (todos em revisao/PY/).

## coleta-sulamerica

### 1. coleta/par-1/importar.py — classificacao(), situacao(), gravar()  (custo baixo, efeito maior)
1. **PY-001 (alta)** campeão sempre em 1º: inserir a linha do campeão da lista quando ele não está na tabela (1917, 1928, 1936, 1991).
2. **PY-002 (alta)** vice da lista (VICES/parachamp) sempre em 2º; corrige 23 edições de uma vez (inclui a regressão do 0b793ba em 1999-2003 e 2020 Clausura). Nos anos de vice duplo, esperar a decisão PY-028.
3. **PY-011 (alta)** situacao(): "Relegation Playoff" não é queda (1967 San Lorenzo; 1994 Pettirossi).
4. **PY-012 (media)** lista REBAIXADOS por ano tirada das linhas "Relegated"/"relegated on points average" das páginas da RSSSF (1965-2025) e da seção "Descenso" das páginas da Wikipédia es; marcar na última edição do ano. 1994: incluir os quatro que caíram na reestruturação (NB de para94).
5. **PY-020 (baixa)** gols da ESPN: descartar lance sem lado / exigir soma total = placar (2007 Trinidense x Nacional).
6. **PY-025 (baixa)** estádio: normalizar nomes da ESPN (tirar "ueno", "Tigo", "UENO"; uma grafia por estádio).
7. **PY-018 (media)** artilheiros 2014-2025: ler "Topscorers" das páginas para2014…para2025 ou a coluna Goleador da Wikipédia es (14 edições).

### 2. coleta/par-1/ler_rsssf.py — tabela_parcial(), FASES, TORNEIOS/FECHA, _vitoria_dada()  (custo médio)
1. **PY-003 (alta)** tabela_parcial(): linha sem número herda a posição de cima e não encerra a tabela (36 edições 1909-1959). Conferir 1928 (10 clubes) e 1936 (11).
2. **PY-008 (media)** TORNEIOS/FECHA (hoje vazios, herdados da Colômbia) para o Apertura e o Clausura de 1996-2007; finais deles como "Final do Apertura/Clausura"; "Overall Final", "Finalísima" = Final; "Triangular de Desempate" = desempate.
3. **PY-006 (media)** "Playoff against 11th Place" -> "Desempate do rebaixamento" (1961, 1963).
4. **PY-010 (media)** _vitoria_dada(): aceitar "awarded as a win to" (1960 Tembetary x Libertad).
5. **PY-009 (media)** data do título da fase ("First Leg [Dec 15]", "Semifinals [Jun 28]") — pode ser no leitor comum (coleta/comum-sulamerica/rsssf_sul.py; aí reimportar as oito competições e comparar) ou só em explicacoes.CORRIGE; de 2005 em diante, a data da ESPN quando a da página vier de rodada anterior.

### 3. coleta/par-1/edicoes.py — trechos e tabelas  (custo baixo)
1. **PY-005 (alta)** linha inicial do campeonato: para62 98, para63 83, para64 127, para65 217, para66 109 (tira 152 jogos de Torneo Preparación, Copa Asunción, Torneo de Honor e Copa República; some o "Ovetense").
2. **PY-007 (media)** tirar ("para05", 953, 971) (final da Intermedia: some o Fernando de la Mora de 2005) e cortar Pre-Sudamericana (2004, 2005), "Second Place Playoff" e "Cuadrangular for Third Copa Libertadores Place" (2000); o "Playoff for Second Place" de 2005 vira desempate do 2º lugar (decide o vice Libertad).
3. **PY-004 (alta)** 1982-1995: apontar por ano a tabela acumulada/final (tabelas=[(página, ini, fim)]); sem ela, só campeão e vice; 1989 com leitor do formato "J-Pts (GP-GC) V E D". Avaliar trazer os jogos de final que as páginas têm (1990, 1991, 1994).
4. **PY-027 (baixa)** 2026 Apertura: só quando o Guilherme decidir.

### 4. coleta/par-1/clubes_par.py  (custo baixo; depende das decisões)
1. **PY-014 (media)** "cerro porteno cd este" -> Cerro Porteño PF (se o Guilherme aprovar).
2. **PY-013 (media)** novo "Pettirossi de Encarnación" para 1994 (se aprovar).
3. **PY-015 (baixa)** 8 de Diciembre: Caaguazú.

### 5. coleta/par-1/explicacoes.py  (custo baixo)
1. **PY-028 (media)** vice escolhido nos anos de vice duplo (depois da decisão).
2. **PY-019 (media)** artilheiros divergentes (1935, 1962, 1963, 1967, 1970, 2003): conferir com a página do ano e registrar.
3. **PY-029 (baixa)** CONSERTA_TEXTO para a nota quebrada de para05 l.572-574.
4. **PY-021 (baixa)** descartar jogador "2"/"22" da ESPN (ou em outras_fontes.lances_espn()).

### 6. coleta/comum-sulamerica/documentar.py e importar.relatorio()
1. **PY-031 (baixa)** textos da ficha ("completa em 1990-1995", "menos jogos que o esperado" com mais jogos).

Fontes novas a usar: Wikipédia es (lista de campeões/vices/artilheiros e páginas de temporada, inclusive "Descenso"); RSSSF páginas do ano para linhas de início, rebaixados e datas de playoff; transfermarkt (2015+) se quiser árbitro e público.

## banco-painel

### gerar_dashboard_v2.py
1. **PY-001 (alta)** campeão do ED a partir de edicao.campeao_id, não da posição 1 (proteção contra pacote com tabela parcial).
2. **PY-023 (media)** linha parcial quando V/E/D vazio (não só J): hoje 87 linhas de 22 edições aparecem com 0 pts e "0 V·0 E·0 D"; esconder "Destaques" em tabela parcial.
3. **PY-024 (baixa)** participações antes de 1996 são parciais (aviso ou contagem só com tabela completa).

### publicação
1. **PY-022 (media)** não publicar o par-1 local (que traz a regressão dos vices) antes de recarregar o pacote corrigido; depois, publicar (o site ainda é o pacote antigo: 7.794 jogos).

### baixar_escudos.py / cadastro
1. **PY-016 (baixa)** 16 clubes sem escudo (Presidente Hayes, Sport Colombia, Colegiales, Cerro Corá, Atlántida…); 12 de Octubre com imagem genérica.
2. **PY-017 (baixa)** "Olímpia" (BRA) x "Olimpia" (PAR), se o Guilherme decidir renomear.
3. **PY-026 (baixa)** largura no celular (pendência conhecida).
