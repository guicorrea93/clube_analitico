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
2. **Commits:** nenhum ainda (esperando o ok do Guilherme).
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
