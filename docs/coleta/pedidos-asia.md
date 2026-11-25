# Pedidos do agente de coleta Ásia

**Para saber o que temos, o que falta e por onde continuar:** `coleta/comum-asia/COMECE-AQUI.md` (guia) e
`coleta/comum-asia/documentacao/` (índice `README.md` e uma ficha por competição, gerada por `documentar.py`).

Recados ao agente 1 (banco e painel) e ao agente de revisão. Ao fim de cada liga entra aqui o "Recado de fim de coleta"
(8 itens da seção 10 de `docs/agentes-internacionais-COMECE-AQUI.md`), com os países novos para as bandeiras.

## 23/11/2026 — início do agente

- Pasta comum `coleta/comum-asia/` montada a partir de `coleta/comum-sulamerica/` (ogol, ESPN, RSSSF, Wikipédia,
  teste de carga e documentação).
- Primeira liga: Japão (`jpn-1`). Cache da ESPN em `data/cache/espn-asia/`.

## Recado de fim de coleta — jpn-1 — 23/11/2026

1. **Feito:** Campeonato Japonês (`jpn-1`), 60 edições (JSL 1965 a 1991/92 e J1 1993 a 2025; 1992 sem liga), 12.190 jogos,
   40 clubes (todos `JPN`), 27.554 gols com autor (J1: 100%) e 31.272 cartões (J1). Fontes: J.League Data Site (site
   oficial: jogos, autores com minuto, cartões, árbitro, público, tabelas oficiais), RSSSF (JSL), Wikipédia em inglês
   (campeão, vice e artilheiro), ogol e ESPN (conferência dos placares). Pacote em `data/coleta/jpn-1/pacote/`,
   relatório em `docs/coleta/jpn-1.md`, ficha em `coleta/comum-asia/documentacao/jpn-1.md`.
2. **Commits:** `71d5006` (no GitHub, 24/11).
3. **Teste de carga:** `jpn-1: 60 edições, 12190 jogos, 40 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar `jpn-1`; **país novo: Japão (`JPN`, AFC)**, em `paises.csv`: baixar a bandeira (o Japão foi a Copas, deve
     já haver bandeira no painel da Copa);
   - temporadas "1985/86" a "1991/92" (calendário europeu) no meio de anos fechados;
   - nos anos de turnos (1993-1995, 1997-2004, 2015, 2016) as fases são "1º turno"/"2º turno" (liga) e "Final"
     (ida e volta; 2015-16 também "Semifinal"); o campeão é o da final, em 1º na classificação final, mesmo sem ser o 1º
     da soma dos turnos;
   - `pontos_vitoria` vazio em 1993 e 1994 (sem pontos: ordem por vitórias) e `pontos` vazio na classificação desses
     anos; 4 em 1977-1979 (pênaltis valiam 2/1: `ajuste_pontos` = pontos das vitórias nos pênaltis);
   - jogos de 1993-1998 com `penaltis_mandante`/`penaltis_visitante` (empate na prorrogação decidido nos pênaltis);
   - JSL sem data nem rodada (só 1988/89 tem); `classificacao_rodada` só nos anos de turno único com 3/1/0 (2005-2014
     e 2017-2025);
   - um jogo `awd` (2021, Urawa x Shonan, 0-3 oficial; 2-3 em campo em `gols_texto` e na observação);
   - árbitro na observação de cada jogo da J1 ("árbitro: ...");
   - escudos: calendários do ogol em `data/cache/ogol-jpn-1/` (1993-1996 e 2004-2025; o ogol não tem 1997-2003); os
     clubes só da JSL (NKK, Honda FC, Nagoya Bank, Toyoda ALW, Tanabe Pharmaceuticals, Eidai Industries, Nippon Steel
     Yawata) e o Yokohama Flügels não estão no ogol da J1.
5. **Decisões:** do Guilherme (23/11): JSL incluída; clube de empresa = clube atual da J.League (Toyo/Mazda = Sanfrecce,
   Mitsubishi = Urawa, Nissan = Yokohama F. Marinos, Yomiuri = Tokyo Verdy, Toshiba = Consadole Sapporo...), Flügels
   separado; campeão dos anos de turnos = o da final. Do agente: repescagem J1/J2 de fora (como no Alemão); rebaixado =
   ausente na edição seguinte (fora Eidai 1976 e Flügels 1998, que fecharam; nada em 1991/92); artilheiro pela lista
   oficial da Wikipédia (a soma por nome erra em 1994: "Otze" e "Ordenewitz" são o mesmo jogador), com os 24 gols do
   Will em 2001 (a lista diz 20). Nada esperando o Guilherme.
6. **Não coletado / pendências:** JSL sem data, rodada e autores (fonte: livro oficial "Nihon Soccer League Zenshi");
   1966, 1971 e 1973 com a tabela de confrontos da RSSSF 1 a 4 gols diferente da tabela final (explicado na edição);
   1977-1979 sem quem ganhou cada disputa de pênaltis; J1 sem marca de gol de pênalti e sem o nome de quem fez gol contra;
   artilheiro de 1986/87 (17 na Wikipédia, 14 na RSSSF).
7. **Onde a revisão deve olhar primeiro:** classificação final dos anos de turnos de 1993-1998 (soma das tabelas dos
   turnos, ordenada por mim; não há tabela anual oficial); identidade dos clubes da JSL (`clubes_jpn.py`); as três
   edições da JSL com divergência; o jogo `awd` de 2021.
8. **Próxima competição:** Coreia do Sul (`kor-1`), depois das decisões de escopo do Guilherme.

## Recado de fim de coleta — kor-1 — 24/11/2026

1. **Feito:** Campeonato Sul-Coreano (`kor-1`), 43 edições (K League 1983 a 2025), 7.163 jogos, 25 clubes (todos `KOR`),
   17.984 gols com autor (23 jogos sem autores) e 24.627 cartões. Fontes: portal de dados oficial da K League (boletim de
   cada jogo: autores com minuto, pênalti e gol contra, cartões, disputa de pênaltis, estádio, público, árbitro); site
   oficial (www.kleague.com: lista de jogos 2013+, linha do tempo em coreano e inglês 2013+, classificação final oficial
   2003-2025); RSSSF (tabelas 1983-2009 e páginas de cada ano: conferência); Wikipédia em inglês (campeão, vice,
   artilheiro) e em coreano (desempate das divergências); ogol (2008-2025: conferência e escudos). Pacote em
   `data/coleta/kor-1/pacote/`, relatório em `docs/coleta/kor-1.md`, ficha em `coleta/comum-asia/documentacao/kor-1.md`.
2. **Commits:** `e04507f` e `7abc4ec` (no GitHub, 24/11).
3. **Teste de carga:** `kor-1: 43 edições, 7163 jogos, 25 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar `kor-1`; **país novo: Coreia do Sul (`KOR`, AFC)**, em `paises.csv`: a Coreia foi a Copas, deve já haver
     bandeira no painel da Copa;
   - fases: "Liga" (com a divisão em grupo do título e grupo de baixo de 2012 em diante dentro dela, como no Escocês: a
     observação do jogo diz o grupo); "1º turno"/"2º turno" em 1984, 1986, 1995, 1996 e 2004-2006; "Final" (1984, 1986,
     1995 com 3 jogos, 1996) e playoff ("Primeira fase", "Segunda fase", "Semifinal", "Final") em 1998-2000 e 2004-2011;
   - pontos diferentes: 1984 (3 pela vitória, 2 pelo empate com gols, 1 pelo 0-0: `pontos_vitoria` 3 e os pontos oficiais
     na classificação); 1993 (`pontos_vitoria` 4; empate decidido nos pênaltis, 2 para quem ganha e 1 para quem perde);
     1998-1999 (3 no tempo normal, 2 na prorrogação com gol de ouro, 1 nos pênaltis); 2000 (3 no tempo normal ou na
     prorrogação, 1 nos pênaltis). Nesses anos não há empate: os jogos têm `penaltis_mandante`/`penaltis_visitante`. A
     `classificacao_final` traz os pontos oficiais;
   - de 2003 em diante a classificação final é a oficial da K League (de 2003 a 2011 os jogos, vitórias e gols contam o
     playoff; os pontos, só a liga); `ajuste_pontos` -9 do Jeonbuk em 2016 (suborno de árbitros);
   - 16 jogos `wo`: 1987 (2, sem placar: a tabela oficial conta a vitória sem gols; o vencedor na observação) e 2012 (14 do
     Sangju Sangmu, 0-2 dado; a tabela conta os gols); 2 jogos `awd` (1996 Pohang 3-0 Suwon; 2021 Gwangju 0-3 Jeju; o
     placar de campo no `gols_texto` e na observação);
   - 1998, Chunan Ilhwa (Seongnam FC) x Jeonnam: 1-1, pênaltis 5-5 e vitória do Seongnam no sorteio (sem refletores): a
     observação diz o vencedor; se o painel recalcula pelos pênaltis, esse jogo precisa usar a observação;
   - classificacao_rodada só de 2013 em diante; 958 jogos antes de 2013 sem rodada;
   - árbitro na observação de cada jogo ("árbitro: ..."); estádio traduzido do hangul por regra; cidade em branco;
   - escudos: calendários do ogol em `data/cache/ogol-kor-1/` (2008-2025); clubes antigos fora do ogol: Hallelujah FC,
     Kookmin Bank, Hanil Bank, Sangmu (1985, sem cidade), Chonbuk Buffalo, Gwangju Sangmu.
5. **Decisões:** do agente, a pedido do Guilherme ("faça uma pesquisa mais a fundo para julgar o que é necessário"):
   K League desde 1983, sem a liga semiprofissional (outra competição, a K League conta desde 1983); clube por código do
   portal oficial (Yukong/Bucheon SK = Jeju United, Daewoo = Busan IPark, Lucky-Goldstar/LG = FC Seoul, Ilhwa = Seongnam
   FC; os quatro times do Exército separados, como a K League); campeão oficial; copa da liga e repescagem contra a K
   League 2 de fora; 2026 quando acabar. Nas divergências entre o portal e a RSSSF valeu o que a Wikipédia em coreano e
   as tabelas confirmam (prova em `coleta/kor-1/explicacoes.py`). Nada esperando o Guilherme.
6. **Não coletado / pendências:** 23 jogos sem autores (os que o boletim tem estão no `gols_texto`; fonte: Wikipédia em
   coreano, resultados de cada ano); 197 estrangeiros de antes de 2013 com o nome romanizado do hangul (lista no
   relatório); 1997, linha do Jeju na RSSSF sem explicação; artilheiro: soma 1 gol abaixo da lista oficial em 7 anos.
7. **Onde a revisão deve olhar primeiro:** os casos de `explicacoes.py` (W.O., awd, sorteio, gol que faltava em 1990);
   os jogos em que o total do boletim e a soma dos lances não batem (listados em cada edição do relatório); a ordem da
   classificação de 1983-2002 (calculada: campeão e vice da decisão em cima, depois a tabela); os nomes dos estrangeiros
   (`nomes_kor.py`).
8. **Próxima competição:** Arábia Saudita (`ksa-1`), depois das decisões de escopo do Guilherme.

## Recado de fim de coleta — ksa-1 — 25/11/2026

1. **Feito:** Campeonato Saudita (`ksa-1`), 69 edições (1957/58 a 2025/26, como o relatório oficial da federação de
   2025), 5.965 jogos, 43 clubes (todos `KSA`), 7.296 gols com autor e 4.801 cartões. Fontes: RSSSF (tabelas de
   1974/75 em diante, jogos em 1974/75, 1976/77, 1980/81, 1982/83, 1983/84, 1986/87 e 1997/98-2024/25, playoffs,
   autores até 2005/06), ogol (fase de liga 1999/00-2025/26), ESPN (2022/23-2025/26: autores, cartões, estádio, público,
   hora), Wikipédia (lista oficial de campeões e vices). Pacote em `data/coleta/ksa-1/pacote/`, relatório em
   `docs/coleta/ksa-1.md`, ficha em `coleta/comum-asia/documentacao/ksa-1.md`.
2. **Commits:** (preencher depois do "sim").
3. **Teste de carga:** `ksa-1: 69 edições, 5965 jogos, 43 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar `ksa-1`; **país novo: Arábia Saudita (`KSA`, AFC)**: a Arábia Saudita foi a Copas, deve já haver bandeira;
   - temporadas no formato "1957/58"; 12 edições sem jogos: 1966/67, 1967/68 e 1969/70 (sem campeão), 1968/69 (sem a
     final) e os anos só com a tabela da RSSSF (1977/78-1979/80, 1984/85, 1985/86, 1987/88-1989/90); 1975/76 tem 16 jogos
     e não tem campeão (abandonada); 1957/58-1973/74 com só a final (fase "Final") e a classificação com 2 linhas
     (campeão e vice, sem números);
   - classificação com números vazios onde a RSSSF só dá jogos e pontos (1977/78-1981/82) ou só a ordem (1985/86);
   - fases: "Liga" (tipo `grupos` com 2 grupos em 1974/75 e 1981/82) e o playoff ("Semifinal", "Final",
     "Disputa do 3º lugar", "Primeira fase", "Segunda fase") em 1974/75, 1981/82 e 1990/91-2006/07; o campeão é o oficial,
     em 1º na classificação mesmo quando não é o 1º da fase de liga;
   - `pontos_vitoria` 2 até 1992/93 e 3 depois; 7 `ajuste_pontos` (punições/bônus da tabela da RSSSF);
   - 5 jogos `awd` com o placar dado e o de campo na observação;
   - escudos: calendários do ogol em `data/cache/ogol-ksa-1/` (1999/00-2025/26); clubes antigos fora do ogol (Al-Yamamah,
     Al-Rabe'e, Al-Kifah, Okaz, Al-Jabalain, Al-Kawkab, Al-Rawdhah, Al-Arabi de Unaizah, Sadous...).
5. **Decisões:** do Guilherme (24/11): desde 1957, como a federação conta (Al-Hilal 21 títulos). Do agente: até 2025/26;
   temporadas não concluídas/canceladas como edição sem campeão; 1990/91-2006/07 campeão do playoff (o oficial); jogos da
   fase de liga da RSSSF até 2005/06 quando completa, do ogol depois; nomes árabes com hífen e cidade nos homônimos;
   2 correções do ogol com prova (Wikipédia). Nada esperando o Guilherme.
6. **Não coletado / pendências:** jogos de 1957-1974 (só a final) e da fase de liga em 1977/78-1996/97 (só a tabela);
   finais de 1994/95 e 1995/96; autores e cartões de 2006/07 a 2021/22; 36 jogos sem data. Fontes que resolveriam: jornais
   da época, súmulas da Saudi Pro League, FBref/Transfermarkt.
7. **Onde a revisão deve olhar primeiro:** as edições de 1957/58-1973/74 (final da Copa do Rei ligada pelo par de clubes,
   às vezes com o rótulo da temporada anterior); a classificação dos anos de playoff (campeão e vice em cima, depois a
   tabela); os placares RSSSF x ogol listados em cada edição; `clubes_ksa.py` (homônimos e grafias).
8. **Próxima competição:** Irã (`irn-1`), depois das decisões de escopo do Guilherme.
