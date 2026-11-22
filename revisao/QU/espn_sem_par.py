"""Jogos do arg-1 e do uru-1 (2001+) que ficaram sem a ESPN (fonte_id sem 'espn:') e que a ESPN tem com os mesmos clubes
em outra data: sinal de data errada no banco (jogo adiado gravado na data da rodada). Só leitura; usa os JSON da ESPN que a
coleta já baixou (data/coleta/<slug>/espn/).
Uso: python -I revisao/QU/espn_sem_par.py -> revisao/QU/espn_sem_par_saida.txt
"""
import json, re, sys, sqlite3, unicodedata, datetime as dt
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = Path(__file__).resolve().parent.parent.parent


def chave(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", s)).strip()


def main():
    c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
    nome = dict(c.execute("select clube_id, nome from clube"))
    # grafias da ESPN de cada clube (clube_nome com fonte espn)
    espn_nome = defaultdict(set)
    for cid, n, f in c.execute("select clube_id, nome, fonte from clube_nome"):
        if f and "espn" in f.lower():
            espn_nome[chave(n)].add(cid)
    out = []
    for slug, pref in (("arg-1", "arg1"), ("uru-1", "uru1")):
        ev = []
        for f in sorted((RAIZ / "data" / "coleta" / slug / "espn").glob(f"{pref}_*.json")):
            for e in json.load(open(f, encoding="utf-8")):
                if e.get("situacao") != "STATUS_FULL_TIME":
                    continue
                ev.append(e)
        por_par = defaultdict(list)
        for e in ev:
            por_par[(chave(e["mandante"]), chave(e["visitante"]))].append(e)
        rows = c.execute("""select e.temporada, p.data, p.mandante_id, p.visitante_id, p.gols_mandante, p.gols_visitante, p.fonte_id,
                            coalesce(p.resultado_especial,'') from partida p join edicao e using(edicao_id) join competicao co using(competicao_id)
                            where co.slug=? and e.ano_inicio>=2001 and p.fonte_id not like '%espn:%' and p.gols_mandante is not null""", (slug,)).fetchall()
        n = 0
        for temp, d, m, v, gm, gv, fid, esp in rows:
            km = {k for k, ids in espn_nome.items() if m in ids} | {chave(nome[m])}
            kv = {k for k, ids in espn_nome.items() if v in ids} | {chave(nome[v])}
            cands = [e for a in km for b in kv for e in por_par.get((a, b), [])]
            if not cands or not d:
                continue
            x = dt.date.fromisoformat(d) if re.fullmatch(r"\d{4}-\d\d-\d\d", d) else None
            if not x:
                continue
            perto = min(cands, key=lambda e: abs((dt.date.fromisoformat(e["data_hora"][:10]) - x).days))
            de = dt.date.fromisoformat(perto["data_hora"][:10])
            dias = (de - x).days
            if 1 < abs(dias) <= 120 and (str(gm), str(gv)) == (perto["gols_mandante"], perto["gols_visitante"]):
                n += 1
                out.append(f"{slug}\t{temp}\tbanco {d}\tESPN {perto['data_hora'][:16]}Z ({dias:+d} dias)\t{nome[m]} {gm}-{gv} {nome[v]}\t{fid}\tespn:{perto['id']}")
        out.append(f"# {slug}: {n} jogos sem ESPN casada que a ESPN tem (mesmo placar) em outra data")
    (RAIZ / "revisao" / "QU" / "espn_sem_par_saida.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(l for l in out if l.startswith("#")))


if __name__ == "__main__":
    main()
