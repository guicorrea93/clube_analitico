# Coleta Oceania — comece aqui

Para o agente de coleta Oceania (países da OFC) que for continuar este trabalho. Leia antes o guia geral
`docs/agentes-internacionais-COMECE-AQUI.md` (formato do pacote, pastas de cada agente, identidade dos clubes e as regras
da casa na seção 10). Este arquivo diz o que já foi feito, como foi feito e de onde continuar.

Última atualização: 23/11/2026.

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
| `ncl-1` Neocaledônio | 76 (1950–2026, sem 1955 e 2024; 36 com jogos) | 2.472 | 63 | ainda não (esperando o ok) | não |

Números de gols, conferência e cobertura: `coleta/comum-oceania/documentacao/` (gerada por `documentar.py`). Detalhe edição a
edição: `docs/coleta/nzl-1.md`.

## 3. De onde continuar

1. **Nova Zelândia (`nzl-1`): pacote pronto e commitado em 23/11 (`d7a6379`, sem push)**; falta o agente 1 carregar. Recado
   de fim de coleta no fim de `docs/coleta/pedidos-oceania.md`.
2. **Taiti (`tah-1`): commitado em 24/11 (`82549d6`, sem push)**; falta o agente 1 carregar.
3. **Nova Caledônia (`ncl-1`): pacote pronto em 24/11**, teste de carga OK; esperando o ok do Guilherme para o commit. Recado no
   fim de `docs/coleta/pedidos-oceania.md`. **Próxima: Fiji (`fij-1`)**, quando o Guilherme mandar; antes, pesquisa a fundo
   (como no Taiti e na Nova Caledônia) e as decisões de escopo.
4. Depois, na ordem: `png-1`, `sol-1`, `van-1`, `sam-1`, `tga-1`, `asa-1`,
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
  o nome completo ou a cidade ("Central United", "Miramar Rangers").
