"""Identidade dos clubes do Taiti (tah-1): cada grafia da RSSSF vira um clube, com cidade e ilha (região).

Decisões (o mesmo clube com outro nome é um clube só):
- nome com "AS" (decisão do Guilherme, 24/11), salvo "Central Sport" (sem "AS" no uso corrente);
- Punaruu = AS Tamarii Punaruu (a RSSSF de 1968: "Punaruu (aka Tamarii Punaruu)"); Temanava = AS Tamarii Temanava (Mooréa);
  Arue, JS Arue e AS Arue (nome completo Tamarii Nahiti d'Arue) = AS Arue; "Paea" de 1971 = AS Manu-Ura ("A.S. Manu Ura de
  Paea relegated");
- seleções de base que jogaram a liga: "Tahiti U-17" (inclui "Tahiti Nui U-17"), "Tahiti U-19" e "Tahiti U-20", como a RSSSF
  escreve (uma por categoria);
- "AS Juventus" (Papeari) não é a Juventus italiana (nome diferente no banco).

Uso: clube(nome, ano) -> nome de exibição (ou None). ano = ano de início da temporada.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-oceania"))
from rsssf_oce import chave  # noqa: E402

# nome de exibição -> (cidade, ilha)
CLUBES: dict[str, tuple[str, str]] = {
    "AS Aorai": ("Papeete", "Tahiti"),
    "AS Arue": ("Arue", "Tahiti"),
    "AS Dragon": ("Papeete", "Tahiti"),
    "AS Excelsior": ("Papeete", "Tahiti"),
    "AS Fei Pi": ("Papeete", "Tahiti"),
    "AS Jeunes Tahitiens": ("Papeete", "Tahiti"),
    "AS Juventus": ("Papeari", "Tahiti"),
    "AS Manu-Ura": ("Paea", "Tahiti"),
    "AS Mataiea": ("Mataiea", "Tahiti"),
    "AS Matavai": ("Papeete", "Tahiti"),
    "AS Mira": ("Papetoai", "Mooréa"),
    "AS Olympic Mahina": ("Mahina", "Tahiti"),
    "AS Papara": ("Papara", "Tahiti"),
    "AS Papenoo": ("Papenoo", "Tahiti"),
    "AS Phénix": ("Punaauia", "Tahiti"),
    "AS Pirae": ("Pirae", "Tahiti"),
    "AS PTT": ("Papeete", "Tahiti"),
    "AS Pueu": ("Pueu", "Tahiti"),
    "AS Racing": ("Papeete", "Tahiti"),
    "AS Roniu": ("Papeete", "Tahiti"),
    "AS Taiarapu": ("Taiarapu", "Tahiti"),
    "AS Tamarii Faa'a": ("Faaa", "Tahiti"),
    "AS Tamarii Punaruu": ("Punaauia", "Tahiti"),
    "AS Tamarii Temanava": ("Maatea", "Mooréa"),
    "AS Tapuhute": ("Haapiti", "Mooréa"),
    "AS Taravao AC": ("Taravao", "Tahiti"),
    "AS Tefana": ("Faaa", "Tahiti"),
    "AS Tiare Tahiti": ("Afareaitu", "Mooréa"),
    "AS Vaiete": ("Papeete", "Tahiti"),
    "AS Vairao": ("Vairao", "Tahiti"),
    "AS Vénus": ("Mahina", "Tahiti"),
    "Central Sport": ("Papeete", "Tahiti"),
    "Tahiti U-17": ("Papeete", "Tahiti"),
    "Tahiti U-19": ("Papeete", "Tahiti"),
    "Tahiti U-20": ("Papeete", "Tahiti"),
}

# (regex sobre chave(nome) sem o "as " do começo, nome de exibição, ano inicial, ano final); a primeira que casa vale
REGRAS: list[tuple[str, str, int, int]] = [
    (r"^aorai$", "AS Aorai", 1900, 2100),
    (r"^(js )?arue$", "AS Arue", 1900, 2100),
    (r"^dragons?$", "AS Dragon", 1900, 2100),
    (r"^excelsior$", "AS Excelsior", 1900, 2100),
    (r"^fei pi$", "AS Fei Pi", 1900, 2100),
    (r"^(jeunes|j|jns) tahitiens$|^jt$", "AS Jeunes Tahitiens", 1900, 2100),
    (r"^juventus$", "AS Juventus", 1900, 2100),
    (r"^manu ura$", "AS Manu-Ura", 1900, 2100),
    (r"^paea$", "AS Manu-Ura", 1971, 1971),
    (r"^mataiea$", "AS Mataiea", 1900, 2100),
    (r"^matavai$", "AS Matavai", 1900, 2100),
    (r"^mira$", "AS Mira", 1900, 2100),
    (r"^(ol|olympic)( mahina)?$", "AS Olympic Mahina", 1900, 2100),
    (r"^papara$", "AS Papara", 1900, 2100),
    (r"^papenoo$", "AS Papenoo", 1900, 2100),
    (r"^phenix$", "AS Phénix", 1900, 2100),
    (r"^pirae$", "AS Pirae", 1900, 2100),
    (r"^ptt$", "AS PTT", 1900, 2100),
    (r"^pueu$", "AS Pueu", 1900, 2100),
    (r"^racing$", "AS Racing", 1900, 2100),
    (r"^roniu$", "AS Roniu", 1900, 2100),
    (r"^taiarapu( fc)?$", "AS Taiarapu", 1900, 2100),
    (r"^(tamarii|tamari|tamaril|temarii|t) faaa$", "AS Tamarii Faa'a", 1900, 2100),
    (r"^(tamarii )?punaruu$", "AS Tamarii Punaruu", 1900, 2100),
    (r"^(tamarii )?temanava$", "AS Tamarii Temanava", 1900, 2100),
    (r"^tapuhute$", "AS Tapuhute", 1900, 2100),
    (r"^(tac|taravao ac)$", "AS Taravao AC", 1900, 2100),
    (r"^tef[ae]na$", "AS Tefana", 1900, 2100),
    (r"^tiare tahiti$", "AS Tiare Tahiti", 1900, 2100),
    (r"^vaiete$", "AS Vaiete", 1900, 2100),
    (r"^vair[ao]{2}$", "AS Vairao", 1900, 2100),
    (r"^venus$", "AS Vénus", 1900, 2100),
    (r"^central( sports?)?$", "Central Sport", 1900, 2100),
    (r"^tahiti( nui)? u 17$", "Tahiti U-17", 1900, 2100),
    (r"^tahiti u 19$", "Tahiti U-19", 1900, 2100),
    (r"^tahiti u 20$", "Tahiti U-20", 1900, 2100),
]


def clube(nome: str, ano: int) -> str | None:
    k = chave(re.sub(r"\s*\([^)]*\)\s*$", "", nome))   # "AS Pirae (Pirae)": a cidade sai
    k = re.sub(r"^as ", "", k)
    for rx, nome_ex, a0, a1 in REGRAS:
        if a0 <= ano <= a1 and re.match(rx, k):
            return nome_ex
    return None
