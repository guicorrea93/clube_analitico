"""Monta o pacote da 1ª divisão tcheca (cze-1), 1993/94 a 2025/26, e o relatório docs/coleta/cze-1.md.

Base dos jogos: o calendário do ogol, com data e rodada; o clube pelo código do ogol (clubes_cze.OGOL). Jogo decidido fora
de campo ("DA" no ogol, sem placar) fica com o placar oficial da matriz da Wikipédia, marcado `awd`. Jogos cancelados
("ANU") ficam de fora.
Formato: pontos corridos; em 2018/19, 2019/20 e de 2021/22 em diante, fase regular de 30 rodadas e grupos com os pontos
acumulados (grupo do título, 1º a 6º; grupo de rebaixamento, 11º a 16º; desde 2022/23, um play-off europeu em mata-mata
entre o 7º e o 10º). A classificação final é a ordem do grupo do título, depois do 7º ao 10º pela fase regular, depois o
grupo de rebaixamento.
Conferência: tabelas da Wikipédia (fase regular e grupos) e da RSSSF (página de cada temporada); matriz de resultados da
Wikipédia e jogos da RSSSF, jogo a jogo. Autores dos gols: a página da RSSSF de 1998/99 a 2011/12 (quando a conta fecha
com o placar). RSSSF: lista de campeões e de artilheiros. Sem football-data, engsoccerdata nem ESPN para a Tchéquia: não
há cartões.

Uso: python coleta/cze-1/importar.py
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-europa"))
sys.path.append(str(AQUI.parent / "gre-1"))   # leitores do grego (wiki_gre, rsssf_gre), no fim da busca
sys.path.insert(0, str(AQUI))
import clubes_cze as clubes  # noqa: E402
import notas_wiki  # noqa: E402
import rsssf_cze as rsssf  # noqa: E402
import wiki_gre  # noqa: E402
from edicoes import DADOS, RAIZ, TEMPORADAS, nome_oficial, rsssf_urls, temporada, wiki_titulo  # noqa: E402
from pacote import gravar  # noqa: E402
from wiki_tabela import tabelas as wiki_tabelas  # noqa: E402

PACOTE = DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / "cze-1.md"


def pontos(a: int) -> tuple[int, int, int]:
    """Pontos por vitória, empate e derrota: 2-1-0 em 1993/94 (como a tabela da RSSSF), 3-1-0 depois."""
    return (2, 1, 0) if a == 1993 else (3, 1, 0)


PTS = (3, 1, 0)   # trocado a cada temporada em main()

# clube que não está na temporada seguinte sem ter caído: (ano, clube) -> motivo
NAO_REBAIXADOS: dict[tuple, str] = {}
# rebaixado fora de campo, que a regra (não estar na temporada seguinte) não pega ou explica: (ano, clube) -> motivo
FORA_DE_CAMPO: dict[tuple, str] = {}
# explicação de cada divergência que sobra entre fontes (vai para o relatório, antes das ocorrências da temporada)
EXPLICACOES: dict[int, list[str]] = {
    1995: ["a matriz da Wikipédia dá Baník Ostrava 0-1 Viktoria Žižkov e 3-1 Dynamo České Budějovice; o ogol dá 2-2 e 0-1, e "
           "as tabelas da RSSSF e da Wikipédia fecham com o ogol: erro da matriz"],
}
# placar corrigido: (ano, mandante, visitante) -> (gols, gols, motivo[, "awd"])
CORRECOES: dict[tuple, tuple] = {
    (2015, "FK Dukla Praga", "Slovan Liberec"): (2, 0, "o ogol dá 1-0; a matriz da Wikipédia, a página da RSSSF e as tabelas "
                                                       "da RSSSF e da Wikipédia dão 2-0"),
}
# jogo decidido fora de campo ("DA" no ogol) com o placar oficial dado aqui: (ano, mandante, visitante) -> (gols, gols, motivo)
DECIDIDOS: dict[tuple, tuple] = {
    (2025, "Slavia Praga", "Sparta Praga"): (0, 3, "abandonado nos acréscimos com 3-2 para o Slavia, depois da invasão de "
                                                   "campo da torcida do Slavia; em 12/05/2026 a liga deu 3-0 ao Sparta (nota da "
                                                   "matriz da Wikipédia)"),
}

COMPETICAO = {
    "slug": "cze-1", "nome": "Campeonato Tcheco", "nome_curto": "Tcheco", "tipo": "liga", "nivel": 1,
    "pais": "CZE", "pais_nome": "Tchéquia", "regiao": None, "confederacao": "UEFA",
    "rotulo_painel": "Tcheco", "menu_painel": "Tchéquia · 1ª divisão",
    "do_painel": "do Campeonato Tcheco", "o_painel": "o Campeonato Tcheco",
    "observacao": "Liga da República Tcheca desde a separação da Tchecoslováquia (1993/94): 1. liga, Gambrinus liga, Fortuna "
                  "liga e Chance liga. Pontos corridos; em 2018/19, 2019/20 e desde 2021/22, fase regular e grupos (título, "
                  "rebaixamento e, desde 2022/23, play-off europeu em mata-mata). A liga tchecoslovaca (1925-1993) e a do "
                  "Protetorado da Boêmia e Morávia (1938/39-1943/44) estão na competição da Tchecoslováquia. Não inclui os "
                  "jogos de acesso contra clubes da 2ª divisão.",
}


def faixa(anos) -> str:
    a = sorted(anos)
    return f"{a[0]}-{a[-1]}" if a[0] != a[-1] else f"{a[0]}"


def chave(nome: str, a: int, fonte: str) -> str:
    c = clubes.esd(nome, a)
    if c is None:
        raise SystemExit(f"{temporada(a)}: nome do {fonte} sem cadastro: {nome}")
    return c


# ------------------------------------------------------------------ fontes
def pagina_rsssf(a: int) -> tuple[str, str] | None:
    for url in rsssf_urls(a):
        arq = DADOS / "rsssf" / url.rsplit("/", 1)[1]
        if arq.exists():
            return rsssf.texto(arq), url
    return None


def texto_wiki(a: int) -> str:
    arqs = sorted((DADOS / "wikipedia").glob(f"{wiki_titulo(a)}*.wiki"))
    return "\n".join(x.read_text(encoding="utf-8") for x in arqs)


def tabelas_wiki(a: int) -> list[dict]:
    res = []
    for tb in wiki_tabelas(texto_wiki(a)):
        for x in tb["times"]:
            x["clube"] = clubes.esd(x["nome"], a)
        res.append(tb)
    return res


def carregar_ogol(a: int) -> list[dict]:
    res = []
    for o in json.loads((DADOS / "ogol" / f"cze1_{a}.json").read_text(encoding="utf-8")):
        if o["resultado"] in ("ADI", "ANU"):
            continue
        m = clubes.ogol(o["mandante_id"], a) or clubes.esd(o["mandante"], a)
        v = clubes.ogol(o["visitante_id"], a) or clubes.esd(o["visitante"], a)
        if m is None or v is None:
            raise SystemExit(f"{temporada(a)}: clube do ogol sem cadastro: {o['mandante']} ({o['mandante_id']}) x "
                             f"{o['visitante']} ({o['visitante_id']})")
        r = re.match(r"^R(\d+)$", o["fase"] or "")
        res.append({"data": o["data"], "m": m, "v": v, "nm": o["mandante"], "nv": o["visitante"], "gm": o["gols_mandante"],
                    "gv": o["gols_visitante"], "rodada": int(r.group(1)) if r else None, "fonte": "ogol", "ogol": o,
                    "fase": "Liga", "grupo": None, "prorrogacao": "(Pro.)" in o["resultado"],
                    "etapa": o["fase"]})
    return res


def campeoes_rsssf() -> dict[int, str]:
    """tsjechamp.html, seção "I. liga CR": "1993/94 AC Sparta Praha"."""
    t = rsssf.texto(DADOS / "rsssf" / "tsjechamp.html")
    t = t[t.find("I. liga CR"):]
    return {int(m.group(1)): clubes.esd(m.group(2), int(m.group(1))) or m.group(2)
            for m in re.finditer(r"^(\d{4})/\d{2}\s+(\S.*?)\s*$", t, re.M)}


# ------------------------------------------------------------------ tabela
def calcular(jogos: list[dict]) -> dict[str, list[int]]:
    t = defaultdict(lambda: [0, 0, 0, 0, 0, 0, 0])   # J V E D GP GC Pts
    for j in jogos:
        if j["gm"] is None:
            continue
        for c, gp, gc in ((j["m"], j["gm"], j["gv"]), (j["v"], j["gv"], j["gm"])):
            x = t[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            k = 1 if gp > gc else 2 if gp == gc else 3
            x[k] += 1
            x[6] += PTS[k - 1]
    return t


def ordenar(t: dict[str, list[int]], ajuste: dict[str, int], criterio: str, jogos: list[dict] | None) -> list[str]:
    """criterio: "vitorias", "saldo" ou "confronto" (pontos; entre os empatados, pontos e saldo nos jogos entre eles)."""
    def p(c):
        return t[c][6] + ajuste.get(c, 0)

    def geral(c):
        j, v, e, d, gp, gc, _ = t[c]
        return (-v, -(gp - gc), -gp) if criterio == "vitorias" else (-(gp - gc), -gp)
    if criterio != "confronto":
        return sorted(sorted(t), key=lambda c: (-p(c), *geral(c)))
    grupos = defaultdict(list)
    for c in sorted(t):
        grupos[p(c)].append(c)
    res = []
    for pt in sorted(grupos, reverse=True):
        g = grupos[pt]
        if len(g) > 1 and jogos is not None:
            mini = calcular([j for j in jogos if j["m"] in g and j["v"] in g])
            g.sort(key=lambda c: (-mini[c][6], -(mini[c][4] - mini[c][5]), -mini[c][4], *geral(c)))
        else:
            g.sort(key=geral)
        res += g
    return res


def separar(jogos: list[dict], so: set) -> tuple[list[dict], list[dict]]:
    """Fase regular (o primeiro jogo de cada par mandante x visitante, pela data, entre os clubes de `so`) e o resto."""
    vistos, regular, resto = set(), [], []
    for j in sorted(jogos, key=lambda j: (j["data"] or "9999", j["rodada"] or 0)):
        if (j["m"], j["v"]) in vistos or not {j["m"], j["v"]} <= so:
            resto.append(j)
        else:
            vistos.add((j["m"], j["v"]))
            regular.append(j)
    return regular, resto


def numeros(x: dict) -> list[int]:
    v, e, d = x["vitorias"] or 0, x["empates"] or 0, x["derrotas"] or 0
    return [v + e + d, v, e, d, x["gols_pro"], x["gols_contra"], PTS[0] * v + PTS[1] * e + (x["ajuste"] or 0)]


# ------------------------------------------------------------------ principal
def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    camp = campeoes_rsssf()
    ogol = {a: carregar_ogol(a) for a in TEMPORADAS + [TEMPORADAS[-1] + 1]}
    nomes = defaultdict(lambda: defaultdict(set))
    ocorr = defaultdict(list)
    tab = defaultdict(list)
    linhas_rel, criterios = [], {}

    global PTS
    for a in TEMPORADAS:
        ocorr[a].extend(EXPLICACOES.get(a, []))
        T = temporada(a)
        PTS = pontos(a)
        tbs = tabelas_wiki(a)
        for tb in tbs:
            for x in tb["times"]:
                if x["clube"] is None:
                    raise SystemExit(f"{T}: nome da Wikipédia sem cadastro: {x['nome']}")
        wk = wiki_gre.ler(texto_wiki(a))
        mz_w = defaultdict(list)
        for w in wk["jogos"]:
            if w["fonte"] == "matriz":
                m_ = clubes.esd(w["tm"] or "", a) or clubes.esd(w["nm"], a)
                v_ = clubes.esd(w["tv"] or "", a) or clubes.esd(w["nv"], a)
                mz_w[(m_, v_)].append((w["gm"], w["gv"]))
        jogos = ogol[a]
        for j in jogos:
            for lado in ("m", "v"):
                nomes[j[lado]][f"ogol:{j['n' + lado]}"].add(a)
        maior = max(tbs, key=lambda tb: len(tb["times"]))
        liga = {x["clube"] for x in maior["times"]}
        n = len(liga)
        grupos_tb = [tb for tb in tbs if tb is not maior and len(tb["times"]) < n]
        fora = [j for j in jogos if not {j["m"], j["v"]} <= liga]
        for j in fora:   # jogos contra clubes de fora da liga (acesso e rebaixamento): ficam de fora
            ocorr[a].append(f"jogo com clube de fora da liga, fora do pacote: {j['m']} x {j['v']} ({j['data']}, "
                            f"{j['ogol']['resultado']})")
        jogos = [j for j in jogos if j not in fora]
        regular, resto = separar(jogos, liga) if grupos_tb else (jogos, [])
        reg_ids = {id(j) for j in regular}
        for j in jogos:   # decidido fora de campo, sem placar no ogol
            if j["gm"] is not None:
                continue
            if (a, j["m"], j["v"]) in DECIDIDOS:
                j["gm"], j["gv"], motivo = DECIDIDOS[(a, j["m"], j["v"])]
                j["especial"] = "awd"
                j["obs"] = f"resultado decidido fora de campo: {motivo}"
                ocorr[a].append(f"{j['m']} x {j['v']} ({j['data']}): {j['ogol']['resultado']} no ogol; fica {j['gm']}-{j['gv']} "
                                f"({motivo})")
                continue
            cand = mz_w.get((j["m"], j["v"]), [])
            if not cand:
                raise SystemExit(f"{T}: jogo sem placar no ogol ({j['ogol']['resultado']}) e sem a matriz da Wikipédia: "
                                 f"{j['m']} x {j['v']} ({j['data']})")
            j["gm"], j["gv"] = cand[0] if id(j) in reg_ids else cand[-1]
            j["especial"] = "awd"
            j["obs"] = (f"resultado decidido fora de campo (no ogol: \"{j['ogol']['resultado']}\", sem placar); placar oficial "
                        f"pela matriz da Wikipédia")
            ocorr[a].append(f"{j['m']} x {j['v']} ({j['data']}): {j['ogol']['resultado']} no ogol; fica {j['gm']}-{j['gv']} "
                            f"pela matriz da Wikipédia")
        for (b_, m_, v_), (g1, g2, motivo, *esp) in CORRECOES.items():
            if b_ != a:
                continue
            j = next((j for j in regular if (j["m"], j["v"]) == (m_, v_)), None)
            if j is None:
                raise SystemExit(f"{T}: jogo da correção não encontrado: {m_} x {v_}")
            j["gm"], j["gv"] = g1, g2
            if esp:
                j["especial"] = esp[0]
            j["obs"] = f"placar corrigido: {motivo}"
            ocorr[a].append(f"{m_} x {v_} ({j['data']}): placar corrigido para {g1}-{g2} ({motivo})")
        clubes_ano = sorted(liga)
        esperados = n * (n - 1)
        if len(regular) != esperados:
            ocorr[a].append(f"fase regular com {len(regular)} jogos de {esperados}")
        fase_reg = "Fase regular" if resto else "Liga"
        for j in regular:
            j["fase"] = fase_reg

        # ---- conferência jogo a jogo com a matriz da Wikipédia (só a da fase regular: a primeira matriz)
        por_par = defaultdict(list)
        for j in regular:
            por_par[(j["m"], j["v"])].append((j["gm"], j["gv"]))
        dif = []
        for par, pl in mz_w.items():
            if not set(par) <= liga:
                continue
            nossos = sorted(por_par.get(par, []))
            if pl[0] not in nossos and nossos:
                dif.append(f"{par[0]} x {par[1]}: ogol {', '.join(f'{x}-{y}' for x, y in nossos)}; Wikipédia "
                           f"{', '.join(f'{x}-{y}' for x, y in pl)}")
        for d in dif[:15]:
            ocorr[a].append(f"placar diferente na matriz da Wikipédia — {d}")
        if len(dif) > 15:
            ocorr[a].append(f"... e mais {len(dif) - 15} pares com placar diferente na matriz da Wikipédia")
        if not mz_w:
            ocorr[a].append("sem matriz na Wikipédia para conferir os jogos")

        # ---- fase regular: tabelas publicadas, punições e ordem
        ref = calcular(regular)
        ajuste = {x["clube"]: x["ajuste"] for x in maior["times"] if x["ajuste"]}
        for x in maior["times"]:
            nomes[x["clube"]][f"wikipedia:{x['nome']}"].add(a)
        pg = pagina_rsssf(a)
        rs = None
        if pg:
            blocos = rsssf.tabelas(pg[0])
            melhor = max(blocos, key=lambda b: len({clubes.esd(x["nome"], a) for x in b} & liga), default=None)
            if melhor and {clubes.esd(x["nome"], a) for x in melhor} == liga:
                rs = melhor
                for x in rs:
                    x["clube"] = clubes.esd(x["nome"], a)
                    nomes[x["clube"]][f"rsssf:{x['nome']}"].add(a)
            else:
                ocorr[a].append("tabela da RSSSF da fase regular não encontrada na página da temporada")
        publicadas = [("Wikipédia", f"https://en.wikipedia.org/wiki/{wiki_titulo(a).replace(' ', '_')}",
                       [dict(x, **dict(zip(("jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra", "pontos"),
                                           numeros(x)))) for x in maior["times"]])]
        if rs:
            publicadas.append(("RSSSF", pg[1], rs))
        conferidas = divergentes = 0
        confere = {}
        for fonte, url, linhas in publicadas:
            erro = []
            for x in linhas:
                c = ref.get(x["clube"])
                pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]
                meu = (c[:6] + [c[6] + ajuste.get(x["clube"], 0)]) if c else None
                if pub != meu:
                    erro.append((x["clube"], pub, meu))
                tab["tabelas_publicadas"].append({
                    "temporada": T, "fase": fase_reg, "grupo": None, "posicao": x["posicao"], "nome_fonte": x["nome"],
                    "clube": clubes.exibicao(x["clube"]), "jogos": pub[0], "vitorias": pub[1], "empates": pub[2],
                    "derrotas": pub[3], "gols_pro": pub[4], "gols_contra": pub[5], "pontos": pub[6], "fonte": url})
            confere[fonte] = erro
            if erro:
                divergentes += 1
            else:
                conferidas += 1
        for fonte, erro in confere.items():
            outra = [f_ for f_ in confere if f_ != fonte]
            for c, pub, meu in erro[:8]:
                fecha = outra and c not in {e[0] for e in confere[outra[0]]}
                ocorr[a].append(f"tabela publicada x jogos ({fonte}) — {c} tabela {pub} jogos {meu}"
                                + (f" (a tabela da {outra[0]} fecha com os jogos)" if fecha else ""))
        ordem = [x["clube"] for x in maior["times"]]
        tentativas = {cr: ordenar(ref, ajuste, cr, regular) for cr in ("confronto", "saldo", "vitorias")}
        ok = [cr for cr, o in tentativas.items() if o == ordem]
        criterio = ok[0] if ok else min(tentativas, key=lambda cr: sum(x != y for x, y in zip(tentativas[cr], ordem)))
        if not ok:
            d_ = [c for c, d in zip(ordem, tentativas[criterio]) if c != d]
            ocorr[a].append(f"nenhum critério calculado reproduz a ordem oficial; o mais próximo ({criterio}) difere em "
                            f"{len(d_)} posições (ex.: {d_[:2]})")
        criterios[a] = (criterio, bool(ok))

        # ---- grupos (título e rebaixamento, pontos acumulados) e play-off europeu (mata-mata)
        fases_po = []
        if resto:
            sobra = list(resto)
            for tb in grupos_tb:
                conj = {x["clube"] for x in tb["times"]}
                fase = "Grupo do título" if ordem[0] in conj else "Grupo de rebaixamento"
                comp = [j for j in sobra if {j["m"], j["v"]} <= conj]
                sobra = [j for j in sobra if j not in comp]
                for j in comp:
                    j["fase"] = fase
                fases_po.append((fase, comp, tb))
                calc_g = calcular(regular + comp)
                erro = []
                for x in tb["times"]:
                    c = x["clube"]
                    nomes[c][f"wikipedia:{x['nome']}"].add(a)
                    pub = numeros(x)
                    meu = calc_g[c][:6] + [calc_g[c][6] + (x["ajuste"] or 0)]
                    if pub != meu:
                        erro.append(f"{c} tabela {pub} jogos {meu}")
                    tab["tabelas_publicadas"].append({
                        "temporada": T, "fase": fase, "grupo": None, "posicao": x["posicao"], "nome_fonte": x["nome"],
                        "clube": clubes.exibicao(c), "jogos": pub[0], "vitorias": pub[1], "empates": pub[2],
                        "derrotas": pub[3], "gols_pro": pub[4], "gols_contra": pub[5], "pontos": pub[6],
                        "fonte": f"https://en.wikipedia.org/wiki/{wiki_titulo(a).replace(' ', '_')}"})
                if erro:
                    divergentes += 1
                    ocorr[a] += [f"tabela do {fase.lower()} (Wikipédia) x jogos — {e_}" for e_ in erro[:6]]
                else:
                    conferidas += 1
            for j in sobra:   # play-off europeu (7º a 10º), em mata-mata
                j["fase"] = "Play-off europeu"
                j["grupo"] = {"SF": "Semifinal", "F": "Final"}.get(j["etapa"], None)
                if j["prorrogacao"]:
                    j["obs"] = "com prorrogação"
            if sobra:
                fases_po.append(("Play-off europeu", sobra, None))

        # ---- classificação final
        if fases_po:
            tit = next((tb for f, c_, tb in fases_po if f == "Grupo do título"), None)
            reb = next((tb for f, c_, tb in fases_po if f == "Grupo de rebaixamento"), None)
            topo = [x["clube"] for x in tit["times"]] if tit else []
            baixo = [x["clube"] for x in reb["times"]] if reb else []
            ordem_final = topo + [c for c in ordem if c not in topo and c not in baixo] + baixo
            fonte_final = "Wikipédia (grupo do título; 7º a 10º pela fase regular; grupo de rebaixamento)"
            ajuste_final = dict(ajuste)
            for tb in (tit, reb):
                for x in (tb or {}).get("times", []):
                    if x["ajuste"]:
                        ajuste_final[x["clube"]] = x["ajuste"]
            grupo_de = {x["clube"]: f for f, c_, tb in fases_po if tb for x in tb["times"]}
            numeros_cl = calcular(regular + [j for f, c_, tb in fases_po if tb for j in c_])
        else:
            ordem_final, fonte_final, ajuste_final, grupo_de, numeros_cl = ordem, "Wikipédia (ordem oficial)", ajuste, {}, ref
        prox_clubes = {c for j in ogol[a + 1] for c in (j["m"], j["v"])}
        rebaixados = set()
        for c in clubes_ano:
            if c not in prox_clubes:
                if (a, c) in NAO_REBAIXADOS:
                    ocorr[a].append(f"{c} não está na temporada seguinte, mas não caiu: {NAO_REBAIXADOS[(a, c)]}")
                else:
                    rebaixados.add(c)
        campeao = ordem_final[0]
        if camp.get(a) != campeao:
            ocorr[a].append(f"campeão diferente na lista de campeões da RSSSF: {camp.get(a)} (classificação: {campeao})")
        for pos, c in enumerate(ordem_final, 1):
            j_, v_, e_, d_, gp, gc, p = numeros_cl[c]
            pts_c = p + ajuste_final.get(c, 0)
            obs = f"{grupo_de[c].lower()}: pontos da fase regular e do grupo somados" if c in grupo_de else None
            nota = next((notas_wiki.traduzir(x["nota"] or x["hth"]) for x in maior["times"] if x["clube"] == c), None)
            tab["classificacao_final"].append({
                "temporada": T, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
                "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": pts_c, "ajuste_pontos": pts_c - p,
                "situacao": "campeao" if pos == 1 else "rebaixado" if c in rebaixados else None, "fonte": fonte_final,
                "observacao": "; ".join(x for x in (obs, nota, FORA_DE_CAMPO.get((a, c))) if x) or None})

        # ---- RSSSF jogo a jogo: conferência dos placares e autores dos gols (1998/99 a 2011/12 trazem os autores)
        autores_ok = 0
        if pg:
            rj = rsssf.jogos(pg[0], a)
            res_rj = [(x, clubes.esd(x["m"], a), clubes.esd(x["v"], a)) for x in rj]
            validos = [(x, m_, v_) for x, m_, v_ in res_rj if m_ in liga and v_ in liga]
            if len(validos) >= 0.9 * esperados:   # página legível (as mais antigas misturam a Copa e outras divisões)
                usados, dif_rs, rs_ok = set(), [], set()
                for x, m_, v_ in validos:
                    cand = [j for j in jogos if (j["m"], j["v"]) == (m_, v_) and id(j) not in usados]
                    j = next((j for j in cand if (j["gm"], j["gv"]) == (x["gm"], x["gv"])), None)
                    if j is None:
                        j = min(cand, key=lambda j: abs((j["rodada"] or 0) - x["rodada"]), default=None)
                        if j is not None and not j.get("especial"):
                            dif_rs.append(f"{m_} x {v_} ({j['data']}): ogol {j['gm']}-{j['gv']}, RSSSF {x['gm']}-{x['gv']}")
                    if j is None:
                        continue
                    usados.add(id(j))
                    if (j["gm"], j["gv"]) == (x["gm"], x["gv"]):
                        rs_ok.add((m_, v_))
                    if x.get("gols_txt") and (j["gm"], j["gv"]) == (x["gm"], x["gv"]) and not j.get("especial"):
                        au = rsssf.autores(x["gols_txt"], x["gm"], x["gv"])
                        if au:
                            j["autores"] = au
                for d in dif_rs[:10]:
                    ocorr[a].append(f"placar diferente na RSSSF — {d}")
                # diferença com a matriz da Wikipédia em que a RSSSF concorda com o ogol: erro da matriz
                ocorr[a] = [o + " (RSSSF = ogol)" if o.startswith("placar diferente na matriz da Wikipédia — ") and
                            tuple(o.split(" — ", 1)[1].split(":")[0].split(" x ")) in rs_ok else o for o in ocorr[a]]
                if len(dif_rs) > 10:
                    ocorr[a].append(f"... e mais {len(dif_rs) - 10} jogos com placar diferente na RSSSF")

        # ---- partidas
        jogos.sort(key=lambda j: (j["data"] or "9999", j["rodada"] or 0, j["m"]))
        gols_ano = 0
        for i, j in enumerate(jogos, 1):
            tab["partidas"].append({
                "id": f"{a}-{i:04d}", "temporada": T, "fase": j["fase"], "grupo": j["grupo"], "rodada": j["rodada"],
                "data": j["data"], "hora": j["ogol"].get("hora") or None, "mandante": clubes.exibicao(j["m"]),
                "visitante": clubes.exibicao(j["v"]), "gols_mandante": j["gm"], "gols_visitante": j["gv"],
                "penaltis_mandante": None, "penaltis_visitante": None, "resultado_especial": j.get("especial"),
                "estadio": None, "cidade": None, "publico": None, "fonte": "ogol", "fonte_id": f"ogol:{j['ogol']['id']}",
                "gols_texto": None, "observacao": j.get("obs"), "arbitro": None})
            gols_ano += j["gm"] + j["gv"]
            for c, lista in zip((j["m"], j["v"]), j.get("autores") or ()):
                for nome, mi, ac, tipo in lista:
                    tab["gols"].append({"partida_id": f"{a}-{i:04d}", "clube": clubes.exibicao(c), "jogador": nome, "minuto": mi,
                                        "acrescimo": ac, "tipo": tipo, "fonte": "RSSSF"})
                    autores_ok += 1

        # ---- classificação rodada a rodada (fase regular)
        if regular and all(j["rodada"] for j in regular):
            pos_reb = {p for p, c in enumerate(ordem, 1) if c in rebaixados}
            for r in sorted({j["rodada"] for j in regular}):
                ate = [j for j in regular if j["rodada"] <= r]
                parcial = calcular(ate)
                for pos, c in enumerate(ordenar(parcial, ajuste, criterio, ate), 1):
                    jj, v_, e_, d_, gp, gc, p = parcial[c]
                    tab["classificacao_rodada"].append({
                        "temporada": T, "rodada": r, "clube": clubes.exibicao(c), "posicao": pos, "pontos": p + ajuste.get(c, 0),
                        "jogos": jj, "vitorias": v_, "empates": e_, "derrotas": d_, "gols_pro": gp, "gols_contra": gc,
                        "zona": "titulo" if pos == 1 else "rebaixamento" if pos in pos_reb else "meio"})

        # ---- edição, fases, conferência
        pun = "; ".join(f"{c} {v:+d} pontos" for c, v in ajuste_final.items())
        formato = "pontos corridos (turno e returno)"
        if fases_po:
            formato = ("fase regular em turno e returno e grupos do título e de rebaixamento, com os pontos acumulados" +
                       ("; play-off europeu em mata-mata do 7º ao 10º" if any(f == "Play-off europeu" for f, *_ in fases_po)
                        else ""))
        tab["edicoes"].append({"temporada": T, "ano_inicio": a, "ano_fim": a + 1, "nome_oficial": nome_oficial(a), "num_clubes": n,
                               "pontos_vitoria": 3, "formato": formato, "campeao": clubes.exibicao(campeao),
                               "vice": clubes.exibicao(ordem_final[1]),
                               "fontes": "ogol + Wikipédia" + (" + RSSSF" if rs else ""),
                               "observacao": f"punições: {pun}" if pun else None})
        crit_txt = {"vitorias": "pontos, vitórias, saldo de gols, gols pró", "saldo": "pontos, saldo de gols, gols pró",
                    "confronto": "pontos, confronto direto, saldo de gols, gols pró"}[criterio]
        tab["fases"].append({"temporada": T, "ordem": 1, "fase": fase_reg, "tipo": "liga", "num_grupos": None,
                             "formato_serie": "pontos_corridos", "criterio": crit_txt})
        for k, (fase, comp, tb) in enumerate(fases_po, 2):
            ko = fase == "Play-off europeu"
            tab["fases"].append({"temporada": T, "ordem": k, "fase": fase, "tipo": "mata_mata" if ko else "grupos",
                                 "num_grupos": None if ko else 1, "formato_serie": "ida_volta" if ko else "pontos_corridos",
                                 "criterio": "soma dos placares, com prorrogação" if ko else "pontos acumulados com a fase regular"})
        tab["conferencia"].append({"temporada": T, "jogos": len(jogos), "jogos_esperados": esperados,
                                   "tabelas_conferidas": conferidas, "tabelas_divergentes": divergentes, "gols": gols_ano,
                                   "gols_com_autor": autores_ok, "observacao": f"campeão {clubes.exibicao(campeao)} (RSSSF, lista de campeões)"})
        linhas_rel.append((T, n, len(jogos), gols_ano, autores_ok, conferidas, divergentes, clubes.exibicao(campeao), pun))
        print(f"{T}: {len(jogos)} jogos ({len(regular)} da fase regular), tabelas {conferidas} ok / {divergentes} div, "
              f"critério {criterio}{'' if ok else ' (aprox.)'}, campeão {clubes.exibicao(campeao)}", flush=True)

    for c, (cidade, pais) in sorted(clubes.CLUBES.items()):
        if c in nomes:
            tab["clubes"].append({"clube": clubes.exibicao(c), "regiao": None, "cidade": cidade, "pais": pais,
                                  "nomes_fonte": "|".join(f"{k}:{faixa(v)}" for k, v in sorted(nomes[c].items()))})
    tab["paises"] = [{"codigo": "CZE", "nome": "Tchéquia", "confederacao": "UEFA"}]
    tab["artilheiros"] = artilheiros(ocorr)
    gravar(PACOTE, COMPETICAO, tab)
    relatorio(linhas_rel, ocorr, tab, criterios)


def artilheiros(ocorr) -> list[dict]:
    """tsjetops.html: "1993/94 Horst Siegl          (Sparta Prague)        20"; empate na linha seguinte, sem temporada."""
    res, ano = [], None
    for l in rsssf.texto(DADOS / "rsssf" / "tsjetops.html").split("\n"):
        m = re.match(r"^(\d{4})/\d{2}\s+(\S.*?)\s+\((.*?)\)\s+(\d+)\s*$", l)
        m2 = re.match(r"^\s{5,}(\S.*?)\s+\((.*?)\)\s+(\d+)\s*$", l)
        if m:
            ano, nome, clube_txt, gols = int(m.group(1)), m.group(2), m.group(3), int(m.group(4))
        elif m2 and ano is not None:
            nome, clube_txt, gols = m2.groups()
            gols = int(gols)
        else:
            continue
        if ano not in TEMPORADAS:
            continue
        c = clubes.esd(clube_txt, ano) if "/" not in clube_txt else None
        res.append({"temporada": temporada(ano), "jogador": nome.strip(), "clube": clubes.exibicao(c) if c else None,
                    "gols": gols, "fonte": "RSSSF (tablest/tsjetops.html)"})
        if c is None:
            ocorr[ano].append(f"artilheiro sem um clube só na lista da RSSSF: {nome} ({clube_txt})")
    return res


def relatorio(linhas, ocorr, tab, criterios) -> None:
    jogos = len(tab["partidas"])
    gols = sum(int(x["gols_mandante"]) + int(x["gols_visitante"]) for x in tab["partidas"])
    cr = Counter(c for c, _ in criterios.values())
    out = [
        "# Campeonato Tcheco (1ª divisão) — coleta de dados", "",
        "Gerado por `python coleta/cze-1/importar.py`. Pacote em `data/coleta/cze-1/pacote/`.", "",
        f"**Edições:** {len(linhas)}, de 1993/94 a 2025/26 (a liga da República Tcheca). A liga tchecoslovaca e a do "
        "Protetorado ficam na competição da Tchecoslováquia.", "",
        f"**Total:** {jogos} jogos, {gols} gols, {len(tab['gols'])} gols com autor (RSSSF, 1998/99 a 2011/12), "
        f"{len(tab['clubes'])} clubes. Sem cartões (nenhuma fonte em lote cobre a Tchéquia).", "",
        "**Fontes:**",
        "- ogol (zerozero): base dos jogos, com data e rodada; o clube pelo código do ogol; calendários em "
        "`data/cache/ogol-cze-1/` para os escudos;",
        "- Wikipédia (en): tabelas da fase regular e dos grupos (ordem oficial, punições), matriz de resultados "
        "(conferência e placar dos jogos decididos fora de campo);",
        "- RSSSF: tabela final e jogos de cada temporada (conferência; autores dos gols de 1998/99 a 2011/12), lista de "
        "campeões e de artilheiros.", "",
        "**Regras:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a "
        "da Wikipédia. Com grupos (2018/19, 2019/20 e desde 2021/22), a classificação final é o grupo do título, depois do "
        "7º ao 10º pela fase regular, depois o grupo de rebaixamento, com os números de todos os jogos da liga (o play-off "
        "europeu fica fora da conta). 2 pontos por vitória em 1993/94 e 3 depois. Rebaixado = clube que não está na 1ª divisão na temporada "
        "seguinte.", "",
        f"**Desempate:** o critério calculado que reproduz a ordem oficial (confronto direto em {cr['confronto']}, saldo em "
        f"{cr['saldo']}, vitórias em {cr['vitorias']}).", "",
        "| Temporada | Clubes | Jogos | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for T, n, j, g, au, ok, dv, camp, pun in linhas:
        out.append(f"| {T} | {n} | {j} | {g} | {au} | {ok} / {dv} | {camp} | {pun or '—'} |")
    out += ["", "## Conferência e ocorrências, temporada a temporada", ""]
    for T, *_ in linhas:
        a = int(T[:4])
        out += [f"### {T}", ""] + [f"- {o}" for o in ocorr.get(a, []) or ["sem ocorrências"]] + [""]
    out += [
        "## Identidade dos clubes", "",
        "- Cadastro em `coleta/comum-europa/clubes_cze.py`, pela linhagem do clube (o alvo do link da Wikipédia). Mesmo "
        "clube: Bohemians Praha (até 2002) e Bohemians 1905; os nomes de patrocinador de Zlín, Brno, Drnovice, Příbram, "
        "Hradec Králové e Karviná. Clubes diferentes: o Dukla Praha histórico (1993/94) e o 1. FK Příbram, para onde ele se "
        "mudou em 1996 (o ogol usa o mesmo código), e o FK Dukla Praha de hoje; o Bohemians de Střížkov (2008/09); o "
        "Slovácká Slavia (1995/96) e o 1. FC Slovácko.",
        "- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.", "",
        "## O que não deu para coletar", "",
        "- **Autores dos gols fora de 1998/99-2011/12, cartões, público, estádio e árbitro:** a ESPN e o football-data não "
        "cobrem a Tchéquia, e a RSSSF só traz os autores nessas temporadas; o resto, só a ficha de cada jogo no ogol (jogo a "
        "jogo).",
        "- **Jogos de acesso e rebaixamento contra clubes da 2ª divisão:** ficam de fora.",
    ]
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
