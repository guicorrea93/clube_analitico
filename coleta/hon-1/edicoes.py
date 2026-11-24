"""Edições da 1ª divisão de Honduras (hon-1): a Liga Nacional, uma edição por título, como na lista de campeões da RSSSF
(tablesh/hondchamp.html). Escopo decidido em 24/11/2026 (pesquisa a pedido do Guilherme):

- 1965/66 a 1996/97, um campeão por temporada (rótulos da RSSSF: "1965/66", "1973", "1978/79"...). 1972/73 foi abandonada:
  entra sem campeão, com a tabela do momento.
- 1997/98: Apertura e Clausura ("1997 Apertura", "1998 Clausura"); 1999: torneio único de transição ("1999"); de 1999/00 em
  diante, Apertura e Clausura ("1999 Apertura", "2000 Clausura"), até o Clausura 2026. O Clausura 2020 (pandemia) entra sem
  campeão.
- Fora: a Liga Amateur de Honduras (1947-1964): mata-mata entre campeões regionais, listado à parte pela RSSSF e sem
  reconhecimento da liga e da FENAFUTH.

Fontes por edição: até 1994/95, as tabelas finais de hondhist.html (as poucas páginas por temporada dessa época trazem só
parte dos jogos); de 1995/96 em diante, a página da temporada (hondAA.html; hondAAAA.html de 2010 em diante), só pelas
tabelas quando a página tem menos de 90% dos jogos.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "hon-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

FIM_PADRAO = (r"^(Second Level|Segunda Divisi|Liga de Ascenso|Copa |Supercopa|Aggregate Table|Tabla Acumulada|"
              r"Relegation Table|NB: full names|list of champions|About this document)")


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
        """2 por vitória até 1993/94; 3 a partir de 1994/95."""
        return 3 if self.ano_inicio >= 1994 else 2

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.wiki is None and self.espn is None


def _e(temporada, ini, fim, trechos, nome, campeao="", obs="", **kw):
    return Edicao(temporada, ini, fim, trechos, nome, campeao, obs, **kw)


def _rsssf():
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-concacaf"))
    import rsssf_concacaf
    return rsssf_concacaf


@lru_cache(maxsize=None)
def _texto(pagina: str) -> tuple[str, ...]:
    return tuple(l.replace("–", "-") for l in _rsssf().texto(PASTA_DADOS / "rsssf" / f"{pagina}.html"))


def _existe(pagina: str) -> bool:
    return (PASTA_DADOS / "rsssf" / f"{pagina}.html").exists()


def _linha(pagina: str, rx: str, depois: int = 0) -> int:
    ls = _texto(pagina)
    for i in range(depois, len(ls)):
        if re.fullmatch(rx, ls[i].strip(), re.I):
            return i
    raise ValueError(f"{pagina}: título {rx!r} não achado")


def _fim(pagina: str, ini: int, rx: str = FIM_PADRAO) -> int:
    ls = _texto(pagina)
    return next((i for i in range(ini + 3, len(ls)) if re.match(rx, ls[i].strip())), len(ls))


def _tem_jogos(pagina: str, ini: int, fim: int) -> bool:
    """A página traz pelo menos 90% dos jogos que a 1ª tabela do trecho diz (soma dos jogos / 2)?"""
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


EDICOES: list[Edicao] = []

# ---------------------------------------------------------------------------------------------------- 1965/66-1994/95

_ROT = ["1965/66", "1966/67", "1967/68", "1968/69", "1969/70", "1970/71", "1971/72", "1972/73", "1973", "1974", "1975",
        "1976", "1977", "1978/79", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989/90",
        "1990/91", "1991/92", "1992/93", "1993/94", "1994/95"]
_cab = [_linha("hondhist", re.escape(r)) for r in _ROT] + [_linha("hondhist", r"About this document")]
for _r, _i, _f in zip(_ROT, _cab, _cab[1:]):
    _a0 = int(_r[:4])
    _a1 = _a0 + 1 if "/" in _r else _a0
    EDICOES.append(_e(_r, _a0, _a1, [], f"Liga Nacional de Fútbol de Honduras {_r}", tabelas=[("hondhist", _i, _f)],
                      obs="só a tabela final (RSSSF, hondhist.html): a RSSSF não tem os jogos desta época",
                      sem_campeao="temporada abandonada, sem título; a classificação é a tabela do momento" if _r == "1972/73" else ""))

# ---------------------------------------------------------------------------------------------------- 1995/96-1996/97

for _a in (1995, 1996):
    _t = f"{_a}/{(_a + 1) % 100:02d}"
    EDICOES.append(_da_pagina(_t, _a, _a + 1, f"hond{(_a + 1) % 100:02d}", 0, None, f"Liga Nacional de Fútbol de Honduras {_t}"))

# ---------------------------------------------------------------------------------------------------- Apertura e Clausura

_FIM2 = r"^(Aggregate Table|Tabla Acumulada|Relegation Table|Second Level|Segunda Divisi|Liga de Ascenso|Copa |About this document)"


def _dois(pagina: str, a0: int):
    ls = _texto(pagina)
    try:
        ap = _linha(pagina, r"(Campeonato |Torneo )?Apertura( \d{4}(/\d{2})?)?( \(.*\))?:?")
    except ValueError:
        ap = 0
    cl = _linha(pagina, r"(Campeonato |Torneo )?Clausura( \d{4}(/\d{2})?)?( \(.*\))?:?", ap + 1)
    return ap, cl, _fim(pagina, cl, _FIM2)


for _a in [1997] + list(range(1999, 2026)):
    _pg = f"hond{(_a + 1) % 100:02d}" if _a + 1 < 2010 else f"hond{_a + 1}"
    _ap, _cl, _fm = _dois(_pg, _a)
    for _ano, _tor, _ini, _f in ((_a, "Apertura", _ap, _cl), (_a + 1, "Clausura", _cl, _fm)):
        _t = f"{_ano} {_tor}"
        EDICOES.append(_da_pagina(_t, _ano, _ano, _pg, _ini, _f, f"Liga Nacional de Fútbol de Honduras {_tor} {_ano}",
                                  sem_campeao="torneio abandonado pela pandemia de covid-19, sem título; a classificação é a "
                                              "tabela do momento" if _t == "2020 Clausura" else ""))
    if _a == 1997:   # 1999: torneio único de transição
        EDICOES.append(_da_pagina("1999", 1999, 1999, "hond99", 0, None, "Liga Nacional de Fútbol de Honduras 1999"))
