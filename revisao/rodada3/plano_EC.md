# Plano de correção — Campeonato Equatoriano (ecu-1), 22/11/2026

Ordem: gravidade x tamanho do erro x custo. Nada disso está no site ainda (o ecu-1 está no banco e no painel local, mas https://clubeanalitico.pages.dev/dados/ecu-1.js devolve a página inicial). Corrigir antes de publicar.

## coleta-sulamerica

### 1. coleta/ecu-1/importar.py — classificação e rebaixados (alta; custo médio; resolve o pódio de ~30 edições)
1. **EC-001, EC-002, EC-003** — `classificacao()`: soma de todos os jogos da edição; ordem = campeão, vice, ordem da tabela publicada da última fase de liga (com bônus/punição), vencedores das disputas de 3º/4º, depois fase alcançada e pontos da temporada. Só usar uma tabela publicada inteira se os jogos dela = jogos do clube. Depende da decisão D-EC-1. Fonte de conferência: Wikipédia es, Historial (3º e 4º de 1957-2025) e `tabelas_publicadas.csv` (fase final). Teste: `revisao/EC/cmp_top4.py` deve dar 0 diferenças.
2. **EC-004, EC-005** — `situacao()`: dicionário `REBAIXADOS` (em `explicacoes.py`), com a lista do EC-004 + 2025 (El Nacional, Vinotinto); não casar "Relegation Group"; El Nacional 2025 com ajuste -9 e motivo. Fonte: Wikipédia es, "Ascensos y descensos a la Serie A". Teste: `revisao/EC/descensos_es.py`.
3. **EC-016** — `ordem_f`: ordenar fases pela data do 1º jogo/linha da página, não por `NIVEL_FASE`.
4. **EC-013** — gols da ESPN só quando a soma bate com o placar (2007, LDU 4-0 Cuenca).

### 2. coleta/ecu-1/ler_rsssf.py — fases e datas (média; custo médio; ~50 jogos + 4 fases)
1. **EC-009** — ler a data do título do bloco ("First Leg [Dec 17]", "Second Legs [Jul 10]", "Final [Dec 18, Quito]") e zerar a rodada ao abrir fase de mata-mata; depois recasar com a ESPN (`outras_fontes.espn`). Se a mudança for no comum `rsssf_sul.py`, reimportar as outras ligas e comparar os pacotes. Teste: `revisao/EC/datas_leg.py` = 0 diferenças.
2. **EC-003** — `FASES`: "Third Place (Playoffs?|Matches)" -> "Disputa do 3º lugar"; "Fourth Place ..." -> "Disputa do 4º lugar" (e `NIVEL_FASE` no importar).
3. **EC-010** — virada de ano: não somar 1 quando a data volta a dezembro (1997 rebaixamento em 1998-12).

### 3. coleta/ecu-1/explicacoes.py — correções pontuais (média; custo baixo)
- **EC-006** CONSERTA_TEXTO ('ecua99', 501) "No Descenso:" -> "Liguilla No Descenso".
- **EC-007** CONSERTA_TEXTO ('ecua63', 64) e ('ecua66', 90) "Final" -> "Final Round"; ('ecua97', 393) "Championship Playoff" -> "Hexagonal Final".
- **EC-010** CONSERTA_TEXTO ('ecua97', 467) "Playoff Descenso" -> "Relegation Group".
- **EC-008** CORRIGE descartar: ecua84:483,492,501,511,521,531; ecua86:541,542,552,553,565,566,579,580,592,593,603,604; ecua94:484,494. E pôr no `conferir.py` um aviso de jogo repetido (mesma data e clubes).
- **EC-011** CONSERTA_TEXTO ('ecua05', 53) "0-2" -> "2-2" (Emelec x LDU de Quito).
- **EC-012** CORRIGE 1965 ecua65:39, 46, 53, 72: awd, pontos para o adversário do Aucas.
- **EC-015** CORRIGE ('2025', 'espn:759348'): W.O. 0-3 para o Delfín (se D-EC-2 = opção 2).
- **EC-017** 2006 Barcelona x LDU (Fase final) = 2006-10-29 (ESPN).
- **EC-024** data 1969-10-26 em América de Ambato 0-11 LDU de Quito (Wikipédia es, página da LDU).
- **EC-014** artilheiros 1988, 1996, 1999: conferir numa 3ª fonte antes de mudar.

Depois: `python coleta/ecu-1/importar.py`, `conferir.py`, `testar_carga.py ecu-1`, `documentar.py` e recado ao agente 1 para recarregar o ecu-1.

## banco-painel
1. **EC-019** — `gerar_dashboard_v2.py`: participações por ano, não por edição (2005 conta duas).
2. **EC-018** — `baixar_escudos.py`: 36 escudos que faltam (Everest, Espoli, Filanbanco, Valdez SC, Patria, Manta Sport, Deportivo Quevedo, LDU de Loja...). Fonte: ogol (página de clube) e Wikipédia es.
3. **EC-020** — largura no celular (já conhecido).
4. Recarregar o ecu-1 depois da coleta corrigir e só então publicar.

## Fontes novas a usar
- Wikipédia es (página da liga e páginas de temporada): rebaixados, 3º/4º, punições, datas de 1960 e finais. Ver SCRATCH/fontes_EC.md.
- Para 1960-1999 não há fonte independente em lote com jogos (ogol vazio, transfermarkt sem esses anos); testar footballdatabase.eu outro dia.
