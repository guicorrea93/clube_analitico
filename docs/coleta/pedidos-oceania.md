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
2. **Commits:** nenhum ainda (esperando o ok do Guilherme).
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
