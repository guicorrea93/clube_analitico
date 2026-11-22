# Plano de correção — Série C, Série D e Copa do Brasil (revisão QC, 22/11/2026)

Todos os ids ABERTOS destas competições (antigos e novos), em ordem de prioridade (gravidade x tamanho do erro x custo).
Nenhum achado de gravidade alta está aberto: os altos (SC-002, SC-004, SD-001 a SD-003, CB-001 a CB-003, CL-001) já foram
corrigidos e reconferidos no ar em 22/11. Por isso não há marca [NO AR].

Depois de cada bloco da coleta: `python coleta/<slug>/importar.py`, `python coleta/comum/testar_carga.py <slug> <scratch>`,
`python coleta/comum/documentar.py`; depois o agente 1 recarrega o banco e o painel. Para conferir: `python -I revisao/QC/compara_bola.py`, `revisao/QC/placar_4fontes.py`,
`revisao/QC/datas_3fontes.py`, `revisao/QC/penaltis_bola.py`, `revisao/QC/fn.py` (rodam do cache, sem baixar de novo).

## coleta-brasil

### 1. coleta/bra-copa-do-brasil/importar.py
1. **QC-005** (média, 2 jogos, custo mínimo): exceções à regra "vale o do ogol": 1995-03-19 Nacional-AM 1x0 Cristal; 1998-02-18 Bahia 1x2 Botafogo-PB (PLACAR_MANUAL ou CORRECAO_JOGO com gm/gv). Regra nova: só trocar RSSSF por ogol com uma 3ª fonte (Bola n@ Área, Wikipédia en, Futebol Nacional).
2. **QC-004** (média, 20 datas): CORRECAO_JOGO com 'data' (motivo _UM_DIA) para os jogos de 2008, 2014, 2015, 2018 e 2024 em `revisao/QC/saida_datas_3fontes.txt`. Fontes: Bola n@ Área + transfermarkt.
3. **CB-005** (média, decisão QC-D3): 1990 e 1991 só depois do jornal; 2002 fica.
4. **CB-007** (média, decisão QC-D4): recomendação: incluir a preliminar de 1999 com a data do Futebol Nacional (28/01/1999, Náutico 0x1 Santa Cruz).
5. **QC-008** (baixa): texto da pendência em coleta/comum/documentar.py (PENDENCIAS).

### 2. coleta/bra-serie-d/importar.py
1. **QC-001** (média, 17 jogos, custo mínimo): pênaltis em CORRECAO_JOGO (chaves 'pm'/'pv' -> p.pen_m/p.pen_v), lista no achado. Fontes: Bola n@ Área + transfermarkt.
2. **SD-011** (baixa, 1 jogo, prova da CBF): CORRECAO_JOGO[(2013, 'Botafogo-PB', 'Salgueiro', '2013-09-06')] = {'data': '2013-10-06'}.
3. **QC-003** (média, 14 datas + 23 de 2026 a conferir): CORRECAO_JOGO com 'data'. Fontes: Bola + transfermarkt (2026: só o transfermarkt).
4. **SC-018** (baixa, decisão): chave de ordenação dos eliminados (vale também para a C).
5. coleta/bra-serie-d/clubes_d.py: **CL-023** (baixa, decisão QC-D1: "Espírito Santo FC", sem escudo) e **CL-028** (baixa: AA Araguaia em Água Boa-MT; Botafogo-DF no DF).

### 3. coleta/bra-serie-c/importar.py (e coleta/comum/ogol.py)
1. **QC-002** (média, 58 datas + 37 de 2026 a conferir): criar CORRECAO_JOGO de datas (como na D) ou corrigir de uma vez no coleta/comum/ogol.py o "dia seguinte em jogo noturno" (2019 e 2026 são BASE_OGOL: todos os jogos das 20h em diante). Fontes: Bola + transfermarkt + Futebol Nacional (2007+); súmulas da CBF desempatam 2013+.
2. **QC-011** (média, 1 jogo): PLACAR_MANUAL 2007-07-14 ABC 4x0 Vera Cruz-PE (ogol, Bola, Futebol Nacional e tabela da pt).
3. **QC-012** (baixa, 17 jogos): ogol + Bola contra a RSSSF; conferir numa 4ª fonte antes de mudar (lista `revisao/QC/saida_placar_4fontes.txt`). Rever a regra "fica o placar que fecha com a tabela da RSSSF".
4. **SC-016** (baixa): 9 dos 12 jogos viram nao-e-erro (Bola confirma o pacote); 3 esperam a decisão QC-D2 / jornal.
5. **SC-021** (baixa): jogos 1995, 2011, 2012 e gols de 2001 são nao-e-erro (Bola); 1999 manter 226 e explicar em coleta/bra-serie-c/explicacoes.py; 2002 e 2008 conferir com a lista do Bola.
6. **SC-018** (baixa, decisão): ver item 2.4.
7. coleta/bra-serie-c/clubes_c.py: **QC-009** (baixa, decisão QC-D1): "Santo Amaro-PE" em 1981.

### 4. Todas as coletas: coleta/comum/
1. **QC-006** (baixa, 100 datas): onde a data da RSSSF for contra ogol + Bola, usar a do ogol (lista `revisao/QC/saida_datas_ogol_bola.txt`).
2. **QC-007** (baixa): coleta/comum/observacao.py (4 observações em inglês) e coleta/comum/rsssf.py / gols.py (notas de rodapé no gols_texto de 17 jogos).

### 5. Buracos de cobertura (não são achados; só se o Guilherme pedir, prioridade baixa)
- Público (0% no pacote): Bola n@ Área em lote (já baixado: ~1.900 jogos da C, ~690 da D, ~1.240 da Copa); ogol (ficha) jogo a jogo para o resto.
- Árbitro: Bola (~1.300 jogos), súmulas da CBF 2013+ (jogo a jogo), transfermarkt 2009+ (jogo a jogo), ogol (ficha).
- Cartões (0%): súmulas da CBF 2013+ (C, D) e 2014+ (Copa), jogo a jogo (~1 PDF por jogo); ogol (ficha) antes disso.
- Autores: Bola completa ~2.900 gols sem autor (C 2000s-2010s, D 2010s, Copa 1989 e 2000s-2010s) em lote; Copa 1990-1999 e Série C 1994-2001 só pela ficha do ogol (jogo a jogo) ou jornal.

## banco-painel

1. **RC-005** (baixa, decisão): gols de W.O. fora das somas (gerar_dashboard_v2.py). Recomendação: conta o jogo, não os gols (Bola e Wikipédia).
2. **RV-005** (baixa): painel/index.html, nome do mandante cortado no começo em 420 px (função jogos(e) e CSS .cp-jogo).
3. **RC-002** (baixa): escudos dos três Operário de Várzea Grande (baixar_escudos.py).
4. **CL-029** (baixa, já com o revisor QA): cidades vazias; para os clubes destas competições a lista de participantes do Bola n@ Área dá a cidade de cada um, edição a edição (ex.: https://www.bolanaarea.com/serie_c_1981_tab.htm, serie_c_2007_partic.htm, copa_do_brasil_2008_fase1.htm).
5. **CL-024** (baixa, com o revisor QA): escudos faltando (Oeste, União Bandeirante, Central-RJ, Rodoviária, Serrano).
