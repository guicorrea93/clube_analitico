"""Lê as páginas da RSSSF da liga inglesa (engpaul/FLA/<temporada>.html, Paul Felton e Barry Spencer).

De cada página, só a 1ª divisão (o primeiro bloco da página):
- a tabela final publicada: posição, nome, jogos, campanha em casa e fora, pontos; nome em MAIÚSCULAS = campeão,
  rebaixado ou promovido; "*" antes do nome = punição explicada na nota logo abaixo;
- a matriz de resultados ("Cross-Table"), quando a página traz: placar de cada mandante contra cada visitante.

Uso como biblioteca: ler(arquivo) -> {"tabela": [...], "notas": [...], "matriz": {(mandante, visitante): (g1, g2)}}
"""
from __future__ import annotations

import html
import re
from pathlib import Path

LINHA = re.compile(r"^\s*(\d+)[.=]?\s+([*+#\s]*[A-Za-z&'.\- ]+?)\s+((?:-?\d+\s+){6,13}-?\d+)\s*(.*)$")
CABECALHO = re.compile(r"^\s+P\s+W\s+D\s+L\s+F\s+A\b.*\bPts\b", re.I)


def _texto(arq: Path) -> list[str]:
    t = arq.read_bytes().decode("latin-1")
    t = html.unescape(re.sub(r"<[^>]+>", "", t))
    return t.replace("\r", "").split("\n")


def ler(arq: Path) -> dict:
    linhas = _texto(arq)
    tabela, notas, matriz = [], [], {}
    # ---- tabela: o primeiro cabeçalho "P W D L F A ... Pts"
    i = next(k for k, l in enumerate(linhas) if CABECALHO.match(l))
    cols = linhas[i].split()   # P W D L F A [W D L F A] [GD] [PD] Pts — PD = pontos deduzidos
    k = i + 1
    while k < len(linhas):
        m = LINHA.match(linhas[k])
        if not m:
            break
        nums = [int(x) for x in m.group(3).split()]
        if len(nums) != len(cols):
            raise ValueError(f"{arq.name}: linha com {len(nums)} números e cabeçalho com {len(cols)}: {linhas[k]!r}")
        nome = m.group(2).strip()
        punido = bool(re.match(r"^[*+#]", nome))
        nome = nome.lstrip("*+# ").strip()
        val = dict(zip([c.upper() for c in cols], nums))   # repetidas (casa e fora) ficam com a última; somo abaixo
        wdl = [n for c, n in zip(cols, nums) if c.upper() in ("W", "D", "L", "F", "A")]
        if len(wdl) == 10:
            v, e, d, gp, gc = (wdl[x] + wdl[x + 5] for x in range(5))
        else:
            v, e, d, gp, gc = wdl
        tabela.append({"posicao": int(m.group(1)), "empate_posicao": "=" in linhas[k][:6], "nome": nome,
                       "maiusculas": nome.upper() == nome and any(c.isalpha() for c in nome), "punido": punido or bool(val.get("PD")),
                       "jogos": nums[0], "vitorias": v, "empates": e, "derrotas": d, "gols_pro": gp, "gols_contra": gc,
                       "pontos": nums[-1], "deduzidos": val.get("PD"), "resto": m.group(4).strip()})
        k += 1
    # notas logo abaixo da tabela ("* Two points deducted ...", com continuação recuada); "14=" é posição empatada
    while k < len(linhas) and (not linhas[k].strip() or linhas[k].startswith("*") or linhas[k].startswith("  ") and notas):
        if linhas[k].startswith("*"):
            notas.append(linhas[k].strip())
        elif linhas[k].strip():
            notas[-1] += " " + linhas[k].strip()
        k += 1
    # ---- matriz de resultados (antes da tabela, quando existe)
    j = next((k for k, l in enumerate(linhas[:i]) if l.strip().startswith("Cross-Table")), None)
    if j is not None:
        cab = linhas[j + 1]
        k = j + 2
        rotulos = []
        while k < i and linhas[k].strip() and not linhas[k].startswith("Final"):
            l = linhas[k]
            m = re.match(r"^(.+?)\s+((?:(?:\d+-\d+|xxx|---|\s{3})\s*)+)$", l.rstrip())
            if not m:
                break
            rotulos.append((m.group(1).strip(), re.findall(r"\d+-\d+|xxx|---|\?-\?", m.group(2))))
            k += 1
        n = len(rotulos)
        for a, (nome, cel) in enumerate(rotulos):
            if len(cel) != n:
                raise ValueError(f"{arq.name}: matriz com {len(cel)} colunas na linha de {nome} (esperado {n})")
            for b, c in enumerate(cel):
                if a != b and re.match(r"\d+-\d+", c):
                    g1, g2 = c.split("-")
                    matriz[(nome, rotulos[b][0])] = (int(g1), int(g2))
    return {"tabela": tabela, "notas": notas, "matriz": matriz}


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    pasta = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "eng-1" / "rsssf"
    for arq in sorted(pasta.glob("*.html")):
        r = ler(arq)
        print(arq.stem, len(r["tabela"]), len(r["matriz"]), [x["nome"] for x in r["tabela"] if x["punido"]], r["notas"][:1])
