"""Jogos e tabelas da Wikipédia em português para as edições da A2 que a RSSSF não traz completas.

Fonte: as páginas "Campeonato Paulista de Futebol de {ano} - {divisão}" (código-fonte em data/coleta/bra-sp-2/wikipedia/
pt_{ano}.wiki) e a transcrição dos jogos delas em jogos_pt.csv (ano;pagina;secao;data;mandante;gols_mandante;
gols_visitante;visitante;nota). Cada jogo do CSV com placar foi conferido no código da página (os dois clubes e o placar
no mesmo trecho): 244 de 244. Jogos só com o resultado ("V"/"E"/"D", sem placar) ficam fora.

Uso: python coleta/bra-sp-2/wikipedia_sp2.py [ano ...]     (lista os jogos lidos)
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from edicoes import PASTA_DADOS  # noqa: E402

PASTA = PASTA_DADOS / "wikipedia"
MESES = {m: i for i, m in enumerate(["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro",
                                     "outubro", "novembro", "dezembro"], 1)}

# (temporada, seção da página) -> (fase, grupo); None: o jogo fica fora
FASE: dict[tuple[str, str], tuple[str, str] | None] = {
    ("1948", "Série Vermelha"): ("Primeira fase - Desempate", "Série Vermelha"),   # Rio Pardo x São Caetano, 1º lugar
    ("1948", "Triangular final"): ("Segunda fase", ""),
    ("1949", "Primeiro turno"): ("Segunda fase", ""), ("1949", "Segundo turno"): ("Segunda fase", ""),
    ("1949", "Jogo de desempate"): ("Final", ""),   # Guarani x Batatais, empatados no Torneio dos Campeões
    # 1951: XV de Jaú x Jabaquara (o último da 1ª divisão), repescagem entre as divisões: não é jogo da A2
    ("1951", "Primeiro jogo"): None, ("1951", "Segundo jogo"): None, ("1951", "Terceiro jogo"): None,
    ("1953", "Primeiro turno"): ("Segunda fase", ""), ("1953", "Segundo turno"): ("Segunda fase", ""),
    ("1954", "Primeiro turno"): ("Segunda fase", ""), ("1954", "Segundo turno"): ("Segunda fase", ""),
    ("1955", "Penúltima partida da fase final"): ("Segunda fase", ""),
    ("1957", 'Última rodada do "Torneio dos Finalistas"'): ("Segunda fase", ""),
    ("1959", "Resultados da fase final"): ("Segunda fase", ""), ("1959", "Jogo decisivo"): ("Segunda fase", ""),
    ("1960", "Jogo decisivo"): ("Primeira fase", ""),   # última rodada do turno e returno
    ("1962", "1º jogo"): ("Final", ""), ("1962", "2º jogo"): ("Final", ""), ("1962", "3º jogo"): ("Final", ""),
    ("1963", "Jogos decisivos"): ("Segunda fase", ""), ("1964", "Forma de disputa"): ("Segunda fase", ""),
    # 1988: a final já está na RSSSF
    ("1988", "Jogo de ida"): None, ("1988", "Jogo de volta"): None,
    ("1990", "Quarta fase"): ("Quarta fase", ""),
    ("1992", "Grupo E"): ("Segunda fase", "Grupo E"), ("1992", "Grupo F"): ("Segunda fase", "Grupo F"),
    ("1992", "Grupo G"): ("Segunda fase", "Grupo G"), ("1992", "Quadrangular final"): ("Fase final", ""),
}
PADRAO = {"Final": ("Final", ""), "Semifinal": ("Semifinal", "")}


def _data(txt: str, temporada: str) -> str | None:
    """"Domingo, 27 de janeiro de 1952", "4 de outubro" (o ano da edição), "01/12/1990" -> "AAAA-MM-DD"."""
    t = re.sub(r"^[^\d]*,\s*", "", (txt or "").strip())
    if m := re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})$", t):
        d, mes, a = int(m.group(1)), int(m.group(2)), int(m.group(3))
        a = a if a >= 1940 else int(temporada)   # "01/12/1900" na página de 1990
        return f"{a:04d}-{mes:02d}-{d:02d}"
    if m := re.match(r"(\d{1,2})\s+de\s+([a-zç]+)(?:\s+de\s+(\d{4}))?$", t, re.I):
        mes = MESES.get(m.group(2).lower())
        if mes:
            return f"{int(m.group(3) or temporada):04d}-{mes:02d}-{int(m.group(1)):02d}"
    return None


# 1967-1984: (temporada, seção) do jogo -> (fase, grupo), quando a regra de _fase_jogo não acerta
FASE_JOGO_NOVA: dict[tuple[str, str], tuple[str, str]] = {
    ("1967", "Fase final"): ("Segunda fase", ""),   # os 4 finalistas; o triangular decisivo é a fase final
    ("1977", "Fase final / Jogo decisivo"): ("Final", ""),   # desempate Francana x Araçatuba, empatados no grupo final
    ("1983", "Rebolo"): None,   # Noroeste x Taubaté, vaga na 1ª divisão: playoff fora da liga, só na observação (D-04)
}
NOVAS = {str(a) for a in (*range(1967, 1979), *range(1980, 1985))}


def _fase_jogo(temporada: str, secao: str) -> tuple[str, str]:
    if (temporada, secao) in FASE_JOGO_NOVA:
        return FASE_JOGO_NOVA[(temporada, secao)]
    s = secao.lower()
    if "semifina" in s:
        g = re.search(r"grupo \w+", secao, re.I)
        return "Semifinal", g.group(0) if g else ""
    if s.startswith("final"):
        return "Final", ""
    # "Jogo decisivo", "Última rodada", rodadas e quadrangulares: jogos da fase final (de grupo)
    return "Fase final", ""


def _jogos_novos(temporada: str) -> list[dict]:
    saida = []
    for j in jogos_footballbox(temporada) + jogos_em_linha(temporada):
        if FASE_JOGO_NOVA.get((temporada, j["secao"]), ()) is None:
            continue
        fase, grupo = _fase_jogo(temporada, j["secao"])
        nomes = [re.sub(r"\s*\([^()]*\)\s*$|\*", "", j[k]).strip() for k in ("mandante", "visitante")]
        nota = "; ".join(x for x in (j["nota"], f"pênaltis {j['pen'][0]}-{j['pen'][1]}" if j["pen"] else "") if x)
        saida.append({"fase": fase, "grupo": grupo, "data": j["data"], "mandante": nomes[0], "visitante": nomes[1], "gm": j["gm"],
                      "gv": j["gv"], "secao": j["secao"], "linha": j["linha"], "nota": nota})
    return sorted(saida, key=lambda j: (j["data"] or "9999", j["linha"]))


def jogos(temporada: str) -> list[dict]:
    """Jogos com placar da temporada: {fase, grupo, data, mandante, visitante, gm, gv, secao, linha, nota}."""
    if temporada in NOVAS:
        return _jogos_novos(temporada)
    saida = []
    with open(PASTA / "jogos_pt.csv", encoding="utf-8") as f:
        for i, r in enumerate(csv.DictReader(f, delimiter=";"), 2):
            if r["ano"] != temporada:
                continue
            gm, gv = r["gols_mandante"].strip(), r["gols_visitante"].strip()
            if m := re.match(r"(\d+)\s*[—–-]\s*(\d+)$", gm):   # "2 — 1" numa coluna só
                gm, gv = m.groups()
            if not (gm.isdigit() and gv.isdigit()):
                continue
            chave = (temporada, r["secao"])
            if chave in FASE and FASE[chave] is None:
                continue
            fase, grupo = FASE.get(chave) or PADRAO.get(r["secao"]) or (r["secao"], "")
            saida.append({"fase": fase, "grupo": grupo, "data": _data(r["data"], temporada), "mandante": r["mandante"].strip(),
                          "visitante": r["visitante"].strip(), "gm": int(gm), "gv": int(gv), "secao": r["secao"], "linha": i,
                          "nota": r.get("nota") or ""})
    return saida


def sem_placar(temporada: str) -> int:
    """Quantos jogos da temporada a página traz só com o resultado (sem placar)."""
    with open(PASTA / "jogos_pt.csv", encoding="utf-8") as f:
        return sum(1 for r in csv.DictReader(f, delimiter=";") if r["ano"] == temporada
                   and not re.match(r"\d", r["gols_mandante"].strip()))



def _pagina(temporada: str) -> str:
    """Código da página da edição; vazio quando a Wikipédia não tem a página (1972)."""
    f = PASTA / f"pt_{temporada}.wiki"
    return f.read_text(encoding="utf-8") if f.exists() else ""

def _limpa(t: str) -> str:
    t = re.sub(r"\[\[(?:File|Ficheiro|Imagem|Image):[^\]]*\]\]", " ", t)
    t = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", t)
    t = re.sub(r"\[\[([^\]]*)\]\]", r"\1", t)
    return re.sub(r"<[^>]+>", "", t)


def tabelas_1965() -> list[tuple[str, list[dict]]]:
    """1965 (a RSSSF não tem a página): os dois grupos da 1ª fase com os pontos. Cada clube vem em três linhas da tabela:
    "!...|<font>1</font>", "|bgcolor=...| [[...|Bragantino]] (Bragança Paulista)" e "|bgcolor=... align="center"|26"."""
    saida: list[tuple[str, list[dict]]] = []
    pos = None
    linha: dict | None = None
    for l in (PASTA / "pt_1965.wiki").read_text(encoding="utf-8").splitlines():
        if m := re.search(r'colspan="\d+".*?>(Série [^<|]+)', l):
            saida.append((m.group(1).strip(), []))
            continue
        if not saida:
            continue
        if m := re.match(r"^!.*>(\d+)</font>\s*$", l):
            pos = int(m.group(1))
        elif m := re.match(r'^\|bgcolor=[^|]*align="center"\|\s*(\d+)', l):
            if linha:
                linha["pts"] = int(m.group(1))
                saida[-1][1].append(linha)
                linha = None
        elif m := re.match(r'^\|bgcolor=[^|]*\|\s*(.+?)\s*$', l):
            txt = _limpa(m.group(1)).strip()
            mc = re.match(r"^(.*?)\s*\(([^()]+)\)$", txt)
            linha = {"pos": pos, "nome": mc.group(1) if mc else txt, "cidade": mc.group(2) if mc else None, "pts": None, "nota": ""}
    return [(g, ls) for g, ls in saida if ls]


_COLUNAS = {"Pts": "pts", "J": "j", "V": "v", "E": "e", "D": "d", "GP": "gp", "GC": "gc", "GS": "gc"}


def tabelas_wiki(temporada: str) -> list[dict]:
    """Todas as tabelas de pontos da página (1967-1984, o mesmo desenho de 1965), com a seção onde estão:
    [{"secao": "Primeiro turno / Primeira fase / Grupo Norte", "titulo": "Série Amarela", "linhas": [{pos, nome, cidade, pts,
    j, v, e, d, gp, gc, nota}]}]. As colunas vêm do cabeçalho ("Time", "Pts", "J", "V"...; "GS" é gols sofridos); a
    cidade, do parêntese depois do nome."""
    saida: list[dict] = []
    secoes: list[str] = []
    cols: list[str] = []
    linha: dict | None = None
    valores: list[str] = []
    def fecha():
        nonlocal linha, valores
        if linha is not None and saida:
            for k, v in zip(cols, valores):
                if k in _COLUNAS and re.fullmatch(r"-?\d+", v):
                    linha[_COLUNAS[k]] = int(v)
            saida[-1]["linhas"].append(linha)
        linha, valores = None, []
    for l in _pagina(temporada).splitlines():
        if m := re.match(r"^(=+)\s*(.*?)\s*=+\s*$", l):
            fecha()
            nivel = len(m.group(1)) - 2
            secoes = secoes[:nivel] + [re.sub(r"<ref.*$", "", m.group(2)).strip()]
            continue
        if m := re.search(r'colspan="\d+"[^|\n]*\|\s*<font[^>]*>([^<\n|]+)', l):
            if m.group(1).strip() != "Time":
                fecha()
                saida.append({"secao": " / ".join(secoes), "titulo": m.group(1).strip(), "linhas": []})
                cols = []
            continue
        if m := re.search(r'<font color="B8860B">\s*([^<\s]+)', l):
            cols.append(m.group(1)) if m.group(1) != "Time" else None
            continue
        if not saida:
            continue
        if l.startswith("|-") or l.startswith("|}"):
            fecha()
        elif m := re.match(r"^!.*>(\d+)</font>\s*$", l):
            fecha()
            linha = {"pos": int(m.group(1)), "nome": None, "cidade": None, "pts": None, "nota": ""}
        elif linha is not None and (m := re.match(r'^\|bgcolor=[^|]*\|\s*(.*?)\s*$', l)):
            if linha["nome"] is None:
                txt = re.sub(r"''", "", _limpa(m.group(1))).strip()
                mc = re.match(r"^(.*?)\s*\(([^()]+)\)$", txt)
                linha["nome"], linha["cidade"] = (mc.group(1), mc.group(2)) if mc else (txt, None)
            else:
                valores.append(_limpa(m.group(1)).strip())
    fecha()
    return [t for t in saida if t["linhas"]] + _tabelas_tooltip(temporada)


_TOOLTIP = {"PG": "pts", "Pts": "pts", "J": "j", "V": "v", "E": "e", "D": "d", "GP": "gp", "GC": "gc", "GS": "gc"}


def _tabelas_tooltip(temporada: str) -> list[dict]:
    """O outro desenho de tabela (1968, 1971, 1982): título "'''Grupo A'''" (com a linha "; Classificação final da série A"
    antes, quando há), cabeçalho "! {{Tooltip|PG|Pontos ganhos}}" e cada clube em linhas "|1", "| [[...|Nome]] (Cidade)" e
    "| align="center"|21" (célula vazia: o dado não existe)."""
    saida: list[dict] = []
    secoes: list[str] = []
    rotulo = ""
    cols: list[str] = []
    linha: dict | None = None
    valores: list[str] = []
    def fecha():
        nonlocal linha, valores
        if linha is not None and saida and linha["nome"]:
            for k, v in zip(cols, valores):
                if k in _TOOLTIP and re.fullmatch(r"-?\d+", v):
                    linha[_TOOLTIP[k]] = int(v)
            saida[-1]["linhas"].append(linha)
        linha, valores = None, []
    for l in _pagina(temporada).splitlines():
        if m := re.match(r"^(=+)\s*(.*?)\s*=+\s*$", l):
            fecha()
            nivel = len(m.group(1)) - 2
            secoes = secoes[:nivel] + [re.sub(r"<ref.*$", "", m.group(2)).strip()]
            rotulo = ""
            continue
        if m := re.match(r"^;\s*(.+?)\s*$", l):
            rotulo = _limpa(m.group(1)).strip()
            continue
        if m := re.match(r"^\|\s*colspan=\"\d+\"\s*\|\s*'''(.+?)'''", l):
            fecha()
            saida.append({"secao": " / ".join(secoes), "titulo": " / ".join(x for x in (rotulo, m.group(1).strip()) if x),
                          "linhas": []})
            cols = []
            continue
        if not saida:
            continue
        if m := re.match(r"^!\s*\{\{Tooltip\|([^|}]+)", l):
            cols.append(m.group(1).strip())
        elif l.startswith("|-") or l.startswith("|}"):
            fecha()
        elif m := re.match(r"^\|\s*(\d{1,2})?\s*$", l):   # posição vazia: empatado com o de cima
            fecha()
            pos_ant = int(m.group(1)) if m.group(1) else (saida[-1]["linhas"][-1]["pos"] if saida[-1]["linhas"] else 1)
            linha = {"pos": pos_ant, "nome": None, "cidade": None, "pts": None, "nota": ""}
        elif linha is not None and linha["nome"] is None and (m := re.match(r"^\|\s*(.+?)\s*$", l)):
            txt = re.sub(r"''|'''", "", _limpa(m.group(1))).strip()
            mc = re.match(r"^(.*?)\s*\(([^()]+)\)$", txt)
            linha["nome"], linha["cidade"] = (mc.group(1), mc.group(2)) if mc else (txt, None)
        elif linha is not None and (m := re.match(r'^\|\s*align="center"\|\s*(.*?)\s*$', l)):
            valores.append(_limpa(m.group(1)).strip())
    fecha()
    return [t for t in saida if t["linhas"]]


def jogos_em_linha(temporada: str) -> list[dict]:
    """Jogos escritos em linha de texto (1982): "13 de novembro de 1982: [[...|Mogi Mirim]] 2 – 2 [[...|Primavera]] (nota)",
    às vezes sem a data. Mesmo formato de jogos_footballbox."""
    saida = []
    secoes: list[str] = []
    for i, l in enumerate(_pagina(temporada).splitlines(), 1):
        if m := re.match(r"^(=+)\s*(.*?)\s*=+\s*$", l):
            nivel = len(m.group(1)) - 2
            secoes = secoes[:nivel] + [re.sub(r"<ref.*$", "", m.group(2)).strip()]
            continue
        m = re.match(r"^(?:(.+?):\s*)?\[\[([^\]]+)\]\]\s*(\d+)\s*[–—-]\s*(\d+)\s*\[\[([^\]]+)\]\]\s*(.*?)\s*(?:<br\s*/?>)?\s*$", l)
        if not m:
            continue
        nome = lambda x: x.split("|")[-1].strip()
        saida.append({"secao": " / ".join(secoes), "data": _data(_limpa(m.group(1) or ""), temporada), "mandante": nome(m.group(2)),
                      "visitante": nome(m.group(5)), "gm": int(m.group(3)), "gv": int(m.group(4)), "pen": None, "linha": i,
                      "nota": _limpa(m.group(6)).strip(" ()")})
    return saida


def podio(temporada: str) -> dict:
    """Campeão, vice, 3º e 4º colocados da predefinição de campeões da A2 na Wikipédia (pt_predefinicao_campeoes.wiki):
    {"campeao": nome, "vice": nome, "terceiro": [nomes], "quarto": [nomes]}. Cada linha da predefinição: o ano, o campeão,
    o placar da final (ou uma nota), o vice, o 3º (às vezes dois, empatados), o 4º e o número de clubes."""
    texto = (PASTA / "pt_predefinicao_campeoes.wiki").read_text(encoding="utf-8")
    for bloco in re.split(r"\n\|-[^\n]*", texto):
        cel = [c for c in bloco.split("\n|")]
        if len(cel) < 6 or not re.search(rf"'''{temporada}'''", cel[0] + (cel[1] if len(cel) > 1 else "")):
            continue
        cel = cel[1:] if re.search(rf"'''{temporada}'''", cel[1]) else cel
        def nomes(c):   # o nome é o texto do link ou, sem link, o texto depois da bandeira ("<br />Aliança Clube")
            ls = [x.split("|")[-1].strip() for x in re.findall(r"\[\[(?!Imagem|Ficheiro|File)([^\]]+)\]\]", c)]
            soltos = [_limpa(x).strip(" '") for x in re.split(r"<br\s*/?>", c)[1:] if "[[" not in x and _limpa(x).strip(" '")]
            return ls + soltos
        return {"campeao": (nomes(cel[1]) or [""])[0], "vice": (nomes(cel[3]) or [""])[0], "terceiro": nomes(cel[4]),
                "quarto": nomes(cel[5]) if len(cel) > 5 else []}
    return {}


def jogos_footballbox(temporada: str) -> list[dict]:
    """Jogos das caixas {{footballbox}} da página, com a seção onde estão: {secao, data, mandante, visitante, gm, gv, pen,
    linha, nota}. Placar "1 – 2"; pênaltis em "(4 – 3 pên.)" ou no campo "pênaltis"."""
    texto = _pagina(temporada)
    saida = []
    secoes: list[str] = []
    pos = 0
    for m in re.finditer(r"(?m)^(=+)\s*(.*?)\s*=+\s*$|\{\{\s*[Ff]ootballbox", texto):
        if m.group(1):
            nivel = len(m.group(1)) - 2
            secoes = secoes[:nivel] + [re.sub(r"<ref.*$", "", m.group(2)).strip()]
            continue
        # o bloco vai até o "}}" que fecha a caixa (as referências dentro têm chaves próprias)
        i, prof = m.start(), 0
        for j in range(m.start(), len(texto) - 1):
            if texto[j:j + 2] == "{{":
                prof += 1
            elif texto[j:j + 2] == "}}":
                prof -= 1
                if prof == 0:
                    break
        bloco = re.sub(r"<ref.*?(?:/>|</ref>)", "", texto[i:j + 2], flags=re.S)
        campo = lambda n: (re.search(rf"\|\s*{n}\s*=\s*(.*)", bloco) or [None, ""])[1].strip()
        placar = _limpa(campo("placar"))
        mp = re.match(r"^\s*(\d+)\s*[–—-]\s*(\d+)", placar)
        if not mp:
            continue
        pen = re.search(r"\((\d+)\s*[–—-]\s*(\d+)", placar + " " + _limpa(campo("pênaltis") or campo("penaltis")))
        time = lambda n: re.sub(r"\s+", " ", _limpa(re.sub(r"\[\[(?:Imagem|Ficheiro|File|Image):[^\]]*\]\]", "", campo(n)))).strip()
        saida.append({"secao": " / ".join(secoes), "data": _data(_limpa(campo("data")), temporada), "mandante": time("time1"),
                      "visitante": time("time2"), "gm": int(mp.group(1)), "gv": int(mp.group(2)),
                      "pen": (int(pen.group(1)), int(pen.group(2))) if pen else None,
                      "linha": texto.count("\n", 0, i) + 1, "nota": ""})
        pos = j
    return saida


def participantes(temporada: str) -> list[tuple[str, str]]:
    """Lista de participantes da página ("* [[Associação Esportiva Araçatuba|Araçatuba]] (Araçatuba)")."""
    saida = []
    for l in _pagina(temporada).splitlines():
        if (m := re.match(r"^\*\s*(.+?)\s*\(([^()]+)\)\s*$", _limpa(l))) and not re.match(r"\d", m.group(1)):
            saida.append((m.group(1).strip(), m.group(2).strip()))
    return saida


def classificacao_publicada(temporada: str) -> list[dict]:
    """Classificação final publicada na página ("* 1.º) Olímpia – 13 pontos (acesso)", 1990: a 4ª fase)."""
    saida = []
    for l in _pagina(temporada).splitlines():
        if m := re.match(r"^\*\s*(\d+)\.?º\)\s*(.+?)\s*[–-]\s*(\d+)\s*pontos?\s*(?:\(([^()]*)\))?", _limpa(l)):
            saida.append({"pos": int(m.group(1)), "nome": m.group(2).strip(), "cidade": None, "pts": int(m.group(3)),
                          "nota": (m.group(4) or "").strip()})
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for a in sys.argv[1:] or sorted({r["ano"] for r in csv.DictReader(open(PASTA / "jogos_pt.csv", encoding="utf-8"), delimiter=";")}):
        js = jogos(a)
        print(f"== {a}: {len(js)} jogos com placar, {sem_placar(a)} sem placar")
        for j in js:
            print(f"   {j['fase']:28} {j['grupo']:15} {j['data']} {j['mandante']} {j['gm']}-{j['gv']} {j['visitante']}")
