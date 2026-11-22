"""Jogos da Wikipédia em espanhol (data/coleta/per-1/wikipedia/es_<ano>.txt), para os anos que a RSSSF não tem.

As páginas peruanas trazem os jogos em três formatos:
- matriz do módulo de resultados ({{#invoke:sports results}} ou {{#invoke:sports table|show_matches=...}}): siglas em
  "|team1=ALI", nome em "|name_ALI=[[Alianza Lima]]" e o jogo em "|match_ALI_CHA=3—0" (mandante ALI); "null", "n.p." e
  vazio são jogos não disputados; placar riscado (<s>2–1</s>) é jogo anulado e fica de fora;
- lista por rodada: {{OneLegResult| Mandante || 2–0 | Visitante }} sob "=== Fecha 3 ===";
- modelo {{Partido}} / {{Partidos}} (local, resultado, visita, fecha, estadio, asistencia).
Na mesma seção (títulos de nível 2 e 3, sem os genéricos "Tabla de posiciones", "Resultados", "Fecha N"), o jogo da lista
que repete um da matriz (mesmo mandante, visitante e placar) só acrescenta a rodada e a data ao da matriz; o que não está na
matriz entra. Duas matrizes da mesma seção ("Fecha 1 a la 14" e "Fecha 15 a la 21") são turnos diferentes: entram as duas.

A fase vem dos títulos (FASES, a primeira regra que casa com "nível 2 / nível 3 / nível 4"); seção que casa com FORA fica de
fora (equipes de reserva, promoção, goleadores). O nome do clube é o alvo do link ("[[Club Sporting Tabaco|Sporting
Tabaco]]" -> "Club Sporting Tabaco"). Devolve rsssf_sul.Jogo com texto "wiki-es_<ano>:<linha>".

Uso: jogos(ano) -> list[Jogo]; python coleta/per-1/wikipedia_jogos.py <ano> ... (resumo)
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from rsssf_sul import Jogo  # noqa: E402

PASTA = AQUI.parent.parent / "data" / "coleta" / "per-1" / "wikipedia"
MESES = {m: k for k, m in enumerate(["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre",
                                     "octubre", "noviembre", "diciembre"], 1)}
_SCORE = re.compile(r"(\d{1,2})\s*[-–—:]\s*(\d{1,2})")
_GENERICO = re.compile(r"^(tabla de posiciones( y resultados)?|resultados|fecha\b.*|partido de (ida|vuelta)|primera rueda|"
                       r"segunda rueda|.*vuelta)$", re.I)
FORA = re.compile(r"reserva|promoci[oó]n|goleador|asistencia|estad[ií]stica|equipos participantes|ascensos", re.I)

# "nível 2 / nível 3 / ..." da seção -> fase do pacote ("" = fase de pontos corridos; grupo vem do "Grupo X")
FASES = [
    (r"regional.*cuartos", "Quartas de final do Regional"), (r"regional.*semifinal", "Semifinal do Regional"),
    (r"regional.*/ final$", "Final do Regional"), (r"regional.*repechaje", "Repechaje do Regional"),
    (r"regional.*desempate", "Desempate do Regional"), (r"regional", "Regional"),
    (r"liguilla (final|por el t[ií]tulo)|tercera fase", "Fase final"),
    (r"liguilla por (el descenso|la permanencia)", "Grupo do rebaixamento"),
    (r"segunda fase", "Segunda fase"),
    (r"final nacional|^final$|play-off", "Final"),
    (r"desempate|partido extra|definici[oó]n", "Desempate do título"),
    (r"", ""),
]


def _fase(secao: str) -> str:
    for rx, nome in FASES:
        if re.search(rx, secao, re.I):
            return nome
    return ""


def _limpa(c: str) -> str:
    c = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?(?:</ref>|$)", " ", c)
    c = re.sub(r"\[\[(?:Archivo|File|Imagen):[^\]]*\]\]", " ", c)
    c = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", c)
    c = re.sub(r"\{\{[^{}]*\}\}|<[^>]+>", " ", c)
    return re.sub(r"\s+", " ", c.replace("'''", "").replace("''", "")).strip()


def _clube(c: str) -> str:
    """Alvo do link ("[[Club Sporting Tabaco|Sporting Tabaco]]" -> "Club Sporting Tabaco"); sem link, o texto limpo."""
    c = re.sub(r"\[\[(?:Archivo|File|Imagen):[^\]]*\]\]", " ", c)   # escudo antes do nome
    m = re.search(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]", c)
    if not m and (m2 := re.search(r"\[\[([^\]|#]+)\|", c)):   # link que continua na linha seguinte
        return m2.group(1).strip()
    return m.group(1).strip() if m else _limpa(c)


def _data(txt: str, ano: int) -> str | None:
    if m := re.search(r"(\d{1,2})(?:\s*(?:y|,|al?)\s*\d{1,2})*\s+de\s+(\w+)(?:\s+de\s+(\d{4}))?", txt):
        mes = MESES.get(m.group(2).lower())
        if mes:
            return f"{int(m.group(3) or ano)}-{mes:02d}-{int(m.group(1)):02d}"
    return None


def _placar(v: str) -> tuple[int, int] | None:
    """Placar da célula; None se não disputado, anulado (riscado) ou sem placar."""
    if re.search(r"<s>|<del>", v, re.I):
        return None
    ms = _SCORE.search(_limpa(v))
    return (int(ms.group(1)), int(ms.group(2))) if ms else None


def jogos(ano: int | str) -> list[Jogo]:
    chave = str(ano)
    ano = int(chave[:4])
    ls = (PASTA / f"es_{chave}.txt").read_text(encoding="utf-8").splitlines()
    tit: dict[int, str] = {}
    rodada = data = None
    matriz: list[tuple[str, Jogo]] = []
    lista: list[tuple[str, Jogo]] = []
    bloco: dict | None = None
    tpl: dict[str, str] | None = None
    txt = f"wiki-es_{chave}"

    def secao() -> str:
        return " / ".join(tit[k] for k in sorted(tit) if not _GENERICO.match(tit[k]))

    def grupo() -> str:
        for k in sorted(tit):
            if m := re.match(r"(?:Grupo|Zona)\s+(.+)$", tit[k], re.I):
                return m.group(1).strip()
        return ""

    def fora() -> bool:
        return any(FORA.search(v) for v in tit.values())

    for i, l in enumerate(ls):
        s = l.strip()
        if bloco is not None:   # módulo de resultados ou de tabela com jogos
            if s.startswith("}}"):
                if not fora():
                    for k, (a, b, v) in bloco["jogos"]:
                        p = _placar(v)
                        if p and a in bloco["nomes"] and b in bloco["nomes"]:
                            matriz.append((bloco["secao"], Jogo(linha=k, mandante=bloco["nomes"][a], visitante=bloco["nomes"][b],
                                                                gm=p[0], gv=p[1], fase=_fase(bloco["secao"]),
                                                                grupo=bloco["grupo"], texto=f"{txt}:{k}")))
                bloco = None
                continue
            for parte in s.split("|"):
                if m := re.match(r"^name_(\S+?)\s*=\s*(.*)$", parte.strip()):
                    bloco["nomes"][m.group(1)] = _clube(m.group(2))
            for m in re.finditer(r"\|\s*match_([^_\s=]+)_([^_\s=]+)\s*=\s*([^|]*)", l):
                bloco["jogos"].append((i, (m.group(1), m.group(2), m.group(3))))
            if m := re.match(r"^\|\s*name_(\S+?)\s*=\s*(\[\[.*)$", s):   # nome com "|" dentro do link
                bloco["nomes"][m.group(1)] = _clube(m.group(2))
            continue
        if re.match(r"^(?:<center>)?\{\{#invoke:\s*sports (results|table)", s, re.I):
            bloco = {"secao": secao(), "grupo": grupo(), "nomes": {}, "jogos": []}
            continue
        if tpl is not None:
            if s.startswith("}}"):
                p = _placar(tpl.get("resultado", ""))
                if p and tpl.get("local") and tpl.get("visita") and not fora():
                    k = int(tpl["_linha"])
                    pen = _SCORE.search(_limpa(tpl.get("penaltyresultado", "") or tpl.get("resultado penalti", "")))
                    lista.append((secao(), Jogo(linha=k, mandante=_clube(tpl["local"]), visitante=_clube(tpl["visita"]), gm=p[0],
                                                gv=p[1], fase=_fase(secao()), grupo=grupo(), rodada=rodada,
                                                data=_data(tpl.get("fecha", ""), ano) or data,
                                                pen_m=int(pen.group(1)) if pen else None, pen_v=int(pen.group(2)) if pen else None,
                                                local=_limpa(tpl.get("estadio", "")) or None,
                                                texto=f"{txt}:{k}")))
                tpl = None
            elif mt := re.match(r"^\|\s*([\w ]+?)\s*=\s*(.*)$", s):
                tpl[mt.group(1).lower()] = mt.group(2)
            continue
        if re.match(r"^\{\{Partidos?\b", s, re.I):
            tpl = {"_linha": str(i)}
            continue
        if m := re.match(r"^\{\{OneLegResult\|(.*)\}\}", s):
            corpo = re.sub(r"\[\[[^\]]*\]\]", lambda x: x.group(0).replace("|", ""), m.group(1))
            celulas = [p.replace("", "|") for p in re.split(r"\|\|?", corpo) if p.strip() != ""]
            if len(celulas) >= 3 and (p := _placar(celulas[1])) and not fora():
                lista.append((secao(), Jogo(linha=i, mandante=_clube(celulas[0]), visitante=_clube(celulas[2]), gm=p[0], gv=p[1],
                                            fase=_fase(secao()), grupo=grupo(), rodada=rodada, data=data, texto=f"{txt}:{i}")))
            continue
        if m := re.match(r"^(=+)\s*(.*?)\s*=+\s*(<!--.*)?$", s):
            n = len(m.group(1))
            texto = _limpa(m.group(2))
            tit = {k: v for k, v in tit.items() if k < n}
            tit[n] = texto
            mf = re.match(r"Fecha\s+(\d+)(?!\s*a\s)", texto, re.I)
            rodada, data = (int(mf.group(1)), None) if mf else (None, None)
            continue
        if rodada is not None and data is None and (d := _data(s, ano)) and not s.startswith(("|", "{", "!")):
            data = d   # "Los partidos se jugaron el 22 y 23 de julio de 1950."
    # seção em que a lista tem todos os jogos da matriz (ou mais): fica só a lista. A matriz de 1950, 1958 e 1965 põe na
    # linha o clube do 1º turno, não o mandante da lista, e repetiria os jogos com o mando trocado
    n_lista, n_matriz = Counter(s for s, _ in lista), Counter(s for s, _ in matriz)
    matriz = [(s, j) for s, j in matriz if n_lista[s] < n_matriz[s]]
    # o jogo da lista que repete um da matriz da mesma seção só dá a rodada e a data
    from clubes_per import clube   # a lista e a matriz podem ligar o mesmo clube a artigos diferentes
    cl = lambda n: clube(n, ano) or n
    livres: dict[tuple, list[Jogo]] = {}
    for sec, j in matriz:
        livres.setdefault((sec, cl(j.mandante), cl(j.visitante), j.gm, j.gv), []).append(j)
    saida = [j for _, j in matriz]
    for sec, j in lista:
        par = livres.get((sec, cl(j.mandante), cl(j.visitante), j.gm, j.gv))
        if not par and (par := livres.get((sec, cl(j.visitante), cl(j.mandante), j.gv, j.gm))):
            # a matriz pôs o jogo com o mando trocado: vale o mando da lista (que traz a rodada)
            par[0].mandante, par[0].visitante, par[0].gm, par[0].gv = j.mandante, j.visitante, j.gm, j.gv
        if par:
            m = par.pop(0)
            m.rodada, m.data = j.rodada or m.rodada, j.data or m.data
            m.local = j.local or m.local
            m.pen_m, m.pen_v = j.pen_m, j.pen_v
        else:
            saida.append(j)
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for a in sys.argv[1:]:
        js = jogos(a)
        print(a, len(js), "jogos", dict(Counter((j.fase, j.grupo) for j in js)),
              "com rodada", sum(1 for j in js if j.rodada), "com data", sum(1 for j in js if j.data))
