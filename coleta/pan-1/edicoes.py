"""Edições da 1ª divisão do Panamá (pan-1): a ANAPROF (1988-2009) e a Liga Panameña de Fútbol (LPF, 2009 em diante), uma
edição por título, como na lista de campeões da RSSSF (tablesp/panamachamp.html, 63 títulos desde 1988) e na contagem da
imprensa local. Escopo decidido em 25/11/2026 (ok do Guilherme):

- 1988 a 2000/01: um campeão por temporada ("1988", "1994/95"); antes de 1988 só havia ligas da capital e de Colón, e os
  campeões nacionais de 1952 a 1987 são desconhecidos: ficam fora;
- LINFUNA (1994/95 e 1995/96): a liga paralela do racha, reconhecida pela FIFA na época, entra como edição à parte
  ("1994/95 LINFUNA"); a RSSSF a soma no total de títulos e a imprensa local conta os dois títulos do Árabe Unido;
- 2001 em diante: Apertura e Clausura, uma edição cada, com o ano do torneio ("2001 Apertura", "2010 Clausura" = Clausura
  2009/10); a final entre os dois campeões (2002, 2005 e 2006) virou uma supercopa e fica fora; em 2009 há dois Aperturas,
  o último da ANAPROF ("2009 Apertura ANAPROF") e o primeiro da LPF ("2009 Apertura"); o Apertura 2020 (pandemia) entra sem
  campeão; depois do Clausura 2025 veio o Clausura 2026.

Fonte de cada edição: a página da temporada da RSSSF (o título diz a temporada); de 1989 a 1993, a ANAPROF de 1994/95 e
1995/96 e 2001 não têm página: só o campeão e o vice da lista. A edição entra só com as tabelas quando o trecho tem menos de
90% dos jogos.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "pan-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

FIM_PADRAO = (r"^(Superfinal|Gran Final|Relegation Table|Aggregate (Final )?Table|Promotion/Relegation|"
              r"Second Level|Second Division|Primera Divisi[oó]n A|Primera A|All Star Game|Liga Nacional del Ascenso|Copa Rommel|"
              r"X[IVX]* Copa Rommel|Liga Ind[ií]gena|Copa Navidad|Liga Distritorial|Third Level|list of champions|"
              r"About this document)")

# nos Aperturas e Clausuras (2002-2006), a "Championship Final" entre os dois campeões é a supercopa que fica fora; até 2000/01
# ela é a final da temporada
FIM_TORNEIO = FIM_PADRAO.replace("^(", "^(Championship Final|", 1)


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
def lista() -> tuple[tuple[str, str, str], ...]:
    """panamachamp.html: (temporada da edição, campeão, vice), na ordem. Temporada: "1988", "1994/95", "1994/95 LINFUNA",
    "2001 Apertura", "2009 Apertura ANAPROF", "2010 Clausura" (Clausura 2009/10). Torneio abandonado (Apertura 2020): campeão
    vazio. Fica fora a seção "national club championship" (1951 e anos desconhecidos)."""
    saida, secao, temp = [], "", None
    for l in _texto("panamachamp"):
        s = l.strip()
        if s in ("ANAPROF League", "Liga Panameña de Fútbol", "LINFUNA"):
            secao = "LPF" if s.startswith("Liga") and secao == "ANAPROF League" else s
            continue
        if s.startswith(("Number of", "Total Number", "Championship Finals", "[*]", "national club championship")):
            secao = ""
            continue
        if not secao or s.startswith(("NB:", "Season")):
            continue
        m = re.match(r"^(\d{4}(?:/\d{2})?)?\s*(Ap|Cl)?\s+(\S.*?)\s*$", l)
        if not m or not (m.group(1) or m.group(2)):
            continue
        if m.group(1):
            temp = m.group(1)
        tor, resto = m.group(2), m.group(3)
        a = int(temp[:4])
        if secao == "LINFUNA":
            t_ = f"{temp} LINFUNA"
        elif not tor:
            t_ = temp
        elif tor == "Ap":
            t_ = f"{a} Apertura" + (" ANAPROF" if a == 2009 and secao == "ANAPROF League" else "")
        else:
            t_ = f"{a + 1 if '/' in temp else a} Clausura"
        if re.match(r"^abandoned", resto):
            saida.append((t_, "", ""))
            continue
        corpo = re.sub(r"\s*\[(?!\*\]).*$", "", resto)
        mm = re.match(r"^(\S.*?)\s{2,}(?:\[\*\]\s+|(?:\d{1,2}-\d{1,2}\s+)*)(\S.*)$", corpo)
        camp, vice = (mm.group(1), mm.group(2)) if mm else (corpo, "")
        saida.append((t_, camp.strip(), vice.strip()))
    return tuple(saida)


_PAGINAS = sorted(p.stem for p in (PASTA_DADOS / "rsssf").glob("panama*.html") if "champ" not in p.stem)
_TITULO = re.compile(r"(ANAPROF - |Liga Panameña de Fútbol - )?(?:Torneo )?(Apertura|Clausura)(?: (\d{4}(?:/\d{2})?))?")


def _torneio(ano: int, tor: str, lpf: bool) -> tuple[str, int, int]:
    """Página e trecho do torneio `tor` ("Apertura", "Clausura") do ano, pelo título ("Torneo Apertura 2012", "Torneo
    Clausura 2009/10", "Clausura 2005", "Liga Panameña de Fútbol - Torneo Apertura 2009"); vai até o próximo torneio ou o fim
    padrão. Título sem ano só vale na página do próprio ano (2002-2006)."""
    propria = f"panama{ano % 100:02d}" if ano < 2010 else f"panama{ano}"
    # Clausura do ano: "2010" ou "2009/10"; Apertura do ano: "2010" ou "2010/11"
    anos = {str(ano), f"{ano - 1}/{ano % 100:02d}" if tor == "Clausura" else f"{ano}/{(ano + 1) % 100:02d}"}
    for pg in [x for x in (propria, f"panama{ano + 1}", f"panama{ano - 1}") if x in _PAGINAS]:
        ls = _texto(pg)
        achados = []
        for i, l in enumerate(ls):
            m = _TITULO.fullmatch(l.strip())
            if not m or m.group(2) != tor:
                continue
            if m.group(3) and m.group(3) not in anos or not m.group(3) and pg != propria:
                continue
            if ano == 2009 and tor == "Apertura" and ("Liga" in (m.group(1) or "")) != lpf:
                continue
            achados.append(i)
        # o primeiro (os seguintes são da 2ª divisão); o título repetido logo abaixo ("Torneo Clausura 2026" no índice do alto
        # da página): vale o de baixo
        achados = [i for i in achados if not any(ls[k].strip() == ls[i].strip() for k in range(i + 1, min(i + 4, len(ls))))]
        if achados:
            i = achados[0]
            fim = next((k for k in range(i + 1, len(ls)) if _TITULO.fullmatch(ls[k].strip())), len(ls))
            return pg, i, min(fim, _fim(pg, i, FIM_TORNEIO))
    raise ValueError(f"torneio {tor} {ano} não achado")


EDICOES: list[Edicao] = []

for _t, _c, _v in lista():
    _a0 = int(_t[:4])
    _a1 = _a0 + 1 if re.match(r"^\d{4}/", _t) else _a0
    if "LINFUNA" in _t:
        _pg = f"panama{_a1 % 100:02d}"
        EDICOES.append(_e(_t, _a0, _a1, [(_pg, 0, None)], f"LINFUNA {_t[:7]}",
                          obs="liga paralela da LINFUNA (racha de 1994-96, reconhecida pela FIFA na época): só a final"))
        continue
    _m = re.search(r"(Apertura|Clausura)", _t)
    if not _m:   # um campeão por temporada (até 2000/01)
        _pg = f"panama{_a1 % 100:02d}" if "/" in _t else f"panama{_a0 % 100:02d}"
        _nome = f"ANAPROF {_t}"
        if _pg not in _PAGINAS or _a0 in (1994, 1995):   # as páginas de 1994/95 e 1995/96 só têm a LINFUNA
            EDICOES.append(_e(_t, _a0, _a1, [], _nome, obs="sem página da RSSSF: só o campeão e o vice"))
        else:
            EDICOES.append(_da_pagina(_t, _a0, _a1, _pg, 0, None, _nome))
        continue
    _tor = _m.group(1)
    _nome = f"{'ANAPROF' if _a0 < 2009 or 'ANAPROF' in _t else 'LPF'} {_tor} {_a0}"
    try:
        _pg, _i, _f = _torneio(_a0, _tor, "ANAPROF" not in _t)
    except ValueError:   # 2001: sem página
        EDICOES.append(_e(_t, _a0, _a0, [], _nome, obs="sem página da RSSSF: só o campeão e o vice"))
        continue
    EDICOES.append(_da_pagina(_t, _a0, _a0, _pg, _i, _f, _nome,
                              sem_campeao="torneio abandonado em 17/03/2020 pela pandemia de covid-19, sem título; a "
                                          "classificação é a tabela do momento" if not _c else ""))

# 1996/97: a página não tem as rodadas 5 a 7 da primeira fase (100 dos 132 jogos) e põe a 2ª divisão entre a primeira fase e
# o hexagonal final: entra com os jogos que tem (incompleta), sem a 2ª divisão
_e97 = next(x for x in EDICOES if x.temporada == "1996/97")
_a = _linha("panama97", r"Second Division Championship:")
_b = _linha("panama97", r"Second Stage", _a)
_e97.trechos, _e97.tabelas = [("panama97", 0, _a), ("panama97", _b, _fim("panama97", _b))], []
_e97.incompleta = "a página não tem as rodadas 5 a 7 da primeira fase (100 dos 132 jogos)"
_e97.obs = ""

# a LINFUNA logo depois da ANAPROF da mesma temporada (ordenação estável pelo ano de início)
EDICOES.sort(key=lambda e: e.ano_inicio)
