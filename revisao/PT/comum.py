"""Leitura do pacote por-1 (só leitura)."""
import csv, pathlib
RAIZ = pathlib.Path(__file__).resolve().parents[2]
PAC = RAIZ / "data" / "coleta" / "por-1" / "pacote"
def ler(nome):
    with open(PAC / nome, encoding="utf-8") as f:
        return list(csv.DictReader(f))
def ano(temporada):
    return int(temporada[:4])
def partidas():
    r = ler("partidas.csv")
    for x in r:
        x["gm"] = int(x["gols_mandante"]); x["gv"] = int(x["gols_visitante"]); x["a"] = ano(x["temporada"])
    return r
