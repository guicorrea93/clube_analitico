"""Lê a tabela {{#invoke:sports table|main|...}} do wikitext da Wikipédia."""
import re
def _limpa(v):
    v = re.sub(r"<!--.*?-->", "", v, flags=re.S)
    v = re.sub(r"<ref[^>]*/>", "", v); v = re.sub(r"<ref.*?</ref>", "", v, flags=re.S)
    return v.strip()
def tabelas(wt):
    out = []
    for m in re.finditer(r"\{\{\s*#invoke:\s*sports table", wt, re.I):
        # acha o fim balanceado
        i, prof = m.start(), 0
        j = i
        while j < len(wt):
            if wt.startswith("{{", j): prof += 1; j += 2; continue
            if wt.startswith("}}", j):
                prof -= 1; j += 2
                if prof == 0: break
                continue
            j += 1
        out.append(wt[i:j])
    return out
def ler(bloco):
    # separa parâmetros no nível 0 (ignora | dentro de [[ ]] e {{ }})
    corpo = bloco[2:-2]
    partes, buf, pc, pl = [], "", 0, 0
    k = 0
    while k < len(corpo):
        s = corpo[k:k+2]
        if s == "{{": pc += 1; buf += s; k += 2; continue
        if s == "}}": pc -= 1; buf += s; k += 2; continue
        if s == "[[": pl += 1; buf += s; k += 2; continue
        if s == "]]": pl -= 1; buf += s; k += 2; continue
        ch = corpo[k]
        if ch == "|" and pc == 0 and pl == 0: partes.append(buf); buf = ""
        else: buf += ch
        k += 1
    partes.append(buf)
    p = {}
    for x in partes:
        if "=" in x:
            a, b = x.split("=", 1); p[a.strip()] = _limpa(b)
    ordem = []
    if "team_order" in p:
        ordem = [t.strip() for t in p["team_order"].split(",") if t.strip()]
    else:
        n = 1
        while f"team{n}" in p: ordem.append(p[f"team{n}"]); n += 1
    linhas = []
    def num(k):
        v = p.get(k, "")
        v = re.sub(r"[^\d\-−]", "", v).replace("−", "-")
        return int(v) if v not in ("", "-") else 0
    for pos, t in enumerate(ordem, 1):
        nome = p.get(f"name_{t}", t)
        mm = re.findall(r"\[\[([^\]]+)\]\]", nome)
        if mm: nome = mm[-1].split("|")[-1]
        nome = re.sub(r"\{\{[^}]*\}\}", "", nome).strip()
        w, d, l, gf, ga = num(f"win_{t}"), num(f"draw_{t}"), num(f"loss_{t}"), num(f"gf_{t}"), num(f"ga_{t}")
        adj = num(f"adjust_points_{t}") if f"adjust_points_{t}" in p else 0
        linhas.append(dict(pos=pos, cod=t, nome=nome, j=w+d+l, v=w, e=d, d=l, gp=gf, gc=ga, adj=adj,
                           status=p.get(f"status_{t}", ""), nota=p.get(f"note_{t}", "")[:200]))
    pv = 3
    if "winpoints" in p:
        try: pv = int(p["winpoints"])
        except: pass
    for r in linhas: r["pts"] = pv*r["v"] + r["e"] + r["adj"]
    return linhas, p
