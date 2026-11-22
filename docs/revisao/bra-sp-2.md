# Revisão — Campeonato Paulista Série A2 (`bra-sp-2`)

Revisão profunda (3ª rodada), 22/11/2026. Prefixo dos achados: A2. Achados com sugestão de correção em
`SCRATCH/achados_A2.csv` (o agente principal junta no `docs/revisao/achados.csv`); scripts em `revisao/A2/`.

**Resumo.** Campeões batem com a lista oficial da FPF (63 de 63, inclusive 1991 Araçatuba) e 180 placares de 2008-2026 batem com a FPF.
Mas faltam 17 edições que existem (1967-1978, 1980-1984), 5 vices estão errados (1979, 1986, 1996, 1997, 2013), quase todos os
rebaixados de 2012-2026 não estão marcados, há 4 acessos falsos e a classificação de 2001 ignora a regra de pontos e uma punição.
30 achados: 11 altos, 12 médios, 7 baixos (1 deles "não é erro"). Nada disso está no ar: a A2 não está no site; está no banco local
e em `painel/dados/bra-sp-2.js` (local, de 22/11 09:14), com os mesmos erros do pacote.

## O que foi revisado

O pacote `data/coleta/bra-sp-2/pacote/` (63 edições, 9.142 jogos, 167 clubes), as fontes guardadas pela coleta, a ficha
`coleta/comum/documentacao/bra-sp-2.md`, o relatório `docs/coleta/bra-sp-2.md` e os recados de 21 e 22/11 em `docs/coleta/pedidos.md`.
Fontes novas (a coleta não usou): FPF (lista oficial de campeões e jogos por rodada pela API do site), Wikipédia pt (páginas de cada
edição de 1979 em diante e a predefinição de campeões com vice, 3º e 4º) e páginas da RSSSF que a coleta não baixou. Detalhes em
`SCRATCH/fontes_A2.md`.

## A. Edições e títulos

- **Conferido:** as 63 edições contra a lista oficial da FPF (`ListarCampeoes.ashx?IdCategoria=2`), a lista da RSSSF (`sp2camp.htm`)
  e a predefinição de campeões da Wikipédia pt.
- **Resultado:**
  - campeões 63 de 63 certos;
  - **faltam 17 edições** (1967-1978 e 1980-1984): A2-001. A ficha diz que são "anos sem 2ª divisão ou sem nenhuma fonte", mas a FPF
    reconhece campeão em todos. A Wikipédia pt tem página de 16 deles (falta 1972), e a RSSSF tem páginas de 1968, 1969, 1971,
    1976, 1980 e 1984 (não linkadas na lista de campeões, por isso o `baixar_rsssf.py` não pegou). Por isso os títulos por clube
    estão errados no painel local: XV de Piracicaba 3 (são 5), Noroeste 1 (são 3), Santo André 3 (são 5);
  - 1991: Araçatuba está certo (A2-030, "não é erro"). FPF, RSSSF e Wikipédia dão o Araçatuba, e os 12 jogos do quadrangular
    dão Araçatuba e Lemense com 8 pontos e saldo +5 contra -1. **Não é preciso perguntar ao Guilherme.**
- **Fontes:** https://futebolpaulista.com.br/Handlers/Clube/ListarCampeoes.ashx?IdCategoria=2,
  https://rsssfbrasil.com/tablessz/sp2camp.htm,
  https://pt.wikipedia.org/wiki/Predefinição:Campeões_do_Campeonato_Paulista_de_Futebol_-_Série_A2

## B. Classificação, acesso e rebaixamento

- **Conferido:**
  - vice, 3º e 4º das 63 edições (predefinição da Wikipédia e tabelas da RSSSF);
  - acesso contra a A1 do ano seguinte (pacote `bra-sp-1`) e o infobox "promovidos" da Wikipédia;
  - rebaixados contra o infobox "rebaixados" da Wikipédia (1994-2026) e a presença no ano seguinte;
  - tabelas da Wikipédia de 1979-2026 contra as campanhas dos jogos do pacote: 326 linhas batem e 65 diferem; as que diferem são
    quase todas nomes antigos ou as divergências que a coleta já explicou.
- **Resultado:**
  - vices errados: 1979 (A2-002), 1986 (A2-003), 1996 (A2-004) e 1997 (A2-005). O importador ordena pelos pontos de todas as fases,
    e não pela tabela da fase final, o mesmo defeito do SP-002 no Paulista;
  - 2013: o vice é o Osasco Audax, que não jogou a final; o certo é o Rio Claro (A2-006);
  - rebaixados (A2-007): nenhum marcado em 2013-2020 e 2022-2026, e faltam clubes em 2000 e 2012. O pacote só marca quando a tabela
    da RSSSF escreve "Relegated", e a leitura da Wikipédia (`pacote.infobox()`) procura arquivos que não existem;
  - 1999: Juventus-SP e Paraguaçuense aparecem como rebaixados, mas só foram ao torneio de rebaixamento (A2-008);
  - acessos falsos (A2-009): 1950 XV de Jaú, 1979 Catanduvense, 2001 Francana e 2002 Atlético Sorocaba. Só aparecem na A1 do ano
    seguinte pela repescagem, que perderam;
  - 2002: a "Portuguesa" do playoff é a Portuguesa Santista, e o acesso está errado (A2-010);
  - 2001: a classificação usa 3-1-0, mas em 2001 os empates iam para os pênaltis, que valiam pontos. O Sãocarlense perdeu 5 pontos.
    O 5º lugar muda (América-SP) e a ordem de baixo também (A2-011);
  - 2004: a 2ª fase está misturada na 1ª, e o 3º e o 4º estão trocados (A2-018);
  - 3º e 4º diferentes da Wikipédia em 9 anos (A2-024, baixo);
  - 1998: o XV de Piracicaba caiu e foi mantido na A2 de 1999. Falta uma observação (A2-026).
- **Fontes:** https://rsssfbrasil.com/tablessz/sp1979l2.htm, sp1986l2.htm, sp1996l2.htm, sp1997l2.htm, sp1999l2.htm, sp2001l2.htm,
  sp2002l2.htm, sp2003l2.htm, sp2004l2.htm, sp2013l2.htm; https://pt.wikipedia.org/wiki/Campeonato_Paulista_de_Futebol_de_2015_-_Série_A2
  (e as demais edições).

## C. Jogos

- **Amostra de placar e data por década, contra fontes independentes:**

  | Década | Fonte | Resultado |
  |---|---|---|
  | 1950s | RSSSF, jogos do campeão (os do pacote vêm da Wikipédia) | 1959: 10 de 10; finais de 1961 e 1962 sem a prorrogação (A2-020) |
  | 1970s e 1980s | Wikipédia (footballbox) | 7 de 7 (finais de 1979, 1985, 1986, 1987 e 1988), mais 149 linhas de tabela batendo |
  | 1990s | Wikipédia (tabelas) | 64 de 76 linhas batem; as que diferem são as divergências já explicadas (1997, 1998, 1999) e nomes de época |
  | 2000s | Wikipédia (footballbox) e FPF | 7 de 7 e 20 de 20 (2008) |
  | 2010s | FPF | 96 de 96 placares e datas |
  | 2020s | FPF | 64 de 64 placares; 48 de 64 datas |

  Ao todo, 180 jogos da FPF de 2008 a 2026: placar 180 de 180, data 164 de 180. As 16 datas erradas são da rodada 7 de 2021 e da
  rodada 8 de 2025 (A2-015, A2-016).
- **Varredura adaptada ao pacote** (`revisao/A2/varredura_pacote.py`, saída em `revisao/A2/varredura_saida.txt`):
  - 95 casos de clube com 2 jogos no mesmo dia: datas herdadas da rodada anterior em 1987, 1998, 1999, 2010, 2011, 2021 e 2025
    (A2-015, A2-016) e datas da própria RSSSF (A2-027);
  - 2 jogos repetidos: 2006, jogo interrompido e completado (A2-013); 2008, jogo anulado pelo TJD que ficou junto do jogo refeito
    (A2-014);
  - 2001: o placar de Nacional x Ituano que fecha com a tabela é o do ogol (A2-017);
  - pênaltis: falta o da final de 2023 (A2-019); a Wikipédia dá pênaltis na final de 2011, e a RSSSF não (A2-028, baixo).
- **Playoffs A1 x A2 dentro da A2** em 1979, 2002 e 2003: clube da A1 contado como participante (A2-012).

## D. Gols e artilheiros

- **Conferido:**
  - artilheiro de cada edição contra o infobox da Wikipédia pt;
  - gols com autor nunca acima do placar (4.526 gols).
- **Resultado:**
  - 36 de 36 batem nos anos que têm os dois;
  - faltam os artilheiros de 1998, 2003 e 2026, que a Wikipédia tem (A2-021);
  - nenhum jogo com mais gols com autor do que o placar.

## E. Clubes

- **Conferido:**
  - os 167 clubes contra o cadastro comum, o `bra-sp-1` e o banco: nenhum nome repetido e nenhuma cidade diferente para o mesmo nome;
  - homônimos por cidade.
- **Identidades pedidas:**
  - certas: Barretos FC (até 1960) x Barretos EC; Catanduva EC dos anos 1950 x Catanduvense; AA Osvaldo Cruz x Osvaldo Cruz FC;
    Araçatuba FC (1954-1955) x AE Araçatuba; "Ferroviária (Botucatu)";
  - erro: 2002, Portuguesa no lugar da Portuguesa Santista (A2-010).
- **Perguntas:**
  - o "Catanduvense" junta o GE Catanduvense (1970) e o Grêmio Catanduvense de Futebol (1999) (A2-022);
  - Barueri x Grêmio Prudente (A2-023).
- **Grafias de cidade:** A2-025 (baixo).
- **Escudos:** não avaliados, porque a competição não está no site. O painel local mostra os escudos dos clubes mais vitoriosos sem
  erro aparente (print em `SCRATCH/A2/tela_historia.png`).

## F. Painel

- A A2 não está no site: https://clubeanalitico.pages.dev/dados/bra-sp-2.js devolve a página inicial, e o seletor do site não tem a A2.
- Ela já está no banco local (`db/futebol.db`: 63 edições, 9.142 jogos) e em `painel/dados/bra-sp-2.js`. O banco confere com o pacote
  e tem os mesmos erros: vices de 1979, 1986, 1996, 1997 e 2013 e só 51 rebaixados.
- Print da aba História no painel local: o cartão mostra "9.138 jogos", 4 a menos que o pacote (jogos sem placar). A "Corrida dos
  títulos" mostra os títulos sem as 17 edições que faltam.
- Antes de publicar, o painel precisa aceitar posição repetida e colunas vazias (A2-029, já pedido pela coleta).

## Perguntas ao Guilherme

1. **A2-022:** o "Catanduvense" de 1979-1995 (GE Catanduvense, de 1970) e o de 2008-2015 (Grêmio Catanduvense de Futebol, de 1999) são
   o mesmo clube? A recomendação é separar, pela regra do clube refundado.
2. **A2-023:** o Grêmio Prudente de 2025-2026 é o Grêmio Barueri, campeão de 2006? A RSSSF diz que sim, e o ogol os separa.
3. **A2-012:** os playoffs A1 x A2 de 1979, 2002 e 2003 saem da A2, como a repescagem de 1951? A recomendação é que sim.
4. **Para incluir 1967-1984 (A2-001):** o EC São José (campeão de 1972) e o São José EC (campeão de 1980) são o mesmo clube? A FPF os
   separa, e a RSSSF os soma.

Opções e provas em `SCRATCH/decisoes_A2.md`; plano por arquivo em `SCRATCH/plano_A2.md`.
