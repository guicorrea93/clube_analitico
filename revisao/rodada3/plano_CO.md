# Plano de correção — Campeonato Colombiano (col-1), revisão CO, 22/11/2026

Ordem: gravidade x tamanho do erro x custo. Depois de cada bloco: `python coleta/col-1/importar.py`, `python coleta/col-1/conferir.py`,
teste de carga, `documentar.py`, e a revisão roda de novo `revisao/CO/campeoes.py`, `tabela_anual.py`, `rebaixados.py`, `varredura.py`,
`datas_repetidas.py` e `datas_espn.py`.

## coleta-sulamerica

### 1. coleta/col-1/ler_rsssf.py + coleta/col-1/importar.py (baratos, alto impacto)
1. **CO-001** (alta, 55 edições, no ar): ler a coluna "Runners Up" em `ler_rsssf.campeoes()`; em `importar.gravar()` vice = lista; em
   `classificacao()` pôr o vice em 2º. Fonte: colchamp.html (já em disco). Custo: ~20 linhas.
2. **CO-002** (alta, ~60 edições, no ar): `importar.classificacao()` ordenar por nível alcançado mesmo quando há tabela publicada
   (decisão CO-D2). Custo: baixo.
3. **CO-007** (alta, 45 rebaixados): dicionário `REBAIXADOS` (Wikipédia es, Anexo Ascensos y descensos) em `explicacoes.py` e
   `importar.situacao()`. Decisão CO-D1 para 1997. Custo: 1 dicionário.
4. **CO-008** (media, ~150 jogos em 48 edições): data de "First/Second Leg(s) [Mon DD]" no `ler_rsssf` (ou `rsssf_sul`, armadilha da
   seção 6 do COMECE-AQUI — se mexer no comum, reimportar as 8 competições); fallback: data da ESPN quando casou e difere > 1 dia.
5. **CO-011** (media): `conferir.eh_mata()` sem "Finalización"; quadrangulares/hexagonais/octogonais como `grupos`.
6. **CO-012** (media, 425 jogos da 1ª fase + quadrangulares de ~30 edições): grupo do quadrangular pelo clube (tabelas Group A/B);
   1ª fase sem grupo (`ler_rsssf.ler()` linhas 176-190).
7. **CO-014** (media): finais do Apertura/Finalización (1974-1982, 1999 "Final Clausura") com nome próprio e nível 0 (`FASES`, `NIVEL_FASE`).
8. **CO-017** (media): regex de `artilheiros_rsssf()` (1971, 1977, 1978); 2008+ pela Wikipédia es (Títulos por temporada).
9. **CO-016** (media): bônus das fases finais 1983-1999 e Tuluá -2 em 1995 em `ajuste_pontos`.
10. **CO-018**, **CO-021**, **CO-022** (media/baixa): gols com autor só quando a soma bate; descartar as linhas "abd"; explicar as
    divergências em `explicacoes.py` e corrigir `esperados()`.

### 2. coleta/col-1/wikipedia_jogos.py (médio custo, fecha os buracos dos anos da Wikipédia)
1. **CO-004** (alta, ~700 jogos faltando em 1955, 1958-1961, 1963, 1966): ler as 4 voltas e as listas "Fecha N"; matriz com 2
   placares por célula (1963). Conferir cada ano com a "Final Table" da RSSSF (hoje não lida: ver por que `tabelas_publicadas.csv`
   não tem 1955, 1958-1961, 1963, 1966).
2. **CO-005** (alta, 1964, +155 jogos): descartar a matriz quando a página tem a lista "Fecha N".
3. **CO-006** (alta, 1986, 1988, 1989, 1976): 1989 ler "Fecha N (Mes D)"; 1976 e 1988 completar as fases finais pela RSSSF
   (col76 "Final Hexagonal", col88); 1986 classificação pelas tabelas da RSSSF.
4. **CO-010** (media): `_data()` com ano + 1 depois da virada (1957 final, 1971 desempate).
5. **CO-013** (media, 1957): octogonal cancelado, grupos dos hexagonais, desempates.
6. **CO-009** (media, 2025 Fi): ler `{{fecha|DD|MM|AAAA}}`; em `outras_fontes.espn()` exigir placar igual quando não há data.
7. **CO-020** (baixa): datas dos títulos de rodada (1952-1988).
8. **CO-015** (media): placares de 1948-1949 pela tabela de confrontos da RSSSF (CORRIGE); os de 2001-2018 só depois de uma 3ª fonte
   (transfermarkt, ficha do jogo).

### 3. coleta/col-1/edicoes.py (tabelas dos anos sem jogos)
1. **CO-003** (alta, 1987 e 1991-1995, no ar): fazer a tabela final da RSSSF entrar como classificação (só os clubes da Primera A;
   1995 tem a tabela da B na mesma página). **CO-019** sai junto.

## banco-painel
1. **CO-023** (baixa): tirar o escudo do Huracán argentino do Huracán de Medellín (`baixar_escudos.py`, `data/escudos/`).
2. **CO-024** (baixa): escudos de 8 clubes (`baixar_escudos.py` PAGINAS).
3. **CO-025** (baixa, já conhecido): largura no celular.
4. Depois que a coleta reimportar: recarregar o `col-1` no banco e no site (todas as correções acima estão no ar hoje).

## Fontes novas a usar
- RSSSF colchamp (coluna Runners Up), Cross-Tables 1948/1949/1960, "Final Table" das páginas antigas, seções "Relegation" e datas "[Mon DD]".
- Wikipédia es: Anexo Ascensos y descensos (rebaixados); "Títulos por temporada" (artilheiros 2008+); páginas de torneio (datas das finais).
- transfermarkt (árbitro, público e 3ª opinião de placar, 2000s em diante; saison_id = ano − 1).
