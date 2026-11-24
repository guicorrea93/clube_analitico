"""Junta as fontes do Campeonato Paulista Série A2 (2ª divisão) e grava o pacote em data/coleta/bra-sp-2/pacote/ e o
relatório em docs/coleta/bra-sp-2.md. Mesmo código do Paulista (coleta/bra-sp-1/importar.py), com as fontes da A2.

Fontes: RSSSF Brasil (tablessz/sp{ano}l2.htm: jogos, fases, grupos, datas e autores; as tabelas publicadas são a
conferência); ogol (calendário de cada edição, de 1998 em diante, e o código de cada clube, que dá a identidade; confere
placares e completa jogos). Campeões pela lista da RSSSF (sp2camp.htm).

A edição é a temporada ("1997"); o ano sai de temporada[:4].

Uso: python coleta/bra-sp-2/importar.py [temporada ...]     (sem temporada: todas; com temporada, só confere e não grava)
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from difflib import SequenceMatcher
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
import clubes_sp2  # noqa: E402
import gols as gols_rsssf  # noqa: E402
import rsssf_sp2  # noqa: E402
import wiki  # noqa: E402
from edicoes import ANOS, NOME_OFICIAL, NOME_PADRAO, PACOTE, PASTA_DADOS, RELATORIO, SLUG  # noqa: E402
from rsssf_sp2 import rsssf  # noqa: E402

wiki.PASTA = PASTA_DADOS / "wikipedia"
OGOL = PASTA_DADOS / "ogol"
ESPN = PASTA_DADOS / "espn"
FONTE_RSSSF = "https://rsssfbrasil.com/tablessz/sp{ano}l2.htm"


# --------------------------------------------------------------------------------------------- partidas

@dataclass
class Partida:
    ano: int
    fase: str                 # nome da fase como na fonte (normalizado depois por fase_pt)
    grupo: str
    rodada: int | None
    data: str | None
    mandante: str             # código do clube no ogol
    visitante: str
    gm: int | None
    gv: int | None
    hora: str | None = None
    pen_m: int | None = None
    pen_v: int | None = None
    especial: str = ""
    estadio: str | None = None
    cidade: str | None = None
    publico: int | None = None
    fonte: str = ""
    fonte_id: str = ""
    gols_texto: str = ""
    obs: str = ""
    gols: list[dict] = field(default_factory=list)
    linha: int = 0
    ogol_fase: str = ""
    ogol_placar: tuple | None = None   # placar do mesmo jogo no ogol (conferência)


def _dia(d: str | None) -> int | None:
    try:
        return datetime.strptime(d, "%Y-%m-%d").toordinal() if d else None
    except ValueError:   # "0000-00-00": jogo sem data no ogol
        return None


def _trocar_dia_mes(d: str | None) -> str | None:
    """'2015-01-06' -> '2015-06-01' (a página de 2015 trocou dia e mês quando o dia era até 12)."""
    if not d or not re.match(r"^\d{4}-\d{2}-\d{2}$", d) or int(d[8:]) > 12:
        return None
    return f"{d[:4]}-{d[8:]}-{d[5:7]}"


def _dist(a: str | None, b: str | None) -> int:
    """Dias entre duas datas; 0 quando uma delas falta (não desempata)."""
    x, y = _dia(a), _dia(b)
    return abs(x - y) if x and y else 0


def _sim(a: str, b: str) -> float:
    a, b = clubes_sp2.chave(a), clubes_sp2.chave(b)
    if not a or not b:
        return 0.0
    if a == b:
        return 1.0
    if a.startswith(b) or b.startswith(a):
        return 0.85
    if rsssf.abreviado(a, b) or rsssf.abreviado(a.replace(".", " "), b):   # "eng beltrao" x "engenheiro beltrao"
        return 0.85
    return SequenceMatcher(None, a, b).ratio()


# código de clube errado no calendário do ogol: (ano, código errado) -> (código certo, motivo)
CORRIGE_OGOL: dict[tuple[int, str], tuple[str, str]] = {}


# clube refundado que o ogol mantém no código do antigo: código -> (ano em que o novo começa, código do novo, motivo)
REFUNDADO: dict[str, tuple[int, str, str]] = {
    "15767": (1999, "rs-gremio-catanduvense", "Grêmio Catanduvense (1999) separado do GE Catanduvense (1970-1995) (D-23 a, A2-022)"),
}


def refundado(ano, i: str | None) -> str | None:
    r = REFUNDADO.get(i)
    return r[1] if r and int(str(ano)[:4]) >= r[0] else i


def ler_ogol(ano: int) -> list[dict]:
    f = OGOL / f"sp2_{str(ano).replace(" ", "_")}.json"
    js = json.loads(f.read_text(encoding="utf-8")) if f.exists() else []
    for o in js:
        for lado in ("mandante", "visitante"):
            if (ano, o.get(f"{lado}_id")) in CORRIGE_OGOL:
                o[f"{lado}_id"] = CORRIGE_OGOL[(ano, o[f"{lado}_id"])][0]
            o[f"{lado}_id"] = refundado(ano, o.get(f"{lado}_id"))
    return [o for o in js if o["id"] not in OGOL_IGNORAR]


def nomes_ogol(ano: int, og: list[dict]) -> dict[str, set[str]]:
    """Código do clube -> nomes que o ogol usa para ele (no calendário do ano e na ficha)."""
    fs = clubes_sp2.fichas()
    saida: dict[str, set[str]] = defaultdict(set)
    for o in og:
        for lado in ("mandante", "visitante"):
            i = o.get(f"{lado}_id")
            if i:
                saida[i].add(o[lado])
                if i in fs:
                    saida[i] |= {fs[i]["curto"], fs[i].get("nome_completo") or ""}
    return saida


# nomes da RSSSF que o casamento automático não acerta (ano, nome) -> código do ogol, com o motivo
NOME_MANUAL: dict[tuple[str, str], tuple[str, str]] = {
    **{(a, n): ("2543", "Ferroviário Atlético Ituano (Itu) é o Ituano FC de hoje (o mesmo clube, com o nome antigo)")
       for a in ("1985", "1986", "1987", "1988", "1989") for n in ("Ferroviário", "Ferroviário Ituano")},
    ("1995", "Catanduva"): ("15767", "Catanduva EC é o novo nome do GE Catanduvense (nota da página de 1994 da RSSSF)"),
    ("1995", "Internacional"): ("3291", "AA Internacional de Limeira (a página de 1995 não tem a lista de participantes; "
                                        "o clube jogou a A2 de 1994 e de 1996)"),
    ("1995", "Botafogo"): ("3154", "Botafogo FC de Ribeirão Preto (a página de 1995 não tem a lista de participantes)"),
    ("1995", "Nacional"): ("3360", "Nacional AC, da capital (a página de 1995 não tem a lista de participantes)"),
    ("1996", "XV de Novembro"): ("8229", "EC XV de Novembro (Piracicaba), na lista de participantes"),
    ("1997", "XV Piracicaba"): ("8229", "EC XV de Novembro (Piracicaba)"),
    ("2002", "Portuguesa"): ("3406", "o playoff Francana x \"AA Portuguesa (Santos)\" é com a Portuguesa Santista, não com a "
                                     "Lusa da capital (página e Wikipédia; achado A2-010)"),
}
# temporadas sem rebaixado, embora a tabela da RSSSF marque "Relegated": temporada -> motivo
SEM_REBAIXAMENTO: dict[str, str] = {
    "2001": "Comercial e Sãocarlense \"saved from relegation\" com a criação do Rio-São Paulo de 2002 (nota da tabela)",
}
# punições de pontos: (temporada, clube) -> (pontos, motivo)
AJUSTES_MANUAIS: dict[tuple[str, str], tuple[int, str]] = {
    ("2001", "Sãocarlense"): (-5, "escalou jogador irregular (tabela da RSSSF; achado A2-011)"),
}
# temporadas em que o empate vai para os pênaltis e muda os pontos: vitória 3; empate com gols, 2 para quem ganha os
# pênaltis e 1 para quem perde; 0-0, 1 e 0 (nota da página de 2001 da RSSSF; achado A2-011)
PONTOS_PENALTIS = {"2001": "empates decididos nos pênaltis"}


def pontos_penaltis(partidas) -> dict[str, int]:
    pts: dict[str, int] = defaultdict(int)
    for p in partidas:
        if p.gm is None:
            continue
        if p.gm != p.gv:
            pts[p.mandante if p.gm > p.gv else p.visitante] += 3
            continue
        pts[p.mandante] += 0; pts[p.visitante] += 0
        if p.pen_m is None:
            raise ValueError(f"empate sem pênaltis numa temporada de PONTOS_PENALTIS: {nome(p.mandante)} x {nome(p.visitante)}")
        venc, perd = (p.mandante, p.visitante) if p.pen_m > p.pen_v else (p.visitante, p.mandante)
        pts[venc] += 1 if p.gm == 0 else 2
        pts[perd] += 0 if p.gm == 0 else 1
    return pts


# rebaixados pelo infobox da Wikipédia pt de cada edição, nos anos em que as tabelas da RSSSF não marcam "Relegated"
# (achado A2-007; conferido pela revisão em revisao/A2/rebaixados_wiki.py: todos somem da A2 e da A1 no ano seguinte)
REBAIXADOS_WIKI: dict[str, list[str]] = {
    "2000": ["Oeste", "XV de Piracicaba"],
    "2012": ["Palmeiras (B)", "Rio Preto", "União São João", "América-SP"],
    "2013": ["Noroeste", "São Carlos", "Santacruzense", "Juventus-SP"],
    "2014": ["Barueri", "Grêmio Osasco", "Itapirense", "São José-SP"],
    "2015": ["Comercial-RP", "Matonense", "Grêmio Catanduvense", "Guaratinguetá"],
    "2016": ["Paulista", "Monte Azul", "Independente de Limeira", "Atlético Sorocaba", "Marília", "Rio Branco-SP"],
    "2017": ["Barretos", "Capivariano", "Mogi Mirim", "Rio Preto", "União Barbarense", "Velo Clube"],
    "2018": ["Osasco Audax", "Batatais"],
    "2019": ["Nacional-SP", "Linense"],
    "2020": ["CA Votuporanguense", "Penapolense"],
    "2022": ["Osasco Audax", "Red Bull Bragantino II"],
    "2023": ["Lemense", "São Caetano"],
    "2024": ["Comercial-RP", "Monte Azul"],
    "2025": ["Portuguesa Santista", "Rio Claro"],
    "2026": ["Grêmio Prudente", "São Bento"],
}
# jogos do calendário do ogol que estão errados (a RSSSF e a tabela publicada mostram outro jogo): código do jogo -> motivo
OGOL_IGNORAR: dict[str, str] = {}
# jogos da RSSSF que ficam de fora: (ano, nome do clube) -> motivo
RSSSF_FORA: dict[tuple[int, str], str] = {}
# jogos da RSSSF anulados: (ano, mandante, visitante, gols, gols) como na página -> motivo
JOGOS_ANULADOS: dict[tuple, str] = {
    ("2008", "Mogi Mirim", "Oeste", 0, 0): "jogo de 03/05/2008 anulado pelo TJD-SP (suspeita de manipulação) e refeito em 24/05 "
                                           "(2-3); a página traz os dois (A2-014)",
}
# playoff contra a 1ª divisão (último da A1 x clube da A2): fica fora da A2 e vai para a observação da edição (decisão
# D-04, achado A2-012); os jogos estão no pacote bra-sp-1. (temporada, fase) -> nome do playoff
PLAYOFF_FORA: dict[tuple[str, str], str] = {
    ("1979", "Repescagem"): "a repescagem",
    ("2002", "Torneio de rebaixamento"): "o playoff",
    ("2003", "Torneio de rebaixamento"): "o playoff",
}


def mapear_nomes(ano: int, rs: list, og: list[dict], log: list[str]) -> dict:
    """Nome na RSSSF -> código do ogol, por grupo: a mesma página às vezes usa o mesmo nome curto para clubes
    diferentes em grupos diferentes ("Esportivo" de Bento Gonçalves e de Passos em 1988).
    Cada jogo da RSSSF vota nos jogos do ogol de mesmo placar e data próxima (o voto pesa mais quando os nomes
    parecem); depois, dentro de cada grupo, um para um, do par mais votado para o menos.
    Devolve chaves (nome, fase, grupo) e, para as tabelas gerais, o nome sozinho."""
    noms = nomes_ogol(ano, og)
    fs = clubes_sp2.fichas()
    cache: dict[tuple, float] = {}
    def sim(n, i):
        """Parecença do nome; a UF escrita no nome da RSSSF ("São José(RS)") desempata homônimos."""
        if (n, i) not in cache:
            s = max((_sim(n, x) for x in noms.get(i, ()) if x), default=0)
            uf_n, uf_i = clubes_sp2.separar_uf(n.replace("(", " (").strip())[1], fs.get(i, {}).get("uf")
            if uf_n and uf_i:
                s = s * 0.6 if uf_n != uf_i else min(1.0, s + 0.05)
            cache[(n, i)] = s
        return cache[(n, i)]
    nomes_todos = {x for j in rs for x in (j.mandante, j.visitante)}
    sem_uf = lambda n: re.sub(r"\s*\([A-Z]{2}\)$", "", n).strip()   # "Betim (MG)" vale como "Betim"
    por_base = {sem_uf(n): v[0] for (a, n), v in NOME_MANUAL.items() if a == ano}
    manual = {n: por_base[sem_uf(n)] for n in nomes_todos if sem_uf(n) in por_base}
    nomes_rs = {x for j in rs for x in (j.mandante, j.visitante)}
    # 1ª etapa: nomes inequívocos (um só clube do ogol com nome igual ou quase)
    ancora: dict[str, str] = dict(manual)
    for n in nomes_rs - set(ancora):
        cands = sorted(((sim(n, i), i) for i in noms), reverse=True)
        if cands and cands[0][0] >= 0.85 and (len(cands) == 1 or cands[1][0] < cands[0][0]):
            ancora[n] = cands[0][1]
    # 2ª etapa: votos dos jogos de mesmo placar e data próxima; o voto vale muito quando o adversário já está ancorado
    # e bate com o do ogol, e pouco quando não
    v_nome: dict[tuple, float] = defaultdict(float)
    v_ctx: dict[tuple, float] = defaultdict(float)
    for j in rs:
        if j.gm is None:
            continue
        dj = _dia(j.data)
        for o in og:
            if (o["gols_mandante"], o["gols_visitante"]) != (j.gm, j.gv) or not o.get("mandante_id"):
                continue
            do = _dia(o["data"])
            if dj and do and abs(dj - do) > 4:
                continue
            base = 1.0 if dj and do else 0.3
            for n, i, adv, adv_i in ((j.mandante, o["mandante_id"], j.visitante, o["visitante_id"]),
                                     (j.visitante, o["visitante_id"], j.mandante, o["mandante_id"])):
                if adv in ancora:
                    peso = 6.0 * base if ancora[adv] == adv_i else 0.0
                else:
                    peso = 0.3 * base * (1 + 2 * sim(adv, adv_i))
                if peso:
                    v_nome[(n, i)] += peso
                    v_ctx[(n, j.fase, j.grupo, i)] += peso
    saida: dict = {}
    # nome sozinho (tabelas gerais e reserva): âncoras primeiro, depois o resto, um para um
    pontos = [(v_nome.get((n, i), 0) + 6 * sim(n, i), n, i) for n in nomes_rs for i in noms if v_nome.get((n, i)) or sim(n, i) >= 0.6]
    usados: set[str] = set()
    for n, i in ancora.items():
        saida[n] = i; usados.add(i)
    for _, n, i in sorted(pontos, reverse=True):
        if n not in saida and i not in usados:
            saida[n] = i; usados.add(i)
    for n in nomes_rs - set(saida):   # duas grafias do mesmo clube na página ("Juventus" e "Juventus-SP")
        cands = [(sim(n, i), i) for i in usados]
        if cands and max(cands)[0] >= 0.85:
            saida[n] = max(cands)[1]
    # por grupo
    ctxs: dict[tuple, set] = defaultdict(set)
    for j in rs:
        ctxs[(j.fase, j.grupo)] |= {j.mandante, j.visitante}
    for (f, g), ns in ctxs.items():
        # vale o clube do nome; o grupo só troca quando os jogos dele apontam outro clube com folga
        for n in ns:
            base = manual.get(n) or saida.get(n)
            votos = {i: v for (n2, f2, g2, i), v in v_ctx.items() if (n2, f2, g2) == (n, f, g)}
            melhor = max(votos, key=votos.get) if votos else None
            if melhor and melhor != base and n not in manual and votos[melhor] >= 4 and votos[melhor] >= 3 * votos.get(base, 0):
                saida[(n, f, g)] = melhor
            elif base:
                saida[(n, f, g)] = base
    sem = sorted(n for n in nomes_rs if n not in saida)
    for n in sem if len(og) >= 20 else []:   # sem calendário no ogol, completar_sem_ogol casa pela cidade
        log.append(f"{ano}: nome da RSSSF sem clube no ogol (jogos dele ficam de fora): {n}")
    return saida


def penaltis(nota: str) -> tuple[int | None, int | None]:
    m = re.search(r"(?:pen(?:alties|altis|als)?|on penalties|nos pênaltis)\D{0,4}(\d{1,2})\s*[-x]\s*(\d{1,2})|(\d{1,2})-(\d{1,2}) on penalties", nota or "", re.I)
    if not m:
        return None, None
    a, b = (m[1], m[2]) if m[1] else (m[3], m[4])
    return int(a), int(b)


def ler_rsssf(ano: int, mapa: dict[str, str], rs: list) -> list[Partida]:
    saida = []
    for j in rs:
        m, v = mapa.get((j.mandante, j.fase, j.grupo)) or mapa.get(j.mandante), mapa.get((j.visitante, j.fase, j.grupo)) or mapa.get(j.visitante)
        if not (m and v):
            continue
        p = Partida(ano, j.fase, j.grupo, j.rodada, j.data, m, v, j.gm, j.gv, hora=j.hora or None, especial=j.especial,
                    estadio=j.estadio or None, publico=j.publico, fonte=FONTE_RSSSF.format(ano=str(ano)[:4]), gols_texto=j.gols, obs=j.nota, linha=j.linha)
        p.pen_m, p.pen_v = penaltis(f"{j.nota} {j.gols}")
        txt = re.sub(r"\[pen \d+-\d+\]", "", j.gols or "").strip()   # pênaltis que vieram junto dos autores (2015)
        p.gols_texto = txt
        if txt:
            lidos = gols_rsssf.ler_planilha(txt, j.gm, j.gv) if j.hora or j.estadio else None
            if lidos is None and txt.startswith("["):
                lidos = gols_rsssf.ler(txt, j.gm, j.gv, j.mandante, j.visitante)
            if lidos is not None and (lidos or (j.gm == 0 and j.gv == 0)):
                p.gols = [{**g, "fonte": "RSSSF"} for g in lidos]
        if j.estadio:
            p.estadio = re.sub(r"[-/][^-/]*-[A-Z]{2}$|[-/][A-Za-zÀ-ú .]+$", "", j.estadio).strip() or j.estadio
            mc = re.search(r"[-/]([^-/]+?)(?:-[A-Z]{2})?$", j.estadio)
            p.cidade = mc.group(1).strip() if mc else None
        saida.append(p)
    return saida


def campanha(partidas: list[Partida], so: set | None = None) -> dict[str, list[int]]:
    c: dict[str, list[int]] = defaultdict(lambda: [0] * 6)
    for p in partidas:
        if p.gm is None:
            continue
        for eu, a, b in ((p.mandante, p.gm, p.gv), (p.visitante, p.gv, p.gm)):
            x = c[eu]
            x[0] += 1; x[4] += a; x[5] += b
            x[1 if a > b else 2 if a == b else 3] += 1
    return c


def tabelas_por_clube(tabelas: list, mapa: dict[str, str], rs: list) -> list[tuple]:
    """[(tabela, {código: [J, V, E, D, GP, GC]})] com os nomes da tabela trocados pelo código do clube."""
    saida = []
    for tb in tabelas:
        if not tb.linhas:
            continue
        nomes_fase = {x for j in rs if j.fase == tb.fase and (not tb.grupo or j.grupo == tb.grupo) for x in (j.mandante, j.visitante)}
        alias = rsssf.casar([r["nome"] for r in tb.linhas], nomes_fase or {x for j in rs for x in (j.mandante, j.visitante)})
        if len(alias) < len(tb.linhas):
            alias.update(rsssf.casar([r["nome"] for r in tb.linhas if r["nome"] not in alias], {x for j in rs for x in (j.mandante, j.visitante)}))
        linhas, nome_id = {}, {}
        for r in tb.linhas:
            nr = alias.get(r["nome"], "")
            c = mapa.get((nr, tb.fase, tb.grupo)) or mapa.get(nr)
            if c:
                linhas[c] = [r["j"], r["v"], r["e"], r["d"], r["gp"], r["gc"]]
                nome_id[r["nome"]] = c
        saida.append((tb, linhas, nome_id))
    return saida


def bloco_da_tabela(tb, partidas: list[Partida]) -> list[Partida]:
    b = [p for p in partidas if p.fase == tb.fase and (p.grupo == tb.grupo or not tb.grupo)]
    if not tb.grupo and len({p.fase for p in partidas}) > 1 and re.search(r"final standings|classifica|overall|geral|^table$", tb.titulo or "", re.I):
        return partidas
    return b


def decidir_placar(p: Partida, alt: tuple[int, int], partidas: list[Partida], tabs: list[tuple]) -> bool:
    """True se o placar alternativo fecha melhor com as tabelas publicadas (dos dois clubes) que o atual."""
    def erros(lista):
        n = 0
        for tb, linhas, _ in tabs:
            if p.mandante not in linhas and p.visitante not in linhas:
                continue
            bl = bloco_da_tabela(tb, lista)
            if p not in bl and not any(q is p for q in bl):
                continue
            camp = campanha(bl)
            n += sum(camp.get(c) != linhas[c] for c in (p.mandante, p.visitante) if c in linhas)
        return n
    antes = erros(partidas)
    velho = (p.gm, p.gv)
    p.gm, p.gv = alt
    depois = erros(partidas)
    p.gm, p.gv = velho
    return depois < antes


def juntar_ogol(ano: int, partidas: list[Partida], og: list[dict], tabs: list[tuple], rs_ok: bool, log: list[str]) -> list[Partida]:
    """Casa cada jogo da RSSSF com o do ogol (mesmo par de clubes, data mais próxima); confere o placar; traz a hora,
    a data que falta e a rodada oficial ("R12"); inclui o que só o ogol tem."""
    usados: set[str] = set()
    datas_trocadas: list[Partida] = []
    datas_dif: list[tuple] = []
    por_par: dict[tuple, list[dict]] = defaultdict(list)
    for o in og:
        por_par[(o.get("mandante_id"), o.get("visitante_id"))].append(o)
    # antes: o mesmo jogo com o mando invertido, no mesmo dia e com o placar espelhado. Nas finais a RSSSF escreve as
    # partidas com o mesmo clube na frente ("[Dec 08] São Paulo 3-0 Corinthians", "[Dec 15] São Paulo 0-0 Corinthians"):
    # quando o mesmo par aparece assim mais de uma vez na fase, vale o mando do ogol
    for p in partidas:
        if p.gm is None or not _dia(p.data):
            continue
        if any(_dist(o["data"], p.data) <= 1 and (o["gols_mandante"], o["gols_visitante"]) == (p.gm, p.gv)
               for o in por_par.get((p.mandante, p.visitante), []) if o["id"] not in usados):
            continue
        inv = [o for o in por_par.get((p.visitante, p.mandante), []) if o["id"] not in usados and _dia(o["data"])
               and _dist(o["data"], p.data) <= 1 and (o["gols_mandante"], o["gols_visitante"]) == (p.gv, p.gm)]
        if len(inv) != 1:
            continue
        o = inv[0]
        usados.add(o["id"])
        repetido = sum((q.fase, q.mandante, q.visitante) == (p.fase, p.mandante, p.visitante) for q in partidas) > 1
        if repetido:
            log.append(f"{ano}: mando da RSSSF trocado pelo do ogol (a página escreve as partidas de {nome(p.mandante)} x "
                       f"{nome(p.visitante)} na {p.fase} sempre na mesma ordem) — ogol {nome(o['mandante_id'])} "
                       f"{o['gols_mandante']}-{o['gols_visitante']} {nome(o['visitante_id'])} ({o['data']})")
            p.mandante, p.visitante, p.gm, p.gv = p.visitante, p.mandante, p.gv, p.gm
            p.pen_m, p.pen_v = p.pen_v, p.pen_m
            p.gols = [{**g, "lado": "visitante" if g.get("lado") == "mandante" else "mandante"} for g in p.gols]
        else:
            log.append(f"{ano}: mando invertido no ogol — RSSSF {nome(p.mandante)} {p.gm}-{p.gv} {nome(p.visitante)}, ogol "
                       f"{nome(o['mandante_id'])} {o['gols_mandante']}-{o['gols_visitante']} {nome(o['visitante_id'])} "
                       f"({o['data']}); fica a RSSSF")
        p.fonte_id, p.ogol_fase, p.data = f"ogol:{o['id']}", o["fase"], o["data"]
        p.hora = p.hora or o.get("hora")
        p.rodada = p.rodada or o.get("rodada")
    for p in sorted(partidas, key=lambda p: (p.data is None, p.data or "")):
        if p.fonte_id:
            continue
        cands = [o for o in por_par.get((p.mandante, p.visitante), []) if o["id"] not in usados]
        if not cands:
            continue
        trocada = _trocar_dia_mes(p.data)
        dist = lambda o: min(_dist(o["data"], p.data), _dist(o["data"], trocada) if trocada else 999)
        cands.sort(key=lambda o: (dist(o), (o["gols_mandante"], o["gols_visitante"]) != (p.gm, p.gv)))
        o = cands[0]
        mesmo_placar = (o["gols_mandante"], o["gols_visitante"]) == (p.gm, p.gv)
        if dist(o) > 40 and not (mesmo_placar and dist(o) <= 120):   # data do título da fase nos jogos (1991, 1994)
            continue
        usados.add(o["id"])
        if p.data and o["data"] and _dia(o["data"]) and _dist(o["data"], p.data) > 3:
            if trocada and _dist(o["data"], trocada) <= 3:
                datas_trocadas.append(p)
            else:
                datas_dif.append((p, o["data"]))
            p.data = o["data"]   # a do ogol (a da RSSSF fica no relatório)
        p.fonte_id = f"ogol:{o['id']}"
        p.ogol_fase = o["fase"]
        p.ogol_placar = (o["gols_mandante"], o["gols_visitante"])
        p.hora = p.hora or o.get("hora")
        if not p.data:
            p.data = o["data"]
        if o.get("rodada") and not p.rodada:
            p.rodada = o["rodada"]
        alt = (o["gols_mandante"], o["gols_visitante"])
        if alt[0] is not None and p.gm is not None and alt != (p.gm, p.gv) and not p.especial:
            if decidir_placar(p, alt, partidas, tabs):
                log.append(f"{ano}: placar corrigido pelo ogol — {nome(p.mandante)} x {nome(p.visitante)} ({p.data}): "
                           f"RSSSF {p.gm}-{p.gv}, ogol {alt[0]}-{alt[1]}; fica o do ogol, que fecha com a tabela publicada")
                p.obs = (p.obs + "; " if p.obs else "") + f"placar da RSSSF {p.gm}-{p.gv} corrigido pelo ogol (fecha com a tabela publicada)"
                p.gm, p.gv = alt
                if p.gols and len(p.gols) != p.gm + p.gv:
                    p.gols = []
            else:
                log.append(f"{ano}: placar diferente no ogol — {nome(p.mandante)} x {nome(p.visitante)} ({p.data}): "
                           f"RSSSF {p.gm}-{p.gv}, ogol {alt[0]}-{alt[1]}; fica o da RSSSF")
        elif p.gm is None and alt[0] is not None:
            p.gm, p.gv = alt
    if datas_trocadas:
        log.append(f"{ano}: data com dia e mês trocados na RSSSF em {len(datas_trocadas)} jogos (ex.: {nome(datas_trocadas[0].mandante)} x "
                   f"{nome(datas_trocadas[0].visitante)}); fica a data do ogol")
    if datas_dif:
        p, d = datas_dif[0]
        log.append(f"{ano}: data diferente entre RSSSF e ogol (mais de 3 dias) em {len(datas_dif)} jogos (ex.: {nome(p.mandante)} x "
                   f"{nome(p.visitante)}, ogol {d}); fica a do ogol")
    # o que sobrou nas duas fontes e é o mesmo jogo: mando invertido (placar espelhado) ou um dos clubes diferente
    # no mesmo dia e com o mesmo placar. Fica o da RSSSF (base), e a diferença vai para o relatório.
    sobra = [p for p in partidas if not p.fonte_id]
    for o in og:
        if o["id"] in usados or o["gols_mandante"] is None:
            continue
        m, v, gm, gv = o.get("mandante_id"), o.get("visitante_id"), o["gols_mandante"], o["gols_visitante"]
        perto = lambda p: _dia(p.data) and _dia(o["data"]) and _dist(p.data, o["data"]) <= 4
        inv = [p for p in sobra if (p.mandante, p.visitante) == (v, m) and (p.gm, p.gv) == (gv, gm) and _dist(p.data, o["data"]) <= 3]
        inv_placar = [p for p in sobra if (p.mandante, p.visitante) == (v, m) and perto(p)]
        mesmo_par = [p for p in sobra if (p.mandante, p.visitante) == (m, v) and perto(p)]
        outro = [p for p in sobra if perto(p) and (p.gm, p.gv) == (gm, gv) and (p.mandante == m) != (p.visitante == v)]
        # mesmo jogo, mesmo dia e mês, ano diferente (1979: "19.08.78" num jogo de agosto de 1979)
        ano_errado = [p for p in sobra if (p.mandante, p.visitante) == (m, v) and (p.gm, p.gv) == (gm, gv) and p.data
                      and o["data"] and p.data[4:] == o["data"][4:] and p.data[:4] != o["data"][:4]]
        if len(ano_errado) == 1:
            p = ano_errado[0]
            usados.add(o["id"]); sobra.remove(p)
            log.append(f"{ano}: ano errado na data da RSSSF — {nome(m)} {gm}-{gv} {nome(v)}: RSSSF {p.data}, ogol {o['data']}; "
                       f"fica a do ogol")
            p.data, p.fonte_id, p.ogol_fase = o["data"], f"ogol:{o['id']}", o["fase"]
            p.hora = p.hora or o.get("hora")
            continue
        for lista, texto in ((inv, "mando invertido"), (inv_placar, "mando invertido e placar diferente"),
                             (mesmo_par, "placar diferente (jogo não achado pela data)"), (outro, "adversário diferente")):
            if len(lista) == 1:
                p = lista[0]
                usados.add(o["id"]); sobra.remove(p)
                p.fonte_id = f"ogol:{o['id']}"
                p.hora = p.hora or o.get("hora")
                log.append(f"{ano}: {texto} no ogol — RSSSF {nome(p.mandante)} {p.gm}-{p.gv} {nome(p.visitante)}, ogol {nome(m)} {gm}-{gv} "
                           f"{nome(v)} ({o['data']}); fica a RSSSF")
                break
    novos = []
    # 2007-2013 e 2017-2023: o calendário do ogol traz junto o Troféu do Interior (2023: a Taça Independência), torneio à parte entre clubes já eliminados, que a
    # leitura da RSSSF deixa de fora. Depois da 1ª fase, jogo só do ogol fica de fora quando é um jogo do Troféu na página
    # da RSSSF, quando os dois clubes jogaram o Troféu (a página às vezes não traz todos os jogos dele) ou quando nenhum
    # dos dois está no mata-mata do campeonato
    fim_1a, mata = None, set()
    trof_pares, trof_clubes = TROFEU.get(str(ano), (set(), set()))
    if rs_ok and int(str(ano)[:4]) in rsssf_sp2.ANOS_A_PARTE and partidas:
        com_data = sorted((p for p in partidas if p.data), key=lambda p: p.data)
        primeira = com_data[0].fase
        fim_1a = max(p.data for p in com_data if p.fase == primeira)
        mata = {x for p in partidas if p.fase != primeira for x in (p.mandante, p.visitante)}
    for o in og:
        if o["id"] in usados or o["gols_mandante"] is None or not (o.get("mandante_id") and o.get("visitante_id")):
            continue
        m, v = o["mandante_id"], o["visitante_id"]
        if fim_1a and o["data"] > fim_1a and (frozenset((m, v)) in trof_pares or {m, v} <= trof_clubes
                                              or not (m in mata or v in mata)):
            log.append(f"{ano}: jogo {'da Taça Independência' if str(ano) == '2023' else 'do Troféu do Interior'} no ogol "
                       f"(torneio à parte), fica de fora: "
                       f"{nome(m)} {o['gols_mandante']}-{o['gols_visitante']} {nome(v)} ({o['data']})")
            continue
        fase, grupo = fase_do_ogol(o, partidas)
        q = Partida(ano, fase, grupo, o.get("rodada"), o["data"], m, v, o["gols_mandante"], o["gols_visitante"], hora=o.get("hora"),
                    fonte="ogol", fonte_id=f"ogol:{o['id']}", ogol_fase=o["fase"])
        if re.search(r"\(\s*\d+\s*-\s*\d+\s*\)|pen", o.get("resultado") or "", re.I):
            mp = re.search(r"\(\s*(\d+)\s*-\s*(\d+)\s*\)", o["resultado"])
            if mp:
                q.pen_m, q.pen_v = int(mp[1]), int(mp[2])
        novos.append(q)
        if rs_ok:
            log.append(f"{ano}: jogo só no ogol, incluído em {fase}{' / ' + grupo if grupo else ''}: "
                       f"{nome(m)} {q.gm}-{q.gv} {nome(v)} ({q.data})")
    if rs_ok:
        for p in partidas:
            if not p.fonte_id and len(og) >= 20:   # 1988-1989: o ogol tem só 2 jogos soltos
                log.append(f"{ano}: só na RSSSF (não achado no ogol): {nome(p.mandante)} {p.gm}-{p.gv} {nome(p.visitante)} ({p.data})")
    return partidas + novos


OGOL_FASE = {"1F": "Primeira fase", "2F": "Segunda fase", "3F": "Terceira fase", "4F": "Quarta fase", "1/16": "Primeira fase eliminatória",
             "1/8": "Oitavas de final", "QF": "Quartas de final", "SF": "Semifinal", "F": "Final"}


def fase_do_ogol(o: dict, partidas: list[Partida]) -> tuple[str, str]:
    """Fase e grupo de um jogo que só o ogol tem: a fase e o grupo em que os dois clubes jogaram juntos, perto da data;
    senão, pelo código de fase do ogol."""
    m, v, d = o["mandante_id"], o["visitante_id"], _dia(o["data"])
    grupos = agrupar(partidas)
    # A2: jogo depois do último jogo da página (a página parou numa fase: 2010, 2012, 2025) vai pelo código do ogol
    ultimo = max((x for x in (_dia(p.data) for p in partidas) if x), default=None)
    f = o.get("fase") or ""
    if d and ultimo and d > ultimo + 3 and not re.match(r"^R\d+$", f):
        if f in OGOL_FASE:
            return OGOL_FASE[f], ""
        return "Segunda fase", f"Grupo {f}" if f else ""
    if d:
        perto, cobre = [], []
        for (f, g), ps in grupos.items():
            ds = [x for x in (_dia(p.data) for p in ps) if x]
            if not ds:
                continue
            cl = {x for p in ps for x in (p.mandante, p.visitante)}
            if m in cl and v in cl and min(ds) - 3 <= d <= max(ds) + 3:
                perto.append((min(abs(x - d) for x in ds), f, g))
            if min(ds) - 1 <= d <= max(ds) + 1:
                cobre.append(f)
        if perto:
            _, f, g = min(perto)
            return f, g
        # jogo que falta na página (o confronto todo): a única fase jogada naqueles dias (2022: quartas de final)
        if len(set(cobre)) == 1:
            return cobre[0], ""
    juntos = []
    for (f, g), ps in grupos.items():
        cl = {x for p in ps for x in (p.mandante, p.visitante)}
        if m in cl and v in cl:
            ds = [x for x in (_dia(p.data) for p in ps) if x]
            dist = min((abs(x - d) for x in ds), default=99) if d else 50
            juntos.append((dist, f, g))
    if juntos:
        _, f, g = min(juntos)
        return f, g
    f = o.get("fase") or ""
    if f in OGOL_FASE:
        return OGOL_FASE[f], ""
    if re.match(r"^R\d+$", f):
        return "Primeira fase", ""
    return "Primeira fase", f"Grupo {f}" if f else ""


def agrupar(partidas: list[Partida]) -> dict[tuple, list[Partida]]:
    d: dict[tuple, list[Partida]] = defaultdict(list)
    for p in partidas:
        d[(p.fase, p.grupo)].append(p)
    return d


def ler_espn(ano: int) -> list[dict]:
    f = ESPN / f"sp2_{str(ano).replace(" ", "_")}.json"
    return [j for j in json.loads(f.read_text(encoding="utf-8")) if j["situacao"] in ("STATUS_FULL_TIME", "STATUS_FINAL", "STATUS_FINAL_PEN",
                                                                                      "STATUS_FINAL_AET")] if f.exists() else []


def juntar_espn(ano: int, partidas: list[Partida], log: list[str]) -> None:
    """ESPN: hora local, estádio e cidade. O nome da ESPN vira código do ogol pelos jogos de mesmo placar no mesmo dia."""
    es = ler_espn(ano)
    if not es:
        return
    votos: dict[tuple, int] = defaultdict(int)
    por_dia: dict[str, list[Partida]] = defaultdict(list)
    for p in partidas:
        if p.data:
            por_dia[p.data].append(p)
    def local(e):
        utc = datetime.strptime(e["data_hora"][:16], "%Y-%m-%dT%H:%M")
        return utc - timedelta(hours=3)
    for e in es:
        l = local(e)
        for dia in (l.strftime("%Y-%m-%d"), (l - timedelta(days=1)).strftime("%Y-%m-%d"), (l + timedelta(days=1)).strftime("%Y-%m-%d")):
            for p in por_dia.get(dia, []):
                if (p.gm, p.gv) == (int(e["gols_mandante"]), int(e["gols_visitante"])):
                    votos[(e["mandante_id"], p.mandante)] += 1
                    votos[(e["visitante_id"], p.visitante)] += 1
    mapa, usados = {}, set()
    for (eid, cid), n in sorted(votos.items(), key=lambda x: -x[1]):
        if eid not in mapa and cid not in usados and n >= 2:
            mapa[eid] = cid; usados.add(cid)
    casados = 0
    for e in es:
        m, v = mapa.get(e["mandante_id"]), mapa.get(e["visitante_id"])
        l = local(e)
        cands = [p for p in partidas if (p.mandante, p.visitante) == (m, v) and _dia(p.data) and abs(_dia(p.data) - l.toordinal()) <= 2]
        if len(cands) != 1:
            continue
        p = cands[0]
        casados += 1
        if (p.gm, p.gv) != (int(e["gols_mandante"]), int(e["gols_visitante"])):
            log.append(f"{ano}: placar diferente na ESPN — {nome(m)} x {nome(v)} ({p.data}): aqui {p.gm}-{p.gv}, "
                       f"ESPN {e['gols_mandante']}-{e['gols_visitante']}; fica o daqui")
        p.hora = l.strftime("%H:%M")
        p.estadio = p.estadio or e.get("estadio")
        p.cidade = p.cidade or e.get("cidade")
        if e.get("publico"):
            p.publico = e["publico"]
        p.fonte_id = (p.fonte_id + ";" if p.fonte_id else "") + f"espn:{e['id']}"
    if casados < len(es):
        log.append(f"{ano}: ESPN — {casados} de {len(es)} jogos casados (hora e estádio)")


# --------------------------------------------------------------------------------------------- fases e nomes

FASES_PT = [
    # Paulista: turnos (com as grafias das páginas) e fases com outro nome
    (r"^final table", "Primeira fase"),   # 1996: os jogos do 1º turno vêm sob o título da tabela final
    # A2: "FIRST STAGE:" quebrado em duas linhas (2022-2025); a semifinal e a final da 1ª fase de 2000; o quadrangular de
    # acesso de 1998 ("Promotion Playoff", que dá o título)
    (r"^(stage|phase)$", "Primeira fase"), (r"^first phase - semi", "Primeira fase - Semifinal"),
    (r"^first phase - final", "Primeira fase - Final"), (r"^promotion playoff", "Fase final"),
    (r"^(1º|1o\.?|1ª|primeiro)\s*turno\s*-\s*qualifying", "1º Turno - Classificatória"),
    (r"^(2º|2o\.?|segundo)\s*turno\s*-\s*qualifying", "2º Turno - Classificatória"),
    (r"^(2º|2o\.?|segundo)\s*turno\s*-\s*1st phase", "2º Turno - 1ª fase"),
    (r"^(2º|2o\.?|segundo)\s*turno\s*-\s*2nd phase", "2º Turno - 2ª fase"),
    (r"^(1º|1o\.?|1ª|primeiro)\s*turno", "1º Turno"), (r"^(2º|2o\.?|segundo)\s*turno", "2º Turno"),
    (r"^phase 1$", "Primeira fase"), (r"^phase 2$", "Segunda fase"), (r"^phase 3$", "Terceira fase"),
    (r"^repescagem", "Repescagem"), (r"relegation", "Torneio de rebaixamento"),
    (r"decide which team would be eliminated", "Desempate"), (r"1995 - final fase", "Fase final"),
    (r"^semfinals?$", "Semifinal"), (r"^final playoff", "Final"), (r"^classifica[çc][ãa]o final", "Fase final"),
    # 1977: três turnos, os dois primeiros com semifinal e final próprias
    (r"^first stage - first phase", "1º Turno"), (r"^first stage - semi", "1º Turno - Semifinal"),
    (r"^first stage - final", "1º Turno - Final"), (r"^second stage - first phase", "2º Turno"),
    (r"^second stage - semi", "2º Turno - Semifinal"), (r"^second stage - final", "2º Turno - Final"),
    (r"^third stage$", "3º Turno"),
    (r"^(fase única|first stage|first phase|1st phase|1a fase|1ª fase|primeira fase|grupo único|group stage)", "Primeira fase"),
    (r"^(second (phase|stage|round)|2nd phase|2a fase|2ª fase|segunda fase)", "Segunda fase"),
    (r"^(third (phase|stage)|3rd phase|3a fase|terceira fase)(?!.*(semi|final))", "Terceira fase"),
    (r"^(fourth (phase|stage)|4th phase|quarta fase)(?!.*(semi|final))", "Quarta fase"),
    (r"serie c\s*-\s*-\s*fourth phase", "Quarta fase"),
    (r"round of 32", "Segunda fase"), (r"^(round of 16|1/8|eighth|oitavas)", "Oitavas de final"),
    (r"(quarter|quartas)", "Quartas de final"), (r"(semi)", "Semifinal"),
    (r"(final phase|final stage|quadrangular final|final standings)", "Fase final"),
    (r"(^|\W)finals?\W*$|final$|^final", "Final"), (r"knockout", "Mata-mata"),
]


def grupo_pt(g: str) -> str:
    """"Group A" -> "Grupo A"; "Green Group" -> "Grupo Verde"; "Série Branca (Torneio de Rebaixamento)" -> "Série Branca";
    "teams of Group 1 against teams of Group 2" (jogos entre os grupos) -> sem grupo."""
    g = (g or "").strip(" :")
    if re.match(r"teams\b", g, re.I):
        return ""
    g = re.sub(r"\s*\(.*\)$", "", g)
    cores = {"green": "Verde", "yellow": "Amarelo", "blue": "Azul", "white": "Branco", "red": "Vermelho", "black": "Preto",
             "gold": "Dourado", "silver": "Prata"}
    if (m := re.match(r"^(\w+) group$|^group (\w+)$", g, re.I)) and (m[1] or m[2]).lower() in cores:
        return f"Grupo {cores[(m[1] or m[2]).lower()]}"
    return re.sub(r"^group\b", "Grupo", g, flags=re.I)


def fase_pt(nome_fase: str) -> str:
    n = nome_fase.strip(" :")
    for padrao, pt in FASES_PT:
        if re.search(padrao, n, re.I):
            return pt
    return n


# nome da RSSSF -> código do ogol, de todas as temporadas já lidas (o mesmo clube em anos sem calendário no ogol)
JA_CASADOS: dict[str, str] = {}
# temporada -> (pares de clubes, clubes) dos jogos do Troféu do Interior na página da RSSSF (2017-2022)
TROFEU: dict[str, tuple[set, set]] = {}


_PARTICIPANTES: dict[str, list[tuple[str, str]]] = {}
_SIGLAS = re.compile(r"\b(?:associa[çc][ãa]o|atl[ée]tic[ao]|esporte|esportes|esportiva|clube|club|futebol|sociedade|gr[êe]mio|"
                     r"desportiva|recreativ[ao]|agr[íi]cola|de|do|da|ec|fc|aa|ae|ac|ca|ge|se|ad|ea|sc|ltda)\b", re.I)


def participantes(ano) -> list[tuple[str, str]]:
    """[(nome, cidade)] da lista de participantes da página: "AA Portuguesa (Santos)", "Capivariano FC - Capivari",
    "Associacao Atletica PONTE PRETA        Campinas" (1997-1999, em colunas, com o nome do clube em maiúsculas).
    Só linhas sem placar e sem nota entre colchetes."""
    t = str(ano)
    if t not in _PARTICIPANTES:
        saida = []
        for l in (rsssf.texto(int(t[:4])).splitlines() if rsssf_sp2.tem_pagina(t) else []):
            if re.search(r"\d\s*[-x]\s*\d|[\[\]]", l):
                continue
            for trecho in re.split(r"\s{3,}(?=\S.*\()", l):   # 1996: duas colunas de participantes na mesma linha
                m = (re.match(r"^\s*([^()\d]+?)\s*\(([^()\d]+)\)", trecho) or re.match(r"^\s*([^()\d]+?)\s+-\s+([^-()\d]+?)\s*$", trecho)
                     or ((m2 := re.match(r"^\s*(\S[^\d()]*?)\s{3,}(\S[^\d()]*?)\s*$", trecho))
                         and re.search(r"\b[A-ZÀ-Ý]{3,}\b", m2.group(1)) and m2))
                if m and len(m.group(2).split()) <= 5:
                    saida.append((m.group(1).strip(), m.group(2).strip()))
        _PARTICIPANTES[t] = saida
    return _PARTICIPANTES[t]


def cidade_na_pagina(ano, n: str) -> str | None:
    """Cidade do participante cujo nome mais se parece com o da página: o nome em maiúsculas ("Associação ESPORTIVA
    Guaratinguetá") ou, sem ele, o nome sem as siglas por extenso ("Associação Esportiva Araçatuba" -> "Araçatuba")."""
    melhor = (0.0, None)
    for nome_p, cidade in participantes(ano):
        caps = " ".join(re.findall(r"\b[A-ZÀ-Ý][A-ZÀ-Ý\-]{2,}\b", nome_p))
        base = re.sub(r"\s+", " ", _SIGLAS.sub(" ", nome_p)).strip()
        s = max(_sim(n, caps) if caps else 0, _sim(n, base) if base else 0, 0.9 if clubes_sp2.norm(n) == clubes_sp2.norm(nome_p) else 0,
                min(0.95, _sim(n, nome_p)))
        if s > melhor[0]:
            melhor = (s, cidade)
    return melhor[1] if melhor[0] >= 0.7 else None


def fundado_depois(k: str, ano, fs: dict) -> bool:
    """A ficha é de um clube fundado depois da edição (CA Votuporanguense, de 2009, não é a AA Votuporanguense de 1988)."""
    f = (fs.get(k, {}).get("fundacao") or "")[:4]
    return f.isdigit() and int(f) > int(str(ano)[:4])


def pela_cidade(ano, n: str, fs: dict, log: list[str], cidade: str | None = None) -> str | None:
    """O clube das fichas do ogol (A2 e A1) da cidade do participante e de nome parecido, quando é um só (e já existia).
    A cidade vem da lista de participantes da página ou, nas edições sem os jogos, da própria tabela."""
    cidade = cidade or cidade_na_pagina(ano, n)
    if not cidade:
        return None
    fs = {k: f for k, f in fs.items() if not fundado_depois(k, ano, fs)}
    c = clubes_sp2.norm(cidade)
    reserva = lambda f: re.search(r"\s(?:II|B|Sub-?\d+)$", f.get("curto") or "")   # time B ("Red Bull Bragantino II")
    mesma = [(max((_sim(n, x) for x in (f.get("curto"), *f.get("nomes_ogol", []), f.get("nome_completo")) if x), default=0), k)
             for k, f in fs.items() if not k.startswith("rs-") and f.get("cidade") and not reserva(f)
             and (clubes_sp2.norm(f["cidade"]) == c or clubes_sp2.norm(f["cidade"]).startswith(c + " ") or c.startswith(clubes_sp2.norm(f["cidade"]) + " "))]
    mesma = sorted((x for x in mesma if x[0] >= 0.5), reverse=True)
    if mesma and (len(mesma) == 1 or mesma[1][0] < mesma[0][0]):
        return mesma[0][1]
    return None


def completar_sem_ogol(ano, mapa: dict, rs: list, og: list, log: list[str]) -> None:
    """Nomes da RSSSF sem clube no ogol daquela temporada: usa o clube do mesmo nome em outra temporada do Paulista;
    se nunca apareceu, vira clube só da RSSSF ("rs-..."), com o nome da página."""
    for n, i in list(mapa.items()):
        if isinstance(n, str):
            JA_CASADOS.setdefault(clubes_sp2.norm(n), i)
    sem = sorted({x for j in rs for x in (j.mandante, j.visitante)} - {n for n in mapa if isinstance(n, str)})
    fs = clubes_sp2.fichas()
    for n in sem:
        # sem calendário no ogol: a cidade da lista de participantes da página separa os homônimos ("Portuguesa" de Santos,
        # "Corinthians" de Presidente Prudente, "Palmeiras" de São João da Boa Vista)
        sem_calendario = len(og) < 20   # 1988 e 1989: o ogol tem só 2 jogos soltos
        i = pela_cidade(ano, n, fs, log) if sem_calendario else None
        cidade = clubes_sp2.norm(cidade_na_pagina(ano, n) or "") if sem_calendario else ""
        def outra_cidade(k):   # o clube do mesmo nome é de outra cidade ("Palmeiras" de São João da Boa Vista)
            c = clubes_sp2.norm(fs.get(k, {}).get("cidade") or clubes_sp2.exibicao().get(k, {}).get("cidade") or "")
            return (fundado_depois(k, ano, fs)
                    or bool(cidade and c and c != cidade and not c.startswith(cidade + " ") and not cidade.startswith(c + " ")))
        if not i and (k := JA_CASADOS.get(clubes_sp2.norm(n))) and not outra_cidade(k):
            i = k
        if not i:   # o mesmo nome numa ficha do ogol (clube de temporadas lidas mais adiante: Atlético Sorocaba em 2003)
            achados = [k for k, f in fs.items() if not k.startswith("rs-") and clubes_sp2.norm(n) in
                       {clubes_sp2.norm(x) for x in (f.get("curto"), *f.get("nomes_ogol", [])) if x}]
            i = achados[0] if len(achados) == 1 and not outra_cidade(achados[0]) else None
            if len(achados) == 1 and not i:
                log.append(f"{ano}: {n} ({cidade_na_pagina(ano, n)}) — não é o {nome(achados[0])}, de outra cidade")
        if i:
            mapa[n] = i
            log.append(f"{ano}: {n} — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas ({nome(i)})")
        else:
            cid_txt = cidade_na_pagina(ano, n) if sem_calendario else None
            # clube só da RSSSF já criado com outra grafia, na mesma cidade ("Pinhalense" e "Ginásio Pinhalense")
            iguais = [k for k, f in clubes_sp2.SEM_OGOL.items() if cid_txt and clubes_sp2.norm(f.get("cidade") or "") == clubes_sp2.norm(cid_txt)
                      and (_sim(n, f["curto"]) >= 0.8 or clubes_sp2.norm(n) in clubes_sp2.norm(f["curto"])
                           or clubes_sp2.norm(f["curto"]) in clubes_sp2.norm(n))]
            mapa[n] = iguais[0] if len(iguais) == 1 else clubes_sp2.sem_ogol(n, cid_txt)
            JA_CASADOS[clubes_sp2.norm(n)] = mapa[n]
            log.append(f"{ano}: {n} — clube que o ogol não tem; entra só pela RSSSF")
    for j in rs:   # chaves por grupo, como as de mapear_nomes
        for n in (j.mandante, j.visitante):
            mapa.setdefault((n, j.fase, j.grupo), mapa.get(n))


def nome(cid: str) -> str:
    return clubes_sp2.exibicao().get(cid, {}).get("clube", cid)


# --------------------------------------------------------------------------------------------- classificação

def pontos_vitoria(ano) -> int:
    return 3 if int(str(ano)[:4]) >= 1995 else 2


def ajustes_wiki(ano: int, ids_do_ano: set[str]) -> dict[str, int]:
    """Punições de pontos na Wikipédia em inglês (adjust_points), com o nome casado ao código do ogol."""
    saida = {}
    fs = clubes_sp2.exibicao()
    for nome_w, v in wiki.ajustes(ano).items():
        cands = sorted(((_sim(nome_w, fs[i]["clube"]), i) for i in ids_do_ano if i in fs), reverse=True)
        if cands and cands[0][0] >= 0.75 and v:
            saida[cands[0][1]] = v
    return saida


def classificacao(ano: int, partidas: list[Partida], tabs: list[tuple], ajustes: dict[str, int], campeao: str | None,
                  log: list[str]) -> list[dict]:
    """Fase alcançada, depois pontos (com punições), vitórias, saldo e gols pró; o campeão e o vice da final em cima.
    Quando a RSSSF publica a classificação geral com todos os clubes e ela fecha com os jogos, vale a ordem dela."""
    camp = campanha(partidas)
    pv = pontos_vitoria(ano)
    sem_nivel = sorted({p.fase for p in partidas} - set(ORDEM))
    if sem_nivel:   # fase nova sem nível: antes caía num padrão 50, acima da Final (achado SP-002 do Paulista)
        raise ValueError(f"{ano}: fase sem nível no ORDEM: {sem_nivel}")
    ordem_fase: dict[str, int] = {}
    for p in partidas:
        # torneio de rebaixamento e repescagem não são avanço: quem os joga fica com a fase anterior
        ordem_fase.setdefault(p.fase, 0 if p.fase in ("Torneio de rebaixamento", "Repescagem") else ORDEM[p.fase])
    alcance: dict[str, int] = defaultdict(int)
    for p in partidas:
        for c in (p.mandante, p.visitante):
            alcance[c] = max(alcance[c], ordem_fase[p.fase])
    final = [p for p in partidas if p.fase == "Final"]
    vice = None
    if campeao and final:
        fin = {x for p in final for x in (p.mandante, p.visitante)} - {campeao}
        if len(fin) == 1:
            vice = next(iter(fin))
        elif fin:   # quadrangular/triangular final: o vice é o 2º do grupo final
            cf = campanha(final)
            vice = max(fin, key=lambda c: (pv * cf[c][1] + cf[c][2], cf[c][1], cf[c][4] - cf[c][5], cf[c][4]))
    # liga decisiva de um grupo só ("Fase final", 1979, 1986, 1996, 1997): quem chegou a ela desempata pelos pontos dela
    # antes dos totais (achados A2-002 a A2-005)
    ff = [p for p in partidas if p.fase == "Fase final"]
    cff = campanha(ff) if ff and len({p.grupo for p in ff}) == 1 else {}
    pos_grupo: dict[str, int] = {}
    if not cff:
        # sem ela: a última fase de grupos (2 ou mais, cada clube com 3 ou mais jogos) antes da final; quem chegou a ela e
        # não à final se ordena pela posição no grupo e depois pelos pontos dela: os 2º de cada grupo são o 3º e o 4º
        # (decisão D-02 A; achado A2-024: 1987, 2006, 2007, 2009, 2010, 2012, como a Wikipédia)
        jogos_fase: dict[str, Counter] = defaultdict(Counter)
        for p in partidas:
            jogos_fase[p.fase].update([p.mandante, p.visitante])
        ligas = [f for f, n in jogos_fase.items() if 2 <= ordem_fase[f] < ORDEM["Final"] and min(n.values()) >= 3
                 and len({p.grupo for p in partidas if p.fase == f}) >= 2]
        if ligas:
            fd = max(ligas, key=lambda f: ordem_fase[f])
            cff = campanha([p for p in partidas if p.fase == fd])
            for g in {p.grupo for p in partidas if p.fase == fd}:
                cg = campanha([p for p in partidas if p.fase == fd and p.grupo == g])
                ordem_g = sorted(cg, key=lambda c: (-(pv * cg[c][1] + cg[c][2]), -cg[c][1], -(cg[c][4] - cg[c][5]), -cg[c][4]))
                pos_grupo.update({c: i for i, c in enumerate(ordem_g, 1)})
    especiais = pontos_penaltis(partidas) if str(ano) in PONTOS_PENALTIS else None
    def pts(c):
        x = camp[c]
        return (especiais[c] if especiais is not None else pv * x[1] + x[2]) + ajustes.get(c, 0)
    def chave(c):
        x, y = camp[c], cff.get(c, [0] * 6)
        return (c != campeao, c != vice, -alcance[c], pos_grupo.get(c, 99), -(pv * y[1] + y[2]), -pts(c), -x[1], -(x[4] - x[5]),
                -x[4], nome(c))
    # classificação geral publicada pela RSSSF (todos os clubes da edição)
    geral = [(tb, linhas) for tb, linhas, _ in tabs if len(linhas) >= len(camp) and len(tb.linhas) >= len(camp)]
    fonte = "calculada (fase alcançada, pontos, vitórias, saldo, gols pró)"
    ordem = sorted(camp, key=chave)
    if geral:
        tb, linhas = geral[-1]
        bate = sum(camp.get(c) == v for c, v in linhas.items())
        if bate >= 0.9 * len(camp):   # a ordem das linhas é a ordem da tabela
            ordem = list(linhas) + [c for c in ordem if c not in linhas]
            fonte = "RSSSF (classificação geral publicada)"
            # a tabela geral soma pontos: o campeão e o outro finalista vão para o 1º e o 2º (A2-006, 2013)
            ordem = [c for c in (campeao, vice) if c in ordem] + [c for c in ordem if c not in (campeao, vice)]
    saida = []
    for i, c in enumerate(ordem, 1):
        x = camp[c]
        saida.append({"pos": i, "clube": c, "j": x[0], "v": x[1], "e": x[2], "d": x[3], "gp": x[4], "gc": x[5], "pts": pts(c),
                      "ajuste": ajustes.get(c, 0), "fonte": fonte})
    return saida


ORDEM = {"Primeira fase": 1, "Segunda fase": 2, "Terceira fase": 3, "Quarta fase": 4, "Mata-mata": 5, "Primeira fase eliminatória": 5,
         "Oitavas de final": 6, "Quartas de final": 7, "Semifinal": 8, "Fase final": 9, "Final": 10, "Fase única": 1,
         # A2: fases paralelas ou intermediárias
         "Primeira fase - Semifinal": 1.3, "Primeira fase - Final": 1.6, "1º Turno": 1, "2º Turno": 2, "3º Turno": 3,
         "Torneio de rebaixamento": 2.5, "Repescagem": 11, "Primeira fase - Desempate": 1.5}


# --------------------------------------------------------------------------------------------- uma edição

def campeoes() -> tuple[dict[str, str], dict[str, str]]:
    """Campeões pela RSSSF (sp2camp.htm, "1997 - Sociedade Esportiva Matonense (Matão)"): temporada -> nome completo,
    com a cidade entre parênteses ("Esporte Clube XV de Novembro (Piracicaba)"), que separa os homônimos. Sem Wikipédia."""
    rs: dict[str, str] = {}
    t = rsssf.texto(0, "sp2camp.htm")
    for l in t.splitlines():
        m = re.match(r"^\s*(\d{4}) - (.+?)\s*$", l)
        if m and "?" not in m.group(2):
            rs[m.group(1)] = re.sub(r"\s*\(\*+\)|\s+-\s+(?:not )?promoted.*$", "", m.group(2)).strip()
    # nomes antigos: Ferroviário Atlético Ituano (1989) é o Ituano FC; Etti Jundiaí (2001) é o Paulista FC com o nome do
    # patrocinador (1999-2001)
    troca = {"Ferroviário Atlético Ituano": "Ituano Futebol Clube", "Etti Jundiaí Futebol Ltda.": "Paulista Futebol Clube"}
    for velho, novo in troca.items():
        rs = {a: n.replace(velho, novo) for a, n in rs.items()}
    return rs, {}


def montar_edicao(ano: int, log: list[str], rs_campeoes: dict, wk_campeoes: dict) -> dict:
    rs, tabelas = rsssf_sp2.ler(ano) if rsssf_sp2.tem_pagina(ano) else ([], [])
    for (a, n), motivo in RSSSF_FORA.items():
        if str(a) == str(ano):
            fora = [j for j in rs if n in (j.mandante, j.visitante)]
            rs = [j for j in rs if j not in fora]
            log.append(f"{ano}: {len(fora)} jogos do {n} ficam de fora: {motivo}")
    for (a, m, v, gm, gv), motivo in JOGOS_ANULADOS.items():
        if str(a) == str(ano):
            fora = [j for j in rs if (j.mandante, j.visitante, j.gm, j.gv) == (m, v, gm, gv)]
            rs = [j for j in rs if j not in fora]
            log.append(f"{ano}: jogo anulado fica de fora ({len(fora)}): {m} {gm}-{gv} {v} — {motivo}")
    for i, motivo in OGOL_IGNORAR.items():
        if motivo.startswith(str(ano)):
            log.append(f"{ano}: jogo do ogol ignorado — {motivo[6:]}")
    og = ler_ogol(ano)
    rs_ok = ano not in BASE_OGOL
    if not rs_ok:
        log.append(f"{ano}: {BASE_OGOL[ano]}")
        rs_usado, tabelas = [], []
    else:
        rs_usado = rs
    if ano in TABELAS_PARCIAIS:
        log.append(f"{ano}: {TABELAS_PARCIAIS[ano]}")
        tabelas = []
    de_um_jogo = [tb for tb in tabelas if tb.linhas and max(r["j"] for r in tb.linhas) <= 1]
    if de_um_jogo:   # "Standings" depois da 1ª rodada do mata-mata (2020): retrato parcial, não é conferência
        log.append(f"{ano}: {len(de_um_jogo)} tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência")
        tabelas = [tb for tb in tabelas if tb not in de_um_jogo]
    mapa = mapear_nomes(ano, rs_usado, og, log) if rs_usado else {}
    completar_sem_ogol(ano, mapa, rs_usado, og, log)
    mapa = {k: refundado(ano, v) for k, v in mapa.items()}
    partidas = ler_rsssf(ano, mapa, rs_usado)
    partidas = [p for p in partidas if p.gm is not None or p.especial]
    tabs = tabelas_por_clube(tabelas, mapa, rs_usado)
    if int(str(ano)[:4]) in rsssf_sp2.ANOS_A_PARTE:   # jogos do Troféu do Interior / Taça Independência, para tirar do ogol
        tj = rsssf_sp2.trofeu(str(ano))
        cod = lambda n: mapa.get(n) or JA_CASADOS.get(clubes_sp2.norm(n))
        TROFEU[str(ano)] = ({frozenset((cod(j.mandante), cod(j.visitante))) for j in tj},
                            {c for j in tj for c in (cod(j.mandante), cod(j.visitante)) if c})
    partidas = juntar_ogol(ano, partidas, og, tabs, rs_ok, log)
    juntar_espn(ano, partidas, log)   # sem arquivo da ESPN, não faz nada
    juntar_wikipedia(ano, partidas, mapa, log)
    # fases em português, nos jogos e nas tabelas (as tabelas já estão ligadas aos códigos dos clubes)
    for p in partidas:
        p.fase = fase_pt(p.fase) if rs_ok else fase_pt(OGOL_FASE.get(p.ogol_fase, p.fase))
        # mata-mata: quando a página não tem o título da fase (2025: a final vem sob "Semi-finals"), vale o código do ogol
        if p.ogol_fase in ("QF", "SF", "F") and p.fase in ("Quartas de final", "Semifinal", "Final") and p.fase != OGOL_FASE[p.ogol_fase]:
            log.append(f"{ano}: {nome(p.mandante)} x {nome(p.visitante)} ({p.data}) vem na página em \"{p.fase}\"; o ogol diz "
                       f"\"{OGOL_FASE[p.ogol_fase]}\", que fica")
            p.fase = OGOL_FASE[p.ogol_fase]
        p.grupo = grupo_pt(p.grupo) if not p.grupo.lower().startswith(("grupo único", "grupo unico")) else ""
    for tb in tabelas:
        tb.fase = fase_pt(tb.fase)
        tb.grupo = grupo_pt(tb.grupo)
    obs_ed = []
    fora = [p for p in partidas if (str(ano), p.fase) in PLAYOFF_FORA]
    if fora:
        partidas = [p for p in partidas if p not in fora]
        jogos = ", ".join(f"{nome(p.mandante)} {p.gm}-{p.gv} {nome(p.visitante)} ({p.data[8:10]}/{p.data[5:7]})" for p in fora)
        obs_ed.append(f"{PLAYOFF_FORA[(str(ano), fora[0].fase)]} contra a 1ª divisão ({jogos}) fica fora da A2 e só nesta "
                      f"observação (decisão D-04); os jogos estão no Paulista (bra-sp-1)")
        log.append(f"{ano}: {len(fora)} jogos do playoff contra a 1ª divisão ficam fora (D-04, A2-012)")
    if len({p.fase for p in partidas}) == 1 and not any(p.grupo for p in partidas):
        for x in [*partidas, *tabelas]:
            x.fase = "Fase única"
    # autores: só quando fecham com o placar
    for p in partidas:
        if p.gols and p.gm is not None and len(p.gols) != p.gm + p.gv:
            p.gols = []
    ids = {x for p in partidas for x in (p.mandante, p.visitante)}
    ajustes = {c: v for (tt, n), (v, _) in AJUSTES_MANUAIS.items() if tt == str(ano) for c in ids if nome(c) == n}
    for (tt, n), (v, motivo) in AJUSTES_MANUAIS.items():
        if tt == str(ano):
            log.append(f"{ano}: {n} {v:+d} pontos — {motivo}")
    # campeão: vencedor da final; conferido com a RSSSF e a Wikipédia (final empatada sem pênaltis: vale a lista oficial)
    campeao = vencedor_final(partidas)
    oficial = campeao_oficial(ano, partidas, rs_campeoes, wk_campeoes)
    tem_final = any(p.fase in ("Final", "Fase final") for p in partidas)
    if campeao is None and oficial and not tem_final:
        # sem final (pontos corridos, ou finais com outro nome): confere com o 1º da campanha da última fase
        lider = lider_ultima_fase(ano, partidas)
        campeao = oficial
        if lider != oficial:
            log.append(f"{ano}: campeão pela lista oficial, {nome(oficial)}; o 1º pela soma dos jogos da última fase é "
                       f"{nome(lider) if lider else '?'} (desempate, jogo extra ou pontos tirados fora de campo)")
    elif campeao is None and oficial:
        campeao = oficial
        log.append(f"{ano}: final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, {nome(oficial)}")
    elif oficial and campeao != oficial:
        log.append(f"{ano}: vencedor da final pelos jogos ({nome(campeao)}) diferente do campeão oficial ({nome(oficial)}); fica o oficial")
        campeao = oficial
    final = classificacao(ano, partidas, tabs, ajustes, campeao, log)
    conf = conferir(ano, partidas, tabs)
    return {"partidas": partidas, "tabelas": tabelas, "tabs": tabs, "final": final, "conf": conf, "rs": rs, "og": og,
            "mapa": mapa, "campeao": campeao, "ajustes": ajustes, "obs": obs_ed}


# temporadas com jogos na RSSSF ou no ogol que a Wikipédia completa (1989: as semifinais; a final já vem do ogol)
WIKI_JUNTAR = {"1989"}


def juntar_wikipedia(ano, partidas: list[Partida], mapa: dict, log: list[str]) -> None:
    """Jogos da Wikipédia em português que nem a RSSSF nem o ogol têm (o mesmo par de clubes em até 3 dias é o mesmo jogo)."""
    if str(ano) not in WIKI_JUNTAR:
        return
    import wikipedia_sp2
    cod = lambda n: mapa.get(n) or JA_CASADOS.get(clubes_sp2.norm(n))
    for j in wikipedia_sp2.jogos(str(ano)):
        m, v = cod(j["mandante"]), cod(j["visitante"])
        if not (m and v):
            log.append(f"{ano}: jogo da Wikipédia sem clube conhecido, fica de fora: {j['mandante']} x {j['visitante']}")
            continue
        if any({p.mandante, p.visitante} == {m, v} and p.data and j["data"] and abs(_dia(p.data) - _dia(j["data"])) <= 3
               for p in partidas):
            continue
        partidas.append(Partida(ano, j["fase"], j["grupo"], None, j["data"], m, v, j["gm"], j["gv"], fonte="Wikipédia (pt)",
                                fonte_id=f"wikipedia:pt_{ano}:{j['linha']}", linha=j["linha"]))
        log.append(f"{ano}: jogo só na Wikipédia, incluído em {j['fase']}: {nome(m)} {j['gm']}-{j['gv']} {nome(v)} ({j['data']})")


def campeao_oficial(ano: int, partidas: list[Partida], rs_c: dict, wk_c: dict, ids: set | None = None) -> str | None:
    """O clube da edição cujo nome bate com o campeão da lista da RSSSF ("Esporte Clube XV de Novembro (Piracicaba)"): o
    nome sem as siglas por extenso, e a cidade entre parênteses desempata os homônimos (XV de Piracicaba x XV de Jaú)."""
    alvo = rs_c.get(ano) or (wk_c.get(str(ano)) or wk_c.get(str(ano)[:4], "")).split(" / ")[0]
    if not alvo:
        return None
    mc = re.search(r"\s*\(([^)]+)\)\s*$", alvo)
    cidade = clubes_sp2.norm(mc.group(1)) if mc else ""
    alvo = alvo[:mc.start()].strip() if mc else alvo
    fs = clubes_sp2.fichas()
    ids = ids or {x for p in partidas for x in (p.mandante, p.visitante)}   # edições sem os jogos: os clubes das tabelas
    nomes_rs: dict[str, set] = defaultdict(set)   # nomes da página ligados a cada clube ("XV Piracicaba")
    for p in partidas:
        nomes_rs[p.mandante].add(nome(p.mandante)); nomes_rs[p.visitante].add(nome(p.visitante))
    def nota(i):
        nomes = {nome(i), *(fs.get(i, {}).get("nomes_ogol") or []), fs.get(i, {}).get("nome_completo") or "", fs.get(i, {}).get("curto", "")}
        # "Associação Atlética São Bento" (nome completo na lista da RSSSF): também sem a sigla por extenso
        curto = re.sub(r"^(Associa[çc][ãa]o|Sport|Clube|Club|Esporte|Sociedade|Gr[eê]mio|Athletic|Atl[eé]tica|Atl[eé]tico|"
                       r"Esportiva|Esportivo|Recreativa|Recreativo|Agr[ií]cola|Desportiva|Club[e]?|de|Futebol|Football|\s)+\b", "",
                       alvo, flags=re.I).strip()
        curto = re.sub(r"(?:\s+(?:Futebol Clube|Esporte Clube|Atl[eé]tico Clube|Futebol Ltda\.?|Ltda\.?|FC|EC))+$", "", curto, flags=re.I)
        cheio = max(_sim(alvo, x) for x in nomes if x)
        na_cidade = cidade and (clubes_sp2.norm(fs.get(i, {}).get("cidade") or "") == cidade
                                or any(cidade in clubes_sp2.norm(x) for x in nomes | nomes_rs[i] if x))
        return max(cheio, max(_sim(curto, x) for x in nomes if x) if curto else 0) + 0.05 * cheio + (0.15 if na_cidade else 0)
    melhor = sorted(((nota(i), i) for i in ids), reverse=True)
    return melhor[0][1] if melhor and melhor[0][0] >= 0.8 and (len(melhor) == 1 or melhor[1][0] < melhor[0][0]) else None


# edições em que a RSSSF não serve de base (o ogol é a base dos jogos)
BASE_OGOL: dict[str, str] = {
    "2026": "sem página da RSSSF: os jogos vêm do ogol",
}
# edições em que as tabelas publicadas pela RSSSF são parciais (a página parou no meio): não servem de conferência
TABELAS_PARCIAIS: dict[str, str] = {}
# temporadas sem os jogos em nenhuma fonte: a RSSSF traz só os pontos de cada fase (1947-1966), a ordem final (1992, 1993) ou
# a tabela final (1994). Entram só com as tabelas, o campeão e o vice (decisão do Guilherme, 21/11/2026: "inclui tudo o que
# tiver"), como as edições sem jogos do uru-1 e do par-1. Não há página de 1965
# 1965 e 1990 (sem página da RSSSF) vêm da Wikipédia em português, que também traz parte dos jogos de vários anos
# (wikipedia_sp2.py)
SO_CLASSIFICACAO = {str(a) for a in (*range(1947, 1985), 1990, 1992, 1993, 1994)} - {"1979"}   # 1967-1984: achado A2-001
# observação da edição (vai para edicoes.csv)
OBS_EDICAO: dict[str, list[str]] = {
    "1983": ["o vice Noroeste perdeu o \"rebolo\" com o Taubaté, penúltimo da 1ª divisão (0-1 em 15/12 e 0-1 em 18/12/1983, "
             "em Campinas), e ficou na 2ª divisão; os jogos ficam fora (decisão D-04)"],
    "1972": ["a Wikipédia não tem a página desta edição: só a lista de participantes (RSSSF) e o pódio (predefinição de "
             "campeões da Wikipédia); a final São José x Garça (3-0 e 0-0) vem lá sem data nem mando e fica fora"],
    "1948": ["Sanjoanense licenciado (não jogou)"],
    "1954": ["2ª fase: a página traz também uma tabela calculada dos jogos (Taubaté 16 e Comercial 11 pontos); vale a "
             "classificação oficial (14 e 13)"],
    "1957": ["AD Araraquara abandonou na 10ª rodada; os jogos dele foram anulados"],
    "1988": ["69 jogos da 1ª fase vêm na fonte sem placar (só quem venceu) e ficam fora"],
    "1951": ["a repescagem XV de Jaú x Jabaquara (o último da 1ª divisão, três jogos) não é jogo da 2ª divisão e fica fora"],
    "1965": ["sem página da RSSSF: as tabelas dos dois grupos e a final vêm da Wikipédia em português"],
    "1989": ["jogos incompletos: a 1ª fase (RSSSF), as semifinais (Wikipédia) e a final (ogol); faltam a 2ª e a 3ª fase"],
    "1990": ["sem página da RSSSF: a Wikipédia em português traz a lista de participantes e só a 4ª fase (jogos e tabela); "
             "a ordem dos eliminados antes dela não é conhecida"],
    "1991": ["jogos incompletos: só a 2ª fase e o quadrangular final (a 1ª fase não está em nenhuma fonte); campeão o "
             "Araçatuba, pelo saldo de gols (a página da RSSSF diz \"Campeão: Lemense\" por engano; a lista de campeões, a "
             "Wikipédia e o Futebol Interior dão o Araçatuba)"],
    "1992": ["Capivariano inscrito, não disputou"],
    "1993": ["com a mudança das divisões da FPF, os clubes foram redistribuídos em 1994 (Série A2, A3 e B1)"],
    "1998": ["o XV de Piracicaba caiu, mas ficou na A2 de 1999 pelo licenciamento do Novorizontino (Wikipédia pt; A2-026)"],
    "2011": ["final XV de Piracicaba 2-2 Guarani: campeão o XV pela campanha (RSSSF); a Wikipédia dá 4-2 nos pênaltis "
             "(A2-028)"],
}
FORMATO_INCOMPLETO = {"1989", "1991"}


def temporadas_com_jogos() -> list[str]:
    """Temporadas com os jogos: página da RSSSF com jogos (fora as de SO_CLASSIFICACAO) ou calendário do ogol."""
    saida = []
    for t in ANOS:
        f = OGOL / f"sp2_{t}.json"
        n_ogol = len(json.loads(f.read_text(encoding="utf-8"))) if f.exists() else 0
        if t not in SO_CLASSIFICACAO and (rsssf_sp2.tem_pagina(t) or n_ogol >= 20):
            saida.append(t)
    return saida


def lider_ultima_fase(ano, partidas: list[Partida]) -> str | None:
    """O 1º pela soma dos jogos da fase do último jogo (pontos, vitórias, saldo, gols pró)."""
    com_data = [p for p in partidas if p.data and p.gm is not None]
    if not com_data:
        return None
    fase = max(com_data, key=lambda p: p.data).fase
    camp = campanha([p for p in partidas if p.fase == fase])
    pv = pontos_vitoria(ano)
    return max(camp, key=lambda c: (pv * camp[c][1] + camp[c][2], camp[c][1], camp[c][4] - camp[c][5], camp[c][4])) if camp else None


def vencedor_final(partidas: list[Partida]) -> str | None:
    final = [p for p in partidas if p.fase == "Final"]
    if not final:
        final = [p for p in partidas if p.fase == "Fase final"]
        if not final:
            return None
        camp = campanha(final)
        return max(camp, key=lambda c: (3 * camp[c][1] + camp[c][2], camp[c][4] - camp[c][5], camp[c][4]))
    gols, pen = Counter(), Counter()
    for p in final:
        gols[p.mandante] += p.gm or 0; gols[p.visitante] += p.gv or 0
        if p.pen_m is not None:
            pen[p.mandante] += p.pen_m; pen[p.visitante] += p.pen_v
    times = list(gols)
    if len(times) != 2:
        return None
    a, b = times
    if gols[a] != gols[b]:
        return a if gols[a] > gols[b] else b
    if pen[a] != pen[b]:
        return a if pen[a] > pen[b] else b
    return None


def motivo_divergencia(c: str, tabela: list, jogos: list | None, bloco: list[Partida]) -> str:
    """Por que a linha da tabela publicada não bate com os jogos do clube."""
    ps = [p for p in bloco if c in (p.mandante, p.visitante)]
    if jogos is None or not ps:
        return "o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)"
    if tabela[0] != jogos[0]:
        return f"a tabela conta {tabela[0]} jogos e as fontes trazem {jogos[0]}"
    sem_ogol = [p for p in ps if p.ogol_placar is None]
    difere = [p for p in ps if p.ogol_placar is not None and p.ogol_placar != (p.gm, p.gv)]
    if difere:
        p = difere[0]
        return (f"placar diverge entre RSSSF e ogol em {nome(p.mandante)} x {nome(p.visitante)} ({p.gm}-{p.gv} x "
                f"{p.ogol_placar[0]}-{p.ogol_placar[1]}) e nenhuma das versões fecha com a tabela; fica a RSSSF")
    if sem_ogol:
        return "há jogo do clube sem conferência no ogol"
    return "RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada"


def conferir(ano: int, partidas: list[Partida], tabs: list[tuple]) -> dict:
    """Cada tabela publicada pela RSSSF contra a soma dos jogos do pacote, do mesmo grupo (ou da edição inteira,
    na classificação geral)."""
    ok, dif, linhas_dif = 0, 0, []
    for tb, linhas, _ in tabs:
        if not linhas:
            continue
        # o bloco da tabela; a fase dela; cada fase (a "Standings" de 2015, no fim da página, é a da 1ª fase); a edição
        cands = [bloco_da_tabela(tb, partidas), [p for p in partidas if p.fase == tb.fase],
                 [p for p in partidas if p.linha and p.linha < tb.linha],   # tabela que soma os turnos de antes
                 *[[p for p in partidas if p.fase == f] for f in {p.fase for p in partidas}], partidas]
        melhor, bloco = None, []
        for bl in cands:
            camp = campanha(bl)
            e = [(c, v, camp.get(c)) for c, v in linhas.items() if camp.get(c) != v]
            if melhor is None or len(e) < len(melhor):
                melhor, bloco = e, bl
        if melhor:
            dif += 1
            linhas_dif += [f"{tb.fase} / {tb.grupo or '-'}: {nome(c)} tabela {v} jogos {x} — {motivo_divergencia(c, v, x, bloco)}"
                           for c, v, x in melhor]
        else:
            ok += 1
    return {"ok": ok, "dif": dif, "linhas": linhas_dif}


# --------------------------------------------------------------------------------------------- saída

# --------------------------------------------------------------------------------------------- edições sem os jogos

# grafias abreviadas das cidades nas tabelas antigas
CIDADES = {
    "Ara.": "Araraquara", "Bot.": "Botucatu", "B. Paulista": "Bragança Paulista", "Br. Paulista": "Bragança Paulista",
    "Birigüi": "Birigui", "E.S. do Pinhal": "Espírito Santo do Pinhal", "E.S.Pinhal": "Espírito Santo do Pinhal",
    "Esp.Sto.do Pinhal": "Espírito Santo do Pinhal", "Guará": "Guaratinguetá", "Jau": "Jaú", "Jundiai": "Jundiaí",
    "Monte Azul": "Monte Azul Paulista", "P. Prudente": "Presidente Prudente", "P.Prudente": "Presidente Prudente",
    "Pres. Prudente": "Presidente Prudente", "Pres.Prudente": "Presidente Prudente", "Pindamonhagaba": "Pindamonhangaba",
    "Rib. Preto": "Ribeirão Preto", "S. B. do Campo": "São Bernardo do Campo", "São Bernardo Campo": "São Bernardo do Campo",
    "S. Caetano do Sul": "São Caetano do Sul", "S.Caetano do Sul": "São Caetano do Sul", "São Caetano Sul": "São Caetano do Sul",
    "S. Carlos": "São Carlos", "S. J. da Barra": "São Joaquim da Barra", "S. J. da Boa Vista": "São João da Boa Vista",
    "S. João da Boa Vista": "São João da Boa Vista", "São J. da Boa Vista": "São João da Boa Vista",
    "S. J. do Rio Preto": "São José do Rio Preto", "S. José do R. Preto": "São José do Rio Preto",
    "S. José do Rio Preto": "São José do Rio Preto", "S.José do R.Preto": "São José do Rio Preto",
    "São J. do Rio Preto": "São José do Rio Preto", "São José Rio Preto": "São José do Rio Preto",
    "S. José do R Pardo": "São José do Rio Pardo", "S. José do R. Pardo": "São José do Rio Pardo",
    "S.José do R.Pardo": "São José do Rio Pardo", "S. José dos Campos": "São José dos Campos", "S. Paulo": "São Paulo",
    "S.Manuel": "São Manuel", "Sta. Cruz do Rio Pardo": "Santa Cruz do Rio Pardo", "Uchôa": "Uchoa", "Votuporan.": "Votuporanga",
    "São Bernardo do Campos": "São Bernardo do Campo", "São João da Rio Preto": "São José do Rio Preto", "Santa Bárbara D´Oeste": "Santa Bárbara d'Oeste",
    "Santa Bárbara D'Oeste": "Santa Bárbara d'Oeste", "São José Dos Campos": "São José dos Campos",
}
# (nome sem siglas, cidade da página) -> cidade certa: o CA Votorantim é de Votorantim (distrito de Sorocaba até 1963); o
# Catanduva EC de 1956 está "(Araçatuba)" por engano; a SE Irmãos Romano é de São Bernardo do Campo (1961-1966; em 1960,
# "Santo André")
CIDADE_DO_CLUBE = {("votorantim", "Sorocaba"): "Votorantim", ("catanduva", "Araçatuba"): "Catanduva",
                   ("irmaos romano", "Santo André"): "São Bernardo do Campo"}
# (temporada, grupo, nome) -> cidade certa de uma linha: em 1948 a Série Branca tem a Internacional de Bebedouro (Wikipédia);
# a página repete "(Limeira)", que é a da Série Preta
CIDADE_DA_LINHA = {("1948", "Série Branca", "AA Internacional"): "Bebedouro"}
# grafias erradas da página
NOME_CORRIGIDO = {"AA Riopardende": "AA Riopardense", "AA Rio Pardense": "AA Riopardense", "AA Potofelicense": "AA Portofelicense",
                  "São Joanense": "Sanjoanense", "SE Sãojoanense": "SE Sanjoanense", "EC Sâo Bento": "EC São Bento",
                  "S. Bento": "São Bento", "A.Brasil Clube": "Atlético Brasil Clube"}
# nome da página -> código, quando a cidade não separa (dois clubes da cidade com o mesmo nome) ou a ficha não tem cidade
MANUAL_ANTIGO = {"AD São Caetano": "2255",   # AD São Caetano (1989); o EC São Caetano (1914) é o 80977
                 "CA Bragantino": "red-bull-bragantino", "Bragantino": "red-bull-bragantino",   # a ficha não tem cidade
                 ("1994", "Catanduva"): "15767",   # "Catanduva EC is the new name of GE Catanduvense" (página de 1994)
                 ("1947", "XV Piracicaba"): "8229",   # 1947: a tabela não traz as cidades
                 ("1994", "São Caetano"): "2255",   # AD São Caetano (lista de participantes da página)
                 "Ferroviário Ituano": "2543",
                 # 1969-1971: Araçatuba FC (a AE Araçatuba, 19365, é de 1972); "Araçatuba" também casaria com o
                 # "São Paulo (Araçatuba)" do cadastro
                 ("1969", "Araçatuba"): "rs-aracatuba", ("1970", "Araçatuba"): "rs-aracatuba", ("1971", "Araçatuba"): "rs-aracatuba",
                 ("1971", "Esportiva"): "68360",   # Esportiva de Guaratinguetá (fora da lista de participantes da RSSSF)
                 ("1982", "Araçatuba"): "19365"}   # AE Araçatuba (fora da lista de participantes da RSSSF)   # Ferroviário Atlético Ituano (Itu) é o Ituano FC (1984; NOME_MANUAL de 1985-1989)
_SIGLA_INI = re.compile(r"^(?:(?:A|AA|AE|AD|EC|FC|CA|SE|GE|AC|SC|EA)\.?\s+|(?:A\.A\.|E\.C\.|C\.A\.|S\.E\.|A\.E\.|F\.C\.|A\.)\s*)")
_SIGLA_FIM = re.compile(r"\s+(?:FC|EC|AC|F\.C|E\.C|A\.C|de Esp\.? Atl[^\s]*|de E\.? ?A|Esp\. Atl[^\s]*|E\. Atl[^\s]*|de Esp\.?)\.?$")


def curto_antigo(n: str) -> str:
    """"EC XV de Novembro" -> "XV de Novembro"; "A Prudentina de Esp. Atl" -> "Prudentina"; "C.A.Linense" -> "Linense"."""
    for _ in range(2):
        n = _SIGLA_FIM.sub("", _SIGLA_INI.sub("", n.strip())).strip(" .")
    return n


def cidade_antiga(n: str, cidade: str | None) -> str | None:
    if not cidade:
        return None
    cidade = CIDADES.get(cidade, cidade)
    return CIDADE_DO_CLUBE.get((clubes_sp2.norm(curto_antigo(n)), cidade), cidade)


_LISTA: dict[str, list[tuple[str, str]]] = {}


def lista_participantes(ano: str) -> list[tuple[str, str]]:
    """[(nome, cidade)] do ano na lista de participantes da 2ª divisão da RSSSF (sp2list.htm: o ano numa linha, depois
    "Associação Atlética FRANCANA (Franca)", com o nome curto em maiúsculas)."""
    if not _LISTA:
        atual = None
        for l in rsssf.texto(0, "sp2list.htm").splitlines():
            if re.fullmatch(r"\s*(\d{4})\s*", l):
                atual = l.strip()
                _LISTA[atual] = []
            elif atual and (m := re.match(r"^\s*([^()]+?)\s*\(([^()]+)\)\s*$", l)):
                _LISTA[atual].append((m.group(1).strip(), m.group(2).strip()))
    return _LISTA.get(ano, [])


def cidade_na_lista(ano: str, n: str) -> str | None:
    """Cidade do clube na lista de participantes do ano (1947 e 1994: a tabela não traz a cidade)."""
    base = clubes_sp2.norm(curto_antigo(n))
    melhor = (0.0, None)
    for nome_l, cidade in lista_participantes(ano):
        caps = clubes_sp2.norm(" ".join(re.findall(r"\b[A-ZÀ-Ý][A-ZÀ-Ý\-]{1,}\b", nome_l)))
        s = max(_sim(base, caps) if caps else 0, _sim(base, clubes_sp2.norm(curto_antigo(nome_l))))
        if s > melhor[0]:
            melhor = (s, cidade)
    return melhor[1] if melhor[0] >= 0.75 else None


# (temporada, nome na página) -> nome da 1ª fase da mesma página, quando o nome curto das fases seguintes não basta
NOME_ANTIGO: dict[tuple[str, str], str] = {
    ("1963", "Port. Santista"): "AA Portuguesa", ("1963", "Corinthians-PP"): "EC Corinthians", ("1963", "São Bento-M"): "AA São Bento",
    ("1963", "Estrada"): "Estrada de Ferro Sorocabana FC", ("1964", "Estrada"): "Estrada de Ferro Sorocabana FC",
}


def ficha_antiga(ano: str, base: str, cidade: str | None) -> str | None:
    """A ficha do ogol (A2 e A1) da mesma cidade, de clube que já existia, com nome igual ou quase (sem as siglas) ou que
    contém o nome da página ("XV de Novembro" em "Esporte Clube XV de Novembro"); só quando é uma."""
    fs = clubes_sp2.fichas()
    c, nb = clubes_sp2.norm(cidade or ""), clubes_sp2.norm(base)
    if not c or not nb:
        return None
    cands = []
    for k, f in fs.items():
        if k.startswith("rs-") or not f.get("cidade") or fundado_depois(k, ano, fs) or re.search(r"\s(?:II|B|Sub-?\d+)$", f.get("curto") or ""):
            continue
        cf = clubes_sp2.norm(f["cidade"])
        if not (cf == c or cf.startswith(c + " ") or c.startswith(cf + " ")):
            continue
        nomes = [clubes_sp2.norm(x) for x in (f.get("curto"), *f.get("nomes_ogol", []), f.get("nome_completo")) if x]
        nomes += [clubes_sp2.norm(curto_antigo(x)) for x in (f.get("curto"), *f.get("nomes_ogol", []), f.get("nome_completo")) if x]
        s = max(_sim(nb, x) for x in nomes)
        if len(nb) >= 4 and any(re.search(rf"\b{re.escape(nb)}\b", x) for x in nomes):
            s = max(s, 0.85)
        if s >= 0.8:
            cands.append((s, k))
    cands.sort(reverse=True)
    return cands[0][1] if cands and (len(cands) == 1 or cands[1][0] < cands[0][0]) else None


def casar_antigo(ano: str, n: str, cidade: str | None, log: list[str]) -> str:
    """Clube de uma linha de tabela com a cidade (1ª fase das edições sem os jogos): a ficha do ogol da mesma cidade
    (ficha_antiga); senão o clube só da RSSSF da mesma cidade e nome parecido (deste pacote ou do cadastro comum); senão um
    clube novo "rs-<nome>-<cidade>"."""
    if (ano, n) in MANUAL_ANTIGO or n in MANUAL_ANTIGO:
        i = MANUAL_ANTIGO.get((ano, n)) or MANUAL_ANTIGO[n]
        if i.startswith("rs-") and i not in clubes_sp2.SEM_OGOL:   # clube só da RSSSF do cadastro comum
            import registro
            r = registro.ler()[i]
            clubes_sp2.SEM_OGOL[i] = {"id": i, "curto": r["clube"], "nomes_ogol": [], "uf": "SP", "cidade": r.get("cidade"),
                                      "nome_completo": None}
            clubes_sp2.fichas.cache_clear()
            clubes_sp2.exibicao.cache_clear()
        return i
    base = curto_antigo(n)
    i = ficha_antiga(ano, base, cidade)
    if i:
        return i
    if not cidade:   # sem a cidade (1947, 1994): a ficha de nome curto igual ao da página, quando é uma só e já existia
        fs = clubes_sp2.fichas()
        iguais = [k for k, f in fs.items() if not k.startswith("rs-") and clubes_sp2.norm(f.get("curto") or "") == clubes_sp2.norm(base)
                  and not fundado_depois(k, ano, fs)]
        if len(iguais) == 1:
            return iguais[0]
    c = clubes_sp2.norm(cidade or "")
    import registro
    ja = {**{k: {"curto": r["clube"], "cidade": r.get("cidade")} for k, r in registro.ler().items() if k.startswith("rs-")},
          **clubes_sp2.SEM_OGOL}
    parecido = lambda x: (_sim(base, x) >= 0.8 or clubes_sp2.norm(base) in clubes_sp2.norm(x) or clubes_sp2.norm(x) in clubes_sp2.norm(base))
    iguais = sorted({k for k, f in ja.items() if c and clubes_sp2.norm(f.get("cidade") or "") == c and parecido(f["curto"])})
    if len(iguais) == 1:
        if iguais[0] not in clubes_sp2.SEM_OGOL:   # clube do cadastro comum: volta a ser conhecido nesta coleta
            clubes_sp2.SEM_OGOL[iguais[0]] = {"id": iguais[0], "curto": ja[iguais[0]]["curto"], "nomes_ogol": [], "uf": "SP",
                                              "cidade": ja[iguais[0]]["cidade"], "nome_completo": None}
            clubes_sp2.fichas.cache_clear()
            clubes_sp2.exibicao.cache_clear()
        return iguais[0]
    i = clubes_sp2.sem_ogol(base, cidade)
    log.append(f"{ano}: {n} ({cidade}) — clube que o ogol não tem; entra só pela RSSSF")
    return i


def casar_fase_seguinte(ano: str, n: str, cidade: str | None, anteriores: list[tuple[str, str, bool]]) -> str | None:
    """Nome curto das fases seguintes ("Linense", "Ferroviária (Bot.)", "São Bento (Marília)") -> clube da 1ª fase:
    o de nome mais parecido (da mesma cidade, quando a página dá), comparando também com o nome de exibição ("XV de Jaú"),
    de preferência um classificado."""
    alvo = NOME_ANTIGO.get((ano, n))
    melhor = (0.0, None)
    b = clubes_sp2.norm(curto_antigo(n))
    for nome_1, cid, classificado in anteriores:
        ex = clubes_sp2.exibicao().get(cid, {})
        if alvo:
            s = 2.0 if nome_1 == alvo else 0
        else:
            if cidade and clubes_sp2.norm(ex.get("cidade") or clubes_sp2.fichas().get(cid, {}).get("cidade") or "") != clubes_sp2.norm(cidade):
                continue
            s = 0.0
            for x in (curto_antigo(nome_1), ex.get("clube") or ""):
                b1 = clubes_sp2.norm(x)
                s = max(s, _sim(b, b1), 0.9 if b and b1 and (b1.startswith(b) or b.startswith(b1)) else 0)
            s += 0.05 if classificado else 0
        if s > melhor[0]:
            melhor = (s, cid)
    return melhor[1] if melhor[0] >= 0.6 else None


def montar_antiga(ano: str, log: list[str], rs_c: dict, wk_c: dict) -> dict:
    """Edição sem os jogos: tabelas publicadas, clubes e classificação final (campeão, vice, depois a fase alcançada e os
    pontos da última fase). Mesmo dicionário de montar_edicao, sem partidas. Cada linha guarda o código do clube em
    "clube_id" (a mesma tabela pode ter dois "AA Ferroviária", de Botucatu e de Assis)."""
    import antigas_sp2
    tbs = antigas_sp2.tabelas(ano)
    anteriores: list[tuple[str, str, bool]] = []
    tabs = []
    for tb in tbs:
        nome_id = {}
        for r in tb.linhas:
            nome_pag = NOME_CORRIGIDO.get(r["nome"], r["nome"])
            cidade = cidade_antiga(nome_pag, CIDADE_DA_LINHA.get((ano, tb.grupo, r["nome"]), r["cidade"]))
            primeira = tb.fase in ("Primeira fase", "Classificação final")
            if primeira and not cidade:
                cidade = cidade_antiga(nome_pag, cidade_na_lista(ano, nome_pag) or cidade_na_pagina(ano, nome_pag))
            cid = (casar_antigo(ano, nome_pag, cidade, log) if primeira or not anteriores
                   else casar_fase_seguinte(ano, nome_pag, cidade, anteriores))
            if not cid:
                log.append(f"{ano}: {r['nome']} ({tb.fase} {tb.grupo}) — sem clube da 1ª fase com esse nome")
                cid = casar_antigo(ano, nome_pag, cidade, log)
            r["clube_id"] = cid
            nome_id.setdefault(r["nome"], cid)
            r.setdefault("obs", r.get("nota") or "")
            for k in ("j", "v", "e", "d", "gp", "gc"):
                r.setdefault(k, None)
            if primeira:
                anteriores.append((nome_pag, cid, bool(re.search(r"qualif|classif", r.get("nota") or ""))))
        tabs.append((tb, {r["clube_id"]: r for r in tb.linhas}, nome_id))
    mapa = {(r["nome"], tb.fase, tb.grupo): r["clube_id"] for tb in tbs for r in tb.linhas}
    todos = [(NOME_CORRIGIDO.get(r["nome"], r["nome"]), r["clube_id"], bool(re.search(r"qualif|classif", r.get("nota") or "")))
             for tb in tbs for r in tb.linhas]
    partidas = jogos_wikipedia_antiga(ano, todos, log)
    final, campeao = classificacao_antiga(ano, tbs, rs_c, wk_c, log, partidas)
    import wikipedia_sp2
    so_ordem = tbs and tbs[0].fase == "Classificação final"
    publicadas = [tb for tb in tbs if tb.publicada]
    tabela = ("a ordem final" if so_ordem else "a lista de participantes e o pódio" if not publicadas
              else "a tabela final" if len(publicadas) == 1 else "os pontos de cada fase")
    obs = list(OBS_EDICAO.get(ano, []))
    if ano in antigas_sp2.NOVAS:
        obs.append("sem os jogos na RSSSF: participantes da lista da RSSSF (sp2list.htm), tabelas e jogos da página da "
                   "Wikipédia em português e vice, 3º e 4º da predefinição de campeões da Wikipédia (achado A2-001)")
    if partidas:
        fases = ", ".join(f.lower() for f in sorted({p.fase for p in partidas}, key=lambda f: ORDEM.get(f, 0)))
        formato = f"jogos incompletos ({tabela} e {len(partidas)} {'jogo' if len(partidas) == 1 else 'jogos'}: {fases})"
        n_sem = wikipedia_sp2.sem_placar(ano)
        obs.append(f"{len(partidas)} {'jogo' if len(partidas) == 1 else 'jogos'} da Wikipédia em português ({fases})"
                   + (f"; outros {n_sem} vêm lá só com o resultado e ficam fora" if n_sem else ""))
    else:
        formato = f"sem jogos (só {tabela})"
    da_wiki = all(tb.fonte.startswith("Wikipédia") for tb in tbs)
    return {"tabs_antigas": tbs, "tabs": tabs, "partidas": partidas, "mapa": mapa, "og": [], "rs": [] if da_wiki else tbs,
            "final": final, "campeao": campeao, "conf": conferir_antiga(ano, tbs, partidas), "ajustes": {}, "formato": formato,
            "num_clubes": len(final), "obs": obs, "sem_rodada": True}


# fase da tabela -> ordem (fase alcançada)
ORDEM_ANTIGA = {"Primeira fase": 1, "Segunda fase": 2, "Quarta fase": 4, "Fase final": 9, "Classificação final": 1}
# (temporada, nome na Wikipédia) -> código, quando o nome não separa dois clubes da edição
NOME_WIKI = {("1959", "AA São Bento"): "rs-sao-bento-marilia", ("1959", "São Bento"): "3457", ("1962", "São Bento"): "3457",
             ("1963", "AA São Bento"): "rs-sao-bento-marilia", ("1966", "Ferroviária"): "15766"}


def jogos_wikipedia_antiga(ano: str, todos: list[tuple[str, str, bool]], log: list[str]) -> list[Partida]:
    """Jogos da Wikipédia de uma edição sem os jogos na RSSSF, com os clubes casados aos das tabelas."""
    import wikipedia_sp2
    saida = []
    for j in wikipedia_sp2.jogos(ano):
        m = NOME_WIKI.get((ano, j["mandante"])) or casar_fase_seguinte(ano, j["mandante"], None, todos)
        v = NOME_WIKI.get((ano, j["visitante"])) or casar_fase_seguinte(ano, j["visitante"], None, todos)
        if not (m and v) or m == v:
            log.append(f"{ano}: jogo da Wikipédia sem os clubes nas tabelas, fica de fora: {j['mandante']} {j['gm']}-{j['gv']} {j['visitante']}")
            continue
        saida.append(Partida(ano, j["fase"], j["grupo"], None, j["data"], m, v, j["gm"], j["gv"], fonte="Wikipédia (pt)",
                             fonte_id=f"wikipedia:pt_{ano}:{j['linha']}", obs=j["nota"], linha=j["linha"]))
    return saida


def conferir_antiga(ano: str, tbs: list, partidas: list[Partida]) -> dict:
    """Tabela publicada x jogos da Wikipédia, só nas fases e grupos com todos os jogos (turno e returno, ou turno único):
    os pontos de cada clube (2 por vitória)."""
    conf = {"ok": 0, "dif": 0, "linhas": []}
    for tb in tbs:
        if not tb.publicada:
            continue
        ids = {r["clube_id"] for r in tb.linhas}
        ps = [p for p in partidas if p.fase == tb.fase and {p.mandante, p.visitante} <= ids]
        n = len(ids)
        if not ps or len(ps) not in (n * (n - 1), n * (n - 1) // 2):
            continue
        camp = campanha(ps)
        pts = lambda c: 2 * camp[c][1] + camp[c][2]
        difs = [f"{nome(r['clube_id'])}: tabela {r['pts']} pts, jogos {pts(r['clube_id'])}"
                for r in tb.linhas if r["pts"] is not None and r["pts"] != pts(r["clube_id"])]
        if difs:
            conf["dif"] += 1
            conf["linhas"].append(f"{tb.fase}{' ' + tb.grupo if tb.grupo else ''} — " + "; ".join(difs))
        else:
            conf["ok"] += 1
    return conf
# temporada -> o vice, quando a regra (o outro finalista) não basta
VICE_ANTIGO: dict[str, str] = {}
# nome do pódio da predefinição da Wikipédia -> nome que casa com o da edição
NOME_PODIO = {"Red Bull Bragantino": "Bragantino", "EC Corinthians": "Corinthians", "Aliança Clube": "Aliança"}


def classificacao_antiga(ano: str, tbs: list, rs_c: dict, wk_c: dict, log: list[str],
                        partidas: list | None = None) -> tuple[list[dict], str | None]:
    """Classificação final de uma edição sem os jogos. O campeão é o da lista da RSSSF; o vice é o outro finalista: o 1º de
    outro grupo da última fase (quando ela tem grupos) ou o melhor da tabela única da última fase. Depois, a fase alcançada
    e, dentro dela, a posição no grupo e os pontos da última fase. Os pontos de cada fase vão na observação; a linha só tem
    os pontos (e V/E/D) quando a edição tem uma tabela só. 1992 e 1993: a ordem da página, com as faixas empatadas."""
    linhas_de: dict[str, list[tuple[object, dict]]] = defaultdict(list)
    for tb in tbs:
        for r in tb.linhas:
            if r.get("nota") == "licensed":   # licenciado: não jogou
                continue
            linhas_de[r["clube_id"]].append((tb, r))
    ids = set(linhas_de)
    campeao = campeao_oficial(ano, [], rs_c, wk_c, ids=ids)
    if not campeao:
        log.append(f"{ano}: campeão da RSSSF ({rs_c.get(ano, '-')}) sem clube nas tabelas")
    def ultima(c):
        return max(linhas_de[c], key=lambda x: ORDEM_ANTIGA.get(x[0].fase, 0))
    # fase alcançada: a da tabela ou a dos jogos (1970, 1980: semifinal e final só nos jogos da Wikipédia)
    alcance = {c: max(ORDEM_ANTIGA.get(tb.fase, 0) for tb, _ in linhas_de[c]) for c in ids}
    for p in partidas or []:
        for c in (p.mandante, p.visitante):
            if c in alcance:
                alcance[c] = max(alcance[c], ORDEM.get(p.fase, 0))
    ordem_max = max(ORDEM_ANTIGA.get(tb.fase, 0) for tb in tbs)
    ult = [tb for tb in tbs if ORDEM_ANTIGA.get(tb.fase, 0) == ordem_max]
    vice = VICE_ANTIGO.get(ano)
    # 1967-1984: o pódio da predefinição de campeões da Wikipédia (vice, 3º e 4º; achado A2-001)
    import antigas_sp2
    import wikipedia_sp2
    podio_rank: dict[str, int] = {}
    if ano in antigas_sp2.NOVAS:
        pod = wikipedia_sp2.podio(ano)
        todos = [(r["nome"], r["clube_id"], False) for tb in tbs for r in tb.linhas]
        for rank, nomes in ((2, [pod.get("vice")]), (3, pod.get("terceiro", [])), (4, pod.get("quarto", []))):
            for n in nomes:
                cid = n and casar_fase_seguinte(ano, NOME_PODIO.get(n, n), None, todos)
                if n and not cid:
                    raise ValueError(f"{ano}: clube do pódio da Wikipédia sem clube na edição: {n}")
                if cid and cid != campeao:
                    podio_rank.setdefault(cid, rank)
        vice = vice or next((c for c, k in podio_rank.items() if k == 2), None)
        # 3º e 4º da predefinição só para quem chegou à fase mais avançada dos outros clubes (1980: o 4º da predefinição,
        # Ginásio Pinhalense, não jogou a semifinal)
        topo = max((alcance[c] for c in ids if c not in (campeao, vice)), default=0)
        for c in [c for c, k in podio_rank.items() if k > 2 and alcance.get(c, 0) < topo]:
            log.append(f"{ano}: {nome(c)} é {podio_rank[c]}º na predefinição da Wikipédia, mas não chegou à fase final; "
                       "fica pela fase alcançada")
            del podio_rank[c]
    if not vice and ult[0].fase != "Classificação final":
        if len(ult) > 1:
            lideres = [min(tb.linhas, key=lambda r: r["pos"])["clube_id"] for tb in ult]
            outros = [c for c in lideres if c != campeao]
            vice = outros[0] if len(outros) == 1 else None
        else:
            outros = sorted((r for r in ult[0].linhas if r["clube_id"] != campeao), key=lambda r: (r["pos"], -(r["pts"] or 0)))
            vice = outros[0]["clube_id"] if outros else None
    def chave(c):
        tb, r = ultima(c)
        abandonou = r.get("nota") == "abandoned"
        return (c != campeao, c != vice, -alcance[c], podio_rank.get(c, 9), abandonou, -ORDEM_ANTIGA.get(tb.fase, 0),
                r["pos"] or 99, -(r["pts"] or 0), nome(c))
    ordem = sorted(ids, key=chave)
    so_ordem = ult[0].fase == "Classificação final"
    uma_tabela = len(tbs) == 1
    fase_pt = {"Primeira fase": "1ª fase", "Segunda fase": "2ª fase", "Quarta fase": "4ª fase", "Fase final": "fase final"}
    saida = []
    for i, c in enumerate(ordem, 1):
        tb, r = ultima(c)
        partes = []
        if so_ordem:
            pos = r["pos"]
            if r.get("faixa"):
                fim = r["pos"] + sum(1 for x in tb.linhas if x["pos"] == r["pos"]) - 1
                partes.append(f"entre o {r['pos']}º e o {fim}º lugar (a página não dá a ordem dentro da faixa)")
            if r.get("nota"):
                partes.append(r["nota"])
        elif c in (campeao, vice) or c in podio_rank:   # pódio da predefinição, sem tabela da fase
            pos = i
            partes.append("posição pela predefinição de campeões da Wikipédia")
        elif r["pos"] is None:   # 1990: a página só lista os participantes eliminados antes da última fase
            pos = sum(1 for x in ordem if ultima(x)[1]["pos"] is not None or x in (campeao, vice) or x in podio_rank) + 1
            if ult[0].publicada:
                partes.append(f"eliminado antes da {fase_pt.get(ult[0].fase, ult[0].fase.lower())}; a página não dá a ordem")
            else:   # 1970, 1972-1975: só a lista de participantes e o pódio
                partes.append("a fonte não dá a ordem dos clubes fora do pódio")
        else:
            pos = i
            if not uma_tabela:
                for tb2, r2 in sorted(linhas_de[c], key=lambda x: ORDEM_ANTIGA.get(x[0].fase, 0)):
                    if r2["pos"] is None:
                        continue
                    rotulo = fase_pt.get(tb2.fase, tb2.fase) + (f" ({tb2.grupo})" if tb2.grupo else "")
                    partes.append(f"{rotulo}: {r2['pos']}º" + (f", {r2['pts']} pts" if r2["pts"] is not None else ""))
            if r.get("nota") == "abandoned":
                partes.append("abandonou o campeonato (jogos anulados)")
        cheia = uma_tabela and not so_ordem
        saida.append({"pos": pos, "clube": c, "j": r.get("j") if cheia else None, "v": r.get("v") if cheia else None,
                      "e": r.get("e") if cheia else None, "d": r.get("d") if cheia else None, "gp": r.get("gp") if cheia else None,
                      "gc": r.get("gc") if cheia else None, "pts": r["pts"] if cheia else None, "ajuste": 0,
                      "fonte": f"{tb.fonte} (" + ("ordem final publicada" if so_ordem else "tabela final publicada" if uma_tabela
                                                    else "tabelas de pontos: fase alcançada, posição e pontos da última fase") + ")",
                      "obs": "; ".join(partes), "rebaixado": bool(re.search(r"relegated|rebaixad", r.get("nota") or "", re.I))})
    return saida, campeao


def main(anos: list[int], gravar: bool) -> None:
    log: list[str] = []
    rs_c, wk_c = campeoes()
    edicoes = {}
    for ano in anos:
        if ano in SO_CLASSIFICACAO:
            e = montar_antiga(ano, log, rs_c, wk_c)
            edicoes[ano] = e
            print(f"{ano}: {len(e['partidas'])} jogos (Wikipédia), {len(e['final'])} clubes, {len(e['tabs'])} tabelas (ok {e['conf']['ok']} / div. {e['conf']['dif']}), campeão "
                  f"{nome(e['campeao']) if e['campeao'] else '?'}, vice {next((nome(f['clube']) for f in e['final'] if f['pos'] == 2), '-')} "
                  f"(RSSSF: {rs_c.get(ano, '-')})", flush=True)
            continue
        e = montar_edicao(ano, log, rs_c, wk_c)
        e.setdefault("obs", []).extend(OBS_EDICAO.get(ano, []))
        edicoes[ano] = e
        ps = e["partidas"]
        print(f"{ano}: {len(ps)} jogos (RSSSF {len(e['rs'])}, ogol {len(e['og'])}), tabelas ok {e['conf']['ok']} / divergentes "
              f"{e['conf']['dif']}, gols c/ autor {sum(len(p.gols) for p in ps)} de {sum((p.gm or 0) + (p.gv or 0) for p in ps)}, "
              f"campeão {nome(e['campeao']) if e['campeao'] else '?'} (RSSSF: {rs_c.get(ano, '-')}; Wikipédia: {wk_c.get(ano, '-')})", flush=True)
        if len(anos) == 1:
            for l in e["conf"]["linhas"]:
                print("   !", l)
    if len(anos) == 1:
        for l in log:
            print("   ", l)
    if gravar:
        import pacote
        pacote.gravar(edicoes, log, rs_c, wk_c)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    anos = [a for a in sys.argv[1:] if a[:4].isdigit()]
    main(anos or sorted(set(temporadas_com_jogos()) | SO_CLASSIFICACAO), gravar=not anos)
