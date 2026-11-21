"""Identidade dos clubes chilenos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido no Brasil ("Colo Colo", "Universidad de Chile", "Universidad Católica", "Cobreloa");
- homônimo de clube do banco ou de outro pacote leva a cidade: "Everton de Viña del Mar" (o Everton inglês está no eng-1),
  "Rangers de Talca", "Naval de Talcahuano";
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte: Green Cross (Santiago até
  1964) -> Green Cross-Temuco (1965) -> Deportes Temuco (1985), como a RSSSF conta o título de 1945; Unión Calera -> Unión La
  Calera; Municipal Iquique -> Deportes Iquique; Provincial Curicó Unido -> Curicó Unido;
- fusões que criaram clube novo ficam separadas: Ferroviarios e Badminton (até 1949) e Ferrobádminton (1950).

A lista de tabelas finais (chilehist.html) põe os pontos de bônus entre parênteses no nome ("Colo Colo (2)"): saem antes da
regra. REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-sulamerica"))
from rsssf_sul import chave  # noqa: E402

RM = "Metropolitana de Santiago"
STG = ("Santiago", RM)

# nome de exibição -> (cidade, região)
CLUBES: dict[str, tuple[str, str]] = {
    "Colo Colo": STG, "Universidad de Chile": STG, "Universidad Católica": STG, "Unión Española": STG, "Audax Italiano": STG,
    "Palestino": STG, "Magallanes": STG, "Santiago Morning": STG, "Badminton": STG, "Ferroviarios": STG, "Ferrobádminton": STG,
    "Santiago National": STG, "Morning Star": STG, "Carlos Walker": STG, "Deportivo Alemán": STG, "Iberia": STG,
    "Metropolitano de Santiago": STG, "Santiago FC": STG, "Deportes Aviación": STG, "Deportes Barnechea": ("Lo Barnechea", RM),
    "Deportes Melipilla": ("Melipilla", RM),
    "Everton de Viña del Mar": ("Viña del Mar", "Valparaíso"), "Santiago Wanderers": ("Valparaíso", "Valparaíso"),
    "San Luis de Quillota": ("Quillota", "Valparaíso"), "Unión La Calera": ("La Calera", "Valparaíso"),
    "Unión San Felipe": ("San Felipe", "Valparaíso"), "Trasandino": ("Los Andes", "Valparaíso"),
    "Deportes Limache": ("Limache", "Valparaíso"),
    "Cobreloa": ("Calama", "Antofagasta"), "Deportes Antofagasta": ("Antofagasta", "Antofagasta"),
    "Cobresal": ("El Salvador", "Atacama"), "Regional Atacama": ("Copiapó", "Atacama"), "Deportes Copiapó": ("Copiapó", "Atacama"),
    "Deportes Iquique": ("Iquique", "Tarapacá"), "Deportes Arica": ("Arica", "Arica y Parinacota"),
    "San Marcos de Arica": ("Arica", "Arica y Parinacota"),
    "Coquimbo Unido": ("Coquimbo", "Coquimbo"), "Deportes La Serena": ("La Serena", "Coquimbo"), "Deportes Ovalle": ("Ovalle", "Coquimbo"),
    "O'Higgins": ("Rancagua", "O'Higgins"), "Unión Santa Cruz": ("Santa Cruz", "O'Higgins"),
    "Rangers de Talca": ("Talca", "Maule"), "Curicó Unido": ("Curicó", "Maule"), "Deportes Linares": ("Linares", "Maule"),
    "Ñublense": ("Chillán", "Ñuble"),
    "Huachipato": ("Talcahuano", "Biobío"), "Naval de Talcahuano": ("Talcahuano", "Biobío"), "Deportes Concepción": ("Concepción", "Biobío"),
    "Universidad de Concepción": ("Concepción", "Biobío"), "Fernández Vial": ("Concepción", "Biobío"), "Lota Schwager": ("Coronel", "Biobío"),
    "Deportes Temuco": ("Temuco", "Araucanía"), "Deportes Valdivia": ("Valdivia", "Los Ríos"),
    "Provincial Osorno": ("Osorno", "Los Lagos"), "Deportes Puerto Montt": ("Puerto Montt", "Los Lagos"),
}

REGRAS: list[tuple[str, str, int, int]] = [
    (r"colo ?colo", "Colo Colo", 1925, 2100),
    (r"(u|univ|universidad) ?(de )?chile", "Universidad de Chile", 1927, 2100),
    (r"(u|univ|universidad) ?catolica", "Universidad Católica", 1937, 2100),
    (r"(u|univ|universidad) (de )?concepcion", "Universidad de Concepción", 1994, 2100),
    (r"(u|union) ?(deportiva )?espa[nñ]ola", "Unión Española", 1920, 2100),
    (r"(a|audax) ?(i|italiano)\b", "Audax Italiano", 1920, 2100),
    (r"palestin[oa]", "Palestino", 1920, 2100),
    (r"magallanes", "Magallanes", 1900, 2100),
    (r"(s|stgo|santiago) ?morning", "Santiago Morning", 1930, 2100),
    (r"(s|stgo|santiago) ?wanderers|wanderers", "Santiago Wanderers", 1930, 2100),
    (r"(santiago )?(n|nat|national)( juventus)?$|santiago national", "Santiago National", 1900, 1960),
    (r"santiago$", "Santiago FC", 1930, 1940),
    (r"morning star", "Morning Star", 1930, 1940),
    (r"carlos walker", "Carlos Walker", 1930, 1940),
    (r"deportivo aleman", "Deportivo Alemán", 1930, 1940),
    (r"ferrobadminton", "Ferrobádminton", 1950, 1970),
    (r"ferroviarios", "Ferroviarios", 1930, 1949),
    (r"badminton", "Badminton", 1930, 1949),
    (r"iberia", "Iberia", 1930, 1960),
    (r"metropolitano", "Metropolitano de Santiago", 1930, 1945),
    (r"(deportes )?aviacion", "Deportes Aviación", 1950, 1985),
    (r"(deportes )?barnechea", "Deportes Barnechea", 2000, 2100),
    (r"(dep|deportes) ?melipilla|melipilla", "Deportes Melipilla", 1990, 2100),
    (r"everton", "Everton de Viña del Mar", 1930, 2100),
    (r"san luis", "San Luis de Quillota", 1950, 2100),
    (r"(u|union) ?(la )?calera", "Unión La Calera", 1955, 2100),
    (r"(u|union) ?san felipe|san felipe", "Unión San Felipe", 1955, 2100),
    (r"trasandino", "Trasandino", 1950, 2100),
    (r"(deportes )?limache", "Deportes Limache", 2000, 2100),
    (r"cobreloa", "Cobreloa", 1977, 2100),
    (r"cobresal", "Cobresal", 1979, 2100),
    (r"(deportes |regional )?antofagasta", "Deportes Antofagasta", 1965, 2100),
    (r"(regional )?atacama", "Regional Atacama", 1979, 2000),
    (r"(deportes )?copiapo", "Deportes Copiapó", 2000, 2100),
    (r"(dep|deportes|municipal) ?iquique|iquique", "Deportes Iquique", 1978, 2100),
    (r"(cd )?san marcos( de arica)?", "San Marcos de Arica", 1978, 2100),
    (r"(deportes )?arica", "Deportes Arica", 1975, 2100),
    (r"coquimbo( u| unido)?", "Coquimbo Unido", 1958, 2100),
    (r"(dep|deportes) ?la serena|la serena", "Deportes La Serena", 1955, 2100),
    (r"(deportes )?ovalle", "Deportes Ovalle", 1965, 2100),
    (r"o ?h?iggins", "O'Higgins", 1955, 2100),
    (r"union santa cruz", "Unión Santa Cruz", 1980, 2100),
    (r"rangers", "Rangers de Talca", 1950, 2100),
    (r"(prov |provincial )?curico unido", "Curicó Unido", 1975, 2100),
    (r"(deportes )?linares", "Deportes Linares", 1960, 2100),
    (r"nublense", "Ñublense", 1960, 2100),
    (r"huachipato", "Huachipato", 1960, 2100),
    (r"naval|los nauticos", "Naval de Talcahuano", 1960, 2100),
    (r"(dep|deportes|deportivo) ?concpe?cion|(dep|deportes|deportivo) ?concepcion|concepcion", "Deportes Concepción", 1965, 2100),
    (r"(arturo )?fernandez vial", "Fernández Vial", 1960, 2100),
    (r"lota schwager", "Lota Schwager", 1965, 2100),
    (r"green cross( temuco)?|(dep|deportes|deportivo) ?temuco|temuco", "Deportes Temuco", 1930, 2100),
    (r"(deportes )?valdivia", "Deportes Valdivia", 1980, 2100),
    (r"(prov |provincial )?osorno", "Provincial Osorno", 1980, 2100),
    (r"(deportes |pto )?puerto montt|pto montt", "Deportes Puerto Montt", 1980, 2100),
]

_BONUS = re.compile(r"\s*\(\s*\d+(\s+bonus points?)?\s*\)\s*$|\s*\(\*\)\s*$", re.I)


def _regra(k: str, ano: int) -> str | None:
    for kk in (k, re.sub(r"^(club|c|cd|cs|csd) ", "", k)):
        for rx, exib, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.match(rx + r"(?:\b|$)", kk):
                return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    nome = _BONUS.sub("", nome)
    return _regra(chave(nome), ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
