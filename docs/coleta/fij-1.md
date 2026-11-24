# Coleta: Campeonato Fijiano (`fij-1`)

Gerado por `python coleta/fij-1/importar.py`. Pacote em `data/coleta/fij-1/pacote/`.

## Resumo

- 50 edições (1977 a 2026), 28 com jogos; 2177 jogos, 6722 gols, 194 com autor.
- Escopo aprovado pelo Guilherme em 24/11/2026, depois de pesquisa a fundo (docstrings de `coleta/fij-1/edicoes.py` e `coleta/fij-1/clubes_fij.py`):
  - a 1ª divisão é a liga dos distritos (desde 1977); ficam de fora o Inter-District Championship, o National Club Championship, a Club Franchise League (2004/05-2006), as copas, a 2ª divisão e as repescagens;
  - 2003 = Ba (os Olympians, 1º na tabela, ganharam um jogo no tribunal; o Ba recorreu à justiça, a final de desempate nunca foi jogada e a federação deu o título ao Ba em 2006); 2010 = Ba (o título dado ao Lautoka no tribunal foi revogado);
  - nomes: o distrito puro, salvo "Ba FC"; seleções de base: "Fiji Olympians", "Fiji U-20" (2010) e "Fiji Youth Teams" (2011).
- Pontuação: 2 por vitória até 1986, 3 a partir de 1988.

## Fontes

- **RSSSF** (`data/coleta/fij-1/rsssf/`, `baixar_rsssf.py`): lista de campeões e páginas por ano (1977-1989, 1992-1994, 1997-2026).
- **Wikipédia em inglês** (`data/coleta/fij-1/wikipedia/`, `baixar_wikipedia.py`): segunda fonte do campeão (bate com a RSSSF em todos os anos).
- **ogol** (`data/coleta/fij-1/ogol/`, cache em `data/cache/ogol-fij-1/`, `baixar_ogol.py`): os jogos de 2011 (fecham com a tabela da RSSSF) e a grafia dos times para os escudos.

## Correções e decisões

- `fiji00 / 56`: descartado (adversário incerto na página).
- `fiji00 / 57`: descartado (adversário incerto na página).
- `fiji00 / 167`: descartado (adversário incerto na página).
- `fiji00 / 168`: descartado (adversário incerto na página).
- `fiji09 / 134`: a página traz Tavua 1-1 Labasa "possibly awarded 2-0"; a tabela conta o empate.
- `fiji2010 / 228`: Lautoka 1-1 Rewa: dado 2-0 ao Lautoka em 11/03/2011 e revogado em 10/07/2011 (o título voltou ao Ba); vale o 1-1, que é o que a tabela conta.
- tabela `fiji2025`, linha 128, fora da conferência: tabela do meio da temporada ("Hakfway Table", com erro de digitação).
- 2000: os 8 jogos do sub-20 ("Under 20") foram anulados e ficam de fora, como na tabela da página.

## Divergências que ficam

- **2005:** grupo do rebaixamento (Pepsi 4): três jogos só com "drw" (empate sem placar) na página ficam de fora; a tabela conta os empates.

## Edição a edição

| Ano | Formato | Jogos | Esperados | Gols | Com autor | Campeão | Vice | Observação |
|---|---|---|---|---|---|---|---|---|
| 1977 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Ba FC |  | só o campeão na RSSSF |
| 1978 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Nadi |  | só o campeão na RSSSF |
| 1979 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Ba FC | Nadroga | só o campeão na RSSSF |
| 1980 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Nadi |  | só o campeão na RSSSF |
| 1981 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Nadi |  | só o campeão na RSSSF |
| 1982 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Nadi |  | só o campeão na RSSSF |
| 1983 | só a tabela final (sem jogos); 2 pontos por vitória | 0 | 0 | 0 | 0 | Nadi | Lautoka | só a tabela final na RSSSF |
| 1984 | só a tabela final (sem jogos); 2 pontos por vitória | 0 | 0 | 0 | 0 | Lautoka | Ba FC | só a tabela final na RSSSF |
| 1985 | só a tabela final (sem jogos); 2 pontos por vitória | 0 | 0 | 0 | 0 | Nadi | Suva | só a tabela final na RSSSF |
| 1986 | só a tabela final (sem jogos); 2 pontos por vitória | 0 | 0 | 0 | 0 | Ba FC | Lautoka | só a tabela final na RSSSF |
| 1987 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Ba FC |  | só o campeão na RSSSF |
| 1988 | só a tabela final (sem jogos); 3 pontos por vitória | 0 | 0 | 0 | 0 | Lautoka | Rewa | só a tabela final na RSSSF |
| 1989 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Nadroga |  | só o campeão na RSSSF |
| 1990 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Nadroga |  | só o campeão na RSSSF |
| 1991 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Labasa |  | só o campeão na RSSSF |
| 1992 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Ba FC |  | só o campeão na RSSSF |
| 1993 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Nadroga |  | só o campeão na RSSSF |
| 1994 | só a tabela final (sem jogos); 3 pontos por vitória | 0 | 0 | 0 | 0 | Ba FC | Labasa | só a tabela final na RSSSF |
| 1995 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Ba FC |  | só o campeão na RSSSF |
| 1996 | só o campeão (sem jogos nem tabela) | 0 | 0 | 0 | 0 | Suva |  | só o campeão na RSSSF |
| 1997 | só a tabela final (sem jogos); 3 pontos por vitória | 0 | 0 | 0 | 0 | Suva | Labasa | só a tabela final na RSSSF |
| 1998 | jogos incompletos: pontos corridos (9 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 30 | 30 | 75 | 0 | Nadi | Ba FC | a página da RSSSF traz só parte dos jogos (a tabela é a publicada) |
| 1999 | jogos incompletos: pontos corridos (9 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 44 | 44 | 117 | 0 | Ba FC | Nadi | a página da RSSSF traz só parte dos jogos (a tabela é a publicada) |
| 2000 | jogos incompletos: pontos corridos (10 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 87 | 87 | 299 | 0 | Nadi | Ba FC | a página da RSSSF traz só parte dos jogos (a tabela é a publicada) |
| 2001 | jogos incompletos: pontos corridos (11 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 108 | 108 | 334 | 1 | Ba FC | Fiji Olympians | a página da RSSSF traz só parte dos jogos (a tabela é a publicada) |
| 2002 | jogos incompletos: pontos corridos (11 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 104 | 104 | 280 | 0 | Ba FC | Lautoka | a página da RSSSF traz só parte dos jogos (a tabela é a publicada) |
| 2003 | jogos incompletos: pontos corridos (11 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 61 | 61 | 184 | 16 | Ba FC | Fiji Olympians | a página da RSSSF traz só parte dos jogos (a tabela é a publicada) |
| 2004 | jogos incompletos: pontos corridos (10 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 83 | 83 | 232 | 8 | Ba FC | Lautoka | a página da RSSSF traz só parte dos jogos (a tabela é a publicada) |
| 2005 | fase de grupos (10 clubes) + grupo do título (6 clubes) + grupo do rebaixamento (4 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 79 | 81 | 215 | 1 | Ba FC | Navua | grupos, depois o Super 6 (título) e o Pepsi 4 (rebaixamento) |
| 2006 | pontos corridos (11 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 109 | 109 | 365 | 0 | Ba FC | Nadi |  |
| 2007 | fase regular (10 clubes) + grupo do título (6 clubes) + grupo do rebaixamento (4 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 87 | 87 | 282 | 40 | Labasa | Lautoka |  |
| 2008 | fase regular (10 clubes) + grupo do título (6 clubes) + grupo do rebaixamento (4 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 87 | 87 | 311 | 32 | Ba FC | Labasa |  |
| 2009 | pontos corridos (10 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 90 | 90 | 280 | 54 | Lautoka | Navua |  |
| 2010 | pontos corridos (11 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 110 | 110 | 381 | 42 | Ba FC | Lautoka |  |
| 2011 | pontos corridos (11 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 110 | 110 | 306 | 0 | Ba FC | Labasa |  |
| 2012 | só a tabela final (sem jogos); 3 pontos por vitória | 0 | 0 | 0 | 0 | Ba FC | Suva | a RSSSF só tem a tabela; o calendário do ogol diverge dela em 7 clubes e falta um jogo, por isso não entra |
| 2013 | pontos corridos (10 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 90 | 90 | 324 | 0 | Ba FC | Nadi |  |
| 2014 | pontos corridos (8 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 56 | 56 | 150 | 0 | Suva | Ba FC |  |
| 2015 | pontos corridos (8 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 56 | 56 | 168 | 0 | Nadi | Suva |  |
| 2016 | pontos corridos (8 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 56 | 56 | 168 | 0 | Ba FC | Rewa |  |
| 2017 | pontos corridos (8 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 56 | 56 | 165 | 0 | Lautoka | Ba FC |  |
| 2018 | pontos corridos (8 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 56 | 56 | 149 | 0 | Lautoka | Ba FC |  |
| 2019 | pontos corridos (8 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 56 | 56 | 166 | 0 | Ba FC | Lautoka |  |
| 2020 | pontos corridos (8 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 56 | 56 | 171 | 0 | Suva | Rewa |  |
| 2021 | pontos corridos (8 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 56 | 56 | 123 | 0 | Lautoka | Rewa |  |
| 2022 | pontos corridos (10 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 90 | 90 | 256 | 0 | Rewa | Suva |  |
| 2023 | pontos corridos (10 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 90 | 90 | 262 | 0 | Lautoka | Rewa |  |
| 2024 | pontos corridos (10 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 90 | 90 | 310 | 0 | Rewa | Labasa |  |
| 2025 | pontos corridos (10 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 90 | 90 | 319 | 0 | Rewa | Labasa |  |
| 2026 | pontos corridos (10 clubes); 3 pontos por vitória, 1 por empate e 0 por derrota | 90 | 90 | 330 | 0 | Ba FC | Labasa |  |

## O que não deu para coletar

- 1977-1982, 1987, 1989-1993, 1995 e 1996: só o campeão (e o vice em poucos anos); 1983-1988, 1994 e 1997 só a tabela.
- 1998-2004 com parte dos jogos; 2012 só a tabela (o calendário do ogol não fecha com ela).
- Hora, estádio, público, cartões e artilheiros.
