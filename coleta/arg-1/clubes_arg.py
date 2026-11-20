"""Identidade dos clubes argentinos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido no Brasil ("Boca Juniors", "River Plate", "Racing Club");
- homônimo dentro da Argentina ou com clube de outro país já no banco/pacotes: acrescenta a cidade
  ("Racing de Córdoba", "Gimnasia de Jujuy", "Arsenal de Sarandí", "Nacional de Buenos Aires");
- o mesmo clube com outro nome (English High School -> Alumni; Racing Football Club -> Racing Club) é um só,
  com o nome atual; os nomes antigos ficam no nomes_fonte.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano). A chave é o nome sem acento, em
minúsculas, com pontuação trocada por espaço (rsssf_sul.chave). Vale a primeira regra que casa com o começo da chave
no ano da edição; por isso as mais específicas vêm antes. Nome que sobra depois do clube (local do jogo colado na
coluna, como "Estudiantes de La Plata Atlanta, Buenos Aires") não atrapalha: a regra casa só o começo.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-sulamerica"))
from rsssf_sul import chave  # noqa: E402

BA, CABA = "Buenos Aires", "Ciudad de Buenos Aires"

# nome de exibição -> (cidade, província)
CLUBES: dict[str, tuple[str, str]] = {
    # ------------------------------------------------------------------ grandes e tradicionais
    "Boca Juniors": ("Buenos Aires", CABA), "River Plate": ("Buenos Aires", CABA), "Racing Club": ("Avellaneda", BA),
    "Independiente": ("Avellaneda", BA), "San Lorenzo": ("Buenos Aires", CABA), "Huracán": ("Buenos Aires", CABA),
    "Vélez Sarsfield": ("Buenos Aires", CABA), "Estudiantes": ("La Plata", BA), "Gimnasia La Plata": ("La Plata", BA),
    "Rosario Central": ("Rosario", "Santa Fe"), "Newell's Old Boys": ("Rosario", "Santa Fe"), "Argentinos Juniors": ("Buenos Aires", CABA),
    "Ferro Carril Oeste": ("Buenos Aires", CABA), "Platense": ("Vicente López", BA), "Lanús": ("Lanús", BA),
    "Banfield": ("Banfield", BA), "Chacarita Juniors": ("San Martín", BA), "Atlanta": ("Buenos Aires", CABA),
    "Quilmes": ("Quilmes", BA), "Tigre": ("Victoria", BA), "Talleres": ("Córdoba", "Córdoba"), "Belgrano": ("Córdoba", "Córdoba"),
    "Instituto": ("Córdoba", "Córdoba"), "Racing de Córdoba": ("Córdoba", "Córdoba"), "Colón": ("Santa Fe", "Santa Fe"),
    "Unión": ("Santa Fe", "Santa Fe"), "Atlético Tucumán": ("San Miguel de Tucumán", "Tucumán"),
    "San Martín de Tucumán": ("San Miguel de Tucumán", "Tucumán"), "Godoy Cruz": ("Godoy Cruz", "Mendoza"),
    "Independiente Rivadavia": ("Mendoza", "Mendoza"), "Gimnasia de Mendoza": ("Mendoza", "Mendoza"),
    "San Martín de Mendoza": ("Mendoza", "Mendoza"), "Gimnasia de Jujuy": ("San Salvador de Jujuy", "Jujuy"),
    "San Martín de San Juan": ("San Juan", "San Juan"), "Olimpo": ("Bahía Blanca", BA), "Arsenal de Sarandí": ("Sarandí", BA),
    "Defensa y Justicia": ("Florencio Varela", BA), "Atlético Rafaela": ("Rafaela", "Santa Fe"), "Tiro Federal": ("Rosario", "Santa Fe"),
    "Aldosivi": ("Mar del Plata", BA), "Patronato": ("Paraná", "Entre Ríos"), "Temperley": ("Temperley", BA),
    "Sarmiento": ("Junín", BA), "Central Córdoba de Santiago del Estero": ("Santiago del Estero", "Santiago del Estero"),
    "Barracas Central": ("Buenos Aires", CABA), "Deportivo Riestra": ("Buenos Aires", CABA), "Crucero del Norte": ("Garupá", "Misiones"),
    "Nueva Chicago": ("Buenos Aires", CABA), "All Boys": ("Buenos Aires", CABA), "Almagro": ("José Ingenieros", BA),
    "Los Andes": ("Lomas de Zamora", BA), "Deportivo Español": ("Buenos Aires", CABA), "Deportivo Italiano": ("Buenos Aires", CABA),
    "Deportivo Armenio": ("Ingeniero Maschwitz", BA), "Deportivo Mandiyú": ("Corrientes", "Corrientes"), "Deportivo Morón": ("Morón", BA),
    "Gimnasia y Tiro": ("Salta", "Salta"), "Juventud Antoniana": ("Salta", "Salta"), "Central Norte": ("Salta", "Salta"),
    "Talleres de Remedios de Escalada": ("Remedios de Escalada", BA), "Central Córdoba de Rosario": ("Rosario", "Santa Fe"),
    "Douglas Haig": ("Pergamino", BA), "Defensores de Belgrano": ("Buenos Aires", CABA), "El Porvenir": ("Gerli", BA),
    "Excursionistas": ("Buenos Aires", CABA), "Colegiales": ("Munro", BA), "Sportivo Dock Sud": ("Dock Sud", BA),
    "Estudiantil Porteño": ("Buenos Aires", CABA), "San Telmo": ("Isla Maciel", BA), "Villa Dálmine": ("Campana", BA),
    # ------------------------------------------------------------------ 1891-1930 (amadores)
    "Saint Andrew's": ("Buenos Aires", CABA), "Caledonians": ("Buenos Aires", CABA), "Buenos Aires Football Club": ("Buenos Aires", CABA),
    "Buenos Aires and Rosario Railway": ("Buenos Aires", CABA), "Belgrano Football Club": ("Buenos Aires", CABA),
    "Hurlingham": ("Hurlingham", BA), "Lomas Athletic": ("Lomas de Zamora", BA), "Lomas Academicals": ("Lomas de Zamora", BA),
    "Flores Athletic": ("Buenos Aires", CABA), "Rosario Athletic": ("Rosario", "Santa Fe"), "Retiro Athletic": ("Buenos Aires", CABA),
    "Alumni": ("Buenos Aires", CABA), "Belgrano Athletic": ("Buenos Aires", CABA), "Belgrano Athletic Extra": ("Buenos Aires", CABA), "Belgrano Athletic B": ("Buenos Aires", CABA),
    "Lanús Athletic": ("Lanús", BA), "Lobos Athletic": ("Lobos", BA), "Palermo Athletic": ("Buenos Aires", CABA),
    "United Banks": ("Buenos Aires", CABA), "Barracas Athletic": ("Buenos Aires", CABA), "Estudiantes de Buenos Aires": ("Buenos Aires", CABA),
    "San Isidro": ("San Isidro", BA), "Argentino de Quilmes": ("Quilmes", BA), "Reformer": ("Campana", BA),
    "San Martín Athletic": ("Buenos Aires", CABA), "Nacional de Buenos Aires": ("Buenos Aires", CABA), "Porteño": ("Buenos Aires", CABA),
    "Gimnasia de Buenos Aires": ("Buenos Aires", CABA), "Olivos": ("Olivos", BA), "Riachuelo": ("Buenos Aires", CABA),
    "Ferrocarril Sud": ("Buenos Aires", CABA), "Comercio": ("Buenos Aires", CABA),
    "Kimberley de Buenos Aires": ("Buenos Aires", CABA), "Sportiva Argentina": ("Buenos Aires", CABA), "Floresta": ("Buenos Aires", CABA),
    "Columbian": ("Buenos Aires", CABA), "Eureka": ("Buenos Aires", CABA), "Sportivo Barracas": ("Buenos Aires", CABA),
    "Sportivo Buenos Aires": ("Isla Maciel", BA), "Sportivo Palermo": ("Buenos Aires", CABA), "Palermo": ("Buenos Aires", CABA),
    "Del Plata": ("Buenos Aires", CABA), "Boca Alumni": ("Buenos Aires", CABA),
    "Alvear": ("Buenos Aires", CABA), "Progresista": ("Buenos Aires", CABA), "Sportsman": ("Buenos Aires", CABA),
    "Universal": ("Buenos Aires", CABA), 
    "General San Martín": ("Buenos Aires", CABA), "Argentino del Sud": ("Buenos Aires", CABA),
    "Argentino de Lomas": ("Lomas de Zamora", BA), "Liberal Argentino": ("Buenos Aires", CABA),
    "San Fernando": ("San Fernando", BA), "General Mitre": ("Buenos Aires", CABA), "Honor y Patria": ("Bernal", BA),
    "Sportivo Balcarce": ("Buenos Aires", CABA), "Gutenberg": ("Buenos Aires", CABA),
    "Ramsar": ("Buenos Aires", CABA), "Sportivo Acassuso": ("San Isidro", BA), "Sportivo Alsina": ("Valentín Alsina", BA),
    "Unión Talleres-Lanús": ("Lanús", BA),
    # ------------------------------------------------------------------ interior (Nacional 1967-1985) e outros
    "Huracán de Bahía Blanca": ("Bahía Blanca", BA), "Huracán de Comodoro Rivadavia": ("Comodoro Rivadavia", "Chubut"),
    "Huracán de Corrientes": ("Corrientes", "Corrientes"), "Huracán de Ingeniero White": ("Ingeniero White", BA),
    "Huracán Las Heras": ("Las Heras", "Mendoza"), "Huracán de San Rafael": ("San Rafael", "Mendoza"),
    "Huracán de Tres Arroyos": ("Tres Arroyos", BA), "San Lorenzo de Mar del Plata": ("Mar del Plata", BA),
    "Kimberley": ("Mar del Plata", BA), "Alvarado": ("Mar del Plata", BA), "Círculo Deportivo": ("Nicanor Otamendi", BA),
    "Estudiantes de Río Cuarto": ("Río Cuarto", "Córdoba"), "Estudiantes de Santiago del Estero": ("Santiago del Estero", "Santiago del Estero"),
    "Altos Hornos Zapla": ("Palpalá", "Jujuy"), "Atlético Ledesma": ("Libertador General San Martín", "Jujuy"),
    "Chaco For Ever": ("Resistencia", "Chaco"), "Sarmiento de Resistencia": ("Resistencia", "Chaco"), "Don Orione": ("Barranqueras", "Chaco"),
    "Cipolletti": ("Cipolletti", "Río Negro"), "Deportivo Roca": ("General Roca", "Río Negro"),
    "Guaraní Antonio Franco": ("Posadas", "Misiones"), "Bartolomé Mitre": ("Posadas", "Misiones"),
    "Sportivo Desamparados": ("San Juan", "San Juan"), "Juventud Alianza": ("Santa Lucía", "San Juan"),
    "Atlético Concepción": ("Banda del Río Salí", "Tucumán"), "Independiente de Trelew": ("Trelew", "Chubut"),
    "Jorge Newbery": ("Junín", BA), "Mariano Moreno": ("Junín", BA), "Puerto Comercial": ("Ingeniero White", BA),
    "Atlético Regina": ("Villa Regina", "Río Negro"), "Unión San Vicente": ("Córdoba", "Córdoba"), "Renato Cesarini": ("Rosario", "Santa Fe"),
    "Loma Negra": ("Olavarría", BA), "Ferro Carril Oeste de General Pico": ("General Pico", "La Pampa"),
    "Unión de General Pinedo": ("General Pinedo", "Chaco"), "Atlético Uruguay": ("Concepción del Uruguay", "Entre Ríos"),
    "Andino": ("La Rioja", "La Rioja"), "Atlético Santa Rosa": ("Santa Rosa", "La Pampa"), "Argentino de Firmat": ("Firmat", "Santa Fe"),
    "Ramón Santamarina": ("Tandil", BA), "Alianza Juventud Pringles": ("Coronel Pringles", BA), "Sportivo Patria": ("Formosa", "Formosa"),
    "Atlético Cipolletti": ("Cipolletti", "Río Negro"), "San Martín de Monte Comán": ("Monte Comán", "Mendoza"),
}

REGRAS: list[tuple[str, str, int, int]] = [
    # ---------------------------------------------- nomes compostos e homônimos (antes dos nomes curtos)
    (r"atlanta argentinos juniors", "Argentinos Juniors", 1934, 1934),   # fusão de 1934: a tabela da RSSSF conta como Argentinos
    (r"union talleres lanus", "Unión Talleres-Lanús", 1934, 1934),
    (r"(c a |club atletico )?racing (c|cba|cor|cordoba)\b|atletico racing", "Racing de Córdoba", 1960, 2100),
    (r"(.*\b)?gimnasia (y )?(esg(rima)?|egrima)? ?\(?(j|juj|jujuy|san salvador de jujuy)\b", "Gimnasia de Jujuy", 1960, 2100),
    (r"(.*\b)?gimnasia (y )?(esg(rima)?|egrima)? ?\(?(m|mza|mdz|mendoza)\b", "Gimnasia de Mendoza", 1960, 2100),
    (r"gimnasia y tiro|gimnasia s$", "Gimnasia y Tiro", 1960, 2100),
    (r"(.*\b)?(gimnasia|gimansia|gimnsasia|grimnasia|ginmasia) (y )?(esgrima )?(ba|bue|buenos aires)\b", "Gimnasia de Buenos Aires", 1900, 1930),
    (r"(club de )?gimnasia y esgrima$", "Gimnasia de Buenos Aires", 1900, 1914),
    (r"(.*\b)?(gimnasia|gimansia|gimnsasia|grimnasia|ginmasia)\b", "Gimnasia La Plata", 1915, 2100),
    (r"(ca |club atletico )?san martin (t|tuc|tucuman|sm|san miguel|sm de tucuman)\b", "San Martín de Tucumán", 1960, 2100),
    (r"(ca |club atletico )?san martin (sj|san juan)\b", "San Martín de San Juan", 1960, 2100),
    (r"san martin (m|mza|mdz|mendoza|gsm)\b", "San Martín de Mendoza", 1960, 2100),
    (r"(c a |ca |club atletico )?san martin$", "San Martín de San Juan", 2015, 2018),   # RSSSF 2015-2017/18: só "San Martín" (San Juan)
    (r"san martin ac|san martin athletic", "San Martín Athletic", 1900, 1915),
    (r"(gral|general) san martin", "General San Martín", 1920, 1940),
    (r"san lorenzo (mar del plata|mdp|mdq)", "San Lorenzo de Mar del Plata", 1960, 2100),
    (r"huracan (bahia blanca|bb)\b", "Huracán de Bahía Blanca", 1960, 2100),
    (r"huracan (com ?rivadavia|comodoro rivadavia|cr)\b", "Huracán de Comodoro Rivadavia", 1960, 2100),
    (r"huracan (ctes|corrientes)\b", "Huracán de Corrientes", 1960, 2100),
    (r"huracan (iwh|ingeniero white)\b", "Huracán de Ingeniero White", 1960, 2100),
    (r"huracan las heras", "Huracán Las Heras", 1960, 2100),
    (r"huracan (sr|san rafael)\b", "Huracán de San Rafael", 1960, 2100),
    (r"huracan (ta|tres arroyos)\b", "Huracán de Tres Arroyos", 1960, 2100),
    (r"estudiantes (rc|rio cuarto|rio iv)\b", "Estudiantes de Río Cuarto", 1960, 2100),
    (r"estudiantes (sgo|santiago del estero|sgo del estero)\b", "Estudiantes de Santiago del Estero", 1960, 2100),
    (r"estudiantes (ba|bs ?as|bs aires|buenos aires|c)\b", "Estudiantes de Buenos Aires", 1900, 2100),
    (r"(club de )?estudiantes$|(club )?atletico estudiantes|ca estudiantes", "Estudiantes de Buenos Aires", 1900, 1934),
    (r"(club )?estudiantes (de )?(la plata|lp|lpg|eva peron)|estudiantes lp", "Estudiantes", 1900, 2100),
    (r"estudiantes$|estudiantes \(?la plata\)?", "Estudiantes", 1935, 2100),
    (r"estudiantes batigre", "Estudiantes de Buenos Aires", 1926, 1926),
    (r"(.*\b)?independiente riv(adavia)?\b|ind rivadavia|cs independiente rivadavia", "Independiente Rivadavia", 1960, 2100),
    (r"independiente \(?t\)?$", "Independiente de Trelew", 1972, 1972),
    (r"(ca |club atletico )?(independiente|indpendiente)\b", "Independiente", 1900, 2100),
    (r"(c a |c |ca |club atletico )?talleres (re|rde|remedios de escalada)\b", "Talleres de Remedios de Escalada", 1920, 1960),
    (r"(ca |club atletico )?(talleres|tallares)\b", "Talleres", 1960, 2100),
    (r"(ca |club atletico )?talleres\b", "Talleres de Remedios de Escalada", 1920, 1959),
    (r"central cordoba \(?(sant|sgo|sde|santiago)", "Central Córdoba de Santiago del Estero", 1960, 2100),
    (r"(ca |club atletico )?central cordoba", "Central Córdoba de Santiago del Estero", 2019, 2100),
    (r"(club atletico )?central cordoba", "Central Córdoba de Rosario", 1900, 2018),
    (r"sarmiento \(?(chaco|resistencia)\b", "Sarmiento de Resistencia", 1960, 2100),
    (r"(ca |club atletico )?sarmiento\b", "Sarmiento", 1960, 2100),
    (r"kimberley (ac|athletic)", "Kimberley de Buenos Aires", 1900, 1930),
    (r"kimberley", "Kimberley de Buenos Aires", 1900, 1930),
    (r"kimberley", "Kimberley", 1960, 2100),
    (r"ferro (carril oeste )?\(?(gral ?pico|general pico)", "Ferro Carril Oeste de General Pico", 1960, 2100),
    (r"union \(?(general pinedo|gral ?pinedo)", "Unión de General Pinedo", 1960, 2100),
    (r"union san vicente", "Unión San Vicente", 1960, 2100),
    (r"(ca |club atletico )?union\b", "Unión", 1960, 2100),
    (r"lanus athletic", "Lanús Athletic", 1890, 1905),
    (r"(ca |club atletico )?lanus\b", "Lanús", 1915, 2100),
    (r"(ca |club atletico )?belgrano (c|cba|cor|cordoba)\b|belgrano cba|(ca |club atletico )?belgrano$", "Belgrano", 1960, 2100),
    (r"(ca )?belgrano (ac |athletic club |athletic )?extra|belgrano extra", "Belgrano Athletic Extra", 1906, 1906),
    (r"belgrano (fc|football club)", "Belgrano Football Club", 1891, 1891),
    (r"belgrano b$", "Belgrano Athletic B", 1897, 1897),
    (r"belgrano (ac|athletic)|belgrano$", "Belgrano Athletic", 1890, 1920),
    (r"argentino del sud|argentinos del sud", "Argentino del Sud", 1900, 1940),
    (r"argentino de (banfield|lomas)", "Argentino de Lomas", 1900, 1940),   # "Argentino de Banfield was renamed Argentino de Lomas"
    (r"argentino de temperley", "Temperley", 1900, 1940),   # "Argentino de Temperley was renamed Temperley in 1935"
    (r"(ca |club atletico )?argentino de quilmes", "Argentino de Quilmes", 1890, 1970),
    (r"argentino \(?f\)?$|argentino de firmat", "Argentino de Firmat", 1985, 1985),
    (r"(.*\b)?(argentinos|arg) (j|jrs|js|juniors|junors)\b", "Argentinos Juniors", 1915, 2100),
    (r"(ca |club atletico )?atletico tucuman|atl tucuman|atletico \(?tucuman\)?|(ca |club atletico )?tucuman\b", "Atlético Tucumán", 1960, 2100),
    (r"(.*\b)?(atletico|atletido|atl) (de )?rafaela", "Atlético Rafaela", 1990, 2100),
    (r"atletico concepcion", "Atlético Concepción", 1960, 2100),
    (r"atletico ledesma", "Atlético Ledesma", 1960, 2100),
    (r"atletico regina", "Atlético Regina", 1960, 2100),
    (r"atletico santa rosa", "Atlético Santa Rosa", 1960, 2100),
    (r"atletico uruguay", "Atlético Uruguay", 1960, 2100),
    (r"atletico cipolletti", "Atlético Cipolletti", 1985, 1985),
    (r"atletico velez sarsfield", "Vélez Sarsfield", 2014, 2014),
    (r"(ca |club atletico )?(velez|velez sarsfield|velez sarfield|velez sarsfield)\b", "Vélez Sarsfield", 1910, 2100),
    # ---------------------------------------------- grandes
    (r"(ca |club atletico )?(boca juniors|boca)\b(?! alumni)", "Boca Juniors", 1905, 2100),
    (r"boca alumni", "Boca Alumni", 1915, 1930),
    (r"(ca |club atletico )?river( plate)?\b", "River Plate", 1905, 2100),
    (r"(c a |ca |club atletico )?racing( club| fc| football club)?$|(c a |ca )?racing (club|fc|football club)\b|racing avellaneda", "Racing Club", 1905, 2100),
    (r"(ca |club atletico |club a |club atl |c a s )?san lorenzo\b|san lorenzoliberal", "San Lorenzo", 1910, 2100),
    (r"(ca |club atletico )?huracan\b", "Huracán", 1910, 2100),
    (r"(ca |club atletico )?(newell s|newells)\b", "Newell's Old Boys", 1930, 2100),
    (r"(ca |club atletico )?rosario (c|cent|ctral|central)\b", "Rosario Central", 1930, 2100),
    (r"(c a |club atletico |club |ca )?ferro\b|ferrocarril( oeste)?$", "Ferro Carril Oeste", 1905, 2100),
    (r"(ca |club atletico )?platense (ii|ba)$", "Universal", 1920, 1930),   # o segundo Platense, da Asociación; virou Retiro e depois Universal
    (r"(ca |club atletico )?platense", "Platense", 1905, 2100),
    (r"(ca |club atletico )?banfield", "Banfield", 1890, 2100),
    (r"(ca |club atletico )?chacarita", "Chacarita Juniors", 1920, 2100),
    (r"(ca |club atletico )?atlanta", "Atlanta", 1905, 2100),
    (r"quilmes rovers|quilmes club|(.*\b)?quilmes( ac| athletic club| atletico club)?$|quilmes athletic|quilmes atletico", "Quilmes", 1890, 2100),
    (r"(ca |club atletico )?(del )?tigre", "Tigre", 1905, 2100),
    (r"(.*\b)?instituto|insituto", "Instituto", 1960, 2100),
    (r"(ca |club atletico )?colon\b|asoc civil club atletico colon|a civil club atletico colon", "Colón", 1960, 2100),
    (r"(.*\b)?godoy cruz", "Godoy Cruz", 1960, 2100),
    (r"(club )?olimpo", "Olimpo", 1960, 2100),
    (r"(ca |club atletico )?arsenal\b", "Arsenal de Sarandí", 1960, 2100),
    (r"(.*\b)?defensa y justicia", "Defensa y Justicia", 1960, 2100),
    (r"(ca |club atletico )?aldosivi", "Aldosivi", 1960, 2100),
    (r"(ca |club atletico )?patronato", "Patronato", 1960, 2100),
    (r"(ca |club atletico )?temperley", "Temperley", 1915, 2100),
    (r"(ca |club atletico )?barracas central", "Barracas Central", 1910, 2100),
    (r"deportivo riestra|club social cultural y deportivo riestra", "Deportivo Riestra", 1950, 2100),
    (r"(.*\b)?crucero del norte", "Crucero del Norte", 2000, 2100),
    (r"tiro federal", "Tiro Federal", 2000, 2100),
    (r"(ca |club atletico )?nueva chicago", "Nueva Chicago", 1910, 2100),
    (r"(ca |club atletico )?all boys", "All Boys", 1915, 2100),
    (r"(ca |club )?almagro", "Almagro", 1915, 2100),
    (r"(club atletico )?los andes", "Los Andes", 1950, 2100),
    (r"(dep|deportivo) espanol", "Deportivo Español", 1950, 2100),
    (r"(dep|deportivo) italiano", "Deportivo Italiano", 1950, 2100),
    (r"(dep|deportivo) armenio", "Deportivo Armenio", 1950, 2100),
    (r"(dep|deportivo)? ?mandiyu", "Deportivo Mandiyú", 1950, 2100),
    (r"(dep|deportivo|club deportivo) moron", "Deportivo Morón", 1950, 2100),
    (r"juv(entud)? antoniana", "Juventud Antoniana", 1960, 2100),
    (r"juventud alianza", "Juventud Alianza", 1960, 2100),
    (r"central norte", "Central Norte", 1960, 2100),
    (r"douglas haig", "Douglas Haig", 1960, 2100),
    (r"(ca |club atletico )?defensores de belgrano", "Defensores de Belgrano", 1910, 2100),
    (r"(club )?el porvenir", "El Porvenir", 1910, 2100),
    (r"(club atletico )?excursionistas", "Excursionistas", 1910, 2100),
    (r"(club atletico )?colegiales", "Colegiales", 1910, 2100),
    (r"(club )?sportivo dock sud|dock sud", "Sportivo Dock Sud", 1910, 2100),
    (r"(ca |club atletico )?estudiantil porteno", "Estudiantil Porteño", 1900, 2100),
    (r"(club atletico )?san telmo", "San Telmo", 1910, 2100),
    (r"villa dalmine", "Villa Dálmine", 1950, 2100),
    # ---------------------------------------------- 1891-1934
    (r"(saint|st) andrews?", "Saint Andrew's", 1890, 1900),
    (r"caledonians", "Caledonians", 1890, 1900),
    (r"buenos aires (fc|football club)", "Buenos Aires Football Club", 1890, 1900),
    (r"buenos aires (and|al)? ?rosario railways?", "Buenos Aires and Rosario Railway", 1890, 1900),
    (r"hurlingham", "Hurlingham", 1890, 1900),
    (r"lomas academ\w*", "Lomas Academicals", 1890, 1900),
    (r"lomas( ac| athletic| athletic club)?$|lomas athletic", "Lomas Athletic", 1890, 1915),
    (r"flores (ac|athletic)", "Flores Athletic", 1890, 1910),
    (r"rosario athletic", "Rosario Athletic", 1890, 1900),
    (r"retiro athletic", "Retiro Athletic", 1890, 1900),
    (r"(buenos aires )?english high school|alumni", "Alumni", 1890, 1915),
    (r"lobos", "Lobos Athletic", 1890, 1900),
    (r"palermo athletic", "Palermo Athletic", 1890, 1900),
    (r"united banks", "United Banks", 1890, 1900),
    (r"barracas (ac|athletic)", "Barracas Athletic", 1900, 1910),
    (r"(ca |club atletico )?(de )?san isidro", "San Isidro", 1900, 1935),
    (r"reformer", "Reformer", 1900, 1910),
    (r"nacional", "Nacional de Buenos Aires", 1908, 1908),
    (r"(ca |club atletico )?porteno", "Porteño", 1900, 1935),
    (r"(ca |club atletico )?olivos", "Olivos", 1910, 1915),
    (r"(ca |club atletico )?riachuelo", "Riachuelo", 1910, 1915),
    (r"(ca |club atletico )?(del )?ferrocarril sud", "Ferrocarril Sud", 1910, 1915),
    (r"(club )?hispano argentino", "Columbian", 1910, 1915),   # "Hispano Argentino was renamed Columbian"
    (r"comercio", "Comercio", 1910, 1916),
    (r"(sociedad )?sportiva argentina", "Sportiva Argentina", 1910, 1915),
    (r"floresta", "Floresta", 1910, 1916),
    (r"columbian", "Columbian", 1910, 1920),
    (r"eureka", "Eureka", 1910, 1920),
    (r"sportivo barracas", "Sportivo Barracas", 1910, 1940),
    (r"sportivo (de )?almagro", "Almagro", 1910, 1930),   # "Sportivo Almagro was renamed Almagro"
    (r"(social y )?sportivo buenos aires", "Sportivo Buenos Aires", 1910, 1940),
    (r"sportivo palermo", "Sportivo Palermo", 1915, 1940),
    (r"(ca |club atletico )?palermo", "Palermo", 1915, 1940),   # outro clube: em 1923 os dois jogaram a Asociación
    (r"sportivo del norte", "Colegiales", 1915, 1930),   # "Sportivo del Norte changed name to Colegiales"
    (r"del plata", "Del Plata", 1915, 1930),
    (r"alvear", "Alvear", 1915, 1930),
    (r"progresista", "Progresista", 1915, 1930),
    (r"sportsman", "Sportsman", 1915, 1930),
    (r"universal", "Universal", 1915, 1930),
    (r"(villa )?urquiza", "General San Martín", 1915, 1930),   # "Villa Urquiza changed name to General San Martín"
    (r"retiro$", "Universal", 1925, 1925),   # "Platense changed name to Retiro and later to Universal" (o Platense da Asociación)
    (r"liberal argentino", "Liberal Argentino", 1915, 1940),
    (r"san fernando", "San Fernando", 1915, 1940),
    (r"general mitre", "General Mitre", 1915, 1970),
    (r"honor y patria", "Honor y Patria", 1915, 1940),
    (r"sportivo balcarce", "Sportivo Balcarce", 1915, 1940),
    (r"gutenberg", "Gutenberg", 1915, 1940),
    (r"ramsar", "Ramsar", 1915, 1940),
    (r"sportivo acassuso", "Sportivo Acassuso", 1915, 1940),
    (r"sportivo alsina", "Sportivo Alsina", 1915, 1940),
    # ---------------------------------------------- interior, 1967-1985
    (r"altos hornos zapla", "Altos Hornos Zapla", 1960, 2100),
    (r"chaco for ever", "Chaco For Ever", 1960, 2100),
    (r"don orione", "Don Orione", 1960, 2100),
    (r"cipolletti", "Cipolletti", 1960, 2100),
    (r"deportivo roca", "Deportivo Roca", 1960, 2100),
    (r"guarani a(ntonio)? ?franco", "Guaraní Antonio Franco", 1960, 2100),
    (r"bartolome mitre", "Bartolomé Mitre", 1960, 2100),
    (r"(sp|sportivo) desamparados", "Sportivo Desamparados", 1960, 2100),
    (r"jorge newbery", "Jorge Newbery", 1960, 2100),
    (r"mariano moreno", "Mariano Moreno", 1960, 2100),
    (r"puerto comercial", "Puerto Comercial", 1960, 2100),
    (r"renato cesarini", "Renato Cesarini", 1960, 2100),
    (r"loma negra", "Loma Negra", 1960, 2100),
    (r"andino", "Andino", 1960, 2100),
    (r"ramon santamarina", "Ramón Santamarina", 1960, 2100),
    (r"alianza juventud pringles", "Alianza Juventud Pringles", 1960, 2100),
    (r"sportivo patria", "Sportivo Patria", 1960, 2100),
    (r"alvarado", "Alvarado", 1960, 2100),
    (r"circulo deportivo", "Círculo Deportivo", 1960, 2100),
]


_FORMA_INI = re.compile(r"^(asociacion civil|asoc civil|a civil) ")
_FORMA_FIM = re.compile(r" (asociacion civil|asoc civil|soc civil|sociedad civil|sociedad c|soc civ|sociedad|soc)$")


def _regra(k: str, ano: int) -> str | None:
    k = _FORMA_FIM.sub("", _FORMA_INI.sub("", k))   # forma jurídica: "Asociación Civil Club Atlético Colón"
    for kk in (k, re.sub(r"^(club|c) ", "", k)):   # "Club Sportivo Barracas" -> "sportivo barracas"
        for rx, exib, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.match(rx + r"(?:\b|$)", kk):
                return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido).
    `cidade` (a sede que a tabela publicada mostra ao lado do nome) desfaz homônimos como os dois San Martín de 2018/19."""
    if cidade:
        base = _FORMA_FIM.sub("", _FORMA_INI.sub("", chave(nome)))
        x = _regra(f"{base} {chave(cidade)}", ano)
        if x:
            return x
    x = _regra(chave(nome), ano)
    if x is None and (m := re.match(r"^(.*?[a-zà-ÿ])([A-Z].*)$", nome.strip())):
        x = _regra(chave(m.group(1)), ano)   # nome colado no local do jogo: "PlatenseBoca Juniors"
    return x


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
