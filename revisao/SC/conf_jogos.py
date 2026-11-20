"""Revisão Série C (SC): placares da Wikipédia (pt e en) x jogos do pacote, jogo a jogo.

Lê as tabelas de confrontos (Module:Sports results e tabelas cruzadas em wikitable) e os
{{Footballbox}} / {{TwoLegResult}}; casa cada jogo (mandante, visitante) com o pacote da mesma edição.
Uso: python -I revisao/SC/conf_jogos.py [ano ...]
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from comum import ler_csv  # noqa: E402
from infobox import ANOS, texto  # noqa: E402
from nomes import casar  # noqa: E402
from tabelas_wiki import _celulas, _fim_bloco, _time  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
CF = defaultdict(list)
for r in ler_csv("classificacao_final.csv"):
    CF[int(r["temporada"])].append(r["clube"])
PT = defaultdict(list)
for r in ler_csv("partidas.csv"):
    PT[int(r["temporada"])].append(r)
PLACAR = re.compile(r"^\s*(?:\[\[[^|\]]*\|)?\s*(\d+)\s*[-–—x×]\s*(\d+)\s*(?:\]\])?")


def _partes(bloco):
    corpo, prof, buf, partes, k = bloco, 0, "", [], 0
    while k < len(corpo):
        if corpo.startswith("{{", k) or corpo.startswith("[[", k):
            prof += 1; buf += corpo[k:k + 2]; k += 2; continue
        if corpo.startswith("}}", k) or corpo.startswith("]]", k):
            prof -= 1; buf += corpo[k:k + 2]; k += 2; continue
        if corpo[k] == "|" and prof == 0:
            partes.append(buf); buf = ""; k += 1; continue
        buf += corpo[k]; k += 1
    partes.append(buf)
    par = {}
    for p in partes:
        if "=" in p:
            a, b = p.split("=", 1)
            par[a.strip()] = re.sub(r"<!--.*?-->|<ref.*?</ref>|<ref[^>]*/>", "", b, flags=re.S).strip()
    return par


def jogos_sports(txt):
    out = []
    for m in re.finditer(r"\{\{\s*#invoke:\s*sports (?:results|table)", txt, re.I):
        fim = _fim_bloco(txt, m.start(), "{{", "}}")
        par = _partes(txt[m.start() + 2:fim - 2])
        nomes = {k[5:]: _time(v) for k, v in par.items() if k.startswith("name_")}
        for k, v in par.items():
            mm = re.fullmatch(r"match_(\w+?)_(\w+)", k)
            if not mm:
                continue
            a, b = mm.group(1), mm.group(2)
            if a not in nomes:   # códigos com "_": tenta dividir de outro jeito
                for i in range(1, len(k) - 6):
                    if k[6:6 + i] in nomes and k[7 + i:] in nomes:
                        a, b = k[6:6 + i], k[7 + i:]
            p = PLACAR.match(v or "")
            if p and a in nomes and b in nomes:
                out.append((nomes[a], nomes[b], int(p.group(1)), int(p.group(2)), "sports results"))
    return out


def jogos_cruzada(txt):
    out = []
    for m in re.finditer(r"(?m)^\{\|", txt):
        fim = _fim_bloco(txt, m.start(), "{|", "|}")
        linhas = re.split(r"\n\|-[^\n]*", txt[m.start():fim - 2])
        rows = []
        for lt in linhas:
            cels = [c for t, c in _celulas(lt)]
            if len(cels) < 3:
                continue
            t = _time(cels[0]) if not PLACAR.match(cels[0]) else None
            if not t:
                continue
            vals = cels[1:]
            ok = [bool(PLACAR.match(v)) or v.strip() in ("-", "—", "–", "x", "X", "", "&nbsp;", "XXX") for v in vals]
            if sum(1 for v in vals if PLACAR.match(v)) >= 1 and all(ok[:len(vals)]):
                rows.append((t, vals))
        n = len(rows)
        if n < 3 or any(len(v) != n for _, v in rows):
            continue
        for i, (t, vals) in enumerate(rows):
            for j, v in enumerate(vals):
                p = PLACAR.match(v)
                if p and i != j:
                    out.append((t, rows[j][0], int(p.group(1)), int(p.group(2)), "tabela cruzada"))
    return out


def jogos_caixas(txt):
    out = []
    for m in re.finditer(r"\{\{\s*(?:Footballbox|footballbox collapsible|Futebol caixa|Partida)[^{]*", txt, re.I):
        fim = _fim_bloco(txt, m.start(), "{{", "}}")
        par = _partes(txt[m.start() + 2:fim - 2])
        a, b, s = par.get("team1") or par.get("time1"), par.get("team2") or par.get("time2"), par.get("score") or par.get("resultado")
        p = PLACAR.match(re.sub(r"\{\{[^}]*\}\}|'''?", "", s or ""))
        if a and b and p:
            out.append((_time(a), _time(b), int(p.group(1)), int(p.group(2)), "footballbox"))
    return out


def jogos_ida_volta(txt):
    """{{TwoLegResult|time1|band|agregado|time2|band|ida|volta}}: ida com o time1 em casa; volta com o time2 em casa."""
    out = []
    for m in re.finditer(r"\{\{\s*TwoLegResult\s*\|", txt, re.I):
        fim = _fim_bloco(txt, m.start(), "{{", "}}")
        corpo, prof, buf, partes, k = txt[m.start() + 2:fim - 2], 0, "", [], 0
        while k < len(corpo):
            if corpo.startswith("{{", k) or corpo.startswith("[[", k):
                prof += 1; buf += corpo[k:k + 2]; k += 2; continue
            if corpo.startswith("}}", k) or corpo.startswith("]]", k):
                prof -= 1; buf += corpo[k:k + 2]; k += 2; continue
            if corpo[k] == "|" and prof == 0:
                partes.append(buf); buf = ""; k += 1; continue
            buf += corpo[k]; k += 1
        partes.append(buf)
        partes = partes[1:]
        if len(partes) < 7:
            continue
        a, b = _time(partes[0]), _time(partes[3])

        def limpa(x):
            return re.sub(r"\{\{[^}]*\}\}|'''?|\(.*?\)|<[^>]+>|\[\[|\]\]", "", x)
        p1, p2 = PLACAR.match(limpa(partes[5])), PLACAR.match(limpa(partes[6]))
        if a and b and p1:
            out.append((a, b, int(p1.group(1)), int(p1.group(2)), "TwoLegResult"))
        if a and b and p2:
            out.append((b, a, int(p2.group(2)), int(p2.group(1)), "TwoLegResult"))
    return out


def main(anos):
    tot = defaultdict(int)
    for ano in anos:
        clubes = CF[ano]
        for lg in ("pt", "en"):
            txt, _ = texto(lg, ano)
            if not txt:
                continue
            vistos = set()
            for a, b, ga, gb, tipo in jogos_sports(txt) + jogos_cruzada(txt) + jogos_caixas(txt) + jogos_ida_volta(txt):
                ca, cb = casar(a, clubes, ano), casar(b, clubes, ano)
                if not ca or not cb or (ca, cb, ga, gb) in vistos:
                    if not (ca and cb):
                        tot["sem_casar"] += 1
                    continue
                vistos.add((ca, cb, ga, gb))
                tot["jogos"] += 1
                cand = [r for r in PT[ano] if r["mandante"] == ca and r["visitante"] == cb]
                if any(r["gols_mandante"] == str(ga) and r["gols_visitante"] == str(gb) for r in cand):
                    tot["iguais"] += 1
                    continue
                inv = [r for r in PT[ano] if r["mandante"] == cb and r["visitante"] == ca and r["gols_mandante"] == str(gb)
                       and r["gols_visitante"] == str(ga)]
                if inv:
                    tot["mando_invertido"] += 1
                    print(f"{ano} {lg} {tipo}: {ca} {ga}-{gb} {cb} | pacote tem com mando invertido: {inv[0]['id']}")
                    continue
                tot["diferentes"] += 1
                print(f"{ano} {lg} {tipo}: {ca} {ga}-{gb} {cb} | pacote: " +
                      ("; ".join(f"{r['id']} {r['fase']} {r['gols_mandante']}-{r['gols_visitante']}" for r in cand) or "jogo não existe"))
        print(f"-- {ano}: {dict(tot)}", flush=True)
    print("TOTAL", dict(tot))


if __name__ == "__main__":
    main([int(a) for a in sys.argv[1:]] or ANOS)
