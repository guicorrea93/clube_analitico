# Plano único de coleta: ordem e jeito de trabalhar

Para os sete agentes de coleta: Brasil, Europa, América do Sul, África, Ásia, CONCACAF e Oceania.
Decidido pelo Guilherme em 25/11/2026. **Vale acima de qualquer ordem ou regra diferente nos seus COMECE-AQUI.** Onde
este plano não fala nada, continua valendo o que já estava combinado.

## 1. A ordem do que coletar

### Fases

Todos os agentes, menos o do Brasil (seção 1.2), seguem quatro fases. Só se passa à fase seguinte quando a anterior
terminar na região inteira.

| Fase | O que entra | Slug | Ordem dos países |
|---|---|---|---|
| **1** | 1ª divisão de **todas** as federações da sua confederação, inclusive as pequenas. Os países que não existem mais entram como competição à parte, logo depois do sucessor (Tchecoslováquia, Iugoslávia, URSS). | `<pais>-1` | ranking (seção 1.1) |
| **2** | Copa nacional de cada federação (como a Copa do Brasil). Entram também as dos países que já têm a 1ª divisão pronta. | `<pais>-copa`, `tipo` "copa" | o mesmo ranking |
| **3** | 2ªs divisões. | `<pais>-2` | o mesmo ranking |
| **4** | O resto, nesta ordem:<br>a) 3ª divisão e abaixo, até onde houver fonte;<br>b) outros torneios nacionais (supercopa, copa da liga);<br>c) torneios regionais. | `<pais>-3`, `<pais>-supercopa`, `<pais>-copa-liga`... | o mesmo ranking |

**Exceção:** país sem liga própria (como Liechtenstein, cujos clubes jogam na Suíça) pula a fase 1, mas entra na
fase 2 se tiver copa.

### 1.1. O ranking: uma foto de 25/11/2026, fixa

A ordem não muda depois, mesmo que o ranking mude.

| Agente | Ranking |
|---|---|
| Europa | Coeficiente de países da UEFA. É a foto de 24/11 que já está no seu COMECE-AQUI, seção 3; continua valendo. |
| África | Ranking de federações da CAF para as competições de clubes (o de 5 anos, que distribui as vagas da Champions da CAF). |
| Ásia | Ranking de federações da AFC para as competições de clubes ("AFC Club Competitions Ranking"). A Austrália entra. |
| América do Sul, CONCACAF e Oceania | Ranking da FIFA masculino, só com os países da sua confederação. A CONMEBOL e as outras duas não têm ranking oficial de federações. |

**Antes da próxima liga:**
- copie a lista completa da sua confederação, da melhor para a pior, para o seu COMECE-AQUI, seção 3;
- marque o que já está pronto e escreva a data e o link da foto;
- o que já está pronto fica pronto: siga do primeiro país que falta.

### 1.2. Brasil (agente 2)

Primeiro **todos os estaduais de 1ª divisão** (`bra-<uf>-1`), na ordem do Ranking Nacional das Federações da CBF (foto
de 25/11/2026, no seu COMECE-AQUI). Já estão prontos SP, RJ e MG. Antes de qualquer estadual de 2ª divisão, entram os
27 estaduais.

Depois, nesta ordem:
1. estaduais de 2ª divisão, pelo mesmo ranking (o Paulista A3 entra aqui, depois das A2 dos outros estados);
2. torneios regionais: Copa do Nordeste, Copa Verde, Rio-São Paulo, Sul-Minas...;
3. outros nacionais: Supercopa do Brasil, Copa dos Campeões...

### 1.3. Uma competição por vez

- **Escopo antes de cada uma.** O escopo é: desde quando, que eras entram, o que a federação reconhece.
  1. Faça a pesquisa a fundo.
  2. Mande ao Guilherme uma proposta curta, com a sua recomendação.
  3. Só comece com o ok dele.
  4. Registre a decisão no seu COMECE-AQUI.

  Se ele disser "decida você", decida pelo que a federação reconhece e anote o motivo.
- **Pendência com fonte:** antes de passar de fase, feche as pendências da fase que tenham fonte acessível. As que
  dependem de jornal ou arquivo ficam anotadas como limite de fonte.

## 2. O mesmo jeito de trabalhar

### 2.1. Fontes, nesta ordem de preferência

1. **Site oficial da liga ou da federação**, quando tem dados. É a melhor fonte (como o J.League Data Site, o portal da
   K League e a API da FPF).
2. **RSSSF:** a base histórica (páginas por ano, campeões, artilheiros).
3. **ogol:** data, rodada e código do clube. **Guarde sempre os calendários** em `data/cache/ogol-<slug>/`, porque os
   escudos saem deles.
4. **ESPN:** hora, estádio, público, gols e cartões, onde houver.
5. **Wikipédia:** segunda fonte do campeão e do vice, tabelas oficiais, punições. Use também a língua do país.
6. **football-data e engsoccerdata:** onde existirem.

Campeão e vice precisam bater em duas fontes. A divergência vai no relatório.

### 2.2. O pacote

Formato completo em `docs/agente-coleta-COMECE-AQUI.md`. Pontos que cada um vinha fazendo de um jeito:

**Pontos**
- Use sempre `pontos_vitoria`, `pontos_empate` e `pontos_derrota` (as duas últimas vazias = 1 e 0) quando o sistema da
  temporada inteira foge do 3-1-0 ou do 2-1-0. Exemplos: 3-2-1, 4-2-1, empate valendo 2.
- O que não cabe nessas colunas vai em `ajuste_pontos`, e a classificação traz os pontos oficiais. São os casos de
  ponto por gol, shootout, pênaltis depois do empate, empate com gols valendo mais que 0-0, bônus e punição.
- **Correção pendente:** a Grécia (até 1972/73) e a Turquia antiga só dizem o 3-2-1 na observação. O agente Europa
  preenche as colunas nessas edições.

**Jogos especiais**
- **Desempate fora da tabela:** os jogos extras de título, rebaixamento ou vaga que não contam na tabela ficam numa
  fase cujo nome **começa** por "Desempate" ("Desempate", "Desempate do título", "Desempate do rebaixamento"). O painel
  os tira da tabela e da Corrida.
- **Desempate que conta na tabela:** jogo de desempate que conta na tabela de uma fase não começa por "Desempate". Use
  "Primeira fase - Desempate".
- **Decidido fora de campo:** `resultado_especial` "awd". Os gols são o placar oficial; ficam vazios na "derrota para
  os dois". O placar de campo e o motivo vão na observação. "wo" continua aceito para o W.O. de quem não compareceu.

**Edições**
- **Título dividido:** coluna `co_campeao`, logo depois de `vice`.
- **Edição não oficial:** coluna `oficial` = "não", com o aviso na observação.
- **Duas edições no mesmo ano:** a `temporada` leva o nome que as distingue ("1932 LMDT", "2009 Apertura ANAPROF").
- **Fonte fraca:** a edição entra assim mesmo. "Só o campeão", "sem jogos (só a tabela final)" e "jogos incompletos..."
  vão no `formato`.

**Nomes de clube**
- Use o nome pelo qual o clube é conhecido no Brasil.
- **Nome que já existe** no banco ou em qualquer `data/coleta/*/pacote/clubes.csv`:
  1. primeiro acrescente a cidade: "Nacional de Asunción", "Al-Ahli de Jeddah";
  2. sem cidade que resolva, ponha o país entre parênteses: "Santos (África do Sul)".

  **Daqui em diante não use "de <país>".** Os nomes já carregados ficam como estão.
- **Clubes que vão colidir com a A-League:** Western United e Central Coast (Ilhas Salomão). O agente da Ásia resolve
  quando chegar à Austrália, pondo a cidade nos australianos.
- **Identidade:** é a linhagem do clube, e cada decisão fica com o motivo. Na mesma cidade, a troca de nome é o mesmo
  clube. A mudança de cidade, a compra de vaga e a refundação geram outro clube.

**Antes do commit**
- Confira os nomes contra o banco, só lendo (`file:db/futebol.db?mode=ro`).
- Confira também contra todos os `clubes.csv` da pasta `data/coleta/`.

### 2.3. Leitor da RSSSF

As cópias do `rsssf_sul.py` nas pastas comuns da Ásia, da CONCACAF e da Oceania têm o defeito dos autores em duas
linhas. Antes da próxima liga, traga a correção do `coleta/comum-sulamerica/rsssf_sul.py`.

**Regra geral:** quem mexe no leitor comum reimporta as competições afetadas, compara os totais e diz no recado o que
mudou.

### 2.4. Entrega: igual para todos

1. `testar_carga.py <slug> <scratchpad>` termina em "-> OK".
2. Rode `documentar.py` e atualize o seu COMECE-AQUI: o que está pronto, a próxima competição, onde parou. Ele tem que
   bater com o recado; havia números e estados desatualizados em vários.
3. Escreva o **recado de fim de coleta** (8 itens) no fim do seu arquivo de pedidos. Entregue o mesmo texto ao
   Guilherme num bloco de código.
   - No item 2, escreva "Commit: o deste recado (`<mensagem do commit>`)".
   - O hash vai só na mensagem ao Guilherme.
   - **Não faça commit só para anotar o hash.**
4. Peça o ok ao Guilherme. **O ok vale para o commit e para o push juntos.** Para o push:
   - confira antes `git log origin/main..HEAD`;
   - comando: `env -u GITHUB_TOKEN GIT_TERMINAL_PROMPT=0 git push origin main`.
5. **Git na pasta compartilhada:**
   - nunca use `git add -A` nem `git add .`;
   - confira que `git diff --cached` está vazio antes de adicionar;
   - adicione só os seus caminhos;
   - termine a mensagem com `Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>`.
6. O agente 1 carrega no banco e publica no painel em lotes. Não precisa esperar por ele para seguir.

Logs e conferências vão para o scratchpad. Fale com o Guilherme em português, curto e por partes.

## 3. De onde cada agente recomeça

| Agente | Pronto | Recomeça por |
|---|---|---|
| **Brasil** | Séries C e D, Copa do Brasil, Paulista, A2, Carioca, Mineiro | Lista dos estaduais pelo ranking da CBF; depois o próximo estadual que falta (pela lista antiga era o Gaúcho). A3 só depois de todos os estaduais. |
| **Europa** | eng, esp, ita, ger, fra, por, ned, sco, bel, tur, gdr, gre, cze (13) | Colunas de pontos em gre-1 e tur-1; depois a Tchecoslováquia (escopo já decidido) e a Polônia, pela lista UEFA. A fase 2 começa pelo `eng-copa` (FA Cup). |
| **América do Sul** | As 9 ligas e as 7 copas (Peru e Bolívia sem copa, decisão de 24/11) | Fases 1 e 2 feitas. Fechar a D5b, se a fonte permitir; depois a fase 3 (2ªs divisões) pelo ranking FIFA. |
| **África** | egy, mar, tun, alg, rsa, nga, gha, cmr (8) | Lista CAF; o próximo país que falta (a lista antiga dizia Costa do Marfim). Escopo antes. |
| **Ásia** | jpn, kor, ksa (3) | Lista AFC; o próximo país que falta (a lista antiga dizia Irã). Escopos já anotados: Irã, Austrália, China, Índia. Antes, corrigir o leitor (2.3) e o COMECE-AQUI (kor-1 e ksa-1 já estão no banco). |
| **CONCACAF** | mex, usa, crc, hon, gua, slv, pan (7) | Lista FIFA da CONCACAF; o próximo que falta (a lista antiga dizia Jamaica). Antes, corrigir o leitor (2.3) e o README (próximas competições desatualizadas). A MLS 2026 entra depois de 18/12. |
| **Oceania** | nzl, tah, ncl, fij, png, sol (6) | Lista FIFA da OFC; o próximo que falta (a lista antiga dizia Vanuatu). Kiribati e Tuvalu só no fim, se houver fonte. Antes, corrigir o leitor (2.3) e o README (dizia "2ªs divisões"). |
