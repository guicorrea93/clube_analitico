"""Edições da 1ª divisão boliviana (bol-1): uma por título, de 1950 a 2025, como na lista de campeões da Wikipédia em inglês
("FBF División Profesional") e na contagem de 93 campeonatos da RSSSF (bolchamp.html).

- 1950-1953: liga de La Paz, semiprofissional desde 1950 (antes dela, a liga amadora de La Paz fica de fora, como na
  Wikipédia);
- 1954-1957: Torneo Integrado (La Paz, Oruro e Cochabamba);
- 1957 Mixto: Certamen Nacional Mixto 1957/58 (clubes de Cochabamba e Oruro), título à parte;
- 1958-1976: campeonato nacional (Torneo Nacional 1958-1959; Copa Simón Bolívar de 1960 a 1976); sem campeonato em 1962.
  De 1960 a 1976 os campeonatos regionais (o de La Paz e os outros) eram a fase classificatória e ficam de fora;
- 1977 em diante: liga profissional (LFPB, desde 2018 FBF División Profesional). Até 2002 um campeão por ano (Apertura e
  Clausura são fases); de 2003 a 2019 e em 2022, Apertura, Clausura e Adecuación dão título cada um (uma edição cada;
  2005 Apertura é o Apertura 2005/06, abortado; 2011/12 e 2016/17 no calendário europeu). 2022 Clausura foi abandonado
  (edição sem campeão). 2020, 2021 e 2023-2025: um campeão por ano.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)], linhas do texto puro (rsssf_sul.texto); linha final None: até o
  primeiro título de outra competição (FIM_PADRAO). 1971, 1977, 1992-1994 e 1995 em diante;
- wiki: ano da página da Wikipédia em espanhol (wikipedia_jogos.py): 1950 e 1953 completos; 1990 e 1991 quase completos;
  só a fase final em 1951, 1960, 1966, 1968, 1976, 1978, 1979, 1982, 1983 e 1985-1989;
- tabelas: a seção do ano em bolhist.html (tabelas finais de 1950 a 1990): de 1965 a 1976 só a parte "(Nacional)";
- espn: datas dos jogos que vêm da ESPN (nenhuma edição precisa: a RSSSF tem os jogos de 1995 em diante).
Nas edições com jogos incompletos (incompleta), a classificação é a tabela publicada, sem conferência.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "bol-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# título que encerra o trecho da 1ª divisão numa página de temporada (quando a edição não diz a linha final)
FIM_PADRAO = (r"^(Promotion/Relegation|Promotion Playoff|Relegation( Table| Averages| Playoffs?)?:?\s*$|Relegation\s{3,}|"
              r"Second Level|Nacional B|Copa Bolivia|Copa Sim[oó]n Bol[ií]var|Copa de la Divisi|Copa Pace|"
              r"Copa Sudamericana|Copa Libertadores Playoff|Playoff for 3rd Copa|Playoff for Copa|Copa Conmebol|"
              r"Torneo Play Off de la Liga|Playoff against Direct Relegation|About this document)")


@dataclass
class Edicao:
    temporada: str                      # "1950", "1957 Mixto", "2003 Apertura", "2011/12 Adecuación"
    ano_inicio: int
    ano_fim: int
    trechos: list[tuple[str, int, int | None]]
    nome_oficial: str
    campeao_rsssf: str = ""
    obs: str = ""
    fases: list[tuple[str, str]] = field(default_factory=list)
    nomes: dict[str, str] = field(default_factory=dict)
    soma_de: list[str] = field(default_factory=list)              # (não usado)
    wiki: str | None = None                                       # ano da página da Wikipédia em espanhol com os jogos
    hist: str = ""                                                # (não usado)
    ogol: int | None = None                                       # (não usado: o ogol não tem os jogos antigos)
    espn: tuple[str, str] | None = None                           # datas dos jogos que vêm da ESPN
    espn_fases: list[tuple[str, str]] = field(default_factory=list)
    tabelas: list[tuple[str, int, int | None]] = field(default_factory=list)   # trechos lidos só pelas tabelas
    parcial: tuple[str, int, int] | None = None                    # (não usado)
    incompleta: str = ""                                           # o que falta nos jogos (entra na observação)

    @property
    def pontos_vitoria(self) -> int:
        """2 por vitória até 1994; 3 a partir de 1995."""
        return 3 if self.ano_inicio >= 1995 else 2

    @property
    def sem_jogos(self) -> bool:
        return not self.trechos and self.wiki is None and self.espn is None


@lru_cache(maxsize=None)
def secao_hist(temporada: str) -> tuple[str, int, int] | None:
    """(página, início, fim) da seção da edição em bolhist.html: "La Paz 1950:", "Torneo Integrado 1954:", "Torneo Mixto
    1957:", "Nacional 1958:"; de 1965 a 1976 a parte "(Nacional):" do ano; de 1977 em diante o ano inteiro ("1977:")."""
    sys.path.insert(0, str(RAIZ / "coleta" / "comum-sulamerica"))
    import rsssf_sul
    ls = [l.strip() for l in rsssf_sul.texto(PASTA_DADOS / "rsssf" / "bolhist.html")]
    ano = int(temporada[:4])
    inicio_ano = r"^((La Paz|Torneo Integrado|Torneo Mixto|Nacional) \d{4}:|\d{4}:|About this document)$"
    if temporada == "1957 Mixto":
        alvo = "Torneo Mixto 1957:"
    elif ano <= 1953:
        alvo = f"La Paz {ano}:"
    elif ano <= 1957:
        alvo = f"Torneo Integrado {ano}:"
    elif ano <= 1959:
        alvo = f"Nacional {ano}:"
    elif ano <= 1964:
        return None   # a página só tem a liga de La Paz desses anos, não o nacional
    else:
        alvo = f"{ano}:"
    if alvo not in ls:
        return None
    ini = ls.index(alvo)
    fim = next((i for i in range(ini + 1, len(ls)) if re.match(inicio_ano, ls[i])), len(ls))
    if 1965 <= ano <= 1976:
        nac = next((i for i in range(ini, fim) if ls[i] == "(Nacional):"), None)
        if nac is None:
            return None
        ini = nac
    return "bolhist", ini, fim


def _e(temporada, ini, fim, trechos, nome, campeao="", obs="", **kw):
    return Edicao(temporada, ini, fim, trechos, nome, campeao, obs, **kw)


def _nome(a: int) -> str:
    if a <= 1953:
        return f"Campeonato de La Paz {a}"
    if a <= 1957:
        return f"Torneo Integrado {a}"
    if a <= 1959:
        return f"Torneo Nacional {a}"
    if a <= 1976:
        return f"Copa Simón Bolívar {a}"
    if a <= 2017:
        return f"Liga de Fútbol Profesional Boliviano {a}"
    return f"División Profesional {a}"


_WIKI_COMPLETO = {1950, 1953, 1990, 1991}
_WIKI_PARCIAL = {1951, 1960, 1966, 1968, 1976, 1978, 1979, 1982, 1983, 1985, 1986, 1987, 1988, 1989}
_PAGINA = {1971: "bol71", 1977: "bol77", 1992: "bol92", 1993: "bol93", 1994: "bol94"}
# trechos explícitos: a página tem outra competição no meio (playoff da Libertadores, rebaixamento antes da fase final)
_TRECHOS: dict[str, list[tuple[str, int, int | None]]] = {
    "1992": [("bol92", 36, None)],   # a tabela de confrontos do topo ("Partial results") tem células vazias: fica de fora
    "1993": [("bol93", 0, 207)], "1994": [("bol94", 0, 125)],   # "Relegation Section" faz parte da temporada
    "1996": [("bol96", 0, 519), ("bol96", 544, None)],
    "1997": [("bol97", 0, 485), ("bol97", 511, None)],
    "1998": [("bol98", 0, 635), ("bol98", 646, 761)],
    "2000": [("bol00", 0, 790), ("bol00", 803, 851)],
    "2001": [("bol01", 0, 656), ("bol01", 678, None)],
    "2003 Apertura": [("bol03", 13, 445)], "2003 Clausura": [("bol03", 470, None)],
    "2004 Apertura": [("bol04", 12, 460)], "2004 Clausura": [("bol04", 474, None)],
    "2005 Adecuación": [("bol05", 12, 483)], "2005 Apertura": [("bol05", 483, None)],
    "2006 Apertura": [("bol06", 16, 458)], "2006 Clausura": [("bol06", 458, None)],
    "2007 Apertura": [("bol07", 16, 476)], "2007 Clausura": [("bol07", 476, None)],
    "2008 Apertura": [("bol08", 12, 459)], "2008 Clausura": [("bol08", 459, None)],
    "2009 Apertura": [("bol09", 23, 471)], "2009 Clausura": [("bol09", 471, None)],
    "2010 Apertura": [("bol2010", 23, 545)], "2010 Clausura": [("bol2010", 661, None)],
    "2011/12 Adecuación": [("bol2012", 21, 412)], "2011/12 Apertura": [("bol2012", 412, 720)],
    "2011/12 Clausura": [("bol2012", 720, None)],
    "2012/13 Apertura": [("bol2013", 26, 430)], "2012/13 Clausura": [("bol2013", 436, None)],
    "2013/14 Apertura": [("bol2014", 26, 435)], "2013/14 Clausura": [("bol2014", 435, None)],
    "2014/15 Apertura": [("bol2015", 25, 434)], "2014/15 Clausura": [("bol2015", 434, None)],
    "2015/16 Apertura": [("bol2016", 25, 454)], "2015/16 Clausura": [("bol2016", 454, None)],
    "2016/17 Apertura": [("bol2017", 25, 440)], "2016/17 Adecuación": [("bol2017", 440, 894)],
    "2016/17 Clausura": [("bol2017", 894, None)],
    "2018 Apertura": [("bol2018", 24, 450)], "2018 Clausura": [("bol2018", 503, None)],
    "2019 Apertura": [("bol2019", 24, 616)], "2019 Clausura": [("bol2019", 616, None)],
    "2022 Apertura": [("bol2022", 24, 487)], "2022 Clausura": [("bol2022", 487, None)],
}
_FASES_ANO: dict[str, list[tuple[str, str]]] = {}
_INCOMPLETA = {
    1951: "só o desempate do título (Wikipédia em espanhol); o resto, só a tabela final da RSSSF",
    1960: "só a fase de grupos (Wikipédia em espanhol)",
    1966: "só a fase final (Wikipédia em espanhol)", 1968: "só a fase final (Wikipédia em espanhol)",
    1971: "só a fase final (RSSSF); a 1ª fase, só as tabelas",
    1976: "só a fase final (Wikipédia em espanhol)", 1978: "só a fase final (Wikipédia em espanhol)",
    1979: "só as finais (Wikipédia em espanhol)", 1982: "só as finais (Wikipédia em espanhol)",
    1983: "só as semifinais e finais (Wikipédia em espanhol)", 1985: "só as finais (Wikipédia em espanhol)",
    1986: "só as finais (Wikipédia em espanhol)", 1987: "só as finais (Wikipédia em espanhol)",
    1988: "só a final (Wikipédia em espanhol)", 1989: "só as finais (Wikipédia em espanhol)",
    1990: "jogos da Wikipédia em espanhol sem a divisão em fases das tabelas da RSSSF (1ª e 2ª fase de cada torneio); a "
          "classificação é a tabela da RSSSF",
    1991: "jogos da Wikipédia em espanhol (parte do Apertura e a final) sem a divisão em fases das tabelas da RSSSF; a "
          "classificação é a tabela da RSSSF",
    1992: "a RSSSF traz só as tabelas da maior parte das fases e os jogos finais",
    1993: "a RSSSF traz só as tabelas da 1ª fase e parte dos jogos",
    1994: "a RSSSF traz só as tabelas e os jogos das finais",
}
_SEM_JOGOS = "sem jogos: nenhuma fonte pública traz os jogos deste ano (só o campeão, o vice e a tabela final da RSSSF)"

EDICOES: list[Edicao] = []


def _anual(a: int, temporada: str | None = None, nome: str | None = None) -> Edicao:
    t = temporada or str(a)
    hist = [secao_hist(t)] if secao_hist(t) else []
    kw: dict = dict(tabelas=hist, incompleta=_INCOMPLETA.get(a, "") if not temporada else "",
                    fases=list(_FASES_ANO.get(t, [])))
    if t in _TRECHOS or a in _PAGINA or a >= 1995:
        pg = _PAGINA.get(a) or (f"bol{a % 100:02d}" if a < 2010 else f"bol{a}")
        kw["trechos"] = _TRECHOS.get(t, [(pg, 0, None)])
        if a in _PAGINA and a != 1977:
            kw["tabelas"] = hist
        elif a >= 1977:
            kw["tabelas"] = []
    else:
        kw["trechos"] = []
    if a in _WIKI_COMPLETO | _WIKI_PARCIAL and not temporada:
        kw["wiki"] = str(a)
        if a in (1990, 1991):   # a página da RSSSF tem poucos jogos: ficam os da Wikipédia; as tabelas da RSSSF conferem
            kw["tabelas"] = [(f"bol{a % 100}", 0, None)]
    obs = _SEM_JOGOS if not kw["trechos"] and "wiki" not in kw else ""
    return _e(t, a, a, kw.pop("trechos"), nome or _nome(a), obs=obs, **kw)


for _a in range(1950, 2026):
    if _a == 1962:   # sem campeonato nacional (a liga de La Paz de 1962 não conta como título)
        continue
    if _a <= 2002 or _a in (2020, 2021, 2023, 2024, 2025):
        EDICOES.append(_anual(_a))
        if _a == 1957:
            EDICOES.append(_anual(1957, "1957 Mixto", "Certamen Nacional Mixto 1957/58"))
        continue
    if _a in (2011, 2012, 2013, 2014, 2015, 2016):
        tor = ["Adecuación", "Apertura", "Clausura"] if _a == 2011 else ["Apertura", "Clausura"]
        if _a == 2016:
            tor = ["Apertura", "Adecuación", "Clausura"]
        base = f"{_a}/{(_a + 1) % 100:02d}"
        for t in tor:
            EDICOES.append(_e(f"{base} {t}", _a, _a + 1, _TRECHOS[f"{base} {t}"], f"{_nome(_a)}/{(_a + 1) % 100:02d} – {t}"))
        continue
    if _a == 2017:
        continue   # 2016/17
    tor = ["Adecuación", "Apertura"] if _a == 2005 else ["Apertura", "Clausura"]
    for t in tor:
        EDICOES.append(_e(f"{_a} {t}", _a, _a, _TRECHOS[f"{_a} {t}"], f"{_nome(_a)} – {t}",
                          obs="abandonado (protestos no departamento de Santa Cruz): sem campeão" if (_a, t) == (2022, "Clausura")
                          else ""))
