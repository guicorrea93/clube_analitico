"""Observação dos jogos em português, a partir das notas da RSSSF (revisão SD-009 e CB-015), e pênaltis que só
estão na nota (revisão CB-008).

Uso: obs_pt(texto) -> texto limpo; penaltis_da_nota(texto, mandante, visitante) -> (pen_mandante, pen_visitante) ou None.
"""
from __future__ import annotations

import re
import unicodedata

MESES_EN = {m: i for i, m in enumerate("january february march april may june july august september october november december".split(), 1)}


def _chave(s: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()).strip()


def penaltis_da_nota(nota: str, mandante: str, visitante: str) -> tuple[int, int] | None:
    """Pênaltis escritos só na nota: "Pen 5-4" / "pen. 3-2" / "[pen 4-3]" (mandante-visitante) e "Rio Negro 4-3 on pen" /
    "5-3 pen" (placar do vencedor, quando ele é nomeado; sem nome, mandante-visitante)."""
    t = nota or ""
    m = re.search(r"(?:^|[\[\s;(])(?P<quem>[^\[\];()]*?)\s*(?P<a>\d+)\s*-\s*(?P<b>\d+)\s*on pen", t, re.I)
    if m:
        a, b, quem = int(m["a"]), int(m["b"]), _chave(m["quem"])
        if quem and (quem in _chave(visitante) or _chave(visitante)[:5] in quem):
            return min(a, b), max(a, b)
        if quem and (quem in _chave(mandante) or _chave(mandante)[:5] in quem):
            return max(a, b), min(a, b)
        return a, b
    m = re.search(r"\bpen(?:alties|\.)?\s*:?\s*(\d+)\s*-\s*(\d+)|(\d+)\s*-\s*(\d+)\s*pen\b", t, re.I)
    if m:
        a, b = (m[1], m[2]) if m[1] else (m[3], m[4])
        return int(a), int(b)
    return None


# notas da RSSSF que seguiam em inglês (achado QC-007): regex do pedaço inteiro -> português
TRADUCOES: list[tuple[str, str]] = [
    (r"2nd match in (.+)", r"2º jogo em \1"),
    (r"walkover awarded (\d+-\d+)", r"W.O. (resultado \1)"),
    (r"awarded (\d+-\d+)", r"resultado \1 dado no tribunal"),
    (r"originally (\d+-\d+), awarded (\d+-\d+)\s*\(ineligible (.+?) player (.+)\)",
     r"resultado \2 dado no tribunal (o jogo terminou \1; o \3 escalou jogador irregular, \4)"),
    (r"originally (\d+-\d+), awarded (\d+-\d+)", r"resultado \2 dado no tribunal (o jogo terminou \1)"),
    # a nota vem quebrada entre duas colunas da página: "... after River's had 2 players sent off and 3 alleging injuries"
    (r"abandoned at 73' after River's had 2", "encerrado aos 73 min: o River ficou com 2 expulsos e 3 alegando contusão"),
    (r"abandoned after 5 players\s+from (.+) were sent off", r"encerrado depois de 5 expulsões do \1"),
    (r"1st leg abandoned at (\d+)', result stood", r"jogo de ida encerrado aos \1 min; resultado mantido"),
    (r"(.+) forfeited, awarded (\d+-\d+)", r"W.O. do \1 (resultado \2)"),
    (r"abandoned at (\d+)' \((.+) with less than 7 players\), (.+) winning (\d+-\d+)",
     r"encerrado aos \1 min (\2 com menos de 7 jogadores), com o \3 vencendo por \4"),
    (r"abandoned at (\d+), (\d+-\d+) result stood", r"encerrado aos \1 min; resultado \2 mantido"),
    (r"2nd leg abd at (\d+-\d+) to (.+) in (\d+)'", r"jogo de volta encerrado aos \3 min com \1 para o \2"),
    # Paulista A2 (o mesmo tradutor)
    (r"abandoned at (\d+-\d+) due to pitch invasion, awarded (\d+-\d+)",
     r"encerrado com \1 por invasão de campo; resultado \2 dado no tribunal"),
    (r"awarded (\d+-\d+), originally (\d+-\d+)", r"resultado \1 dado no tribunal (o jogo terminou \2)"),
    (r"points awarded to (.+)", r"pontos dados ao \1"),
    (r"match interrupted at (\d+) minutes", r"jogo interrompido aos \1 min"),
    (r"match suspended", "jogo suspenso"),
    (r"suspended at (\d+)'", r"suspenso aos \1 min"),
    (r"result apparently stood", "resultado aparentemente mantido"),
]


def limpar_gols_texto(texto: str) -> str:
    """Autores dos gols sem as notas de rodapé que a página cola no último jogo do bloco ("[c] 2nd match played in Porto
    Alegre", "(*) ALL Baré players...", "- The 6 bye clubs..."; achado QC-007): fica só o colchete dos autores."""
    t = (texto or "").strip()
    if re.match(r"^\[[a-z*]\]", t):   # só a nota, sem autores
        return ""
    m = re.search(r"\s(?:\[[a-z*]\]|\(\*\)|- [A-Z])", t)
    if m:
        t = t[:m.start()].strip()
        if t.startswith("[") and t.count("[") > t.count("]"):
            t += "]"
    return t


def obs_pt(texto: str) -> str:
    """Nota crua da RSSSF -> observação em português. Os pênaltis saem (estão nos campos próprios); números soltos saem."""
    partes = []
    pedacos = re.split(r";|\]\s*\[|\]\s+\(|\]", texto or "")
    tem_wo = any(x.strip(" [").startswith("W.O.") for x in pedacos)
    for p in pedacos:
        p = p.strip(" []")
        while p.startswith("(") and p.count("(") > p.count(")"):
            p = p[1:].strip()
        while p.endswith(")") and p.count(")") > p.count("("):
            p = p[:-1].strip()
        if p.startswith("(") and p.endswith(")"):
            p = p[1:-1].strip()
        if not p or re.fullmatch(r"\d+", p):
            continue
        # data solta ("Feb 3", 1999) e nota de campeonato que não é do jogo ("São Paulo lost 5 points due to...", 1996)
        if re.fullmatch(r"[A-Z][a-z]{2}\.? \d{1,2}", p) or re.search(r"\blost \d+ points\b", p, re.I):
            continue
        if re.search(r"\bpen(?:alties)?\.?\s*:?\s*\d+\s*-\s*\d+|\d+\s*-\s*\d+\s*(?:on )?pen(?:alties)?\b", p, re.I):
            continue
        if tem_wo and re.fullmatch(r"awd\s+\d+-\d+", p, re.I):   # o W.O. já explica
            continue
        p = re.sub(r"^Pro\s+(\d+-\d+)$", r"prorrogação \1", p)
        p = re.sub(r"^played in (.+)$", r"jogo em \1", p, flags=re.I)
        p = re.sub(r"^played at (.+?) stadium$", r"jogo no estádio \1", p, flags=re.I)
        p = re.sub(r"^(.+?) qualified on away goals$", r"\1 classificado pelo gol fora de casa", p, flags=re.I)
        p = re.sub(r"^awd\s+(\d+-\d+)$", r"resultado dado no tribunal (\1)", p, flags=re.I)
        m = re.match(r"^Concluded on (\w+) (\d{1,2}), (\d{4})$", p, re.I)
        if m and m[1].lower() in MESES_EN:
            p = f"concluído em {int(m[2]):02d}/{MESES_EN[m[1].lower()]:02d}/{m[3]}"
        for padrao, troca in TRADUCOES:
            if re.fullmatch(padrao, p, re.I):
                p = re.sub(padrao, troca, p, flags=re.I)
                break
        if p not in partes:
            partes.append(p)
    return "; ".join(partes)
