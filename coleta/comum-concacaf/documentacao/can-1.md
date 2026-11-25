# Campeonato Canadense (`can-1`) — documentação

Gerado por `python coleta/comum-concacaf/documentar.py` a partir do pacote `data/coleta/can-1/pacote/`, do código `coleta/can-1/` e do relatório `docs/coleta/can-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 15, de 1983 a 2026; 0 sem jogos.
- **Jogos:** 922 (922 com placar); **gols:** 2525; **gols com autor:** 3 (0%); **cartões:** 0.
- **Clubes:** 28; **artilheiros:** 0 edições com artilheiro (0 linhas, com empates).
- **Classificação final:** 15 edições; **tabelas publicadas guardadas para conferência:** 104 linhas.
- **No banco:** ainda não; **último commit do pacote:** nenhum (pacote ainda não commitado).
- **Observação da competição:** As três ligas profissionais nacionais do Canadá, como a lista da RSSSF: Canadian Professional Soccer League (1983), Canadian Soccer League (1987-1992) e Canadian Premier League (2019-2026). Ficam fora a National Soccer League e as que a seguiram (regionais, de Toronto) e os clubes canadenses da MLS (no usa-1).

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão do Canadá (can-1): as três ligas profissionais nacionais que a RSSSF junta como o topo do futebol
canadense (tablesc/canchamp.html, "CPSL/CSL 1983-1992 and CPL since 2019"). Escopo decidido em 25/11/2026 (ok do Guilherme):

- 1983: Canadian Professional Soccer League (uma temporada, abandonada no meio; o título saiu nos playoffs);
- 1987 a 1992: Canadian Soccer League (a página de Dave Litterer, usadave/csl.html, só tem as tabelas e os playoffs);
- 2019 em diante: Canadian Premier League (a liga atual, 1ª divisão sancionada pela Canada Soccer).

Ficam fora a National Soccer League (1922-1997) e as ligas que a seguiram (CPSL/CSL, 1998-2025), de clubes quase só da região
de Toronto (regionais, como a Liga Capitalina da Guatemala); o Canadian Championship (copa, fase 2: can-copa); e os clubes
canadenses da MLS (já no usa-1).

Fontes de cada edição: 1983 a página da CPSL (usadave/cpsl.html); 1987-1992 a do CSL; 2019-2024 a seção "Canadian Premier
League" da página do ano (tablesc/canAAAA.html); 2025 a página (tabela e playoffs) mais a fase regular do ogol (a RSSSF não
tem os jogos); 2026 só o ogol (a RSSSF ainda não tem a página).
```

**Edições:** 15, uma por título, como o bloco "CPSL/CSL 1983-1992 and CPL since 2019" da lista de campeões da RSSSF (`canchamp.html`): as três tentativas de uma liga profissional nacional de 1ª divisão. Escopo decidido em 25/11/2026: a Canadian Professional Soccer League de 1983 (uma temporada, abandonada no meio; o título saiu nos playoffs), a Canadian Soccer League de 1987 a 1992 e a Canadian Premier League de 2019 a 2026 (a liga atual, 1ª divisão sancionada pela Canada Soccer). Ficam fora a National Soccer League (1922-1997) e as ligas que a seguiram (1998-2025), de clubes quase só da região de Toronto; o Canadian Championship (copa, fase 2); e os clubes canadenses da MLS (já no `usa-1`).

**Fontes:** RSSSF (`data/coleta/can-1/rsssf/`) e ogol (`data/cache/ogol-can-1/`: a fase regular de 2025, que a página da RSSSF não tem, e a temporada 2026, que ela ainda não tem; campeão e vice de 2026 também na imprensa, TSN e CBC). A ESPN não cobre a CPL.

**Clubes:** nomes e identidades no começo de `coleta/can-1/clubes_can.py`. Vancouver 86ers = Vancouver Whitecaps (o mesmo do `usa-1`); o Toronto Blizzard do CSL leva "(CSL)" (o da NASL está no `usa-1`).

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 7.
- **Edições com alguma tabela divergente** (0; motivo no relatório, na edição): nenhuma.
- **Edições sem tabela para conferir** (8): 1983, 1987, 1988, 1989, 1990, 1991, 1992, 2026.
- **Edições com menos jogos que o esperado:** nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1980s | 4 | 56 | 66% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 3 | 31 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2010s | 1 | 100 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2020s | 7 | 735 | 99% | 0% | 67% | 0% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na CONCACAF: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1983: 6 clubes
- 1987: 8 clubes
- 1988: 9 clubes
- 1989: 10 clubes
- 1990: 11 clubes
- 1991: 8 clubes
- 1992: 6 clubes
- 2019: 7 clubes
- 2020 a 2026: 8 clubes

**Pontos por vitória:**

- 1983 a 1990: 2
- 1991 a 2026: 3

**Nome oficial:**

- 1983: Canadian Professional Soccer League <ano>
- 1987 a 1992: Canadian Soccer League <ano>
- 2019 a 2026: Canadian Premier League <ano>

**Formato** (fases na ordem, do edicoes.csv):

- 1983: jogos incompletos; pontos corridos + mata-mata
- 1987 a 1992: jogos incompletos; mata-mata
- 2019 a 2026: pontos corridos + mata-mata

**Fases e grupos de cada edição com mais de uma fase:**

- 1983: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 1987: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1988: Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 1989: Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 1990: Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 1991: Quartas de final (mata_mata, ida_volta); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 1992: Semifinal (mata_mata, ida_volta); Final (mata_mata, ida_volta)
- 2019: Primavera (liga); Outono (liga); Final (mata_mata, ida_volta)
- 2020: Primeira fase (liga); Fase final (liga); Final (mata_mata, jogo_unico)
- 2021: Primeira fase (liga); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2022: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)
- 2023: Primeira fase (liga); Fase preliminar (liga); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2024: Primeira fase (liga); Fase preliminar (liga); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2025: Primeira fase (liga); Fase preliminar (liga); Quartas de final (mata_mata, jogo_unico); Semifinal (mata_mata, jogo_unico); Final (mata_mata, jogo_unico)
- 2026: Primeira fase (liga); Semifinal (mata_mata, ida_volta); Final (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 10 edições
- lista de campeões: 4 edições
- calculada: 1 edições

**Observações das edições:**

- 1983: jogos incompletos: temporada abandonada no meio (dois dos seis clubes desistiram); a tabela é a do momento da parada e o título saiu nos playoffs
- 1987: jogos incompletos: só os jogos dos playoffs: a fase regular só com a tabela (a página não tem os jogos)
- 1988: jogos incompletos: só os jogos dos playoffs: a fase regular só com a tabela (a página não tem os jogos)
- 1989: jogos incompletos: só os jogos dos playoffs: a fase regular só com a tabela (a página não tem os jogos)
- 1990: jogos incompletos: só os jogos dos playoffs: a fase regular só com a tabela (a página não tem os jogos)
- 1991: jogos incompletos: só os jogos dos playoffs: a fase regular só com a tabela (a página não tem os jogos)
- 1992: jogos incompletos: só os jogos dos playoffs: a fase regular só com a tabela (a página não tem os jogos)
- 2025: fase regular do ogol (a página da RSSSF só tem a tabela e os playoffs)
- 2026: só o ogol (a RSSSF ainda não tem a página de 2026); campeão e vice também na imprensa (TSN, CBC)

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Vancouver Whitecaps: 4
- Forge FC: 4
- Cavalry FC: 2
- Edmonton Eagles: 1
- Calgary Kickers: 1
- Winnipeg Fury: 1
- Pacific FC: 1
- Atlético Ottawa: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1983 | Edmonton Eagles | Hamilton Steelers |
| 1987 | Calgary Kickers | Hamilton Steelers |
| 1988 | Vancouver Whitecaps | Hamilton Steelers |
| 1989 | Vancouver Whitecaps | Hamilton Steelers |
| 1990 | Vancouver Whitecaps | Hamilton Steelers |
| 1991 | Vancouver Whitecaps | Toronto Blizzard (CSL) |
| 1992 | Winnipeg Fury | Vancouver Whitecaps |
| 2019 | Forge FC | Cavalry FC |
| 2020 | Forge FC | HFX Wanderers |
| 2021 | Pacific FC | Forge FC |
| 2022 | Forge FC | Atlético Ottawa |
| 2023 | Forge FC | Cavalry FC |
| 2024 | Cavalry FC | Forge FC |
| 2025 | Atlético Ottawa | Cavalry FC |
| 2026 | Cavalry FC | Atlético Ottawa |

**Rebaixados marcados na classificação:** 0 em 0 edições (só onde a tabela publicada marca a queda).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1987: Edmonton Brickmen -1
- 1987: Toronto Blizzard (CSL) +2
- 1990: Winnipeg Fury -3
- 1990: Edmonton Brickmen -8
- 1992: London Lasers -3
- 1992: Toronto Blizzard (CSL) -3

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/can-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Identidade dos clubes

Regras em `coleta/can-1/clubes_can.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes da 1ª divisão do Canadá: cada grafia -> nome de exibição único no mundo.

Regras (docs/coleta/plano-de-coleta.md, seção 2.2), decididas em 25/11/2026:
- nome pelo qual o clube é conhecido (Forge FC, Cavalry FC, Pacific FC, HFX Wanderers, Atlético Ottawa), com as grafias das
  páginas e do ogol;
- o mesmo clube com outro nome (mesma cidade): York9 / York United / Inter Toronto (o nome desde 2025); Ottawa Pioneers /
  Ottawa Intrepid; Kitchener Spirit (1990) / Kitchener Kickers; Vancouver 86ers = Vancouver Whitecaps (a mesma organização: virou Whitecaps em 2001 e entrou na MLS em
  2011; o nome do usa-1);
- clubes diferentes (refundação ou outra cidade): o Toronto Blizzard do CSL (1986-1993) e o da NASL (no usa-1);
  o Edmonton Brickmen (1986-1990), o FC Edmonton (2019-2022) e o Edmonton Eagles (1983); o Montreal Supra (1988-1992) e o
  FC Supra du Québec (2026);
- nome que já existe no banco ou em outro pacote: a cidade ou o ano entre parênteses ("Toronto Blizzard (CSL)"), como o
  usa-1 fez com "(NASL)".

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
```

## 8. O que não deu para coletar

- **Edições sem jogos da fase regular (7):** 1987 a 1992 (a página do CSL só tem as tabelas e os playoffs; os playoffs entram) e 1983 (temporada abandonada no meio).
- **Edições sem jogos** (0): nenhuma.
- **Décadas com menos da metade dos gols com autor:** 1980s, 1990s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1980s, 1990s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- CSL 1987-1992 sem os jogos da fase regular (a página de Dave Litterer só tem as tabelas e os playoffs). Fonte que resolveria: jornais da época (Toronto Star, Vancouver Sun) ou o canadiansoccerhistory.com.
- Quase sem autores de gol: as páginas da CPL trazem só a lista de artilheiros da temporada, não os autores por jogo.
- CPL 2026 só do ogol: conferir com a página da RSSSF quando ela sair.
- Fora do can-1 (decisão de 25/11): a National Soccer League (1922-1997) e as ligas que a seguiram (1998-2025), regionais (Toronto); podem entrar na fase 4.

## 10. Arquivos e comandos

Código em `coleta/can-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `clubes_can.py` | Identidade dos clubes da 1ª divisão do Canadá: cada grafia -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão do Canadá (can-1): as três ligas profissionais nacionais que a RSSSF junta como o topo do futebol |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão do Canadá, edição a edição (entram no relatório). |
| `faltam.py` | Ajuda da conferência: na fase de pontos corridos de uma edição, os confrontos (mandante x visitante) que aparecem um número de |
| `importar.py` | Junta as fontes da 1ª divisão do Canadá e grava o pacote em data/coleta/can-1/pacote/ e o relatório em docs/coleta/can-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição da 1ª divisão do Canadá nas páginas da RSSSF (data/coleta/can-1/rsssf/) com o leitor comum |
| `outras_fontes.py` | Casa os jogos da RSSSF com a ESPN (o ogol entra em 2025 e 2026). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |

- Fontes baixadas: `data/coleta/can-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-concacaf/`, do ogol em `data/cache/ogol-can-1/`.
- Pacote: `data/coleta/can-1/pacote/`; relatório: `docs/coleta/can-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/can-1/importar.py
python coleta/can-1/conferir.py [-v temporada]   # divergências
python coleta/comum-concacaf/testar_carga.py can-1 <scratchpad>
python coleta/comum-concacaf/documentar.py
```

