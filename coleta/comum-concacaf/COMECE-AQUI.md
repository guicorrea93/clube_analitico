# Coleta CONCACAF — comece aqui

Para o agente de coleta da América do Norte e Central (CONCACAF) que for continuar este trabalho. Leia antes:
1. `docs/COMECE-AQUI.md` (mapa do projeto);
2. `docs/agente-coleta-COMECE-AQUI.md` (método e formato do pacote);
3. `docs/agentes-internacionais-COMECE-AQUI.md` (o que muda fora do Brasil; regras da casa na seção 10);
4. `coleta/comum-sulamerica/COMECE-AQUI.md` e `coleta/arg-1/` (modelo copiado: dois campeões por ano, Apertura e Clausura).

Este arquivo diz o que já foi feito, como foi feito e de onde continuar.

Última atualização: 23/11/2026.

**Documentação completa:** `coleta/comum-concacaf/documentacao/` (gerada por `python coleta/comum-concacaf/documentar.py`
a partir dos pacotes, do código e dos relatórios). Rode depois de toda importação ou correção e mantenha à mão só as listas
`LIGAS`, `PAIS` e `PENDENCIAS`, no começo do script.

## 1. Regras da casa (combinadas com o Guilherme)

- **Uma competição por vez.** Antes de cada liga, mande ao Guilherme, em poucas linhas, as decisões de escopo. Ao fim:
  - resumo curto;
  - pedido de ok para o commit;
  - **recado de fim de coleta**: seção "Recado de fim de coleta — <slug> — <data>" no fim de
    `docs/coleta/pedidos-concacaf.md`, para o agente 1 (banco e painel) e para o agente de revisão, e o mesmo texto ao
    Guilherme, num bloco de código. Os 8 itens da seção 10 do guia internacional; no item 4, **liste os países novos**
    (o agente 1 baixa as bandeiras).
- **Mexa só nas suas pastas:**
  - `coleta/<slug>/` e `coleta/comum-concacaf/`;
  - `data/coleta/<slug>/`, `data/cache/*-concacaf*/` e `data/cache/ogol-<slug>/`;
  - `docs/coleta/<slug>.md` e `docs/coleta/pedidos-concacaf.md`.

  Nunca toque em `db/`, `futebol/`, `painel/` nem nas pastas comuns e de competição dos outros agentes. Não importe código
  da pasta de outro agente (ele pode mudar): copie para cá.
- **Banco só para leitura:** `sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)`. O teste de carga usa uma cópia.
- **Git:** nunca `git add -A` nem `git add .`; antes do `git add`, confira que `git diff --cached` está vazio (a pasta é
  compartilhada); commit só com o ok explícito do Guilherme; push só quando ele pedir; não troque de ramo; a mensagem
  termina com `Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>`.
- **Logs e conferências vão para o scratchpad**, nunca soltos no repositório.
- **Critério nas dúvidas:** o que for mais fiel à história e ao que a federação do país reconhece. Registre a decisão com o
  motivo em `explicacoes.py` e no relatório; o que for decisão dele, pergunte.
- **Fale com ele em português, curto e por partes.** Trabalhe sozinho; pergunte só as decisões que são dele.

## 2. O que está pronto

| Competição | Edições | Jogos | Clubes | Commit do pacote | No banco |
|---|---|---|---|---|---|
| `mex-1` Mexicano | 158 (1902/03–2026 Clausura) | 26.606 | 92 | cb0355f (no GitHub) | sim |
| `usa-1` Norte-Americano | 63 (ASL 1921/22–1932/33, 1967, NASL 1968–1984, MLS 1996–2025) | 8.708 | 134 (13 do Canadá) | 5bace06 (no GitHub) | sim |
| `crc-1` Costarriquenho | 123 (1921–2026 Clausura) | 7.065 | 65 | 17766bf (no GitHub) | sim |
| `hon-1` Hondurenho | 89 (1965/66–2026 Clausura) | 5.391 | 55 | 6e59e93 (no GitHub) | sim |
| `gua-1` Guatemalteco | 101 (1942/43–2026 Clausura) | 6.836 | 73 | 7fd2f61 (no GitHub) | sim |
| `slv-1` Salvadorenho | 111 (1926–2026 Clausura) | 6.026 | 71 | f343c14f (no GitHub) | sim |
| `pan-1` Panamenho | 66 (1988–2026 Clausura, com 2 da LINFUNA) | 4.520 | 33 | 83c08786 (no GitHub) | sim |

Gols, cartões, conferência e cobertura: `documentacao/README.md` e uma ficha por competição.

## 3. De onde continuar

**Vale o plano único: `docs/coleta/plano-de-coleta.md` (25/11/2026), acima de qualquer ordem antiga deste guia.** Fase 1 =
a 1ª divisão de todas as federações da CONCACAF, na ordem do ranking abaixo; só depois a fase 2 (copas nacionais), a fase 3
(2ªs divisões) e a fase 4 (o resto). Uma competição por vez, com o escopo antes (proposta ao Guilherme, ok, registro na
seção 6).

### 3.1. Ranking (foto fixa de 25/11/2026)

Ranking FIFA masculino (o de 18/11/2026, vigente em 25/11), só com as federações da CONCACAF, da melhor para a pior. Fonte:
[globalfootballrankings.com](https://globalfootballrankings.com/rankings/fifa-world-ranking/men) e
[FIFA, notícia de 18/11](https://inside.fifa.com/fifa-rankings/world-ranking/men/news/coca-cola-mens-world-rankings-november-2026-morocco-canada).
A ordem não muda depois, mesmo que o ranking mude.

| # | Federação (posição no mundo) | Slug | Estado |
|---|---|---|---|
| 1 | México (13) | `mex-1` | pronto, no banco |
| 2 | EUA (16) | `usa-1` | pronto, no banco (falta a MLS 2026, depois de 18/12) |
| 3 | Canadá (25) | `can-1` | **próxima** (escopo antes) |
| 4 | Panamá (45) | `pan-1` | pronto, no banco |
| 5 | Costa Rica (55) | `crc-1` | pronto, no banco |
| 6 | Jamaica (67) | `jam-1` | |
| 7 | Honduras (68) | `hon-1` | pronto, no banco |
| 8 | Curaçao (81) | `cuw-1` | |
| 9 | Haiti (86) | `hai-1` | |
| 10 | Guatemala (97) | `gua-1` | pronto, no banco |
| 11 | El Salvador (101) | `slv-1` | pronto, no banco |
| 12 | Trinidad e Tobago (104) | `tri-1` | |
| 13 | Suriname (128) | `sur-1` | |
| 14 | Nicarágua (132) | `nca-1` | |
| 15 | República Dominicana (136) | `dom-1` | |
| 16 | Guiana (140) | `guy-1` | |
| 17 | São Cristóvão e Névis (154) | `skn-1` | |
| 18 | Porto Rico (155) | `pur-1` | |
| 19 | Cuba (162) | `cub-1` | |
| 20 | Santa Lúcia (163) | `lca-1` | |
| 21 | Antígua e Barbuda (164) | `atg-1` | |
| 22 | São Vicente e Granadinas (165) | `vin-1` | |
| 23 | Granada (168) | `grn-1` | |
| 24 | Bermudas (171) | `ber-1` | |
| 25 | Barbados (174) | `brb-1` | |
| 26 | Montserrat (175) | `msr-1` | |
| 27 | Belize (181) | `blz-1` | |
| 28 | Aruba (183) | `aru-1` | |
| 29 | Dominica (184) | `dma-1` | |
| 30 | Ilhas Cayman (201) | `cay-1` | |
| 31 | Turks e Caicos (204) | `tca-1` | |
| 32 | Ilhas Virgens Americanas (206) | `vir-1` | |
| 33 | Bahamas (208) | `bah-1` | |
| 34 | Ilhas Virgens Britânicas (209) | `vgb-1` | |
| 35 | Anguila (210) | `aia-1` | |
| 36-41 | Fora do ranking (filiadas à CONCACAF, não à FIFA): Guiana Francesa, Guadalupe, Martinica, Sint Maarten, Saint-Martin, Bonaire | `guf-1`, `glp-1`, `mtq-1`, `sxm-1`, `smn-1`, `bon-1` | no fim, se houver fonte |

Os slugs das que faltam seguem o código FIFA (`<pais>-1`); conferir no banco antes de criar.

### 3.2. Onde parou

1. **Prontas e no banco (7):** `mex-1`, `usa-1`, `crc-1`, `hon-1`, `gua-1`, `slv-1`, `pan-1`; tudo no GitHub (último
   pacote: `pan-1`, 83c08786). Recados de fim de coleta no fim de `docs/coleta/pedidos-concacaf.md`.
2. **Correção do plano (seção 2.3), 25/11:** o leitor comum (`rsssf_concacaf.py`) passou a juntar os autores de gol em duas
   linhas (como o `rsssf_sul.py`, a0222fa9); as sete ligas foram reimportadas e os totais comparados (recado em
   `docs/coleta/pedidos-concacaf.md`).
3. **Próxima: Canadá (`can-1`)**, com o escopo antes. Depois, pelo ranking: Jamaica, Curaçao, Haiti, Trinidad e Tobago...
4. **MLS 2026:** entra na `usa-1` depois da final (18/12/2026).
5. Ficar de olho em `docs/coleta/pedidos-concacaf.md`: respostas do agente 1 e pedidos da revisão.

## 4. Código comum (`coleta/comum-concacaf/`)

| Arquivo | O que faz |
|---|---|
| `rsssf_concacaf.py` | leitor genérico das páginas da RSSSF (cópia de `rsssf_sul.py`): `texto`, `ler`, `linha_tabela`, `_jogo`, `chave`. **Mudou? Reimporte as ligas já feitas e compare os pacotes (`git diff --stat`)** |
| `baixar.py` | `pegar(url, destino, espera)`: download educado, com cache |
| `espn.py` | URL do placar diário e `resumir(evento)` (`mex.1`, `usa.1`...) |
| `ogol.py`, `wikipedia.py` | calendário do ogol; wikitexto pela API |
| `documentar.py` | gera `documentacao/` |
| `testar_carga.py` | `python coleta/comum-concacaf/testar_carga.py <slug> <scratchpad>`; deve terminar com `<slug>: N edições, N jogos, N clubes novos -> OK` |

Cache: ESPN em `data/cache/espn-concacaf/`, ogol em `data/cache/ogol-<slug>/calendario_<ano_inicio>_<id>_p<página>.html`
(o agente 1 tira os escudos de lá).

Para uma competição nova, copie `coleta/mex-1/` (o modelo da região) e siga os passos da seção 4 de
`coleta/comum-sulamerica/COMECE-AQUI.md`. O que o `mex-1` tem de diferente do `ven-1`, de onde foi copiado:
- `edicoes.py`: trechos achados pelos títulos de cada página (`_linha`, `_dois_torneios`, `_cortes`), não por número de linha;
  `_PULA` tira competições do meio de um torneio (Libertadores, Interliga);
- `conferir._hist()`: lê a página de tabelas finais de todas as temporadas (`mexhist.html`), que serve de conferência e de
  classificação nas edições sem jogos ou incompletas;
- `conferir.preparar()`: grupos da fase regular só de classificação (todos jogam contra todos) não vão para os jogos;
- `faltam.py`: mostra os confrontos que faltam ou sobram numa fase de pontos corridos (o jeito mais rápido de achar uma rodada
  que o leitor não leu).

Mudanças no leitor comum (`rsssf_concacaf.py`) em 23/11, antes de qualquer liga: páginas em UTF-16 e páginas com fim de linha
`\r` sozinho (antigas, do Mac), que antes viravam uma linha só.

## 5. Armadilhas da região (já sabidas antes da coleta)

- **Apertura e Clausura** (México desde 1996, quase toda a América Central): uma edição por torneio que deu título
  ("2023 Apertura", "2024 Clausura"). A Liguilla e as finais são fases. O Clausura 2020 (pandemia) entra sem campeão.
- **Pontos fora do padrão:** MLS com shootout (1996-1999) e NASL com ponto por gol. Nesses anos a classificação vem da
  tabela publicada; explicar no relatório.
- **Clubes de um país na liga de outro:** os canadenses da MLS entram na `usa-1` com país `CAN`.
- **Homônimos:** já existem "Olimpia" (Paraguai) e "Santos" (Brasil). Usar "Olimpia de Tegucigalpa", "América do México" e
  "Santos Laguna"; os outros "América" levam a cidade. Conferir sempre o banco e os `data/coleta/*/pacote/clubes.csv`.
- As armadilhas da RSSSF, da ESPN e do ogol já vistas na América do Sul estão na seção 6 de
  `coleta/comum-sulamerica/COMECE-AQUI.md`.

**Vistas no Panamá (25/11):**
- **A ESPN não tem a liga do Panamá** (não há `pan.1` na lista de ligas dela): só a RSSSF.
- **Edições com rótulo do ano do torneio** ("2010 Clausura" = Clausura 2009/10; "2009 Apertura ANAPROF" e "2009 Apertura" da
  LPF): `edicoes.lista()` e `edicoes._torneio()` (o título do torneio vale na página do ano, na seguinte ou na anterior;
  o primeiro título da página é o da 1ª divisão, os seguintes são da 2ª).
- **"Championship Final" com dois sentidos:** até 2000/01 é a final da temporada; de 2002 a 2006 é a decisão entre os
  campeões do Apertura e do Clausura (supercopa, fora): `FIM_TORNEIO` só nos Aperturas e Clausuras.
- **"Topscorers" no meio da página** (antes das semifinais): não serve de fim de trecho.
- **"Sporting '89":** o apóstrofo impede a leitura da linha como jogo; `linhas()` troca por "Sporting 89".
- **Liga paralela (LINFUNA 1994-96):** edição à parte na mesma temporada ("1994/95 LINFUNA"), ordenada logo depois da oficial.

**Vistas em El Salvador (24/11):**
- **Lista de campeões com seções** ("unofficial editions", "official championships", "Playoff between Zonal Champions",
  "National League"): `edicoes.lista()` lê só as oficiais e já dá o vice; a Copa Pilsener 1998/99 sai pela nota `[Pilsener]`.
- **Página de tabelas finais com as finais antigas** (`elsalhist.html`, 1926 a 1997/98): `edicoes.secoes_hist()` acha a seção
  de cada temporada pelo título (só o ano); de 1926 a 1938 as finais entram como jogos, 1942/43/46 só com a tabela.
- **Trecho a tirar no meio da página** (repechaje de 1996/97 contra clube da 2ª; rodadas anuladas de 2022): `edicoes._corta()`.
- **Jogo extra pela 4ª vaga** ("Fourth Place Match", "Qualifying Playoff", 2002-2013): fase "Desempate do 4º lugar", fora da
  conta da fase regular.
- **Linha de jogo com inicial minúscula** ("once Municipal 0-3 Alianza"): o leitor comum não lê; `CONSERTA_TEXTO`.
- **Vaga comprada** (Inter FA ficou com a do Dragón, Hércules com a do Once Deportivo, 2025): clube próprio.
- **ESPN (`slv.1`) que não fecha com a RSSSF** nos Aperturas de 2010 e 2011 (as edições só com tabela): não usada para completar;
  serve só para hora, estádio e lances (2006 em diante; sem lances de 2018 a 2025).

**Vistas na Guatemala (24/11):**
- **Nomes de arquivo irregulares** (`guat71a.html` = 1970/71): `edicoes.paginas_por_temporada()` casa pelo título da página.
- **Pontos por vitória sem data certa da mudança:** `edicoes._pv()` decide pela tabela publicada de cada temporada.
- **Lista de campeões sem vice:** o vice é o 2º da classificação.

**Vistas em Honduras (24/11):**
- **Nome com a cidade entre parênteses** ("Marathón (San Pedro Sula)", 2002 em diante): `clubes_hon._LIXO` tira.
- **"Grupo A" depois de uma fase chamada "Fase final"** volta à fase regular no leitor comum: dar à fase um nome próprio
  ("Triangulares").
- **Tabelas de 1965/66 a 1994/95 numa página só** (`hondhist.html`): uma seção por temporada, lida como `Edicao.tabelas`.

**Vistas na Costa Rica (24/11):**
- **Apertura e Clausura como fases do ano** (1997/98 a 2006/07): `ler_rsssf.TORNEIOS` e `FECHA` (do `ven-1`); a fase da final do
  ano ("Championship Playoff") fecha o torneio.
- **Edição só com tabela, decidida pela página:** `edicoes._tem_jogos` compara os jogos da página com a soma da 1ª tabela.
- **Pênaltis colados no nome** ("Belen (Saprissa 4-2 pen)", 1996/97): `linhas()` vira nota de pênaltis.
- **ESPN com jogo adiado repetido** (o original como 0-0) e o Brujas chamado de "Orión FC" em 2010/11: não usar a ESPN para a fase
  regular desses anos. A `crc.1` só traz gols (sem cartões).

**Vistas nos EUA (24/11):**
- **Ligas antigas só com tabelas** (ASL I, NASL): `edicoes.tabelas` e o leitor de tabelas próprio `ler_rsssf.tabelas_texto`, guiado
  pelo cabeçalho de cada tabela ("GP W WS LS L GF GA Pts", "G W L GF GA PTS % Att."), com nome colado no número ("Philadelphia
  Field Club24") e linha sem gols. Vale copiar para ligas com tabelas fora do padrão.
- **Shootout** (MLS 1996-1999, NASL 1975-1984): o jogo é empate com pênaltis; na tabela, WS e LS somam aos empates; a pontuação
  fora do padrão vai em `Edicao.pontos_fora` (sem "ajuste de pontos" na classificação).
- **Conferências e divisões:** a classificação junta as tabelas de clubes diferentes e ordena por pontos (`importar.classificacao`).
- **Páginas da MLS com outras competições** (US Open Cup, USL, MLS is Back 2020, jogos de exibição na ESPN): `FIM_PADRAO` e
  `clubes_usa._NAO_CLUBE`.
- **"Round 1" depois do título dos playoffs** é fase, não rodada (`linhas()` troca por "Playoff First Round").

**Vistas no México (23/11):**
- **Fim de linha `\r` sozinho** (1956/57, 1958/59, 1959/60, 1976/77, 1983/84): a página inteira virava poucas linhas e o leitor
  perdia jogos. Corrigido no leitor comum.
- **Placar depois de cada nome** ("Guadalajara 4 León 0": México 70 inteiro, a última rodada de 1995/96, 1933/34): convertido
  em `ler_rsssf.linhas()`.
- **"Final" do playoff de rebaixamento** contava como final do título: depois de "Relegation playoffs", os títulos "Final" e
  "Semifinals" viram "Relegation Final".
- **Jogo suspenso e completado depois** ("abd" e depois "[remaining 79']"): descartar a primeira linha em `CORRIGE`. Se a nota
  diz "result stood", não é jogo repetido: `linhas()` troca "suspended" por "stopped".
- **Tabela do meio do torneio** publicada antes dos jogos (2007 Clausura) e "Table at the end of Round 19" (1974/75): ficam fora
  da conferência (`conferir`: mesma tabela com mais jogos adiante, ou o título diz que é parcial).
- **Página com outra competição no meio** (Copa Eliminatoria no meio da liga de 1927/28; Torneo Presidente López Mateos em
  1962/63; Liguilla Pre-Libertadores e Interliga entre o Apertura e o Clausura): `FIM_PADRAO`, `_PULA` ou trechos explícitos.
- **Coluna de hora e de canal de TV** antes do mandante (1983/84: "20:45   Televisa 4 (D) Necaxa"): limpo em `clubes_mex._LIXO`.
- **ESPN junto com a página** (Apertura 2025 e Clausura 2026: a página só tem as tabelas e a liguilla): limitar a janela da ESPN
  à fase regular, senão a liguilla entra em dobro.

## 6. Decisões do Guilherme já tomadas

- **México (23/11):**
  - a era amadora (Primera Fuerza e Liga Mayor, 1902/03-1942/43) entra, com o que houver (tabela ou só campeão e vice);
  - 1920/21 e 1921/22: duas edições por ano, uma por liga (Liga Nacional e Liga Mexicana); o Torneo del Centenario
    (1921, do governo) fica fora;
  - México 70, Prode 85 e México 86 são edições próprias (a Liga MX conta como título);
  - decisões do agente, já combinadas na regra geral: Invierno/Verano (1996-2002) e Apertura/Clausura, uma edição cada
    ("1996 Invierno", "2023 Apertura"); Clausura 2020 sem campeão; nomes "América do México", "Santos Laguna" e
    "Real Club España" (já existe "España" do Equador);
  - **decididas em 24/11, depois de pesquisa (o Guilherme aprovou o commit com elas):** Pachuca AC (era amadora) = Pachuca
    de hoje (o clube conta a história desde 1892; paradas em 1922-1950 e 1952-1960, refundado em 1960 com o mesmo nome);
    Atlético Español (1971-1982) = Necaxa (vendido e renomeado; a Televisa devolveu nome e cores em 1982; todas as fontes
    tratam como o mesmo clube); 1930/31 sem campeão (a federação declarou o campeonato deserto).
- **EUA (24/11; o Guilherme pediu "pesquise a fundo e veja o que é mais pertinente"):** a 1ª divisão é a que a RSSSF conta
  como "Division I" (`usachamp.html`):
  - ASL I (1921/22 a 1932/33, 14 títulos, com as meias-temporadas 1929, 1930 e 1932): edições só com a tabela (a RSSSF não
    tem os jogos);
  - 1967: duas edições, United Soccer Association (a liga da FIFA) e NPSL (a liga "pirata"), como a RSSSF e a Wikipédia;
  - NASL 1968-1984: tabelas e playoffs (a RSSSF não tem os jogos da fase regular); campeão = vencedor dos playoffs (Soccer
    Bowl), o 1º da fase regular na observação; pontos do jeito da NASL (6 por vitória + 1 por gol até 3): a classificação é a
    tabela publicada;
  - 1985-1995 sem edição (não houve liga de 1ª divisão);
  - MLS 1996-2025: campeão = MLS Cup (é o título da liga); a Supporters' Shield (melhor campanha) na observação; shootout de
    1996-1999 pela tabela publicada. A temporada 2026 fica para depois da final de 18/12/2026;
  - fora: ASL II (1933-1983, liga regional e depois de 2º nível), International Soccer League (torneio de verão com clubes
    estrangeiros), APSL / A-League (1985-1995, 2º nível) e as temporadas indoor da NASL.
- **Costa Rica (24/11, pesquisado pelo agente; o Guilherme mandou seguir):** a contagem oficial (UNAFUT, igual à lista da
  RSSSF `tablesc/coschamp.html`): 1921 a 2006/07, um campeão por ano (rótulo "1986/87" em diante, quando a temporada passou a
  cruzar o ano); 1954 e 1956 não tiveram campeonato (sem edição); 1961 com duas edições, uma por entidade (Asofútbol, campeão
  Herediano; Federación, campeão Carmelita, reconhecido pela UNAFUT em 2003); de 2007/08 em diante, Apertura e Clausura, uma
  edição cada ("2007 Apertura", "2008 Clausura"), até o Clausura 2026.
- **Honduras (24/11, pesquisado a pedido do Guilherme: "pesquise a fundo e veja se vale pôr ou não"):** só a Liga Nacional,
  de 1965/66 em diante. A Liga Amateur de Honduras (1947-1964, 17 títulos) fica fora: era um mata-mata entre os campeões
  das ligas regionais, não uma liga; a RSSSF a lista à parte da Liga Nacional (`hondchamp.html`); a liga e a FENAFUTH não
  reconhecem esses títulos (há só um pedido do Olimpia, sem decisão); e quase não há dados (vários anos sem vice, nenhuma
  tabela). Se um dia entrar, como competição própria, não dentro do `hon-1`.
- **Panamá (25/11, ok do Guilherme: "sim"):** de 1988 (ANAPROF, depois LPF) em diante, como a lista da RSSSF (63 títulos) e
  a imprensa local; antes só ligas da capital e de Colón, e os campeões de 1952 a 1987 são desconhecidos. Apertura e Clausura
  de 2001 em diante (a liga passou a contar os de 2001 a 2006 como títulos; a final entre os dois campeões fica fora, como
  supercopa). A LINFUNA (1994/95 e 1995/96, liga paralela do racha, reconhecida pela FIFA na época) entra como edições à
  parte: a RSSSF a soma no total e a imprensa conta os 2 títulos do Árabe Unido (15 no total). Apertura 2020 sem campeão.
- **El Salvador (24/11, ok do Guilherme: "siga"):** a lista de campeões da RSSSF (110 títulos), que é a contagem da
  imprensa de lá (FAS 20, Alianza 18, Águila 17). Entram os nove campeonatos nacionais de 1926 a 1946 (final ou quadrangular
  entre os campeões das zonas, que a RSSSF conta como oficiais, como a era amadora do México). Ficam fora 1924-25 (não
  oficiais), os títulos só da Zona Central (1931-36, 1939-41, 1944-45; regionais, como a Liga Capitalina da Guatemala, embora
  a tradição às vezes os conte), 1947 (parou depois de duas rodadas) e a Copa Pilsener 1998/99. O Clausura 2023 (cancelado
  depois da tragédia no Cuscatlán) entra sem campeão.
- **Guatemala (24/11, mesmo critério de Honduras, com o ok do Guilherme para seguir):** só o Campeonato de Liga (Liga
  Nacional), de 1942/43 em diante, como a contagem oficial (Municipal 33, Comunicaciones 32 títulos até o Clausura 2026). A
  Liga Capitalina / Liga Mayor (1919-1941, liga da capital) e os torneios nacionais da época (Campeonato Nacional 1919-1923,
  Campeonato de la República 1931-1941) ficam fora; a RSSSF os lista à parte (`guatchamp.html`).
