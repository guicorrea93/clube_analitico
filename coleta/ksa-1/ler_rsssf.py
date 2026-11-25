"""Lê as páginas da RSSSF da liga saudita (data/coleta/ksa-1/rsssf/sauNN.html e sauNNNN.html, uma por temporada; o nome
é o ano em que a temporada termina).

Cada página traz, em seções: a tabela final (às vezes por grupo), as rodadas da liga com os jogos, o playoff do título
(1990/91 a 2006/07, "Golden Box") e as copas do ano (Copa do Rei, Copa do Príncipe Herdeiro, Copa da Federação...). A
leitura é por linha:
- título de seção: linha sem placar que não é data nem autores ("Round 1", "Playoffs", "Kings Cup 1991/92"...); a seção
  vale para os jogos abaixo, e o que vem depois de uma copa ou de outra divisão não é da liga (ver `da_liga`);
- data: "[Oct 24]", "Round 1 [Oct 15,16]" (vale a primeira) ou no fim da linha do jogo ("... [Dec 18]", jogo remarcado);
- jogo: "Mandante   2-1  Visitante"; ida e volta numa linha só: "Ahly 0-2 0-0 Ittifaq";
- autores: a linha de baixo entre colchetes, "[Nasser Eid 55, 61; Idris Adam 85]" (mandante; visitante), com o minuto em
  vários jeitos ("34", "(54')", "45+1", "50pen", "7og", "(og)");
- tabela: "1.Al-Hilal  14 11 3 0 34- 8 25 ...".

Uso como biblioteca: pagina(fim) -> {"tabelas": [...], "jogos": [...]}; para ver: python coleta/ksa-1/ler_rsssf.py <fim>
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PASTA = AQUI.parent.parent / "data" / "coleta" / "ksa-1" / "rsssf"
MESES = {m: i + 1 for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split())}
NOME = r"[A-Za-z'][\w'.,&()/ -]*?[\w.)']"
JOGO = re.compile(rf"^\s*({NOME})\s+(\d+)\s*-\s*(\d+)\s+(?:(\d+)\s*-\s*(\d+)\s+)?({NOME})(?:\s{{2,}}|\s*\[|\s*\(|\s*$)(.*)$")
AWD = re.compile(r"^\s*([A-Za-z'][\w'.,&()/ -]*?[\w.)'])\s+awd\s+([A-Za-z'][\w'.,&()/ -]*?[\w.)'])\s*(\[.*)$")
NOME_T = r"[A-Za-z'][A-Za-z'.,&()/ -]*?[A-Za-z.)']"   # nome na tabela: sem dígitos
TABELA = re.compile(rf"^\s*(\d+)\.\s*({NOME_T})#?\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*-\s*(\d+)\s+(\d+)\s*(.*)$")
# tabelas incompletas dos anos 1977-1986: só jogos e pontos ("1.Al-Ahli  18   29  Champions") ou só a ordem
TABELA_CURTA = re.compile(rf"^\s*(\d+)\.\s*({NOME_T})\s+(\d+)\s{{3,}}(\d+)\s*(\D.*)?$")
TABELA_ORDEM = re.compile(rf"^\s*(\d+)\.\s*({NOME_T})\s*$")
FORA_DA_LIGA = re.compile(r"(?i)\bcup\b|division\s*[12]|first division|second division|super cup|champions cup|"
                          r"federation|olympic|youth|reserve|friendl|crown prince|kings? cup|golden cup")


def texto(fim: int) -> str:
    for nome in (f"sau{fim % 100:02d}.html", f"sau{fim}.html"):
        arq = PASTA / nome
        if arq.exists():
            b = arq.read_bytes()
            t = b.decode("utf-16") if b[:2] in (b"\xff\xfe", b"\xfe\xff") else b.decode("latin-1")
            return html.unescape(re.sub(r"<[^>]+>", "", t)).replace("\r", "").replace("\t", "    ")
    return ""


def _data(s: str, fim: int) -> str | None:
    m = re.search(r"\[(?:[A-Za-z]+,?\s+)?([A-Za-z]{3})[a-z]*\.?\s+(\d{1,2})\b[^\]]*\]", s)
    if not m or m.group(1).lower() not in MESES:
        return None
    mes = MESES[m.group(1).lower()]
    ano = fim - 1 if mes >= 8 else fim   # temporada de agosto a julho (há finais em julho)
    a = re.search(r"\b(19\d\d|20\d\d)\b", s[m.start():m.end()])
    return f"{a.group(1) if a else ano}-{mes:02d}-{int(m.group(2)):02d}"


def autores(texto_: str, gm: int, gv: int) -> tuple[list, list] | None:
    """"[Nasser Eid 55, 61; Idris Adam 85]" -> ([(nome, minuto, tipo)...] do mandante, [...] do visitante); None quando
    não dá para separar os lados. tipo: normal, penalti, contra."""
    s = texto_.strip()
    if s.startswith("["):
        s = s[1:]
    s = s.rsplit("]", 1)[0]
    s = re.sub(r"\(([^()]*)\)", lambda m: "(" + m.group(1).replace(";", ",") + ")", s)   # "(20'; 40')": mesmo jogador
    if not s.strip():
        return None
    if ";" in s:
        lados = s.split(";")
    elif " - " in s and gm and gv:   # "Roberto Anderson (54') - Abdullah Al-Waked (52'), ..."
        lados = s.split(" - ", 1)
    elif gm and gv:
        return None
    else:
        lados = [s, ""] if gm else ["", s]
    if len(lados) != 2:
        return None
    saida = []
    for lado in lados:
        gols = []
        for parte in re.finditer(r"([A-Za-z'][^\d;,()]*?)\s*((?:\(?\s*\d+(?:\+\d+)?'?\s*(?:pen|PK|p|og|o\.g\.)?\s*\)?\s*[,;]?\s*)+|\((?:og|pen)\))",
                                 lado):
            nome = parte.group(1).strip(" .'-")
            if not nome or nome.lower() in ("og", "pen"):
                continue
            mins = re.findall(r"(\d+)(?:\+(\d+))?'?\s*(pen|PK|p|og|o\.g\.)?", parte.group(2))
            if not mins:   # "(og)" sem minuto
                gols.append((nome, None, "contra" if "og" in parte.group(2) else "normal"))
            for mi, ac, tp in mins:
                tipo = "contra" if tp and tp.lower().startswith("o") else "penalti" if tp else "normal"
                gols.append((nome, int(mi) + int(ac or 0), tipo))
        saida.append(gols)
    return saida[0], saida[1]


def pagina(fim: int) -> dict:
    linhas = texto(fim).split("\n")
    tabelas, jogos = [], []
    secao, data, fora, viu_liga = "", None, False, False
    i = 0
    while i < len(linhas):
        linha = linhas[i]
        s = linha.strip()
        i += 1
        if not s:
            continue
        artilheiros = re.search(r"(?i)scorer", secao)
        t = None if artilheiros else TABELA.match(linha)
        tc = None if t or artilheiros else TABELA_CURTA.match(linha) or TABELA_ORDEM.match(linha)
        if tc:
            curta = tc.re is TABELA_CURTA
            tabelas.append({"secao": secao, "pos": int(tc.group(1)), "nome": tc.group(2).strip(),
                            "jogos": int(tc.group(3)) if curta else None, "v": None, "e": None, "d": None, "gp": None,
                            "gc": None, "pontos": int(tc.group(4)) if curta else None,
                            "obs": (tc.group(5) or "").strip() if curta else "", "fora": fora})
            viu_liga = viu_liga or not fora
            continue
        if t:
            tabelas.append({"secao": secao, "pos": int(t.group(1)), "nome": t.group(2).strip(), "jogos": int(t.group(3)),
                            "v": int(t.group(4)), "e": int(t.group(5)), "d": int(t.group(6)), "gp": int(t.group(7)),
                            "gc": int(t.group(8)), "pontos": int(t.group(9)), "obs": t.group(10).strip(), "fora": fora})
            viu_liga = viu_liga or not fora
            continue
        a = AWD.match(linha)
        if a:   # "Urooba  awd Nasr  [awarded 0-3, originally 2-1; Urooba fielded ineligible player]" (pode seguir na linha de baixo)
            txt = a.group(3)
            k = i
            while "]" not in txt and k < len(linhas) and k < i + 3:
                txt += " " + re.sub(r"^.*?\s{3,}", "", linhas[k].strip()) if re.search(r"\s{3,}\S", linhas[k]) else " " + linhas[k].strip()
                k += 1
            dado = re.search(r"awarded (\d+)-(\d+)", txt)
            campo = re.search(r"originally (\d+)-(\d+)", txt)
            if dado:
                jogos.append({"secao": secao, "fora": fora, "data": _data(txt, fim) or data, "mandante": a.group(1).strip(),
                              "visitante": a.group(2).strip(), "obs": txt.strip(" []"), "linha": s, "autores": "",
                              "gm": int(dado.group(1)), "gv": int(dado.group(2)), "awd": True,
                              "campo": (int(campo.group(1)), int(campo.group(2))) if campo else None})
                viu_liga = viu_liga or not fora
            continue
        j = JOGO.match(linha)
        if j and not re.match(r"^\s*\d+\.", linha):
            d = _data(j.group(7), fim) or data
            aut, k = "", i
            while k < len(linhas) and not linhas[k].strip():
                k += 1
            prox = linhas[k].strip() if k < len(linhas) else ""
            if prox.startswith("[") and not _data(prox, fim):
                aut = prox
                while "]" not in aut and k + 1 < len(linhas):
                    k += 1
                    aut += " " + linhas[k].strip()
                i = k + 1
            base = {"secao": secao, "fora": fora, "data": d, "mandante": j.group(1).strip(), "visitante": j.group(6).strip(),
                    "obs": j.group(7).strip(), "linha": s}
            if j.group(4) is not None:   # ida e volta na mesma linha
                jogos.append(dict(base, gm=int(j.group(2)), gv=int(j.group(3)), autores="", perna=1))
                jogos.append(dict(base, mandante=base["visitante"], visitante=base["mandante"], gm=int(j.group(5)),
                                  gv=int(j.group(4)), autores="", perna=2))
            else:
                jogos.append(dict(base, gm=int(j.group(2)), gv=int(j.group(3)), autores=aut))
            viu_liga = viu_liga or not fora
            continue
        d = _data(s, fim)
        if d:
            data = d
            cab = re.sub(r"\[[^\]]*\]", "", s).strip()
            if cab and not cab.startswith("["):
                secao = cab
            continue
        if s.startswith("["):
            continue
        if len(s) < 70 and not re.search(r"\d+\s*-\s*\d+", s) and not s.startswith(("NB", "(", "*", "-")):
            secao = s
            if FORA_DA_LIGA.search(s) and viu_liga:   # nota antes da liga ("... Saudi First Division") não conta
                fora = True
            elif re.match(r"(?i)^(round|playoff|semi|final|championship|regular|group|saudi league|professional league|"
                          r"premier league|league|table|final table)", s):
                fora = fora and not re.match(r"(?i)^(saudi league|professional league|premier league|regular)", s)
    return {"tabelas": tabelas, "jogos": jogos}


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    p = pagina(int(sys.argv[1]))
    for x in p["tabelas"]:
        print("T", x["fora"], x["secao"][:20], x["pos"], x["nome"], x["jogos"], x["gp"], x["gc"], x["pontos"])
    for x in p["jogos"]:
        print("J", x["fora"], x["secao"][:25], x["data"], x["mandante"], x["gm"], x["gv"], x["visitante"], "|", x["autores"][:60])
