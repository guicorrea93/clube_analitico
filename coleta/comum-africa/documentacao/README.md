# Coleta África — documentação

Gerado por `python coleta/comum-africa/documentar.py`. Uma ficha por competição, com tudo o que o pacote tem, como as edições foram definidas, fontes e regras, a conferência, a cobertura de cada campo década a década, o formato ao longo do tempo, campeões e vices, ajustes de pontos, todas as correções e decisões com o motivo, o que não deu para coletar e as pendências.

Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum-africa/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-africa.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-africa`).

| Competição | Edições | Sem jogos | Jogos | Gols c/ autor | Cartões | Clubes | Edições ok / div. | No banco | Commit | Achados abertos | Ficha |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Campeonato Egípcio | 73 (1948/49–2025/26) | 13 | 11574 | 3068 | 0 | 74 | 42 / 12 | sim | 06635c8 | 0 | [egy-1](egy-1.md) |
| Campeonato Marroquino | 110 (1915/16–2025/26) | 41 | 11736 | 18 | 0 | 100 | 35 / 20 | não | — | 0 | [mar-1](mar-1.md) |

## Pendências de todas as competições

- **egy-1:** 1948/49 a 1963/64 sem jogos (nenhuma fonte pública tem): só a tabela final, e a final ou o desempate do título quando a página da RSSSF traz (1948/49, 1957/58, 1962/63, 1963/64, 1975/76). As listas "Results Ahly" (só os jogos do Al-Ahly, sem data nem mando) ficaram de fora. Fonte que resolveria: o site do Dr. Tarek Said (drtareksaid.net, arquivado) ou jornais egípcios da época.
- **egy-1:** 1954/55, 1971/72 e 1973/74 (não terminadas): nenhuma fonte tem jogos nem tabela; entram só com a observação.
- **egy-1:** Autores dos gols só onde a RSSSF traz (1998/99 a 2006/07, nem sempre a temporada inteira); de 2007/08 em diante a página não tem autores e a ESPN não cobre a liga. Fonte que resolveria: o ogol jogo a jogo (página de cada partida).
- **egy-1:** Divergências entre a tabela da RSSSF e os jogos do ogol sem terceira fonte (1979/80, 1980/81) e as que a Wikipédia confirma a tabela (1977/78 Zamalek, 1991/92 Damanhour 0-0 Zamalek = 1-2?, 2010/11): o jogo provável está no relatório; nenhum placar foi mudado.
- **egy-1:** Identidade a conferir: o "Sohag Railways" de 2000/01 e o "Sohag" de 2001/02 entraram como um clube só; o Al-Shourta de 1975/76 entrou como Ittihad El-Shorta; o "Suez Club" do ogol é o Ittihad Suez só em 1965/66.
- **mar-1:** Ainda não carregado no banco (pacote pronto em 24/11/2026; teste de carga OK).
- **mar-1:** Era colonial (1915/16 a 1954/55): 9 anos sem página da RSSSF (só o campeão); nos outros, jogos incompletos (ligas regionais com os resultados conhecidos e o mata-mata nacional) ou só a classificação (1949/50 a 1953/54, a maioria dos clubes só com os pontos). Fonte que resolveria: os jornais da época (Le Petit Marocain, La Vigie Marocaine) na Gallica (BnF).
- **mar-1:** 1968/69 a 1994/95 (fora 1980/81, 1989/90 e 1990/91): só a tabela final; o ogol só tem os jogos de 2004/05 em diante. 1970/71, 1973/74 e 1981/82 sem página da RSSSF: só o campeão e o vice.
- **mar-1:** Tabelas de confrontos (1956/57 a 1967/68, 1980/81, 1989/90): os jogos não têm data nem rodada, e vários resultados não batem com a tabela final da página (vitórias e empates trocados com os mesmos gols); sem terceira fonte.
- **mar-1:** Autores dos gols quase nenhum (a RSSSF do Marrocos não traz) e nenhum cartão. Fonte que resolveria: o ogol jogo a jogo (2004/05 em diante).
- **mar-1:** Identidade a conferir: Racing Casablanca (colonial) = Racing AC = ADM Casablanca (como a RSSSF conta); AS Salé = SA Salé = Sporting Salé; JS Massira = Forces Auxiliaires (a página de 1994/95 diz que o clube mudou para El Ayoun); "ASM" (1957/58) sem nome completo; "US Casablanca" = USA Casablanca.
- **mar-1:** 1946/47: campeão USA Casablanca (página da temporada e Wikipédia); a lista de campeões da RSSSF põe a US Marocaine (erro da lista; avisar a RSSSF?).

## Próximas competições

- 2ªs divisões, na ordem do guia geral, só quando o Guilherme pedir. Como fazer: `COMECE-AQUI.md`, seção 4.
