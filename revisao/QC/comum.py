"""Funções comuns da revisão QC (3ª rodada): pacote, nomes e casamento de jogos com uma fonte nova."""
import csv, os, re, unicodedata
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUGS = ["bra-serie-c", "bra-serie-d", "bra-copa-do-brasil"]
UFS = set("AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO".split())
PARADAS = {"ec", "fc", "sc", "ac", "aa", "se", "ad", "ce", "esporte", "clube", "futebol", "de", "do", "da", "dos",
           "atletico_", "sociedade", "esportiva", "associacao", "atletica", "e", "cr", "ca", "ge", "gremio_"}


def pacote(slug):
    p = os.path.join(RAIZ, "data", "coleta", slug, "pacote", "partidas.csv")
    return list(csv.DictReader(open(p, encoding="utf-8")))


def clubes(slug):
    p = os.path.join(RAIZ, "data", "coleta", slug, "pacote", "clubes.csv")
    return {r["clube"]: r for r in csv.DictReader(open(p, encoding="utf-8"))}


def gols(slug):
    p = os.path.join(RAIZ, "data", "coleta", slug, "pacote", "gols.csv")
    out = {}
    for r in csv.DictReader(open(p, encoding="utf-8")):
        out.setdefault(r["partida_id"], []).append(r)
    return out


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def separa_uf(nome):
    n = nome.strip()
    m = re.search(r"[\s\-/(]+([A-Z]{2})\)?$", n)
    if m and m.group(1) in UFS:
        return n[: m.start()].strip(), m.group(1)
    return n, ""


def tokens(nome):
    n, _ = separa_uf(nome)
    n = sem_acento(n).lower().replace("-", " ").replace(".", " ").replace("'", " ")
    ts = [t for t in re.split(r"[^a-z0-9]+", n) if t]
    return [t for t in ts if t not in PARADAS] or ts


def sim(a, b, uf_b=""):
    """Semelhança de dois nomes (0 a 1,2). uf_b: UF do clube do pacote, para desempatar."""
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return 0.0
    _, uf_a = separa_uf(a)
    sa, sb = set(ta), set(tb)
    if ta == tb:
        s = 1.0
    elif sa <= sb or sb <= sa:
        s = 0.8
    else:
        inter = len(sa & sb)
        s = inter / len(sa | sb)
        # abreviações: 'inter' x 'internacional', 'atl' x 'atletico'
        if s == 0:
            for x in sa:
                for y in sb:
                    if len(x) >= 4 and len(y) >= 4 and (x.startswith(y) or y.startswith(x)):
                        s = max(s, 0.6)
    if uf_a and uf_b:
        s += 0.2 if uf_a == uf_b else -0.3
    return s


def dt(s):
    try:
        a, m, d = s[:10].split("-")
        return date(int(a), int(m), int(d))
    except Exception:
        return None


def casar(fonte, jogos_pac, uf_de, limite=0.5, dias=45):
    """Casa jogos da fonte com jogos do pacote (mesma temporada). Devolve lista (j_fonte, j_pacote, invertido)."""
    cand = []
    for i, f in enumerate(fonte):
        df = dt(f.get("data", ""))
        for k, p in enumerate(jogos_pac):
            dp = dt(p["data"])
            dd = abs((df - dp).days) if (df and dp) else 15
            if dd > dias:
                continue
            ufm, ufv = uf_de.get(p["mandante"], ""), uf_de.get(p["visitante"], "")
            s1 = min(sim(f["mandante"], p["mandante"], ufm), sim(f["visitante"], p["visitante"], ufv))
            s2 = min(sim(f["mandante"], p["visitante"], ufv), sim(f["visitante"], p["mandante"], ufm))
            for s, inv in ((s1, False), (s2, True)):
                if s >= limite:
                    # placar igual ajuda a separar ida e volta
                    if inv:
                        igual = (f["gm"], f["gv"]) == (int(p["gols_visitante"] or -1), int(p["gols_mandante"] or -1))
                    else:
                        igual = (f["gm"], f["gv"]) == (int(p["gols_mandante"] or -1), int(p["gols_visitante"] or -1))
                    nota = s * 10 - dd * 0.3 - (1.5 if inv else 0) + (0.5 if igual else 0)
                    cand.append((nota, i, k, inv))
    cand.sort(reverse=True)
    usados_f, usados_p, res = set(), set(), []
    for nota, i, k, inv in cand:
        if i in usados_f or k in usados_p:
            continue
        usados_f.add(i)
        usados_p.add(k)
        res.append((fonte[i], jogos_pac[k], inv))
    return res, [f for i, f in enumerate(fonte) if i not in usados_f]


def placar_igual(f, p, inv):
    if p["gols_mandante"] == "":
        return False
    gm, gv = int(p["gols_mandante"]), int(p["gols_visitante"])
    return (f["gm"], f["gv"]) == ((gv, gm) if inv else (gm, gv))


def decada(ano):
    return "%ds" % (int(ano) // 10 * 10)
