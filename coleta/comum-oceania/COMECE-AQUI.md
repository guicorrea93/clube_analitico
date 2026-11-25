# Coleta Oceania — comece aqui

Para o agente de coleta Oceania (países da OFC) que for continuar este trabalho. Leia antes o guia geral
`docs/agentes-internacionais-COMECE-AQUI.md` (formato do pacote, pastas de cada agente, identidade dos clubes e as regras
da casa na seção 10). Este arquivo diz o que já foi feito, como foi feito e de onde continuar.

Última atualização: 25/11/2026.

## 1. Escopo e regras

- **Competições:** as 1ªs divisões dos países da OFC, na ordem `nzl-1`, `tah-1`, `ncl-1`, `fij-1`, `png-1`, `sol-1`,
  `van-1`, `sam-1`, `tga-1`, `asa-1`, `cok-1`. A **Austrália não é nossa** (AFC, agente da Ásia).
- **Pastas nossas** (não grave em mais nada; o banco é só para leitura):
  - `coleta/<slug>/` e `coleta/comum-oceania/`;
  - `data/coleta/<slug>/`, `data/cache/*-oceania*/` e `data/cache/ogol-<slug>/`;
  - `docs/coleta/<slug>.md` e `docs/coleta/pedidos-oceania.md`.
- **Antes de cada liga:** mandar ao Guilherme, em poucas linhas, as decisões de escopo.
- **Ao fim de cada liga:** resumo curto, recado de fim de coleta (8 itens da seção 10 do guia geral) no fim de
  `docs/coleta/pedidos-oceania.md` e o mesmo texto ao Guilherme; listar os países novos (para o agente 1 baixar as
  bandeiras). Commit só com o "sim" dele; push só quando ele pedir; nunca `git add -A`/`git add .`; conferir antes que
  `git diff --cached` está vazio.
- **Wellington Phoenix e Auckland FC** jogam a A-League com o agente da Ásia, com país `NZL`: se aparecerem nas nossas
  ligas, use exatamente o mesmo nome que ele usar.
- **Clubes com sigla** ("AS Pirae", "AS Tefana"): nome curto de uso corrente, conferido contra homônimos no banco e nos
  `data/coleta/*/pacote/clubes.csv`.
- **Fonte fraca é o normal aqui:** edição só com o campeão, ou só com a tabela, é aceita; edição com parte dos jogos leva
  `formato` começando por "jogos incompletos".

## 2. O que está pronto

| Competição | Edições | Jogos | Clubes | Commit do pacote | No banco |
|---|---|---|---|---|---|
| `nzl-1` Neozelandês | 55 (1970–2025) | 7.480 | 101 | d7a6379 | não |
| `tah-1` Taitiano | 79 (1948–2025/26; 31 com jogos) | 2.647 | 35 | 82549d6 | não |
| `ncl-1` Neocaledônio | 76 (1950–2026, sem 1955 e 2024; 36 com jogos) | 2.472 | 63 | 8f154e1 | não |
| `fij-1` Fijiano | 50 (1977–2026; 28 com jogos) | 2.177 | 17 | 8fa059a | não |
| `png-1` Papua-Nova-Guineense | 19 (2006–2026, sem 2021) | 1.336 | 78 | 60aaa017 | não |
| `sol-1` Salomonense | 25 (2000–2025, sem 2012/13; 21 com jogos) | 1.464 | 62 | "Campeonato Salomonense (sol-1)", no GitHub | não |

Números de gols, conferência e cobertura: `coleta/comum-oceania/documentacao/` (gerada por `documentar.py`). Detalhe edição a
edição: `docs/coleta/nzl-1.md`.

## 3. De onde continuar

1. **Nova Zelândia (`nzl-1`): pacote pronto e commitado em 23/11 (`d7a6379`, sem push)**; falta o agente 1 carregar. Recado
   de fim de coleta no fim de `docs/coleta/pedidos-oceania.md`.
2. **Taiti (`tah-1`): commitado em 24/11 (`82549d6`, sem push)**; falta o agente 1 carregar.
3. **Nova Caledônia (`ncl-1`): commitada em 24/11 (`8f154e1`, sem push)**, junto com as colunas de pontos do Taiti; falta o
   agente 1 carregar. Recado no fim de `docs/coleta/pedidos-oceania.md`. Fiji depois.
4. **Fiji (`fij-1`): commitado em 24/11 (`8fa059a`, sem push)**; falta o agente 1 carregar. Recado no fim de
   `docs/coleta/pedidos-oceania.md`.
5. **Papua-Nova Guiné (`png-1`): commitada em 25/11 (`60aaa017`, no GitHub)**; falta o agente 1 carregar; teste de carga OK.
   Recado no fim de `docs/coleta/pedidos-oceania.md`.
6. **Ilhas Salomão (`sol-1`): commitada e no GitHub em 25/11**; falta o agente 1 carregar; teste de carga OK.
   Recado no fim de `docs/coleta/pedidos-oceania.md`. **Próxima: Vanuatu (`van-1`)**, quando ele mandar; antes, pesquisa a
   fundo e as decisões de escopo.
7. Depois, na ordem: `van-1`, `sam-1`, `tga-1`, `asa-1`,
   `cok-1`. Tuvalu e Kiribati ficam de fora por enquanto (aprovado em 23/11; entram no fim se ele quiser).

### Decisões do Guilherme (23/11)

- NZ: começa em 1970; campeão da lista oficial (desde 1993 o da final, com o 1º da fase de liga na observação); 2004 e 2021
  fora; ligas regionais como 1ª fase; "Wellington Phoenix Reserves" para o time reserva.
- Nova Caledônia a partir de 1950; Tuvalu e Kiribati fora por enquanto.
- Taiti (24/11): desde 1948 (a lista oficial); "2025/26" nas temporadas que cruzam o ano (a RSSSF dá o ano final: "1999" =
  1998/99); até 2025/26 (a última terminada); nomes com "AS" ("AS Pirae", "AS Vénus", "AS Tefana", "AS Dragon", "Central
  Sport"); em 1956, 1957 e 1961 vale a RSSSF (a Wikipédia diverge, mas copia uma versão antiga da própria RSSSF: pendência);
  entram as fases do título e do rebaixamento (com o campeão de Mooréa no playoff, quando havia) e a seleção sub-20 ("Tahiti
  U-20", 2008/09); ficam de fora copas, 2ª e 3ª divisões, ligas das outras ilhas, barragens com a 2ª divisão e o Tahiti United
  (liga profissional da OFC).
- Nova Caledônia (24/11, depois de pesquisa a fundo): 2024 fora (abandonada, a federação não declarou campeão); 1963 e 1964 =
  Club Sportif Militaire (RSSSF atual, corrigida no fim de 2025 por recorte de jornal da época; Wikipédia e ogol copiam a
  versão antiga: USC e JS Vallée du Tir); AS Le Nickel = AS Magenta (mesmo clube com outro nome, Wikipédia fr/en e lista de
  fundações da RSSSF); Gaïtcha FCN = Gaïtcha FC, mas ASC Gaïca (Lifou) separado; "Île des Pins" (1961) = AS Kunié; JS Baco =
  "AS Baco"; Entente Gélima separada do US Gélima; nomes oficiais/de uso ("AS Tiga Sport", não "Tiga Sports"). Formato: até
  2001 só a fase nacional (as ligas das províncias eram competições regionais à parte); 2002-2011 liga da Grande Terre como
  1ª fase + playoff com o campeão das ilhas; 2012 em diante Super Ligue única.
- Fiji (24/11, depois de pesquisa a fundo): a 1ª divisão é a liga dos distritos, de 1977 a 2026 (RSSSF e Wikipédia batem em
  todos os anos); fora Inter-District Championship, National Club Championship, Club Franchise League (2004/05-2006), copas,
  2ª divisão e repescagens; 2003 = Ba (decisão da federação em 2006; Olympians em 2º); 2010 = Ba (o título dado ao Lautoka foi
  revogado); nomes = o distrito puro ("Nadi", "Lautoka"...), salvo "Ba FC"; seleções: "Fiji Olympians" (um clube só, 1998-2006),
  "Fiji U-20" (2010), "Fiji Youth Teams" (2011, a campanha somada que a RSSSF dá); os 8 jogos do sub-20 em 2000 foram anulados.
- Papua-Nova Guiné (24/11, depois de pesquisa a fundo): só a National Soccer League / Premier Soccer League, desde 2006 (o
  campeonato amador de clubes de 1976-2005 fica de fora; pode virar competição à parte); 2021 fora (abandonada); a "National
  Premier League" rebelde de 2017-2018 fora; Lae City Dwellers (2014) = Toti City = "Lae City" (os 7 títulos), e o "Lae City
  Dwellers" de 2021 é outro clube; o Hekari aparece como "Hekari United" (PRK Souths, Hekari Souths, PNG Hekari no histórico);
  Gulf Komara = Erema; Morobe United = Gigira Laitepo = Welgris Morobe United; Madang FC = Madang Flying Fox; Rapatona = CMSS
  Rapatona Tigers; Morobe Wawens, Lae FC e Besta PNG United separados; "Central United Port Moresby" (homônimo da NZ).
  Na coleta (pesquisa na Wikipédia, mesma linha das decisões): Morobe United vem do Tuguba Laitepo Blue Kumuls (2006) e do
  Morobe Kumuls (2007/08); o "Gigira Laitepo United" de 2015/16 (zona sul) é outra franquia; Southern Strikers = Port Moresby
  Strikers; o "Besta PNG FA Under-20" (2009/10, 2010/11) é o Besta PNG United; "Madang Besta" (2007/08) = Besta Madang
  Fighters; "Oro FC" (o "Oro" do banco é do México).
- Ilhas Salomão (25/11, depois de pesquisa a fundo): 1ª divisão = o campeonato nacional de clubes (2000 a 2009/10: torneio
  curto com os melhores de Honiara e os campeões das províncias) e a S-League (2010/11 a 2025), como a lista de campeões da
  RSSSF; fora a liga de Honiara (1947-1999, regional, só campeões), a "S-League" de franquias de Honiara (2004 e 2005), a
  Solomon Cup e o Interprovincial (seleções de província), o Knockout Championship e os playoffs da OFC; 2000-2002 e 2004
  só com o campeão (2004 com a final por W.O.), 2011/12 só a tabela, 2012/13 não houve; 2026 fora até o título sair
  (depende de punições pendentes); 2015/16 = Western United (playoff final, RSSSF; o Solomon Warriors, campeão pela
  Wikipédia, foi o 1º da fase regular); 2024 = Central Coast (RSSSF e Wikipédia; o ogol dá o Real Kakamora); mesmos clubes:
  Solomon Warriors = Uncles = Wantoks, Marist = Marist Fire = Systek Kingz, KOSSA = Fair West, Makuru = JP Su'uria, Real
  Kakamora = Kakamora FC (a seleção de Makira é outra), Laugu United = Blue Boys, Central Coast = CY Strikers, Ghupo = Ghupo
  Wantoks; homônimos de outros países levam a cidade ("Western United Honiara", "Central Coast Honiara", "Southern United
  Honiara"; Kula FC idem se a cidade se confirmar), só quando o nome já existe no banco; pontuação 3-1-0.

### Como a NZ foi feita (modelo para as próximas)

| Arquivo (`coleta/nzl-1/`) | O que faz |
|---|---|
| `baixar_rsssf.py`, `baixar_wikipedia.py`, `baixar_ogol.py` | fontes para `data/coleta/nzl-1/<fonte>/` (ogol também em `data/cache/ogol-nzl-1/`) |
| `edicoes.py` | uma `Edicao` por título; `trechos` = (página, linha inicial, final, fase, grupo) |
| `ler.py` | matriz de resultados (`matrizes`, `casar_matriz`), rodadas (leitor comum), ogol e Wikipédia; `campeoes()` |
| `clubes_nzl.py` | `CLUBES` (nome -> cidade, região) e `REGRAS` (regex, nome, anos); decisões de identidade na docstring |
| `explicacoes.py` | `CONSERTA_TEXTO`, `MATRIZ_NOME`, `CORRIGE`, `WIKI_FORA`, `TABELAS_FORA`, `EXPLICACOES` |
| `conferir.py` | soma dos jogos x tabelas: `python coleta/nzl-1/conferir.py [-v] [temporada]` |
| `autores.py` | separa os autores dos gols (minuto, contagem "Nome 2", og, pen) |
| `wikipedia_nz.py` | "Sports table" e "Sports results" da Wikipédia |
| `importar.py` | pacote e relatório |

## 4. Código comum (`coleta/comum-oceania/`)

Copiado de `coleta/comum-sulamerica/` em 23/11/2026 (não importe código da pasta de outro agente).

| Arquivo | O que faz |
|---|---|
| `rsssf_oce.py` | leitor genérico das páginas da RSSSF (`texto`, `ler`, `linha_tabela`, `_jogo`, `chave`). Mudou? Reimporte as competições já feitas e compare os pacotes |
| `baixar.py` | `pegar(url, destino, espera)`: download educado, com cache e 429 |
| `espn.py` | URL do placar diário e `resumir(evento)` |
| `ogol.py`, `wikipedia.py` | calendário do ogol; wikitexto pela API |
| `documentar.py` | gera `documentacao/` (pôr a competição em `LIGAS`, `PAIS` e `PENDENCIAS`) |
| `testar_carga.py` | teste de carga numa cópia do banco: `python coleta/comum-oceania/testar_carga.py <slug> <scratchpad>` |

Para uma competição nova, o modelo mais próximo é `coleta/ven-1/` (fonte fraca, era amadora, tabela cruzada); a lista de
módulos de cada competição está em `coleta/comum-sulamerica/COMECE-AQUI.md`, seção 4.

## 5. Fontes (o que já se sabe)

- **RSSSF**, listas de campeões guardadas em `data/cache/rsssf-oceania/`: `nzchamp`, `nzhist`, `tahitichamp` (desde 1948),
  `newcalchamp` (1933; 1934-49 desconhecidos; tabelas só em alguns anos), `fijichamp` (1977), `pngchamp` (2006),
  `solomchamp`, `vanuatuchamp` (Port Vila desde 1975; nacional desde 2010), `samoachamp` (1979), `tongachamp` (1969/70),
  `amsamoachamp` (1976, muitos anos desconhecidos), `cookchamp`, `tuvaluchamp` (1980), `kirichamp` (torneio de ilhas, 1984).
- **Nova Zelândia na RSSSF:** 1970-1992 tabela + matriz de resultados (sem data nem autor); 1993-1995 ligas regionais +
  fase nacional; 1996-1998 Summer Soccer League com Grand Final; 1999 NISL e SISL + final; 2000-2003 liga + mata-mata
  dos 4 primeiros (rodadas com data e autores dos gols); 2004 sem campeão (só ligas regionais); 2004/05-2020/21
  NZFC/Premiership (fase de liga + mata-mata); 2021 só a "South Central Series"; 2022-2025 ligas regionais + fase nacional
  + final. As páginas trazem também a Chatham Cup (copa): o trecho da liga acaba antes dela.

## 6. Armadilhas

- **Heredoc no Windows** (`python - <<'EOF'`) estraga `\b` e `\1` (viram caracteres de controle): edite com o Edit ou por
  arquivo, e confira com `grep -c $'\x01\|\x08' arquivo.py`.
- **Matriz de resultados da RSSSF** (NZ 1970-1995): nome da linha abreviado ("Well Utd"), casado com a tabela por semelhança;
  diferenças de um gol com a tabela são comuns (a tabela costuma estar certa: confira com a da Wikipédia).
- **Placar "5(2)"** (1996, 1996/97): o do intervalo entre parênteses, autores em duas colunas abaixo (`ler._ht`).
- **Tabela com coluna de bônus** (P W D L F A B Pts): o leitor comum toma o bônus pelos pontos; ver `ler.ler` (nz96/nz97).
- **Nome com número** ("FC Twenty 11"): quebra a linha da tabela; troque na página ("Twenty-11").
- **Wikipédia**: módulo `{{#invoke:sports table|...}}` em minúscula; `[[A|B]]` e `{{nowrap|...}}` dentro dos campos; matrizes
  de resultados às vezes erradas ou incompletas (2023-2025): confira com a tabela da RSSSF antes de usar.
- **ogol**: o calendário de uma edição pode juntar ligas regionais e fase nacional (NZ 2025): separe pelos clubes de cada
  grupo e pela data do primeiro jogo entre regiões.
- **Fiji (24/11):**
  - os times da liga são as associações dos distritos ("Ba", "Nadi"...); a página traz junto copas, campeonato de clubes e
    ligas locais: `edicoes._trecho` acha o começo (o 1º título seguido de tabela ou rodada; o índice do topo repete os
    títulos) e o fim (próxima competição);
  - linha de tabela com erro de digitação (V+E+D diferente de J) é descartada pelo leitor comum e corta a tabela:
    `ler._tabelas_inteiras` relê a tabela inteira;
  - duas tabelas da mesma fase (2002: a montada com os resultados conhecidos e a final divulgada): vale a última;
  - "Tavua/Lautoka" = adversário incerto (o jogo sai); "possibly awarded" e "awarded... revogado": vale o placar de campo;
  - o ogol tem a liga completa de 2011 (fecha com a tabela) e a de 2012 (não fecha: fica de fora).
- **Papua-Nova Guiné (24/11):**
  - uma página da RSSSF por temporada (a lista de campeões não liga quase nenhuma): `baixar_rsssf.py` baixa pela lista fixa;
  - datas com estádio e cidade ("[May 6, Laiwaden Oval, Madang]") e cabeçalhos do mata-mata com data ("Semifinals [Mar 14]")
    não eram reconhecidos (a linha virava "autores" do jogo de cima): `ler.linhas` deixa só a data;
  - nota que continua na linha de baixo, ao lado da data ("[Nov 23]      to fading light]"), escondia a data do jogo seguinte:
    `ler.linhas` devolve o pedaço para a linha de cima;
  - autores com placar corrido ("Jacob Max 2-1, 3-2", "Jonathan Allen (0-1)"), contagem entre parênteses ("Kema Jack (2)",
    "(2, 1 pen)") e lados separados por ";": `autores._png`;
  - jogo abandonado sem placar na coluna ("abd") e "awarded 0-3 against both clubs" entram por `explicacoes.CORRIGE` (o
    leitor deixa passar o que está lá); "drw", "lt" e "bt" (sem placar) ficam de fora; 3º lugar sem placar: `TERCEIROS`;
  - 2019/20 vai de dezembro de 2019 a outubro de 2020: `ler.CORTE` (mês a partir do qual a data é do 1º ano);
  - no ogol o rótulo da edição às vezes é o ano vizinho (mapa conferido em `baixar_ogol.py`); em 2015/16 o ogol chama o PS
    Huawei de "Huawey Eastern Stars" e o Gigira Laitepo United de "Gigira Laitepo Morobe" (ficam sem clube, de propósito).
- **Ilhas Salomão (25/11):**
  - as páginas da RSSSF ficam em `tabless/` (não `tablesp/`) e têm o nome do ano em que a temporada termina (`solom2016` =
    2015/16, `solom2017` = 2016; não existe `solom2014`); `solom06` traz o campeonato de fev/2006, que a lista chama de 2005/06;
  - "Pool A"/"Pool B" viram "Group A" em `ler.linhas` (o leitor comum só reconhece "Group"); sem isso os jogos ficam sem grupo;
  - "awarded 0-3; originally 2-1": `ler.ler` põe o placar de campo da nota (o oficial fica em `gm_of`);
  - desclassificado na tabela com "-." no lugar da posição e uma linha solta de "playing record" embaixo (2013/14):
    `CONSERTA_TEXTO` numera e transforma a linha solta em nota;
  - notas que continuam ao lado de outros jogos (2009/10, 2010/11, 2025) e escondem data ou "Round N": `CONSERTA_TEXTO`;
  - nada de ogol para 2016, 2018 e 2020/21; os rótulos das edições do ogol estão trocados (mapa em `baixar_ogol.py`).
- `_junta` (importadores do Taiti, da Nova Caledônia e de Fiji) agora copia a tabela antes de juntar os pedaços (antes
  alterava a original).
- **Nova Caledônia (24/11):**
  - a lista de campeões da RSSSF muda de colunas no meio (final "X 2-1 Y" até 2005; "Champions / Runners-Up / Third" depois):
    `ler.campeoes()` lê os dois;
  - "2002" e "2002/03" são duas edições diferentes; o calendário volta ao ano civil em 2009;
  - páginas antigas põem a ida e a volta na mesma linha ("AS Poum  0-1 3-1  Wé-Luecilla"); "Groupe A" (francês); "[Lifou]" no
    meio da linha da tabela: `ler.linhas` acerta os três;
  - em 2025 as rodadas misturam os dois grupos: o grupo sai da tabela de cada clube;
  - vitória dada no tribunal em que a tabela conta os gols de campo (2007/08): `gols_contam` em `conferir.soma`.
- **Taiti (24/11):**
  - a RSSSF dá o ano em que a temporada termina ("1999" = 1998/99); as páginas de 2010 em diante têm um índice no topo
    com os mesmos títulos das seções (o trecho começa no segundo "Division 1");
  - "Faa'a" (apóstrofo no fim do nome do mandante) é lido como minuto: `ler.linhas` troca por "Faaa";
  - jogo anulado e jogado de novo aparece duas vezes ("annulled", "replay"): o anulado não conta (`n/p` no pacote);
  - "awarded 0-0 loss to both" = derrota para os dois (`derrota_ambos` em `conferir.soma`);
  - tabelas do playoff que somam a fase regular (2001/02, 2002/03: `acumula`); tabela só com pontos (2004/05: `importar.MANUAL`);
  - pontuação muda de ano para ano (4-2-1, 3-2-1, 3-1-0): confira pela conta da tabela; bônus e punições vão no ajuste;
  - seleções de base do Taiti jogaram a liga (U-17, U-19, U-20).
- Homônimos já no banco: "Central" (BRA), "Miramar" (URU), "Rangers" (SCO), "Hamilton Academical" (SCO): os da NZ levam
  o nome completo ou a cidade ("Central United", "Miramar Rangers"); "Oro" (MEX): o de PNG é "Oro FC"; "Central United"
  (NZL): o de PNG é "Central United Port Moresby"; "Southern United" (NZL), "Northern United" (GHA) e "Kula" (PNG): os das
  Ilhas Salomão são "Southern United Honiara", "Northern United Malaita" e "Kula FC (Ilhas Salomão)".
