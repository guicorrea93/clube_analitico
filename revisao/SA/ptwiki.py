"""Lê a tabela 'Classificação final' de páginas da Wikipédia em português."""
import re
def secao(wt, padrao=r"Classifica[cç][aã]o (final|geral)"):
    ms = list(re.finditer(r"\n(=+)\s*([^=\n]*" + padrao + r"[^=\n]*)\s*=+", wt, re.I))
    if not ms: return ""
    m = ms[-1]
    nivel = len(m.group(1))
    f = re.search(r"\n={1,%d}[^=]" % nivel, wt[m.end():])
    return wt[m.end(): m.end() + f.start()] if f else wt[m.end():]
def limpa(c):
    c = re.sub(r"<!--.*?-->", "", c, flags=re.S)
    c = re.sub(r"<ref[^>]*/>", "", c); c = re.sub(r"<ref.*?</ref>", "", c, flags=re.S)
    m = re.search(r"\{\{\s*(?:Futebol|futebol|Fb|fb team)\s+([^}|]+)", c)
    if m: return m.group(1).strip()
    m = re.findall(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", c)
    c2 = re.sub(r"\{\{[^}]*\}\}", "", c)
    if m and not re.fullmatch(r"\s*[\d\-−+]+\s*", c2): 
        return m[-1].strip()
    c = re.sub(r"<[^>]+>", "", c2).replace("'''", "").replace("''", "")
    return c.strip()
def celulas(linha):
    """separa as células de uma linha de wikitable (texto depois de | ou !)."""
    out = []
    for parte in re.split(r"\|\||!!", linha[1:]):
        # tira atributos: 'style=... | conteúdo'
        segs = parte.split("|")
        if len(segs) > 1 and re.search(r"(style|align|bgcolor|class|colspan|rowspan|width)\s*=", segs[0]):
            parte = "|".join(segs[1:])
        out.append(parte)
    return out
def tabela(sec):
    linhas = []
    cab = None
    for bloco in re.split(r"\n\|-[^\n]*", sec):
        cels = []
        tipos = []
        for l in bloco.split("\n"):
            l = l.rstrip()
            if l.startswith("{|") or l.startswith("|}") or not l or l.startswith("|+"): continue
            if l[0] in "|!":
                for c in celulas(l):
                    cels.append(limpa(c)); tipos.append(l[0])
            elif cels:
                cels[-1] += " " + limpa(l)
        if not cels: continue
        if all(t == "!" for t in tipos) and any(re.fullmatch(r"(PG|Pts|P|J|V|E|D|GP|GC|SG)", x) for x in cels):
            cab = [x for x in cels]; continue
        linhas.append(cels)
    return cab, linhas
ROT = {"PG": "pts", "PTS": "pts", "P": "pts", "PONTOS": "pts", "J": "j", "V": "v", "E": "e", "D": "d", "GP": "gp", "GM": "gp", "GF": "gp",
       "GC": "gc", "GS": "gc", "SG": "sg", "S": "sg", "%": "ap", "APR": "ap", "APROV": "ap", "AP": "ap", "POS": "pos", "#": "pos", "POSICAO": "pos", "COL": "pos"}
def ler(wt):
    sec = secao(wt)
    if not sec: return []
    cab, linhas = tabela(sec)
    rot = []
    if cab:
        for c in cab:
            k = re.sub(r"[^A-Z%#]", "", c.upper().replace("Ç", "C").replace("Ã", "A").replace("Ó", "O"))
            if re.search(r"TIME|CLUBE|EQUIPE|ESTADO|CLASSIFICA|TABELA", k) or not k: continue
            rot.append(ROT.get(k, "x_" + k))
    out = []
    for cels in linhas:
        nums = [x.strip().rstrip("º°ª") for x in cels if re.fullmatch(r"[−\-+]?\d+([.,]\d+)?[%º°ª]?", x.strip())]
        nomes = [x for x in cels if re.search(r"[A-Za-zÀ-ÿ]{2}", x) and not re.fullmatch(r"(Campeão|Vice.*|Rebaixad.*)", x.strip(), re.I)]
        if not nomes or len(nums) < 8: continue
        n = [float(x.strip().replace("−", "-").replace(",", ".").rstrip("%")) for x in nums]
        r = rot if "pos" in rot else ["pos"] + rot
        if len(r) != len(n):
            r = ["pos", "pts", "j", "v", "e", "d", "gp", "gc", "sg", "ap"][:len(n)]
        dd = {k: int(v) for k, v in zip(r, n) if k != "ap" and not k.startswith("x_")}
        dd["extras"] = {k: v for k, v in zip(r, n) if k.startswith("x_")}
        dd["nome"] = nomes[0]
        dd["bruto"] = [int(x) for x in n]
        out.append(dd)
    return out
