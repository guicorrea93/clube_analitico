"""Grava SCRATCH/achados_QE.csv (3ª rodada, eng-1 e esp-1). Uso: python -I revisao/QE/gravar_achados.py <SCRATCH>"""
import csv
import sys

SCRATCH = sys.argv[1]
CAB = ["id", "competicao", "item", "edicao", "clube", "o_que_esta_no_painel", "o_que_a_fonte_diz", "fonte", "gravidade",
       "quem_corrige", "situacao"]
A = [
    ["QE-001", "esp-1", "B critério de desempate / F Corrida",
     "1928/29 a 2025/26 (Corrida); 1954/55, 1963/64, 1969/70, 1972/73, 1981/82, 1995/96 (critério)", "",
     "fases.csv e a classificação rodada a rodada usam o 'confronto' da coleta: pontos e saldo nos jogos entre os empatados, "
     "testado primeiro e aplicado com os jogos já disputados. (1) Em 1963/64 o critério escolhido foi 'média de gols', só "
     "porque reproduz a ordem; em 1954/55, 1969/70, 1972/73, 1981/82 e 1995/96 nenhum critério reproduz a ordem e a última "
     "rodada da Corrida difere da Classificação (ex.: 1969/70 Real Madrid 5º e Valencia 6º na Corrida; 1995/96 Athletic 14º e "
     "Oviedo 15º). (2) Na Corrida, o confronto entra com só um dos dois jogos disputados: 11.351 posições de rodada em 95 "
     "temporadas (202 com troca de líder) diferem da regra (ex.: 1928/29 rodada 2, Espanyol 4º e Real Unión 8º; pelo saldo, "
     "Real Unión 4º)",
     "A regra espanhola é o confronto direto desde 1928/29 (class_rules de todas as temporadas na Wikipédia en; nos dados, em "
     "1930/31, 1931/32, 1933/34, 1934/35... só o confronto reproduz a ordem), aplicado de novo entre os que seguem empatados "
     "(recursivo): pontos entre os empatados, pontos entre os que sobram empatados, saldo entre eles, saldo geral, gols pró. Essa "
     "regra reproduz 92 das 93 temporadas de fase única (todas menos 1960/61, ver QE-002), inclusive as 6 acima. E o confronto só "
     "vale depois de jogados todos os jogos entre os empatados; antes, saldo e gols pró (nota do class_rules desde 2017/18: "
     "'Head-to-head record is used only after all the matches between the teams in question have been played') | SUGESTÃO: "
     "critério fixo 'confronto_esp' em todas as temporadas (sem escolher pelo 1º que reproduz): rank recursivo como o "
     "'confronto_geral' do por-1, mais o saldo entre os empatados; na classificação de rodada, usar o confronto só quando "
     "len(jogos entre eles) == n*(n-1), senão saldo e gols pró; texto em fases.csv: 'pontos, confronto direto (pontos e saldo "
     "entre os empatados, de novo entre os que seguem empatados), saldo de gols, gols pró'. Código de referência pronto: "
     "revisao/QE/desempate_esp.py (ordenar_esp, so_completo=True); lista das 11.351 posições: revisao/QE/corrida_esp_saida.txt; "
     "fonte: https://en.wikipedia.org/wiki/2017%E2%80%9318_La_Liga (class_rules) e data/coleta/esp-1/wikipedia/*.wiki; "
     "mexer em: coleta/esp-1/importar.py, ordenar() (linhas ~339-363), escolha do critério em main() (~631-642) e "
     "classificação rodada a rodada (~737-752); depois testar_carga e documentar.py",
     "revisao/QE/desempate_esp.py; revisao/QE/corrida_esp.py; https://en.wikipedia.org/wiki/1963%E2%80%9364_La_Liga",
     "media", "coleta-europa", "aberto"],
    ["QE-002", "esp-1", "B classificação", "1960/61", "Athletic Bilbao; Betis",
     "6º Betis e 7º Athletic Bilbao (os dois com 30 pontos, empatados também com a Real Sociedad, 8ª). Ordem da Wikipédia en/es",
     "A tabela da RSSSF (https://www.rsssf.org/tabless/spanhist5969.html#6061) e a do BDFutbol "
     "(https://www.bdfutbol.com/es/t/t1960-61.html) dão 6º Athletic e 7º Betis. É o que dá a regra que reproduz as outras 92 "
     "temporadas (QE-001): no triangular Betis e Athletic fazem 5 pontos e a Real Sociedad 2; entre os dois, Athletic 0-0 Betis e "
     "Betis 1-3 Athletic. A Wikipédia só põe o Betis à frente pelo saldo do triangular (sem aplicar o confronto de novo entre os "
     "dois), critério que falha em 1963/64. Sem efeito em título nem rebaixamento | SUGESTÃO: 6º Athletic Bilbao, 7º Betis (RSSSF); fonte: "
     "https://www.rsssf.org/tabless/spanhist5969.html#6061; mexer em: coleta/esp-1/importar.py, escolha da ordem oficial "
     "(~linhas 607-622, 'ordem oficial: Wikipédia; sem ela, RSSSF'): com o QE-001 aplicado, ficar com a fonte que "
     "bate com o critério, ou um dicionário ORDEM_OFICIAL {1960: 'RSSSF'} com o motivo. Antes de trocar, se der, confirmar numa "
     "4ª fonte (jornal da época: ABC ou Mundo Deportivo de 01/05/1961)",
     "https://www.rsssf.org/tabless/spanhist5969.html#6061; https://www.bdfutbol.com/es/t/t1960-61.html; "
     "https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_de_Espa%C3%B1a_1960-61",
     "alta", "coleta-europa", "aberto"],
    ["QE-003", "esp-1", "C datas", "2003/04", "Barcelona; Sevilla",
     "Barcelona 1-1 Sevilla em 02/09/2003, sem hora (pacote, banco)",
     "O jogo começou à 00:05 de 03/09/2003 (o famoso jogo da meia-noite): football-data '03/09/03'; ESPN 2003-09-02T22:05Z = "
     "00:05 em Madri; transfermarkt 'Wed 03/09/03 12:05 AM'; BDFutbol 03/09/2003. A data 02/09 vem do engsoccerdata e do ogol | "
     "SUGESTÃO: data 2003-09-03, hora 00:05; fonte: https://www.bdfutbol.com/es/p/p.php?id=23214 e "
     "data/coleta/esp-1/football-data/SP1_0304.csv; mexer em: coleta/esp-1/importar.py, dicionário novo DATAS "
     "{(2003, 'Barcelona', 'Sevilla'): '2003-09-03'} aplicado como no eng-1 (coleta/eng-1/importar.py, DATAS, ~linha 310), "
     "antes de casar a ESPN (assim a hora entra)",
     "https://www.bdfutbol.com/es/p/p.php?id=23214; https://www.transfermarkt.com/laliga/gesamtspielplan/wettbewerb/ES1/saison_id/2003",
     "media", "coleta-europa", "aberto"],
    ["QE-004", "esp-1", "C jogos suspensos", "2004/05; 2023/24", "Real Madrid; Real Sociedad; Granada; Athletic Bilbao",
     "Real Madrid 2-1 Real Sociedad em 05/01/2005 e Granada 1-1 Athletic em 11/12/2023, sem observação",
     "Os dois começaram em outro dia e foram suspensos: Real Madrid x Real Sociedad em 12/12/2004 (ameaça de bomba, aos 88', "
     "1-1), completado em 05/01/2005; Granada x Athletic em 10/12/2023 (morte de um torcedor na arquibancada, no 1º tempo), "
     "completado em 11/12/2023. BDFutbol e transfermarkt trazem a data de início; ogol, ESPN e o pacote, a do fim | SUGESTÃO: "
     "manter a data de conclusão e pôr a observação 'começou em 12/12/2004 e foi suspenso aos 88' (ameaça de bomba)' e "
     "'começou em 10/12/2023 e foi suspenso no 1º tempo (morte de um torcedor)'; fonte: https://www.bdfutbol.com/es/p/p.php?id=23749 "
     "e https://www.bdfutbol.com/es/p/p.php?id=31397; mexer em: coleta/esp-1/importar.py, EXPLICACOES (2004 e 2023) e campo "
     "observacao da partida",
     "https://www.bdfutbol.com/es/p/p.php?id=23749; https://www.bdfutbol.com/es/p/p.php?id=31397",
     "baixa", "coleta-europa", "aberto"],
    ["QE-005", "eng-1", "C datas", "1953/54", "Sheffield Wednesday; Aston Villa",
     "Sheffield Wednesday 3-1 Aston Villa em 07/09/1953 (segunda-feira)",
     "11v11 e transfermarkt dão sábado 07/11/1953; no pacote, 07/11/1953 tem só 10 jogos (os outros 20 clubes) e os dois não "
     "jogam nesse sábado; o engsoccerdata e o ogol trocaram o mês | SUGESTÃO: data 1953-11-07; fonte: "
     "https://www.11v11.com/teams/sheffield-wednesday/tab/matches/season/1954/ e "
     "https://www.transfermarkt.com/first-division-bis-91-92-/gesamtspielplan/wettbewerb/EFD1/saison_id/1953; mexer em: "
     "coleta/eng-1/importar.py, DATAS (linha ~53): (1953, 'Sheffield Wednesday', 'Aston Villa'): '1953-11-07'",
     "https://www.11v11.com/teams/sheffield-wednesday/tab/matches/season/1954/; transfermarkt EFD1 1953",
     "media", "coleta-europa", "aberto"],
    ["QE-006", "eng-1", "C árbitro", "2000/01 a 2025/26", "",
     "partida.arbitro (football-data) em 3 formatos: 'David Elleray' (2000/01), 'Elleray, D. R.' (211 jogos de 2001/02) e "
     "'D Elleray' (2002/03 em diante); o mesmo árbitro com 2 ou 3 nomes (ex.: 'Dean, M. L', 'M Dean'); 'David Ellaray' (21 jogos "
     "de 2000/01, grafia errada); 40 jogos com outro sobrenome (24 em 2000/01, 7 em 2024/25...; ex.: 2000/01 Everton x Charlton 'Andy Hall', BDFutbol 'Neale Barry'). "
     "O painel ainda não mostra árbitro",
     "BDFutbol traz o nome completo do árbitro em todos os jogos (página da temporada, 1 por temporada); bate pelo sobrenome em "
     "9.607 de 9.880 jogos de 2000/01 a 2025/26; os outros 273 são formato/grafia (lista em revisao/QE/cmp_bdfutbol.py, saída "
     "na tela) | SUGESTÃO: nome completo do BDFutbol ('Mike Dean', 'David Elleray', 'Graham Poll'...) em todas as temporadas; "
     "onde o sobrenome difere, ficar com o BDFutbol e conferir no transfermarkt; fonte: https://www.bdfutbol.com/es/t/teng2001-02.html; "
     "mexer em: coleta/eng-1/importar.py, campo 'arbitro' de partidas (linha ~561, (x or {}).get('Referee')): trocar pela "
     "coluna Árbitro da página da temporada do BDFutbol (ou normalizar com um dicionário ARBITROS)",
     "https://www.bdfutbol.com/es/t/teng2000-01.html; data/coleta/eng-1/football-data",
     "baixa", "coleta-europa", "aberto"],
    ["QE-007", "eng-1; esp-1", "B observações em inglês", "eng-1: 1890/91, 1897/98, 1984/85-1988/89, 1996/97, 1997/98, 2009/10, "
     "2023/24; esp-1: 1959/60, 1961/62, 1979/80, 1994/95, 1998/99, 2001/02, 2003/04, 2009/10, 2014/15", "",
     "classificacao_final.observacao com a nota da Wikipédia en sem tradução: 18 linhas no eng-1 (ex.: 'Sunderland were deducted "
     "two points for fielding an unregistered player.'; 'Manchester United would have qualified for the Cup Winners' Cup...') e "
     "13 no esp-1. O painel hoje não mostra esse campo",
     "Texto em português, como o resto do pacote (ex.: 'não foi reeleito...') | SUGESTÃO: traduzir as notas (ou guardar só as "
     "de punição e rebaixamento, em português) e descartar as de vaga europeia hipotética (1984/85-1989/90, banimento inglês); "
     "fonte: as próprias notas (Wikipédia en de cada temporada); mexer em: coleta/comum-europa/wiki_tabela.py (leitura das "
     "notas) ou no importar.py de cada liga, onde a observacao da classificação é montada",
     "banco: select observacao from classificacao_final ... (eng-1, esp-1)",
     "baixa", "coleta-europa", "aberto"],
    ["QE-008", "eng-1", "B critério de desempate / F Corrida", "todas", "",
     "Conferido o vício do DE-002 (critério escolhido por ser o 1º que reproduz a ordem)",
     "Não afeta o Inglês: o critério é fixo por época (coleta/eng-1/importar.py, ordenar: média de gols até 1975/76, saldo e "
     "gols pró depois), igual à regra da liga; a Corrida só existe nas 33 temporadas com rodadas fixas (1992/93, 1993/94, "
     "1995/96 em diante), com saldo, e a última rodada é igual à classificação final nas 33. Os 126 quadros finais já batiam "
     "com o 11v11 (2ª rodada); o BDFutbol confirma 1960/61-2025/26 (as diferenças dele são de média x saldo antes de 1976 e da "
     "punição do Everton em 2023/24, erros do BDFutbol)",
     "revisao/QE/cmp_bdfutbol.py (eng); coleta/eng-1/importar.py",
     "baixa", "coleta-europa", "nao-e-erro"],
    ["QE-009", "esp-1", "A edições", "2025/26", "",
     "2025/26 no pacote, no banco e no painel local (95 edições, 27.716 jogos): campeão Barcelona (94), vice Real Madrid (86); "
     "rebaixados Mallorca (18º, 42 pontos, triplo empate com Levante e Osasuna), Girona e Real Oviedo; artilheiro Mbappé 25. "
     "O site ainda mostra 94 edições (dados/esp-1.js publicado é o anterior)",
     "BDFutbol (https://www.bdfutbol.com/es/t/t2025-26.html): os 380 jogos com o mesmo placar e a mesma data; a classificação "
     "inteira igual (posição, J, V, E, D, GP, GC e pontos); 1.024 gols, todos com autor; a ordem do triplo empate em 42 bate com "
     "o confronto direto recursivo. Só falta publicar (decisão do Guilherme)",
     "https://www.bdfutbol.com/es/t/t2025-26.html; revisao/QE/cmp_bdfutbol.py",
     "baixa", "banco-painel", "nao-e-erro"],
    ["QE-010", "eng-1; esp-1", "C datas", "esp-1: 1929/30, 1946/47, 1955/56, 1977/78, 1988/89, 2000/01, 2011/12; eng-1: 1960/61 a "
     "2001/02 (19 jogos); 1889/90 e 1935/36 (transfermarkt)", "",
     "Datas em que a fonte nova diverge do pacote",
     "Terceira opinião (11v11, transfermarkt ou ogol) confirma o pacote em todas: ex.: 1988/89 rodada de 01/01/1989 (BDFutbol "
     "31/12/1988; transfermarkt 'Sun 01/01/1989'); 2011/12 Granada x Mallorca adiado para 07/12/2011; 1987/88 Tottenham x Derby "
     "01/03/1988 (BDFutbol 01/05). São erros do BDFutbol (cerca de 40 em 56 mil jogos) e do transfermarkt (1889/90, temporada "
     "incompleta lá). Lista em revisao/QE/cmp_bdfutbol_esp.txt, cmp_bdfutbol_eng.txt e cmp_tm_eng.txt; terceira opinião por "
     "revisao/QE/terceira_datas.py",
     "revisao/QE/terceira_datas.py",
     "baixa", "coleta-europa", "nao-e-erro"],
]
with open(f"{SCRATCH}/achados_QE.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(CAB)
    for a in A:
        assert len(a) == len(CAB), a[0]
        w.writerow(a)
print(len(A))
