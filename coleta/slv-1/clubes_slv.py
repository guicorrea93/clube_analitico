"""Identidade dos clubes da 1ª divisão de El Salvador: cada grafia -> nome de exibição único no mundo.

Regras (docs/agentes-internacionais-COMECE-AQUI.md, seção 4), decididas em 24/11/2026:
- nome pelo qual o clube é conhecido (FAS, Alianza FC, Águila, Luis Ángel Firpo, Isidro Metapán, Atlético Marte), com as
  grafias de cada época e as abreviações das páginas ("L.Á. Firpo", "LA Firpo", "Mun Limeno", "S Clara", "Balbao");
- o mesmo clube com outro nome: Atlético Arabe Marte (1996-98, nome do Atlético Marte depois da fusão com o Árabe; a página
  de 1997/98 diz que o da tabela é o de San Salvador) = Atlético Marte; ADET / A.D.E.T. / AD El Tránsito / Baygón ADET;
  Universidad / UES / Univ. de El Salvador = Universidad de El Salvador; Independiente / CS Independiente / Indep. Nacional /
  Nacional 1906 = Independiente de San Vicente (o clube de 1906; o de 1948/49 é presumido o mesmo); Isidro (2001) / Isidro
  Metapán (fusão de 2000 do CD Metapán com o Isidro Menéndez);
- clubes diferentes: CD Metapán (até 1991/92) e Isidro Metapán (2000 em diante); Sonsonate FC (até 1999) e CD Sonsonate (2009
  em diante); Once Municipal, Once Lobos e Once Deportivo; Juventud Olímpica, Santa Anita e Juventud Independiente;
  Quequeisque (Nueva San Salvador, até 1965) e Santa Tecla FC (2007);
- vaga comprada: Inter FA (comprou a vaga do Dragón em 2025) e Hércules (ficou com a vaga do Once Deportivo em 2025) entram
  como clubes próprios; o Hércules de 2025 é tratado como o histórico Hércules renascido (campeão de 1927 a 1929/30);
- Tapachulteca (1975): clube mexicano de Tapachula que jogou a liga salvadorenha naquele ano;
- homônimo de clube do banco ou de outro pacote leva o país ou a cidade: Hércules de El Salvador, Libertad de El Salvador,
  España de El Salvador, Atlante de El Salvador, Internacional de El Salvador, Excélsior de Santa Ana, Platense de
  Zacatecoluca, Independiente de San Vicente, Alianza de El Salvador, Leones de El Salvador, Once Deportivo de El
  Salvador, San Luis de El Salvador, Santa Clara de El Salvador, Tiburones de El Salvador (conferido com o teste de carga).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-concacaf"))
from rsssf_concacaf import chave  # noqa: E402

SS = ("San Salvador", "San Salvador")
SA = ("Santa Ana", "Santa Ana")
SM = ("San Miguel", "San Miguel")
_N = {  # nome de exibição -> (cidade, departamento)
    "FAS": SA, "Alianza de El Salvador": SS, "Águila": SM, "Luis Ángel Firpo": ("Usulután", "Usulután"),
    "Isidro Metapán": ("Metapán", "Santa Ana"), "Atlético Marte": SS, "Santa Tecla FC": ("Santa Tecla", "La Libertad"),
    "Dragón": SM, "Hércules de El Salvador": SS, "CD 33": SS, "Juventud Olímpica": SS,
    "Once Deportivo de El Salvador": ("Ahuachapán", "Ahuachapán"), "Once Municipal": ("Ahuachapán", "Ahuachapán"),
    "Quequeisque": ("Santa Tecla", "La Libertad"), "Chinameca": ("Chinameca", "San Miguel"), "Libertad de El Salvador": SS,
    "Platense de Zacatecoluca": ("Zacatecoluca", "La Paz"), "San Salvador FC": SS,
    "Santiagueño": ("Santiago de la Frontera", "Santa Ana"), "Vista Hermosa": ("San Francisco Gotera", "Morazán"),
    "Municipal Limeño": ("Santa Rosa de Lima", "La Unión"), "Chalatenango": ("Chalatenango", "Chalatenango"),
    "ADET": ("El Tránsito", "San Miguel"), "Atlético Balboa": ("La Unión", "La Unión"), "Nequepio": SS,
    "Excélsior de Santa Ana": SA, "Alacranes": SS, "Maya": SS, "Los 44": SA, "Internacional de El Salvador": SM,
    "Ferrocarril": SA, "Cuscatleco": SS, "España de El Salvador": SS, "Santa Anita": SS, "Leones de El Salvador": SS,
    "Atlante de El Salvador": SS, "Olímpic": SA, "Asturias Municipal": SS, "Adler": SS,
    "Universidad de El Salvador": SS, "UCA": ("Antiguo Cuscatlán", "La Libertad"), "Telecomunicaciones": SS,
    "Gatos de Monterrey": SS, "Sonsonate FC": ("Sonsonate", "Sonsonate"), "CD Sonsonate": ("Sonsonate", "Sonsonate"),
    "Antel": SS, "Negocios Internacionales": SS, "Agave": SS, "Acajutla": ("Acajutla", "Sonsonate"),
    "Soyapango": ("Soyapango", "San Salvador"), "Cojutepeque": ("Cojutepeque", "Cuscatlán"),
    "Tiburones de El Salvador": ("La Libertad", "La Libertad"), "Apaneca": ("Apaneca", "Ahuachapán"), "CD Metapán": ("Metapán", "Santa Ana"),
    "Fuerte San Francisco": ("San Francisco Gotera", "Morazán"), "El Roble": ("Ilobasco", "Cabañas"),
    "Once Lobos": ("Chalchuapa", "Santa Ana"), "Santa Clara de El Salvador": ("Santa Clara de El Salvador", "San Vicente"),
    "Arcense": ("Ciudad Arce", "La Libertad"), "San Luis de El Salvador": ("San Luis Talpa", "La Paz"), "Nejapa FC": ("Nejapa", "San Salvador"),
    "Juventud Independiente": ("San Juan Opico", "La Libertad"), "Independiente de San Vicente": ("San Vicente", "San Vicente"),
    "Pasaquina": ("Pasaquina", "La Unión"), "Audaz": ("Apastepeque", "San Vicente"), "El Vencedor": ("Santa Elena", "Usulután"),
    "Jocoro": ("Jocoro", "Morazán"), "Cacahuatique": ("Ciudad Barrios", "San Miguel"),
    "Zacatecoluca FC": ("Zacatecoluca", "La Paz"), "Inter FA": ("Santa Tecla", "La Libertad"),
}
CLUBES: dict[str, tuple[str, str, str]] = {k: (c, d, "SLV") for k, (c, d) in _N.items()}
CLUBES["Tapachulteca"] = ("Tapachula", "Chiapas", "MEX")

REGRAS: list[tuple[str, str, int, int]] = [
    (r"(c ?d |deportivo )?f ?a ?s", "FAS", 1940, 2100), (r"alianza( f ?c)?", "Alianza de El Salvador", 1955, 2100),
    (r"(c ?d )?aguila", "Águila", 1945, 2100), (r"(luis angel |l ?a )?firpo", "Luis Ángel Firpo", 1940, 2100),
    (r"(a ?d |c ?d )?isidro( metapan| metapan)?|isidro metap ?an", "Isidro Metapán", 2000, 2100),
    (r"((atl(etico)?|a) )?(arabe )?marte", "Atlético Marte", 1945, 2100), (r"santa tecla( f ?c)?", "Santa Tecla FC", 2005, 2100),
    (r"(c ?d )?dragon", "Dragón", 1940, 2100), (r"(c ?d )?hercules", "Hércules de El Salvador", 1920, 2100),
    (r"(c ?d )?33", "CD 33", 1930, 1945), (r"(j(uventud)? ?)?ol(impica)?|juventud", "Juventud Olímpica", 1940, 2005),
    (r"once deportivo", "Once Deportivo de El Salvador", 2015, 2100), (r"once munic?i?pal", "Once Municipal", 1940, 2100),
    (r"quequeisque", "Quequeisque", 1940, 1970), (r"chinameca( s ?c)?", "Chinameca", 1920, 1930),
    (r"(c ?d )?libertad", "Libertad de El Salvador", 1940, 1950), (r"(c ?d )?platense", "Platense de Zacatecoluca", 1970, 2100),
    (r"s(an)? salvador( f ?c)?", "San Salvador FC", 2000, 2010), (r"(c ?d )?santiagueno", "Santiagueño", 1930, 1990),
    (r"vista hermosa", "Vista Hermosa", 2000, 2015),
    (r"(c ?d )?(mun(icipal)?|m) ?limeno|limeno|municipal", "Municipal Limeño", 1970, 2100),
    (r"(a ?d |c ?d )?chalatenango", "Chalatenango", 1975, 2100),
    (r"a ?d ?e ?t|ad el transito|baygon adet", "ADET", 1980, 2005),
    (r"(atletico )?balb(o|oa|ao)", "Atlético Balboa", 2000, 2015), (r"nequepio", "Nequepio", 1920, 1930),
    (r"excelsior", "Excélsior de Santa Ana", 1920, 1980), (r"alacranes", "Alacranes", 1930, 1950),
    (r"(c ?d )?maya", "Maya", 1930, 1945), (r"los 44", "Los 44", 1930, 1945),
    (r"internacional", "Internacional de El Salvador", 1930, 1945), (r"ferrocarril", "Ferrocarril", 1930, 1955),
    (r"cuscatleco", "Cuscatleco", 1945, 1950), (r"espana", "España de El Salvador", 1945, 1950),
    (r"santa anita", "Santa Anita", 1945, 1965), (r"leones", "Leones de El Salvador", 1950, 1965), (r"atlante", "Atlante de El Salvador", 1950, 1975),
    (r"olimpic", "Olímpic", 1945, 1955), (r"asturias municipal", "Asturias Municipal", 1950, 1960), (r"adler", "Adler", 1960, 1975),
    (r"(c ?d )?(universidad( de el salvador)?|univ de el salvador|ues)", "Universidad de El Salvador", 1955, 2100), (r"uca", "UCA", 1965, 1990),
    (r"telecomunicaciones", "Telecomunicaciones", 1955, 1970), (r"gatos de monterrey", "Gatos de Monterrey", 1960, 1970),
    (r"sonsonate( f ?c)?", "Sonsonate FC", 1960, 2008), (r"(c ?d )?sonsonate", "CD Sonsonate", 2009, 2100),
    (r"antel", "Antel", 1970, 1980), (r"negocios int(ernacionales|l)", "Negocios Internacionales", 1970, 1980),
    (r"agave", "Agave", 1975, 1990), (r"acajutla", "Acajutla", 1980, 1995), (r"soyapango", "Soyapango", 1980, 1995),
    (r"cojutepeque", "Cojutepeque", 1980, 2000), (r"tiburones", "Tiburones de El Salvador", 1985, 2000), (r"apaneca", "Apaneca", 1985, 2000),
    (r"metapan", "CD Metapán", 1980, 1999), (r"fuerte (san francisco|s ?f)", "Fuerte San Francisco", 1985, 2100),
    (r"el roble", "El Roble", 1990, 2005), (r"once lobos", "Once Lobos", 1975, 2010),
    (r"s(anta)? clara", "Santa Clara de El Salvador", 1995, 2005), (r"(c ?d )?arcense", "Arcense", 2000, 2010), (r"san luis", "San Luis de El Salvador", 1995, 2005),
    (r"nejapa( f ?c)?", "Nejapa FC", 2005, 2015), (r"j(uv(entud)?)? ind(ependiente)?", "Juventud Independiente", 2005, 2020),
    (r"(c ?s )?indep(endiente)?( nacional)?|nacional 1906", "Independiente de San Vicente", 1945, 2100),
    (r"(c ?d )?pasaquina", "Pasaquina", 2010, 2025), (r"(c ?d )?audaz", "Audaz", 2015, 2025),
    (r"(c ?d )?el vencedor", "El Vencedor", 2015, 2025), (r"jocoro( f ?c)?", "Jocoro", 2015, 2100),
    (r"(c ?d )?cacahuatique", "Cacahuatique", 2020, 2100), (r"zacatecoluca( f ?c)?", "Zacatecoluca FC", 2020, 2100),
    (r"inter f ?a|internacional santa tecla", "Inter FA", 2020, 2100), (r"tapachulteca", "Tapachulteca", 1970, 1980),
]
_LIXO = re.compile(r"\[\[|\]\]")


def _regra(k: str, ano: int) -> str | None:
    for kk in (k, re.sub(r"^(club deportivo|c ?d|c ?s|a ?d|f ?c|club) ", "", k), re.sub(r" (f ?c|s ?c)$", "", k)):
        for rx, exib, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.fullmatch(f"(?:{rx})", kk):
                return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    return _regra(chave(_LIXO.sub("", re.sub(r"\s*\([^)]*\)", "", nome.strip()))), ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
