"""Baixa do J.League Data Site (data.j-league.or.jp, o site oficial de dados da J.League), em inglês, os jogos da J1
de 1993 a 2025: a lista de cada ano e a página de cada jogo (autores dos gols com minuto, cartões, árbitro, público).

Competições ("competition_frame_ids") baixadas:
- 1: J1 LEAGUE (liga, os dois turnos dos anos com turnos);
- 12: Championship (final entre os campeões dos turnos, 1993-2004);
- 30: MEIJI YASUDA CHAMPIONSHIP (mata-mata do título de 2015 e 2016);
- 13 e 28: J1/J2 Play Off e Play-Offs (repescagem entre J1 e J2/JFL: 1998, 2004-2008, 2018-2021).

As páginas brutas ficam comprimidas em data/cache/jleague-asia/ (fora do git; rodar de novo não baixa outra vez).
Cada ano vira data/coleta/jpn-1/jleague/lista_<ano>.json (a lista, uma linha por jogo, com o id do jogo).

Uso: python coleta/jpn-1/baixar_jleague.py [ano ...] [--sem-jogos] [--reverso]
"""
from __future__ import annotations

import gzip
import html
import http.cookiejar
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
CACHE = RAIZ / "data" / "cache" / "jleague-asia"
PASTA = RAIZ / "data" / "coleta" / "jpn-1" / "jleague"
BASE = "https://data.j-league.or.jp"
FRAMES = {1: "J1", 12: "Championship", 30: "Championship", 13: "Playoff", 28: "Playoff"}
ESPERA = 1.3

_op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
_op.addheaders = [("User-Agent", "Mozilla/5.0 (clube-analitico; projeto pessoal de estatisticas)")]
_ultimo = [0.0]
_ingles = [False]


def _baixar(url: str) -> bytes:
    if not _ingles[0]:   # a língua fica na sessão (cookie): a primeira visita escolhe o inglês
        _op.open(BASE + "/?lang=en", timeout=45).read()
        _ingles[0] = True
    for t in range(6):
        falta = ESPERA - (time.time() - _ultimo[0])
        if falta > 0:
            time.sleep(falta)
        _ultimo[0] = time.time()
        try:
            with _op.open(url, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if t == 5:
                raise
            time.sleep(max(int(e.headers.get("Retry-After") or 0), 10 * (t + 1)) if e.code == 429 else 5 * (t + 1))
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            if t == 5:
                raise
            time.sleep(5 * (t + 1))
    raise RuntimeError(url)


def pegar(url: str, arq: Path) -> str:
    """Página da URL, do cache comprimido se já existe. Confere que veio em inglês."""
    if arq.exists():
        return gzip.decompress(arq.read_bytes()).decode("utf-8", "ignore")
    for _ in range(3):
        b = _baixar(url)
        t = b.decode("utf-8", "ignore")
        if "Results &amp; Schedule" in t or "Results & Schedule" in t:
            break
        _ingles[0] = False   # a sessão caiu e a página veio em japonês: escolhe o inglês de novo
    else:
        raise RuntimeError(f"página não veio em inglês: {url}")
    arq.parent.mkdir(parents=True, exist_ok=True)
    arq.write_bytes(gzip.compress(b))
    return t


def _celula(v: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", v.replace("&nbsp", " ")))).strip()


def lista(ano: int) -> list[dict]:
    jogos = []
    for frame, tipo in FRAMES.items():
        url = f"{BASE}/SFMS01/search?competition_years={ano}&competition_frame_ids={frame}"
        t = pegar(url, CACHE / f"lista_{ano}_{frame}.html.gz")
        for linha in re.findall(r"<tr>\s*<td class=\"bl-non nowrap\">.*?</tr>", t, flags=re.S):
            cel = [_celula(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", linha, flags=re.S)]
            mid = re.search(r"match_card_id=(\d+)", linha)
            if len(cel) < 10:
                continue
            jogos.append({"frame": frame, "tipo": tipo, "temporada": cel[0], "torneio": cel[1], "rodada": cel[2],
                          "data": cel[3], "hora": cel[4], "mandante": cel[5], "placar": cel[6], "visitante": cel[7],
                          "estadio": cel[8], "publico": cel[9], "id": mid.group(1) if mid else None})
    return jogos


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    PASTA.mkdir(parents=True, exist_ok=True)
    anos = [int(a) for a in args] or list(range(1993, 2026))
    for ano in (reversed(anos) if "--reverso" in sys.argv else anos):
        js = lista(ano)
        (PASTA / f"lista_{ano}.json").write_text(json.dumps(js, ensure_ascii=False, indent=0), encoding="utf-8")
        print(ano, len(js), "jogos na lista", {k: sum(1 for j in js if j["tipo"] == k) for k in set(FRAMES.values())}, flush=True)
        if "--sem-jogos" in sys.argv:
            continue
        for j in (reversed(js) if "--reverso" in sys.argv else js):   # --reverso: outra fila, do fim para o começo
            if j["id"]:
                pegar(f"{BASE}/SFMS02/?match_card_id={j['id']}", CACHE / "jogos" / f"{j['id']}.html.gz")
        print(ano, "páginas dos jogos ok", flush=True)
