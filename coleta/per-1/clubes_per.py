"""Identidade dos clubes peruanos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido no Brasil ("Universitario", "Alianza Lima", "Sporting Cristal", "Melgar", "César
  Vallejo", "Binacional");
- homônimo de clube do banco ou de outro pacote leva a cidade: "Libertad de Trujillo" (o Libertad é o paraguaio),
  "Internazionale de San Borja";
- o mesmo clube com outro nome em outra época fica com o nome atual: Federación Universitaria (até 1930) é o Universitario;
  Sport Alianza (até 1927) é o Alianza Lima; Sucre FBC é o Mariscal Sucre; Inti Gas Deportes (2009-2014) é o Ayacucho;
  Total Clean (Arequipa, 2007-2009) é o Total Chalaco; Real Garcilaso (até 2019) é o Cusco FC; Colegio San Agustín é o Deportivo San Agustín;
- clubes diferentes com o mesmo nome: Alfonso Ugarte de Chiclín (1966-1967) e Alfonso Ugarte (Puno); Sport José Gálvez
  (Lima, 1926) e José Gálvez (Chimbote); Sportivo Melgar (Lima, 1937) e Melgar (Arequipa); Atlético Barrio Frigorífico
  (Callao, 1974) e Alianza Frigorífico (Callao, 1928-1931; a RSSSF o chama de Alianza Callao em 1928, e a Wikipédia liga
  esse nome ao Alianza Frigorífico Nacional);
- Estudiantes de Medicina (Ica) jogou 2004 em Piura como "Grau-Estudiantes" (fusão com o Atlético Grau, desfeita no fim do
  ano): fica Estudiantes de Medicina.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-sulamerica"))
from rsssf_sul import chave  # noqa: E402

LIM = ("Lima", "Lima")
CAL = ("Callao", "Callao")

# nome de exibição -> (cidade, departamento)
CLUBES: dict[str, tuple[str, str]] = {
    "Escuela Militar de Chorrillos": LIM, "Miraflores Sporting": LIM, "Sport Vitarte": LIM, "Atlético Grau No. 1": LIM, "Unión Miraflores": LIM, "Sporting Fry": LIM, "Sport Tacna No. 1": LIM, "Unión Perú": LIM, "Fraternal Barranco": LIM, "Escuela de Artes y Oficios": LIM, "Sportivo Lima": LIM, "Sport Huascar": LIM, "Sport Calavera": LIM, "Unión Barranco": LIM,
    # Lima e Callao
    "Universitario": LIM, "Alianza Lima": LIM, "Sporting Cristal": LIM, "Sport Boys": CAL, "Deportivo Municipal": LIM,
    "Atlético Chalaco": CAL, "Universidad San Martín": LIM, "Defensor Lima": LIM, "Mariscal Sucre": LIM, "Centro Iqueño": LIM,
    "Sporting Tabaco": LIM,   # PE-021: de Lima
    "Total Chalaco": CAL, "Guardia Republicana": LIM, "Deportivo San Agustín": LIM,
    "Internazionale de San Borja": LIM, "AELU": LIM, "Lawn Tennis": LIM, "Circolo Sportivo Italiano": LIM,
    "Sportivo Tarapacá Ferrocarril": LIM, "Unión Buenos Aires": CAL, "Sport Progreso": LIM, "Teniente Ruiz": LIM,
    "Jorge Washington": CAL, "Deportivo Nacional": LIM, "Sport José Gálvez": LIM, "Asociación Alianza": LIM,
    "Association FBC": LIM, "Ciclista Lima": LIM, "Hidroaviación": LIM, "Alianza Chorrillos": LIM, "Santa Catalina": LIM,
    "Alberto Secada": LIM, "Jorge Chávez": CAL, "José Olaya": LIM, "Unión FC": LIM,
    "Alianza Frigorífico": CAL, "Telmo Carbajo": CAL, "Progresista Apurímac": CAL, "Atlético Córdoba": LIM,
    "Santiago Barranco": LIM, "Unión Carbone": LIM, "Sportivo Melgar": LIM, "Carlos Concha": CAL, "Unión Callao": CAL,
    "Asociación Chorrillos": LIM, "Mariscal Castilla": LIM, "Porvenir Miraflores": LIM, "KDT Nacional": CAL,
    "Unión América": LIM, "Defensor Arica": LIM, "Deportivo SIMA": CAL, "Atlético Olímpico": CAL,
    "Atlético Barrio Frigorífico": CAL, "Unión Gonzales Prada": LIM, "Academia Cantolao": CAL, "Pacífico FC": LIM,
    "Sportivo Unión": LIM, "Lawn Tennis de la Exposición": LIM, "Deportivo Hospital": LIM, "Meteor Sport Club": LIM,
    "Sport Pacífico": LIM, "Juventud La Palma": ("Huacho", "Lima"), "Juventud La Joya": ("Chancay", "Lima"),
    "Unión Huaral": ("Huaral", "Lima"), "Walter Ormeño": ("Cañete", "Lima"), "América Cochahuayco": LIM,
    "Atlético Minero": ("Matucana", "Lima"), "Deportivo Wanka": ("Huancayo", "Junín"),
    # resto do país
    "Melgar": ("Arequipa", "Arequipa"), "Cienciano": ("Cusco", "Cusco"), "Juan Aurich": ("Chiclayo", "Lambayeque"),
    "César Vallejo": ("Trujillo", "La Libertad"), "Sport Huancayo": ("Huancayo", "Junín"), "UTC": ("Cajamarca", "Cajamarca"),
    "Alianza Atlético": ("Sullana", "Piura"), "Coronel Bolognesi": ("Tacna", "Tacna"), "León de Huánuco": ("Huánuco", "Huánuco"),
    "Ayacucho": ("Ayacucho", "Ayacucho"), "Binacional": ("Juliaca", "Puno"), "Cusco FC": ("Cusco", "Cusco"), "Deportivo Garcilaso": ("Cusco", "Cusco"), "Los Chankas": ("Andahuaylas", "Apurímac"),
    "ADT": ("Tarma", "Junín"), "Carlos Mannucci": ("Trujillo", "La Libertad"), "Atlético Grau": ("Piura", "Piura"),
    "CNI": ("Iquitos", "Loreto"), "Sport Áncash": ("Huaraz", "Áncash"), "José Gálvez": ("Chimbote", "Áncash"),
    "Unión Comercio": ("Moyobamba", "San Martín"), "Unión Minas": ("Cerro de Pasco", "Pasco"),
    "Deportivo Pesquero": ("Chimbote", "Áncash"), "Deportivo Sipesa": ("Chimbote", "Áncash"),
    "Aurich-Cañaña": ("Chiclayo", "Lambayeque"), "Deportivo Cañaña": ("Lambayeque", "Lambayeque"),
    "Hungaritos Agustinos": ("Iquitos", "Loreto"), "Libertad de Trujillo": ("Trujillo", "La Libertad"),
    "Diablos Rojos": ("Juliaca", "Puno"), "Alfonso Ugarte": ("Puno", "Puno"), "Alfonso Ugarte de Chiclín": ("Chiclín", "La Libertad"),
    "Atlético Torino": ("Talara", "Piura"), "Defensor ANDA": ("Aucayacu", "Huánuco"), "Atlético Huracán": ("Moquegua", "Moquegua"),
    "Mina San Vicente": ("San Ramón", "Junín"), "Deportivo Junín": ("Huancayo", "Junín"), "Huancayo FC": ("Huancayo", "Junín"),
    "Sport Pilsen": ("Guadalupe", "La Libertad"), "Los Espartanos": ("Pacasmayo", "La Libertad"),
    "Chanchamayo FC": ("La Merced", "Junín"), "Deportivo Pucallpa": ("Pucallpa", "Ucayali"),
    "Deportivo COOPTRIP": ("Pucallpa", "Ucayali"), "Alianza Naval": ("Mollendo", "Arequipa"),
    "Alipio Ponce": ("Mazamari", "Junín"), "Deportivo Tintaya": ("Yauri", "Cusco"), "Juvenil Los Ángeles": ("Moquegua", "Moquegua"),
    "FBC Aurora": ("Arequipa", "Arequipa"), "Hijos de Yurimaguas": ("Yurimaguas", "Loreto"),
    "Deportivo Yurimaguas": ("Yurimaguas", "Loreto"), "Unión Tarapoto": ("Tarapoto", "San Martín"),
    "Alianza Huánuco": ("Huánuco", "Huánuco"), "Mariscal Nieto": ("Ilo", "Moquegua"), "15 de Setiembre": ("Trujillo", "La Libertad"),
    "Estudiantes de Medicina": ("Ica", "Ica"), "Coopsol": ("Trujillo", "La Libertad"),
    "Deportivo UPAO": ("Trujillo", "La Libertad"), "Octavio Espinosa": ("Ica", "Ica"), "Unión Tumán": ("Tumán", "Lambayeque"),
    "Piérola": ("Arequipa", "Arequipa"), "Unión Pesquero": ("Ilo", "Moquegua"), "Sportivo Huracán": ("Arequipa", "Arequipa"),
    "Comerciantes Unidos": ("Cutervo", "Cajamarca"), "Deportivo Llacuabamba": ("Pataz", "La Libertad"),
    "Pirata FC": ("Chiclayo", "Lambayeque"), "Carlos Stein": ("Lambayeque", "Lambayeque"),
    "Juan Pablo II": ("Chongoyape", "Lambayeque"), "Alianza Universidad": ("Huánuco", "Huánuco"),
    "Sport Rosario": ("Huaraz", "Áncash"), "Defensor La Bocana": ("Sechura", "Piura"), "Sport Loreto": ("Pucallpa", "Ucayali"),
    "San Simón": ("Moquegua", "Moquegua"), "Los Caimanes": ("Puerto Eten", "Lambayeque"), "Cobresol": ("Moquegua", "Moquegua"),
    "Atlético Universidad": ("Arequipa", "Arequipa"), "Unión Huayllaspanca": ("Cusco", "Cusco"),
    "Deportivo Los Ángeles": ("Moquegua", "Moquegua"), "La Loretana": ("Iquitos", "Loreto"), "Alcides Vigo": LIM,
    "IMI": ("Talara", "Piura"), "Deportivo Bancos": ("", ""), "Lima Cricket": LIM, "Sport Juan Bielovucic": LIM,
    "Sport Inca": LIM, "Atlético Peruano": LIM, "Sport Sáenz Peña": LIM, "Jorge Chávez N°1": LIM,
}

REGRAS: list[tuple[str, str, int, int]] = [
    # Liga Peruana (1912-1921): clubes só das ordens e listas de participantes das páginas peru1912-1921 (D-06 A)
    (r"escuela militar( de chorrillos)?", "Escuela Militar de Chorrillos", 1900, 1930),
    (r"miraflores (sc|sporting)", "Miraflores Sporting", 1900, 1930),
    (r"sport vitarte", "Sport Vitarte", 1900, 1930),
    (r"atletico grau (no|n|nr) ?1( lima)?", "Atlético Grau No. 1", 1900, 1930),
    (r"union miraflores", "Unión Miraflores", 1900, 1930),
    (r"sporting fry", "Sporting Fry", 1900, 1930),
    (r"sport tacna (no|n|nr) ?1", "Sport Tacna No. 1", 1900, 1930),
    (r"union peru", "Unión Perú", 1900, 1930),
    (r"fraternal barranco", "Fraternal Barranco", 1900, 1930),
    (r"escuela de artes y oficios", "Escuela de Artes y Oficios", 1900, 1930),
    (r"sportivo lima", "Sportivo Lima", 1900, 1930),
    (r"sport huascar", "Sport Huascar", 1900, 1930),
    (r"sport calavera", "Sport Calavera", 1900, 1930),
    (r"union barranco", "Unión Barranco", 1900, 1930),
    (r"saenz pena", "Sport Sáenz Peña", 1900, 1960),
    # Lima e Callao
    (r"(club )?universitario( de deportes)?( lima)?|universitario lima|federacion universitaria|fed universitaria|u$|"
     r"union huallaspanca universitario$", "Universitario", 1924, 2100),
    (r"(club )?alianza lima( lima)?|sport alianza|alianza$", "Alianza Lima", 1901, 2100),
    (r"(club )?sp(o|i)rting cristal|sp cristal|cristal$", "Sporting Cristal", 1955, 2100),
    (r"sports? ?boys( association| callao)*|s boys", "Sport Boys", 1927, 2100),
    (r"(centro )?dep(ortivo)? mun(i)?cipal( lima)?|municipal( lima)?$", "Deportivo Municipal", 1935, 2100),
    (r"(club )?atletico chalaco( callao)?", "Atlético Chalaco", 1902, 2100),
    (r"univ(ersidad)? ?san martin( de p(orres)?)?( lima)?|universidad smp|san martin$", "Universidad San Martín", 2004, 2100),
    (r"defensor lima", "Defensor Lima", 1931, 2100),
    (r"(club )?mariscal sucre( de deportes)?|sucre f ?b? ?c|sucre$", "Mariscal Sucre", 1926, 2100),
    (r"centro iqueno", "Centro Iqueño", 1927, 2100),
    (r"(club )?sporting tabaco", "Sporting Tabaco", 1928, 2100),
    (r"total (chalaco|clean)( callao| arequipa)?", "Total Chalaco", 2004, 2100),
    (r"guardia republicana|republicana$", "Guardia Republicana", 1980, 2100),
    (r"(colegio |dep(ortivo)? |asociacion deportiva )?san agustin", "Deportivo San Agustín", 1970, 2100),
    (r"interna(z|c)ionale?|internacional$", "Internazionale de San Borja", 1980, 2100),
    (r"a ?e ?l ?u", "AELU", 1950, 2100),
    (r"lawn tennis de la exp(osicion)?( futbol)?", "Lawn Tennis de la Exposición", 1920, 1960),
    (r"lawn tennis", "Lawn Tennis", 1990, 2100),
    (r"circolo (s(portivo)? )?ital(iano)?", "Circolo Sportivo Italiano", 1900, 2100),
    (r"sportivo tarapaca (ferrocarril|ff ?cc)", "Sportivo Tarapacá Ferrocarril", 1900, 2100),
    (r"union buenos aires", "Unión Buenos Aires", 1900, 2100),
    (r"sport progreso", "Sport Progreso", 1900, 2100),
    (r"(club )?teniente ruiz", "Teniente Ruiz", 1900, 2100),
    (r"(club sportivo )?jorge washington( callao)?", "Jorge Washington", 1900, 2100),
    (r"deportivo nacional", "Deportivo Nacional", 1900, 1960),
    (r"(sport )?jose galvez", "Sport José Gálvez", 1900, 1925),
    (r"sport jose galvez", "Sport José Gálvez", 1926, 1960),
    (r"lima cricket( and football club| fc)?", "Lima Cricket", 1900, 1960),
    (r"(sport )?juan biel(o|u)vucic( no 1)?", "Sport Juan Bielovucic", 1900, 1960),
    (r"sport inca", "Sport Inca", 1900, 1960),
    (r"atletico peruano", "Atlético Peruano", 1900, 1960),
    (r"sport saenz pena", "Sport Sáenz Peña", 1900, 1960),
    # PE-001: N°1 só com o número escrito; "Jorge Chávez" sem número (vice de 1918 e 1921) é o do Callao
    (r"(club sportivo )?jorge chavez (n|no|nr) ?o? ?1", "Jorge Chávez N°1", 1900, 1925),
    (r"(club sportivo )?jorge chavez$", "Jorge Chávez N°1", 1912, 1915),   # o do Callao (N°2) só entra em 1916
    (r"(asociacion|association) alianza", "Asociación Alianza", 1900, 2100),
    (r"association football club|association fbc", "Association FBC", 1900, 2100),
    (r"ciclista( lima)?( assoc(iation)?)?", "Ciclista Lima", 1896, 2100),
    (r"(escuela de )?hidroaviacion", "Hidroaviación", 1900, 2100),
    (r"alianza chorrillos", "Alianza Chorrillos", 1900, 2100),
    (r"(club )?(union )?santa catalina", "Santa Catalina", 1900, 2100),
    (r"(club sporting )?alberto secada", "Alberto Secada", 1900, 2100),
    (r"(club sportivo )?jorge chavez( callao)?", "Jorge Chávez", 1900, 2100),
    (r"(club sport )?jose olaya", "José Olaya", 1900, 2100),
    (r"union (f b c|futbol club|fc)$", "Unión FC", 1900, 1960),
    (r"(alianza|atletico) frigorifico( nacional)?|alianza callao( callao)?", "Alianza Frigorífico", 1900, 1960),
    (r"atletico barrio frigorifico", "Atlético Barrio Frigorífico", 1960, 2100),
    (r"telmo carbajo( callao)?", "Telmo Carbajo", 1900, 2100),
    (r"progresista apurimac( callao)?", "Progresista Apurímac", 1900, 2100),
    (r"atletico cordoba", "Atlético Córdoba", 1900, 2100),
    (r"santiago barranco", "Santiago Barranco", 1900, 2100),
    (r"union carbone", "Unión Carbone", 1900, 2100),
    (r"sportivo melgar", "Sportivo Melgar", 1900, 1960),
    (r"(club )?carlos concha( callao)?", "Carlos Concha", 1900, 2100),
    (r"union callao( callao)?", "Unión Callao", 1900, 2100),
    (r"(asociacion|association) chorrillos", "Asociación Chorrillos", 1900, 2100),
    (r"(club )?mariscal castilla", "Mariscal Castilla", 1900, 2100),
    (r"porvenir miraflores", "Porvenir Miraflores", 1900, 2100),
    (r"kdt nacional( sporting club| callao)?", "KDT Nacional", 1900, 2100),
    (r"union america", "Unión América", 1900, 2100),
    (r"defensor arica", "Defensor Arica", 1900, 2100),
    (r"deportivo sima( callao)?", "Deportivo SIMA", 1900, 2100),
    (r"atletico deportivo olimpico( callao)?", "Atlético Olímpico", 1900, 2100),
    (r"union gonzales prada", "Unión Gonzales Prada", 1900, 2100),
    (r"academia cantolao( callao)?", "Academia Cantolao", 1900, 2100),
    (r"pacifico fc( lima)?", "Pacífico FC", 1900, 2100),
    (r"sport pacifico", "Sport Pacífico", 1900, 2100),
    (r"sportivo union", "Sportivo Unión", 1900, 2100),
    (r"deportivo hospital", "Deportivo Hospital", 1900, 2100),
    (r"meteor sport club", "Meteor Sport Club", 1900, 2100),
    (r"juventud la palma( huacho)?", "Juventud La Palma", 1900, 2100),
    (r"juventud la joya( chancay)?", "Juventud La Joya", 1900, 2100),
    (r"(sport )?un[io]*n hu?a?ral( huaral)?|huaral$", "Unión Huaral", 1940, 2100),
    (r"walter ormeno( canete)?", "Walter Ormeño", 1900, 2100),
    (r"america cochahuayco", "América Cochahuayco", 1900, 2100),
    (r"atletico minero( matucana)?", "Atlético Minero", 1900, 2100),
    (r"(deportivo )?wanka", "Deportivo Wanka", 1900, 2100),
    # resto do país
    (r"(fbc |m )?melgar( f ?b ?c)?( arequipa)?", "Melgar", 1915, 2100),
    (r"cienciano( cusco| cuzco)?", "Cienciano", 1901, 2100),
    (r"aurich canana|juan aurich canana|(juan )?aurich", "Aurich-Cañaña", 1994, 1996),   # fusão de 1994 a 1996
    (r"(j |juan )?aurich( chiclayo)?", "Juan Aurich", 1922, 2100),
    (r"(univ(ersidad)? )?cesar vallejo( trujillo)?|universidad cv", "César Vallejo", 1996, 2100),
    (r"sport huancayo", "Sport Huancayo", 2007, 2100),
    (r"u ?t ?c( cajamarca)?|univ(ersidad)? tecnica( de)? cajamarca", "UTC", 1964, 2100),
    (r"alianza atl(etico)?( sullana)?|a atletico|alanza atletico", "Alianza Atlético", 1920, 2100),
    (r"(cnel |coronel )?bolognesi( tacna| fc)?|cnel bolognesi", "Coronel Bolognesi", 1929, 2100),
    (r"leon( de)? hu?a?nuco|leon$", "León de Huánuco", 1946, 2100),
    (r"inti gas( deportes)?( ica| ayacucho)?|ayacucho fc", "Ayacucho", 2008, 2100),
    (r"(e ?m ?d )?binacional( arequipa| juliaca| jul)?", "Binacional", 2010, 2100),
    (r"real garcilaso( cusco)?|cusco( f ?c)?( cusco)?", "Cusco FC", 2009, 2100),
    (r"deportivo garcilaso( cusco)?", "Deportivo Garcilaso", 1950, 2100),
    (r"dep(ortivo)? los chankas( andahuaylas)?", "Los Chankas", 2000, 2100),
    (r"(asociacion deportiva )?(tarma|\(tarma\))$|a ?d ?t( tarma)?|asociacion deportiva tarma", "ADT", 1929, 2100),
    (r"carlos a? ?mann?ucci( trujillo)?", "Carlos Mannucci", 1959, 2100),
    (r"(atletico ?|miguel )grau( piura)?|atleticograu", "Atlético Grau", 1919, 2100),
    (r"c ?n ?i|colegio nac(ional)?( de)? iquitos", "CNI", 1926, 2100),
    (r"sport ancash( huaraz)?", "Sport Áncash", 1967, 2100),
    (r"jose g[ae]lvez( fbc)?( chimbote)?|galvez$", "José Gálvez", 1951, 2100),
    (r"un[io]*n comercio( moyobamba)?", "Unión Comercio", 2002, 2100),
    (r"union minas( cerro de pasco)?|minas$", "Unión Minas", 1980, 2100),
    (r"(deportivo )?pesquero", "Deportivo Pesquero", 1990, 2100),
    (r"(deportivo )?sipesa( chimbote)?", "Deportivo Sipesa", 1990, 2100),
    (r"(deportivo )?canana( lambayeque)?", "Deportivo Cañaña", 1980, 2100),
    (r"hungaritos agustinos( iquitos)?", "Hungaritos Agustinos", 1980, 2100),
    (r"libertad( trujillo)?", "Libertad de Trujillo", 1980, 2100),
    (r"diablos rojos( de)?( juliaca)?", "Diablos Rojos", 1960, 2100),
    (r"alfonso ugarte( de)? chiclin|(club deportivo )?alfonso ugarte", "Alfonso Ugarte de Chiclín", 1960, 1970),
    (r"(club deportivo )?alfonso ugarte( de)?( puno)?", "Alfonso Ugarte", 1971, 2100),
    (r"(atletico )?torino( talara)?|aletico torino", "Atlético Torino", 1960, 2100),
    (r"defensor anda( aucayacu)?", "Defensor ANDA", 1980, 2100),
    (r"(club )?atl(etico)? huracan( moquegua)?", "Atlético Huracán", 1980, 2100),
    (r"mina san vicente( san ramon)?", "Mina San Vicente", 1980, 2100),
    (r"deportivo junin( huancayo)?", "Deportivo Junín", 1970, 2100),
    (r"huancayo f ?c( huancayo)?", "Huancayo FC", 1980, 2100),
    (r"sport pilsen( guadalupe)?", "Sport Pilsen", 1980, 2100),
    (r"los espartanos( pacasmayo)?", "Los Espartanos", 1980, 2100),
    (r"chanchamayo f ?c( la merced)?", "Chanchamayo FC", 1980, 2100),
    (r"dep(o|ortivo)? pucallpa( pucallpa)?", "Deportivo Pucallpa", 1980, 2100),
    (r"deportivo cooptrip( pucallpa)?", "Deportivo COOPTRIP", 1980, 2100),
    (r"alianza naval( mollendo)?", "Alianza Naval", 1980, 2100),
    (r"alipio ponce( mazamari)?", "Alipio Ponce", 1980, 2100),
    (r"dep(ortivo)? tintaya( yauri)?", "Deportivo Tintaya", 1980, 2100),
    (r"juvenil los angeles( moquegua)?", "Juvenil Los Ángeles", 1980, 2100),
    (r"dep(ortivo)? los angeles", "Deportivo Los Ángeles", 1980, 2100),
    (r"fbc aurora", "FBC Aurora", 1980, 2100),
    (r"hijos de yurimaguas", "Hijos de Yurimaguas", 1980, 2100),
    (r"dep(ortivo)? yurimaguas", "Deportivo Yurimaguas", 1980, 2100),
    (r"union tarapoto", "Unión Tarapoto", 1980, 2100),
    (r"alianza huanuco", "Alianza Huánuco", 1980, 2100),
    (r"mariscal nieto", "Mariscal Nieto", 1980, 2100),
    (r"15 de setiembre", "15 de Setiembre", 1980, 2100),
    (r"(grau( |-)?)?estudiantes( de medicina)?( grau)?|medicina$", "Estudiantes de Medicina", 1990, 2100),
    (r"(sport )?coopsol( trujillo)?", "Coopsol", 1990, 2100),
    (r"(deportivo )?u ?p ?a ?o", "Deportivo UPAO", 1990, 2100),
    (r"(club )?octavio espino(s|z)a( ica)?", "Octavio Espinosa", 1950, 2100),
    (r"union tuman( tuman)?", "Unión Tumán", 1950, 2100),
    (r"pierola f ?b ?c( arequipa)?", "Piérola", 1950, 2100),
    (r"union pesquero( ilo)?", "Unión Pesquero", 1950, 2100),
    (r"sportivo huracan( arequipa)?", "Sportivo Huracán", 1950, 2100),
    (r"comerciantes unidos( cutervo)?", "Comerciantes Unidos", 1990, 2100),
    (r"dep(ortivo)? llacuabamba( pataz)?", "Deportivo Llacuabamba", 1990, 2100),
    (r"pirata fc( chiclayo)?", "Pirata FC", 1990, 2100),
    (r"(f ?c )?carlos stein( chiclayo| lambayeque)?", "Carlos Stein", 1990, 2100),
    (r"juan pablo ii( collage)?( chongoyape)?", "Juan Pablo II", 1990, 2100),
    (r"alianza universidad( huanuco)?", "Alianza Universidad", 1990, 2100),
    (r"sport rosario( huaraz)?", "Sport Rosario", 1990, 2100),
    (r"defensor la bocana( sechura)?", "Defensor La Bocana", 1990, 2100),
    (r"sport loreto( pucallpa)?", "Sport Loreto", 1990, 2100),
    (r"san simon( moquegua)?", "San Simón", 1990, 2100),
    (r"los caimanes( de puerto eten)?( chiclayo)?", "Los Caimanes", 1990, 2100),
    (r"cobresol( fbc)?( moquegua)?", "Cobresol", 1990, 2100),
    (r"atl(etico)? universidad( nacional)?( arequipa)?", "Atlético Universidad", 1990, 2100),
    (r"union hua?y?llaspanca", "Unión Huayllaspanca", 1980, 2100),
    (r"(la )?loretana", "La Loretana", 1980, 2100),
    (r"alcides( vigo( hurtado)?)?", "Alcides Vigo", 1980, 2100),
    (r"i ?m ?i( f ?c)?", "IMI", 1980, 2100),
    (r"deportivo bancos", "Deportivo Bancos", 1980, 2100),
]

_LIXO = re.compile(r"^\s*[-/]\s*|\s*-\s*$|\[\[|\]\]", re.I)


def _regra(k: str, ano: int) -> str | None:
    for kk in (k, re.sub(r"^(club|c|cd|csd) ", "", k)):
        for rx, exib, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.fullmatch(f"(?:{rx})" + r"(?:\s.*)?", kk):
                return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    return _regra(chave(_LIXO.sub("", nome.strip())), ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
