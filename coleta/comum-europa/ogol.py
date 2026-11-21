"""Calendário de uma edição no ogol (zerozero), para as ligas europeias (copiado de coleta/comum/ogol.py).

De cada jogo: data e hora, mandante, visitante, placar, rodada ("R12" = 12ª rodada), código de cada clube e o link.
As páginas ficam em data/cache/ogol-<slug>/calendario_<ano_inicio>_<id da edição>_p<página>.html: o agente 1
tira os escudos de lá (docs/agentes-internacionais-COMECE-AQUI.md, seção 5).

Uso como biblioteca: edicoes(url_competicao, cache) -> [(id, "1888/89")]; calendario(id, ano_inicio, cache) -> list[dict]
"""
from __future__ import annotations

import html
import re
import time
from pathlib import Path

from baixar import pegar

BASE = "https://www.ogol.com.br"


def _texto(v: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", v))).strip()


def edicoes(competicao: str, cache: Path) -> list[tuple[str, str]]:
    """Lista de edições do seletor da página da competição ("premier-league"): [(id, "2024/25"), ...]."""
    t = (pegar(f"{BASE}/competicao/{competicao}", cache / f"competicao_{competicao}.html") or b"").decode("utf-8", "ignore")
    for sel in re.findall(r"<select\b.*?</select>", t, flags=re.S):
        ops = re.findall(r'<option value="(\d+)"[^>]*>\s*([^<]+?)\s*</option>', sel)
        if ops and all(re.match(r"^\d{4}(/\d{2})?$", n) for _, n in ops):
            return ops
    return []


class PaginaTrocada(Exception):
    pass


def pagina_valida(t: str, ed: str | int, pagina: int) -> bool:
    """O ogol às vezes devolve a página de outra competição no lugar da pedida (visto em 20/11/2026: Islândia, Hong Kong,
    Portugal...). A página certa traz o link canônico com o id da edição e a página."""
    m = re.search(r'<link rel="canonical" href="([^"]+)"', t)
    return bool(m and re.search(rf"/{ed}/calendario\?page={pagina}$", html.unescape(m.group(1))))


def _pagina(ed: str | int, ano: int, pagina: int, cache: Path) -> str:
    arq = cache / f"calendario_{ano}_{ed}_p{pagina}.html"
    for tentativa in range(8):
        t = (pegar(f"{BASE}/edicao/-/{ed}/calendario?page={pagina}", arq, espera=3.0) or b"").decode("utf-8", "ignore")
        if pagina_valida(t, ed, pagina):
            return t
        arq.unlink(missing_ok=True)   # página trocada: apaga e tenta de novo, com mais espera
        time.sleep(20 * (tentativa + 1))
    raise PaginaTrocada(f"edição {ed}, página {pagina}: o ogol devolveu outra página 8 vezes")


def calendario(ed: str | int, ano: int, cache: Path) -> list[dict]:
    jogos, vistos = [], set()
    for pagina in range(1, 80):
        t = _pagina(ed, ano, pagina, cache)
        antes = len(vistos)
        for linha in re.findall(r"<tr\b.*?</tr>", t, flags=re.S | re.I):
            link = re.search(r'href="(/jogo/(\d{4}-\d{2}-\d{2})-[^"]+/(\d+))"', linha)
            if not link or link.group(3) in vistos:
                continue
            casa = re.search(r'class="text home"[^>]*>(.*?)</td>', linha, flags=re.S)
            fora = re.search(r'class="text away"[^>]*>(.*?)</td>', linha, flags=re.S)
            placar = re.search(r'class="result"[^>]*>(.*?)</td>', linha, flags=re.S)
            fase = re.search(r'class="phase"[^>]*>(.*?)</td>', linha, flags=re.S)
            hora = re.search(r'<td>\s*(\d{1,2}:\d{2})\s*</td>', linha)
            if not (casa and fora):
                continue
            vistos.add(link.group(3))
            res = _texto(placar.group(1)) if placar else ""
            mp = re.search(r"(\d+)\s*-\s*(\d+)", res)
            f = _texto(fase.group(1)) if fase else ""
            # código do clube no link ("/equipe/stoke-city/2581"); os grandes vêm só com o apelido ("/equipe/wolverhampton")
            id_casa = re.search(r'/equipe/([^/"?]+)(?:/(\d+))?', casa.group(1))
            id_fora = re.search(r'/equipe/([^/"?]+)(?:/(\d+))?', fora.group(1))
            jogos.append({"id": link.group(3), "data": link.group(2), "hora": hora.group(1) if hora else None,
                          "mandante": _texto(casa.group(1)), "visitante": _texto(fora.group(1)),
                          "mandante_id": (id_casa.group(2) or id_casa.group(1)) if id_casa else None,
                          "visitante_id": (id_fora.group(2) or id_fora.group(1)) if id_fora else None,
                          "gols_mandante": int(mp.group(1)) if mp else None, "gols_visitante": int(mp.group(2)) if mp else None,
                          "resultado": res, "fase": f, "rodada": int(m.group(1)) if (m := re.match(r"^R(\d+)$", f)) else None,
                          "url": BASE + link.group(1)})
        if len(vistos) == antes:
            break
    return jogos


def equipe(id_ogol: str, cache: Path) -> dict:
    """Ficha do clube no ogol: nome completo, cidade, país e ano de fundação."""
    url = f"{BASE}/equipe/-/{id_ogol}" if id_ogol.isdigit() else f"{BASE}/equipe/{id_ogol}"
    t = (pegar(url, cache / f"equipe_{id_ogol}.html", espera=1.2) or b"").decode("utf-8", "ignore")
    linhas = [l.strip() for l in html.unescape(re.sub(r"<[^>]+>", "\n", t)).split("\n") if l.strip()]
    def depois(rotulo):
        for i, l in enumerate(linhas[:-1]):
            if l == rotulo:
                return linhas[i + 1]
        return None
    titulo = re.search(r"<title>(.*?)</title>", t, re.S)
    return {"id": id_ogol, "nome_completo": depois("Nome"), "cidade": depois("Cidade"), "pais": depois("País"),
            "fundacao": depois("Ano de Fundação"), "titulo": _texto(titulo.group(1)) if titulo else None}
