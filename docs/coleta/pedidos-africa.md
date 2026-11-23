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
2. **Commits:** nenhum ainda (esperando o ok do Guilherme).
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
