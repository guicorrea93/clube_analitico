"""Compara os placares do banco (Série B, pontos corridos) com a matriz de resultados da Wikipédia pt.

Linha da matriz = mandante, coluna = visitante. Uso: python -I revisao/SB/compara_jogos_matriz.py [anos]
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabelas_wiki, nomes_sb  # noqa: E402

con = nomes_sb.con


def matriz(t):
    """Acha a matriz de resultados: devolve (rótulos das linhas, [[placar|None]])."""
    for m in re.finditer(r"\{\|.*?\n\|\}", t, re.S):
        tab = m.group(0)
        if tab.count("–") + tab.count("-") < 300 or "!!" not in tab:
            continue
        linhas = re.split(r"\n\|-[^\n]*", tab)
        rot = []; res = []
        for ln in linhas[1:]:
            ln = re.sub(r"<!--.*?-->[ \t]*", "", ln).strip("\n")
            mm = re.match(r"!\s*(?:[^|\n]*\|)?(.+)", ln)
            if not mm or "!!" in ln.split("\n")[0]:
                continue
            nome = mm.group(1).split("\n")[0]
            nome = tabelas_wiki.limpa_time(nome) or re.sub(r"<[^>]+>|'''|\[\[|\]\]", "", nome).split("|")[-1].strip()
            cel = re.split(r"\n\|", "\n" + "\n".join(ln.split("\n")[1:]))[1:]
            pl = []
            for c in cel:
                c = re.sub(r"<!--.*?-->", "", c)
                c = c.split("|")[-1] if re.search(r"(bgcolor|style)\s*=", c.split("|")[0]) else c
                c = re.sub(r"<[^>]+>|'''|''", "", c)
                c = re.sub(r"\[\[[^|\]]*\|([^\]]*)\]\]", r"\1", c)
                x = re.search(r"(\d+)\s*[–-]\s*(\d+)", c)
                pl.append((int(x.group(1)), int(x.group(2))) if x else None)
            rot.append(nome); res.append(pl)
        if len(rot) >= 18 and all(len(p) >= len(rot) - 1 for p in res):
            for i, p in enumerate(res):   # diagonal sem célula: põe um vazio no lugar
                if len(p) == len(rot) - 1:
                    p.insert(i, None)
            return rot, res
    return None, None


def modulo(t):
    """{{#invoke:sports results}}: team1..teamN, name_X, match_X_Y."""
    m = re.search(r"\{\{#invoke:\s*sports results(.*?)\n\}\}", t, re.S | re.I)
    if not m:
        return None, None
    b = m.group(1)
    ids = [x for _, x in sorted((int(n), v.strip()) for n, v in re.findall(r"\|\s*team(\d+)\s*=\s*([^|\n]+)", b))]
    rot = []
    for i in ids:
        nm = re.search(r"\|\s*name_" + re.escape(i) + r"\s*=\s*([^\n]+)", b)
        rot.append(tabelas_wiki.limpa_time(nm.group(1)) if nm else i)
    res = []
    for i in ids:
        lin = []
        for j in ids:
            x = re.search(r"\|\s*match_" + re.escape(i) + "_" + re.escape(j) + r"\s*=\s*[^\n|]*?(\d+)\s*[–-]\s*(\d+)", b)
            lin.append((int(x.group(1)), int(x.group(2))) if x else None)
        res.append(lin)
    return rot, res


def compara(ano):
    t = tabelas_wiki.wikitext(ano)
    if not t:
        return {"ano": ano, "status": "sem página"}
    rot, res = matriz(t)
    if not rot:
        rot, res = modulo(t)
    if not rot:
        return {"ano": ano, "status": "sem matriz"}
    r, cl = nomes_sb.resolvedor(ano)
    ids = [r(n) for n in rot]
    if None in ids or len(set(ids)) != len(ids):
        return {"ano": ano, "status": "nomes", "rot": list(zip(rot, ids))}
    db = {(m, v): (gm, gv, esp) for m, v, gm, gv, esp in con.execute(
        """SELECT mandante_id, visitante_id, gols_mandante, gols_visitante, resultado_especial FROM partida p JOIN edicao e USING(edicao_id)
           WHERE e.competicao_id=2 AND e.temporada=?""", (str(ano),))}
    n = ok = 0; difs = []
    for i, m in enumerate(ids):
        for j, v in enumerate(ids):
            if i == j:
                continue
            w = res[i][j] if j < len(res[i]) else None
            if w is None:
                continue
            n += 1
            d = db.get((m, v))
            if d and (d[0], d[1]) == w:
                ok += 1
            else:
                difs.append((cl[m], cl[v], "banco", d, "wiki", w))
    return {"ano": ano, "status": "ok" if not difs else "dif", "jogos_wiki": n, "iguais": ok, "difs": difs}


if __name__ == "__main__":
    anos = [int(a) for a in sys.argv[1:]] or list(range(2006, 2026))
    for a in anos:
        print(json.dumps(compara(a), ensure_ascii=False))
