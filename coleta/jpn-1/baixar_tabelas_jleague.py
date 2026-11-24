"""Baixa do J.League Data Site as tabelas oficiais da J1 (1993-2025), base da conferência e da classificação final.

- "League table" (SFRT01): a tabela de cada torneio da J1 no ano (os dois turnos nos anos de turnos: "Suntory" e
  "NICOS", "1st Stage" e "2nd Stage"), na última rodada;
- "Overall table for the season" (SFRT03): a tabela somada dos dois turnos (1999-2004, 2015 e 2016).

As colunas mudam com a época: "W 90W VW PKW L 90L VL PKL" (vitórias no tempo normal, na prorrogação e nos pênaltis,
1993-1998), "W D L" com "VW" (1999-2002) ou só "W D L" (2003 em diante).

Saída: data/coleta/jpn-1/jleague/tabelas_<ano>.json = [{"torneio", "fonte", "colunas", "linhas": [[...], ...]}].
Páginas brutas em data/cache/jleague-asia/tabelas/.

Uso: python coleta/jpn-1/baixar_tabelas_jleague.py [ano ...]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from baixar_jleague import BASE, CACHE, PASTA, _celula, pegar  # noqa: E402

TAB = CACHE / "tabelas"


def _opcoes(t: str) -> list[tuple[str, str]]:
    return [(v, _celula(n)) for v, n in re.findall(r'<option value="(\d+)"[^>]*>([^<]*)', t)]


def _tabela(t: str) -> tuple[list[str], list[list[str]]]:
    """Cabeçalho e linhas da tabela de classificação ("Position Team Pts GP ...")."""
    for tab in re.findall(r"<table\b.*?</table>", t, flags=re.S):
        cab = [_celula(c) for c in re.findall(r"<th[^>]*>(.*?)</th>", tab, flags=re.S)]
        if "Team" in cab and ("Pts" in cab or "W" in cab):   # 1993 e 1994 não têm pontos
            linhas = []
            for tr in re.findall(r"<tr\b.*?</tr>", tab, flags=re.S):
                cel = [_celula(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, flags=re.S)]
                if len(cel) >= 6:
                    linhas.append(cel)
            return cab, linhas
    return [], []


def _sem_cache(url: str, arq: Path) -> str:
    """As páginas de opções (pequenas, sem o menu em inglês) não passam pela conferência de língua de pegar()."""
    from baixar_jleague import _baixar
    import gzip
    if arq.exists():
        return gzip.decompress(arq.read_bytes()).decode("utf-8", "ignore")
    b = _baixar(url)
    arq.parent.mkdir(parents=True, exist_ok=True)
    arq.write_bytes(gzip.compress(b))
    return b.decode("utf-8", "ignore")


def ano(a: int) -> list[dict]:
    saida = []
    comps = _opcoes(_sem_cache(f"{BASE}/SFRT01/competition?yearId={a}", TAB / f"comp_{a}.html.gz"))
    for cid, nome in comps:
        if not re.search(r"J1|J\.LEAGUE (Suntory|NICOS|Division 1)|J\.LEAGUE$|J\.LEAGUE (1st|2nd)|Suntory|NICOS", nome, re.I) \
                or re.search(r"Cup|J2|J3|Play-?Off|Youth|Division 2", nome, re.I):
            continue
        secs = [v for v, _ in _opcoes(_sem_cache(f"{BASE}/SFRT01/competitionSection?competitionId={cid}", TAB / f"sec_{cid}.html.gz")) if v != "0"]
        sec = max(secs, key=int)
        t = pegar(f"{BASE}/SFRT01/search?yearId={a}&competitionId={cid}&competitionSectionId={sec}", TAB / f"tab_{a}_{cid}_{sec}.html.gz")
        cab, linhas = _tabela(t)
        saida.append({"torneio": nome, "fonte": f"SFRT01 {cid}/{sec}", "colunas": cab, "linhas": linhas})
    if a in (1999, 2000, 2001, 2002, 2003, 2004, 2015, 2016):
        frames = _opcoes(_sem_cache(f"{BASE}/SFRT03/competitionFrame?yearId={a}", TAB / f"frame_{a}.html.gz"))
        fid = frames[0][0]
        secs = [v for v, _ in _opcoes(_sem_cache(f"{BASE}/SFRT03/competitionSection?yearId={a}&competitionFrameId={fid}",
                                                 TAB / f"sec3_{a}_{fid}.html.gz")) if v != "0"]
        url = f"{BASE}/SFRT03/search?yearId={a}&competitionFrameId={fid}" + (f"&competitionSectionId={max(secs, key=int)}" if secs else "")
        cab, linhas = _tabela(pegar(url, TAB / f"anual_{a}.html.gz"))
        saida.append({"torneio": "Overall", "fonte": f"SFRT03 {fid}", "colunas": cab, "linhas": linhas})
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for a in [int(x) for x in sys.argv[1:]] or range(1993, 2026):
        tabs = ano(a)
        (PASTA / f"tabelas_{a}.json").write_text(json.dumps(tabs, ensure_ascii=False, indent=0), encoding="utf-8")
        print(a, [(t["torneio"], len(t["linhas"])) for t in tabs], flush=True)
