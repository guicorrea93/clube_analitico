# Campeonato Paulista (`bra-sp-1`) — documentação

Gerado por `python coleta/comum/documentar.py` a partir do pacote `data/coleta/bra-sp-1/pacote/` e dos módulos de `coleta/bra-sp-1/`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/bra-sp-1.md`.

## 1. O que temos

- **Edições:** 135, de 1902 a 2026.
- **Jogos:** 21849; **gols:** 64382; **gols com autor:** 6405 (10%); **cartões:** 0.
- **Clubes:** 112; **artilheiros:** 132 temporadas com artilheiro (157 linhas, com empates).
- **Classificação final:** 135 temporadas; **rodada a rodada:** 22 temporadas.
- **Tabelas publicadas guardadas para conferência:** 2801 linhas.
- **No banco (`db/futebol.db`):** sim (135 edições, 21849 jogos).
- **Observação da competição:** 1ª divisão paulista, de 1902 a 2026. Nos anos de ligas rivais (1913-1916, 1926-1929, 1935-1936) cada torneio reconhecido pela federação é uma edição ("1913 LPF", "1913 APEA").

## 2. Fontes e regras

**Temporadas:** 135, de 1902 a 2026 (2026 pelo ogol e pela FPF; a RSSSF ainda não tem a página). Nos anos de duas ligas (1913-1916 e 1935-1936: LPF e APEA; 1926-1929: APEA e LAF) cada liga é uma temporada própria ("1913 LPF", "1913 APEA"), com o mesmo ano. Campeões conferidos na RSSSF Brasil (spcamp.htm) e na Wikipédia em português ("Campeonato Paulista de Futebol").

**Fontes:** RSSSF Brasil (`sp{ano}.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada edição e o código de cada clube; confere placares, traz a rodada e completa jogos); Wikipédia (lista de campeões); FPF (API do site, `coleta/bra-sp-1/baixar_fpf.py`: data oficial de cada jogo de 2007 em diante e fase e grupo de 2024 a 2026).

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela, fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` ou nos pacotes das Séries C e D e da Copa do Brasil usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`). Palestra Itália e Palmeiras são o mesmo clube (o ogol já os junta). Os homônimos antigos levam "-SP" quando o nome já é de um clube de outro estado ("Internacional-SP").

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF): 222 tabelas fecham com os jogos e 120 divergem (cada divergência é explicada no relatório, na temporada).
- Temporadas com alguma tabela divergente: 1906, 1908, 1909, 1910, 1914 APEA, 1915 LPF, 1915 APEA, 1916 LPF, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926 APEA, 1927 APEA, 1927 LAF, 1928 APEA, 1928 LAF, 1929 LAF, 1930, 1931, 1932, 1934, 1935 LPF, 1935 APEA, 1936 LPF, 1937, 1938, 1939, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1956, 1957, 1962, 1966, 1967, 1968, 1969, 1970, 1974, 1975, 1978, 1980, 1981, 1982, 1983, 1985, 1986, 1987, 1988, 1990, 1991, 1992, 1994, 1997, 1999, 2001, 2002, 2003, 2005, 2006, 2010, 2016, 2022, 2024.
- Temporadas sem tabela para conferir: 1940, 1951, 1952, 1953, 1954, 1955, 1958, 1959, 1960, 1961, 1963, 1964, 1965, 1971, 1972, 1984, 2014, 2025, 2026.
- Temporadas com menos jogos do que o ogol: 1913 LPF (20 de 24), 1914 LPF (19 de 32), 1916 APEA (41 de 43), 1927 LAF (45 de 73), 1935 APEA (56 de 58), 1938 (55 de 56), 2009 (196 de 202), 2010 (196 de 202), 2011 (198 de 202), 2012 (198 de 202), 2013 (198 de 202), 2017 (110 de 121), 2018 (110 de 121), 2019 (110 de 121), 2020 (104 de 110), 2021 (104 de 109), 2022 (104 de 109), 2023 (104 de 109).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|
| 1900s | 223 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1910s | 560 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1920s | 1088 | 100% | 0% | 4% | 0% | 0% | 0% | 0% | 0.0 |
| 1930s | 1031 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 1122 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 2593 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 2270 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 2414 | 100% | 0% | 17% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 3739 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 2898 | 100% | 9% | 19% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 1621 | 100% | 73% | 97% | 0% | 0% | 0% | 31% | 0.0 |
| 2010s | 1594 | 100% | 100% | 93% | 1% | 1% | 6% | 95% | 0.0 |
| 2020s | 696 | 100% | 100% | 76% | 0% | 0% | 0% | 54% | 0.0 |

**Fonte de cada jogo:** RSSSF Brasil: 21641; ogol: 191; Futebol Nacional: 17.

## 5. Formato ao longo do tempo

**Número de clubes:**

- 1902 a 1903: 5 clubes
- 1904 a 1911: 6 clubes
- 1912: 7 clubes
- 1913 LPF: 5 clubes
- 1913 APEA: 3 clubes
- 1914 LPF: 5 clubes
- 1914 APEA: 6 clubes
- 1915 LPF: 7 clubes
- 1915 APEA: 6 clubes
- 1916 LPF: 14 clubes
- 1916 APEA: 7 clubes
- 1917: 9 clubes
- 1918 a 1920: 10 clubes
- 1921 a 1922: 12 clubes
- 1923 a 1925: 11 clubes
- 1926 APEA: 10 clubes
- 1926 LAF: 8 clubes
- 1927 APEA: 14 clubes
- 1927 LAF: 10 clubes
- 1928 APEA: 7 clubes
- 1928 LAF: 12 clubes
- 1929 APEA: 8 clubes
- 1929 LAF: 12 clubes
- 1930 a 1931: 14 clubes
- 1932: 12 clubes
- 1933 a 1934: 8 clubes
- 1935 LPF: 7 clubes
- 1935 APEA: 8 clubes
- 1936 LPF: 12 clubes
- 1936 APEA: 7 clubes
- 1937: 10 clubes
- 1938 a 1948: 11 clubes
- 1949 a 1950: 12 clubes
- 1951 a 1952: 16 clubes
- 1953: 15 clubes
- 1954 a 1955: 14 clubes
- 1956: 18 clubes
- 1957 a 1959: 20 clubes
- 1960: 18 clubes
- 1961 a 1965: 16 clubes
- 1966: 15 clubes
- 1967 a 1969: 14 clubes
- 1970: 10 clubes
- 1971 a 1973: 12 clubes
- 1974: 14 clubes
- 1975: 19 clubes
- 1976: 18 clubes
- 1977: 19 clubes
- 1978 a 1980: 21 clubes
- 1981 a 1988: 20 clubes
- 1989: 22 clubes
- 1990: 24 clubes
- 1991 a 1992: 28 clubes
- 1993: 30 clubes
- 1994: 16 clubes
- 1995: 17 clubes
- 1996 a 1999: 16 clubes
- 2000: 17 clubes
- 2001: 16 clubes
- 2002: 13 clubes
- 2003: 22 clubes
- 2004: 21 clubes
- 2005 a 2016: 20 clubes
- 2017 a 2026: 16 clubes

**Pontos por vitória:**

- 1902 a 1994: 2
- 1995 a 2026: 3

**Nome oficial:**

- 1902 a 1912: Campeonato Paulista
- 1913 LPF: Campeonato Paulista (LPF)
- 1913 APEA: Campeonato Paulista (APEA)
- 1914 LPF: Campeonato Paulista (LPF)
- 1914 APEA: Campeonato Paulista (APEA)
- 1915 LPF: Campeonato Paulista (LPF)
- 1915 APEA: Campeonato Paulista (APEA)
- 1916 LPF: Campeonato Paulista (LPF)
- 1916 APEA: Campeonato Paulista (APEA)
- 1917 a 1925: Campeonato Paulista
- 1926 APEA: Campeonato Paulista (APEA)
- 1926 LAF: Campeonato Paulista (LAF)
- 1927 APEA: Campeonato Paulista (APEA)
- 1927 LAF: Campeonato Paulista (LAF)
- 1928 APEA: Campeonato Paulista (APEA)
- 1928 LAF: Campeonato Paulista (LAF)
- 1929 APEA: Campeonato Paulista (APEA)
- 1929 LAF: Campeonato Paulista (LAF)
- 1930 a 1934: Campeonato Paulista
- 1935 LPF: Campeonato Paulista (LPF)
- 1935 APEA: Campeonato Paulista (APEA)
- 1936 LPF: Campeonato Paulista (LPF)
- 1936 APEA: Campeonato Paulista (APEA)
- 1937 a 1993: Campeonato Paulista
- 1994 a 2026: Campeonato Paulista Série A1

**Formato de cada edição** (fases na ordem; grupos; mata-mata):

- 1902 a 1904: pontos corridos + mata-mata
- 1905 a 1950: pontos corridos
- 1951: mata-mata + pontos corridos
- 1952 a 1965: pontos corridos
- 1966: mata-mata + pontos corridos
- 1967 a 1968: pontos corridos
- 1969: pontos corridos + 2 grupos + pontos corridos
- 1970 a 1972: pontos corridos
- 1973 a 1975: pontos corridos + mata-mata
- 1976: 3 grupos + pontos corridos
- 1977: pontos corridos + mata-mata + pontos corridos + mata-mata + 2 grupos + mata-mata
- 1978: mata-mata + 4 grupos + mata-mata + 2 grupos + mata-mata
- 1979: mata-mata + pontos corridos + 2 grupos + mata-mata
- 1980: mata-mata + pontos corridos
- 1981: 2 grupos + mata-mata + 2 grupos + 3 grupos + pontos corridos + 2 grupos + mata-mata
- 1982: pontos corridos
- 1983: pontos corridos + 4 grupos + 2 grupos + mata-mata
- 1984: pontos corridos
- 1985 a 1987: pontos corridos + mata-mata
- 1988: pontos corridos + 2 grupos + mata-mata
- 1989: pontos corridos + 2 grupos + 4 grupos + mata-mata
- 1990: 2 grupos + pontos corridos + 2 grupos + mata-mata
- 1991: 2 grupos + mata-mata
- 1992 a 1993: pontos corridos + 2 grupos + mata-mata
- 1994: pontos corridos
- 1995: pontos corridos + 2 grupos + mata-mata
- 1996: pontos corridos
- 1997: 2 grupos + pontos corridos
- 1998 a 1999: pontos corridos + 2 grupos + mata-mata
- 2000: 2 grupos + 4 grupos + 2 grupos + mata-mata
- 2001: pontos corridos + mata-mata
- 2002: mata-mata + pontos corridos
- 2003: pontos corridos + 3 grupos + mata-mata
- 2004: 2 grupos + mata-mata
- 2005 a 2006: pontos corridos
- 2007 a 2023: pontos corridos + mata-mata
- 2024 a 2025: 4 grupos + mata-mata
- 2026: pontos corridos + mata-mata

**Fases que aparecem** (número de temporadas): Fase única (68); Final (49); Primeira fase (36); Semifinal (34); 1º Turno (29); 2º Turno (27); Segunda fase (21); Quartas de final (11); Torneio de rebaixamento (5); Repescagem (4); Fase final (4); 1º Turno - Final (3); 2º Turno - Final (3); Desempate (2); 1º Turno - Semifinal (2); 2º Turno - Semifinal (2); 3º Turno (2); Terceira fase (2); Torneio de Classificação (1); Fase de Classificação (1); 2º Turno - 1ª fase (1); 2º Turno - 2ª fase (1); 1º Turno - Quartas de final (1); 2º Turno - Quartas de final (1); 1º Turno - Classificatória (1); 2º Turno - Classificatória (1).

**Observações das edições:**

- 1973: título dividido entre Portuguesa e Santos: a final terminou 0-0 e o árbitro encerrou os pênaltis com 2-0 para o Santos quando a Portuguesa ainda podia empatar; a FPF declarou os dois campeões (o Santos só chega aos 22 títulos da lista oficial com este) e o Palmeiras herdou o vice (D-07, SP-001)

## 6. Campeões, acessos, rebaixados e punições

**Títulos:**

- Corinthians: 31
- Palmeiras: 27
- São Paulo: 22
- Santos: 21
- Paulistano-SP: 11
- São Paulo Athletic: 4
- AA das Palmeiras: 3
- Portuguesa: 3
- Germânia: 2
- SC Internacional-SP: 2
- Americano-SP: 2
- AA São Bento: 2
- Ituano: 2
- Inter de Limeira: 1
- Bragantino: 1
- São Caetano: 1

**Acessos:** nenhum marcado no pacote.

**Rebaixamentos:** 140 no total; quem mais teve: Juventus-SP (5), Ponte Preta (5), XV de Piracicaba (5), Noroeste (5), São Bento (5), Santo André (5), Portuguesa Santista (4), América-SP (4).

**Punições em pontos:**

- nenhuma

## 7. Correções e decisões (com o motivo)

Registradas nos módulos de `coleta/bra-sp-1/`; cada uma também aparece no relatório, na temporada.

### Temporadas com o ogol como base dos jogos (`importar.BASE_OGOL`)

- **2026:** a RSSSF ainda não tem a página de 2026 (SP-004, D-01): os jogos vêm do ogol, e a fase e o grupo da FPF

### Tabelas publicadas parciais (fora da conferência) (`importar.TABELAS_PARCIAIS`)

- **2025:** a página da RSSSF parou na 6ª rodada da 1ª fase: as tabelas dela são parciais e não servem de conferência; os outros jogos vêm do ogol

### Observações das edições (`importar.OBS_EDICAO`)

- **1973:** título dividido entre Portuguesa e Santos: a final terminou 0-0 e o árbitro encerrou os pênaltis com 2-0 para o Santos quando a Portuguesa ainda podia empatar; a FPF declarou os dois campeões (o Santos só chega aos 22 títulos da lista oficial com este) e o Palmeiras herdou o vice (D-07, SP-001)

### Clube trocado pelo ogol numa temporada (código -> código) (`importar.CORRIGE_OGOL`)

- **1933 · 233382:** [39622] "São Bento de São Paulo" é a AA São Bento da capital: a RSSSF e o Futebol Nacional escrevem "AA São Bento" em 1933 (D-23 d, SP-026)
- **1935 LPF · 81019:** [275483] "ECPaulista" (ficha de São Carlos) é o CA Paulista da capital: o Futebol Nacional escreve "CA Paulista" em 1934, 1935 LPF e 1936 (D-23 e, SP-027)

### Nome da página casado à mão com o clube (`importar.NOME_MANUAL`)

- **1927 APEA · Corinthians de Santo André:** [81207] "Corinthians (SBC)" na página; o ogol tem os 13 jogos dele (SP-009)

### Jogos que ficam fora (`importar.JOGOS_FORA`)

- **1906 · 1906-08-05 · São Paulo Athletic · SC Internacional-SP:** o SPAC desistiu depois deste jogo e a LPF o cancelou, dando os pontos dos seguintes aos adversários (FN; QS-005)
- **1916 APEA · 1916-10-29 · Ypiranga-SP · Mackenzie-SP:** 3º jogo do par, fora da tabela publicada (RSSSF e FN; QS-006)
- **1916 APEA · 1916-12-03 · AA das Palmeiras · Palmeiras:** 3º jogo do par, fora da tabela publicada (RSSSF e FN; QS-006)
- **1928 APEA · 1928-07-29 · Palmeiras · Portuguesa:** 3º jogo Palestra x Portuguesa na página; o ogol não o tem e, sem ele, as campanhas dos dois fecham com a tabela da RSSSF (8 vitórias e 45 gols pró do Palestra); vice: Santos (pódio da Wikipédia; SP-003)

### Jogos anulados (`importar.JOGOS_ANULADOS`)

- **1956 · Taubaté · Corinthians · 2 · 2:** 21/11/1956: a tabela da própria página dá 18 jogos ao Taubaté e ao Corinthians, o que só fecha sem ele; o ogol e o FN só têm o 0-2 de 23/12 (achado QS-013)

### Clubes com todos os jogos fora (`importar.RSSSF_FORA`)

- **1988 · Ponte Preta:** perdeu a vaga na 1ª divisão e todos os jogos dela foram cancelados (nota da página; FN "Cancelado"; o ogol não os tem; achado SP-014)
- **1988 · Bandeirante:** perdeu a vaga na 1ª divisão e todos os jogos dele foram cancelados (nota da página; FN "Cancelado"; o ogol não os tem; achado SP-014)

### Jogos do ogol ignorados (`importar.OGOL_IGNORAR`)

- **2591655:** 1928 LAF: Paulista 127-0 LAF não é jogo (linha de resumo do ogol, sem data e contra um clube "LAF" que não existe; o Futebol Nacional dá 133 jogos sem ele; achado SP-011)

### Fases da página renomeadas (por temporada) (`importar.FASE_ANO`)

- **1976 · 2º Turno:** [Fase final] o "2º turno" de 1976 é a fase final com os 12 melhores (achado SP-008)

### Seções da Wikipédia -> fase e grupo (`fpf_sp1.FASE`)

- **1:** Primeira fase
- **2:** Quartas de final
- **3:** Semifinal
- **4:** Final

### Ocorrências explicadas, por temporada (`explicacoes.EXPLICACOES`)

- **1905:** Paulistano x AA das Palmeiras não foi jogado e a vitória foi dada ao Paulistano ("awarded 0-0" na página): conta como vitória sem gols do Paulistano (W.O., decisão D-15), como na tabela publicada; o ogol registra 1 a 0
- **1909:** o SC Internacional foi eliminado depois do jogo de 21/11/1909 e fica fora da tabela da RSSSF; o vice é o Paulistano
- **1978:** três turnos: o 1º e o 2º com decisão em mata-mata ("1º Turno - ...", "2º Turno - ..."), o 3º em dois grupos, depois semifinal e final; 3º lugar: Guarani, eliminado na semifinal com a melhor campanha (D-02). O playoff Velo Clube x Paulista (junho de 1979) é o torneio de rebaixamento
- **1914 APEA:** campeão: Associação Atlética São Bento (o São Bento da capital, extinto; não é o de Sorocaba)
- **1925:** campeão: Associação Atlética São Bento (o mesmo de 1914 APEA)
- **1979:** a repescagem Marília x Santo André vem na página depois da final (fevereiro de 1980) só com dia e mês ("[Dec 5]"); ficou dezembro de 1980 pela ordem da página, mas pode ser dezembro de 1979 (o ogol não tem esses jogos)
- **2002:** os clubes do Torneio Rio-São Paulo não jogaram o Paulista; o campeão é o Ituano. O Supercampeonato de 2002 (vencido pelo São Paulo) é outra competição e não entra

### Clube do ogol casado à mão com o nome do banco (`clubes_sp1.MANUAL_DB`)

- **3333:** [J.Malucelli] o ogol escreve 'JMalucelli'; é o J. Malucelli do banco (Série A 2000)
- **24836:** [Novorizontino] Grêmio Novorizontino (2010-); o banco separou o GE Novorizontino (1973-1999) em 20/11/2026

### Nome de exibição de clube novo, dado à mão (`clubes_sp1.MANUAL_NOVO`)

- **68358:** [Corinthians Prudente] EC Corinthians de Presidente Prudente (1996): não é o Corinthians paulistano do banco
- **45210:** [Maringá] Maringá FC fundado em 2010 (Copa do Brasil 2025): não é o GE Maringá do banco
- **241210:** [Maringá FC 1995] Maringá FC fundado em 1995 (Copa do Brasil 1997): outro clube, nome como no ogol
- **60858:** [GE Novorizontino] Grêmio Esportivo Novorizontino (1973-1999, campeão de 1994): outro clube; o 'Novorizontino' do banco fica com o Grêmio Novorizontino, fundado em 2010 (decisão do Guilherme, 20/11/2026)
- **20122:** [Linhares EC] dois clubes de Linhares-ES: o EC (anos 1990) e o FC (anos 2000); o sufixo já distingue
- **9783:** [Linhares FC] dois clubes de Linhares-ES: o EC (anos 1990) e o FC (anos 2000); o sufixo já distingue
- **rs-gremio-catanduvense:** [Grêmio Catanduvense] Grêmio Catanduvense de Futebol, fundado em 1999; o ogol usa o código do GE Catanduvense (1970-1995), que fica com o nome 'Catanduvense' do banco (Série B 1989). Clube refundado é outro cadastro (D-23 a, A2-022)

### Fichas do ogol com cidade ou estado errados (`clubes_sp1.FICHA_CORRIGIDA`)

- **39622:** cidade → São Paulo; uf → SP
- **59514:** cidade → São Paulo; uf → SP; estado → São Paulo; nome_completo → None; fundacao → None
- **80977:** cidade → São Caetano do Sul

### Anos com torneio à parte na página (fica fora) (`rsssf_sp1.ANOS_A_PARTE`)

- 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2017, 2018, 2019, 2020, 2021, 2022, 2023

### Letras trocadas na página da RSSSF (`rsssf_sp1.LETRAS`)

- **S�o:** São
- **s�o:** são
- **Jundia�:** Jundiaí
- **It�lia:** Itália
- **Guaratinguet�:** Guaratinguetá
- **Germ�nia:** Germânia
- **S�rio:** Sírio
- **Independ�ncia:** Independência
- **Mar�lia:** Marília
- **Sert�ozinho:** Sertãozinho
- **Am�rica:** América
- **S�rie:** Série
- **Liban�s:** Libanês
- **Trof�u:** Troféu
- **TROF�U:** TROFÉU
- **Campe�o:** Campeão
- **CAMPE�O:** CAMPEÃO
- **Jos�:** José
- **El�seos:** Elíseos
- **Atl�tico:** Atlético
- **Divis�o:** Divisão
- **Andr�:** André
- **In�cio:** Início
- **Ribeir�o:** Ribeirão
- **Uni�o:** União
- **Ant�rtica:** Antártica
- **Ferrovi�ria:** Ferroviária
- **Maranh�o:** Maranhão
- **S�lex:** Sílex
- **Brit�nia:** Britânia
- **Ja�:** Jaú
- **Taubat�:** Taubaté
- **Bragan�a:** Bragança
- **�talo:** Ítalo

### Títulos divididos (D-07) (`importar.CAMPEOES_DIVIDIDOS`)

- **1973:** [['Portuguesa', 'Santos']] Palmeiras

### Páginas da RSSSF corrigidas na leitura (`rsssf.CORRECOES`, registradas em `coleta/bra-sp-1/rsssf_*.py`)

- **sp1902.htm:** letras trocadas por "�" na página
- **sp1903.htm:** letras trocadas por "�" na página
- **sp1904.htm:** letras trocadas por "�" na página
- **sp1905.htm:** letras trocadas por "�" na página
- **sp1906.htm:** letras trocadas por "�" na página
- **sp1907.htm:** letras trocadas por "�" na página
- **sp1908.htm:** letras trocadas por "�" na página
- **sp1909.htm:** letras trocadas por "�" na página
- **sp1910.htm:** letras trocadas por "�" na página; a página começa com a seletiva (Ypiranga, Vila Buarque e Savóia), que não é o campeonato
- **sp1911.htm:** letras trocadas por "�" na página
- **sp1912.htm:** letras trocadas por "�" na página
- **sp1913.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada
- **sp1914.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada
- **sp1915.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada
- **sp1916.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada
- **sp1917.htm:** letras trocadas por "�" na página
- **sp1918.htm:** letras trocadas por "�" na página
- **sp1919.htm:** letras trocadas por "�" na página
- **sp1920.htm:** letras trocadas por "�" na página
- **sp1921.htm:** letras trocadas por "�" na página
- **sp1922.htm:** letras trocadas por "�" na página
- **sp1923.htm:** letras trocadas por "�" na página
- **sp1924.htm:** letras trocadas por "�" na página
- **sp1925.htm:** letras trocadas por "�" na página
- **sp1926.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada
- **sp1927.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada; o leitor tira a cidade entre parênteses e o Corinthians de Santo André virava o Corinthians da capital (achado SP-009)
- **sp1928.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada
- **sp1929.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada; ano errado na data (FN: 09/06/1929; achado QS-002)
- **sp1930.htm:** letras trocadas por "�" na página
- **sp1931.htm:** letras trocadas por "�" na página
- **sp1932.htm:** letras trocadas por "�" na página
- **sp1933.htm:** letras trocadas por "�" na página; nome do clube quebrado em duas linhas ("Corinthians 2x0 AA São" / "Bento" virava Corinthians x São Paulo; SP-022)
- **sp1934.htm:** letras trocadas por "�" na página
- **sp1935.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada
- **sp1936.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada
- **sp1937.htm:** letras trocadas por "�" na página
- **sp1938.htm:** letras trocadas por "�" na página
- **sp1939.htm:** letras trocadas por "�" na página
- **sp1940.htm:** letras trocadas por "�" na página
- **sp1941.htm:** letras trocadas por "�" na página
- **sp1942.htm:** letras trocadas por "�" na página; o jogo vem sem os gols do Palmeiras; 3-1 pelo Futebol Nacional (achado SP-012)
- **sp1943.htm:** letras trocadas por "�" na página
- **sp1944.htm:** letras trocadas por "�" na página
- **sp1945.htm:** letras trocadas por "�" na página
- **sp1946.htm:** letras trocadas por "�" na página
- **sp1947.htm:** letras trocadas por "�" na página
- **sp1948.htm:** letras trocadas por "�" na página
- **sp1949.htm:** letras trocadas por "�" na página
- **sp1950.htm:** letras trocadas por "�" na página
- **sp1951.htm:** letras trocadas por "�" na página; a repescagem Jabaquara x XV de Jaú vem sem título e ficava na fase anterior
- **sp1952.htm:** letras trocadas por "�" na página
- **sp1953.htm:** letras trocadas por "�" na página
- **sp1954.htm:** letras trocadas por "�" na página
- **sp1955.htm:** letras trocadas por "�" na página
- **sp1956.htm:** letras trocadas por "�" na página
- **sp1957.htm:** letras trocadas por "�" na página
- **sp1958.htm:** letras trocadas por "�" na página
- **sp1959.htm:** letras trocadas por "�" na página
- **sp1960.htm:** letras trocadas por "�" na página
- **sp1961.htm:** letras trocadas por "�" na página
- **sp1962.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1963.htm:** letras trocadas por "�" na página
- **sp1964.htm:** letras trocadas por "�" na página
- **sp1965.htm:** letras trocadas por "�" na página
- **sp1966.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1967.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1968.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1969.htm:** letras trocadas por "�" na página; no 2º turno a página repete o 1-3 do turno final (08/jun); o jogo do 2º turno foi 25/05 1-1 (FN e ogol; achado QS-004); data com o mês por extenso na frente do jogo
- **sp1970.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1971.htm:** letras trocadas por "�" na página
- **sp1972.htm:** letras trocadas por "�" na página
- **sp1973.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1974.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1975.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1976.htm:** letras trocadas por "�" na página
- **sp1977.htm:** letras trocadas por "�" na página
- **sp1978.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1979.htm:** letras trocadas por "�" na página; ano errado na data da 15ª rodada (FN: 19/08/1979; achado QS-003); jogo em 'A - B 2:1' e data em 'dd.mm.aa'
- **sp1980.htm:** letras trocadas por "�" na página; jogo em 'A - B 2:1' e data em 'dd.mm.aa'
- **sp1981.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1982.htm:** letras trocadas por "�" na página
- **sp1983.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1984.htm:** letras trocadas por "�" na página
- **sp1985.htm:** letras trocadas por "�" na página; a página traz também a 2ª e a 3ª divisões de 1985
- **sp1986.htm:** letras trocadas por "�" na página
- **sp1987.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1988.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1989.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1990.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1991.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1992.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1993.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1994.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo
- **sp1995.htm:** letras trocadas por "�" na página
- **sp1996.htm:** letras trocadas por "�" na página
- **sp1997.htm:** letras trocadas por "�" na página
- **sp1998.htm:** letras trocadas por "�" na página
- **sp1999.htm:** letras trocadas por "�" na página
- **sp2000.htm:** letras trocadas por "�" na página
- **sp2001.htm:** letras trocadas por "�" na página
- **sp2002.htm:** letras trocadas por "�" na página; a nota sobre o Supercampeonato, logo abaixo de "First Phase", não é título de fase
- **sp2003.htm:** letras trocadas por "�" na página; nome abreviado do Atlético Sorocaba
- **sp2004.htm:** letras trocadas por "�" na página
- **sp2005.htm:** letras trocadas por "�" na página
- **sp2006.htm:** letras trocadas por "�" na página
- **sp2007.htm:** letras trocadas por "�" na página; a página traz o Troféu do Interior (torneio à parte)
- **sp2008.htm:** letras trocadas por "�" na página; a página traz o Troféu do Interior (torneio à parte)
- **sp2009.htm:** letras trocadas por "�" na página; a página traz o Troféu do Interior (torneio à parte)
- **sp2010.htm:** letras trocadas por "�" na página; a página traz o Troféu do Interior (torneio à parte)
- **sp2011.htm:** letras trocadas por "�" na página; a página traz o Troféu do Interior (torneio à parte)
- **sp2012.htm:** letras trocadas por "�" na página; a página traz o Troféu do Interior (torneio à parte)
- **sp2013.htm:** letras trocadas por "�" na página; a página traz o Troféu do Interior (torneio à parte)
- **sp2014.htm:** letras trocadas por "�" na página; nomes de clube quebrados em duas linhas
- **sp2015.htm:** letras trocadas por "�" na página
- **sp2016.htm:** letras trocadas por "�" na página; títulos das tabelas dos grupos
- **sp2017.htm:** letras trocadas por "�" na página; a página traz o Troféu do Interior (torneio à parte); títulos das tabelas dos grupos
- **sp2018.htm:** letras trocadas por "�" na página; a página traz o Troféu do Interior (torneio à parte); títulos das tabelas dos grupos
- **sp2019.htm:** letras trocadas por "�" na página; a página traz o Troféu do Interior (torneio à parte); títulos das tabelas dos grupos
- **sp2020.htm:** letras trocadas por "�" na página; a página traz o Troféu do Interior (torneio à parte); títulos das tabelas dos grupos
- **sp2021.htm:** letras trocadas por "�" na página; a página traz o Troféu do Interior (torneio à parte); títulos das tabelas dos grupos
- **sp2022.htm:** letras trocadas por "�" na página; a página traz o Troféu do Interior (torneio à parte); títulos das tabelas dos grupos
- **sp2023.htm:** letras trocadas por "�" na página; a página traz a Taça Independência (torneio à parte dos clubes eliminados); títulos das tabelas dos grupos; o grupo D da 1ª fase vem como "Group L"
- **sp2024.htm:** letras trocadas por "�" na página; títulos das tabelas dos grupos
- **sp2025.htm:** letras trocadas por "�" na página; títulos das tabelas dos grupos

## 8. O que não deu para coletar

- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade, combinado com o Guilherme).
- **Autores dos gols:** só onde a RSSSF traz e a soma fecha com o placar.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima.
- **Classificação por rodada:** só nas fases de pontos corridos em que todos os jogos têm a rodada (vem do ogol).

## 9. Pendências e próximos passos

- Plano da revisão (docs/revisao/plano-coleta-brasil.md) concluído em 24/11, em 5 commits (ERRADO NO AR, jogos, FPF e 2026, pacote.py, pódio); detalhes em docs/coleta/pedidos.md.
- Ficam como estão, com o motivo: 3º lugar de 1917 e 1954 (o FN confirma o pacote; a Wikipédia diverge), 1927 LAF, 1928 LAF e 1930 (3º dividido na RSSSF), 1959 (empate sem regra da época); 44 casos de clube com dois jogos no mesmo dia de 1906 a 1983 (conferir com o Futebol Nacional); artilheiro de 1927 APEA, 1928 LAF e 1936 LPF.
- Autores dos gols e cartões nos anos sem RSSSF com autores: jogo a jogo, pela ficha do ogol (prioridade baixa).

## 10. Arquivos e comandos

| Arquivo | O que faz |
|---|---|
| `coleta/bra-sp-1/baixar_fpf.py` | Baixa da API pública do site da FPF (futebolpaulista.com.br) os jogos da Série A1 (IdCampeonato 73, categoria 39) de cada ano, rodada a rodada, e a artilharia oficial. Grava data/coleta/bra-sp-1/fpf/jogos_{ano}.json e ar |
| `coleta/bra-sp-1/baixar_ogol.py` | Baixa o calendário de cada edição do Paulista (1ª divisão) no ogol para data/coleta/bra-sp-1/ogol/sp1_{temporada}.json e a ficha de cada clube para data/coleta/bra-sp-1/ogol/clubes.json. |
| `coleta/bra-sp-1/clubes_sp1.py` | Identidade dos clubes da Copa do Brasil (mesmo método da Série C; clube já nomeado na Série C usa o mesmo nome). |
| `coleta/bra-sp-1/edicoes.py` | Edições do Campeonato Paulista (1ª divisão, `bra-sp-1`): temporadas, anos e nomes oficiais. |
| `coleta/bra-sp-1/explicacoes.py` | Textos do relatório do Paulista (1ª divisão) que não saem do código: introdução, explicações de cada temporada e o fim. |
| `coleta/bra-sp-1/fpf_sp1.py` | Leitor dos jogos da FPF (data/coleta/bra-sp-1/fpf/jogos_{ano}.json, de baixar_fpf.py): casa cada jogo da FPF com o do pacote e traz a data oficial (de 2007 em diante; achado QS-008) e, nos anos de FASES_DA_FPF, a fase e  |
| `coleta/bra-sp-1/importar.py` | Junta as fontes do Campeonato Paulista (1ª divisão) e grava o pacote em data/coleta/bra-sp-1/pacote/ e o relatório em docs/coleta/bra-sp-1.md. Mesmo método da Série C (docs/coleta/bra-serie-c.md). |
| `coleta/bra-sp-1/pacote.py` | Grava o pacote do Campeonato Paulista (data/coleta/bra-sp-1/pacote/) e o relatório (docs/coleta/bra-sp-1.md), no formato de docs/agente-coleta-COMECE-AQUI.md, seção 4. Chamado por importar.py. |
| `coleta/bra-sp-1/rsssf_sp1.py` | Leitura das páginas do Campeonato Paulista da RSSSF Brasil (data/coleta/bra-sp-1/rsssfbrasil/sp{ano}.htm). |

- Fontes baixadas: `data/coleta/bra-sp-1/` (fpf, ogol, rsssfbrasil, wikipedia). Pacote: `data/coleta/bra-sp-1/pacote/`. Relatório: `docs/coleta/bra-sp-1.md`.
- Código comum: `coleta/comum/` (`rsssf.py` leitor das páginas da RSSSF Brasil, `ogol.py` calendários e fichas, `gols.py` autores dos gols, `registro.py` cadastro comum de nomes `data/coleta/comum/clubes_ogol.json`, `baixar.py` download educado).
- Refazer do zero (da raiz do `clube_analitico`, logs no scratchpad):

  - `python coleta/bra-sp-1/baixar_fpf.py` (ver o docstring)
  - `python coleta/bra-sp-1/baixar_ogol.py` (ver o docstring)
  - `python coleta/bra-sp-1/importar.py` (grava o pacote e o relatório; `importar.py <ano>` só mostra, sem gravar)
  - `python coleta/comum/testar_carga.py bra-sp-1 <pasta temporária>` (deve terminar com `-> OK`)
  - `python coleta/comum/documentar.py`

