"""Junta as fontes da 1ª divisão chilena e grava o pacote em data/coleta/chi-1/pacote/ e o relatório em docs/coleta/chi-1.md.

Fontes, na ordem em que entram:
- RSSSF (ler_rsssf.py): base de jogos, fases, grupos, rodadas, datas e autores dos gols (1933-1983 e 1996-2024). As tabelas
  publicadas na página da temporada e a lista de tabelas finais (chilehist.html, 1933-1996) são a conferência.
- ogol: base dos jogos de 1984 a 1995 e de 2025, quando a RSSSF só tem a tabela final; nos outros anos, rodada e data que
  faltam, conferência de placar e o nome de cada clube no ogol.
- ESPN (liga chi.1, 2001 em diante): base da fase de pontos corridos do Clausura 2011 e de 2012; hora, estádio, público,
  gols com minuto e cartões.

Uso: python coleta/chi-1/importar.py
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
from clubes_chi import CLUBES, clube  # noqa: E402
from conferir import conferir_tabelas, eh_mata, preparar, soma  # noqa: E402
from edicoes import EDICOES, PACOTE, RELATORIO, SLUG, Edicao  # noqa: E402
from explicacoes import CORRIGE, EXPLICACOES, EXTRAS  # noqa: E402
from ler_rsssf import campeoes  # noqa: E402
from rsssf_sul import chave  # noqa: E402

# ordem das fases (quanto maior, mais longe o clube chegou); os torneios do ano (Apertura, Intermedio, Clausura) e as finais
# de cada um ficam no nível 0: decidem vaga nas finais do campeonato, não o título
NIVEL_FASE = {"": 0, "Grupo do rebaixamento": 0, "Desempate do rebaixamento": 0, "Desempate do 2º lugar": 1, "Segunda fase": 1,
              "Terceira fase": 1, "Nacional": 2, "Oitavas de final": 3, "Quartas de final": 4,
              "Desempate da tabela anual": 1, "Fase final": 2, "Semifinal": 5, "Final": 6, "Desempate do título": 6}
WIKI: dict[str, str] = {}
TOPS: dict[str, list] = {}


def nome_fase(f: str, fases: set[str]) -> str:
    if f:
        return f
    return "Primeira fase" if fases - {""} else "Fase única"


def id_edicao(e: Edicao) -> str:
    return re.sub(r"[^0-9a-z]+", "-", chave(e.temporada))


def especial(esp: str) -> str:
    return {"wo_m": "wo", "wo_v": "wo", "awd": "awd", "abd": "abd", "anulado": "n/p", "n/p": "n/p"}.get(esp, "")


def acerta_ano(e: Edicao, jogos: list[dict]) -> None:
    """CH-011: em 2020 a 1ª data (Jan 24) é <= junho numa edição com ano_fim 2021, e o leitor comum leva a temporada inteira
    um ano para a frente. Janela da temporada a partir do 1º jogo da página (mesma regra do AR-022 do arg-1 e do UY-015 do uru-1)."""
    from datetime import date, timedelta
    if e.temporada != "2020":
        return
    da_pagina = [j for j in jogos if j["j"] and j["j"].data and not j["j"].texto.startswith(("espn", "wiki", "ogol"))]
    da_pagina.sort(key=lambda j: int(j["j"].texto.split(":")[1]))
    if not da_pagina:
        return
    d0 = da_pagina[0]["j"].data
    ini = date(e.ano_inicio, int(d0[5:7]), int(d0[8:10])) - timedelta(days=30)
    fim = ini + timedelta(days=500)
    prev = None
    for j in da_pagina:
        x = j["j"]
        mo, di = int(x.data[5:7]), int(x.data[8:10])
        cands = [w for y in range(ini.year, fim.year + 1) for w in [_dia(y, mo, di)] if w and ini <= w <= fim]
        if not cands:
            continue
        z = cands[0] if len(cands) == 1 or prev is None else min(cands, key=lambda w: abs((w - prev).days))
        prev = z
        x.data = z.isoformat() + x.data[10:]


def _dia(y: int, mo: int, di: int):
    from datetime import date
    try:
        return date(y, mo, di)
    except ValueError:
        return None


VICES: dict[str, str] = {}
TERCEIROS: dict[str, str] = {}


def podio_oficial(e: Edicao, final: list[dict], campeao: str | None, log: list[str]) -> None:
    """Vice e 3º da lista da AUF (Wikipédia em inglês, colunas Runner-up e Third place) logo abaixo do campeão (UY-004,
    UY-005). 1947 fica sem vice (D-22 c)."""
    if not campeao or e.temporada in SEM_VICE:
        return
    for pos, lista in ((2, VICES), (3, TERCEIROS)):
        txt = lista.get(e.temporada)
        c = clube(txt, e.ano_inicio) if txt else None
        r = next((r for r in final if r["clube"] == c), None) if c else None
        if r is None or len(final) < pos:
            continue
        if final.index(r) > pos - 1:
            log.append(f"{'vice' if pos == 2 else '3º'} pela lista oficial: {c} (a tabela o punha em {final.index(r) + 1}º)")
            final.remove(r)
            final.insert(pos - 1, r)
    for k, r in enumerate(final, 1):
        r["pos"] = k


def montar(e: Edicao, cps: dict[str, str]) -> dict:
    p = preparar(e)
    acerta_ano(e, p["jogos"])
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
    # campeão pela lista da RSSSF (chilechamp.html)
    camp_txt = e.campeao_rsssf or cps.get(e.temporada, "")
    campeao = clube(camp_txt, e.ano_inicio) if camp_txt else None
    if not campeao and camp_txt:
        log.append(f"campeão da lista da RSSSF não reconhecido: {camp_txt}")
    final = classificacao(e, p, calc, nivel, campeao, clubes)
    return {"e": e, "p": p, "difs": difs, "log": log, "clubes": clubes, "campeao": campeao, "camp_txt": camp_txt,
            "final": final, "fases": fases}


def artilheiros_rsssf() -> dict[str, list[tuple[str, str, int]]]:
    """chiletops.html: temporada -> [(jogador, clube como na página, gols)], de 1933 a 2010. "Ap"/"Cl" ao lado do ano é o
    Apertura ou o Clausura; empate na artilharia vem em linhas seguidas, cada uma com os gols."""
    from ler_rsssf import linhas
    saida: dict[str, list] = defaultdict(list)
    ano = temp = None
    for l in linhas("chiletops"):
        # ("Ap"/"Cl" só como palavra: "Apolonides VERA", 1947, virava "1947 Apertura"; CH-018)
        m = re.match(r"^(\d{4})?\s+(?:(Ap|Cl)\s+)?(\S.*?)\s{2,}(\S.*?)\s{2,}(\S.*?)\s+(\d{1,2})\s*$", l)
        if not m:
            continue
        if m.group(1):
            ano = m.group(1)
        if not ano:
            continue
        if m.group(2):
            temp = f"{ano} {'Apertura' if m.group(2) == 'Ap' else 'Clausura'}"
        elif m.group(1):
            temp = ano
        # sem ano nem "Ap"/"Cl": empate com a linha de cima (mesma temporada)
        jog = " ".join(p.capitalize() if p.isupper() and len(p) > 1 else p for p in m.group(3).split())
        saida[temp].append((jog, m.group(5).strip(), int(m.group(6))))
    return saida


def classificacao(e: Edicao, p: dict, calc: dict, nivel: dict, campeao: str | None, clubes: list[str]) -> list[dict]:
    """Classificação final: a tabela publicada que traz todos os clubes e fecha com os jogos (ordem oficial, pontos com
    punições); sem ela, calculada (fase alcançada, pontos, saldo, gols pró). O campeão da lista oficial fica em 1º."""
    pv = e.pontos_vitoria
    pub = next((tb for tb in p["tabelas"] if not tb.get("acumulada") and tb.get("ok") and
                {r["clube"] for r in tb["linhas"]} == set(clubes)), None)
    if e.temporada in TABELAS_CLASS:   # a tabela publicada (ou duas emendadas) vale mesmo sem fechar com os jogos
        por_id = {f"{tb['fonte']}:{tb['t'].linha}": tb for tb in p["tabelas"]}
        partes = [por_id[k] for k in TABELAS_CLASS[e.temporada] if k in por_id]
        if partes:
            vistos = set()
            pub = {**partes[0], "fonte": "+".join(f"{x['fonte']}:{x['t'].linha}" for x in partes),
                   "linhas": [r for x in partes for r in x["linhas"] if not (r["clube"] in vistos or vistos.add(r["clube"]))]}
    if e.sem_jogos:   # sem jogos: a tabela final da RSSSF é a classificação
        pub = next((tb for tb in p["tabelas"] if tb.get("sem_conferencia")), None)
    linhas = []
    if pub:
        for k, r in enumerate(pub["linhas"], 1):
            pts_calc = r["v"] * pv + r["e"]
            linhas.append({"clube": r["clube"], "j": r["j"], "v": r["v"], "e": r["e"], "d": r["d"], "gp": r["gp"], "gc": r["gc"],
                           "pts": r["pts"], "ajuste": r["pts"] - pts_calc,
                           "obs": r.get("obs", ""), "fonte": f"RSSSF ({pub['fonte']})"})
        # a ordem publicada vale; empates sem número herdam a posição de cima
        for c in sorted(set(clubes) - {r["clube"] for r in linhas},   # clubes de outras fases (1968: fora do Nacional)
                        key=lambda c: (-nivel[c], -(calc.get(c, [0] * 6)[1] * pv + calc.get(c, [0] * 6)[2]), c)):
            x = calc.get(c, [0] * 6)
            linhas.append({"clube": c, "j": x[0], "v": x[1], "e": x[2], "d": x[3], "gp": x[4], "gc": x[5], "pts": x[1] * pv + x[2],
                           "ajuste": 0, "obs": "", "fonte": "calculada (fora da tabela publicada usada)"})
    else:
        for c in clubes:
            x = calc.get(c, [0] * 6)
            linhas.append({"clube": c, "j": x[0], "v": x[1], "e": x[2], "d": x[3], "gp": x[4], "gc": x[5], "pts": x[1] * pv + x[2],
                           "ajuste": 0, "obs": "", "fonte": "calculada (fase alcançada, pontos, saldo, gols pró)"})
        linhas.sort(key=lambda r: (-nivel[r["clube"]], -r["pts"], -(r["gp"] - r["gc"]), -r["gp"], r["clube"]))
    if campeao and linhas and linhas[0]["clube"] != campeao and any(r["clube"] == campeao for r in linhas):
        c = next(r for r in linhas if r["clube"] == campeao)
        linhas.remove(c)
        linhas.insert(0, c)
    if not e.sem_jogos:   # CH-025: clube da tabela sem jogo na edição (2008 Clausura, Deportes Concepção) fica de fora
        linhas = [r for r in linhas if r["j"] or r["clube"] == campeao]
    # vice da lista oficial (Wikipédia em inglês) logo abaixo do campeão (CH-002 a CH-008)
    vice = clube(VICES[e.temporada], e.ano_inicio) if VICES.get(e.temporada) and campeao else None
    if vice and len(linhas) > 2 and linhas[1]["clube"] != vice and any(r["clube"] == vice for r in linhas[2:]):
        v = next(r for r in linhas if r["clube"] == vice)
        linhas.remove(v)
        linhas.insert(1, v)
    for k, r in enumerate(linhas, 1):
        r["pos"] = k
    return linhas


VICES: dict[str, str] = {}
# CH-001, CH-003, CH-004, CH-005, CH-007, CH-009, CH-015, CH-016, CH-019: a classificação é a tabela publicada (bônus,
# punições, desempates fora da liga, jogos que a página não fecha); 1954 e 1955: tabela acumulada do grupo final (1º-8º)
# e do grupo do rebaixamento (9º-14º); 1968: a do Nacional (os clubes de fora vêm depois)
TABELAS_CLASS = {
    "1947": ["chile47:40"], "1954": ["chile54:356", "chile54:412"], "1955": ["chile55:356", "chile55:412"],
    "1968": ["chile68:505"], "1971": ["chile71:16"], "1977": ["chile77:16"], "1979": ["chile79:220"], "1981": ["chile81:240"],
    "1982": ["chile82:255"], "1983": ["chile83:515"], "1985": ["chilehist:1348"], "1990": ["chilehist:1476"],
    "1997 Apertura": ["chile97:20"], "2011 Apertura": ["chile2011:34"],
}


def situacao(r: dict, campeao: str | None, k: int) -> str:
    if r["clube"] == campeao:
        return "campeao"
    if k == 2:
        return "vice"
    if re.search(r"\brelegated\b|descend|rebaix", r.get("obs", ""), re.I):   # CH-010: "Relegation group/playoff" não é queda
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
        "slug": SLUG, "nome": "Campeonato Chileno", "nome_curto": "Chileno", "tipo": "liga", "nivel": 1, "pais": "CHI",
        "pais_nome": "Chile", "regiao": None, "confederacao": "CONMEBOL", "rotulo_painel": "Chileno",
        "menu_painel": "Chile · 1ª divisão", "do_painel": "do Campeonato Chileno", "o_painel": "o Campeonato Chileno",
        "observacao": "1ª divisão chilena de 1933 a 2025: uma edição por torneio que deu título de campeão (Apertura e Clausura "
                      "em 1997, 2002-2009, 2011, 2012 e 2013/14-2016/17; Transición em 2013 e 2017; \"2020\" é a temporada "
                      "2020/21). Sem a Copa Chile, as liguillas e os jogos de promoção."},
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
                pref = x.texto.split(":")[0] if x.texto.startswith(("ogol:", "espn:")) else "rsssf"
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
            base = (x.texto.split(":")[0] if x.texto.startswith(("ogol:", "espn:")) else "rsssf") if x else "rsssf"
            fonte_id = (x.texto if base != "rsssf" else f"rsssf:{x.texto}") if x else ex["fonte_id"]
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
                cidade = "La Serena" if cidade == "Estadio La Portada" else cidade   # CH-024: a ESPN põe o estádio no lugar da cidade
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
                                  {"ogol": "ogol", "espn": "ESPN"}.get(base, "RSSSF"), fonte_id,
                                  "" if sep or not texto_autores or not autores.eh_autores(texto_autores) else texto_autores,
                                  "; ".join(o for o in obs if o)])
        # classificação final
        for r in d["final"]:
            L["classificacao_final"].append([e.temporada, r["pos"], r["clube"], r["j"], r["v"], r["e"], r["d"], r["gp"], r["gc"],
                                             r["pts"], r["ajuste"], situacao(r, d["campeao"], r["pos"]), r["fonte"],
                                             "punição/bônus de pontos (tabela publicada)" if r["ajuste"] else ""])
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
                L["tabelas_publicadas"].append([e.temporada, nome_fase(tb["t"].fase, fases) if tb["fonte"].startswith("chile") and
                                                not tb["fonte"].startswith("chilehist") else "classificação final",
                                                tb["t"].grupo, r["pos"], r["nome"], r["clube"], r["j"], r["v"], r["e"], r["d"], r["gp"],
                                                r["gc"], r["pts"], f"RSSSF ({tb['fonte']}, linha {tb['t'].linha})"])
        # artilheiros: lista da RSSSF; sem ela, a contagem dos gols com autor (quando quase todos os gols têm autor)
        tops = TOPS.get(e.temporada)
        if tops:
            for jog, ctxt, ng in tops:
                L["artilheiros"].append([e.temporada, jog, clube(ctxt, e.ano_inicio) or ctxt, ng, "RSSSF (chiletops.html)"])
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
                             "; ".join((["RSSSF"] if e.trechos or e.tabelas else []) +
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
        L["clubes"].append([c, prov, cid, "CHI", "|".join(partes)])
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
            fase = tb["t"].fase if tb["fonte"].startswith("chile") and not tb["fonte"].startswith("chilehist") else ""
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
    n_ed = len(eds)
    linhas = ["# Campeonato Chileno (1ª divisão) — coleta de dados", "",
              "Gerado por `python coleta/chi-1/importar.py`. Pacote em `data/coleta/chi-1/pacote/`.", "",
              f"**Edições:** {n_ed}, uma por torneio que deu título de campeão chileno da 1ª divisão, de 1933 a 2025, como na lista "
              "de campeões da RSSSF (`chilechamp.html`) e na Wikipédia em inglês (as duas trazem os mesmos campeões). Apertura e "
              "Clausura deram título cada um em 1997, de 2002 a 2009, em 2011, 2012 e de 2013/14 a 2016/17: uma edição por "
              "torneio, como no arg-1; os torneios de Transición de 2013 e 2017 também. \"2020\" é a temporada 2020/21 "
              "(pandemia); 2019 foi encerrado na 24ª rodada pelos protestos de outubro.", "",
              "**Fora do pacote:** a Copa Chile (e as copas de começo e de fim de ano dos anos 1930-1980, \"Campeonato de "
              "Apertura\" e \"Campeonato de Clausura\"), as liguillas pré-Libertadores e pré-Sudamericana e os jogos de "
              "promoção contra clubes da 2ª divisão.", "",
              "**Fontes:** RSSSF (uma página por temporada, `data/coleta/chi-1/rsssf/`: base de jogos de 1933 a 1983 e de 1996 "
              "a 2024, com fases, grupos, rodadas, datas e autores dos gols; as tabelas da própria página e a lista de tabelas "
              "finais `chilehist.html`, de 1933 a 1996, são a conferência); ogol (base dos jogos de 1984 a 1995 e de 2025, anos "
              "em que a RSSSF só traz a tabela final; nos outros anos, rodada e data que faltam, conferência de placar e o nome "
              "de cada clube no ogol); ESPN (liga `chi.1`, 2001 em diante: base da fase de pontos corridos do Clausura 2011 e de "
              "2012, que a RSSSF não traz; hora, estádio, público, gols com minuto e cartões); Wikipédia em inglês (lista de "
              "campeões, segunda fonte do campeão).", "",
              "**Clubes:** Green Cross (Santiago, campeão em 1945), Green Cross-Temuco (1965) e Deportes Temuco (1985) são um clube "
              "só, como a RSSSF conta; Ferroviarios e Badminton (até 1949) e Ferrobádminton (fusão de 1950) ficam separados. "
              "Homônimos de clubes do banco levam a cidade: Everton de Viña del Mar, Rangers de Talca, Naval de Talcahuano, "
              "Metropolitano de Santiago.", "",
              "**Regras:** o placar é o da RSSSF (ou do ogol e da ESPN, nos anos em que são a base); o ogol entra como "
              "conferência nos outros anos. Jogo decidido no tribunal leva o placar dado (`awd`) ou, sem placar, a vitória (`wo`, "
              "com o placar de campo na observação). Autores dos gols só entram quando a soma bate com o placar (senão ficam em "
              "`gols_texto`). Com a ESPN, os gols levam o minuto. Pontos por vitória: 2 até 1994 e 3 a partir de 1995 (várias "
              "temporadas tiveram pontos de bônus, que a tabela publicada mostra; a diferença vai em `ajuste_pontos`).", "",
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
    from campeoes_wiki import campeoes as campeoes_wiki
    WIKI.update(campeoes_wiki())
    from campeoes_wiki import vices
    VICES.update(vices())
    TOPS.update(artilheiros_rsssf())
    eds = []
    for e in EDICOES:
        d = montar(e, cps)
        eds.append(d)
        print(f"{e.temporada:20s} {len(d['p']['jogos']):4d} jogos  campeão {d['campeao']}  divergências {len(d['difs'])}", flush=True)
    gravar(eds)
    relatorio(eds)
    print("pacote gravado em", PACOTE, "e relatório em", RELATORIO)
