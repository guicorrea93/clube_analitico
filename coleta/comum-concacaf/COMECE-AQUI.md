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
| `mex-1` Mexicano | 158 (1902/03–2026 Clausura) | 26.606 | 92 | sem commit (espera o ok) | não |

Gols, cartões, conferência e cobertura: `documentacao/README.md` e `documentacao/mex-1.md`.

## 3. De onde continuar

1. **México (`mex-1`):** pacote pronto em 23/11 (teste de carga OK); espera o ok do commit e as decisões da seção 6 marcadas
   "decididas em 24/11". Recado de fim de coleta no fim de `docs/coleta/pedidos-concacaf.md`.
2. **Próxima: EUA (`usa-1`).** Antes, mandar ao Guilherme as decisões de escopo (MLS só, ou também NASL 1968-1984 e a ASL
   antiga? Campeão da MLS Cup, com a Supporters' Shield na observação?). Os clubes canadenses da MLS entram com país `CAN`.
3. Depois, na ordem sugerida: `crc-1`, `hon-1`, `gua-1`, `slv-1`, `pan-1`, `jam-1`, `tri-1`, `can-1`, `hai-1`; depois as
   outras 1ªs divisões da CONCACAF (Caribe, Guiana, Suriname, Guiana Francesa).
4. Ficar de olho em `docs/coleta/pedidos-concacaf.md`: respostas do agente 1 e pedidos da revisão.

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
