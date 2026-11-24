"""Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF.

As tabelas das edições sem jogos (ou com jogos incompletos) não entram na soma: são a classificação.

Uso: python coleta/tun-1/conferir.py [temporada ...]   (sem temporada: todas; mostra só as edições com problema)
     python coleta/tun-1/conferir.py -v 1950             (detalha a edição)
"""
from __future__ import annotations

import sys
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-africa"))
sys.path.insert(0, str(AQUI))
from clubes_tun import clube  # noqa: E402
from edicoes import EDICOES, Edicao  # noqa: E402
from edicoes import PASTA_DADOS  # noqa: E402
from explicacoes import ANULA_CLUBE, CORRIGE, EXTRAS, TABELAS_FORA  # noqa: E402
from ler_rsssf import ler  # noqa: E402
from ler_rsssf import linhas as linhas_pag  # noqa: E402
import re  # noqa: E402
import rsssf_africa  # noqa: E402

CONTA = ("j", "v", "e", "d", "gp", "gc")


def eh_mata(f: str) -> bool:
    """Fase de mata-mata ou desempate (fora das somas de liga)."""
    return f.startswith(("Final", "Semifinal", "Desempate", "Oitavas", "Quartas", "Repechaje"))


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


def preparar(e: Edicao) -> dict:
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
            jg.update({k: v for k, v in c.items() if k not in ("motivo", "data", "nota", "oficial")})
            if "oficial" in c:   # resultado dado fora de campo: placar oficial, o de campo fica na observação
                jg["j"].gm_of, jg["j"].gv_of = c["oficial"]
                jg["j"].especial = jg["esp"] = "awd"
                jg["gm"], jg["gv"] = c["oficial"]
            if "data" in c:
                jg["j"].data = c["data"]
            if "nota" in c:
                jg["j"].nota = c["nota"]
            log.append(f"corrigido — {jg['m']} x {jg['v']} ({jg['j'].data}): {c['motivo']}")
    jogos = [jg for jg in jogos if not jg.get("descartar")]
    if e.temporada in ANULA_CLUBE:   # clube que desistiu: jogos anulados
        quem, motivo = ANULA_CLUBE[e.temporada]
        for jg in jogos:
            if quem in (jg["m"], jg["v"]):
                jg["esp"] = "anulado"
                jg["j"].nota = (jg["j"].nota + "; " + motivo).strip("; ")
        log.append(f"jogos do {quem} anulados: {motivo}")
    # jogos acrescentados à mão (explicacoes.EXTRAS, com a fonte e o motivo)
    for x in EXTRAS.get(e.temporada, []):
        jogos.append({"m": nome(x["mandante"]) or x["mandante"], "v": nome(x["visitante"]) or x["visitante"], "gm": x["gm"],
                      "gv": x["gv"], "fase": x.get("fase", ""),
                      "grupo": "", "esp": x.get("esp", ""), "extra": x, "j": None})
    # linha de nota que repete um jogo já listado ("Vélez Sarsfield 1-0 Boca Juniors." no resumo das decisões): sai
    pares = Counter((jg["m"], jg["v"]) for jg in jogos)
    for jg in [jg for jg in jogos if pares[(jg["m"], jg["v"])] > 1 and jg["j"] and not jg["j"].texto.startswith(("wiki", "ogol", "espn"))]:
        texto = linhas_pag(jg["j"].texto.split(":")[0])[int(jg["j"].texto.split(":")[1])].rstrip()
        # (abreviação com ponto no fim, "Rampla Jrs.", "Huracan B.", é jogo de verdade)
        if texto.endswith(".") and not re.search(r"\]\s*\.$", texto) and re.search(r"[A-Za-zÀ-ÿ]{5}\.$", texto):
            jogos.remove(jg)
            pares[(jg["m"], jg["v"])] -= 1
            log.append(f"linha de nota que repete o jogo {jg['m']} x {jg['v']} ({jg['j'].texto}): fica de fora")
    tabelas = []
    pag0 = (e.trechos or e.tabelas or [("", 0, 0)])[0][0]   # página das tabelas lidas
    for t in ts:
        if (motivo := TABELAS_FORA.get((e.temporada, f"{pag0}:{t.linha}"))):
            log.append(f"tabela {pag0}:{t.linha} fora da conferência: {motivo}")
            continue
        linhas = []
        for r in t.linhas:
            c = nome(r["nome"], r.get("cidade"))
            if not c:
                sem_nome.add(r["nome"])
            linhas.append({**r, "clube": c})
        # tabela de critério de desempate (só os jogos entre os empatados e os primeiros): não é classificação
        acima = " ".join(linhas_pag(pag0)[max(0, t.linha - 7):t.linha]) if pag0 else ""
        desempate = bool(re.search(r"won more points|points won|Article \d|against the team|top (three|five|two)|first (three|five) teams|"
                                   r"teams with (they )?tied|goal average in the accum", acima, re.I))
        # tabela da metade do campeonato ("Halfway Table"): parcial, fora da conferência
        # (o título mais próximo acima da tabela: "Halfway Tables:" vale para os dois grupos que vêm debaixo dele)
        parcial = False
        if pag0 and not t.secao.startswith("@"):
            ls_ = linhas_pag(pag0)
            for k in range(t.linha - 1, max(-1, t.linha - 40), -1):
                if re.search(r"Halfway|Half-way|Table after|First half", ls_[k], re.I):
                    parcial = True
                    break
                if re.search(r"Final Tables?|^\s*Tables?:|Standings", ls_[k], re.I):
                    break
        tabelas.append({"t": t, "linhas": linhas, "fonte": t.secao[1:] if t.secao.startswith("@") else pag0,
                        "desempate": desempate, "parcial": parcial})
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
    # edição sem jogos ou com só parte deles: as tabelas da página são a classificação, sem conferência com a soma
    if e.sem_jogos or e.incompleta:
        for tb in tabelas:
            tb["sem_conferencia"] = True
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
        # campanha inteira na fase, com os jogos contra quem não está na tabela (excluído, outro grupo)
        variantes.append((f"campanha na fase {f or 'principal'}", [j for j in jogos if j["fase"] == f], False))
    if t.grupo:
        variantes.append(("grupo", [j for j in jogos if j["fase"] == t.fase and j["grupo"] == t.grupo], False))
        variantes.append(("grupo + interzonais", [j for j in jogos if j["fase"] == t.fase and j["grupo"] in (t.grupo, "Interzonal")], False))
    variantes.append(("jogos de liga (sem finais e desempates)", [j for j in jogos if not eh_mata(j["fase"])], True))
    variantes.append(("campanha nos jogos de liga", [j for j in jogos if not eh_mata(j["fase"])], False))
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
        if tb.get("sem_conferencia"):
            continue
        if sum(1 for r in tb["linhas"] if r["j"] > teto) > len(tb["linhas"]) // 2:
            tb["acumulada"] = True
            continue
        if tb.get("desempate") or tb.get("parcial"):
            continue
        # liga de turno único: tabela com no máximo 60% dos jogos é parcial (meio do campeonato, minitabela de desempate)
        so_liga = all(f == "" or eh_mata(f) for f in {j["fase"] for j in p["jogos"]})
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
        if not difs and not p["sem_nome"] and (n_tab or e.sem_jogos):
            tot_ok += 1
            if not detalhe:
                continue
        print(f"{e.temporada:20s} jogos {len(p['jogos']):4d}  tabelas {n_tab}  linhas divergentes {len(difs)}  sem nome {len(p['sem_nome'])}")
        if p["sem_nome"]:
            print("    sem nome:", sorted(p["sem_nome"])[:12])
        for d in difs[: (40 if detalhe else 4)]:
            print("    ", d)
    print("edições sem problema:", tot_ok)
