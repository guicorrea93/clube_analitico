"""Compara os jogos do Futebol Nacional (fn_jogos.json) com o pacote bra-sp-1 (partidas.csv), edição a edição:
placar e data de cada jogo, jogos só numa fonte e totais. Os nomes do Futebol Nacional são casados com os do pacote por
votos (jogos do mesmo dia com o mesmo placar), primeiro na edição e depois no geral.
Saídas: revisao/QS/fn_comparar_saida.txt (resumo por década e por edição) e revisao/QS/fn_diferencas.csv (jogo a jogo).
Uso (da raiz): python -I -X utf8 revisao/QS/fn_comparar.py"""
import csv
import json
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
AQUI = Path(__file__).resolve().parent
PAC = RAIZ / "data" / "coleta" / "bra-sp-1" / "pacote" / "partidas.csv"


def temporada_fn(t: str) -> str:
    """'1913 (APSA)' -> '1913 APEA'; '1935 (LPF)' -> '1935 LPF'."""
    m = re.match(r"(\d{4})(?: \((\w+)\))?", t)
    liga = {"APSA": "APEA"}.get(m[2], m[2]) if m[2] else ""
    return f"{m[1]} {liga}".strip()


def iso(d):
    if not d:
        return None
    dd, mm, aa = d.split("/")
    return f"{aa}-{mm}-{dd}"


def dias(a, b):
    try:
        return abs((date.fromisoformat(a) - date.fromisoformat(b)).days)
    except (TypeError, ValueError):
        return 9999


def placar(s):
    m = re.match(r"^(\d+)\s*-\s*(\d+)", s or "")
    return (int(m[1]), int(m[2])) if m else None


OGOL = RAIZ / "data" / "coleta" / "bra-sp-1" / "ogol"


def ogol_do_ano(t):
    """Jogos do calendário do ogol guardado pela coleta (sp1_<temporada>.json): {(data, placar ordenado)}."""
    arq = OGOL / f"sp1_{t.replace(' ', '_')}.json"
    if not arq.exists():
        arq = OGOL / f"sp1_{t[:4]}.json"
    if not arq.exists():
        return None
    return json.loads(arq.read_text(encoding="utf-8"))


def opiniao_ogol(og, p):
    """O mesmo jogo no calendário do ogol (pelo código ogol:<id> que a coleta guardou em fonte_id): 'data placar'."""
    m = re.search(r"ogol:(\d+)", p.get("fonte_id") or "")
    if not og or not m:
        return "ogol: -"
    o = next((x for x in og if str(x.get("id")) == m[1]), None)
    if not o:
        return "ogol: -"
    return f"ogol: {o.get('data')} {o.get('mandante')} {o.get('resultado')} {o.get('visitante')}"


def main():
    fn = json.loads((AQUI / "fn_jogos.json").read_text(encoding="utf-8"))
    pac = defaultdict(list)
    for p in csv.DictReader(open(PAC, encoding="utf-8")):
        pac[p["temporada"]].append(p)
    eds = {}
    for t, v in fn.items():
        k = temporada_fn(t)
        if k not in pac and k[:4] in pac and k.endswith("APEA"):   # 1933 e 1934: o pacote só tem a APEA, sem a sigla
            k = k[:4]
        eds[k] = v
    # 1) votos de nome: dias com 1 jogo só em cada fonte e o mesmo placar
    votos_ed, votos = defaultdict(Counter), defaultdict(Counter)
    for t, info in eds.items():
        if t not in pac:
            continue
        fdia, pdia = defaultdict(list), defaultdict(list)
        for j in info["jogos"]:
            if placar(j["placar"]):
                fdia[iso(j["data"])].append(j)
        for p in pac[t]:
            pdia[p["data"]].append(p)
        for d, fs in fdia.items():
            ps = pdia.get(d, [])
            if len(fs) == 1 and len(ps) == 1:
                j, p = fs[0], ps[0]
                g = placar(j["placar"])
                if p["gols_mandante"] and g == (int(p["gols_mandante"]), int(p["gols_visitante"])):
                    for a, b in ((j["mandante"], p["mandante"]), (j["visitante"], p["visitante"])):
                        votos_ed[(t, a)][b] += 1; votos[a][b] += 1
    # 2) segundo passo: com o mapa parcial, casa jogos do mesmo dia em que um dos clubes já é conhecido
    def mapa_de(t, n):
        if votos_ed[(t, n)]:
            return votos_ed[(t, n)].most_common(1)[0][0]
        return votos[n].most_common(1)[0][0] if votos[n] else None
    for _ in range(2):
        for t, info in eds.items():
            if t not in pac:
                continue
            pdia = defaultdict(list)
            for p in pac[t]:
                pdia[p["data"]].append(p)
            for j in info["jogos"]:
                for p in pdia.get(iso(j["data"]), []):
                    m1, m2 = mapa_de(t, j["mandante"]), mapa_de(t, j["visitante"])
                    if m1 == p["mandante"] and not m2:
                        votos_ed[(t, j["visitante"])][p["visitante"]] += 1; votos[j["visitante"]][p["visitante"]] += 1
                    if m2 == p["visitante"] and not m1:
                        votos_ed[(t, j["mandante"])][p["mandante"]] += 1; votos[j["mandante"]][p["mandante"]] += 1
    # 3) comparação jogo a jogo
    linhas, resumo, decada = [], [], defaultdict(Counter)
    for t in sorted(set(eds) | set(pac), key=lambda x: (x[:4], x)):
        info = eds.get(t)
        ps = pac.get(t, [])
        if not info:
            resumo.append(f"{t}\tsó no pacote ({len(ps)} jogos)")
            continue
        if not ps:
            resumo.append(f"{t}\tsó no Futebol Nacional ({len(info['jogos'])} jogos; {info['url']})")
            continue
        livres = list(ps)
        og = ogol_do_ano(t)
        c = Counter()
        for j in info["jogos"]:
            m, v = mapa_de(t, j["mandante"]), mapa_de(t, j["visitante"])
            g = placar(j["placar"])
            cancel = "cancel" in (j["nota"] or "").lower() or "anulad" in (j["nota"] or "").lower()
            cands = [p for p in livres if {p["mandante"], p["visitante"]} == {m, v} and dias(p["data"], iso(j["data"])) <= 45]
            if not cands:
                c["so_fn"] += 1
                linhas.append([t, "só no Futebol Nacional", iso(j["data"]), j["mandante"], j["placar"], j["visitante"],
                               "", "", j["nota"], j["fase"]])
                continue
            p = min(cands, key=lambda p: dias(p["data"], iso(j["data"])))
            livres.remove(p)
            c["casados"] += 1
            gp = (int(p["gols_mandante"]), int(p["gols_visitante"])) if p["gols_mandante"] else None
            if gp and p["mandante"] != m:
                gp = gp[::-1]
            dd = dias(p["data"], iso(j["data"]))
            ok_placar = g is not None and gp == g
            if g is not None and gp is not None:
                c["placar_conf"] += 1; c["placar_ok"] += ok_placar
            if iso(j["data"]) and p["data"] and p["data"] > "0000-00-00":
                c["data_conf"] += 1; c["data_ok"] += dd == 0
            if (g is not None and gp is not None and not ok_placar) or (dd and dd != 9999) or cancel:
                linhas.append([t, "placar" if not ok_placar and g and gp else "data" if dd else "cancelado no FN",
                               iso(j["data"]), j["mandante"], j["placar"], j["visitante"], p["data"],
                               f"{p['mandante']} {p['gols_mandante']}-{p['gols_visitante']} {p['visitante']}", j["nota"], j["fase"],
                               opiniao_ogol(og, p)])
        for p in livres:
            c["so_pac"] += 1
            linhas.append([t, "só no pacote", "", "", "", "", p["data"],
                           f"{p['mandante']} {p['gols_mandante']}-{p['gols_visitante']} {p['visitante']}", p["observacao"], p["fase"]])
        dec = t[:3] + "0s"
        decada[dec].update(c)
        resumo.append(f"{t}\tFN {len(info['jogos'])} (registrados {info['jogos_registrados']}, com resultado "
                      f"{info['jogos_com_resultado']}) x pacote {len(ps)}\tcasados {c['casados']}\tplacar {c['placar_ok']}/"
                      f"{c['placar_conf']}\tdata {c['data_ok']}/{c['data_conf']}\tsó FN {c['so_fn']}\tsó pacote {c['so_pac']}")
    with open(AQUI / "fn_diferencas.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["temporada", "tipo", "data_fn", "mandante_fn", "placar_fn", "visitante_fn", "data_pacote", "jogo_pacote",
                    "nota", "fase", "ogol"])
        w.writerows(linhas)
    txt = ["Década\tcasados\tplacar ok/conf\tdata ok/conf\tsó FN\tsó pacote"]
    for d in sorted(decada):
        c = decada[d]
        txt.append(f"{d}\t{c['casados']}\t{c['placar_ok']}/{c['placar_conf']}\t{c['data_ok']}/{c['data_conf']}\t{c['so_fn']}\t{c['so_pac']}")
    txt += [""] + resumo
    nomes = sorted((n, cc.most_common(2)) for n, cc in votos.items())
    txt += ["", "Nomes (Futebol Nacional -> pacote, votos):"] + [f"{n}\t{v}" for n, v in nomes]
    (AQUI / "fn_comparar_saida.txt").write_text("\n".join(txt) + "\n", encoding="utf-8")
    print("\n".join(txt[:16]))


if __name__ == "__main__":
    main()
