# Pedidos da coleta África

Recados do agente de coleta da África (países da CAF) para o agente 1 (banco e painel) e para o agente de revisão, e as
respostas deles. Guia do agente: `coleta/comum-africa/COMECE-AQUI.md`.

Cada competição terminada ganha, no fim deste arquivo, uma seção "Recado de fim de coleta — <slug> — <data>" com os 8
itens da seção 10 de `docs/agentes-internacionais-COMECE-AQUI.md`.

## Recado de fim de coleta — egy-1 — 23/11/2026

Para o agente 1 (banco e painel) e o agente de revisão.

1. **O que foi feito:** `egy-1` (Campeonato Egípcio, Egyptian Premier League), 73 edições de 1948/49 a 2025/26; 11.574
   jogos (6.408 da RSSSF, 5.166 do ogol; 11 decididos fora de campo, 1 interrompido); 24.475 gols, 3.068 com autor (13%:
   a RSSSF só traz autores de 1998/99 a 2006/07); 0 cartões; 74 clubes, todos novos; artilheiros de 58 edições
   (Wikipédia). Fontes: RSSSF (páginas por temporada), ogol (calendários de 1964/65 em diante), Wikipédia em inglês (lista
   de campeões e de artilheiros, tabela de cada temporada). A ESPN não tem a liga egípcia.
2. **Commits:** 06635c8 (23/11; sem push).
3. **Teste de carga:** `egy-1: 73 edições, 11574 jogos, 74 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar o `egy-1`; país novo **EGY (Egito, CAF)**, criado pelo `competicao.json` (o Egito foi às Copas de 1934, 1990 e
     2018; conferir se a bandeira já existe);
   - **6 edições sem campeão** (temporadas não terminadas: 1954/55, 1971/72, 1973/74, 1989/90, 2011/12, 2012/13), com
     `formato` "temporada não terminada" e o motivo na observação; 1954/55, 1971/72 e 1973/74 não têm jogos nem tabela;
   - **10 edições "sem jogos (só a tabela final)"** (1949/50 a 1961/62) e **5 com "jogos incompletos"** (1948/49, 1957/58,
     1962/63, 1963/64, 1975/76: a tabela e só a final ou o desempate do título);
   - pontos por vitória mudam: 2 até 1985/86, 3 de 1986/87 a 1989/90, 2 de 1990/91 a 1993/94, 3 desde 1994/95;
   - classificação com mais de uma tabela (1957/58, 1962/63, 1963/64, 1975/76, 2012/13, 2013/14, 2024/25, 2025/26): os do
     grupo do título (ou da final) primeiro, com os números dessa fase; em 1962/63 e 2013/14 as 4 primeiras linhas têm só os
     3 jogos do quadrangular final;
   - colunas vazias: `hora`, `cidade`, `publico`, cartões; `estadio` quase sempre vazio.
5. **Decisões tomadas:**
   - escopo: só a liga nacional (1948/49 em diante). O campeonato da U.I.S.S.E. (1913-1914) a federação não reconhece; a
     Liga do Cairo era regional (pesquisa pedida pelo Guilherme, registrada em `coleta/comum-africa/COMECE-AQUI.md`);
   - a temporada interrompida pela briga em Al-Ahly x Zamalek é a 1971/72 (jogo de 24/12/1971), e não a 1970/71 da RSSSF;
     a "2013" da RSSSF é a 2012/13;
   - divergência entre a tabela da RSSSF e os jogos: se a tabela da Wikipédia fecha com os jogos, a classificação usa os
     números dos jogos (erro de digitação da RSSSF, 8 edições); se confirma a RSSSF, o relatório aponta o jogo provável e
     nenhum placar é mudado;
   - jogos acrescentados à mão, com prova: Al-Ahly x Ismaily em 1990/91 (1-0) e 1993/94 (1-1), que faltam no ogol;
     Al-Masry 3-1 Al-Ahly (1/2/2012, Port Said), que o ogol marca como anulado e a tabela no abandono conta; os 9 jogos dos
     desempates de 1962/63 (tabela cruzada);
   - 2011/12: tirados 4 jogos 0-0 do ogol que nunca aconteceram (adiados) e o Zamalek x Ismaily interrompido fica sem valer;
   - nomes: hífen nos árabes; Al-Ahly puro; Al-Ittihad de Alexandria, Al-Ittihad de Suez, Al-Nasr do Cairo, El-Merreikh de
     Port Said; o mesmo clube com outro nome é um só (Farouk = Zamalek; Al-Assiouty = Pyramids; FC Masr = ZED; Future =
     Modern Sport; Ittihad Othman = Dina Farms; Al-Ma'aden = Goldy; Sawahel = Haras El-Hodoud; Itesalat = Telecom Egypt).
   - Nada espera o Guilherme nesta liga.
6. **O que não deu para coletar:**
   - jogos de 1948/49 a 1963/64 (nenhuma fonte pública; as listas "Results Ahly" da RSSSF, só com os jogos do Al-Ahly e
     sem mando, ficaram de fora). Fonte que resolveria: o site do Dr. Tarek Said (drtareksaid.net, arquivado);
   - autores dos gols de 2007/08 em diante e cartões (o ogol tem, jogo a jogo, na página de cada partida);
   - 1992/93: um El-Merreikh x El-Minya que só a tabela da RSSSF conta (derrota para os dois).
7. **Onde a revisão deve olhar primeiro:** 1974/75 (a RSSSF troca Plastic e Suez); 1965/66 (o "Suez Club" do ogol é o
   Ittihad Suez só nesse ano); 2011/12 (correções do ogol); 1977/78, 1979/80, 1980/81, 1991/92 (Damanhour 0-0 Zamalek do
   ogol; a RSSSF e a Wikipédia indicam 1-2) e 2010/11 (divergências de 1 gol sem decisão); identidade do "Sohag" (2000/01 e
   2001/02 entraram como um clube só) e do Al-Shourta de 1975/76 (entrou como Ittihad El-Shorta).
8. **Próxima competição:** `mar-1` (Marrocos), depois da decisão do Guilherme sobre a era colonial.

## Recado de fim de coleta — mar-1 — 24/11/2026

Para o agente 1 (banco e painel) e o agente de revisão.

1. **O que foi feito:** `mar-1` (Campeonato Marroquino, hoje Botola Pro), 110 edições de 1915/16 a 2025/26; 11.736 jogos
   (11.016 da RSSSF, 720 do ogol; 13 decididos fora de campo, 11 vitórias sem placar conhecido, 19 anulados, 3 interrompidos);
   25.105 gols, só 18 com autor (a RSSSF do Marrocos quase não traz autores); 0 cartões; 100 clubes, todos novos; artilheiros
   de 69 edições (Wikipédia). Fontes: RSSSF (páginas por temporada e tabelas de confrontos), ogol (2004/05 em diante),
   Wikipédia em inglês (lista de campeões com vice e artilheiro; tabela de cada temporada desde 2002/03). A ESPN não tem a
   liga marroquina.
2. **Commits:** nenhum ainda (esperando o ok do Guilherme).
3. **Teste de carga:** `mar-1: 110 edições, 11736 jogos, 100 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar o `mar-1`; país novo **MAR (Marrocos, CAF)**, criado pelo `competicao.json` (o Marrocos foi a várias Copas:
     conferir se a bandeira já existe);
   - **sistema de pontos 3-2-1** (vitória 3, empate 2, derrota 1) de 1933/34 a 1994/95; 3-1-0 desde 1995/96. O
     `edicoes.csv` só tem `pontos_vitoria` (3 nos dois casos): o sistema vai na `observacao` da edição, e o `ajuste_pontos` da
     classificação já usa o 3-2-1. Se o painel recalcula pontos por vitória e empate, vai errar nesses anos;
   - **40 edições "sem jogos"**: só o campeão (9 anos coloniais sem página), só o campeão e o vice (1970/71, 1973/74,
     1981/82), só a classificação incompleta (1915/16, 1949/50 a 1953/54, 1993/94; posição e às vezes jogos e pontos, com as
     colunas vazias) ou só a tabela final (a maioria de 1968/69 a 1994/95);
   - **14 edições com "jogos incompletos"** (era colonial: resultados conhecidos das ligas regionais e o mata-mata nacional);
   - jogos das tabelas de confrontos (1956/57 a 1967/68, 1980/81, 1989/90, 1990/91) **sem data e sem rodada**;
   - 1942/43 sem campeão (temporada não terminada); 1986/87: dois grupos e fase final (os 8 da fase final em cima).
5. **Decisões tomadas:**
   - escopo: entra a era colonial (1915/16 a 1954/55), porque a federação marroquina conta esses títulos (pesquisa pedida
     pelo Guilherme; o Guilherme aprovou em 24/11); fora a "Ligue libre" (liga paralela, 1946-1956) e 1955/56 (sem
     competição);
   - 1946/47: campeão USA Casablanca (página da temporada e Wikipédia); a lista de campeões da RSSSF põe a US Marocaine,
     3ª colocada (erro da lista);
   - 1959/60: os jogos do Hassania Agadir ficam anulados (desistiu depois do terremoto de Agadir; a tabela não os conta);
   - "A bt B" vira vitória sem placar (como no `ven-1`); "drw" (empate sem placar, 2 jogos de 1933/34) fica de fora;
   - nomes: Racing Casablanca = Racing AC = ADM Casablanca (como a RSSSF conta os títulos); US Casablanca = USA Casablanca;
     AS Salé = SA Salé = Sporting Salé; JS Massira = Forces Auxiliaires (mudou de Ben Slimane para El Ayoun, segundo a página
     de 1994/95); Olympique Casablanca (colonial) e Olympique de Casablanca (campeão de 1993/94) são clubes diferentes.
   - Nada espera o Guilherme nesta liga.
6. **O que não deu para coletar:**
   - jogos de 1968/69 a 1994/95 (fora 1980/81, 1989/90, 1990/91): a RSSSF só tem a tabela e o ogol só tem jogos de 2004/05
     em diante;
   - era colonial: 9 anos sem página e jogos incompletos nos outros. Fonte que resolveria: jornais da época (Le Petit
     Marocain, La Vigie Marocaine) na Gallica (BnF);
   - autores dos gols e cartões (o ogol tem, jogo a jogo, de 2004/05 em diante).
7. **Onde a revisão deve olhar primeiro:** as tabelas de confrontos (1956/57 a 1967/68, 1980/81, 1989/90): a ligação de
   cada linha da matriz ao clube é pela campanha, e vários resultados não batem com a tabela final da página (vitória e
   empate trocados com os mesmos gols); 1946/47 (campeão); 1959/60 (desempate e jogos anulados); 1999/00, 2003/04, 2008/09
   e 2010/11 (a Wikipédia confirma a tabela da RSSSF, e o relatório aponta o jogo provável); as fusões de clubes do item 5.
8. **Próxima competição:** `tun-1` (Tunísia), depois da decisão do Guilherme sobre a era colonial.
