"""Identidade dos clubes da 1ª divisão de Honduras: cada grafia -> nome de exibição único no mundo.

Regras (docs/agentes-internacionais-COMECE-AQUI.md, seção 4), decididas em 24/11/2026:
- nome pelo qual o clube é conhecido (Motagua, Marathón, Real España, Platense, Vida, Victoria), com as grafias de cada fonte
  ("Marathon", "Real Espana", "España" nos anos 2000, "Real España (San Pedro Sula)");
- o mesmo clube com outro nome: La Salle (1965/66) = San Pedro (o nome mudou para 1966/67, RSSSF); Honduras (El Progreso) =
  Honduras Progreso; Juventud (2008/09) = Real Juventud; Patepluma = Real Patepluma; Valencia = Municipal Valencia;
  Atlético Olanchano / Olanchano; Dep. Savio / Savio = Deportes Savio; Comayagua = Real Comayagua; UPNFM = Lobos UPNFM;
  Atl. Choloma / Atlético Cholomeño (2011-2013);
- clubes diferentes: Atlético Olanchano (2003-2008) e Olancho FC (2022 em diante); Atlético Choloma (2011-2013) e Choloma
  (2025 em diante); Broncos e Universidad (a página escreve os dois na mesma temporada);
- homônimo de clube do banco ou de outro pacote leva a cidade ou o país: Olimpia de Tegucigalpa, Necaxa de Tegucigalpa, Real
  Sociedad de Tocoa, Palestino de Honduras, Independiente de Honduras, Progreso de Honduras, Atlético Español de Honduras, Platense de Puerto Cortés,
  San Pedro de Honduras, Atlántida de La Ceiba.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-concacaf"))
from rsssf_concacaf import chave  # noqa: E402

TGU = ("Tegucigalpa", "Francisco Morazán")
SPS = ("San Pedro Sula", "Cortés")
_H = lambda c, p: (c, p, "HON")   # noqa: E731
CLUBES: dict[str, tuple[str, str, str]] = {
    "Olimpia de Tegucigalpa": _H(*TGU), "Motagua": _H(*TGU), "Marathón": _H(*SPS), "Real España": _H(*SPS),
    "Platense de Puerto Cortés": _H("Puerto Cortés", "Cortés"), "Vida": _H("La Ceiba", "Atlántida"), "Victoria": _H("La Ceiba", "Atlántida"),
    "Universidad": _H(*TGU), "Broncos": _H("Choluteca", "Choluteca"), "Honduras Progreso": _H("El Progreso", "Yoro"),
    "Atlético Español de Honduras": _H(*TGU), "San Pedro de Honduras": _H(*SPS), "Troya": _H(*TGU), "Atlético Indio": _H(*TGU),
    "Lempira": _H(*TGU), "Progreso de Honduras": _H("El Progreso", "Yoro"), "Verdún": _H(*TGU), "Federal": _H(*TGU),
    "Atlántida de La Ceiba": _H("La Ceiba", "Atlántida"), "Campamento": _H("Campamento", "Olancho"), "Tiburones": _H("Puerto Cortés", "Cortés"),
    "Atlético Portuario": _H("Puerto Cortés", "Cortés"), "Atlético Morazán": _H(*TGU), "Independiente de Honduras": _H(*SPS),
    "Dandy": _H(*TGU), "Juventud Morazánica": _H(*TGU), "Sula": _H("La Lima", "Cortés"), "Juventud de Sula": _H(*SPS),
    "Tela Timsa": _H("Tela", "Atlántida"), "EACI": _H(*TGU), "Curaçao": _H(*TGU), "Súper Estrella": _H("Danlí", "El Paraíso"),
    "Petrotela": _H("Tela", "Atlántida"), "Real Maya": _H(*TGU), "Deportes Progreseño": _H("El Progreso", "Yoro"),
    "Palestino de Honduras": _H(*SPS), "Deportes Savio": _H("Santa Rosa de Copán", "Copán"),
    "Real Comayagua": _H("Comayagua", "Comayagua"), "Salzburg": _H("El Progreso", "Yoro"),
    "Real Patepluma": _H("Santa Bárbara", "Santa Bárbara"), "Atlético Olanchano": _H("Catacamas", "Olancho"),
    "Municipal Valencia": _H(*TGU), "Hispano": _H("Comayagua", "Comayagua"), "Real Juventud": _H("Santa Bárbara", "Santa Bárbara"),
    "Necaxa de Tegucigalpa": _H(*TGU), "Atlético Choloma": _H("Choloma", "Cortés"), "Real Sociedad de Tocoa": _H("Tocoa", "Colón"),
    "Parrillas One": _H(*SPS), "Juticalpa": _H("Juticalpa", "Olancho"), "Social Sol": _H("Olanchito", "Yoro"),
    "Lobos UPNFM": _H(*TGU), "Real de Minas": _H(*TGU), "Olancho FC": _H("Juticalpa", "Olancho"),
    "Génesis": _H("Comayagua", "Comayagua"), "Choloma": _H("Choloma", "Cortés"),
}

REGRAS: list[tuple[str, str, int, int]] = [
    (r"olimpia", "Olimpia de Tegucigalpa", 1960, 2100), (r"motagua", "Motagua", 1960, 2100),
    (r"marath(o|ó)n", "Marathón", 1960, 2100), (r"(real )?espa(n|ñ)a", "Real España", 1960, 2100),
    (r"platense", "Platense de Puerto Cortés", 1960, 2100), (r"vida( ceiba| la ceiba)?", "Vida", 1960, 2100),
    (r"victoria( ceiba| la ceiba)?", "Victoria", 1960, 2100), (r"universidad( choluteca)?|unah", "Universidad", 1960, 2100),
    (r"broncos( unah)?", "Broncos", 1960, 2100), (r"honduras( el progreso| p| progreso)?", "Honduras Progreso", 1960, 2100),
    (r"atletico espanol", "Atlético Español de Honduras", 1960, 1980), (r"la salle|san pedro", "San Pedro de Honduras", 1960, 1975),
    (r"troya", "Troya", 1960, 1980), (r"atletico indio", "Atlético Indio", 1960, 2000), (r"lempira", "Lempira", 1960, 1980),
    (r"progreso", "Progreso de Honduras", 1960, 1980), (r"verdun", "Verdún", 1960, 1980), (r"federal", "Federal", 1960, 2100),
    (r"atlantida", "Atlántida de La Ceiba", 1970, 1985), (r"campamento", "Campamento", 1970, 1985), (r"tiburones", "Tiburones", 1970, 1985),
    (r"atletico portuario", "Atlético Portuario", 1970, 1990), (r"atletico morazan", "Atlético Morazán", 1975, 1990),
    (r"independiente", "Independiente de Honduras", 1975, 2000), (r"dandy", "Dandy", 1975, 1990),
    (r"juventud morazanica", "Juventud Morazánica", 1980, 1990), (r"sula", "Sula", 1980, 1995),
    (r"juventud de sula", "Juventud de Sula", 1980, 1990), (r"tela timsa", "Tela Timsa", 1980, 1995),
    (r"e ?a ?c ?i", "EACI", 1980, 1990), (r"curacao", "Curaçao", 1985, 1995), (r"super estrella", "Súper Estrella", 1985, 1995),
    (r"petrotela", "Petrotela", 1985, 1995), (r"real maya", "Real Maya", 1990, 2005),
    (r"deportes progresen?o", "Deportes Progreseño", 1990, 2000), (r"palestino", "Palestino de Honduras", 1995, 2000),
    (r"(dep(ortes)? )?savio( santa rosa de copan)?", "Deportes Savio", 1995, 2100),
    (r"(real )?comayagua", "Real Comayagua", 1995, 2005), (r"salzburg( el progreso)?", "Salzburg", 2000, 2005),
    (r"(real )?patepluma( santa barbara| sta barbara)?", "Real Patepluma", 2000, 2005),
    (r"(atletico )?olan(d)?chano( catacamas)?", "Atlético Olanchano", 2000, 2010),
    (r"(municipal )?valencia( tegucigalpa)?", "Municipal Valencia", 2000, 2010), (r"hispano( comayagua)?", "Hispano", 2000, 2015),
    (r"(real )?juventud( santa barbara)?", "Real Juventud", 2005, 2012), (r"necaxa( tegucigalpa)?", "Necaxa de Tegucigalpa", 2005, 2015),
    (r"atl(etico)? cholome?(n|ñ)?o( choloma)?|atl choloma|choloma", "Atlético Choloma", 2010, 2015),
    (r"real sociedad( tocoa)?", "Real Sociedad de Tocoa", 2010, 2100), (r"parrillas one( san pedro sula)?", "Parrillas One", 2010, 2020),
    (r"juticalpa( juticalpa)?", "Juticalpa", 2010, 2100), (r"social sol( olanchito)?", "Social Sol", 2010, 2100),
    (r"(lobos )?upnfm( tegucigalpa)?", "Lobos UPNFM", 2015, 2100), (r"real de minas( tegucigalpa)?", "Real de Minas", 2015, 2100),
    (r"olancho( fc)?( juticalpa)?", "Olancho FC", 2020, 2100), (r"genesis( comayagua)?", "Génesis", 2020, 2100),
    (r"choloma( choloma)?", "Choloma", 2020, 2100),
]

_LIXO = re.compile(r"\s*\([^)]*\)|\[\[|\]\]")   # cidade entre parênteses: "Marathón (San Pedro Sula)"


def _regra(k: str, ano: int) -> str | None:
    # ESPN: "Club Deportivo Olimpia", "FC Motagua", "C.D.Real Sociedad", "Juticalpa FC", "Génesis PN"
    k = re.sub(r" (fc|pn|cd)$", "", re.sub(r"^(club deportivo|c ?d|fc|club|cdys|cds) ", "", k))
    for rx, exib, a0, a1 in REGRAS:
        if a0 <= ano <= a1 and re.fullmatch(f"(?:{rx})", k):
            return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    return _regra(chave(_LIXO.sub("", nome.strip())), ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
