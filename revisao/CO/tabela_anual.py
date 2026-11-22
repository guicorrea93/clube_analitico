"""Blocos B/C: anos de turno único (1948-1967) — a tabela final da RSSSF (colNN.html, "Final Table") x a soma dos jogos do
pacote, clube a clube (jogos, V, E, D, gols). Pega as temporadas que a coleta marcou "sem tabela para conferir" porque o leitor
não reconheceu o formato "1. Santa Fe  44 22 17 5 95:64 61".
Uso (da raiz): python -I revisao/CO/tabela_anual.py"""
import csv, html, re, sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path("coleta/col-1").resolve()))
sys.path.insert(0, str(Path("coleta/comum-sulamerica").resolve()))
from clubes_col import clube  # noqa: E402  (só leitura do dicionário de nomes da coleta)

P = "data/coleta/col-1/pacote/"
soma = defaultdict(lambda: defaultdict(lambda: [0] * 6))
for p in csv.DictReader(open(P + "partidas.csv", encoding="utf-8")):
    if p["gols_mandante"] == "":
        continue
    gm, gv = int(p["gols_mandante"]), int(p["gols_visitante"])
    for c, a, b in ((p["mandante"], gm, gv), (p["visitante"], gv, gm)):
        x = soma[p["temporada"]][c]
        x[0] += 1; x[1] += a > b; x[2] += a == b; x[3] += a < b; x[4] += a; x[5] += b
tot = 0
for ano in range(1948, 1968):
    t = html.unescape(re.sub(r"<[^>]+>", "", open(f"data/coleta/col-1/rsssf/col{str(ano)[2:]}.html", encoding="latin-1").read()))
    linhas = []
    for l in t.splitlines():
        m = re.match(r"^\s*\d+\.\s+(.+?)\s{2,}(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*[:-]\s*(\d+)\s+(\d+)", l)
        if m:
            linhas.append((m.group(1).strip(), [int(m.group(k)) for k in range(2, 8)]))
        elif linhas:
            break
    pac = soma[str(ano)]
    jt = sum(r[1][0] for r in linhas) // 2
    jp = sum(v[0] for v in pac.values()) // 2
    print(f"{ano}: RSSSF {len(linhas)} clubes, {jt} jogos | pacote {len(pac)} clubes, {jp} jogos" + ("   <<< DIFERE" if (jt, len(linhas)) != (jp, len(pac)) else ""))
    for nome, v in linhas:
        c = clube(nome, ano) or "?" + nome
        if pac.get(c) != v:
            print(f"    {c}: RSSSF {v} | pacote {pac.get(c)}")
            tot += 1
print("linhas divergentes:", tot)
