"""Junta as fontes da 1ª divisão peruana e grava o pacote em data/coleta/per-1/pacote/ e o relatório em docs/coleta/per-1.md.

Fontes, na ordem em que entram:
- RSSSF (ler_rsssf.py): base de jogos, fases, grupos, rodadas, datas e autores dos gols (1930-1942, 1968, 1969, 1975, 1978,
  1980, 1981, 1983, 1984 e 1986 em diante). As tabelas das páginas e as tabelas finais de peruhist.html são a conferência;
  nos anos sem jogos, a tabela final de peruhist.html é a classificação, e sem ela entram o campeão e o vice da Wikipédia.
- Wikipédia em espanhol (wikipedia_jogos.py): jogos de 1926-1929, 1943-1967, 1982 e 1985.
- ESPN (liga per.1, 2005 em diante): hora, estádio, público, gols com minuto e cartões.

Uso: python coleta/per-1/importar.py
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
from clubes_per import CLUBES, clube  # noqa: E402
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
              "Liguillas": 1}
WIKI: dict[str, str] = {}
VICES: dict[str, str] = {}
TOPS: dict[str, list] = {}


def nome_fase(f: str, fases: set[str]) -> str:
    if f:
        return f
    return "Primeira fase" if fases - {""} else "Fase única"


def id_edicao(e: Edicao) -> str:
    return re.sub(r"[^0-9a-z]+", "-", chave(e.temporada))


def especial(esp: str) -> str:
    return {"wo_m": "wo", "wo_v": "wo", "awd": "awd", "abd": "abd", "anulado": "n/p", "n/p": "n/p"}.get(esp, "")


def virada_do_ano(e: Edicao, jogos: list[dict]) -> None:
    """PE-010: em 1990 os jogos de janeiro (liguilla final do Regional II e final nacional) são de 1991; a 1ª fase começa em
    abril de 1990."""
    if e.temporada != "1990":
        return
    for j in jogos:
        if j["j"] and j["j"].data and j["j"].data[:7] == "1990-01":
            j["j"].data = "1991" + j["j"].data[4:]


def montar(e: Edicao, cps: dict[str, str]) -> dict:
    p = preparar(e)
    virada_do_ano(e, p["jogos"])
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
    if e.sem_jogos:   # edição sem jogos: os clubes são os da tabela final
        clubes = sorted({r["clube"] for tb in p["tabelas"] for r in tb["linhas"] if r["clube"]})
    calc = soma(jogos, set(clubes))
    nivel: dict[str, int] = defaultdict(int)
    for j in jogos:
        for x in (j["m"], j["v"]):
            nivel[x] = max(nivel[x], NIVEL_FASE.get(j["fase"], 0))
    # campeão pela lista da RSSSF (peruchamp.html); 1912-1921 (fora da lista principal da RSSSF), pela Wikipédia
    camp_txt = e.campeao_rsssf or cps.get(e.temporada, "") or WIKI.get(e.temporada, "")
    campeao = clube(camp_txt, e.ano_inicio) if camp_txt else None
    if not campeao and camp_txt:
        log.append(f"campeão da lista da RSSSF não reconhecido: {camp_txt}")
    final = classificacao(e, p, calc, nivel, campeao, clubes)
    return {"e": e, "p": p, "difs": difs, "log": log, "clubes": clubes, "campeao": campeao, "camp_txt": camp_txt,
            "final": final, "fases": fases}


def artilheiros_rsssf() -> dict[str, list[tuple[str, str, int]]]:
    """perutops.html: temporada -> [(jogador, clube como na página, gols)], de 1928 a 2025; empate na artilharia vem em
    linhas seguidas sem o ano. "[Uruguay]" depois do nome é a nacionalidade; "[*]" no fim marca o artilheiro do campeão."""
    from ler_rsssf import linhas
    saida: dict[str, list] = defaultdict(list)
    ano = None
    for l in linhas("perutops"):
        # " 1928   Alejandro VILLANUEVA                    Alianza Lima             3  [*]"; "        Felipe RODRIGUEZ [Uruguay] ..."
        m = re.match(r"^\s*(\d{4})?\s+(\S.*?)(?:\s*\[[A-Za-z ]+\])?\s{2,}(\S.*?)\s+(\d{1,2})\s*(?:\[\*\])?\s*$", l)
        if not m or re.search(r"\d", m.group(3)) or re.search(r"No tournament", l):
            continue
        if m.group(1):
            ano = m.group(1)
        if not ano:
            continue
        cap = lambda p: (p[0] + p[1:].capitalize()) if p[0] in "\"'(" else p.capitalize()   # "LOLO" entre aspas
        jog = " ".join(cap(p) if p.isupper() and len(p) > 1 else p for p in m.group(2).split())
        saida[ano].append((jog, m.group(3).strip(), int(m.group(4))))
    return saida


def classificacao(e: Edicao, p: dict, calc: dict, nivel: dict, campeao: str | None, clubes: list[str]) -> list[dict]:
    """Classificação final: a tabela publicada que traz todos os clubes e fecha com os jogos (ordem oficial, pontos com
    punições); sem ela, calculada (fase alcançada, pontos, saldo, gols pró). O campeão da lista oficial fica em 1º."""
    pv = e.pontos_vitoria
    pontos = (lambda v, e_, d: 3 * v + 2 * e_ + d) if 1931 <= e.ano_inicio <= 1942 else (lambda v, e_, d: pv * v + e_)
    # entre as tabelas que fecham com os jogos e trazem todos os clubes, a de mais jogos (a acumulada do ano, quando há)
    ts = [tb for tb in p["tabelas"] if not tb.get("acumulada") and tb.get("ok")]
    # tabela cortada em duas pela linha de rebaixamento ("- - - -"): as duas partes seguidas da mesma página viram uma
    ts += [{**a, "linhas": a["linhas"] + b["linhas"]} for a, b in zip(ts, ts[1:])
           if a["fonte"] == b["fonte"] and not {r["clube"] for r in a["linhas"]} & {r["clube"] for r in b["linhas"]} and
           b["linhas"][0]["pos"] == len(a["linhas"]) + 1]
    cands = [tb for tb in ts if {r["clube"] for r in tb["linhas"]} == set(clubes)]
    pub = max(cands, key=lambda tb: sum(r["j"] or 0 for r in tb["linhas"]), default=None)
    if e.sem_jogos:   # sem jogos: a tabela final da RSSSF é a classificação
        pub = next((tb for tb in p["tabelas"] if tb.get("sem_conferencia")), None)
    if e.temporada in TABELAS_CLASS:   # tabela(s) do ano inteiro, emendadas (PE-002, PE-004, PE-006, PE-008)
        por_id = {f"{tb['fonte']}:{tb['t'].linha}": tb for tb in p["tabelas"]}
        partes = [por_id[k] for k in TABELAS_CLASS[e.temporada] if k in por_id]
        vistos: set = set()
        rows = [r for x in partes for r in x["linhas"] if not (r["clube"] in vistos or vistos.add(r["clube"]))]
        if e.temporada in POR_PONTOS:   # 2009 e 2012: as duas liguillas (44 jogos cada clube) por pontos
            rows.sort(key=lambda r: (-(r["pts"] or 0), -((r["gp"] or 0) - (r["gc"] or 0))))
        pub = {**partes[0], "fonte": "+".join(f"{x['fonte']}:{x['t'].linha}" for x in partes), "linhas": rows} if partes else pub
    elif e.temporada in SOMA_ANO:   # 2001, 2004, 2005: sem tabela acumulada na página; a soma do Apertura e do Clausura (PE-008)
        pub = None
    linhas = []
    if pub:
        parcial = any(r["v"] is None for r in pub["linhas"])
        for k, r in enumerate(pub["linhas"], 1):
            ajuste = None if None in (r["v"], r["e"], r["d"], r["pts"]) else r["pts"] - pontos(r["v"], r["e"], r["d"])
            linhas.append({"clube": r["clube"], "j": r["j"], "v": r["v"], "e": r["e"], "d": r["d"], "gp": r["gp"], "gc": r["gc"],
                           "pts": r["pts"], "ajuste": ajuste, "obs": r.get("obs", ""),
                           "fonte": f"RSSSF ({pub['fonte']}{', tabela parcial' if parcial else ''})"})
        # a ordem publicada vale; empates sem número herdam a posição de cima
    elif e.sem_jogos and 1912 <= e.ano_inicio <= 1921:   # Liga Peruana (D-06 A, PE-019): a ordem e os participantes da página
        from ler_rsssf import ranking_liga
        for pos, nome in ranking_liga(e.ano_inicio):
            c = clube(nome, e.ano_inicio)
            if c and all(r["clube"] != c for r in linhas):
                linhas.append({"clube": c, "j": None, "v": None, "e": None, "d": None, "gp": None, "gc": None, "pts": None,
                               "ajuste": None, "obs": "" if pos else "participante (a página não dá a posição)",
                               "fonte": f"RSSSF (peru{e.ano_inicio}: ordem{'' if pos else ' e participantes'})"})
    elif e.sem_jogos:   # sem jogos e sem tabela: só o campeão e o vice da Wikipédia
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
    if pub and not e.sem_jogos:   # clubes com jogos que a tabela usada não tem vêm depois, calculados
        for c in sorted(set(clubes) - {r["clube"] for r in linhas}, key=lambda c: -(calc.get(c, [0] * 6)[1])):
            x = calc.get(c, [0] * 6)
            linhas.append({"clube": c, "j": x[0], "v": x[1], "e": x[2], "d": x[3], "gp": x[4], "gc": x[5],
                           "pts": pontos(x[1], x[2], x[3]), "ajuste": 0, "obs": "", "fonte": "calculada (fora da tabela usada)"})
    if not e.sem_jogos:   # clube sem jogo válido na edição (2021, Carlos Stein: só um jogo anulado) fica de fora (PE-006)
        linhas = [r for r in linhas if r["j"] or r["clube"] == campeao]
    if e.temporada == "2021":
        # PE-006 e PE-007: a tabela anual da RSSSF é de antes do TAS (21/01/2022), que anulou o 3-0 dado ao Cusco sobre o
        # Cienciano (vale o 2-2 de campo): Cusco 23 pontos, Cienciano 39; rebaixados Cusco FC e Alianza Universidad
        for r in linhas:
            if r["clube"] == "Cusco FC":
                r.update(v=r["v"] - 1, e=r["e"] + 1, pts=r["pts"] - 2, gp=r["gp"] - 1, gc=r["gc"] + 2, obs="Relegated (TAS)")
            elif r["clube"] == "Cienciano":
                r.update(d=r["d"] - 1, e=r["e"] + 1, pts=r["pts"] + 1, gp=r["gp"] + 2, gc=r["gc"] - 1)
            elif r["clube"] == "Universidad San Martín":
                r["obs"] = "salvo da queda pela decisão do TAS"
        linhas.sort(key=lambda r: -(r["pts"] or 0))
    if campeao and linhas and linhas[0]["clube"] != campeao and any(r["clube"] == campeao for r in linhas):
        c = next(r for r in linhas if r["clube"] == campeao)
        linhas.remove(c)
        linhas.insert(0, c)
    # vice da lista da Wikipédia (o finalista, nos anos com final) logo abaixo do campeão
    vice = clube(VICES.get(e.temporada, ""), e.ano_inicio) if VICES.get(e.temporada) else None
    if vice and vice != campeao and len(linhas) > 2 and linhas[1]["clube"] != vice and any(r["clube"] == vice for r in linhas):
        v = next(r for r in linhas if r["clube"] == vice)
        linhas.remove(v)
        linhas.insert(1, v)
    for k, r in enumerate(linhas, 1):
        r["pos"] = k
    return linhas


TABELAS_CLASS = {
    "1970": ["peruhist:978", "peruhist:988"], "1972": ["peruhist:1078", "peruhist:1059"], "1973": ["peruhist:1120", "peruhist:1099"],
    "1974": ["peruhist:1166", "peruhist:1141"], "1977": ["peruhist:1297", "peruhist:1278"],
    "1979": ["peruhist:1404", "peruhist:1415", "peruhist:1385"],
    "1998": ["peru98:718", "peru98:722"], "2000": ["peru00:784", "peru00:795"], "2009": ["peru09:714", "peru09:909"],
    "2012": ["peru2012:734", "peru2012:751"], "2020": ["peru2020:919"], "2021": ["peru2021:783"],
}
POR_PONTOS = {"2009", "2012"}
SOMA_ANO = {"2001", "2004", "2005"}


def situacao(r: dict, campeao: str | None, k: int) -> str:
    if r["clube"] == campeao:
        return "campeao"
    if k == 2 and campeao:
        return "vice"
    # PE-003: só "Relegated" explícito; "to Relegation Group/Playoff" não é queda
    if re.search(r"(?<!to )\brelegated\b|descend|rebaix", r.get("obs", ""), re.I):
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
        "slug": SLUG, "nome": "Campeonato Peruano", "nome_curto": "Peruano", "tipo": "liga", "nivel": 1, "pais": "PER",
        "pais_nome": "Peru", "regiao": None, "confederacao": "CONMEBOL", "rotulo_painel": "Peruano",
        "menu_painel": "Peru · 1ª divisão", "do_painel": "do Campeonato Peruano", "o_painel": "o Campeonato Peruano",
        "observacao": "1ª divisão peruana de 1912 a 2025, um campeão por ano (sem campeonato em 1922-1925 e 1936). 1912-1921: "
                      "Liga Peruana de Football, só com campeão e vice. Sem jogos em 1970-1974, 1976, 1977 e 1979 (só a tabela "
                      "final); jogos incompletos em 1926, 1982, 1984, 1986, 1988-1991 e 2003."},
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
                pref = "wikipedia" if x.texto.startswith("wiki") else "rsssf"
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
            base = ("wikipedia" if x.texto.startswith("wiki") else "rsssf") if x else "rsssf"
            fonte_id = ((f"wikipedia:{x.texto[5:]}" if base == "wikipedia" else f"rsssf:{x.texto}") if x else ex["fonte_id"])
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
                                  {"wikipedia": "Wikipédia (es)"}.get(base, "RSSSF"), fonte_id,
                                  "" if sep or not texto_autores or not autores.eh_autores(texto_autores) else texto_autores,
                                  "; ".join(o for o in obs if o)])
        # classificação final
        for r in d["final"]:
            L["classificacao_final"].append([e.temporada, r["pos"], r["clube"], r["j"], r["v"], r["e"], r["d"], r["gp"], r["gc"],
                                             r["pts"], r["ajuste"], situacao(r, d["campeao"], r["pos"]), r["fonte"],
                                             "punição/bônus de pontos (tabela publicada)" if r["ajuste"] else ""])
            if r["clube"] in CLUBES and r["fonte"].startswith("lista de campeões"):   # clube só da lista de campeões (1912-1921)
                so_tabela[r["clube"]][f"wikipedia:{r['clube']}"].append(e.ano_inicio)
            elif r["clube"] in CLUBES and r["fonte"].startswith(f"RSSSF (peru{e.ano_inicio}:"):   # ordem da Liga Peruana
                so_tabela[r["clube"]][f"rsssf:{r['clube']}"].append(e.ano_inicio)
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
                L["tabelas_publicadas"].append([e.temporada, nome_fase(tb["t"].fase, fases) if (tb["fonte"].startswith("peru") and tb["fonte"] != "peruhist") else "classificação final",
                                                tb["t"].grupo, r["pos"], r["nome"], r["clube"], r["j"], r["v"], r["e"], r["d"], r["gp"],
                                                r["gc"], r["pts"], f"RSSSF ({tb['fonte']}, linha {tb['t'].linha})"])
        # artilheiros: lista da RSSSF; sem ela, a contagem dos gols com autor (quando quase todos os gols têm autor)
        tops = TOPS.get(e.temporada)
        if tops:
            for jog, ctxt, ng in tops:
                L["artilheiros"].append([e.temporada, jog, clube(ctxt, e.ano_inicio) or ctxt, ng, "RSSSF (perutops.html)"])
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
        vice = final[1]["clube"] if len(final) > 1 else ""
        L["edicoes"].append([e.temporada, e.ano_inicio, e.ano_fim, e.nome_oficial, len(d["clubes"]), e.pontos_vitoria,
                             ("sem jogos (só a tabela final)" if e.sem_jogos else
                              formato(ordem_f, L["fases"], e.temporada)), d["campeao"] or "", vice,
                             "; ".join((["RSSSF"] if e.trechos or e.tabelas else []) + (["Wikipédia (es)"] if e.wiki else []) +
                                       (["ogol"] if og["ligado"] else []) + (["ESPN"] if es["ligado"] else [])), e.obs])
        n_tab = 0 if e.sem_jogos else len(vistas)   # sem jogos: a tabela não tem com o que ser conferida
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
        L["clubes"].append([c, prov or None, cid or None, "PER", "|".join(partes)])
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
            fase = tb["t"].fase if (tb["fonte"].startswith("peru") and tb["fonte"] != "peruhist") else ""
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
    linhas = ["# Campeonato Peruano (1ª divisão) — coleta de dados", "",
              "Gerado por `python coleta/per-1/importar.py`. Pacote em `data/coleta/per-1/pacote/`.", "",
              f"**Edições:** {n_ed}, uma por título de campeão peruano, de 1912 a 2025, como na lista de campeões da RSSSF "
              "(`peruchamp.html`) e na Wikipédia em inglês (\"List of Peruvian football champions\"). Um campeão por ano; sem "
              "campeonato de 1922 a 1925 e em 1936 (sem torneio oficial, ano dos Jogos Olímpicos). Apertura, Clausura, Torneo de "
              "Verano, Regional, liguillas e finais são fases da edição anual.", "",
              "**1912-1921 (Liga Peruana de Football):** a liga anterior à Federação Peruana de Futebol (1922). A RSSSF lista "
              "esses campeões à parte e não os soma aos títulos nacionais; a Wikipédia em inglês os conta (numera os títulos a "
              "partir de 1912). Entram como edições só com o campeão e o vice (da Wikipédia): nenhuma fonte pública tem tabela "
              "ou jogos completos (a RSSSF tem 8 jogos soltos de 1912). Se o agente 1 preferir a contagem da RSSSF, basta tirar "
              "essas 10 edições.", "",
              f"**Edições sem jogos ({n_sem}):** 1912-1921, 1970-1974, 1976, 1977 e 1979. Pesquisamos RSSSF, ogol (sem jogos "
              "peruanos), Wikipédias em espanhol e inglês (as tabelas de confrontos em inglês desses anos estão incompletas) e "
              "ESPN (só de 2005 em diante): nenhuma fonte pública traz os jogos. De 1970 em diante entram com a tabela final de "
              "`peruhist.html`.", "",
              "**Edições com jogos incompletos:** 1926 (torneio suspenso; a Wikipédia tem parte dos jogos), 1982, 1984, 1986, "
              "1988-1991 (anos de Torneo Regional + Descentralizado: a RSSSF tem só as tabelas de parte das fases) e 2003 (as "
              "rodadas 16 e 17 do Clausura, jogadas com sub-20 durante a greve, foram anuladas). O que falta está na observação "
              "da edição.", "",
              "**Fora do pacote:** a Copa Perú, a Segunda División e a Intermedia, as ligas de reservas (que davam pontos de "
              "bônus de 1931 a 1934), o Torneo del Inca, a Copa Bicentenario, a Supercopa, as liguillas pré-Libertadores e "
              "pré-Sudamericana e os jogos de promoção contra clubes de baixo.", "",
              "**Fontes:** RSSSF (uma página por temporada e a lista de tabelas finais `peruhist.html`, em "
              "`data/coleta/per-1/rsssf/`: base de jogos de 1930-1942, 1968, 1969, 1975, 1978, 1980, 1981, 1983, 1984 e 1986 "
              "em diante, com fases, grupos, rodadas, datas e autores dos gols); Wikipédia em espanhol (jogos de 1926-1929, "
              "1943-1967, 1982 e 1985, quase sempre em tabela de confrontos, sem rodada nem data; em `data/coleta/per-1/wikipedia/`); "
              "ESPN (liga `per.1`, 2005 em diante: hora, estádio, público, gols com minuto e cartões); Wikipédia em inglês "
              "(lista de campeões, segunda fonte do campeão e vice de 1912-1921). O ogol não tem jogos peruanos.", "",
              "**Clubes:** nome pelo qual o clube é conhecido no Brasil (Universitario, Melgar, César Vallejo, Binacional, UTC, "
              "CNI, ADT). Homônimos de outros países levam a cidade: Libertad de Trujillo, Internazionale de San Borja. O mesmo "
              "clube com outro nome fica com o atual: Federación Universitaria (até 1930) = Universitario; Sport Alianza = Alianza "
              "Lima; Sucre FBC = Mariscal Sucre; Inti Gas = Ayacucho; Total Clean = Total Chalaco; Real Garcilaso = Cusco FC; "
              "Colegio San Agustín = Deportivo "
              "San Agustín; Grau-Estudiantes (2004) = Estudiantes de Medicina. Aurich-Cañaña (fusão de 1994 a 1996) é clube à "
              "parte do Juan Aurich.", "",
              "**Regras:** o placar é o da fonte de base (RSSSF ou Wikipédia). Jogo decidido no tribunal leva o placar dado "
              "(`awd`), com o de campo na observação. Autores dos gols só entram quando a soma bate com o placar (senão ficam em "
              "`gols_texto`). Com a ESPN, os gols levam o minuto. Pontos: 2 por vitória até 1994 e 3 a partir de 1995; de 1931 "
              "a 1942 a vitória valia 3, o empate 2 e a derrota 1 (o `ajuste_pontos` desses anos parte dessa conta; de 1931 a "
              "1934 a tabela soma ainda os pontos de bônus da liga de reservas).", "",
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
    from campeoes_wiki import campeoes as campeoes_wiki, vices
    VICES.update(vices())
    WIKI.update(campeoes_wiki())
    TOPS.update(artilheiros_rsssf())
    eds = []
    for e in EDICOES:
        d = montar(e, cps)
        eds.append(d)
        print(f"{e.temporada:20s} {len(d['p']['jogos']):4d} jogos  campeão {d['campeao']}  divergências {len(d['difs'])}", flush=True)
    gravar(eds)
    relatorio(eds)
    print("pacote gravado em", PACOTE, "e relatório em", RELATORIO)
