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
