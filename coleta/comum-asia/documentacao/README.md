# Coleta Ásia — documentação

Gerado por `python coleta/comum-asia/documentar.py`. Uma ficha por competição, com tudo o que o pacote tem, como as edições foram definidas, fontes e regras, a conferência, a cobertura de cada campo década a década, o formato ao longo do tempo, campeões e vices, ajustes de pontos, todas as correções e decisões com o motivo, o que não deu para coletar e as pendências.

Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum-asia/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-asia.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-asia`).

| Competição | Edições | Sem jogos | Jogos | Gols c/ autor | Cartões | Clubes | Edições ok / div. | No banco | Commit | Achados abertos | Ficha |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Campeonato Japonês | 60 (1965–2025) | 0 | 12190 | 27554 | 31272 | 40 | 57 / 3 | sim | 71d50064 | 0 | [jpn-1](jpn-1.md) |
| Campeonato Sul-Coreano | 43 (1983–2025) | 0 | 7163 | 17984 | 24627 | 25 | 37 / 6 | sim | e04507f1 | 0 | [kor-1](kor-1.md) |
| Campeonato Saudita | 69 (1957/58–2025/26) | 12 | 5965 | 7296 | 4801 | 43 | 35 / 8 | não | 204e7d6d | 0 | [ksa-1](ksa-1.md) |

## Pendências de todas as competições

- **jpn-1:** JSL (1965 a 1991/92): os jogos vêm da tabela de confrontos da RSSSF, sem data, rodada nem autores dos gols (menos 1988/89, com rodada e data). Fonte que resolveria: o livro oficial 'Nihon Soccer League Zenshi' (1993), citado pela Wikipédia em japonês, ou jornais da época.
- **jpn-1:** 1966, 1971 e 1973: a tabela de confrontos da RSSSF não fecha com a tabela final por 1 a 4 gols num confronto (há duas células possíveis; explicado na edição). A mesma fonte acima resolveria.
- **jpn-1:** 1977 a 1979: os empates foram decididos nos pênaltis e a página não diz quem ganhou cada disputa.
- **jpn-1:** J1: a J.League não marca os gols de pênalti (ficam como 'normal') nem dá o nome de quem fez gol contra.
- **jpn-1:** Artilheiro de 1986/87: a lista de campeões da Wikipédia dá 17 gols a Toshio Matsuura (NKK), a RSSSF dá 14; ficou o da Wikipédia. Fonte que resolveria: o livro oficial da JSL.
- **kor-1:** 23 jogos sem os autores dos gols (o boletim do portal não fecha com o placar; os autores que ele tem estão no gols_texto). Fonte que resolveria: as páginas 'NNNN년 K리그의 경기 결과' da Wikipédia em coreano (têm os autores de cada jogo; serviram para 1987 e 1990).
- **kor-1:** 197 estrangeiros de antes de 2013 com o nome romanizado do hangul (aproximação; a maioria só com cartões): sem nome em inglês no site oficial nem autor na RSSSF. Lista no relatório. Fonte que resolveria: a página de jogador do site da K League (não achei a chamada de dados) ou a Wikipédia em coreano.
- **kor-1:** Coreanos: grafia oficial em inglês do site da K League para quem jogou de 2013 em diante, romanização revisada para os outros (Park Yun-gi, e não Park Yoon-ki, como a Wikipédia escreve). Uns poucos cortes de sílaba esquisitos vêm da grafia do próprio site ("Jeewong").
- **kor-1:** 1997: a linha do Jeju United (Puchon SK) da RSSSF (18-35) não fecha com os jogos (19-36); a RSSSF não tem os jogos de 1997 e a Wikipédia em coreano não tem a tabela.
- **kor-1:** Artilheiro: a soma dos boletins fica 1 gol abaixo da lista oficial em 1984, 1993, 1997, 1999, 2005, 2006 e 2021 (gols em jogos sem autores; em 2005 a K League parece contar o playoff); em 2013, 2022 e 2023 a soma dá empate e a lista oficial desempata pelo número de jogos. Vale a lista oficial (Wikipédia).
- **kor-1:** 958 jogos de antes de 2013 sem rodada (o portal não dá; a rodada sai da ordem dos jogos de cada clube quando os dois batem); classificacao_rodada só de 2013 em diante.
- **kor-1:** Estádios: nome traduzido por regra do hangul do portal (cidade + tipo: 월드컵 World Cup Stadium, 종합 Sports Complex...); cidade dos jogos em branco. O Sangmu de 1985 fica sem cidade (time do Exército, sem sede).
- **kor-1:** 2026: entra quando acabar (em 24/11 faltavam 12 jogos).
- **ksa-1:** 1957/58 a 1973/74 (His Majesty's League): só campeão, vice e, quando a RSSSF tem o mesmo par, o jogo da final da Copa do Rei; sem os outros jogos nem a data. 1968/69 sem a final (o par oficial não está na lista da RSSSF). Fonte que resolveria: o relatório oficial da federação (2025), que não está publicado em detalhe.
- **ksa-1:** Sem os jogos da fase de liga em 1977/78-1979/80, 1981/82, 1984/85, 1985/86 e 1987/88-1996/97 (a RSSSF só tem a tabela; o ogol só tem jogos de 1999/00 em diante); 1977/78-1981/82 com tabela só de jogos e pontos, 1985/86 só a ordem. Fonte que resolveria: os jornais da época (Arab News, citado pela RSSSF) ou o arquivo antigo do Kooora (o site mudou e não mostra mais os anos antigos).
- **ksa-1:** Finais do playoff que a RSSSF não tem: 1994/95 e 1995/96 (campeão e vice da lista oficial).
- **ksa-1:** Autores dos gols só onde a RSSSF tem (1974/75-2005/06, com falhas: 1997/98 sem nenhum, 2003/04 66%) e a ESPN (2022/23-2025/26, 98-100%); 2006/07-2021/22 sem autores nem cartões. Fonte que resolveria: as súmulas do site da Saudi Pro League ou o FBref/Transfermarkt.
- **ksa-1:** Placares diferentes entre a RSSSF e o ogol em uns 2 a 8 jogos por ano (listados em cada edição); ficou a fonte dos jogos do ano, conferida com a tabela da RSSSF. 1997/98, 2003/04, 2011/12: diferenças de 1 gol entre os jogos e a tabela da RSSSF.
- **ksa-1:** Datas: 36 jogos sem data (finais antigas e playoffs da RSSSF sem data).

## Próximas competições

- 1ªs divisões da AFC, na ordem do guia geral: irn-1, aus-1, chn-1, qat-1, uae-1, uzb-1, irq-1, ind-1, tha-1; depois as outras. Antes de cada uma, as decisões de escopo vão ao Guilherme. Como fazer: `COMECE-AQUI.md`, seção 4.
