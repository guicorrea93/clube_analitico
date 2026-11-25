"""Identidade dos clubes das Ilhas Salomão (sol-1): cada grafia da RSSSF vira um clube, com cidade e província (região).

Decisões aprovadas pelo Guilherme em 25/11/2026, depois de pesquisa a fundo (RSSSF, inclusive a lista de fundação dos
clubes, Wikipédia e ogol):
- "Solomon Warriors": fundado em 1981 como Uncles FC (no campeonato nacional até 2008/09), Solomon Warriors desde maio de
  2010 (na "S-League" de franquias de 2004 e 2005, que não entra, jogou como Wantoks);
- "Marist": Marist Fire FC na S-League de 2010/11 a 2015/16 (Systek Kingz nas franquias de 2004 e 2005);
- "KOSSA" (Kossa FC; Fair West nas franquias); "Makuru" (JP Su'uria nas franquias); "Real Kakamora" (Kakamora FC até 2010;
  a seleção de Makira de mesmo nome, na Solomon Cup, é outra equipe); "Laugu United" (Blue Boys de 2009 a 2018); "Central
  Coast" (CY Strikers até 2019); "Ghupo" (Ghupo Wantoks em 2026, sem relação com o Wantoks de 2004);
- grafias da mesma equipe: "Kokohale" ("Kohohale", "FK Kokohale FC"), "Paritasi" ("Paratasi"), "FC Guadalcanal"
  ("Guadalcanal"), "Isabel United" ("FC Isabel United"), "Juniper Tree" ("FC Juniper Tree"), "Camp United" (o "Central
  United FC" de Gizo: a tabela de 2005/06 dá os dois nomes; fica o de uso, que não se confunde com o da Nova Zelândia);
- Malaita Kingz (S-League) e Auki Kingz (campeonato nacional de 2003 e 2006/07) ficam separados (nenhuma fonte liga os dois);
- homônimos de clubes de outros países já no banco levam a cidade ou a província: "Southern United Honiara" (o Southern
  United é da Nova Zelândia), "Northern United Malaita" (o Northern United é de Gana) e "Kula FC (Ilhas Salomão)" (o Kula é
  de Papua-Nova Guiné; a cidade do clube não foi achada). Western United e Central Coast não colidem com nada no banco e
  ficam sem a cidade.

A região é a província ("Honiara" para a capital, que é território à parte); a cidade fica vazia quando nenhuma fonte a dá.

Uso: clube(nome, ano) -> nome de exibição (ou None).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-oceania"))
from rsssf_oce import chave  # noqa: E402

HON, MAL, WES, GUA, CEN, ISA, MAK, REN, TEM, CHO = ("Honiara", "Malaita", "Western", "Guadalcanal", "Central", "Isabel",
                                                    "Makira-Ulawa", "Rennell and Bellona", "Temotu", "Choiseul")
# nome de exibição -> (cidade, província)
CLUBES: dict[str, tuple[str, str]] = {
    "Koloale": (HON, HON), "Solomon Warriors": (HON, HON), "Marist": (HON, HON), "KOSSA": (HON, HON), "Makuru": (HON, HON),
    "Naha": (HON, HON), "Sunbeam": (HON, HON), "Hana FC": (HON, HON), "X-Beam": (HON, HON), "West Honiara": (HON, HON),
    "Henderson Eels": (HON, HON), "Laugu United": (HON, HON), "Central Coast": (HON, HON), "Honiara City": (HON, HON),
    "Southern United Honiara": (HON, HON), "Waneagu United": (HON, HON), "SOSA": (HON, HON), "Juniper Tree": (HON, HON),
    "Green Shield": (HON, HON), "Ghupo": (HON, HON), "Kula FC (Ilhas Salomão)": ("", ""),
    "Western United": ("", WES), "Malaita Kingz": ("", MAL), "Real Kakamora": ("", MAK), "FC Guadalcanal": ("", GUA),
    "Isabel United": ("", ISA),
    "Auki Kingz": ("Auki", MAL), "Senga": ("", CHO), "Kuara": ("", GUA), "Husa": ("", WES), "Banika Bulls": ("Banika", CEN),
    "Mareeba Bulls": ("", MAK), "TNT": ("", REN), "Central Realas": ("", MAL),
    "Camp United": ("Gizo", WES), "Mafi United": ("", ISA), "New Jersey": ("", MAK), "Tematangi": ("", REN),
    "Mobile Cools": ("", CEN), "Aimela": ("", MAL), "Ngaube": ("", TEM),
    "Northern Warriors": ("", CEN), "Paritasi": ("", GUA), "Katova": ("", ISA), "Avaiki Chiefs Warriors": ("", REN),
    "Kokohale": ("Munda", WES),
    "Vatu": ("Sahalu", GUA), "Landowners": ("", MAL), "Fasi Roos": ("", MAL), "Iceland Rovers": ("", MAK),
    "Lagoon Brothers": ("Gizo", WES),
    "Gossa": ("Gizo", WES), "Soloso": ("", WES), "Malu'u United": ("Malu'u", MAL), "Malango": ("", GUA),
    "Gizo United": ("Gizo", WES), "Rendova Devon": ("", WES), "Harbour Lights": ("", MAL), "Northern United Malaita": ("", MAL),
    "South Central Gold": ("", GUA), "SIPA": ("", REN), "Ka'arua": ("", MAK),
}

# (regex sobre chave(nome), nome de exibição, ano inicial, ano final); a primeira que casa vale
REGRAS: list[tuple[str, str, int, int]] = [
    (r"^uncles?( fc)?$|^solomon warriors( fc)?$", "Solomon Warriors", 2000, 2100),
    (r"^marist( fire)?( fc)?$", "Marist", 2000, 2100),
    (r"^kossa( fc)?$", "KOSSA", 2000, 2100),
    (r"^makuru( fc)?$", "Makuru", 2000, 2100),
    (r"^(real )?kakamora( fc)?$", "Real Kakamora", 2000, 2100),
    (r"^laugu( united)?( fc)?$", "Laugu United", 2000, 2100),
    (r"^central coast( fc)?$", "Central Coast", 2019, 2100),
    (r"^ghupo( wantoks)?( fc)?$", "Ghupo", 2025, 2100),
    (r"^(fk )?ko[kh]ohale( fc)?$", "Kokohale", 2006, 2100),
    (r"^par[ai]tasi( fc)?$", "Paritasi", 2006, 2100),
    (r"^(fc )?guadalcanal( fc)?$", "FC Guadalcanal", 2015, 2100),
    (r"^(fc )?isabel united( fc)?$", "Isabel United", 2019, 2100),
    (r"^(fc )?juniper( tree)?( fc)?$", "Juniper Tree", 2023, 2100),
    (r"^camp united$|^central united( fc)?$", "Camp United", 2005, 2006),
    (r"^southern united( fc)?$", "Southern United Honiara", 2020, 2100),
    (r"^northern united( fc)?$", "Northern United Malaita", 2009, 2010),
    (r"^kula( fc)?$", "Kula FC (Ilhas Salomão)", 2021, 2100),
    (r"^hana( fc)?$", "Hana FC", 2000, 2100),
    (r"^western united( fc)?$", "Western United", 2010, 2100),
    (r"^mafi( united)?$", "Mafi United", 2005, 2006),
    (r"^malu.?u united$", "Malu'u United", 2008, 2009),   # ogol: "Malu´u United FC"
    (r"^avaiki chiefs w(arriors)?$", "Avaiki Chiefs Warriors", 2006, 2007),
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
