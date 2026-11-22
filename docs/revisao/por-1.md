# Revisão — Campeonato Português (`por-1`)

22/11/2026 (3ª rodada, revisão profunda). **Nada disto está no ar:** o `por-1` ainda não foi carregado no banco nem
publicado; a revisão foi feita no pacote `data/coleta/por-1/pacote/`. Achados `PT-001` a `PT-022`.

**Resumo:**
- Pacote sólido: 20.918 de 20.936 placares batem com o Transfermarkt; campeões 92/92; números da seção 1 da ficha batem com o pacote.
- O pacote **não carrega hoje**: "Sanjoanense" já existe no banco (Brasil, bra-sp-2) (PT-001). E uma correção da coleta está errada: 1994/95 Benfica x Sporting foi 1-2, não 2-0 (PT-002).
- Altas: vice de 1944/45 é o Sporting (PT-003); 1986/87 Braga x Benfica teve derrota para os dois (PT-004, decisão). Mais 3 decisões: Porto 2007/08, Académica x Naval 2005/06, identidade do Estrela da Amadora (e dos Elvas).

Scripts em `revisao/PT/`; páginas em `data/cache/revisao/PT/`.

## A. Edições e títulos
- **Conferido:** 92 edições (1934/35–2025/26, sem buraco); campeão e vice de todas contra a infobox da Wikipédia pt
  (fonte que a coleta não usou) e a lista de campeões da RSSSF.
- **Resultado:** campeões 92/92 ok; vices 91/92 — **PT-003** (1944/45: Sporting, não Belenenses).
- Campeonato da Liga 1934/35–1937/38: a RSSSF chama de "unofficial" e dá o título da época ao Campeonato de Portugal,
  mas a FPF considera oficiais esses títulos e a contagem atual bate (Benfica 38, Porto 31, Sporting 21) — **PT-021**
  (não é erro). Nomes de época (Campeonato da Liga, Primeira Divisão, Primeira Liga) ok.
- Fontes: https://pt.wikipedia.org/wiki/Primeira_Liga ; https://www.rsssf.org/tablesp/portchamp.html

## B. Classificação final
- **Conferido:** 85 tabelas legíveis da Wikipédia pt (1.286 linhas: posição, J, V, E, D, gols, pontos); rebaixados de
  33 temporadas contra a seção "Despromovidos" da pt; todos os rebaixamentos fora das últimas posições, um a um;
  pontos por vitória e número de clubes por época; última rodada x classificação final (varredura).
- **Resultado:** 78/85 na mesma ordem; 61/85 com os números idênticos — quase todas as diferenças são erro de digitação
  da pt (ponto ou gol trocado numa linha; o pacote fecha com a RSSSF e a Wikipédia en). Achados:
  - **PT-003** (alta) 1944/45: ordem da Wikipédia en só sai do critério "saldo"; RSSSF, pt e confronto direto dão Sporting 2º e Olhanense 6º;
  - **PT-004** (alta, decisão D3) 1986/87: derrota dada a Braga e Benfica; Braga 9º → 11º;
  - **PT-002** (média) 1994/95: pontos do Sporting (55) e do Benfica (47) errados por causa da correção errada;
  - **PT-005** (média, decisão D2) 2005/06: Naval 13º e Académica 14º pelo confronto direto entre os três; o pacote é incoerente (a rodada a rodada já termina assim);
  - **PT-006** (média, decisão D1) 2007/08: Porto 69 x 75; Leiria -3;
  - **PT-016** (baixa) rebaixamentos fora da zona sem explicação (Leça 1997/98, liguilhas de 1950/51, 1961/62, 1973/74);
  - **PT-014**, **PT-015** (baixa) observações com códigos crus da Wikipédia en (46) e em inglês (50).
- Ok (não é erro): 2 pontos por vitória até 1994/95; 8 a 20 clubes conforme a época; 2019/20 parado e retomado em
  03/06/2020; Gil Vicente 2005/06, Boavista 2007/08, Estrela 2008/09 e V. Setúbal/Aves 2019/20 rebaixados fora de
  campo; 1974/75 (Académica 13º pela média de gols, coerente com o Oriental rebaixado) — **PT-022**.
- Fontes: https://pt.wikipedia.org/wiki/Primeira_Divis%C3%A3o_de_1950%E2%80%9351 (e demais temporadas); https://www.rsssf.org/tablesp/portchamp.html

## C. Jogos
- **Conferido:** todos os jogos contra o calendário do **Transfermarkt** (20.936 de 20.978 casados por temporada +
  mandante + visitante; mínimo de 342 jogos por década) e 16.143 contra as matrizes da **Wikipédia pt**; datas contra o
  Transfermarkt e, de 1994/95 em diante, também contra o football-data; varredura de datas impossíveis; jogos
  decididos fora de campo (amostra de 11 correções da coleta: 8 confirmadas, 1 errada, 2 discutíveis).
- **Resultado placar:** 20.918/20.936 iguais ao Transfermarkt; 16.072/16.143 iguais à pt. Achados:
  - **PT-002** (média) 1994/95 Benfica 1-2 Sporting (correção da coleta errada; prova: artigo da temporada do Benfica com marcadores, público e árbitro);
  - **PT-007** (média) 1980/81 Benfica 2-1 Espinho e Espinho 2-0 Benfica;
  - **PT-009** (baixa) 1974/75 CUF x V. Setúbal: o motivo do TRIBUNAL diz que a versão da RSSSF não fecha, mas fecha;
  - **PT-008** (não é erro) 1963/64 e 1965/66: Transfermarkt e Wikipédias divergem, mas as fichas do ogol têm marcadores que confirmam o pacote.
- **Resultado datas:** antes de 1994/95 o Transfermarkt põe tudo na data da rodada (sem valor de prova). De 1994/95 em
  diante (9.264 jogos com as 3 fontes): 26 jogos com a data do ogol isolada — **PT-011**. Datas impossíveis (clube com
  2 jogos no mesmo dia ou em dias seguidos): 5 casos — **PT-010** (1938/39, 1939/40, 1979/80, 1993/94, 1997/98).
- Cobertura (ficha, seção 4): **PT-019** (marcadores 1999/00–2005/06 pela RSSSF, em lote) e **PT-020** (árbitro 0% e público antigo pelo Transfermarkt).
- Fontes: https://www.transfermarkt.com/primeira-liga/gesamtspielplan/wettbewerb/PO1?saison_id=1994 ; https://en.wikipedia.org/wiki/1994%E2%80%9395_S.L._Benfica_season ; https://en.wikipedia.org/wiki/1986%E2%80%9387_S.L._Benfica_season ; lista: `revisao/PT/datas_divergentes.txt`

## D. Gols e artilheiros
- **Conferido:** 92 temporadas (99 linhas) contra a Bola de Prata (Wikipédia en) e a infobox da pt; de 2006/07 em diante
  também contra os gols da ESPN do próprio pacote; soma dos gols com autor por jogo ≤ placar (todos os jogos).
- **Resultado:** 91/92 ok. **PT-012** (média) 2018/19 Seferović 23, não 33 (erro de digitação da RSSSF);
  **PT-013** (baixa) caractere sobrando no nome do Luis Suárez (2025/26). Nenhum jogo com mais gols com autor que o placar.
- Fonte: https://en.wikipedia.org/wiki/Bola_de_Prata_(Portugal)

## E. Clubes
- **Conferido:** os 73 clubes contra a tabela `clube` do banco e os `clubes.csv` de todos os pacotes (nome único no
  mundo); identidade (SADs, fusões, refundações).
- **Resultado:** **PT-001** (alta) "Sanjoanense" repetido com o clube brasileiro: o teste de carga falha hoje
  (`NomeRepetido`). Identidade: Belenenses x Belenenses SAD, AVS x Desportivo das Aves, Boavista, Salgueiros, Farense,
  Campomaiorense ok (**PT-022**); decisões **PT-017** (Estrela da Amadora 1932 x 2020, junto no pacote; as Wikipédias
  separam) e **PT-018** (SL Elvas x O Elvas, separados; o Transfermarkt junta).
- Escudos: não se aplica ainda (clubes fora do banco; os calendários do ogol para os escudos estão em `data/cache/ogol-por-1/`).

## F. Painel
- Não se aplica: o `por-1` não está no painel nem no site.

## Perguntas ao Guilherme
Detalhe, prova e recomendação de cada uma em `decisoes_PT.md` (scratchpad da revisão).
1. **D1 (PT-006)** Porto 2007/08: 69 pontos (desconto do Apito Final) ou 75 (pontos devolvidos pelo Conselho de Justiça em 2017)? Recomendo 75 com observação; Leiria fica -3.
2. **D2 (PT-005)** 2005/06: Naval 13º e Académica 14º (confronto direto entre os três, RSSSF e Wikipédia pt)? Recomendo sim.
3. **D3 (PT-004)** 1986/87 Braga x Benfica: vale a derrota dada aos dois pela Federação (Benfica 48, Braga 11º) ou o 1-1 de campo? Recomendo a derrota para os dois.
4. **D4 (PT-017)** Estrela da Amadora de 1932 e o de 2020 são o mesmo clube? Recomendo manter junto, com observação.
5. **D5 (PT-018)** SL Elvas e O Elvas: separados? Recomendo manter separados.
