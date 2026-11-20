"""Revisão Série C (SC): lista jogos do pacote. Uso: python revisao/SC/jogos.py ANO [clube ...] [--fase X]"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from comum import ler_csv  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
args = sys.argv[1:]
ano = args.pop(0)
fase = None
if "--fase" in args:
    i = args.index("--fase"); fase = args[i + 1]; del args[i:i + 2]
for r in ler_csv("partidas.csv"):
    if r["temporada"] != ano or (fase and fase.lower() not in r["fase"].lower()):
        continue
    if args and not any(a.lower() in (r["mandante"] + "|" + r["visitante"]).lower() for a in args):
        continue
    print(r["id"], r["fase"], r["grupo"], r["data"], r["mandante"], r["gols_mandante"], "x", r["gols_visitante"], r["visitante"],
          r["fonte"], r["fonte_id"], r["resultado_especial"], r["observacao"][:60])
