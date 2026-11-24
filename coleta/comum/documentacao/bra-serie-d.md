# Campeonato Brasileiro Série D (`bra-serie-d`) — documentação

Gerado por `python coleta/comum/documentar.py` a partir do pacote `data/coleta/bra-serie-d/pacote/` e dos módulos de `coleta/bra-serie-d/`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/bra-serie-d.md`.

## 1. O que temos

- **Edições:** 18, de 2009 a 2026.
- **Jogos:** 6032; **gols:** 14542; **gols com autor:** 11227 (77%); **cartões:** 0.
- **Clubes:** 333; **artilheiros:** 18 temporadas com artilheiro (23 linhas, com empates).
- **Classificação final:** 18 temporadas; **rodada a rodada:** 0 temporadas.
- **Tabelas publicadas guardadas para conferência:** 1541 linhas.
- **No banco (`db/futebol.db`):** sim (18 edições, 6032 jogos).
- **Observação da competição:** Quarta divisão nacional, disputada desde 2009.

## 2. Fontes e regras

**Fontes:** RSSSF Brasil (`br{ano}l4.htm`: base de jogos, fases, grupos, datas e autores; as tabelas publicadas são a conferência); ogol (calendário de todas as edições e o código de cada clube, que dá a identidade; completa os jogos que faltam na RSSSF); Wikipédia (punições de pontos, lista de campeões, promovidos e artilheiros). A ESPN não tem a Série D.

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela, fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` usa o nome de lá; clube que já apareceu na Série C usa o mesmo nome do pacote da Série C (cadastro comum `data/coleta/comum/clubes_ogol.json`).

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF): 431 tabelas fecham com os jogos e 4 divergem (cada divergência é explicada no relatório, na temporada).
- Temporadas com alguma tabela divergente: 2009, 2010, 2024.
- Temporadas sem tabela para conferir: 2021, 2023, 2026.
- Temporadas com menos jogos do que o ogol: nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|
| 2000s | 158 | 100% | 100% | 72% | 0% | 0% | 0% | 91% | 0.0 |
| 2010s | 2188 | 100% | 99% | 57% | 0% | 0% | 0% | 88% | 0.0 |
| 2020s | 3686 | 100% | 100% | 51% | 0% | 0% | 0% | 70% | 0.0 |

**Fonte de cada jogo:** RSSSF Brasil: 4929; ogol: 1103.

## 5. Formato ao longo do tempo

**Número de clubes:**

- 2009: 39 clubes
- 2010 a 2013: 40 clubes
- 2014: 41 clubes
- 2015: 40 clubes
- 2016 a 2021: 68 clubes
- 2022 a 2025: 64 clubes
- 2026: 96 clubes

**Pontos por vitória:**

- 2009 a 2026: 3

**Nome oficial:**

- 2009 a 2026: Campeonato Brasileiro Série D

**Formato de cada edição** (fases na ordem; grupos; mata-mata):

- 2009 a 2010: 10 grupos + mata-mata
- 2011 a 2015: 8 grupos + mata-mata
- 2016 a 2019: 17 grupos + mata-mata
- 2020 a 2021: mata-mata + 8 grupos + mata-mata
- 2022 a 2025: 8 grupos + mata-mata
- 2026: 16 grupos + mata-mata

**Fases que aparecem** (número de temporadas): Primeira fase (18); Quartas de final (18); Semifinal (18); Final (18); Oitavas de final (16); Segunda fase (13); Terceira fase (3); Fase preliminar (2); Repescagem (1).

**Observações das edições:**

- nenhuma

## 6. Campeões, acessos, rebaixados e punições

**Títulos:**

- Ferroviário-CE: 2
- São Raimundo-PA: 1
- Guarany: 1
- Tupi: 1
- Sampaio Corrêa: 1
- Botafogo-PB: 1
- Tombense: 1
- Botafogo-SP: 1
- Volta Redonda: 1
- Operário-PR: 1
- Brusque: 1
- Mirassol: 1
- Aparecidense: 1
- América-RN: 1
- Retrô FC: 1
- Barra-SC: 1
- Uberlândia: 1

**Acessos:** 57 no total; quem mais teve: Santa Cruz (2), Treze (2), ABC (2), Macaé (1), Chapecoense (1), Alecrim (1), Madureira (1), Araguaína (1).

**Rebaixamentos:** nenhum marcado no pacote.

**Punições em pontos:**

- 2009: Araguaia -6
- 2009: Naviraiense -6
- 2010: América-AM -10
- 2012: Comercial-PI -3
- 2012: Santos-AP -3
- 2013: Paragominas -6
- 2014: River-PI -4
- 2014: Villa Nova-MG -14
- 2015: Colo Colo-BA -3
- 2015: Santos-AP -3
- 2015: Náutico-RR -4
- 2016: Baré -4
- 2017: São Raimundo-PA -3
- 2017: Itabaiana -3
- 2019: Bahia de Feira -3
- 2025: Maracanã -3

## 7. Correções e decisões (com o motivo)

Registradas nos módulos de `coleta/bra-serie-d/`; cada uma também aparece no relatório, na temporada.

### Temporadas com o ogol como base dos jogos (`importar.BASE_OGOL`)

- **2026:** a RSSSF ainda não tem a página de 2026: a base dos jogos é o ogol (revisão SD-001)

### Tabelas publicadas parciais (fora da conferência) (`importar.TABELAS_PARCIAIS`)

- **2021:** a página da RSSSF parou na 3ª rodada da 1ª fase (103 dos 518 jogos); as tabelas dela são parciais e não servem de conferência; os jogos que faltam vêm do ogol

### Jogos anulados (`importar.JOGOS_ANULADOS`)

- **2011 · Anapolina · Tocantinópolis · 4 · 1:** 1ª fase: anulado pelo STJD (o Tocantinópolis terminou com 6 jogadores); o jogo foi refeito em 17/10 (6-1), e a tabela do grupo A5 conta só o novo jogo
- **2011 · Itumbiara · Villa Nova · 3 · 1:** 2ª fase: jogado em 25/09 e anulado depois que o jogo Anapolina x Tocantinópolis da 1ª fase foi refeito (nota da página da RSSSF)

### Jogos corrigidos (placar, data, mando) (`importar.CORRECAO_JOGO`)

- **2013 · Botafogo-PB · Salgueiro · 2013-09-06:** [data=2013-10-06] volta da semifinal em 06/10 (súmula da CBF, jogo 186; Bola e transfermarkt; revisão SD-011)
- **2011 · Oeste · Cianorte · 2011-09-30:** [pm=4, pv=3] pênaltis 4-3 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2011 · Mirassol · Oeste · 2011-10-16:** [pm=3, pv=4] pênaltis 3-4 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2012 · Cianorte · Mogi Mirim · 2012-09-23:** [pm=2, pv=4] pênaltis 2-4 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2014 · Rio Branco-AC · Anapolina · 2014-10-04:** [pm=12, pv=13] pênaltis 12-13 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2020 · Bragantino-PA · Juventude-MA · 2020-12-12:** [pm=3, pv=4] pênaltis 3-4 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2020 · Mirassol · Caxias · 2020-12-13:** [pm=3, pv=0] pênaltis 3-0 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2020 · Fast-AM · Moto Club · 2020-12-13:** [pm=6, pv=5] pênaltis 6-5 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2020 · Fast-AM · Globo FC · 2020-12-26:** [pm=6, pv=5] pênaltis 6-5 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2020 · Altos · Salgueiro · 2020-12-27:** [pm=4, pv=2] pênaltis 4-2 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2021 · Campinense · Sergipe · 2021-09-18:** [pm=4, pv=2] pênaltis 4-2 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2021 · Joinville · Bangu · 2021-09-18:** [pm=4, pv=3] pênaltis 4-3 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2021 · Santo André · Esportivo-RS · 2021-09-18:** [pm=4, pv=5] pênaltis 4-5 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2021 · Juazeirense · Atlético Cearense · 2021-09-18:** [pm=3, pv=5] pênaltis 3-5 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2021 · Portuguesa · Caxias · 2021-09-18:** [pm=1, pv=4] pênaltis 1-4 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2021 · Joinville · Uberlândia · 2021-10-02:** [pm=1, pv=3] pênaltis 1-3 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2021 · Campinense · América-RN · 2021-10-16:** [pm=4, pv=2] pênaltis 4-2 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2021 · Ferroviária-SP · Atlético Cearense · 2021-10-17:** [pm=3, pv=4] pênaltis 3-4 (Bola n@ Área e transfermarkt; revisão QC-001)
- **2024 · Princesa · Manaus FC · 2024-05-11:** [gm=3, gv=3] ogol e Wikipédia: 3-3 (revisão SD-010)
- **2016 · CSA · Volta Redonda · 2016-09-29:** [data=2016-09-25] a ida da final foi em 25/09 (borderô da CBF; revisão SD-012)
- **2014 · Itaporã · Villa Nova-MG · 2014-09-07:** [especial=w.o.] W.O.: o Itaporã abandonou a competição (revisão SD-013)
- **2014 · Anapolina · Itaporã · 2014-09-21:** [especial=w.o.] W.O.: o Itaporã abandonou a competição (revisão SD-013)
- **2014 · Barueri · CEOV Operário · 2014-08-15:** [especial=w.o.] W.O. (revisão SD-013)

### Punições em pontos (`importar.AJUSTE_MANUAL`)

- **2009:** Araguaia → -6; Naviraiense → -6
- **2010:** América-AM → -10
- **2012:** Comercial-PI → -3; Santos-AP → -3
- **2013:** Paragominas → -6
- **2014:** River-PI → -4; Villa Nova-MG → -14
- **2015:** Náutico-RR → -4; Santos-AP → -3
- **2017:** São Raimundo-PA → -3
- **2019:** Bahia de Feira → -3
- **2025:** Maracanã → -3

### Punições que não valem (`importar.AJUSTE_FORA`)

- **2017 · São Raimundo:** é o São Raimundo-PA, e não o -RR (revisão SD-015)
- **2025 · Maracanã:** é o Maracanã (CE), e não o Maricá (revisão SD-016)

### Ocorrências explicadas, por temporada (`explicacoes.EXPLICACOES`)

- **2026:** a RSSSF ainda não tem a página de 2026: os jogos, as fases e os grupos vêm do ogol (revisão SD-001). Os perdedores das quartas jogaram uma repescagem pelas duas últimas vagas de acesso (Nacional-AM e Goiatuba subiram). Sem autores de gols
- **2011:** dois jogos da página foram anulados e ficam de fora (motivo abaixo); com isso, jogos e tabelas batem com o ogol
- **2012:** a página da RSSSF não traz os autores dos gols
- **2016:** as tabelas desta página (e de 2017 a 2019) têm uma coluna a mais ('PTS J PE V E D'); o leitor reconhece essa ordem
- **2020:** a página da RSSSF parou no meio da 2ª fase (472 dos 518 jogos); o resto vem do ogol
- **2021:** clubes, grupos e jogos que faltam vêm do ogol; os autores dos gols só existem nos 103 jogos da página
- **2023:** a página da RSSSF não publica tabelas e parou antes do fim (478 dos 510 jogos): conferência só pelo ogol, que tem o mesmo placar em todos os jogos em comum

### Clube do ogol casado à mão com o nome do banco (`clubes_d.MANUAL_DB`)

- **3333:** [J.Malucelli] o ogol escreve 'JMalucelli'; é o J. Malucelli do banco (Série A 2000)
- **24836:** [Novorizontino] Grêmio Novorizontino (2010-); o banco separou o GE Novorizontino (1973-1999) em 20/11/2026

### Nome de exibição de clube novo, dado à mão (`clubes_d.MANUAL_NOVO`)

- **35176:** [Espírito Santo FC] Espírito Santo FC, de Alegre: jogou a Série D (2016-2018) com este nome (ogol e RSSSF); "Rive A.C." é nome posterior. Nome da época no cadastro (decisão D-03)
- **68358:** [Corinthians Prudente] EC Corinthians de Presidente Prudente (1996): não é o Corinthians paulistano do banco
- **45210:** [Maringá] Maringá FC fundado em 2010 (Série D 2025): não é o GE Maringá do banco
- **241210:** [Maringá FC 1995] Maringá FC fundado em 1995 (Série D 1997): outro clube, nome como no ogol
- **60858:** [GE Novorizontino] Grêmio Esportivo Novorizontino (1973-1999, campeão de 1994): outro clube; o 'Novorizontino' do banco fica com o Grêmio Novorizontino, fundado em 2010 (decisão do Guilherme, 20/11/2026)
- **20122:** [Linhares EC] dois clubes de Linhares-ES: o EC (anos 1990) e o FC (anos 2000); o sufixo já distingue
- **9783:** [Linhares FC] dois clubes de Linhares-ES: o EC (anos 1990) e o FC (anos 2000); o sufixo já distingue

### Páginas da RSSSF corrigidas na leitura (`rsssf.CORRECOES`, registradas em `coleta/bra-serie-d/rsssf_*.py`)

- **br2013l4.htm:** pênaltis em linha própria, colada no título seguinte ('PK: 4-3  GRUPO B')
- **br2014l4.htm:** pênaltis em linha própria, colada no título seguinte ('PK: 4-3  GRUPO B')
- **br2015l4.htm:** pênaltis em linha própria, colada no título seguinte ('PK: 4-3  GRUPO B')
- **br2023l4.htm:** pênaltis em linha própria, colada no título seguinte ('PK: 4-3  GRUPO B')

## 8. O que não deu para coletar

- **Cartões:** nenhuma das fontes lidas traz cartões da Série D. O ogol tem na página de cada jogo (fica para depois, se aprovado).
- **Autores dos gols:** só onde a RSSSF traz e a soma fecha com o placar.
- **Hora, estádio e público:** a ESPN não tem a Série D; hora pelo ogol e estádio só nas páginas da RSSSF que trazem.
- **Classificação final:** calculada (fase alcançada, pontos, vitórias, saldo, gols pró) quando a RSSSF não publica a geral.

## 9. Pendências e próximos passos

- Achados da revisão SD-001 a SD-021: tratados (docs/coleta/pedidos.md, parte 3, parte 4 e edições de 2026). A revisão ainda não reconferiu.
- Cartões: só jogo a jogo, pela ficha do ogol (prioridade baixa).

## 10. Arquivos e comandos

| Arquivo | O que faz |
|---|---|
| `coleta/bra-serie-d/baixar_espn_wiki.py` | Baixa as fontes complementares da Série D: - ESPN: a liga "bra.4" existe, mas não tem jogos da Série D (conferido em 2019, 2023 e 2025); não é usada. - Wikipédia em português e em inglês, uma página por edição -> data/co |
| `coleta/bra-serie-d/baixar_ogol.py` | Baixa o calendário de cada edição da Série D no ogol para data/coleta/bra-serie-d/ogol/serie_d_{ano}.json. |
| `coleta/bra-serie-d/baixar_ogol_clubes.py` | Baixa a ficha no ogol de cada clube que aparece nos calendários da Série D (nome completo, cidade, UF) e grava data/coleta/bra-serie-d/ogol/clubes.json. As páginas ficam em data/cache/ogol_equipes/. |
| `coleta/bra-serie-d/baixar_rsssf.py` | Baixa as páginas da Série D da RSSSF Brasil para data/coleta/bra-serie-d/rsssfbrasil/. |
| `coleta/bra-serie-d/clubes_d.py` | Identidade dos clubes da Série D (mesmo método da Série C; clube já nomeado na Série C usa o mesmo nome). |
| `coleta/bra-serie-d/edicoes.py` | Edições da Série D: anos, nomes oficiais e campeões (conferidos em duas fontes). |
| `coleta/bra-serie-d/explicacoes.py` | Textos do relatório da Série D que não saem do código: introdução, explicações de cada edição e o fim. |
| `coleta/bra-serie-d/importar.py` | Junta as fontes da Série D (mesmo método da Série C) e grava o pacote em data/coleta/bra-serie-d/pacote/ e o relatório em docs/coleta/bra-serie-d.md. |
| `coleta/bra-serie-d/pacote.py` | Grava o pacote da Série D (data/coleta/bra-serie-d/pacote/) e o relatório (docs/coleta/bra-serie-d.md), no formato de docs/agente-coleta-COMECE-AQUI.md, seção 4. Chamado por importar.py. |
| `coleta/bra-serie-d/rsssf_d.py` | Leitura das páginas da Série D da RSSSF Brasil (data/coleta/bra-serie-d/rsssfbrasil/br{ano}l4.htm). |

- Fontes baixadas: `data/coleta/bra-serie-d/` (ogol, rsssfbrasil, wikipedia). Pacote: `data/coleta/bra-serie-d/pacote/`. Relatório: `docs/coleta/bra-serie-d.md`.
- Código comum: `coleta/comum/` (`rsssf.py` leitor das páginas da RSSSF Brasil, `ogol.py` calendários e fichas, `gols.py` autores dos gols, `registro.py` cadastro comum de nomes `data/coleta/comum/clubes_ogol.json`, `baixar.py` download educado).
- Refazer do zero (da raiz do `clube_analitico`, logs no scratchpad):

  - `python coleta/bra-serie-d/baixar_espn_wiki.py` (ver o docstring)
  - `python coleta/bra-serie-d/baixar_ogol.py` (ver o docstring)
  - `python coleta/bra-serie-d/baixar_ogol_clubes.py` (ver o docstring)
  - `python coleta/bra-serie-d/baixar_rsssf.py` (ver o docstring)
  - `python coleta/bra-serie-d/importar.py` (grava o pacote e o relatório; `importar.py <ano>` só mostra, sem gravar)
  - `python coleta/comum/testar_carga.py bra-serie-d <pasta temporária>` (deve terminar com `-> OK`)
  - `python coleta/comum/documentar.py`

