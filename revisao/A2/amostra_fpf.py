"""Amostra de jogos (placar e data) contra a FPF (futebolpaulista.com.br, Handlers/Competicoes/ListarTabela.ashx).
Fonte que a coleta NÃO usou. Uso: python -I revisao/A2/amostra_fpf.py 2012:1,2 2016:3 ..."""
import sys, os, json, csv, re, unicodedata
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
from baixar import get
def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\b(ec|fc|ac|aa|ae|ad|sc|saf|ca|ge|clube|futebol|esporte|-sp|sp|ii|b)\b", " ", s.replace("-", " "))
    return set(w for w in s.split() if len(w) > 2)
ALIAS = {"osasco sporting": "oeste", "red bull brasil": "bragantino", "audax": "osasco audax", "lemense": "lemense atibaia", "gremio prudente": "barueri prudente"}
pac = [r for r in csv.DictReader(open("data/coleta/bra-sp-2/pacote/partidas.csv", encoding="utf-8"))]
ok = dif = nao = 0; linhas = []
for arg in sys.argv[1:]:
    ano, rds = arg.split(":")
    for rd in rds.split(","):
        t = get(f"https://futebolpaulista.com.br/Handlers/Competicoes/ListarTabela.ashx?IdCampeonato=74&Ano={ano}&Rodada={rd}", "fpf", ".json")
        for j in (json.loads(t)["Retorno"].get("listTabela") or []):
            d = "-".join(reversed(j["Data"].split("/")))
            m, v = j["NomePopularMandante"], j["NomePopularVisitante"]
            nm, nv = norm(ALIAS.get(m.lower(), m)), norm(ALIAS.get(v.lower(), v))
            cand = [p for p in pac if p["temporada"] == ano and p["data"] and abs((date.fromisoformat(p["data"]) - date.fromisoformat(d)).days) <= 4
                    and (norm(p["mandante"]) & nm) and (norm(p["visitante"]) & nv)]
            if not cand:
                nao += 1; linhas.append(f"NAO ACHADO {ano} r{rd} {d} {m} {j['ResultadoMandante']}x{j['ResultadoVisitante']} {v}"); continue
            p = cand[0]
            pl = (str(j["ResultadoMandante"]), str(j["ResultadoVisitante"])) == (p["gols_mandante"], p["gols_visitante"])
            dt = p["data"] == d
            if pl and dt: ok += 1
            else:
                dif += 1
            linhas.append(f"{'OK ' if pl and dt else 'DIF'} {ano} r{rd} FPF {d} {m} {j['ResultadoMandante']}x{j['ResultadoVisitante']} {v} | pacote {p['data']} {p['mandante']} {p['gols_mandante']}x{p['gols_visitante']} {p['visitante']}")
print("\n".join(linhas)); print(f"\nbateu {ok}, difere {dif}, não achado {nao}")
