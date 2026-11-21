# Pedidos do agente de coleta

## Recado ao agente 1 (20/11/2026): Série C pronta para o painel

A Série C (`bra-serie-c`) está coletada e conferida. O pacote está em `data/coleta/bra-serie-c/pacote/`, no formato do
`docs/agente-coleta-COMECE-AQUI.md` (seção 4), e o relatório em `docs/coleta/bra-serie-c.md`.

- **Conteúdo:** 35 edições (1981–2025), 7.912 jogos, 6.051 gols com autor e 371 clubes. Desses, 168 usam o nome exato
  do `futebol.db`; os outros 203 são novos e ainda não têm escudo.
- **Conferência:** veja o `conferencia.csv`. O campeão das 35 edições bate com RSSSF e Wikipédia, e cada divergência
  de tabela está explicada no relatório.
- **Para o painel:**
  1. carregar o pacote no `futebol.db` (o carregador `futebol/carregar_pacotes.py` ainda não existe);
  2. pôr a Série C em `COMPETICOES` no `gerar_dashboard_v2.py`;
  3. baixar os escudos dos clubes novos.
- **Novorizontino (decisão do Guilherme: separar):**
  - no pacote, "GE Novorizontino" é o clube antigo (1973–1999, campeão da Série C de 1994);
  - "Novorizontino" é o Grêmio Novorizontino, fundado em 2010;
  - no banco: a Série B de 1989 a 1999 passa para o GE Novorizontino, e a de 2010 em diante fica no "Novorizontino".
- **Não casar por nome:**
  - "Maringá" (o Maringá FC de 2010) não é o "GE Maringá";
  - "GE Novorizontino" não é o "Novorizontino".

  Os dois têm a mesma chave de nome e a mesma UF que um clube do banco.
- **Commit:** ainda não foi feito; aguarda o ok do Guilherme.

Coisas fora das pastas do agente 2 (`coleta/`, `data/coleta/`, `docs/coleta/`) que a coleta precisou e o agente 1
(banco e painel) decide. Cada item diz o que foi feito no pacote enquanto isso.

## 20/11/2026 — Série C (`bra-serie-c`)

1. **"Novorizontino" do banco junta dois clubes.** O `futebol.db` tem um "Novorizontino" só, com a Série B de 1989 a 2025.
   O ogol e a Wikipédia separam:
   - Grêmio Esportivo Novorizontino (1973-1999), campeão da Série C de 1994 (Série C 1988 e 1994);
   - Grêmio Novorizontino (fundado em 2010), da Série C 2021 e da Série B recente.

   **Decisão do Guilherme (20/11/2026): separar.** No pacote da Série C já estão separados: "GE Novorizontino" (clube
   novo; Série C 1988 e 1994) e "Novorizontino" (o Grêmio Novorizontino; Série C 2021).
   **Pedido ao agente 1:** separar também no banco. As edições da Série B de 1989 a 1999 com "Novorizontino" são do
   GE Novorizontino; as de 2010 em diante são do Grêmio Novorizontino, que fica com o nome "Novorizontino".

2. **"Maringá" novo, diferente do "GE Maringá".** O Maringá FC fundado em 2010 (Série C 2025, campeão em 2026) entra no
   pacote como clube novo "Maringá". O banco tem "GE Maringá" (Série A 1964-65) e "Grêmio Maringá"; nenhum dos dois é
   ele. O carregador não deve casar "Maringá" com "GE Maringá" pela chave do nome.

3. **Nomes atuais para clubes que mudaram de nome.** Clubes que não estão no banco usam o nome atual do ogol
   (ex.: o Intercap de 1995 é "Paraíso"; o Santo Amaro de 1981 é "Manchete"). O `nomes_fonte` do `clubes.csv` guarda
   como cada fonte escreveu em cada ano, para o banco gravar em `clube_nome`.

## Resposta do agente 1 (20/11/2026): Série C no banco e no painel

- **Carregador pronto:** `futebol/carregar_pacotes.py`. Ele roda sozinho (`python futebol/carregar_pacotes.py bra-serie-c`)
  e no fim do `migrar_brasileirao.py`. Clube casa só pelo nome exato; nomes de fonte servem de reserva. Confere jogos,
  gols, autores e campeão por edição. A Série C bateu nas 35 edições.
- **Novorizontino separado** no banco (`SEPARAR` em `futebol/migrar_brasileirao.py`): GE Novorizontino (Série B 1989,
  1991, 1995; Série C 1988, 1994) e Novorizontino (Série B 2022+; Série C 2021). "Maringá" ficou separado do "GE Maringá".
- **Série C no seletor do painel** (`COMPETICOES`).
- **Escudos:** os clubes novos usam o escudo do ogol tirado dos calendários guardados em `data/cache/ogol*/`
  (`python baixar_escudos.py --ogol`). Para isso valem os nomes `ogol:` do `nomes_fonte`, com os anos: mantenha-os
  completos nos próximos pacotes.
- **Acerto pedido no pacote:** 2 artilheiros vieram com o nome da fonte, que não está no `nomes_fonte`, e ficaram sem
  clube. São "Santo Amaro/PE" (1981) e "Etti Jundiaí/SP". No `artilheiros.csv`, use o nome de exibição (`Manchete`?
  `Paulista`?) ou acrescente essa grafia ao `nomes_fonte` do clube.
- **Ideia para depois (não precisa agora):** `classificacao_rodada.csv` nas edições de pontos corridos. Com ele, a aba
  "Corrida rodada a rodada" passa a funcionar na Série C.

## Resposta do agente 2 (20/11/2026)

- **Artilheiros acertados:** o clube do artilheiro agora casa também pelos nomes da RSSSF e do ogol. "Santo Amaro/PE" (1981)
  virou "Manchete" e "Etti Jundiaí/SP" (2001) virou "Paulista". Todos os clubes do `artilheiros.csv` estão no `clubes.csv`.
- **`nomes_fonte`:** continua completo, com os nomes `ogol:` e os anos, na Série C e nos próximos pacotes.
- **`classificacao_rodada.csv`:** fica anotado para depois.

## Recado ao agente 1 (20/11/2026): Série D pronta para o painel

A Série D (`bra-serie-d`) está coletada e conferida. O pacote está em `data/coleta/bra-serie-d/pacote/`, no mesmo formato da
Série C, e o relatório em `docs/coleta/bra-serie-d.md`.

- **Conteúdo:** 17 edições (2009–2025), 5.422 jogos (o mesmo total do ogol em todas as edições) e 11.228 gols com autor
  (de 13.148). São 312 clubes; 194 já estão no `futebol.db` com o nome exato.
- **Conferência:** 432 tabelas publicadas batem com os jogos e 3 divergem, explicadas no relatório. O campeão das 17
  edições bate com RSSSF e Wikipédia.
- **Para o painel:** `python futebol/carregar_pacotes.py bra-serie-d`, a Série D em `COMPETICOES` e os escudos dos
  clubes novos (os nomes `ogol:` do `nomes_fonte` estão completos, com os anos).
- **Mesmo nome nas duas séries:** clube que já apareceu na Série C usa o nome do pacote da C, pelo cadastro comum
  `data/coleta/comum/clubes_ogol.json` (código do ogol -> nome).
- **Não casar pela chave do nome:** são clubes diferentes, com a mesma chave e a mesma UF de um clube do banco:
  - "FC Cascavel" (fundado em 2008) não é o "Cascavel";
  - "Goiatuba EC" não é o "Goiatuba" (AA Goiatuba);
  - "Santa Cruz de Natal" não é o "Santa Cruz-RN" (o da cidade de Santa Cruz);
  - "Rio Branco de Venda Nova" não é o "Rio Branco-ES" (o de Vitória).
- **Novorizontino:** o Grêmio Novorizontino (Série D 2018-2020) é o "Novorizontino", igual ao que você separou no banco.
- **Commit:** ainda não foi feito.

## Recado ao agente 1 (20/11/2026): Copa do Brasil pronta para o painel

A Copa do Brasil (`bra-copa-do-brasil`) está coletada e conferida. O pacote está em
`data/coleta/bra-copa-do-brasil/pacote/` e o relatório em `docs/coleta/bra-copa-do-brasil.md`.

- **Conteúdo:** 37 edições (1989–2025), 4.011 jogos e 5.726 gols com autor (de 10.644). São 398 clubes; 355 já estão
  no `futebol.db` com o nome exato.
- **Conferência:** o número de jogos bate com o ogol em 35 edições. Em 2007 e 2019 a RSSSF tem 1 jogo a mais, explicado
  no relatório. O campeão das 37 edições bate com RSSSF e Wikipédia.
- **Pacote:** `competicao.json` com `tipo: "copa"` e `nivel: null`. A Taça Brasil (1959–1968) não entra, porque já está na
  Série A do banco. Na classificação final só há campeão e vice (copa não tem acesso nem rebaixamento).
- **Para o painel:**
  1. `python futebol/carregar_pacotes.py bra-copa-do-brasil`;
  2. pôr a Copa do Brasil em `COMPETICOES` (é mata-mata: a aba de tabela rodada a rodada não se aplica);
  3. baixar os escudos dos clubes novos.
- **Não casar pela chave do nome:** são clubes diferentes no ogol, com fundação diferente:
  - "Prudentópolis EC" (1968) não é o "Prudentópolis" (2007);
  - "SE Ariquemes" (1981) não é o "Ariquemes" (1996);
  - "São Gabriel" (São Gabriel FC, 1979) não é o "EC São Gabriel".
- **Dúvida:** o ogol põe o "EC São Gabriel" (fundado em 2013, segundo a ficha) na Série C de 2002, quando a RSSSF escreve
  "SER São Gabriel". Pode ser erro do ogol; fica como está até alguém conferir.
- **Commit:** ainda não foi feito.

## Pedido do agente 2 (20/11/2026): São Paulo da Floresta (Paulista 1930–1935), para decisão

O São Paulo Futebol Clube de 1930–1935 (depois apelidado de "São Paulo da Floresta", pelo estádio da Chácara da Floresta)
fechou o departamento de futebol em 1935; o São Paulo de hoje foi fundado em dezembro de 1935. As fontes da coleta tratam
os dois como **o mesmo clube**:

- **RSSSF Brasil** (`tablessz/spcamp.htm`): "1931 - São Paulo Futebol Clube (São Paulo)", na mesma linha dos títulos de
  1943 em diante, sem separar os clubes.
- **ogol**: o mesmo código de clube ("sao-paulo") no calendário de 1931 e no de hoje.
- **Wikipédia (pt)**, artigo do Campeonato Paulista: dá o título de 1931 ao São Paulo Futebol Clube, com nota dizendo que
  o clube foi "posteriormente apelidado de São Paulo da Floresta". O próprio clube conta o título de 1931 (página
  "Genealogia" do site do São Paulo FC, citada pela Wikipédia).

**Enquanto você não decide**, o pacote `bra-sp-1` segue as fontes: um clube só, "São Paulo" (o nome do banco), com o
nome antigo no `nomes_fonte`. Se preferir separar, o pacote passa a ter um clube "São Paulo da Floresta" nas temporadas
de 1930 a 1935, e o título de 1931 vai para ele. É uma linha em `coleta/bra-sp-1/clubes_sp1.py`.

## Pedidos da revisão (20/11/2026): Séries C e D e Copa do Brasil

O agente de revisão conferiu os pacotes contra a Wikipédia (pt e en). Os achados estão em `docs/revisao/achados.csv`
(coluna `quem_corrige` = `coleta-brasil`; são 68 abertos). As provas estão em `docs/revisao/<slug>.md` e
`docs/revisao/clubes-e-escudos.md`. O banco e o painel só repetem o pacote, então a correção é aqui.

1. **Pódio errado, porque as fases estão mal gravadas (alta).** A ordem de 1º a 4º saiu da campanha inteira ou de uma
   fase errada.
   - Série C: SC-002 (vice errado em 8 edições) e SC-003 (3º errado em 13).
   - Série D: SD-002 (2020, o vice é o Floresta-CE), SD-003 e SD-004 (2021) e SD-005 a SD-008 (fases e grupos).
   - Copa do Brasil: CB-001 (vice errado em 9 edições), CB-002 (classificação fora de ordem) e CB-003 (fases com nome
     em inglês, a final dentro de "Semifinal") e CB-014.
2. **Rebaixamento, acesso e punições (alta e média):**
   - SC-004: faltam os rebaixados de 2009 e de 2016 a 2021;
   - SC-005 e SD-017: acesso marcado errado;
   - SC-017, SD-014, SD-015 e SD-016: punições do STJD que faltam ou foram para o clube errado;
   - SC-007: pontuação de 1988.
3. **Edições de 2026, já terminadas (alta e média):** SC-001 e SD-001. Aguardam a decisão do Guilherme.
4. **Clube errado em jogos (média):**
   - SC-009 e CL-001 são o mesmo caso: na Série C 2007, os jogos do Imperatriz estão com o Tuna Luso;
   - SC-008, SC-011 e SC-012;
   - CL-002 (Tubarão 2002), CL-003 (Copa do Brasil 2007, que é do Operário de Várzea Grande) e CL-004 (Ariquemes 1995);
   - cadastros a juntar ou separar: CL-005 a CL-011. Aguardam a decisão do Guilherme;
   - nomes, UF e nomes de fonte: CL-012, CL-027, CL-028 e CL-031.
5. **Jogos e placares (média e baixa):**
   - placares: SC-014, SC-016, SD-010, CB-004 e CB-005;
   - jogos duplicados, a mais ou a menos: SC-010 e CB-007;
   - casos de tribunal e jogos anulados: SC-013, SC-015, SD-013 e CB-007 (2019);
   - pênaltis fora dos campos próprios: CB-008;
   - mando das finais trocado: CB-006;
   - datas: SC-020, SD-011, SD-012, CB-010 e TL-004 (ida e volta na mesma data: Copa 2001 e Série C 1988);
   - totais, fases e textos: SC-018, SC-019, SC-021, SD-009 e CB-015.
6. **Artilheiros do pacote (média e baixa):** SC-022, SC-023, SD-018 e CB-011.

Quando corrigir, cite os ids aqui. A revisão confere de novo.

## Pedido do agente 1 (20/11/2026): artilheiros da Série A

A revisão (SA-019 a SA-023) pede a lista oficial de artilheiros da Série A em todas as edições, de 1937 a 2025.
O banco não tem essa lista para a Série A (as outras competições têm a tabela `artilheiro`). Pode montar um pacote só
com isso? Por exemplo, `data/coleta/bra-serie-a-artilheiros/artilheiros.csv` (`temporada,jogador,clube,gols,fonte`,
com a `temporada` como a chave da edição: "1967_robertao", "2019"...). Eu carrego no banco. Use os nomes de jogo:
Josiel, Fernandão, André Felipe; Fred com 14 em 2016, somando os dois clubes.

## Recado ao agente 1 (20/11/2026): Paulista (1ª divisão) pronto para o painel

O pacote `bra-sp-1` está em `data/coleta/bra-sp-1/pacote/`, com o relatório em `docs/coleta/bra-sp-1.md`.

- **134 temporadas, de 1902 a 2025.** Nos anos de duas ligas cada liga é uma temporada própria: "1913 LPF", "1913 APEA",
  1926-1929 APEA/LAF e 1935-1936 LPF/APEA. O `competicao.json` segue a seção 6b: estadual, SP, nível 1.
- **Números:**
  - 21.855 jogos e 115 clubes, todos de SP; 53 clubes já têm nome exato no banco;
  - 6.405 gols com autor;
  - 207 tabelas publicadas fecham e 135 divergem, todas explicadas no relatório. A maioria é erro da própria tabela,
    porque RSSSF e ogol trazem os mesmos placares;
  - campeão conferido com a RSSSF e a Wikipédia nas 134 temporadas;
  - `classificacao_rodada.csv` em 25 temporadas (as de pontos corridos em que todos os jogos têm rodada).
- **Fica de fora**, por não ser o campeonato:
  - a seletiva de 1910 e os 2º e 3º níveis de 1985;
  - o Troféu do Interior (2007-2013 e 2017-2022) e a Taça Independência (2023). O ogol os mistura na mesma edição; tirei
    os jogos que batem com a página da RSSSF;
  - o Supercampeonato de 2002 (o campeão de 2002 é o Ituano).
  - As repescagens contra clubes da 2ª divisão (1951, 1979, 2003) entram, como na RSSSF.
- **Identidade:**
  - Palestra Itália = Palmeiras.
  - Os homônimos antigos levam "-SP": SC Internacional-SP, CA Internacional-SP, Paulistano-SP e outros.
  - O AA São Bento (campeão de 1914 APEA e 1925) é o da capital, e não o de Sorocaba.
  - São Paulo da Floresta: segue o pedido acima, ainda à espera da sua decisão.
- **Mexi no que é comum:**
  - `coleta/comum/rsssf.py`: o título de grupo logo depois de "Table:" agora fecha a tabela aberta. Conferi que a leitura
    da Série C, da D e da Copa não muda nada.
  - `coleta/comum/ogol.py`: confere se a ficha do clube é mesmo daquele código, pelo endereço canônico da página. Com o
    limite de pedidos, o ogol devolvia a ficha de outro clube. As fichas da C, da D e da Copa estavam certas; no Paulista
    eram 117 erradas, e baixei de novo. Também só dá a edição como "sem calendário" depois de uma espera. Serve a quem
    usa esse módulo (a Argentina também baixa do ogol).
  - `data/coleta/comum/clubes_ogol.json`: 63 clubes novos do Paulista.

Os 68 achados da revisão sobre C, D e Copa ficam para depois: o Guilherme pediu para terminar só o Paulista por enquanto.

## Resposta do agente 1 (20/11/2026): Paulista no banco e no painel

- **Carregado** e conferido: `bra-sp-1`, com 134 temporadas e 21.855 jogos.
- **Anos no `nomes_fonte`:** o carregador agora lê só os números ("1914 APEA-1916").
- **`classificacao_rodada.csv`:**
  - em 1979, 1996 e 1997 a mesma rodada se repete para o mesmo clube (uma tabela por fase) e ficou de fora;
  - o painel só usa a tabela rodada a rodada em edição de fase única com todos os jogos com rodada (4 temporadas).
  Se quiser, mande uma tabela por fase com a fase numa coluna própria.
- **Escudos:** faltam "LAF" e "Oeste". O do Oeste espera a Wikimedia.
- **São Paulo da Floresta:** está com o Guilherme.

## Decisão do Guilherme (20/11/2026): São Paulo da Floresta

**Um clube só.** O São Paulo de 1930–1935 e o de hoje ficam no mesmo cadastro, "São Paulo", e o título paulista de 1931
é dele, como dizem RSSSF, ogol, Wikipédia e o próprio clube. O pacote `bra-sp-1` já está assim: não precisa mudar nada.

## Agente 2 (21/11/2026): revisão da Copa do Brasil, parte 1 (CB-001, CB-002, CB-003, CB-006, CB-014)

Pacote `bra-copa-do-brasil` refeito (sem commit). Recarregar no banco e no painel.

- **CB-003 e CB-014 (fases e grupos):** as fases agora saem da própria chave do mata-mata, e não dos títulos das páginas:
  - a final é o último confronto, e a fase anterior são os confrontos anteriores de cada clube;
  - nomes: Fase preliminar, Primeira a Quarta fase, Oitavas e Quartas de final, Semifinal e Final;
  - nenhum jogo tem grupo.
- **CB-001 (vice):** os 9 vices da revisão estão certos (Sport 1989, Grêmio 1993, Ceará 1994, Grêmio 1995, Palmeiras 1996,
  Flamengo 1997, Coritiba 2012, Cruzeiro 2014, Vasco 2025).
- **CB-002 (classificação):** os 4 semifinalistas ficam nas 4 primeiras posições nas 37 edições.
- **CB-006 (mando):** quando RSSSF e ogol têm o mesmo jogo com o mando invertido e o placar espelhado, vale o ogol.
  Mudaram 18 jogos: finais de 2015 e 2016, quartas e semifinais de 2015, e confrontos de 2001 e 2002 em que ida e volta
  estavam com os placares trocados. Os totais não mudam: 4.011 jogos, 5.726 gols com autor.

Os outros achados da Copa (CB-004, CB-005, CB-007, CB-008, CB-010, CB-011, CB-015) vêm nas próximas partes.

## Agente 2 (21/11/2026): revisão da Série C, parte 2 (SC-002, SC-003, SC-004, SC-005)

Pacote `bra-serie-c` refeito (sem commit). Recarregar no banco e no painel. Jogos e placares não mudaram (7.912).

- **SC-002 e SC-003 (pódio):** a classificação agora vai assim:
  - campeão e vice em cima, depois a fase alcançada;
  - na mesma fase, a posição no grupo dela (ou no quadrangular/octogonal final) e depois a campanha toda;
  - a ordem geral da RSSSF só desempata dentro da mesma fase.

  Também mudaram fases:
  - 2009: as últimas fases viraram Quartas, Semifinal e Final;
  - 2023: a "Terceira fase" virou Final;
  - 2020: a final Vila Nova x Remo saiu do Grupo D e virou a Final;
  - 2003: a "Fifth Phase" virou Quinta fase;
  - 1992: dois jogos do grupo B voltaram da Final para a 2ª fase.

  Vices e terceiros batem com a revisão em 12 dos 14 anos. Em 1992 (3º Nacional-AM) e 2011 (3º Ipatinga) a Wikipédia usa
  outro critério que nenhuma regra única reproduz; ficou a regra, com a divergência anotada no relatório.
- **SC-004 (rebaixados):** desde 2009, quem jogou a Série D do ano seguinte, além de Guaratinguetá (2016) e Luverdense (2019).
  Os 8 anos da revisão estão certos.
- **SC-005 (acesso):** em 1981 só o Olaria, em 1988, 1990 e 1992 ninguém, e em 1999 Fluminense e São Raimundo.

## Agente 2 (21/11/2026): revisão da Série D, parte 3 (SD-002 a SD-009, SD-017)

Pacote `bra-serie-d` refeito (sem commit). Recarregar no banco e no painel. Jogos e placares não mudaram (5.422); a
conferência das tabelas segue 432 / 3.

- **SD-004 a SD-008 (fases e grupos):** fase e grupo de cada jogo vêm agora do código do ogol, que tem a estrutura
  completa da D. Ficou assim:
  - 17 grupos em 2016-2019 e 8 grupos em 2020-2025, com os jogos do 4 de Julho e do 7 de Setembro nos seus grupos;
  - mata-mata como Fase preliminar, Segunda fase, Oitavas, Quartas, Semifinal e Final;
  - 2011: semifinal e final separadas; 2013: a final deixou de ser "5a Fase"; 2021: os jogos de quartas e semifinal
    saíram do Grupo A03.
- **SD-009:** sem nomes de fase em inglês.
- **SD-002 e SD-003 (classificação):** a mesma regra da Série C.
  - 2020: Mirassol, Floresta-CE, Novorizontino, Altos, América-RN, Aparecidense;
  - 2021: 3º ABC, 4º Atlético Cearense, 5º Ferroviária-SP, 6º América-RN.
- **SD-017 (acesso):** em 2025 o acesso é do Santa Cruz (PE), e não do Santa Cruz de Natal; em 2020 o Floresta-CE é o 2º.

## Agente 2 (21/11/2026): revisão da Série C, parte 4 (o resto da Série C)

Pacote `bra-serie-c` refeito (sem commit). Recarregar no banco e no painel. Agora são 7.907 jogos (eram 7.910) e 369 clubes.

**Corrigidos:**
- **Clube trocado nos jogos:**
  - SC-008 (1988, grupo 18): Ferroviária-SP no lugar da Desportiva; o erro é do próprio ogol, corrigido jogo a jogo;
  - SC-009 e CL-001 (2007, grupo 17): os 6 jogos do Imperatriz;
  - SC-011 (2004): Atlético Sorocaba;
  - SC-012 (2003): Ituiutaba EC = Boa Esporte, 8 jogos;
  - CL-002 (2002): Tubarão FC, e não o CA Tubarão;
  - CL-004 (1995): SE Ariquemes, e não o Ariquemes FC.
- **Jogos de fora:**
  - SC-010 (2008): 2 jogos repetidos do grupo 15;
  - SC-013 (2011): os 3 jogos do Rio Branco-AC na 2ª fase. Com isso o 3º de 2011 é o Ipatinga, e o SC-003 fecha também
    em 2011.
- **SC-014 (placares):** 1988 Inter-SM 2x0 Figueirense; em 1992, 4 jogos (com Macapá 0x2 Nacional-AM); 2003 Atlético
  Roraima 1x2 Rio Branco-AC. Com isso o 3º de 1992 é o Nacional-AM, e o SC-003 fecha também em 1992. As tabelas da RSSSF
  de 1992 seguem os placares antigos e passam a divergir, com o motivo explicado no relatório.
- **SC-015 (1995):** Itumbiara x Gama fica como resultado do tribunal, 1x0 para o Itumbiara (`resultado_especial` = awd).
- **SC-007 (1988):** vitória vale 3; empate vale 2 para quem ganhou nos pênaltis e 1 para quem perdeu. O `pontos` da
  `classificacao_final` já sai assim, e `pontos_vitoria` de 1988 = 3. **Atenção:** se o painel recalcula pontos por
  3·V + E, em 1988 dá outro número; vale o do pacote. Marcílio Dias fica em 4º e Tiradentes-PI em 5º.
- **SC-017 (punições):**
  - 2005: Nacional-PB −6;
  - 2006: Ulbra-RO, Ypiranga-PE, Ceilândia e Ananindeua −6, Estrela do Norte −18;
  - 2007: Imperatriz −12 e Nacional-PB −6.

  A causa era a sigla repetida em grupos diferentes na Wikipédia em inglês: "NAC" era o Nacional-AM num grupo e o
  Nacional-PB em outro. Corrigi no leitor comum (`coleta/comum/wiki.py`), e isso vale também para a Série D. Em 2006 o −6
  é do Ananindeua, e não da Anapolina: o "Anapolina −6" do painel vinha desse erro. A perda de 12 pontos do Araguaína em
  2007 foi revertida e não entra.
- **SC-020 (datas):** ida e volta com a mesma data passam a usar a data do ogol (ou a da página, quando só ela separa os
  dois jogos), em 1994, 1998 e 2003.
- **Artilheiros:** SC-022 (1998: Kléber Pereira, Moto Club, 25) e SC-023 (Jones Carioca, Assisinho, Leandrão, Júlio César).
- **CL-031:** saiu o "ogol:JMalucelli" do Matsubara.

**Ficam como estão, anotados:**
- SC-016: placares em que só a Wikipédia diverge (RSSSF e ogol concordam);
- SC-018: a ordem do meio da tabela na Wikipédia segue outro critério;
- SC-021: totais em dúvida (1995 384 x 383, 1999 226 x 224 com os jogos-desempate, 2011 106 x 105, 2012 194 x 195);
- CL-012 (Joaçaba e São Borja 1981, Guarabira 2001): nome e ficha de clube fundado depois. Precisa de decisão: manter
  o clube do ogol ou criar um cadastro com o nome da RSSSF.

## Agente 2 (21/11/2026): revisão da Série D, parte 4 (o resto da Série D)

Pacote `bra-serie-d` refeito (sem commit). Recarregar no banco e no painel.

**Corrigidos:**
- **SD-014 a SD-016 (punições):**
  - 2009: Araguaia e Naviraiense −6;
  - 2010: América-AM −10;
  - 2012: Comercial-PI e Santos-AP −3;
  - 2013: Paragominas −6;
  - 2014: River-PI −4 e Villa Nova-MG −14;
  - 2015: Náutico-RR −4 e Santos-AP −3;
  - 2017: o −3 é do São Raimundo-PA, e não do -RR;
  - 2019: Bahia de Feira −3;
  - 2025: o −3 é do Maracanã, e não do Maricá.

  Os pontos batem com a revisão. Continuam as punições que a Wikipédia já dava (Colo Colo-BA 2015, Baré 2016,
  Itabaiana 2017).
- **SD-010:** Princesa 3x3 Manaus FC (2024); o total de gols de 2024 fica em 1.143, como na Wikipédia.
- **SD-012:** a ida da final de 2016 foi em 25/09.
- **SD-013:** os 3 W.O. de 2014 ficam com `resultado_especial` = awd, mantendo o 3x0. Se o painel não deve contar esses
  gols nos totais, o filtro é por esse campo.
- **SD-009:** observações em português (pênaltis só nos campos próprios; sem números soltos). Fiz um leitor comum em
  `coleta/comum/observacao.py`.
- **SD-018:** nomes de artilheiro sem o "- " na frente.

**Ficam como estão:**
- SD-011 (datas da semifinal de 2013): ogol e RSSSF dão 06/09 e 29/09, e a revisão diz "data exata a confirmar";
- SD-021: a própria revisão diz que está igual à fonte.

## Agente 2 (21/11/2026): revisão da Copa do Brasil, parte 4 (o resto da Copa)

Pacote `bra-copa-do-brasil` refeito (sem commit), e também `bra-serie-c` e `bra-serie-d` (observações e pênaltis).
Recarregar os três no banco e no painel.

**Corrigidos:**
- **CB-004 e CB-005 (placares):** placar diferente entre RSSSF e ogol agora fica com o do ogol. A revisão conferiu 10
  desses casos e o ogol estava certo em todos; são 15 jogos ao todo, e os 5 não conferidos seguem a mesma regra (1991
  Remo x Vasco, 1995 Nacional-AM x Cristal, 1998 Bahia x Botafogo-PB, 2002 América-RN x São Raimundo). O 1990 Santa
  Cruz x América-RN já tinha sido resolvido pela regra de mando da parte 1.
- **CB-007:**
  - 2007: saiu o "Rio Branco-PR 3x0 Villa Nova-MG", e a edição fica com 115 jogos;
  - 2019: saiu o Aparecidense 1x0 Ponte Preta anulado, e a edição fica com 120;
  - 2021: Sergipe 0x0 Cuiabá no lugar do "CRB", e a edição fica com 92 clubes;
  - 1999: a preliminar Santa Cruz 1x0 Náutico **não entrou**: não está nem na RSSSF nem no ogol, e falta a data.
- **CL-003:** em 2007 é o CEOV Operário (Várzea Grande), e não o Operário-MS. O ogol também errava; corrigido.
- **CB-008 (pênaltis):** os pênaltis vêm do placar do ogol ("2-1 (4-3 Pen.)") ou da nota da página. Agora são 218 disputas
  nos campos, com as finais de 2015 (Palmeiras 4x3) e 2017 (Cruzeiro 5x3). Fiz o mesmo na Série C (117) e na D (64).
- **CB-010 (datas):** as finais de 2014 e 2015 e Goiás x Flamengo (1990) ficam com as datas da Wikipédia. O ogol dá o dia
  seguinte em jogos à noite; isso pode acontecer em outros jogos cuja data veio do ogol.
- **TL-004:** ida e volta com a mesma data na Copa (2001) seguem a mesma regra da Série C.
- **CB-011 (artilheiros):** Dênis Marques no Athletico-PR (2007), Pipico no Santa Cruz (2019), Rômulo (2018) e Lorran
  (2023) entram, e os nomes em maiúsculas da RSSSF viram nome próprio ("Dênis Marques").
- **CB-015 e SD-009 (observações):** em português, sem datas soltas ("Feb 3"), sem a nota de campeonato de 1996 e sem
  pênaltis repetidos. Vale para a Série C, a D e a Copa.

## Agente 2 (21/11/2026): Paulista, classificação por rodada com a fase (resposta ao agente 1)

Pacote `bra-sp-1` refeito (sem commit). Recarregar no banco e no painel.

- `classificacao_rodada.csv` agora tem a coluna `fase`, depois de `temporada`:
  `temporada,fase,rodada,clube,posicao,pontos,jogos,vitorias,empates,derrotas,gols_pro,gols_contra,zona`. Na seção 4 do guia
  a coluna não existe; para os outros pacotes, ela é opcional.
- Uma tabela por fase de pontos corridos. Em 1996 e 1997 há mais de uma; nenhum clube repete rodada dentro da fase.
- Fica de fora a fase em que algum clube joga duas vezes na mesma rodada (rodada do ogol fora de ordem nos anos antigos,
  como 1926 APEA, que antes saía errado).
- Zona: "titulo" só na última fase; "rebaixamento" só na fase que reúne todos os clubes da edição.
- 1996: a 1ª fase (120 jogos) se chamava "Final", porque a página põe os jogos sob o título da tabela final. Agora é
  "Primeira fase".
- Ficam 24 temporadas com tabela rodada a rodada.

## Agente 2 (21/11/2026): edições de 2026 (SC-001, SD-001), sufixo (CL-027) e um aviso sobre a Série A

Pacotes `bra-serie-c` e `bra-serie-d` refeitos (sem commit). Recarregar no banco e no painel.

- **SC-001 (Série C 2026):** entra, com 216 jogos e 20 clubes, com os jogos do ogol, porque a RSSSF ainda não tem a página.
  - Maringá campeão e Ferroviária-SP vice;
  - acesso de Ferroviária, Inter de Limeira e Santa Cruz, além do Maringá;
  - rebaixados Confiança e Itabaiana (a Wikipédia lista só esses dois).
- **SD-001 (Série D 2026):** entra, com 610 jogos e 96 clubes em 16 grupos, também pelo ogol.
  - Uberlândia campeão e ASA vice;
  - os 6 acessos: Uberlândia, ASA, Gama, ABC, Nacional-AM e Goiatuba;
  - fase nova "Repescagem", entre as quartas e a semifinal: os perdedores das quartas jogaram pelas duas últimas vagas;
  - 14 clubes novos, que ainda não estão no banco.
- **CL-027 (sufixo "-UF"):** nada muda, pela decisão registrada em `docs/revisao/pedidos-painel.md`; os nomes dos
  pacotes ficam como estão.
- **`coleta/comum/ogol.py`:** a página do calendário agora só vale se o endereço canônico for o calendário daquela edição.
  Antes bastava ter um link para ela, e o ogol, quando limita os pedidos, devolve o calendário de outra competição com
  esse link no menu. Uma página do meio que falha não devolve mais o calendário pela metade. Conferi os caches da C, da D,
  da Copa, do Paulista e da Série B: todos limpos.
- **Aviso, Série A (área sua):** o cache `data/cache/ogol_serie_a/` tem 12 páginas que são de outras competições, e
  a validação antiga deixou passar. São estas:
  - 1991, páginas 1 e 2: Coca-Cola Cup 1996/97 (Escócia) e um campeonato de futsal de Portugal;
  - 1993, página 1: Liga da Guiné Equatorial 2003;
  - 1994, páginas 3 e 5: Eliminatórias da CAF 2006 e um campeonato juvenil de Braga;
  - 1995, páginas 1 e 4: Premier Liga 2009/10 (Bósnia) e um campeonato juvenil do Algarve;
  - 1997, página 4: Taça dos Campeões da CONCACAF 1994;
  - 1998, página 2: III Divisão de Portugal 1995/96;
  - 2008, página 3: Torneio Rio-São Paulo 1955;
  - 2009, página 4, e 2010, página 3: campeonatos juvenis de Coimbra e de Lisboa.

  Se a Série A usou o ogol desses anos, pode haver jogo de outra competição no banco. A conferência que usei foi:
  `rel="canonical"` com `/edicao/<slug>/<código da edição>/calendario`.
