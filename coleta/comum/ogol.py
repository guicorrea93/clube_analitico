"""Calendário de uma edição no ogol (zerozero), comum a todas as coletas (copiado de serie_b/ogol.py).

De cada jogo: data e hora, mandante, visitante, placar, fase ou rodada ("R12" = 12ª rodada) e o link do jogo.
As páginas baixadas ficam em data/cache/ogol_<slug>/ (rodar de novo não baixa outra vez).

Uso como biblioteca: calendario(id_edicao, cache) -> list[dict]
"""
from __future__ import annotations

import html
import re
import time
from pathlib import Path

from baixar import pegar

BASE = "https://www.ogol.com.br"
ESPERA = 1.2   # segundos entre pedidos (cada coleta pode aumentar)


def _texto(v: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", v))).strip()


def _edicao_abre(ed: int) -> bool:
    """A página da própria edição abre (e não a lista de competições)? Distingue edição sem calendário de limite de pedidos."""
    t = (pegar(f"{BASE}/edicao/-/{ed}", None, espera=ESPERA) or b"").decode("utf-8", "ignore")
    tit = re.search(r"<title>\s*([^<]*)", t)
    return bool(tit) and not tit.group(1).startswith("Competi")


def calendario(ed: int, cache: Path, prefixo: str, titulo: str = "") -> list[dict]:
    """`titulo`: palavra que o título da página tem de ter ("Paulista"), contra a página trocada que o ogol devolve."""
    jogos, vistos = [], set()
    for pagina in range(1, 60):
        destino = cache / f"{prefixo}_{ed}_p{pagina}.html"
        for tentativa in range(4):
            t = (pegar(f"{BASE}/edicao/-/{ed}/calendario?page={pagina}", destino, espera=ESPERA,
                       de_novo=tentativa > 0) or b"").decode("utf-8", "ignore")
            # tem de ser o calendário desta edição: o ogol, quando limita os pedidos, devolve outra página (até o
            # calendário de outra competição)
            tit = re.search(r"<title>\s*(Calend[^<]*)", t)
            if tit and titulo.lower() in tit.group(1).lower() and re.search(rf'/edicao/[^"/]+/{ed}\b', t):
                break
            # o ogol, quando limita os pedidos, devolve outra página (lista de competições...): não fica no cache
            destino.unlink(missing_ok=True)
            # a edição abre e o calendário não, já depois de uma espera: a edição não tem (mais) calendário no ogol
            if tentativa >= 1 and _edicao_abre(ed):
                return jogos
            time.sleep(60 * (tentativa + 1))
        else:
            raise RuntimeError(f"ogol não devolveu o calendário da edição {ed}, página {pagina}")
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
            # código do clube no link ("/equipe/atletico-ba/3128"); os grandes vêm só com o apelido ("/equipe/fortaleza")
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


def ficha_certa(t: str, id_ogol: str) -> bool:
    """A página é a ficha deste clube? O endereço canônico tem de ser o do código ("/equipe/aa-sao-bento/39622"; os
    grandes, "/equipe/fortaleza"): o ogol, quando limita os pedidos, devolve a ficha de outro clube."""
    can = re.search(r'rel="canonical"\s+href="[^"]*/equipe/([^"/?]+)(?:/(\d+))?/?"', t)
    return bool(can) and id_ogol in (can.group(2), can.group(1))


def equipe(id_ogol: str, cache: Path) -> dict:
    """Ficha do clube no ogol: nome completo, cidade e UF ("Cidade: Alagoinhas (BA)"), ano de fundação."""
    url = f"{BASE}/equipe/-/{id_ogol}" if id_ogol.isdigit() else f"{BASE}/equipe/{id_ogol}"
    destino = cache / f"equipe_{id_ogol}.html"
    for tentativa in range(4):
        t = (pegar(url, destino, espera=ESPERA, de_novo=tentativa > 0) or b"").decode("utf-8", "ignore")
        if ficha_certa(t, id_ogol):
            break
        # página de limite de pedidos do ogol (lista de competições, de clubes ou a ficha de outro clube): não fica no cache
        destino.unlink(missing_ok=True)
        time.sleep(60 * (tentativa + 1))
    else:
        t = ""
    linhas = [l.strip() for l in html.unescape(re.sub(r"<[^>]+>", "\n", t)).split("\n") if l.strip()]
    def depois(rotulo):
        for i, l in enumerate(linhas[:-1]):
            if l == rotulo:
                return linhas[i + 1]
        return None
    cidade = depois("Cidade") or ""
    # "Alagoinhas (BA)", "Caaporã - PB", "Cariacica-ES", "Mucajaí, RR", "Serra Talhada/ PE" ou só a cidade
    m = re.match(r"^(.*?)\s*(?:\(|[-/,]\s*)([A-Z]{2})\)?\s*$", cidade)
    estado = depois("Estado")
    uf = m.group(2) if m else ESTADOS.get(estado or "")
    titulo = re.search(r"<title>(.*?)</title>", t, re.S)
    return {"id": id_ogol, "nome_completo": depois("Nome"), "cidade": m.group(1).strip() if m else cidade or None,
            "uf": uf, "estado": estado, "pais": depois("País") if depois("País") != "Valor" else None,
            "fundacao": depois("Ano de Fundação"), "titulo": _texto(titulo.group(1)) if titulo else None}


ESTADOS = {"Acre": "AC", "Alagoas": "AL", "Amapá": "AP", "Amazonas": "AM", "Bahia": "BA", "Ceará": "CE", "Distrito Federal": "DF",
           "Espírito Santo": "ES", "Goiás": "GO", "Maranhão": "MA", "Mato Grosso": "MT", "Mato Grosso do Sul": "MS", "Minas Gerais": "MG",
           "Pará": "PA", "Paraíba": "PB", "Paraná": "PR", "Pernambuco": "PE", "Piauí": "PI", "Rio de Janeiro": "RJ",
           "Rio Grande do Norte": "RN", "Rio Grande do Sul": "RS", "Rondônia": "RO", "Roraima": "RR", "Santa Catarina": "SC",
           "São Paulo": "SP", "Sergipe": "SE", "Tocantins": "TO"}
