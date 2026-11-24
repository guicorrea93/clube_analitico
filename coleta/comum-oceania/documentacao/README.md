# Coleta Oceania — documentação

Gerado por `python coleta/comum-oceania/documentar.py`. Uma ficha por competição, com tudo o que o pacote tem, como as edições foram definidas, fontes e regras, a conferência, a cobertura de cada campo década a década, o formato ao longo do tempo, campeões e vices, ajustes de pontos, todas as correções e decisões com o motivo, o que não deu para coletar e as pendências.

Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum-oceania/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-oceania.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-oceania`).

| Competição | Edições | Sem jogos | Jogos | Gols c/ autor | Cartões | Clubes | Edições ok / div. | No banco | Commit | Achados abertos | Ficha |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Campeonato Neozelandês | 55 (1970–2025) | 0 | 7480 | 2888 | 0 | 101 | 45 / 10 | sim | d7a6379 | 0 | [nzl-1](nzl-1.md) |
| Campeonato Taitiano | 79 (1948–2025/26) | 48 | 2647 | 113 | 0 | 35 | 23 / 0 | sim | 8f154e1 | 0 | [tah-1](tah-1.md) |
| Campeonato Neocaledônio | 76 (1950–2026) | 40 | 2472 | 188 | 0 | 63 | 21 / 4 | sim | 8f154e1 | 0 | [ncl-1](ncl-1.md) |
| Campeonato Fijiano | 50 (1977–2026) | 22 | 2177 | 194 | 0 | 17 | 20 / 1 | não | — | 0 | [fij-1](fij-1.md) |

## Pendências de todas as competições

- **nzl-1:** Fase nacional de 1994 sem jogos (28): a RSSSF e a Wikipédia só têm a tabela.
- **nzl-1:** Autores dos gols só de 1993-2007/08 (parte); de 2008/09 em diante só a página de cada jogo do ogol tem (não baixada).
- **nzl-1:** Ligas regionais de 2023-2025 com divergências entre as fontes (Wikipédia, ogol e RSSSF): explicadas na conferência; a Central League 2025 tem 89 dos 90 jogos.
- **nzl-1:** Artilheiros: não coletados (a RSSSF lista só em algumas temporadas; a Wikipédia tem nas temporadas recentes).
- **nzl-1:** Datas: sem data em 1970-1995 (matrizes) e nas ligas regionais de 2022-2024 (matriz da Wikipédia).
- **tah-1:** 1948-1967 e 1972-1998 só com o campeão (e o vice em 8 anos): nenhuma fonte aberta tem jogos ou tabelas.
- **tah-1:** 1956, 1957 e 1961: a Wikipédia dá outro campeão (copia uma versão antiga da RSSSF); vale a RSSSF (decisão do Guilherme, 24/11/2026). Uma fonte da época (Journal de Tahiti) resolveria.
- **tah-1:** 1998/99 a 2004/05 com parte dos jogos; 2010/11 (playoff) e 2011/12 só com as tabelas.
- **tah-1:** Autores dos gols só em poucas temporadas; artilheiros, cartões, estádio e público não coletados.
- **ncl-1:** 1950-1983 e 1986-1996 só com o campeão (a final em 1964, 1971, 1977 e 1978; vice e 3º em parte dos anos).
- **ncl-1:** 1963 e 1964: Club Sportif Militaire pela RSSSF atual; a versão antiga (USC, JS Vallée du Tir), copiada pela Wikipédia e pelo ogol, fica registrada. Um jornal da época (La France Australe) resolveria de vez.
- **ncl-1:** Identidades com evidência parcial: Entente Gélima, Wé-Luécilla, AS Auteuil x FC Auteuil (separados).
- **ncl-1:** Jogos sem placar ("bt", "drw", "lt") em 2004/05, 2013 e 2015; ligas das províncias e torneio das ilhas fora.
- **fij-1:** 1977-1982, 1987, 1989-1993, 1995 e 1996 só com o campeão (vice em poucos anos); 1983-1988, 1994 e 1997 só a tabela.
- **fij-1:** 1998-2004 com parte dos jogos (as tabelas da página são as publicadas, algumas "based on known results"); 2011 e 2012 só a tabela na RSSSF.
- **fij-1:** Tabelas com erro de digitação na própria página (vitórias + empates + derrotas diferente de jogos) entram com nota.
- **fij-1:** Autores dos gols só em parte de 2001-2010; artilheiros, cartões, estádio e público não coletados.

## Próximas competições

- 2ªs divisões, na ordem do guia geral, só quando o Guilherme pedir. Como fazer: `COMECE-AQUI.md`, seção 4.
