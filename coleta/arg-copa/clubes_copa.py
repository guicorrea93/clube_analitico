"""Clubes da Copa Argentina (o ano das regras é o ano_inicio da edição: 2018/19 = 2018): os do arg-1 (coleta/arg-1/clubes_arg.py) mais os do Ascenso e do Federal que só jogam a copa.
As regras daqui vêm antes das do arg-1 e casam o nome inteiro (as do arg-1 casam o começo do nome e confundem "Boca Unidos"
com o Boca Juniors, "Gimnasia y Tiro" com o Gimnasia La Plata, "Talleres (R. de Escalada)" com o Talleres de Córdoba...).

Homônimos desfeitos pelas tabelas da própria RSSSF (sede ao lado do nome) e pela Wikipédia em espanhol de cada edição:
- "Club Atlético Gimnasia y Esgrima" sem cidade: o de Jujuy em 2012/13, 2014/15 e 2015/16; "CA Gimnasia y Esgrima" sem cidade,
  o de Mendoza (2016/17, 2018/19, 2023 e 2024); "Gimnasia y Esgrima Foot Ball Club" (2012/13) é o de Concepción del Uruguay;
- "CA San Martín" sem cidade: o General San Martín de Formosa em 2016/17 e o de Tucumán em 2022; "(UAQ)" é o de San Juan,
  "(SMC)" o de Tucumán; "Atlético Club San Martín" é o de Mendoza; "CSyD San Martín" (2024) o de Burzaco;
- "CA Sarmiento" sem cidade é o de Junín; "Sarmiento (La Banda)" e "(Resistencia)" são outros clubes;
- "Unión (Rawson)" (2012/13) é o Unión de Villa Krause (Rawson, San Juan);
- 1969: entre parênteses vem o local do jogo (tirado), menos em "CA Independiente (Trelew)" e "(Avellaneda)"; o All Boys
  é o de Santa Rosa (La Pampa) e o Sarmiento o de La Banda (tabela final da página); 1970: siglas de cidade ("Quilmes
  (MDQ)" é o de Mar del Plata, "All Boys (RSA)" o de Santa Rosa) e cidades da lista de participantes da página.
Cidades pelas tabelas da RSSSF, pelo nome do clube ou pela Wikipédia em espanhol; sem fonte, vazias.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "arg-1"))
import clubes_arg  # noqa: E402
from rsssf_sul import chave  # noqa: E402

SEM = ("", "")
BA = "Buenos Aires"
CABA = ("Buenos Aires", "Ciudad de Buenos Aires")
CLUBES_COPA: dict[str, tuple[str, str]] = {
    "Agropecuario": ("Carlos Casares", BA), "Alianza de Coronel Moldes": ("Coronel Moldes", "Córdoba"),
    "All Boys de Santa Rosa": ("Santa Rosa", "La Pampa"), "Almirante Brown": ("Isidro Casanova", BA),
    "Américo Tesorieri": ("La Rioja", "La Rioja"), "Américo Tesorieri de Catamarca": ("San Fernando del Valle de Catamarca", "Catamarca"),
    "Argentino de Merlo": ("Merlo", BA), "Argentino de Monte Maíz": ("Monte Maíz", "Córdoba"),
    "Argentinos del Norte": ("San Miguel de Tucumán", "Tucumán"), "Atenas de Río Cuarto": ("Río Cuarto", "Córdoba"),
    "Atenas de Santo Tomé": ("Santo Tomé", ""), "Atlas (Argentina)": ("General Rodríguez", BA),
    "Atlético Palmira": ("Palmira", "Mendoza"), "Atlético Paraná": ("Paraná", "Entre Ríos"),
    "Berazategui": ("Berazategui", BA), "Boca Unidos": ("Corrientes", "Corrientes"), "Brown de Adrogué": ("Adrogué", BA),
    "Camioneros": ("Esteban Echeverría", BA), "Cañuelas": ("Cañuelas", BA), "Central Ballester": ("José León Suárez", BA),
    "Central Norte Argentino": ("Resistencia", "Chaco"), "Ciudad de Bolívar": ("Bolívar", BA), "Claypole": ("Claypole", BA),
    "Colón Juniors": ("San Juan", "San Juan"), "Comunicaciones (Argentina)": CABA,
    "Defensores de Cambaceres": ("Ensenada", BA), "Defensores de Pronunciamiento": ("Pronunciamiento", "Entre Ríos"),
    "Defensores Unidos": ("Zárate", BA), "Deportivo Guaymallén": ("Guaymallén", "Mendoza"),
    "Deportivo Laferrere": ("Gregorio de Laferrere", BA), "Deportivo Madryn": ("Puerto Madryn", "Chubut"),
    "Deportivo Maipú": ("Maipú", "Mendoza"), "Deportivo Merlo": ("Merlo", BA),
    "Deportivo Rincón": ("Rincón de los Sauces", "Neuquén"), "Ferrocarril Midland": ("Libertad", BA),
    "Flandria": ("Jáuregui", BA), "General Lamadrid": CABA, "General San Martín de Formosa": ("Formosa", "Formosa"),
    "Germinal": ("Rawson", "Chubut"), "Gimnasia de Concepción del Uruguay": ("Concepción del Uruguay", "Entre Ríos"),
    "Guillermo Brown": ("Puerto Madryn", "Chubut"), "Güemes": ("Santiago del Estero", "Santiago del Estero"),
    "Independiente de Chivilcoy": ("Chivilcoy", BA), "Independiente de Neuquén": ("Neuquén", "Neuquén"),
    "Ituzaingó": ("Ituzaingó", BA), "Jorge Gibson Brown": ("Posadas", "Misiones"),
    "Justo José de Urquiza": ("Loma Hermosa", BA), "Juventud Unida de Gualeguaychú": ("Gualeguaychú", "Entre Ríos"),
    "Juventud Unida Universitario": ("San Luis", "San Luis"), "La Emilia": ("La Emilia", BA),
    "Leandro N. Alem": ("General Rodríguez", BA), "Liniers de Bahía Blanca": ("Bahía Blanca", BA), "Lipton": ("Corrientes", "Corrientes"),
    "Luján": ("Luján", BA), "Mitre de Santiago del Estero": ("Santiago del Estero", "Santiago del Estero"),
    "Pacífico de General Alvear": ("General Alvear", "Mendoza"), "Pacífico de Neuquén": ("Neuquén", "Neuquén"),
    "Policial de Catamarca": ("San Fernando del Valle de Catamarca", "Catamarca"), "Puerto Nuevo": ("Campana", BA),
    "Quilmes de Mar del Plata": ("Mar del Plata", BA), "Racing de Olavarría": ("Olavarría", BA), "Racing de Trelew": ("Trelew", "Chubut"),
    "Real Pilar": ("Pilar", BA), "Rosario Puerto Belgrano": ("Punta Alta", BA), "Sacachispas (Argentina)": CABA,
    "San Miguel (Argentina)": ("Los Polvorines", BA), "Sansinena": ("General Cerri", BA),
    "Sarmiento de La Banda": ("La Banda", "Santiago del Estero"), "Social y Deportivo General Roca": ("General Roca", "Río Negro"),
    "Social y Deportivo Liniers": ("San Justo", BA), "Social y Deportivo San Martín": ("Burzaco", BA),
    "Social y Recreativo Español": SEM, "Sol de América de Formosa": ("Formosa", "Formosa"), "Sol de Mayo de Viedma": ("Viedma", "Río Negro"),
    "Sporting de Punta Alta": ("Punta Alta", BA), "Sportivo AC de Las Parejas": ("Las Parejas", "Santa Fe"),
    "Sportivo Alfredo Guzmán": ("San Miguel de Tucumán", "Tucumán"), "Sportivo Belgrano de San Francisco": ("San Francisco", "Córdoba"),
    "Sportivo Bernardino Rivadavia": ("Venado Tuerto", "Santa Fe"), "Sportivo Estudiantes": ("San Luis", "San Luis"),
    "Sportivo Los Andes": ("Tudcum", "San Juan"), "Sportivo Peñarol": ("Chimbas", "San Juan"), "Talleres Juniors": ("Comodoro Rivadavia", "Chubut"),
    "Tristán Suárez": ("Tristán Suárez", BA), "UAI Urquiza": ("Villa Lynch", BA), "Unión Aconquija": ("Aconquija", "Catamarca"),
    "Unión de Sunchales": ("Sunchales", "Santa Fe"), "Unión de Villa Krause": ("Villa Krause", "San Juan"),
    "Unión Santiago": ("Santiago del Estero", "Santiago del Estero"), "Viale FC": ("Viale", "Entre Ríos"),
    "Victoriano Arenas": ("Valentín Alsina", BA), "Villa Cubas": ("San Fernando del Valle de Catamarca", "Catamarca"),
    "Villa Mitre": ("Bahía Blanca", BA), "Villa San Carlos": ("Berisso", BA), "Yupanqui": CABA,
}
_ALL_BOYS_SR = "All Boys de Santa Rosa"
# edições antigas: (regex sobre a chave do nome, nome de exibição), só naquele ano
ANTIGAS: dict[int, list[tuple[str, str]]] = {
    1969: [(r"asociacion club atletico all boys", _ALL_BOYS_SR), (r"club atletico sarmiento", "Sarmiento de La Banda"),
           (r"club atletico talleres juniors", "Talleres Juniors"), (r"club atletico americo tesorieri", "Américo Tesorieri"),
           (r"club deportivo americo tesorieri", "Américo Tesorieri de Catamarca"), (r"club atletico pacifico", "Pacífico de Neuquén"),
           (r"club atletico sporting", "Sporting de Punta Alta"), (r"club sportivo los andes", "Sportivo Los Andes"),
           (r"lipton football club", "Lipton")],
    1970: [(r"all boys rsa", _ALL_BOYS_SR), (r"atenas", "Atenas de Santo Tomé"), (r"colon juniors", "Colón Juniors"),
           (r"juventud unida", "Juventud Unida Universitario"), (r"mitre", "Mitre de Santiago del Estero"), (r"palmira", "Atlético Palmira"),
           (r"quilmes mdq", "Quilmes de Mar del Plata"), (r"quilmes qui", "Quilmes"), (r"argentinos del norte", "Argentinos del Norte"),
           (r"central norte argentino", "Central Norte Argentino"), (r"rosario puerto belgrano", "Rosario Puerto Belgrano")],
}
# (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano); casa o nome inteiro
REGRAS_COPA: list[tuple[str, str, int, int]] = [
    # homônimos e clubes que as regras do arg-1 confundem
    (r"(ca |club atletico )?boca unidos( corrientes)?", "Boca Unidos", 0, 9999),
    (r"(ca |club atletico )?huracan las heras", "Huracán Las Heras", 0, 9999),
    (r"ca independiente (chivilcoy|cvy)", "Independiente de Chivilcoy", 0, 9999),
    (r"ca independiente del neuquen", "Independiente de Neuquén", 0, 9999),
    (r"ca independiente trelew", "Independiente de Trelew", 0, 9999),
    (r"ca sarmiento la banda", "Sarmiento de La Banda", 0, 9999),
    (r"(ca )?sarmiento resistencia", "Sarmiento de Resistencia", 0, 9999),
    (r"(ca |club atletico )?union sunchales", "Unión de Sunchales", 0, 9999),
    (r"club atletico union santiago", "Unión Santiago", 0, 9999), (r"club union aconquija", "Unión Aconquija", 0, 9999),
    (r"union (rawson|villa krause)", "Unión de Villa Krause", 0, 9999),
    (r"ca talleres (r de escalada|rde|remedios escalada)", "Talleres de Remedios de Escalada", 0, 9999),
    (r"(c|cd|club de) gimnasia y tiro( ac)?", "Gimnasia y Tiro", 0, 9999),
    (r"ca gimnasia y esgrima (ss jujuy|ssj)", "Gimnasia de Jujuy", 0, 9999),
    (r"club atletico gimnasia y esgrima", "Gimnasia de Jujuy", 2012, 2015),
    (r"ca gimnasia y esgrima", "Gimnasia de Mendoza", 2016, 9999),
    (r"gimnasia (concepcion del uruguay|y esgrima foot ball club)", "Gimnasia de Concepción del Uruguay", 0, 9999),
    (r"ca central cordoba (ros|rosario)", "Central Córdoba de Rosario", 0, 9999),
    (r"ca central cordoba( santiago.*| sant estero| sde)?", "Central Córdoba de Santiago del Estero", 2016, 9999),
    (r"ca argentino de quilmes", "Argentino de Quilmes", 0, 9999),
    (r"club atletico san martin", "San Martín de San Juan", 2011, 9999),
    (r"ca san martin", "General San Martín de Formosa", 2016, 2016), (r"ca san martin", "San Martín de Tucumán", 2022, 2022),
    (r"ca san martin smc|club atletico san martin s civil", "San Martín de Tucumán", 0, 9999),
    (r"ca san martin uaq", "San Martín de San Juan", 0, 9999), (r"atletico club san martin", "San Martín de Mendoza", 0, 9999),
    (r"csyd san martin", "Social y Deportivo San Martín", 0, 9999),
    (r"(club sportivo|cs) general san martin", "General San Martín de Formosa", 0, 9999),
    (r"atletico estudiantes|(ca|club atletico) estudiantes", "Estudiantes de Buenos Aires", 0, 9999),
    (r"aa estudiantes", "Estudiantes de Río Cuarto", 0, 9999), (r"(club sportivo|cs) estudiantes", "Sportivo Estudiantes", 0, 9999),
    (r"atletico velez sarsfield", "Vélez Sarsfield", 0, 9999),
    # clubes do arg-1 em grafias que as regras dele não pegam
    (r"(ac social y deportivo|acsd|acsyd) sol de mayo( la pampa)?", "Sol de Mayo de Viedma", 0, 9999),
    (r"ac y deportiva altos hornos zapla( salta)?", "Altos Hornos Zapla", 0, 9999),
    (r"(ca |club atletico )?ac+as+uso", "Sportivo Acassuso", 0, 9999),
    (r"(ca |club atletico )?central norte( salta)?", "Central Norte", 0, 9999),
    (r"(ca |club atletico )?chaco for ever", "Chaco For Ever", 0, 9999),
    (r"(ca )?colegiales", "Colegiales", 0, 9999), (r"(ca |club atletico )?douglas haig", "Douglas Haig", 0, 9999),
    (r"(ca )?excursionistas", "Excursionistas", 0, 9999), (r"(ca )?kimberley", "Kimberley", 0, 9999),
    (r"(ca )?los andes", "Los Andes", 0, 9999), (r"(ca )?san telmo", "San Telmo", 0, 9999), (r"(ca )?alvarado", "Alvarado", 0, 9999),
    (r"(cas|cay social|cays) defensores de belgrano", "Defensores de Belgrano", 0, 9999),
    (r"(c y biblioteca|cb|deportivo)? ?ramon santamarina|(deportivo )?santamarina", "Ramón Santamarina", 0, 9999),
    (r"cd armenio", "Deportivo Armenio", 0, 9999), (r"cd moron", "Deportivo Morón", 0, 9999),
    (r"cd guarani antonio franco", "Guaraní Antonio Franco", 0, 9999), (r"centro juventud antoniana", "Juventud Antoniana", 0, 9999),
    (r"(c sportivo barracas barracas|club sportivo barracas|cs barracas)", "Sportivo Barracas", 0, 9999),
    (r"cs dock sud", "Sportivo Dock Sud", 0, 9999), (r"sportivo italiano", "Deportivo Italiano", 0, 9999),
    (r"cs deportivo y c espanol dlraac", "Deportivo Español", 0, 9999),
    # clubes que só jogam a copa
    (r"ad berazategui", "Berazategui", 0, 9999), (r"alianza coronel moldes", "Alianza de Coronel Moldes", 0, 9999),
    (r"(club )?almirante brown", "Almirante Brown", 0, 9999), (r"asyd justo j de urquiza", "Justo José de Urquiza", 0, 9999),
    (r"atenas", "Atenas de Río Cuarto", 2011, 9999),
    (r"(club )?atletico parana", "Atlético Paraná", 0, 9999), (r"atletico policial catamarca", "Policial de Catamarca", 0, 9999),
    (r"(ca |club atletico |atletico )?brown( adrogue)?", "Brown de Adrogué", 0, 9999),
    (r"(csa|csya) guillermo brown|guillermo brown( pm)?", "Guillermo Brown", 0, 9999), (r"jorge gibson brown", "Jorge Gibson Brown", 0, 9999),
    (r"c sportivo bernardino rivadavia", "Sportivo Bernardino Rivadavia", 0, 9999),
    (r"(ca )?argentino de merlo", "Argentino de Merlo", 0, 9999), (r"(ca|club atletico) atlas", "Atlas (Argentina)", 0, 9999),
    (r"ca claypole", "Claypole", 0, 9999), (r"(ca )?defensores unidos", "Defensores Unidos", 0, 9999),
    (r"(ca )?ferrocarril midland", "Ferrocarril Midland", 0, 9999), (r"(ca )?general lamadrid", "General Lamadrid", 0, 9999),
    (r"(ca|club atletico) guemes", "Güemes", 0, 9999), (r"ca ituzaingo", "Ituzaingó", 0, 9999),
    (r"ca mitre( santiago del estero)?", "Mitre de Santiago del Estero", 0, 9999), (r"ca puerto nuevo", "Puerto Nuevo", 0, 9999),
    (r"ca san miguel", "San Miguel (Argentina)", 0, 9999), (r"ca sansinena social y deportivo", "Sansinena", 0, 9999),
    (r"ca victoriano arenas", "Victoriano Arenas", 0, 9999), (r"(ca )?villa san carlos", "Villa San Carlos", 0, 9999),
    (r"canuelas fc", "Cañuelas", 0, 9999), (r"(casd|casyd) camioneros", "Camioneros", 0, 9999),
    (r"cd argentino", "Argentino de Monte Maíz", 0, 9999),
    (r"(cd|club deportivo) juventud unida", "Juventud Unida de Gualeguaychú", 0, 9999),
    (r"(club )?juventud unida universitario.*", "Juventud Unida Universitario", 0, 9999),
    (r"cd maipu", "Deportivo Maipú", 0, 9999), (r"cd rincon( rincon de los sauces)?", "Deportivo Rincón", 0, 9999),
    (r"cdm leandro n alem", "Leandro N. Alem", 0, 9999), (r"club agropecuario argentino", "Agropecuario", 0, 9999),
    (r"club atletico germinal", "Germinal", 0, 9999), (r"club atletico liniers", "Liniers de Bahía Blanca", 0, 9999),
    (r"csyd liniers", "Social y Deportivo Liniers", 0, 9999), (r"club ciudad de bolivar", "Ciudad de Bolívar", 0, 9999),
    (r"club comunicaciones", "Comunicaciones (Argentina)", 0, 9999),
    (r"(club )?defensores de cambaceres", "Defensores de Cambaceres", 0, 9999),
    (r"(club deportivo )?uai urquiza", "UAI Urquiza", 0, 9999), (r"club lujan", "Luján", 0, 9999),
    (r"(club social y deportivo|csyd) flandria", "Flandria", 0, 9999), (r"club social y deportivo la emilia", "La Emilia", 0, 9999),
    (r"(club social y deportivo|csd|csyd) madryn", "Deportivo Madryn", 0, 9999),
    (r"(club social y deportivo merlo ac|deportivo merlo)", "Deportivo Merlo", 0, 9999),
    (r"club sportivo alfredo guzman", "Sportivo Alfredo Guzmán", 0, 9999),
    (r"(club sportivo|cs|sportivo) belgrano( san francisco| sfco)?", "Sportivo Belgrano de San Francisco", 0, 9999),
    (r"(club )?tristan suarez", "Tristán Suárez", 0, 9999), (r"club villa mitre", "Villa Mitre", 0, 9999),
    (r"cs penarol", "Sportivo Peñarol", 0, 9999), (r"(cs y cultural deportivo|cscyd) laferrere", "Deportivo Laferrere", 0, 9999),
    (r"cs y social sol de america", "Sol de América de Formosa", 0, 9999),
    (r"csy dep def de pronunciamiento|defensores de pronunciamiento.*", "Defensores de Pronunciamiento", 0, 9999),
    (r"csyd central ballester", "Central Ballester", 0, 9999), (r"csyd general roca", "Social y Deportivo General Roca", 0, 9999),
    (r"csyd yupanqui", "Yupanqui", 0, 9999), (r"csyr espanol", "Social y Recreativo Español", 0, 9999),
    (r"deportivo guaymallen( mza)?", "Deportivo Guaymallén", 0, 9999),
    (r"(mercado central )?sacach[i]?s?pas( fc)?", "Sacachispas (Argentina)", 0, 9999),
    (r"racing (athletic club|olavarria)", "Racing de Olavarría", 0, 9999), (r"racing trelew", "Racing de Trelew", 0, 9999),
    (r"real pilar fc", "Real Pilar", 0, 9999), (r"sc pacifico de general alvear", "Pacífico de General Alvear", 0, 9999),
    (r"sportivo (ac|atletico club)", "Sportivo AC de Las Parejas", 0, 9999), (r"viale foot ball club", "Viale FC", 0, 9999),
    (r"villa cubas", "Villa Cubas", 0, 9999),
]
CLUBES = {**clubes_arg.CLUBES, **CLUBES_COPA}
assert all(e in CLUBES for _, e, _, _ in REGRAS_COPA), [e for _, e, _, _ in REGRAS_COPA if e not in CLUBES]
assert all(e in CLUBES for rs in ANTIGAS.values() for _, e in rs)


def clube(nome: str, ano: int) -> str | None:
    """Nome de exibição: as regras da edição antiga, as da copa (nome inteiro) e, sem elas, as do arg-1."""
    nome = nome.strip()
    if ano == 1969:   # "(Rawson)", "(Posadas, Misiones)": local do jogo colado no nome
        nome = re.sub(r"\s*\((?!Trelew\)|Avellaneda\))[^)]*\)$", "", nome)
    k = re.sub(r"\s+", " ", chave(nome)).strip()
    for rx, exib in ANTIGAS.get(ano, []):
        if re.fullmatch(rx, k):
            return exib
    for rx, exib, a0, a1 in REGRAS_COPA:
        if a0 <= ano <= a1 and re.fullmatch(rx, k):
            return exib
    return clubes_arg.clube(nome, ano)
