"""Junta as fontes da 1ª divisão venezuelana e grava o pacote em data/coleta/ven-1/pacote/ e o relatório em docs/coleta/ven-1.md.

Fontes, na ordem em que entram:
- RSSSF (ler_rsssf.py): base de jogos, fases, grupos, rodadas, datas e autores dos gols (uma página por temporada, venezYY);
  as tabelas das páginas são a conferência e, nas edições incompletas, a classificação. A lista de campeões
  (venezchamp.html) traz campeão e vice; a de artilheiros, veneztops.html (1957-2007/08).
- ESPN (liga ven.1, 2005 em diante): hora, estádio, público, gols com minuto e cartões; jogos do Clausura 2011, de 2011/12 e
  de 2025 (a RSSSF tem só parte deles ou só as tabelas).
- Wikipédia em inglês (campeoes_wiki.py): segunda fonte do campeão e do vice e fonte dos artilheiros fora da lista da RSSSF.

Uso: python coleta/ven-1/importar.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
sys.path.insert(0, str(AQUI))
import autores  # noqa: E402
import outras_fontes  # noqa: E402
from clubes_ven import CLUBES, clube  # noqa: E402
from conferir import conferir_tabelas, eh_mata, preparar, soma  # noqa: E402
from edicoes import EDICOES, PACOTE, RELATORIO, SLUG, Edicao  # noqa: E402
from explicacoes import CORRIGE, EXPLICACOES, EXTRAS  # noqa: E402
from ler_rsssf import campeoes  # noqa: E402
from rsssf_sul import chave  # noqa: E402

# ordem das fases (quanto maior, mais longe o clube chegou); os torneios do ano (Apertura, Intermedio, Clausura) e as finais
# de cada um ficam no nível 0: decidem vaga nas finais do campeonato, não o título
NIVEL_FASE = {"": 0, "Grupo do rebaixamento": 0, "Desempate do rebaixamento": 0, "Desempate do 2º lugar": 1, "Segunda fase": 1,
              "Quadrangulares semifinais": 4, "Pentagonais": 3, "Triangulares": 4, "Hexagonal final": 5, "Octogonal final": 5,
              "Quadrangular final": 6, "Finalísima": 6,
              "Terceira fase": 1, "Nacional": 2, "Oitavas de final": 3, "Quartas de final": 4,
              "Desempate da tabela anual": 1, "Fase final": 2, "Semifinal": 5, "Final": 6, "Desempate do título": 6,
              "Liguillas": 1, "Liguillas do Apertura": 0, "Liguillas do Clausura": 0, "Hexagonal 2": 1,
              "Triangular do 2º lugar": 1, "Desempate da segunda fase": 1, "Desempate do 6º lugar": 1}
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
    # campeão pela lista da RSSSF (venezchamp.html); sem ela, pela Wikipédia
    camp_txt = e.campeao_rsssf or cps.get(e.temporada, "") or WIKI.get(e.temporada, "")
    campeao = clube(camp_txt, e.ano_inicio) if camp_txt else None
    if not campeao and camp_txt:
        log.append(f"campeão da lista da RSSSF não reconhecido: {camp_txt}")
    final = classificacao(e, p, calc, nivel, campeao, clubes)
    return {"e": e, "p": p, "difs": difs, "log": log, "clubes": clubes, "campeao": campeao, "camp_txt": camp_txt,
            "final": final, "fases": fases}


def artilheiros_rsssf() -> dict[str, list[tuple[str, str, int]]]:
    """veneztops.html: temporada -> [(jogador, clube como na página, gols)], de 1957 a 2007/08; empate na artilharia vem em
    linhas seguidas sem o ano; "1986-87" é a temporada "1986/87"; 1974 sem dados. Colunas: ano, jogador em maiúsculas com a
    nacionalidade entre parênteses ("PEDRO PASCUAL PERALTA (Paraguay)"), clube e gols."""
    from ler_rsssf import linhas
    saida: dict[str, list] = defaultdict(list)
    ano = None
    for l in linhas("veneztops"):
        if l.strip().startswith("About this document"):
            break
        m = re.match(r"^(\d{4}(?:-\d{2})?)?\s+(\S.*?)(?:\s+\([A-Z][a-z]+\))?\s{2,}(\S.*?)\s+(\d{1,2})\s*$", l)
        if not m:
            continue
        if m.group(1):
            ano = m.group(1).replace("-", "/")
        if not ano:
            continue
        cap = lambda p: (p[0] + p[1:].capitalize()) if p[0] in "\"'(" else p.capitalize()
        jog = " ".join(cap(p) if p.isupper() and len(p) > 1 else p for p in m.group(2).split())
        saida[ano].append((jog, m.group(3).strip(), int(m.group(4))))
    return saida


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
    if e.sem_jogos or e.incompleta:   # sem jogos ou com parte deles: a tabela final da RSSSF é a classificação
        pub = next((tb for tb in p["tabelas"] if tb.get("sem_conferencia")), None)
    linhas = []
    if pub:
        parcial = any(r["v"] is None for r in pub["linhas"])
        for k, r in enumerate(pub["linhas"], 1):
            ajuste = None if None in (r["v"], r["e"], r["d"], r["pts"]) else r["pts"] - pontos(r["v"], r["e"], r["d"])
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
        "slug": SLUG, "nome": "Campeonato Venezuelano", "nome_curto": "Venezuelano", "tipo": "liga", "nivel": 1, "pais": "VEN",
        "pais_nome": "Venezuela", "regiao": None, "confederacao": "CONMEBOL", "rotulo_painel": "Venezuelano",
        "menu_painel": "Venezuela · 1ª divisão", "do_painel": "do Campeonato Venezuelano", "o_painel": "o Campeonato Venezuelano",
        "observacao": "1ª divisão venezuelana de 1921 (temporada 1920/21) a 2025, uma edição por título, como na lista de "
                      "campeões da RSSSF: era amadora (1921-1956; jogos só em parte), profissional em ano fechado (1957-1986), "
                      "calendário europeu (1986/87 a 2014/15; Apertura e Clausura são fases), Torneo de Adecuación 2015 e "
                      "Liga FUTVE (2016 em diante). Jogos completos de 1957 em diante, salvo 1993/94 e 1994/95 (fases só com "
                      "tabelas); sem jogos em 1922, 1924, 1931, 1938, 1939, 1949 e 1950."},
        ensure_ascii=False, indent=1), encoding="utf-8")
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
            mata = eh_mata(f) and f != "Repechaje"
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
                              formato(ordem_f, L["fases"], e.temporada)), d["campeao"] or "", vice,
                             "; ".join((["RSSSF"] if e.trechos or e.tabelas else []) +
                                       (["ogol"] if og["ligado"] else []) + (["ESPN"] if es["ligado"] else [])), e.obs])
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
        cid, prov = CLUBES[c]
        partes = []
        for nf, anos in sorted(nomes_fonte[c].items()):
            a = sorted(set(anos))
            partes.append(f"{nf}:{a[0]}" + (f"-{a[-1]}" if a[-1] != a[0] else ""))
        L["clubes"].append([c, prov or None, cid or None, "VEN", "|".join(partes)])
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
    for tb in p["tabelas"]:
        if tb.get("ok") is not None and not (tb.get("acumulada") or tb.get("parcial") or tb.get("desempate")) and                 {r["clube"] for r in tb["linhas"]} == set(d["clubes"]):
            fase = tb["t"].fase if tb["fonte"] != "bolhist" else ""
            return sum(r["j"] for r in tb["linhas"]) // 2 + sum(1 for j in p["jogos"] if j["fase"] != fase)
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
    linhas = ["# Campeonato Venezuelano (1ª divisão) — coleta de dados", "",
              "Gerado por `python coleta/ven-1/importar.py`. Pacote em `data/coleta/ven-1/pacote/`.", "",
              f"**Edições:** {n_ed}, uma por título de 1921 (temporada 1920/21) a 2025, como na lista de campeões da RSSSF "
              "(`venezchamp.html`, 106 títulos). A Wikipédia em inglês (página \"Liga FUTVE\") tem os mesmos campeões, "
              "menos o Torneo de Adecuación 2015, que ela não conta como temporada; aqui ele entra, como na RSSSF. Era "
              "amadora (1921-1956), profissional em ano fechado (1957-1986), calendário europeu de 1986/87 a 2014/15 "
              "(Apertura, Clausura, liguillas e finais são fases do ano), Adecuación 2015 e Liga FUTVE (2016 em diante, "
              "Apertura e Clausura com final entre os vencedores).", "",
              "**Fora do pacote:** a 2ª e a 3ª divisões, a Copa Venezuela (salvo quando foi a 1ª fase da temporada: "
              "1993/94, 1994/95, 1995/96 e 2000/01), as outras copas (Copa Caracas, Liga Mayor, de las Naciones, "
              "Cuatricentenario, Valencia, de Campeones, Bicentenario), os jogos de promoção e os playoffs da Sudamericana "
              "e da Conmebol.", "",
              f"**Edições sem jogos ({n_sem}):** 1922, 1924, 1931, 1938, 1939, 1949 e 1950: a RSSSF não tem página desses "
              "anos; entram com o campeão e o vice da lista.", "",
              "**Edições com jogos incompletos:** a era amadora (1921-1956), salvo 1940, 1955 e 1956: a RSSSF traz só parte "
              "dos jogos da liga (ou só o campeão e a classificação; os jogos das copas da mesma página ficam de fora); 1993/94 (o Apertura, que era a Copa Venezuela, só tem as "
              "tabelas dos grupos, e 8 jogos da liga estão sem placar); 1994/95 (o Torneo Iniciación só tem as tabelas). "
              "Nelas a classificação é a tabela publicada, sem conferência; o que falta está na observação da edição.", "",
              "**Fontes:** RSSSF (uma página por temporada, `venezYY.html` / `venezAAAA.html`, em "
              "`data/coleta/ven-1/rsssf/`: base de jogos, com fases, grupos, rodadas, datas e autores dos gols; lista de "
              "campeões `venezchamp.html`; artilheiros `veneztops.html`, 1957-2007/08); ESPN (liga `ven.1`, 2005 em diante: "
              "hora, estádio, público, gols com minuto e cartões; jogos do Clausura 2011, de 2011/12 e de 2025, que a RSSSF "
              "tem só em parte ou só nas tabelas); Wikipédia em inglês (lista de campeões: segunda fonte do campeão e do "
              "vice e fonte dos artilheiros depois de 2007/08).", "",
              "**Clubes:** nome pelo qual o clube é conhecido (Caracas FC, Deportivo Táchira, Estudiantes de Mérida, "
              "Mineros de Guayana). O mesmo clube com outro nome, como na lista de campeões da RSSSF: Unión Atlético "
              "Táchira (1985-1999) é o Deportivo Táchira; ItalChacao e Deportivo Petare são o Deportivo Italia; o Atlético "
              "Zulia (1996/97 e 1997/98) é o Unicol de Lagunillas renomeado; o Internacional de Lara (1998/99) é o "
              "Trujillanos; UE Lara e UD Lara são a Unión Deportiva Lara; Internacional de Barinas é o Hermanos Colmenárez. "
              "Clubes diferentes com nome parecido ficam separados: Atlético Zamora (até 2005) e Zamora FC; Lara FC "
              "(1965-1985), Unión Deportiva Lara (1986-2002) e Deportivo Lara (2009 em diante); Anzoátegui FC (1967), "
              "Atlético Anzoátegui (1986-1990), Deportivo Anzoátegui (2007 em diante) e o Anzoátegui FC de 2025; Atlético "
              "Monagas (2000) e Monagas SC; Estudiantes de Caracas (era amadora) e Estudiantes de Caracas SC (2015-2019). "
              "Homônimos de clubes de outros países levam a cidade ou o país (Deportivo Español de Caracas, Celta de "
              "Caracas, Danubio de Caracas, América de Caracas).", "",
              "**Regras:** o placar é o da fonte de base (RSSSF; ESPN onde a RSSSF não tem). Jogo decidido no tribunal leva "
              "o placar dado (`awd`), com o de campo na observação; \"bt\" / \"lt\" (venceu / perdeu sem placar "
              "conhecido) viram W.O. (vitória sem gols, como a tabela conta); \"drw\" (empate sem placar, 1994/95) fica "
              "de fora. Ida e volta numa linha só (\"A 1-0 0-4 B\") vira dois jogos, com os gols de A primeiro e o mando "
              "da volta presumido. Pontos: 2 por vitória até 1994/95 e 3 a partir de 1995/96. Nas edições sem jogos, "
              "campeão e vice da lista ficam em 1º e 2º.", "",
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
    from campeoes_wiki import campeoes as campeoes_wiki, vices as vices_wiki
    from ler_rsssf import vices
    VICES.update({**vices_wiki(), **vices()})   # vice da lista da RSSSF; a da Wikipédia confere
    WIKI.update(campeoes_wiki())
    from campeoes_wiki import artilheiros as artilheiros_wiki
    for t_, v_ in artilheiros_wiki().items():   # Wikipédia em inglês onde a lista da RSSSF (1957-2007/08) não chega
        TOPS[t_], TOPS_FONTE[t_] = v_, "Wikipédia em inglês (lista de campeões)"
    for t_, v_ in artilheiros_rsssf().items():
        TOPS[t_], TOPS_FONTE[t_] = v_, "RSSSF (veneztops.html)"
    eds = []
    for e in EDICOES:
        d = montar(e, cps)
        eds.append(d)
        print(f"{e.temporada:20s} {len(d['p']['jogos']):4d} jogos  campeão {d['campeao']}  divergências {len(d['difs'])}", flush=True)
    gravar(eds)
    relatorio(eds)
    print("pacote gravado em", PACOTE, "e relatório em", RELATORIO)
