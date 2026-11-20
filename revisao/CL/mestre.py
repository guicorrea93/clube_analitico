"""Revisão CL (clubes e escudos): tabela-mestre de clubes do futebol.db e do painel.

Saída: SCRATCH/CL/mestre.json e mestre.csv (um clube por linha: id, nome, exibição, UF, cidade, nome_completo,
anos por competição, nomes de fonte, arquivo de escudo que o painel mostra).
Só leitura do banco. Uso: python revisao/CL/mestre.py <SCRATCH>
"""
import csv
import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(sys.argv[1]) / "CL"
SLUGS = ["bra-serie-a", "bra-serie-b", "bra-serie-c", "bra-serie-d", "bra-copa-do-brasil"]

con = sqlite3.connect(f"file:{ROOT / 'db' / 'futebol.db'}?mode=ro", uri=True)
clubes = {r[0]: dict(id=r[0], nome=r[1], regiao=r[2], cidade=r[3], nome_completo=r[4], escudo_db=r[5], obs=r[6])
          for r in con.execute("SELECT clube_id, nome, regiao, cidade, nome_completo, escudo, observacao FROM clube")}
for c in clubes.values():
    c["anos"] = {}
    c["nomes"] = []
q = """SELECT c.slug, e.ano_inicio, x.cid FROM (
         SELECT edicao_id, mandante_id cid FROM partida UNION SELECT edicao_id, visitante_id FROM partida
         UNION SELECT edicao_id, clube_id FROM classificacao_final) x
       JOIN edicao e USING (edicao_id) JOIN competicao c USING (competicao_id)"""
for slug, ano, cid in con.execute(q):
    clubes[cid]["anos"].setdefault(slug, set()).add(ano)
for cid, nome, fonte, a1, a2 in con.execute("SELECT clube_id, nome, fonte, ano_inicio, ano_fim FROM clube_nome"):
    clubes[cid]["nomes"].append(f"{fonte}:{nome}:{a1 or ''}-{a2 or ''}")

# escudos do painel (ESCUDOS no index.html) por nome de exibição
html = (ROOT / "painel" / "index.html").read_text(encoding="utf-8")
m = re.search(r"ESCUDOS = (\{.*?\});", html)
ESC = json.loads(m.group(1))
sys.path.insert(0, str(ROOT))
from gerar_dashboard_v2 import nome as exib  # noqa: E402

# nomes que aparecem nos dados de cada competição do painel (PART)
painel = {}
for s in SLUGS:
    t = (ROOT / "painel" / "dados" / f"{s}.js").read_text(encoding="utf-8")
    d = json.loads(t[t.index("{"):].rstrip().rstrip(";"))
    painel[s] = set(d["PART"].keys())

linhas = []
for c in clubes.values():
    c["exib"] = exib(c["nome"])
    c["escudo_painel"] = ESC.get(c["exib"])
    c["anos"] = {k: sorted(v) for k, v in c["anos"].items()}
    c["no_painel"] = [s for s in SLUGS if c["exib"] in painel[s]]
    c["primeira"] = next((s for s in SLUGS if s in c["anos"]), "")
    linhas.append(c)
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "mestre.json").write_text(json.dumps(linhas, ensure_ascii=False, indent=0), encoding="utf-8")
with (OUT / "mestre.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "nome", "exib", "uf", "cidade", "nome_completo", "primeira", "anos", "escudo_painel", "nomes"])
    for c in sorted(linhas, key=lambda c: c["exib"]):
        anos = "; ".join(f"{k[4:]}:{v[0]}-{v[-1]}({len(v)})" for k, v in c["anos"].items())
        w.writerow([c["id"], c["nome"], c["exib"], c["regiao"], c["cidade"], c["nome_completo"], c["primeira"], anos,
                    c["escudo_painel"] or "", " | ".join(c["nomes"])])
print(len(linhas), "clubes;", sum(1 for c in linhas if c["anos"]), "com jogos;",
      {s: len(painel[s]) for s in SLUGS})
sem = [c["exib"] for c in linhas if c["anos"] and not c["escudo_painel"]]
print("sem escudo no painel:", len(sem))
fora = {s: sorted(painel[s] - {c["exib"] for c in linhas}) for s in SLUGS}
print("nomes do painel sem clube no banco:", {k: v for k, v in fora.items() if v})
