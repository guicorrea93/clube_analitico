"""Calendário de uma edição no ogol (zerozero), comum às coletas da CONCACAF (copiado de coleta/comum-sulamerica/ogol.py em 23/11/2026).

De cada jogo: data e hora, mandante, visitante, placar, fase ou rodada ("R12" = 12ª rodada) e o link do jogo.
As páginas baixadas ficam em data/cache/ogol_<slug>/ (rodar de novo não baixa outra vez).

Uso como biblioteca: calendario(id_edicao, cache) -> list[dict]
"""
from __future__ import annotations

import html
import re
from pathlib import Path

import time

from baixar import pegar

BASE = "https://www.ogol.com.br"


def _texto(v: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", v))).strip()


def calendario(ed: int, cache: Path, prefixo: str) -> list[dict]:
    jogos, vistos = [], set()
    for pagina in range(1, 60):
        arq = cache / f"{prefixo}_{ed}_p{pagina}.html"
        for tentativa in range(4):
            t = pegar(f"{BASE}/edicao/-/{ed}/calendario?page={pagina}", arq, espera=2.5)
            if t and b"<title>Calend" in t and re.search(rb'href="/edicao/[^"/]*/' + str(ed).encode() + rb'/calendario', t):
                break
            # o ogol às vezes responde com a página "Competições" (limite de ritmo) ou com o calendário de outra edição:
            # apaga, espera e tenta de novo
            arq.unlink(missing_ok=True)
            time.sleep(15 * (tentativa + 1))
        else:   # não veio a página certa: para aqui (a edição fica incompleta) e avisa
            print(f"AVISO: ogol não devolveu o calendário da edição {ed}, página {pagina}; edição incompleta", flush=True)
            break
        t = (t or b"").decode("utf-8", "ignore")
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


def equipe(id_ogol: str, cache: Path) -> dict:
    """Ficha do clube no ogol: nome completo, cidade e UF ("Cidade: Alagoinhas (BA)"), ano de fundação."""
    url = f"{BASE}/equipe/-/{id_ogol}" if id_ogol.isdigit() else f"{BASE}/equipe/{id_ogol}"
    t = (pegar(url, cache / f"equipe_{id_ogol}.html", espera=1.2) or b"").decode("utf-8", "ignore")
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
