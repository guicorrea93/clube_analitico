"""Lê o histórico oficial da AUF (auf.org.uy/historico-temporadas/3/<id>/ e a tabela anual) e confere o uru-1 (banco, só leitura).

Uso: python -I revisao/QU/auf.py  -> revisao/QU/auf_saida.txt e auf_jogos.tsv
Confere: placar e data de todos os jogos (2013/14 a 2025), fases de decisão (semifinal, finais, Supercopa), a tabela anual
(1º a último, com pontos) contra a classificacao_final do banco, e o artilheiro oficial da temporada contra a tabela artilheiro.
"""
import re, sys, html, sqlite3, unicodedata, datetime as dt
from pathlib import Path
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = Path(__file__).resolve().parent.parent.parent
CACHE = RAIZ / "data" / "cache" / "revisao" / "QU"
TEMPORADAS = {2: "2013/14", 6: "2014/15", 4: "2015/16", 1: "2017", 5: "2018", 3: "2019", 7: "2020", 8: "2021", 9: "2022",
              10: "2023", 11: "2024", 12: "2025"}
APELIDO = {"def sporting": "defensor sporting", "defensor sp": "defensor sporting", "wanderers": "montevideo wanderers",
           "m c torque": "montevideo city torque", "torque": "montevideo city torque", "river plate": "river plate de montevideo",
           "liverpool": "liverpool de montevideo", "racing": "racing de montevideo", "juventud": "juventud de las piedras",
           "boston river": "boston river", "plaza colonia": "plaza colonia", "cerro largo": "cerro largo", "cerro": "cerro",
           "rampla juniors": "rampla juniors", "rampla": "rampla juniors", "sud america": "sud america", "el tanque sisley": "el tanque sisley",
           "atenas": "atenas de san carlos", "villa espanola": "villa espanola", "deportivo maldonado": "deportivo maldonado",
           "rentistas": "rentistas", "la luz": "la luz", "progreso": "progreso", "fenix": "fenix", "danubio": "danubio",
           "nacional": "nacional", "penarol": "penarol", "miramar misiones": "miramar misiones", "tacuarembo": "tacuarembo",
           "juventud de las piedras": "juventud de las piedras", "racing club": "racing de montevideo", "cerrito": "cerrito",
           "villa teresa": "villa teresa", "d maldonado": "deportivo maldonado", "dep maldonado": "deportivo maldonado",
           "c largo": "cerro largo", "p colonia": "plaza colonia", "b river": "boston river", "mc torque": "montevideo city torque",
           "m city torque": "montevideo city torque", "montevideo city torque": "montevideo city torque", "rampla jrs": "rampla juniors", "albion": "albion de montevideo", "colon": "colon de montevideo"}


def chave(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", s)).strip()


def ler(b: bytes) -> str:
    try:
        return b.decode("utf-8")
    except UnicodeDecodeError:
        return b.decode("cp1252")


def jogos_auf(i):
    t = ler((CACHE / f"auf_historico-temporadas_3_{i}_.html").read_bytes())
    # cortes por título de seção
    marcas = [(m.start(), html.unescape(m.group(1)).strip()) for m in re.finditer(r"<h3>((?:FIXTURE|Finales|SUPERCOPA|Final|Semifinal|Desempate|Definici)[^<]*)</h3>", t, re.I)]
    out = []
    for k, (ini, titulo) in enumerate(marcas):
        fim = marcas[k + 1][0] if k + 1 < len(marcas) else len(t)
        bloco = t[ini:fim]
        fecha = None
        for m in re.finditer(r'class="fecha_slider">([^<]+)<|<div class="row no-gutters align-items-center item-fixture(.*?)fecha_estadio">\s*<strong>([^<]*)</strong>\s*([^<]*)<', bloco, re.S):
            if m.group(1):
                fecha = m.group(1).strip(); continue
            corpo = m.group(2)
            nomes = re.findall(r'<span class="hidden-xs">([^<]+)</span>', corpo)
            res = re.search(r'resultado">\s*(.*?)\s*</div>', corpo, re.S)
            r = re.sub(r"<[^>]+>", " ", res.group(1)) if res else ""
            r = re.sub(r"\s+", " ", html.unescape(r)).strip()
            mr = re.match(r"^(\d+)\s*-\s*(\d+)", r)
            data = m.group(3).strip()
            md = re.match(r"(\d\d)/(\d\d)/(\d{4})", data)
            out.append({"secao": titulo, "fecha": fecha, "a": html.unescape(nomes[0]).strip() if nomes else "?",
                        "b": html.unescape(nomes[1]).strip() if len(nomes) > 1 else "?",
                        "ga": int(mr.group(1)) if mr else None, "gb": int(mr.group(2)) if mr else None, "res": r,
                        "data": f"{md.group(3)}-{md.group(2)}-{md.group(1)}" if md else "", "estadio": m.group(4).strip()})
    return out


def anual(i):
    t = ler((CACHE / f"auf_anual_{i}.html").read_bytes())
    s = re.sub(r"<[^>]+>", " | ", t)
    s = re.sub(r"(\s*\|\s*)+", "|", html.unescape(s))
    linhas = []
    for m in re.finditer(r"\|([^|0-9][^|]*?)\|([A-ZÑ]{2,4})\|(-?\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(-?\d+)", s):
        linhas.append((m.group(1).strip(), int(m.group(3)), int(m.group(4)), int(m.group(5)), int(m.group(6)), int(m.group(7)), int(m.group(8)), int(m.group(9))))
    return linhas


def goleadores(i):
    t = ler((CACHE / f"auf_historico-temporadas_3_{i}_.html").read_bytes())
    k = t.find("Goleadores de la Temporada")
    if k < 0:
        return []
    out = []
    for m in re.finditer(r'<span class="numero">(\d+)</span>.*?<h3>([^<]+)</h3>\s*<h5><span>([^<]+)</span>.*?icono-goles"></span>\s*<span>(\d+)</span>', t[k:], re.S):
        out.append((int(m.group(1)), html.unescape(m.group(2)).strip(), html.unescape(m.group(3)).strip(), int(m.group(4))))
    return out


def familia(secao):
    s = secao.upper()
    if "SUPERCOPA" in s:
        return re.compile(r"^Final$")
    if "SEMI" in s:
        return re.compile(r"Semifinal")
    if "FINAL" in s and "FIXTURE" not in s:
        return re.compile(r"^Final$")
    if "INTERMEDIO" in s:
        return re.compile(r"Intermedio")
    if "APERTURA" in s:
        return re.compile(r"Apertura")
    if "CLAUSURA" in s:
        return re.compile(r"Clausura")
    if "DESEMPATE" in s:
        return re.compile(r"Desempate")
    return None


def main():
    c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
    nome = dict(c.execute("select clube_id, nome from clube"))
    ed = {t: eid for eid, t in c.execute("select e.edicao_id, e.temporada from edicao e join competicao co using(competicao_id) where co.slug='uru-1'")}
    saida, tsv = [], ["temporada\tsecao\tdata_auf\tjogo_auf\tdata_banco\tjogo_banco\tfase_banco\tplacar\tdata"]
    tot = Counter(); por_dec = defaultdict(Counter)
    for i, temp in TEMPORADAS.items():
        aj = jogos_auf(i)
        eid = ed[temp]
        db = c.execute("""select p.partida_id, p.data, p.mandante_id, p.visitante_id, p.gols_mandante, p.gols_visitante,
                          coalesce(p.resultado_especial,''), p.fonte_id, f.nome, p.penaltis_mandante, p.penaltis_visitante
                          from partida p join fase f using(fase_id) where p.edicao_id=?""", (eid,)).fetchall()
        usados = set(); k = Counter()
        saida.append(f"\n== {temp}: {len(aj)} jogos na AUF ({Counter(j['secao'] for j in aj)}), {len(db)} no banco  https://www.auf.org.uy/historico-temporadas/3/{i}/")
        for j in aj:
            ka, kb = chave(j["a"]), chave(j["b"])
            ka, kb = APELIDO.get(ka, ka), APELIDO.get(kb, kb)
            cands = []
            for r in db:
                if r[0] in usados:
                    continue
                m_, v_ = chave(nome[r[2]]), chave(nome[r[3]])
                if {m_, v_} == {ka, kb} or (m_.startswith(ka) and v_.startswith(kb)) or (m_.startswith(kb) and v_.startswith(ka)):
                    dist = 9999
                    if j["data"] and r[1]:
                        try:
                            x = dt.date.fromisoformat(r[1]); d_ = dt.date.fromisoformat(j["data"])
                            dist = min(abs((x - d_).days), *(abs((x.replace(year=x.year + k_) - d_).days) for k_ in (-1, 1)))
                        except ValueError:
                            dist = 5000
                    if familia(j["secao"]) and not familia(j["secao"]).search(r[8]):
                        dist += 1000
                    cands.append((dist, r))
            if not cands:
                k["sem_par"] += 1
                saida.append(f"   SEM PAR  [{j['secao']} / {j['fecha']}] {j['data']} {j['a']} {j['res']} {j['b']}")
                continue
            cands.sort(key=lambda x: x[0])
            dist, r = cands[0]
            usados.add(r[0])
            pid, dd, m, v, gm, gv, esp, fid, fase, pm, pv = r
            inv = chave(nome[m]).startswith(kb) and not chave(nome[m]).startswith(ka)
            ga, gb = (j["gb"], j["ga"]) if inv else (j["ga"], j["gb"])
            ok = (gm, gv) == (ga, gb) or ga is None
            sd = "igual" if dd == j["data"] else (f"dif {(dt.date.fromisoformat(dd) - dt.date.fromisoformat(j['data'])).days:+d} dias" if dd and j["data"] else "sem data")
            k["jogos"] += 1; k["placar_ok" if ok else "placar_dif"] += 1; k["data_igual" if sd == "igual" else "data_dif"] += 1
            dec = "2010s" if temp < "2020" else "2020s"
            por_dec[dec]["jogos"] += 1; por_dec[dec]["placar_ok"] += ok; por_dec[dec]["data_igual"] += sd == "igual"
            jb = f"{nome[m]} {gm}-{gv} {nome[v]}" + (f" [{esp}]" if esp else "")
            tsv.append(f"{temp}\t{j['secao']}\t{j['data']}\t{j['a']} {j['res']} {j['b']}\t{dd}\t{jb}\t{fase}\t{'ok' if ok else 'DIF'}\t{sd}")
            decisao = re.search(r"Final|Semi|SUPERCOPA|Desempate|Definici", j["secao"], re.I)
            if not ok or sd != "igual" or decisao:
                saida.append(f"   [{j['secao']}] {j['data']} {j['a']} {j['res']} {j['b']} | banco {dd} {jb} ({fase}) | placar {'ok' if ok else 'DIF'} | data {sd}")
        for r in db:
            if r[0] not in usados:
                k["so_banco"] += 1
                saida.append(f"   SÓ NO BANCO: {r[1]} {nome[r[2]]} {r[4]}-{r[5]} {nome[r[3]]} [{r[6]}] ({r[8]})")
        tot.update(k)
        saida.append(f"   resumo {temp}: {dict(k)}")
        # tabela anual x classificacao_final
        an = anual(i)
        cf = c.execute("select posicao, clube_id, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, pontos from classificacao_final where edicao_id=? order by posicao", (eid,)).fetchall()
        saida.append(f"   TABELA ANUAL AUF ({len(an)} clubes) x classificacao_final do banco ({len(cf)}):")
        for pos, (n_, pts, pj, pg, pe, pp, gf, gc) in enumerate(an, 1):
            b = cf[pos - 1] if pos <= len(cf) else None
            bb = f"{nome[b[1]]} {b[2]}j {b[3]}-{b[4]}-{b[5]} {b[6]}-{b[7]} {b[8]}p" if b else "-"
            igual = b and chave(nome[b[1]]).startswith(APELIDO.get(chave(n_), chave(n_))[:6]) and b[2] == pj and b[8] == pts
            saida.append(f"      {pos:2d}. AUF {n_} {pj}j {pg}-{pe}-{pp} {gf}-{gc} {pts}p   | banco {bb}   {'=' if igual else 'DIF'}")
        gl = goleadores(i)
        art = c.execute("select jogador, gols from artilheiro where edicao_id=? order by gols desc", (eid,)).fetchall()
        saida.append(f"   GOLEADOR OFICIAL AUF: {gl[:3]} | banco: {art[:3]}")
    cab = [f"TOTAL: {dict(tot)}", "Por década: " + "; ".join(f"{d}: {dict(x)}" for d, x in por_dec.items())]
    (RAIZ / "revisao" / "QU" / "auf_saida.txt").write_text("\n".join(cab + saida) + "\n", encoding="utf-8")
    (RAIZ / "revisao" / "QU" / "auf_jogos.tsv").write_text("\n".join(tsv) + "\n", encoding="utf-8")
    print("\n".join(cab))


if __name__ == "__main__":
    main()
