"""Edições da 1ª divisão mexicana (mex-1): uma por título, como na lista de campeões da RSSSF (mexchamp.html) e na da
Wikipédia em inglês ("List of Mexican football champions"). Escopo decidido pelo Guilherme em 23/11/2026:

- 1902/03 a 1942/43: era amadora (Primera Fuerza e Liga Mayor do Distrito Federal), uma edição por temporada. 1920/21 e
  1921/22 têm duas edições, uma por liga (Liga Mexicana, a oficial, e Liga Nacional, a do RC España). O Torneo del
  Centenario (1921, do governo) fica fora. 1930/31 foi cancelada no começo: entra sem campeão, com a tabela do
  cancelamento. 1911/12 e 1916/17 não têm página: só a tabela de mexhist.html.
- 1943/44 a 1995/96: profissional, uma edição por temporada (a liguilla e as finais, desde 1970/71, são fases). Os torneios
  curtos México 70, Prode 85 e México 86, que a federação conta como título, são edições próprias.
- 1996/97 a 2001/02: Invierno e Verano, uma edição cada ("1996 Invierno", "1997 Verano").
- 2002/03 em diante: Apertura e Clausura, uma edição cada ("2002 Apertura", "2003 Clausura"). O Clausura 2020 (pandemia)
  entra sem campeão. A última é o Clausura 2026 (o Apertura 2026 ainda está em disputa).
Ficam de fora a 2ª e a 3ª divisões, a Copa México, o Campeón de Campeones, a Interliga, os playoffs da Libertadores e as
copas das páginas da era amadora (Copa Tower, Copa Eliminatoria...).

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], linhas do texto puro (rsssf_concacaf.texto); linha final None:
  até o primeiro título de outra competição (FIM_PADRAO). Página mexAAAA (1903-1919), mexAA (1920-2009: a do ano em que a
  temporada termina; mex6970 = 1969/70, mex70 = México 70, mex86 = Prode 85 e México 86), mex2-2010 e mexAAAA (2011 em diante:
  o Apertura do ano anterior e o Clausura do ano). Nas páginas com dois torneios, os trechos saem dos títulos ("Invierno 1996",
  "Clausura 2010").
- espn: datas dos jogos que vêm da ESPN (quando a página não tem a fase regular).
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "mex-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada (quando a edição não diz a linha final)
FIM_PADRAO = (r"^(Copa (Tower|M[eé]xico|Eliminatoria|Presidente|Covadonga|El Universal|Alcal[aá]|MX|Libertadores)|Tower Cup|"
              r"Campe[oó]n de Campeones|(Mexico|M[eé]xico)\b.*(Segunda|Second Level|Primera Divisi[oó]n A|Third)|Segunda Divisi|"
              r"Second Level|Primera Divisi[oó]n A\b|Liga de Ascenso|Liga Expansi[oó]n|Changes for (the |tne )?next season|"
              r"(Torneo )?Interliga|Torneo Pre-Libertadores|Libertadores \d{4} Playoff|Supercopa|International Match|"
              r"\d+(st|nd|rd|th) [Aa]nnual [Ii]nternational|Friendly matches|Promotional [Tt]ournament|list of champions|"
              r"Promotion ?/ ?Relegation|Relegation ?/ ?Promotion|Promotion (Playoff|Final)|Promotional playoff|"
              r"Primera Divisi[oó]n \"A\"|Liguilla Pre-Libertadores|Copa Federaci[oó]n|Torneo Presidente|.*\(Extraordinary|"
              r"About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1902/03", "1920/21 Liga Mexicana", "1970 México 70", "2023 Apertura"
    ano_inicio: int
    ano_fim: int
    trechos: list[tuple[str, int, int | None]]
    nome_oficial: str
    campeao_rsssf: str = ""
    obs: str = ""
    fases: list[tuple[str, str]] = field(default_factory=list)
    nomes: dict[str, str] = field(default_factory=dict)
    soma_de: list[str] = field(default_factory=list)              # (não usado)
    wiki: str | None = None                                       # (não usado)
    hist: str = ""                                                # título da seção de mexhist.html com a tabela final
    ogol: int | None = None                                       # (não usado)
    espn: tuple[str, str] | None = None                           # datas dos jogos que vêm da ESPN
    espn_fases: list[tuple[str, str]] = field(default_factory=list)
    tabelas: list[tuple[str, int, int | None]] = field(default_factory=list)   # trechos lidos só pelas tabelas
    parcial: tuple[str, int, int] | None = None                    # (não usado)
    incompleta: str = ""                                           # o que falta nos jogos (entra na observação)
    sem_campeao: str = ""                                          # motivo (1930/31, Clausura 2020)

    @property
    def pontos_vitoria(self) -> int:
        """2 por vitória até 1994/95; 3 a partir de 1995/96."""
        return 3 if self.ano_inicio >= 1995 else 2

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.wiki is None and self.espn is None


def _e(temporada, ini, fim, trechos, nome, campeao="", obs="", **kw):
    return Edicao(temporada, ini, fim, trechos, nome, campeao, obs, **kw)


@lru_cache(maxsize=None)
def _texto(pagina: str) -> tuple[str, ...]:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-concacaf"))
    import rsssf_concacaf
    return tuple(rsssf_concacaf.texto(PASTA_DADOS / "rsssf" / f"{pagina}.html"))


def _linha(pagina: str, rx: str, depois: int = 0) -> int:
    """Primeira linha (a partir de `depois`) cujo texto inteiro casa com rx."""
    ls = _texto(pagina)
    for i in range(depois, len(ls)):
        if re.fullmatch(rx, ls[i].strip(), re.I):
            return i
    raise ValueError(f"{pagina}: título {rx!r} não achado")


# títulos de outra competição no meio de um torneio (Libertadores, Interliga): o trecho pula até a fase seguinte do torneio
_PULA = r"(Liguilla Pre-Libertadores \d{4}.*|Copa Libertadores \d{4} (qualification|Playoff)|Libertadores \d{4} Playoff|(Torneo )?Interliga( \d{4})?|Torneo Pre-Libertadores \d{4})"
_VOLTA = r"(Playoffs?( \(Liguilla\))?|Championship [Pp]layoffs?|Quarterfinals|(Apertura|Clausura|Invierno|Verano) \d{4}.*)"


def _cortes(pagina: str, ini: int, fim: int) -> list[tuple[str, int, int]]:
    """O trecho [ini, fim) sem as competições do meio (_PULA)."""
    ls = _texto(pagina)
    saida, a, i = [], ini, ini
    while i < fim:
        if re.fullmatch(_PULA, ls[i].strip(), re.I):
            saida.append((pagina, a, i))
            k = i + 1
            while k < fim and not re.fullmatch(_VOLTA, ls[k].strip(), re.I):
                k += 1
            a = i = k
            continue
        i += 1
    if a < fim:
        saida.append((pagina, a, fim))
    return saida


def _dois_torneios(pagina: str, t1: str, t2: str) -> tuple[list, list]:
    """Página com dois torneios ("Invierno 1996" e "Verano 1997"; "Apertura 2009" e "Clausura 2010")."""
    a = _linha(pagina, rf"{t1} \d{{4}}( \(.*\))?")
    b = _linha(pagina, rf"{t2} \d{{4}}( \(.*\))?", a + 1)
    from_fim = _fim(pagina, b)
    return _cortes(pagina, a, b), _cortes(pagina, b, from_fim)


def _fim(pagina: str, ini: int) -> int:
    """Primeira linha, depois do primeiro jogo, que abre outra competição (como ler_rsssf.fim_padrao)."""
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-concacaf"))
    import rsssf_concacaf
    ls = _texto(pagina)
    viu = False
    for i in range(ini, len(ls)):
        if not viu:
            viu = bool(rsssf_concacaf._jogo(ls[i].replace("–", "-")))
            continue
        if re.match(FIM_PADRAO, ls[i].strip(), re.I):
            return i
    return len(ls)


_INICIO = r"((\d{4}[-/]\d{2} )?Regular [Ss]eason( \d{4}[-/]\d{2})?|Regular SeasonRound 1|First Phase)"


def _temporada(pagina: str) -> list[tuple[str, int, None]]:
    """Página de uma temporada só: do título da fase regular (ou do começo) até a próxima competição."""
    try:
        ini = _linha(pagina, _INICIO)
    except ValueError:
        ini = 0
    return [(pagina, ini, None)]


# ---------------------------------------------------------------------------------------------------- era amadora

_NOME_AMADOR = [
    (1902, "The Mexico Association Foot-ball League"),
    (1904, "The Mexico Amateur Association Football League"),
    (1912, "Asociación de Aficionados de México en la Liga de Football"),
    (1916, "Liga Mexicana de Aficionados de Futbol Asociación"),
    (1922, "Campeonato de Primera Fuerza de la Federación Mexicana de Football Association"),
    (1923, "Campeonato de Primera Fuerza de la Federación Central de Futbol"),
    (1927, "Campeonato de Primera Fuerza de la Federación Mexicana de Futbol"),
    (1930, "Campeonato Preferente de la Liga Mayor del Distrito Federal"),
]
_SEM_PAGINA = "sem jogos: a RSSSF não tem página desta temporada (só a tabela final de mexhist.html)"
_POUCOS = ("a página da RSSSF traz só parte dos jogos (\"known results\"); a classificação é a tabela final publicada "
           "(mexhist.html)")
# temporadas amadoras com jogos incompletos na RSSSF (a conferência mostra quais faltam)
_INCOMPLETA_AMADOR = {"1920/21 Liga Mexicana": _POUCOS, "1920/21 Liga Nacional": _POUCOS, "1921/22 Liga Mexicana": _POUCOS,
                      "1921/22 Liga Nacional": _POUCOS + "; a Liga Nacional não terminou (a decisão foi um jogo extra)",
                      "1915/16": "a página da RSSSF traz 22 dos 30 jogos; a classificação é a tabela final publicada",
                      "1924/25": "a página da RSSSF traz 37 dos 42 jogos; a classificação é a tabela final publicada"}
# trechos explícitos da era amadora: amistosos antes da liga (1902/03); copa no meio da liga (1927/28: a Copa Eliminatoria foi
# jogada na pausa para a seleção ir aos Jogos Olímpicos de Amsterdã)
_TRECHOS_AMADOR = {"1902/03": [("mex1903", 56, None)], "1927/28": [("mex28", 14, 138), ("mex28", 161, None)]}

EDICOES: list[Edicao] = []


def _nome_amador(a: int) -> str:
    return [n for a0, n in _NOME_AMADOR if a0 <= a][-1]


for _a in range(1902, 1943):
    _t = f"{_a}/{(_a + 1) % 100:02d}"
    _pg = f"mex{_a + 1}" if _a + 1 <= 1919 else f"mex{(_a + 1) % 100:02d}"
    _hist = f"{_a}-{(_a + 1) % 100:02d}"
    if _a == 1920 or _a == 1921:   # duas ligas
        _ls = _texto(_pg)
        _ln = _linha(_pg, r"Liga Nacional de Aficionados al Football Association \(unofficial\)")
        if _a == 1920:
            _lm = [(_pg, _linha(_pg, r"Liga Mexicana de Aficionados al Football Association \(official\)"), _ln)]
        else:
            _lm = [(_pg, 0, _ln)]
        EDICOES.append(_e(f"{_t} Liga Mexicana", _a, _a + 1, _lm, f"Liga Mexicana de Aficionados de Futbol Asociación {_t}",
                          hist=f"{_hist} Liga Mexicana", incompleta=_INCOMPLETA_AMADOR[f"{_t} Liga Mexicana"],
                          obs="liga oficial; o RC España jogou a Liga Nacional, paralela (alguns historiadores dão a temporada como anulada)"))
        EDICOES.append(_e(f"{_t} Liga Nacional", _a, _a + 1, [(_pg, _ln, None)], f"Liga Nacional de Aficionados de Futbol Asociación {_t}",
                          hist=f"{_hist} Liga Nacional", incompleta=_INCOMPLETA_AMADOR[f"{_t} Liga Nacional"],
                          obs="liga paralela, do RC España, que a lista de campeões da RSSSF conta como título (alguns historiadores dão a temporada como anulada)"))
        continue
    _existe = (PASTA_DADOS / "rsssf" / f"{_pg}.html").exists() and _a not in (1911, 1916)
    EDICOES.append(_e(_t, _a, _a + 1, _TRECHOS_AMADOR.get(_t, _temporada(_pg)) if _existe else [], f"{_nome_amador(_a)} {_t}",
                      hist=_hist, obs="" if _existe else _SEM_PAGINA, incompleta=_INCOMPLETA_AMADOR.get(_t, ""),
                      sem_campeao="temporada cancelada no começo e declarada deserta (o RC España saiu no caso Gaspar Rubio e a liga foi refeita como "
                                  "Liga Mayor do Distrito Federal); a classificação é a tabela do cancelamento" if _a == 1930 else ""))

# ---------------------------------------------------------------------------------------------------- profissional

for _a in range(1943, 1996):
    if _a == 1985:   # sem temporada 1985/86: Prode 85 e México 86 (página mex86)
        _ls = _texto("mex86")
        _p, _m = _linha("mex86", r"TOURNAMENT PRODE .85"), _linha("mex86", r"TOURNAMENT \"M[ÉE]XICO .86\"")
        EDICOES.append(_e("1985 Prode 85", 1985, 1985, [("mex86", _p, _m)], "Torneo Prode 85", hist="PRODE-85",
                          obs="torneio curto no lugar da temporada 1985/86 (Copa do Mundo de 1986); a federação o conta como "
                              "título desde outubro de 1986"))
        EDICOES.append(_e("1986 México 86", 1985, 1986, [("mex86", _m, None)], "Torneo México 86", hist="México-86",
                          obs="torneio curto no lugar da temporada 1985/86 (Copa do Mundo de 1986); a federação o conta como "
                              "título desde outubro de 1986"))
        continue
    _t = f"{_a}/{(_a + 1) % 100:02d}"
    _pg = "mex6970" if _a == 1969 else f"mex{(_a + 1) % 100:02d}"
    _nome = "Liga Mayor" if _a < 1949 else "Primera División de México"
    EDICOES.append(_e(_t, _a, _a + 1, _temporada(_pg), f"{_nome} {_t}", hist=f"{_a}-{(_a + 1) % 100:02d}"))
    if _a == 1969:
        EDICOES.append(_e("1970 México 70", 1970, 1970, [("mex70", _linha("mex70", "First Phase"), None)], "Torneo México 70",
                          hist="México 1970",
                          obs="torneio curto entre 1969/70 e 1970/71, jogado antes e depois da Copa do Mundo de 1970; a "
                              "federação o conta como título"))

# ---------------------------------------------------------------------------------------------------- torneios curtos

_NOMES_TORNEIO = {"2010 Clausura": "Torneo Bicentenario 2010", "2020 Apertura": "Torneo Guard1anes 2020",
                  "2021 Clausura": "Torneo Guard1anes 2021", "2021 Apertura": "Torneo Grita México A21",
                  "2022 Clausura": "Torneo Grita México C22"}
# a página da RSSSF de 2025/26 só tem as tabelas e a liguilla: a fase regular vem da ESPN (o jogo que a página já tem sai da ESPN)
_ESPN = {"2025 Apertura": ("2025-07-01", "2025-11-12"), "2026 Clausura": ("2026-01-01", "2026-04-28")}
for _a in range(1996, 2026):
    _pg = f"mex{(_a + 1) % 100:02d}" if _a + 1 < 2010 else ("mex2-2010" if _a + 1 == 2010 else f"mex{_a + 1}")
    _t1, _t2 = ("Invierno", "Verano") if _a < 2002 else ("Apertura", "Clausura")
    _tr1, _tr2 = _dois_torneios(_pg, _t1, _t2)
    _liga = "Primera División de México" if _a < 2012 else "Liga MX"
    for _ano, _tor, _tr in ((_a, _t1, _tr1), (_a + 1, _t2, _tr2)):
        _t = f"{_ano} {_tor}"
        EDICOES.append(_e(_t, _ano, _ano, _tr, _NOMES_TORNEIO.get(_t, f"{_liga} {_tor} {_ano}"), espn=_ESPN.get(_t),
                          hist=f"{_tor} {_ano}",
                          sem_campeao="torneio cancelado na 10ª rodada pela pandemia de covid-19, sem campeão; a classificação "
                                      "é a tabela do cancelamento" if _t == "2020 Clausura" else ""))
