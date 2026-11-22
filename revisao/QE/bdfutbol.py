"""BDFutbol (bdfutbol.com): leitor das páginas de temporada e de jogo (revisão QE, 3ª rodada).

Temporada: https://www.bdfutbol.com/es/t/t1928-29.html (Espanha) e /es/t/teng1960-61.html (Inglaterra, desde 1960/61).
Cada página traz todos os jogos: rodada, data, mandante, placar, visitante, estádio, árbitro e o id da ficha (p.php?id=N).
Ficha do jogo: https://www.bdfutbol.com/es/p/p.php?id=N (autores com minuto, árbitro, escalações, técnicos).

Uso: python -I revisao/QE/bdfutbol.py baixar esp 1928-2025   |   python -I revisao/QE/bdfutbol.py baixar eng 1960-2025
"""
import html
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from baixar import baixar  # noqa: E402


def url_temporada(liga: str, ai: int) -> str:
    s = f"{ai}-{str(ai + 1)[-2:]}"
    return f"https://www.bdfutbol.com/es/t/t{'eng' if liga == 'eng' else ''}{s}.html"


def url_jogo(pid: str) -> str:
    return f"https://www.bdfutbol.com/es/p/p.php?id={pid}"


def _txt(x: str) -> str:
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", x))).strip()


LINHA = re.compile(r"<tr class='jornadai ij(\d+)'[^>]*data-jornada='(\d+)'>(.*?)</tr>", re.S)


def jogos_temporada(arq: str) -> list[dict]:
    t = open(arq, encoding="utf-8", errors="replace").read()
    res = []
    for m in LINHA.finditer(t):
        corpo = m.group(3)
        if "p.php?id=" not in corpo:
            continue
        tds = re.findall(r"<td[^>]*>(.*?)</td>", corpo, re.S)
        if len(tds) < 4:
            continue
        pid = re.search(r"p\.php\?id=(\d+)", corpo).group(1)
        gols = _txt(tds[2]).split()
        res.append({
            "rodada": int(m.group(2)), "data": _txt(tds[0]), "mandante": _txt(tds[1]), "visitante": _txt(tds[3]),
            "gm": gols[0] if len(gols) > 0 else "", "gv": gols[1] if len(gols) > 1 else "",
            "estadio": _txt(tds[4]) if len(tds) > 4 else "", "arbitro": _txt(tds[5]) if len(tds) > 5 else "",
            "pid": pid, "placar_txt": _txt(tds[2]),
        })
    return res


def ficha(arq: str) -> dict:
    """Ficha do jogo: autores (minuto, placar parcial), árbitro, público (quando há), cartões (quando há)."""
    t = open(arq, encoding="utf-8", errors="replace").read()
    b = t.find("<body")
    corpo = re.sub(r"<script.*?</script>", "", t[b:], flags=re.S)
    s = _txt(corpo)
    i = s.find("Competición")
    j = s.find("Histórico", i)
    cab = s[i:j]
    gols = re.findall(r"(\d+)-(\d+) ([^\d']+?) (\d+)(?:\+\d+)?'( \((?:pp|p)\))?", cab)
    pub = re.search(r"(?:Espectadores|Asistencia|Público)\s*:?\s*([\d\.]+)", s)
    cart = re.findall(r'title="(Tarjeta [^"]+)"></div>\s*(\d+)', corpo)
    return {"cab": cab, "gols": [(int(a), int(b_), n.strip() + (" (contra)" if t_ == " (pp)" else " (pênalti)" if t_ == " (p)" else ""), int(mi))
                     for a, b_, n, mi, t_ in gols],
            "publico": pub.group(1) if pub else "", "cartoes": cart, "texto": s}


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if sys.argv[1] == "baixar":
        liga = sys.argv[2]
        a0, a1 = map(int, sys.argv[3].split("-"))
        for ai in range(a0, a1 + 1):
            if liga == "esp" and 1936 <= ai <= 1938:
                continue
            arq = baixar(url_temporada(liga, ai))
            print(ai, arq and len(jogos_temporada(arq)), flush=True)


def tabela_final(arq: str) -> list[dict]:
    """Classificação da página da temporada (1ª tabela depois do cabeçalho 'Pts.'): posição, nome, Pts, J, V, E, D, GP, GC,
    amarelos e vermelhos da temporada (TA/TR)."""
    t = open(arq, encoding="utf-8", errors="replace").read()
    i = t.find(">Pts.<")
    if i < 0:
        return []
    fim = t.find("</table>", i)
    res = []
    for tr in re.findall(r"<tr data-ideq=[^>]*>(.*?)</tr>", t[i:fim], re.S):
        tds = [_txt(x) for x in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)]
        if len(tds) < 11:
            continue
        n = [int(x) if re.fullmatch(r"-?\d+", x) else None for x in tds[4:13]]
        mp = re.match(r"\d+", tds[1])
        if not mp:
            continue
        res.append({"pos": int(mp.group()), "nome": tds[3], "pts": n[0], "j": n[1], "v": n[2], "e": n[3],
                    "d": n[4], "gp": n[5], "gc": n[6], "ta": n[7] if len(n) > 7 else None, "tr": n[8] if len(n) > 8 else None})
    return res
