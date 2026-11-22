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
  - recado ao agente do banco no fim de `docs/coleta/pedidos-sulamerica.md`. Ele gosta de recebê-lo também num bloco de
    código, para copiar.
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
| `arg-1` Argentino | 196 (1891–2025) | 43.235 | 171 | ba21d2a, 665fe93 | sim |
| `uru-1` Uruguaio | 126 (1900–2025) | 12.464 | 81 | 0ead727 | sim |
| `chi-1` Chileno | 109 (1933–2025) | 22.601 | 53 | 36e0690 | sim |
| `col-1` Colombiano | 101 (1948–2025) | 22.788 | 42 | 3f5c1d0 | sim |
| `par-1` Paraguaio | 133 (1906–2025) | 7.865 | 43 | dc2b360, 9d1ca3b, 0b793ba | sim (versão antiga: recarregar) |
| `per-1` Peruano | 109 (1912–2025) | 17.316 | 153 | 9d1ca3b, 0b793ba | não |
| `ecu-1` Equatoriano | 68 (1957–2025) | 14.195 | 63 | 0b793ba | não |

Os números de gols, cartões, conferência e cobertura estão no `README.md` da documentação. Tudo está no GitHub (push de 22/11).

## 3. De onde continuar (pendências, em ordem)

1. **Agente 1 carregar `ecu-1` e `per-1` e recarregar o `par-1`** (no GitHub desde o `0b793ba`, 22/11; recado no fim de
   `docs/coleta/pedidos-sulamerica.md`). Só acompanhar a resposta dele.
2. **Achados da revisão em aberto (o maior trabalho que falta):** 36 do Argentino (prefixo AR) e 19 do Uruguaio (UY), em
   `docs/revisao/achados.csv` (`quem_corrige` = `coleta-sulamerica`), com as provas em `docs/revisao/arg-1.md` e
   `uru-1.md`. O resumo está em `docs/coleta/pedidos-sulamerica.md`, seções "Pedidos da revisão". Os mais graves:
   - **Uruguai, UY-006:** de 1994 a 2025 a classificação final é a tabela do Apertura, com o campeão puxado para o 1º
     lugar. Por isso o vice sai errado em 14 edições (UY-004) e o 3º em 19 (UY-005). A classificação deve ser a tabla
     anual.
   - **Argentina, AR-001:** em 1913 Federación, os jogos do Estudiantes de La Plata estão gravados como Estudiantes de
     Buenos Aires.
   - **Argentina, AR-002 a AR-013:** vices errados em 12 edições.
   - **Argentina, AR-022:** cerca de 3.920 jogos com o ano errado nas temporadas que cruzam o ano.
   - **Uruguai, UY-013:** a Supercopa AUF entrou como "Final".

   Corrija, reimporte, cite os ids no `pedidos-sulamerica.md` e rode o `documentar.py`. As decisões que são do Guilherme
   estão listadas nas pendências de cada ficha: pergunte antes.
3. **Decisões em aberto:**
   - **Peru:** 1912-1921 (Liga Peruana) entraram como 10 edições só com campeão e vice, a escolha recomendada que ele
     aprovou. O agente 1 pode preferir a contagem da RSSSF.
4. **Próxima competição: `bol-1` (Bolívia), só quando o Guilherme pedir.** Depois `ven-1` (Venezuela). Siga a seção 4.
5. **Ficar de olho em `docs/coleta/pedidos-sulamerica.md`:** respostas do agente 1 e pedidos novos da revisão.

## 4. Como fazer uma competição nova

Copie a pasta da competição mais parecida e adapte. A mais recente e completa é `coleta/ecu-1/`, que tem:
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
| `rsssf_sul.py` | leitor genérico das páginas da RSSSF: `texto`, `ler`, `linha_tabela`, `_jogo`, `chave`. **Mudou? Reimporte as sete competições e compare os pacotes (`git diff --stat`)** |
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

**Python no Windows:** editar arquivo por heredoc com `python - <<'EOF'` estraga `\b` (vira backspace) e às vezes `\n`. Para
regex, use o Edit e confira com `grep -c $'\x08'`. Em f-string com `rf"..."`, `\d{1,2}` vira tupla: use `{{1,2}}`.

## 7. Decisões do Guilherme já tomadas

- Uma edição por título de campeão, como na lista da RSSSF; Apertura e Clausura que dão título são edições separadas.
- Argentino: "2025 Liga" (tabela anual) entra como edição sem jogos; Hurlingham (1891) no cadastro.
- Uruguaio: C.U.R.C.C. = Peñarol (mantido em 21/11, depois de pesquisa mostrar que é disputado).
- Paraguaio: anos sem jogos entram como edição com campeão, vice e tabela parcial (posição e pontos) quando houver; os
  jogos soltos ("Known Results") ficam de fora.
- Peruano: 1912-1921 como edições só com campeão e vice (escolha recomendada aprovada em 21/11).
- Não começar outra competição sem ele pedir.
