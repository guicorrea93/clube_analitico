"""Clubes da Copa Ecuador: os do ecu-1 (coleta/ecu-1/clubes_ecu.py) mais os da Serie B, da Segunda Categoría e amadores que
só jogam a copa. As regras daqui vêm antes das do ecu-1 e casam o nome inteiro. Identidades pela Wikipédia em espanhol
("Copa Ecuador 2022"): "Portoviejo" é o Portoviejo Fútbol Club (não a LDU de Portoviejo), "Quito" é o Quito Fútbol Club,
"Danubio" é o Danubio Sporting Club e "Peñarol" é o Club Deportivo Peñarol (nomes diferentes dos clubes uruguaios).
A cidade só entra quando o nome a traz; nos outros, fica vazia (sem fonte).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ecu-1"))
import clubes_ecu  # noqa: E402
from rsssf_sul import chave  # noqa: E402

SEM = ("", "")
SD = ("Santo Domingo", "Santo Domingo de los Tsáchilas")
CLUBES_COPA: dict[str, tuple[str, str]] = {
    "7 de Febrero": SEM, "Aampetra": SEM, "Águilas (Equador)": SEM, "Alianza Cotopaxi": SEM,
    "Alianza de Guano": ("Guano", "Chimborazo"), "Anaconda": SEM, "Atlético Porteño": SEM,
    "Atlético Portoviejo": ("Portoviejo", "Manabí"), "Atlético Samborondón": ("Samborondón", "Guayas"),
    "Atlético Santo Domingo": SD, "Audaz Octubrino": SEM, "Brasilia (Equador)": SEM, "Búhos ULVR": ("Guayaquil", "Guayas"),
    "Chacaritas": SEM, "Chicos Malos": SEM, "Cuenca Juniors": ("Cuenca", "Azuay"), "Danubio Sporting Club": SEM,
    "Deportivo Morona": SEM, "Deportivo Santo Domingo": SD, "Dunamis 04": SEM, "Duros del Balón": SEM,
    "Estudiantes de Cuenca": ("Cuenca", "Azuay"), "Independiente de Azogues": ("Azogues", "Cañar"),
    "Independiente Juniors": SEM, "Insutec": SEM, "La Cantera": SEM, "La Gloria": SEM, "La Unión (Equador)": SEM,
    "Leones de Atuntaqui": ("Atuntaqui", "Imbabura"), "Leones del Norte": SEM, "Mineros (Equador)": SEM, "Orellanense": SEM,
    "Peñarol (Equador)": SEM, "Portoviejo FC": ("Portoviejo", "Manabí"), "Primero de Mayo": SEM, "Quito FC": ("Quito", "Pichincha"),
    "San Antonio (Equador)": SEM, "San Francisco (Equador)": SEM, "San Pedro (Equador)": SEM,
    "Santa Elena Sumpa": ("Santa Elena", "Santa Elena"), "Spartak (Equador)": SEM, "Toreros (Equador)": SEM,
    "Unibolívar": SEM, "Unión Manabita": SEM, "Universitario de Píllaro": ("Píllaro", "Tungurahua"),
    "Valle Catamayo": ("Catamayo", "Loja"), "Vargas Torres": SEM,
    # 2024 e 2025 (fases iniciais pela Wikipédia em espanhol, pendência D5)
    "22 de Julio": ("Esmeraldas", "Esmeraldas"), "AV25": SEM, "Atlético Quinindé": ("Quinindé", "Esmeraldas"),
    "Atlético Vinotinto": SEM, "Baños Ciudad de Fuego": ("Baños", "Tungurahua"), "Deportivo Coca": ("El Coca", "Orellana"),
    "Deportivo Ibarra": ("Ibarra", "Imbabura"), "Ecuagenera": SEM, "Folke Anderson": ("Esmeraldas", "Esmeraldas"),
    "Grupo 7": SEM, "Huaquillas": ("Huaquillas", "El Oro"), "Junior (Equador)": SEM, "La Castellana": SEM,
    "La Paz (Equador)": SEM, "La Troncal": ("La Troncal", "Cañar"), "Leones (Equador)": SEM, "Liga de Cuenca": ("Cuenca", "Azuay"),
    "Liga de Macas": ("Macas", "Morona Santiago"), "Loja City": ("Loja", "Loja"), "Luz Valdivia": SEM,
    "Miguel Iturralde": SEM, "Montúfar": ("San Gabriel", "Carchi"), "Municipal de La Troncal": ("La Troncal", "Cañar"),
    "Naranja Mekánica": SEM, "Panamericana": SEM, "Río Aguarico": ("", "Sucumbíos"), "Río Babahoyo": ("Babahoyo", "Los Ríos"),
    "San Camilo": SEM, "Sembrando Buenos Campeones": SEM, "Sportivo Loja": ("Loja", "Loja"), "Vicentino Dragons": SEM,
}
# (regex sobre a chave do nome, nome de exibição); casa o nome inteiro; valem de 2018 em diante (a copa de 1970 só tem clubes do ecu-1)
REGRAS_COPA: list[tuple[str, str]] = [
    (r"7 de febrero", "7 de Febrero"), (r"aampetra", "Aampetra"), (r"aguilas", "Águilas (Equador)"),
    (r"alianza cotopaxi", "Alianza Cotopaxi"), (r"alianza de guano", "Alianza de Guano"), (r"anaconda", "Anaconda"),
    (r"atletico porteno", "Atlético Porteño"), (r"atletico portoviejo", "Atlético Portoviejo"),
    (r"atletico samborondon", "Atlético Samborondón"), (r"atl(etico)?( de)? santo domingo", "Atlético Santo Domingo"),
    (r"audaz oc[tu]+brino", "Audaz Octubrino"), (r"brasilia", "Brasilia (Equador)"), (r"buhos ulvr", "Búhos ULVR"),
    (r"chacaritas", "Chacaritas"), (r"chicos malos", "Chicos Malos"), (r"cuenca juniors", "Cuenca Juniors"),
    (r"danubio", "Danubio Sporting Club"), (r"deportivo morona", "Deportivo Morona"),
    (r"dep(ortivo)? santo domingo", "Deportivo Santo Domingo"), (r"dunamis( 04)?", "Dunamis 04"),
    (r"duros del balon", "Duros del Balón"), (r"estudiantes de cuenca", "Estudiantes de Cuenca"),
    (r"independiente azogues", "Independiente de Azogues"), (r"independiente juniors", "Independiente Juniors"),
    (r"ins[ue]l?tec", "Insutec"), (r"la cantera", "La Cantera"), (r"la gloria", "La Gloria"), (r"la union", "La Unión (Equador)"),
    (r"leones atuntaqui", "Leones de Atuntaqui"), (r"leones del norte", "Leones del Norte"), (r"mineros", "Mineros (Equador)"),
    (r"orellanense", "Orellanense"), (r"penarol", "Peñarol (Equador)"), (r"portoviejo", "Portoviejo FC"),
    (r"primero de mayo", "Primero de Mayo"), (r"quito", "Quito FC"), (r"san antonio", "San Antonio (Equador)"),
    (r"san francisco", "San Francisco (Equador)"), (r"san pedro", "San Pedro (Equador)"), (r"santa elena sumpa", "Santa Elena Sumpa"),
    (r"spartak", "Spartak (Equador)"), (r"toreros", "Toreros (Equador)"), (r"unibolivar", "Unibolívar"),
    (r"union manabita", "Unión Manabita"), (r"universitario pillaro", "Universitario de Píllaro"),
    (r"valle catamayo", "Valle Catamayo"), (r"vargas torres", "Vargas Torres"),
    # 2024 e 2025
    (r"22 de julio", "22 de Julio"), (r"av ?25", "AV25"), (r"atletico quininde", "Atlético Quinindé"),
    (r"atletico vinotinto", "Atlético Vinotinto"), (r"banos ciudad de fuego", "Baños Ciudad de Fuego"),
    (r"deportivo coca", "Deportivo Coca"), (r"deportivo ibarra", "Deportivo Ibarra"), (r"ecuagenera", "Ecuagenera"),
    (r"folke anderson", "Folke Anderson"), (r"grupo 7", "Grupo 7"), (r"huaquillas", "Huaquillas"), (r"junior", "Junior (Equador)"),
    (r"la castellana", "La Castellana"), (r"la paz", "La Paz (Equador)"), (r"la troncal", "La Troncal"),
    (r"leones", "Leones (Equador)"), (r"liga de cuenca", "Liga de Cuenca"), (r"liga de macas", "Liga de Macas"),
    (r"loja city", "Loja City"), (r"luz valdivia", "Luz Valdivia"), (r"miguel iturralde", "Miguel Iturralde"),
    (r"montufar", "Montúfar"), (r"municipal de la troncal", "Municipal de La Troncal"), (r"naranja mekanica", "Naranja Mekánica"),
    (r"panamericana", "Panamericana"), (r"rio aguarico", "Río Aguarico"), (r"rio babahoyo", "Río Babahoyo"),
    (r"san camilo", "San Camilo"), (r"sembrando buenos campeones", "Sembrando Buenos Campeones"),
    (r"sportivo loja", "Sportivo Loja"), (r"vicentino dragons", "Vicentino Dragons"),
]
CLUBES = {**clubes_ecu.CLUBES, **CLUBES_COPA}
assert all(e in CLUBES for _, e in REGRAS_COPA), [e for _, e in REGRAS_COPA if e not in CLUBES]


def clube(nome: str, ano: int) -> str | None:
    """Nome de exibição: as regras da copa (nome inteiro) e, sem elas, as do ecu-1."""
    k = re.sub(r"\s+", " ", chave(nome)).strip()
    if ano >= 2018:
        for rx, exib in REGRAS_COPA:
            if re.fullmatch(rx, k):
                return exib
    return clubes_ecu.clube(nome, ano)
