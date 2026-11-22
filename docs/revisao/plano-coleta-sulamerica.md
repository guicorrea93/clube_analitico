# Plano de correção — coleta América do Sul

Para: agente de coleta América do Sul. Revisão profunda de 22/11/2026.
Competições: Argentino (`arg-1`), Uruguaio (`uru-1`), Chileno (`chi-1`), Colombiano (`col-1`), Paraguaio (`par-1`),
Peruano (`per-1`) e Equatoriano (`ecu-1`).

## Como usar

1. Só comece quando o Guilherme mandar corrigir. Hoje a prioridade dele é coletar.
2. Corrija na ordem: primeiro "ERRADO NO AR", depois cada competição de cima para baixo.
3. Cada linha é um resumo. A sugestão completa está no `docs/revisao/achados.csv`, coluna `o_que_a_fonte_diz`,
   depois de "SUGESTÃO:" (e "COMPLEMENTO (22/11):").
4. Ids marcados "espera D-xx": o Guilherme respondeu em 22/11 (todas menos a D-10). Corrija pela resposta registrada
   em `docs/revisao/decisoes-guilherme.md` (seção "Respostas do Guilherme").
5. Identifique jogos por competição + data + clubes, nunca pelo `partida_id`.
6. Depois de cada liga: `python coleta/<slug>/importar.py`, `conferir.py`,
   `python coleta/comum-sulamerica/testar_carga.py <slug> <scratch>`, `documentar.py`.
7. **Leitor comum** (`coleta/comum-sulamerica/rsssf_sul.py`): várias ligas pedem a mesma mudança (data no título da fase,
   coluna de bônus, virada de ano). Faça uma vez só, reimporte as 8 ligas e compare os pacotes (armadilha da seção 6 do
   COMECE-AQUI). Ids: AR-023, UY-014, UY-015, CH-001, CH-012, CO-008, PY-009, PE-009, EC-009, EC-010.
8. No fim: escreva os ids corrigidos em `docs/coleta/pedidos-sulamerica.md` e rode as varreduras
   `python -I revisao/tela/varredura.py` e `python -I revisao/tela/datas_repetidas.py` (copie e troque a lista).
   O agente 1 recarrega o banco e publica.

## ERRADO NO AR (altos já visíveis no site)

> **Atualização de 22/11:** o Peruano e o Equatoriano foram publicados às 11:18 (commit fed171c), e o Paraguaio do site
> passou a ser o pacote novo, com os vices quebrados de 1999 a 2003 e do Clausura 2020 (PY-002 e PY-022). Entram no ar:
> PE-001, PE-002, PE-004, PE-005, PE-006 e PE-008; EC-001, EC-002, EC-003 e EC-005.


Argentino (`arg-1`):
- AR-001 (alta): 1913 Federación, campeão errado (Estudiantes de Buenos Aires no lugar do Estudiantes de La Plata).
- AR-011 (alta): 1913 Federación, vice certo GEBA (um jogo a mais).
- AR-002 (alta): 1976 Nacional, vice certo River Plate.
- AR-003 (alta): 1987/88, vice certo San Lorenzo (falta 1 jogo).
- AR-004 (alta): 1989/90, vice certo Independiente (faltam punições).
- AR-005 (alta): 2008/09 Apertura, vice certo Tigre.
- AR-006 (alta): 1926 Amateurs, só 43 de 325 jogos; usar a tabela publicada.
- AR-007 (alta): 1926 Asociación, vice certo Argentinos Juniors.
- AR-008 (alta): 1919 Asociación soma o torneio anulado.
- AR-009 (alta): 1919 Amateurs, vice certo Vélez.
- AR-010 (alta): 1912 Asociación, vice certo San Isidro.
- AR-012 (alta): 1895, vice certo Lomas Academy (W.O. sem pontos).
- AR-013 (alta): 1896, vice certo Flores; 2 jogos a mais.
- AR-016 (alta): 1949, jogo "Gimnasia 1-0 Gimnasia" e desempates somados na tabela.

Uruguaio (`uru-1`):
- UY-006 (alta): 1994-2025, classificação final é a tabela do Apertura (28 edições).
- UY-004 (alta): vices errados em 14 edições.
- UY-001 (alta, espera D-09): títulos de 1923 FUF, 1924 FUF e 1926 que a AUF não reconhece.

Chileno (`chi-1`):
- CH-001 (alta): 1981 e 1983, a coluna Pts mostra o bônus no lugar dos pontos.
- CH-008 (alta): liguillas pré-Libertadores como "Semifinal/Final" (2015/16, 2016/17, 2017); vice 2016/17 Ap errado.
- CH-002 (alta): clube trocado em jogos de 1943, 1944, 1953 e 1972; vice 1944 certo Audax.
- CH-003 (alta): 1954 e 1955 com a tabela da 1ª fase; vice 1955 certo Colo Colo.
- CH-004 (alta): 1968, vice certo U. Católica.
- CH-005 (alta): bônus fora da classificação calculada; vice 1982 certo Colo Colo.
- CH-006 (alta): 1984, ordem pelo quadrangular final (vice Cobresal).
- CH-007 (alta): 1985, vice certo Everton.
- CH-009 (alta): desempates do título de 1997 Ap e 2013/14 Ap dentro da fase única.

Colombiano (`col-1`):
- CO-001 (alta): vice errado em 55 edições.
- CO-002 (alta, espera D-02): classificação final é a da 1ª fase (~60 edições).
- CO-003 (alta): 1987 e 1991-1995 com tabela zerada.
- CO-004 (alta): faltam ~700 jogos (1955-1966).
- CO-005 (alta): 1964 com jogos duplicados (72 por clube).
- CO-006 (alta): 1976, 1986, 1988 e 1989 com jogos faltando.

Paraguaio (`par-1`; o site ainda é o pacote antigo):
- PY-001 (alta): campeão fora do 1º lugar (1917, 1928, 1936, 1991); a contagem de títulos fica errada.
- PY-002 (alta): vices errados ou vazios (18 edições no site).
- PY-003 (alta): tabelas parciais cortadas (1909-1959; 1928 e 1936 com 1 clube).
- PY-004 (alta): 1982-1995 com a tabela de uma fase; 1989 com colunas trocadas.
- PY-005 (alta): 1962-1966 com 152 jogos de copas de pré-temporada.

Só no banco (a tela não mostra a marca "rebaixado"): CH-010, CO-007, PY-011.
O Peruano e o Equatoriano não estão no site.

## Argentino (`arg-1`) — 41 ids

### 1. Pódio e campeão (dados já no disco; custo baixo)
`coleta/arg-1/edicoes.py` (`_EST_LP` e trecho da 1913 Federación):
- AR-001 (alta): "CA Estudiantes" e "Club Atlético Estudiantes" no `_EST_LP`.
- QU-001 (média): trecho `('arg13', 377, 585)` (tira 2 amistosos).
- AR-011 (alta): sai com os dois acima (GEBA 2º).

`coleta/arg-1/campeoes_wiki.py` + `importar.montar()` (vices e 3º da lista oficial, `en_campeoes.txt`):
- AR-002 (alta): 1976 Nacional River; fases da 1976 como "Desempate do grupo".
- AR-005 (alta): 2008/09 Apertura pela mini-tabela do triangular.
- AR-014 (média): 1997/98 Apertura, falta River 1-3 Rosario Central (CONSERTA_TEXTO arg98:61).
- AR-015 (média): 3º de 1974 Nacional (Vélez) e 1929 (River).

`coleta/arg-1/importar.py`, `classificacao()` com TABELA_OFICIAL (tabela publicada quando os jogos não fecham):
- AR-006 (alta): 1926 Amateurs (jogos incompletos).
- AR-007 (alta): 1926 Asociación (+ jogos do Boca pelo historiadeboca).
- AR-008 (alta): 1919 Asociación, só o torneio final.
- AR-009 (alta): 1919 Amateurs.
- AR-010 (alta): 1912 Asociación, sem os clubes que foram para a FAF.
- AR-012 (alta): 1895, W.O. dão pontos (`conferir.soma()`).
- AR-013 (alta): 1896, tirar o jogo repetido de 17/08.
- AR-020 (média): 1908, 1929, 1931 Liga e 1965.
- AR-003 (alta): 1987/88, incluir Instituto x San Lorenzo (08/05/1988) em CORRIGE.
- AR-004 (alta): 1989/90, punições de -2 (AJUSTES ou tabela publicada).
- QU-004 (média): 1989/90 Newell's x Boca: conferir 1-2 x 0-2 awd.
- AR-016 (alta): CONSERTA_TEXTO arg49:246 (Gimnasia x Estudiantes LP); desempates fora da tabela.

### 2. Datas (grande: ~3.900 jogos; custo médio)
- AR-022 (média): ano errado em ~3.920 jogos; regra validada em `revisao/QU/sim_ano.py` (lista `sim_ano_mudancas.tsv`).
- QU-002 (média): janela real nas temporadas longas (1927, 1928, 1930) e o ano escrito na página (1937).
- AR-023 (média): data no título da fase ou rodada (leitor comum, item 7 do "Como usar").
- QU-003 (média): `outras_fontes.py`, casar a ESPN pelo par de clubes; data da ESPN vale (ex.: Boca 2-0 River 2025).
- AR-024 (baixa): 2005-09-31 pela ESPN; 2021-02-29 sai com o AR-022.
- QU-005 (baixa): datas do Boca de 1945, 1954, 1977 e 1990: só com 3ª fonte.

### 3. Jogos, fases e artilheiros
`edicoes.py` e `ler_rsssf.py` (FASES):
- AR-026 (média): "Final" com jogos de outra disputa (1929, 1970 Nacional, 1979); "Disputa do 3º lugar".
- AR-025 (média): "Desempate do título" errado (1931 Asociación, 1937, 1939, 1923, 1979).

`edicoes.py` / `explicacoes.EXTRAS` e CONSERTA_TEXTO:
- AR-018 (média): 4 jogos de 2016/17 que só a ESPN tem (462770, 462744, 462710, 462684).
- AR-019 (média): 1975 Metropolitano, 2 placares com 1 gol a menos (conferir com a es).

`importar.artilheiros_rsssf()` + ARTILHEIROS_CORRIGE:
- AR-027 (média): 1894 Gifford 7.
- AR-028 (média): 1934 Asociación Maseda e Tarasconi 16.
- AR-029 (média): 2025 Apertura Molina 10; 1932 Irurieta 23; 1997/98 Clausura Sosa 16.
- AR-030 (baixa): 1936 (Copa de Honor e Campeonato) e 1988/89.

`conferir.soma()` / `importar.classificacao()`:
- AR-017 (média): 1988/89 com 3/2/1 pontos (pênaltis já no banco).

### 4. Clubes e rebaixados
- AR-031 (média): `clubes_arg.py`, Atlético Cipolletti = Cipolletti.
- AR-034 (baixa): nomes colados de 1926 (CONSERTA_TEXTO na arg26; tirar a REGRA "estudiantes batigre").
- AR-021 (baixa): `importar.situacao()` por lista de rebaixados (BDFA 2012/13+, es).
- AR-032 (baixa, espera D-25): Quilmes 1893-1895.
- AR-033 (baixa, espera D-25): fusões de 1934.
- AR-043 (baixa, espera D-01): Apertura 2026.
- AR-044 (baixa, espera D-07): título de 1891.

## Uruguaio (`uru-1`) — 21 ids

### 1. Classificação e pódio (`coleta/uru-1/importar.py`, `classificacao()` e `situacao()`)
- UY-006 (alta): tabela anual (AUF 2013/14-2025; RSSSF "Tabla Anual" 1994-2012/13).
- UY-004 (alta): vice = perdedor da final; sem final, espera D-22.
- UY-005 (média): 3º sai com o UY-006.
- UY-003 (média): 1948 sem vice (edição sem campeão).
- UY-011 (média): 1951 pela tabela publicada.
- UY-001 (alta, espera D-09): `edicoes.py`, 1923 FUF, 1924 FUF e 1926.

### 2. Jogos e datas
- UY-013 (média): `edicoes.py`, Supercopa fora da "Final" (8 jogos; FIM_PADRAO).
- UY-014 (média): datas das decisões (leitor comum, mesmo conserto do AR-023).
- UY-015 (média): 2020 com o ano +1 (179 jogos; `rsssf_sul.fixa_data`).
- QU-006 (média): CONSERTA_TEXTO uru06 838/855/860, "Apr" vira "May".
- UY-023 (baixa): CONSERTA_TEXTO da final de 1996 (nome com autores no `nomes_fonte`).
- UY-010 (média): 1908, W.O. para o Bristol (`wikipedia_jogos.py` ou CORRIGE).

### 3. Artilheiros (`importar.artilheiros_rsssf()` + ARTILHEIROS_AUF)
- UY-017 (média): artilharia oficial da AUF 2013/14-2025 (12 edições).
- QU-008 (baixa): 2017 e 2023 pela AUF; divergência da es em EXPLICACOES.
- UY-018 (baixa): 1900-1931 pela coluna "Goleador" da es.
- UY-019 (baixa): 3 grafias (Castaldo 1935, Mamelli 1972, Cardoso 2005/06).

### 4. Só registrar (EXPLICACOES) e decisões
- UY-012 (baixa): tabelas sem jogos (RSSSF x es): só anotar.
- UY-016 (baixa): 31 placares (a AUF confirma o banco em 2013/14-2015/16): só anotar.
- UY-007 (média, espera D-22): vice de 1954.
- UY-008 (baixa, espera D-22): vice de 1947.
- UY-020 (média, espera D-25): "Atlético Wanderers" da FUF.

## Chileno (`chi-1`) — 26 ids

### 1. `coleta/chi-1/edicoes.py` e `ler_rsssf.py` (fases e trechos; rápido)
- CH-008 (alta): cortar antes das liguillas Pré-Sul-Americana/Libertadores; "Pre-?Sudamericana" no FIM_PADRAO.
- CH-009 (alta): fase "Desempate do título" (1997 Ap, 2013/14 Ap).
- CH-016 (média): fase "Desempate do rebaixamento" (1971, 1977).
- CH-011 (média): 2020 com `ano_fim = 2020`; depois recasar a ESPN.
- CH-012 (média): datas "First/Second Leg [..]" (leitor comum) ou da ESPN.
- CH-022 (baixa): grupos herdados (2002-2008), "Interseries" (1969-70), 5º do Provincial (1968).

### 2. Leitor comum `rsssf_sul.linha_tabela` (coluna de bônus)
- CH-001 (alta): 1979, 1981, 1982 e 1983 com o bônus antes dos pontos.

### 3. `coleta/chi-1/explicacoes.py` (CONSERTA_TEXTO e CORRIGE)
- CH-002 (alta): chile44:167, chile43:186, chile53:198, chile72:214.
- CH-013 (média): placares do ogol de 1990-1995 (transfermarkt + RSSSF + es concordam).
- CH-014 (média): 1988 jogo duplicado; 1986 adversários trocados.
- CH-007 (alta): 1985 Everton: achar os 2 jogos numa 3ª fonte; até lá, a tabela da RSSSF.

### 4. `coleta/chi-1/importar.py`, `classificacao()` e `situacao()`
- CH-003 (alta): tabela acumulada/final no lugar da 1ª fase (1954, 1955).
- CH-004 (alta): 1968 pela tabela do Nacional + desempate do 2º lugar.
- CH-005 (alta): bônus como `ajuste_pontos` na calculada (1979, 1982, 1990, 1969-70).
- CH-006 (alta): 1984 pela ordem do quadrangular final.
- CH-015 (média): punições como ajuste também na calculada; 2011 Ap "award revoked".
- CH-019 (média): tabela publicada que só não fecha por 1-2 gols vale a ordem dela (1947).
- CH-010 (alta): "rebaixado" só com "Relegated" (20 linhas erradas; 2020 U. de Concepción).
- CH-025 (baixa): Deportes Concepción fora do 2008 Clausura.
- CH-018 (média): `artilheiros_rsssf()` aceitar 1 espaço (1936, 1937, 1947); 1968 e 1998 esperam D-17.

### 5. `coleta/chi-1/outras_fontes.py`
- CH-017 (média): gol repetido da ESPN; só gravar gols que fecham com o placar.
- CH-024 (baixa): cidade "Estadio La Portada" vira "La Serena".
- CH-023 (baixa): 7 datas do ogol de 1969 casadas com jogo de outra fase.

### 6. `coleta/chi-1/baixar_ogol.py` (demorado)
- CH-028 (baixa): páginas que faltam do calendário (1964, 1971, 1977, 1982); conferir 1951-1957.

### 7. Decididos em 22/11 (antes esperavam decisão) (`clubes_chi.py` REGRAS)
- CH-020 (média, espera D-25): Green Cross x Deportes Temuco.
- CH-021 (média, espera D-25): Deportes Arica = San Marcos de Arica.

## Colombiano (`col-1`) — 22 ids

### 1. `coleta/col-1/ler_rsssf.py` + `importar.py` (baratos, alto impacto)
- CO-001 (alta): vice pela coluna "Runners Up" da colchamp (~20 linhas).
- CO-002 (alta, espera D-02): ordenar por fase alcançada mesmo com tabela publicada.
- CO-007 (alta): REBAIXADOS (Anexo da es) em `explicacoes.py`; 1997 espera D-18.
- CO-008 (média): datas "First/Second Leg [..]" (leitor comum) ou da ESPN.
- CO-011 (média): `conferir.eh_mata()` sem "Finalización"; quadrangulares como grupos.
- CO-012 (média): grupo do quadrangular pelo clube; 1ª fase sem grupo.
- CO-014 (média): "Final do Apertura/Finalización" com nível 0 (1974-1982, 1999).
- CO-017 (média): regex dos artilheiros (1971, 1977, 1978); 2008+ pela es.
- CO-016 (média): bônus das fases finais 1983-1999; Tuluá -2 em 1995.
- CO-018 (média): gols com autor só quando a soma bate.
- CO-021 (baixa): descartar as linhas "abd" repetidas.
- CO-022 (baixa): explicar as divergências em `explicacoes.py`; `esperados()` só da mesma fase.

### 2. `coleta/col-1/wikipedia_jogos.py` (custo médio)
- CO-004 (alta): ler as 4 voltas e as listas "Fecha N" (1955, 1958-1961, 1963, 1966).
- CO-005 (alta): 1964, descartar a matriz quando há lista.
- CO-006 (alta): 1989 pelas listas; 1976 e 1988 pela RSSSF; 1986 pelas tabelas da RSSSF.
- CO-010 (média): ano + 1 depois da virada (1957 final; 1971 desempate).
- CO-013 (média): 1957, octogonal cancelado e hexagonais com grupo.
- CO-009 (média): 2025 Fi, ler `{{fecha}}`; ESPN só com placar igual.
- CO-020 (baixa): datas dos títulos de rodada (1952-1988).
- CO-015 (média): 1948-1949 pela tabela de confrontos da RSSSF; 2001-2018 só com 3ª fonte.

### 3. `coleta/col-1/edicoes.py`
- CO-003 (alta): tabela final da RSSSF (1987, 1991-1995), só clubes da Primera A.
- CO-019 (baixa): `num_clubes` sai junto (1986, 1989, 1995).

## Paraguaio (`par-1`) — 24 ids

Atenção: o `painel/dados/par-1.js` local piora o site (PY-022). Publicar só depois deste bloco.

### 1. `coleta/par-1/importar.py` (custo baixo, efeito maior)
- PY-001 (alta): campeão da lista sempre em 1º (o painel também muda: plano do banco e painel).
- PY-002 (alta): vice da lista sempre em 2º (23 edições); anos de vice duplo esperam D-22.
- PY-011 (alta): "Relegation Playoff" não é queda (1967, 1994).
- PY-012 (média): lista REBAIXADOS por ano (RSSSF + es).
- PY-018 (média): artilheiros 2014-2025 ("Topscorers" ou es).
- PY-020 (baixa): gols da ESPN só quando a soma bate (2007).
- PY-025 (baixa): nomes de estádio sem patrocinador ("ueno", "Tigo").

### 2. `coleta/par-1/ler_rsssf.py` (custo médio)
- PY-003 (alta): `tabela_parcial()` aceita linha sem número (36 edições).
- PY-008 (média): TORNEIOS/FECHA do Apertura e Clausura 1996-2007; finais próprias.
- PY-006 (média): "Playoff against 11th Place" = desempate do rebaixamento (1961, 1963).
- PY-010 (média): `_vitoria_dada()` aceita "awarded as a win to" (1960).
- PY-009 (média): data no título da fase (leitor comum) ou ESPN de 2005 em diante.

### 3. `coleta/par-1/edicoes.py` (custo baixo)
- PY-005 (alta): linha inicial do campeonato em 1962-1966 (tira 152 jogos).
- PY-007 (média): tirar a final da Intermedia de 2005 e os playoffs de vaga (2000, 2004, 2005).
- PY-004 (alta): 1982-1995, tabela acumulada/final por ano; 1989 com leitor próprio.
- PY-027 (baixa, espera D-01): Apertura 2026.

### 4. `coleta/par-1/clubes_par.py`
- PY-015 (baixa): 8 de Diciembre em Caaguazú.
- PY-013 (média, espera D-25): Pettirossi de Encarnación.
- PY-014 (média, espera D-25): Cerro Porteño PF.

### 5. `coleta/par-1/explicacoes.py`
- PY-019 (média): artilheiros divergentes (1935, 1962, 1963, 1967, 1970, 2003): conferir e registrar.
- PY-029 (baixa): CONSERTA_TEXTO da nota quebrada de 2005.
- PY-021 (baixa): descartar jogador "2"/"22" da ESPN.
- PY-028 (média, espera D-22): vice nos anos de vice duplo.

### 6. `coleta/comum-sulamerica/documentar.py` e `importar.relatorio()`
- PY-031 (baixa): textos da ficha ("completa em 1990-1995", "menos jogos").

## Peruano (`per-1`) — 22 ids

Não está no site. Corrigir as altas antes de publicar.

### 1. `coleta/per-1/importar.py` (4 altas)
- PE-008 (alta): preferir a tabela acumulada do ano (1998, 2000, 2001, 2004, 2005, 2009, 2012).
- PE-002 (alta): anos sem jogos com grupo final + grupo do rebaixamento (1970-1979).
- PE-003 (alta): "rebaixado" só com "Relegated" explícito.
- PE-006 (alta): 2021, tabela anual com descontos e TAS; Carlos Stein fora.
- PE-015 (média): artilheiro de 1996 (Czornomaz e Sáenz, 20).
- PE-019 (média, espera D-06): 1912-1921 com a ordem completa.

### 2. `coleta/per-1/explicacoes.py`
- PE-004 (alta): 2020, TABELAS_FORA da 1ª tabela anual (pré-TAS).
- PE-007 (média): 2021 Cusco x Cienciano 2-2 (TAS).
- PE-014 (média): REBAIXADOS por ano (~45 edições, es).
- PE-018 (média): 2022, conferir +2 Alianza, +1 Ayacucho e Vallejo -2/-3.
- PE-016 (baixa): registrar o critério dos artilheiros.
- PE-017 (média): placares só com 3ª fonte (dechalaca, transfermarkt).

### 3. `coleta/per-1/edicoes.py`
- PE-005 (alta): 2021, trecho até "Finals" (os 2 jogos da final).
- PE-023 (baixa): textos de 1912-1921 e "Ainda não carregado" (também `documentar.py`).

### 4. `coleta/per-1/ler_rsssf.py` (FASES, TORNEIOS, ano)
- PE-013 (média): "Final do Torneo de Verano" (2017, 2018).
- PE-010 (média): 1990, janeiro depois de dezembro = ano seguinte.
- PE-011 (média): 1987/1988 "Regional Final" como fase própria.
- PE-012 (média): 1988, liguilla final separada da "Final".

### 5. Leitor comum + `outras_fontes.py`
- PE-009 (média): data no título da fase; com ESPN casada, data local da ESPN.

### 6. `coleta/per-1/clubes_per.py`
- PE-001 (alta): "Jorge Chávez" sem número = o do Callao (vice 1918 e 1921).
- PE-021 (baixa): Sporting Tabaco em Lima.
- PE-022 (baixa): cidade do Deportivo Bancos.

## Equatoriano (`ecu-1`) — 18 ids

Não está no site. Corrigir antes de publicar.

### 1. `coleta/ecu-1/importar.py`
- EC-001 (alta, espera D-02): classificação = soma de todos os jogos, ordem da última fase.
- EC-002 (alta, espera D-02): mesma regra na calculada.
- EC-004 (alta): REBAIXADOS (lista do achado); 1970-1981 espera D-18.
- EC-005 (alta): 2025, rebaixados El Nacional (-9) e Vinotinto.
- EC-016 (baixa): ordenar fases pela data do 1º jogo.
- EC-013 (média): gols da ESPN só quando a soma bate (2007).
- EC-014 (média): artilheiros 1988, 1996, 1999: 3ª fonte antes.

### 2. `coleta/ecu-1/ler_rsssf.py`
- EC-009 (média): data do título do bloco ("First Leg [Dec 17]"); recasar a ESPN.
- EC-003 (alta): fases "Disputa do 3º/4º lugar" (pode fazer já; a ordem final espera D-02).
- EC-010 (média): virada de ano (1997) e "Relegation Group".

### 3. `coleta/ecu-1/explicacoes.py`
- EC-006 (média): 1999 "Liguilla No Descenso".
- EC-007 (média): 1963, 1966 e 1997 "Final" vira fase de liga.
- EC-008 (média): descartar 20 jogos repetidos (1984, 1986, 1994); aviso no `conferir.py`.
- EC-011 (média): 2005 Emelec 2-2 LDU.
- EC-012 (média): 1965, 4 jogos awd do Aucas.
- EC-017 (baixa): 2006 Barcelona x LDU em 29/10; 1988 conferir.
- EC-024 (baixa): data 1969-10-26 no 0-11 da LDU.
- EC-015 (média, espera D-20): El Nacional x Delfín 2025.

## Decididas pelo Guilherme em 22/11 (já podem ser corrigidas)

Resposta: a recomendação de cada uma em `decisoes-guilherme.md`, menos a D-01, que ficou com a opção A: tudo o que
já terminou entra agora, inclusive os Aperturas 2026 da Argentina e do Paraguai. A D-10 ficou com a opção B (edições não oficiais com aviso).


- D-01 (edições de 2026): AR-043, PY-027.
- D-02 (ordem final com fase final): CO-002, EC-001, EC-002 (e a ordem do EC-003).
- D-06 (Peru 1912-1921): PE-019.
- D-07 (títulos divididos): AR-044.
- D-09 (títulos que a federação não reconhece): UY-001.
- D-17 (artilheiros em dúvida): CH-018 (só 1968 e 1998).
- D-18 (rebaixados fora do padrão): CO-007 (só 1997), EC-004 (só 1970-1981).
- D-20 (tribunal): EC-015.
- D-22 (vices em dúvida): PY-028, UY-004 (só 2011/12 e 2021), UY-007, UY-008.
- D-25 (identidade de clubes, América do Sul): AR-032, AR-033, CH-020, CH-021, PY-013, PY-014, UY-020.

## Fontes novas a usar

Detalhes em `docs/revisao/fontes.md`.
- RSSSF (partes que a coleta não leu): colchamp "Runners Up", chilehist (RELEGATED, bônus), "Final Table" antigas,
  peru1912-1921, datas "First Leg [..]".
- Wikipédia es: vices, 3º e 4º, rebaixados por ano (Ascensos y descensos), artilheiros, tabelas acumuladas.
- AUF (auf.org.uy): tabela anual, decisões, Supercopa e artilharia oficial 2013/14-2025.
- historiadeboca.com.ar: datas das rodadas antigas da Argentina e jogos do Boca que faltam.
- BDFA: rebaixados da Argentina 2012/13-2021.
- ESPN (já baixada): datas dos mata-matas e jogos adiados.
- Transfermarkt: 3ª opinião de placar (Chile 1990-1995) e árbitro/público (fichas).
- footballdatabase.eu: só para o que nenhuma outra cobre (Uruguai e Equador antigos; limite de 50 páginas por dia).

Cobre 174 de 174 ids abertos de `coleta-sulamerica` no `achados.csv` (22/11/2026; os fechados na conferência final estão riscados).
