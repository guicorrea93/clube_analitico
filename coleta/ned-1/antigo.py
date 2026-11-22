"""Campeonato holandês antes da Eredivisie (1888/89 a 1955/56), no mesmo pacote ned-1 (decisão do Guilherme, 22/11/2026).

Fonte: RSSSF, uma página por temporada (tablesn/ned1889.html ... ned1954.html, pelo ano final; ned55.html e ned56.html
para as temporadas profissionais de 1954/55 e 1955/56) e a lista de campeões (nedchamp.html).

- 1897/98 a 1955/56: a fase final do título (os campeões regionais em pontos corridos), com os jogos da matriz de resultados
  (sem data) ou, nas temporadas profissionais, os jogos datados; a tabela da RSSSF é conferida com os jogos.
- 1888/89 a 1896/97 (só a liga do oeste) e as temporadas em que a página não tem a fase final em formato legível: o campeão
  oficial e a tabela publicada da Eerste Klasse, sem os jogos (pendência registrada).
- 1944/45: sem campeonato (guerra). 1892/93: sem campeão declarado.

Uso: montar(tab, nomes, ocorr) acrescenta edições, fases, partidas, classificação, tabelas publicadas e conferência ao `tab`
do importador (importar.py chama no fim).
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

import clubes_ned as clubes
from edicoes import DADOS
from rsssf_antigo import TABELA, fase_final, texto

TEMPORADAS_ANTIGAS = list(range(1888, 1956))
SEM_CAMPEONATO = {1944: "sem campeonato (Segunda Guerra Mundial)"}
NAO_OFICIAIS = {1914: "edição não oficial na época (Primeira Guerra Mundial); contada hoje entre os títulos",
                1939: "campeonato de emergência (Segunda Guerra Mundial); contado hoje entre os títulos"}
JOGO_DATADO = re.compile(r"^\s*(\S.*?)\s+-\s+(\S.*?)\s+(\d+)\s*-\s*(\d+)\s+\(\s*(\d+)/\s*(\d+)/(\d{4})\)")
TABELA_PRO = re.compile(r"^\s*(\d+)\s+(\S.*?)\s+(\d+)\s+(\d+)-\s*(\d+)-\s*(\d+)\s+(\d+)\s+(\d+)-\s*(\d+)")


def temporada(a: int) -> str:
    return f"{a}/{str(a + 1)[-2:]}"


def campeoes() -> dict[int, str | None]:
    """Campeão de cada temporada pela RSSSF (nedchamp.html: "1956/57 Ajax"; "not awarded"/"no competition" = sem)."""
    t = texto(DADOS / "rsssf" / "nedchamp.html")
    res = {}
    for m in re.finditer(r"^(\d{4})/\d{2}\s+(.+?)\s*$", t, re.M):
        a = int(m.group(1))
        if a in TEMPORADAS_ANTIGAS and a not in res:
            nome = re.sub(r"\s*(\(.*?\)|\[.*?\])\s*", " ", m.group(2)).strip()
            res[a] = None if re.search(r"(?i)not|no |abandon|none|-{2,}", nome) else clubes.esd(nome, a)
    return res


def chave(nome: str, a: int) -> str:
    c = clubes.esd(nome, a)
    if c is None:
        raise SystemExit(f"{temporada(a)}: clube antigo sem cadastro: {nome}")
    return c


def calcular(jogos: list[dict]) -> dict[str, list[int]]:
    t = defaultdict(lambda: [0, 0, 0, 0, 0, 0, 0])
    for j in jogos:
        for c, gp, gc in ((j["m"], j["gm"], j["gv"]), (j["v"], j["gv"], j["gm"])):
            x = t[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            x[1 if gp > gc else 2 if gp == gc else 3] += 1
            x[6] += 2 if gp > gc else 1 if gp == gc else 0
    return t


def pagina(a: int) -> Path:
    if a in (1954, 1955):
        return DADOS / "rsssf" / f"ned{str(a + 1)[-2:]}.html"
    return DADOS / "rsssf" / f"ned{a + 1}.html"


def fase_profissional(arq: Path) -> dict:
    """1954/55 e 1955/56: jogos datados e tabela da seção "Championship Playoff" da página profissional."""
    t = texto(arq)
    sec = t[t.rfind("Championship Playoff"):]
    fim = re.search(r"\n\s*(?:1e Klasse|Eerste Klasse|Hoofdklasse|2e Klasse|Tweede Klasse|Promotion|Relegation|\d{4}/\d{2}\s*\n)",
                    sec[30:])
    sec = sec[:fim.start() + 30] if fim else sec
    jogos, tabela, fechada = [], [], False
    for l in sec.split("\n"):
        m = JOGO_DATADO.match(l)
        if m:
            d, mes, ano = int(m.group(5)), int(m.group(6)), int(m.group(7))
            jogos.append({"nm": m.group(1).strip(), "nv": m.group(2).strip(), "gm": int(m.group(3)), "gv": int(m.group(4)),
                          "data": f"{ano:04d}-{mes:02d}-{d:02d}"})
            continue
        m = TABELA_PRO.match(l)
        if m and not (tabela and int(m.group(1)) <= tabela[-1]["posicao"]) and not fechada:
            pos, nome, j, v, e, d, p, gp, gc = m.groups()
            tabela.append({"posicao": int(pos), "nome": nome.strip(), "jogos": int(j), "vitorias": int(v), "empates": int(e),
                           "derrotas": int(d), "pontos": int(p), "gols_pro": int(gp), "gols_contra": int(gc)})
        elif m:
            fechada = True   # a numeração recomeçou: outra tabela (as ligas emendadas na página)
    nomes_fase = {x["nome"] for x in tabela}
    jogos = [j for j in jogos if j["nm"] in nomes_fase and j["nv"] in nomes_fase]
    desempate = re.search(r"Playoff:\s*(.+?)\s+-\s+(.+?)\s+(\d+)-(\d+)", sec)
    return {"jogos": jogos, "tabela": tabela, "desempate": desempate.groups() if desempate else None}


def tabela_eerste_klasse(arq: Path) -> list[dict]:
    """Primeira tabela final ("Final Table:") depois do primeiro título "Eerste Klasse" da página (a liga nacional, no
    oeste), nas temporadas sem fase final."""
    t = texto(arq)
    i = t.find("\nEerste Klasse\n", t.find("\nEerste Klasse\n") + 1)   # o primeiro é o índice do topo
    if i < 0:
        i = t.find("\nEerste Klasse\n")
    j = t.find("Final Table:", i)
    if i < 0 or j < 0:
        return []
    res = []
    for l in t[j:j + 3000].split("\n")[1:]:
        m = re.match(r"^\s*(\d+)\.\s*(\S.*?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*-\s*(\d+)\s+(\d+)", l)
        if m:
            pos, nome, j_, v, e, d, gp, gc, p = m.groups()
            res.append({"posicao": int(pos), "nome": re.sub(r"\s*\(.*?\)\s*$", "", nome).strip(), "jogos": int(j_),
                        "vitorias": int(v), "empates": int(e), "derrotas": int(d), "gols_pro": int(gp), "gols_contra": int(gc),
                        "pontos": int(p)})
        elif res and not l.strip():
            break
    return res


def montar(tab: dict, nomes: dict, ocorr: dict) -> list[tuple]:
    """Acrescenta as temporadas antigas ao `tab`. Devolve as linhas do resumo do relatório."""
    camp = campeoes()
    linhas = []
    for a in TEMPORADAS_ANTIGAS:
        T = temporada(a)
        arq = pagina(a)
        url = f"https://www.rsssf.org/tablesn/{arq.name}"
        if a in SEM_CAMPEONATO:
            tab["edicoes"].append({"temporada": T, "ano_inicio": a, "ano_fim": a + 1, "nome_oficial": "Campeonato Holandês",
                                   "num_clubes": None, "pontos_vitoria": 2, "formato": "sem campeonato", "campeao": None,
                                   "vice": None, "fontes": "RSSSF", "observacao": SEM_CAMPEONATO[a]})
            ocorr[a].append(SEM_CAMPEONATO[a])
            linhas.append((T, "RSSSF", 0, 0, 0, 0, 0, 0, "—", ""))
            continue
        jogos, tabela, fase_nome, desempate, regionais = [], [], "Fase final", None, []
        if a in (1954, 1955):
            r = fase_profissional(arq)
            for x in r["jogos"]:
                jogos.append({"m": chave(x["nm"], a), "v": chave(x["nv"], a), "nm": x["nm"], "gm": x["gm"], "gv": x["gv"],
                              "data": x["data"], "especial": None})
            tabela, desempate = r["tabela"], r["desempate"]
        else:
            r = fase_final(arq) if arq.exists() else None
            if r and r["tabela"]:
                regionais = r["campeoes_regionais"]
                for (nm, nv), (g1, g2, dado) in r["matriz"].items():
                    jogos.append({"m": chave(nm, a), "v": chave(nv, a), "nm": nm, "gm": g1, "gv": g2, "data": None,
                                  "especial": "awd" if dado else None})
                tabela = r["tabela"]
                desempate = next((re.search(r"Playoff:\s*(.+?)\s+-\s+(.+?)\s+(\d+)-(\d+)", n).groups()
                                  for n in r["notas"] if re.search(r"Playoff:\s*\S.+-.+\d+-\d+", n)), None)
                for n in r["notas"]:
                    ocorr[a].append(f"nota da RSSSF: {n}")
            elif arq.exists():
                tabela, fase_nome = tabela_eerste_klasse(arq), "Eerste Klasse"
                ocorr[a].append("a página da RSSSF não tem a fase final em formato legível: entram o campeão oficial e a tabela "
                                "publicada da Eerste Klasse, sem os jogos")
        for x in tabela:
            x["clube"] = chave(x["nome"], a)
            nomes[x["clube"]][f"rsssf:{x['nome']}"].add(a)
        for j in jogos:
            nomes[j["m"]][f"rsssf:{j['nm']}"].add(a)
        campeao = camp.get(a)
        if campeao is None and a not in camp:
            ocorr[a].append("a lista de campeões da RSSSF não traz esta temporada")
        # ordem: a da tabela da RSSSF, com o campeão oficial em 1º (título decidido em jogo de desempate)
        ordem = [x["clube"] for x in sorted(tabela, key=lambda x: x["posicao"])]
        if campeao and campeao in ordem and ordem[0] != campeao:
            ordem.remove(campeao)
            ordem.insert(0, campeao)
        if desempate:
            ocorr[a].append(f"título decidido em jogo de desempate: {desempate[0]} {desempate[2]}-{desempate[3]} {desempate[1]} "
                            f"(fica de fora dos jogos da fase final)")
        if campeao and campeao not in ordem:
            ocorr[a].append(f"o campeão oficial ({campeao}) não está na tabela lida")
            ordem.insert(0, campeao)
        calc = calcular(jogos) if jogos else {}
        ajuste = {}
        for x in tabela:   # punição: a linha da RSSSF fecha com os jogos, menos nos pontos (a menos)
            c_ = calc.get(x["clube"])
            if c_ and c_[:6] == [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"]]                     and x["pontos"] < c_[6]:
                ajuste[x["clube"]] = x["pontos"] - c_[6]
                c_[6] = x["pontos"]
                ocorr[a].append(f"punição tirada da tabela da RSSSF: {x['clube']} {ajuste[x['clube']]:+d} pontos")
        conferidas = divergentes = 0
        if jogos and tabela:
            dif = [f"{x['clube']} tabela {[x['jogos'], x['vitorias'], x['empates'], x['derrotas'], x['gols_pro'], x['gols_contra'], x['pontos']]} "
                   f"jogos {calc.get(x['clube'])}" for x in tabela
                   if calc.get(x["clube"]) != [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"],
                                               x["gols_contra"], x["pontos"]]]
            if dif:
                divergentes = 1
                for d in dif:
                    ocorr[a].append(f"tabela publicada x jogos (RSSSF) — {d}")
            else:
                conferidas = 1
        for x in tabela:
            tab["tabelas_publicadas"].append({
                "temporada": T, "fase": fase_nome, "grupo": None, "posicao": x["posicao"], "nome_fonte": x["nome"],
                "clube": x["clube"], "jogos": x["jogos"], "vitorias": x["vitorias"], "empates": x["empates"],
                "derrotas": x["derrotas"], "gols_pro": x["gols_pro"], "gols_contra": x["gols_contra"], "pontos": x["pontos"],
                "fonte": url})
        por_clube = {x["clube"]: x for x in tabela}
        for pos, c in enumerate(ordem, 1):
            x = calc.get(c) or ([por_clube[c][k] for k in ("jogos", "vitorias", "empates", "derrotas", "gols_pro",
                                                          "gols_contra", "pontos")] if c in por_clube else [None] * 7)
            tab["classificacao_final"].append({
                "temporada": T, "posicao": pos, "clube": c, "jogos": x[0], "vitorias": x[1], "empates": x[2], "derrotas": x[3],
                "gols_pro": x[4], "gols_contra": x[5], "pontos": x[6], "ajuste_pontos": ajuste.get(c, 0),
                "situacao": "campeao" if c == campeao else None,
                "fonte": "RSSSF (fase final; campeão oficial em 1º)" if fase_nome == "Fase final" else "RSSSF (Eerste Klasse)",
                "observacao": None})
        for i, j in enumerate(sorted(jogos, key=lambda j: (j["data"] or "9999", j["m"])), 1):
            tab["partidas"].append({
                "id": f"{a}-{i:04d}", "temporada": T, "fase": fase_nome, "grupo": None, "rodada": None, "data": j["data"],
                "hora": None, "mandante": j["m"], "visitante": j["v"], "gols_mandante": j["gm"], "gols_visitante": j["gv"],
                "penaltis_mandante": None, "penaltis_visitante": None, "resultado_especial": j["especial"], "estadio": None,
                "cidade": None, "publico": None, "fonte": "RSSSF", "fonte_id": None, "gols_texto": None,
                "observacao": "vitória dada fora de campo (5*0 na RSSSF)" if j["especial"] else None, "arbitro": None})
        obs = "; ".join(x for x in (
            NAO_OFICIAIS.get(a, ""),
            ("campeões regionais: " + "; ".join(regionais)) if regionais else "",
            "sem campeão declarado" if a in camp and camp[a] is None else "") if x) or None
        n = len(ordem)
        tab["edicoes"].append({"temporada": T, "ano_inicio": a, "ano_fim": a + 1, "nome_oficial": "Campeonato Holandês",
                               "num_clubes": n, "pontos_vitoria": 2,
                               "formato": "ligas regionais e fase final em pontos corridos entre os campeões regionais"
                               if fase_nome == "Fase final" else "Eerste Klasse (liga do oeste)",
                               "campeao": campeao, "vice": ordem[1] if len(ordem) > 1 else None, "fontes": "RSSSF",
                               "observacao": obs})
        tab["fases"].append({"temporada": T, "ordem": 1, "fase": fase_nome, "tipo": "liga", "num_grupos": None,
                             "formato_serie": "pontos_corridos", "criterio": "pontos (desempate em jogo extra)"})
        gols = sum(j["gm"] + j["gv"] for j in jogos)
        tab["conferencia"].append({"temporada": T, "jogos": len(jogos), "jogos_esperados": n * (n - 1) if jogos else None,
                                   "tabelas_conferidas": conferidas, "tabelas_divergentes": divergentes, "gols": gols,
                                   "gols_com_autor": 0, "observacao": f"campeão {campeao or 'não atribuído'} (RSSSF)"})
        linhas.append((T, "RSSSF", n, len(jogos), gols, 0, conferidas, divergentes, campeao or "—", ""))
    return linhas
