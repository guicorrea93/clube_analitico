"""Leitura das páginas do Campeonato Carioca da RSSSF Brasil (data/coleta/bra-rj-1/rsssfbrasil/rj{ano}.htm).

Usa o leitor comum (coleta/comum/rsssf.py), com o placar "2 x 2" ligado (PLACAR_X_ESPACADO). Antes da leitura, corrige
o texto das páginas que fogem desse desenho (CORRECOES, com o motivo). Nos anos de duas ligas a página traz os dois
torneios; `ler(temporada)` lê só o trecho da liga pedida. 1979 Especial fica em rj1979s.htm.

Uso: python coleta/bra-rj-1/rsssf_rj1.py [temporada ...]     (sem temporada: todas; com uma, lista as divergências)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
import rsssf  # noqa: E402
from edicoes import LIGAS, PASTA_DADOS, TEMPORADAS, ano_de, liga_de, pagina_rsssf  # noqa: E402

rsssf.PASTA = PASTA_DADOS / "rsssfbrasil"
rsssf.MODELO = "rj{ano}.htm"
rsssf.PLACAR_X_ESPACADO = True
rsssf.QUEBRA_BLOCOS = True   # <P>/<PRE>/<H2> sem <br>: o título de cada liga ficava colado no jogo

LIGA_ATUAL = {"liga": ""}   # liga pedida em ler(); a correção _liga usa
SIGLAS_LIGAS = "AFRJ|LMSA|LMDT|AMEA|LCF|FMD"


def _liga(t: str) -> str:
    """Anos de duas ligas: fica só o trecho da liga pedida (do título dela até o título da outra)."""
    liga = LIGA_ATUAL["liga"]
    if not liga:
        return t
    titulos = [(m.start(), m.group(1)) for m in re.finditer(rf"^[ \t]*(?:[^\n]*?\b)?({SIGLAS_LIGAS})\b[^\n]*$", t, re.M)
               if len(m.group(0).strip()) < 80]
    for k, (pos, nome) in enumerate(titulos):
        if nome == liga:
            fim = next((p for p, n in titulos[k + 1:] if n != liga), len(t))
            return t[pos:fim]
    return t


def _data_mes(t: str) -> str:
    """"13/Aug      Bangu 5-0 Canto do Rio": a data com o mês por extenso na frente do jogo vai para o formato "[Aug 13]" que
    o leitor comum entende (igual ao Paulista, coleta/bra-sp-1/rsssf_sp1.py)."""
    # também com o ano ("02/Jan/1955  Madureira 1-8 Fluminense"): "[Jan 02, 1955]"
    return re.sub(r"^([ \t]*)(\d{1,2})/([A-Za-z]{3})(?:/(\d{4}))?\b\.?[ \t]+",
                  lambda m: f"{m[1]}[{m[3].capitalize()} {m[2]}{', ' + m[4] if m[4] else ''}] ", t, flags=re.M)


_MESES_ABREV = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def _linha_de_jogo(t: str) -> str:
    """Jogos com a data na frente e o local no fim (1911-1922, 1934, 1944, 1980): "16/05 – Bangu 0 x 5 América (Rua Ferrer).",
    "[May 03] - Paysandu 5-4 Fluminense (Rua Guanabara).", "01/07 - Vasco 3 x 3 Fluminense". A data "dd/mm" vira "[May 16]",
    o traço depois da data sai, o local do jogo vira nota ("[Rua Ferrer]", antes ele entrava no nome do visitante), o
    traço solto antes do placar ("América - 3 x 1") sai e o W.O. ("WO - 0") fica como o leitor comum entende ("wo-0")."""
    def troca(l: str) -> str:
        # também com o ano em dois dígitos ("02/04/11 - Paysandu 5 x 2 Mangueira - (Laranjeiras).", 1911)
        m = re.match(r"^([ \t]*)(\d{1,2})/(\d{1,2})(?:/\d{2,4})?[ \t]*[–-][ \t]*(?=\S)", l)
        if m and 1 <= int(m[3]) <= 12:
            l = f"{m[1]}[{_MESES_ABREV[int(m[3]) - 1]} {int(m[2]):02d}] " + l[m.end():]
        m = re.match(r"^([ \t]*\[[A-Z][a-z]{2} \d{1,2}(?:, \d{4})?\])[ \t]*[–-][ \t]*", l)
        if m:
            l = m[1] + " " + l[m.end():]
        if re.match(r"^[ \t]*\[[A-Z][a-z]{2} \d", l):
            l = re.sub(r"[ \t][–-][ \t]*(\d+[ \t]*(?:x|-)[ \t]*\d)", r" \1", l)
            l = re.sub(r"(?i)\bWO[ \t]*-[ \t]*(\d)\b", r"wo-\1", l)
            l = re.sub(r"(?i)\b(\d)[ \t]*-[ \t]*WO\b", r"\1-wo", l)
            l = re.sub(r"[ \t]*(?:[–-][ \t]*)?\(([^()]*)\)\.?[ \t]*$", r"  [\1]", l)
        return l
    return "\n".join(troca(l) for l in t.split("\n"))


def _homonimos(t: str) -> str:
    """"Fluminense (Nova Friburgo)" (1979): o leitor comum tira a cidade entre parênteses e o clube virava o Fluminense do
    Rio; fica "Fluminense-NF", como a própria página escreve nas tabelas."""
    return re.sub(r"Fluminense \(Nova Friburgo\)", "Fluminense-NF", t)


rsssf.CORRECOES.update({f"rj{a}.htm": [(_liga, None, "ano de duas ligas: lê só o trecho da liga da temporada")]
                        for a, ls in LIGAS.items() if all(ls)})
for _arq in [f"rj{a}.htm" for a in range(1906, 2027)] + ["rj1979s.htm"]:
    rsssf.CORRECOES.setdefault(_arq, []).append((_data_mes, None, "data com o mês por extenso na frente do jogo"))
    rsssf.CORRECOES.setdefault(_arq, []).append((_homonimos, None, "Fluminense de Nova Friburgo separado do Fluminense do Rio"))
    if int(_arq[2:6]) <= 1990:   # em 1993 e 1995 piora a leitura
        rsssf.CORRECOES.setdefault(_arq, []).append((_linha_de_jogo, None, "data dd/mm na frente e o local do jogo no fim"))
rsssf.CORRECOES.setdefault("rj1921.htm", []).append(
    (r"(?m)^(\[Sep 04, 1921\] Flamengo) 1-1 (América)[ \t]*\n[ \t]*Extra-Time: Flamengo 1-0 América.*$",
     r"\1 2-1 \2  [after extra time; 1-1 after 90 minutes; Flamengo champions]",
     "1921: o desempate Flamengo x América foi 1-1 no tempo normal e 1-0 na prorrogação (a prorrogação vinha numa linha à "
     "parte e virava um jogo de um clube \"Extra-Time: Flamengo\")"))
rsssf.CORRECOES["rjcamp.htm"] = [
    (r"\(que(\s+)corresponde ao interior", r"que\1corresponde ao interior",
     "parêntese aberto na nota em português: o leitor emendava a linha de 1906 nela"),
    (r"Botafogo Football Club \(Rio de Janeiro(?=\s+\[AFRJ\])", "Botafogo Football Club (Rio de Janeiro)",
     "parêntese sem fechar no Botafogo de 1912 (AFRJ): o leitor emendava a linha de 1913 nela"),
]


def _taca_a_parte(t: str) -> str:
    """2009-2012: torneios de consolação entre os turnos, para os clubes fora das semifinais da Taça (Taça Moisés Mathias de
    Andrade, Taça João Ellis Filho, Torneio Washington Rodrigues, Torneio Carlos Alberto Torres, Torneio Edílson Silva,
    Torneio Luiz Penido): não são jogos do campeonato e saem, do título até a linha "X wins ...". O importador tira os
    mesmos jogos do ogol (ANOS_A_PARTE)."""
    titulo = re.compile(r"^[ \t]*(?:Torneio|Taça|TORNEIO|TAÇA) (?!Guanabara|Rio\b|GUANABARA|RIO\b)[^\n]*:[ \t]*$", re.M)
    def fim_de(m) -> int:
        """Fim do torneio: a linha do vencedor ("* América wins ...", "* X are ... champions"), inclusive; ou o começo do
        turno seguinte, do torneio de rebaixamento ou da fase final do campeonato, exclusive."""
        venc = re.compile(r"(?im)^.*\b(?:wins?|champions)\b.*$").search(t, m.end())
        # (a "SEMIFINALS:" em maiúsculas pode ser do próprio torneio: não serve de fim)
        prox = re.compile(r"(?m)^[ \t]*(?:(?:FIRST|SECOND|THIRD) STAGE\b|Relegation|Final standings)").search(t, m.end())
        if venc and (not prox or venc.start() < prox.start()):
            return venc.end()
        return prox.start() if prox else len(t)
    if SO_A_PARTE["sim"]:   # trofeu(): só os trechos tirados
        return "\n".join(t[m.start():fim_de(m)] for m in titulo.finditer(t))
    while (m := titulo.search(t)):
        t = t[:m.start()] + t[fim_de(m):]
    return t


SO_A_PARTE = {"sim": False}
_ESTAGIO = re.compile(r"^[ \t]*(FIRST|SECOND|THIRD) STAGE\b.*$", re.I)
_TITULO_FASE = re.compile(r"^[ \t]*(First Phase|Second Phase|Stage Semifinals?|Stage Finals?|Semifinals?|Finals?|"
                          r"Quarterfinals?)[ \t]*:?[ \t]*$", re.I)


def _num_estagio(l: str) -> str | None:
    """Turno que a linha de título abre: "FIRST STAGE (...)", "Second Round (Taça Rio de Janeiro)" pela ordem; "Taça
    Guanabara" (1º turno) e "Taça Rio" (2º turno) pelo nome da taça. Não é título: linha de grupo ("Group D - Taça Rio"),
    de vencedor ("Vasco win Taça Guanabara") ou longa."""
    s = l.strip()
    if not s or len(s) > 90 or re.match(r"^[*\d\[(]", s) or re.match(r"(?i)(group|grupo)\b", s):
        return None
    if (m := re.match(r"(?i)(first|second|third)[ \t]+(?:stage|round)\b", s)):
        return m.group(1).capitalize()
    if re.search(r"(?i)\b(wins?|won|are|is|qualif\w*|champions?|semi-?finals?|finals?|winners)\b", s):
        return None
    if re.search(r"(?i)\bta[çc]a guanabara\b", s):
        return "First"
    if re.search(r"(?i)\bta[çc]a rio\b", s):
        return "Second"
    return None


def _estagios(t: str) -> str:
    """O campeonato em dois turnos (1977-2024, com formatos que mudam): "FIRST STAGE (XLVI Taça Guanabara ...)", "First Round
    (Taça Guanabara)", "Taça Guanabara" sozinha, "SECOND STAGE - XXXVI Taça Rio"... O título do turno vira "First Stage -
    First Phase" e os títulos das fases dentro dele ganham o turno na frente ("First Stage - Semifinals"), que o importador
    traduz para "1º Turno", "1º Turno - Semifinal"... A fase do campeonato depois dos turnos ("Final Phase", "SEMIFINALS:",
    "FINALS:", "LEAGUE ...", o torneio de rebaixamento e a classificação final) fica sem turno."""
    saida, estagio = [], None
    for l in t.split("\n"):
        if (n := _num_estagio(l)):
            estagio = n
            saida.append(f"{estagio} Stage - First Phase")
            continue
        if estagio and re.match(r"^[ \t]*(?:Relegation|Final standings|Final Phase|SEMIFINALS|FINALS?\b|FINAL\b|LEAGUE\b|"
                                r"Championship (?:Final|Playoff))", l):
            estagio = None
        if estagio and (mt := _TITULO_FASE.match(l)):
            nome = re.sub(r"(?i)^stage\s+", "", mt.group(1)).capitalize()
            l = f"{estagio} Stage - {nome}"
        saida.append(l)
    return "\n".join(saida)


# letras que a própria página da RSSSF já traz trocadas por "�" (2001-2006): a grafia certa
LETRAS = {"Ta�a": "Taça", "S�o": "São", "Crist�v�o": "Cristóvão", "Am�rica": "América", "Mac�": "Macaé",
          "Maca�": "Macaé", "Volta Redonda": "Volta Redonda", "Friburguense": "Friburguense", "Gon�alo": "Gonçalo",
          "Niter�i": "Niterói", "Cabofriense": "Cabofriense", "Bonsucesso": "Bonsucesso", "Tr�s": "Três",
          "Itaperuna": "Itaperuna", "Petr�polis": "Petrópolis", "Serrano": "Serrano", "Ol�ria": "Olaria"}


def _letras(t: str) -> str:
    for errado, certo in LETRAS.items():
        t = t.replace(errado, certo)
    return t


for _a in range(1906, 2027):   # antes das outras correções
    rsssf.CORRECOES.setdefault(f"rj{_a}.htm", []).insert(0, (_letras, None, "letras trocadas por \"�\" na página"))
ANOS_A_PARTE = {2009, 2010, 2011, 2012}
# anos em que os turnos (Taça Guanabara, Taça Rio) organizam a página
TURNOS = set(range(1977, 2025)) - {1998, 2014, 2015, 2016, 2017}   # nesses a correção piora a leitura (2016: _2016)
rsssf.CORRECOES.setdefault("rj2016.htm", []).extend([
    (r"(?m)^[ \t]*FIRST STAGE:[ \t]*$", "First Phase", "2016: a 1ª fase (grupos A e B)"),
    (r"(?m)^[ \t]*Group D - Taça Rio[ \t]*$", "Second Phase\nGroup D",
     "2016: a 2ª fase tem o grupo C (Taça Guanabara, os 8 de cima) e o grupo D (Taça Rio, os 8 de baixo)"),
    (r"(?m)^[ \t]*Taça Guanabara/Group C[ \t]*$", "Group C", "2016: grupo C da 2ª fase"),
    (r"(?m)^[ \t]*Taça Rio semifinals:[ \t]*$", "Taça Rio - Semifinals", "2016: semifinal da Taça Rio (vaga na Série D)"),
    (r"(?m)^[ \t]*Finals:[ \t]*$", "Taça Rio - Finals", "2016: final da Taça Rio"),
])
for _a in range(2007, 2014):
    rsssf.CORRECOES.setdefault(f"rj{_a}.htm", []).append((_taca_a_parte, None, "torneios de consolação entre os turnos ficam de fora"))
for _a in TURNOS:
    rsssf.CORRECOES.setdefault(f"rj{_a}.htm", []).append((_estagios, None, "turnos (Taça Guanabara e Taça Rio) nos títulos das fases"))


def trofeu(temporada: str) -> list:
    """Os jogos dos torneios de consolação da página (ANOS_A_PARTE), para o importador tirar os mesmos do ogol."""
    if ano_de(temporada) not in ANOS_A_PARTE:
        return []
    SO_A_PARTE["sim"] = True
    try:
        return rsssf.ler(ano_de(temporada), pagina_rsssf(temporada))[0]
    finally:
        SO_A_PARTE["sim"] = False


def tem_pagina(temporada: str) -> bool:
    return (rsssf.PASTA / pagina_rsssf(temporada)).exists()


def _grupo_limpo(g: str) -> str:
    """"Group D   M  W  D  L  GF-GA  Pts": o cabeçalho das colunas sai do nome do grupo."""
    return re.split(r"\s{2,}|Pos(?=Team)", g)[0].strip(" :")


def _casar_tabela(nomes_tab: list[str], nomes_jogos: set[str]) -> dict[str, str]:
    """Nome da tabela -> nome nos jogos: igual; senão o de prefixo comum mais longo, quando um começa com o outro
    ("Portuguesa Sant" -> "Portuguesa Sa", e não "Portuguesa"); o resto pelo casamento comum."""
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
    """Desde 2016 a página traz as tabelas dos grupos antes dos jogos, e os jogos vêm por rodada, com os grupos misturados
    (e no formato de 2017 em diante os clubes só enfrentam os de outros grupos). O grupo de cada jogo sai das tabelas da
    fase: os dois clubes no mesmo grupo -> esse grupo; em grupos diferentes -> sem grupo."""
    for fase in {j.fase for j in jogos}:
        tabs = [tb for tb in tabelas if tb.fase == fase and re.match(r"(group|grupo|s[ée]rie)\b", tb.grupo, re.I)]
        if len({tb.grupo for tb in tabs}) < 2:
            continue
        nos_jogos = {x for j in jogos if j.fase == fase for x in (j.mandante, j.visitante)}
        grupo_de = {}
        # a tabela geral da fase (16 clubes) vem com o título do último grupo: as tabelas menores valem por cima dela
        for tb in sorted(tabs, key=lambda tb: -len(tb.linhas)):
            for nt, nj in _casar_tabela([r["nome"] for r in tb.linhas], nos_jogos).items():
                grupo_de[nj] = tb.grupo
        menor = min(len(tb.linhas) for tb in tabs if tb.linhas) if any(tb.linhas for tb in tabs) else 0
        for tb in tabs:
            if menor and len(tb.linhas) >= 2 * menor:   # a tabela geral
                tb.grupo = ""
        for j in jogos:
            if j.fase == fase:
                gm, gv = grupo_de.get(j.mandante), grupo_de.get(j.visitante)
                if gm and gv:   # um nome que não casou com a tabela: fica o grupo da página
                    j.grupo = gm if gm == gv else ""
    # mata-mata: cada confronto vem com uma tabelinha de "grupo" ("Group E" nas quartas); grupo de dois clubes não é grupo
    clubes: dict[tuple, set] = {}
    for j in jogos:
        clubes.setdefault((j.fase, j.grupo), set()).update((j.mandante, j.visitante))
    for x in [*jogos, *tabelas]:
        if x.grupo and len(clubes.get((x.fase, x.grupo), ())) <= 2 and (not hasattr(x, "linhas") or len(x.linhas) <= 2):
            x.grupo = ""


def _caixa_alta(n: str) -> bool:
    return bool(re.search(r"[A-ZÀ-Ý]{4,}", n)) and n == n.upper()


def sem_sumulas(jogos: list) -> list:
    """A página traz, depois dos jogos decisivos, a súmula do jogo com os nomes em caixa alta ("BOTAFOGO 4 x 2 FLUMINENSE",
    "Data - ...", "Local - ...", "Árbitro - ..."). É o mesmo jogo da lista: sai a súmula quando há um jogo em letra normal
    com os mesmos clubes e o mesmo placar (1952 e 1953, com a página inteira em caixa alta, ficam como estão)."""
    chave = lambda s: re.sub(r"[^a-z]", "", rsssf.chave(s).lower())[:6]
    normais = [j for j in jogos if not (_caixa_alta(j.mandante) and _caixa_alta(j.visitante))]
    saida = []
    for j in jogos:
        if _caixa_alta(j.mandante) and _caixa_alta(j.visitante) and any(
                {chave(k.mandante), chave(k.visitante)} == {chave(j.mandante), chave(j.visitante)}
                and (k.gm, k.gv) in ((j.gm, j.gv), (j.gv, j.gm)) for k in normais):
            continue
        saida.append(j)
    return saida


def ler(temporada: str):
    LIGA_ATUAL["liga"] = liga_de(temporada) if liga_de(temporada) != "Especial" else ""
    try:
        jogos, tabelas = rsssf.ler(ano_de(temporada), pagina_rsssf(temporada))
    finally:
        LIGA_ATUAL["liga"] = ""
    for x in [*jogos, *tabelas]:
        x.grupo = _grupo_limpo(x.grupo)
    for j in jogos:   # "- Mangueira": traço que sobra da data em algumas linhas
        j.mandante, j.visitante = j.mandante.lstrip("-– ").strip(), j.visitante.lstrip("-– ").strip()
    jogos = sem_sumulas(jogos)
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
