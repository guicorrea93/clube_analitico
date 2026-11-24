"""Lê a 1ª divisão da Japan Soccer League (JSL, 1965 a 1991/92) nas páginas de temporada da RSSSF (jap65.html a jap92.html).

Cada página traz a JSL1 no começo: tabela final ("Final Table:"), tabela de confrontos ("Cross-Table:") e artilheiros;
depois vêm a JSL2, a Copa do Imperador e as ligas regionais, que ficam de fora. Só 1988/89 traz as rodadas com data.

- Tabela final: "1.Toyo Industries  14 12  2  0  44- 9  26". De 1977 a 1979 os empates iam para os pênaltis
  ("18 14 1/2  1 64-15  60": vitórias, vitórias/derrotas nos pênaltis, derrotas; 4 pontos a vitória, 2 a vitória nos
  pênaltis, 1 a derrota nos pênaltis). A tabela de confrontos não diz quem ganhou cada disputa de pênaltis.
- Tabela de confrontos: mandante na linha, visitante na coluna, "x" (ou "xxx") na diagonal. Dois formatos: linhas
  numeradas ("1.Hitachi  x 1-3 2-1 ...", coluna j = clube j) e, em 1988/89, siglas no cabeçalho com as linhas em ordem
  alfabética (coluna j = linha j).
- Rodadas (1988/89): "Round 1", "[Sep 23]", "Matsushita  1-1 All Nippon Airways".

Uso como biblioteca: ler(ano) -> Temporada; para ver: python coleta/jpn-1/ler_jsl.py [ano]
"""
from __future__ import annotations

import html
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
PASTA = RAIZ / "data" / "coleta" / "jpn-1" / "rsssf"
MESES = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


@dataclass
class Linha:
    pos: int
    nome: str
    j: int
    v: int
    e: int
    d: int
    gp: int
    gc: int
    pts: int
    v_pen: int | None = None   # 1977-1979: vitórias e derrotas nos pênaltis (os empates)
    d_pen: int | None = None
    nota: str = ""


@dataclass
class Jogo:
    mandante: str
    visitante: str
    gm: int
    gv: int
    rodada: int | None = None
    data: str | None = None
    linha: int = 0


@dataclass
class Temporada:
    ano: int                 # ano da página (jap<ano>): o ano de início, ou o de fim nas temporadas "1985/86"...
    pagina: str
    tabela: list[Linha] = field(default_factory=list)
    jogos: list[Jogo] = field(default_factory=list)          # da tabela de confrontos
    rodadas: list[Jogo] = field(default_factory=list)        # da lista por rodada (só 1988/89)
    artilheiros: list[tuple[str, str, int]] = field(default_factory=list)   # (jogador, clube como escrito, gols)
    notas: list[str] = field(default_factory=list)


def texto(caminho: Path) -> list[str]:
    """Página -> linhas de texto puro (páginas em UTF-16 ou em cp1252)."""
    b = caminho.read_bytes()
    if b[:2] in (b"\xff\xfe", b"\xfe\xff"):
        t = b.decode("utf-16")
    else:
        try:
            t = b.decode("utf-8")
        except UnicodeDecodeError:
            t = b.decode("cp1252", "ignore")
    t = re.sub(r"<[^>]+>", "", t)
    return html.unescape(t).replace("\r", "").replace("\t", "        ").split("\n")


def pagina(ano: int) -> Path:
    return PASTA / f"jap{ano % 100:02d}.html"


_TAB = re.compile(r"^\s*(\d+)\.\s*(\S.*?)\s+(\d+)\s+(\d+)\s+(\d+)(?:/(\d+))?\s+(\d+)\s+(\d+)\s*-\s*(\d+)\s+(\d+)(.*)$")


def trecho(linhas: list[str]) -> list[str]:
    """Só a JSL1: do começo até o título da JSL2, da Copa do Imperador ou das ligas regionais."""
    for i, l in enumerate(linhas):
        if i > 12 and re.search(r"Second Division|\(JSL2\)|Emperor's Cup|Regional Leagues|JSL Cup", l):
            return linhas[:i]
    return linhas


def ler(ano: int, conserta: dict | None = None) -> Temporada:
    """conserta: {(número da linha, texto errado): (texto certo, motivo)}, aplicado antes da leitura."""
    linhas = texto(pagina(ano))
    for (n, errado), (certo, _motivo) in (conserta or {}).items():
        assert errado in linhas[n], (ano, n, linhas[n])
        linhas[n] = linhas[n].replace(errado, certo)
    linhas = trecho(linhas)
    t = Temporada(ano, pagina(ano).name)
    secao = ""
    rodada, data = None, None
    nomes_cruzada: list[str] = []
    for n, l in enumerate(linhas):
        s = l.strip()
        if re.match(r"^Final Table", s):
            secao = "tabela" if not t.tabela else "fora"; continue   # 1988/89 repete a tabela depois das rodadas
        if re.match(r"^Cross-?Table", s):
            secao = "cruzada"; continue
        if re.match(r"^Top scorers", s, re.I):
            secao = "artilheiros"; continue
        if re.match(r"^Promotion/Relegation", s):
            secao = "fora"; continue
        if m := re.match(r"^Round (\d+)\s*(?:\[(\w{3})\w*\.? (\d{1,2})\])?$", s):   # "Round 21 [Apr 26]"
            secao, rodada = "rodadas", int(m.group(1))
            data = (MESES[m.group(2).lower()], int(m.group(3))) if m.group(2) else None
            continue
        if secao == "tabela":
            if m := _TAB.match(l):
                pos, nome, j, v, e, pen, d, gp, gc, pts, resto = m.groups()
                if pen is not None:   # "14 1/2 1": e = vitórias nos pênaltis, pen = derrotas nos pênaltis
                    t.tabela.append(Linha(int(pos), nome.strip(), int(j), int(v), int(e) + int(pen), int(d), int(gp),
                                          int(gc), int(pts), int(e), int(pen), resto.strip()))
                else:
                    t.tabela.append(Linha(int(pos), nome.strip(), int(j), int(v), int(e), int(d), int(gp), int(gc),
                                          int(pts), None, None, resto.strip()))
            elif s.startswith("[") or s.startswith(("Promoted", "Relegated", "No teams", "Name", "Disbanded", "NB")):
                t.notas.append(s)
        elif secao == "cruzada":
            if not s or re.match(r"^(\d+\s+)+\d+$", s) or s.startswith("Team"):
                continue
            if s.startswith(("Promoted", "Relegated", "No teams", "Name", "Disbanded", "[", "Nippon Kokan were")):
                t.notas.append(s); continue
            nomes_cruzada.append((n, l))
        elif secao == "artilheiros":
            if m := re.match(r"^\s*(?:\d+\.)?\s*(.+?)\s*\(([^)]+)\)\s+(\d+)\b", l):
                t.artilheiros.append((m.group(1).strip(), m.group(2).strip(), int(m.group(3))))
        elif secao == "rodadas":
            if m := re.match(r"^\s*\[(\w{3})\w*\.? (\d{1,2})\]\s*$", l):
                data = (MESES[m.group(1).lower()], int(m.group(2))); continue
            if m := re.match(r"^\s*(\S.*?)\s+(\d+)-(\d+)\s+(\S.*?)\s*$", l):
                t.rodadas.append(Jogo(m.group(1), m.group(4), int(m.group(2)), int(m.group(3)), rodada,
                                      _data(ano, data), n))
    t.jogos = _cruzada(nomes_cruzada, len(t.tabela))
    return t


def _data(ano: int, md: tuple[int, int] | None) -> str | None:
    """1988/89 vai de setembro a março: de julho em diante é o ano de início."""
    if not md:
        return None
    mes, dia = md
    a = ano - 1 if mes >= 7 else ano
    return f"{a}-{mes:02d}-{dia:02d}"


def _cruzada(linhas: list[tuple[int, str]], n: int) -> list[Jogo]:
    nomes, celulas = [], []
    for num, l in linhas[:n]:
        partes = l.split()
        cel, nome = partes[-n:], " ".join(partes[:-n])
        nome = re.sub(r"^\d+\.\s*", "", nome)
        nomes.append((num, nome))
        celulas.append(cel)
    jogos = []
    for i, (num, mand) in enumerate(nomes):
        for j, c in enumerate(celulas[i]):
            if i == j:
                assert c.lower() in ("x", "xxx"), (mand, celulas[i])
                continue
            m = re.match(r"^(\d+)\D(\d+)$", c)   # 1985/86 tem um travessão (byte 0x97) no lugar do hífen
            assert m, (mand, c, celulas[i])
            jogos.append(Jogo(mand, nomes[j][1], int(m.group(1)), int(m.group(2)), linha=num))
    return jogos


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    from explicacoes import CONSERTA_JSL
    for a in [int(x) for x in sys.argv[1:]] or [*range(1965, 1985), *range(1986, 1993)]:
        t = ler(a, CONSERTA_JSL.get(a))
        print(a, t.pagina, "clubes", len(t.tabela), "jogos", len(t.jogos), "rodadas", len(t.rodadas),
              "artilheiros", len(t.artilheiros), "|", "; ".join(t.notas)[:150])
