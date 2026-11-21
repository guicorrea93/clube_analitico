"""Junta as fontes da Série B e grava no banco (tabelas *_serie_b) e em CSV (data/serie_b/csv/).

Fontes, na ordem em que são usadas:
- RSSSF Brasil (serie_b/rsssf.py): jogos de todas as edições com fase, grupo, rodada, data e autores dos gols;
  as tabelas de cada fase (conferência) e, em alguns anos, a classificação geral.
- ESPN (serie_b/espn.py), de 2010 em diante: todos os jogos, com data e hora, estádio, público, gols e cartões.
  Nos anos em que a página da RSSSF parou no meio (2014, 2016, 2019 a 2021, 2023 e 2024), é a base dos jogos.
- Wikipédia em inglês (serie_b/wiki.py): tabela final oficial (ordem e punições de pontos) de 2016 em diante e a
  matriz de resultados, que desempata o placar quando RSSSF e ESPN discordam.

Jogo sem rodada (adiado, ou só na ESPN) ganha a primeira rodada em que os dois clubes ainda não jogaram,
na ordem das datas. A classificação final vem da Wikipédia (2016+), da tabela final da RSSSF (pontos corridos)
ou é calculada: fase alcançada, depois pontos, vitórias, saldo e gols pró.

Uso: python serie_b/importar.py [--sem-gravar]     (gera o relatório docs/serie_b_coleta.md)
"""
from __future__ import annotations

import csv
import json
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import clubes  # noqa: E402
import gols as gols_rsssf  # noqa: E402
import nomes  # noqa: E402
import rsssf  # noqa: E402
import wiki  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
DB = RAIZ / "db" / "brasileirao.db"
ESPN = RAIZ / "data" / "serie_b" / "espn"
OGOL = RAIZ / "data" / "serie_b" / "ogol"
CSV = RAIZ / "data" / "serie_b" / "csv"
RELATORIO = RAIZ / "docs" / "serie_b_coleta.md"
FONTE_RSSSF = "https://rsssfbrasil.com/tablesae/br{ano}l2.htm"

# campeões (RSSSF, lista de campeões da 2ª divisão) — conferência da classificação final
CAMPEOES = {
    1971: "Villa Nova-MG", 1972: "Sampaio Corrêa", 1980: "Londrina", 1981: "Guarani", 1982: "Campo Grande-RJ", 1983: "Juventus-SP",
    1984: "Uberlândia", 1985: "Tuna Luso", 1988: "Inter de Limeira", 1989: "Bragantino", 1990: "Sport", 1991: "Paysandu", 1992: "Paraná",
    1994: "Juventude", 1995: "Athletico-PR", 1996: "União São João", 1997: "América-MG", 1998: "Gama", 1999: "Goiás", 2001: "Paysandu",
    2002: "Criciúma", 2003: "Palmeiras", 2004: "Brasiliense", 2005: "Grêmio", 2006: "Atlético-MG", 2007: "Coritiba", 2008: "Corinthians",
    2009: "Vasco", 2010: "Coritiba", 2011: "Portuguesa", 2012: "Goiás", 2013: "Palmeiras", 2014: "Joinville", 2015: "Botafogo",
    2016: "Atlético-GO", 2017: "América-MG", 2018: "Fortaleza", 2019: "Bragantino", 2020: "Chapecoense", 2021: "Botafogo",
    2022: "Cruzeiro", 2023: "Vitória", 2024: "Santos", 2025: "Coritiba",
}
ANOS = sorted(CAMPEOES)

FASES_PT = [  # nome da fase na RSSSF -> português
    (r"^fase única$", "Fase única"), (r"^(first|1st) (phase|stage)", "Primeira fase"), (r"^(second|2nd) (phase|stage)", "Segunda fase"),
    (r"^(third|3rd) (phase|stage)", "Terceira fase"), (r"^(fourth|4th) (phase|stage)", "Quarta fase"), (r"^final (phase|stage)", "Fase final"),
    (r"^quarter", "Quartas de final"), (r"^semi", "Semifinal"), (r"^(1/8|round of 16|eighth)", "Oitavas de final"),
    (r"^finals?$", "Final"), (r"^final table", "Classificação final"), (r"^knockout", "Mata-mata"),
]


def fase_pt(nome: str) -> str:
    n = nome.strip()
    for padrao, pt in FASES_PT:
        if re.search(padrao, n, re.I):
            # mantém o que vem depois ("Second Phase - Promotion playoff" -> "Segunda fase - Promotion playoff")
            resto = re.sub(r"^[^-–(]*", "", n).strip()
            return f"{pt} {resto}".strip() if resto and not resto.startswith("(") else pt
    return n


def grupo_pt(nome: str) -> str:
    return re.sub(r"^group\b", "Grupo", nome.strip(), flags=re.I)


@dataclass
class Partida:
    ano: int
    fase: str
    grupo: str
    rodada: int | None
    data: str | None
    mandante: str
    visitante: str
    gm: int | None
    gv: int | None
    hora: str | None = None
    especial: str = ""
    obs: str = ""
    gols_texto: str = ""
    estadio: str | None = None
    cidade: str | None = None
    publico: int | None = None
    espn_id: str | None = None
    fonte: str = ""
    gols: list[dict] = field(default_factory=list)
    cartoes: list[dict] = field(default_factory=list)
    linha: int = 0


def _minuto(txt: str | None) -> tuple[int | None, int | None]:
    m = re.match(r"(\d+)'?(?:\s*\+\s*(\d+))?", txt or "")
    return (int(m.group(1)), int(m.group(2)) if m.group(2) else None) if m else (None, None)


def jogos_manuais(ano: int) -> list[Partida]:
    """Jogos que nenhuma fonte de placar traz, com o resultado oficial (decisão do tribunal), pela Wikipédia."""
    if ano == 2014:
        return [Partida(2014, "Fase única", "", 1, "2014-04-18", "Joinville", "Portuguesa", 3, 0, hora="19:30", especial="awd",
                        obs="A Portuguesa abandonou o campo aos 17 minutos, por ordem judicial (0-0 no momento); o STJD deu a vitória "
                            "ao Joinville por 3-0.", fonte="Wikipédia (decisão do STJD)")]
    return []


# placar oficial que as fontes de jogos trazem errado (revisão de 20/11/2026, docs/revisao/bra-serie-b.md):
# (ano, mandante, visitante) -> (gols do mandante, gols do visitante, especial, observação)
CORRECOES = {
    (2001, "Figueirense", "Caxias"): (1, 0, "awd", "Jogo encerrado aos 90' com 1-0 por invasão de campo; o STJD manteve a vitória do "
                                      "Figueirense, que foi vice e subiu (CBF; Wikipédia pt e en). Achado SB-002."),
    (1998, "Volta Redonda", "Santa Cruz"): (0, 2, "wo", "W.O.: vitória dada ao Santa Cruz por 2-0 (RSSSF 'awarded 2-0 to Sta.Cruz'; "
                                             "tabela da Wikipédia pt). Achado SB-007."),
    (1994, "Desportiva-ES", "CRB"): (1, 0, "", "Placar 1-0 (ogol e tabela final da Wikipédia pt). Achado SB-008."),
    (2006, "Ituano", "Vila Nova-GO"): (1, 1, "", "Placar 1-1 (tabela da RSSSF, ogol e Wikipédia pt). Achado SB-009."),
    (2008, "Fortaleza", "Criciúma"): (2, 1, "", "Placar 2-1 (tabela da Wikipédia pt, tabela da RSSSF e ogol). Achado SB-010."),
}
# pontos na tabela da RSSSF que não são punição (erro de soma da página): (ano, clube); achados SB-005 e SB-015
AJUSTE_FALSO = {(2008, "Juventude"), (2009, "Juventude"),
                # o Pleno do STJD devolveu os 3 pontos do Brusque em 18/11/2021 (a Wikipédia en mantém a punição); SB-016
                (2021, "Brusque")}
# fase que não leva o clube adiante (repescagem para não cair): não conta como "fase alcançada"; achado SB-003
FASE_DE_BAIXO = re.compile(r"relega|rebaix|repescagem|descenso", re.I)


def corrigir(ano: int, partidas: list[Partida], log: list[str]) -> list[Partida]:
    """Aplica CORRECOES e tira o jogo repetido (mesma fase, mandante, visitante e placar: a página o lista duas
    vezes; fica o de data mais nova). Achado SB-006."""
    for p in partidas:
        c = CORRECOES.get((ano, p.mandante, p.visitante))
        if c:
            antes = f"{p.gm}-{p.gv}"
            p.gm, p.gv, p.especial, p.obs = c[0], c[1], c[2], c[3]
            if p.gols and len(p.gols) != p.gm + p.gv:
                p.gols = []
            log.append(f"{ano}: placar corrigido {p.mandante} {antes} -> {p.gm}-{p.gv} {p.visitante}")
    vistos: dict[tuple, Partida] = {}
    saida = []
    for p in sorted(partidas, key=lambda x: x.data or "", reverse=True):
        k = (p.fase, p.mandante, p.visitante, p.gm, p.gv)
        if p.gm is not None and k in vistos and (p.fase.lower().startswith("final") or p.data == vistos[k].data):
            log.append(f"{ano}: jogo repetido retirado: {p.fase} {p.mandante} {p.gm}-{p.gv} {p.visitante} ({p.data})")
            continue
        vistos[k] = p
        saida.append(p)
    return sorted(saida, key=lambda x: partidas.index(x))


def aplicar_ogol(ano: int, partidas: list[Partida], log: list[str]) -> list[Partida]:
    """ogol: rodada oficial dos jogos de turno único (vale sobre a da RSSSF, que às vezes põe o jogo adiado
    na rodada em que foi jogado) e jogo que faltou nas outras fontes. Nas edições com fases, só confere placar."""
    f = OGOL / f"serie_b_{ano}.json"
    if not f.exists():
        return partidas
    og = []
    for o in json.loads(f.read_text(encoding="utf-8")):
        m, v = nomes.casar(o["mandante"], ano), nomes.casar(o["visitante"], ano)
        if m and v and o["gols_mandante"] is not None:
            og.append((m, v, o))
        elif o["gols_mandante"] is not None:
            log.append(f"{ano}: ogol — clube sem casar: {o['mandante']} x {o['visitante']}")
    por_par = defaultdict(list)
    for p in partidas:
        por_par[(p.mandante, p.visitante)].append(p)
    turno_unico = all(p.fase == "Fase única" for p in partidas)
    mudou_rodada = placar_dif = 0
    novos = []
    dia = lambda d: datetime.strptime(d, "%Y-%m-%d").toordinal() if d else None
    encontros_og = Counter(frozenset((m, v)) for m, v, _ in og)
    encontros_aqui = Counter(frozenset((p.mandante, p.visitante)) for p in partidas)
    incluidos: Counter = Counter()
    for m, v, o in og:
        cands = por_par.get((m, v), [])
        if not turno_unico:   # com fases o par pode se repetir: vale o jogo de data próxima (ou sem data)
            cands = [p for p in cands if p.data is None or abs(dia(p.data) - dia(o["data"])) <= 4]
        if len(cands) > 1:
            cands = [p for p in cands if p.data == o["data"]] or cands[:1]
        p = cands[0] if cands else None
        if p is None and not turno_unico:
            # com fases, as datas das fontes antigas divergem muito: só entra o que o ogol tem a mais desse par
            par = frozenset((m, v))
            if encontros_og[par] - encontros_aqui[par] - incluidos[par] <= 0:
                continue
            incluidos[par] += 1
        if p is None:
            fase, grupo = "Fase única", ""
            if not turno_unico:   # a fase e o grupo em que os dois clubes estavam juntos perto daquela data
                juntos = [(abs(dia(q.data) - dia(o["data"])) if q.data else 99, q.fase, q.grupo) for q in partidas
                          if {q.mandante, q.visitante} & {m, v} and any({r.mandante, r.visitante} >= {m} for r in partidas if (r.fase, r.grupo) == (q.fase, q.grupo))
                          and any({r.mandante, r.visitante} >= {v} for r in partidas if (r.fase, r.grupo) == (q.fase, q.grupo))]
                if not juntos:
                    log.append(f"{ano}: jogo só no ogol, sem fase conhecida (fora): {m} {o['gols_mandante']}-{o['gols_visitante']} {v} ({o['data']}, {o['fase']})")
                    continue
                _, fase, grupo = min(juntos)
            novos.append(Partida(ano, fase, grupo, o["rodada"], o["data"], m, v, o["gols_mandante"], o["gols_visitante"],
                                 hora=o["hora"], fonte="ogol"))
            log.append(f"{ano}: jogo só no ogol, incluído em {fase}{' / ' + grupo if grupo else ''}: {m} {o['gols_mandante']}-{o['gols_visitante']} {v} ({o['data']})")
            continue
        if (p.gm, p.gv) != (o["gols_mandante"], o["gols_visitante"]):
            placar_dif += 1
            if placar_dif <= 15:
                log.append(f"{ano}: placar diferente no ogol — {m} x {v}: aqui {p.gm}-{p.gv}, ogol {o['gols_mandante']}-{o['gols_visitante']}")
        if turno_unico and o["rodada"] and p.rodada != o["rodada"]:
            mudou_rodada += p.rodada is not None
            p.rodada = o["rodada"]
    if mudou_rodada:
        log.append(f"{ano}: rodada do ogol diferente da RSSSF em {mudou_rodada} jogos (fica a do ogol, a oficial)")
    if placar_dif > 15:
        log.append(f"{ano}: ... {placar_dif} placares diferentes no ogol no total")
    return partidas + novos


def ler_espn(ano: int) -> list[Partida]:
    f = ESPN / f"serie_b_{ano}.json"
    if not f.exists():
        return []
    saida = []
    for j in json.loads(f.read_text(encoding="utf-8")):
        if j["situacao"] not in ("STATUS_FULL_TIME", "STATUS_FINAL", "STATUS_FINAL_PEN", "STATUS_FINAL_AET"):
            continue
        m, v = nomes.casar(j["mandante"], ano), nomes.casar(j["visitante"], ano)
        utc = datetime.strptime(j["data_hora"][:16], "%Y-%m-%dT%H:%M")
        local = utc - timedelta(hours=3)
        p = Partida(ano, "Fase única", "", None, local.strftime("%Y-%m-%d"), m or j["mandante"], v or j["visitante"],
                    int(j["gols_mandante"]), int(j["gols_visitante"]), hora=local.strftime("%H:%M"), estadio=j["estadio"],
                    cidade=j["cidade"], publico=j["publico"], espn_id=j["id"], fonte="ESPN")
        for l in j["lances"]:
            lado = {"home": "mandante", "away": "visitante"}.get(l["lado"])
            mi, ac = _minuto(l["minuto"])
            jog = l["jogadores"][0] if l["jogadores"] else None
            if l["gol"]:
                p.gols.append({"lado": lado, "jogador": jog, "minuto": mi, "acrescimo": ac,
                               "tipo": "contra" if l["contra"] else "penalti" if l["penalti"] else "normal", "fonte": "ESPN"})
            elif l["amarelo"] or l["vermelho"]:
                p.cartoes.append({"lado": lado, "jogador": jog, "minuto": mi, "acrescimo": ac, "cor": "vermelho" if l["vermelho"] else "amarelo"})
        saida.append(p)
    return saida


EXTRAS: dict[str, str] = {}   # clubes achados só pela tabela de grupo (nome -> estado)


def clube_de(base: str, uf: str, can: dict) -> str:
    """Clube de nome-base e estado conhecidos (o mesmo nome de exibição já usado); senão, um novo "Base-UF"."""
    k = clubes.chave_base(base, uf)
    for c in can.values():
        b, u = clubes.separar_estado(c["clube"])
        if c["uf"] == uf and clubes.chave_base(b, uf) == k:
            return c["clube"]
    nome = f"{base}-{uf}"
    EXTRAS[nome] = uf
    return nome


def ler_rsssf(ano: int, can: dict) -> tuple[list[Partida], list[rsssf.Tabela], list[rsssf.Jogo]]:
    if not (rsssf.PASTA / f"br{ano}l2.htm").exists():
        return [], [], []
    jogos, tabelas = rsssf.ler(ano)
    # o mesmo nome curto pode ser de dois clubes no mesmo ano, em grupos diferentes ("Nacional" de Manaus no grupo A
    # e de Patos no grupo E, em 1989): quando a tabela do grupo traz o nome com o estado, ela decide
    pelo_grupo: dict[tuple, str] = {}
    for tb in tabelas:
        bloco = {x for j in jogos if (j.fase, j.grupo) == (tb.fase, tb.grupo) for x in (j.mandante, j.visitante)}
        for nt, nj in rsssf.casar([r["nome"] for r in tb.linhas], bloco).items():
            base, uf = clubes.separar_estado(nt)
            uf_ano = can[(ano, nj)]["uf"]
            if uf and uf != uf_ano:
                pelo_grupo[(tb.fase, tb.grupo, nj)] = clube_de(base.split("/")[0].strip(), uf, can)
    def clube(j, nome):
        return pelo_grupo.get((j.fase, j.grupo, nome)) or can[(ano, nome)]["clube"]
    saida = []
    for j in jogos:
        m, v = clube(j, j.mandante), clube(j, j.visitante)
        p = Partida(ano, fase_pt(j.fase), grupo_pt(j.grupo), j.rodada, j.data, m, v, j.gm, j.gv, especial=j.especial,
                    obs=j.nota, gols_texto=j.gols, fonte=FONTE_RSSSF.format(ano=ano), linha=j.linha)
        lidos = gols_rsssf.ler(j.gols, j.gm, j.gv, j.mandante, j.visitante)
        if lidos:
            p.gols = [{**g, "fonte": "RSSSF"} for g in lidos]
        saida.append(p)
    return saida, tabelas, jogos


def juntar(ano: int, rs: list[Partida], es: list[Partida], log: list[str]) -> list[Partida]:
    """Partidas do ano: RSSSF + ESPN (pelo par mandante-visitante; nos pontos corridos ele é único)."""
    if not es:
        return rs
    matriz = {}
    for m, v, gm, gv in wiki.resultados(ano):
        cm, cv = nomes.casar(m, ano), nomes.casar(v, ano)
        if cm and cv:
            matriz[(cm, cv)] = (gm, gv)
    por_par = defaultdict(list)
    for p in rs:
        por_par[(p.mandante, p.visitante)].append(p)
    usados, saida = set(), []
    for e in es:
        cands = por_par.get((e.mandante, e.visitante), [])
        r = next((c for c in cands if id(c) not in usados), None)
        if r is None:
            saida.append(e)
            continue
        usados.add(id(r))
        if r.gm is not None and (r.gm, r.gv) != (e.gm, e.gv):
            w = matriz.get((e.mandante, e.visitante))
            escolha = "RSSSF" if w == (r.gm, r.gv) else "ESPN"
            log.append(f"{ano}: {e.mandante} x {e.visitante} — RSSSF {r.gm}-{r.gv}, ESPN {e.gm}-{e.gv}, Wikipédia "
                       f"{'-'.join(map(str, w)) if w else 'sem'} → fica {escolha}")
            if escolha == "RSSSF":
                e.gm, e.gv = r.gm, r.gv
                e.gols = r.gols
        # do jogo da RSSSF ficam fase, grupo, rodada, nota e o texto dos gols; da ESPN, data e hora, estádio, público e lances
        e.fase, e.grupo, e.rodada, e.obs, e.gols_texto = r.fase, r.grupo, r.rodada, r.obs, r.gols_texto
        e.fonte = "RSSSF + ESPN"
        if not e.gols and r.gols:
            e.gols = r.gols
        saida.append(e)
    so_rsssf = [p for p in rs if id(p) not in usados]
    for p in so_rsssf:
        log.append(f"{ano}: só na RSSSF (não achado na ESPN): {p.mandante} {p.gm}-{p.gv} {p.visitante} ({p.data})")
    return saida + so_rsssf


def _turno_ordem_da_data(pares, fixos, primeiro, meia) -> dict:
    """Cada par, na ordem da data do 1º encontro, vai para a primeira rodada do turno em que os dois estão livres."""
    turno_de, livre = dict(fixos), defaultdict(set)
    for par, k in fixos.items():
        livre[k] |= par
    for par in sorted((p for p in pares if p not in fixos), key=lambda p: primeiro[p]):
        k = next((k for k in range(1, meia + 1) if not (livre[k] & par)), None)
        if k is not None:
            turno_de[par] = k
            livre[k] |= par
    return turno_de


def _turno_posto_do_clube(pares, fixos, primeiro, clubes_fase, meia) -> dict:
    """Cada clube ordena seus confrontos pela data (o n-ésimo é a rodada n); se os dois concordam, fica; os outros
    (adiados, antecipados) vão para a rodada que sobra livre para os dois."""
    turno_de, livre = dict(fixos), defaultdict(set)
    for par, k in fixos.items():
        livre[k] |= par
    posto = {}
    for c in clubes_fase:
        for i, par in enumerate(sorted((p for p in pares if c in p), key=lambda p: primeiro[p]), 1):
            posto[(c, par)] = i
    def candidatas(par):
        a, b = tuple(par)
        return [k for k in dict.fromkeys((posto[(a, par)], posto[(b, par)])) if k <= meia and not (livre[k] & par)]
    pendentes = [p for p in pares if p not in fixos]
    for par in sorted(pendentes, key=lambda p: primeiro[p]):
        a, b = tuple(par)
        k = posto[(a, par)]
        if k == posto[(b, par)] and k <= meia and not (livre[k] & par):
            turno_de[par] = k; livre[k] |= par
    mudou = True
    while mudou:
        mudou = False
        for par in [p for p in pendentes if p not in turno_de]:
            c = candidatas(par)
            if len(c) == 1:
                turno_de[par] = c[0]; livre[c[0]] |= par; mudou = True
    for par in sorted((p for p in pendentes if p not in turno_de), key=lambda p: primeiro[p]):
        k = next((k for k in candidatas(par) + list(range(1, meia + 1)) if not (livre[k] & par)), None)
        if k is not None:
            turno_de[par] = k; livre[k] |= par
    return turno_de


def _turno_busca(pares, fixos, primeiro, clubes_fase, meia) -> dict:
    """Busca com volta atrás: fixa os confrontos em que os dois clubes concordam na rodada (pela ordem das
    datas) e testa, para os outros, as rodadas mais perto dessa posição, começando pelo que tem menos opção."""
    posto = {}
    for c in clubes_fase:
        for i, par in enumerate(sorted((p for p in pares if c in p), key=lambda p: primeiro[p]), 1):
            posto[(c, par)] = i
    turno_de, livre = dict(fixos), defaultdict(set)
    for par, k in fixos.items():
        livre[k] |= par
    for par in sorted((p for p in pares if p not in fixos), key=lambda p: primeiro[p]):
        a, b = tuple(par)
        k = posto[(a, par)]
        if k == posto[(b, par)] and k <= meia and not (livre[k] & par):
            turno_de[par] = k; livre[k] |= par
    resto = [p for p in pares if p not in turno_de]
    def ordem(par):
        a, b = tuple(par)
        return sorted(range(1, meia + 1), key=lambda k: (min(abs(k - posto[(a, par)]), abs(k - posto[(b, par)])), k))
    pref = {par: ordem(par) for par in resto}
    orcamento = [200000]
    def busca() -> bool:
        pend = [p for p in resto if p not in turno_de]
        if not pend:
            return True
        orcamento[0] -= 1
        if orcamento[0] < 0:
            return False
        par = min(pend, key=lambda p: sum(1 for k in pref[p] if not (livre[k] & p)))
        for k in pref[par]:
            if livre[k] & par:
                continue
            turno_de[par] = k; livre[k] |= par
            if busca():
                return True
            del turno_de[par]; livre[k] -= par
        return False
    busca()
    return turno_de


def _turno_valido(turno_de, pares, meia, n) -> bool:
    if len(turno_de) != len(pares):
        return False
    por = Counter(turno_de.values())
    return all(por.get(k) == n // 2 for k in range(1, meia + 1))


def _dispersao(turno_de, primeiro) -> float:
    """Soma das distâncias (em dias) de cada 1º encontro à data mediana da sua rodada."""
    por = defaultdict(list)
    for par, k in turno_de.items():
        if primeiro[par][0] != "9999":
            por[k].append(datetime.strptime(primeiro[par][0], "%Y-%m-%d").toordinal())
    total = 0.0
    for ds in por.values():
        ds.sort()
        med = ds[len(ds) // 2]
        total += sum(abs(d - med) for d in ds)
    return total


def inferir_rodadas(partidas: list[Partida], log: list[str]) -> None:
    """Pontos corridos: descobre a rodada dos jogos que vieram sem ela.

    Turno e returno completos: o returno espelha o turno (A x B na rodada k volta como B x A na k + 19 —
    conferido em todas as temporadas em que a RSSSF traz as rodadas). Cada par de clubes ganha a rodada do
    turno pela rodada conhecida de um dos dois jogos ou, sem ela, pela data do primeiro encontro: a primeira
    rodada do turno em que os dois ainda não jogaram. Fora disso, cada jogo vai para a primeira rodada livre."""
    unica = [p for p in partidas if p.fase == "Fase única"]
    if not unica or all(p.rodada for p in unica):
        return
    clubes_fase = {p.mandante for p in unica} | {p.visitante for p in unica}
    n = len(clubes_fase)
    pares: dict[frozenset, list[Partida]] = defaultdict(list)
    for p in unica:
        pares[frozenset((p.mandante, p.visitante))].append(p)
    if n % 2 == 0 and len(unica) == n * (n - 1) and all(len(v) == 2 for v in pares.values()):
        meia = n - 1
        fixos: dict[frozenset, int] = {}
        for par, js in pares.items():
            r = next((p.rodada for p in js if p.rodada), None)
            if r:
                fixos[par] = r if r <= meia else r - meia
        primeiro = {par: min((p.data or "9999", p.hora or "") for p in js) for par, js in pares.items()}
        # três maneiras de montar o turno; fica a que dá uma tabela válida (cada clube uma vez por rodada,
        # todas as rodadas cheias) com as datas mais juntas dentro de cada rodada
        opcoes = [_turno_ordem_da_data(pares, fixos, primeiro, meia), _turno_posto_do_clube(pares, fixos, primeiro, clubes_fase, meia),
                  _turno_busca(pares, fixos, primeiro, clubes_fase, meia)]
        turno_de = min(opcoes, key=lambda t: (not _turno_valido(t, pares, meia, n), -len(t), _dispersao(t, primeiro)))
        antes = sum(1 for p in unica if p.rodada)
        for par, js in pares.items():
            k = turno_de.get(par)
            if not k:
                continue
            conhecido = next((p for p in js if p.rodada), None)
            if conhecido:   # o outro jogo é o espelho
                for p in js:
                    if not p.rodada:
                        p.rodada = k + meia if conhecido.rodada <= meia else k
            else:           # o primeiro encontro (pela data) é o do turno
                a, b = sorted(js, key=lambda p: (p.data or "9999", p.hora or ""))
                a.rodada, b.rodada = k, k + meia
        por_rodada = Counter(p.rodada for p in unica)
        erradas = {r: c for r, c in por_rodada.items() if c != n // 2}
        log.append(f"{partidas[0].ano}: rodada descoberta para {len(unica) - antes} jogos (turno espelhado no returno)"
                   + (f"; rodadas com nº de jogos diferente de {n // 2}: {erradas}" if erradas else ""))
        return
    total_rodadas = 2 * (n - 1) if len(unica) > n * (n - 1) / 2 + 1 else n - 1
    ocupado: dict[int, set] = defaultdict(set)
    for p in unica:
        if p.rodada:
            ocupado[p.rodada] |= {p.mandante, p.visitante}
    sem = sorted((p for p in unica if not p.rodada), key=lambda p: (p.data or "9999", p.hora or ""))
    for p in sem:
        for r in range(1, total_rodadas + 1):
            if p.mandante not in ocupado[r] and p.visitante not in ocupado[r]:
                p.rodada = r
                ocupado[r] |= {p.mandante, p.visitante}
                break
    por_rodada = Counter(p.rodada for p in unica)
    erradas = {r: c for r, c in por_rodada.items() if c != n // 2}
    log.append(f"{partidas[0].ano}: rodada descoberta para {len(sem)} jogos" + (f"; rodadas com nº de jogos diferente de {n // 2}: {erradas}" if erradas else ""))


def campanha(partidas: list[Partida]) -> dict[str, list[int]]:
    c: dict[str, list[int]] = defaultdict(lambda: [0] * 6)
    for p in partidas:
        if p.gm is None:
            continue
        for eu, a, b in ((p.mandante, p.gm, p.gv), (p.visitante, p.gv, p.gm)):
            x = c[eu]
            x[0] += 1; x[4] += a; x[5] += b
            x[1 if a > b else 2 if a == b else 3] += 1
    return c


def pontos_vitoria(ano: int) -> int:
    return 3 if ano >= 1995 else 2


def classificacao_final(ano: int, partidas: list[Partida], tabelas: list[rsssf.Tabela], rs_jogos: list[rsssf.Jogo],
                        can: dict, log: list[str]) -> list[dict]:
    """[{pos, clube, j, v, e, d, gp, gc, pts, ajuste, fonte}]."""
    camp = campanha(partidas)
    pv = pontos_vitoria(ano)
    # 1. Wikipédia (tabela oficial, com punições)
    tw = wiki.tabela(ano)
    if tw:
        saida = []
        for r in tw:
            c = nomes.casar(r["nome"], ano) or r["nome"]
            j = r["v"] + r["e"] + r["d"]
            aj = 0 if (ano, c) in AJUSTE_FALSO else r["ajuste"]
            saida.append({"pos": r["pos"], "clube": c, "j": j, "v": r["v"], "e": r["e"], "d": r["d"], "gp": r["gp"], "gc": r["gc"],
                          "pts": pv * r["v"] + r["e"] + aj, "ajuste": aj, "fonte": "Wikipédia (tabela oficial)"})
        if any((ano, s["clube"]) in AJUSTE_FALSO for s in saida):   # punição desfeita: a ordem segue os pontos
            saida.sort(key=lambda s: (-s["pts"], -s["v"], -(s["gp"] - s["gc"]), -s["gp"]))
            for i, s in enumerate(saida, 1):
                s["pos"] = i
        for s in saida:
            x = camp.get(s["clube"])
            if x and x != [s["j"], s["v"], s["e"], s["d"], s["gp"], s["gc"]]:
                log.append(f"{ano}: tabela da Wikipédia x jogos — {s['clube']}: tabela {[s['j'], s['v'], s['e'], s['d'], s['gp'], s['gc']]} jogos {x}")
        return saida
    # 2. RSSSF: tabela com todos os clubes da edição e a campanha inteira (pontos corridos) ou a classificação geral
    todos = set(camp)
    for tb in sorted(tabelas, key=lambda t: -len(t.linhas)):
        if len(tb.linhas) < len(todos) or not tb.linhas:
            continue
        nomes_jogos = {j.mandante for j in rs_jogos} | {j.visitante for j in rs_jogos}
        alias = rsssf.casar([r["nome"] for r in tb.linhas], nomes_jogos)
        saida = []
        for r in tb.linhas:
            bruto = alias.get(r["nome"])
            c = can[(ano, bruto)]["clube"] if bruto and (ano, bruto) in can else None
            if not c:
                break
            aj = 0 if ano == 1988 or (ano, c) in AJUSTE_FALSO else r["pts"] - (pv * r["v"] + r["e"])
            saida.append({"pos": r["pos"], "clube": c, "j": r["j"], "v": r["v"], "e": r["e"], "d": r["d"], "gp": r["gp"], "gc": r["gc"],
                          "pts": pv * r["v"] + r["e"] + aj, "ajuste": aj, "fonte": "RSSSF (tabela final)"})
        else:
            # só vale a tabela que traz a campanha inteira de cada clube (não a de uma fase só); no turno único,
            # a tabela publicada vale mesmo que falte jogo na página (fica anotado)
            bate = sum(1 for s in saida if camp.get(s["clube"]) == [s["j"], s["v"], s["e"], s["d"], s["gp"], s["gc"]])
            turno_unico = all(p.fase == "Fase única" for p in partidas) and len({s["j"] for s in saida}) == 1
            if {s["clube"] for s in saida} >= todos and (bate >= 0.9 * len(saida) or turno_unico):
                for s in saida:
                    x = camp.get(s["clube"])
                    if x != [s["j"], s["v"], s["e"], s["d"], s["gp"], s["gc"]]:
                        log.append(f"{ano}: tabela final da RSSSF x jogos — {s['clube']}: tabela {[s['j'], s['v'], s['e'], s['d'], s['gp'], s['gc']]} jogos {x}")
                        if x and turno_unico:   # turno único: vale o que os jogos somam (a página erra a soma; achado SB-015)
                            s.update(zip(("j", "v", "e", "d", "gp", "gc"), x))
                            s["pts"] = pv * s["v"] + s["e"] + s["ajuste"]
                if turno_unico:   # pontos acertados podem mudar a ordem (achado SB-005)
                    saida.sort(key=lambda s: (s["pos"] != 1, -s["pts"], -s["v"], -(s["gp"] - s["gc"]), -s["gp"]))
                    for i, s in enumerate(saida, 1):
                        s["pos"] = i
                return saida
    # 3. calculada: fase alcançada, pontos, vitórias, saldo, gols pró (o campeão da lista oficial em primeiro)
    ordem_fase = {}
    for p in partidas:
        ordem_fase.setdefault(p.fase, 0 if FASE_DE_BAIXO.search(p.fase) else len(ordem_fase))
    alcance = defaultdict(int)
    for p in partidas:
        for c in (p.mandante, p.visitante):
            alcance[c] = max(alcance[c], ordem_fase[p.fase])
    for p in partidas:   # quem foi para a repescagem fica abaixo de todos os que não precisaram dela
        if FASE_DE_BAIXO.search(p.fase):
            alcance[p.mandante] = alcance[p.visitante] = -1
    # punições de pontos (Wikipédia), nas edições de pontos corridos
    ajuste = {}
    if ano >= 2003:
        for nome_w, v in wiki.ajustes(ano).items():
            c = nomes.casar(nome_w, ano)
            if c in camp:
                ajuste[c] = v
    campeao = CAMPEOES.get(ano)
    final = [p for p in partidas if ordem_fase[p.fase] == max(ordem_fase.values())]
    finalistas = {p.mandante for p in final} | {p.visitante for p in final}
    na_final = campanha(final)   # quem chegou à última fase fica na ordem dela (grupo final; achados SB-001, SB-002, SB-004)
    def chave(c):
        x, f = camp[c], na_final.get(c, [0] * 6)
        return (c != campeao, -alcance[c], -(pv * f[1] + f[2]), -f[1], -(f[4] - f[5]), -(pv * x[1] + x[2] + ajuste.get(c, 0)),
                -x[1], -(x[4] - x[5]), -x[4], c)
    saida = []
    for i, c in enumerate(sorted(camp, key=chave), 1):
        x = camp[c]
        saida.append({"pos": i, "clube": c, "j": x[0], "v": x[1], "e": x[2], "d": x[3], "gp": x[4], "gc": x[5],
                      "pts": pv * x[1] + x[2] + ajuste.get(c, 0), "ajuste": ajuste.get(c, 0),
                      "fonte": "calculada (fase alcançada, pontos, vitórias, saldo, gols)"})
    if campeao and campeao not in camp:
        log.append(f"{ano}: campeão oficial {campeao} não aparece nos jogos")
    if len(finalistas) > 2 and not all(p.fase == "Fase única" for p in partidas):
        log.append(f"{ano}: classificação calculada; última fase com {len(finalistas)} clubes (posições abaixo do campeão são aproximadas)")
    return saida


def artilheiros_rsssf() -> dict[int, list[tuple[str, str, int | None]]]:
    """Lista de artilheiros da RSSSF (br2tops.htm): ano -> [(jogador, clube como está na página, gols)].
    Empate: os nomes ficam em linhas seguidas e o número de gols só na última."""
    t = rsssf.texto(0, "br2tops.htm")
    saida: dict[int, list] = {}
    ano, grupo = None, []
    for l in t.splitlines():
        m = re.match(r"^(\d{4})\s+(.*)$", l) or (re.match(r"^\s{4,}(\S.*)$", l) and ano and re.match(r"^\s{4,}()(.*)$", l))
        if not m:
            continue
        if m.group(1):
            ano, grupo = int(m.group(1)), []
        x = re.match(r"^(.+?)\s+\((.+?)\)\s*(\d+)?", m.group(2).strip())
        if not x:
            continue
        grupo.append((x.group(1).strip(), x.group(2).strip()))
        if x.group(3):
            saida[ano] = [(j, c, int(x.group(3))) for j, c in grupo]
    return saida


def classificacao_rodadas(partidas: list[Partida], ajustes: dict[str, int]) -> list[tuple]:
    """Pontos corridos: (rodada, clube, posição, pontos, J, V, E, D, GP, GC) depois de cada rodada."""
    unica = [p for p in partidas if p.fase == "Fase única" and p.rodada and p.gm is not None]
    if not unica:
        return []
    pv = pontos_vitoria(partidas[0].ano)
    clubes_fase = sorted({p.mandante for p in unica} | {p.visitante for p in unica})
    saida = []
    for r in range(1, max(p.rodada for p in unica) + 1):
        camp = campanha([p for p in unica if p.rodada <= r])
        def pts(c):
            x = camp.get(c, [0] * 6)
            return pv * x[1] + x[2] + ajustes.get(c, 0)
        ordem = sorted(clubes_fase, key=lambda c: (-pts(c), -camp.get(c, [0] * 6)[1], -(camp.get(c, [0] * 6)[4] - camp.get(c, [0] * 6)[5]),
                                                  -camp.get(c, [0] * 6)[4], c))
        for i, c in enumerate(ordem, 1):
            x = camp.get(c, [0] * 6)
            saida.append((r, c, i, pts(c), *x))
    return saida


TABELAS_SQL = """
DROP TABLE IF EXISTS fato_artilheiro_serie_b;
DROP TABLE IF EXISTS fato_classificacao_rodada_serie_b;
DROP TABLE IF EXISTS fato_classificacao_final_serie_b;
DROP TABLE IF EXISTS fato_tabela_fase_serie_b;
DROP TABLE IF EXISTS fato_cartao_serie_b;
DROP TABLE IF EXISTS fato_gol_serie_b;
DROP TABLE IF EXISTS fato_partida_serie_b;
DROP TABLE IF EXISTS dim_fase_serie_b;
DROP TABLE IF EXISTS dim_edicao_serie_b;
CREATE TABLE dim_edicao_serie_b (
    edicao_serie_b_id INTEGER PRIMARY KEY,   -- = ano
    temporada_id INTEGER NOT NULL,
    num_clubes INTEGER, num_jogos INTEGER, num_gols INTEGER, pontos_vitoria INTEGER,
    campeao_id INTEGER REFERENCES dim_clube(clube_id), vice_id INTEGER REFERENCES dim_clube(clube_id),
    fontes TEXT, observacao TEXT
);
CREATE TABLE dim_fase_serie_b (
    fase_serie_b_id INTEGER PRIMARY KEY AUTOINCREMENT,
    edicao_serie_b_id INTEGER NOT NULL REFERENCES dim_edicao_serie_b(edicao_serie_b_id),
    fase_ordem INTEGER NOT NULL, fase_nome TEXT NOT NULL, fase_nome_fonte TEXT, num_grupos INTEGER, num_jogos INTEGER,
    UNIQUE (edicao_serie_b_id, fase_nome)
);
CREATE TABLE fato_partida_serie_b (
    partida_serie_b_id INTEGER PRIMARY KEY AUTOINCREMENT,
    edicao_serie_b_id INTEGER NOT NULL REFERENCES dim_edicao_serie_b(edicao_serie_b_id),
    fase_serie_b_id INTEGER NOT NULL REFERENCES dim_fase_serie_b(fase_serie_b_id),
    grupo TEXT, rodada INTEGER, data TEXT, hora TEXT,
    mandante_id INTEGER NOT NULL REFERENCES dim_clube(clube_id), visitante_id INTEGER NOT NULL REFERENCES dim_clube(clube_id),
    gols_mandante INTEGER, gols_visitante INTEGER,
    resultado_especial TEXT,      -- awd (tribunal), wo, n/p (não jogado), abd (abandonado)
    estadio TEXT, cidade TEXT, publico INTEGER, espn_id TEXT,
    gols_texto TEXT,              -- autores dos gols como a RSSSF escreve
    fonte TEXT, observacao TEXT
);
CREATE TABLE fato_gol_serie_b (
    partida_serie_b_id INTEGER NOT NULL REFERENCES fato_partida_serie_b(partida_serie_b_id),
    clube_id INTEGER NOT NULL REFERENCES dim_clube(clube_id),   -- quem ganhou o gol (no gol contra, o adversário do autor)
    jogador TEXT, minuto INTEGER, acrescimo INTEGER, tipo TEXT, fonte TEXT
);
CREATE TABLE fato_cartao_serie_b (
    partida_serie_b_id INTEGER NOT NULL REFERENCES fato_partida_serie_b(partida_serie_b_id),
    clube_id INTEGER NOT NULL REFERENCES dim_clube(clube_id), jogador TEXT, minuto INTEGER, acrescimo INTEGER, cor TEXT, fonte TEXT
);
CREATE TABLE fato_tabela_fase_serie_b (   -- tabelas como a RSSSF publica (conferência)
    edicao_serie_b_id INTEGER NOT NULL, fase TEXT, grupo TEXT, posicao INTEGER, clube_id INTEGER, nome_fonte TEXT,
    jogos INTEGER, vitorias INTEGER, empates INTEGER, derrotas INTEGER, gols_pro INTEGER, gols_contra INTEGER, pontos INTEGER
);
CREATE TABLE fato_classificacao_final_serie_b (
    edicao_serie_b_id INTEGER NOT NULL REFERENCES dim_edicao_serie_b(edicao_serie_b_id),
    clube_id INTEGER NOT NULL REFERENCES dim_clube(clube_id), posicao INTEGER NOT NULL,
    jogos INTEGER, vitorias INTEGER, empates INTEGER, derrotas INTEGER, gols_pro INTEGER, gols_contra INTEGER,
    pontos INTEGER, ajuste_pontos INTEGER, fonte TEXT,
    PRIMARY KEY (edicao_serie_b_id, clube_id)
);
CREATE TABLE fato_classificacao_rodada_serie_b (
    edicao_serie_b_id INTEGER NOT NULL, rodada INTEGER NOT NULL, clube_id INTEGER NOT NULL, posicao INTEGER,
    pontos INTEGER, jogos INTEGER, vitorias INTEGER, empates INTEGER, derrotas INTEGER, gols_pro INTEGER, gols_contra INTEGER,
    PRIMARY KEY (edicao_serie_b_id, rodada, clube_id)
);
CREATE TABLE fato_artilheiro_serie_b (
    edicao_serie_b_id INTEGER NOT NULL, jogador TEXT NOT NULL, clube_id INTEGER, clube_fonte TEXT, gols INTEGER, fonte TEXT
);
CREATE INDEX idx_partida_serie_b ON fato_partida_serie_b(edicao_serie_b_id, fase_serie_b_id);
CREATE INDEX idx_partida_serie_b_clubes ON fato_partida_serie_b(mandante_id, visitante_id);
CREATE INDEX idx_gol_serie_b ON fato_gol_serie_b(partida_serie_b_id);
"""


def montar() -> tuple[dict, list[str]]:
    por_ano_rs = clubes.resolver_todos()
    can = clubes.canonicos(por_ano_rs)
    log: list[str] = []
    edicoes = {}
    for ano in ANOS:
        rs, tabelas, rs_jogos = ler_rsssf(ano, can)
        es = ler_espn(ano)
        partidas = juntar(ano, rs, es, log)
        partidas = [p for p in partidas if p.gm is not None or p.especial]
        if len({p.fase for p in partidas}) == 1:   # turno único ("First Phase" numa página sem outra fase)
            for p in partidas:
                p.fase = "Fase única"
        partidas = aplicar_ogol(ano, partidas, log)
        for jm in jogos_manuais(ano):
            if not any((p.mandante, p.visitante) == (jm.mandante, jm.visitante) for p in partidas):
                partidas.append(jm)
                log.append(f"{ano}: jogo incluído à mão (resultado do tribunal): {jm.mandante} {jm.gm}-{jm.gv} {jm.visitante}")
        partidas = corrigir(ano, partidas, log)
        inferir_rodadas(partidas, log)
        # autores só quando fecham com o placar, lado a lado (a ESPN às vezes repete ou deixa de fora um lance, ou grava o
        # gol contra como gol do time de quem chutou; achado SB-011)
        lado = lambda p, l: sum(1 for g in p.gols if g.get("lado") == l)
        for p in partidas:   # gol sem time (a ESPN deixa assim o gol contra): vai para o lado que falta, se só um lado falta
            sem = [g for g in p.gols if not g.get("lado")]
            if sem and p.gm is not None:
                falta = {"mandante": p.gm - lado(p, "mandante"), "visitante": p.gv - lado(p, "visitante")}
                if sorted(falta.values()) == [0, len(sem)]:
                    quem = max(falta, key=falta.get)
                    for g in sem:
                        g["lado"], g["tipo"] = quem, "contra"
        sem_fechar = [p for p in partidas if p.gols and p.gm is not None and (len(p.gols) != p.gm + p.gv
                      or not all(g.get("lado") for g in p.gols) or (lado(p, "mandante"), lado(p, "visitante")) != (p.gm, p.gv))]
        for p in sem_fechar:
            p.gols = []
        if sem_fechar:
            log.append(f"{ano}: autores dos gols descartados em {len(sem_fechar)} jogos (os lances não fecham com o placar)")
        final = classificacao_final(ano, partidas, tabelas, rs_jogos, can, log)
        if final and CAMPEOES.get(ano) and final[0]["clube"] != CAMPEOES[ano]:
            log.append(f"{ano}: 1º da classificação ({final[0]['clube']}) não é o campeão oficial ({CAMPEOES[ano]})")
        ajustes = {f["clube"]: f["ajuste"] for f in final if f["ajuste"]}
        rodadas = classificacao_rodadas(partidas, ajustes) if ano >= 2006 else []
        edicoes[ano] = {"partidas": partidas, "tabelas": tabelas, "rs_jogos": rs_jogos, "final": final, "rodadas": rodadas,
                        "fontes": ("RSSSF Brasil" if rs else "") + (" + ESPN" if es else "") + (" + ogol" if (OGOL / f"serie_b_{ano}.json").exists() else "")
                                  + (" + Wikipédia" if wiki.tabela(ano) or wiki.ajustes(ano) else "")}
    return {"edicoes": edicoes, "can": can, "artilheiros": artilheiros_rsssf()}, log


def gravar(dados: dict) -> None:
    con = sqlite3.connect(DB)
    con.executescript(TABELAS_SQL)
    # clubes: os que já estão na Série A mantêm o id; os novos entram em dim_clube com nome e estado
    ids: dict[str, int] = {}
    info = {}
    for c in dados["can"].values():
        info[c["clube"]] = (c["uf"], c["clube_id"])
    for nome_x, uf_x in EXTRAS.items():
        info.setdefault(nome_x, (uf_x, None))
    usados = {p.mandante for e in dados["edicoes"].values() for p in e["partidas"]} | \
             {p.visitante for e in dados["edicoes"].values() for p in e["partidas"]} | \
             {f["clube"] for e in dados["edicoes"].values() for f in e["final"]}
    for c in sorted(usados):
        uf, cid = info.get(c, (None, None))
        if not cid:
            linha = con.execute("SELECT clube_id FROM dim_clube WHERE nome = ?", (c,)).fetchone()
            cid = linha[0] if linha else con.execute("INSERT INTO dim_clube (nome, uf) VALUES (?, ?)", (c, uf)).lastrowid
        ids[c] = cid
    CSV.mkdir(parents=True, exist_ok=True)
    for ano, e in dados["edicoes"].items():
        ps = e["partidas"]
        final = e["final"]
        con.execute("INSERT INTO dim_edicao_serie_b VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (ano, ano, len(final), len(ps), sum((p.gm or 0) + (p.gv or 0) for p in ps), pontos_vitoria(ano),
                     ids.get(final[0]["clube"]) if final else None, ids.get(final[1]["clube"]) if len(final) > 1 else None, e["fontes"].strip(" +"), None))
        fases = {}
        for p in ps:
            fases.setdefault(p.fase, []).append(p)
        fase_id = {}
        for ordem, (nome_f, jogos_f) in enumerate(fases.items(), 1):
            fase_id[nome_f] = con.execute("INSERT INTO dim_fase_serie_b (edicao_serie_b_id, fase_ordem, fase_nome, num_grupos, num_jogos) VALUES (?,?,?,?,?)",
                                          (ano, ordem, nome_f, len({p.grupo for p in jogos_f if p.grupo}) or None, len(jogos_f))).lastrowid
        linhas_csv = []
        for p in sorted(ps, key=lambda p: (fase_id[p.fase], p.data or "9999", p.hora or "", p.linha)):
            pid = con.execute("""INSERT INTO fato_partida_serie_b (edicao_serie_b_id, fase_serie_b_id, grupo, rodada, data, hora, mandante_id,
                                 visitante_id, gols_mandante, gols_visitante, resultado_especial, estadio, cidade, publico, espn_id, gols_texto, fonte, observacao)
                                 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                              (ano, fase_id[p.fase], p.grupo or None, p.rodada, p.data, p.hora, ids[p.mandante], ids[p.visitante], p.gm, p.gv,
                               p.especial or None, p.estadio, p.cidade, p.publico, p.espn_id, p.gols_texto or None, p.fonte, p.obs or None)).lastrowid
            for g in p.gols:
                con.execute("INSERT INTO fato_gol_serie_b VALUES (?,?,?,?,?,?,?)",
                            (pid, ids[p.mandante if g["lado"] == "mandante" else p.visitante], g["jogador"], g["minuto"], g["acrescimo"], g["tipo"], g["fonte"]))
            for k in p.cartoes:
                if k["lado"]:
                    con.execute("INSERT INTO fato_cartao_serie_b VALUES (?,?,?,?,?,?,?)",
                                (pid, ids[p.mandante if k["lado"] == "mandante" else p.visitante], k["jogador"], k["minuto"], k["acrescimo"], k["cor"], "ESPN"))
            linhas_csv.append([ano, p.fase, p.grupo, p.rodada or "", p.data or "", p.hora or "", p.mandante,
                               "" if p.gm is None else f"{p.gm}-{p.gv}", p.visitante, p.especial, p.estadio or "", p.publico or "", p.obs, p.fonte])
        with open(CSV / f"serie_b_{ano}_partidas.csv", "w", encoding="utf-8-sig", newline="") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["temporada", "fase", "grupo", "rodada", "data", "hora", "mandante", "placar", "visitante", "especial", "estadio", "publico", "observacao", "fonte"])
            w.writerows(linhas_csv)
        for f_ in final:
            con.execute("INSERT INTO fato_classificacao_final_serie_b VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                        (ano, ids[f_["clube"]], f_["pos"], f_["j"], f_["v"], f_["e"], f_["d"], f_["gp"], f_["gc"], f_["pts"], f_["ajuste"], f_["fonte"]))
        nomes_jogos = {j.mandante for j in e["rs_jogos"]} | {j.visitante for j in e["rs_jogos"]}
        for tb in e["tabelas"]:
            alias = rsssf.casar([r["nome"] for r in tb.linhas], nomes_jogos)
            for r in tb.linhas:
                bruto = alias.get(r["nome"])
                c = dados["can"].get((ano, bruto), {}).get("clube") if bruto else None
                con.execute("INSERT INTO fato_tabela_fase_serie_b VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            (ano, fase_pt(tb.fase), grupo_pt(tb.grupo) or None, r["pos"], ids.get(c), r["nome"], r["j"], r["v"], r["e"], r["d"], r["gp"], r["gc"], r["pts"]))
        lista = dados["artilheiros"].get(ano)
        if lista:
            for jog, clube_txt, n in lista:
                c = nomes.casar(clube_txt, ano)
                con.execute("INSERT INTO fato_artilheiro_serie_b VALUES (?,?,?,?,?,?)", (ano, jog, ids.get(c), clube_txt, n, "RSSSF (lista de artilheiros)"))
        else:
            cont = Counter((g["jogador"], p.mandante if g["lado"] == "mandante" else p.visitante) for p in ps for g in p.gols
                           if g["tipo"] != "contra" and g["jogador"])
            total_gols = sum((p.gm or 0) + (p.gv or 0) for p in ps)
            if cont and sum(cont.values()) >= 0.95 * total_gols:   # só com autor de quase todos os gols
                topo = max(cont.values())
                for (jog, c), n in cont.items():
                    if n == topo:
                        con.execute("INSERT INTO fato_artilheiro_serie_b VALUES (?,?,?,?,?,?)", (ano, jog, ids.get(c), c, n, "contagem dos gols com autor"))
        for r, c, pos, pts, j, v, em, d, gp, gc in e["rodadas"]:
            con.execute("INSERT INTO fato_classificacao_rodada_serie_b VALUES (?,?,?,?,?,?,?,?,?,?,?)", (ano, r, ids[c], pos, pts, j, v, em, d, gp, gc))
    con.commit()
    con.close()


def relatorio(dados: dict, log: list[str]) -> None:
    linhas = ["# Série B — coleta de dados", "",
              "Gerado por `python serie_b/importar.py`. Fontes: RSSSF Brasil (todas as edições), ESPN (2010 em diante),",
              "ogol (rodada oficial; conferência de placar e jogos que faltavam) e Wikipédia em inglês (tabela final de 2016",
              "em diante, punições de pontos e matriz de resultados).", "",
              "| Ano | Fontes | Clubes | Jogos | Gols | Gols c/ autor | Rodada | Campeão | Classificação |",
              "|---|---|---|---|---|---|---|---|---|"]
    for ano, e in dados["edicoes"].items():
        ps = e["partidas"]
        ng = sum((p.gm or 0) + (p.gv or 0) for p in ps)
        com_autor = sum(len(p.gols) for p in ps)
        com_rodada = sum(1 for p in ps if p.rodada)
        f = e["final"]
        linhas.append(f"| {ano} | {e['fontes'].strip(' +')} | {len(f)} | {len(ps)} | {ng} | {com_autor} | {com_rodada} | "
                      f"{f[0]['clube'] if f else '-'} | {f[0]['fonte'] if f else '-'} |")
    linhas += ["", "## Ocorrências", ""] + [f"- {l}" for l in log]
    RELATORIO.write_text("\n".join(linhas) + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    dados, log = montar()
    for ano, e in dados["edicoes"].items():
        f = e["final"]
        print(f"{ano}: {len(e['partidas'])} jogos, {len(f)} clubes, campeão {f[0]['clube'] if f else '-'} ({f[0]['fonte'] if f else '-'}), "
              f"{sum(len(p.gols) for p in e['partidas'])} gols com autor")
    print(len(log), "ocorrências")
    relatorio(dados, log)
    if "--sem-gravar" not in sys.argv:
        gravar(dados)
        print("gravado em", DB)
