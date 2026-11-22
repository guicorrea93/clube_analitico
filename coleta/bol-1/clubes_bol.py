"""Identidade dos clubes bolivianos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido ("Bolívar", "The Strongest", "Jorge Wilstermann", "Oriente Petrolero");
- homônimo de clube do banco ou de outro pacote leva a cidade: os Universitarios (de La Paz, Sucre, Potosí, Beni, Pando e
  Vinto; o Universitario é o peruano), "Ferroviario de La Paz", "Internacional de Oruro" (Certamen Mixto 1957) e
  "Internacional de La Paz" (1958-1960), "Municipal de La Paz" (o Deportivo Municipal é o peruano); clubes bolivianos com o
  mesmo nome também: "Litoral de La Paz" e "Litoral de Cochabamba" (1966-1969), "Petrolero de Cochabamba" e "Petrolero de
  Yacuiba", "Primero de Mayo de La Paz" (1958-1959) e "Primero de Mayo de Potosí" (1983-1984), "31 de Octubre" (La Paz) e
  "31 de Octubre de Oruro" (1975), "Stormers" (Sucre) e "Stormers Petrolero" (Potosí);
- o mesmo clube com outro nome em outra época fica com o nome atual: Deportivo Chaco (até 1962) é o Chaco Petrolero;
  Universidad Iberoamericana é o Iberoamericana; CDT Real Oruro / CD Totora Real Oruro é o Real Oruro; Atlético Palmaflor
  (Palmaflor del Trópico) é o Palmaflor;
- nomes curtos das páginas: "Oriente", "Chaco", "Strongest", "Wilstermann", "Independiente" (Independiente Petrolero),
  "Municipal", "Petrolero" (o de Cochabamba até 1993), "Universitario" (depende do ano);
- de 1995 a 1998 as páginas da RSSSF põem a cidade antes do clube ("Cochabamba Wilstermann", "Santa Cruz Blooming"): a
  cidade cai antes de procurar o clube.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-sulamerica"))
from rsssf_sul import chave  # noqa: E402

LPZ = ("La Paz", "La Paz")
CBB = ("Cochabamba", "Cochabamba")
SCZ = ("Santa Cruz de la Sierra", "Santa Cruz")
ORU = ("Oruro", "Oruro")
SUC = ("Sucre", "Chuquisaca")
PTS = ("Potosí", "Potosí")
TJA = ("Tarija", "Tarija")
TDD = ("Trinidad", "Beni")

# nome de exibição -> (cidade, departamento)
CLUBES: dict[str, tuple[str, str]] = {
    # La Paz
    "Bolívar": LPZ, "The Strongest": LPZ, "Always Ready": ("El Alto", "La Paz"), "Litoral de La Paz": LPZ,
    "Chaco Petrolero": LPZ, "Municipal de La Paz": LPZ, "Ferroviario de La Paz": LPZ, "Atlético La Paz": LPZ,
    "Ingavi": LPZ, "Northern": LPZ, "Unión Maestranza": ("Viacha", "La Paz"), "Deportivo Árabe": LPZ, "31 de Octubre": LPZ,
    "Universitario de La Paz": LPZ, "Mariscal Santa Cruz": LPZ, "Mariscal Braun": LPZ, "La Paz FC": LPZ,
    "Iberoamericana": LPZ, "Internacional de La Paz": LPZ, "Primero de Mayo de La Paz": LPZ,
    # Cochabamba
    "Jorge Wilstermann": CBB, "Aurora": CBB, "Bata": ("Quillacollo", "Cochabamba"), "Petrolero de Cochabamba": CBB,
    "Litoral de Cochabamba": CBB, "Tránsito": CBB, "Palmaflor": ("Quillacollo", "Cochabamba"),
    "Universitario de Vinto": ("Vinto", "Cochabamba"), "San Antonio Bulo Bulo": ("Bulo Bulo", "Cochabamba"),
    # Santa Cruz
    "Oriente Petrolero": SCZ, "Blooming": SCZ, "Guabirá": ("Montero", "Santa Cruz"), "Destroyers": SCZ, "Real Santa Cruz": SCZ,
    "La Bélgica": SCZ, "Universidad Santa Cruz": SCZ, "Royal Pari": SCZ, "Sport Boys Warnes": ("Warnes", "Santa Cruz"),
    "Atlético Pompeya": SCZ, "Gualberto Villarroel": ("San José de Chiquitos", "Santa Cruz"),
    # Oruro
    "San José": ORU, "Oruro Royal": ORU, "Ingenieros": ORU, "Miner's Japo": ORU, "31 de Octubre de Oruro": ORU,
    "Internacional de Oruro": ORU, "Orcobol": ORU, "Metalsan": ORU, "Real Oruro": ORU, "San Pedro": ORU,
    # Sucre
    "Universitario de Sucre": SUC, "Independiente Petrolero": SUC, "Stormers": SUC, "Magisterio": SUC, "Policar": SUC,
    "Francesa": SUC, "ABB": SUC,
    # Potosí
    "Real Potosí": PTS, "Nacional Potosí": PTS, "Universitario de Potosí": PTS, "Stormers Petrolero": PTS,
    "Wilstermann Unificada": PTS, "Wilstermann Cooperativas": PTS, "Independiente Unificada": PTS, "Bamin": PTS,
    "Primero de Mayo de Potosí": PTS,
    # Tarija e Chaco
    "Ciclón": TJA, "Unión Central": TJA, "Real Tomayapo": TJA, "Petrolero de Yacuiba": ("Yacuiba", "Tarija"),
    # Beni e Pando
    "Real Mamoré": TDD, "Universitario de Beni": TDD, "20 de Agosto": TDD, "Real Beni": TDD,
    "Libertad Gran Mamoré": TDD, "Vaca Díez": ("Cobija", "Pando"), "Universitario de Pando": ("Cobija", "Pando"),
}

REGRAS: list[tuple[str, str, int, int]] = [
    # Universitarios (o nome sozinho depende do ano)
    (r"univ(ersitario)?( de)? (la paz)", "Universitario de La Paz", 1900, 2100),
    (r"univ(ersitario)?( de)? sucre", "Universitario de Sucre", 1900, 2100),
    (r"univ(ersitario)?( de)? potosi|universitario p$", "Universitario de Potosí", 1900, 2100),
    (r"univ(ersitario)?( de)? beni|universitario b$", "Universitario de Beni", 1900, 2100),
    (r"univ(ersitario)?( de)? pando", "Universitario de Pando", 1900, 2100),
    (r"univ(ersitario)?( de)? vinto", "Universitario de Vinto", 1900, 2100),
    (r"universitario$", "Universitario de La Paz", 1950, 1970),
    (r"universitario$", "Universitario de Potosí", 1971, 1994),
    (r"universitario$", "Universitario de Sucre", 1995, 2100),
    (r"univ(ersidad)? iberoamericana|iberoamerican[ao]", "Iberoamericana", 1990, 2100),
    (r"universidad santa cruz", "Universidad Santa Cruz", 1950, 2100),
    # La Paz
    (r"(club )?bolivar", "Bolívar", 1925, 2100),
    (r"(the )?strongest|the srongest", "The Strongest", 1908, 2100),
    (r"always re?a?dy", "Always Ready", 1933, 2100),
    (r"litoral (cochabamba|c$)", "Litoral de Cochabamba", 1950, 2100),
    (r"litoral$", "Litoral de Cochabamba", 1966, 1969),   # no nacional desses anos (a página da liga de La Paz fica de fora)
    (r"litoral", "Litoral de La Paz", 1932, 2100),
    (r"chaco( petrolero)?|deportivo chaco", "Chaco Petrolero", 1944, 2100),
    (r"(deportivo )?municipal", "Municipal de La Paz", 1944, 2100),
    (r"ferroviario", "Ferroviario de La Paz", 1920, 2100),
    (r"atletico la paz", "Atlético La Paz", 1900, 1960),
    (r"ingavi", "Ingavi", 1900, 2100),
    (r"northern", "Northern", 1900, 2100),
    (r"(union )?(u )?mae?s?tranza", "Unión Maestranza", 1900, 2100),
    (r"(deportivo )?arabe", "Deportivo Árabe", 1900, 2100),
    (r"31 de octubre oruro", "31 de Octubre de Oruro", 1900, 2100),
    (r"31 de octubre", "31 de Octubre", 1900, 2100),
    (r"mariscal santa cruz", "Mariscal Santa Cruz", 1900, 2100),
    (r"mariscal braun", "Mariscal Braun", 1900, 2100),
    (r"la paz( fc)?$|la paz fc", "La Paz FC", 1990, 2100),
    (r"internacional|international", "Internacional de Oruro", 1957, 1957),
    (r"internacional|international", "Internacional de La Paz", 1958, 1965),
    (r"(primero|1o) de mayo potosi", "Primero de Mayo de Potosí", 1900, 2100),
    (r"(primero|1o) de mayo", "Primero de Mayo de La Paz", 1950, 1970),
    (r"(primero|1o) de mayo", "Primero de Mayo de Potosí", 1971, 2100),
    # Cochabamba
    (r"(j(orge)? )?wilstermann( cochabamba)?$|j(orge)? ?wilstermann", "Jorge Wilstermann", 1949, 2100),
    (r"aurora", "Aurora", 1935, 2100),
    (r"bata", "Bata", 1900, 2100),
    (r"petrolero (yacuiba)", "Petrolero de Yacuiba", 1900, 2100),
    (r"petrolero( cochabamba| c)?$|petrolero cochabamba", "Petrolero de Cochabamba", 1950, 2000),
    (r"transito", "Tránsito", 1900, 2100),
    (r"(atl(etico)? )?palmaflor( del tropico)?", "Palmaflor", 2000, 2100),
    (r"san antonio( bulo bulo)?", "San Antonio Bulo Bulo", 2000, 2100),
    # Santa Cruz
    (r"oriente( p| petrolero| peterolero)?", "Oriente Petrolero", 1955, 2100),
    (r"blooming", "Blooming", 1946, 2100),
    (r"guabira", "Guabirá", 1962, 2100),
    (r"destroyers", "Destroyers", 1948, 2100),
    (r"real (santa|sta) cruz", "Real Santa Cruz", 1962, 2100),
    (r"santa cruz$", "Real Santa Cruz", 1999, 1999),   # 1999: "Santa Cruz  2-2 Guabira" (o Real Santa Cruz, único da cidade sem nome na rodada)
    (r"la belgica", "La Bélgica", 1900, 2100),
    (r"royal pari( fc)?", "Royal Pari", 1990, 2100),
    (r"sport boys( warnes)?", "Sport Boys Warnes", 1990, 2100),
    (r"atletico pompeya", "Atlético Pompeya", 1900, 2100),
    (r"g(ualberto)? villarroel", "Gualberto Villarroel", 1900, 2100),
    # Oruro
    (r"san jose", "San José", 1942, 2100),
    (r"oruro royal", "Oruro Royal", 1900, 2100),
    (r"ingenieros", "Ingenieros", 1900, 2100),
    (r"miners japo|miner s japo", "Miner's Japo", 1900, 2100),
    (r"orcobol", "Orcobol", 1900, 2100),
    (r"metalsan", "Metalsan", 1900, 2100),
    (r"(cdt |cd totora )?real oruro", "Real Oruro", 1900, 2100),
    (r"san pedro", "San Pedro", 1900, 2100),
    # Sucre
    (r"indep(endiente)?\.? ?petrolero|independiente p$|independiente$", "Independiente Petrolero", 1932, 2100),
    (r"stormers petrolero", "Stormers Petrolero", 1900, 2100),
    (r"stormers", "Stormers", 1900, 2100),
    (r"magisterio", "Magisterio", 1900, 2100),
    (r"policar", "Policar", 1900, 2100),
    (r"francesa", "Francesa", 1900, 2100),
    (r"abb", "ABB", 2000, 2100),
    # Potosí
    (r"real potosi", "Real Potosí", 1980, 2100),
    (r"nacional potosi", "Nacional Potosí", 1900, 2100),
    (r"wilst(ermann?)?\.? ?unificada", "Wilstermann Unificada", 1900, 2100),
    (r"wilst(ermann?)?\.? ?cooperativas?", "Wilstermann Cooperativas", 1900, 2100),
    (r"ind(ep(endiente)?)?\.? ?unificada", "Independiente Unificada", 1900, 2100),
    (r"bamin", "Bamin", 1900, 2100),
    # Tarija, Beni, Pando
    (r"ciclon", "Ciclón", 1900, 2100),
    (r"union central", "Unión Central", 1900, 2100),
    (r"real tomayapo", "Real Tomayapo", 1900, 2100),
    (r"real mamore", "Real Mamoré", 1900, 2100),
    (r"20 de agosto", "20 de Agosto", 1900, 2100),
    (r"real beni", "Real Beni", 1900, 2100),
    (r"libertad( gran mamore)?", "Libertad Gran Mamoré", 2000, 2100),
    (r"vaca diez", "Vaca Díez", 1900, 2100),
]

_LIXO = re.compile(r"^\s*[-/]\s*|\s*-\s*$|\[\[|\]\]", re.I)
# cidade antes do nome nas páginas de 1995 a 1998 ("Cochabamba Wilstermann")
_CIDADE = re.compile(r"^(cochabamba|santa cruz|la paz|oruro|sucre|potosi|tarija) (?=\S)")


def _regra(k: str, ano: int) -> str | None:
    for kk in (k, re.sub(r"^(club|c|cd|csd) ", "", k)):
        for rx, exib, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.fullmatch(f"(?:{rx})" + r"(?:\s.*)?", kk):
                return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    k = chave(_LIXO.sub("", nome.strip()))
    achado = _regra(k, ano)
    if (achado is None or (achado == "La Paz FC" and k != "la paz fc")) and 1995 <= ano <= 1999 and _CIDADE.match(k):
        achado = _regra(_CIDADE.sub("", k), ano) or achado
    return achado


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
