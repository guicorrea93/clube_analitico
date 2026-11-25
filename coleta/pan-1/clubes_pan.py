"""Identidade dos clubes da 1ª divisão do Panamá: cada grafia -> nome de exibição único no mundo.

Regras (docs/agentes-internacionais-COMECE-AQUI.md, seção 4), decididas em 25/11/2026:
- nome pelo qual o clube é conhecido (Tauro, Plaza Amador, Árabe Unido, San Francisco, CAI La Chorrera), com as grafias e
  abreviações das páginas ("Arabe", "P Amador", "S Francisco", "Sporting SM", "C.A.I");
- o mesmo clube com outro nome (a lista de campeões da RSSSF diz): Deportivo La Previsora = San Francisco FC; Chorrillo FC /
  El Chorrillo / Municipal Chorrillo = CD Universitario (o nome desde 2018); Sporting '89 / Sporting SM = Sporting San
  Miguelito; River Plate FC = Colón River (renomeado em 2004); Projusa / Los Bravos del Projusa; Deportivo del Este = Potros
  del Este; Veraguas CD = Veraguas United;
- clubes diferentes: Chiriquí FC (até 2001) e Atlético Chiriquí (2002 em diante); Atlético Nacional (anos 1990) e SD Atlético
  Nacional (2015 em diante); Atlético Veragüense e Veraguas United; Sporting Colón, Sporting Coclé e Sporting San Miguelito;
- homônimo de clube do banco ou de outro pacote leva o país: Alianza de Panamá, Atlético Nacional de Panamá, SD Atlético
  Nacional de Panamá (conferido com o teste de carga).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-concacaf"))
from rsssf_concacaf import chave  # noqa: E402

CP = ("Ciudad de Panamá", "Panamá")
_N = {  # nome de exibição -> (cidade, província)
    "Tauro": CP, "Plaza Amador": CP, "Árabe Unido": ("Colón", "Colón"), "San Francisco": ("La Chorrera", "Panamá Oeste"),
    "CAI La Chorrera": ("La Chorrera", "Panamá Oeste"), "CD Universitario": CP, "Alianza de Panamá": CP, "Euro Kickers": CP,
    "Sporting San Miguelito": ("San Miguelito", "Panamá"), "Panamá Viejo": CP, "Projusa": ("Santiago de Veraguas", "Veraguas"),
    "Sporting Colón": ("Colón", "Colón"), "Cosmos": CP, "Atlético Nacional de Panamá": CP, "SD Atlético Nacional de Panamá": CP,
    "Chiriquí FC": ("David", "Chiriquí"), "Atlético Chiriquí": ("David", "Chiriquí"),
    "Atlético Veragüense": ("Santiago de Veraguas", "Veraguas"), "Veraguas United": ("Santiago de Veraguas", "Veraguas"),
    "Ejecutivo Jr": ("San Miguelito", "Panamá"), "Pan de Azúcar": ("San Miguelito", "Panamá"),
    "Colón River": ("Colón", "Colón"), "Atlético Municipal Colón": ("Colón", "Colón"), "Sporting Coclé": ("Penonomé", "Coclé"),
    "Policía Nacional": CP, "Chepo": ("Chepo", "Panamá"), "Río Abajo": CP, "Santa Gema": ("Arraiján", "Panamá Oeste"),
    "Costa del Este": CP, "Herrera FC": ("Chitré", "Herrera"), "Potros del Este": CP, "Umecit": CP,
    "Unión Coclé": ("Penonomé", "Coclé"),
}
CLUBES: dict[str, tuple[str, str, str]] = {k: (c, d, "PAN") for k, (c, d) in _N.items()}

REGRAS: list[tuple[str, str, int, int]] = [
    (r"tauro", "Tauro", 1985, 2100), (r"(c ?d )?(plaza|p) ?amadora?|plaza a", "Plaza Amador", 1985, 2100),
    (r"((c ?d|dep(ortivo)?) )?[aà]ra[bp][ea]( unido)?|araba unido", "Árabe Unido", 1985, 2100),
    (r"(s(an)? francis?c?o|deportivo la previsora)", "San Francisco", 1985, 2100),
    (r"c ?a ?i", "CAI La Chorrera", 2005, 2100),
    (r"(el |mun(icipal)? )?chorrillo|(c ?d )?universitario", "CD Universitario", 1995, 2100),
    (r"alianza", "Alianza de Panamá", 1995, 2100), (r"(afc |fc )?euro ?kickers", "Euro Kickers", 1985, 2005),
    (r"sporting( 89| s ?m| san miguelito)?", "Sporting San Miguelito", 1995, 2100),
    (r"panam[ae] v(iejo)?", "Panamá Viejo", 1985, 2005), (r"(los )?bravos( del projusa)?|projusa", "Projusa", 1985, 2000),
    (r"sporting colon", "Sporting Colón", 1985, 1995), (r"cosmos", "Cosmos", 1990, 2000),
    (r"(atl(etico)? )?nacional", "Atlético Nacional de Panamá", 1990, 2005),
    (r"(s ?d )?(atl(etico)? )?nacional", "SD Atlético Nacional de Panamá", 2010, 2100),
    (r"chir(i)?qui", "Chiriquí FC", 1990, 2001), (r"(atl(etico)? )?chiriqui", "Atlético Chiriquí", 2002, 2100),
    (r"(atl(etico)? |atketico )?veraguense", "Atlético Veragüense", 2000, 2020),
    (r"veraguas( cd| united)?", "Veraguas United", 2019, 2100),
    (r"ejecutivo( jr)?", "Ejecutivo Jr", 1990, 2000), (r"pan (de )?a(zucar)?", "Pan de Azúcar", 1990, 2010),
    (r"(colon )?river( plate)?", "Colón River", 2000, 2010), (r"atl(etico)? municipal colon", "Atlético Municipal Colón", 1995, 2005),
    (r"(sporting )?cocle", "Sporting Coclé", 2000, 2010), (r"policia nacional", "Policía Nacional", 2000, 2010),
    (r"chepo", "Chepo", 2005, 2020), (r"rio abajo", "Río Abajo", 2010, 2020), (r"santa gema", "Santa Gema", 2010, 2025),
    (r"costa del este", "Costa del Este", 2015, 2025), (r"herrera", "Herrera FC", 2015, 2100),
    (r"(potros|deportivo)( del)? este", "Potros del Este", 2020, 2100), (r"umecit", "Umecit", 2020, 2100),
    (r"union cocle", "Unión Coclé", 2020, 2100),
]
_LIXO = re.compile(r"\[\[|\]\]")


def _regra(k: str, ano: int) -> str | None:
    for kk in (k, re.sub(r"^(club deportivo|c ?d|s ?d|a ?f ?c|f ?c|club) ", "", k), re.sub(r" (f ?c)$", "", k)):
        for rx, exib, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.fullmatch(f"(?:{rx})", kk):
                return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    return _regra(chave(_LIXO.sub("", re.sub(r"\s*\([^)]*\)", "", nome.strip()))), ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
