# Campeonato Paulista (1ª divisão) — coleta de dados

Gerado por `python coleta/bra-sp-1/importar.py`. Pacote em `data/coleta/bra-sp-1/pacote/`. Método e
código iguais aos da Série C (`docs/coleta/bra-serie-c.md`).

**Temporadas:** 134, de 1902 a 2025. Nos anos de duas ligas (1913-1916 e 1935-1936: LPF e APEA; 1926-1929: APEA e LAF)
cada liga é uma temporada própria ("1913 LPF", "1913 APEA"), com o mesmo ano. Campeões conferidos na RSSSF Brasil
(spcamp.htm) e na Wikipédia em português ("Campeonato Paulista de Futebol").

**Fontes:** RSSSF Brasil (`sp{ano}.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada edição e o
código de cada clube; confere placares, traz a rodada e completa jogos); Wikipédia (lista de campeões).

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,
fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` ou nos pacotes
das Séries C e D e da Copa do Brasil usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).
Palestra Itália e Palmeiras são o mesmo clube (o ogol já os junta). Os homônimos antigos levam "-SP" quando o nome
já é de um clube de outro estado ("Internacional-SP").

**Fica de fora** o que a página da RSSSF (ou o calendário do ogol) traz junto e não é o campeonato: a seletiva de 1910;
os 2º e 3º níveis de 1985; o Troféu do Interior (2007-2013 e 2017-2022) e a Taça Independência (2023), torneios à parte
dos clubes já eliminados; e o Supercampeonato de 2002. As repescagens contra clubes da 2ª divisão (1951, 1979, 2003) entram,
como na RSSSF.

| Ano | Fontes | Clubes | Jogos (ogol) | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Classificação |
|---|---|---|---|---|---|---|---|---|
| 1902 | RSSSF + ogol | 5 | 21 (21) | 60 | 0 | 1 / 0 | São Paulo Athletic | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1903 | RSSSF + ogol | 5 | 21 (21) | 64 | 0 | 1 / 0 | São Paulo Athletic | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1904 | RSSSF + ogol | 6 | 31 (31) | 99 | 0 | 1 / 0 | São Paulo Athletic | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1905 | RSSSF + ogol | 6 | 30 (30) | 118 | 0 | 0 / 1 | Paulistano-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1906 | RSSSF + ogol | 6 | 23 (23) | 91 | 0 | 0 / 2 | Germânia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1907 | RSSSF + ogol | 6 | 30 (29) | 93 | 0 | 2 / 0 | SC Internacional-SP | RSSSF (classificação geral publicada) |
| 1908 | RSSSF + ogol | 6 | 30 (30) | 88 | 0 | 0 / 2 | Paulistano-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1909 | RSSSF + ogol | 6 | 31 (31) | 96 | 0 | 0 / 2 | AA das Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1910 | RSSSF + ogol | 6 | 30 (30) | 133 | 0 | 0 / 2 | AA das Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1911 | RSSSF + ogol | 6 | 24 (24) | 109 | 0 | 2 / 0 | São Paulo Athletic | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1912 | RSSSF + ogol | 7 | 42 (38) | 162 | 0 | 2 / 0 | Americano-SP | RSSSF (classificação geral publicada) |
| 1913 LPF | RSSSF + ogol | 6 | 24 (24) | 97 | 0 | 0 / 1 | Americano-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1913 APEA | RSSSF + ogol | 3 | 9 (9) | 36 | 0 | 1 / 0 | Paulistano-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1914 LPF | RSSSF + ogol | 7 | 32 (32) | 106 | 0 | 0 / 1 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1914 APEA | RSSSF + ogol | 6 | 30 (30) | 107 | 0 | 0 / 1 | AA São Bento | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1915 LPF | RSSSF + ogol | 7 | 42 (42) | 129 | 0 | 0 / 1 | Germânia | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1915 APEA | RSSSF + ogol | 6 | 29 (29) | 99 | 0 | 1 / 1 | AA das Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1916 LPF | RSSSF + ogol | 14 | 47 (51) | 119 | 0 | 0 / 1 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1916 APEA | RSSSF + ogol | 7 | 43 (43) | 184 | 0 | 0 / 1 | Paulistano-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1917 | RSSSF + ogol | 9 | 72 (72) | 301 | 0 | 0 / 1 | Paulistano-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1918 | RSSSF + ogol | 10 | 67 (67) | 333 | 0 | 0 / 2 | Paulistano-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1919 | RSSSF + ogol | 10 | 84 (84) | 385 | 0 | 0 / 1 | Paulistano-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1920 | RSSSF + ogol | 10 | 80 (80) | 391 | 0 | 0 / 1 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1921 | RSSSF + ogol | 12 | 132 (132) | 553 | 0 | 0 / 1 | Paulistano-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1922 | RSSSF + ogol | 12 | 94 (94) | 392 | 0 | 1 / 1 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1923 | RSSSF + ogol | 12 | 91 (83) | 331 | 0 | 0 / 2 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1924 | RSSSF + ogol | 12 | 87 (85) | 325 | 0 | 0 / 2 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1925 | RSSSF + ogol | 12 | 62 (55) | 219 | 0 | 0 / 1 | AA São Bento | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1926 APEA | RSSSF + ogol | 10 | 45 (45) | 198 | 0 | 0 / 1 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1926 LAF | RSSSF + ogol | 8 | 56 (56) | 257 | 0 | 1 / 0 | Paulistano-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1927 APEA | RSSSF + ogol | 14 | 92 (91) | 548 | 0 | 1 / 2 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1927 LAF | RSSSF + ogol | 15 | 71 (73) | 304 | 0 | 0 / 1 | Paulistano-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1928 APEA | RSSSF + ogol | 8 | 47 (42) | 212 | 0 | 0 / 1 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1928 LAF | RSSSF + ogol | 13 | 134 (134) | 691 | 0 | 0 / 1 | SC Internacional-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1929 APEA | RSSSF + ogol | 8 | 28 (28) | 144 | 0 | 1 / 0 | Corinthians | RSSSF (classificação geral publicada) |
| 1929 LAF | RSSSF + ogol | 12 | 116 (116) | 442 | 0 | 0 / 1 | Paulistano-SP | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1930 | RSSSF + ogol | 14 | 182 (182) | 808 | 0 | 0 / 1 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1931 | RSSSF + ogol | 14 | 182 (182) | 787 | 0 | 0 / 1 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1932 | RSSSF + ogol | 12 | 66 (66) | 322 | 0 | 0 / 1 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1933 | RSSSF + ogol | 8 | 57 (56) | 274 | 0 | 0 / 1 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1934 | RSSSF + ogol | 8 | 56 (56) | 219 | 0 | 0 / 1 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1935 LPF | RSSSF + ogol | 7 | 42 (42) | 164 | 0 | 0 / 1 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1935 APEA | RSSSF + ogol | 9 | 58 (58) | 277 | 0 | 0 / 1 | Portuguesa | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1936 LPF | RSSSF + ogol | 12 | 124 (124) | 561 | 0 | 0 / 1 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1936 APEA | RSSSF + ogol | 7 | 42 (42) | 177 | 0 | 2 / 0 | Portuguesa | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1937 | RSSSF + ogol | 10 | 60 (60) | 216 | 0 | 1 / 1 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1938 | RSSSF + ogol | 12 | 56 (56) | 214 | 0 | 0 / 1 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1939 | RSSSF + ogol | 11 | 110 (110) | 430 | 0 | 0 / 1 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1940 | RSSSF + ogol | 11 | 110 (110) | 481 | 0 | 0 / 0 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1941 | RSSSF + ogol | 11 | 110 (110) | 504 | 0 | 0 / 1 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1942 | RSSSF + ogol | 11 | 109 (100) | 567 | 0 | 0 / 1 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1943 | RSSSF + ogol | 11 | 110 (110) | 498 | 0 | 0 / 1 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1944 | RSSSF + ogol | 11 | 110 (110) | 471 | 0 | 0 / 1 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1945 | RSSSF + ogol | 11 | 110 (110) | 463 | 0 | 0 / 1 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1946 | RSSSF + ogol | 11 | 110 (110) | 444 | 0 | 0 / 1 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1947 | RSSSF + ogol | 11 | 110 (100) | 392 | 0 | 0 / 1 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1948 | RSSSF + ogol | 11 | 110 (110) | 415 | 0 | 0 / 1 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1949 | RSSSF + ogol | 12 | 132 (132) | 529 | 0 | 0 / 1 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1950 | RSSSF + ogol | 12 | 132 (132) | 471 | 0 | 0 / 1 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1951 | RSSSF + ogol | 16 | 213 (210) | 817 | 1 | 0 / 0 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1952 | RSSSF + ogol | 16 | 240 (240) | 852 | 0 | 0 / 0 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1953 | RSSSF + ogol | 15 | 210 (210) | 771 | 0 | 0 / 0 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1954 | RSSSF + ogol | 14 | 182 (182) | 647 | 0 | 0 / 0 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1955 | RSSSF + ogol | 14 | 182 (182) | 699 | 0 | 0 / 0 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1956 | RSSSF + ogol | 18 | 301 (300) | 1162 | 0 | 1 / 3 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1957 | RSSSF + ogol | 20 | 370 (200) | 1362 | 0 | 0 / 1 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1958 | RSSSF + ogol | 20 | 380 (200) | 1329 | 0 | 0 / 0 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1959 | RSSSF + ogol | 20 | 383 (383) | 1358 | 0 | 0 / 0 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1960 | RSSSF + ogol | 18 | 306 (306) | 1052 | 0 | 0 / 0 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1961 | RSSSF + ogol | 16 | 240 (240) | 878 | 0 | 0 / 0 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1962 | RSSSF + ogol | 16 | 240 (240) | 792 | 0 | 0 / 1 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1963 | RSSSF + ogol | 16 | 240 (240) | 767 | 0 | 0 / 0 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1964 | RSSSF + ogol | 16 | 240 (240) | 737 | 0 | 0 / 0 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1965 | RSSSF + ogol | 16 | 240 (100) | 731 | 0 | 0 / 0 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1966 | RSSSF + ogol | 15 | 210 (210) | 689 | 0 | 0 / 1 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1967 | RSSSF + ogol | 14 | 183 (100) | 524 | 0 | 0 / 1 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1968 | RSSSF + ogol | 14 | 182 (182) | 529 | 0 | 0 / 1 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1969 | RSSSF + ogol | 14 | 188 (187) | 527 | 0 | 1 / 2 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1970 | RSSSF + ogol | 10 | 90 (90) | 201 | 0 | 0 / 1 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1971 | RSSSF + ogol | 12 | 132 (132) | 347 | 0 | 0 / 0 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1972 | RSSSF + ogol | 12 | 132 (132) | 277 | 0 | 0 / 0 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1973 | RSSSF + ogol | 12 | 133 (133) | 260 | 0 | 2 / 0 | Portuguesa | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1974 | RSSSF + ogol | 14 | 184 (184) | 354 | 0 | 0 / 2 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1975 | RSSSF + ogol | 19 | 278 (278) | 622 | 0 | 1 / 3 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1976 | RSSSF + ogol | 18 | 219 (219) | 442 | 0 | 4 / 0 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1977 | RSSSF + ogol | 19 | 379 (378) | 874 | 0 | 2 / 0 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1978 | RSSSF + ogol | 20 | 444 (444) | 984 | 0 | 2 / 8 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1979 | RSSSF + ogol | 21 | 420 (417) | 825 | 0 | 6 / 0 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1980 | RSSSF + ogol | 21 | 395 (395) | 878 | 0 | 1 / 2 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1981 | RSSSF + ogol | 20 | 537 (537) | 1188 | 0 | 6 / 6 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1982 | RSSSF + ogol | 20 | 382 (382) | 754 | 0 | 1 / 2 | Corinthians | RSSSF (classificação geral publicada) |
| 1983 | RSSSF + ogol | 20 | 410 (410) | 781 | 0 | 4 / 2 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1984 | RSSSF + ogol | 20 | 380 (380) | 781 | 0 | 0 / 0 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1985 | RSSSF + ogol | 20 | 386 (386) | 738 | 0 | 1 / 2 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1986 | RSSSF + ogol | 20 | 386 (386) | 808 | 0 | 0 / 3 | Inter de Limeira | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1987 | RSSSF + ogol | 20 | 386 (386) | 720 | 0 | 0 / 1 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1988 | RSSSF + ogol | 22 | 239 (216) | 533 | 0 | 2 / 2 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1989 | RSSSF + ogol | 22 | 261 (261) | 507 | 0 | 6 / 0 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1990 | RSSSF + ogol | 24 | 422 (422) | 793 | 0 | 5 / 1 | Bragantino | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1991 | RSSSF + ogol | 28 | 390 (390) | 755 | 0 | 2 / 2 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1992 | RSSSF + ogol | 28 | 390 (390) | 888 | 0 | 2 / 2 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1993 | RSSSF + ogol | 30 | 448 (448) | 1171 | 0 | 4 / 0 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1994 | RSSSF + ogol | 16 | 240 (240) | 637 | 0 | 0 / 1 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1995 | RSSSF + ogol | 17 | 266 (266) | 646 | 0 | 2 / 1 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1996 | RSSSF + ogol | 16 | 240 (240) | 734 | 0 | 4 / 0 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1997 | RSSSF + ogol | 16 | 190 (190) | 611 | 0 | 5 / 3 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1998 | RSSSF + ogol | 16 | 138 (126) | 480 | 0 | 5 / 0 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 1999 | RSSSF + ogol | 16 | 174 (174) | 590 | 3 | 7 / 1 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2000 | RSSSF + ogol | 17 | 171 (170) | 537 | 15 | 14 / 2 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2001 | RSSSF + ogol | 16 | 126 (126) | 459 | 437 | 0 / 6 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2002 | RSSSF + ogol | 13 | 134 (132) | 425 | 0 | 0 / 2 | Ituano | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2003 | RSSSF + ogol | 22 | 111 (109) | 363 | 220 | 2 / 2 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2004 | RSSSF + ogol | 21 | 111 (110) | 360 | 326 | 1 / 1 | São Caetano | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2005 | RSSSF + ogol | 20 | 190 (190) | 610 | 0 | 0 / 2 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2006 | RSSSF + ogol | 20 | 190 (190) | 571 | 0 | 0 / 2 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2007 | RSSSF + ogol | 20 | 196 (196) | 591 | 0 | 1 / 0 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2008 | RSSSF + ogol | 20 | 196 (196) | 510 | 0 | 3 / 0 | Palmeiras | RSSSF (classificação geral publicada) |
| 2009 | RSSSF + ogol | 20 | 196 (202) | 560 | 546 | 3 / 0 | Corinthians | RSSSF (classificação geral publicada) |
| 2010 | RSSSF + ogol | 20 | 196 (202) | 623 | 623 | 0 / 2 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2011 | RSSSF + ogol | 20 | 198 (202) | 506 | 498 | 2 / 0 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2012 | RSSSF + ogol | 20 | 198 (202) | 609 | 595 | 2 / 0 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2013 | RSSSF + ogol | 20 | 198 (202) | 546 | 546 | 2 / 0 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2014 | RSSSF + ogol | 20 | 158 (158) | 421 | 387 | 0 / 0 | Ituano | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2015 | RSSSF + ogol | 20 | 158 (158) | 374 | 364 | 4 / 0 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2016 | RSSSF + ogol | 20 | 158 (158) | 411 | 405 | 9 / 1 | Santos | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2017 | RSSSF + ogol | 16 | 110 (121) | 280 | 273 | 11 / 0 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2018 | RSSSF + ogol | 16 | 110 (121) | 219 | 79 | 12 / 0 | Corinthians | RSSSF (classificação geral publicada) |
| 2019 | RSSSF + ogol | 16 | 110 (121) | 232 | 227 | 11 / 0 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2020 | RSSSF + ogol | 16 | 104 (110) | 227 | 224 | 5 / 0 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2021 | RSSSF + ogol | 16 | 104 (109) | 235 | 232 | 9 / 0 | São Paulo | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2022 | RSSSF + ogol | 16 | 104 (109) | 246 | 81 | 9 / 1 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2023 | RSSSF + ogol | 16 | 104 (109) | 230 | 222 | 5 / 0 | Palmeiras | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |
| 2024 | RSSSF + ogol | 16 | 104 (104) | 230 | 76 | 8 / 3 | Palmeiras | RSSSF (classificação geral publicada) |
| 2025 | RSSSF + ogol | 16 | 104 (104) | 252 | 25 | 0 / 0 | Corinthians | calculada (fase alcançada, pontos, vitórias, saldo, gols pró) |

## Conferência e correções, ano a ano

### 1902

- sem ocorrências

### 1903

- sem ocorrências

### 1904

- sem ocorrências

### 1905

- Paulistano x AA das Palmeiras não foi jogado e a vitória foi dada ao Paulistano sem placar ("awarded 0-0"); fica 0 a 0 com resultado especial, e por isso a campanha do Paulistano e a da AA das Palmeiras não fecham com a tabela publicada (que conta a vitória); o ogol registra 1 a 0
- tabela publicada x jogos — Fase única / -: Paulistano-SP tabela [10, 8, 2, 0, 20, 3] jogos [10, 7, 3, 0, 20, 3] — placar diverge entre RSSSF e ogol em Paulistano-SP x AA das Palmeiras (0-0 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: AA das Palmeiras tabela [10, 1, 1, 8, 10, 27] jogos [10, 1, 2, 7, 10, 27] — placar diverge entre RSSSF e ogol em Paulistano-SP x AA das Palmeiras (0-0 x 1-0) e nenhuma das versões fecha com a tabela; fica a RSSSF

### 1906

- tabela publicada x jogos — Fase única / -: Germânia tabela [8, 6, 0, 2, 16, 8] jogos [9, 7, 0, 2, 25, 9] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: SC Internacional-SP tabela [8, 4, 0, 4, 12, 13] jogos [10, 6, 0, 4, 23, 14] — a tabela conta 8 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: Paulistano-SP tabela [8, 1, 1, 6, 8, 21] jogos [8, 1, 1, 6, 10, 21] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Germânia tabela [8, 6, 0, 2, 16, 8] jogos [9, 7, 0, 2, 25, 9] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: SC Internacional-SP tabela [8, 4, 0, 4, 12, 13] jogos [10, 6, 0, 4, 23, 14] — a tabela conta 8 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: Paulistano-SP tabela [8, 1, 1, 6, 8, 21] jogos [8, 1, 1, 6, 10, 21] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1907

- placar corrigido pelo ogol — Germânia x SC Internacional-SP (1907-10-20): RSSSF 3-3, ogol 3-2; fica o do ogol, que fecha com a tabela publicada
- só na RSSSF (não achado no ogol): São Paulo Athletic None-None CA Internacional-SP (1907-11-15)

### 1908

- tabela publicada x jogos — Fase única / -: Paulistano-SP tabela [10, 6, 3, 1, 24, 17] jogos [9, 5, 3, 1, 24, 17] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: Americano-SP tabela [10, 6, 2, 2, 15, 10] jogos [7, 3, 2, 2, 15, 10] — a tabela conta 10 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase única / -: SC Internacional-SP tabela [10, 5, 3, 2, 20, 12] jogos [9, 4, 3, 2, 20, 12] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: São Paulo Athletic tabela [10, 2, 0, 8, 7, 27] jogos [7, 1, 0, 6, 7, 27] — a tabela conta 10 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase única / -: CA Internacional-SP tabela [10, 0, 0, 10, 0, 14] jogos [6, 0, 0, 6, 0, 14] — a tabela conta 10 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase única / -: Paulistano-SP tabela [10, 6, 3, 1, 24, 17] jogos [9, 5, 3, 1, 24, 17] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: Americano-SP tabela [10, 6, 2, 2, 15, 10] jogos [7, 3, 2, 2, 15, 10] — a tabela conta 10 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase única / -: SC Internacional-SP tabela [10, 5, 3, 2, 20, 12] jogos [9, 4, 3, 2, 20, 12] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: São Paulo Athletic tabela [10, 2, 0, 8, 7, 27] jogos [7, 1, 0, 6, 7, 27] — a tabela conta 10 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase única / -: CA Internacional-SP tabela [10, 0, 0, 10, 0, 14] jogos [6, 0, 0, 6, 0, 14] — a tabela conta 10 jogos e as fontes trazem 6
- campeão pela lista oficial, Paulistano-SP; o 1º pela soma dos jogos da última fase é Germânia (desempate, jogo extra ou pontos tirados fora de campo)

### 1909

- tabela publicada x jogos — Fase única / -: AA das Palmeiras tabela [10, 6, 2, 2, 18, 8] jogos [10, 6, 2, 2, 19, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Paulistano-SP tabela [10, 5, 4, 1, 26, 12] jogos [11, 5, 4, 2, 27, 14] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Germânia tabela [10, 2, 1, 7, 11, 22] jogos [8, 2, 1, 5, 12, 21] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase única / -: AA das Palmeiras tabela [10, 6, 2, 2, 18, 8] jogos [9, 5, 2, 2, 17, 9] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: Germânia tabela [10, 2, 1, 7, 11, 22] jogos [8, 2, 1, 5, 12, 21] — a tabela conta 10 jogos e as fontes trazem 8

### 1910

- tabela publicada x jogos — Fase única / -: Americano-SP tabela [10, 8, 0, 2, 25, 18] jogos [9, 7, 0, 2, 24, 16] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: Paulistano-SP tabela [10, 3, 2, 5, 19, 17] jogos [8, 3, 2, 3, 17, 16] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase única / -: Germânia tabela [10, 1, 1, 8, 14, 31] jogos [9, 0, 1, 8, 14, 31] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: Americano-SP tabela [10, 8, 0, 2, 25, 18] jogos [9, 7, 0, 2, 24, 16] — a tabela conta 10 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: Paulistano-SP tabela [10, 3, 2, 5, 19, 17] jogos [8, 3, 2, 3, 17, 16] — a tabela conta 10 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase única / -: Germânia tabela [10, 1, 1, 8, 14, 31] jogos [9, 0, 1, 8, 14, 31] — a tabela conta 10 jogos e as fontes trazem 9

### 1911

- sem ocorrências

### 1912

- só na RSSSF (não achado no ogol): SC Internacional-SP None-None Americano-SP (1912-10-27)
- só na RSSSF (não achado no ogol): Mackenzie-SP None-None Paulistano-SP (1912-10-27)
- só na RSSSF (não achado no ogol): São Paulo Athletic None-None Paulistano-SP (1912-10-27)
- só na RSSSF (não achado no ogol): SC Internacional-SP None-None Mackenzie-SP (1912-10-27)

### 1913 LPF

- tabela publicada x jogos — Fase única / -: Americano-SP tabela [8, 5, 3, 0, 24, 5] jogos [9, 6, 3, 0, 30, 6] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: SC Internacional-SP tabela [8, 3, 2, 3, 14, 13] jogos [9, 4, 2, 3, 19, 14] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: Corinthians tabela [8, 1, 4, 3, 8, 16] jogos [9, 1, 4, 4, 11, 22] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: Germânia tabela [8, 2, 0, 6, 9, 23] jogos [9, 3, 0, 6, 17, 25] — a tabela conta 8 jogos e as fontes trazem 9

### 1913 APEA

- sem ocorrências

### 1914 LPF

- tabela publicada x jogos — Fase única / -: Corinthians tabela [8, 8, 0, 0, 30, 7] jogos [10, 10, 0, 0, 37, 9] — a tabela conta 8 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: Campos Elyseos tabela [7, 4, 0, 3, 12, 14] jogos [10, 5, 1, 4, 16, 24] — a tabela conta 7 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: Minas Gerais FC tabela [7, 2, 2, 3, 9, 12] jogos [10, 2, 2, 6, 9, 18] — a tabela conta 7 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: SC Internacional-SP tabela [8, 2, 1, 5, 13, 19] jogos [10, 3, 1, 6, 14, 20] — a tabela conta 8 jogos e as fontes trazem 10
- tabela publicada x jogos — Fase única / -: Luzitano-SP tabela [8, 1, 1, 6, 6, 18] jogos [10, 2, 1, 7, 7, 19] — a tabela conta 8 jogos e as fontes trazem 10

### 1914 APEA

- campeão: Associação Atlética São Bento (o São Bento da capital, extinto; não é o de Sorocaba)
- tabela publicada x jogos — Fase única / -: Paulistano-SP tabela [10, 7, 0, 3, 22, 15] jogos [10, 7, 0, 3, 23, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Mackenzie-SP tabela [10, 5, 1, 4, 20, 14] jogos [10, 5, 1, 4, 20, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Scottish Wanderers tabela [10, 2, 1, 7, 13, 23] jogos [10, 2, 1, 7, 13, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1915 LPF

- tabela publicada x jogos — Fase única / -: Maranhão-SP tabela [12, 2, 1, 9, 10, 22] jogos [12, 2, 1, 9, 11, 30] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Vicentino tabela [12, 2, 1, 9, 11, 30] jogos [12, 2, 1, 9, 10, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1915 APEA

- tabela publicada x jogos — Fase única / -: AA São Bento tabela [10, 0, 1, 9, 5, 20] jogos [9, 0, 1, 8, 5, 20] — a tabela conta 10 jogos e as fontes trazem 9

### 1916 LPF

- tabela publicada x jogos — Fase única / -: Corinthians tabela [8, 8, 0, 0, 20, 3] jogos [7, 7, 0, 0, 20, 3] — a tabela conta 8 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase única / -: União Lapa tabela [8, 5, 0, 3, 14, 18] jogos [9, 6, 0, 3, 16, 19] — a tabela conta 8 jogos e as fontes trazem 9
- tabela publicada x jogos — Fase única / -: Alumni-SP tabela [7, 4, 2, 1, 6, 8] jogos [8, 4, 2, 2, 7, 11] — a tabela conta 7 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase única / -: Minas Gerais FC tabela [7, 2, 3, 2, 6, 8] jogos [6, 1, 3, 2, 6, 8] — a tabela conta 7 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase única / -: Paysandu-SP tabela [9, 2, 3, 4, 4, 9] jogos [8, 1, 3, 4, 4, 9] — a tabela conta 9 jogos e as fontes trazem 8
- tabela publicada x jogos — Fase única / -: Americano-SP tabela [5, 2, 2, 1, 13, 3] jogos [6, 3, 2, 1, 17, 3] — a tabela conta 5 jogos e as fontes trazem 6
- tabela publicada x jogos — Fase única / -: Ítalo tabela [6, 2, 1, 3, 5, 8] jogos [7, 3, 1, 3, 8, 8] — a tabela conta 6 jogos e as fontes trazem 7
- tabela publicada x jogos — Fase única / -: Vicentino tabela [7, 2, 1, 4, 7, 11] jogos [7, 1, 1, 5, 7, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Ruggerone tabela [11, 1, 1, 9, 2, 8] jogos [8, 2, 1, 5, 5, 9] — a tabela conta 11 jogos e as fontes trazem 8

### 1916 APEA

- tabela publicada x jogos — Fase única / -: Mackenzie-SP tabela [12, 6, 1, 5, 27, 23] jogos [13, 6, 1, 6, 30, 28] — a tabela conta 12 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase única / -: Ypiranga-SP tabela [12, 6, 1, 5, 19, 19] jogos [13, 7, 1, 5, 24, 22] — a tabela conta 12 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase única / -: Palmeiras tabela [12, 2, 2, 8, 16, 26] jogos [13, 3, 2, 8, 20, 27] — a tabela conta 12 jogos e as fontes trazem 13

### 1917

- tabela publicada x jogos — Fase única / -: Santos tabela [16, 8, 2, 6, 44, 36] jogos [16, 8, 3, 5, 45, 36] — placar diverge entre RSSSF e ogol em Ypiranga-SP x Santos (4-2 x 4-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: AA São Bento tabela [16, 3, 3, 10, 23, 41] jogos [16, 3, 3, 10, 23, 42] — placar diverge entre RSSSF e ogol em Corinthians x AA São Bento (8-3 x 8-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: Mackenzie-SP tabela [16, 1, 3, 12, 21, 40] jogos [16, 1, 4, 11, 21, 40] — placar diverge entre RSSSF e ogol em Ypiranga-SP x Mackenzie-SP (7-2 x 7-0) e nenhuma das versões fecha com a tabela; fica a RSSSF
- placar diferente no ogol — Palmeiras x SC Internacional-SP (1917-04-21): RSSSF 5-1, ogol 5-0; fica o da RSSSF
- placar diferente no ogol — Paulistano-SP x SC Internacional-SP (1917-05-06): RSSSF 4-1, ogol 4-0; fica o da RSSSF
- placar diferente no ogol — Ypiranga-SP x Mackenzie-SP (1917-05-13): RSSSF 7-2, ogol 7-0; fica o da RSSSF
- placar diferente no ogol — Corinthians x SC Internacional-SP (1917-05-17): RSSSF 5-2, ogol 5-0; fica o da RSSSF
- placar diferente no ogol — Ypiranga-SP x Santos (1917-05-20): RSSSF 4-2, ogol 4-0; fica o da RSSSF
- placar diferente no ogol — Paulistano-SP x Mackenzie-SP (1917-05-20): RSSSF 4-3, ogol 4-0; fica o da RSSSF
- placar diferente no ogol — Corinthians x AA São Bento (1917-05-27): RSSSF 8-3, ogol 8-0; fica o da RSSSF
- placar diferente no ogol — Santos x AA São Bento (1917-06-03): RSSSF 5-1, ogol 5-0; fica o da RSSSF
- placar diferente no ogol — Paulistano-SP x Corinthians (1917-06-29): RSSSF 2-1, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Palmeiras x Ypiranga-SP (1917-06-29): RSSSF 2-1, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — AA das Palmeiras x Santos (1917-07-01): RSSSF 9-4, ogol 9-0; fica o da RSSSF
- placar diferente no ogol — Paulistano-SP x AA São Bento (1917-07-15): RSSSF 3-2, ogol 3-0; fica o da RSSSF
- placar diferente no ogol — Palmeiras x SC Internacional-SP (1917-07-15): RSSSF 4-3, ogol 4-0; fica o da RSSSF
- placar diferente no ogol — Santos x Mackenzie-SP (1917-08-05): RSSSF 2-1, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — Ypiranga-SP x AA São Bento (1917-08-12): RSSSF 4-2, ogol 4-0; fica o da RSSSF
- placar diferente no ogol — Santos x SC Internacional-SP (1917-08-12): RSSSF 4-2, ogol 4-0; fica o da RSSSF
- placar diferente no ogol — Paulistano-SP x SC Internacional-SP (1917-09-02): RSSSF 5-1, ogol 5-0; fica o da RSSSF
- placar diferente no ogol — SC Internacional-SP x Mackenzie-SP (1917-09-23): RSSSF 3-2, ogol 3-0; fica o da RSSSF
- placar diferente no ogol — SC Internacional-SP x Ypiranga-SP (1917-10-14): RSSSF 3-2, ogol 3-0; fica o da RSSSF
- placar diferente no ogol — AA São Bento x Mackenzie-SP (1917-10-28): RSSSF 2-1, ogol 2-0; fica o da RSSSF
- placar diferente no ogol — AA das Palmeiras x SC Internacional-SP (1917-11-04): RSSSF 4-2, ogol 4-0; fica o da RSSSF
- placar diferente no ogol — Palmeiras x Ypiranga-SP (1917-11-25): RSSSF 6-1, ogol 6-0; fica o da RSSSF
- jogo só no ogol, incluído em Fase única: AA São Bento 0-1 Santos (1917-11-25)

### 1918

- tabela publicada x jogos — Fase única / -: Paulistano-SP tabela [15, 12, 0, 3, 65, 11] jogos [16, 13, 0, 3, 68, 14] — a tabela conta 15 jogos e as fontes trazem 16
- tabela publicada x jogos — Fase única / -: Corinthians tabela [15, 11, 1, 3, 57, 15] jogos [17, 12, 2, 3, 65, 19] — a tabela conta 15 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase única / -: AA São Bento tabela [12, 4, 2, 6, 39, 34] jogos [14, 5, 2, 7, 43, 40] — a tabela conta 12 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase única / -: SC Internacional-SP tabela [14, 2, 0, 12, 16, 64] jogos [15, 2, 0, 13, 17, 66] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase única / -: Minas Gerais FC tabela [12, 2, 1, 9, 9, 48] jogos [13, 2, 1, 10, 9, 54] — a tabela conta 12 jogos e as fontes trazem 13

### 1919

- tabela publicada x jogos — Fase única / -: Santos tabela [18, 6, 1, 11, 36, 43] jogos [18, 6, 2, 10, 36, 43] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Minas Gerais FC tabela [15, 4, 2, 9, 18, 49] jogos [15, 3, 3, 9, 19, 49] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Mackenzie-SP tabela [15, 1, 0, 14, 11, 57] jogos [15, 1, 0, 14, 11, 58] — há jogo do clube sem conferência no ogol
- jogo só no ogol, incluído em Fase única: Mackenzie-SP 0-1 Minas Gerais FC (1919-06-01)
- jogo só no ogol, incluído em Fase única: Minas Gerais FC 0-0 Santos (1919-11-30)

### 1920

- tabela publicada x jogos — Fase única / -: Palmeiras tabela [16, 12, 2, 2, 55, 9] jogos [18, 14, 2, 2, 58, 11] — a tabela conta 16 jogos e as fontes trazem 18
- tabela publicada x jogos — Fase única / -: Paulistano-SP tabela [16, 12, 2, 2, 63, 21] jogos [18, 13, 2, 3, 68, 23] — a tabela conta 16 jogos e as fontes trazem 18
- tabela publicada x jogos — Fase única / -: Corinthians tabela [16, 12, 1, 3, 64, 21] jogos [17, 13, 1, 3, 75, 21] — a tabela conta 16 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase única / -: AA São Bento tabela [16, 9, 1, 6, 34, 25] jogos [17, 10, 1, 6, 36, 26] — a tabela conta 16 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase única / -: Ypiranga-SP tabela [16, 6, 3, 7, 31, 31] jogos [17, 7, 3, 7, 38, 31] — a tabela conta 16 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase única / -: SC Internacional-SP tabela [16, 5, 1, 10, 24, 57] jogos [17, 5, 1, 11, 24, 61] — a tabela conta 16 jogos e as fontes trazem 17
- tabela publicada x jogos — Fase única / -: AA das Palmeiras tabela [16, 2, 1, 13, 17, 73] jogos [17, 3, 1, 13, 22, 77] — a tabela conta 16 jogos e as fontes trazem 17
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AA Palmeiras
- AA Palmeiras — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (AA das Palmeiras)

### 1921

- tabela publicada x jogos — Fase única / -: Paulistano-SP tabela [22, 19, 1, 2, 98, 14] jogos [22, 20, 1, 1, 98, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Ypiranga-SP tabela [22, 9, 4, 9, 35, 58] jogos [22, 8, 4, 10, 35, 58] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1922

- tabela publicada x jogos — 1º Turno / -: EC Sírio tabela [11, 8, 2, 1, 28, 14] jogos [12, 9, 2, 1, 31, 16] — a tabela conta 11 jogos e as fontes trazem 12
- tabela publicada x jogos — 1º Turno / -: AA das Palmeiras tabela [11, 4, 3, 4, 26, 20] jogos [12, 4, 3, 5, 28, 23] — a tabela conta 11 jogos e as fontes trazem 12
- jogo só no ogol, incluído em Primeiro Turno: Germânia 1-3 Santos (1922-04-23)
- jogo só no ogol, incluído em Primeiro Turno: AA das Palmeiras 2-3 EC Sírio (1922-11-26)
- campeão pela lista oficial, Corinthians; o 1º pela soma dos jogos da última fase é Palmeiras (desempate, jogo extra ou pontos tirados fora de campo)

### 1923

- tabela publicada x jogos — 1º Turno / -: Palmeiras tabela [10, 6, 1, 3, 24, 14] jogos [11, 6, 2, 3, 27, 17] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 1º Turno / -: EC Sírio tabela [10, 5, 3, 2, 16, 9] jogos [11, 5, 3, 3, 16, 12] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 1º Turno / -: AA São Bento tabela [10, 5, 2, 3, 20, 19] jogos [11, 5, 2, 4, 20, 22] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 1º Turno / -: Portuguesa tabela [10, 3, 4, 3, 15, 13] jogos [11, 3, 4, 4, 16, 17] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 1º Turno / -: Ypiranga-SP tabela [10, 3, 3, 4, 12, 12] jogos [11, 3, 4, 4, 12, 12] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 1º Turno / -: Santos tabela [10, 2, 3, 5, 12, 19] jogos [11, 2, 3, 6, 12, 21] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 1º Turno / -: SC Internacional-SP tabela [10, 1, 1, 8, 10, 37] jogos [11, 1, 1, 9, 10, 43] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 1º Turno / -: Minas Gerais FC tabela [10, 0, 3, 7, 13, 28] jogos [11, 0, 4, 7, 16, 31] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 1º Turno / -: Corinthians tabela [17, 14, 1, 2, 53, 14] jogos [17, 14, 1, 2, 54, 14] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Palmeiras tabela [17, 11, 2, 4, 44, 22] jogos [18, 11, 3, 4, 44, 23] — a tabela conta 17 jogos e as fontes trazem 18
- tabela publicada x jogos — 1º Turno / -: EC Sírio tabela [17, 10, 3, 4, 35, 20] jogos [18, 10, 3, 5, 35, 21] — a tabela conta 17 jogos e as fontes trazem 18
- tabela publicada x jogos — 1º Turno / -: AA São Bento tabela [17, 8, 3, 6, 35, 33] jogos [18, 8, 3, 7, 35, 33] — a tabela conta 17 jogos e as fontes trazem 18
- tabela publicada x jogos — 1º Turno / -: Portuguesa tabela [17, 6, 6, 5, 25, 25] jogos [18, 6, 6, 6, 25, 25] — a tabela conta 17 jogos e as fontes trazem 18
- tabela publicada x jogos — 1º Turno / -: Ypiranga-SP tabela [17, 5, 5, 7, 22, 24] jogos [18, 5, 6, 7, 22, 24] — a tabela conta 17 jogos e as fontes trazem 18
- tabela publicada x jogos — 1º Turno / -: Germânia tabela [17, 6, 2, 9, 27, 42] jogos [17, 6, 2, 9, 28, 42] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / -: Santos tabela [10, 2, 3, 5, 12, 19] jogos [11, 2, 3, 6, 12, 21] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 1º Turno / -: SC Internacional-SP tabela [10, 1, 1, 8, 10, 37] jogos [11, 1, 1, 9, 10, 43] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 1º Turno / -: Minas Gerais FC tabela [10, 0, 3, 7, 13, 28] jogos [11, 0, 4, 7, 16, 31] — a tabela conta 10 jogos e as fontes trazem 11
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Paulistano
- Paulistano — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Paulistano-SP)
- jogo só no ogol, incluído em Primeiro Turno: Corinthians 4-1 Portuguesa (1923-04-22)
- jogo só no ogol, incluído em Segundo Turno: AA São Bento 2-2 Ypiranga-SP (1923-08-19)
- jogo só no ogol, incluído em Segundo Turno: Palmeiras 0-1 Corinthians (1923-09-16)
- só na RSSSF (não achado no ogol): Paulistano-SP 3-0 EC Sírio (1923-04-22)
- só na RSSSF (não achado no ogol): Paulistano-SP 3-0 AA São Bento (1923-05-06)
- só na RSSSF (não achado no ogol): Paulistano-SP 3-3 Minas Gerais FC (1923-05-13)
- só na RSSSF (não achado no ogol): Paulistano-SP 4-1 Portuguesa (1923-05-27)
- só na RSSSF (não achado no ogol): Santos 0-2 Paulistano-SP (1923-06-10)
- só na RSSSF (não achado no ogol): Paulistano-SP 6-0 SC Internacional-SP (1923-06-17)
- só na RSSSF (não achado no ogol): Palmeiras 3-3 Paulistano-SP (1923-06-24)
- só na RSSSF (não achado no ogol): Ypiranga-SP 0-0 Paulistano-SP (1923-07-01)
- campeão pela lista oficial, Corinthians; o 1º pela soma dos jogos da última fase é Palmeiras (desempate, jogo extra ou pontos tirados fora de campo)

### 1924

- tabela publicada x jogos — 1º Turno / -: Paulistano-SP tabela [10, 6, 2, 2, 20, 12] jogos [11, 7, 2, 2, 23, 13] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 1º Turno / -: Minas Gerais FC tabela [10, 3, 2, 5, 17, 24] jogos [11, 4, 2, 5, 20, 26] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — 3. AA das Palmeiras  0 eliminated / -: Paulistano-SP tabela [17, 10, 3, 4, 31, 15] jogos [18, 11, 3, 4, 34, 16] — a tabela conta 17 jogos e as fontes trazem 18
- tabela publicada x jogos — 3. AA das Palmeiras  0 eliminated / -: AA São Bento tabela [17, 9, 4, 4, 30, 20] jogos [17, 9, 4, 4, 31, 20] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3. AA das Palmeiras  0 eliminated / -: Santos tabela [17, 9, 3, 5, 44, 29] jogos [17, 9, 3, 5, 45, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 3. AA das Palmeiras  0 eliminated / -: Minas Gerais FC tabela [16, 3, 4, 9, 24, 41] jogos [19, 5, 5, 9, 34, 48] — a tabela conta 16 jogos e as fontes trazem 19
- tabela publicada x jogos — 3. AA das Palmeiras  0 eliminated / -: Portuguesa tabela [16, 3, 2, 11, 18, 39] jogos [18, 4, 3, 11, 26, 48] — a tabela conta 16 jogos e as fontes trazem 18
- tabela publicada x jogos — 3. AA das Palmeiras  0 eliminated / -: Germânia tabela [10, 2, 1, 7, 16, 21] jogos [10, 3, 1, 6, 17, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palestra Itália
- Palestra Itália — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Palmeiras)
- jogo só no ogol, incluído em Segundo Turno: Santos 2-0 Corinthians (1924-10-12)
- jogo só no ogol, incluído em Segundo Turno: AA São Bento 1-0 Portuguesa (1925-01-04)
- jogo só no ogol, incluído em Segundo Turno: Santos 1-0 Portuguesa (1925-01-11)
- só na RSSSF (não achado no ogol): Paulistano-SP 3-1 Palmeiras (1924-04-21)
- só na RSSSF (não achado no ogol): Minas Gerais FC 3-2 Palmeiras (1924-05-03)
- campeão pela lista oficial, Corinthians; o 1º pela soma dos jogos da última fase é Santos (desempate, jogo extra ou pontos tirados fora de campo)

### 1925

- campeão: Associação Atlética São Bento (o mesmo de 1914 APEA)
- tabela publicada x jogos — Fase única / -: AA São Bento tabela [10, 8, 0, 2, 25, 17] jogos [11, 9, 0, 2, 26, 17] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Corinthians tabela [10, 7, 1, 2, 20, 7] jogos [11, 8, 1, 2, 24, 8] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Palmeiras tabela [10, 5, 1, 4, 23, 16] jogos [10, 5, 2, 3, 23, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Portuguesa tabela [10, 4, 0, 6, 14, 17] jogos [11, 4, 0, 7, 15, 19] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: SC Internacional-SP tabela [10, 3, 0, 7, 15, 23] jogos [11, 4, 0, 7, 19, 25] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Germânia tabela [10, 3, 0, 7, 14, 24] jogos [11, 3, 1, 7, 16, 24] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Ypiranga-SP tabela [10, 2, 2, 6, 12, 21] jogos [11, 2, 2, 7, 14, 24] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Auto Audax tabela [10, 1, 1, 8, 9, 24] jogos [11, 2, 1, 8, 11, 25] — a tabela conta 10 jogos e as fontes trazem 11
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AA das Palmeiras
- AA das Palmeiras — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (AA das Palmeiras)
- só na RSSSF (não achado no ogol): AA das Palmeiras 1-2 Auto Audax (1925-04-19)
- só na RSSSF (não achado no ogol): AA das Palmeiras 0-2 Germânia (1925-05-03)
- só na RSSSF (não achado no ogol): Ypiranga-SP 2-3 AA das Palmeiras (1925-05-13)
- só na RSSSF (não achado no ogol): AA das Palmeiras 2-1 Portuguesa (1925-05-24)
- só na RSSSF (não achado no ogol): AA das Palmeiras 1-4 Corinthians (1925-05-31)
- só na RSSSF (não achado no ogol): AA das Palmeiras 0-1 AA São Bento (1925-06-14)
- só na RSSSF (não achado no ogol): SC Internacional-SP 4-2 AA das Palmeiras (1925-06-21)

### 1926 APEA

- tabela publicada x jogos — Fase única / -: Santos tabela [9, 5, 1, 3, 24, 17] jogos [9, 5, 1, 3, 25, 17] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: AA São Bento tabela [9, 2, 0, 7, 9, 31] jogos [9, 2, 0, 7, 9, 32] — há jogo do clube sem conferência no ogol
- jogo só no ogol, incluído em Fase única: Santos 1-0 AA São Bento (1926-09-17)

### 1926 LAF

- sem ocorrências

### 1927 APEA

- tabela publicada x jogos — 1º Turno / -: Palmeiras tabela [12, 11, 1, 0, 70, 13] jogos [17, 15, 1, 1, 100, 24] — a tabela conta 12 jogos e as fontes trazem 17
- tabela publicada x jogos — 1º Turno / -: Corinthians tabela [13, 3, 1, 9, 20, 43] jogos [29, 15, 1, 13, 80, 75] — a tabela conta 13 jogos e as fontes trazem 29
- tabela publicada x jogos — 1º Turno / -: Guarani tabela [11, 7, 1, 3, 39, 28] jogos [14, 8, 1, 5, 49, 38] — a tabela conta 11 jogos e as fontes trazem 14
- tabela publicada x jogos — 1º Turno / -: Santos tabela [8, 7, 0, 1, 39, 19] jogos [16, 14, 0, 2, 100, 33] — a tabela conta 8 jogos e as fontes trazem 16
- tabela publicada x jogos — 1º Turno / -: Palmeiras tabela [16, 14, 1, 1, 89, 22] jogos [17, 15, 1, 1, 100, 24] — a tabela conta 16 jogos e as fontes trazem 17
- tabela publicada x jogos — 1º Turno / -: Corinthians tabela [13, 3, 1, 9, 20, 43] jogos [29, 15, 1, 13, 80, 75] — a tabela conta 13 jogos e as fontes trazem 29
- tabela publicada x jogos — 1º Turno / -: Guarani tabela [14, 7, 1, 6, 47, 38] jogos [14, 8, 1, 5, 49, 38] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Portuguesa tabela [13, 7, 0, 6, 43, 44] jogos [13, 7, 0, 6, 43, 43] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Comercial-RP tabela [9, 3, 0, 6, 13, 22] jogos [9, 2, 0, 7, 13, 24] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Sílex tabela [11, 4, 1, 6, 23, 27] jogos [11, 4, 1, 6, 22, 27] — há jogo do clube sem conferência no ogol
- placar diferente no ogol — Palmeiras x Corinthians (1927-08-21): RSSSF 11-2, ogol 3-1; fica o da RSSSF
- placar corrigido pelo ogol — Sílex x Portuguesa (1927-08-21): RSSSF 1-1, ogol 0-1; fica o do ogol, que fecha com a tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Palmeiras x Corinthians, ogol 1927-08-21); fica a do ogol
- adversário diferente no ogol — RSSSF Portuguesa 5-1 Corinthians, ogol Portuguesa 5-1 Corinthians de Santo André (1927-05-13); fica a RSSSF
- adversário diferente no ogol — RSSSF Corinthians 0-2 República, ogol Corinthians de Santo André 0-2 República (1927-05-22); fica a RSSSF
- adversário diferente no ogol — RSSSF SPAlpargatas 1-1 Corinthians, ogol SPAlpargatas 1-1 Corinthians de Santo André (1927-05-29); fica a RSSSF
- adversário diferente no ogol — RSSSF Corinthians 3-2 Americano-SP, ogol Corinthians de Santo André 3-2 Americano-SP (1927-06-12); fica a RSSSF
- adversário diferente no ogol — RSSSF Barra Funda 1-0 Corinthians, ogol Barra Funda 1-0 Corinthians de Santo André (1927-06-26); fica a RSSSF
- adversário diferente no ogol — RSSSF Corinthians 7-5 Ypiranga-SP, ogol Corinthians de Santo André 7-5 Ypiranga-SP (1927-07-10); fica a RSSSF
- adversário diferente no ogol — RSSSF Guarani 4-1 Corinthians, ogol Guarani 4-1 Corinthians de Santo André (1927-07-24); fica a RSSSF
- adversário diferente no ogol — RSSSF Corinthians 4-1 Corinthians, ogol Corinthians 4-1 Corinthians de Santo André (1927-07-31); fica a RSSSF
- adversário diferente no ogol — RSSSF Primeiro de Maio-SP 1-2 Corinthians, ogol Primeiro de Maio-SP 1-2 Corinthians de Santo André (1927-08-21); fica a RSSSF
- adversário diferente no ogol — RSSSF Santos 4-1 Corinthians, ogol Santos 4-1 Corinthians de Santo André (1927-08-29); fica a RSSSF
- adversário diferente no ogol — RSSSF Comercial-RP 2-1 Corinthians, ogol Comercial-RP 2-1 Corinthians de Santo André (1927-09-04); fica a RSSSF
- adversário diferente no ogol — RSSSF Sílex 1-0 Corinthians, ogol Sílex 1-0 Corinthians de Santo André (1927-10-16); fica a RSSSF
- jogo só no ogol, incluído em Primeiro Turno: Americano-SP 0-0 Barra Funda (1927-05-03)
- jogo só no ogol, incluído em Primeiro Turno: Palmeiras 11-2 Corinthians de Santo André (1927-07-17)
- jogo só no ogol, incluído em Primeiro Turno: Guarani 2-4 Santos (1928-02-05)
- só na RSSSF (não achado no ogol): Palmeiras 3-1 Corinthians (1927-08-21)

### 1927 LAF

- tabela publicada x jogos — Fase única / -: Paulistano-SP tabela [9, 6, 3, 0, 30, 7] jogos [11, 6, 4, 1, 32, 10] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Jabaquara tabela [9, 6, 1, 2, 23, 16] jogos [11, 6, 2, 3, 26, 24] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Paulista tabela [9, 5, 1, 3, 24, 20] jogos [11, 6, 1, 4, 29, 27] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: AA São Bento tabela [9, 5, 1, 3, 17, 11] jogos [11, 5, 1, 5, 18, 16] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Germânia tabela [9, 4, 2, 3, 25, 22] jogos [12, 7, 2, 3, 32, 24] — a tabela conta 9 jogos e as fontes trazem 12
- tabela publicada x jogos — Fase única / -: AA das Palmeiras tabela [9, 3, 2, 4, 15, 23] jogos [11, 3, 2, 6, 17, 28] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: SC Internacional-SP tabela [9, 3, 1, 5, 16, 20] jogos [9, 2, 1, 6, 17, 23] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Atlético Santista tabela [9, 3, 1, 5, 17, 18] jogos [13, 6, 1, 6, 24, 24] — a tabela conta 9 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase única / -: Antarctica tabela [9, 2, 1, 6, 16, 33] jogos [11, 2, 2, 7, 21, 40] — a tabela conta 9 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: SantAnna tabela [9, 1, 1, 7, 8, 21] jogos [12, 0, 2, 10, 11, 30] — a tabela conta 9 jogos e as fontes trazem 12
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AA Palmeiras
- AA Palmeiras — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (AA das Palmeiras)
- placar diferente no ogol — Paulistano-SP x Corinthians (1927-06-26): RSSSF 0-1, ogol 1-0; fica o da RSSSF
- jogo só no ogol, incluído em Fase única: Germânia 2-2 Paulistano-SP (1927-04-03)
- campeão pela lista oficial, Paulistano-SP; o 1º pela soma dos jogos da última fase é Germânia (desempate, jogo extra ou pontos tirados fora de campo)

### 1928 APEA

- tabela publicada x jogos — Fase única / -: Palmeiras tabela [12, 8, 2, 2, 45, 16] jogos [14, 9, 3, 2, 52, 19] — a tabela conta 12 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase única / -: Guarani tabela [12, 5, 1, 6, 28, 24] jogos [13, 5, 1, 7, 28, 27] — a tabela conta 12 jogos e as fontes trazem 13
- tabela publicada x jogos — Fase única / -: Portuguesa tabela [12, 3, 1, 8, 12, 35] jogos [14, 3, 1, 10, 16, 45] — a tabela conta 12 jogos e as fontes trazem 14
- tabela publicada x jogos — Fase única / -: EC Sírio tabela [12, 1, 1, 10, 7, 44] jogos [13, 2, 1, 10, 10, 44] — a tabela conta 12 jogos e as fontes trazem 13
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Comercial (RP)
- Comercial (RP) — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Comercial-RP)
- só na RSSSF (não achado no ogol): Palmeiras 1-1 Comercial-RP (1928-07-01)
- só na RSSSF (não achado no ogol): Comercial-RP 3-1 Guarani (1928-07-08)
- só na RSSSF (não achado no ogol): Portuguesa 1-3 Comercial-RP (1928-07-14)
- só na RSSSF (não achado no ogol): Comercial-RP 1-3 EC Sírio (1928-07-22)
- só na RSSSF (não achado no ogol): Palmeiras 6-3 Portuguesa (1928-07-29)

### 1928 LAF

- tabela publicada x jogos — Primeira fase / -: SC Internacional-SP tabela [22, 14, 5, 3, 61, 32] jogos [22, 14, 5, 3, 63, 32] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Paulistano-SP tabela [22, 15, 3, 4, 61, 22] jogos [23, 15, 3, 5, 61, 24] — a tabela conta 22 jogos e as fontes trazem 23
- tabela publicada x jogos — Primeira fase / -: Atlético Santista tabela [22, 10, 6, 6, 57, 31] jogos [22, 10, 5, 7, 56, 31] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: AA São Bento tabela [22, 9, 5, 8, 41, 40] jogos [22, 10, 4, 8, 41, 39] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Independência-SP tabela [22, 8, 2, 12, 50, 58] jogos [21, 8, 2, 11, 50, 58] — a tabela conta 22 jogos e as fontes trazem 21
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Sant'Anna
- Sant'Anna — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (SantAnna)
- jogo só no ogol, incluído em Primeira fase / Grupo C: Paulista 127-0 LAF (0000-00-00)
- jogo só no ogol, incluído em Fase única: SC Internacional-SP 1-0 Independência-SP (1928-07-29)

### 1929 APEA

- sem ocorrências

### 1929 LAF

- tabela publicada x jogos — Fase única / -: Paulistano-SP tabela [19, 14, 2, 3, 53, 15] jogos [19, 14, 2, 3, 52, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Ponte Preta tabela [20, 12, 2, 6, 55, 36] jogos [20, 12, 3, 5, 55, 36] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: SC Internacional-SP tabela [18, 9, 5, 4, 34, 23] jogos [19, 9, 5, 5, 34, 24] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Fase única / -: Independência-SP tabela [20, 8, 5, 7, 42, 37] jogos [20, 7, 6, 7, 42, 37] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Atlético Santista tabela [19, 7, 5, 7, 34, 28] jogos [18, 7, 5, 6, 32, 25] — a tabela conta 19 jogos e as fontes trazem 18
- tabela publicada x jogos — Fase única / -: Portuguesa Santista tabela [21, 7, 4, 10, 37, 40] jogos [21, 8, 4, 9, 38, 40] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: AA São Bento tabela [19, 5, 6, 8, 20, 32] jogos [19, 4, 6, 9, 20, 33] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: AA das Palmeiras tabela [17, 5, 1, 11, 28, 50] jogos [16, 3, 2, 11, 25, 47] — a tabela conta 17 jogos e as fontes trazem 16
- tabela publicada x jogos — Fase única / -: Paulista tabela [20, 5, 1, 14, 29, 58] jogos [21, 6, 2, 13, 30, 58] — a tabela conta 20 jogos e as fontes trazem 21
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): AA Palmeiras
- AA Palmeiras — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (AA das Palmeiras)
- jogo só no ogol, incluído em Fase única: AA das Palmeiras 0-0 Ponte Preta (1929-09-15)
- jogo só no ogol, incluído em Fase única: Independência-SP 0-0 Paulista (1929-09-22)
- jogo só no ogol, incluído em Fase única: AA São Bento 0-1 Portuguesa Santista (1929-11-15)

### 1930

- tabela publicada x jogos — Fase única / -: Corinthians tabela [26, 20, 4, 2, 94, 33] jogos [26, 19, 4, 3, 94, 33] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: São Paulo tabela [26, 15, 10, 1, 74, 27] jogos [26, 16, 9, 1, 77, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Palmeiras tabela [26, 17, 6, 3, 85, 27] jogos [26, 18, 6, 2, 85, 29] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Santos tabela [26, 18, 4, 4, 80, 38] jogos [26, 18, 4, 4, 80, 39] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: SC Internacional-SP tabela [26, 10, 5, 11, 45, 43] jogos [26, 10, 5, 11, 42, 42] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: EC Sírio tabela [26, 9, 3, 14, 65, 60] jogos [26, 10, 3, 13, 66, 60] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Ypiranga-SP tabela [26, 4, 3, 19, 29, 100] jogos [26, 3, 3, 20, 28, 101] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Germânia tabela [26, 5, 1, 20, 44, 79] jogos [26, 6, 1, 19, 44, 76] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1931

- tabela publicada x jogos — Fase única / -: São Paulo tabela [26, 20, 5, 1, 92, 30] jogos [26, 19, 6, 1, 92, 32] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Santos tabela [25, 18, 6, 1, 79, 28] jogos [26, 18, 6, 2, 79, 29] — a tabela conta 25 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase única / -: Atlético Santista tabela [25, 13, 7, 5, 66, 44] jogos [26, 13, 8, 5, 67, 44] — a tabela conta 25 jogos e as fontes trazem 26
- tabela publicada x jogos — Fase única / -: Portuguesa tabela [26, 14, 4, 8, 55, 35] jogos [26, 14, 5, 7, 55, 35] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Corinthians tabela [26, 11, 8, 7, 66, 47] jogos [26, 10, 9, 7, 66, 48] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Guarani tabela [26, 11, 4, 11, 54, 49] jogos [26, 11, 4, 11, 54, 50] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: SC Internacional-SP tabela [26, 7, 5, 14, 35, 51] jogos [26, 7, 5, 14, 37, 52] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: AA São Bento tabela [26, 4, 6, 16, 45, 74] jogos [26, 5, 5, 16, 46, 74] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Germânia tabela [26, 4, 2, 20, 35, 91] jogos [26, 4, 3, 19, 37, 91] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo só no ogol, incluído em Fase única: Atlético Santista 0-0 Portuguesa (1931-09-20)

### 1932

- tabela publicada x jogos — Fase única / -: São Paulo tabela [11, 8, 1, 2, 34, 12] jogos [11, 8, 1, 2, 36, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Portuguesa tabela [11, 4, 2, 5, 22, 24] jogos [11, 4, 2, 5, 23, 26] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1933

- tabela publicada x jogos — 2º Turno / -: São Paulo tabela [14, 11, 1, 2, 62, 16] jogos [15, 11, 1, 3, 62, 18] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — 2º Turno / -: Corinthians tabela [14, 7, 1, 6, 31, 38] jogos [15, 8, 1, 6, 33, 38] — a tabela conta 14 jogos e as fontes trazem 15
- placar diferente no ogol — São Bento de São Paulo x Portuguesa (1933-10-15): RSSSF 3-5, ogol 3-0; fica o da RSSSF
- jogo só no ogol, incluído em 1o.TURNO: Palmeiras 5-1 Corinthians (1933-05-07)
- jogo só no ogol, incluído em 2o.TURNO: Palmeiras 1-1 Portuguesa (1933-09-07)
- jogo só no ogol, incluído em 2o.TURNO: Corinthians 2-0 São Bento de São Paulo (1933-11-15)
- só na RSSSF (não achado no ogol): Corinthians 2-0 São Paulo (None)

### 1934

- tabela publicada x jogos — Fase única / -: Santos tabela [14, 5, 3, 6, 22, 27] jogos [14, 5, 3, 6, 23, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: EC Sírio tabela [14, 1, 0, 13, 10, 57] jogos [14, 1, 0, 13, 10, 58] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1935 LPF

- tabela publicada x jogos — Fase única / -: Santos tabela [12, 9, 2, 1, 31, 11] jogos [12, 9, 2, 1, 32, 12] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Palmeiras tabela [12, 8, 2, 2, 24, 12] jogos [12, 8, 2, 2, 28, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Portuguesa Santista tabela [12, 5, 1, 6, 28, 31] jogos [12, 5, 1, 6, 29, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: ECPaulista tabela [12, 2, 1, 9, 17, 43] jogos [12, 2, 1, 9, 18, 44] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Juventus-SP tabela [12, 1, 2, 9, 12, 27] jogos [12, 1, 2, 9, 14, 32] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1935 APEA

- tabela publicada x jogos — Fase única / -: Portuguesa tabela [14, 10, 2, 2, 65, 17] jogos [16, 11, 3, 2, 65, 17] — a tabela conta 14 jogos e as fontes trazem 16
- tabela publicada x jogos — Fase única / -: Ypiranga-SP tabela [14, 11, 0, 3, 50, 33] jogos [16, 10, 2, 4, 50, 33] — a tabela conta 14 jogos e as fontes trazem 16
- tabela publicada x jogos — Fase única / -: Estudantes de São Paulo tabela [14, 9, 2, 3, 47, 16] jogos [14, 9, 3, 2, 47, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: São Caetano EC tabela [14, 7, 2, 5, 29, 31] jogos [15, 8, 2, 5, 33, 34] — a tabela conta 14 jogos e as fontes trazem 15
- tabela publicada x jogos — Fase única / -: Jardim América tabela [13, 3, 1, 9, 23, 39] jogos [14, 4, 1, 9, 24, 39] — a tabela conta 13 jogos e as fontes trazem 14
- jogo só no ogol, incluído em Fase única: Portuguesa 2-2 Ypiranga-SP (1936-01-05)
- jogo só no ogol, incluído em Fase única: Portuguesa 5-2 Ypiranga-SP (1936-01-12)

### 1936 LPF

- tabela publicada x jogos — Fase única / -: Palmeiras tabela [21, 15, 3, 3, 70, 15] jogos [24, 17, 4, 3, 70, 15] — a tabela conta 21 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase única / -: Corinthians tabela [21, 15, 1, 5, 70, 33] jogos [24, 15, 2, 7, 70, 34] — a tabela conta 21 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase única / -: Santos tabela [21, 13, 2, 6, 70, 37] jogos [21, 12, 4, 5, 67, 34] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Estudantes de São Paulo tabela [21, 11, 2, 8, 50, 45] jogos [21, 11, 3, 7, 49, 42] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Jabaquara tabela [21, 10, 3, 8, 52, 43] jogos [21, 9, 4, 8, 50, 43] — placar diverge entre RSSSF e ogol em São Paulo x Jabaquara (1-3 x 1-4) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: São Paulo tabela [21, 6, 3, 12, 42, 59] jogos [21, 7, 2, 12, 27, 34] — placar diverge entre RSSSF e ogol em São Paulo x Jabaquara (1-3 x 1-4) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — Fase única / -: CA Paulista tabela [21, 2, 2, 17, 44, 100] jogos [21, 2, 2, 17, 44, 99] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — São Paulo x Jabaquara (1936-10-01): RSSSF 1-3, ogol 1-4; fica o da RSSSF
- jogo só no ogol, incluído em Fase única: Estudantes de São Paulo 2-1 Albion (1936-04-25)
- jogo só no ogol, incluído em Fase única: Palmeiras 1-0 Corinthians (1937-04-25)
- jogo só no ogol, incluído em Fase única: Corinthians 0-0 Palmeiras (1937-05-02)
- jogo só no ogol, incluído em Fase única: Palmeiras 2-1 Corinthians (1937-05-09)

### 1936 APEA

- jogo só no ogol, incluído em Fase única: Humberto Primeiro 2-6 Portuguesa (1936-08-09)

### 1937

- tabela publicada x jogos — 1º Turno / -: Corinthians tabela [14, 10, 2, 2, 33, 14] jogos [14, 10, 2, 2, 33, 12] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 1º Turno / -: Estudantes de São Paulo tabela [14, 7, 1, 6, 33, 22] jogos [14, 7, 1, 6, 31, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / -: São Paulo tabela [9, 2, 1, 6, 11, 25] jogos [9, 4, 0, 5, 8, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo só no ogol, incluído em Primeiro Turno: Corinthians 5-0 Luzitano-SP (1937-06-13)
- jogo só no ogol, incluído em Segundo Turno: Portuguesa Santista 3-2 Corinthians (1937-10-10)
- campeão pela lista oficial, Corinthians; o 1º pela soma dos jogos da última fase é Portuguesa Santista (desempate, jogo extra ou pontos tirados fora de campo)

### 1938

- tabela publicada x jogos — Fase única / -: Corinthians tabela [10, 7, 3, 0, 19, 8] jogos [10, 6, 4, 0, 19, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: São Paulo tabela [10, 3, 2, 5, 19, 23] jogos [10, 6, 2, 2, 30, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Juventus-SP tabela [10, 4, 1, 5, 14, 15] jogos [11, 4, 1, 6, 15, 17] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Fase única / -: Luzitano-SP tabela [10, 2, 0, 8, 12, 38] jogos [10, 2, 1, 7, 14, 38] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1939

- tabela publicada x jogos — Fase única / -: Jabaquara tabela [20, 5, 4, 11, 28, 46] jogos [20, 5, 4, 11, 28, 48] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Ypiranga-SP tabela [20, 4, 1, 15, 27, 51] jogos [20, 4, 1, 15, 29, 51] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar corrigido pelo ogol — São Paulo x Jabaquara (1939-11-18): RSSSF 2-0, ogol 5-0; fica o do ogol, que fecha com a tabela publicada

### 1940

- sem ocorrências

### 1941

- tabela publicada x jogos — Fase única / -: São Paulo tabela [20, 7, 4, 9, 48, 53] jogos [20, 13, 5, 2, 55, 32] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Jabaquara tabela [20, 8, 2, 10, 48, 57] jogos [20, 7, 3, 10, 48, 57] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Comercial Paulistano tabela [20, 1, 3, 16, 27, 76] jogos [20, 1, 4, 15, 24, 76] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1942

- tabela publicada x jogos — Fase única / -: Palmeiras tabela [20, 17, 2, 1, 65, 19] jogos [19, 17, 2, 0, 64, 16] — a tabela conta 20 jogos e as fontes trazem 19
- tabela publicada x jogos — Fase única / -: Corinthians tabela [20, 15, 3, 2, 78, 29] jogos [19, 14, 3, 2, 75, 28] — a tabela conta 20 jogos e as fontes trazem 19
- tabela publicada x jogos — Fase única / -: São Paulo tabela [20, 8, 3, 9, 48, 61] jogos [20, 15, 2, 3, 77, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Portuguesa tabela [20, 8, 2, 10, 44, 52] jogos [20, 7, 2, 11, 44, 51] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Portuguesa Santista tabela [20, 5, 0, 15, 39, 60] jogos [20, 6, 0, 14, 39, 60] — há jogo do clube sem conferência no ogol
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Palestra de São Paulo
- Palestra de São Paulo — clube que o ogol não tem; entra só pela RSSSF
- só na RSSSF (não achado no ogol): Palmeiras 3-1 São Paulo (1942-09-20)
- só na RSSSF (não achado no ogol): Portuguesa Santista 3-4 Corinthians (1942-09-20)
- só na RSSSF (não achado no ogol): Corinthians 4-0 Juventus-SP (1942-09-27)
- só na RSSSF (não achado no ogol): Ypiranga-SP 3-0 Portuguesa (1942-09-27)
- só na RSSSF (não achado no ogol): Santos 0-0 Comercial Paulistano (1942-09-27)
- só na RSSSF (não achado no ogol): São Paulo 0-1 Jabaquara (1942-09-27)
- só na RSSSF (não achado no ogol): Portuguesa 3-1 SPRAC (1942-10-03)
- só na RSSSF (não achado no ogol): Portuguesa Santista 2-1 Santos (1942-10-04)
- só na RSSSF (não achado no ogol): Ypiranga-SP 7-1 Comercial Paulistano (1942-10-04)

### 1943

- tabela publicada x jogos — Fase única / -: São Paulo tabela [20, 4, 1, 15, 38, 77] jogos [20, 15, 3, 2, 63, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: São Paulo x Portuguesa Santista, ogol 1943-05-30); fica a do ogol

### 1944

- tabela publicada x jogos — Fase única / -: São Paulo tabela [20, 9, 3, 8, 41, 48] jogos [20, 13, 3, 4, 69, 32] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Santos tabela [20, 8, 4, 8, 39, 41] jogos [20, 7, 5, 8, 39, 41] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Juventus-SP tabela [20, 7, 4, 9, 39, 49] jogos [20, 7, 5, 8, 39, 49] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Comercial Paulistano tabela [20, 8, 2, 10, 37, 57] jogos [20, 8, 2, 10, 37, 52] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1945

- tabela publicada x jogos — Fase única / -: São Paulo tabela [20, 6, 2, 12, 37, 52] jogos [20, 17, 2, 1, 70, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Palmeiras tabela [20, 11, 7, 2, 47, 17] jogos [20, 11, 7, 2, 47, 18] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Portuguesa tabela [20, 10, 5, 5, 44, 22] jogos [20, 10, 5, 5, 45, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Ypiranga-SP tabela [20, 8, 1, 11, 37, 44] jogos [20, 8, 1, 11, 38, 44] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Juventus-SP tabela [20, 5, 2, 13, 34, 45] jogos [20, 6, 2, 12, 34, 45] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Comercial Paulistano tabela [20, 4, 3, 13, 32, 60] jogos [20, 3, 3, 14, 31, 60] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Portuguesa Santista tabela [20, 2, 3, 15, 23, 69] jogos [20, 2, 3, 15, 23, 67] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1946

- tabela publicada x jogos — Fase única / -: São Paulo tabela [20, 5, 2, 13, 27, 46] jogos [20, 17, 3, 0, 62, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Santos tabela [20, 9, 4, 7, 37, 32] jogos [20, 9, 4, 7, 36, 31] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Ypiranga-SP tabela [20, 6, 2, 12, 35, 48] jogos [20, 6, 2, 12, 35, 50] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Comercial Paulistano tabela [20, 4, 6, 10, 38, 55] jogos [20, 4, 6, 10, 37, 54] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Jabaquara tabela [20, 4, 1, 15, 27, 52] jogos [20, 4, 1, 15, 29, 52] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1947

- tabela publicada x jogos — Fase única / -: São Paulo tabela [20, 8, 9, 3, 48, 27] jogos [20, 8, 9, 3, 48, 26] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Nacional-SP tabela [20, 3, 4, 13, 25, 47] jogos [20, 3, 4, 13, 24, 47] — há jogo do clube sem conferência no ogol
- só na RSSSF (não achado no ogol): Ypiranga-SP 4-0 Juventus-SP (1947-12-21)
- só na RSSSF (não achado no ogol): Nacional-SP 3-3 Jabaquara (1947-12-21)
- só na RSSSF (não achado no ogol): Portuguesa 5-1 Comercial Paulistano (1947-12-21)
- só na RSSSF (não achado no ogol): Juventus-SP 2-1 São Paulo (1947-12-27)
- só na RSSSF (não achado no ogol): Santos 1-2 Palmeiras (1947-12-28)
- só na RSSSF (não achado no ogol): Corinthians 3-0 Nacional-SP (1947-12-28)
- só na RSSSF (não achado no ogol): Palmeiras 2-0 Comercial Paulistano (1948-01-03)
- só na RSSSF (não achado no ogol): São Paulo 1-1 Corinthians (1948-01-04)
- só na RSSSF (não achado no ogol): Jabaquara 0-1 Portuguesa (1948-01-04)
- só na RSSSF (não achado no ogol): Portuguesa Santista 0-3 Corinthians (1948-01-11)

### 1948

- tabela publicada x jogos — Fase única / -: São Paulo tabela [20, 16, 2, 2, 54, 19] jogos [19, 16, 1, 2, 52, 17] — a tabela conta 20 jogos e as fontes trazem 19
- tabela publicada x jogos — Fase única / -: Portuguesa tabela [20, 9, 2, 9, 49, 34] jogos [20, 10, 2, 8, 50, 33] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Juventus-SP tabela [20, 7, 5, 8, 32, 49] jogos [21, 7, 6, 8, 34, 51] — a tabela conta 20 jogos e as fontes trazem 21
- tabela publicada x jogos — Fase única / -: Nacional-SP tabela [20, 2, 3, 15, 18, 55] jogos [20, 1, 3, 16, 17, 56] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- adversário diferente no ogol — RSSSF Comercial Paulistano 2-2 Juventus-SP, ogol Comercial Paulistano 2-2 São Paulo (1948-05-16); fica a RSSSF

### 1949

- tabela publicada x jogos — Fase única / -: Santos tabela [22, 11, 4, 7, 51, 40] jogos [22, 11, 4, 7, 52, 40] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Nacional-SP tabela [22, 5, 2, 15, 27, 70] jogos [22, 5, 2, 15, 27, 71] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1950

- tabela publicada x jogos — Fase única / -: São Paulo tabela [22, 13, 5, 4, 54, 26] jogos [22, 13, 5, 4, 55, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Guarani tabela [22, 9, 5, 8, 34, 41] jogos [22, 9, 5, 8, 35, 42] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Ypiranga-SP tabela [22, 9, 1, 12, 33, 40] jogos [22, 9, 1, 12, 33, 39] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Portuguesa Santista tabela [22, 6, 4, 12, 34, 39] jogos [22, 6, 4, 12, 34, 40] — há jogo do clube sem conferência no ogol
- jogo só no ogol, incluído em Fase única: Portuguesa Santista 2-1 Jabaquara (1950-12-17)

### 1951

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): XV de Jaú
- XV de Jaú — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (XV de Jaú)
- jogo só no ogol, incluído em Fase única: Corinthians 3-2 Nacional-SP (1951-06-02)
- só na RSSSF (não achado no ogol): XV de Jaú 5-0 Jabaquara (1952-02-03)
- só na RSSSF (não achado no ogol): Jabaquara 2-0 XV de Jaú (1952-02-10)
- só na RSSSF (não achado no ogol): XV de Jaú 1-0 Jabaquara (1952-02-17)
- campeão pela lista oficial, Corinthians; o 1º pela soma dos jogos da última fase é XV de Jaú (desempate, jogo extra ou pontos tirados fora de campo)

### 1952

- placar diferente no ogol — Radium x Palmeiras (1953-01-25): RSSSF 3-3, ogol 3-2; fica o da RSSSF
- placar diferente no ogol — Ypiranga-SP x Nacional-SP (1953-02-01): RSSSF 3-3, ogol 3-1; fica o da RSSSF

### 1953

- sem ocorrências

### 1954

- placar diferente no ogol — São Paulo x Ypiranga-SP (1954-10-01): RSSSF 0-1, ogol 5-1; fica o da RSSSF

### 1955

- sem ocorrências

### 1956

- tabela publicada x jogos — Fase final / -: Noroeste tabela [14, 10, 1, 3, 43, 20] jogos [31, 16, 3, 12, 65, 56] — a tabela conta 14 jogos e as fontes trazem 31
- tabela publicada x jogos — Fase final / -: Ferroviária-SP tabela [14, 9, 2, 3, 35, 16] jogos [31, 14, 4, 13, 70, 61] — a tabela conta 14 jogos e as fontes trazem 31
- tabela publicada x jogos — Fase final / -: Ponte Preta tabela [14, 7, 4, 3, 27, 19] jogos [31, 13, 7, 11, 54, 47] — a tabela conta 14 jogos e as fontes trazem 31
- tabela publicada x jogos — Fase final / -: Portuguesa Santista tabela [14, 6, 2, 6, 36, 27] jogos [31, 9, 5, 17, 56, 66] — a tabela conta 14 jogos e as fontes trazem 31
- tabela publicada x jogos — Fase final / -: Linense tabela [14, 5, 3, 6, 32, 42] jogos [31, 8, 6, 17, 59, 97] — a tabela conta 14 jogos e as fontes trazem 31
- tabela publicada x jogos — Fase final / -: Nacional-SP tabela [14, 5, 0, 9, 28, 41] jogos [31, 7, 6, 18, 45, 81] — a tabela conta 14 jogos e as fontes trazem 31
- tabela publicada x jogos — Fase final / -: Guarani tabela [14, 4, 1, 9, 19, 39] jogos [31, 8, 5, 18, 45, 78] — a tabela conta 14 jogos e as fontes trazem 31
- tabela publicada x jogos — Fase final / -: Jabaquara tabela [14, 3, 1, 10, 22, 38] jogos [31, 7, 3, 21, 50, 85] — a tabela conta 14 jogos e as fontes trazem 31
- tabela publicada x jogos — Fase final / -: Santos tabela [18, 15, 0, 3, 43, 18] jogos [19, 16, 0, 3, 47, 20] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Fase final / -: São Paulo tabela [18, 13, 4, 1, 56, 21] jogos [19, 13, 4, 2, 58, 24] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Fase final / -: Corinthians tabela [18, 9, 7, 2, 41, 22] jogos [19, 9, 8, 2, 43, 24] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Fase final / -: Juventus-SP tabela [18, 4, 3, 11, 24, 38] jogos [18, 4, 3, 11, 23, 38] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Taubaté tabela [18, 3, 5, 10, 23, 41] jogos [19, 3, 6, 10, 25, 43] — a tabela conta 18 jogos e as fontes trazem 19
- tabela publicada x jogos — Fase final / -: São Paulo tabela [36, 25, 5, 6, 114, 46] jogos [36, 25, 5, 6, 114, 48] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Corinthians tabela [35, 23, 8, 4, 95, 50] jogos [36, 23, 9, 4, 97, 52] — a tabela conta 35 jogos e as fontes trazem 36
- tabela publicada x jogos — Fase final / -: Portuguesa tabela [31, 9, 5, 17, 56, 66] jogos [35, 15, 7, 13, 60, 55] — a tabela conta 31 jogos e as fontes trazem 35
- tabela publicada x jogos — Fase final / -: Taubaté tabela [35, 9, 10, 16, 45, 63] jogos [36, 9, 11, 16, 47, 65] — a tabela conta 35 jogos e as fontes trazem 36
- tabela publicada x jogos — Fase final / -: São Bento de SCS tabela [35, 9, 10, 16, 57, 65] jogos [35, 9, 10, 16, 59, 65] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — Taubaté x Corinthians (1956-12-23): RSSSF 2-2, ogol 0-2; fica o da RSSSF
- placar corrigido pelo ogol — São Paulo x Juventus-SP (1956-11-22): RSSSF 3-2, ogol 3-1; fica o do ogol, que fecha com a tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Taubaté x Corinthians, ogol 1956-12-23); fica a do ogol
- jogo só no ogol, incluído em Torneio de Classificação / Série Branca (Torneio de Rebaixamento): Ferroviária-SP 2-0 Jabaquara (1956-10-28)
- jogo só no ogol, incluído em Classificação Final / Série Azul: Portuguesa 2-2 Corinthians (1956-11-21)
- só na RSSSF (não achado no ogol): Taubaté 0-2 Corinthians (1956-12-23)

### 1957

- tabela publicada x jogos — Fase de Classificação / -: Jabaquara tabela [19, 11, 3, 5, 35, 33] jogos [18, 11, 3, 4, 34, 28] — a tabela conta 19 jogos e as fontes trazem 18
- tabela publicada x jogos — Fase de Classificação / -: Guarani tabela [19, 5, 3, 11, 35, 48] jogos [18, 4, 3, 11, 30, 47] — a tabela conta 19 jogos e as fontes trazem 18
- placar diferente no ogol — Botafogo-SP x São Paulo (1957-07-14): RSSSF 1-0, ogol 2-1; fica o da RSSSF
- jogo só no ogol, incluído em Fase de Classificação: Guarani 5-1 Jabaquara (1957-06-09)
- jogo só no ogol, incluído em Fase de Classificação: Botafogo-SP 4-1 Noroeste (1957-10-06)
- jogo só no ogol, incluído em Classificação Final / Série Azul: Portuguesa Santista 1-0 Ponte Preta (1957-10-09)
- só na RSSSF (não achado no ogol): Taubaté 2-0 Ferroviária-SP (1957-10-20)
- só na RSSSF (não achado no ogol): Guarani 3-1 Noroeste (1957-10-20)
- só na RSSSF (não achado no ogol): XV de Jaú 3-2 Juventus-SP (1957-10-20)
- só na RSSSF (não achado no ogol): Nacional-SP 2-1 Ypiranga-SP (1957-10-20)
- só na RSSSF (não achado no ogol): Ferroviária-SP 4-0 XV de Jaú (1957-10-27)
- só na RSSSF (não achado no ogol): Guarani 6-2 Taubaté (1957-10-27)
- só na RSSSF (não achado no ogol): Juventus-SP 1-1 Noroeste (1957-10-27)
- só na RSSSF (não achado no ogol): Linense 0-3 Nacional-SP (1957-10-27)
- só na RSSSF (não achado no ogol): São Bento de SCS 2-1 Ypiranga-SP (1957-10-27)
- só na RSSSF (não achado no ogol): Noroeste 6-0 Linense (1957-10-31)
- só na RSSSF (não achado no ogol): Nacional-SP 6-2 Ferroviária-SP (1957-11-03)
- só na RSSSF (não achado no ogol): Taubaté 2-1 Juventus-SP (1957-11-03)
- só na RSSSF (não achado no ogol): Linense 3-2 Guarani (1957-11-03)
- só na RSSSF (não achado no ogol): XV de Jaú 0-0 São Bento de SCS (1957-11-03)
- só na RSSSF (não achado no ogol): Ypiranga-SP 3-4 Noroeste (1957-11-03)
- só na RSSSF (não achado no ogol): Linense 1-1 Taubaté (1957-11-10)
- só na RSSSF (não achado no ogol): Ferroviária-SP 1-0 São Bento de SCS (1957-11-10)
- só na RSSSF (não achado no ogol): XV de Jaú 1-2 Nacional-SP (1957-11-10)
- só na RSSSF (não achado no ogol): Guarani 4-0 Ypiranga-SP (1957-11-10)
- só na RSSSF (não achado no ogol): Noroeste 3-1 Ferroviária-SP (1957-11-13)
- só na RSSSF (não achado no ogol): Ferroviária-SP 2-1 Linense (1957-11-17)
- só na RSSSF (não achado no ogol): Taubaté 4-0 XV de Jaú (1957-11-17)
- só na RSSSF (não achado no ogol): Nacional-SP 3-2 Guarani (1957-11-17)
- só na RSSSF (não achado no ogol): Ypiranga-SP 2-1 Juventus-SP (1957-11-17)
- só na RSSSF (não achado no ogol): São Bento de SCS 1-0 Noroeste (1957-11-17)
- só na RSSSF (não achado no ogol): Juventus-SP 5-1 Nacional-SP (1957-11-20)
- só na RSSSF (não achado no ogol): Ferroviária-SP 0-0 Ypiranga-SP (1957-11-24)
- só na RSSSF (não achado no ogol): Noroeste 3-0 Nacional-SP (1957-11-24)
- só na RSSSF (não achado no ogol): Guarani 3-0 Juventus-SP (1957-11-24)
- só na RSSSF (não achado no ogol): São Bento de SCS 1-3 Taubaté (1957-11-24)
- só na RSSSF (não achado no ogol): Linense 0-0 XV de Jaú (1957-11-24)
- só na RSSSF (não achado no ogol): Ypiranga-SP 0-0 Taubaté (1957-11-27)
- só na RSSSF (não achado no ogol): Juventus-SP 0-0 São Bento de SCS (1957-11-27)
- só na RSSSF (não achado no ogol): XV de Jaú 3-0 Ypiranga-SP (1957-12-01)
- só na RSSSF (não achado no ogol): Ferroviária-SP 4-3 Guarani (1957-12-01)
- só na RSSSF (não achado no ogol): São Bento de SCS 2-2 Nacional-SP (1957-12-01)
- só na RSSSF (não achado no ogol): Juventus-SP 4-0 Linense (1957-12-01)
- só na RSSSF (não achado no ogol): Taubaté 2-1 Noroeste (1957-12-01)
- só na RSSSF (não achado no ogol): Guarani 6-3 XV de Jaú (1957-12-03)
- só na RSSSF (não achado no ogol): Noroeste 2-1 XV de Jaú (1957-12-08)
- só na RSSSF (não achado no ogol): Juventus-SP 2-0 Ferroviária-SP (1957-12-08)
- só na RSSSF (não achado no ogol): São Bento de SCS 1-1 Guarani (1957-12-08)
- só na RSSSF (não achado no ogol): Nacional-SP 2-1 Taubaté (1957-12-08)
- só na RSSSF (não achado no ogol): Ypiranga-SP 4-1 Linense (1957-12-08)
- só na RSSSF (não achado no ogol): Nacional-SP 1-1 Linense (1957-12-15)
- só na RSSSF (não achado no ogol): Taubaté 4-1 Ypiranga-SP (1957-12-15)
- só na RSSSF (não achado no ogol): Noroeste 3-2 Juventus-SP (1957-12-15)
- só na RSSSF (não achado no ogol): XV de Jaú 2-3 Guarani (1957-12-15)
- só na RSSSF (não achado no ogol): São Bento de SCS 2-1 Ferroviária-SP (1957-12-15)
- só na RSSSF (não achado no ogol): Nacional-SP 1-0 Ypiranga-SP (1957-12-18)
- só na RSSSF (não achado no ogol): Linense 1-0 Noroeste (1957-12-18)
- só na RSSSF (não achado no ogol): Nacional-SP 5-2 XV de Jaú (1957-12-22)
- só na RSSSF (não achado no ogol): Juventus-SP 3-2 Guarani (1957-12-22)
- só na RSSSF (não achado no ogol): Noroeste 1-0 Taubaté (1957-12-22)
- só na RSSSF (não achado no ogol): Linense 2-2 São Bento de SCS (1957-12-22)
- só na RSSSF (não achado no ogol): Ypiranga-SP 1-1 Ferroviária-SP (1957-12-22)
- só na RSSSF (não achado no ogol): Ferroviária-SP 4-0 Nacional-SP (1957-12-29)
- só na RSSSF (não achado no ogol): Noroeste 2-0 Ypiranga-SP (1957-12-29)
- só na RSSSF (não achado no ogol): Guarani 4-4 São Bento de SCS (1957-12-29)
- só na RSSSF (não achado no ogol): Taubaté 4-1 XV de Jaú (1957-12-29)
- só na RSSSF (não achado no ogol): Juventus-SP 1-0 Linense (1957-12-29)
- só na RSSSF (não achado no ogol): São Bento de SCS 2-2 Juventus-SP (1958-01-05)
- só na RSSSF (não achado no ogol): Ypiranga-SP 1-0 Guarani (1958-01-05)
- só na RSSSF (não achado no ogol): Taubaté 3-2 Linense (1958-01-05)
- só na RSSSF (não achado no ogol): Nacional-SP 1-1 Noroeste (1958-01-05)
- só na RSSSF (não achado no ogol): XV de Jaú 3-4 Ferroviária-SP (1958-01-05)
- só na RSSSF (não achado no ogol): Taubaté 1-0 Guarani (1958-01-08)
- só na RSSSF (não achado no ogol): Ypiranga-SP 2-0 São Bento de SCS (1958-01-08)
- só na RSSSF (não achado no ogol): Guarani 3-0 Nacional-SP (1958-01-12)
- só na RSSSF (não achado no ogol): São Bento de SCS 3-1 Taubaté (1958-01-12)
- só na RSSSF (não achado no ogol): Juventus-SP 3-1 Ypiranga-SP (1958-01-12)
- só na RSSSF (não achado no ogol): XV de Jaú 4-1 Noroeste (1958-01-12)
- só na RSSSF (não achado no ogol): Linense 3-2 Ferroviária-SP (1958-01-12)
- só na RSSSF (não achado no ogol): Juventus-SP 1-4 Taubaté (1958-01-15)
- só na RSSSF (não achado no ogol): São Bento de SCS 2-0 XV de Jaú (1958-01-15)
- só na RSSSF (não achado no ogol): Ferroviária-SP 0-2 Noroeste (1958-01-15)
- só na RSSSF (não achado no ogol): Guarani 4-0 Linense (1958-01-19)
- só na RSSSF (não achado no ogol): Ypiranga-SP 0-2 XV de Jaú (1958-01-19)
- só na RSSSF (não achado no ogol): Noroeste 1-1 São Bento de SCS (1958-01-19)
- só na RSSSF (não achado no ogol): Ferroviária-SP 1-1 Juventus-SP (1958-01-19)
- só na RSSSF (não achado no ogol): Taubaté 4-1 Nacional-SP (1958-01-19)
- só na RSSSF (não achado no ogol): XV de Jaú 5-0 Linense (1958-01-22)
- só na RSSSF (não achado no ogol): Guarani 8-2 Ferroviária-SP (1958-01-22)
- só na RSSSF (não achado no ogol): Nacional-SP 3-1 Juventus-SP (1958-01-22)
- só na RSSSF (não achado no ogol): Nacional-SP 2-0 São Bento de SCS (1958-01-26)
- só na RSSSF (não achado no ogol): Ferroviária-SP 3-1 Taubaté (1958-01-26)
- só na RSSSF (não achado no ogol): Noroeste 3-2 Guarani (1958-01-26)
- só na RSSSF (não achado no ogol): Linense 2-2 Ypiranga-SP (1958-01-26)
- só na RSSSF (não achado no ogol): Juventus-SP 4-1 XV de Jaú (1958-01-28)
- só na RSSSF (não achado no ogol): São Paulo 5-1 Portuguesa Santista (1957-10-16)
- só na RSSSF (não achado no ogol): Ponte Preta 1-0 Botafogo-SP (1957-10-16)
- só na RSSSF (não achado no ogol): Portuguesa 1-1 Palmeiras (1957-10-19)
- só na RSSSF (não achado no ogol): Botafogo-SP 4-2 Santos (1957-10-20)
- só na RSSSF (não achado no ogol): XV de Piracicaba 2-1 Ponte Preta (1957-10-20)
- só na RSSSF (não achado no ogol): Corinthians 1-1 São Paulo (1957-10-20)
- só na RSSSF (não achado no ogol): Portuguesa Santista 3-3 Jabaquara (1957-10-20)
- só na RSSSF (não achado no ogol): Corinthians 4-0 Botafogo-SP (1957-10-23)
- só na RSSSF (não achado no ogol): Santos 2-2 Portuguesa Santista (1957-10-23)
- só na RSSSF (não achado no ogol): Jabaquara 1-1 Portuguesa (1957-10-24)
- só na RSSSF (não achado no ogol): Palmeiras 3-4 Santos (1957-10-26)
- só na RSSSF (não achado no ogol): Portuguesa Santista 2-3 Corinthians (1957-10-27)
- só na RSSSF (não achado no ogol): Portuguesa 4-0 São Paulo (1957-10-27)
- só na RSSSF (não achado no ogol): Botafogo-SP 3-1 XV de Piracicaba (1957-10-27)
- só na RSSSF (não achado no ogol): Jabaquara 0-1 Corinthians (1957-10-30)
- só na RSSSF (não achado no ogol): Palmeiras 1-2 Ponte Preta (1957-10-30)
- só na RSSSF (não achado no ogol): XV de Piracicaba 3-0 Jabaquara (1957-11-03)
- só na RSSSF (não achado no ogol): Corinthians 3-3 Santos (1957-11-03)
- só na RSSSF (não achado no ogol): Portuguesa Santista 2-2 Palmeiras (1957-11-03)
- só na RSSSF (não achado no ogol): Ponte Preta 0-2 São Paulo (1957-11-03)
- só na RSSSF (não achado no ogol): Portuguesa 5-0 Botafogo-SP (1957-11-03)
- só na RSSSF (não achado no ogol): Palmeiras 1-1 XV de Piracicaba (1957-11-06)
- só na RSSSF (não achado no ogol): Ponte Preta 1-3 Corinthians (1957-11-06)
- só na RSSSF (não achado no ogol): Santos 3-1 Portuguesa (1957-11-06)
- só na RSSSF (não achado no ogol): Portuguesa 2-2 Corinthians (1957-11-09)
- só na RSSSF (não achado no ogol): Jabaquara 4-1 Ponte Preta (1957-11-10)
- só na RSSSF (não achado no ogol): Botafogo-SP 0-1 Portuguesa Santista (1957-11-10)
- só na RSSSF (não achado no ogol): São Paulo 4-2 Palmeiras (1957-11-10)
- só na RSSSF (não achado no ogol): XV de Piracicaba 0-3 Santos (1957-11-10)
- só na RSSSF (não achado no ogol): São Paulo 7-1 XV de Piracicaba (1957-11-13)
- só na RSSSF (não achado no ogol): Jabaquara 0-0 Palmeiras (1957-11-13)
- só na RSSSF (não achado no ogol): Ponte Preta 0-0 Portuguesa (1957-11-17)
- só na RSSSF (não achado no ogol): Botafogo-SP 1-1 Jabaquara (1957-11-17)
- só na RSSSF (não achado no ogol): Santos 2-6 São Paulo (1957-11-17)
- só na RSSSF (não achado no ogol): Corinthians 1-0 Palmeiras (1957-11-17)
- só na RSSSF (não achado no ogol): XV de Piracicaba 0-0 Portuguesa Santista (1957-11-17)
- só na RSSSF (não achado no ogol): Portuguesa 2-1 Jabaquara (1957-11-20)
- só na RSSSF (não achado no ogol): São Paulo 6-2 Ponte Preta (1957-11-20)
- só na RSSSF (não achado no ogol): Palmeiras 3-0 Botafogo-SP (1957-11-21)
- só na RSSSF (não achado no ogol): Corinthians 5-1 Portuguesa Santista (1957-11-21)
- só na RSSSF (não achado no ogol): XV de Piracicaba 3-5 São Paulo (1957-11-24)
- só na RSSSF (não achado no ogol): Botafogo-SP 2-2 Portuguesa (1957-11-24)
- só na RSSSF (não achado no ogol): Palmeiras 3-4 Portuguesa Santista (1957-11-24)
- só na RSSSF (não achado no ogol): Corinthians 5-1 Ponte Preta (1957-11-24)
- só na RSSSF (não achado no ogol): Santos 5-1 Jabaquara (1957-11-24)
- só na RSSSF (não achado no ogol): Corinthians 3-1 Palmeiras (1957-11-27)
- só na RSSSF (não achado no ogol): Ponte Preta 3-1 Jabaquara (1957-11-27)
- só na RSSSF (não achado no ogol): Santos 6-2 XV de Piracicaba (1957-11-27)
- só na RSSSF (não achado no ogol): Botafogo-SP 2-2 Corinthians (1957-11-30)
- só na RSSSF (não achado no ogol): Jabaquara 1-2 São Paulo (1957-11-30)
- só na RSSSF (não achado no ogol): Santos 6-2 Portuguesa Santista (1957-12-01)
- só na RSSSF (não achado no ogol): XV de Piracicaba 5-3 Portuguesa (1957-12-01)
- só na RSSSF (não achado no ogol): Ponte Preta 2-1 Palmeiras (1957-12-01)
- só na RSSSF (não achado no ogol): São Paulo 2-2 Santos (1957-12-03)
- só na RSSSF (não achado no ogol): Botafogo-SP 2-1 Ponte Preta (1957-12-04)
- só na RSSSF (não achado no ogol): Portuguesa Santista 4-2 XV de Piracicaba (1957-12-04)
- só na RSSSF (não achado no ogol): Portuguesa 2-0 Palmeiras (1957-12-04)
- só na RSSSF (não achado no ogol): Botafogo-SP 0-0 São Paulo (1957-12-07)
- só na RSSSF (não achado no ogol): XV de Piracicaba 1-6 Palmeiras (1957-12-08)
- só na RSSSF (não achado no ogol): Jabaquara 1-1 Portuguesa Santista (1957-12-08)
- só na RSSSF (não achado no ogol): Ponte Preta 1-2 Santos (1957-12-08)
- só na RSSSF (não achado no ogol): Corinthians 1-0 Portuguesa (1957-12-08)
- só na RSSSF (não achado no ogol): Ponte Preta 1-0 XV de Piracicaba (1957-12-11)
- só na RSSSF (não achado no ogol): Portuguesa Santista 1-1 Botafogo-SP (1957-12-11)
- só na RSSSF (não achado no ogol): Palmeiras 2-2 Jabaquara (1957-12-11)
- só na RSSSF (não achado no ogol): Jabaquara 1-2 Botafogo-SP (1957-12-14)
- só na RSSSF (não achado no ogol): Portuguesa 0-6 Santos (1957-12-15)
- só na RSSSF (não achado no ogol): Portuguesa Santista 2-3 São Paulo (1957-12-15)
- só na RSSSF (não achado no ogol): XV de Piracicaba 2-5 Corinthians (1957-12-15)
- só na RSSSF (não achado no ogol): Corinthians 1-0 Jabaquara (1957-12-18)
- só na RSSSF (não achado no ogol): Ponte Preta 2-1 Portuguesa Santista (1957-12-18)
- só na RSSSF (não achado no ogol): Santos 2-1 Botafogo-SP (1957-12-18)
- só na RSSSF (não achado no ogol): São Paulo 3-1 Portuguesa (1957-12-19)
- só na RSSSF (não achado no ogol): Jabaquara 2-0 XV de Piracicaba (1957-12-21)
- só na RSSSF (não achado no ogol): Santos 1-0 Corinthians (1957-12-22)
- só na RSSSF (não achado no ogol): Portuguesa 5-2 Ponte Preta (1957-12-22)
- só na RSSSF (não achado no ogol): São Paulo 1-0 Palmeiras (1957-12-22)
- só na RSSSF (não achado no ogol): Santos 4-1 Palmeiras (1957-12-28)
- só na RSSSF (não achado no ogol): Portuguesa Santista 2-2 Portuguesa (1957-12-29)
- só na RSSSF (não achado no ogol): São Paulo 3-1 Corinthians (1957-12-29)
- só na RSSSF (não achado no ogol): XV de Piracicaba 1-3 Botafogo-SP (1957-12-29)

### 1958

- só na RSSSF (não achado no ogol): Ponte Preta 1-3 Portuguesa Santista (1958-10-02)
- só na RSSSF (não achado no ogol): Nacional-SP 2-0 Guarani (1958-10-04)
- só na RSSSF (não achado no ogol): Jabaquara 0-0 Botafogo-SP (1958-10-05)
- só na RSSSF (não achado no ogol): São Paulo 4-1 Comercial Paulistano (1958-10-05)
- só na RSSSF (não achado no ogol): XV de Piracicaba 5-0 Juventus-SP (1958-10-05)
- só na RSSSF (não achado no ogol): Corinthians 4-0 Portuguesa Santista (1958-10-05)
- só na RSSSF (não achado no ogol): Noroeste 1-1 Portuguesa (1958-10-05)
- só na RSSSF (não achado no ogol): Taubaté 3-2 Santos (1958-10-05)
- só na RSSSF (não achado no ogol): Ferroviária-SP 0-2 Palmeiras (1958-10-05)
- só na RSSSF (não achado no ogol): Ponte Preta 3-0 Ypiranga-SP (1958-10-05)
- só na RSSSF (não achado no ogol): XV de Jaú 2-2 América-SP (1958-10-05)
- só na RSSSF (não achado no ogol): São Paulo 2-0 Taubaté (1958-10-08)
- só na RSSSF (não achado no ogol): Corinthians 2-0 XV de Piracicaba (1958-10-08)
- só na RSSSF (não achado no ogol): Ferroviária-SP 3-0 Ponte Preta (1958-10-08)
- só na RSSSF (não achado no ogol): Ypiranga-SP 3-2 América-SP (1958-10-09)
- só na RSSSF (não achado no ogol): Nacional-SP 4-0 Jabaquara (1958-10-09)
- só na RSSSF (não achado no ogol): Portuguesa Santista 2-0 Portuguesa (1958-10-09)
- só na RSSSF (não achado no ogol): Palmeiras 1-1 XV de Piracicaba (1958-10-11)
- só na RSSSF (não achado no ogol): Santos 3-0 Noroeste (1958-10-11)
- só na RSSSF (não achado no ogol): América-SP 2-4 Corinthians (1958-10-12)
- só na RSSSF (não achado no ogol): Juventus-SP 2-2 Taubaté (1958-10-12)
- só na RSSSF (não achado no ogol): XV de Jaú 1-1 Nacional-SP (1958-10-12)
- só na RSSSF (não achado no ogol): Comercial Paulistano 0-0 Ferroviária-SP (1958-10-12)
- só na RSSSF (não achado no ogol): Portuguesa Santista 5-1 Jabaquara (1958-10-12)
- só na RSSSF (não achado no ogol): Ypiranga-SP 0-3 Botafogo-SP (1958-10-12)
- só na RSSSF (não achado no ogol): Guarani 0-1 São Paulo (1958-10-12)
- só na RSSSF (não achado no ogol): Portuguesa 6-0 Ponte Preta (1958-10-12)
- só na RSSSF (não achado no ogol): Santos 6-1 Portuguesa Santista (1958-10-15)
- só na RSSSF (não achado no ogol): São Paulo 3-2 Nacional-SP (1958-10-15)
- só na RSSSF (não achado no ogol): Portuguesa 4-1 XV de Jaú (1958-10-15)
- só na RSSSF (não achado no ogol): Taubaté 0-0 Ypiranga-SP (1958-10-16)
- só na RSSSF (não achado no ogol): XV de Piracicaba 1-0 Ferroviária-SP (1958-10-16)
- só na RSSSF (não achado no ogol): Palmeiras 4-2 Comercial Paulistano (1958-10-16)
- só na RSSSF (não achado no ogol): Portuguesa Santista 4-1 América-SP (1958-10-18)
- só na RSSSF (não achado no ogol): Corinthians 8-1 Guarani (1958-10-18)
- só na RSSSF (não achado no ogol): Botafogo-SP 2-1 São Paulo (1958-10-18)
- só na RSSSF (não achado no ogol): Santos 3-1 América-SP (1958-10-19)
- só na RSSSF (não achado no ogol): Portuguesa 5-0 Ferroviária-SP (1958-10-22)
- só na RSSSF (não achado no ogol): XV de Jaú 2-4 Ponte Preta (1958-10-22)
- só na RSSSF (não achado no ogol): Santos 6-2 Jabaquara (1958-10-22)
- só na RSSSF (não achado no ogol): Palmeiras 1-1 Juventus-SP (1958-10-22)
- só na RSSSF (não achado no ogol): Taubaté 3-1 América-SP (1958-10-22)
- só na RSSSF (não achado no ogol): Guarani 1-1 Ypiranga-SP (1958-10-23)
- só na RSSSF (não achado no ogol): Botafogo-SP 5-1 Portuguesa Santista (1958-10-23)
- só na RSSSF (não achado no ogol): Corinthians 1-0 Comercial Paulistano (1958-10-23)
- só na RSSSF (não achado no ogol): América-SP 1-2 Nacional-SP (1958-10-25)
- só na RSSSF (não achado no ogol): Jabaquara 1-2 Ferroviária-SP (1958-10-25)
- só na RSSSF (não achado no ogol): Comercial Paulistano 1-4 XV de Piracicaba (1958-10-26)
- só na RSSSF (não achado no ogol): Portuguesa 3-1 Juventus-SP (1958-10-26)
- só na RSSSF (não achado no ogol): Taubaté 2-2 Portuguesa Santista (1958-10-26)
- só na RSSSF (não achado no ogol): Noroeste 3-1 Guarani (1958-10-26)
- só na RSSSF (não achado no ogol): Santos 4-0 Botafogo-SP (1958-10-26)
- só na RSSSF (não achado no ogol): XV de Jaú 0-1 Palmeiras (1958-10-26)
- só na RSSSF (não achado no ogol): Ponte Preta 1-4 Corinthians (1958-10-26)
- só na RSSSF (não achado no ogol): São Paulo 5-1 Ypiranga-SP (1958-10-26)
- só na RSSSF (não achado no ogol): Jabaquara 0-2 Palmeiras (1958-10-28)
- só na RSSSF (não achado no ogol): Botafogo-SP 3-0 XV de Jaú (1958-10-29)
- só na RSSSF (não achado no ogol): São Paulo 4-2 Juventus-SP (1958-10-29)
- só na RSSSF (não achado no ogol): Corinthians 2-0 Ypiranga-SP (1958-10-29)
- só na RSSSF (não achado no ogol): Taubaté 2-0 Ponte Preta (1958-10-29)
- só na RSSSF (não achado no ogol): Portuguesa 1-1 Santos (1958-10-29)
- só na RSSSF (não achado no ogol): Botafogo-SP 3-3 Corinthians (1958-11-01)
- só na RSSSF (não achado no ogol): Juventus-SP 3-2 Ypiranga-SP (1958-11-01)
- só na RSSSF (não achado no ogol): Portuguesa Santista 3-0 Guarani (1958-11-01)
- só na RSSSF (não achado no ogol): Comercial Paulistano 2-0 Jabaquara (1958-11-01)
- só na RSSSF (não achado no ogol): Palmeiras 4-2 Nacional-SP (1958-11-01)
- só na RSSSF (não achado no ogol): XV de Jaú 0-0 Santos (1958-11-01)
- só na RSSSF (não achado no ogol): América-SP 0-2 São Paulo (1958-11-01)
- só na RSSSF (não achado no ogol): Ferroviária-SP 3-0 Taubaté (1958-11-01)
- só na RSSSF (não achado no ogol): Ponte Preta 0-0 Noroeste (1958-11-01)
- só na RSSSF (não achado no ogol): XV de Piracicaba 3-3 Portuguesa (1958-11-01)
- só na RSSSF (não achado no ogol): Comercial Paulistano 1-0 Taubaté (1958-11-05)
- só na RSSSF (não achado no ogol): Noroeste 3-1 Jabaquara (1958-11-05)
- só na RSSSF (não achado no ogol): São Paulo 2-1 Ferroviária-SP (1958-11-05)
- só na RSSSF (não achado no ogol): Jabaquara 2-1 XV de Jaú (1958-11-05)
- só na RSSSF (não achado no ogol): Palmeiras 2-1 Corinthians (1958-11-05)
- só na RSSSF (não achado no ogol): XV de Piracicaba 2-0 Guarani (1958-11-05)
- só na RSSSF (não achado no ogol): Juventus-SP 3-2 Nacional-SP (1958-11-05)
- só na RSSSF (não achado no ogol): Portuguesa Santista 4-2 Nacional-SP (1958-11-05)
- só na RSSSF (não achado no ogol): Ferroviária-SP 3-0 Ypiranga-SP (1958-11-06)
- só na RSSSF (não achado no ogol): Portuguesa 3-1 Taubaté (1958-11-06)
- só na RSSSF (não achado no ogol): Noroeste 1-0 Comercial Paulistano (1958-11-06)
- só na RSSSF (não achado no ogol): XV de Piracicaba 0-5 Santos (1958-11-06)
- só na RSSSF (não achado no ogol): Ponte Preta 2-1 Palmeiras (1958-11-06)
- só na RSSSF (não achado no ogol): Palmeiras 4-3 Botafogo-SP (1958-11-08)
- só na RSSSF (não achado no ogol): Comercial Paulistano 2-1 Nacional-SP (1958-11-09)
- só na RSSSF (não achado no ogol): Jabaquara 2-0 Ponte Preta (1958-11-09)
- só na RSSSF (não achado no ogol): São Paulo 3-1 Portuguesa (1958-11-09)
- só na RSSSF (não achado no ogol): Ferroviária-SP 2-1 Santos (1958-11-09)
- só na RSSSF (não achado no ogol): Juventus-SP 1-2 XV de Jaú (1958-11-09)
- só na RSSSF (não achado no ogol): Taubaté 2-1 Corinthians (1958-11-09)
- só na RSSSF (não achado no ogol): Guarani 1-0 América-SP (1958-11-09)
- só na RSSSF (não achado no ogol): Noroeste 3-3 XV de Piracicaba (1958-11-09)
- só na RSSSF (não achado no ogol): Ypiranga-SP 1-1 Portuguesa Santista (1958-11-09)
- só na RSSSF (não achado no ogol): Ferroviária-SP 4-2 XV de Jaú (1958-11-12)
- só na RSSSF (não achado no ogol): Portuguesa 1-1 Comercial Paulistano (1958-11-12)
- só na RSSSF (não achado no ogol): Juventus-SP 1-0 Botafogo-SP (1958-11-12)
- só na RSSSF (não achado no ogol): Portuguesa Santista 1-1 XV de Piracicaba (1958-11-12)
- só na RSSSF (não achado no ogol): Jabaquara 1-1 Corinthians (1958-11-13)
- só na RSSSF (não achado no ogol): Nacional-SP 3-1 Noroeste (1958-11-13)
- só na RSSSF (não achado no ogol): Botafogo-SP 0-1 Taubaté (1958-11-15)
- só na RSSSF (não achado no ogol): Portuguesa Santista 5-0 Comercial Paulistano (1958-11-15)
- só na RSSSF (não achado no ogol): Corinthians 3-1 Portuguesa (1958-11-16)
- só na RSSSF (não achado no ogol): Ponte Preta 1-1 Nacional-SP (1958-11-16)
- só na RSSSF (não achado no ogol): XV de Piracicaba 2-2 São Paulo (1958-11-16)
- só na RSSSF (não achado no ogol): Juventus-SP 1-0 Guarani (1958-11-16)
- só na RSSSF (não achado no ogol): Santos 2-1 Palmeiras (1958-11-16)
- só na RSSSF (não achado no ogol): América-SP 4-1 Jabaquara (1958-11-16)
- só na RSSSF (não achado no ogol): Noroeste 3-2 Ferroviária-SP (1958-11-16)
- só na RSSSF (não achado no ogol): XV de Jaú 5-2 Ypiranga-SP (1958-11-16)
- só na RSSSF (não achado no ogol): Santos 9-1 Comercial Paulistano (1958-11-19)
- só na RSSSF (não achado no ogol): Botafogo-SP 3-0 Portuguesa (1958-11-19)
- só na RSSSF (não achado no ogol): XV de Jaú 1-1 Noroeste (1958-11-19)
- só na RSSSF (não achado no ogol): Juventus-SP 1-1 Ferroviária-SP (1958-11-19)
- só na RSSSF (não achado no ogol): XV de Piracicaba 2-0 Nacional-SP (1958-11-20)
- só na RSSSF (não achado no ogol): Botafogo-SP 2-1 Ferroviária-SP (1958-11-22)
- só na RSSSF (não achado no ogol): Comercial Paulistano 0-2 Guarani (1958-11-22)
- só na RSSSF (não achado no ogol): Jabaquara 1-0 Taubaté (1958-11-22)
- só na RSSSF (não achado no ogol): América-SP 1-0 Palmeiras (1958-11-23)
- só na RSSSF (não achado no ogol): XV de Jaú 0-4 Corinthians (1958-11-23)
- só na RSSSF (não achado no ogol): Ponte Preta 1-2 Santos (1958-11-23)
- só na RSSSF (não achado no ogol): Ypiranga-SP 1-0 XV de Piracicaba (1958-11-23)
- só na RSSSF (não achado no ogol): Portuguesa 2-1 Nacional-SP (1958-11-23)
- só na RSSSF (não achado no ogol): Portuguesa 1-0 América-SP (1958-11-26)
- só na RSSSF (não achado no ogol): Corinthians 1-1 São Paulo (1958-11-26)
- só na RSSSF (não achado no ogol): Ypiranga-SP 2-0 Comercial Paulistano (1958-11-27)
- só na RSSSF (não achado no ogol): Noroeste 3-0 Botafogo-SP (1958-11-27)
- só na RSSSF (não achado no ogol): Palmeiras 6-0 Guarani (1958-11-27)
- só na RSSSF (não achado no ogol): Jabaquara 1-2 Juventus-SP (1958-11-29)
- só na RSSSF (não achado no ogol): São Paulo 1-1 Ponte Preta (1958-11-29)
- só na RSSSF (não achado no ogol): América-SP 1-1 XV de Piracicaba (1958-11-30)
- só na RSSSF (não achado no ogol): Guarani 2-8 Portuguesa (1958-11-30)
- só na RSSSF (não achado no ogol): Taubaté 2-2 Palmeiras (1958-11-30)
- só na RSSSF (não achado no ogol): Botafogo-SP 4-2 Comercial Paulistano (1958-11-30)
- só na RSSSF (não achado no ogol): Nacional-SP 3-4 Santos (1958-11-30)
- só na RSSSF (não achado no ogol): Ypiranga-SP 0-0 Noroeste (1958-11-30)
- só na RSSSF (não achado no ogol): Ferroviária-SP 2-3 Corinthians (1958-11-30)
- só na RSSSF (não achado no ogol): Portuguesa Santista 2-1 XV de Jaú (1958-11-30)
- só na RSSSF (não achado no ogol): Ponte Preta 1-1 América-SP (1958-12-03)
- só na RSSSF (não achado no ogol): São Paulo 4-1 Jabaquara (1958-12-03)
- só na RSSSF (não achado no ogol): Nacional-SP 4-2 Taubaté (1958-12-03)
- só na RSSSF (não achado no ogol): Guarani 5-2 Ferroviária-SP (1958-12-04)
- só na RSSSF (não achado no ogol): XV de Jaú 1-0 XV de Piracicaba (1958-12-04)
- só na RSSSF (não achado no ogol): Corinthians 1-1 Juventus-SP (1958-12-04)
- só na RSSSF (não achado no ogol): Palmeiras 2-2 São Paulo (1958-12-06)
- só na RSSSF (não achado no ogol): Portuguesa Santista 2-1 Noroeste (1958-12-06)
- só na RSSSF (não achado no ogol): América-SP 3-1 Botafogo-SP (1958-12-06)
- só na RSSSF (não achado no ogol): Juventus-SP 4-2 Comercial Paulistano (1958-12-07)
- só na RSSSF (não achado no ogol): Santos 6-1 Corinthians (1958-12-07)
- só na RSSSF (não achado no ogol): Ponte Preta 2-2 Guarani (1958-12-07)
- só na RSSSF (não achado no ogol): XV de Jaú 5-1 Taubaté (1958-12-07)
- só na RSSSF (não achado no ogol): Ferroviária-SP 4-0 Nacional-SP (1958-12-07)
- só na RSSSF (não achado no ogol): Portuguesa 5-2 Ypiranga-SP (1958-12-07)
- só na RSSSF (não achado no ogol): XV de Piracicaba 4-2 Jabaquara (1958-12-07)
- só na RSSSF (não achado no ogol): Noroeste 1-3 São Paulo (1958-12-09)
- só na RSSSF (não achado no ogol): Santos 7-1 Juventus-SP (1958-12-09)
- só na RSSSF (não achado no ogol): Portuguesa 2-0 Jabaquara (1958-12-10)
- só na RSSSF (não achado no ogol): Palmeiras 4-2 Ypiranga-SP (1958-12-10)
- só na RSSSF (não achado no ogol): XV de Piracicaba 2-1 Ponte Preta (1958-12-11)
- só na RSSSF (não achado no ogol): América-SP 3-1 Noroeste (1958-12-11)
- só na RSSSF (não achado no ogol): Nacional-SP 2-1 Botafogo-SP (1958-12-11)
- só na RSSSF (não achado no ogol): Portuguesa Santista 1-1 São Paulo (1958-12-13)
- só na RSSSF (não achado no ogol): Comercial Paulistano 3-1 XV de Jaú (1958-12-13)
- só na RSSSF (não achado no ogol): Palmeiras 2-0 Portuguesa (1958-12-13)
- só na RSSSF (não achado no ogol): Guarani 1-7 Santos (1958-12-14)
- só na RSSSF (não achado no ogol): Taubaté 1-2 XV de Piracicaba (1958-12-14)
- só na RSSSF (não achado no ogol): Botafogo-SP 5-1 Ponte Preta (1958-12-14)
- só na RSSSF (não achado no ogol): Juventus-SP 3-1 Noroeste (1958-12-14)
- só na RSSSF (não achado no ogol): Ypiranga-SP 3-3 Jabaquara (1958-12-14)
- só na RSSSF (não achado no ogol): Ferroviária-SP 1-0 América-SP (1958-12-14)
- só na RSSSF (não achado no ogol): Nacional-SP 2-2 Corinthians (1958-12-14)
- só na RSSSF (não achado no ogol): Portuguesa Santista 1-2 Palmeiras (1958-12-16)
- só na RSSSF (não achado no ogol): América-SP 1-0 Juventus-SP (1958-12-17)
- só na RSSSF (não achado no ogol): Taubaté 3-0 Guarani (1958-12-17)
- só na RSSSF (não achado no ogol): Corinthians 4-0 Noroeste (1958-12-18)
- só na RSSSF (não achado no ogol): São Paulo 2-2 Santos (1958-12-18)
- só na RSSSF (não achado no ogol): Comercial Paulistano 0-2 Ponte Preta (1958-12-18)
- só na RSSSF (não achado no ogol): Juventus-SP 1-1 Portuguesa Santista (1958-12-20)
- só na RSSSF (não achado no ogol): Taubaté 5-2 Noroeste (1958-12-20)
- só na RSSSF (não achado no ogol): Guarani 1-0 Botafogo-SP (1958-12-20)

### 1959

- sem ocorrências

### 1960

- placar diferente no ogol — São Paulo x América-SP (1960-07-28): RSSSF 3-2, ogol 3-0; fica o da RSSSF

### 1961

- sem ocorrências

### 1962

- tabela publicada x jogos — 2º Turno / -: Santos tabela [30, 24, 5, 1, 105, 28] jogos [30, 23, 5, 2, 102, 31] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Corinthians tabela [30, 18, 7, 5, 77, 37] jogos [30, 18, 6, 6, 76, 37] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: São Paulo tabela [30, 18, 5, 7, 63, 39] jogos [30, 19, 5, 6, 66, 36] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Portuguesa tabela [30, 12, 9, 9, 42, 43] jogos [30, 11, 9, 10, 40, 44] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Botafogo-SP tabela [30, 14, 4, 12, 65, 52] jogos [30, 14, 4, 12, 60, 51] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Ferroviária-SP tabela [30, 13, 6, 11, 51, 44] jogos [30, 13, 7, 10, 51, 43] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Guarani tabela [30, 11, 7, 12, 50, 45] jogos [30, 12, 6, 12, 50, 44] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Esportiva Guaratinguetá tabela [30, 9, 7, 14, 30, 48] jogos [30, 9, 7, 14, 28, 46] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: XV de Piracicaba tabela [30, 9, 6, 15, 38, 63] jogos [30, 8, 7, 15, 36, 58] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Prudentina tabela [30, 9, 5, 16, 38, 65] jogos [30, 10, 5, 15, 40, 63] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Taubaté tabela [30, 4, 5, 21, 27, 73] jogos [30, 4, 5, 21, 24, 71] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1963

- sem ocorrências

### 1964

- sem ocorrências

### 1965

- só na RSSSF (não achado no ogol): Juventus-SP 1-3 Santos (1965-09-08)
- só na RSSSF (não achado no ogol): Portuguesa 2-0 São Bento (1965-09-11)
- só na RSSSF (não achado no ogol): Santos 7-0 Guarani (1965-09-11)
- só na RSSSF (não achado no ogol): Juventus-SP 2-0 Noroeste (1965-09-11)
- só na RSSSF (não achado no ogol): Comercial-RP 2-0 Botafogo-SP (1965-09-12)
- só na RSSSF (não achado no ogol): Prudentina 0-0 Portuguesa Santista (1965-09-12)
- só na RSSSF (não achado no ogol): Ferroviária-SP 0-1 São Paulo (1965-09-12)
- só na RSSSF (não achado no ogol): América-SP 2-0 XV de Piracicaba (1965-09-12)
- só na RSSSF (não achado no ogol): Palmeiras 0-0 Corinthians (1965-09-12)
- só na RSSSF (não achado no ogol): Palmeiras 2-0 São Bento (1965-09-15)
- só na RSSSF (não achado no ogol): Portuguesa Santista 2-1 Juventus-SP (1965-09-16)
- só na RSSSF (não achado no ogol): Corinthians 2-1 Ferroviária-SP (1965-09-16)
- só na RSSSF (não achado no ogol): São Paulo 4-0 América-SP (1965-09-18)
- só na RSSSF (não achado no ogol): Ferroviária-SP 2-3 Prudentina (1965-09-19)
- só na RSSSF (não achado no ogol): Santos 0-1 Palmeiras (1965-09-19)
- só na RSSSF (não achado no ogol): Guarani 6-0 Noroeste (1965-09-19)
- só na RSSSF (não achado no ogol): São Bento 1-0 Botafogo-SP (1965-09-19)
- só na RSSSF (não achado no ogol): Comercial-RP 2-2 Juventus-SP (1965-09-19)
- só na RSSSF (não achado no ogol): Portuguesa 3-1 Portuguesa Santista (1965-09-19)
- só na RSSSF (não achado no ogol): XV de Piracicaba 1-3 Corinthians (1965-09-19)
- só na RSSSF (não achado no ogol): Comercial-RP 3-2 Noroeste (1965-09-22)
- só na RSSSF (não achado no ogol): XV de Piracicaba 0-2 Guarani (1965-09-22)
- só na RSSSF (não achado no ogol): Santos 4-2 Ferroviária-SP (1965-09-22)
- só na RSSSF (não achado no ogol): São Bento 2-0 Portuguesa Santista (1965-09-22)
- só na RSSSF (não achado no ogol): Palmeiras 1-0 Prudentina (1965-09-23)
- só na RSSSF (não achado no ogol): Guarani 1-0 Portuguesa Santista (1965-09-26)
- só na RSSSF (não achado no ogol): XV de Piracicaba 3-1 Comercial-RP (1965-09-26)
- só na RSSSF (não achado no ogol): Prudentina 0-0 São Paulo (1965-09-26)
- só na RSSSF (não achado no ogol): América-SP 2-2 Botafogo-SP (1965-09-26)
- só na RSSSF (não achado no ogol): São Bento 2-4 Corinthians (1965-09-26)
- só na RSSSF (não achado no ogol): Portuguesa Santista 2-0 América-SP (1965-09-29)
- só na RSSSF (não achado no ogol): Botafogo-SP 3-2 Guarani (1965-09-29)
- só na RSSSF (não achado no ogol): Ferroviária-SP 2-0 Portuguesa (1965-09-29)
- só na RSSSF (não achado no ogol): Botafogo-SP 2-0 Ferroviária-SP (1965-10-02)
- só na RSSSF (não achado no ogol): Juventus-SP 2-1 XV de Piracicaba (1965-10-02)
- só na RSSSF (não achado no ogol): América-SP 1-1 São Bento (1965-10-03)
- só na RSSSF (não achado no ogol): Noroeste 0-3 Santos (1965-10-03)
- só na RSSSF (não achado no ogol): Comercial-RP 3-1 Palmeiras (1965-10-03)
- só na RSSSF (não achado no ogol): Portuguesa Santista 1-1 Portuguesa (1965-10-03)
- só na RSSSF (não achado no ogol): Corinthians 1-1 São Paulo (1965-10-03)
- só na RSSSF (não achado no ogol): Prudentina 1-0 Guarani (1965-10-03)
- só na RSSSF (não achado no ogol): Guarani 0-2 São Paulo (1965-10-06)
- só na RSSSF (não achado no ogol): Noroeste 0-0 Portuguesa Santista (1965-10-06)
- só na RSSSF (não achado no ogol): Portuguesa 2-2 Palmeiras (1965-10-06)
- só na RSSSF (não achado no ogol): Santos 4-2 São Bento (1965-10-07)
- só na RSSSF (não achado no ogol): Ferroviária-SP 2-0 XV de Piracicaba (1965-10-10)
- só na RSSSF (não achado no ogol): Portuguesa Santista 0-0 Botafogo-SP (1965-10-10)
- só na RSSSF (não achado no ogol): Comercial-RP 0-2 Santos (1965-10-10)
- só na RSSSF (não achado no ogol): Guarani 2-0 América-SP (1965-10-10)
- só na RSSSF (não achado no ogol): São Paulo 3-1 Juventus-SP (1965-10-10)
- só na RSSSF (não achado no ogol): Corinthians 2-0 Prudentina (1965-10-10)
- só na RSSSF (não achado no ogol): Noroeste 1-0 Palmeiras (1965-10-10)
- só na RSSSF (não achado no ogol): Santos 3-0 Portuguesa Santista (1965-10-13)
- só na RSSSF (não achado no ogol): Portuguesa 5-1 Guarani (1965-10-14)
- só na RSSSF (não achado no ogol): Santos 0-0 São Paulo (1965-10-16)
- só na RSSSF (não achado no ogol): Botafogo-SP 3-0 XV de Piracicaba (1965-10-17)
- só na RSSSF (não achado no ogol): Palmeiras 1-0 Guarani (1965-10-17)
- só na RSSSF (não achado no ogol): Corinthians 2-1 Portuguesa Santista (1965-10-17)
- só na RSSSF (não achado no ogol): Prudentina 2-0 Comercial-RP (1965-10-17)
- só na RSSSF (não achado no ogol): América-SP 0-1 Portuguesa (1965-10-17)
- só na RSSSF (não achado no ogol): Ferroviária-SP 0-2 Noroeste (1965-10-17)
- só na RSSSF (não achado no ogol): São Bento 3-0 Juventus-SP (1965-10-17)
- só na RSSSF (não achado no ogol): América-SP 1-0 Ferroviária-SP (1965-10-20)
- só na RSSSF (não achado no ogol): São Bento 4-1 Noroeste (1965-10-20)
- só na RSSSF (não achado no ogol): XV de Piracicaba 1-3 Prudentina (1965-10-20)
- só na RSSSF (não achado no ogol): Corinthians 6-2 Juventus-SP (1965-10-21)
- só na RSSSF (não achado no ogol): Palmeiras 2-1 São Paulo (1965-10-23)
- só na RSSSF (não achado no ogol): São Paulo 2-1 Botafogo-SP (1965-10-23)
- só na RSSSF (não achado no ogol): América-SP 0-4 Santos (1965-10-24)
- só na RSSSF (não achado no ogol): Ferroviária-SP 1-2 Guarani (1965-10-24)
- só na RSSSF (não achado no ogol): XV de Piracicaba 3-1 São Bento (1965-10-24)
- só na RSSSF (não achado no ogol): Botafogo-SP 0-2 Prudentina (1965-10-24)
- só na RSSSF (não achado no ogol): Guarani 0-1 Juventus-SP (1965-10-24)
- só na RSSSF (não achado no ogol): Corinthians 2-1 Comercial-RP (1965-10-24)
- só na RSSSF (não achado no ogol): Noroeste 1-0 Portuguesa (1965-10-24)
- só na RSSSF (não achado no ogol): Portuguesa 0-1 Santos (1965-10-27)
- só na RSSSF (não achado no ogol): Juventus-SP 0-2 América-SP (1965-10-30)
- só na RSSSF (não achado no ogol): Comercial-RP 1-0 São Paulo (1965-10-31)
- só na RSSSF (não achado no ogol): Noroeste 1-0 XV de Piracicaba (1965-10-31)
- só na RSSSF (não achado no ogol): Corinthians 2-0 Portuguesa (1965-10-31)
- só na RSSSF (não achado no ogol): Prudentina 2-5 Santos (1965-10-31)
- só na RSSSF (não achado no ogol): Guarani 1-1 São Bento (1965-10-31)
- só na RSSSF (não achado no ogol): XV de Piracicaba 1-1 Portuguesa Santista (1965-11-03)
- só na RSSSF (não achado no ogol): América-SP 2-0 Comercial-RP (1965-11-03)
- só na RSSSF (não achado no ogol): Portuguesa 1-1 Botafogo-SP (1965-11-04)
- só na RSSSF (não achado no ogol): Comercial-RP 3-1 Ferroviária-SP (1965-11-06)
- só na RSSSF (não achado no ogol): Botafogo-SP 2-2 Juventus-SP (1965-11-07)
- só na RSSSF (não achado no ogol): Prudentina 1-2 São Bento (1965-11-07)
- só na RSSSF (não achado no ogol): Corinthians 4-0 América-SP (1965-11-07)
- só na RSSSF (não achado no ogol): São Paulo 8-0 Noroeste (1965-11-07)
- só na RSSSF (não achado no ogol): Portuguesa Santista 1-2 Palmeiras (1965-11-07)
- só na RSSSF (não achado no ogol): XV de Piracicaba 0-2 Santos (1965-11-07)
- só na RSSSF (não achado no ogol): Botafogo-SP 1-0 Noroeste (1965-11-10)
- só na RSSSF (não achado no ogol): Portuguesa Santista 1-3 Comercial-RP (1965-11-10)
- só na RSSSF (não achado no ogol): Juventus-SP 1-1 Portuguesa (1965-11-11)
- só na RSSSF (não achado no ogol): Palmeiras 2-1 América-SP (1965-11-13)
- só na RSSSF (não achado no ogol): São Paulo 6-1 Portuguesa Santista (1965-11-13)
- só na RSSSF (não achado no ogol): Ferroviária-SP 1-1 Juventus-SP (1965-11-14)
- só na RSSSF (não achado no ogol): XV de Piracicaba 1-0 Portuguesa (1965-11-14)
- só na RSSSF (não achado no ogol): Noroeste 0-0 Prudentina (1965-11-14)
- só na RSSSF (não achado no ogol): Comercial-RP 2-3 São Bento (1965-11-14)
- só na RSSSF (não achado no ogol): Santos 4-2 Corinthians (1965-11-14)
- só na RSSSF (não achado no ogol): Juventus-SP 2-0 Prudentina (1965-11-17)
- só na RSSSF (não achado no ogol): Portuguesa Santista 1-0 Ferroviária-SP (1965-11-17)
- só na RSSSF (não achado no ogol): América-SP 2-1 Noroeste (1965-11-20)
- só na RSSSF (não achado no ogol): Ferroviária-SP 3-2 São Bento (1965-11-20)
- só na RSSSF (não achado no ogol): Palmeiras 1-0 XV de Piracicaba (1965-11-24)
- só na RSSSF (não achado no ogol): Portuguesa 2-1 São Paulo (1965-11-24)
- só na RSSSF (não achado no ogol): Juventus-SP 1-0 Portuguesa Santista (1965-11-24)
- só na RSSSF (não achado no ogol): Santos 5-0 Botafogo-SP (1965-11-25)
- só na RSSSF (não achado no ogol): Guarani 3-1 Corinthians (1965-11-25)
- só na RSSSF (não achado no ogol): Palmeiras 4-3 Ferroviária-SP (1965-11-27)
- só na RSSSF (não achado no ogol): Santos 4-0 Juventus-SP (1965-11-27)
- só na RSSSF (não achado no ogol): Corinthians 5-1 Noroeste (1965-11-28)
- só na RSSSF (não achado no ogol): São Bento 2-2 Portuguesa (1965-11-28)
- só na RSSSF (não achado no ogol): Guarani 3-1 Comercial-RP (1965-11-28)
- só na RSSSF (não achado no ogol): São Paulo 4-1 XV de Piracicaba (1965-11-28)
- só na RSSSF (não achado no ogol): Prudentina 1-1 América-SP (1965-11-28)
- só na RSSSF (não achado no ogol): Palmeiras 2-1 Botafogo-SP (1965-11-30)
- só na RSSSF (não achado no ogol): São Bento 2-0 São Paulo (1965-12-01)
- só na RSSSF (não achado no ogol): Guarani 0-1 Santos (1965-12-04)
- só na RSSSF (não achado no ogol): São Paulo 1-0 Ferroviária-SP (1965-12-04)
- só na RSSSF (não achado no ogol): Comercial-RP 0-0 Botafogo-SP (1965-12-05)
- só na RSSSF (não achado no ogol): Portuguesa Santista 1-1 Prudentina (1965-12-05)
- só na RSSSF (não achado no ogol): Noroeste 2-2 Juventus-SP (1965-12-05)
- só na RSSSF (não achado no ogol): XV de Piracicaba 2-1 América-SP (1965-12-05)
- só na RSSSF (não achado no ogol): Palmeiras 1-0 Corinthians (1965-12-05)
- só na RSSSF (não achado no ogol): Ferroviária-SP 2-1 Corinthians (1965-12-08)
- só na RSSSF (não achado no ogol): Portuguesa 3-1 Comercial-RP (1965-12-09)
- só na RSSSF (não achado no ogol): São Bento 1-3 Palmeiras (1965-12-09)
- só na RSSSF (não achado no ogol): Botafogo-SP 0-0 Corinthians (1965-12-11)
- só na RSSSF (não achado no ogol): América-SP 1-0 São Paulo (1965-12-12)
- só na RSSSF (não achado no ogol): Palmeiras 5-0 Santos (1965-12-12)
- só na RSSSF (não achado no ogol): Juventus-SP 1-2 Comercial-RP (1965-12-12)
- só na RSSSF (não achado no ogol): Prudentina 2-0 Ferroviária-SP (1965-12-12)
- só na RSSSF (não achado no ogol): Noroeste 1-1 Guarani (1965-12-12)
- só na RSSSF (não achado no ogol): Corinthians 7-0 XV de Piracicaba (1965-12-15)
- só na RSSSF (não achado no ogol): Botafogo-SP 1-2 São Bento (1965-12-15)
- só na RSSSF (não achado no ogol): Palmeiras 1-0 Juventus-SP (1965-12-16)
- só na RSSSF (não achado no ogol): Prudentina 1-1 Portuguesa (1965-12-16)

### 1966

- tabela publicada x jogos — 2º Turno / -: Corinthians tabela [28, 17, 5, 6, 57, 33] jogos [28, 17, 5, 6, 56, 33] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — 2º Turno / -: Prudentina tabela [28, 10, 6, 12, 46, 46] jogos [28, 10, 6, 12, 45, 45] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Juventus-SP tabela [28, 7, 8, 13, 26, 44] jogos [28, 7, 8, 13, 25, 42] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Guarani tabela [28, 9, 3, 16, 34, 43] jogos [28, 9, 3, 16, 34, 46] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Noroeste tabela [28, 7, 7, 14, 33, 57] jogos [28, 7, 7, 14, 36, 57] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar corrigido pelo ogol — Santos x Guarani (1966-11-26): RSSSF 1-2, ogol 2-1; fica o do ogol, que fecha com a tabela publicada
- jogo só no ogol, incluído em 1º Turno: Portuguesa Santista 1-1 Corinthians (1966-08-14)
- campeão pela lista oficial, Palmeiras; o 1º pela soma dos jogos da última fase é Santos (desempate, jogo extra ou pontos tirados fora de campo)

### 1967

- tabela publicada x jogos — Fase única / -: Santos tabela [26, 16, 9, 1, 61, 32] jogos [26, 16, 9, 1, 61, 29] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: América-SP tabela [26, 9, 5, 12, 41, 41] jogos [26, 9, 5, 12, 41, 43] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Botafogo-SP tabela [26, 7, 6, 13, 38, 55] jogos [26, 7, 6, 13, 33, 53] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: São Bento tabela [26, 6, 8, 12, 25, 38] jogos [26, 6, 8, 12, 23, 36] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Portuguesa Santista tabela [26, 7, 5, 14, 24, 38] jogos [26, 7, 5, 14, 25, 38] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Juventus-SP tabela [26, 6, 6, 14, 26, 43] jogos [26, 6, 6, 14, 27, 43] — há jogo do clube sem conferência no ogol
- só na RSSSF (não achado no ogol): Botafogo-SP 1-0 Juventus-SP (1967-09-20)
- só na RSSSF (não achado no ogol): Guarani 2-0 América-SP (1967-09-20)
- só na RSSSF (não achado no ogol): Portuguesa Santista 1-2 América-SP (1967-09-23)
- só na RSSSF (não achado no ogol): Ferroviária-SP 0-2 Comercial-RP (1967-09-24)
- só na RSSSF (não achado no ogol): Prudentina 1-2 Guarani (1967-09-24)
- só na RSSSF (não achado no ogol): Juventus-SP 1-2 São Bento (1967-09-24)
- só na RSSSF (não achado no ogol): Portuguesa Santista 2-0 Ferroviária-SP (1967-10-01)
- só na RSSSF (não achado no ogol): Botafogo-SP 2-0 Comercial-RP (1967-10-01)
- só na RSSSF (não achado no ogol): Juventus-SP 3-0 Prudentina (1967-10-01)
- só na RSSSF (não achado no ogol): Guarani 1-0 São Bento (1967-10-01)
- só na RSSSF (não achado no ogol): Portuguesa Santista 0-2 Corinthians (1967-10-04)
- só na RSSSF (não achado no ogol): Santos 5-1 Botafogo-SP (1967-10-05)
- só na RSSSF (não achado no ogol): América-SP 2-3 Santos (1967-10-08)
- só na RSSSF (não achado no ogol): Ferroviária-SP 1-0 São Paulo (1967-10-08)
- só na RSSSF (não achado no ogol): Prudentina 2-2 Portuguesa Santista (1967-10-08)
- só na RSSSF (não achado no ogol): Botafogo-SP 2-3 Palmeiras (1967-10-08)
- só na RSSSF (não achado no ogol): Corinthians 1-0 Juventus-SP (1967-10-08)
- só na RSSSF (não achado no ogol): Palmeiras 1-0 Portuguesa Santista (1967-10-14)
- só na RSSSF (não achado no ogol): Comercial-RP 2-0 Prudentina (1967-10-14)
- só na RSSSF (não achado no ogol): Juventus-SP 3-0 Guarani (1967-10-15)
- só na RSSSF (não achado no ogol): Ferroviária-SP 2-1 América-SP (1967-10-15)
- só na RSSSF (não achado no ogol): Botafogo-SP 2-0 Portuguesa (1967-10-15)
- só na RSSSF (não achado no ogol): São Bento 0-0 Corinthians (1967-10-15)
- só na RSSSF (não achado no ogol): São Paulo 2-2 Santos (1967-10-15)
- só na RSSSF (não achado no ogol): América-SP 1-1 Palmeiras (1967-10-22)
- só na RSSSF (não achado no ogol): Portuguesa Santista 1-1 Botafogo-SP (1967-10-22)
- só na RSSSF (não achado no ogol): Prudentina 1-3 Santos (1967-10-22)
- só na RSSSF (não achado no ogol): Comercial-RP 3-2 Juventus-SP (1967-10-22)
- só na RSSSF (não achado no ogol): Guarani 1-1 Corinthians (1967-10-22)
- só na RSSSF (não achado no ogol): São Paulo 2-1 Portuguesa (1967-10-22)
- só na RSSSF (não achado no ogol): Portuguesa 3-0 Ferroviária-SP (1967-10-28)
- só na RSSSF (não achado no ogol): Portuguesa Santista 2-1 Guarani (1967-10-29)
- só na RSSSF (não achado no ogol): Botafogo-SP 3-2 Prudentina (1967-10-29)
- só na RSSSF (não achado no ogol): São Bento 0-0 São Paulo (1967-10-29)
- só na RSSSF (não achado no ogol): Palmeiras 1-4 Santos (1967-10-29)
- só na RSSSF (não achado no ogol): Corinthians 4-0 Comercial-RP (1967-10-29)
- só na RSSSF (não achado no ogol): Santos 4-1 Juventus-SP (1967-11-01)
- só na RSSSF (não achado no ogol): São Paulo 6-0 Botafogo-SP (1967-11-04)
- só na RSSSF (não achado no ogol): América-SP 5-0 São Bento (1967-11-05)
- só na RSSSF (não achado no ogol): Ferroviária-SP 3-0 Prudentina (1967-11-05)
- só na RSSSF (não achado no ogol): Corinthians 4-0 Portuguesa (1967-11-05)
- só na RSSSF (não achado no ogol): Comercial-RP 2-4 Palmeiras (1967-11-05)
- só na RSSSF (não achado no ogol): Palmeiras 2-2 Portuguesa (1967-11-10)
- só na RSSSF (não achado no ogol): América-SP 3-0 Corinthians (1967-11-12)
- só na RSSSF (não achado no ogol): Prudentina 2-0 São Bento (1967-11-12)
- só na RSSSF (não achado no ogol): Comercial-RP 1-1 Santos (1967-11-12)
- só na RSSSF (não achado no ogol): São Paulo 1-0 Portuguesa Santista (1967-11-12)
- só na RSSSF (não achado no ogol): Portuguesa Santista 1-0 Comercial-RP (1967-11-15)
- só na RSSSF (não achado no ogol): Ferroviária-SP 2-0 Botafogo-SP (1967-11-15)
- só na RSSSF (não achado no ogol): Portuguesa 3-1 Guarani (1967-11-15)
- só na RSSSF (não achado no ogol): Prudentina 1-0 América-SP (1967-11-15)
- só na RSSSF (não achado no ogol): São Bento 1-2 Palmeiras (1967-11-15)
- só na RSSSF (não achado no ogol): São Paulo 2-1 Juventus-SP (1967-11-15)
- só na RSSSF (não achado no ogol): Comercial-RP 2-3 São Paulo (1967-11-19)
- só na RSSSF (não achado no ogol): São Bento 1-1 Santos (1967-11-19)
- só na RSSSF (não achado no ogol): Guarani 0-0 Ferroviária-SP (1967-11-19)
- só na RSSSF (não achado no ogol): Palmeiras 2-0 Corinthians (1967-11-19)
- só na RSSSF (não achado no ogol): Ferroviária-SP 2-0 Palmeiras (1967-11-26)
- só na RSSSF (não achado no ogol): Comercial-RP 2-0 São Bento (1967-11-26)
- só na RSSSF (não achado no ogol): Guarani 4-1 Botafogo-SP (1967-11-26)
- só na RSSSF (não achado no ogol): Santos 0-0 Portuguesa (1967-11-26)
- só na RSSSF (não achado no ogol): São Paulo 6-1 América-SP (1967-11-26)
- só na RSSSF (não achado no ogol): Corinthians 4-1 Prudentina (1967-11-26)
- só na RSSSF (não achado no ogol): Portuguesa 2-0 Portuguesa Santista (1967-12-02)
- só na RSSSF (não achado no ogol): Botafogo-SP 0-3 Corinthians (1967-12-02)
- só na RSSSF (não achado no ogol): América-SP 2-3 Comercial-RP (1967-12-03)
- só na RSSSF (não achado no ogol): Ferroviária-SP 1-1 Juventus-SP (1967-12-03)
- só na RSSSF (não achado no ogol): Guarani 1-1 Santos (1967-12-03)
- só na RSSSF (não achado no ogol): Palmeiras 0-0 São Paulo (1967-12-03)
- só na RSSSF (não achado no ogol): Portuguesa 3-2 Comercial-RP (1967-12-09)
- só na RSSSF (não achado no ogol): Botafogo-SP 0-0 São Bento (1967-12-10)
- só na RSSSF (não achado no ogol): Juventus-SP 1-0 América-SP (1967-12-10)
- só na RSSSF (não achado no ogol): Guarani 0-2 São Paulo (1967-12-10)
- só na RSSSF (não achado no ogol): Santos 2-1 Corinthians (1967-12-10)
- só na RSSSF (não achado no ogol): Palmeiras 2-0 Prudentina (1967-12-10)
- só na RSSSF (não achado no ogol): Juventus-SP 1-2 Palmeiras (1967-12-17)
- só na RSSSF (não achado no ogol): Portuguesa Santista 1-3 Santos (1967-12-17)
- só na RSSSF (não achado no ogol): Prudentina 5-1 Portuguesa (1967-12-17)
- só na RSSSF (não achado no ogol): Comercial-RP 2-1 Guarani (1967-12-17)
- só na RSSSF (não achado no ogol): São Bento 0-1 Ferroviária-SP (1967-12-17)
- só na RSSSF (não achado no ogol): Corinthians 1-1 São Paulo (1967-12-17)
- só na RSSSF (não achado no ogol): Juventus-SP 1-0 Portuguesa Santista (1967-12-19)
- só na RSSSF (não achado no ogol): Santos 2-1 São Paulo (1967-12-21)

### 1968

- tabela publicada x jogos — 2º Turno / -: Ferroviária-SP tabela [26, 11, 8, 7, 42, 31] jogos [26, 11, 8, 7, 42, 32] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Guarani tabela [26, 8, 6, 12, 28, 29] jogos [26, 8, 7, 11, 29, 29] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Palmeiras tabela [26, 8, 5, 13, 34, 43] jogos [26, 7, 6, 13, 34, 43] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar corrigido pelo ogol — Juventus-SP x XV de Piracicaba (1968-05-18): RSSSF 0-2, ogol 2-0; fica o do ogol, que fecha com a tabela publicada
- placar corrigido pelo ogol — Comercial-RP x Portuguesa (1968-06-02): RSSSF 0-1, ogol 0-0; fica o do ogol, que fecha com a tabela publicada

### 1969

- tabela publicada x jogos — 2º Turno / Grupo A: Santos tabela [26, 17, 3, 6, 60, 30] jogos [26, 17, 3, 6, 59, 30] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo A: Ferroviária-SP tabela [26, 10, 6, 10, 29, 35] jogos [26, 10, 7, 9, 29, 35] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo A: XV de Piracicaba tabela [26, 5, 11, 10, 30, 41] jogos [26, 6, 11, 9, 30, 39] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo B: América-SP tabela [26, 8, 7, 11, 29, 45] jogos [26, 8, 7, 11, 30, 45] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo B: Botafogo-SP tabela [26, 6, 7, 13, 25, 41] jogos [26, 5, 7, 14, 25, 42] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo B: São Bento tabela [26, 6, 7, 13, 26, 45] jogos [26, 5, 8, 13, 29, 49] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo B: Paulista tabela [26, 7, 4, 15, 25, 40] jogos [26, 7, 4, 15, 26, 42] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — Corinthians x Santos (1969-05-25): RSSSF 1-3, ogol 1-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Santos x América-SP, ogol 1969-03-19); fica a do ogol
- só na RSSSF (não achado no ogol): Corinthians 2-2 Portuguesa (1969-06-08)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Santos

### 1970

- tabela publicada x jogos — 2º Turno / -: São Bento tabela [18, 3, 5, 10, 15, 26] jogos [18, 2, 6, 10, 15, 26] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Botafogo-SP tabela [18, 2, 4, 12, 14, 33] jogos [18, 2, 5, 11, 14, 33] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1971

- sem ocorrências

### 1972

- sem ocorrências

### 1973

- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Portuguesa

### 1974

- tabela publicada x jogos — 1º Turno / -: Corinthians tabela [13, 8, 3, 2, 18, 7] jogos [13, 8, 3, 2, 19, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / -: Botafogo-SP tabela [13, 4, 4, 5, 15, 16] jogos [13, 4, 4, 5, 15, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Palmeiras tabela [13, 8, 5, 0, 24, 7] jogos [13, 9, 4, 0, 24, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Santos tabela [13, 5, 8, 0, 17, 11] jogos [13, 7, 4, 2, 17, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Juventus-SP tabela [13, 4, 5, 4, 13, 13] jogos [13, 3, 7, 3, 13, 13] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Corinthians tabela [13, 5, 3, 5, 9, 14] jogos [13, 5, 2, 6, 9, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: São Bento tabela [13, 2, 4, 7, 8, 21] jogos [13, 3, 2, 8, 9, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1975

- tabela publicada x jogos — 1º Turno / -: Portuguesa tabela [18, 11, 3, 4, 26, 16] jogos [18, 11, 3, 4, 26, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / -: Marília tabela [18, 7, 6, 5, 27, 28] jogos [18, 7, 6, 5, 27, 27] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / -: Ponte Preta tabela [18, 5, 7, 6, 22, 17] jogos [18, 5, 7, 6, 21, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / -: América-SP tabela [18, 6, 2, 10, 17, 24] jogos [18, 6, 2, 10, 16, 24] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno - 1ª fase / Grupo A: Comercial-RP tabela [9, 3, 2, 4, 8, 11] jogos [9, 3, 2, 4, 7, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno - 1ª fase / Grupo A: São Bento tabela [9, 0, 5, 4, 5, 15] jogos [9, 1, 4, 4, 6, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno - 1ª fase / Grupo A: Marília tabela [9, 1, 1, 7, 4, 15] jogos [9, 1, 1, 7, 4, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno - 1ª fase / Grupo A: Botafogo-SP tabela [9, 0, 2, 7, 6, 13] jogos [9, 0, 2, 7, 6, 21] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno - 1ª fase / Grupo B: América-SP tabela [10, 6, 1, 3, 14, 6] jogos [10, 6, 1, 3, 15, 6] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno - 1ª fase / Grupo B: XV de Piracicaba tabela [10, 3, 5, 2, 10, 9] jogos [10, 3, 5, 2, 9, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno - 1ª fase / Grupo B: Juventus-SP tabela [10, 4, 3, 3, 10, 9] jogos [10, 4, 2, 4, 10, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, São Paulo

### 1976

- jogo só no ogol, incluído em Primeiro Turno: América-SP 2-0 Ferroviária-SP (1976-02-22)
- jogo só no ogol, incluído em Segundo Turno: Corinthians 1-0 São Bento (1976-07-11)

### 1977

- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Corinthians x Ponte Preta na Final sempre na mesma ordem) — ogol Ponte Preta 0-1 Corinthians (1977-10-06)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Santos x Corinthians, ogol 1977-06-21); fica a do ogol
- só na RSSSF (não achado no ogol): Palmeiras None-None Botafogo-SP (1977-10-02)

### 1978

- tabela publicada x jogos — Primeira fase / Grupo C: Corinthians tabela [19, 9, 8, 2, 24, 17] jogos [19, 9, 9, 1, 24, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo D: Palmeiras tabela [19, 9, 6, 4, 26, 15] jogos [19, 8, 7, 4, 24, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo A: Guarani tabela [19, 7, 8, 4, 24, 16] jogos [5, 5, 0, 0, 11, 2] — a tabela conta 19 jogos e as fontes trazem 5
- tabela publicada x jogos — Primeira fase / Grupo A: Juventus-SP tabela [19, 8, 5, 6, 33, 27] jogos [5, 1, 2, 2, 9, 10] — a tabela conta 19 jogos e as fontes trazem 5
- tabela publicada x jogos — Primeira fase / Grupo A: Portuguesa Santista tabela [19, 8, 5, 6, 13, 14] jogos [5, 0, 1, 4, 3, 14] — a tabela conta 19 jogos e as fontes trazem 5
- tabela publicada x jogos — Primeira fase / Grupo A: Palmeiras tabela [19, 8, 4, 7, 23, 18] jogos [5, 3, 1, 1, 12, 5] — a tabela conta 19 jogos e as fontes trazem 5
- tabela publicada x jogos — Primeira fase / Grupo A: Paulista tabela [19, 3, 8, 8, 10, 20] jogos [6, 1, 2, 3, 4, 8] — a tabela conta 19 jogos e as fontes trazem 6
- tabela publicada x jogos — Primeira fase / Grupo B: Corinthians tabela [19, 7, 8, 4, 25, 20] jogos [6, 2, 4, 0, 5, 3] — a tabela conta 19 jogos e as fontes trazem 6
- tabela publicada x jogos — Primeira fase / Grupo B: Botafogo-SP tabela [19, 7, 8, 4, 23, 19] jogos [6, 2, 2, 2, 5, 6] — a tabela conta 19 jogos e as fontes trazem 6
- tabela publicada x jogos — Primeira fase / Grupo B: Comercial-RP tabela [19, 5, 7, 7, 10, 19] jogos [6, 3, 2, 1, 8, 5] — a tabela conta 19 jogos e as fontes trazem 6
- tabela publicada x jogos — Primeira fase / Grupo B: Noroeste tabela [19, 4, 7, 8, 13, 22] jogos [5, 0, 2, 3, 1, 6] — a tabela conta 19 jogos e as fontes trazem 5
- tabela publicada x jogos — Primeira fase / Grupo B: América-SP tabela [19, 3, 9, 7, 19, 29] jogos [7, 2, 2, 3, 6, 5] — a tabela conta 19 jogos e as fontes trazem 7
- tabela publicada x jogos — Primeira fase / Grupo C: Ponte Preta tabela [19, 12, 5, 2, 39, 16] jogos [5, 1, 3, 1, 3, 3] — a tabela conta 19 jogos e as fontes trazem 5
- tabela publicada x jogos — Primeira fase / Grupo C: Francana tabela [19, 5, 9, 5, 22, 27] jogos [5, 3, 2, 0, 11, 4] — a tabela conta 19 jogos e as fontes trazem 5
- tabela publicada x jogos — Primeira fase / Grupo C: São Paulo tabela [19, 6, 4, 9, 24, 27] jogos [6, 4, 1, 1, 7, 4] — a tabela conta 19 jogos e as fontes trazem 6
- tabela publicada x jogos — Primeira fase / Grupo C: Marília tabela [19, 4, 8, 7, 22, 27] jogos [5, 0, 0, 5, 4, 12] — a tabela conta 19 jogos e as fontes trazem 5
- tabela publicada x jogos — Primeira fase / Grupo C: São Bento tabela [19, 5, 4, 10, 23, 30] jogos [5, 1, 2, 2, 5, 7] — a tabela conta 19 jogos e as fontes trazem 5
- tabela publicada x jogos — Primeira fase / Grupo D: Santos tabela [19, 10, 4, 5, 25, 15] jogos [4, 2, 2, 0, 10, 4] — a tabela conta 19 jogos e as fontes trazem 4
- tabela publicada x jogos — Primeira fase / Grupo D: Ferroviária-SP tabela [19, 7, 8, 4, 18, 14] jogos [5, 2, 1, 2, 7, 8] — a tabela conta 19 jogos e as fontes trazem 5
- tabela publicada x jogos — Primeira fase / Grupo D: XV de Piracicaba tabela [19, 6, 8, 5, 16, 16] jogos [6, 2, 3, 1, 6, 5] — a tabela conta 19 jogos e as fontes trazem 6
- tabela publicada x jogos — Primeira fase / Grupo D: XV de Jaú tabela [19, 6, 4, 9, 18, 19] jogos [5, 2, 2, 1, 8, 7] — a tabela conta 19 jogos e as fontes trazem 5
- tabela publicada x jogos — Primeira fase / Grupo D: Portuguesa tabela [19, 5, 5, 9, 19, 24] jogos [6, 0, 2, 4, 5, 12] — a tabela conta 19 jogos e as fontes trazem 6
- tabela publicada x jogos — 3º Turno / Grupo A: Guarani tabela [9, 5, 3, 1, 19, 7] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / Grupo A: São Paulo tabela [9, 4, 5, 0, 14, 6] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / Grupo A: Corinthians tabela [9, 5, 2, 2, 16, 11] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / Grupo A: Francana tabela [9, 1, 3, 5, 9, 14] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / Grupo A: Botafogo-SP tabela [9, 1, 0, 8, 7, 24] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / Grupo B: Palmeiras tabela [9, 6, 2, 1, 17, 6] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / Grupo B: Santos tabela [9, 5, 0, 4, 18, 9] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / Grupo B: Ponte Preta tabela [9, 4, 2, 3, 11, 10] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / Grupo B: Juventus-SP tabela [9, 3, 3, 3, 11, 16] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — 3º Turno / Grupo B: Portuguesa tabela [9, 0, 2, 7, 3, 22] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- placar diferente no ogol — Corinthians x Guarani (1978-11-19): RSSSF 2-2, ogol 3-2; fica o da RSSSF
- jogo só no ogol, incluído em 1st Phase: Juventus-SP 1-2 Corinthians (1979-01-28)
- jogo só no ogol, incluído em 1st Phase: Santos 4-1 São Paulo (1979-01-28)
- jogo só no ogol, incluído em 1st Phase: São Bento 2-0 Palmeiras (1979-01-28)
- jogo só no ogol, incluído em 1st Phase: Comercial-RP 0-0 Guarani (1979-01-28)
- jogo só no ogol, incluído em 1st Phase: América-SP 0-3 Portuguesa (1979-01-28)
- jogo só no ogol, incluído em 1st Phase: Ponte Preta 3-1 Francana (1979-01-28)
- jogo só no ogol, incluído em 1st Phase: XV de Jaú 1-0 Noroeste (1979-01-28)
- jogo só no ogol, incluído em 1st Phase: Marília 1-1 XV de Piracicaba (1979-01-28)
- jogo só no ogol, incluído em 1st Phase: Paulista 0-1 Botafogo-SP (1979-01-28)
- jogo só no ogol, incluído em 1st Phase: Portuguesa Santista 1-0 Ferroviária-SP (1979-01-28)
- jogo só no ogol, incluído em 1st Phase: São Paulo 3-1 São Bento (1979-01-31)
- jogo só no ogol, incluído em 1st Phase: Guarani 0-0 Marília (1979-01-31)
- jogo só no ogol, incluído em 1st Phase: XV de Piracicaba 1-2 Ponte Preta (1979-01-31)
- jogo só no ogol, incluído em 1st Phase: Francana 1-1 Paulista (1979-01-31)
- jogo só no ogol, incluído em 1st Phase: Portuguesa 2-0 Portuguesa Santista (1979-02-01)
- jogo só no ogol, incluído em 1st Phase: Palmeiras 1-2 Guarani (1979-02-03)
- jogo só no ogol, incluído em 1st Phase: São Paulo 1-2 Portuguesa (1979-02-04)
- jogo só no ogol, incluído em 1st Phase: XV de Jaú 2-3 Francana (1979-02-04)
- jogo só no ogol, incluído em 1st Phase: XV de Piracicaba 1-1 São Bento (1979-02-04)
- jogo só no ogol, incluído em 1st Phase: Marília 1-2 Portuguesa Santista (1979-02-04)
- jogo só no ogol, incluído em 1st Phase: Ponte Preta 0-0 Juventus-SP (1979-02-04)
- jogo só no ogol, incluído em 1st Phase: Paulista 0-2 Corinthians (1979-02-04)
- jogo só no ogol, incluído em 1st Phase: América-SP 1-1 Botafogo-SP (1979-02-04)
- jogo só no ogol, incluído em 1st Phase: Noroeste 0-0 Ferroviária-SP (1979-02-04)
- jogo só no ogol, incluído em 1st Phase: Comercial-RP 0-1 Santos (1979-02-04)
- jogo só no ogol, incluído em 1st Phase: Francana 0-0 Juventus-SP (1979-02-07)
- jogo só no ogol, incluído em 1st Phase: Corinthians 2-2 XV de Piracicaba (1979-02-07)
- jogo só no ogol, incluído em 1st Phase: Portuguesa Santista 0-0 Palmeiras (1979-02-07)
- jogo só no ogol, incluído em 1st Phase: XV de Jaú 3-1 São Paulo (1979-02-07)
- jogo só no ogol, incluído em 1st Phase: São Bento 1-2 América-SP (1979-02-07)
- jogo só no ogol, incluído em 1st Phase: Portuguesa 1-1 Botafogo-SP (1979-02-08)
- jogo só no ogol, incluído em 1st Phase: Palmeiras 2-1 América-SP (1979-02-10)
- jogo só no ogol, incluído em 1st Phase: Juventus-SP 1-3 Paulista (1979-02-11)
- jogo só no ogol, incluído em 1st Phase: Corinthians 2-1 Santos (1979-02-11)
- jogo só no ogol, incluído em 1st Phase: Botafogo-SP 1-2 Ponte Preta (1979-02-11)
- jogo só no ogol, incluído em 1st Phase: Guarani 4-0 Portuguesa (1979-02-11)
- jogo só no ogol, incluído em 1st Phase: São Bento 1-2 Marília (1979-02-11)
- jogo só no ogol, incluído em 1st Phase: Francana 1-0 São Paulo (1979-02-11)
- jogo só no ogol, incluído em 1st Phase: XV de Piracicaba 0-0 Comercial-RP (1979-02-11)
- jogo só no ogol, incluído em 1st Phase: Portuguesa Santista 0-0 Noroeste (1979-02-11)
- jogo só no ogol, incluído em 1st Phase: Ferroviária-SP 1-0 XV de Jaú (1979-02-11)
- jogo só no ogol, incluído em 1st Phase: Marília 3-0 Portuguesa (1979-02-14)
- jogo só no ogol, incluído em 1st Phase: Palmeiras 5-1 Juventus-SP (1979-02-14)
- jogo só no ogol, incluído em 1st Phase: Botafogo-SP 3-0 São Bento (1979-02-14)
- jogo só no ogol, incluído em 1st Phase: Santos 1-0 XV de Piracicaba (1979-02-14)
- jogo só no ogol, incluído em 1st Phase: Ponte Preta 4-0 Comercial-RP (1979-02-14)
- jogo só no ogol, incluído em 1st Phase: Ferroviária-SP 2-2 América-SP (1979-02-14)
- jogo só no ogol, incluído em 1st Phase: Francana 2-2 Guarani (1979-02-14)
- jogo só no ogol, incluído em 1st Phase: São Paulo 3-0 Paulista (1979-02-15)
- jogo só no ogol, incluído em 1st Phase: Portuguesa 1-2 Ponte Preta (1979-02-17)
- jogo só no ogol, incluído em 1st Phase: Santos 1-0 XV de Jaú (1979-02-17)
- jogo só no ogol, incluído em 1st Phase: Juventus-SP 4-0 Noroeste (1979-02-18)
- jogo só no ogol, incluído em 1st Phase: Palmeiras 0-0 Corinthians (1979-02-18)
- jogo só no ogol, incluído em 1st Phase: América-SP 1-1 São Paulo (1979-02-18)
- jogo só no ogol, incluído em 1st Phase: Guarani 0-0 Ferroviária-SP (1979-02-18)
- jogo só no ogol, incluído em 1st Phase: São Bento 5-0 Comercial-RP (1979-02-18)
- jogo só no ogol, incluído em 1st Phase: Portuguesa Santista 2-0 Paulista (1979-02-18)
- jogo só no ogol, incluído em 1st Phase: Botafogo-SP 2-0 XV de Piracicaba (1979-02-18)
- jogo só no ogol, incluído em 1st Phase: Marília 2-1 Francana (1979-02-18)
- jogo só no ogol, incluído em 1st Phase: Juventus-SP 2-1 Guarani (1979-02-21)
- jogo só no ogol, incluído em 1st Phase: Noroeste 0-0 Santos (1979-02-21)
- jogo só no ogol, incluído em 1st Phase: São Paulo 0-2 Juventus-SP (1979-02-24)
- jogo só no ogol, incluído em 1st Phase: Noroeste 1-1 Corinthians (1979-02-24)
- jogo só no ogol, incluído em 1st Phase: Botafogo-SP 1-0 Palmeiras (1979-02-24)
- jogo só no ogol, incluído em 1st Phase: Guarani 2-2 XV de Piracicaba (1979-02-24)
- jogo só no ogol, incluído em 1st Phase: Portuguesa 1-1 Francana (1979-02-24)
- jogo só no ogol, incluído em 1st Phase: Marília 4-4 Ponte Preta (1979-02-24)
- jogo só no ogol, incluído em 1st Phase: Paulista 0-0 Santos (1979-02-24)
- jogo só no ogol, incluído em 1st Phase: América-SP 0-1 Portuguesa Santista (1979-02-24)
- jogo só no ogol, incluído em 1st Phase: São Bento 1-1 Ferroviária-SP (1979-02-24)
- jogo só no ogol, incluído em 1st Phase: XV de Jaú 2-0 Comercial-RP (1979-02-24)
- jogo só no ogol, incluído em 1st Phase: São Paulo 3-0 Guarani (1979-03-03)
- jogo só no ogol, incluído em 1st Phase: Juventus-SP 1-1 Portuguesa (1979-03-04)
- jogo só no ogol, incluído em 1st Phase: Santos 1-2 Palmeiras (1979-03-04)
- jogo só no ogol, incluído em 1st Phase: América-SP 1-1 Marília (1979-03-04)
- jogo só no ogol, incluído em 1st Phase: Francana 0-0 Noroeste (1979-03-04)
- jogo só no ogol, incluído em 1st Phase: Comercial-RP 1-1 Corinthians (1979-03-04)
- jogo só no ogol, incluído em 1st Phase: Ferroviária-SP 2-2 Botafogo-SP (1979-03-04)
- jogo só no ogol, incluído em 1st Phase: Ponte Preta 5-2 São Bento (1979-03-04)
- jogo só no ogol, incluído em 1st Phase: Paulista 2-2 XV de Jaú (1979-03-04)
- jogo só no ogol, incluído em 1st Phase: XV de Piracicaba 0-0 Portuguesa Santista (1979-03-04)
- jogo só no ogol, incluído em 1st Phase: São Bento 2-0 Santos (1979-03-07)
- jogo só no ogol, incluído em 1st Phase: Portuguesa 1-1 XV de Jaú (1979-03-08)
- jogo só no ogol, incluído em 1st Phase: Corinthians 2-1 São Bento (1979-03-10)
- jogo só no ogol, incluído em 1st Phase: Portuguesa 2-3 Santos (1979-03-11)
- jogo só no ogol, incluído em 1st Phase: XV de Jaú 3-2 Juventus-SP (1979-03-11)
- jogo só no ogol, incluído em 1st Phase: XV de Piracicaba 1-0 São Paulo (1979-03-11)
- jogo só no ogol, incluído em 1st Phase: Comercial-RP 0-0 Paulista (1979-03-11)
- jogo só no ogol, incluído em 1st Phase: América-SP 3-3 Francana (1979-03-11)
- jogo só no ogol, incluído em 1st Phase: Ferroviária-SP 1-0 Marília (1979-03-11)
- jogo só no ogol, incluído em 1st Phase: Noroeste 1-1 Botafogo-SP (1979-03-11)
- jogo só no ogol, incluído em 1st Phase: Portuguesa Santista 2-0 Guarani (1979-03-11)
- jogo só no ogol, incluído em 1st Phase: São Paulo 2-1 Noroeste (1979-03-14)
- jogo só no ogol, incluído em 1st Phase: Santos 4-0 América-SP (1979-03-14)
- jogo só no ogol, incluído em 1st Phase: Ponte Preta 3-0 Portuguesa Santista (1979-03-14)
- jogo só no ogol, incluído em 1st Phase: Botafogo-SP 1-0 Marília (1979-03-14)
- jogo só no ogol, incluído em 1st Phase: São Paulo 0-3 Comercial-RP (1979-03-17)
- jogo só no ogol, incluído em 1st Phase: Corinthians 2-0 Portuguesa (1979-03-18)
- jogo só no ogol, incluído em 1st Phase: XV de Jaú 0-1 São Bento (1979-03-18)
- jogo só no ogol, incluído em 1st Phase: Botafogo-SP 3-3 Juventus-SP (1979-03-18)
- jogo só no ogol, incluído em 1st Phase: Marília 0-0 Palmeiras (1979-03-18)
- jogo só no ogol, incluído em 1st Phase: Portuguesa Santista 0-1 Francana (1979-03-18)
- jogo só no ogol, incluído em 1st Phase: XV de Piracicaba 1-1 América-SP (1979-03-18)
- jogo só no ogol, incluído em 1st Phase: Ferroviária-SP 0-2 Ponte Preta (1979-03-18)
- jogo só no ogol, incluído em 1st Phase: Guarani 0-1 Santos (1979-03-18)
- jogo só no ogol, incluído em 1st Phase: Corinthians 0-0 Ponte Preta (1979-03-21)
- jogo só no ogol, incluído em 1st Phase: Paulista 0-0 Ferroviária-SP (1979-03-21)
- jogo só no ogol, incluído em 1st Phase: Comercial-RP 0-2 Noroeste (1979-03-21)
- jogo só no ogol, incluído em 1st Phase: Juventus-SP 3-2 Marília (1979-03-24)
- jogo só no ogol, incluído em 1st Phase: Francana 0-4 Corinthians (1979-03-25)
- jogo só no ogol, incluído em 1st Phase: Ponte Preta 1-0 Paulista (1979-03-25)
- jogo só no ogol, incluído em 1st Phase: Portuguesa Santista 0-3 São Paulo (1979-03-25)
- jogo só no ogol, incluído em 1st Phase: Comercial-RP 0-0 Portuguesa (1979-03-25)
- jogo só no ogol, incluído em 1st Phase: Santos 3-0 Botafogo-SP (1979-03-25)
- jogo só no ogol, incluído em 1st Phase: América-SP 2-0 XV de Jaú (1979-03-25)
- jogo só no ogol, incluído em 1st Phase: Ferroviária-SP 2-0 XV de Piracicaba (1979-03-25)
- jogo só no ogol, incluído em 1st Phase: São Bento 0-0 Guarani (1979-03-28)
- jogo só no ogol, incluído em 1st Phase: Corinthians 2-1 Portuguesa Santista (1979-03-28)
- jogo só no ogol, incluído em 1st Phase: Botafogo-SP 1-0 XV de Jaú (1979-03-28)
- jogo só no ogol, incluído em 1st Phase: Ferroviária-SP 0-0 Santos (1979-03-28)
- jogo só no ogol, incluído em 1st Phase: Marília 0-1 Comercial-RP (1979-03-28)
- jogo só no ogol, incluído em 1st Phase: Ponte Preta 3-0 Palmeiras (1979-03-28)
- jogo só no ogol, incluído em 1st Phase: Portuguesa 3-0 São Bento (1979-03-31)
- jogo só no ogol, incluído em 1st Phase: Palmeiras 2-0 São Paulo (1979-04-01)
- jogo só no ogol, incluído em 1st Phase: Guarani 4-0 Corinthians (1979-04-01)
- jogo só no ogol, incluído em 1st Phase: Santos 0-1 Ponte Preta (1979-04-01)
- jogo só no ogol, incluído em 1st Phase: Juventus-SP 3-1 América-SP (1979-04-01)
- jogo só no ogol, incluído em 1st Phase: Comercial-RP 0-1 Ferroviária-SP (1979-04-01)
- jogo só no ogol, incluído em 1st Phase: Noroeste 5-1 Marília (1979-04-01)
- jogo só no ogol, incluído em 1st Phase: Paulista 0-0 XV de Piracicaba (1979-04-01)
- jogo só no ogol, incluído em 1st Phase: Francana 1-1 Botafogo-SP (1979-04-01)
- jogo só no ogol, incluído em 1st Phase: XV de Jaú 0-1 Portuguesa Santista (1979-04-01)
- jogo só no ogol, incluído em 1st Phase: Palmeiras 2-1 Noroeste (1979-04-04)
- jogo só no ogol, incluído em 1st Phase: Ponte Preta 3-0 Ferroviária-SP (1979-04-08)
- jogo só no ogol, incluído em 1st Phase: Santos 2-1 Francana (1979-04-14)
- jogo só no ogol, incluído em 1st Phase: Palmeiras 0-1 Comercial-RP (1979-04-18)
- jogo só no ogol, incluído em 1st Phase: Guarani 2-1 Botafogo-SP (1979-04-19)
- jogo só no ogol, incluído em 1st Phase: Corinthians 0-1 Juventus-SP (1979-04-19)
- jogo só no ogol, incluído em 1st Phase: Santos 1-2 Ponte Preta (1979-04-19)
- jogo só no ogol, incluído em 1st Phase: Juventus-SP 0-2 Guarani (1979-04-25)
- jogo só no ogol, incluído em 1st Phase: Noroeste 1-0 Paulista (1979-04-27)
- jogo só no ogol, incluído em 1st Phase: Corinthians 2-0 Portuguesa (1979-04-29)
- jogo só no ogol, incluído em 1st Phase: São Paulo 0-0 Juventus-SP (1979-04-29)
- jogo só no ogol, incluído em 1st Phase: Ponte Preta 1-0 Francana (1979-04-29)
- jogo só no ogol, incluído em 1st Phase: Portuguesa 0-0 Juventus-SP (1979-05-02)
- jogo só no ogol, incluído em 1st Phase: Palmeiras 3-1 Francana (1979-05-02)
- jogo só no ogol, incluído em 1st Phase: Santos 5-1 Botafogo-SP (1979-05-02)
- jogo só no ogol, incluído em 1st Phase: Guarani 2-0 Ponte Preta (1979-05-03)
- jogo só no ogol, incluído em 1st Phase: São Paulo 2-2 Corinthians (1979-05-05)
- jogo só no ogol, incluído em 1st Phase: Corinthians 3-1 Botafogo-SP (1979-05-05)
- jogo só no ogol, incluído em 1st Phase: Santos 1-0 Francana (1979-05-06)
- jogo só no ogol, incluído em 1st Phase: Ponte Preta 2-0 Portuguesa (1979-05-06)
- jogo só no ogol, incluído em 1st Phase: Juventus-SP 1-4 Palmeiras (1979-05-06)
- jogo só no ogol, incluído em 1st Phase: Palmeiras 0-0 Guarani (1979-05-06)
- jogo só no ogol, incluído em 1st Phase: Santos 2-0 Ponte Preta (1979-05-07)
- jogo só no ogol, incluído em 1st Phase: São Paulo 1-0 Palmeiras (1979-05-09)
- jogo só no ogol, incluído em 1st Phase: Santos 5-1 Portuguesa (1979-05-09)
- jogo só no ogol, incluído em 1st Phase: Ponte Preta 3-0 Botafogo-SP (1979-05-09)
- jogo só no ogol, incluído em 1st Phase: São Paulo 1-1 Guarani (1979-05-09)
- jogo só no ogol, incluído em 1st Phase: Juventus-SP 2-1 Botafogo-SP (1979-05-09)
- jogo só no ogol, incluído em 1st Phase: Guarani 2-1 Francana (1979-05-10)
- jogo só no ogol, incluído em 1st Phase: Corinthians 2-3 Juventus-SP (1979-05-10)
- jogo só no ogol, incluído em 1st Phase: Francana 0-0 Portuguesa (1979-05-10)
- jogo só no ogol, incluído em 1st Phase: Palmeiras 1-1 Ponte Preta (1979-05-10)
- jogo só no ogol, incluído em 1st Phase: Santos 0-1 Corinthians (1979-05-10)
- jogo só no ogol, incluído em 1st Phase: São Paulo 2-1 Santos (1979-05-12)
- jogo só no ogol, incluído em 1st Phase: Corinthians 3-1 Ponte Preta (1979-05-13)
- jogo só no ogol, incluído em 1st Phase: Francana 2-1 Botafogo-SP (1979-05-13)
- jogo só no ogol, incluído em 1st Phase: Palmeiras 4-1 Portuguesa (1979-05-13)
- jogo só no ogol, incluído em 1st Phase: Guarani 5-1 Juventus-SP (1979-05-13)
- jogo só no ogol, incluído em 1st Phase: São Paulo 2-0 Botafogo-SP (1979-05-13)
- jogo só no ogol, incluído em 1st Phase: Juventus-SP 1-2 Ponte Preta (1979-05-13)
- jogo só no ogol, incluído em 1st Phase: Corinthians 0-0 Guarani (1979-05-14)
- jogo só no ogol, incluído em 1st Phase: Juventus-SP 2-2 Francana (1979-05-16)
- jogo só no ogol, incluído em 1st Phase: Guarani 3-0 Portuguesa (1979-05-16)
- jogo só no ogol, incluído em 1st Phase: Palmeiras 1-0 Botafogo-SP (1979-05-16)
- jogo só no ogol, incluído em 1st Phase: Santos 3-1 Guarani (1979-05-16)
- jogo só no ogol, incluído em 1st Phase: Palmeiras 0-1 São Paulo (1979-05-17)
- jogo só no ogol, incluído em 1st Phase: São Paulo 1-1 Ponte Preta (1979-05-19)
- jogo só no ogol, incluído em 1st Phase: Corinthians 0-2 Palmeiras (1979-05-20)
- jogo só no ogol, incluído em 1st Phase: Santos 0-1 Juventus-SP (1979-05-20)
- jogo só no ogol, incluído em 1st Phase: Botafogo-SP 2-1 Portuguesa (1979-05-20)
- jogo só no ogol, incluído em 1st Phase: São Paulo 1-2 Santos (1979-05-20)
- jogo só no ogol, incluído em 1st Phase: Portuguesa 0-4 São Paulo (1979-05-26)
- jogo só no ogol, incluído em 1st Phase: Ponte Preta 1-1 Guarani (1979-05-27)
- jogo só no ogol, incluído em 1st Phase: Corinthians 3-2 Francana (1979-05-27)
- jogo só no ogol, incluído em 1st Phase: Palmeiras 2-1 Santos (1979-05-27)
- jogo só no ogol, incluído em 1st Phase: Guarani 5-1 Botafogo-SP (1979-05-27)
- jogo só no ogol, incluído em 1st Phase: São Paulo 1-1 Francana (1979-05-30)
- jogo só no ogol, incluído em 1st Phase: Santos 3-1 Guarani (1979-05-30)
- jogo só no ogol, incluído em 1st Phase: Santos 1-1 São Paulo (1979-06-24)
- jogo só no ogol, incluído em 1st Phase: Santos 0-2 São Paulo (1979-06-28)
- vencedor da final pelos jogos (Corinthians) diferente do campeão oficial (Santos); fica o oficial

### 1979

- a repescagem Marília x Santo André vem na página depois da final (fevereiro de 1980) só com dia e mês ("[Dec 5]"); ficou dezembro de 1980 pela ordem da página, mas pode ser dezembro de 1979 (o ogol não tem esses jogos)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Santo André
- Santo André — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Santo André)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de Corinthians x Ponte Preta na FINAL sempre na mesma ordem) — ogol Ponte Preta 0-1 Corinthians (1980-02-03)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Ponte Preta x Guarani, ogol 1979-11-22); fica a do ogol
- ano errado na data da RSSSF — Botafogo-SP 0-0 São Paulo: RSSSF 1978-08-19, ogol 1979-08-19; fica a do ogol
- ano errado na data da RSSSF — Corinthians 1-3 Palmeiras: RSSSF 1978-08-19, ogol 1979-08-19; fica a do ogol
- só na RSSSF (não achado no ogol): Marília 2-0 Santo André (1980-12-05)
- só na RSSSF (não achado no ogol): Santo André 2-1 Marília (1980-12-08)
- só na RSSSF (não achado no ogol): Marília 4-1 Santo André (1980-12-12)

### 1980

- tabela publicada x jogos — 2º Turno / -: São Paulo tabela [19, 11, 7, 1, 26, 9] jogos [25, 15, 7, 3, 33, 14] — a tabela conta 19 jogos e as fontes trazem 25
- tabela publicada x jogos — 2º Turno / -: Ponte Preta tabela [19, 9, 9, 1, 27, 12] jogos [23, 11, 10, 2, 33, 15] — a tabela conta 19 jogos e as fontes trazem 23
- tabela publicada x jogos — 2º Turno / -: Corinthians tabela [19, 11, 4, 4, 30, 18] jogos [21, 11, 5, 5, 31, 22] — a tabela conta 19 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Inter de Limeira tabela [19, 9, 8, 2, 30, 17] jogos [21, 10, 8, 3, 33, 20] — a tabela conta 19 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Santos tabela [19, 6, 9, 4, 19, 19] jogos [21, 6, 9, 6, 19, 21] — a tabela conta 19 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Ponte Preta tabela [38, 17, 16, 5, 57, 32] jogos [44, 19, 18, 7, 63, 37] — a tabela conta 38 jogos e as fontes trazem 44
- tabela publicada x jogos — 2º Turno / -: São Paulo tabela [38, 18, 13, 7, 47, 27] jogos [44, 22, 13, 9, 54, 32] — a tabela conta 38 jogos e as fontes trazem 44
- tabela publicada x jogos — 2º Turno / -: Corinthians tabela [38, 18, 12, 8, 48, 30] jogos [40, 18, 13, 9, 49, 34] — a tabela conta 38 jogos e as fontes trazem 40
- tabela publicada x jogos — 2º Turno / -: Santos tabela [38, 16, 16, 6, 48, 32] jogos [44, 20, 16, 8, 58, 36] — a tabela conta 38 jogos e as fontes trazem 44
- tabela publicada x jogos — 2º Turno / -: Portuguesa tabela [38, 18, 10, 10, 48, 43] jogos [42, 19, 11, 12, 51, 46] — a tabela conta 38 jogos e as fontes trazem 42
- tabela publicada x jogos — 2º Turno / -: Inter de Limeira tabela [38, 14, 17, 7, 56, 41] jogos [40, 15, 17, 8, 59, 44] — a tabela conta 38 jogos e as fontes trazem 40
- tabela publicada x jogos — 2º Turno / -: Botafogo-SP tabela [38, 16, 10, 12, 55, 33] jogos [40, 16, 10, 14, 56, 40] — a tabela conta 38 jogos e as fontes trazem 40
- tabela publicada x jogos — 2º Turno / -: Juventus-SP tabela [38, 13, 11, 14, 38, 44] jogos [38, 14, 11, 13, 39, 43] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: São Bento tabela [38, 12, 13, 13, 33, 36] jogos [38, 11, 13, 14, 32, 37] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de São Paulo x Ponte Preta na 2º Turno - FINAL sempre na mesma ordem) — ogol Ponte Preta 1-2 São Paulo (1980-11-09)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de São Paulo x Santos na 2º Turno - FINAL sempre na mesma ordem) — ogol Santos 0-1 São Paulo (1980-11-16)
- placar diferente no ogol — Inter de Limeira x São Paulo (1980-11-05): RSSSF 1-2, ogol 1-3; fica o da RSSSF

### 1981

- tabela publicada x jogos — 1º Turno - Classificatória / Grupo Dourado: São Bento tabela [10, 7, 1, 2, 19, 15] jogos [10, 7, 1, 2, 20, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno - Classificatória / Grupo Dourado: Taubaté tabela [10, 1, 3, 6, 14, 19] jogos [10, 1, 3, 6, 14, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno - Classificatória / Grupo Vermelho: Comercial-RP tabela [10, 5, 3, 2, 16, 8] jogos [10, 6, 2, 2, 17, 8] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno - Classificatória / Grupo Vermelho: Francana tabela [10, 2, 5, 3, 10, 10] jogos [10, 2, 4, 4, 10, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / -: Ponte Preta tabela [19, 11, 7, 1, 29, 13] jogos [27, 15, 11, 1, 42, 18] — a tabela conta 19 jogos e as fontes trazem 27
- tabela publicada x jogos — 1º Turno / -: Guarani tabela [19, 9, 7, 3, 36, 23] jogos [27, 13, 10, 4, 49, 29] — a tabela conta 19 jogos e as fontes trazem 27
- tabela publicada x jogos — 1º Turno / -: Inter de Limeira tabela [19, 10, 4, 5, 31, 21] jogos [25, 10, 7, 8, 35, 30] — a tabela conta 19 jogos e as fontes trazem 25
- tabela publicada x jogos — 1º Turno / -: Botafogo-SP tabela [19, 9, 4, 6, 16, 15] jogos [25, 10, 7, 8, 18, 19] — a tabela conta 19 jogos e as fontes trazem 25
- tabela publicada x jogos — 1º Turno / -: Portuguesa tabela [19, 8, 6, 5, 19, 16] jogos [25, 10, 7, 8, 25, 24] — a tabela conta 19 jogos e as fontes trazem 25
- tabela publicada x jogos — 1º Turno / -: Santos tabela [19, 9, 3, 7, 26, 20] jogos [25, 10, 4, 11, 30, 30] — a tabela conta 19 jogos e as fontes trazem 25
- tabela publicada x jogos — 1º Turno / -: XV de Jaú tabela [19, 7, 7, 5, 20, 16] jogos [19, 7, 7, 5, 19, 15] — placar diverge entre RSSSF e ogol em XV de Jaú x São Paulo (0-0 x 1-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 1º Turno / -: Juventus-SP tabela [19, 7, 6, 6, 17, 11] jogos [19, 6, 8, 5, 17, 11] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 1º Turno / -: São Paulo tabela [19, 7, 5, 7, 20, 14] jogos [19, 7, 5, 7, 19, 13] — placar diverge entre RSSSF e ogol em XV de Jaú x São Paulo (0-0 x 1-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 1º Turno / -: América-SP tabela [19, 5, 9, 5, 11, 14] jogos [25, 7, 12, 6, 15, 17] — a tabela conta 19 jogos e as fontes trazem 25
- tabela publicada x jogos — 1º Turno / -: Comercial-RP tabela [19, 5, 7, 7, 15, 26] jogos [25, 7, 9, 9, 21, 33] — a tabela conta 19 jogos e as fontes trazem 25
- tabela publicada x jogos — 1º Turno / -: Noroeste tabela [19, 4, 4, 11, 10, 22] jogos [19, 3, 6, 10, 10, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: São Paulo tabela [2, 1, 1, 0, 2, 1] jogos [4, 2, 2, 0, 5, 2] — a tabela conta 2 jogos e as fontes trazem 4
- tabela publicada x jogos — 2º Turno / -: São Paulo tabela [19, 11, 3, 5, 36, 18] jogos [27, 15, 5, 7, 45, 24] — a tabela conta 19 jogos e as fontes trazem 27
- tabela publicada x jogos — 2º Turno / -: Guarani tabela [19, 9, 6, 4, 34, 23] jogos [25, 11, 10, 4, 43, 28] — a tabela conta 19 jogos e as fontes trazem 25
- tabela publicada x jogos — 2º Turno / -: São José-SP tabela [19, 8, 6, 5, 19, 18] jogos [27, 11, 9, 7, 28, 25] — a tabela conta 19 jogos e as fontes trazem 27
- tabela publicada x jogos — 2º Turno / -: Ponte Preta tabela [19, 7, 8, 4, 31, 20] jogos [25, 8, 11, 6, 34, 24] — a tabela conta 19 jogos e as fontes trazem 25
- tabela publicada x jogos — 2º Turno / -: XV de Jaú tabela [19, 7, 8, 4, 24, 17] jogos [25, 7, 9, 9, 25, 28] — a tabela conta 19 jogos e as fontes trazem 25
- tabela publicada x jogos — 2º Turno / -: Santos tabela [19, 7, 8, 4, 21, 15] jogos [25, 8, 11, 6, 28, 23] — a tabela conta 19 jogos e as fontes trazem 25
- tabela publicada x jogos — 2º Turno / -: Palmeiras tabela [19, 6, 8, 5, 20, 24] jogos [25, 8, 11, 6, 25, 28] — a tabela conta 19 jogos e as fontes trazem 25
- tabela publicada x jogos — 2º Turno / -: Corinthians tabela [19, 6, 7, 6, 23, 23] jogos [25, 7, 11, 7, 28, 29] — a tabela conta 19 jogos e as fontes trazem 25
- tabela publicada x jogos — 2º Turno / -: Ferroviária-SP tabela [19, 6, 7, 6, 22, 26] jogos [19, 6, 8, 5, 23, 26] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: São Bento tabela [19, 4, 10, 5, 14, 19] jogos [19, 4, 10, 5, 14, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo Preto: São José-SP tabela [6, 2, 3, 1, 5, 3] jogos [6, 2, 3, 1, 6, 4] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo Preto: Ponte Preta tabela [6, 1, 3, 2, 2, 4] jogos [6, 1, 3, 2, 3, 5] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): XV de Novembro
- XV de Novembro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (XV de Piracicaba)
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de São Paulo x Ponte Preta na Final sempre na mesma ordem) — ogol Ponte Preta 1-1 São Paulo (1981-11-25)
- placar diferente no ogol — XV de Jaú x São Paulo (1981-06-18): RSSSF 0-0, ogol 1-1; fica o da RSSSF
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, São Paulo

### 1982

- tabela publicada x jogos — 2º Turno / -: São Paulo tabela [19, 14, 3, 2, 38, 14] jogos [21, 14, 3, 4, 39, 18] — a tabela conta 19 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Corinthians tabela [19, 12, 3, 4, 41, 21] jogos [21, 14, 3, 4, 45, 22] — a tabela conta 19 jogos e as fontes trazem 21
- tabela publicada x jogos — 2º Turno / -: Juventus-SP tabela [19, 7, 5, 7, 20, 23] jogos [19, 7, 5, 7, 20, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: América-SP tabela [19, 4, 10, 5, 16, 17] jogos [19, 4, 10, 5, 15, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Juventus-SP tabela [38, 14, 14, 10, 38, 35] jogos [38, 14, 14, 10, 38, 34] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: América-SP tabela [38, 7, 18, 13, 28, 35] jogos [38, 7, 18, 13, 27, 35] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1983

- tabela publicada x jogos — 2º Turno / Grupo A: Santos tabela [38, 17, 14, 7, 54, 34] jogos [38, 18, 12, 8, 54, 34] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo A: São José-SP tabela [38, 7, 16, 15, 25, 38] jogos [38, 7, 16, 15, 25, 39] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / Grupo D: Comercial-RP tabela [38, 10, 15, 13, 29, 31] jogos [38, 10, 15, 13, 30, 31] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1984

- jogo só no ogol, incluído em Fase única: Portuguesa 2-0 São Bento (1984-09-09)
- jogo só no ogol, incluído em Fase única: Taquaritinga 1-0 Marília (1984-09-09)

### 1985

- tabela publicada x jogos — Segunda fase / -: XV de Jaú tabela [19, 4, 8, 7, 16, 25] jogos [19, 4, 8, 7, 15, 24] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Marília tabela [19, 3, 8, 8, 13, 21] jogos [19, 3, 8, 8, 12, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Comibned Table - both stages / -: XV de Jaú tabela [38, 10, 16, 12, 36, 43] jogos [38, 10, 16, 12, 35, 42] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Comibned Table - both stages / -: Paulista tabela [38, 9, 16, 13, 31, 34] jogos [38, 9, 16, 13, 31, 35] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Comibned Table - both stages / -: Marília tabela [38, 8, 15, 15, 22, 35] jogos [38, 8, 15, 15, 21, 34] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 1986

- tabela publicada x jogos — Primeira fase / -: Portuguesa tabela [19, 10, 5, 4, 29, 21] jogos [19, 10, 5, 4, 28, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Juventus-SP tabela [19, 10, 3, 6, 28, 21] jogos [19, 10, 3, 6, 28, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Mogi Mirim tabela [19, 4, 11, 4, 20, 17] jogos [19, 4, 11, 4, 19, 16] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: XV de Jaú tabela [19, 5, 4, 10, 17, 26] jogos [19, 5, 4, 10, 18, 26] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Santo André tabela [19, 7, 7, 5, 11, 14] jogos [19, 8, 6, 5, 12, 14] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Juventus-SP tabela [19, 6, 7, 6, 20, 20] jogos [19, 6, 7, 6, 20, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: XV de Jaú tabela [19, 6, 7, 6, 14, 14] jogos [19, 6, 6, 7, 14, 15] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: XV de Piracicaba tabela [19, 6, 6, 7, 11, 19] jogos [19, 5, 6, 8, 8, 19] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Segunda fase / -: Comercial-RP tabela [19, 5, 6, 8, 17, 21] jogos [19, 5, 6, 8, 16, 21] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / -: Guarani tabela [19, 4, 7, 8, 15, 20] jogos [19, 5, 7, 7, 15, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Palmeiras tabela [38, 17, 13, 8, 54, 31] jogos [37, 17, 12, 8, 54, 31] — a tabela conta 38 jogos e as fontes trazem 37
- tabela publicada x jogos — Primeira fase / -: Portuguesa tabela [38, 16, 11, 11, 52, 37] jogos [38, 16, 11, 11, 51, 36] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Santo André tabela [38, 11, 17, 10, 26, 35] jogos [38, 12, 16, 10, 27, 35] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: XV de Piracicaba tabela [38, 10, 15, 13, 32, 43] jogos [37, 9, 14, 14, 29, 43] — a tabela conta 38 jogos e as fontes trazem 37
- tabela publicada x jogos — Primeira fase / -: Mogi Mirim tabela [38, 8, 19, 11, 36, 38] jogos [38, 8, 19, 11, 35, 37] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Guarani tabela [38, 10, 14, 14, 40, 47] jogos [38, 11, 14, 13, 40, 44] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: XV de Jaú tabela [38, 11, 11, 16, 31, 40] jogos [38, 11, 10, 17, 32, 41] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Comercial-RP tabela [38, 10, 13, 15, 38, 49] jogos [38, 10, 13, 15, 37, 49] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Xv De Novembro/J
- Xv De Novembro/J — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (XV de Jaú)
- placar corrigido pelo ogol — Santo André x Ferroviária-SP (1986-03-09): RSSSF 4-1, ogol 1-1; fica o do ogol, que fecha com a tabela publicada
- placar diferente no ogol — Palmeiras x Corinthians (1986-08-27): RSSSF 1-0, ogol 3-0; fica o da RSSSF
- jogo só no ogol, incluído em Second Stage: Palmeiras 0-0 XV de Piracicaba (1986-06-19)

### 1987

- tabela publicada x jogos — 2º Turno / -: Santo André tabela [38, 13, 13, 12, 43, 48] jogos [38, 13, 13, 12, 43, 38] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Ferroviária-SP tabela [38, 8, 18, 12, 22, 40] jogos [38, 7, 19, 12, 22, 40] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Bandeirante-SP tabela [38, 6, 11, 21, 23, 47] jogos [38, 6, 12, 20, 23, 47] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Aménca
- Aménca — clube que o ogol não tem; entra só pela RSSSF

### 1988

- tabela publicada x jogos — 2º Turno / Grupo A: Inter de Limeira tabela [19, 10, 6, 3, 23, 10] jogos [20, 10, 7, 3, 24, 11] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / Grupo A: Santos tabela [19, 9, 6, 4, 20, 12] jogos [20, 9, 7, 4, 20, 12] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / Grupo A: XV de Jaú tabela [19, 7, 7, 5, 26, 25] jogos [20, 6, 9, 5, 23, 25] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / Grupo A: Noroeste tabela [19, 5, 9, 5, 19, 19] jogos [20, 5, 9, 6, 20, 21] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / Grupo A: Botafogo-SP tabela [19, 7, 4, 8, 18, 25] jogos [20, 7, 5, 8, 19, 26] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / Grupo A: Mogi Mirim tabela [19, 6, 5, 8, 15, 23] jogos [20, 6, 5, 9, 17, 26] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / Grupo A: Juventus-SP tabela [19, 5, 6, 8, 19, 26] jogos [31, 10, 12, 9, 35, 34] — a tabela conta 19 jogos e as fontes trazem 31
- tabela publicada x jogos — 2º Turno / Grupo A: GE Novorizontino tabela [19, 3, 5, 11, 18, 29] jogos [20, 3, 6, 11, 19, 30] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / Grupo A: União São João tabela [19, 3, 5, 11, 15, 26] jogos [20, 3, 6, 11, 15, 25] — a tabela conta 19 jogos e as fontes trazem 20
- tabela publicada x jogos — 2º Turno / Grupo B: Corinthians tabela [19, 11, 4, 4, 32, 16] jogos [9, 4, 3, 2, 10, 7] — a tabela conta 19 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / Grupo B: Guarani tabela [19, 9, 8, 2, 35, 15] jogos [9, 3, 5, 1, 17, 11] — a tabela conta 19 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / Grupo B: São José-SP tabela [19, 9, 8, 2, 29, 16] jogos [9, 6, 2, 1, 18, 9] — a tabela conta 19 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / Grupo B: Palmeiras tabela [19, 8, 7, 4, 26, 18] jogos [9, 4, 5, 0, 17, 8] — a tabela conta 19 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / Grupo B: Portuguesa tabela [19, 7, 5, 7, 24, 22] jogos [9, 3, 1, 5, 8, 11] — a tabela conta 19 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / Grupo B: Ferroviária-SP tabela [19, 7, 4, 8, 24, 31] jogos [9, 3, 3, 3, 14, 18] — a tabela conta 19 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / Grupo B: XV de Piracicaba tabela [19, 6, 4, 9, 20, 28] jogos [9, 3, 2, 4, 11, 12] — a tabela conta 19 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / Grupo B: Santo André tabela [19, 2, 9, 8, 20, 30] jogos [9, 0, 4, 5, 11, 20] — a tabela conta 19 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / Grupo B: São Bento tabela [19, 2, 9, 8, 9, 22] jogos [9, 1, 6, 2, 7, 9] — a tabela conta 19 jogos e as fontes trazem 9
- tabela publicada x jogos — 2º Turno / Grupo B: América-SP tabela [19, 3, 6, 10, 21, 35] jogos [9, 1, 3, 5, 10, 18] — a tabela conta 19 jogos e as fontes trazem 9
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Bandeirante
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Ponte Preta
- Bandeirante — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Bandeirante-SP)
- Ponte Preta — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Ponte Preta)
- placar diferente no ogol — Juventus-SP x XV de Jaú (1988-06-05): RSSSF 0-0, ogol 1-1; fica o da RSSSF
- placar diferente no ogol — Juventus-SP x GE Novorizontino (1988-05-25): RSSSF 1-1, ogol 1-0; fica o da RSSSF
- placar diferente no ogol — Guarani x Corinthians (1988-07-31): RSSSF 0-0, ogol 0-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 3 jogos (ex.: Juventus-SP x XV de Jaú, ogol 1988-06-05); fica a do ogol
- só na RSSSF (não achado no ogol): Ponte Preta 5-1 Bandeirante-SP (1988-03-20)
- só na RSSSF (não achado no ogol): Corinthians 0-0 Ponte Preta (1988-04-21)
- só na RSSSF (não achado no ogol): Juventus-SP 1-0 GE Novorizontino (1988-05-25)
- só na RSSSF (não achado no ogol): Juventus-SP 1-1 XV de Jaú (1988-06-05)
- só na RSSSF (não achado no ogol): Juventus-SP 5-1 Bandeirante-SP (1988-03-20)
- só na RSSSF (não achado no ogol): Corinthians 0-0 Juventus-SP (1988-04-21)
- só na RSSSF (não achado no ogol): Juventus-SP 0-0 Santos (1988-05-01)
- só na RSSSF (não achado no ogol): São Bento 0-0 Bandeirante-SP (1988-05-01)
- só na RSSSF (não achado no ogol): Bandeirante-SP 1-1 Guarani (1988-05-04)
- só na RSSSF (não achado no ogol): Noroeste 1-2 Juventus-SP (1988-05-08)
- só na RSSSF (não achado no ogol): Bandeirante-SP 0-0 São José-SP (1988-05-08)
- só na RSSSF (não achado no ogol): Palmeiras 2-0 Bandeirante-SP (1988-05-11)
- só na RSSSF (não achado no ogol): Botafogo-SP 1-1 Juventus-SP (1988-05-15)
- só na RSSSF (não achado no ogol): Bandeirante-SP 1-0 Santo André (1988-05-15)
- só na RSSSF (não achado no ogol): Bandeirante-SP 1-1 Corinthians (1988-05-18)
- só na RSSSF (não achado no ogol): Mogi Mirim 2-3 Juventus-SP (1988-05-22)
- só na RSSSF (não achado no ogol): Ferroviária-SP 2-0 Bandeirante-SP (1988-05-22)
- só na RSSSF (não achado no ogol): União São João 0-2 Juventus-SP (1988-05-25)
- só na RSSSF (não achado no ogol): XV de Piracicaba 1-1 Bandeirante-SP (1988-05-25)
- só na RSSSF (não achado no ogol): Juventus-SP 1-0 Juventus-SP (1988-05-29)
- só na RSSSF (não achado no ogol): América-SP 0-0 Bandeirante-SP (1988-05-29)
- só na RSSSF (não achado no ogol): Juventus-SP 1-1 Inter de Limeira (1988-06-01)
- só na RSSSF (não achado no ogol): Bandeirante-SP 1-1 Portuguesa (1988-06-01)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Corinthians

### 1989

- placar diferente no ogol — São José-SP x Corinthians (1989-06-25): RSSSF 1-0, ogol 2-0; fica o da RSSSF

### 1990

- tabela publicada x jogos — Terceira fase / Grupo Preto: Corinthians tabela [12, 5, 7, 0, 13, 6] jogos [12, 4, 8, 0, 12, 7] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Terceira fase / Grupo Preto: Botafogo-SP tabela [12, 5, 2, 5, 12, 11] jogos [12, 5, 3, 4, 13, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 9 jogos (ex.: Ponte Preta x Santos, ogol 1990-03-30); fica a do ogol
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Bragantino

### 1991

- tabela publicada x jogos — Primeira fase / Grupo Verde: América-SP tabela [26, 5, 14, 7, 15, 21] jogos [26, 5, 14, 7, 16, 20] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo Verde: XV de Piracicaba tabela [26, 7, 8, 11, 26, 34] jogos [26, 7, 8, 11, 25, 35] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo Verde: Ferroviária-SP tabela [26, 5, 13, 8, 16, 18] jogos [26, 3, 14, 9, 13, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo Amarelo: Inter de Limeira tabela [26, 16, 2, 8, 37, 22] jogos [26, 15, 3, 8, 36, 24] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo Amarelo: Juventus-SP tabela [26, 9, 10, 7, 23, 24] jogos [26, 9, 11, 6, 23, 23] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo Amarelo: São José-SP tabela [26, 8, 7, 11, 23, 33] jogos [26, 7, 7, 12, 21, 35] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo Amarelo: Catanduvense tabela [26, 4, 12, 10, 15, 33] jogos [26, 4, 12, 10, 15, 32] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / Grupo Amarelo: São Bento tabela [26, 4, 7, 15, 18, 36] jogos [26, 4, 7, 15, 18, 35] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de São Paulo x Corinthians na FINAL sempre na mesma ordem) — ogol Corinthians 0-3 São Paulo (1991-12-08)

### 1992

- tabela publicada x jogos — 2º Turno / -: GE Novorizontino tabela [26, 8, 9, 9, 27, 26] jogos [26, 9, 8, 9, 30, 26] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Olímpia tabela [26, 8, 9, 9, 24, 25] jogos [26, 9, 9, 8, 25, 24] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Araçatuba tabela [26, 5, 10, 11, 16, 25] jogos [26, 5, 9, 12, 16, 28] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Catanduvense tabela [26, 2, 7, 17, 10, 47] jogos [26, 1, 7, 18, 9, 48] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Segunda fase / Grupo 1: São Paulo tabela [12, 6, 5, 1, 0, 14] jogos [6, 5, 1, 0, 14, 4] — a tabela conta 12 jogos e as fontes trazem 6
- mando da RSSSF trocado pelo do ogol (a página escreve as partidas de São Paulo x Palmeiras na FINAL sempre na mesma ordem) — ogol Palmeiras 2-4 São Paulo (1992-12-05)

### 1993

- mando invertido no ogol — RSSSF GE Novorizontino 2-3 Santos, ogol Santos 3-2 GE Novorizontino (1993-05-23); fica a RSSSF
- mando invertido no ogol — RSSSF Santos 2-3 GE Novorizontino, ogol GE Novorizontino 3-2 Santos (1993-05-30); fica a RSSSF
- placar diferente no ogol — Palmeiras x Corinthians (1993-06-12): RSSSF 3-0, ogol 4-0; fica o da RSSSF

### 1994

- tabela publicada x jogos — 2º Turno / -: Palmeiras tabela [30, 20, 7, 3, 63, 24] jogos [30, 20, 7, 3, 63, 22] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Corinthians tabela [30, 16, 9, 5, 59, 34] jogos [30, 16, 9, 5, 60, 34] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Portuguesa tabela [30, 9, 10, 11, 40, 49] jogos [30, 9, 10, 11, 40, 50] — placar diverge entre RSSSF e ogol em Santo André x Portuguesa (1-3 x 1-2) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / -: Guarani tabela [30, 8, 11, 11, 49, 46] jogos [30, 8, 11, 11, 47, 46] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Ponte Preta tabela [30, 8, 10, 12, 37, 43] jogos [30, 8, 10, 12, 37, 44] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — 2º Turno / -: Ituano tabela [30, 5, 9, 16, 22, 46] jogos [30, 5, 9, 16, 21, 46] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — Santo André x Portuguesa (1994-05-07): RSSSF 1-3, ogol 1-2; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 5 jogos (ex.: Santos x Bragantino, ogol 1994-03-15); fica a do ogol

### 1995

- tabela publicada x jogos — 2º Turno / Grupo A1: Santos tabela [30, 13, 11, 6, 49, 30] jogos [30, 13, 11, 6, 49, 31] — placar diverge entre RSSSF e ogol em Santos x Ponte Preta (4-2 x 4-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- tabela publicada x jogos — 2º Turno / Grupo A1: Ponte Preta tabela [30, 7, 8, 15, 30, 55] jogos [30, 7, 8, 15, 31, 55] — placar diverge entre RSSSF e ogol em Santos x Ponte Preta (4-2 x 4-1) e nenhuma das versões fecha com a tabela; fica a RSSSF
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): XV de Novembro
- XV de Novembro — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (XV de Piracicaba)
- placar diferente no ogol — Santos x Ponte Preta (1995-03-20): RSSSF 4-2, ogol 4-1; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 12 jogos (ex.: Portuguesa x Palmeiras, ogol 1995-01-29); fica a do ogol
- jogo só no ogol, incluído em Schedule of Championship of São Paulo 1995 - Final Fase:: União São João 1-1 Santos (1995-07-15)
- jogo só no ogol, incluído em Schedule of Championship of São Paulo 1995 - Final Fase:: Portuguesa 0-1 Corinthians (1995-07-15)
- jogo só no ogol, incluído em Schedule of Championship of São Paulo 1995 - Final Fase: / Group 1: São Paulo 0-1 Palmeiras (1995-07-16)
- jogo só no ogol, incluído em Schedule of Championship of São Paulo 1995 - Final Fase: / Group 1: Mogi Mirim 1-0 Guarani (1995-07-16)
- jogo só no ogol, incluído em FINAL: Palmeiras 1-2 Corinthians (1995-08-06)

### 1996

- sem ocorrências

### 1997

- tabela publicada x jogos — Primeira fase / Grupo 1: Palmeiras tabela [23, 14, 6, 3, 58, 27] jogos [26, 14, 6, 6, 59, 37] — a tabela conta 23 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / Grupo 1: Santos tabela [23, 13, 7, 3, 45, 23] jogos [26, 14, 7, 5, 52, 28] — a tabela conta 23 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / Grupo 2: Corinthians tabela [23, 13, 6, 4, 51, 28] jogos [26, 15, 7, 4, 58, 32] — a tabela conta 23 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / Grupo 2: São Paulo tabela [23, 10, 10, 3, 50, 26] jogos [26, 12, 11, 3, 56, 28] — a tabela conta 23 jogos e as fontes trazem 26
- tabela publicada x jogos — Primeira fase / Grupo 2: Inter Limeira tabela [23, 7, 8, 8, 35, 37] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- tabela publicada x jogos — Terceira fase / Grupo 2: Inter Limeira tabela [23, 7, 8, 8, 35, 37] jogos None — o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Inter Limeira
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Poruguesa Sant
- Inter Limeira — clube que o ogol não tem; entra só pela RSSSF
- Poruguesa Sant — clube que o ogol não tem; entra só pela RSSSF
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Corinthians

### 1998

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Uniao SJ
- Uniao SJ — clube que o ogol não tem; entra só pela RSSSF
- placar diferente no ogol — Portuguesa Santista x Juventus-SP (1998-02-11): RSSSF 2-4, ogol 2-1; fica o da RSSSF
- placar corrigido pelo ogol — São Paulo x Santos (1998-03-28): RSSSF 3-0, ogol 2-1; fica o do ogol, que fecha com a tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Portuguesa Santista x Juventus-SP, ogol 1998-02-11); fica a do ogol
- só na RSSSF (não achado no ogol): Portuguesa Santista 2-1 Juventus-SP (None)
- só na RSSSF (não achado no ogol): Juventus-SP 0-1 Inter de Limeira (1998-03-15)
- só na RSSSF (não achado no ogol): Araçatuba 1-0 Portuguesa Santista (1998-03-15)
- só na RSSSF (não achado no ogol): Araçatuba 2-0 Inter de Limeira (1998-03-22)
- só na RSSSF (não achado no ogol): Juventus-SP 1-1 Araçatuba (1998-03-29)
- só na RSSSF (não achado no ogol): Inter de Limeira 2-2 Portuguesa Santista (1998-03-29)
- só na RSSSF (não achado no ogol): Araçatuba 2-0 Juventus-SP (1998-04-05)
- só na RSSSF (não achado no ogol): Portuguesa Santista 1-1 Inter de Limeira (1998-04-05)
- só na RSSSF (não achado no ogol): Inter de Limeira 1-0 Araçatuba (1998-04-12)
- só na RSSSF (não achado no ogol): Juventus-SP 0-1 Portuguesa Santista (1998-04-12)
- só na RSSSF (não achado no ogol): Inter de Limeira 5-3 Juventus-SP (1998-04-19)
- só na RSSSF (não achado no ogol): Portuguesa Santista 1-0 Araçatuba (1998-04-19)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, São Paulo

### 1999

- tabela publicada x jogos — Primeira fase / Grupo 1: União Barbarense tabela [10, 6, 2, 2, 20, 10] jogos [10, 5, 3, 2, 20, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Uniao SJ
- Uniao SJ — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Uniao SJ)
- placar diferente no ogol — Rio Branco-SP x São José-SP (1999-01-31): RSSSF 3-1, ogol 2-1; fica o da RSSSF

### 2000

- tabela publicada x jogos — Primeira fase / Grupo 1: Matonense tabela [10, 5, 1, 4, 22, 13] jogos [11, 5, 1, 5, 22, 15] — a tabela conta 10 jogos e as fontes trazem 11
- tabela publicada x jogos — Primeira fase / Grupo 1: Matonense tabela [10, 5, 1, 4, 22, 13] jogos [11, 5, 1, 5, 22, 15] — a tabela conta 10 jogos e as fontes trazem 11
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Inter Limeira
- Inter Limeira — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Inter Limeira)
- data diferente entre RSSSF e ogol (mais de 3 dias) em 2 jogos (ex.: Palmeiras x Santos, ogol 2000-06-03); fica a do ogol
- só na RSSSF (não achado no ogol): Matonense 0-2 Portuguesa (2000-01-27)

### 2001

- tabela publicada x jogos — Primeira fase / -: Botafogo-SP tabela [5, 1, 0, 4, 23, 25] jogos [19, 6, 8, 5, 28, 32] — a tabela conta 5 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: São Caetano tabela [6, 1, 0, 5, 29, 22] jogos [15, 6, 4, 5, 29, 22] — a tabela conta 6 jogos e as fontes trazem 15
- tabela publicada x jogos — Primeira fase / -: Palmeiras tabela [7, 1, 1, 5, 28, 25] jogos [15, 7, 3, 5, 28, 25] — a tabela conta 7 jogos e as fontes trazem 15
- tabela publicada x jogos — Primeira fase / -: São Paulo tabela [6, 0, 0, 6, 32, 26] jogos [15, 6, 3, 6, 32, 26] — a tabela conta 6 jogos e as fontes trazem 15
- tabela publicada x jogos — Primeira fase / -: Guarani tabela [4, 0, 3, 1, 7, 16] jogos [15, 4, 4, 7, 16, 25] — a tabela conta 4 jogos e as fontes trazem 15
- tabela publicada x jogos — Primeira fase / -: Botafogo-SP tabela [5, 1, 0, 4, 23, 25] jogos [19, 6, 8, 5, 28, 32] — a tabela conta 5 jogos e as fontes trazem 19
- tabela publicada x jogos — Primeira fase / -: São Caetano tabela [6, 1, 0, 5, 29, 22] jogos [15, 6, 4, 5, 29, 22] — a tabela conta 6 jogos e as fontes trazem 15
- tabela publicada x jogos — Primeira fase / -: Palmeiras tabela [7, 1, 1, 5, 28, 25] jogos [15, 7, 3, 5, 28, 25] — a tabela conta 7 jogos e as fontes trazem 15
- tabela publicada x jogos — Primeira fase / -: São Paulo tabela [6, 0, 0, 6, 32, 26] jogos [15, 6, 3, 6, 32, 26] — a tabela conta 6 jogos e as fontes trazem 15
- tabela publicada x jogos — Primeira fase / -: Guarani tabela [4, 0, 3, 1, 7, 16] jogos [15, 4, 4, 7, 16, 25] — a tabela conta 4 jogos e as fontes trazem 15

### 2002

- os clubes do Torneio Rio-São Paulo não jogaram o Paulista; o campeão é o Ituano. O Supercampeonato de 2002 (vencido pelo São Paulo) é outra competição e não entra
- tabela publicada x jogos — Fase única / -: Juventus-SP tabela [22, 10, 7, 5, 38, 34] jogos [22, 10, 7, 5, 38, 35] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: União Barbarense tabela [22, 6, 10, 6, 33, 36] jogos [22, 6, 9, 7, 33, 36] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Portuguesa Santista tabela [22, 5, 4, 13, 28, 47] jogos [24, 5, 6, 13, 32, 51] — a tabela conta 22 jogos e as fontes trazem 24
- tabela publicada x jogos — Fase única / -: Juventus-SP tabela [22, 10, 7, 5, 38, 34] jogos [22, 10, 7, 5, 38, 35] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: União Barbarense tabela [22, 6, 10, 6, 33, 36] jogos [22, 6, 9, 7, 33, 36] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Francana
- Francana — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Francana)
- só na RSSSF (não achado no ogol): Francana 2-2 Portuguesa Santista (2002-06-02)
- só na RSSSF (não achado no ogol): Portuguesa Santista 2-2 Francana (2002-06-05)

### 2003

- tabela publicada x jogos — Primeira fase / Grupo 1: Rio Branco-SP tabela [6, 2, 3, 1, 11, 8] jogos [6, 2, 3, 1, 12, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Inter de Limeira tabela [6, 0, 1, 5, 3, 13] jogos [6, 0, 1, 5, 3, 12] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Atlético Sorocaba
- Atlético Sorocaba — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Atlético Sorocaba)
- só na RSSSF (não achado no ogol): Atlético Sorocaba 2-1 Botafogo-SP (2003-04-02)
- só na RSSSF (não achado no ogol): Botafogo-SP 0-0 Atlético Sorocaba (2003-04-05)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Corinthians

### 2004

- tabela publicada x jogos — Primeira fase / Grupo 1: Ponte Preta tabela [9, 3, 4, 2, 12, 9] jogos [10, 4, 4, 2, 15, 9] — a tabela conta 9 jogos e as fontes trazem 10
- tabela publicada x jogos — Primeira fase / Grupo 1: Juventus-SP tabela [9, 2, 0, 7, 13, 23] jogos [10, 2, 0, 8, 13, 26] — a tabela conta 9 jogos e as fontes trazem 10
- placar diferente no ogol — Paulista x Ponte Preta (2004-03-20): RSSSF 2-2, ogol 4-3; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Juventus-SP x Ponte Preta, ogol 2004-02-11); fica a do ogol
- só na RSSSF (não achado no ogol): Juventus-SP 0-3 Ponte Preta (2004-02-01)

### 2005

- tabela publicada x jogos — Fase única / -: Portuguesa tabela [19, 6, 5, 8, 19, 27] jogos [19, 6, 6, 7, 27, 32] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: União Barbarense tabela [19, 5, 5, 9, 24, 30] jogos [19, 5, 5, 9, 25, 30] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: União São João tabela [19, 5, 5, 9, 31, 46] jogos [19, 5, 5, 9, 31, 47] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Atlético Sorocaba tabela [19, 3, 4, 12, 26, 37] jogos [19, 4, 4, 11, 26, 37] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Portuguesa tabela [19, 6, 5, 8, 19, 27] jogos [19, 6, 6, 7, 27, 32] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: União Barbarense tabela [19, 5, 5, 9, 24, 30] jogos [19, 5, 5, 9, 25, 30] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: União São João tabela [19, 5, 5, 9, 31, 46] jogos [19, 5, 5, 9, 31, 47] — há jogo do clube sem conferência no ogol
- tabela publicada x jogos — Fase única / -: Atlético Sorocaba tabela [19, 3, 4, 12, 26, 37] jogos [19, 4, 4, 11, 26, 37] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- mando invertido no ogol — RSSSF Palmeiras 0-3 São Paulo, ogol São Paulo 3-0 Palmeiras (2005-02-20); fica a RSSSF
- mando invertido no ogol — RSSSF São Paulo 5-0 Portuguesa Santista, ogol Portuguesa Santista 0-5 São Paulo (2005-02-24); fica a RSSSF
- mando invertido no ogol — RSSSF Portuguesa Santista 3-2 Paulista, ogol Paulista 2-3 Portuguesa Santista (2005-02-27); fica a RSSSF
- mando invertido no ogol — RSSSF Corinthians 6-1 União São João, ogol União São João 1-6 Corinthians (2005-03-05); fica a RSSSF

### 2006

- tabela publicada x jogos — Fase única / -: Portuguesa tabela [19, 5, 2, 12, 22, 38] jogos [19, 5, 3, 11, 21, 30] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase única / -: Portuguesa tabela [19, 5, 2, 12, 22, 38] jogos [19, 5, 3, 11, 21, 30] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- placar diferente no ogol — Bragantino x Ponte Preta (2006-04-09): RSSSF 0-1, ogol 0-0; fica o da RSSSF

### 2007

- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Santos x América-SP, ogol 2007-02-14); fica a do ogol
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Santos

### 2008

- sem ocorrências

### 2009

- placar corrigido pelo ogol — Marília x Guaratinguetá (2009-02-26): RSSSF 1-2, ogol 2-2; fica o do ogol, que fecha com a tabela publicada
- placar corrigido pelo ogol — Bragantino x Santos (2009-02-26): RSSSF 2-0, ogol 2-2; fica o do ogol, que fecha com a tabela publicada
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Barueri 2-3 Mirassol (2009-04-11)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ponte Preta 3-2 Santo André (2009-04-12)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Santo André 1-1 Ponte Preta (2009-04-18)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Mirassol 3-5 Barueri (2009-04-19)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ponte Preta 2-0 Barueri (2009-04-25)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Barueri 1-1 Ponte Preta (2009-05-02)

### 2010

- tabela publicada x jogos — Primeira fase / -: São Caetano tabela [19, 8, 3, 8, 29, 25] jogos [19, 8, 3, 8, 30, 25] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Rio Claro tabela [19, 5, 4, 10, 24, 33] jogos [19, 5, 4, 10, 24, 34] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: São Caetano tabela [19, 8, 3, 8, 29, 25] jogos [19, 8, 3, 8, 30, 25] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Rio Claro tabela [19, 5, 4, 10, 24, 33] jogos [19, 5, 4, 10, 24, 34] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ponte Preta 0-0 Botafogo-SP (2010-04-10)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Oeste 1-0 São Caetano (2010-04-10)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: São Caetano 3-1 Oeste (2010-04-17)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Botafogo-SP 2-2 Ponte Preta (2010-04-17)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: São Caetano 1-0 Botafogo-SP (2010-04-24)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Botafogo-SP 1-0 São Caetano (2010-05-01)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Santos

### 2011

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Botofago
- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): Gremio Prudente
- Botofago — clube que o ogol não tem; entra só pela RSSSF
- Gremio Prudente — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas (Barueri)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Oeste 1-0 Mirassol (2011-04-30)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ponte Preta 0-0 São Caetano (2011-04-30)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ponte Preta 2-1 Oeste (2011-05-04)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Oeste 3-0 Ponte Preta (2011-05-07)

### 2012

- placar corrigido pelo ogol — Botafogo-SP x XV de Piracicaba (2012-01-25): RSSSF 3-1, ogol 2-1; fica o do ogol, que fecha com a tabela publicada
- placar corrigido pelo ogol — São Paulo x Comercial-RP (2012-02-09): RSSSF 1-0, ogol 1-1; fica o do ogol, que fecha com a tabela publicada
- placar corrigido pelo ogol — Catanduvense x Guarani (2012-04-01): RSSSF 0-2, ogol 1-2; fica o do ogol, que fecha com a tabela publicada
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Mogi Mirim 3-2 Oeste (2012-04-28)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Bragantino 1-1 Mirassol (2012-04-28)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Bragantino 2-4 Mogi Mirim (2012-05-05)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Mogi Mirim 4-2 Bragantino (2012-05-12)
- jogo só no ogol, incluído em FINALS:: Santos 4-2 Guarani (2012-05-13)

### 2013

- nome da RSSSF sem clube no ogol (jogos dele ficam de fora): União Bandeirante
- União Bandeirante — clube que o ogol não tem; entra só pela RSSSF
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Botafogo-SP 1-4 Penapolense (2013-05-04)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ponte Preta 1-0 Linense (2013-05-05)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Penapolense 0-0 Ponte Preta (2013-05-12)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ponte Preta 4-2 Penapolense (2013-05-18)

### 2014

- placar diferente no ogol — XV de Piracicaba x São Paulo (2014-02-26): RSSSF 1-2, ogol 1-3; fica o da RSSSF
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Ponte Preta x Ituano, ogol 2014-02-12); fica a do ogol
- jogo só no ogol, incluído em First Phase: Mogi Mirim 3-3 Atlético Sorocaba (2014-01-29)
- jogo só no ogol, incluído em First Phase: Oeste 1-1 Comercial-RP (2014-01-29)
- jogo só no ogol, incluído em First Phase: Portuguesa 4-0 Linense (2014-02-09)

### 2015

- sem ocorrências

### 2016

- tabela publicada x jogos — Fase final / -: Santos tabela [19, 12, 6, 1, 34, 17] jogos [19, 11, 7, 1, 34, 17] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Osasco Audax tabela [19, 9, 4, 6, 32, 26] jogos [19, 8, 5, 6, 32, 26] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Corinthians tabela [17, 12, 2, 3, 32, 10] jogos [17, 12, 3, 2, 32, 10] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Fase final / -: Palmeiras tabela [17, 8, 3, 6, 29, 19] jogos [17, 8, 4, 5, 29, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada

### 2017

- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Mirassol 0-1 Ituano (2017-04-01)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Santo André 2-0 Red Bull Bragantino II (2017-04-02)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ferroviária-SP 2-2 São Bento (2017-04-04)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ituano 1-1 Santo André (2017-04-08)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: São Bento 1-1 Mirassol (2017-04-08)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Red Bull Bragantino II 4-1 Ferroviária-SP (2017-04-08)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Santo André 1-1 São Bento (2017-04-15)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ituano 0-3 Ferroviária-SP (2017-04-15)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Mirassol 3-1 Red Bull Bragantino II (2017-04-15)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ituano 1-0 Santo André (2017-04-21)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Santo André 1-1 Ituano (2017-04-29)

### 2018

- jogo só no ogol, incluído em FIRST STAGE:: São Bento 2-0 São Paulo (2018-01-17)
- jogo só no ogol, incluído em FIRST STAGE:: Corinthians 2-1 Ferroviária-SP (2018-01-24)
- jogo só no ogol, incluído em FIRST STAGE:: Mirassol 0-2 São Paulo (2018-01-24)
- jogo só no ogol, incluído em FIRST STAGE:: Ponte Preta 1-2 Santos (2018-01-25)
- jogo só no ogol, incluído em FIRST STAGE:: Ituano 0-0 Santo André (2018-01-25)
- jogo só no ogol, incluído em FIRST STAGE:: Red Bull Bragantino II 2-1 Linense (2018-01-29)
- jogo só no ogol, incluído em FIRST STAGE:: Santo André 2-1 Corinthians (2018-02-09)
- jogo só no ogol, incluído em FIRST STAGE:: São Paulo 0-1 Santos (2018-02-18)
- jogo só no ogol, incluído em FIRST STAGE:: São Caetano 1-0 São Bento (2018-02-25)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Mirassol 3-1 Red Bull Bragantino II (2018-03-17)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: São Bento 1-2 Ituano (2018-03-17)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ferroviária-SP 0-2 Ponte Preta (2018-03-18)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Red Bull Bragantino II 2-2 São Bento (2018-03-20)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ituano 2-2 Ferroviária-SP (2018-03-21)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ponte Preta 2-0 Mirassol (2018-03-21)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ituano 0-2 Mirassol (2018-03-24)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ferroviária-SP 3-1 Red Bull Bragantino II (2018-03-24)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: São Bento 3-1 Ponte Preta (2018-03-24)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Mirassol 1-1 Ponte Preta (2018-03-29)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ponte Preta 1-0 Mirassol (2018-04-03)
- final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, Corinthians

### 2019

- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Botafogo-SP 1-1 Oeste (2019-03-23)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Bragantino 0-1 Ponte Preta (2019-03-24)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Mirassol 2-0 Guarani (2019-03-25)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Oeste 3-3 Botafogo-SP (2019-03-27)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ponte Preta 1-1 Bragantino (2019-03-27)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Guarani 2-2 Mirassol (2019-03-28)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Oeste 2-2 Ponte Preta (2019-03-30)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Mirassol 0-1 Red Bull Bragantino II (2019-04-02)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ponte Preta 2-0 Oeste (2019-04-07)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Red Bull Bragantino II 3-1 Mirassol (2019-04-09)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Red Bull Bragantino II 0-0 Ponte Preta (2019-04-16)

### 2020

- 6 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ferroviária-SP 0-2 Inter de Limeira (2020-07-29)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Guarani 1-1 Ituano (2020-07-29)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Novorizontino 0-2 Botafogo-SP (2020-07-29)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Inter de Limeira 1-2 Guarani (2020-08-01)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Bragantino 1-1 Botafogo-SP (2020-08-02)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Bragantino 1-0 Guarani (2020-08-05)

### 2021

- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ituano 5-1 Santo André (2021-05-13)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ponte Preta 0-0 Botafogo-SP (2021-05-14)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Bragantino 1-1 Ponte Preta (2021-05-16)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Novorizontino 4-0 Ituano (2021-05-18)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Novorizontino 2-0 Ponte Preta (2021-05-20)

### 2022

- tabela publicada x jogos — Primeira fase / -: Corinthians tabela [12, 7, 2, 3, 19, 11] jogos [12, 7, 2, 3, 19, 9] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- data diferente entre RSSSF e ogol (mais de 3 dias) em 1 jogos (ex.: Palmeiras x Corinthians, ogol 2022-03-17); fica a do ogol
- jogo só no ogol, incluído em Second Phase - Fase Quartas-de-final: Corinthians 1-1 Guarani (2022-03-24)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Mirassol 0-1 EC Água Santa (2022-03-25)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ferroviária-SP 1-1 Inter de Limeira (2022-03-26)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Botafogo-SP 3-0 Inter de Limeira (2022-03-28)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Ituano 2-2 EC Água Santa (2022-03-28)
- jogo do Troféu do Interior no ogol (torneio à parte), fica de fora: Botafogo-SP 0-3 Ituano (2022-03-31)

### 2023

- 6 tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência
- jogo da Taça Independência no ogol (torneio à parte), fica de fora: Guarani 2-1 Portuguesa (2023-03-10)
- jogo da Taça Independência no ogol (torneio à parte), fica de fora: Santo André 0-0 Inter de Limeira (2023-03-11)
- jogo da Taça Independência no ogol (torneio à parte), fica de fora: São Bernardo 1-0 Inter de Limeira (2023-03-16)
- jogo da Taça Independência no ogol (torneio à parte), fica de fora: Mirassol 1-0 Guarani (2023-03-17)
- jogo da Taça Independência no ogol (torneio à parte), fica de fora: São Bernardo 0-0 Mirassol (2023-03-26)

### 2024

- tabela publicada x jogos — Primeira fase / -: Ituano tabela [12, 1, 3, 8, 5, 18] jogos [12, 1, 3, 8, 5, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Primeira fase / -: Ituano tabela [12, 1, 3, 8, 5, 18] jogos [12, 1, 3, 8, 5, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- tabela publicada x jogos — Final / -: Ituano tabela [12, 1, 3, 8, 5, 18] jogos [12, 1, 3, 8, 5, 19] — RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada
- jogo só no ogol, incluído em Third Phase - Fase Semifinal: Santos 1-0 Palmeiras (2024-03-31)
- jogo só no ogol, incluído em Third Phase - Fase Semifinal: Palmeiras 2-0 Santos (2024-04-07)

### 2025

- a página da RSSSF parou na 6ª rodada da 1ª fase: as tabelas dela são parciais e não servem de conferência; os outros jogos vêm do ogol
- jogo só no ogol, incluído em FIRST STAGE:: Velo Clube 2-2 Portuguesa (2025-02-04)
- jogo só no ogol, incluído em FIRST STAGE:: Inter de Limeira 1-1 Bragantino (2025-02-04)
- jogo só no ogol, incluído em FIRST STAGE:: Noroeste 1-2 Ponte Preta (2025-02-05)
- jogo só no ogol, incluído em FIRST STAGE:: São Paulo 4-1 Mirassol (2025-02-05)
- jogo só no ogol, incluído em FIRST STAGE:: Santos 1-1 Botafogo-SP (2025-02-06)
- jogo só no ogol, incluído em FIRST STAGE:: São Bernardo 1-1 Novorizontino (2025-02-06)
- jogo só no ogol, incluído em FIRST STAGE:: Guarani 4-0 EC Água Santa (2025-02-06)
- jogo só no ogol, incluído em FIRST STAGE:: Palmeiras 1-1 Corinthians (2025-02-06)
- jogo só no ogol, incluído em FIRST STAGE:: Portuguesa 2-0 Inter de Limeira (2025-02-07)
- jogo só no ogol, incluído em FIRST STAGE:: Botafogo-SP 1-0 Velo Clube (2025-02-08)
- jogo só no ogol, incluído em FIRST STAGE:: Mirassol 1-1 Noroeste (2025-02-08)
- jogo só no ogol, incluído em FIRST STAGE:: Bragantino 1-0 São Paulo (2025-02-08)
- jogo só no ogol, incluído em FIRST STAGE:: Novorizontino 0-0 Santos (2025-02-09)
- jogo só no ogol, incluído em FIRST STAGE:: Ponte Preta 2-0 Guarani (2025-02-09)
- jogo só no ogol, incluído em FIRST STAGE:: EC Água Santa 1-1 Palmeiras (2025-02-09)
- jogo só no ogol, incluído em FIRST STAGE:: Corinthians 2-0 São Bernardo (2025-02-09)
- jogo só no ogol, incluído em FIRST STAGE:: São Paulo 0-0 Inter de Limeira (2025-02-11)
- jogo só no ogol, incluído em FIRST STAGE:: Botafogo-SP 1-0 Bragantino (2025-02-11)
- jogo só no ogol, incluído em FIRST STAGE:: Noroeste 2-3 São Bernardo (2025-02-12)
- jogo só no ogol, incluído em FIRST STAGE:: Mirassol 1-2 Ponte Preta (2025-02-12)
- jogo só no ogol, incluído em FIRST STAGE:: EC Água Santa 0-0 Portuguesa (2025-02-12)
- jogo só no ogol, incluído em FIRST STAGE:: Corinthians 2-1 Santos (2025-02-13)
- jogo só no ogol, incluído em FIRST STAGE:: Guarani 0-0 Novorizontino (2025-02-13)
- jogo só no ogol, incluído em FIRST STAGE:: Inter de Limeira 0-3 Palmeiras (2025-02-13)
- jogo só no ogol, incluído em FIRST STAGE:: São Paulo 3-3 Velo Clube (2025-02-14)
- jogo só no ogol, incluído em FIRST STAGE:: Ponte Preta 0-0 Botafogo-SP (2025-02-15)
- jogo só no ogol, incluído em FIRST STAGE:: Portuguesa 2-2 Corinthians (2025-02-15)
- jogo só no ogol, incluído em FIRST STAGE:: Bragantino 2-1 Noroeste (2025-02-15)
- jogo só no ogol, incluído em FIRST STAGE:: São Bernardo 1-0 Guarani (2025-02-16)
- jogo só no ogol, incluído em FIRST STAGE:: Velo Clube 2-1 Inter de Limeira (2025-02-16)
- jogo só no ogol, incluído em FIRST STAGE:: Palmeiras 0-0 São Paulo (2025-02-16)
- jogo só no ogol, incluído em FIRST STAGE:: Santos 3-1 EC Água Santa (2025-02-16)
- jogo só no ogol, incluído em FIRST STAGE:: Novorizontino 2-1 Mirassol (2025-02-17)
- jogo só no ogol, incluído em FIRST STAGE:: EC Água Santa 2-2 Inter de Limeira (2025-02-19)
- jogo só no ogol, incluído em FIRST STAGE:: Guarani 1-1 Velo Clube (2025-02-19)
- jogo só no ogol, incluído em FIRST STAGE:: Santos 3-0 Noroeste (2025-02-19)
- jogo só no ogol, incluído em FIRST STAGE:: São Paulo 1-2 Ponte Preta (2025-02-19)
- jogo só no ogol, incluído em FIRST STAGE:: Bragantino 3-0 Mirassol (2025-02-20)
- jogo só no ogol, incluído em FIRST STAGE:: Palmeiras 3-1 Botafogo-SP (2025-02-20)
- jogo só no ogol, incluído em FIRST STAGE:: Portuguesa 1-1 São Bernardo (2025-02-21)
- jogo só no ogol, incluído em FIRST STAGE:: Botafogo-SP 1-2 Novorizontino (2025-02-23)
- jogo só no ogol, incluído em FIRST STAGE:: Corinthians 2-2 Guarani (2025-02-23)
- jogo só no ogol, incluído em FIRST STAGE:: Noroeste 1-1 Portuguesa (2025-02-23)
- jogo só no ogol, incluído em FIRST STAGE:: Inter de Limeira 0-3 Santos (2025-02-23)
- jogo só no ogol, incluído em FIRST STAGE:: Mirassol 2-3 Palmeiras (2025-02-23)
- jogo só no ogol, incluído em FIRST STAGE:: Ponte Preta 0-2 Bragantino (2025-02-23)
- jogo só no ogol, incluído em FIRST STAGE:: São Bernardo 1-3 São Paulo (2025-02-23)
- jogo só no ogol, incluído em FIRST STAGE:: Velo Clube 1-0 EC Água Santa (2025-02-23)
- jogo só no ogol, incluído em FIRST STAGE:: São Bernardo 0-3 Palmeiras (2025-03-01)
- jogo só no ogol, incluído em FIRST STAGE:: Corinthians 2-0 Mirassol (2025-03-02)
- jogo só no ogol, incluído em FIRST STAGE:: Santos 2-0 Bragantino (2025-03-02)
- jogo só no ogol, incluído em FIRST STAGE:: São Paulo 1-0 Novorizontino (2025-03-03)
- jogo só no ogol, incluído em FIRST STAGE:: Corinthians 2-1 Santos (2025-03-09)
- jogo só no ogol, incluído em FIRST STAGE:: Palmeiras 1-0 São Paulo (2025-03-11)
- jogo só no ogol, incluído em FIRST STAGE:: Palmeiras 0-1 Corinthians (2025-03-16)
- jogo só no ogol, incluído em FIRST STAGE:: Corinthians 0-0 Palmeiras (2025-03-28)

## Identidade dos clubes

- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol (clube antigo sem cidade na ficha
  é dado como paulista).
- Clube do `futebol.db` usa o nome de lá; clube das Séries C e D e da Copa usa o nome daqueles pacotes; os outros seguem o
  nome curto do ogol, com "-SP" só quando outro clube de outro estado tem o mesmo nome.
- Clube que o ogol não tem (temporadas sem calendário no ogol) entra pela RSSSF, com código "rs-<nome>"; quando o mesmo
  nome aparece em outra temporada com código do ogol, vale esse código.
- **São Paulo da Floresta (1930-1935) e São Paulo FC:** a RSSSF, o ogol (mesmo código) e a Wikipédia tratam como o mesmo
  clube; o pacote segue as fontes até a decisão do agente principal (pedido em `docs/coleta/pedidos.md`).

## O que não deu para coletar

- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade, combinado com o Guilherme).
- **Autores dos gols:** só onde a RSSSF traz e a soma fecha com o placar.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima.
- **Classificação por rodada:** só nas fases de pontos corridos em que todos os jogos têm a rodada (vem do ogol).
