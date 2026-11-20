"""Baixa o calendário de cada edição da Série B no ogol (zerozero) para data/serie_b/ogol/serie_b_{ano}.json.

O calendário traz, de cada jogo: data e hora, mandante, visitante, placar e a fase ou rodada oficial
("R12" = 12ª rodada; nas edições antigas, o nome da fase). É a fonte da rodada dos anos em que a página
da RSSSF parou no meio. As páginas baixadas ficam em data/cache/ogol_serie_b/ (rodar de novo não baixa outra vez).

Uso: python serie_b/ogol.py [ano ...]     (sem ano: as 44 edições)
"""
from __future__ import annotations

import html
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / "data" / "serie_b" / "ogol"
CACHE = RAIZ / "data" / "cache" / "ogol_serie_b"
BASE = "https://www.ogol.com.br"
UA = {"User-Agent": "Mozilla/5.0 clube-analitico"}
# código da edição no ogol (lista de edições da página da competição "brasileirao-serie-b")
EDICOES = {
    2025: 195259, 2024: 184705, 2023: 172531, 2022: 162063, 2021: 154316, 2020: 142502, 2019: 131668, 2018: 122165,
    2017: 104432, 2016: 96941, 2015: 79847, 2014: 67162, 2013: 57174, 2012: 42649, 2011: 21286, 2010: 13883, 2009: 5340,
    2008: 2235, 2007: 1426, 2006: 1414, 2005: 10850, 2004: 19314, 2003: 19313, 2002: 19312, 2001: 19311, 1999: 23322,
    1998: 23323, 1997: 42487, 1996: 23325, 1995: 23326, 1994: 42461, 1992: 23328, 1991: 23329, 1990: 23330, 1989: 23331,
    1988: 23332, 1985: 23333, 1984: 19331, 1983: 23334, 1982: 23335, 1981: 19212, 1980: 14193, 1972: 14185, 1971: 14183,
}


def pegar(url: str, arquivo: str) -> str:
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / arquivo
    if f.exists():
        return f.read_text(encoding="utf-8", errors="ignore")
    for tentativa in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45) as r:
                t = r.read().decode(r.headers.get_content_charset() or "utf-8", "ignore")
            break
        except Exception:
            if tentativa == 3:
                raise
            time.sleep(5 * (tentativa + 1))
    f.write_text(t, encoding="utf-8")
    time.sleep(1.0)
    return t


def _texto(v: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", v))).strip()


def calendario(ano: int) -> list[dict]:
    ed = EDICOES[ano]
    jogos, vistos = [], set()
    for pagina in range(1, 40):
        t = pegar(f"{BASE}/edicao/-/{ed}/calendario?page={pagina}", f"calendario_{ano}_{ed}_p{pagina}.html")
        antes = len(vistos)
        for linha in re.findall(r"<tr\b.*?</tr>", t, flags=re.S | re.I):
            link = re.search(r'href="(/jogo/(\d{4}-\d{2}-\d{2})-[^"]+/(\d+))"', linha)
            if not link or link.group(3) in vistos:
                continue
            casa = re.search(r'class="text home"[^>]*>(.*?)</td>', linha, flags=re.S)
            fora = re.search(r'class="text away"[^>]*>(.*?)</td>', linha, flags=re.S)
            placar = re.search(r'class="result"[^>]*>.*?>\s*(\d+)\s*-\s*(\d+)\s*<', linha, flags=re.S)
            fase = re.search(r'class="phase"[^>]*>(.*?)</td>', linha, flags=re.S)
            hora = re.search(r'<td>\s*(\d{1,2}:\d{2})\s*</td>', linha)
            if not (casa and fora):
                continue
            vistos.add(link.group(3))
            f = _texto(fase.group(1)) if fase else ""
            jogos.append({"id": link.group(3), "data": link.group(2), "hora": hora.group(1) if hora else None,
                          "mandante": _texto(casa.group(1)), "visitante": _texto(fora.group(1)),
                          "gols_mandante": int(placar.group(1)) if placar else None, "gols_visitante": int(placar.group(2)) if placar else None,
                          "fase": f, "rodada": int(m.group(1)) if (m := re.match(r"^R(\d+)$", f)) else None,
                          "url": BASE + link.group(1)})
        if len(vistos) == antes:
            break
    return jogos


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    for ano in [int(a) for a in sys.argv[1:]] or sorted(EDICOES, reverse=True):
        js = calendario(ano)
        (PASTA / f"serie_b_{ano}.json").write_text(json.dumps(js, ensure_ascii=False, indent=0), encoding="utf-8")
        print(f"{ano}: {len(js)} jogos, {sum(1 for j in js if j['rodada'])} com rodada, fases {sorted({j['fase'] for j in js})[:8]}", flush=True)
