"""Bloco C: amostra de placares e datas por década contra fontes que a coleta NÃO usou como base daquele ano.
- 1948, 1949 e 1960: tabela de confrontos (Cross-Table) da RSSSF (colNN.html) — a base da coleta nesses anos é a Wikipédia es;
- 1974-1979: jogos das fases finais na página da RSSSF (base da coleta: Wikipédia es);
- 1995/96 em diante: páginas da Wikipédia es da temporada ou do torneio (base da coleta: RSSSF), lidas com o leitor da
  própria coleta (coleta/col-1/wikipedia_jogos.py, só importado, apontado para o cache da revisão).
Casamento: temporada + mandante + visitante (+ placar mais próximo); identidade dos jogos nunca pelo partida_id.
Uso (da raiz): python -I revisao/CO/amostra_wiki.py"""
import csv, html, re, sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path("coleta/col-1").resolve()))
sys.path.insert(0, str(Path("coleta/comum-sulamerica").resolve()))
sys.path.insert(0, str(Path("revisao/CO").resolve()))
import baixar  # noqa: E402
import wikipedia_jogos  # noqa: E402
from clubes_col import clube  # noqa: E402

P = "data/coleta/col-1/pacote/"
pac = defaultdict(list)
for p in csv.DictReader(open(P + "partidas.csv", encoding="utf-8")):
    pac[p["temporada"]].append(p)


def compara(temp, fonte_jogos, rotulo, ano):
    """fonte_jogos: lista de (mandante_fonte, visitante_fonte, gm, gv, data|None)."""
    usados = set()
    ok = dif = sem = 0
    difs = []
    for m, v, gm, gv, d in fonte_jogos:
        cm, cv = clube(m, ano), clube(v, ano)
        if not cm or not cv:
            sem += 1
            continue
        cand = [k for k, p in enumerate(pac[temp]) if k not in usados and p["mandante"] == cm and p["visitante"] == cv]
        if not cand:
            difs.append(f"  falta no pacote: {cm} {gm}-{gv} {cv} ({d or 's/d'})")
            dif += 1
            continue
        k = min(cand, key=lambda k: (pac[temp][k]["gols_mandante"] != str(gm) or pac[temp][k]["gols_visitante"] != str(gv),
                                     pac[temp][k]["data"] != (d or pac[temp][k]["data"])))
        usados.add(k)
        p = pac[temp][k]
        erro = []
        if (p["gols_mandante"], p["gols_visitante"]) != (str(gm), str(gv)):
            erro.append(f"placar pacote {p['gols_mandante']}-{p['gols_visitante']} x fonte {gm}-{gv}")
        if d and p["data"] and p["data"] != d:
            erro.append(f"data pacote {p['data']} x fonte {d}")
        if erro:
            dif += 1
            difs.append(f"  {p['fase']}: {cm} x {cv}: " + "; ".join(erro))
        else:
            ok += 1
    print(f"{temp} [{rotulo}]: {ok + dif} jogos da fonte casados ou procurados; batem {ok}; diferem {dif}; nomes não reconhecidos {sem}")
    for l in difs[:25]:
        print(l)
    if len(difs) > 25:
        print(f"  ... mais {len(difs) - 25}")
    return ok, dif


def cross(ano):
    t = html.unescape(re.sub(r"<[^>]+>", "", open(f"data/coleta/col-1/rsssf/col{str(ano)[2:]}.html", encoding="latin-1").read()))
    ls = t.splitlines()
    i = next(k for k, l in enumerate(ls) if "Cross" in l)
    nomes, jogos, ult = [], [], None
    for l in ls[i + 1:]:
        if re.match(r"^\s*(Topscorers|NB)", l):
            break
        m = re.match(r"^(.*?)\s{1,}((?:(?:\d{1,2}-\d{1,2}|===)\s*){4,})$", l.rstrip())
        if not m:
            continue
        nome = re.sub(r"\s*\([A-Z]{3}\)", "", m.group(1)).strip()
        cel = re.findall(r"\d{1,2}-\d{1,2}|===", m.group(2))
        if nome.startswith("_") or not nome:
            nome = ult
        else:
            nomes.append(nome)
            ult = nome
        jogos.append((nome, cel))
    saida = []
    for nome, cel in jogos:
        for k, c in enumerate(cel):
            if c != "===":
                a, b = c.split("-")
                saida.append((nome, nomes[k], int(a), int(b), None))
    return saida


tot_ok = tot_dif = 0
for ano in (1948, 1949, 1960):
    o, d = compara(str(ano), cross(ano), f"RSSSF col{str(ano)[2:]} Cross-Table", ano)
    tot_ok += o; tot_dif += d

# fases finais 1974-1979 na RSSSF: linhas "Clube A  x-y  Clube B"
for ano in range(1974, 1980):
    t = html.unescape(re.sub(r"<[^>]+>", "", open(f"data/coleta/col-1/rsssf/col{str(ano)[2:]}.html", encoding="latin-1").read()))
    js = []
    for l in t.splitlines():
        m = re.match(r"^\s*([A-Z][A-Za-zÀ-ÿ.\' ]+?)\s{1,}(\d{1,2})-(\d{1,2})\s{1,}([A-Z][A-Za-zÀ-ÿ.\' ]+?)\s*(?:\[.*)?$", l)
        if m:
            js.append((m.group(1).strip(), m.group(4).strip(), int(m.group(2)), int(m.group(3)), None))
    o, d = compara(str(ano), js, f"RSSSF col{str(ano)[2:]} jogos das fases finais", ano)
    tot_ok += o; tot_dif += d

# 1995/96 em diante: Wikipédia es (página da temporada ou do torneio)
PAGS = {"1998": "Campeonato colombiano 1998", "2001": "Campeonato colombiano 2001",
        "2005 Apertura": "Torneo Apertura 2005 (Colombia)", "2009 Finalización": "Torneo Finalización 2009 (Colombia)",
        "2016 Apertura": "Torneo Apertura 2016 (Colombia)", "2022 Finalización": "Torneo Finalización 2022 (Colombia)"}
wikipedia_jogos.PASTA = Path("data/cache/revisao/CO")
for temp, tit in PAGS.items():
    chave = temp
    baixar.wiki("es", tit, f"es_{chave.replace(' ', '_')}.txt")
    try:
        js = wikipedia_jogos.jogos(chave)
    except Exception as ex:  # página com formato que o leitor não conhece
        print(f"{temp}: leitor da Wikipédia falhou ({ex})")
        continue
    lista = [(j.mandante, j.visitante, j.gm, j.gv, j.data) for j in js if j.gm is not None]
    o, d = compara(temp, lista, f"Wikipédia es: {tit}", int(temp[:4]))
    tot_ok += o; tot_dif += d
print(f"\nTOTAL: batem {tot_ok}; diferem {tot_dif}")
