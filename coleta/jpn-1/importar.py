"""Monta o pacote do Campeonato Japonês (jpn-1) em data/coleta/jpn-1/pacote/ e o relatório docs/coleta/jpn-1.md.

- JSL (1965 a 1991/92): páginas da RSSSF (ler_jsl.py). Todos os jogos vêm da tabela de confrontos (sem data nem rodada;
  em 1988/89 a página traz também as rodadas com data). A classificação é a tabela final publicada.
- J1 (1993 a 2025): J.League Data Site, o site oficial de dados da J.League (ler_jleague.py): todos os jogos com rodada,
  data, hora, estádio, público, árbitro, autores dos gols e cartões; as tabelas oficiais de cada turno e a anual são a
  conferência e a classificação.
- Campeão e vice conferidos com a lista da Wikipédia em inglês (campeoes_wiki.py); placares de 2006 em diante
  conferidos com a ESPN (liga jpn.1).

Uso: python coleta/jpn-1/importar.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import ler_jleague  # noqa: E402
import ler_jsl  # noqa: E402
from campeoes_wiki import artilheiros, podio  # noqa: E402
from clubes_jpn import CLUBES, clube  # noqa: E402
from edicoes import EDICOES, TURNOS, Edicao  # noqa: E402
from explicacoes import ARTILHEIRO_GOLS, AWD, CONSERTA_JSL, EXPLICACOES  # noqa: E402

RAIZ = AQUI.parent.parent
PACOTE = RAIZ / "data" / "coleta" / "jpn-1" / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / "jpn-1.md"
FONTE_JL = "J.League Data Site"

# nomes como cada fonte escreve: clube -> fonte -> nome -> anos
NOMES: dict[str, dict[str, dict[str, set]]] = defaultdict(lambda: defaultdict(lambda: defaultdict(set)))


def nome_clube(nome: str, fonte: str, ano: int) -> str:
    c = clube(nome)
    if c is None:
        raise SystemExit(f"sem regra de clube: {nome!r} ({fonte}, {ano})")
    NOMES[c][fonte][nome].add(ano)
    return c


def nome_jogador(s: str) -> str:
    """"Takuya TAKAGI" -> "Takuya Takagi"; "PEDRO JUNIOR" -> "Pedro Junior"; "NOMURA Mutsuhiko" -> "Nomura Mutsuhiko"."""
    def tok(t: str) -> str:
        if re.search(r"[a-zà-ÿ]", t) or not re.search(r"[A-ZÀ-Þ]{2}", t):
            return t
        return "-".join(p[:1] + p[1:].lower() for p in t.split("-"))
    return " ".join(tok(t) for t in s.split())


def faixa(anos: set) -> str:
    a = sorted(anos)
    return str(a[0]) if a[0] == a[-1] else f"{a[0]}-{a[-1]}"


# ----------------------------------------------------------------------------------------------------- JSL
def jsl(e: Edicao, proximos: set[str] | None) -> dict:
    t = ler_jsl.ler(e.pagina, CONSERTA_JSL.get(e.pagina))
    ano = e.ano_inicio
    tab = [(l, nome_clube(l.nome, "rsssf", ano)) for l in t.tabela]
    n = len(tab)
    jogos = []
    for j in t.jogos:
        jogos.append({"mandante": nome_clube(j.mandante, "rsssf", ano), "visitante": nome_clube(j.visitante, "rsssf", ano),
                      "gm": j.gm, "gv": j.gv, "rodada": None, "data": None, "obs": ""})
    obs_ed = []
    # 1988/89: rodadas com data, casadas com a tabela de confrontos pelo par de clubes
    if t.rodadas:
        por_par = {(j["mandante"], j["visitante"]): j for j in jogos}
        sem_par, invertidos = [], []
        for r in t.rodadas:
            m_, v_ = nome_clube(r.mandante, "rsssf", ano), nome_clube(r.visitante, "rsssf", ano)
            j = por_par.get((m_, v_))
            if not j or (j["gm"], j["gv"]) != (r.gm, r.gv) or j["rodada"]:
                # a lista de rodadas às vezes inverte o mando: vale a tabela de confrontos, que fecha com a tabela final
                inv = por_par.get((v_, m_))
                if inv and (inv["gm"], inv["gv"]) == (r.gv, r.gm) and not inv["rodada"]:
                    j = inv
                    invertidos.append(f"{r.mandante} {r.gm}-{r.gv} {r.visitante} (rodada {r.rodada}): na tabela de confrontos "
                                      f"o mandante é o {v_}")
                else:
                    sem_par.append(f"{r.mandante} {r.gm}-{r.gv} {r.visitante} (rodada {r.rodada})"); continue
            j["rodada"], j["data"] = r.rodada, r.data
        assert not sem_par, (e.temporada, sem_par)
        obs_ed.append(f"rodada e data dos {len(t.rodadas)} jogos pela lista de rodadas da página")
        if invertidos:
            obs_ed.append("mando invertido na lista de rodadas, vale o da tabela de confrontos (que fecha com a tabela "
                          "final): " + "; ".join(invertidos))
    # pontos por vitória: o mesmo em todas as linhas da tabela
    pen = any(l.v_pen is not None for l, _ in tab)
    cand = Counter()
    for l, _ in tab:
        if l.v:
            cand[(l.pts - (2 * l.v_pen + l.d_pen if pen else l.e)) / l.v] += 1
    pv = int(cand.most_common(1)[0][0])
    # conferência: soma dos jogos x tabela publicada
    calc = defaultdict(lambda: [0, 0, 0, 0, 0, 0])
    for j in jogos:
        for c, gp, gc in ((j["mandante"], j["gm"], j["gv"]), (j["visitante"], j["gv"], j["gm"])):
            x = calc[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            x[1 if gp > gc else 2 if gp == gc else 3] += 1
    difs = []
    for l, c in tab:
        if calc[c] != [l.j, l.v, l.e, l.d, l.gp, l.gc]:
            difs.append(f"{c}: tabela {[l.j, l.v, l.e, l.d, l.gp, l.gc]}, jogos {calc[c]}")
        conta = pv * l.v + (2 * l.v_pen + l.d_pen if pen else l.e)
        if conta != l.pts:
            difs.append(f"{c}: {l.pts} pontos na tabela, {conta} na conta ({pv} por vitória)")
    clf = []
    for l, c in tab:
        sit = "campeao" if l.pos == 1 else ""
        if proximos is not None and c not in proximos and (e.temporada, c) not in SAIU_SEM_CAIR:
            sit = "rebaixado"
        clf.append({"posicao": l.pos, "clube": c, "jogos": l.j, "vitorias": l.v, "empates": l.e, "derrotas": l.d,
                    "gols_pro": l.gp, "gols_contra": l.gc, "pontos": l.pts,
                    "ajuste_pontos": (l.pts - (pv * l.v + l.e)) if pen else "",
                    "situacao": sit, "fonte": f"RSSSF ({t.pagina})",
                    "observacao": f"vitórias nos pênaltis: {l.v_pen}, derrotas nos pênaltis: {l.d_pen}" if pen else ""})
    pub = [{"fase": "Liga", "grupo": "", "posicao": l.pos, "nome_fonte": l.nome, "clube": c, "jogos": l.j, "vitorias": l.v,
            "empates": l.e, "derrotas": l.d, "gols_pro": l.gp, "gols_contra": l.gc, "pontos": l.pts,
            "fonte": f"RSSSF ({t.pagina})"} for l, c in tab]
    maximo = max((g for _, _, g in t.artilheiros), default=0)
    art = [{"jogador": nome_jogador(re.sub(r"\s*\[.*$", "", j)), "clube": nome_clube(cl, "rsssf-artilheiros", ano), "gols": g,
            "fonte": f"RSSSF ({t.pagina})"} for j, cl, g in t.artilheiros if g == maximo]
    if pen:
        obs_ed.append("empates decididos nos pênaltis (4 pontos a vitória, 2 a vitória nos pênaltis, 1 a derrota nos "
                      "pênaltis); a tabela de confrontos não diz quem ganhou cada disputa: os jogos ficam como empate")
    formato = f"pontos corridos, {n} clubes, turno e returno"
    return {"jogos": jogos, "fases": [("Liga", "liga", "pontos_corridos")], "clf": clf, "pub": pub, "art": art,
            "difs": difs, "n_tabelas": 1, "pv": pv, "num_clubes": n, "formato": formato, "obs": obs_ed,
            "campeao": tab[0][1], "vice": tab[1][1], "classificacao": f"RSSSF ({t.pagina})", "esperados": n * (n - 1),
            "rodada_ok": False}


# clubes que não estavam na edição seguinte sem ter caído
SAIU_SEM_CAIR = {("1976", "Eidai Industries"): "desfeito no fim de 1976 (a RSSSF: 'Disbanded: Eidai Industries; replaced by Fujitsu')",
                 ("1998", "Yokohama Flügels"): "fechou no fim de 1998 (fusão com o Yokohama Marinos)"}


# ----------------------------------------------------------------------------------------------------- J1
FASE_TURNO = {"J1 Suntory": "1º turno (Suntory Series)", "J1 NICOS": "2º turno (NICOS Series)", "J1 1st": "1º turno",
              "J1 2nd": "2º turno", "J1": "Liga"}


def _data_lista(s: str) -> str | None:
    m = re.search(r"(\d{2})/(\d{2})/(\d{2})", s)
    if not m:
        return None
    a = int(m.group(3))
    return f"{1900 + a if a > 50 else 2000 + a}-{m.group(1)}-{m.group(2)}"


def _placar_lista(s: str) -> tuple:
    m = re.match(r"^(\d+)-(\d+)(?: \(Penalty(\d+)-(\d+)\))?$", s.strip())
    return tuple(int(x) if x is not None else None for x in m.groups()) if m else (None, None, None, None)


def _tabela_oficial(t: dict) -> list[dict]:
    """Linhas da tabela oficial como dicionários, pelo cabeçalho; "tag" = a marca do fim da linha (J2, ACL...)."""
    cab = t["colunas"]
    saida = []
    for l in t["linhas"]:
        d = dict(zip(cab, l))
        d["tag"] = l[-2] if len(l) >= len(cab) else ""
        d["id_clube"] = l[-1]
        pos = d.get("Position") or d.get("Overall Ranking") or ""
        d["pos"] = int(re.sub(r"\D", "", pos)) if re.search(r"\d", pos) and pos != "1or2" else None
        d["pos_txt"] = pos
        saida.append(d)
    return saida


def _num(d: dict, k: str) -> int:
    v = d.get(k, "")
    return int(v) if re.match(r"^-?\d+$", v or "") else 0


def j1(e: Edicao, proximos: set[str] | None, espn: dict) -> dict:
    a = e.ano_inicio
    lista = [x for x in ler_jleague.jogos(a) if x["lista"]["tipo"] in ("J1", "Championship")]
    fora = [x for x in ler_jleague.lista(a) if x["tipo"] == "Playoff"]
    jogos, sem_pagina, gols_dif = [], 0, []
    for x in lista:
        l = x["lista"]
        pag = not x.get("sem_pagina")
        sem_pagina += not pag
        mand = nome_clube(x["mandante"], FONTE_JL, a) if pag else clube(l["mandante"])
        vis = nome_clube(x["visitante"], FONTE_JL, a) if pag else clube(l["visitante"])
        nome_clube(l["mandante"], "jleague-sigla", a); nome_clube(l["visitante"], "jleague-sigla", a)
        gm, gv, pm, pv_ = _placar_lista(l["placar"])
        if pag:
            assert (x["gm"], x["gv"]) == (gm, gv), (a, l, x["gm"], x["gv"])
            assert (x["pen_m"], x["pen_v"]) == (pm, pv_), (a, l, x["pen_m"], x["pen_v"])
        if l["tipo"] == "J1":
            fase = FASE_TURNO[l["torneio"]]
            rod = int(re.search(r"(\d+)\w\w Sec", l["rodada"]).group(1))
        elif "Semi" in l["rodada"]:
            fase, rod = "Semifinal", None
        else:
            fase, rod = "Final", None
        obs = []
        if fase == "Final" or fase == "Semifinal":
            if re.search(r"1st (Leg|Day 1st Sec)|Final 1st Leg|1st Day 1st Sec", l["rodada"]):
                obs.append("jogo de ida")
            elif re.search(r"2nd Leg|1st Day 2nd Sec", l["rodada"]):
                obs.append("jogo de volta")
        if pag and x["prorrogacao"]:
            gols_pr = sum(m + v for nome, m, v in x["tempos"] if nome.startswith("Extra"))
            obs.append("prorrogação" + (" (gol de ouro)" if gols_pr and a <= 2002 and fase != "Final" else "") +
                       ("" if gols_pr else " sem gols"))
        if pm is not None:
            obs.append(f"{mand if pm > pv_ else vis} venceu nos pênaltis por {max(pm, pv_)}-{min(pm, pv_)}")
        j = {"mandante": mand, "visitante": vis, "gm": gm, "gv": gv, "pm": pm, "pv": pv_, "fase": fase, "rodada": rod,
             "data": (x["data"] if pag else None) or _data_lista(l["data"]),
             "hora": (x["hora"] if pag else None) or (l["hora"] or None),
             "estadio": (x["estadio"] if pag else None) or l["estadio"] or None,
             "publico": (x["publico"] if pag else None) or (int(l["publico"].replace(",", "")) if re.match(r"^[\d,]+$", l["publico"]) else None),
             "fonte_id": x["id"], "obs": "; ".join(obs), "gols": [], "cartoes": [],
             "prorrogacao": bool(pag and x["prorrogacao"]), "arbitro": x.get("arbitro") if pag else None}
        if pag:
            lados = {"m": mand, "v": vis}
            sm = sum(1 for g in x["gols"] if g["lado"] == "m")
            if (sm, len(x["gols"]) - sm) == (gm, gv):
                j["gols"] = [dict(g, clube=lados[g["lado"]], jogador=nome_jogador(g["jogador"])) for g in x["gols"]]
            else:
                gols_dif.append(f"{mand} {gm}-{gv} {vis}: {sm}+{len(x['gols']) - sm} autores")
            j["cartoes"] = [dict(c, clube=lados[c["lado"]], jogador=nome_jogador(c["jogador"])) for c in x["cartoes"]]
        if x["id"] in AWD:
            j["especial"] = "awd"
            j["gols_texto"] = "; ".join(f"{nome_jogador(g['jogador'])} ({lados[g['lado']]}) {g['minuto']}'" for g in x["gols"])
            j["obs"] = "; ".join(filter(None, [j["obs"], AWD[x["id"]]]))
            gols_dif[:] = [g for g in gols_dif if not g.startswith(f"{mand} {gm}-{gv} {vis}")]
        jogos.append(j)
    tabs = json.loads((ler_jleague.LISTAS / f"tabelas_{a}.json").read_text(encoding="utf-8"))
    torneios = [t for t in tabs if t["torneio"] != "Overall"]
    anual = next((t for t in tabs if t["torneio"] == "Overall"), None)
    fases_liga = list(dict.fromkeys(j["fase"] for j in jogos if j["fase"] not in ("Final", "Semifinal")))
    assert len(fases_liga) == len(torneios), (a, fases_liga, [t["torneio"] for t in torneios])
    # conferência: cada tabela oficial de turno contra a soma dos jogos do turno, com as regras de pontos do ano
    difs, pub = [], []
    for fase, t in zip(fases_liga, torneios):
        calc = defaultdict(lambda: {"GP": 0, "W": 0, "D": 0, "L": 0, "GF": 0, "GA": 0, "Pts": 0})
        for j in (j for j in jogos if j["fase"] == fase):
            for lado, c, gp, gc, pp, pc in (("m", j["mandante"], j["gm"], j["gv"], j["pm"], j["pv"]),
                                            ("v", j["visitante"], j["gv"], j["gm"], j["pv"], j["pm"])):
                x = calc[c]
                x["GP"] += 1; x["GF"] += gp; x["GA"] += gc
                ganhou = gp > gc or (gp == gc and pp is not None and pp > pc)
                perdeu = gp < gc or (gp == gc and pp is not None and pp < pc)
                x["W" if ganhou else "L" if perdeu else "D"] += 1
                x["Pts"] += pontos_j1(a, ganhou, perdeu, j["prorrogacao"], pp is not None)
        for d in _tabela_oficial(t):
            c = nome_clube(d["Team"], FONTE_JL + " (tabela)", a)
            x = calc[c]
            ofi = {k: _num(d, k) for k in ("GP", "W", "D", "L", "GF", "GA", "Pts") if k in d}
            if any(x[k] != v for k, v in ofi.items()):
                difs.append(f"{fase}, {c}: oficial {ofi}, jogos { {k: x[k] for k in ofi} }")
            pub.append({"fase": fase, "grupo": "", "posicao": d["pos"], "nome_fonte": d["Team"], "clube": c,
                        "jogos": _num(d, "GP"), "vitorias": _num(d, "W"), "empates": _num(d, "D"), "derrotas": _num(d, "L"),
                        "gols_pro": _num(d, "GF"), "gols_contra": _num(d, "GA"), "pontos": d.get("Pts", ""),
                        "fonte": f"{FONTE_JL} ({t['fonte']}: {t['torneio']})"})
    # final e semifinal
    final = [j for j in jogos if j["fase"] == "Final"]
    campeao = vice = None
    if final:
        tot = Counter()
        for j in final:
            tot[j["mandante"]] += j["gm"]; tot[j["visitante"]] += j["gv"]
        a1, a2 = final[0]["mandante"], final[0]["visitante"]
        ult = final[-1]
        if tot[a1] != tot[a2]:
            campeao = a1 if tot[a1] > tot[a2] else a2
        else:   # empate no agregado: pênaltis no 2º jogo (1999, 2004) ou gol fora (2015: Sanfrecce)
            if ult["pm"] is not None:
                campeao = ult["mandante"] if ult["pm"] > ult["pv"] else ult["visitante"]
            else:
                fora_ = Counter()
                for j in final:
                    fora_[j["visitante"]] += j["gv"]
                campeao = a1 if fora_[a1] > fora_[a2] else a2
        vice = a2 if campeao == a1 else a1
    # classificação final
    if len(torneios) == 1:
        base = _tabela_oficial(torneios[0])
        fonte_clf = f"{FONTE_JL} (tabela oficial: {torneios[0]['torneio']})"
    elif anual:
        base = _tabela_oficial(anual)
        fonte_clf = f"{FONTE_JL} (tabela anual oficial: Overall table for the season)"
    else:   # 1993-1998: soma das tabelas dos dois turnos
        soma = {}
        for t in torneios:
            for d in _tabela_oficial(t):
                s = soma.setdefault(clube(d["Team"]), {"Team": d["Team"], **{k: 0 for k in ("GP", "W", "D", "L", "GF", "GA", "Pts")},
                                                       "tag": ""})
                for k in ("GP", "W", "D", "L", "GF", "GA", "Pts"):
                    s[k] = str(int(s[k]) + _num(d, k))
        chave_ord = (lambda d: (-int(d["W"]), -(int(d["GF"]) - int(d["GA"])), -int(d["GF"]))) if a <= 1994 else \
                    (lambda d: (-int(d["Pts"]), -(int(d["GF"]) - int(d["GA"])), -int(d["GF"])))
        base = sorted(soma.values(), key=chave_ord)
        for i, d in enumerate(base, 1):
            d["pos"] = i
        fonte_clf = (f"soma das tabelas oficiais dos dois turnos ({FONTE_JL}), ordenada por "
                     + ("vitórias" if a <= 1994 else "pontos") + ", saldo e gols pró")
    linhas = []
    for d in base:
        c = nome_clube(d["Team"], FONTE_JL + " (tabela)", a)
        linhas.append({"clube": c, "jogos": _num(d, "GP"), "vitorias": _num(d, "W"), "empates": _num(d, "D"),
                       "derrotas": _num(d, "L"), "gols_pro": _num(d, "GF"), "gols_contra": _num(d, "GA"),
                       "pontos": d.get("Pts", "") if a >= 1995 else "", "tag": d.get("tag", ""), "pos": d.get("pos")})
    if campeao:   # o campeão e o vice da final vão para 1º e 2º; os outros seguem a tabela
        linhas.sort(key=lambda l: (l["clube"] != campeao, l["clube"] != vice))
    else:
        campeao, vice = linhas[0]["clube"], linhas[1]["clube"]
    clf = []
    for i, l in enumerate(linhas, 1):
        sit = "campeao" if i == 1 else ""
        if l["tag"] == "J2" or (proximos is not None and l["clube"] not in proximos and (e.temporada, l["clube"]) not in SAIU_SEM_CAIR):
            sit = "rebaixado"
        clf.append({"posicao": i, "clube": l["clube"], "jogos": l["jogos"], "vitorias": l["vitorias"], "empates": l["empates"],
                    "derrotas": l["derrotas"], "gols_pro": l["gols_pro"], "gols_contra": l["gols_contra"],
                    "pontos": l["pontos"], "ajuste_pontos": "", "situacao": sit, "fonte": fonte_clf,
                    "observacao": "vitórias contam as da prorrogação e as dos pênaltis" if a <= 1998 else ""})
    # artilheiro: gols da liga (sem a final), como a J.League conta
    por_jog = defaultdict(Counter)
    for j in jogos:
        if j["fase"] in ("Final", "Semifinal"):
            continue
        for g in j["gols"]:
            if g["tipo"] != "contra" and g["jogador"]:
                por_jog[g["jogador"]][g["clube"]] += 1
    tot = {p: sum(c.values()) for p, c in por_jog.items()}
    maximo = max(tot.values(), default=0)
    art = [{"jogador": p, "clube": por_jog[p].most_common(1)[0][0], "gols": n, "fonte": f"{FONTE_JL} (soma dos gols da liga)"}
           for p, n in tot.items() if n == maximo]
    # ESPN (2006 em diante): conferência dos placares
    espn_dif, espn_ok = [], 0
    for j in jogos:
        k = (j["mandante"], j["visitante"])
        for d in (0, -1, 1):
            dia = (date.fromisoformat(j["data"]) + timedelta(days=d)).isoformat()
            if (k, dia) in espn:
                gm_e, gv_e = espn[(k, dia)]
                if (gm_e, gv_e) == (j["gm"], j["gv"]):
                    espn_ok += 1
                else:
                    espn_dif.append(f"{j['data']} {k[0]} {j['gm']}-{j['gv']} {k[1]} (ESPN {gm_e}-{gv_e})")
                break
    # ogol (1993-1996 e 2004 em diante; o ogol não tem os jogos de 1997 a 2003): conferência dos placares
    ogol_dif, ogol_ok = [], 0
    arq = RAIZ / "data" / "coleta" / "jpn-1" / "ogol" / f"{a}.json"
    og = {}
    if arq.exists():
        for o in json.loads(arq.read_text(encoding="utf-8")):
            if o["gols_mandante"] is not None and clube(o["mandante"]) and clube(o["visitante"]):
                og[((clube(o["mandante"]), clube(o["visitante"])), o["data"])] = (o["gols_mandante"], o["gols_visitante"])
    for j in jogos:
        k = (j["mandante"], j["visitante"])
        for d in (0, -1, 1):
            dia = (date.fromisoformat(j["data"]) + timedelta(days=d)).isoformat()
            if (k, dia) in og:
                if og[(k, dia)] == (j["gm"], j["gv"]):
                    ogol_ok += 1
                else:
                    ogol_dif.append(f"{j['data']} {k[0]} {j['gm']}-{j['gv']} {k[1]} (ogol {og[(k, dia)][0]}-{og[(k, dia)][1]})")
                break
    n = len({j["mandante"] for j in jogos if j["fase"] not in ("Final", "Semifinal")})
    if a in TURNOS:
        formato = f"dois turnos de pontos corridos ({n} clubes, turno único em cada um)" + (
            "; final entre os campeões dos turnos (ida e volta)" if final and a != 2015 and a != 2016 else
            "; semifinal (jogo único) e final (ida e volta) entre os campeões dos turnos e o melhor da tabela anual" if final else
            "; sem final: o mesmo clube ganhou os dois turnos")
    else:
        formato = f"pontos corridos, {n} clubes, turno e returno"
    fases = [(f, "liga", "pontos_corridos") for f in fases_liga]
    if any(j["fase"] == "Semifinal" for j in jogos):
        fases.append(("Semifinal", "mata_mata", "jogo_unico"))
    if final:
        fases.append(("Final", "mata_mata", "ida_volta"))
    obs_ed = []
    if fora:
        obs_ed.append(f"fora do pacote: {len(fora)} jogo(s) da repescagem J1/J2 (entram com a 2ª divisão)")
    if sem_pagina:
        obs_ed.append(f"{sem_pagina} jogo(s) sem a página do jogo (só a lista: sem autores dos gols nem cartões)")
    return {"jogos": jogos, "fases": fases, "clf": clf, "pub": pub, "art": art, "difs": difs, "n_tabelas": len(torneios),
            "pv": None if a <= 1994 else 3, "num_clubes": n, "formato": formato, "obs": obs_ed, "campeao": campeao,
            "vice": vice, "classificacao": fonte_clf, "esperados": len(lista), "gols_dif": gols_dif,
            "espn": (espn_ok, espn_dif), "ogol": (ogol_ok, ogol_dif), "rodada_ok": a not in TURNOS and a >= 2005}


def pontos_j1(a: int, ganhou: bool, perdeu: bool, prorrogacao: bool, penaltis: bool) -> int:
    """Pontos de um jogo para um clube, pelas regras de cada época (veja edicoes.py)."""
    if a <= 1994:
        return 0
    if a <= 1996:   # toda vitória vale 3; a derrota nos pênaltis vale 1 (conferido nas tabelas oficiais)
        return 3 if ganhou else 1 if penaltis else 0
    if a <= 1998:
        return (1 if penaltis else 2 if prorrogacao else 3) if ganhou else 0
    if a <= 2002:
        return (2 if prorrogacao else 3) if ganhou else 0 if perdeu else 1
    return 3 if ganhou else 0 if perdeu else 1


def ler_espn() -> dict:
    """{((mandante, visitante), data em Tóquio): (gols mandante, gols visitante)} dos jogos da ESPN (2006 em diante)."""
    saida = {}
    for arq in sorted((RAIZ / "data" / "coleta" / "jpn-1" / "espn").glob("jpn1_*.json")):
        for j in json.loads(arq.read_text(encoding="utf-8")):
            if j["situacao"] != "STATUS_FULL_TIME" or j["gols_mandante"] in (None, ""):
                continue
            m, v = clube(j["mandante"]), clube(j["visitante"])
            if not (m and v):
                continue
            dia = (datetime.fromisoformat(j["data_hora"].replace("Z", "+00:00")) + timedelta(hours=9)).date().isoformat()
            saida[((m, v), dia)] = (int(j["gols_mandante"]), int(j["gols_visitante"]))
    return saida


# ----------------------------------------------------------------------------------------------------- classificação por rodada
def por_rodada(temporada: str, jogos: list[dict], clf: list[dict]) -> list[dict]:
    clubes = [c["clube"] for c in clf]
    n = len(clubes)
    rebaixados = sum(1 for c in clf if c["situacao"] == "rebaixado")
    acum = {c: [0, 0, 0, 0, 0, 0, 0] for c in clubes}   # pts, j, v, e, d, gp, gc
    saida = []
    for r in sorted({j["rodada"] for j in jogos}):
        for j in (j for j in jogos if j["rodada"] == r):
            for c, gp, gc in ((j["mandante"], j["gm"], j["gv"]), (j["visitante"], j["gv"], j["gm"])):
                x = acum[c]
                x[1] += 1; x[5] += gp; x[6] += gc
                if gp > gc:
                    x[0] += 3; x[2] += 1
                elif gp == gc:
                    x[0] += 1; x[3] += 1
                else:
                    x[4] += 1
        ordem = sorted(clubes, key=lambda c: (-acum[c][0], -(acum[c][5] - acum[c][6]), -acum[c][5], c))
        for i, c in enumerate(ordem, 1):
            x = acum[c]
            zona = "titulo" if i == 1 else "rebaixamento" if i > n - rebaixados else "meio"
            saida.append({"temporada": temporada, "rodada": r, "clube": c, "posicao": i, "pontos": x[0], "jogos": x[1],
                          "vitorias": x[2], "empates": x[3], "derrotas": x[4], "gols_pro": x[5], "gols_contra": x[6],
                          "zona": zona})
    return saida


# ----------------------------------------------------------------------------------------------------- saída
def escrever(nome: str, campos: list[str], linhas: list[dict]) -> None:
    with (PACOTE / f"{nome}.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for l in linhas:
            w.writerow({k: ("" if l.get(k) is None else l.get(k)) for k in campos})


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    PACOTE.mkdir(parents=True, exist_ok=True)
    wiki = podio()
    wiki_art = artilheiros()
    espn = ler_espn()
    participantes: dict[str, set[str]] = {}
    res: dict[str, dict] = {}
    # primeiro sem o rebaixamento (que depende da edição seguinte), depois de novo com ele
    for passo in (1, 2):
        for i, e in enumerate(EDICOES):
            prox = None
            if passo == 2 and i + 1 < len(EDICOES) and e.temporada != "1991/92":
                prox = participantes[EDICOES[i + 1].temporada]
            r = jsl(e, prox) if e.era == "jsl" else j1(e, prox, espn)
            participantes[e.temporada] = {c["clube"] for c in r["clf"]}
            res[e.temporada] = r
    ed_l, fa_l, pa_l, go_l, ca_l, cf_l, cr_l, pu_l, ar_l, co_l, rel = [], [], [], [], [], [], [], [], [], [], []
    for e in EDICOES:
        r = res[e.temporada]
        w = wiki.get(e.temporada)
        assert w and w[0][0] == r["campeao"], (e.temporada, r["campeao"], w)
        vice_wiki = w[1][0] if len(w) > 1 else None
        obs_conf = f"campeão {r['campeao']} (Wikipédia, lista de campeões: {w[0][1]})"
        if vice_wiki != r["vice"]:
            obs_conf += f"; vice: {r['vice']} aqui, {vice_wiki} na Wikipédia"
        if r["difs"]:
            obs_conf += "; divergências explicadas no relatório"
        ed_l.append({"temporada": e.temporada, "ano_inicio": e.ano_inicio, "ano_fim": e.ano_fim, "nome_oficial": e.nome_oficial,
                     "num_clubes": r["num_clubes"], "pontos_vitoria": r["pv"], "formato": r["formato"], "campeao": r["campeao"],
                     "vice": r["vice"], "fontes": "RSSSF" if e.era == "jsl" else FONTE_JL,
                     "observacao": "; ".join(r["obs"] + ([EXPLICACOES[e.temporada]] if e.temporada in EXPLICACOES else []))})
        for o, (f, tipo, serie) in enumerate(r["fases"], 1):
            fa_l.append({"temporada": e.temporada, "ordem": o, "fase": f, "tipo": tipo, "num_grupos": "", "formato_serie": serie,
                         "criterio": "pontos, saldo de gols, gols pró" if tipo == "liga" else
                                     "gols no agregado, gol fora, pênaltis" if serie == "ida_volta" else "prorrogação e pênaltis"})
        gols_ed = autores = 0
        fases_nome = {f for f, _, _ in r["fases"]}
        for n, j in enumerate(sorted(r["jogos"], key=lambda j: (j.get("data") or "", j.get("fonte_id") or "")) if e.era == "j1"
                              else r["jogos"], 1):
            pid = f"{e.ano_inicio}-{n:04d}"
            fase = j.get("fase", "Liga")
            assert fase in fases_nome
            obs = j["obs"]
            if j.get("arbitro"):
                obs = (obs + "; " if obs else "") + f"árbitro: {nome_jogador(j['arbitro'])}"
            pa_l.append({"id": pid, "temporada": e.temporada, "fase": fase, "grupo": "", "rodada": j["rodada"], "data": j["data"],
                         "hora": j.get("hora"), "mandante": j["mandante"], "visitante": j["visitante"], "gols_mandante": j["gm"],
                         "gols_visitante": j["gv"], "penaltis_mandante": j.get("pm"), "penaltis_visitante": j.get("pv"),
                         "resultado_especial": j.get("especial", ""), "estadio": j.get("estadio"), "cidade": "", "publico": j.get("publico"),
                         "fonte": "RSSSF" if e.era == "jsl" else FONTE_JL,
                         "fonte_id": f"jap{e.pagina % 100:02d}" if e.era == "jsl" else j["fonte_id"], "gols_texto": j.get("gols_texto", ""),
                         "observacao": obs})
            gols_ed += j["gm"] + j["gv"]
            for g in j.get("gols", []):
                go_l.append({"partida_id": pid, "clube": g["clube"], "jogador": g["jogador"], "minuto": g["minuto"],
                             "acrescimo": g["acrescimo"], "tipo": g["tipo"], "fonte": FONTE_JL})
                autores += 1
            for c in j.get("cartoes", []):
                ca_l.append({"partida_id": pid, "clube": c["clube"], "jogador": c["jogador"], "minuto": c["minuto"],
                             "acrescimo": c["acrescimo"], "cor": c["cor"], "fonte": FONTE_JL})
        for c in r["clf"]:
            cf_l.append(dict(c, temporada=e.temporada))
        if r["rodada_ok"]:
            cr_l += por_rodada(e.temporada, r["jogos"], r["clf"])
        for p in r["pub"]:
            pu_l.append(dict(p, temporada=e.temporada))
        # artilheiro oficial: lista da Wikipédia (a soma por nome da J.League erra quando o jogador tem dois nomes, como
        # "Otze" e "Ordenewitz" em 1994); a RSSSF (JSL) e a soma da J.League (J1) são a conferência
        oficial = wiki_art[e.temporada]
        if e.temporada in ARTILHEIRO_GOLS:
            oficial = [(j, cl, txt, ARTILHEIRO_GOLS[e.temporada][0]) for j, cl, txt, _ in oficial]
        for jog, cl, _, g in oficial:
            ar_l.append({"temporada": e.temporada, "jogador": jog, "clube": cl, "gols": g,
                         "fonte": "Wikipédia (List of Japanese football champions)"})
        outra = "RSSSF" if e.era == "jsl" else "soma dos gols da J.League"
        if {(cl, g) for _, cl, _, g in oficial} != {(x["clube"], x["gols"]) for x in r["art"]}:
            r["art_dif"] = (f"artilheiro na Wikipédia: " + "; ".join(f"{j} ({cl}) {g}" for j, cl, _, g in oficial) +
                            f"; pela {outra}: " + "; ".join(f"{x['jogador']} ({x['clube']}) {x['gols']}" for x in r["art"]))
        r["art"] = [{"jogador": j, "clube": cl, "gols": g} for j, cl, _, g in oficial]
        if e.temporada in ARTILHEIRO_GOLS:
            r["art_dif"] = "gols corrigidos: " + ARTILHEIRO_GOLS[e.temporada][1]
        div = len({d.split(",")[0] for d in r["difs"]}) if r["difs"] else 0
        co_l.append({"temporada": e.temporada, "jogos": len(r["jogos"]), "jogos_esperados": r["esperados"],
                     "tabelas_conferidas": r["n_tabelas"], "tabelas_divergentes": min(div, r["n_tabelas"]), "gols": gols_ed,
                     "gols_com_autor": autores, "observacao": obs_conf})
        rel.append((e, r, gols_ed, autores, obs_conf))
    # grafias do ogol (o agente 1 tira os escudos dos calendários do ogol pelo nome) e da ESPN
    for e in EDICOES:
        if e.era != "j1":
            continue
        presentes = participantes[e.temporada]
        for fonte, arq in (("ogol", RAIZ / "data" / "coleta" / "jpn-1" / "ogol" / f"{e.ano_inicio}.json"),
                           ("espn", RAIZ / "data" / "coleta" / "jpn-1" / "espn" / f"jpn1_{e.ano_inicio}.json")):
            if arq.exists():
                for j in json.loads(arq.read_text(encoding="utf-8")):
                    for n in (j["mandante"], j["visitante"]):
                        if clube(n) in presentes:
                            nome_clube(n, fonte, e.ano_inicio)
    # clubes
    cl_l = []
    for c in sorted(NOMES):
        cidade, prov = CLUBES[c]
        partes = []
        for fonte, nomes in sorted(NOMES[c].items()):
            for nome, anos in sorted(nomes.items(), key=lambda x: min(x[1])):
                partes.append(f"{fonte}:{nome}:{faixa(anos)}")
        cl_l.append({"clube": c, "regiao": prov, "cidade": cidade, "pais": "JPN", "nomes_fonte": "|".join(partes)})
    (PACOTE / "competicao.json").write_text(json.dumps({
        "slug": "jpn-1", "nome": "Campeonato Japonês", "nome_curto": "Japonês", "tipo": "liga", "nivel": 1, "pais": "JPN",
        "pais_nome": "Japão", "regiao": None, "confederacao": "AFC", "rotulo_painel": "Japonês",
        "menu_painel": "Japão · 1ª divisão", "do_painel": "do Campeonato Japonês", "o_painel": "o Campeonato Japonês",
        "observacao": "Japan Soccer League (JSL, amadora, 1965 a 1991/92) e J.League/J1 (1993 em diante); 1992 sem liga"},
        ensure_ascii=False, indent=1), encoding="utf-8")
    escrever("paises", ["codigo", "nome", "confederacao"], [{"codigo": "JPN", "nome": "Japão", "confederacao": "AFC"}])
    escrever("clubes", ["clube", "regiao", "cidade", "pais", "nomes_fonte"], cl_l)
    escrever("edicoes", ["temporada", "ano_inicio", "ano_fim", "nome_oficial", "num_clubes", "pontos_vitoria", "formato", "campeao",
                         "vice", "fontes", "observacao"], ed_l)
    escrever("fases", ["temporada", "ordem", "fase", "tipo", "num_grupos", "formato_serie", "criterio"], fa_l)
    escrever("partidas", ["id", "temporada", "fase", "grupo", "rodada", "data", "hora", "mandante", "visitante", "gols_mandante",
                          "gols_visitante", "penaltis_mandante", "penaltis_visitante", "resultado_especial", "estadio", "cidade",
                          "publico", "fonte", "fonte_id", "gols_texto", "observacao"], pa_l)
    escrever("gols", ["partida_id", "clube", "jogador", "minuto", "acrescimo", "tipo", "fonte"], go_l)
    escrever("cartoes", ["partida_id", "clube", "jogador", "minuto", "acrescimo", "cor", "fonte"], ca_l)
    escrever("classificacao_final", ["temporada", "posicao", "clube", "jogos", "vitorias", "empates", "derrotas", "gols_pro",
                                     "gols_contra", "pontos", "ajuste_pontos", "situacao", "fonte", "observacao"], cf_l)
    escrever("classificacao_rodada", ["temporada", "rodada", "clube", "posicao", "pontos", "jogos", "vitorias", "empates",
                                      "derrotas", "gols_pro", "gols_contra", "zona"], cr_l)
    escrever("tabelas_publicadas", ["temporada", "fase", "grupo", "posicao", "nome_fonte", "clube", "jogos", "vitorias", "empates",
                                    "derrotas", "gols_pro", "gols_contra", "pontos", "fonte"], pu_l)
    escrever("artilheiros", ["temporada", "jogador", "clube", "gols", "fonte"], ar_l)
    escrever("conferencia", ["temporada", "jogos", "jogos_esperados", "tabelas_conferidas", "tabelas_divergentes", "gols",
                             "gols_com_autor", "observacao"], co_l)
    relatorio(rel, cl_l, pa_l, go_l, ca_l)
    print(f"{len(ed_l)} edições, {len(pa_l)} jogos, {len(go_l)} gols com autor, {len(ca_l)} cartões, {len(cl_l)} clubes")
    for e, r, *_ in rel:
        if r["difs"] or r.get("gols_dif") or (r.get("espn") and r["espn"][1]) or (r.get("ogol") and r["ogol"][1]):
            print(e.temporada, "| difs:", r["difs"][:4], "| gols:", r.get("gols_dif", [])[:3], "| espn:", (r.get("espn") or (0, []))[1][:3],
                  "| ogol:", (r.get("ogol") or (0, []))[1][:5])


def relatorio(rel, cl_l, pa_l, go_l, ca_l) -> None:
    from relatorio import escrever_relatorio
    escrever_relatorio(RELATORIO, rel, cl_l, pa_l, go_l, ca_l)


if __name__ == "__main__":
    main()
