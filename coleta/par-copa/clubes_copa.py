"""Clubes da Copa Paraguay: os do par-1 (coleta/par-1/clubes_par.py) mais os da Intermedia, da Primera B e C e do interior
(UFI) que só jogam a copa. As regras daqui vêm antes das do par-1 e casam o nome inteiro: "Nacional (Yby Yaú)" não é o
Nacional de Asunción, "Olimpia (Itá)" não é o Olimpia, "12 de Octubre (Santo Domingo)" não é o de Itauguá.

Nomes únicos no mundo: clube do interior leva a cidade quando a RSSSF a dá ("Nacional de Yby Yaú"). A cidade só é
preenchida quando a página a traz (entre parênteses) ou o clube já está no par-1; nos outros, fica vazia (sem fonte).
Grafias sem cidade e com mais de um clube possível: "24 de Setiembre" fica com o de Valle Pucú e "Cristóbal Colón" com o de
J. Augusto Saldívar (os dois da Intermedia, os que chegam às fases finais); dito no recado.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "par-1"))
import clubes_par  # noqa: E402
from rsssf_sul import chave  # noqa: E402

SEM = ("", "")
CLUBES_COPA: dict[str, tuple[str, str]] = {
    "1° de Marzo (FDM)": ("Fernando de la Mora", "Central"), "12 de Octubre de Paso Yobái": ("Paso Yobái", "Guairá"),
    "12 de Octubre de Santo Domingo": SEM, "12 de Octubre de San Pedro": ("San Pedro de Ycuamandiyú", "San Pedro"),
    "15 de Agosto (BA)": SEM, "15 de Agosto (S)": SEM, "16 de Agosto": SEM, "19 de Marzo": SEM,
    "22 de Setiembre de Encarnación": ("Encarnación", "Itapúa"), "24 de Junio": SEM,
    "24 de Setiembre de Valle Pucú": ("Areguá", "Central"), "29 de Setiembre": SEM, "3 de Mayo": SEM, "3 de Noviembre": SEM,
    "4 de Mayo": SEM, "5 de Octubre de Santa Elena": SEM, "8 de Setiembre": SEM, "Aquidabán": SEM, "Athletic Club (Paraguai)": SEM,
    "Athletic FBC": SEM, "Atlético 13 de Junio": SEM, "Atlético 3 de Febrero": SEM, "Atlético Amambay": SEM,
    "Atlético Juventud": SEM, "Atlético Mil Palos": SEM, "Atlético Trébol": SEM, "Atyrá FC": ("Atyrá", "Cordillera"),
    "Benjamín Aceval": ("Benjamín Aceval", "Presidente Hayes"), "Club Oriental (Paraguai)": SEM, "Coronel Martínez": SEM,
    "Cristóbal Colón de J. Augusto Saldívar": ("J. Augusto Saldívar", "Central"), "Cristóbal Colón de Ñemby": ("Ñemby", "Central"),
    "Deportivo Alto Paraguay": SEM, "Deportivo Caaguazú": ("Caaguazú", "Caaguazú"), "Deportivo Carapeguá": ("Carapeguá", "Paraguarí"),
    "Deportivo Juventud": SEM, "Deportivo La Colmena": SEM, "Deportivo Minga Guazú": ("Minga Guazú", "Alto Paraná"),
    "Deportivo Obrero": SEM, "Deportivo Pinozá": SEM, "Deportivo Primavera": SEM, "Encarnación FC": ("Encarnación", "Itapúa"),
    "Fulgencio Yegros": SEM, "General Caballero JLM": clubes_par.CLUBES["General Caballero JLM"],
    "Independiente de Nanawa": ("Nanawa", "Presidente Hayes"), "Independiente de Pedro Juan Caballero": ("Pedro Juan Caballero", "Amambay"),
    "Itoró": SEM, "Karai Chivé": SEM, "Liberación": SEM, "Mariscal Estigarribia": SEM, "Martín Ledesma": SEM,
    "Nacional de Yby Yaú": ("Yby Yaú", "Concepción"), "Nueva Estrella": SEM, "Obreros Unidos": SEM, "Olimpia de Itá": ("Itá", "Central"),
    "Pastoreo": SEM, "Pilcomayo": SEM, "Porvenir FC": SEM, "R.I. 3 Corrales": SEM, "San Antonio (SCD)": SEM,
    "Sol de América de Caaguazú": ("Caaguazú", "Caaguazú"), "Sol de Mayo": SEM, "Sport Colonial": SEM, "Sport Pocobá": SEM,
    "Sport Primavera": SEM, "Sport Puerto Diana": SEM, "Sport Santo Domingo": SEM, "Sport Sastreño": SEM,
    "Sport Valenzolano": SEM, "Sportivo Iteño": ("Itá", "Central"), "Sportivo Limpeño": ("Limpio", "Central"),
    "Sportivo San Juan": SEM, "Sud América (Paraguai)": SEM, "Teniente Fariña": SEM, "Teniente Rojas": SEM,
    "Valois Rivarola": SEM,
}
# (regex sobre a chave do nome, nome de exibição); casa o nome inteiro; valem de 2018 em diante (a Copa Paraguay começou em 2018)
REGRAS_COPA: list[tuple[str, str]] = [
    (r"1 de marzo( fbc| fdm)?", "1° de Marzo (FDM)"), (r"12 de octubre paso yobai", "12 de Octubre de Paso Yobái"),
    (r"12 de octubre santo domingo", "12 de Octubre de Santo Domingo"), (r"12 de octubre vr san pedro", "12 de Octubre de San Pedro"),
    (r"15 de agosto ba", "15 de Agosto (BA)"), (r"15 de agosto s", "15 de Agosto (S)"), (r"16 de agosto", "16 de Agosto"),
    (r"19 de marzo( fbc)?", "19 de Marzo"), (r"22 de setiembre encarnacion", "22 de Setiembre de Encarnación"),
    (r"24 de junio", "24 de Junio"), (r"24 de setiembre( de valle pucu| valle pucu| vp)?", "24 de Setiembre de Valle Pucú"),
    (r"29 de sep?tiembre", "29 de Setiembre"), (r"3 de februero( ciudad del este| fbc)?", "3 de Febrero"),
    (r"3 de mayo", "3 de Mayo"), (r"3 de novi?embre", "3 de Noviembre"), (r"4 de mayo", "4 de Mayo"),
    (r"5 de octubre( santa elena)?", "5 de Octubre de Santa Elena"), (r"8 de setiembre", "8 de Setiembre"),
    (r"aquidaban", "Aquidabán"), (r"athletic club", "Athletic Club (Paraguai)"), (r"athletic fbc", "Athletic FBC"),
    (r"atletico 13 de jun[iu]o", "Atlético 13 de Junio"), (r"atletico 3 de febrero", "Atlético 3 de Febrero"),
    (r"atletico amambay", "Atlético Amambay"), (r"atletico juventud", "Atlético Juventud"), (r"atletico mil palos", "Atlético Mil Palos"),
    (r"atletico trebol", "Atlético Trébol"), (r"atyra", "Atyrá FC"), (r"benjamin aceval", "Benjamín Aceval"),
    (r"(club )?oriental", "Club Oriental (Paraguai)"), (r"coronel martinez", "Coronel Martínez"),
    (r"(club )?cristobal colon( jas| ja saldivar| juan augusto sald[ei]var)?", "Cristóbal Colón de J. Augusto Saldívar"),
    (r"cristobal colon nemby", "Cristóbal Colón de Ñemby"), (r"deportico capiata", "Deportivo Capiatá"),
    (r"deportivo alto paraguay", "Deportivo Alto Paraguay"), (r"deportivo caaguazu", "Deportivo Caaguazú"),
    (r"deportivo carapegua", "Deportivo Carapeguá"), (r"deportivo juventud", "Deportivo Juventud"),
    (r"deportivo la colmena", "Deportivo La Colmena"), (r"deportivo minga guazu", "Deportivo Minga Guazú"),
    (r"deportivo obrero", "Deportivo Obrero"), (r"deportivo pinoza", "Deportivo Pinozá"), (r"deportivo primavera", "Deportivo Primavera"),
    (r"encarnacion", "Encarnación FC"), (r"fulgencio yegros", "Fulgencio Yegros"),
    (r"general caballero (jl mall|juan leon mallorquin)", "General Caballero JLM"),
    (r"independiente nanawa", "Independiente de Nanawa"), (r"independiente pedro juan caballero", "Independiente de Pedro Juan Caballero"),
    (r"itoro", "Itoró"), (r"karai chive", "Karai Chivé"), (r"liberacion", "Liberación"),
    (r"mariscal estigarribia", "Mariscal Estigarribia"), (r"martin ledesma", "Martín Ledesma"),
    (r"nacional yby yau", "Nacional de Yby Yaú"), (r"nueva estrella", "Nueva Estrella"), (r"obreros unidos", "Obreros Unidos"),
    (r"olimpia ita", "Olimpia de Itá"), (r"pastoreo", "Pastoreo"), (r"pilcomayo", "Pilcomayo"), (r"porvenir( fc)?", "Porvenir FC"),
    (r"r i 3 corrales", "R.I. 3 Corrales"), (r"scd san antonio", "San Antonio (SCD)"),
    (r"sol de america caaguazu", "Sol de América de Caaguazú"), (r"sol de mayo", "Sol de Mayo"),
    (r"sport ameliano", "Sportivo Ameliano"), (r"sport colonial", "Sport Colonial"), (r"sport pocoba", "Sport Pocobá"),
    (r"sport prima ?vera", "Sport Primavera"), (r"sport puerto diana", "Sport Puerto Diana"),
    (r"sport santo domingo", "Sport Santo Domingo"), (r"sport sastreno", "Sport Sastreño"), (r"sport valenzolano", "Sport Valenzolano"),
    (r"sportivo iteno", "Sportivo Iteño"), (r"sportivo limpeno", "Sportivo Limpeño"), (r"sportivo san juan", "Sportivo San Juan"),
    (r"sud america", "Sud América (Paraguai)"), (r"te[bn]iente farina", "Teniente Fariña"), (r"teniente rojas", "Teniente Rojas"),
    (r"(sportivo )?valois rivarola", "Valois Rivarola"),
]
CLUBES = {**clubes_par.CLUBES, **CLUBES_COPA}
assert all(e in CLUBES for _, e in REGRAS_COPA), [e for _, e in REGRAS_COPA if e not in CLUBES]


def clube(nome: str, ano: int) -> str | None:
    """Nome de exibição: as regras da copa (nome inteiro) e, sem elas, as do par-1."""
    k = re.sub(r"\s+", " ", chave(nome)).strip()
    if ano >= 2018:
        for rx, exib in REGRAS_COPA:
            if re.fullmatch(rx, k):
                return exib
    return clubes_par.clube(nome, ano)
