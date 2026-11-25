"""Leitor genérico das páginas de temporada da RSSSF (rsssf.org/tablesX/...), copiado de coleta/comum-sulamerica/rsssf_sul.py (23/11/2026; de novo em 26/11/2026, com a data no título da fase e os autores em duas linhas) para as coletas da Oceania.

As páginas são texto pré-formatado: tabelas ("1. River Plate  34 20 8 6 60-30 48"), cabeçalhos de rodada
("Round 1 [Apr 2]:"), datas ("[Apr 5, Sun]") e jogos ("Atlanta   3-3  San Lorenzo  [at Boca Juniors]"), às vezes
com os autores dos gols na linha seguinte ("[Stagnaro, Soria; Gaslini]"). Cada país e cada época escreve de um jeito;
o leitor aceita as variações vistas e devolve, para um trecho da página:

- jogos: [Jogo] na ordem da página, com rodada, data, local, nota, autores e o título de seção em vigor;
- tabelas: [Tabela] com as linhas publicadas e o título de seção em vigor.

Uso como biblioteca:
    texto = rsssf_oce.texto(caminho)                 # página -> texto puro (linhas)
    jogos, tabelas = rsssf_oce.ler(linhas, ano_ini, ano_fim, fases=[(regex, nome), ...])
"""
from __future__ import annotations

import html
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

MESES = {"jan": 1, "feb": 2, "fev": 2, "mar": 3, "apr": 4, "abr": 4, "may": 5, "mai": 5, "jun": 6, "jul": 7, "aug": 8, "ago": 8,
         "sep": 9, "set": 9, "sept": 9, "oct": 10, "out": 10, "nov": 11, "dec": 12, "dic": 12, "dez": 12, "ene": 1, "enero": 1}


def texto(caminho: Path) -> list[str]:
    """Página da RSSSF -> linhas de texto puro (tabulações viram espaços, com paradas de 8)."""
    b = caminho.read_bytes()
    try:
        t = b.decode("utf-8")
    except UnicodeDecodeError:
        t = b.decode("cp1252", "ignore")
    t = re.sub(r"<br\s*/?>", "\n", t, flags=re.I)
    t = re.sub(r"</?(p|h\d|tr|div)\b[^>]*>", "\n", t, flags=re.I)
    t = html.unescape(re.sub(r"<[^>]+>", "", t)).replace("\xa0", " ").replace("\r", "")
    return [l.expandtabs(8).rstrip() for l in t.split("\n")]


def chave(nome: str) -> str:
    """Nome sem acento, minúsculo, só letras e números separados por um espaço."""
    s = unicodedata.normalize("NFKD", nome or "").encode("ascii", "ignore").decode().lower()
    s = s.replace("'", "").replace("’", "").replace("´", "")
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


@dataclass
class Jogo:
    linha: int                 # índice da linha na página (ordem)
    mandante: str
    visitante: str
    gm: int | None
    gv: int | None
    rodada: int | None = None
    data: str | None = None    # AAAA-MM-DD
    secao: str = ""            # título de seção em vigor (texto)
    fase: str = ""             # fase reconhecida pelos padrões passados a ler()
    grupo: str = ""            # "A", "B", "1"... pelos títulos "Group A", "Zona 1"; "Interzonal" nos jogos entre grupos
    especial: str = ""         # wo (W.O.), awd (tribunal), n/p, abd, anulado
    nota: str = ""             # texto entre colchetes ou depois do placar
    local: str | None = None   # "at Boca Juniors"
    gols_texto: str = ""       # autores como a página escreve
    pen_m: int | None = None
    pen_v: int | None = None
    prorrogacao: bool = False
    texto: str = ""            # a linha original
    gm_of: int | None = None   # placar oficial quando difere do jogado (tribunal: "Awarded 2-0", "won the points (0-1)")
    gv_of: int | None = None


@dataclass
class Tabela:
    linha: int
    secao: str
    fase: str
    linhas: list[dict] = field(default_factory=list)
    grupo: str = ""   # {pos, nome, cidade, j, v, e, d, gp, gc, pts, obs}


# ------------------------------------------------------------------------------------------------ padrões

_PLACAR = r"(?P<gm>\d{1,2})\s*[-:]\s*(?P<gv>\d{1,2})"
_ESPECIAL = r"(?P<esp>wp\s*[-:]\s*[l1]p|[l1]p\s*[-:]\s*wp|lw\s*[-:]\s*wp|wp\s*[-:]\s*lw|void|frib|w\s*[-:]\s*l|l\s*[-:]\s*w|\+\s*[-:]\s*-|-\s*[-:]\s*\+|w/o|awd\.?|n/p|abd\.?|susp\.?|ann\.?|canc\.?|p\s*[-:]\s*p|\?\s*[-:]\s*\?)"
# "Atlanta   3-3  San Lorenzo  [at Boca]"; "Racing Club 1:1 Belgrano"; "Estudiantes  wp-lp  Reformer"
_JOGO = re.compile(rf"^(?P<a>\S.*?)(?:\s+|(?<=\)))(?:(?P<wl1>(?-i:wp|lp))\s+(?=\d))?(?:\[(?P<pk_m>\d{{1,2}})\]\s*)?(?:{_PLACAR}|{_ESPECIAL})(?:\s*\[(?P<pk_v>\d{{1,2}})\])?(?:\s+(?P<wl2>(?-i:wp|lp))\b)?(?P<x>\s*\(?(?:aet|a\.e\.t\.|et|pror\.?)\)?(?:\s*,?\s*(?:PK|pen\.?)\s*\d{{1,2}}\s*[-:]\s*\d{{1,2}})?)?(?:\s+awd\.?\s+(?P<awd_m>\d{{1,2}})\s*[-:]\s*(?P<awd_v>\d{{1,2}}))?(?:\s+(?P<b>\S.*?))?\s*$", re.I)
_JOGO_FIM = re.compile(r"^(?P<a>[^\d\s\[(].*?)\s{2,}(?:v\s+)?(?P<b>[^\d\s\[(].*?)\s+"
                       r"(?P<p>\d{1,2}\s*[-:]\s*\d{1,2}(?:\s*\(?(?:aet|a\.e\.t\.)\)?)?|(?:w/o|awd\.?|n/p|abd\.?|susp\.?|canc\.?))"
                       r"(?P<resto>\s+[\[(].*)?\s*$", re.I)
# nome que começa por número só com data ("9 de Octubre", "3 de Febrero", "12 de Octubre")
_LINHA_TAB = re.compile(r"^\s*(?:(?P<pos>\d{1,3})\s*[\.\)]\s*|(?P<sp>\s*))(?P<nome>(?:\d{1,2} de [A-Z]|[^\d\s\[\(\-=])[^\[]*?)\s+"
                        r"(?P<nums>\d{1,3}(?:\s*[-:]?\s*\d{1,3}){5,16})(?P<resto>\s*(?:\D.*)?)$")


def linha_tabela(l: str) -> dict | None:
    """Linha de tabela -> {pos, nome, j, v, e, d, gp, gc, pts, obs}. Aceita 7 números (J V E D GP GC P),
    8 (com saldo antes dos pontos) e 13 (com campanha em casa e fora). Confere V+E+D = J."""
    m = _LINHA_TAB.match(l)
    if not m:
        return None
    n = [int(x) for x in re.findall(r"\d+", m.group("nums"))]
    if len(n) == 7:
        j, v, e, d, gp, gc, pts = n
    elif len(n) == 8 and n[6] == n[4] - n[5]:
        j, v, e, d, gp, gc, _, pts = n
    elif len(n) == 8 and n[1] + n[2] + n[3] == n[0]:
        j, v, e, d, gp, gc, pts = n[:7]   # coluna extra depois dos pontos (média, pontos de promédio)
    elif len(n) == 13 and n[4] + n[7] == n[1]:
        j, v, e, d, gp, gc, pts = n[0], n[1], n[2], n[3], n[10], n[11], n[12]
    else:
        return None
    if v + e + d != j:
        return None
    nome = re.sub(r"\s+", " ", m.group("nome")).strip(" .")
    sigla = re.fullmatch(r"(?:[A-Z]\.){3,}[A-Z]?", nome + ".")   # "C.U.R.C.C."
    # cabeçalho ("No Team", "Team  P W D L", "Pos"); "Team Wellington" e "Team Otago" (NZ) são clubes
    if (not re.search(r"[A-Za-zÀ-ÿ]{2}", nome) and not sigla) or re.match(r"^(no|pos)\b|^team$|^team\s+(name|p|pld)\b", nome, re.I):
        return None
    resto = (m.group("resto") or "").strip()
    cidade = mc.group(1) if (mc := re.search(r"\(([^)]+)\)", resto)) else None
    return {"pos": int(m.group("pos")) if m.group("pos") else None, "nome": nome, "cidade": cidade, "j": j, "v": v, "e": e, "d": d,
            "gp": gp, "gc": gc, "pts": pts, "obs": resto}


_RODADA = re.compile(r"^\s*(?:(?:Round|Fecha|Matchday|Jornada|Rodada|Date)\s*(?P<n1>\d{1,2})\b|(?P<n2>\d{1,2})\s*(?:st|nd|rd|th|º|°|ª)?\.?\s*(?:Round|Fecha|Jornada)\b)(?P<resto>.*)$", re.I)
_DATA = re.compile(r"(?P<d1>\d{1,2})\s*(?:de\s+)?(?P<m1>[A-Za-z]{3,5})\.?(?:\s+(?P<a1>\d{4}))?|(?P<m2>[A-Za-z]{3,5})\.?\s*(?P<d2>\d{1,2})(?:\s*,\s*(?P<a2>\d{4}))?|(?P<d3>\d{1,2})[/.](?P<m3>\d{1,2})(?:[/.](?P<a3>\d{2,4}))?")


def _mes(s: str) -> int | None:
    s = s.lower().rstrip(".")
    return MESES.get(s) or MESES.get(s[:3]) if s[:3] in MESES or s in MESES else None


def achar_data(s: str) -> tuple[int, int, int | None] | None:
    """(mês, dia, ano ou None) do primeiro trecho de data em s: "Apr 5", "5 Apr", "[May 3. Sun]", "5/4"."""
    for m in _DATA.finditer(s):
        if m.group("m1") and _mes(m.group("m1")):
            return _mes(m.group("m1")), int(m.group("d1")), int(m.group("a1")) if m.group("a1") else None
        if m.group("m2") and _mes(m.group("m2")):
            return _mes(m.group("m2")), int(m.group("d2")), int(m.group("a2")) if m.group("a2") else None
        if m.group("m3") and 1 <= int(m.group("m3")) <= 12 and 1 <= int(m.group("d3")) <= 31:
            a = m.group("a3")
            return int(m.group("m3")), int(m.group("d3")), (int(a) + (1900 if int(a) > 30 else 2000) if a and len(a) == 2 else int(a) if a else None)
    return None


# "[Dec 23]", "[Dec 23, 1997]", "[23 Dec]", "[Jul 29, Estadio Centenario]" num título (só mês e dia no começo do colchete)
_DATA_TITULO = re.compile(r"\[\s*((?:[A-Za-z]{3,9}\.?\s+\d{1,2}|\d{1,2}\s+[A-Za-z]{3,9}\.?)(?:,?\s*\d{4})?)\s*(?:[,;][^\]]*)?\]")


def _linha_de_data(l: str) -> bool:
    """Linha que é só data: "[Apr 5, Sun]", "Apr 5", "(5/4)", "Sunday, April 5"."""
    s = l.strip().strip("[]():").strip()
    if not s or len(s) > 40:
        return False
    if not achar_data(s):
        return False
    if re.search(r"\d\s*-\s*\d{1,2}\s+\S", s) and _jogo(l):
        return False   # jogo entre clubes com nome de data: "3 de Febrero  2-0  12 de Octubre"
    resto = re.sub(r"\b(mon|tue|wed|thu|fri|sat|sun)[a-z]*\.?|\b\d{1,4}\b|[,\./\-]|\b(de|of)\b", " ", s, flags=re.I)
    resto = re.sub(r"\b(" + "|".join(MESES) + r")[a-z]*\.?", " ", resto, flags=re.I)
    return not resto.strip()


_GRUPO = re.compile(r"^\s*(?:\d\.\d\.\s*)?(?:Table\s*[-–]?\s*)?(?:(?P<inter>Inter\s*-?\s*(?:group|zonal|zone)s?\b.*|Group [A-Z] vs\.? Group [A-Z].*|Interzonal.*)"
                    r"|(?:Group|Grupo|Zona|Zone|Serie)\s+(?P<g>[A-Z0-9]{1,2}|Even|Odd|Par|Impar|Norte|Sur|North|South)\b[^:\[]{0,25}?)\s*:?\s*$", re.I)
_NOTA_FIM = re.compile(r"\s*(\[[^\]]*\]?|\((?!\s*\d+\s*-\s*\d+\s*pen)[^)]*\)\s*$)\s*$")


def _limpa_nome(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip(" .;,*#")).strip()


def _separa_b(b: str) -> tuple[str, str, str | None]:
    """Lado direito do jogo -> (visitante, nota, local). Corta notas entre colchetes, "at X" e colunas extras."""
    nota, local = "", None
    m = re.search(r"\[(.*?)\]?\s*$", b)
    if m and "[" in b:
        nota = m.group(1)
        b = b[:b.index("[")]
    partes = re.split(r"\s{2,}", b.strip())
    b = partes[0]
    extra = " ".join(partes[1:]).strip()
    m = re.search(r"\s+(?:at|en|played at)\s+(.+)$", b)
    if m:
        local, b = m.group(1).strip(), b[:m.start()]
    if extra:
        if re.match(r"^(at|en|played at)\s+", extra, re.I):
            local = re.sub(r"^(at|en|played at)\s+", "", extra, flags=re.I)
        else:
            nota = (nota + " " + extra).strip()
    if nota and (lm := re.match(r"^\s*(?:played )?at\s+(.+?)\s*$", nota, re.I)):
        local = local or lm.group(1)
    return _limpa_nome(b), nota.strip(), local


def _penaltis(txt: str) -> tuple[int | None, int | None]:
    m = re.search(r"(\d{1,2})\s*[-:]\s*(\d{1,2})\s*(?:on\s+)?(?:pen|pk|p\.|penalties|penales)", txt, re.I) or \
        re.search(r"(?:pen|penalties|penales|pk)\.?\s*:?\s*(\d{1,2})\s*[-:]\s*(\d{1,2})", txt, re.I)
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


def _jogo(l: str) -> dict | None:
    s = l.strip()
    if not s or s[0] in ".([" or re.match(r"^(nb|note|notes|obs|n\.b\.)\b", s, re.I):
        return None
    if linha_tabela(l):
        return None
    r = _jogo_base(s)
    if r is None and (mf := _JOGO_FIM.match(s)):
        # placar no fim ("Basanez   Rampla Juniors   2-5", "Penarol   v Liverpool   2-0"): volta ao formato de sempre
        r = _jogo_base(f"{mf.group('a')}  {mf.group('p')}  {mf.group('b')}{mf.group('resto') or ''}")
    return r


def _jogo_base(s: str) -> dict | None:
    m = _JOGO.match(s)
    if not m or not m.group("b"):
        return None
    a = m.group("a")
    # data no começo da linha: "Apr 2  Atlanta 3-3 ..." ou "02.04  Atlanta"
    data = None
    md = re.match(r"^\[?((?:[A-Za-z]{3}\s+\d{1,2}|\d{1,2}\s+[A-Za-z]{3}|\d{1,2}[/.]\d{1,2})(?:,?\s+\d{4})?)\]?\s{1,}(.+)$", a)
    if md and achar_data(md.group(1)) and len(md.group(2)) > 2:
        data, a = achar_data(md.group(1)), md.group(2)
    a = _limpa_nome(re.split(r"\s{2,}", a.strip())[-1] if re.search(r"\s{2,}", a.strip()) else a)
    b, nota, local = _separa_b(m.group("b"))
    if a.endswith(":") or "'" in a[-4:]:
        return None   # "Goal: 0-1 58' Kempes."
    if "," in a or re.match(r"^(then|and|but|the match|match)\b", a, re.I) or a[:1].islower():
        return None
    sigla = lambda x: re.fullmatch(r"(?:[A-Z]\.){2,}[A-Z]?\.?", x.strip())   # "U.T.C.", "A.D.T"
    if not a or not b or len(a) > 60 or len(b) > 90 or not (re.search(r"[A-Za-zÀ-ÿ]{2}", a) or sigla(a)) or \
            not (re.search(r"[A-Za-zÀ-ÿ]{2}", b) or sigla(b)):
        return None
    if re.match(r"^(round|fecha|matchday|jornada|group|zona|zone|grupo|first|second|final|semi|quarter)\b", a, re.I) and not m.group("gm"):
        return None
    esp = (m.group("esp") or "").lower().replace(" ", "")
    gm = int(m.group("gm")) if m.group("gm") else None
    gv = int(m.group("gv")) if m.group("gv") else None
    especial = ""
    if esp:
        esp = esp.replace("1p", "lp")   # "wp-1p": erro de digitação da página
        if esp.startswith("fri"):
            return None   # amistoso citado na página
        if esp == "void":
            especial = "anulado"
        elif esp in ("wp-lp", "wp:lp", "w-l", "w:l", "+-", "+:-", "wp-lw", "wp:lw"):
            especial, gm, gv = "wo_m", None, None
        elif esp in ("lp-wp", "lp:wp", "l-w", "l:w", "-+", "-:+", "lw-wp", "lw:wp"):
            especial, gm, gv = "wo_v", None, None
        elif esp.startswith(("abd", "susp")):
            especial = "abd"
        elif esp.startswith(("ann", "canc", "n/p", "p-p", "p:p", "?")):
            especial = "n/p"
        else:
            especial = "awd"
    if m.group("awd_m"):   # "San Lorenzo (MdP)   1-2 awd 1-0   Boca Juniors": placar do tribunal ao lado
        nota = (nota + f" awarded {m.group('awd_m')}-{m.group('awd_v')}").strip()
    if m.group("wl1") or m.group("wl2"):   # "Newell's lp 1:1 wp Huracán": placar em campo, pontos dados pelo tribunal
        especial = "wo_m" if (m.group("wl1") or "").lower() == "wp" or (m.group("wl2") or "").lower() == "lp" else "wo_v"
    resto = (m.group("x") or "") + " " + nota
    pm, pv = _penaltis(resto)
    if m.group("pk_m") and m.group("pk_v"):   # "Boca [4] 0- 0 [2] Lanús ... pso": pênaltis entre colchetes
        pm, pv = int(m.group("pk_m")), int(m.group("pk_v"))
        nota = re.sub(r"^pso,?\s*", "", nota)
    if re.search(r"\bannul", nota, re.I):
        especial = especial or "anulado"
    return {"a": a, "b": b, "gm": gm, "gv": gv, "especial": especial, "nota": nota, "local": local, "data": data,
            "prorrogacao": bool(m.group("x")) or bool(re.search(r"\baet\b|a\.e\.t|extra time", nota, re.I)), "pen_m": pm, "pen_v": pv}


def _autores(l: str) -> str | None:
    """Linha de autores logo abaixo do jogo: "  [Stagnaro, Soria; Gaslini]" ou "  Stagnaro 10, Soria 30; Gaslini 50"."""
    s = l.strip()
    if s.startswith("[") and re.search(r"[A-Za-zÀ-ÿ]{2}", s) and not _linha_de_data(s):
        return s.strip("[] ")
    return None


def _continuacao(linhas: list[str], i: int) -> list[str]:
    """Linhas de baixo que continuam os autores abertos na linha i ("[A 9, B 68;" e "   C 87]"), até a que fecha o colchete
    (no máximo 3). Para em linha vazia, de jogo ou que abre outro colchete; sem o "]", não junta nada (podia ser escalação)."""
    extra = []
    for k in range(i + 1, min(i + 4, len(linhas))):
        t = linhas[k].strip()
        if not t or t.startswith("[") or _jogo(linhas[k]):
            return []
        extra.append(t)
        if "]" in t:
            return extra
    return []


def ler(linhas: list[str], ano_ini: int, ano_fim: int | None = None, fases: list[tuple[str, str]] | None = None,
        ignorar: list[str] | None = None) -> tuple[list[Jogo], list[Tabela]]:
    """Jogos e tabelas de um trecho de página. fases: [(regex do título, nome da fase)]: um título que casa muda a
    fase dos jogos seguintes. ignorar: regex de linhas que não são jogo (ex.: amistosos citados no texto)."""
    ano_fim = ano_fim or ano_ini
    jogos: list[Jogo] = []
    tabelas: list[Tabela] = []
    secao, fase, grupo = "", "", ""
    rodada: int | None = None
    data: str | None = None
    ano = ano_ini
    ultimo_mes: int | None = None
    tab: Tabela | None = None
    ult_jogo: Jogo | None = None
    ult_l = -10

    def fixa_data(md: tuple[int, int, int | None]) -> str | None:
        nonlocal ano, ultimo_mes
        mes, dia, a = md
        if a:
            ano = a
        elif ultimo_mes is not None and ultimo_mes >= 10 and mes <= 3 and ano < ano_fim + 1:
            ano += 1   # virada de ano (dezembro -> janeiro)
        elif ultimo_mes is None and ano_fim > ano_ini and mes <= 6 and not a:
            ano = ano_fim   # temporada que cruza o ano e começa a página já no ano seguinte
        ultimo_mes = mes
        try:
            return f"{ano:04d}-{mes:02d}-{dia:02d}" if 1 <= dia <= 31 else None
        except ValueError:
            return None

    pular: set[int] = set()   # linhas de continuação dos autores, já juntadas à linha de cima
    for i, l in enumerate(linhas):
        if i in pular:
            continue
        s = l.strip()
        if not s:
            tab = None
            continue
        if ignorar and any(re.search(p, s, re.I) for p in ignorar):
            continue
        r = linha_tabela(l)
        if r:
            if tab is None or (tabelas and tabelas[-1] is not tab):
                tab = Tabela(i, secao, fase, grupo=grupo)
                tabelas.append(tab)
            tab.linhas.append(r)
            continue
        if tab is not None and re.match(r"^[-=_\s]+$", s):
            continue   # traço dentro da tabela
        tab = None
        if ult_jogo is not None and s.startswith("[") and (i - ult_l) <= 2:
            if _NOTA_KW.search(s):
                ult_jogo.nota = (ult_jogo.nota + " " + s.strip("[] ")).strip()
                ult_l = i
                continue
            if (a := _autores(l)):
                if "]" not in s:   # o colchete continua nas linhas de baixo ("[A 9, B 68;" + "   C 87]")
                    extra = _continuacao(linhas, i)
                    if extra:
                        a = (a + " " + " ".join(extra)).split("]")[0].strip()
                        pular.update(range(i + 1, i + 1 + len(extra)))
                ult_jogo.gols_texto = (ult_jogo.gols_texto + " " + a).strip()
                ult_l = i
                continue
        if fases:
            for rx, nome_fase in fases:
                if re.search(rx, s, re.I):
                    if nome_fase == "Desempate do título" and fase.startswith("Desempate") and re.match(r"^(First|Second|Third)? ?(leg|playoff)|^Playoff", s, re.I):
                        break   # "Playoff [Dec 10]" dentro dos desempates do 2º lugar: segue a mesma fase
                    if nome_fase != fase:
                        grupo = ""
                    fase = nome_fase
                    break
        # data entre colchetes no título da fase ou do jogo de ida e volta ("Final [Dec 23]:", "First Leg [Jul 29]",
        # "Semifinals [Jun 28]"): vale para os jogos de baixo (antes eles herdavam a data do último jogo da liga; AR-023,
        # UY-014, CH-012, CO-008, PY-009, PE-009, EC-009, 23/11/2026)
        if len(s) < 70 and not s.startswith(("[", "NB", "(")) and not _jogo(l) and \
                (mt := _DATA_TITULO.search(s)) and (md := achar_data(mt.group(1))):
            data = fixa_data(md)
        mg = _GRUPO.match(s)
        if mg:
            grupo = "Interzonal" if mg.group("inter") else mg.group("g").upper()
            if fase in _MATA_MATA or fase == "Fase final":
                fase = ""   # "Group A" depois do resumo do mata-mata no topo da página: volta à fase de grupos
            continue
        mr = _RODADA.match(s)
        if mr:
            rodada = int(mr.group("n1") or mr.group("n2"))
            resto = mr.group("resto") or ""
            # "Round 3. 1: Championship playoff - 1st. leg." muda a fase; rodada nova depois de um desempate volta à fase de liga
            nova = next((nf for rx, nf in (fases or []) if re.search(rx, re.sub(r"^[\s.\d:]+", "", resto), re.I)), None)
            if nova:
                fase = nova
            elif fase.startswith("Desempate"):
                fase = ""
            md = achar_data(resto)
            data = fixa_data(md) if md else None
            # "Round 1: 16 Aug  Atlanta 3-3 Boca" (jogo na mesma linha) não acontece; segue
            continue
        if _linha_de_data(s):
            md = achar_data(s)
            data = fixa_data(md) if md else data
            continue
        j = _jogo(l)
        if j:
            d = fixa_data(j["data"]) if j["data"] else data
            ult_jogo = Jogo(i, j["a"], j["b"], j["gm"], j["gv"], rodada, d, secao, fase, grupo, j["especial"], j["nota"], j["local"],
                            pen_m=j["pen_m"], pen_v=j["pen_v"], prorrogacao=j["prorrogacao"], texto=s)
            jogos.append(ult_jogo)
            ult_l = i
            continue
        # outra linha: título de seção (curto) ou texto
        if len(s) < 100 and not s.startswith("."):
            secao = s
            if re.search(r"(round|fecha|jornada)\b", s, re.I) is None:
                rodada = rodada if re.match(r"^\[", s) else rodada
        ult_jogo = None
    for j in jogos:
        oficial(j)
    _continuados(jogos)
    return [j for j in jogos if j.especial != "duplicado"], tabelas


def _continuados(jogos: list[Jogo]) -> None:
    """Jogo suspenso e continuado depois aparece duas vezes na página: fica a linha da continuação (placar final),
    com a nota da suspensão; a primeira vira "duplicado" e sai."""
    for i, j in enumerate(jogos):
        if not re.search(r"suspend|interrupt|abandon", j.nota, re.I) or j.gm_of is not None:
            continue
        continuado = re.search(r"continu|resum|complet|finished on|played on", j.nota, re.I)
        for k in jogos[i + 1:i + 400]:
            if k.mandante == j.mandante and k.visitante == j.visitante and k.especial != "duplicado":
                if continuado:   # a segunda linha traz o placar final do mesmo jogo
                    k.nota = (j.nota + "; " + k.nota).strip("; ")
                    k.gols_texto = k.gols_texto or j.gols_texto
                    j.especial = "duplicado"
                else:            # suspenso e jogado de novo: o primeiro fica como abandonado, sem valer
                    j.especial = "abd"
                    k.nota = (k.nota + "; jogo repetido (o primeiro foi suspenso)").strip("; ")
                break


_MATA_MATA = {"Oitavas de final", "Quartas de final", "Semifinal", "Final", "Desempate do título", "Desempate do 2º lugar",
              "Desempate do rebaixamento"}
_NOTA_KW = re.compile(r"suspend|abandon|award|won the points|annul|not played|replay|forfeit|walk ?over|deducted|lost the points|"
                      r"interrupt|continued|postponed|finished at|played (at|on)|was given", re.I)


def oficial(j: Jogo) -> None:
    """Placar oficial a partir da nota: "Awarded 2-0", "won the points (0-1)", "awarded 1-0 to X". Na ordem mandante-visitante.
    Sem placar: "awarded wp-lp" e "X lost the points" viram W.O. (vitória sem gols, como a tabela conta);
    "Suspended ...; not continued" sem decisão: vale o placar do momento (é o que as tabelas dos anos 1990 contam)."""
    m = re.search(r"awarded\s*\(?(wp\s*[-:]\s*lp|lp\s*[-:]\s*wp)", j.nota, re.I)
    if m:
        j.especial = "wo_m" if m.group(1).lower().startswith("wp") else "wo_v"
        return
    m = re.search(r"(?:awarded|won the points|points? (?:were )?given|result(?:ed)? (?:as|in)|declared)\D{0,30}?\(?(\d{1,2})\s*[-:]\s*(\d{1,2})\)?",
                  j.nota, re.I)
    if m:
        j.gm_of, j.gv_of = int(m.group(1)), int(m.group(2))
        if not j.especial:
            j.especial = "awd"
        return
    for rx, perdeu in ((r"([A-Z][\w'.() -]{2,40}?)\s+lost the points", True), (r"([A-Z][\w'.() -]{2,40}?)\s+won (?:the )?points", False)):
        m = re.search(rx, j.nota)
        if m:
            quem = chave(m.group(1)).split()[-1] if not perdeu else chave(m.group(1)).split()[0]
            casa, fora = quem and quem in chave(j.mandante).split(), quem and quem in chave(j.visitante).split()
            if casa != fora:
                j.especial = ("wo_v" if casa else "wo_m") if perdeu else ("wo_m" if casa else "wo_v")
                return
    # abandonado, mas o placar do momento foi mantido: "[abandoned at 2-3 in 81'] [score allowed to stand]"
    m = re.search(r"abandoned at (\d{1,2})\s*[-:]\s*(\d{1,2})", j.nota, re.I)
    if m and re.search(r"(score|result)\s+(was\s+)?(allowed to stand|stood|stands|confirmed|maintained|validated|kept)", j.nota, re.I):
        if j.gm is None:
            j.gm, j.gv = int(m.group(1)), int(m.group(2))
        j.gm_of, j.gv_of = int(m.group(1)), int(m.group(2))
