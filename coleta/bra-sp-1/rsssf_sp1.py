"""Leitura das páginas do Campeonato Paulista da RSSSF Brasil (data/coleta/bra-sp-1/rsssfbrasil/sp{ano}.htm).

Usa o leitor comum (coleta/comum/rsssf.py) com o placar "2 x 2" e a data na frente do jogo ligados
(PLACAR_X_ESPACADO). Antes da leitura, corrige o texto das páginas que fogem desse desenho (CORRECOES, com o motivo).
Nos anos de duas ligas a página traz os dois torneios ("Campeonato Paulista 1913 APEA" ... "Campeonato Paulista
1913 LPF"); `ler(temporada)` lê só o trecho da liga pedida.

Uso: python coleta/bra-sp-1/rsssf_sp1.py [temporada ...]     (sem temporada: todas; com uma, lista as divergências)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
import rsssf  # noqa: E402
from edicoes import LIGAS, PASTA_DADOS, TEMPORADAS, ano_de, liga_de  # noqa: E402

rsssf.PASTA = PASTA_DADOS / "rsssfbrasil"
rsssf.MODELO = "sp{ano}.htm"
rsssf.PLACAR_X_ESPACADO = True

LIGA_ATUAL = {"liga": ""}   # liga pedida em ler(); a correção _liga usa
MESES_EN = {m: i for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}


def _liga(t: str) -> str:
    """Anos de duas ligas: fica só o trecho da liga pedida (do título dela até o título da outra)."""
    liga = LIGA_ATUAL["liga"]
    if not liga:
        return t
    titulos = [(m.start(), m.group(1)) for m in re.finditer(r"^\s*(?:Campeonato Paulista(?: de)? \d{4} )?(LPF|APEA|LAF)\s*$", t, re.M)]
    for k, (pos, nome) in enumerate(titulos):
        if nome == liga:
            fim = next((p for p, n in titulos[k + 1:] if n != liga), len(t))
            return t[pos:fim]
    return t


def _data_mes(t: str) -> str:
    """"08/Jul Corinthians 5-0 XV de Novembro" e "15/may   Ferroviária 0-1 Corinthians": a data com o mês por extenso vai
    para o formato "[Jul 08]" que o leitor comum entende."""
    # 1978 escreve também o ano ("03/Jun/1979"): sem aceitar o ano, os jogos de 1979 ficavam fora da leitura e vinham só
    # do ogol, com o mês errado no 3º turno (o ano vem da virada de mês do leitor comum)
    return re.sub(r"^([ \t]*)(\d{1,2})/([A-Za-z]{3})(?:/\d{4})?\b\.?[ \t]+", lambda m: f"{m[1]}[{m[3].capitalize()} {m[2]}] ", t, flags=re.M)


def _dois_pontos(t: str) -> str:
    """1979-1980: "América - Francana 2:1" com a data em linha própria ("14.05.80"). Vira "América  2-1  Francana" e
    "14/05/1980"."""
    t = re.sub(r"^([ \t]*)(\d{1,2})\.(\d{1,2})\.(\d{2})[ \t]*$", lambda m: f"{m[1]}{m[2]}/{m[3]}/19{m[4]}", t, flags=re.M)
    return re.sub(r"^([ \t]*)(\S.*?)[ \t]+-[ \t]+(\S.*?)[ \t]+(\d{1,2}):(\d{1,2})[ \t]*(.*)$", r"\1\2  \4-\5  \3  \6", t, flags=re.M)


def _sem_trecho(inicio: str, fim: str | None):
    """Tira da página o trecho de outra competição: do título `inicio` até a linha `fim` (inclusive) ou até o fim."""
    def f(t: str) -> str:
        i = t.find(inicio)
        if i < 0:
            return "" if SO_TROFEU["sim"] else t
        j = t.find("\n", t.find(fim, i)) if fim and t.find(fim, i) >= 0 else len(t)
        return t[i:j] if SO_TROFEU["sim"] else t[:i] + t[j:]   # trofeu(): só o trecho tirado
    return f


def _sem_trofeu(t: str) -> str:
    """2007-2013 e 2017-2022: tira o Troféu do Interior (torneio à parte dos clubes do interior eliminados; "Countryside
    Tournament", "COUNTRYSIDE CHAMPIONSHIP (Título do Interior)", "TROFÉU CAMPEÃO DO INTERIOR"), do título dele até a fase
    seguinte do campeonato ("LEAGUE SEMIFINALS:", "Second Phase - Quartas-de-final"), até a linha do campeão do Troféu
    (2007) ou até o fim da página (2018, 2021, 2022: o Troféu tem a sua própria "Second Phase - Fase Semifinal")."""
    m = re.search(r"^[ \t]*(?:\(\*\)[ \t]*)?TROF[ÉE]U\b.*INTERIOR.*$|^[ \t]*Trof[ée]u do Interior[ \t]*$"
                  r"|^[ \t]*Countryside (?:Tournament|Championship).*$", t, re.M | re.I)
    if not m:
        return "" if SO_TROFEU["sim"] else t
    fim = re.compile(r"^[ \t]*(?:Second (?:Phase|Stage)[ \t]*-[ \t]*Quartas|LEAGUE\b)|(?<=\n)(?=.*won the Countryside)",
                     re.M).search(t, m.end())
    if fim and fim.group(0) == "":   # 2007: até a linha do campeão do Troféu, inclusive
        fim = re.compile(r"\n").search(t, fim.end())
    if SO_TROFEU["sim"]:   # trofeu(): só o trecho do Troféu
        return t[m.start():fim.start() if fim else len(t)]
    return t[:m.start()] + (t[fim.start():] if fim else "")


SO_TROFEU = {"sim": False}


def trofeu(temporada: str) -> list:
    """Os jogos do torneio à parte da página (ANOS_A_PARTE): Troféu do Interior ou Taça Independência (2023). O importador
    tira do ogol os mesmos jogos, que vêm na mesma edição."""
    if ano_de(temporada) not in ANOS_A_PARTE:
        return []
    SO_TROFEU["sim"] = True
    try:
        return rsssf.ler(ano_de(temporada))[0]
    finally:
        SO_TROFEU["sim"] = False


_PLACAR = re.compile(r"(?<!\S)\d{1,2}-\d{1,2}(?!\S)")


def _pedaco(s: str) -> bool:
    """Linha que é só um pedaço de nome de clube ("Paulo", "Rio", "Osasco")."""
    s = s.strip()
    return (bool(s) and len(s) <= 22 and not s.startswith(("[", "(", "*")) and not re.search(r"\d", s)
            and not re.match(r"(round|group|grupo|first|second|third|fourth|final|semi|quarter|table|standing|classif|"
                             r"participants|source|top\b|pos\b)", s, re.I))


def _nomes_quebrados(t: str) -> str:
    """2014: o nome do clube quebra em duas linhas ("Bragantino   2-0   São" / "Paulo"; "Rio" / "Claro   1-0  Atlético
    Sorocaba"; "Palmeiras" / " 3-2 " / " Ponte Preta"): as linhas voltam a ser uma só."""
    ls = t.split("\n")
    i, colada = 0, -1   # colada: linha que já recebeu o resto do nome do visitante (só recebe uma vez)
    while i < len(ls) - 1:
        cur, prox = ls[i], ls[i + 1]
        m = list(_PLACAR.finditer(cur))
        if m and not cur.lstrip().startswith("[") and _pedaco(prox) and (colada != i or not cur[m[-1].end():].strip()):
            # depois do placar: o nome do visitante continua na linha de baixo (ou ainda nem começou)
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


def _tabelas_dos_grupos(t: str) -> str:
    """2016-2025: "Top 2 go to second phase (quartas-de-final)" acima das tabelas não é título de fase; e o título do
    grupo vem colado ao cabeçalho das colunas ("Group A   M  W  D  L  GF-GA  Pts")."""
    t = re.sub(r"^[ \t]*(?:Top 2 go to second phase.*|Tables:[ \t]*)$", "", t, flags=re.M)
    t = re.sub(r"^([ \t]*Group [A-Z0-9])[ \t]*(?:Pos)?[ \t]*(?:M|Team)\b.*$", r"\1", t, flags=re.M)
    t = re.sub(r"^([ \t]*\S.*?)[ \t]{2,}M[ \t]+W[ \t]+D[ \t]+L[ \t]+GF-GA.*$", r"\1", t, flags=re.M)   # "Final General Table   M  W"
    return re.sub(r"^([ \t]*Fourth Phase - Fase Final)[ \t]*-[ \t]*Group K[ \t]*$", r"\1", t, flags=re.M)   # a final não é grupo


rsssf.CORRECOES.update({
    "sp1985.htm": [(_sem_trecho("\nSecond Level", None), None, "a página traz também a 2ª e a 3ª divisões de 1985")],
    "sp2023.htm": [(_sem_trecho("Taça Independência - First Stage", "conquistou a Taça Independ"), None,
                    "a página traz a Taça Independência (torneio à parte dos clubes eliminados)")],
})
rsssf.CORRECOES.update({f"sp{a}.htm": [(_liga, None, "ano de duas ligas: lê só o trecho da liga da temporada")] for a in LIGAS})
for _a in (1962, 1966, 1967, 1968, 1969, 1970, 1973, 1974, 1975, 1978, 1981, 1983, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994):
    rsssf.CORRECOES.setdefault(f"sp{_a}.htm", []).append((_data_mes, None, "data com o mês por extenso na frente do jogo"))
# anos em que a página traz um torneio à parte (Troféu do Interior; 2023: Taça Independência), que fica de fora
ANOS_A_PARTE = {*range(2007, 2014), *range(2017, 2024)}
for _a in ANOS_A_PARTE - {2023}:
    rsssf.CORRECOES.setdefault(f"sp{_a}.htm", []).append((_sem_trofeu, None, "a página traz o Troféu do Interior (torneio à parte)"))
for _a in range(2016, 2026):
    rsssf.CORRECOES.setdefault(f"sp{_a}.htm", []).append((_tabelas_dos_grupos, None, "títulos das tabelas dos grupos"))
rsssf.CORRECOES.setdefault("sp2002.htm", []).append(
    (r"(?m)^Top 1 qualify to \"superchampionship\".*\n.*Torneio Rio S.o Paulo[ \t]*$", "",
     "a nota sobre o Supercampeonato, logo abaixo de \"First Phase\", não é título de fase"))
rsssf.CORRECOES.setdefault("sp2023.htm", []).append((r"(?m)^Group L$", "Group D", "o grupo D da 1ª fase vem como \"Group L\""))
rsssf.CORRECOES.setdefault("sp2014.htm", []).append((_nomes_quebrados, None, "nomes de clube quebrados em duas linhas"))
rsssf.CORRECOES.setdefault("sp1910.htm", []).append((_sem_trecho("Qualifying Tournament:", "3.Savóia"), None,
                                                      "a página começa com a seletiva (Ypiranga, Vila Buarque e Savóia), que não é o campeonato"))
rsssf.CORRECOES.setdefault("sp1951.htm", []).append(
    (r"(?m)^(Jabaquara \(last-placed of 1st level\))", r"Repescagem\n\n\1",
     "a repescagem Jabaquara x XV de Jaú vem sem título e ficava na fase anterior"))
rsssf.CORRECOES.setdefault("sp2003.htm", []).append((r"Atl\.Sorocaba", "Atlético Sorocaba", "nome abreviado do Atlético Sorocaba"))
rsssf.CORRECOES.setdefault("sp1927.htm", []).append(
    (r"Corinthians \(SBC\)", "Corinthians de Santo André",
     "o leitor tira a cidade entre parênteses e o Corinthians de Santo André virava o Corinthians da capital (achado SP-009)"))
rsssf.CORRECOES.setdefault("sp1942.htm", []).append(
    (r"(?m)^04/10/1942 Corinthians 3 x Palmeiras", "04/10/1942 Corinthians 3 x 1 Palmeiras",
     "o jogo vem sem os gols do Palmeiras; 3-1 pelo Futebol Nacional (achado SP-012)"))
for _a in (1979, 1980):
    rsssf.CORRECOES.setdefault(f"sp{_a}.htm", []).append((_dois_pontos, None, "jogo em 'A - B 2:1' e data em 'dd.mm.aa'"))
rsssf.CORRECOES.setdefault("sp1933.htm", []).append(
    (r"(\d+x\d+[^\n]*?)[ \t]*\n(Itália|Bento|Paulo|Corinthians|Portuguesa)[ \t]*$", r"\1 \2",
     "nome do clube quebrado em duas linhas (\"Corinthians 2x0 AA São\" / \"Bento\" virava Corinthians x São Paulo; SP-022)"))
rsssf.CORRECOES.setdefault("sp1929.htm", []).append(
    (r"09/06/1959 AA das Palmeiras", "09/06/1929 AA das Palmeiras", "ano errado na data (FN: 09/06/1929; achado QS-002)"))
rsssf.CORRECOES["sp1979.htm"].insert(0, (r"(?m)^19\.08\.78\b", "19.08.79",
                                         "ano errado na data da 15ª rodada (FN: 19/08/1979; achado QS-003)"))
rsssf.CORRECOES.setdefault("sp1969.htm", []).insert(0, (
    r"(?m)^08/Jun(\s+)Corinthians 1-3 Santos", r"25/May\1Corinthians 1-1 Santos",
    "no 2º turno a página repete o 1-3 do turno final (08/jun); o jogo do 2º turno foi 25/05 1-1 (FN e ogol; achado QS-004)"))

# letras que a própria página da RSSSF já traz trocadas por "�" (1913-1936, 1953-1972, 1984, 2008): a grafia certa
LETRAS = {"S�o": "São", "s�o": "são", "Jundia�": "Jundiaí", "It�lia": "Itália", "Guaratinguet�": "Guaratinguetá",
          "Germ�nia": "Germânia", "S�rio": "Sírio", "Independ�ncia": "Independência", "Mar�lia": "Marília",
          "Sert�ozinho": "Sertãozinho", "Am�rica": "América", "S�rie": "Série", "Liban�s": "Libanês",
          "Trof�u": "Troféu", "TROF�U": "TROFÉU", "Campe�o": "Campeão", "CAMPE�O": "CAMPEÃO", "Jos�": "José",
          "El�seos": "Elíseos", "Atl�tico": "Atlético", "Divis�o": "Divisão", "Andr�": "André",
          "In�cio": "Início", "Ribeir�o": "Ribeirão", "Uni�o": "União", "Ant�rtica": "Antártica",
          "Ferrovi�ria": "Ferroviária", "Maranh�o": "Maranhão", "S�lex": "Sílex", "Brit�nia": "Britânia",
          "Ja�": "Jaú", "Taubat�": "Taubaté", "Bragan�a": "Bragança", "�talo": "Ítalo"}


def _letras(t: str) -> str:
    for errado, certo in LETRAS.items():
        t = t.replace(errado, certo)
    return t


for _a in range(1902, 2026):   # antes das outras correções
    rsssf.CORRECOES.setdefault(f"sp{_a}.htm", []).insert(0, (_letras, None, "letras trocadas por \"�\" na página"))


def _grupo_limpo(g: str) -> str:
    """"Group D   M  W  D  L  GF-GA  Pts" e "Group DPosTeamPTSJVED...": o cabeçalho das colunas sai do nome do grupo."""
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


def ler(temporada: str):
    LIGA_ATUAL["liga"] = liga_de(temporada)
    try:
        jogos, tabelas = rsssf.ler(ano_de(temporada))
    finally:
        LIGA_ATUAL["liga"] = ""
    for x in [*jogos, *tabelas]:
        x.grupo = _grupo_limpo(x.grupo)
    _grupos_pelas_tabelas(jogos, tabelas)
    return jogos, tabelas


def conferir(temporada: str):
    jogos, tabelas = ler(temporada)
    return jogos, tabelas, rsssf.conferir(jogos, tabelas)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    alvo = sys.argv[1:] or TEMPORADAS
    for t in alvo:
        jogos, tabelas, erros = conferir(t)
        print(f"{t}: {len(jogos)} jogos, {len(tabelas)} tabelas ({sum(len(x.linhas) for x in tabelas)} linhas), {len(erros)} divergências")
        if len(alvo) == 1:
            for e in erros[:60]:
                print("   !", e)
