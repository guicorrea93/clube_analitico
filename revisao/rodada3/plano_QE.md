# Plano de correção — Inglês (eng-1) e Espanhol (esp-1), revisor QE, 22/11/2026

Todos os achados abertos das duas ligas (antigos e novos), por quem corrige e por arquivo, em ordem de prioridade
(gravidade x tamanho do erro x custo). [NO AR] = alto e visível no site. Provas e sugestões completas em
`docs/revisao/achados.csv` (ids antigos), `SCRATCH/achados_QE.csv` e `SCRATCH/sugestoes_QE.csv`; fontes em
`SCRATCH/fontes_QE.md`; decisões em `SCRATCH/decisoes_QE.md`.

## coleta-europa

### `coleta/esp-1/importar.py`
1. **QE-002 (alta) [NO AR]** 1960/61: 6º Athletic e 7º Betis (hoje invertidos). Depende da decisão (decisoes_QE.md) ou sai
   sozinho com o QE-001 se a ordem oficial passar a ser a que bate com o critério. Fonte: RSSSF spanhist5969 e BDFutbol.
   Custo: 1 linha.
2. **QE-001 (média)** critério de desempate: `ordenar()` com confronto direto recursivo (como o `confronto_geral` do por-1 +
   saldo entre os empatados) e, na classificação de rodada, confronto só com todos os jogos entre os empatados disputados.
   Muda 11.351 posições da Corrida em 95 temporadas e acerta a última rodada de 1954/55, 1969/70, 1972/73, 1981/82 e 1995/96;
   1963/64 deixa de ser "média de gols". Código de referência: `revisao/QE/desempate_esp.py` (`ordenar_esp`). Fonte: class_rules
   da Wikipédia en (todas as temporadas). Custo: baixo (função pronta), refazer pacote + testar_carga + documentar.
3. **QE-003 (média)** 2003/04 Barcelona x Sevilla em 03/09/2003, 00:05 (dicionário `DATAS` novo, como no eng-1). Fonte:
   football-data, ESPN, transfermarkt, BDFutbol.
4. **QE-004 (baixa)** observação dos 2 jogos suspensos e completados noutro dia (2004/05 Real Madrid x Real Sociedad; 2023/24
   Granada x Athletic) em `EXPLICACOES`. Fonte: BDFutbol (fichas 23749 e 31397).
5. *(cobertura, sem id)* **árbitro** (hoje 0%) e **estádio antes de 2001/02** (hoje 0%) de todos os 27.716 jogos: coluna
   Árbitro/Estadio da página da temporada do BDFutbol (95 páginas, já baixadas em `data/cache/revisao/QE/`; leitor
   `revisao/QE/bdfutbol.py`, `jogos_temporada`; casamento pronto em `revisao/QE/cmp_bdfutbol.py`). Custo: baixo; risco: grafia
   de nomes de época dos estádios.
6. *(cobertura, sem id)* **autores dos gols antes de 2001/02** (19.668 jogos): ficha do BDFutbol (autor e minuto, ~890 KB por
   página, ~11 h) ou do transfermarkt (nome completo, ~117 KB, ~11 h). Melhor perguntar ao BDFutbol pelo serviço de dados antes.
   **Cartões** antes de 2001/02: só o transfermarkt. **Público** antes de 2000: nenhuma fonte testada tem.

### `coleta/eng-1/importar.py`
7. **QE-005 (média)** 1953/54 Sheffield Wednesday x Aston Villa em 07/11/1953 (`DATAS`). Fonte: 11v11 e transfermarkt.
8. **EN-016 (baixa)** autores dos 12 jogos sem autor (lista pronta em `SCRATCH/sugestoes_QE.csv`), dicionário novo
   `GOLS_MANUAIS`. Fonte: fichas do BDFutbol. Com isso a artilharia calculada de 2014/15 fica Agüero 26.
9. **QE-006 (baixa)** árbitro com nome completo (BDFutbol) no lugar dos 3 formatos do football-data; conferir os 40 jogos com
   outro sobrenome.
10. **EN-004 (baixa)** artilheiro de 1905/06: decisão (decisoes_QE.md; recomendação: Shepherd com a divergência anotada).
11. *(cobertura, sem id)* **árbitro e estádio de 1960/61 a 1999/00**: página da temporada do BDFutbol (40 páginas, em cache;
    árbitro em 74-100% dos jogos). **Autores e público antes de 2001/02**: ficha do transfermarkt (1888/89 e 1922/23-1959/60:
    ~14.450 páginas, ~9 h; 1960/61-1991/92: +~14.000; Premier League 1992/93-2000/01: ~3.670), ou ficha do BDFutbol de 1960/61
    em diante (autores, sem público). 1889/90-1921/22: nenhuma fonte completa (o transfermarkt tem 15-25% dos jogos).

### `coleta/comum-europa/`
12. **RC-004 (baixa)** nomes da ESPN fora de ordem no eng-1 (e fra-1): levar o `NOMES_ESPN` do esp-1 para `espn.py`.
13. **QE-007 (baixa)** observações da classificação em inglês (18 no eng-1, 13 no esp-1): traduzir em `wiki_tabela.py` ou no
    importador.

## banco-painel

### `gerar_dashboard_v2.py`
1. **RC-003 (baixa)** antes de publicar o eng-1 local: "pontos corridos" sem exigir `classificacao_rodada` (senão o Título mais
   apertado perde 1888/89-1991/92).
2. **ES-011 e EN-010 (baixa)** nota das punições e casos especiais na edição (`notas()`, a partir de `edicao.observacao`).
3. **EN-009 (baixa)** Participantes: "↓ caiu" / "↑ subiu" pelos rebaixados do banco (campo `rb` em EDS e função `seta`).
4. **ES-014 (baixa)** rótulos com a temporada ("2012/13") nas Curiosidades e na Corrida dos títulos (Espanhol e Inglês).
5. **EN-013 (baixa)** cartão "Título mais apertado" com muitos escudos (`.cu-um` com quebra de linha).
6. **ES-013 (baixa)** nome de época: decisão (decisoes_QE.md; recomendação: nome da época nas telas de edição).

### `baixar_escudos.py`
7. **ES-012 (baixa)** escudos do CD Málaga e da AD Almería em `OUTRAS_FONTES` (BDFutbol: /i/eg/175f.png e /i/eg/174.png).

### Publicação
8. **QE-009 (`nao-e-erro`)** esp-1 com 2025/26 está certo no pacote, no banco e no painel local (conferido com o BDFutbol);
   o site ainda tem 94 edições: publicar quando o Guilherme mandar (junto com o QE-001/QE-002, se já corrigidos, para não
   publicar duas vezes).

## Ordem sugerida de trabalho
1. coleta-europa: QE-001 + QE-002 + QE-003 + QE-004 no esp-1 (um só reimport), depois QE-005 + EN-016 + QE-006 no eng-1.
2. banco-painel: recarregar, RC-003, publicar eng-1 e esp-1; depois os textos (ES-011/EN-010, EN-009, ES-014, EN-013) e os
   escudos (ES-012).
3. Cobertura (árbitro e estádio do esp-1 pelo BDFutbol) quando o Guilherme quiser enriquecer; autores antigos só com ok
   para muitas horas de download.
