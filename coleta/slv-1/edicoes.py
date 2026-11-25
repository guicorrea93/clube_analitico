"""Edições da 1ª divisão de El Salvador (slv-1): uma edição por título, como na lista de campeões da RSSSF
(tablese/elsalchamp.html, 110 títulos desde 1926), que é a contagem que a imprensa de lá usa. Escopo decidido em 24/11/2026:

- 1926 a 1946: os campeonatos nacionais oficiais (1926, 1927, 1928, 1929/30, 1937, 1938, 1942, 1943, 1946): final, ou
  quadrangular, entre os campeões das zonas; ficam fora 1924 e 1925 (não oficiais, pela própria RSSSF), os títulos só da
  Zona Central (1931-36, 1939-41, 1944-45) e 1947 (parou depois de duas rodadas, sem tabela);
- 1948/49 a 1997/98: um campeão por temporada (os anos sem campeonato não têm edição);
- 1998/99: só o Clausura ("Copa Clima"), que deu o título; a Copa Pilsener (Apertura) não é título oficial;
- 1999/00 em diante: Apertura e Clausura, uma edição cada ("1999 Apertura", "2000 Clausura"). O Clausura 2023 (cancelado
  depois da tragédia no estádio Cuscatlán) entra sem campeão.

Fontes de cada edição: até 1985/86 a página de tabelas finais (elsalhist.html, uma seção por temporada); de 1986/87 em
diante a página da temporada quando existe (o título diz a temporada: "El Salvador 1999/2000"). A edição entra só com as
tabelas quando o trecho tem menos de 90% dos jogos.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "slv-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

FIM_PADRAO = (r"^(Aggregate Table|Tabla Anual|Copa Presidente|Second Level|Third Level|Reserves Tournament|Promotion/Relegation|"
              r"Playoff Against Ninth|Liga de Ascenso|Second Division|Segunda Divisi|list of champions|About this document)")


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
def paginas_por_temporada() -> dict[str, str]:
    """Título da página ("El Salvador 1999/2000") -> nome do arquivo, com a temporada no formato da lista ("1999/00")."""
    saida = {}
    for p in sorted((PASTA_DADOS / "rsssf").glob("elsal*.html")):
        if p.stem in ("elsalchamp", "elsalhist"):
            continue
        tit = next((l.strip() for l in _texto(p.stem) if l.strip()), "")
        m = re.match(r"^El Salvador (\d{4})(?:/(\d{2,4}))?\s*$", tit)
        if m:
            saida[f"{m.group(1)}/{m.group(2)[-2:]}" if m.group(2) else m.group(1)] = p.stem
    return saida


@lru_cache(maxsize=None)
def secoes_hist() -> dict[str, tuple[int, int]]:
    """Seções da página de tabelas finais: temporada ("1926", "1948/49") -> (linha do título, linha do próximo título)."""
    ls = _texto("elsalhist")
    tit = [(i, l.strip()) for i, l in enumerate(ls) if re.fullmatch(r"\d{4}(/\d{2})?(-\d{2}(/\d{2})?)?", l.strip())]
    fim = next(i for i, l in enumerate(ls) if l.strip() == "About this document")
    return {t: (i, tit[k + 1][0] if k + 1 < len(tit) else fim) for k, (i, t) in enumerate(tit)}


@lru_cache(maxsize=None)
def lista() -> tuple[tuple[str, str, str], ...]:
    """elsalchamp.html: (temporada da edição, campeão, vice) dos títulos oficiais, na ordem. Temporada como as edições:
    "1926", "1948/49", "1998/99" (o Clausura que deu o título), "1999 Apertura", "2000 Clausura". Torneio abandonado
    (Clausura 2023): campeão vazio. Ficam fora 1924-25 (não oficiais), 1947 e 1949/50 (sem campeonato) e a Copa Pilsener."""
    saida, oficial = [], False
    for l in _texto("elsalchamp"):
        s = l.strip()
        if s.startswith("Sports Week Football Tournament"):
            oficial = "(official" in s
            continue
        if s in ("Playoff between Zonal Champions", "National League"):
            oficial = True
            continue
        if s.startswith("NB:"):
            break
        m = re.match(r"^(\d{4}(?:/\d{2})?)\s+(\S.*?)\s*$", l)
        if not m or not oficial:
            continue
        temp, resto = m.groups()
        notas = re.findall(r"\[([^\]]*)\]", resto)
        corpo = re.sub(r"\s*\[.*$", "", resto)
        if "Pilsener" in notas:
            continue
        if re.match(r"^championship abandoned", corpo) and not {"Apertura", "Clausura"} & set(notas):
            continue
        if re.match(r"^(no championship|not held)", corpo):
            continue
        a = int(temp[:4])
        if temp == "1998/99":
            t_ = temp
        elif "Apertura" in notas:
            t_ = f"{a} Apertura"
        elif "Clausura" in notas:
            t_ = f"{a + 1} Clausura"
        else:
            t_ = temp
        if corpo.startswith("championship abandoned"):
            saida.append((t_, "", ""))
            continue
        mm = re.match(r"^(\S.*?)\s{2,}((?:\d{1,2}-\d{1,2}\s+)*)(\S.*)$", corpo)
        camp, vice = (mm.group(1), mm.group(3)) if mm else (corpo, "")
        saida.append((t_, camp.strip(), "" if vice.strip() == "not determined" else vice.strip()))
    return tuple(saida)


EDICOES: list[Edicao] = []
_FIM2 = FIM_PADRAO

for _t, _c, _v in lista():
    _a0 = int(_t[:4])
    _a1 = _a0 + 1 if "/" in _t else _a0
    _nome = f"Primera División de El Salvador {_t}"
    if _a0 < 1947:   # campeonato nacional entre os campeões das zonas: final (ou quadrangular) na página de tabelas
        _i, _f = secoes_hist()[_t]
        _q = any(_rsssf().linha_tabela(l) for l in _texto("elsalhist")[_i:_f])
        EDICOES.append(_e(_t, _a0, _a1, [] if _q else [("elsalhist", _i, _f)], f"Campeonato Nacional de El Salvador {_t}",
                          tabelas=[("elsalhist", _i, _f)] if _q else [],
                          obs="quadrangular entre os campeões das zonas: a RSSSF só tem a tabela" if _q else
                              "final entre os campeões das zonas (Semana Deportiva até 1929/30)"))
        continue
    if _t == "1998/99":   # só o Clausura ("Copa Clima"); a Copa Pilsener não é título oficial
        _pg = paginas_por_temporada()[_t]
        _cl = _linha(_pg, r"Clausura \(\"Copa Clima\"\)")
        EDICOES.append(_da_pagina(_t, _a0, _a1, _pg, _cl, _linha(_pg, r"Topscorers:", _cl), _nome,
                                  obs="só o Clausura (\"Copa Clima\"), que deu o título; a Copa Pilsener (Apertura) não é "
                                      "título oficial"))
        continue
    if "/" in _t or not re.search(r"Apertura|Clausura", _t):   # um campeão por temporada
        _pg = paginas_por_temporada().get(_t)
        if _pg:
            EDICOES.append(_da_pagina(_t, _a0, _a1, _pg, 0, None, _nome))
        else:
            _i, _f = secoes_hist()[_t]
            EDICOES.append(_da_pagina(_t, _a0, _a1, "elsalhist", _i, _f, _nome))
        continue
    # Apertura e Clausura: a página da temporada que começa no ano do Apertura
    _tor = _t.split()[1]
    _ta = _a0 if _tor == "Apertura" else _a0 - 1
    _pg = paginas_por_temporada()[f"{_ta}/{(_ta + 1) % 100:02d}"]
    _ap = _linha(_pg, r"(Campeonato )?Apertura( \d{4}(/\d{2})?)?( \(.*\))?:?")
    _cl = _linha(_pg, r"(Campeonato )?Clausura( \d{4}(/\d{2})?)?( \(.*\))?:?", _ap + 1)
    _ini, _f = (_ap, _cl) if _tor == "Apertura" else (_cl, _fim(_pg, _cl, _FIM2))
    EDICOES.append(_da_pagina(_t, _a0, _a0, _pg, _ini, _f, f"Primera División de El Salvador {_tor} {_a0}",
                              sem_campeao="torneio cancelado nas quartas de final depois da tragédia no estádio Cuscatlán "
                                          "(20/05/2023), sem título; a classificação é a da fase regular" if not _c else ""))


def _corta(temporada: str, de: str, ate: str, motivo: str) -> None:
    """Tira da edição o trecho da página entre os títulos `de` (inclusive) e `ate` (exclusive), com o motivo na observação."""
    e = next(x for x in EDICOES if x.temporada == temporada)
    pg, ini, fim = e.trechos[0]
    a = _linha(pg, de, ini)
    b = _linha(pg, ate, a + 1)
    e.trechos = [(pg, ini, a), (pg, b, fim)]
    e.obs = "; ".join(x for x in (e.obs, motivo) if x)


_corta("1996/97", r"Repechaje \[best of 3\]:", r"First six teams qualified for second stage \(knock out\)\.",
       "o repechaje Municipal Limeño x Real Independiente (vaga na 1ª divisão, contra clube da 2ª) fica fora")
_corta("2022 Apertura", r"Original Round 1 \[annulled\]", r"Round 1",
       "as duas rodadas de julho foram anuladas (campeonato parado pela investigação contra a federação e recomeçado em "
       "setembro): ficam fora, com a tabela do momento da parada")


# 2010/11 e 2011/12: a página só tem as tabelas e a fase final. A ESPN tem 94 e 93 jogos dos Aperturas de 2010 e 2011, mas
# não fecha com as tabelas da RSSSF (placares diferentes, um jogo faltando, um repetido, em 6 e 7 clubes): não é usada para
# completar essas edições (como na Costa Rica); os Clausuras de 2011 e 2012 a ESPN quase não tem (1 e 67 dos 90 jogos).
