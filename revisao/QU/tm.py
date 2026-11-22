"""Confere placar e data com o transfermarkt (gesamtspielplan), fonte que a coleta não usou. Só leitura do banco.

Uso: python -I revisao/QU/tm.py  -> revisao/QU/tm_saida.txt
Páginas em data/cache/revisao/QU/tm/<COMP>_<saison>.html (baixadas com curl, 1 a cada 3 s).
"""
import re, sys, html, sqlite3, unicodedata, datetime as dt
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = Path(__file__).resolve().parent.parent.parent
CACHE = RAIZ / "data" / "cache" / "revisao" / "QU" / "tm"
# (arquivo, slug, temporadas do banco a casar)
ALVOS = [("URU1_2005.html", "uru-1", ["2005/06"]), ("URU1_2007.html", "uru-1", ["2007/08"]),
         ("AR1N_2018.html", "arg-1", ["2018/19"])]


def chave(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\b(ca|cd|club|atletico|fc|cs|sc|cdsc|ac|de|la|montevideo|juniors|futbol|football)\b", " ", re.sub(r"[^a-z0-9]+", " ", s))
    return re.sub(r"\s+", " ", s).strip()


def ler_tm(f):
    t = f.read_bytes().decode("utf-8", "replace")
    out, data = [], None
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", t, re.S):
        md = re.search(r'datum/(\d{4}-\d\d-\d\d)">', tr)
        if md:
            data = md.group(1)
        h = re.search(r'<td class="text-right no-border-rechts hauptlink">(?:<span[^>]*>[^<]*</span>(?:s|&nbsp;)*)?<a title="([^"]+)"', tr)
        r = re.search(r'class="ergebnis-link"[^>]*>([^<]+)</a>', tr)
        v = re.search(r'<td class="no-border-links hauptlink">(?:<span[^>]*>[^<]*</span>(?:s|&nbsp;)*)?<a title="([^"]+)"', tr)
        if not (h and r and v):
            continue
        g = re.match(r"(\d+):(\d+)", r.group(1).strip())
        out.append((data, html.unescape(h.group(1)), int(g.group(1)) if g else None, int(g.group(2)) if g else None, html.unescape(v.group(1))))
    return out


def main():
    c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
    nome = dict(c.execute("select clube_id, nome from clube"))
    saida = []
    for arq, slug, temps in ALVOS:
        f = CACHE / arq
        if not f.exists():
            saida.append(f"{arq}: não baixado"); continue
        tj = ler_tm(f)
        db = c.execute(f"""select p.data, p.mandante_id, p.visitante_id, p.gols_mandante, p.gols_visitante, coalesce(p.resultado_especial,''), p.fonte_id
                          from partida p join edicao e using(edicao_id) join competicao co using(competicao_id)
                          where co.slug=? and e.temporada in ({','.join('?' * len(temps))})""", (slug, *temps)).fetchall()
        k = Counter(); difs = []
        usados = set()
        for d, a, ga, gb, b in tj:
            ka, kb = chave(a), chave(b)
            cand = [r for r in db if r[6] not in usados and (chave(nome[r[1]]).startswith(ka[:7]) or ka.startswith(chave(nome[r[1]])[:7]))
                    and (chave(nome[r[2]]).startswith(kb[:7]) or kb.startswith(chave(nome[r[2]])[:7]))]
            if not cand:
                k["sem_par"] += 1; continue
            if d:
                cand.sort(key=lambda r: abs((dt.date.fromisoformat(r[0]) - dt.date.fromisoformat(d)).days) if r[0] else 9999)
            r = cand[0]; usados.add(r[6])
            k["jogos"] += 1
            ok = (r[3], r[4]) == (ga, gb) or r[5] in ("wo", "awd")
            k["placar_ok" if ok else "placar_dif"] += 1
            if r[0] == d:
                k["data_igual"] += 1
            else:
                k["data_dif"] += 1
                difs.append(f"   TM {d} {a} {ga}-{gb} {b} | banco {r[0]} {nome[r[1]]} {r[3]}-{r[4]} {nome[r[2]]} | {r[6]}")
            if not ok:
                difs.append(f"   PLACAR TM {d} {a} {ga}-{gb} {b} | banco {r[0]} {nome[r[1]]} {r[3]}-{r[4]} {nome[r[2]]} | {r[6]}")
        saida.append(f"== {arq} ({slug} {temps}): {len(tj)} jogos no TM; {dict(k)}")
        saida += difs[:60]
    (RAIZ / "revisao" / "QU" / "tm_saida.txt").write_text("\n".join(saida) + "\n", encoding="utf-8")
    print("\n".join(l for l in saida if l.startswith("==")))


if __name__ == "__main__":
    main()
