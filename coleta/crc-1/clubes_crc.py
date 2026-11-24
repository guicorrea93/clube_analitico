"""Identidade dos clubes da 1ª divisão da Costa Rica: cada grafia -> nome de exibição único no mundo.

Regras (docs/agentes-internacionais-COMECE-AQUI.md, seção 4), decididas em 24/11/2026:
- nome pelo qual o clube é conhecido (Saprissa, Alajuelense, Herediano, Cartaginés), com as grafias de cada época ("LD
  Alajuelense", "L.D.Alajuela", "Alajuela" nos anos 1990; "CS Herediano", "Heredia"; "Cartago");
- o mesmo clube com outro nome, como na lista de campeões da RSSSF: Carmen FC / El Carmen = Carmelita; CS Uruguay = Uruguay de
  Coronado; Univ. de Costa Rica / UCR / Universidad = Universidad de Costa Rica; A.D. Belemita / Belén Siglo XXI / Belén FC =
  Belén; San Ramón = Ramonense; Guanacaste = Guanacasteca; Liberia Mía (2004-2012, o nome do AD Municipal Liberia
  nesses anos; campeão do Clausura 2009) = Municipal Liberia;
- clubes diferentes: Municipal Puntarenas (até 2003) e Puntarenas FC (2004 em diante), contados à parte na lista de campeões;
  Gimnástica Limonense (1921), Limonense (AD Limonense, 1964-2001), Municipal Limón (1980-1983), Limón Northern (1984-1988) e
  Limón FC (2010 em diante); Alajuela Junior (1933-1936) e Alajuelense;
- homônimo de clube do banco ou de outro pacote leva a cidade: Santos de Guápiles, Sporting de San José, Uruguay de Coronado,
  Progreso de San José, Paraíso de Cartago.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-concacaf"))
from rsssf_concacaf import chave  # noqa: E402

SJ = ("San José", "San José")
_C = lambda c, p: (c, p, "CRC")   # noqa: E731
CLUBES: dict[str, tuple[str, str, str]] = {
    "Herediano": _C("Heredia", "Heredia"), "Alajuelense": _C("Alajuela", "Alajuela"), "Cartaginés": _C("Cartago", "Cartago"),
    "Saprissa": _C("Tibás", "San José"), "La Libertad": _C(*SJ), "La Unión de Tres Ríos": _C("Tres Ríos", "Cartago"),
    "Gimnástica Española": _C(*SJ), "Gimnástica Limonense": _C("Limón", "Limón"), "Progreso de San José": _C(*SJ), "Once Tigres": _C(*SJ),
    "Juventud": _C(*SJ), "Corsarios": _C(*SJ), "Costa Rica FC": _C(*SJ), "Orión": _C(*SJ), "Buenos Aires": _C(*SJ),
    "CS México": _C(*SJ), "Hispano Atlético": _C(*SJ), "Alajuela Junior": _C("Alajuela", "Alajuela"), "Moravia": _C("Moravia", "San José"),
    "Universidad de Costa Rica": _C("San Pedro", "San José"), "Carmelita": _C("Alajuela", "Alajuela"),
    "Uruguay de Coronado": _C("Coronado", "San José"), "Barrio México": _C(*SJ), "Limonense": _C("Limón", "Limón"),
    "Municipal Puntarenas": _C("Puntarenas", "Puntarenas"), "Puntarenas FC": _C("Puntarenas", "Puntarenas"),
    "Nicolás Marín": _C(*SJ), "Turrialba": _C("Turrialba", "Cartago"), "San Carlos": _C("Ciudad Quesada", "Alajuela"),
    "Ramonense": _C("San Ramón", "Alajuela"), "Municipal Limón": _C("Limón", "Limón"), "San Miguel": _C("Desamparados", "San José"),
    "Municipal San José": _C(*SJ), "Sagrada Familia": _C(*SJ), "Limón Northern": _C("Limón", "Limón"),
    "Curridabat": _C("Curridabat", "San José"), "Guanacasteca": _C("Nicoya", "Guanacaste"), "Palmares": _C("Palmares", "Alajuela"),
    "Municipal Generaleña": _C("San Isidro de El General", "San José"), "Pérez Zeledón": _C("San Isidro de El General", "San José"),
    "Belén": _C("Belén", "Heredia"), "Goicoechea": _C("Guadalupe", "San José"), "Municipal Liberia": _C("Liberia", "Guanacaste"),
"Santa Bárbara": _C("Santa Bárbara", "Heredia"),
    "Santos de Guápiles": _C("Guápiles", "Limón"), "Osa": _C("Ciudad Cortés", "Puntarenas"), "Brujas de Escazú": _C("Escazú", "San José"),
    "Santacruceña": _C("Santa Cruz", "Guanacaste"), "Águilas Guanacastecas": _C("Liberia", "Guanacaste"),
    "Limón FC": _C("Limón", "Limón"), "Puma Generaleña": _C("San Isidro de El General", "San José"),
    "Grecia": _C("Grecia", "Alajuela"), "Guadalupe": _C("Guadalupe", "San José"), "Jicaral": _C("Jicaral", "Puntarenas"),
    "Sporting de San José": _C(*SJ), "Santa Ana": _C("Santa Ana", "San José"), "Cariari Pococí": _C("Cariari", "Limón"),
    "Naranjeña": _C("Naranjo", "Alajuela"), "Orotinense": _C("Orotina", "Alajuela"), "Paraíso de Cartago": _C("Paraíso", "Cartago"),
    "Puriscal": _C("Puriscal", "San José"), "Quepos": _C("Quepos", "Puntarenas"), "Vecinos": _C(*SJ),
    "Ciudad Colón": _C("Ciudad Colón", "San José"), "Tournón": _C(*SJ),
}

REGRAS: list[tuple[str, str, int, int]] = [
    (r"(cs |c s )?herediano|heredia", "Herediano", 1921, 2100),
    (r"alajuela junior", "Alajuela Junior", 1921, 1940),
    (r"(ld |l d )?alajuel(ense|a)", "Alajuelense", 1921, 2100),
    (r"(cs |cd |c d )?cart(a|e)gin(e|é)s|cartago", "Cartaginés", 1921, 2100),
    (r"(cd |dep(ortivo)? )?saprissa", "Saprissa", 1935, 2100),
    (r"(cs )?la libertad", "La Libertad", 1921, 1970),
    (r"(cs )?la union", "La Unión de Tres Ríos", 1921, 2100),
    (r"(sg |sociedad )?(gimnastica )?espanola", "Gimnástica Española", 1921, 1970),
    (r"sg limonense", "Gimnástica Limonense", 1921, 1930),
    (r"(cs )?progreso", "Progreso de San José", 1921, 1930), (r"(cs )?once tigres", "Once Tigres", 1921, 1930),
    (r"juventud", "Juventud", 1921, 1935), (r"corsarios( fc)?", "Corsarios", 1921, 1935),
    (r"costa rica", "Costa Rica FC", 1921, 1930), (r"orion( fc)?", "Orión", 1921, 2100),
    (r"buenos aires", "Buenos Aires", 1921, 1940), (r"(cs )?mexico", "CS México", 1930, 1940),
    (r"hispano atletico", "Hispano Atlético", 1930, 1940), (r"(ud )?moravia", "Moravia", 1921, 1960),
    (r"univ(ersidad)?( de costa rica)?|ucr", "Universidad de Costa Rica", 1921, 2100),
    (r"(ad )?(carmen( fc)?|el carmen|carmelita|carmelota)", "Carmelita", 1921, 2100),
    (r"(cs )?uruguay( coronado| de coronado)?", "Uruguay de Coronado", 1921, 2100),
    (r"(ad )?barrio mexico|dep mexico", "Barrio México", 1940, 2100),
    (r"(ad |a d )?limonense|limon", "Limonense", 1950, 2005),
    (r"(ad )?municipal limon", "Municipal Limón", 1978, 1984),
    (r"(ad )?(municipal |m |mun )?puntarenas|puntarenense|puntareans", "Municipal Puntarenas", 1950, 2003),
    (r"(d |ad )?(municipal )?puntarenas( fc)?|puntareans", "Puntarenas FC", 2004, 2100),
    (r"nicolas marin", "Nicolás Marín", 1960, 1970),
    (r"(ad )?(municipal )?turrialba( f ?c)?", "Turrialba", 1960, 2100),
    (r"(ad |a d )?san carlos( fc)?|s carlos", "San Carlos", 1960, 2100),
    (r"(ad |a d )?ramonense|san ramon", "Ramonense", 1960, 2100),
    (r"(ad )?san miguel", "San Miguel", 1978, 1985), (r"(ad )?municipal san jose", "Municipal San José", 1978, 1990),
    (r"(ad |a d )?(mun )?sagrada f(amilia)?", "Sagrada Familia", 1978, 2100),
    (r"(ad )?limon northern", "Limón Northern", 1983, 1990),
    (r"(ad )?(municipal )?curridabat", "Curridabat", 1983, 1990),
    (r"(ad )?guanacaste(ca)?", "Guanacasteca", 1980, 2100),
    (r"(ad )?palmares", "Palmares", 1985, 1995),
    (r"(ad )?municipal generalena", "Municipal Generaleña", 1985, 1995),
    (r"(ad |adm |ad municipal |a d )?(p|perez) ?zeledon", "Pérez Zeledón", 1960, 2100),
    (r"(ad |a d )?(belen|belemita)( fc| siglo xxi)?", "Belén", 1980, 2100),
    (r"goico?e?chea", "Goicoechea", 1980, 2100),
    (r"(ad )?(municipal )?liberia( mia)?", "Municipal Liberia", 1980, 2100),
    (r"(s|sta|santa) barbara", "Santa Bárbara", 1980, 2100),
    (r"(sd |ad )?santos( guapiles)?", "Santos de Guápiles", 1990, 2100),
    (r"osa", "Osa", 1995, 2100), (r"brujas( fc)?( escazu)?", "Brujas de Escazú", 2000, 2100),
    (r"santacrucena", "Santacruceña", 2000, 2100), (r"aguilas g(uanacastecas)?", "Águilas Guanacastecas", 2005, 2100),
    (r"limon( fc)?", "Limón FC", 2006, 2100),
    (r"(as )?(puma|p) generalena", "Puma Generaleña", 2010, 2100),
    (r"grecia( fc)?", "Grecia", 2010, 2100), (r"guadalupe( fc)?", "Guadalupe", 2010, 2100),
    (r"(adr )?jicaral", "Jicaral", 2015, 2100), (r"sporting( fc)?( san jose)?", "Sporting de San José", 2015, 2100),
    (r"santa ana( fc)?", "Santa Ana", 2020, 2100),
    (r"cariari pococi", "Cariari Pococí", 1990, 2000), (r"naranjena", "Naranjeña", 1990, 2000),
    (r"orotinense", "Orotinense", 1990, 2000), (r"paraiso", "Paraíso de Cartago", 1990, 2000), (r"puriscal", "Puriscal", 1990, 2000),
    (r"quepos", "Quepos", 1990, 2000), (r"vecinos", "Vecinos", 1990, 2000), (r"ciudad colon", "Ciudad Colón", 1990, 2000),
    (r"tournon", "Tournón", 1990, 2000),
]

# lixo: data e disputa de pênaltis entre parênteses colados no nome ("Goicoechea (Mar 7)", "Belen (Saprissa 4-2 pen)")
_LIXO = re.compile(r"\s*\((?:[A-Z][a-z]{2}\s+\d{1,2}|[^()]*\bpen)\)|\[\[|\]\]")


def _regra(k: str, ano: int) -> str | None:
    for rx, exib, a0, a1 in REGRAS:
        if a0 <= ano <= a1 and re.fullmatch(f"(?:{rx})", k):
            return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    return _regra(chave(_LIXO.sub("", nome.strip())), ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
