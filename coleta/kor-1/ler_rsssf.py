"""Lê os jogos das páginas da RSSSF da Coreia do Sul (data/coleta/kor-1/rsssf/skorYY.html e skorYYYY.html), para a
conferência dos placares do portal oficial.

As páginas mudam de forma de um ano para outro, então a leitura é genérica:
- a data vem da linha "1983/05/08" (ou "[Mar 10, 2002]", "Mar 10" com o ano da página) e vale para os jogos abaixo;
- o jogo é a linha "Mandante   2-1  Visitante   [local]" (dois espaços ou mais entre os nomes e o placar), com "aet",
  "pen" e afins guardados em obs;
- as páginas novas vêm em UTF-16 (com BOM).
Os nomes ficam como estão na RSSSF; a ligação com os códigos do portal é feita por quem usa (mesma data e mesmo placar).

Uso como biblioteca: jogos(ano) -> lista de dicts {data, mandante, visitante, gm, gv, obs, linha}.
Para ver: python coleta/kor-1/ler_rsssf.py <ano>
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PASTA = AQUI.parent.parent / "data" / "coleta" / "kor-1" / "rsssf"
MESES = {m: i + 1 for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split())}
JOGO = re.compile(r"^\s*([A-Za-z][\w'.&()/ -]*?[\w.)'])\s{2,}(\d+)\s*-\s*(\d+)\s+(?:\(.*?\)\s+)?"
                  r"([A-Za-z][\w'.&()/ -]*?[\w.)'])(?:\s{2,}|\s*\[|\s*$)(.*)$")


def texto(ano: int) -> str:
    arq = PASTA / (f"skor{ano % 100:02d}.html" if ano < 2010 else f"skor{ano}.html")
    b = arq.read_bytes()
    t = b.decode("utf-16") if b[:2] in (b"\xff\xfe", b"\xfe\xff") else b.decode("latin-1")
    return html.unescape(re.sub(r"<[^>]+>", "", t)).replace("\r", "")


AUTOR = re.compile(r"([A-Za-z'][^\d,;\[\]]*?)\s*((?:\d+(?:\+\d+)?\s*(?:PK|pen\.?|og\.?|own goal|FK)?\s*,?\s*)+)")


def autores(texto_: str, gm: int, gv: int) -> tuple[list, list] | None:
    """"[Kim Hyeon-Bok 25, Park Seong-Hwa 40; Park Yun-Gi 32, 75]" -> ([(nome, minuto), ...] do mandante, [...] do
    visitante). None quando não dá para separar os lados."""
    s = texto_.strip().strip("[]")
    if not s:
        return None
    lados = s.split(";")
    if len(lados) == 1:
        if gm and gv:
            return None
        lados = [s, ""] if gm else ["", s]
    if len(lados) != 2:
        return None
    saida = []
    for lado in lados:
        gols = []
        for m in AUTOR.finditer(lado):
            nome = re.sub(r"\(.*?\)", "", m.group(1)).strip(" .'")
            for mi in re.findall(r"(\d+)(?:\+(\d+))?", m.group(2)):
                gols.append((nome, int(mi[0]) + int(mi[1] or 0)))
        saida.append(gols)
    return saida[0], saida[1]


def jogos(ano: int) -> list[dict]:
    out, data = [], None
    linhas = texto(ano).split("\n")
    for i, linha in enumerate(linhas):
        s = linha.strip()
        m = re.match(r"^\[?(\d{4})/(\d{1,2})/(\d{1,2})\]?", s)
        if m:
            data = f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
        else:
            m = re.match(r"^\[?(?:[A-Za-z]+,?\s+)?([A-Za-z]{3})[a-z]*\.?\s+(\d{1,2})(?:,\s*(\d{4}))?\]?\s*$", s) or \
                re.search(r"\[([A-Za-z]{3})[a-z]*\.?\s+(\d{1,2})(?:,\s*(\d{4}))?\]\s*$", s)
            if m and m.group(1).lower() in MESES:
                data = f"{m.group(3) or ano}-{MESES[m.group(1).lower()]:02d}-{int(m.group(2)):02d}"
        j = JOGO.match(linha)
        if j and not re.match(r"^\s*\d+\.", linha):
            aut, k = "", i + 1
            prox = linhas[k].strip() if k < len(linhas) else ""
            data_ = re.match(r"^\[(?:[A-Za-z]+,?\s+)?([A-Za-z]{3})[a-z]*\.?\s+\d{1,2}\b", prox)
            if prox.startswith("[") and not (data_ and data_.group(1).lower() in MESES):   # os autores na linha de baixo
                aut = linhas[k].strip()
                while "]" not in aut and k + 1 < len(linhas):
                    k += 1
                    aut += " " + linhas[k].strip()
            out.append({"data": data, "mandante": j.group(1).strip(), "gm": int(j.group(2)), "gv": int(j.group(3)),
                        "visitante": j.group(4).strip(), "obs": j.group(5).strip(), "linha": linha.strip(), "autores": aut})
    return out


LINHA_TAB = re.compile(r"^\s*(?:\d+\.\s*)?([A-Za-z][\w'.&()/ -]*?[\w.)'])#?\s{2,}((?:\d+\s*-?\s*)+)")


def _linhas_tabela(t: str) -> list[dict]:
    out = []
    for linha in t.split("\n"):
        m = LINHA_TAB.match(linha.replace("\t", "    "))
        if not m:
            continue
        nums = [int(x) for x in re.findall(r"\d+", m.group(2))]
        if len(nums) < 6 or JOGO.match(linha):
            continue
        out.append({"nome": m.group(1).strip(), "jogos": nums[0], "gp": nums[-3], "gc": nums[-2], "pontos": nums[-1],
                    "meio": nums[1:-3], "linha": linha.strip()})
    return out


def tabelas(ano: int) -> list[dict]:
    """Linhas de tabela do ano: de 1983 a 2009 a tabela da temporada da skorhist.html (sem os playoffs, os dois turnos
    somados); de 2010 em diante todas as tabelas da página do ano (fase regular, grupos depois da divisão)."""
    if ano <= 2009:
        b = (PASTA / "skorhist.html").read_bytes()
        t = html.unescape(re.sub(r"<[^>]+>", "", b.decode("latin-1"))).replace("\r", "")
        i = t.find(f"{ano} Season")
        f = t.find("Season", i + 12)
        f = t.rfind("\n", 0, f) if f > 0 else t.find("All-Time", i)
        return _linhas_tabela(t[i:f])
    return _linhas_tabela(texto(ano))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for x in jogos(int(sys.argv[1])):
        print(x["data"], x["mandante"], x["gm"], x["gv"], x["visitante"], "|", x["obs"][:40])
