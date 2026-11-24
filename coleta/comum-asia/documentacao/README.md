# Coleta Ásia — documentação

Gerado por `python coleta/comum-asia/documentar.py`. Uma ficha por competição, com tudo o que o pacote tem, como as edições foram definidas, fontes e regras, a conferência, a cobertura de cada campo década a década, o formato ao longo do tempo, campeões e vices, ajustes de pontos, todas as correções e decisões com o motivo, o que não deu para coletar e as pendências.

Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum-asia/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-asia.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-asia`).

| Competição | Edições | Sem jogos | Jogos | Gols c/ autor | Cartões | Clubes | Edições ok / div. | No banco | Commit | Achados abertos | Ficha |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Campeonato Japonês | 60 (1965–2025) | 0 | 12190 | 27554 | 31272 | 40 | 57 / 3 | sim | 71d5006 | 0 | [jpn-1](jpn-1.md) |
| Campeonato Sul-Coreano | 43 (1983–2025) | 0 | 7163 | 17984 | 24627 | 25 | 37 / 6 | não | e04507f | 0 | [kor-1](kor-1.md) |

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

## Próximas competições

- 1ªs divisões da AFC, na ordem do guia geral: ksa-1, irn-1, aus-1, chn-1, qat-1, uae-1, uzb-1, irq-1, ind-1, tha-1; depois as outras. Antes de cada uma, as decisões de escopo vão ao Guilherme. Como fazer: `COMECE-AQUI.md`, seção 4.
