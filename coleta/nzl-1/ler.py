"""Lê os jogos e as tabelas de cada edição nas páginas da RSSSF (data/coleta/nzl-1/rsssf/), trecho a trecho (edicoes.py).

- Matriz de resultados (1970-1995 e ligas regionais): cabeçalho com siglas e uma linha por clube (mandante), com uma célula
  por adversário na ordem das linhas; "-" na diagonal. O nome da linha vem abreviado ("Well Utd", "N Shore"): casa com o
  nome da tabela do mesmo trecho. Com matriz no trecho, os jogos saem dela (as rodadas da página, quando há, só dão o número
  da rodada).
- Rodadas (demais trechos): leitor comum (rsssf_oce.ler), com data, rodada e autores dos gols.
- 1996 e 1996/97: o placar vem com o do intervalo entre parênteses ("Waitakere City  5(2)  Miramar Rangers  2(1)") e os
  autores em duas colunas abaixo; linhas() reescreve no formato de sempre.

Uso como biblioteca: ler(edicao) -> (jogos, tabelas); campeoes() -> {temporada: (campeão, vice)} da lista da RSSSF.
Uso direto: python coleta/nzl-1/ler.py [temporada ...]   (resumo por edição)
"""
from __future__ import annotations

import difflib
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
    """Jogo lido: nomes como na página."""
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
    origem: str = "rodadas"       # "matriz", "rodadas", "ogol" ou "wikipedia"
    correcao: str = ""            # motivo da correção (explicacoes.CORRIGE)
    nome_m: str = ""              # nomes como na fonte (antes de virar o nome de exibição)
    nome_v: str = ""


@dataclass
class T:
    """Tabela publicada no trecho."""
    pagina: str
    linha: int
    fase: str
    grupo: str
    linhas: list[dict] = field(default_factory=list)
    titulo: str = ""


_HT = re.compile(r"^(?P<a>\S.*?)\s+(?P<ga>\d{1,2})\((?P<ha>[\d?])\)\s+(?P<b>\S.*?)\s+(?P<gb>\d{1,2})\((?P<hb>[\d?])\)(?P<resto>.*)$")


def _ht(ls: list[str]) -> list[str]:
    """Placar com o do intervalo ("5(2)") e autores em duas colunas abaixo -> "A  5-2  B  [pens]" + "[autores A - autores B]"."""
    out = list(ls)
    k = 0
    while k < len(out):
        m = _HT.match(out[k])
        if not m:
            k += 1
            continue
        col_b = out[k].index(m.group("b"), len(m.group("a")) + 2)   # coluna onde começa o visitante (e os autores dele)
        resto = m.group("resto").strip()
        out[k] = f"{m.group('a')}  {m.group('ga')}-{m.group('gb')}  {m.group('b')}" + (f"  [{resto}]" if resto else "")
        casa, fora, n = [], [], k + 1
        while n < len(out) and out[n].strip() and not _HT.match(out[n]) and not re.match(r"^\s*(Round|Semi|Major|Minor|Prelim|Grand|Final|\d+ \w+ 19)", out[n]):
            l = out[n]
            esq, dir_ = l[:col_b].strip(), l[col_b:].strip() if len(l) > col_b else ""
            if esq:
                casa.append(esq)
            if dir_:
                fora.append(dir_)
            out[n] = ""
            n += 1
        if casa or fora:
            out[k + 1] = "[" + ", ".join(casa) + " - " + ", ".join(fora) + "]"
        k = n
    return out


@lru_cache(maxsize=None)
def linhas(pagina: str) -> tuple[str, ...]:
    """Texto puro da página, com os erros de digitação corrigidos (explicacoes.CONSERTA_TEXTO, cada um com o motivo)."""
    from explicacoes import CONSERTA_TEXTO
    ls = [l.replace("–", "-").replace("—", "-") for l in rsssf_oce.texto(PASTA / f"{pagina}.html")]
    # "FC Twenty 11" (2023-2024): o número no nome quebra a linha da tabela
    ls = [l.replace("Twenty 11", "Twenty-11") for l in ls]
    for (pg, n), (antes, depois, _motivo) in CONSERTA_TEXTO.items():
        if pg == pagina:
            assert antes in ls[n], f"{pagina}:{n} mudou: {ls[n]!r}"
            ls[n] = ls[n].replace(antes, depois)
    # autores que continuam na linha de baixo (" [Grant Young 45+2', Keryn Jordan 63', ... -" / "  Stuart Kelly 59']"): numa linha só
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
    if pagina in ("nz96", "nz97"):
        ls = [re.sub(r"^Round (\d+)[ab] -", r"Round \1 -", l) for l in ls]   # "Round 10a" / "Round 10b" (jogos adiados)
        ls = _ht(ls)
    return tuple(ls)


# ------------------------------------------------------------------------------------------------ matriz de resultados

_CAB = re.compile(r"^\s{3,}((?:[A-Za-z][A-Za-z.']{1,4}\s+){2,}[A-Za-z][A-Za-z.']{1,4})\s*$")
_CEL = re.compile(r"^(-|x+|\d{1,2}-\d{1,2}|n/p|---|\?-\?)$", re.I)


def matrizes(ls: tuple[str, ...], ini: int, fim: int) -> list[tuple[int, list[tuple[int, str, list[str]]]]]:
    """[(linha do cabeçalho, [(linha, nome da linha, células)])] das matrizes do trecho."""
    out = []
    i = ini
    while i < fim:
        m = _CAB.match(ls[i])
        if not m:
            i += 1
            continue
        n = len(m.group(1).split())
        rows, k = [], i + 1
        while k < fim and len(rows) < n:
            toks = ls[k].split()
            if not toks:
                k += 1
                continue
            cels = []
            while toks and _CEL.match(toks[-1]) and len(cels) < n:
                cels.insert(0, toks.pop())
            if len(cels) != n or not toks:
                break
            rows.append((k, " ".join(toks), cels))
            k += 1
        if len(rows) == n:
            out.append((i, rows))
        i = k
    return out


def _parecido(a: str, b: str) -> float:
    """Quanto o nome abreviado da matriz (a) se parece com o nome da tabela (b): fração das palavras de a que começam uma
    palavra de b ("Well Utd" ~ "Wellington Utd"; "Chch Tech" ~ "Christchurch Tech")."""
    ka = rsssf_oce.chave(a.replace("Chch", "Christchurch").replace("Auck ", "Auckland ").replace("Wgtn", "Wellington")).split()
    kb = rsssf_oce.chave(b).split()
    if not ka:
        return 0.0
    ok = sum(1 for p in ka if any(w.startswith(p) or (len(p) >= 4 and p.startswith(w[:4])) for w in kb))
    # erro de digitação ("Mirmar Rangers"): semelhança das letras
    letras = difflib.SequenceMatcher(None, " ".join(ka), " ".join(kb)).ratio()
    return max(ok / len(ka), letras - 0.2) + (0.01 if ka[0] and kb and kb[0].startswith(ka[0]) else 0)


def casar_matriz(nomes: list[str], tabela: list[str]) -> dict[str, str]:
    """Nome da linha da matriz -> nome da tabela (o mais parecido, um para um)."""
    from explicacoes import MATRIZ_NOME
    pares = sorted(((_parecido(a, b), a, b) for a in nomes for b in tabela), reverse=True)
    res: dict[str, str] = {a: MATRIZ_NOME[a] for a in nomes if a in MATRIZ_NOME}
    usados = set(res.values())
    for s, a, b in pares:
        if a in res or b in usados or s < 0.5:
            continue
        res[a], usados = b, usados | {b}
    falta = [a for a in nomes if a not in res]
    if falta:
        raise ValueError(f"matriz: sem nome na tabela para {falta} (tabela: {tabela})")
    return res


# ------------------------------------------------------------------------------------------------ edição

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
            if chave_tb in vistos or (pg, ini + tb.linha) in TABELAS_FORA:
                continue   # a mesma tabela repetida no topo e no fim da página
            vistos.add(chave_tb)
            if pg in ("nz96", "nz97"):   # colunas P W D L F A B Pts: o leitor comum toma o bônus (B) pelos pontos
                for r in tb.linhas:
                    l = next(x for x in trecho[tb.linha:] if x.strip().startswith(r["nome"]))
                    r["pts"] = int(l.split()[-1])
            tabelas.append(T(pg, ini + tb.linha, fase, grupo, tb.linhas, tb.secao))
        mats = matrizes(ls, ini, fim)
        if mats:
            # nomes da tabela do mesmo trecho (a de mais linhas)
            nomes_tab = max((t.linhas for t in tabelas if t.pagina == pg and ini <= t.linha < fim), key=len, default=[])
            from clubes_nzl import clube
            # rodada do jogo: só quando a lista de rodadas traz o mesmo mando e o mesmo placar da matriz (1987)
            rodada_de = {(clube(j.mandante, e.ano_inicio), clube(j.visitante, e.ano_inicio), j.gm, j.gv): j.rodada
                         for j in lidos if j.rodada}
            for cab, rows in mats:
                nomes = casar_matriz([r[1] for r in rows], [r["nome"] for r in nomes_tab])
                ordem = [nomes[r[1]] for r in rows]
                for k, nome_row, cels in rows:
                    casa = nomes[nome_row]
                    for idx, (fora, c) in enumerate(zip(ordem, cels)):
                        mm = re.fullmatch(r"(\d{1,2})-(\d{1,2})", c)
                        if fora == casa:
                            assert not mm, f"{pg}:{k} diagonal com placar"
                            continue
                        if not mm:
                            continue
                        jogos.append(J(pg, k, fase, grupo, casa, fora, int(mm.group(1)), int(mm.group(2)),
                                       rodada=rodada_de.get((clube(casa, e.ano_inicio), clube(fora, e.ano_inicio),
                                                             int(mm.group(1)), int(mm.group(2)))), origem="matriz"))
        else:
            for j in lidos:
                if j.especial == "n/p" and j.gm is None:
                    continue   # adiado / não jogado ("p/p", "ppd", "-")
                data = j.data
                if data is None:   # data só no título logo acima ("Final [Dec 13, Newtown Park, Wellington]")
                    for l in trecho[max(0, j.linha - 3):j.linha][::-1]:
                        if "[" in l and (md := rsssf_oce.achar_data(l[l.index("["):])):
                            data = f"{e.ano_inicio:04d}-{md[0]:02d}-{md[1]:02d}"
                            break
                jogos.append(J(pg, ini + j.linha, fase, grupo, j.mandante, j.visitante, j.gm, j.gv, j.rodada, data, j.especial,
                               j.nota, j.local, j.gols_texto, j.pen_m, j.pen_v, j.prorrogacao, j.gm_of, j.gv_of))
    jogos += _ogol(e) + _wiki_regional(e) + _ogol_regional(e, tabelas)
    # correções com motivo (explicacoes.CORRIGE): (página, linha) -> campos novos; None descarta o jogo
    saida = []
    for j in jogos:
        c = CORRIGE.get((j.pagina, j.linha, j.mandante, j.visitante), CORRIGE.get((j.pagina, j.linha),
                        CORRIGE.get((j.pagina, e.temporada, j.mandante, j.visitante), ...)))
        if c is None:
            continue
        if c is not ...:
            for campo, valor in c[0].items():
                setattr(j, campo, valor)
            j.correcao = c[1]
        if j.data and e.ano_fim > e.ano_inicio:   # temporada que cruza o ano: julho-dezembro no 1º ano, janeiro-junho no 2º
            j.data = f"{e.ano_inicio if int(j.data[5:7]) >= 7 else e.ano_fim}{j.data[4:]}"
        elif j.data:
            j.data = f"{e.ano_inicio}{j.data[4:]}"
        saida.append(j)
    return saida, tabelas


def _ogol(e: Edicao) -> list[J]:
    """Fase de liga do ogol nas edições em que a RSSSF só tem as tabelas (2010/11 e 2011/12): os jogos com rodada ("R12")."""
    if not e.ogol:
        return []
    import json
    arq = PASTA_DADOS / "ogol" / f"{e.temporada.replace('/', '-')}.json"
    out = []
    for x in json.loads(arq.read_text(encoding="utf-8")):
        if x["rodada"] is None or x["gols_mandante"] is None:
            continue
        out.append(J("ogol", int(x["id"]), "Fase de liga", "", x["mandante"], x["visitante"], x["gols_mandante"], x["gols_visitante"],
                     rodada=x["rodada"], data=x["data"], origem="ogol"))
    return out


def _ogol_regional(e: Edicao, tabelas: list[T]) -> list[J]:
    """Liga regional cuja matriz da Wikipédia não serve (explicacoes.WIKI_FORA): os jogos do ogol entre os clubes da tabela
    da RSSSF daquele grupo (o calendário do ogol de 2025 traz as três ligas regionais e a fase nacional juntas)."""
    import json
    from clubes_nzl import clube
    from explicacoes import WIKI_FORA
    arq = PASTA_DADOS / "ogol" / f"{e.temporada.replace('/', '-')}.json"
    if not arq.exists() or not any(t == e.temporada for t, _ in WIKI_FORA):
        return []
    todos = json.loads(arq.read_text(encoding="utf-8"))
    grupo_de = {clube(r["nome"], e.ano_inicio): t.grupo for t in tabelas if t.fase == "Fase regional" for r in t.linhas}
    # a fase nacional começa no primeiro jogo entre clubes de regiões diferentes: dali em diante, nada é da liga regional
    inter = [x["data"] for x in todos if {grupo_de.get(clube(x["mandante"], e.ano_inicio)), grupo_de.get(clube(x["visitante"], e.ano_inicio))}
             >= {"Norte", "Centro"} or {grupo_de.get(clube(x["mandante"], e.ano_inicio)), grupo_de.get(clube(x["visitante"], e.ano_inicio))}
             >= {"Sul"} and len({grupo_de.get(clube(x["mandante"], e.ano_inicio)), grupo_de.get(clube(x["visitante"], e.ano_inicio))}) == 2]
    corte = min(inter) if inter else "9999"
    out = []
    for (temporada, reg) in WIKI_FORA:
        if temporada != e.temporada:
            continue
        clubes = {c for c, g in grupo_de.items() if g == reg}
        for x in todos:
            if x["gols_mandante"] is None or x["rodada"] is None or x["data"] >= corte:
                continue
            if clube(x["mandante"], e.ano_inicio) in clubes and clube(x["visitante"], e.ano_inicio) in clubes:
                out.append(J("ogol", int(x["id"]), "Fase regional", reg, x["mandante"], x["visitante"], x["gols_mandante"],
                             x["gols_visitante"], rodada=x["rodada"], data=x["data"], origem="ogol"))
    return out


_REGIAO_WIKI = {"Northern": "Norte", "Central": "Centro", "Southern": "Sul"}


def _wiki_regional(e: Edicao) -> list[J]:
    """Ligas regionais de 2022-2025 pela matriz de resultados da Wikipédia (a RSSSF só tem as tabelas). Sem data nem rodada."""
    if not any(f == "Fase regional" for _, _, _, f, _ in e.trechos) or e.ano_inicio < 2022:
        return []
    import wikipedia_nz
    from explicacoes import WIKI_FORA
    out = []
    for b in wikipedia_nz.resultados(e.temporada):
        reg = next((v for k, v in _REGIAO_WIKI.items() if b["secao"].startswith(k)), None)
        if reg is None or (e.temporada, reg) in WIKI_FORA:
            continue
        for k, (a, c, gm, gv, cel) in enumerate(b["jogos"]):
            out.append(J("wikipedia", k, "Fase regional", reg, a, c, gm, gv, nota=cel if re.search(r"[a-zA-Z]", cel) else "",
                         origem="wikipedia"))
    return out


# ------------------------------------------------------------------------------------------------ campeões

def campeoes() -> dict[str, tuple[str, str]]:
    """Lista de campeões nacionais da RSSSF (nzchamp.html): temporada -> (campeão, vice)."""
    ls = rsssf_oce.texto(PASTA / "nzchamp.html")
    ini = max(i for i, l in enumerate(ls) if l.startswith("National Champions since 1970"))
    out = {}
    for l in ls[ini:]:
        m = re.match(r"^[*#]?(\d{4}(?:/\d{2})?)\s+(\S.*?)\s{2,}(?:\d+\s+)?(\S.*?)(?:\s{2,}\d+)?(?:\s+\[.*\])?\s*$", l)
        if m and "cancel" not in l:
            casa, vice = m.group(2).strip(), re.sub(r"\s+\d+$", "", m.group(3).strip())
            out[m.group(1)] = (re.sub(r"\s+\d+$", "", casa), vice)
        if l.strip().startswith("*3 points"):
            break
    return out


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    pedidas = set(sys.argv[1:])
    for e in EDICOES:
        if pedidas and e.temporada not in pedidas:
            continue
        jogos, tabelas = ler(e)
        por_fase: dict[str, int] = {}
        for j in jogos:
            por_fase[f"{j.fase}/{j.grupo}" if j.grupo else j.fase] = por_fase.get(f"{j.fase}/{j.grupo}" if j.grupo else j.fase, 0) + 1
        print(e.temporada, len(jogos), por_fase, "tabelas:", [(t.fase, t.grupo, len(t.linhas)) for t in tabelas])


if __name__ == "__main__":
    main()
