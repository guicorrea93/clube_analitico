"""Amostra de jogos: Wikipédia es (páginas de temporada) x pacote ecu-1. Casa por temporada + mandante + visitante
(e data, quando a página traz). Saída: casados, placar igual/diferente, data igual/diferente, por década."""
import sys; sys.stdout.reconfigure(encoding="utf-8")
import re, csv, collections, unicodedata
sys.path.insert(0, "revisao/EC")
import baixar
MES = {m: i for i, m in enumerate("enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split(), 1)}
MES["setiembre"] = 9
def ch(s): return re.sub(r"[^a-z0-9]", "", "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn"))
AL = {"ldu(q)": "LDU de Quito", "ldu q": "LDU de Quito", "liga de quito": "LDU de Quito", "ldu quito": "LDU de Quito", "ldu(p)": "LDU de Portoviejo",
      "liga de portoviejo": "LDU de Portoviejo", "ldu(c)": "LDU de Cuenca", "liga de loja": "LDU de Loja", "ldu(l)": "LDU de Loja",
      "dep.quito": "Deportivo Quito", "dep. quito": "Deportivo Quito", "univ.católica": "Universidad Católica de Quito", "universidad católica": "Universidad Católica de Quito",
      "u. católica": "Universidad Católica de Quito", "barcelona": "Barcelona de Guayaquil", "dep.cuenca": "Deportivo Cuenca", "dep. cuenca": "Deportivo Cuenca",
      "independiente josé terán": "Independiente del Valle", "independiente": "Independiente del Valle", "river ecuador": "Guayaquil City",
      "técnico u.": "Técnico Universitario", "dep.quevedo": "Deportivo Quevedo", "azogues": "Deportivo Azogues", "libertad": "Libertad de Loja",
      "américa(q)": "América de Quito", "américa": "América de Quito", "manta": "Manta FC", "cuniburo": "Vinotinto", "macara": "Macará"}
pac = collections.defaultdict(list)
for r in csv.DictReader(open("data/coleta/ecu-1/pacote/partidas.csv", encoding="utf-8")):
    pac[r["temporada"][:4]].append(r)
def resolve(nome, clubes):
    n = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", nome); n = re.sub(r"'''|''|style=\"[^\"]*\"\||bgcolor=#\w+\||<[^>]+>", "", n).strip()
    n = n.split("|")[-1].strip()
    if n.lower() in AL and AL[n.lower()] in clubes: return AL[n.lower()]
    k = ch(n)
    if not k: return None
    for c in clubes:
        if ch(c) == k: return c
    cands = [c for c in clubes if k in ch(c) or ch(c) in k]
    if len(cands) == 1: return cands[0]
    if n.lower() in AL: return AL[n.lower()]
    return None
def jogos_wiki(pagina, ano):
    t = baixar.wikitext("es", pagina)
    t = re.sub(r"<ref[^>]*?/>|<ref.*?</ref>", "", t, flags=re.S)
    out = []; data = None
    for tab in re.split(r"\n\{\|", t):
        data = None
        for row in tab.split("\n|-"):
            cel = [c.strip() for c in re.findall(r"^\|(?![-}])(.*)$", row, re.M)]
            cel = [x for c in cel for x in c.split("||")]
            for i, c in enumerate(cel):
                txt = re.sub(r"\[https?://\S+\s+([^\]]+)\]", r"\1", c)
                txt = re.sub(r"style=\"[^\"]*\"\||bgcolor=#\w+\||'''", "", txt)
                m = re.fullmatch(r"\s*\[*(?:[^|\]]*\|)?\s*(\d{1,2})\s*[-:–]\s*(\d{1,2})\s*\]*\s*(?:\(.*\))?\s*", txt)
                if m and 0 < i < len(cel) - 1:
                    for c2 in cel[i + 2:]:
                        dm = re.search(r"(\d{1,2}) de (\w+)", re.sub(r"rowspan=\d+\|", "", c2))
                        if dm and dm.group(2).lower() in MES:
                            data = f"{ano}-{MES[dm.group(2).lower()]:02d}-{int(dm.group(1)):02d}"; break
                    out.append((cel[i - 1], cel[i + 1], int(m.group(1)), int(m.group(2)), data))
                    break
    return out
ALVO = [l.strip() for l in open("revisao/EC/alvo_espn.txt", encoding="utf-8")] if len(sys.argv) > 2 else []
pags = [l.split(" ", 1)[1].strip() for l in open(sys.argv[1], encoding="utf-8")]
stat = collections.defaultdict(lambda: collections.Counter())
dif = []
for p in pags:
    ano = re.search(r"(\d{4})", p).group(1)
    if ano not in pac: continue
    clubes = {r["mandante"] for r in pac[ano]} | {r["visitante"] for r in pac[ano]}
    for hm, aw, gm, gv, d in jogos_wiki(p, ano):
        m, v = resolve(hm, clubes), resolve(aw, clubes)
        dec = ano[:3] + "0s"
        if not m or not v: stat[dec]["nome não resolvido"] += 1; continue
        cands = [r for r in pac[ano] if r["mandante"] == m and r["visitante"] == v]
        if not cands: stat[dec]["sem jogo no pacote"] += 1; dif.append(("SEM JOGO", ano, m, gm, gv, v, d, p)); continue
        for a_ in ALVO:
            an, am, av = a_.split("|")
            if an == ano and am == m and av == v: print("ALVO", ano, m, gm, gv, v, d, [(r["gols_mandante"], r["gols_visitante"], r["data"]) for r in cands])
        same = [r for r in cands if (r["gols_mandante"], r["gols_visitante"]) == (str(gm), str(gv))]
        if same:
            stat[dec]["placar igual"] += 1
            if d:
                if any(r["data"] == d for r in same): stat[dec]["data igual"] += 1
                else: stat[dec]["data diferente"] += 1; dif.append(("DATA", ano, m, gm, gv, v, d, [r["data"] for r in same], p))
        else:
            stat[dec]["placar diferente"] += 1
            dif.append(("PLACAR", ano, m, gm, gv, v, d, [(r["gols_mandante"], r["gols_visitante"], r["data"], r["fase"]) for r in cands], p))
for dec in sorted(stat): print(dec, dict(stat[dec]))
for x in dif: print(*x, sep=" | ")
