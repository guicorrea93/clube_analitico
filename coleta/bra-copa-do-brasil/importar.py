"""Junta as fontes da Copa do Brasil (mesmo método da Série C) e grava o pacote em data/coleta/bra-copa-do-brasil/pacote/ e o relatório em docs/coleta/bra-copa-do-brasil.md.

Fontes, na ordem em que entram:
- RSSSF Brasil (rsssf_cb.py): base de jogos, fases, grupos, rodadas, datas e autores dos gols; as tabelas publicadas
  servem de conferência.
- ogol (baixar_ogol.py): calendário completo de todas as edições, com o código de cada clube (identidade). Confere
  o placar e completa os jogos que faltam na RSSSF.
- ESPN: não tem jogos da Copa do Brasil (a liga bra.4 vem vazia); o código fica, sem uso.
- Wikipédia: punições de pontos (adjust_points) e a lista de campeões (segunda fonte do campeão).

Placar diferente entre RSSSF e ogol: fica o que fecha com a tabela publicada pela RSSSF (os dois clubes);
sem tabela para decidir, fica o da RSSSF. Tudo fica registrado no relatório.

Uso: python coleta/bra-copa-do-brasil/importar.py [ano ...]     (sem ano: todas as edições; com ano, só confere e não grava)
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
import clubes_cb  # noqa: E402
import gols as gols_rsssf  # noqa: E402
from observacao import penaltis_da_nota  # noqa: E402
import rsssf_cb  # noqa: E402
import wiki  # noqa: E402
from edicoes import ANOS, NOME_OFICIAL, NOME_PADRAO, PACOTE, PASTA_DADOS, RELATORIO, SLUG  # noqa: E402
from rsssf_cb import rsssf  # noqa: E402

wiki.PASTA = PASTA_DADOS / "wikipedia"
OGOL = PASTA_DADOS / "ogol"
ESPN = PASTA_DADOS / "espn"
FONTE_RSSSF = "https://rsssfbrasil.com/tablesae/cbr{ano}.htm"


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
    a, b = clubes_cb.chave(a), clubes_cb.chave(b)
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
CORRIGE_OGOL: dict[tuple[int, str], tuple[str, str]] = {
    (2007, "3374"): ("36613", "o Operário de 2007 é o Operário de Várzea Grande (CEOV), campeão mato-grossense de 2006; o ogol "
                              "põe o Operário-MS (revisão CL-003)"),
}


def ler_ogol(ano: int) -> list[dict]:
    f = OGOL / f"copa_brasil_{ano}.json"
    js = json.loads(f.read_text(encoding="utf-8")) if f.exists() else []
    for o in js:
        for lado in ("mandante", "visitante"):
            if (ano, o.get(f"{lado}_id")) in CORRIGE_OGOL:
                o[f"{lado}_id"] = CORRIGE_OGOL[(ano, o[f"{lado}_id"])][0]
    return [o for o in js if o["id"] not in OGOL_IGNORAR]


def nomes_ogol(ano: int, og: list[dict]) -> dict[str, set[str]]:
    """Código do clube -> nomes que o ogol usa para ele (no calendário do ano e na ficha)."""
    fs = clubes_cb.fichas()
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
NOME_MANUAL: dict[tuple[int, str], tuple[str, str]] = {
    (1991, "Fluminense(BA)"): ("3247", "Fluminense de Feira; o Grêmio venceu ele e o Auto Esporte pelos mesmos placares (1-0 e 2-0), "
                                       "e o casamento pelo placar confundia os dois"),
    (1996, "Linhares"): ("20122", "Linhares EC, o de 1996 (o Linhares FC é dos anos 2000)"),
    (2003, "CF Amazônia"): ("3190", "Clube de Futebol Amazônia, o 'CFA' de Porto Velho no ogol"),
    (2011, "Prudente (SP)"): ("5229", "Grêmio Prudente, nome do Grêmio Barueri em 2010-2011 (hoje 'Barueri' no banco)"),
    (2013, "Resende (PA)"): ("12036", "erro da RSSSF: é o Resende (RJ), como no ogol (jogos contra o Caxias)"),
    (2013, "Betim"): ("3297", "Betim Esporte Clube, ex-Ipatinga (o mesmo clube no ogol)"),
    (2017, "Sete de Setembro"): ("15589", "7 de Setembro de Dourados (MS), como no ogol"),
    (2018, "Tubarão"): ("15723", "Atlético Tubarão (SC), como no ogol"),
    (2023, "Mutum-MT"): ("240425", "Nova Mutum (MT), como no ogol"),
    (2007, "Operário(MT)"): ("36613", "CE Operário Várzea-grandense, como nos participantes da RSSSF (revisão CL-003)"),
}
# jogos do calendário do ogol que estão errados (a RSSSF e a tabela publicada mostram outro jogo): código do jogo -> motivo
OGOL_IGNORAR: dict[str, str] = {}
# jogos da RSSSF que ficam de fora: (ano, nome do clube) -> motivo
RSSSF_FORA: dict[tuple[int, str], str] = {}
# jogos da RSSSF anulados: (ano, mandante, visitante, gols, gols) como na página -> motivo
JOGOS_ANULADOS: dict[tuple, str] = {
    (2007, "Rio Branco(PR)", "Villa Nova(MG)", 3, 0): "erro da página: na 2ª fase o Villa Nova enfrentou o Avaí (revisão CB-007)",
    (2019, "Aparecidense/GO", "Ponte Preta/SP", 1, 0): "jogo anulado pelo STJD; vale o 2-0 de 03/04 (revisão CB-007)",
}
# jogo da página com clube ou placar errado: (ano, mandante, visitante, data da página) -> (mandante, visitante, gols, gols, motivo)
PLACAR_MANUAL: dict[tuple, tuple] = {
    (2021, "CRB-AL", "Cuiabá-MT", "2021-03-16"): ("Sergipe-SE", "Cuiabá-MT", 0, 0, "o jogo foi Sergipe 0-0 Cuiabá, como no ogol; o "
                                                   "CRB jogou a 1ª fase com o Goianésia (revisão CB-007)"),
}
# correções de jogos já juntados (nomes de exibição e data do pacote) -> campos novos e motivo
_UM_DIA = "o ogol dá o dia seguinte (jogo à noite no Brasil); data da Wikipédia pt e en (revisão CB-010)"
CORRECAO_JOGO: dict[tuple, dict] = {
    (1990, "Goiás", "Flamengo", "1990-11-08"): {"data": "1990-11-07", "motivo": _UM_DIA},
    (2014, "Atlético-MG", "Cruzeiro", "2014-11-13"): {"data": "2014-11-12", "motivo": _UM_DIA},
    (2014, "Cruzeiro", "Atlético-MG", "2014-11-27"): {"data": "2014-11-26", "motivo": _UM_DIA},
    (2015, "Santos", "Palmeiras", "2015-11-26"): {"data": "2015-11-25", "motivo": _UM_DIA},
    (2015, "Palmeiras", "Santos", "2015-12-03"): {"data": "2015-12-02", "motivo": _UM_DIA},
}


def mapear_nomes(ano: int, rs: list, og: list[dict], log: list[str]) -> dict:
    """Nome na RSSSF -> código do ogol, por grupo: a mesma página às vezes usa o mesmo nome curto para clubes
    diferentes em grupos diferentes ("Esportivo" de Bento Gonçalves e de Passos em 1988).
    Cada jogo da RSSSF vota nos jogos do ogol de mesmo placar e data próxima (o voto pesa mais quando os nomes
    parecem); depois, dentro de cada grupo, um para um, do par mais votado para o menos.
    Devolve chaves (nome, fase, grupo) e, para as tabelas gerais, o nome sozinho."""
    noms = nomes_ogol(ano, og)
    fs = clubes_cb.fichas()
    cache: dict[tuple, float] = {}
    def sim(n, i):
        """Parecença do nome; a UF escrita no nome da RSSSF ("São José(RS)") desempata homônimos."""
        if (n, i) not in cache:
            s = max((_sim(n, x) for x in noms.get(i, ()) if x), default=0)
            uf_n, uf_i = clubes_cb.separar_uf(n.replace("(", " (").strip())[1], fs.get(i, {}).get("uf")
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
    for n in sem:
        log.append(f"{ano}: nome da RSSSF sem clube no ogol (jogos dele ficam de fora): {n}")
    return saida


def penaltis(nota: str) -> tuple[int | None, int | None]:
    m = re.search(r"(?:pen(?:alties|altis)?|on penalties|nos pênaltis)\D{0,4}(\d{1,2})\s*[-x]\s*(\d{1,2})|(\d{1,2})-(\d{1,2}) on penalties", nota or "", re.I)
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
                    estadio=j.estadio or None, publico=j.publico, fonte=FONTE_RSSSF.format(ano=ano), gols_texto=j.gols, obs=j.nota, linha=j.linha)
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
    # antes: o mesmo jogo com o mando invertido, no mesmo dia (±1) e com o placar espelhado. A RSSSF da Copa escreve o
    # confronto do ponto de vista de um dos clubes, nem sempre o mandante (finais de 2015 e 2016): vale o mando do ogol
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
        log.append(f"{ano}: mando da RSSSF trocado pelo do ogol (mesmo jogo, mesmo dia, placar espelhado) — RSSSF "
                   f"{nome(p.mandante)} {p.gm}-{p.gv} {nome(p.visitante)}, ogol {nome(o['mandante_id'])} "
                   f"{o['gols_mandante']}-{o['gols_visitante']} {nome(o['visitante_id'])} ({o['data']})")
        p.mandante, p.visitante, p.gm, p.gv = p.visitante, p.mandante, p.gv, p.gm
        p.pen_m, p.pen_v = p.pen_v, p.pen_m
        p.gols = [{**g, "lado": "visitante" if g.get("lado") == "mandante" else "mandante"} for g in p.gols]
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
                # Copa (mata-mata, sem tabela que desempate): fica o do ogol. A revisão (CB-004, CB-005) conferiu 10 desses
                # casos na Wikipédia, e em todos o certo era o do ogol; vários placares da página repetem o do outro jogo
                log.append(f"{ano}: placar diferente no ogol — {nome(p.mandante)} x {nome(p.visitante)} ({p.data}): "
                           f"RSSSF {p.gm}-{p.gv}, ogol {alt[0]}-{alt[1]}; fica o do ogol")
                p.obs = (p.obs + "; " if p.obs else "") + f"placar da RSSSF {p.gm}-{p.gv}; vale o do ogol"
                p.gm, p.gv = alt
                lados = (sum(g["lado"] == "mandante" for g in p.gols), sum(g["lado"] == "visitante" for g in p.gols))
                if p.gols and lados != (p.gm, p.gv):   # os autores da página são do placar antigo
                    p.gols = []
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
        # mando invertido com o placar espelhado: até 10 dias (2016: a RSSSF dá a volta da final em 30/11, o ogol em 07/12)
        inv = [p for p in sobra if (p.mandante, p.visitante) == (v, m) and (p.gm, p.gv) == (gv, gm) and _dist(p.data, o["data"]) <= 10]
        inv_placar = [p for p in sobra if (p.mandante, p.visitante) == (v, m) and perto(p)]
        mesmo_par = [p for p in sobra if (p.mandante, p.visitante) == (m, v) and perto(p)]
        outro = [p for p in sobra if perto(p) and (p.gm, p.gv) == (gm, gv) and (p.mandante == m) != (p.visitante == v)]
        for lista, texto in ((inv, "mando invertido"), (inv_placar, "mando invertido e placar diferente"),
                             (mesmo_par, "placar diferente (jogo não achado pela data)"), (outro, "adversário diferente")):
            if len(lista) == 1:
                p = lista[0]
                usados.add(o["id"]); sobra.remove(p)
                p.fonte_id = f"ogol:{o['id']}"
                p.hora = p.hora or o.get("hora")
                if texto == "mando invertido":   # o mesmo jogo: vale o mando e a data do ogol (a RSSSF da Copa não marca o mandante)
                    log.append(f"{ano}: {texto} no ogol — RSSSF {nome(p.mandante)} {p.gm}-{p.gv} {nome(p.visitante)} ({p.data}), ogol "
                               f"{nome(m)} {gm}-{gv} {nome(v)} ({o['data']}); fica o ogol")
                    p.mandante, p.visitante, p.gm, p.gv, p.pen_m, p.pen_v = m, v, gm, gv, p.pen_v, p.pen_m
                    p.gols = [{**g, "lado": "visitante" if g.get("lado") == "mandante" else "mandante"} for g in p.gols]
                    p.data = o["data"]
                    break
                log.append(f"{ano}: {texto} no ogol — RSSSF {nome(p.mandante)} {p.gm}-{p.gv} {nome(p.visitante)}, ogol {nome(m)} {gm}-{gv} "
                           f"{nome(v)} ({o['data']}); fica a RSSSF")
                break
    novos = []
    for o in og:
        if o["id"] in usados or o["gols_mandante"] is None or not (o.get("mandante_id") and o.get("visitante_id")):
            continue
        m, v = o["mandante_id"], o["visitante_id"]
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
            if not p.fonte_id and og:
                log.append(f"{ano}: só na RSSSF (não achado no ogol): {nome(p.mandante)} {p.gm}-{p.gv} {nome(p.visitante)} ({p.data})")
    return partidas + novos


OGOL_FASE = {"1F": "Primeira fase", "2F": "Segunda fase", "3F": "Terceira fase", "4F": "Quarta fase", "1/16": "Primeira fase eliminatória",
             "1/8": "Oitavas de final", "QF": "Quartas de final", "SF": "Semifinal", "F": "Final"}


def fase_do_ogol(o: dict, partidas: list[Partida]) -> tuple[str, str]:
    """Fase e grupo de um jogo que só o ogol tem: a fase e o grupo em que os dois clubes jogaram juntos, perto da data;
    senão, pelo código de fase do ogol."""
    m, v, d = o["mandante_id"], o["visitante_id"], _dia(o["data"])
    juntos = []
    for (f, g), ps in agrupar(partidas).items():
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
    f = ESPN / f"copa_brasil_{ano}.json"
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


def fase_pt(nome_fase: str) -> str:
    n = nome_fase.strip(" :")
    for padrao, pt in FASES_PT:
        if re.search(padrao, n, re.I):
            return pt
    return n


def nome(cid: str) -> str:
    return clubes_cb.exibicao().get(cid, {}).get("clube", cid)


# --------------------------------------------------------------------------------------------- classificação

def pontos_vitoria(ano: int) -> int:
    return 3 if ano >= 1995 else 2


def ajustes_wiki(ano: int, ids_do_ano: set[str]) -> dict[str, int]:
    """Punições de pontos na Wikipédia em inglês (adjust_points), com o nome casado ao código do ogol."""
    saida = {}
    fs = clubes_cb.exibicao()
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
    ordem_fase: dict[str, int] = {}
    for p in partidas:
        ordem_fase.setdefault(p.fase, ORDEM.get(p.fase, 50))
    alcance: dict[str, int] = defaultdict(int)
    for p in partidas:
        for c in (p.mandante, p.visitante):
            alcance[c] = max(alcance[c], ordem_fase[p.fase])
    final = [p for p in partidas if p.fase == "Final"]
    vice = None
    if campeao and final:
        fin = {x for p in final for x in (p.mandante, p.visitante)} - {campeao}
        vice = next(iter(fin)) if len(fin) == 1 else None
    def pts(c):
        x = camp[c]
        return pv * x[1] + x[2] + ajustes.get(c, 0)
    def chave(c):
        x = camp[c]
        return (c != campeao, c != vice, -alcance[c], -pts(c), -x[1], -(x[4] - x[5]), -x[4], nome(c))
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
    saida = []
    for i, c in enumerate(ordem, 1):
        x = camp[c]
        saida.append({"pos": i, "clube": c, "j": x[0], "v": x[1], "e": x[2], "d": x[3], "gp": x[4], "gc": x[5], "pts": pts(c),
                      "ajuste": ajustes.get(c, 0), "fonte": fonte})
    return saida


ORDEM = {"Fase preliminar": 0.5, "Primeira fase": 1, "Segunda fase": 2, "Terceira fase": 3, "Quarta fase": 4, "Quinta fase": 4.5,
         "Mata-mata": 5, "Primeira fase eliminatória": 5, "Oitavas de final": 6, "Quartas de final": 7, "Semifinal": 8,
         "Fase final": 9, "Final": 10}
NUMERAIS = ["Primeira", "Segunda", "Terceira", "Quarta", "Quinta"]


def datas_do_confronto(ano, partidas: list[Partida], og: list[dict], data_rs: dict, log: list[str]) -> None:
    """Ida e volta do mesmo confronto com a mesma data (revisão TL-004: 2001, a página dá aos dois jogos a data do título
    da rodada): vale a fonte que separa as duas datas, o ogol, senão a página."""
    data_og = {o["id"]: o["data"] for o in og}
    grupos = defaultdict(list)
    for p in partidas:
        grupos[(frozenset((p.mandante, p.visitante)), p.data)].append(p)
    for (par, d), ps in grupos.items():
        if len(ps) < 2 or not d:
            continue
        og_d = [data_og.get(p.fonte_id.split("ogol:")[-1].split(";")[0]) if "ogol:" in p.fonte_id else None for p in ps]
        rs_d = [data_rs.get(id(p)) for p in ps]
        novas = og_d if all(og_d) and len(set(og_d)) == len(ps) else rs_d if all(rs_d) and len(set(rs_d)) == len(ps) else None
        if novas:
            for p, n in zip(ps, novas):
                p.data = n
            log.append(f"{ano}: ida e volta de {nome(ps[0].mandante)} x {nome(ps[0].visitante)} vinham com a mesma data ({d}); "
                       f"ficam {', '.join(novas)} ({'do ogol' if novas == og_d else 'da página'})")


def penaltis_faltando(ano, partidas: list[Partida], og: list[dict], log: list[str]) -> None:
    """Disputa de pênaltis que não está nos campos (revisão CB-008): do placar do ogol ("2-1 (4-3 Pen.)", na ordem do jogo
    do ogol) ou da nota da página ("Rio Negro 4-3 on pen", "3-5pen")."""
    og_por_id = {o["id"]: o for o in og}
    n = 0
    for p in partidas:
        if p.pen_m is not None or p.gm is None:
            continue
        pen = None
        o = og_por_id.get(p.fonte_id.split("ogol:")[-1].split(";")[0]) if "ogol:" in p.fonte_id else None
        m = re.search(r"\((\d+)\s*-\s*(\d+)\s*Pen", (o or {}).get("resultado") or "")
        if m:
            a, b = int(m[1]), int(m[2])
            pen = (a, b) if o.get("mandante_id") == p.mandante else (b, a)
        if pen is None:
            pen = penaltis_da_nota(p.obs, nome(p.mandante), nome(p.visitante))
        if pen:
            p.pen_m, p.pen_v = pen
            n += 1
    if n:
        log.append(f"{ano}: {n} disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)")


def corrigir_jogos(ano, partidas: list[Partida], log: list[str]) -> None:
    for p in partidas:
        c = CORRECAO_JOGO.get((ano, nome(p.mandante), nome(p.visitante), p.data))
        if not c:
            continue
        p.data = c.get("data", p.data)
        p.obs = (p.obs + "; " if p.obs else "") + c["motivo"]
        log.append(f"{ano}: jogo corrigido à mão — {nome(p.mandante)} x {nome(p.visitante)}: {c['motivo']}")


def fases_da_chave(ano: int, partidas: list[Partida], tabs: list[tuple], log: list[str]) -> None:
    """A Copa é mata-mata: as fases saem da própria chave, e não dos títulos das páginas (em inglês, fora de ordem e às
    vezes trocados). Confronto = o mesmo par de clubes (ida e volta a até 200 dias). A final é o último confronto; a fase
    anterior a uma fase são os confrontos anteriores de cada clube dela; e assim até o começo. Nomes de trás para frente:
    Final, Semifinal, Quartas e Oitavas de final; as fases antes delas contam do começo (Primeira fase, Segunda fase...),
    e a primeira, quando tem até um quarto dos confrontos da seguinte, é a Fase preliminar. Mata-mata não tem grupos."""
    pares: dict[frozenset, list[Partida]] = defaultdict(list)
    for p in partidas:
        pares[frozenset((p.mandante, p.visitante))].append(p)
    confrontos: list[list[Partida]] = []
    for ps in pares.values():
        ps.sort(key=lambda p: p.data or "9999")
        cur = [ps[0]]
        for q in ps[1:]:
            if cur[-1].data and q.data and _dist(cur[-1].data, q.data) > 200:   # 2020: ida em março e volta em agosto (pandemia)
                confrontos.append(cur); cur = [q]
            else:
                cur.append(q)
        confrontos.append(cur)
    datados = [c for c in confrontos if any(p.data for p in c)]
    inicio = lambda c: min(p.data for p in c if p.data)
    fim = lambda c: max(p.data for p in c if p.data)
    clubes = lambda c: {c[0].mandante, c[0].visitante}
    if not datados:
        return
    rodadas = [[max(datados, key=fim)]]
    vistos = {id(rodadas[0][0])}
    while True:
        ant = []
        for c in rodadas[-1]:
            for clube in clubes(c):
                prev = [x for x in datados if id(x) not in vistos and clube in clubes(x) and inicio(x) < inicio(c)]
                if prev:
                    x = max(prev, key=inicio)
                    vistos.add(id(x)); ant.append(x)
        if not ant:
            break
        rodadas.append(ant)
    rodadas.reverse()   # do começo para a final
    finais = ["Oitavas de final", "Quartas de final", "Semifinal", "Final"][-len(rodadas):]
    antes = len(rodadas) - len(finais)
    nomes = []
    for k in range(antes):
        nomes.append(f"{NUMERAIS[k]} fase" if k < len(NUMERAIS) else f"{k + 1}ª fase")
    if antes >= 2 and len(rodadas[0]) * 4 <= len(rodadas[1]):
        nomes = ["Fase preliminar"] + [f"{NUMERAIS[k]} fase" for k in range(antes - 1)]
    nomes += finais
    fase_de = {}
    for nome_f, cs in zip(nomes, rodadas):
        for c in cs:
            for p in c:
                fase_de[id(p)] = nome_f
    # confronto fora da chave (sem data, ou clube que não seguiu): a fase em que o clube jogou mais perto daquela data
    sobra = [c for c in confrontos if id(c) not in vistos]
    for c in sobra:
        perto = sorted((abs(_dia(inicio(c)) - _dia(inicio(x))) if c in datados and _dia(inicio(c)) and _dia(inicio(x)) else 999,
                       fase_de[id(x[0])]) for x in datados if id(x) in vistos and clubes(x) & clubes(c))
        f = perto[0][1] if perto else c[0].fase
        for p in c:
            fase_de[id(p)] = f
        log.append(f"{ano}: confronto fora da chave ({nome(c[0].mandante)} x {nome(c[0].visitante)}, {inicio(c) if c in datados else 'sem data'}): "
                   f"fica na {f}")
    mudou = Counter()
    for p in partidas:
        novo = fase_de.get(id(p), p.fase)
        if novo != p.fase:
            mudou[(p.fase, novo)] += 1
        p.fase, p.grupo = novo, ""
    for tb, linhas, *_ in tabs:   # tabelinhas de confronto da RSSSF: a fase dos jogos entre os clubes dela
        fs = Counter(p.fase for p in partidas if p.mandante in linhas and p.visitante in linhas)
        if fs:
            tb.fase = fs.most_common(1)[0][0]
        tb.grupo = ""
    if mudou:
        log.append(f"{ano}: fases pela chave do mata-mata ({' / '.join(f'{n} {len(c)}' for n, c in zip(nomes, rodadas))} confrontos); "
                   f"mudaram: " + "; ".join(f"{a or '—'} → {b} ({n})" for (a, b), n in mudou.most_common()))


# --------------------------------------------------------------------------------------------- uma edição

def campeoes() -> tuple[dict[int, str], dict[int, str]]:
    """Campeões pela RSSSF (cbrcamp.htm) e pela Wikipédia (pt_lista.txt): ano -> nome como a fonte escreve."""
    rs = {}
    t = rsssf.texto(0, "cbrcamp.htm")
    for a, n in re.findall(r"^(\d{4}) - (?!\s*not)(.+?)\s*(?:\(|$)", t, re.M):
        rs[int(a)] = n.strip()
    wk = {}
    txt = (PASTA_DADOS / "wikipedia" / "pt_lista.txt").read_text(encoding="utf-8")
    a, b = txt.find("=== Por clube"), txt.find("=== Por cidade")
    for r in txt[a:b].split("\n|-")[2:]:
        cel = [c for c in r.split("\n|") if c.strip()]
        if len(cel) < 2:
            continue
        nm = re.findall(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", cel[0]) or re.findall(r"\{\{\s*[Ff]utebol\s+([^}|]+)", cel[0])
        for y in re.findall(r"\d{4}", cel[1]):
            wk[int(y)] = nm[0] if nm else cel[0]
    return rs, wk


def montar_edicao(ano: int, log: list[str], rs_campeoes: dict, wk_campeoes: dict) -> dict:
    rs, tabelas = rsssf_cb.ler(ano)
    for (a, n), motivo in RSSSF_FORA.items():
        if a == ano:
            fora = [j for j in rs if n in (j.mandante, j.visitante)]
            rs = [j for j in rs if j not in fora]
            log.append(f"{ano}: {len(fora)} jogos do {n} ficam de fora: {motivo}")
    for (a, m, v, gm, gv), motivo in JOGOS_ANULADOS.items():
        if a == ano:
            fora = [j for j in rs if (j.mandante, j.visitante, j.gm, j.gv) == (m, v, gm, gv)]
            rs = [j for j in rs if j not in fora]
            log.append(f"{ano}: jogo anulado fica de fora ({len(fora)}): {m} {gm}-{gv} {v} — {motivo}")
    for j in rs:
        corr = PLACAR_MANUAL.get((ano, j.mandante, j.visitante, j.data))
        if corr:
            m, v, gm, gv, motivo = corr
            log.append(f"{ano}: jogo da página corrigido — {j.mandante} {j.gm}-{j.gv} {j.visitante} ({j.data}) vira {m} {gm}-{gv} {v}: {motivo}")
            j.mandante, j.visitante, j.gm, j.gv = m, v, gm, gv
            j.gols = ""
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
    partidas = ler_rsssf(ano, mapa, rs_usado)
    partidas = [p for p in partidas if p.gm is not None or p.especial]
    tabs = tabelas_por_clube(tabelas, mapa, rs_usado)
    data_rs = {id(p): p.data for p in partidas}
    partidas = juntar_ogol(ano, partidas, og, tabs, rs_ok, log)
    juntar_espn(ano, partidas, log)   # sem arquivo da ESPN, não faz nada
    datas_do_confronto(ano, partidas, og, data_rs, log)
    penaltis_faltando(ano, partidas, og, log)
    corrigir_jogos(ano, partidas, log)
    # fases em português, nos jogos e nas tabelas (as tabelas já estão ligadas aos códigos dos clubes)
    for p in partidas:
        p.fase = fase_pt(p.fase) if rs_ok else fase_pt(OGOL_FASE.get(p.ogol_fase, p.fase))
        p.grupo = p.grupo if not p.grupo.lower().startswith(("grupo único", "grupo unico")) else ""
    for tb in tabelas:
        tb.fase = fase_pt(tb.fase)
    fases_da_chave(ano, partidas, tabs, log)
    # autores: só quando fecham com o placar
    for p in partidas:
        if p.gols and p.gm is not None and len(p.gols) != p.gm + p.gv:
            p.gols = []
    ids = {x for p in partidas for x in (p.mandante, p.visitante)}
    ajustes = ajustes_wiki(ano, ids) if ano >= 2003 else {}
    # campeão: vencedor da final; conferido com a RSSSF e a Wikipédia (final empatada sem pênaltis: vale a lista oficial)
    campeao = vencedor_final(partidas)
    oficial = campeao_oficial(ano, partidas, rs_campeoes, wk_campeoes)
    if campeao is None and oficial:
        campeao = oficial
        log.append(f"{ano}: final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, {nome(oficial)}")
    elif oficial and campeao != oficial:
        log.append(f"{ano}: vencedor da final pelos jogos ({nome(campeao)}) diferente do campeão oficial ({nome(oficial)}); fica o oficial")
        campeao = oficial
    final = classificacao(ano, partidas, tabs, ajustes, campeao, log)
    conf = conferir(ano, partidas, tabs)
    return {"partidas": partidas, "tabelas": tabelas, "tabs": tabs, "final": final, "conf": conf, "rs": rs, "og": og,
            "mapa": mapa, "campeao": campeao, "ajustes": ajustes}


def campeao_oficial(ano: int, partidas: list[Partida], rs_c: dict, wk_c: dict) -> str | None:
    """O clube da edição cujo nome bate com o campeão da lista da Wikipédia (ou, sem ela, da RSSSF)."""
    alvo = wk_c.get(ano) or rs_c.get(ano)
    if not alvo:
        return None
    fs = clubes_cb.fichas()
    ids = {x for p in partidas for x in (p.mandante, p.visitante)}
    def nota(i):
        nomes = {nome(i), *(fs.get(i, {}).get("nomes_ogol") or []), fs.get(i, {}).get("nome_completo") or "", fs.get(i, {}).get("curto", "")}
        uf = clubes_cb.separar_uf(alvo)[1]   # "Botafogo-PB" x "Botafogo-SP": a UF desempata
        return max(_sim(alvo, x) for x in nomes if x) + (0.1 if uf and fs.get(i, {}).get("uf") == uf else 0)
    melhor = sorted(((nota(i), i) for i in ids), reverse=True)
    return melhor[0][1] if melhor and melhor[0][0] >= 0.8 and (len(melhor) == 1 or melhor[1][0] < melhor[0][0]) else None


# edições em que a RSSSF não serve de base (o ogol é a base dos jogos)
BASE_OGOL: dict[int, str] = {}
# edições em que as tabelas publicadas pela RSSSF são parciais (a página parou no meio): não servem de conferência
TABELAS_PARCIAIS: dict[int, str] = {}


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

def main(anos: list[int], gravar: bool) -> None:
    log: list[str] = []
    rs_c, wk_c = campeoes()
    edicoes = {}
    for ano in anos:
        e = montar_edicao(ano, log, rs_c, wk_c)
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
    anos = [int(a) for a in sys.argv[1:] if a.isdigit()]
    main(anos or ANOS, gravar=not anos)
