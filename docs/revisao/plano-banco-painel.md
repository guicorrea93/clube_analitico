# Plano de correção — banco e painel (agente 1)

Para: agente 1 (banco, painel, escudos, Séries A e B). Revisão profunda de 22/11/2026.

## Como usar

1. Só comece quando o Guilherme mandar corrigir.
2. Corrija na ordem: primeiro "ERRADO NO AR" e "Publicação", depois os blocos de cima para baixo.
3. Cada linha é um resumo. A sugestão completa está no `docs/revisao/achados.csv`, coluna `o_que_a_fonte_diz`,
   depois de "SUGESTÃO:".
4. Ids marcados "espera D-xx": o Guilherme respondeu em 22/11 (todas menos a D-10). Corrija pela resposta registrada
   em `docs/revisao/decisoes-guilherme.md` (seção "Respostas do Guilherme").
5. Identifique jogos por competição + data + clubes, nunca pelo `partida_id`.
6. Depois de mexer: refazer o banco (`python futebol/migrar_brasileirao.py` e `futebol/carregar_pacotes.py`), gerar o
   painel (`python gerar_dashboard_v2.py`), escrever os ids corrigidos em `docs/revisao/pedidos-painel.md` e rodar as
   varreduras `python -I revisao/tela/varredura.py` e `python -I revisao/tela/datas_repetidas.py`.
7. Os planos das coletas (`plano-coleta-brasil.md`, `-europa.md`, `-sulamerica.md`) mudam pacotes. Depois de cada um,
   recarregue a competição e publique uma vez só.

## ERRADO NO AR

> **Atualização de 22/11:** o aviso de não publicar o `par-1` (PY-022) chegou tarde: o site já tem o pacote novo
> (commit fed171c, 11:18). Depois que a coleta corrigir o `par-1`, recarregue e publique logo.


Nenhum achado alto aberto é do agente 1. Os altos no ar são das coletas (lista em `decisoes-guilherme.md`).
O mais urgente aqui:
- PY-022 (média): **não publicar o `par-1` local**. Ele piora o site (vices de 1999-2003 e 2020 Clausura). Publicar só
  depois que a coleta corrigir PY-001 a PY-005.
- IT-013 (média): no site a classificação não mostra punição (Itália 2005/06: Milan 58 sem o "-30"; Juventus 20º sem nota).

## 1. Publicação (depois das coletas, uma vez por competição)

- PY-022 (média): `par-1` só depois do pacote novo corrigido.
- PE-024 (baixa): `per-1` só depois de PE-001 a PE-008.
- IT-015 (baixa): `ita-1` com 2025/26, junto das correções da coleta.
- DE-015 (baixa): `ger-1` com 2025/26 (já no banco local).
- Sem id: `ecu-1`, `fra-1`, `por-1` e `bra-sp-2` só depois das altas dos planos das coletas. O `esp-1` com 2025/26 está
  certo (QE-009): publicar junto com o QE-001/QE-002.

## 2. `gerar_dashboard_v2.py` (somas, textos e regras)

- IT-013 (média): coluna de ajuste "58 (-30)" e a `observacao` da edição na nota (vale para todas as ligas).
- ES-011 (baixa): nota das punições do Espanhol (mesmo mecanismo do IT-013).
- EN-010 (baixa): nota das punições do Inglês (mesmo mecanismo).
- PY-023 (média): linha parcial quando V/E/D vazio; esconder "Destaques" em tabela parcial.
- UY-025 (média): textos de "Jogos e vitórias" e "Gols": "nas N edições com jogos" (uru, col, par, per).
- PY-024 (baixa): aviso de participações parciais antes de 1996.
- EC-019 (baixa): participações por ano, não por edição (2005 conta duas).
- EN-009 (baixa): Participantes com "↓ caiu" e "↑ subiu" pela `situacao`. Fazer **depois** que as coletas acertarem
  os rebaixados (SP-015, IT-001, CH-010, CO-007, PY-011), senão as marcas erradas aparecem na tela.
- RC-003 (baixa): "pontos corridos" sem exigir `classificacao_rodada` (Inglês, "Título mais apertado").
- EN-013 (baixa): cartão com muitos escudos (CSS `.cu-um` com quebra).
- A2-029 (baixa): posição repetida e colunas vazias antes de publicar a A2 (conferir: parte já entrou em 22/11).
- Também (id da coleta): PY-001, campeão do ED por `edicao.campeao_id`, não pela posição 1.
- RC-005 (baixa, espera D-15): gols de W.O. nos totais.
- IT-011 (média, espera D-21): clubes da Serie B de 1945/46 nas participações.

## 3. `painel/index.html` (telas)

- RV-005 (baixa): nome do mandante cortado no começo em 420 px (função `jogos(e)`, `.cp-jogo`).
- ES-014 (baixa): rótulos com a temporada ("2012/13") nas Curiosidades e na Corrida.
- AR-041 (baixa): torneio no selo ("1975 Met") e nome da época no seletor.
- UY-027 (baixa): eixo da Corrida com marcas de década fixas.
- ~~DE-016~~ FECHADO em 22/11 (`nao-e-erro`): falso alarme. O Chrome sem janela desenha a 504 px; num iframe de 420 px a página cabe
  (SA-030, ES-020). Conferir assim e fechar.
- ES-013 (baixa, espera D-03): nome da época nas telas de edição.
- Sem id: aceitar dois campeões numa edição, se D-07 for "A" (Paulista 1973).

## 4. Série A: `futebol/migrar_brasileirao.py`

`corrigir_serie_a` (placares; custo baixo):
- QA-001 (média): 2001 Bahia 3x2 Ponte Preta e Fluminense 3x2 Ponte Preta.
- QA-002 (média): Taça Brasil 1959: Atlético-MG 2x1 Rio Branco-ES; datas e mando de 6 jogos.
- SA-017 (média): 1979 Central 0x1 Vasco; 1984 Portuguesa 0x1 Botafogo (confiança média); River-PI 1979 espera jornal.
- SA-024 (baixa): 2005 Brasiliense 0x1 Vasco com awd e observação.
- ~~SA-009~~ FECHADO em 22/11 (`nao-e-erro`): a Bola na Área dá a ordem do banco.

`datas_serie_a` (um CSV de datas revisadas):
- QA-003 (média): 1988, 1991, 1993, 1994, 1995 e 1999 (Transfermarkt + Bola na Área); 1974 só a Bola.
- SA-025 (baixa): 1996-1998, data real dos jogos remarcados.
- TL-002 (média): fecha com os dois acima; 2008-2010 já resolvidos.

Outros:
- QA-004 (baixa): pênaltis de 1988 da observação para as colunas.
- SA-023 (baixa): nomes da tabela `gol` ("Josiel", "Fernandão"...).
- CL-025 (baixa): "Brasília EC" vira "Brasília" (e a chave em `baixar_escudos.py`).
- CL-029 (baixa): 38 cidades vazias (`CIDADES`, `UF_MANUAL`).
- SA-016 (média, espera D-12): `historico/edicoes.py`, grupos E a H de 1986.

## 5. Série B: `serie_b/importar.py`

`CORRECOES` (placares; custo baixo):
- QA-007 (média): 1981 Flamengo-PI 2x2 Remo (03/02/1981).
- QA-006 (média): 1972 Atlético-BA 3x1 Central.
- QA-010 (média): 1994 Democrata-GV 0x0 Sergipe.
- QA-011 (baixa): 1982, dois awd com 0x1.
- QA-009 (baixa): 1992 Ceará x Fortaleza, mando invertido (`MANDO_INVERTIDO`).
- QA-005 (média, espera D-13): 1971 Grupo A, 12 ou 10 jogos.
- QA-008 (média, espera D-13): 5 placares com fontes 2 x 2.

Datas (`aplicar_ogol` + `DATAS_REVISADAS`; custo médio):
- RC-001 (média): 1990, 1991 e 1998 pela pt; não aplicar data que crie conflito; Série A 1997 rodada 24.
- RV-003 (média): 1980 semifinais e 1990/1991 (junto do RC-001).
- QA-012 (média): 2009 (54), 1981 (13), 1982 (3); 1989 com "Esportivo Passense" em `serie_b/clubes.py`.
- TL-003 (média): fecha com o QA-012.
- SB-017 (baixa): 1971, 1985, 1994 e 1997 só pela Bola, sem criar conflito.

Outros:
- SB-013 (baixa): artilheiros 1971, 1988-1990, 2004 e 2016.

## 6. Escudos: `baixar_escudos.py` e `data/escudos/`

- CO-023 (baixa): tirar o escudo do Huracán argentino do Huracán de Medellín.
- UY-021 (baixa): Deportivo Colonia (está o escudo do D. Italiano); Independencia sem escudo.
- RC-002 (baixa): Operário-MT com o escudo do Várzea Grande EC.
- ES-012 (baixa): CD Málaga e AD Almería pelo BDFutbol (`OUTRAS_FONTES`).
- CL-024 (baixa): Oeste (rodar de novo), União Bandeirante, Central-RJ, Rodoviária, Serrano.
- SP-029 (baixa): Oeste; o "LAF" some com o SP-011 da coleta.
- UY-022 (baixa): 47 escudos pela AUF.
- AR-035 (baixa): 114 escudos pelo BDFA (`/imagenes/<clube>_p.gif`).
- PE-020 (baixa): 114 escudos (começar pelos campeões).
- EC-018 (baixa): 36 escudos (ogol, Wikipédia es).
- PY-016 (baixa): 16 escudos; o do 12 de Octubre é genérico.
- CO-024 (baixa): 8 escudos.
- CH-026 (baixa): 5 escudos.
- CL-023 (baixa, espera D-03): "Espírito Santo FC" sem o escudo do Gálatas.

## 7. Cadastro de clubes (`futebol/`)

- SP-028 (baixa): Red Bull Brasil com nome de época (2015-2019); cidades de Humberto Primeiro e São Caetano EC.
- PY-017 (baixa, espera D-25): "Olímpia" do Brasil vira "Olímpia-SP".

## Achado de 22/11, depois da consolidação

- SA-031 (média): Série A 1987 sem os jogos do Módulo Amarelo, que pela CBF é parte da Série A. O campeão Sport aparece
  com só 2 jogos. Importar o Módulo Amarelo (RSSSF Brasil e Bola n@ Área) em `historico/` e `corrigir_serie_a`. Junto com a D-08.

## D-10 (22/11): edições não oficiais com aviso

- SB-026 (média): importar as edições não oficiais da Série B (1986, 1987, 2000; 1979 se houver disputa), em `serie_b/`.
- TL-005 (média): o painel marca a edição não oficial (aviso no Resumo e no seletor) e não conta o título.

## Decididas pelo Guilherme em 22/11 (já podem ser corrigidas)

Resposta: a recomendação de cada uma em `decisoes-guilherme.md`, menos a D-01, que ficou com a opção A: tudo o que
já terminou entra agora, inclusive os Aperturas 2026 da Argentina e do Paraguai. A D-10 ficou com a opção B (edições não oficiais com aviso).


- D-03 (nome da época): ES-013, CL-023.
- D-12 (Série A 1986): SA-016.
- D-13 (placares com fontes divididas): QA-005, QA-008.
- D-15 (gols de W.O.): RC-005.
- D-21 (Itália 1945/46): IT-011.
- D-25 (identidade, América do Sul): PY-017.
- D-07 (títulos divididos): sem id do agente 1, mas o painel precisa aceitar dois campeões na mesma edição (Paulista 1973: Santos e Portuguesa).

## Fontes novas a usar

Detalhes em `docs/revisao/fontes.md`.
- Transfermarkt (calendário e ficha): datas da Série A 1985-1999 e da Série B 2005+; autores, árbitro e público.
- Bola na Área: datas das Séries A e B 1971-1999; artilheiros da B; cidades dos clubes.
- Campeões do Futebol: artilheiros da Série B; 1937 e Robertão.
- Hemeroteca Digital: só para os empates de fonte (D-13).
- Escudos: BDFA (Argentina), AUF (Uruguai), BDFutbol (Espanha), ogol e Wikipédia es (Equador, Peru, Paraguai).

Cobre 66 de 66 ids abertos de `banco-painel` no `achados.csv` (22/11/2026; os fechados na conferência final estão riscados).
