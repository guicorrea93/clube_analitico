"""Campeonatos turcos antes da liga nacional (antes de 1959), no mesmo pacote tur-1 (pedido do Guilherme, 24/11/2026).

Três competições:
  Türkiye Futbol Şampiyonası (1924-1951)  mata-mata (e, de 1942 em diante, grupo final) entre os campeões regionais;
  Millî Küme (1937-1950)                  liga dos melhores clubes de Istambul, Ancara e Esmirna (vitória 3, empate 2,
                                          derrota 1 ponto na maior parte das edições);
  Federasyon Kupası (1956/57 e 1957/58)   eliminatórias e grupo final, para escolher o representante na Copa dos
                                          Campeões.
Títulos: a federação reconhece as duas Federasyon Kupası como campeonato (desde 2002) e não reconhece o Şampiyonası nem a
Millî Küme. Pela regra D-09 (seguir a federação), só as Federasyon Kupası têm `campeao`; nas outras o vencedor está na
classificação e na observação, sem contar título.

Fonte: Wikipédia (en), artigo de cada edição (coleta/tur-1/wiki_antigo.py): fichas de jogo, matriz de resultados e tabelas.
Conferência: tabela da Wikipédia e da RSSSF (turkhist.html) com os jogos.

Uso: montar(tab, nomes, ocorr) acrescenta as edições ao `tab` do importador e devolve as linhas do resumo do relatório.
"""
from __future__ import annotations

import re
from collections import defaultdict

import clubes_tur as clubes
import wiki_antigo as w
from edicoes import DADOS
from rsssf_tur import ler as ler_rsssf

PASTA = DADOS / "wikipedia-antigo"
URL = "https://en.wikipedia.org/wiki/"
URL_RSSSF = "https://www.rsssf.org/tablest/turkhist.html"
NAO_RECONHECIDO = "título não reconhecido pela federação turca (a federação só conta o campeonato desde 1959 e as Federasyon Kupası)"
# (artigo, temporada, ano inicial, ano final, competição, vencedor, vice)
TFS, MK, FK = "Türkiye Futbol Şampiyonası", "Millî Küme", "Federasyon Kupası"
EDICOES = [
    ("1924 Turkish Football Championship", "1924 (Şampiyonası)", 1924, 1924, TFS, "Harp Okulu", "Bahriye"),
    ("1927 Turkish Football Championship", "1927 (Şampiyonası)", 1927, 1927, TFS, "Muhafızgücü", "Altınordu"),
    ("1932 Turkish Football Championship", "1932 (Şampiyonası)", 1932, 1932, TFS, "İstanbulspor", "Altınordu"),
    ("1933 Turkish Football Championship", "1933 (Şampiyonası)", 1933, 1933, TFS, "Fenerbahçe", "İzmirspor"),
    ("1934 Turkish Football Championship", "1934 (Şampiyonası)", 1934, 1934, TFS, "Beşiktaş", "Altay"),
    ("1935 Turkish Football Championship", "1935 (Şampiyonası)", 1935, 1935, TFS, "Fenerbahçe", "Altınordu"),
    ("1937 Turkish National Division", "1937 (Millî Küme)", 1937, 1937, MK, "Fenerbahçe", "Galatasaray"),
    ("1938 Turkish National Division", "1938 (Millî Küme)", 1938, 1938, MK, "Güneş", "Beşiktaş"),
    ("1939 Turkish National Division", "1939 (Millî Küme)", 1939, 1939, MK, "Galatasaray", "Ankara Demirspor"),
    ("1940 Turkish National Division", "1940 (Millî Küme)", 1940, 1940, MK, "Fenerbahçe", "Galatasaray"),
    ("1940 Turkish Football Championship", "1940 (Şampiyonası)", 1940, 1940, TFS, "Eskişehir Demirspor", "Fenerbahçe"),
    ("1941 Turkish National Division", "1941 (Millî Küme)", 1941, 1941, MK, "Beşiktaş", "Galatasaray"),
    ("1941 Turkish Football Championship", "1941 (Şampiyonası)", 1941, 1941, TFS, "Gençlerbirliği", "Beşiktaş"),
    ("1942 Turkish Football Championship", "1942 (Şampiyonası)", 1942, 1942, TFS, "Harp Okulu", "Göztepe"),
    ("1943 Turkish National Division", "1943 (Millî Küme)", 1943, 1943, MK, "Fenerbahçe", "Galatasaray"),
    ("1944 Turkish National Division", "1944 (Millî Küme)", 1944, 1944, MK, "Beşiktaş", "Fenerbahçe"),
    ("1944 Turkish Football Championship", "1944 (Şampiyonası)", 1944, 1944, TFS, "Fenerbahçe", "Harp Okulu"),
    ("1945 Turkish National Division", "1945 (Millî Küme)", 1945, 1945, MK, "Fenerbahçe", "Beşiktaş"),
    ("1945 Turkish Football Championship", "1945 (Şampiyonası)", 1945, 1945, TFS, "Harp Okulu", "İzmit Harp Filosu"),
    ("1946 Turkish National Division", "1946 (Millî Küme)", 1946, 1946, MK, "Fenerbahçe", "Beşiktaş"),
    ("1946 Turkish Football Championship", "1946 (Şampiyonası)", 1946, 1946, TFS, "Gençlerbirliği", "Beşiktaş"),
    ("1947 Turkish National Division", "1947 (Millî Küme)", 1947, 1947, MK, "Beşiktaş", "Fenerbahçe"),
    ("1947 Turkish Football Championship", "1947 (Şampiyonası)", 1947, 1947, TFS, "Ankara Demirspor", "Fenerbahçe"),
    ("1949 Turkish Football Championship", "1949 (Şampiyonası)", 1949, 1949, TFS, "Ankaragücü", "Galatasaray"),
    ("1950 Turkish National Division", "1950 (Millî Küme)", 1950, 1950, MK, "Fenerbahçe", "Galatasaray"),
    ("1950 Turkish Football Championship", "1950 (Şampiyonası)", 1950, 1950, TFS, "Göztepe", "Gençlerbirliği"),
    ("1951 Turkish Football Championship", "1951 (Şampiyonası)", 1951, 1951, TFS, "Beşiktaş", "Altay"),
    ("1956–57 Federation Cup", "1956/57 (Federasyon Kupası)", 1956, 1957, FK, "Beşiktaş", "Galatasaray"),
    ("1957–58 Federation Cup", "1957/58 (Federasyon Kupası)", 1957, 1958, FK, "Beşiktaş", "Galatasaray"),
]
# pontos por vitória, empate e derrota: 3-2-1 na maior parte; 2-1-0 nestas edições (tabelas da RSSSF)
PONTOS_2_1_0 = {"1943 (Millî Küme)", "1944 (Millî Küme)", "1944 (Şampiyonası)", "1947 (Şampiyonası)",
                "1956/57 (Federasyon Kupası)", "1957/58 (Federasyon Kupası)"}
# explicação das divergências que sobram (vai para o relatório)
EXPLICACOES = {
    "1938 (Millî Küme)": ["o Fenerbahçe abandonou a liga depois da 4ª rodada; os jogos que faltavam valeram 3-0 e os "
                          "pontos para os adversários (sem ponto para o Fenerbahçe), e as tabelas contam os gols de outro jeito"],
    "1939 (Millî Küme)": ["Galatasaray com 35 pontos na RSSSF (36 pela conta 3-2-1): derrota por W.O. não dava ponto"],
    "1946 (Millî Küme)": ["duas fases (liga e grupo final de 4); a tabela do grupo final na Wikipédia não traz os gols"],
}
GENERICOS = {"results", "league table", "standings", "season", "overview", "teams", "format", "references",
             "external links", "matches", "table", "fixtures", "final standings", "league"}
TRADUCAO = [(r"(?i)^round (\d+)$", lambda m: f"{m.group(1)}ª eliminatória"), (r"(?i)^preliminary round$", "Eliminatória prévia"),
            (r"(?i)^quarter-?finals?$", "Quartas de final"), (r"(?i)^semi-?finals?$", "Semifinal"),
            (r"(?i)^third place.*$", "Disputa de 3º lugar"), (r"(?i)^final group$", "Grupo final"), (r"(?i)^finals?$", "Final"),
            (r"(?i)^group stage$", "Fase de grupos"), (r"(?i)^final stage$", "Fase final"), (r"(?i)^group final$", "Final do grupo"),
            (r"(?i)^play-?offs?$", "Desempate"), (r"(?i)^qualification$", "Eliminatórias"),
            (r"(?i)^(.+?) group$", lambda m: f"Grupo de {m.group(1).replace('Istanbul', 'Istambul').replace('İzmir', 'Esmirna').replace('Ankara', 'Ancara')}")]


def traduzir(s: str) -> str:
    for a, b in TRADUCAO:
        if re.match(a, s):
            return re.sub(a, b, s)
    return s


def nome_fase(secao: list[str], comp: str) -> tuple[str, str | None]:
    cam = [s for s in secao if s.lower() not in GENERICOS and not re.match(r"(?i)^\d{4}", s)]
    grupo = next((traduzir(s) for s in cam if re.search(r"(?i)\bgroup$", s) and not re.match(r"(?i)^final group$", s)), None)
    resto = [traduzir(s) for s in cam if not (re.search(r"(?i)\bgroup$", s) and not re.match(r"(?i)^final group$", s))]
    if not resto and not grupo:
        return ("Liga" if comp == MK else "Fase única"), None
    return (" · ".join(resto) if resto else "Fase de grupos"), grupo


def chave(nome: str, alvo: str | None, a: int) -> str:
    c = (clubes.esd(alvo, a) if alvo else None) or clubes.esd(nome, a)
    if c is None:
        raise SystemExit(f"era antiga turca ({a}): clube sem cadastro: {nome} ({alvo})")
    return c


def calcular(jogos: list[dict], pts=(2, 1, 0)) -> dict[str, list[int]]:
    t = defaultdict(lambda: [0] * 7)
    for j in jogos:
        for c, gp, gc in ((j["m"], j["gm"], j["gv"]), (j["v"], j["gv"], j["gm"])):
            x = t[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            k = 1 if gp > gc else 2 if gp == gc else 3
            x[k] += 1
            x[6] += pts[k - 1]
    return t


def rsssf_tabela(rs: dict, a: int, comp: str):
    """Tabela da RSSSF da competição no ano (título "Millî Küme" ou "Final Group")."""
    for tb in rs.get(a, []):
        t = (tb["titulo"] or "").lower()
        if (comp == MK and "küme" in t) or (comp != MK and "final group" in t):
            return tb
    return None


def montar(tab: dict, nomes: dict, ocorr: dict) -> list[tuple]:
    rs = ler_rsssf(DADOS / "rsssf" / "turkhist.html")
    linhas = []
    for artigo, T, a1, a2, comp, venc, vice in EDICOES:
        texto = (PASTA / f"{artigo}.wiki").read_text(encoding="utf-8")
        url = URL + artigo.replace(" ", "_")
        r = w.ler(texto)
        jogos, vistos = [], {}
        for x in r["jogos"]:
            m, v = chave(x["nm"], x["tm"], a1), chave(x["nv"], x["tv"], a1)
            fase, grupo = nome_fase(x["secao"], comp)
            j = {**x, "m": m, "v": v, "fase": fase, "grupo": grupo}
            k = (m, v, x["gm"], x["gv"])
            if k in vistos and x["fonte"] == "matriz":   # o mesmo jogo na ficha e na matriz: fica a ficha
                continue
            vistos[k] = j
            jogos.append(j)
            nomes[m]["wikipedia-antigo"].add(a1)
            nomes[v]["wikipedia-antigo"].add(a1)
        conta = comp == FK
        campeao = clubes.esd(venc, a1)
        vice_c = clubes.esd(vice, a1)
        ocorr[T].extend(EXPLICACOES.get(T, []))
        ocorr[T].append(f"{comp}: vencedor {clubes.exibicao(campeao)}, vice {clubes.exibicao(vice_c)}"
                        + ("" if conta else f" — {NAO_RECONHECIDO}"))
        # ---- conferência e classificação
        pts = (2, 1, 0) if T in PONTOS_2_1_0 else (3, 2, 1)
        conferidas = divergentes = 0
        tabelas_ed = []
        for tb in r["tabelas"]:
            linhas_tb = []
            for x in tb["times"]:
                c = chave(x["nome"], None, a1)
                nomes[c]["wikipedia-antigo"].add(a1)
                j_ = sum(x[k] or 0 for k in ("vitorias", "empates", "derrotas"))
                linhas_tb.append(dict(x, clube=c, jogos=j_))
            tabelas_ed.append(("Wikipédia", url, linhas_tb))
        tb_rs = rsssf_tabela(rs, a1, comp)
        if tb_rs:
            linhas_tb = []
            for x in tb_rs["linhas"]:
                # a RSSSF junta a cidade ao nome ("Doğanspor İzmir", "Güneş Istanbul")
                sem_cidade = re.sub(r"\s+(Istanbul|İzmir|Izmir|Ankara|Adana|Eskişehir|Bursa|İzmit|Izmit|Trabzon)$", "", x["nome"])
                c = clubes.esd(x["nome"], a1) or clubes.esd(sem_cidade, a1)
                if c is None:
                    raise SystemExit(f"era antiga turca ({a1}): nome da RSSSF sem cadastro: {x['nome']}")
                nomes[c][f"rsssf:{x['nome']}"].add(a1)
                linhas_tb.append(dict(x, clube=c))
            tabelas_ed.append(("RSSSF", URL_RSSSF, linhas_tb))
        ordem_tabela, pontos_rsssf = None, {}
        for fonte, u, linhas_tb in tabelas_ed:
            if not linhas_tb:
                continue
            conj = {x["clube"] for x in linhas_tb}
            js = [j for j in jogos if {j["m"], j["v"]} <= conj and j["fase"] in ("Liga", "Grupo final", "Fase única")] \
                or [j for j in jogos if {j["m"], j["v"]} <= conj]
            calc = calcular(js, pts)
            fase_t = js[0]["fase"] if js else "Liga"
            erro = []
            for x in linhas_tb:
                pts_tab = x.get("pontos")
                if pts_tab is None:   # Wikipédia: pontos pelo sistema da época, mais o ajuste
                    pts_tab = pts[0] * (x["vitorias"] or 0) + pts[1] * (x["empates"] or 0) + pts[2] * (x["derrotas"] or 0) + (x.get("ajuste") or 0)
                pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], pts_tab]
                tab["tabelas_publicadas"].append({
                    "temporada": T, "fase": fase_t, "grupo": None, "posicao": x["posicao"], "nome_fonte": x["nome"],
                    "clube": clubes.exibicao(x["clube"]), "jogos": pub[0], "vitorias": pub[1], "empates": pub[2],
                    "derrotas": pub[3], "gols_pro": pub[4], "gols_contra": pub[5], "pontos": pub[6], "fonte": u})
                c = calc.get(x["clube"])
                if js and c and pub[:6] != c[:6]:
                    erro.append(f"{clubes.exibicao(x['clube'])} tabela {pub[:6]} jogos {c[:6]}")
            if js:
                if erro:
                    divergentes += 1
                    for e_ in erro[:5]:
                        ocorr[T].append(f"tabela ({fonte}) x jogos — {e_}")
                else:
                    conferidas += 1
            if ordem_tabela is None:
                ordem_tabela = [x["clube"] for x in linhas_tb]
                pontos_tabela = {x["clube"]: x for x in linhas_tb}
            if fonte == "RSSSF":   # os pontos da RSSSF valem (trazem as exceções, como W.O. sem ponto)
                pontos_rsssf = {x["clube"]: x["pontos"] for x in linhas_tb}
        total = calcular(jogos, pts)
        fases_ordem = list(dict.fromkeys((j["fase"], j["grupo"]) for j in jogos))
        fases_clube = defaultdict(set)
        for j in jogos:
            for c in (j["m"], j["v"]):
                fases_clube[c].add(fases_ordem.index((j["fase"], j["grupo"])))
        if comp == MK and ordem_tabela:
            ordem = ordem_tabela + [c for c in total if c not in ordem_tabela]
        else:
            topo = [campeao, vice_c] + [c for c in (ordem_tabela or []) if c not in (campeao, vice_c)]
            resto = sorted((c for c in total if c not in topo),
                           key=lambda c: (-max(fases_clube[c]), -len(fases_clube[c]), -total[c][6], -(total[c][4] - total[c][5])))
            ordem = topo + resto
        for pos, c in enumerate(ordem, 1):
            j_, v_, e_, d_, gp, gc, p = total[c] if c in total else [0] * 7
            if comp == MK and ordem_tabela and c in pontos_tabela:
                x = pontos_tabela[c]
                p_of = pontos_rsssf.get(c, pts[0] * (x["vitorias"] or 0) + pts[1] * (x["empates"] or 0)
                                       + pts[2] * (x["derrotas"] or 0) + (x.get("ajuste") or 0))
                obs = ("vitória 3, empate 2, derrota 1 ponto" if pts == (3, 2, 1) else "vitória 2, empate 1") + " (sistema da época)"
            else:
                p_of = p
                obs = (f"soma de todas as fases (vitória {pts[0]}, empate {pts[1]}, derrota {pts[2]}); sem classificação oficial "
                       "além do vencedor e do vice")
            if pos == 1 and not conta:
                obs = f"vencedor ({NAO_RECONHECIDO}); " + obs
            tab["classificacao_final"].append({
                "temporada": T, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
                "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": p_of, "ajuste_pontos": p_of - p,
                "situacao": "campeao" if (conta and c == campeao) else None,
                "fonte": "Wikipédia (en) e RSSSF" + ("" if comp == MK else "; ordem montada (vencedor, vice e fase alcançada)"),
                "observacao": obs})
        # ---- partidas e gols
        jogos.sort(key=lambda j: (j["data"] or "9999", fases_ordem.index((j["fase"], j["grupo"]))))
        suf = {TFS: "s", MK: "m", FK: "f"}[comp]
        autor = 0
        for i, j in enumerate(jogos, 1):
            pid = f"{a1}{suf}-{i:04d}"
            extra = (j["extra"] or "").lower()
            esp = "w/o" if re.search(r"w\.?/?o\b|walkover", extra) else "awd" if "awarded" in extra or "forfeit" in extra else None
            tab["partidas"].append({
                "id": pid, "temporada": T, "fase": j["fase"], "grupo": j["grupo"], "rodada": None, "data": j["data"], "hora": None,
                "mandante": clubes.exibicao(j["m"]), "visitante": clubes.exibicao(j["v"]), "gols_mandante": j["gm"],
                "gols_visitante": j["gv"], "penaltis_mandante": None, "penaltis_visitante": None, "resultado_especial": esp,
                "estadio": j["estadio"], "cidade": j["local"], "publico": None,
                "fonte": "Wikipédia (en)" + {"matriz": " (matriz, sem data)", "eliminatoria": " (sem data)"}.get(j["fonte"], ""),
                "fonte_id": None, "gols_texto": None, "observacao": j["extra"] or None, "arbitro": j["arbitro"]})
            gm_, gv_ = j["gols_m"], j["gols_v"]
            if (gm_ or gv_) and (len(gm_), len(gv_)) == (j["gm"], j["gv"]):
                for lado, gl in ((j["m"], gm_), (j["v"], gv_)):
                    for jog, mi in gl:
                        tab["gols"].append({"partida_id": pid, "clube": clubes.exibicao(lado), "jogador": jog, "minuto": mi,
                                            "acrescimo": None, "tipo": "normal", "fonte": "Wikipédia (en)"})
                autor += len(gm_) + len(gv_)
        # ---- edição, fases, conferência
        fases_unicas = list(dict.fromkeys(f for f, _ in fases_ordem))
        for i, f in enumerate(fases_unicas, 1):
            gs = {g for f2, g in fases_ordem if f2 == f and g}
            liga = f in ("Liga", "Grupo final")
            tab["fases"].append({"temporada": T, "ordem": i, "fase": f, "tipo": "grupos" if liga or gs else "mata_mata",
                                 "num_grupos": len(gs) or (1 if liga else None),
                                 "formato_serie": "pontos_corridos" if liga else "jogo_unico", "criterio": "pontos" if liga else "resultado"})
        gols = sum(j["gm"] + j["gv"] for j in jogos)
        obs_ed = (f"{comp}: título reconhecido pela federação desde 2002" if conta else
                  f"{comp}: vencedor {clubes.exibicao(campeao)}; {NAO_RECONHECIDO}")
        tab["edicoes"].append({"temporada": T, "ano_inicio": a1, "ano_fim": a2, "nome_oficial": comp, "num_clubes": len(ordem),
                               "pontos_vitoria": pts[0], "formato": " → ".join(fases_unicas),
                               "campeao": clubes.exibicao(campeao) if conta else None,
                               "vice": clubes.exibicao(vice_c) if conta else None,
                               "fontes": "Wikipédia (en)" + (" + RSSSF" if tb_rs else ""), "observacao": obs_ed})
        tab["conferencia"].append({"temporada": T, "jogos": len(jogos), "jogos_esperados": None, "tabelas_conferidas": conferidas,
                                   "tabelas_divergentes": divergentes, "gols": gols, "gols_com_autor": autor,
                                   "observacao": obs_ed})
        linhas.append((T, "Wikipédia (en)" + (" + RSSSF" if tb_rs else ""), len(ordem), len(jogos), gols, autor, conferidas,
                       divergentes, clubes.exibicao(campeao) if conta else f"— ({clubes.exibicao(campeao)}, não reconhecido)", ""))
        print(f"{T}: {len(jogos)} jogos, {len(ordem)} clubes, tabelas {conferidas} ok / {divergentes} div, vencedor "
              f"{clubes.exibicao(campeao)}", flush=True)
    return linhas
