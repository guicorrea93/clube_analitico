"""Compara a classificação final da Série B (banco / painel) com a tabela final da Wikipédia pt (e en quando houver).

Casamento dos clubes: primeiro por números (J, V, E, D, GP, GC), depois por nome aproximado.
Uso: python -I revisao/SB/compara_classificacao.py [anos...]
"""
import json, os, re, sqlite3, sys, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabelas_wiki  # noqa: E402

RAIZ = tabelas_wiki.RAIZ
con = sqlite3.connect("file:" + os.path.join(RAIZ, "db", "futebol.db").replace("\\", "/") + "?mode=ro", uri=True)


def chave(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\b(fc|ec|sc|ac|futebol|clube|esporte|atletico)\b", "", s)
    return re.sub(r"[^a-z]", "", s)


def banco(ano):
    return con.execute("""SELECT f.posicao, c.nome, f.jogos, f.vitorias, f.empates, f.derrotas, f.gols_pro, f.gols_contra, f.pontos,
                          f.ajuste_pontos, f.fonte FROM classificacao_final f JOIN edicao e USING(edicao_id) JOIN clube c USING(clube_id)
                          WHERE e.competicao_id=2 AND e.temporada=? ORDER BY f.posicao""", (str(ano),)).fetchall()


def escolhe(tabs, n):
    cands = [t for t in tabs if len(t["linhas"]) >= n - 1]
    if not cands:
        return None
    fin = [t for t in cands if re.search(r"final|geral", t["titulo"], re.I)]
    return (fin or cands)[-1] if fin else max(cands, key=lambda t: len(t["linhas"]))


def compara(ano, lingua="pt"):
    tabs = tabelas_wiki.tabelas(ano, lingua)
    db = banco(ano)
    if tabs is None:
        return {"ano": ano, "status": "sem página"}
    tb = escolhe(tabs, len(db))
    if not tb:
        return {"ano": ano, "status": "sem tabela final", "tabelas": [(t["titulo"], len(t["linhas"])) for t in tabs]}
    w = tb["linhas"]
    usados = set(); par = {}
    num = lambda r: (r.get("j"), r.get("v"), r.get("e"), r.get("d"), r.get("gp"), r.get("gc"))
    for i, r in enumerate(db):
        k = tuple(r[2:8])
        cand = [j for j, x in enumerate(w) if j not in usados and num(x) == k]
        if len(cand) > 1:
            cand = [j for j in cand if chave(w[j]["time"])[:4] == chave(r[1])[:4]] or cand
        if cand:
            par[i] = cand[0]; usados.add(cand[0])
    for i, r in enumerate(db):
        if i in par:
            continue
        cand = [j for j, x in enumerate(w) if j not in usados and (chave(x["time"]) == chave(r[1]) or chave(x["time"])[:5] == chave(r[1])[:5])]
        if cand:
            par[i] = cand[0]; usados.add(cand[0])
    difs = []
    for i, r in enumerate(db):
        if i not in par:
            difs.append(("sem par na Wikipédia", r[0], r[1], tuple(r[2:9])))
            continue
        x = w[par[i]]
        if num(x) != tuple(r[2:8]):
            difs.append(("números", r[0], r[1], "banco", tuple(r[2:9]), "wiki", num(x) + (x.get("pts"),), x["time"]))
        if x.get("pos") is not None and x["pos"] != r[0]:
            difs.append(("posição", r[1], "banco", r[0], "wiki", x["pos"], x["time"]))
        if x.get("pts") is not None and x["pts"] != r[8]:
            difs.append(("pontos", r[1], "banco", r[8], "wiki", x["pts"]))
    sobra = [w[j]["time"] for j in range(len(w)) if j not in usados]
    return {"ano": ano, "status": "ok" if not difs and not sobra else "dif", "tabela": tb["titulo"], "n_wiki": len(w),
            "n_banco": len(db), "difs": difs, "sobra_wiki": sobra, "fonte_banco": db[0][10] if db else None}


if __name__ == "__main__":
    anos = [int(a) for a in sys.argv[1:] if a.isdigit()] or [int(t) for (t,) in con.execute(
        "SELECT temporada FROM edicao WHERE competicao_id=2 ORDER BY ano_inicio")]
    lingua = "en" if "en" in sys.argv else "pt"
    for a in anos:
        r = compara(a, lingua)
        print(json.dumps(r, ensure_ascii=False))
