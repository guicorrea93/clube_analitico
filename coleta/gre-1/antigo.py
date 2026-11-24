"""Era antiga do campeonato grego (1927/28 a 1958/59), no mesmo pacote gre-1: a fase nacional (Panhellenic
Championship) entre os campeões das ligas regionais. Os títulos são os reconhecidos pela federação (lista de campeões da
RSSSF, grkchamp.html, igual à contagem oficial).

Fonte: RSSSF (grkprehist.html), bloco "National Championship" de cada temporada:
  - matriz da fase nacional (sem data); célula com nota ("(1)") resolvida em NOTAS;
  - jogos com data ("18.5.1930 Pireas : Olympiakos S.F.P. - Aris A.S. 5:0"): as finais de ida e volta e a fase de
    1929/30;
  - jogos-desempate (título, 2º e 4º lugar) em EXTRAS;
  - tabela final (pontos, punições).
Conferência: tabela e matriz da fase final da Wikipédia (en), artigo "1930–31 Panhellenic Championship"; as fichas da
Wikipédia dão a data e a cidade dos jogos que a RSSSF traz sem data.
Ficam de fora as ligas regionais, a fase semifinal de 1955/56 (só as tabelas) e as eliminatórias inter-regionais do sul
(1953/54 a 1958/59), que classificavam para a fase nacional.

Uso: montar(tab, nomes, ocorr) acrescenta as edições ao `tab` do importador e devolve as linhas do resumo do relatório.
"""
from __future__ import annotations

import re
from collections import defaultdict

import clubes_gre as clubes
import rsssf_gre as rsssf
import wiki_gre
from edicoes import ANTIGAS, DADOS, nome_oficial, temporada, wiki_titulo

URL = "https://www.rsssf.org/tablesg/grkprehist.html"
# placar das células da matriz que remetem a uma nota: (ano, nota) -> (gols, gols, especial, observação); None = não jogado
NOTAS: dict[tuple, tuple | None] = {
    (1932, "1"): None,   # AEK x Aris: suspenso por tumulto, não repetido (não mudava o campeão)
    (1936, "1"): (2, 0, "awd", "vitória dada fora de campo (RSSSF: \"games awarded 2-0\")"),
    (1946, "1"): (2, 0, "awd", "vitória dada ao Atromitos Piraeus; o Makedonikos perdeu também 2 pontos (RSSSF)"),
    (1948, "1"): (2, 0, "awd", "2-0 em campo; resultado mantido fora de campo (RSSSF: \"originally 2:0 awarded 2-0\")"),
    (1948, "2"): (2, 0, "awd", "1-0 em campo; vitória dada fora de campo por 2-0 (RSSSF)"),
    (1950, "1"): (2, 0, "awd", "vitória dada ao Panionios fora de campo (RSSSF)"),
    (1956, "1"): (None, None, "awd", "o Ethnikos foi desclassificado nos 4 últimos jogos, acusado de profissionalismo (contato "
                                     "com Ferenc Puskás e Sándor Kocsis): derrota por 0-2 (RSSSF)"),
    (1956, "2"): (2, 0, "awd", "o Panargiakos não compareceu em Salônica: derrota por 0-2 (RSSSF)"),
    (1957, "9"): (0, 2, "awd", "suspenso; vitória dada ao Proodeftiki por 0-2 (RSSSF; na matriz, \"0-2~\")"),
    (1958, "1"): (0, 2, "awd", "abandonado com 0-0 e não terminado; vitória dada ao Panegialios por 0-2, e o Apollon Kalamarias "
                               "perdeu também 1 ponto (RSSSF)"),
}
# célula da matriz da RSSSF com erro de digitação: ano -> (texto, troca); a troca aponta para uma nota de NOTAS
CELULAS = {1957: ("0-2~2:2", "(9) 2:2")}
# jogo não disputado (nota None): (ano, nota) -> motivo
NAO_JOGADOS = {(1932, "1"): "AEK x Aris foi suspenso por tumulto e não foi repetido, porque não mudava o campeão (RSSSF)"}
# jogos-desempate fora da matriz: ano -> [(data, cidade, mandante, visitante, gols, gols, especial, observação)]
EXTRAS: dict[int, list[tuple]] = {
    1955: [(None, None, "Ethnikos Piraeus", "Panathinaikos", 2, 0, "awd",
            "desempate pelo 2º lugar: o Panathinaikos não compareceu (RSSSF: \"2:0 forfait\")"),
           (None, None, "PAOK", "Apollon Smyrnis", 1, 0, None, "desempate pelo 4º lugar (RSSSF)")],
    1956: [("1957-07-15", "Atenas", "Olympiacos", "Panathinaikos", 0, 0, None,
            "desempate pelo título, com prorrogação; no estádio do AEK (RSSSF)"),
           ("1957-07-18", "Atenas", "Olympiacos", "Panathinaikos", 1, 0, None,
            "desempate pelo título, jogo extra; gol de Mesologgitis aos 46 minutos; no estádio do AEK (RSSSF)")],
}
GOLS_EXTRAS = {(1956, "1957-07-18"): [("Olympiacos", "Mesologgitis", 46)]}
# temporadas decididas em final de ida e volta (sem grupo): o campeão pela soma dos placares
FINAIS = {1933, 1938, 1939}
# punição que a tabela da RSSSF não deixa tirar sozinha (linha com erro de digitação): (ano, clube) -> pontos
AJUSTES = {(1946, "Makedonikos"): -2}
EXPLICACOES: dict[int, list[str]] = {
    1932: ["a tabela da Wikipédia conta AEK 1-2 Aris (o placar na hora da suspensão); a RSSSF diz que o jogo não foi "
           "repetido nem contado, porque não mudava o campeão. Fica a RSSSF"],
    1935: ["a tabela da RSSSF não fecha nem com a matriz da própria RSSSF; com os placares da matriz da Wikipédia onde as duas "
           "discordam, os jogos fecham com a tabela da Wikipédia"],
    1946: ["a tabela da RSSSF dá ao Makedonikos 0-0-8 em 10 jogos (erro de digitação: são 10 derrotas) e 8 pontos (10 menos os "
           "2 de punição); a da Wikipédia dá AEK 0-1 Iraklis, e a RSSSF (matriz e tabela) 2-0. Fica a RSSSF"],
    1952: ["a tabela da RSSSF dá ao Aris 0-2-3 em 4 jogos (erro de digitação: são 0-1-3); a da Wikipédia fecha"],
    1953: ["a tabela da RSSSF dá 1 gol a menos ao Panathinaikos e ao Panachaiki; a da Wikipédia fecha com os jogos (3-0 no "
           "Panathinaikos x Panachaiki, da matriz da Wikipédia; a da RSSSF dá 2-0)"],
    1954: ["as tabelas da RSSSF e da Wikipédia concordam entre si e dão ao Apollon 2 gols pró a menos e ao Olympiacos Volos e "
           "ao Panetolikos 1 gol contra a menos; nenhuma das duas matrizes fecha com elas. Limite de fonte (seria preciso o "
           "jornal da época)"],
    1955: ["fase final: as tabelas da RSSSF e da Wikipédia concordam entre si (Olympiacos 13-9, Ethnikos 12-8, Panathinaikos "
           "15-11) e não fecham com a matriz da RSSSF, a única da fase final (a Wikipédia não tem matriz dela). Limite de fonte"],
    1957: ["a tabela da RSSSF dá ao Proodeftiki 10-3-9 (os jogos e a tabela da Wikipédia, 9-3-10) e 1 ponto a mais ao "
           "Olympiacos e ao Panionios; a da Wikipédia fecha com os jogos e dá as punições"],
}
CIDADES = {"pireas": "Pireu", "athens": "Atenas", "athina": "Atenas", "thessaloniki": "Salônica"}


def chave(nome: str, a: int) -> str:
    n = re.sub(r"^\s*\d+\s*\.\s*", "", nome).strip()
    c = clubes.esd(n, a)
    if c is None:
        raise SystemExit(f"{temporada(a)} (era antiga): nome da RSSSF sem cadastro: {nome}")
    return c


def pontos(tb: list[dict]) -> tuple[int, int, int]:
    """Sistema de pontos que fecha com a tabela (2-1-0 ou 3-2-1)."""
    melhor = max([(2, 1, 0), (3, 2, 1)], key=lambda p: sum(x["pontos"] == p[0] * x["vitorias"] + p[1] * x["empates"] +
                                                           p[2] * x["derrotas"] for x in tb))
    return melhor


def calcular(jogos: list[dict], pts) -> dict[str, list[int]]:
    t = defaultdict(lambda: [0] * 7)
    for j in jogos:
        if j["gm"] is None:
            continue
        for c, gp, gc in ((j["m"], j["gm"], j["gv"]), (j["v"], j["gv"], j["gm"])):
            x = t[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            k = 1 if gp > gc else 2 if gp == gc else 3
            x[k] += 1
            x[6] += pts[k - 1]
    return t


def bloco_nacional(a: int) -> str:
    t = rsssf.blocos(DADOS / "rsssf" / "grkprehist.html").get(temporada(a), "")
    i = max((m.start() for m in re.finditer(r"(?m)^\s*National Championship\.?\s*$", t)), default=-1)
    if i < 0:
        raise SystemExit(f"{temporada(a)}: sem \"National Championship\" na RSSSF")
    t = t[i:]
    j = t.find("Final Stage")   # 1955/56: a fase semifinal (só tabelas) fica de fora
    return t[j:] if j > 0 else t


def matriz(t: str, a: int) -> tuple[list[str], list[dict]]:
    """Matriz tolerante: a linha pode trazer a tabela depois das células (1927/28) e o nome grudado no primeiro placar."""
    if a in CELULAS:
        t = t.replace(*CELULAS[a])
    linhas = [l for l in t.split("\n") if re.search(r"\bXXX\b", l)]
    nomes, celulas = [], []
    for l in linhas:
        m = re.match(r"^\s*\d*\s*\.?\s*(.*?)\s*((?:XXX|\(\d+\)|\d+\s*[:;]\s*\d+)(?:\s+(?:XXX|\(\d+\)|\d+\s*[:;]\s*\d+))*)", l)
        nomes.append(m.group(1).strip())
        celulas.append(re.findall(r"XXX|\((\d+)\)|(\d+)\s*[:;]\s*(\d+)", m.group(2)))
    n = len(nomes)
    cl = [chave(x, a) for x in nomes]
    jogos = []
    for i in range(n):
        cel = celulas[i][:n]
        if len(cel) != n:
            raise SystemExit(f"{temporada(a)}: matriz da RSSSF com {len(cel)} células na linha de {nomes[i]}")
        for k, (nota, g1, g2) in enumerate(cel):
            if k == i:
                continue
            j = {"m": cl[i], "v": cl[k], "nm": nomes[i], "nv": nomes[k], "data": None, "cidade": None, "fonte": "RSSSF (matriz)"}
            if nota:
                r = NOTAS.get((a, nota), "falta")
                if r == "falta":
                    raise SystemExit(f"{temporada(a)}: nota ({nota}) da matriz da RSSSF sem placar em NOTAS: {cl[i]} x {cl[k]}")
                if r is None:
                    continue
                gm, gv, esp, obs = r
                if gm is None:   # desclassificação do Ethnikos (1956/57): 0-2 para ele, de qualquer lado
                    gm, gv = (0, 2) if cl[i] == "Ethnikos Piraeus" else (2, 0)
                j.update(gm=gm, gv=gv, especial=esp, obs=obs)
            elif g1 == "":
                continue
            else:
                j.update(gm=int(g1), gv=int(g2))
            jogos.append(j)
    return cl, jogos


def montar(tab: dict, nomes: dict, ocorr: dict) -> list[tuple]:
    camp = {}
    for m in re.finditer(r"^(\d{4})/\d{2}\s+(\S.*?)\s*$", rsssf.texto(DADOS / "rsssf" / "grkchamp.html"), re.M):
        if "not held" not in m.group(2):
            camp[int(m.group(1))] = clubes.esd(m.group(2).replace("�", "i").replace("ï", "i"), int(m.group(1)))
    linhas_rel = []
    for a in ANTIGAS:
        T = temporada(a)
        ocorr[a].extend(EXPLICACOES.get(a, []))
        t = bloco_nacional(a)
        # ---- jogos
        jogos = []
        if re.search(r"\bXXX\b", t):
            cl_mz, jogos = matriz(t, a)
        for d in rsssf.datados(t):
            m_, v_ = chave(d["m"], a), chave(d["v"], a)
            jogos.append({"m": m_, "v": v_, "nm": d["m"], "nv": d["v"], "gm": d["gm"], "gv": d["gv"], "data": d["data"],
                          "cidade": CIDADES.get(d["cidade"].lower(), d["cidade"]), "fonte": "RSSSF"})
        for data, cidade, m_, v_, gm, gv, esp, obs in EXTRAS.get(a, []):
            jogos.append({"m": m_, "v": v_, "nm": m_, "nv": v_, "gm": gm, "gv": gv, "data": data, "cidade": cidade,
                          "fonte": "RSSSF", "especial": esp, "obs": obs, "fase": "Desempate"})
        if (a, "1") in NAO_JOGADOS:
            ocorr[a].append(NAO_JOGADOS[(a, "1")])
        if not jogos:
            raise SystemExit(f"{T}: sem jogos na fase nacional da RSSSF")
        fase = "Final" if a in FINAIS else "Fase final"
        for j in jogos:
            j.setdefault("fase", fase)
            for lado in ("m", "v"):
                nomes[j[lado]][f"rsssf:{re.sub(r'^[0-9]+[.]', '', j['n' + lado]).strip()}"].add(a)
        principais = [j for j in jogos if j["fase"] != "Desempate"]
        clubes_ano = sorted({j[k] for j in principais for k in ("m", "v")})

        # ---- tabela da RSSSF (a primeira depois da matriz) e sistema de pontos
        tb = []
        for x in rsssf.tabela(t):
            if tb and x["posicao"] < tb[-1]["posicao"]:
                break
            x["clube"] = chave(x["nome"], a)
            tb.append(x)
        pts = pontos(tb) if tb else ((2, 1, 0) if a < 1945 else (3, 2, 1))
        calc = calcular(principais, pts)
        ajuste, conferidas, divergentes = {}, 0, 0
        if tb:
            erro = []
            for x in tb:
                c = calc.get(x["clube"])
                pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"]]
                if c and pub == c[:6] and x["pontos"] != c[6]:
                    ajuste[x["clube"]] = x["pontos"] - c[6]
                    ocorr[a].append(f"punição tirada da tabela da RSSSF: {x['clube']} {x['pontos'] - c[6]:+d} pontos")
                if not c or pub + [x["pontos"]] != c[:6] + [c[6] + ajuste.get(x["clube"], 0)]:
                    erro.append(f"{x['clube']} tabela {pub + [x['pontos']]} jogos {c[:6] + [c[6]] if c else None}")
                tab["tabelas_publicadas"].append({
                    "temporada": T, "fase": fase, "grupo": None, "posicao": x["posicao"], "nome_fonte": x["nome"],
                    "clube": clubes.exibicao(x["clube"]), "jogos": x["jogos"], "vitorias": x["vitorias"],
                    "empates": x["empates"], "derrotas": x["derrotas"], "gols_pro": x["gols_pro"],
                    "gols_contra": x["gols_contra"], "pontos": x["pontos"], "fonte": URL})
            if erro:
                divergentes += 1
                for e in erro:
                    ocorr[a].append(f"tabela da RSSSF x jogos — {e}")
            else:
                conferidas += 1

        # ---- Wikipédia: tabela e matriz da fase final (conferência) e datas das fichas
        wk = wiki_gre.ler((DADOS / "wikipedia" / f"{wiki_titulo(a)}.wiki").read_text(encoding="utf-8"))
        for j in wk["jogos"]:
            j["mc"] = clubes.esd(j["tm"] or "", a) or clubes.esd(j["nm"], a)
            j["vc"] = clubes.esd(j["tv"] or "", a) or clubes.esd(j["nv"], a)
        cs = set(clubes_ano)
        w_tb = None
        for tbw in wk["tabelas"]:
            conj = {clubes.esd(x["nome"], a) for x in tbw["times"]}
            if conj == cs:
                w_tb = tbw
        if w_tb:
            erro = []
            for x in w_tb["times"]:
                c_ = clubes.esd(x["nome"], a)
                nomes[c_][f"wikipedia:{x['nome']}"].add(a)
                v, e, d = x["vitorias"] or 0, x["empates"] or 0, x["derrotas"] or 0
                pub = [v + e + d, v, e, d, x["gols_pro"], x["gols_contra"]]
                if pub != calc[c_][:6]:
                    erro.append(f"{c_} tabela {pub} jogos {calc[c_][:6]}")
            if erro:
                divergentes += 1
                for e in erro:
                    ocorr[a].append(f"tabela da Wikipédia x jogos — {e}")
            else:
                conferidas += 1
        mz_w = defaultdict(list)
        for j in wk["jogos"]:   # só a fase final (as matrizes regionais e dos grupos semifinais ficam de fora)
            if j["fonte"] != "matriz" or not {j["mc"], j["vc"]} <= cs:
                continue
            if re.search(r"(?i)association|regional|group", " ".join(j["secao"])):
                continue
            if (j["gm"], j["gv"]) not in mz_w.get((j["mc"], j["vc"]), []):
                mz_w[(j["mc"], j["vc"])].append((j["gm"], j["gv"]))
        # placar em que a matriz da RSSSF e a da Wikipédia discordam: fica o que deixa os clubes mais perto das tabelas
        # publicadas (RSSSF e Wikipédia). Dois caminhos: jogo a jogo, ou a matriz inteira da Wikipédia e depois jogo a jogo;
        # fica o que fecha melhor
        pubs = []
        if tb:
            pubs.append({x["clube"]: [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"]]
                         for x in tb})
        if w_tb:
            pubs.append({clubes.esd(x["nome"], a): [(x["vitorias"] or 0) + (x["empates"] or 0) + (x["derrotas"] or 0),
                                                    x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"]]
                         for x in w_tb["times"]})

        def distancia(cs_):
            t_ = calcular(principais, pts)
            return sum(abs(t_[c][k] - p_[c][k]) for p_ in pubs for c in cs_ if c in p_ for k in range(6))
        originais = {id(j): (j["gm"], j["gv"]) for j in principais}
        mudaveis = [j for j in principais if not j.get("especial") and mz_w.get((j["m"], j["v"]))]

        def jogo_a_jogo():
            for j in mudaveis:
                for cand in mz_w[(j["m"], j["v"])]:
                    if cand == (j["gm"], j["gv"]):
                        break
                    antes, velho = distancia((j["m"], j["v"])), (j["gm"], j["gv"])
                    j["gm"], j["gv"] = cand
                    if distancia((j["m"], j["v"])) < antes:
                        break
                    j["gm"], j["gv"] = velho
        resultado = []
        for inteira in (False, True):
            for j in principais:
                j["gm"], j["gv"] = originais[id(j)]
            if inteira:
                for j in mudaveis:
                    if len(mz_w[(j["m"], j["v"])]) == 1:
                        j["gm"], j["gv"] = mz_w[(j["m"], j["v"])][0]
            jogo_a_jogo()
            resultado.append((distancia(cs) if pubs else 0, {id(j): (j["gm"], j["gv"]) for j in principais}))
        melhor = min(resultado, key=lambda r: r[0])[1]
        trocas = 0
        for j in principais:
            j["gm"], j["gv"] = melhor[id(j)]
            velho = originais[id(j)]
            if (j["gm"], j["gv"]) != velho:
                trocas += 1
                j["fonte"] = "RSSSF (matriz) + Wikipédia (placar)"
                j["obs"] = f"placar da matriz da Wikipédia; a da RSSSF dá {velho[0]}-{velho[1]}, que não fecha com as tabelas"
                ocorr[a].append(f"{j['m']} x {j['v']}: fica {j['gm']}-{j['gv']} (matriz da Wikipédia), que fecha com as "
                                f"tabelas; a matriz da RSSSF dá {velho[0]}-{velho[1]}")
        if trocas:   # a tabela muda com as trocas: confere de novo
            calc = calcular(principais, pts)
            tab["tabelas_publicadas"] = [x for x in tab["tabelas_publicadas"] if x["temporada"] != T]
            ocorr[a] = [o for o in ocorr[a] if not o.startswith(("tabela da RSSSF x jogos", "tabela da Wikipédia x jogos",
                                                                 "punição tirada"))]
            conferidas = divergentes = 0
            ajuste = {}
            for fonte_t, linhas_t in (("RSSSF", tb), ("Wikipédia", w_tb["times"] if w_tb else [])):
                erro = []
                for x in linhas_t:
                    c_ = x.get("clube") or clubes.esd(x["nome"], a)
                    v, e, d = x["vitorias"] or 0, x["empates"] or 0, x["derrotas"] or 0
                    pub = [v + e + d, v, e, d, x["gols_pro"], x["gols_contra"]]
                    if fonte_t == "RSSSF":
                        if pub == calc[c_][:6] and x["pontos"] != calc[c_][6]:
                            ajuste[c_] = x["pontos"] - calc[c_][6]
                        tab["tabelas_publicadas"].append({
                            "temporada": T, "fase": fase, "grupo": None, "posicao": x["posicao"], "nome_fonte": x["nome"],
                            "clube": clubes.exibicao(c_), "jogos": x["jogos"], "vitorias": v, "empates": e, "derrotas": d,
                            "gols_pro": x["gols_pro"], "gols_contra": x["gols_contra"], "pontos": x["pontos"], "fonte": URL})
                    if pub != calc[c_][:6]:
                        erro.append(f"{c_} tabela {pub} jogos {calc[c_][:6]}")
                if not linhas_t:
                    continue
                if erro:
                    divergentes += 1
                    ocorr[a] += [f"tabela da {fonte_t} x jogos — {e_}" for e_ in erro]
                else:
                    conferidas += 1
            for c_, v_ in ajuste.items():
                ocorr[a].append(f"punição tirada da tabela da RSSSF: {c_} {v_:+d} pontos")
        if mz_w:
            por_par = defaultdict(list)
            for j in principais:
                por_par[(j["m"], j["v"])].append((j["gm"], j["gv"]))
            for par, pl in mz_w.items():
                if sorted(pl) != sorted(por_par.get(par, [])):
                    ocorr[a].append(f"placar diferente na matriz da Wikipédia — {par[0]} x {par[1]}: RSSSF "
                                    f"{', '.join(f'{x}-{y}' for x, y in por_par.get(par, [])) or '—'}; Wikipédia "
                                    f"{', '.join(f'{x}-{y}' for x, y in pl)}")
        for w in wk["jogos"]:   # data e cidade das fichas da Wikipédia (fase nacional)
            if w["fonte"] != "ficha" or not w["data"] or not {w["mc"], w["vc"]} <= cs:
                continue
            j = next((j for j in jogos if (j["m"], j["v"], j["gm"], j["gv"]) == (w["mc"], w["vc"], w["gm"], w["gv"])
                      and not j["data"]), None)
            if j:
                j["data"], j["cidade"] = w["data"], j["cidade"] or w["local"]
                j["estadio"], j["arbitro"] = w["estadio"], w["arbitro"]
                j["fonte"] += " + Wikipédia (ficha)"
                if (len(w["gols_m"]), len(w["gols_v"])) == (j["gm"], j["gv"]):
                    j["gols"] = [(j["m"], n_, mi) for n_, mi in w["gols_m"]] + [(j["v"], n_, mi) for n_, mi in w["gols_v"]]

        # ---- punições: as da tabela da Wikipédia quando ela fecha com os jogos (o ajuste é explícito); senão, as da RSSSF
        # (diferença de pontos com os mesmos números), mais as de AJUSTES (linha da RSSSF com erro de digitação)
        calc = calcular(principais, pts)
        if w_tb and all([(x["vitorias"] or 0) + (x["empates"] or 0) + (x["derrotas"] or 0), x["vitorias"], x["empates"],
                         x["derrotas"], x["gols_pro"], x["gols_contra"]] == calc[clubes.esd(x["nome"], a)][:6]
                        for x in w_tb["times"]):
            novo = {clubes.esd(x["nome"], a): x["ajuste"] for x in w_tb["times"] if x["ajuste"]}
            if novo != ajuste:
                ocorr[a] = [o for o in ocorr[a] if not o.startswith("punição tirada")]
                ocorr[a] += [f"punição pela tabela da Wikipédia (que fecha com os jogos): {c_} {v_:+d} pontos"
                             for c_, v_ in novo.items()]
            ajuste = novo
        for (b_, c_), v_ in AJUSTES.items():
            if b_ == a:
                ajuste[c_] = v_
                ocorr[a].append(f"punição pela nota da RSSSF: {c_} {v_:+d} pontos")

        # ---- classificação final
        campeao = camp.get(a)
        if a in FINAIS:
            soma = calcular(principais, pts)
            vice = next(c for c in clubes_ano if c != campeao)
            ordem = [campeao, vice]
            fonte_cl = "RSSSF (final de ida e volta)"
        else:
            ordem = [x["clube"] for x in sorted(tb, key=lambda x: x["posicao"])] if tb else sorted(calc, key=lambda c: -calc[c][6])
            fonte_cl = "RSSSF (tabela da fase nacional)"
            soma = calc
        if set(ordem) != cs:
            raise SystemExit(f"{T}: classificação da era antiga com outros clubes: {sorted(set(ordem) ^ cs)}")
        if ordem[0] != campeao:
            ocorr[a].append(f"campeão diferente na lista de campeões da RSSSF: {campeao} (classificação: {ordem[0]})")
            if campeao in ordem:   # decidido em jogo-desempate
                ordem.remove(campeao)
                ordem.insert(0, campeao)
        for pos, c in enumerate(ordem, 1):
            j_, v_, e_, d_, gp, gc, p = soma[c]
            tab["classificacao_final"].append({
                "temporada": T, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
                "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": p + ajuste.get(c, 0), "ajuste_pontos": ajuste.get(c, 0),
                "situacao": "campeao" if pos == 1 else None, "fonte": fonte_cl,
                "observacao": "fase nacional entre os campeões regionais" + ("; campeão pela soma dos dois jogos da final"
                                                                             if a in FINAIS and pos == 1 else "")})

        # ---- partidas e gols
        jogos.sort(key=lambda j: (j["fase"] == "Desempate", j["data"] or "9999", j["m"]))
        gols_ano = autor = 0
        for i, j in enumerate(jogos, 1):
            pid = f"{a}-{i:04d}"
            tab["partidas"].append({
                "id": pid, "temporada": T, "fase": j["fase"], "grupo": None, "rodada": None, "data": j["data"], "hora": None,
                "mandante": clubes.exibicao(j["m"]), "visitante": clubes.exibicao(j["v"]), "gols_mandante": j["gm"],
                "gols_visitante": j["gv"], "penaltis_mandante": None, "penaltis_visitante": None,
                "resultado_especial": j.get("especial"), "estadio": j.get("estadio"), "cidade": j.get("cidade"),
                "publico": None, "fonte": j["fonte"], "fonte_id": None, "gols_texto": None,
                "observacao": j.get("obs") or ("desempate, fora da tabela" if j["fase"] == "Desempate" else None),
                "arbitro": j.get("arbitro")})
            gols_ano += j["gm"] + j["gv"]
            gl = j.get("gols") or [(c, n_, mi) for (b_, d_), lista in GOLS_EXTRAS.items() if b_ == a and d_ == j["data"]
                                   for c, n_, mi in lista]
            for c, n_, mi in gl:
                tab["gols"].append({"partida_id": pid, "clube": clubes.exibicao(c), "jogador": n_, "minuto": mi,
                                    "acrescimo": None, "tipo": "normal", "fonte": "Wikipédia (ficha)" if j.get("gols") else "RSSSF"})
            autor += len(gl)

        # ---- edição, fases, conferência
        n = len(clubes_ano)
        formato = ("final de ida e volta entre os campeões de Atenas/Pireu e de Salônica" if a in FINAIS else
                   f"fase nacional em pontos corridos entre {n} clubes (campeões e classificados das ligas regionais)")
        sist = "2 pontos por vitória" if pts == (2, 1, 0) else "3 pontos por vitória, 2 por empate e 1 por derrota"
        pun = "; ".join(f"{c} {v:+d} pontos" for c, v in ajuste.items())
        tab["edicoes"].append({"temporada": T, "ano_inicio": a, "ano_fim": a + 1, "nome_oficial": nome_oficial(a), "num_clubes": n,
                               "pontos_vitoria": pts[0], "formato": formato, "campeao": clubes.exibicao(campeao),
                               "vice": clubes.exibicao(ordem[1]), "fontes": "RSSSF + Wikipédia",
                               "observacao": "; ".join(x for x in ("só a fase nacional; as ligas regionais ficam de fora",
                                                                    sist if pts == (3, 2, 1) else "",
                                                                    f"punições: {pun}" if pun else "") if x)})
        tab["fases"].append({"temporada": T, "ordem": 1, "fase": fase, "tipo": "mata_mata" if a in FINAIS else "liga",
                             "num_grupos": None, "formato_serie": "ida_volta" if a in FINAIS else "pontos_corridos",
                             "criterio": "soma dos placares" if a in FINAIS else "pontos"})
        if any(j["fase"] == "Desempate" for j in jogos):
            tab["fases"].append({"temporada": T, "ordem": 2, "fase": "Desempate", "tipo": "mata_mata", "num_grupos": None,
                                 "formato_serie": "jogo_unico", "criterio": "jogo-desempate, fora da tabela"})
        tab["conferencia"].append({"temporada": T, "jogos": len(jogos), "jogos_esperados": None, "tabelas_conferidas": conferidas,
                                   "tabelas_divergentes": divergentes, "gols": gols_ano, "gols_com_autor": autor,
                                   "observacao": f"campeão {clubes.exibicao(campeao)} (RSSSF, lista de campeões); só a fase nacional"})
        linhas_rel.append((T, "RSSSF + Wikipédia", n, len(jogos), gols_ano, autor, conferidas, divergentes,
                           clubes.exibicao(campeao), pun))
        print(f"{T} (era antiga): {len(jogos)} jogos, {n} clubes, tabelas {conferidas} ok / {divergentes} div, campeão "
              f"{clubes.exibicao(campeao)}", flush=True)
    return linhas_rel
