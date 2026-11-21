"""Leitor de tabelas de classificação (wikitext da Wikipédia pt). tabelas(txt) -> [(titulo, [ {nome, pts, j, v, e, d, gp, gc} ])]"""
import re, unicodedata
from listas_campeoes import limpa

H = {"pg": "pts", "pts": "pts", "p": "pts", "j": "j", "pj": "j", "v": "v", "e": "e", "d": "d", "gp": "gp", "gm": "gp", "gf": "gp", "gc": "gc"}


def _num(x):
    return re.fullmatch(r"[+\-]?\d+", x.replace("−", "-").replace("–", "-"))


def _low(x):
    return unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode().lower().strip()


def tabelas(txt):
    txt = re.sub(r"\{\{Tooltip\|([^|}]+)\|[^}]*\}\}", r"\1", txt)
    out = []
    for m in re.finditer(r"\{\|", txt):
        fim = txt.find("\n|}", m.start())
        corpo = txt[m.start():fim]
        if "{|" in corpo[2:]:
            continue
        tits = re.findall(r"\n==+\s*([^=\n]+?)\s*==+", txt[:m.start()])
        tit = tits[-1] if tits else ""
        cab_t = re.search(r"colspan=\"?\d+\"?[^|\n]*\|(?:<font[^>]*>)?([^\n<]+)", corpo)
        if cab_t:
            tit = tit + " / " + limpa(cab_t.group(1)).strip()
        cab, rows = None, []
        for ln in re.split(r"\n\|-[^\n]*", corpo):
            cels = []
            for l in ln.split("\n"):
                l = l.strip()
                if l.startswith("!") or (l.startswith("|") and not l.startswith("|}") and not l.startswith("{|")):
                    for cc in re.split(r"\|\||!!", l[1:]):
                        mm = re.match(r"\s*(?:[a-z\-]+\s*=\s*\"?[^|\"]*\"?\s*)+\|(.*)", cc)
                        cels.append(limpa(mm.group(1) if mm else cc))
            if not cels:
                continue
            low = [_low(x) for x in cels]
            if cab is None and ("j" in low or "pj" in low) and "v" in low and ("gp" in low or "gm" in low or "gf" in low):
                cab = low
                continue
            if cab:
                rows.append(cels)
        if not cab or not rows:
            continue
        inome = next((i for i, x in enumerate(cab) if x in ("time", "times", "equipe", "equipes", "clube", "clubes")), 1)
        hdr = cab[inome + 1:]
        res = []
        for r in rows:
            ni = next((i for i, x in enumerate(r) if x and not _num(x) and len(x) > 2 and not re.fullmatch(r"\d+px|\d+\.?", x)), None)
            if ni is None:
                continue
            d = {"nome": r[ni]}
            for h, v in zip(hdr, r[ni + 1:]):
                hh = H.get(h)
                if hh and _num(v):
                    d[hh] = int(v.replace("−", "-").replace("–", "-"))
            if "j" in d and "v" in d:
                res.append(d)
        if res:
            out.append((tit, res))
    return out
