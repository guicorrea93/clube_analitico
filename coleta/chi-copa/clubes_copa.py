"""Clubes da Copa Chile: os do chi-1 (coleta/chi-1/clubes_chi.py) mais os das divisões de acesso, amadores e seleções de
cidade que só jogam a copa. As regras daqui vêm antes das do chi-1 e casam o nome inteiro (as do chi-1 casam o começo do
nome e juntavam o "Colo Colo Chico" de Aysén ao Colo Colo).

SIGLAS: as das páginas de 1990-1996 ("CC" Colo Colo, "U" Universidad de Chile...). "SR" (1991, um jogo) é erro de digitação
de "SER" (o jogo é do grupo da La Serena); "CBA" (1991) é o Cobreandino de Los Andes, "SOI" o Soinca Bata, "LOZ" o
Lozapenco, "COL" o Colchagua e "SC" o Unión Santa Cruz ("U. Santa Cruz" na tabela de 1994; o
Deportes Santa Cruz das edições de 2008 em diante fica à parte).

Identidades: "Lister Rossel" passou a se chamar Linares depois da copa de 1974 (nota da página) e é o Deportes Linares;
"Deportes Osorno" (1985, 1989) é o Provincial Osorno; o Thomas Bata (1959) é o Soinca Bata; o Iberia de Los Ángeles é o
Iberia; "AGC-Cabildo" mudou de nome para "AGC-Provincial" em 2009 (nota da página); "Lord Cochrane" sem cidade (2009) é o
de Concepción (o de Aysén caiu antes); o Municipal de Santiago de 1962 e o Municipal Santiago de 2018 ficam separados; o
San Fernando de 1958-1959 fica separado do Colchagua. Cidades pela tabela da RSSSF ou pelo nome entre parênteses; sem
fonte, vazias.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "chi-1"))
import clubes_chi  # noqa: E402
from rsssf_sul import chave  # noqa: E402

SEM = ("", "")
RM = clubes_chi.RM
VAL, BIO, OHI, MAU, COQ, ARA, LAG, RIO = "Valparaíso", "Biobío", "O'Higgins", "Maule", "Coquimbo", "Araucanía", "Los Lagos", "Los Ríos"
STG = ("Santiago", RM)
CLUBES_COPA: dict[str, tuple[str, str]] = {
    "Cobreandino": ("Los Andes", VAL), "Colchagua": ("San Fernando", OHI), "Lozapenco": ("Concepción", BIO),
    "Soinca Bata": ("Peñaflor", RM), "Deportes Santa Cruz": ("Santa Cruz", OHI),
    # 1958-1978
    "Alianza de Curicó": ("Curicó", MAU), "San Fernando (Chile)": ("San Fernando", OHI), "San Bernardo Central": ("San Bernardo", RM),
    "Universidad Técnica del Estado": STG, "Municipal de Santiago": STG, "Valparaíso Ferroviario": ("Valparaíso", VAL),
    "Luis Cruz Martínez": ("Curicó", MAU), "Regional Zona Central": SEM, "Independiente de Cauquenes": ("Cauquenes", MAU),
    "Malleco Unido": ("Angol", ARA), "San Antonio Unido": ("San Antonio", VAL),
    "Selección de Antofagasta": ("Antofagasta", "Antofagasta"), "Selección de Arica": ("Arica", "Arica y Parinacota"),
    "Selección de Calama": ("Calama", "Antofagasta"), "Selección de Cauquenes": ("Cauquenes", MAU),
    "Selección de Copiapó": ("Copiapó", "Atacama"), "Selección de Iquique": ("Iquique", "Tarapacá"),
    "Selección de Osorno": ("Osorno", LAG), "Selección de Ovalle": ("Ovalle", COQ), "Selección de Peñaflor": ("Peñaflor", RM),
    "Selección de Pitrufquén": ("Pitrufquén", ARA), "Selección de Temuco": ("Temuco", ARA),
    "Selección de Tocopilla": ("Tocopilla", "Antofagasta"), "Selección de Valdivia": ("Valdivia", RIO),
    "Selección de Schwager": ("Coronel", BIO),
    # 2008 em diante (Tercera División, amadores e seleções)
    "11 de Septiembre": SEM, "Academia Quilpué": ("Quilpué", VAL), "Academia Samuel Reyes": SEM, "AGC Provincial": ("Cabildo", VAL),
    "Alas Portuarias": ("", "Aysén"), "Arturo Prat de Punta Arenas": ("Punta Arenas", "Magallanes"),
    "Asotel": ("Antofagasta", "Antofagasta"), "Atlético Balmaceda": ("San Antonio", VAL), "Barcelona (Chile)": SEM,
    "Brujas de Salamanca": ("Salamanca", COQ), "Central Norte (Chile)": SEM, "CF Rapa Nui": ("Hanga Roa", VAL),
    "Chimbarongo FC": ("Chimbarongo", OHI), "Colo Colo Chico": ("", "Aysén"), "Comunal Cabrero": ("Cabrero", BIO),
    "Concón Nacional": ("Concón", VAL), "Constitución Unido": ("Constitución", MAU), "Dante": ("Nueva Imperial", ARA),
    "David Arellano": ("Coquimbo", COQ), "Defensor de Casablanca": ("Casablanca", VAL), "Deportes Cerro Navia": STG,
    "Deportes Colina": ("Colina", RM), "Deportes Quilicura": STG, "Deportes Quillón": ("Quillón", "Ñuble"),
    "Deportes Recoleta": STG, "Deportes Rengo": ("Rengo", OHI), "Deportes Tocopilla": ("Tocopilla", "Antofagasta"),
    "Deportes Vallenar": ("Vallenar", "Atacama"), "Deportivo Audax": ("Futrono", RIO), "Deportivo Halcones": ("", "Aysén"),
    "Deportivo Lintz": ("Puerto Montt", LAG), "Deportivo Ormazábal": SEM, "Deportivo Paniahue": ("Santa Cruz", OHI),
    "Deportivo Purranque": ("Purranque", LAG), "Deportivo Quesos Kumey": ("Río Negro", LAG), "El Lucero": SEM,
    "Enfoque": ("Rancagua", OHI), "Estrella del Mar": ("Lota", BIO), "Favorita": ("Lontué", MAU),
    "General Velásquez": ("Puchuncaví", VAL), "Imperial Unido": ("Nueva Imperial", ARA), "José Miguel Carrera": ("Purranque", LAG),
    "Juan Lyon": ("Pichidegua", OHI), "Jugendland": ("Peñaflor", RM), "Juvenil Seminario": SEM,
    "Juventud Hospital": ("Chañaral", "Atacama"), "Juventud Padre Hurtado": ("Padre Hurtado", RM),
    "Juventud Puente Alto": ("Puente Alto", RM), "Juventud Varsovia": STG, "Juventus de Caldera": ("Caldera", "Atacama"),
    "Lautaro de Buin": ("Buin", RM), "Lord Cochrane de Aysén": ("Puerto Aysén", "Aysén"), "Lord Cochrane de Concepción": ("Concepción", BIO),
    "Luchador de Coñaripe": ("Coñaripe", RIO), "Luis Matte Larraín": ("Puente Alto", RM), "Manuel Rodríguez": ("Puente Alto", RM),
    "Marcos Trincado": SEM, "Miramar Sidempart": SEM, "Municipal Hijuelas": ("Hijuelas", VAL), "Municipal La Pintana": STG,
    "Municipal Mejillones": ("Mejillones", "Antofagasta"), "Municipal Pozo Almonte": ("Pozo Almonte", "Tarapacá"),
    "Municipal Puente Alto": ("Puente Alto", RM), "Municipal Santiago": STG, "Norte Unido": SEM, "Ñuñoa": STG,
    "Oscar Bonilla": ("Linares", MAU), "Peñalolén": STG, "Pilmahue": SEM, "Presidente Ibáñez": SEM,
    "Provincial Ovalle": ("Ovalle", COQ), "Provincial Talagante": ("Talagante", RM), "Pudahuel Barrancas": STG, "Real León": STG,
    "Real San Joaquín": STG, "Rodelindo Román": SEM, "San Antonio Unido (Temuco)": ("Temuco", ARA), "Santiago City": STG,
    "Selección de Coyhaique": ("Coyhaique", "Aysén"), "Selección de Juan Fernández": ("Juan Fernández", VAL),
    "Selección de Puerto Aysén": ("Puerto Aysén", "Aysén"), "Selección de Punta Arenas": ("Punta Arenas", "Magallanes"),
    "Selección de San Pedro de Atacama": ("San Pedro de Atacama", "Antofagasta"), "Selección de Vallenar": ("Vallenar", "Atacama"),
    "Tomás Greig": SEM, "Trasandino de Socoroma": ("Arica", "Arica y Parinacota"), "Universidad Iberoamericana": STG,
    "Unión Bellavista": SEM, "Unión Compañías": ("La Serena", COQ), "Unión Glorias Navales": ("Viña del Mar", VAL),
    "Unión Quilpué": ("Quilpué", VAL), "Unión Santa María": ("Los Ángeles", BIO), "Unión Temuco": ("Temuco", ARA),
    "Unión Wanderers": ("Valdivia", RIO), "Vicente Pérez Rosales": SEM, "Yungay de Iquique": ("Iquique", "Tarapacá"),
    # 2022 e 2023 (fases iniciais pela Wikipédia em espanhol, pendência D5)
    "Quintero Unido": ("Quintero", VAL), "San Bernardo Unido": ("San Bernardo", RM), "La Higuera": SEM, "Aguará": STG,
    "Tricolor Municipal": ("Paine", RM), "Cóndor (Chile)": ("", OHI), "La Obra": SEM, "Colo-Colito": SEM,
    "Provincial Ranco": ("La Unión", RIO), "Constitución FC": ("Constitución", MAU), "Ferroviario Comercial": SEM,
    "Teniente Merino": SEM, "Gol y Gol": SEM, "Liga Universitaria": ("", "Aysén"), "Bories": ("Punta Arenas", "Magallanes"),
    "CD Unión (Chile)": ("", "Tarapacá"), "Ojanco": ("", "Atacama"), "Eléctrico Refinería": ("", "Antofagasta"),
    "Los Nogales": SEM, "Juventud Unida (Chile)": SEM, "Rancagua Sur": ("Rancagua", OHI),
}
SIGLAS = {
    "AI": "Audax Italiano", "ANT": "Deportes Antofagasta", "AR": "San Marcos de Arica", "ATA": "Regional Atacama", "CB": "Cobreloa",
    "CBA": "Cobreandino", "CC": "Colo Colo", "COL": "Colchagua", "CON": "Deportes Concepción", "CS": "Cobresal", "CU": "Coquimbo Unido",
    "EV": "Everton de Viña del Mar", "FV": "Fernández Vial", "HUA": "Huachipato", "IB": "Iberia", "IQ": "Deportes Iquique",
    "LIN": "Deportes Linares", "LOZ": "Lozapenco", "LS": "Lota Schwager", "MAG": "Magallanes", "MEL": "Deportes Melipilla",
    "NAV": "Naval de Talcahuano", "OH": "O'Higgins", "OS": "Provincial Osorno", "OV": "Deportes Ovalle", "PAL": "Palestino",
    "PM": "Deportes Puerto Montt", "RAN": "Rangers de Talca", "SC": "Unión Santa Cruz", "SER": "Deportes La Serena",
    "SR": "Deportes La Serena", "SF": "Unión San Felipe", "SOI": "Soinca Bata", "SW": "Santiago Wanderers", "TEM": "Deportes Temuco",
    "U": "Universidad de Chile", "UC": "Universidad Católica", "UE": "Unión Española", "ULC": "Unión La Calera", "ÑUB": "Ñublense",
}
_T = 9999
# (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano); casa o nome inteiro
REGRAS_COPA: list[tuple[str, str, int, int]] = [
    # nomes da ESPN (D5b, datas e estádios): o AC Colina é o "Colina" da RSSSF de 2019 em diante
    (r"ac colina", "Deportes Colina", 0, _T), (r"central norte antofagasta", "Central Norte (Chile)", 0, _T),
    (r"chimbarongo", "Chimbarongo FC", 0, _T), (r"club 11 de septiembre", "11 de Septiembre", 0, _T),
    (r"deportivo el lucero", "El Lucero", 0, _T), (r"electricos refinerias", "Eléctrico Refinería", 0, _T),
    (r"glorias navales", "Unión Glorias Navales", 0, _T), (r"juan fernandez islands", "Selección de Juan Fernández", 0, _T),
    (r"poblacion los nogales", "Los Nogales", 0, _T), (r"rengo", "Deportes Rengo", 0, _T),
    (r"san antonio unido \(?sa\)?", "San Antonio Unido", 0, _T),
    # grafias de clubes do chi-1 que as regras dele não pegam (ou pegam errado)
    (r"colo colo chico", "Colo Colo Chico", 0, _T), (r"audax italoiano", "Audax Italiano", 0, _T),
    (r"univeridad catolica", "Universidad Católica", 0, _T), (r"unido san felipe", "Unión San Felipe", 0, _T),
    (r"union de calera", "Unión La Calera", 0, _T), (r"bernechea", "Deportes Barnechea", 0, _T),
    (r"deportes limachew", "Deportes Limache", 0, _T), (r"deportes milipilla", "Deportes Melipilla", 0, _T),
    (r"naval( talcahuano)?", "Naval de Talcahuano", 0, _T), (r"f vial( concepcion)?", "Fernández Vial", 0, _T),
    (r"(dep|deportes) ovalle( s ?a)?", "Deportes Ovalle", 0, _T), (r"(dep|deportes) puerto montt", "Deportes Puerto Montt", 0, _T),
    (r"(dep|deportes) copiapo( s ?a)?", "Deportes Copiapó", 0, _T), (r"(dep|deportes) valdivia", "Deportes Valdivia", 0, _T),
    (r"(s ?m|sab marcos) de arica", "San Marcos de Arica", 0, _T), (r"deportes osorno", "Provincial Osorno", 0, _T),
    (r"lister rossel", "Deportes Linares", 0, _T), (r"iberia( los angeles)?", "Iberia", 0, _T),
    (r"colchagua( cd)?( san fernando)?", "Colchagua", 0, _T), (r"(dep|deportes) santa cruz", "Deportes Santa Cruz", 0, _T),
    (r"thomas bata|soinca", "Soinca Bata", 0, _T), (r"(deportes|d) colchagua", "Colchagua", 0, _T),
    (r"iberia bio bio", "Iberia", 0, _T), (r"a ?f vial", "Fernández Vial", 0, _T), (r"d arica", "San Marcos de Arica", 0, _T),
    (r"d concepcion", "Deportes Concepción", 0, _T), (r"d iquique", "Deportes Iquique", 0, _T),
    (r"d la serena", "Deportes La Serena", 0, _T), (r"d melipilla", "Deportes Melipilla", 0, _T),
    (r"d ovalle", "Deportes Ovalle", 0, _T), (r"d temuco", "Deportes Temuco", 0, _T), (r"p osorno", "Provincial Osorno", 0, _T),
    (r"r atacama", "Regional Atacama", 0, _T), (r"(u )?santa cruz", "Unión Santa Cruz", 1980, 1999),
    # 1958-1978
    (r"alianza", "Alianza de Curicó", 0, 1990), (r"san fernando", "San Fernando (Chile)", 0, 1990),
    (r"san bernardo central", "San Bernardo Central", 0, _T), (r"universidad tecnica( del estado)?", "Universidad Técnica del Estado", 0, _T),
    (r"municipal( best loser)?", "Municipal de Santiago", 0, 1990), (r"valparaiso ferroviario", "Valparaíso Ferroviario", 0, _T),
    (r"luis cruz martinez", "Luis Cruz Martínez", 0, _T), (r"regional zona central", "Regional Zona Central", 0, _T),
    (r"independiente( de cauquenes)?", "Independiente de Cauquenes", 0, _T), (r"malleco unido", "Malleco Unido", 0, _T),
    (r"san antonio (de )?unido", "San Antonio Unido", 0, _T),
    (r"antofagasta sel", "Selección de Antofagasta", 0, _T), (r"arica sel", "Selección de Arica", 0, _T),
    (r"calama sel", "Selección de Calama", 0, _T), (r"cauquenes sel", "Selección de Cauquenes", 0, _T),
    (r"copiapo sel", "Selección de Copiapó", 0, _T), (r"iquique sel", "Selección de Iquique", 0, _T),
    (r"osorno sel", "Selección de Osorno", 0, _T), (r"ovalle sel", "Selección de Ovalle", 0, _T),
    (r"penaflor sel", "Selección de Peñaflor", 0, _T), (r"pitrufquen sel", "Selección de Pitrufquén", 0, _T),
    (r"temuco sel", "Selección de Temuco", 0, _T), (r"tocopilla sel", "Selección de Tocopilla", 0, _T),
    (r"valdivia sel", "Selección de Valdivia", 0, _T), (r"schwager sel", "Selección de Schwager", 0, _T),
    # 2008 em diante
    (r"acad quilpue", "Academia Quilpué", 0, _T), (r"acad samuel reyes", "Academia Samuel Reyes", 0, _T),
    (r"agc ?(cabildo|provincial)", "AGC Provincial", 0, _T), (r"alas portuarias", "Alas Portuarias", 0, _T),
    (r"arturo prat( punta arenas)?", "Arturo Prat de Punta Arenas", 0, _T), (r"asotel( antofagasta)?", "Asotel", 0, _T),
    (r"(atletico )?balmaceda( san antonio)?", "Atlético Balmaceda", 0, _T), (r"barcelona", "Barcelona (Chile)", 0, _T),
    (r"brujas de salamanca", "Brujas de Salamanca", 0, _T), (r"central norte", "Central Norte (Chile)", 0, _T),
    (r"cf rapa nui", "CF Rapa Nui", 0, _T), (r"chimbarongo fc", "Chimbarongo FC", 0, _T),
    (r"comunal cabrero", "Comunal Cabrero", 0, _T), (r"concon nacional", "Concón Nacional", 0, _T),
    (r"constitucion unido", "Constitución Unido", 0, _T), (r"dante( nueva imperial)?", "Dante", 0, _T),
    (r"david arellano( coquimbo)?", "David Arellano", 0, _T), (r"defensor( casablanca)?", "Defensor de Casablanca", 0, _T),
    (r"(dep |deportes )?cerro navia( santiago)?", "Deportes Cerro Navia", 0, _T), (r"(deportes )?colina", "Deportes Colina", 0, _T),
    (r"(dep|deportes) quilicura( santiago)?", "Deportes Quilicura", 0, _T), (r"deportes quillon", "Deportes Quillón", 0, _T),
    (r"deportes recoleta", "Deportes Recoleta", 0, _T), (r"(dep|deportes) rengo", "Deportes Rengo", 0, _T),
    (r"(dep|deportes) tocopilla", "Deportes Tocopilla", 0, _T), (r"deportes vallenar", "Deportes Vallenar", 0, _T),
    (r"deportivo audax( futrono)?", "Deportivo Audax", 0, _T), (r"(deportivo )?halcones", "Deportivo Halcones", 0, _T),
    (r"deportivo lintz( puerto montt)?", "Deportivo Lintz", 0, _T), (r"dvo ormazabal", "Deportivo Ormazábal", 0, _T),
    (r"(deportivo )?paniahue( santa cruz)?", "Deportivo Paniahue", 0, _T), (r"dvo purranque", "Deportivo Purranque", 0, _T),
    (r"deportivo quesos kumey( rio negro)?", "Deportivo Quesos Kumey", 0, _T), (r"el lucero", "El Lucero", 0, _T),
    (r"(cd )?enfoque( rancagua)?", "Enfoque", 0, _T), (r"estrella del mar( lota)?", "Estrella del Mar", 0, _T),
    (r"favorita( lontue)?", "Favorita", 0, _T), (r"(general|gral) velasquez( puchuncavi)?", "General Velásquez", 0, _T),
    (r"imperial unido", "Imperial Unido", 0, _T), (r"jose miguel carrera( purranque)?", "José Miguel Carrera", 0, _T),
    (r"juan lyon( pichidegua)?", "Juan Lyon", 0, _T), (r"jugendland( penaflor)?", "Jugendland", 0, _T),
    (r"juvenil seminario", "Juvenil Seminario", 0, _T), (r"juventud hospital( chanaral)?", "Juventud Hospital", 0, _T),
    (r"juv padre hurtado", "Juventud Padre Hurtado", 0, _T), (r"juv puente alto", "Juventud Puente Alto", 0, _T),
    (r"juventud varsovia( santiago)?", "Juventud Varsovia", 0, _T), (r"juventus( caldera)?", "Juventus de Caldera", 0, _T),
    (r"lautaro( de)?( buin)?", "Lautaro de Buin", 2008, _T),
    (r"lord cochrane (aysen|puerto aysen)", "Lord Cochrane de Aysén", 0, _T),
    (r"lord cochrane( concepcion)?( 1st leg in molina| 2nd leg in tome)?", "Lord Cochrane de Concepción", 0, _T),
    (r"(el )?luchador( conaripe)?", "Luchador de Coñaripe", 0, _T), (r"luis matte larrain", "Luis Matte Larraín", 0, _T),
    (r"manuel rodriguez( puente alto)?", "Manuel Rodríguez", 0, _T), (r"marcos trincado", "Marcos Trincado", 0, _T),
    (r"miramar sidempart", "Miramar Sidempart", 0, _T), (r"(mun|municipal) hijuelas", "Municipal Hijuelas", 0, _T),
    (r"(mun|municipal) la pintana( santiago)?", "Municipal La Pintana", 0, _T),
    (r"(mun|municipal) mejillones", "Municipal Mejillones", 0, _T), (r"municipal pozo almonte", "Municipal Pozo Almonte", 0, _T),
    (r"municipal puente alto", "Municipal Puente Alto", 0, _T), (r"municipal santiago", "Municipal Santiago", 2000, _T),
    (r"norte unido", "Norte Unido", 0, _T), (r"nunoa", "Ñuñoa", 0, _T), (r"oscar bonilla( linares)?", "Oscar Bonilla", 0, _T),
    (r"penalolen( santiago)?", "Peñalolén", 0, _T), (r"pilmahue", "Pilmahue", 0, _T), (r"presidente ibanez", "Presidente Ibáñez", 0, _T),
    (r"provincial ovalle", "Provincial Ovalle", 0, _T), (r"(prov|provincial) talagante", "Provincial Talagante", 0, _T),
    (r"pudahuel barrancas( santiago)?", "Pudahuel Barrancas", 0, _T), (r"real leon", "Real León", 0, _T),
    (r"real san joaquin", "Real San Joaquín", 0, _T), (r"rodelindo roman", "Rodelindo Román", 0, _T),
    (r"san antonio unido temuco", "San Antonio Unido (Temuco)", 0, _T), (r"santiago city", "Santiago City", 0, _T),
    (r"seleccion de coyhaique", "Selección de Coyhaique", 0, _T), (r"seleccion de juan fernandez", "Selección de Juan Fernández", 0, _T),
    (r"seleccion de puerto aysen", "Selección de Puerto Aysén", 0, _T), (r"seleccion de punta arenas", "Selección de Punta Arenas", 0, _T),
    (r"seleccion de san pedro (de )?atacama", "Selección de San Pedro de Atacama", 0, _T),
    (r"seleccion de vallenar", "Selección de Vallenar", 0, _T), (r"tomas greig", "Tomás Greig", 0, _T),
    (r"trasandino de socoroma( arica)?", "Trasandino de Socoroma", 0, _T),
    (r"(u|univ) iberoamericana", "Universidad Iberoamericana", 0, _T), (r"union bellavista", "Unión Bellavista", 0, _T),
    (r"union companias", "Unión Compañías", 0, _T), (r"union glorias navales", "Unión Glorias Navales", 0, _T),
    (r"union quilpue", "Unión Quilpué", 0, _T), (r"(u|union) santa maria( los angeles)?", "Unión Santa María", 0, _T),
    (r"union temuco", "Unión Temuco", 0, _T), (r"union wanderers( general lagos)?( valdivia)?", "Unión Wanderers", 0, _T),
    (r"vicente perez r", "Vicente Pérez Rosales", 0, _T), (r"yungay( iquique)?", "Yungay de Iquique", 0, _T),
    (r"11 de septiembre", "11 de Septiembre", 0, _T),
    # 2022 e 2023
    (r"quintero unido", "Quintero Unido", 0, _T), (r"san bernardo unido", "San Bernardo Unido", 0, _T),
    (r"la higuera", "La Higuera", 0, _T), (r"aguara", "Aguará", 0, _T), (r"tricolor municipal", "Tricolor Municipal", 0, _T),
    (r"condor", "Cóndor (Chile)", 2000, _T), (r"la obra", "La Obra", 0, _T), (r"colo ?colito", "Colo-Colito", 0, _T),
    (r"provincial ranco", "Provincial Ranco", 0, _T), (r"constitucion fc", "Constitución FC", 0, _T),
    (r"ferroviario comercial", "Ferroviario Comercial", 0, _T), (r"teniente merino", "Teniente Merino", 0, _T),
    (r"gol y gol", "Gol y Gol", 0, _T), (r"liga universitaria", "Liga Universitaria", 0, _T), (r"bories", "Bories", 0, _T),
    (r"concon national", "Concón Nacional", 0, _T), (r"cd union", "CD Unión (Chile)", 2000, _T), (r"ojanco", "Ojanco", 0, _T),
    (r"electrico refineria", "Eléctrico Refinería", 0, _T), (r"los nogales", "Los Nogales", 0, _T),
    (r"juventud unida", "Juventud Unida (Chile)", 2000, _T),
    (r"rancagua sur", "Rancagua Sur", 0, _T),
]
CLUBES = {**clubes_chi.CLUBES, **CLUBES_COPA}
assert all(e in CLUBES for _, e, _, _ in REGRAS_COPA), [e for _, e, _, _ in REGRAS_COPA if e not in CLUBES]
assert all(e in CLUBES for e in SIGLAS.values()), [e for e in SIGLAS.values() if e not in CLUBES]
_EXIB = {chave(c): c for c in CLUBES}


def clube(nome: str, ano: int) -> str | None:
    """Nome de exibição: o próprio nome de exibição (as siglas já trocadas), as regras da copa e, sem elas, as do chi-1."""
    nome = re.sub(r"\s*\*$", "", nome.strip())   # "P. Osorno *" (classificado, tabela de 1994)
    k = re.sub(r"\s+", " ", chave(nome)).strip()
    if k in _EXIB:
        return _EXIB[k]
    for rx, exib, a0, a1 in REGRAS_COPA:
        if a0 <= ano <= a1 and re.fullmatch(rx, k):
            return exib
    return clubes_chi.clube(nome, ano)
