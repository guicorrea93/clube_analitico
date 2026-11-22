# Campeonato Argentino (`arg-1`) — documentação

Gerado por `python coleta/comum-sulamerica/documentar.py` a partir do pacote `data/coleta/arg-1/pacote/`, do código `coleta/arg-1/` e do relatório `docs/coleta/arg-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 196, de 1891 a 2025 Liga; 1 sem jogos.
- **Jogos:** 43235 (42546 com placar); **gols:** 120669; **gols com autor:** 34264 (28%); **cartões:** 37037.
- **Clubes:** 171; **artilheiros:** 191 edições com artilheiro (229 linhas, com empates).
- **Classificação final:** 196 edições; **tabelas publicadas guardadas para conferência:** 4311 linhas.
- **No banco:** sim; **último commit do pacote:** 665fe93.
- **Observação da competição:** 1ª divisão argentina de 1891 a 2025: uma edição por torneio que deu título de campeão (ligas rivais de 1912-1914, 1919-1926 e 1931-1934; Copa de Honor, Campeonato e Copa de Oro em 1936; Metropolitano e Nacional de 1967 a 1985; Apertura e Clausura de 1991/92 a 2013/14 e em 2025). Sem as copas da liga (2019-2024), a Copa Campeonato 2013/14, os torneios de reclassificação e as liguillas, que não davam o título.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão argentina (arg-1): uma por torneio que deu título de campeão da Primera División.

Lista de títulos: RSSSF (argchamp.html, "Argentine Amateur/Professional First Division Champions"), conferida com a
Wikipédia. Regra do guia internacional: ano com mais de um campeão oficial (ligas rivais de 1912-1914, 1919-1926 e
1931-1934; Copa de Honor, Campeonato e Copa de Oro de 1936; Metropolitano e Nacional de 1967 a 1985; Apertura e Clausura
de 1991/92 a 2013/14 e de 2025) vira uma edição por torneio.

Ficam de fora, como na lista de campeões da RSSSF:
- as "copas da liga" (Copa de la Superliga 2019, Copa de la Liga Profesional 2020 a 2024): copas, não campeonatos;
- a Copa Campeonato 2013/14 (jogo entre os campeões do Inicial e do Final, que a AFA tratou como copa nacional);
- os torneios de reclassificação, de promoção e as liguillas pré-Libertadores (não davam título).
A tabela anual de 2025 (Rosario Central, "campeão da Liga" pela AFA em 20/11/2025) entra como edição sem jogos próprios
("2025 Liga"): a classificação é a tabela anual, conferida com a soma das fases de grupos do Apertura e do Clausura.

Cada edição diz onde estão os jogos: [(página da RSSSF, linha inicial, linha final)], com as linhas do texto puro
(rsssf_sul.texto). Linha final None: até o primeiro título de outra competição (FIM_PADRAO).
```

**Edições:** 196: 195 torneios que deram título de campeão argentino da 1ª divisão, de 1891 a 2025, como na lista de campeões da RSSSF (`argchamp.html`) e na Wikipédia em inglês (*List of Argentine football champions*): as duas trazem os mesmos 195 campeões. Ano com mais de um campeão oficial vira uma edição por torneio: ligas rivais (Asociación x Federación em 1912-1914, Asociación x Amateurs em 1919-1926, Liga profissional x Asociación amadora em 1931-1934), Copa de Honor, Copa Campeonato e Copa de Oro em 1936, Metropolitano e Nacional de 1967 a 1985, Apertura e Clausura de 1991/92 a 2011/12 e em 2025, Inicial, Final e o jogo do Campeonato 2012/13, mais a tabela anual de 2025.

**Tabela anual de 2025:** o Rosario Central foi proclamado "campeão da Liga" pela AFA em 20/11/2025. Entra como a edição "2025 Liga", sem jogos próprios (decisão do Guilherme, 20/11/2026): a classificação é a tabela anual da RSSSF, que fecha com a soma das fases de grupos do Apertura e do Clausura.

**Fontes:** RSSSF (uma página por temporada, `data/coleta/arg-1/rsssf/`: base de jogos, fases, grupos, rodadas, datas, local e autores dos gols; as tabelas da própria página e as dos índices por década, `arghist-*.html`, são a conferência); ogol (calendários de 1931 em diante, com muitos anos vazios: rodada e data que faltam, conferência de placar e o nome de cada clube no ogol); ESPN (liga `arg.1`, 2001 em diante: hora, estádio, público, gols com minuto e cartões); Wikipédia (lista de campeões, segunda fonte do campeão).

**Regras:** o placar é o da RSSSF; o ogol só completa rodada e data e entra como conferência. Jogo decidido no tribunal leva o placar dado (`awd`) ou, sem placar, a vitória (`wo`, com o placar de campo na observação). Jogo suspenso e repetido fica como `abd` e não conta; suspenso e continuado depois vira um jogo só. Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos por vitória: 2 até 1994/95 e 3 a partir do Apertura 1995 (em 1988/89, 3 pela vitória e 2 ou 1 no empate decidido nos pênaltis).

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 136.
- **Edições com alguma tabela divergente** (54; motivo no relatório, na edição): 1896, 1908, 1909, 1910, 1912 Federación, 1913 Asociación, 1913 Federación, 1915, 1919 Amateurs, 1921 Amateurs, 1922 Asociación, 1922 Amateurs, 1923 Amateurs, 1924 Asociación, 1924 Amateurs, 1925 Asociación, 1926 Asociación, 1927, 1928, 1929, 1930, 1931 Liga, 1931 Asociación, 1932 Asociación, 1934 Liga, 1934 Asociación, 1949, 1965, 1968 Metropolitano, 1970 Nacional, 1971 Nacional, 1972 Nacional, 1974 Metropolitano, 1982 Nacional, 1984 Metropolitano, 1984 Nacional, 1986/87, 1987/88, 1988/89, 1989/90, 1990/91, 1992/93 Clausura, 1995/96 Clausura, 1996/97 Apertura, 1996/97 Clausura, 1997/98 Apertura, 1998/99 Apertura, 1998/99 Clausura, 1999/00 Apertura, 2000/01 Apertura, 2001/02 Apertura, 2004/05 Clausura, 2016, 2016/17.
- **Edições sem tabela para conferir** (6): 1894, 1895, 1919 Asociación, 1923 Asociación, 1926 Amateurs, 1936 Copa de Oro.
- **Edições com menos jogos que o esperado:** 1893 (23 de 20), 1896 (22 de 20), 1905 (43 de 42), 1906 (51 de 52), 1907 (111 de 110), 1913 Asociación (138 de 139), 1913 Federación (92 de 90), 1915 (302 de 301), 1917 (211 de 210), 1918 (191 de 190), 1922 Amateurs (427 de 420), 1924 Amateurs (282 de 276), 1925 Asociación (237 de 235), 1925 Amateurs (301 de 300), 1927 (564 de 563), 1928 (631 de 630), 1930 (633 de 630), 1931 Liga (311 de 306), 1932 Liga (311 de 307), 1932 Asociación (276 de 275), 1933 Liga (307 de 306), 1934 Liga (276 de 273), 1939 (309 de 308), 1941 (241 de 240), 1955 (243 de 240), 1965 (306 de 305), 1977 Metropolitano (513 de 507), 1986/87 (382 de 381), 1995/96 Clausura (191 de 190), 1997/98 Apertura (189 de 190), 1999/00 Clausura (191 de 190), 2000/01 Apertura (194 de 190), 2001/02 Apertura (191 de 190), 2001/02 Clausura (191 de 190), 2002/03 Apertura (192 de 190), 2002/03 Clausura (191 de 190), 2003/04 Apertura (191 de 190), 2004/05 Clausura (191 de 190), 2005/06 Clausura (191 de 190), 2006/07 Apertura (194 de 191), 2006/07 Clausura (192 de 190), 2007/08 Apertura (191 de 190), 2007/08 Clausura (191 de 190), 2008/09 Apertura (194 de 193), 2008/09 Clausura (191 de 190), 2009/10 Clausura (194 de 190), 2010/11 Clausura (192 de 190), 2012/13 Inicial (191 de 190), 2012/13 Final (192 de 190), 2016 (242 de 483), 2016/17 (446 de 450).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1890s | 8 | 222 | 100% | 0% | 10% | 11% | 0% | 0% | 0% | 0.0 |
| 1900s | 10 | 491 | 100% | 0% | 18% | 9% | 0% | 0% | 2% | 0.0 |
| 1910s | 14 | 1770 | 100% | 0% | 45% | 9% | 0% | 0% | 1% | 0.0 |
| 1920s | 17 | 4841 | 92% | 0% | 93% | 12% | 0% | 0% | 21% | 0.0 |
| 1930s | 16 | 4186 | 100% | 0% | 86% | 10% | 0% | 7% | 19% | 0.0 |
| 1940s | 10 | 2539 | 100% | 0% | 100% | 7% | 0% | 0% | 0% | 0.0 |
| 1950s | 10 | 2510 | 100% | 0% | 100% | 7% | 0% | 0% | 0% | 0.0 |
| 1960s | 13 | 2934 | 100% | 0% | 100% | 8% | 0% | 0% | 8% | 0.0 |
| 1970s | 20 | 5595 | 100% | 0% | 100% | 15% | 0% | 0% | 31% | 0.0 |
| 1980s | 16 | 4713 | 100% | 0% | 100% | 25% | 0% | 0% | 0% | 0.0 |
| 1990s | 19 | 3803 | 100% | 0% | 100% | 17% | 0% | 0% | 28% | 0.0 |
| 2000s | 20 | 3829 | 100% | 77% | 100% | 49% | 48% | 12% | 98% | 2.7 |
| 2010s | 16 | 3833 | 100% | 78% | 100% | 79% | 79% | 0% | 79% | 4.3 |
| 2020s | 7 | 1969 | 100% | 94% | 100% | 100% | 100% | 0% | 100% | 5.2 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na América do Sul: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1891 a 1893: 5 clubes
- 1894: 7 clubes
- 1895: 6 clubes
- 1896: 5 clubes
- 1897 a 1898: 7 clubes
- 1899 a 1901: 4 clubes
- 1902: 5 clubes
- 1903 a 1904: 6 clubes
- 1905: 7 clubes
- 1906 a 1908: 11 clubes
- 1909: 10 clubes
- 1910 a 1911: 9 clubes
- 1912 Asociación: 10 clubes
- 1912 Federación: 8 clubes
- 1913 Asociación: 15 clubes
- 1913 Federación: 10 clubes
- 1914 Asociación: 14 clubes
- 1914 Federación: 10 clubes
- 1915: 25 clubes
- 1916: 22 clubes
- 1917: 21 clubes
- 1918 a 1919 Asociación: 20 clubes
- 1919 Amateurs: 14 clubes
- 1920 Asociación: 13 clubes
- 1920 Amateurs: 19 clubes
- 1921 Asociación: 11 clubes
- 1921 Amateurs: 21 clubes
- 1922 Asociación: 17 clubes
- 1922 Amateurs: 21 clubes
- 1923 Asociación: 23 clubes
- 1923 Amateurs: 21 clubes
- 1924 Asociación: 22 clubes
- 1924 Amateurs: 24 clubes
- 1925 Asociación: 23 clubes
- 1925 Amateurs: 25 clubes
- 1926 Asociación: 24 clubes
- 1926 Amateurs: 26 clubes
- 1927: 34 clubes
- 1928: 36 clubes
- 1929: 35 clubes
- 1930: 36 clubes
- 1931 Liga: 18 clubes
- 1931 Asociación: 17 clubes
- 1932 Liga: 18 clubes
- 1932 Asociación: 17 clubes
- 1933 Liga: 18 clubes
- 1933 Asociación: 20 clubes
- 1934 Liga: 14 clubes
- 1934 Asociación: 23 clubes
- 1935 a 1936 Campeonato: 18 clubes
- 1936 Copa de Oro: 2 clubes
- 1937: 18 clubes
- 1938: 17 clubes
- 1939 a 1940: 18 clubes
- 1941 a 1948: 16 clubes
- 1949 a 1950: 18 clubes
- 1951: 17 clubes
- 1952 a 1961: 16 clubes
- 1962: 15 clubes
- 1963: 14 clubes
- 1964: 16 clubes
- 1965: 18 clubes
- 1966: 20 clubes
- 1967 Metropolitano: 22 clubes
- 1967 Nacional: 16 clubes
- 1968 Metropolitano: 22 clubes
- 1968 Nacional: 16 clubes
- 1969 Metropolitano: 22 clubes
- 1969 Nacional: 18 clubes
- 1970 Metropolitano: 21 clubes
- 1970 Nacional: 20 clubes
- 1971 Metropolitano: 19 clubes
- 1971 Nacional: 28 clubes
- 1972 Metropolitano: 18 clubes
- 1972 Nacional: 26 clubes
- 1973 Metropolitano: 17 clubes
- 1973 Nacional: 30 clubes
- 1974 Metropolitano: 18 clubes
- 1974 Nacional: 36 clubes
- 1975 Metropolitano: 20 clubes
- 1975 Nacional: 32 clubes
- 1976 Metropolitano: 22 clubes
- 1976 Nacional: 34 clubes
- 1977 Metropolitano: 23 clubes
- 1977 Nacional: 32 clubes
- 1978 Metropolitano: 21 clubes
- 1978 Nacional: 32 clubes
- 1979 Metropolitano: 20 clubes
- 1979 Nacional: 28 clubes
- 1980 Metropolitano: 19 clubes
- 1980 Nacional: 28 clubes
- 1981 Metropolitano: 18 clubes
- 1981 Nacional: 28 clubes
- 1982 Metropolitano: 19 clubes
- 1982 Nacional: 32 clubes
- 1983 Metropolitano: 19 clubes
- 1983 Nacional: 32 clubes
- 1984 Metropolitano: 19 clubes
- 1984 Nacional a 1985 Nacional: 32 clubes
- 1985/86: 19 clubes
- 1986/87 a 2012/13 Final: 20 clubes
- 2012/13 Campeonato: 2 clubes
- 2013/14 Inicial a 2014: 20 clubes
- 2015 a 2016/17: 30 clubes
- 2017/18: 28 clubes
- 2018/19: 26 clubes
- 2019/20: 24 clubes
- 2021: 26 clubes
- 2022 a 2024: 28 clubes
- 2025 Apertura a 2025 Liga: 30 clubes

**Pontos por vitória:**

- 1891 a 1987/88: 2
- 1988/89: 3
- 1989/90 a 1994/95 Clausura: 2
- 1995/96 Apertura a 2025 Liga: 3

**Nome oficial:**

- 1891: Argentine Association Football League <ano>
- 1893 a 1905: Championship <ano>
- 1906 a 1911: Campeonato <ano>
- 1912 Asociación: Asociación Argentina de Football – Copa Campeonato <ano>
- 1912 Federación: Federación Argentina de Football – Campeonato <ano>
- 1913 Asociación: Asociación Argentina de Football – Copa Campeonato <ano>
- 1913 Federación: Federación Argentina de Football – Primera División <ano>
- 1914 Asociación: Asociación Argentina de Football – Copa Campeonato <ano>
- 1914 Federación: Federación Argentina de Football – Primera División <ano>
- 1915 a 1918: Copa Campeonato <ano>
- 1919 Asociación: Asociación Argentina de Football – Copa Campeonato <ano>
- 1919 Amateurs: Asociación Amateurs de Football – Primera División <ano>
- 1920 Asociación: Asociación Argentina de Football – Copa Campeonato <ano>
- 1920 Amateurs: Asociación Amateurs de Football – Primera División <ano>
- 1921 Asociación: Asociación Argentina de Football – Copa Campeonato <ano>
- 1921 Amateurs: Asociación Amateurs de Football – Primera División <ano>
- 1922 Asociación: Asociación Argentina de Football – Copa Campeonato <ano>
- 1922 Amateurs: Asociación Amateurs de Football – Primera División <ano>
- 1923 Asociación: Asociación Argentina de Football – Copa Campeonato <ano>
- 1923 Amateurs: Asociación Amateurs de Football – Primera División <ano>
- 1924 Asociación: Asociación Argentina de Football – Campeonato <ano>
- 1924 Amateurs: Asociación Amateurs de Football – Primera División <ano>
- 1925 Asociación: Asociación Argentina de Football – Copa Campeonato <ano>
- 1925 Amateurs: Asociación Amateurs de Football – Primera División <ano>
- 1926 Asociación: Asociación Argentina de Football – Copa Campeonato <ano>
- 1926 Amateurs: Asociación Amateurs de Football – Primera División <ano>
- 1927 a 1928: Asociación Amateurs Argentina de Football – Primera División <ano>
- 1929: Campeonato Estímulo <ano>
- 1930: Asociación Amateurs Argentina de Football – Primera División <ano>
- 1931 Liga: Liga Argentina de Football – Campeonato <ano>
- 1931 Asociación: Asociación Argentina de Football (Amateurs y Profesionales) – Copa Campeonato <ano>
- 1932 Liga: Liga Argentina de Football – Campeonato <ano>
- 1932 Asociación: Asociación Argentina de Football – Primera División <ano>
- 1933 Liga: Liga Argentina de Football – Campeonato <ano>
- 1933 Asociación: Asociación Argentina de Football – Primera División <ano>
- 1934 Liga: Liga Argentina de Football – Campeonato <ano>
- 1934 Asociación: Asociación Argentina de Football – Primera División <ano>
- 1935: Campeonato de Primera División <ano>
- 1936 Copa de Honor: Copa de Honor Municipalidad de Buenos Aires <ano>
- 1936 Campeonato: Copa Campeonato <ano>
- 1936 Copa de Oro: Copa de Oro <ano>
- 1937 a 1966: Campeonato de Primera División <ano>
- 1967 Metropolitano: Campeonato Metropolitano <ano>
- 1967 Nacional: Campeonato Nacional <ano>
- 1968 Metropolitano: Campeonato Metropolitano <ano>
- 1968 Nacional: Campeonato Nacional <ano>
- 1969 Metropolitano: Campeonato Metropolitano <ano>
- 1969 Nacional: Campeonato Nacional <ano>
- 1970 Metropolitano: Campeonato Metropolitano <ano>
- 1970 Nacional: Campeonato Nacional <ano>
- 1971 Metropolitano: Campeonato Metropolitano <ano>
- 1971 Nacional: Campeonato Nacional <ano>
- 1972 Metropolitano: Campeonato Metropolitano <ano>
- 1972 Nacional: Campeonato Nacional <ano>
- 1973 Metropolitano: Campeonato Metropolitano <ano>
- 1973 Nacional: Campeonato Nacional <ano>
- 1974 Metropolitano: Campeonato Metropolitano <ano>
- 1974 Nacional: Campeonato Nacional <ano>
- 1975 Metropolitano: Campeonato Metropolitano <ano>
- 1975 Nacional: Campeonato Nacional <ano>
- 1976 Metropolitano: Campeonato Metropolitano <ano>
- 1976 Nacional: Campeonato Nacional <ano>
- 1977 Metropolitano: Campeonato Metropolitano <ano>
- 1977 Nacional: Campeonato Nacional <ano>
- 1978 Metropolitano: Campeonato Metropolitano <ano>
- 1978 Nacional: Campeonato Nacional <ano>
- 1979 Metropolitano: Campeonato Metropolitano <ano>
- 1979 Nacional: Campeonato Nacional <ano>
- 1980 Metropolitano: Campeonato de Primera División <ano> (Metropolitano)
- 1980 Nacional: Campeonato Nacional <ano>
- 1981 Metropolitano: Campeonato de Primera División <ano> (Metropolitano)
- 1981 Nacional: Campeonato Nacional <ano>
- 1982 Metropolitano: Campeonato de Primera División <ano> (Metropolitano)
- 1982 Nacional: Campeonato Nacional <ano>
- 1983 Metropolitano: Campeonato de Primera División <ano> (Metropolitano)
- 1983 Nacional: Campeonato Nacional <ano>
- 1984 Metropolitano: Campeonato de Primera División <ano> (Metropolitano)
- 1984 Nacional a 1985 Nacional: Campeonato Nacional <ano>
- 1985/86 a 1990/91: Campeonato de Primera División <ano>
- 1991/92 Apertura: Torneo Apertura <ano>
- 1991/92 Clausura: Torneo Clausura <ano>
- 1992/93 Apertura: Torneo Apertura <ano>
- 1992/93 Clausura: Torneo Clausura <ano>
- 1993/94 Apertura: Torneo Apertura <ano>
- 1993/94 Clausura: Torneo Clausura <ano>
- 1994/95 Apertura: Torneo Apertura <ano>
- 1994/95 Clausura: Torneo Clausura <ano>
- 1995/96 Apertura: Torneo Apertura <ano>
- 1995/96 Clausura: Torneo Clausura <ano>
- 1996/97 Apertura: Torneo Apertura <ano>
- 1996/97 Clausura: Torneo Clausura <ano>
- 1997/98 Apertura: Torneo Apertura <ano>
- 1997/98 Clausura: Torneo Clausura <ano>
- 1998/99 Apertura: Torneo Apertura <ano>
- 1998/99 Clausura: Torneo Clausura <ano>
- 1999/00 Apertura: Torneo Apertura <ano>
- 1999/00 Clausura: Torneo Clausura <ano>
- 2000/01 Apertura: Torneo Apertura <ano>
- 2000/01 Clausura: Torneo Clausura <ano>
- 2001/02 Apertura: Torneo Apertura <ano>
- 2001/02 Clausura: Torneo Clausura <ano>
- 2002/03 Apertura: Torneo Apertura <ano>
- 2002/03 Clausura: Torneo Clausura <ano>
- 2003/04 Apertura: Torneo Apertura <ano>
- 2003/04 Clausura: Torneo Clausura <ano>
- 2004/05 Apertura: Torneo Apertura <ano>
- 2004/05 Clausura: Torneo Clausura <ano>
- 2005/06 Apertura: Torneo Apertura <ano>
- 2005/06 Clausura: Torneo Clausura <ano>
- 2006/07 Apertura: Torneo Apertura <ano>
- 2006/07 Clausura: Torneo Clausura <ano>
- 2007/08 Apertura: Torneo Apertura <ano>
- 2007/08 Clausura: Torneo Clausura <ano>
- 2008/09 Apertura: Torneo Apertura <ano>
- 2008/09 Clausura: Torneo Clausura <ano>
- 2009/10 Apertura: Torneo Apertura <ano>
- 2009/10 Clausura: Torneo Clausura <ano>
- 2010/11 Apertura: Torneo Apertura <ano>
- 2010/11 Clausura: Torneo Clausura <ano>
- 2011/12 Apertura: Torneo Apertura <ano>
- 2011/12 Clausura: Torneo Clausura <ano>
- 2012/13 Inicial: Torneo Inicial <ano>
- 2012/13 Final: Torneo Final <ano>
- 2012/13 Campeonato: Campeonato de Primera División <ano>
- 2013/14 Inicial: Torneo Inicial <ano>
- 2013/14 Final: Torneo Final <ano>
- 2014 a 2016/17: Campeonato de Primera División <ano>
- 2017/18 a 2019/20: Superliga Argentina <ano>
- 2021 a 2024: Torneo de la Liga Profesional de Fútbol <ano>
- 2025 Apertura: Torneo Apertura <ano>
- 2025 Clausura: Torneo Clausura <ano>
- 2025 Liga: Tabla Anual de la LPF <ano> (Campeón de Liga)

**Formato** (fases na ordem, do edicoes.csv):

- 1891: pontos corridos + desempate
- 1893 a 1896: pontos corridos
- 1897 a 1898: pontos corridos + desempate
- 1899 a 1905: pontos corridos
- 1906: 2 grupos + mata-mata
- 1907 a 1910: pontos corridos
- 1911: pontos corridos + desempate
- 1912 Asociación: pontos corridos
- 1912 Federación: pontos corridos + desempate
- 1913 Asociación: 3 grupos + mata-mata
- 1913 Federación a 1914 Federación: pontos corridos
- 1915: pontos corridos + desempate
- 1916 a 1924 Amateurs: pontos corridos
- 1925 Asociación: pontos corridos + desempate
- 1925 Amateurs a 1926 Amateurs: pontos corridos
- 1927: pontos corridos + desempate
- 1928: pontos corridos
- 1929: 2 grupos + desempate + mata-mata
- 1930 a 1931 Liga: pontos corridos
- 1931 Asociación: desempate
- 1932 Liga a 1932 Asociación: pontos corridos + desempate
- 1933 Liga a 1936 Campeonato: pontos corridos
- 1936 Copa de Oro: mata-mata
- 1937: pontos corridos + desempate
- 1938: pontos corridos
- 1939: pontos corridos + desempate
- 1940 a 1948: pontos corridos
- 1949 a 1951: pontos corridos + desempate
- 1952 a 1957: pontos corridos
- 1958: pontos corridos + desempate
- 1959 a 1966: pontos corridos
- 1967 Metropolitano: 2 grupos + mata-mata
- 1967 Nacional: pontos corridos
- 1968 Metropolitano: 2 grupos + mata-mata
- 1968 Nacional: pontos corridos + desempate
- 1969 Metropolitano: 2 grupos + mata-mata
- 1969 Nacional: pontos corridos + desempate
- 1970 Metropolitano: pontos corridos
- 1970 Nacional: 2 grupos + mata-mata
- 1971 Metropolitano: pontos corridos
- 1971 Nacional: 2 grupos + mata-mata
- 1972 Metropolitano: pontos corridos
- 1972 Nacional: 2 grupos + mata-mata
- 1973 Metropolitano: pontos corridos
- 1973 Nacional: 2 grupos + mata-mata
- 1974 Metropolitano: 2 grupos + pontos corridos
- 1974 Nacional: 4 grupos + pontos corridos
- 1975 Metropolitano: pontos corridos
- 1975 Nacional: 4 grupos + pontos corridos
- 1976 Metropolitano: 2 grupos + pontos corridos
- 1976 Nacional: 4 grupos + mata-mata + desempate + mata-mata
- 1977 Metropolitano: pontos corridos + desempate
- 1977 Nacional: 4 grupos + mata-mata
- 1978 Metropolitano: pontos corridos
- 1978 Nacional: 4 grupos + mata-mata
- 1979 Metropolitano: 2 grupos + mata-mata + desempate + mata-mata
- 1979 Nacional: 4 grupos + mata-mata
- 1980 Metropolitano: pontos corridos
- 1980 Nacional: 4 grupos + mata-mata
- 1981 Metropolitano: pontos corridos
- 1981 Nacional: 4 grupos + mata-mata
- 1982 Metropolitano: pontos corridos + desempate
- 1982 Nacional: 4 grupos + mata-mata
- 1983 Metropolitano: pontos corridos
- 1983 Nacional: 8 grupos + mata-mata
- 1984 Metropolitano: pontos corridos
- 1984 Nacional a 1985 Nacional: 8 grupos + mata-mata
- 1985/86: pontos corridos
- 1986/87 a 1987/88: pontos corridos + desempate
- 1988/89: pontos corridos
- 1989/90: pontos corridos + desempate
- 1990/91: pontos corridos + mata-mata
- 1991/92 Apertura a 2005/06 Clausura: pontos corridos
- 2006/07 Apertura: pontos corridos + desempate
- 2006/07 Clausura a 2007/08 Clausura: pontos corridos
- 2008/09 Apertura: pontos corridos + desempate
- 2008/09 Clausura a 2015: pontos corridos
- 2016: 2 grupos + mata-mata
- 2016/17 a 2024: pontos corridos
- 2025 Apertura a 2025 Clausura: 2 grupos + mata-mata
- 2025 Liga: tabela anual (soma das fases de grupos do Apertura e do Clausura)

**Fases e grupos de cada edição com mais de uma fase:**

- 1891: Fase única (liga); Desempate do título (mata_mata, jogo_unico)
- 1897: Fase única (liga); Desempate do título (mata_mata, ida_volta)
- 1898: Fase única (liga); Desempate do título (mata_mata, ida_volta)
- 1906: Primeira fase (grupos, 2 grupos); Final (mata_mata, jogo_unico)
- 1911: Fase única (liga); Desempate do título (mata_mata, jogo_unico)
- 1912 Federación: Fase única (liga); Desempate do título (mata_mata, ida_volta)
- 1913 Asociación: Primeira fase (grupos, 3 grupos); Final (mata_mata, jogo_unico)
- 1915: Fase única (liga); Desempate do título (mata_mata, jogo_unico)
- 1925 Asociación: Fase única (liga); Desempate do título (mata_mata, jogo_unico)
- 1927: Fase única (liga); Desempate do rebaixamento (mata_mata, ida_volta)
- 1929: Primeira fase (grupos, 2 grupos); Desempate do título (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 1932 Liga: Fase única (liga); Desempate do título (mata_mata, jogo_unico)
- 1932 Asociación: Fase única (liga); Desempate do rebaixamento (mata_mata, ida_volta)
- 1937: Fase única (liga); Desempate do título (mata_mata, jogo_unico)
- 1939: Fase única (liga); Desempate do 2º lugar (mata_mata, jogo_unico); Desempate do título (mata_mata, jogo_unico)
- 1949: Fase única (liga); Desempate do rebaixamento (mata_mata, ida_volta); Desempate do 2º lugar (mata_mata, ida_volta)
- 1950: Fase única (liga); Desempate do rebaixamento (mata_mata, ida_volta); Desempate do 2º lugar (mata_mata, ida_volta)
- 1951: Fase única (liga); Desempate do título (mata_mata, ida_volta)
- 1958: Fase única (liga); Desempate do 2º lugar (mata_mata, ida_volta)
- 1967 Metropolitano: Primeira fase (grupos, 2 grupos); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1968 Metropolitano: Primeira fase (grupos, 2 grupos); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1968 Nacional: Fase única (liga); Desempate do título (mata_mata, jogo_unico)
- 1969 Metropolitano: Primeira fase (grupos, 2 grupos); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1969 Nacional: Fase única (liga); Desempate do rebaixamento (mata_mata, ida_volta)
- 1970 Nacional: Primeira fase (grupos, 2 grupos); Semifinal (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 1971 Nacional: Primeira fase (grupos, 2 grupos); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1972 Nacional: Primeira fase (grupos, 2 grupos); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1973 Nacional: Primeira fase (grupos, 2 grupos); Final (mata_mata, jogo_unico)
- 1974 Metropolitano: Primeira fase (grupos, 2 grupos); Fase final (liga)
- 1974 Nacional: Primeira fase (grupos, 4 grupos); Fase final (liga)
- 1975 Nacional: Primeira fase (grupos, 4 grupos); Fase final (liga)
- 1976 Metropolitano: Primeira fase (grupos, 2 grupos); Grupo do rebaixamento (liga); Fase final (liga)
- 1976 Nacional: Primeira fase (grupos, 4 grupos); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Desempate do título (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1977 Metropolitano: Fase única (liga); Desempate do rebaixamento (mata_mata, jogo_unico)
- 1977 Nacional: Primeira fase (grupos, 4 grupos); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1978 Nacional: Primeira fase (grupos, 4 grupos); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1979 Metropolitano: Primeira fase (grupos, 2 grupos); Semifinal (mata_mata, ida_volta); Desempate do título (mata_mata, jogo_unico); Final (mata_mata, ida_volta)
- 1979 Nacional: Primeira fase (grupos, 4 grupos); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1980 Nacional: Primeira fase (grupos, 4 grupos); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1981 Nacional: Primeira fase (grupos, 4 grupos); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1982 Metropolitano: Fase única (liga); Desempate do rebaixamento (mata_mata, jogo_unico)
- 1982 Nacional: Primeira fase (grupos, 4 grupos); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1983 Nacional: Primeira fase (grupos, 8 grupos); Oitavas de final (mata_mata, ida_volta); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1984 Nacional: Primeira fase (grupos, 8 grupos); Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 1985 Nacional: Primeira fase (grupos, 8 grupos); Final (mata_mata, ida_volta)
- 1986/87: Fase única (liga); Desempate do rebaixamento (mata_mata, jogo_unico)
- 1987/88: Fase única (liga); Desempate do rebaixamento (mata_mata, jogo_unico)
- 1989/90: Fase única (liga); Desempate do rebaixamento (mata_mata, jogo_unico)
- 1990/91: Apertura (liga); Clausura (liga); Final (mata_mata, ida_volta)
- 2006/07 Apertura: Fase única (liga); Desempate do título (mata_mata, jogo_unico)
- 2008/09 Apertura: Fase única (liga); Desempate do título (mata_mata, jogo_unico)
- 2016: Primeira fase (grupos, 2 grupos); Final (mata_mata, jogo_unico)
- 2025 Apertura: Primeira fase (grupos, 2 grupos); Oitavas de final (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2025 Clausura: Primeira fase (grupos, 2 grupos); Oitavas de final (mata_mata, jogo_unico); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 115 edições
- calculada: 81 edições

**Observações das edições:**

- 1891: título dividido entre Saint Andrew's e Caledonians pela liga da época; a AFA só cita o Saint Andrew's (RSSSF)
- 1931 Asociación: o campeonato da Asociación Amateurs, começado antes da saída dos clubes profissionais, foi anulado e recomeçado
- 1934 Liga: a Liga e a Asociación se fundiram em 3/11/1934, com o campeonato em andamento
- 1936 Copa de Honor: título de Primera División reconhecido pela AFA em 4/7/2013
- 1936 Copa de Oro: jogo entre os campeões da Copa de Honor e da Copa Campeonato; título reconhecido pela AFA em 4/7/2013
- 1988/89: empate decidido nos pênaltis: 2 pontos para o vencedor e 1 para o perdedor; vitória no tempo normal, 3 pontos
- 1990/91: Apertura 1990 (Newell's) e Clausura 1991 (Boca) eram fases; o título saiu da final entre os dois
- 2012/13 Campeonato: jogo único entre os campeões do Inicial (Vélez Sarsfield) e do Final (Newell's Old Boys)
- 2019/20: campeonato de 23 rodadas; a temporada parou na pandemia durante a Copa de la Superliga (fora do pacote)
- 2025 Liga: título dado pela AFA em 20/11/2025 ao 1º da tabela anual (soma das fases de grupos do Apertura e do Clausura); sem jogos próprios: os jogos estão nas edições 2025 Apertura e 2025 Clausura

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- River Plate: 38
- Boca Juniors: 35
- Racing Club: 18
- Independiente: 16
- San Lorenzo: 15
- Vélez Sarsfield: 11
- Alumni: 10
- Estudiantes: 7
- Newell's Old Boys: 6
- Lomas Athletic: 5
- Huracán: 5
- Rosario Central: 5
- Belgrano Athletic: 3
- Argentinos Juniors: 3
- Quilmes: 2
- Porteño: 2
- Estudiantil Porteño: 2
- Ferro Carril Oeste: 2
- Lanús: 2
- Saint Andrew's: 1
- Lomas Academicals: 1
- Gimnasia La Plata: 1
- Sportivo Barracas: 1
- Sportivo Dock Sud: 1
- Chacarita Juniors: 1
- Banfield: 1
- Arsenal de Sarandí: 1
- Platense: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1891 | Saint Andrew's | Caledonians |
| 1893 | Lomas Athletic | Flores Athletic |
| 1894 | Lomas Athletic | Rosario Athletic |
| 1895 | Lomas Athletic | Flores Athletic |
| 1896 | Lomas Academicals | Lomas Athletic |
| 1897 | Lomas Athletic | Lanús Athletic |
| 1898 | Lomas Athletic | Lobos Athletic |
| 1899 | Belgrano Athletic | Lobos Athletic |
| 1900 | Alumni | Lomas Athletic |
| 1901 | Alumni | Belgrano Athletic |
| 1902 | Alumni | Barracas Athletic |
| 1903 | Alumni | Belgrano Athletic |
| 1904 | Belgrano Athletic | Alumni |
| 1905 | Alumni | Belgrano Athletic |
| 1906 | Alumni | Lomas Athletic |
| 1907 | Alumni | Estudiantes de Buenos Aires |
| 1908 | Belgrano Athletic | Alumni |
| 1909 | Alumni | River Plate |
| 1910 | Alumni | Porteño |
| 1911 | Alumni | Porteño |
| 1912 Asociación | Quilmes | Racing Club |
| 1912 Federación | Porteño | Independiente |
| 1913 Asociación | Racing Club | San Isidro |
| 1913 Federación | Estudiantes | Argentino de Quilmes |
| 1914 Asociación | Racing Club | Estudiantes de Buenos Aires |
| 1914 Federación | Porteño | Estudiantes |
| 1915 | Racing Club | San Isidro |
| 1916 | Racing Club | Platense |
| 1917 | Racing Club | River Plate |
| 1918 | Racing Club | River Plate |
| 1919 Asociación | Boca Juniors | Independiente |
| 1919 Amateurs | Racing Club | Atlanta |
| 1920 Asociación | Boca Juniors | Banfield |
| 1920 Amateurs | River Plate | Racing Club |
| 1921 Asociación | Huracán | Del Plata |
| 1921 Amateurs | Racing Club | River Plate |
| 1922 Asociación | Huracán | Sportivo Palermo |
| 1922 Amateurs | Independiente | River Plate |
| 1923 Asociación | Boca Juniors | Huracán |
| 1923 Amateurs | San Lorenzo | Independiente |
| 1924 Asociación | Boca Juniors | Temperley |
| 1924 Amateurs | San Lorenzo | Gimnasia La Plata |
| 1925 Asociación | Huracán | Nueva Chicago |
| 1925 Amateurs | Racing Club | San Lorenzo |
| 1926 Asociación | Boca Juniors | Huracán |
| 1926 Amateurs | Independiente | Lanús |
| 1927 | San Lorenzo | Boca Juniors |
| 1928 | Huracán | Boca Juniors |
| 1929 | Gimnasia La Plata | Boca Juniors |
| 1930 | Boca Juniors | Estudiantes |
| 1931 Liga | Boca Juniors | San Lorenzo |
| 1931 Asociación | Estudiantil Porteño | Almagro |
| 1932 Liga | River Plate | Independiente |
| 1932 Asociación | Sportivo Barracas | Barracas Central |
| 1933 Liga | San Lorenzo | Boca Juniors |
| 1933 Asociación | Sportivo Dock Sud | Nueva Chicago |
| 1934 Liga | Boca Juniors | Independiente |
| 1934 Asociación | Estudiantil Porteño | Banfield |
| 1935 | Boca Juniors | Independiente |
| 1936 Copa de Honor | San Lorenzo | Huracán |
| 1936 Campeonato | River Plate | San Lorenzo |
| 1936 Copa de Oro | River Plate | San Lorenzo |
| 1937 | River Plate | Independiente |
| 1938 | Independiente | River Plate |
| 1939 | Independiente | River Plate |
| 1940 | Boca Juniors | Independiente |
| 1941 | River Plate | San Lorenzo |
| 1942 | River Plate | San Lorenzo |
| 1943 | Boca Juniors | River Plate |
| 1944 | Boca Juniors | River Plate |
| 1945 | River Plate | Boca Juniors |
| 1946 | San Lorenzo | Boca Juniors |
| 1947 | River Plate | Boca Juniors |
| 1948 | Independiente | River Plate |
| 1949 | Racing Club | River Plate |
| 1950 | Racing Club | Boca Juniors |
| 1951 | Racing Club | Banfield |
| 1952 | River Plate | Racing Club |
| 1953 | River Plate | Vélez Sarsfield |
| 1954 | Boca Juniors | Independiente |
| 1955 | River Plate | Racing Club |
| 1956 | River Plate | Lanús |
| 1957 | River Plate | San Lorenzo |
| 1958 | Racing Club | Boca Juniors |
| 1959 | San Lorenzo | Racing Club |
| 1960 | Independiente | River Plate |
| 1961 | Racing Club | San Lorenzo |
| 1962 | Boca Juniors | River Plate |
| 1963 | Independiente | River Plate |
| 1964 | Boca Juniors | Independiente |
| 1965 | Boca Juniors | River Plate |
| 1966 | Racing Club | River Plate |
| 1967 Metropolitano | Estudiantes | Racing Club |
| 1967 Nacional | Independiente | Estudiantes |
| 1968 Metropolitano | San Lorenzo | Estudiantes |
| 1968 Nacional | Vélez Sarsfield | River Plate |
| 1969 Metropolitano | Chacarita Juniors | River Plate |
| 1969 Nacional | Boca Juniors | River Plate |
| 1970 Metropolitano | Independiente | River Plate |
| 1970 Nacional | Boca Juniors | Rosario Central |
| 1971 Metropolitano | Independiente | Vélez Sarsfield |
| 1971 Nacional | Rosario Central | San Lorenzo |
| 1972 Metropolitano | San Lorenzo | Racing Club |
| 1972 Nacional | San Lorenzo | River Plate |
| 1973 Metropolitano | Huracán | Boca Juniors |
| 1973 Nacional | Rosario Central | River Plate |
| 1974 Metropolitano | Newell's Old Boys | Rosario Central |
| 1974 Nacional | San Lorenzo | Rosario Central |
| 1975 Metropolitano | River Plate | Huracán |
| 1975 Nacional | River Plate | Estudiantes |
| 1976 Metropolitano | Boca Juniors | Huracán |
| 1976 Nacional | Boca Juniors | Talleres |
| 1977 Metropolitano | River Plate | Independiente |
| 1977 Nacional | Independiente | Talleres |
| 1978 Metropolitano | Quilmes | Boca Juniors |
| 1978 Nacional | Independiente | River Plate |
| 1979 Metropolitano | River Plate | Vélez Sarsfield |
| 1979 Nacional | River Plate | Unión |
| 1980 Metropolitano | River Plate | Argentinos Juniors |
| 1980 Nacional | Rosario Central | Racing de Córdoba |
| 1981 Metropolitano | Boca Juniors | Ferro Carril Oeste |
| 1981 Nacional | River Plate | Ferro Carril Oeste |
| 1982 Metropolitano | Estudiantes | Independiente |
| 1982 Nacional | Ferro Carril Oeste | Quilmes |
| 1983 Metropolitano | Independiente | San Lorenzo |
| 1983 Nacional | Estudiantes | Independiente |
| 1984 Metropolitano | Argentinos Juniors | Ferro Carril Oeste |
| 1984 Nacional | Ferro Carril Oeste | River Plate |
| 1985 Nacional | Argentinos Juniors | Vélez Sarsfield |
| 1985/86 | River Plate | Newell's Old Boys |
| 1986/87 | Rosario Central | Newell's Old Boys |
| 1987/88 | Newell's Old Boys | Racing Club |
| 1988/89 | Independiente | Boca Juniors |
| 1989/90 | River Plate | Rosario Central |
| 1990/91 | Newell's Old Boys | Boca Juniors |
| 1991/92 Apertura | River Plate | Boca Juniors |
| 1991/92 Clausura | Newell's Old Boys | Vélez Sarsfield |
| 1992/93 Apertura | Boca Juniors | River Plate |
| 1992/93 Clausura | Vélez Sarsfield | Independiente |
| 1993/94 Apertura | River Plate | Vélez Sarsfield |
| 1993/94 Clausura | Independiente | Huracán |
| 1994/95 Apertura | River Plate | San Lorenzo |
| 1994/95 Clausura | San Lorenzo | Gimnasia La Plata |
| 1995/96 Apertura | Vélez Sarsfield | Racing Club |
| 1995/96 Clausura | Vélez Sarsfield | Gimnasia La Plata |
| 1996/97 Apertura | River Plate | Independiente |
| 1996/97 Clausura | River Plate | Colón |
| 1997/98 Apertura | River Plate | Boca Juniors |
| 1997/98 Clausura | Vélez Sarsfield | Lanús |
| 1998/99 Apertura | Boca Juniors | Gimnasia La Plata |
| 1998/99 Clausura | Boca Juniors | River Plate |
| 1999/00 Apertura | River Plate | Rosario Central |
| 1999/00 Clausura | River Plate | Independiente |
| 2000/01 Apertura | Boca Juniors | River Plate |
| 2000/01 Clausura | San Lorenzo | River Plate |
| 2001/02 Apertura | Racing Club | River Plate |
| 2001/02 Clausura | River Plate | Gimnasia La Plata |
| 2002/03 Apertura | Independiente | Boca Juniors |
| 2002/03 Clausura | River Plate | Boca Juniors |
| 2003/04 Apertura | Boca Juniors | San Lorenzo |
| 2003/04 Clausura | River Plate | Boca Juniors |
| 2004/05 Apertura | Newell's Old Boys | Vélez Sarsfield |
| 2004/05 Clausura | Vélez Sarsfield | Banfield |
| 2005/06 Apertura | Boca Juniors | Gimnasia La Plata |
| 2005/06 Clausura | Boca Juniors | Lanús |
| 2006/07 Apertura | Estudiantes | Boca Juniors |
| 2006/07 Clausura | San Lorenzo | Boca Juniors |
| 2007/08 Apertura | Lanús | Tigre |
| 2007/08 Clausura | River Plate | Boca Juniors |
| 2008/09 Apertura | Boca Juniors | San Lorenzo |
| 2008/09 Clausura | Vélez Sarsfield | Huracán |
| 2009/10 Apertura | Banfield | Newell's Old Boys |
| 2009/10 Clausura | Argentinos Juniors | Estudiantes |
| 2010/11 Apertura | Estudiantes | Vélez Sarsfield |
| 2010/11 Clausura | Vélez Sarsfield | Lanús |
| 2011/12 Apertura | Boca Juniors | Racing Club |
| 2011/12 Clausura | Arsenal de Sarandí | Tigre |
| 2012/13 Inicial | Vélez Sarsfield | Newell's Old Boys |
| 2012/13 Final | Newell's Old Boys | River Plate |
| 2012/13 Campeonato | Vélez Sarsfield | Newell's Old Boys |
| 2013/14 Inicial | San Lorenzo | Lanús |
| 2013/14 Final | River Plate | Boca Juniors |
| 2014 | Racing Club | River Plate |
| 2015 | Boca Juniors | San Lorenzo |
| 2016 | Lanús | San Lorenzo |
| 2016/17 | Boca Juniors | River Plate |
| 2017/18 | Boca Juniors | Godoy Cruz |
| 2018/19 | Racing Club | Defensa y Justicia |
| 2019/20 | Boca Juniors | River Plate |
| 2021 | River Plate | Defensa y Justicia |
| 2022 | Boca Juniors | Racing Club |
| 2023 | River Plate | Talleres |
| 2024 | Vélez Sarsfield | Talleres |
| 2025 Apertura | Platense | Huracán |
| 2025 Clausura | Estudiantes | Racing Club |
| 2025 Liga | Rosario Central | Boca Juniors |

**Rebaixados marcados na classificação:** 36 em 17 edições (só onde a tabela publicada marca a queda); quem mais caiu: Quilmes (4), Platense (3), Banfield (2), Ferro Carril Oeste (2), Argentino de Quilmes (2).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1906: Barracas Athletic -2
- 1941: Banfield -16
- 1948: Racing Club -4
- 1958: River Plate -2
- 1969 Nacional: Unión -2
- 1972 Metropolitano: Banfield -21
- 1978 Metropolitano: Huracán +1
- 1991/92 Clausura: Quilmes -2
- 1992/93 Apertura: River Plate -2
- 1992/93 Apertura: San Martín de Tucumán -2
- 1994/95 Apertura: Talleres -2
- 1997/98 Clausura: Independiente -3
- 1999/00 Clausura: Boca Juniors -3
- 1999/00 Clausura: Lanús -3
- 2000/01 Clausura: Los Andes -3
- 2003/04 Apertura: Chacarita Juniors -3
- 2013/14 Inicial: Colón -6
- 2017/18: Newell's Old Boys -1
- 2017/18: Arsenal de Sarandí -2
- 2017/18: Olimpo -1

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/arg-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 1)

- **arg66 · 396:** «0 6 Racing» → «0:6 Racing»: placar sem os dois-pontos ('0 6'); 0-6 fecha com a tabela publicada

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 2)

- **1936 Copa de Oro · arg-oro36:17:** [descartado] a linha do texto corrido vira o jogo escrito à mão (EXTRAS), com data, local e autores dos gols
- **1965 · arg65:198:** [abandonado] Independiente 2-2 Racing Club suspenso aos 68' e não continuado; a tabela publicada não conta o jogo (33 jogos para os dois)

### Jogos acrescentados à mão (a página traz em texto corrido) (`EXTRAS`, 1)

- **1936 Copa de Oro:** River Plate 4-2 San Lorenzo (Final, rsssf:arg-oro36:9) jogo único; o 2-1 de Bernabé Ferreyra desviou em Chividini; o 3-2 é de Cavadini (outras fontes: Canteli)

### Divergências entre fontes já explicadas (`EXPLICACOES`, 2)

- **1891:** a liga da época deu o título dividido entre Saint Andrew's e Caledonians (empatados); Saint Andrew's venceu o desempate pelas medalhas. A AFA cita só o Saint Andrew's, que fica como campeão no pacote
- **1936 Copa de Oro:** jogo único entre os campeões da Copa de Honor (San Lorenzo) e da Copa Campeonato (River Plate), lido à mão da página arg-oro36 da RSSSF (texto corrido)

### Identidade dos clubes

Regras em `coleta/arg-1/clubes_arg.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes argentinos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido no Brasil ("Boca Juniors", "River Plate", "Racing Club");
- homônimo dentro da Argentina ou com clube de outro país já no banco/pacotes: acrescenta a cidade
  ("Racing de Córdoba", "Gimnasia de Jujuy", "Arsenal de Sarandí", "Nacional de Buenos Aires");
- o mesmo clube com outro nome (English High School -> Alumni; Racing Football Club -> Racing Club) é um só,
  com o nome atual; os nomes antigos ficam no nomes_fonte.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano). A chave é o nome sem acento, em
minúsculas, com pontuação trocada por espaço (rsssf_sul.chave). Vale a primeira regra que casa com o começo da chave
no ano da edição; por isso as mais específicas vêm antes. Nome que sobra depois do clube (local do jogo colado na
coluna, como "Estudiantes de La Plata Atlanta, Buenos Aires") não atrapalha: a regra casa só o começo.
```

## 8. O que não deu para coletar

- **Fora do pacote:** as copas da liga (Copa de la Superliga 2019, Copa de la Liga Profesional 2020-2024) e a Copa Campeonato 2013/14, que a AFA e a RSSSF tratam como copas; os torneios de reclassificação, os promocionais, as liguillas pré-Libertadores e os jogos de promoção contra clubes da 2ª divisão.
- **Edições sem jogos** (1): 2025 Liga.
- **Décadas com menos da metade dos gols com autor:** 1890s, 1900s, 1910s, 1920s, 1930s, 1940s, 1950s, 1960s, 1970s, 1980s, 1990s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1890s, 1900s, 1910s, 1920s, 1930s, 1940s, 1950s, 1960s, 1970s, 1980s, 1990s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- Achados da revisão em aberto (36, prefixo AR; lista na seção 9): vices errados em 12 edições, campeão de 1913 Federación, datas com ano errado (~3.920 jogos), fases, artilheiros e clubes. Corrigir e citar os ids em docs/coleta/pedidos-sulamerica.md.
- Decisões do Guilherme pedidas pela revisão: título de 1891 (só Saint Andrew's ou dividido), Apertura 2026, Quilmes de 1893-1895, fusões de 1934, Copa de Oro de 1936.

**Achados da revisão em aberto** (`docs/revisao/achados.csv`, provas em `docs/revisao/arg-1.md`):

- AR-001 (alta) A campeão — 1913 Federación: Campeão FAF 1913: Estudiantes de La Plata, 31 pts (18 j, 14-3-1, 64-16); vice GEBA 28; 3º Argentino de Quilmes 27.
- AR-002 (alta) A vice — 1976 Nacional: Final Boca 1-0 River (22/12/1976): vice River Plate. A fase 'Desempate do título' (14/12) são desempates de grupo (Boca x Quilmes, Talleres x Newell's), antes das quartas.
- AR-003 (alta) A vice — 1987/88: San Lorenzo 2º com 49 (38 j, 16-17-5, 49-28); Racing 3º 48; Instituto 15º com 33 (38 j).
- AR-004 (alta) A vice — 1989/90: Independiente 2º 46; Boca 3º 43; Rosario Central 4º 43 (16-13-9, 45-36, com -2); Talleres e Newell's 36 (-2 cada).
- AR-005 (alta) A vice — 2008/09 Apertura: Triangular: Tigre 1-2 San Lorenzo, San Lorenzo 1-3 Boca, Boca 0-1 Tigre: Boca 1º, Tigre 2º, San Lorenzo 3º. Arsenal 6º, Estudiantes 7º; Argentinos 11º, Godoy 12º, Banfield 13º.
- AR-006 (alta) A vice — 1926 Amateurs: 26 clubes, 25 jogos cada: Independiente 46, San Lorenzo 45, Platense 37, Racing 34...
- AR-007 (alta) A vice — 1926 Asociación: 18 clubes, 17 jogos cada: Boca 32, Argentinos Juniors 28, Huracán 24, Sportivo Balcarce 23...
- AR-008 (alta) A vice — 1919 Asociación: Torneio final de 6 clubes: Boca 16 (8 j), Estudiantes (LP) 7, Huracán 4, Eureka 3, Sportivo Almagro 3, Porteño 3. Independiente, Racing, River... saíram para a AAm.
- AR-009 (alta) A vice — 1919 Amateurs: Racing 26, Vélez 20 (13 j, 9-2-2), River 16, Defensores de Belgrano 16, Atlanta 14...
- AR-010 (alta) A vice — 1912 Asociación: 6 clubes, 10 j: Quilmes 15, San Isidro 11, Racing 10, Estudiantes (BA) 8, Belgrano Athletic 7, River 7.
- AR-011 (alta) A vice — 1913 Federación: GEBA (Gimnasia y Esgrima BA) 2º 28; Argentino de Quilmes 3º 27 (18 j, 12-3-3).
- AR-012 (alta) A vice — 1895: Lomas Academy 2º 13 (10 j, com os W.O.); Flores 3º 12.
- AR-013 (alta) A vice — 1896: 8 jogos por clube, 20 no total: Lomas Academy 12, Flores Athletic 10, Lomas Athletic 9 (4-1-3), Belgrano Athletic 8.
- AR-014 (media) A 3º lugar — 1997/98 Apertura: River 1-3 Rosario Central (31/08/1997). Rosario Central 3º (35); San Lorenzo 5º (9-5-5); Huracán 3-3-13.
- AR-015 (media) A 3º lugar — 1974 Nacional; 1929: 1974 Nacional: 3º Vélez Sarsfield (grupo final: San Lorenzo 11, Rosario Central 10, Vélez 8). 1929: 3º River Plate.
- AR-016 (alta) B classificação — 1949: O jogo é Gimnasia y Esgrima 1:0 Estudiantes de La Plata (RSSSF arg49, rodada 20). Tabela de 34 j: Boca 15º, Tigre 16º, Huracán 17º, Lanús 18º (rebaixado após o desempate).
- AR-017 (media) B classificação — 1988/89: 1988/89: 3 pela vitória, 2 pelo empate ganho nos pênaltis e 1 pelo perdido: Independiente 84, Boca 76, Deportivo Español 68.
- AR-018 (media) B classificação — 2016/17: Lanús 1-0 Atlético Tucumán (19/11), Lanús 1-0 Gimnasia (05/12), Tigre 0-0 Atlético Tucumán (19/12), Tigre 0-1 Gimnasia (18/03). Todos com 30 j; Lanús 8º.
- AR-019 (media) B classificação — 1975 Metropolitano: River 72-38, Huracán 73-46, Estudiantes 68-51, Banfield 57-73 (dois placares com 1 gol a menos no banco).
- AR-020 (media) B classificação — 1908; 1929; 1931 Liga; 1965: 1908: Belgrano 31, San Isidro 4º, Estudiantes 5º, Nacional 2 j; 1929: Lanús 8-8-1 24 pts; 1931: Platense e Lanús 34 j; 1965: Racing 5º com 34 j (a RSSSF conta 33).
- AR-021 (baixa) B rebaixamento — várias: Rebaixamentos por promedios e desempates de cada temporada (ex.: 2011: River, Huracán, Quilmes e Gimnasia LP).
- AR-022 (media) C datas — 26 edições: 1931: 31/05/1931 a 06/01/1932; 1937: 04/04 a 19/12/1937; Superliga 2018-19: 10/08/2018 a 07/04/2019 (fichas da es).
- AR-023 (media) C datas — ~40 edições: 1990/91: ida 06/07 e volta 09/07/1991; 2006 Apertura: Estudiantes 2-1 Boca em 13/12/2006; 1939: desempate do 1º turno em 10/12/1939 e do 2º lugar em 09/11/1941 (no banco 1939-07-16 e 1939-12-22).
- AR-024 (baixa) C datas — 2005/06 Apertura; 2019/20: Datas que não existem.
- AR-025 (media) C fases — 1931 Asociación; 1937; 1939; 1976 Nacional; 1979 Metropolitano; 1923 Asociación: 1937 e 1939: 'Playoff to define the first position in the first step' / 'First stage winner playoff' (RSSSF); 1923: desempate Boca x Huracán 3-0, 0-2, 0-0, 2-0.
- AR-026 (media) C fases — 1929; 1970 Nacional; 1979 Metropolitano: A final de 1929 foi Gimnasia x Boca; a de 1979 Metropolitano, River x Vélez; a de 1970 Nacional, Boca x Rosario Central.
- AR-027 (media) D artilheiro — 1894: James Gifford 7 gols.
- AR-028 (media) D artilheiro — 1934 Asociación: Pedro Maseda (Argentino de Quilmes) e Domingo Tarasconi (General San Martín), 16 gols.
- AR-029 (media) D artilheiro — 2025 Apertura; 1932 Asociación; 1997/98 Clausura: 2025 Apertura: Tomás Molina 10 (artilheiro único); 1932 Irurieta 23; 1998 Clausura Roberto Sosa 16.
- AR-030 (baixa) D artilheiro — 1936 Copa de Honor; 1936 Campeonato; 1988/89: 1936 Copa de Honor: Alberto Zozaya 16; 1936 Copa Campeonato: Evaristo Barrera 19; 1988/89: Oscar Dertycia e Néstor Gorosito 20.
- AR-031 (media) E clube duplicado — 1985 Nacional: O participante do Nacional 1985 é o Club Cipolletti (o mesmo de 1973-1980).
- AR-032 (baixa) E clube — 1893-1895: es: 'El Quilmes Atlético Club, sin evidencias, infiere ser la misma entidad que el Quilmes Rowers Athletic Club, aunque historiadores afirman que se trata de dos entidades distintas.' (pergunta ao Guilherme)
- AR-033 (baixa) E clube — 1934 Liga: Os dois times de 1934 foram fusões temporárias (pergunta ao Guilherme: como mostrar).
- AR-034 (baixa) E nomes — 1926: Nomes separados (sinal de linhas mal lidas em 1926).
- AR-043 (baixa) A edições — 2026 Apertura: O Apertura 2026 já terminou (Belgrano campeão, River vice). Pergunta ao Guilherme: entra agora ou só quando a temporada 2026 fechar?
- AR-044 (baixa) A título — 1891: es e en listam o título dividido entre Saint Andrew's e Old Caledonians (decisão da liga da época). Pergunta ao Guilherme.

## 10. Arquivos e comandos

Código em `coleta/arg-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_espn.py` | Baixa o placar diário da ESPN (liga arg.1) de 2001 a 2025 para data/coleta/arg-1/espn/arg1_<ano>.json. |
| `baixar_ogol.py` | Baixa o calendário de cada edição da 1ª divisão argentina no ogol para data/coleta/arg-1/ogol/<id>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão argentina para data/coleta/arg-1/rsssf/. |
| `campeoes_wiki.py` | Lista de campeões da Wikipédia em inglês ("List of Argentine football champions"), segunda fonte do campeão. |
| `clubes_arg.py` | Identidade dos clubes argentinos: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão argentina (arg-1): uma por torneio que deu título de campeão da Primera División. |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão argentina, edição a edição (entram no relatório). |
| `importar.py` | Junta as fontes da 1ª divisão argentina e grava o pacote em data/coleta/arg-1/pacote/ e o relatório em docs/coleta/arg-1.md. |
| `ler_rsssf.py` | Lê o trecho de cada edição nas páginas da RSSSF (data/coleta/arg-1/rsssf/) com o leitor comum (rsssf_sul). |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol e com a ESPN. |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |

- Fontes baixadas: `data/coleta/arg-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-sulamerica/`, do ogol em `data/cache/ogol-arg-1/`.
- Pacote: `data/coleta/arg-1/pacote/`; relatório: `docs/coleta/arg-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/arg-1/baixar_espn.py
python coleta/arg-1/baixar_ogol.py
python coleta/arg-1/baixar_rsssf.py
python coleta/arg-1/importar.py
python coleta/arg-1/conferir.py [-v temporada]   # divergências
python coleta/comum-sulamerica/testar_carga.py arg-1 <scratchpad>
python coleta/comum-sulamerica/documentar.py
```

