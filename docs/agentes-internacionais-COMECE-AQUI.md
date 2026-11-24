# Agentes de coleta internacionais: comece aqui

Guia dos agentes de coleta de fora do Brasil, um por confederação:
- **agente Europa:** países da UEFA;
- **agente América do Sul:** países da CONMEBOL, fora o Brasil;
- **agente África:** países da CAF (desde 23/11/2026);
- **agente Ásia:** países da AFC, inclusive a Austrália (desde 23/11/2026);
- **agente Oceania:** países da OFC (desde 23/11/2026);
- **agente América do Norte e Central:** países da CONCACAF, inclusive o Caribe, a Guiana, o Suriname e a Guiana
  Francesa (desde 23/11/2026).

Atualizado em 23/11/2026.

Leia antes, nesta ordem:
1. `docs/COMECE-AQUI.md`: mapa do projeto e regras da casa;
2. `docs/agente-coleta-COMECE-AQUI.md`: o método e o **formato do pacote**, que vale igual para vocês;
3. `docs/coleta/bra-serie-c.md` e o código de `coleta/bra-serie-c/`: um pacote completo, feito pelo agente de coleta do Brasil.

Este arquivo só traz **o que muda** para ligas de fora do Brasil.

## 1. Quem mexe onde

São vários agentes na mesma pasta, no ramo `main`, ao mesmo tempo (fora estes, há o agente de revisão, em `revisao/` e
`docs/revisao/`). Ninguém troca de ramo e cada um só grava no que é seu:

| Agente | Competições | Pastas suas | Pedidos ao agente 1 |
|---|---|---|---|
| Banco e painel (agente 1) | — | `futebol/`, `db/`, `gerar_dashboard_v2.py`, `painel/`, `dashboard_v2.html`, `baixar_escudos.py`, `data/escudos/` | — |
| Coleta Brasil | `bra-*` | `coleta/bra-*`, `coleta/comum/`, `data/coleta/bra-*` | `docs/coleta/pedidos.md` |
| **Coleta Europa** | países da UEFA | `coleta/<slug>/`, `coleta/comum-europa/`, `data/coleta/<slug>/`, `data/cache/*-europa*/` | `docs/coleta/pedidos-europa.md` |
| **Coleta América do Sul** | países da CONMEBOL fora o Brasil | `coleta/<slug>/`, `coleta/comum-sulamerica/`, `data/coleta/<slug>/`, `data/cache/*-sulamerica*/` | `docs/coleta/pedidos-sulamerica.md` |
| **Coleta África** | países da CAF | `coleta/<slug>/`, `coleta/comum-africa/`, `data/coleta/<slug>/`, `data/cache/*-africa*/` | `docs/coleta/pedidos-africa.md` |
| **Coleta Ásia** | países da AFC | `coleta/<slug>/`, `coleta/comum-asia/`, `data/coleta/<slug>/`, `data/cache/*-asia*/` | `docs/coleta/pedidos-asia.md` |
| **Coleta Oceania** | países da OFC | `coleta/<slug>/`, `coleta/comum-oceania/`, `data/coleta/<slug>/`, `data/cache/*-oceania*/` | `docs/coleta/pedidos-oceania.md` |
| **Coleta América do Norte e Central** | países da CONCACAF | `coleta/<slug>/`, `coleta/comum-concacaf/`, `data/coleta/<slug>/`, `data/cache/*-concacaf*/` | `docs/coleta/pedidos-concacaf.md` |

Todos também gravam `data/cache/ogol-<slug>/` e `docs/coleta/<slug>.md` das suas competições.

**Quem fica com cada país:** vale a confederação, não o mapa. Austrália na Ásia (AFC desde 2006); Guiana, Suriname e
Guiana Francesa na CONCACAF; Israel, Cazaquistão, Turquia, Chipre, Armênia, Geórgia e Azerbaijão na Europa. Clube que
joga a liga de outro país entra nela com o país dele (Toronto FC na MLS é `CAN`; Wellington Phoenix na A-League é `NZL`).

O relatório de cada competição vai em `docs/coleta/<slug>.md`. Pode **ler** tudo, inclusive o código dos
outros agentes e o `db/futebol.db` (só leitura: `sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)`).
Commit só com o ok do Guilherme, adicionando só os seus caminhos.

## 2. Nome das competições

- **País:** código FIFA de 3 letras. Exemplos: `ENG`, `SCO`, `ESP`, `ITA`, `GER`, `FRA`, `POR`, `NED`, `BEL`, `ARG`,
  `URU`, `CHI`, `COL`, `PAR`, `PER`, `ECU`, `BOL`, `VEN`; `EGY`, `MAR`, `RSA`; `JPN`, `KOR`, `KSA`, `AUS`; `NZL`, `TAH`;
  `MEX`, `USA`, `CRC`.
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
- **África, Ásia, Oceania e CONCACAF:** a RSSSF é a base (muitas temporadas só têm tabela final ou só o campeão). O ogol
  cobre bem as ligas principais das últimas décadas; a ESPN tem algumas (teste `mex.1`, `usa.1`, `jpn.1`, `ksa.1`,
  `aus.1`, `rsa.1`...). Liga com fonte fraca entra mesmo assim, com o que houver: edição só com campeão, ou só com a
  tabela, é aceita pelo banco (como o Peru de 1912-1921 e a Holanda antes de 1900); edição com parte dos jogos leva
  `formato` começando por "jogos incompletos" (como a Paulista A2 antiga), e o painel avisa.

## 7. Ordem de trabalho

- **Europa:** `eng-1`, `esp-1`, `ita-1`, `ger-1`, `fra-1`, `por-1`, `ned-1`; depois Escócia, Bélgica e Turquia;
  depois as 2ªs divisões das cinco grandes. As 2ªs divisões são o que faz aparecer, no painel, quem subiu e quem caiu.
- **América do Sul:** `arg-1`, `uru-1`, `chi-1`, `col-1`, `par-1`, `per-1`, `ecu-1`, `bol-1`, `ven-1`; depois as 2ªs divisões.
- **África:** `egy-1`, `mar-1`, `tun-1`, `alg-1`, `rsa-1`, `nga-1`, `gha-1`, `cmr-1`, `civ-1`, `cod-1`, `sen-1`, `ang-1`;
  depois as outras 1ªs divisões da CAF.
- **Ásia:** `jpn-1`, `kor-1`, `ksa-1`, `irn-1`, `aus-1`, `chn-1`, `qat-1`, `uae-1`, `uzb-1`, `irq-1`, `ind-1`, `tha-1`;
  depois as outras 1ªs divisões da AFC.
- **Oceania:** `nzl-1`, `tah-1`, `ncl-1`, `fij-1`, `png-1`, `sol-1`, `van-1`, `sam-1`, `tga-1`, `asa-1`, `cok-1`.
- **América do Norte e Central:** `mex-1`, `usa-1`, `crc-1`, `hon-1`, `gua-1`, `slv-1`, `pan-1`, `jam-1`, `tri-1`,
  `can-1`, `hai-1`; depois as outras 1ªs divisões da CONCACAF.

A ordem das 1ªs divisões de cada região é uma sugestão do agente 1; quem decide é o Guilherme.

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
ao agente 1 no seu arquivo de pedidos (seção 10).

## 10. Regras combinadas com o Guilherme (22 e 23/11/2026)

- **Uma competição por vez.** Ao fim de cada uma: resumo curto, pedido de ok para o commit e o **recado de fim de
  coleta**, uma seção "Recado de fim de coleta — <slug> — <data>" no fim do seu arquivo de pedidos, para o agente 1 e
  para o agente de revisão. Entregue o mesmo texto ao Guilherme, num bloco de código. Os 8 itens:
  1. o que foi feito: edições, jogos, clubes, gols com autor, cartões e fontes;
  2. commits;
  3. resultado do teste de carga;
  4. pedidos ao banco e ao painel: o que carregar, formatos novos, colunas vazias, casos especiais;
  5. decisões tomadas (com o motivo) e as que esperam o Guilherme;
  6. o que não deu para coletar e as pendências, com a fonte que poderia resolver;
  7. onde a revisão deve olhar primeiro;
  8. próxima competição.
- **Coleta e revisão:** o agente de revisão confere tudo e deixa um plano por agente em `docs/revisao/`. As correções
  só começam quando o Guilherme manda; até lá, siga com as competições novas.
- **Pasta comum da região:** comece copiando `coleta/comum-sulamerica/` (ogol, ESPN, RSSSF, Wikipédia, teste de carga e
  documentação) para a sua pasta comum, e adapte lá. Não importe código da pasta de outro agente: ele pode mudar.
- **Teste de carga** antes de todo commit: `python coleta/comum-<região>/testar_carga.py <slug> <scratchpad>`; deve
  terminar com `<slug>: N edições, N jogos, N clubes novos -> OK`.
- **Documentação sempre em dia:** depois de toda importação ou correção, rode o seu `documentar.py` e atualize o
  `COMECE-AQUI.md` da sua pasta comum (o que está pronto, de onde continuar, armadilhas). Os dois entram no mesmo
  commit da competição. Outro agente tem que conseguir continuar o seu trabalho só por eles.
- **Git:** nunca `git add -A` nem `git add .`; adicione só os seus caminhos e confira antes que `git diff --cached` está
  vazio (a pasta é compartilhada e outro agente pode estar no meio de um commit). Commit só com o ok explícito do
  Guilherme; push só quando ele pedir. A mensagem termina com
  `Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>`.
- **Logs e conferências** vão para o scratchpad, nunca soltos no repositório.
- **Critério nas dúvidas:** o que for mais fiel à história e ao que a federação do país reconhece. Registre a decisão
  com o motivo no relatório; o que for decisão dele, pergunte ao Guilherme.
- **Bandeiras:** país que nunca foi à Copa do Mundo não tem bandeira no painel; diga no recado quais países novos o
  pacote traz, e o agente 1 baixa a bandeira.
- **Fale com o Guilherme em português, curto e por partes.** Trabalhe sozinho, sem perguntar a cada passo.
