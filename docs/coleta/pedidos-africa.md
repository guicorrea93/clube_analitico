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
2. **Commits:** 820bf5f (24/11; sem push).
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

## Recado de fim de coleta — tun-1 — 24/11/2026

Para o agente 1 (banco e painel) e o agente de revisão.

1. **O que foi feito:** `tun-1` (Campeonato Tunisiano, hoje Ligue Professionnelle 1), 109 edições de 1907 a 2025/26;
   8.092 jogos (7.852 da RSSSF, 240 do ogol; 39 decididos fora de campo com placar, 7 vitórias sem placar conhecido ou W.O.,
   5 abandonados, 1 não jogado); 17.062 gols, 771 com autor (quase só 2004/05 e 2010/11); 0 cartões; 74 clubes, todos novos;
   artilheiros de 71 edições (Wikipédia). Fontes: RSSSF (páginas por temporada, tabelas de confrontos e a lista de tabelas
   finais `tunhist.html`), ogol (base de 2025/26; conferência, rodada e data desde 2005/06), Wikipédia em inglês (listas de
   campeões e artilheiros, tabela e notas de cada temporada). A ESPN não tem a liga tunisiana.
2. **Commits:** 786998d (24/11; sem push; junto, o `edicoes.csv` do `mar-1` com os pontos por empate e derrota).
3. **Teste de carga:** `tun-1: 109 edições, 8092 jogos, 74 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar o `tun-1`; país novo **TUN (Tunísia, CAF)**, criado pelo `competicao.json` (a Tunísia foi a várias Copas:
     conferir se a bandeira já existe);
   - **quatro sistemas de pontos:** 3-2-1 (vitória, empate, derrota) até 1985/86, 4-2-1 de 1986/87 a 1991/92, 2-1-0 de
     1992/93 a 1994/95, 3-1-0 desde 1995/96, nas colunas `pontos_vitoria`, `pontos_empate` e `pontos_derrota` do
     `edicoes.csv` (recado do agente 1 de 24/11; vazias = 1 e 0). O mesmo commit preenche o `mar-1` (3-2-1 até 1994/95;
     só o `edicoes.csv` muda);
   - **55 edições "sem jogos"**: só o campeão (28: era colonial sem página e anos sem jogos na RSSSF) ou só a tabela final
     (27, de 1955/56 a 1995/96 fora os anos da tabela de confrontos);
   - **9 edições com "jogos incompletos"** (era colonial: só a final ou o mata-mata; 1949/50, só os resultados conhecidos);
   - jogos das tabelas de confrontos (1968/69, 1970/71, 1977/78, 1980/81, 1982/83, 1987/88 a 1995/96) **sem data e sem
     rodada**;
   - 1951/52 sem campeão (abandonado em janeiro de 1952; a tabela é a do abandono);
   - anos com 1ª fase em dois grupos e fase final (1998/99, 2012/13, 2016/17, 2021/22 a 2023/24): a fase final dá as
     primeiras posições; em 2012/13 e 2021/22 os jogos de classificação ("Seventh Place Match"...) dão a ordem do meio.
5. **Decisões tomadas:**
   - escopo: entra a era colonial, desde 1907 (USFSA até 1920/21, Liga da Tunísia de 1921/22 a 1954/55), porque a contagem
     oficial usada na Tunísia inclui esses títulos (o "34º título" do Espérance em 2024/25 e o "14º" do Club Africain em
     2025/26 só fecham com eles); o Guilherme autorizou decidir pela pesquisa (24/11). Fora os anos sem competição (1909/10,
     guerras mundiais, 1942/43, 1943/44);
   - 1909/10: a Wikipédia dá um título ao Racing Club de Tunis; a RSSSF diz que não houve campeonato: fica de fora;
   - resultados dados fora de campo com o placar oficial e o de campo na observação: 2006/07 (CS Hammam-Lif 2-0 US
     Monastir, jogador irregular) e três em 2025/26 (notas da Wikipédia; um deles, US Monastir x CS Sfaxien, o ogol traz sem
     placar, "DA"); células "awd" das tabelas de confrontos (4 jogos) entram como W.O., pela nota da página;
   - rebaixamentos fora da tabela: 2012/13 (ES Zarzis, jogo de 13º lugar), 2019/20 (CS Hammam-Lif nos "Barrages"; CS Chebba
     excluído), 2021/22 (o CAS manteve o CS Chebba; caíram ES Zarzis e CS Hammam-Lif no desempate do 16º lugar), 2023/24 (AS
     Marsa, desempate do rebaixamento);
   - nomes: Railway Sports de Sfax (colonial) = Sfax Railways Sports; US Ferryville = USM Bourguiba; Olympique Tunis = US
     Musulmane Olympique (mudou de nome em 1957); "ES" de 1949/50 = Espérance de Tunis.
   - Nada espera o Guilherme nesta liga.
6. **O que não deu para coletar:**
   - jogos de 1955/56 a 1995/96 fora os anos da tabela de confrontos: a RSSSF só tem a tabela e o ogol só tem jogos de
     2005/06 em diante;
   - era colonial: só 9 anos com jogos (a final ou o mata-mata). Fonte que resolveria: jornais da época (La Dépêche
     tunisienne, Le Petit Matin) na Gallica (BnF);
   - autores dos gols e cartões (o ogol tem, jogo a jogo, de 2005/06 em diante).
7. **Onde a revisão deve olhar primeiro:** as tabelas de confrontos que não fecham com a tabela final da página (um par de
   jogos em 1968/69, 1977/78, 1980/81, 1982/83, 1987/88 a 1990/91 e 1993/94; 1994/95 em 13 dos 14 clubes, erro da própria
   página); a ordem final de 2012/13 e 2021/22 (`ORDEM_FINAL`) e os rebaixamentos do item 5 (`SITUACAO_FIXA`); a ligação
   das linhas das matrizes com nomes aos clubes.
8. **Próxima competição:** `alg-1` (Argélia), depois da decisão do Guilherme sobre o escopo (era colonial).

## Recado de fim de coleta — alg-1 — 24/11/2026

Para o agente 1 (banco e painel) e o agente de revisão.

1. **O que foi feito:** `alg-1` (Campeonato Argelino, hoje Ligue Professionnelle 1), 64 edições de 1962/63 a 2025/26;
   15.210 jogos, todos da RSSSF (110 decididos fora de campo, 7 não jogados, 5 abandonados); 33.855 gols, 3.829 com autor
   (quase só de 1997/98 a 2005/06); 0 cartões; 81 clubes, todos novos; artilheiros de 58 edições (Wikipédia). Fontes:
   RSSSF (página de cada temporada), ogol (1985/86 em diante: data, rodada e conferência; repete os placares da RSSSF),
   Wikipédia em inglês (lista de campeões com vice e artilheiro; tabela de toda temporada). A ESPN não tem a liga argelina.
2. **Commits:** b09bbaa (24/11; sem push).
3. **Teste de carga:** `alg-1: 64 edições, 15210 jogos, 81 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar o `alg-1`; país novo **ALG (Argélia, CAF)**, criado pelo `competicao.json` (a Argélia foi a várias Copas:
     conferir se a bandeira já existe);
   - **três sistemas de pontos**, nas colunas `pontos_vitoria`, `pontos_empate` e `pontos_derrota` do `edicoes.csv`:
     3-2-1 (vitória, empate, derrota) até 1985/86, 2-1-0 de 1986/87 a 1994/95, 3-1-0 desde 1995/96;
   - **1962/63 e 1963/64 com "jogos incompletos"** (ligas regionais de Argel, Orã e Constantine e a fase final); os quatro
     primeiros vêm da fase final;
   - **2019/20 "temporada interrompida (Covid-19)"**: campeão CR Belouizdad (declarado pela federação), sem rebaixamento;
   - 1997/98 e 1998/99: dois grupos e final (o campeão e o vice em cima, os outros pela posição no grupo).
5. **Decisões tomadas:**
   - escopo: só desde a independência (1962/63), como a RSSSF ("64 títulos; desde a independência"), a Wikipédia e a
     contagem dos clubes; a era colonial fica de fora (só ligas regionais; o Guilherme aprovou em 24/11);
   - nomes: o nome atual com a sigla francesa; os da reforma esportiva de 1977 a 1989 e os antigos são o mesmo clube (MP
     Alger = MC Alger; JE Tizi Ouzou e JS Kawkabi = JS Kabylie; EP Sétif e WR Sétif = ES Sétif; CM Belcourt = CR Belouizdad;
     NAR Alger e RS Kouba = RC Kouba; ASTO El Asnam, DNC Asnam, Chlef SO e AS Orléansville = ASO Chlef...); o USM Annaba
     até 1979 é o Hamra Annaba (o atual USM Annaba é de 1983); DNC Alger = OC Alger = JH Djazaïr;
   - placar só muda com outra fonte: dois jogos de 2025/26 pelo ogol (as tabelas da RSSSF e da Wikipédia só fecham com
     eles); cópias de rodada descartadas (1972/73) ou com os jogos verdadeiros faltando (1974/75 rodada 4, 1975/76
     rodada 18); "US Constantine" de 1996/97 = US Chaouia (erro de digitação);
   - 1997/98: ninguém caiu (a liga passou a dois grupos de 14), apesar dos desempates de rebaixamento.
   - Nada espera o Guilherme nesta liga.
6. **O que não deu para coletar:**
   - placares certos dos jogos que não fecham com a tabela de 1964/65 a 1998/99 (a lista de jogos da RSSSF erra em vários
     clubes por ano; o ogol copia a RSSSF). Fonte que resolveria: jornais argelinos da época (El Moudjahid) ou o arquivo
     da federação;
   - os jogos verdadeiros das rodadas copiadas (1974/75, 1975/76) e a 1ª fase regional de 1962/63;
   - autores dos gols fora de 1997/98 a 2005/06, e cartões.
7. **Onde a revisão deve olhar primeiro:** as divergências jogo x tabela de 1964/65 a 1998/99 (jogo provável no
   relatório `docs/coleta/alg-1.md`); os pares com o mando provavelmente trocado (o mesmo mandante x visitante duas vezes
   na temporada); a identidade dos clubes da reforma de 1977 (DNC Alger, WKF Collo, USM Aïn Beïda/ISM); 2009/10 (CA Bordj
   Bou Arréridj x MC Alger, "derrota para os dois", sem placar).
8. **Próxima competição:** `rsa-1` (África do Sul), depois da decisão do Guilherme sobre o escopo (NFL, NPSL, NSL, PSL e
   as ligas paralelas do apartheid).

## Recado de fim de coleta — rsa-1 — 24/11/2026

Para o agente 1 (banco e painel) e o agente de revisão.

1. **O que foi feito:** `rsa-1` (Campeonato Sul-Africano: NPSL, NSL e Premier Soccer League), 55 edições de 1971 a
   2025/26; 8.108 jogos (7.868 da RSSSF, 240 do ogol; 8 decididos fora de campo, 31 não jogados ou anulados, 20
   abandonados); 18.432 gols, 4.721 com autor (sobretudo de 2002/03 a 2013/14); 0 cartões; 89 clubes, todos novos.
   Fontes: RSSSF (página de cada ano), ogol (jogos de 2005/06 em diante: base de 2025/26; data, rodada e conferência nos
   outros), Wikipédia em inglês (tabela de 48 temporadas). A ESPN não tem a liga.
2. **Commits:** b755594 (24/11; sem push).
3. **Teste de carga:** `rsa-1: 55 edições, 8108 jogos, 89 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar o `rsa-1`; país novo **RSA (África do Sul, CAF)**, criado pelo `competicao.json` (a África do Sul foi a
     várias Copas e sediou a de 2010: conferir se a bandeira já existe);
   - **temporadas no ano civil até 1995** ("1971" ... "1995") e no formato "1996/97" depois;
   - **dois sistemas de pontos**: 2-1-0 (vitória, empate, derrota) até 1994 e 3-1-0 desde 1995 (o `edicoes.csv` já diz;
     empate 1 e derrota 0 nos dois, então as colunas novas ficam vazias);
   - **22 edições "sem jogos"**: só a tabela final (18, de 1971 a 1995) ou só o campeão (1972, 1973, 1975 e 1977);
   - **4 edições com "jogos incompletos"** (1987, 1992, 1993 e 1996/97: só os jogos que a página traz);
   - 2024/25: o Royal AM foi excluído e os resultados dele anulados.
5. **Decisões tomadas:**
   - escopo: a linha NPSL (1971-1984), NSL (1985-1995) e PSL (desde 1996/97), como a RSSSF e a imprensa contam; fora as
     ligas separadas por raça do apartheid (NFL dos brancos, SASL/FPL), a NPSL paralela depois de 1985 e o torneio de
     transição de 1996 (o Guilherme aprovou em 24/11);
   - nomes: nome que já existe em outro país leva "(África do Sul)" (Santos, Rangers, Dynamos, Leeds United, Leicester
     City, Colchester United, Vasco da Gama); clube refundado com nome de um antigo leva o ano do antigo (Durban City
     (1959), Cape Town City (1962), Highlands Park (1959)); mesmo clube com outro nome é um só (Zulu Royals = AmaZulu;
     Pretoria City e Albany City = SuperSport United; Qwa Qwa Stars e Score Stars = Free State Stars; Ajax Cape Town =
     Cape Town Spurs; Silver Stars = Platinum Stars; Witbank Aces = Mpumalanga Black Aces; Benoni Premier United = Thanda
     Royal Zulu); clube que comprou a vaga de outro (Marumo Gallants, Royal AM, TS Galaxy, Siwelele) é um clube próprio;
   - quatro linhas de tabela com vitórias + empates + derrotas que não davam os jogos (1982, 1986, 1993) corrigidas pelos
     pontos; 2001/02 Ajax Cape Town x Orlando Pirates: 1-0 dado ao Ajax (nota da página);
   - rebaixamento pelos desempates de acesso marcado à mão (o 15º que perdeu o desempate, de 2004/05 a 2025/26); venda de
     vaga não é rebaixamento.
   - Nada espera o Guilherme nesta liga.
6. **O que não deu para coletar:**
   - os jogos de 1971 a 1995 (a RSSSF só tem a tabela, fora parte de 1987, 1992 e 1993) e parte de 1996/97; o ogol só tem
     jogos de 2005/06 em diante. Fonte que resolveria: jornais sul-africanos (The World, Sowetan, Rand Daily Mail) ou o
     arquivo da PSL;
   - a tabela da NPSL de 1972, 1973, 1975 e 1977 (só o campeão);
   - autores dos gols fora de 2002/03 a 2013/14, artilheiros de quase todas as temporadas e cartões.
7. **Onde a revisão deve olhar primeiro:** a identidade dos clubes (vendas de vaga, fusões e trocas de nome no meio da
   temporada: 1993, 2007/08); os rebaixamentos marcados à mão; 1999/00 (a lista de jogos não fecha com a tabela em seis
   clubes; a Wikipédia confirma a tabela).
8. **Próxima competição:** `nga-1` (Nigéria), depois da decisão do Guilherme sobre o escopo.

## Recado de fim de coleta — nga-1 — 24/11/2026

Para o agente 1 (banco e painel) e o agente de revisão.

1. **O que foi feito:** `nga-1` (Campeonato Nigeriano, hoje Nigeria Premier Football League), 55 edições de 1972 a
   2025/26; 8.906 jogos (7.766 da RSSSF, 1.140 do ogol; 51 decididos fora de campo, 10 W.O., 32 não jogados ou anulados,
   30 abandonados); 17.820 gols, só 73 com autor; 0 cartões; 82 clubes, todos novos. Fontes: RSSSF (página de cada ano),
   ogol (jogos de 2008/09 em diante: base de 2009/10 a 2011/12; data, rodada e conferência nos outros), Wikipédia em
   inglês (tabela das temporadas desde 2009/10). A ESPN não tem a liga.
2. **Commits:** bc5287a6 (24/11; no GitHub).
3. **Teste de carga:** `nga-1: 55 edições, 8906 jogos, 82 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar o `nga-1`; país novo **NGA (Nigéria, CAF)**, criado pelo `competicao.json` (a Nigéria foi a várias Copas:
     conferir se a bandeira já existe);
   - **temporadas que mudam de formato**: ano civil até 2007, 2007/08 a 2011/12, ano civil de 2013 a 2019, 2019/20 a
     2021/22, 2023 e 2023/24 em diante;
   - **pontos**: 2-1-0 (vitória, empate, derrota) até 1989; de 1990 a 1994, 3 por vitória, 2 por empate com gols e 1 por
     empate sem gols (o `edicoes.csv` dá 3-1-0 e o ponto a mais vai no `ajuste_pontos`); 3-1-0 desde 1995;
   - **26 edições "sem jogos"**: só o campeão (17: 1973 a 1988 e 1990) ou só a tabela final (9: 1972, 1989, 1991 a 1997);
   - **2 temporadas abandonadas sem campeão** (2018 e 2019/20) e **7 com "jogos incompletos"** (1998 a 2003 e 2007/08);
   - 2006, 2007, 2019 e 2023: dois grupos e fase final (a fase final dá as primeiras posições);
   - 2016: o Giwa FC foi expulso e os resultados dele anulados.
5. **Decisões tomadas:**
   - escopo: a liga nacional desde 1972, como a liga e a imprensa contam (o título de 2025/26 foi o "9º" do Enugu Rangers);
     fora a Amachree Gold Cup de 1971, que a RSSSF conta (o Guilherme aprovou em 24/11);
   - nomes: Enugu Rangers = Rangers International; Heartland = Iwuanyanwu Nationale; Dolphin = Eagle Cement; Shooting
     Stars = IICC = 3SC; Ifeanyi Ubah = Gabros International; ABS = Bukola Babes; Nigerian Ports Authority = NPA; NITEL
     Vasco = P&T Vasco da Gama; o Rivers United (fusão de Dolphin e Sharks em 2016) é um clube próprio;
   - correções: quatro linhas de tabela com vitórias + empates + derrotas que não davam os jogos (1992, 1994, 1996,
     2002), pelos pontos; 2005: a rodada 20 de julho anulada (jogada de novo em novembro) e um 0-2 dado e depois revogado;
     2006: um 0-3 dado (o leitor tinha lido "n/p"); 2023/24: um jogo válido que o leitor marcava como anulado (nota de
     outro jogo);
   - rebaixamento marcado onde a página diz (tabela ou nota: 1993, 1996).
   - Nada espera o Guilherme nesta liga.
6. **O que não deu para coletar:**
   - os jogos de 1972 a 1997 (a RSSSF só tem a tabela ou o campeão; sem páginas de 1980 a 1982) e parte dos de 1998 a
     2003, 2007/08 e 2019/20; o ogol só tem jogos de 2008/09 em diante. Fonte que resolveria: jornais nigerianos (Daily
     Times, The Guardian, Complete Sports) ou o arquivo da NPFL;
   - autores dos gols, artilheiros e cartões.
7. **Onde a revisão deve olhar primeiro:** 2009/10 a 2011/12 (os jogos do ogol não fecham com a tabela da RSSSF em vários
   clubes); as punições de pontos e gols (2023/24, 2024/25, 2025/26); a identidade dos clubes do item 5.
8. **Próxima competição:** `gha-1` (Gana), depois da decisão do Guilherme sobre o escopo.

## Recado de fim de coleta — gha-1 — 24/11/2026

Para o agente 1 (banco e painel) e o agente de revisão.

1. **O que foi feito:** `gha-1` (Campeonato Ganês, hoje Ghana Premier League), 65 edições de 1958 a 2025/26; 6.069 jogos
   (5.828 da RSSSF, 241 do ogol; 54 decididos fora de campo, 7 W.O., 17 abandonados, 6 não jogados); 12.631 gols, 294 com
   autor; 0 cartões; 137 clubes, todos novos. Fontes: RSSSF (lista de tabelas finais de 1958 a 1987 e página de cada
   ano), ogol (jogos de 2008/09 a 2010/11 e de 2015 em diante: base de 2010/11; data, rodada e conferência nos outros),
   Wikipédia em inglês (tabela de 16 temporadas). A ESPN não tem a liga.
2. **Commits:** cd02564c (25/11; sem push).
3. **Teste de carga:** `gha-1: 65 edições, 6069 jogos, 137 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar o `gha-1`; país novo **GHA (Gana, CAF)**, criado pelo `competicao.json` (Gana foi a várias Copas: conferir
     se a bandeira já existe);
   - **temporadas que mudam de formato** (ano civil, duas temporadas, de novo ano civil), como a lista da RSSSF;
   - **pontos**: 2-1-0 (vitória, empate, derrota) até 1993/94, fora 1989/90 (3 por vitória); 3-1-0 desde 1994/95;
   - **39 edições "sem jogos"**: só a tabela final (37: 1958 a 1987, 1990/91 a 1996/97 e 2011/12), só o campeão
     (1988/89) ou só a classificação incompleta (1989/90);
   - **2 temporadas abandonadas sem campeão** (2018 e 2019/20) e **2 com "jogos incompletos"** (1997/98 e 2006/07);
   - 2004/05: dois grupos e o jogo do título (Hearts of Oak 1-0 Asante Kotoko).
5. **Decisões tomadas:**
   - escopo: a liga nacional de 1958 a 2025/26, sem o campeonato não oficial de 1956 e sem a competição especial do
     Comitê de Normalização de 2019 (não foi liga; a RSSSF conta, a imprensa não) (o Guilherme aprovou em 24/11);
   - nomes: Ashanti Gold = Goldfields; Ebusua Dwarfs = Mysterious Dwarfs; Real Tamale United = RTU; Swedru All Blacks =
     Gamba All Blacks; Tano Bofoakwa = Bofoakwa; nomes que já existem em outros pacotes levam "(Gana)" (Mighty Jets,
     Highlanders, Aston Villa); os de Berekum levam a cidade (Berekum Arsenal, Berekum Chelsea);
   - correções: sete linhas de tabela com vitórias + empates + derrotas que não davam os jogos (1968 a 1981 e 2008/09),
     pelos pontos; 2003: os oito resultados dados que a tabela conta (a nota que os lista era lida como jogos); 2009/10:
     um jogo que falta na página, pelo ogol (a tabela só fecha com ele);
   - rebaixamento marcado onde a tabela ou a nota diz (2003 e 2004/05 à mão).
   - Nada espera o Guilherme nesta liga.
6. **O que não deu para coletar:**
   - os jogos de 1958 a 1996/97 (a RSSSF só tem a tabela) e parte dos de 1997/98 e 2006/07; 2011/12 a 2013/14 sem jogos no
     ogol (2011/12 fica só com a tabela). Fonte que resolveria: jornais ganeses (Daily Graphic) ou o arquivo da GFA;
   - a tabela de 1988/89 ("Final table missing") e a completa de 1989/90;
   - autores dos gols (quase nenhum), artilheiros e cartões.
7. **Onde a revisão deve olhar primeiro:** 2010/11 (os jogos do ogol não fecham com a tabela da RSSSF em sete clubes);
   2003 (resultados dados e descontos de pontos); a identidade dos clubes do item 5.
8. **Próxima competição:** `cmr-1` (Camarões), depois da decisão do Guilherme sobre o escopo.

## Recado de fim de coleta — cmr-1 — 25/11/2026

Para o agente 1 (banco e painel) e o agente de revisão.

1. **O que foi feito:** `cmr-1` (Campeonato Camaronês, hoje Elite One), 66 edições de 1961 a 2026; 6.804 jogos (6.679 da
   RSSSF, 125 do ogol; 62 decididos fora de campo, 11 W.O., 22 abandonados, 16 não jogados); 13.633 gols, 1.138 com autor
   (2004 e 2005); 0 cartões; 85 clubes, todos novos. Fontes: RSSSF (lista de campeões `kamchamp.html` e página de cada
   ano), ogol (jogos de 2005 em diante, fora 2013 a 2016: base de 2010/11; data, rodada e conferência nos outros),
   Wikipédia em inglês (tabela de 34 temporadas). A ESPN não tem a liga.
2. **Commits:** e7f2bfa8 (25/11; no GitHub).
3. **Teste de carga:** `cmr-1: 66 edições, 6804 jogos, 85 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar o `cmr-1`; país novo **CMR (Camarões, CAF)**, criado pelo `competicao.json` (Camarões foi a várias Copas:
     conferir se a bandeira já existe);
   - **temporadas que mudam de formato** (ano civil e duas temporadas se alternam), como a lista da RSSSF;
   - **pontos**: 2-1-0 (vitória, empate, derrota) até 1987/88 e de 1991 a 1994; 3-1-0 em 1988/89, 1989/90 e desde 1995;
   - **37 edições "sem jogos"**: só o campeão (21: 1961 a 1977/78, 1984/85, 1986/87 e 1992), só a classificação
     incompleta (8: 1978/79 a 1985/86, 1993 e 1996) ou só a tabela final (8: 1982/83, 1988/89 a 1991, 1994, 1995, 1997 e
     1998); **4 com "jogos incompletos"** (1987/88, 1999, 2000 e 2010/11);
   - 2019/20 abandonado (Covid-19) com o PWD Bamenda declarado campeão, sem rebaixamento; 2020/21 é a "Ligue 2021", da
     FECAFOOT (a liga da LFPC parou na 1ª rodada);
   - fases: 2004, 2019 e 2023/24 (grupos do título e do rebaixamento depois dos grupos), 2020/21 e 2022 (semifinais, 3º
     lugar e final), 2022/23 (fase final de quatro).
5. **Decisões tomadas:**
   - escopo: o campeonato nacional de 1961 a 2026, como a lista da RSSSF; "1960" e "1961" da lista são uma edição só
     ("1961"); fora o campeonato territorial da era colonial, as ligas do Camarões anglófono até 1972 e as copas (o
     Guilherme aprovou em 25/11);
   - nomes: os dois Aigle Royal são clubes diferentes (do Moungo, de Nkongsamba; da Menoua, de Dschang; "Aigle" sozinho
     até 2004 = Moungo, de 2005 a 2023 = Menoua); Djiko FC = Feutcheu FC ("Feutcheu FC were renamed Djiko FC"); nomes que
     já existem em outros pacotes levam "(Camarões)" (Botafogo, Santos);
   - correções: vitórias dadas sem gols ("awarded 0-0 win": 2009/10 e 2023/24) e resultados dados que a página marca
     "abd" ou "n/p" (2006 e 2007) entram como a tabela conta; 2000: a rodada 21 da página é cópia da 22 (descartada);
     2005: o 3-0 dado e depois revogado fica 1-2; 2024/25: um jogo válido anulado por nota da linha de cima; 2011/12 e
     2020/21: as datas de julho a outubro estavam no ano errado (as duas temporadas foram jogadas num ano só);
   - 2001: a classificação é a tabela oficial da FECAFOOT (a página traz também a dos resultados conhecidos);
   - rebaixamento à mão onde a nota diz: 2007 (Bamboutos, excluído), 2020/21 (ninguém caiu: a liga subiu para 25), 2022
     (Panthère, por manipulação, no lugar do Yaoundé II), 2022/23 (Eding Sport, no desempate) e 2026 (AS Fortuna, no
     desempate com a Elite Two).
   - Nada espera o Guilherme nesta liga.
6. **O que não deu para coletar:**
   - os jogos de 1961 a 1998 (a RSSSF só tem campeão, topo da tabela ou tabela) e parte dos de 1987/88, 1999 e 2000.
     Fonte que resolveria: jornais camaroneses (Cameroon Tribune) ou o arquivo da FECAFOOT;
   - 2010/11: os jogos do Union e do Caïman Douala (o ogol dá aos dois o mesmo nome e o mesmo id);
   - autores dos gols fora de 2004 e 2005, artilheiros (só desses dois anos) e cartões.
7. **Onde a revisão deve olhar primeiro:** 2001 (a tabela oficial não fecha com os jogos); 2000 (tabela "not checked with
   scores" e rodada copiada); 2014 (Douala AC x Coton Sport, derrota dada aos dois); 2015 (um placar entre Fovu e Canon);
   a identidade dos clubes do item 5.
8. **Próxima competição:** `civ-1` (Costa do Marfim), depois da decisão do Guilherme sobre o escopo.

## Recado de fim de coleta — tan-1 — 25/11/2026

Para o agente 1 (banco e painel) e o agente de revisão.

1. **O que foi feito:** `tan-1` (Campeonato Tanzaniano, hoje Ligi Kuu Tanzania Bara), 62 edições de 1965 a 2025/26;
   5.929 jogos (5.747 da RSSSF, 182 do ogol; 75 decididos fora de campo, 38 W.O., 14 abandonados, 56 não jogados ou
   anulados); 12.332 gols, 1.299 com autor; 0 cartões; 82 clubes, todos novos. Fontes: RSSSF (lista de campeões e
   página de cada ano), ogol (jogos de 2007/08 em diante: base de 2011/12; data, rodada e conferência nos outros),
   Wikipédia em inglês (tabela de 11 temporadas). A ESPN não tem a liga.
2. **Commit:** o deste recado (`Coleta Tanzânia (tan-1): 62 edições, 5.929 jogos`).
3. **Teste de carga:** `tan-1: 62 edições, 5929 jogos, 82 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar o `tan-1`; país novo **TAN (Tanzânia, CAF)**, criado pelo `competicao.json` (conferir a bandeira);
   - **temporadas**: ano civil até 2007, duas metades de 2007/08 em diante;
   - **pontos**: 2-1-0 (vitória, empate, derrota) até 1995; 3-1-0 desde 1995/96;
   - **32 edições "sem jogos"**: só o campeão (23: 1966 a 1982 e 1990 a 1995), só os primeiros colocados (3: 1965,
     1983, 1995/96) ou só a tabela final (6: 1985 a 1987, 1989, 1996/97, 1998); **8 com "jogos incompletos"** (1988 e
     2000 a 2006);
   - fases: 2000 a 2004 (grupos e fase final: "Super Eight", "Mainland Championship Playoff"); 2007 (mini-liga de
     transição: três grupos, o "Super Six" e a final, Simba x Young Africans nos pênaltis); desde 2021/22, o desempate
     do rebaixamento fora da tabela.
5. **Decisões tomadas:**
   - escopo: a liga do continente de 1965 a 2025/26, com o campeão do continente em todos os anos (a lista que a TFF e
     os clubes contam); fora a liga de Dar es Salaam (1921–1964), a "Union League" de 1982 a 2003 (com Zanzibar; é o
     campeão que a lista da RSSSF dá nesses anos), Zanzibar e as copas (o Guilherme aprovou em 25/11);
   - nomes: Simba = Sunderland; Young Africans = Yanga; Moro United = Kajumulo = Sigara (trocas registradas pela RSSSF);
     Kahama United = KJ82 Rangers; JKT Tanzania = JKT Ruvu; Tabora United = Kitayosce; Singida Fountain Gate = Singida
     Big Stars; o Singida Black Stars (ex-Ihefu, levado para Singida) é outro clube; os clubes do exército com número
     viram "KJ977 Meru Warriors", "KJ44 Karume Rangers";
   - correções: três linhas de tabela com vitórias + empates + derrotas que não davam os jogos (2001 e 2006, pelos
     pontos); resultados dados que a página marca como abandono (1999) ou deixa sem placar (2000); um "may yet be
     awarded" que a tabela conta como 1-1 (1999); clubes excluídos com os jogos anulados (2001: Kagera Stars; 2004:
     Reli Kigoma, Kariakoo e Pallsons);
   - classificação nos anos de fase final (2000 a 2004): a tabela da fase final dá as primeiras posições;
   - rebaixamento à mão onde a nota diz: 2000 (cancelado), 2001, 2002, 2004 ("seem to have been") e 2007.
   - Nada espera o Guilherme nesta liga.
6. **O que não deu para coletar:**
   - os jogos de 1965 a 1998 (fora a matriz de 1984 e metade de 1988) e parte dos de 2000 a 2006. Fonte que
     resolveria: jornais tanzanianos (Daily News, Mwananchi) ou o arquivo da TFF;
   - as tabelas de 1966 a 1984 e de 1990 a 1995;
   - autores dos gols na maior parte dos anos, artilheiros e cartões.
7. **Onde a revisão deve olhar primeiro:** a identidade dos clubes do item 5 (Moro United, JKT Tanzania, Kahama
   United); 2004 (rebaixados incertos e "Super Eight" só até a 6ª rodada); 2011/12 (um gol de diferença em 4 clubes
   entre o ogol e a tabela).
8. **Próxima competição:** `ang-1` (Angola), depois da decisão do Guilherme sobre o escopo.

## Recado de fim de coleta — ang-1 — 25/11/2026

Para o agente 1 (banco e painel) e o agente de revisão.

1. **O que foi feito:** `ang-1` (Campeonato Angolano, o Girabola), 48 edições de 1979 a 2025/26; 6.488 jogos (todos da
   RSSSF; 82 decididos fora de campo, 12 abandonados, 78 não jogados ou anulados); 13.984 gols, 440 com autor; 0 cartões;
   93 clubes, todos novos. Fontes: RSSSF (lista de campeões e página de cada ano), ogol (jogos de 1999 em diante:
   conferência, rodada e data). A Wikipédia ficou para depois (a API recusou o download por excesso de pedidos). A ESPN
   não tem a liga.
2. **Commit:** o deste recado (`Coleta Angola (ang-1): 48 edições, 6.488 jogos`).
3. **Teste de carga:** `ang-1: 48 edições, 6488 jogos, 93 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar o `ang-1`; país novo **ANG (Angola, CAF)**, criado pelo `competicao.json` (conferir a bandeira);
   - **temporadas**: ano civil de 1979 a 2018, duas metades de 2018/19 em diante;
   - **pontos**: 2-1-0 (vitória, empate, derrota) até 1994; 3-1-0 desde 1995;
   - **17 edições "sem jogos"** (só a tabela final: 1981 a 1997) e **1 com "jogos incompletos"** (1998);
   - **2019/20 abandonado** (Covid-19), sem campeão;
   - 1979: quatro grupos de seis, fase final e final.
5. **Decisões tomadas:**
   - escopo: o Girabola de 1979 a 2025/26, como a federação o numera (2025/26 = "XLVIII Girabola") e os clubes contam;
     fora o Campeonato Provincial da era colonial (1941–1974; 1975 abandonado), a Taça e a Supertaça (o Guilherme
     aprovou em 25/11);
   - nomes: "1º de Agosto", "1º de Maio", "Petro de Luanda", "Benfica de Luanda" (os Benficas levam a cidade); "ASA de
     Luanda" (o "ASA" já é o de Arapiraca); Atlético do Namibe = Desportivo Sonangol do Namibe; Santa Rita do Namibe = GD
     Welwitschia (o Santa Rita de Cássia, do Uíge, é outro clube); Bravos do Maqui = Onze Bravos do Maqui;
   - correções: um jogo repetido em 1999 (descartado); clubes que desistiram ou foram excluídos com os jogos anulados
     (1998: Kabuscorp; 2018: JGM; 2019/20: 1º de Maio; 2022/23: Cuando Cubango); em 1998 a classificação é a tabela
     final (sem o Kabuscorp, que vem depois);
   - rebaixamento à mão onde a nota diz: 1998 (Kabuscorp, desclassificado) e 2009 (1º de Maio e Académica do Lobito, no
     desempate com a 2ª divisão, que ficou fora da edição).
   - Nada espera o Guilherme nesta liga.
6. **O que não deu para coletar:**
   - os jogos de 1981 a 1997 (a RSSSF só tem a tabela) e parte dos de 1998. Fonte que resolveria: o Jornal de Angola ou o
     arquivo da FAF;
   - a Wikipédia (terceira fonte): fica para quando a API liberar;
   - autores dos gols na maior parte dos anos, artilheiros e cartões.
7. **Onde a revisão deve olhar primeiro:** a identidade dos clubes do item 5 (Atlético do Namibe, Santa Rita do Namibe,
   "Progresso" sozinho como o do Sambizanga); 1980, 2000 e 2007 (um placar diferente da tabela em dois clubes).
8. **Próxima competição:** `cod-1` (RD Congo), depois da decisão do Guilherme sobre o escopo.
