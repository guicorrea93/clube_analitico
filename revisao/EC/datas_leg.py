"""Datas escritas na página da RSSSF no título do bloco ("First Leg [Dec 12]", "Second Legs [Jul 10]", "Final [Dec 18, Quito]")
x data do jogo no pacote. Lê a página pelo leitor da coleta (só leitura) e olha até 8 linhas acima de cada jogo."""
import sys; sys.stdout.reconfigure(encoding="utf-8")
import csv, re
sys.path.insert(0, "coleta/ecu-1"); sys.path.insert(0, "coleta/comum-sulamerica")
from ler_rsssf import linhas
MES = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}
n = dif = 0
for r in csv.DictReader(open("data/coleta/ecu-1/pacote/partidas.csv", encoding="utf-8")):
    m = re.match(r"rsssf:(\w+):(\d+)", r["fonte_id"])
    if not m: continue
    pg, ln = m.group(1), int(m.group(2))
    ls = linhas(pg)
    for k in range(ln - 1, max(ln - 9, 0), -1):
        s = ls[k].strip()
        if re.match(r"^\[|^Round|^Fecha", s): break   # bloco com data própria: o leitor já lê
        mm = re.match(r"^(First|Second|Third)? ?(Leg|Legs|Final|Match|Replay|Semifinals?|Quarterfinals?)\b.*\[(\w{3}) (\d{1,2})(?:,\s*(\d{4}))?", s)
        if mm:
            n += 1
            ano = int(mm.group(5)) if mm.group(5) else int(r["data"][:4]) if r["data"] else int(r["temporada"][:4])
            d = f"{ano:04d}-{MES[mm.group(3)]:02d}-{int(mm.group(4)):02d}"
            if d != r["data"]:
                dif += 1
                print(r["temporada"], r["fase"], r["rodada"], "pacote:", r["data"] or "(vazio)", "| página:", d, f"({s})", "|", r["mandante"], r["gols_mandante"], "x", r["gols_visitante"], r["visitante"], "|", r["fonte_id"])
            break
print("jogos com data no título do bloco:", n, "| data diferente:", dif)
