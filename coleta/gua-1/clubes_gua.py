"""Identidade dos clubes da 1ª divisão da Guatemala: cada grafia -> nome de exibição único no mundo.

Regras (docs/agentes-internacionais-COMECE-AQUI.md, seção 4), decididas em 24/11/2026:
- nome pelo qual o clube é conhecido (Municipal, Comunicaciones, Xelajú MC, Antigua GFC, Cobán Imperial, Suchitepéquez), com
  as grafias de cada época ("Tip Nac", "Xelaju", "Coban", "Communicaciones");
- o mesmo clube com outro nome: Universidad / USAC / Univ. San Carlos = USAC; Deportivo Heredia / Heredia-Jaguares = Heredia;
  Juca / Tally Juca = Tally Juca; Retalteca / Juventud Retalteca; Dep. Carchá / Carchá; Izabal / Izabal JC;
- Halcones La Mesilla (2012-2015) = Peñarol La Mesilla renomeado (a ESPN segue chamando de "Penarol" nesses anos);
- clubes diferentes: Escuintla e Juventud Escuintleca;
- homônimo de clube do banco ou de outro pacote leva o país: Hércules de Guatemala, Racing de Guatemala, España de
  Guatemala, América de Guatemala, Aurora de Guatemala, Eureka de Guatemala (conferido com o teste de carga).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-concacaf"))
from rsssf_concacaf import chave  # noqa: E402

GC = ("Ciudad de Guatemala", "Guatemala")
_G = lambda c, d: (c, d, "GUA")   # noqa: E731
_N = {  # nome de exibição -> (cidade, departamento)
    "Municipal": GC, "Comunicaciones": GC, "Aurora de Guatemala": GC, "Xelajú MC": ("Quetzaltenango", "Quetzaltenango"),
    "Antigua GFC": ("Antigua Guatemala", "Sacatepéquez"), "Suchitepéquez": ("Mazatenango", "Suchitepéquez"),
    "Cobán Imperial": ("Cobán", "Alta Verapaz"), "Jalapa": ("Jalapa", "Jalapa"), "Marquense": ("San Marcos", "San Marcos"),
    "Malacateco": ("Malacatán", "San Marcos"), "Guastatoya": ("Guastatoya", "El Progreso"), "Mixco": ("Mixco", "Guatemala"),
    "Achuapa": ("El Progreso", "Jutiapa"), "Petapa": ("San Miguel Petapa", "Guatemala"), "Sanarate": ("Sanarate", "El Progreso"),
    "Siquinalá": ("Siquinalá", "Escuintla"), "Mictlán": ("Asunción Mita", "Jutiapa"), "Iztapa": ("Iztapa", "Escuintla"),
    "Coatepeque": ("Coatepeque", "Quetzaltenango"), "Sololá": ("Sololá", "Sololá"), "Chiantla": ("Chiantla", "Huehuetenango"),
    "Nueva Concepción": ("Nueva Concepción", "Escuintla"), "Santa Lucía Cotzumalguapa": ("Santa Lucía Cotzumalguapa", "Escuintla"),
    "USAC": GC, "Heredia": ("Morales", "Izabal"), "Peñarol La Mesilla": ("La Mesilla", "Huehuetenango"),
 "Juventud Retalteca": ("Retalhuleu", "Retalhuleu"),
    "Teculután": ("Teculután", "Zacapa"), "Xinabajul": ("Huehuetenango", "Huehuetenango"), "Zacapa": ("Zacapa", "Zacapa"),
    "Escuintla": ("Escuintla", "Escuintla"), "Juventud Escuintleca": ("Escuintla", "Escuintla"), "Carchá": ("San Pedro Carchá", "Alta Verapaz"),
    "Amatitlán": ("Amatitlán", "Guatemala"), "Izabal JC": ("Puerto Barrios", "Izabal"), "Tally Juca": GC,
    "Tipografía Nacional": GC, "Guatemala FC": GC, "Hércules de Guatemala": GC, "Racing de Guatemala": GC,
    "España de Guatemala": GC, "América de Guatemala": GC, "Hospicio": GC, "IRCA": GC, "IGSS": GC, "Gallo": GC, "Aviateca": GC,
    "Correos": GC, "Folgar": GC, "Chichicaste": GC, "Eureka de Guatemala": GC, "Quiché": ("Santa Cruz del Quiché", "Quiché"),
    "Sacachispas": ("Chiquimula", "Chiquimula"), "Huehuetenango": ("Huehuetenango", "Huehuetenango"), "Rosario": GC,
    "Botrán": GC, "Palo Gordo": ("San Antonio Suchitepéquez", "Suchitepéquez"), "Pepsi Cola": GC, "Cementos Novella": GC,
    "Fegua": GC, "Galcasa": GC, "Tiquisate": ("Tiquisate", "Escuintla"), "Caminos": GC, "Pensamiento": GC, "Finanzas": GC,
    "Chiquimula": ("Chiquimula", "Chiquimula"), "Del Monte": ("Morales", "Izabal"), "Bandegua": ("Morales", "Izabal"),
    "Chiquimulilla": ("Chiquimulilla", "Santa Rosa"), "Azucareros": ("Escuintla", "Escuintla"), "Fundazúcar": ("Escuintla", "Escuintla"),
    "Chimaltenango": ("Chimaltenango", "Chimaltenango"), "Utatlán": GC,
}
CLUBES: dict[str, tuple[str, str, str]] = {k: _G(*v) for k, v in _N.items()}

REGRAS: list[tuple[str, str, int, int]] = [
    (r"(csd )?municipal", "Municipal", 1940, 2100), (r"comm?unicaciones", "Comunicaciones", 1940, 2100),
    (r"aurora( fc)?", "Aurora de Guatemala", 1940, 2100), (r"xelaju( mc)?", "Xelajú MC", 1940, 2100),
    (r"antigua( gfc)?", "Antigua GFC", 1950, 2100), (r"(deportivo )?suchitep(e|é)quez", "Suchitepéquez", 1950, 2100),
    (r"coban( imperial)?", "Cobán Imperial", 1950, 2100), (r"(deportivo )?jalapa", "Jalapa", 1960, 2100),
    (r"(deportivo )?marquense", "Marquense", 1950, 2100), (r"malacateco", "Malacateco", 2000, 2100),
    (r"guastatoya", "Guastatoya", 2010, 2100), (r"mixco", "Mixco", 2010, 2100), (r"(dep(ortivo)? )?achuapa", "Achuapa", 1990, 2100),
    (r"(deportivo )?petapa", "Petapa", 2000, 2100), (r"sanarate", "Sanarate", 1950, 2100), (r"siquinala", "Siquinalá", 2010, 2100),
    (r"mictlan", "Mictlán", 1990, 2100), (r"iztapa", "Iztapa", 2010, 2100), (r"coatepeque", "Coatepeque", 2010, 2100),
    (r"solola", "Sololá", 2010, 2100), (r"chiantla", "Chiantla", 2010, 2100), (r"nueva concepcion", "Nueva Concepción", 2010, 2100),
    (r"santa lucia( cotzumalguapa)?", "Santa Lucía Cotzumalguapa", 1990, 2100),
    (r"universidad( usac)?|usac|univ(ersidad)?( de)? san carlos", "USAC", 1940, 2100),
    (r"(deportivo )?heredia( jaguares)?", "Heredia", 2000, 2100), (r"penarol( la mesilla)?|halcones( lm| la mesilla)", "Peñarol La Mesilla", 2005, 2020),
 (r"(juv(entud)? ?)?retalteca|juventud r", "Juventud Retalteca", 1950, 2100),
    (r"tc?e(c|u)u?lut(a|á)n", "Teculután", 1990, 2100), (r"xinabajul", "Xinabajul", 2000, 2100), (r"(deportivo )?zacapa", "Zacapa", 1950, 2100),
    (r"juventud escuintleca", "Juventud Escuintleca", 2000, 2100), (r"(dep )?escuintla|rgm escuintla", "Escuintla", 1950, 2100),
    (r"(dep(ortivo)? )?carch(a|á)", "Carchá", 1990, 2100), (r"(deportivo )?amatitl(a|á)n", "Amatitlán", 1950, 2100),
    (r"(deportivo )?izabal( jc)?", "Izabal JC", 1980, 2100), (r"(tally )?ju ?ca", "Tally Juca", 1960, 2000),
    (r"tip( nac(ional)?|ografia nacional)", "Tipografía Nacional", 1940, 2000), (r"guatemala( fc)?", "Guatemala FC", 1940, 1960),
    (r"hercules", "Hércules de Guatemala", 1940, 1960), (r"racing", "Racing de Guatemala", 1940, 1950),
    (r"espana", "España de Guatemala", 1940, 1950), (r"america", "América de Guatemala", 1960, 1980),
    (r"hospicio", "Hospicio", 1940, 1950), (r"irca", "IRCA", 1940, 1970), (r"igss", "IGSS", 1950, 1970), (r"gallo", "Gallo", 1955, 1965),
    (r"aviateca", "Aviateca", 1955, 1965), (r"correos", "Correos", 1950, 1960), (r"folgar", "Folgar", 1950, 1960),
    (r"chichicaste", "Chichicaste", 1950, 1965), (r"eureka", "Eureka de Guatemala", 1955, 1965), (r"quiche", "Quiché", 1955, 1965),
    (r"sacachispas", "Sacachispas", 1955, 2100), (r"huehuetenango", "Huehuetenango", 1955, 1970), (r"rosario", "Rosario", 1955, 1965),
    (r"botran", "Botrán", 1960, 1970), (r"palo gordo", "Palo Gordo", 1960, 1975), (r"pepsi cola", "Pepsi Cola", 1960, 1975),
    (r"cementos novella", "Cementos Novella", 1965, 1980), (r"fegua", "Fegua", 1965, 1980), (r"galcasa", "Galcasa", 1970, 1995),
    (r"tiquisate", "Tiquisate", 1970, 1985), (r"caminos", "Caminos", 1970, 1985), (r"pensamiento", "Pensamiento", 1975, 1985),
    (r"finanzas", "Finanzas", 1975, 1990), (r"chiquimula", "Chiquimula", 1975, 1985), (r"del monte", "Del Monte", 1985, 1995),
    (r"bandegua", "Bandegua", 1985, 1995), (r"chiquimulilla", "Chiquimulilla", 1985, 1995), (r"azucareros", "Azucareros", 1990, 2000),
    (r"fundazucar", "Fundazúcar", 1990, 2000), (r"chimaltenango", "Chimaltenango", 1990, 2000), (r"utatlan", "Utatlán", 1945, 1960),
]
_LIXO = re.compile(r"\[\[|\]\]")


def _regra(k: str, ano: int) -> str | None:
    k = re.sub(r"^(club deportivo|csyd|csd|cd|fc|club) ", "", k)
    k = re.sub(r" (fc|cf)$", "", k)
    for kk in (k, re.sub(r"^(deportivo|atletico) ", "", k)):   # ESPN: "Atlético Mictlán", "Deportivo Mixco"
        for rx, exib, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.fullmatch(f"(?:{rx})", kk):
                return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    return _regra(chave(_LIXO.sub("", re.sub(r"\s*\((?!usac)[^)]*\)", "", nome.strip()))), ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
