"""Leitura das páginas de temporada da es.wikipedia (wikitext do Módulo Football table e da ficha)."""
import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baixar_eswiki import arquivo_temporada, temporadas, url_pagina

def wikitext(t):
    d = json.load(open(arquivo_temporada(t), encoding="utf-8"))
    return d["parse"]["title"], d["parse"]["wikitext"]["*"]

def limpa(s):
    s = re.sub(r"<ref[^>]*/>", "", s); s = re.sub(r"<ref.*?</ref>", "", s, flags=re.S)
    s = re.sub(r"\{\{(?:bandera|bandera2|band|nowrap)\|[^{}]*\}\}", "", s, flags=re.I)
    s = re.sub(r"\[\[(?:Archivo|File|Imagen):[^\]]*\]\]", "", s)
    return s

def tabelas(w):
    """Todas as chamadas do Football table: lista de dicionários de parâmetros."""
    out = []
    for m in re.finditer(r"\{\{#invoke:\s*(?:Football|Sports) table", w, re.I):
        i = m.start(); prof = 0; j = i
        while j < len(w):
            if w.startswith("{{", j): prof += 1; j += 2; continue
            if w.startswith("}}", j):
                prof -= 1; j += 2
                if prof == 0: break
                continue
            j += 1
        bloco = w[i + 2:j - 2]
        # separa parâmetros no nível 0
        partes, prof, cur, k = [], 0, "", 0
        while k < len(bloco):
            if bloco.startswith("{{", k) or bloco.startswith("[[", k): prof += 1; cur += bloco[k:k+2]; k += 2; continue
            if bloco.startswith("}}", k) or bloco.startswith("]]", k): prof -= 1; cur += bloco[k:k+2]; k += 2; continue
            if bloco[k] == "|" and prof == 0: partes.append(cur); cur = ""; k += 1; continue
            cur += bloco[k]; k += 1
        partes.append(cur)
        p = {}
        for x in partes[1:]:
            if "=" in x:
                a, b = x.split("=", 1); p[a.strip()] = re.sub(r"<!--.*?-->", "", b, flags=re.S).strip()
        out.append((i, p))
    return out

def link_alvo(s):
    m = re.search(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]+))?\]\]", s)
    return (m.group(1).strip(), (m.group(2) or m.group(1)).strip()) if m else (re.sub(r"<[^>]+>|'''?", "", s).strip(), re.sub(r"<[^>]+>|'''?", "", s).strip())

def placar(s):
    m = re.search(r"(\d+)\s*[-–]\s*(\d+)", re.sub(r"\[\[[^\]|]*\|", "", s))
    return (int(m.group(1)), int(m.group(2))) if m else None

def ficha(w):
    m = re.search(r"\{\{Ficha de (?:competici[oó]n deportiva|campeonato)(.*?)\n\}\}", w, re.S)
    f = {}
    if not m: return f
    for linha in re.split(r"\n\s*\|", m.group(1)):
        if "=" in linha:
            a, b = linha.split("=", 1); f[a.strip().lower()] = limpa(b.strip())
    return f

def links(s):
    return [a for a, _ in [link_alvo(x) for x in re.findall(r"\[\[[^\]]+\]\]", s)]]
