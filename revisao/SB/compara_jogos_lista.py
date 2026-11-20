"""Compara jogos do banco (Série B) com jogos listados na Wikipédia pt: footballbox e tabelas ida/volta.

Para cada jogo da página, procura no banco um jogo entre os dois clubes com o mesmo placar (mesmo mando quando a
página diz o mando). Uso: python -I revisao/SB/compara_jogos_lista.py ANO
"""
import json, os, re, sys
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabelas_wiki, nomes_sb  # noqa: E402

con = nomes_sb.con


def nome_de(c):
    c = re.sub(r"\{\{BR-[A-Z]{2}b\}\}", "", c)
    return tabelas_wiki.limpa_time(c) or re.sub(r"[\[\]']", "", c).strip()


def footballbox(t):
    out = []
    for m in re.finditer(r"\{\{\s*[Ff]ootballbox(.*?)\n\}\}", t, re.S):
        b = m.group(1)
        g = lambda k: (re.search(r"\|\s*" + k + r"\s*=\s*([^\n]*)", b) or [None, ""])[1]
        pl = re.search(r"(\d+)\s*[–x×-]\s*(\d+)", g("placar") or g("score"))
        if not pl:
            continue
        out.append({"m": nome_de(g("time1") or g("team1")), "v": nome_de(g("time2") or g("team2")),
                    "gm": int(pl.group(1)), "gv": int(pl.group(2)), "data": re.sub(r"[\[\]]", "", g("data") or g("date")).strip(), "mando": True})
    return out


def ida_volta(t):
    """Tabelas 'Datas | Datas | Time 1 | Placar | Placar | Time 2 | Total'. 1º jogo no mando do Time 1; o 2º no do Time 2
    (o placar do 2º jogo vem na ordem Time 1 x Time 2)."""
    out = []
    for m in re.finditer(r"\{\|.*?\n\|\}", t, re.S):
        tab = m.group(0)
        if "Placar" not in tab or "Time 1" not in tab:
            continue
        for ln in re.split(r"\n\|-[^\n]*", tab)[1:]:
            cs = [c.strip() for c in re.split(r"\n\|", "\n" + ln.strip())[1:]]
            cs = [re.sub(r'^align="?\w+"?\s*\|', "", c) for c in cs]
            if len(cs) < 6:
                continue
            t1, p1, p2, t2 = nome_de(cs[2]), cs[3], cs[4], nome_de(cs[5])
            a = re.match(r"\s*(\d+)\s*x\s*(\d+)", p1); b = re.match(r"\s*(\d+)\s*x\s*(\d+)", p2)
            if a:
                out.append({"m": t1, "v": t2, "gm": int(a.group(1)), "gv": int(a.group(2)), "data": re.sub(r"[\[\]]", "", cs[0]), "mando": False})
            if b:
                out.append({"m": t2, "v": t1, "gm": int(b.group(2)), "gv": int(b.group(1)), "data": re.sub(r"[\[\]]", "", cs[1]), "mando": False})
    return out


def compara(ano):
    t = tabelas_wiki.wikitext(ano)
    jogos = footballbox(t) + ida_volta(t)
    r, cl = nomes_sb.resolvedor(ano)
    db = con.execute("""SELECT partida_id, mandante_id, visitante_id, gols_mandante, gols_visitante, data FROM partida p
                        JOIN edicao e USING(edicao_id) WHERE e.competicao_id=2 AND e.temporada=?""", (str(ano),)).fetchall()
    usados = set(); ok = 0; difs = []; sem_nome = []
    for j in jogos:
        m, v = r(j["m"]), r(j["v"])
        if not m or not v:
            sem_nome.append((j["m"], j["v"])); continue
        cand = [x for x in db if x[0] not in usados and {x[1], x[2]} == {m, v}]
        def placar_ok(x):
            if x[1] == m:
                return (x[3], x[4]) == (j["gm"], j["gv"])
            return (x[4], x[3]) == (j["gm"], j["gv"]) and not j["mando"]
        bate = [x for x in cand if placar_ok(x)]
        if bate:
            usados.add(bate[0][0]); ok += 1
        else:
            difs.append((cl[m], cl[v], f"wiki {j['gm']}-{j['gv']} ({j['data']})",
                         "banco " + "; ".join(f"{cl[x[1]]} {x[3]}-{x[4]} {cl[x[2]]} ({x[5]})" for x in cand)))
    return {"ano": ano, "jogos_wiki": len(jogos), "iguais": ok, "difs": difs, "sem_nome": sem_nome, "jogos_banco": len(db)}


if __name__ == "__main__":
    for a in sys.argv[1:]:
        print(json.dumps(compara(int(a)), ensure_ascii=False, indent=1))
