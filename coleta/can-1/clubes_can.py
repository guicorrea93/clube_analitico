"""Identidade dos clubes da 1ª divisão do Canadá: cada grafia -> nome de exibição único no mundo.

Regras (docs/coleta/plano-de-coleta.md, seção 2.2), decididas em 25/11/2026:
- nome pelo qual o clube é conhecido (Forge FC, Cavalry FC, Pacific FC, HFX Wanderers, Atlético Ottawa), com as grafias das
  páginas e do ogol;
- o mesmo clube com outro nome (mesma cidade): York9 / York United / Inter Toronto (o nome desde 2025); Ottawa Pioneers /
  Ottawa Intrepid; Kitchener Spirit (1990) / Kitchener Kickers; Vancouver 86ers = Vancouver Whitecaps (a mesma organização: virou Whitecaps em 2001 e entrou na MLS em
  2011; o nome do usa-1);
- clubes diferentes (refundação ou outra cidade): o Toronto Blizzard do CSL (1986-1993) e o da NASL (no usa-1);
  o Edmonton Brickmen (1986-1990), o FC Edmonton (2019-2022) e o Edmonton Eagles (1983); o Montreal Supra (1988-1992) e o
  FC Supra du Québec (2026);
- nome que já existe no banco ou em outro pacote: a cidade ou o ano entre parênteses ("Toronto Blizzard (CSL)"), como o
  usa-1 fez com "(NASL)".

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-concacaf"))
from rsssf_concacaf import chave  # noqa: E402

ON, AB, BC, QC, MB = "Ontário", "Alberta", "Colúmbia Britânica", "Quebec", "Manitoba"
_N = {  # nome de exibição -> (cidade, província)
    "Forge FC": ("Hamilton", ON), "Cavalry FC": ("Calgary", AB), "Pacific FC": ("Langford", BC),
    "HFX Wanderers": ("Halifax", "Nova Escócia"), "Valour FC": ("Winnipeg", MB), "Inter Toronto": ("Toronto", ON),
    "FC Edmonton": ("Edmonton", AB), "Atlético Ottawa": ("Ottawa", ON), "Vancouver FC": ("Langley", BC),
    "FC Supra du Québec": ("Laval", QC),
    "Hamilton Steelers": ("Hamilton", ON), "Ottawa Intrepid": ("Ottawa", ON), "Toronto Blizzard (CSL)": ("Toronto", ON),
    "North York Rockets": ("Toronto", ON), "Calgary Kickers": ("Calgary", AB), "Vancouver Whitecaps": ("Vancouver", BC),
    "Edmonton Brickmen": ("Edmonton", AB), "Winnipeg Fury": ("Winnipeg", MB), "Montreal Supra": ("Montreal", QC),
    "Victoria Vistas": ("Victoria", BC), "Kitchener Kickers": ("Kitchener", ON), "London Lasers": ("London", ON),
    "Nova Scotia Clippers": ("Halifax", "Nova Escócia"),
    "Edmonton Eagles": ("Edmonton", AB), "Calgary Mustangs": ("Calgary", AB), "Mississauga Croatia": ("Mississauga", ON),
    "Inter-Montréal": ("Montreal", QC), "Toronto Nationals": ("Toronto", ON),
}
CLUBES: dict[str, tuple[str, str, str]] = {k: (c, d, "CAN") for k, (c, d) in _N.items()}

REGRAS: list[tuple[str, str, int, int]] = [
    (r"forge( fc)?", "Forge FC", 2019, 2100), (r"cavalry( fc)?", "Cavalry FC", 2019, 2100), (r"pacific( fc)?", "Pacific FC", 2019, 2100),
    (r"(hfx|halifax)( wanderers)?( fc)?", "HFX Wanderers", 2019, 2100), (r"valour( fc)?", "Valour FC", 2019, 2100),
    (r"york ?9( fc)?|york united( fc)?|york|inter toronto( fc)?", "Inter Toronto", 2019, 2100),
    (r"fc edmonton|edmonton", "FC Edmonton", 2019, 2022), (r"(atl(etico)? )?ottawa", "Atlético Ottawa", 2020, 2100),
    (r"vancouver( fc)?", "Vancouver FC", 2023, 2100), (r"(fc )?supra( du quebec)?", "FC Supra du Québec", 2026, 2100),
    (r"hamilton( steelers)?", "Hamilton Steelers", 1983, 1992), (r"ottawa( pioneers| intrepid)?", "Ottawa Intrepid", 1987, 1990),
    (r"toronto( blizzard)?", "Toronto Blizzard (CSL)", 1986, 1993), (r"north york( rockets)?", "North York Rockets", 1987, 1992),
    (r"calgary( kickers| strikers)?", "Calgary Kickers", 1987, 1989), (r"vancouver( 86ers)?", "Vancouver Whitecaps", 1986, 2000),
    (r"edmonton( brick ?men)?", "Edmonton Brickmen", 1986, 1990), (r"winnipeg( fury)?", "Winnipeg Fury", 1987, 1992),
    (r"montreal( supra)?", "Montreal Supra", 1988, 1992), (r"victoria( vistas)?", "Victoria Vistas", 1989, 1990),
    (r"kitchener( kickers| spirit)?", "Kitchener Kickers", 1990, 1991), (r"london( lasers)?", "London Lasers", 1990, 1992),
    (r"nova scotia( clippers)?", "Nova Scotia Clippers", 1991, 1992),
    (r"edmonton( eagles)?", "Edmonton Eagles", 1983, 1983), (r"calgary( mustangs)?", "Calgary Mustangs", 1983, 1983),
    (r"mis+[ia]s+auga( croatia)?( sc)?", "Mississauga Croatia", 1983, 1983), (r"inter montreal( fc)?|montreal", "Inter-Montréal", 1983, 1983),
    (r"toronto( nationals)?", "Toronto Nationals", 1983, 1983),
]
_LIXO = re.compile(r"\[\[|\]\]")


def _regra(k: str, ano: int) -> str | None:
    for kk in (k, re.sub(r"^(club deportivo|c ?d|f ?c|club) ", "", k)):
        for rx, exib, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.fullmatch(f"(?:{rx})", kk):
                return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    return _regra(chave(_LIXO.sub("", re.sub(r"\s*\([^)]*\)", "", nome.strip()))), ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
