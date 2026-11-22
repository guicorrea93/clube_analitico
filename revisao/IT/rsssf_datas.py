"""Datas por jogo nas páginas de temporada da RSSSF (cabeçalho 'Na GIORNATA dd mmm aaaa' e notas '* played ...'),
lidas do cache da coleta (data/coleta/ita-1/rsssf/, só leitura). Terceira opinião para as datas divergentes.
"""
import html, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import itwiki  # noqa: E402
MES = itwiki.MESES
CAB = re.compile(r"(\d+)\s*a\s*GIORNATA\s*(\d{1,2})(?:-\d{1,2})?\s*(gen|feb|mar|apr|mag|giu|lug|ago|set|ott|nov|dic)[a-z.]*\s*(\d{4})", re.I)
JOGO = re.compile(r"^\s*([A-Z][A-Za-z.'& ]+?)\s*-\s*([A-Z][A-Za-z.'& ]+?)\s+(\d+)\s*-\s*(\d+)\s*(\*)?")
NOTA = re.compile(r"^\s*\*+\s*(?:played|giocata|disputata)?\s*(?:on\s*)?(\d{1,2})\s*(gen|feb|mar|apr|mag|giu|lug|ago|set|ott|nov|dic|jan|may|jun|jul|aug|sep|oct|dec)[a-z.]*\s*(\d{4})", re.I)
EN = {"jan": 1, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10, "dec": 12}


def datas(ano):
    f = int(ano) + 1
    nome = f"ital{str(f)[-2:] if f < 2010 else f}.html"
    arq = os.path.join(itwiki.RAIZ, "data", "coleta", "ita-1", "rsssf", nome)
    if not os.path.exists(arq):
        return {}
    t = html.unescape(re.sub(r"<[^>]+>", "", open(arq, "rb").read().decode("latin-1"))).replace("\r", "")
    res, atual, pend = {}, None, []
    for l in t.split("\n"):
        c = CAB.search(l)
        if c:
            atual = f"{int(c.group(4)):04d}-{MES[c.group(3).lower()]:02d}-{int(c.group(2)):02d}"
            pend = []
            continue
        n = NOTA.match(l)
        if n and pend:
            mes = n.group(2).lower()
            m_ = MES.get(mes) or EN.get(mes)
            k = pend.pop(0)
            res[k] = (f"{int(n.group(3)):04d}-{m_:02d}-{int(n.group(1)):02d}", "nota")
            continue
        j = JOGO.match(l)
        if j and atual:
            m, v = itwiki.clube(j.group(1), ano), itwiki.clube(j.group(2), ano)
            if m and v:
                res[(m, v)] = (atual, "rodada")
                if j.group(5):
                    pend.append((m, v))
    return res
