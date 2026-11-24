"""Leitura das páginas da 2ª divisão paulista da RSSSF Brasil (data/coleta/bra-sp-2/rsssfbrasil/sp{ano}l2.htm).

Usa o leitor comum (coleta/comum/rsssf.py) com o placar "2 x 2" e a data na frente do jogo ligados
(PLACAR_X_ESPACADO). Antes da leitura, corrige o texto das páginas que fogem desse desenho (CORRECOES, com o motivo).

Uso: python coleta/bra-sp-2/rsssf_sp2.py [temporada ...]     (sem temporada: todas; com uma, lista as divergências)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
import rsssf  # noqa: E402
from edicoes import PASTA_DADOS, TEMPORADAS, ano_de  # noqa: E402

rsssf.PASTA = PASTA_DADOS / "rsssfbrasil"
rsssf.MODELO = "sp{ano}l2.htm"
rsssf.PLACAR_X_ESPACADO = True


_CABECA = re.compile(r"\b(?:Round|Rodada)\s*\d+", re.I)


def _cortar(l: str, col: int) -> tuple[str, str]:
    """Separa a linha na coluna; a palavra que atravessa a coluna fica do lado esquerdo."""
    p = col
    while 0 < p < len(l) and l[p - 1] != " " and l[p] != " ":
        p += 1
    return l[:p].rstrip(), l[p:].strip()


def _duas_colunas(t: str) -> str:
    """1998-1999: as rodadas vêm em duas colunas ("Round 1 [Feb 1]      Round 2 [Feb 4]" e os jogos das duas lado a
    lado). Cada bloco (do cabeçalho duplo até a linha em branco) vira a coluna da esquerda e depois a da direita."""
    ls, saida, i = t.split("\n"), [], 0
    while i < len(ls):
        cab = list(_CABECA.finditer(ls[i]))
        if len(cab) < 2:
            saida.append(ls[i]); i += 1
            continue
        col, bloco = cab[1].start(), []
        while i < len(ls) and ls[i].strip():
            bloco.append(_cortar(ls[i], col))
            i += 1
        saida += [e for e, _ in bloco] + [""] + [d for _, d in bloco if d] + [""]
    return "\n".join(saida)


def _celula_1997(c: str, ano: int) -> tuple[str, str | None]:
    """Uma célula do quadro de 1997 em texto que o leitor entende; o segundo valor é a data de um jogo adiado
    ("Paulista (13/3)")."""
    c = c.strip()
    if (m := re.match(r"RODADA\s*(\d+)", c)):
        return f"Round {int(m[1])}", None
    if (m := re.match(r"(\d{1,2})/(\d{1,2})/(\d{2})\b", c)):
        return f"{int(m[1]):02d}/{int(m[2]):02d}/19{m[3]}", None
    adiado = None
    if (m := re.search(r"\((\d{1,2})/(\d{1,2})\)\s*$", c)):
        adiado, c = f"{int(m[1]):02d}/{int(m[2]):02d}/{ano}", c[:m.start()]
    c = re.sub(r"\((?:TV|\*+)\)?|\(TV\)|\(\*+\)", " ", c)
    c = re.sub(r"^(.*?\S)\s+(\d{1,2})x(\d{1,2})\s+(\S.*?)\s*$", r"\1  \2-\3  \4", c.strip())
    return c, adiado


def _quadros_1997(t: str) -> str:
    """1997: jogos em quadros de duas colunas ("| Saocarlense     3x1  Corinthians-PP| Noroeste ...") e as tabelas dos
    grupos em quadro ("| 1  * SANTO ANDRE   44   22   11   11    -   43   23   20  |": P, J, V, E, D, GP, GC, SG, com
    "-" no lugar do zero). Os quadros viram texto corrido: coluna da esquerda, depois a da direita; jogo adiado
    ("(13/3)") vai para o fim da coluna com a data dele. As tabelas viram " 1.Santo Andre  22 11 11 0 43-23 44"."""
    saida: list[str] = []
    cols: list[list[str]] = [[], []]
    adiados: list[list[str]] = [[], []]
    def despejar():
        for k in (0, 1):
            saida.extend(cols[k] + adiados[k] + [""])
            cols[k].clear(); adiados[k].clear()
    for l in t.split("\n"):
        s = l.strip()
        if "Second Phase" in s and s.startswith("|"):   # "| XV Piracicaba 2x1 Ponte Preta(TV| ----- Second Phase -----":
            cols[0].append(_celula_1997(s[:s.index("|", 1)].strip("|"), 1997)[0])   # o returno segue na mesma fase
            despejar()
            continue
        if re.match(r"^\|?[-+|\s]+$", s) and s:
            if any(re.search(r"\d-\d", x) for c in cols for x in c):
                despejar()
            continue
        if not s.startswith("|"):
            saida.append(l)
            continue
        mt = re.match(r"^\|\s*(\d{1,2})\s+\**\s*([A-Z][A-Z .\-]+?)\s{2,}(-?\d+|-)\s+(\d+|-)\s+(\d+|-)\s+(\d+|-)\s+(\d+|-)\s+(\d+|-)\s+(\d+|-)", s)
        if mt:   # linha da tabela do grupo
            n = [0 if x == "-" else int(x) for x in mt.groups()[2:]]
            saida.append(f" {int(mt[1])}.{mt[2].title():<18} {n[1]:>2} {n[2]:>2} {n[3]:>2} {n[4]:>2} {n[5]:>2}-{n[6]:<2} {n[0]:>2}")
            continue
        if (mg := re.search(r">+\s*GRUPO\s*(\d+)", s)):
            saida += ["", f"Group {mg[1]}"]
            continue
        partes = s.split("|")[1:-1] if s.endswith("|") else s.split("|")[1:]
        for k, c in enumerate(partes[:2]):
            txt, adiado = _celula_1997(c, 1997)
            if not txt:
                continue
            if adiado:
                adiados[k] += [adiado, txt]
            else:
                cols[k].append(txt)
    despejar()
    return "\n".join(saida)


_PLACAR = re.compile(r"(?<!\S)\d{1,2}-\d{1,2}(?!\S)")


def _pedaco(s: str) -> bool:
    """Linha que é só um pedaço de nome de clube ("Bento", "Clube", "Osasco")."""
    s = s.strip()
    return (bool(s) and len(s) <= 22 and not s.startswith(("[", "(", "*")) and not re.search(r"\d", s)
            and not re.match(r"(round|group|grupo|first|second|third|fourth|final|semi|quarter|table|standing|classif|"
                             r"participants|source|top\b|pos\b|stage|phase)", s, re.I))


def _nomes_quebrados(t: str) -> str:
    """2014 e 2022: o nome do clube quebra em duas linhas ("Velo" / "Clube   1-0  São" / "Bento"): as linhas voltam a
    ser uma só (a mesma correção do Paulista de 2014, coleta/bra-sp-1/rsssf_sp1.py)."""
    ls = t.split("\n")
    i, colada = 0, -1
    while i < len(ls) - 1:
        cur, prox = ls[i], ls[i + 1]
        m = list(_PLACAR.finditer(cur))
        if m and not cur.lstrip().startswith("[") and _pedaco(prox) and (colada != i or not cur[m[-1].end():].strip()):
            ls[i] = cur.rstrip() + ("  " if not cur[m[-1].end():].strip() else " ") + prox.strip()
            del ls[i + 1]
            colada = i
            continue
        if _pedaco(cur) and _PLACAR.search(prox) and not prox.lstrip().startswith("["):
            ls[i] = cur.strip() + ("  " if _PLACAR.match(prox.strip()) else " ") + prox.strip()
            del ls[i + 1]
            continue
        i += 1
    return "\n".join(ls)


_MESES = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def _data_na_frente(t: str) -> str:
    """"09/May União 2-0 Aparecida" e "13/03 Palmeiras 1-3 Taubaté" (data sem o ano na frente do jogo): a data vai para o
    formato "[May 09]" que o leitor comum entende."""
    t = re.sub(r"^([ \t]*)(\d{1,2})/([A-Za-z]{3})\b\.?[ \t]+", lambda m: f"{m[1]}[{m[3].capitalize()} {m[2]}] ", t, flags=re.M)
    return re.sub(r"^([ \t]*)(\d{1,2})/(\d{1,2})(?![/\d])[ \t]+(?=\S)",
                  lambda m: f"{m[1]}[{_MESES[int(m[3]) - 1]} {m[2]}] " if 1 <= int(m[3]) <= 12 else m[0], t, flags=re.M)


def _turnos_sem_titulo(t: str) -> str:
    """1987-1988: "1º Turno" / "2º Turno" dentro do grupo não são fases (o título apagaria o grupo, e a tabela do grupo
    soma os dois turnos). O 2º turno começa com jogos sem data: a data do 1º turno não passa para eles."""
    t = re.sub(r"(?mi)^[ \t]*(?:1º|primeiro)[ \t]+turno[ \t]*$", "", t)
    return re.sub(r"(?mi)^[ \t]*(?:2º|segundo)[ \t]+turno[ \t]*$", "[unknown]", t)


rsssf.CORRECOES.update({
    "sp1979l2.htm": [(r"\[Jun (11|12)\]", r"[Jul \1]", "datas \"Jun 11\" e \"Jun 12\" no meio dos jogos de julho (8 e 14 de julho)"),
                     (r"Gin\. Pinhalense|Ginásio Pinalense", "Ginásio Pinhalense", "grafias do Ginásio Pinhalense")],
    "sp1986l2.htm": [(r"\(Bebedouro\s+Associação", "(Bebedouro)\nAssociação", "duas linhas da lista de participantes coladas")],
    "sp1985l2.htm": [(r"\(Bebedouro\s+Associação", "(Bebedouro)\nAssociação", "duas linhas da lista de participantes coladas"),
                     (r"(Sãocarl\. used an)\s+(Round 18)\s+(ineligible player\])", r"\1 \3\n\2",
                      "o título da rodada 18, na coluna da direita, entra no meio da nota do jogo Barretos x Sãocarlense"),
                     (r"\[victory awarded to S\.Bernardo,\s*\n(\[Sep 1\])\s+originally 0-0, Nacional used an\s*\n(Bragantino\s+1-0\s+Aparecida)\s+ineligible player\]",
                      r"[victory awarded to S.Bernardo, originally 0-0, Nacional used an ineligible player]\n\1\n\2",
                      "a nota do jogo Nacional x São Bernardo, em coluna, se espalha por três linhas e cola no nome do Aparecida")],
    "sp1998l2.htm": [(r"Mirassol \[\*\]", "Mirassol", "marca de nota no nome do Mirassol"),
                     (r"Corintians-PP", "Corinthians-PP", "nome do Corinthians de Presidente Prudente sem o \"h\"")],
    "sp2000l2.htm": [(r"(?s)(NB: best team will take place.*?)\nSemifinals\n(.*?)\nFinal\n", r"\1\nFirst Phase - Semifinals\n\2\nFirst Phase - Final\n",
                      "a 1ª fase tem semifinal e final próprias (o vencedor sobe para a 1ª divisão na 2ª fase)")],
    "sp2021l2.htm": [(r"Água Santa\]", "Água Santa", "colchete solto depois do nome do Água Santa"),
                     (r"\[Penalty shootout: (\d+)-(\d+)\]", r"[pen \1-\2]", "pênaltis da final (\"Penalty shootout\")")],
    "sp1987l2.htm": [(_data_na_frente, None, "data sem o ano na frente do jogo (\"09/May\")"),
                     (_turnos_sem_titulo, None, "turnos dentro do grupo")],
    "sp1988l2.htm": [(_data_na_frente, None, "data sem o ano na frente do jogo (\"13/03\")"),
                     (_turnos_sem_titulo, None, "turnos dentro da fase")],
    "sp1995l2.htm": [(_data_na_frente, None, "data sem o ano na frente do jogo (\"29/Jan\")"),
                     (r"-V de Jaú", "XV de Jaú", "o \"X\" do XV de Jaú virou \"-\" na página")],
    "sp1997l2.htm": [(r"(?m)^\s*SECOND STAGE\s*$\n\s*\n?\s*First Phase\s*$", "",
                    "a 1ª fase vai até o returno dentro dos grupos (\"SECOND STAGE\"): as tabelas dos grupos somam as 22 rodadas"),
                   (r"Ferroviaria     1x1  Noroeste \(\*\*\)", "Ferroviaria  awd  Noroeste [awarded 1-0]",
                    "Ferroviária 1x1 Noroeste (23/02): jogo inacabado; a FPF deu a vitória à Ferroviária (a tabela conta 1-0)"),
                   (_quadros_1997, None, "jogos e tabelas em quadros de duas colunas"),
                   (r"(?m)^\s*Second Phase\s*$", "", "o returno dentro dos grupos (\"Second Phase\") segue na 1ª fase"),
                   (r"Paraguacuese", "Paraguacuense", "nome do Paraguaçuense com uma letra a menos (1ª rodada)"),
                   (r"(?m)^\s*Quadrangular Final\s*$", "Final Phase", "o quadrangular final é a fase final")],
    "sp1998l2.htm": [(_duas_colunas, None, "rodadas em duas colunas"),
                     (r"(?m)^Final Table:", "Table:", "\"Final Table:\" é a tabela do quadrangular, não outra fase"),
                     (r"EC XV de Novembro", "XV Piracicaba", "o XV de Piracicaba aparece na tabela com o nome sem a cidade")],
    "sp1999l2.htm": [(_duas_colunas, None, "rodadas em duas colunas")],
})


def _travessao(t: str) -> str:
    """Placar com travessão ("Paulista   0–1   Portuguesa", 1979): vira hífen."""
    return re.sub(r"(?<=\d)[ \t]*[–—][ \t]*(?=\d)", "-", t)


# letras que a própria página da RSSSF já traz trocadas por "�" (2000-2003): a grafia certa
LETRAS = {"S�o": "São", "Jos�": "José", "S�ocarlense": "Sãocarlense", "Paragua�uense": "Paraguaçuense", "Jundia�": "Jundiaí",
          "Andr�": "André", "Am�rica": "América", "Ara�atuba": "Araçatuba", "Atl�tico": "Atlético", "Mar�lia": "Marília",
          "S�rie": "Série", "It�polis": "Itápolis", "Bragan�a": "Bragança", "Ribeir�o": "Ribeirão", "Paragua�u": "Paraguaçu",
          "Birig�i": "Birigüi", "Mat�o": "Matão"}


def _letras(t: str) -> str:
    for errado, certo in LETRAS.items():
        t = t.replace(errado, certo)
    return t


for _a in (2014, 2022, 2023, 2024):
    rsssf.CORRECOES.setdefault(f"sp{_a}l2.htm", []).append((_nomes_quebrados, None, "nomes de clube quebrados em duas linhas"))
rsssf.CORRECOES["sp2014l2.htm"].insert(-1, (r"(?m)^(Guarani\s+2-3\s+Rio)[ \t]*\n[ \t]*Branco\b", r"\1 Branco",
                                            "nome do Rio Branco quebrado, com a nota na mesma linha"))
rsssf.CORRECOES["sp2022l2.htm"].insert(-1, (r"(?m)^(Oeste\s+1-1\s+São)\s*\n(Bento)\s+\[Pênaltis: (\d+)-(\d+)\]", r"\1 \2 [pen \3-\4]",
                                            "nome do São Bento quebrado, com os pênaltis na mesma linha"))

for _a in range(1947, 2026):   # antes das outras correções
    rsssf.CORRECOES.setdefault(f"sp{_a}l2.htm", []).insert(0, (_travessao, None, "placar com travessão"))
    rsssf.CORRECOES[f"sp{_a}l2.htm"].insert(0, (_letras, None, "letras trocadas por \"�\" na página"))



def _tabela_2001(t: str) -> str:
    """2001: a tabela traz os empates abertos ("18  6/ 1/ 0  6": empates e as duas colunas da regra dos pênaltis); fica o
    total de empates (jogos - vitórias - derrotas), no desenho que o leitor comum entende (achado A2-011)."""
    def troca(m):
        j, v, d = int(m[2]), int(m[3]), int(m[4])
        return f"{m[1]}{j:3d} {v:2d} {j - v - d:2d} {d:2d}{m[5]}"
    return re.sub(r"(?m)^(\s*\d+\.\S.*?)\s+(\d+)\s+(\d+)\s+\d+/\s*\d+/\s*\d+\s+(\d+)(\s+\d+-\d+.*)$", troca, t)


rsssf.CORRECOES.setdefault("sp2001l2.htm", []).append((_tabela_2001, None, "tabela com os empates abertos pela regra dos pênaltis"))
rsssf.CORRECOES["sp2001l2.htm"].append(
    (r"(?m)^Nacional(\s+)1-0(\s+)Ituano", r"Nacional\g<1>0-1\g<2>Ituano",
     "Nacional 0-1 Ituano (03/03/2001), como o ogol: só esse placar fecha com a tabela publicada (achado A2-017)"))
rsssf.CORRECOES.setdefault("sp2006l2.htm", []).append(
    (r"(?m)^Bandeirante\s+abd\s+União São João\s+\[abandoned at halftime[^\n]*\n\[Apr 3\][^\n]*\n(Bandeirante\s+0-1\s+União São João)"
     r"\s+\[remaining 45 minutes\]",
     r"\1  [interrompido no intervalo com 0-1 por falta de luz; os 45 minutos restantes foram jogados em 03/04]",
     "jogo interrompido e completado no dia seguinte: um jogo só, 0-1 (achado A2-013)"))
rsssf.CORRECOES.setdefault("sp2021l2.htm", []).append(
    (r"(?m)^(Round 7\n)\[Apr 26\]", r"\1[Apr 24]", "a rodada 7 foi em 24/04 (FPF); a página repete a data da rodada 8 (achado A2-016)"))

# a A2 não tem torneio à parte na página (no Paulista: Troféu do Interior); o importador comum pergunta
ANOS_A_PARTE: set[int] = set()


def trofeu(temporada: str) -> list:
    return []


def tem_pagina(temporada: str) -> bool:
    return (rsssf.PASTA / rsssf.MODELO.format(ano=ano_de(temporada))).exists()


def _grupo_limpo(g: str) -> str:
    """"Group D   M  W  D  L  GF-GA  Pts": o cabeçalho das colunas sai do nome do grupo."""
    return re.split(r"\s{2,}|Pos(?=Team)", g)[0].strip(" :")


def _casar_tabela(nomes_tab: list[str], nomes_jogos: set[str]) -> dict[str, str]:
    """Nome da tabela -> nome nos jogos: igual; senão o de prefixo comum mais longo, quando um começa com o outro; o
    resto pelo casamento comum (como no Paulista, coleta/bra-sp-1/rsssf_sp1.py)."""
    saida = {nt: nt for nt in nomes_tab if nt in nomes_jogos}
    for nt in nomes_tab:
        if nt in saida:
            continue
        k = rsssf.chave(nt)
        cands = [(len(rsssf.chave(nj)), nj) for nj in nomes_jogos - set(saida.values())
                 if k.startswith(rsssf.chave(nj)) or rsssf.chave(nj).startswith(k)]
        if cands:
            cands.sort(reverse=True)
            if len(cands) == 1 or cands[0][0] != cands[1][0]:
                saida[nt] = cands[0][1]
    resto = [nt for nt in nomes_tab if nt not in saida]
    if resto:
        saida.update(rsssf.casar(resto, nomes_jogos - set(saida.values())))
    return saida


def _grupos_pelas_tabelas(jogos: list, tabelas: list) -> None:
    """As tabelas dos grupos vêm antes ou depois dos jogos, e os jogos vêm por rodada, com os grupos misturados (e às vezes
    os clubes também enfrentam os do outro grupo). O grupo de cada jogo sai das tabelas da fase: os dois clubes no mesmo
    grupo -> esse grupo; em grupos diferentes -> sem grupo. Como no Paulista (rsssf_sp1._grupos_pelas_tabelas)."""
    for fase in {j.fase for j in jogos}:
        tabs = [tb for tb in tabelas if tb.fase == fase and re.match(r"(group|grupo|s[ée]rie)\b", tb.grupo, re.I)]
        if len({tb.grupo for tb in tabs}) < 2:
            continue
        nos_jogos = {x for j in jogos if j.fase == fase for x in (j.mandante, j.visitante)}
        grupo_de = {}
        for tb in sorted(tabs, key=lambda tb: -len(tb.linhas)):
            for nt, nj in _casar_tabela([r["nome"] for r in tb.linhas], nos_jogos).items():
                grupo_de[nj] = tb.grupo
        for j in jogos:
            if j.fase == fase:
                gm, gv = grupo_de.get(j.mandante), grupo_de.get(j.visitante)
                if gm and gv:
                    j.grupo = gm if gm == gv else ""
    # mata-mata: grupo de dois clubes não é grupo
    clubes: dict[tuple, set] = {}
    for j in jogos:
        clubes.setdefault((j.fase, j.grupo), set()).update((j.mandante, j.visitante))
    for x in [*jogos, *tabelas]:
        if x.grupo and len(clubes.get((x.fase, x.grupo), ())) <= 2 and (not hasattr(x, "linhas") or len(x.linhas) <= 2):
            x.grupo = ""


# 1989 e 1991 (páginas incompletas): os jogos vêm só sob "1º Turno" / "2º Turno" (e "Fase Final"), sem o nome da fase nem
# do grupo. 1989 tem só a 1ª fase: a Série A joga contra a B (Grupo 1) e a C contra a D (Grupo 2). 1991 tem só a 2ª fase
# (Séries E e F, turno e returno) e o quadrangular final
FASE_ANO = {"1989": {"1º Turno": "First Phase", "2º Turno": "First Phase"},
            "1991": {"1º Turno": "Second Phase", "2º Turno": "Second Phase", "Fase Final": "Final Phase"}}
GRUPO_ANO = {
    "1989": {**dict.fromkeys(["Capivariano", "Jacareí", "Nacional", "Rio Branco", "São Bernardo", "Taubaté", "União", "Ituano",
                              "Independente", "Lemense", "Palmeiras", "Paulista", "Ponte Preta"], "Grupo 1"),
             **dict.fromkeys(["Bandeirante", "Corinthians", "Marília", "Mirassol", "Tanabi", "Taquaritinga", "VOCEM", "Comercial",
                              "Fernandópolis", "Francana", "Linense", "Olímpia", "Rio Preto", "Votuporanguense"], "Grupo 2")},
    "1991": {**dict.fromkeys(["Araçatuba", "Independente", "Jaboticabal", "Mirassol", "Radium", "Taubaté"], "Série E"),
             **dict.fromkeys(["Barretos", "Francana", "Lemense", "Nacional", "Paulista", "Tanabi"], "Série F")},
}


def _fase_e_grupo_do_ano(temporada: str, jogos) -> None:
    fases, grupos = FASE_ANO.get(temporada), GRUPO_ANO.get(temporada, {})
    if not fases:
        return
    for j in jogos:
        if j.fase in fases:
            j.fase = fases[j.fase]
            if j.fase != "Final Phase":
                gm, gv = grupos.get(j.mandante), grupos.get(j.visitante)
                j.grupo = gm if gm and gm == gv else ""


def ler(temporada: str):
    jogos, tabelas = rsssf.ler(ano_de(temporada))
    for x in [*jogos, *tabelas]:
        x.grupo = _grupo_limpo(x.grupo)
    _fase_e_grupo_do_ano(temporada, jogos)
    _grupos_pelas_tabelas(jogos, tabelas)
    return jogos, tabelas


def conferir(temporada: str):
    jogos, tabelas = ler(temporada)
    return jogos, tabelas, rsssf.conferir(jogos, tabelas)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    alvo = sys.argv[1:] or [t for t in TEMPORADAS if tem_pagina(t)]
    for t in alvo:
        jogos, tabelas, erros = conferir(t)
        print(f"{t}: {len(jogos)} jogos, {len(tabelas)} tabelas ({sum(len(x.linhas) for x in tabelas)} linhas), {len(erros)} divergências")
        if len(alvo) == 1:
            for e in erros[:60]:
                print("   !", e)
