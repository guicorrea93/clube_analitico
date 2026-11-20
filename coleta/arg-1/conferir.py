"""Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF.

Uso: python coleta/arg-1/conferir.py [temporada ...]   (sem temporada: todas; mostra só as edições com problema)
     python coleta/arg-1/conferir.py -v 1950             (detalha a edição)
"""
from __future__ import annotations

import sys
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
sys.path.insert(0, str(AQUI))
from clubes_arg import clube  # noqa: E402
from edicoes import EDICOES, Edicao  # noqa: E402
from edicoes import PASTA_DADOS  # noqa: E402
from explicacoes import CORRIGE  # noqa: E402
from ler_rsssf import ler  # noqa: E402
from ler_rsssf import linhas as linhas_pag  # noqa: E402
import re  # noqa: E402
import rsssf_sul  # noqa: E402

CONTA = ("j", "v", "e", "d", "gp", "gc")


def soma(jogos: list, clubes: set[str]) -> dict[str, list[int]]:
    """Campanha de cada clube (J V E D GP GC) nos jogos entre clubes do conjunto."""
    t: dict[str, list[int]] = defaultdict(lambda: [0] * 6)
    for j in jogos:
        if j["m"] not in clubes or j["v"] not in clubes or j["esp"] in ("anulado", "n/p", "abd"):
            continue
        gm, gv = j["gm"], j["gv"]
        if j["esp"] in ("wo_m", "wo_v"):   # W.O. ou pontos dados pelo tribunal: a tabela conta os gols do campo (sem placar, nenhum)
            res = 1 if j["esp"] == "wo_m" else -1
            if gm is None:
                gm = gv = 0
        elif gm is None:
            continue
        else:
            res = (gm > gv) - (gm < gv)
        for a, b, ga, gb, r in ((j["m"], j["v"], gm, gv, res), (j["v"], j["m"], gv, gm, -res)):
            x = t[a]
            x[0] += 1
            x[1 + (0 if r > 0 else 1 if r == 0 else 2)] += 1
            x[4] += ga
            x[5] += gb
    return t


def _hist() -> list[tuple[str, rsssf_sul.Tabela, str]]:
    """Tabelas finais das páginas por década (arghist-*.html): [(página, tabela, título)]."""
    saida = []
    for f in sorted((PASTA_DADOS / "rsssf").glob("arghist-*.html")):
        ls = rsssf_sul.texto(f)
        _, ts = rsssf_sul.ler(ls, 1900)
        for t in ts:
            h = [l.strip() for l in ls[max(0, t.linha - 8):t.linha] if l.strip()]
            saida.append((f.stem, t, " / ".join(h[-4:])))
    return saida


_HIST: list | None = None


def preparar(e: Edicao) -> dict:
    global _HIST
    js, ts = ler(e)
    sem_nome: set[str] = set()
    jogos = []
    nome = lambda n, cid=None: e.nomes.get(n) or clube(n, e.ano_inicio, cid)
    for j in js:
        m, v = nome(j.mandante), nome(j.visitante)
        if not m:
            sem_nome.add(j.mandante)
        if not v:
            sem_nome.add(j.visitante)
        of = j.gm_of is not None
        jogos.append({"m": m, "v": v, "gm": j.gm_of if of else j.gm, "gv": j.gv_of if of else j.gv, "fase": j.fase, "grupo": j.grupo,
                      "esp": j.especial, "j": j})
    # correções escritas à mão (explicacoes.CORRIGE, com o motivo)
    log = []
    for jg in jogos:
        c = CORRIGE.get((e.temporada, jg["j"].texto))
        if c:
            jg.update({k: v for k, v in c.items() if k != "motivo"})
            log.append(f"corrigido — {jg['m']} x {jg['v']} ({jg['j'].data}): {c['motivo']}")
    jogos = [jg for jg in jogos if not jg.get("descartar")]
    # linha de nota que repete um jogo já listado ("Vélez Sarsfield 1-0 Boca Juniors." no resumo das decisões): sai
    pares = Counter((jg["m"], jg["v"]) for jg in jogos)
    for jg in [jg for jg in jogos if pares[(jg["m"], jg["v"])] > 1]:
        texto = linhas_pag(jg["j"].texto.split(":")[0])[int(jg["j"].texto.split(":")[1])].rstrip()
        if texto.endswith(".") and not re.search(r"\]\s*\.$", texto):
            jogos.remove(jg)
            pares[(jg["m"], jg["v"])] -= 1
            log.append(f"linha de nota que repete o jogo {jg['m']} x {jg['v']} ({jg['j'].texto}): fica de fora")
    tabelas = []
    for t in ts:
        linhas = []
        for r in t.linhas:
            c = nome(r["nome"], r.get("cidade"))
            if not c:
                sem_nome.add(r["nome"])
            linhas.append({**r, "clube": c})
        # tabela de critério de desempate (só os jogos entre os empatados e os primeiros): não é classificação
        acima = " ".join(linhas_pag(e.trechos[0][0])[max(0, t.linha - 7):t.linha])
        desempate = bool(re.search(r"won more points|points won|Article \d|against the team|top (three|five|two)|first (three|five) teams|"
                                   r"teams with (they )?tied|goal average in the accum", acima, re.I))
        tabelas.append({"t": t, "linhas": linhas, "fonte": e.trechos[0][0], "desempate": desempate})
    # zonas sem marca nos jogos (a página lista as rodadas juntas): o grupo sai da tabela de cada zona
    zonas: dict[str, set] = {}
    for tb in tabelas:
        if tb["t"].grupo and tb["t"].grupo != "Interzonal" and len(tb["linhas"]) >= 3:
            zonas.setdefault(tb["t"].grupo, set()).update(r["clube"] for r in tb["linhas"] if r["clube"])
    if len(zonas) >= 2 and not any(set(a) & set(b) for k1, a in zonas.items() for k2, b in zonas.items() if k1 < k2):
        for jg in jogos:
            if jg["grupo"] == "" and jg["fase"] == "":
                gm_ = next((g for g, cs in zonas.items() if jg["m"] in cs), None)
                gv_ = next((g for g, cs in zonas.items() if jg["v"] in cs), None)
                if gm_ and gv_:
                    jg["grupo"] = gm_ if gm_ == gv_ else "Interzonal"
    # tabelas finais do índice por década que pertencem a esta edição (os clubes e os jogos batem)
    if _HIST is None:
        _HIST = _hist()
    clubes_ed = {x for j in jogos for x in (j["m"], j["v"]) if x}
    anos = {str(e.ano_inicio), f"{e.ano_inicio}/{e.ano_fim}", f"{e.ano_inicio}/{str(e.ano_fim)[2:]}"}
    for pag, t, titulo in _HIST:
        if not any(a in titulo for a in anos) or len(t.linhas) < 2:
            continue
        linhas = [{**r, "clube": clube(r["nome"], e.ano_inicio, r.get("cidade"))} for r in t.linhas]
        if not all(r["clube"] in clubes_ed for r in linhas):
            continue
        tb = {"t": t, "linhas": linhas, "fonte": pag, "titulo": titulo}
        dif, _ = _melhor(tb, jogos)
        if len(dif) <= len(linhas) // 2:
            tabelas.append(tb)
    p = {"jogos": jogos, "tabelas": tabelas, "sem_nome": sem_nome, "log": log}
    if e.soma_de:   # edição sem jogos próprios (tabela anual): confere com os jogos das fases de grupos das edições somadas
        from edicoes import EDICOES
        p["jogos_conf"] = [j for x in EDICOES if x.temporada in e.soma_de for j in preparar(x)["jogos"] if j["fase"] == ""]
        p["jogos"] = []
    return p


def _melhor(tb: dict, jogos: list) -> tuple[list, str]:
    """Diferenças da tabela contra a variante de soma que mais se aproxima dela:
    jogos da fase da tabela entre os clubes dela; só os jogos do grupo; grupo + interzonais; todos os jogos entre eles."""
    t = tb["t"]
    clubes = {r["clube"] for r in tb["linhas"] if r["clube"]}
    fases = {j["fase"] for j in jogos}
    variantes = []
    for f in ([t.fase] if t.fase in fases else []) + sorted(fases - {t.fase}):
        variantes.append((f"fase {f or 'principal'}", [j for j in jogos if j["fase"] == f], True))
    if t.grupo:
        variantes.append(("grupo", [j for j in jogos if j["fase"] == t.fase and j["grupo"] == t.grupo], False))
        variantes.append(("grupo + interzonais", [j for j in jogos if j["fase"] == t.fase and j["grupo"] in (t.grupo, "Interzonal")], False))
    variantes.append(("todos os jogos", jogos, True))
    variantes.append(("campanha completa", jogos, False))
    melhor = None
    for nome, js, restringe in variantes:
        calc = soma(js, clubes if restringe else {x for j in js for x in (j["m"], j["v"])})
        dif = []
        for r in tb["linhas"]:
            pub = [r[k] for k in CONTA]
            c = calc.get(r["clube"], [0] * 6)
            if pub != c:
                dif.append((r["clube"] or r["nome"], pub, c))
        if melhor is None or len(dif) < len(melhor[0]):
            melhor = (dif, nome)
    return melhor


def conferir_tabelas(p: dict) -> list[tuple]:
    """[(fonte:linha, clube, publicado, calculado)] das linhas que não batem; tabela repetida conta uma vez."""
    difs, vistas = [], set()
    # jogos por clube na edição: tabela com mais jogos que isso é acumulada (Apertura + Clausura, promédio) e fica de fora
    por_clube: dict[str, int] = defaultdict(int)
    for j in p.get("jogos_conf") or p["jogos"]:
        if j["esp"] not in ("anulado", "n/p"):
            for x in (j["m"], j["v"]):
                por_clube[x] += 1
    teto = max(por_clube.values(), default=0)
    for tb in p["tabelas"]:
        if sum(1 for r in tb["linhas"] if r["j"] > teto) > len(tb["linhas"]) // 2:
            tb["acumulada"] = True
            continue
        if tb.get("desempate"):
            continue
        # liga de turno único: tabela com no máximo 60% dos jogos é parcial (meio do campeonato, minitabela de desempate)
        so_liga = {j["fase"] for j in p["jogos"]} <= {"", "Desempate do título", "Desempate do 2º lugar", "Desempate do rebaixamento"}
        if so_liga and teto >= 10 and all(r["j"] <= 0.6 * teto for r in tb["linhas"]) and                 not any(j["fase"] for j in p["jogos"] if {j["m"], j["v"]} <= {r["clube"] for r in tb["linhas"]}):
            tb["parcial"] = True
            continue
        chave_t = tuple((r["clube"], r["j"], r["pts"]) for r in tb["linhas"])
        if chave_t in vistas:
            continue
        vistas.add(chave_t)
        dif, variante = _melhor(tb, p.get("jogos_conf") or p["jogos"])
        tb["ok"] = not dif
        tb["variante"] = variante
        difs += [(f"{tb['fonte']}:{tb['t'].linha}", *d) for d in dif]
    return difs


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    args = [a for a in sys.argv[1:] if a != "-v"]
    detalhe = "-v" in sys.argv
    tot_ok = 0
    for e in EDICOES:
        if args and e.temporada not in args:
            continue
        p = preparar(e)
        difs = conferir_tabelas(p)
        n_tab = len({tuple((r["clube"], r["j"]) for r in tb["linhas"]) for tb in p["tabelas"]})
        if not difs and not p["sem_nome"] and n_tab:
            tot_ok += 1
            if not detalhe:
                continue
        print(f"{e.temporada:20s} jogos {len(p['jogos']):4d}  tabelas {n_tab}  linhas divergentes {len(difs)}  sem nome {len(p['sem_nome'])}")
        if p["sem_nome"]:
            print("    sem nome:", sorted(p["sem_nome"])[:12])
        for d in difs[: (40 if detalhe else 4)]:
            print("    ", d)
    print("edições sem problema:", tot_ok)
