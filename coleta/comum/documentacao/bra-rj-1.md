# Campeonato Carioca (`bra-rj-1`) — documentação

Gerado por `python coleta/comum/documentar.py` a partir do pacote `data/coleta/bra-rj-1/pacote/` e dos módulos de `coleta/bra-rj-1/`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/bra-rj-1.md`.

## 1. O que temos

- **Edições:** 129, de 1906 a 2026.
- **Jogos:** 14144; **gols:** 44481; **gols com autor:** 3383 (8%); **cartões:** 0.
- **Clubes:** 83; **artilheiros:** 119 temporadas com artilheiro (128 linhas, com empates).
- **Classificação final:** 129 temporadas; **rodada a rodada:** 27 temporadas.
- **Tabelas publicadas guardadas para conferência:** 2894 linhas.
- **No banco (`db/futebol.db`):** sim (129 edições, 14144 jogos).
- **Observação da competição:** 1ª divisão do Rio de Janeiro, de 1906 a 2026: até 1959 o campeonato do Distrito Federal (a cidade do Rio), de 1960 a 1974 o do estado da Guanabara e, depois da fusão de 1975, o do estado do Rio de Janeiro. Nos anos de ligas rivais (1912, 1924, 1933-1936) cada torneio reconhecido é uma edição ("1933 AMEA", "1933 LCF"); 1979 teve o campeonato normal e o Especial.

## 2. Fontes e regras

**Temporadas:** 1906 a 2026. Até 1959 é o campeonato do Distrito Federal (a cidade do Rio de Janeiro); de 1960 a 1974, o do estado da Guanabara; de 1975 em diante, o do estado do Rio de Janeiro. Nos anos de ligas rivais cada torneio reconhecido é uma edição: 1912 (AFRJ e LMSA), 1924 (LMDT e AMEA), 1933 e 1934 (AMEA e LCF), 1935 e 1936 (FMD e LCF), 1937 (LFRJ, a liga da pacificação, na temporada "1937"; e o torneio inacabado da FMD, "1937 FMD", título homologado pela FERJ em 2023). 1979 teve dois campeonatos reconhecidos: o Especial (fevereiro a abril) e o normal (maio a setembro). O campeonato do antigo estado do Rio (interior, até 1978) é outra competição e fica de fora.

**Fontes:** RSSSF Brasil (`tablesr/rj{ano}.htm`: jogos, fases, datas, autores e tabelas; `rj1979s.htm`: o Especial de 1979; não há página de 2025 nem de 2026); ogol (calendário de cada edição, de 1906 a 2026, e o código de cada clube; confere placares, traz a rodada e completa os jogos que a página não traz); Wikipédia em português (artigo do Campeonato Carioca: campeões e vices de cada ano, segunda fonte do campeão). Artilheiros pela lista da RSSSF (`rjtops.htm`).

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela, fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` ou nos outros pacotes usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF): 223 tabelas fecham com os jogos e 127 divergem (cada divergência é explicada no relatório, na temporada).
- Temporadas com alguma tabela divergente: 1906, 1907, 1909, 1910, 1912 AFRJ, 1913, 1916, 1917, 1918, 1919, 1921, 1922, 1923, 1924 LMDT, 1926, 1928, 1929, 1930, 1931, 1932, 1933 LCF, 1934 AMEA, 1935 FMD, 1935 LCF, 1938, 1941, 1946, 1948, 1953, 1955, 1958, 1959, 1961, 1963, 1970, 1971, 1973, 1974, 1975, 1976, 1977, 1979, 1979 Especial, 1980, 1981, 1983, 1985, 1986, 1987, 1988, 1990, 1991, 1992, 1993, 1995, 1996, 1997, 1998, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2009, 2010, 2011, 2012, 2013, 2017, 2019, 2022, 2024.
- Temporadas sem tabela para conferir: 1911, 1912 LMSA, 1915, 1925, 1933 AMEA, 1934 LCF, 1940, 1944, 2018, 2020, 2025, 2026.
- Temporadas com menos jogos do que o ogol: 1910 (28 de 30), 1912 AFRJ (27 de 30), 1912 LMSA (55 de 56), 1924 LMDT (153 de 156), 1931 (112 de 113), 1934 AMEA (39 de 41), 2011 (126 de 132), 2012 (128 de 134).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|
| 1900s | 103 | 100% | 10% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1910s | 595 | 99% | 12% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1920s | 1081 | 100% | 10% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1930s | 1129 | 100% | 11% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 1065 | 100% | 9% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 1335 | 94% | 8% | 10% | 0% | 0% | 0% | 7% | 0.0 |
| 1960s | 1158 | 100% | 2% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 1618 | 100% | 2% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 1491 | 98% | 4% | 18% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 1700 | 92% | 1% | 37% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 1064 | 100% | 59% | 93% | 0% | 0% | 0% | 6% | 0.0 |
| 2010s | 1214 | 100% | 100% | 89% | 0% | 0% | 0% | 74% | 0.0 |
| 2020s | 591 | 100% | 100% | 60% | 0% | 0% | 0% | 27% | 0.0 |

**Fonte de cada jogo:** RSSSF Brasil: 13551; ogol: 593.

## 5. Formato ao longo do tempo

**Número de clubes:**

- 1906: 6 clubes
- 1907: 4 clubes
- 1908: 6 clubes
- 1909: 7 clubes
- 1910: 6 clubes
- 1911: 4 clubes
- 1912 AFRJ: 7 clubes
- 1912 LMSA: 8 clubes
- 1913: 10 clubes
- 1914: 7 clubes
- 1915 a 1916: 8 clubes
- 1917 a 1919: 11 clubes
- 1920: 10 clubes
- 1921 a 1922: 14 clubes
- 1923: 16 clubes
- 1924 LMDT: 23 clubes
- 1924 AMEA: 8 clubes
- 1925: 12 clubes
- 1926 a 1927: 10 clubes
- 1928 a 1931: 11 clubes
- 1932: 12 clubes
- 1933 AMEA: 13 clubes
- 1933 LCF: 6 clubes
- 1934 AMEA: 10 clubes
- 1934 LCF: 7 clubes
- 1935 FMD: 9 clubes
- 1935 LCF: 6 clubes
- 1936 FMD: 7 clubes
- 1936 LCF: 6 clubes
- 1937: 12 clubes
- 1937 FMD: 8 clubes
- 1938 a 1940: 9 clubes
- 1941 a 1946: 10 clubes
- 1947 a 1952: 11 clubes
- 1953 a 1961: 12 clubes
- 1962 a 1964: 13 clubes
- 1965: 8 clubes
- 1966 a 1975: 12 clubes
- 1976 a 1977: 15 clubes
- 1978: 12 clubes
- 1979: 18 clubes
- 1979 Especial: 10 clubes
- 1980: 14 clubes
- 1981 a 1986: 12 clubes
- 1987: 14 clubes
- 1988 a 1990: 12 clubes
- 1991: 24 clubes
- 1992: 26 clubes
- 1993: 24 clubes
- 1994: 12 clubes
- 1995: 17 clubes
- 1996 a 1998: 12 clubes
- 1999: 13 clubes
- 2000: 14 clubes
- 2001: 16 clubes
- 2002 a 2007: 12 clubes
- 2008 a 2020: 16 clubes
- 2021: 17 clubes
- 2022 a 2026: 12 clubes

**Pontos por vitória:**

- 1906 a 1994: 2
- 1995 a 2026: 3

**Nome oficial:**

- 1906 a 1911: Campeonato Carioca
- 1912 AFRJ: Campeonato Carioca (AFRJ)
- 1912 LMSA: Campeonato Carioca (LMSA)
- 1913 a 1923: Campeonato Carioca
- 1924 LMDT: Campeonato Carioca (LMDT)
- 1924 AMEA: Campeonato Carioca (AMEA)
- 1925 a 1932: Campeonato Carioca
- 1933 AMEA: Campeonato Carioca (AMEA)
- 1933 LCF: Campeonato Carioca (LCF)
- 1934 AMEA: Campeonato Carioca (AMEA)
- 1934 LCF: Campeonato Carioca (LCF)
- 1935 FMD: Campeonato Carioca (FMD)
- 1935 LCF: Campeonato Carioca (LCF)
- 1936 FMD: Campeonato Carioca (FMD)
- 1936 LCF: Campeonato Carioca (LCF)
- 1937: Campeonato Carioca
- 1937 FMD: Campeonato Carioca (FMD)
- 1938 a 1979: Campeonato Carioca
- 1979 Especial: Campeonato Carioca Especial
- 1980 a 2026: Campeonato Carioca

**Formato de cada edição** (fases na ordem; grupos; mata-mata):

- 1906 a 1910: pontos corridos
- 1911: pontos corridos + mata-mata
- 1912 AFRJ a 1914: pontos corridos
- 1915: mata-mata + pontos corridos
- 1916 a 1920: pontos corridos
- 1921: 2 grupos + mata-mata
- 1922 a 1923: 2 grupos
- 1924 LMDT: 2 grupos + pontos corridos
- 1924 AMEA a 1935 LCF: pontos corridos
- 1936 FMD: pontos corridos + mata-mata
- 1936 LCF a 1943: pontos corridos
- 1944: pontos corridos + mata-mata
- 1945 a 1967: pontos corridos
- 1968: 2 grupos + pontos corridos
- 1969 a 1972: pontos corridos
- 1973: mata-mata + pontos corridos + 2 grupos + mata-mata
- 1974 a 1979 Especial: pontos corridos
- 1980 a 1981: pontos corridos + mata-mata
- 1982 a 1985: pontos corridos
- 1986: pontos corridos + mata-mata
- 1987: pontos corridos
- 1988 a 1989: pontos corridos + mata-mata
- 1990: pontos corridos
- 1991: mata-mata + 2 grupos + mata-mata
- 1992: 2 grupos
- 1993: 2 grupos + mata-mata
- 1994: 2 grupos + mata-mata + pontos corridos
- 1995: pontos corridos + mata-mata + pontos corridos
- 1996: pontos corridos
- 1997: mata-mata + pontos corridos + mata-mata
- 1998: pontos corridos
- 1999: pontos corridos + mata-mata
- 2000: 2 grupos + pontos corridos + mata-mata
- 2001: pontos corridos + 2 grupos + mata-mata + pontos corridos + mata-mata
- 2002: pontos corridos + 2 grupos + mata-mata
- 2003: pontos corridos + mata-mata
- 2004: mata-mata + 2 grupos + mata-mata + pontos corridos + mata-mata + pontos corridos
- 2005: 2 grupos + mata-mata + pontos corridos + mata-mata
- 2006: 2 grupos + mata-mata + pontos corridos + mata-mata + pontos corridos + mata-mata
- 2007 a 2008: 2 grupos + mata-mata + pontos corridos + mata-mata
- 2009: mata-mata + 2 grupos + mata-mata + pontos corridos + mata-mata
- 2010: 2 grupos + mata-mata + pontos corridos + mata-mata + pontos corridos
- 2011 a 2012: 2 grupos + mata-mata + pontos corridos + mata-mata
- 2013: pontos corridos + mata-mata + 2 grupos + mata-mata
- 2014 a 2015: pontos corridos + mata-mata
- 2016: pontos corridos + 2 grupos + mata-mata
- 2017: pontos corridos
- 2018: pontos corridos + 2 grupos + pontos corridos + mata-mata
- 2019: pontos corridos + 2 grupos + pontos corridos
- 2020: pontos corridos + 2 grupos + pontos corridos + mata-mata
- 2021 a 2026: pontos corridos + mata-mata

**Fases que aparecem** (número de temporadas): 1º Turno (62); 2º Turno (57); Fase única (48); Final (30); Primeira fase (23); Fase final (16); 2º Turno - Final (14); 1º Turno - Final (13); Semifinal (13); 2º Turno - Semifinal (11); 1º Turno - Semifinal (10); 3º Turno (6); Segunda fase (6); Fase preliminar (6); Taça Rio - Semifinal (2); Taça Rio - Final (2); 2° TURNO (1); 1° TURNO (1); Prova Eliminatória (1); 4º Turno (1); 3º Turno (Taça José de Albuquerque) (1); First Round (1); 3º Turno (Taça Pedro Magalhães Corrêa) (1); 3º Turno (Taça Danilo Leal Carneiro) (1); 3º Turno (Taça Sylvio Corrêa Pacheco) (1); Taça Rio de Janeiro winner qualified to the final playoff (1); 3º Turno (Taça Euzëbio de Andrade) (1); 3º Turno (Taça Jerônimo Bastos) (1); Second Place Playoff (1); Championship Playoff (1); Terceira fase (1); Vasco da Gama won the 2nd stage (1); LEAGUE FINALS (if needed) (1); Torneio de rebaixamento (1); Quadrangular de Descenso (1); Quartas de final (1).

**Observações das edições:**

- 1907: título dividido entre Fluminense e Botafogo: terminaram empatados, a LMSA acabou sem decidir e a FERJ declarou os dois campeões em 1996 (D-07); sem vice
- 1937: torneio da LFRJ, a liga da pacificação (FMD e LCF juntas); o da FMD, que parou no meio, é a edição "1937 FMD"
- 1937 FMD: torneio inacabado: parou na 8ª rodada (26 jogos) com a pacificação das ligas; a FMD proclamou o São Cristóvão campeão (invicto, 7 vitórias em 7 jogos) em 03/09/1937, e a FERJ homologou o título em dezembro de 2023

## 6. Campeões, acessos, rebaixados e punições

**Títulos:**

- Flamengo: 40
- Fluminense: 33
- Vasco: 24
- Botafogo: 20
- América-RJ: 7
- São Cristóvão: 2
- Bangu: 2
- Paysandu-RJ: 1

**Acessos:** nenhum marcado no pacote.

**Rebaixamentos:** 55 no total; quem mais teve: América-RJ (5), São Cristóvão (4), Olaria (4), Bonsucesso (4), Cabofriense (4), Campo Grande-RJ (3), Volta Redonda (3), Itaperuna (3).

**Punições em pontos:**

- nenhuma

## 7. Correções e decisões (com o motivo)

Registradas nos módulos de `coleta/bra-rj-1/`; cada uma também aparece no relatório, na temporada.

### Temporadas com o ogol como base dos jogos (`importar.BASE_OGOL`)

- **2025:** sem página da RSSSF (a lista de campeões tem o link, mas a página não existe): os jogos vêm do ogol
- **2026:** sem página da RSSSF: os jogos vêm do ogol

### Tabelas publicadas parciais (fora da conferência) (`importar.TABELAS_PARCIAIS`)

- **2018:** a página da RSSSF parou em fevereiro de 2018 (44 jogos sem placar, na Taça Rio): as tabelas dela são parciais e não servem de conferência; os outros jogos vêm do ogol
- **2020:** a página da RSSSF parou em março de 2020 (21 jogos sem placar): as tabelas dela são parciais e não servem de conferência; os outros jogos vêm do ogol

### Observações das edições (`importar.OBS_EDICAO`)

- **1907:** título dividido entre Fluminense e Botafogo: terminaram empatados, a LMSA acabou sem decidir e a FERJ declarou os dois campeões em 1996 (D-07); sem vice
- **1937:** torneio da LFRJ, a liga da pacificação (FMD e LCF juntas); o da FMD, que parou no meio, é a edição "1937 FMD"
- **1937 FMD:** torneio inacabado: parou na 8ª rodada (26 jogos) com a pacificação das ligas; a FMD proclamou o São Cristóvão campeão (invicto, 7 vitórias em 7 jogos) em 03/09/1937, e a FERJ homologou o título em dezembro de 2023

### Nome da página casado à mão com o clube (`importar.NOME_MANUAL`)

- **1906 · F. & Athletic:** [98591] o Football & Athletic de Niterói escrito abreviado num jogo da página
- **1916 · Carioca:** [98437] Carioca FC, o mesmo dos anos seguintes no ogol (o calendário de 1916 não o tem)
- **1917 · CATTETE:** [98582] Cattete FC (o do ogol em 1912 AFRJ)
- **1917 · Cattete:** [98582] Cattete FC
- **1929 · MAVILIS FC:** [98489] Mavilis, o mesmo de 1933-1934 no ogol
- **1918 · Americano FC:** [98562] Americano FC, do Rio (o do ogol em 1924 LMDT): o nome parecido levava ao America FC
- **1918 · AMERICANO FC:** [98562] Americano FC, do Rio (o do ogol em 1924 LMDT): o nome parecido levava ao America FC
- **1919 · Americano FC:** [98562] Americano FC, do Rio (o do ogol em 1924 LMDT): o nome parecido levava ao America FC
- **1919 · AMERICANO FC:** [98562] Americano FC, do Rio (o do ogol em 1924 LMDT): o nome parecido levava ao America FC
- **1920 · Americano FC:** [98562] Americano FC, do Rio (o do ogol em 1924 LMDT): o nome parecido levava ao America FC
- **1920 · AMERICANO FC:** [98562] Americano FC, do Rio (o do ogol em 1924 LMDT): o nome parecido levava ao America FC
- **1921 · Americano FC:** [98562] Americano FC, do Rio (o do ogol em 1924 LMDT): o nome parecido levava ao America FC
- **1921 · AMERICANO FC:** [98562] Americano FC, do Rio (o do ogol em 1924 LMDT): o nome parecido levava ao America FC
- **1922 · Americano FC:** [98562] Americano FC, do Rio (o do ogol em 1924 LMDT): o nome parecido levava ao America FC
- **1922 · AMERICANO FC:** [98562] Americano FC, do Rio (o do ogol em 1924 LMDT): o nome parecido levava ao America FC
- **1923 · Americano FC:** [98562] Americano FC, do Rio (o do ogol em 1924 LMDT): o nome parecido levava ao America FC
- **1923 · AMERICANO FC:** [98562] Americano FC, do Rio (o do ogol em 1924 LMDT): o nome parecido levava ao America FC
- **1924 · Americano FC:** [98562] Americano FC, do Rio (o do ogol em 1924 LMDT): o nome parecido levava ao America FC
- **1924 · AMERICANO FC:** [98562] Americano FC, do Rio (o do ogol em 1924 LMDT): o nome parecido levava ao America FC
- **1925 · Americano FC:** [98562] Americano FC, do Rio (o do ogol em 1924 LMDT): o nome parecido levava ao America FC
- **1925 · AMERICANO FC:** [98562] Americano FC, do Rio (o do ogol em 1924 LMDT): o nome parecido levava ao America FC
- **1998 · America:** [2228] America FC, do Rio: o casamento pelos jogos levava ao Americano de Campos
- **1999 · America:** [2228] America FC, do Rio: o casamento pelos jogos levava ao Americano de Campos

### Jogos anulados (`importar.JOGOS_ANULADOS`)

- **1906 · F. ATHLETIC C · RIACHUELO F. C · 5 · 2:** jogo anotado depois da fonte, no fim da página (4/11/1906): o Riachuelo não jogou o campeonato de 1906 (não está na tabela nem no ogol)
- **1928 · SC AMÉRICA · CAMPO GRANDE AC · 1 · 0:** decisão da série de subúrbio (SC América, não o America FC); outra divisão
- **1929 · SC AMÉRICA · MAVILIS FC · 3 · 2:** final da série de subúrbio (SC América, não o America FC); outra divisão
- **1930 · GS SANTA CRUZ · SC AMÉRICA · 2 · 0:** final da série de subúrbio (GS Santa Cruz x SC América); outra divisão

### Ocorrências explicadas, por temporada (`explicacoes.EXPLICACOES`)

- **1907:** título dividido entre Fluminense e Botafogo: terminaram empatados (Botafogo 10 pontos e Fluminense 8 na tabela da RSSSF, os dois com 2 pontos perdidos), não houve acordo sobre o desempate e a LMSA acabou sem declarar campeão; em 1996 a FERJ declarou os dois campeões (RSSSF; Lance; Wikipédia). O pacote tem o Fluminense em campeao, o Botafogo em co_campeao e o vice vazio (D-07, como o Paulista 1973)
- **1921:** o desempate Flamengo x América foi 1-1 no tempo normal e 1-0 na prorrogação: fica 2-1 para o Flamengo
- **1937:** torneio da LFRJ (a liga da pacificação: FMD e LCF juntas), campeão o Fluminense. O torneio da FMD, disputado antes, é a edição "1937 FMD"
- **1937 FMD:** torneio da FMD, que parou na 8ª rodada (26 jogos, de 02/05 a 11/07) com a pacificação entre a FMD e a LCF; os jogos não foram anulados. A FMD proclamou o São Cristóvão campeão em 03/09/1937 (invicto, 7 vitórias em 7 jogos); o título ficou esquecido e a FERJ o homologou em dezembro de 2023, depois do dossiê do jornalista André Luiz Pereira Nunes (cerimônia em 13/01/2024; Super Rádio Tupi, 09/01/2024). A lista de campeões da RSSSF é de antes e ainda diz "unfinished": o campeão vem de importar.CAMPEOES_MANUAIS. O ogol não tem essa edição; os jogos vêm só da RSSSF
- **1979:** artilheiro: a RSSSF dá Zico 26 no campeonato normal e 34 no Especial; a Wikipédia, o contrário. Fica a RSSSF

### Clube do ogol casado à mão com o nome do banco (`clubes_rj1.MANUAL_DB`)

- **3333:** [J.Malucelli] o ogol escreve 'JMalucelli'; é o J. Malucelli do banco (Série A 2000)
- **24836:** [Novorizontino] Grêmio Novorizontino (2010-); o banco separou o GE Novorizontino (1973-1999) em 20/11/2026

### Nome de exibição de clube novo, dado à mão (`clubes_rj1.MANUAL_NOVO`)

- **68358:** [Corinthians Prudente] EC Corinthians de Presidente Prudente (1996): não é o Corinthians paulistano do banco
- **45210:** [Maringá] Maringá FC fundado em 2010 (Copa do Brasil 2025): não é o GE Maringá do banco
- **241210:** [Maringá FC 1995] Maringá FC fundado em 1995 (Copa do Brasil 1997): outro clube, nome como no ogol
- **60858:** [GE Novorizontino] Grêmio Esportivo Novorizontino (1973-1999, campeão de 1994): outro clube; o 'Novorizontino' do banco fica com o Grêmio Novorizontino, fundado em 2010 (decisão do Guilherme, 20/11/2026)
- **20122:** [Linhares EC] dois clubes de Linhares-ES: o EC (anos 1990) e o FC (anos 2000); o sufixo já distingue
- **9783:** [Linhares FC] dois clubes de Linhares-ES: o EC (anos 1990) e o FC (anos 2000); o sufixo já distingue

### Fichas do ogol com cidade ou estado errados (`clubes_rj1.FICHA_CORRIGIDA`)

- **98567:** cidade → Rio de Janeiro; uf → RJ; estado → Rio de Janeiro; nome_completo → None; fundacao → None

### Anos com torneio à parte na página (fica fora) (`rsssf_rj1.ANOS_A_PARTE`)

- 2009, 2010, 2011, 2012

### Anos com turnos (Taça Guanabara, Taça Rio) nos títulos das fases (`rsssf_rj1.TURNOS`)

- 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2018, 2019, 2020, 2021, 2022, 2023, 2024

### Letras trocadas na página da RSSSF (`rsssf_rj1.LETRAS`)

- **Ta�a:** Taça
- **S�o:** São
- **Crist�v�o:** Cristóvão
- **Am�rica:** América
- **Mac�:** Macaé
- **Maca�:** Macaé
- **Volta Redonda:** Volta Redonda
- **Friburguense:** Friburguense
- **Gon�alo:** Gonçalo
- **Niter�i:** Niterói
- **Cabofriense:** Cabofriense
- **Bonsucesso:** Bonsucesso
- **Tr�s:** Três
- **Itaperuna:** Itaperuna
- **Petr�polis:** Petrópolis
- **Serrano:** Serrano
- **Ol�ria:** Olaria

### Páginas da RSSSF corrigidas na leitura (`rsssf.CORRECOES`, registradas em `coleta/bra-rj-1/rsssf_*.py`)

- **rj1906.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1907.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1908.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1909.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1910.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1911.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1912.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1913.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1914.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1915.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1916.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1917.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1918.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1919.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1920.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1921.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim; 1921: o desempate Flamengo x América foi 1-1 no tempo normal e 1-0 na prorrogação (a prorrogação vinha numa linha à parte e virava um jogo de um clube "Extra-Time: Flamengo")
- **rj1922.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1923.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1924.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1925.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1926.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1927.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1928.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1929.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1930.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1931.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1932.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1933.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1934.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1935.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1936.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1937.htm:** letras trocadas por "�" na página; ano de duas ligas: lê só o trecho da liga da temporada; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim; 1937 FMD: data "dd / mm –" e os jogos do dia nas linhas de baixo
- **rj1938.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1939.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1940.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1941.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1942.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1943.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1944.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1945.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1946.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1947.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1948.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1949.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1950.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1951.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1952.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1953.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1954.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1955.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1956.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1957.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1958.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1959.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1960.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1961.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1962.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1963.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1964.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1965.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1966.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1967.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1968.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1969.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1970.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1971.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1972.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1973.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1974.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1975.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1976.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1977.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1978.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1979.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1979s.htm:** data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim
- **rj1980.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1981.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1982.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1983.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1984.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1985.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1986.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1987.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1988.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1989.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1990.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; data dd/mm na frente e o local do jogo no fim; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1991.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1992.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1993.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1994.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1995.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1996.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1997.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj1998.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio
- **rj1999.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2000.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2001.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2002.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2003.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2004.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2005.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2006.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2007.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; torneios de consolação entre os turnos ficam de fora; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2008.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; torneios de consolação entre os turnos ficam de fora; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2009.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; torneios de consolação entre os turnos ficam de fora; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2010.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; torneios de consolação entre os turnos ficam de fora; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2011.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; torneios de consolação entre os turnos ficam de fora; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2012.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; torneios de consolação entre os turnos ficam de fora; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2013.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; torneios de consolação entre os turnos ficam de fora; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2014.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio
- **rj2015.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio
- **rj2016.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; 2016: a 1ª fase (grupos A e B); 2016: a 2ª fase tem o grupo C (Taça Guanabara, os 8 de cima) e o grupo D (Taça Rio, os 8 de baixo); 2016: grupo C da 2ª fase; 2016: semifinal da Taça Rio (vaga na Série D); 2016: final da Taça Rio
- **rj2017.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio
- **rj2018.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2019.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2020.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2021.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2022.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2023.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2024.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio; turnos (Taça Guanabara e Taça Rio) nos títulos das fases
- **rj2025.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio
- **rj2026.htm:** letras trocadas por "�" na página; data com o mês por extenso na frente do jogo; Fluminense de Nova Friburgo separado do Fluminense do Rio
- **rjcamp.htm:** parêntese aberto na nota em português: o leitor emendava a linha de 1906 nela; parêntese sem fechar no Botafogo de 1912 (AFRJ): o leitor emendava a linha de 1913 nela

## 8. O que não deu para coletar

- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).
- **Autores dos gols:** 3.383 gols com autor, quase todos de 2010 em diante (74% dos gols dos anos 2010). Nas outras
  décadas a RSSSF não traz os autores ou traz num formato que o leitor ainda não junta ao jogo ("Gols: ..." na linha de
  baixo, nos anos 1900); só entram quando a soma bate com o placar (pendência).
- **W.O. sem vencedor:** o ogol traz cerca de 66 W.O. (1908-1935) sem dizer quem venceu; o vencedor sai da tabela
  publicada, e o W.O. conta como vitória sem gols. Sem como decidir pela tabela, fica fora (ver as temporadas).
- **Torneios à parte:** os de consolação entre os turnos (2009-2012) e as séries de subúrbio (1928-1930) ficam fora.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima.

## 9. Pendências e próximos passos

- Autores dos gols: só 3.383 (quase todos de 2010 em diante). Nas outras décadas a página não traz os autores ou traz num formato que o leitor ainda não junta ao jogo ("Gols: ..." na linha de baixo, nos anos 1900).
- 127 tabelas divergentes a explicar (ou corrigir) uma a uma no relatório; jogos avulsos do fim das páginas (súmulas sem par na lista: 1915, 1917-1919, 1924 AMEA, 1925, 1938, 1944, 1959, 1976) a conferir.
- Artilheiros de 2015 em diante: a lista da RSSSF (rjtops.htm) parou em 2014; a Wikipédia em português tem a tabela ano a ano (pt_lista.txt), ainda não lida.
- Mesma correção dos artilheiros no Paulista: lá a lista da RSSSF nunca era usada (chave pelo ano em número), o que deve explicar o SP-024.

## 10. Arquivos e comandos

| Arquivo | O que faz |
|---|---|
| `coleta/bra-rj-1/baixar_ogol.py` | Baixa o calendário de cada edição do Campeonato Carioca no ogol para data/coleta/bra-rj-1/ogol/rj1_{temporada}.json e a ficha de cada clube para data/coleta/bra-rj-1/ogol/clubes.json. |
| `coleta/bra-rj-1/baixar_rsssf.py` | Baixa as páginas do Campeonato Carioca da RSSSF Brasil para data/coleta/bra-rj-1/rsssfbrasil/. |
| `coleta/bra-rj-1/baixar_wiki.py` | Baixa o código do artigo "Campeonato Carioca de Futebol" da Wikipédia em português para data/coleta/bra-rj-1/wikipedia/pt_lista.txt (a lista de campeões ano a ano, segunda fonte do campeão). |
| `coleta/bra-rj-1/clubes_rj1.py` | Identidade dos clubes do Campeonato Carioca (mesmo método do Paulista, coleta/bra-sp-1/clubes_sp1.py; clube já nomeado em outra coleta usa o mesmo nome, pelo cadastro comum data/coleta/comum/clubes_ogol.json). |
| `coleta/bra-rj-1/edicoes.py` | Edições do Campeonato Carioca (1ª divisão, `bra-rj-1`): temporadas, anos e nomes oficiais. |
| `coleta/bra-rj-1/explicacoes.py` | Textos do relatório do Campeonato Carioca (1ª divisão) que não saem do código: introdução, explicações de cada temporada e o fim. |
| `coleta/bra-rj-1/importar.py` | Junta as fontes do Campeonato Carioca (1ª divisão) e grava o pacote em data/coleta/bra-rj-1/pacote/ e o relatório em docs/coleta/bra-rj-1.md. Mesmo método do Paulista (coleta/bra-sp-1/importar.py, de onde este foi copiad |
| `coleta/bra-rj-1/pacote.py` | Grava o pacote do Campeonato Carioca (data/coleta/bra-rj-1/pacote/) e o relatório (docs/coleta/bra-rj-1.md), no formato de docs/agente-coleta-COMECE-AQUI.md, seção 4. Chamado por importar.py. |
| `coleta/bra-rj-1/rsssf_rj1.py` | Leitura das páginas do Campeonato Carioca da RSSSF Brasil (data/coleta/bra-rj-1/rsssfbrasil/rj{ano}.htm). |

- Fontes baixadas: `data/coleta/bra-rj-1/` (ogol, rsssfbrasil, wikipedia). Pacote: `data/coleta/bra-rj-1/pacote/`. Relatório: `docs/coleta/bra-rj-1.md`.
- Código comum: `coleta/comum/` (`rsssf.py` leitor das páginas da RSSSF Brasil, `ogol.py` calendários e fichas, `gols.py` autores dos gols, `registro.py` cadastro comum de nomes `data/coleta/comum/clubes_ogol.json`, `baixar.py` download educado).
- Refazer do zero (da raiz do `clube_analitico`, logs no scratchpad):

  - `python coleta/bra-rj-1/baixar_ogol.py` (ver o docstring)
  - `python coleta/bra-rj-1/baixar_rsssf.py` (ver o docstring)
  - `python coleta/bra-rj-1/baixar_wiki.py` (ver o docstring)
  - `python coleta/bra-rj-1/importar.py` (grava o pacote e o relatório; `importar.py <ano>` só mostra, sem gravar)
  - `python coleta/comum/testar_carga.py bra-rj-1 <pasta temporária>` (deve terminar com `-> OK`)
  - `python coleta/comum/documentar.py`

