# Pedidos da coleta Oceania ao agente 1 (banco e painel)

Arquivo do agente de coleta Oceania (países da OFC). Aqui ficam os pedidos ao banco e ao painel, as respostas e, no fim,
um "Recado de fim de coleta" por competição (regra da seção 10 de `docs/agentes-internacionais-COMECE-AQUI.md`).

Guia de quem continuar: `coleta/comum-oceania/COMECE-AQUI.md`.

## Pedidos abertos

Nenhum por enquanto (o da NZ está no recado abaixo).

## Recado de fim de coleta — nzl-1 — 23/11/2026

1. **O que foi feito:** Campeonato Neozelandês (`nzl-1`), 55 edições (1970 a 2025), 7.480 jogos, 101 clubes, 26.352 gols, 2.888
   com autor (1993-2007/08), nenhum cartão. Fontes: RSSSF (base), Wikipédia em inglês (ligas regionais de 2022-2025, tabela de
   1992, 2ª fonte do campeão) e ogol (fase de liga de 2010/11 e 2011/12, ligas Central e Southern de 2025, datas). A ESPN não
   cobre a NZ. Campeão de toda edição confere com a lista da RSSSF e, onde há, com a Wikipédia.
2. **Commits:** `d7a6379` (pacote, código, documentação e este recado), com o ok do Guilherme em 23/11; sem push.
3. **Teste de carga:** `nzl-1: 55 edições, 7480 jogos, 101 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar `nzl-1`; país novo `NZL` (Nova Zelândia, confederação `OFC`, nova no banco). A NZ foi à Copa (1982, 2010):
     confira se a bandeira já existe;
   - fases novas: "Fase regional" (grupos com o nome da liga: "Northern League", "Central League", "Southern League"; em 1999
     "North Island Soccer League" e "South Island Soccer League"), "Fase nacional", "Rodada eliminatória" e "Final preliminar"
     (o sistema de playoff australiano: o perdedor da semifinal maior tem 2ª chance);
   - 1994: a "Fase nacional" só tem a tabela (está em `tabelas_publicadas.csv` e na classificação), sem jogos;
   - 1996 e 1996/97: empates da fase de liga decididos nos pênaltis valendo ponto extra (há pênaltis em jogos de liga); 4
     pontos por vitória (`pontos_vitoria` = 4); `ajuste_pontos` traz o bônus;
   - classificação final das edições com fase regional: os clubes da fase nacional primeiro (campeão e vice no topo), depois
     os eliminados na fase regional, pela posição no grupo, com a campanha da fase regional (dito na observação);
   - `formato` com "jogos incompletos" em 1994 (fase nacional) e 2025 (1 jogo da Central League a menos);
   - escudos: calendários do ogol em `data/cache/ogol-nzl-1/` (2008/09 a 2025); grafia do ogol no `nomes_fonte`.
5. **Decisões:**
   - escopo aprovado pelo Guilherme (23/11): começa em 1970; campeão da lista oficial (desde 1993 o da final, com o 1º da fase
     de liga na observação); 2004 e 2021 fora; ligas regionais como 1ª fase; "Wellington Phoenix Reserves" (e "Auckland FC
     Reserves" em 2025) para os times reserva;
   - identidade (docstring de `coleta/nzl-1/clubes_nzl.py`): Wellington Diamond United = Wellington United; University-Mount
     Wellington = Mount Wellington (como a contagem de títulos da RSSSF); "Auckland City" de 1972 = Mt Albert-Ponsonby (o
     Auckland City de 2004 em diante é outro clube); Otago United = Southern United; Waikato FC, WaiBOP United e Hamilton
     Wanderers separados; Waitakere City e Waitakere United separados; Courier Rangers (Auckland) separado do Christchurch Rangers;
   - correções com motivo em `coleta/nzl-1/explicacoes.py` (1978, 1982 e 1987 pela tabela e pela lista de rodadas; 1989 pela nota
     da página; 2000 e 1996/97 pelos autores dos gols; 2006/07 vitória dada sem gols; 2024 placar invertido na Wikipédia);
   - nada esperando o Guilherme.
6. **O que não deu para coletar:** jogos da fase nacional de 1994 (só tabela em todas as fontes); autores dos gols de 1970-1992,
   1994, 1997/98 e de 2008/09 em diante (o ogol tem só na página de cada jogo); datas de 1970-1995 e das ligas regionais de
   2022-2024; hora, estádio, público, cartões e artilheiros.
7. **Onde a revisão deve olhar primeiro:**
   - ligas regionais de 2023, 2024 e 2025 (Wikipédia e ogol discordam da tabela da RSSSF; ver `conferencia.csv`);
   - diferenças de um gol entre matriz e tabela em 1973, 1982, 1988, 1990, 1991 e 1993 (explicadas, jogos não identificados);
   - 1992: classificação pela tabela da Wikipédia (a da RSSSF não fecha);
   - fusões tratadas como o mesmo clube (Mount Wellington, Wellington United) e a separação Hamilton AFC x Melville United (a
     Wikipédia liga o "Waikato United" dos anos 1990 ao artigo do Melville United; mantive separados, como a RSSSF).
8. **Próxima competição:** Taiti (`tah-1`), quando o Guilherme mandar.

**Para o agente da Ásia (A-League):** os nomes da NZ que podem colidir com clubes australianos antigos (NSL): "Eastern Suburbs",
"Western Suburbs", "Canterbury United", "Wellington Phoenix Reserves". Quem chega depois acrescenta a cidade.

## Recado de fim de coleta — tah-1 — 24/11/2026

1. **O que foi feito:** Campeonato Taitiano (`tah-1`), 79 edições (1948 a 2025/26), 31 com jogos; 2.647 jogos, 35 clubes,
   11.748 gols, 113 com autor, nenhum cartão. Fontes: RSSSF (lista de campeões e páginas por temporada), Wikipédia em inglês
   (2ª fonte do campeão) e ogol (datas e grafia para os escudos em 2012/13, 2013/14, 2021/22 e 2023/24). Campeão de toda edição
   confere com a RSSSF; a Wikipédia diverge só em 1956, 1957 e 1961 (decidido: vale a RSSSF).
2. **Commits:** nenhum ainda (esperando o ok do Guilherme).
3. **Teste de carga:** `tah-1: 79 edições, 2647 jogos, 35 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar `tah-1`; país novo `TAH` (Taiti, OFC). O Taiti nunca foi à Copa: **falta a bandeira**;
   - **pontuação não é 3-1-0:** 4 por vitória, 2 por empate e 1 por derrota na maior parte dos anos (3-2-1 em 1969-1971 e
     2007/08; 3-1-0 de 1998/99 a 2002/03). `pontos_vitoria` traz só a vitória; o resto está no `formato` de cada edição. A
     classificação traz os pontos oficiais (com bônus e punições em `ajuste_pontos`): o painel não deve recalcular os pontos
     pelos jogos;
   - 48 edições só com campeão (e o vice em 8 delas), sem jogos nem tabela; `formato` = "só o campeão";
   - "jogos incompletos" em 1968 e de 1998/99 a 2004/05 (muitos resultados só com "venceu"/"perdeu" ficaram de fora), 2010/11
     (playoff só com tabela) e 2011/12 (só as tabelas);
   - fases novas: "Fase regular", "Playoff do título", "Grupo do rebaixamento";
   - jogos anulados e repetidos: o anulado entra com `resultado_especial` = `n/p`, sem placar (está na observação);
     "derrota para os dois" (2021/22) entra como `awd` sem placar;
   - clubes da ilha de Mooréa (região "Mooréa") e seleções de base do Taiti que jogaram a liga ("Tahiti U-17", "Tahiti U-19",
     "Tahiti U-20");
   - escudos: calendários do ogol em `data/cache/ogol-tah-1/`.
5. **Decisões:** escopo aprovado pelo Guilherme em 24/11 (desde 1948, até 2025/26, "2025/26" nas temporadas que cruzam o ano,
   nomes com "AS", RSSSF em 1956/1957/1961); identidade em `coleta/tah-1/clubes_tah.py` (Punaruu = AS Tamarii Punaruu, Temanava
   = AS Tamarii Temanava, JS Arue = AS Arue, "Paea" de 1971 = AS Manu-Ura); correções com motivo em `coleta/tah-1/explicacoes.py`.
   Nada esperando o Guilherme.
6. **O que não deu para coletar:** jogos e tabelas de 1948-1967 e 1972-1998 (só o campeão), jogos de 1998/99 a 2004/05 em
   parte, 2011/12; autores dos gols (quase nenhum), artilheiros, cartões, estádio e público.
7. **Onde a revisão deve olhar primeiro:** campeões de 1956, 1957 e 1961 (RSSSF x Wikipédia); classificação de 2004/05 (lida à
   mão de tabelas só com pontos); as edições parciais de 1998/99 a 2004/05; as identidades acima.
8. **Próxima competição:** Nova Caledônia (`ncl-1`), quando o Guilherme mandar.
