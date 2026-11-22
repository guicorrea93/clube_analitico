"""Jogos e tabelas da Wikipédia em português para as edições da A2 que a RSSSF não traz completas.

Fonte: as páginas "Campeonato Paulista de Futebol de {ano} - {divisão}" (código-fonte em data/coleta/bra-sp-2/wikipedia/
pt_{ano}.wiki) e a transcrição dos jogos delas em jogos_pt.csv (ano;pagina;secao;data;mandante;gols_mandante;
gols_visitante;visitante;nota). Cada jogo do CSV com placar foi conferido no código da página (os dois clubes e o placar
no mesmo trecho): 244 de 244. Jogos só com o resultado ("V"/"E"/"D", sem placar) ficam fora.

Uso: python coleta/bra-sp-2/wikipedia_sp2.py [ano ...]     (lista os jogos lidos)
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from edicoes import PASTA_DADOS  # noqa: E402

PASTA = PASTA_DADOS / "wikipedia"
MESES = {m: i for i, m in enumerate(["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro",
                                     "outubro", "novembro", "dezembro"], 1)}

# (temporada, seção da página) -> (fase, grupo); None: o jogo fica fora
FASE: dict[tuple[str, str], tuple[str, str] | None] = {
    ("1948", "Série Vermelha"): ("Primeira fase - Desempate", "Série Vermelha"),   # Rio Pardo x São Caetano, 1º lugar
    ("1948", "Triangular final"): ("Segunda fase", ""),
    ("1949", "Primeiro turno"): ("Segunda fase", ""), ("1949", "Segundo turno"): ("Segunda fase", ""),
    ("1949", "Jogo de desempate"): ("Final", ""),   # Guarani x Batatais, empatados no Torneio dos Campeões
    # 1951: XV de Jaú x Jabaquara (o último da 1ª divisão), repescagem entre as divisões: não é jogo da A2
    ("1951", "Primeiro jogo"): None, ("1951", "Segundo jogo"): None, ("1951", "Terceiro jogo"): None,
    ("1953", "Primeiro turno"): ("Segunda fase", ""), ("1953", "Segundo turno"): ("Segunda fase", ""),
    ("1954", "Primeiro turno"): ("Segunda fase", ""), ("1954", "Segundo turno"): ("Segunda fase", ""),
    ("1955", "Penúltima partida da fase final"): ("Segunda fase", ""),
    ("1957", 'Última rodada do "Torneio dos Finalistas"'): ("Segunda fase", ""),
    ("1959", "Resultados da fase final"): ("Segunda fase", ""), ("1959", "Jogo decisivo"): ("Segunda fase", ""),
    ("1960", "Jogo decisivo"): ("Primeira fase", ""),   # última rodada do turno e returno
    ("1962", "1º jogo"): ("Final", ""), ("1962", "2º jogo"): ("Final", ""), ("1962", "3º jogo"): ("Final", ""),
    ("1963", "Jogos decisivos"): ("Segunda fase", ""), ("1964", "Forma de disputa"): ("Segunda fase", ""),
    # 1988: a final já está na RSSSF
    ("1988", "Jogo de ida"): None, ("1988", "Jogo de volta"): None,
    ("1990", "Quarta fase"): ("Quarta fase", ""),
    ("1992", "Grupo E"): ("Segunda fase", "Grupo E"), ("1992", "Grupo F"): ("Segunda fase", "Grupo F"),
    ("1992", "Grupo G"): ("Segunda fase", "Grupo G"), ("1992", "Quadrangular final"): ("Fase final", ""),
}
PADRAO = {"Final": ("Final", ""), "Semifinal": ("Semifinal", "")}


def _data(txt: str, temporada: str) -> str | None:
    """"Domingo, 27 de janeiro de 1952", "4 de outubro" (o ano da edição), "01/12/1990" -> "AAAA-MM-DD"."""
    t = re.sub(r"^[^\d]*,\s*", "", (txt or "").strip())
    if m := re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})$", t):
        d, mes, a = int(m.group(1)), int(m.group(2)), int(m.group(3))
        a = a if a >= 1940 else int(temporada)   # "01/12/1900" na página de 1990
        return f"{a:04d}-{mes:02d}-{d:02d}"
    if m := re.match(r"(\d{1,2})\s+de\s+([a-zç]+)(?:\s+de\s+(\d{4}))?$", t, re.I):
        mes = MESES.get(m.group(2).lower())
        if mes:
            return f"{int(m.group(3) or temporada):04d}-{mes:02d}-{int(m.group(1)):02d}"
    return None


def jogos(temporada: str) -> list[dict]:
    """Jogos com placar da temporada: {fase, grupo, data, mandante, visitante, gm, gv, secao, linha, nota}."""
    saida = []
    with open(PASTA / "jogos_pt.csv", encoding="utf-8") as f:
        for i, r in enumerate(csv.DictReader(f, delimiter=";"), 2):
            if r["ano"] != temporada:
                continue
            gm, gv = r["gols_mandante"].strip(), r["gols_visitante"].strip()
            if m := re.match(r"(\d+)\s*[—–-]\s*(\d+)$", gm):   # "2 — 1" numa coluna só
                gm, gv = m.groups()
            if not (gm.isdigit() and gv.isdigit()):
                continue
            chave = (temporada, r["secao"])
            if chave in FASE and FASE[chave] is None:
                continue
            fase, grupo = FASE.get(chave) or PADRAO.get(r["secao"]) or (r["secao"], "")
            saida.append({"fase": fase, "grupo": grupo, "data": _data(r["data"], temporada), "mandante": r["mandante"].strip(),
                          "visitante": r["visitante"].strip(), "gm": int(gm), "gv": int(gv), "secao": r["secao"], "linha": i,
                          "nota": r.get("nota") or ""})
    return saida


def sem_placar(temporada: str) -> int:
    """Quantos jogos da temporada a página traz só com o resultado (sem placar)."""
    with open(PASTA / "jogos_pt.csv", encoding="utf-8") as f:
        return sum(1 for r in csv.DictReader(f, delimiter=";") if r["ano"] == temporada
                   and not re.match(r"\d", r["gols_mandante"].strip()))


def _limpa(t: str) -> str:
    t = re.sub(r"\[\[(?:File|Ficheiro|Imagem|Image):[^\]]*\]\]", " ", t)
    t = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", t)
    t = re.sub(r"\[\[([^\]]*)\]\]", r"\1", t)
    return re.sub(r"<[^>]+>", "", t)


def tabelas_1965() -> list[tuple[str, list[dict]]]:
    """1965 (a RSSSF não tem a página): os dois grupos da 1ª fase com os pontos. Cada clube vem em três linhas da tabela:
    "!...|<font>1</font>", "|bgcolor=...| [[...|Bragantino]] (Bragança Paulista)" e "|bgcolor=... align="center"|26"."""
    saida: list[tuple[str, list[dict]]] = []
    pos = None
    linha: dict | None = None
    for l in (PASTA / "pt_1965.wiki").read_text(encoding="utf-8").splitlines():
        if m := re.search(r'colspan="\d+".*?>(Série [^<|]+)', l):
            saida.append((m.group(1).strip(), []))
            continue
        if not saida:
            continue
        if m := re.match(r"^!.*>(\d+)</font>\s*$", l):
            pos = int(m.group(1))
        elif m := re.match(r'^\|bgcolor=[^|]*align="center"\|\s*(\d+)', l):
            if linha:
                linha["pts"] = int(m.group(1))
                saida[-1][1].append(linha)
                linha = None
        elif m := re.match(r'^\|bgcolor=[^|]*\|\s*(.+?)\s*$', l):
            txt = _limpa(m.group(1)).strip()
            mc = re.match(r"^(.*?)\s*\(([^()]+)\)$", txt)
            linha = {"pos": pos, "nome": mc.group(1) if mc else txt, "cidade": mc.group(2) if mc else None, "pts": None, "nota": ""}
    return [(g, ls) for g, ls in saida if ls]


def participantes(temporada: str) -> list[tuple[str, str]]:
    """Lista de participantes da página ("* [[Associação Esportiva Araçatuba|Araçatuba]] (Araçatuba)")."""
    saida = []
    for l in (PASTA / f"pt_{temporada}.wiki").read_text(encoding="utf-8").splitlines():
        if (m := re.match(r"^\*\s*(.+?)\s*\(([^()]+)\)\s*$", _limpa(l))) and not re.match(r"\d", m.group(1)):
            saida.append((m.group(1).strip(), m.group(2).strip()))
    return saida


def classificacao_publicada(temporada: str) -> list[dict]:
    """Classificação final publicada na página ("* 1.º) Olímpia – 13 pontos (acesso)", 1990: a 4ª fase)."""
    saida = []
    for l in (PASTA / f"pt_{temporada}.wiki").read_text(encoding="utf-8").splitlines():
        if m := re.match(r"^\*\s*(\d+)\.?º\)\s*(.+?)\s*[–-]\s*(\d+)\s*pontos?\s*(?:\(([^()]*)\))?", _limpa(l)):
            saida.append({"pos": int(m.group(1)), "nome": m.group(2).strip(), "cidade": None, "pts": int(m.group(3)),
                          "nota": (m.group(4) or "").strip()})
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for a in sys.argv[1:] or sorted({r["ano"] for r in csv.DictReader(open(PASTA / "jogos_pt.csv", encoding="utf-8"), delimiter=";")}):
        js = jogos(a)
        print(f"== {a}: {len(js)} jogos com placar, {sem_placar(a)} sem placar")
        for j in js:
            print(f"   {j['fase']:28} {j['grupo']:15} {j['data']} {j['mandante']} {j['gm']}-{j['gv']} {j['visitante']}")
