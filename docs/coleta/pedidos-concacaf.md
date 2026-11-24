# Pedidos da coleta CONCACAF

Recados do agente de coleta da América do Norte e Central (CONCACAF) para o agente 1 (banco e painel) e para o agente de
revisão, e as respostas deles. Cada liga termina com uma seção "Recado de fim de coleta — <slug> — <data>" no fim deste
arquivo (regras na seção 10 de `docs/agentes-internacionais-COMECE-AQUI.md`).

Guia do agente: `coleta/comum-concacaf/COMECE-AQUI.md`.

## 23/11/2026 — início

- Pasta comum `coleta/comum-concacaf/` montada, copiada de `coleta/comum-sulamerica/` (ogol, ESPN, RSSSF, Wikipédia, teste
  de carga e documentação).
- Primeira liga: México (`mex-1`), depois a ordem sugerida (`usa-1`, `crc-1`, `hon-1`, `gua-1`, `slv-1`, `pan-1`, `jam-1`,
  `tri-1`, `can-1`, `hai-1`).
- Escopo do México decidido pelo Guilherme: era amadora (1902/03-1942/43) entra; 1920/21 e 1921/22 com duas edições
  (Liga Nacional e Liga Mexicana), sem o Torneo del Centenario 1921; México 70, Prode 85 e México 86 como edições
  próprias. Invierno/Verano e Apertura/Clausura, uma edição cada; Clausura 2020 sem campeão.
- País novo no banco: México (`MEX`, CONCACAF). Nenhum país da CONCACAF está no banco ainda.

## Recado de fim de coleta — mex-1 — 23/11/2026

Para o agente 1 (banco e painel) e para o agente de revisão.

1. **O que foi feito:** Campeonato Mexicano (`mex-1`), 158 edições (1902/03 ao Clausura 2026), uma por título: era amadora
   (1902/03-1942/43; 1920/21 e 1921/22 com duas ligas), profissional (1943/44-1995/96, mais México 70, Prode 85 e México 86),
   Invierno/Verano (1996-2002) e Apertura/Clausura (2002 em diante). 26.606 jogos, 92 clubes, 76.536 gols (56.671 com autor,
   74%), 42.633 cartões, artilheiros em 152 edições. Fontes: RSSSF (uma página por temporada, tabelas finais `mexhist.html`,
   campeões `mexchamp.html`, artilheiros `mextops.html`), ESPN (`mex.1`, Apertura 2002 em diante: hora, estádio, público,
   gols com minuto, cartões; fase regular do Apertura 2025 e do Clausura 2026) e Wikipédia em inglês (2ª fonte do campeão e
   do vice). Campeão e vice batem com as duas listas em todas as edições.
2. **Commits:** `cb0355f` (24/11). Sem push.
3. **Teste de carga:** `mex-1: 158 edições, 26606 jogos, 92 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar `data/coleta/mex-1/pacote/`;
   - **país novo: México (`MEX`, CONCACAF)**, em `paises.csv` do pacote. O México já foi à Copa do Mundo, mas é o primeiro
     país da CONCACAF no banco: conferir se a bandeira já está no painel;
   - duas edições sem campeão: 1930/31 (cancelada no começo e declarada deserta) e 2020 Clausura (pandemia); a classificação é a
     tabela do momento;
   - duas edições no mesmo ano: "1920/21 Liga Mexicana" e "1920/21 Liga Nacional" (e o mesmo em 1921/22), como LPF e APEA
     no Paulista; "1985 Prode 85" e "1986 México 86" têm `ano_inicio` 1985;
   - nomes de temporada: "1902/03", "1970 México 70", "1996 Invierno", "1997 Verano", "2002 Apertura", "2003 Clausura";
   - duas edições sem jogos (1911/12 e 1916/17: só a tabela) e quatro com jogos incompletos (`formato` começa por "jogos
     incompletos"): 1915/16, 1924/25 e as duas ligas de 1920/21 e de 1921/22;
   - os jogos da fase regular de 1970 a 2011 não têm grupo: os grupos eram só de classificação (todos jogam contra todos);
     México 70, Prode 85 e México 86, em que só se jogava dentro do grupo, têm.
5. **Decisões:**
   - do Guilherme (23/11): era amadora entra; duas ligas em 1920/21 e 1921/22, sem o Torneo del Centenario de 1921; México
     70, Prode 85 e México 86 como edições próprias;
   - decididas em 24/11, depois de pesquisa: o Pachuca AC da era amadora é o Pachuca de hoje: o clube conta a própria história desde 1892 (Pachuca Football Club, depois Pachuca Athletic Club), celebra os 3 títulos amadores (1904/05, 1917/18, 1919/20) e é tratado pela imprensa e pelas Wikipédias como o mesmo clube, com duas paradas (1922-1950 e 1952-1960) e a refundação de 1960 com o mesmo nome; Atlético Español (1971-1982) é o Necaxa (vendido a empresários
     espanhóis em 1971; a Televisa devolveu nome e cores em julho de 1982; todas as fontes tratam como o mesmo clube); 1930/31
     entra sem campeão (a federação declarou o campeonato deserto; as fontes divergem entre duas e quatro rodadas jogadas);
   - do agente: Centro Unión = América; Atlético Morelia = Morelia; Mazatlán (2020) é clube novo, separado do Morelia; nomes
     únicos no mundo: América do México, Santos Laguna, Real Club España, Deportivo Español de México, Sporting de México,
     Nacional de Guadalajara, Laguna de Torreón (lista completa em `coleta/mex-1/clubes_mex.py`).
6. **O que não deu para coletar:** jogos de 1911/12 e 1916/17 e parte dos de 1915/16, 1920/21, 1921/22 e 1924/25 (fonte que
   resolveria: jornais da época na Hemeroteca Nacional Digital da UNAM); o Guadalajara x Pumas do 1º turno de 1995/96 (pela
   tabela, 3-0); estádio só de 2002 em diante (ESPN) e nos jogos com "at X" (as linhas de estádio das páginas ainda não são
   lidas); cerca de 30 edições com diferença de um gol ou de um resultado entre a página e a tabela dela (erro da página,
   explicado no relatório).
7. **Onde a revisão deve olhar primeiro:** as identidades decididas em 24/11 (Pachuca AC = Pachuca, Atlético Español = Necaxa); a era amadora
   (1902/03-1942/43: tabelas e jogos com mais divergências); 1940/41 (tabela de campo x tabela oficial depois de três jogos
   dados aos adversários do Asturias); 1995/96 (jogo que falta); as 33 edições com tabela divergente no `conferencia.csv`.
8. **Próxima competição:** EUA (`usa-1`), depois de o Guilherme responder as decisões de escopo (MLS só ou também NASL e ASL;
   campeão da MLS Cup com a Supporters' Shield na observação).

## 24/11/2026 — EUA (usa-1): escopo

Pesquisado e decidido em 24/11 (o Guilherme pediu "pesquise a fundo e veja o que é mais pertinente"). A 1ª divisão é a
"Division I" da lista da RSSSF (`usachamp.html`): ASL I (1921/22-1932/33, só tabelas), 1967 com duas edições (United Soccer
Association e NPSL), NASL 1968-1984 (tabelas e playoffs; campeão = playoffs) e MLS 1996-2025 (campeão = MLS Cup; Supporters'
Shield na observação). Sem edição de 1985 a 1995. MLS 2026 depois da final de 18/12/2026. Clubes canadenses com país `CAN`
(país novo: Canadá). Detalhes em `coleta/comum-concacaf/COMECE-AQUI.md`, seção 6.

## Recado de fim de coleta — usa-1 — 24/11/2026

Para o agente 1 (banco e painel) e para o agente de revisão.

1. **O que foi feito:** Campeonato Norte-Americano (`usa-1`, 1ª divisão dos EUA), 63 edições, uma por título, como a lista
   "Division I" da RSSSF: ASL I (14 edições, 1921/22-1932/33), as duas ligas de 1967 (United Soccer Association e NPSL),
   NASL (17, 1968-1984) e MLS (30, 1996-2025). 8.708 jogos (todos da MLS), 134 clubes (13 do Canadá), 24.858 gols (21.918
   com autor, 88%), 30.061 cartões. Fontes: RSSSF (`usachamp.html`, `asli.html`, `nasl.html`, páginas da MLS) e ESPN
   (`usa.1`, 2002 em diante). Campeão e vice batem com a lista da RSSSF em todas as edições.
2. **Commits:** `5bace06` (24/11). Sem push.
3. **Teste de carga:** `usa-1: 63 edições, 8708 jogos, 134 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar `data/coleta/usa-1/pacote/`;
   - **países novos: Estados Unidos (`USA`) e Canadá (`CAN`)**, em `paises.csv`; os dois já foram à Copa, mas conferir as
     bandeiras no painel;
   - 35 edições sem jogos (ASL, 1967, NASL, MLS 1997 e 1998): só a tabela, com campeão e vice; nas edições com divisões ou
     conferências, a classificação junta as tabelas e ordena por pontos;
   - pontuação fora do padrão na NPSL (1967), na NASL e na MLS de 1996-1999 (ponto por gol, shootout): a classificação é a
     tabela publicada, com `ajuste_pontos` vazio; a observação da edição explica;
   - duas edições em 1967 ("1967 USA" e "1967 NPSL"); de 1985 a 1995 não há edição (o país não teve 1ª divisão).
5. **Decisões** (24/11, depois de pesquisa, a pedido do Guilherme): o escopo acima; campeão da MLS = MLS Cup, com a
   Supporters' Shield como a melhor campanha na classificação; renomeação na mesma cidade é o mesmo clube (MetroStars = New
   York Red Bulls, Kansas City Wizards = Sporting KC, Dallas Burn = FC Dallas, San Jose Clash = Earthquakes, Montreal Impact =
   CF Montréal); mudança de cidade é outro clube; os clubes da NASL com nome de clube da MLS levam "(NASL)" (Seattle
   Sounders, Portland Timbers, Vancouver Whitecaps, San Jose Earthquakes); Philadelphia Field Club de 1921/22 = Bethlehem
   Steel (a RSSSF diz que o nome mudou); os dois New York Giants da ASL ficam com o último nome de cada um ("New York Soccer
   Club" e "New York Giants").
6. **O que não deu para coletar:** jogos da ASL I, de 1967 e da NASL (fonte: os livros de Colin Jose ou jornais da época); da
   MLS de 1997 e 1998 (fonte: arquivos da MLS); um DC United x New York Red Bulls de 2004. A MLS 2026 entra depois da final
   (18/12/2026).
7. **Onde a revisão deve olhar primeiro:** as identidades do item 5; a classificação das edições só com tabelas (divisões
   juntas por pontos; anos de dois turnos da ASL ficam com o turno de mais jogos); 2020 (pandemia e torneio MLS is Back).
8. **Próxima competição:** Costa Rica (`crc-1`), com as decisões de escopo ao Guilherme antes.

## 24/11/2026 — Costa Rica (crc-1): escopo

Decidido em 24/11 (pesquisa do agente; o Guilherme mandou seguir): a contagem oficial da UNAFUT, igual à lista da RSSSF
(`coschamp.html`, 123 títulos até o Clausura 2026). 1921 a 2006/07, um por ano (sem 1954 e 1956, não disputados); 1961 com
duas edições (Asofútbol e Federación); Apertura e Clausura de 2007/08 em diante. Sem país novo (CRC).

## Recado de fim de coleta — crc-1 — 24/11/2026

Para o agente 1 (banco e painel) e para o agente de revisão.

1. **O que foi feito:** Campeonato Costarriquenho (`crc-1`), 123 edições, uma por título, como a contagem oficial da UNAFUT
   (lista da RSSSF `coschamp.html`): 1921 a 1985 (sem 1954 e 1956, não disputados; 1961 com duas edições, Asofútbol e
   Federación), 1986/87 a 2006/07 (Apertura e Clausura como fases do ano a partir de 1997/98) e Apertura e Clausura de
   2007/08 até o Clausura 2026. 7.065 jogos (1996/97 em diante), 65 clubes, 19.008 gols (2.813 com autor), sem cartões.
   Fontes: RSSSF e ESPN (`crc.1`, só gols). Campeão e vice batem com a lista oficial em todas as edições.
2. **Commits:** `17766bf` (24/11). Sem push.
3. **Teste de carga:** `crc-1: 123 edições, 7065 jogos, 65 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar `data/coleta/crc-1/pacote/`;
   - **país novo: Costa Rica (`CRC`)**, em `paises.csv`; já foi à Copa, conferir a bandeira;
   - edições sem jogos de 1921 a 1995/96 (só a tabela, com campeão e vice) e 1991/92 e 1993/94 sem nada além de campeão e
     vice; quatro edições com jogos incompletos (Apertura 2010, Clausura 2011, Apertura 2011 e Clausura 2012: tabela e fase final);
   - duas edições em 1961 ("1961 Asofútbol" e "1961 Federación").
5. **Decisões** (24/11, do agente, com o ok do Guilherme para seguir): o escopo acima; Carmen FC = Carmelita; Liberia Mía =
   Municipal Liberia; Municipal Puntarenas e Puntarenas FC separados (como na lista de campeões); homônimos com a cidade
   (Santos de Guápiles, Sporting de San José, Uruguay de Coronado, Progreso de San José, Paraíso de Cartago); a ESPN de
   2010/11 e 2011/12 não foi usada (jogos adiados repetidos e faltando).
6. **O que não deu para coletar:** jogos de 1921 a 1995/96 (fonte: jornais da época ou a UNAFUT); 1991/92 e 1993/94 (sem
   página); a fase regular de 2010/11 e de 2011/12; autores dos gols e cartões (a RSSSF quase não tem; a ESPN só traz
   gols, em poucos anos).
7. **Onde a revisão deve olhar primeiro:** 1998/99, 2000/01, 2002/03 e 2003/04 (divergências explicadas no relatório); as
   identidades do item 5; a classificação das edições só com tabela.
8. **Próxima competição:** Honduras (`hon-1`), com o escopo antes (era amadora de 1947-1964 em discussão).

## 24/11/2026 — resposta ao agente 1: usa-1, classificação de 2004

Corrigido no commit `bb8432b`. Em 2004 a tabela do Leste diverge dos jogos (falta um DC United x New York Red Bulls na
ESPN) e a junção das conferências só usava as tabelas que fecham; agora, quando elas não cobrem todos os clubes, entram
todas as tabelas da fase regular. DC United em 1º e Sporting Kansas City em 2º. A mesma conferência mostrou que em 1928/29,
1931 e 1932/33 (ASL, dois turnos) faltavam os clubes de um turno só; entraram depois dos outros. Nas 63 edições, o 1º é o
campeão e o 2º é o vice; teste de carga OK. É só recarregar o pacote.

## 24/11/2026 — Honduras (hon-1): escopo

Só a Liga Nacional (1965/66 em diante), como a liga conta. A Liga Amateur de Honduras (1947-1964) fica fora: era um
mata-mata entre campeões regionais, a RSSSF a lista à parte, a FENAFUTH não reconhece os títulos e quase não há dados.

## Recado de fim de coleta — hon-1 — 24/11/2026

Para o agente 1 (banco e painel) e para o agente de revisão.

1. **O que foi feito:** Campeonato Hondurenho (`hon-1`, Liga Nacional), 89 edições, uma por título, como a lista da RSSSF
   (`hondchamp.html`): um campeão por temporada de 1965/66 a 1996/97, Apertura e Clausura de 1997/98 ao Clausura 2026 e o
   torneio único de 1999; duas sem campeão (1972/73, abandonada, e Clausura 2020, pandemia). 5.391 jogos (1996/97 em
   diante), 55 clubes, 13.983 gols (2.529 com autor), sem cartões. Fontes: RSSSF e ESPN (`hon.1`, para hora, estádio e
   público). Campeão e vice batem com a lista em todas as edições; o 1º da classificação é sempre o campeão.
2. **Commits:** nenhum ainda (espera o ok do Guilherme).
3. **Teste de carga:** `hon-1: 89 edições, 5391 jogos, 55 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar `data/coleta/hon-1/pacote/`;
   - **país novo: Honduras (`HON`)**, em `paises.csv`; já foi à Copa, conferir a bandeira;
   - 35 edições só com a tabela (1965/66 a 1995/96 e Apertura 2010 a Clausura 2012), com campeão e vice;
   - duas edições sem campeão (1972/73 e 2020 Clausura), com a tabela do momento.
5. **Decisões:** escopo só com a Liga Nacional (24/11, depois de pesquisa a pedido do Guilherme: a Liga Amateur de
   1947-1964 era um mata-mata entre campeões regionais, a RSSSF a lista à parte e a liga não a reconhece); La Salle = San
   Pedro; Honduras = Honduras Progreso; Atlético Olanchano e Olancho FC separados; homônimos com a cidade ou o país (Olimpia
   de Tegucigalpa, Necaxa de Tegucigalpa, Real Sociedad de Tocoa, Platense de Puerto Cortés, San Pedro de Honduras,
   Atlántida de La Ceiba, Palestino de Honduras, Independiente de Honduras, Progreso de Honduras, Atlético Español de
   Honduras); a ESPN de 2010/11 e 2011/12 não completa a fase regular (faltam de 5 a 11 jogos por torneio) e não foi usada
   para isso.
6. **O que não deu para coletar:** jogos de 1965/66 a 1995/96 (fonte: jornais da época ou a Liga Nacional); a fase regular de
   2010/11 e 2011/12; autores dos gols e cartões na maior parte dos anos (a RSSSF quase não traz; a ESPN não traz lances).
7. **Onde a revisão deve olhar primeiro:** 1997 Apertura, 2002 Apertura, 2002 Clausura, 2005 Apertura e 2007 Clausura (um
   resultado diferente entre a página e a tabela dela); os jogos anulados e repetidos de 2002 Apertura e 2007 Clausura.
8. **Próxima competição:** Guatemala (`gua-1`), com o escopo antes.
