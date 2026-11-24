"""Jogos-desempate (spareggi) de título e de rebaixamento da Serie A, pela Wikipédia em italiano (revisão IT-018, decisão
D-04 b: fase "Desempate", fora da tabela; os de vaga europeia ficam de fora).

A seção "Spareggi" (ou "Spareggio ...") do artigo de cada temporada (data/coleta/ita-1/wikipedia-it/) traz uma tabela por
desempate, com linhas "| Bari || 2-1 || '''Brescia''' || [[Bologna]], 16 giugno [[1932]]" (mandante, placar, visitante,
local e data); prorrogação ("dts") e pênaltis ("dtr", "{{dcr|4|2}}") ficam na mesma célula do placar.

Uso como biblioteca: ler(a) -> [{"motivo", "secao", "m", "v", "gm", "gv", "pen_m", "pen_v", "prorrogacao", "data", "cidade"}]
"""
from __future__ import annotations

import re
from pathlib import Path

DADOS = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "ita-1" / "wikipedia-it"
MESES = {m: i for i, m in enumerate(["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto",
                                     "settembre", "ottobre", "novembre", "dicembre"], 1)}
TITULO = re.compile(r"(?i)scudetto|titolo|primo posto|1º posto")   # 2003/04: "Sfida salvezza/promozione"
QUEDA = re.compile(r"(?i)salvezza|sfida|retroced|retrocess|permanenza|interdivisional|ammissione alla serie a|1[5-9]º posto|"
                   r"2[01]º posto|spareggi?o?$|spareggi?\s*$")
EUROPA = re.compile(r"(?i)uefa|coppa|champions|europa|intertoto|6º posto|5º posto|4º posto|mitropa")


# desempates que a Wikipédia it não traz com placar: ano -> jogos (fonte e gols de cada um)
URL_54 = "RSSSF (tablesi/ital54.html)"
EXTRAS = {
    1953: [   # triangular de rebaixamento (15º a 17º): Udinese 3, SPAL 2, Palermo 1 — caiu o Palermo
        {"motivo": "rebaixamento", "secao": "triangular de rebaixamento (15º a 17º)", "m": "Udinese", "v": "SPAL", "gm": 2,
         "gv": 0, "pen_m": None, "pen_v": None, "prorrogacao": False, "data": "1954-06-06", "cidade": "Milão", "fonte": URL_54,
         "gols": [("m", "Virgili", 18), ("m", "Menegotti", 31)]},
        {"motivo": "rebaixamento", "secao": "triangular de rebaixamento (15º a 17º)", "m": "Udinese", "v": "Palermo", "gm": 1,
         "gv": 1, "pen_m": None, "pen_v": None, "prorrogacao": False, "data": "1954-06-13", "cidade": "Florença", "fonte": URL_54,
         "gols": [("v", "Cavazzuti", 58), ("m", "Zorzi", 63)]},
        {"motivo": "rebaixamento", "secao": "triangular de rebaixamento (15º a 17º)", "m": "SPAL", "v": "Palermo", "gm": 2,
         "gv": 1, "pen_m": None, "pen_v": None, "prorrogacao": False, "data": "1954-06-20", "cidade": "Roma", "fonte": URL_54,
         "gols": [("v", "Lucchesi", 19), ("m", "Olivieri", 23), ("m", "Bernardin", 78)]},
    ],
}


def _limpo(cel: str) -> str:
    cel = re.sub(r"^\s*\|?\s*(?:(?:bgcolor|style|align)=[^|]*\|)?", "", cel)
    m = re.search(r"\{\{\s*Calcio\s+([^|}]+?)\s*(?:\|[^}]*)?\}\}", cel)
    if m:
        return m.group(1).strip()
    cel = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", cel)
    cel = re.sub(r"<[^>]+>|\{\{[^}]*\}\}|'''|''", "", cel)
    return cel.strip()


def ler(a: int) -> list[dict]:
    nome = f"{'Divisione Nazionale' if a == 1945 else 'Serie A'} {a}-{a + 1}.wiki"
    arq = DADOS / nome
    if a in EXTRAS:
        return EXTRAS[a]
    if not arq.exists():
        return []
    t = arq.read_text(encoding="utf-8")
    res = []
    cab = [(m.start(), len(m.group(1)), m.group(2).strip()) for m in re.finditer(r"^(={2,})\s*(.*?)\s*\1\s*$", t, re.M)]
    for i, (ini, nivel, titulo) in enumerate(cab):
        fim = next((p for p, n, _ in cab[i + 1:]), len(t))
        pai = next((tt for p, n, tt in reversed(cab[:i]) if n < nivel), "")
        if not re.search(r"(?i)spareggi|sfida salvezza", titulo + " " + pai):
            continue
        secao = f"{pai} / {titulo}" if pai and re.search(r"(?i)spareggi", pai) else titulo
        if re.search(r"(?i)qualificazione", secao):   # 1945/46: vaga no grupo final (nem título nem queda)
            continue
        if EUROPA.search(secao):
            continue
        motivo = "título" if TITULO.search(secao) else "rebaixamento" if QUEDA.search(secao) else None
        if motivo is None:
            continue
        for l in t[ini:fim].split("\n"):
            if not l.startswith("|") or "||" not in l:
                continue
            cel = l[1:].split("||")
            if len(cel) < 4:
                continue
            sc = re.match(r"\s*(\d+)\s*-\s*(\d+)(.*)$", re.sub(r"'''", "", cel[1]))
            if not sc:
                continue
            extra = sc.group(3)
            pen = re.search(r"\{\{dcr\|(\d+)\|(\d+)\}\}|\((\d+)\s*-\s*(\d+)\s*\[\[[^\]]*dtr", extra) or \
                re.search(r"(\d+)\s*-\s*(\d+)\s*(?:\[\[[^\]]*\|)?dtr", extra)
            pm = pv = None
            if pen:
                g = [x for x in pen.groups() if x is not None]
                pm, pv = int(g[0]), int(g[1])
            dl = re.search(r"(\d{1,2})\s+(\w+)\s+\[?\[?(\d{4})", _limpo(cel[3]) if False else re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", cel[3]))
            data = None
            if dl and dl.group(2).lower() in MESES:
                data = f"{dl.group(3)}-{MESES[dl.group(2).lower()]:02d}-{int(dl.group(1)):02d}"
            cidade = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", cel[3]).split(",")[0].strip() or None
            res.append({"motivo": motivo, "secao": secao, "m": _limpo(cel[0]), "v": _limpo(cel[2]), "gm": int(sc.group(1)),
                        "gv": int(sc.group(2)), "pen_m": pm, "pen_v": pv,
                        "prorrogacao": bool(re.search(r"dts|aet|supplementar", extra, re.I)) or pm is not None,
                        "data": data, "cidade": cidade})
    return res
