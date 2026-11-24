# Coleta América do Sul — comece aqui

Para o agente de coleta América do Sul (agente 4) que for continuar este trabalho. Leia antes o guia geral
`docs/agentes-internacionais-COMECE-AQUI.md`, com o formato do pacote, as pastas de cada agente e as regras de identidade
dos clubes. Este arquivo diz o que já foi feito, como foi feito e de onde continuar.

Última atualização: 22/11/2026.

**Documentação completa:** `coleta/comum-sulamerica/documentacao/`. Tem o índice (`README.md`) e uma ficha por competição,
com:
- tudo o que o pacote tem e se já está no banco;
- como as edições foram definidas, fontes e regras;
- conferência com as tabelas publicadas;
- cobertura de cada campo, década a década;
- formato ao longo do tempo;
- campeões, vices e ajustes de pontos;
- todas as correções e decisões, com o motivo;
- o que não deu para coletar;
- pendências, com os achados da revisão ainda abertos.

A documentação é gerada por `python coleta/comum-sulamerica/documentar.py` a partir dos pacotes, do código e dos relatórios.
Rode depois de toda importação ou correção e mantenha à mão só a lista `PENDENCIAS`, no começo do script. Os relatórios
`docs/coleta/<slug>.md` continuam com o detalhe edição a edição.

## 1. Regras da casa (combinadas com o Guilherme)

- **Uma competição por vez, e só quando ele pedir.** Ao fim de cada uma:
  - resumo curto;
  - pedido de ok para o commit;
  - **recado de fim de coleta** (regra de 22/11): seção "Recado de fim de coleta — <slug> — <data>" no fim de
    `docs/coleta/pedidos-sulamerica.md`, para o agente 1 (banco e painel) e para o agente de revisão, e o mesmo texto ao
    Guilherme, num bloco de código. Conteúdo:
    1. o que foi feito: edições, jogos, clubes, gols com autor, cartões e fontes;
    2. commits;
    3. resultado do teste de carga;
    4. pedidos ao banco e ao painel: o que carregar, formatos novos, colunas vazias, casos especiais;
    5. decisões tomadas (com o motivo) e as que esperam o Guilherme;
    6. o que não deu para coletar e as pendências, com a fonte que poderia resolver;
    7. onde a revisão deve olhar primeiro;
    8. próxima competição.
- **Mexeu no leitor comum?** Diga no recado quais competições mudaram e se ids de partidas mudaram.
- **Mexa só nas suas pastas:**
  - `coleta/<slug>/` e `coleta/comum-sulamerica/`;
  - `data/coleta/<slug>/`, `data/cache/*-sulamerica*/` e `data/cache/ogol-<slug>/`;
  - `docs/coleta/<slug>.md` e `docs/coleta/pedidos-sulamerica.md`.

  Nunca toque em `db/`, `futebol/`, `serie_b/`, `painel/`, `coleta/comum/`, `coleta/comum-europa/` nem nas pastas dos
  outros agentes (`bra-*`, `eng-1`, `por-1`...).
- **Banco só para leitura:** `sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)`. O teste de carga usa uma cópia
  (seção 5).
- **Git:**
  - nunca `git add -A` nem `git add .`: adicione só os seus caminhos;
  - **commit só com o ok explícito do Guilherme** (o agente 1 reclamou do `ba21d2a`, feito sem ok);
  - push só quando ele pedir;
  - não troque de ramo;
  - a mensagem de commit termina com `Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>`.
- **A pasta é compartilhada com os outros agentes:**
  - antes do `git add`, confira que `git diff --cached` está vazio;
  - em 21/11 o agente 2 commitou no mesmo instante, e os meus arquivos entraram no commit dele.
- **Logs e conferências vão para o scratchpad**, nunca soltos no repositório.
- **Nome de clube único no mundo:** confira na tabela `clube` do banco e nos `data/coleta/*/pacote/clubes.csv` antes de
  batizar. Homônimo leva a cidade (Barcelona de Guayaquil, Libertad de Loja, Nacional de Asunción, River Plate de
  Montevideo).
- **Critério nas dúvidas:** "o que for mais fiel à história". Pesquise em mais fontes quando divergem e registre a
  decisão com o motivo em `explicacoes.py` e no relatório.
- **Depois de toda importação ou correção:**
  - rode o `documentar.py` e atualize este arquivo;
  - os dois entram no mesmo commit da competição.
- **Fale com ele em português, curto e por partes.** Trabalhe sozinho, sem perguntar a cada passo; pergunte só as decisões
  que são dele.

## 2. O que está pronto

| Competição | Edições | Jogos | Clubes | Commit do pacote | No banco |
|---|---|---|---|---|---|
| `arg-1` Argentino | 197 (1891–2026 Ap.) | 43.726 | 173 | ba21d2a, 665fe93; correções 30f0b00, e698941 | sim (versão antes das correções) |
| `uru-1` Uruguaio | 126 (1900–2025) | 12.456 | 84 | 0ead727; correções 31c14b0 | sim (versão antes das correções) |
| `chi-1` Chileno | 109 (1933–2025) | 22.586 | 53 | 36e0690; correções 209641e, b8b5a57 | sim (versão antes das correções) |
| `col-1` Colombiano | 101 (1948–2025) | 22.512 | 42 | 3f5c1d0; correções b8d739d, d6bec05 | sim (versão antes das correções) |
| `par-1` Paraguaio | 134 (1906–2026 Ap.) | 7.823 | 50 | dc2b360, 9d1ca3b, 0b793ba; correções 4583f7e, a22c1ff | sim (versão antes das correções) |
| `per-1` Peruano | 109 (1912–2025) | 17.318 | 167 | 9d1ca3b, 0b793ba; correções 55c7066, 70d8caf | sim (versão antes das correções) |
| `ecu-1` Equatoriano | 68 (1957–2025) | 14.175 | 63 | 0b793ba; correções 4577457, cf612c6 | sim (versão antes das correções) |
| `bol-1` Boliviano | 94 (1950–2025) | 8.563 | 77 | 9ed3dcd | sim |
| `ven-1` Venezuelano | 106 (1921–2025) | 13.580 | 108 | 35dc0a2; leitor comum 415911b; cf612c6 | sim (versão de 22/11) |
| `uru-copa` Copa AUF Uruguay | 4 (2022–2025) | 221 | 100 | 1fe6d99 | não |
| `par-copa` Copa Paraguay | 7 (2018–2025, sem 2020) | 296 | 110 | e31a932 | não |
| `ecu-copa` Copa Ecuador | 5 (1970, 2018/19–2025) | 208 | 80 | e216792 | não |
| `col-copa` Copa Colombia | 21 (1950-51, 1952-53, 1956-57, 2008–2025) | 2.441 | 58 | 3683817 | não |
| `arg-copa` Copa Argentina | 15 (1969, 1970, 2011/12–2025; só a fase final) | 952 | 174 | 1dbc701 | não |
| `chi-copa` Copa Chile | 45 (1958–2025, com buracos) | 3.497 | 174 | 683177b | não |
| `ven-copa` Copa Venezuela | 66 (1932–2025, com buracos) | 1.397 | 161 | 025eb7f | não |

Os números de gols, cartões, conferência e cobertura estão no `README.md` da documentação. Com isso, as 1ªs divisões
da América do Sul estão todas coletadas (a do Brasil é de outros agentes).

## 3. De onde continuar (pendências, em ordem)

**Lista completa das pendências (levantada em 24/11 a pedido do Guilherme, para nada ficar para trás).** Os itens 1 a 6
abaixo são o histórico; o que está em aberto é esta lista.

- **A. Do agente 1 (banco e site):**
  - A1. Recarregar 7 ligas que estão no banco numa versão anterior às correções de 23-24/11: `uru-1`, `chi-1`, `col-1`,
    `par-1`, `per-1`, `ecu-1`, `ven-1` (jogos no banco x pacote em 24/11: uru 12.464 x 12.456, chi 22.601 x 22.586,
    col 22.788 x 23.418, par 7.865 x 7.823, per 17.316 x 17.318, ecu 14.195 x 14.175, ven 13.582 x 13.580). `arg-1`,
    `bol-1` e as 7 copas estão iguais. Pedido registrado em `docs/coleta/pedidos-sulamerica.md` (24/11).
  - A2. Opcional: recarregar `par-copa`, `ecu-copa`, `col-copa` e `chi-copa` (só a coluna `nomes_fonte` do `clubes.csv`).
- **B. Da revisão:**
  - B1. `docs/revisao/achados.csv` ainda marca "aberto" cerca de 190 ids da América do Sul já corrigidos (recados com os
    ids em `pedidos-sulamerica.md`). Reconferir depois da recarga (A1) e fechar. O arquivo é da revisão: não mexer.
  - B2. Nunca revisados: `bol-1`, `ven-1` e as 7 copas.
- **C. Decisões do Guilherme:**
  - C1. RESOLVIDA (24/11, "pesquise e veja o que acha"): o Atlético Zulia é o Unicol renomeado (páginas da RSSSF de
    1995/96 e 1996/97, Wikipédia em espanhol, ForoVinotinto; a ULA jogou o Torneo de Promoción de 1997 ao mesmo tempo).
    `clubes_ven.py`: Unicol e Atlético Zulia viram "Atlético Zulia" (Maracaibo); título de 1997/98 e vice de 1996/97
    saem da Universidad de Los Andes. `ven-1` e `ven-copa` reimportados.
  - C2. RESOLVIDA (24/11): a Bolívia fica de 1950 em diante, como está.
  - C3. RESOLVIDA (24/11, ok do Guilherme: fica como está, Galicia em 1970 e 66 edições; nota na observação da edição). Edições: 66; o anexo da Wikipédia e a lista da RSSSF contam as
    mesmas 66, e o "63" não aparece em nenhuma fonte. 1970: a RSSSF (jogos da final 2-0 e 1-1, tirados de três jornais de
    Caracas, e a lista de campeões) e a página do Deportivo Galicia na Wikipédia em inglês dão o Galicia; a Wikipédia em
    espanhol (lista, anexo, texto e palmarés do Galicia e do Deportivo Miranda) e a lista da Wikipédia em inglês dão o
    Deportivo Italia, com os mesmos placares e sem citar jogo. Decidido: fica como está (Galicia, pelos jogos), com a
    divergência registrada.
- **D. Trabalho do agente 4 (quando o Guilherme mandar):**
  - D1. FEITO (24/11), pesquisa de 3ª fonte:
    - QU-005: só River 1-0 Boca de 1945 tinha 3ª fonte (vai para 29/07); as outras 4 datas ficam e estão nas
      EXPLICACOES do arg-1.
    - CO-015: América 2-2 Once Caldas (2001) confirmado pela FutbolRed, fica; os "6 jogos com a ESPN" da revisão não têm
      lista e o relatório não mostra placar diferente da ESPN (pedir a lista à revisão, se ainda valer).
    - CO-004 (1966) e CO-006 (1986, 1988): sem fonte (Wikipédia baixada de novo, igual); nas EXPLICACOES do col-1.
    - CO-022: `esperados()` não soma de novo as fases quando a tabela é a do ano inteiro (1963, 1969-1979, 1988...) e o
      "o erro é desta tabela" só quando a outra tabela cobre os mesmos jogos (de 107 para 11); EXPLICACOES do col-1
      deixou de ser vazia.
  - D2. FEITA (24/11, ok do Guilherme): `rsssf_sul._continuacao` junta as linhas dos autores até o "]" (no máximo 3;
    sem o "]" não junta). +19.060 gols com autor nas 9 ligas; restam os "outros formatos" abaixo. Conferência de antes: O `rsssf_sul.ler` só guarda a 1ª linha dos autores
    ("[A 9, B 68;" e perde "   C 87]"); a conta não fecha com o placar e o jogo fica sem nenhum autor (texto em
    `partidas.gols_texto`). Nos pacotes das 9 ligas: 5.214 jogos com autores não separados, dos quais 3.766 com a lista
    cortada (texto termina em "," ";" ou "/"): arg 19, uru 998, chi 322, col 169, par 505, per 361, ecu 123, bol 1.187,
    ven 82. Correção: juntar as linhas de continuação no leitor comum (como o `_autores_inteiros` das copas) e reimportar
    as 9 ligas. Os outros 1.448 têm outros formatos (sem ";" entre os times, "53'", "og." etc.: arg 332, uru 76, chi 24,
    col 86, par 65, per 487, ecu 24, bol 335, ven 19).
  - D2b. "Outros formatos" de autores FEITOS em parte (24/11): +3.767 gols com autor; restam 688 jogos sem separar
    (arg 183, uru 125, per 105, col 88, bol 57, par 51, chi 34, ecu 25, ven 20), quase todos com nota ou duas colunas
    emendadas no texto, autor "?" ou formato único. Mudanças nos `autores.py`: `bol-1` (2ª leitura "G. Galindo 2" =
    quantidade; data grudada no fim; parêntese sem par), `per-1` (minuto "36´(pk)" sem vírgulas, "/" entre os times, gol
    contra do lado do time do jogador, notas grudadas), `arg-1` ("76' and 78' (p) Gancedo", "/" entre os times, divisão
    pelo placar quando as colunas vêm emendadas, `_pelo_placar`), `uru-1`, `par-1`, `ecu-1` ("/" entre os times).
  - D3. CONFERIDA (24/11): o formato "Alario 11m pen / Musto 26m" que o `coleta/arg-1/autores.py` não separa só aparece em
    3 jogos da liga (1906, 1961, 1963); entra junto com os "outros formatos" da D2.
  - D4. FEITA (24/11) no `bol-1` (27 linhas) e no `ven-1` (33 linhas): `classificacao()` põe no fim os clubes com jogos fora da tabela da fonte (mesma
    posição para a mesma fase). Era o pedido do agente 1 (22/11): classificação final de `bol-1` com todos os
    clubes com jogos em 1960, 1976, 1990, 1993 e 1994; talvez também nas edições incompletas do `ven-1`.
  - D5. Lacunas das copas que outra fonte (Wikipédia de cada edição) poderia fechar: Copa Chile 1984-1986 (parciais),
    2013/14, 2014/15 e 2015 (grupos só em tabela), 2022, 2023 e 2025 (página começa no mata-mata); Copa Ecuador 2024 e
    2025 e Copa Venezuela 2024 (só das oitavas); Copa Venezuela com 12 edições sem jogos; datas e cidades vazias.
  - D6. 2ªs divisões, na ordem do guia geral (seção 7), só quando o Guilherme pedir.
- **Ordem sugerida (24/11):** o Guilherme responde C1-C3 e avisa o agente 1 (A1); depois D2 e D3 (conferências de
  autores); depois D1, D4 e D5 conforme ele mandar; por último D6.


1. **Correções da revisão: FEITAS em 23/11** (`docs/revisao/plano-coleta-sulamerica.md`; um commit por liga, ids no fim
   de `docs/coleta/pedidos-sulamerica.md`): Argentino `30f0b00`, Uruguaio `31c14b0`, Chileno `209641e` (atenção: o leitor
   do Chile tinha `\b` virado backspace em três regex; corrigido), Colombiano `b8d739d`, Paraguaio `4583f7e`, Peruano
   `55c7066`, Equatoriano `4577457`. Leitor comum `415911b`: a data entre colchetes no título da fase ("Final [Dec 23]:")
   vale para os jogos de baixo (AR-023, UY-014, CH-012, CO-008, PY-009, PE-009, EC-009). O agente 1 ainda precisa
   recarregar as 9 ligas (o `ven-1` nunca foi carregado).
2. **Abertos da revisão (EM ANDAMENTO desde 23/11, ordem do Guilherme: "os abertos", sem perguntar):** uma liga por vez,
   com commit, push e recado: Equador, Peru, Paraguai, Chile, Argentina, Colômbia.
   - **Equador: feito (`cf612c6`)** (EC-013, EC-014). Junto: a regra "gol da ESPN sem lado não entra" (a do PY-020) foi para o
     `outras_fontes.py` de `ecu-1`, `chi-1`, `col-1`, `per-1` e `ven-1` (EC-013, CH-017, CO-018); a Venezuela foi
     reimportada no mesmo commit, e Chile, Colômbia e Peru entram com os seus.
   - **Peru: feito (`70d8caf`)** (PE-010, PE-012, PE-014, PE-015, PE-017, PE-022). Novo: `coleta/per-1/rebaixados_es.py`
     (seção "Ascensos y descensos" das páginas da es; `baixar_wikipedia.py` agora baixa todos os anos, "Liga1 <ano> (Perú)"
     de 2019 em diante).
   - **Abertos da revisão: FEITOS (24/11)**, fora os que esperam 3ª fonte (lista no fim de `pedidos-sulamerica.md`).
   - **Paraguai: feito (`a22c1ff`)** (PY-008, PY-012, PY-018, PY-019, PY-031). Novo: `coleta/par-1/goleadores_es.py`
     (coluna "Goleador" da es, guardada em `data/coleta/par-1/wikipedia/es_principal.txt`) e `explicacoes.REBAIXADOS`.
     Torneios (Apertura e Clausura) ligados no leitor só de 1996 a 2007 (`ANOS_TORNEIOS`).
   - **Chile: feito (`b8b5a57`)** (CH-006, CH-014 de 1986, CH-017, CH-022, CH-023, CH-028). Novo no `importar.py`:
     `_pontos_ultima_fase` (ordem pela fase final de pontos; `PONTOS_ACUMULADOS` = 1946 e 1951) e `acerta_grupos`; no
     `outras_fontes.py`: `OGOL_FORA` e o casamento sem data com placar igual quando o par se repete.
   - **Argentina: feito (`e698941`)** (AR-020, AR-021, QU-003; QU-005 aberto sem 3ª fonte). Novo:
     `coleta/arg-1/rebaixados_es.py` (anexo "Movilidad interdivisional" da es), `FASE_PELA_TABELA`, `FORA_DA_TABELA` e o
     3º passo da ESPN (jogo adiado, `adiado`) no `outras_fontes.py`.
   - **Colômbia: feito (`d6bec05`)**: CO-004, CO-006 (1976, 1989), CO-009, CO-012, CO-013, CO-015 (1948-1949),
     CO-016, CO-017, CO-018, CO-020. Abertos: CO-006 (1986, 1988), CO-004 (1966), CO-015 (2001-2018), CO-022. Novo:
     `goleadores_es.py`, `bonus_fase_final()`, `acerta_grupos()`, `ler_rsssf.cruzada()` (tabela de confrontos) e, no
     `wikipedia_jogos.py`, `ANOS_LISTAS`/`ANOS_TEXTO` (formatos de lista só nesses anos). ATENÇÃO: a chave do CORRIGE para
     jogo da Wikipédia é "wiki-es_<ano>:<linha>" (com hífen); "wiki:es_" nunca casou (corrigido no col-1 e no uru-1).
   - O detalhe de cada id está em `docs/revisao/achados.csv`; o que não tiver fonte fica registrado em `explicacoes.py`.
3. **Copas nacionais: FEITAS em 24/11 (decisões do Guilherme em `copas-nacionais.md`):** as sete (ARG, URU, CHI,
   COL, PAR, ECU, VEN), contagem da Wikipédia, das menores às maiores: Uruguai (FEITO, `uru-copa`), Paraguai (FEITO, `par-copa`), Equador (FEITO, `ecu-copa`),
   Colômbia (FEITO, `col-copa`), Argentina (FEITO, `arg-copa`), Chile (FEITO, `chi-copa`), Venezuela (FEITO, `ven-copa`). Slug `<país>-copa`. Importador comum: `coleta/comum-sulamerica/copa_rsssf.py`;
   cada copa só configura edições (página e trecho da RSSSF), fases, regiões e clubes (`clubes_copa.py`: regras da copa
   antes das da liga, nome inteiro, interior com a cidade). Não entra no `documentar.py` (que é de liga): o relatório
   `docs/coleta/<slug>.md` sai do próprio importador. Ver também: o leitor comum perde a continuação do colchete dos
   autores ("[A 9, B 68;" + "   C 87]"); o importador das copas junta (`_autores_inteiros`); conferir se as ligas perdem
   autores por isso (pendência).
   - **Copa Argentina (`arg-copa`) FEITA em 24/11:** só a fase final (decisão do Guilherme); 1969 e 1970 inteiras.
     Trechos e títulos de fase por página em `coleta/arg-copa/importar.py` (`TRECHOS`, `F_PAG`); homônimos desfeitos em
     `coleta/arg-copa/clubes_copa.py` (o ano das regras é o `ano_inicio` da edição: 2018/19 = 2018). O importador comum
     ganhou `anos_leitura` (datar 2019/20, que vai de fev/2020 a dez/2021) e `Copa.trocas` (troca de texto antes de ler:
     "[Mar 18 We]" da arg2015). 1969 é lida em trechos (cada região volta a dezembro).
   - **Copa Chile (`chi-copa`) FEITA em 24/11:** tudo o que a RSSSF traz de cada uma das 45 edições. Formatos por época
     no docstring de `coleta/chi-copa/importar.py`: siglas de 1990-1996 (`SIGLAS` em `clubes_copa.py`, troca feita antes
     de ler; jogos suspensos juntados com a linha do placar), linhas "A-B 3-1" de 1984-1986, grupos de 1991-1995 tirados
     das tabelas finais (`_grupos`). O importador comum ganhou: `trocas` por edição (aceita função), fases por trecho
     (4º elemento do trecho), `campeao_fonte` (final empatada sem placar dos pênaltis, 1958), `campeao_tabela`
     (quadrangular final, 1982), `grupos_clubes` e `Copa.fases_pontos` (grupos sem tabela legível). As outras copas
     não mudaram (rodei de novo).
   - **Copa Venezuela (`ven-copa`) FEITA em 24/11. AS SETE COPAS ESTÃO PRONTAS.** Contagem do anexo da Wikipédia
     ("Anexo:Temporadas de la Copa Venezuela", em `data/coleta/ven-copa/wikipedia/`): 66 edições (a pesquisa de 23/11
     falava em 63). Campeão e vice da Wikipédia (`CAMPEOES` em `coleta/ven-copa/importar.py`) quando os jogos não decidem;
     12 edições sem jogos (só tabela ou sem página). 1995 pelas tabelas de confrontos (`_cruzadas_1995`, leitor do ven-1).
     O importador comum ganhou: `vice_fonte`, campeão e vice entram na classificação mesmo sem jogo, `final_desempate`
     (final com "Replay": decide o último jogo) e clube só de tabela publicada vai para o `clubes.csv` (nas outras copas
     só a coluna `nomes_fonte` mudou).
   - Antes de cada commit de copa, cruzar os nomes com TODOS os `data/coleta/*/pacote/clubes.csv` e rodar o
     `testar_carga.py` (que agora pega os clubes já carregados das outras confederações: "Hispano" era de Honduras).
4. **Por último: 2ªs divisões**, na ordem do guia geral, só quando o Guilherme pedir (seção 7). Pedido do agente 1 para o
   `bol-1` (22/11, "quando o Guilherme mandar revisar"): a classificação final de 1960, 1976, 1990, 1993 e 1994 com todos
   os clubes com jogos (eliminados com a posição da fase em que caíram), como no `bra-sp-2`; o mesmo pode valer para as
   edições incompletas do `ven-1`.
5. **Decisões em aberto:**
   - **Venezuela:** Atlético Zulia = Unicol (RESOLVIDA em 24/11, item C1 da lista do topo da seção 3).
   - **Bolívia:** escopo de 1950 em diante (liga de La Paz semiprofissional, Integrado, Mixto), como a Wikipédia e a
     contagem de 93 campeonatos da RSSSF; a contagem "84 títulos desde 1958" da RSSSF deixaria de fora 1950-1957.
6. **Ficar de olho em `docs/coleta/pedidos-sulamerica.md`:** respostas do agente 1 e pedidos novos da revisão.

## 4. Como fazer uma competição nova

Copie a pasta da competição mais parecida e adapte. A mais recente é `coleta/ven-1/` (ESPN com fase por data e sem corte por data, tabelas cruzadas com a diagonal
em branco, era amadora com a liga antes das copas). A mais completa em módulos é `coleta/ecu-1/`, que tem:
- tabela de confrontos;
- jogos da ESPN com fase por data;
- `espn_fases`;
- `_FIM` nos títulos.

Para anos que só a Wikipédia tem, veja também `coleta/per-1/`. Os dois foram copiados um do outro e têm os mesmos
módulos:

| Arquivo | O que faz |
|---|---|
| `edicoes.py` | `EDICOES`: uma `Edicao` por título; `trechos` = (página da RSSSF, linha inicial, final); `FIM_PADRAO` (título que encerra o trecho); `espn`/`espn_fases` (jogos que vêm da ESPN); `wiki` (ano com jogos da Wikipédia) |
| `baixar_rsssf.py`, `baixar_espn.py`, `baixar_wikipedia.py` (`baixar_ogol.py` nos mais antigos) | baixam para `data/coleta/<slug>/<fonte>/` |
| `ler_rsssf.py` | lê cada edição: `FASES` (título -> fase), `TORNEIOS` (Apertura/Clausura dentro do ano), `FECHA`, `confrontos()` (tabela de confrontos), `espn_jogos()`, `campeoes()`/`vices()` |
| `wikipedia_jogos.py` | jogos da Wikipédia em espanhol (matriz `match_X_Y`, `OneLegResult`, `{{Partido}}`) |
| `clubes_<pais>.py` | `CLUBES` (nome de exibição -> cidade, província) e `REGRAS` (regex sobre a chave do nome, nome, ano inicial, ano final) |
| `explicacoes.py` | `CONSERTA_TEXTO`, `CORRIGE`, `EXTRAS`, `TABELAS_FORA`, `EXPLICACOES`, sempre com o motivo |
| `conferir.py` | soma dos jogos x tabelas publicadas; `python coleta/<slug>/conferir.py [-v temporada]` |
| `outras_fontes.py` | casa os jogos com a ESPN (e o ogol): hora, estádio, público, gols com minuto, cartões |
| `autores.py` | separa os autores dos gols do texto da RSSSF |
| `campeoes_wiki.py` | lista de campeões da Wikipédia em inglês (segunda fonte do campeão e do vice) |
| `importar.py` | monta o pacote e o relatório |
| `ver.py` | mostra os jogos entre dois clubes numa edição, com a linha da página |

Código comum em `coleta/comum-sulamerica/`:

| Arquivo | O que faz |
|---|---|
| `rsssf_sul.py` | leitor genérico das páginas da RSSSF: `texto`, `ler`, `linha_tabela`, `_jogo`, `chave`. **Mudou? Reimporte as nove competições e compare os pacotes (`git diff --stat`)** |
| `baixar.py` | `pegar(url, destino, espera)`: download educado, com cache |
| `espn.py` | URL do placar diário e `resumir(evento)` |
| `ogol.py`, `wikipedia.py` | calendário do ogol; wikitexto pela API |
| `documentar.py` | gera `documentacao/` |
| `testar_carga.py` | teste de carga numa cópia do banco |

Passos:

1. **Fontes:**
   - lista de campeões e de artilheiros da RSSSF (`tablesX/<pais>champ.html`, `<pais>tops.html`) e as páginas por ano;
   - ESPN (`<pais>.1`): baixe já no começo, porque leva de 30 a 60 minutos. Rode anos separados em paralelo
     (`baixar_espn.py 2025 2024`);
   - Wikipédia en (lista de campeões);
   - Wikipédia es, para os anos sem jogos na RSSSF.
2. **`edicoes.py`:** uma edição por título, como na lista da RSSSF. Ache onde cada página passa para outra competição
   (Serie B, copa, regionais) e ponha em `FIM_PADRAO`.
3. **`ler_rsssf.py`:** rode `python coleta/<slug>/ler_rsssf.py` e veja as fases de cada edição. Um esqueleto da página
   (títulos, blocos de jogos e de tabelas) ajuda muito.
4. **`clubes_<pais>.py`:** todo nome de toda fonte precisa resolver (`conferir.py` mostra "sem nome"). Confira a unicidade
   (seção 1).
5. **`conferir.py`:** cada tabela publicada contra a soma dos jogos. Toda divergência:
   - vira correção com motivo em `explicacoes.py`; ou
   - é erro da própria página (um gol, um resultado), que o relatório explica sozinho.
6. **`importar.py`:**
   - troque os textos do relatório e o `competicao.json`;
   - confira que campeão e vice batem com a Wikipédia e que "jogos = jogos esperados".
7. **Teste de carga** (seção 5).
8. **Documentação e recado:** ponha a competição em `LIGAS`, `PAIS` e `PENDENCIAS` no `documentar.py`, rode-o, atualize
   este arquivo e escreva o recado em `pedidos-sulamerica.md`.
9. Peça o ok do commit.

## 5. Teste de carga

```
python coleta/comum-sulamerica/testar_carga.py <slug> <pasta temporária (o scratchpad)>
```

Deve terminar com `<slug>: N edições, N jogos, N clubes novos -> OK`. Em 22/11 ele achou dois erros que o `conferir.py`
não pega:
- **Peru:** clubes que só estão na classificação (1912-1921) e não estavam no `clubes.csv`;
- **Paraguai:** um clube sem regra que só aparece em tabela (8 de Diciembre, 1994).

## 6. Armadilhas já encontradas

**RSSSF (páginas por ano)**
- **Notas que quebram a linha.** Uma nota como "...qualified for / Octogonal Final." deixa "Octogonal Final." no começo
  da linha seguinte, e o leitor toma isso por título de fase. No `ecu-1`, título de fase de liga só vale se for a linha
  inteira (`_FIM`). O mesmo vale para `FECHA`.
- **Clube com nome de data** ("3 de Febrero", "12 de Octubre", "9 de Octubre"):
  - era lido como posição na tabela e como linha de data;
  - corrigido no `rsssf_sul.py` em 21/11;
  - nome em minúscula ("9 de octubre") ainda não é lido: corrija na página.
- **Siglas** ("U.T.C.", "A.D.T."): corrigido no `rsssf_sul.py` em 21/11.
- **Tabela de confrontos (`Cross-Table`):** mandante na linha, "xxx" na diagonal, linha sem nome = segundo turno do clube de
  cima, "0*2" = placar dado. Ver `ler_rsssf.confrontos` do `ecu-1`. Sem data nem rodada.
- **Jogo interrompido e completado depois:** aparece em duas linhas ("abd" e "[remaining 57']"). Descarte a primeira em
  `CORRIGE`.
- **Datas:** "First Leg [Dec 11]" não é lido como data. O jogo fica sem data, e o corte dos jogos da ESPN tem de ser por data
  explícita em `_ESPN`.
- **Títulos enganosos:**
  - "Championship Final:" que abre uma liguilla de pontos corridos (`ecu-1` 1999);
  - "Championship Playoff", que no Equador é a final;
  - desempate com "Round 1/2/3": o leitor comum volta à fase de liga a cada rodada (`ult` em `_torneios` do `ecu-1`);
  - "Finalización" começa com "Final": cuidado com `startswith("Final")` (`eh_mata` do `ecu-1`).
- **Erros de digitação:**
  - V+E+D diferente de J (a linha da tabela some);
  - clube trocado numa rodada (um clube duas vezes, outro nenhuma);
  - jogo sem placar com os autores dos gols.

  Corrija em `CONSERTA_TEXTO` com o motivo, conferindo com a tabela.
- **Páginas com outra competição no meio** (Sudamericana, Serie B, Copa Ecuador, Supercopa, regionais): use `FIM_PADRAO`
  ou `trechos` explícitos.
- **Acentos da página de código 437** ("Am‚rica", "Cat¢lica") e lixo na lista de artilheiros ("RODR-GUEZ", "P+REZ"):
  tradução em `ler_rsssf._CP437` e `importar._ACENTO_TOPS` do `ecu-1`.

**ESPN**
- **Cobertura:** começa em anos diferentes (Peru e Equador: 2005; 2001-2004 vazios) e tem buracos de lances (Equador
  2014-2020).
- **Fuso:** hora em UTC. Converta: Lima e Guayaquil UTC-5; Santiago e Assunção têm horário de verão (veja o
  `outras_fontes` de cada um).
- **Jogos que a RSSSF não tem:** a fase vem por data (`espn_fases`) ou pela tabela que tem os dois clubes (`"*"`).
- **W.O.:** traz como placar (Equador 2025, El Nacional x Delfín, 0-3) jogo que a RSSSF diz não disputado. Vale a RSSSF.

**ogol:** devolve a página de outra edição (confira o link canônico); para a Colômbia e para quase todo o Paraguai o calendário
vem vazio.

**Wikipédia:** a lista de campeões muda de página (o Equador está em "LigaPro Serie A", não em "List of ... champions");
siga o redirecionamento.

**Bolívia (22/11):**
- página de 2011/12 da RSSSF em UTF-16 (um caractere nulo entre as letras): `linhas()` tira os nulos;
- `bolhist.html` escreve os gols entre parênteses ("(40-32)");
- ida e volta numa linha só ("Oriente Petrolero  1-0 0-4 Bolívar"): `_IDA_VOLTA` em `ler_rsssf` vira dois jogos;
- tabela de confrontos com as siglas na mesma linha do título ("Crosstable  Bol Des Wil") e "XXX" maiúsculo;
- "awarded to X (originally 0-0)" é vitória dada; "points awarded to X" a RSSSF às vezes não conta na tabela (2007);
- a página "Copa Simón Bolívar <ano>" da Wikipédia em espanhol é de outro torneio (Colômbia x Venezuela);
- edição que já é um torneio ("2004 Clausura"): o título do torneio na página não vira fase (`tor = {}` em `ler`);
- "Liguilla" não pode encerrar o torneio (em 2024 era o mata-mata do Apertura); "Final" sozinho encerra (final do ano).

**Venezuela (22/11):**
- era amadora: a página traz a liga (às vezes só o campeão) e depois copas (Copa Venezuela, Copa IND, Copa del Distrito
  Federal); o trecho da liga acaba no primeiro título "Copa ..." mesmo sem jogo antes (`ler` do `ven-1`);
- "bt" / "lt" = venceu / perdeu sem placar (viram W.O.); "drw" = empate sem placar (fica de fora); "1-0 awd X" (1967) =
  placar dado antes do "awd";
- "Championship Playoff" é grupo final quando vem com "Final Table" (1968-1984, 1999/00, 2022, 2023) e final quando não;
  "Championhip" (sem s) é erro de digitação da página;
- "Liguilla (Cuadrangulares)" seguida de "Grupo A": o leitor comum volta à fase de grupos depois de "Fase final"; use
  "Liguillas" como nome da fase;
- tabela cruzada sem "xxx" (diagonal em branco, 1995/96): `linhas()` põe o "xxx";
- o mesmo nome em duas fases do ano é clube diferente ("Monagas" na Copa Venezuela 2000 = Atlético Monagas; no Torneo
  Nacional 2001 = Monagas SC): troque o nome na página, em `linhas()`;
- ESPN com placar absurdo (2011, "15-0"): a tabela final da RSSSF mostra o certo; corrija em `CORRIGE`;
- jogos da ESPN somados aos da página: em vez do corte por data, sai da ESPN só o jogo que a página já tem (mesmo par
  até 3 dias de diferença);
- artilheiro com dois clubes ("Estudiantes/Carabobo FC"): fica o último, os dois na fonte (o teste de carga pegou).

**Correções da revisão (23/11):**
- **Pódio oficial:** `campeoes_wiki.py` do `arg-1` lê campeão, vice e 3º da lista da Wikipédia em inglês; `importar.podio_oficial()`
  põe vice e 3º nas posições 2 e 3 (1891 fica como está: título dividido).
- **Tabela publicada como classificação** quando os jogos não fecham (W.O., punições, derrota para os dois clubes):
  `importar.TABELA_OFICIAL` do `arg-1`. Com só parte dos jogos, a tabela completa parece "acumulada" para a conferência:
  não filtre por isso.
- **Ano das datas:** `importar.acerta_ano()` do `arg-1` (janela da temporada; regra simulada pela revisão em
  `revisao/QU/sim_ano.py`) e `DATA_FIXA` para o ano escrito na própria linha.
- **Página com um `<PRE>` por linha** (arg26): o texto puro junta tudo numa linha. `ler_rsssf.PRE_POR_LINHA` quebra por
  `</PRE>`. Muda os números de linha da página: refaça trechos e correções dela.
- **Resumo no topo da página** com títulos de fase ("Playoff:", "Torneo por el Descenso"): o título vale para os jogos de
  baixo. Corte o resumo do trecho ou anule o título só nessa edição (`_FASES_EXTRA` do `arg-1`).

**Python no Windows:** editar arquivo por heredoc com `python - <<'EOF'` estraga `\b` (vira backspace) e às vezes `\n`. Para
regex, use o Edit e confira com `grep -c $'\x08'`. Em f-string com `rf"..."`, `\d{1,2}` vira tupla: use `{{1,2}}`.

## 7. Decisões do Guilherme já tomadas

- Uma edição por título de campeão, como na lista da RSSSF; Apertura e Clausura que dão título são edições separadas.
- Argentino: "2025 Liga" (tabela anual) entra como edição sem jogos; Hurlingham (1891) no cadastro.
- Uruguaio: C.U.R.C.C. = Peñarol (mantido em 21/11, depois de pesquisa mostrar que é disputado).
- Paraguaio: anos sem jogos entram como edição com campeão, vice e tabela parcial (posição e pontos) quando houver; os
  jogos soltos ("Known Results") ficam de fora.
- Peruano: 1912-1921 como edições só com campeão e vice (escolha recomendada aprovada em 21/11).
- 22/11: prioridade é coletar (Bolívia, depois Venezuela); a revisão do Argentino e do Uruguaio espera o plano da revisão.
- 22/11: depois da Venezuela, as 2ªs divisões, na ordem do guia geral, quando ele pedir.
- 23/11: primeiro as correções da revisão; depois as copas nacionais (documentadas em `copas-nacionais.md`); depois as 2ªs divisões.
- Não começar outra competição sem ele pedir.
