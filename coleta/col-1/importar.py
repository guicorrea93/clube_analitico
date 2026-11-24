"""Junta as fontes da 1ª divisão colombiana e grava o pacote em data/coleta/col-1/pacote/ e o relatório em docs/coleta/col-1.md.

Fontes, na ordem em que entram:
- RSSSF (ler_rsssf.py): base de jogos, fases, grupos, rodadas, datas e autores dos gols de 1995/96 em diante (menos 2011,
  2012 e 2025). As tabelas publicadas nas páginas de cada temporada (1948 em diante) são a conferência; nos anos sem jogos,
  a tabela final é a classificação.
- Wikipédia em espanhol (wikipedia_jogos.py): jogos de 1948-1986, 1988-1990, 2011, 2012 e 2025.
- ESPN (liga col.1, 2005 em diante): hora, estádio, público, gols com minuto e cartões.

Uso: python coleta/col-1/importar.py
"""
from __future__ import annotations

import csv
import json
import re
import unicodedata
import sys
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
sys.path.insert(0, str(AQUI))
import autores  # noqa: E402
import outras_fontes  # noqa: E402
from clubes_col import CLUBES, clube  # noqa: E402
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
              "Desempate do grupo": 5, "Final dos hexagonais": 5}   # CO-013 (1957)
WIKI: dict[str, str] = {}
TOPS: dict[str, list] = {}
TOPS_ES: dict[str, tuple[list[str], int]] = {}
BONUS: dict[str, dict[str, str]] = {}   # CO-016: temporada -> clube -> observação do bônus da fase final


def bonus_fase_final() -> dict[str, dict[str, str]]:
    """CO-016: bônus da fase final (frações de ponto) pelas páginas da RSSSF: "Bonus Table" (1983-1988, 1993, 1994), o texto
    de 1992 e o "[BP: x]" de 1998. Ficam na observação da classificação: os pontos são inteiros no banco (1990 e 1991 já vêm
    com o bônus somado nas tabelas da fase final)."""
    from ler_rsssf import linhas
    saida: dict[str, dict[str, str]] = defaultdict(dict)
    texto = lambda b, fonte: f"bônus de {b.replace('.', ',')} ponto(s) para a fase final (RSSSF, {fonte}), fora dos pontos"
    for ano in (1983, 1984, 1985, 1986, 1987, 1988, 1993, 1994):
        ls = linhas(f"col{ano % 100:02d}")
        i = next((k for k, l in enumerate(ls) if l.strip() == "Bonus Table"), None)
        for l in ls[i + 1:i + 14] if i is not None else []:
            if m := re.match(r"^\s*\d+\.\s+(.+?)\s{2,}.*?([\d.]+)\s*$", l):
                if (c := clube(m.group(1).strip(), ano)) and float(m.group(2)) > 0:
                    saida[str(ano)][c] = texto(m.group(2), "Bonus Table")
    for l in linhas("col92"):
        if l.startswith("Cali 1, "):   # "Bonus points won for final rounds: Cali 1, Indep. Santa Fe 0.75, ..."
            for nome, b in re.findall(r"([A-Z][\w. ]+?)\s+([\d.]+)(?:,|\.$)", l):
                if c := clube(nome.strip(), 1992):
                    saida["1992"][c] = texto(b, "texto da página")
    for l in linhas("col98")[:900]:   # só a 1ª divisão (a 2ª vem depois)
        if m := re.match(r"^\s*\d+\.(.+?)\s{2,}.*\[BP:\s*([\d.]+)\s*\]", l):
            if c := clube(m.group(1).strip(), 1998):
                saida["1998"][c] = texto(m.group(2), "[BP]")
    return saida


def _clube_do_autor(jog: str, autores: Counter) -> str:
    """Clube de um goleador da Wikipédia pelos gols com autor da edição: o autor com o mesmo sobrenome (e o mesmo prenome,
    se houver mais de um) que mais marcou. Sem ninguém, fica vazio."""
    sem = lambda s: "".join(ch for ch in unicodedata.normalize("NFKD", s.lower()) if not unicodedata.combining(ch)).split()
    alvo = sem(jog)
    if not alvo:
        return ""
    cands = [(n, c, x) for (n, c), x in autores.items() if alvo[-1] in sem(n)]
    if len({c for _, c, _ in cands}) > 1:
        cands = [k for k in cands if sem(k[0])[:1] == alvo[:1]] or cands
    return max(cands, key=lambda k: k[2])[1] if cands else ""


def nome_fase(f: str, fases: set[str]) -> str:
    if f:
        return f
    return "Primeira fase" if fases - {""} else "Fase única"


def id_edicao(e: Edicao) -> str:
    return re.sub(r"[^0-9a-z]+", "-", chave(e.temporada))


def especial(esp: str) -> str:
    return {"wo_m": "wo", "wo_v": "wo", "awd": "awd", "abd": "abd", "anulado": "n/p", "n/p": "n/p"}.get(esp, "")


def virada_do_ano(e: Edicao, jogos: list[dict]) -> None:
    """CO-010: na Wikipédia a data vem sem ano e o leitor põe o ano do campeonato. A final de 1957 e a final dos hexagonais
    (CO-013) foram em fevereiro e março de 1958; o desempate do título de 1971, em janeiro e fevereiro de 1972."""
    fases = {"1957": {"Final", "Final dos hexagonais"}, "1971": {"Desempate do título"}}.get(e.temporada, set())
    for j in jogos:
        if j["fase"] in fases and j["j"] and j["j"].data and j["j"].data[:4] == str(e.ano_inicio):
            j["j"].data = f"{e.ano_inicio + 1}{j['j'].data[4:]}"


def acerta_grupos(e: Edicao, p: dict) -> None:
    """CO-012 (1999 em diante, depois da conferência): nos quadrangulares semifinais, o grupo de cada jogo sai das tabelas
    publicadas da fase (cada tabela com clubes que as outras não têm é um grupo; sem rótulo, A, B na ordem); a 1ª fase sem
    tabelas de grupo fica sem grupo (é uma tabela só; os jogos herdavam o grupo dos quadrangulares). As outras fases ficam
    como estão (a Copa Mustang de 1995-1997 tem tabelas parciais que enganariam a regra)."""
    if e.ano_inicio < 1999:
        return
    tabs: dict[str, list[tuple[str, frozenset]]] = defaultdict(list)
    for tb in p["tabelas"]:
        cs = frozenset(r["clube"] for r in tb["linhas"] if r["clube"])
        if cs and all(cs != x for _, x in tabs[tb["t"].fase]):
            tabs[tb["t"].fase].append((tb["t"].grupo, cs))
    for fase in {j["fase"] for j in p["jogos"]} & {"", "Quadrangulares semifinais"}:
        ts = tabs.get(fase, [])
        disjuntas = len(ts) >= 2 and all(not (a & b) for k, (_, a) in enumerate(ts) for _, b in ts[k + 1:])
        nome = {c: (g or "ABCDEFGH"[k]) for k, (g, cs) in enumerate(ts) for c in cs} if disjuntas else {}
        for j in p["jogos"]:
            if j["fase"] == fase:
                j["grupo"] = nome[j["m"]] if nome.get(j["m"]) and nome.get(j["m"]) == nome.get(j["v"]) else ""


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
    acerta_grupos(e, p)
    jogos = p["jogos"]
    fases = {j["fase"] for j in jogos}
    # campanha de cada clube (resultado oficial; W.O. vale vitória) e fase mais longe
    clubes = sorted({x for j in jogos for x in (j["m"], j["v"]) if x})
    if e.sem_jogos and p["tabelas"]:   # edição sem jogos: os clubes são os da maior tabela (só a Primera A: CO-003, CO-019)
        maior = max(p["tabelas"], key=lambda tb: (len(tb["linhas"]), sum(r["j"] or 0 for r in tb["linhas"])))
        clubes = sorted({r["clube"] for r in maior["linhas"] if r["clube"]})
    calc = soma(jogos, set(clubes))
    nivel: dict[str, int] = defaultdict(int)
    for j in jogos:
        for x in (j["m"], j["v"]):
            nivel[x] = max(nivel[x], NIVEL_FASE.get(j["fase"], 0))
    # campeão pela lista da RSSSF (colchamp.html)
    camp_txt = e.campeao_rsssf or cps.get(e.temporada, "")
    campeao = clube(camp_txt, e.ano_inicio) if camp_txt else None
    if not campeao and camp_txt:
        log.append(f"campeão da lista da RSSSF não reconhecido: {camp_txt}")
    final = classificacao(e, p, calc, nivel, campeao, clubes)
    return {"e": e, "p": p, "difs": difs, "log": log, "clubes": clubes, "campeao": campeao, "camp_txt": camp_txt,
            "final": final, "fases": fases}


def artilheiros_rsssf() -> dict[str, list[tuple[str, str, int]]]:
    """coltops.html: temporada -> [(jogador, clube como na página, gols)]. "Ap"/"Fn" ao lado do ano é o Apertura ou o
    Finalización; empate na artilharia vem em linhas seguidas, cada uma com os gols."""
    from ler_rsssf import linhas
    saida: dict[str, list] = defaultdict(list)
    ano = temp = None
    for l in linhas("coltops"):
        # "1948    Alfredo CASTILLO (Arg.)    Millonarios    31"; "2002 Ap ..."; "     Fn ..."
        # CO-017: "(Arg.)" com um espaço só antes do clube (1977, 1978); "Ap"/"Fn" só como palavra ("Apolinar PANIAGUA",
        # 1971, virava "1971 Apertura")
        m = re.match(r"^(\d{4}(?:/\d{2})?)?\s+(?:(Ap|Fn|Fi|Cl)\s+)?(\S.*?)(?:\s*\([A-Za-z.]+\)\s+|\s{2,})(\S.*?)\s+(\d{1,2})\s*$", l)
        if not m or re.search(r"\d", m.group(4)):   # linha com duas colunas de artilheiros: fica de fora
            continue
        if m.group(1):
            ano = m.group(1)
        if not ano:
            continue
        if m.group(2):
            temp = f"{ano} {'Apertura' if m.group(2) == 'Ap' else 'Finalización'}"
        elif m.group(1):
            temp = ano
        # sem ano nem "Ap"/"Fn": empate com a linha de cima (mesma temporada)
        jog = " ".join(p.capitalize() if p.isupper() and len(p) > 1 else p for p in m.group(3).split())
        saida[temp].append((jog, m.group(4).strip(), int(m.group(5))))
    return saida


def classificacao(e: Edicao, p: dict, calc: dict, nivel: dict, campeao: str | None, clubes: list[str]) -> list[dict]:
    """Classificação final: a tabela publicada que traz todos os clubes e fecha com os jogos (ordem oficial, pontos com
    punições); sem ela, calculada (fase alcançada, pontos, saldo, gols pró). O campeão da lista oficial fica em 1º."""
    pv = e.pontos_vitoria
    pub = next((tb for tb in p["tabelas"] if not tb.get("acumulada") and tb.get("ok") and
                {r["clube"] for r in tb["linhas"]} == set(clubes)), None)
    if e.sem_jogos:   # sem jogos: a tabela final da RSSSF é a classificação
        pub = next((tb for tb in p["tabelas"] if tb.get("sem_conferencia")), None)
        if pub is None and p["tabelas"]:   # CO-003 (1987, 1991-1995): a maior tabela da página (a da temporada inteira)
            pub = max(p["tabelas"], key=lambda tb: (len(tb["linhas"]), sum(r["j"] or 0 for r in tb["linhas"])))
    elif any(nivel[c] > 0 for c in clubes):
        # D-02 (A), CO-002: com fase final, a ordem é a da fase alcançada e, dentro dela, os pontos da campanha toda (números =
        # soma de todos os jogos da edição); campeão e vice da lista em cima. Não a tabela da 1ª fase
        pub = None
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
    # CO-001: vice da lista da RSSSF (coluna Runners Up) logo abaixo do campeão
    vice = clube(VICES[e.temporada], e.ano_inicio) if VICES.get(e.temporada) and campeao else None
    if vice and len(linhas) > 2 and linhas[1]["clube"] != vice and any(r["clube"] == vice for r in linhas[2:]):
        v = next(r for r in linhas if r["clube"] == vice)
        linhas.remove(v)
        linhas.insert(1, v)
    for k, r in enumerate(linhas, 1):
        r["pos"] = k
    return linhas


VICES: dict[str, str] = {}
REBAIXADOS: dict[str, set[str]] = {}


def situacao(r: dict, campeao: str | None, k: int, temporada: str = "") -> str:
    if r["clube"] == campeao:
        return "campeao"
    if k == 2 and campeao:
        return "vice"
    if r["clube"] in REBAIXADOS.get(temporada, set()):   # CO-007: lista da Wikipédia em espanhol
        return "rebaixado"
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
        "slug": SLUG, "nome": "Campeonato Colombiano", "nome_curto": "Colombiano", "tipo": "liga", "nivel": 1, "pais": "COL",
        "pais_nome": "Colômbia", "regiao": None, "confederacao": "CONMEBOL", "rotulo_painel": "Colombiano",
        "menu_painel": "Colômbia · 1ª divisão", "do_painel": "do Campeonato Colombiano", "o_painel": "o Campeonato Colombiano",
        "observacao": "1ª divisão colombiana de 1948 a 2025: um campeão por ano até 2001 (1989 sem campeão; 1995/96 e 1996/97 no "
                      "calendário europeu) e uma edição por torneio (Apertura e Finalización) de 2002 em diante. Jogos de 1948-1986, "
                      "1988-1990 e 1995/96 em diante; 1987 e 1991-1995 só com a tabela final e o campeão."},
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
            # (quadrangulares, hexagonais, octogonais etc. são grupos de pontos corridos, não mata-mata: CO-011)
            mata = eh_mata(f) and f != "Repechaje" and not re.match(r"(Quadrangula|Hexagonal|Octogonal|Pentagona|Triangula)", f)
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
                                             r["pts"], r["ajuste"], situacao(r, d["campeao"], r["pos"], e.temporada), r["fonte"],
                                             "; ".join(x for x in ("punição/bônus de pontos (tabela publicada)" if r["ajuste"] else "",
                                                                   BONUS.get(e.temporada, {}).get(r["clube"], "")) if x)])
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
                L["tabelas_publicadas"].append([e.temporada, nome_fase(tb["t"].fase, fases) if tb["fonte"].startswith("col") else "classificação final",
                                                tb["t"].grupo, r["pos"], r["nome"], r["clube"], r["j"], r["v"], r["e"], r["d"], r["gp"],
                                                r["gc"], r["pts"], f"RSSSF ({tb['fonte']}, linha {tb['t'].linha})"])
        # artilheiros: lista da RSSSF (até 2007); sem ela, a da Wikipédia em espanhol (CO-017, 2008 em diante, com o clube
        # tirado dos gols com autor); sem as duas, a contagem dos gols com autor (quando quase todos os gols têm autor)
        tops = TOPS.get(e.temporada)
        if tops:
            for jog, ctxt, ng in tops:
                L["artilheiros"].append([e.temporada, jog, clube(ctxt, e.ano_inicio) or ctxt, ng, "RSSSF (coltops.html)"])
        elif e.temporada in TOPS_ES:
            nomes, ng = TOPS_ES[e.temporada]
            autores_ed = Counter((r[2], r[1]) for r in L["gols"] if r[0].startswith(eid + "-") and r[5] != "contra")
            for jog in nomes:
                L["artilheiros"].append([e.temporada, jog, _clube_do_autor(jog, autores_ed), ng,
                                         "Wikipédia em espanhol (Categoría Primera A, Títulos por temporada)"])
        elif gols_ed and autor_ed >= 0.95 * gols_ed:
            cont = Counter((r[2], r[1]) for r in L["gols"] if r[0].startswith(eid + "-") and r[5] != "contra")
            if cont:
                topo = max(cont.values())
                for (jog, c), ng in sorted(cont.items()):
                    if ng == topo:
                        L["artilheiros"].append([e.temporada, jog, c, ng, "contagem dos gols com autor"])
        # edição
        final = d["final"]
        vice = final[1]["clube"] if len(final) > 1 and d["campeao"] else ""   # 1989: sem campeão, sem vice
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
        L["clubes"].append([c, prov, cid, "COL", "|".join(partes)])
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
            fase = tb["t"].fase if tb["fonte"].startswith("col") else ""
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
    linhas = ["# Campeonato Colombiano (1ª divisão) — coleta de dados", "",
              "Gerado por `python coleta/col-1/importar.py`. Pacote em `data/coleta/col-1/pacote/`.", "",
              f"**Edições:** {n_ed}, uma por título de campeão colombiano da 1ª divisão, de 1948 a 2025, como na lista de campeões "
              "da RSSSF (`colchamp.html`) e na Wikipédia em inglês. Até 2001 um campeão por ano: de 1968 em diante, Apertura e "
              "Finalización (e os quadrangulares, hexagonais e octogonais finais) são fases da edição anual. 1989 entra sem campeão "
              "(a fase final foi suspensa depois do assassinato do árbitro Álvaro Ortega); 1995 foi o torneio de transição e "
              "1995/96 e 1996/97 seguiram o calendário europeu. De 2002 em diante, Apertura e Finalización dão título cada um: "
              "uma edição por torneio (em 2020 só houve o Apertura).", "",
              f"**Edições sem jogos ({n_sem}):** 1987 e 1991-1995. Nenhuma fonte pública que achamos tem os jogos desses anos (a "
              "RSSSF e a Wikipédia trazem só as tabelas; o ogol tem as edições vazias). Elas entram com a tabela final da RSSSF "
              "como classificação e o campeão. Em 1986 a Wikipédia traz só parte do octogonal final.", "",
              "**Fora do pacote:** a Copa Colombia, a Superliga, as liguillas, o Torneo Adecuación 1997 e os jogos de promoção.", "",
              "**Fontes:** RSSSF (uma página por temporada, `data/coleta/col-1/rsssf/`: base de jogos de 1995/96 em diante, menos "
              "2011, 2012 e 2025, com fases, grupos, rodadas, datas e autores dos gols; as tabelas das páginas de todos os anos são "
              "a conferência); Wikipédia em espanhol (páginas \"Campeonato colombiano <ano>\" e \"Torneo Apertura <ano> (Colombia)\": "
              "jogos de 1948-1986, 1988-1990, 2011, 2012 e 2025, por rodada ou em tabela de confrontos, sem autores dos gols, e as "
              "finais com data e estádio); ESPN (liga `col.1`, 2005 em diante: hora, estádio, público, gols com minuto e cartões); "
              "Wikipédia em inglês (lista de campeões, segunda fonte do campeão). O ogol não tem os jogos da liga colombiana.", "",
              "**Clubes:** Deportes Caldas (campeão em 1950) entra como Once Caldas, como a RSSSF e o próprio clube contam; "
              "Atlético Municipal é o Atlético Nacional; Cristal Caldas, o Once Caldas; Itagüí, o Águilas Doradas; La Equidad, o "
              "Internacional de Bogotá (2025); Alianza Petrolera, o Alianza FC (2024). Homônimos de outros países levam a cidade: "
              "Libertad de Barranquilla, Universidad Nacional de Bogotá, Boca Juniors de Cali, Huracán de Medellín.", "",
              "**Regras:** o placar é o da RSSSF (ou da Wikipédia, nos anos dela). Jogo decidido no tribunal leva o placar dado "
              "(`awd`). Autores dos gols só entram quando a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os "
              "gols levam o minuto. Pontos por vitória: 2 até 1994 e 3 a partir de 1995 (as tabelas de vários anos têm pontos de "
              "bônus, que vão em `ajuste_pontos`).", "",
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
    from ler_rsssf import vices
    VICES.update(vices())
    from rebaixados_es import rebaixados
    _ano = {e.temporada: e.ano_inicio for e in EDICOES}
    for t_, ns in rebaixados().items():
        if t_ in _ano:
            REBAIXADOS[t_] = {clube(n, _ano[t_]) for n in ns} - {None}
    TOPS.update(artilheiros_rsssf())
    from goleadores_es import goleadores
    TOPS_ES.update(goleadores())
    BONUS.update(bonus_fase_final())
    eds = []
    for e in EDICOES:
        d = montar(e, cps)
        eds.append(d)
        print(f"{e.temporada:20s} {len(d['p']['jogos']):4d} jogos  campeão {d['campeao']}  divergências {len(d['difs'])}", flush=True)
    gravar(eds)
    relatorio(eds)
    print("pacote gravado em", PACOTE, "e relatório em", RELATORIO)
