"""Identidade dos clubes equatorianos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido no Brasil ("Emelec", "LDU de Quito", "Independiente del Valle", "El Nacional");
- homônimo de clube do banco ou de outro pacote leva a cidade: "Barcelona de Guayaquil" (o Barcelona é o espanhol),
  "Universidad Católica de Quito" (a Universidad Católica é a chilena), "River Plate de Manta" (1963, 1966) e "River Plate
  de Riobamba" (1987, 1988), dois clubes diferentes (Wikipédia em espanhol), "Libertad de Loja",
  "Santos de El Guabo", "Juventus de Esmeraldas", "Santa Rita de Vinces"; os Américas de Quito, Ambato e Manta levam a cidade;
- o mesmo clube com outro nome em outra época fica com o nome atual: Independiente José Terán (até 2014) é o Independiente
  del Valle; River Ecuador (2015-2016) é o Guayaquil City; Cuniburo (até 2025) é o Vinotinto; Manta Sport Club ("Manta SC",
  "Manta Sport") é um só clube, diferente do Manta FC (fundado em 1998);
- clubes diferentes com o mesmo nome: LDU de Quito, LDU de Portoviejo, LDU de Cuenca e LDU de Loja; UD Valdez (Milagro, 1978)
  e Valdez SC (Milagro, 1991-1994, que recebeu a vaga do Filanbanco); "LDU" e "Deportivo" sozinhos, nas páginas de
  1997-2002, dependem do ano (regras abaixo, conferidas com as tabelas da página).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-sulamerica"))
from rsssf_sul import chave  # noqa: E402

GYE = ("Guayaquil", "Guayas")
UIO = ("Quito", "Pichincha")
AMB = ("Ambato", "Tungurahua")
MEC = ("Manta", "Manabí")

# nome de exibição -> (cidade, província)
CLUBES: dict[str, tuple[str, str]] = {
    # Guayaquil e Guayas
    "Barcelona de Guayaquil": GYE, "Emelec": GYE, "9 de Octubre": GYE, "Everest": GYE, "Patria": GYE, "Español": GYE,
    "Norte América": GYE, "Estibadores Navales": GYE, "Guayaquil Sport": GYE, "Panamá": GYE, "Guayaquil City": GYE,
    "Filanbanco": GYE, "UD Valdez": ("Milagro", "Guayas"), "Valdez SC": ("Milagro", "Guayas"),
    # Quito e Pichincha
    "LDU de Quito": UIO, "El Nacional": UIO, "Deportivo Quito": UIO, "Aucas": UIO, "Universidad Católica de Quito": UIO,
    "América de Quito": UIO, "España": UIO, "Politécnico": UIO, "Espoli": UIO, "Cumbayá": UIO,
    "Independiente del Valle": ("Sangolquí", "Pichincha"), "Clan Juvenil": ("Sangolquí", "Pichincha"),
    "Vinotinto": UIO,
    # Serra
    "Macará": AMB, "Técnico Universitario": AMB, "América de Ambato": AMB, "Mushuc Runa": AMB, "Brasil de Ambato": AMB,
    "Olmedo": ("Riobamba", "Chimborazo"), "Atlético Riobamba": ("Riobamba", "Chimborazo"),
    "River Plate de Riobamba": ("Riobamba", "Chimborazo"),
    "Deportivo Cuenca": ("Cuenca", "Azuay"), "LDU de Cuenca": ("Cuenca", "Azuay"), "Gualaceo": ("Gualaceo", "Azuay"),
    "Deportivo Azogues": ("Azogues", "Cañar"), "Deportivo Cotopaxi": ("Latacunga", "Cotopaxi"),
    "Deportivo Saquisilí": ("Saquisilí", "Cotopaxi"), "Imbabura": ("Ibarra", "Imbabura"),
    "LDU de Loja": ("Loja", "Loja"), "Libertad de Loja": ("Loja", "Loja"),
    # Costa
    "LDU de Portoviejo": ("Portoviejo", "Manabí"), "Manta Sport": MEC, "Manta FC": MEC, "Delfín": MEC, "Green Cross": MEC,
    "América de Manta": MEC, "Juventud Italiana": MEC, "Inecel": MEC, "River Plate de Manta": MEC,
    "Audaz Octubrino": ("Machala", "El Oro"), "Carmen Mora": ("Machala", "El Oro"), "Bonita Banana": ("Machala", "El Oro"),
    "Orense": ("Machala", "El Oro"), "Fuerza Amarilla": ("Machala", "El Oro"), "Calvi": ("Machala", "El Oro"), "Santos de El Guabo": ("El Guabo", "El Oro"),
    "Esmeraldas Petrolero": ("Esmeraldas", "Esmeraldas"), "Juventus de Esmeraldas": ("Esmeraldas", "Esmeraldas"),
    "Juvenil de Esmeraldas": ("Esmeraldas", "Esmeraldas"), "UD Juvenil": ("Quinindé", "Esmeraldas"),
    "Deportivo Quevedo": ("Quevedo", "Los Ríos"), "Santa Rita de Vinces": ("Vinces", "Los Ríos"),
}

REGRAS: list[tuple[str, str, int, int]] = [
    # nomes curtos que dependem do ano (páginas de 1996-2002)
    (r"ldu$", "LDU de Portoviejo", 2001, 2001),   # a LDU de Quito jogou a Serie B em 2001
    (r"ldu$", "LDU de Quito", 1997, 2002),
    (r"nacional$", "El Nacional", 1990, 2002),
    (r"cuenca$", "Deportivo Cuenca", 1990, 2002),
    (r"portoviejo$", "LDU de Portoviejo", 1990, 2002),
    (r"quevedo$", "Deportivo Quevedo", 1990, 2002),
    (r"petrolero$", "Esmeraldas Petrolero", 1990, 2002),
    (r"tecnico$", "Técnico Universitario", 1990, 2002),
    (r"g cross", "Green Cross", 1990, 2002),
    (r"deportivo$", "Deportivo Quevedo", 1999, 1999),
    (r"deportivo$", "Deportivo Quito", 2000, 2001),
    # Guayaquil
    (r"(bsc )?barcelona( sc| sporting club)?( guayaquil)?|barelona", "Barcelona de Guayaquil", 1925, 2100),
    (r"(cs )?emelec", "Emelec", 1929, 2100),
    (r"(9|nueve) de octubre", "9 de Octubre", 1912, 2100),
    (r"everest", "Everest", 1931, 2100),
    (r"patria", "Patria", 1908, 2100),
    (r"espanol", "Español", 1950, 2100),
    (r"norte america", "Norte América", 1940, 2100),
    (r"estibadores navales", "Estibadores Navales", 1950, 2100),
    (r"guayaquil sport", "Guayaquil Sport", 1950, 2100),
    (r"panama", "Panamá", 1990, 2100),
    (r"guayaquil city( fc)?|river ecuador", "Guayaquil City", 2007, 2100),
    (r"fi?anbanco|filanbanco", "Filanbanco", 1979, 1991),
    (r"ud valdez|valdez$", "UD Valdez", 1970, 1985),
    (r"valdez( sc)?", "Valdez SC", 1991, 2100),
    # Quito
    (r"ldu( de)? quito|liga( deportiva universitaria)?( de)? quito", "LDU de Quito", 1930, 2100),
    (r"(club deportivo )?el nacional|nacional quito", "El Nacional", 1964, 2100),
    (r"dep(ortivo)? quito|sociedad deportivo quito", "Deportivo Quito", 1955, 2100),
    (r"(sd )?aucas", "Aucas", 1945, 2100),
    (r"univ(ersidad|erisdad)? catn?o?lica( quito| ecuador)?|u catolica|universidad catolica del ecuador|univ catlica|universidad catlica",
     "Universidad Católica de Quito", 1963, 2100),
    (r"america( de)? quito|america q|amrica q", "América de Quito", 1939, 2100),
    (r"america( de)? ambato|america a", "América de Ambato", 1940, 2100),
    (r"america( de)? manta", "América de Manta", 1940, 2100),
    (r"america", "América de Quito", 1939, 2100),
    (r"espana", "España", 1950, 1970),
    (r"politecnico", "Politécnico", 1950, 2100),
    (r"espoli", "Espoli", 1986, 2100),
    (r"cumbaya( fc)?", "Cumbayá", 2009, 2100),
    (r"indep(endiente)? (del valle|(jose )?teran)", "Independiente del Valle", 1958, 2100),
    (r"clan juvenil", "Clan Juvenil", 2009, 2100),
    (r"vinotinto( fc)?|cuniburo( fc)?", "Vinotinto", 2010, 2100),
    # serra
    (r"macar(a)?", "Macará", 1939, 2100),
    (r"(tecnico|tecnivo|tenico|tcnico|tec) univ(ersitario)?|tecnico u$", "Técnico Universitario", 1971, 2100),
    (r"mushuc runa( sc)?", "Mushuc Runa", 2003, 2100),
    (r"brasil", "Brasil de Ambato", 1960, 1980),
    (r"(cd )?olmedo", "Olmedo", 1919, 2100),
    (r"atletico riobamba", "Atlético Riobamba", 1960, 2100),
    (r"river plate", "River Plate de Manta", 1950, 1970),     # 1963 e 1966 (a RSSSF põe "[Riobamba]" em 1963)
    (r"river plate", "River Plate de Riobamba", 1971, 2000),  # 1987 e 1988
    (r"dep(ortivo|rotivo)? cuenca", "Deportivo Cuenca", 1971, 2100),
    (r"ldu de cuenca", "LDU de Cuenca", 1960, 2100),
    (r"gualaceo( sc)?", "Gualaceo", 2000, 2100),
    (r"deportivo azogues", "Deportivo Azogues", 2000, 2100),
    (r"dep(ortivo)? cotopaxi", "Deportivo Cotopaxi", 1970, 2100),
    (r"dep(ortivo)? saquisili", "Deportivo Saquisilí", 1990, 2100),
    (r"imbabura( s ?c)?", "Imbabura", 1990, 2100),
    (r"ldu( de)? loja|liga de loja", "LDU de Loja", 1979, 2100),
    (r"libertad( fc)?", "Libertad de Loja", 2017, 2100),
    # costa
    (r"ldu( de)? portoviejo|liga de portoviejo", "LDU de Portoviejo", 1969, 2100),
    (r"manta (sc|sport)|manta$", "Manta Sport", 1940, 1997),
    (r"manta( f ?c)?", "Manta FC", 1998, 2100),
    (r"delfin( sc)?", "Delfín", 1989, 2100),
    (r"green cross", "Green Cross", 1980, 2100),
    (r"juventud italiana", "Juventud Italiana", 1950, 2100),
    (r"inecel", "Inecel", 1960, 2100),
    (r"audaz octubrino", "Audaz Octubrino", 1960, 2100),
    (r"carmen mora", "Carmen Mora", 1960, 2100),
    (r"bonita banana", "Bonita Banana", 1960, 2100),
    (r"orense( sc)?", "Orense", 2009, 2100),
    (r"fuerza amarilla( sc)?", "Fuerza Amarilla", 1999, 2100),
    (r"calvi", "Calvi", 1990, 2100),
    (r"santos", "Santos de El Guabo", 1990, 2000),
    (r"esm(eraldas)? petrolero+", "Esmeraldas Petrolero", 1970, 2100),
    (r"juventus", "Juventus de Esmeraldas", 1980, 2100),
    (r"juvenil$", "Juvenil de Esmeraldas", 1980, 1995),
    (r"ud juvenil|quininde", "UD Juvenil", 1996, 2100),
    (r"dep(ortivo)? quevedo", "Deportivo Quevedo", 1970, 2100),
    (r"santas? rita", "Santa Rita de Vinces", 1990, 2100),
]

_LIXO = re.compile(r"^\s*[-/]\s*|\s*-\s*$|\[\[|\]\]", re.I)


def _regra(k: str, ano: int) -> str | None:
    for kk in (k, re.sub(r"^(club|c|cd|csd|sd) ", "", k)):
        for rx, exib, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.fullmatch(f"(?:{rx})" + r"(?:\s.*)?", kk):
                return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    return _regra(chave(_LIXO.sub("", nome.strip())), ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
