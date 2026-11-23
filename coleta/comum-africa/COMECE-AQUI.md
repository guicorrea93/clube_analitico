# Coleta África — comece aqui

Para o agente de coleta da África (países da CAF) que for continuar este trabalho. Leia antes:
1. `docs/COMECE-AQUI.md` (mapa do projeto);
2. `docs/agente-coleta-COMECE-AQUI.md` (método e formato do pacote);
3. `docs/agentes-internacionais-COMECE-AQUI.md` (o que muda fora do Brasil; regras da casa na seção 10);
4. `coleta/comum-sulamerica/COMECE-AQUI.md` e `coleta/ven-1/` (o exemplo de onde esta pasta foi copiada).

Este arquivo diz o que já foi feito, como e de onde continuar.

Última atualização: 23/11/2026.

## 1. Regras da casa (combinadas com o Guilherme)

- **Uma competição por vez.** Antes de cada liga, mande ao Guilherme, em poucas linhas, as decisões de escopo (era
  colonial, ligas paralelas, temporadas canceladas). Ao fim de cada uma:
  - resumo curto;
  - pedido de ok para o commit;
  - **recado de fim de coleta**: seção "Recado de fim de coleta — <slug> — <data>" no fim de
    `docs/coleta/pedidos-africa.md`, com os 8 itens da seção 10 do guia internacional, e o mesmo texto ao Guilherme num
    bloco de código. Liste os **países novos** (o agente 1 baixa as bandeiras).
- **Mexa só nas suas pastas:**
  - `coleta/<slug>/` e `coleta/comum-africa/`;
  - `data/coleta/<slug>/`, `data/cache/*-africa*/` e `data/cache/ogol-<slug>/`;
  - `docs/coleta/<slug>.md` e `docs/coleta/pedidos-africa.md`.
- **Banco só para leitura:** `sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)`. O teste de carga usa uma cópia.
- **Git:** nunca `git add -A` nem `git add .`; confira que `git diff --cached` está vazio antes do `git add`; commit só
  com o ok explícito do Guilherme; push só quando ele pedir; não troque de ramo. A mensagem termina com
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

Ordem sugerida: `egy-1`, `mar-1`, `tun-1`, `alg-1`, `rsa-1`, `nga-1`, `gha-1`, `cmr-1`, `civ-1`, `cod-1`, `sen-1`,
`ang-1`; depois as outras 1ªs divisões da CAF.

| Competição | Edições | Jogos | Clubes | Commit do pacote | No banco |
|---|---|---|---|---|---|
| `egy-1` Egípcio | 73 (1948/49–2025/26) | 11.574 | 74 | esperando o ok do Guilherme (23/11) | não |

Os números de gols, conferência e cobertura estão em `documentacao/README.md`.

**De onde continuar:**
1. `egy-1`: commit (com o ok do Guilherme) e esperar o agente 1 carregar (recado no fim de `docs/coleta/pedidos-africa.md`).
2. Próxima liga: `mar-1` (Marrocos). Antes, mandar ao Guilherme as decisões de escopo: era colonial (antes de 1956) entra ou
   não?
3. Pendências do `egy-1`: na lista `PENDENCIAS` do `documentar.py` (e no `documentacao/README.md`).

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

**Python no Windows:** como no guia da América do Sul, editar por heredoc com `python - <<'EOF'` transforma `\b` em
backspace; o `sed` com `\\b` também erra. Use o Edit e confira com `grep -c $'\x08'`.
