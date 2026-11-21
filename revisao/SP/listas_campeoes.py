"""Lê as listas de campeões da Wikipédia (en: campeão e vice; pt: campeão, vice, 3º e 4º; es) e grava
revisao/SP/listas_campeoes.json: {fonte: [{ano, liga, campeoes:[...], vices:[...], terceiro, quarto}]}"""
import sys as _s; _s.stdout.reconfigure(encoding="utf-8")
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baixar import wikitext

AQUI = os.path.dirname(os.path.abspath(__file__))


def limpa(cel):
    cel = re.sub(r"<ref[^>]*/>", "", cel)
    cel = re.sub(r"<ref.*?</ref>", "", cel, flags=re.S)
    cel = re.sub(r"\{\{nre\|.*", "", cel, flags=re.S)
    cel = re.sub(r"\{\{Futebol ([^}|]+)(\|[^}]*)?\}\}", r"\1", cel)
    cel = re.sub(r"\{\{small\|(.*?)\}\}", r"\1", cel)
    cel = re.sub(r"<sup>.*?</sup>", "", cel)
    cel = re.sub(r"<small>\s*\(\d+\)\s*</small>", "", cel)
    cel = re.sub(r"\[\[[^]|]*\|([^]]*)\]\]", r"\1", cel)
    cel = re.sub(r"\[\[([^]]*)\]\]", r"\1", cel)
    cel = re.sub(r"<[^>]+>", "", cel)
    cel = re.sub(r"\{\{[^}]*\}\}", "", cel)
    cel = re.sub(r"'''?", "", cel)
    cel = re.sub(r"\(\d+\)", "", cel)
    return cel.strip()


def tabela(txt):
    """Linhas de uma wikitable com rowspan expandido: lista de listas de células."""
    linhas = []
    pend = {}  # col -> (restante, valor)
    for bloco in re.split(r"\n\|-[^\n]*", txt)[1:]:
        cels = []
        for ln in bloco.split("\n"):
            if ln.startswith("|}"):
                break
            if ln.startswith("|") and not ln.startswith("|+"):
                for c in re.split(r"\|\|", ln[1:]):
                    cels.append(c)
            elif cels and ln.strip() and not ln.startswith("!"):
                cels[-1] += "\n" + ln
        if not cels:
            continue
        row = []
        col = 0
        it = iter(cels)
        while True:
            if col in pend and pend[col][0] > 0:
                r, v = pend[col]
                row.append(v)
                pend[col] = (r - 1, v)
                col += 1
                continue
            try:
                c = next(it)
            except StopIteration:
                # completa colunas pendentes no fim
                while col in pend and pend[col][0] > 0:
                    r, v = pend[col]; row.append(v); pend[col] = (r - 1, v); col += 1
                break
            m = re.match(r"\s*rowspan\s*=\s*\"?(\d+)\"?\s*\|(.*)", c, re.S)
            if m:
                v = limpa(m.group(2))
                pend[col] = (int(m.group(1)) - 1, v)
            else:
                m2 = re.match(r"\s*(?:style|align|bgcolor)[^|]*\|(.*)", c, re.S)
                v = limpa(m2.group(1) if m2 else c)
            row.append(v)
            col += 1
        linhas.append(row)
    return linhas


def en():
    w = wikitext("Campeonato Paulista", "en")
    i = w.find("==Champions=="); j = w.find("=== Names change")
    out = []
    for r in tabela(w[i:j]):
        if len(r) < 4 or not re.match(r"\d{4}", r[0]):
            continue
        out.append({"ano": int(r[0][:4]), "liga": r[1], "campeao": r[2], "vice": r[3]})
    return out


def pt():
    w = wikitext("Campeonato Paulista de Futebol", "pt")
    i = w.find("=== Campeonato Paulista ==="); j = w.find("=== Campeonato Paulista Extra")
    s = w[i:j]
    s = s[s.find("{|"):]
    out = []
    for r in tabela(s):
        if len(r) < 4 or not re.match(r"\d{4}", r[0]):
            continue
        out.append({"ano": int(r[0][:4]), "liga": r[1], "campeao": r[2], "vice": r[3],
                    "terceiro": r[4] if len(r) > 4 else "", "quarto": r[5] if len(r) > 5 else ""})
    return out


if __name__ == "__main__":
    d = {"en": en(), "pt": pt()}
    json.dump(d, open(os.path.join(AQUI, "listas_campeoes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    for k, v in d.items():
        print(k, len(v))
        for x in v:
            print(" ", x)
