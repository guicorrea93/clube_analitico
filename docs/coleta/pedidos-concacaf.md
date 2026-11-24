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
2. **Commits:** o deste recado (24/11; o hash vai na seção seguinte). Sem push.
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
