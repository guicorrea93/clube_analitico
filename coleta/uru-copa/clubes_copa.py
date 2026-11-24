"""Clubes da Copa AUF Uruguay: os do uru-1 (coleta/uru-1/clubes_uru.py) mais os amadores da AUF e os do interior (OFI) que
só jogam a copa. As regras daqui vêm antes das do uru-1 e casam o nome inteiro (sem prefixo): "Wanderers Durazno" não é o
Montevideo Wanderers, "Central San José" não é o Central Español, "Huracán Paysandú" não é o Huracán Buceo.

Nomes únicos no mundo: clube do interior leva a cidade ("Wanderers de Durazno", "Huracán de Rivera"); homônimo de clube de
outro país também ("Platense de Montevideo", "Sportivo Italiano de Montevideo"). Clube que já está no uru-1 fica com o nome
de lá (Paysandú Bella Vista, Colón de Montevideo, Alto Perú, Lito). Cidades pela RSSSF (listas de participantes) e pela
Wikipédia em espanhol (Primera e Segunda División Amateur de Uruguay); sem fonte, a cidade fica vazia.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "uru-1"))
import clubes_uru  # noqa: E402
from rsssf_sul import chave  # noqa: E402

MVD = ("Montevideo", "Montevideo")
CLUBES_COPA: dict[str, tuple[str, str]] = {
    # interior (OFI)
    "18 de Julio de Fray Bentos": ("Fray Bentos", "Río Negro"), "Arsenal de Salto": ("Salto", "Salto"),
    "Atenas de Tala": ("Tala", "Canelones"), "Atlético Florida": ("Florida", "Florida"),
    "Barrio Olímpico de Minas": ("Minas", "Lavalleja"), "Boquita de Sarandí Grande": ("Sarandí Grande", "Florida"),
    "Bristol de Mercedes": ("Mercedes", "Soriano"), "Campana de Libertad": ("Libertad", "San José"),
    "Central de San José": ("San José de Mayo", "San José"), "Ferro Carril de Salto": ("Salto", "Salto"),
    "Huracán de Paysandú": ("Paysandú", "Paysandú"), "Huracán de Rivera": ("Rivera", "Rivera"),
    "Huracán de Treinta y Tres": ("Treinta y Tres", "Treinta y Tres"),
    "Ituzaingó de Punta del Este": ("Punta del Este", "Maldonado"), "Juanicó": ("Juanicó", "Canelones"),
    "Juventud de Colonia": ("Colonia del Sacramento", "Colonia"), "Juventud Unida de Libertad": ("Libertad", "San José"),
    "Laureles de Fray Bentos": ("Fray Bentos", "Río Negro"), "Lavalleja de Minas": ("Minas", "Lavalleja"),
    "Lavalleja de Rocha": ("Rocha", "Rocha"), "Libertad de San Carlos": ("San Carlos", "Maldonado"),
    "Litoral de Paysandú": ("Paysandú", "Paysandú"), "Melo Wanderers": ("Melo", "Cerro Largo"),
    "Nacional de Nueva Helvecia": ("Nueva Helvecia", "Colonia"), "Palermo de Rocha": ("Rocha", "Rocha"),
    "Piriápolis FC": ("Piriápolis", "Maldonado"), "Porongos de Flores": ("Trinidad", "Flores"),
    "Progreso de Atlántida": ("Estación Atlántida", "Canelones"), "Quilmes de Florida": ("Florida", "Florida"),
    "Río Negro de San José": ("San José de Mayo", "San José"), "San Carlos (OFI)": ("San Carlos", "Maldonado"),
    "Santa Emilia de Cardona": ("Cardona", "Soriano"), "Sportivo Barracas de Dolores": ("Dolores", "Soriano"),
    "Universal de San José": ("San José de Mayo", "San José"), "Universitario de Salto": ("Salto", "Salto"),
    "Wanderers de Durazno": ("Durazno", "Durazno"), "Wanderers de Santa Lucía": ("Santa Lucía", "Canelones"),
    "Wanderers Juvenil de Tacuarembó": ("Tacuarembó", "Tacuarembó"),
    # amadores da AUF
    "Academia de Montevideo": MVD, "Artigas de Montevideo": MVD, "Bella Italia": MVD, "Canadian": MVD, "Cooper": MVD,
    "Deutscher FK": MVD, "Durazno FC": ("Durazno", "Durazno"), "Estudiantes del Plata": ("", ""),
    "Huracán de Paso de la Arena": MVD, "Los Halcones": MVD, "Mar de Fondo": MVD, "Oriental de La Paz": ("La Paz", "Canelones"),
    "Parque del Plata": ("Parque del Plata", "Canelones"), "Paso de la Arena": MVD, "Platense de Montevideo": MVD,
    "Potencia": MVD, "Rincón de Carrasco": ("", ""), "Salto FC": ("Salto", "Salto"), "Salus": MVD,
    "Sportivo Italiano de Montevideo": MVD, "Terremoto": MVD, "Uruguay Montevideo": MVD,
}
# (regex sobre a chave do nome, nome de exibição); casa o nome inteiro; valem de 2022 em diante (a Copa AUF começou em 2022)
REGRAS_COPA: list[tuple[str, str]] = [
    (r"18 de julio", "18 de Julio de Fray Bentos"), (r"(atl(etico)? )?arsenal( salto)?", "Arsenal de Salto"),
    (r"atenas tala|atenas de tala", "Atenas de Tala"), (r"atletico florida", "Atlético Florida"),
    (r"barrio ol(impico)?( minas)?", "Barrio Olímpico de Minas"), (r"boquita( sarandi gr(ande)?)?", "Boquita de Sarandí Grande"),
    (r"bristol", "Bristol de Mercedes"), (r"campana libertad", "Campana de Libertad"),
    (r"central san jose", "Central de San José"), (r"ferro ?carril( salto)?", "Ferro Carril de Salto"),
    (r"huracan paysandu", "Huracán de Paysandú"), (r"huracan rivera", "Huracán de Rivera"),
    (r"huracan (33|treinta y tres)", "Huracán de Treinta y Tres"), (r"huracan", "Huracán de Paso de la Arena"),
    (r"ituzaingo( pde| punta del este)?", "Ituzaingó de Punta del Este"), (r"juanico", "Juanicó"),
    (r"juventud colonia|juventud de colonia", "Juventud de Colonia"), (r"juventud unida( l(ibertad)?)?", "Juventud Unida de Libertad"),
    (r"laureles( fb| fray bentos)?", "Laureles de Fray Bentos"), (r"lav[ae]ll?eja minas", "Lavalleja de Minas"),
    (r"lavalleja rocha", "Lavalleja de Rocha"), (r"libertad (s carlos|de san carlos)", "Libertad de San Carlos"),
    (r"l[ií]toral( paysandu)?", "Litoral de Paysandú"), (r"melo wanderers", "Melo Wanderers"),
    (r"nac(ional)? n ?helv(ecia)?|nacional de nueva helvecia", "Nacional de Nueva Helvecia"), (r"palermo", "Palermo de Rocha"),
    (r"piriapolis( fc)?", "Piriápolis FC"), (r"porongos( flores| de flores)?", "Porongos de Flores"),
    (r"progreso atlantida", "Progreso de Atlántida"), (r"quilmes( florida)?", "Quilmes de Florida"),
    (r"rio negro( san jose| de san jose)?", "Río Negro de San José"), (r"san carlos", "San Carlos (OFI)"),
    (r"santa emilia", "Santa Emilia de Cardona"), (r"(sp|sportivo) barracas|barracas dolores", "Sportivo Barracas de Dolores"),
    (r"universal san jose", "Universal de San José"),
    (r"univ(tario|ersit|ersitario)? salto|universitario de salto", "Universitario de Salto"),
    (r"wanderers durazno|wanderers de durazno", "Wanderers de Durazno"), (r"wanderers (s|santa) lucia", "Wanderers de Santa Lucía"),
    (r"wanderers juvenil", "Wanderers Juvenil de Tacuarembó"),
    (r"bella vista pays(andu)?|atl(etico)? bella vista", "Paysandú Bella Vista"),
    (r"academia", "Academia de Montevideo"), (r"artigas", "Artigas de Montevideo"), (r"bella italia", "Bella Italia"),
    (r"canadian", "Canadian"), (r"cooper", "Cooper"), (r"deutscher( fk)?", "Deutscher FK"), (r"durazno", "Durazno FC"),
    (r"estudiantes (del )?plata", "Estudiantes del Plata"), (r"halcones", "Los Halcones"), (r"mar de fondo", "Mar de Fondo"),
    (r"oriental", "Oriental de La Paz"), (r"parque del plata", "Parque del Plata"), (r"paso de la arena", "Paso de la Arena"),
    (r"platense", "Platense de Montevideo"), (r"potencia", "Potencia"), (r"rincon( de carrasco)?", "Rincón de Carrasco"),
    (r"salto", "Salto FC"), (r"salus", "Salus"), (r"italiano", "Sportivo Italiano de Montevideo"), (r"terremoto", "Terremoto"),
    (r"uruguay montevideo", "Uruguay Montevideo"), (r"colon", "Colón de Montevideo"), (r"alto peru", "Alto Perú"),
    (r"lito", "Lito"),
]
CLUBES = {**clubes_uru.CLUBES, **CLUBES_COPA}
assert all(e in CLUBES for _, e in REGRAS_COPA), [e for _, e in REGRAS_COPA if e not in CLUBES]


def clube(nome: str, ano: int) -> str | None:
    """Nome de exibição: as regras da copa (nome inteiro) e, sem elas, as do uru-1."""
    k = re.sub(r"\s+", " ", chave(nome)).strip()
    if ano >= 2022:
        for rx, exib in REGRAS_COPA:
            if re.fullmatch(rx, k):
                return exib
    return clubes_uru.clube(nome, ano)
