# Coleta Europa — documentação

Gerado por `python coleta/comum-europa/documentar.py`. Uma ficha por liga, com tudo o que o pacote tem, a cobertura de cada campo década a década, o formato do campeonato ao longo do tempo, campeões, punições, todas as correções e decisões com o motivo, o que não deu para coletar e as pendências.

Regras de trabalho, ordem das pendências e como fazer uma liga nova: `coleta/comum-europa/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-europa.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-europa`).

| Liga | Temporadas | Jogos | Gols c/ autor | Cartões | Clubes | Tabelas ok / div. | Pendências | Ficha |
|---|---|---|---|---|---|---|---|---|
| Campeonato Inglês | 127 (1888/89–2025/26) | 51330 | 25841 | 33166 | 65 | 226 / 1 | 2 | [eng-1](eng-1.md) |
| Campeonato Espanhol | 94 (1928/29–2024/25) | 27336 | 24048 | 49824 | 63 | 178 / 11 | 2 | [esp-1](esp-1.md) |
| Campeonato Italiano | 94 (1929/30–2024/25) | 28864 | 23642 | 42440 | 69 | 161 / 9 | 2 | [ita-1](ita-1.md) |
| Campeonato Alemão | 62 (1963/64–2024/25) | 18914 | 21522 | 29022 | 58 | 121 / 3 | 2 | [ger-1](ger-1.md) |
| Campeonato Francês | 88 (1932/33–2025/26) | 30466 | 22613 | 35434 | 76 | 156 / 18 | 2 | [fra-1](fra-1.md) |
| Campeonato Português | 92 (1934/35–2025/26) | 20978 | 13874 | 30915 | 73 | 175 / 9 | 2 | [por-1](por-1.md) |

## Pendências de todas as ligas

- **eng-1:** EN-016 (revisão, baixa): 12 jogos de 2002/03 a 2016/17 sem nenhum gol com autor (a soma dos gols da ESPN não bate com o placar). Precisa de outra fonte jogo a jogo (ficha do ogol ou 11v11).
- **eng-1:** Autores dos gols e cartões antes de 2001/02: nenhuma fonte em lote; seria jogo a jogo (ficha do ogol).
- **esp-1:** Incluir 2025/26 (o guia pede até a última temporada terminada; pedir o ok do Guilherme).
- **esp-1:** Autores dos gols e cartões antes de 2001/02: a RSSSF tem de 2000/01 em diante; antes, jogo a jogo (ficha do ogol).
- **ita-1:** Incluir 2025/26 (o guia pede até a última temporada terminada; pedir o ok do Guilherme).
- **ita-1:** Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).
- **ger-1:** Incluir 2025/26 (o guia pede até a última temporada terminada; pedir o ok do Guilherme).
- **ger-1:** Campeonato alemão antes da Bundesliga (1902/03 a 1962/63: ligas regionais e fase final): ficou de fora; seria outra competição ou uma decisão do Guilherme.
- **fra-1:** Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).
- **fra-1:** Datas dos 356 jogos dos anos 1930 que nenhuma fonte tem.
- **por-1:** Autores dos gols e cartões antes de 2006/07 (a ESPN começa aí): jogo a jogo (ficha do ogol).
- **por-1:** Pontos do Porto em 2007/08 (Apito Final): ficou o desconto de 6, como no fim da temporada; se o Guilherme preferir a situação de hoje (absolvição em 2017), tirar o desconto em importar.py.

## Próximas ligas

- `ned-1` (Holanda), depois Escócia, Bélgica e Turquia (guia geral `docs/agentes-internacionais-COMECE-AQUI.md`), uma por vez e só com o ok do Guilherme.
