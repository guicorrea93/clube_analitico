"""Identidade dos clubes colombianos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido no Brasil ("Millonarios", "Atlético Nacional", "América de Cali", "Junior de
  Barranquilla", "Independiente Santa Fe", "Independiente Medellín");
- homônimo de clube do banco ou de outro pacote leva a cidade ("Libertad de Barranquilla", "Universidad Nacional de Bogotá");
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte: Atlético Municipal ->
  Atlético Nacional; Atlético Quindío -> Deportes Quindío; Cristal Caldas -> Once Caldas; Itagüí (Ditaires) -> Águilas
  Doradas (mudou para Pereira em 2015 e para Rionegro em 2016); La Equidad -> Internacional de Bogotá (2025); Alianza
  Petrolera -> Alianza FC (Valledupar, 2024); Chicó -> Boyacá Chicó; Corporación Tuluá -> Cortuluá;
- Deportes Caldas (campeão em 1950) entra como Once Caldas, como a RSSSF e o próprio Once Caldas contam (o Once Caldas
  nasceu em 1961 da fusão do Deportes Caldas com o Once Deportivo); o Once Deportivo fica separado.

As tabelas da RSSSF põem os pontos de bônus no nome ("América Cali (1 BP)") e a de 1995 abre a linha com "- ": saem antes da
regra. REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-sulamerica"))
from rsssf_sul import chave  # noqa: E402

BOG = ("Bogotá", "Bogotá D.C.")
MED = ("Medellín", "Antioquia")
CALI = ("Cali", "Valle del Cauca")
BAQ = ("Barranquilla", "Atlántico")

# nome de exibição -> (cidade, departamento)
CLUBES: dict[str, tuple[str, str]] = {
    "Millonarios": BOG, "Independiente Santa Fe": BOG, "Internacional de Bogotá": BOG, "Fortaleza CEIF": BOG,
    "Universidad Nacional de Bogotá": BOG, "Tigres FC": ("Soacha", "Cundinamarca"),
    "Atlético Nacional": MED, "Independiente Medellín": MED, "Huracán de Medellín": MED, "Envigado": ("Envigado", "Antioquia"),
    "Águilas Doradas": ("Rionegro", "Antioquia"), "Leones FC": ("Itagüí", "Antioquia"),
    "América de Cali": CALI, "Deportivo Cali": CALI, "Boca Juniors de Cali": CALI, "Cortuluá": ("Tuluá", "Valle del Cauca"),
    "Junior de Barranquilla": BAQ, "Sporting de Barranquilla": BAQ, "Deportivo Barranquilla": BAQ, "Libertad de Barranquilla": BAQ,
    "Uniautónoma": BAQ,
    "Once Caldas": ("Manizales", "Caldas"), "Once Deportivo": ("Manizales", "Caldas"),
    "Atlético Manizales": ("Manizales", "Caldas"),
    "Deportivo Pereira": ("Pereira", "Risaralda"), "Deportes Quindío": ("Armenia", "Quindío"), "Deportes Tolima": ("Ibagué", "Tolima"),
    "Atlético Bucaramanga": ("Bucaramanga", "Santander"), "Alianza FC": ("Valledupar", "Cesar"),
    "Cúcuta Deportivo": ("Cúcuta", "Norte de Santander"), "Unión Magdalena": ("Santa Marta", "Magdalena"),
    "Deportivo Samarios": ("Santa Marta", "Magdalena"), "Real Cartagena": ("Cartagena", "Bolívar"),
    "Atlético Huila": ("Neiva", "Huila"), "Deportivo Pasto": ("Pasto", "Nariño"), "Boyacá Chicó": ("Tunja", "Boyacá"),
    "Patriotas Boyacá": ("Tunja", "Boyacá"), "Jaguares de Córdoba": ("Montería", "Córdoba"),
    "Llaneros FC": ("Villavicencio", "Meta"), "Centauros Villavicencio": ("Villavicencio", "Meta"),
    "Oro Negro": ("Barrancabermeja", "Santander"), "Unicosta": BAQ,
}

REGRAS: list[tuple[str, str, int, int]] = [
    (r"(cd )?millonari?o?s( fc| futbol club)?|millionarios|millonaros", "Millonarios", 1946, 2100),
    (r"(i|ind|indep|independ|independiente) ?(santa ?f[eé]|sante ?fe)|santa ?f[eé]|santafe|sante fe", "Independiente Santa Fe", 1940, 2100),
    (r"(cd |d |dep |deportivo )?(i|ind|indep|indendiente|independ|independiente|lndependiente)\.? ?medell[ií]n|di medell[ií]n|imedell[ií]n|"
     r"(cd )?indep medell[ií]n|medell[ií]n", "Independiente Medellín", 1940, 2100),
    (r"(a|at|atl|atletico) ?nacional|nacional( won)?$|nacional\b", "Atlético Nacional", 1950, 2100),
    (r"(deportivo )?independiente$", "Independiente Medellín", 1990, 1995),   # "Independiente [Medellin]" nas tabelas
    (r"(atletico )?municipal", "Atlético Nacional", 1946, 1950),
    (r"(cd |corporacion deportiva )?america( de)? ?(cali)?( b)?$|america cali|america de cali|america\b", "América de Cali", 1946, 2100),
    (r"(d|dep|deportes|deportivo) ?cali|cali$", "Deportivo Cali", 1946, 2100),
    (r"(a |atl |atletico )?j[uú]nior( de barranquilla)?", "Junior de Barranquilla", 1946, 2100),
    (r"(once|o|i|cristal|d|dep|deportes|deportivo) caldas|(corporacion deportiva )?once caldas|caldas$", "Once Caldas", 1946, 2100),
    (r"once (deportivo|deport|d tivo)", "Once Deportivo", 1946, 1959),
    (r"(d |dep |deportes |deportivo )?pereira", "Deportivo Pereira", 1946, 2100),
    (r"(d |dep |deportes |corporacion deportes |atletico )?(quindio|qundio)", "Deportes Quindío", 1950, 2100),
    (r"(d |dep |deportes |club deportes |coop |cooperamos )?tolima", "Deportes Tolima", 1954, 2100),
    (r"(a |atl |atletico |club atletico )?buca?ra?m?anga|bucamaranga|bucuramanga", "Atlético Bucaramanga", 1948, 2100),
    (r"(a |at |atl |atletico )?huila", "Atlético Huila", 1990, 2100),
    (r"(u|un|union) ?magdalena|magdalena", "Unión Magdalena", 1953, 2100),
    (r"cucuta( dep| deportivol?| deportivo)?|cucuta", "Cúcuta Deportivo", 1949, 2100),
    (r"(r |real )?cartagena", "Real Cartagena", 1970, 2100),
    (r"(dep |deportivo )?pasto", "Deportivo Pasto", 1995, 2100),
    (r"envi[gd]ado( f ?c)?", "Envigado", 1991, 2100),
    (r"(boyaca )?chico( fc)?", "Boyacá Chicó", 2002, 2100),
    (r"patriotas( fc| boyaca)?", "Patriotas Boyacá", 2010, 2100),
    (r"(la )?equidad|(cd la equidad)|internacional de bogota", "Internacional de Bogotá", 2005, 2100),
    (r"fortaleza( ceif| fc)?", "Fortaleza CEIF", 2010, 2100),
    (r"jaguares( de cordoba)?", "Jaguares de Córdoba", 2012, 2100),
    (r"uniautonoma( fc)?", "Uniautónoma", 2012, 2100),
    (r"(cd )?(rionegro )?aguilas( doradas)?|itagui( ditaires| fc)?|(cd )?itagui ditaires", "Águilas Doradas", 2000, 2100),
    (r"(itagui )?leones( fc)?", "Leones FC", 2015, 2100),
    (r"tigres( fc)?", "Tigres FC", 2015, 2100),
    (r"alianza( fc| p| petrolera| valledupar)?", "Alianza FC", 2010, 2100),
    (r"(cor |corp |corporacion |d |dep |deportivo )?tul[uú]a|cortulua", "Cortuluá", 1990, 2100),
    (r"llaneros( fc)?", "Llaneros FC", 2020, 2100),
    (r"centauros( villavicencio)?", "Centauros Villavicencio", 2000, 2010),
    (r"(club )?universidad( nacional)?( de bogota)?", "Universidad Nacional de Bogotá", 1946, 1953),
    (r"boca (jrs|js|juniors)( de cal?i?)?", "Boca Juniors de Cali", 1946, 1960),
    (r"hurac[aá]n( de medellin)?", "Huracán de Medellín", 1946, 1955),
    (r"sporting( club| barranquilla| b quilla| barr)?|sp barranquilla", "Sporting de Barranquilla", 1946, 1995),
    (r"(dep |deportivo )?(barranquilla|b quilla)", "Deportivo Barranquilla", 1946, 1952),
    (r"(deportivo )?samarios", "Deportivo Samarios", 1946, 1955),
    (r"(atletico )?manizales|club deportivo manizales", "Atlético Manizales", 1946, 1960),
    (r"libertad", "Libertad de Barranquilla", 1946, 1960),
    (r"(club deportivo )?oro negro", "Oro Negro", 1965, 1975),
    (r"(dep |deportivo )?unicosta", "Unicosta", 1990, 2000),
]

_LIXO = re.compile(r"^\s*-\s*|\s*\(\s*[\d.,]+\s*BP\s*\)\s*$|\s*\(\d{4}\)\s*$", re.I)


def _regra(k: str, ano: int) -> str | None:
    for kk in (k, re.sub(r"^(club|c|cd|corporacion deportiva) ", "", k)):
        for rx, exib, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.match(rx + r"(?:\b|$)", kk):
                return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    nome = _LIXO.sub("", _LIXO.sub("", nome))
    return _regra(chave(nome), ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
