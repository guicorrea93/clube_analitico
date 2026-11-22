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

## 2. O que está pronto

Todos os pacotes abaixo estão no GitHub, passaram no teste de carga e têm relatório em `docs/coleta/<slug>.md`.

| Liga | Temporadas | Jogos | Gols c/ autor | Cartões | Clubes | Último commit |
|---|---|---|---|---|---|---|
| `eng-1` Inglês | 127 (1888/89–2025/26) | 51.330 | 25.841 | 33.166 | 65 | 103ccf1 |
| `esp-1` Espanhol | 95 (1928/29–2025/26) | 27.716 | 25.072 | 51.662 | 63 | (2025/26: ver git log) |
| `ita-1` Italiano | 95 (1929/30–2025/26) | 29.244 | 24.564 | 43.962 | 69 | (2025/26: ver git log) |
| `ger-1` Alemão (Bundesliga) | 63 (1963/64–2025/26) | 19.220 | 22.512 | 30.251 | 58 | (2025/26: ver git log) |
| `fra-1` Francês | 88 (1932/33–2025/26) | 30.466 | 22.613 | 35.434 | 76 | 469f615 |
| `por-1` Português | 92 (1934/35–2025/26) | 20.978 | 13.874 | 30.915 | 73 | c0ddbdd |

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

1. **EN-016 (revisão, baixa):** 12 jogos do Inglês (2002/03 a 2016/17) sem nenhum gol com autor; a ESPN não fecha nesses
   jogos. Precisa de outra fonte jogo a jogo (ficha do ogol, 11v11). É o único achado da revisão ainda aberto para a coleta
   Europa. Os outros estão corrigidos ou foram marcados `nao-e-erro` (`docs/revisao/achados.csv`, `quem_corrige` =
   `coleta-europa`).
2. **Próxima liga: `ned-1` (Holanda), só quando o Guilherme mandar.** Depois Escócia, Bélgica e Turquia (guia geral).
   Fontes já vistas para a Holanda:
   - engsoccerdata `holland.csv`, 1ª divisão de 1956/57 a 2024/25 sem buracos;
   - football-data `N1.csv`;
   - ESPN `ned.1`.

   Falta achar o código da competição no ogol (veja a seção 4).
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
`bundesliga`, `campeonato-frances`, `campeonato-portugues`. Para achar um novo, teste
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

## 7. Decisões do Guilherme já tomadas

- Inglês 2025/26 incluído (EN-001).
- Wolverhampton x Everton 1888/89 = 5-0 (EN-006).
- Rodada vazia onde não havia rodadas fixas (EN-007).
- Stoke 1889/90 e Darwen 1891/92: "não reeleitos", não "rebaixados" (EN-018).
- Atlético de Madrid 1935/36 rebaixado (ES-001).
- Artilheiros do Espanhol pela contagem oficial da LFP; o Pichichi fica anotado (ES-005).

Detalhes em `docs/coleta/pedidos-europa.md`, seção "Decisões do Guilherme (21/11/2026) aplicadas".
