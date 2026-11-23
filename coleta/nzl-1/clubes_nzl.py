"""Identidade dos clubes da Nova Zelândia (nzl-1): cada grafia da RSSSF e do ogol vira um clube, com cidade e região.

Decisões (critério: o mesmo clube com outro nome é um clube só; fusão ou franquia nova é outro clube):
- "Auckland City" de 1972 é o Mt Albert-Ponsonby com outro nome (voltou ao nome antigo depois); o Auckland City de 2004 em
  diante é a franquia da NZFC, outro clube;
- Wellington Diamond United (1973-1984) e Wellington United (fusão com o Wellington City em 1985) são um clube só, como na
  contagem de títulos da RSSSF ("Wellington United 3", com 1976 e 1981);
- University-Mount Wellington (fusão do Mount Wellington com a Auckland University em 2000) entra como Mount Wellington, como
  na contagem da RSSSF ("Uni - Mt Wellington 6, includes Mt Wellington");
- Trans Tours United (1977) é o Christchurch United com nome de patrocinador; Courier Rangers (1978-1979) é o Rangers de
  Christchurch ("Christchurch Rangers", porque "Rangers" é o da Escócia);
- Otago United (2004-2012) mudou de nome para Southern United em 2013: um clube só, "Southern United";
- Waikato FC (2004-2013), WaiBOP United (2014-2015) e Hamilton Wanderers (2016 em diante) são franquias diferentes, uma no
  lugar da outra: três clubes;
- Waitakere City (clube, até 2003) e Waitakere United (franquia, 2004 em diante) são dois clubes, como na RSSSF;
- Christchurch City (2000-2001) é a fusão de Woolston e Christchurch Technical: outro clube; Cashmere Technical (2022 em
  diante) é outra fusão (Cashmere Wanderers e Christchurch Technical, 2014): outro clube;
- o time reserva do Wellington Phoenix ("Wellington Phoenix", "Wellington Phoenix U-20") é "Wellington Phoenix Reserves", e
  o do Auckland FC (2025) é "Auckland FC Reserves" (os times principais jogam a A-League, com o agente da Ásia);
- Wanderers SC (2013/14 e 2014/15) é o time sub-20 da federação.

Uso: clube(nome, ano) -> nome de exibição (ou None). ano = ano de início da temporada.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-oceania"))
from rsssf_oce import chave  # noqa: E402

# nome de exibição -> (cidade, região)
CLUBES: dict[str, tuple[str, str]] = {
    "Auckland City": ("Auckland", "Auckland"),
    "Auckland FC Reserves": ("Auckland", "Auckland"),
    "Auckland United": ("Auckland", "Auckland"),
    "Auckland University": ("Auckland", "Auckland"),
    "Bay Olympic": ("Auckland", "Auckland"),
    "Birkenhead United": ("Auckland", "Auckland"),
    "Blockhouse Bay": ("Auckland", "Auckland"),
    "Burnside": ("Christchurch", "Canterbury"),
    "Canterbury United": ("Christchurch", "Canterbury"),
    "Cashmere Technical": ("Christchurch", "Canterbury"),
    "Cashmere Wanderers": ("Christchurch", "Canterbury"),
    "Caversham": ("Dunedin", "Otago"),
    "Central United": ("Auckland", "Auckland"),
    "Christchurch City": ("Christchurch", "Canterbury"),
    "Christchurch Rangers": ("Christchurch", "Canterbury"),
    "Christchurch Technical": ("Christchurch", "Canterbury"),
    "Christchurch United": ("Christchurch", "Canterbury"),
    "Coastal Spirit": ("Christchurch", "Canterbury"),
    "Dunedin City": ("Dunedin", "Otago"),
    "Dunedin City Royals": ("Dunedin", "Otago"),
    "Dunedin Suburbs": ("Dunedin", "Otago"),
    "Dunedin Technical": ("Dunedin", "Otago"),
    "East Auckland": ("Auckland", "Auckland"),
    "East Coast Bays": ("Auckland", "Auckland"),
    "Eastern Suburbs": ("Auckland", "Auckland"),
    "Eden": ("Auckland", "Auckland"),
    "Ellerslie": ("Auckland", "Auckland"),
    "Fencibles United": ("Auckland", "Auckland"),
    "FC Twenty 11": ("Christchurch", "Canterbury"),
    "Ferrymead Bays": ("Christchurch", "Canterbury"),
    "Gisborne City": ("Gisborne", "Gisborne"),
    "Green Island": ("Dunedin", "Otago"),
    "Halswell United": ("Christchurch", "Canterbury"),
    "Hamilton AFC": ("Hamilton", "Waikato"),
    "Hamilton Wanderers": ("Hamilton", "Waikato"),
    "Havelock North Wanderers": ("Havelock North", "Hawke's Bay"),
    "Hawke's Bay United": ("Napier", "Hawke's Bay"),
    "Hungaria": ("Wellington", "Wellington"),
    "Hutt Valley United": ("Lower Hutt", "Wellington"),
    "Invercargill Thistle": ("Invercargill", "Southland"),
    "Island Bay United": ("Wellington", "Wellington"),
    "Lower Hutt City": ("Lower Hutt", "Wellington"),
    "Manawatu AFC": ("Palmerston North", "Manawatu-Whanganui"),
    "Manawatu United": ("Palmerston North", "Manawatu-Whanganui"),
    "Manukau United": ("Auckland", "Auckland"),
    "Manurewa": ("Auckland", "Auckland"),
    "Marlborough": ("Blenheim", "Marlborough"),
    "Melville United": ("Hamilton", "Waikato"),
    "Metro FC": ("Auckland", "Auckland"),
    "Miramar Rangers": ("Wellington", "Wellington"),
    "Mosgiel": ("Mosgiel", "Otago"),
    "Mount Maunganui": ("Mount Maunganui", "Bay of Plenty"),
    "Mount Wellington": ("Auckland", "Auckland"),
    "Mt Albert-Ponsonby": ("Auckland", "Auckland"),
    "Napier City Rovers": ("Napier", "Hawke's Bay"),
    "Nelson Suburbs": ("Nelson", "Nelson"),
    "Nelson United": ("Nelson", "Nelson"),
    "New Brighton": ("Christchurch", "Canterbury"),
    "New Plymouth Rangers": ("New Plymouth", "Taranaki"),
    "Nomads United": ("Christchurch", "Canterbury"),
    "North Shore United": ("Auckland", "Auckland"),
    "North Wellington": ("Wellington", "Wellington"),
    "Northern Hearts": ("Timaru", "Canterbury"),
    "Oratia United": ("Auckland", "Auckland"),
    "Papatoetoe": ("Auckland", "Auckland"),
    "Petone": ("Lower Hutt", "Wellington"),
    "Porirua United": ("Porirua", "Wellington"),
    "Roslyn-Wakari": ("Dunedin", "Otago"),
    "Selwyn United": ("Rolleston", "Canterbury"),
    "Southern United": ("Dunedin", "Otago"),
    "Southland": ("Invercargill", "Southland"),
    "Stop Out": ("Lower Hutt", "Wellington"),
    "Takapuna": ("Auckland", "Auckland"),
    "Takapuna City": ("Auckland", "Auckland"),
    "Tasman United": ("Nelson", "Nelson"),
    "Tauranga City": ("Tauranga", "Bay of Plenty"),
    "Tauranga City United": ("Tauranga", "Bay of Plenty"),
    "Tawa": ("Wellington", "Wellington"),
    "Team Otago": ("Dunedin", "Otago"),
    "Team Wellington": ("Wellington", "Wellington"),
    "University of Canterbury": ("Christchurch", "Canterbury"),
    "Upper Hutt City": ("Upper Hutt", "Wellington"),
    "WaiBOP United": ("Hamilton", "Waikato"),
    "Waiheke United": ("Auckland", "Auckland"),
    "Waikato FC": ("Hamilton", "Waikato"),
    "Waikato United": ("Hamilton", "Waikato"),
    "Waitakere City": ("Auckland", "Auckland"),
    "Waitakere United": ("Auckland", "Auckland"),
    "Wanaka": ("Wanaka", "Otago"),
    "Wanderers SC": ("Auckland", "Auckland"),
    "Waterside": ("Wellington", "Wellington"),
    "Waterside Karori": ("Wellington", "Wellington"),
    "Wellington City": ("Wellington", "Wellington"),
    "Wellington Olympic": ("Wellington", "Wellington"),
    "Wellington Phoenix Reserves": ("Wellington", "Wellington"),
    "Wellington United": ("Wellington", "Wellington"),
    "West Coast Rangers": ("Auckland", "Auckland"),
    "Western AFC": ("Christchurch", "Canterbury"),
    "Western Springs": ("Auckland", "Auckland"),
    "Western Suburbs": ("Porirua", "Wellington"),
    "Whanganui Athletic": ("Whanganui", "Manawatu-Whanganui"),
    "Woolston": ("Christchurch", "Canterbury"),
    "YoungHeart Manawatu": ("Palmerston North", "Manawatu-Whanganui"),
}

# (regex sobre chave(nome), nome de exibição, ano inicial, ano final); a primeira que casa vale
REGRAS: list[tuple[str, str, int, int]] = [
    (r"^auckland city$", "Mt Albert-Ponsonby", 1970, 1999),
    (r"^(auckland city|auckland)$", "Auckland City", 2004, 2100),
    (r"^auckland fc( reserves)?$", "Auckland FC Reserves", 2025, 2100),
    (r"^(m a p|mt albert ponsonby)$", "Mt Albert-Ponsonby", 1970, 2100),
    (r"^(university|auck university)$", "Auckland University", 1970, 2003),
    (r"^burnside( united)?$", "Burnside", 1900, 2100),
    (r"^canterbury( united( dragons)?)?$", "Canterbury United", 2002, 2100),
    (r"^canterbury w(oolston)?$", "Woolston", 1990, 2001),
    (r"^central( u| united| utd)?$", "Central United", 1990, 2100),
    (r"^christchurch( c| city)?$", "Christchurch City", 2000, 2001),
    (r"^christchurch t(ech(nical)?)?$", "Christchurch Technical", 1990, 2013),
    (r"^(christchurch (utd|united|u)|tt christchurch u|trans tours united)$", "Christchurch United", 1970, 2100),
    (r"^(courier rangers|rangers)$", "Christchurch Rangers", 1970, 1999),
    (r"^dunedin( t| tech| technical)?$", "Dunedin Technical", 1990, 2019),
    (r"^dunedin technical$", "Dunedin Technical", 1970, 2100),
    (r"^dunedin city$", "Dunedin City", 1970, 2019),
    (r"^e(ast)? auckland$", "East Auckland", 2003, 2003),
    (r"^hamilton$", "Hamilton AFC", 1970, 1999),
    (r"^hawke ?s bay( united)?$", "Hawke's Bay United", 2004, 2100),
    (r"^(hutt|hutty? city|lower hutt( city)?)$", "Lower Hutt City", 1990, 2100),
    (r"^hutt valley (utd|united)$", "Hutt Valley United", 1970, 2100),
    (r"^invercargill th(istle)?$", "Invercargill Thistle", 1970, 2100),
    (r"^manawatu( (utd|united))?$", "Manawatu United", 1970, 1998),
    (r"^manawatu( afc)?$", "Manawatu AFC", 1999, 2003),
    (r"^(m?manawatu( afc)?|youngheart manawatu)$", "YoungHeart Manawatu", 2004, 2012),
    (r"^melville( u| united)?$", "Melville United", 1970, 2100),
    (r"^metro( afc| mt albert)?$", "Metro FC", 1990, 2100),
    (r"^miramar( rangers)?$", "Miramar Rangers", 1970, 2100),
    (r"^(mt|mount) mau?nganui$", "Mount Maunganui", 1970, 2100),
    (r"^((mt|mount) wellington|uni mt wellington|university mt wellington)$", "Mount Wellington", 1970, 2002),
    (r"^napier( city( rovers)?)?$", "Napier City Rovers", 1970, 2100),
    (r"^nelson (utd|united)$", "Nelson United", 1970, 2100),
    (r"^nelson( suburbs)?$", "Nelson Suburbs", 1996, 2100),
    (r"^new plymouth( rangers)?$", "New Plymouth Rangers", 1970, 2100),
    (r"^north shore( u| utd| united)?$", "North Shore United", 1970, 2100),
    (r"^northern( hearts)?$", "Northern Hearts", 1999, 1999),
    (r"^(otago|otago united|southern united)$", "Southern United", 2004, 2100),
    (r"^porirua (utd|united)$", "Porirua United", 1970, 2100),
    (r"^takapuna$", "Takapuna", 2000, 2100),
    (r"^taurana$|^tauranga( city( united)?)?$", "Tauranga City United", 2001, 2003),
    (r"^tauranga city( utd| united)?$", "Tauranga City", 2004, 2100),
    (r"^team otago$", "Team Otago", 1990, 2003),
    (r"^(team )?wellington$", "Team Wellington", 2004, 2100),
    (r"^waibop( united)?$", "WaiBOP United", 2014, 2015),
    (r"^waikato( fc)?$", "Waikato FC", 2004, 2013),
    (r"^waikato( utd| united)?$", "Waikato United", 1970, 2003),
    (r"^(waitakere|wiatakere)( city| ciry)?$", "Waitakere City", 1970, 2003),
    (r"^waitakere( united)?$", "Waitakere United", 2004, 2100),
    (r"^wanderers (fc|sc)$", "Wanderers SC", 2013, 2014),
    (r"^(w|wh)anganui at(h)?letic$", "Whanganui Athletic", 1970, 2100),
    (r"^waterside karori$", "Waterside Karori", 1970, 2100),
    (r"^waterside$", "Waterside", 1970, 1987),
    (r"^(wellington d u|wellington d utd|wellington diamond utd|wellington diamond united|wellington (utd|united))$",
     "Wellington United", 1970, 2100),
    (r"^(wellington olympic|welington olympic|olympic)$", "Wellington Olympic", 1970, 2100),
    (r"^wellington phoenix( reserves| u 20)?$", "Wellington Phoenix Reserves", 2014, 2100),
    (r"^western s(uburbs)?$", "Western Suburbs", 1970, 2100),
    (r"^western$", "Western AFC", 1990, 1999),
    (r"^woolston( wmc)?$", "Woolston", 1970, 2001),
    (r"^halswell (utd|united)$", "Halswell United", 1970, 2100),
    (r"^(fc )?twenty 11$", "FC Twenty 11", 2000, 2100),
    (r"^south city royals$", "Dunedin City Royals", 2020, 2100),
    (r"^universities$", "University of Canterbury", 2025, 2025),
    (r"^canterbury utd$", "Canterbury United", 2002, 2100),
]

_NOMES_CHAVE = {chave(n): n for n in CLUBES}


def clube(nome: str, ano: int) -> str | None:
    k = chave(re.sub(r"\s*\([^)]*\)\s*$", "", nome))   # "Napier City Rovers (Napier)": a cidade sai
    k = re.sub(r" reservas$", " reserves", k)            # ogol: "Wellington Phoenix Reservas"
    for kk in (k, re.sub(r" (a?fc|sc)$", "", k), re.sub(r"\butd$", "united", k)):   # ogol: "Petone FC", "Manurewa AFC"
        for rx, nome_ex, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.match(rx, kk):
                return nome_ex
        if kk in _NOMES_CHAVE:
            return _NOMES_CHAVE[kk]
    return None
