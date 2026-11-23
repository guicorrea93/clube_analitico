"""Junta as fontes da 1ª divisão uruguaia e grava o pacote em data/coleta/uru-1/pacote/ e o relatório em docs/coleta/uru-1.md.

Fontes, na ordem em que entram:
- RSSSF (ler_rsssf.py): base de jogos, fases, grupos, rodadas, datas, local e autores dos gols (1932-1959, 1965 e 1994 em
  diante). As tabelas publicadas na página da temporada e a lista de tabelas finais (uruhist.html, 1900-2000) são a
  conferência; nas edições sem jogos, a tabela final é a classificação.
- Wikipédia em espanhol (wikipedia_jogos.py): jogos de 1900, 1901, 1905, 1908, 1916, 1960-1964 e 1966-1974.
- ogol (ogol.py): rodada e data dos jogos que ele tem (2005/06 em diante) e o nome de cada clube no ogol.
- ESPN (liga uru.1, 2005 em diante): hora, estádio, público e, de 2005 a 2013, gols com minuto e cartões.

Uso: python coleta/uru-1/importar.py
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
from clubes_uru import CLUBES, clube  # noqa: E402
from conferir import conferir_tabelas, eh_mata, preparar, soma  # noqa: E402
from edicoes import EDICOES, PACOTE, RELATORIO, SLUG, Edicao  # noqa: E402
from explicacoes import CORRIGE, EXPLICACOES, EXTRAS  # noqa: E402
from ler_rsssf import campeoes  # noqa: E402
from rsssf_sul import chave  # noqa: E402

# ordem das fases (quanto maior, mais longe o clube chegou); os torneios do ano (Apertura, Intermedio, Clausura) e as finais
# de cada um ficam no nível 0: decidem vaga nas finais do campeonato, não o título
NIVEL_FASE = {"": 0, "Grupo do rebaixamento": 0, "Desempate do rebaixamento": 0, "Desempate do 2º lugar": 1,
              "Desempate da tabela anual": 1, "Fase final": 2, "Semifinal": 5, "Final": 6, "Desempate do título": 6}
WIKI: dict[str, str] = {}
TOPS: dict[str, list] = {}
TOPS_FONTE: dict[str, str] = {}
# UY-019: grafias da urutops corrigidas pela es e outras fontes
GRAFIAS = {"Antonio Cataldo": "Antonio Castaldo", "Juan C. Mameli": "Juan Mamelli", "Pedro Cardozo": "Pedro Cardoso"}
# UY-017 e QU-008: artilharia oficial da AUF ("Goleadores de la Temporada", auf.org.uy/historico-temporadas), 2013/14-2025
ARTILHEIROS_AUF: dict[str, list[tuple[str, str, int]]] = {
    "2013/14": [("Héctor Acuña", "Cerro", 20)], "2014/15": [("Iván Alonso", "Nacional", 23)],
    "2015/16": [("Gastón Rodríguez", "Montevideo Wanderers", 19), ("Junior Arias", "Liverpool", 19)],
    "2017": [("Maureen Franco", "Cerro", 25)], "2018": [("Gonzalo Bergessio", "Nacional", 17)],
    "2019": [("Juan Ignacio Ramírez", "Liverpool", 24)], "2020": [("Gonzalo Bergessio", "Nacional", 25)],
    "2021": [("Maximiliano Silvera", "Cerrito", 21)], "2022": [("Thiago Borbas", "River Plate", 18)],
    "2023": [("Juan Ignacio Ramírez", "Nacional", 18)], "2024": [("Leonardo Fernández", "Peñarol", 16)],
    "2025": [("Abel Hernández", "Liverpool", 25)],
}


def nome_fase(f: str, fases: set[str]) -> str:
    if f:
        return f
    return "Primeira fase" if fases - {""} else "Fase única"


def id_edicao(e: Edicao) -> str:
    return re.sub(r"[^0-9a-z]+", "-", chave(e.temporada))


def especial(esp: str) -> str:
    return {"wo_m": "wo", "wo_v": "wo", "awd": "awd", "abd": "abd", "anulado": "n/p", "n/p": "n/p"}.get(esp, "")


# D-09 (a): títulos que a AUF não reconhece: a edição fica, sem campeão, com nota (UY-001)
SEM_TITULO = {"1923 FUF", "1924 FUF", "1926"}
# D-22 (c): 1947 sem vice, o triangular pelo 2º lugar não terminou (UY-008); 1948 sem campeão, sem vice (UY-003)
SEM_VICE = {"1947", "1948"}
TABELA_OFICIAL = {"1951"}   # UY-011: a tabela publicada (RSSSF e es) não fecha com nenhum jogo do banco


def acerta_ano(e: Edicao, jogos: list[dict]) -> None:
    """UY-015: em 2020 a 1ª data (Feb 15) é <= junho numa edição com ano_fim 2021, e o leitor comum leva o Apertura e o
    Intermedio para 2021. Janela da temporada a partir do 1º jogo da página (mesma regra do AR-022 do arg-1)."""
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
    # campeão pela lista da RSSSF (uruchamp.html)
    camp_txt = "" if e.temporada in SEM_TITULO else (e.campeao_rsssf or cps.get(e.temporada, ""))
    campeao = clube(camp_txt, e.ano_inicio) if camp_txt else None
    if not campeao and camp_txt:
        log.append(f"campeão da lista da RSSSF não reconhecido: {camp_txt}")
    final = classificacao(e, p, calc, nivel, campeao, clubes)
    podio_oficial(e, final, campeao, log)
    return {"e": e, "p": p, "difs": difs, "log": log, "clubes": clubes, "campeao": campeao, "camp_txt": camp_txt,
            "final": final, "fases": fases}


def artilheiros_rsssf() -> dict[str, list[tuple[str, str, int]]]:
    """urutops.html: temporada -> [(jogador, clube como na página, gols)], de 1932 a 2007/08. Empate na artilharia vem em
    linhas seguidas, com os gols só na última. A lista de artilheiros da liguilla (mais abaixo) fica de fora."""
    from ler_rsssf import linhas
    saida: dict[str, list] = defaultdict(list)
    ano, pendentes = None, []
    for l in linhas("urutops"):
        if l.startswith("[*]") or "Liguilla" in l:
            break
        m = re.match(r"^(\d{4}(?:/\d{2})?)?\s+([A-ZÀ-Ý][A-ZÀ-Ý .'-]+?)(?:\s*\[\*\])?\s{2,}(\S.*?)(?:\s+(\d{1,2}))?\s*$", l)
        if not m:
            continue
        if m.group(1):
            ano, pendentes = ("2020" if m.group(1) == "2020/21" else m.group(1)), []
        if not ano:
            continue
        pendentes.append((m.group(2).strip().title(), m.group(3).strip()))
        if m.group(4):
            saida[ano] += [(jog, c, int(m.group(4))) for jog, c in pendentes]
            pendentes = []
    return saida


def classificacao(e: Edicao, p: dict, calc: dict, nivel: dict, campeao: str | None, clubes: list[str]) -> list[dict]:
    """Classificação final: a tabela publicada que traz todos os clubes e fecha com os jogos (ordem oficial, pontos com
    punições); sem ela, calculada (fase alcançada, pontos, saldo, gols pró). O campeão da lista oficial fica em 1º."""
    pv = e.pontos_vitoria
    pub = next((tb for tb in p["tabelas"] if not tb.get("acumulada") and tb.get("ok") and
                {r["clube"] for r in tb["linhas"]} == set(clubes)), None)
    if e.ano_inicio >= 1994 and not e.sem_jogos or e.temporada in TABELA_OFICIAL:
        # UY-006: de 1994 em diante a classificação é a tabela anual (acumulada), não a do Apertura; UY-011: 1951 pela
        # tabela publicada. Entre as tabelas com todos os clubes, a de mais jogos
        cands = [tb for tb in p["tabelas"] if {r["clube"] for r in tb["linhas"]} >= set(clubes) - {None}
                 and all(r["j"] is not None for r in tb["linhas"])]
        pub = max(cands, key=lambda tb: sum(r["j"] for r in tb["linhas"]), default=pub)
    if e.sem_jogos:   # sem jogos: a tabela final da RSSSF (uruhist.html) é a classificação
        pub = next((tb for tb in p["tabelas"] if tb.get("sem_conferencia")), None)
    linhas = []
    if pub:
        for k, r in enumerate(pub["linhas"], 1):
            pts_calc = r["v"] * pv + r["e"]
            linhas.append({"clube": r["clube"], "j": r["j"], "v": r["v"], "e": r["e"], "d": r["d"], "gp": r["gp"], "gc": r["gc"],
                           "pts": r["pts"], "ajuste": r["pts"] - pts_calc,
                           "obs": r.get("obs", ""), "fonte": f"RSSSF ({pub['fonte']})"})
        # a ordem publicada vale; empates sem número herdam a posição de cima
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
    # UY-004: vice = o adversário do campeão na final do ano (fase "Final"; a Supercopa saiu, UY-013); sem final, fica o 2º
    # da tabela anual (D-22 d). O 3º é o seguinte da tabela anual (UY-005)
    adv = [j["v"] if j["m"] == campeao else j["m"] for j in p["jogos"] if j["fase"] == "Final" and campeao in (j["m"], j["v"])]
    if campeao and adv and len(set(adv)) == 1 and any(r["clube"] == adv[0] for r in linhas) and linhas[1]["clube"] != adv[0]:
        v = next(r for r in linhas if r["clube"] == adv[0])
        linhas.remove(v)
        linhas.insert(1, v)
    for k, r in enumerate(linhas, 1):
        r["pos"] = k
    return linhas


def situacao(r: dict, campeao: str | None, k: int, temporada: str = "") -> str:
    if r["clube"] == campeao:
        return "campeao"
    if k == 2 and campeao and temporada not in SEM_VICE:   # UY-003: edição sem campeão não tem vice; UY-008: 1947
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
        "slug": SLUG, "nome": "Campeonato Uruguaio", "nome_curto": "Uruguaio", "tipo": "liga", "nivel": 1, "pais": "URU",
        "pais_nome": "Uruguai", "regiao": None, "confederacao": "CONMEBOL", "rotulo_painel": "Uruguaio",
        "menu_painel": "Uruguai · 1ª divisão", "do_painel": "do Campeonato Uruguaio", "o_painel": "o Campeonato Uruguaio",
        "observacao": "1ª divisão uruguaia de 1900 a 2025: uma edição por título (AUF e FUF em 1923 e 1924; Torneo del Consejo "
                      "Provisorio em 1926; temporadas no calendário europeu de 2005/06 a 2015/16). Apertura, Intermedio e Clausura "
                      "são fases da edição. Jogos de 1900, 1901, 1905, 1908, 1916, 1932-1974 e 1994 em diante; nos outros anos, "
                      "só a tabela final e o campeão (nenhuma fonte pública tem os jogos)."},
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
            da_wiki = bool(x) and x.texto.startswith("wiki")
            fonte_id = (f"wikipedia:{x.texto[5:]}" if da_wiki else f"rsssf:{x.texto}") if x else ex["fonte_id"]
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
                                  "Wikipédia (es)" if da_wiki else "RSSSF", fonte_id,
                                  "" if sep or not texto_autores or not autores.eh_autores(texto_autores) else texto_autores,
                                  "; ".join(o for o in obs if o)])
        # classificação final
        for r in d["final"]:
            L["classificacao_final"].append([e.temporada, r["pos"], r["clube"], r["j"], r["v"], r["e"], r["d"], r["gp"], r["gc"],
                                             r["pts"], r["ajuste"], situacao(r, d["campeao"], r["pos"], e.temporada), r["fonte"],
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
                L["tabelas_publicadas"].append([e.temporada, nome_fase(tb["t"].fase, fases) if tb["fonte"].startswith("uru") and
                                                not tb["fonte"].startswith("uruhist") else "classificação final",
                                                tb["t"].grupo, r["pos"], r["nome"], r["clube"], r["j"], r["v"], r["e"], r["d"], r["gp"],
                                                r["gc"], r["pts"], f"RSSSF ({tb['fonte']}, linha {tb['t'].linha})"])
        # artilheiros: lista da RSSSF; sem ela, a contagem dos gols com autor (quando quase todos os gols têm autor)
        tops = TOPS.get(e.temporada)
        if tops:
            for jog, ctxt, ng in tops:
                L["artilheiros"].append([e.temporada, GRAFIAS.get(jog, jog), clube(ctxt, e.ano_inicio) or ctxt, ng,
                                         TOPS_FONTE.get(e.temporada, "RSSSF (urutops.html)")])
        elif gols_ed and autor_ed >= 0.95 * gols_ed:
            cont = Counter((r[2], r[1]) for r in L["gols"] if r[0].startswith(eid + "-") and r[5] != "contra")
            if cont:
                topo = max(cont.values())
                for (jog, c), ng in sorted(cont.items()):
                    if ng == topo:
                        L["artilheiros"].append([e.temporada, jog, c, ng, "contagem dos gols com autor"])
        # edição
        final = d["final"]
        vice = final[1]["clube"] if len(final) > 1 and d["campeao"] and e.temporada not in SEM_VICE else ""
        L["edicoes"].append([e.temporada, e.ano_inicio, e.ano_fim, e.nome_oficial, len(d["clubes"]), e.pontos_vitoria,
                             ("sem jogos (só a tabela final)" if e.sem_jogos else
                              formato(ordem_f, L["fases"], e.temporada)), d["campeao"] or "", vice,
                             "; ".join(["RSSSF"] + (["Wikipédia (es)"] if e.wiki is not None else []) +
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
        L["clubes"].append([c, prov, cid, "URU", "|".join(partes)])
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
            fase = tb["t"].fase if tb["fonte"].startswith("uru") and not tb["fonte"].startswith("uruhist") else ""
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
    linhas = ["# Campeonato Uruguaio (1ª divisão) — coleta de dados", "",
              "Gerado por `python coleta/uru-1/importar.py`. Pacote em `data/coleta/uru-1/pacote/`.", "",
              f"**Edições:** {n_ed}, uma por título de campeão uruguaio da 1ª divisão, de 1900 a 2025, como na lista de campeões "
              "da RSSSF (`uruchamp.html`). Os cismas de 1923 e 1924 dão duas edições cada (\"1923 AUF\" e \"1923 FUF\"), como a "
              "RSSSF conta; 1926 é o Torneo del Consejo Provisorio. Sem edição: 1904 e 1930 (não houve campeonato) e 1925 (AUF e FUF "
              "não terminaram). 1948 entra sem campeão (abandonado na greve dos jogadores). De 2005/06 a 2015/16 as temporadas "
              "seguem o calendário europeu; \"2005\" é o Torneo Uruguay Especial e \"2016\" a Transición. Apertura, Intermedio e "
              "Clausura não davam título de campeão uruguaio: são fases da edição, com as finais de cada um, a tabela anual e as "
              "finais do campeonato.", "",
              f"**Edições sem jogos ({n_sem}):** 1902-1903, 1906-1907, 1909-1915, 1917-1931 (com AUF e FUF) e 1975-1993. Nenhuma "
              "fonte pública que achamos tem os jogos desses anos (RSSSF, ogol e Wikipédias em espanhol e inglês trazem só a tabela "
              "final; para 1975-1993 a RSSSF tem só a liguilla pré-Libertadores). Elas entram com a tabela final da RSSSF "
              "(`uruhist.html`) como classificação e o campeão, sem jogos.", "",
              "**Fora do pacote:** as liguillas pré-Libertadores, o Torneo Integración (1994), o Torneo Nacional (1996), a Copa "
              "Artigas, o Torneo Permanencia (2001-2002), o Reclasificatorio (2004), a Copa AUF Uruguay, a Supercopa e os jogos "
              "de promoção contra clubes da 2ª divisão.", "",
              "**Fontes:** RSSSF (uma página por temporada, `data/coleta/uru-1/rsssf/`: base de jogos de 1932-1959, 1965 e 1994 em "
              "diante, com fases, grupos, rodadas, datas e autores dos gols; as tabelas da própria página e a lista de tabelas "
              "finais `uruhist.html`, de 1900 a 2000, são a conferência); Wikipédia em espanhol (páginas \"Campeonato Uruguayo de "
              "Primera División <ano>\": jogos de 1900, 1901, 1905, 1908, 1916, 1960-1964 e 1966-1974, por rodada, sem autores; "
              "em 1969 no lugar da RSSSF, que tem só 18 das 20 rodadas); ogol (calendários de 2005/06 em diante: rodada e data "
              "que faltam, conferência de placar e o nome de cada clube no ogol); ESPN (liga `uru.1`, 2005 em diante: hora, "
              "estádio e público; gols com minuto e cartões de 2005 a 2013); Wikipédia em inglês (lista de campeões da AUF, "
              "segunda fonte do campeão; não traz a FUF nem 1926).", "",
              "**Clubes:** C.U.R.C.C. (1900-1913) entra como Peñarol, como a RSSSF e a Wikipédia contam (a seção de futebol do "
              "C.U.R.C.C. virou o Peñarol; o Nacional contesta). Defensor e Defensor Sporting são um clube só; Miramar, Misiones e "
              "Miramar Misiones (fusão de 1980) ficam separados; o River Plate amador (River Plate FC, até 1929) não é o atual "
              "(River Plate de Montevideo, de 1932). Homônimos de clubes do banco levam a cidade (Liverpool de Montevideo, Racing "
              "de Montevideo, River Plate de Montevideo...).", "",
              "**Regras:** o placar é o da RSSSF (ou da Wikipédia, nos anos dela); o ogol só completa rodada e data e entra como "
              "conferência. Jogo decidido no tribunal leva o placar dado (`awd`) ou, quando o tribunal só deu a vitória "
              "(\"awarded win to X; goal records unchanged\"), fica sem placar como `awd`, com o placar de campo na observação "
              "(a tabela conta a vitória com os gols de campo). Autores dos gols só entram quando a soma bate com o placar (senão "
              "ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos por vitória: 2 até 1994 e 3 a partir de 1995.", "",
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
    from campeoes_wiki import terceiros, vices
    VICES.update(vices())
    TERCEIROS.update(terceiros())
    TOPS.update(artilheiros_rsssf())
    from goleadores_es import goleadores   # UY-018: 1900-1931, coluna "Goleador" da Wikipédia em espanhol
    for t_, v_ in goleadores().items():
        if t_ not in TOPS:
            TOPS[t_], TOPS_FONTE[t_] = v_, "Wikipédia em espanhol (Títulos de liga por año, coluna Goleador)"
    for t_, v_ in ARTILHEIROS_AUF.items():
        TOPS[t_], TOPS_FONTE[t_] = v_, "AUF (Goleadores de la Temporada)"
    eds = []
    for e in EDICOES:
        d = montar(e, cps)
        eds.append(d)
        print(f"{e.temporada:20s} {len(d['p']['jogos']):4d} jogos  campeão {d['campeao']}  divergências {len(d['difs'])}", flush=True)
    gravar(eds)
    relatorio(eds)
    print("pacote gravado em", PACOTE, "e relatório em", RELATORIO)
