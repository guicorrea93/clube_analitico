# Coleta Ásia — comece aqui

Para o agente de coleta da Ásia (países da AFC, inclusive a Austrália) e para quem for continuar este trabalho. Leia
antes o guia geral `docs/agentes-internacionais-COMECE-AQUI.md`, com o formato do pacote, as pastas de cada agente e as
regras de identidade dos clubes. Este arquivo diz o que já foi feito, como foi feito e de onde continuar.

Última atualização: 23/11/2026 (Japão pronto, esperando o ok do commit).

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
| `jpn-1` Japonês | 60 (1965–2025) | 12.190 | 40 | (esperando o ok) | não |

**Pasta comum (23/11):** cópia de `coleta/comum-sulamerica/` (ver seção 4). O `rsssf_asia.py` ainda não foi usado: o
Japão tem leitor próprio (`coleta/jpn-1/ler_jsl.py`), porque a JSL é só tabela final e tabela de confrontos.

## 3. De onde continuar

1. **Japão (`jpn-1`): pronto em 23/11**, esperando o ok do commit do Guilherme. Recado de fim de coleta no fim de
   `docs/coleta/pedidos-asia.md`. Pendências na lista `PENDENCIAS` do `documentar.py`.
2. Próxima: Coreia do Sul (`kor-1`), depois de mandar ao Guilherme as decisões de escopo. Depois, na ordem sugerida: `ksa-1`, `irn-1`, `aus-1`, `chn-1`, `qat-1`, `uae-1`, `uzb-1`, `irq-1`, `ind-1`,
   `tha-1`; depois as outras 1ªs divisões da AFC.

**Decisões de escopo já conhecidas (perguntar antes da liga):**
- **China:** o campeonato nacional desde 1951 ou só desde a Jia-A (1994)?
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

**Python no Windows:** editar arquivo por heredoc com `python - <<'EOF'` estraga `\b` e às vezes `\n`. Para regex, use o
Edit e confira com `grep -c $'\x08'`.

## 7. Decisões do Guilherme já tomadas

- 23/11, Japão: a JSL (1965-1991/92) entra antes da J1; clube de empresa = clube atual da J.League (Yokohama Flügels
  separado); nos anos de turnos o campeão é o da final, e os turnos são fases.
- Repescagem contra a 2ª divisão fica de fora (decisão do agente, seguindo o Alemão).
