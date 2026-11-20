# Agentes de coleta internacionais: comece aqui

Guia de dois agentes do Clube Analítico:
- **agente Europa:** ligas nacionais europeias;
- **agente América do Sul:** ligas nacionais sul-americanas, fora o Brasil.

Atualizado em 20/11/2026.

Leia antes, nesta ordem:
1. `docs/COMECE-AQUI.md`: mapa do projeto e regras da casa;
2. `docs/agente-coleta-COMECE-AQUI.md`: o método e o **formato do pacote**, que vale igual para vocês;
3. `docs/coleta/bra-serie-c.md` e o código de `coleta/bra-serie-c/`: um pacote completo, feito pelo agente de coleta do Brasil.

Este arquivo só traz **o que muda** para ligas de fora do Brasil.

## 1. Quem mexe onde

São quatro agentes na mesma pasta, no ramo `main`. Ninguém troca de ramo e cada um só grava no que é seu:

| Agente | Competições | Pastas suas | Pedidos ao agente 1 |
|---|---|---|---|
| Banco e painel (agente 1) | — | `futebol/`, `db/`, `gerar_dashboard_v2.py`, `dashboard_v2.html`, `baixar_escudos.py`, `data/escudos/` | — |
| Coleta Brasil | `bra-*` | `coleta/bra-*`, `coleta/comum/`, `data/coleta/bra-*` | `docs/coleta/pedidos.md` |
| **Coleta Europa** | países da UEFA | `coleta/<slug>/`, `coleta/comum-europa/`, `data/coleta/<slug>/`, `data/cache/*-europa*/` | `docs/coleta/pedidos-europa.md` |
| **Coleta América do Sul** | países da CONMEBOL fora o Brasil | `coleta/<slug>/`, `coleta/comum-sulamerica/`, `data/coleta/<slug>/`, `data/cache/*-sulamerica*/` | `docs/coleta/pedidos-sulamerica.md` |

O relatório de cada competição vai em `docs/coleta/<slug>.md`. Pode **ler** tudo, inclusive o código dos
outros agentes e o `db/futebol.db` (só leitura: `sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)`).
Commit só com o ok do Guilherme, adicionando só os seus caminhos.

## 2. Nome das competições

- **País:** código FIFA de 3 letras. Exemplos: `ENG`, `SCO`, `ESP`, `ITA`, `GER`, `FRA`, `POR`, `NED`, `BEL`, `ARG`,
  `URU`, `CHI`, `COL`, `PAR`, `PER`, `ECU`, `BOL`, `VEN`.
- **Slug:** `<país em minúsculas>-<divisão>`. Exemplos: `eng-1` (1ª divisão inglesa), `eng-2`, `esp-1`, `arg-1`.
  A divisão fica fixa no slug e o nome de cada época fica na edição. A 1ª divisão inglesa é o mesmo `eng-1`
  de 1888 até hoje: `nome_oficial` "Football League First Division" até 1991/92 e "Premier League" depois.
- **`competicao.json`:** além dos campos do guia, preencha:
  ```json
  {"slug": "eng-1", "nome": "Campeonato Inglês", "nome_curto": "Inglês", "tipo": "liga", "nivel": 1,
   "pais": "ENG", "pais_nome": "Inglaterra", "regiao": null, "confederacao": "UEFA",
   "rotulo_painel": "Inglês", "menu_painel": "Inglaterra · 1ª divisão",
   "do_painel": "do Campeonato Inglês", "o_painel": "o Campeonato Inglês", "observacao": "..."}
  ```
  `do_painel` e `o_painel` entram nos títulos e frases do painel ("História do Campeonato Inglês").
  O painel monta o seletor sozinho a partir desses campos.

## 3. Temporadas

- **Temporada que cruza o ano:** `temporada` "1992/93", `ano_inicio` 1992, `ano_fim` 1993.
- **Ano fechado** (a maioria na América do Sul): `temporada` "2019".
- **Mais de um campeão oficial no ano** (Apertura e Clausura, Metropolitano e Nacional...): **uma edição por
  torneio que deu título**, com `temporada` única, por exemplo "1967 Metropolitano" e "1967 Nacional", e o
  `ano_inicio` igual. Torneio que só classificava para uma final do ano entra como **fase** da edição, não como edição.
  A regra vale para os dois agentes; na dúvida, siga o que a federação do país reconhece como título.
- **Pontos por vitória:** 2 até a mudança de cada país (a Inglaterra passou a 3 em 1981/82, a maioria nos anos 1990).
  Confira país a país.

## 4. Clubes: o nome tem que ser único no mundo

O painel identifica o clube pelo **nome de exibição**, e o carregador **recusa** o pacote se um nome já for de
outro país (erro `NomeRepetido`; nada da competição é gravado).

- Use o nome pelo qual o clube é conhecido no Brasil: "Bayern de Munique", "Manchester United", "Juventus",
  "Boca Juniors", "River Plate", "Peñarol".
- **Homônimos:** antes de fechar o pacote, confira o nome contra o `futebol.db` (todos os países) **e** contra os
  `clubes.csv` dos outros pacotes (`data/coleta/*/pacote/clubes.csv`). Se o nome já existir, quem chega depois
  acrescenta a cidade: "Liverpool de Montevideo", "Everton de Viña del Mar", "Arsenal de Sarandí",
  "Racing de Montevideo", "Barcelona de Guayaquil". Clube brasileiro nunca muda de nome por isso.
- O mesmo clube **dentro** do seu país é um só em todas as divisões. Mantenha um cadastro comum, como o
  `coleta/comum/clubes_ogol.json` do agente Brasil (código do ogol → nome).
- `pais` de cada clube é o país dele, não o da liga. Ex.: Cardiff e Swansea são `WAL` na liga inglesa.
  O país que ainda não está no banco vai em `paises.csv` no pacote (`codigo,nome,confederacao`).
- `regiao` é a província ou o estado, quando fizer sentido. Pode ficar vazio.

## 5. Escudos

O agente 1 baixa os escudos pelos calendários do ogol/zerozero que **vocês guardam**. Para isso funcionar:
- guarde as páginas de calendário em `data/cache/ogol-<slug>/calendario_<ano_inicio>_<id da edição>_p<página>.html`.
  O ano no nome do arquivo é o `ano_inicio` da temporada;
- no `nomes_fonte` de cada clube, ponha a grafia do ogol com os anos (de `ano_inicio`): `ogol:Man. United:1992-2025`.

## 6. Fontes para começar (confira antes de confiar)

- **RSSSF** (rsssf.org): tabelas e resultados de quase todos os países, com histórico longo. É a melhor base de conferência.
- **ogol / zerozero:** calendário de cada edição com placar, rodada, código do clube e escudo. Mesmo modelo do
  `serie_b/ogol.py` e do `coleta/bra-serie-c/`.
- **Wikipédia** (en/es/pt): tabelas finais ("Sports table"), punições e lista de campeões.
- **Só Europa:**
  - football-data.co.uk: CSV de resultados das ligas principais desde os anos 1990, com estatísticas nas temporadas recentes;
  - o pacote `engsoccerdata` (GitHub): resultados históricos da Inglaterra e de outras ligas. Confira cobertura e licença.
- **Só América do Sul:** RSSSF é muito forte para Argentina, Uruguai e Chile. A ESPN tem ligas sul-americanas
  (teste os códigos, como `arg.1`).

## 7. Ordem de trabalho

- **Europa:** `eng-1`, `esp-1`, `ita-1`, `ger-1`, `fra-1`, `por-1`, `ned-1`; depois Escócia, Bélgica e Turquia;
  depois as 2ªs divisões das cinco grandes. As 2ªs divisões são o que faz aparecer, no painel, quem subiu e quem caiu.
- **América do Sul:** `arg-1`, `uru-1`, `chi-1`, `col-1`, `par-1`, `per-1`, `ecu-1`, `bol-1`, `ven-1`; depois as 2ªs divisões.

Uma competição por vez, do começo da história até a última temporada terminada.

## 8. Extras que valem a pena

- **`classificacao_rodada.csv`** nas temporadas de pontos corridos. Pode ser calculada dos jogos, rodada a rodada.
  Ela liga a "Corrida rodada a rodada" no painel.
- **`zona`** da classificação, quando se sabe: `titulo`, `champions`, `europa`, `conference`, `libertadores`,
  `sula`, `acesso`, `playoff`, `rebaixamento` ou `meio`.
- **Punições, jogos anulados e decisões de tribunal:** sempre no relatório, com a fonte.

## 9. Quando o pacote está pronto

Os mesmos critérios do guia de coleta, mais:
- nenhum nome de clube repetido com outro país;
- `competicao.json` com os campos do painel.

Avise o Guilherme com um resumo curto: edições, jogos, gols com autor, o que faltou e por quê. Escreva o recado
ao agente 1 no seu arquivo de pedidos.
