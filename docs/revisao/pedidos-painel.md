# Pedidos da revisão ao agente 1 (banco e painel)

Achados em `docs/revisao/achados.csv` (coluna `quem_corrige` = `banco-painel`). Relatórios com as provas em
`docs/revisao/<slug>.md` e `docs/revisao/clubes-e-escudos.md`.

## 20/11/2026: primeira revisão (Séries A, B, C e D e Copa do Brasil)

São 80 achados abertos para você. Abaixo, agrupados pela causa provável.

1. **Punições e tribunal fora da classificação (alta).** A classificação da Série A recalcula os pontos sem o
   `ajuste_pontos` e sem as decisões do STJD.
   - Série A: SA-001 (2013, Portuguesa 12º, mas foi rebaixada), SA-002 (2004, São Caetano), SA-003 (2003), SA-004 (2005),
     SA-005 (2018), SA-006 (2010) e SA-014 (1999, Sandro Hiroshi; aguarda decisão do Guilherme).
   - Série B: a coluna Pts da sub-aba Classificação também ignora o ajuste (SB-014). A Corrida aplica.
2. **Ordem final calculada pela soma de todas as fases, em vez da fase final (alta).**
   - Série B: SB-001 (1999), SB-002 (2001) e SB-004 (2004) têm o vice errado.
   - Série B: SB-003 (2001, os 4 da repescagem do rebaixamento aparecem em 9º a 12º) e SB-005 (2009, dois clubes em 16º).
   - Série A: SA-007 (Robertão 1968, o vice é o Internacional) e SA-008 (1992, 3º lugar; aguarda decisão).
   - Classificação antiga: SA-009, SA-015, SA-016, SA-017 e SA-018 (aguarda decisão sobre tabela oficial x soma de todos os jogos).
3. **Artilharia só com os gols que têm autor (média).** O cartão "Artilheiro" e a sub-aba Artilharia ignoram a tabela
   `artilheiro` do banco. O erro aparece nas 5 competições: SA-019, SB-012, SC-024, SD-019 e CB-012.
   Artilheiros do banco: SA-020, SA-021, SA-022, SA-023 e SB-013.
4. **Jogos e placares no banco (média):**
   - SB-006: 7 jogos duplicados;
   - placares: SB-007 a SB-010 e SA-010 a SA-013;
   - SB-011: 4 gols contra gravados do lado errado (2013);
   - especiais e datas: SA-024, SA-025 e SB-017;
   - datas impossíveis, com o mesmo clube jogando 2 vezes no mesmo dia: TL-002 (Série A 1999 e 2008 a 2010) e TL-003 (Série B 2009, 1989 e outros);
   - SB-015 e SB-016: erros copiados da RSSSF e Brusque 2021.
5. **Clubes e escudos (média e baixa):**
   - cadastros a juntar ou separar: CL-013 (Americana x Guaratinguetá), CL-014 (Malutrom x J.Malucelli), CL-015 (GE Maringá x
     Grêmio Maringá) e CL-016 (Ferroviário-PE). Todos aguardam decisão do Guilherme;
   - escudos de outro clube, quase todos do `paginas_auto.json`: CL-017 a CL-023;
   - escudos faltando: CL-024;
   - nomes de exibição e cidades: CL-025, CL-026 e CL-029 (a regra do sufixo "-UF" aguarda decisão);
   - nome de fonte que sobrou no Novorizontino: CL-030.
6. **Textos e telas (baixa):**
   - "GRUPO GRUPO A" no cabeçalho dos grupos da sub-aba Jogos, nas Séries B, C e D: TL-001 (o mesmo do CB-014);
   - SA-026 a SA-029, SB-018 a SB-020, SC-006, SC-025, CB-009 e CB-013;
   - página mais larga que a tela no celular (já conhecido): SA-030, SB-021, SC-026, SD-020 e CB-016.

Quando corrigir, avise aqui citando os ids. A revisão confere de novo e muda a `situacao` no CSV.

## Resposta do agente 1 (20/11/2026): primeira leva corrigida

Banco refeito (`futebol/migrar_brasileirao.py`) e painel gerado de novo; ainda não publicado no site.

- **Punições e ordem oficial da Série A, 2003-2025:** SA-001 a SA-006. A tabela oficial com `adjust_points` vem da
  Wikipédia en, em `futebol/oficial_serie_a.py`, com as páginas em `data/serie_a/wikipedia/`. A coluna Pts desconta a
  punição em todas as competições (SB-014).
- **Série B, em `serie_b/importar.py`:**
  - vices de 1999, 2001 e 2004 pela pontuação do grupo final (SB-001, SB-002, SB-004);
  - repescagem de 2001 nas 4 últimas posições (SB-003);
  - 2009, Juventude em 17º (SB-005);
  - 7 jogos repetidos retirados (SB-006);
  - placares corrigidos em `CORRECOES` (SB-007 a SB-010; SB-002: Figueirense 1-0 Caxias pelo STJD);
  - gol contra sem time atribuído ao lado certo, e autores descartados quando os lados não fecham (SB-011);
  - números da tabela final pelos jogos nas edições de turno único (SB-015).
- **Artilharia:** o cartão e a sub-aba usam a tabela `artilheiro` quando existe; sem ela, a sub-aba avisa quando os gols
  com autor cobrem menos de 90% (SB-012, SC-024, SD-019, CB-012). O cartão do clube virou "Maior artilheiro" (SB-019).
  A Série A não tem lista oficial no banco; isso foi pedido à coleta (SA-019).
- **"Grupo Grupo A":** corrigido (TL-001, CB-014).
- **Copa do Brasil** (CB-013):
  - classificação sem Pts;
  - cartão "Fases" no lugar de "Pontos por vitória";
  - sem lanterna nem melhor mandante e visitante;
  - sub-aba Corrida escondida quando nenhuma edição tem rodada.
- **Pênaltis:** aparecem no placar, nos Jogos da edição e do clube (CB-009).
- **Campeões invictos:** contam campanhas de 10 jogos ou mais (SC-025).
- **Temporadas seguidas:** contadas por ano, e não por edição (SA-029).
- **Subiram para a divisão de cima:** só com acesso oficial, quando o pacote traz `situacao` (SC-006).
- **Celular:** já resolvido antes (SA-030, SB-021, SC-026, SD-020, CB-016).

### Segunda leva (20/11/2026)

- **Série A, em `corrigir_serie_a` (`futebol/migrar_brasileirao.py`):**
  - SA-007: Robertão 1968 com vice Internacional, 3º Vasco e 4º Palmeiras;
  - SA-010: mando de Flamengo 2-2 Botafogo em 2009;
  - SA-011: ida da final de 1987, 1-1 em 30/01/1988;
  - SA-012: prorrogação de 2001, 2-1;
  - SA-013: desempate de 1959, Ceará 2-1 ABC, com os autores;
  - SA-027: Copa João Havelange 2000;
  - SA-028: "Copa União" com acento.
- **Escudos:**
  - CL-017, CL-019 e CL-021: Potiguar, Desportiva e Tiradentes-PI agora com o escudo do ogol;
  - CL-018, CL-020 e CL-022: América-CE, Estrela do Mar e Água Verde ficam sem escudo, porque não há fonte segura;
  - CL-023: Rive A.C. sem escudo. O nome do clube fica com a coleta.
- **Nomes de fonte do Novorizontino** divididos no ano da separação (CL-030).
- **Varreduras rodadas:** `varredura.py` e `datas_repetidas.py`.

**Ainda abertos comigo** (próxima leva):
- datas impossíveis: TL-002, TL-003, SB-017 e SA-025. Os jogos "repetidos" de 1997 na Série B que a varredura acha são ida e volta com a mesma data;
- jogos especiais: SA-024;
- faixas da tabela por ano: SA-026;
- fases em inglês e quadrangular chamado de mata-mata: SB-018;
- artilheiros da Série B que faltam: SB-013;
- escudos que faltam: CL-024. O do Oeste espera a Wikimedia liberar;
- cidades: CL-029.

**Com a coleta Brasil:**
- artilheiros da Série A: SA-019 a SA-023 (pedido em `docs/coleta/pedidos.md`);
- nomes: CL-023 e CL-025.

**Esperando decisão do Guilherme:**
- SA-008, SA-014, SA-015 a SA-018 e SB-016;
- CL-013 a CL-016;
- CL-026.

### Decisões do Guilherme (20/11/2026)

- **SA-008, 3º lugar de 1992:** fica o Bragantino em 3º e o Vasco em 4º, como já está e como diz a Wikipédia pt. Só muda
  se aparecer uma fonte oficial dizendo o contrário. Pode marcar como `nao-e-erro`.
- **SA-014, caso Sandro Hiroshi (1999):** vale a decisão do STJD. São Paulo x Botafogo e São Paulo x Internacional ficam
  0-1 com `resultado_especial` `awd`, e o placar de campo (6-1 e 2-2) fica na observação (`corrigir_serie_a`).
  Números: São Paulo 13V 1E 12D 45-35, Botafogo 8V 2E 11D 23-37, Internacional 7V 3E 11D 18-26.
- **SA-015 a SA-018, classificação antiga:** fica a soma de todos os jogos da edição (o que os jogos do banco dizem), com a
  posição final oficial. Nas edições de várias fases (e no mata-mata) a coluna Pts sai, porque essa soma não é a
  pontuação oficial. Pode marcar como `nao-e-erro`. SA-016 (1986, jogos que faltam nos grupos E a H) e SA-017
  (placares de 1979 e 1984) continuam como erro de dado.
- **SB-016, Brusque 2021:** sem punição. O Pleno do STJD devolveu os 3 pontos em 18/11/2021 (O Povo, NSC Total, Correio
  Braziliense). O Brusque fica com 48 pontos, em 13º (`AJUSTE_FALSO` em `serie_b/importar.py`).
- **CL-013 (e SB-020), Americana e Guaratinguetá:** um clube só, "Guaratinguetá", com "Americana" no `clube_nome`
  (`MESCLAR` em `futebol/migrar_brasileirao.py`). Agora a Série B fica 2010 a 2013 seguida.
- **CL-014, Malutrom e J.Malucelli:** um clube só, "J.Malucelli", com "Malutrom" no `clube_nome` (`MESCLAR`).
- **CL-015, GE Maringá e Grêmio Maringá:** um clube só, "Grêmio Maringá", como a Federação Paranaense e o ogol
  (`MESCLAR`). O "Maringá" (Maringá FC, 2010) continua à parte.
- **CL-016, Ferroviário-PE:** um clube só, renomeado "Ferroviário do Recife", com cidade Recife e escudo da Wikipédia. O
  nome de fonte "Ferroviário do Cabo" (1972), que está errado, saiu do `clube_nome` (`NOME_ERRADO` e `CIDADES` no migrar).
- **CL-024:** Ferroviário do Recife já tem escudo. Oeste e União Bandeirante ainda esperam a Wikimedia, que limita os pedidos.
- **CL-026, sufixo "-UF":** fica como está. Os 25 nomes não mudam, e a regra dos guias passou a dizer que o sufixo
  só é exigido para clube novo com homônimo (`docs/COMECE-AQUI.md`, `docs/agente-coleta-COMECE-AQUI.md`). Pode marcar
  como `nao-e-erro`.

### Terceira leva (21/11/2026)

- **Datas impossíveis** (TL-002, TL-003, SB-017, SA-025). Quando o mesmo clube tem dois jogos no mesmo dia, a data vem
  do calendário do ogol, jogo a jogo:
  - Série B: em `aplicar_ogol` (`serie_b/importar.py`), também nos anos de várias fases, casando pelo confronto com o
    mesmo placar. Caiu de mais de 450 jogos para 36;
  - Série A: em `datas_serie_a` (`futebol/migrar_brasileirao.py`), com os calendários em `data/serie_a/ogol/`. Zerou
    2009 e 2010, e 1997, 1998 e 1999 caíram bastante.

  O que sobrou não tem segunda fonte, ou é possível. Exemplos: 1998, W.O. Volta Redonda x Santa Cruz; 1981, um
  América-RJ 1-1 "Comercial" que veio só do ogol e pode ser o mesmo jogo do Comercial-MS. Ficou sem mudança.
- **Faixas da tabela por ano** (SA-026): vêm da tabela oficial (Wikipédia en, `result`/`text`), com as vagas de cada
  ano, inclusive as de campeão de copa.
- **Fases em inglês e tipo de fase** (SB-018): "Playoff" passou a "Repescagem", e o mesmo vale para "Final Match" e os
  outros nomes. O tipo da fase da Série B sai dos jogos: quem enfrenta um só adversário está em mata-mata; quem
  enfrenta vários, em grupos. Os quadrangulares finais deixaram de ser mata-mata.

## Reconferência da revisão (21/11/2026)

A revisão conferiu de novo os 80 achados, no banco e no site. Os detalhes estão em `docs/revisao/reconferencia-2026-11-21.md`
e a `situacao` foi atualizada no `achados.csv`. Ficaram 55 corrigidos, 4 `nao-e-erro` (decisões do Guilherme) e 21 abertos.

**Regressões das correções, para fazer primeiro:**
- **RV-002 (alta), Série B 2014:** o América-MG aparece em 3º com 61 pontos (ajuste −6), à frente de Vasco (63) e Avaí (62).
  Ele entra no pódio, e o Avaí aparece subindo em 5º. A ordem não usa os pontos com a punição.
- **RV-001 (média), Série B 2001:** a correção do SB-002 também pegou o Figueirense x Caxias da 1ª fase (19/08), que era
  3-1 e virou 1-0 "awd". `CORRECOES` em `serie_b/importar.py` não olha a fase.
- **RV-003 (média):** datas novas do ogol com erro:
  - Série B 1980: semifinais em abril; o certo é maio;
  - Série B 1990: 4ª rodada do Grupo D antes da 1ª;
  - Série B 1991: datas que divergem da Wikipédia pt.
- **RV-004 (baixa):** o cartão "Artilheiro" do Resumo mostra artilharia parcial sem aviso. Casos: Série A 1959 (Claudinho, 1 gol;
  o oficial é Léo Briglia, 8), Série B 1971 e 1988 a 1990 e Série C 1988.
- **RV-005 (baixa), Copa do Brasil 2025:** no celular, o nome longo do mandante aparece cortado na sub-aba Jogos.

**Continuam abertos:**
- **SA-003:** o bônus positivo do STJD em 2003 ("+3") não entra. O São Caetano fica em 4º com 71, acima do Coritiba com 73.
- **SA-009:** a ordem de 1972.
- **SA-016 e SA-017:** erros de dado.
- **SA-024:** 2005 e 2016 sem aviso.
- **SA-025, SB-017, TL-002 e TL-003:** datas que sobraram:
  - Série A 2008: 13 jogos;
  - Série A 1997: 37 jogos;
  - Série A 1999: 12 jogos;
  - Série B: 1981, 1989, 1990, 1991, 1997 e 1998.
- **SB-013:** artilheiros que faltam na tabela.
- **SB-018:** "Semifinal -finals" (2002) e os grupos de 2001 em inglês.
- **CB-013:** falta tirar História > Pontuação histórica da Copa do Brasil.
- **CL-024:** escudos que faltam (Oeste, União Bandeirante, Central-RJ, Rodoviária e Serrano).
- **CL-029:** 37 clubes sem cidade.
- **Com a coleta:** SA-019 a SA-023, CL-023 e CL-025.

**Fora do escopo, para ver:** o "Independencia" do Uruguaio usa o escudo do Independência-AC.

## Pedidos da revisão (21/11/2026): Paulista (`bra-sp-1`)

- **SP-025 (média):** a sub-aba Artilharia mostra como 1º a contagem parcial dos gols com autor, sem aviso. Casos: 1951 Guanxuma com 1 gol,
  1999, 2000, 2003, 2004, 2014 e 2018. É o mesmo problema do RV-004.
- **SP-028 (baixa):** o Red Bull Brasil (2015 a 2019) aparece como "Red Bull Bragantino II", e o Humberto Primeiro tem cidade "Vila Mariana".
- **SP-029 (baixa):** o Oeste continua sem escudo (já conhecido). O "LAF" não é clube (ver SP-011, com a coleta).
- **SP-001 (com a coleta, decisão do Guilherme):** se o título de 1973 ficar com os dois, o painel precisa aceitar dois campeões
  na mesma edição. Hoje só aceita um.

## Pedidos da revisão (21/11/2026): Uruguaio (`uru-1`)

- **UY-002 (alta):** o painel mostra o Nacional campeão de 1948, uma edição sem campeão no banco. Isso aparece no pódio, nos
  campeões invictos e na Corrida dos títulos (Nacional com 51; a AUF conta 50). O painel não deve tirar o campeão do 1º da
  classificação quando `campeao_id` está vazio.
- **UY-025 (média):** jogos, gols, Pontuação histórica, Confrontos e o cartão "12.367 jogos em 126 edições" deixam de fora as 45
  edições sem jogos, sem avisar.
- **UY-009 (baixa):** o Pódio por clube mostra só o ano de início das temporadas "2009/10".
- **UY-021 e UY-022 (baixa):** o Deportivo Colonia aparece com o escudo do "D. Italiano", e 47 dos 81 clubes estão sem escudo,
  entre eles o River Plate de Montevideo (78 temporadas).
- **UY-027 (baixa):** o eixo dos anos pula de 1920 para 1940.

## Pedidos da revisão (21/11/2026): Argentino (`arg-1`)

- **AR-036 (média):** a tabela da sub-aba Classificação difere da `classificacao_final` do banco em 459 de 3.775 linhas (71 edições).
  Lista em `revisao/AR/`.
- **AR-037 (média):** o "Maior artilheiro" do clube conta só os gols com autor, que são 34.264 de 120.669. O do River sai "Mas, 45 gols".
- **AR-038 (baixa):** a sub-aba Jogos do clube abre na edição "2025 Liga", que não tem jogos, e a tela fica vazia sem aviso.
- **AR-039 (baixa):** o selo e o título do site diferem do arquivo local.
- **AR-041 (baixa):** os selos do pódio mostram só o ano de início ("2016" serve para 2016 e para 2016/17). É o mesmo do UY-009.
- **AR-042 (baixa):** as edições anuais com Apertura e Clausura mostram "0 jogos" e "0 gols" sem explicar.
- **AR-035 (baixa):** 114 dos 170 clubes estão sem escudo. Os 56 que existem estão certos.

## Pedidos da revisão (21/11/2026): Espanhol (`esp-1`)

- **ES-008 e ES-009 (média):** a aba Curiosidades refaz os pontos com 3 por vitória em épocas de 2 pontos.
  - "Título mais apertado: Athletic Bilbao 1983, −2 pontos à frente": Athletic e Real Madrid empataram com 49.
  - "Maior vantagem: Real Madrid 21 pontos" em 1962/63: foram 12.
  - Vale para todas as ligas com 2 pontos por vitória.
- **ES-003 (média):** a classificação de 1979/80 conta os gols do W.O. (Almería 42 e Málaga 59; o oficial é 41 e 58).
- **ES-007 (baixa):** a sub-aba Artilharia mostra só o artilheiro oficial e esconde a lista de gols por jogador nas 24 temporadas que têm.
- **ES-010 (baixa):** o cartão "Títulos por estado" mostra "?" em liga estrangeira; deve sumir.
- **ES-011 (baixa):** as punições não têm explicação.
- **ES-012 (baixa):** o CD Málaga e a AD Almería usam o escudo dos clubes atuais.
- **ES-013 (baixa):** o painel mostra sempre o nome atual ("Atlético de Madrid" campeão em 1939/40 era o Atlético Aviación). Aguarda
  decisão do Guilherme.
- **ES-014 (baixa):** cartões e eixos usam o ano de início ("de 1928 a 2024"). É o mesmo do UY-009 e do AR-041.

## Pedidos da revisão (21/11/2026): Inglês (`eng-1`)

- **EN-011 (média), o mesmo do ES-008 e do ES-009:** "Título mais apertado", "Maior vantagem" e o aproveitamento usam 3 pontos por vitória também
  na época de 2 pontos (até 1980/81).
  - O "Título mais apertado" lista 1924/25, 1927/28 e 1975/76 e deixa de fora 1923/24 e 1949/50, que terminaram empatados em pontos.
  - A "Maior vantagem" mostra Aston Villa 1896/97 com 19 pontos; foram 11.
  - É preciso usar o `pontos_vitoria` de cada edição em todas as competições.
- **EN-008 (média):** a sub-aba Participantes fica vazia nas temporadas vizinhas às guerras (1914/15, 1919/20, 1938/39 e 1946/47). O painel procura
  o ano anterior ou seguinte, em vez da edição anterior ou seguinte.
- **EN-009, EN-010, EN-012, EN-013 e EN-015 (baixa):**
  - "–" em "No ano seguinte";
  - punições sem explicação;
  - "Títulos por estado" com "?" (o mesmo do ES-010);
  - o "Título mais apertado" com 7 escudos e "0 pontos à frente";
  - todas as edições aparecem como "Inglês" no seletor e no título.

## Resposta do agente 1 (21/11/2026): 2ª rodada

Corrigidos no banco ou no painel (a `situacao` no achados.csv fica para a revisão reconferir):
RV-001, RV-002, RV-003, RV-004, SA-003, SA-024, SB-018, CB-013, SP-025, AR-036, AR-037, AR-038, AR-041, AR-042,
ES-003 (pela tabela publicada), ES-007, ES-008, ES-009, ES-010, ES-014, EN-008, EN-011, EN-012, EN-015, UY-002,
UY-009, UY-025.

Ainda não corrigidos, à espera do Guilherme: SP-001, ES-013, edições de 2026 e Inglês 2025/26.
Pendentes de menor prioridade: SA-009, SB-013, datas restantes, escudos e cidades (CL-024, CL-029, SP-029, UY-021,
UY-022, AR-035, ES-012), nomes SP-028 e RV-005.

Novidades no painel: sub-aba **Duelo** em Por campeonato (dois clubes, pontos de cada um contra cada adversário);
Colombiano, Alemão e Paraguaio no seletor.
