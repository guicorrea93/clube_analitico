"""Jogos da Wikipédia em espanhol (data/coleta/bol-1/wikipedia/es_<chave>.txt), para os anos que a RSSSF não tem.

As páginas não têm modelo único; o leitor aceita os dois formatos que aparecem:
- lista: tabela com colunas "Local / Resultado / Visitante" (às vezes "Equipo Local"), com "Fecha N" no título da tabela
  ou da seção (a data da rodada vem no título da seção: "Fecha 3 — 18 de febrero de 1962");
- matriz: tabela de confrontos, com as siglas dos clubes no cabeçalho ("[[América de Cali|AME]]") e o mandante na linha.
Numa mesma seção com lista e matriz, fica a lista (a matriz repete os jogos).

A fase vem do título de seção de nível 2 ("Torneo Apertura", "Cuadrangulares semifinales", "Hexagonal final"), o grupo do
título "Grupo A". Placar com o do tribunal entre parênteses ("2 - 2 (0-1)") vale o do tribunal (awd), com o de campo na nota.
Devolve rsssf_sul.Jogo com texto "wiki-es_<chave>:<linha>".

Uso: jogos(chave) -> list[Jogo]; python coleta/bol-1/wikipedia_jogos.py <chave> ... (resumo)
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
from rsssf_sul import Jogo  # noqa: E402

PASTA = AQUI.parent.parent / "data" / "coleta" / "bol-1" / "wikipedia"
MESES = {m: k for k, m in enumerate(["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre",
                                     "octubre", "noviembre", "diciembre"], 1)}
_FORA = r"goleador|referencia|enlaces|bibliograf|fuentes|notas|datos de los clubes|equipos participantes|localizaci|" \
        r"clasificaci[oó]n$|tabla|bonificaci|desarrollo|antecedentes|sistema|hitos|clubes inscritos|estad[ií]sticas|" \
        r"campe[oó]n|p[uú]blico|asistencia|reclasificaci"
_SCORE = re.compile(r"(\d{1,2})\s*[-–:]\s*(\d{1,2})")


# título de seção -> fase do pacote ("" = fase de pontos corridos)
FASES = [
    (r"todos contra todos|^resultados|primera vuelta|segunda vuelta|fase regular|campeonato$|^torneo$|primera fase|"
     r"fase de grupos|^fixture|^partidos$", ""),
    (r"^torneo clausura|^clausura", "Clausura"), (r"segunda fase", "Segunda fase"),
    (r"partido definitorio|^campe[oó]n$", "Desempate do título"), (r"^fase final", "Fase final"),
    (r"^torneo apertura|^apertura", "Apertura"), (r"^torneo finalizaci[oó]n|^finalizaci[oó]n", "Finalización"),
    (r"octavos", "Oitavas de final"), (r"cuartos", "Quartas de final"), (r"^semifinal", "Semifinal"),
    (r"cuadrangulares semifinales|cuadrangulares$", "Quadrangulares semifinais"), (r"cuadrangular final", "Quadrangular final"),
    (r"hexagonal", "Hexagonal final"), (r"octogonal", "Octogonal final"), (r"pentagonal", "Pentagonais"),
    (r"triangular", "Triangulares"), (r"desempate", "Desempate do título"), (r"^final|gran final", "Final"),
]


def _fase(titulo: str) -> str:
    for rx, nome in FASES:
        if re.search(rx, titulo, re.I):
            return nome
    return titulo


def _limpa(c: str) -> str:
    c = re.sub(r"\[\[(?:Archivo|File|Imagen):[^\]]*\]\]|<ref[^>]*/>|<ref[^>]*>.*?(?:</ref>|$)", " ", c)
    c = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", c)
    c = re.sub(r"\{\{[^{}]*\}\}|<[^>]+>", " ", c)
    if re.match(r"^\s*(?:[a-z-]+\s*=\s*\"?[^|\"]*\"?\s*)+\|", c, re.I):   # atributos da célula: "bgcolor=#D0E7FF|'''Santa Fe"
        c = c.split("|", 1)[1]
    return re.sub(r"\s+", " ", c.replace("'''", "").replace("''", "")).strip()


def _alvo(c: str) -> str | None:
    """Alvo do link da célula: "[[América de Cali|AME]]" -> "América de Cali"."""
    m = re.search(r"\[\[([^\]|]+)\|[^\]]*\]\]", c)
    return m.group(1).strip() if m else None


def _data(txt: str, ano: int) -> str | None:
    if m := re.search(r"(\d{1,2}) de (\w+)(?: de (\d{4}))?", txt):
        mes = MESES.get(m.group(2).lower())
        if mes:
            return f"{int(m.group(3) or ano)}-{mes:02d}-{int(m.group(1)):02d}"
    return None


def _celulas(linha: str) -> list[str]:
    s = linha.strip()
    sep = "!!" if s.startswith("!") else "||"
    return [c for c in s[1:].split(sep)]


def jogos(chave: str) -> list[Jogo]:
    arq = PASTA / f"es_{chave.replace(' ', '_')}.txt"
    ls = arq.read_text(encoding="utf-8").splitlines()
    ano = int(chave[:4])
    saida: list[tuple[str, str, Jogo]] = []   # (seção, tipo, jogo)
    tit: dict[int, str] = {}
    rodada = data = None
    linhas_tab: list[tuple[int, str]] = []
    nivel_tab = 0

    def contexto() -> tuple[str, str, str]:
        """(fase, grupo, chave da seção)."""
        fase = _fase(tit.get(2, ""))
        if tit.get(3) and _fase(tit[3]) in ("Oitavas de final", "Quartas de final", "Semifinal", "Final", "Desempate do título"):
            fase = _fase(tit[3])
        grupo = ""
        for n in (3, 4):
            if m := re.match(r"(?:Grupo|Group)\s+([A-Z0-9])\b", tit.get(n, ""), re.I):
                grupo = m.group(1).upper()
        return fase, grupo, " / ".join(tit[k] for k in sorted(tit))

    def processa_tabela(tab: list[tuple[int, str]]):
        nonlocal rodada, data
        linhas = []   # [(nº da linha, [células cruas])]
        atual: list[tuple[int, str]] = []
        for i, l in tab:
            s = l.strip()
            if s.startswith("|-") or s.startswith("{|") or s.startswith("|}"):
                if atual:
                    linhas.append((atual[0][0], [c for _, c in atual]))
                atual = []
                continue
            if s.startswith(("|", "!")):
                atual += [(i, c) for c in _celulas(s)]
        if atual:
            linhas.append((atual[0][0], [c for _, c in atual]))
        # célula com rowspan=N vale também para as N-1 linhas seguintes, na mesma coluna ("Primera" da rodada, a data)
        carregadas: dict[int, list] = {}
        for k, (i, cel) in enumerate(linhas):
            nova, col = [], 0
            for c in cel + [None]:
                while col in carregadas:
                    resto, valor = carregadas[col]
                    nova.append(valor)
                    if resto <= 1:
                        del carregadas[col]
                    else:
                        carregadas[col] = [resto - 1, valor]
                    col += 1
                if c is None:
                    break
                if (mr := re.search(r"rowspan\s*=\s*\"?(\d+)", c)) and int(mr.group(1)) > 1:
                    carregadas[col] = [int(mr.group(1)) - 1, c]
                nova.append(c)
                col += 1
            linhas[k] = (i, nova)
        fase, grupo, secao = contexto()
        if re.search(_FORA, secao.split(" / ")[-1] if secao else "", re.I) and not re.search(r"resultado|fecha|partido", secao, re.I):
            return
        if re.search(r"estad[ií]stica|goleador|r[eé]cord|asistencia", tit.get(2, ""), re.I):
            return
        cab: list[str] | None = None
        siglas: list[str] | None = None
        for k, (i, cel) in enumerate(linhas):
            txt = [_limpa(c) for c in cel]
            junto = " ".join(txt).lower()
            if m := re.search(r"fecha\s+(\d+)", junto):
                if len([t for t in txt if t]) <= 2:
                    rodada = int(m.group(1))
                    data = _data(junto, ano) or data
                    continue
            if "local" in junto and "visitante" in junto:
                cab = [("local" if "local" in t.lower() else "visitante" if "visitante" in t.lower() else
                        "res" if re.search(r"resultado|marcador|score", t, re.I) else t.lower()) for t in txt]
                continue
            if cab:
                d = {cab[n]: (txt[n], cel[n]) for n in range(min(len(cab), len(txt)))}
                loc, vis, res = d.get("local"), d.get("visitante"), d.get("res")
                if loc and vis and res and (ms := _SCORE.search(res[0])):
                    gm, gv = int(ms.group(1)), int(ms.group(2))
                    esp, nota, gmo = "", "", None
                    tribunal = re.search(r"demand|dada|otorg|w\.?\s*o\b|walkover|mesa|sanci|perdi[oó] los puntos", res[1], re.I)
                    if tribunal and (mo := re.search(r"\(\s*(\d{1,2})\s*[-–:]\s*(\d{1,2})\s*\)", res[0])):
                        gmo = (int(mo.group(1)), int(mo.group(2)))
                        esp, nota = "awd", f"placar em campo {gm}-{gv}; o tribunal deu {gmo[0]}-{gmo[1]}"
                    j = Jogo(linha=i, mandante=loc[0], visitante=vis[0], gm=gm, gv=gv, rodada=rodada,
                             data=_data(d.get("fecha", ("", ""))[0], ano) or data, fase=fase, grupo=grupo, especial=esp,
                             nota=nota, texto=f"wiki-es_{chave.replace(' ', '_')}:{i}")
                    if gmo:
                        j.gm_of, j.gv_of = gmo
                    saida.append((secao, "lista", j))
                continue
            # matriz: cabeçalho com siglas que linkam para os clubes
            alvos = [_alvo(c) for c in cel]
            if sum(1 for a in alvos if a) >= 3 and not any(_SCORE.search(t) for t in txt):
                siglas = [_alvo(c) or "" for c in cel]
                desloc = 1 if not alvos[0] else 0   # 1ª célula vazia ou com o título
                siglas = siglas[desloc:] if desloc else siglas
                continue
            if siglas and len(txt) >= 3:
                mand = _alvo(cel[0]) or txt[0]
                for n, t in enumerate(txt[1:]):
                    if n >= len(siglas) or not siglas[n]:
                        continue
                    for ms in _SCORE.finditer(t):   # célula com dois jogos ("2:1 / 0:0") vira dois
                        saida.append((secao, "matriz", Jogo(linha=i, mandante=mand, visitante=siglas[n], gm=int(ms.group(1)),
                                                            gv=int(ms.group(2)), fase=fase, grupo=grupo,
                                                            texto=f"wiki-es_{chave.replace(' ', '_')}:{i}")))

    tpl: dict[str, str] | None = None
    for i, l in enumerate(ls):
        s = l.strip()
        if re.match(r"^\{\{Partidos?\b", s, re.I):   # jogo avulso (finais, mata-matas)
            tpl = {"_linha": str(i)}
            continue
        if tpl is not None:
            if s.startswith("}}"):
                ms = _SCORE.search(_limpa(tpl.get("resultado", "")))
                if ms and tpl.get("local") and (tpl.get("visita") or tpl.get("visitante")):
                    fase, grupo, secao = contexto()
                    k = int(tpl["_linha"])
                    pen = re.search(r"(\d{1,2})\s*[-–:]\s*(\d{1,2})", tpl.get("resultado penalti", "") or tpl.get("penales", ""))
                    saida.append((secao, "lista", Jogo(linha=k, mandante=_limpa(tpl["local"]),
                                                       visitante=_limpa(tpl.get("visita") or tpl["visitante"]),
                                                       gm=int(ms.group(1)), gv=int(ms.group(2)), fase=fase, grupo=grupo,
                                                       data=_data(tpl.get("fecha", ""), ano),
                                                       pen_m=int(pen.group(1)) if pen else None, pen_v=int(pen.group(2)) if pen else None,
                                                       local=_limpa(tpl.get("estadio", "")) or None,
                                                       texto=f"wiki-es_{chave.replace(' ', '_')}:{k}")))
                tpl = None
            elif mt := re.match(r"^\|\s*([\w ]+?)\s*=\s*(.*)$", s):
                tpl[mt.group(1).lower()] = mt.group(2)
            continue
        if m := re.match(r"^(=+)\s*(.*?)\s*=+\s*(<!--.*)?$", s):
            n = len(m.group(1))
            texto = _limpa(m.group(2))
            tit = {k: v for k, v in tit.items() if k < n}
            if mf := re.match(r"Fecha\s+(\d+)", texto, re.I):
                rodada, data = int(mf.group(1)), _data(texto, ano)
            elif not re.search(r"resultado|vuelta|partidos", texto, re.I) or n == 2:
                tit[n] = texto
                rodada = data = None
            continue
        if s.startswith("{|"):
            nivel_tab += 1
            if nivel_tab == 1:
                linhas_tab = []
        if nivel_tab:
            linhas_tab.append((i, l))
        if s.startswith("|}") and nivel_tab:
            nivel_tab -= 1
            if nivel_tab == 0:
                processa_tabela(linhas_tab)
    # seção com lista e matriz: fica a lista
    com_lista = {sec for sec, tp, _ in saida if tp == "lista"}
    return [j for sec, tp, j in saida if tp == "lista" or sec not in com_lista]


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for a in sys.argv[1:]:
        js = jogos(a)
        print(a, len(js), "jogos", dict(Counter((j.fase, j.grupo) for j in js)))
