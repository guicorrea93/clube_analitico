"""Notas da tabela da Wikipédia en (note_XXX, hth_XXX) em português, para a observação da classificação final (revisão
QE-007, FR-014, DE-007, PT-015).

Fica em português o que explica a classificação: desempate (confronto direto), punição, rebaixamento ou permanência fora do
padrão, mudança de nome ou fusão. As notas de vaga europeia (classificação para copas, "would have qualified", Intertoto)
são descartadas: não dizem nada da classificação e muitas são hipotéticas (banimento inglês de 1985-1990).

Uso: traduzir(texto) -> texto em português ou None (descartada). As frases que as regras não cobrem estão em MANUAL; uma
nota nova sem regra nem tradução levanta erro no importador (para não entrar inglês no pacote).
"""
from __future__ import annotations

import re

NUMEROS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
           "eleven": 11, "twelve": 12, "fifteen": 15, "eighteen": 18, "thirty": 30}
EUROPA = re.compile(r"(?i)\b(qualif\w*|UEFA|Champions League|European Cup|Cup Winners|Fairs Cup|Intertoto|Europa League|"
                    r"Conference League|European competition|play-off round|gained entry|entered the 20|licen[cs]e)\b")


def _n(s: str) -> int:
    s = s.lower()
    return int(s) if s.isdigit() else NUMEROS[s]


def _placares(s: str) -> str:
    return s.replace("–", "-").strip().rstrip(".")


def _pontos(s: str) -> str:
    """"Lecce: 10 pts, Reggina: 4 pts" / "Marítimo 12, Boavista 4" -> "Lecce 10, Reggina 4"."""
    s = re.sub(r"\s*:\s*", " ", s.strip().rstrip("."))
    s = re.sub(r"\s*\bpts?\b\.?|\s*\bpoints?\b", "", s)
    return re.sub(r"\s*;\s*", ", ", s)


REGRAS: list[tuple[re.Pattern, callable]] = [
    # desempate pelo confronto direto
    (re.compile(r"^(.+?) (?:finished|is|are ranked|ranked|placed)? ?ahead of (.+?) on head[- ]to[- ]head (points|record|goal difference|goals)[:;,]?\s*(.*?)\.?$", re.I),
     lambda m: f"{m.group(1)} à frente de {m.group(2).replace(' and ', ' e ')} pelo "
               + {"goal difference": "saldo no confronto direto", "goals": "gols no confronto direto"}.get(m.group(3).lower(), "confronto direto")
               + (f": {_pontos(_placares(m.group(4)))}" if m.group(4) else "")),
    (re.compile(r"^Head[- ]to[- ]head points:\s*(.*)$", re.I), lambda m: f"pontos no confronto direto: {_pontos(m.group(1))}"),
    (re.compile(r"^Positions? (?:determined|decided|defined) by head[- ]to[- ]head points[:.]?\s*(.*)$", re.I),
     lambda m: f"posições pelo confronto direto: {_pontos(m.group(1))}"),
    (re.compile(r"^Head[- ]to[- ]head (?:was used as a tie-breaker|record) between (.+?) and (.+?)\.?$", re.I),
     lambda m: f"{m.group(1)} e {m.group(2)} desempatados pelo confronto direto"),
    (re.compile(r"^(.+?) (?:finished |is |placed )?ahead of (.+?) on overall goal difference\.?$", re.I),
     lambda m: f"{m.group(1)} à frente de {m.group(2)} pelo saldo de gols geral"),
    (re.compile(r"^(.+?) finished ahead of (.+?) on head[-–]to[-–]head (?:away goals(?: scored)?|goal-difference)[:;,]?\s*(.*?)\.?$", re.I),
     lambda m: f"{m.group(1)} à frente de {m.group(2)} pelo confronto direto (saldo e gols fora)"
               + (f": {_placares(m.group(3))}" if m.group(3) else "")),
    (re.compile(r"^(.+?) finished ahead of (.+?) on goal difference\s*[:;,]?\s*(.*?)\.?$", re.I),
     lambda m: f"{m.group(1)} à frente de {m.group(2)} pelo saldo de gols" + (f": {_placares(m.group(3)).replace(' = ', ' ')}" if m.group(3) else "")),
    (re.compile(r"^(.+?) ahead on head-to-head record;\s*(.*?)\.?$", re.I),
     lambda m: f"{m.group(1)} à frente pelo confronto direto: {_placares(m.group(2))}"),
    (re.compile(r"^Head-to-head record:\s*(.*)$", re.I), lambda m: f"pontos no confronto direto: {_pontos(m.group(1))}"),
    (re.compile(r"^Head-to-head away goals(?: scored)?:\s*(.*?)\.?$", re.I),
     lambda m: f"gols fora no confronto direto: {m.group(1)}"),
    (re.compile(r"^(\S[^:]{1,40}): (\d+) points?$", re.I), lambda m: f"pontos no confronto direto: {m.group(1)} {m.group(2)}"),
    (re.compile(r"^(.+?) had (\w+) points? deducted\.?$", re.I), lambda m: f"{m.group(1)}: {_n(m.group(2))} pontos a menos"),
    # confronto direto só com códigos e placares ("SEV 1–3 ATM; ATM 1–0 SEV", "OSA: 10 pts; CEL: 7 pts")
    (re.compile(r"^[A-ZÁÉÍÓÚÇ]{2,4}\b[A-ZÁÉÍÓÚÇ0-9:;,.()\s\-–→=+*]*(?:pts?\.?)?[A-ZÁÉÍÓÚÇ0-9:;,.()\s\-–→=+*pts]*$"),
     lambda m: "confronto direto: " + re.sub(r"\s*\bpts?\b\.?", "", m.group(0).replace("–", "-")).strip().rstrip(".")),
    # punições
    (re.compile(r"^(.+?) (?:were|was|have been|had been) (?:docked|deducted) (\w+) points?\.?$", re.I),
     lambda m: f"{m.group(1)}: {_n(m.group(2))} pontos a menos"),
    (re.compile(r"^(\w+) points? deducted\.?$", re.I), lambda m: f"{_n(m.group(1))} pontos a menos"),
]

# frases sem regra: a tradução (None = descartada). Chave = a nota como vem da Wikipédia (sem o ponto final).
MANUAL: dict[str, str | None] = {
    # Inglês
    "Sunderland were deducted two points for fielding an unregistered player": "2 pontos a menos por escalar jogador não inscrito",
    "Blackburn Rovers were initially relegated but were later reprieved due to the First Division expanding to 18 teams for "
    "the following season": "rebaixado em campo, mas ficou na 1ª divisão, ampliada para 18 clubes na temporada seguinte",
    "Middlesbrough were docked three points for failing to fulfill their original fixture at Blackburn Rovers on 21 December "
    "1996": "3 pontos a menos por não comparecer ao jogo contra o Blackburn Rovers marcado para 21/12/1996",
    "Portsmouth were docked nine points for entering administration": "9 pontos a menos por entrar em recuperação judicial",
    "Everton were deducted eight points for breaching profitability and sustainability rules. They were originally deducted "
    "ten points but this was reduced to six after an appeal. The club were then deducted an additional two points for further "
    "PSR breaches": "8 pontos a menos por violar as regras financeiras (PSR): 10, reduzidos a 6 no recurso, e mais 2",
    "Nottingham Forest were deducted four points for breaching profitability and sustainability rules. The club appealed the "
    "decision but were unsuccessful": "4 pontos a menos por violar as regras financeiras (PSR); o recurso foi negado",
    # Espanhol
    "Head-to-head points and goal difference: Deportivo 4 (+4), Celta 4 (0), Valladolid 4 (–4)":
        "pontos e saldo no confronto direto: Deportivo 4 (+4), Celta 4 (0), Valladolid 4 (-4)",
    "Málaga did not show up for the match of the 27th round, against Almería, which was played in Algeciras after Málaga's La "
    "Rosaleda Stadium had been closed. The Royal Spanish Football Federation awarded a win to Almería, while Málaga were also "
    "penalized with a three-point deduction": "não compareceu ao jogo da 27ª rodada contra o Almería (em Algeciras, com o "
                                              "estádio La Rosaleda interditado): vitória dada ao Almería e 3 pontos a menos",
    "Racing Santander were docked one point deduction due to using foreign players exceeds the quota during a match against "
    "Osasuna on 14 December 2003": "1 ponto a menos por escalar estrangeiros acima da cota contra o Osasuna (14/12/2003)",
    "Almería was docked 3 points due to an unpayment of a transfer": "3 pontos a menos por não pagar uma transferência",
    "Elche administratively relegated by the LFP": "rebaixado administrativamente pela LFP",
    "Tied on head-to-head points. Almería finished ahead of Granada on overall goal difference":
        "empatados no confronto direto; Almería à frente de Granada pelo saldo de gols geral",
    "Tied on head-to-head points and goal difference. Real Sociedad placed ahead of Espanyol on overall goal difference":
        "empatados em pontos e saldo no confronto direto; Real Sociedad à frente de Espanyol pelo saldo de gols geral",
    "Real Sociedad finished ahead of Real Betis and Alavés on head-to-head points: Real Sociedad 6, Real Betis 5, Alavés 5. "
    "Real Betis finished ahead of Alavés on goal difference: Real Betis –8, Alavés –11":
        "Real Sociedad à frente de Real Betis e Alavés pelo confronto direto: Real Sociedad 6, Real Betis 5, Alavés 5; Real "
        "Betis à frente de Alavés pelo saldo de gols (-8 e -11)",
    # notas de tabelas que entram em outras temporadas e divisões
    'Bootle was liquidated at the end of the season': 'o clube foi liquidado no fim da temporada',
    'Middlesbrough Ironopolis was liquidated at the end of the season': 'o clube foi liquidado no fim da temporada',
    'The official Football League records originally showed Birmingham in 5th place and Arsenal in 6th place. In 1975 it was discovered that an error in the calculation of Goal Average had been made and the table was corrected': 'a liga registrou Birmingham em 5º e Arsenal em 6º; em 1975 achou-se um erro no cálculo da média de gols e a tabela foi corrigida',
    'Leeds City were expelled from the league after 8 games; Port Vale took their place and inherited their record': 'Leeds City expulso depois de 8 jogos; o Port Vale ficou com a vaga e a campanha',
    'Stockport County had two points deducted for fielding Joe Smith without FA permission on 26 March 1927': '2 pontos a menos por escalar Joe Smith sem autorização (26/03/1927)',
    'After this season, South Shields moved to Gateshead and became Gateshead A.F.C': 'depois desta temporada mudou-se para Gateshead e virou Gateshead AFC',
    'Peterborough United were deducted 19 points for making irregular payments to players': '19 pontos a menos por pagamentos irregulares a jogadores',
    'Due to financial irregularities, Port Vale were initially expelled from the league, but this punishment was later reduced to applying for re-election': 'expulso por irregularidades financeiras; a punição virou pedido de reeleição',
    'Newport County had one point deducted for fielding an ineligible player': '1 ponto a menos por escalar jogador irregular',
    'Scunthorpe United v. Exeter was never played; Exeter failed to turn up and Scunthorpe were awarded the points': 'Scunthorpe x Exeter não foi jogado (o Exeter não compareceu); pontos para o Scunthorpe',
    'Bradford City v. Lincoln City was abandoned after 40 mins; the result (0–0) stood': 'Bradford City x Lincoln City interrompido aos 40 minutos; valeu o 0-0',
    'Swindon Town were disqualified from promotion after being found guilty of making illegal payments, and the play-off runners-up Sunderland were promoted in their place': 'Swindon perdeu o acesso por pagamentos ilegais; subiu o Sunderland',
    "Aldershot resigned from the Football League on 25 March 1992 and subsequently folded; the club's playing record of Pld36 W3 D8 L25 GF21 GA63 Pts17 was expunged": 'Aldershot deixou a liga em 25/03/1992 e fechou; a campanha foi anulada',
    'Mestalla was ineligible for promotion, as they were the reserve team of Valencia': 'Mestalla não podia subir (time reserva do Valencia)',
    'España Industrial was ineligible for promotion, as they were the reserve team of Barcelona': 'España Industrial não podia subir (time reserva do Barcelona)',
    'For playing in La Liga, España Industrial resigned to continue being the reserve team of Barcelona and was renamed as Condal': 'o España Industrial desistiu da 1ª divisão para seguir como reserva do Barcelona, com o nome de Condal',
    'RCD Español was renamed RCD Espanyol in February 1995': 'o RCD Español passou a se chamar RCD Espanyol em fevereiro de 1995',
    'AC Sampierdarenese was called AC Liguria before the war': 'a Sampierdarenese se chamava AC Liguria antes da guerra',
    'Brescia lost Relegation tie-breaker 1–3 vs.Udinese on 12 June 1993 then relegated to 1993-94 Serie B': 'perdeu o desempate de rebaixamento para a Udinese (1-3, 12/06/1993) e caiu',
    'winner of relegation tie-breaker 1-1*(5:4) vs Genoa. (10 June 1995)': 'venceu o desempate de rebaixamento contra o Genoa (1-1, 5-4 nos pênaltis, 10/06/1995)',
    'Loser of relegation tie-breaker 1-1*(4:5) vs Padova. (10 June 1995). Relegated to 1995-96 Serie B': 'perdeu o desempate de rebaixamento para o Padova (1-1, 4-5 nos pênaltis, 10/06/1995) e caiu',
    'ROM 1-1 PAR; PAR 1-1 ROM Roma is ahead due to Goal difference': 'confronto direto: ROM 1-1 PAR; PAR 1-1 ROM; Roma à frente pelo saldo de gols',
    'Hellas Verona winner of 2000–01 Relegation tie-breaker against Reggina': 'venceu o desempate de rebaixamento contra a Reggina',
    "Messina were reprieved from relegation following Juventus's punishment": 'rebaixado em campo, ficou na Serie A com a punição da Juventus (Calciopoli)',
    'Atalanta were deducted 6 points due to involvement in the 2011–12 Italian football scandal': '6 pontos a menos pelo escândalo de apostas de 2011/12',
    'Internazionale finished ahead of Lazio on head-to-head: Internazionale 0–0 Lazio, Lazio 2–3 Internazionale': 'Internazionale à frente de Lazio pelo confronto direto: Internazionale 0-0 Lazio, Lazio 2-3 Internazionale',
    'Eintracht Frankfurt were docked two points because of licensing irregularities': '2 pontos a menos por irregularidades na licença',
    'Championship not considered official due to an unequal number of matches played between teams': 'campeonato não oficial: os clubes jogaram números diferentes de jogos',
    '2PT': None,
    '2 points deducted for failing to play a match against Spekholzerheide': '2 pontos a menos por não jogar contra o Spekholzerheide',
    'Owing to the war, Feijenoord were forced to play their home games on neutral grounds': 'por causa da guerra, o Feijenoord jogou em casa em campo neutro',
    'Changed name back to Juliana': 'voltou a se chamar Juliana',
    'Hermes DVS and Sparta Rotterdam were level on points after 26 games and played a play-off game to decide the league winners and entrance to the championship play-offs': 'Hermes DVS e Sparta empataram em pontos e fizeram um jogo de desempate pela vaga na fase final',
    '1 point deducted?': '1 ponto a menos (a fonte marca dúvida)',
    'Winners KNVB Cup': None,
    'relegated after losing promotion/relegation play-offs': 'rebaixado ao perder o play-off de acesso e rebaixamento',
    'Dumbarton and Rangers finished equal on points, and a play-off to determine the winner ended in a 2−2 draw so both teams were declared joint champions': 'Dumbarton e Rangers empataram em pontos e no jogo de desempate (2-2): campeões juntos',
    'Cowlairs failed re-election to compete in the league for the next season': 'Cowlairs não foi reeleito para a temporada seguinte',
    'Renton were expelled from the league in September 1890 for professionalism and their record was expunged': 'Renton expulso em setembro de 1890 por profissionalismo; a campanha foi anulada',
    # Francês
    "During World War II, Excelsior and Roubaix merged into CO Roubaix-Tourcoing, which took Excelsior's place in Division 1 "
    "after the war ended": "na guerra, Excelsior e Roubaix se fundiram no CO Roubaix-Tourcoing, que ficou com a vaga do "
                           "Excelsior na 1ª divisão depois da guerra",
    "During World War II, Lillois and Fives merged to form Lille OSC, which took both the clubs' place in Division 1 after the "
    "war ended": "na guerra, Olympique Lillois e Fives se fundiram no Lille OSC, que ficou com a vaga dos dois na 1ª divisão "
                 "depois da guerra",
    "Marseille and Valenciennes were deducted one point for their involvement in the French football bribery scandal":
        "Marseille e Valenciennes: 1 ponto a menos pelo escândalo de suborno (caso VA-OM)",
    "Metz were deducted one point by the Discipline Commission and ordered to play one match behind closed doors as a result "
    "of the racist insults inflicted by one of their fans on Valenciennes player Abdeslam Ouaddou. However, the decision of the "
    "point deduction was reversed on 27 March 2008": "1 ponto a menos (insultos racistas de torcedor), anulado em 27/03/2008",
    "On 9 August 2012, Ajaccio was docked two points, one suspended, by the Disciplinary Committee of the Ligue de Football "
    "Professionnel for the 2012–13 season because of incidents during a 2011–12 league match against Lyon":
        "2 pontos a menos (1 com suspensão) por incidentes num jogo contra o Lyon em 2011/12",
    "Monaco were deducted 2 points due to poor fan behavior in a match last season. However this was overturned on 13 August "
    "2013": "2 pontos a menos por conduta da torcida, anulados em 13/08/2013",
    "It was announced on 29 January 2015 that Lens' promotion from Ligue 2 at the end of the 2013–14 season has been ruled "
    "invalid, and will thus be automatically relegated to Ligue 2 for the 2015–16 season, regardless of where the team place "
    "this season. It has been confirmed by the French Football Federation that the decision of the Administrative Court of "
    "Besançon will be appealed": "o acesso de 2013/14 foi invalidado (29/01/2015): rebaixado à Ligue 2 qualquer que fosse a "
                                 "posição",
    "Originally, the 18th-placed Ligue 1 team would play in promotion-relegation play-offs at the end of the season with a "
    "team from Ligue 2 to decide whether they would remain in Ligue 1 for the 2020–21 season, but the play-offs were cancelled "
    "and the 18th-placed team remained in Ligue 1": "o 18º jogaria o play-off de rebaixamento, cancelado (covid-19): ficou na Ligue 1",
    "Lyon were deducted one point for uncontrolled crowd trouble that caused the abandonment of their match against Marseille":
        "1 ponto a menos por incidentes da torcida que interromperam o jogo contra o Marseille",
    "Nice were deducted one point for uncontrolled crowd trouble that caused the abandonment of their match against Marseille":
        "1 ponto a menos por incidentes da torcida que interromperam o jogo contra o Marseille",
    "Montpellier was deducted one point for uncontrolled crowd trouble that caused the abandonment of its match against "
    "Clermont": "1 ponto a menos por incidentes da torcida que interromperam o jogo contra o Clermont",
    # Alemão
    "Meidericher SV changed their name to MSV Duisburg during the season": "o Meidericher SV passou a se chamar MSV Duisburg "
                                                                            "durante a temporada",
    "Following the DFB investigation into match fixing, Arminia Bielefeld was automatically relegated. Records were expunged":
        "rebaixado pela DFB por manipulação de resultados; os jogos ficaram com 0 pontos para o Arminia",
    "Dynamo Dresden were docked four points because of financial irregularities": "4 pontos a menos por irregularidades financeiras",
    "1. FC Kaiserslautern were docked three points for financial irregularities": "3 pontos a menos por irregularidades financeiras",
    # Italiano
    "Atalanta was ranked last by the Federation due to a match fixing scandal, but later got acquitted":
        "posto em último pela federação por manipulação de resultados; depois absolvido",
    "Genoa was penalized of 18 points for bribery, and 10 more in the following season. The points for the following seasons "
    "were reduced to 7 in appeal": "18 pontos a menos por suborno (e mais 10 na temporada seguinte, reduzidos a 7 no recurso)",
    "After the title tie-breaker with Bologna (2–0)": "perdeu o desempate pelo título para o Bologna (0-2)",
    "6 points deducted for bribery": "6 pontos a menos por suborno",
    "3 points deducted for alleged bribery": "3 pontos a menos por suposto suborno",
    "Demoted in the last place for bribery by the Federation": "posto em último pela federação por suborno",
    "Bologna, Avellino and Perugia started the season with a 5-point penalisation because of the Totonero 1980 scandal":
        "Bologna, Avellino e Perugia começaram com 5 pontos a menos (escândalo Totonero de 1980)",
    "Juventus became the first team in Italian football to be awarded two golden stars, to commemorate their 20th title win":
        None,
    "Udinese was penalised 9 points from the start of the season for the Totonero 1986":
        "começou com 9 pontos a menos (escândalo Totonero de 1986)",
    "Empoli was penalised of 5 points from the start of the season": "começou com 5 pontos a menos",
    "Fiorentina relegated for head-to-head points (Brescia 5; Udinese 4; Fiorentina 3)":
        "rebaixado pelo confronto direto: Brescia 5, Udinese 4, Fiorentina 3",
    "Relegated to 1997-98 Serie B for direct matches": "rebaixado pelo confronto direto",
    "Empoli were docked two points due to attempted bribery of referee during a match against Sampdoria on 25 October 1998":
        "2 pontos a menos por tentativa de suborno do árbitro contra a Sampdoria (25/10/1998)",
    "Fiorentina was denied entry to the 2002–03 Serie B season, having entered administration. It was later admitted to the "
    "Lega Professionisti Serie C after bankruptcy": "falido, ficou fora da Serie B 2002/03; refundado, foi para a Serie C",
    "Ancona was denied entry to the 2004–05 Serie B season, having entered administration. It was later admitted to the Lega "
    "Professionisti Serie C after bankruptcy": "falido, ficou fora da Serie B 2004/05; refundado, foi para a Serie C",
    "Juventus were stripped of the title during the 2005–06 Serie A season, because of the 2006 Italian football scandal":
        "título revogado em 2006 (Calciopoli)",
    "Juventus were originally the first-placed team, but the title was put sub judice due to the Calciopoli scandal. After "
    "court hearings, Juventus were placed at the bottom of the league table (points were not deducted), relegating them to "
    "Serie B, while the title was assigned to Internazionale, the team taking the first place in the end":
        "terminou em 1º, mas foi posto em último pelo Calciopoli e rebaixado; o título foi dado à Inter",
    "Milan, Fiorentina and Lazio were docked 30 points, all for involvement in the Calciopoli":
        "Milan, Fiorentina e Lazio: 30 pontos a menos (Calciopoli)",
    "Fiorentina were docked 15 points, Reggina 11 points, Milan 8 points and Lazio 3 points, all for involvement in the 2006 "
    "Italian football scandal": "pontos a menos pelo Calciopoli: Fiorentina 15, Reggina 11, Milan 8 e Lazio 3",
    "Siena were given a one-point deduction for a delay in payment of social security contributions":
        "1 ponto a menos por atraso nas contribuições previdenciárias",
    "Cagliari was docked 3 points for filing an unauthorized lawsuit, but the penalty was later reversed":
        "3 pontos a menos por ação judicial não autorizada; a punição foi anulada depois",
    "Bologna were deducted a total 3 points: 1 point because of unpaid taxes, plus 2 points because of unpaid wages":
        "3 pontos a menos: 1 por impostos e 2 por salários atrasados",
    "Atalanta was docked 2 points due to involvement in the 2011–12 Italian football scandal":
        "2 pontos a menos pelo escândalo de apostas de 2011/12",
    "Sampdoria and Torino were docked 1 point due to involvement in the 2011–12 Italian football scandal":
        "Sampdoria e Torino: 1 ponto a menos pelo escândalo de apostas de 2011/12",
    "Siena was docked 6 points due to involvement in the 2011–12 Italian football scandal":
        "6 pontos a menos pelo escândalo de apostas de 2011/12",
    "Parma was docked 7 points for failing to pay over players' wages. Later the club announced bankruptcy, and it was "
    "recreated without professional status": "7 pontos a menos por salários atrasados; depois faliu e foi refundado como amador",
    "Chievo were deducted 3 points after being found guilty of false accounting": "3 pontos a menos por fraude contábil",
    "Juventus were deducted 10 points as punishment for capital gain violations":
        "10 pontos a menos por fraude nas plusvalenze (ganhos de capital)",
    # Holandês
    "Winners of the 1989–90 KNVB Cup": None,
    "Winners of the KNVB Cup": None,
    "won and remained in the 1995–96 Eredivisie": "venceu o play-off e ficou na Eredivisie",
    "Ajax won the 2005–06 KNVB Cup": None,
    "NAC Breda were docked 1 point because they were late with payment obligations to Contractspelers Fonds KNVB (CFK)":
        "1 ponto a menos por atraso nos pagamentos ao fundo de jogadores da KNVB",
    "FC Twente were deducted three points twice since they did not meet the financial standards set by the KNVB":
        "6 pontos a menos (3 duas vezes) por não cumprir as normas financeiras da KNVB",
    "Twente was excluded from European football for 3 years on 15 December 2015": None,
    "Twente were excluded from European football for 3 years on 15 December 2015": None,
    # Português
    "CUF Barreiro was temporarily renamed Unidos Futebol Clube, commonly known as Unidos do Barreiro":
        "a CUF jogou esta temporada com o nome de Unidos Futebol Clube (Unidos do Barreiro)",
    "Vitória de Setúbal: 4 points": "pontos no confronto direto: Vitória de Setúbal 4",
    "Belenenses were docked 3 points for fielding an ineligible player": "3 pontos a menos por escalar jogador irregular",
    "Paços de Ferreira were originally relegated but stayed in the league because of Boavista being relegated over the "
    "bribery scandal": "rebaixado em campo, mas ficou na liga: o Boavista foi rebaixado pelo Apito Final",
    "Porto were docked 6 points due to attempted bribery of referees in the 2003–04 season. However, the Council of Justice of "
    "the Portuguese Federation returned them in 2017": "6 pontos a menos por tentativa de suborno de árbitros em 2003/04 "
                                                       "(Apito Final); devolvidos pela federação em 2017",
    "Estoril is ahead of Chaves and Vitória de Setúbal on head-to-head points: Estoril 6 pts, Chaves 5 pts, Vitória de Setúbal "
    "5 pts. Chaves is ahead of Vitória de Setúbal on head-to-head goal difference":
        "Estoril à frente de Chaves e Vitória de Setúbal pelo confronto direto: Estoril 6, Chaves 5, Vitória de Setúbal 5; "
        "Chaves à frente de Vitória de Setúbal pelo saldo no confronto direto",
    # Escocês
    "Celtic, 3rd LRV and Cowlairs were deducted four points each for fielding ineligible players":
        "Celtic, 3rd LRV e Cowlairs: 4 pontos a menos cada um por escalar jogadores irregulares",
    "Dundee and Partick Thistle finished level on points but Dundee won a play-off match to determine ranking positions":
        "empatado em pontos com o Partick Thistle; ficou à frente por vencer o jogo de desempate",
    "Gretna were deducted 10 points for entering administration": "10 pontos a menos por entrar em recuperação judicial",
    "Teams in the bottom half at the time of the split may not overtake a team in the top 6 at the time of the split":
        "depois da divisão em dois grupos, os 6 de baixo não podem passar os 6 de cima",
    "Heart of Midlothian were deducted 15 points for entering administration":
        "15 pontos a menos por entrar em recuperação judicial",
    "Teams in the bottom six at the time of the split (33 games) cannot pass teams in the top six":
        "depois da divisão em dois grupos (33 rodadas), os 6 de baixo não podem passar os 6 de cima",
    "Dundee United were deducted three points for fielding an ineligible player in their win over Inverness Caledonian Thistle "
    "on 6 May 2016": "3 pontos a menos por escalar jogador irregular na vitória sobre o Inverness CT (06/05/2016)",
}


def traduzir(texto: str | None) -> str | None:
    if not texto:
        return None
    t = re.sub(r"\s+", " ", texto).strip()
    chave = t.rstrip(".")
    if chave in MANUAL:
        return MANUAL[chave]
    for regex, f in REGRAS:
        m = regex.match(t)
        if m:
            r = f(m)
            if re.search(r"\b(the|on|ahead|is|are|were|was|points|and|of)\b", r):   # sobrou inglês: vai para MANUAL
                raise KeyError(t)
            return r
    if EUROPA.search(t):
        return None
    raise KeyError(t)
