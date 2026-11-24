"""Edições da 1ª divisão da Guatemala (gua-1): o Campeonato de Liga (Liga Nacional), uma edição por título, como na lista de
campeões da RSSSF (tablesg/guatchamp.html, 100 títulos desde 1942) e na contagem oficial. Escopo decidido em 24/11/2026: a
Liga Capitalina / Liga Mayor (1919-1941, liga da capital) fica fora.

- 1942/43 a 1998/99: um campeão por temporada (rótulos da RSSSF: "1942/43", "1943", "1970/71", "1971"...); os anos sem
  campeonato não têm edição.
- 1999/00 em diante: Apertura e Clausura, uma edição cada ("1999 Apertura", "2000 Clausura"); em 2001/02 o primeiro torneio
  foi o Campeonato de Reordenamiento ("2001 Reordenamiento"). O Clausura 2020 (pandemia) entra sem campeão.

Cada página da RSSSF tem a temporada no título ("Guatemala 1970/71"); os nomes dos arquivos são irregulares (guat71a.html é
1970/71), e o casamento é pelo título. Até 1995/96 as páginas trazem quase só as tabelas: a edição entra só com elas quando
a página tem menos de 90% dos jogos.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "gua-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

FIM_PADRAO = (r"^(Super Cup|Supercopa|Tabla Anual|Primera Divisi[oó]n\s*$|Copa |Torneo de Copa|Second Level|Segunda Divisi|Primera Divisi[oó]n B|Aggregate Table|"
              r"Tabla Acumulada|NB: full names|list of champions|About this document)")


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
    return next((i for i in range(ini + 3, len(ls)) if re.match(rx, ls[i].strip())), len(ls))


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
def paginas_por_temporada() -> dict[str, str]:
    """Título da página ("Guatemala 1999/2000") -> nome do arquivo, com a temporada no formato da lista ("1999/00")."""
    saida = {}
    for p in sorted((PASTA_DADOS / "rsssf").glob("guat*.html")):
        if p.stem == "guatchamp":
            continue
        tit = next((l.strip() for l in _texto(p.stem) if l.strip()), "")
        m = re.match(r"^Guatemala (\d{4})(?:/(\d{2,4}))?\s*$", tit)
        if m:
            saida[f"{m.group(1)}/{m.group(2)[-2:]}" if m.group(2) else m.group(1)] = p.stem
    return saida


def lista_temporadas() -> list[str]:
    """Temporadas do Campeonato de Liga na lista de campeões, na ordem (a 1ª coluna de cada linha com ano)."""
    ls = _texto("guatchamp")
    ini = next(i for i, l in enumerate(ls) if l.strip() == "Campeonato de Liga")
    saida = []
    for l in ls[ini:]:
        if l.strip().startswith("NB:"):
            break
        if m := re.match(r"^(\d{4}(?:/\d{2})?)\s", l):
            saida.append(m.group(1))
    return saida


EDICOES: list[Edicao] = []
_FIM2 = r"^(Aggregate Table|Tabla Acumulada|Tabla Anual|Primera Divisi[oó]n\s*$|Promotion|Torneo de Copa|Copa |Super Cup|Supercopa|Second Level|Segunda Divisi|About this document)"

for _t in lista_temporadas():
    _a0 = int(_t[:4])
    _a1 = _a0 + 1 if "/" in _t else _a0
    _pg = paginas_por_temporada().get(_t)
    if _a0 < 1999:
        if not _pg:
            EDICOES.append(_e(_t, _a0, _a1, [], f"Liga Nacional de Guatemala {_t}", obs="sem página da RSSSF: só o campeão"))
            continue
        EDICOES.append(_da_pagina(_t, _a0, _a1, _pg, 0, None, f"Liga Nacional de Guatemala {_t}"))
        continue
    # Apertura (ou Reordenamiento, 2001) e Clausura
    _ap = _linha(_pg, r"(Campeonato de |Campeonato |Torneo )?(Apertura|Reordenamiento)( \d{4}(/\d{2})?)?( \(.*\))?:?")
    _cl = _linha(_pg, r"(Campeonato de |Campeonato |Torneo )?Clausura( \d{4}(/\d{2})?)?( \(.*\))?:?", _ap + 1)
    _fm = _fim(_pg, _cl, _FIM2)
    _tor1 = "Reordenamiento" if "Reordenamiento" in _texto(_pg)[_ap] else "Apertura"
    for _ano, _tor, _ini, _f in ((_a0, _tor1, _ap, _cl), (_a0 + 1, "Clausura", _cl, _fm)):
        _tt = f"{_ano} {_tor}"
        EDICOES.append(_da_pagina(_tt, _ano, _ano, _pg, _ini, _f, f"Liga Nacional de Guatemala {_tor} {_ano}",
                                  sem_campeao="torneio abandonado pela pandemia de covid-19, sem título; a classificação é a "
                                              "tabela do momento" if _tt == "2020 Clausura" else ""))
