# Plano de correção — per-1 (revisor PE, 22/11/2026)

O per-1 está no banco e no painel local, **ainda não publicado** no site. Corrigir as altas antes de publicar.
Depois de cada correção: `python coleta/per-1/importar.py`, `conferir.py`, `testar_carga.py per-1 <scratch>`, `documentar.py`; o agente 1 recarrega.
Identifique jogos por edição + data + clubes (os ids mudam ao reimportar).

## coleta-sulamerica

### 1. coleta/per-1/importar.py — classificacao() e situacao()  (maior ganho: 4 altas)
1. **PE-008 (alta)** aceitar e preferir a tabela "acumulada" do ano (`ts = [... if not tb.get("acumulada") ...]`): conserta 1998, 2000, 2001, 2004, 2005, 2009, 2012. Conferir com a tabela acumulada da Wikipédia es.
2. **PE-002 (alta)** anos sem jogos (`if e.sem_jogos: pub = next(...)`): usar o Championship Group (+ Relegation Group) da peruhist: 1970, 1972, 1973, 1974, 1977, 1979.
3. **PE-003 (alta)** `situacao()`: rebaixado só com "Relegated" explícito (não "to Relegation Group/Playoff", "Relegation Playoff"): 1938, 1970, 1977, 1979, 2002, 2006, 2008, 2014.
4. **PE-006 (alta)** 2021: tabela anual com descontos + decisão do TAS (Cusco -2, Cienciano +1); clube só com jogo anulado (Carlos Stein) fora da classificação.
5. **PE-019 (media)** 1912-1921: gravar a ordem completa da RSSSF/es (depende de PE-D1).
6. **PE-015 (media)** artilheiro 1996: Czornomaz e Sáenz, 20.
Fontes novas: Wikipédia es (tabela acumulada, Ascensos y descensos).

### 2. coleta/per-1/explicacoes.py
1. **PE-004 (alta)** 2020: TABELAS_FORA para a 1ª tabela anual (pré-TAS); Carlos Stein -3 rebaixado, Alianza fica.
2. **PE-007 (media)** CORRIGE rsssf:peru2021:542 (Cusco x Cienciano 2021-08-27) -> 2-2, TAS 21/01/2022.
3. **PE-014 (media)** novo REBAIXADOS {ano: [clubes]} da Wikipédia es (~45 edições sem marca), usado por situacao().
4. **PE-018 (media)** 2022: conferir +2 Alianza, +1 Ayacucho, Vallejo -2 x -3 (Res. 046-CCL-FPF-2022).
5. **PE-026, PE-016 (baixa)** registrar as divergências (vice 1914, critério dos artilheiros).
6. **PE-017 (media)** só corrigir placares com terceira fonte (jornal/dechalaca; transfermarkt para 2004+).

### 3. coleta/per-1/edicoes.py
1. **PE-005 (alta)** 2021: trecho até a seção "Finals" (Alianza 1-0 Cristal 21/11, Cristal 0-0 Alianza 28/11), sem o Promotion/Relegation Playoff (ou EXTRAS).
2. **PE-023 (baixa)** docstring de 1912-1921 ("nenhuma fonte tem tabela" está errado).

### 4. coleta/per-1/ler_rsssf.py — FASES, TORNEIOS, ano das datas
1. **PE-013 (media)** final do Torneo de Verano 2017 e 2018 -> "Final do Torneo de Verano".
2. **PE-010 (media)** 1990: janeiro depois de dezembro = ano seguinte; final nacional 1991-02-03 como "Final".
3. **PE-011 (media)** 1987/1988 "Regional Final (in Lima)" -> fase própria; playoff 1987-09-16.
4. **PE-012 (media)** 1988: liguilla final separada da "Final".

### 5. coleta/comum-sulamerica/rsssf_sul.py + coleta/per-1/outras_fontes.py
1. **PE-009 (media)** data no título da fase ("First Leg [Nov 21]", "Playoff [Dec 17]"); mata-mata sem a rodada da liga; com ESPN casada, gravar a data local da ESPN. Mexe no leitor comum: reimportar as 8 competições e comparar.

### 6. coleta/per-1/clubes_per.py
1. **PE-001 (alta)** regra de "Jorge Chávez" 1900-1925: sem número -> "Jorge Chávez" (Callao = Nr. 2); vice 1918 e 1921.
2. **PE-021, PE-022 (baixa)** Sporting Tabaco = Lima (Rímac); cidade do Deportivo Bancos.

### 7. coleta/comum-sulamerica/documentar.py
1. **PE-023 (baixa)** PENDENCIAS: tirar "Ainda não carregado no banco".

## banco-painel
1. **PE-024 (baixa)** publicar o per-1 só depois das altas acima.
2. **PE-020 (baixa)** baixar_escudos.py PAGINAS: 114 clubes sem escudo; começar por Atlético Chalaco, Mariscal Sucre, Unión Huaral, Defensor Lima, Deportivo San Agustín, Centro Iqueño, Sport Progreso, Coronel Bolognesi, CNI, Ciclista Lima, Sporting Tabaco (Wikipédia es).
3. **PE-025 (baixa)** celular mais largo que a tela (já conhecido).

## Decisão do Guilherme
- PE-D1 (1912-1921): recomendação A (manter e completar, com etiqueta "Liga Peruana").
