"""Clubes da Copa Colombia: os do col-1 (coleta/col-1/clubes_col.py) mais os da Primera B que só jogam a copa. As regras
daqui vêm antes das do col-1 e casam o nome inteiro; valem de 2008 em diante (as edições antigas só têm clubes do col-1).

Identidades: Deportivo Rionegro (2008-2014) e Itagüí Leones são a linha do Leones FC; Rionegro Águilas e Itagüí Ditaires,
a das Águilas Doradas (como no col-1); Alianza Petrolera é o Alianza FC (mudou-se para Valledupar em 2024, como no col-1);
"Internacional" em 2024 é o Internacional de Palmira (Primera B), não o Internacional de Bogotá (a La Equidad de 2025);
o Boca Juniors de Cali da Primera B (2020 em diante) é outro clube, refundado, não o de 1937 do col-1.
Cidades pelo nome do clube ou pela Wikipédia em espanhol; sem fonte, vazias.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "col-1"))
import clubes_col  # noqa: E402
from rsssf_sul import chave  # noqa: E402

SEM = ("", "")
VALLE = "Valle del Cauca"
CLUBES_COPA: dict[str, tuple[str, str]] = {
    "Academia FC": ("Bogotá", "Bogotá D.C."), "Atlético de la Sabana": ("Sincelejo", "Sucre"),
    "Atlético FC de Cali": ("Cali", VALLE), "Bajo Cauca FC": ("Caucasia", "Antioquia"),
    "Barranquilla FC": ("Barranquilla", "Atlántico"), "Boca Juniors de Cali (refundado)": ("Cali", VALLE),
    "Bogotá FC": ("Bogotá", "Bogotá D.C."), "Córdoba FC": ("Montería", "Córdoba"), "Depor FC": SEM,
    "Deportes Palmira": ("Palmira", VALLE), "Expreso Rojo": SEM, "Girardot FC": ("Girardot", "Cundinamarca"),
    "Internacional de Palmira": ("Palmira", VALLE), "Juventud Soacha": ("Soacha", "Cundinamarca"),
    "Once Manizales": ("Manizales", "Caldas"), "Orsomarso": SEM, "Pacífico de Buenaventura": ("Buenaventura", VALLE),
    "Real Cundinamarca": SEM, "Real San Andrés": ("San Andrés", "San Andrés y Providencia"), "Real Santander": ("", "Santander"),
    "Sucre FC": ("Sincelejo", "Sucre"), "Universitario de Popayán": ("Popayán", "Cauca"), "Valledupar FC": ("Valledupar", "Cesar"),
}
# (regex sobre a chave do nome, nome de exibição); casa o nome inteiro
REGRAS_COPA: list[tuple[str, str]] = [
    (r"academia( fc)?", "Academia FC"), (r"atl(etico)? de la sabana", "Atlético de la Sabana"),
    (r"atletico( fc| f c| cali| de cali)?", "Atlético FC de Cali"), (r"bajo cauca fc", "Bajo Cauca FC"),
    (r"barranquilla( fc| f c)?", "Barranquilla FC"), (r"boca juniors( de cali)?", "Boca Juniors de Cali (refundado)"),
    (r"bogota( fc| f c)?", "Bogotá FC"), (r"cordoba fc", "Córdoba FC"), (r"depor( fc| f c)?", "Depor FC"),
    (r"dep(ortes)? palmira", "Deportes Palmira"), (r"expreso( rojo)?", "Expreso Rojo"), (r"girardot fc", "Girardot FC"),
    (r"internacional", "Internacional de Palmira"), (r"juventud( soacha)?", "Juventud Soacha"), (r"once manizales", "Once Manizales"),
    (r"orsomarso( sc)?", "Orsomarso"), (r"pacifico( fc)?", "Pacífico de Buenaventura"), (r"real cundinamarca", "Real Cundinamarca"),
    (r"(r|real) san andres", "Real San Andrés"), (r"(real )?santander( cd)?", "Real Santander"), (r"sucre", "Sucre FC"),
    (r"universit[aá]rio( de popayan)?", "Universitario de Popayán"), (r"valledupar( fc| f c)?", "Valledupar FC"),
    # clubes do col-1 em grafias que as regras dele não pegam
    (r"(al(ianza)? )?petrolera", "Alianza FC"), (r"(dvo|dep(ortivo)?) ?rionegro|rionegro|itagui leones", "Leones FC"),
    (r"(r|rionegro) ag(uilas)?", "Águilas Doradas"), (r"tigres?( fc| f c)?", "Tigres FC"),
    (r"bucamanga", "Atlético Bucaramanga"), (r"b chico", "Boyacá Chicó"), (r"deportivo quindio", "Deportes Quindío"),
    (r"dvo cali", "Deportivo Cali"), (r"dvo pasto", "Deportivo Pasto"), (r"centauros", "Centauros Villavicencio"),
    (r"llaneros( fc)?", "Llaneros FC"), (r"patriot(as|es)( fc)?", "Patriotas Boyacá"), (r"uniautonoma", "Uniautónoma"),
]
CLUBES = {**clubes_col.CLUBES, **CLUBES_COPA}
assert all(e in CLUBES for _, e in REGRAS_COPA), [e for _, e in REGRAS_COPA if e not in CLUBES]


def clube(nome: str, ano: int) -> str | None:
    """Nome de exibição: as regras da copa (nome inteiro, de 2008 em diante) e, sem elas, as do col-1."""
    nome = re.sub(r"\{\{.*$", "", nome).strip()   # nota {{Refn|...}} colada no nome (Wikipédia, 2012)
    k = re.sub(r"\s+", " ", chave(nome)).strip()
    if ano >= 2008:
        for rx, exib in REGRAS_COPA:
            if re.fullmatch(rx, k):
                return exib
    return clubes_col.clube(nome, ano)
