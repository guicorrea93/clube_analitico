"""Identidade dos clubes da liga saudita: cada grafia de cada fonte (RSSSF, ogol, ESPN, Wikipédia) aponta para um clube.

Nome de exibição: o nome árabe com hífen, na grafia mais usada hoje (a do clube e da liga). Ficam com o nome puro
Al-Hilal, Al-Ittihad, Al-Nassr e Al-Shabab (combinado entre os agentes, 23/11); o homônimo de clube de outro país leva a
cidade (Al-Ahli de Jeddah, Al-Wehda de Meca, Al-Qadsiah de Khobar, Al-Faisaly de Harmah, Al-Khaleej de Saihat, Al-Nahda
de Dammam, Al-Ansar de Medina, Al-Najma de Unaizah, Al-Orobah de Sakakah, Al-Arabi de Unaizah, Al-Ain de Al-Baha).

Mesmo clube com grafias diferentes: Al-Nasr = Al-Nassr; Al-Ahly = Al-Ahli; Al-Ittifaq = Al-Ettifaq; Al-Qadisiya =
Al-Qadsiah; Al-Wahda = Al-Wehda; Al-Nijma/Al-Nejmeh = Al-Najma; a linha "Al-Nojoom" da tabela da RSSSF de
2025/26 é o Neom (mesmos números: 12-9-13, 43-48, 45 pontos; o Al-Nojoom, de Al-Hasa, nunca jogou a 1ª divisão); Al-Ta'ee/Al-Tai; Al-Ra'ed/Al-Raed; Al-Faysali/Al-Faisaly;
Al-Fat'h/Al-Fateh; Al-Hazm/Al-Hazem; Faiha'a/Al-Fayha; Dhamk/Damak/Damac; Hajr/Hajer; Ukhdood/Al-Akhdoud/Al-Okhdood;
Al-Urooba/Al-Orobah; Al-Sho'ala/Al-Shoalah/Al-Shoulla; Al-Rouda/Al-Rawda/Al-Rawdhah; Okadh/Okaz; Al-Khlood/Al-Kholood;
Al-Riyadh SC = Al-Riyadh.

CLUBES: nome de exibição -> (cidade, província). REGRAS: (regex sobre a grafia da fonte, sem "Al"/"Al-"/"FC"/"Club"/
"SC" e sem acento, em minúsculas) -> nome de exibição. Grafia sem regra é erro (de propósito).
"""
from __future__ import annotations

import re
import unicodedata

CLUBES: dict[str, tuple[str, str]] = {
    "Al-Hilal": ("Riade", "Riade"),
    "Al-Nassr": ("Riade", "Riade"),
    "Al-Shabab": ("Riade", "Riade"),
    "Al-Riyadh": ("Riade", "Riade"),
    "Al-Ittihad": ("Jeddah", "Meca"),
    "Al-Ahli de Jeddah": ("Jeddah", "Meca"),
    "Al-Wehda de Meca": ("Meca", "Meca"),
    "Okaz": ("Taif", "Meca"),
    "Ohod": ("Medina", "Medina"),
    "Al-Ansar de Medina": ("Medina", "Medina"),
    "Al-Ettifaq": ("Dammam", "Província Oriental"),
    "Al-Nahda de Dammam": ("Dammam", "Província Oriental"),
    "Al-Qadsiah de Khobar": ("Khobar", "Província Oriental"),
    "Al-Khaleej de Saihat": ("Saihat", "Província Oriental"),
    "Al-Fateh": ("Al-Mubarraz", "Província Oriental"),
    "Hajer": ("Al-Hasa", "Província Oriental"),
    "Al-Adalah": ("Al-Hasa", "Província Oriental"),
    "Al-Rawdhah": ("Al-Hasa", "Província Oriental"),
    "Al-Batin": ("Hafar Al-Batin", "Província Oriental"),
    "Al-Raed": ("Buraidah", "Qassim"),
    "Al-Taawoun": ("Buraidah", "Qassim"),
    "Al-Najma de Unaizah": ("Unaizah", "Qassim"),
    "Al-Arabi de Unaizah": ("Unaizah", "Qassim"),
    "Al-Hazem": ("Ar Rass", "Qassim"),
    "Al-Kholood": ("Ar Rass", "Qassim"),
    "Al-Tai": ("Ha'il", "Ha'il"),
    "Al-Jabalain": ("Ha'il", "Ha'il"),
    "Al-Faisaly de Harmah": ("Harmah", "Riade"),
    "Al-Fayha": ("Al-Majma'ah", "Riade"),
    "Al-Shoulla": ("Al-Kharj", "Riade"),
    "Al-Kawkab": ("Al-Kharj", "Riade"),
    "Al-Yamamah": ("Al-Kharj", "Riade"),
    "Sadous": ("Sadus", "Riade"),
    "Abha": ("Abha", "Asir"),
    "Damac": ("Khamis Mushait", "Asir"),
    "Najran": ("Najran", "Najran"),
    "Al-Okhdood": ("Najran", "Najran"),
    "Al-Orobah de Sakakah": ("Sakakah", "Al-Jouf"),
    "Al-Watani": ("Tabuk", "Tabuk"),
    "Neom": ("Neom", "Tabuk"),
    "Al-Ain de Al-Baha": ("Al-Baha", "Al-Baha"),
    "Al-Rabe'e": ("", ""),
    "Al-Kifah": ("", ""),
}

REGRAS: list[tuple[str, str]] = [
    (r"^hilal$", "Al-Hilal"),
    (r"^nass?r$", "Al-Nassr"),
    (r"^shabab$", "Al-Shabab"),
    (r"^r[ie]y?adh( sc)?$", "Al-Riyadh"),
    (r"^i+tt?i?hh?ad( jeddah)?$", "Al-Ittihad"),
    (r"^ahl[iy]( jeddah| saudi)?$", "Al-Ahli de Jeddah"),
    (r"^w[ae]h?da$", "Al-Wehda de Meca"),
    (r"^oka[dz]h?$", "Okaz"),
    (r"^o?u?hod$", "Ohod"),
    (r"^ansar$", "Al-Ansar de Medina"),
    (r"^[ei]tt?[ie]faq$", "Al-Ettifaq"),
    (r"^nah?da$", "Al-Nahda de Dammam"),
    (r"^qad[ei]?s[ei]?y?ah?$|^qadsia$", "Al-Qadsiah de Khobar"),
    (r"^khaleej$", "Al-Khaleej de Saihat"),
    (r"^fat'?e?h$", "Al-Fateh"),
    (r"^ha[j]e?r$", "Hajer"),
    (r"^adalah?$", "Al-Adalah"),
    (r"^r[ao]u?w?dh?a?h?$", "Al-Rawdhah"),
    (r"^bat[ie]n$", "Al-Batin"),
    (r"^ra'?e?d$", "Al-Raed"),
    (r"^ta'?a?wo?u?n$", "Al-Taawoun"),
    (r"^(najma|nejma|nejmeh|nijma|nijmeh)$", "Al-Najma de Unaizah"),
    (r"^n[jo]+o?m$", "Neom"),   # só na RSSSF de 2025/26: os números da linha "Al-Nojoom" são os do Neom
    (r"^arabi$", "Al-Arabi de Unaizah"),
    (r"^haze?m$", "Al-Hazem"),
    (r"^(kholood|khlood|kholoud)$", "Al-Kholood"),
    (r"^ta'?e?e?i?$|^ta'i$", "Al-Tai"),
    (r"^jabalain$", "Al-Jabalain"),
    (r"^fa[iy]sal[iy]$", "Al-Faisaly de Harmah"),
    (r"^fa[iy]ha'?a?$", "Al-Fayha"),
    (r"^sho'?[ua]?'?l(l)?ah?$", "Al-Shoulla"),
    (r"^kawkab$", "Al-Kawkab"),
    (r"^yamamah$", "Al-Yamamah"),
    (r"^s[a]?d[o]+u?s$", "Sadous"),
    (r"^abha$", "Abha"),
    (r"^(damac|damak|dhamk|damc)$", "Damac"),
    (r"^najran$", "Najran"),
    (r"^(ukh|akh|okh)doo?u?d$", "Al-Okhdood"),
    (r"^or?o?u?ro?o?bah?$|^urooba$", "Al-Orobah de Sakakah"),
    (r"^watani$", "Al-Watani"),
    (r"^neom$", "Neom"),
    (r"^ain$", "Al-Ain de Al-Baha"),
    (r"^rabe'?e$", "Al-Rabe'e"),
    (r"^ke?i?fah$", "Al-Kifah"),
]


def chave(nome: str) -> str:
    s = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().lower().strip()
    s = re.sub(r"\((.*?)\)", "", s)
    s = re.sub(r"\b(fc|sc|club|sfc|saudi club)\b", "", s)
    s = re.sub(r"^al[- ]?", "", s.strip())
    return re.sub(r"\s+", " ", s).strip(" -.")


def clube(nome: str) -> str | None:
    k = chave(nome)
    for rx, c in REGRAS:
        if re.search(rx, k):
            return c
    return None


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for n in sys.argv[1:]:
        print(n, "->", clube(n))
