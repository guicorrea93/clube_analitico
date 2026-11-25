# Campeonato Mineiro (`bra-mg-1`) — documentação

Gerado por `python coleta/comum/documentar.py` a partir do pacote `data/coleta/bra-mg-1/pacote/` e dos módulos de `coleta/bra-mg-1/`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/bra-mg-1.md`.

## 1. O que temos

- **Edições:** 113, de 1915 a 2026.
- **Jogos:** 11521; **gols:** 31081; **gols com autor:** 24324 (78%); **cartões:** 0.
- **Clubes:** 96; **artilheiros:** 111 temporadas com artilheiro (122 linhas, com empates).
- **Classificação final:** 113 temporadas; **rodada a rodada:** 49 temporadas.
- **Tabelas publicadas guardadas para conferência:** 4045 linhas.
- **No banco (`db/futebol.db`):** sim (113 edições, 11521 jogos).
- **Observação da competição:** 1ª divisão de Minas Gerais, de 1915 a 2026 (até os anos 1940 com os clubes de Belo Horizonte e arredores). Em 1932 houve duas ligas, e a FMF reconhece os dois títulos: cada torneio é uma edição ("1932 LMDT" e "1932 AMEG"). 1956 teve título dividido (Atlético e Cruzeiro).

## 2. Fontes e regras

**Temporadas:** 1915 a 2026. Até os anos 1940 é o campeonato dos clubes de Belo Horizonte e arredores; o interior entra aos poucos (1958-1959 com os torneios de classificação; de 1970 em diante, o campeonato estadual). Em 1932 houve duas ligas e a FMF reconhece os dois títulos: cada torneio é uma edição ("1932 LMDT" e "1932 AMEG"). 1956 teve título dividido (Atlético e Cruzeiro). 1925 é a edição que a liga considerou inexistente na época e a FMF homologou em 2012 (campeão o América). Em 2002 Atlético, Cruzeiro e América (Copa Sul-Minas) não jogaram; o campeão foi a Caldense.

**Fontes:** RSSSF Brasil (`tablesfq/mg{ano}.htm`: jogos, fases, datas, autores e tabelas; `mg1926l.htm`, `mg1932l.htm` e `mg1932a.htm` com a letra da liga); ogol (calendário de cada edição e o código de cada clube; confere placares, traz a rodada e completa os jogos que a página não traz); Wikipédia em português (artigo do Campeonato Mineiro: tabela de resultados ano a ano, segunda fonte do campeão e do vice). Artilheiros pela lista da RSSSF (`mgtops.htm`).

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela, fica a da RSSSF. W.O. conta como vitória sem gols (decisão D-15). Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` ou nos outros pacotes usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF): 285 tabelas fecham com os jogos e 196 divergem (cada divergência é explicada no relatório, na temporada).
- Temporadas com alguma tabela divergente: 1915, 1918, 1919, 1922, 1923, 1926, 1927, 1928, 1929, 1930, 1931, 1932 LMDT, 1932 AMEG, 1936, 1937, 1938, 1939, 1940, 1941, 1944, 1945, 1946, 1947, 1948, 1949, 1952, 1954, 1955, 1956, 1957, 1958, 1960, 1961, 1963, 1965, 1966, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1993, 1996, 1999, 2000, 2001, 2003, 2004, 2009, 2016, 2018, 2020, 2022, 2023, 2024, 2026.
- Temporadas sem tabela para conferir: 1925, 1933.
- Temporadas com menos jogos do que o ogol: 1923 (19 de 21), 1926 (31 de 36), 1927 (58 de 59), 1930 (42 de 52), 1931 (24 de 55), 1936 (9 de 36), 1939 (44 de 45), 1940 (23 de 30), 1942 (30 de 36), 1976 (189 de 251), 1982 (200 de 201), 2020 (72 de 75), 2021 (72 de 75), 2022 (73 de 78), 2023 (59 de 66), 2024 (60 de 66), 2025 (54 de 60), 2026 (53 de 59).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|
| 1910s | 85 | 100% | 0% | 0% | 0% | 0% | 0% | 61% | 0.0 |
| 1920s | 377 | 100% | 2% | 0% | 0% | 0% | 0% | 62% | 0.0 |
| 1930s | 429 | 100% | 0% | 10% | 0% | 0% | 0% | 83% | 0.0 |
| 1940s | 474 | 100% | 0% | 0% | 0% | 0% | 0% | 94% | 0.0 |
| 1950s | 1026 | 100% | 0% | 5% | 0% | 0% | 0% | 96% | 0.0 |
| 1960s | 1594 | 100% | 0% | 25% | 0% | 0% | 0% | 97% | 0.0 |
| 1970s | 1732 | 100% | 0% | 87% | 0% | 0% | 0% | 93% | 0.0 |
| 1980s | 1998 | 100% | 1% | 62% | 0% | 0% | 0% | 66% | 0.0 |
| 1990s | 1822 | 100% | 1% | 83% | 0% | 0% | 0% | 16% | 0.0 |
| 2000s | 805 | 100% | 75% | 73% | 0% | 0% | 7% | 98% | 0.0 |
| 2010s | 736 | 100% | 100% | 90% | 0% | 0% | 0% | 96% | 0.0 |
| 2020s | 443 | 100% | 100% | 88% | 0% | 0% | 0% | 98% | 0.0 |

**Fonte de cada jogo:** RSSSF Brasil: 11503; ogol: 18.

## 5. Formato ao longo do tempo

**Número de clubes:**

- 1915: 5 clubes
- 1916: 6 clubes
- 1917 a 1918: 5 clubes
- 1919: 4 clubes
- 1920: 6 clubes
- 1921: 12 clubes
- 1922 a 1923: 7 clubes
- 1924: 5 clubes
- 1925 a 1926: 6 clubes
- 1927: 11 clubes
- 1928: 9 clubes
- 1929: 10 clubes
- 1930 a 1931: 7 clubes
- 1932 LMDT: 8 clubes
- 1932 AMEG: 6 clubes
- 1933: 9 clubes
- 1934: 8 clubes
- 1935: 6 clubes
- 1936: 3 clubes
- 1937 a 1939: 6 clubes
- 1940: 5 clubes
- 1941: 7 clubes
- 1942 a 1944: 6 clubes
- 1945 a 1950: 7 clubes
- 1951: 8 clubes
- 1952: 9 clubes
- 1953: 10 clubes
- 1954 a 1955: 9 clubes
- 1956 a 1957: 10 clubes
- 1958: 16 clubes
- 1959: 17 clubes
- 1960: 16 clubes
- 1961: 14 clubes
- 1962 a 1968: 12 clubes
- 1969: 16 clubes
- 1970: 28 clubes
- 1971: 21 clubes
- 1972: 20 clubes
- 1973: 16 clubes
- 1974: 14 clubes
- 1975: 16 clubes
- 1976: 23 clubes
- 1977 a 1978: 12 clubes
- 1979: 16 clubes
- 1980: 21 clubes
- 1981 a 1983: 12 clubes
- 1984 a 1985: 14 clubes
- 1986 a 1988: 16 clubes
- 1989: 17 clubes
- 1990: 18 clubes
- 1991 a 1992: 24 clubes
- 1993: 23 clubes
- 1994 a 1995: 12 clubes
- 1996: 13 clubes
- 1997 a 2001: 12 clubes
- 2002: 8 clubes
- 2003: 13 clubes
- 2004: 14 clubes
- 2005 a 2026: 12 clubes

**Pontos por vitória:**

- 1915 a 1994: 2
- 1995 a 2026: 3

**Nome oficial:**

- 1915 a 1931: Campeonato Mineiro
- 1932 LMDT: Campeonato Mineiro (LMDT)
- 1932 AMEG: Campeonato Mineiro (AMEG)
- 1933 a 2026: Campeonato Mineiro

**Formato de cada edição** (fases na ordem; grupos; mata-mata):

- 1915 a 1919: pontos corridos
- 1920 a 1922: pontos corridos + mata-mata
- 1923 a 1930: pontos corridos
- 1931: pontos corridos + mata-mata
- 1932 LMDT a 1933: pontos corridos
- 1934: pontos corridos + mata-mata
- 1935 a 1936: pontos corridos
- 1937: pontos corridos + mata-mata
- 1938 a 1939: pontos corridos
- 1940 a 1941: pontos corridos + mata-mata
- 1942 a 1950: pontos corridos
- 1951: pontos corridos + mata-mata
- 1952: pontos corridos + mata-mata + pontos corridos
- 1953: pontos corridos + mata-mata
- 1954: pontos corridos + mata-mata + pontos corridos + mata-mata + pontos corridos + mata-mata
- 1955: pontos corridos + mata-mata + pontos corridos
- 1956: pontos corridos + mata-mata + pontos corridos + mata-mata
- 1957: pontos corridos + mata-mata
- 1958: pontos corridos + mata-mata + pontos corridos + mata-mata
- 1959: 3 grupos + mata-mata + pontos corridos
- 1960: pontos corridos
- 1961 a 1962: pontos corridos + mata-mata
- 1963 a 1966: pontos corridos
- 1967: pontos corridos + mata-mata
- 1968 a 1969: pontos corridos
- 1970: 3 grupos + pontos corridos
- 1971: 4 grupos + mata-mata + pontos corridos
- 1972: 3 grupos + pontos corridos + 2 grupos + pontos corridos + mata-mata
- 1973: 2 grupos + mata-mata + 2 grupos + pontos corridos
- 1974: 2 grupos + pontos corridos
- 1975: pontos corridos + mata-mata + 2 grupos + pontos corridos
- 1976: 2 grupos + mata-mata + 2 grupos + mata-mata + pontos corridos + mata-mata
- 1977: pontos corridos + mata-mata
- 1978: pontos corridos
- 1979: pontos corridos + mata-mata + pontos corridos
- 1980: 3 grupos + pontos corridos
- 1981 a 1982: pontos corridos
- 1983: pontos corridos + mata-mata + pontos corridos
- 1984: pontos corridos + mata-mata + pontos corridos + mata-mata
- 1985: pontos corridos + mata-mata
- 1986: pontos corridos
- 1987: pontos corridos + mata-mata
- 1988: pontos corridos
- 1989: 2 grupos + pontos corridos
- 1990: pontos corridos + mata-mata
- 1991: 3 grupos + pontos corridos
- 1992: 3 grupos + mata-mata
- 1993: 3 grupos + pontos corridos
- 1994 a 1996: pontos corridos
- 1997 a 2000: pontos corridos + mata-mata
- 2001: pontos corridos + 2 grupos + mata-mata
- 2002 a 2003: pontos corridos
- 2004 a 2014: pontos corridos + mata-mata
- 2015: pontos corridos
- 2016 a 2026: pontos corridos + mata-mata

**Fases que aparecem** (número de temporadas): Primeira fase (70); Final (48); Fase única (37); Segunda fase (29); Semifinal (26); Fase final (18); Fase classificatória (7); Primeira fase - Desempate (6); Torneio de rebaixamento (6); Quartas de final (6); Fase classificatória - Desempate (5); 1º Turno (5); Segunda fase - Desempate (4); 1º Turno - Final (4); 2º Turno (4); 1º Turno - Semifinal (3); 2º Turno - Final (3); Terceira fase (2); Primeira fase - Final (1); 2º Turno - Semifinal (1); Disputa do 3º lugar (1).

**Observações das edições:**

- 1925: campeonato de poucos jogos (4 na RSSSF), considerado inexistente pela liga em dezembro de 1925; a FMF homologou o título do América em 2012; sem vice
- 1932 LMDT: torneio da LMDT (Liga Mineira de Desportos Terrestres); no mesmo ano a AMEG fez o seu ("1932 AMEG"), e a FMF reconhece os dois campeões
- 1932 AMEG: torneio da AMEG (Associação Mineira de Esportes Gerais); no mesmo ano a LMDT fez o seu ("1932 LMDT"), e a FMF reconhece os dois campeões
- 1956: título dividido entre Atlético e Cruzeiro (D-07); sem vice
- 2002: Atlético, Cruzeiro e América (os clubes mineiros da Copa Sul-Minas) não jogaram o campeonato

## 6. Campeões, acessos, rebaixados e punições

**Títulos:**

- Atlético-MG: 50
- Cruzeiro: 38
- América-MG: 16
- Villa Nova-MG: 5
- Siderúrgica: 2
- Caldense: 1
- Ipatinga: 1

**Acessos:** nenhum marcado no pacote.

**Rebaixamentos:** 121 no total; quem mais teve: Guarani-MG (8), Democrata-GV (8), Uberlândia (7), Caldense (6), Valeriodoce (5), Democrata-SL (5), Villa Nova-MG (5), Nacional Uberaba (4).

**Punições em pontos:**

- nenhuma

## 7. Correções e decisões (com o motivo)

Registradas nos módulos de `coleta/bra-mg-1/`; cada uma também aparece no relatório, na temporada.

### Observações das edições (`importar.OBS_EDICAO`)

- **1932 LMDT:** torneio da LMDT (Liga Mineira de Desportos Terrestres); no mesmo ano a AMEG fez o seu ("1932 AMEG"), e a FMF reconhece os dois campeões
- **1932 AMEG:** torneio da AMEG (Associação Mineira de Esportes Gerais); no mesmo ano a LMDT fez o seu ("1932 LMDT"), e a FMF reconhece os dois campeões
- **1925:** campeonato de poucos jogos (4 na RSSSF), considerado inexistente pela liga em dezembro de 1925; a FMF homologou o título do América em 2012; sem vice
- **1956:** título dividido entre Atlético e Cruzeiro (D-07); sem vice
- **2002:** Atlético, Cruzeiro e América (os clubes mineiros da Copa Sul-Minas) não jogaram o campeonato

### Clube trocado pelo ogol numa temporada (código -> código) (`importar.CORRIGE_OGOL`)

- **1959 · 94588:** [241728] Pedro Leopoldo FC: a RSSSF lista o Pedro Leopoldo Futebol Clube; o ogol usa a ficha da AE Pedro Leopoldo
- **1960 · 94588:** [241728] Pedro Leopoldo FC: a RSSSF lista o Pedro Leopoldo Futebol Clube; o ogol usa a ficha da AE Pedro Leopoldo
- **1961 · 94588:** [241728] Pedro Leopoldo FC: a RSSSF lista o Pedro Leopoldo Futebol Clube; o ogol usa a ficha da AE Pedro Leopoldo
- **1962 · 94588:** [241728] Pedro Leopoldo FC: a RSSSF lista o Pedro Leopoldo Futebol Clube; o ogol usa a ficha da AE Pedro Leopoldo
- **1963 · 94588:** [241728] Pedro Leopoldo FC: a RSSSF lista o Pedro Leopoldo Futebol Clube; o ogol usa a ficha da AE Pedro Leopoldo
- **1973 · 55393:** [72165] Flamengo Futebol Clube (RSSSF, 1973); a ficha que o ogol usa é a do Flamengo EC, fundado em 1979
- **1990 · 72165:** [55393] Flamengo Esporte Clube (RSSSF, 1990): o ogol usa as duas fichas na mesma edição

### Nome da página casado à mão com o clube (`importar.NOME_MANUAL`)

- **1921 · Cristóvão Colombo:** [259237] Sport Club Christovam Colombo, o mesmo de 1915-1917 no ogol (o torneio eliminatório de 1921 não está no ogol)
- **1921 · Palmeiras:** [99077] Palmeiras FBC, de Belo Horizonte, o mesmo de 1923-1930 no ogol (o torneio eliminatório de 1921 não está no ogol; virava um segundo cadastro "Palmeiras-MG")
- **1921 · Progresso:** [259266] Progresso Foot Ball Club, o mesmo de 1922 no ogol (Progresso-BH)
- **1925 · Sport Calafate:** [99078] Sport Club Calafate, o Calafate de 1926-1932 no ogol (1925 não tem edição no ogol)

### Jogos anulados (`importar.JOGOS_ANULADOS`)

- **1923 · América · Yale · 10 · 0:** 2º turno: uma assembleia geral anulou todos os jogos do 2º turno e deu o título ao América, vencedor do 1º (a página marca os outros jogos "[annulled]", este não)

### Clubes com todos os jogos fora (`importar.RSSSF_FORA`)

- **1936 · Palestra Itália:** abandonou a liga em 28/10/1936, antes do 3º turno; todos os jogos dele foram cancelados e não contam (RSSSF: a tabela final o traz com 0 jogos)
- **1936 · América:** abandonou a liga em 28/10/1936, antes do 3º turno; todos os jogos dele foram cancelados e não contam (RSSSF: a tabela final o traz com 0 jogos)
- **1936 · Villa Nova:** abandonou a liga em 28/10/1936, antes do 3º turno; todos os jogos dele foram cancelados e não contam (RSSSF: a tabela final o traz com 0 jogos)

### Fases da página renomeadas (por temporada) (`rsssf_mg1.FASE_ANO`)

- **1920:** Second place tiebreak → Primeira fase - Desempate
- **1921:** Final qualifiers → Fase classificatória
- **1922:** League tiebreak → Final
- **1941:** THIRD STAGE → Segunda fase; TIEBREAK PLAYOFFS → Final
- **1952:** Tie-breaking for First Stage → Primeira fase - Desempate
- **1954:** Tiebreak playoff → Primeira fase - Desempate; THIRD STAGE → Terceira fase; Tie-breaking → Segunda fase - Desempate
- **1955:** Tiebreaking playoff → Primeira fase - Desempate; THIRD STAGE - all matches in Belo Horizonte → Terceira fase
- **1956:** Tie-breaking matches → Primeira fase - Desempate
- **1957:** Tiebreak playoff → Segunda fase - Desempate
- **1958:** Qualification Stage Tiebreak → Fase classificatória - Desempate; Second stage tiebreak → Segunda fase - Desempate
- **1959:** "Sertão" Zone Tiebreaking Playoff → Fase classificatória - Desempate; Metallurgic Zone Tiebreaking Playoff → Fase classificatória - Desempate
- **1961:** Tiebreak playoffs (at neutral venues) → Primeira fase - Desempate; Tiebreak (neutral venue) → Torneio de rebaixamento
- **1971:** Play-Off → Fase classificatória - Desempate
- **1972:** Play-off Tournament → Fase classificatória - Desempate; Tiebreak → Fase classificatória - Desempate
- **1973:** Play-off matches → Fase classificatória - Desempate; Semifinal Phase → Segunda fase
- **1974:** Qualifying Phase → Primeira fase; Semifinal Phase → Segunda fase
- **1975:** FIRST STAGE → 1º Turno; Stage finals → 1º Turno - Final
- **1976:** First Phase → 1º Turno; Semifinal → 1º Turno - Semifinal; Final → 1º Turno - Final; First Stage → 2º Turno; First Stage Finals → 2º Turno - Final; Second Stage → Segunda fase; Final Phase → Fase final; Championship Finals → Final
- **1979:** Tie-breaking match of 2nd Stage → Segunda fase - Desempate
- **1983:** First Stage → 1º Turno; Second Stage → 2º Turno; 2nd Stage Tie-breaking → 2º Turno - Final; 1st Phase Finals → Primeira fase - Final
- **1987:** FIRST STAGE → 1º Turno; Semifinals → 1º Turno - Semifinal; Final → 1º Turno - Final; SECOND STAGE → 2º Turno; FINALS → Final

### Ocorrências explicadas, por temporada (`explicacoes.EXPLICACOES`)

- **1956:** título dividido entre Atlético e Cruzeiro: o pacote tem o Atlético em campeao, o Cruzeiro em co_campeao e o vice vazio (D-07, como o Carioca 1907 e o Paulista 1973)
- **1976:** Torneios Paralelos I, II e III: consolação para os 11 clubes que não foram à Taça Governador do Estado; ficam fora (rsssf_mg1.ANOS_A_PARTE), como os torneios à parte do Carioca
- **2020:** Troféu Inconfidência (do 5º ao 8º da 1ª fase): torneio à parte, fica fora; o calendário do ogol traz os jogos dele junto com os do campeonato (rsssf_mg1.ANOS_A_PARTE)
- **2021:** Troféu Inconfidência (do 5º ao 8º da 1ª fase): torneio à parte, fica fora; o calendário do ogol traz os jogos dele junto com os do campeonato (rsssf_mg1.ANOS_A_PARTE)
- **2022:** Troféu Inconfidência (do 5º ao 8º da 1ª fase): torneio à parte, fica fora; o calendário do ogol traz os jogos dele junto com os do campeonato (rsssf_mg1.ANOS_A_PARTE)
- **2023:** Troféu Inconfidência (do 5º ao 8º da 1ª fase): torneio à parte, fica fora; o calendário do ogol traz os jogos dele junto com os do campeonato (rsssf_mg1.ANOS_A_PARTE)
- **2024:** Troféu Inconfidência (do 5º ao 8º da 1ª fase): torneio à parte, fica fora; o calendário do ogol traz os jogos dele junto com os do campeonato (rsssf_mg1.ANOS_A_PARTE)
- **2025:** Troféu Inconfidência (do 5º ao 8º da 1ª fase): torneio à parte, fica fora; o calendário do ogol traz os jogos dele junto com os do campeonato (rsssf_mg1.ANOS_A_PARTE)
- **2026:** Troféu Inconfidência (do 5º ao 8º da 1ª fase): torneio à parte, fica fora; o calendário do ogol traz os jogos dele junto com os do campeonato (rsssf_mg1.ANOS_A_PARTE)

### Clube do ogol casado à mão com o nome do banco (`clubes_mg1.MANUAL_DB`)

- **3333:** [J.Malucelli] o ogol escreve 'JMalucelli'; é o J. Malucelli do banco (Série A 2000)
- **24836:** [Novorizontino] Grêmio Novorizontino (2010-); o banco separou o GE Novorizontino (1973-1999) em 20/11/2026

### Nome de exibição de clube novo, dado à mão (`clubes_mg1.MANUAL_NOVO`)

- **68358:** [Corinthians Prudente] EC Corinthians de Presidente Prudente (1996): não é o Corinthians paulistano do banco
- **45210:** [Maringá] Maringá FC fundado em 2010 (Copa do Brasil 2025): não é o GE Maringá do banco
- **241210:** [Maringá FC 1995] Maringá FC fundado em 1995 (Copa do Brasil 1997): outro clube, nome como no ogol
- **60858:** [GE Novorizontino] Grêmio Esportivo Novorizontino (1973-1999, campeão de 1994): outro clube; o 'Novorizontino' do banco fica com o Grêmio Novorizontino, fundado em 2010 (decisão do Guilherme, 20/11/2026)
- **20122:** [Linhares EC] dois clubes de Linhares-ES: o EC (anos 1990) e o FC (anos 2000); o sufixo já distingue
- **9783:** [Linhares FC] dois clubes de Linhares-ES: o EC (anos 1990) e o FC (anos 2000); o sufixo já distingue

### Anos com torneio à parte na página (fica fora) (`rsssf_mg1.ANOS_A_PARTE`)

- 1976, 2020, 2021, 2022, 2023, 2024, 2025, 2026

### Letras trocadas na página da RSSSF (`rsssf_mg1.LETRAS`)

- **Atl�tico:** Atlético
- **Am�rica:** América
- **It�lia:** Itália
- **Hygi�nicos:** Hygiênicos
- **S�o:** São
- **Sider�rgica:** Siderúrgica
- **Uni�o:** União
- **Uberl�ndia:** Uberlândia
- **Valeriodoce:** Valeriodoce

### Edições sem vice (`importar.SEM_VICE`)

- **1925:** campeonato de poucos jogos, considerado inexistente pela liga em dezembro de 1925; a FMF homologou o título do América em 2012, sem vice (RSSSF e Wikipédia: "não houve")

### Títulos divididos (D-07) (`importar.CAMPEOES_DIVIDIDOS`)

- **1956:** Atlético-MG / Cruzeiro

### Páginas da RSSSF corrigidas na leitura (`rsssf.CORRECOES`, registradas em `coleta/bra-mg-1/rsssf_*.py`)

- **mg1915.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1916.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1917.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1918.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1919.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1920.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1921.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou); a liga depois do torneio eliminatório (sem título de fase na página)
- **mg1922.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1923.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1924.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1925.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1926l.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1927.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1928.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1929.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1930.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1931.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1932a.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1932l.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1933.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1934.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1935.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1936.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1937.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1938.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1939.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1940.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1941.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1942.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1943.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1944.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1945.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1946.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1947.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1948.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1949.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1950.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1951.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou); 1º turno: a linha do Villa Nova traz 6 vitórias (6 + 1 + 1 = 8 jogos em 7); com 11 pontos e 1 empate são 5
- **mg1952.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1953.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1954.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1955.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou); o 2º turno começa em outubro de 1955 (a data de cima é a de um desempate jogado em abril de 1956)
- **mg1956.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1957.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1958.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1959.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou); a zona metalúrgica é outra chave do torneio de classificação (vinha depois do desempate da zona do sertão)
- **mg1960.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1961.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1962.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1963.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1964.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1965.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1966.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1967.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1968.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1969.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1970.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1971.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1972.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou); a chave C é do torneio de classificação (vinha depois do desempate da chave B)
- **mg1973.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou); a 1ª fase é de 1973 (o torneio de classificação, logo acima, terminou em dezembro de 1972); a data numérica fixa o ano sem a virada de dezembro para março
- **mg1974.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1975.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1976.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1977.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1978.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1979.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1980.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1981.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1982.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou); a fase final é de outubro de 1982 (a repescagem, listada antes, é de fevereiro de 1983)
- **mg1983.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou); 1º turno: a linha do Atlético traz 2 derrotas (7 + 3 + 2 = 12 jogos em 11); com 17 pontos é 1 derrota
- **mg1984.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou); dois turnos com subfases de mesmo nome
- **mg1985.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1986.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1987.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1988.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1989.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1990.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1991.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1992.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1993.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1994.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1995.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1996.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1997.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1998.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg1999.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2000.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2001.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2002.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2003.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2004.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2005.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou); semifinal: a página escreve "URT 0-4 URT"; o adversário era o Ipatinga (ogol; volta Ipatinga 2-2 URT)
- **mg2006.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2007.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2008.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2009.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2010.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2011.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2012.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2013.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2014.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2015.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2016.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2017.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2018.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2019.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2020.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2021.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou); 1ª rodada: "Feb 29" não existe em 2021; o ogol dá 27/02/2021 para os três jogos
- **mg2022.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2023.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2024.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2025.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)
- **mg2026.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; placar com travessão ("1–2"); frase ("X are qualified ..."), não título de fase; público "Att: 535" (o leitor comum lê "att:"); linha de tabela de clube empatado sem o número da posição; "A bt B": vitória do A, placar desconhecido; W.O. "1-WO" / "WO-1" (o WO marca quem faltou)

## 8. O que não deu para coletar

- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).
- **Autores dos gols:** só entram quando a soma bate com o placar.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;
  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.

## 9. Pendências e próximos passos

- 196 tabelas divergentes a explicar no relatório. Boa parte não é erro de jogo: a tabela publicada conta o W.O. com gols (D-15: sem gols), traz um turno por tabela quando a página junta os jogos (1983-1987), ou erra a soma (RSSSF e ogol com os mesmos placares).
- Vices em que as fontes discordam: 1934 (pacote Tupynambás, que perdeu a final estadual; RSSSF Palestra Itália; Wikipédia Tupynambás no estadual e Atlético na cidade), 1942 (RSSSF América; Wikipédia e pacote Palestra Mineiro, o Cruzeiro) e 1950 (RSSSF Cruzeiro; Wikipédia e pacote Siderúrgica).
- 1924 e 1925 incompletos na própria fonte (1924: "Incomplete scores"; 1925: 4 jogos, campeonato anulado na época e título homologado pela FMF em 2012). Pontos extras de 1975 (Atlético e Cruzeiro, +1 na fase final) não entram na classificação calculada.
- Autores dos gols: 24.324 de 31.081; cartões: só jogo a jogo, pela ficha do ogol (prioridade baixa).

## 10. Arquivos e comandos

| Arquivo | O que faz |
|---|---|
| `coleta/bra-mg-1/baixar_ogol.py` | Baixa o calendário de cada edição do Campeonato Mineiro no ogol para data/coleta/bra-mg-1/ogol/mg1_{temporada}.json e a ficha de cada clube para data/coleta/bra-mg-1/ogol/clubes.json. |
| `coleta/bra-mg-1/baixar_rsssf.py` | Baixa as páginas do Campeonato Mineiro da RSSSF Brasil para data/coleta/bra-mg-1/rsssfbrasil/. |
| `coleta/bra-mg-1/baixar_wiki.py` | Baixa o código do artigo "Campeonato Mineiro de Futebol" da Wikipédia em português para data/coleta/bra-mg-1/wikipedia/pt_lista.txt (a lista de campeões ano a ano, segunda fonte do campeão). |
| `coleta/bra-mg-1/clubes_mg1.py` | Identidade dos clubes do Campeonato Mineiro (mesmo método do Paulista, coleta/bra-sp-1/clubes_sp1.py; clube já nomeado em outra coleta usa o mesmo nome, pelo cadastro comum data/coleta/comum/clubes_ogol.json). |
| `coleta/bra-mg-1/edicoes.py` | Edições do Campeonato Mineiro (1ª divisão, `bra-mg-1`): temporadas, anos e nomes oficiais. |
| `coleta/bra-mg-1/explicacoes.py` | Textos do relatório do Campeonato Mineiro (1ª divisão) que não saem do código: introdução, explicações de cada temporada e o fim. |
| `coleta/bra-mg-1/importar.py` | Junta as fontes do Campeonato Mineiro (1ª divisão) e grava o pacote em data/coleta/bra-mg-1/pacote/ e o relatório em docs/coleta/bra-mg-1.md. Mesmo método do Carioca (coleta/bra-rj-1/importar.py, de onde este foi copiado |
| `coleta/bra-mg-1/pacote.py` | Grava o pacote do Campeonato Mineiro (data/coleta/bra-mg-1/pacote/) e o relatório (docs/coleta/bra-mg-1.md), no formato de docs/agente-coleta-COMECE-AQUI.md, seção 4. Chamado por importar.py. |
| `coleta/bra-mg-1/rsssf_mg1.py` | Leitura das páginas do Campeonato Mineiro da RSSSF Brasil (data/coleta/bra-mg-1/rsssfbrasil/mg{ano}.htm). |

- Fontes baixadas: `data/coleta/bra-mg-1/` (ogol, rsssfbrasil, wikipedia). Pacote: `data/coleta/bra-mg-1/pacote/`. Relatório: `docs/coleta/bra-mg-1.md`.
- Código comum: `coleta/comum/` (`rsssf.py` leitor das páginas da RSSSF Brasil, `ogol.py` calendários e fichas, `gols.py` autores dos gols, `registro.py` cadastro comum de nomes `data/coleta/comum/clubes_ogol.json`, `baixar.py` download educado).
- Refazer do zero (da raiz do `clube_analitico`, logs no scratchpad):

  - `python coleta/bra-mg-1/baixar_ogol.py` (ver o docstring)
  - `python coleta/bra-mg-1/baixar_rsssf.py` (ver o docstring)
  - `python coleta/bra-mg-1/baixar_wiki.py` (ver o docstring)
  - `python coleta/bra-mg-1/importar.py` (grava o pacote e o relatório; `importar.py <ano>` só mostra, sem gravar)
  - `python coleta/comum/testar_carga.py bra-mg-1 <pasta temporária>` (deve terminar com `-> OK`)
  - `python coleta/comum/documentar.py`

