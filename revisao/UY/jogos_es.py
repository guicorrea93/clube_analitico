"""Bloco C: jogos do banco x fixture das páginas da Wikipédia es de cada edição (só nas edições em que a coleta usou a
RSSSF como base: 1932-1959, 1965 e 1994-2025). Compara placar e, quando a es traz, a data.
Uso: python -I revisao/UY/jogos_es.py [temporada ...] > SCRATCH/UY/jogos_es.txt"""
import re, sqlite3, sys
from collections import defaultdict
sys.path.insert(0, "revisao/UY")
from tabelas_es import clube, limpa, pagina  # noqa: E402

MESES = {m: i for i, m in enumerate(["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
                                     "septiembre", "octubre", "noviembre", "diciembre"], 1)}
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
nome = dict(c.execute("select clube_id, nome from clube"))


def jogos_es(txt, ano, ano_fim):
    txt = limpa(txt)
    out = []
    for tab in re.findall(r"\{\|.*?\n\|\}", txt, flags=re.S):
        if not re.search(r"Fecha|Jornada|Resultado", tab):
            continue
        data = None
        for row in re.split(r"\n\|-[^\n]*", tab):
            links = re.findall(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", row)
            times = [(a, b) for a, b in links if not re.match(r"(Estadio|Parque|Gran Parque|Archivo)", a)
                     and not re.search(r"Estadio|Parque [A-Z]|Campe[oó]n del Siglo", b or a)]
            pl = None   # placar: a linha logo depois do 1º clube (pode vir com "bgcolor=...|")
            lin = row.split("\n")
            k1 = next((k for k, x in enumerate(lin) if "[[" in x and not re.search(r"Estadio|Archivo", x)), None)
            for x in (lin[k1 + 1:k1 + 2] if k1 is not None else []):
                pl = re.match(r"\|(?:[^|]*\|)?\s*'*\s*(\d+)\s*[-:–]\s*(\d+)\b", x.strip())
            d = re.search(r"(\d{1,2}) de (" + "|".join(MESES) + r")(?: de (\d{4}))?", row)
            if d:
                mes = MESES[d.group(2)]
                a = int(d.group(3)) if d.group(3) else (ano if (ano_fim == ano or mes >= 7) else ano_fim)
                data = f"{a:04d}-{mes:02d}-{int(d.group(1)):02d}"
            if len(times) >= 2 and pl:
                m = clube(times[0][0], times[0][1] or times[0][0], ano)
                v = clube(times[1][0], times[1][1] or times[1][0], ano)
                out.append((m, v, int(pl.group(1)), int(pl.group(2)), data if d or "rowspan" in tab else None))
    return out


if __name__ == "__main__":
    filtro = set(sys.argv[1:])
    eds = c.execute("""select edicao_id, temporada, ano_inicio, ano_fim from edicao e join competicao co using(competicao_id)
                       where slug='uru-1' order by ano_inicio, temporada""").fetchall()
    tot = defaultdict(int)
    for eid, temp, ano, ano_fim in eds:
        base_rsssf = 1932 <= ano <= 1959 or ano == 1965 or ano >= 1994
        if (filtro and temp not in filtro) or not base_rsssf:
            continue
        p, url = pagina(temp)
        if not p:
            continue
        es = jogos_es(open(p, encoding="utf-8").read(), ano, ano_fim)
        db = defaultdict(list)
        for pid, m, v, gm, gv, data, fase, esp in c.execute(
                """select partida_id, mandante_id, visitante_id, gols_mandante, gols_visitante, data, f.nome,
                          coalesce(resultado_especial,'') from partida p join fase f using(fase_id) where p.edicao_id=?""", (eid,)):
            db[(nome[m], nome[v])].append((gm, gv, data, fase, esp))
        casou = igual = 0
        difs = []
        for m, v, gm, gv, data in es:
            cand = db.get((m, v))
            if not cand:
                continue
            casou += 1
            alvo = [x for x in cand if (x[0], x[1]) == (gm, gv)]
            if alvo:
                igual += 1
                if data and not any(x[2] == data for x in alvo):
                    difs.append(f"data: {m} {gm}-{gv} {v}: es {data}, banco {[x[2] for x in alvo]}")
            else:
                difs.append(f"placar: {m} x {v}: es {gm}-{gv}, banco {[(x[0], x[1], x[3], x[4]) for x in cand]}")
        tot["es"] += len(es)
        tot["casou"] += casou
        tot["igual"] += igual
        print(f"== {temp}: es {len(es)} jogos lidos, {casou} achados no banco, {igual} com o mesmo placar ({url})")
        for d in difs:
            print("   ", d)
    print("TOTAL", dict(tot))
