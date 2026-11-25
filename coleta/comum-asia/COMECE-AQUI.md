# Coleta Ásia — comece aqui

Para o agente de coleta da Ásia (países da AFC, inclusive a Austrália) e para quem for continuar este trabalho. Leia
antes o guia geral `docs/agentes-internacionais-COMECE-AQUI.md`, com o formato do pacote, as pastas de cada agente e as
regras de identidade dos clubes. Este arquivo diz o que já foi feito, como foi feito e de onde continuar.

Última atualização: 25/11/2026 (Arábia Saudita commitada, 204e7d6d).

**Documentação completa:** `coleta/comum-asia/documentacao/`, gerada por `python coleta/comum-asia/documentar.py` a partir
dos pacotes, do código e dos relatórios (uma ficha por competição e o índice `README.md`). Rode depois de toda
importação ou correção e mantenha à mão só as listas `LIGAS`, `PAIS` e `PENDENCIAS`, no começo do script. Os relatórios
`docs/coleta/<slug>.md` têm o detalhe edição a edição.

## 1. Regras da casa (combinadas com o Guilherme)

- **Uma competição por vez.** Antes de cada liga, mande ao Guilherme, em poucas linhas, as decisões de escopo.
- **Ao fim de cada liga:**
  - resumo curto e pedido de ok para o commit;
  - **recado de fim de coleta:** seção "Recado de fim de coleta — <slug> — <data>" no fim de `docs/coleta/pedidos-asia.md`,
    para o agente 1 (banco e painel) e para o agente de revisão, e o mesmo texto ao Guilherme, num bloco de código. Os 8
    itens da seção 10 do guia geral:
    1. o que foi feito: edições, jogos, clubes, gols com autor, cartões e fontes;
    2. commits;
    3. resultado do teste de carga;
    4. pedidos ao banco e ao painel: o que carregar, formatos novos, colunas vazias, casos especiais;
    5. decisões tomadas (com o motivo) e as que esperam o Guilherme;
    6. o que não deu para coletar e as pendências, com a fonte que poderia resolver;
    7. onde a revisão deve olhar primeiro;
    8. próxima competição.
  - **liste os países novos** (para o agente 1 baixar as bandeiras).
- **Mexa só nas suas pastas:**
  - `coleta/<slug>/` e `coleta/comum-asia/`;
  - `data/coleta/<slug>/`, `data/cache/*-asia*/` e `data/cache/ogol-<slug>/`;
  - `docs/coleta/<slug>.md` e `docs/coleta/pedidos-asia.md`.

  Nunca toque em `db/`, `futebol/`, `painel/`, `coleta/comum*/` dos outros nem nas pastas das ligas dos outros agentes.
  Não importe código da pasta de outro agente: copie para cá.
- **Banco só para leitura:** `sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)`. O teste de carga usa uma cópia.
- **Git:** nunca `git add -A` nem `git add .`; antes do `git add`, confira que `git diff --cached` está vazio (a pasta é
  compartilhada); commit só com o ok explícito do Guilherme; push só quando ele pedir; não troque de ramo; a mensagem
  termina com `Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>`.
- **Logs e conferências vão para o scratchpad**, nunca soltos no repositório.
- **Critério nas dúvidas:** o que for mais fiel à história e ao que a federação do país reconhece. Registre a decisão com
  o motivo em `explicacoes.py` e no relatório.
- **Fale com ele em português, curto e por partes.** Trabalhe sozinho; pergunte só as decisões que são dele.

## 2. O que está pronto

| Competição | Edições | Jogos | Clubes | Commit do pacote | No banco |
|---|---|---|---|---|---|
| `jpn-1` Japonês | 60 (1965–2025) | 12.190 | 40 | 71d5006 (no GitHub) | sim |
| `kor-1` Sul-Coreano | 43 (1983–2025) | 7.163 | 25 | e04507f (no GitHub) | não |
| `ksa-1` Saudita | 69 (1957/58–2025/26) | 5.965 | 43 | 204e7d6d (sem push) | não |

**Pasta comum (23/11):** cópia de `coleta/comum-sulamerica/` (ver seção 4). O `rsssf_asia.py` ainda não foi usado: o
Japão tem leitor próprio (`coleta/jpn-1/ler_jsl.py`), porque a JSL é só tabela final e tabela de confrontos.

## 3. De onde continuar

1. **Japão (`jpn-1`): pronto e no GitHub (`71d5006`, 24/11)** e já no banco. Recado de fim de coleta no fim de
   `docs/coleta/pedidos-asia.md`. Pendências na lista `PENDENCIAS` do `documentar.py`.
2. **Coreia do Sul (`kor-1`): pronta e commitada em 24/11 (`e04507f`, no GitHub)**; falta o agente 1 carregar. Recado de
   fim de coleta no fim de `docs/coleta/pedidos-asia.md`; pendências na lista `PENDENCIAS` do `documentar.py`.
3. **Arábia Saudita (`ksa-1`): pronta e commitada em 25/11 (`204e7d6d`, sem push)**; falta o agente 1 carregar. Recado no fim de
   `docs/coleta/pedidos-asia.md`; pendências no `PENDENCIAS` do `documentar.py`.
4. Próxima: Irã (`irn-1`), depois das decisões de escopo do Guilherme. Depois, na ordem sugerida:
   `aus-1`, `chn-1`, `qat-1`, `uae-1`, `uzb-1`, `irq-1`, `ind-1`, `tha-1`; depois as outras 1ªs divisões da AFC.

**Como a Arábia Saudita foi feita (`coleta/ksa-1/`), bom modelo para liga só com RSSSF + ogol + ESPN:**

| Arquivo | O que faz |
|---|---|
| `baixar_rsssf.py`, `baixar_ogol.py`, `baixar_espn.py`, `baixar_wikipedia.py` | fontes (RSSSF `sauNN.html` e `saucuphist.html`; ogol `liga-saudita` 1999/00+; ESPN `ksa.1` 2022/23+; Wikipédia `Saudi_Pro_League`) |
| `ler_rsssf.py` | página da RSSSF: tabelas (completa, só jogos e pontos, só ordem), jogos (com ida e volta numa linha e `awd`), autores, seções (separa as copas) |
| `fontes.py` | jogos e tabelas de cada fonte já com o nome do clube; tira a tabela do meio do campeonato e as repetidas; aplica `OGOL_CORRIGE` |
| `clubes_ksa.py`, `campeoes_wiki.py`, `edicoes.py`, `explicacoes.py` | clubes; lista oficial de campeões (69 temporadas); eras e fases do playoff; correções com prova |
| `importar.py`, `relatorio.py` | pacote, conferência (tabela da RSSSF, RSSSF x ogol, ESPN) e relatório |

**Coreia do Sul (`kor-1`): escopo decidido pelo agente em 24/11** (o Guilherme pediu que o agente pesquisasse e decidisse):
- **K League (1ª divisão profissional) de 1983 a 2025.** A liga semiprofissional (1964-2002) fica de fora: torneio de uma
  semana em grupos e final, títulos divididos, quase sem dados; a K League e a RSSSF contam os títulos desde 1983.
- **2026 entra quando acabar** (em 24/11 faltavam 12 jogos; a Wikipédia já dá o FC Seoul campeão).
- **Clubes: um por código do portal oficial** (K01...), o mesmo nas mudanças de nome e cidade (Yukong/Bucheon SK = Jeju
  United, K04; Daewoo = Busan IPark; Lucky-Goldstar/LG = FC Seoul; Ilhwa = Seongnam FC). Os times do Exército têm códigos
  diferentes e ficam separados (Sangmu 1985 K24, Gwangju Sangmu K14, Sangju Sangmu K23, Gimcheon Sangmu K35).
- **Campeão oficial** (final ou playoff quando houve); de 2012 em diante a divisão em grupos fica numa fase só "Liga",
  como no Escocês. Fora: copa da liga, repescagem contra a K League 2.

**Como a Coreia foi feita (`coleta/kor-1/`), bom modelo para liga com portal oficial de boletins:**

| Arquivo | O que faz |
|---|---|
| `baixar_portal.py` | portal.kleague.com (convidado): calendário (até 2012), lista oficial (2013+, www.kleague.com `getScheduleList.do`, com fase e rodada) e boletim de cada jogo (cache comprimido em `data/cache/kleague-asia/jogos/`). O portal aguenta várias filas: com 8-12 filas (anos diferentes, `--reverso`) foram ~85 boletins por minuto |
| `baixar_oficial.py` | API do site oficial (`matchInfo.do`, 2013+; 500 antes), em coreano e inglês (língua pela sessão, `/changeLang.do`): conferência do placar e nome em inglês dos jogadores |
| `baixar_tabelas.py` | classificação final oficial (`teamRank.do`, 2003-2025; antes vem vazia) |
| `baixar_rsssf.py`, `baixar_ogol.py`, `baixar_wikipedia.py` | fontes de apoio (RSSSF: `skorhist.html` com as tabelas 1983-2009 e as páginas de cada ano; ogol 2008-2025; Wikipédia: campeões e artilheiros) |
| `competicoes.py` | o que é a 1ª divisão no portal: `meet_seq` 1 de cada ano e as finais de 1984, 1986, 1995 e 1996 |
| `ler_portal.py` | boletim: dados do jogo, gols (minuto, pênalti, gol contra), cartões, disputa de pênaltis |
| `ler_oficial.py`, `ler_rsssf.py` | API oficial; jogos, autores e tabelas da RSSSF |
| `clubes_kor.py`, `nomes_kor.py` | identidade dos clubes; nome dos jogadores (romanização, grafia oficial em inglês, nome de jogo dos estrangeiros) |
| `edicoes.py`, `campeoes_wiki.py`, `explicacoes.py` | fases e pontos de cada época; campeão, vice e artilheiro da Wikipédia; casos especiais com prova (`WO`, `AWD`, `GOL_FALTANDO`, `SORTEIO`, `TABELA_RSSSF`, `OBS_CLASSIFICACAO`) |
| `importar.py`, `relatorio.py` | pacote, conferência e relatório |

**Decisões de escopo já conhecidas (perguntar antes da liga):**
- **China:** o campeonato nacional desde 1951 ou só desde a Jia-A (1994)?
- **Japão, 2026:** a J.League passou ao calendário europeu (2026/27) e jogou um torneio especial no 1º semestre de 2026
  ("100 Year Vision League"): ver se conta como título antes de pôr 2026 no `jpn-1`.
- **Irã:** Takht Jamshid (1973-1978), Azadegan e IPL; os anos sem campeonato entram como edição sem campeão.
- **Austrália:** o campeão é o da Grand Final (o oficial) e o 1º da fase de liga fica na observação? NSL (1977-2004)
  mais A-League?
- **Índia:** I-League e ISL conviveram como 1ª divisão (2014-2022): qual vale em cada ano?

## 4. Código comum (`coleta/comum-asia/`)

Copiado de `coleta/comum-sulamerica/` em 23/11/2026.

| Arquivo | O que faz |
|---|---|
| `rsssf_asia.py` | leitor genérico das páginas da RSSSF: `texto`, `ler`, `linha_tabela`, `_jogo`, `chave` (cópia do `rsssf_sul.py`). **Mudou? Reimporte as ligas já prontas e compare os pacotes (`git diff --stat`)** |
| `baixar.py` | `pegar(url, destino, espera)`: download educado, com cache e tratamento do 429 |
| `espn.py` | URL do placar diário e `resumir(evento)` |
| `ogol.py`, `wikipedia.py` | calendário do ogol; wikitexto pela API |
| `documentar.py` | gera `documentacao/` (listas `LIGAS`, `PAIS`, `PENDENCIAS` no começo) |
| `testar_carga.py` | teste de carga numa cópia do banco |

**Teste de carga** antes de todo commit:

```
python coleta/comum-asia/testar_carga.py <slug> <scratchpad>
```

Deve terminar com `<slug>: N edições, N jogos, N clubes novos -> OK`.

**Como fazer uma competição nova:** o passo a passo e os módulos de cada liga (`edicoes.py`, `ler_rsssf.py`,
`clubes_<pais>.py`, `explicacoes.py`, `conferir.py`, `outras_fontes.py`, `autores.py`, `campeoes_wiki.py`,
`importar.py`, `ver.py`) estão em `coleta/comum-sulamerica/COMECE-AQUI.md`, seção 4. O modelo mais recente da América do
Sul é `coleta/ven-1/`. Copie para `coleta/<slug>/` e troque o `sys.path` para `comum-asia`.

**Como o Japão foi feito (`coleta/jpn-1/`), bom modelo para liga com site oficial de dados:**

| Arquivo | O que faz |
|---|---|
| `baixar_rsssf.py`, `baixar_wikipedia.py`, `baixar_espn.py`, `baixar_ogol.py` | fontes de apoio |
| `baixar_jleague.py` | J.League Data Site: lista de jogos por ano e página de cada jogo (cache comprimido em `data/cache/jleague-asia/`; `--reverso` abre outra fila: o site leva ~2,4 s por página, as 9.759 levaram ~4 h com 8 filas) |
| `baixar_tabelas_jleague.py` | tabelas oficiais de cada turno e a anual |
| `ler_jsl.py` | JSL na RSSSF: tabela final, tabela de confrontos (dois formatos), rodadas de 1988/89, artilheiros |
| `ler_jleague.py` | página do jogo: placar por tempo, pênaltis, autores com minuto, cartões, árbitro, público |
| `clubes_jpn.py` | identidade dos clubes (clube de empresa da JSL = clube da J.League) |
| `edicoes.py` | as 60 edições e as regras de pontos de cada época |
| `campeoes_wiki.py` | campeão, vice, 3º e artilheiro da lista de campeões da Wikipédia |
| `explicacoes.py` | `CONSERTA_JSL`, `AWD`, `ARTILHEIRO_GOLS`, `EXPLICACOES` |
| `importar.py`, `relatorio.py` | pacote, conferência (tabelas oficiais, ESPN, ogol) e relatório |

## 5. Nomes de clube

- **Únicos no mundo:** confira na tabela `clube` do banco e nos `data/coleta/*/pacote/clubes.csv` antes de batizar.
  Homônimo leva a cidade.
- **Nomes árabes** (combinado com o agente da África, 23/11):
  - sempre com hífen;
  - ficam com o nome puro: Al-Hilal, Al-Ittihad, Al-Nassr e Al-Shabab (Arábia Saudita) e Al-Ahly (Egito, da África);
  - os outros levam a cidade: "Al-Ahli de Jeddah", "Al-Ahli de Doha", "Al-Nasr de Dubai", "Al-Wahda de Abu Dhabi".
- **Clube de outro país numa liga da AFC:** entra com o país dele. Wellington Phoenix e Auckland FC jogam a A-League
  com país `NZL`; o agente da Oceania usa o mesmo nome, e o banco junta os dois.
- **Clube que mudou de nome** (Toyo Kogyo → Sanfrecce Hiroshima, Yomiuri → Verdy): um cadastro, com o nome atual; os
  antigos no `nomes_fonte`.

## 6. Armadilhas já encontradas

**RSSSF**
- **Páginas em UTF-16** (um caractere nulo entre as letras; começam com `ÿþ`): `jap92.html`, `jap94.html` e outras.
  A Bolívia já teve isso: `linhas()` tem de tirar os nulos (ou decodificar como `utf-16`).
- **JSL (1965-1991/92):** tabela final + tabela de confrontos (`Cross-Table`, mandante na linha, "x" na diagonal), sem
  data nem rodada. A mesma página traz depois a JSL2, a Copa do Imperador e outras copas: corte o trecho.
- **J-League 1993-1998:** sem empate. Na tabela de resultados, "1-0" = no tempo normal, "1=0" = na prorrogação
  (morte súbita), placar igual = pênaltis, com ">" (vitória do mandante) ou "<". Os pontos por vitória mudam por
  tipo de vitória: a classificação vem da tabela publicada, e o relatório explica.

- **JSL 1966, 1971 e 1973:** a tabela de confrontos não fecha com a tabela final (1 a 4 gols num confronto, duas células
  possíveis): explicado, sem correção.
- **JSL 1977-1979:** empate decidido nos pênaltis (4/2/1 pontos); a página não diz quem ganhou cada disputa.
- **JSL 1988/89:** a lista de rodadas tem um jogo com o mando invertido; vale a tabela de confrontos.
- **1985/86:** um placar com travessão (byte 0x97) no lugar do hífen.

**J.League (1993-2025)**
- Pontos de cada época, tirados das tabelas oficiais (e não da memória): 1993-94 sem pontos; 1995-96 vitória 3 (também
  nos pênaltis) e **derrota nos pênaltis 1**; 1997-98 3/2/1 (normal, prorrogação, pênaltis); 1999-2002 3/2/1 (normal,
  prorrogação, empate); 2003+ 3/1/0.
- A página do jogo: "Own-Goal" sem nome; acréscimo "90'+2"; cartão com minuto "***" (desconhecido). Não marca pênalti.
- O mesmo jogador com dois nomes ("Otze" e "Ordenewitz", 1994): artilheiro pela lista oficial, não pela soma por nome.
- Lista de campeões da Wikipédia: Will 2001 com 20 gols (são 24); 2020 e 2021 com o artilheiro na mesma linha do pódio.
- 2021, Urawa x Shonan: 2-3 em campo, 0-3 oficial (`AWD`).
- Siglas da lista: "Yokahama M"/"Yokahama F" (com erro de grafia), "F-Tokyo", "V-Kawasaki"...

**ESPN**
- `jpn.1` tem jogos desde 2006; tem placares parciais (9 jogos de 2009-2014 com menos gols): só conferência. Hora em UTC
  (Japão: UTC+9, sem horário de verão).

**ogol:** a J1 é `liga-japonesa`; não tem os jogos de 1997 a 2003; em 1996 soma os pênaltis ao placar; algumas páginas
vêm trocadas (rodar de novo o ano).

**K League (portal e site oficial):**
- O total de gols do boletim (`H_Goal_Qty`) **nunca conta o gol contra**; o lance do gol contra tem o `Team_Id` do clube
  que ganhou o gol. O placar é a soma dos lances; quando não bate com o total + gols contra, decide outra fonte.
- Alguns boletins têm gols a menos (o total certo) ou a mais; jogos W.O. aparecem 0-0 sem lances, público nem árbitro
  (1987: Hyundai; 2012: Sangju, 14 jogos); jogo decidido fora de campo fica com o placar de campo (1996, 2021).
- Tipos de lance: G gol, Y amarelo, R vermelho, Z segundo amarelo (expulsão), C substituição, P não é gol. Cartão sem
  número de camisa é de técnico/comissão.
- Disputa de pênaltis: blocos com `Name`/`Gain_YN`, o 1º é o mandante; às vezes só as 5 primeiras de cada lado (1998:
  5-5 decidido no sorteio, sem refletores).
- O calendário do portal esconde jogos nos dias cheios de 2013 em diante: use a lista do site oficial.
- A tabela oficial (`teamRank.do`, 2003+) conta os jogos do playoff (2003-2011), mas os pontos só da liga.
- A K League conta o artilheiro só na liga (sem playoff), com desempate pelo número de jogos.
- A RSSSF da Coreia mistura outras ligas (N-League, K3) com nomes de cidade: ligar nomes só com votos firmes.
- Nomes dos estrangeiros: o hangul é o nome de jogo; o inglês do site é o nome civil completo. Apelido que não está no
  nome civil vai à mão em `nomes_kor.NOME_DE_JOGO`.
- `python -I` tira a pasta do script do `sys.path`: os scripts põem `AQUI` no `sys.path` à mão.

**Liga saudita (RSSSF, ogol, ESPN):**
- A página da RSSSF repete a tabela final no fim e traz a do meio do campeonato ("Halfway Table"): use só uma.
- Jogo decidido fora de campo aparece como "Urooba  awd Nasr  [awarded 0-3, originally 2-1; ...]", às vezes com o
  motivo na linha de baixo misturado com a coluna ao lado; o ogol traz o placar de campo.
- A RSSSF de 2025/26 chama o Neom de "Al-Nojoom"; a de 1990s escreve "Al Hilal" sem hífen.
- O ogol põe jogos do playoff como rodadas a mais (R23-R25) e tem erros de mando/placar (corrigidos em
  `OGOL_CORRIGE`, com a matriz de resultados da Wikipédia como prova).
- Na ESPN o gol contra já vem do lado do time que ganhou o gol (não inverter). A ESPN pôs um amistoso (Al-Raed x
  Al-Wehdat, 2022) na liga.
- Temporada saudita vai de agosto a julho (há finais em julho).

**Python no Windows:** editar arquivo por heredoc com `python - <<'EOF'` estraga `\b` e às vezes `\n`. Para regex, use o
Edit e confira com `grep -c $'\x08'`.

## 7. Decisões do Guilherme já tomadas

- 23/11, Japão: a JSL (1965-1991/92) entra antes da J1; clube de empresa = clube atual da J.League (Yokohama Flügels
  separado); nos anos de turnos o campeão é o da final, e os turnos são fases.
- Repescagem contra a 2ª divisão fica de fora (decisão do agente, seguindo o Alemão).
- 24/11, Coreia: o Guilherme pediu que o agente pesquisasse e decidisse o escopo ("faça uma pesquisa mais a fundo para
  julgar o que é necessário"). Decidido: K League 1983-2025 (sem a semiprofissional), clube por código do portal (os
  Sangmu separados), campeão oficial, divisão em grupos numa fase só, 2026 quando acabar (seção 3).
- 24/11, Arábia Saudita: **desde 1957/58**, como o relatório oficial da federação (2025: Al-Hilal 21 títulos; Arab News,
  Saudi Gazette). A "His Majesty's League" (1957-1974, campeões iguais aos da antiga Copa do Rei, mata-mata) entra com
  campeão e vice, com os jogos que houver. Do agente: até 2025/26; temporadas canceladas ou não concluídas (1966/67,
  1967/68, 1969/70, 1975/76) como edição sem campeão; 1990/91-2006/07 campeão do quadrangular final ("Golden Box");
  temporadas sem jogos só com a tabela final. Fontes: RSSSF (`sauNN.html`, jogos com autores de 1999/00 em diante),
  ogol (`liga-saudita`, jogos de 1999/00 em diante), ESPN (`ksa.1`, 2022/23 em diante).
