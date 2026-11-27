# Pedidos do agente de coleta

> **Coleta Brasil (agente 2):** o estado de tudo, as regras e as pendências em ordem estão em
> `coleta/comum/COMECE-AQUI.md`; a documentação de cada competição (gerada por `coleta/comum/documentar.py`), em
> `coleta/comum/documentacao/` (índice no `README.md`).

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

## Agente 2 (21/11/2026): identidade de clubes, CL-005 a CL-011 (decisão do Guilherme)

Pesquisei cada caso: Wikipédia, sites dos clubes, federações, RSSSF, ogol, imprensa e, quando deu, o CNPJ. O
Guilherme decidiu seguir as recomendações. Pacotes `bra-serie-c` e `bra-copa-do-brasil` refeitos (sem commit); a
Série D já estava certa.

| Caso | Decisão | Nos pacotes |
|---|---|---|
| CL-005 São Gabriel (RS) | um clube só, o São Gabriel FC (2000-2013); o EC São Gabriel é de 2013 e não tem jogos nacionais | Série C 2002 passa de "EC São Gabriel" para "São Gabriel" (o da Copa 2004) |
| CL-006 Goiatuba (GO) | um clube só, o Goiatuba EC (1970; mesmo CNPJ, licenciado de 2009 a 2019); a AA Goiatuba é de 2009 | Série C 2003 passa de "Goiatuba" para "Goiatuba EC" |
| CL-007 Operário (Várzea Grande, MT) | três clubes: CEOV (1949), EC Operário (1996-2001) e Operário FC Ltda (2002, hoje Várzea Grande EC) | Copa 1995 e 1996 → "CEOV Operário"; Série C 1997 e Copa 1998 → "EC Operário-MT" (novo, sem ficha no ogol); Série C 2006 e Copa 2003, 2006 e 2007 → "Operário-MT" (o Operário FC Ltda) |
| CL-008 Lagarto (SE) | dois clubes: Lagarto EC (1955-1990) e Lagarto FC (2009) | Série C 1988 e 1990 → "Lagarto EC" (novo) |
| CL-009 Cabofriense (RJ) | dois clubes: AA Cabofriense (1955) e AD Cabofriense (1997) | Série C 1988 → "AA Cabofriense" (novo) |
| CL-010 Foz do Iguaçu (PR) | dois clubes: Foz do Iguaçu EC (1988-1999) e Foz do Iguaçu FC (1995) | nada nos meus pacotes; só a Série B 1989 muda |
| CL-011 Limoeiro (CE) | dois clubes: EC Limoeiro (1942) e AD Limoeiro (2001) | Série C 1998 → "EC Limoeiro" (novo) |

Corrigi também o CL-003 (Copa do Brasil 2007). Pela pesquisa, o Operário de 2007 é o Operário FC Ltda, campeão
mato-grossense de 2006, e não o CEOV, como eu tinha posto hoje.

**Para o banco e o painel (área sua):**
- **Série A 1968-1986 e Série B 1980-1992:** o "Operário-MT" desses anos é o CEOV e deve ir para "CEOV Operário". O nome
  "Operário-MT" fica para o Operário FC Ltda, com o escudo do Várzea Grande EC (hoje ele tem o do CEOV).
- **Série B 1989:**
  - "Lagarto" → "Lagarto EC";
  - "Cabofriense" → "AA Cabofriense";
  - "Foz do Iguaçu" → um novo "Foz do Iguaçu EC".
- **Série B 1989-1997, "Goiatuba":** é o Goiatuba EC; juntar com "Goiatuba EC" (os pacotes usam esse nome).
- **"EC São Gabriel"** não aparece mais em nenhum pacote. Juntar com "São Gabriel" ou tirar.
- **Clubes novos sem escudo:** Lagarto EC, AA Cabofriense, EC Limoeiro e EC Operário-MT. A AA Cabofriense e o EC
  Limoeiro existem até hoje e talvez tenham escudo na Wikimedia.
- **Fontes da pesquisa:** Wikipédia pt e en de cada clube, sites oficiais (lagartofc.com.br, fozfutebolclube.com.br,
  limoeirofc.com), FGF-GO, Federação Paranaense, RSSSF, ogol e CNPJ (Goiatuba EC 02.364.479/0001-70; Foz EC
  78.097.102/0001-64, baixado em 2008).

## Pedidos da revisão (21/11/2026): Paulista (`bra-sp-1`)

A revisão conferiu o pacote contra a Wikipédia (pt e en). Os achados estão em `docs/revisao/achados.csv` (SP-001 a SP-027,
com `quem_corrige` = `coleta-brasil`) e as provas em `docs/revisao/bra-sp-1.md`.

1. **Jogo falso (alta):** SP-011. Em 1928 LAF entrou um "Paulista 127 x 0 LAF", com data 0000-00-00 e contra um clube "LAF" que
   não existe. Ele vira o recorde de maior goleada do painel e entra na classificação.
2. **Vice e ordem final (alta):**
   - SP-002: vice errado em 14 edições;
   - SP-007: repescagem e torneio de rebaixamento contam como fase final (1951, 1998, 1999 e 2003; em 2003 o Botafogo-SP aparece como vice);
   - SP-008: a fase final verdadeira não decide a ordem (1957, 1976, 1978, 1997, 2024 e 2025; em 2025 o mata-mata está dentro de "Fase única");
   - SP-003: 3º lugar diferente da fonte em 29 edições.
3. **Dados que mudam o vice (alta):**
   - SP-009: em 1927 APEA, jogos do Corinthians de Santo André estão gravados como do Corinthians;
   - SP-010: 1927 LAF tem 15 clubes no banco, contra 10 na fonte;
   - SP-012: falta o jogo Corinthians x Palmeiras de 1942;
   - SP-013: falta a punição de 2 pontos do Palestra Itália em 1930;
   - SP-014: em 1988, o Juventus está no lugar de outro clube.
4. **Rebaixamento (alta):** SP-015. Falta a marca de rebaixado em 2014, 2015, 2017 a 2020 e 2022 a 2024, e há marca errada em 1994,
   1998, 1999 e 2002.
5. **Jogos, datas e totais (média e baixa):** SP-016 (W.O. sem placar fora da classificação), SP-017, SP-018, SP-019, SP-020,
   SP-021 (72 casos de clube com 2 jogos no mesmo dia) e SP-022 (observações em inglês).
6. **Artilheiros (média):** SP-023 e SP-024. Só 13 edições têm artilheiro no banco, e 8 delas vêm da contagem dos gols com autor.
7. **Aguardam decisão do Guilherme:**
   - SP-001: título de 1973 dividido entre Santos e Portuguesa;
   - SP-004: edição de 2026;
   - SP-005: amadores da FPF em 1933 e 1934;
   - SP-006: "Paulistinha" de 1970 e de 1972 a 1974;
   - SP-026: juntar AA São Bento e São Bento de São Paulo;
   - SP-027: juntar CA Paulista e ECPaulista.

Quando corrigir, cite os ids aqui. A revisão confere de novo.

## Agente 2 (21/11/2026): identidade de clubes, CL-012 (decisão do Guilherme)

Pesquisados como os anteriores. Nos três casos, quem jogou foi um clube antigo, diferente do clube do cadastro.
Pacote `bra-serie-c` refeito.

| Ano | Antes | Agora (ficha do ogol) | Por quê |
|---|---|---|---|
| 1981 | "Joaçaba" (Joaçaba AC, 1997) | "Joaçaba EC" (238972; 1977, extinto nos anos 1980) | o Joaçaba AC vem da AD Joaçaba (1989), não do EC |
| 1981 | "São Borja" (EC São Borja, 2009) | "SE São Borja" (241325; 1977) | outra pessoa jurídica; o EC de 2009 só herdou escudo, cores e estádio |
| 2001 | "Desportiva Guarabira" (AD Guarabira) | "Guarabira EC" (89206; 1936, extinto em 2004) | a AD Guarabira vem do Juventus EC, não do Guarabira EC |

**Para o banco (área sua):** "Joaçaba", "São Borja" e "Desportiva Guarabira" só existiam por causa desses anos da
Série C. Viram os clubes novos (ou saem). Os escudos atuais são dos clubes de hoje; os novos ficam sem escudo
(Wikimedia, se houver).

## Agente 2 (21/11/2026): artilheiros da Série A (resposta ao pedido do agente 1)

Pronto em `data/coleta/bra-serie-a-artilheiros/artilheiros.csv` (`temporada,jogador,clube,gols,fonte`). Relatório em
`docs/coleta/bra-serie-a-artilheiros.md`.
- 70 edições (todas as do banco, de 1937 a 2025) e 84 linhas, com os empates em linhas separadas.
- A `temporada` é a `chave` da edição ("1967_robertao", "1967_taca_brasil"...). O `clube` é o nome do banco; todos
  casaram.
- Fonte: Wikipédia en (lista de artilheiros por temporada), conferida com a lista pt.
- Atende SA-019 a SA-023:
  - 2007: Josiel, 20;
  - 2008: Keirrison, Kléber Pereira e Washington, 21;
  - 2016: Fred, 14, numa linha só com o Atlético-MG ("gols somados de dois clubes");
  - nomes de jogo: Josiel, Luciano, Alerrandro.

## Resposta do agente 1 (21/11/2026): correções, identidade e artilheiros no banco

- Banco remontado com os pacotes novos (C, D, Copa, Paulista), a identidade CL-005 a CL-012 e as renomeações.
- Artilheiros oficiais da Série A (`data/coleta/bra-serie-a-artilheiros/artilheiros.csv`) carregados pela montagem
  (`artilheiros_serie_a` em `futebol/migrar_brasileirao.py`); a sub-aba Artilharia mostra a lista oficial primeiro.
- Cache do ogol da Série A: as páginas erradas foram apagadas e os anos 1977, 1980, 1989, 1991, 1993-1995,
  1997-1999 e 2008-2010 baixados de novo com o `coleta/comum/ogol.py` validado (1995 tinha jogos da Bósnia).
- Edições de 2026: carregadas como vêm no pacote; a decisão sobre mostrá-las segue com o Guilherme.

## Agente 2 (21/11/2026): Paulista Série A2 (`bra-sp-2`) pronto

Pacote em `data/coleta/bra-sp-2/pacote/` (mesmo formato do `bra-sp-1`); relatório em `docs/coleta/bra-sp-2.md`.
Código em `coleta/bra-sp-2/` (cópia do importador do Paulista, com as fontes da A2).

- **37 edições com os jogos:** 1979, 1985-1988 e 1995-2026. 8.649 jogos, 20.887 gols (4.526 com autor, de 2013 em diante),
  99 clubes (61 já no banco), 124 tabelas conferidas e 30 divergentes (explicadas no relatório).
- `competicao.json`: `tipo` estadual, `nivel` 2, `regiao` SP, `rotulo_painel` "Paulista A2", `do_painel` "da Série A2".
  O `nome_oficial` muda por época (Segunda Divisão, Divisão Intermediária, Divisão Especial, Série A2).
- **Acesso** (`situacao` = "acesso"): o clube que joga a 1ª divisão do ano seguinte no pacote `bra-sp-1`.
- **2026:** só pelo ogol (a RSSSF ainda não tem a página); campeão Juventus-SP.
- **Fontes:** RSSSF de 1979 a 2025; ogol de 1998 em diante (antes disso o ogol não tem os jogos).

**Identidade antes de 1998 (sem ogol):** o nome da página foi casado com as fichas do ogol (A2 e A1) pela cidade da
lista de participantes. Não vale ficha de clube fundado depois da edição. Casos que mudam o que já existe:
- "Votuporanguense" dos anos 1980 é a AA Votuporanguense, clube novo; não é o "CA Votuporanguense" do banco (de 2009).
- "EC Lemense" (anos 1980) é clube novo; não é o "Lemense" (Lemense FC, 2005).
- Clubes novos que levam a cidade no nome, para não repetir o nome de outro clube:
  - "Palmeiras (São João da Boa Vista)";
  - "Internacional de Bebedouro";
  - "União Mogi".
- "Ferroviário Ituano" = Ituano; "Catanduva" (1995) = Catanduvense; "Etti Jundiaí" (campeão de 2001) = Paulista.

**Mudança em `coleta/comum/rsssf.py`:** `<br>` com atributos em outra linha (`<br\r\n style=...>`) agora quebra a
linha (a página da A2 de 2021 vinha inteira numa linha só). Conferido: nenhuma página da C, D e Copa tem isso. A
única do Paulista é a de 2014, que dá o mesmo resultado antes e depois (155 jogos, 0 divergências).

**Fora do pacote (decisão pendente com o Guilherme):** edições sem os jogos em nenhuma fonte:
- 1947-1966: só a classificação em pontos e os jogos do campeão;
- 1989: só a 1ª fase;
- 1991: só a 2ª fase;
- 1992-1994: só a classificação.

## Agente 2 (22/11/2026): Paulista A2 (`bra-sp-2`) com as edições antigas e incompletas

O Guilherme decidiu incluir tudo o que existir. O pacote foi regravado e as edições de 1995 a 2026 não mudaram.

- **Totais:** 63 edições (eram 37), 9.142 jogos, 167 clubes.
- **Edições novas:**
  - **1947 a 1966:** inclui 1965, que não tem página na RSSSF e vem da Wikipédia em português.
  - **1990:** também só na Wikipédia em português.
  - **1992 a 1994.**
- **Edições sem jogos ou com parte dos jogos:** seguem o padrão do `uru-1` e do `par-1`, e o `formato` diz o que cada uma tem:
  - **Sem jogo nenhum:** 1947, 1993 e 1994. Têm só `edicoes.csv`, `classificacao_final.csv` e `tabelas_publicadas.csv`. O `formato` começa com "sem jogos".
  - **Com parte dos jogos:** as outras. O `formato` começa com "jogos incompletos". Os jogos vêm da Wikipédia em português: `fonte` "Wikipédia (pt)", `fonte_id` "wikipedia:pt_<ano>:<linha>". São finais e fases finais de 1948 a 1966, a 4ª fase de 1990, a 2ª fase e o quadrangular de 1992, e as semifinais de 1989.
  - **Classificação por rodada:** essas edições não têm `classificacao_rodada`.
- **Classificação final dessas edições:**
  - **Fonte:** as tabelas publicadas.
  - **Ordem:** o campeão da lista da RSSSF; o vice, que é o outro finalista; depois a fase alcançada, a posição no grupo e os pontos da última fase.
  - **Colunas numéricas:** preenchidas só quando há uma tabela só (1947, 1960 e 1994). Nas outras ficam vazias, e a `observacao` da linha traz os pontos de cada fase.
  - **Posição repetida:**
    - Em 1992 e 1993 a página dá só faixas, por exemplo do 5º ao 12º, e os clubes da faixa ficam com a posição do começo dela.
    - Em 1990, os 20 eliminados antes da 4ª fase ficam todos em 7º.
  - **Pedido:** que o painel aceite colunas vazias e posição repetida, como no `par-1`.
- **1989 e 1991:**
  - Agora entram, com o `formato` marcado "(jogos incompletos)".
  - O campeão de 1991 é o Araçatuba, à frente do Lemense pelo saldo. A página da RSSSF diz "Lemense" por engano.
- **Clubes:** são 63 novos no cadastro comum (`rs-...`). Nenhum nome que já existia mudou, nenhum se repete e nenhum é igual a um nome do banco. Identidades que mudam o que você conhece:
  - o Barretos FC (até 1960) não é o Barretos EC, de 1960;
  - o Catanduva EC dos anos 1950 não é o GE Catanduvense, de 1970;
  - a AA Osvaldo Cruz não é o Osvaldo Cruz FC, de 2004;
  - o Araçatuba FC de 1954 não é a AE Araçatuba, de 1972.

  Homônimos levam a cidade, por exemplo "Ferroviária (Botucatu)" e "São Paulo (Araçatuba)".
- **Fontes novas guardadas em `data/coleta/bra-sp-2/wikipedia/`:**
  - o código das páginas, em `pt_<ano>.wiki`;
  - os jogos transcritos, em `jogos_pt.csv`. Os 244 jogos com placar foram conferidos um a um no código das páginas.

## Revisão profunda (22/11/2026)

- **87 ids abertos** para a coleta Brasil; **25 altos**; **13 no ar** (todos do Paulista).
- Competições: Paulista (`bra-sp-1`) 41, Paulista A2 (`bra-sp-2`) 28, Série C 8, Série D 3, Copa do Brasil 5, e 2 ids
  que valem para as três (C, D e Copa).
- Plano pronto, em ordem e por arquivo do código: `docs/revisao/plano-coleta-brasil.md`. Começar só quando o Guilherme
  mandar.
- Decisões que esperam o Guilherme: `docs/revisao/decisoes-guilherme.md`. Fontes: `docs/revisao/fontes.md`.

## Decisões do Guilherme (22/11/2026), da revisão profunda

O Guilherme respondeu às decisões D-01 a D-25 de `docs/revisao/decisoes-guilherme.md`:
- **D-01:** opção A. Tudo o que já terminou entra agora, inclusive o Paulista 2026 e os Aperturas 2026 da Argentina e do
  Paraguai.
- **D-10:** opção B. As edições não oficiais das Séries B e C entram com aviso, sem contar título (SB-026, SC-029, TL-005).
- **As outras:** vale a recomendação de cada uma.

Os ids que esperavam essas decisões estão liberados no seu plano. As correções continuam esperando a largada do Guilherme.

## Recado de fim de coleta — bra-rj-1 — 22/11/2026

Para o agente 1 (banco e painel) e o agente de revisão. Ficha completa: `coleta/comum/documentacao/bra-rj-1.md`;
relatório ano a ano: `docs/coleta/bra-rj-1.md`.

1. **O que foi feito:** Campeonato Carioca (1ª divisão).
   - 128 edições, de 1906 a 2026. As ligas rivais têm uma edição cada: 1912 (AFRJ e LMSA), 1924 (LMDT e AMEA), 1933 e 1934 (AMEA e LCF), 1935 e 1936 (FMD e LCF). 1979 tem o campeonato normal e o Especial.
   - 14.118 jogos, 83 clubes (29 já no banco), 3.383 gols com autor (quase todos de 2010 em diante) e nenhum cartão.
   - Tabelas publicadas: 222 fecham com os jogos e 128 divergem.
   - Fontes:
     - RSSSF Brasil (`tablesr/rj{ano}.htm`; não há página de 2025 nem de 2026);
     - ogol, competição 893, de 1906 a 2026, que dá a identidade dos clubes e completa os jogos;
     - Wikipédia em português: campeões e vices de cada ano, como segunda fonte.
   - O campeão bate com a RSSSF e com a Wikipédia em todas as edições.
2. **Commit:** o deste recado (Carioca, documentação e a opção nova do leitor comum).
3. **Teste de carga:** `bra-rj-1: 128 edições, 14118 jogos, 54 clubes novos -> OK`. O carregador avisa que ignora a tabela por rodada em 1997, 1999, 2000, 2017 e 2021, que têm mais de uma fase.
4. **Pedidos ao banco e ao painel:**
   - **Carregar `bra-rj-1`.** `competicao.json`: `tipo` estadual, `nivel` 1, `regiao` RJ, `rotulo_painel` "Carioca".
   - **Ligas rivais:** a `temporada` leva a liga ("1933 AMEA"), como no Paulista.
   - **W.O. sem placar:** `resultado_especial` "awd", sem gols, com o vencedor na `observacao`. Vêm do ogol (1908-1935), e o vencedor saiu da tabela publicada.
   - **Desempate de 1921:** fica 2-1 na prorrogação.
   - **Nomes:** nenhum nome que já existia no cadastro comum mudou e nenhum se repete. Bonsucesso e Serrano são os mesmos clubes do banco (Série B).
5. **Decisões:**
   - **Que eu tomei:**
     - os torneios de consolação entre os turnos (2009-2012) e as finais das séries de subúrbio (1928-1930) ficam fora;
     - na classificação, os turnos (Taça Guanabara e Taça Rio) contam como a 1ª fase, e do 3º em diante vale a soma dos pontos, como a classificação final publicada;
     - o torneio de rebaixamento e a Taça Rio dos clubes de baixo (2016) não contam como avanço;
     - o artilheiro de 1979 segue a RSSSF (a Wikipédia inverte o normal e o Especial).
   - **Que esperam o Guilherme:**
     - **1907, título dividido entre Fluminense e Botafogo:** hoje só o Fluminense. Pela D-07 (Paulista 1973 com dois campeões), deve ter os dois, no formato que o agente 1 definir para dois campeões.
     - **1937:** a Wikipédia conta o São Cristóvão campeão pela FMD; a RSSSF diz que o torneio ficou inacabado. Hoje só a LFRJ (Fluminense).
6. **O que não deu e pendências:**
   - **Autores dos gols** fora dos anos 2010: as páginas antigas trazem "Gols: ..." numa linha à parte, que o leitor ainda não junta ao jogo.
   - **Artilheiros de 2015 em diante:** a lista da RSSSF parou em 2014. A Wikipédia em português tem a tabela ano a ano (`pt_lista.txt`).
   - **W.O. que a tabela não decide** (ex.: 1910): ficam fora.
   - **Cartões:** só jogo a jogo, pela ficha do ogol.
   - **No Paulista:** a mesma leitura de artilheiros nunca usava a lista da RSSSF (a chave era o ano em número), o que deve explicar o SP-024.
7. **Onde a revisão deve olhar primeiro:**
   - as 128 tabelas divergentes, concentradas nos anos dos turnos (2008-2013) e nos anos 1910;
   - a identidade dos clubes antigos que só a RSSSF tem (Petropolitano, Miguel Couto, Paduano, União Nacional, Olympico, Saquarema) e dos casados à mão (`NOME_MANUAL`);
   - os W.O. decididos pela tabela;
   - os jogos avulsos do fim das páginas que ficaram (súmulas sem par na lista: 1915, 1917-1919, 1924 AMEA, 1925, 1938, 1944, 1959, 1976).
8. **Próximo campeonato:** Mineiro (`bra-mg-1`), com o ok do Guilherme. A RSSSF Brasil ficou fora do ar em 22/11; se voltar, começo por ela.

## Recado de correção — bra-rj-1 — 23/11/2026 (1907 e 1937)

Decisão do Guilherme (23/11), depois de pesquisa: valem os títulos que a FERJ reconhece.

1. **1937 FMD (edição nova):**
   - É o torneio da FMD, que parou na 8ª rodada com a pacificação das ligas. Tem 26 jogos, só da RSSSF (o ogol não tem essa edição).
   - Campeão: São Cristóvão (invicto, 7 vitórias em 7 jogos). A FMD o proclamou em 03/09/1937 e a FERJ homologou o título em dezembro de 2023 (Super Rádio Tupi, 09/01/2024; Wikipédia em português).
   - A temporada "1937" continua sendo a da LFRJ, com o Fluminense campeão. O nome dela não muda.
   - O Carioca agora tem 129 edições e 14.144 jogos, sem clube novo.
   - O que muda nas tabelas: a da FMD, antes presa à "1937" como divergente, agora fecha na "1937 FMD". São 223 tabelas que fecham e 127 que divergem.
   - testar_carga: `bra-rj-1: 129 edições, 14144 jogos, 0 clubes novos -> OK`.
2. **1907 (título dividido):**
   - Fluminense e Botafogo são os dois campeões: a FERJ os declarou em 1996.
   - Enquanto o banco aceita um campeão só, o pacote fica assim:
     - `campeao` = Fluminense;
     - `vice` vazio (o Botafogo não é vice);
     - o Botafogo na `observacao` de `edicoes.csv`.
3. **Pedidos ao banco e ao painel:**
   - Recarregar o `bra-rj-1` (edição nova "1937 FMD", com aviso de torneio inacabado na observação).
   - Quando definir o formato de dois campeões numa edição (D-07, Paulista 1973), aplicar também ao Carioca 1907. Basta me dizer o formato, que eu ajusto o pacote (`importar.CAMPEOES_DIVIDIDOS`).
   - O título de 1937 FMD conta para o São Cristóvão, que passa a ter 1926 e 1937.
4. **Commit:** "Carioca: 1937 FMD (São Cristóvão) e 1907 dividido", com o ok do Guilherme.


## Resposta do agente 1 — formato de título dividido (D-07) — 23/11/2026

Para o agente de coleta do Brasil (e a revisão, para fechar SP-001 quando o Paulista chegar).

1. **Formato:** coluna nova e opcional `co_campeao` em `edicoes.csv`, logo depois de `vice`, com o nome do outro
   campeão (o mesmo nome de `clubes.csv`). Fica vazia nas outras edições.
   - `campeao` continua sendo o 1º da classificação; `co_campeao` é o outro campeão, esteja onde estiver na tabela.
   - `vice` é o próximo colocado que não é campeão (Paulista 1973: Palmeiras). Pode ficar vazio, como no Carioca 1907.
   - A classificação final não muda: as posições seguem a fonte.
2. **Banco:** `edicao.co_campeao_id` (`futebol/esquema.sql`); o `carregar_pacotes.py` lê a coluna. Pacote sem a coluna
   carrega igual.
3. **Painel:** o título conta para os dois (títulos, corrida, curiosidades); o pódio da edição mostra os dois no degrau
   do meio; o vice e o 3º do histórico pulam o co-campeão.
4. **Carioca 1907:** pus a coluna à mão no `data/coleta/bra-rj-1/pacote/edicoes.csv` (Botafogo) e publiquei. Falta o
   `pacote.py` gravá-la a partir de `importar.CAMPEOES_DIVIDIDOS`; senão, a próxima geração do pacote a apaga.
   A observação de 1907 pode perder o trecho "até o banco aceitar dois campeões".
5. **Paulista 1973 (SP-001):** não mexi, porque o pacote está com correções suas em andamento. Quando fechar:
   `co_campeao` = Santos e `vice` = Palmeiras.

## Correções da revisão — bra-sp-1 — 23/11/2026 ("ERRADO NO AR" do Paulista)

O Guilherme mandou corrigir pelo plano `docs/revisao/plano-coleta-brasil.md`. Este é o primeiro bloco: os altos do Paulista que já estão no site.

1. **Corrigidos** (tudo em `coleta/bra-sp-1/importar.py`, com o motivo e a fonte ao lado de cada linha):
   - **SP-011:** fora o jogo falso "Paulista 127 x 0 LAF" (ogol 2591655, `OGOL_IGNORAR`). O clube "LAF" (999999) saiu do cadastro comum. 1928 LAF tem agora 12 clubes.
   - **SP-002, SP-007, SP-008:**
     - `ORDEM` passa a ter todas as fases: repescagem, torneio de rebaixamento e desempate valem 0, e os turnos valem 1. Fase sem nível agora faz o importador parar com erro (antes caía em 50).
     - O vice do quadrangular final é o 2º do grupo.
     - Quem chegou à "Fase final" desempata pelos pontos dela.
     - `FASE_ANO`: 1976.
     - `FASE_JOGO`: 1978, 1981, 1998 e 2003.
     - Vices certos agora em 1951, 1957, 1976, 1978, 1997 e 2003; 3º certos em 1951, 1957, 1976, 1989, 1997, 1998, 1999 e 2003.
   - **QS-001 e SP-010** (`CLUBES_FORA`): saem os jogos cancelados dos clubes que abandonaram:
     - 1913 LPF, 1914 LPF, 1923, 1924, 1925, 1928 APEA, 1935 APEA e 1938;
     - 1927 LAF, com 10 clubes: saem Corinthians, Independência, Sírio, Sílex e Taubaté.
   - **QS-006** (`JOGOS_FORA`): saem os 2 jogos de 1916 APEA fora da tabela. Vice: AA São Bento.
   - **QS-005:**
     - fora o SPAC 1-9 Internacional;
     - entram os 7 jogos com pontos dados ao adversário (`JOGOS_EXTRA_WO`, sem placar);
     - vice SC Internacional (`VICE_OFICIAL`: a AA das Palmeiras foi eliminada pela LPF).
   - **QS-015 e SP-013** (`PONTOS_FORA_DE_CAMPO`): os 12 jogos agora vão como W.O. para quem ganhou os pontos, sem gols (D-15), e o placar de campo fica na observação. 1930: vice São Paulo. 1984: 3º São Paulo.
   - **SP-016:** o W.O. sem placar ("victory awarded to X") conta como vitória sem gols. 1927 LAF ganha o W.O. SC Internacional x Paulista de 30/10 (página e FN).
   - **SP-009:** "Corinthians (SBC)" volta a ser o Corinthians de Santo André (81207), em 13 jogos. Com isso some o jogo repetido de 21/08 e o vice passa a ser o Santos.
   - **SP-012:** 1942 Corinthians 3-1 Palmeiras (04/10/1942), placar pelo FN (a página não tinha os gols do Palmeiras). Vice: Corinthians.
   - **SP-001 (D-07):** 1973 com campeao Portuguesa, `co_campeao` Santos e vice Palmeiras, no formato do agente 1 (coluna `co_campeao` de `edicoes.csv`, gravada pelo `pacote.py` a partir de `importar.CAMPEOES_DIVIDIDOS`).
   - **Carioca 1907, no mesmo formato:** o `coleta/bra-rj-1/pacote.py` agora grava `co_campeao` = Botafogo (antes estava à mão no pacote), e a observação perdeu o trecho "até o banco aceitar".
2. **Números:**
   - 134 edições, 21.791 jogos (eram 21.855).
   - Tabelas publicadas: 213 fecham e 129 divergem (eram 207 e 135).
   - testar_carga: `bra-sp-1: 134 edições, 21791 jogos, 0 clubes novos -> OK`.
3. **Não feito neste bloco:**
   - SP-008 em 2024 e 2025: as fases dependem da API da FPF, que é o mesmo leitor do QS-008 e do SP-004.
   - Os 3º lugares que sobram do SP-003.
   - 1927 LAF: o 3º é a AA São Bento, empatado com o Paulista na tabela da RSSSF. A Wikipédia dá o Paulista.
   - 1930: o 3º é o Santos, empatado com o Palestra na tabela da RSSSF. A Wikipédia dá o Palestra.
4. **Pedidos:**
   - **Ao agente 1:** recarregar o `bra-sp-1` e o `bra-rj-1` (os dois com a coluna `co_campeao`).
   - **À revisão:** depois da recarga, rodar as varreduras `revisao/tela/varredura.py` e `revisao/tela/datas_repetidas.py`. Elas leem o banco.
5. **Próximo bloco:** o "ERRADO NO AR" da A2 (A2-001 a A2-011).

## Correções da revisão — bra-sp-2 — 23/11/2026 ("ERRADO NO AR" da A2, menos o A2-001)

1. **Corrigidos** (em `coleta/bra-sp-2/`, com o motivo e a fonte ao lado de cada linha):
   - **A2-002 a A2-005** (`importar.classificacao`): quem chegou à "Fase final" de um grupo só desempata pelos pontos dela; o vice do quadrangular final é o 2º do grupo. Vices: 1979 Santo André, 1986 Noroeste, 1996 Portuguesa Santista, 1997 Ituano. Também o 3º de 2004, que passa a ser o Taquaritinga (A2-018).
   - **A2-006:** na classificação geral publicada, o campeão e o outro finalista vão para 1º e 2º. 2013: vice Rio Claro.
   - **A2-007** (`importar.REBAIXADOS_WIKI`): rebaixados pelo infobox da Wikipédia pt em 2000 e de 2012 a 2026, nos anos em que a RSSSF não marca. O importador para com erro se um nome não estiver na classificação.
   - **A2-008:** "Relegation Playoff" não é queda; a marca exige "Relegated"/"rebaixado". 1999: Juventus e Paraguaçuense sem "rebaixado".
   - **A2-009** (`pacote.clubes_a1_por_ano`): acesso só para quem jogou a 1ª divisão no ano seguinte. Repescagem, torneio de rebaixamento e playoff A1 x A2 (até 4 jogos) não contam. Sem acesso: XV de Jaú 1950, Catanduvense 1979, Francana 2001 e Atlético Sorocaba 2002.
   - **A2-010:** o playoff de 2002 é Francana x Portuguesa Santista (`NOME_MANUAL`); a Lusa da capital saiu da A2 de 2002.
   - **A2-011:** 2001 com a regra da página: empate vai para os pênaltis, com 2 e 1 pontos (ou 1 e 0 no 0-0). Também a punição de -5 do Sãocarlense (`AJUSTES_MANUAIS`) e nenhum rebaixado (`SEM_REBAIXAMENTO`: "saved from relegation"). A tabela publicada agora é lida (`rsssf_sp2._tabela_2001`). Os pontos dos 16 clubes batem com ela.
   - **A2-017:** Nacional 0-1 Ituano (03/03/2001), como o ogol. Só esse placar fecha com a tabela.
2. **Números:** 63 edições, 9.142 jogos (sem mudança). testar_carga: `bra-sp-2: 63 edições, 9142 jogos, 0 clubes novos -> OK`.
3. **Pedido ao agente 1:** recarregar o `bra-sp-2` (situação de acesso e rebaixado, vices e a ordem de 2001).
4. **Próximo:** A2-001, as 17 edições de 1967-1978 e 1980-1984. É o maior bloco do plano.

## Correções da revisão — bra-sp-2 — 23/11/2026 (A2-001: edições de 1967-1978 e 1980-1984)

1. **Feito:** as 17 edições que faltavam entram como "jogos incompletos" ou "sem jogos", como as de 1947-1966.
   - **Participantes:** lista da RSSSF (`sp2list.htm`, com a cidade).
   - **Tabelas de pontos e jogos:** página de cada edição na Wikipédia em português, baixada por `coleta/bra-sp-2/baixar_wiki.py`. Os jogos vêm das caixas "footballbox" e das linhas de texto. 1972 não tem página.
   - **Pódio:** vice, 3º e 4º da predefinição de campeões da A2 na Wikipédia. O 3º e o 4º só valem para quem chegou à fase mais avançada (em 1980, o Ginásio Pinhalense, 4º na predefinição, não jogou a semifinal).
   - **Campeão:** pela lista da RSSSF, como sempre. O campeão e o vice batem com a lista oficial nos 17 anos, e o 3º com a predefinição.
2. **Decisões:**
   - São José dos Campos (D-23c revista pelo Guilherme em 23/11): é um clube só (São José-SP). O "Esporte Clube São José" (1933) só mudou de nome em 24/12/1976.
   - 1983: o "rebolo" Noroeste x Taubaté (0-1 e 0-1) fica só na observação (D-04).
3. **Números:**
   - 80 edições (eram 63) e 9.223 jogos (eram 9.142).
   - 16 clubes novos, só da RSSSF: Andradina, Ituveravense, Ferroviário de Araçatuba, São Carlos Clube, Vasco da Gama (Americana), Tião Maia, Estrela da Bela Vista, José Bonifácio, Presidente Prudente, Americana, Independência (Osasco), MAF, Aparecida, Campo Limpo, Rio Branco (Ibitinga) e Barra Bonita.
   - Nenhum nome antigo mudou e não há nome repetido no cadastro.
   - testar_carga: `bra-sp-2: 80 edições, 9223 jogos, 16 clubes novos -> OK`.
4. **Pedido ao agente 1:** recarregar o `bra-sp-2`. Os títulos por clube mudam, por exemplo XV de Piracicaba, Noroeste, Santo André e Catanduvense.
5. **Pendências:**
   - Os jogos dos campeões nas páginas da RSSSF de 1968, 1969, 1971, 1976, 1980 e 1984 ainda não entraram.
   - A final de 1972 (São José x Garça, 3-0 e 0-0) não tem data nem mando.
   - Identidade a conferir pela revisão: Vasco da Gama (1969) e Americana (1976), os dois de Americana; e o Presidente Prudente FC (1974).
6. **Com isso termina o "ERRADO NO AR" do plano.** O resto segue quando o Guilherme mandar.


## Correções da revisão — bra-sp-1 — 24/11/2026 (parte 1: jogos)

O Guilherme mandou seguir o resto do plano `docs/revisao/plano-coleta-brasil.md`, competição a competição. O Paulista vai em 4 partes: jogos, leitor da API da FPF, `pacote.py` e pódio. Esta é a parte 1.

1. **Corrigidos** (em `coleta/bra-sp-1/importar.py` e `rsssf_sp1.py`, com o motivo e a fonte ao lado de cada linha):
   - **SP-014:** 1988 sem a Ponte Preta e o Bandeirante (`RSSSF_FORA`). A página lista os jogos cancelados dos dois, e o leitor punha a Ponte Preta no lugar do Juventus. Ficam 20 clubes e 216 jogos, os mesmos do ogol.
   - **QS-013:** 1956, fora o Taubaté 2-2 Corinthians de 21/11 (`JOGOS_ANULADOS`). A tabela da página só fecha sem ele; fica o 0-2 de 23/12.
   - **QS-009:** jogo abandonado sem "result stands" fica sem placar e fora da campanha, e não pega mais o placar do jogo refeito. 2000: Matonense x Portuguesa de 26/01. 2004: Juventus x Ponte Preta de 31/01; o 0-3 é o de 11/02.
   - **QS-004:** 1969, o jogo do 2º turno é Corinthians 1-1 Santos (25/05). A página repetia ali o 1-3 do turno final (08/06), que fica na Final.
   - **QS-002 e QS-003:** datas de 1929 LAF (09/06/1929) e de 1979 (sete jogos em 19/08/1979), corrigidas na página. Quando o ano da RSSSF e o do ogol diferem, fica o que cai no ano da edição.
   - **QS-007 e SP-018** (`JOGOS_EXTRA`, pelo Futebol Nacional):
     - 1916 LPF: 4 W.O. contra o Ruggerone;
     - 1920: 2 W.O. do Santos (o "Mack-Port" da página é a Portuguesa);
     - 1929 LAF: AA das Palmeiras 3-2 Atlético Santista (28/04);
     - 1957: São Bento de SCS 1-0 Linense (19/10, Série Branca);
     - 1966: o desempate do rebaixamento Guarani 3-1 Noroeste (22/12, fase "Desempate", nível 0).
   - **QS-012** (`JOGO_CORRIGIDO`): placares pelo FN e pelo ogol:
     - 1952: Radium 3-2 Palmeiras e Ypiranga 3-1 Nacional;
     - 1981: XV de Jaú 1-1 São Paulo;
     - 1995: Santos 4-1 Ponte Preta;
     - 1999: Rio Branco 2-1 São José;
     - 2014: XV de Piracicaba 1-3 São Paulo, também pela FPF.

     Em 1998, o 2-4 do torneio do descenso volta para 22/03, e o 2-1 da 1ª fase fica com 11/02.
   - **SP-019:** em 2002, Francana x Portuguesa Santista (02 e 05/06) passa para "Repescagem", nível 0. Os outros totais por edição saem dos itens acima.
   - **Vice de 1928 APEA** (do SP-003): sai o 3º jogo Palestra x Portuguesa (29/07, 6-3), que o ogol não tem; sem ele as campanhas fecham com a tabela da RSSSF. Vice: Santos.
2. **Números:**
   - 134 edições e 21.775 jogos (eram 21.791).
   - Tabelas publicadas: 218 fecham e 124 divergem (eram 213 e 129).
   - A A2 foi rodada de novo e não muda, porque o acesso lê os jogos do Paulista.
   - testar_carga: `bra-sp-1: 134 edições, 21775 jogos, 0 clubes novos -> OK`.
3. **Pódio que muda:** 1928 APEA (vice Santos, 3º Palmeiras) e 1988 (3º São Paulo, 4º São José).
4. **Pedido ao agente 1:** recarregar o `bra-sp-1`.
5. **Próximo, parte 2:** leitor da API da FPF, para as datas de 2007 em diante (QS-008, SP-021), as fases de 2024-2025 (SP-008), a edição de 2026 (SP-004) e a artilharia.

## Correções da revisão — bra-sp-1 — 24/11/2026 (parte 2: FPF e 2026)

1. **Feito:**
   - **Fonte nova:** a API do site da FPF, a fonte oficial. `coleta/bra-sp-1/baixar_fpf.py` grava em `data/coleta/bra-sp-1/fpf/` os jogos (2007-2026) e a artilharia de cada ano. `fpf_sp1.py` casa cada jogo da FPF com o do pacote pelo par de clubes, pela data (até 10 dias) e pelo placar.
   - **QS-008:** de 2007 em diante vale a data da FPF. Mudam 68 jogos, os mesmos do achado (2007 3, 2008 2, 2009 1, 2010 2, 2011 2, 2012 10, 2013 13, 2014 5, 2016 1, 2018 1, 2021 3, 2022 7, 2024 6, 2025 12). A hora entra quando falta.
   - **SP-008 (2024 e 2025):** fase e grupo pela FPF: Primeira fase com os grupos A a D, quartas, semifinal e final.
     - 2024: a final sai da "Semifinal".
     - 2025: quartas, semifinal e final saem da "Fase única"; 3º São Paulo e 4º Santos.
   - **SP-004 (D-01):** entra a edição de 2026, com 72 jogos.
     - Os jogos vêm do ogol, e a fase e a data da FPF. A RSSSF ainda não tem a página.
     - Pódio: campeão Palmeiras, vice Novorizontino, 3º São Paulo, 4º Corinthians.
     - O Primavera estreia na 1ª divisão, mas já estava no cadastro comum pela A2.
   - **SP-021 (em parte):** clubes com dois jogos no mesmo dia caem de 70 (antes da parte 1) para 56. Saem 1988 e 2022. Os que sobram são de 1906 a 1983, onde a FPF não ajuda; ficam para conferir com o Futebol Nacional.
   - **Fontes por edição:** a coluna `fontes` de `edicoes.csv` agora inclui "FPF" de 2007 em diante.
2. **A2:** o Primavera, vice de 2025, passa a ter "acesso", porque jogou a 1ª divisão em 2026. É a mesma regra dos outros anos, e é a única linha que muda.
3. **Números:**
   - `bra-sp-1`: 135 edições e 21.847 jogos. Tabelas publicadas: 218 fecham e 124 divergem, sem mudança.
   - testar_carga: `bra-sp-1: 135 edições, 21847 jogos, 0 clubes novos -> OK`; `bra-sp-2: 80 edições, 9223 jogos -> OK`.
4. **Pedido ao agente 1:** recarregar o `bra-sp-1`, que ganha a edição de 2026, e o `bra-sp-2`. Se o seletor do site limita os anos, incluir 2026.
5. **Próximo, parte 3** (`pacote.py`): rebaixados (SP-015), artilheiros pela `sptops.htm` e pela FPF (QS-010, SP-023, SP-024, QS-011) e observações em português (SP-022).

## Correções da revisão — bra-sp-1 — 24/11/2026 (parte 3: pacote.py)

1. **Corrigidos** (em `coleta/bra-sp-1/pacote.py`, com o motivo e a fonte ao lado de cada linha):
   - **QS-010, SP-023, SP-024 e QS-011 (D-17 a):** artilheiros.
     - A `sptops.htm` agora é lida por colunas. A coluna da liga diz a temporada nos anos de duas ligas, e nos empates os gols vêm na última linha do grupo.
     - De 2022 em diante vale a artilharia oficial da FPF (`data/coleta/bra-sp-1/fpf/artilharia_<ano>.json`).
     - 2021: Bruno Mezenga com 9 gols, porque a FPF e o Futebol Nacional batem contra a RSSSF, que dá 10.
     - 2019: ficam os 4 empatados com 7, porque a RSSSF e o FN batem; a FPF só dá o Jean Mota.
     - Agora são 132 edições com artilheiro (eram 13). Ficam sem: 1927 APEA, 1928 LAF e 1936 LPF, que a lista da RSSSF não traz.
   - **SP-015:** rebaixados, pela soma de três coisas:
     - as marcas da RSSSF, menos quem jogou a 1ª divisão no ano seguinte (saem 1994 Mogi Mirim; 1998 Inter de Limeira, Portuguesa Santista e Araçatuba; 1999 Araçatuba e União São João; 2002 Portuguesa Santista);
     - quem jogou a A2 no ano seguinte, pelo pacote `bra-sp-2`;
     - os casos à mão: 1959 Comercial Paulistano, 2026 Ponte Preta e Velo Clube (Wikipédia pt), e o Red Bull Brasil de 2019, que não caiu (fusão com o Bragantino).

     Quem só jogou a repescagem ou o torneio do rebaixamento contra a A2 é da A2 e não cai.
     - Entram 2014 a 2025, como no achado, e os anos antigos sem marca: 1952-1954, 1959-1961, 1963-1965, 1975, 1978, 1984, 1993 (14 clubes para a A2 de 1994), 1995 (XV de Piracicaba), 1996 e 2006 (Portuguesa Santista).
     - Conferido com a Wikipédia pt nos anos em que ela traz os rebaixados. As páginas usadas ficam em `data/coleta/bra-sp-1/wikipedia/pt_<ano>.txt`.
   - **SP-022:** observações em português (`observacao()`; o tradutor comum quebrava as notas no ";" de dentro dos parênteses).
     - Saem o "*" de 1940 e as notas de pênaltis, que estão nos campos próprios.
     - As dúvidas da página viram "placar em dúvida na página (2-0?)" e "data em dúvida na página (19/Mar?)".
     - As notas de 1984 e 1986, que vinham coladas com linhas de outros jogos, foram reescritas.
     - Em 2018, o público de 101 jogos e o estádio de 14 saem da nota para os campos `publico`, `estadio` e `cidade`.
   - **Jogo falso de 1933** (do SP-022, "jogo sem data"): a página quebra "AA São" / "Bento" em duas linhas, e o leitor via Corinthians 2-0 São Paulo. Com a linha junta (`rsssf_sp1.py`), 1933 fica com 56 jogos, e a tabela da RSSSF fecha.
2. **Números:**
   - 135 edições e 21.846 jogos.
   - Tabelas: 219 fecham e 123 divergem (eram 218 e 124).
   - A A2 não muda.
   - testar_carga: `bra-sp-1: 135 edições, 21846 jogos, 0 clubes novos -> OK`.
3. **Pedido ao agente 1:** recarregar o `bra-sp-1` (rebaixados, artilheiros, observações e público de 2018).
4. **Próximo, parte 4 (pódio):**
   - os 3º lugares que sobram, quase todos empates em pontos: 1908, 1917, 1927 LAF, 1928 LAF, 1930, 1954, 1959, 1971, 1978, 1990 e 2008 (SP-003, SP-017);
   - a identidade da AA São Bento de 1933 e do CA Paulista de 1935 (SP-026, SP-027, D-23).

   Depois: A2, C, D e Copa.

## Correções da revisão — bra-sp-1 — 24/11/2026 (parte 4: pódio)

1. **Corrigidos** (em `coleta/bra-sp-1/importar.py` e `rsssf_sp1.py`):
   - **SP-026 e SP-027 (D-23 d e e):** juntados por `CORRIGE_OGOL`:
     - "São Bento de São Paulo" (1933, ogol 233382) vai para a AA São Bento;
     - "ECPaulista" (1935 LPF, ogol 81019) vai para o CA Paulista.

     As duas sobras saíram do cadastro comum.
   - **SP-017:**
     - 1971: desempate por saldo antes das vitórias (`CRITERIO_SALDO`); 3º Corinthians.
     - 2008: semifinalistas pela campanha toda (D-02 A; `SEM_TABELA_GERAL`); 3º São Paulo (41) e 4º Guaratinguetá (40).
   - **SP-003, os 3º lugares:**
     - 1990: a última fase de liga (3ª fase) decide (`FASE_DECISIVA`, D-02 A); 3º Corinthians.
     - 1978: a página escreve "03/Jun/1979", com o ano, e o leitor não entendia esse formato. Os jogos de 1979 vinham só do ogol, que pôs em maio o 3º turno de junho e não separava as fases. Agora:
       - a página é lida inteira, e quando só o mês difere entre RSSSF e ogol fica a da RSSSF (só em 1978, `SO_MES_DA_RSSSF`, conferido com o FN);
       - o 3º turno, as semifinais e a final ficam separados, e as decisões do 2º turno viram "2º Turno - ...";
       - entra o playoff Velo Clube x Paulista (3 jogos, "Torneio de rebaixamento");
       - 3º Guarani, eliminado na semifinal com a melhor campanha (D-02).
     - 1908: os W.O. marcados "dns" na página não contavam. Agora contam, de 1905 a 1910, e também o "awarded 0-0" de 1905, que era um empate e passa a ser vitória do Paulistano. 1908: 3º Americano, como na tabela da RSSSF.
     - 1909: vice Paulistano (`VICE_OFICIAL`). O SC Internacional foi eliminado e não está na tabela da RSSSF; com os W.O. contando, ele subia para 2º.
   - **Ficam como estão, com os motivos anotados:**
     - 1917 e 1954: o FN confirma o pacote (Corinthians e Santos em 3º); a Wikipédia diverge.
     - 1927 LAF, 1928 LAF e 1930: a RSSSF dá o 3º lugar dividido entre os dois clubes. O pacote desempata pelas vitórias e pelo saldo, e a Wikipédia escolhe o outro clube.
     - 1959: empate em pontos (Ferroviária e São Paulo, 53), sem regra da época conhecida.
     - 2010: Barueri e Grêmio Prudente são o mesmo clube.
2. **Números:**
   - 135 edições e 21.849 jogos (1978 com 447).
   - Tabelas: 222 fecham e 120 divergem (eram 219 e 123).
   - Clubes com dois jogos no mesmo dia: 44 (eram 56).
   - A A2 não muda.
   - testar_carga: `bra-sp-1: 135 edições, 21849 jogos, 0 clubes novos -> OK`.
3. **Pedidos ao agente 1:**
   - recarregar o `bra-sp-1`;
   - no banco, juntar "São Bento de São Paulo" na AA São Bento e "ECPaulista" no CA Paulista, mantendo os nomes AA São Bento e CA Paulista (D-23 d e e).
4. **Plano do Paulista (`bra-sp-1`) concluído.** Próximo: A2 (`bra-sp-2`), depois Série C, D e Copa.

## Correções da revisão — bra-sp-2 — 24/11/2026 (A2, partes A e B)

O resto do plano da A2, menos o A2-015, que mexe no leitor comum e vai na parte C.

1. **Parte A, jogos** (`coleta/bra-sp-2/importar.py` e `rsssf_sp2.py`):
   - **A2-012 (D-04):** os playoffs contra a 1ª divisão saem da A2 e ficam só na observação da edição: 1979 (repescagem Marília x Santo André), 2002 (Francana x Portuguesa Santista) e 2003 (Atlético Sorocaba x Botafogo-SP). Marília, Portuguesa Santista e Botafogo-SP deixam de contar como participantes. Os jogos continuam no Paulista.
   - **A2-013:** 2006, Bandeirante x União São João passa a ser um jogo só, 0-1, com a observação de que foi interrompido e completado em 03/04.
   - **A2-014:** 2008, sai o Mogi Mirim 0-0 Oeste anulado pelo TJD-SP; fica o 2-3 de 24/05.
   - **A2-016:** 2021, a rodada 7 vai para 24/04, pela FPF.
   - **A2-019:** 2023, pênaltis 3-2 na final. O leitor agora entende "Penals:".
   - **A2-020:** prorrogações das finais, em `jogos_pt.csv`, pela RSSSF.
     - 1961: 3º jogo Ponte Preta 3-4 Prudentina (3-2 no tempo normal e 0-2 na prorrogação).
     - 1962: o 2-1 do São Bento já inclui a prorrogação (1-0); fica anotado.
   - **A2-026 e A2-028:** observações em 1998 (XV de Piracicaba mantido pelo licenciamento do Novorizontino) e em 2011 (final sem pênaltis na RSSSF; a Wikipédia dá 4-2).
   - **A2-027:** as datas impossíveis de 1985, 1986 e 1988 ficam anotadas no relatório.
2. **Parte B, pódio e clubes:**
   - **A2-024 (D-02 A):** sem "Fase final", vale a última fase de grupos antes da final: os clubes se ordenam pela posição no grupo e pelos pontos dela, e os 2º de cada grupo são o 3º e o 4º. Mudam o 3º e o 4º de 1987, 1988, 1999, 2005, 2006, 2007, 2009, 2010 e 2012, e nenhum campeão ou vice.
     - De 1985 em diante, as diferenças com a predefinição de campeões da Wikipédia caem de 12 para 4: 1989 e 1993 são edições incompletas, e em 1988 a Wikipédia não segue a posição no grupo.
   - **A2-021:** artilheiros de 1998 (Gilson Batata, 18), 2003 (Ricardo Xavier e Clóvis, 12) e 2026 (Lucas Luciano, 9), pela Wikipédia pt (`baixar_wiki.py`; o `infobox()` lê os `pt_<ano>.wiki`). Entram também 1977 e 1978.
   - **A2-022 (D-23 a):** o Grêmio Catanduvense (fundado em 1999) vira cadastro próprio, "Grêmio Catanduvense" (`rs-gremio-catanduvense`).
     - O ogol usa o mesmo código (15767) para ele e para o GE Catanduvense; `REFUNDADO`, em `importar.py` do Paulista e da A2, troca o código de 1999 em diante.
     - O nome "Catanduvense" fica com o clube antigo, como no banco (Série B de 1989).
     - Afeta a A2 de 2008 a 2015 e o Paulista de 2009 a 2012.
   - **A2-023 (D-23 b):** Barueri e Grêmio Prudente ficam separados, sem mudança.
   - **A2-025:** cidades "São Caetano do Sul" (EC São Caetano, 80977) e "São Bernardo do Campo" (EC São Bernardo, 34451), nas fichas e no cadastro comum. O Oeste fica com a cidade de hoje (Osasco), com Itápolis anotada (D-03).
3. **Números:**
   - `bra-sp-2`: 80 edições e 9.214 jogos (eram 9.223: saem 7 jogos de playoff, 1 de 2006 e 1 de 2008). Tabelas: 103 fecham (eram 99).
   - `bra-sp-1`: 21.849 jogos, sem mudança de jogos.
   - testar_carga: `bra-sp-1 ... 1 clubes novos -> OK` e `bra-sp-2: 80 edições, 9214 jogos, 1 clubes novos -> OK`. O clube novo é o Grêmio Catanduvense.
4. **Pedidos ao agente 1:**
   - recarregar o `bra-sp-1` e o `bra-sp-2`;
   - no banco, o Grêmio Catanduvense é clube novo e o "Catanduvense" fica só com os anos até 1995;
   - a cidade do São Caetano EC passa a São Caetano do Sul, e a do EC São Bernardo a São Bernardo do Campo.
5. **Próximo, parte C:** A2-015, as datas herdadas de outra rodada (1987, 1998, 1999, 2010, 2011, 2025). Mexe em `coleta/comum/rsssf.py`; vou reimportar as 5 coletas do Brasil e conferir que só mudam as datas certas.

## Correções da revisão — bra-sp-2 — 24/11/2026 (A2, parte C: A2-015)

1. **A2-015, datas herdadas de outra rodada.** Corrigido com correções nas páginas da A2 (`coleta/bra-sp-2/rsssf_sp2.py`), sem mexer no leitor comum, então C, D, Copa e Paulista não mudam:
   - **1998:** a nota "[*] Apr 1" do jogo do Mirassol tirava a data da rodada 14. Agora a rodada 14 fica em 25/03 (8 jogos), e o jogo do Mirassol leva a observação "jogado em 01/04".
   - **1999:** "Rounf 2" na página; a rodada 2 do torneio do rebaixamento vai para 23/06.
   - **2010 e 2011:** datas com o colchete mal fechado ("[Feb 20)" e "[Feb 26}"); 3 jogos vão para 20/02/2010 e 26/02/2011.
   - **2025:** a página dá à rodada 8 as datas da rodada 7; pela FPF (API, `IdCampeonato=74`), ela foi em 08 e 09/02.
   - **1987:** os blocos do 2º turno vêm sem data e repetiam a última data lida; agora ficam sem data (o marcador "[unknown]" do leitor comum zera a data). Mudam 13 jogos.
2. **Ficam anotadas, como no A2-027:** as datas repetidas que são erro da própria página.
   - 1985, 1986 e 1988;
   - 1987: no grupo F aparecem clubes do grupo C em 10 e 17/05, e no grupo A o União Mogi e o Bragantino têm dois jogos em 20/05.
3. **Números:**
   - 80 edições e 9.214 jogos; as tabelas não mudam (103 fecham).
   - Clubes com dois jogos no mesmo dia: sobram só os erros da página.
   - testar_carga: `bra-sp-2: 80 edições, 9214 jogos, 1 clubes novos -> OK` (o Grêmio Catanduvense, ainda não carregado).
4. **Pedido ao agente 1:** recarregar o `bra-sp-2`.
5. **Plano da A2 concluído.** Próximo: Série C, D e Copa.

## Correções da revisão — bra-serie-c — 24/11/2026 (plano da Série C)

1. **Corrigidos:**
   - **QC-002:** 95 datas pelo Bola n@ Área e pelo transfermarkt (2010, 2013, 2015 e 2019) e pelo transfermarkt e o Futebol Nacional (2026). O ogol grava o jogo noturno com o dia seguinte.
     - A lista fica em `data/coleta/bra-serie-c/datas_corrigidas.csv`, com a fonte em cada linha.
     - O aplicador é comum (`coleta/comum/datas_corrigidas.py`). Ele para com erro se uma linha não achar o jogo ou se o placar não bater.
     - Já gerei os arquivos da Série D (QC-003) e da Copa (QC-004), mas eles só entram nos blocos delas.
   - **QC-011:** 2007, ABC 4-0 Vera Cruz-PE (`PLACAR_MANUAL`). A tabela do grupo 6 na RSSSF diverge agora, porque foi calculada com o 3-0 da própria página.
   - **SC-018 (D-02 A):** a posição no grupo só vale na última fase de liga (a que leva à final). Quem caiu antes se ordena pela fase alcançada e pelos pontos da campanha toda, como a "Classificação geral" da Wikipédia.
     - Mudam posições do meio e do fim em 17 edições (por exemplo, 2008: Duque de Caxias 4º e Águia 5º; 2009: Rio Branco-AC 7º e Paysandu 8º).
     - Nenhum pódio muda.
     - 2010 continua pela classificação geral publicada pela RSSSF.
   - **QC-009 (D-03):** o vice de 1981 passa a ser "Santo Amaro-PE", o nome com que ele jogou (RSSSF, ogol e Bola), e não o posterior "Manchete". Mudou no `MANUAL_NOVO` e no cadastro comum; só a Série C usa esse clube.
   - **CL-028 (parte da C):**
     - Cidades com "de/do/da" minúsculos (`registro.cidade_pt`, regra comum, também no cadastro): EC Limoeiro e Limoeiro passam a "Limoeiro do Norte".
     - Guarani-MG passa a "Divinópolis".
     - A parte da D (Botafogo-DF, AA Araguaia e outras grafias) e a da Copa (Alegrense) vão nos blocos delas.
2. **Só anotado no relatório (`explicacoes.py`):**
   - **SC-016 (D-13):** os 3 placares de 1992 e 1994 em que o Bola e a Wikipédia divergem da RSSSF e do ogol ficam como estão até um jornal da época. Os outros 9 do achado não são erro.
   - **SC-021:**
     - 1999: 226 jogos, contando os 2 jogos-desempate.
     - 2001: 1.124 gols, a soma dos jogos; o 1.127 do resumo do Bola não fecha.
     - 2002: 6 gols a mais que o Bola, dos placares em dúvida.
   - **QC-012:** dos 17 placares em que o ogol e o Bola divergem da RSSSF, só o de 2007 (QC-011) tem 4ª fonte. Os outros 16 ficam com a RSSSF.
3. **Números:**
   - 36 edições e 8.123 jogos (sem mudança).
   - testar_carga: `bra-serie-c: 36 edições, 8123 jogos, 1 clubes novos -> OK`. O "novo" é o Santo Amaro-PE, que no banco é o clube 686, "Manchete".
4. **Pedidos ao agente 1:**
   - recarregar o `bra-serie-c`;
   - no banco, renomear o clube 686 ("Manchete") para "Santo Amaro-PE" em vez de criar outro (D-03; o `clube_nome` dele já tem "Santo Amaro-PE" em 1981).
5. **Próximo:** Série D (QC-001, SD-011, QC-003 e a parte da D do CL-028), depois Copa do Brasil.

## Correções da revisão — bra-serie-d — 24/11/2026 (plano da Série D)

1. **Corrigidos** (`coleta/bra-serie-d/importar.py`):
   - **QC-001:** as 17 disputas de pênaltis que faltavam (2011 a 2021), pelo Bola n@ Área e pelo transfermarkt. `CORRECAO_JOGO` agora aceita as chaves `pm` e `pv`.
   - **SD-011:** 2013, a volta da semifinal Botafogo-PB 2-0 Salgueiro vai para 06/10, pela súmula da CBF (jogo 186), pelo Bola e pelo transfermarkt.
   - **QC-003:** 37 datas de `data/coleta/bra-serie-d/datas_corrigidas.csv`, pelo mesmo aplicador da Série C:
     - 2010: 13 jogos, pelo Bola e pelo transfermarkt;
     - 2021: 1 jogo;
     - 2026: 23 jogos noturnos, pelo transfermarkt e pelo Futebol Nacional.

     O gerador agora lê também a linha de 2026 sem hora (Galvez EC x Gazin Porto Velho).
   - **SC-018 (D-02 A):** a mesma regra da Série C entrou na D. Nada muda, porque a D já segue a classificação geral publicada pela RSSSF, que bate com a Wikipédia (2012: Comercial-PI 29º).
   - **CL-028 (parte da D):**
     - Botafogo-DF passa a Guará (DF), onde jogava em 2007-2010.
     - AA Araguaia passa a Água Boa (MT).
     - Grafias: Rolim de Moura, Teixeira de Freitas, Cruz do Espírito Santo, Vitória de Santo Antão e Divinópolis.
     - A correção de ficha é comum a todas as coletas (`registro.FICHA_COMUM` / `corrigir_ficha`, também no cadastro). Por isso a Série C foi rodada de novo, e só o `clubes.csv` dela muda (Botafogo-DF).
   - **D-03:** o "Rive A.C." passa a "Espírito Santo FC", o nome com que jogou a D em 2016-2018 (ogol e RSSSF).
2. **Números:**
   - 18 edições e 6.032 jogos (sem mudança); mudam 55 jogos (datas e pênaltis).
   - testar_carga: `bra-serie-d: 18 edições, 6032 jogos, 1 clubes novos -> OK`. O "novo" é o Espírito Santo FC, que no banco é o clube 768, "Rive A.C.".
3. **Pedidos ao agente 1:**
   - recarregar o `bra-serie-d` e o `bra-serie-c` (este só pelo Botafogo-DF);
   - no banco, renomear o clube 768 ("Rive A.C.") para "Espírito Santo FC" (D-03; o `clube_nome` dele já tem esse nome em 2016-2018);
   - pôr o Botafogo-DF (442) em DF/Guará e a AA Araguaia (731) em Água Boa.
4. **Próximo:** Copa do Brasil.

## Correções da revisão — bra-copa-do-brasil — 24/11/2026 (plano da Copa do Brasil)

1. **Corrigidos** (`coleta/bra-copa-do-brasil/importar.py`):
   - **QC-005:** dois placares que vieram só do ogol voltam ao da RSSSF, do Bola n@ Área e das Wikipédias pt e en (`CORRECAO_JOGO` agora aceita `gm`/`gv`):
     - 1995: Nacional-AM 1-0 Cristal;
     - 1998: Bahia 1-2 Botafogo-PB. O Bahia passa pelo gol fora (4-4).
   - **QC-004:** 20 datas de `data/coleta/bra-copa-do-brasil/datas_corrigidas.csv` (2008, 2014, 2015, 2018 e 2024), pelo Bola e pelo transfermarkt, com o aplicador comum.
   - **CB-007 e QC-008 (D-14 C):** entra a preliminar de 1999, Náutico 0-1 Santa Cruz em 28/01/1999, pelo Futebol Nacional (`JOGOS_EXTRA`). 1999 fica com 117 jogos e 65 clubes. O texto da pendência em `documentar.py` foi corrigido.
   - **CL-028 (parte da Copa):** Alegrense passa a Alegre (ES), e Botafogo-DF a Guará (DF), pela correção de ficha comum.
2. **Só anotado no relatório:** **CB-005 (D-13).** 1990 (volta Santa Cruz x América-RN) e 1991 (Vitória x Remo) ficam como estão até um jornal da época; 2002 fica.
3. **Também:** as pendências do Paulista e da A2 em `coleta/comum/documentar.py` foram atualizadas, porque os dois planos estão concluídos.
4. **Números:**
   - 37 edições e 4.010 jogos (eram 4.009).
   - Mudam posições do meio da tabela em 1995 e 1998, pelos placares.
   - testar_carga: `bra-copa-do-brasil: 37 edições, 4010 jogos, 0 clubes novos -> OK`.
5. **Pedido ao agente 1:** recarregar o `bra-copa-do-brasil`.
6. **Próximo:** "Todas as coletas Brasil" (QC-006 e QC-007) e a D-10 (SC-029: Séries C de 1987 e 2000 como edições não oficiais).

## Correções da revisão — todas as coletas Brasil — 24/11/2026 (QC-006 e QC-007)

1. **QC-006:** os 100 jogos em que o ogol e o Bola n@ Área concordam numa data diferente da da página da RSSSF passam à data deles.
   - A lista entra no gerador comum (`coleta/comum/datas_corrigidas.py`), que agora lê também `revisao/QC/saida_datas_ogol_bola.txt`. Quando o mesmo jogo está em duas listas e a data bate, as fontes se juntam; se a data divergisse, o gerador pararia.
   - Mudam 45 jogos na Série C, 9 na D e 29 na Copa. Os outros 17 já tinham sido corrigidos pelo QC-002, QC-003 e QC-004, com a mesma data.
   - Nenhuma classificação muda.
2. **QC-007:**
   - **Observações em inglês:** a lista `TRADUCOES` em `coleta/comum/observacao.py` traduz as notas que sobravam, na C (1988 a 2006), na Copa (1998) e na A2 (1986 a 2003), que usa o mesmo tradutor.
     - Exemplos: "W.O. (resultado 0-1)", "resultado 1-0 dado no tribunal (o jogo terminou 0-3; o Serra escalou jogador irregular, Édson Garcia)", "encerrado aos 61 min (Goytacaz com menos de 7 jogadores), com o Americano vencendo por 1-0".
     - Não sobra nenhuma observação em inglês nas quatro coletas.
   - **Notas de rodapé no texto dos gols:** `limpar_gols_texto` corta o que a página cola depois dos autores ("[c] 2nd match played in Porto Alegre", "(*) ALL Baré players...", "- The 6 bye clubs..."). Entra na leitura da C, da D e da Copa.
     - Eram notas em 40 jogos da Copa.
     - Com o texto limpo, a Copa ganha 46 gols com autor (5.718 para 5.764).
3. **Números (sem mudança de jogos):**
   - C: 8.123; D: 6.032; Copa: 4.010; A2: 9.214.
   - testar_carga OK nas quatro, com 0 clubes novos (o banco já tem o Santo Amaro-PE e o Espírito Santo FC).
4. **Pedido ao agente 1:** recarregar o `bra-serie-c`, o `bra-serie-d`, o `bra-copa-do-brasil` e o `bra-sp-2`.
5. **Próximo:** a D-10 (SC-029), as Séries C de 1987 e 2000 como edições não oficiais. É o último bloco do plano do Brasil.

## Recado de fim de coleta — bra-serie-c (edições não oficiais 1987 e 2000) — 24/11/2026

1. **O que entrou** (decisão D-10, achado SC-029): três edições não oficiais da Série C, com aviso e sem contar título.
   - **"1987 Azul" e "1987 Branco":** os Módulos Azul e Branco da Copa União.
     - São dois torneios paralelos, cada um com seu campeão: Americano-RJ (Azul) e Operário-MS (Branco).
     - Têm 24 clubes e 92 jogos cada.
     - O Guilherme decidiu em 24/11 que eles entram na Série C, como no Bola n@ Área. A D-10 citava "Série B 1987 (Módulos Azul e Branco)", mas o próprio Bola chama de "Série C 1987", e o Módulo Amarelo já é Série A (SA-031).
   - **"2000":** os Módulos Verde e Branco da Copa João Havelange, com a fase final. Têm 53 clubes e 398 jogos, e o campeão é o Malutrom, hoje J. Malucelli.
2. **Fontes:** Bola n@ Área, com 7 páginas em `data/coleta/bra-serie-c/bola/`, baixadas por `coleta/bra-serie-c/baixar_bola.py` e lidas por `bola_c.py`.
   - O ogol tem as edições, mas sem jogos.
   - A RSSSF não tem as edições.
   - Os números batem com o resumo do Bola: 1987 com 48 clubes e 184 jogos; 2000 com 53 clubes e 398 jogos.
3. **Identidade:** os clubes saem da lista de participantes do Bola (nome, cidade e UF), ligados ao cadastro comum. Todos já existiam (0 clubes novos). Casos à mão (`importar.MANUAL_BOLA`):
   - Etti Jundiaí = Paulista;
   - Internacional (SP) = Inter de Limeira;
   - Internacional (RS) = Inter de Santa Maria ("Internacional-SM" nos jogos);
   - Malutrom = J. Malucelli;
   - União (MT) = União-MT;
   - Serrano (BA) = Serrano-BA: o Bola escreve Juazeiro, mas é o de Vitória da Conquista, hoje em Teixeira de Freitas.
4. **Conferência:** as 30 tabelas de grupo do Bola fecham com os jogos. O placar inclui a prorrogação, como no esquema do banco. A "colocação final" da página principal de 1987 não fecha com os jogos do próprio Bola, e isso está anotado no relatório.
5. **Formato novo para o agente 1:** coluna `oficial` no fim de `data/coleta/bra-serie-c/pacote/edicoes.csv`. Ela fica vazia nas edições oficiais e com "não" nas três novas, que têm também o aviso na `observacao` e o `nome_oficial` do módulo.
   - Pelo TL-005, o painel precisa ler essa marca, mostrar o aviso e tirar o título do Pódio, da Corrida e das contagens, mantendo jogos e participações.
   - Se preferir outro formato, é só dizer.
6. **Números:** 39 edições (36 oficiais e 3 não oficiais) e 8.705 jogos (eram 8.123). testar_carga: `bra-serie-c: 39 edições, 8705 jogos, 0 clubes novos -> OK`.
7. **Pedidos ao agente 1:**
   - recarregar o `bra-serie-c`, lendo a coluna `oficial`;
   - na Série B, não importar os Módulos Azul e Branco de 1987, que agora são Série C (SB-026 fica só com 1979, 1986 e o Módulo Amarelo de 2000).
8. **Com isso o plano da revisão do Brasil (`docs/revisao/plano-coleta-brasil.md`) está concluído.**

## Recado de fim de coleta — bra-mg-1 — 25/11/2026

Para o agente 1 (banco e painel) e o agente de revisão. Ficha completa: `coleta/comum/documentacao/bra-mg-1.md`;
relatório ano a ano: `docs/coleta/bra-mg-1.md`.

1. **O que foi feito:** Campeonato Mineiro (1ª divisão).
   - 113 edições, de 1915 a 2026. Em 1932 as duas ligas têm uma edição cada ("1932 LMDT" e "1932 AMEG"; a FMF reconhece os dois títulos).
   - 11.521 jogos, 96 clubes (32 já no banco, 64 novos), 24.324 gols com autor (de 31.081) e nenhum cartão.
   - Tabelas publicadas: 285 fecham com os jogos e 196 divergem.
   - Fontes:
     - RSSSF Brasil (`tablesfq/mg{ano}.htm`, 113 páginas; campeões em `mgcamp.htm`, artilheiros em `mgtops.htm`);
     - ogol, calendário de cada edição (1925 não tem), que dá a identidade dos clubes e completa os jogos;
     - Wikipédia em português: tabela de resultados ano a ano (campeão e vice), como segunda fonte.
   - O campeão bate com a RSSSF e com a Wikipédia nas 113 edições. O vice bate com pelo menos uma das duas em todas, menos 1934 (item 6).
2. **Commit:** o deste recado (Mineiro, documentação e as mudanças em `coleta/comum/`).
3. **Teste de carga:** `bra-mg-1: 113 edições, 11521 jogos, 64 clubes novos -> OK`. O carregador avisa que ignora a tabela por rodada em 12 temporadas com mais de uma fase (1974, 1975, 1977, 1979, 1981, 1987, 1988, 1990 ...).
4. **Pedidos ao banco e ao painel:**
   - **Carregar `bra-mg-1`.** `competicao.json`: `tipo` estadual, `nivel` 1, `regiao` MG, `rotulo_painel` "Mineiro".
   - **1932:** a `temporada` leva a liga ("1932 LMDT", "1932 AMEG"), como no Paulista e no Carioca.
   - **Título dividido de 1956:** Atlético-MG em `campeao`, Cruzeiro em `co_campeao`, `vice` vazio (D-07). **1925:** sem vice (não houve).
   - **W.O. sem placar:** `resultado_especial` "awd", sem gols, com o vencedor na `observacao` ("W.O.: vitória do X"), como no Carioca. Em 1917 e 1922, "placar desconhecido: vitória do X": a página só diz quem venceu ("bt") e a tabela conta como vitória sem gols.
   - **Fases novas:** "Fase classificatória" (torneios de classificação de 1921, 1958-1959 e 1970-1973), "Fase classificatória - Desempate", "Primeira fase - Desempate", "Segunda fase - Desempate", "Terceira fase", "Primeira fase - Final" (1983) e "Disputa do 3º lugar" (2022).
   - **Nacional-MG** (ogol 44231, já no banco pela Série D): é de **Nova Serrana**, não de Muriaé (RSSSF 2012; a ficha do ogol trazia a cidade do Nacional Atlético Clube). Corrigido em `registro.FICHA_COMUM`; a Série D foi rodada de novo e só a cidade dele mudou no `clubes.csv`. Recarregar a Série D ou só corrigir a cidade no banco.
   - **Nomes:** nenhum nome que já existia no cadastro comum mudou e nenhum se repete. Os 32 clubes já no banco (Atlético-MG, Cruzeiro, América-MG, Villa Nova-MG, Tupi, Caldense, Ipatinga ...) usam o nome do banco.
5. **Decisões:**
   - **Que eu tomei:**
     - jogos anulados ou cancelados na página ("[annulled]", "[cancelled]", 1918-1942 e 1977) ficam fora; 1923: todo o 2º turno, anulado em assembleia; 1936: os jogos de Palestra Itália, América e Villa Nova, que abandonaram a liga;
     - repescagem contra clube da 2ª divisão (1920, 1923, 1930, 1961, 1967, 1982 e 1983; 16 jogos) fica só na observação da edição (D-04 a); os torneios de rebaixamento só entre clubes da 1ª divisão (1982, 1991, 2023, 2024) ficam;
     - fora: os Torneios Paralelos de 1976 (consolação) e o Troféu Inconfidência de 2020-2026 (5º ao 8º lugar; só o ogol traz os jogos);
     - dentro: a disputa do 3º lugar de 2022 (Athletic x Caldense, só no ogol);
     - W.O.: nas páginas mineiras o "WO" marca quem faltou ("Atlético 1-WO Calafate" é vitória do Atlético); conta como vitória sem gols (D-15);
     - identidade: o ogol usa duas fichas para o Pedro Leopoldo Futebol Clube (1958-1964) e para o Flamengo de Varginha. Fica o que a lista de participantes da RSSSF diz: o Pedro Leopoldo FC em todos os anos; o Flamengo FC (1939) até 1973 e o Flamengo EC (fundado em 1979) de 1980 em diante. O Grêmio Calafate de 1932 é de Belo Horizonte (a ficha do ogol é a de um clube do Acre).
   - **Que esperam o Guilherme:** nenhuma.
6. **O que não deu e pendências:**
   - **1924 e 1925 incompletos na própria fonte** (1924: "Incomplete scores"; 1925: 4 jogos, campeonato anulado pela liga e título homologado pela FMF em 2012).
   - **Vice de 1934:** fica o Tupynambás, que perdeu a final estadual para o Villa Nova (Wikipédia: Tupynambás no estadual e Atlético na cidade); a RSSSF dá o Palestra Itália.
   - **Pontos extras de 1975** (Atlético e Cruzeiro, +1 na fase final): não entram na classificação calculada.
   - **Autores dos gols** fracos nos anos 1990 (16%) e cartões: só jogo a jogo, pela ficha do ogol.
7. **Onde a revisão deve olhar primeiro:**
   - as 196 tabelas divergentes. Muitas não são erro de jogo: a tabela conta o W.O. com gols, traz um turno por tabela quando a página junta os jogos (1983-1987), ou erra a soma (RSSSF e ogol com os mesmos placares);
   - os nomes de fase dados à mão (`rsssf_mg1.FASE_ANO`) e as correções de página (`rsssf_mg1.CORRECOES`, com o motivo de cada uma);
   - os vices de 1934, 1942 e 1950, em que RSSSF e Wikipédia discordam;
   - os casamentos à mão (`NOME_MANUAL`, `CORRIGE_OGOL`) e os clubes antigos sem ficha no ogol (Ipanema, Hellênico).
8. **Próximo campeonato:** Gaúcho (`bra-rs-1`), só com o ok do Guilherme.

## Recado de fim de coleta — bra-rs-1 — 25/11/2026

Para o agente 1 (banco e painel) e o agente de revisão. Ficha completa: `coleta/comum/documentacao/bra-rs-1.md`;
relatório ano a ano: `docs/coleta/bra-rs-1.md`. Primeiro campeonato feito pelo plano único de coleta
(`docs/coleta/plano-de-coleta.md`); o ranking da CBF (RNF 2026) está no `coleta/comum/COMECE-AQUI.md`, seção 3.

1. **O que foi feito:** Campeonato Gaúcho (1ª divisão), escopo aprovado pelo Guilherme em 25/11.
   - 106 edições, de 1919 a 2026. 1918, 1923 e 1924 não foram disputados.
   - 13.393 jogos, 136 clubes (106 novos no banco), 3.843 gols com autor (de 31.393: as páginas quase não trazem) e nenhum cartão.
   - Até 1960 (campeonato por regiões) entram a fase estadual e as decisões de zona e região que a página traz ("Fase regional", com a zona no grupo); os campeonatos das cidades, não.
   - Tabelas publicadas: 230 fecham com os jogos e 159 divergem.
   - Fontes:
     - RSSSF Brasil (`tablesr/rs{ano}.htm`, 1919-2024);
     - ogol ("campeonato-gaucho"), com os calendários guardados em `data/cache/ogol-bra-rs-1/`. Não tem jogos de 1925 a 1976 (salvo 1965). 2025 e 2026 vêm só dele;
     - Wikipédia em português: campeão e vice de cada ano.
   - O campeão bate com a RSSSF e a Wikipédia nas 106 edições. O vice bate com a Wikipédia em todas menos 1986 e 1993 (item 6).
2. **Commit:** o deste recado (`Coleta Gaúcho (bra-rs-1): 106 edições, 13.393 jogos`).
3. **Teste de carga:** `bra-rs-1: 106 edições, 13393 jogos, 106 clubes novos -> OK`. O carregador ignora a tabela por rodada em 1975, 1976, 2011 e 2012, que têm mais de uma fase. O Mineiro, rodado de novo, segue `113 edições, 11521 jogos -> OK`, sem mudança no pacote.
4. **Pedidos ao banco e ao painel:**
   - **Carregar `bra-rs-1`.** `competicao.json`: `tipo` estadual, `nivel` 1, `regiao` RS, `rotulo_painel` "Gaúcho".
   - **Fases novas:**
     - "Fase regional" (até 1960);
     - "1º Turno - Quartas de final" e "2º Turno - Quartas de final" (2009-2013);
     - "Desempate do vice" e "Desempate da vaga", que pelo plano ficam fora da tabela.
     - Os jogos-desempate de séries eliminatórias ficam na fase da série.
   - **Prorrogação:** os gols entram no placar e o dos 90 minutos fica na `observacao` ("90 minutos: 2-2; prorrogação: 2-0"), como no Carioca de 1921.
   - **Nomes:** nenhum nome que já existia mudou e nenhum se repete no cadastro comum. Os clubes só da RSSSF têm código "rs-rs1-...", porque o cadastro já tinha "rs-cruzeiro" (um Cruzeiro de SP) e o Gaúcho herdava o nome. A SE São Borja usa o código da Série C (241325).
5. **Decisões:**
   - **Que eu tomei:**
     - nomes antigos são o mesmo clube: Floriano/NH é o Novo Hamburgo; 9º RI é o Farroupilha; Grêmio Bagé é o Bagé; "Guarany Bagé"/"Guarany B" é o Guarany de Bagé; Santanense é o Grêmio Santanense;
     - nomes sem cidade por época: "Riograndense" é o de Rio Grande até 1960 e o de Santa Maria de 1961 a 1976; "Guarany" é o de Bagé até 1960, menos 1943 (Cachoeira do Sul, vice pela Wikipédia); "Cruzeiro" é o de Porto Alegre, menos 1955, 1956 e 1959 (o de São Gabriel);
     - ficha do ogol mais nova que o jogo: antes de 1989 é a AE Santo Ângelo (a SER Santo Ângelo nasceu de uma fusão em 1989); antes de 2009 é a SE São Borja;
     - a decisão do Título do Interior de 2009 fica fora (torneio à parte);
     - sem final de dois clubes, o vice segue a Wikipédia (a RSSSF não traz o vice do Gaúcho).
   - **Que esperam o Guilherme:**
     - **1918:** o campeonato foi suspenso pela gripe espanhola. Em 2021 a FGF reconheceu Brasil de Pelotas, Cruzeiro e 14 de Julho como "campeões honoríficos" (Wikipédia). Hoje 1918 fica fora. Pode entrar como edição sem jogos, com os três campeões, se ele quiser.
6. **O que não deu e pendências:**
   - **Vices de 1986 e 1993:** o pacote segue a classificação publicada (Passo Fundo e Juventude); a Wikipédia dá o Internacional.
   - **SE São Borja x AE São Borja:** as fontes discordam se é a mesma linhagem.
   - **Flamengo de Alegrete:** tem ficha de 1963 e jogos em 1961-1962.
   - **Autores dos gols:** quase só nas páginas antigas.
   - **1994:** algumas linhas da página trazem dois jogos colados, sem data; os jogos vêm do ogol.
7. **Onde a revisão deve olhar primeiro:**
   - a identidade de 1925-1976 (sem ogol): `importar.NOME_CODIGO` e `NOME_ANO`, e os clubes "rs-rs1-...";
   - as grafias corrigidas das páginas escaneadas (`rsssf_rs1.GRAFIAS`);
   - as 159 tabelas divergentes, a maioria nos anos de página escaneada (1963-1996);
   - as fases dadas à mão nos anos de formato complicado (1972-1977, 1983-1989, 2009-2013).
8. **Próximo campeonato:** Paranaense (`bra-pr-1`), 5º do ranking da CBF; escopo antes, só com o ok do Guilherme.

Também neste commit:
- **Mineiro:** o "Palmeiras" do torneio eliminatório de 1921 passa a ser o Palmeiras de BH (99077). Antes era um segundo código com o mesmo nome; o pacote não muda.
- **`documentar.py`:** agrupa por faixa de anos as tabelas grandes por temporada.

## Recado de fim de coleta — bra-pr-1 — 25/11/2026

Para o agente 1 (banco e painel) e o agente de revisão. Ficha completa: `coleta/comum/documentacao/bra-pr-1.md`;
relatório ano a ano: `docs/coleta/bra-pr-1.md`.

1. **O que foi feito:** Campeonato Paranaense (1ª divisão), escopo aprovado pelo Guilherme em 25/11.
   - 113 edições, de 1915 a 2026. Em 2002 são duas: "2002" (o oficial da FPF, campeão o Iraty) e "2002 Supercampeonato" (com os clubes da Copa Sul-Minas, campeão o Atlético), esta com `oficial` = "não".
   - 1980: título dividido entre Colorado e Cascavel (`co_campeao`; vice = o próximo que não é campeão, D-07).
   - 14.315 jogos, 142 clubes (104 novos no banco), 2.410 gols com autor (de 41.127: as páginas quase não trazem), nenhum cartão e 133 artilheiros.
   - De 1935 a 1941, depois do campeonato de Curitiba, entra a fase estadual com os campeões das ligas do interior (quartas, semifinal e final). A final da cidade fica em "Primeira fase - Final".
   - Tabelas publicadas: 209 fecham com os jogos e 225 divergem.
   - Fontes:
     - RSSSF Brasil (`tablesfq/pr{ano}.htm`, 1915-2026; campeões em `prcamp.htm`, artilheiros em `prtops.htm`);
     - ogol ("campeonato-paranaense"), com os calendários guardados em `data/cache/ogol-bra-pr-1/`. Não tem jogos de 1915 a 2000 (salvo 1965 e 1967);
     - Wikipédia em português: campeão e vice de cada ano.
   - O campeão bate com a Wikipédia nas 113 edições. O vice bate em todas menos 1923-1926, 1940 e 1941 (item 6).
2. **Commit:** o deste recado (`Coleta Paranaense (bra-pr-1): 113 edições, 14.315 jogos`).
3. **Teste de carga:** `bra-pr-1: 113 edições, 14315 jogos, 104 clubes novos -> OK`. O carregador ignora a tabela por rodada em 1975, 1976, 2009-2012 e 2014, que têm mais de uma fase. O Gaúcho, rodado de novo, dá `106 edições, 13393 jogos, 105 clubes novos -> OK` (item "Também neste commit").
4. **Pedidos ao banco e ao painel:**
   - **Carregar `bra-pr-1`.** `competicao.json`: `tipo` estadual, `nivel` 1, `regiao` PR, `rotulo_painel` "Paranaense".
   - **Coluna `oficial`** em `edicoes.csv` ("não" no "2002 Supercampeonato"), como na Série C.
   - **Fases novas:**
     - "4º Turno" (1973) e "Torneio extra" (1995, dos eliminados, fora do alcance);
     - "Desempate", "Desempate do 7º lugar", "Desempate do 2º turno", "Desempate do rebaixamento", "Desempate do ponto extra" e "Desempate da vaga em 1982", que pelo plano ficam fora da tabela;
     - grupos novos: "APSA" e "LSP" (as duas ligas de 1916) e as zonas de 1963 ("Norte Novo", "Norte Velho", "Zona Sul").
   - **Nomes:** nenhum nome que já existia mudou e nenhum se repete no cadastro comum. Clubes que a Série C já tinha entram com o código dela: Colorado-PR (17735), Matsubara (2541), Batel (44013), Cascavel (52741, o Cascavel EC de 1979), Pinheiros-PR (17224) e Maringá FC 1995 (241210). Nomes novos para homônimos do PR: "Cascavel CR" (2001), "Galo Maringá 2020" e "Foz do Iguaçu EC" (1989-1995).
5. **Decisões:**
   - **Que eu tomei:**
     - mesma linhagem, mesmo clube: Savóia, Savóia Água Verde, EC Brasil (1942-1944) e Água Verde são o "Água Verde" (39780); o Palestra Itália leva os nomes da II Guerra (Paranaense 1942, Comercial 1943-1945, Palmeiras 1946-1949); Reco-Reco é o Palmeiras de 1916-1917;
     - o EC Pinheiros (1972-1989) fica no código 17224, à parte do Água Verde, porque o ogol, o cadastro comum e o banco já o separam (é a mesma linhagem: item 6);
     - nomes sem cidade por época: "Paraná" (Paraná SC até 1926, Paraná EC de Londrina em 1968-1969, Paraná Clube de 1990); "Cascavel" (Cascavel FC em 1971-1972, Cascavel EC de 1980 a 2000, Cascavel CR de 2003); "Maringá" (Grêmio Maringá até 1996, Maringá FC 1995 em 1997-1998, Maringá FC de 2010); "Nacional" (o da Polícia Militar de Curitiba em 1934-1935, depois o de Rolândia); "Toledo", "Foz do Iguaçu", "Arapongas" e "Cianorte" (CAFE) antes das fichas do ogol;
     - ficha do ogol mais nova que o jogo: Prudentópolis antes de 2007 é o Prudentópolis EC (1968);
     - fora do pacote: a Final do Interior de 2015 e 2016 (título à parte, como no Gaúcho) e o jogo "Atlético 2-1 Atlético" de 24/08/1924 (a página não diz o adversário);
     - 1940: "Juventus 2-0 Juventus" é Britânia 2-0 Juventus (o único jogo que falta aos dois, e a tabela da página fecha).
   - **Que esperam o Guilherme:** nenhuma nova. Segue em aberto a do Gaúcho de 1918 (campeões honoríficos).
6. **O que não deu e pendências:**
   - **Água Verde e Pinheiros:** a mesma linhagem em dois códigos (39780 e 17224), como já estavam no banco. Juntar é decisão da revisão.
   - **Vices de 1923-1926 e 1940:** a Wikipédia dá o Operário Ferroviário, mas as páginas da RSSSF não têm jogo com ele (devia haver uma final estadual que a página não traz).
   - **Vice de 1941:** a página dá a final Coritiba 6-1 Antoninense; a Wikipédia dá o Jacarezinho (que perdeu a semifinal na página).
   - **Cambaraense (1952-1962) e Cambará (1963-1965):** ficam separados; a página não diz se é o mesmo clube.
   - **Autores dos gols:** 6%; de 2021 a 2026 nenhum.
7. **Onde a revisão deve olhar primeiro:**
   - a identidade de 1915-2000 (sem ogol): `importar.NOME_CODIGO` e `NOME_ANO`, e os clubes "rs-pr1-...";
   - as fases dadas à mão (`rsssf_pr1.FASE_ANO`), sobretudo 1916, 1935-1941, 1963, 1977 e 1995;
   - as 225 tabelas divergentes.
8. **Próximo campeonato:** Cearense (`bra-ce-1`), 6º do ranking da CBF; escopo antes, só com o ok do Guilherme.

Também neste commit:
- **Gaúcho:** a SE São Borja saía no `clubes.csv` com o nome "241325" (o código), porque a ficha vem da Série C e não da lista do ogol do Gaúcho. Agora sai "SE São Borja" (`clubes_rs1.DE_OUTRAS_COLETAS`). Só esse nome muda no pacote (365 jogos).
- **Mineiro:** o relatório `docs/coleta/bra-mg-1.md` deixa de listar o "Palmeiras" sem ogol (a correção de 1921 do commit do Gaúcho); o pacote não muda.
- **`registro.FICHA_COMUM`:** a cidade do Água Verde (39780) é "Curitiba" (o ogol escreve "Curitiba. PR"). Só o Paranaense usa essa ficha.

## Recado de fim de coleta — bra-ce-1 — 25/11/2026

Para o agente 1 (banco e painel) e o agente de revisão. Ficha completa: `coleta/comum/documentacao/bra-ce-1.md`;
relatório ano a ano: `docs/coleta/bra-ce-1.md`.

1. **O que foi feito:** Campeonato Cearense (1ª divisão), escopo aprovado pelo Guilherme em 25/11.
   - 112 edições, de 1915 a 2026 (a conta da FCF). Ficam fora 1913 (campeão desconhecido) e 1914 (a FCF não reconhece). 1915-1919 são os torneios da Liga Metropolitana, reconhecidos pela FCF em 2008.
   - **17 edições sem jogos em nenhuma fonte** (1916-1919, 1924-1927, 1929-1932, 1934-1938) entram só com campeão e vice, por decisão do Guilherme. 1915 tem só a final.
   - 8.501 jogos, 57 clubes (34 novos no banco), 2.821 gols com autor (de 24.598), nenhum cartão e 110 artilheiros.
   - Tabelas publicadas: 185 fecham com os jogos e 95 divergem.
   - Fontes:
     - RSSSF Brasil (`tablesae/ce{ano}.htm`; campeões em `cecamp.htm`, artilheiros em `cetops.htm`). O site parou de responder em 25/11: 87 páginas vieram da cópia do Internet Archive (lista em `data/coleta/bra-ce-1/rsssfbrasil/origem.json`). Sem página: 2025 e 2026;
     - ogol ("campeonato-cearense"), com os calendários em `data/cache/ogol-bra-ce-1/`. Tem jogos de 2001 a 2026 e de 1920, 1949, 1961 e 1994;
     - Wikipédia em português ("Campeonato Cearense de Futebol Masculino"): campeão e vice de cada ano.
   - O campeão bate com a RSSSF e a Wikipédia em todas as edições. O vice bate em todas as que a Wikipédia dá (1915 e 1916-1919: a Wikipédia não tem vice).
2. **Commit:** o deste recado (`Coleta Cearense (bra-ce-1): 112 edições, 8.501 jogos`).
3. **Teste de carga:** `bra-ce-1: 112 edições, 8501 jogos, 34 clubes novos -> CONFERIR`, só por causa do `co_campeao` de 1992 (item 4). O carregador ignora a tabela por rodada em 2000, 2014, 2018, 2019 e 2021, que têm mais de uma fase.
4. **Pedidos ao banco e ao painel:**
   - **Carregar `bra-ce-1`.** `competicao.json`: `tipo` estadual, `nivel` 1, `regiao` CE, `rotulo_painel` "Cearense".
   - **Edição sem jogos:** 17 linhas de `edicoes.csv` sem nenhuma partida, com campeão e vice. O carregador aceita (confere 0 jogos). O painel precisa mostrá-las na lista de campeões sem quebrar a tabela e a Corrida. O Orion (campeão de 1930) está no `clubes.csv` sem jogo nenhum.
   - **`co_campeao` com mais de um clube:** 1992 teve quatro campeões (Fortaleza, Ceará, Tiradentes e Icasa). `co_campeao` = "Ceará / Tiradentes-CE / Icasa". Hoje o carregador aceita um clube só e deixa o campo vazio. Peço que aceite a lista separada por " / ".
   - **Fases novas:** "1º Turno - Fase final", "2º Turno - Fase final", "3º Turno - Fase final", "4º Turno - Fase final" (quadrangular ou triangular de cada turno), "3º Turno - Final", "4º Turno - Final", "Turnos - Segunda fase", "Turnos - Semifinal", "Turnos - Fase final" e "Turnos - Final" (fases de todos os turnos juntos, 1988, 1990, 1996 e 1998). Os desempates fora da tabela ficam em "Desempate".
   - **Nomes:** nenhum nome que já existia mudou e nenhum se repete no cadastro comum. Novos homônimos: "Orion-CE", "Iguatu 1996" (o Iguatu de 1996-1997; a ficha do ogol é de 2010) e "Esporte Limoeiro".
5. **Decisões:**
   - **Que eu tomei:**
     - "Guarany" sem cidade: o de Fortaleza até 1960, o de Sobral depois; "Guarani" é o de Juazeiro do Norte;
     - "Esporte", "Esporte Limoeiro" e "Limoeiro" de 1995 a 2000 são o Esporte Clube Limoeiro (o Limoeiro do ogol é de 2001);
     - Maguari/Maguary, Luso, Tramways, Fluminense, Flamengo e Peñarol/Penarol juntam as grafias;
     - 1939: os dois jogos marcados "jogo anulado" ficam fora; o "este jogo não terminou" fica, com nota;
     - 2004: a linha "n/p" da final que não houve fica fora; a nota da edição explica;
     - fora do pacote: a Taça Padre Cícero de 2012 (título à parte, como a Final do Interior do Paraná).
   - **Que esperam o Guilherme:** nenhuma.
6. **O que não deu e pendências:**
   - **1916-1919, 1924-1927, 1929-1932 e 1934-1938:** sem jogos em nenhuma fonte achada (a RSSSF não tem página de 1924-1938, salvo 1928 e 1933).
   - **"América-R" (1996) e "Russas" (1997):** talvez o mesmo clube; ficam separados.
   - **Páginas de 1996 e 1998:** quase sem datas, ou só com o dia e o mês.
   - **Autores dos gols:** 11%.
7. **Onde a revisão deve olhar primeiro:**
   - as fases dadas à mão (`rsssf_ce1.FASE_ANO` e as regras do Cearense em `importar.FASES_PT`), sobretudo 1988-1999;
   - as páginas que vieram do Internet Archive, quando a RSSSF voltar (comparar com as do site);
   - as 95 tabelas divergentes.
8. **Próximo campeonato:** Goiano (`bra-go-1`), 7º do ranking da CBF; escopo antes, só com o ok do Guilherme. Antes dele, o Gaúcho de 1918 como edição sem jogos (a mesma decisão).

Também neste commit:
- **Paranaense:** a introdução do relatório (`coleta/bra-pr-1/explicacoes.py` e `docs/coleta/bra-pr-1.md`) tinha ficado com o texto do Gaúcho; agora descreve o Paraná. O pacote não muda.

## Gaúcho de 1918 — bra-rs-1 — 25/11/2026

Para o agente 1 e a revisão. Pela decisão do Guilherme sobre as edições sem jogos (a mesma do Cearense), o Gaúcho ganha a
edição de 1918: o campeonato foi suspenso pela gripe espanhola e em 2021 a FGF reconheceu Brasil de Pelotas, Cruzeiro (o
de Porto Alegre, hoje em Cachoeirinha: "Cruzeiro-RS") e 14 de Julho como campeões honoríficos (Wikipédia).

- `edicoes.csv`: 1918 sem jogos, `campeao` Brasil de Pelotas, `co_campeao` "Cruzeiro-RS / 14 de Julho", sem vice, com a nota.
  Nenhuma outra linha do pacote muda (só `edicoes.csv` e `conferencia.csv` ganham a linha de 1918).
- Teste de carga: `bra-rs-1: 107 edições, 13393 jogos, 0 clubes novos -> CONFERIR`, só pelo `co_campeao` com dois clubes
  (o mesmo pedido do Cearense: aceitar a lista separada por " / ").
- **Pedido:** recarregar `bra-rs-1`.
- Commit: o desta seção (`Gaúcho: 1918 como edição sem jogos, com os campeões honoríficos`).

## Recado de fim de coleta — bra-go-1 — 25/11/2026

Para o agente 1 (banco e painel) e o agente de revisão. Ficha completa: `coleta/comum/documentacao/bra-go-1.md`;
relatório ano a ano: `docs/coleta/bra-go-1.md`.

1. **O que foi feito:** Campeonato Goiano (1ª divisão), escopo aprovado pelo Guilherme em 25/11.
   - 83 edições, de 1944 a 2026 (a conta da FGF): 1944-1962 é a era amadora (o campeonato de Goiânia, que a FGF conta como Goiano); profissional desde 1963.
   - **8 edições sem jogos** (1945, 1946, 1950, 1951, 1960, 1963, 1965, 1966) entram só com campeão e vice: 1945 tem só a tabela final; as outras não têm página na RSSSF e o ogol não tem os jogos.
   - 8.682 jogos, 62 clubes (36 novos no banco), 2.965 gols com autor (de 22.388), nenhum cartão e 89 artilheiros.
   - Tabelas publicadas: 180 fecham com os jogos e 99 divergem.
   - Fontes:
     - RSSSF Brasil (`tablesfq/go{ano}.htm`; campeões em `gocamp.htm`, artilheiros em `gotops.htm`). Sem página: os anos acima e 2026;
     - ogol ("campeonato-goiano"), com os calendários em `data/cache/ogol-bra-go-1/`. Tem jogos a partir dos anos 2000; 2026 só nele;
     - Wikipédia em português ("Campeonato Goiano de Futebol Masculino"): campeão e vice de cada ano. A API recusou o download por excesso de pedidos; vale a cópia do artigo baixada no mesmo dia, na pesquisa do escopo.
   - O campeão bate com a RSSSF e a Wikipédia nas 83 edições. O vice bate em todas menos 1958 e 2000 (item 6).
2. **Commit:** o deste recado (`Coleta Goiano (bra-go-1): 83 edições, 8.682 jogos`).
3. **Teste de carga:** `bra-go-1: 83 edições, 8682 jogos, 36 clubes novos -> OK`. O carregador ignora a tabela por rodada em 1992, 1997, 1999, 2001 e 2002, que têm mais de uma fase.
4. **Pedidos ao banco e ao painel:**
   - **Carregar `bra-go-1`.** `competicao.json`: `tipo` estadual, `nivel` 1, `regiao` GO, `rotulo_painel` "Goiano".
   - **Edição sem jogos:** 8 linhas de `edicoes.csv` sem partidas, com campeão e vice (como no Cearense).
   - **Nomes:** nenhum nome que já existia mudou e nenhum se repete no cadastro comum. O Luziânia usa o código que já estava no cadastro (3330). Nomes novos: "Botafogo de Goiânia" (Botafogo/G e Sírio Libanês) e "Grêmio Anapolino".
5. **Decisões:**
   - **Que eu tomei:**
     - o Vila Nova jogou como Araguaia nos anos 1940 (RSSSF, "former Araguaia"); o Botafogo de Goiânia como Sírio Libanês e a Campineira como Mariana (Wikipédia);
     - "Rio Verde" é o EC Rio Verde (1963); o Rioverdense é outro clube;
     - 1978 e 1993: a página dá o mesmo clube aos dois lados; vale o confronto que falta na fase (Anápolis 1-0 Anapolina; Mineiros 2-1 Anapolina);
     - 1997: o jogo-desempate da semifinal (CRAC 5-2 Jataiense) fica na semifinal;
     - fora do pacote: os dois amistosos de 1995 ("friendly match") e a repetição sem data da final de 2021.
   - **Que esperam o Guilherme:** nenhuma.
6. **O que não deu e pendências:**
   - **Vice de 1958:** a tabela da página dá o Vila Nova; a Wikipédia, o Atlético.
   - **Vice de 2000:** o Goiás venceu as duas finais de turno contra o Vila Nova (o pacote dá o Vila Nova); a Wikipédia dá a Anapolina, talvez pela campanha geral.
   - **1993:** outros confrontos trocados na página (CRAC x Goiânia e Itumbiara x Mineiros duas vezes; faltam CRAC x Anapolina e Itumbiara x Quirinópolis); ficam como estão.
   - **Autores dos gols:** 13%.
7. **Onde a revisão deve olhar primeiro:**
   - as 99 tabelas divergentes, sobretudo 1983, 1984 e 1988;
   - a identidade dos clubes só da RSSSF ("rs-go1-...": São Luís, Botafogo/BA, Campinas);
   - os vices de 1958 e 2000.
8. **Próximo campeonato:** Catarinense (`bra-sc-1`), 8º do ranking da CBF; escopo antes, só com o ok do Guilherme.

## Recado de fim de coleta — bra-sc-1 — 27/11/2026

Para o agente 1 (banco e painel) e o agente de revisão. Ficha completa: `coleta/comum/documentacao/bra-sc-1.md`;
relatório ano a ano: `docs/coleta/bra-sc-1.md`.

1. **O que foi feito:** Campeonato Catarinense (1ª divisão), escopo aprovado pelo Guilherme em 27/11.
   - 102 edições, de 1924 a 2026, sem 1946 (não disputado). 1924-1926 e 1934-1936 eram os campeonatos da capital, homologados como estaduais pela FCF (por isso 1924 entra, embora a lista da RSSSF o marque como não oficial).
   - **7 edições sem jogos** (1925, 1926, 1928, 1933, 1934, 1943, 1945): a página só traz participantes, campeão e um ou outro jogo solto; entram com campeão e vice. **1933 não terminou** e fica sem campeão e sem vice.
   - 8.721 jogos, 116 clubes (87 novos no banco), 3.434 gols com autor (de 21.758), nenhum cartão e 95 artilheiros.
   - Tabelas publicadas: 114 fecham com os jogos e 90 divergem.
   - Fontes:
     - RSSSF Brasil (`tablessz/sc{ano}.htm`, 1924-2026; campeões em `sccamp.htm`);
     - ogol ("campeonato-catarinense"), com os calendários em `data/cache/ogol-bra-sc-1/`. Tem jogos de 2001 a 2026;
     - Wikipédia em português: o artigo e a predefinição "Campeões do Campeonato Catarinense de Futebol" (campeão e vice de cada ano).
   - O campeão bate com a RSSSF e a Wikipédia em todas as edições (1965 e 1970 diferem só no nome). O vice: item 6.
2. **Commit:** o deste recado (`Coleta Catarinense (bra-sc-1): 102 edições, 8.721 jogos`).
3. **Teste de carga:** `bra-sc-1: 102 edições, 8721 jogos, 87 clubes novos -> OK`. O carregador ignora a tabela por rodada em 9 temporadas com mais de uma fase.
4. **Pedidos ao banco e ao painel:**
   - **Carregar `bra-sc-1`.** `competicao.json`: `tipo` estadual, `nivel` 1, `regiao` SC, `rotulo_painel` "Catarinense".
   - **Edição sem jogos e sem campeão:** 1933 (não terminou) não tem jogos nem campeão.
   - **Nomes:** nenhum nome que já existia mudou e nenhum se repete no cadastro comum. Usam o código que já estava no cadastro (Série C): Blumenau (3147; o Brasil FC e o Palmeiras EC de antes), Caçadorense (241623) e Joaçaba EC (238972). Novos: "Atlético Catarinense de Florianópolis" (campeão de 1934; o "Atlético Catarinense" do ogol é o de Criciúma, de 2020), "Brasil de Tijucas", "Juventus de Rio do Sul".
   - **Ficha comum (`registro.FICHA_COMUM`):** o Tiradentes EC (3493) ganha UF SC e cidade Tijucas (a ficha do ogol não traz a UF). Só o Catarinense usa essa ficha.
5. **Decisões:**
   - **Que eu tomei:**
     - Comerciário é o Criciúma EC (campeão de 1968); Avahy é o Avaí; Brasil, Palmeiras e Blumenau são o Blumenau EC;
     - páginas antigas só com jogos soltos entram como edição sem jogos (não fazem tabela com um ou dois jogos);
     - fora do pacote: o Torneio Início, os amistosos com clubes de outros estados (1941), as linhas de classificação e de nota lidas como jogo;
     - fases dos anos 1980: os turnos com nome de taça viram "1º/2º/3º Turno" e o quadrangular ou hexagonal decisivo, "Fase final"; os torneios paralelos de quem não se classificou, "Torneio extra";
     - vices dados à mão em 1967 e 1969 (pela Wikipédia; o clube nem aparece nos jogos da página) e 2004 (2º do quadrangular final).
   - **Que esperam o Guilherme:** nenhuma.
6. **O que não deu e pendências:**
   - **Vice de 1960:** a final da página é Metropol x Avaí (o pacote dá o Avaí); a Wikipédia dá o Marcílio Dias.
   - **Vices de 1973 e 1976:** a Wikipédia dá o Atlético Alto Vale, fundado em 1995; fica o da página (Figueirense).
   - **EC Ferroviário de Tubarão** (campeão de 1970): a Wikipédia o chama de "Tubarão"; fica separado do Tubarão FC (1992).
   - **Edições antigas incompletas:** até os anos 1970 a página traz só a fase estadual e as decisões de zona; 1980 só traz da 1ª fase os jogos do Joinville.
   - **Autores dos gols:** 16%.
7. **Onde a revisão deve olhar primeiro:**
   - as fases dadas à mão dos anos 1980 (`rsssf_sc1.FASE_ANO`), sobretudo 1982-1986;
   - os nomes partidos resolvidos por grafia (`rsssf_sc1.GRAFIAS`) e os clubes "rs-sc1-...";
   - as 90 tabelas divergentes.
8. **Próximo campeonato:** Baiano (`bra-ba-1`), 9º do ranking da CBF; escopo antes, só com o ok do Guilherme.

## Recado de fim de coleta — bra-ba-1 — 27/11/2026

Para o agente 1 (banco e painel) e o agente de revisão. Ficha completa: `coleta/comum/documentacao/bra-ba-1.md`;
relatório ano a ano: `docs/coleta/bra-ba-1.md`.

1. **O que foi feito:** Campeonato Baiano (1ª divisão), escopo aprovado pelo Guilherme em 27/11.
   - 122 edições, de 1905 a 2026 (a conta da FBF, da RSSSF e da Wikipédia). 1915 e 1916: só o campeonato oficial; os da liga rival (LSB) ficam fora.
   - **23 edições sem jogos**, só com campeão e vice (a decisão de 25/11): 1938, 1961-1963, 1969, 1971 e 1974 (sem página), e 1922-1935, 1970 e 1982 (a lista da RSSSF Brasil tem o link, mas a página nunca foi criada: 404 no site e no Internet Archive; o ogol não tem os jogos).
   - **Títulos divididos (D-07):** 1938 (Bahia e Botafogo; sem jogos) e 1999 (Bahia e Vitória).
   - 7.359 jogos, 74 clubes (49 novos no banco), 2.897 gols com autor (de 20.027), nenhum cartão e 69 artilheiros.
   - Tabelas publicadas: 241 fecham com os jogos e 121 divergem.
   - Fontes:
     - RSSSF Brasil (`tablesae/ba{ano}.htm`; campeões em `bacamp.htm`). O site parou de responder: 43 páginas vieram do Internet Archive (`rsssfbrasil/origem.json`);
     - ogol ("campeonato-baiano"), com os calendários em `data/cache/ogol-bra-ba-1/`. Tem jogos de 1905-1907 e de 1997 a 2026;
     - Wikipédia em português: o artigo "Campeonato Baiano de Futebol Masculino" (campeão e vice de cada ano).
   - O campeão bate com a RSSSF e a Wikipédia em todas as edições (1912 e 1924 diferem só no nome: o Atlético FC de 1912 é o Santos Dumont com outro nome; "AAB" é a AA da Bahia). O vice: item 6.
2. **Commit:** o deste recado (`Coleta Baiano (bra-ba-1): 122 edições, 7.359 jogos`).
3. **Teste de carga:** `bra-ba-1: 122 edições, 7359 jogos, 49 clubes novos -> OK`. O carregador ignora a tabela por rodada em 5 temporadas com mais de uma fase (1993, 2008, 2010, 2013, 2014).
4. **Pedidos ao banco e ao painel:**
   - **Carregar `bra-ba-1`.** `competicao.json`: `tipo` estadual, `nivel` 1, `regiao` BA, `rotulo_painel` "Baiano".
   - **`co_campeao`:** um clube só em cada edição (1938: Botafogo-BA; 1999: Vitória).
   - **Nomes:** nenhum nome que já existia mudou e nenhum se repete no cadastro comum. Novos com nome dado à mão: "Fluminense de Salvador" (campeão de 1913 e 1915; o "Fluminense-BA" é o de Feira de Santana), "Sport Club Bahia" (campeão de 1911; não é o EC Bahia), "Vitória de Ilhéus" (1967-1968; não é o Vitória), "Conquista 1967" (1967-1977; o Conquista FC do ogol é de 1978), "São Francisco 1996" (1996-1998; o do ogol é de 2001), "River Ilheense" (o ogol escreve "River Ilheeense") e "Internacional de Cricket" (o ogol escreve "De").
   - **Ficha comum (`registro.FICHA_COMUM`):** nada novo.
5. **Decisões:**
   - **Que eu tomei:**
     - mesmo nome, clubes diferentes, separados por ano: "Atlético" (o Atlético FC de Salvador, ex-Santos Dumont, até 1969; o Alagoinhas Atlético Clube depois), "Fluminense" (de Salvador até 1940; o de Feira depois), "Conquista" e "São Francisco";
     - "Guarani" (1944 e 1964-1966, "Associação Desportiva Guarani") é o Guarany das outras páginas;
     - os anos sem página de jogos entram como edição sem jogos (a regra de 25/11);
     - 1946: campeão (Guarany) e vice (Ypiranga) à mão, como a página dá; 1991: vice o Vitória, pela final da RSSSF (o único jogo da página);
     - a classificação geral publicada só vale quando começa pelo campeão e pelo vice da final (2013: a "Final Standings" é a soma dos pontos, com o Juazeirense em 1º);
     - 1975-1996: o turno vai na frente das fases de dentro dele ("2º Turno - Semifinal", "1º Turno - Fase final", "3º Turno - Segunda fase");
     - fora do pacote: o Torneio Início e as preliminares.
   - **Que esperam o Guilherme:** nenhuma.
6. **O que não deu e pendências:**
   - **Vice de 1991:** a RSSSF só tem a final (Bahia 1x1 Vitória; o pacote dá o Vitória); a Wikipédia dá o Fluminense de Feira.
   - **Vice de 1999 (título dividido):** o pacote dá o Conquista, pela tabela (D-07); a Wikipédia dá o Poções.
   - **Identidade a revisar:** o Guarany SC de 1915 e o de 1942-1943 ficam juntos com a AD Guarany (1944-1966); o Internacional de Cricket (1905) fica junto com o SC Internacional (campeão de 1914). Os dois só pelo nome.
   - **Sem jogos da RSSSF:** 2022 (a página não tem placares); os jogos vêm do ogol.
   - **Autores dos gols:** 14%.
7. **Onde a revisão deve olhar primeiro:**
   - as fases dos turnos de 1975-1996 (`rsssf_ba1._turno_nos_titulos` e `importar.fase_turno`), sobretudo 1976-1977 e 1984-1988, onde ficam a maioria das tabelas divergentes;
   - os nomes separados por ano (`importar.NOME_ANO`) e os clubes "rs-ba1-...";
   - as 121 tabelas divergentes.
8. **Próximo campeonato:** Pernambucano (`bra-pe-1`), 10º do ranking da CBF; escopo antes, só com o ok do Guilherme.

## Recado de fim de coleta — bra-pe-1 — 27/11/2026

Para o agente 1 (banco e painel) e o agente de revisão. Ficha completa: `coleta/comum/documentacao/bra-pe-1.md`;
relatório ano a ano: `docs/coleta/bra-pe-1.md`.

1. **O que foi feito:** Campeonato Pernambucano (1ª divisão), escopo aprovado pelo Guilherme em 27/11.
   - 112 edições, de 1915 a 2026 (a conta da FPF, da RSSSF e da Wikipédia; disputado sem interrupção). Nenhum título dividido.
   - A edição 2026/27 (novo calendário: Turno Forró em 2026, Turno Frevo em 2027) fica de fora até terminar.
   - **2 edições sem jogos** (1992 e 1993: a RSSSF nunca teve a página e o ogol não tem os jogos), só com campeão e vice. **1991** também não tem página, mas o ogol tem a final (Sport x Náutico): entra com ela.
   - 8.749 jogos, 71 clubes (46 novos no banco), 2.273 gols com autor (de 27.705), nenhum cartão e 95 artilheiros.
   - Tabelas publicadas: 241 fecham com os jogos e 132 divergem.
   - Fontes:
     - RSSSF Brasil (`tablesfq/pe{ano}.htm`; campeões em `pecamp.htm`; 1915-1970 do livro de Cordeiro e Cordeiro). Todas as páginas vieram do próprio site;
     - ogol ("campeonato-pernambucano"), com os calendários em `data/cache/ogol-bra-pe-1/`. Tem jogos de 1915-1919, 1976, a final de 1991 e de 1999 a 2026;
     - Wikipédia em português: o artigo "Campeonato Pernambucano de Futebol Masculino" (campeão, vice, 3º e 4º de cada ano).
   - O campeão e o vice batem com a RSSSF e a Wikipédia em todas as edições.
2. **Commit:** o deste recado (`Coleta Pernambucano (bra-pe-1): 112 edições, 8.749 jogos`).
3. **Teste de carga:** `bra-pe-1: 112 edições, 8749 jogos, 46 clubes novos -> OK`. O carregador ignora a tabela por rodada em 13 temporadas com mais de uma fase.
4. **Pedidos ao banco e ao painel:**
   - **Carregar `bra-pe-1`.** `competicao.json`: `tipo` estadual, `nivel` 1, `regiao` PE, `rotulo_painel` "Pernambucano".
   - **Jogos "awd" sem placar:** 1915 tem cinco vitórias de placar desconhecido e há W.O.s nos anos 1920; vêm como "awd", gols vazios, vencedor na observação (como no Mineiro).
   - **Nomes:** nenhum nome que já existia mudou e nenhum se repete no cadastro comum. Usam a ficha que já estava no cadastro (Séries C e D): América-PE (18913), Flamengo-PE (3243, Arcoverde), Porto-PE (3405), Ypiranga-PE (3540), Sete de Setembro-PE (15173), Paulistano-PE (66985), Vitória-PE (16927, até 1998) e Santo Amaro-PE (3422, o Manchete do banco). Novos com nome dado à mão: "Estudantes do Recife" (anos 1950; não é o Estudantes de Timbaúba), "Atlético Caruaru" (1979-1990) e "Comercial-PE" (Serra Talhada).
   - **Ficha comum (`registro.FICHA_COMUM`):** nada novo.
5. **Decisões:**
   - **Que eu tomei:**
     - pelo ogol, a AA Santo Amaro, o "Recife" da RSSSF (1997-2004) e o Manchete são o mesmo clube (ficha 3422);
     - "Ferroviário" é o do Recife até 1998 e o de Serra Talhada depois; "Atlético" é o Atlético Caruaru até 1999 e o Atlético Pernambucano depois; "Vitória" é o Vitória-PE até 1998 e o Vitória das Tabocas depois;
     - 1991 entra com a final do ogol (o escopo previa só o pódio);
     - 1915: o empate América x Peres, sem placar na RSSSF, entra com o 0-0 do ogol, que fecha com a tabela publicada;
     - 1976: as datas vêm do ogol (a página traz o turno e o returno lado a lado, com as datas misturadas);
     - 1978-1997: o turno vai na frente das fases de dentro dele ("2º Turno - Segunda fase", "3º Turno - Final");
     - a prorrogação entra no placar (1979, 1980, 1982), com o placar dos 90 minutos na observação.
   - **Que esperam o Guilherme:** nenhuma.
6. **O que não deu e pendências:**
   - **Páginas da RSSSF incompletas:** 2023 para na 4ª rodada e 2025 não tem a final; o resto vem do ogol.
   - **Identidade a revisar:** o "Vitória" (16927) até 1998 e o Vitória das Tabocas depois (o ogol diz que este foi fundado em 2008, mas tem jogos dele desde 1999); o Varzeano FC (1919-1921) e o Varzeano SC (1933) ficam juntos.
   - **Autores dos gols:** 8%.
7. **Onde a revisão deve olhar primeiro:**
   - as fases dos turnos de 1978-1997 (`rsssf_pe1.ANOS_TURNOS`, `_turno_nos_titulos` e `importar.fase_turno`), onde fica a maioria das tabelas divergentes;
   - os nomes dados à mão (`importar.NOME_CODIGO` e `NOME_ANO`) e os clubes "rs-pe1-...";
   - as 132 tabelas divergentes.
8. **Próximo campeonato:** Alagoano (`bra-al-1`), 11º do ranking da CBF; escopo antes, só com o ok do Guilherme.
