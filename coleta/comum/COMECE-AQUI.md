# Coleta Brasil — comece aqui

Para o agente de coleta Brasil (agente 2) que for continuar este trabalho. Leia antes o guia geral
`docs/agente-coleta-COMECE-AQUI.md`. Ele traz:
- a missão;
- onde você pode mexer;
- o formato do pacote (seção 4);
- a regra 6b dos nomes de clube.

Este arquivo diz o que já foi feito, como foi feito e de onde continuar.

Última atualização: 25/11/2026 (Gaúcho coletado; plano único de coleta e ranking da CBF na seção 3).

**Documentação completa:** `coleta/comum/documentacao/`. Tem o índice (`README.md`) e uma ficha por competição, com:
- tudo o que o pacote tem;
- fontes e regras;
- conferência com as tabelas publicadas;
- cobertura de cada campo década a década;
- formato ao longo do tempo;
- campeões, acessos, rebaixados e punições;
- todas as correções e decisões, com o motivo;
- o que não deu para coletar;
- pendências;
- arquivos e comandos para refazer do zero.

A documentação é gerada por `python coleta/comum/documentar.py` a partir dos pacotes, dos módulos de cada competição e do
banco (só leitura). Rode depois de toda importação ou correção e mantenha à mão só a lista `PENDENCIAS`, no começo do
script. Os relatórios `docs/coleta/<slug>.md` continuam com o detalhe temporada a temporada.

## 1. Regras da casa (combinadas com o Guilherme)

- **Uma competição por vez, e só com o ok dele.** Ele decidiu em 20/11/2026: não começar outro campeonato sem ele pedir.
  Ao fim de cada competição:
  - resumo curto;
  - pedido de ok para o commit;
  - recado ao agente do banco (agente 1) no fim de `docs/coleta/pedidos.md`.
- **Mexa só nas suas pastas:**
  - `coleta/<slug>/`, `coleta/comum/` e `data/coleta/<slug>/`;
  - `data/coleta/comum/` (o cadastro comum de nomes de clube);
  - `docs/coleta/<slug>.md` e `docs/coleta/pedidos.md`.

  Nunca toque em `db/`, `futebol/`, `serie_b/`, `historico/`, `gerar_dashboard_v2.py`, `painel/`, `marca/`, nem nas pastas
  dos outros agentes de coleta: `coleta/comum-europa/`, `coleta/comum-sulamerica/` e as ligas deles (`eng-1`, `arg-1`, ...).
- **Mudou `coleta/comum/`?** Rode de novo todas as coletas que usam o arquivo (C, D, Copa, Paulista, A2) e compare os
  totais antes e depois. O leitor da RSSSF e o `ogol.py` servem a todas.
- **Banco só para leitura:** `sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)`. O teste de carga usa uma cópia
  (seção 5).
- **Git:**
  - nunca `git add -A` nem `git add .`;
  - faça o commit com os caminhos na linha de comando: `git commit -F msg -- <caminho> <caminho> ...`. Outro agente
    trabalha na mesma pasta e pode estar preparando os arquivos dele ao mesmo tempo. Em 21/11 um commit meu levou os
    arquivos do Peru e do Paraguai e teve de ser refeito. Confira com `git show --stat HEAD` depois de cada commit;
  - commit e push só com o ok do Guilherme;
  - não troque de ramo;
  - a conta é a pessoal (`guicorrea93`, e-mail noreply), já configurada no repositório;
  - a mensagem de commit termina com `Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>`.
- **Logs e conferências vão para o scratchpad**, nunca soltos no repositório.
- **Nome de clube único (regra 6b):** nunca o nome exato de outro clube, seja do banco, do cadastro comum
  `data/coleta/comum/clubes_ogol.json` ou dos outros pacotes. Homônimo leva a cidade: "Palmeiras (São João da Boa Vista)",
  "Ferroviária (Botucatu)". **Nome já dado não muda mais:** o `registro.py` guarda o nome de cada código no cadastro
  comum, na primeira vez que ele é usado.
- **Clube refundado ou substituto é outro cadastro.** Pesquise caso a caso (Wikipédia, site do clube, federação, CNPJ) e
  use a data de fundação da ficha do ogol: uma ficha fundada depois da edição não vale (CL-005 a CL-012).
- **Critério nas dúvidas:** o mais fiel à história do campeonato. Pesquise na internet quando as fontes divergem e
  registre a decisão com o motivo no código e no relatório.
- **Fale com ele em português, curto e por partes.** O recado ao agente principal vai num bloco, pronto para copiar.

## 2. O que está pronto

| Competição | Temporadas | Jogos | Último commit | No banco | Teste de carga (22/11) |
|---|---|---|---|---|---|
| `bra-serie-c` Série C | 39 (1981–2026; 3 não oficiais: 1987 Azul, 1987 Branco, 2000) | 8.705 | d1a8fbb9; D-10 neste commit (24/11) | sim; recarregar (coluna `oficial`) | OK |
| `bra-serie-d` Série D | 18 (2009–2026) | 6.032 | ecafa9e; plano da revisão neste commit (24/11) | sim; recarregar | OK (Espírito Santo FC = Rive A.C. do banco) |
| `bra-copa-do-brasil` Copa do Brasil | 37 (1989–2025) | 4.010 | c4f83be; plano da revisão neste commit (24/11) | sim; recarregar | OK |
| `bra-sp-1` Paulista (1ª divisão) | 135 (1902–2026) | 21.849 | 046e6e4; Grêmio Catanduvense separado (A2-022) neste commit (24/11) | sim; recarregar | OK (1 clube novo) |
| `bra-sp-2` Paulista Série A2 | 80 (1947–1984, 1985–2026) | 9.214 | ada0940; A2-015 (parte C) neste commit (24/11); plano da A2 concluído | sim; recarregar | OK (1 clube novo) |
| `bra-rj-1` Carioca | 129 (1906–2026; ligas rivais em 1912, 1924, 1933-1937; 1979 e 1979 Especial) | 14.144 | 08d5587, e6e343d; `co_campeao` neste commit (23/11) | sim (agente 1, 23/11) | OK (o banco já tem os clubes) |
| `bra-mg-1` Mineiro | 113 (1915–2026; 1932 LMDT e 1932 AMEG) | 11.521 | be07b131 (25/11) | não; carregar | OK (64 clubes novos) |
| `bra-rs-1` Gaúcho | 106 (1919–2026; sem 1918, 1923 e 1924) | 13.393 | 3a0ffbba; nome do SE São Borja corrigido neste commit (25/11) | não; carregar | OK (105 clubes novos) |
| `bra-pr-1` Paranaense | 113 (1915–2026; 2002 e 2002 Supercampeonato, este não oficial) | 14.315 | neste commit (25/11) | não; carregar | OK (104 clubes novos) |
| `bra-serie-a-artilheiros` | 70 edições da Série A (1937–2025) | — | a65c201 | sim (o agente 1 carregou) | — |

Números por competição, sempre atualizados: `coleta/comum/documentacao/README.md`.

## 3. De onde continuar (pendências, em ordem)

**Plano único de coleta (`docs/coleta/plano-de-coleta.md`, decidido pelo Guilherme em 25/11/2026): vale acima deste
arquivo.** Para o Brasil (seção 1.2 dele):
1. primeiro **todos os estaduais de 1ª divisão** (`bra-<uf>-1`), na ordem do Ranking Nacional das Federações da CBF;
2. depois os estaduais de 2ª divisão, pelo mesmo ranking (o Paulista A3 entra aqui, depois das A2 dos outros estados);
3. depois os torneios regionais (Copa do Nordeste, Copa Verde, Rio-São Paulo, Sul-Minas...);
4. por fim, outros nacionais (Supercopa do Brasil, Copa dos Campeões...).

Uma competição por vez: pesquisa a fundo, proposta de escopo curta ao Guilherme (desde quando, que eras entram, o que a
federação reconhece), só começar com o ok dele e registrar a decisão aqui. Entrega, pacote e git: seção 2 do plano.

**Ranking Nacional das Federações (RNF) da CBF para 2026: foto de 25/11/2026, fixa** (não muda depois). Divulgado em
24/12/2025; PDF oficial:
https://stcbfsiteprdimgbrs.blob.core.windows.net/img-site/cdn/RNF_Ranking_Nacional_das_Federacoes_2026_30b87e87a3.pdf
(notícia: https://www.cbf.com.br/a-cbf/noticias/informes-cbf/a/cbf-divulga-ranking-nacional-de-clubes-e-de-federacoes-do-futebol-masculino-para-2026).
As 27 posições foram conferidas no PDF.

| Pos. | UF | Pontos | Estadual de 1ª divisão | Situação |
|---|---|---|---|---|
| 1 | SP | 93.528 | `bra-sp-1` Paulista | **pronto** (no banco) |
| 2 | RJ | 61.308 | `bra-rj-1` Carioca | **pronto** (no banco) |
| 3 | MG | 41.451 | `bra-mg-1` Mineiro | **pronto** (be07b131, 25/11; falta o agente 1 carregar) |
| 4 | RS | 39.283 | `bra-rs-1` Gaúcho | **pronto** (3a0ffbba, 25/11; falta o agente 1 carregar) |
| 5 | PR | 31.792 | `bra-pr-1` Paranaense | **pronto** (25/11; espera o ok do commit; falta o agente 1 carregar) |
| 6 | CE | 24.954 | `bra-ce-1` Cearense | **próximo** (pesquisa a fundo e proposta de escopo antes) |
| 7 | GO | 24.148 | `bra-go-1` Goiano | falta |
| 8 | SC | 23.938 | `bra-sc-1` Catarinense | falta |
| 9 | BA | 23.642 | `bra-ba-1` Baiano | falta |
| 10 | PE | 14.158 | `bra-pe-1` Pernambucano | falta |
| 11 | AL | 12.240 | `bra-al-1` Alagoano | falta |
| 12 | PA | 10.710 | `bra-pa-1` Paraense | falta |
| 13 | MT | 9.346 | `bra-mt-1` Mato-Grossense | falta |
| 14 | AM | 6.688 | `bra-am-1` Amazonense | falta |
| 15 | RN | 6.131 | `bra-rn-1` Potiguar | falta |
| 16 | PB | 5.507 | `bra-pb-1` Paraibano | falta |
| 17 | MA | 5.451 | `bra-ma-1` Maranhense | falta |
| 18 | SE | 5.082 | `bra-se-1` Sergipano | falta |
| 19 | DF | 3.633 | `bra-df-1` Brasiliense | falta |
| 20 | PI | 3.545 | `bra-pi-1` Piauiense | falta |
| 21 | ES | 2.623 | `bra-es-1` Capixaba | falta |
| 22 | TO | 2.435 | `bra-to-1` Tocantinense | falta |
| 23 | AC | 2.306 | `bra-ac-1` Acreano | falta |
| 24 | RO | 1.648 | `bra-ro-1` Rondoniense | falta |
| 25 | RR | 1.598 | `bra-rr-1` Roraimense | falta |
| 26 | MS | 1.450 | `bra-ms-1` Sul-Mato-Grossense | falta |
| 27 | AP | 1.375 | `bra-ap-1` Amapaense | falta |

Já prontos fora dos estaduais de 1ª divisão: Séries C e D, Copa do Brasil e Paulista A2 (`bra-sp-2`, que pela ordem nova
seria da etapa 2). Ao fim de cada campeonato, a seção "Recado de fim de coleta — <slug> — <data>" no fim de
`docs/coleta/pedidos.md`. Autores pela ficha do ogol e jornais da A2: só se o Guilherme pedir.

1. **Mineiro (`bra-mg-1`), Gaúcho (`bra-rs-1`) e Paranaense (`bra-pr-1`) feitos em 25/11.** Próximo: o Cearense
   (`bra-ce-1`), 6º do RNF; antes, pesquisa a fundo e proposta de escopo ao Guilherme. Em aberto com ele: o Gaúcho de
   1918 (campeões honoríficos da FGF em 2021) entra como edição sem jogos?
   **Escopo do Paranaense, aprovado pelo Guilherme em 25/11:**
   - 1915 a 2026 (todos os anos disputados; RSSSF `tablesfq/pr{ano}.htm` e ogol "campeonato-paranaense").
   - 1980: título dividido entre Colorado e Cascavel (`co_campeao`; vice = o próximo que não é campeão, D-07).
   - 2002: duas edições. "2002" é o campeonato oficial da FPF (sem os clubes da Copa Sul-Minas; campeão o Iraty) e
     "2002 Supercampeonato" (com os da Sul-Minas; campeão o Atlético) entra com `oficial` = "não" e a nota de que o
     Athletico conta o título (a lista oficial da FPF não foi achada).
   **Escopo do Gaúcho, aprovado pelo Guilherme em 25/11:**
   - 1919 a 2026, 106 edições. Ficam fora 1918, 1923 e 1924, que não foram disputados (o ogol marca 1923 e 1924 como
     "Não Disputada").
   - 1930 entra: foi organizado pela FAGET, no lugar da FRGD, e a RSSSF conta o título.
   - 1919-1960, fase por regiões: entram a fase estadual e as decisões de zona e região que a página da RSSSF traz. Os
     campeonatos das cidades e das ligas locais ficam fora (são outras competições; só davam a vaga).
   - 2026: sem página da RSSSF; os jogos vêm do ogol.
   - Fontes: RSSSF Brasil (`tablesr/rs{ano}.htm`, 1919-2025), ogol ("campeonato-gaucho", 1919-2026) e Wikipédia pt.
   - Ficam fora (etapa 4): Copa FGF, Super Copa Gaúcha e Recopa Gaúcha. O Paulista A3 (`bra-sp-3`) fica para a etapa 2 (depois de todos os estaduais de 1ª divisão e das A2 dos
   estados à frente dele). Pendências do Carioca e do Mineiro: seção 9 de `coleta/comum/documentacao/bra-rj-1.md` e
   `bra-mg-1.md`.
2. **Correções da revisão: siga `docs/revisao/plano-coleta-brasil.md`** (o Guilherme mandou começar em 23/11).
   - Feito em 23/11: o "ERRADO NO AR" do Paulista (SP-011, SP-002, SP-007, SP-008 menos 2024-2025, QS-001, QS-006, SP-010,
     QS-015, SP-013, QS-005, SP-009, SP-012 e SP-001, este com a coluna `co_campeao`). Ids e como em
     `docs/coleta/pedidos.md`, seção "Correções da revisão — bra-sp-1 — 23/11/2026".
   - Feito em 23/11: A2-002 a A2-011 e A2-017 (seção "Correções da revisão — bra-sp-2 — 23/11/2026" de
     `docs/coleta/pedidos.md`).
   - Feito em 23/11: A2-001 (as 17 edições de 1967-1978 e 1980-1984). "ERRADO NO AR" do plano concluído.
   - 24/11: o Guilherme mandou seguir o resto do plano, competição a competição. Paulista em 4 partes:
     1. jogos (feita 24/11: SP-014, QS-013, QS-009, QS-004, QS-007, SP-018, QS-002, QS-003, QS-012, SP-019 e o vice de
        1928 APEA; seção "Correções da revisão — bra-sp-1 — 24/11/2026 (parte 1: jogos)" de `docs/coleta/pedidos.md`);
     2. leitor da API da FPF (feita 24/11: QS-008, SP-008 de 2024-2025, SP-004 com 2026, SP-021 em parte;
        `coleta/bra-sp-1/baixar_fpf.py` e `fpf_sp1.py`; seção "... (parte 2: FPF e 2026)" de `docs/coleta/pedidos.md`);
     3. `pacote.py` (feita 24/11: SP-015, QS-010, SP-023, SP-024, QS-011, SP-022 e o jogo falso de 1933; seção
        "... (parte 3: pacote.py)" de `docs/coleta/pedidos.md`);
     4. pódio (feita 24/11: SP-003, SP-017, SP-026, SP-027, W.O. "dns" de 1905-1910 e 1978 lido inteiro; seção
        "... (parte 4: pódio)" de `docs/coleta/pedidos.md`). Plano do Paulista concluído; sobra só o anotado lá.
   - A2 (`bra-sp-2`), em 3 partes. Feitas 24/11: A (jogos: A2-012 a 014, 016, 019, 020, 026 a 028) e B (pódio, artilheiros,
     clubes: A2-021, 022, 024, 025; 023 fica separado pela D-23 b). Seção "Correções da revisão — bra-sp-2 — 24/11/2026" de
     `docs/coleta/pedidos.md`.
   - Feito 24/11: A2 parte C (A2-015), por correções nas páginas da A2 (`rsssf_sp2.py`), sem mexer no leitor comum. O
     marcador "[unknown]" do leitor comum zera a data (serve para blocos sem data). Plano da A2 concluído.
   - Feito 24/11: Série C (QC-002, QC-009, QC-011, QC-012, SC-016, SC-018, SC-021, CL-028 na parte da C). Datas
     corrigidas por jogo em `data/coleta/<slug>/datas_corrigidas.csv` (aplicador `coleta/comum/datas_corrigidas.py`; o
     mesmo serve à D e à Copa, já com os arquivos gerados); cidade em português por `registro.cidade_pt`.
   - Feito 24/11: Série D (QC-001, SD-011, QC-003, CL-028 na parte da D; D-03 no Espírito Santo FC). Correção de ficha
     comum a todas as coletas em `registro.FICHA_COMUM` / `registro.corrigir_ficha` (Botafogo-DF, AA Araguaia).
   - Feito 24/11: Copa do Brasil (QC-005, QC-004, CB-007 e QC-008 pela D-14 C, CB-005 anotado pela D-13, CL-028).
   - Feito 24/11: "Todas as coletas Brasil" (QC-006: as 100 datas entram nos `datas_corrigidas.csv` da C, D e Copa;
     QC-007: `observacao.TRADUCOES` e `observacao.limpar_gols_texto`, também na A2).
   - Feito 24/11: D-10 (SC-029). Série C de 1987 (Módulos Azul e Branco, duas temporadas: "1987 Azul" e "1987 Branco";
     decisão do Guilherme em 24/11: entram na C, como no Bola) e 2000 (Módulos Verde e Branco), pelo Bola n@ Área
     (`baixar_bola.py`, `bola_c.py`, `importar.montar_bola`); coluna nova `oficial` ("não") em `edicoes.csv`.
   - **Plano da revisão do Brasil (`docs/revisao/plano-coleta-brasil.md`) concluído em 24/11.** Próximo: o que o Guilherme
     mandar (o Mineiro estava na fila, seção 4).
   - Em `coleta/bra-sp-1/importar.py`, as correções por jogo usam o nome de exibição do clube (CLUBES_FORA, JOGOS_FORA,
     PONTOS_FORA_DE_CAMPO, JOGOS_EXTRA_WO, JOGO_CORRIGIDO, JOGOS_EXTRA): se um nome não casar, o importador para com erro
     (não passa calado). `RSSSF_FORA` e `JOGOS_ANULADOS` usam o nome como está na página e tiram o jogo antes do ogol.
   - Os jogos do Futebol Nacional que a revisão baixou estão em `revisao/QS/fn_jogos.json` (só leitura): 3ª opinião
     de placar e data sem baixar de novo.
   - Ao corrigir, cite os ids em `docs/coleta/pedidos.md`; a revisão confere de novo.
3. **Séries C e D e Copa:** os achados SC, SD, CB e CL foram tratados (seções "revisão ... parte 1 a 4" de
   `docs/coleta/pedidos.md`), mas `docs/revisao/achados.csv` ainda marca "aberto". Quem atualiza é a revisão; se ela
   pedir de novo, responda pelo id.
4. **Autores dos gols e cartões pelas fichas de jogo do ogol:** cerca de 8 mil pedidos (~3 h) só na Série C. Prioridade
   baixa, e cartões mais baixa ainda (decisão de 20/11). Só se ele pedir.

5. **Fique de olho em `docs/coleta/pedidos.md`:** respostas do agente 1 e pedidos novos da revisão.

## 4. Como fazer uma competição nova

Copie a competição mais parecida e adapte:
- **estadual com página da RSSSF por ano:** `bra-sp-2`, o mais completo, com edições antigas sem jogos e Wikipédia, ou
  `bra-sp-1`;
- **nacional por grupos:** `bra-serie-c` ou `bra-serie-d`;
- **copa em mata-mata:** `bra-copa-do-brasil`.

Arquivos de cada competição, em `coleta/<slug>/`:

| Arquivo | O que faz |
|---|---|
| `edicoes.py` | `SLUG`, `PASTA_DADOS`, `PACOTE`, `RELATORIO`, `TEMPORADAS`/`ANOS` e o nome oficial de cada época |
| `baixar_rsssf.py`, `baixar_ogol.py`, `baixar_ogol_clubes.py`, `baixar_espn_wiki.py` | uma fonte cada; gravam em `data/coleta/<slug>/<fonte>/`. Educados: espera entre pedidos e cache, sem baixar de novo |
| `rsssf_<x>.py` | configura o leitor comum (`rsssf.PASTA`, `rsssf.MODELO = "sp{ano}l2.htm"`) e registra as correções de cada página em `rsssf.CORRECOES[arquivo]` (regex ou função, com o motivo) |
| `clubes_<x>.py` | identidade: ficha do ogol -> nome de exibição (do banco, do cadastro comum ou novo); `MANUAL_DB`, `MANUAL_NOVO`, `FICHA_CORRIGIDA`, `sem_ogol()` para os clubes que só a RSSSF tem |
| `importar.py` | junta RSSSF e ogol (e ESPN e Wikipédia, quando há), casa os nomes, confere com as tabelas publicadas, monta a classificação e grava o pacote e o relatório. Os dicionários de decisões ficam no topo |
| `pacote.py` | grava os CSV do pacote (formato do guia geral, seção 4) e o relatório |
| `explicacoes.py` | textos do relatório: `INTRO` (temporadas, fontes, regras), `EXPLICACOES` por temporada, `FIM` (identidade e o que não deu) |

Código comum em `coleta/comum/`:

| Arquivo | O que faz |
|---|---|
| `rsssf.py` | leitor das páginas da RSSSF Brasil: jogos, fases, grupos, tabelas e conferência; `texto()` aplica as `CORRECOES` |
| `ogol.py` | `calendario()`, `edicoes()` e fichas de clube; valida o link canônico e espera quando o ogol limita os pedidos |
| `gols.py` | lê os autores dos gols da RSSSF; só entram quando a soma bate com o placar |
| `registro.py` | cadastro comum `data/coleta/comum/clubes_ogol.json`: código -> nome, que não muda mais |
| `observacao.py` | `obs_pt`: tradução das notas da RSSSF |
| `wiki.py`, `wikipedia.py`, `espn.py`, `baixar.py` | Wikipédia (infobox, punições), ESPN e download educado |
| `documentar.py`, `testar_carga.py` | documentação e teste de carga |

Passos:

1. **Ver as fontes:** a lista de campeões e de participantes da RSSSF, as páginas por ano, a competição no ogol (o código
   e desde quando há calendário) e a Wikipédia pt de cada edição.
2. **Escrever** `edicoes.py` e os `baixar_*.py` e baixar tudo, com os logs no scratchpad.
3. **Escrever `rsssf_<x>.py`** e rodar `python coleta/<slug>/rsssf_<x>.py` até cada página dar os jogos certos e "0
   divergências". As correções vão em `CORRECOES`, com o motivo.
4. **Identidade:** pelo ogol, quando há calendário. Sem ele, pela cidade da lista de participantes e pela fundação da
   ficha. Confira a unicidade dos nomes (regra 6b).
5. **`importar.py`:** comece com `python coleta/<slug>/importar.py <ano>` (só mostra) e depois rode sem ano (grava).
   - Toda divergência com a tabela publicada vira correção ou explicação.
   - O campeão é conferido com a lista oficial.
6. **Teste de carga** (seção 5) e recado em `docs/coleta/pedidos.md`.
7. **Documentação:** ponha a competição em `COMPETICOES` e `PENDENCIAS` no `documentar.py`, rode e atualize este arquivo.
8. **Commit:** peça o ok. A documentação vai no mesmo commit da competição.

## 5. Teste de carga

```
python coleta/comum/testar_carga.py <slug> <pasta temporária (o scratchpad)>
```

Deve terminar com `<slug>: N edições, N jogos, N clubes novos -> OK`. O aviso "tabela por rodada ignorada em ... com
mais de uma fase" (Paulista 1996 e 1997, A2 1996 e 2013) é do carregador e já é conhecido.

## 6. Armadilhas já encontradas

**ogol**
- **Limite de pedidos:** quando o ogol limita, devolve a página de outra competição ou de outro clube, com cara de certa.
  O `ogol.py` só aceita a página cujo `rel="canonical"` é o calendário daquela edição (ou a ficha daquele clube) e espera
  60 s, 120 s... antes de tentar de novo. Calendário com 0 jogos, baixe de novo.
- **Jogo à noite:** às vezes o ogol dá o dia seguinte; vale a data da RSSSF.
- **Mesmo código para clubes diferentes:** o ogol liga um clube antigo ao novo do mesmo nome (Matsubara de 1981 no J.
  Malucelli) ou troca um clube num jogo. Corrija em `CORRIGE_OGOL` e `CORRIGE_OGOL_JOGO`.
- **Fichas:** algumas têm a cidade errada (`FICHA_CORRIGIDA`) ou a fundação de outro clube.
- **Paulista A2:** só tem jogos de 1998 em diante (1948, 1950, 1988 e 1989 têm 1 a 4 jogos soltos).

**RSSSF Brasil**
- **Formatos que variam de página para página:**
  - duas colunas (1998-1999 na A2, jogos do campeão nos anos 1950);
  - jogos em quadros (1997);
  - a data na frente do jogo;
  - nomes quebrados em duas linhas (2014, 2022-2024);
  - letras trocadas por "�" (2000-2003);
  - `<br>` com atributos em outra linha (A2 2021).

  Tudo isso é corrigido em `rsssf_<x>.py`.
- **Páginas que param no meio:** Série C 2019, Série D 2021, Paulista 2025. Use `BASE_OGOL` (o ogol vira a base) ou
  `TABELAS_PARCIAIS` (a tabela não serve de conferência).
- **Erros da própria página:**
  - "Campeão: Lemense" na A2 1991 (o campeão é o Araçatuba);
  - a cidade da Internacional na A2 1948;
  - a tabela calculada dos jogos ao lado da oficial (A2 1954).

  Confira o campeão na lista `*camp.htm` e, na dúvida, na Wikipédia pt.
- **Jogos sem placar:** às vezes vêm só com quem venceu ("venceu", "empatou"): A2 1988, 69 jogos. Ficam fora.
- **Anos com duas ligas:** Paulista 1913-1926, LPF e APEA. São duas edições (`rsssf_sp1.LIGAS`).
- **Edições antigas da A2 (1947-1966):** só os pontos por grupo. A cidade de cada clube vem da própria tabela ou da
  lista de participantes (`sp2list.htm`).

**Wikipédia pt**
- Tem as finais e as fases finais de muitas edições antigas e as edições que a RSSSF não tem (A2 1965 e 1990).
- Jogos só com "V/E/D" ficam fora.
- Data sem ano: é o ano da edição.
- Os jogos transcritos estão em `data/coleta/bra-sp-2/wikipedia/jogos_pt.csv`, cada um conferido no código da página
  (`pt_<ano>.wiki`).

**Carioca (o que valeu aprender)**
- **Tags de bloco:** as páginas do Rio põem o título de cada liga e o primeiro jogo dentro de `<P>`/`<PRE>` sem `<br>`;
  `rsssf.QUEBRA_BLOCOS = True` (opção do leitor comum, desligada nas outras coletas) quebra a linha nessas tags.
- **Súmulas em caixa alta** ("BOTAFOGO 4 x 2 FLUMINENSE", com "Data - / Local - / Árbitro -"): repetem o jogo decisivo da
  lista e saíam em dobro; `rsssf_rj1.sem_sumulas` tira a súmula quando há o mesmo jogo em letra normal.
- **Local do jogo entre parênteses** no fim da linha ("Bangu 0 x 5 América (Rua Ferrer).") entrava no nome do visitante e
  criava clubes falsos; `_linha_de_jogo` vira nota. "Fluminense (Nova Friburgo)" perdia a cidade e virava o Fluminense.
- **W.O. sem vencedor no ogol** (anos antigos): o vencedor sai da tabela publicada (`importar.wo_do_ogol`).
- **ogol lento:** com uma frente só, ~4 min por edição. Rode várias frentes em paralelo, cada uma com as suas temporadas e
  sem sobreposição (`baixar_ogol.py <temporadas> --sem-fichas`), e as fichas dos clubes numa rodada só no fim
  (`baixar_ogol.py clubes`). 8 frentes baixaram ~65 edições em ~30 min. Temporada que volta vazia: rode de novo.
- **Cadastro comum durante os testes:** cada importação grava os nomes novos em `clubes_ogol.json`; limpe as entradas da
  competição antes da rodada final (tirar as que só têm o slug dela) para não fixar nome errado.

**Mineiro (o que valeu aprender)**
- **Fases sem palavra de fase:** "LEAGUE", "Qualification Tournament", "RELEGATION TOURNAMENT" e os desempates ("League
  tiebreak", "Tie-breaking") não viravam título; `rsssf_mg1` acrescenta "tournament", "^league$" e "tie-?break" ao
  `rsssf.FASE` só no Mineiro. O nome em português de cada fase estranha fica em `rsssf_mg1.FASE_ANO` (temporada ->
  nome na página -> fase), e o importador aceita direto o nome que já está em `ORDEM`; fase sem ordem vira AVISO no log.
- **Torneio de classificação** (1921, 1958-1959, 1970-1973): "Fase classificatória" (ordem 0.5). Os pontos dela (e do
  torneio de rebaixamento) não entram no desempate da classificação final (1921: o Luzitano passava o Atlético, vice).
- **W.O.:** nas páginas mineiras o "WO" marca quem faltou ("Atlético 1-WO Calafate" = vitória do Atlético), ao contrário
  do leitor comum; `_wo` vira "awd ... [victory awarded to X]". "A bt B" (1917, 1922) é vitória sem placar conhecido;
  o ogol inventa 1-0 e o importador não pega placar do ogol para W.O. Saída: "awd", sem gols, vencedor na observação.
- **Anulados e cancelados** ("[annulled]", "[cancelled]", 1918-1942): saem na leitura (`rsssf_mg1.ANULADOS`) e o jogo
  igual do ogol (mesma data e placar) sai junto; o mesmo vale para `RSSSF_FORA` e `JOGOS_ANULADOS` (1923, 1936).
- **Repescagem contra o campeão da 2ª divisão:** sai e vai para a observação da edição (D-04 a), automaticamente
  (`importar.repescagem_fora`: clube que só aparece no torneio de rebaixamento).
- **Torneios à parte:** os Torneios Paralelos de 1976 (na página) e o Troféu Inconfidência de 2020-2026 (só no ogol)
  ficam fora (`ANOS_A_PARTE`); a disputa do 3º lugar de 2022 (só no ogol) entra como "Disputa do 3º lugar".
- **Datas:** o leitor comum só vira o ano de dezembro para janeiro-março quando o ano corrente é o da temporada; página
  que começa no ano anterior (1973) precisa da data numérica ("25/03/1973"), que fixa o ano sem a virada.
- **Linha de tabela sem posição** ("  .Renascença", empate) e "Att: 535" (público com A maiúsculo) precisam de
  correção no Mineiro (`_empatados` e a troca para "att:").
- **ogol com duas fichas para o mesmo clube** (Pedro Leopoldo FC/AE Pedro Leopoldo, Flamengo de Varginha):
  `CORRIGE_OGOL` por temporada, conferido na lista de participantes da RSSSF. Fichas com cidade de outro clube:
  `registro.FICHA_COMUM` (Nacional-MG de Nova Serrana, Grêmio Calafate de Belo Horizonte).

**Gaúcho (o que valeu aprender)**
- **Páginas de cada época com um formato:** datas "09 Oct" sem colchete (até 1960), "10-Abr-1960" e "22-Jan-61" com
  vários jogos na mesma linha, "26/02/89-" em duas colunas com placar "1x2", "[Fev 27]São Luiz" colado, "Jan 19"
  sozinho na linha (2013); prorrogação numa linha "Prorrogação: Gaúcho 2-0" (soma no placar, os 90 minutos na nota) e
  pênaltis "Pk: Cruzeiro 5-4". Tudo em `rsssf_rs1.py`, uma função por formato.
- **Texto escaneado (anos 1960-1990):** grafias como "AIIÚIORÉ", "GREMIQ" e "INTERNACfONAL(SM)" em
  `rsssf_rs1.GRAFIAS` / `INTER_SM`.
- **Sem ogol de 1925 a 1976:** a identidade sai de `importar.NOME_CODIGO` (nome -> clube, todas as temporadas) e
  `NOME_ANO` (nome ambíguo por época: "Riograndense" de Rio Grande até 1960 e de Santa Maria depois; "Guarany" de Bagé,
  menos 1943). As duas tabelas valem ANTES do casamento pelo ogol (senão "Grêmio/SL" vira o Grêmio).
- **Código "rs-" de clube só da RSSSF** leva o slug ("rs-rs1-..."): o cadastro comum já tinha "rs-cruzeiro" (um Cruzeiro
  de SP, da A2) e o Gaúcho herdava o nome. Antes de cada rodada de teste, limpe as entradas novas do cadastro.
- **Parênteses de cidade com 3-4 letras ou minúsculas** ("BRASIL(PEL)", "Grêmio(sl)") viram "/PEL", "/SL": o leitor
  comum tira o parêntese do fim do nome e dois clubes viravam um só.
- **Mesmo nome para os dois clubes do jogo** ("Inter 2-3 Inter"): vale o jogo do ogol de mesma data e placar.
- **Nome firme:** nome igual ao de um só clube do calendário não troca por voto de placar e data (1977: datas da página
  uma semana antes das do ogol).
- **Ficha do ogol mais nova que o jogo** (Santo Ângelo de 1989, AE São Borja de 2009): `CORRIGE_OGOL` por temporada
  manda para o clube antigo (AE Santo Ângelo; SE São Borja, 241325).
- **Conferência de nomes antes do commit:** nenhum nome com dois códigos no cadastro comum (achou o "Palmeiras-MG" duplo
  do Mineiro, corrigido em `bra-mg-1/importar.NOME_MANUAL`).

**Paranaense (o que valeu aprender)**
- **Mais formatos de página:** "[12/mai]" e "29-abr" (mês em português), "13.03.1938" na linha, placar "2×1" e
  ", em Curitiba" depois do jogo (fase estadual de 1935-1941), "W-O" sem vencedor, vários jogos por linha com a data
  "[May 22]" (1932), placar depois de cada nome (1994), planilhas de 2026. Tudo em `rsssf_pr1.py` (`_POR_PAGINA`: as
  listas da mesma página se somam).
- **Notas grudadas no nome** ("Londrina Played in Rolândia", "Esperança It did not finish", o estádio na coluna do
  nome): `rsssf_pr1.NOTA_NO_NOME`. Nome quebrado em duas linhas ("Foz do" / "Iguaçu", 1995): correção da página.
- **`FASE_ANO` com "fase|grupo":** as duas ligas de 1916 (APSA e LSP), as zonas de 1963, os grupos de 1977 e 1995.
  Fases em inglês e títulos de rodada ("1ª RODADA - 2ª FASE", 2022) mapeados ano a ano; nenhum AVISO de fase sobrou.
- **Fase estadual depois do campeonato de Curitiba** (1935-1941): turnos da cidade, "Primeira fase - Final" (a final da
  cidade) e depois quartas/semifinal/final com os campeões das ligas do interior. Sem isso o vice saía errado.
- **`NOME_ANO` não pode vazar para outras temporadas:** o nome casado à mão só para uns anos ("Comercial" = Palestra
  Itália em 1943-1945) não entra em `JA_CASADOS`; e o nome-base sem sigla ("Paraná" de "Paraná SC") só entra quando o
  nome não está em `NOME_CODIGO`.
- **Clube de outra coleta que o ogol desta coleta não lista** (Maringá FC 1995, Pinheiros, Colorado, Matsubara, Batel,
  Cascavel EC): `clubes_<x>.DE_OUTRAS_COLETAS` traz a ficha do cadastro comum. Sem isso o nome de exibição saía o código
  ("241325" no Gaúcho; corrigido neste commit).
- **Confira o cadastro comum por UF antes de criar clube "rs-":** o Colorado, o Matsubara, o Batel, o Cascavel EC e o
  EC Pinheiros já estavam lá pela Série C. Homônimos da mesma UF não ganham "-UF": "Cascavel CR", "Galo Maringá 2020" e
  "Foz do Iguaçu EC" vão em `MANUAL_NOVO`.
- **Jogo só do ogol no mata-mata** (2020, 2026): vale o código de fase do ogol (QF, SF, F) antes da "fase em que os dois
  já se cruzaram"; final de turno (2018) é a "F" logo depois da semifinal do turno.
- **Final do Interior** (2015 e 2016): título à parte, fora do pacote (`A_PARTE`), como o Troféu do Interior do Gaúcho.

**Identidade**
- **Nomes curtos ambíguos:** "Corinthians" (Presidente Prudente ou Santo André), "Ferroviária" (Araraquara, Botucatu,
  Assis), "São Bento" (Sorocaba ou Marília), "Paulista" (Jundiaí ou Araraquara). Use a cidade; sem ela, casamento à mão
  (`NOME_MANUAL`, `NOME_WIKI`).
- **Times B e II:** ficam fora do casamento pela cidade.
- **Clubes que o ogol não tem:** viram `rs-<nome>-<cidade>`. Um clube novo homônimo de outro também criado na mesma
  rodada pode ficar com o nome sem cidade: confira os novos no cadastro comum depois de cada rodada e ponha o nome em
  `MANUAL_NOVO`.
- **Sobras no cadastro comum:** rodadas intermediárias podem deixar entradas sem uso em `clubes_ogol.json`. Antes do
  commit, compare com o `clubes.csv` do pacote e tire as que sobraram; nenhum nome já existente pode mudar.

## 7. Decisões do Guilherme já tomadas

- **Novorizontino:** separado. "GE Novorizontino" (1973-1999) e "Novorizontino" (Grêmio Novorizontino, 2010) (20/11).
- **São Paulo da Floresta:** um clube só com o São Paulo de hoje; o título de 1931 é dele (20/11).
- **Prioridades:** autores dos gols com prioridade baixa; cartões, mais baixa ainda (20/11).
- **Não começar outra competição sem ele pedir** (20/11).
- **Identidade CL-005 a CL-012:** seguir as recomendações da pesquisa; clube refundado é outro cadastro (21/11).
- **Sufixo "-UF" (CL-027):** os nomes ficam como estão (21/11).
- **Edições de 2026 da C, da D e da A2:** entram, pelo ogol (21/11).
- **Prioridade (22/11, pelo agente 1):** coletar Carioca, Mineiro, Gaúcho e A3; revisão só quando ele mandar, seguindo o
  plano da revisão.
- **Carioca 1907 e 1937 (23/11):** valem os títulos que a FERJ reconhece. 1907: Fluminense e Botafogo campeões (título
  dividido, FERJ 1996), o Botafogo em `co_campeao` (D-07). 1937: além da LFRJ (Fluminense), a edição
  "1937 FMD" (torneio inacabado, 26 jogos) com o São Cristóvão campeão (FERJ, dezembro de 2023).
- **São José dos Campos (23/11, D-23c revista):** o "Esporte Clube São José" (1933) só mudou de nome para "São José
  Esporte Clube" em 24/12/1976; é um clube só (São José-SP, 9638), com os títulos da A2 de 1972 e 1980.
- **Título dividido (D-07, formato do agente 1, 23/11):** coluna `co_campeao` em `edicoes.csv`, logo depois de `vice`;
  `campeao` é o 1º da classificação; `vice` é o próximo que não é campeão (pode ficar vazio). Paulista 1973, Carioca 1907.
- **Mineiro (24/11):** "se já fez o commit e push, pode seguir" — Mineiro coletado em 25/11, espera o ok do commit.
- **Paulista A2:** incluir tudo o que existir, inclusive as edições sem jogos e as incompletas (21/11). O que só existe em
  jornal escaneado fica de fora.

Detalhes e respostas do agente 1 em `docs/coleta/pedidos.md`.
