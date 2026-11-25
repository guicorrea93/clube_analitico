"""Clubes da Copa Venezuela: os do ven-1 (coleta/ven-1/clubes_ven.py) mais os amadores e das divisões de acesso que só
jogam a copa. As regras daqui vêm antes das do ven-1 e casam o nome inteiro.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ven-1"))
import clubes_ven  # noqa: E402
from rsssf_sul import chave  # noqa: E402

SEM = ("", "")
CLUBES_COPA: dict[str, tuple[str, str]] = {
    # era amadora
    "Barrio Nuevo": ("Caracas", "Distrito Capital"), "San Bernardino": ("Caracas", "Distrito Capital"),
    # 2007 em diante (Segunda e Tercera División, amadores)
    "Academia Emeritense": ("Mérida", "Mérida"), "Academia San José": SEM, "América FC (Venezuela)": SEM,
    "Atlético Cojedes": ("San Carlos", "Cojedes"), "Atlético Córdova": SEM, "Atlético Furrial": ("El Furrial", "Monagas"),
    "Atlético Guanare": ("Guanare", "Portuguesa"), "Atlético La Cruz": SEM, "Atlético Miranda": SEM,
    "Atlético Nacional (Venezuela)": SEM, "Atlético Orinoco": SEM, "Atlético PDVSA Gas": ("", "Anzoátegui"),
    "Atlético Turén": ("Turén", "Portuguesa"), "Atlético Varyná": ("Barinas", "Barinas"), "Baralt FC": ("", "Zulia"),
    "Bolívar SC": SEM, "CALH FC": SEM, "Cenfemaca FC": SEM, "Chicó de Guayana": ("Ciudad Guayana", "Bolívar"),
    "Ciudad Vinotinto": SEM, "Deportivo Apure": ("", "Apure"), "Deportivo Barinas": ("Barinas", "Barinas"),
    "Deportivo Madeirense": SEM, "Deportivo Metropolitano": SEM, "Deportivo Nueva Esparta": ("", "Nueva Esparta"),
    "Deportivo Peñarol": SEM, "Deportivo San Antonio": ("San Antonio del Táchira", "Táchira"),
    "Diamantes de Guayana": ("Ciudad Guayana", "Bolívar"), "Dynamo Puerto": SEM, "Estudiantes de Caroní": ("", "Bolívar"),
    "Fundación AIFI": SEM, "Fundación Cesarger": SEM, "Guatire FC": ("Guatire", "Miranda"), "Hermandad Gallega": ("Valencia", "Carabobo"),
    "Independiente La Fría": ("La Fría", "Táchira"), "Internacional Turén": ("Turén", "Portuguesa"),
    "La Victoria FC": ("La Victoria", "Aragua"), "Libertador FC": SEM, "Lotería del Táchira": ("San Cristóbal", "Táchira"),
    "Margarita FC": ("", "Nueva Esparta"), "Marineros FC": SEM, "Minasoro": SEM, "Olímpico de Guárico": ("", "Guárico"),
    "Omega FC": SEM, "Orinoco FC": SEM, "Pacairigua": ("Guatire", "Miranda"), "Pellícanos FC": SEM,
    "Petroleros de Anzoátegui": ("", "Anzoátegui"), "Policía de Lara": ("Barquisimeto", "Lara"), "Potros de Barinas": ("Barinas", "Barinas"),
    "REDI Colón": SEM, "Real Anzoátegui": ("", "Anzoátegui"), "Real Bolívar": ("", "Bolívar"), "Real Frontera": ("", "Táchira"),
    "Santa Bárbara FC": SEM, "SC Guaraní (Venezuela)": SEM, "TFC Maracaibo": ("Maracaibo", "Zulia"), "Talentos del Sur": SEM,
    "Titanes FC": SEM, "UCLA FC": ("Barquisimeto", "Lara"), "UNEFA FC": SEM, "Universitario FC (Venezuela)": SEM,
    "Unión Atlético Falcón": ("", "Falcón"), "Unión Atlético Lagunillas": ("Lagunillas", "Zulia"), "Unión Atlético Piar": ("", "Bolívar"),
    "Unión Atlético San Antonio": ("San Antonio del Táchira", "Táchira"), "Unión Atlético Trujillo": ("", "Trujillo"),
    "Unión Liga Municipal": SEM, "Yaracuy FC": ("", "Yaracuy"),
    # fase de grupos de 2024 (Wikipédia em espanhol)
    "Academia Rey": SEM, "Deportivo Miranda": ("", "Miranda"), "Héroes de Falcón": ("", "Falcón"),
}
_T = 9999
# (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano); casa o nome inteiro
REGRAS_COPA: list[tuple[str, str, int, int]] = [
    # clubes do ven-1 em grafias que as regras dele não pegam
    (r"estudiantes", "Loyola", 1942, 1944),   # "Estudiantes [aka Loyola SC]" (RSSSF, venez43)
    (r"canarias", "Unión Deportiva Canarias", 0, _T), (r"unversidad de los andes", "Universidad de Los Andes", 0, _T),
    (r"estudiantes de merfida", "Estudiantes de Mérida", 0, _T), (r"minerfos de guayana", "Mineros de Guayana", 0, _T),
    (r"(awd )?(fund |fundacion )?(atl|atletico) el vigia( fc)?", "Atlético El Vigía", 0, _T),
    (r"(ac )?lala( fc)?", "LALA FC", 0, _T), (r"angostura( fc)?", "Angostura FC", 0, _T), (r"arroceros fc", "Arroceros de Calabozo", 0, _T),
    (r"barquisimeto", "Barquisimeto FC", 0, _T), (r"deportivo jbl( del zulia)?", "Deportivo JBL Zulia", 0, _T),
    (r"catalonia fc", "Catalonia", 0, _T), (r"el vigia", "El Vigía FC", 2014, _T),
    # clubes que só jogam a copa
    (r"barrio nuevo fbc", "Barrio Nuevo", 0, _T), (r"san bernardino fbc", "San Bernardino", 0, _T),
    (r"acad(emia)? emeritense", "Academia Emeritense", 0, _T), (r"acad san jose", "Academia San José", 0, _T),
    (r"america fc", "América FC (Venezuela)", 2000, _T), (r"(atl|atletico) cojedes", "Atlético Cojedes", 0, _T),
    (r"(atl|atletico) cordova", "Atlético Córdova", 0, _T), (r"(atl|atletico) furrial", "Atlético Furrial", 0, _T),
    (r"atletico guanare", "Atlético Guanare", 0, _T), (r"atletico la cruz", "Atlético La Cruz", 0, _T),
    (r"(atletico|ca) miranda", "Atlético Miranda", 0, _T), (r"atletico nacional", "Atlético Nacional (Venezuela)", 0, _T),
    (r"atl orinoco", "Atlético Orinoco", 0, _T), (r"(atl|atletico) pdvsa ?gas fc", "Atlético PDVSA Gas", 0, _T),
    (r"(atl|atletico) turen", "Atlético Turén", 0, _T), (r"atl varyna cf", "Atlético Varyná", 0, _T), (r"baralt fc", "Baralt FC", 0, _T),
    (r"bolivar sc", "Bolívar SC", 0, _T), (r"calh fc", "CALH FC", 0, _T), (r"cenfemaca fc", "Cenfemaca FC", 0, _T),
    (r"chico de guayana", "Chicó de Guayana", 0, _T), (r"ciudad vinotinto", "Ciudad Vinotinto", 0, _T),
    (r"dvo apure", "Deportivo Apure", 0, _T), (r"(deportivo|deportvo|dvo) barinas", "Deportivo Barinas", 0, _T),
    (r"dvo madeirense", "Deportivo Madeirense", 0, _T), (r"deportivo metropolitano", "Deportivo Metropolitano", 0, _T),
    (r"deportivo nueva esparta", "Deportivo Nueva Esparta", 0, _T), (r"dvo penarol", "Deportivo Peñarol", 0, _T),
    (r"(cd|deportivo) san antonio", "Deportivo San Antonio", 0, _T), (r"diamantes de guayana", "Diamantes de Guayana", 0, _T),
    (r"dynamo puerto", "Dynamo Puerto", 0, _T), (r"estudiantes de caroni", "Estudiantes de Caroní", 0, _T),
    (r"fundacion aifi", "Fundación AIFI", 0, _T), (r"(fund|fundacion) cesarger", "Fundación Cesarger", 0, _T),
    (r"guatire fc", "Guatire FC", 0, _T), (r"hermandad gallega", "Hermandad Gallega", 0, _T),
    (r"independiente la fria", "Independiente La Fría", 0, _T), (r"internacional turen", "Internacional Turén", 0, _T),
    (r"la victoria fc", "La Victoria FC", 0, _T), (r"libertador", "Libertador FC", 0, _T),
    (r"loteria del tachira( fc)?", "Lotería del Táchira", 0, _T), (r"margarita( fc)?", "Margarita FC", 0, _T),
    (r"marineros fc", "Marineros FC", 0, _T), (r"minasoro( fc)?", "Minasoro", 0, _T), (r"olimpico de guarico", "Olímpico de Guárico", 0, _T),
    (r"omega fc", "Omega FC", 0, _T), (r"orinoco fc", "Orinoco FC", 0, _T), (r"pacairigua", "Pacairigua", 0, _T),
    (r"pellicanos? fc", "Pellícanos FC", 0, _T), (r"petroleros( de anzoategui)?", "Petroleros de Anzoátegui", 2015, _T),
    (r"policia de lara( fc)?", "Policía de Lara", 0, _T), (r"potros de barinas", "Potros de Barinas", 0, _T),
    (r"redi colon", "REDI Colón", 0, _T), (r"real anzoategui", "Real Anzoátegui", 0, _T), (r"real bolivar( fc)?", "Real Bolívar", 0, _T),
    (r"real frontera", "Real Frontera", 0, _T), (r"santa barbara fc", "Santa Bárbara FC", 0, _T),
    (r"(club |sc |ec )?guarani( sc)?", "SC Guaraní (Venezuela)", 2000, _T), (r"tfc maracaibo", "TFC Maracaibo", 0, _T),
    (r"talentos del sur", "Talentos del Sur", 0, _T), (r"titanes", "Titanes FC", 0, _T), (r"ucla fc", "UCLA FC", 0, _T),
    (r"unefa fc", "UNEFA FC", 0, _T), (r"universitario fc", "Universitario FC (Venezuela)", 0, _T),
    (r"(ua|union atletico) falcon", "Unión Atlético Falcón", 0, _T), (r"ua lagunillas", "Unión Atlético Lagunillas", 0, _T),
    (r"(ua|union atletico) piar( fc)?", "Unión Atlético Piar", 0, _T), (r"ua san antonio", "Unión Atlético San Antonio", 0, _T),
    (r"(ua|union atletico) trujillo", "Unión Atlético Trujillo", 0, _T), (r"union liga municipal", "Unión Liga Municipal", 0, _T),
    (r"yaracuy", "Yaracuy FC", 0, _T),
    # fase de grupos de 2024 (Wikipédia em espanhol, nomes curtos)
    (r"academia rey( fc)?", "Academia Rey", 0, _T), (r"deportivo miranda( fc)?", "Deportivo Miranda", 0, _T),
    (r"heroes de falcon( fc)?", "Héroes de Falcón", 0, _T), (r"aifi", "Fundación AIFI", 0, _T),
    (r"bolivar", "Bolívar SC", 2024, _T), (r"anzoategui", "Anzoátegui FC", 2020, _T),
    # a RSSSF chama de "Deportivo Anzoátegui" o Anzoátegui FC (2021) no mata-mata de 2024 (a Wikipédia liga ao de 2021)
    (r"(deportivo|dep|dvo) anzoategui( sc| fc)?", "Anzoátegui FC", 2021, _T),
]
CLUBES = {**clubes_ven.CLUBES, **CLUBES_COPA}
assert all(e in CLUBES for _, e, _, _ in REGRAS_COPA), [e for _, e, _, _ in REGRAS_COPA if e not in CLUBES]
_EXIB = {chave(c): c for c in CLUBES}


def clube(nome: str, ano: int) -> str | None:
    """Nome de exibição: as regras da copa (nome inteiro) e, sem elas, as do ven-1."""
    k = re.sub(r"\s+", " ", chave(nome)).strip()
    for rx, exib, a0, a1 in REGRAS_COPA:
        if a0 <= ano <= a1 and re.fullmatch(rx, k):
            return exib
    return clubes_ven.clube(nome, ano) or _EXIB.get(k)
