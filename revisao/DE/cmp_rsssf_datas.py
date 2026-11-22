"""Datas, placares e autores dos gols: pacote ger-1 x páginas da RSSSF por temporada (tablesd/duitNN.html, as mesmas que a
coleta baixou só para a tabela final). A RSSSF dá a data de cada rodada ("Round 10 [Sep 30]") e, dentro dela, a de cada
grupo de jogos ("[Oct 1]"); dá também os autores dos gols com minuto, de 1963/64 a 1998/99.
Os nomes curtos da RSSSF ("K'lautern", "TB Berlin") são casados com os clubes por votação (mesma rodada e mesmo placar).
Uso: python -I revisao/DE/cmp_rsssf_datas.py > revisao/DE/cmp_rsssf_datas_saida.txt"""
import csv, re, html, sys, pathlib
from collections import defaultdict, Counter
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
AQUI = pathlib.Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "coleta" / "ger-1"))
from edicoes import rsssf_url  # noqa
PAC = RAIZ / "data" / "coleta" / "ger-1" / "pacote"
MES = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}
jogos = defaultdict(list)
for r in csv.DictReader(open(PAC / "partidas.csv", encoding="utf-8")):
    jogos[int(r["temporada"][:4])].append(r)
LINHA = re.compile(r"^(\S.{0,14}?\S)\s+(\d+)-(\d+)\s+(\S.{0,14}?\S)(?:\s{2,}|\s*\(|\s*$)(.*)$")


def pagina(a):
    b = (RAIZ / "data" / "coleta" / "ger-1" / "rsssf" / rsssf_url(a).rsplit("/", 1)[1]).read_bytes().decode("latin-1")
    return html.unescape(re.sub(r"<[^>]+>", "", b)).replace("\r", "")


def ler(a):
    """Lista de (rodada, data, mandante_rsssf, visitante_rsssf, gm, gv, texto_autores)."""
    t = pagina(a)
    res, rod, dt = [], None, None
    linhas = t.split("\n")
    k = 0
    while k < len(linhas):
        l = linhas[k]
        m = re.match(r"^Round (\d+)\s*\[(\w{3})\s+(\d+)", l)
        if m:
            rod = int(m.group(1)); dt = (m.group(2), int(m.group(3)))
        else:
            m2 = re.match(r"^\[(\w{3})\s+(\d+)\]", l.strip())
            if m2 and rod:
                dt = (m2.group(1), int(m2.group(2)))
            else:
                m3 = LINHA.match(l)
                if m3 and rod and dt and m3.group(1).strip()[0].isalpha():
                    aut = m3.group(5)
                    while aut.count("(") > aut.count(")") and k + 1 < len(linhas) and linhas[k + 1].startswith(" "):
                        k += 1; aut += " " + linhas[k].strip()
                    mes = MES.get(dt[0][:3].title())
                    if mes:
                        ano = a if mes >= 7 else a + 1
                        try:
                            d = date(ano, mes, dt[1]).isoformat()
                        except ValueError:
                            d = None
                        res.append((rod, d, m3.group(1).strip(), m3.group(4).strip(), int(m3.group(2)), int(m3.group(3)), aut))
        k += 1
    return res


def autores(txt, gm, gv):
    """Conta os gols com autor no texto "(A 10, 20, B 30 p - C 40)" de cada lado."""
    m = re.search(r"\(([^()]*(?:\([^()]*\)[^()]*)*)\)", txt)
    if not m:
        return None
    lados = m.group(1).split(" - ") if " - " in m.group(1) else ([m.group(1), ""] if gm else ["", m.group(1)])
    if len(lados) != 2:
        return None
    return tuple(len(re.findall(r"\d+", re.sub(r"\[.*?\]", "", s))) for s in lados)


def mapa_rsssf(a):
    """(mandante, visitante) do pacote -> (data, rodada) da RSSSF."""
    rs = ler(a); pk = jogos[a]
    votos = defaultdict(Counter); por = defaultdict(list)
    for p in pk:
        por[(int(p["rodada"]), int(p["gols_mandante"]), int(p["gols_visitante"]))].append(p)
    for r, d, m, v, gm, gv, _ in rs:
        c = por.get((r, gm, gv), [])
        if len(c) == 1:
            votos[m][c[0]["mandante"]] += 1; votos[v][c[0]["visitante"]] += 1
    mp = {k: c.most_common(1)[0][0] for k, c in votos.items()}
    return {(mp.get(m), mp.get(v)): (d, r) for r, d, m, v, gm, gv, _ in rs}


if __name__ == "__main__":
    tot = Counter()
    for a in range(1963, 1999):
        rs = ler(a)
        pk = jogos[a]
        # votação: nome curto da RSSSF -> clube (mesma rodada e mesmo placar, quando só um jogo serve)
        votos = defaultdict(Counter)
        por = defaultdict(list)
        for p in pk:
            por[(int(p["rodada"]), int(p["gols_mandante"]), int(p["gols_visitante"]))].append(p)
        for r, d, m, v, gm, gv, _ in rs:
            c = por.get((r, gm, gv), [])
            if len(c) == 1:
                votos[m][c[0]["mandante"]] += 1; votos[v][c[0]["visitante"]] += 1
        mapa = {k: c.most_common(1)[0][0] for k, c in votos.items()}
        idx = {(p["mandante"], p["visitante"]): p for p in pk}
        dif_d, dif_p, sem, aut_ok, aut_n = [], [], 0, 0, 0
        vistos = set()
        for r, d, m, v, gm, gv, txt in rs:
            cm, cv = mapa.get(m), mapa.get(v)
            p = idx.get((cm, cv))
            if not p or (cm, cv) in vistos:
                sem += 1; continue
            vistos.add((cm, cv))
            tot["jogos"] += 1
            if (int(p["gols_mandante"]), int(p["gols_visitante"])) != (gm, gv):
                dif_p.append(f"{cm} x {cv} (rodada {r}): pacote {p['gols_mandante']}-{p['gols_visitante']} | RSSSF {gm}-{gv}")
            if d and p["data"] and p["data"] != d:
                dd = abs((date.fromisoformat(p["data"]) - date.fromisoformat(d)).days)
                dif_d.append((dd, f"{cm} x {cv} (rodada {p['rodada']}): pacote {p['data']} | RSSSF {d} (rodada {r}) [{dd} dias]"))
            au = autores(txt, gm, gv)
            if gm + gv:
                aut_n += 1
                if au == (gm, gv):
                    aut_ok += 1
        tot["dif_data"] += len(dif_d); tot["dif_placar"] += len(dif_p); tot["sem_par"] += sem
        tot["jogos_com_gol"] += aut_n; tot["autores_completos"] += aut_ok
        print(f"{a}/{str(a+1)[-2:]}: RSSSF {len(rs)} jogos lidos, {len(vistos)} casados, {sem} sem par; datas diferentes {len(dif_d)} "
              f"(>3 dias: {sum(1 for x, _ in dif_d if x > 3)}); placares diferentes {len(dif_p)}; autores completos em {aut_ok} de {aut_n} jogos com gol")
        for x in dif_p:
            print("    PLACAR", x)
        for dd, x in sorted(dif_d, reverse=True):
            if dd > 3 or "-v" in sys.argv:
                print("    DATA", x)
    print(dict(tot))
