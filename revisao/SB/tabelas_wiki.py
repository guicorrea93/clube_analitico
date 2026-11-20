"""Lê tabelas de classificação do wikitext das páginas da Wikipédia pt (Série B, por ano).

tabelas(ano) -> lista de tabelas; cada tabela = {"titulo": seção, "linhas": [{pos, time, pts, j, v, e, d, gp, gc}]}
Suporta: tabelas wiki comuns (cabeçalho PG/Pts, J, V, E, D, GP, GC, SG) e o módulo Sports table.
"""
import glob, json, os, re

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
CACHE = os.path.join(RAIZ, "data", "cache", "revisao", "SB")

COL = {"pg": "pts", "pts": "pts", "p": "pts", "pontos": "pts", "j": "j", "pj": "j", "jogos": "j", "v": "v", "e": "e",
       "d": "d", "gp": "gp", "gm": "gp", "gf": "gp", "gc": "gc", "gs": "gc", "ga": "gc", "sg": "sg", "gd": "sg", "ap": "ap",
       "aprov": "ap", "%": "ap"}


_INDICE = None


def por_titulo(titulo):
    """Wikitext de uma página do cache pelo título (lê o título gravado no JSON)."""
    global _INDICE
    if _INDICE is None:
        _INDICE = {}
        for f in glob.glob(os.path.join(CACHE, "*wikipedia.org*")):
            if f.endswith(".txt"):
                continue
            try:
                d = json.load(open(f, encoding="utf8"))
                _INDICE[(("en" if "en.wikipedia" in f else "pt"), d["parse"]["title"])] = d["parse"]["wikitext"]["*"]
            except Exception:
                pass
    return _INDICE.get(titulo)


def wikitext(ano, lingua="pt"):
    if lingua == "en":
        return por_titulo(("en", f"{ano} Campeonato Brasileiro Série B"))
    if lingua == "pt":
        x = por_titulo(("pt", f"Campeonato Brasileiro de Futebol de {ano} - Série B"))
        if x is not None:
            tpl = por_titulo(("pt", f"Predefinição:Tabela do Campeonato Brasileiro da Série B - {ano}"))
            return x + ("\n" + tpl if tpl else "")
        pad = f"pt.wikipedia.org_w_api.php_action_parse_page_Campeonato_Brasileiro_de_Futebol_de_{ano}_-_S_C3_A9rie_B_prop*"
    else:
        pad = f"en.wikipedia.org_w_api.php_action_parse_page_{ano}_Campeonato_Brasileiro_S_C3_A9rie_B_prop*"
    fs = [f for f in glob.glob(os.path.join(CACHE, pad)) if not f.endswith(".txt")]
    if not fs:
        return None
    d = json.load(open(fs[0], encoding="utf8"))
    if "parse" not in d:
        return None
    return d["parse"]["wikitext"]["*"]


def limpa_time(x):
    x = x.replace("'''", "").replace("''", "")
    m = re.search(r"\{\{\s*(?:Futebol|futebol|Fb team|fb team|Fb|Bandeira-futebol)\s+([^|}]+)", x)
    if m:
        return m.group(1).strip()
    m = re.search(r"\{\{\s*(?:Futebol)\s*\|\s*([^|}]+)", x)
    if m:
        return m.group(1).strip()
    ls = re.findall(r"\[\[([^\]]+)\]\]", x)
    ls = [l for l in ls if not l.lower().startswith(("ficheiro:", "file:", "imagem:"))]
    if ls:
        l = ls[-1]
        return l.split("|")[-1].strip()
    return None


def texto_celula(c):
    # tira atributos: 'style="..."|valor' -> 'valor'
    c = re.sub(r"<ref[^>]*/>|<ref.*?</ref>", "", c, flags=re.S)
    c = re.sub(r"\{\{(?:Tooltip|tooltip|abbr|Abbr)\|([^|}]+)\|[^}]*\}\}", r"\1", c)
    partes = re.split(r"(?<!\[)\|(?!\])", c)
    v = partes[-1] if len(partes) > 1 and "=" in partes[0] and "{{" not in partes[0] else c
    v = v.replace("'''", "").replace("''", "")
    v = re.sub(r"<[^>]+>", "", v)
    return v.strip()


def celulas(linha):
    linha = "\n" + linha.strip("\n")
    out = []
    for pedaco in re.split(r"\n(?=[|!])", linha):
        pedaco = pedaco.strip()
        if not pedaco or pedaco.startswith(("|-", "|}", "{|", "|+")):
            continue
        sep = "!!" if pedaco.startswith("!") else "||"
        corpo = pedaco[1:]
        for c in re.split(r"\|\||!!", corpo):
            out.append(c)
    return out


def tabelas_comuns(t):
    res = []
    secao = ""
    for m in re.finditer(r"(^=+[^=\n].*?=+\s*$)|(\{\|.*?\n\|\})", t, re.M | re.S):
        if m.group(1):
            secao = m.group(1).strip("= \n")
            continue
        tab = m.group(2)
        linhas = re.split(r"\n\s*\|-[^\n]*", tab)
        cab = None
        rows = []
        pend_pos = None
        for ln in linhas:
            cs = celulas(ln)
            if not cs:
                continue
            txt = [texto_celula(c) for c in cs]
            low = [re.sub(r"[^a-z%]", "", x.lower()) for x in txt]
            if cab is None and ("j" in low or "pj" in low) and "v" in low and "e" in low and "d" in low:
                cab = [COL.get(x) for x in low if COL.get(x)]
                continue
            if cab is None:
                continue
            time = None; nums = []; pos = None
            for c, x in zip(cs, txt):
                tm = limpa_time(c) if time is None and not re.fullmatch(r"-?\d+", x) else None
                if tm and time is None and not re.fullmatch(r"-?\d+", x):
                    time = tm
                    continue
                if re.fullmatch(r"[−-]?\d+", x.replace("−", "-")):
                    if time is None:
                        pos = int(x.replace("−", "-"))
                    else:
                        nums.append(int(x.replace("−", "-")))
                elif re.fullmatch(r"[+]\d+", x) and time is not None:
                    nums.append(int(x))
                elif re.fullmatch(r"\d+[,.]\d+%?", x) and time is not None:
                    nums.append(float(x.replace(",", ".").rstrip("%")))
            if time is None and pos is not None and not nums:
                pend_pos = pos
                continue
            if time and len(nums) >= 6:
                if pos is None:
                    pos = pend_pos
                pend_pos = None
                r = {"pos": pos, "time": time}
                for k, v in zip(cab, nums):
                    r.setdefault(k, v)
                rows.append(r)
        if rows:
            res.append({"titulo": secao, "linhas": rows})
    return res


def tabelas_modulo(t):
    res = []
    for m in re.finditer(r"\{\{#invoke:\s*Sports table(.*?)\n\}\}", t, re.S | re.I):
        b = m.group(1)
        ordem = re.search(r"\|\s*team_order\s*=\s*([^\n|]+)", b)
        if ordem:
            ids = [x.strip() for x in ordem.group(1).split(",") if x.strip()]
        else:
            ids = [x for _, x in sorted((int(n), v.strip()) for n, v in re.findall(r"\|\s*team(\d+)\s*=\s*([^|\n]+)", b))]
        if not ids:
            continue
        def val(k, i):
            mm = re.search(r"\|\s*" + k + "_" + re.escape(i) + r"\s*=\s*(-?\d+)", b)
            return int(mm.group(1)) if mm else 0
        rows = []
        for p, i in enumerate(ids, 1):
            nm = re.search(r"\|\s*name_" + re.escape(i) + r"\s*=\s*([^\n]+)", b)
            time = limpa_time(nm.group(1)) if nm else i
            v, e, d, gp, gc = val("win", i), val("draw", i), val("loss", i), val("gf", i), val("ga", i)
            aj = val("adjust_points", i)
            rows.append({"pos": p, "time": time or i, "id": i, "j": v + e + d, "v": v, "e": e, "d": d, "gp": gp, "gc": gc,
                         "pts": 3 * v + e + aj, "ajuste": aj})
        res.append({"titulo": "Sports table", "linhas": rows})
    return res


def tabelas(ano, lingua="pt"):
    t = wikitext(ano, lingua)
    if t is None:
        return None
    return tabelas_modulo(t) + tabelas_comuns(t)


if __name__ == "__main__":
    import sys
    for tb in tabelas(int(sys.argv[1]), sys.argv[2] if len(sys.argv) > 2 else "pt") or []:
        print("==", tb["titulo"], len(tb["linhas"]))
        for r in tb["linhas"]:
            print("  ", r)
