"""Identidade dos clubes paraguaios: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido no Brasil ("Olimpia", "Cerro Porteño", "Libertad"); o Guaraní vira "Guaraní de
  Asunción" para não se confundir com o Guarani de Campinas;
- homônimo de clube do banco ou de outro pacote leva a cidade: "Nacional de Asunción" (o Nacional é o uruguaio), "River
  Plate de Asunción", "Sportivo San Lorenzo" (o San Lorenzo é o argentino), "Independiente de Campo Grande", "Universal de
  Encarnación";
- clubes diferentes com o mesmo nome: General Caballero (Zeballos Cué) e General Caballero JLM (Juan León Mallorquín);
  Cerro Porteño e Cerro Porteño PF (Presidente Franco).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-sulamerica"))
from rsssf_sul import chave  # noqa: E402

ASU = ("Asunción", "Asunción")
CEN = "Central"

# nome de exibição -> (cidade, departamento)
CLUBES: dict[str, tuple[str, str]] = {
    "Olimpia": ASU, "Cerro Porteño": ASU, "Libertad": ASU, "Guaraní de Asunción": ASU, "Nacional de Asunción": ASU, "Sol de América": ASU,
    "River Plate de Asunción": ASU, "Presidente Hayes": ASU, "Atlántida": ASU, "Atlético Colegiales": ASU, "Sport Colombia": ("Fernando de la Mora", CEN),
    "Sportivo Luqueño": ("Luque", CEN), "General Díaz": ("Luque", CEN), "Sportivo San Lorenzo": ("San Lorenzo", CEN),
    "Rubio Ñu": ASU, "Tacuary": ASU, "Sportivo Trinidense": ASU, "Deportivo Recoleta": ASU, "Silvio Pettirossi": ASU,
    "Sportivo Ameliano": ASU, "Resistencia": ASU, "Cerro Corá": ASU, "Atlético Tembetary": ("Ypané", CEN),
    "12 de Octubre": ("Itauguá", CEN), "3 de Febrero": ("Ciudad del Este", "Alto Paraná"), "2 de Mayo": ("Pedro Juan Caballero", "Amambay"),
    "General Caballero": ("Zeballos Cué", ASU[1]), "General Caballero JLM": ("Juan León Mallorquín", "Alto Paraná"),
    "Cerro Porteño PF": ("Presidente Franco", "Alto Paraná"), "Independiente de Campo Grande": ASU,
    "Deportivo Capiatá": ("Capiatá", CEN), "Deportivo Santaní": ("San Estanislao", "San Pedro"), "Fernando de la Mora": ("Fernando de la Mora", CEN),
    "Guaireña": ("Villarrica", "Guairá"), "Sportivo Carapeguá": ("Carapeguá", "Paraguarí"), "Universal de Encarnación": ("Encarnación", "Itapúa"),
    "Deportivo Humaitá": ("Mariano Roque Alonso", CEN), "Ovetense": ("Coronel Oviedo", "Caaguazú"),
    "Guaraní de Coronel Oviedo": ("Coronel Oviedo", "Caaguazú"), "Cerro Porteño de Ciudad del Este": ("Ciudad del Este", "Alto Paraná"),
    "Deportivo Boquerón": ("Ciudad del Este", "Alto Paraná"), "Capitán Figari": ("Lambaré", CEN),
}

REGRAS: list[tuple[str, str, int, int]] = [
    (r"(club )?olimpia( asuncion)?", "Olimpia", 1902, 2100),
    (r"cerro porteno (pf|de franco|\(?pf\)?)|cerro porteno \(pf\)", "Cerro Porteño PF", 2000, 2100),
    (r"cerro porteno cd este", "Cerro Porteño de Ciudad del Este", 1990, 2100),
    (r"(dep |deportivo )?boqueron", "Deportivo Boquerón", 1990, 2100),
    (r"(c |cerro )?p(orte[nñ]o)?$|c porteno|cerro porteno|cerro p$", "Cerro Porteño", 1912, 2100),
    (r"cerro c(ora)?( campo grande)?|c cora", "Cerro Corá", 1980, 2100),
    (r"libertad", "Libertad", 1905, 2100),
    (r"guarani coronel oviedo", "Guaraní de Coronel Oviedo", 1990, 2100),
    (r"guarani", "Guaraní de Asunción", 1903, 2100),
    (r"nacional", "Nacional de Asunción", 1904, 2100),
    (r"sol( de america)?", "Sol de América", 1909, 2100),
    (r"river( plate)?", "River Plate de Asunción", 1911, 2100),
    (r"(p |presidente )hayes|p ?hayes", "Presidente Hayes", 1907, 2100),
    (r"atlantida", "Atlántida", 1906, 2100),
    (r"(at |atletico )?colegiales", "Atlético Colegiales", 1977, 2100),
    (r"(sport )?colombia", "Sport Colombia", 1924, 2100),
    (r"(sp |sportivo )?luque[nñ]o", "Sportivo Luqueño", 1921, 2100),
    (r"(gral |general )d[ií]az", "General Díaz", 1905, 2100),
    (r"(sp |sportivo |s )?san lorenzo|s lorenzo", "Sportivo San Lorenzo", 1930, 2100),
    (r"rubio [nñ]u", "Rubio Ñu", 1913, 2100),
    (r"tac(u|au)a?ry", "Tacuary", 1923, 2100),
    (r"(sp |sportivo )?trinidense", "Sportivo Trinidense", 1935, 2100),
    (r"(dep |deportivo )?recoleta", "Deportivo Recoleta", 1931, 2100),
    (r"(silvio )?pettirossi", "Silvio Pettirossi", 1926, 2100),
    (r"(sportivo )?ameliano", "Sportivo Ameliano", 1936, 2100),
    (r"resistencia( sc)?", "Resistencia", 1917, 2100),
    (r"(atl |atletico )?tembetary", "Atlético Tembetary", 1942, 2100),
    (r"12 (de )?octubre", "12 de Octubre", 1914, 2100),
    (r"3 de febrero", "3 de Febrero", 1970, 2100),
    (r"2 de mayo", "2 de Mayo", 1935, 2100),
    (r"(gral |general )caballero (jlm|de juan leon mallorquin)", "General Caballero JLM", 1960, 2100),
    (r"(gral |general )caballero( zc| \(?zc\)?)?", "General Caballero", 1918, 2100),
    (r"independiente( cg| \(?cg\)?| fbc| de campo grande)?", "Independiente de Campo Grande", 1925, 2100),
    (r"(deportivo )?capiata", "Deportivo Capiatá", 2008, 2100),
    (r"(deportivo )?santani", "Deportivo Santaní", 2000, 2100),
    (r"fernando de la mora", "Fernando de la Mora", 1960, 2100),
    (r"guairena", "Guaireña", 2000, 2100),
    (r"(sp |sportivo )?carapegua", "Sportivo Carapeguá", 2000, 2100),
    (r"universal( encarnacion)?", "Universal de Encarnación", 1990, 2100),
    (r"(dep |deportivo )?humaita", "Deportivo Humaitá", 1980, 2100),
    (r"ovetense", "Ovetense", 1950, 2100),
    (r"(cap |capitan )figari", "Capitán Figari", 1950, 2100),
]

_LIXO = re.compile(r"\s*\((?:asunci[oó]n|\d-\d pen)\)\s*$|\s+asuncion$|\s+as$|\s*-\s*-\s*$", re.I)


def _regra(k: str, ano: int) -> str | None:
    for kk in (k, re.sub(r"^(club|c|cd|csd) ", "", k)):
        for rx, exib, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.match(rx + r"(?:\b|$)", kk):
                return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    return _regra(chave(_LIXO.sub("", nome.strip())), ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
