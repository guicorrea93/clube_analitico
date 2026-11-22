"""Leitor da fase final do campeonato alemão antigo na RSSSF.

1902/03 a 1943/44: uma página por temporada (tablesd/duit1903.html ... duit1944.html, pelo ano final). A seção "Deutsche
Meisterschaft" traz os participantes ("Berlin:  BTuFC Britannia 1892"), as fases ("1/8 Finals", "Quarterfinals",
"Semifinals", "Final [Jun 7, Frankfurt]", "Replay"...) com a data e o local entre colchetes ("[May 3, Köln]") e os jogos
("TuRU 1880 Düsseldorf     4-1 VfR Mannheim 1896  [aet]"; "w/o", "o/w" e "n/p" sem placar); de 1933/34 em diante, a fase
de grupos ("Gruppe I"), com a matriz de resultados e a tabela na mesma linha. A seção acaba em duas linhas em branco.

1947/48 a 1962/63: uma página só (tablesd/duithist4763.html), uma temporada por bloco ("1950-51"), com as fases ("First
Round:", "Group 1:", "Final:"), a data ("[Jun 6]" ou "13.5.1956" no fim da linha), o local ("(Berlin)"), os jogos de
mata-mata ("FC St Pauli   4-1 Rot-Weiß Essen") e de grupo ("Schalke 04  -  1. FC Kaiserslautern  3:1"), as tabelas
("1.Karlsruher SC   6  3  1  2   7: 5   7- 5") e, em algumas finais, o público e os gols ("1-0 Läpple   17").

Uso como biblioteca: fase_final(arq, ano_fim) e pos_guerra(arq) -> {"jogos": [...], "grupos": {nome: [linhas]}, ...}
"""
from __future__ import annotations

import html
import re
from pathlib import Path

MESES = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
DATA = re.compile(r"^\[(\w{3})\w*\.?\s+(\d{1,2})(?:,\s*(\d{4}))?(?:,\s*([^\]]*))?\]")
JOGO = re.compile(r"^(\S.{0,32}?)\s+(\d+)\s*-\s*(\d+)\s+(\S.*?)\s*(?:\[(.*)\])?\s*$")
JOGO_SEM = re.compile(r"^(\S.{0,32}?)\s+(n/p|w/o|o/w|awd|abd)\s+(\S.*?)\s*(?:\[(.*)\])?\s*$")
FASE = re.compile(r"^\s*(Preliminary Round|Qualifying Round|Round \d|1st Round|2nd Round|1/8 Finals|Eighthfinals|Quarterfinals?|"
                  r"Semifinals?|Final|Replay|Second Replay|Third Place|Group Stage|Gruppe [IVX\d]+[ab]?|Group \d|Play-?off|"
                  r"Intermediate Round|Repeat|Endspiel Gruppe [IVX\d]+)\b(.*)$", re.I)
MATRIZ = re.compile(r"^\s*(\d+)\.\s*(\S.*?)\s+((?:---|\d+-\d+|\s)+?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*-\s*(\d+)\s*$")


def texto(arq: Path) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", arq.read_bytes().decode("latin-1"))).replace("\r", "")


def _data(m: re.Match, ano_fim: int) -> tuple[str | None, str | None]:
    mes = MESES.get(m.group(1).lower()[:3])
    if not mes:
        return None, None
    ano = int(m.group(3)) if m.group(3) else (ano_fim if mes <= 8 else ano_fim - 1)
    return f"{ano:04d}-{mes:02d}-{int(m.group(2)):02d}", (m.group(4) or "").strip() or None


def _jogo(fase, grupo, data, local, nm, nv, gm, gv, nota, especial=None) -> dict:
    return {"fase": fase, "grupo": grupo, "data": data, "local": local, "nm": nm.strip(), "nv": nv.strip(), "gm": gm, "gv": gv,
            "nota": (nota or "").strip() or None, "especial": especial, "publico": None, "gols": []}


def fase_final(arq: Path, ano_fim: int) -> dict:
    """1902/03-1943/44: seção "Deutsche Meisterschaft" da página da temporada."""
    t = texto(arq)
    idx = [m.start() for m in re.finditer(r"\nDeutsche Meisterschaft\.?\s*\n", t)]
    vazio = {"jogos": [], "grupos": {}, "participantes": [], "nao_houve": True}
    if not idx:
        return vazio
    ini = idx[1] if len(idx) > 1 else idx[0]   # a primeira é o índice do topo
    linhas, brancas = [], 0
    for l in t[ini:].split("\n")[2:]:
        brancas = brancas + 1 if not l.strip() else 0
        if brancas >= 2 and linhas:
            break
        linhas.append(l)
    sec = "\n".join(linhas)
    if re.search(r"(?i)not held|not contested", sec[:400]):
        return vazio
    participantes = re.findall(r"^[A-ZÄÖÜ0-9][\w .\-/äöüÄÖÜß]+:\s+(\S.*)$", sec, re.M)
    jogos, grupos = [], {}
    fase, grupo, data, local = None, None, None, None
    aberta, pendente = False, None
    for l in linhas:
        f = FASE.match(l)
        if f and not JOGO.match(l) and not JOGO_SEM.match(l):
            cab = l.split("[")[0].strip().rstrip(":")
            if re.match(r"(?i)gruppe|group \d", cab):
                fase, grupo = "Fase de grupos", cab
            elif re.match(r"(?i)group stage|playoff stage", cab):
                fase, grupo = ("Fase de grupos" if "group" in cab.lower() else fase), None
            else:
                fase, grupo = cab, None
            d = DATA.match(l[l.find("["):]) if "[" in l else None
            data, local = _data(d, ano_fim) if d else (None, None)
            continue
        if l.strip().startswith("["):
            d = DATA.match(l.strip())
            if d:
                data, local = _data(d, ano_fim)
            continue
        m = MATRIZ.match(l)
        if m and grupo:
            grupos.setdefault(grupo, []).append({"posicao": int(m.group(1)), "nome": m.group(2).strip(),
                                                 "celulas": re.findall(r"---|\d+-\d+", m.group(3)),
                                                 "jogos": int(m.group(4)), "vitorias": int(m.group(5)), "empates": int(m.group(6)),
                                                 "derrotas": int(m.group(7)), "pontos": int(m.group(8)),
                                                 "gols_pro": int(m.group(9)), "gols_contra": int(m.group(10))})
            continue
        if not fase or grupo:
            continue
        if l.startswith(" "):   # nota de várias linhas embaixo do jogo ("  [match not played; ...]")
            if jogos and (aberta or l.strip().startswith("[")):
                jogos[-1]["nota"] = " ".join(x for x in (jogos[-1]["nota"], l.strip().strip("[]")) if x)
                aberta = "]" not in l
            continue
        m = JOGO.match(l) or JOGO_SEM.match(l)
        if m:
            if m.re is JOGO:
                nm, gm, gv, resto, esp = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4), None
            else:
                nm, gm, gv, resto, esp = m.group(1), None, None, m.group(3), m.group(2)
            if m.group(m.re.groups):   # a nota entre colchetes que fechou na linha
                resto += f"  [{m.group(m.re.groups)}]"
            partes = re.split(r"\s{2,}", resto.strip(), 1)   # o nome do visitante acaba em dois espaços
            nv, cauda = partes[0], (partes[1].strip() if len(partes) > 1 else "")
            nota = cauda.strip("[]") or None
            if pendente is not None:   # continuação da nota aberta num jogo de cima (colchete à direita)
                pendente["nota"] = " ".join(x for x in (pendente["nota"], cauda.strip("[]")) if x)
                nota = None
                if "]" in cauda:
                    pendente = None
            jogos.append(_jogo(fase, None, data, local, nm, nv, gm, gv, nota, esp))
            if cauda.startswith("[") and "]" not in cauda:
                pendente = jogos[-1]
            aberta = False
    # jogos da fase de grupos, pela matriz (sem data): linha = mandante
    for g, tab in grupos.items():
        nomes = [x["nome"] for x in tab]
        for i, x in enumerate(tab):
            for k, c in enumerate(x["celulas"]):
                mm = re.match(r"^(\d+)-(\d+)$", c)
                if mm and k != i and k < len(nomes):
                    jogos.append(_jogo("Fase de grupos", g, None, None, x["nome"], nomes[k], int(mm.group(1)), int(mm.group(2)), None))
    return {"jogos": jogos, "grupos": grupos, "participantes": participantes, "nao_houve": False}


KO_4763 = re.compile(r"^\s*(?:\((.+?)\))?\s*(\S.*?)\s+(\d+-\d+|awd|w/o)\s+(\S.*?)\s*(?:\[(.*?)\])?\s*$")
GRUPO_4763 = re.compile(r"^\s*(?:\((.+?)\))?\s*(\S.*?)\s+-\s+(\S.*?)\s+(\d+):(\d+)\s*(?:(\d{1,2})\.(\d{1,2})\.(\d{4}))?\s*$")
TABELA_4763 = re.compile(r"^\s*(\d+)\.\s*(\S.*?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+):\s*(\d+)\s+(\d+)-\s*(\d+)\s*$")
GOL_4763 = re.compile(r"^\s*(\d+)-(\d+)\s+(\S.*?)\s+(\d+)\W*$")   # "17\x92": o apóstrofo do minuto (cp1252)


def pos_guerra(arq: Path) -> dict[int, dict]:
    """1947/48-1962/63: página duithist4763.html. Devolve {ano de início: {"jogos", "grupos"}}."""
    t = texto(arq)
    res: dict[int, dict] = {}
    cur = None
    fase = grupo = data = local = None
    modo = None   # "tabela" | "gols"
    data_fim = None   # data no fim da linha (1954/55, 1955/56): vale para o jogo seguinte sem data
    for l in t.split("\n"):
        s = l.strip()
        m = re.match(r"^(\d{4})-(\d{2})$", s)
        if m and int(m.group(1)) >= 1947 and t.find(s) != t.rfind(s):   # cabeçalho do bloco (o índice do topo tem as mesmas)
            if int(m.group(1)) in res or l != s:
                continue
            cur = res.setdefault(int(m.group(1)), {"jogos": [], "grupos": {}})
            fase = grupo = data = local = data_fim = modo = None
            continue
        if cur is None:
            continue
        ano_fim = max(res) + 1
        if re.match(r"^(?:G?roup|Group) (\d+):$", s):
            fase, grupo, modo, data, local, data_fim = "Fase de grupos", "Group " + re.search(r"\d+", s).group(), None, None, None, None
            continue
        if s == "Table:":
            modo = "tabela"
            continue
        if s == "Goals:":
            modo = "gols"
            continue
        m = re.match(r"^Spectators:\s*([\d,.]+)", s)
        if m and cur["jogos"]:
            cur["jogos"][-1]["publico"] = int(re.sub(r"\D", "", m.group(1)))
            continue
        if re.match(r"^[A-Z][\w\s\-]*:$", s):
            fase, grupo, modo, data, local = s[:-1], None, None, None, None
            continue
        if s.startswith("["):
            d = DATA.match(s)
            if d:
                data, local = _data(d, ano_fim)[0], None
            continue
        m = re.match(r"^\((.+)\)$", s)
        if m:
            local = m.group(1)
            continue
        if modo == "tabela":
            m = TABELA_4763.match(l)
            if m:
                cur["grupos"].setdefault(grupo, []).append({
                    "posicao": int(m.group(1)), "nome": m.group(2).strip(), "jogos": int(m.group(3)), "vitorias": int(m.group(4)),
                    "empates": int(m.group(5)), "derrotas": int(m.group(6)), "gols_pro": int(m.group(7)),
                    "gols_contra": int(m.group(8)), "pontos": int(m.group(9))})
            continue
        if modo == "gols":
            m = GOL_4763.match(l)
            if m and cur["jogos"]:
                cur["jogos"][-1]["gols"].append({"placar": (int(m.group(1)), int(m.group(2))), "jogador": m.group(3).strip(),
                                                 "minuto": int(m.group(4))})
            continue
        if not s or not fase:
            continue
        m = GRUPO_4763.match(l)
        if m and grupo:
            if m.group(6):
                data_fim = f"{m.group(8)}-{int(m.group(7)):02d}-{int(m.group(6)):02d}"
            cur["jogos"].append(_jogo(fase, grupo, data_fim or data, m.group(1) or local, m.group(2), m.group(3), int(m.group(4)),
                                      int(m.group(5)), None))
            continue
        m = KO_4763.match(l)
        if m:
            sc = re.match(r"(\d+)-(\d+)", m.group(3))
            cur["jogos"].append(_jogo(fase, grupo, data, m.group(1) or local, m.group(2), m.group(4),
                                      int(sc.group(1)) if sc else None, int(sc.group(2)) if sc else None, m.group(5),
                                      None if sc else m.group(3)))
    return res
