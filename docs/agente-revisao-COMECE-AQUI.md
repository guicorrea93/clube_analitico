# Agente de revisão: comece aqui

Guia do agente que **revisa o que já está no painel** do Clube Analítico, competição por competição e item por
item, para saber se as informações estão certas. Atualizado em 20/11/2026.

Leia antes: `docs/COMECE-AQUI.md` (mapa do projeto e regras da casa). Para entender de onde vem cada dado, leia
também o relatório de coleta da competição que for revisar (`docs/serie_b_coleta.md`, `docs/coleta/<slug>.md`).

## 1. Sua missão

Dizer, com prova, o que está **certo**, **errado** ou **em dúvida** em cada competição do painel. Você **não corrige**
dados nem código: registra o achado e diz quem deve corrigir. Pode trabalhar sozinho ou dividir o trabalho com
subagentes, uma competição ou um bloco de itens para cada um. A escolha é sua.

## 2. Onde você pode mexer

- `revisao/`: seus scripts de conferência.
- `docs/revisao/<slug>.md`: o relatório de cada competição.
- `docs/revisao/achados.csv`: todos os achados, numa tabela só (formato na seção 5).
- `data/cache/revisao/`: páginas baixadas para conferir. Fica fora do git.

Só **leitura** no resto:
- `db/futebol.db`, aberto com `sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)`;
- os dados do painel em `painel/dados/<slug>.js`, que são um JSON depois de `window.DADOS_COMP = `;
- os pacotes em `data/coleta/<slug>/pacote/` e o código de todos.

Logs e saídas temporárias vão para o scratchpad. Faça commit só com o ok do Guilherme, adicionando só os seus caminhos.

## 3. O que conferir (para cada competição)

Ordem sugerida: Série A, Série B, Série C, Série D e Copa do Brasil. Depois, as competições novas que forem entrando
no seletor do painel.

**A. Edições e títulos**
- A lista de edições é a oficial: nenhuma sobrando, nenhuma faltando. O nome de cada época está certo
  (Taça Brasil, Robertão, Taça de Prata...).
- Campeão, vice e 3º de cada edição conferem com a entidade oficial (CBF ou federação) e mais uma fonte.

**B. Classificação final de cada edição**
- Posição, jogos, vitórias, empates, derrotas, gols pró e contra, e pontos, contra uma tabela publicada (RSSSF, Wikipédia).
- Punições de pontos e casos de tribunal estão aplicados e explicados.
- Clube que subiu e clube que caiu: confira a sub-aba **Participantes** do painel contra a realidade.

**C. Jogos**
- Total de jogos por edição.
- Amostra de placares e datas contra outra fonte. Varie a época: uma edição antiga, uma do meio e uma recente,
  no mínimo 20 jogos por edição.
- Jogos de W.O., anulados e decididos no tribunal.

**D. Gols e artilheiros**
- Artilheiro de cada edição contra a lista oficial.
- Soma dos gols com autor por jogo nunca maior que o placar.

**E. Clubes**
- Mesmo clube com dois nomes (cadastros duplicados).
- Clubes diferentes juntados num nome só. Já aconteceu: GE Novorizontino e Grêmio Novorizontino.
- Estado ou país errado; nome de exibição estranho.
- **Escudo errado:** monte uma folha com os escudos e nomes (ver `baixar_escudos.py` e `data/escudos/`) e olhe um a um.

**F. Painel, aba por aba**
- História, Por campeonato e Por clube: os números de cada cartão, gráfico e tabela batem com o banco.
- Recordes e curiosidades fazem sentido (maior goleada, maior sequência...). Confira os principais numa fonte.
- Textos, legendas e avisos certos para aquela competição.
- Telas: abra o painel (`painel/index.html?c=<slug>#aba/subaba/item`) num navegador sem janela (Chrome `--headless`)
  e veja se não há erro nem tela quebrada. Olhe também o celular (largura de 420 px).

Quando um item for grande demais para conferir inteiro, confira uma **amostra** e diga no relatório qual foi.

## 4. Fontes para conferir

Use fontes **diferentes** das que a coleta usou como base, sempre que der. A coleta de cada competição diz quais
usou no relatório dela.
- Wikipédia (pt, en, es): campeões, tabelas finais, artilheiros;
- RSSSF;
- ogol / zerozero;
- CBF e federações.

Guarde o endereço de cada prova.

## 5. Como registrar

**`docs/revisao/achados.csv`**: `id,competicao,item,edicao,clube,o_que_esta_no_painel,o_que_a_fonte_diz,fonte,gravidade,quem_corrige,situacao`
- `gravidade`:
  - `alta`: título, campeão, rebaixamento ou classificação errados;
  - `media`: placar, número ou clube errado;
  - `baixa`: texto, escudo, detalhe.
- `quem_corrige`: `coleta-brasil`, `coleta-europa`, `coleta-sulamerica` ou `banco-painel`.
- `situacao`: `aberto`, `corrigido` ou `nao-e-erro`. Quando o achado for corrigido e você conferir de novo, atualize.

**`docs/revisao/<slug>.md`**: para cada bloco (A a F), o que foi conferido, o tamanho da amostra, o resultado
(ok, achados) e as fontes. No topo, um resumo de 3 linhas.

**Recado aos outros agentes:** escreva no arquivo de pedidos de quem corrige:
- `docs/coleta/pedidos.md` (Brasil), `pedidos-europa.md` ou `pedidos-sulamerica.md`;
- `docs/revisao/pedidos-painel.md`, quando for comigo (banco e painel).

Cite os `id`s dos achados.

## 6. Como conversar com o Guilherme

Em português, curto e por partes. Ao fim de cada competição, mande:
- o resumo: quantos itens conferidos, quantos certos e quantos achados por gravidade;
- os 3 achados mais importantes.

Siga sozinho, sem pedir confirmação a cada passo. Pergunte **só** quando a dúvida for de decisão. Exemplos:
- qual título reconhecer;
- se dois clubes são o mesmo.
