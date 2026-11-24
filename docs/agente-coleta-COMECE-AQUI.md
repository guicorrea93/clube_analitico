# Agente de coleta: comece aqui

Guia do segundo agente do Clube Analítico, o que coleta competições novas. Antes deste, leia
`docs/COMECE-AQUI.md` (mapa do projeto e regras da casa). Atualizado em 20/11/2026.

## 1. Sua missão

Levantar **todas as edições** de cada competição, com **tudo o que as fontes oferecerem**: jogos,
fase, grupo, rodada, data e hora, estádio, público, autores dos gols, cartões, classificação final,
punições, artilheiros. Cada competição vira um **pacote** de arquivos num formato fixo (seção 4).
O agente 1 carrega o pacote no `db/futebol.db` e leva a competição para o painel.

Ordem de prioridade (o Guilherme pode mudar):

1. **Brasileirão Série C** (`bra-serie-c`)
2. **Brasileirão Série D** (`bra-serie-d`)
3. **Estaduais**, começando pelos maiores: Paulista, Carioca, Mineiro, Gaúcho (`bra-sp-1`, `bra-rj-1`...; regras na seção 6b)
4. **Ligas nacionais estrangeiras:** primeiro as principais da Europa e da América do Sul, depois
   África e Ásia (`eng-premier-league`, `esp-la-liga`, `arg-primera`...)

Trabalhe **uma competição por vez** e só passe à próxima quando o pacote estiver conferido.

## 2. Onde você pode mexer

- `coleta/<slug>/`: seus scripts. Exemplo: `coleta/bra-serie-c/rsssf.py`, `importar.py`.
- `data/coleta/<slug>/`: fontes baixadas (páginas, JSON) e o pacote final em `data/coleta/<slug>/pacote/`.
- `docs/coleta/<slug>.md`: relatório da coleta, ano a ano.
- `coleta/comum/`: código que serve a várias competições (leitor genérico, casamento de nomes...).

**Não mexa** em nada fora disso. Isso inclui `db/`, `futebol/`, `serie_b/`, `historico/`,
`gerar_dashboard_v2.py`, os `dashboard*.html` e `data/escudos/`. Pode **ler** o `db/futebol.db`
(abra com `sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)`) e copiar ideias do `serie_b/`.
Se precisar mudar algo de fora, escreva o pedido em `docs/coleta/pedidos.md` e avise o Guilherme.

Os dois agentes trabalham na mesma pasta e no ramo `main`. Não troque de ramo. Faça commit só
com aprovação e adicione só os seus caminhos (`git add coleta/bra-serie-c data/coleta/bra-serie-c docs/coleta/bra-serie-c.md`).
O cache bruto de download vai em `data/cache/` (fora do git). O que é fonte guardada de verdade
vai em `data/coleta/<slug>/` (no git, como `data/serie_b/`).

## 3. Como foi feita a Série B (copie o método)

O código está em `serie_b/` e o relatório em `docs/serie_b_coleta.md`.

1. **Fonte base com conferência:** as páginas da RSSSF Brasil (`data/serie_b/rsssfbrasil/br{ano}l2.htm`).
   O leitor (`serie_b/rsssf.py`) pega fases, grupos, rodadas, datas, jogos e autores dos gols.
   A função `conferir` soma os jogos lidos e compara com cada tabela publicada na página.
   É isso que prova que a página foi lida inteira e certa.
2. **Identidade dos clubes** (`serie_b/clubes.py`): cada nome de cada ano vira clube + estado.
   O estado sai, nesta ordem, de: sufixo no nome ("América-RN") → lista de participantes →
   tabela do grupo → decisão manual (`MANUAL`) → mesmo nome em outros anos.
3. **Outras fontes, casadas por nome** (`serie_b/nomes.py`):
   - ESPN (`site.api.espn.com/apis/site/v2/sports/soccer/bra.2/scoreboard?dates=AAAAMMDD`, um dia por pedido, 2010+): hora, estádio, público, gols e cartões com minuto;
   - ogol (`www.ogol.com.br/edicao/-/{id}/calendario?page=N`): rodada oficial ("R12") e conferência de placar;
   - Wikipédia (API, wikitexto): tabela final oficial e punições ("Sports table"), matriz de resultados ("Sports results").
4. **Desempate entre fontes:** quando RSSSF e ESPN discordam do placar, a matriz da Wikipédia decide.
   Jogo que falta numa fonte entra pela outra, e isso fica registrado no relatório.
5. **Relatório por ano:** fontes usadas, jogos, gols, quantos têm autor, rodada, campeão e
   ocorrências (W.O., tribunal, jogo anulado).

Armadilhas que já apareceram:
- nomes de jogador lidos como data ("Mario" virando "Mar");
- virada de ano errada nas datas;
- dois clubes com o mesmo nome no mesmo ano (os dois "Nacional" de 1989);
- página da RSSSF que para no meio da temporada;
- evento de gol da ESPN que não bate com o placar (descartado e registrado);
- jogo decidido no tribunal sem placar na fonte (entra como `awd`, com o placar dado pelo tribunal).

## 4. O pacote (formato de entrega)

Pasta `data/coleta/<slug>/pacote/`, em UTF-8, CSV separado por vírgula com cabeçalho. Clubes
aparecem pelo **nome de exibição** (coluna `clube` do `clubes.csv`), nunca por id.

**`competicao.json`**
```json
{"slug": "bra-serie-c", "nome": "Campeonato Brasileiro Série C", "nome_curto": "Série C",
 "tipo": "liga", "nivel": 3, "pais": "BRA", "regiao": null, "confederacao": "CONMEBOL",
 "observacao": "inclui ...", "rotulo_painel": "Série C", "menu_painel": "Brasileirão Série C"}
```
`tipo`: `liga`, `copa`, `estadual`, `continental` ou `mundial`. Opcionais para o painel: `pais_nome`, `do_painel`
("da Série C") e `o_painel` ("a Série C"); sem eles, o painel usa "da/a" + `rotulo_painel`. O seletor do painel
lê esses campos sozinho.

**Nomes de clube únicos no mundo:** o carregador recusa um nome que já seja de clube de outro país (veja
`docs/agentes-internacionais-COMECE-AQUI.md`, seção 4). `pais`: código ISO de 3 letras.
`regiao`: a UF, só nos estaduais.

**`clubes.csv`**: `clube,regiao,cidade,pais,nomes_fonte`
- `clube`: o nome de exibição. **Se o clube já existe no `futebol.db`, use exatamente o
  `clube.nome` de lá.** Confira em `clube` e `clube_nome`; ex.: "Botafogo-PB", "Brasil de Pelotas".
  Clube novo segue o mesmo padrão: nome curto, com "-UF" quando há outro com o mesmo nome. Nunca renomeie um clube
  que já está no banco, mesmo que o sufixo pareça sobrar (decisão de 21/11/2026).
- `nomes_fonte`: todas as grafias vistas, com fonte e anos, separadas por `|`.
  Ex.: `rsssf:Botafogo/PB:1981-1999|espn:Botafogo-PB:2010-2025`.

**`edicoes.csv`**: `temporada,ano_inicio,ano_fim,nome_oficial,num_clubes,pontos_vitoria,formato,campeao,vice,fontes,observacao`
- `temporada`: "2019" ou "2019/20".
- `formato`: texto curto; use `mata-mata` quando a edição inteira for eliminatória.
- Colunas opcionais (o pacote que não as tem continua valendo):
  - `co_campeao`, logo depois de `vice`: o outro campeão de um título dividido (D-07; Paulista 1973, Carioca 1907);
  - `pontos_empate` e `pontos_derrota`, logo depois de `pontos_vitoria`: vazias valem 1 e 0. Preencha quando a liga
    pontuava de outro jeito (Marrocos 3-2-1 de 1933/34 a 1994/95; Taiti 4-2-1). O painel usa as três na Corrida, nos
    duelos e nas campanhas. Ponto por gol, shootout e bônus não cabem aqui: vão no `ajuste_pontos`, ou, se a
    classificação traz os pontos oficiais, o painel usa esses pontos na tabela da edição (24/11/2026).

**`fases.csv`**: `temporada,ordem,fase,tipo,num_grupos,formato_serie,criterio`
- `tipo`: `liga`, `grupos` ou `mata_mata`.
- `formato_serie`: `pontos_corridos`, `jogo_unico`, `ida_volta` ou `melhor_de_3`.

**`partidas.csv`**: `id,temporada,fase,grupo,rodada,data,hora,mandante,visitante,gols_mandante,gols_visitante,penaltis_mandante,penaltis_visitante,resultado_especial,estadio,cidade,publico,fonte,fonte_id,gols_texto,observacao`
- `id`: único no pacote. Ex.: `2019-0123`.
- `data`: AAAA-MM-DD.
- Placar oficial, já com a prorrogação.
- `resultado_especial`: `awd` (tribunal), `wo`, `abd` (abandonado) ou `n/p` (não jogado).
- `gols_texto`: os autores como a fonte escreve, quando não deu para separar.

**`gols.csv`**: `partida_id,clube,jogador,minuto,acrescimo,tipo,fonte`
- `clube` é quem ganhou o gol. No gol contra, é o adversário de quem chutou.
- `tipo`: `normal`, `penalti`, `contra` ou `falta`.
- Só grave os gols de um jogo quando a soma bater com o placar.

**`cartoes.csv`**: `partida_id,clube,jogador,minuto,acrescimo,cor,fonte`. `cor`: `amarelo` ou `vermelho`.

**`classificacao_final.csv`**: `temporada,posicao,clube,jogos,vitorias,empates,derrotas,gols_pro,gols_contra,pontos,ajuste_pontos,situacao,fonte,observacao`
- `ajuste_pontos`: punição negativa ou bônus.
- `situacao`: `campeao`, `acesso`, `rebaixado`, `classificado`...
- Ordem: a oficial. Quando não houver, calcule e diga isso em `observacao`.

**`classificacao_rodada.csv`** (opcional, só pontos corridos): `temporada,rodada,clube,posicao,pontos,jogos,vitorias,empates,derrotas,gols_pro,gols_contra,zona`
- `zona`: `titulo`, `acesso`, `libertadores`, `sula`, `rebaixamento` ou `meio`.

**`tabelas_publicadas.csv`**: `temporada,fase,grupo,posicao,nome_fonte,clube,jogos,vitorias,empates,derrotas,gols_pro,gols_contra,pontos,fonte`
- As tabelas como a fonte publica. Servem de prova da conferência.

**`artilheiros.csv`**: `temporada,jogador,clube,gols,fonte`.

**`conferencia.csv`**: `temporada,jogos,jogos_esperados,tabelas_conferidas,tabelas_divergentes,gols,gols_com_autor,observacao`
- Uma linha por edição. É a primeira coisa que o agente 1 olha.

Junto do pacote vai o relatório `docs/coleta/<slug>.md`, com o mesmo modelo de `docs/serie_b_coleta.md`.

## 5. Quando o pacote está pronto

- Toda edição tem jogos, ou está explicado no relatório por que não tem.
- `conferencia.csv` sem divergência sem explicação. Cada divergência fica justificada no relatório
  e corrigida no código, com o motivo.
- Campeão de cada edição conferido com uma segunda fonte (Wikipédia ou ogol).
- Nenhum clube repetido com dois nomes, e nenhum nome que já existe no `futebol.db` com grafia diferente.
- Então: avise o Guilherme com um resumo curto e peça aprovação para o commit.

## 6. Pontos de partida para a Série C (confira antes de confiar)

- **RSSSF Brasil:** a Série B usou `br{ano}l2.htm`. Para a Série C, o provável é `br{ano}l3.htm`.
  Abra o índice do site e confirme quais anos existem.
- **Anos da Série C:** a competição existe desde 1981, com interrupções (houve anos sem Série C).
  Levante a lista certa na Wikipédia e no ogol antes de coletar.
- **ESPN:** a Série B é a liga `bra.2`. Teste se `bra.3` responde e desde que ano.
- **ogol:** cada edição tem um id; a lista da Série B está em `serie_b/ogol.py` (`EDICOES`). Monte a da C.
- **Série D (2009+):** muitos clubes novos no banco; capriche na identidade e no estado de cada um.

## 6b. Estaduais

- **Slug:** `bra-<uf>-<divisão>`. Exemplos: `bra-sp-1` (1ª divisão paulista, de 1902 até hoje), depois `bra-sp-2` (A2).
  O nome de cada época vai em `nome_oficial` (ex.: "Série A1").
- **`competicao.json`:** `"tipo": "estadual"`, `"regiao": "SP"`, `"nivel": 1`, `"rotulo_painel": "Paulista"`,
  `"menu_painel": "Paulista"`, `"do_painel": "do Paulistão"`, `"o_painel": "o Paulistão"`.
  No painel, "subiu" e "caiu" são contados entre as divisões do **mesmo estado** (`bra-sp-1` ↔ `bra-sp-2`).
- **Ano com dois campeões** (ligas rivais, como LPF e APEA em 1913–1916 e 1926–1929): uma edição por torneio que a
  federação reconhece como título, com `temporada` única (ex.: "1913 LPF", "1913 APEA"). É a mesma regra do
  guia internacional.
- **Mesmo clube com outro nome** (Palestra Itália → Palmeiras): um clube só, com o nome atual, e os nomes antigos
  no `nomes_fonte`.
- **Clube antigo homônimo de um clube do banco** (ex.: um "Internacional" paulista dos anos 1900): **nunca** use
  o nome exato de um clube do banco para outro clube, porque o carregador junta os dois. Diferencie: "Internacional-SP".
- **Continuidade discutida** (ex.: São Paulo da Floresta, 1930–1935, e o São Paulo de hoje): não decida sozinho.
  Escreva o caso em `docs/coleta/pedidos.md`, com as fontes, e pergunte ao Guilherme.

## 7. Como conversar com o Guilherme

Em português, curto e por partes. Diga o que fez, o que achou e o que precisa dele. Não peça
confirmação para cada passo da coleta: ele prefere que o agente siga sozinho e mostre o resultado.
Peça aprovação **só** para commit/push e para decisões de identidade que mudam dados que já estão
no banco (ex.: dizer que dois clubes existentes são o mesmo).
