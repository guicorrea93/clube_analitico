"""Edições da A2 sem os jogos (1947-1966, 1992-1994): as tabelas de pontos das páginas da RSSSF.

Nesses anos a página traz a classificação de cada fase e grupo (quase sempre só os pontos; em 1954, 1963 e 1994 a tabela
completa), às vezes só a ordem final (1992 e 1993), e os jogos soltos (os do campeão, finais e desempates).
Daqui saem as tabelas publicadas; a classificação final é montada no importador.

Uso: python coleta/bra-sp-2/antigas_sp2.py [ano ...]     (lista as tabelas lidas)
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(AQUI.parent / "comum"))
import rsssf_sp2  # noqa: E402,F401  (configura rsssf.PASTA e rsssf.MODELO da A2)
import rsssf  # noqa: E402

# 1967-1978 e 1980-1984 (achado A2-001): participantes da lista da RSSSF (sp2list.htm), tabelas e jogos da Wikipédia em
# português e o pódio da predefinição de campeões da Wikipédia; 1972 não tem página na Wikipédia
NOVAS = [str(a) for a in (*range(1967, 1979), *range(1980, 1985))]
ANOS = [str(a) for a in (*range(1947, 1967), 1990, 1992, 1993, 1994)] + NOVAS   # 1965 e 1990: só a Wikipédia


@dataclass
class Tabela:
    fase: str
    grupo: str
    linhas: list[dict] = field(default_factory=list)   # pos, nome, cidade, pts, j, v, e, d, gp, gc, nota
    publicada: bool = True   # False: só a lista de participantes (sem posição nem pontos), fora de tabelas_publicadas
    fonte: str = "RSSSF"


FASES = [(r"^first phase", "Primeira fase"), (r"^second phase", "Segunda fase"), (r"^final phase", "Fase final"),
         (r"^tie-?break", "Desempate"), (r"^final\b", "Final"), (r"^classifica[çc][ãa]o final", "Classificação final")]
GRUPO = re.compile(r"^\s*((?:série|serie|grupo|group|zona|setor)\b.*|(?:primeira|segunda|terceira|quarta|quinta) (?:região|série))\s*$", re.I)
# fim da parte das tabelas: jogos do campeão, resultados soltos, rodapé
FIM = re.compile(r"(?i)^\s*(matches of the (winner|champion)|known results|topscorer|overall topscorer|\d{4} \((1st|2nd|3rd)|list of)")
NOTA = re.compile(r"\((qualified|champions?|classified|campeão|promoted)\)|\b(licensed|abandoned)\b", re.I)
# tabela completa: "1. Taubaté  16  10  7  2  1  27  12  15  champions" (P J V E D GP GC SG; 1963 com "30-16")
COMPLETA = re.compile(r"^\s*(\d{1,2})\.\s*(\D+?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*[-\s]\s*(\d+)\s+-?\d+\s*(.*)$")
# linha de pontos: "1º) Batatais FC (Batatais)   31 (qualified)", "  Francana   19", "1º EC XV de Novembro (Piracicaba).... 38 pts"
PONTOS = re.compile(r"^\s*(?:(\d{1,2})\s*(?:º\)?|°|\)|\.)?\s+)?([A-Za-zÀ-ÿ\"'][^\d]*?)[\s.]*(?<=[\s.)])(\d{1,2})\s*(?:pts?\b|pontos)?\s*(\(.*\))?\s*$")
SEM_PONTOS = re.compile(r"^\s*(?:(\d{1,2})\s*(?:º\)?|°|\)|\.)?\s+)?([A-Za-zÀ-ÿ\"'][^\d]*?)[\s.]*\s(licensed|abandoned)\s*$")


def _fase(l: str) -> str | None:
    t = l.strip().lower()
    for padrao, fase in FASES:
        if re.match(padrao, t):
            return fase
    return None


def _nome_e_cidade(txt: str) -> tuple[str, str | None]:
    """"EC XV de Novembro (Piracicaba)" -> ("EC XV de Novembro", "Piracicaba"); "XV Piracicaba (Campeão)" -> ("XV Piracicaba", None)."""
    txt = re.sub(r"\((campeão|champions?)\)", "", txt, flags=re.I).strip(" .")
    m = re.match(r"^(.*?)\s*\(([^()]+)\)\s*$", txt)
    if m:
        return m.group(1).strip(" ."), m.group(2).strip()
    return txt.strip(" ."), None


def tabelas(ano: str) -> list[Tabela]:
    if ano in ("1992", "1993"):
        return _ordem_final(ano)
    if ano in ("1965", "1990"):
        return _da_wikipedia(ano)
    if ano in NOVAS:
        return _novas(ano)
    saida = _da_rsssf(ano)
    if not any(tb.fase == "Segunda fase" for tb in saida):   # 1948 e 1949: a "Final Phase" é a 2ª fase
        for tb in saida:
            if tb.fase == "Fase final":
                tb.fase = "Segunda fase"
    return saida


def _da_wikipedia(ano: str) -> list[Tabela]:
    """1965: os dois grupos da 1ª fase com os pontos; 1990: a lista de participantes e a classificação da 4ª fase."""
    import wikipedia_sp2
    if ano == "1965":
        return [Tabela("Primeira fase", g, ls, fonte="Wikipédia (pt)") for g, ls in wikipedia_sp2.tabelas_1965()]
    part = [{"pos": None, "nome": n, "cidade": c, "pts": None, "nota": ""} for n, c in wikipedia_sp2.participantes(ano)]
    return [Tabela("Primeira fase", "", part, publicada=False, fonte="Wikipédia (pt)"),
            Tabela("Quarta fase", "", wikipedia_sp2.classificacao_publicada(ano), fonte="Wikipédia (pt)")]



# (temporada, seção, título) da tabela da Wikipédia -> (fase, grupo), quando a regra de _fase_tabela não acerta
TABELA_FASE: dict[tuple[str, str, str], tuple[str, str]] = {
    ("1967", "Fase final", "Torneio dos Finalistas"): ("Segunda fase", ""),   # os 4 finalistas; depois, o triangular
    ("1967", "Triangular decisivo", "Classificação Final"): ("Fase final", ""),
    ("1968", "Participantes", "Classificação final da série A / Grupo A"): ("Primeira fase", "Série A"),
    ("1968", "Participantes", "Classificação final da série B / Grupo A"): ("Primeira fase", "Série B"),
    ("1971", "Fase semifinal", "Grupo A"): ("Segunda fase", ""),
    ("1971", "Fase final / Classificação final", "Grupo A"): ("Fase final", ""),
    ("1977", "Fase final", "Grupo dos Perdedores"): ("Segunda fase", "Grupo dos Perdedores"),   # o "torneio da morte"
    ("1977", "Fase final", "Grupo dos Vencedores"): ("Fase final", ""),
    ("1982", "Fase final", "Grupo A"): ("Fase final", ""),
}


def _fase_tabela(ano: str, secao: str, titulo: str) -> tuple[str, str]:
    if (ano, secao, titulo) in TABELA_FASE:
        return TABELA_FASE[(ano, secao, titulo)]
    s, tt = secao.lower(), titulo.lower()
    if re.search(r"quadrangular|hexagonal|triangular|finalistas", tt):
        return "Fase final", ""
    # 1981: dois turnos, cada um com a 1ª fase (quatro séries) e o octogonal (dois grupos)
    turno = "1º turno - " if s.startswith("primeiro turno") else "2º turno - " if s.startswith("segundo turno") else ""
    if "primeira fase" in s:
        return "Primeira fase", turno + titulo
    if "segunda fase" in s:
        return "Segunda fase", turno + titulo
    if "final" in s:
        return "Fase final", ""
    raise ValueError(f"{ano}: tabela da Wikipédia sem fase: [{secao}] {titulo}")


def _curto_da_lista(n: str) -> str:
    """"Associação Atlética FRANCANA" -> "Francana"; "UNIÃO Agrícola BARBARENSE Futebol Clube" -> "União Barbarense";
    "Esporte Clube XV DE NOVEMBRO" -> "XV de Novembro" (a lista da RSSSF escreve o nome curto em maiúsculas)."""
    caps = re.findall(r"(?<![\wÀ-ÿ])[A-ZÀ-Ý0-9][A-ZÀ-Ý0-9´'\-]+(?![\wÀ-ÿ])", n)
    if not caps:
        return n
    def palavra(w):
        if re.fullmatch(r"[IVXL]+", w) or w in ("MAF",):   # algarismos romanos e siglas
            return w
        return w.lower() if w in ("DE", "DA", "DO", "DOS", "DAS") else w.capitalize()
    return " ".join(palavra(w) for w in caps)


def _participantes_rsssf(ano: str) -> list[dict]:
    saida, atual = [], None
    for l in rsssf.texto(0, "sp2list.htm").splitlines():
        if re.fullmatch(r"\s*(\d{4})\s*", l):
            atual = l.strip()
        elif atual == ano and (m := re.match(r"^\s*([^()]+?)\s*\(([^()]+)\)\s*$", l)):
            saida.append({"pos": None, "nome": _curto_da_lista(m.group(1).strip()), "cidade": m.group(2).strip(), "pts": None,
                          "nota": ""})
    return saida


def _novas(ano: str) -> list[Tabela]:
    """1967-1984: as tabelas da Wikipédia, cada uma com a sua fase; sem tabela da 1ª fase, a lista de participantes da
    RSSSF entra como 1ª fase (sem posição nem pontos, fora de tabelas_publicadas)."""
    import wikipedia_sp2
    saida: list[Tabela] = []
    for tw in wikipedia_sp2.tabelas_wiki(ano):
        fase, grupo = _fase_tabela(ano, tw["secao"], tw["titulo"])
        linhas = []
        for r in tw["linhas"]:
            r = dict(r)
            if r["nome"] and r["nome"].endswith("*"):   # "União Barbarense*": a nota da tabela
                r["nome"], r["nota"] = r["nome"].rstrip("* "), (r.get("nota") or "") + "*"
            linhas.append(r)
        saida.append(Tabela(fase, grupo, linhas, fonte="Wikipédia (pt)"))
    if not any(tb.fase == "Primeira fase" for tb in saida):
        saida.insert(0, Tabela("Primeira fase", "", _participantes_rsssf(ano), publicada=False, fonte="RSSSF (sp2list.htm)"))
    # a 1ª fase antes (os clubes das fases seguintes casam com os dela; em 1968 a tabela da fase final vem antes na página)
    ordem = {"Primeira fase": 0, "Segunda fase": 1, "Fase final": 2}
    return sorted(saida, key=lambda tb: ordem.get(tb.fase, 1))


def _da_rsssf(ano: str) -> list[Tabela]:
    t = rsssf.texto(int(ano))
    saida: list[Tabela] = []
    fase, grupo, atual, pos_ant = "Primeira fase", "", None, 0
    comecou = False
    for l in t.splitlines():
        if not l.strip():
            continue
        if re.search(r"(?i)second level|2nd level", l):
            comecou = True
            continue
        if not comecou:
            continue
        if FIM.match(l):
            if re.match(r"(?i)^\s*(matches of the|\d{4} \(|list of)", l):
                break
            continue
        if (f := _fase(l)) and not re.search(r"\d\s*-\s*\d", l):
            fase, grupo, atual = f, "", None
            continue
        if GRUPO.match(l) and not re.search(r"\d{2}", l):
            grupo, atual = GRUPO.match(l).group(1).replace('"', "").strip(), None
            continue
        m = COMPLETA.match(l)
        if m:
            nome, cidade = _nome_e_cidade(m.group(2))
            linha = {"pos": int(m.group(1)), "nome": nome, "cidade": cidade, "pts": int(m.group(3)), "j": int(m.group(4)),
                     "v": int(m.group(5)), "e": int(m.group(6)), "d": int(m.group(7)), "gp": int(m.group(8)), "gc": int(m.group(9)),
                     "nota": m.group(10).strip()}
        elif (m := PONTOS.match(l)) or (m := SEM_PONTOS.match(l)):
            nome, cidade = _nome_e_cidade(m.group(2))
            if re.search(r"(?i)\b(qualified|after|won|wins|played|decided|was|were|ended|draw)\b", nome) or len(nome) > 60:
                continue
            pts = int(m.group(3)) if m.group(3).isdigit() else None
            linha = {"pos": int(m.group(1)) if m.group(1) else None, "nome": nome, "cidade": cidade, "pts": pts,
                     "nota": (m.group(4) or "").strip("() ") if pts is not None else m.group(3)}
        else:
            continue
        # a mesma fase e grupo de novo, a partir do 1º (1954: a tabela calculada dos jogos da 2ª fase e depois a
        # classificação oficial, com outros pontos): fica a última
        recomeca = atual is not None and linha["pos"] == 1 and pos_ant > 1
        if atual is None or (atual.fase, atual.grupo) != (fase, grupo) or recomeca:
            saida = [x for x in saida if (x.fase, x.grupo) != (fase, grupo)]
            atual = Tabela(fase, grupo)
            saida.append(atual)
            pos_ant = 0
        linha["pos"] = linha["pos"] or pos_ant   # empatado: a linha sem número fica com a posição de cima
        pos_ant = linha["pos"]
        atual.linhas.append(linha)
    return saida


def _ordem_final(ano: str) -> list[Tabela]:
    """1992 e 1993: só a ordem final, por fase alcançada ("Eliminados na Segunda Fase (5º a 12º)"); dentro da faixa a página
    não dá a ordem (lista em ordem alfabética), e todos ficam com a posição do começo da faixa."""
    t = rsssf.texto(int(ano))
    tb = Tabela("Classificação final", "")
    pos_faixa, comecou = None, False
    for l in t.splitlines():
        if re.search(r"(?i)classifica[çc][ãa]o final", l):
            comecou = True
            continue
        if not comecou or not l.strip():
            continue
        if re.match(r"(?i)^\s*(\d{4} \(|list of)", l):
            break
        if m := re.search(r"\((\d+)º (?:a|e) \d+º\)", l):
            pos_faixa = int(m.group(1))
            continue
        if re.match(r"(?i)^\s*(participantes|promovidos|eliminados|não disputou|nenhum|com a mudança|clubes foram|equivalente)", l):
            if re.match(r"(?i)^\s*não disputou", l):
                pos_faixa = None
            continue
        m = re.match(r"^\s*(?:(\d{1,2})º\s+)?([A-Za-zÀ-ÿ][^()]*?)\s*\(([^()]+)\)\s*(?:-\s*(.*))?$", l)
        if not m:
            continue
        if pos_faixa is None and not m.group(1):
            continue
        if m.group(1) and pos_faixa is None and int(m.group(1)) > 20:   # "28º Capivariano" sob "Não disputou"
            continue
        tb.linhas.append({"pos": int(m.group(1)) if m.group(1) else pos_faixa, "nome": m.group(2).strip(), "cidade": m.group(3).strip(),
                          "pts": None, "nota": (m.group(4) or "").strip(), "faixa": not m.group(1)})
    return [tb]


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for a in sys.argv[1:] or ANOS:
        tbs = tabelas(a)
        print(f"== {a}: {len(tbs)} tabelas, {sum(len(x.linhas) for x in tbs)} linhas")
        for tb in tbs:
            print(f"   [{tb.fase} | {tb.grupo}] " + "; ".join(
                f"{r['pos']} {r['nome']}{' (' + r['cidade'] + ')' if r['cidade'] else ''} {r['pts'] if r['pts'] is not None else '-'}"
                + (f" [{r['nota']}]" if r.get("nota") else "") for r in tb.linhas))
