"""Lê os jogos e as tabelas de cada edição nas páginas da RSSSF (data/coleta/tah-1/rsssf/), trecho a trecho (edicoes.py),
com o leitor comum (rsssf_oce.ler).

- "Faa'a" vira "Faaa" antes da leitura (o apóstrofo no fim do nome do mandante confunde o leitor com um minuto: "87'");
- jogos sem placar ("bt", "lt", "drw", "-", "ppd", "6-?") ficam de fora;
- a mesma tabela repetida no topo e no fim do trecho entra uma vez; a do meio da temporada ("Halfway Table", "Top of
  table") e as de explicacoes.TABELAS_FORA não servem de conferência.

Uso como biblioteca: ler(edicao) -> (jogos, tabelas); campeoes() -> {ano da lista: campeão}.
Uso direto: python coleta/tah-1/ler.py [temporada ...]
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-oceania"))
sys.path.insert(0, str(AQUI))
import rsssf_oce  # noqa: E402
from edicoes import EDICOES, PASTA_DADOS, Edicao  # noqa: E402

PASTA = PASTA_DADOS / "rsssf"


@dataclass
class J:
    pagina: str
    linha: int
    fase: str
    grupo: str
    mandante: str
    visitante: str
    gm: int | None
    gv: int | None
    rodada: int | None = None
    data: str | None = None
    especial: str = ""
    nota: str = ""
    local: str | None = None
    gols_texto: str = ""
    pen_m: int | None = None
    pen_v: int | None = None
    prorrogacao: bool = False
    gm_of: int | None = None
    gv_of: int | None = None
    origem: str = "rodadas"
    correcao: str = ""
    nome_m: str = ""
    nome_v: str = ""


@dataclass
class T:
    pagina: str
    linha: int
    fase: str
    grupo: str
    linhas: list[dict] = field(default_factory=list)
    titulo: str = ""


@lru_cache(maxsize=None)
def linhas(pagina: str) -> tuple[str, ...]:
    """Texto puro da página, com os erros de digitação corrigidos (explicacoes.CONSERTA_TEXTO, cada um com o motivo)."""
    from explicacoes import CONSERTA_TEXTO
    ls = [l.replace("–", "-").replace("—", "-") for l in rsssf_oce.texto(PASTA / f"{pagina}.html")]
    ls = [re.sub(r"Faa['’¹]a", "Faaa", l) for l in ls]
    for (pg, n), (antes, depois, _motivo) in CONSERTA_TEXTO.items():
        if pg == pagina:
            assert antes in ls[n], f"{pagina}:{n} mudou: {ls[n]!r}"
            ls[n] = ls[n].replace(antes, depois)
    # autores que continuam na linha de baixo: numa linha só
    for k, l in enumerate(ls):
        s = l.strip()
        if s.startswith("[") and "]" not in s and re.search(r"\d'?\s*(,|-)?\s*$|\s-\s*$|,\s*$", s):
            n = k + 1
            while n < len(ls) and n <= k + 4 and ls[n].strip() and not rsssf_oce._jogo(ls[n]):
                ls[k] = ls[k].rstrip() + " " + ls[n].strip()
                fecha = "]" in ls[n]
                ls[n] = ""
                n += 1
                if fecha:
                    break
    return tuple(ls)


_TAB_PARCIAL = re.compile(r"halfway|top of table|half-way|after round|\(\w{3} \d", re.I)


def ler(e: Edicao) -> tuple[list[J], list[T]]:
    from explicacoes import CORRIGE, TABELAS_FORA
    jogos: list[J] = []
    tabelas: list[T] = []
    for pg, ini, fim, fase, grupo in e.trechos:
        ls = linhas(pg)
        trecho = list(ls[ini:fim])
        lidos, tabs = rsssf_oce.ler(trecho, e.ano_inicio, e.ano_fim)
        vistos = set()
        for tb in tabs:
            chave_tb = tuple((r["nome"], r["j"], r["gp"], r["gc"]) for r in tb.linhas)
            if chave_tb in vistos or (pg, ini + tb.linha) in TABELAS_FORA or _TAB_PARCIAL.search(tb.secao or ""):
                continue
            vistos.add(chave_tb)
            tabelas.append(T(pg, ini + tb.linha, fase, grupo, tb.linhas, tb.secao))
        for j in lidos:
            if j.gm is None and j.especial not in ("wo_m", "wo_v", "awd"):
                continue   # sem placar ("bt", "lt", "-", "ppd", "n/p")
            data = j.data
            jogos.append(J(pg, ini + j.linha, fase, grupo, j.mandante, j.visitante, j.gm, j.gv, j.rodada, data, j.especial,
                           j.nota, j.local, j.gols_texto, j.pen_m, j.pen_v, j.prorrogacao, j.gm_of, j.gv_of))
    saida = []
    for j in jogos:
        c = CORRIGE.get((j.pagina, j.linha, j.mandante, j.visitante), CORRIGE.get((j.pagina, j.linha), ...))
        if c is None:
            continue
        if c is not ...:
            for campo, valor in c[0].items():
                setattr(j, campo, valor)
            j.correcao = c[1]
        if j.data and e.ano_fim > e.ano_inicio:   # temporada que cruza o ano: julho-dezembro no 1º ano
            j.data = f"{e.ano_inicio if int(j.data[5:7]) >= 7 else e.ano_fim}{j.data[4:]}"
        elif j.data:
            j.data = f"{e.ano_inicio}{j.data[4:]}"
        saida.append(j)
    return saida, tabelas


def campeoes() -> dict[int, str]:
    """Lista de campeões da RSSSF: ano da lista -> campeão (sem a cidade)."""
    ls = rsssf_oce.texto(PASTA / "tahitichamp.html")
    out = {}
    for l in ls:
        m = re.match(r"^(\d{4})\s+(\S.*?)\s*(?:\[\*\])?\s*$", l)
        if m and not l.strip().endswith(("known", "held")):
            out[int(m.group(1))] = re.sub(r"\s*\([^)]*\)\s*$", "", m.group(2)).strip()
    return out


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    pedidas = set(sys.argv[1:])
    for e in EDICOES:
        if (pedidas and e.temporada not in pedidas) or not e.trechos:
            continue
        jogos, tabelas = ler(e)
        por_fase: dict[str, int] = {}
        for j in jogos:
            por_fase[j.fase] = por_fase.get(j.fase, 0) + 1
        print(e.temporada, len(jogos), por_fase, "tabelas:", [(t.fase, len(t.linhas), t.linha) for t in tabelas])


if __name__ == "__main__":
    main()
