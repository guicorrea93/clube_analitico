"""Junta as fontes da 1ª divisão de Honduras e grava o pacote em data/coleta/hon-1/pacote/ e o relatório em docs/coleta/hon-1.md.

Fontes: RSSSF (lista de campeões hondchamp.html; tabelas finais de 1965/66 a 1994/95, hondhist.html; uma página por temporada
depois, hondAA.html e hondAAAA.html: jogos, autores dos gols e tabelas) e ESPN (liga hon.1: hora, estádio, público, gols com
minuto e cartões, casados com os jogos da RSSSF).

Uso: python coleta/hon-1/importar.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-concacaf"))
sys.path.insert(0, str(AQUI))
import autores  # noqa: E402
import outras_fontes  # noqa: E402
from clubes_hon import CLUBES, clube  # noqa: E402
from conferir import conferir_tabelas, eh_mata, preparar, soma  # noqa: E402
from edicoes import EDICOES, PACOTE, RELATORIO, SLUG, Edicao  # noqa: E402
from explicacoes import CORRIGE, EXPLICACOES, EXTRAS  # noqa: E402
from ler_rsssf import campeoes  # noqa: E402
from rsssf_concacaf import chave  # noqa: E402

# ordem das fases (quanto maior, mais longe o clube chegou); os torneios do ano (Apertura, Intermedio, Clausura) e as finais
# de cada um ficam no nível 0: decidem vaga nas finais do campeonato, não o título
NIVEL_FASE = {"": 0, "Apertura": 0, "Clausura": 0, "Grupo do rebaixamento": 0, "Segunda fase": 1, "Fase final": 3,
              "Quartas de final": 3, "Semifinal": 4, "Final": 6, "Desempate do título": 6, "Final dos grupos": 4, "Repescagem": 1,
              "Finalíssima": 7, "Triangulares": 4}
WIKI: dict[str, str] = {}
VICES: dict[str, str] = {}
TOPS: dict[str, list] = {}
TOPS_FONTE: dict[str, str] = {}


def nome_fase(f: str, fases: set[str]) -> str:
    if f:
        return f
    return "Primeira fase" if fases - {""} else "Fase única"


def id_edicao(e: Edicao) -> str:
    return re.sub(r"[^0-9a-z]+", "-", chave(e.temporada))


def especial(esp: str) -> str:
    return {"wo_m": "wo", "wo_v": "wo", "awd": "awd", "abd": "abd", "anulado": "n/p", "n/p": "n/p"}.get(esp, "")


def montar(e: Edicao, cps: dict[str, str]) -> dict:
    p = preparar(e)
    log: list[str] = list(p["log"])
    for x in EXTRAS.get(e.temporada, []):
        p["jogos"].append({"m": x["mandante"], "v": x["visitante"], "gm": x["gm"], "gv": x["gv"], "fase": x.get("fase", ""),
                           "grupo": "", "esp": x.get("esp", ""), "extra": x, "j": None})
    for j in [j for j in p["jogos"] if not j["m"] or not j["v"]]:
        log.append(f"linha lida como jogo e descartada (clube não reconhecido): {j['j'].texto} «{j['j'].mandante} x {j['j'].visitante}»")
        p["jogos"].remove(j)
    difs = conferir_tabelas(p)
    jogos = p["jogos"]
    fases = {j["fase"] for j in jogos}
    # campanha de cada clube (resultado oficial; W.O. vale vitória) e fase mais longe
    clubes = sorted({x for j in jogos for x in (j["m"], j["v"]) if x})
    if e.sem_jogos or e.incompleta:   # sem jogos (ou com parte deles): os clubes são também os da tabela final
        clubes = sorted(set(clubes) | {r["clube"] for tb in p["tabelas"] for r in tb["linhas"] if r["clube"]})
    calc = soma(jogos, set(clubes))
    nivel: dict[str, int] = defaultdict(int)
    for j in jogos:
        for x in (j["m"], j["v"]):
            nivel[x] = max(nivel[x], NIVEL_FASE.get(j["fase"], 0))
    # campeão pela lista da RSSSF (hondchamp.html)
    camp_txt = "" if e.sem_campeao else (e.campeao_rsssf or cps.get(e.temporada, "") or WIKI.get(e.temporada, ""))
    campeao = clube(camp_txt, e.ano_inicio) if camp_txt else None
    if not campeao and camp_txt:
        log.append(f"campeão da lista da RSSSF não reconhecido: {camp_txt}")
    final = classificacao(e, p, calc, nivel, campeao, clubes)
    return {"e": e, "p": p, "difs": difs, "log": log, "clubes": clubes, "campeao": campeao, "camp_txt": camp_txt,
            "final": final, "fases": fases}


def classificacao(e: Edicao, p: dict, calc: dict, nivel: dict, campeao: str | None, clubes: list[str]) -> list[dict]:
    """Classificação final: a tabela publicada que traz todos os clubes e fecha com os jogos (ordem oficial, pontos com
    punições); sem ela, calculada (fase alcançada, pontos, saldo, gols pró). O campeão da lista oficial fica em 1º."""
    pv = e.pontos_vitoria
    pontos = lambda v, e_, d: pv * v + e_
    # entre as tabelas que fecham com os jogos e trazem todos os clubes, a de mais jogos (a acumulada do ano, quando há)
    ts = [tb for tb in p["tabelas"] if not tb.get("acumulada") and tb.get("ok")]
    # tabela cortada em duas pela linha de rebaixamento ("- - - -"): as duas partes seguidas da mesma página viram uma
    ts += [{**a, "linhas": a["linhas"] + b["linhas"]} for a, b in zip(ts, ts[1:])
           if a["fonte"] == b["fonte"] and not {r["clube"] for r in a["linhas"]} & {r["clube"] for r in b["linhas"]} and
           b["linhas"][0]["pos"] == len(a["linhas"]) + 1]
    cands = [tb for tb in ts if {r["clube"] for r in tb["linhas"]} == set(clubes)]
    pub = max(cands, key=lambda tb: sum(r["j"] or 0 for r in tb["linhas"]), default=None)
    if e.sem_jogos or e.incompleta:   # sem jogos: as tabelas publicadas são a classificação
        ts = [tb for tb in p["tabelas"] if tb.get("sem_conferencia")]
        pub = None
    if pub is None and not {r["clube"] for tb in ts for r in tb["linhas"]} >= set(clubes):
        # as tabelas que fecham com os jogos não cobrem todos os clubes (uma conferência diverge, como em 2004): entram todas
        # as tabelas publicadas da fase regular
        ts = [tb for tb in p["tabelas"] if not (tb.get("acumulada") or tb.get("parcial") or tb.get("desempate"))]
    if pub is None and ts:
        # conferências / divisões: junta as tabelas de clubes diferentes, a maior primeiro (no ano com dois turnos, fica o
        # turno de mais jogos), e ordena por pontos, saldo e gols pró
        juntas, vistos = [], set()
        for tb in sorted(ts, key=lambda tb: -sum(r["j"] or 0 for r in tb["linhas"])):
            cs = {r["clube"] for r in tb["linhas"]}
            if not cs & vistos and tb["t"].fase == "":
                juntas.append(tb)
                vistos |= cs
        ls_ = [r for tb in juntas for r in tb["linhas"]]
        ls_.sort(key=lambda r: (-(r["pts"] or 0), -((r["gp"] or 0) - (r["gc"] or 0)), -(r["gp"] or 0)))
        if juntas:
            pub = {**juntas[0], "linhas": ls_, "fonte": " + ".join(dict.fromkeys(tb["fonte"] for tb in juntas))}
    linhas = []
    if pub:
        parcial = any(r["v"] is None for r in pub["linhas"])
        for k, r in enumerate(pub["linhas"], 1):
            ajuste = (None if None in (r["v"], r["e"], r["d"], r["pts"]) or e.pontos_fora
                      else r["pts"] - pontos(r["v"], r["e"], r["d"]))
            linhas.append({"clube": r["clube"], "j": r["j"], "v": r["v"], "e": r["e"], "d": r["d"], "gp": r["gp"], "gc": r["gc"],
                           "pts": r["pts"], "ajuste": ajuste, "obs": r.get("obs", ""),
                           "fonte": f"RSSSF ({pub['fonte']}{', tabela parcial' if parcial else ''})"})
        # a ordem publicada vale; empates sem número herdam a posição de cima
    elif e.sem_jogos or e.incompleta:   # sem tabela: só o campeão e o vice (anos sem página e era amadora)
        vice = VICES.get(e.temporada, "")
        for nome in [campeao or ""] + re.split(r"\s+and\s+|,\s*", vice):
            c = nome if nome == campeao else clube(nome.strip(), e.ano_inicio)
            if c and all(r["clube"] != c for r in linhas):
                linhas.append({"clube": c, "j": None, "v": None, "e": None, "d": None, "gp": None, "gc": None, "pts": None,
                               "ajuste": None, "obs": "", "fonte": "lista de campeões da Wikipédia em inglês (campeão e vice)"})
    else:
        for c in clubes:
            x = calc.get(c, [0] * 6)
            linhas.append({"clube": c, "j": x[0], "v": x[1], "e": x[2], "d": x[3], "gp": x[4], "gc": x[5], "pts": pontos(x[1], x[2], x[3]),
                           "ajuste": 0, "obs": "", "fonte": "calculada (fase alcançada, pontos, saldo, gols pró)"})
        linhas.sort(key=lambda r: (-nivel[r["clube"]], -r["pts"], -(r["gp"] - r["gc"]), -r["gp"], r["clube"]))
    # (nos anos sem jogos a classificação é a tabela do ano; campeão e vice da lista podem não estar nela: entram no topo,
    # sem a campanha, com a fonte da lista)
    sem_campanha = lambda c: {"clube": c, "j": None, "v": None, "e": None, "d": None, "gp": None, "gc": None, "pts": None,
                              "ajuste": None, "obs": "", "fonte": "lista de campeões (RSSSF e Wikipédia)"}
    if campeao and linhas and not any(r["clube"] == campeao for r in linhas) and (e.sem_jogos or e.incompleta):
        linhas.insert(0, sem_campanha(campeao))
    if campeao and linhas and linhas[0]["clube"] != campeao and any(r["clube"] == campeao for r in linhas):
        c = next(r for r in linhas if r["clube"] == campeao)
        linhas.remove(c)
        linhas.insert(0, c)
    # vice da lista (da RSSSF; da Wikipédia onde ela não tem) logo abaixo do campeão
    vice = clube(VICES.get(e.temporada, ""), e.ano_inicio) if VICES.get(e.temporada) and campeao else None
    if vice and vice != campeao and linhas and not any(r["clube"] == vice for r in linhas) and (e.sem_jogos or e.incompleta):
        linhas.insert(1, sem_campanha(vice))
    if vice and vice != campeao and len(linhas) > 2 and linhas[1]["clube"] != vice and any(r["clube"] == vice for r in linhas):
        v = next(r for r in linhas if r["clube"] == vice)
        linhas.remove(v)
        linhas.insert(1, v)
    for k, r in enumerate(linhas, 1):
        r["pos"] = k
    return linhas


def situacao(r: dict, campeao: str | None, k: int) -> str:
    if r["clube"] == campeao:
        return "campeao"
    if k == 2:
        return "vice"
    if re.search(r"relegat|descend|rebaix", r.get("obs", ""), re.I):
        return "rebaixado"
    return ""


def _csv(arquivo: str, cab: list[str], linhas: list[list]) -> None:
    PACOTE.mkdir(parents=True, exist_ok=True)
    with open(PACOTE / arquivo, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(cab)
        for l in linhas:
            w.writerow(["" if x is None else x for x in l])


def gravar(eds: list[dict]) -> None:
    (PACOTE).mkdir(parents=True, exist_ok=True)
    (PACOTE / "competicao.json").write_text(json.dumps({
        "slug": SLUG, "nome": "Campeonato Hondurenho", "nome_curto": "Hondurenho", "tipo": "liga", "nivel": 1,
        "pais": "HON", "pais_nome": "Honduras", "regiao": None, "confederacao": "CONCACAF", "rotulo_painel": "Hondurenho",
        "menu_painel": "Honduras · 1ª divisão", "do_painel": "do Campeonato Hondurenho", "o_painel": "o Campeonato Hondurenho",
        "observacao": "Liga Nacional de Honduras de 1965/66 ao Clausura 2026, uma edição por título, como a lista de campeões da "
                      "RSSSF: um campeão por temporada até 1996/97 (1972/73 abandonada, sem campeão), Apertura e Clausura de "
                      "1997/98 em diante (1999, torneio único; Clausura 2020 sem campeão). Até 1995/96 só as tabelas. A Liga "
                      "Amateur de 1947-1964 fica fora (não é reconhecida pela liga)."},
        ensure_ascii=False, indent=1), encoding="utf-8")
    _csv("paises.csv", ["codigo", "nome", "confederacao"], [["HON", "Honduras", "CONCACAF"]])
    L = defaultdict(list)
    nomes_fonte: dict[str, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
    usados: set[str] = set()
    so_tabela: dict[str, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
    for d in eds:
        e, p = d["e"], d["p"]
        eid = id_edicao(e)
        fases = d["fases"]
        ordem_f = sorted(fases, key=lambda f: (NIVEL_FASE.get(f, 0),
                                               min((j["j"].linha for j in p["jogos"] if j["fase"] == f and j["j"]), default=0)))
        for k, f in enumerate(ordem_f, 1):
            js = [j for j in p["jogos"] if j["fase"] == f]
            grupos = sorted({j["grupo"] for j in js if j["grupo"] and j["grupo"] != "Interzonal"})
            mata = eh_mata(f) or (f == "Liguilla" and not grupos)
            pares = Counter(frozenset((j["m"], j["v"])) for j in js)
            serie = ("jogo_unico" if max(pares.values(), default=1) == 1 else "ida_volta") if mata else "pontos_corridos"
            tipo = "mata_mata" if mata else ("grupos" if len(grupos) >= 2 else "liga")
            L["fases"].append([e.temporada, k, nome_fase(f, fases), tipo, len(grupos) if tipo == "grupos" else None, serie, ""])
        n = 0
        gols_ed = autor_ed = 0
        og = outras_fontes.ogol(e, p["jogos"])
        es = outras_fontes.espn(e, p["jogos"])
        d["ogol"], d["espn"] = og, es
        idx = {id(j): k for k, j in enumerate(p["jogos"])}
        for k, g in og["ligado"].items():
            j = p["jogos"][k]
            for lado, nm in (("m", "mandante"), ("v", "visitante")):
                nomes_fonte[j[lado]][f"ogol:{g[nm]}"].append(e.ano_inicio)
            x = j["j"]
            if (g["gols_mandante"], g["gols_visitante"]) != (x.gm, x.gv) and x.gm is not None and g["gols_mandante"] is not None:
                d["log"].append(f"placar diferente no ogol — {j['m']} x {j['v']} ({x.data}): RSSSF {x.gm}-{x.gv}, ogol "
                                f"{g['gols_mandante']}-{g['gols_visitante']}; fica o da RSSSF")
            dd = outras_fontes._dia(g["data"])
            dr = outras_fontes._dia(x.data)
            if dr and dd and abs(dr - dd) > 3:
                d["log"].append(f"data diferente no ogol — {j['m']} x {j['v']}: RSSSF {x.data}, ogol {g['data']}; fica a da RSSSF")
        for k, g in es["ligado"].items():
            j = p["jogos"][k]
            for lado, nm in (("m", "mandante"), ("v", "visitante")):
                nomes_fonte[j[lado]][f"espn:{g[nm]}"].append(e.ano_inicio)
        for j in sorted(p["jogos"], key=lambda j: (ordem_f.index(j["fase"]), j["j"].linha if j["j"] else 10 ** 6)):
            n += 1
            pid = f"{eid}-{n:04d}"
            x = j["j"]
            ex = j.get("extra")
            usados |= {j["m"], j["v"]}
            if x:
                pref = "espn" if x.texto.startswith("espn:") else "wikipedia" if x.texto.startswith("wiki") else "rsssf"
                nomes_fonte[j["m"]][f"{pref}:{x.mandante}"].append(e.ano_inicio)
                nomes_fonte[j["v"]][f"{pref}:{x.visitante}"].append(e.ano_inicio)
            gm, gv = j["gm"], j["gv"]
            esp = especial(j["esp"])
            obs = []
            if j["esp"] in ("wo_m", "wo_v"):
                venc = j["m"] if j["esp"] == "wo_m" else j["v"]
                if gm is not None:   # jogo disputado, pontos dados pelo tribunal: o placar de campo vai para a observação
                    obs.append(f"pontos para o {venc} (decisão fora de campo); placar em campo {gm}-{gv}")
                    esp = "awd"
                else:
                    obs.append(f"W.O.: vitória do {venc} (a tabela conta a vitória sem gols)")
                gm = gv = None
            if x and x.gm_of is not None and (x.gm, x.gv) != (x.gm_of, x.gv_of):
                obs.append(f"placar em campo {x.gm}-{x.gv}" if x.gm is not None else "decidido fora de campo")
            if j["esp"] == "abd":
                obs.append(f"abandonado ou suspenso{f' com {x.gm}-{x.gv}' if x and x.gm is not None else ''}; não vale na tabela")
                gm = gv = None
            if j["esp"] == "anulado":
                obs.append(f"jogo anulado{f' ({x.gm}-{x.gv})' if x and x.gm is not None else ''}")
                gm = gv = None
            if j["esp"] == "n/p" and gm is not None:   # não disputado (2025: a ESPN traz um placar, a RSSSF diz que não houve)
                obs.append(f"não disputado; a ESPN registra {gm}-{gv}")
                gm = gv = None
            if x and x.nota:
                obs.append(x.nota)
            if j["grupo"] == "Interzonal":
                obs.append("jogo interzonal")
            texto_autores = x.gols_texto if x else ""
            publico = autores.publico(texto_autores) if texto_autores else None
            sep = None
            if x and gm is not None and esp == "" and autores.eh_autores(texto_autores):
                sep = autores.separar(texto_autores, gm, gv)
            if gm is not None:
                gols_ed += gm + gv
            if sep:
                for lado, gs in ((j["m"], sep[0]), (j["v"], sep[1])):
                    for g in gs:
                        L["gols"].append([pid, lado, g["jogador"], g["minuto"], g["acrescimo"], g["tipo"], "RSSSF"])
                        autor_ed += 1
            if ex:
                for lado, jog, mi, tp in ex.get("gols", []):
                    L["gols"].append([pid, lado, jog, mi, None, tp, "RSSSF"])
                    autor_ed += 1
                if ex.get("obs"):
                    obs.append(ex["obs"])
            local = x.local if x else None
            loc_clube = clube(local, e.ano_inicio) if local else None
            estadio = (ex or {}).get("estadio") or (f"Estádio do {loc_clube}" if loc_clube else local)
            cidade = (ex or {}).get("cidade")
            rodada, data, hora = (x.rodada if x else None), (x.data if x else ex.get("data")), None
            base = ("espn" if x.texto.startswith("espn:") else "wikipedia" if x.texto.startswith("wiki") else "rsssf") if x else "rsssf"
            fonte_id = ((x.texto if base == "espn" else f"wikipedia:{x.texto[5:]}" if base == "wikipedia" else f"rsssf:{x.texto}")
                        if x else ex["fonte_id"])
            k = idx[id(j)]
            go = og["ligado"].get(k)
            if go:
                fonte_id += f" ogol:{go['id']}"
                rodada = rodada or go.get("rodada")
                data = data or (go["data"] if go["data"][:4] != "0000" else None)
            ge = es["ligado"].get(k)
            if ge:
                fonte_id += f" espn:{ge['id']}"
                loc = outras_fontes._local(ge)
                hora = loc.strftime("%H:%M") if loc.strftime("%H:%M") != "21:00" or ge["data_hora"][11:16] != "00:00" else None
                data = data or loc.date().isoformat()
                estadio = ge.get("estadio") or estadio
                cidade = ge.get("cidade") or cidade
                publico = publico or (ge.get("publico") or None)
                gl, ct = outras_fontes.lances_espn(ge)
                if gm is not None and esp == "" and sum(1 for g in gl if g["lado"] == "home") == gm and                         sum(1 for g in gl if g["lado"] == "away") == gv and all(g["jogador"] for g in gl):
                    if sep:   # a ESPN traz o minuto: troca os gols da RSSSF pelos dela
                        L["gols"] = [r for r in L["gols"] if r[0] != pid]
                        autor_ed -= gm + gv
                    for g in gl:
                        L["gols"].append([pid, j["m"] if g["lado"] == "home" else j["v"], g["jogador"], g["minuto"], g["acrescimo"],
                                          g["tipo"], "ESPN"])
                        autor_ed += 1
                    sep = sep or True
                for c in ct:
                    if c["jogador"]:
                        L["cartoes"].append([pid, j["m"] if c["lado"] == "home" else j["v"], c["jogador"], c["minuto"], c["acrescimo"],
                                             c["cor"], "ESPN"])
            L["partidas"].append([pid, e.temporada, nome_fase(j["fase"], fases), j["grupo"] if j["grupo"] != "Interzonal" else "",
                                  rodada, data, hora, j["m"], j["v"], gm, gv,
                                  x.pen_m if x else None, x.pen_v if x else None, esp, estadio, cidade, publico,
                                  {"espn": "ESPN", "wikipedia": "Wikipédia (es)"}.get(base, "RSSSF"), fonte_id,
                                  "" if sep or not texto_autores or not autores.eh_autores(texto_autores) else texto_autores,
                                  "; ".join(o for o in obs if o)])
        # classificação final
        for r in d["final"]:
            L["classificacao_final"].append([e.temporada, r["pos"], r["clube"], r["j"], r["v"], r["e"], r["d"], r["gp"], r["gc"],
                                             r["pts"], r["ajuste"], situacao(r, d["campeao"], r["pos"]), r["fonte"],
                                             "punição/bônus de pontos (tabela publicada)" if r["ajuste"] else ""])
            if r["clube"] in CLUBES and r["fonte"].startswith("lista de campeões"):   # clube só da lista de campeões (1912-1921)
                so_tabela[r["clube"]][f"wikipedia:{r['clube']}"].append(e.ano_inicio)
        # tabelas publicadas (as que entraram na conferência)
        vistas = set()
        for tb in p["tabelas"]:
            ch = tuple((r["clube"], r["j"], r["pts"]) for r in tb["linhas"])
            if ch in vistas or tb.get("acumulada") or tb.get("parcial") or tb.get("desempate"):
                continue
            vistas.add(ch)
            for r in tb["linhas"]:
                # clube só da tabela (ex.: Hurlingham 1891, que abandonou sem jogar) também entra no clubes.csv
                if r["clube"] in CLUBES:
                    so_tabela[r["clube"]][f"rsssf:{r['nome']}"].append(e.ano_inicio)
                L["tabelas_publicadas"].append([e.temporada, nome_fase(tb["t"].fase, fases) if tb["fonte"] != "bolhist" else "classificação final",
                                                tb["t"].grupo, r["pos"], r["nome"], r["clube"], r["j"], r["v"], r["e"], r["d"], r["gp"],
                                                r["gc"], r["pts"], f"RSSSF ({tb['fonte']}, linha {tb['t'].linha})"])
        # artilheiros: lista da RSSSF; sem ela, a contagem dos gols com autor (quando quase todos os gols têm autor)
        tops = TOPS.get(e.temporada)
        if tops:
            for jog, ctxt, ng in tops:
                fonte = TOPS_FONTE[e.temporada]
                if "/" in ctxt:   # "Estudiantes/Carabobo FC": trocou de clube na temporada; fica o último, os dois na fonte
                    partes = [x.strip() for x in ctxt.split("/")]
                    ctxt = partes[-1] if clube(partes[-1], e.ano_inicio) else ctxt
                    fonte += f"; jogou por {' e '.join(partes)}"
                L["artilheiros"].append([e.temporada, jog, clube(ctxt, e.ano_inicio) or ctxt, ng, fonte])
                if (ca := clube(ctxt, e.ano_inicio)) in CLUBES:   # clube só da lista de artilheiros também entra no clubes.csv
                    so_tabela[ca][f"rsssf:{ctxt}"].append(e.ano_inicio)
        elif gols_ed and autor_ed >= 0.95 * gols_ed:
            cont = Counter((r[2], r[1]) for r in L["gols"] if r[0].startswith(eid + "-") and r[5] != "contra")
            if cont:
                topo = max(cont.values())
                for (jog, c), ng in sorted(cont.items()):
                    if ng == topo:
                        L["artilheiros"].append([e.temporada, jog, c, ng, "contagem dos gols com autor"])
        # edição
        final = d["final"]
        vice = final[1]["clube"] if len(final) > 1 and d["campeao"] else ""   # edição sem campeão (2022 Clausura): sem vice
        L["edicoes"].append([e.temporada, e.ano_inicio, e.ano_fim, e.nome_oficial, len(d["clubes"]), e.pontos_vitoria,
                             ("sem jogos (só a tabela final)" if e.sem_jogos else
                              ("jogos incompletos; " if e.incompleta else "") + formato(ordem_f, L["fases"], e.temporada)),
                             d["campeao"] or "", vice,
                             "; ".join((["RSSSF"] if e.trechos or e.tabelas or e.hist else []) +
                                       (["ogol"] if og["ligado"] else []) + (["ESPN"] if es["ligado"] or e.espn else [])),
                             "; ".join(x for x in (e.obs, e.incompleta and f"jogos incompletos: {e.incompleta}", e.sem_campeao,
                                                   e.pontos_fora and f"pontuação: {e.pontos_fora} (a classificação é a tabela publicada)")
                                       if x)])
        n_tab = 0 if e.sem_jogos or e.incompleta else len(vistas)   # sem jogos: a tabela não tem com o que ser conferida
        n_div = len({x[0] for x in d["difs"]})
        L["conferencia"].append([e.temporada, n, esperados(d), n_tab - n_div, n_div, gols_ed, autor_ed,
                                 f"campeão {d['campeao']} (RSSSF: {d['camp_txt']}; Wikipédia: {WIKI.get(e.temporada, '-')})" +
                                 ("; divergências explicadas no relatório" if n_div else "")])
    # clubes
    for c in set(so_tabela) - usados:
        usados.add(c)
        nomes_fonte[c] = so_tabela[c]
    for c in sorted(usados):
        cid, prov, pais_c = CLUBES[c]
        partes = []
        for nf, anos in sorted(nomes_fonte[c].items()):
            a = sorted(set(anos))
            partes.append(f"{nf}:{a[0]}" + (f"-{a[-1]}" if a[-1] != a[0] else ""))
        L["clubes"].append([c, prov or None, cid or None, pais_c, "|".join(partes)])
    _csv("clubes.csv", ["clube", "regiao", "cidade", "pais", "nomes_fonte"], L["clubes"])
    _csv("edicoes.csv", ["temporada", "ano_inicio", "ano_fim", "nome_oficial", "num_clubes", "pontos_vitoria", "formato", "campeao", "vice",
                         "fontes", "observacao"], L["edicoes"])
    _csv("fases.csv", ["temporada", "ordem", "fase", "tipo", "num_grupos", "formato_serie", "criterio"], L["fases"])
    _csv("partidas.csv", ["id", "temporada", "fase", "grupo", "rodada", "data", "hora", "mandante", "visitante", "gols_mandante",
                          "gols_visitante", "penaltis_mandante", "penaltis_visitante", "resultado_especial", "estadio", "cidade", "publico",
                          "fonte", "fonte_id", "gols_texto", "observacao"], L["partidas"])
    _csv("gols.csv", ["partida_id", "clube", "jogador", "minuto", "acrescimo", "tipo", "fonte"], L["gols"])
    _csv("cartoes.csv", ["partida_id", "clube", "jogador", "minuto", "acrescimo", "cor", "fonte"], L["cartoes"])
    _csv("classificacao_final.csv", ["temporada", "posicao", "clube", "jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra",
                                     "pontos", "ajuste_pontos", "situacao", "fonte", "observacao"], L["classificacao_final"])
    _csv("tabelas_publicadas.csv", ["temporada", "fase", "grupo", "posicao", "nome_fonte", "clube", "jogos", "vitorias", "empates", "derrotas",
                                    "gols_pro", "gols_contra", "pontos", "fonte"], L["tabelas_publicadas"])
    _csv("artilheiros.csv", ["temporada", "jogador", "clube", "gols", "fonte"], L["artilheiros"])
    _csv("conferencia.csv", ["temporada", "jogos", "jogos_esperados", "tabelas_conferidas", "tabelas_divergentes", "gols", "gols_com_autor",
                             "observacao"], L["conferencia"])
    CONF[:] = L["conferencia"]


def esperados(d: dict) -> int:
    """Jogos esperados: pela tabela publicada completa (soma dos jogos / 2) mais os jogos das outras fases; sem ela, os lidos."""
    p = d["p"]
    if d["e"].sem_jogos:
        return 0
    fases_j = {j["fase"] for j in p["jogos"]}
    if {"Apertura", "Clausura"} <= fases_j:   # Apertura e Clausura como fases do ano: uma tabela de cada torneio
        tor = {}
        for tb in p["tabelas"]:
            f = tb["t"].fase
            if f in ("Apertura", "Clausura") and {r["clube"] for r in tb["linhas"]} >= {x for j in p["jogos"] if j["fase"] == f for x in (j["m"], j["v"])}:
                tor.setdefault(f, sum(r["j"] or 0 for r in tb["linhas"]) // 2)
        if len(tor) == 2:
            return sum(tor.values()) + sum(1 for j in p["jogos"] if j["fase"] not in ("Apertura", "Clausura"))
    for tb in p["tabelas"]:
        if tb.get("ok") is not None and not (tb.get("acumulada") or tb.get("parcial") or tb.get("desempate")) and                 {r["clube"] for r in tb["linhas"]} == set(d["clubes"]):
            fase = tb["t"].fase if tb["fonte"] != "bolhist" else ""
            # tabela agregada do ano (Apertura + Clausura, fases do ano): os jogos dos dois torneios já estão nela
            dentro = {fase} | ({"Apertura", "Clausura"} if fase == "" else set())
            return sum(r["j"] for r in tb["linhas"]) // 2 + sum(1 for j in p["jogos"] if j["fase"] not in dentro)
    return len(p["jogos"])


def formato(ordem_f: list[str], linhas_fases: list[list], temporada: str) -> str:
    desc = []
    for r in linhas_fases:
        if r[0] != temporada:
            continue
        t = {"liga": "pontos corridos", "grupos": f"{r[4]} grupos", "mata_mata": "mata-mata"}[r[3]]
        if r[2].startswith("Desempate"):
            t = "desempate"
        if not desc or desc[-1] != t:
            desc.append(t)
    return "mata-mata" if all(x == "mata-mata" for x in desc) else " + ".join(desc)


def diagnostico(d: dict) -> list[str]:
    """Uma linha por clube que não fecha com a tabela publicada, com o motivo quando as fontes deixam ver."""
    p = d["p"]
    saida = []
    ok_por_clube = defaultdict(list)   # tabelas que fecham, por clube
    for tb in p["tabelas"]:
        if tb.get("ok"):
            for r in tb["linhas"]:
                ok_por_clube[r["clube"]].append(tb["fonte"])
    og = d.get("ogol", {}).get("ligado", {})
    ligados = {id(p["jogos"][k]) for k in og}
    for fonte_l, clube_, pub, calc in d["difs"]:
        jogos_c = [j for j in p["jogos"] if clube_ in (j["m"], j["v"]) and j["j"]]
        txt = f"tabela publicada x jogos — {fonte_l}: {clube_} tabela {pub} jogos {calc}"
        if ok_por_clube.get(clube_):
            txt += f" — a outra tabela publicada ({ok_por_clube[clube_][0]}) fecha com os jogos: o erro é desta tabela"
        elif jogos_c and all(id(j) in ligados and (og_g := next(g for k, g in og.items() if p["jogos"][k] is j)) and
                             (og_g["gols_mandante"], og_g["gols_visitante"]) == (j["j"].gm, j["j"].gv) for j in jogos_c):
            txt += " — o ogol traz os mesmos placares para todos os jogos do clube: o erro é da tabela publicada"
        elif (dec := [j for j in jogos_c if j["esp"] in ("awd", "wo_m", "wo_v", "abd", "anulado") and
                      ({j["m"], j["v"]} - {clube_}) & {x[1] for x in d["difs"] if x[0] == fonte_l}]):
            j = dec[0]
            txt += (f" — a diferença vem de {j['m']} x {j['v']} ({j['j'].data or 's/d'}), decidido fora de campo ou abandonado: a "
                    f"tabela conta esse jogo de outro jeito (gols do campo, sem gols ou sem o jogo)")
        elif pub[0] != calc[0]:
            txt += f" — {'faltam' if calc[0] < pub[0] else 'sobram'} {abs(pub[0] - calc[0])} jogo(s) do clube na página"
        else:
            txt += " — mesmo número de jogos; placar diferente em algum jogo do clube (a página não diz qual)"
        saida.append(txt)
    return saida


def relatorio(eds: list[dict]) -> None:
    n_ed, n_sem = len(eds), sum(1 for d in eds if d["e"].sem_jogos)
    n_inc = sum(1 for d in eds if d["e"].incompleta)
    linhas = ["# Campeonato Hondurenho (Liga Nacional) — coleta de dados", "",
              "Gerado por `python coleta/hon-1/importar.py`. Pacote em `data/coleta/hon-1/pacote/`.", "",
              f"**Edições:** {n_ed}, uma por título, como a lista de campeões da RSSSF (`hondchamp.html`, 87 títulos da Liga "
              "Nacional). Escopo decidido em 24/11/2026, depois de pesquisa a pedido do Guilherme: só a Liga Nacional, de "
              "1965/66 em diante, como a liga conta. Um campeão por temporada até 1996/97 (1972/73 foi abandonada e entra sem "
              "campeão); Apertura e Clausura de 1997/98 em diante, uma edição cada, com o torneio único de 1999; o Clausura "
              "2020 (pandemia) entra sem campeão. A Liga Amateur de Honduras (1947-1964) fica fora: era um mata-mata entre "
              "campeões regionais, a RSSSF a lista à parte e a liga e a FENAFUTH não reconhecem esses títulos.", "",
              f"**Edições sem jogos ({n_sem}):** de 1965/66 a 1995/96 (a RSSSF só tem as tabelas finais, `hondhist.html`) e as "
              "edições de 2010/11 e 2011/12 em que a página só tem as tabelas e a fase final.", "",
              "**Fontes:** RSSSF (`data/coleta/hon-1/rsssf/`) e ESPN (liga `hon.1`: hora, estádio, público, gols com minuto e "
              "cartões, casados com os jogos da RSSSF).", "",
              "**Clubes:** nomes e identidades no começo de `coleta/hon-1/clubes_hon.py` (La Salle = San Pedro; Honduras = "
              "Honduras Progreso; Atlético Olanchano e Olancho FC separados). Homônimos de clubes de outros países levam a "
              "cidade ou o país: Olimpia de Tegucigalpa, Necaxa de Tegucigalpa, Real Sociedad de Tocoa, Palestino de Honduras, "
              "Independiente de Honduras, Progreso de Honduras, Atlético Español de Honduras, Platense de Puerto Cortés, San "
              "Pedro de Honduras, Atlántida de La Ceiba.", "",
              "**Pontos:** 2 por vitória até 1993/94 e 3 a partir de 1994/95.", "",
              "| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |",
              "|---|---|---|---|---|---|---|---|"]
    conf = {r[0]: r for r in CONF}
    for d in eds:
        e = d["e"]
        c = conf[e.temporada]
        linhas.append(f"| {e.temporada} | {len(d['clubes'])} | {c[1]} ({c[2]}) | {c[5]} | {c[6]} | {c[3]} / {c[4]} | {d['campeao']} | "
                      f"{d['final'][0]['fonte'] if d['final'] else '-'} |")
    linhas += ["", "## Conferência e correções, edição a edição", ""]
    for d in eds:
        e = d["e"]
        especiais = []
        for j in d["p"]["jogos"]:
            x = j["j"]
            if x and j["esp"] in ("wo_m", "wo_v", "awd", "abd", "anulado", "n/p"):
                rot = {"wo_m": "W.O./pontos para o mandante", "wo_v": "W.O./pontos para o visitante", "awd": "decidido fora de campo",
                       "abd": "abandonado/suspenso, sem valer", "anulado": "anulado", "n/p": "não jogado"}[j["esp"]]
                placar = f" {x.gm}-{x.gv}" if x.gm is not None else ""
                especiais.append(f"{rot} — {j['m']}{placar} {j['v']} ({x.data or 's/d'}){': ' + x.nota if x.nota else ''}")
        og = d.get("ogol") or {}
        fontes = [f"ogol: {len(og.get('ligado', {}))} jogos casados (edição {og['edicao']} do ogol, {og.get('n', 0)} jogos)"]             if og.get("ligado") else []
        es = d.get("espn") or {}
        if es.get("ligado"):
            fontes.append(f"ESPN: {len(es['ligado'])} jogos casados")
        itens = EXPLICACOES.get(e.temporada, []) + ([e.obs] if e.obs else []) + fontes + diagnostico(d) + d["log"] + especiais
        linhas.append(f"### {e.temporada}")
        linhas.append("")
        linhas += [f"- {x}" for x in itens] or ["- sem ocorrências"]
        linhas.append("")
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(linhas) + "\n", encoding="utf-8")


CONF: list = []


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    cps = campeoes()
    from ler_rsssf import vices, vices_texto
    VICES.update(vices())   # vice da lista de campeões da RSSSF
    eds = []
    for e in EDICOES:
        d = montar(e, cps)
        eds.append(d)
        print(f"{e.temporada:20s} {len(d['p']['jogos']):4d} jogos  campeão {d['campeao']}  divergências {len(d['difs'])}", flush=True)
    gravar(eds)
    relatorio(eds)
    print("pacote gravado em", PACOTE, "e relatório em", RELATORIO)
