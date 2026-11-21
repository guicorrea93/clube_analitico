"""Bloco C: jogos (placar e mando) do banco contra os jogos listados na Wikipédia pt da edição.
Lê: listas de texto "dd/m Time a-b Time", tabelas de jogos (wikitable) e o módulo sports results (match_X_Y).
Uso: python -I revisao/SP/cmp_jogos.py 1909 1955 2022 ...  Saída: revisao/SP/saida_jogos.txt"""
import sys as _s; _s.stdout.reconfigure(encoding="utf-8")
import difflib, json, os, re, sqlite3, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baixar import wikitext
from listas_campeoes import limpa
from nomes import MAPA
AQUI = os.path.dirname(os.path.abspath(__file__))
INFO = json.load(open(os.path.join(AQUI, "infobox.json"), encoding="utf-8"))
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)


def k(x):
    x = re.sub(r"\(.*?\)", "", x)
    return unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode().lower().strip()


EXTRA = {"sao paulo ac": "São Paulo Athletic", "aa palmeiras": "AA das Palmeiras", "internacional": "SC Internacional-SP",
         "americano": "Americano-SP", "palestra italia": "Palmeiras", "palestra": "Palmeiras", "red bull brasil": "Red Bull Bragantino II",
         "gremio novorizontino": "Novorizontino", "red bull bragantino": "Bragantino", "agua santa": "EC Água Santa",
         "inter de limeira": "Inter de Limeira", "sao paulo": "São Paulo", "hespanha": "Jabaquara"}


def casa(nome, clubes):
    kk = k(nome)
    for d in (EXTRA, {kk2: v for kk2, v in MAPA.items()}):
        if kk in d and d[kk] in clubes:
            return d[kk]
    for cl in clubes:
        if k(cl) == kk or k(cl).replace("-sp", "") == kk:
            return cl
    m = difflib.get_close_matches(kk, [k(x) for x in clubes], n=1, cutoff=0.6)
    if m:
        return next(x for x in clubes if k(x) == m[0])
    cand = [x for x in clubes if kk and (kk in k(x) or k(x).replace("-sp", "") in kk)]
    return cand[0] if len(cand) == 1 else None


def jogos_wiki(txt):
    out = []
    # 1) sports results
    for bloco in re.findall(r"\{\{#invoke:sports results\|main(.*?)\n\}\}", txt, re.S):
        nomes = {m.group(1): limpa(m.group(2)) for m in re.finditer(r"\|name_([A-Za-z0-9]+)[ \t]*=[ \t]*(.+)", bloco)}
        for m in re.finditer(r"\|match_([A-Za-z0-9]+)_([A-Za-z0-9]+)[ \t]*=[ \t]*(.*)", bloco):
            s = limpa(m.group(3))
            mm = re.search(r"(\d+)\s*[–\-−x×]\s*(\d+)", s)
            if mm and m.group(1) in nomes and m.group(2) in nomes:
                out.append((None, nomes[m.group(1)], int(mm.group(1)), int(mm.group(2)), nomes[m.group(2)]))
    # 2) linhas de texto
    for ln in txt.split("\n"):
        l = limpa(ln).strip()
        m = re.match(r"^(\d{1,2}/\d{1,2}(?:/\d{2,4})?)\s+(.+?)\s+(\d+)\s*[-–x×]\s*(\d+)\s+(.+?)\s*(?:\(.*)?$", l)
        if m:
            out.append((m.group(1), m.group(2).strip(), int(m.group(3)), int(m.group(4)), m.group(5).strip()))
    # 3) tabelas: linhas com data | mandante | placar | visitante
    for row in re.split(r"\n\|-[^\n]*", txt):
        cels = []
        for l in row.split("\n"):
            if l.startswith("|") and not l.startswith("|}") and not l.startswith("{|"):
                for cc in re.split(r"\|\|", l[1:]):
                    mm = re.match(r"\s*(?:[a-z\-]+\s*=\s*\"?[^|\"]*\"?\s*)+\|(.*)", cc)
                    cels.append(limpa(mm.group(1) if mm else cc))
        for i in range(1, len(cels) - 1):
            mm = re.fullmatch(r"(\d+)\s*[–\-−x×]\s*(\d+)", cels[i])
            if mm and cels[i - 1] and cels[i + 1] and not re.match(r"\d", cels[i - 1]) and not re.match(r"\d", cels[i + 1]):
                out.append((cels[0] if i > 1 else None, cels[i - 1], int(mm.group(1)), int(mm.group(2)), cels[i + 1]))
                break
    return out


if __name__ == "__main__":
    res = []
    total = {"lidos": 0, "achados": 0, "placar_igual": 0}
    for temp in sys.argv[1:]:
        kk = temp if temp in INFO else temp.split(" ")[0]
        txt = wikitext(INFO[kk]["titulo"], "pt")
        eid = c.execute("select edicao_id from edicao where competicao_id=7 and temporada=?", (temp,)).fetchone()[0]
        db = c.execute("""select p.data, m.nome, p.gols_mandante, p.gols_visitante, v.nome, f.nome from partida p join clube m on m.clube_id=mandante_id
                          join clube v on v.clube_id=visitante_id join fase f using(fase_id) where p.edicao_id=?""", (eid,)).fetchall()
        clubes = sorted({x for r in db for x in (r[1], r[4])})
        wj = jogos_wiki(txt)
        usados = set()
        st = {"lidos": 0, "achados": 0, "placar_igual": 0}
        linhas = []
        for d, a, ga, gb, b in wj:
            ca, cb = casa(a, clubes), casa(b, clubes)
            if not ca or not cb or ca == cb:
                continue
            st["lidos"] += 1
            cand = [i for i, r in enumerate(db) if i not in usados and r[1] == ca and r[4] == cb]
            cand_inv = [i for i, r in enumerate(db) if i not in usados and r[1] == cb and r[4] == ca]
            ok = [i for i in cand if (db[i][2], db[i][3]) == (ga, gb)]
            if ok:
                usados.add(ok[0]); st["achados"] += 1; st["placar_igual"] += 1
                continue
            ok_inv = [i for i in cand_inv if (db[i][2], db[i][3]) == (gb, ga)]
            if ok_inv:
                usados.add(ok_inv[0]); st["achados"] += 1; st["placar_igual"] += 1
                linhas.append(f"   mando invertido: wiki {d} {ca} {ga}-{gb} {cb} | banco {db[ok_inv[0]][0]} {cb} {gb}-{ga} {ca}")
                continue
            if cand or cand_inv:
                i = (cand or cand_inv)[0]
                usados.add(i); st["achados"] += 1
                linhas.append(f" ≠ placar: wiki {d} {ca} {ga}-{gb} {cb} | banco {db[i][0]} {db[i][1]} {db[i][2]}-{db[i][3]} {db[i][4]} ({db[i][5]})")
            else:
                linhas.append(f" ? só na wiki: {d} {ca} {ga}-{gb} {cb}  ('{a}' x '{b}')")
        for kx in total: total[kx] += st[kx]
        res.append(f"== {temp}: banco {len(db)} jogos; wiki lidos {st['lidos']}, achados no banco {st['achados']}, placar igual {st['placar_igual']}")
        res += linhas
    res.append(str(total))
    open(os.path.join(AQUI, "saida_jogos.txt"), "w", encoding="utf-8").write("\n".join(res) + "\n")
    print("\n".join(res))
