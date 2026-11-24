"""Junta as fontes da 1ª divisão argentina e grava o pacote em data/coleta/arg-1/pacote/ e o relatório em docs/coleta/arg-1.md.

Fontes, na ordem em que entram:
- RSSSF (ler_rsssf.py): base de jogos, fases, grupos, rodadas, datas, local e autores dos gols, de 1891 a 2025.
  As tabelas publicadas na página da temporada e no índice por década (arghist) são a conferência.
- ogol (ogol.py): rodada e data dos jogos que ele tem (1931 em diante, com buracos) e o nome de cada clube no ogol.
- ESPN (espn_arg.py, liga arg.1, 2001 em diante): hora, estádio, público, gols com minuto e cartões.

Uso: python coleta/arg-1/importar.py
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
from clubes_arg import CLUBES, clube  # noqa: E402
from conferir import conferir_tabelas, preparar, soma  # noqa: E402
from edicoes import EDICOES, PACOTE, RELATORIO, SLUG, Edicao  # noqa: E402
from explicacoes import CORRIGE, EXPLICACOES, EXTRAS  # noqa: E402
from ler_rsssf import campeoes  # noqa: E402
from rsssf_sul import chave  # noqa: E402

# ordem das fases (quanto maior, mais longe o clube chegou)
NIVEL_FASE = {"": 0, "Apertura": 0, "Clausura": 0, "Grupo do rebaixamento": 0, "Desempate do rebaixamento": 0,
              "Desempate do 2º lugar": 1, "Fase final": 2, "Oitavas de final": 3, "Quartas de final": 4, "Semifinal": 5,
              "Final": 6, "Desempate do título": 6, "Desempate do 1º turno": 0, "Desempate do grupo": 1, "Disputa do 3º lugar": 5}
WIKI: dict[str, str] = {}
TOPS: dict[str, list] = {}
TOPS_FONTE: dict[str, str] = {}
# artilheiros corrigidos pela lista da Wikipédia em espanhol ("Anexo:Goleadores de la Primera División de Argentina"), onde a
# argtops erra ou não tem (AR-027 a AR-030): temporada -> [(jogador, clube, gols)]
_ES = "Wikipédia em espanhol (Anexo:Goleadores de la Primera División de Argentina)"
ARTILHEIROS_CORRIGE: dict[str, list[tuple[str, str, int]]] = {
    "1894": [("James D. Gifford", "Flores Athletic", 7)],                         # a argtops dá 4
    "1932 Asociación": [("Juan Irurieta", "All Boys", 23)],                        # a argtops dá 24
    "1934 Asociación": [("Pedro Maseda", "Argentino de Quilmes", 16), ("Domingo Tarasconi", "General San Martín", 16)],
    "1936 Copa de Honor": [("Alberto Zozaya", "Estudiantes", 16)],                 # a argtops soma as duas copas de 1936
    "1936 Campeonato": [("Evaristo Barrera", "Racing Club", 19)],
    "1988/89": [("Oscar Dertycia", "Argentinos Juniors", 20), ("Néstor Gorosito", "San Lorenzo", 20)],
    "1997/98 Clausura": [("Roberto Sosa", "Gimnasia La Plata", 16)],               # a argtops dá 17
    "2025 Apertura": [("Tomás Molina", "Argentinos Juniors", 10)],                 # 4 gols do torneio sem autor
}
MATA = {"Oitavas de final", "Quartas de final", "Semifinal", "Final", "Desempate do título", "Desempate do 2º lugar", "Desempate do rebaixamento",
        "Desempate do 1º turno", "Desempate do grupo", "Disputa do 3º lugar"}


def nome_fase(f: str, fases: set[str]) -> str:
    if f:
        return f
    return "Primeira fase" if fases & {"Fase final", "Oitavas de final", "Quartas de final", "Semifinal", "Final"} else "Fase única"


def id_edicao(e: Edicao) -> str:
    return re.sub(r"[^0-9a-z]+", "-", chave(e.temporada))


def especial(esp: str) -> str:
    return {"wo_m": "wo", "wo_v": "wo", "awd": "awd", "abd": "abd", "anulado": "n/p", "n/p": "n/p"}.get(esp, "")


# AR-022: o leitor comum erra o ano em ~3.500 jogos de 25 edições (a 1ª data <= junho numa edição que cruza o ano vai para
# ano_fim; o ano escrito numa linha vale para os jogos seguintes; virada dez -> jan com jogos adiados). Regra validada pela
# revisão (revisao/QU/sim_ano.py): âncora = ano_inicio (ano_fim no Clausura/Final/Campeonato de temporada dividida); janela
# = [1º jogo da página - 30 dias, +365 dias] (fim explícito nas temporadas longas); cada jogo recebe o ano que põe dia/mês
# na janela; se couber em dois, o mais perto do jogo anterior na ordem da página.
ACERTA_ANO = {"1919 Asociación", "1919 Amateurs", "1924 Asociación", "1925 Asociación", "1927", "1928", "1929", "1930", "1931 Liga",
              "1937", "1977 Nacional", "1981 Nacional", "1985/86", "1986/87", "1989/90", "1999/00 Apertura", "2003/04 Apertura",
              "2006/07 Apertura", "2007/08 Apertura", "2010/11 Apertura", "2011/12 Apertura", "2012/13 Inicial", "2017/18",
              "2018/19", "2019/20"}
FIM_TEMPORADA = {"1927": "1928-01-31", "1928": "1929-07-31", "1930": "1931-04-30", "1937": "1939-02-28"}   # (historiadeboca)
# ano escrito na própria linha do jogo (QU-002): 1937, desempate do 1º turno River 5-3 Boca, "[11 Feb 1939]"
# AR-024: 2005/06 Apertura Newell's x Estudiantes escrito "Sep 31" na página; a ESPN (187600) dá 30/09/2005 às 20h locais
DATA_FIXA = {("1937", "arg37:223"): "1939-02-11", ("2005/06 Apertura", "arg06:231"): "2005-09-30"}


def acerta_ano(e: Edicao, jogos: list[dict]) -> None:
    from datetime import date, timedelta
    for j in jogos:
        if j["j"] and (e.temporada, j["j"].texto) in DATA_FIXA:
            j["j"].data = DATA_FIXA[(e.temporada, j["j"].texto)]
    if e.temporada not in ACERTA_ANO:
        return
    pags: list[str] = []
    da_pagina = [j for j in jogos if j["j"] and j["j"].data and not j["j"].texto.startswith(("espn", "wiki", "ogol"))]
    for j in da_pagina:
        pg = j["j"].texto.split(":")[0]
        if pg not in pags:
            pags.append(pg)
    da_pagina.sort(key=lambda j: (pags.index(j["j"].texto.split(":")[0]), int(j["j"].texto.split(":")[1])))
    if not da_pagina:
        return
    anc = e.ano_fim if ("/" in e.temporada and re.search(r"Clausura|\bFinal$|Campeonato$", e.temporada)) else e.ano_inicio
    d0 = da_pagina[0]["j"].data
    ini = date(anc, int(d0[5:7]), int(d0[8:10])) - timedelta(days=30)
    fim = date.fromisoformat(FIM_TEMPORADA[e.temporada]) if e.temporada in FIM_TEMPORADA else ini + timedelta(days=365)
    prev = None
    for j in da_pagina:
        x = j["j"]
        if (e.temporada, x.texto) in DATA_FIXA:
            x.data = DATA_FIXA[(e.temporada, x.texto)]
            continue
        mo, di = int(x.data[5:7]), int(x.data[8:10])
        cands = []
        for y in range(ini.year, fim.year + 1):
            try:
                w = date(y, mo, di)
            except ValueError:
                continue
            if ini <= w <= fim:
                cands.append(w)
        if not cands:
            continue
        z = cands[0] if len(cands) == 1 or prev is None else min(cands, key=lambda w: (abs((w - prev).days), w.weekday() < 5))
        prev = z
        x.data = z.isoformat() + x.data[10:]


def montar(e: Edicao, cps: dict[str, list[str]]) -> dict:
    p = preparar(e)
    acerta_ano(e, p["jogos"])
    log: list[str] = list(p["log"])
    for x in EXTRAS.get(e.temporada, []):
        p["jogos"].append({"m": x["mandante"], "v": x["visitante"], "gm": x["gm"], "gv": x["gv"], "fase": x.get("fase", ""),
                           "grupo": "", "esp": "", "extra": x, "j": None})
    for j in [j for j in p["jogos"] if not j["m"] or not j["v"]]:
        log.append(f"linha lida como jogo e descartada (clube não reconhecido): {j['j'].texto} «{j['j'].mandante} x {j['j'].visitante}»")
        p["jogos"].remove(j)
    difs = conferir_tabelas(p)
    jogos = p["jogos"]
    fases = {j["fase"] for j in jogos}
    # campanha de cada clube (resultado oficial; W.O. vale vitória) e fase mais longe
    clubes = sorted({x for j in jogos for x in (j["m"], j["v"]) if x})
    if e.soma_de:   # tabela anual sem jogos próprios: os clubes são os da tabela
        clubes = sorted({r["clube"] for tb in p["tabelas"] for r in tb["linhas"] if r["clube"]})
    calc = soma(jogos, set(clubes))
    nivel: dict[str, int] = defaultdict(int)
    for j in jogos:
        for x in (j["m"], j["v"]):
            nivel[x] = max(nivel[x], NIVEL_FASE.get(j["fase"], 0))
    # campeão pela lista da RSSSF (argchamp.html)
    camp_txt = e.campeao_rsssf or ((cps.get(str(e.ano_inicio)) or [""])[0])
    campeao = clube(camp_txt, e.ano_inicio) if camp_txt else None
    if not campeao and camp_txt:
        log.append(f"campeão da lista da RSSSF não reconhecido: {camp_txt}")
    final = classificacao(e, p, calc, nivel, campeao, clubes)
    podio_oficial(e, final, campeao, log)
    return {"e": e, "p": p, "difs": difs, "log": log, "clubes": clubes, "campeao": campeao, "camp_txt": camp_txt,
            "final": final, "fases": fases}


# edições em que a classificação é a tabela publicada, mesmo sem fechar com os jogos: 1912 Asociación sem os clubes que foram para a FAF; nas outras, W.O. e jogos anulados que a página conta de outro jeito
# 1989/90 e 1997/98 Apertura: jogos com derrota para os dois clubes e punições de pontos (AR-004, AR-014)
# AR-020: edições em que a fase de grupos vale pela tabela publicada (pontos dados por W.O. que não estão na lista de jogos)
FASE_PELA_TABELA = {"1929": ""}   # "" = 1ª fase
# AR-020: clube com jogos (anulados) que a tabela publicada não traz entra no fim (1908: Nacional, eliminado depois de 2 jogos)
FORA_DA_TABELA = {"1908"}
TABELA_OFICIAL = {"1896", "1908", "1912 Asociación", "1919 Amateurs", "1926 Asociación", "1931 Liga", "1965",
                  "1989/90", "1997/98 Apertura", "1988/89"}   # 1988/89: 3 pela vitória, 2 ou 1 no empate decidido nos pênaltis (AR-017)

# grafias da lista oficial (Wikipédia em inglês) que as REGRAS não pegam
_NOME_LISTA = {"Flores": "Flores Athletic", "Rosario AC": "Rosario Athletic", "Argentino (Q)": "Argentino de Quilmes"}
VICES: dict[str, str] = {}
TERCEIROS: dict[str, str] = {}


def rebaixados_por_temporada(eds: list[dict]) -> None:
    """AR-021: cada rebaixado da Wikipédia em espanhol vai para a última edição da temporada em que jogou ("2010-11": o
    Clausura; "M 1970": o Metropolitano). A temporada ainda em andamento (só o Apertura de 2026) fica de fora."""
    from rebaixados_es import rebaixados
    jogou = {d["e"].temporada: set(d["clubes"]) | {r["clube"] for r in d["final"]} for d in eds}
    for (temp, metro), nomes in rebaixados().items():
        if temp == "2026":
            continue
        if "-" in temp:
            eds_t = [d["e"] for d in eds if d["e"].temporada.startswith(temp.replace("-", "/"))]
        elif metro:
            eds_t = [d["e"] for d in eds if d["e"].temporada == f"{temp} Metropolitano"]
        else:
            eds_t = [d["e"] for d in eds if d["e"].ano_inicio == int(temp) and "/" not in d["e"].temporada]
        for nome, alvo in nomes:
            ano = eds_t[0].ano_inicio if eds_t else int(temp[:4])
            c = _NOME_ES.get(nome) or clube(nome, ano) or clube(alvo, ano)
            ed = next((x for x in reversed(eds_t) if c in jogou[x.temporada]), None)
            if ed:
                REBAIXADOS[ed.temporada].add(c)
            else:
                print(f"rebaixado sem edição: {temp} {nome} ({c})")


def podio_oficial(e: Edicao, final: list[dict], campeao: str | None, log: list[str]) -> None:
    """Vice e 3º da lista oficial (Wikipédia em inglês, a mesma do campeão) logo abaixo do campeão (AR-002 a AR-013,
    AR-015): a tabela lida às vezes não fecha (jogo a mais ou a menos, punição, desempate fora da tabela).
    1891 fica como está: a lista dá o título dividido (Saint Andrew's e Old Caledonians) e o clube seguinte como "vice";
    pela D-07 (b) só o Saint Andrew's é campeão, e o Old Caledonians, que perdeu o desempate, é o vice."""
    if e.temporada == "1891":
        return
    for pos, lista in ((2, VICES), (3, TERCEIROS)):
        txt = lista.get(e.temporada)
        if not txt or not campeao or len(final) < pos:
            continue
        c = _NOME_LISTA.get(txt) or clube(txt, e.ano_inicio)
        r = next((r for r in final if r["clube"] == c), None)
        if r is None:
            log.append(f"{'vice' if pos == 2 else '3º'} da lista oficial ({txt}) não está na classificação")
            continue
        if final.index(r) != pos - 1 and final.index(r) >= pos - 1:
            log.append(f"{'vice' if pos == 2 else '3º'} pela lista oficial: {c} (a tabela o punha em {final.index(r) + 1}º)")
            final.remove(r)
            final.insert(pos - 1, r)
    for k, r in enumerate(final, 1):
        r["pos"] = k


def artilheiros_rsssf() -> dict[str, list[tuple[str, str, int]]]:
    """argtops.html: temporada do pacote -> [(jogador, clube como na página, gols)]. O código ao lado do ano diz o torneio
    (AAF Asociación, FAF Federación, AAm Amateurs, LAF Liga, Met/Nac, Ape/Cla, Ini/Fin). 1936 fica de fora: a lista soma
    a Copa de Honor e a Copa Campeonato."""
    from ler_rsssf import linhas
    cod = {"AAF": "Asociación", "FAF": "Federación", "AAm": "Amateurs", "LAF": "Liga", "Met": "Metropolitano", "Nac": "Nacional",
           "Ape": "Apertura", "Cla": "Clausura", "Ini": "Inicial", "Fin": "Final"}
    saida: dict[str, list] = defaultdict(list)
    ano = sig = None
    for l in linhas("argtops"):
        m = re.match(r"^(\d{4}(?:/\d{2})?)?\s+(?:(AAF|FAF|AAm|LAF|Met|Nac|Ape|Cla|Ini|Fin)\s+)?(\S.*?,.*?)\s{2,}(\S.*?)\s+(\d{1,2})\s*$", l)
        if not m:
            if re.match(r"^\d{4}", l):
                ano, sig = None, None
            continue
        if m.group(1):
            ano, sig = m.group(1), None
        if m.group(2):
            sig = m.group(2)
        if not ano or ano.startswith("1936"):
            continue
        sobrenome, _, nome = m.group(3).partition(",")
        temp = ano if not sig else f"{ano} {cod[sig]}"
        saida[temp].append((f"{nome.strip()} {sobrenome.strip()}".strip(), m.group(4).strip(), int(m.group(5))))
    return saida


def classificacao(e: Edicao, p: dict, calc: dict, nivel: dict, campeao: str | None, clubes: list[str]) -> list[dict]:
    """Classificação final: a tabela publicada que traz todos os clubes e fecha com os jogos (ordem oficial, pontos com
    punições); sem ela, calculada (fase alcançada, pontos, saldo, gols pró). O campeão da lista oficial fica em 1º."""
    pv = e.pontos_vitoria
    pub = next((tb for tb in p["tabelas"] if not tb.get("acumulada") and tb.get("ok") and
                {r["clube"] for r in tb["linhas"]} == set(clubes)), None)
    if e.temporada in TABELA_OFICIAL:   # jogos incompletos ou que não fecham: vale a tabela publicada (AR-006, AR-010, AR-020)
        cands = p["tabelas"]   # (com só parte dos jogos, a tabela completa parece "acumulada" para a conferência)
        pub = max(cands, key=lambda tb: (len(tb["linhas"]), sum(r["j"] or 0 for r in tb["linhas"])), default=pub)
    linhas = []
    if pub:
        for k, r in enumerate(pub["linhas"], 1):
            pts_calc = r["v"] * pv + r["e"]
            linhas.append({"clube": r["clube"], "j": r["j"], "v": r["v"], "e": r["e"], "d": r["d"], "gp": r["gp"], "gc": r["gc"],
                           "pts": r["pts"], "ajuste": r["pts"] - pts_calc if e.temporada != "1988/89" else 0,
                           "obs": r.get("obs", ""), "fonte": f"RSSSF ({pub['fonte']})"})
        # a ordem publicada vale; empates sem número herdam a posição de cima
        for c in sorted(set(clubes) - {r["clube"] for r in linhas} if e.temporada in FORA_DA_TABELA else ()):
            x = calc.get(c, [0] * 6)
            linhas.append({"clube": c, "j": x[0], "v": x[1], "e": x[2], "d": x[3], "gp": x[4], "gc": x[5], "pts": x[1] * pv + x[2],
                           "ajuste": 0, "obs": "", "fonte": "calculada (fora da tabela publicada: jogos anulados)"})
    else:
        fase_tb = FASE_PELA_TABELA.get(e.temporada)
        if fase_tb is not None:   # AR-020: números da fase pelas tabelas publicadas (com os W.O.) mais os jogos das outras fases
            da_tabela: dict[str, dict] = {}
            for tb in p["tabelas"]:
                if tb["t"].fase == fase_tb:
                    for r in tb["linhas"]:
                        if r["clube"] and (r["clube"] not in da_tabela or (r["j"] or 0) > (da_tabela[r["clube"]]["j"] or 0)):
                            da_tabela[r["clube"]] = r
            outros = soma([j for j in p["jogos"] if j["fase"] != fase_tb], set(clubes))
        for c in clubes:
            x = calc.get(c, [0] * 6)
            pts, fonte = x[1] * pv + x[2], "calculada (fase alcançada, pontos, saldo, gols pró)"
            if fase_tb is not None and c in da_tabela:
                r, o = da_tabela[c], outros.get(c, [0] * 6)
                x = [r["j"] + o[0], r["v"] + o[1], r["e"] + o[2], r["d"] + o[3], r["gp"] + o[4], r["gc"] + o[5]]
                pts = r["pts"] + o[1] * pv + o[2]
                fonte = "calculada: tabelas publicadas da 1ª fase (com os W.O.) mais os jogos das outras fases"
            linhas.append({"clube": c, "j": x[0], "v": x[1], "e": x[2], "d": x[3], "gp": x[4], "gc": x[5], "pts": pts,
                           "ajuste": 0, "obs": "", "fonte": fonte})
        linhas.sort(key=lambda r: (-nivel[r["clube"]], -r["pts"], -(r["gp"] - r["gc"]), -r["gp"], r["clube"]))
    if campeao and linhas and linhas[0]["clube"] != campeao and any(r["clube"] == campeao for r in linhas):
        c = next(r for r in linhas if r["clube"] == campeao)
        linhas.remove(c)
        linhas.insert(0, c)
    for k, r in enumerate(linhas, 1):
        r["pos"] = k
    return linhas


# AR-021: rebaixados por temporada pela Wikipédia em espanhol (rebaixados_es.py), na última edição da temporada em que o clube
# jogou; a nota "Relegated" da tabela continua valendo nas outras
REBAIXADOS: dict[str, set[str]] = defaultdict(set)
_NOME_ES: dict[str, str] = {}   # grafias da es que as REGRAS não pegam (até aqui, nenhuma)


def situacao(r: dict, campeao: str | None, k: int, temporada: str = "") -> str:
    if r["clube"] == campeao:
        return "campeao"
    if k == 2:
        return "vice"
    if r["clube"] in REBAIXADOS.get(temporada, ()):
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
        "slug": SLUG, "nome": "Campeonato Argentino", "nome_curto": "Argentino", "tipo": "liga", "nivel": 1, "pais": "ARG",
        "pais_nome": "Argentina", "regiao": None, "confederacao": "CONMEBOL", "rotulo_painel": "Argentino",
        "menu_painel": "Argentina · 1ª divisão", "do_painel": "do Campeonato Argentino", "o_painel": "o Campeonato Argentino",
        "observacao": "1ª divisão argentina de 1891 a 2025: uma edição por torneio que deu título de campeão (ligas rivais de "
                      "1912-1914, 1919-1926 e 1931-1934; Copa de Honor, Campeonato e Copa de Oro em 1936; Metropolitano e Nacional "
                      "de 1967 a 1985; Apertura e Clausura de 1991/92 a 2013/14 e em 2025). Sem as copas da liga (2019-2024), a "
                      "Copa Campeonato 2013/14, os torneios de reclassificação e as liguillas, que não davam o título."},
        ensure_ascii=False, indent=1), encoding="utf-8")
    L = defaultdict(list)
    nomes_fonte: dict[str, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
    usados: set[str] = set()
    so_tabela: dict[str, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
    for d in eds:
        e, p = d["e"], d["p"]
        eid = id_edicao(e)
        fases = d["fases"]
        ordem_f = sorted(fases, key=lambda f: (NIVEL_FASE.get(f, 0) if f not in ("Apertura", "Clausura") else (0 if f == "Apertura" else 0.5),
                                               min((j["j"].linha for j in p["jogos"] if j["fase"] == f and j["j"]), default=0)))
        for k, f in enumerate(ordem_f, 1):
            js = [j for j in p["jogos"] if j["fase"] == f]
            grupos = sorted({j["grupo"] for j in js if j["grupo"] and j["grupo"] != "Interzonal"})
            mata = f in MATA
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
                nomes_fonte[j["m"]][f"rsssf:{x.mandante}"].append(e.ano_inicio)
                nomes_fonte[j["v"]][f"rsssf:{x.visitante}"].append(e.ano_inicio)
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
            fonte_id = f"rsssf:{x.texto}" if x else ex["fonte_id"]
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
                if k in es.get("adiado", ()) and data != loc.date().isoformat():   # QU-003: jogo adiado, vale a data da ESPN
                    obs.append(f"jogo adiado: data da ESPN (a página da RSSSF o põe na rodada original{f', {data}' if data else ''})")
                    data = loc.date().isoformat()
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
                                  "RSSSF", fonte_id,
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
                L["tabelas_publicadas"].append([e.temporada, nome_fase(tb["t"].fase, fases) if tb["fonte"].startswith("arg") and
                                                not tb["fonte"].startswith("arghist") else "classificação final",
                                                tb["t"].grupo, r["pos"], r["nome"], r["clube"], r["j"], r["v"], r["e"], r["d"], r["gp"],
                                                r["gc"], r["pts"], f"RSSSF ({tb['fonte']}, linha {tb['t'].linha})"])
        # artilheiros: lista da RSSSF; sem ela, a contagem dos gols com autor (quando quase todos os gols têm autor)
        tops = TOPS.get(e.temporada)
        if tops:
            for jog, ctxt, ng in tops:
                L["artilheiros"].append([e.temporada, jog, clube(ctxt, e.ano_inicio) or ctxt, ng, TOPS_FONTE.get(e.temporada, "RSSSF (argtops.html)")])
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
                             ("tabela anual (soma das fases de grupos do Apertura e do Clausura)" if e.soma_de else
                              formato(ordem_f, L["fases"], e.temporada)), d["campeao"] or "", vice, "RSSSF", e.obs])
        n_tab = len(vistas)
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
        L["clubes"].append([c, prov, cid, "ARG", "|".join(partes)])
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
    if d["e"].soma_de:
        return 0
    for tb in p["tabelas"]:
        if tb.get("ok") is not None and not (tb.get("acumulada") or tb.get("parcial") or tb.get("desempate")) and                 {r["clube"] for r in tb["linhas"]} == set(d["clubes"]):
            fase = tb["t"].fase if tb["fonte"].startswith("arg") and not tb["fonte"].startswith("arghist") else ""
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
    linhas = ["# Campeonato Argentino (1ª divisão) — coleta de dados", "",
              "Gerado por `python coleta/arg-1/importar.py`. Pacote em `data/coleta/arg-1/pacote/`.", "",
              "**Edições:** 196: 195 torneios que deram título de campeão argentino da 1ª divisão, de 1891 a 2025, como na lista de "
              "campeões da RSSSF (`argchamp.html`) e na Wikipédia em inglês (*List of Argentine football champions*): as duas trazem "
              "os mesmos 195 campeões. Ano com mais de um campeão oficial vira uma edição por torneio: ligas rivais (Asociación x "
              "Federación em 1912-1914, Asociación x Amateurs em 1919-1926, Liga profissional x Asociación amadora em 1931-1934), "
              "Copa de Honor, Copa Campeonato e Copa de Oro em 1936, Metropolitano e Nacional de 1967 a 1985, Apertura e Clausura de "
              "1991/92 a 2011/12 e em 2025, Inicial, Final e o jogo do Campeonato 2012/13, mais a tabela anual de 2025.", "",
              "**Fora do pacote:** as copas da liga (Copa de la Superliga 2019, Copa de la Liga Profesional 2020-2024) e a Copa "
              "Campeonato 2013/14, que a AFA e a RSSSF tratam como copas; os torneios de reclassificação, os promocionais, as "
              "liguillas pré-Libertadores e os jogos de promoção contra clubes da 2ª divisão.", "",
              "**Tabela anual de 2025:** o Rosario Central foi proclamado \"campeão da Liga\" pela AFA em 20/11/2025. Entra como a "
              "edição \"2025 Liga\", sem jogos próprios (decisão do Guilherme, 20/11/2026): a classificação é a tabela anual da RSSSF, "
              "que fecha com a soma das fases de grupos do Apertura e do Clausura.", "",
              "**Fontes:** RSSSF (uma página por temporada, `data/coleta/arg-1/rsssf/`: base de jogos, fases, grupos, rodadas, "
              "datas, local e autores dos gols; as tabelas da própria página e as dos índices por década, `arghist-*.html`, são a "
              "conferência); ogol (calendários de 1931 em diante, com muitos anos vazios: rodada e data que faltam, conferência de "
              "placar e o nome de cada clube no ogol); ESPN (liga `arg.1`, 2001 em diante: hora, estádio, público, gols com minuto e "
              "cartões); Wikipédia (lista de campeões, segunda fonte do campeão).", "",
              "**Regras:** o placar é o da RSSSF; o ogol só completa rodada e data e entra como conferência. Jogo decidido no tribunal "
              "leva o placar dado (`awd`) ou, sem placar, a vitória (`wo`, com o placar de campo na observação). Jogo suspenso e "
              "repetido fica como `abd` e não conta; suspenso e continuado depois vira um jogo só. Autores dos gols só entram quando "
              "a soma bate com o placar (senão ficam em `gols_texto`). Com a ESPN, os gols levam o minuto. Pontos por vitória: 2 até "
              "1994/95 e 3 a partir do Apertura 1995 (em 1988/89, 3 pela vitória e 2 ou 1 no empate decidido nos pênaltis).", "",
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
    for t_, v_ in ARTILHEIROS_CORRIGE.items():
        TOPS[t_], TOPS_FONTE[t_] = v_, _ES
    eds = []
    for e in EDICOES:
        d = montar(e, cps)
        eds.append(d)
        print(f"{e.temporada:20s} {len(d['p']['jogos']):4d} jogos  campeão {d['campeao']}  divergências {len(d['difs'])}", flush=True)
    rebaixados_por_temporada(eds)
    gravar(eds)
    relatorio(eds)
    print("pacote gravado em", PACOTE, "e relatório em", RELATORIO)
