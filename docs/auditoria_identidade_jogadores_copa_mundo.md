# Auditoria de identidade de jogadores da Copa do Mundo

Data: 2026-07-10

## Escopo

Revisao dos nomes de jogadores no banco `db/copa_mundo.db`, com foco em:

- aliases iguais em selecoes diferentes;
- aliases iguais na mesma selecao em edicoes distantes;
- gols contra que estavam contaminando o contexto da pessoa;
- marcadores sem prefixo de selecao atribuidos ao lado errado.

Fontes usadas como base:

- Wikipedia PT/cache local usado pelo dashboard;
- RSSSF como fonte de cruzamento historico;
- FIFA como fonte oficial de competicao;
- Wikidata para IDs estaveis quando aplicavel.

## Correcoes aplicadas

1. `gol` passou a diferenciar:
   - `selecao_id`: selecao creditada no placar;
   - `selecao_autor_id`: selecao do jogador que marcou.

2. Gols contra agora mantem o jogador no contexto da selecao correta. Exemplo:
   `Mandzukic 18' (g.c.)` na final de 2018 credita gol para a Franca, mas o
   autor fica ligado a Croacia.

3. Marcadores sem prefixo passaram a usar o placar para inferir o lado quando
   seguro. Exemplos corrigidos:
   - Colombia 0-2 Inglaterra, 1998: Beckham pertence a Inglaterra;
   - Argentina 0-1 Inglaterra, 2002: Beckham pertence a Inglaterra;
   - Portugal 0-1 Coreia do Sul, 2002: Park Ji-sung pertence a Coreia do Sul.

4. A regex de gol contra foi corrigida. Antes, `g\.?\s*c\.?` era ampla demais
   e podia classificar textos comuns como gol contra. Agora exige `g.c.`/`gc`,
   `contra`, `own goal`, `autogol` ou entrada curada.

5. Aliases curtos dentro da mesma selecao foram separados por ano. Exemplos:
   - Alemanha `Muller`: Gerd Muller (1970/1974) e Thomas Muller (2010/2014);
   - Mexico `Hernandez`: Hector Hernandez (1962), Luis Hernandez (1998) e
     Javier Hernandez (2010/2014/2018);
   - Chile `Sanchez`: Leonel Sanchez (1962) e Alexis Sanchez (2014).

## Resultado validado

`python validar_banco_copa_mundo.py` passou com:

- 23 edicoes;
- 1.057 partidas;
- 89 selecoes;
- 5.044 pessoas;
- 2.971 gols/eventos;
- 9.273 registros de escalacao;
- 0 divergencias entre eventos de gol e placar;
- Portugal + Ronaldo -> Cristiano Ronaldo;
- Brasil + Ronaldo separado de Cristiano Ronaldo.

## Revisao por alias de jogador

| Alias | Contextos encontrados | Decisao |
| --- | --- | --- |
| Aguero | Paraguai:Aguero; Argentina:Aguero | Manter separado. Homonimos por selecao/contexto. |
| Albert | Hungria:Albert; Belgica:Albert | Manter separado. Homonimos por selecao/contexto. |
| Alvarez | Mexico:Alvarez; Argentina:Alvarez | Manter separado. Homonimos por selecao/contexto. |
| Ayala | Paraguai:Ayala; Argentina:Ayala | Manter separado. Homonimos por selecao/contexto. |
| Brown | Estados Unidos:Brown; Argentina:Brown; Alemanha:Brown | Manter separado. Sobrenome/apelido curto em contextos distintos. |
| Campbell | Inglaterra:Campbell; Costa Rica:Campbell | Manter separado. Homonimos por selecao/contexto. |
| Carlos Sanchez | Colombia:Carlos Sanchez; Uruguai:Carlos Sanchez | Manter separado. Jogadores diferentes. |
| Clarke | Inglaterra:Clarke; Irlanda do Norte:Clarke | Manter separado. Homonimos por selecao/contexto. |
| Collins | Escocia:Bobby Collins; Escocia:John Collins | Corrigido. Separado por ano dentro da Escocia. |
| de Jong | Paises Baixos:Theo de Jong; Paises Baixos:Frenkie de Jong | Corrigido. Separado por ano dentro dos Paises Baixos. |
| Dejan Stankovic | Servia e Montenegro:Dejan Stankovic; Servia:Dejan Stankovic | Resolvido com `identidade_pessoa` global: Dejan Stankovic. |
| Delgado | Equador:Delgado; Angola:Delgado | Manter separado. Homonimos por selecao/contexto. |
| Dembele | Belgica:Dembele; Franca:Dembele | Manter separado. Jogadores diferentes. |
| Diaz | Mexico:Diaz; Peru:Diaz; Argentina:Diaz; Colombia:Diaz | Manter separado. Sobrenome curto em varias selecoes. |
| Diop | Senegal:Diop; Marrocos:Diop | Manter separado. Homonimos por selecao/contexto. |
| Eder | Brasil:Eder; Portugal:Eder | Manter separado. Jogadores diferentes. |
| Eriksen | Dinamarca:John Eriksen; Dinamarca:Christian Eriksen | Corrigido. Separado por ano dentro da Dinamarca. |
| Falcao | Brasil:Falcao; Colombia:Falcao | Manter separado. Falcao brasileiro e Radamel Falcao. |
| Flores | Mexico:Flores; Costa Rica:Flores | Manter separado. Homonimos por selecao/contexto. |
| Fonseca | Uruguai:Fonseca; Mexico:Fonseca | Manter separado. Homonimos por selecao/contexto. |
| Gonzalez | Mexico:Gonzalez; Costa Rica:Gonzalez; Chile:Gonzalez | Manter separado. Sobrenome curto em varias selecoes. |
| Hernandez | Mexico:Hector Hernandez; Mexico:Luis Hernandez; Mexico:Javier Hernandez | Corrigido. Separado por ano dentro do Mexico. |
| Juanito | Espanha:Juan Gomez; Espanha:Juan Gutierrez Moreno | Corrigido. Separado por ano dentro da Espanha. |
| Junior | Brasil:Leovegildo Junior; Brasil:Jenilson Angelo de Souza | Corrigido. Separado por ano dentro do Brasil. |
| Koller | Austria:Koller; Tchequia:Koller | Manter separado. Homonimos por selecao/contexto. |
| Lopez | Franca:Lopez; Argentina:Lopez | Manter separado. Homonimos por selecao/contexto. |
| Lozano | Colombia:Lozano; Mexico:Lozano | Manter separado. Homonimos por selecao/contexto. |
| Marcos | Chile:Marcos; Brasil:Marcos | Manter separado. Homonimos por selecao/contexto. |
| Martinez | Colombia:Martinez; Argentina:Martinez | Manter separado. Sobrenome curto em selecoes distintas. |
| Mazzola | Brasil:Jose Altafini; Italia:Sandro Mazzola | Corrigido. Nao e identidade global unica; Brasil 1958 e Jose Altafini, Italia 1966 e Sandro Mazzola. |
| Mokoena | Africa do Sul:Aaron Mokoena; Africa do Sul:Teboho Mokoena | Corrigido. Separado por ano dentro da Africa do Sul. |
| Muller | Alemanha:Gerd Muller; Brasil:Muller; Alemanha:Thomas Muller | Corrigido para Alemanha por ano; Brasil permanece separado. |
| Muntari | Gana:Muntari; Catar:Muntari | Manter separado. Homonimos por selecao/contexto. |
| Murray | Escocia:Murray; Estados Unidos:Murray | Manter separado. Homonimos por selecao/contexto. |
| Musa | Nigeria:Musa; Croacia:Musa | Manter separado. Homonimos por selecao/contexto. |
| Nakamura | Japao:Shunsuke Nakamura; Japao:Nakamura | Parcialmente corrigido. 2006 identificado como Shunsuke Nakamura; falta confirmar nome completo do Nakamura de 2026. |
| Nikola Zigic | Servia e Montenegro:Nikola Zigic; Servia:Nikola Zigic | Resolvido com `identidade_pessoa` global: Nikola Zigic. |
| Oscar | Brasil:Jose Oscar Bernardi; Brasil:Oscar | Corrigido. Separado por ano dentro do Brasil. |
| Pedro | Espanha:Pedro; Brasil:Pedro | Manter separado. Jogadores diferentes. |
| Pepe / Pepe | Portugal:Pepe; Costa do Marfim:Pepe | Manter separado. Jogadores diferentes. |
| Petit | Franca:Petit; Portugal:Petit | Manter separado. Jogadores diferentes. |
| Petkovic | Iugoslavia:Petkovic; Croacia:Petkovic | Manter separado. Jogadores diferentes por epoca/contexto. |
| Prosinecki | Iugoslavia:Prosinecki; Croacia:Prosinecki | Resolvido com `identidade_pessoa` global: Robert Prosinecki. |
| Ramirez | Chile:Ramirez; El Salvador:Ramirez | Manter separado. Homonimos por selecao/contexto. |
| Rodriguez | Espanha:Rodriguez; Uruguai:Rodriguez; Argentina:Rodriguez; Colombia:Rodriguez | Manter separado. Sobrenome curto em varias selecoes. |
| Ronaldo | Brasil:Ronaldo; Portugal:Cristiano Ronaldo | Corrigido. Portugal `Ronaldo` aponta para Cristiano Ronaldo; Brasil permanece separado. |
| Sanchez | Chile:Leonel Sanchez; Mexico:Hugo Sanchez; Chile:Alexis Sanchez | Corrigido no Chile/Mexico por ano; contextos permanecem separados. |
| Soler | Franca:Soler; Espanha:Soler | Manter separado. Homonimos por selecao/contexto. |
| Toth | Hungria:Mihaly Toth; Hungria:Jozsef Toth | Corrigido. Separado por ano dentro da Hungria. |
| Trezeguet | Franca:Trezeguet; Egito:Trezeguet | Manter separado. Jogadores diferentes. |
| Valdivia | Mexico:Valdivia; Chile:Valdivia | Manter separado. Jogadores diferentes. |
| Valencia | Colombia:Valencia; Equador:Valencia | Manter separado. Homonimos por selecao/contexto. |
| Varela | Uruguai:Varela; Portugal:Varela | Manter separado. Homonimos por selecao/contexto. |
| Vargas | Chile:Vargas; Costa Rica:Vargas; Suica:Vargas | Manter separado. Sobrenome curto em varias selecoes. |
| Wright | Inglaterra:Wright; Costa Rica:Wright; Estados Unidos:Wright | Manter separado. Homonimos por selecao/contexto. |
| Zidane | Argelia:Zidane; Franca:Zidane | Manter separado. Djamel Zidane e Zinedine Zidane. |

## Pendencias reais

1. Confirmar o nome completo do `Nakamura` do Japao em 2026 antes de fixar alias
   definitivo.

2. Expandir Wikidata IDs para os aliases corrigidos por ano. Hoje IDs foram
   preenchidos apenas nos casos de maior confianca ja conhecidos, como Cristiano
   Ronaldo, Ronaldinho Gaucho, Gerd Muller e Thomas Muller.

## Pendencias resolvidas

Foi criada a tabela `identidade_pessoa` e a FK `pessoa.identidade_pessoa_id`.
Com isso, a pessoa contextual por selecao continua existindo, mas os casos abaixo
agora tambem compartilham uma identidade global:

- Dejan Stankovic: Servia e Montenegro + Servia;
- Nikola Zigic: Servia e Montenegro + Servia;
- Robert Prosinecki: Iugoslavia + Croacia.

`Mazzola` foi revisado durante a implementacao da identidade global e ficou
separado: Jose Altafini no Brasil e Sandro Mazzola na Italia.
