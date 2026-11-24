"""Identidade dos clubes mexicanos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido ("Guadalajara", "Cruz Azul", "Pumas", "Tigres", "Tecos", "Leones Negros");
- o mesmo clube com outro nome: Centro Unión (1918-1920) é o América; Atlético Español (1971-1982) é o Necaxa vendido e
  renomeado, que voltou a se chamar Necaxa; Atlético Morelia e Monarcas são o Morelia; U.N.A.M. é o Pumas; U.A.N.L. e
  U. de N.L. são o Tigres; U.A.G., UAG, Estudiantes UAG e Estudiantes Tecos são o Tecos; U. de G. (Universidad de Guadalajara)
  é o Leones Negros; U.A.T. / U.A. Tamaulipas é o Correcaminos; T.M. Gallos Blancos (1994/95, o Tampico Madero jogando em
  Querétaro) é o Tampico Madero; Gallos Blancos (2002-2004) é o Querétaro; Oaxtepec/Ángeles (1984) é o Ángeles; Club México
  e México FC são o mesmo clube (a RSSSF usa os dois nomes); Pachuca AC (era amadora) é o Pachuca de hoje: o clube conta
  a própria história desde 1892 e celebra os 3 títulos amadores, com duas paradas (1922-1950 e 1952-1960) e a refundação
  de 1960 com o mesmo nome (pesquisa de 24/11/2026, aprovada pelo Guilherme; a RSSSF só diz que o clube se desfez em 1920);
- clubes diferentes, mesmo com nome parecido: Tigres da era amadora (Cidade do México, 1918-1922) e o Tigres da UANL;
  Mexico FC (1907/08) e Club México (desde 1910); Puebla AC (1904-1906) e Puebla (1944 em diante); Orizaba AC (1902-1904),
  ADO (Asociación Deportiva Orizabeña, 1943-1949) e Moctezuma de Orizaba; Laguna (Torreón, 1968-1977), Torreón (1969-1973) e
  Santos Laguna (1988 em diante); Tampico (até 1981) e Tampico Madero (1982 em diante); Celaya (1958-1961) e Atlético Celaya
  (1995-2002); San Luis (1971-1976) e San Luis FC (2002-2013), e o Atlético de San Luis (2019 em diante); Deportivo Neza
  (1978-1988) e Toros Neza (1993-2002); Cobras (Ciudad Juárez, 1986-1991), Indios (2008-2010) e FC Juárez (2019 em diante);
  Morelia e Mazatlán (2020, a vaga do Morelia levada a Mazatlán: clube novo);
- homônimo de clube do banco ou de outro pacote leva a cidade ou o país: América do México, Santos Laguna, Real Club España,
  Deportivo Español de México, Sporting de México, Nacional de Guadalajara, Laguna de Torreón (conferido com o banco e os
  outros pacotes em 23/11/2026).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-concacaf"))
from rsssf_concacaf import chave  # noqa: E402

CDMX = ("Ciudad de México", "Ciudad de México")
GDL = ("Guadalajara", "Jalisco")

# nome de exibição -> (cidade, estado)
CLUBES: dict[str, tuple[str, str]] = {
    # era amadora (Cidade do México, salvo indicação)
    "Orizaba AC": ("Orizaba", "Veracruz"), "Mexico Cricket Club": CDMX, "British Club": CDMX, "Reforma AC": CDMX,
    "Pachuca": ("Pachuca", "Hidalgo"), "Puebla AC": ("Puebla", "Puebla"), "San Pedro Golf Club": CDMX,
    "Mexico Country Club": CDMX, "Mexico FC (1907)": CDMX, "Popo FC": CDMX, "British-Popo": CDMX, "Club México": CDMX,
    "Real Club España": CDMX, "Real Club España B": CDMX, "Rovers FC": CDMX, "L'Amicale Française": CDMX, "Junior Club": CDMX,
    "Deportivo Español de México": CDMX, "Germania FV": CDMX, "América do México": CDMX, "España de Veracruz": CDMX,
    "Tigres (1918)": CDMX, "Asturias": CDMX, "Deportivo Internacional": CDMX, "Morelos": CDMX, "Luz y Fuerza": CDMX,
    "Tranvías": CDMX, "Guerra y Marina": CDMX, "Necaxa": CDMX, "Son-Sin": CDMX, "Aurrerá": CDMX, "Marte": CDMX,
    "Atlante": CDMX, "Leones": CDMX, "Sporting de México": CDMX, "Euzkadi": CDMX, "Selección Jalisco": GDL,
    "Moctezuma de Orizaba": ("Orizaba", "Veracruz"),
    # profissional
    "ADO Orizaba": ("Orizaba", "Veracruz"), "Atlas": GDL, "Guadalajara": GDL, "Veracruz": ("Veracruz", "Veracruz"),
    "Oro": GDL, "León": ("León", "Guanajuato"), "Puebla": ("Puebla", "Puebla"), "Monterrey": ("Monterrey", "Nuevo León"),
    "Tampico": ("Tampico", "Tamaulipas"), "San Sebastián de León": ("León", "Guanajuato"),
    "Zacatepec": ("Zacatepec", "Morelos"), "Toluca": ("Toluca", "Estado de México"), "La Piedad": ("La Piedad", "Michoacán"),
    "Irapuato": ("Irapuato", "Guanajuato"), "Cuautla": ("Cuautla", "Morelos"), "Zamora": ("Zamora", "Michoacán"),
    "Morelia": ("Morelia", "Michoacán"), "Celaya": ("Celaya", "Guanajuato"), "Nacional de Guadalajara": GDL,
    "Pumas": CDMX, "Poza Rica": ("Poza Rica", "Veracruz"), "Ciudad Madero": ("Ciudad Madero", "Tamaulipas"),
    "Cruz Azul": CDMX, "Jabatos de Nuevo León": ("Monterrey", "Nuevo León"), "Laguna de Torreón": ("Torreón", "Coahuila"),
    "Torreón": ("Torreón", "Coahuila"), "Jalisco": GDL, "Tigres": ("San Nicolás de los Garza", "Nuevo León"),
    "Unión de Curtidores": ("León", "Guanajuato"), "San Luis": ("San Luis Potosí", "San Luis Potosí"),
    "Atlético Potosino": ("San Luis Potosí", "San Luis Potosí"), "Leones Negros": GDL, "Tecos": ("Zapopan", "Jalisco"),
    "Atletas Campesinos": ("Querétaro", "Querétaro"), "Deportivo Neza": ("Nezahualcóyotl", "Estado de México"),
    "Oaxtepec": ("Oaxtepec", "Morelos"), "Ángeles": ("Puebla", "Puebla"), "Tampico Madero": ("Tampico", "Tamaulipas"),
    "Cobras": ("Ciudad Juárez", "Chihuahua"), "Santos Laguna": ("Torreón", "Coahuila"),
    "Correcaminos UAT": ("Ciudad Victoria", "Tamaulipas"), "Querétaro": ("Querétaro", "Querétaro"),
    "Toros Neza": ("Nezahualcóyotl", "Estado de México"), "Atlético Celaya": ("Celaya", "Guanajuato"),
    "Colibríes de Morelos": ("Cuernavaca", "Morelos"), "Jaguares de Chiapas": ("Tuxtla Gutiérrez", "Chiapas"),
    "Dorados": ("Culiacán", "Sinaloa"), "San Luis FC": ("San Luis Potosí", "San Luis Potosí"),
    "Indios": ("Ciudad Juárez", "Chihuahua"), "Tijuana": ("Tijuana", "Baja California"), "Lobos BUAP": ("Puebla", "Puebla"),
    "Atlético de San Luis": ("San Luis Potosí", "San Luis Potosí"), "FC Juárez": ("Ciudad Juárez", "Chihuahua"),
    "Mazatlán": ("Mazatlán", "Sinaloa"),
}

REGRAS: list[tuple[str, str, int, int]] = [
    # era amadora
    (r"orizaba( ac)?", "Orizaba AC", 1900, 1930),
    (r"(mexico|méxico) (cricket club|cc|cr club)", "Mexico Cricket Club", 1900, 1930),
    (r"british (club|fc)", "British Club", 1900, 1930),
    (r"british popo", "British-Popo", 1900, 1930),
    (r"reforma( ac| athletic club)?", "Reforma AC", 1900, 1930),
    (r"pachuca( ac| athletic club)?", "Pachuca", 1900, 2100),
    (r"puebla ac", "Puebla AC", 1900, 1930),
    (r"san pedro (golf club|gc)", "San Pedro Golf Club", 1900, 1930),
    (r"mexico country club", "Mexico Country Club", 1900, 1930),
    (r"mexico fc", "Mexico FC (1907)", 1907, 1909),
    (r"popo( fc| packing.*)?", "Popo FC", 1900, 1930),
    (r"(club )?mexico( fc)?", "Club México", 1910, 1940),
    (r"(rc |real club |club )?espana( fc)? b", "Real Club España B", 1910, 1930),
    (r"(rc |real club |real |club )?espana( fc)?", "Real Club España", 1910, 1960),
    (r"rovers( fc)?", "Rovers FC", 1900, 1930),
    (r"l ?amicale francaise", "L'Amicale Française", 1900, 1930),
    (r"junior( club)?", "Junior Club", 1900, 1930),
    (r"deportivo espanol", "Deportivo Español de México", 1900, 1930),
    (r"germania( fv)?", "Germania FV", 1900, 1940),
    (r"(c(entro)? union( america)?|centro union)", "América do México", 1910, 1925),
    (r"espana (de )?veracruz", "España de Veracruz", 1900, 1930),
    (r"tigres", "Tigres (1918)", 1900, 1930),
    (r"asturias", "Asturias", 1900, 1960),
    (r"deportivo internacional", "Deportivo Internacional", 1900, 1930),
    (r"morelos", "Morelos", 1900, 1930),
    (r"luz y fuerza", "Luz y Fuerza", 1900, 1930),
    (r"tranvias", "Tranvías", 1900, 1930),
    (r"guerra y marina", "Guerra y Marina", 1900, 1930),
    (r"son sin", "Son-Sin", 1900, 1930),
    (r"aurrera", "Aurrerá", 1900, 1930),
    (r"marte( fc)?", "Marte", 1920, 1960),
    (r"leones( op)?", "Leones", 1920, 1940),
    (r"sporting", "Sporting de México", 1920, 1940),
    (r"euzkadi", "Euzkadi", 1930, 1940),
    (r"seleccion jalisco", "Selección Jalisco", 1930, 1945),
    (r"moctezuma", "Moctezuma de Orizaba", 1930, 1960),
    # profissional
    (r"(club )?america|amerika", "América do México", 1900, 2100),
    (r"(club )?necaxa|nexaca|(a(tletico)?\.? ?)?espanol", "Necaxa", 1920, 2100),
    (r"atlante", "Atlante", 1920, 2100),
    (r"a ?d ?o|ado orizaba|orizabeno", "ADO Orizaba", 1940, 1960),
    (r"atlas", "Atlas", 1940, 2100),
    (r"(cd |chivas )?guadalajara|chivas", "Guadalajara", 1940, 2100),
    (r"veracruz|tiburones rojos( de veracruz)?", "Veracruz", 1940, 2100),
    (r"oro", "Oro", 1940, 1980),
    (r"(club )?leon", "León", 1940, 2100),
    (r"(club )?puebla", "Puebla", 1940, 2100),
    (r"(cf )?monterrey|rayados", "Monterrey", 1940, 2100),
    (r"tampico", "Tampico", 1940, 1981),
    (r"san sebastian", "San Sebastián de León", 1940, 1960),
    (r"zacatepec", "Zacatepec", 1950, 2100),
    (r"(deportivo )?toluca", "Toluca", 1950, 2100),
    (r"la piedad", "La Piedad", 1950, 2100),
    (r"irapuato", "Irapuato", 1950, 2100),
    (r"cuautla", "Cuautla", 1950, 2100),
    (r"zamora", "Zamora", 1950, 2100),
    (r"(atletico |monarcas |club atletico )?morelia", "Morelia", 1950, 2100),
    (r"celaya", "Celaya", 1950, 1980),
    (r"atletico celaya|celaya", "Atlético Celaya", 1990, 2100),
    (r"nacional", "Nacional de Guadalajara", 1950, 1980),
    (r"u ?n ?a ?m|pumas( unam)?|universidad nacional", "Pumas", 1950, 2100),
    (r"poza rica", "Poza Rica", 1950, 2100),
    (r"ciudad madero", "Ciudad Madero", 1950, 1980),
    (r"cruz azul", "Cruz Azul", 1950, 2100),
    (r"(jabatos )?(n ?l|nuevo leon)", "Jabatos de Nuevo León", 1960, 1975),
    (r"laguna", "Laguna de Torreón", 1960, 1980),
    (r"torreon", "Torreón", 1960, 1980),
    (r"jalisco", "Jalisco", 1960, 1990),
    (r"(tigres )?u ?a ?n ?l|u de n ?l|tigres( uanl)?", "Tigres", 1960, 2100),
    (r"u(nion)? ?de curtidores", "Unión de Curtidores", 1960, 2100),
    (r"san luis( potosi)?", "San Luis", 1960, 1995),
    (r"a(tl(etico)?)?\.? ?potosino", "Atlético Potosino", 1960, 2000),
    (r"u ?(de)? ?g(uadalajara)?|leones negros( udeg)?", "Leones Negros", 1960, 2100),
    (r"u ?a ?(de )?g|tecos( uag)?|estudiantes( uag| tecos)?", "Tecos", 1960, 2100),
    (r"a(tletas)?\.? ?campesinos", "Atletas Campesinos", 1970, 1990),
    (r"(deportivo )?neza", "Deportivo Neza", 1970, 1990),
    (r"oaxtepec( angeles)?", "Oaxtepec", 1980, 1983),
    (r"(oaxtepec )?angeles( de puebla)?|oaxtepec", "Ángeles", 1984, 1990),
    (r"(tm |t m )?(tampico ?madero|tampico mad|gallos blancos)", "Tampico Madero", 1980, 1999),
    (r"cobras( juarez| de ciudad juarez)?", "Cobras", 1980, 2000),
    (r"santos( laguna| lag)?", "Santos Laguna", 1980, 2100),
    (r"(correcaminos )?(u ?a ?t|u ?a ?ta+ma?u?li(p|o)a?s|u ?a ?tamaulioas)( correcaminos)?|correcaminos", "Correcaminos UAT", 1980, 2100),
    (r"queretaro( fc)?|gallos blancos|gallos b", "Querétaro", 1980, 2100),
    (r"to?os neza|toros (neza|hidalgo|neza hidalgo)", "Toros Neza", 1990, 2005),
    (r"colibries( de)?( morelos)?", "Colibríes de Morelos", 2000, 2010),
    (r"(jaguares|chiapas)( chiapas| de chiapas| fc)?", "Jaguares de Chiapas", 2000, 2100),
    (r"dorados( de)?( sinaloa)?", "Dorados", 2000, 2100),
    (r"(real )?san luis( fc)?", "San Luis FC", 2000, 2015),
    (r"indios( de ciudad juarez| juarez)?", "Indios", 2000, 2015),
    (r"(club )?tijuana|xolos( de tijuana)?", "Tijuana", 2000, 2100),
    (r"lobos( buap| b u a p)?", "Lobos BUAP", 2010, 2100),
    (r"(atl(etico)?|a) (de )?san luis", "Atlético de San Luis", 2015, 2100),
    (r"(fc )?juarez", "FC Juárez", 2015, 2100),
    (r"mazatlan( fc)?", "Mazatlán", 2020, 2100),
]

# o que nunca é clube: seleções do jogo anual Inglaterra x Escócia (era amadora) e times de exibição
_NAO_CLUBE = re.compile(r"^(england|scotland|mexican|foreign|mexico) xi$")
# lixo de colunas: hora e canal de TV (1983/84: "20:45   Televisa 4 (D) Necaxa"), estádio (1988/89: "Estadio Azteca América")
_LIXO = re.compile(r"^\s*[-/]\s*|\s*-\s*$|\[\[|\]\]|^(televisa|canal|imevision)\s*\d*\s*(\([A-Z]\))?\s*|^estadio azteca\s+", re.I)


def _regra(k: str, ano: int) -> str | None:
    if _NAO_CLUBE.match(k):
        return None
    for kk in (k, re.sub(r"^(club|c|cd|cf|fc|ca) ", "", k)):
        for rx, exib, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.fullmatch(f"(?:{rx})", kk):
                return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    nome = re.sub(r"\s+\d$", "", _LIXO.sub("", _LIXO.sub("", nome.strip())))   # "Monterrey 1": chamada de nota
    return _regra(chave(nome), ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
