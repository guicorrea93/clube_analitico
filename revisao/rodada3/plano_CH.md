# Plano de correção — Campeonato Chileno (chi-1), 22/11/2026

Ordem: gravidade x tamanho x custo. Depois de cada bloco: `python coleta/chi-1/importar.py`, `conferir.py`, `testar_carga.py chi-1 <scratch>`, `documentar.py`; conferir de novo com `revisao/CH/tres_vias.py`, `classif_x_jogos.py`, `campeoes_es.py`, `pares.py`, `sobe_desce.py`.

## coleta-sulamerica

### 1. coleta/chi-1/edicoes.py e ler_rsssf.py (fases e trechos) — rápido, muda pódio e "Final" no ar
- CH-008: cortar os trechos antes da Liguilla Pré-Sul-Americana/Pré-Libertadores (2015/16 Ap e Cl, 2016/17 Ap, 2017 Transición); "Pre-?Sudamericana" no FIM_PADRAO. Vice 2016/17 Ap = Deportes Iquique.
- CH-009: fase "Desempate do título" para "Playoff for Apertura Championship" (1997) e "Apertura Championship Playoff" (2013/14).
- CH-016: fase "Desempate do rebaixamento" para "Playoff against (direct )?relegation" (1971, 1977).
- CH-011: edição 2020 — ler com ano_fim = 2020 (a 1ª data é janeiro) para as datas não pularem um ano; depois refazer o casamento com a ESPN.
- CH-012: ler "First/Second Leg(s) [Mon d]" como data (ou usar a data da ESPN nos mata-matas). Fonte de conferência: ESPN e es.wiki.
- CH-022 (baixa): grupos herdados da tabela do topo (2002-2008), "Interseries" (1969-70), 5º lugar do Provincial (1968).

### 2. rsssf_sul.linha_tabela / ler_rsssf (coluna de bônus) — rápido, pontos errados no ar
- CH-001: tabelas de 1979, 1981, 1982 e 1983 com a coluna de bônus antes dos pontos. Avisar o agente se mexer no leitor comum (reimportar as competições e comparar pacotes).

### 3. coleta/chi-1/explicacoes.py (CONSERTA_TEXTO e CORRIGE) — rápido
- CH-002: chile44:167, chile43:186, chile53:198, chile72:214 (clube trocado na rodada). Vice 1944 = Audax.
- CH-013: placares do ogol de 1990, 1991, 1993, 1994, 1995 (transfermarkt + RSSSF + es.wiki concordam); reabrir as outras divergências de 1985-1995 com o transfermarkt.
- CH-014: 1988 jogo duplicado (ogol:5293713 -> Naval 1-1 O'Higgins); 1986 adversários trocados.
- CH-015 (parte): 2011 Ap Ñublense 2-0 Wanderers ("award revoked").
- CH-007: 1985 Everton (achar os 2 jogos numa 3ª fonte; footballdatabase.eu quando o limite diário voltar).

### 4. coleta/chi-1/importar.py classificacao() e situacao() — médio, muda vice e rebaixados
- CH-003: preferir a tabela acumulada/final às da 1ª fase (1954, 1955). Vice 1955 = Colo Colo.
- CH-004: 1968 pela tabela do Nacional + desempate do 2º lugar. Vice = U. Católica.
- CH-005: bônus (Polla Gol 1979/1982/1990; 1969-70) e CH-015 punições como ajuste_pontos também na classificação calculada. Vice 1982 = Colo Colo.
- CH-006: 1984 pela ordem do quadrangular final. Vice = Cobresal.
- CH-019: quando a tabela publicada existe e só não fecha por 1-2 gols, usar a ordem dela (1947: 3º U. de Chile).
- CH-010: situacao "rebaixado" só com "Relegated"; rebaixados das linhas RELEGATED (chilehist) e "Relegated:" (páginas por ano). 2020: U. de Concepción, não Colo Colo.
- CH-025 (baixa): Deportes Concepción fora do 2008 Clausura.
- CH-018: artilheiros_rsssf() aceitar um espaço entre país e clube (1936, 1937, 1947).

### 5. coleta/chi-1/outras_fontes.py — rápido
- CH-017: lance repetido da ESPN (gol contra dos dois lados); só gravar gols que fecham com o placar.
- CH-024 (baixa): cidade "Estadio La Portada" -> "La Serena".
- CH-023 (baixa): 7 datas do ogol de 1969 casadas com jogo de outra fase; 2010 conferir com es.wiki.

### 6. coleta/chi-1/baixar_ogol.py — demorado (download educado)
- CH-028: páginas que faltam do calendário (1964, 1971, 1977, 1982) e conferir 1951-1957: ~1.000 datas a mais.

### 7. Decisões (esperam o Guilherme): CH-020 (Green Cross), CH-021 (Deportes Arica = San Marcos), CH-018 (artilheiro 1968/1998) — clubes_chi.py REGRAS.

## banco-painel
- CH-026 (baixa): escudos de Carlos Walker, Deportivo Alemán, Ferroviarios, Iberia, Santiago FC (baixar_escudos.py PAGINAS).
- CH-027 (baixa, já conhecido): largura no celular.
- Depois das correções da coleta: recarregar o chi-1 (`futebol/carregar_pacotes.py`) e publicar.

## Fontes novas a usar
- transfermarkt (CLPD, 1990-2001 e 2018-2025): 3ª fonte de placar e data; fichas com árbitro, público e autores.
- es.wiki (páginas de temporada): jogos com data de ~1992 em diante, goleadores, descensos.
- RSSSF chilehist: rebaixados oficiais e bônus.
