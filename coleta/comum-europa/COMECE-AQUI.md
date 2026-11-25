# Coleta Europa — comece aqui

Para o agente de coleta Europa (agente 3) que for continuar este trabalho. Leia antes o guia geral
`docs/agentes-internacionais-COMECE-AQUI.md`, que traz o formato do pacote, as pastas de cada agente e as regras de
identidade dos clubes. Este arquivo diz o que já foi feito, como foi feito e de onde continuar.

Última atualização: 22/11/2026.

**Documentação completa:** `coleta/comum-europa/documentacao/`. Tem o índice (`README.md`) e uma ficha por liga, com:
- tudo o que o pacote tem;
- fontes e regras;
- conferência com as tabelas publicadas;
- cobertura de cada campo década a década;
- formato do campeonato ao longo do tempo;
- campeões, rebaixados e punições;
- todas as correções e decisões, com o motivo;
- o que não deu para coletar;
- pendências.

A documentação é gerada por `python coleta/comum-europa/documentar.py` a partir dos pacotes e dos importadores. Rode
depois de toda importação e mantenha à mão só a lista `PENDENCIAS`, no começo do script. Os relatórios
`docs/coleta/<slug>.md` continuam com o detalhe temporada a temporada.

## 1. Regras da casa (combinadas com o Guilherme)

- **Uma liga por vez, e só com o ok dele.** Ao fim de cada liga: resumo curto, pedido de ok para o commit, e recado ao
  agente do banco em `docs/coleta/pedidos-europa.md`.
- **Mexa só nas suas pastas:** `coleta/<slug>/`, `coleta/comum-europa/`, `data/coleta/<slug>/`,
  `data/cache/*-europa*/` e `data/cache/ogol-<slug>/`, `docs/coleta/<slug>.md` e `docs/coleta/pedidos-europa.md`.
  Nunca toque em `db/`, `futebol/`, `serie_b/`, `historico/`, `gerar_dashboard_v2.py`, `painel/`, `dashboard*.html`,
  `data/escudos/`.
- **Banco só para leitura:** `sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)`. O teste de carga usa uma cópia
  (seção 5).
- **Git:**
  - nunca `git add -A` nem `git add .`: adicione só os seus caminhos;
  - commit e push só com o ok do Guilherme;
  - não troque de ramo;
  - push com `env -u GITHUB_TOKEN GIT_TERMINAL_PROMPT=0 git push origin main`;
  - a mensagem de commit termina com `Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>`.
- **Push com commits de outros agentes na fila:** veja `git log --oneline origin/main..HEAD` antes. Se houver commits de
  outros agentes, o envio pode ser barrado pelas permissões; avise o Guilherme ou espere eles enviarem.
- **Logs e conferências vão para o scratchpad**, nunca soltos no repositório.
- **Nome de clube único no mundo:** confira no banco e nos `clubes.csv` dos outros pacotes antes de batizar um clube
  (por exemplo, "Nacional da Madeira", porque já existe o Nacional do Uruguai). Um jeito rápido: ler a tabela `clube` do
  banco e juntar os `data/coleta/*/pacote/clubes.csv`.
- **Calendários do ogol ficam em `data/cache/ogol-<slug>/`:** o agente 1 tira os escudos de lá.
- **Critério do Guilherme nas dúvidas:** "o que for mais fiel à história / ao campeonato". Pesquise na internet quando as
  fontes divergem, e registre a decisão com o motivo no código (dicionários `CORRECOES`, `TRIBUNAL`...) e no relatório.
- **Fale com ele em português, curto e por partes.** Ele gosta de receber o recado ao agente principal num bloco de código,
  para copiar.

## 1.1 Prioridade e recado de fim de coleta (decisão do Guilherme, 22/11/2026)

- **Prioridade agora é coletar ligas novas, na ordem:** `ned-1` (Holanda), `sco-1` (Escócia), `bel-1` (Bélgica) e
  `tur-1` (Turquia). O ok para a `ned-1` está dado.
- **Ordem atualizada (decisão do Guilherme, 22/11/2026):**
  1. `sco-1` (Escócia);
  2. eras antigas no mesmo slug: Holanda 1888/89–1955/56 (`ned-1`) e Alemanha 1902/03–1962/63 (`ger-1`), com os títulos
     oficiais;
  3. `bel-1` (Bélgica);
  4. `tur-1` (Turquia).
- **Situação (24/11/2026):** `sco-1`, eras antigas da Holanda e da Alemanha, `bel-1` e `tur-1` no GitHub (ver git log).
  IT-017 (Itália 1898 a 1928/29) pronto em 24/11. A ordem da seção 1.1 e a fila da revisão estão cumpridas; a próxima
  liga espera o Guilherme.
- **Como fazer as eras antigas:**
  - o painel aceita fases regionais + fase final, edição sem jogos e tabela parcial (colunas vazias, posição repetida,
    como no `bra-sp-2` e no `par-1`);
  - a classificação final traz todos os participantes da fase final (e, se der, dos regionais), com o campeão oficial em
    1º;
  - edição sem campeão (guerra) fica com `campeao` vazio e o motivo na `observacao`.
- **Não trate agora achados da revisão nem pendências antigas.** O agente de revisão está fazendo uma revisão profunda e
  vai deixar um plano em `docs/revisao/plano-coleta-europa.md`. Siga esse plano quando o Guilherme disser que é hora.
- **A qualidade das ligas novas não muda:**
  - conferência com as tabelas publicadas;
  - `testar_carga.py`;
  - `documentar.py` e este guia atualizados no mesmo commit;
  - commit e envio com o ok do Guilherme.
- **Ao terminar cada liga, escreva o recado de fim de coleta.** Ele vai no fim de `docs/coleta/pedidos-europa.md`, numa
  seção "Recado de fim de coleta — <slug> — <data>", para o agente 1 e o agente de revisão. Entregue o mesmo texto ao
  Guilherme. Conteúdo:
  1. o que foi feito: temporadas, jogos, clubes, gols com autor, cartões e fontes;
  2. commit(s);
  3. teste de carga;
  4. pedidos ao banco e ao painel;
  5. decisões tomadas (com o motivo) e as que esperam o Guilherme;
  6. o que não deu para coletar e as pendências, com a fonte que poderia resolver;
  7. onde a revisão deve olhar primeiro;
  8. próxima liga.

## 2. O que está pronto

Todos os pacotes abaixo estão no GitHub, passaram no teste de carga e têm relatório em `docs/coleta/<slug>.md`.

| Liga | Temporadas | Jogos | Gols c/ autor | Cartões | Clubes | Último commit |
|---|---|---|---|---|---|---|
| `eng-1` Inglês | 127 (1888/89–2025/26) | 51.330 | 25.878 | 33.166 | 65 | 103ccf1 |
| `esp-1` Espanhol | 95 (1928/29–2025/26) | 27.716 | 25.072 | 51.662 | 63 | 62a8693 |
| `ita-1` Italiano (grupos regionais e finais até 1928/29; Serie A) | 124 (1898–2025/26) | 34.732 | 24.598 | 43.962 | 191 | (ver git log) |
| `ger-1` Alemão (fase final até 1962/63; Bundesliga) | 124 (1902/03–2025/26) | 20.303 | 56.842 | 30.251 | 194 | (ver git log) |
| `fra-1` Francês | 88 (1932/33–2025/26) | 30.466 | 22.613 | 35.434 | 77 | 469f615 |
| `por-1` Português | 92 (1934/35–2025/26) | 20.978 | 18.958 | 30.915 | 73 | c0ddbdd |
| `ned-1` Holandês (fase final até 1955/56; Eredivisie) | 138 (1888/89–2025/26) | 21.878 | 23.019 | 24.431 | 93 | (ver git log) |
| `sco-1` Escocês | 129 (1890/91–2025/26) | 33.076 | 14.565 | 19.812 | 46 | 2fef629 |
| `bel-1` Belga | 123 (1895/96–2025/26) | 28.712 | 12.031 | 18.167 | 81 | f4a1701 |
| `tur-1` Turco (era antiga até 1958; liga nacional) | 97 (1924–2025/26) | 20.971 | 13.891 | 23.395 | 168 | (ver git log) |
| `gdr-1` Alemanha Oriental (zona soviética e DDR-Oberliga) | 44 (1948–1990/91) | 8.062 | 0 | 0 | 52 | (ver git log) |
| `gre-1` Grego (fase nacional até 1958/59; Alpha Ethniki e Super League) | 90 (1927/28–2025/26) | 18.689 | 8.900 | 20.025 | 69 | (ver git log) |
| `cze-1` Tcheco (liga da República Tcheca) | 33 (1993/94–2025/26) | 8.234 | 7.121 | 0 | 35 | (ver git log) |

Todas as ligas vão até 2025/26, a última temporada terminada. O agente 1 já carregou e publicou Inglês, Espanhol, Italiano
e Alemão até 2024/25 (`docs/coleta/pedidos-europa.md`, respostas dele). Os recados para recarregar Espanhol, Italiano,
Alemão e Francês (com 2025/26) e carregar o Português já estão lá.

**Quando terminar uma temporada nova** (2026/27 termina em maio de 2027), estenda cada liga:
- a) mude `TEMPORADAS` em `edicoes.py` e os `range(..., 2026)` de `baixar.py` e `importar.py`;
- b) baixe com `python coleta/<slug>/baixar.py fd ogol=<ano>-<ano> wiki rsssf espn`; apague antes as listas de campeões
  e de artilheiros já baixadas, para virem atualizadas;
- c) ponha o ano em `SO_FD` do importador, porque o engsoccerdata demora a trazer a temporada nova e a base vem do
  football-data (no Francês a temporada sai do ogol, pelo `reparar`; no Português o ogol já é a base);
- d) importe, teste a carga e rode o `documentar.py`.

**Rebaixamento na última temporada:** como não há temporada seguinte para comparar, vale a marca da Wikipédia.
- A marca de play-off não é rebaixamento.
- Confira o resultado do play-off e ponha quem perdeu à mão (`PLAYOFF_PERDIDO` no Alemão; no Português, o importador
  baixa a temporada seguinte do ogol).

## 3. De onde continuar (pendências, em ordem)

**Revisão profunda (plano `docs/revisao/plano-coleta-europa.md`): corrigida em 23/11/2026**, liga a liga, a pedido do
Guilherme. Commits:
- 5a1d3ea: IT-002, QE-002;
- 5794549: Italiano;
- 3d2db74: Espanhol;
- db95ab2: Inglês;
- f2cfcbc: Francês;
- 28d0534: Alemão;
- b4175a0: Português;
- 692670f e e22bf60: tradutor comum.

**Rodada de fechamento (24/11/2026, a pedido do Guilherme: "não ter nada pendente antes de uma nova etapa").** Nada
ficou em aberto na coleta. Em `documentar.py`, as sobras estão em três dicionários:
- `PENDENCIAS`: o que falta fazer. Está vazio;
- `LIMITES`: limites de fonte, fechados. Nenhuma fonte em lote tem o dado, e o item só volta com uma fonte nova;
- `REVISAO`: decisões da coleta que o agente de revisão confere (fusões da Holanda, tabelas da Escócia, Kayseri,
  clubes da RDA e da era antiga da Itália).

O que foi resolvido na rodada:
- **DE-004:** o ogol concorda com a base nas 3 datas; fica a base (EXPLICACOES de 1964, 1969 e 1978 no
  `ger-1/importar.py`);
- **Alemão 1947/48:** a Wikipédia em alemão confirma os placares da RSSSF (EXPLICACOES de 1947 no `ger-1/antigo.py`);
- **Italiano 1953/54:** o triangular de rebaixamento (Udinese, SPAL e Palermo) entrou com placares, datas, cidades e
  autores dos gols da RSSSF (`EXTRAS` em `ita-1/spareggi.py`);
- **nomes da ESPN:** varredura dos nomes em formato de documento que repetem um jogador do mesmo clube e temporada com o
  nome de jogo. Foram 29 trocas em `nomes_jogadores.py`, em 7 ligas;
- **fechados como limite de fonte:**
  - PT-010: sem terceira fonte; explicado em EXPLICACOES de 1938 e 1939 no `por-1/importar.py`;
  - FR-005 e FR-017: só o jornal da época decidiria;
  - Turco 1962/63: o grupo de classificação não está no ogol nem nas Wikipédias en e tr;
  - PT-020, FR-009 (1 ou 2 dias), FR-022, autores dos gols antes da ESPN e ligas regionais: dados só jogo a jogo.

Também na rodada:
- a ordem dos clubes empatados em tudo na classificação montada da era antiga do Italiano agora é alfabética (antes
  mudava a cada execução);
- o índice da documentação mostra a primeira e a última temporada pelo ano, e não pela ordem das linhas.

Antes, já feito: IT-017 (Itália 1898-1929), em 24/11 (`coleta/ita-1/antigo.py`, Wikipédia em italiano).

Ferramentas novas no código comum, para as próximas ligas:
- `notas_wiki.py`: notas da Wikipédia em português; nota nova sem tradução para o importador;
- `nomes_jogadores.py`: nomes da ESPN em formato de documento, aplicado ao gravar o pacote;
- `bdfutbol.py`: página de temporada do BDFutbol (árbitro, estádio);
- `ogol_ficha.py`: autores dos gols na ficha do ogol. O importador lista as fichas que faltam em
  `data/coleta/<slug>/fichas_pendentes.json`, e `baixar.py fichas` as baixa.

Correções em lote ficam em `data/coleta/<slug>/correcoes/` (datas, jogos a tavolino), com a fonte de cada linha.

1. **EN-016 (revisão, baixa): resolvido** nas correções do Inglês de 23/11 (db95ab2): os 12 jogos têm os autores pela
   ficha do BDFutbol (`GOLS_MANUAIS` em `coleta/eng-1/importar.py`, 37 gols); conferido em 24/11: nenhum jogo do Inglês
   com gols ficou sem autor desde 2002/03. Nenhum achado da revisão segue aberto para a coleta Europa.
2. **Ordem de coleta: plano único de coleta (`docs/coleta/plano-de-coleta.md`, Guilherme, 25/11/2026). Vale acima
   do resto deste guia.**
   - **Fases** (só se passa à seguinte quando a anterior terminar na região inteira):
     1. 1ª divisão de **todas** as federações (`<pais>-1`), inclusive as pequenas. Os países que não existem mais entram
        como competição à parte, logo depois do sucessor;
     2. copa nacional de cada federação (`<pais>-copa`, `tipo` "copa"), começando pelo `eng-copa` (FA Cup);
     3. 2ªs divisões (`<pais>-2`);
     4. o resto: 3ª divisão e abaixo, supercopa e copa da liga, torneios regionais.
   - **Ordem dos países:** coeficiente de países da UEFA, numa foto de 24/11/2026, fixa: não muda quando o ranking mudar.
     Fonte: [UEFA coefficient, Wikipédia](https://en.wikipedia.org/wiki/UEFA_coefficient), tabela "as of 24 November
     2026" (a mesma do [ranking da UEFA](https://www.uefa.com/nationalassociations/uefarankings/country/)). O que já
     está pronto fica pronto; segue-se do primeiro país que falta.
   - **Uma competição por vez:** pesquisa do escopo, proposta curta ao Guilherme com a recomendação, só começa com o ok
     dele, e a decisão fica registrada aqui. Se ele disser "decida você", vale o que a federação reconhece.
   - **Entrega:** teste de carga, `documentar.py`, este guia e o recado de fim de coleta. Pedir o ok ao Guilherme, que vale
     para o commit e o push juntos.

   | Rank UEFA | Federação | Situação |
   |---|---|---|
   | 1 | Inglaterra | **pronta** `eng-1` |
   | 2 | Itália | **pronta** `ita-1` |
   | 3 | Espanha | **pronta** `esp-1` |
   | 4 | Alemanha | **pronta** `ger-1` (e gdr-1, Alemanha Oriental) |
   | 5 | França | **pronta** `fra-1` |
   | 6 | Portugal | **pronta** `por-1` |
   | 7 | Bélgica | **pronta** `bel-1` |
   | 8 | Holanda | **pronta** `ned-1` |
   | 9 | Turquia | **pronta** `tur-1` |
   | 10 | Grécia | **pronta** `gre-1` (24/11) |
   | 11 | Tchéquia | **pronta** `cze-1` (25/11); depois a Tchecoslováquia |
   | 12 | Polônia |  |
   | 13 | Noruega |  |
   | 14 | Dinamarca |  |
   | 15 | Chipre |  |
   | 16 | Suíça |  |
   | 17 | Áustria |  |
   | 18 | Hungria |  |
   | 19 | Croácia |  |
   | 20 | Suécia |  |
   | 21 | Escócia | **pronta** `sco-1` |
   | 22 | Romênia |  |
   | 23 | Ucrânia |  |
   | 24 | Azerbaijão |  |
   | 25 | Israel |  |
   | 26 | Eslovênia |  |
   | 27 | Eslováquia |  |
   | 28 | Bulgária |  |
   | 29 | Sérvia | depois a Iugoslávia |
   | 30 | Rússia | depois a URSS |
   | 31 | Islândia |  |
   | 32 | Irlanda |  |
   | 33 | Armênia |  |
   | 34 | Letônia |  |
   | 35 | Bósnia |  |
   | 36 | Kosovo |  |
   | 37 | Finlândia |  |
   | 38 | Cazaquistão |  |
   | 39 | Liechtenstein | sem liga própria (clubes no campeonato suíço): pula a fase 1; entra na fase 2 se tiver copa |
   | 40 | Moldávia |  |
   | 41 | Ilhas Faroé |  |
   | 42 | Albânia |  |
   | 43 | Macedônia do Norte |  |
   | 44 | Belarus |  |
   | 45 | Lituânia |  |
   | 46 | Gibraltar |  |
   | 47 | Andorra |  |
   | 48 | Malta |  |
   | 49 | Estônia |  |
   | 50 | Geórgia |  |
   | 51 | Irlanda do Norte |  |
   | 52 | Luxemburgo |  |
   | 53 | Montenegro |  |
   | 54 | País de Gales |  |
   | 55 | San Marino |  |

   **Próxima: a Tchecoslováquia** (competição à parte, logo depois da Tchéquia). Decidido em 25/11/2026: entra a liga do
   Protetorado da Boêmia e Morávia (1938/39-1943/44); o resto do escopo vai em proposta ao Guilherme. Depois, a Polônia.

   **Correções do plano (seção 3 e regras da seção 2.2), feitas em 25/11/2026:**
   - colunas `pontos_empate` e `pontos_derrota` preenchidas no 3-2-1 da Grécia (até 1972/73 e na era antiga) e da Turquia
     antiga;
   - Turquia antiga: as 27 edições não reconhecidas (Şampiyonası, Millî Küme) com vencedor e vice e `oficial` = "não";
   - derrota para os dois com gols vazios: Francês 1992/93 (VA x OM), Português 1986/87 (Braga x Benfica) e Grego (greve
     de 1986/87; Niki Volos x OFI, 2014/15). O placar de campo fica na observação;
   - título dividido: Escocês 1890/91, com Rangers em `co_campeao` e sem vice;
   - o `pacote.py` grava as colunas novas (`pontos_empate`, `pontos_derrota`, `co_campeao`, `oficial`) e a regra da
     derrota para os dois (`_derrota_dois` na partida).

   Em 24/11 também ficaram prontos `bel-1`, `tur-1` (com a era antiga), IT-017 e `gdr-1` (D-05b), e a rodada de
   fechamento zerou as pendências. As eras antigas da Holanda (1888/89–1955/56) e da
   Alemanha (1902/03–1962/63) estão prontas (22/11), cada uma no `antigo.py` do seu slug (leitura da RSSSF em
   `rsssf_antigo.py`), chamado pelo `importar.py` antes do cadastro de clubes. O que ficou de fora está nas pendências de
   cada liga (`documentacao/ned-1.md` e `documentacao/ger-1.md`).
3. **Ficar de olho em `docs/coleta/pedidos-europa.md`:** respostas do agente 1 e pedidos novos da revisão.

## 4. Como fazer uma liga nova

Copie a liga mais parecida e adapte:

- **com engsoccerdata como base:** `fra-1` (base engsoccerdata + `reparar` pelo ogol onde a base falha) ou `ita-1`;
- **sem engsoccerdata nos anos antigos:** `por-1`, mais simples, com base no ogol e o clube casado pelo código do ogol.

Arquivos de cada liga, em `coleta/<slug>/`:

| Arquivo | O que faz |
|---|---|
| `edicoes.py` | `TEMPORADAS`, `temporada(a)` ("1992/93"), `nome_oficial(a)`, `wiki_titulo(a)`, `rsssf_url(a)` |
| `baixar.py` | uma função por fonte, que grava em `data/coleta/<slug>/<fonte>/`; rodar `python coleta/<slug>/baixar.py ogol esd fd rsssf wiki espn` (`ogol=1934-1960` baixa só uma faixa; dá para rodar várias faixas em paralelo) |
| `rsssf_<pais>.py` | leitor das páginas da RSSSF daquele país, quando o formato é próprio |
| `importar.py` | monta o pacote em `data/coleta/<slug>/pacote/` e o relatório `docs/coleta/<slug>.md` |

Código comum em `coleta/comum-europa/`:

| Arquivo | O que faz |
|---|---|
| `baixar.py` | `pegar(url, destino)`: download educado, com cache e espera |
| `ogol.py` | `edicoes(slug_da_competicao, cache)` e `calendario(id, ano, cache)`; valida o link canônico porque o ogol às vezes devolve a página de outra competição |
| `espn.py` | `dias(liga, [datas], cache)`: placar diário da ESPN (hora, estádio, público, gols e cartões com minuto) |
| `wikipedia.py`, `wiki_tabela.py` | wikitexto pela API e leitor do módulo "Sports table" (ordem oficial, ajuste de pontos, marcas de resultado) |
| `pacote.py` | `gravar(pasta, competicao, tabelas)` no formato do guia geral; extras `arbitro` e `estatisticas.csv` |
| `clubes_<pais>.py` | cadastro dos clubes do país (nome de exibição, cidade, país), `ALIASES`, `POR_ANO` (nomes que dependem da época) e, no Português, `OGOL` (código do ogol -> clube) |
| `testar_carga.py` | teste de carga numa cópia do banco |

Códigos das competições no ogol: `premier-league` (Inglaterra, desde 1888), `campeonato-espanhol`, `campeonato-italiano`,
`bundesliga`, `campeonato-frances`, `campeonato-portugues`, `campeonato-holandes` (desde 1888/89), `liga-escocesa` (desde 1890/91). Para achar um novo, teste
`ogol.edicoes("<slug>", cache)` com nomes prováveis e fique com o que lista todas as temporadas.

Passos de uma liga:

1. Ver as fontes:
   - engsoccerdata em `data/cache/engsoccerdata-europa/`;
   - football-data;
   - ESPN: testar a URL do placar num dia de jogo para ver desde quando cobre;
   - ogol;
   - RSSSF: lista de campeões, artilheiros e páginas por temporada;
   - Wikipédia en: título da temporada, com redirecionamento.
2. Escrever `edicoes.py` e `baixar.py` e baixar tudo, com os logs no scratchpad.
3. Escrever `clubes_<pais>.py` e garantir que todo nome de toda fonte resolve. Confira a unicidade dos nomes (seção 1).
4. Comparar a base com a outra fonte jogo a jogo (matriz da RSSSF, ogol) antes de escrever o importador. Assim aparecem
   cedo as temporadas quebradas e as colunas trocadas.
5. `importar.py`:
   - cada tabela publicada (RSSSF, Wikipédia) é comparada com a tabela calculada dos jogos;
   - toda divergência vira correção com motivo ou explicação em `EXPLICACOES`;
   - o critério de desempate é testado por temporada;
   - rebaixado = quem não está na temporada seguinte, com as exceções explicadas.
6. Testar a carga e escrever o recado em `pedidos-europa.md`.
7. Pôr a liga em `LIGAS` e `PENDENCIAS` no `documentar.py`, rodá-lo e atualizar este arquivo.
8. Pedir o ok do commit. A documentação vai no mesmo commit da liga.

## 5. Teste de carga

```
python coleta/comum-europa/testar_carga.py <slug> <pasta temporária (o scratchpad)>
```

Deve terminar com `<slug>: N edições, N jogos, N clubes novos -> OK`.

## 6. Armadilhas já encontradas (vale para as próximas ligas)

**ogol**
- Às vezes devolve a página de outra competição: `pagina_valida` confere o link canônico e baixa de novo.
- Junta clubes diferentes no mesmo código (CD Málaga e Málaga CF). Por isso o voto por código é por temporada (`Mapa`, com
  `get(cod, ano)`).
- "DA" (decisão administrativa) e "IC" vêm sem placar. A ficha do jogo
  (`https://www.ogol.com.br/jogo/<data>-<clubes>/<id>`) traz o motivo e o placar do intervalo ("Int: 1-1"); guarde-a em
  `data/cache/ogol-<slug>/jogo_<id>.html`.
- Anos 1930: datas provisórias (01/07 ou 01/08, com dezenas de jogos no mesmo dia). Ficam vazias.

**engsoccerdata**
- França anos 1930: clubes trocados. Itália 1946–48: temporada quebrada.
- Faltam temporadas inteiras: França 1937/38 e 1994/95; Portugal tudo antes de 1994/95; tudo a partir de 2025/26.

**RSSSF**
- As matrizes têm erros de forma: linhas com o número trocado (Portugal 1977/78) e colunas trocadas (Portugal 1990/91,
  colunas 13 e 14). Confira a matriz contra o ogol antes de confiar nela.
- Às vezes erra pontos ou V-E-D de um clube. Ponto a mais na tabela da RSSSF é erro de digitação, não punição.

**Wikipédia**
- **Tabela:**
  - erra gols de um clube aqui e ali;
  - punições: às vezes põe só como nota (Porto 2007/08: a Wikipédia de hoje não desconta os 6 pontos do Apito Final);
  - França 1973–76: põe o bônus ofensivo no `adjust_points`.
- **Marcas:** a de play-off (`RPO`, "Qualification for the relegation play-offs") não é rebaixamento.
- **Temporadas recentes:** a tabela fica num modelo à parte ("{{2024–25 Ligue 1 table}}"); o `baixar.py` guarda como
  "<título> (tabela).wiki".

**ogol, mais armadilhas (Holanda):**
- A mesma edição traz play-offs (vaga europeia, nacompetitie): fique só com os jogos de rodada ("R12").
- Em temporada cancelada traz jogos adiados ("ADI") e anulados ("ANU"), sem placar: descarte.
- Às vezes põe o antecessor de um clube formado por fusão na ficha do sucessor (Rapid JC no Roda JC, Alkmaar '54 no AZ):
  o `OGOL` do cadastro aceita uma faixa de anos por código (`clubes_ned.py`).

**Escócia, o que serve para outras ligas:**
- **Par que se repete:** o mesmo par joga 2, 3 ou 4 vezes por temporada. As outras fontes são casadas pelo par e pela data
  mais próxima (`casar` em `coleta/sco-1/importar.py`); se só sobra um jogo do par, aceita a data diferente (jogo adiado).
- **Mando invertido no ogol:** quando outra fonte traz o par ao contrário na mesma data e com o mesmo placar, o mando é
  corrigido (`inverter`).
- **Matriz de resultados da Wikipédia** (`wiki_tabela.resultados`): conferência jogo a jogo. Um placar do ogol só é trocado
  pelo da matriz quando as tabelas publicadas fecham melhor com ele (um por um e, se preciso, em combinação de até 4).
- **Divisão em dois grupos depois da 33ª rodada** (2000/01+): na classificação rodada a rodada, o grupo de cima fica nas 6
  primeiras posições; o desempate é testado dentro de cada grupo.
- **RSSSF com erros de leitura óptica** ("l8", "lo", "Z,"): normalizados no leitor (`rsssf_sco.texto`).
- **Velocidade do ogol:** com várias frentes em faixas sem sobreposição, de ~5 para ~50 páginas por minuto (recado ao
  agente do Brasil).

**Bélgica, o que serve para outras ligas:**
- **ogol só desde 1960/61:** antes, a base é a matriz da Wikipédia (sem data). A soma dos jogos nem sempre fecha com a
  tabela da RSSSF: a classificação final fica com os números publicados, com observação (`numeros_pub` no importador).
- **Nomes do ogol não confiáveis:** o clube vai pelo código do ogol, identificado pelos números da campanha iguais aos da
  RSSSF e da Wikipédia (`clubes_bel.OGOL`).
- **Play-offs (2009/10+):** a fase regular é o primeiro jogo de cada par entre os clubes da maior tabela da Wikipédia; o
  resto vai para a tabela de play-off que contém os dois clubes. A tabela do título é a que tem o 1º da fase regular, a de
  rebaixamento a que tem o último, as outras são do europeu (o título da seção na Wikipédia às vezes vem vazio). Os pontos
  de partida (metade da fase regular) vêm do ajuste da tabela.
- **Matriz dentro da tabela:** os jogos dos play-offs ficam em "Sports table" com `match_XXX_YYY`; o importador troca o
  nome do módulo e lê com `wiki_tabela.resultados`. Nota de rodapé dentro da célula (`{{efn|...3–1...}}`) vira placar
  falso: tire antes (`sem_notas`).
- **Código da matriz:** use primeiro o nome da tabela do mesmo artigo (a matriz mostra "Mechelen" para o Racing Mechelen).
- **Modelos transcluídos:** a tabela pode estar em `{{... play-offs table}}`; o `baixar.py wiki` baixa todos.
- **Clube excluído no meio da temporada** (Lommel 2002/03, Mouscron 2009/10): jogos anulados fora do pacote, clube no fim,
  zerado (`EXCLUIDOS`).
- **ESPN 2016/17-2017/18:** gols repetidos, às vezes com 1 minuto de diferença; o importador tira os repetidos.

**Itália antes da Serie A (IT-017), o que serve para outras eras antigas:**
- **Wikipédia em italiano:** cada artigo de temporada tem, por grupo, "Classifica finale" (com o modelo `{{Calcio X}}`,
  que identifica o clube sem ambiguidade), "Calendario" (rodadas com ida e volta e data) e/ou "Tabellone" (matriz). Leitor
  em `coleta/ita-1/wiki_antigo.py`.
- **Identidade pelo modelo `{{Calcio X}}`:** a Wikipédia it separa as entidades ("Hellas (1907-1918)", "Piemonte
  (1910-1915)"); mapa modelo → chave em `clubes_ita.MODELOS_IT`.
- **Nome curto do calendário:** casado com os clubes do mesmo grupo (exato, prefixo, contido, palavras); apelidos de época
  (`APELIDOS`, `APELIDOS_SECAO` em `antigo.py`).
- **Armadilhas do wikitexto:** linha que começa com "||" (célula vazia) e `<ref>` de várias linhas quebram a leitura
  (`notas_em_marcas`); números de ano dentro da célula da classificação; `\b` vira backspace no heredoc do bash (use o
  editor ou `chr(92)`).
- **Dois campeonatos na mesma temporada** (1921/22): temporadas "1921/22 (FIGC)" e "1921/22 (CCI)", ocorrências pela
  temporada em texto.

**Alemanha Oriental (`gdr-1`), o que serve para outras ligas:**
- **RSSSF por temporada** (`tablesd/ddrYY.html`): rodada, data e placar; a primeira seção é a Oberliga, depois vêm a
  DDR-Liga e a copa (o leitor `coleta/gdr-1/rsssf_gdr.py` para na tabela final). Jogo dado fora de campo como "X:0"
  (vitória para o lado do X, gols 0:0); nome do visitante colado no placar ("2:1Hallescher FC Chemie").
- **Identidade:** cadastro próprio (`clubes_gdr.py`) com mapeamento explícito de cada grafia; os clubes que também
  jogaram a Bundesliga usam a chave do `clubes_ger.py` (a busca aproximada do alemão erra aqui: "Vorwärts Berlin" cairia
  no Vorwärts 1890).

**Turquia, o que serve para outras ligas:**
- **Era antiga (antes de 1959):** três competições no mesmo slug, com rótulos "1940 (Millî Küme)", "1940 (Şampiyonası)",
  "1956/57 (Federasyon Kupası)". Só as reconhecidas pela federação têm `campeao` (regra D-09); o sistema de pontos muda
  por edição (3-2-1 ou 2-1-0, `PONTOS_2_1_0` em `coleta/tur-1/antigo.py`). O alvo do link da Wikipédia resolve os nomes
  forçados dos anos 1930 (Alsancak = Altay, Ateşspor = İzmirspor).
- **Escopo pela federação:** a liga nacional começa em 1959; os campeonatos anteriores ficam de fora (ver as pendências da
  liga). A temporada de 1959 (fevereiro a junho) tem a chave 1958 e o rótulo "1959" (`edicoes.temporada`); o
  `documentar.py` agora usa o `temporada()` de cada importador.
- **Nomes do ogol não confiáveis nas temporadas antigas:** de novo, código do ogol identificado pelos números da campanha;
  o ogol às vezes troca os códigos de dois clubes numa temporada (`OGOL_POR_ANO` em `clubes_tur.py`).
- **Troca de nomes (Kayserispor x Kayseri Erciyesspor, 2004):** segue a Wikipédia (linhagem legal).
- **Jogos dados pela federação com placar no ogol** (acidente do Samsunspor em 1989, Ankaraspor em 2009/10): marcados
  `awd` pela data (`DADOS_FORA`).
- **Correções pelo id do jogo no ogol** (`CORRECOES`), com mando: o ogol inverte mandos às vezes.
- **Analisador de placares:** testar, temporada a temporada, trocar o placar do ogol pelo das outras fontes e ver quais
  trocas fecham as tabelas (feito no scratchpad; vale virar ferramenta comum).
- **Matriz mal fechada na Wikipédia:** um bloco que não fecha engole o seguinte; leia os parâmetros de nível de cima, como o
  `wiki_tabela.resultados` (`matriz_wiki` do Turco).
- **RSSSF em UTF-16** (lista de artilheiros turca): `rsssf_tur.texto` detecta pelo BOM.

**Wikipédia, rebaixados:** a caixa de resumo do artigo ("| relegated = ...") traz a lista oficial e explica fusões e
falências. É melhor que as cores da tabela; o Holandês confere com ela. A punição às vezes vem em `startpoints_X`, e não
em `adjust_points_X` (o leitor comum lê os dois).

**football-data:** a hora é a do Reino Unido; converta para a local (o Santa Clara joga nos Açores).

**ESPN:**
- Cobertura começa em anos diferentes: 2001/02 na maioria; 2006/07 em Portugal.
- Repete eventos.
- Os gols só entram quando a soma bate com o placar.

**Desempate:** varia por país e por época. Já existem os critérios "confronto", "confronto_geral" e "confronto_fora"
(confronto direto aplicado de novo entre os que seguem empatados, com gols fora de casa; Portugal), "saldo" e "media"
(goal average). O teste por temporada escolhe o que reproduz a ordem oficial.

**Rodada:**
- A liga inglesa não tinha rodadas fixas antes de 1992/93: a rodada fica vazia (decisão do Guilherme, EN-007).
- Na Alemanha, a fase "C" do ogol tem a rodada inferida pela data.

**Eras antigas (fase final entre campeões regionais):**
- A RSSSF repete o título da seção no índice do topo da página ("Deutsche Meisterschaft", "Championship Playoff"): leia a
  partir da segunda ocorrência.
- Nas páginas alemãs, a seção da fase final acaba em duas linhas em branco; depois vêm as ligas regionais, com jogos no
  mesmo formato (não deixe o leitor continuar).
- Nota entre colchetes que continua nas linhas de baixo, à direita de outros jogos ("[Königsberg disqualified for
  fielding / ineligible goal keeper..."): o nome do visitante acaba em dois espaços; o resto é nota.
- O minuto do gol na duithist4763 vem com apóstrofo cp1252 ("17\x92").
- Clube que existe até hoje fica com o nome atual (SpVgg Fürth = Greuther Fürth, 1. SV Jena = Carl Zeiss Jena); clube
  extinto, com o nome e a cidade da época. "FSV Frankfurt" caía no Eintracht pela busca reduzida: cadastre o nome exato.
- Data: onde a Wikipédia tem a ficha da partida (football box), vale a data dela. A RSSSF erra em casos conferidos (final
  de 1941 em 22/06; Kaiserslautern com dois jogos em 03/07/1949).
- Classificação de mata-mata: campeão oficial em 1º, vice em 2º, depois a fase alcançada; na mesma fase, a posição no
  grupo e a campanha.


**Grécia, o que serve para outras ligas:**
- **Ogol só com o campeão nas temporadas antigas:** a edição existe no ogol desde 1927/28, mas os jogos só desde 1993/94.
  Testar a página de calendário de alguns anos antes de planejar a base.
- **Matriz da RSSSF x matriz da Wikipédia:** quando discordam, fica o placar que deixa os clubes mais perto das duas
  tabelas publicadas. A troca é testada jogo a jogo e em pares (placares trocados entre duas células), e, na era antiga,
  também com a matriz inteira; fica o caminho que fecha melhor (`importar.py` e `antigo.py` do `gre-1`). Cada troca fica
  anotada no jogo.
- **Células com nota na matriz da RSSSF** ("(1)", "(*)", "{1}"): o placar vem da nota, à mão (`NOTAS_MATRIZ`); "*" ou "x"
  no placar é W.O. A greve de 1986/87 tem "derrota para os dois" (0-0 `awd`).
- **Desempates que só estão nas notas da tabela da Wikipédia** ("7th place play-off: PAOK–Aris 0–0"): entram na fase
  "Desempate", sem data. Deduplicar só contra os outros desempates; a fase regular pode ter o mesmo par e o mesmo placar.
- **Sistemas de pontos que mudam:** 3-2-1 até 1972/73, 2-1-0 até 1991/92, 3-1-0 depois. Na era antiga, o sistema sai da
  tabela da RSSSF. A punição sai da tabela da Wikipédia quando ela fecha com os jogos; a diferença de pontos da RSSSF que a
  Wikipédia contradiz é erro da RSSSF.
- **"ANU" no ogol pode ter valido** (Niki Volos e OFI, 2014/15): tratar como "DA" e buscar o placar oficial.
- **Fusão no meio da história** (Chalkidona em 2004/05, que o ogol põe no Atromitos): seguir a tabela da Wikipédia
  (`OGOL_POR_ANO`).
- **Campeões do Chipre na liga grega (1967/68-1973/74):** país CYP; não contam como rebaixados.
- **`\b` em heredoc vira backspace (chr 8):** caiu de novo. Para código com regex, usar Write/Edit; conferir com
  `chr(8) in texto`.

**Tchéquia, o que serve para outras ligas:**
- **Sem ESPN nem football-data:** confira cedo se a liga existe nessas fontes (a ESPN não tem a `cze.1`).
- **Páginas de temporada da RSSSF com os autores dos gols** (Tchéquia, 1998/99 a 2011/12): "[P.Horvath 45pen, T.Janotka
  80og; P.Sultes 64]", com o mandante antes do ";". Lidas por `rsssf_cze.autores()` e casadas com o jogo do ogol pelo
  par e pelo placar; só entram quando a conta fecha. Vale olhar nas páginas de outros países.
- **Nome de 2 dígitos da RSSSF só até 2008/09:** "tsje22.html" é a Tchecoslováquia de 1922, não 2021/22.
- **Conflito de módulos entre pastas:** ao reaproveitar leitores de outro slug (`wiki_gre`, `rsssf_gre`), pôr a pasta no
  fim do `sys.path` (`append`); com `insert(0, ...)` o `edicoes.py` do outro slug passa na frente.
- **Pontos de 1993/94:** ainda 2 por vitória (a tabela da RSSSF mostra); a Wikipédia calcula com 3.
- **Nome curto ambíguo na RSSSF** ("Bohemians" sozinho em 2008/09 = Střížkov): regra por época em `POR_ANO`.
## 7. Decisões do Guilherme já tomadas

- Inglês 2025/26 incluído (EN-001).
- Wolverhampton x Everton 1888/89 = 5-0 (EN-006).
- Rodada vazia onde não havia rodadas fixas (EN-007).
- Stoke 1889/90 e Darwen 1891/92: "não reeleitos", não "rebaixados" (EN-018).
- Atlético de Madrid 1935/36 rebaixado (ES-001).
- Artilheiros do Espanhol pela contagem oficial da LFP; o Pichichi fica anotado (ES-005).

Detalhes em `docs/coleta/pedidos-europa.md`, seção "Decisões do Guilherme (21/11/2026) aplicadas".
