# Plano do banco relacional da Copa do Mundo

## Objetivo

Transformar o payload atual do dashboard das Copas em um banco SQLite relacional,
com nomes de tabelas e colunas em portugues, preservando a rastreabilidade das
fontes e evitando duplicidade de selecoes, jogadores, tecnicos, arbitros e
estadios.

Banco alvo: `db/copa_mundo.db`.

## Padrao adotado

O desenho segue a mesma linha do banco do Brasileirao:

- script criador na raiz: `criar_banco_copa_mundo.py`;
- schema SQL versionado: `sql/schema_copa_mundo.sql`;
- validacao separada: `validar_banco_copa_mundo.py`;
- fonte primaria local: cache/payload usado pelo dashboard em
  `gerar_dashboard_copa_mundo_html.py`.

## Fontes

Fonte primaria operacional:

- Wikipedia PT/cache local, pois e a fonte ja usada pelo dashboard e permite
  reconstruir o HTML offline.

Fontes de cruzamento recomendadas:

- RSSSF: placares, finais, rankings, treinadores, artilheiros e detalhes
  historicos de Copas.
- FIFA: fonte oficial para competicao, estatisticas e fichas quando disponiveis.
- Wikidata: identificador estavel para pessoas e entidades, usado para resolver
  aliases como `Ronaldo`/`Cristiano Ronaldo`.

As fontes entram na tabela `fonte`; correcoes de identidade entram em
`alias_pessoa` e eventuais conflitos em `auditoria_identidade`.

## Modelo fisico inicial

Principais tabelas:

- `competicao`
- `edicao`
- `selecao`
- `alias_selecao`
- `identidade_pessoa`
- `pessoa`
- `alias_pessoa`
- `estadio`
- `fase`
- `grupo`
- `participacao_edicao`
- `partida`
- `gol`
- `escalacao`
- `comando_tecnico`
- `premiacao`
- `auditoria_identidade`

Views iniciais:

- `vw_gols_por_jogador`
- `vw_partidas_resumo`

## Regra de identidade

Pessoa nunca deve ser deduzida apenas pelo texto do nome. O contexto tambem
importa:

- nome/alias;
- selecao;
- papel no dado (`jogador`, `tecnico`, `arbitro`);
- fonte.

Exemplo ja tratado:

- `Portugal + Ronaldo + jogador` aponta para `Cristiano Ronaldo`, com
  `wikidata_id = Q11571`;
- `Brasil + Ronaldo + jogador` permanece separado e nao e mesclado com Cristiano.

Isso evita o problema visto no dashboard: em 2006 Portugal aparece como
`Ronaldo`, mas o jogador correto e Cristiano Ronaldo.

Para casos em que a mesma pessoa aparece em selecoes diferentes ou sucessoras,
`pessoa` permanece contextual por selecao, mas aponta para uma
`identidade_pessoa` global. Isso permite manter estatisticas por selecao e, ao
mesmo tempo, agregar a carreira de uma pessoa. Casos ja implementados:

- Dejan Stankovic: Servia e Montenegro + Servia;
- Nikola Zigic: Servia e Montenegro + Servia;
- Robert Prosinecki: Iugoslavia + Croacia.

`Mazzola` foi revisado como excecao: no Brasil de 1958 e Jose Altafini; na
Italia de 1966 e Sandro Mazzola. Portanto nao deve ser uma identidade global
unica.

## Proximos refinamentos

1. Cruzar aliases de jogadores com Wikidata/DBpedia/FIFA quando houver ID
   publico estavel.
2. Montar uma tabela de auditoria de nomes parecidos por selecao e edicao.
3. Normalizar tecnicos e arbitros com o mesmo mecanismo de `alias_pessoa`.
4. Enriquecer `gol` com assistencias/cartoes/substituicoes quando a fonte tiver
   esses eventos.
5. Adaptar o dashboard para ler do banco ou exportar o mesmo `DATA` a partir do
   SQLite.
