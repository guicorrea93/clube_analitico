# Coleta CONCACAF — documentação

Gerado por `python coleta/comum-concacaf/documentar.py`. Uma ficha por competição, com tudo o que o pacote tem, como as edições foram definidas, fontes e regras, a conferência, a cobertura de cada campo década a década, o formato ao longo do tempo, campeões e vices, ajustes de pontos, todas as correções e decisões com o motivo, o que não deu para coletar e as pendências.

Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum-concacaf/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-concacaf.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-concacaf`).

| Competição | Edições | Sem jogos | Jogos | Gols c/ autor | Cartões | Clubes | Edições ok / div. | No banco | Commit | Achados abertos | Ficha |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Campeonato Mexicano | 158 (1902/03–2026 Clausura) | 2 | 26606 | 56671 | 42633 | 92 | 116 / 33 | não | — | 0 | [mex-1](mex-1.md) |

## Pendências de todas as competições

- **mex-1:** Decidido em 24/11 (pesquisa aprovada pelo Guilherme): o Pachuca AC da era amadora (1902-1922) é o Pachuca de hoje, como o clube conta a própria história; a RSSSF diz que o Pachuca AC se dissolveu em 1920. Se forem clubes diferentes, separar em clubes_mex.py (regra 'pachuca').
- **mex-1:** Decidido em 24/11 (pesquisa aprovada pelo Guilherme): Atlético Español (1971-1982) = Necaxa (o clube vendido e renomeado, que voltou a se chamar Necaxa); a temporada 1930/31, cancelada, entra sem campeão, com a tabela do cancelamento.
- **mex-1:** Edições sem jogos: 1911/12 e 1916/17 (a RSSSF não tem página; só a tabela final de mexhist.html). Jogos incompletos: 1915/16, 1924/25, 1920/21 e 1921/22 (as duas ligas). Fonte que resolveria: jornais da época (Hemeroteca Nacional Digital da UNAM, a fonte dos autores das páginas da RSSSF).
- **mex-1:** 1995/96: falta o Guadalajara x Pumas do 1º turno (não está na página); pela tabela, o Guadalajara venceu por 3-0.
- **mex-1:** Estádio só de 2002 em diante (ESPN) e nos jogos com "at X": as linhas de estádio das páginas da RSSSF ("Estadio Jalisco, Guadalajara", acima do jogo) ainda não são lidas.
- **mex-1:** Divergências de um gol ou de um resultado entre a página e a tabela dela em cerca de 30 edições: ficam como erro da página (o relatório diz qual clube e qual tabela).

## Próximas competições

- 1ªs divisões da CONCACAF, na ordem do guia geral: usa-1, crc-1, hon-1, gua-1, slv-1, pan-1, jam-1, tri-1, can-1, hai-1; depois as outras. Antes de cada uma, as decisões de escopo ao Guilherme. Como fazer: `COMECE-AQUI.md`, seção 4.
