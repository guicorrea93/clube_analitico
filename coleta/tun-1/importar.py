"""Junta as fontes da 1ª divisão tunisiana e grava o pacote em data/coleta/tun-1/pacote/ e o relatório em docs/coleta/tun-1.md.

Fontes, na ordem em que entram:
- RSSSF (ler_rsssf.py): base de jogos, fases, rodadas, datas e autores dos gols de 1996/97 a 2024/25 e dos jogos que as
  páginas da era colonial trazem; a tabela de confrontos de vários anos de 1968/69 a 1995/96; a lista de tabelas finais
  (tunhist.html) de 1955/56 a 2002/03. As tabelas publicadas são a conferência.
- ogol: base dos jogos de 2025/26, quando a RSSSF só tem a tabela; nos outros anos, rodada e data que faltam, conferência
  de placar e o nome de cada clube no ogol.
- Wikipédia em inglês: lista de campeões (com vice), lista de artilheiros e a tabela final de cada temporada, terceira fonte
  quando a tabela da RSSSF e a soma dos jogos não fecham.

Uso: python coleta/tun-1/importar.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-africa"))
sys.path.insert(0, str(AQUI))
import autores  # noqa: E402
import outras_fontes  # noqa: E402
import wiki_tabelas  # noqa: E402
from clubes_tun import CLUBES, clube  # noqa: E402
from conferir import conferir_tabelas, eh_mata, preparar, soma  # noqa: E402
from edicoes import EDICOES, PACOTE, RELATORIO, SLUG, Edicao  # noqa: E402
from explicacoes import EXPLICACOES  # noqa: E402
from ler_rsssf import campeoes, parcial  # noqa: E402
from rsssf_africa import chave  # noqa: E402

# ordem das fases (quanto maior, mais longe o clube chegou)
NIVEL_FASE = {"": 0, "Grupo do rebaixamento": 0, "Desempate do rebaixamento": 0, "Desempate do 2º lugar": 1,
              "Desempate do 6º lugar": 0, "Desempate do 9º lugar": 0, "Fase final": 2, "Mata-mata final": 3,
              "Quartas de final": 4, "Semifinal": 5, "Jogos de classificação": 0, "Jogos de classificação": 0, "Jogos de classificação": 0, "Final": 6, "Desempate do título": 6}
WIKI: dict[str, str] = {}
TOPS: dict[str, list] = {}

# classificação montada com mais de uma tabela publicada, na ordem ("página:linha"); os clubes que faltam vêm depois, pela
# posição no grupo e pelos pontos. 1ª fase em grupos + fase final: a fase final dá as primeiras posições
TABELAS_CLASS: dict[str, list[str]] = {
    "1998/99": ["tun99:352", "tun99:462"],
    "2012/13": ["tun2013:331"],
    "2016/17": ["tun2017:367", "tun2017:491"],
    "2021/22": ["tun2022:391", "tun2022:446"],
    "2022/23": ["tun2023:416", "tun2023:495"],
    "2023/24": ["tun2024:330", "tun2024:479"],
}
# ordem final decidida por jogos de classificação ("Fifth Place Match"...): o vencedor fica com a posição do título do
# jogo, o perdedor com a seguinte (as tabelas dos grupos não dizem isso)
ORDEM_FINAL: dict[str, list[str]] = {
    "2012/13": ["CS Sfaxien", "Espérance de Tunis", "Étoile du Sahel", "Club Africain", "US Monastir", "CA Bizertin",
                "AS Marsa", "CS Hammam-Lif", "Stade Tunisien", "JS Kairouan", "Stade Gabésien", "Olympique Béja",
                "EGS Gafsa", "ES Zarzis", "ES Hammam-Sousse", "Olympique du Kef"],
    "2021/22": ["Espérance de Tunis", "US Monastir", "CS Sfaxien", "Club Africain", "Étoile du Sahel", "US Ben Guerdane",
                "US Tataouine", "AS Rejiche", "CA Bizertin", "AS Solimane", "ES Hammam-Sousse", "Olympique Béja",
                "ES Métlaoui", "ES Zarzis", "CS Chebba", "CS Hammam-Lif"],
}
# rebaixamento que a tabela não diz (ou diz errado): 2012/13, o ES Zarzis perdeu o jogo de 13º lugar ("NB: ES Zarzis
# relegated"); 2021/22, o CAS manteve o CS Chebba (jogo contra o Club Africain dado a ele) e o desempate do 16º lugar
# rebaixou o ES Zarzis e o CS Hammam-Lif
SITUACAO_FIXA: dict[str, dict[str, str]] = {
    "2012/13": {"ES Zarzis": "rebaixado"},
    "2021/22": {"CS Chebba": "", "ES Métlaoui": "", "ES Zarzis": "rebaixado", "CS Hammam-Lif": "rebaixado"},
    # 2019/20: o CS Hammam-Lif caiu nos "Barrages" com clubes da 2ª divisão (fora do pacote) e o CS Chebba foi excluído da
    # 1ª divisão de 2020/21 ("Excluded for 2020/21"; o CAS o readmitiu depois, para 2021/22)
    "2019/20": {"CS Hammam-Lif": "rebaixado", "CS Chebba": "rebaixado"},
    # 2023/24: o AS Marsa perdeu o desempate do rebaixamento ("NB: AS Marsa relegated", fora da tabela)
    "2023/24": {"AS Marsa": "rebaixado"},
}


def nome_fase(f: str, fases: set[str]) -> str:
    if f:
        return f
    return "Primeira fase" if fases - {""} else "Fase única"


def id_edicao(e: Edicao) -> str:
    return re.sub(r"[^0-9a-z]+", "-", chave(e.temporada))


def especial(esp: str) -> str:
    return {"wo_m": "wo", "wo_v": "wo", "awd": "awd", "abd": "abd", "anulado": "n/p", "n/p": "n/p"}.get(esp, "")


def wiki_por_clube(e: Edicao) -> dict[str, list[int]]:
    """Tabela da Wikipédia da temporada: clube -> [J, V, E, D, GP, GC] (a primeira linha de cada clube)."""
    saida: dict[str, list[int]] = {}
    for tb in wiki_tabelas.tabelas(e.temporada):
        for r in tb:
            c = clube(r["nome"], e.ano_inicio) or clube(re.sub(r"^(El|Al)[- ]", "", r["nome"]), e.ano_inicio)
            if c:
                saida.setdefault(c, [r[k] for k in ("j", "v", "e", "d", "gp", "gc")])
    return saida


def montar(e: Edicao, cps: dict[str, str]) -> dict:
    p = preparar(e)
    log: list[str] = list(p["log"])
    for j in [j for j in p["jogos"] if not j["m"] or not j["v"]]:
        log.append(f"linha lida como jogo e descartada (clube não reconhecido): {j['j'].texto} «{j['j'].mandante} x {j['j'].visitante}»")
        p["jogos"].remove(j)
    difs = conferir_tabelas(p)
    jogos = p["jogos"]
    fases = {j["fase"] for j in jogos}
    clubes = sorted({x for j in jogos for x in (j["m"], j["v"]) if x} |
                    {r["clube"] for tb in p["tabelas"] for r in tb["linhas"] if r["clube"] and (e.sem_jogos or e.incompleta)})
    calc = soma(jogos, set(clubes))
    nivel: dict[str, int] = defaultdict(int)
    for j in jogos:
        for x in (j["m"], j["v"]):
            nivel[x] = max(nivel[x], NIVEL_FASE.get(j["fase"], 0))
    camp_txt, vice_txt = ("", "") if e.cancelada else cps.get(e.temporada, ("", ""))
    camp_txt = e.campeao_rsssf or camp_txt
    campeao = clube(camp_txt, e.ano_inicio) if camp_txt else None
    vice = clube(vice_txt, e.ano_inicio) if vice_txt else None
    for txt, c in ((camp_txt, campeao), (vice_txt, vice)):
        if txt and not c:
            log.append(f"clube da lista de campeões da RSSSF não reconhecido: {txt}")
    wk = wiki_por_clube(e)
    final = classificacao(e, p, calc, nivel, campeao, vice, clubes, difs, wk, log)
    return {"e": e, "p": p, "difs": difs, "log": log, "clubes": clubes, "campeao": campeao, "camp_txt": camp_txt,
            "final": final, "fases": fases, "wiki": wk}


def pontos_de(e: Edicao, v: int, emp: int, d: int) -> int:
    pv, pe, pd = e.pontos
    return v * pv + emp * pe + d * pd


def classificacao(e: Edicao, p: dict, calc: dict, nivel: dict, campeao: str | None, vice: str | None, clubes: list[str],
                  difs: list, wk: dict, log: list[str]) -> list[dict]:
    """Classificação final pela tabela publicada (ordem oficial, pontos com punições): a que traz todos os clubes; ou as
    de TABELAS_CLASS, emendadas; ou, com grupos, as dos grupos pela posição. A linha que não fecha com os jogos fica com
    os números dos jogos quando a tabela da Wikipédia confirma os jogos (erro de digitação da tabela da RSSSF). Sem
    tabela, calculada (fase alcançada, pontos, saldo, gols pró). Com só a classificação incompleta da página (posição, às
    vezes jogos e pontos), ela é a classificação. O campeão da lista oficial fica em 1º e o vice (desde 1956/57) em 2º."""
    if e.parcial:
        return parcial_class(e, campeao, vice, log)
    tabs = [tb for tb in p["tabelas"] if not tb.get("acumulada") and not tb.get("parcial") and not tb.get("desempate")]
    por_id = {f"{tb['fonte']}:{tb['t'].linha}": tb for tb in tabs}
    partes: list[dict] = []
    if e.temporada in TABELAS_CLASS:
        partes = [por_id[k] for k in TABELAS_CLASS[e.temporada] if k in por_id]
    else:
        todos = next((tb for tb in tabs if {r["clube"] for r in tb["linhas"]} >= set(clubes) - {None}), None)
        if todos:
            partes = [todos]
    linhas: list[dict] = []
    vistos: set[str] = set()
    errada = {(c, tuple(pub)) for _, c, pub, calc_ in difs if wk.get(c) == calc_}

    def da_tabela(r: dict, tb: dict, nota: str = "") -> dict:
        nums = [r[k] for k in ("j", "v", "e", "d", "gp", "gc")]
        fonte = f"RSSSF ({tb['fonte']}, linha {tb['t'].linha})"
        if (r["clube"], tuple(nums)) in errada:
            nums = calc[r["clube"]]
            fonte += "; números dos jogos (a tabela da Wikipédia confirma os jogos)"
        pts = r["pts"] if (r["clube"], tuple([r[k] for k in ("j", "v", "e", "d", "gp", "gc")])) not in errada else             pontos_de(e, nums[1], nums[2], nums[3])
        return {"clube": r["clube"], "j": nums[0], "v": nums[1], "e": nums[2], "d": nums[3], "gp": nums[4], "gc": nums[5],
                "pts": pts, "ajuste": pts - pontos_de(e, nums[1], nums[2], nums[3]), "obs": (r.get("obs", "") + " " + nota).strip(),
                "fonte": fonte}

    for tb in partes:
        for r in tb["linhas"]:
            if r["clube"] and r["clube"] not in vistos:
                vistos.add(r["clube"])
                linhas.append(da_tabela(r, tb))
    # clubes que faltam: das outras tabelas (grupos), pela posição no grupo e pelos pontos
    resto = []
    for tb in tabs:
        for k, r in enumerate(tb["linhas"], 1):
            if r["clube"] and r["clube"] not in vistos and (not clubes or r["clube"] in clubes):
                resto.append((nivel[r["clube"]], r.get("pos") or k, r["pts"], r["gp"] - r["gc"], r["gp"], r, tb))
                vistos.add(r["clube"])
    for *_, r, tb in sorted(resto, key=lambda x: (-x[0], x[1], -x[2], -x[3], -x[4], x[5]["clube"])):
        linhas.append(da_tabela(r, tb))
    # clubes sem tabela: calculados
    pts_c = lambda c: pontos_de(e, *calc.get(c, [0] * 6)[1:4])
    for c in sorted(set(clubes) - vistos, key=lambda c: (-nivel[c], -pts_c(c), c)):
        x = calc.get(c, [0] * 6)
        linhas.append({"clube": c, "j": x[0], "v": x[1], "e": x[2], "d": x[3], "gp": x[4], "gc": x[5], "pts": pts_c(c),
                       "ajuste": 0, "obs": "", "fonte": "calculada (fora das tabelas publicadas)" if p["tabelas"] else
                       "calculada com os jogos que a página traz (fase alcançada, pontos)"})
    # mata-mata decidido depois da liga (final, desempate do título): campeão e finalista em cima
    # (só quando a final decide o título: a "final" do grupo do rebaixamento não sobe ninguém)
    finalistas = [c for c in clubes if nivel[c] >= 6]
    finalistas = finalistas if campeao in finalistas else []
    if e.temporada in ORDEM_FINAL:
        ordem = ORDEM_FINAL[e.temporada]
        assert {r["clube"] for r in linhas} == set(ordem), e.temporada
        linhas.sort(key=lambda r: ordem.index(r["clube"]))
    for c in sorted(finalistas, key=lambda c: c != campeao):
        r = next((r for r in linhas if r["clube"] == c), None)
        if r:
            linhas.remove(r)
            linhas.insert(0 if c == campeao else 1, r)
    return podio(linhas, campeao, vice, log)


def podio(linhas: list[dict], campeao: str | None, vice: str | None, log: list[str]) -> list[dict]:
    """Campeão em 1º e vice da lista (desde 1956/57) em 2º; sem classificação nenhuma, só os dois."""
    vazio = {"j": None, "v": None, "e": None, "d": None, "gp": None, "gc": None, "pts": None, "ajuste": None, "obs": ""}
    for pos, c in ((1, vice), (0, campeao)):
        if not c:
            continue
        r = next((r for r in linhas if r["clube"] == c), None)
        if r is None:
            r = {"clube": c, **vazio, "fonte": "lista de campeões da RSSSF (tunchamp.html)"}
        else:
            linhas.remove(r)
        linhas.insert(min(pos, len(linhas)), r)
    for k, r in enumerate(linhas, 1):
        r["pos"] = k
    return linhas


def parcial_class(e: Edicao, campeao: str | None, vice: str | None, log: list[str]) -> list[dict]:
    """Classificação incompleta da página (ler_rsssf.parcial): a ordem da página, com o que ela traz."""
    linhas = []
    for r in parcial(e):
        c = clube(r["nome"], e.ano_inicio, r.get("cidade"))
        if not c:
            log.append(f"clube da classificação incompleta não reconhecido: {r['nome']}")
            continue
        tem = r["v"] is not None and r["pts"] is not None
        linhas.append({"clube": c, "j": r["j"], "v": r["v"], "e": r["e"], "d": r["d"], "gp": r["gp"], "gc": r["gc"],
                       "pts": r["pts"], "ajuste": (r["pts"] - pontos_de(e, r["v"], r["e"], r["d"])) if tem else None,
                       "obs": r.get("obs", ""), "fonte": f"RSSSF ({e.parcial[0]}, classificação incompleta)"})
    return podio(linhas, campeao, vice, log)


def situacao(r: dict, campeao: str | None, k: int, cancelada: bool) -> str:
    if r["clube"] == campeao:
        return "campeao"
    if k == 2 and not cancelada:
        return "vice"
    if re.search(r"(?<!not )\brelegated\b", r.get("obs", ""), re.I) and not cancelada:   # temporada cancelada: sem rebaixamento
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
    PACOTE.mkdir(parents=True, exist_ok=True)
    (PACOTE / "competicao.json").write_text(json.dumps({
        "slug": SLUG, "nome": "Campeonato Tunisiano", "nome_curto": "Tunisiano", "tipo": "liga", "nivel": 1, "pais": "TUN",
        "pais_nome": "Tunísia", "regiao": None, "confederacao": "CAF", "rotulo_painel": "Tunisiano",
        "menu_painel": "Tunísia · 1ª divisão", "do_painel": "do Campeonato Tunisiano", "o_painel": "o Campeonato Tunisiano",
        "observacao": "1ª divisão tunisiana (hoje Ligue Professionnelle 1) de 1907 a 2025/26, com a era colonial (campeonato "
                      "da USFSA até 1920/21 e da Liga da Tunísia de 1921/22 a 1954/55), que a contagem oficial inclui. Sem as "
                      "temporadas sem competição; 1951/52 (abandonado) entra sem campeão. Pontos 3-2-1 até 1985/86, 4-2-1 de "
                      "1986/87 a 1991/92, 2-1-0 de 1992/93 a 1994/95 e 3-1-0 desde 1995/96."},
        ensure_ascii=False, indent=1), encoding="utf-8")
    L = defaultdict(list)
    nomes_fonte: dict[str, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
    usados: set[str] = set()
    for d in eds:
        e, p = d["e"], d["p"]
        eid = id_edicao(e)
        fases = d["fases"]
        linha_de = lambda j: j["j"].linha if j["j"] else 10 ** 6
        ordem_f = sorted(fases, key=lambda f: (NIVEL_FASE.get(f, 0), min((linha_de(j) for j in p["jogos"] if j["fase"] == f), default=0)))
        for k, f in enumerate(ordem_f, 1):
            js = [j for j in p["jogos"] if j["fase"] == f]
            grupos = sorted({j["grupo"] for j in js if j["grupo"] and j["grupo"] != "Interzonal"})
            mata = eh_mata(f) and f != "Desempate do grupo B"
            pares = Counter(frozenset((j["m"], j["v"])) for j in js)
            serie = ("jogo_unico" if max(pares.values(), default=1) == 1 else "ida_volta") if mata else "pontos_corridos"
            tipo = "mata_mata" if mata else ("grupos" if len(grupos) >= 2 else "liga")
            L["fases"].append([e.temporada, k, nome_fase(f, fases), tipo, len(grupos) if tipo == "grupos" else None, serie, ""])
        n = 0
        gols_ed = autor_ed = 0
        og = outras_fontes.ogol(e, p["jogos"])
        d["ogol"] = og
        idx = {id(j): k for k, j in enumerate(p["jogos"])}
        for k, g in og["ligado"].items():
            j = p["jogos"][k]
            if j["j"] and j["j"].texto.startswith("ogol:"):
                continue   # o próprio jogo do ogol (ano em que ele é a base)
            for lado, nm in (("m", "mandante"), ("v", "visitante")):
                if clube(g[nm], e.ano_inicio):
                    nomes_fonte[j[lado]][f"ogol:{g[nm]}"].append(e.ano_inicio)
            x = j["j"]
            if (g["gols_mandante"], g["gols_visitante"]) != (x.gm, x.gv) and x.gm is not None and g["gols_mandante"] is not None:
                d["log"].append(f"placar diferente no ogol — {j['m']} x {j['v']} ({x.data}): RSSSF {x.gm}-{x.gv}, ogol "
                                f"{g['gols_mandante']}-{g['gols_visitante']}; fica o da RSSSF")
            dd, dr = outras_fontes._dia(g["data"]), outras_fontes._dia(x.data)
            if dr and dd and abs(dr - dd) > 3:
                d["log"].append(f"data diferente no ogol — {j['m']} x {j['v']}: RSSSF {x.data}, ogol {g['data']}; fica a da RSSSF")
        for j in sorted(p["jogos"], key=lambda j: (ordem_f.index(j["fase"]), j["j"].linha if j["j"] else 10 ** 6)):
            n += 1
            pid = f"{eid}-{n:04d}"
            x = j["j"]
            ex = j.get("extra")
            usados |= {j["m"], j["v"]}
            if x:
                pref = "ogol" if x.texto.startswith("ogol:") else "rsssf"
                nomes_fonte[j["m"]][f"{pref}:{x.mandante}"].append(e.ano_inicio)
                nomes_fonte[j["v"]][f"{pref}:{x.visitante}"].append(e.ano_inicio)
            gm, gv = j["gm"], j["gv"]
            esp = especial(j["esp"])
            obs = []
            if j["esp"] in ("wo_m", "wo_v"):
                venc = j["m"] if j["esp"] == "wo_m" else j["v"]
                if gm is not None:
                    obs.append(f"pontos para o {venc} (decisão fora de campo); placar em campo {gm}-{gv}")
                    esp = "awd"
                else:
                    if x and x.nota in ("bt", "lt"):   # "A bt B": a página diz só quem venceu
                        obs.append(f"vitória do {venc} sem placar conhecido (a página diz só quem venceu)")
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
            if x and x.nota and x.nota not in ("bt", "lt"):
                obs.append(x.nota)
            if ex and ex.get("obs"):
                obs.append(ex["obs"])
            texto_autores = x.gols_texto if x else ""
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
            local = x.local if x else None
            loc_clube = clube(local, e.ano_inicio) if local else None
            estadio = f"Estádio do {loc_clube}" if loc_clube else local
            rodada, data = (x.rodada, x.data) if x else (ex.get("rodada"), ex.get("data"))
            base = ("ogol" if x.texto.startswith("ogol:") else "rsssf") if x else ex.get("base", "rsssf")
            fonte_id = (x.texto if base == "ogol" else f"rsssf:{x.texto}") if x else ex["fonte_id"]
            go = og["ligado"].get(idx[id(j)])
            if go and base != "ogol":
                fonte_id += f" ogol:{go['id']}"
                rodada = rodada or go.get("rodada")
                data = data or (go["data"] if go["data"][:4] != "0000" else None)
            L["partidas"].append([pid, e.temporada, nome_fase(j["fase"], fases), j["grupo"] if j["grupo"] != "Interzonal" else "",
                                  rodada, data, None, j["m"], j["v"], gm, gv,
                                  x.pen_m if x else None, x.pen_v if x else None, esp, estadio, None, None,
                                  "ogol" if base == "ogol" else "RSSSF", fonte_id,
                                  "" if sep or not texto_autores or not autores.eh_autores(texto_autores) else texto_autores,
                                  "; ".join(o for o in obs if o)])
        # classificação final
        for r in d["final"]:
            usados.add(r["clube"])
            L["classificacao_final"].append([e.temporada, r["pos"], r["clube"], r["j"], r["v"], r["e"], r["d"], r["gp"], r["gc"],
                                             r["pts"], r["ajuste"],
                                             SITUACAO_FIXA.get(e.temporada, {}).get(r["clube"],
                                                 situacao(r, d["campeao"], r["pos"], bool(e.cancelada))),
                                             r["fonte"], "punição/bônus de pontos (tabela publicada)" if r["ajuste"] else ""])
        # tabelas publicadas (as da página da RSSSF)
        vistas = set()
        for tb in p["tabelas"]:
            ch = tuple((r["clube"], r["j"], r["pts"]) for r in tb["linhas"])
            if ch in vistas or tb.get("acumulada") or tb.get("parcial") or tb.get("desempate"):
                continue
            vistas.add(ch)
            for r in tb["linhas"]:
                if r["clube"]:
                    nomes_fonte[r["clube"]][f"rsssf:{r['nome']}"].append(e.ano_inicio)
                L["tabelas_publicadas"].append([e.temporada, nome_fase(tb["t"].fase, fases), tb["t"].grupo, r["pos"], r["nome"],
                                                r["clube"], r["j"], r["v"], r["e"], r["d"], r["gp"], r["gc"], r["pts"],
                                                f"RSSSF ({tb['fonte']}, linha {tb['t'].linha})"])
        # artilheiros: lista da Wikipédia; sem ela, a contagem dos gols com autor (quando quase todos os gols têm autor)
        tops = TOPS.get(e.temporada)
        if tops:
            for jog, ctxt, ng in tops:
                L["artilheiros"].append([e.temporada, jog, clube(ctxt, e.ano_inicio) or clube(re.sub(r"^(El|Al)[- ]", "", ctxt), e.ano_inicio)
                                         or ctxt, ng, "Wikipédia (en, List of Tunisian Ligue Professionnelle 1 top scorers)"])
        elif gols_ed and autor_ed >= 0.95 * gols_ed:
            cont = Counter((r[2], r[1]) for r in L["gols"] if r[0].startswith(eid + "-") and r[5] != "contra")
            if cont:
                topo = max(cont.values())
                for (jog, c), ng in sorted(cont.items()):
                    if ng == topo:
                        L["artilheiros"].append([e.temporada, jog, c, ng, "contagem dos gols com autor"])
        # edição
        final = d["final"]
        vice = final[1]["clube"] if len(final) > 1 and d["campeao"] else ""
        if e.cancelada:
            formato_ = "temporada não terminada" + (f" ({e.incompleta})" if e.incompleta else "")
        elif e.sem_jogos:
            formato_ = ("sem jogos (só a tabela final)" if e.tabelas or e.hist else "sem jogos (só a classificação incompleta)"
                        if e.parcial else "sem jogos (só o campeão)" if not e.ano_inicio >= 1955 else "sem jogos (só o campeão e o vice)")
        else:
            formato_ = e.incompleta or formato(ordem_f, L["fases"], e.temporada)
        d["formato"] = formato_
        pv, pe, pd = e.pontos
        sistema = f"pontos {pv}-{pe}-{pd} (vitória, empate, derrota)" if pd or pe != 1 else ""
        obs_ed = "; ".join(x for x in (e.cancelada, e.obs, sistema if e.ano_inicio >= 1955 else "") if x)
        L["edicoes"].append([e.temporada, e.ano_inicio, e.ano_fim, e.nome_oficial, len(final) or len(d["clubes"]), e.pontos_vitoria,
                             # empate e derrota só quando não são 1 e 0 (vazias valem 1 e 0)
                             *(e.pontos[1:] if e.pontos[1:] != (1, 0) else ("", "")),
                             formato_, d["campeao"] or "", vice,
                             "; ".join((["RSSSF"] if e.trechos or e.tabelas else []) + (["ogol"] if e.ogol is not None or og["ligado"] else [])
                                       + (["Wikipédia"] if d["wiki"] else [])), obs_ed])
        n_tab = 0 if (e.sem_jogos or e.incompleta) else len(vistas)
        n_div = len({x[0] for x in d["difs"]})
        L["conferencia"].append([e.temporada, n, esperados(d), n_tab - n_div, n_div, gols_ed, autor_ed,
                                 (f"campeão {d['campeao']} (RSSSF: {d['camp_txt']}; Wikipédia: {WIKI.get(e.temporada, ('-', ''))[0]})"
                                  if d["campeao"] else "sem campeão: " + (e.cancelada or "-")) +
                                 ("; divergências explicadas no relatório" if n_div else "")])
    # clubes
    for c in sorted(u for u in usados if u):
        cid, prov = CLUBES[c]
        partes = []
        for nf, anos in sorted(nomes_fonte[c].items()):
            a = sorted(set(anos))
            partes.append(f"{nf}:{a[0]}" + (f"-{a[-1]}" if a[-1] != a[0] else ""))
        L["clubes"].append([c, prov or None, cid or None, "TUN", "|".join(partes)])
    _csv("clubes.csv", ["clube", "regiao", "cidade", "pais", "nomes_fonte"], L["clubes"])
    _csv("edicoes.csv", ["temporada", "ano_inicio", "ano_fim", "nome_oficial", "num_clubes", "pontos_vitoria", "pontos_empate", "pontos_derrota",
                         "formato", "campeao", "vice",
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
    p, e = d["p"], d["e"]
    if e.sem_jogos or e.incompleta:
        return len(p["jogos"])
    for tb in p["tabelas"]:
        if tb.get("ok") is not None and not (tb.get("acumulada") or tb.get("parcial") or tb.get("desempate")) and \
                {r["clube"] for r in tb["linhas"]} == set(d["clubes"]):
            # (o jogo interrompido e não completado fica no pacote, sem valer na tabela)
            return sum(r["j"] for r in tb["linhas"]) // 2 + sum(1 for j in p["jogos"] if j["fase"] != tb["t"].fase or
                                                                 j["esp"] in ("abd", "anulado", "n/p"))
    return len(p["jogos"])


def formato(ordem_f: list[str], linhas_fases: list[list], temporada: str) -> str:
    desc = []
    for r in linhas_fases:
        if r[0] != temporada:
            continue
        t = {"liga": "pontos corridos", "grupos": f"{r[4]} grupos", "mata_mata": "mata-mata"}[r[3]]
        if r[2].startswith("Desempate"):
            t = "desempate"
        elif r[2] == "Jogos de classificação":
            t = "jogos de classificação"
        elif r[2] in ("Fase final", "Grupo do rebaixamento"):
            t = "grupos do título e do rebaixamento" if r[2] == "Grupo do rebaixamento" else "fase final"
        if not desc or desc[-1] != t:
            desc.append(t)
    if "grupos do título e do rebaixamento" in desc and "fase final" in desc:
        desc.remove("fase final")
    return "mata-mata" if desc and all(x == "mata-mata" for x in desc) else " + ".join(desc)


def candidatos(d: dict) -> list[str]:
    """Jogo entre dois clubes que não fecham cujo placar, trocado, faz os dois fecharem com a tabela publicada (a correção
    não é aplicada: fica no relatório como o provável jogo da diferença)."""
    # (fora os clubes em que a tabela da Wikipédia confirma os jogos: ali o erro é da tabela)
    divs = {c: (pub, calc) for _, c, pub, calc in d["difs"] if d["wiki"].get(c) != calc}
    res = lambda x, y: (x > y) - (x < y)
    saida = []
    cs = list(divs)
    for i, a in enumerate(cs):
        for b in cs[i + 1:]:
            da = [x - y for x, y in zip(*divs[a])]
            db = [x - y for x, y in zip(*divs[b])]
            if da[0] or db[0]:
                continue
            for j in d["p"]["jogos"]:
                if {j["m"], j["v"]} != {a, b} or j["gm"] is None:
                    continue
                dm, dv = (da, db) if j["m"] == a else (db, da)
                ngm, ngv = j["gm"] + dm[4], j["gv"] + dv[4]
                if dm[4] != dv[5] or dv[4] != dm[5] or ngm < 0 or ngv < 0 or (ngm, ngv) == (j["gm"], j["gv"]):
                    continue
                novo, velho = res(ngm, ngv), res(j["gm"], j["gv"])
                if dm[1] == (novo == 1) - (velho == 1) and dm[2] == (novo == 0) - (velho == 0):
                    x = j["j"]
                    saida.append(f"provável jogo da diferença: {j['m']} {j['gm']}-{j['gv']} {j['v']} ({x.data if x else 's/d'}, "
                                 f"{x.texto if x else 'extra'}); com {ngm}-{ngv} as linhas dos dois clubes fechariam com a tabela. "
                                 "Não corrigido: só a tabela indica o placar")
    return saida


def diagnostico(d: dict) -> list[str]:
    """Uma linha por clube que não fecha com a tabela publicada, com o que a tabela da Wikipédia diz."""
    saida = []
    for fonte_l, clube_, pub, calc in d["difs"]:
        w = d["wiki"].get(clube_)
        txt = f"tabela publicada x jogos — {fonte_l}: {clube_} tabela {pub} jogos {calc}"
        if w == calc:
            txt += " — a tabela da Wikipédia fecha com os jogos: erro de digitação da tabela da RSSSF (a classificação usa os números dos jogos)"
        elif w == pub:
            txt += " — a tabela da Wikipédia confirma a da RSSSF: algum placar do clube está diferente na fonte dos jogos"
        elif w:
            txt += f" — a Wikipédia traz {w}"
        elif pub[0] != calc[0]:
            txt += f" — {'faltam' if calc[0] < pub[0] else 'sobram'} {abs(pub[0] - calc[0])} jogo(s) do clube na fonte dos jogos"
        else:
            txt += " — mesmo número de jogos; placar diferente em algum jogo do clube (sem terceira fonte para dizer qual)"
        saida.append(txt)
    return saida + candidatos(d)


def relatorio(eds: list[dict]) -> None:
    linhas = ["# Campeonato Tunisiano (1ª divisão) — coleta de dados", "",
              "Gerado por `python coleta/tun-1/importar.py`. Pacote em `data/coleta/tun-1/pacote/`.", "",
              f"**Edições:** {len(eds)}, uma por temporada, de 1907 a 2025/26, como na lista de campeões da RSSSF "
              "(`tunchamp.html`) e na Wikipédia em inglês. A era colonial entra (pesquisa de 24/11/2026): a contagem oficial "
              "usada na Tunísia inclui esses títulos (o \"34º título\" do Espérance em 2024/25 só fecha com o de 1941/42; o "
              "\"14º\" do Club Africain em 2025/26, com os de 1946/47 e 1947/48). Até 1920/21 era o campeonato da USFSA; de "
              "1921/22 a 1954/55, da Liga da Tunísia, quase sempre com campeões regionais e uma final. Ficam de fora as "
              "temporadas sem competição (1909/10, as das guerras mundiais e 1942/43 e 1943/44); 1951/52 foi abandonado e entra "
              "sem campeão. A Wikipédia lista um título do Racing Club de Tunis em 1909/10, que a RSSSF não traz: fica de "
              "fora.", "",
              "**Fora do pacote:** a Copa da Tunísia e as outras copas, a 2ª divisão e os jogos de promoção.", "",
              "**Fontes:** RSSSF (páginas por temporada, `data/coleta/tun-1/rsssf/`: base dos jogos de 1996/97 a 2024/25; a "
              "tabela de confrontos de 1968/69, 1970/71, 1977/78, 1980/81, 1982/83 e de 1987/88 a 1995/96, sem datas; a lista de "
              "tabelas finais `tunhist.html`, de 1955/56 a 2002/03; na era colonial, as finais que a página traz); ogol (base "
              "dos jogos de 2025/26; nos outros anos, conferência, rodada e data); Wikipédia em inglês (listas de campeões e "
              "de artilheiros e a tabela de cada temporada, terceira fonte nas divergências). A ESPN não tem a liga "
              "tunisiana.", "",
              "**Clubes:** o nome pelo qual o clube é conhecido (Espérance de Tunis, Club Africain, Étoile du Sahel, CS "
              "Sfaxien...). Mesmo clube com outro nome é um só (Railway Sports de Sfax = Sfax Railways Sports; US Ferryville "
              "= USM Bourguiba; Olympique Tunis = US Musulmane Olympique). Regras em `coleta/tun-1/clubes_tun.py`.", "",
              "**Regras:** o placar é o da RSSSF (ou do ogol, nos anos em que é a base). A classificação é a tabela publicada "
              "(ordem oficial e pontos); quando uma linha dela não fecha com os jogos e a tabela da Wikipédia confirma os "
              "jogos, a linha fica com os números dos jogos. \"A bt B\" (venceu, sem placar conhecido) entra como vitória sem "
              "placar. Pontos como as tabelas contam: 3-2-1 (vitória, empate, derrota) até 1985/86, 4-2-1 de 1986/87 a 1991/92, "
              "2-1-0 de 1992/93 a 1994/95 e 3-1-0 desde 1995/96 (o `ajuste_pontos` já usa o sistema de cada ano).", "",
              "| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Formato |",
              "|---|---|---|---|---|---|---|---|"]
    conf = {r[0]: r for r in CONF}
    for d in eds:
        e = d["e"]
        c = conf[e.temporada]
        linhas.append(f"| {e.temporada} | {len(d['final']) or len(d['clubes'])} | {c[1]} ({c[2]}) | {c[5]} | {c[6]} | {c[3]} / {c[4]} | "
                      f"{d['campeao'] or '—'} | {d.get('formato', '')} |")
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
        fontes = []
        if e.ogol is not None:
            fontes.append(f"ogol: base dos jogos ({sum(1 for j in d['p']['jogos'] if j['j'] and j['j'].texto.startswith('ogol:'))} jogos)")
        elif og.get("ligado"):
            fontes.append(f"ogol: {len(og['ligado'])} jogos casados (edição {og['edicao']} do ogol, {og.get('n', 0)} jogos)")
        extras = [f"jogo acrescentado à mão — {j['m']} {j['gm']}-{j['gv']} {j['v']}: {j['extra'].get('obs') or j['extra']['fonte_id']}"
                  for j in d["p"]["jogos"] if j.get("extra")]
        itens = EXPLICACOES.get(e.temporada, []) + [x for x in (e.cancelada, e.incompleta, e.obs) if x] + fontes + extras + \
            diagnostico(d) + d["log"] + especiais
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
    WIKI.update(wiki_tabelas.campeoes())   # temporada -> (campeão, vice)
    TOPS.update(wiki_tabelas.artilheiros())
    eds = []
    for e in EDICOES:
        d = montar(e, cps)
        eds.append(d)
        print(f"{e.temporada:10s} {len(d['p']['jogos']):4d} jogos  campeão {d['campeao']}  divergências {len(d['difs'])}", flush=True)
    gravar(eds)
    relatorio(eds)
    print("pacote gravado em", PACOTE, "e relatório em", RELATORIO)
