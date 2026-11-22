"""Confere datas e placares dos jogos do Boca Juniors no arg-1 (banco, só leitura) com o historiadeboca.com.ar.

Uso: python -I revisao/QU/cmp_hdb.py            -> revisao/QU/cmp_hdb_saida.txt e cmp_hdb_jogos.tsv
Casa cada jogo da campanha (data, rival, placar) com o jogo do Boca na edição do arg-1 pelo rival (e, entre vários, pela
data mais próxima, ignorando o ano). Diz se o placar e a data batem e, se só o ano difere, quanto.
"""
import re, sys, html, sqlite3, unicodedata, datetime as dt
from pathlib import Path
from collections import defaultdict, Counter

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = Path(__file__).resolve().parent.parent.parent
CACHE = RAIZ / "data" / "cache" / "revisao" / "QU" / "hdb"

# (ano no historiadeboca, id do torneio) -> temporada do arg-1
MAPA = {
    (1913, "1000"): "1913 Asociación", (1919, "1005"): "1919 Asociación", (1919, "1015"): "1919 Asociación",
    (1920, "1002"): "1920 Asociación", (1924, "1014"): "1924 Asociación", (1925, "1009"): "1925 Asociación",
    (1926, "1010"): "1926 Asociación", (1927, "1011"): "1927", (1928, "1012"): "1928", (1929, "1013"): "1929",
    (1930, "1012"): "1930", (1931, "1"): "1931 Liga", (1937, "1"): "1937", (1937, "47"): "1937", (1939, "1"): "1939",
    (1945, "5"): "1945", (1954, "5"): "1954", (1965, "1"): "1965", (1976, "21"): "1976 Metropolitano",
    (1976, "22"): "1976 Nacional", (1977, "23"): "1977 Metropolitano", (1977, "17"): "1977 Nacional",
    (1981, "18"): "1981 Metropolitano", (1981, "20"): "1981 Nacional", (1986, "28"): "1985/86", (1987, "30"): "1986/87",
    (1989, "34"): "1988/89", (1990, "36"): "1989/90", (1990, "41"): "1990/91", (1997, "42"): "1996/97 Clausura",
    (1997, "41"): "1997/98 Apertura", (1999, "42"): "1998/99 Clausura", (1999, "41"): "1999/00 Apertura",
    (2003, "42"): "2002/03 Clausura", (2003, "41"): "2003/04 Apertura", (2006, "42"): "2005/06 Clausura",
    (2006, "44"): "2006/07 Apertura", (2007, "42"): "2006/07 Clausura", (2007, "41"): "2007/08 Apertura",
    (2008, "42"): "2007/08 Clausura", (2008, "46"): "2008/09 Apertura", (2010, "42"): "2009/10 Clausura",
    (2010, "41"): "2010/11 Apertura", (2011, "42"): "2010/11 Clausura", (2011, "41"): "2011/12 Apertura",
    (2012, "42"): "2011/12 Clausura", (2012, "48"): "2012/13 Inicial", (2017, "56"): "2016/17", (2018, "57"): "2017/18",
    (2019, "58"): "2018/19", (2020, "55"): "2019/20", (2021, "1024"): "2021", (2023, "1026"): "2023",
    (2025, "1028"): "2025 Apertura", (2025, "1029"): "2025 Clausura",
}

APELIDO = {  # nome curto do historiadeboca -> começo do nome no banco
    "r central": "rosario central", "newell s": "newell", "estudiantes lp": "estudiantes", "gimnasia lp": "gimnasia la plata",
    "ferro": "ferro carril oeste", "argentinos": "argentinos juniors", "velez": "velez", "def y justicia": "defensa y justicia",
    "chacarita": "chacarita", "san lorenzo": "san lorenzo", "racing": "racing club", "independiente": "independiente",
    "gimnasia mza": "gimnasia de mendoza", "gimnasia j": "gimnasia de jujuy", "san martin t": "san martin de tucuman",
    "san martin sj": "san martin de san juan", "san martin mza": "san martin de mendoza", "talleres c": "talleres",
    "talleres re": "talleres de remedios", "central cba": "central cordoba", "racing cba": "racing de cordoba",
    "atl tucuman": "atletico tucuman", "a tucuman": "atletico tucuman", "atl rafaela": "atletico rafaela",
    "estudiantes ba": "estudiantes de buenos aires", "sp barracas": "sportivo barracas", "dock sud": "sportivo dock sud",
    "sp palermo": "sportivo palermo", "def de belgrano": "defensores de belgrano", "gral san martin": "general san martin",
    "e porteno": "estudiantil porteno", "union": "union", "olimpo": "olimpo", "godoy cruz": "godoy cruz", "arsenal": "arsenal",
    "nueva chicago": "nueva chicago", "huracan": "huracan", "quilmes": "quilmes", "lanus": "lanus", "banfield": "banfield",
    "tigre": "tigre", "platense": "platense", "atlanta": "atlanta", "colon": "colon", "belgrano": "belgrano",
    "instituto": "instituto", "aldosivi": "aldosivi", "patronato": "patronato", "sarmiento": "sarmiento",
    "central norte": "central norte", "temperley": "temperley", "almagro": "almagro", "porteno": "porteno",
    "barracas central": "barracas central", "el porvenir": "el porvenir", "tiro federal": "tiro federal",
    "riestra": "deportivo riestra", "dep riestra": "deportivo riestra", "ind rivadavia": "independiente rivadavia",
    "mitre": "central cordoba", "sp almagro": "almagro", "sportivo del norte": "colegiales", "arg de banfield": "argentino de lomas",
    "sp buenos aires": "sportivo buenos aires", "urquiza": "general san martin", "c cordoba sde": "central cordoba de santiago",
    "ind rivadavia mza": "independiente rivadavia", "sp balcarce": "sportivo balcarce", "talleres re": "talleres de remedios", "n chicago": "nueva chicago", "dep espanol": "deportivo espanol", "d espanol": "deportivo espanol",
    "dep italiano": "deportivo italiano", "dep armenio": "deportivo armenio", "dep mandiyu": "mandiyu", "mandiyu": "mandiyu",
}


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def ler_campanha(f: Path):
    t = f.read_bytes().decode("utf-8", "replace")
    jogos = []
    for m in re.finditer(r'<td style="font-size:14px;">([^<]*)</td>\s*<td>([^<]*)</td>.*?class="fontnegra tooltip-hov"[^>]*>([^<]+)</a>'
                         r'.*?<td style="font-size:13px">([^<]*)</td>\s*<td style="font-size:11px">([^<]*)</td>', t, re.S):
        data, rodada, partido, estadio, cond = (html.unescape(x).strip() for x in m.groups())
        mp = re.match(r"^(.*?)\s+(\d+)(?:\s*\(\d+\))?\s*-\s*(.*?)\s+(\d+)(?:\s*\(\d+\))?\s*$", partido)
        if not mp:
            jogos.append((data, rodada, partido, None, None, None, None, estadio, cond)); continue
        a, ga, b, gb = mp.group(1), int(mp.group(2)), mp.group(3), int(mp.group(4))
        jogos.append((data, rodada, partido, a, ga, b, gb, estadio, cond))
    return jogos


def main():
    c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
    nome = dict(c.execute("select clube_id, nome from clube"))
    boca = c.execute("select clube_id from clube where nome='Boca Juniors'").fetchone()[0]
    ed = {t: eid for eid, t in c.execute("select e.edicao_id, e.temporada from edicao e join competicao co using(competicao_id) where co.slug='arg-1'")}
    saida, tsv = [], ["temporada\tdata_hdb\tjogo_hdb\tdata_banco\tjogo_banco\tplacar\tdata\tfonte_id"]
    resumo = defaultdict(Counter)
    por_ed = defaultdict(list)
    for (ano, tid), temp in MAPA.items():
        por_ed[temp].append((ano, tid))
    for temp, paginas in por_ed.items():
        hj, urls = [], []
        for ano, tid in paginas:
            f = CACHE / f"camp_{ano}_{tid}.html"
            if not f.exists():
                saida.append(f"{temp}: sem página ({f.name})"); continue
            urls.append((CACHE / f"url_{ano}_{tid}.txt").read_text(encoding="utf-8").strip())
            hj += ler_campanha(f)
        url = " ; ".join(urls)
        db = c.execute("""select p.partida_id, p.data, p.mandante_id, p.visitante_id, p.gols_mandante, p.gols_visitante,
                          coalesce(p.resultado_especial,''), p.fonte_id, f.nome from partida p join fase f using(fase_id)
                          where p.edicao_id=? and (p.mandante_id=? or p.visitante_id=?)""", (ed[temp], boca, boca)).fetchall()
        usados = set()
        saida.append(f"\n== {temp}  ({len(hj)} jogos no historiadeboca, {len(db)} no banco)  {url}")
        for data, rodada, partido, a, ga, b, gb, estadio, cond in hj:
            if a is None:
                saida.append(f"   ? não li: {partido}"); resumo[temp]["nao_lido"] += 1; continue
            boca_casa = chave(a).startswith("boca")
            rival = b if boca_casa else a
            gb_, gr_ = (ga, gb) if boca_casa else (gb, ga)
            rk = chave(rival); rk = APELIDO.get(rk, rk)
            if temp in ("1924 Asociación", "1925 Asociación") and rk == "platense":
                rk = "universal"   # o Platense da Asociación (1922-1925) é o Universal no banco
            try:
                d = dt.date(int(data[6:10]), int(data[3:5]), int(data[0:2]))
            except ValueError:
                d = None
            cands = []
            for row in db:
                pid, dd, m, v, gm, gv, esp, fid, fase = row
                if pid in usados:
                    continue
                outro = v if m == boca else m
                if chave(nome[outro]).startswith(rk) or rk.startswith(chave(nome[outro])[:6]):
                    dist = 9999
                    if d and dd:
                        try:
                            x = dt.date.fromisoformat(dd)
                            dist = min(abs((x.replace(year=d.year) - d).days), abs((x - d).days))
                        except ValueError:
                            dist = 5000
                    cands.append((dist, row))
            if not cands:
                saida.append(f"   SEM PAR  {data} {partido}  (rodada {rodada})"); resumo[temp]["sem_par"] += 1; continue
            cands.sort(key=lambda x: x[0])
            dist, (pid, dd, m, v, gm, gv, esp, fid, fase) = cands[0]
            usados.add(pid)
            if m == boca:
                pb, pr = gm, gv
            else:
                pb, pr = gv, gm
            ok_placar = (pb, pr) == (gb_, gr_) or esp in ("wo", "awd") and pb is None
            iso = d.isoformat() if d else ""
            if dd == iso:
                sd = "igual"
            elif dd and iso and dd[5:] == iso[5:]:
                sd = f"ano {int(dd[:4]) - d.year:+d}"
            elif dd and iso:
                try:
                    delta = (dt.date.fromisoformat(dd) - d).days
                    sd = f"dif {delta:+d} dias"
                    if abs(delta) > 300:
                        x = dt.date.fromisoformat(dd)
                        sd = f"ano {x.year - d.year:+d} e dif {(x.replace(year=d.year) - d).days:+d} dias"
                except ValueError:
                    sd = f"inválida {dd}"
            else:
                sd = "sem data"
            resumo[temp]["jogos"] += 1
            resumo[temp]["placar_ok" if ok_placar else "placar_dif"] += 1
            resumo[temp]["data_" + ("igual" if sd == "igual" else "ano" if sd.startswith("ano") else "outra")] += 1
            jb = f"{nome[m]} {gm}-{gv} {nome[v]}" + (f" [{esp}]" if esp else "") + f" ({fase})"
            tsv.append(f"{temp}\t{iso}\t{partido}\t{dd}\t{jb}\t{'ok' if ok_placar else 'DIF'}\t{sd}\t{fid}")
            if not ok_placar or sd != "igual":
                saida.append(f"   {iso} {partido:40s} | banco {dd} {jb} | placar {'ok' if ok_placar else 'DIF'} | data {sd} | {fid}")
        sobra = [r for r in db if r[0] not in usados]
        for r in sobra:
            saida.append(f"   SÓ NO BANCO: {r[1]} {nome[r[2]]} {r[4]}-{r[5]} {nome[r[3]]} [{r[6]}] ({r[8]}) {r[7]}")
        resumo[temp]["so_banco"] += len(sobra)
    cab = ["Resumo por edição (jogos do Boca casados; placar ok/dif; data igual/só o ano/outra; sem par; só no banco):"]
    for temp, k in resumo.items():
        cab.append(f"{temp:20s} jogos {k['jogos']:3d} | placar ok {k['placar_ok']:3d} dif {k['placar_dif']:2d} | data igual {k['data_igual']:3d} "
                   f"ano {k['data_ano']:3d} outra {k['data_outra']:3d} | sem par {k['sem_par']:2d} | só banco {k['so_banco']:2d}")
    tot = Counter()
    for k in resumo.values():
        tot.update(k)
    cab.append(f"TOTAL jogos {tot['jogos']} | placar ok {tot['placar_ok']} dif {tot['placar_dif']} | data igual {tot['data_igual']} ano {tot['data_ano']} outra {tot['data_outra']} | sem par {tot['sem_par']} | só banco {tot['so_banco']}")
    out = RAIZ / "revisao" / "QU" / "cmp_hdb_saida.txt"
    out.write_text("\n".join(cab + saida) + "\n", encoding="utf-8")
    (RAIZ / "revisao" / "QU" / "cmp_hdb_jogos.tsv").write_text("\n".join(tsv) + "\n", encoding="utf-8")
    print("\n".join(cab))


if __name__ == "__main__":
    main()
