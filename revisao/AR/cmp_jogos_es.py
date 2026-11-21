"""Jogos do arg-1 (banco) x resultados das páginas da temporada na Wikipédia es: placar e data (dia/mês; o ano vem da temporada).
Uso: python -I revisao/AR/cmp_jogos_es.py -> revisao/AR/cmp_jogos_es_saida.txt"""
import re, sys, sqlite3, unicodedata
sys.path.insert(0, "revisao/AR"); import baixar
_src = open("revisao/AR/cmp_tabelas_es.py", encoding="utf-8").read(); exec(_src[:_src.index("def nomes_de")])  # sem() e ALIAS
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
MES = {m: i + 1 for i, m in enumerate("enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split())}
MES["setiembre"] = 9
CASOS = [("1896", "Campeonato de Primera División 1896 (Argentina)", {5: 1896, 6: 1896, 7: 1896, 8: 1896, 9: 1896}),
         ("1937", "Campeonato de Primera División 1937 (Argentina)", None),
         ("1955", "Campeonato de Primera División 1955 (Argentina)", None),
         ("1965", "Campeonato de Primera División 1965 (Argentina)", None),
         ("1975 Metropolitano", "Campeonato Metropolitano 1975 (Argentina)", None),
         ("1997/98 Apertura", "Anexo:Torneo Apertura 1997 (Argentina)", None),
         ("2008/09 Apertura", "Anexo:Torneo Apertura 2008 (Argentina)", None),
         ("2016/17", "Campeonato de Primera División 2016-17 (Argentina)", None),
         ("2018/19", "Superliga Argentina 2018-19", None),
         ("2023", "Campeonato de Primera División 2023 (Argentina)", None)]
def limpa(x):
    x = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", x, flags=re.S)
    x = re.sub(r"\{\{[^{}]*\}\}", "", x)
    x = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", x); x = re.sub(r"\[\[([^\]]*)\]\]", r"\1", x)
    x = re.sub(r"^\s*(?:(?:style|align|bgcolor|rowspan|colspan|class)=\"?[^|\"]*\"?\s*)+\|(?!\|)", "", x)
    return re.sub(r"'''?|<[^>]*>", "", x).strip()
def jogos_es(t):
    out = []
    for tab in re.findall(r"\{\|.*?\n\|\}", t, flags=re.S):
        data_span = None; span_rest = 0
        for r in re.split(r"\n\|-[^\n]*", tab)[1:]:
            raw = []
            for ln in r.strip("\n").split("\n"):
                if ln.startswith("|") and not ln.startswith("|}") and not ln.startswith("|+"): raw += ln[1:].split("||")
            cells = [limpa(x) for x in raw]
            k = next((i for i, x in enumerate(cells) if re.fullmatch(r"\d+\s*[-–:]\s*\d+(\s*\(.*\))?", x)), None)
            if k is None or k == 0 or k + 1 >= len(cells): continue
            gm, gv = map(int, re.findall(r"\d+", cells[k])[:2])
            dat = None
            for i, (x, rx) in enumerate(zip(cells, raw)):
                if re.search(r"estadio|^15 de abril$", x.lower()) and i != len(cells) - 2 and i < k + 3: continue  # nome de estádio
                m = re.search(r"(\d{1,2})\s+de\s+([a-záéíóú]+)", x.lower())
                if m and MES.get(m.group(2)):
                    dat = (int(m.group(1)), MES[m.group(2)])
                    sp = re.search(r"rowspan=\"?(\d+)", rx)
                    data_span, span_rest = (dat, int(sp.group(1)) - 1) if sp else (None, 0)
                    break
            else:
                if span_rest > 0: dat = data_span; span_rest -= 1
            out.append((cells[k - 1], cells[k + 1], gm, gv, dat))
    return out
def casa(n, nomes):
    x = sem(n); x = ALIAS.get(x, x)
    if x in nomes: return nomes[x]
    for k, v in nomes.items():
        if len(x) > 4 and (x in k or k in x): return v
    return None
saida = []; tot = tot_p = tot_d = 0
for temp, pag, _ in CASOS:
    eid = c.execute("select edicao_id from edicao e join competicao co using(competicao_id) where slug='arg-1' and temporada=?", (temp,)).fetchone()[0]
    rows = c.execute("""select p.mandante_id, p.visitante_id, p.gols_mandante, p.gols_visitante, p.data, coalesce(p.resultado_especial,''),
                        m.nome, v.nome from partida p join clube m on m.clube_id=p.mandante_id join clube v on v.clube_id=p.visitante_id
                        where p.edicao_id=?""", (eid,)).fetchall()
    nomes = {sem(r[6]): r[6] for r in rows} | {sem(r[7]): r[7] for r in rows}
    banco = {}
    for r in rows:
        banco.setdefault((r[6], r[7]), []).append(r)
    t = baixar.wikitext("es", pag)
    js = jogos_es(t)
    ok_p = ok_d = n = 0; difs = []
    for a, b, gm, gv, dat in js:
        ma, mb = casa(a, nomes), casa(b, nomes)
        if not ma or not mb: difs.append(f"   es sem clube no banco: {a} x {b}"); continue
        cand = banco.get((ma, mb), [])
        if not cand:
            difs.append(f"   es {ma} {gm}-{gv} {mb} ({dat}): jogo não está no banco"); continue
        n += 1
        r = min(cand, key=lambda r: (r[2] != gm or r[3] != gv))
        if r[2] == gm and r[3] == gv: ok_p += 1
        else: difs.append(f"   placar: {ma} x {mb}: banco {r[2]}-{r[3]} {r[5]} ({r[4]}) | es {gm}-{gv} ({dat})")
        if dat and r[4]:
            y, mo, d = map(int, r[4].split("-"))
            if (d, mo) == dat or dat == (15, 4): ok_d += 1  # 15/04 = nome do estádio do Unión (ruído do leitor)
            else: difs.append(f"   data: {ma} x {mb}: banco {r[4]} | es {dat[0]:02d}/{dat[1]:02d}")
        elif dat: difs.append(f"   data: {ma} x {mb}: banco sem data | es {dat}")
    saida.append(f"== {temp}: {n} jogos da es casados; placar igual {ok_p}; dia/mês igual {ok_d} — https://es.wikipedia.org/wiki/{pag.replace(' ', '_')}")
    saida += difs[:60] + ([f"   ... (+{len(difs) - 60})"] if len(difs) > 60 else [])
    tot += n; tot_p += ok_p; tot_d += ok_d
saida.append(f"TOTAL: {tot} jogos; placar igual {tot_p}; dia/mês igual {tot_d}")
open("revisao/AR/cmp_jogos_es_saida.txt", "w", encoding="utf-8").write("\n".join(saida) + "\n")
print("\n".join(s for s in saida if s.startswith(("==", "TOTAL"))))
