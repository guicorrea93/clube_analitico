"""Lê tabelas finais do módulo "Sports table" da Wikipédia ({{#invoke:Sports table|main|style=WDL ...}}).

De cada tabela: a ordem oficial (team_order), o nome de cada time, vitórias, empates, derrotas, gols pró e contra,
ajuste de pontos (adjust_points; punição negativa), pontos por vitória (win_points), a marca de resultado
(result<n> = C, R, Q...) e as notas (note_XXX, hth_XXX).

Uso como biblioteca: tabelas(wikitexto) -> [tabela, ...]; cada tabela = {"params", "times": [{codigo, nome, ...}]}
"""
from __future__ import annotations

import re


def _fecha(t: str, i: int) -> int:
    """Posição logo depois do "}}" que fecha o "{{" em t[i]."""
    n = 0
    k = i
    while k < len(t):
        if t.startswith("{{", k):
            n += 1; k += 2; continue
        if t.startswith("}}", k):
            n -= 1; k += 2
            if n == 0:
                return k
            continue
        k += 1
    return len(t)


def _partes(corpo: str) -> list[str]:
    """Divide pelos "|" de nível de topo (fora de [[...]] e {{...}})."""
    partes, nivel, atual, k = [], 0, [], 0
    while k < len(corpo):
        dois = corpo[k:k + 2]
        if dois in ("{{", "[["):
            nivel += 1; atual.append(dois); k += 2; continue
        if dois in ("}}", "]]"):
            nivel -= 1; atual.append(dois); k += 2; continue
        if corpo[k] == "|" and nivel == 0:
            partes.append("".join(atual)); atual = []; k += 1; continue
        atual.append(corpo[k]); k += 1
    partes.append("".join(atual))
    return partes


def limpar(v: str) -> str:
    """Texto visível: [[A|B]] -> B, tira modelos, refs e marcação."""
    v = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", v, flags=re.S)
    v = re.sub(r"<!--.*?-->", "", v, flags=re.S)
    v = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", v)
    v = re.sub(r"\{\{[^{}]*\}\}", "", v)
    v = re.sub(r"<[^>]+>", "", v).replace("'''", "").replace("''", "")
    return re.sub(r"\s+", " ", v).strip()


def _num(v: str | None) -> int | None:
    v = limpar(v or "").replace("−", "-").replace("–", "-")
    m = re.match(r"^[+-]?\d+$", v)
    return int(v) if m else None


def tabelas(texto: str) -> list[dict]:
    res = []
    for m in re.finditer(r"\{\{\s*#invoke:\s*sports table\s*\|", texto, flags=re.I):
        fim = _fecha(texto, m.start())
        corpo = re.sub(r"<!--.*?-->", "", texto[m.start() + 2:fim - 2], flags=re.S)
        params: dict[str, str] = {}
        for p in _partes(corpo)[1:]:
            if "=" in p:
                k, v = p.split("=", 1)
                params[k.strip()] = v.strip()
        ordem = [c.strip() for c in re.split(r"[,\n]", params.get("team_order", "")) if c.strip()]
        if not ordem:   # outra forma: team1=EVE|team2=PNE...
            ordem = [params[k].strip() for k in sorted((k for k in params if re.match(r"^team\d+$", k)), key=lambda k: int(k[4:]))]
        if not ordem:
            continue
        # marcas de resultado: result1=C, result18=R (posição -> código); col_C / text_C dizem o que é
        times = []
        for pos, c in enumerate(ordem, 1):
            times.append({"posicao": pos, "codigo": c, "nome": limpar(params.get(f"name_{c}", c)),
                          "nome_wiki": params.get(f"name_{c}", c),
                          "vitorias": _num(params.get(f"win_{c}")), "empates": _num(params.get(f"draw_{c}")),
                          "derrotas": _num(params.get(f"loss_{c}")), "gols_pro": _num(params.get(f"gf_{c}")),
                          "gols_contra": _num(params.get(f"ga_{c}")), "ajuste": _num(params.get(f"adjust_points_{c}")) or 0,
                          "resultado": params.get(f"result{pos}", "").strip(), "status": params.get(f"status_{c}", "").strip(),
                          "nota": limpar(params.get(f"note_{c}", "")), "hth": limpar(params.get(f"hth_{c}", ""))})
        res.append({"params": params, "times": times, "pontos_vitoria": _num(params.get("winpoints") or params.get("win_points")) or 3,
                    "secao": limpar(params.get("section", "")),
                    "inicio": m.start()})
    return res
