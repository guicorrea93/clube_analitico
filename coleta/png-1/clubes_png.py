"""Identidade dos clubes de Papua-Nova Guiné (png-1): cada grafia da RSSSF vira um clube, com cidade e província (região).

Decisões aprovadas pelo Guilherme em 24/11/2026, depois de pesquisa a fundo (RSSSF, Wikipédia, ogol, imprensa de PNG):
- "Lae City": o Lae City Dwellers fundado em 2014 (na NSL desde 2015), rebatizado Toti City em 2018 e Lae City em 2019/20 é
  um clube só, o dos 7 títulos (2015, 2015/16, 2017, 2018, 2019, 2019/20, 2022); o "Lae City Dwellers" que aparece desde
  2022, ao lado do Lae City, é outro clube (fundado em 2021);
- "Hekari United": PRK Souths United (2006), Hekari Souths United (2007/08-2009/10), Hekari United, PNG Hekari (2026);
- "Gulf Komara": Erema FC (2015/16) e PRK Gulf Komara (2019, 2019/20);
- "Madang FC": Madang Flying Fox (2006), Madang Fox / Madang Niupetro Fox (2007/08-2010/11), Madang FC, Madang United (2026);
- "Rapatona": Inspac Rapatona, CMSS Rapatona Tigers (2007/08-2009/10), Rapatona FC (2015/16);
- "Morobe United": Tuguba Laitepo Blue Kumuls (2006), Morobe Kumuls (2007/08, "formerly Tuguba Laitepo Blue Kumuls"),
  Gigira Laitepo Morobe (2008/09-2014; "KTB = Kikira Tuguba Laitepo"; em 2011/12 Gigira Laitepo Central Coast), Welgris
  Morobe United (2015/16) e Morobe United (2019 e 2019/20);
- "Welgris Highlanders": Welgris Momads (2006; a RSSSF de 2007/08: "formerly Welgris Momads");
- "Besta PNG United": entrou na NSL em 2009/10 como a seleção sub-20 ("Besta PNG FA Under-20", até 2010/11; Wikipédia), PNG
  Besta United em 2013; "Eastern Stars" (Huawei Eastern Stars em 2014); "Port Moresby Strikers" (Southern Strikers em 2018-2019; Wikipédia:
  "also known as Southern Strikers", fundado em 2017); "PS United" (PS Huawei em
  2015/16, Huawei PS United em 2017); "Buang" (Prima Buang em 2017); "Morobe Wawens" (FC Morobe Wawens, Agmark FC Morobe
  Wawens); "Oro FC" (NC Civil Works Oro em 2013; "Oro" sozinho é o clube do México); "Tavur" (West New Britain Tavur em 2013); "Lahi" (Lahi Snax em 2019);
  "Greengold" (NBPOL Greengold Liners em 2019); "Rabaul Radazz"; "FC Kutubu"; "NCD" (National Capital District FC);
- separados: Lae FC (2014), Morobe Wawens, Besta PNG United, Besta Madang Fighters ("Madang Besta" na RSSSF, 2007/08), Gigira Laitepo United (2015/16, zona
  sul: franquia nova "com nome parecido", Gigira Amoana em 2017; Wikipédia), Admiralty Palaiau (2014-2015/16) e Admiralty Island (2024-2026), Goroka Gosiha (2015/16) e Goroka FC (2022), Mount Hagen FC (2019) e
  Hagen FC (2022), Markham FC (2019) e Radza FC (Markham, 2022), Aporro Mai (Kutubu, 2019) e FC Kutubu (2019/20); Blue Kumuls
  (Mount Hagen, 2019; não confundir com o Blue Kumuls de Lae, hoje Morobe United) e Ape Aporo (2022: fusão dele com o Aporro Mai);
- "Central United Port Moresby": o Central United de 2019 (a NZ tem o Central United de Auckland).

Uso: clube(nome, ano) -> nome de exibição (ou None).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-oceania"))
from rsssf_oce import chave  # noqa: E402

NCD, CEN, MOR, MAD, WHI, EHI, SHI = ("National Capital District", "Central", "Morobe", "Madang", "Western Highlands",
                                     "Eastern Highlands", "Southern Highlands")
POM = "Port Moresby"
# nome de exibição -> (cidade, província)
CLUBES: dict[str, tuple[str, str]] = {
    "Hekari United": (POM, NCD), "Gelle Hills United": (POM, CEN), "Madang FC": ("Madang", MAD), "Besta Madang Fighters": ("Madang", MAD),
    "Welgris Highlanders": ("Mount Hagen", WHI), "Morobe United": ("Lae", MOR), "Rapatona": (POM, NCD),
    "University Inter": (POM, NCD), "Eastern Stars": ("Alotau", "Milne Bay"), "Nabasa United": ("Madang", MAD),
    "Sepik": ("Wewak", "East Sepik"), "Tukoko University": ("Lae", MOR), "Besta PNG United": ("Lae", MOR), "Petro Souths": ("Mendi", SHI), "Bulolo United": ("Bulolo", MOR),
    "FC Port Moresby": (POM, NCD), "Oro FC": (POM, "Oro"), "Tavur": ("Kimbe", "West New Britain"), "Lae FC": ("Lae", MOR),
    "Admiralty Palaiau": (POM, "Manus"), "Lae City": ("Lae", MOR), "PS United": (POM, NCD), "Gulf Komara": ("Kerema", "Gulf"),
    "Gigira Laitepo United": (POM, CEN), "Goroka Gosiha": ("Goroka", EHI), "Buang": ("Mount Hagen", WHI),
    "Vitis Yamaros": (POM, NCD), "Morobe Wawens": ("Lae", MOR), "FC Momase": ("", MOR),
    "Port Moresby United": (POM, NCD), "FC Bougainville": (POM, "Bougainville"), "Central United Port Moresby": (POM, NCD),
    "Star Mountain": ("Tabubil", "Western"), "Lahi": ("Lae", MOR), "Laiwaden": ("Madang", MAD), "Markham": ("", MOR),
    "Tusbab Stallions": ("Madang", MAD), "Kagua-Erave": ("Kagua", SHI), "Blue Kumuls": ("Mount Hagen", WHI),
    "Mount Hagen FC": ("Mount Hagen", WHI), "Aporro Mai": ("Kutubu", SHI), "Enga Laima": ("Wabag", "Enga"),
    "Simbu Angra": ("Kundiawa", "Simbu"), "Chebu AROB": ("", "Bougainville"), "West Tribes": ("Kimbe", "West New Britain"),
    "Rabaul Radazz": ("Kokopo", "East New Britain"), "Greengold": ("Kimbe", "West New Britain"),
    "Vudal Gazelle": ("Kokopo", "East New Britain"), "Vitiaz United": (POM, NCD), "FC Kutubu": ("Kutubu", SHI),
    "Central Amoana": ("Kaparoko", CEN), "FC Genesis": ("", NCD), "NCD Souths": (POM, NCD), "NCD": (POM, NCD),
    "Lae Natives": ("Lae", MOR), "Lae City Dwellers": ("Lae", MOR), "Ape Aporo": ("Mount Hagen", WHI),
    "Kuri": ("Mount Hagen", WHI), "Radza": ("Markham", MOR), "Hagen FC": ("Mount Hagen", WHI), "Goroka FC": ("Goroka", EHI),
    "Wapak": ("Wabag", "Enga"), "Kimbe Eagle": ("Kimbe", "West New Britain"), "Laheri": ("", "West New Britain"),
    "Seeds United": ("", "West New Britain"), "Panguna Metals": ("Panguna", "Bougainville"), "Wantoks": ("", "Bougainville"),
    "Bougainville United": ("", "Bougainville"), "Kiara": ("", "Bougainville"), "Laden San Kamap": ("Buka", "Bougainville"),
    "North Bougainville": ("", "Bougainville"), "Port Moresby Strikers": (POM, NCD), "United Highlands": ("Mount Hagen", WHI),
    "Admiralty Island": ("", "Manus"), "Kula": ("Alotau", "Milne Bay"), "Blue Kumuls United": (POM, NCD),
    "Finschhafen Bavarians": ("Finschhafen", MOR), "WaWa": ("Wau", MOR),
}

# (regex sobre chave(nome), nome de exibição, ano inicial, ano final); a primeira que casa vale
REGRAS: list[tuple[str, str, int, int]] = [
    (r"^(prk )?souths? u(nited)?$|^(prk |png )?hekari( souths)? united$|^png hekari$", "Hekari United", 2006, 2100),
    (r"^gel+e hills u(nited)?$", "Gelle Hills United", 2006, 2100),
    (r"^(madang )?(flying |niupetro |mpg and rd tuna madang )?fox$|^madang( fc| united)?$", "Madang FC", 2006, 2100),
    (r"^(welgris )?(momads|highlanders)$", "Welgris Highlanders", 2006, 2014),
    (r"^(tl |tuguba laitepo )?blue kumuls$|^morobe kumuls$", "Morobe United", 2006, 2008),
    (r"^gigira laitepo( morobe( united)?| central coast)?$|^morobe$", "Morobe United", 2008, 2014),
    (r"^gigira laitepo united$", "Gigira Laitepo United", 2015, 2016),
    (r"^(welgris )?morobe united$", "Morobe United", 2015, 2100),
    (r"^(inspac |cmss )?rapatona( tigers)?$", "Rapatona", 2006, 2100),
    (r"^madang besta$", "Besta Madang Fighters", 2007, 2008),
    (r"^tukoko university( lae)?$", "Tukoko University", 2009, 2100),
    (r"^besta (png )?(fa )?(u 20|under 20)$", "Besta PNG United", 2009, 2011),
    (r"^(besta png|png besta) united$", "Besta PNG United", 2011, 2100),
    (r"^(fc )?port moresby$", "FC Port Moresby", 2013, 2016),
    (r"^(huawei )?eastern stars$", "Eastern Stars", 2008, 2100),
    (r"^(nc civil works )?oro( fc)?$", "Oro FC", 2013, 2100),
    (r"^(west new britain )?tavur$", "Tavur", 2013, 2100),
    (r"^lae$", "Lae FC", 2014, 2014),
    (r"^lae city dwellers$|^toti city$|^lae city$", "Lae City", 2014, 2020),
    (r"^lae city dwellers$", "Lae City Dwellers", 2021, 2100),
    (r"^lae city$", "Lae City", 2021, 2100),
    (r"^(huawei )?ps (united|huawei)$", "PS United", 2015, 2018),
    (r"^erema$|^(prk )?gulf komara$", "Gulf Komara", 2015, 2100),
    (r"^goroka( gosiha)?$", "Goroka Gosiha", 2015, 2016),
    (r"^goroka$", "Goroka FC", 2021, 2100),
    (r"^(prima )?buang$", "Buang", 2017, 2100),
    (r"^(fc )?momase$", "FC Momase", 2018, 2018),
    (r"^(agmark )?(fc )?morobe wawens$", "Morobe Wawens", 2018, 2100),
    (r"^(fc )?bougainville$", "FC Bougainville", 2019, 2020),
    (r"^central united$", "Central United Port Moresby", 2019, 2100),
    (r"^southern strikers$", "Port Moresby Strikers", 2017, 2100),
    (r"^lahi( snax)?$", "Lahi", 2019, 2100),
    (r"^(nbpol )?greengold( liners)?$", "Greengold", 2019, 2100),
    (r"^(rabaul )?radazz$", "Rabaul Radazz", 2019, 2100),
    (r"^(fc )?kutubu$", "FC Kutubu", 2019, 2100),
    (r"^mount hagen$", "Mount Hagen FC", 2019, 2100),
    (r"^hagen$", "Hagen FC", 2022, 2100),
    (r"^ncd souths$|^national capital district souths$", "NCD Souths", 2022, 2100),
    (r"^ncd$|^national capital district$", "NCD", 2022, 2100),
    (r"^star mountain$", "Star Mountain", 2019, 2100),
    (r"^blue kumuls$", "Blue Kumuls", 2019, 2019),
    # grafias do ogol
    (r"^admiralty$", "Admiralty Palaiau", 2014, 2016),
    (r"^admiralty$", "Admiralty Island", 2024, 2100),
    (r"^bavarians$", "Finschhafen Bavarians", 2026, 2100),
    (r"^erema gulf$", "Gulf Komara", 2015, 2100),
    (r"^kimbe eagles$", "Kimbe Eagle", 2022, 2100),
    (r"^wnb tavur$", "Tavur", 2013, 2100),
    (r"^wlgris morobe$", "Morobe United", 2015, 2100),
    # no ogol de 2015/16, "Gigira Laitepo Morobe" é o Gigira Laitepo United e "Huawey Eastern Stars FC" é o PS United (os
    # jogos batem com os da RSSSF): rótulos errados do ogol, de propósito sem clube (dariam o escudo de outro clube)
]
_NOMES_CHAVE = {chave(n): n for n in CLUBES}


def clube(nome: str, ano: int) -> str | None:
    k = chave(re.sub(r"\s*\([^)]*\)\s*$", "", nome))
    for kk in dict.fromkeys((k, re.sub(r" (fc|football club)$", "", k))):
        for rx, nome_ex, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.match(rx, kk):
                return nome_ex
        if kk in _NOMES_CHAVE:
            return _NOMES_CHAVE[kk]
    return None
