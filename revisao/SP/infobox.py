"""Infobox das páginas de cada edição (Wikipédia pt): participantes, jogos, gols, campeão, vice, artilheiro.
Compara com o banco (n.º de clubes, jogos, gols). Saída: revisao/SP/infobox.json e saida_infobox.txt"""
import sys as _s; _s.stdout.reconfigure(encoding="utf-8")
import json, os, re, sqlite3, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baixar import wikitext
from listas_campeoes import limpa
AQUI = os.path.dirname(os.path.abspath(__file__))

w = wikitext("Campeonato Paulista de Futebol", "pt")
i = w.find("=== Campeonato Paulista ==="); j = w.find("=== Campeonato Paulista Extra")
tit = []
for t in re.findall(r"\[\[(Campeonato Paulista de Futebol de \d{4}[^]|]*)", w[i:j]):
    if t not in tit:
        tit.append(t)


def chave(t):
    m = re.match(r"Campeonato Paulista de Futebol de (\d{4})(?: \((\w+)\))?", t)
    ano, liga = m.group(1), m.group(2)
    liga = {"LFP": "LPF"}.get(liga, liga)
    return ano + (" " + liga if liga else "")


def campo(txt, nome):
    m = re.search(r"\|\s*" + nome + r"\s*=\s*(.*)", txt)
    return limpa(m.group(1)) if m else None


info = {}
for t in tit:
    txt = wikitext(t, "pt")
    if not txt:
        continue
    k = chave(t)
    ib = txt[:txt.find("\n}}") + 3] if "{{Info" in txt[:3000] else ""
    info[k] = {"titulo": t, "n": campo(ib, "n_participantes"), "jogos": campo(ib, "jogos"), "gols": campo(ib, r"go?l[o]?s"),
               "campeao": campo(ib, "campeão"), "vice": campo(ib, "vicecampeão"), "artilheiro": campo(ib, "artilheiro")}
json.dump(info, open(os.path.join(AQUI, "infobox.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)

c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
out = []
cont = {"ed": 0, "jogos_conf": 0, "jogos_ok": 0, "gols_conf": 0, "gols_ok": 0, "n_conf": 0, "n_ok": 0}
for eid, temp, n in c.execute("select edicao_id, temporada, num_clubes from edicao where competicao_id=7 order by ano_inicio, temporada").fetchall():
    j, g = c.execute("select count(*), sum(gols_mandante+gols_visitante) from partida where edicao_id=?", (eid,)).fetchone()
    jn = c.execute("select count(*) from partida where edicao_id=? and gols_mandante is not null", (eid,)).fetchone()[0]
    k = temp if temp in info else temp.split(" ")[0]
    ib = info.get(k)
    cont["ed"] += 1
    if not ib:
        out.append(f"{temp}\tsem página/infobox")
        continue
    def num(x):
        m = re.match(r"\s*(\d+)", x or "")
        return int(m.group(1)) if m else None
    wj, wg, wn = num(ib["jogos"]), num(ib["gols"]), num(ib["n"])
    linha = []
    if wj is not None:
        cont["jogos_conf"] += 1
        if wj in (j, jn): cont["jogos_ok"] += 1
        else: linha.append(f"jogos banco {j} (com placar {jn}) wiki {wj}")
    if wg is not None:
        cont["gols_conf"] += 1
        if wg == g: cont["gols_ok"] += 1
        else: linha.append(f"gols banco {g} wiki {wg}")
    if wn is not None:
        cont["n_conf"] += 1
        if wn == n: cont["n_ok"] += 1
        else: linha.append(f"clubes banco {n} wiki {wn}")
    if linha:
        out.append(f"{temp}\t" + " | ".join(linha))
out.append(str(cont))
open(os.path.join(AQUI, "saida_infobox.txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out))
