"""Edições da 1ª divisão do Canadá (can-1): as três ligas profissionais nacionais que a RSSSF junta como o topo do futebol
canadense (tablesc/canchamp.html, "CPSL/CSL 1983-1992 and CPL since 2019"). Escopo decidido em 25/11/2026 (ok do Guilherme):

- 1983: Canadian Professional Soccer League (uma temporada, abandonada no meio; o título saiu nos playoffs);
- 1987 a 1992: Canadian Soccer League (a página de Dave Litterer, usadave/csl.html, só tem as tabelas e os playoffs);
- 2019 em diante: Canadian Premier League (a liga atual, 1ª divisão sancionada pela Canada Soccer).

Ficam fora a National Soccer League (1922-1997) e as ligas que a seguiram (CPSL/CSL, 1998-2025), de clubes quase só da região
de Toronto (regionais, como a Liga Capitalina da Guatemala); o Canadian Championship (copa, fase 2: can-copa); e os clubes
canadenses da MLS (já no usa-1).

Fontes de cada edição: 1983 a página da CPSL (usadave/cpsl.html); 1987-1992 a do CSL; 2019-2024 a seção "Canadian Premier
League" da página do ano (tablesc/canAAAA.html); 2025 a página (tabela e playoffs) mais a fase regular do ogol (a RSSSF não
tem os jogos); 2026 só o ogol (a RSSSF ainda não tem a página).
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "can-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

FIM_PADRAO = (r"^(Prince Edward Island|Quebec Province|Exhibition Matches|list of champions|canada - list of champions|"
              r"About this document)")


@dataclass
class Edicao:
    temporada: str
    ano_inicio: int
    ano_fim: int
    trechos: list[tuple[str, int, int | None]]
    nome_oficial: str
    campeao_rsssf: str = ""
    obs: str = ""
    fases: list[tuple[str, str]] = field(default_factory=list)
    nomes: dict[str, str] = field(default_factory=dict)
    soma_de: list[str] = field(default_factory=list)
    wiki: str | None = None
    hist: str = ""
    ogol: int | None = None
    espn: tuple[str, str] | None = None
    espn_fases: list[tuple[str, str]] = field(default_factory=list)
    tabelas: list[tuple[str, int, int | None]] = field(default_factory=list)
    parcial: tuple[str, int, int] | None = None
    incompleta: str = ""
    sem_campeao: str = ""
    liga: str = ""
    pontos_fora: str = ""

    @property
    def pontos_vitoria(self) -> int:
        """Pela própria tabela publicada (2 ou 3 por vitória: o que fecha com mais linhas); sem tabela, 3 a partir de 1995."""
        return _pv(self.temporada, tuple(self.trechos or self.tabelas), self.ano_inicio)

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.wiki is None and self.espn is None and self.ogol is None


def _e(temporada, ini, fim, trechos, nome, campeao="", obs="", **kw):
    return Edicao(temporada, ini, fim, trechos, nome, campeao, obs, **kw)


def _rsssf():
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-concacaf"))
    import rsssf_concacaf
    return rsssf_concacaf


@lru_cache(maxsize=None)
def _texto(pagina: str) -> tuple[str, ...]:
    return tuple(l.replace("–", "-") for l in _rsssf().texto(PASTA_DADOS / "rsssf" / f"{pagina}.html"))


@lru_cache(maxsize=None)
def _pv(temporada: str, trechos: tuple, ano: int) -> int:
    r = _rsssf()
    dois = tres = 0
    for pagina, ini, fim in trechos:
        for l in _texto(pagina)[ini:fim]:
            t = r.linha_tabela(l)
            if t and t["v"] + t["e"] > 0:
                dois += t["pts"] == 2 * t["v"] + t["e"]
                tres += t["pts"] == 3 * t["v"] + t["e"]
    if dois == tres:
        return 3 if ano >= 1995 else 2
    return 3 if tres > dois else 2


def _linha(pagina: str, rx: str, depois: int = 0) -> int:
    ls = _texto(pagina)
    for i in range(depois, len(ls)):
        if re.fullmatch(rx, ls[i].strip(), re.I):
            return i
    raise ValueError(f"{pagina}: título {rx!r} não achado")


def _fim(pagina: str, ini: int, rx: str = FIM_PADRAO) -> int:
    ls = _texto(pagina)
    return next((i for i in range(ini + 3, len(ls)) if re.match(rx, ls[i].strip(), re.I)), len(ls))


def _tem_jogos(pagina: str, ini: int, fim: int) -> bool:
    r = _rsssf()
    ls = _texto(pagina)[ini:fim]
    jogos = sum(1 for l in ls if r._jogo(l))
    tab, esperado = False, 0
    for l in ls:
        t = r.linha_tabela(l)
        if t:
            esperado += t["j"]
            tab = True
        elif tab and l.strip() and not re.match(r"^[-=\s]+$", l.strip()):
            break
    if esperado == 0:
        return jogos >= 60
    return jogos >= 0.9 * esperado / 2


def _da_pagina(t, a0, a1, pagina, ini=0, fim=None, nome="", **kw) -> Edicao:
    fim = fim if fim is not None else _fim(pagina, ini)
    if _tem_jogos(pagina, ini, fim):
        return _e(t, a0, a1, [(pagina, ini, fim)], nome, **kw)
    obs = "só a tabela: a página da RSSSF não tem os jogos da fase regular (os da fase final ficam de fora)"
    return _e(t, a0, a1, [], nome, tabelas=[(pagina, ini, fim)], obs="; ".join(x for x in (kw.pop("obs", ""), obs) if x), **kw)


@lru_cache(maxsize=None)
def lista() -> tuple[tuple[str, str, str], ...]:
    """canchamp.html, só o bloco "CPSL/CSL 1983-1992 and CPL since 2019": (temporada, campeão, vice). A CPL 2026 (final de
    21/11/2026, Cavalry 3-2 Atlético Ottawa) ainda não está na lista: entra à mão, com o ogol e a imprensa (TSN, CBC)."""
    saida, dentro = [], False
    for l in _texto("canchamp"):
        s = l.strip()
        if s.startswith("CPSL/CSL 1983-1992"):
            dentro = True
            continue
        if s.startswith("NSL/CPSL/CSL since"):
            break
        if not dentro:
            continue
        m = re.match(r"^(\d{4})\s+(\S.*?)\s*$", l)
        if not m:
            continue
        corpo = re.sub(r"\s*\[.*$", "", m.group(2))
        mm = re.match(r"^(\S.*?)\s{2,}(?:(?:\d{1,2}-\d{1,2}\s+)*)(\S.*)$", corpo)
        camp, vice = (mm.group(1), mm.group(2)) if mm else (corpo, "")
        saida.append((m.group(1), camp.strip(), vice.strip()))
    if not any(t == "2026" for t, _, _ in saida):
        saida.append(("2026", "Cavalry FC", "Atlético Ottawa"))
    return tuple(saida)


def _secao_csl(ano: int) -> tuple[int, int]:
    ls = _texto("csl")
    i = next(k for k, l in enumerate(ls) if l.strip() == str(ano))
    f = next((k for k in range(i + 1, len(ls)) if re.fullmatch(r"\d{4}", ls[k].strip()) or ls[k].strip() == "About this document"),
             len(ls))
    return i, f


def _secao_cpl(pg: str) -> tuple[int, int]:
    """A seção da CPL na página do ano: o segundo título "Canadian Premier League AAAA" (o primeiro é o índice do alto; na
    página de 2025 o título diz 2024, erro da página) até o próximo título de seção."""
    ls = _texto(pg)
    tits = [k for k, l in enumerate(ls) if re.fullmatch(r"Canadian Premier League \d{4}", l.strip())]
    i = tits[1] if len(tits) > 1 else tits[0]
    return i, _fim(pg, i)


EDICOES: list[Edicao] = []
_OGOL = {2019: 132008, 2020: 143069, 2021: 156253, 2022: 162357, 2023: 171866, 2024: 182704, 2025: 195235, 2026: 213365}

for _t, _c, _v in lista():
    _a = int(_t)
    if _a == 1983:
        _i = _linha("cpsl", r"Canadian Professional Soccer League 1983")
        EDICOES.append(_e(_t, _a, _a, [("cpsl", _i, _fim("cpsl", _i))], "Canadian Professional Soccer League 1983",
                          incompleta="temporada abandonada no meio (dois dos seis clubes desistiram); a tabela é a do momento da "
                                     "parada e o título saiu nos playoffs"))
    elif _a <= 1992:
        _i, _f = _secao_csl(_a)
        EDICOES.append(_e(_t, _a, _a, [("csl", _i, _f)], f"Canadian Soccer League {_a}",
                          incompleta="só os jogos dos playoffs: a fase regular só com a tabela (a página não tem os jogos)"))
    elif _a <= 2024:
        _pg = f"can{_a}"
        _i, _f = _secao_cpl(_pg)
        EDICOES.append(_e(_t, _a, _a, [(_pg, _i, _f)], f"Canadian Premier League {_a}"))
    elif _a == 2025:
        _i, _f = _secao_cpl("can2025")
        EDICOES.append(_e(_t, _a, _a, [("can2025", _i, _f)], "Canadian Premier League 2025", ogol=_OGOL[2025],
                          obs="fase regular do ogol (a página da RSSSF só tem a tabela e os playoffs)"))
    else:
        EDICOES.append(_e(_t, _a, _a, [], f"Canadian Premier League {_a}", ogol=_OGOL[_a],
                          obs="só o ogol (a RSSSF ainda não tem a página de 2026); campeão e vice também na imprensa (TSN, CBC)"))
