"""Leitor das páginas do Bola n@ Área (data/coleta/bra-serie-c/bola/, de baixar_bola.py) das Séries C não oficiais de
1987 e 2000 (decisão D-10, achado SC-029). A página é lida célula a célula (o mesmo jeito de revisao/QC/bola.py):

- participantes: "GRUPO G", depois o nome em maiúsculas e "(Cidade/UF)" (às vezes quebrado em duas células);
- jogos: títulos de fase ("PRIMEIRA FASE", "SEGUNDA FASE", "FASE FINAL"...), "GRUPO X", a data ("12/10/1987 - Segunda"),
  o jogo numa célula ("Mixto 2x1 Operário-MS") ou em três ("Auto Esporte" / "0x1" / "Mixto"), e os detalhes logo abaixo
  ("Local: ...", "Público: ...; Árbitro: ...", "Gols: ..."); "*x*" é jogo cancelado e fica de fora; as tabelas de
  classificação são lidas à parte (conferência).

ler(pagina) -> {"participantes": [{grupo, nome, cidade, uf}], "jogos": [{fase, grupo, data, hora, mandante, visitante,
gm, gv, local, publico, gols_texto, nota}], "tabelas": [{fase, grupo, linhas: [{pos, nome, uf, pts, j, v, e, d, gp, gc}]}]}
"""
from __future__ import annotations

import html
import re
import unicodedata

from edicoes import PASTA_DADOS

PASTA = PASTA_DADOS / "bola"
QUEBRA = "\u0001"
FASES = {"PRIMEIRA FASE": "Primeira fase", "SEGUNDA FASE": "Segunda fase", "TERCEIRA FASE": "Terceira fase",
         "QUARTA FASE": "Quarta fase", "QUINTA FASE": "Quinta fase", "OITAVAS DE FINAL": "Oitavas de final",
         "QUARTAS DE FINAL": "Quartas de final", "SEMIFINAL": "Semifinal", "SEMIFINAIS": "Semifinal", "FASE FINAL": "Fase final",
         "FINAL": "Final", "FINAIS": "Final", "QUADRANGULAR FINAL": "Fase final", "TRIANGULAR FINAL": "Fase final"}
DATA = re.compile(r"^(\d{1,2})/(\d{1,2})/(\d{4})\b")
PLACAR = re.compile(r"^(\d{1,2}|\*)\s*x\s*(\d{1,2}|\*)(?:\s*\(.*\))?$", re.I)
JOGO = re.compile(r"^(.+?)\s+(\d{1,2}|\*)\s*x\s*(\d{1,2}|\*)\s+(.+?)\s*\*?$", re.I)
HORA = re.compile(r"^\d{1,2}h\d{2}$")


def chave(n: str) -> str:
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", n or "").encode("ascii", "ignore").decode().lower())


def celulas(s: str) -> list[str]:
    s = re.sub(r"<script.*?</script>|<style.*?</style>", " ", s, flags=re.S | re.I)
    s = re.sub(r"</?(?:font|b|i|u|span|a|strong|em|sup|sub)(?:\s[^>]*)?>", "", s, flags=re.I)
    s = re.sub(r"<(?:br|/p|p|/div|div|/td|td|/th|th|/tr|tr|/li|li|table|/table|h\d|/h\d)(?:\s[^>]*)?/?>", QUEBRA, s, flags=re.I)
    s = html.unescape(re.sub(r"<[^>]+>", " ", s)).replace("\xa0", " ")
    return [x for x in (re.sub(r"\s+", " ", p).strip() for p in s.split(QUEBRA)) if x and x != "."]


def _titulo(c: str) -> str | None:
    t = re.sub(r"\s+", " ", c.upper()).strip()
    return FASES.get(t)


def ler(pagina: str) -> dict:
    cs = celulas((PASTA / f"{pagina}.htm").read_bytes().decode("latin-1"))
    part, jogos, tabelas = [], [], []
    fase, grupo, data, hora = None, "", None, None
    i, n = 0, len(cs)
    # participantes: do "PARTICIPANTES" até o primeiro título de fase (a página da fase final de 2000 não tem a lista).
    # 1987: nome em maiúsculas e "(Cidade/UF)" embaixo; 2000: em duas colunas, dois nomes e depois as duas "(UF)"
    primeiro = next((k for k, c in enumerate(cs) if _titulo(c)), n)
    ini = next((k for k, c in enumerate(cs[:primeiro]) if "PARTICIPANTES" in c.upper()), None)
    g, pendentes = "", []
    k = (ini + 1) if ini is not None else primeiro
    while k < primeiro:
        c = cs[k]
        m = re.match(r"^GRUPO\s+(\S+)$", c, re.I)
        if m:
            g, pendentes = m.group(1).upper(), []
        elif c.startswith("("):
            txt = c
            while ")" not in txt and k + 1 < primeiro:   # "(Santa Cruz do" / "Sul/RS)"
                k += 1
                txt += " " + cs[k]
            mc = re.match(r"^\((?:(.+?)/)?([A-Z]{2})\)$", txt)
            if mc and pendentes:
                pendentes.pop(0).update(cidade=mc.group(1).strip() if mc.group(1) else None, uf=mc.group(2))
        elif not re.search(r"\d", c) and len(c) <= 40:
            if pendentes and c.isupper() and pendentes[-1]["nome"].isupper() and not pendentes[-1]["nome"].endswith(")")                     and len(pendentes) == 1 and k > 0 and not cs[k - 1].startswith("(") and cs[k - 1] == pendentes[-1]["nome"]                     and len(pendentes[-1]["nome"].split()) >= 2 and pendentes[-1]["nome"].split()[-1] in ("DO", "DA", "DE", "DOS"):
                pendentes[-1]["nome"] += " " + c   # nome quebrado: "ESTRELA DO" / "NORTE"
            else:
                novo = {"grupo": g, "nome": c, "cidade": None, "uf": None}
                part.append(novo)
                pendentes.append(novo)
        k += 1
    i = primeiro
    nomes = {chave(p["nome"]) for p in part}
    while i < n:
        c = cs[i]
        t = _titulo(c)
        if t:
            fase, grupo = t, ""
            i += 1
            continue
        m = re.match(r"^GRUPO\s+(\S+)$", c, re.I)
        if m:
            grupo = m.group(1).upper()
            i += 1
            continue
        if c.upper() == "CLASSIFICAÇÃO":   # tabela: pos, "Nome (UF)", 8 números
            linhas = []
            i += 1
            while i < n and cs[i] in ("PG", "J", "V", "E", "D", "GP", "GC", "SG", "C", "PARTICIPANTES"):
                i += 1
            while i + 9 < n and re.match(r"^\d+º$", cs[i]):
                mn = re.match(r"^(.+?)\s*\(([A-Z]{2})\)$", cs[i + 1])
                nums = cs[i + 2:i + 10]
                if not mn or not all(re.match(r"^-?\d+$", x) for x in nums):
                    break
                pts, j, v, e, d, gp, gc, _ = map(int, nums)
                linhas.append({"pos": int(cs[i][:-1]), "nome": mn.group(1), "uf": mn.group(2), "pts": pts, "j": j, "v": v,
                               "e": e, "d": d, "gp": gp, "gc": gc})
                i += 10
            tabelas.append({"fase": fase, "grupo": grupo, "linhas": linhas})
            continue
        md = DATA.match(c)
        if md:
            data = f"{md.group(3)}-{int(md.group(2)):02d}-{int(md.group(1)):02d}"
            hora = None
            i += 1
            continue
        if HORA.match(c):
            hora = c.replace("h", ":")
            i += 1
            continue
        jogo, prox = None, i + 1
        mj = JOGO.match(c)
        if mj and fase and len(c) < 80 and not c.startswith(("Local", "Público", "Gol")):
            jogo = [mj.group(1), mj.group(2), mj.group(3), mj.group(4)]
        elif fase and PLACAR.match(c) and 0 < i and i + 1 < n:
            jogo = [cs[i - 1], *PLACAR.match(c).groups(), cs[i + 1]]
            prox = i + 2
        if jogo and jogo[0].startswith("(") and jogos:
            # "(Nos pênaltis: Juventus 4x5 Botafogo-SP)" e "(Na prorrogação: Uberlândia 3x0 Corumbaense)": do jogo anterior
            ant = jogos[-1]
            ma, mv = re.sub(r"^\(.*?:\s*", "", jogo[0]), jogo[3].rstrip(") ")
            gm, gv = (int(jogo[1]), int(jogo[2])) if chave(ma) == chave(ant["mandante"]) else (int(jogo[2]), int(jogo[1]))
            if "nalti" in jogo[0]:
                ant["pen_m"], ant["pen_v"] = gm, gv
            else:   # o placar oficial inclui a prorrogação (como no banco e nas tabelas do Bola)
                ant["nota"] = "; ".join(x for x in (ant["nota"], f"prorrogação {gm}-{gv}; no tempo normal {ant['gm']}-{ant['gv']}") if x)
                ant["gm"], ant["gv"] = ant["gm"] + gm, ant["gv"] + gv
            i = prox
            continue
        if jogo:
            # visitante quebrado em duas células ("Santa" / "Cruz"): junta se o nome junto é de um participante
            if prox < n and chave(jogo[3]) not in nomes and chave(jogo[3] + cs[prox]) in nomes:
                jogo[3] += " " + cs[prox]
                prox += 1
            det = []
            while prox < n and not (_titulo(cs[prox]) or DATA.match(cs[prox]) or HORA.match(cs[prox])
                                    or JOGO.match(cs[prox]) or re.match(r"^GRUPO\s", cs[prox], re.I)
                                    or cs[prox].upper() == "CLASSIFICAÇÃO" or (prox + 1 < n and PLACAR.match(cs[prox + 1]))):
                det.append(cs[prox])
                prox += 1
            txt = " ".join(det)
            cancelado = "*" in (jogo[1], jogo[2])
            local = re.search(r"Local:\s*([^;]+)", txt)
            pub = re.search(r"P[úu]blico:\s*([\d.]+)", txt)
            gols = re.search(r"Gols?:\s*(.+?)(?:;?\s*(?:Expuls|[A-ZÀ-Ú]{4,}:)|$)", txt)
            if not cancelado:
                jogos.append({"fase": fase, "grupo": grupo, "data": data, "hora": hora, "mandante": jogo[0].strip(" *"),
                              "visitante": jogo[3].strip(" *"), "gm": int(jogo[1]), "gv": int(jogo[2]),
                              "local": (local.group(1).strip() if local else (det[0] if det and "(" in det[0] and ":" not in det[0] else None)),
                              "publico": int(pub.group(1).replace(".", "")) if pub and pub.group(1).strip(".") else None,
                              "gols_texto": gols.group(1).strip() if gols else "", "nota": txt if re.search(r"\*|W\.?O|cancel|anulad", txt, re.I) else ""})
            hora = None
            i = prox
            continue
        i += 1
    return {"participantes": part, "jogos": jogos, "tabelas": tabelas}


if __name__ == "__main__":
    import sys
    from collections import Counter
    sys.stdout.reconfigure(encoding="utf-8")
    for p in sys.argv[1:]:
        r = ler(p)
        print(p, len(r["participantes"]), "participantes;", len(r["jogos"]), "jogos;", len(r["tabelas"]), "tabelas;",
              dict(Counter((j["fase"], j["grupo"]) for j in r["jogos"])))
