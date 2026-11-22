"""Leitor das páginas de temporada da Wikipédia it (Serie A): classifica finale, tabellone, calendario, marcatori.
Só leitura do cache (data/cache/revisao/IT/). Nomes dos clubes resolvidos com coleta/comum-europa/clubes_ita.py.
"""
import os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "coleta", "comum-europa"))
sys.path.insert(0, AQUI)
import clubes_ita  # noqa: E402
from baixar import nome_cache  # noqa: E402
from baixar_itwiki import url, ANOS  # noqa: E402

EXTRA = {  # nomes da Wikipédia it que o cadastro não conhece
    "ambrosianainter": "Inter", "genova1893": "Genoa CFC", "liguria": "Sampierdarenese", "lrvicenza": "Vicenza Calcio",
    "lanerossivicenza": "Vicenza Calcio", "chievoverona": "Chievo Verona", "verona": "Hellas Verona", "hellasverona": "Hellas Verona",
    "spal": "SPAL 1907 Ferrara", "messina": "A.C.R. Messina", "internazionale": "Inter", "inter": "Inter",
    "milano": "AC Milan", "anconitana": "Ancona Calcio", "proLivorno".lower(): "AS Livorno", "juventuscisitalia": "Juventus",
    "fiorentina": "ACF Fiorentina", "salernitana": "Salernitana Calcio 1919", "palermo": "US Palermo", "foggia": "US Foggia",
    "foggiaincedit": "US Foggia", "lazio": "Lazio Roma", "romulea": None, "talmonetorino": "Torino FC", "foggiaandincedit": "US Foggia",
}


def clube(nome, ano):
    n = re.sub(r"<[^>]+>|'''|''", "", nome).strip()
    n = re.sub(r"\s*\(.*?\)\s*$", "", n).strip()
    k = clubes_ita.chave(n)
    if k in EXTRA:
        c = EXTRA[k]
    else:
        c = clubes_ita.esd(n, ano)
    return clubes_ita.exibicao(c) if c else None


def texto(ano):
    arq = nome_cache(url(ano))
    if not os.path.exists(arq):
        return None
    return open(arq, encoding="utf-8").read()


def secao(t, titulo_re):
    m = re.search(r"^==+\s*" + titulo_re + r"\s*==+\s*$", t, re.M | re.I)
    if not m:
        return None
    resto = t[m.end():]
    nivel = len(re.match(r"^(=+)", t[m.start():]).group(1))
    fim = re.search(r"^={2,%d}[^=].*?={2,%d}\s*$" % (nivel, nivel), resto, re.M)
    return resto[:fim.start()] if fim else resto


def tabela_de(s):
    i = s.find("{|")
    if i < 0:
        return None
    prof, j = 0, i
    while j < len(s):
        if s.startswith("{|", j):
            prof += 1; j += 2; continue
        if s.startswith("|}", j):
            prof -= 1; j += 2
            if prof == 0:
                return s[i:j]
            continue
        j += 1
    return s[i:]


TPL = re.compile(r"\{\{\s*[Cc]alcio\s+([^|}]+)(?:\|[^}]*)?\}\}")


def classifica(ano, t=None):
    """[{pos, clube, pts, g, v, n, p, gf, gs, pen, cor, nome}] da tabela 'Classifica finale'."""
    t = t or texto(ano)
    s = secao(t, r"Classifica(?: finale)?")
    if s is None:
        return None
    tb = tabela_de(s)
    res = []
    for bloco in tb.split("\n|-")[1:]:
        cor = re.search(r"background(?:-color)?\s*:\s*(#[0-9A-Fa-f]{6})", bloco.split("\n", 1)[0])
        m = re.search(r"\|\|\s*'*(\d+)\.?'*\s*\|\|", bloco)
        if not m:
            continue
        resto = bloco[m.end():]
        tm = TPL.search(resto)
        if tm:
            nome = tm.group(1).strip()
            depois = resto[tm.end():]
        else:
            lk = re.search(r"\[\[(?:[^|\]]+\|)?([^\]]+)\]\]", resto)
            if not lk:
                continue
            nome = lk.group(1); depois = resto[lk.end():]
        pen = re.search(r"\(\s*([−\-–]\s*\d+)\s*\)", depois.split("\n", 1)[0])
        depois_limpo = re.sub(r"<ref[^>]*/>|<ref.*?</ref>|<ref[^>]*>.*", "", depois, flags=re.S)
        nums = re.findall(r"(?:^|\|)\s*(?:'''|<s>)?\s*([−\-–+]?\d+)", depois_limpo.split("\n", 1)[1] if "\n" in depois_limpo else depois_limpo)
        nums = [int(x.replace("−", "-").replace("–", "-")) for x in nums]
        if len(nums) < 7:
            continue
        pts, g, v, n, p, gf, gs = nums[:7]
        res.append({"pos": int(m.group(1)), "nome": nome, "clube": clube(nome, ano), "pts": pts, "g": g, "v": v, "n": n,
                    "p": p, "gf": gf, "gs": gs, "pen": int(pen.group(1).replace("−", "-").replace("–", "-").replace(" ", "")) if pen else 0,
                    "cor": cor.group(1).upper() if cor else None})
    return res


def legenda(ano, t=None):
    t = t or texto(ano)
    s = secao(t, r"Classifica(?: finale)?") or ""
    return {c.upper(): re.sub(r"\[\[(?:[^|\]]+\|)?([^\]]+)\]\]", r"\1", d).replace("'''", "").strip()
            for c, d in re.findall(r"background-color:\s*(#[0-9A-Fa-f]{6});?\"?>(?:&nbsp;)*</span>\s*(.*)", s)}


def tabellone(ano, t=None):
    """{(mandante, visitante): (gm, gv, nota)} do 'Tabellone' (matriz). Clubes pelo nome de exibição."""
    t = t or texto(ano)
    s = secao(t, r"Tabellone")
    if s is None:
        return None
    tb = tabela_de(s)
    linhas = []
    for bloco in tb.split("\n|-")[1:]:
        b = bloco.split("\n", 1)
        if len(b) < 2:
            continue
        corpo = b[1].strip()
        if not corpo.startswith("|") or corpo.startswith("|}"):
            continue
        # primeira célula: nome do clube (texto depois do último | da primeira linha)
        prim, _, resto = corpo.partition("\n")
        nome = prim.split("|")[-1].strip()
        resto = (resto or "").replace("\n", "")
        if prim.count("||") > 0:   # nome e células na mesma linha
            partes = prim.split("||")
            nome = partes[0].split("|")[-1].strip(); resto = "||" + "||".join(partes[1:]) + ("||" + resto.lstrip("|") if resto.strip() else "")
        resto = resto.strip()
        celulas = re.sub(r"^\|+", "", resto).split("||") if resto else []
        linhas.append((nome, celulas))
    res = {}
    nomes = [clube(n, ano) for n, _ in linhas]
    for (nome, cel), m in zip(linhas, nomes):
        if len(cel) != len(linhas):
            return {"_erro": f"linha {nome} com {len(cel)} células (clubes {len(linhas)})"}
        for c, v in zip(cel, nomes):
            if v == m:
                continue
            sc = re.search(r"(\d+)\s*[-–]\s*(\d+)", c)
            if not sc:
                res[(m, v)] = (None, None, c.strip())
                continue
            nota = "tavolino" if re.search(r"tavolino|a tav|sospesa|n\.d\.|non disputata", c, re.I) else ""
            res[(m, v)] = (int(sc.group(1)), int(sc.group(2)), nota or (c.strip() if "Abbr" in c else ""))
    if None in nomes:
        res["_sem_nome"] = [n for (n, _), x in zip(linhas, nomes) if x is None]
    return res


MESES = {"gen": 1, "feb": 2, "mar": 3, "apr": 4, "mag": 5, "giu": 6, "lug": 7, "ago": 8, "set": 9, "ott": 10, "nov": 11, "dic": 12}


def marcatori(ano, t=None):
    t = t or texto(ano)
    res = []
    for m in re.finditer(r"\{\{Classifica marcatori\|([^\n]*)\}\}", t):
        p = dict(x.split("=", 1) for x in re.split(r"\|(?![^\[]*\]\])", m.group(1)) if "=" in x)
        if "reti" in p:
            nome = re.sub(r"\[\[(?:[^|\]]+\|)?([^\]]+)\]\]", r"\1", p.get("nome", "")).strip()
            try:
                res.append((int(re.sub(r"\D", "", p["reti"])), nome, p.get("squadra", "").strip()))
            except ValueError:
                pass
    return res


DATA_RE = re.compile(r"(\d{1,2})\s*º?\s*(gen|feb|mar|apr|mag|giu|lug|ago|set|ott|nov|dic)[a-z]*\.?", re.I)


def _limpa(c):
    c = re.sub(r"<ref[^>]*/>|<ref.*?</ref>|<ref[^>]*>.*", "", c, flags=re.S)
    return c


def _par(c, ano):
    c = re.sub(r"\{\{[^{}]*\}\}|<[^>]+>|'''|''|\[\[(?:[^|\]]+\|)?([^\]]+)\]\]", lambda m: m.group(1) or "", c).strip()
    c = c.split("|")[-1].strip()
    for i in [i for i, ch in enumerate(c) if ch in "-–"]:
        m, v = clube(c[:i], ano), clube(c[i + 1:], ano)
        if m and v:
            return m, v
    return None


def _cel_data(c, ano):
    c2 = _limpa(c)
    m = DATA_RE.search(c2.split("|")[-1]) or (DATA_RE.search(c2) if "rowspan" in c2 or "bgcolor" in c2 else None)
    if not m or re.search(r"\d+\s*-\s*\d+", c2.split("|")[-1]):
        return None
    mes = MESES[m.group(2).lower()[:3]]
    y = ano if mes >= 7 else ano + 1
    rs = re.search(r"rowspan\s*=\s*\"?(\d+)", c2)
    return (f"{y:04d}-{mes:02d}-{int(m.group(1)):02d}", int(rs.group(1)) if rs else 1)


def calendario(ano, t=None):
    """{(mandante, visitante): data AAAA-MM-DD} pelo 'Calendario' (datas por jogo, com rowspan)."""
    t = t or texto(ano)
    s = secao(t, r"Calendario")
    if s is None:
        return {}
    res = {}
    for bloco in re.split(r"\{\|\s*border=0", s)[1:]:
        bloco = bloco.split("\n|}")[0]
        dupla = "ritorno" in bloco.split("\n|-")[0]
        esq = dir_ = None
        resta_e = resta_d = 0
        for linha in bloco.split("\n|-")[1:]:
            corpo = "\n".join(l for l in linha.split("\n")[1:] if not l.startswith("!"))
            corpo = _limpa(corpo).replace("\n", "")
            if not corpo.strip():
                continue
            cel = re.sub(r"^\s*\|+", "", corpo).split("||")
            ip = next((i for i, c in enumerate(cel) if _par(c, ano)), None)
            if ip is None:
                continue
            m, v = _par(cel[ip], ano)
            d_e = next((_cel_data(c, ano) for c in cel[:ip] if _cel_data(c, ano)), None)
            d_d = next((_cel_data(c, ano) for c in cel[ip + 1:] if _cel_data(c, ano)), None)
            if d_e:
                esq, resta_e = d_e[0], d_e[1]
            elif resta_e <= 0:
                esq = None
            if d_d:
                dir_, resta_d = d_d[0], d_d[1]
            elif resta_d <= 0:
                dir_ = None
            if esq:
                res[(m, v)] = esq
            if dupla and dir_:
                res[(v, m)] = dir_
            resta_e -= 1; resta_d -= 1
    return res
