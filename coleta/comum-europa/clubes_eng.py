"""Cadastro dos clubes ingleses (e galeses da liga inglesa), comum a todas as divisões da Inglaterra.

Chave: o nome do engsoccerdata (nome atual do clube). Valor: nome de exibição no painel (como o clube é conhecido
no Brasil), cidade e país (código FIFA). O mesmo clube tem o mesmo nome em eng-1, eng-2...

ALIASES: outras grafias (RSSSF, football-data, ESPN, Wikipédia) -> chave do engsoccerdata. O ogol e a ESPN
são casados pelo código do clube (votação jogo a jogo em importar.py), não por aqui.
"""
from __future__ import annotations

import re
import unicodedata

CLUBES = {
    "AFC Bournemouth": ("Bournemouth", "Bournemouth", "ENG"),
    "Accrington F.C.": ("Accrington", "Accrington", "ENG"),        # o Accrington FC original (1878-1896), não o Stanley
    "Arsenal": ("Arsenal", "Londres", "ENG"),
    "Aston Villa": ("Aston Villa", "Birmingham", "ENG"),
    "Barnsley": ("Barnsley", "Barnsley", "ENG"),
    "Birmingham City": ("Birmingham", "Birmingham", "ENG"),
    "Blackburn Rovers": ("Blackburn", "Blackburn", "ENG"),
    "Blackpool": ("Blackpool", "Blackpool", "ENG"),
    "Bolton Wanderers": ("Bolton", "Bolton", "ENG"),
    "Bradford City": ("Bradford City", "Bradford", "ENG"),
    "Bradford Park Avenue": ("Bradford Park Avenue", "Bradford", "ENG"),
    "Brentford": ("Brentford", "Londres", "ENG"),
    "Brighton & Hove Albion": ("Brighton", "Brighton", "ENG"),
    "Bristol City": ("Bristol City", "Bristol", "ENG"),
    "Burnley": ("Burnley", "Burnley", "ENG"),
    "Bury": ("Bury", "Bury", "ENG"),
    "Cardiff City": ("Cardiff", "Cardiff", "WAL"),
    "Carlisle United": ("Carlisle", "Carlisle", "ENG"),
    "Charlton Athletic": ("Charlton", "Londres", "ENG"),
    "Chelsea": ("Chelsea", "Londres", "ENG"),
    "Coventry City": ("Coventry", "Coventry", "ENG"),
    "Crystal Palace": ("Crystal Palace", "Londres", "ENG"),
    "Darwen": ("Darwen", "Darwen", "ENG"),
    "Derby County": ("Derby County", "Derby", "ENG"),
    "Everton": ("Everton", "Liverpool", "ENG"),
    "Fulham": ("Fulham", "Londres", "ENG"),
    "Glossop North End": ("Glossop", "Glossop", "ENG"),
    "Grimsby Town": ("Grimsby", "Cleethorpes", "ENG"),
    "Huddersfield Town": ("Huddersfield", "Huddersfield", "ENG"),
    "Hull City": ("Hull City", "Hull", "ENG"),
    "Ipswich Town": ("Ipswich", "Ipswich", "ENG"),
    "Leeds United": ("Leeds", "Leeds", "ENG"),
    "Leicester City": ("Leicester", "Leicester", "ENG"),
    "Leyton Orient": ("Leyton Orient", "Londres", "ENG"),
    "Liverpool": ("Liverpool", "Liverpool", "ENG"),
    "Luton Town": ("Luton", "Luton", "ENG"),
    "Manchester City": ("Manchester City", "Manchester", "ENG"),
    "Manchester United": ("Manchester United", "Manchester", "ENG"),
    "Middlesbrough": ("Middlesbrough", "Middlesbrough", "ENG"),
    "Millwall": ("Millwall", "Londres", "ENG"),
    "Newcastle United": ("Newcastle", "Newcastle upon Tyne", "ENG"),
    "Northampton Town": ("Northampton", "Northampton", "ENG"),
    "Norwich City": ("Norwich", "Norwich", "ENG"),
    "Nottingham Forest": ("Nottingham Forest", "Nottingham", "ENG"),
    "Notts County": ("Notts County", "Nottingham", "ENG"),
    "Oldham Athletic": ("Oldham", "Oldham", "ENG"),
    "Oxford United": ("Oxford United", "Oxford", "ENG"),
    "Portsmouth": ("Portsmouth", "Portsmouth", "ENG"),
    "Preston North End": ("Preston", "Preston", "ENG"),
    "Queens Park Rangers": ("QPR", "Londres", "ENG"),
    "Reading": ("Reading", "Reading", "ENG"),
    "Sheffield United": ("Sheffield United", "Sheffield", "ENG"),
    "Sheffield Wednesday": ("Sheffield Wednesday", "Sheffield", "ENG"),
    "Southampton": ("Southampton", "Southampton", "ENG"),
    "Stoke City": ("Stoke City", "Stoke-on-Trent", "ENG"),
    "Sunderland": ("Sunderland", "Sunderland", "ENG"),
    "Swansea City": ("Swansea", "Swansea", "WAL"),
    "Swindon Town": ("Swindon", "Swindon", "ENG"),
    "Tottenham Hotspur": ("Tottenham", "Londres", "ENG"),
    "Watford": ("Watford", "Watford", "ENG"),
    "West Bromwich Albion": ("West Bromwich", "West Bromwich", "ENG"),
    "West Ham United": ("West Ham", "Londres", "ENG"),
    "Wigan Athletic": ("Wigan", "Wigan", "ENG"),
    "Wimbledon": ("Wimbledon", "Londres", "ENG"),               # o Wimbledon FC (1889-2004), não o AFC Wimbledon
    "Wolverhampton Wanderers": ("Wolverhampton", "Wolverhampton", "ENG"),
}

# grafias de outras fontes -> chave do engsoccerdata
ALIASES = {
    # football-data.co.uk
    "Bournemouth": "AFC Bournemouth", "Man United": "Manchester United", "Man City": "Manchester City",
    "Newcastle": "Newcastle United", "West Ham": "West Ham United", "Tottenham": "Tottenham Hotspur",
    "Wolves": "Wolverhampton Wanderers", "Brighton": "Brighton & Hove Albion", "West Brom": "West Bromwich Albion",
    "Leicester": "Leicester City", "Leeds": "Leeds United", "Norwich": "Norwich City", "Nott'm Forest": "Nottingham Forest",
    "Sheffield United": "Sheffield United", "Sheffield Weds": "Sheffield Wednesday", "QPR": "Queens Park Rangers",
    "Ipswich": "Ipswich Town", "Luton": "Luton Town", "Coventry": "Coventry City", "Swindon": "Swindon Town",
    "Oldham": "Oldham Athletic", "Blackburn": "Blackburn Rovers", "Bolton": "Bolton Wanderers", "Charlton": "Charlton Athletic",
    "Birmingham": "Birmingham City", "Wigan": "Wigan Athletic", "Hull": "Hull City", "Stoke": "Stoke City",
    "Swansea": "Swansea City", "Cardiff": "Cardiff City", "Huddersfield": "Huddersfield Town", "Derby": "Derby County",
    "Bradford": "Bradford City",
    # RSSSF (matriz e tabela)
    "Accrington": "Accrington F.C.", "Manchester Utd": "Manchester United", "Nottm Forest": "Nottingham Forest",
    "W.B.A.": "West Bromwich Albion", "WBA": "West Bromwich Albion", "Sheffield Wedn": "Sheffield Wednesday",
    "Sheffield Wed": "Sheffield Wednesday", "Sheffield Utd": "Sheffield United", "Newton Heath": "Manchester United",
    "Small Heath": "Birmingham City", "Woolwich Arsenal": "Arsenal", "The Arsenal": "Arsenal",
    "The Wednesday": "Sheffield Wednesday", "Birmingham": "Birmingham City",
    "Glossop": "Glossop North End", "Preston": "Preston North End", "Wolverhampton": "Wolverhampton Wanderers",
    "Q.P.R.": "Queens Park Rangers", "Queen's Park Rangers": "Queens Park Rangers", "Brighton & H.A.": "Brighton & Hove Albion",
    "Brighton & Hove A": "Brighton & Hove Albion", "Bradford PA": "Bradford Park Avenue", "Bradford P.A.": "Bradford Park Avenue",
    "Bradford Park Ave": "Bradford Park Avenue", "Bradford C": "Bradford City", "Orient": "Leyton Orient",
    "Grimsby": "Grimsby Town", "Northampton": "Northampton Town", "Carlisle": "Carlisle United", "Oxford": "Oxford United",
    "Oxford Utd": "Oxford United", "Newcastle Utd": "Newcastle United", "West Ham Utd": "West Ham United",
    "Leeds Utd": "Leeds United", "Tottenham H": "Tottenham Hotspur", "Spurs": "Tottenham Hotspur",
    "Birmingham C": "Birmingham City", "Leicester Fosse": "Leicester City", "Stoke": "Stoke City",
    "Wimbledon FC": "Wimbledon", "Middlesboro": "Middlesbrough", "Bournemouth AFC": "AFC Bournemouth",
    "Blackburn R": "Blackburn Rovers", "Bolton W": "Bolton Wanderers", "Bolton Wand": "Bolton Wanderers",
    "Bristol C": "Bristol City", "Cardiff C": "Cardiff City", "Derby Co": "Derby County", "Oldham A": "Oldham Athletic",
    "Preston NE": "Preston North End", "West Bromwich": "West Bromwich Albion",
    # erros de digitação das tabelas da RSSSF (2000/01, 2001/02, 2004/05, 2005/06)
    "Tottenham Hotspurs": "Tottenham Hotspur", "Charlton Atletic": "Charlton Athletic", "Wigan Athleitc": "Wigan Athletic",
    # ESPN e Wikipédia
    "Brighton and Hove Albion": "Brighton & Hove Albion", "Brighton & Hove Albion": "Brighton & Hove Albion",
    "Wolverhampton Wanderers": "Wolverhampton Wanderers", "AFC Bournemouth": "AFC Bournemouth",
    "Tottenham Hotspur": "Tottenham Hotspur",
}


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s.replace("&", "and"))


_INDICE = {chave(k): k for k in CLUBES} | {chave(k): v for k, v in ALIASES.items()}


def esd(nome: str) -> str | None:
    """Nome de qualquer fonte -> chave do engsoccerdata (None se não conhecer)."""
    return _INDICE.get(chave(nome.strip().rstrip("*").strip()))


def exibicao(nome_esd: str) -> str:
    return CLUBES[nome_esd][0]
