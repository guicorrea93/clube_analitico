# Campeonato Paulista Série A2 (`bra-sp-2`) — documentação

Gerado por `python coleta/comum/documentar.py` a partir do pacote `data/coleta/bra-sp-2/pacote/` e dos módulos de `coleta/bra-sp-2/`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/bra-sp-2.md`.

## 1. O que temos

- **Edições:** 63, de 1947 a 2026; sem nenhum jogo: 1947, 1993, 1994; com parte dos jogos: 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1989, 1990, 1991, 1992.
- **Jogos:** 9142; **gols:** 22052; **gols com autor:** 4526 (21%); **cartões:** 0.
- **Clubes:** 167; **artilheiros:** 53 temporadas com artilheiro (61 linhas, com empates).
- **Classificação final:** 63 temporadas; **rodada a rodada:** 23 temporadas.
- **Tabelas publicadas guardadas para conferência:** 1989 linhas.
- **No banco (`db/futebol.db`):** não.
- **Observação da competição:** 2ª divisão paulista (Série A2 desde 1994; antes Segunda Divisão, Primeira Divisão, Divisão Intermediária, Divisão Especial, conforme a época), edições de 1947 a 2026. As edições sem os jogos em nenhuma fonte (1947-1966, 1992-1994) entram só com as tabelas, o campeão e o vice; 1989 e 1991 têm parte dos jogos. Fica de fora a fase amadora (1916-1946).

## 2. Fontes e regras

**Temporadas:** 1947-1966, 1979 e 1985-2026 (63 edições). Com os jogos: 1979, 1985-1988 e 1995-2026; com parte dos jogos: 1989 e 1991, e várias de 1948-1966, 1990 e 1992 (os jogos que a Wikipédia em português traz); sem jogo nenhum: 1947, 1993 e 1994 (só a tabela ou a ordem final). Nome oficial de cada época na lista da RSSSF (Segunda Divisão, Primeira Divisão, Divisão Intermediária, Divisão Especial; Série A2 desde 1994). Campeões conferidos na lista da RSSSF (`sp2camp.htm`).

**Fontes:** RSSSF Brasil (`sp{ano}l2.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada edição, de 1998 em diante, e o código de cada clube; confere placares, traz a rodada e completa os jogos que a página não traz). Artilheiros pela lista da RSSSF (`sp2tops.htm`). 2026 vem só do ogol (a RSSSF ainda não tem a página). Wikipédia em português (`data/coleta/bra-sp-2/wikipedia/`: o código das páginas de cada edição e os jogos transcritos delas em `jogos_pt.csv`, cada um conferido no código da página): 1965 e 1990 (sem página da RSSSF), os jogos que a RSSSF não traz (finais e fases finais de 1948-1966, a 4ª fase de 1990, a 2ª fase e o quadrangular de 1992, as semifinais de 1989). Lista de participantes da RSSSF (`sp2list.htm`): a cidade de cada clube de 1947 a 1966.

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela, fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` ou nos outros pacotes usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`). Acesso: o clube que joga a 1ª divisão do ano seguinte (pacote `bra-sp-1`).

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF; Wikipédia em 1965 e 1990): 128 tabelas fecham com os jogos e 31 divergem (cada divergência é explicada no relatório, na temporada).
- Temporadas com alguma tabela divergente: 1954, 1979, 1985, 1986, 1988, 1996, 1997, 1998, 1999, 2004, 2005, 2006, 2007, 2008, 2025.
- Temporadas sem tabela para conferir: 1947, 1950, 1951, 1952, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1987, 1989, 1991, 1992, 1993, 1994, 2001, 2014, 2022, 2023, 2024, 2026.
- Temporadas com menos jogos do que o ogol: nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|
| 1940s | 22 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 125 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 14 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 267 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 2645 | 98% | 0% | 56% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 1343 | 100% | 0% | 63% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 1884 | 100% | 22% | 98% | 0% | 0% | 0% | 0% | 0.0 |
| 2010s | 1888 | 100% | 98% | 96% | 0% | 0% | 0% | 57% | 0.0 |
| 2020s | 954 | 100% | 100% | 79% | 0% | 0% | 0% | 81% | 0.0 |

**Fonte de cada jogo:** RSSSF Brasil: 8699; Wikipédia (pt): 237; ogol: 206.

## 5. Formato ao longo do tempo

**Número de clubes:**

- 1947: 14 clubes
- 1948: 42 clubes
- 1949: 47 clubes
- 1950: 54 clubes
- 1951: 46 clubes
- 1952: 45 clubes
- 1953: 20 clubes
- 1954: 19 clubes
- 1955: 24 clubes
- 1956 a 1957: 32 clubes
- 1958: 38 clubes
- 1959: 39 clubes
- 1960: 11 clubes
- 1961 a 1965: 22 clubes
- 1966: 24 clubes
- 1979: 21 clubes
- 1985: 52 clubes
- 1986: 55 clubes
- 1987: 54 clubes
- 1988: 28 clubes
- 1989: 27 clubes
- 1990: 26 clubes
- 1991: 12 clubes
- 1992: 27 clubes
- 1993: 28 clubes
- 1994 a 1999: 16 clubes
- 2000: 18 clubes
- 2001: 16 clubes
- 2002 a 2003: 17 clubes
- 2004: 16 clubes
- 2005 a 2017: 20 clubes
- 2018 a 2026: 16 clubes

**Pontos por vitória:**

- 1947 a 1994: 2
- 1995 a 2026: 3

**Nome oficial:**

- 1947 a 1959: Campeonato Paulista Segunda Divisão
- 1960 a 1966: Campeonato Paulista Primeira Divisão
- 1979: Campeonato Paulista Divisão Intermediária
- 1985 a 1986: Campeonato Paulista Segunda Divisão
- 1987 a 1990: Campeonato Paulista Divisão Especial
- 1991 a 1993: Campeonato Paulista Divisão Intermediária
- 1994 a 2026: Campeonato Paulista Série A2

**Formato de cada edição** (fases na ordem; grupos; mata-mata):

- 1947: sem jogos (só a tabela final)
- 1948: jogos incompletos (os pontos de cada fase e 9 jogos: primeira fase - desempate, segunda fase, semifinal, final)
- 1949: jogos incompletos (os pontos de cada fase e 13 jogos: segunda fase, final)
- 1950: jogos incompletos (os pontos de cada fase e 4 jogos: final)
- 1951 a 1952: jogos incompletos (os pontos de cada fase e 1 jogo: final)
- 1953 a 1954: jogos incompletos (os pontos de cada fase e 30 jogos: segunda fase)
- 1955: jogos incompletos (os pontos de cada fase e 1 jogo: segunda fase)
- 1956: jogos incompletos (os pontos de cada fase e 3 jogos: final)
- 1957: jogos incompletos (os pontos de cada fase e 1 jogo: segunda fase)
- 1958: jogos incompletos (os pontos de cada fase e 3 jogos: final)
- 1959: jogos incompletos (os pontos de cada fase e 51 jogos: segunda fase)
- 1960: jogos incompletos (a tabela final e 1 jogo: primeira fase)
- 1961 a 1962: jogos incompletos (os pontos de cada fase e 3 jogos: final)
- 1963: jogos incompletos (os pontos de cada fase e 2 jogos: segunda fase)
- 1964: jogos incompletos (os pontos de cada fase e 1 jogo: segunda fase)
- 1965 a 1966: jogos incompletos (os pontos de cada fase e 2 jogos: final)
- 1979: 2 grupos + pontos corridos + mata-mata
- 1985: 4 grupos + pontos corridos
- 1986: 4 grupos + mata-mata + pontos corridos
- 1987: 6 grupos + 4 grupos + 2 grupos + mata-mata
- 1988: pontos corridos + 4 grupos + 2 grupos + mata-mata
- 1989: 2 grupos + mata-mata (jogos incompletos)
- 1990: jogos incompletos (a tabela final e 30 jogos: quarta fase)
- 1991: 2 grupos + pontos corridos (jogos incompletos)
- 1992: jogos incompletos (a ordem final e 42 jogos: segunda fase, fase final)
- 1993: sem jogos (só a ordem final)
- 1994: sem jogos (só a tabela final)
- 1995 a 1996: pontos corridos
- 1997: 2 grupos + pontos corridos
- 1998: pontos corridos
- 1999: 2 grupos + pontos corridos + 2 grupos + mata-mata
- 2000: 3 grupos + mata-mata + pontos corridos + mata-mata
- 2001: pontos corridos
- 2002: pontos corridos + mata-mata
- 2003: 2 grupos + mata-mata
- 2004: 4 grupos + pontos corridos
- 2005 a 2006: 2 grupos + mata-mata
- 2007 a 2009: pontos corridos + 2 grupos + mata-mata
- 2010: pontos corridos + 2 grupos
- 2011: 2 grupos + mata-mata
- 2012: pontos corridos + 2 grupos + mata-mata
- 2013: pontos corridos + mata-mata
- 2014 a 2015: pontos corridos
- 2016 a 2025: pontos corridos + mata-mata
- 2026: 2 grupos + mata-mata

**Fases que aparecem** (número de temporadas): Final (37); Primeira fase (35); Segunda fase (32); Semifinal (15); Fase final (9); Quartas de final (6); Torneio de rebaixamento (4); Fase única (3); Terceira fase (2); Primeira fase - Desempate (1); Repescagem (1); Mata-mata (1); Quarta fase (1); 1º Turno (1); 2º Turno (1); 3º Turno (1); Primeira fase - Semifinal (1); Primeira fase - Final (1).

**Observações das edições:**

- 1948: Sanjoanense licenciado (não jogou); 9 jogos da Wikipédia em português (primeira fase - desempate, segunda fase, semifinal, final)
- 1949: 13 jogos da Wikipédia em português (segunda fase, final)
- 1950: 4 jogos da Wikipédia em português (final)
- 1951: a repescagem XV de Jaú x Jabaquara (o último da 1ª divisão, três jogos) não é jogo da 2ª divisão e fica fora; 1 jogo da Wikipédia em português (final)
- 1952: 1 jogo da Wikipédia em português (final)
- 1953: 30 jogos da Wikipédia em português (segunda fase)
- 1954: 2ª fase: a página traz também uma tabela calculada dos jogos (Taubaté 16 e Comercial 11 pontos); vale a classificação oficial (14 e 13); 30 jogos da Wikipédia em português (segunda fase)
- 1955: 1 jogo da Wikipédia em português (segunda fase)
- 1956: 3 jogos da Wikipédia em português (final)
- 1957: AD Araraquara abandonou na 10ª rodada; os jogos dele foram anulados; 1 jogo da Wikipédia em português (segunda fase)
- 1958: 3 jogos da Wikipédia em português (final)
- 1959: 51 jogos da Wikipédia em português (segunda fase)
- 1960: 1 jogo da Wikipédia em português (primeira fase)
- 1961: 3 jogos da Wikipédia em português (final)
- 1962: 3 jogos da Wikipédia em português (final)
- 1963: 2 jogos da Wikipédia em português (segunda fase)
- 1964: 1 jogo da Wikipédia em português (segunda fase)
- 1965: sem página da RSSSF: as tabelas dos dois grupos e a final vêm da Wikipédia em português; 2 jogos da Wikipédia em português (final)
- 1966: 2 jogos da Wikipédia em português (final)
- 1988: 69 jogos da 1ª fase vêm na fonte sem placar (só quem venceu) e ficam fora
- 1989: jogos incompletos: a 1ª fase (RSSSF), as semifinais (Wikipédia) e a final (ogol); faltam a 2ª e a 3ª fase
- 1990: sem página da RSSSF: a Wikipédia em português traz a lista de participantes e só a 4ª fase (jogos e tabela); a ordem dos eliminados antes dela não é conhecida; 30 jogos da Wikipédia em português (quarta fase)
- 1991: jogos incompletos: só a 2ª fase e o quadrangular final (a 1ª fase não está em nenhuma fonte); campeão o Araçatuba, pelo saldo de gols (a página da RSSSF diz "Campeão: Lemense" por engano; a lista de campeões, a Wikipédia e o Futebol Interior dão o Araçatuba)
- 1992: Capivariano inscrito, não disputou; 42 jogos da Wikipédia em português (segunda fase, fase final); outros 6 vêm lá só com o resultado e ficam fora
- 1993: com a mudança das divisões da FPF, os clubes foram redistribuídos em 1994 (Série A2, A3 e B1)

## 6. Campeões, acessos, rebaixados e punições

**Títulos:**

- XV de Piracicaba: 3
- Ferroviária-SP: 3
- América-SP: 3
- São Caetano: 3
- Portuguesa: 3
- Santo André: 3
- Guarani: 2
- Linense: 2
- Taubaté: 2
- Bragantino: 2
- Mogi Mirim: 2
- Araçatuba: 2
- Inter de Limeira: 2
- Juventus-SP: 2
- São Bernardo: 2
- Capivariano: 2
- Radium: 1
- XV de Jaú: 1
- Noroeste: 1
- Botafogo-SP: 1
- Comercial-RP: 1
- Corinthians Prudente: 1
- Esportiva Guaratinguetá: 1
- Prudentina: 1
- São Bento: 1
- Portuguesa Santista: 1
- Bandeirante-SP: 1
- União São João: 1
- Ituano: 1
- Olímpia: 1
- Taquaritinga: 1
- Paraguaçuense: 1
- Matonense: 1
- União Barbarense: 1
- Paulista: 1
- Marília: 1
- Oeste: 1
- Barueri: 1
- Monte Azul: 1
- Ponte Preta: 1
- Velo Clube: 1

**Acessos:** 74 no total; quem mais teve: Noroeste (4), São Bento (4), Ponte Preta (3), Juventus-SP (3), Catanduvense (3), Botafogo-SP (3), Rio Claro (3), Oeste (3).

**Rebaixamentos:** 51 no total; quem mais teve: Olímpia (3), Marília (2), Noroeste (2), Taquaritinga (2), Nacional-SP (2), Bandeirante-SP (2), XV de Piracicaba (2), Juventus-SP (2).

**Punições em pontos:**

- nenhuma

## 7. Correções e decisões (com o motivo)

Registradas nos módulos de `coleta/bra-sp-2/`; cada uma também aparece no relatório, na temporada.

### Temporadas com o ogol como base dos jogos (`importar.BASE_OGOL`)

- **2026:** sem página da RSSSF: os jogos vêm do ogol

### Temporadas sem os jogos na RSSSF (só as tabelas) (`importar.SO_CLASSIFICACAO`)

- 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1990, 1992, 1993, 1994

### Temporadas completadas com jogos da Wikipédia (`importar.WIKI_JUNTAR`)

- 1989

### Temporadas com parte dos jogos (`importar.FORMATO_INCOMPLETO`)

- 1989, 1991

### Observações das edições (`importar.OBS_EDICAO`)

- **1948:** Sanjoanense licenciado (não jogou)
- **1954:** 2ª fase: a página traz também uma tabela calculada dos jogos (Taubaté 16 e Comercial 11 pontos); vale a classificação oficial (14 e 13)
- **1957:** AD Araraquara abandonou na 10ª rodada; os jogos dele foram anulados
- **1988:** 69 jogos da 1ª fase vêm na fonte sem placar (só quem venceu) e ficam fora
- **1951:** a repescagem XV de Jaú x Jabaquara (o último da 1ª divisão, três jogos) não é jogo da 2ª divisão e fica fora
- **1965:** sem página da RSSSF: as tabelas dos dois grupos e a final vêm da Wikipédia em português
- **1989:** jogos incompletos: a 1ª fase (RSSSF), as semifinais (Wikipédia) e a final (ogol); faltam a 2ª e a 3ª fase
- **1990:** sem página da RSSSF: a Wikipédia em português traz a lista de participantes e só a 4ª fase (jogos e tabela); a ordem dos eliminados antes dela não é conhecida
- **1991:** jogos incompletos: só a 2ª fase e o quadrangular final (a 1ª fase não está em nenhuma fonte); campeão o Araçatuba, pelo saldo de gols (a página da RSSSF diz "Campeão: Lemense" por engano; a lista de campeões, a Wikipédia e o Futebol Interior dão o Araçatuba)
- **1992:** Capivariano inscrito, não disputou
- **1993:** com a mudança das divisões da FPF, os clubes foram redistribuídos em 1994 (Série A2, A3 e B1)

### Nome da página casado à mão com o clube (`importar.NOME_MANUAL`)

- **1985 · Ferroviário:** [2543] Ferroviário Atlético Ituano (Itu) é o Ituano FC de hoje (o mesmo clube, com o nome antigo)
- **1985 · Ferroviário Ituano:** [2543] Ferroviário Atlético Ituano (Itu) é o Ituano FC de hoje (o mesmo clube, com o nome antigo)
- **1986 · Ferroviário:** [2543] Ferroviário Atlético Ituano (Itu) é o Ituano FC de hoje (o mesmo clube, com o nome antigo)
- **1986 · Ferroviário Ituano:** [2543] Ferroviário Atlético Ituano (Itu) é o Ituano FC de hoje (o mesmo clube, com o nome antigo)
- **1987 · Ferroviário:** [2543] Ferroviário Atlético Ituano (Itu) é o Ituano FC de hoje (o mesmo clube, com o nome antigo)
- **1987 · Ferroviário Ituano:** [2543] Ferroviário Atlético Ituano (Itu) é o Ituano FC de hoje (o mesmo clube, com o nome antigo)
- **1988 · Ferroviário:** [2543] Ferroviário Atlético Ituano (Itu) é o Ituano FC de hoje (o mesmo clube, com o nome antigo)
- **1988 · Ferroviário Ituano:** [2543] Ferroviário Atlético Ituano (Itu) é o Ituano FC de hoje (o mesmo clube, com o nome antigo)
- **1989 · Ferroviário:** [2543] Ferroviário Atlético Ituano (Itu) é o Ituano FC de hoje (o mesmo clube, com o nome antigo)
- **1989 · Ferroviário Ituano:** [2543] Ferroviário Atlético Ituano (Itu) é o Ituano FC de hoje (o mesmo clube, com o nome antigo)
- **1995 · Catanduva:** [15767] Catanduva EC é o novo nome do GE Catanduvense (nota da página de 1994 da RSSSF)
- **1995 · Internacional:** [3291] AA Internacional de Limeira (a página de 1995 não tem a lista de participantes; o clube jogou a A2 de 1994 e de 1996)
- **1995 · Botafogo:** [3154] Botafogo FC de Ribeirão Preto (a página de 1995 não tem a lista de participantes)
- **1995 · Nacional:** [3360] Nacional AC, da capital (a página de 1995 não tem a lista de participantes)
- **1996 · XV de Novembro:** [8229] EC XV de Novembro (Piracicaba), na lista de participantes
- **1997 · XV Piracicaba:** [8229] EC XV de Novembro (Piracicaba)

### Clube das edições antigas casado à mão (`importar.MANUAL_ANTIGO`)

- **AD São Caetano:** 2255
- **CA Bragantino:** red-bull-bragantino
- **Bragantino:** red-bull-bragantino
- **1994 · Catanduva:** 15767
- **1947 · XV Piracicaba:** 8229
- **1994 · São Caetano:** 2255

### Nome curto das fases seguintes casado à mão (edições antigas) (`importar.NOME_ANTIGO`)

- **1963 · Port. Santista:** AA Portuguesa
- **1963 · Corinthians-PP:** EC Corinthians
- **1963 · São Bento-M:** AA São Bento
- **1963 · Estrada:** Estrada de Ferro Sorocabana FC
- **1964 · Estrada:** Estrada de Ferro Sorocabana FC

### Nome da Wikipédia casado à mão (`importar.NOME_WIKI`)

- **1959 · AA São Bento:** rs-sao-bento-marilia
- **1959 · São Bento:** 3457
- **1962 · São Bento:** 3457
- **1963 · AA São Bento:** rs-sao-bento-marilia
- **1966 · Ferroviária:** 15766

### Grafias da página corrigidas (`importar.NOME_CORRIGIDO`)

- **AA Riopardende:** AA Riopardense
- **AA Rio Pardense:** AA Riopardense
- **AA Potofelicense:** AA Portofelicense
- **São Joanense:** Sanjoanense
- **SE Sãojoanense:** SE Sanjoanense
- **EC Sâo Bento:** EC São Bento
- **S. Bento:** São Bento
- **A.Brasil Clube:** Atlético Brasil Clube

### Cidades abreviadas nas tabelas antigas (`importar.CIDADES`)

- **Ara.:** Araraquara
- **Bot.:** Botucatu
- **B. Paulista:** Bragança Paulista
- **Br. Paulista:** Bragança Paulista
- **Birigüi:** Birigui
- **E.S. do Pinhal:** Espírito Santo do Pinhal
- **E.S.Pinhal:** Espírito Santo do Pinhal
- **Esp.Sto.do Pinhal:** Espírito Santo do Pinhal
- **Guará:** Guaratinguetá
- **Jau:** Jaú
- **Jundiai:** Jundiaí
- **Monte Azul:** Monte Azul Paulista
- **P. Prudente:** Presidente Prudente
- **P.Prudente:** Presidente Prudente
- **Pres. Prudente:** Presidente Prudente
- **Pres.Prudente:** Presidente Prudente
- **Pindamonhagaba:** Pindamonhangaba
- **Rib. Preto:** Ribeirão Preto
- **S. B. do Campo:** São Bernardo do Campo
- **São Bernardo Campo:** São Bernardo do Campo
- **S. Caetano do Sul:** São Caetano do Sul
- **S.Caetano do Sul:** São Caetano do Sul
- **São Caetano Sul:** São Caetano do Sul
- **S. Carlos:** São Carlos
- **S. J. da Barra:** São Joaquim da Barra
- **S. J. da Boa Vista:** São João da Boa Vista
- **S. João da Boa Vista:** São João da Boa Vista
- **São J. da Boa Vista:** São João da Boa Vista
- **S. J. do Rio Preto:** São José do Rio Preto
- **S. José do R. Preto:** São José do Rio Preto
- **S. José do Rio Preto:** São José do Rio Preto
- **S.José do R.Preto:** São José do Rio Preto
- **São J. do Rio Preto:** São José do Rio Preto
- **São José Rio Preto:** São José do Rio Preto
- **S. José do R Pardo:** São José do Rio Pardo
- **S. José do R. Pardo:** São José do Rio Pardo
- **S.José do R.Pardo:** São José do Rio Pardo
- **S. José dos Campos:** São José dos Campos
- **S. Paulo:** São Paulo
- **S.Manuel:** São Manuel
- **Sta. Cruz do Rio Pardo:** Santa Cruz do Rio Pardo
- **Uchôa:** Uchoa
- **Votuporan.:** Votuporanga

### Cidade de um clube corrigida (`importar.CIDADE_DO_CLUBE`)

- **votorantim · Sorocaba:** Votorantim
- **catanduva · Araçatuba:** Catanduva
- **irmaos romano · Santo André:** São Bernardo do Campo

### Cidade de uma linha de tabela corrigida (`importar.CIDADE_DA_LINHA`)

- **1948 · Série Branca · AA Internacional:** Bebedouro

### Fases da página renomeadas (por temporada) (`rsssf_sp2.FASE_ANO`)

- **1989:** 1º Turno → First Phase; 2º Turno → First Phase
- **1991:** 1º Turno → Second Phase; 2º Turno → Second Phase; Fase Final → Final Phase

### Grupos montados à mão (por temporada) (`rsssf_sp2.GRUPO_ANO`)

- **1989:** Capivariano → Grupo 1; Jacareí → Grupo 1; Nacional → Grupo 1; Rio Branco → Grupo 1; São Bernardo → Grupo 1; Taubaté → Grupo 1; União → Grupo 1; Ituano → Grupo 1; Independente → Grupo 1; Lemense → Grupo 1; Palmeiras → Grupo 1; Paulista → Grupo 1; Ponte Preta → Grupo 1; Bandeirante → Grupo 2; Corinthians → Grupo 2; Marília → Grupo 2; Mirassol → Grupo 2; Tanabi → Grupo 2; Taquaritinga → Grupo 2; VOCEM → Grupo 2; Comercial → Grupo 2; Fernandópolis → Grupo 2; Francana → Grupo 2; Linense → Grupo 2; Olímpia → Grupo 2; Rio Preto → Grupo 2; Votuporanguense → Grupo 2
- **1991:** Araçatuba → Série E; Independente → Série E; Jaboticabal → Série E; Mirassol → Série E; Radium → Série E; Taubaté → Série E; Barretos → Série F; Francana → Série F; Lemense → Série F; Nacional → Série F; Paulista → Série F; Tanabi → Série F

### Seções da Wikipédia -> fase e grupo (`wikipedia_sp2.FASE`)

- **1948 · Série Vermelha:** [Série Vermelha] Primeira fase - Desempate
- **1948 · Triangular final:** [] Segunda fase
- **1949 · Primeiro turno:** [] Segunda fase
- **1949 · Segundo turno:** [] Segunda fase
- **1949 · Jogo de desempate:** [] Final
- **1951 · Primeiro jogo:** None
- **1951 · Segundo jogo:** None
- **1951 · Terceiro jogo:** None
- **1953 · Primeiro turno:** [] Segunda fase
- **1953 · Segundo turno:** [] Segunda fase
- **1954 · Primeiro turno:** [] Segunda fase
- **1954 · Segundo turno:** [] Segunda fase
- **1955 · Penúltima partida da fase final:** [] Segunda fase
- **1957 · Última rodada do "Torneio dos Finalistas":** [] Segunda fase
- **1959 · Resultados da fase final:** [] Segunda fase
- **1959 · Jogo decisivo:** [] Segunda fase
- **1960 · Jogo decisivo:** [] Primeira fase
- **1962 · 1º jogo:** [] Final
- **1962 · 2º jogo:** [] Final
- **1962 · 3º jogo:** [] Final
- **1963 · Jogos decisivos:** [] Segunda fase
- **1964 · Forma de disputa:** [] Segunda fase
- **1988 · Jogo de ida:** None
- **1988 · Jogo de volta:** None
- **1990 · Quarta fase:** [] Quarta fase
- **1992 · Grupo E:** [Grupo E] Segunda fase
- **1992 · Grupo F:** [Grupo F] Segunda fase
- **1992 · Grupo G:** [Grupo G] Segunda fase
- **1992 · Quadrangular final:** [] Fase final

### Ocorrências explicadas, por temporada (`explicacoes.EXPLICACOES`)

- **1985:** Nacional x São Bernardo (31/08): a vitória foi dada ao São Bernardo no tribunal, sem placar (o jogo terminou 0 a 0 e o Nacional escalou jogador irregular); Barretos x Sãocarlense (18/08): vitória dada ao Barretos (1 a 1 em campo)
- **1948:** a Internacional da Série Branca é a de Bebedouro (Wikipédia); a página da RSSSF repete "(Limeira)"
- **1954:** 2ª fase: a página traz uma tabela calculada dos jogos (Taubaté 16, Comercial 11) e a classificação oficial (Taubaté 14, Comercial 13); vale a oficial. Os 30 jogos da Wikipédia fecham com a calculada
- **1988:** 69 jogos vêm na página só com o resultado ("venceu", "empatou", "perdeu" ou "-"), sem placar, e ficam fora do pacote; por isso as tabelas da 1ª fase não fecham. O ogol e a Wikipédia não têm esses jogos
- **1991:** campeão: Araçatuba, empatado em pontos com o Lemense no quadrangular e na frente pelo saldo. A página da RSSSF diz "Campeão: Lemense", mas a lista de campeões da RSSSF, a Wikipédia e o Futebol Interior dão o Araçatuba
- **1995:** a página não tem a lista de participantes: Internacional (de Limeira), Botafogo (de Ribeirão Preto), Nacional (da capital) e Catanduva (o GE Catanduvense, que mudou de nome em 1994) foram casados à mão
- **1997:** Ferroviária 1x1 Noroeste (23/02): jogo inacabado; a FPF deu a vitória à Ferroviária, e a tabela conta 1 a 0. A 1ª fase vai do jogo entre grupos (8 rodadas) ao turno e returno dentro dos grupos (14 rodadas), como nas tabelas da página (22 jogos por clube)
- **2000:** a 1ª fase tem semifinal e final próprias: o Botafogo venceu e subiu para a 1ª divisão no meio do ano (não joga a 2ª fase); o título da A2 é do vencedor da 2ª fase em diante
- **2001:** campeão: Etti Jundiaí, nome do Paulista FC de 1999 a 2001 (patrocínio)

### Clube do ogol casado à mão com o nome do banco (`clubes_sp2.MANUAL_DB`)

- **3333:** [J.Malucelli] o ogol escreve 'JMalucelli'; é o J. Malucelli do banco (Série A 2000)
- **24836:** [Novorizontino] Grêmio Novorizontino (2010-); o banco separou o GE Novorizontino (1973-1999) em 20/11/2026

### Nome de exibição de clube novo, dado à mão (`clubes_sp2.MANUAL_NOVO`)

- **68358:** [Corinthians Prudente] EC Corinthians de Presidente Prudente (1996): não é o Corinthians paulistano do banco
- **45210:** [Maringá] Maringá FC fundado em 2010 (Copa do Brasil 2025): não é o GE Maringá do banco
- **241210:** [Maringá FC 1995] Maringá FC fundado em 1995 (Copa do Brasil 1997): outro clube, nome como no ogol
- **60858:** [GE Novorizontino] Grêmio Esportivo Novorizontino (1973-1999, campeão de 1994): outro clube; o 'Novorizontino' do banco fica com o Grêmio Novorizontino, fundado em 2010 (decisão do Guilherme, 20/11/2026)
- **20122:** [Linhares EC] dois clubes de Linhares-ES: o EC (anos 1990) e o FC (anos 2000); o sufixo já distingue
- **9783:** [Linhares FC] dois clubes de Linhares-ES: o EC (anos 1990) e o FC (anos 2000); o sufixo já distingue
- **rs-uniao-mogi-das-cruzes:** [União Mogi] União FC de Mogi das Cruzes; "União-SP" não diz qual União paulista é
- **rs-internacional-bebedouro:** [Internacional de Bebedouro] AA Internacional de Bebedouro; o cadastro já tem "SC Internacional-SP" e "CA Internacional-SP", e o Inter de Limeira
- **rs-lemense-leme:** [EC Lemense] Esporte Clube Lemense (anos 1980): não é o Lemense FC, fundado em 2005 (ogol 24586)
- **rs-palmeiras-sao-joao-da-boa-vista:** [Palmeiras (São João da Boa Vista)] Palmeiras FC de São João da Boa Vista: nunca o nome exato do Palmeiras do banco (regra 6b)
- **rs-barretos:** [Barretos FC] Barretos Futebol Clube (até 1960); o Barretos EC, fundado em 1960, é o 24576 do ogol
- **rs-aracatuba:** [Araçatuba FC] Araçatuba Futebol Clube (1954-1955); a AE Araçatuba (ogol 19365) é de 1972
- **rs-sao-paulo-aracatuba:** [São Paulo (Araçatuba)] São Paulo FC de Araçatuba; "São Paulo-SP" seria o tricolor
- **rs-ferroviaria-botucatu:** [Ferroviária (Botucatu)] AA Ferroviária de Botucatu; a Ferroviária do banco é a de Araraquara
- **rs-comercial-limeira:** [Comercial (Limeira)] Comercial FC de Limeira
- **rs-comercial-lins:** [Comercial (Lins)] Comercial FC de Lins
- **rs-fortaleza-barretos:** [Fortaleza (Barretos)] Fortaleza EC de Barretos
- **rs-avenida-salto:** [Avenida (Salto)] AA Avenida de Salto
- **rs-rio-pardo-sao-jose-do-rio-pardo:** [Rio Pardo FC] Rio Pardo FC de São José do Rio Pardo
- **rs-osvaldo-cruz:** [AA Osvaldo Cruz] AA Osvaldo Cruz (1959-1966); o Osvaldo Cruz FC (ogol 15768) é de 2004
- **rs-estrada-de-ferro-sorocaba:** [Estrada de Ferro Sorocabana] Estrada de Ferro Sorocabana FC, de Sorocaba
- **rs-estrela-piquete:** [Estrela (Piquete)] EC Estrela de Piquete
- **rs-derac-araraquara:** [Derac (Araraquara)] EC D.E.R. de Araraquara; o "DERAC" dos anos 1980 é o de Itapetininga
- **rs-palestra-sao-bernardo-do-campo:** [Palestra São Bernardo] Palestra FC de São Bernardo do Campo
- **rs-catanduva:** [Catanduva EC] Catanduva EC (1955-1963); o GE Catanduvense (ogol 15767) é de 1970
- **rs-atletico-brasil-clube-paraguacu-paulista:** [Atlético Brasil] Atlético Brasil Clube de Paraguaçu Paulista
- **rs-sao-joao-jundiai:** [São João (Jundiaí)] São João FC de Jundiaí
- **rs-bauru:** [Bauru AC] Bauru Atlético Clube
- **rs-ferroviaria-assis:** [Ferroviária (Assis)] AA Ferroviária de Assis; a Ferroviária do banco é a de Araraquara
- **rs-comercial-araras:** [Comercial (Araras)] Comercial FC de Araras
- **rs-comercial-mogi-das-cruzes:** [Comercial (Mogi das Cruzes)] Comercial FC de Mogi das Cruzes
- **rs-ferroviaria-pindamonhangaba:** [Ferroviária (Pindamonhangaba)] AA Ferroviária de Pindamonhangaba
- **rs-sao-paulo-araraquara:** [São Paulo (Araraquara)] São Paulo FC de Araraquara; "São Paulo-SP" seria o tricolor

### Fichas do ogol com cidade ou estado errados (`clubes_sp2.FICHA_CORRIGIDA`)

- **39622:** cidade → São Paulo; uf → SP
- **59514:** cidade → São Paulo; uf → SP; estado → São Paulo; nome_completo → None; fundacao → None

### Páginas da RSSSF corrigidas na leitura (`rsssf.CORRECOES`, registradas em `coleta/bra-sp-2/rsssf_*.py`)

- **sp1947l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1948l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1949l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1950l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1951l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1952l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1953l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1954l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1955l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1956l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1957l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1958l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1959l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1960l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1961l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1962l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1963l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1964l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1965l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1966l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1967l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1968l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1969l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1970l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1971l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1972l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1973l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1974l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1975l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1976l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1977l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1978l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1979l2.htm:** letras trocadas por "�" na página; placar com travessão; datas "Jun 11" e "Jun 12" no meio dos jogos de julho (8 e 14 de julho); grafias do Ginásio Pinhalense
- **sp1980l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1981l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1982l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1983l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1984l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1985l2.htm:** letras trocadas por "�" na página; placar com travessão; duas linhas da lista de participantes coladas; o título da rodada 18, na coluna da direita, entra no meio da nota do jogo Barretos x Sãocarlense; a nota do jogo Nacional x São Bernardo, em coluna, se espalha por três linhas e cola no nome do Aparecida
- **sp1986l2.htm:** letras trocadas por "�" na página; placar com travessão; duas linhas da lista de participantes coladas
- **sp1987l2.htm:** letras trocadas por "�" na página; placar com travessão; data sem o ano na frente do jogo ("09/May"); turnos dentro do grupo
- **sp1988l2.htm:** letras trocadas por "�" na página; placar com travessão; data sem o ano na frente do jogo ("13/03"); turnos dentro da fase
- **sp1989l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1990l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1991l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1992l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1993l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1994l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1995l2.htm:** letras trocadas por "�" na página; placar com travessão; data sem o ano na frente do jogo ("29/Jan"); o "X" do XV de Jaú virou "-" na página
- **sp1996l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp1997l2.htm:** letras trocadas por "�" na página; placar com travessão; a 1ª fase vai até o returno dentro dos grupos ("SECOND STAGE"): as tabelas dos grupos somam as 22 rodadas; Ferroviária 1x1 Noroeste (23/02): jogo inacabado; a FPF deu a vitória à Ferroviária (a tabela conta 1-0); jogos e tabelas em quadros de duas colunas; o returno dentro dos grupos ("Second Phase") segue na 1ª fase; nome do Paraguaçuense com uma letra a menos (1ª rodada); o quadrangular final é a fase final
- **sp1998l2.htm:** letras trocadas por "�" na página; placar com travessão; rodadas em duas colunas; "Final Table:" é a tabela do quadrangular, não outra fase; o XV de Piracicaba aparece na tabela com o nome sem a cidade
- **sp1999l2.htm:** letras trocadas por "�" na página; placar com travessão; rodadas em duas colunas
- **sp2000l2.htm:** letras trocadas por "�" na página; placar com travessão; a 1ª fase tem semifinal e final próprias (o vencedor sobe para a 1ª divisão na 2ª fase)
- **sp2001l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2002l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2003l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2004l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2005l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2006l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2007l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2008l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2009l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2010l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2011l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2012l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2013l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2014l2.htm:** letras trocadas por "�" na página; placar com travessão; nome do Rio Branco quebrado, com a nota na mesma linha; nomes de clube quebrados em duas linhas
- **sp2015l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2016l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2017l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2018l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2019l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2020l2.htm:** letras trocadas por "�" na página; placar com travessão
- **sp2021l2.htm:** letras trocadas por "�" na página; placar com travessão; colchete solto depois do nome do Água Santa; pênaltis da final ("Penalty shootout")
- **sp2022l2.htm:** letras trocadas por "�" na página; placar com travessão; nome do São Bento quebrado, com os pênaltis na mesma linha; nomes de clube quebrados em duas linhas
- **sp2023l2.htm:** letras trocadas por "�" na página; placar com travessão; nomes de clube quebrados em duas linhas
- **sp2024l2.htm:** letras trocadas por "�" na página; placar com travessão; nomes de clube quebrados em duas linhas
- **sp2025l2.htm:** letras trocadas por "�" na página; placar com travessão

## 8. O que não deu para coletar

- **Jogos que faltam:** 1947-1966 (fora o que a Wikipédia traz), 1989 (2ª e 3ª fases), 1990 (1ª a 3ª fases), 1991
  (1ª fase), 1992 (1ª fase e 6 jogos só com o resultado), 1993 e 1994 (todos), 1988 (69 sem placar). Só há esses
  jogos em jornais da época (Hemeroteca Digital, acervos do Estadão e da Folha), em imagem.
- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).
- **Autores dos gols:** só onde a RSSSF traz (a partir de 2013) e a soma fecha com o placar.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;
  torneio de rebaixamento e repescagem não contam como fase alcançada.

## 9. Pendências e próximos passos

- Commit das edições antigas e da documentação (22/11/2026): pedir o ok do Guilherme. Depois, o agente 1 carregar a A2 no banco (recados no fim de docs/coleta/pedidos.md).
- Jogos que faltam (1947-1966 fora o que a Wikipédia traz; 1988: 69 sem placar; 1989: 2ª e 3ª fases; 1990: 1ª a 3ª; 1991: 1ª fase; 1992: 1ª fase; 1993 e 1994): só em jornais da época (Hemeroteca Digital, acervos do Estadão e da Folha), em imagem. Só se o Guilherme pedir.
- Os mesmos achados de vice e ordem final do Paulista (SP-002, SP-007, SP-008) podem valer na A2: conferir quando tratar o bra-sp-1 (o importador é cópia do dele).

## 10. Arquivos e comandos

| Arquivo | O que faz |
|---|---|
| `coleta/bra-sp-2/antigas_sp2.py` | Edições da A2 sem os jogos (1947-1966, 1992-1994): as tabelas de pontos das páginas da RSSSF. |
| `coleta/bra-sp-2/baixar_ogol.py` | Baixa o calendário de cada edição do Paulista Série A2 (2ª divisão) no ogol para data/coleta/bra-sp-2/ogol/sp2_{temporada}.json e a ficha de cada clube para data/coleta/bra-sp-2/ogol/clubes.json. |
| `coleta/bra-sp-2/baixar_rsssf.py` | Baixa as páginas da 2ª divisão paulista da RSSSF Brasil para data/coleta/bra-sp-2/rsssfbrasil/. |
| `coleta/bra-sp-2/clubes_sp2.py` | Identidade dos clubes da Copa do Brasil (mesmo método da Série C; clube já nomeado na Série C usa o mesmo nome). |
| `coleta/bra-sp-2/edicoes.py` | Edições do Campeonato Paulista Série A2 (2ª divisão, `bra-sp-2`): temporadas, anos e nomes oficiais. |
| `coleta/bra-sp-2/explicacoes.py` | Textos do relatório do Paulista Série A2 (2ª divisão) que não saem do código: introdução, explicações de cada temporada e o fim. |
| `coleta/bra-sp-2/importar.py` | Junta as fontes do Campeonato Paulista Série A2 (2ª divisão) e grava o pacote em data/coleta/bra-sp-2/pacote/ e o relatório em docs/coleta/bra-sp-2.md. Mesmo código do Paulista (coleta/bra-sp-1/importar.py), com as fonte |
| `coleta/bra-sp-2/pacote.py` | Grava o pacote do Campeonato Paulista Série A2 (data/coleta/bra-sp-2/pacote/) e o relatório (docs/coleta/bra-sp-2.md), no formato de docs/agente-coleta-COMECE-AQUI.md, seção 4. Chamado por importar.py. |
| `coleta/bra-sp-2/rsssf_sp2.py` | Leitura das páginas da 2ª divisão paulista da RSSSF Brasil (data/coleta/bra-sp-2/rsssfbrasil/sp{ano}l2.htm). |
| `coleta/bra-sp-2/wikipedia_sp2.py` | Jogos e tabelas da Wikipédia em português para as edições da A2 que a RSSSF não traz completas. |

- Fontes baixadas: `data/coleta/bra-sp-2/` (ogol, rsssfbrasil, wikipedia). Pacote: `data/coleta/bra-sp-2/pacote/`. Relatório: `docs/coleta/bra-sp-2.md`.
- Código comum: `coleta/comum/` (`rsssf.py` leitor das páginas da RSSSF Brasil, `ogol.py` calendários e fichas, `gols.py` autores dos gols, `registro.py` cadastro comum de nomes `data/coleta/comum/clubes_ogol.json`, `baixar.py` download educado).
- Refazer do zero (da raiz do `clube_analitico`, logs no scratchpad):

  - `python coleta/bra-sp-2/baixar_ogol.py` (ver o docstring)
  - `python coleta/bra-sp-2/baixar_rsssf.py` (ver o docstring)
  - `python coleta/bra-sp-2/importar.py` (grava o pacote e o relatório; `importar.py <ano>` só mostra, sem gravar)
  - `python coleta/comum/testar_carga.py bra-sp-2 <pasta temporária>` (deve terminar com `-> OK`)
  - `python coleta/comum/documentar.py`

