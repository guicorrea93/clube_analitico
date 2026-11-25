# Coleta África — comece aqui

Para o agente de coleta da África (países da CAF) que for continuar este trabalho. Leia antes:
1. `docs/COMECE-AQUI.md` (mapa do projeto);
2. `docs/agente-coleta-COMECE-AQUI.md` (método e formato do pacote);
3. `docs/agentes-internacionais-COMECE-AQUI.md` (o que muda fora do Brasil; regras da casa na seção 10);
4. `coleta/comum-sulamerica/COMECE-AQUI.md` e `coleta/ven-1/` (o exemplo de onde esta pasta foi copiada).

Este arquivo diz o que já foi feito, como e de onde continuar.

Última atualização: 25/11/2026 (plano único de coleta).

## 1. Regras da casa (combinadas com o Guilherme)

**O plano único de coleta (`docs/coleta/plano-de-coleta.md`, 25/11/2026) vale acima de tudo o que estiver diferente
aqui:** ordem das fases e dos países, fontes, formato do pacote, nomes, entrega e git. Pontos dele que mudam o que se
fazia nesta pasta:
- **campeão e vice batem em duas fontes** (a lista da RSSSF e a Wikipédia, ou o site da liga); a divergência vai no
  relatório;
- **decidido fora de campo:** `resultado_especial` "awd", com o placar oficial nos gols (vazios na "derrota para os
  dois") e o de campo na observação; "wo" fica para quem não compareceu;
- **nome repetido:** primeiro a cidade; só sem cidade que resolva, o país entre parênteses. Nunca "de <país>";
- **recado:** item 2 = "Commit: o deste recado (`<mensagem do commit>`)"; o hash vai só na mensagem ao Guilherme;
  **nunca um commit só para anotar o hash**;
- **o ok do Guilherme vale para o commit e o push juntos**; antes do push, conferir `git log origin/main..HEAD`;
- o agente 1 carrega e publica em lotes: não esperar por ele para seguir.

- **Uma competição por vez.** Antes de cada liga, mande ao Guilherme, em poucas linhas, as decisões de escopo (era
  colonial, ligas paralelas, temporadas canceladas). Ao fim de cada uma:
  - resumo curto;
  - pedido de ok para o commit e o push;
  - **recado de fim de coleta**: seção "Recado de fim de coleta — <slug> — <data>" no fim de
    `docs/coleta/pedidos-africa.md`, com os 8 itens da seção 10 do guia internacional, e o mesmo texto ao Guilherme num
    bloco de código. Liste os **países novos** (o agente 1 baixa as bandeiras).
- **Mexa só nas suas pastas:**
  - `coleta/<slug>/` e `coleta/comum-africa/`;
  - `data/coleta/<slug>/`, `data/cache/*-africa*/` e `data/cache/ogol-<slug>/`;
  - `docs/coleta/<slug>.md` e `docs/coleta/pedidos-africa.md`.
- **Banco só para leitura:** `sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)`. O teste de carga usa uma cópia.
- **Git:** nunca `git add -A` nem `git add .`; confira que `git diff --cached` está vazio antes do `git add`; commit e
  push juntos, só com o ok explícito do Guilherme (veja acima); não troque de ramo. A mensagem termina com
  `Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>`.
- **Logs e conferências vão para o scratchpad**, nunca soltos no repositório.
- **Fale com ele em português, curto e por partes.**

## 2. Regras de escopo da África (recado do agente 1, 23/11)

- **Fontes fracas e temporadas incompletas:** entra o que houver. Edição só com o campeão, ou só com a tabela, é aceita;
  edição com parte dos jogos leva `formato` começando por "jogos incompletos ..." (o painel avisa).
- **Temporada cancelada ou anulada** (Egito 2011/12, por exemplo): entra como edição **sem campeão**, com o motivo na
  observação.
- **Fontes:** a RSSSF é a base; o ogol cobre bem o Norte da África e a África do Sul nas últimas décadas.
- **Nomes árabes** (combinado com o agente da Ásia):
  - sempre com hífen ("Al-Ahly");
  - fica com o nome puro o clube mais conhecido no Brasil: Al-Ahly (Egito), Al-Hilal, Al-Ittihad, Al-Nassr e Al-Shabab
    (Arábia Saudita);
  - os outros levam a cidade: "Al-Hilal de Omdurman", "Al-Ittihad de Alexandria", "Al-Ittihad de Trípoli".
- **Lusófonos:** confira o banco antes de batizar ("Benfica" e "Sporting" já são de Portugal); use "Petro de Luanda",
  "1º de Agosto", "Benfica de Luanda".
- **Nome único no mundo:** confira na tabela `clube` do banco e nos `data/coleta/*/pacote/clubes.csv` (inclusive os do
  agente da Ásia, que trabalha ao mesmo tempo) antes de batizar.

## 3. Ordem e estado

**Ordem (plano único de coleta, `docs/coleta/plano-de-coleta.md`, seção 1.1; vale acima da ordem antiga):** ranking de
federações da CAF para as competições de clubes, o de 5 anos que distribui as vagas da Champions da CAF. Foto de
25/11/2026, fixa (não muda depois):
- a tabela em vigor é a da temporada 2026–27 (resultados de 2021–22 a 2025–26): artigo "CAF 5-year ranking" da Wikipédia
  em inglês, seção "Association ranking for the 2026–27 CAF club season", revisão 1384297260
  (https://en.wikipedia.org/w/index.php?title=CAF_5-year_ranking&oldid=1384297260);
- só 27 federações pontuaram. Empates e as 27 com 0 ponto (Burkina Faso inclusive) vão pelo ranking da FIFA masculino
  de 18/11/2026 (https://globalfootballrankings.com/rankings/fifa-world-ranking/men, lido em 25/11/2026);
- o que já está pronto fica pronto; segue-se do primeiro país que falta. Fases (plano, seção 1): 1 = 1ª divisão de
  todas as 54; 2 = copas nacionais; 3 = 2ªs divisões; 4 = o resto. Só se passa de fase com a região inteira feita.

| Ordem | CAF 2026–27 | FIFA (desempate) | País | Slug | Fase 1 |
|---|---|---|---|---|---|
| 1 | 1 |  | Egito (EGY) | `egy-1` | pronto |
| 2 | 2 |  | Marrocos (MAR) | `mar-1` | pronto |
| 3 | 3 |  | Argélia (ALG) | `alg-1` | pronto |
| 4 | 4 |  | África do Sul (RSA) | `rsa-1` | pronto |
| 5 | 5 |  | Tanzânia (TAN) | `tan-1` | pronto |
| 6 | 6 |  | Tunísia (TUN) | `tun-1` | pronto |
| 7 | 7 |  | Angola (ANG) | `ang-1` | pronto |
| 8 | 8 |  | RD Congo (COD) | `cod-1` | **próximo** |
| 9 | 9 |  | Sudão (SDN) | `sdn-1` |  |
| 10 | 10 |  | Mali (MLI) | `mli-1` |  |
| 11 | 11 |  | Costa do Marfim (CIV) | `civ-1` |  |
| 12 | 12 |  | Nigéria (NGA) | `nga-1` | pronto |
| 13 | 13 |  | Líbia (LBY) | `lby-1` |  |
| 14 | 14 |  | Congo (CGO) | `cgo-1` |  |
| 15 | 15 |  | Zâmbia (ZAM) | `zam-1` |  |
| 16 | 16 |  | Gana (GHA) | `gha-1` | pronto |
| 17 | 17 |  | Guiné (GUI) | `gui-1` |  |
| 18 | 18 | 118 | Mauritânia (MTN) | `mtn-1` |  |
| 19 | 18 | 139 | Botsuana (BOT) | `bot-1` |  |
| 20 | 20 |  | Senegal (SEN) | `sen-1` |  |
| 21 | 21 | 42 | Camarões (CMR) | `cmr-1` | pronto |
| 22 | 21 | 115 | Quênia (KEN) | `ken-1` |  |
| 23 | 23 | 89 | Uganda (UGA) | `uga-1` |  |
| 24 | 23 | 98 | Moçambique (MOZ) | `moz-1` |  |
| 25 | 23 | 113 | Togo (TOG) | `tog-1` |  |
| 26 | 26 | 114 | Níger (NIG) | `nig-1` |  |
| 27 | 26 | 166 | Essuatíni (SWZ) | `swz-1` |  |
| 28 | — | 59 | Burkina Faso (BFA) | `bfa-1` |  |
| 29 | — | 71 | Cabo Verde (CPV) | `cpv-1` |  |
| 30 | — | 85 | Benin (BEN) | `ben-1` |  |
| 31 | — | 87 | Gabão (GAB) | `gab-1` |  |
| 32 | — | 105 | Comores (COM) | `com-1` |  |
| 33 | — | 107 | Gâmbia (GAM) | `gam-1` |  |
| 34 | — | 108 | Guiné Equatorial (EQG) | `eqg-1` |  |
| 35 | — | 109 | Madagascar (MAD) | `mad-1` |  |
| 36 | — | 120 | Guiné-Bissau (GNB) | `gnb-1` |  |
| 37 | — | 125 | Ruanda (RWA) | `rwa-1` |  |
| 38 | — | 126 | Zimbábue (ZIM) | `zim-1` |  |
| 39 | — | 129 | Namíbia (NAM) | `nam-1` |  |
| 40 | — | 130 | Malawi (MWI) | `mwi-1` |  |
| 41 | — | 131 | Serra Leoa (SLE) | `sle-1` |  |
| 42 | — | 138 | Burundi (BDI) | `bdi-1` |  |
| 43 | — | 143 | Libéria (LBR) | `lbr-1` |  |
| 44 | — | 144 | Etiópia (ETH) | `eth-1` |  |
| 45 | — | 147 | Lesoto (LES) | `les-1` |  |
| 46 | — | 150 | República Centro-Africana (CTA) | `cta-1` |  |
| 47 | — | 170 | Sudão do Sul (SSD) | `ssd-1` |  |
| 48 | — | 179 | Maurício (MRI) | `mri-1` |  |
| 49 | — | 180 | Chade (CHA) | `cha-1` |  |
| 50 | — | 186 | Eritreia (ERI) | `eri-1` |  |
| 51 | — | 194 | São Tomé e Príncipe (STP) | `stp-1` |  |
| 52 | — | 195 | Djibuti (DJI) | `dji-1` |  |
| 53 | — | 199 | Somália (SOM) | `som-1` |  |
| 54 | — | 205 | Seicheles (SEY) | `sey-1` |  |

| Competição | Edições | Jogos | Clubes | Commit do pacote | No banco |
|---|---|---|---|---|---|
| `egy-1` Egípcio | 73 (1948/49–2025/26) | 11.574 | 74 | 06635c8 (23/11, no GitHub) | sim |
| `mar-1` Marroquino | 110 (1915/16–2025/26) | 11.736 | 100 | 820bf5f (no GitHub) | sim |
| `tun-1` Tunisiano | 109 (1907–2025/26) | 8.092 | 74 | 786998d (no GitHub) | sim |
| `alg-1` Argelino | 64 (1962/63–2025/26) | 15.210 | 81 | b09bbaa (no GitHub) | sim |
| `rsa-1` Sul-Africano | 55 (1971–2025/26) | 8.108 | 89 | b755594 (no GitHub) | sim |
| `nga-1` Nigeriano | 55 (1972–2025/26) | 8.906 | 82 | bc5287a6 (no GitHub) | sim |
| `gha-1` Ganês | 65 (1958–2025/26) | 6.069 | 137 | cd02564c (no GitHub) | sim |
| `cmr-1` Camaronês | 66 (1961–2026) | 6.804 | 85 | e7f2bfa8 (no GitHub) | sim |
| `tan-1` Tanzaniano | 62 (1965–2025/26) | 5.929 | 82 | a22036fc (no GitHub) | sim |
| `ang-1` Angolano | 48 (1979–2025/26) | 6.488 | 93 | "Coleta Angola (ang-1)..." (25/11; teste de carga OK) | não |

Os números de gols, conferência e cobertura estão em `documentacao/README.md`.

**De onde continuar:**
1. `mar-1`: commit 820bf5f; push só quando o Guilherme pedir; esperar o agente 1 carregar (recado no fim de `docs/coleta/pedidos-africa.md`).
2. `tun-1`: commit 786998d (com o `edicoes.csv` do mar-1: pontos por empate e derrota); push só quando o Guilherme
   pedir; esperar o agente 1 carregar (recado no fim de `docs/coleta/pedidos-africa.md`).
3. `alg-1`: commit b09bbaa; push só quando o Guilherme pedir; esperar o agente 1 carregar (recado no fim de
   `docs/coleta/pedidos-africa.md`).
4. `rsa-1`: commit b755594; push só quando o Guilherme pedir; esperar o agente 1 carregar (recado no fim de
   `docs/coleta/pedidos-africa.md`).
5. `nga-1`: commit bc5287a6, no GitHub (24/11); esperar o agente 1 carregar (recado no fim de
   `docs/coleta/pedidos-africa.md`).
6. `gha-1`: commit cd02564c, no GitHub e no painel (25/11). As sete ligas (egy, mar, tun, alg, rsa, nga, gha) estão
   na lista LIBERADAS do painel (`gerar_dashboard_v2.py`).
7. `cmr-1`: commit e7f2bfa8, no GitHub, no banco e no painel (25/11). As oito ligas estão na LIBERADAS.
8. `tan-1`: commit a22036fc, no GitHub e no banco (25/11).
9. `ang-1`: pacote pronto (25/11; teste de carga OK; recado no fim de `docs/coleta/pedidos-africa.md`); commit e push
   com o ok do Guilherme.
10. Próxima liga: `cod-1` (RD Congo, o primeiro país da lista acima que falta). Antes, mandar ao Guilherme o escopo.
11. Pendências de cada liga: na lista `PENDENCIAS` do `documentar.py` (e no `documentacao/README.md`).

## 4. Código comum (`coleta/comum-africa/`)

Copiado de `coleta/comum-sulamerica/` em 23/11/2026. Não importe código da pasta de outro agente: ele pode mudar.

| Arquivo | O que faz |
|---|---|
| `rsssf_africa.py` | leitor genérico das páginas da RSSSF (cópia do `rsssf_sul.py`): `texto`, `ler`, `linha_tabela`, `chave`. **Mudou? Reimporte as ligas já feitas e compare os pacotes** |
| `baixar.py` | `pegar(url, destino, espera)`: download educado, com cache |
| `espn.py` | URL do placar diário e `resumir(evento)` |
| `ogol.py` | calendário de uma edição do ogol (`calendario(id, cache, prefixo)`) |
| `wikipedia.py` | wikitexto pela API |
| `documentar.py` | gera `documentacao/` (ponha a liga em `LIGAS`, `PAIS` e `PENDENCIAS`) |
| `testar_carga.py` | teste de carga numa cópia do banco: `python coleta/comum-africa/testar_carga.py <slug> <scratchpad>` |

**Como fazer uma liga nova:** copie `coleta/egy-1/` (veio do `coleta/chi-1/`, o modelo da América do Sul para "RSSSF onde
tem jogos, ogol onde ela só tem a tabela"). Módulos:

| Arquivo | O que faz |
|---|---|
| `baixar_rsssf.py`, `baixar_ogol.py`, `baixar_wikipedia.py` | baixam para `data/coleta/<slug>/<fonte>/` (o ogol guarda as páginas de calendário em `data/cache/ogol-<slug>/`, para os escudos) |
| `edicoes.py` | `EDICOES`: uma `Edicao` por temporada; `trechos` (RSSSF com jogos), `ogol` (ano do calendário do ogol que é a base), `tabelas` (RSSSF só com a tabela), `cancelada` (motivo; sem campeão), `incompleta` (vira o `formato`), `fases` e `nomes` por edição |
| `ler_rsssf.py` | lê cada edição (RSSSF e ogol), `FASES`, `campeoes()`; limpa o texto antes do leitor comum (ver armadilhas) |
| `clubes_<pais>.py` | `CLUBES` (nome de exibição -> cidade, província) e `REGRAS` (regex sobre a chave do nome, nome, ano inicial, ano final) |
| `conferir.py` | soma dos jogos x tabelas publicadas; `python coleta/<slug>/conferir.py [-v temporada]` |
| `wiki_tabelas.py` | tabelas dos artigos de temporada da Wikipédia em inglês (terceira fonte), lista de campeões e de artilheiros |
| `explicacoes.py` | `EXTRAS` (jogos à mão), `CONSERTA_TEXTO`, `CORRIGE` (também `data`, `nota`, `descartar`, `esp`), `TABELAS_FORA`, `EXPLICACOES` |
| `outras_fontes.py` | casa os jogos da RSSSF com o ogol (rodada, data, nome do clube no ogol) |
| `importar.py` | monta o pacote e o relatório; a classificação é a tabela publicada (ou as de `TABELAS_CLASS`, emendadas) |
| `ver.py` | jogos entre dois clubes numa edição, com a linha da página |

**Pontos por empate e por derrota** (recado do agente 1, 24/11): o `edicoes.csv` tem `pontos_empate` e `pontos_derrota`
logo depois de `pontos_vitoria`; preencha só quando não são 1 e 0 (`Edicao.pontos` dá os três; o `importar.py` deixa
vazio quando é 1-0). Egito: sempre 1 e 0; Marrocos 3-2-1 até 1994/95; Tunísia 3-2-1 até 1985/86 e 4-2-1 até 1991/92.

Regra das divergências (Egito, 23/11): quando a tabela da RSSSF e a soma dos jogos não fecham, olhe a tabela do artigo da
temporada na Wikipédia. Se ela fecha com os jogos, o erro é de digitação da RSSSF e a classificação usa os números dos jogos.
Se ela confirma a RSSSF, o relatório aponta o jogo provável, mas **nenhum placar é mudado** só pela tabela. Jogo que falta
numa fonte entra à mão (`EXTRAS`) só quando há outra prova do placar (lista de resultados do clube, notícia).

## 5. Fontes por país (o que já se sabe)

**Egito (`egy-1`):**
- RSSSF: lista de campeões em `tablese/egychamp.html` (não `egypchamp`); uma página por temporada (`egy49` ... `egy99`,
  `egy00` ... `egy09`, `egy2010` ... `egy2026`, pelo ano em que a temporada termina). Faltam as das temporadas não
  terminadas 1954/55, 1970/71, 1973/74 e 1989/90; 2011/12 (`egy2012`) só tem a tabela no abandono.
- ogol: competição `liga-egipcia`, edições de 1948/49 a 2026/27.
- ESPN: não tem a liga egípcia (`egy.1` dá erro 400).
- **Escopo (pesquisa de 23/11):** só a liga nacional, de 1948/49 em diante. Motivos:
  - a liga nacional foi criada por decreto real em 22/10/1948; Wikipédia en e ar, RSSSF e ogol começam aí, e a contagem
    de títulos dos clubes também (Al-Ahly 45, Zamalek 15);
  - o campeonato da U.I.S.S.E. (1912/13 a 1914) era mata-mata, com clubes de colônias estrangeiras (gregos, italianos,
    malteses); a federação atual (1921) **não o reconhece** (RSSSF, `egy1913.html`); o próprio Zamalek o lista como título
    "não oficial";
  - a Liga do Cairo (1922/23 a 1957/58) era regional (havia também as de Alexandria, Canal e Bahary) e é contada à parte.
    Se um dia entrar, é como competição regional própria, não no `egy-1`.
- **1971/72:** a RSSSF chama de 1970/71 a temporada interrompida pela briga em Al-Ahly x Zamalek; o jogo foi em
  24/12/1971 (Kooora; Wikipédia en): é a 1971/72, e 1970/71 não foi disputada.
- **Wikipédia:** há artigo por temporada ("1974–75 Egyptian Premier League") com a tabela final, tirada do site do Dr. Tarek
  Said (um dos autores da RSSSF), em versão mais nova; faltam 1979/80 a 1982/83, 1984/85 a 1986/87, 1988/89, 1989/90 e
  1999/00.

**Marrocos (`mar-1`):**
- RSSSF: lista de campeões em `tablesm/marochamp.html` (39 títulos de 1915/16 a 1954/55 e 70 desde 1956/57).
- **Escopo (pesquisa de 24/11):** entra a era colonial, de 1915/16 a 1954/55 (campeonato do Marrocos da USFSA e, desde 1922,
  da Liga do Marrocos, LMFA). Motivos:
  - a federação marroquina conta esses títulos: em 2015, o site da FRMF anunciou o "18º título do WAC desde 1948" (5 antes
    de 1956 e 13 depois), e o porta-voz disse que o palmarès é contado desde 1916 (TelQuel, 20/05/2015);
  - RSSSF ("Number of Titles: 109, overall, since 1915"), Wikipédia en e fr e o próprio Wydad (22 títulos) contam os
    títulos de antes da independência;
  - era o campeonato do Marrocos inteiro, não uma liga regional (diferente da Liga do Cairo do Egito).
- Ficam de fora: a "Ligue libre" (1946-1956, liga paralela dos clubes marroquinos, que ninguém conta no palmarès) e
  1955/56 (sem competição). 1942/43 (abandonado; a US Marocaine ganhou a Coupe de la Guerre) entra como edição sem campeão.
- Páginas por temporada: `maroAA` (ou `maroAAAA` nos anos 1910 e desde 2010), `maro3944` com 1938/39 a 1944/45. Sem página:
  1917/18 a 1921/22, 1923/24, 1925/26 a 1927/28, 1970/71, 1973/74, 1981/82.
- Tabela de confrontos (matriz) de 1956/57 a 1967/68, 1980/81, 1989/90 e 1990/91: `ler_rsssf.matriz()`.
- Sistema de pontos 3-2-1 (vitória, empate, derrota) até 1994/95; 3-1-0 desde 1995/96 (`Edicao.pontos`).
- ogol: competição `liga-marroquina`; só tem jogos de 2004/05 em diante (antes, vazio). ESPN: não tem (`mar.1` dá 400).
- Wikipédia: artigos "AAAA–AA Botola" de 1956/57 em diante, mas só os de 2002/03 em diante têm tabela (os antigos são
  esboços); "1972–73 Botola" e "1989–90 Botola" redirecionam para o artigo da liga (tabela de todos os tempos: não use).
  Baixe em lote (`baixar_wikipedia.lote`, 50 títulos por pedido): um por um, o limite de ritmo deixa o download em horas.
- 1946/47: a lista de campeões da RSSSF dá a US Marocaine, mas a página da temporada e a Wikipédia dão a USA Casablanca,
  que venceu o desempate do título (`campeao_rsssf` da edição).

**Tunísia (`tun-1`):**
- RSSSF: lista de campeões em `tablest/tunchamp.html` (de 1907; conta 29 títulos de 1921/22 a 1954/55 e 71 desde 1955/56).
- **Escopo (pesquisa de 24/11; o Guilherme autorizou decidir pela pesquisa):** entra a era colonial, desde 1907 (campeonato
  da USFSA até 1920/21 e da Liga da Tunísia de 1921/22 a 1954/55). Motivos:
  - a contagem oficial usada na Tunísia inclui a era colonial: o "34º título" do Espérance em 2024/25 (La Presse de Tunisie,
    Kapitalis, FIFA) só fecha com o título de 1941/42 (33 depois da independência), e o "14º" do Club Africain em 2025/26
    só fecha com os de 1946/47 e 1947/48;
  - a Wikipédia conta desde 1907 ("record of champions since 1907"; as primeiras temporadas, da USFSA); a RSSSF lista desde
    1907 e conta desde 1921. Como no Marrocos (onde a era da USFSA entrou, porque a FRMF conta desde 1916), entra desde 1907.
- Ficam de fora os anos sem competição (1909/10, 1914/15 a 1918/19, 1939/40, 1940/41, 1942/43, 1943/44); 1951/52
  (abandonado) entra sem campeão.
- RSSSF: páginas por temporada `tunAA` (ou `tunAAAA` nos anos 1900-1910 e desde 2009), pelo ano em que a temporada termina;
  na era colonial só há página de 12 anos (`_PAGINAS_COLONIAIS` em `edicoes.py`), quase sempre só com a final. De 1955/56 a
  2002/03, a lista de tabelas finais `tablest/tunhist.html` (seção "1955-56"; `ler_rsssf.secao_hist()`) é a tabela.
- Tabela de confrontos (matriz) de 1968/69, 1970/71, 1977/78, 1980/81, 1982/83 e 1987/88 a 1995/96; em vários anos com o
  nome do clube, não a sigla (`matriz_nomes()`).
- Pontos: 3-2-1 até 1985/86, 4-2-1 de 1986/87 a 1991/92, 2-1-0 de 1992/93 a 1994/95, 3-1-0 desde 1995/96.
- ogol: competição `liga-tunisina`, edições de 1955/56 a 2025/26, mas só com jogos de 2005/06 em diante. ESPN: não tem.
- Wikipédia: artigos "AAAA–AA Tunisian Ligue Professionnelle 1" (ou "... National Championship"), baixados em lote; as
  notas da tabela de confrontos ("match_X_Y_note") explicam resultados dados fora de campo (2025/26).
- 1909/10: a Wikipédia dá um título ao Racing Club de Tunis; a RSSSF diz que não houve campeonato (fica de fora).

**Argélia (`alg-1`):**
- **Escopo (pesquisa de 24/11; o Guilherme aprovou em 24/11):** só o campeonato nacional, de 1962/63 em diante (64
  edições). A RSSSF ("64 títulos; desde a independência") e a Wikipédia (en e fr) contam desde 1962/63, e a contagem dos
  clubes também (o "10º título" do MC Alger em 2026 só fecha sem a era colonial). A era colonial fica de fora: não havia
  campeonato único (ligas regionais de Argel, Orã e Constantine, cujos campeões iam ao Campeonato do Norte da África), e o
  "campeonato da Argélia" de 1957/58 a 1960/61 era do futebol colonial francês, que ninguém conta.
- 2019/20: parado em março de 2020 (Covid); a federação declarou o CR Belouizdad campeão, sem rebaixamento: entra com
  campeão (título oficial), com os jogos até a parada e a observação.
- Nomes: siglas francesas, como os clubes são conhecidos (MC Alger, USM Alger). JS Kabylie = JE Tizi Ouzou = JS Kawkabi;
  CR Belouizdad = CR Belcourt; MC Alger = MP Alger; ES Sétif = EP Sétif; MC Oran = MP Oran. O USM Annaba campeão de
  1963/64 não é o atual (fundado em 1984).
- RSSSF: lista de campeões em `tablesa/algchamp.html`; páginas `alg63` (1962/63) ... `alg99`, `alg00` ... `alg09`,
  `alg2010` ... `alg2026`, pelo ano em que a temporada termina (as `alg1905`, `alg17`, `alg18`, `alg21` a `alg59` são da
  era colonial e não são baixadas).
- ogol: competição `liga-argelina`, edições de 1962/63 a 2026/27. Wikipédia: artigo de toda temporada ("1993–94 Algerian
  Championnat National"; desde 2010/11, "Algerian Ligue Professionnelle 1"); a lista de campeões traz vice, 3º e artilheiro.

**África do Sul (`rsa-1`):**
- **Escopo (pesquisa de 24/11; o Guilherme aprovou em 24/11):** a linha do futebol profissional que a RSSSF ("NPSL/NSL/PSL
  championships, 55, since 1971") e a imprensa contam (Sundowns 18, Chiefs 12, Pirates 10): NPSL 1971-1984, NSL
  1985-1995, PSL desde 1996/97. Fora: as ligas separadas por raça do apartheid (NFL dos brancos, SASL/FPL), a NPSL paralela
  depois de 1985, as NPSL amadoras de 1968 e 1969 e o torneio de transição de 1996 (Coca-Cola Challenge).
- RSSSF: lista em `tablesz/zafchamp.html` (seção "National Champions", uma coluna por liga em cada bloco); páginas `zaf71`
  ... `zaf96` (ano civil), `zaf97` (1996/97) ... `zaf2026`. 1971-1977: a página é da NFL; a NPSL vem no meio (1971, 1974,
  1976) ou nem vem (só o campeão). Até 1995, quase só a tabela final.
- ogol: competição `liga-sul-africana`, edições desde 1996/97, mas só com jogos de 2005/06 em diante.
- Wikipédia: artigos por temporada (48 de 55); o artigo da liga não tem lista de campeões que sirva (desligada).

**Nigéria (`nga-1`):**
- **Escopo (pesquisa de 24/11; o Guilherme aprovou em 24/11):** a liga nacional desde 1972, como a liga e a imprensa contam
  (o título de 2025/26 foi o "9º" do Enugu Rangers); fora a Amachree Gold Cup de 1971 (a RSSSF conta), as ligas
  regionais e as copas. 2018 e 2019/20 abandonados, sem campeão.
- RSSSF: lista em `tablesn/nigchamp.html`; páginas `nig72` (a década de 1970 inteira), `nig83` ... `nig99`, `nig00` ...
  `nig09`, `nig2010` ... `nig2026` (sem 1980 a 1982; `nig88` = 1987/88). Temporadas no ano civil até 2007, 2007/08 a
  2011/12, ano civil de 2013 a 2019, depois 2019/20 a 2021/22, 2023 e 2023/24 em diante.
- ogol: competição `liga-nigeriana`, jogos só de 2008/09 em diante; **rotula as temporadas de ano civil pelo ano anterior**
  ("2016/17" = 2017; "2022/23" = 2023): cada edição se liga ao ogol pelo id (`Edicao.ogol_id`), não pelo ano.
- Wikipédia: artigos por temporada só de 2009/10 em diante.

**Gana (`gha-1`):**
- **Escopo (pesquisa de 24/11; o Guilherme aprovou em 24/11):** a liga nacional de 1958 a 2025/26, como a lista da RSSSF,
  sem o campeonato não oficial de 1956 e sem a competição especial do Comitê de Normalização de 2019 (não foi liga; a
  imprensa não a conta: 2021/22 foi o "25º título" do Kotoko). 2018 e 2019/20 abandonados, sem campeão.
- RSSSF: lista em `tablesg/ghachamp.html`; lista de tabelas finais `ghahist.html` (seção = a própria temporada; tabelas só
  até 1987); páginas `gha58` ... `gha99`, `gha00` ... `gha09` (sem `gha06`), `gha2010` ... `gha2026`. "2004/05" é a
  `gha04` e "2005" é a `gha05` ("Ghana 2005/06").
- ogol: competição `liga-ganesa`, mesmo rótulo de temporada que a RSSSF, jogos só de 2008/09 a 2010/11 e de 2015 em diante.

**Angola (`ang-1`):**
- **Escopo (pesquisa de 25/11; o Guilherme aprovou em 25/11):** o Girabola de 1979 a 2025/26 (48 edições), como a
  federação o numera (2025/26 = "XLVIII Girabola") e os clubes contam os títulos. 2019/20 abandonado (Covid-19), sem
  campeão. Fora: o Campeonato Provincial da era colonial (1941–1974; 1975 abandonado), a Taça e a Supertaça.
- RSSSF: lista em `tablesa/angochamp.html` (parte "Since Independence"; desde 2019 o ano é o do fim da temporada); páginas
  `ango79` ... `ango99`, `ango00` ... `ango09`, `ango2010` ... `ango2026`. Tabela só de 1981 a 1997.
- Pontos: 2-1-0 até 1994, 3-1-0 desde 1995 ("introduction of 3-1-0 point system in 1995").
- ogol: competição `liga-angolana`, mesmo rótulo; jogos só de 1999 em diante.
- Wikipédia: não baixada (a API recusou por excesso de pedidos em 25/11/2026, com outro agente baixando ao mesmo tempo);
  pendência: rodar `coleta/ang-1/baixar_wikipedia.py` e reimportar.

**Tanzânia (`tan-1`):**
- **Escopo (pesquisa de 25/11; o Guilherme aprovou em 25/11):** a liga do continente (Tanganica), hoje Ligi Kuu Tanzania
  Bara, de 1965 a 2025/26 (62 edições), com o campeão do continente em todos os anos: é a lista que a TFF e os clubes
  contam (2024 = "30º título" do Young Africans). Fora: a liga de Dar es Salaam (1921–1964), a "Union League" de 1982 a
  2003 (continente x Zanzibar; é o campeão que a lista da RSSSF dá nesses anos), Zanzibar (membro associado da CAF, fica
  fora da lista das 54) e as copas. A mini-liga de transição de 2007 entra (a RSSSF e o Simba a contam).
- RSSSF: lista em `tablest/tanzchamp.html` (de 1982 a 2003, o campeão do continente está na 2ª coluna); páginas `tanz65`,
  `tanz82` ... `tanz91`, `tanz96` ... `tanz99`, `tanz00` ... `tanz09`, `tanz2010` ... `tanz2026`. O "1995/96" e o "1996/97"
  das páginas são os campeonatos que a lista chama de 1996 e 1997; desde 2008 a lista usa o ano do fim ("2008" = 2007/08).
- Pontos: 2-1-0 até 1995 (pelas tabelas até 1989), 3-1-0 desde 1995/96 (pelas tabelas desde 1996/97).
- ogol: competição `liga-tanzaniana`, mesmo rótulo; jogos só de 2007/08 em diante (as edições antigas vêm vazias).
- Wikipédia: "AAAA–AA Tanzanian Premier League", com tabela de 2015/16 em diante.

**Camarões (`cmr-1`):**
- **Escopo (pesquisa de 25/11; o Guilherme aprovou em 25/11):** o campeonato nacional de 1961 a 2026 (66 edições), como a
  lista da RSSSF ("since independence"); "1960" e "1961" da lista são o mesmo campeonato (uma edição, "1961"). Fora: o
  campeonato territorial da era colonial (1936/37 a 1955/56), as ligas do Camarões anglófono até 1972 e as copas.
- RSSSF: lista em `tablesk/kamchamp.html`; páginas `kam61`, `kam68`, `kam79` ... `kam99`, `kam00` ... `kam09`,
  `kam2010` ... `kam2026` (sem página: 1962 a 1967, 1969 a 1977/78, 1984/85, 1992). O rótulo alterna ano civil e duas
  temporadas (mapa em `edicoes._PAG`). Até 1998 só tabela, topo da tabela ou campeão; jogos de 1999 em diante.
- Pontos: 2-1-0 até 1987/88 e de 1991 a 1994; 3-1-0 em 1988/89 e 1989/90 (a página anota) e desde 1995.
- ogol: competição `liga-dos-camaroes`; jogos de 2005 em diante, fora 2013 a 2016 (vazios); **rotula pela data** ("2004/05"
  = 2005; "2011" = 2010/11; "2024" = 2023/24): mapa em `edicoes._OGOL`.
- Wikipédia: "AAAA Cameroonian Premier League" até 2007 (com o ano do fim da temporada), "AAAA–AA Elite One" depois; tabela
  de 1982/83 em diante.

## 6. Armadilhas já encontradas

**RSSSF (Egito):**
- **Nome com apóstrofo perto do fim** ("Razja'h", "Ala'ab"): o leitor comum recusa a linha do jogo (protege de "58' Kempes")
  e o jogo some sem aviso; 2013/14, 2014/15 e 2017/18 perdiam de 10 a 38 jogos. `ler_rsssf.linhas()` tira o apóstrofo.
- **Cidade entre colchetes na tabela** ("8.Al Qanat [Suez]  26 7 9 10 ..."): a linha não é lida e a tabela se parte em duas
  (1991/92 a 1995/96). Vira parênteses em `linhas()`.
- **Autores que continuam na linha de baixo** sem "[" ("   Mohamed Abd Rabbou 22]"): o "Abd" era lido como jogo abandonado.
  `_sem_resultados()` junta a continuação à linha de cima.
- **Listas "Results Ahly:"** (ida e volta na mesma linha, sem data nem mando): ficam de fora.
- **Tabela cruzada** ("Ismaily  xxx 0-1 0-1"): a linha é apagada e os jogos entram à mão (`EXTRAS`).
- **Copa sem título** depois da liga ("Preliminary Round", 2004/05) ou com título curto ("Cup 2001/02"): corte o trecho
  (`FIM_PADRAO` ou linha final explícita).
- **Índice no topo** das páginas de 2009/10 em diante ("First Level", "Egypt Cup", "Second Level"): o campeonato começa no
  segundo "First Level" (`inicio()`).
- **"Championship Playoff"** é um jogo só em 2008/09 (desempate do título) e um grupo em 2013/14, 2024/25 e 2025/26; e
  "Relegation Playoff" é um jogo em 1997/98 e 1998/99 e um grupo em 2024/25: `fases` por edição.
- **Jogo interrompido e completado** (2023/24, Pyramids x Smouha): duas linhas; fica a da continuação (`CORRIGE`).

**ogol (Egito):**
- O calendário vem cortado quando o ogol limita o ritmo (aviso "edição incompleta"): apague o `<id>.json` e baixe de novo
  (as páginas do cache ficam).
- **Cobertura:** jogos de 1964/65 em diante; antes, as edições existem mas vêm vazias.
- **Clube trocado:** "Suez Club" é um código só para dois clubes de Suez; "Bani Ebeid" em 2011/12 é o Telephonat Beni Suef;
  "Team" (1999-2002) não identifica o clube.
- **Temporada abandonada** (2011/12): 0-0 em jogos que nunca aconteceram e "ANU" nos anulados; confira com a tabela no
  abandono.
- **Rodadas recomeçam** na fase final (2025/26: "R1" de novo): a fase sai do segundo encontro do par (`DIVIDE_DEPOIS`).
- Faltam jogos isolados (1990/91 e 1993/94: um Al-Ahly x Ismaily cada).

**RSSSF (Marrocos):**
- **Tabela de confrontos com siglas repetidas** ("KAC" é o Kawkab de Marrakech e o Kénitra na mesma página) e sigla longa
  ("LARACHE"): cada linha da matriz é ligada ao clube da tabela pela campanha mais parecida, e a ordem desempata. Tire da
  conta a linha do clube que desistiu (vários "n/p"), senão a ligação troca clubes de mesma campanha (1959/60).
- **"A bt B" / "A lt B"** (venceu / perdeu sem placar): viram vitória sem placar, com a nota; "drw" (empate sem placar) fica
  de fora. Placar no fim da linha ("COD Meknes  - SA Sale   5-2", anos 1990) volta ao formato comum em `linhas()`.
- **Notas de outra fonte com placares** ("OC Khouribga   38-21 instead of 40-22"): eram lidas como jogos; saem em `_limpa()`.
- **Classificação só com pontos** ("2.USD Meknes  22   59"): `ler_rsssf.parcial()`; o nome acaba no primeiro número.
- **Copa no meio da página** com título "Morocco Cup ..." ou "XVIIIth edition of the Coupe du Trone": no `FIM_PADRAO`.
- **Siglas e nomes curtos dos anos 1990** ("Fes", "KAC", "Ittihad") dependem do ano: `nomes` da edição.
- **Nome grudado no número** na tabela ("Credit Agricole Rabat30"): `CONSERTA_TEXTO`.

**RSSSF (Tunísia):**
- **Células "awd" na tabela de confrontos** (1968/69, 1970/71, 1977/78, 1980/81): o leitor da matriz pula; quem venceu está
  no "NB: X-Y was awarded a win to Z". Entram em `EXTRAS` como W.O. (a tabela conta a vitória sem gols).
- **Nota do resultado dado antes do placar e quebrada** ("[2-0 awarded; originally 0-0; / ... ineligible player]",
  2006/07): o leitor não pega o 2-0; `CORRIGE` com `"oficial": (2, 0)` (chave nova, em `conferir.preparar`).
- **"Groupe A"** (francês) vira "Group" em `linhas()`; **título de grupo com data** ("Group A [Sep 12]"): o leitor comum
  (`rsssf_africa._GRUPO`) passou a aceitar.
- **Jogos da 1ª fase sem o grupo** (2021/22 a 2023/24): `GRUPO_PELA_TABELA` deixa o grupo em branco e a conferência o tira
  das tabelas.
- **"Final Table:" x "Final [data]"**: padrão de fase `^Final\b` pega o título da tabela e some com as tabelas (2021/22);
  use `^(Semi)?[Ff]inal \[`.
- **"Relegation Playoff"** é grupo na maioria dos anos e jogo único em 2023/24; **"Seventh Place Match"** etc. (2012/13,
  2021/22) são jogos de classificação e a ordem final vem deles (`ORDEM_FINAL` no `importar.py`).
- **Rebaixamento fora da tabela** ("NB: AS Marsa relegated", "Barrages" com a 2ª divisão, exclusão, decisão do CAS):
  `SITUACAO_FIXA` no `importar.py`; "Not Relegated" não conta como rebaixado.
- **Tabela partida por erro de digitação** (`tun06`, Club Africain "12 9 3"): `CONSERTA_TEXTO`.
- **"ES" em 1949/50** é o Espérance (o Étoile é "ES Sahel"): `nomes` da edição.

**RSSSF (Argélia):**
- **Índice no topo** de toda página ("Ligue 1", "Coupe Nationale", "Ligue 2"...): a 1ª divisão é a primeira seção depois
  dele; o fim é a seção seguinte do índice ou o padrão de fim, o que vier primeiro (`ler_rsssf.secao()`; o título da copa
  no corpo nem sempre é o do índice). 1999/00 a 2001/02: a 1ª divisão é a "Super Division" (a "Division 1" é a 2ª).
- **Tabela com o nome atual e o da época entre colchetes** ("JS Kabylie ... [as Jamiat Sari' Kawkabi]"); os jogos usam o
  nome da época (JS Kawkabi, MP Alger, NAR Alger...): as regras de `clubes_alg.py` saíram desses colchetes.
- **Listas de jogos que não fecham com a tabela da própria página** (quase todo ano de 1964/65 a 1998/99): o ogol copia a
  RSSSF (mesmos placares) e a Wikipédia confirma a tabela; nada a corrigir sem outra fonte.
- **Rodada copiada** (1974/75, 1975/76) ou repetida (1972/73): o mesmo mandante x visitante duas vezes; procure com um
  contador de pares por temporada.
- **Datas com o ano errado:** jogo adiado listado depois de janeiro faz o leitor comum avançar o ano de novo
  (`ano < ano_fim + 1` em `rsssf_africa.ler`); a Argélia acerta o ano pelo mês (`ler_rsssf._acerta_anos`).
- **"[0-3 awarded; abd at 1-2]"**: o placar vem antes de "awarded"; `linhas()` inverte para "[awarded 0-3; ...]".
  "temporarily awarded ... later revoked" (2002/03) foi tirado com `CONSERTA_TEXTO`.
- **Nome partido por espaços** ("NA Hussein          Dey 1-2", "MO  Constantine") e cidade repetida ("ASPTT Alger
  Alger"): `linhas()`.
- **Tabela "acumulada":** a conferência herdada pula tabela com mais jogos que a soma; na Argélia não há tabela acumulada
  e isso escondia os anos com jogos faltando (desligado em `conferir.py`).

**RSSSF (África do Sul):**
- **Fim do trecho:** copa com o nome entre parênteses ("Datsun Challenge 1982 (NPSL League Cup)"), ligas regionais ("Natal
  Football League", "Transvaal Soccer Board League") e desempates de acesso com a 2ª divisão ("Mvela Golden League
  Platinum Playoffs", 2006/07; "Promotion/Relegation Playoff"): no `FIM_PADRAO` ou linha final explícita.
- **Cidade entre colchetes** na tabela ("Bush Bucks [Durban]"): vira parênteses em `linhas()`.
- **Vitórias + empates + derrotas que não dão os jogos** (1982, 1986, 1993): a linha não é lida e a tabela se parte;
  `CONSERTA_TEXTO`, com os pontos dizendo o número certo.
- **Clube que muda de nome no meio da temporada** (1993, 2007/08) ou "Rangers" que muda de dono por época: regras por ano e
  `nomes` da edição.
- **Clube excluído com resultados anulados** (Royal AM, 2024/25): `ANULA_CLUBE` e a linha "record at exclusion" em
  `TABELAS_FORA`.
- **Rebaixamento pelos desempates de acesso** não vem na tabela: `SITUACAO_FIXA` (15º que some no ano seguinte); venda de
  vaga (comum na PSL) não é rebaixamento.

**RSSSF (Nigéria):**
- **Tabelas dos anos 1990 em outros formatos** ("Teams P W SD GLD L GF GA GD PTS", "P W D L ...", "14  9/ 3   4"): convertidas
  em `linhas()`; o empate com gols valia 2 pontos (o ponto a mais vai no `ajuste_pontos`).
- **"3SC"** (Shooting Stars) começa por número: o leitor comum recusa a linha; trocado em `linhas()`.
- **Nota que continua nas linhas de baixo** cola em outro jogo ("committee annulled ..." marcou como anulado um jogo
  válido, 2023/24): `CORRIGE`.
- **Rodada anulada e jogada de novo** ("Replay Round 20", 2005) e resultado dado depois revogado: `CORRIGE`.
- **"3 points and 3 goals deducted"**: a tabela desconta os gols; os jogos não fecham (explicado).

**RSSSF (Gana):**
- **Nota que lista resultados dados com o placar de campo** ("rd 1 Goldfields 1-0 Arsenal, awarded 0-3", 2003): era lida
  como jogo (os nomes "1 Goldfields", "3 BA United"); descartada, e os jogos das rodadas ficam com o placar dado.
- **"FC Samartex 1996"**: o ano no fim do nome confunde o leitor; vira "FC Samartex" em `linhas()`.
- **2ª divisão regional logo depois da liga** ("Central Regional Division 2", 2017): linha final explícita.

**RSSSF (Camarões):**
- **"awarded 0-0 win to X"**: vitória dada sem gols (a tabela conta a vitória e nenhum gol); o leitor deixa sem resultado.
  `CORRIGE` com `wo_m`/`wo_v` e sem placar (2009/10, 2023/24); "original score stood but points awarded" fica com o placar.
- **Resultado dado marcado "abd" ou "n/p"** ("abd ... [awarded 3-0; 1-0 abd at 75']", "n/p ... [awarded 3-0]"): ficava fora
  da conta; `CORRIGE` com `oficial`.
- **Nota que continua na linha de baixo** ("award of 3-0 annulled, match refixtured", 2024/25) anulou um jogo válido.
- **Rodada copiada** (2000: a 21 repete a 22) e **tabelas "not checked with scores"** (2000) ou duas tabelas (2001: a
  oficial da FECAFOOT e a dos resultados conhecidos).
- **"Poule A"** não é título de grupo para o leitor comum: vira "Group A" em `linhas()`.
- **Artilharia no meio da liga** ("Topscorer (only playoff)", 2004) encerra o trecho pelo `FIM_PADRAO`: trechos explícitos.
- **Fase final que numera depois dos clubes só da 1ª fase** (2019: grupo do rebaixamento 13º a 18º): `TABELAS_FIM` no
  `importar.py`.
- **Dois Aigle Royal** (Moungo, de Nkongsamba; Menoua, de Dschang) e "Aigle" sozinho nos jogos: regra por ano em
  `clubes_cmr.py`.

**RSSSF (Tanzânia):**
- **Zanzibar e a Union League na mesma página**, às vezes logo depois dos primeiros colocados do continente (sem tabela):
  `FIM_SEMPRE` no `ler_rsssf.py` encerra o trecho em qualquer ponto.
- **Clubes do exército com número** ("977 KJ Meru Warriors", "82 KJ Rangers", "44KJ"): o número vira posição ou
  campanha; trocados em `linhas()` ("KJ977 ...").
- **Matrizes de vários tipos:** numerada com a campanha nas pontas (1984: `matriz_numerada`) e por grupo, com siglas e
  "xxx" na diagonal (2000: `matriz_grupos`, só dentro do trecho: a Union League vem em matriz depois).
- **A "Superleague 1991"** é a fase com Zanzibar (Small Simba, Jamhuri): 1991 fica só com o campeão.
- **Tabelas do meio da temporada** (2005) e **linhas de campanha anulada** de clube excluído (2001, 2004): `TABELAS_FORA`;
  vários clubes excluídos na mesma edição: `ANULA_CLUBE` aceita lista.
- **Nota de jogo dado que não valeu** ("may yet be awarded 2-0", 1999): `CORRIGE` com `"oficial": None`.
- "Second level" em nota corrida casava com o `FIM_PADRAO` (que ignora maiúsculas): os nomes de divisão ficam em
  `(?-i:...)`.

**RSSSF (Angola):**
- **Clubes com data no nome** ("1º de Agosto", "17 de Maio", "4 de Abril", e "1º Agosto", "1° de Agosto"): o número
  quebra a linha da tabela e a do jogo; `linhas()` troca pelo extenso ("Primeiro de Agosto") e `clubes_ang.clube()` faz o
  mesmo com os nomes do ogol. Os ids das tabelas mudam depois da troca (as linhas passam a ser lidas inteiras).
- **Nota recuada que cita uma copa** ("    Cup, together with ..."): encerrava o trecho; o `fim_padrao` ignora linhas
  recuadas.
- **Tabela final sem o clube desclassificado** (1998, Kabuscorp): o importar escolhia uma tabela do meio da temporada que
  tinha todos os clubes; `TABELAS_CLASS` com a final.
- **O mesmo jogo duas vezes**, uma delas colada na continuação de uma nota (1999): `CORRIGE` descarta.
- Nomes repetidos em outros países: "ASA" já é o de Arapiraca (vira "ASA de Luanda"); os Benficas levam a cidade.

**ogol (Camarões):** em 2010/11 o Union e o Caïman Douala têm o mesmo nome e o mesmo id (2482): os jogos dos dois ficam de
fora. Nomes como "Lausanne SA De Yaoundé", "FC Renaissance", "Eagle Royale Casamba".

**ogol (Argélia):** só tem jogos de 1985/86 em diante, com os mesmos placares da RSSSF (copiados): serve para data e
rodada, não como segunda fonte de placar. Nomes curtos ("CS Constantinois", "Ol. Medea", "Tadjenanet", "MCE Bayadh").

**ogol (Tunísia):** "DA" (decisão administrativa) vem sem placar e o jogo some: entra em `EXTRAS` com o resultado dado
(2025/26, US Monastir x CS Sfaxien). Edições cortadas pelo limite de ritmo: veja os avisos do log e baixe de novo.

**Python no Windows:** como no guia da América do Sul, editar por heredoc com `python - <<'EOF'` transforma `\b` em
backspace; o `sed` com `\\b` também erra. Use o Edit e confira com `grep -c $'\x08'`.
