# Revisão: Copa do Brasil (bra-copa-do-brasil)

Data: 20/11/2026 · Revisor: subagente CB · Achados: `CB-001` a `CB-017` (SCRATCH/achados_CB.csv)

**Resumo.** Os 37 campeões, a lista de edições e quase todos os placares estão certos (2.272 de 2.327 confrontos batem com a
Wikipédia pt). O problema grande está nas **fases**: as finais caíram dentro de outras fases, e com isso o **vice está errado
em 9 edições** e a classificação final (3º, semifinalistas) sai fora de ordem em quase todas. Pacote, banco e painel são
iguais (4.011 jogos, 10.644 gols, 2.425 linhas de classificação): os erros nasceram no pacote, menos os de exibição do painel.

## A. Edições e títulos
- **Conferido:** lista de edições (37, 1989–2025, nome "Copa do Brasil", sem a Taça Brasil), campeão e vice das 37.
- **Resultado:** edições ok; campeão 37/37 ok; **vice 28/37** (CB-001: 1989, 1993, 1994, 1995, 1996, 1997, 2012, 2014,
  2025). O erro se espalha para História > Pódio e Corrida dos títulos, cartão "Vices" e Por clube (ex.: Flamengo com vice
  em 1995, que não teve, e sem o de 1997).
- **Fontes:** infobox e quadros da final de cada edição em https://pt.wikipedia.org/wiki/Copa_do_Brasil_de_Futebol_de_1989
  (… até 2025) e https://en.wikipedia.org/wiki/1989_Copa_do_Brasil (… até 2025); https://pt.wikipedia.org/wiki/Copa_do_Brasil_de_Futebol.
- Script: `revisao/CB/podio.py` → `revisao/CB/saida_podio.txt`.

## B. Classificação final (copa)
- **Conferido:** campeão, vice e os 2 outros semifinalistas das 37 edições; o "3º" do painel; ordem da classificação
  (quem saiu depois deve ficar acima); números (J, V, E, D, GP, GC) das 2.425 linhas contra os jogos; sub-aba Participantes
  (amostra 2025 e 1989).
- **Resultado:**
  - números de cada linha batem com os jogos (2.425/2.425);
  - **"3º" é semifinalista em só 21/37** e os 4 semifinalistas estão no top 4 em **só 17/37**; semifinalistas aparecem em
    83º/84º (2018), 82º/83º (2017), 51º (2000); em 36 edições há clube eliminado depois abaixo de clube eliminado antes
    (CB-002). Causa provável: fases erradas (CB-003);
  - Participantes: na copa o painel mostra a divisão de cada clube no ano, sem subir/cair (ok). Os conceitos de liga que
    sobram estão em CB-013.
- Scripts: `revisao/CB/podio.py`, `revisao/CB/ordem_classificacao.py` (saídas `saida_podio.txt`, `saida_ordem_classificacao.txt`).

## C. Jogos
- **Conferido:** total de jogos e de gols das 37 edições contra a infobox pt/en; **todos** os confrontos que as chaves da
  Wikipédia pt trazem (2.327 confrontos, 3.870 jogos; 1989–2012 e 1.ª–3.ª fases de 2013–2025) e as chaves da en (1.207
  confrontos); os 74 jogos das finais (mando e placar pelos quadros da pt/en); datas de 64 jogos com quadro.
- **Resultado:**
  - total: pacote 4.011 jogos, Wikipédia 4.010; 34/37 edições batem. Diferenças: 1999 falta a preliminar, 2007 tem um jogo
    a mais, 2019 conta um jogo anulado pelo STJD, 2021 tem CRB no lugar do Sergipe (CB-007);
  - **fases** com nomes em inglês e finais dentro de "Semifinal", "Third Round" ou "First Round" (CB-003);
  - placares: 2.272/2.327 confrontos iguais na pt; das diferenças, 3 placares mudam quem passou (CB-004) e 8 têm duas
    fontes contra o pacote (CB-005); o resto são diferenças de nome ou da própria pt (conferido com a en);
  - finais: placares certos, mas **2015 e 2016 com ida e volta trocadas de casa** (CB-006);
  - pênaltis: só 84 jogos com pênaltis nos campos; 124 disputas da pt faltam (CB-008), e o painel não mostra pênaltis (CB-009);
  - datas: 58/64 iguais; finais de 1990, 2014 e 2015 1 dia depois (CB-010); observações com lixo da RSSSF (CB-015).
- Lista dos jogos: `revisao/CB/lista_placares.txt`. Scripts: `revisao/CB/confrontos.py` (pt e `en`), `mando.py`, `datas.py`.

## D. Gols e artilheiros
- **Conferido:** artilheiro das 37 edições (artilheiros.csv do pacote e o que o painel mostra) contra a lista da pt
  (Copa do Brasil de Futebol > Artilharia) e as infoboxes pt/en; gols com autor ≤ placar nos 4.011 jogos.
- **Resultado:**
  - gols com autor ≤ placar: 4.011/4.011 ok (nenhum gol de clube estranho ao jogo);
  - pacote: 32/37 ok; 2007 e 2019 com o clube errado, 2018 e 2023 com artilheiro faltando (CB-011); 2001, 2004 e 2005
    com fontes divididas (CB-017, não é erro);
  - **painel:** a Artilharia e o cartão "Artilheiro" usam só os gols com autor (54%) e acertam o artilheiro em só 4 das 24
    edições que têm gols com autor (CB-012).

## F. Painel
- **Conferido:** as 3 abas e as 18 sub-abas (13 prints em 1400 px e 420 px, mais o log do Chrome em 9 rotas) em
  `SCRATCH/CB/` (História: corrida, pódio, pontos, curiosidades; Por campeonato 1989, 2012, 2013 e 2025: resumo,
  classificação, participantes, corrida, jogos, artilharia; Por clube: Flamengo).
- **Resultado:** nenhum erro de JavaScript; maior goleada (Atlético-MG 11×0 Caiçara, 1991) e maior goleada fora
  (Sergipe 0×8 Palmeiras, 1996) conferem com a pt. Problemas: os do pacote aparecem no pódio, nos destaques e na trajetória
  do clube (ex.: Flamengo 84º em 2018, quando foi semifinalista); coisas de liga numa copa (CB-013); "Grupo Grupo 77" em
  2019/2025 (CB-014); sem pênaltis (CB-009); celular mais largo que a tela, já conhecido (CB-016).

## Perguntas ao Guilherme
1. **"3º lugar" na copa:** a Copa do Brasil não tem disputa de 3º. O painel deve mostrar "3º" (o semifinalista de melhor
   campanha) ou trocar por "semifinalistas" (os dois)?
2. **Jogo anulado (2019, Aparecidense 1×0 Ponte Preta, anulado pelo STJD):** sai das contagens (como na Wikipédia, 120
   jogos) ou fica guardado marcado como anulado?
