"""Revisão Série C (SC): lê as tabelas de classificação das páginas da Wikipédia (wikitable e Module:Sports table).

tabelas(txt) -> lista de {"secao": [títulos acima], "linhas": [{"pos", "time", "pts", "j", "v", "e", "d", "gp", "gc", "aj"}]}
"""
import re

CAB = {"pts": "pts", "p": "pts", "pg": "pts", "pontos": "pts", "points": "pts",
       "j": "j", "pj": "j", "jogos": "j", "pld": "j", "gp_jogos": "j", "played": "j",
       "v": "v", "w": "v", "g": "v", "vitórias": "v", "wins": "v",
       "e": "e", "d_emp": "e", "empates": "e", "draws": "e",
       "d": "d", "l": "d", "derrotas": "d", "losses": "d",
       "gp": "gp", "gf": "gp", "gm": "gp", "gols pró": "gp",
       "gc": "gc", "ga": "gc", "gs": "gc", "gols contra": "gc",
       "sg": "sg", "gd": "sg", "dg": "sg", "saldo": "sg"}


def _time(cel):
    cel = re.sub(r"\{\{\s*(?:flagicon|flag|bandeira|band|fb)\s*\|[^}]*\}\}", "", cel, flags=re.I)
    m = re.search(r"\{\{\s*(?:Futebol|Fb team|Fbaicon|Fb|futebol)[ _]([^}|]+)", cel)
    if m:
        return m.group(1).strip()
    m = re.search(r"\[\[(?:[^|\]]*\|)?([^\]]+)\]\]", cel)
    if m:
        return m.group(1).strip()
    t = re.sub(r"\{\{[^}]*\}\}|'''?|<[^>]+>", "", cel).strip()
    return t or None


def _num(cel):
    c = re.sub(r"<ref.*?</ref>|<ref[^>]*/>|\{\{[^}]*\}\}|'''?|<[^>]+>", "", cel)
    c = c.replace("−", "-").replace("–", "-").replace("+", "").strip()
    m = re.fullmatch(r"-?\d+", c)
    return int(c) if m else None


def _cab(cel):
    m = re.search(r"\{\{\s*(?:Tooltip|Abbr|Abreviatura|H:title)\s*\|\s*([^|}]+)", cel, re.I)
    t = m.group(1) if m else re.sub(r"\{\{[^}]*\}\}|\[\[|\]\]|'''?|<[^>]+>", "", cel.split("|")[-1])
    return CAB.get(t.strip().lower())


def _celulas(linha_txt):
    """Divide o texto de uma linha da wikitable em células (|| e quebras com |), sem atributos."""
    cels = []
    for ln in linha_txt.split("\n"):
        ln = ln.strip()
        if not ln or ln.startswith("|-") or ln.startswith("|+"):
            continue
        if ln[0] not in "|!":
            if cels:
                cels[-1] = (cels[-1][0], cels[-1][1] + " " + ln)
            continue
        corpo = ln[1:]
        sep = "!!" if ln[0] == "!" else "||"
        partes, buf, prof = [], "", 0
        k = 0
        while k < len(corpo):
            if corpo.startswith("{{", k) or corpo.startswith("[[", k):
                prof += 1; buf += corpo[k:k + 2]; k += 2; continue
            if corpo.startswith("}}", k) or corpo.startswith("]]", k):
                prof -= 1; buf += corpo[k:k + 2]; k += 2; continue
            if prof == 0 and corpo.startswith(sep, k):
                partes.append(buf); buf = ""; k += 2; continue
            buf += corpo[k]; k += 1
        partes.append(buf)
        for p in partes:
            # tira atributo: 'align="left"|valor' (pipe simples fora de {{ }} e [[ ]])
            prof, corte = 0, None
            for k in range(len(p)):
                if p.startswith("{{", k) or p.startswith("[["):
                    pass
                ch2 = p[k:k + 2]
                if ch2 in ("{{", "[["):
                    prof += 1
                elif ch2 in ("}}", "]]"):
                    prof -= 1
                elif p[k] == "|" and prof == 0 and not p.startswith("||", k):
                    corte = k
                    break
            if corte is not None and re.search(r"=|^\s*$", p[:corte]):
                p = p[corte + 1:]
            cels.append(("!" if ln[0] == "!" else "|", p.strip()))
    return cels


def _wikitable(bloco):
    linhas = re.split(r"\n\|-[^\n]*", bloco)
    cab = None
    out = []
    for lt in linhas:
        cels = _celulas(lt)
        if not cels:
            continue
        if all(t == "!" for t, _ in cels) and len(cels) >= 5:
            cab = [_cab(c) for _, c in cels]
            continue
        if cab is None:
            continue
        vals = [c for _, c in cels]
        # células com rowspan de texto (ex.: "Classificados") ficam no fim; casar pelo começo
        if len(vals) < len(cab) - 1:
            continue
        reg = {}
        # posição e time: primeira célula numérica e a primeira com nome
        pos_i = next((i for i, v in enumerate(vals[:3]) if _num(v) is not None), None)
        t_i = next((i for i, v in enumerate(vals[:4]) if _num(v) is None and _time(v)), None)
        if t_i is None:
            continue
        reg["pos"] = _num(vals[pos_i]) if pos_i is not None and pos_i < t_i else None
        reg["time"] = _time(vals[t_i])
        # números depois do time, na ordem do cabeçalho depois da coluna do time
        nums_cab = [c for c in cab[cab.index(None, 0) if None in cab else 0:] if c] if False else None
        cab_pos = [c for c in cab]
        # índice do time no cabeçalho: a 1ª coluna sem chave depois da posição
        idx_t = None
        for i, c in enumerate(cab_pos):
            if c is None and i >= (1 if reg["pos"] is not None else 0):
                idx_t = i
                break
        if idx_t is None:
            continue
        resto_cab = cab_pos[idx_t + 1:]
        resto_val = vals[t_i + 1:]
        for c, v in zip(resto_cab, resto_val):
            if c:
                reg[c] = _num(v)
        if all(reg.get(k) is not None for k in ("v", "e", "d")):
            out.append(reg)
    return out


def _sports(bloco):
    par = {}
    corpo, prof, buf, partes = bloco[2:-2], 0, "", []
    k = 0
    while k < len(corpo):
        if corpo.startswith("{{", k) or corpo.startswith("[[", k):
            prof += 1; buf += corpo[k:k + 2]; k += 2; continue
        if corpo.startswith("}}", k) or corpo.startswith("]]", k):
            prof -= 1; buf += corpo[k:k + 2]; k += 2; continue
        if corpo[k] == "|" and prof == 0:
            partes.append(buf); buf = ""; k += 1; continue
        buf += corpo[k]; k += 1
    partes.append(buf)
    for p in partes:
        if "=" in p:
            a, b = p.split("=", 1)
            par[a.strip()] = re.sub(r"<!--.*?-->", "", b, flags=re.S).strip()
    ordem = []
    k = 1
    while f"team{k}" in par:
        ordem.append(par[f"team{k}"]); k += 1
    out = []
    for i, t in enumerate(ordem, 1):
        def n(c):
            v = par.get(f"{c}_{t}", "").strip()
            return int(v) if re.fullmatch(r"-?\d+", v) else 0
        nome = par.get(f"name_{t}", t)
        out.append({"pos": i, "time": _time(nome) or t, "v": n("win"), "e": n("draw"), "d": n("loss"),
                    "gp": n("gf"), "gc": n("ga"), "aj": n("adjust_points"), "j": n("win") + n("draw") + n("loss")})
    return out


def _fim_bloco(txt, i, abre, fecha):
    prof, j = 0, i
    while j < len(txt):
        if txt.startswith(abre, j):
            prof += 1; j += len(abre); continue
        if txt.startswith(fecha, j):
            prof -= 1; j += len(fecha)
            if prof == 0:
                return j
            continue
        j += 1
    return len(txt)


def tabelas(txt):
    out = []
    titulos = [(m.start(), len(m.group(1)), m.group(2).strip()) for m in re.finditer(r"(?m)^(={2,5})\s*(.*?)\s*=+\s*$", txt)]

    def secao(pos):
        pilha = []
        for p, nivel, t in titulos:
            if p > pos:
                break
            pilha = [x for x in pilha if x[0] < nivel] + [(nivel, t)]
        return [t for _, t in pilha]

    for m in re.finditer(r"(?m)^\{\|", txt):
        fim = _fim_bloco(txt, m.start(), "{|", "|}")
        ls = _wikitable(txt[m.start():fim])
        if len(ls) >= 2:
            out.append({"secao": secao(m.start()), "tipo": "wikitable", "linhas": ls})
    for m in re.finditer(r"\{\{\s*#invoke:\s*Sports table", txt, re.I):
        fim = _fim_bloco(txt, m.start(), "{{", "}}")
        ls = _sports(txt[m.start():fim])
        if len(ls) >= 2:
            out.append({"secao": secao(m.start()), "tipo": "sports", "linhas": ls})
    return out


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    t = open(sys.argv[1], encoding="utf-8").read()
    for tb in tabelas(t):
        print(tb["tipo"], " > ".join(tb["secao"]), len(tb["linhas"]))
        for r in tb["linhas"][:3]:
            print("   ", r)
