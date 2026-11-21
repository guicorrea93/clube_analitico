# Revisão: Campeonato Paulista, 1ª divisão (bra-sp-1)

Revisor: SP · 21/11/2026 (2ª rodada) · achados em `SCRATCH/achados_SP.csv` (SP-001 a SP-032) · scripts em `revisao/SP/`

**Resumo.** Os campeões batem em 133 das 134 edições; o erro é 1973, título dividido entre Santos e Portuguesa (SP-001). Os vices erram em 14 edições e o 3º em 29.
A causa é a classificação calculada: repescagem e torneio de rebaixamento contam como fase final; a fase final de verdade é ignorada; há clube trocado, jogo a mais, jogo faltando e punição ausente. Há um jogo falso, "Paulista 127 x 0 LAF" (1928), que virou o recorde de goleada do painel.
Achados: 10 altos, 12 médios, 8 baixos e 2 que não são erro.

Fontes de conferência: Wikipédia pt e en. Na pt foram usadas a lista de campeões (vice, 3º e 4º), a lista de artilheiros, as maiores goleadas e as 134 páginas de edição (infobox, tabelas e jogos). Na en, as listas de campeões e de artilheiros.
A coleta usou RSSSF e ogol como base e só a coluna de campeões da Wikipédia pt. Páginas guardadas em `data/cache/revisao/SP/`.
O site publicado (`https://clubeanalitico.pages.dev/dados/bra-sp-1.js` e `index.html`) é igual, byte a byte, ao `painel/` local. Os números do painel batem com o banco.

## A. Edições e títulos
- **Conferido:** a lista de edições; o campeão e o vice das 134 edições (listas en e pt); o 3º em 128 edições (lista pt).
- **Lista de edições:** as 134 do banco existem nas fontes, inclusive as ligas duplas (1913-1916 LPF/APEA, 1926-1929 APEA/LAF, 1935-1936 LPF/APEA).
  - Falta 2026, já disputado: Palmeiras campeão, Novorizontino vice → SP-004.
  - As listas pt/en têm também os campeonatos da FPF amadora de 1933 (Albion) e 1934 (Fiorentino) → SP-005 (pergunta).
  - 1970 e 1972-1974: falta a fase preliminar ("Paulistinha") → SP-006 (pergunta).
- **Campeões:** 133 de 134 certos, inclusive São Paulo 1931 (o da Floresta, como decidido), AA São Bento 1914/1925 e Ituano 2002.
  - Em 1973 só a Portuguesa aparece como campeã → SP-001.
- **Vices:** 119 de 134 certos.
  - Erram 1906, 1913 LPF, 1916 APEA, 1927 APEA, 1927 LAF, 1928 APEA, 1930, 1942, 1951, 1957, 1976, 1978, 1997 e 2003 → SP-002.
  - 1973 depende de SP-001.
  - Nas edições com 2 vices na fonte (1907, 1950, 1962, 1970), o banco tem um deles: ok.
- **3º lugar:** 98 de 128 certos → SP-003.
  - 2010 Barueri = Grêmio Prudente: é o mesmo clube, não é erro.

## B. Classificação final
- **Contra as tabelas das páginas pt:** 20 edições, com pelo menos uma por década.
  - Edições: 1909, 1919, 1924, 1927 APEA, 1927 LAF, 1929 LAF, 1930, 1938, 1942, 1953, 1959, 1964, 1970, 1971, 1984, 1996, 1997, 2008, 2015 e 2022.
  - Iguais: 1964, 1970 (fase principal), 1996, 2008 (menos o 3º/4º), 2015 e 1953/1959/1938 (diferenças de 1 jogo).
  - 2022: as diferenças são os jogos do Troféu do Interior que a Wikipédia soma. Não é erro.
  - Saída completa: `revisao/SP/saida_classificacao.txt`.
- **Fase decisiva errada:** repescagem ou torneio de rebaixamento como fase final em 1951, 1998, 1999 e 2003 → SP-007.
- **Fase final não usada:** 1957, 1976, 1978, 1997, 2024 e 2025 → SP-008.
- **Por edição:**
  - 1927 APEA: Corinthians de Santo André gravado como Corinthians → SP-009.
  - 1927 LAF: clubes e jogos a mais → SP-010.
  - 1942: falta Corinthians x Palmeiras → SP-012.
  - 1930: falta a punição do Palestra → SP-013.
  - 1988: Juventus-SP no lugar de outro clube → SP-014.
  - 1929 LAF: classificação diferente da fonte → SP-018.
- **Rebaixamento** (marca `rebaixado` comparada com a participação no ano seguinte, de 1947 a 2024) → SP-015.
  - Falta a marca em 2014, 2015, 2017-2020 e 2022-2024.
  - Há marca errada em 1994, 1998, 1999 e 2002.
  - A sub-aba Participantes ("no ano seguinte") está certa, porque olha o ano seguinte.
  - 2025 não tem marca e não dá para conferir sem a edição de 2026.
- **W.O. sem placar** fora da tabela (1905 e 1908-1910) → SP-016.
- **Desempate e pontos extras:**
  - 1971: o banco desempata por vitórias; o regulamento da época usa o saldo.
  - 1984: São Paulo com 53 pontos na fonte e 51 no banco.
  - 2008: 3º e 4º trocados.
  - → SP-017.
- **Pontos por vitória:** 2 até 1994 e 3 de 1995 em diante: ok (1994: Palmeiras 47 pontos com 20-7-3).

## C. Jogos
- **Total por edição:** pacote, banco e painel batem (21.855 jogos; o painel conta 21.839, sem os 16 jogos sem placar).
  - Contra o infobox pt (90 edições com o dado): 61 batem nos jogos e 35 nos gols.
  - As diferenças de 2008-2013 e 2017-2023 são o Troféu do Interior e a Taça Independência, tirados de propósito.
  - As outras estão em SP-019 (1916 LPF, 1920, 1921, 1928 APEA, 1935 APEA, 1957, 1958, 1960, 1977, 1999, 2002 e 2016), mais 1988 (SP-014).
- **Jogo a jogo:** 22 edições contra as listas e matrizes das páginas pt.
  - Antigas: 1904-1925 e 1929 LAF.
  - Do meio: 1945, 1946 e 1956. Só há listas parciais nesse período (jogos de um clube): 71 jogos.
  - Recentes: 2018 a 2025.
  - Resultado: 1.477 jogos achados, 1.464 com o mesmo placar (SP-031).
  - Diferenças → SP-020. Ruído de leitura (jogos de outra tabela): `revisao/SP/saida_jogos.txt`.
- **Jogos estranhos:**
  - jogo falso de 127 x 0 (SP-011);
  - "Corinthians x Corinthians" em 1927 (SP-009) e "Juventus x Juventus" em 1988 (SP-014);
  - jogos repetidos em 1927 APEA, 1956 e 1988;
  - 72 casos de clube com 2 jogos no mesmo dia (SP-021).
- **Textos:** observações dos jogos em inglês no pacote (SP-022).

## D. Gols e artilheiros
- **Gols com autor ≤ placar:** os 2.239 jogos com autor fecham exatamente (6.405 gols): ok (SP-032).
- **Artilheiros no banco:** só 13 edições, todas pela "contagem dos gols com autor".
  - Batem 5: 2011, 2015, 2016, 2020 e 2021.
  - Erram 8: 2001, 2009, 2010, 2012, 2013, 2017, 2019 e 2023 → SP-023.
  - A lista oficial (pt e en) tem 125 edições → SP-024.
- **Painel:** a aba Artilharia e o card "Maior artilheiro" mostram a contagem parcial em 10 edições com cobertura de 1% a 36% (ex.: 2025 "Gabriel, 2 gols") → SP-025.

## E. Clubes e escudos
- **Conferido:** os 115 clubes do Paulista (nome, cidade, nomes de fonte, anos) e a folha de contato com os 115 escudos (`SCRATCH/SP/escudos.png`).
- **Certos:** Palestra Itália = Palmeiras; Hespanha = Jabaquara; Fiorentino = Juventus; os homônimos antigos com "-SP" (SC Internacional-SP x Inter de Limeira, Americano-SP, Paulistano-SP); o São Bento da capital (1914-1932) separado do de Sorocaba; São Caetano EC (1935) separado da AD São Caetano.
- **Achados:**
  - AA São Bento duplicado em 1933 → SP-026.
  - "ECPaulista" (1935, São Carlos) x "CA Paulista" → SP-027.
  - Nomes de época e nomes estranhos no `clube_nome` → SP-028.
  - Escudos de Oeste e "LAF" ausentes → SP-029.
  - O clube falso "LAF" → SP-011.

## F. Painel (site publicado)
- **Telas:** 18 prints no computador e 5 no celular, todas as abas e sub-abas (`SCRATCH/SP/telas/`):
  - História: Corrida, Pódio, Participações, Jogos, Gols, Pontuação e Curiosidades;
  - Por campeonato: Resumo 1973, Classificação 2003, Participantes 2003, Corrida 2005, Jogos 1928 LAF e Artilharia 2025;
  - Por clube: Paulista, São Paulo, Corinthians, Paulistano e Santos.
- Sem erro de JavaScript nem tela quebrada.
- **Os números batem com o banco:** cartões (134 edições, 21.839 jogos, 64.729 gols), pódio das 134 edições e jogos/gols por edição.
- **Saltam aos olhos:**
  - "Maior goleada 127 x 0" (SP-011);
  - Botafogo-SP vice em 2003 e "Final" com 38 jogos em 2003 (SP-007);
  - Santos com 21 títulos (SP-001);
  - artilheiro de 2 gols em 2025 (SP-025).
- **Varredura de tela** (`revisao/SP/varredura.py` e `datas_repetidas.py`; saídas em `revisao/SP/*_saida.txt`):
  - 2 clubes contra eles mesmos, 4 jogos repetidos, 4 fases fora de ordem;
  - 5 "Final com jogos demais" (1969, 1981, 1997, 1998, 2003) e 3 pódios x final;
  - 4 semifinalistas fora do top 4 e 72 datas repetidas;
  - 34 "Grupo Grupo": o nome do grupo já vem com "Grupo" (1928 LAF, 1969, 1976-2004). É detalhe de exibição.
  - Nenhum campeão fora do 1º lugar e nenhuma posição repetida.
- **Celular:** a página fica mais larga que a tela (já conhecido) → SP-030.

## Perguntas ao Guilherme
1. **1973 (SP-001):** o título fica com os dois, Santos e Portuguesa, como a FPF? O painel hoje aceita um campeão só por edição.
2. **1933 e 1934 (SP-005):** reconhecer os campeonatos amadores da FPF (Albion e Fiorentino), que a Wikipédia lista ao lado dos da APEA?
3. **"Paulistinha" de 1970 e 1972-1974 (SP-006):** a fase preliminar entra na edição?
4. **AA São Bento (SP-026):** juntar "AA São Bento" e "São Bento de São Paulo" (1933) num clube só?
5. **CA Paulista e "ECPaulista" (SP-027):** juntar num clube só?
