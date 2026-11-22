# Briefing comum dos subagentes de revisão (Clube Analítico)

Projeto: C:\Users\guilhermecorrea\Downloads\Gui\GitHub\clube_analitico (abaixo, "projeto").
Scratchpad: <scratchpad da sessão> (abaixo, "SCRATCH").

## Leia antes de começar (inteiros)
- projeto/docs/COMECE-AQUI.md
- projeto/docs/agente-revisao-COMECE-AQUI.md (o guia da revisão: blocos A a F, gravidades, formato do CSV)
- o relatório de coleta da sua competição (ver a sua tarefa)

## Regras
1. Você NÃO corrige nada: nem dados, nem código, nem pacotes, nem o painel. Só lê e registra.
2. Pode escrever SOMENTE em:
   - projeto/revisao/<seu-prefixo>/ : seus scripts de conferência;
   - projeto/data/cache/revisao/<seu-prefixo>/ : páginas baixadas (fora do git);
   - projeto/docs/revisao/<slug>.md : seu relatório (o agente de clubes escreve projeto/docs/revisao/clubes-e-escudos.md);
   - SCRATCH/achados_<seu-prefixo>.csv : seus achados (o agente principal junta tudo no achados.csv oficial);
   - SCRATCH/<seu-prefixo>/ : logs, prints de tela, saídas temporárias.
   NÃO escreva em docs/revisao/achados.csv nem nos arquivos de pedidos (docs/coleta/pedidos*.md, docs/revisao/pedidos-painel.md): o agente principal faz isso.
   NÃO use git (nem add, nem commit, nem checkout).
3. Banco só leitura: sqlite3.connect("file:db/futebol.db?mode=ro", uri=True). Dados do painel: painel/dados/<slug>.js (JSON depois de "window.DADOS_COMP = "). Pacotes: data/coleta/<slug>/pacote/.
4. Fontes: use fontes DIFERENTES das que a coleta usou como base (o relatório de coleta diz quais). Funcionam por curl/Python: Wikipédia pt/en/es (prefira a API: https://pt.wikipedia.org/w/api.php?action=parse&page=...&prop=wikitext&format=json, ou o HTML da página) e RSSSF (www.rsssf.org). zerozero.pt responde 403. Teste ogol.com.br, cbf.com.br e outras antes de contar com elas.
5. Downloads educados: no máximo 1 pedido a cada 2 s, guarde cada página em data/cache/revisao/<seu-prefixo>/, nunca baixe de novo o que já tem, trate 429 (esperar 30-60 s e tentar de novo). Use User-Agent identificável (ex.: "clube-analitico-revisao/1.0 (uso pessoal)"). Há outros revisores baixando ao mesmo tempo.
6. Guarde a prova de cada achado: endereço exato (URL da página, e seção/tabela quando der).
7. Python: use `python` (3.12). Use -I ao rodar scripts que leem páginas baixadas (ex.: python -I revisao/x/script.py).
8. Painel no navegador sem janela (Chrome): "C:/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --disable-gpu --user-data-dir=SCRATCH/<seu-prefixo>/chrome-perfil --window-size=1400,900 --virtual-time-budget=8000 --screenshot=SCRATCH/<seu-prefixo>/tela.png "file:///C:/Users/guilhermecorrea/Downloads/Gui/GitHub/clube_analitico/painel/index.html?c=<slug>#<aba>/<subaba>/<item>"
   - Celular: --window-size=420,900. Use SEMPRE o seu próprio --user-data-dir (há outros revisores usando o Chrome ao mesmo tempo).
   - Erros de JavaScript: --enable-logging=stderr --v=0 (ou --dump-dom e procurar mensagens), e leia painel/index.html para entender as rotas (#aba/subaba/item) e as sub-abas.
   - Olhe os prints com a ferramenta Read (ela mostra imagens). Não precisa olhar todas as edições: amostre.
   - Já se sabe que "no celular a página fica mais larga que a tela" (pendência do agente 1). Se confirmar, registre uma vez como baixa citando que já é conhecida.
9. Quando um item for grande demais, confira uma amostra e diga no relatório qual foi.
10. Decisões que são do Guilherme (qual título reconhecer, se dois clubes são o mesmo): NÃO decida. Registre o achado (situacao "aberto") e liste a pergunta no seu relatório (seção "Perguntas ao Guilherme") e na sua resposta final.

## Formato de SCRATCH/achados_<seu-prefixo>.csv
Cabeçalho exato (UTF-8, separador vírgula, aspas quando precisar):
id,competicao,item,edicao,clube,o_que_esta_no_painel,o_que_a_fonte_diz,fonte,gravidade,quem_corrige,situacao
- id: <PREFIXO>-001, <PREFIXO>-002...
- competicao: o slug (bra-serie-a, bra-serie-b, bra-serie-c, bra-serie-d, bra-copa-do-brasil)
- item: A, B, C, D, E ou F (bloco do guia) seguido de um nome curto, ex.: "B classificação", "F aba História/Pódio"
- gravidade: alta (título, campeão, rebaixamento ou classificação errados) | media (placar, número ou clube errado) | baixa (texto, escudo, detalhe)
- quem_corrige: coleta-brasil (dado do pacote da Série C, D ou Copa do Brasil) | banco-painel (Séries A e B, banco, carregador, painel, escudos)
- situacao: aberto (ou nao-e-erro, quando você investigou algo suspeito e viu que está certo, se valer registrar)
- Um achado por linha. Se o mesmo erro se repete em muitos jogos/edições, agrupe numa linha e liste os casos (ou ponha a lista num arquivo em revisao/<seu-prefixo>/ e cite).

## Relatório docs/revisao/<slug>.md (em português, curto e objetivo)
- No topo: resumo de 3 linhas.
- Uma seção por bloco (A a F, só os seus): o que foi conferido, tamanho da amostra, resultado (ok / ids dos achados), fontes (URLs).
- Seção "Perguntas ao Guilherme" (se houver).
- Data: 20/11/2026.

## Resposta final (para o agente principal; curta, em português)
- quantos itens conferidos, quantos certos, achados por gravidade (alta/media/baixa);
- os 3 achados mais importantes (id + uma linha cada);
- perguntas de decisão para o Guilherme;
- caminhos do relatório e do CSV.

## Atualizações da 2ª rodada (21/11/2026) — valem por cima do que está acima
- O painel está publicado em https://clubeanalitico.pages.dev/?c=<slug>#<aba>/<subaba>/<item> (os dados publicados em https://clubeanalitico.pages.dev/dados/<slug>.js). Confira as telas NO SITE (Chrome sem janela abre https normalmente) e os números no banco local (db/futebol.db, só leitura; ele não está mais no git, é refeito por script) e em painel/dados/<slug>.js. Se site e arquivo local diferirem, registre.
- Rode sempre a varredura de tela, que procura o que salta aos olhos (vice que não jogou a final, "Final" com jogos demais, fases fora de ordem ou em inglês, clube contra ele mesmo, jogo repetido, clube com 2 jogos no mesmo dia, campeão fora do 1º lugar, posição repetida):
  copie revisao/tela/varredura.py e revisao/tela/datas_repetidas.py para revisao/<seu-prefixo>/ e troque a lista de competições para a sua (não edite os originais). Rode com python -I na raiz do projeto.
- Ligas estrangeiras e estaduais: a "Série A/B" não se aplica; confira o que o painel diz sobre acesso/rebaixamento, nomes de época, temporadas "2019/20", edições sem jogos, campeonatos amadores x profissionais, títulos divididos e anulados, desempates (playoffs de título), pontos por vitória de cada época (2 ou 3) e punições.
- O bloco E (clubes e escudos) agora é SEU também, só para os clubes da sua competição: duplicados, homônimos juntados, país/cidade errados, nomes de época, e escudos (monte a folha de contato e olhe todos, ou pelo menos os ~150 clubes com mais temporadas, dizendo a amostra).
- Nos resumos, cite os anos/edições de cada achado (não só contagens).
- quem_corrige: coleta-europa (eng-1, esp-1), coleta-sulamerica (arg-1, uru-1), coleta-brasil (bra-sp-1) para dado do pacote; banco-painel para carregador/banco/painel/escudos.

## 3ª rodada (22/11/2026): REVISÃO PROFUNDA — vale por cima de tudo acima
Decisão do Guilherme: as coletas agora só coletam campeonatos novos; as correções só começam quando ele mandar. A revisão deixa PRONTO o que cada agente vai corrigir. Por isso, além de achar o erro, você entrega a correção pronta.

1. Olhe os DADOS (pacote, banco, painel), não só a documentação. A ficha da coleta é o mapa para achar problemas:
   - Brasil: coleta/comum/COMECE-AQUI.md e coleta/comum/documentacao/<slug>.md
   - Europa: coleta/comum-europa/COMECE-AQUI.md e coleta/comum-europa/documentacao/<slug>.md
   - América do Sul: coleta/comum-sulamerica/COMECE-AQUI.md e coleta/comum-sulamerica/documentacao/<slug>.md
   - relatório da importação docs/coleta/<slug>.md e recados nos arquivos de pedidos (docs/coleta/pedidos*.md).
   A ficha tem 10 seções: 1 o que temos, 2 fontes e regras, 3 conferência, 4 cobertura por década, 5 formato, 6 campeões/rebaixados/punições, 7 correções e decisões, 8 o que não deu, 9 pendências, 10 arquivos e comandos. Use como roteiro:
   - Seção 1: os números batem com o pacote, o banco e o painel?
   - Seção 3: cada temporada com tabela divergente tem explicação convincente? Confira com uma fonte que a coleta NÃO usou. Divergência sem causa clara é achado.
   - Seção 4: buracos de cobertura (autores de gols, cartões, datas, público, árbitro, tabelas antigas). Para cada buraco: existe fonte que cubra? quanto custa (em lote ou jogo a jogo)?
   - Seção 5: número de clubes, pontos por vitória, fases e desempate fazem sentido para a época?
   - Seção 6: lista COMPLETA de campeões, vices e rebaixados contra a lista oficial (federação/liga) e a Wikipédia na língua do país. Atenção a play-offs, rebaixamentos fora de campo, punições, fusões.
   - Seção 7: por amostra (pelo menos 5 correções), a fonte citada diz mesmo o que a correção afirma?
   - Seções 8 e 9: proponha caminho, fonte, custo e risco para cada falta/pendência.
   - Clubes: nome único no mundo, identidade ao longo do tempo (fusões, refundações, SADs), escudo certo.
   - Dados: amostra de placares E datas POR DÉCADA (pelo menos 20 jogos por década onde houver jogos) contra uma fonte independente; artilheiros; datas impossíveis (varredura).
2. Algumas competições ainda NÃO estão no banco (só no pacote data/coleta/<slug>/pacote/): revise o pacote direto (e adapte a varredura para ler os CSVs do pacote). Quando estiver no banco e no site, compare pacote x banco x painel/site.
3. Identifique jogos por competição + data + clubes, NUNCA pelo partida_id (ids mudam quando a coleta reimporta).
4. Não reabra decisão já tomada pelo Guilherme (estão nos COMECE-AQUI de cada coleta e nos arquivos de pedidos) sem prova nova.
5. SUGESTÃO DE CORREÇÃO em todo achado: no CSV, a coluna o_que_a_fonte_diz leva "<prova> | SUGESTÃO: <valor certo>; fonte: <URL>; mexer em: <arquivo do código da coleta ou do banco/painel e o dicionário/função>". As fichas em documentacao/ são GERADAS: nunca sugira editar o .md; aponte o código (ex.: coleta/<slug>/importar.py, dicionário CORRECOES). Abra o código da coleta para achar o lugar certo.
6. FONTES NOVAS: procure fontes que a coleta não usou e que cubram buracos ou sirvam de terceira opinião. Teste cada uma por amostra antes de recomendar. Testado por curl em 22/11:
   - respondem: 11v11.com, footballdatabase.eu, transfermarkt (com/com.br), bdfutbol.com, ogol.com.br, rsssf.org, rsssfbrasil.com, cbf.com.br, futebolinterior.com.br, football-data.co.uk, soccerway.com, statto.com, ligaportugal.pt, ligue1.com, dfb.de, afa.com.ar, auf.org.uy, anfp.cl, dimayor.com.co, apf.org.py, liga1.pe, ligapro.ec, espn.com.br, national-football-teams.com, Wikipédias;
   - bloqueiam (403): worldfootball.net, weltfussball.de, fbref.com, kicker.de, fussballdaten.de, zerozero.pt; não abriram: enciclopediadelcalcio.it, footballfacts.ru.
   Seja educado (1 pedido a cada 2 s, cache, 429). Não tente contornar bloqueio.
7. ENTREGAS (além do relatório docs/revisao/<slug>.md e de SCRATCH/achados_<P>.csv):
   - SCRATCH/fontes_<P>.md: uma entrada por fonte avaliada, assim:
     ### <nome da fonte>
     - endereço: <URL modelo de página>
     - cobre: <campos e anos/competições>
     - como baixar: <em lote | jogo a jogo>; <formato>
     - amostra: <bateu x de y; com o quê>
     - serve a: <coleta-brasil | coleta-europa | coleta-sulamerica | banco-painel>; buscar: <o que buscar lá>
   - SCRATCH/decisoes_<P>.md: uma entrada por decisão do Guilherme: ### <id> <pergunta>; opções; prova (URLs); recomendação (e por quê).
   - SCRATCH/plano_<P>.md: os ids da sua competição em ordem de prioridade (gravidade x tamanho do erro x custo), agrupados por quem corrige e, dentro, por arquivo do código a mexer, com as fontes novas a usar.
8. Na resposta final, além do formato do briefing, liste os achados de gravidade ALTA que já estão NO AR (visíveis no site), para a seção "ERRADO NO AR".
9. Aviso de 22/11: footballdatabase.eu limita 50 páginas por dia por IP e o limite já acabou hoje (os revisores dividem o IP). 11v11 não tem a liga francesa; ligue1.com só tem a temporada atual. A ficha de jogo do transfermarkt tem árbitro, público, autores e cartões até em jogos antigos (uma página por jogo).
