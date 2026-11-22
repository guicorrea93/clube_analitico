"""Campeonato alemão antes da Bundesliga (1902/03 a 1962/63), no mesmo pacote ger-1 (decisão do Guilherme, 22/11/2026).

O título era decidido numa fase final entre os campeões (e, depois de 1947, também os vices) das ligas regionais: mata-mata
até 1932/33, grupos e mata-mata de 1933/34 a 1943/44 (mata-mata de novo em 1941/42 a 1943/44), mata-mata de 1947/48 a
1949/50 e dois grupos com final de 1950/51 a 1962/63. No pacote entra a fase final (as ligas regionais ficam de fora).

Fontes:
  RSSSF      1902/03-1943/44: uma página por temporada (tablesd/duit1903.html ... duit1944.html, seção "Deutsche
             Meisterschaft"); 1947/48-1962/63: tablesd/duithist4763.html. Jogos (data e cidade na maioria), tabelas dos
             grupos e, em duas finais, público e gols. Leitura em rsssf_antigo.py.
  RSSSF      lista de campeões (tablesd/duitchamp.html): o campeão oficial de cada temporada.
  Wikipédia  artigo de cada temporada ("1925–26 German football championship"): das partidas com "football box" (as
             finais, quase sempre) vêm estádio, público, árbitro e gols com minuto.

Sem campeonato: 1914/15 a 1918/19 (Primeira Guerra Mundial), 1944/45 a 1946/47 (Segunda Guerra e pós-guerra). Sem campeão:
1903/04 (final não jogada, anulada por protesto) e 1921/22 (título não atribuído).

Uso: montar(tab, nomes, ocorr) acrescenta edições, fases, partidas, gols, classificação, tabelas publicadas e conferência ao
`tab` do importador (importar.py chama antes do cadastro de clubes).
"""
from __future__ import annotations

import re
from collections import defaultdict

import clubes_ger as clubes
from edicoes import DADOS
from rsssf_antigo import fase_final, pos_guerra, texto
from wiki_tabela import _fecha, _partes, limpar

TEMPORADAS_ANTIGAS = list(range(1902, 1963))
SEM_CAMPEONATO = {**{a: "sem campeonato (Primeira Guerra Mundial)" for a in range(1914, 1919)},
                  1944: "sem campeonato (Segunda Guerra Mundial)",
                  1945: "sem campeonato (pós-guerra: só as ligas regionais das zonas de ocupação)",
                  1946: "sem campeonato (pós-guerra: só as ligas regionais das zonas de ocupação)"}
SEM_CAMPEAO = {1903: "final não jogada: a federação anulou a fase final depois do protesto do Karlsruher FV; sem campeão",
               1921: "título não atribuído: a final entre Hamburger SV e Nürnberg teve dois jogos sem vencedor (2-2 e o "
                     "segundo interrompido em 1-1); a federação deu o título ao Hamburgo, que renunciou a ele"}
# explicação das divergências que sobram (vai para o relatório, antes das ocorrências da temporada)
EXPLICACOES = {
    1905: ["Schlesien Breslau x Hertha (quartas de final): 1-7 na RSSSF, 0-7 na Wikipédia; fica a RSSSF"],
    1947: ["a Wikipédia (en) traz Kaiserslautern 1-0 1860 Munique e Union Oberschöneweide 0-4 St. Pauli nas quartas e "
           "Kaiserslautern 2-0 Neuendorf na semifinal; a RSSSF traz 5-1, 0-7 e 5-1. Fica a RSSSF, fonte principal "
           "(pendência: conferir numa terceira fonte, como o kicker ou a Wikipédia em alemão)"],
    1956: ["tabela do Grupo 2 na RSSSF: Kickers Offenbach com 2 vitórias, 1 empate e 0 derrota e 4 pontos (a conta não fecha); "
           "os jogos dão 2 vitórias e 1 derrota (3-1 Hertha, 4-1 Kaiserslautern, 1-2 Dortmund) e os mesmos 4 pontos: erro de "
           "digitação da RSSSF"],
    1962: ["tabela do Grupo 2 na RSSSF: Borussia Neunkirchen com 6 gols pró; os jogos dão 8 (3-0 e 1-1 com o Hamburgo, 0-0 e "
           "2-5 com o Dortmund, 0-4 e 2-1 com o 1860), e só com 8 os gols pró do grupo fecham com os contra (40): erro de "
           "digitação da RSSSF"],
}
ORDEM = ["Fase preliminar", "Eliminatória", "1ª eliminatória", "2ª eliminatória", "3ª eliminatória", "Primeira fase",
         "Segunda fase", "Terceira fase", "Quarta fase", "Quinta fase", "Fase de grupos", "Final de grupo", "Oitavas de final",
         "Quartas de final", "Fase intermediária", "Semifinal", "Disputa de 3º lugar", "Final"]
ROMANOS = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6}


def temporada(a: int) -> str:
    return f"{a}/{str(a + 1)[-2:]}"


def fase_pt(nome: str) -> tuple[str, bool]:
    """Nome da fase na RSSSF -> (fase em português, é jogo de desempate)."""
    n = nome.lower()
    extra = "replay" in n or "repeat" in n
    if "third place" in n or "3rd place" in n:
        return "Disputa de 3º lugar", extra
    if "endspiel gruppe" in n:
        return "Final de grupo", extra
    if "semi" in n:
        return "Semifinal", extra
    if "quarter" in n:
        return "Quartas de final", extra
    if "1/8" in n or "eighth" in n:
        return "Oitavas de final", extra
    if "intermediate" in n:
        return "Fase intermediária", extra
    if "preliminary" in n:
        return "Fase preliminar", extra
    if "qualifying" in n:
        for k, v in (("first", "1ª"), ("second", "2ª"), ("third", "3ª")):
            if k in n:
                return f"{v} eliminatória", extra
        return "Eliminatória", extra
    m = re.search(r"round (\d)|(first|second|third|fourth|fifth) round", n)
    if m:
        i = int(m.group(1)) if m.group(1) else ["first", "second", "third", "fourth", "fifth"].index(m.group(2)) + 1
        return ["Primeira fase", "Segunda fase", "Terceira fase", "Quarta fase", "Quinta fase"][i - 1], extra
    if "grupos" in n:
        return "Fase de grupos", False
    if n.startswith("final"):
        return "Final", extra
    raise SystemExit(f"fase sem tradução: {nome}")


def grupo_pt(g: str | None) -> str | None:
    if not g:
        return None
    m = re.match(r"(?:Gruppe|Group)\s+([IVX]+|\d+)([ab]?)$", g)
    if not m:
        return g
    n = ROMANOS.get(m.group(1)) or int(m.group(1))
    return f"Grupo {n}{m.group(2).upper()}"


def campeoes() -> dict[int, str | None]:
    """Campeão de cada temporada pela RSSSF (duitchamp.html: "1925/26   SpVgg Fürth   4-1 Hertha BSC Berlin")."""
    t = texto(DADOS / "rsssf" / "duitchamp.html")
    t = t[t.find("finals of championship playoffs"):t.find("Bundesliga winners")]
    res = {}
    for l in t.split("\n"):
        m = re.match(r"^(\d{4})/\d{2}\s+(\S.*?)\s+\d+-\d+", l)
        if m:
            res[int(m.group(1))] = clubes.esd(m.group(2), int(m.group(1))) or m.group(2)
        elif re.match(r"^(\d{4})/\d{2}\s+not", l):
            res[int(l[:4])] = None
    return res


def chave(nome: str, a: int) -> str:
    c = clubes.esd(nome, a)
    if c is None:
        raise SystemExit(f"{temporada(a)}: clube antigo sem cadastro: {nome}")
    return c


# ---- Wikipédia: {{football box}} das partidas (estádio, público, árbitro, gols)
MESES_EN = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august", "september",
                                        "october", "november", "december"], 1)}


def _clube_wiki(cel: str, a: int) -> str | None:
    for alvo in re.findall(r"\[\[([^|\]]+)(?:\|([^\]]+))?\]\]", cel):
        for x in alvo:
            if x and (c := clubes.esd(x, a)):
                return c
    return clubes.esd(limpar(cel), a)


def _gols_wiki(cel: str) -> list[dict]:
    res = []
    for parte in re.split(r"<br\s*/?>", cel or ""):
        jog = limpar(re.sub(r"\{\{goal[^}]*\}\}", "", parte, flags=re.I))
        for g in re.findall(r"\{\{goal\|([^}]*)\}\}", parte, flags=re.I):
            for item in [x.strip() for x in g.split("|")]:
                if re.match(r"^\d+", item):
                    res.append({"jogador": jog, "minuto": int(re.match(r"\d+", item).group()), "tipo": "normal"})
                elif res and re.match(r"(?i)^(o\.?g|pen)", item):
                    res[-1]["tipo"] = "contra" if item.lower().startswith("o") else "penalti"
    return res


def caixas(a: int) -> list[dict]:
    arq = DADOS / "wikipedia" / f"{a}–{str(a + 1)[-2:]} German football championship.wiki"
    if not arq.exists():
        return []
    t = arq.read_text(encoding="utf-8")
    res = []
    for m in re.finditer(r"\{\{\s*football box", t, flags=re.I):
        corpo = t[m.start() + 2:_fecha(t, m.start()) - 2]
        p = {}
        for x in _partes(corpo)[1:]:
            k, _, v = x.partition("=")
            p[k.strip().lower()] = v.strip()
        d = re.search(r"(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})", limpar(p.get("date", "")))
        sc = re.search(r"(\d+)\s*[–-]\s*(\d+)", limpar(p.get("score", "")))
        if not sc:
            continue
        est = limpar(p.get("stadium", ""))
        pub = re.sub(r"\D", "", limpar(p.get("attendance", "")).split("(")[0])
        res.append({"data": f"{d.group(3)}-{MESES_EN.get(d.group(2).lower(), 0):02d}-{int(d.group(1)):02d}" if d else None,
                    "m": _clube_wiki(p.get("team1", ""), a), "v": _clube_wiki(p.get("team2", ""), a),
                    "nm": limpar(p.get("team1", "")), "nv": limpar(p.get("team2", "")),
                    "gm": int(sc.group(1)), "gv": int(sc.group(2)),
                    "estadio": est.rsplit(",", 1)[0].strip() or None if est else None,
                    "cidade": est.rsplit(",", 1)[1].strip() if "," in est else None,
                    "publico": int(pub) if pub else None, "arbitro": limpar(p.get("referee", "")) or None,
                    "gols_m": _gols_wiki(p.get("goals1", "")), "gols_v": _gols_wiki(p.get("goals2", ""))})
    return res


# ---- tabela e classificação
def calcular(jogos: list[dict]) -> dict[str, list[int]]:
    t = defaultdict(lambda: [0, 0, 0, 0, 0, 0, 0])
    for j in jogos:
        if j["gm"] is None or j["especial"]:
            continue
        for c, gp, gc in ((j["m"], j["gm"], j["gv"]), (j["v"], j["gv"], j["gm"])):
            x = t[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            x[1 if gp > gc else 2 if gp == gc else 3] += 1
            x[6] += 2 if gp > gc else 1 if gp == gc else 0
    return t


def vencedor(j: dict) -> str | None:
    if j["especial"] in ("w/o", "awd"):
        return j["m"]
    if j["especial"] == "o/w":
        return j["v"]
    if j["gm"] is None or j["gm"] == j["gv"]:
        return None
    return j["m"] if j["gm"] > j["gv"] else j["v"]


def montar(tab: dict, nomes: dict, ocorr: dict) -> list[tuple]:
    """Acrescenta as temporadas antigas ao `tab`. Devolve as linhas do resumo do relatório."""
    camp = campeoes()
    pg = pos_guerra(DADOS / "rsssf" / "duithist4763.html")
    linhas = []
    for a in TEMPORADAS_ANTIGAS:
        T = temporada(a)
        ocorr[a].extend(EXPLICACOES.get(a, []))
        if a in SEM_CAMPEONATO:
            tab["edicoes"].append({"temporada": T, "ano_inicio": a, "ano_fim": a + 1, "nome_oficial": "Campeonato Alemão",
                                   "num_clubes": None, "pontos_vitoria": 2, "formato": "sem campeonato", "campeao": None,
                                   "vice": None, "fontes": "RSSSF", "observacao": SEM_CAMPEONATO[a]})
            ocorr[a].append(SEM_CAMPEONATO[a])
            linhas.append((T, "RSSSF", 0, 0, 0, 0, 0, 0, 0, "—", ""))
            continue
        if a < 1947:
            url = f"https://www.rsssf.org/tablesd/duit{a + 1}.html"
            r = fase_final(DADOS / "rsssf" / f"duit{a + 1}.html", a + 1)
        else:
            url = "https://www.rsssf.org/tablesd/duithist4763.html"
            r = pg[a]
        jogos = []
        for x in r["jogos"]:
            fase, extra = fase_pt(x["fase"])
            j = {**x, "fase": fase, "extra": extra, "grupo": grupo_pt(x["grupo"]), "m": chave(x["nm"], a), "v": chave(x["nv"], a)}
            ab = re.search(r"abandoned at (\d+)-(\d+)", x["nota"] or "")
            if x["especial"] == "abd" and ab:   # placar na hora da interrupção (fica fora da campanha)
                j["gm"], j["gv"] = int(ab.group(1)), int(ab.group(2))
            jogos.append(j)
            nomes[j["m"]][f"rsssf:{x['nm']}"].add(a)
            nomes[j["v"]][f"rsssf:{x['nv']}"].add(a)
        grupos = {grupo_pt(g): [{**x, "clube": chave(x["nome"], a)} for x in v] for g, v in r["grupos"].items()}
        for v in grupos.values():
            for x in v:
                nomes[x["clube"]][f"rsssf:{x['nome']}"].add(a)

        # Wikipédia: dados das partidas com football box (pelo par de clubes; placar e data desempatam os jogos extras)
        fontes = ["RSSSF"]
        usados = set()
        for cx in caixas(a):
            if not cx["m"] or not cx["v"]:
                ocorr[a].append(f"partida da Wikipédia com clube sem cadastro: {cx['nm']} x {cx['nv']}")
                continue
            cand = [j for j in jogos if {j["m"], j["v"]} == {cx["m"], cx["v"]} and id(j) not in usados]
            if not cand:
                ocorr[a].append(f"partida da Wikipédia sem par na RSSSF: {cx['nm']} {cx['gm']}-{cx['gv']} {cx['nv']} ({cx['data']})")
                continue

            def placar(j):
                return (j["gm"], j["gv"]) if j["m"] == cx["m"] else (j["gv"], j["gm"])
            cand.sort(key=lambda j: (placar(j) != (cx["gm"], cx["gv"]), j["data"] != cx["data"]))
            j = cand[0]
            usados.add(id(j))
            if placar(j) != (cx["gm"], cx["gv"]):
                ocorr[a].append(f"placar diferente na Wikipédia — {clubes.exibicao(j['m'])} x {clubes.exibicao(j['v'])}: RSSSF "
                                f"{j['gm']}-{j['gv']}, Wikipédia {cx['nm']} {cx['gm']}-{cx['gv']} {cx['nv']}")
                continue
            if cx["data"] and j["data"] and cx["data"] != j["data"]:
                ocorr[a].append(f"data diferente — {clubes.exibicao(j['m'])} x {clubes.exibicao(j['v'])}: RSSSF {j['data']}, "
                                f"Wikipédia {cx['data']}; fica a da Wikipédia, que traz a ficha da partida (a RSSSF erra em "
                                f"casos conferidos: final de 1941 em 22/06, Kaiserslautern com dois jogos em 03/07/1949)")
            j["data"] = cx["data"] or j["data"]
            j["estadio"], j["cidade_wiki"], j["arbitro"] = cx["estadio"], cx["cidade"], cx["arbitro"]
            j["publico"] = j.get("publico") or cx["publico"]
            gm_, gv_ = (cx["gols_m"], cx["gols_v"]) if j["m"] == cx["m"] else (cx["gols_v"], cx["gols_m"])
            if len(gm_) == j["gm"] and len(gv_) == j["gv"]:
                j["gols_wiki"] = (gm_, gv_)
            elif gm_ or gv_:
                ocorr[a].append(f"gols da Wikipédia não batem com o placar — {clubes.exibicao(j['m'])} {j['gm']}-{j['gv']} "
                                f"{clubes.exibicao(j['v'])}: {len(gm_)} e {len(gv_)}")
            if "Wikipédia" not in fontes:
                fontes.append("Wikipédia")

        # campeão e checagem com a final
        campeao = camp.get(a)
        if isinstance(campeao, str) and campeao not in clubes.CLUBES:
            raise SystemExit(f"{T}: campeão sem cadastro: {campeao}")
        finais = [j for j in jogos if j["fase"] == "Final"]
        venc_final = vencedor(finais[-1]) if finais else None
        if a in SEM_CAMPEAO:
            ocorr[a].append(SEM_CAMPEAO[a])
            campeao = None
        elif campeao != venc_final:
            ocorr[a].append(f"campeão da lista da RSSSF ({campeao}) diferente do vencedor da final lida ({venc_final})")

        # classificação: campeão em 1º; depois a fase mais adiantada; na mesma fase, a posição no grupo e a campanha
        calc = calcular(jogos)
        prof, terceiro = defaultdict(int), {}
        for j in jogos:
            k = ORDEM.index(j["fase"]) if j["fase"] != "Disputa de 3º lugar" else ORDEM.index("Semifinal")
            for c in (j["m"], j["v"]):
                prof[c] = max(prof[c], k)
            if j["fase"] == "Disputa de 3º lugar" and (w := vencedor(j)):
                terceiro[w] = 1
                terceiro[j["v"] if w == j["m"] else j["m"]] = 0
        pos_grupo = {x["clube"]: x["posicao"] for v in grupos.values() for x in v}
        ordem = sorted(prof, key=lambda c: (c != campeao, -prof[c], -terceiro.get(c, -1), pos_grupo.get(c, 0),
                                            -calc[c][6], -(calc[c][4] - calc[c][5]), -calc[c][4], clubes.exibicao(c)))
        finalistas = {finais[0]["m"], finais[0]["v"]} if finais else set()
        vice = next((c for c in ordem if c in finalistas and c != campeao), None) if campeao else None
        for pos, c in enumerate(ordem, 1):
            x = calc[c]
            tab["classificacao_final"].append({
                "temporada": T, "posicao": pos, "clube": clubes.exibicao(c), "jogos": x[0], "vitorias": x[1], "empates": x[2],
                "derrotas": x[3], "gols_pro": x[4], "gols_contra": x[5], "pontos": x[6], "ajuste_pontos": 0,
                "situacao": "campeao" if c == campeao else None,
                "fonte": "RSSSF (fase final; campeão oficial em 1º, depois a fase alcançada)",
                "observacao": f"parou em: {ORDEM[prof[c]]}" if c != campeao and c != vice else None})

        # tabelas dos grupos x jogos
        conferidas = divergentes = 0
        for g, v in grupos.items():
            cg = calcular([j for j in jogos if j["grupo"] == g and j["fase"] == "Fase de grupos"])
            dif = []
            for x in v:
                pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]
                if cg.get(x["clube"]) != pub:
                    dif.append(f"{clubes.exibicao(x['clube'])} tabela {pub} jogos {cg.get(x['clube'])}")
                tab["tabelas_publicadas"].append({
                    "temporada": T, "fase": "Fase de grupos", "grupo": g, "posicao": x["posicao"], "nome_fonte": x["nome"],
                    "clube": clubes.exibicao(x["clube"]), "jogos": x["jogos"], "vitorias": x["vitorias"], "empates": x["empates"],
                    "derrotas": x["derrotas"], "gols_pro": x["gols_pro"], "gols_contra": x["gols_contra"], "pontos": x["pontos"],
                    "fonte": url})
            if dif:
                divergentes += 1
                for d in dif:
                    ocorr[a].append(f"tabela do {g} (RSSSF) x jogos — {d}")
            else:
                conferidas += 1

        # partidas e gols
        jogos.sort(key=lambda j: (ORDEM.index(j["fase"]), j["extra"], j["data"] or "9999", j["grupo"] or "", j["m"]))
        gols_ano = autor_ano = 0
        for i, j in enumerate(jogos, 1):
            pid = f"{a}-{i:04d}"
            obs = []
            if j["extra"]:
                obs.append("jogo de desempate (o anterior empatou)")
            nota = j["nota"] or ""
            if re.fullmatch(r"(?i)aet|a\.e\.t\.", nota):
                obs.append("prorrogação")
            elif nota:
                obs.append(f"RSSSF: {nota}")
            esp = {"w/o": "wo", "o/w": "wo", "awd": "wo", "n/p": "n/p", "abd": "abd"}.get(j["especial"])
            if esp == "wo":
                obs.append(f"vitória de {clubes.exibicao(vencedor(j))} sem jogo (W.O.)")
            if j["gm"] is not None:
                gols_ano += j["gm"] + j["gv"]
            gw = j.get("gols_wiki")
            if gw:
                for lado, lista in ((j["m"], gw[0]), (j["v"], gw[1])):
                    for g in lista:
                        # gol contra: a Wikipédia lista no lado de quem marcou no placar
                        tab["gols"].append({"partida_id": pid, "clube": clubes.exibicao(lado), "jogador": g["jogador"],
                                            "minuto": g["minuto"], "acrescimo": None, "tipo": g["tipo"], "fonte": "Wikipédia"})
                        autor_ano += 1
            elif j.get("gols") and j["gm"] is not None and len(j["gols"]) == j["gm"] + j["gv"]:
                antes = (0, 0)
                for g in j["gols"]:
                    lado = j["m"] if g["placar"][0] > antes[0] else j["v"]
                    antes = g["placar"]
                    tab["gols"].append({"partida_id": pid, "clube": clubes.exibicao(lado), "jogador": g["jogador"],
                                        "minuto": g["minuto"], "acrescimo": None, "tipo": "normal", "fonte": "RSSSF"})
                    autor_ano += 1
            local = (j.get("local") or "").replace("both in ", "").strip() or None
            tab["partidas"].append({
                "id": pid, "temporada": T, "fase": j["fase"], "grupo": j["grupo"], "rodada": None, "data": j["data"],
                "hora": None, "mandante": clubes.exibicao(j["m"]), "visitante": clubes.exibicao(j["v"]),
                "gols_mandante": j["gm"], "gols_visitante": j["gv"], "penaltis_mandante": None, "penaltis_visitante": None,
                "resultado_especial": esp, "estadio": j.get("estadio"), "cidade": j.get("cidade_wiki") or local,
                "publico": j.get("publico"), "fonte": "RSSSF" + (" + Wikipédia" if j.get("estadio") or gw else ""),
                "fonte_id": None, "gols_texto": None, "observacao": "; ".join(obs) or None, "arbitro": j.get("arbitro")})

        # fases e edição
        fases_ano = sorted({j["fase"] for j in jogos}, key=ORDEM.index)
        for k, f in enumerate(fases_ano, 1):
            ng = len({j["grupo"] for j in jogos if j["fase"] == f and j["grupo"]})
            tab["fases"].append({"temporada": T, "ordem": k, "fase": f, "tipo": "grupos" if f == "Fase de grupos" else "mata_mata",
                                 "num_grupos": ng or None,
                                 "formato_serie": "pontos_corridos" if f == "Fase de grupos" else
                                 "ida_volta" if f == "Final de grupo" else "jogo_unico",
                                 "criterio": "pontos (2 por vitória), depois média de gols" if f == "Fase de grupos" else
                                 "jogo único; empate com prorrogação e novo jogo"})
        formato = ("ligas regionais; fase final entre os campeões regionais: "
                   + ("grupos e mata-mata" if "Fase de grupos" in fases_ano and fases_ano.index("Fase de grupos") < len(fases_ano) - 2
                      else "dois grupos e final" if "Fase de grupos" in fases_ano else "mata-mata em jogo único"))
        n = len(ordem)
        tab["edicoes"].append({"temporada": T, "ano_inicio": a, "ano_fim": a + 1, "nome_oficial": "Campeonato Alemão",
                               "num_clubes": n, "pontos_vitoria": 2, "formato": formato,
                               "campeao": clubes.exibicao(campeao) if campeao else None,
                               "vice": clubes.exibicao(vice) if vice else None, "fontes": " + ".join(fontes),
                               "observacao": SEM_CAMPEAO.get(a)})
        com_placar = [j for j in jogos if j["gm"] is not None]
        tab["conferencia"].append({"temporada": T, "jogos": len(com_placar), "jogos_esperados": None,
                                   "tabelas_conferidas": conferidas, "tabelas_divergentes": divergentes, "gols": gols_ano,
                                   "gols_com_autor": autor_ano,
                                   "observacao": f"campeão {clubes.exibicao(campeao) if campeao else 'não atribuído'} (RSSSF)"})
        linhas.append((T, " + ".join(fontes), n, len(com_placar), 0, gols_ano, autor_ano, conferidas, divergentes,
                       clubes.exibicao(campeao) if campeao else "—", ""))
        print(f"{T}: {len(jogos)} jogos, {n} clubes, grupos {conferidas} ok / {divergentes} div, gols {gols_ano} ({autor_ano} c/ "
              f"autor), campeão {clubes.exibicao(campeao) if campeao else '—'}", flush=True)
    return linhas
