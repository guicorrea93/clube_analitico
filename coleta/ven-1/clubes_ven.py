"""Identidade dos clubes venezuelanos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido ("Caracas FC", "Deportivo Táchira", "Estudiantes de Mérida", "Zamora FC");
- o mesmo clube com outro nome, como na lista de campeões da RSSSF (venezchamp.html): Unión Atlético Táchira (fusão de 1985
  com o Atlético San Cristóbal, até 1999) é o Deportivo Táchira; ItalChacao (fusão temporária com o Deportivo Chacao) e
  Deportivo Petare (2010-2016) são o Deportivo Italia; o Atlético Zulia (1996/97 e 1997/98) é a Universidad de Los Andes
  levada a Maracaibo e que voltou a Mérida como FCU-ULA (a página de 1996/97 diz que era o Unicol; fica a lista de campeões,
  que conta o título de 1997/98 assim); o Internacional de Lara (1998/99) é o Trujillanos levado a Barquisimeto;
- renomeações na mesma cidade, como nas notas das páginas: UE Lara -> UD Lara (1986/87); Nacional -> Pampero (1948);
  Internacional El Vigía -> El Vigía FC (1999/00); Hermanos Colmenárez -> Internacional de Barinas (2024);
- clubes diferentes, mesmo com licença comprada ou nome parecido: Nacional Táchira ("novo nome da UD Lara", 1996/97, mas em
  outra cidade: fica separado); Atlético Monagas e Monagas SC ("different from", 2000/01); Atlético Zamora (até 2005) e
  Zamora FC; Lara FC (1965-1985), Unión Deportiva Lara (1986-2002) e Deportivo Lara (2009 em diante); Anzoátegui FC (1967),
  Atlético Anzoátegui (1986-1990), Deportivo Anzoátegui (2007 em diante) e Anzoátegui FC (2025); Estudiantes de Caracas
  (era amadora) e Estudiantes de Caracas SC (2015-2019); San Cristóbal FC (1994/95) e Atlético San Cristóbal (1980-1985);
  Aragua FC de 1966-1975 ("Aragua FC (1966)") e o de 2002;
- homônimo de clube do banco ou de outro pacote leva a cidade (Deportivo Español de Caracas, Celta de Caracas, Danubio de
  Caracas, América de Caracas, Universidad Católica de Caracas; conferido com o banco e os outros pacotes).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-sulamerica"))
from rsssf_sul import chave  # noqa: E402

CCS = ("Caracas", "Distrito Capital")

# nome de exibição -> (cidade, estado)
CLUBES: dict[str, tuple[str, str]] = {
    # era amadora (Caracas, salvo indicação)
    "América de Caracas": CCS, "Centro Atlético": CCS, "Vargas": ("La Guaira", "Vargas"), "Loyola": CCS, "Venzóleo": CCS,
    "Deportivo Venezuela": CCS, "Unión SC": CCS, "Dos Caminos": CCS, "Litoral": ("La Guaira", "Vargas"),
    "Deportivo Español de Caracas": CCS, "La Salle": CCS, "Deportivo Vasco": CCS, "Banco Obrero": CCS, "Atenas": CCS,
    "Deutscher SV": CCS, "Nueva Esparta": CCS, "Centro Alemán": ("Puerto Cabello", "Carabobo"), "Deportivo España": CCS,
    "Kadima": CCS, "Pampero": CCS, "Universidad Central": CCS, "Catalonia": CCS, "Hispano": CCS, "Nuevos del Este": CCS,
    "Deportivo Universitario": CCS,
    # Caracas e arredores
    "Deportivo Portugués": CCS, "Deportivo Italia": CCS, "Deportivo Galicia": CCS, "Celta de Caracas": CCS,
    "Danubio de Caracas": CCS, "Banco Agrícola y Pecuario": CCS, "Banco Francés-Italiano": CCS,
    "Universidad Católica de Caracas": CCS, "Unión Deportiva Canarias": CCS, "Tiquire Flores": ("Maracay", "Aragua"),
    "Tiquire Aragua": ("Maracay", "Aragua"), "Tiquire-Canarias": CCS, "Miranda-Canarias": CCS, "Nacional FC": CCS,
    "Caracas FC": CCS, "CS Marítimo": CCS, "Deportivo Chacao": CCS, "Atlético Venezuela": CCS, "Metropolitanos": CCS,
    "Deportivo La Guaira": CCS, "Estudiantes de Caracas": CCS, "Estudiantes de Caracas SC": CCS, "SD Centro Ítalo": CCS, "Real Esppor": CCS,
    "Hermanos Colmenárez": ("Barinas", "Barinas"),
    # Andes
    "Deportivo Táchira": ("San Cristóbal", "Táchira"), "Atlético San Cristóbal": ("San Cristóbal", "Táchira"),
    "Nacional Táchira": ("San Cristóbal", "Táchira"), "Estudiantes de Mérida": ("Mérida", "Mérida"),
    "Universidad de Los Andes": ("Mérida", "Mérida"), "Trujillanos": ("Valera", "Trujillo"),
    "El Vigía FC": ("El Vigía", "Mérida"), "Atlético El Vigía": ("El Vigía", "Mérida"),
    "Unión Atlético El Vigía": ("El Vigía", "Mérida"), "Ureña SC": ("Ureña", "Táchira"),
    "Atlético Socopó": ("Socopó", "Barinas"),
    # centro-ocidente
    "Portuguesa FC": ("Acarigua", "Portuguesa"), "Lara FC": ("Barquisimeto", "Lara"), "Unión Deportiva Lara": ("Barquisimeto", "Lara"),
    "Deportivo Lara": ("Barquisimeto", "Lara"),
    "Unión Lara": ("Barquisimeto", "Lara"), "Guaros de Lara": ("Barquisimeto", "Lara"), "Barquisimeto FC": ("Barquisimeto", "Lara"),
    "Llaneros de Guanare": ("Guanare", "Portuguesa"), "Atlético Zamora": ("Barinas", "Barinas"), "Zamora FC": ("Barinas", "Barinas"),
    "Yaracuyanos": ("San Felipe", "Yaracuy"),
    "Valencia FC": ("Valencia", "Carabobo"), "Carabobo FC": ("Valencia", "Carabobo"), "Deportivo Carabobo": ("Valencia", "Carabobo"),
    "Nacional Carabobo": ("Valencia", "Carabobo"), "Academia Puerto Cabello": ("Puerto Cabello", "Carabobo"),
    "Aragua FC": ("Maracay", "Aragua"), "Aragua FC (1966)": ("Maracay", "Aragua"), "Saman de Aragua": ("Maracay", "Aragua"),
    "GV Maracay": ("Maracay", "Aragua"), "Arroceros de Calabozo": ("Calabozo", "Guárico"), "Deportivo Tuy": ("Ocumare del Tuy", "Miranda"),
    "Atlético Falcón": ("Coro", "Falcón"), "Falcón FC": ("Coro", "Falcón"), "LALA FC": ("Guanare", "Portuguesa"),
    # Zulia
    "Zulia FC": ("Maracaibo", "Zulia"), "Unión Atlético Maracaibo": ("Maracaibo", "Zulia"), "Maracaibo FC": ("Maracaibo", "Zulia"),
    "Petroleros del Zulia": ("Maracaibo", "Zulia"), "Unicol": ("Lagunillas", "Zulia"), "Zulianos": ("Maracaibo", "Zulia"),
    "Deportivo ItalMaracaibo": ("Maracaibo", "Zulia"), "Deportivo JBL Zulia": ("Maracaibo", "Zulia"),
    "Deportivo Rayo Zuliano": ("Maracaibo", "Zulia"),
    # oriente e Guayana
    "Mineros de Guayana": ("Puerto Ordaz", "Bolívar"), "Minervén": ("El Callao", "Bolívar"),
    "Industriales del Caroní": ("Ciudad Guayana", "Bolívar"), "Caroní FC": ("Ciudad Guayana", "Bolívar"),
    "Angostura FC": ("Ciudad Bolívar", "Bolívar"), "Monagas SC": ("Maturín", "Monagas"), "Atlético Monagas": ("Maturín", "Monagas"),
    "Anzoátegui FC (1967)": ("Puerto La Cruz", "Anzoátegui"), "Anzoátegui FC": ("Puerto La Cruz", "Anzoátegui"),
    "Internacional de Puerto La Cruz": ("Puerto La Cruz", "Anzoátegui"), "San Cristóbal FC": ("San Cristóbal", "Táchira"), "Atlético Anzoátegui": ("Puerto La Cruz", "Anzoátegui"),
    "Deportivo Anzoátegui": ("Puerto La Cruz", "Anzoátegui"), "Universitarios de Oriente": ("Cumaná", "Sucre"),
    "Marinos de Sucre": ("Cumaná", "Sucre"), "Salineros de Araya": ("Araya", "Sucre"), "Peninsulares de Araya": ("Araya", "Sucre"),
    "Pepeganga Margarita": ("Porlamar", "Nueva Esparta"), "Nueva Cádiz": ("Cumaná", "Sucre"),
    "Estrella Roja": ("Puerto Ordaz", "Bolívar"), "Tucanes de Amazonas": ("Puerto Ayacucho", "Amazonas"),
}

REGRAS: list[tuple[str, str, int, int]] = [
    # Táchira
    (r"(union atletico|ua|ud|u a|atl) tachira( fc)?|union tachira", "Deportivo Táchira", 1985, 1999),
    (r"(deportivo|dep|dvo) (tachira|san cristobal)|tachira$", "Deportivo Táchira", 1974, 2100),
    (r"atletico san cristobal|san cristobal( fc)?$", "Atlético San Cristóbal", 1980, 1985),
    (r"san cristobal( fc)?", "San Cristóbal FC", 1990, 2000),
    (r"nacional tachira|nacional$", "Nacional Táchira", 1996, 2003),
    # Caracas
    (r"(dep(ortivo)? |dvo )?ital ?chacao( fc)?", "Deportivo Italia", 1998, 2007),
    (r"(dep(ortivo)? |dvo )?italia( fc| caracas)?$|italia$|(dep(ortivo)? |dvo )?petare( fc)?", "Deportivo Italia", 1950, 2100),
    (r"(dep(ortivo)? )?chacao", "Deportivo Chacao", 1990, 2100),
    (r"(dep(ortivo)? )?galicia( fc| de caracas)?|galicia", "Deportivo Galicia", 1950, 2100),
    (r"(dep(ortivo)? )?portugu[eé]s", "Deportivo Portugués", 1950, 2100),
    (r"caracas( fc)?|carcaas fc|fc caracas", "Caracas FC", 1967, 2100),
    (r"(cs )?maritimo( fc)?", "CS Marítimo", 1959, 2100),
    (r"universidad central|univ central|ucv( fc)?|universidad( fc)?$", "Universidad Central", 1947, 2100),
    (r"universidad catolica", "Universidad Católica de Caracas", 1950, 2100),
    (r"(b(anco)?\.? )?agric(ola)?\.? y? ?pecuar(io)?|banco agric pecuar", "Banco Agrícola y Pecuario", 1950, 2100),
    (r"banco frances italiano", "Banco Francés-Italiano", 1950, 2100),
    (r"banco obrero", "Banco Obrero", 1950, 2100),
    (r"(ud|union deportiv[oa]) canarias", "Unión Deportiva Canarias", 1960, 2100),
    (r"tiquire flores", "Tiquire Flores", 1950, 2100),
    (r"tiquire aragua", "Tiquire Aragua", 1950, 2100),
    (r"tiquire canarias", "Tiquire-Canarias", 1950, 2100),
    (r"miranda canarias", "Miranda-Canarias", 1950, 2100),
    (r"nacional fc|nacional$", "Nacional FC", 1960, 1970),
    (r"celta", "Celta de Caracas", 1950, 2100),
    (r"danubio", "Danubio de Caracas", 1950, 2100),
    (r"catalonia( fc)?", "Catalonia", 1950, 2100),
    (r"hispano", "Hispano", 1950, 2100),
    (r"nuevos del este", "Nuevos del Este", 1950, 2100),
    (r"(at(l(etico)?)? )?venezuela$|atletico venezuela", "Atlético Venezuela", 2000, 2100),
    (r"metropolitanos( fc)?", "Metropolitanos", 2000, 2100),
    (r"(dep(ortivo)? |dvo )?la guaira", "Deportivo La Guaira", 2000, 2100),
    (r"estudiantes (sc|de caracas)", "Estudiantes de Caracas SC", 2010, 2100),
    (r"estudiantes( fc| sc)?", "Estudiantes de Caracas", 1900, 1959),
    (r"(sd )?centro italo( fc)?", "SD Centro Ítalo", 2000, 2100),
    (r"(real )?(atletico )?espp?or( club)?", "Real Esppor", 2000, 2100),
    (r"hermanos colmenarez|inter(nacional)?( de)? barinas", "Hermanos Colmenárez", 2000, 2100),
    # amadores
    (r"america", "América de Caracas", 1900, 1950),
    (r"centro atletico( sc| caracas)?", "Centro Atlético", 1900, 2100),
    (r"vargas", "Vargas", 1900, 1950),
    (r"loyola( sc)?", "Loyola", 1900, 2100),
    (r"(cf )?venzoleo", "Venzóleo", 1900, 2100),
    (r"(dep(ortivo)? )?venezuela?$|deportivo venezuel", "Deportivo Venezuela", 1900, 1960),
    (r"union( sc)?$", "Unión SC", 1900, 1960),
    (r"dos caminos( sc)?", "Dos Caminos", 1900, 2100),
    (r"litoral( sc| fc)?", "Litoral", 1900, 1970),
    (r"(deportivo )?espanol", "Deportivo Español de Caracas", 1900, 2100),
    (r"deportivo espa(n)?a", "Deportivo España", 1900, 2100),
    (r"la salle( fc| sc)?", "La Salle", 1900, 2100),
    (r"deportivo vasco", "Deportivo Vasco", 1900, 2100),
    (r"atenas( fbc)?", "Atenas", 1900, 1960),
    (r"deutscher sv", "Deutscher SV", 1900, 1960),
    (r"nueva esparta( fbc)?", "Nueva Esparta", 1900, 1960),
    (r"centro aleman", "Centro Alemán", 1900, 1960),
    (r"(cd )?kadima", "Kadima", 1900, 1960),
    (r"nacional", "Pampero", 1940, 1950),   # 1948: "Nacional renamed Pampero FC"
    (r"pampero( fc)?", "Pampero", 1900, 1960),
    (r"(dep(ortivo)? )?universitario", "Deportivo Universitario", 1900, 1960),
    # Andes
    (r"estudiantes( de)? merida( fc)?|estudiantes merida|estudiantes( fc)?$", "Estudiantes de Mérida", 1960, 2100),
    (r"(atletico )?zulia$", "Universidad de Los Andes", 1996, 1997),
    (r"(fcu )?ula( fc| merida)?|univ(ersidad)?( de)? los andes", "Universidad de Los Andes", 1970, 2100),
    (r"trujillanos( fc| valera)?|(cd |deportivo )trujillanos|inter(nacional)?( de)? lara", "Trujillanos", 1980, 2100),
    (r"el vigia( fc| el vigia)?$|el vigia fc|vigia$|inter(nacional)?( el vigia)?$", "El Vigía FC", 1990, 2002),
    (r"union atletico el vigia( fc)?", "Unión Atlético El Vigía", 2002, 2006),
    (r"(fundacion )?(at(l(etico)?)? )(el )?vigia( fc)?", "Atlético El Vigía", 2006, 2100),
    (r"urena( sc)?", "Ureña SC", 2000, 2100),
    (r"atletico socopo( fc)?", "Atlético Socopó", 2000, 2100),
    # centro-ocidente
    (r"portuguesa( fc)?", "Portuguesa FC", 1970, 2100),
    (r"lara fc( barquisimeto)?", "Lara FC", 1960, 1985),
    (r"lara$", "Lara FC", 1960, 1985),
    (r"ud lara|union deportiva( de)? lara|lara$|ue lara|union espanola de lara", "Unión Deportiva Lara", 1980, 2002),
    (r"(cd |club deportivo |deportivo )lara", "Deportivo Lara", 2009, 2100),
    (r"deportivo lara", "Lara FC", 1970, 1985),   # 1978: a tabela e quase todos os jogos chamam o Lara FC de "Deportivo Lara"
    (r"union lara( fc)?", "Unión Lara", 2000, 2100),
    (r"guaros de lara( fc)?", "Guaros de Lara", 2000, 2100),
    (r"barquisimeto fc", "Barquisimeto FC", 1970, 1985),
    (r"llaneros( de)?( guanare)?( fc| dfc)?|llaneros fc", "Llaneros de Guanare", 1980, 2100),
    (r"(atl(etico)? )?zamora", "Atlético Zamora", 1975, 2005),
    (r"atletico zamora", "Zamora FC", 2006, 2100),
    (r"zamora( fc)?", "Zamora FC", 2006, 2100),
    (r"yaracuyanos( fc)?", "Yaracuyanos", 2000, 2100),
    (r"valencia( fc)?( valencia)?", "Valencia FC", 1960, 2000),
    (r"carabobo( fc)?", "Carabobo FC", 1995, 2100),
    (r"deportivo carabobo", "Deportivo Carabobo", 1970, 1990),
    (r"nacional carabobo", "Nacional Carabobo", 1970, 1990),
    (r"academia (pc|puerto cabello)", "Academia Puerto Cabello", 2000, 2100),
    (r"aragua fc( maracay)?", "Aragua FC (1966)", 1960, 1975),
    (r"(ua )?aragua( fc)?", "Aragua FC", 2000, 2100),
    (r"saman( de aragua)?", "Saman de Aragua", 1980, 2100),
    (r"gv maracay|gran valencia( maracay)?", "GV Maracay", 2000, 2100),
    (r"arroceros de calabozo( fc)?", "Arroceros de Calabozo", 1980, 2100),
    (r"(dep(ortivo)? )?tuy", "Deportivo Tuy", 1980, 2100),
    (r"atletico falcon", "Atlético Falcón", 1970, 2100),
    (r"falcon fc", "Falcón FC", 1970, 2100),
    (r"lala fc", "LALA FC", 2000, 2100),
    # Zulia
    (r"zulia fc|zulia$", "Zulia FC", 1960, 2100),
    (r"(union atletico|ua) maracaibo", "Unión Atlético Maracaibo", 2000, 2100),
    (r"maracaibo( fc)?", "Maracaibo FC", 1980, 2000),
    (r"petroleros de(l)? zulia", "Petroleros del Zulia", 1970, 2100),
    (r"unicol( fc| lagunillas)?", "Unicol", 1980, 2100),
    (r"zulianos( fc)?", "Zulianos", 1990, 2100),
    (r"(deportivo )?italmaracaibo", "Deportivo ItalMaracaibo", 2000, 2100),
    (r"(dep(ortivo)? )?jbl zulia", "Deportivo JBL Zulia", 2000, 2100),
    (r"(deportivo )?rayo zuliano", "Deportivo Rayo Zuliano", 2000, 2100),
    # oriente e Guayana
    (r"(ac |ad )?mineros( de| del)?( guayana| guyana| puerto ordaz)?( fc)?", "Mineros de Guayana", 1980, 2100),
    (r"(ac )?minerven( fc)?( bolivar| del callao| el callao)?", "Minervén", 1980, 2100),
    (r"industriales( del caroni)?", "Industriales del Caroní", 1980, 2100),
    (r"caroni( fc)?", "Caroní FC", 2000, 2100),
    (r"angostura fc( sc)?", "Angostura FC", 2000, 2100),
    (r"monagas( sc| sport club)?", "Monagas SC", 1980, 2100),
    (r"atl(etico)? monagas", "Atlético Monagas", 1990, 2100),   # 2000/01: "different from Monagas SC" (RSSSF)
    (r"anzoategui( fc| puerto la cruz)?$|anzoategui fc", "Anzoátegui FC (1967)", 1960, 1996),
    (r"atl(etico)?\.? anzoategui|(deportivo|dep|dvo) anzoategui", "Atlético Anzoátegui", 1986, 1990),
    (r"anzoategui fc", "Anzoátegui FC", 2020, 2100),
    (r"internacional( plc| puerto la cruz)?", "Internacional de Puerto La Cruz", 1989, 1989),
    (r"(deportivo|dep|dvo) anzoategui( sc| fc)?", "Deportivo Anzoátegui", 2000, 2100),
    (r"universit(arios|os) de oriente", "Universitarios de Oriente", 1970, 2100),
    (r"marinos( de sucre)?", "Marinos de Sucre", 1980, 2100),
    (r"salineros de araya", "Salineros de Araya", 1980, 2100),
    (r"peninsulares de araya", "Peninsulares de Araya", 1980, 2100),
    (r"pepeganga margarita", "Pepeganga Margarita", 1980, 2100),
    (r"nueva cadiz( fc)?", "Nueva Cádiz", 1980, 2100),
    (r"estrella roja( fc)?", "Estrella Roja", 2000, 2100),
    (r"tucanes( de amazonas)?( fc)?", "Tucanes de Amazonas", 2000, 2100),
]

_LIXO = re.compile(r"^\s*[-/]\s*|\s*-\s*$|\[\[|\]\]", re.I)


def _regra(k: str, ano: int) -> str | None:
    for kk in (k, re.sub(r"^(club|c|cd|csd|ac|ad|cs) ", "", k)):
        for rx, exib, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.fullmatch(f"(?:{rx})" + r"(?:\s.*)?", kk):
                return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    nome = re.sub(r"\b((?:[A-Z]\.){2,})", lambda m: m.group(1).replace(".", ""), nome)   # "A.C. Mineros", "U.A. Maracaibo"
    return _regra(chave(_LIXO.sub("", nome.strip())), ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
