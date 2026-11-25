"""Cadastro dos clubes do campeonato da Tchecoslováquia (tch-1, 1925 a 1992/93).

Os clubes que também jogaram a liga tcheca têm a mesma chave do `clubes_cze` (o mesmo clube nas duas competições, de
propósito, como o `gdr-1` com o `ger-1`). Os outros: clubes tchecos que não chegaram à liga tcheca e os eslovacos (país
de hoje, SVK; o Rusj Užhorod, de Užhorod, hoje Ucrânia, UKR).

Identidade: pelo alvo do link da Wikipédia em cada temporada (LINKS), que segue a linhagem do clube através das trocas de
nome da era comunista (Sparta = Bratrství Sparta = Spartak Praha Sokolovo; Slavia = Dynamo Praha; Dukla = ATK = ÚDA;
Slovan Bratislava = ŠK = NV Bratislava; Bohemians = AFK Vršovice = Spartak Praha Stalingrad...). Os poucos links que
apontam para um artigo errado ou repetido (redirecionamentos, "FK Dukla Prague" em 1980/81) estão em LINKS também.
"""
from __future__ import annotations

import clubes_cze

CLUBES = dict(clubes_cze.CLUBES)
CLUBES.update({
    # tchecos que não jogaram a liga tcheca
    "DFC Prag": ("Praga", "CZE"), "ČAFC Vinohrady": ("Praga", "CZE"), "Čechie Karlín": ("Praga", "CZE"),
    "SK Libeň": ("Praga", "CZE"), "Nuselský SK": ("Praga", "CZE"), "Meteor Praga VIII": ("Praga", "CZE"),
    "Slavoj Žižkov": ("Praga", "CZE"), "Čechie VIII": ("Praga", "CZE"), "Teplitzer FK": ("Teplice", "CZE"),
    "SK Náchod": ("Náchod", "CZE"), "SK Plzeň": ("Plzeň", "CZE"), "SK Prostějov": ("Prostějov", "CZE"),
    "AFK Kolín": ("Kolín", "CZE"), "Moravská Slavia Brno": ("Brno", "CZE"), "DSV Saaz": ("Žatec", "CZE"),
    "SK Pardubice": ("Pardubice", "CZE"), "SK Olomouc ASO": ("Olomouc", "CZE"), "Polaban Nymburk": ("Nymburk", "CZE"),
    "SK Nusle": ("Praga", "CZE"), "SK Rakovník": ("Rakovník", "CZE"), "ČAFC Židenice": ("Brno", "CZE"),
    "Křídla vlasti Olomouc": ("Olomouc", "CZE"), "Dukla Pardubice": ("Pardubice", "CZE"),
    "Slavoj Liberec": ("Liberec", "CZE"), "Jiskra Liberec": ("Liberec", "CZE"), "Rudá Hvězda Brno": ("Brno", "CZE"),
    "LeRK Brno": ("Brno", "CZE"), "Motorlet Praga": ("Praga", "CZE"), "Baťov": ("Otrokovice", "CZE"),
    "Třinec": ("Třinec", "CZE"), "Frýdek-Místek": ("Frýdek-Místek", "CZE"), "Pardubice 1899": ("Pardubice", "CZE"),
    # eslovacos
    "Slovan Bratislava": ("Bratislava", "SVK"), "Spartak Trnava": ("Trnava", "SVK"),
    "Inter Bratislava": ("Bratislava", "SVK"), "Žilina": ("Žilina", "SVK"), "Tatran Prešov": ("Prešov", "SVK"),
    "Lokomotíva Košice": ("Košice", "SVK"), "VSS Košice": ("Košice", "SVK"), "TTS Trenčín": ("Trenčín", "SVK"),
    "Považská Bystrica": ("Považská Bystrica", "SVK"), "Nitra": ("Nitra", "SVK"),
    "Dukla Banská Bystrica": ("Banská Bystrica", "SVK"), "Petržalka": ("Bratislava", "SVK"),
    "DAC Dunajská Streda": ("Dunajská Streda", "SVK"), "Slávia Bratislava": ("Bratislava", "SVK"),
    "Juventus Topoľčany": ("Topoľčany", "SVK"), "Spišská Nová Ves": ("Spišská Nová Ves", "SVK"),
    "ZTK Zvolen": ("Zvolen", "SVK"), "SK Baťovany": ("Partizánske", "SVK"),
    # hoje na Ucrânia
    "Rusj Užhorod": ("Užhorod", "UKR"),
})

# alvo do link da Wikipédia -> chave
LINKS = {
    "AC Sparta Prague": "Sparta Praga", "Sparta Prague": "Sparta Praga",
    "SK Slavia Prague": "Slavia Praga",
    "FK Viktoria Žižkov": "Viktoria Žižkov", "Bohemians 1905": "Bohemians 1905",
    "SK Kladno": "Kladno", "FC Viktoria Plzeň": "Viktoria Plzeň", "Viktoria Plzeň": "Viktoria Plzeň",
    "FC Zbrojovka Brno": "Zbrojovka Brno", "1. FC Zbrojovka Brno": "Zbrojovka Brno", "FC Zbrojovka  Brno": "Zbrojovka Brno",
    "FC Boby Brno": "Zbrojovka Brno",
    "FC Baník Ostrava": "Baník Ostrava", "Baník Ostrava": "Baník Ostrava",
    "FC Fastav Zlín": "Zlín", "FK Teplice": "Teplice", "FK Ústí nad Labem": "Ústí nad Labem",
    "MFK Vítkovice": "Vítkovice", "FC Vítkovice": "Vítkovice", "TJ Vítkovice": "Vítkovice",
    "Dukla Prague": "Dukla Praga", "FK Dukla Prague": "Dukla Praga",   # 1980/81: o link aponta o clube novo; é o Dukla do exército
    "FC Hradec Králové": "Hradec Králové", "FK Jablonec": "Jablonec", "FK Hvězda Cheb": "Union Cheb",
    "SK Sigma Olomouc": "Sigma Olomouc", "SK Dynamo České Budějovice": "Dynamo České Budějovice",
    "SK České Budějovice": "Dynamo České Budějovice",
    "DFC Prag": "DFC Prag", "ČAFC Prague": "ČAFC Vinohrady", "ČAFC Vinohrady": "ČAFC Vinohrady",
    "Čechie Karlín": "Čechie Karlín", "SK Libeň": "SK Libeň", "Nuselský SK": "Nuselský SK",
    "FK Meteor Prague VIII": "Meteor Praga VIII", "SK Slavoj Žižkov": "Slavoj Žižkov", "SK Čechie VIII": "Čechie VIII",
    "Teplitzer FK": "Teplitzer FK", "SK Náchod": "SK Náchod", "FK Náchod": "SK Náchod", "SK Plzeň": "SK Plzeň",
    "SK Prostějov": "SK Prostějov", "1. SK Prostějov": "SK Prostějov", "AFK Kolín": "AFK Kolín",
    "SK Moravská Slavia Brno": "Moravská Slavia Brno", "DSV Saaz": "DSV Saaz", "SK Pardubice": "SK Pardubice",
    "SK Olomouc ASO": "SK Olomouc ASO", "SK Polaban Nymburk": "Polaban Nymburk", "SK Nusle": "SK Nusle",
    "SK Rakovník": "SK Rakovník", "ČAFC Židenice": "ČAFC Židenice", "Křídla vlasti Olomouc": "Křídla vlasti Olomouc",
    "Dukla Pardubice": "Dukla Pardubice", "Slavoj Liberec": "Slavoj Liberec", "Jiskra Liberec": "Jiskra Liberec",
    "Rudá Hvězda Brno": "Rudá Hvězda Brno", "FC LeRK Brno": "LeRK Brno", "FK Motorlet Prague": "Motorlet Praga",
    "SK Baťov 1930": "Baťov", "FK Fotbal Třinec": "Třinec", "MFK Frýdek-Místek": "Frýdek-Místek",
    "FK Pardubice 1899": "Pardubice 1899",
    "ŠK Slovan Bratislava": "Slovan Bratislava", "FC Spartak Trnava": "Spartak Trnava",
    "FK Inter Bratislava": "Inter Bratislava", "Inter Bratislava": "Inter Bratislava", "MŠK Žilina": "Žilina",
    "1. FC Tatran Prešov": "Tatran Prešov", "FC Lokomotíva Košice": "Lokomotíva Košice",
    "FC VSS Košice": "VSS Košice", "MFK Košice": "VSS Košice", "TTS Trenčín": "TTS Trenčín",
    "MŠK Považská Bystrica (football)": "Považská Bystrica", "FC Nitra": "Nitra", "Slovan Nitra": "Nitra",
    "FK Dukla Banská Bystrica": "Dukla Banská Bystrica", "FC Petržalka": "Petržalka", "FC Petržalka 1898": "Petržalka",
    "FC DAC 1904 Dunajská Streda": "DAC Dunajská Streda", "Slavia Bratislava VS": "Slávia Bratislava",
    "Slávia Bratislava VŠ": "Slávia Bratislava", "ASC Juventus Topoľčany": "Juventus Topoľčany",
    "AC Spišská Nová Ves": "Spišská Nová Ves", "ZTK Zvolen": "ZTK Zvolen", "SK Baťovany": "SK Baťovany",
    "SC Rusj Uzhorod": "Rusj Užhorod", "SC Rusj Užhorod": "Rusj Užhorod",
}


def link(alvo: str | None) -> str | None:
    return LINKS.get((alvo or "").strip())


def exibicao(chave_clube: str) -> str:
    return chave_clube
