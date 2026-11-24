"""Edições da 1ª divisão da Costa Rica (crc-1): uma por título, como na lista de campeões da RSSSF (tablesc/coschamp.html),
que é a contagem oficial da UNAFUT. Escopo decidido em 24/11/2026:

- 1921 a 1985, um campeão por ano; 1954 e 1956 não foram disputados (sem edição); 1961 com duas edições, uma por entidade
  rival (Asofútbol, campeão Herediano; Federación, campeão Carmelita, título reconhecido pela UNAFUT em 2003).
- 1986/87 a 2006/07, uma por temporada (a temporada passou a cruzar o ano); de 1997/98 a 2006/07, Apertura e Clausura são
  fases do ano (a final entre os vencedores, quando houve, decide o título).
- 2007/08 em diante, Apertura e Clausura, uma edição cada ("2007 Apertura", "2008 Clausura"), até o Clausura 2026 (o Apertura
  2026 ainda está em disputa).

Fontes dos jogos por edição: a página da temporada (cosAA.html; cosAAAA.html de 2010 em diante). Até 1996 as páginas trazem
quase só as tabelas: a edição entra só com elas quando a página tem menos de 90% dos jogos que a tabela diz. 1991/92 e
1993/94 não têm página (só campeão e vice da lista). 2010/11 e 2011/12: a página só tem as tabelas e a fase final; a fase
regular vem da ESPN.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "crc-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

FIM_PADRAO = (r"^(Second Level|Segunda Divisi|Copa |Torneo de Copa|Copa Unafut|Supercopa|Aggregate Table|Tabla Acumulada|"
              r"NB: full names|list of champions|all-time table|About this document|\d{4}\.$|\d{4}/\d{2}\.$)")


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
        """2 por vitória até 1994/95; 3 a partir de 1995/96."""
        return 3 if self.ano_inicio >= 1995 else 2

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
    if esperado == 0:   # tabela em outro formato (1996/97): basta a página ter jogos de um campeonato inteiro
        return jogos >= 100
    return esperado > 0 and jogos >= 0.9 * esperado / 2


def _anual(t: str, a0: int, a1: int, pagina: str, ini: int = 0, fim: int | None = None, nome: str = "", **kw) -> Edicao:
    fim = fim if fim is not None else _fim(pagina, ini)
    nome = nome or f"Primera División de Costa Rica {t}"
    if _tem_jogos(pagina, ini, fim):
        return _e(t, a0, a1, [(pagina, ini, fim)], nome, **kw)
    obs = "só a tabela: a página da RSSSF não tem os jogos (os da final, quando há, ficam de fora)"
    return _e(t, a0, a1, [], nome, tabelas=[(pagina, ini, fim)], obs="; ".join(x for x in (kw.pop("obs", ""), obs) if x), **kw)


EDICOES: list[Edicao] = []

# ---------------------------------------------------------------------------------------------------- 1921-1985

for _a in range(1921, 1986):
    if _a in (1954, 1956):
        continue
    _pg = f"cos{_a % 100:02d}"
    if _a == 1961:
        _as = _linha(_pg, r"Asof[úu]tbol Championship 1961")
        _cp = _linha(_pg, r"Copa Asof[úu]tbol 1961")
        _fe = _linha(_pg, r"Federaci[óo]n Championship 1961")
        EDICOES.append(_anual("1961 Asofútbol", 1961, 1961, _pg, _as, _cp, "Campeonato de la Asofútbol 1961",
                              obs="campeonato da Asociación de Fútbol (os clubes rebeldes), paralelo ao da Federación"))
        EDICOES.append(_anual("1961 Federación", 1961, 1961, _pg, _fe, None, "Campeonato de la Federación 1961",
                              obs="campeonato da Federación (3 clubes); o título do Carmelita foi reconhecido pela UNAFUT em 2003"))
        continue
    EDICOES.append(_anual(str(_a), _a, _a, _pg))

# ---------------------------------------------------------------------------------------------------- 1986/87-2006/07

_TORNEIO_FASE = [(r"^Apertura( \d{4})?( \(.*\))?$", "Apertura"), (r"^Clausura( \d{4})?( \(.*\))?$", "Clausura")]
for _a in range(1986, 2007):
    _t = f"{_a}/{(_a + 1) % 100:02d}"
    _pg = f"cos{_a % 100:02d}" if _a < 1990 else f"cos{(_a + 1) % 100:02d}"
    if not _existe(_pg):
        EDICOES.append(_e(_t, _a, _a + 1, [], f"Primera División de Costa Rica {_t}",
                          obs="sem página da RSSSF: só o campeão e o vice da lista"))
        continue
    EDICOES.append(_anual(_t, _a, _a + 1, _pg))

# ---------------------------------------------------------------------------------------------------- Apertura e Clausura

_ESPN = {"2010 Apertura": ("2010-07-01", "2010-12-31"), "2011 Clausura": ("2011-01-01", "2011-06-30"),
         "2011 Apertura": ("2011-07-01", "2011-12-31"), "2012 Clausura": ("2012-01-01", "2012-06-30")}
_FIM2 = r"^(Aggregate Table|Tabla Acumulada|Second Level|Segunda Divisi|Copa |Supercopa|all-time table|NB: full names|About this document)"
for _a in range(2007, 2026):
    _pg = f"cos{(_a + 1) % 100:02d}" if _a + 1 < 2010 else f"cos{_a + 1}"
    _ap = _linha(_pg, r"(Campeonato )?(Torneo )?Apertura \d{4}.*")
    _cl = _linha(_pg, r"(Campeonato )?(Torneo )?Clausura \d{4}.*", _ap + 1)
    _fm = _fim(_pg, _cl, _FIM2)
    for _ano, _tor, _ini, _f in ((_a, "Apertura", _ap, _cl), (_a + 1, "Clausura", _cl, _fm)):
        _t = f"{_ano} {_tor}"
        if _t in _ESPN:
            # a página só tem as tabelas e a fase final; a ESPN destes anos tem jogos adiados repetidos (o original como 0-0) e
            # jogos faltando, e chama o Brujas de "Orión FC": a fase regular fica só com a tabela publicada
            EDICOES.append(_e(_t, _ano, _ano, [(_pg, _ini, _f)], f"Primera División de Costa Rica {_tor} {_ano}",
                              incompleta="a página da RSSSF só tem a tabela da fase regular e os jogos da fase final; a ESPN "
                                         "destes anos tem jogos adiados repetidos e jogos faltando (não foi usada); entram a "
                                         "tabela publicada e a fase final"))
        else:
            EDICOES.append(_anual(_t, _ano, _ano, _pg, _ini, _f, f"Primera División de Costa Rica {_tor} {_ano}"))
