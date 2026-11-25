"""Lê os jogos e as tabelas de cada edição nas páginas da RSSSF (data/coleta/png-1/rsssf/), trecho a trecho (edicoes.py),
com o leitor comum (rsssf_oce.ler).

- ida e volta numa linha só vira dois jogos;
- jogos sem placar ("bt", "lt", "drw", "-", "ppd", "n/p") ficam de fora (salvo os de explicacoes.CORRIGE);
- a mesma tabela repetida no topo e no fim do trecho entra uma vez; a do meio da temporada e as de
  explicacoes.TABELAS_FORA não servem de conferência.

Uso como biblioteca: ler(edicao) -> (jogos, tabelas); campeoes() -> {temporada da lista: (campeão, vice, None)}.
Uso direto: python coleta/png-1/ler.py [temporada ...]
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
    # data com estádio e cidade ("[May 6, Laiwaden Oval, Madang]", "Semifinals [Mar 14, Lloyd Robson Oval, Port Moresby]"):
    # fica só a data, que o leitor comum reconhece (sem isso a linha vira "autores" do jogo de cima)
    ls = [re.sub(r"\[((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2})(?:,[^\]]*)?\]", r"[\1]", l) for l in ls]
    # cabeçalho do mata-mata com a data ("Semifinals [Mar 14]", "Third Place Match [Mar 28]"): fica só a data (a fase vem do
    # trecho em edicoes.py), para o leitor comum datar os jogos de baixo
    ls = [re.sub(r"^(?:Semi-?finals?|Third Place Match|3rd Place Match|(?:Grand )?Final|Quarter-?finals?)\s*(?=\[[A-Z][a-z]+ \d{1,2}\]\s*$)",
                 "", l) for l in ls]
    out = []
    for l in ls:   # ida e volta numa linha: "AS Poum         0-1 3-1 Wé-Luecilla"
        m = re.match(r"^(\S.*?)\s+(\d{1,2})-(\d{1,2})\s+(\d{1,2})-(\d{1,2})\s+([^\d\s\[].*?)\s*$", l)
        if m:
            out += [f"{m.group(1)}  {m.group(2)}-{m.group(3)}  {m.group(6)}", f"{m.group(6)}  {m.group(5)}-{m.group(4)}  {m.group(1)}"]
        else:
            out.append(l)
    ls = out
    # nota que continua na linha de baixo, à direita da data ou do "Round N" ("[Nov 23]        to fading light]"): o pedaço
    # volta para a linha de cima, e a data (ou a rodada) fica sozinha, para o leitor comum
    for k in range(1, len(ls)):
        m = re.match(r"^((?:Round \d+\s*)?\[[A-Z][a-z]{2} \d{1,2}\]|Round \d+)\s{5,}(\S.*\])\s*$", ls[k])
        if m and "[" in ls[k - 1] and not ls[k - 1].rstrip().endswith("]"):
            ls[k - 1] = ls[k - 1].rstrip() + " " + m.group(2)
            ls[k] = m.group(1)
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


_LINHA_SOLTA = re.compile(r"^\s*(\d{1,2})\.\s*(\S.*?)\s+(\d{1,2})\s+(\d{1,2})\s+(\d{1,2})\s+(\d{1,2})\s+(\d{1,3})\s*-\s*(\d{1,3})\s+(\d{1,3})(.*)$")


def _tabelas_inteiras(trecho: list[str], tabs: list) -> list:
    """Linha de tabela com erro de digitação (vitórias + empates + derrotas diferente de jogos: "7.Navua  16 4 4 10 ...") é
    descartada pelo leitor comum e corta a tabela em duas. Aqui a tabela é relida do começo ao fim, aceitando essas linhas
    (com a nota na observação); o pedaço que sobrava depois dela sai."""
    out, usadas = [], set()
    for tb in tabs:
        if tb.linha in usadas:
            continue
        k, linhas_tb = tb.linha, []
        while k < len(trecho):
            s = trecho[k]
            r = rsssf_oce.linha_tabela(s)
            m = None if r else _LINHA_SOLTA.match(s)
            if r:
                linhas_tb.append(r)
            elif m:
                j_, v, e_, d_ = (int(m.group(n)) for n in (3, 4, 5, 6))
                linhas_tb.append({"pos": int(m.group(1)), "nome": m.group(2).strip(), "cidade": None, "j": j_, "v": v, "e": e_,
                                  "d": d_, "gp": int(m.group(7)), "gc": int(m.group(8)), "pts": int(m.group(9)),
                                  "obs": (m.group(10).strip() + " " if m.group(10).strip() else "") +
                                         "(vitórias + empates + derrotas não fecham com os jogos na página)"})
            elif not re.match(r"^[\s\-=_]*$", s) or not s.strip() and (k + 1 >= len(trecho) or not (
                    rsssf_oce.linha_tabela(trecho[k + 1]) or _LINHA_SOLTA.match(trecho[k + 1]))):
                break
            usadas.add(k)
            k += 1
        tb.linhas = linhas_tb or tb.linhas
        out.append(tb)
    return out


CORTE = {"2019/20": 12}   # mês a partir do qual a data é do 1º ano (2019/20: de dezembro de 2019 a outubro de 2020)
OGOL_JOGOS: set[str] = set()   # temporadas em que os jogos vêm do ogol (nenhuma em PNG)
_TAB_PARCIAL = re.compile(r"halfway|top of table|half-way|after round|\(\w{3} \d", re.I)


def ler(e: Edicao) -> tuple[list[J], list[T]]:
    from explicacoes import CORRIGE, TABELAS_FORA
    jogos: list[J] = []
    tabelas: list[T] = []
    for pg, ini, fim, fase, grupo in e.trechos:
        ls = linhas(pg)
        trecho = list(ls[ini:fim])
        lidos, tabs = rsssf_oce.ler(trecho, e.ano_inicio, e.ano_fim)
        tabs = _tabelas_inteiras(trecho, tabs)
        vistos = set()
        for tb in tabs:
            chave_tb = tuple((r["nome"], r["j"], r["gp"], r["gc"]) for r in tb.linhas)
            if chave_tb in vistos or (pg, ini + tb.linha) in TABELAS_FORA or _TAB_PARCIAL.search(tb.secao or ""):
                continue
            vistos.add(chave_tb)
            tabelas.append(T(pg, ini + tb.linha, fase, grupo or tb.grupo, tb.linhas, tb.secao))
        for j in lidos:
            if j.gm is None and j.especial not in ("wo_m", "wo_v", "awd") and (pg, ini + j.linha) not in CORRIGE:
                continue   # sem placar ("bt", "lt", "drw", "-", "ppd", "n/p"), salvo os de explicacoes.CORRIGE
            data = j.data
            gt, nota = j.gols_texto, j.nota
            if re.fullmatch(r"\s*\[?\s*(date|[A-Z][a-z]{2} \d{1,2})\?\s*\]?\s*", gt or ""):
                gt = ""   # "[date?]", "[Nov 26?]" embaixo do jogo: data incerta, não autores
            elif re.search(r"'keeper|during the match", gt or ""):
                gt, nota = "", (nota + "; " + gt.strip("[] ")).strip("; ")   # nota, não autores
            jogos.append(J(pg, ini + j.linha, fase, grupo or j.grupo, j.mandante, j.visitante, j.gm, j.gv, j.rodada, data, j.especial,
                           nota, j.local, gt, j.pen_m, j.pen_v, j.prorrogacao, j.gm_of, j.gv_of))
    if e.temporada in OGOL_JOGOS:   # a RSSSF só tem a tabela: os jogos vêm do ogol (todos da fase única)
        import json
        for x in json.loads((PASTA_DADOS / "ogol" / f"{e.temporada}.json").read_text(encoding="utf-8")):
            if x["gols_mandante"] is not None:
                jogos.append(J("ogol", int(x["id"]), "Fase única", "", x["mandante"], x["visitante"], x["gols_mandante"],
                               x["gols_visitante"], data=x["data"], origem="ogol"))
    if any(f == "Fase de grupos" for _, _, _, f, _ in e.trechos):   # rodadas com os dois grupos juntos (2025): grupo pelos clubes
        from clubes_png import clube
        grupo_de = {clube(r["nome"], e.ano_inicio): t.grupo for t in tabelas if t.fase == "Fase de grupos" for r in t.linhas}
        for j in jogos:
            if j.fase == "Fase de grupos":
                j.grupo = grupo_de.get(clube(j.mandante, e.ano_inicio), j.grupo)
    if not e.trechos:
        jogos += final_lista(e)
    saida = []
    for j in jogos:
        c = CORRIGE.get((j.pagina, j.linha, j.mandante, j.visitante), CORRIGE.get((j.pagina, j.linha), ...))
        if c is None:
            continue
        if c is not ...:
            for campo, valor in c[0].items():
                setattr(j, campo, valor)
            j.correcao = c[1]
        if j.data and e.ano_fim > e.ano_inicio:   # temporada que cruza o ano: julho-dezembro no 1º ano (2019/20: só dezembro)
            j.data = f"{e.ano_inicio if int(j.data[5:7]) >= CORTE.get(e.temporada, 7) else e.ano_fim}{j.data[4:]}"
        elif j.data:
            j.data = f"{e.ano_inicio}{j.data[4:]}"
        saida.append(j)
    return saida, tabelas


def campeoes() -> dict[str, tuple[str, str | None, str | None]]:
    """Lista de campeões da National Soccer League na RSSSF (pngchamp.html): temporada -> (campeão, vice da final, None)."""
    out = {}
    ls = rsssf_oce.texto(PASTA / "pngchamp.html")
    ini = next(i for i, l in enumerate(ls) if l.startswith("National Soccer League"))
    for l in ls[ini:]:
        if l.startswith("NB: 2008/09") or l.startswith("Number of Wins"):
            break
        m = re.match(r"^(\d{4}(?:/\d{2})?)\s+(\S.*?)(?:\s+(?:\d+-\d+|n/p|abd|bt)\s+|\s{3,})(\S.*?)?\s*(\[.*\])?\s*$", l)
        if m:
            out[m.group(1)] = (m.group(2).strip(), (m.group(3) or "").strip() or None, None)
    return out


def final_lista(e: Edicao) -> list[J]:
    return []


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
