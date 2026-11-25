"""Leitura das páginas do Campeonato Mineiro da RSSSF Brasil (data/coleta/bra-mg-1/rsssfbrasil/mg{ano}.htm).

Usa o leitor comum (coleta/comum/rsssf.py), como o Carioca (coleta/bra-rj-1/rsssf_rj1.py), de onde vêm as correções
genéricas: a data "dd/Mon" na frente do jogo, as súmulas em caixa alta que repetem o jogo da lista e o grupo de cada jogo
pelas tabelas da fase. As correções de cada página ficam em CORRECOES, com o motivo. 1926 e os dois torneios de 1932 têm
página própria (edicoes.pagina_rsssf).

Uso: python coleta/bra-mg-1/rsssf_mg1.py [temporada ...]     (sem temporada: todas; com uma, lista as divergências)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
import rsssf  # noqa: E402
from edicoes import PASTA_DADOS, TEMPORADAS, ano_de, pagina_rsssf  # noqa: E402

rsssf.PASTA = PASTA_DADOS / "rsssfbrasil"
rsssf.MODELO = "mg{ano}.htm"
rsssf.QUEBRA_BLOCOS = True   # <P>/<PRE>/<H2> sem <br>: o título ficava colado no jogo


def _data_mes(t: str) -> str:
    """"13/Aug      Atlético 5-0 Villa Nova": a data com o mês por extenso na frente do jogo vai para o formato "[Aug 13]"
    que o leitor comum entende (igual ao Carioca); também com o ano ("02/Jan/1955 ...": "[Jan 02, 1955]")."""
    return re.sub(r"^([ \t]*)(\d{1,2})/([A-Za-z]{3})(?:/(\d{4}))?\b\.?[ \t]+",
                  lambda m: f"{m[1]}[{m[3].capitalize()} {m[2]}{', ' + m[4] if m[4] else ''}] ", t, flags=re.M)


def _wo(t: str) -> str:
    """W.O. em todas as páginas (1915-1960): "Atlético  1-WO Hygiênicos" (o Hygiênicos não compareceu: vitória do
    Atlético, 1-0 na tabela) e "América  WO-1  Yale" (o América não compareceu: vitória do Yale). O "WO" marca quem faltou,
    ao contrário do leitor comum ("0-WO": vitória do visitante). Vira "A  awd  B  [victory awarded to X]": o jogo conta
    como vitória sem gols (decisão D-15)."""
    def troca(m) -> str:
        a, placar, b, resto = m.group(1).rstrip(), m.group(2).upper(), m.group(3).strip(), (m.group(4) or "").strip()
        venc = a if placar.endswith("WO") else b
        nota = "; ".join(x.strip("[] ") for x in (f"W.O.: victory awarded to {venc}", resto) if x.strip("[] "))
        return f"{a}  awd  {b}  [{nota}]"
    return re.sub(r"(?m)^([ \t]*\S[^\n]*?)[ \t]+(\d-WO|WO-\d)[ \t]+([^\[\n]*?)[ \t]*(\[[^\n]*\])?[ \t]*$", troca, t)


def _bt(t: str) -> str:
    """"Yale  bt  Sete de Setembro" (1917, 1922): o Yale venceu, placar desconhecido. A tabela publicada conta a vitória
    sem gols, como o W.O.; vira "A  awd  B  [score unknown; victory awarded to A]" (o ogol grava 1-0, placar inventado)."""
    def troca(m) -> str:
        a, b = m.group(1).rstrip(), m.group(2).strip()
        return f"{a}  awd  {b}  [score unknown; victory awarded to {a.strip()}]"
    return re.sub(r"(?m)^([ \t]*\S[^\n]*?)[ \t]+bt[ \t]+(\S[^\n\[]*?)[ \t]*$", troca, t)


# letras que a própria página traz trocadas por "�": a grafia certa
LETRAS = {"Atl�tico": "Atlético", "Am�rica": "América", "It�lia": "Itália", "Hygi�nicos": "Hygiênicos", "S�o": "São",
          "Sider�rgica": "Siderúrgica", "Uni�o": "União", "Uberl�ndia": "Uberlândia", "Valeriodoce": "Valeriodoce"}


def _letras(t: str) -> str:
    for errado, certo in LETRAS.items():
        t = t.replace(errado, certo)
    return t


def _dois_turnos(t: str) -> str:
    """1984: cada turno ("FIRST STAGE:" e "SECOND STAGE:") tem "First Phase", "Stage semifinals:" e "Stage finals:" com o
    mesmo nome; viram "1º Turno", "1º Turno - Semifinal", "1º Turno - Final" (e o mesmo no 2º turno)."""
    saida, turno = [], 1
    for l in t.splitlines():
        s = l.strip()
        if s.startswith(("FIRST STAGE", "SECOND STAGE")):
            turno = 1 if s.startswith("FIRST") else 2
        nova = {"First Phase": f"{turno}º Turno", "Stage semifinals:": f"{turno}º Turno - Semifinal",
                "Stage finals:": f"{turno}º Turno - Final"}.get(s)
        saida.append(nova or l)
    return "\n".join(saida)


def _empatados(t: str) -> str:
    """Linha de tabela de clube empatado sem o número da posição ("  .Renascença  15  6  4  5  27-24  16"): ganha a
    posição da linha de cima (o leitor comum só lê linha de tabela que começa com o número)."""
    saida, pos = [], None
    for l in t.splitlines():
        m = re.match(r"^\s*(\d{1,2})\s*\.\s*\D", l)
        if m:
            pos = m.group(1)
        elif pos and re.match(r"^\s+\.[^\s.]", l):
            l = re.sub(r"^\s+\.", f" {pos}.", l, count=1)
        saida.append(l)
    return "\n".join(saida)


for _t in TEMPORADAS:
    rsssf.CORRECOES.setdefault(pagina_rsssf(_t), []).insert(0, (_letras, None, "letras trocadas por \"�\" na página"))
    rsssf.CORRECOES[pagina_rsssf(_t)].append((_data_mes, None, "data com o mês por extenso na frente do jogo"))
    rsssf.CORRECOES[pagina_rsssf(_t)].append((r"(\d)[ \t]*–[ \t]*(\d)", r"\1-\2", "placar com travessão (\"1–2\")"))
    rsssf.CORRECOES[pagina_rsssf(_t)].append((r"^([A-ZÀ-Ý][^\n(\[]*\bare (?:qualified|relegated|promoted)\b[^\n]*)$", r"(\1)",
                                              "frase (\"X are qualified ...\"), não título de fase"))
    rsssf.CORRECOES[pagina_rsssf(_t)].append((r"[ \t]+Att:[ \t]*([\d.,]+)[ \t]*$", r"  att: \1",
                                              "público \"Att: 535\" (o leitor comum lê \"att:\")"))
    rsssf.CORRECOES[pagina_rsssf(_t)].append((_empatados, None, "linha de tabela de clube empatado sem o número da posição"))
    rsssf.CORRECOES[pagina_rsssf(_t)].append((_bt, None, "\"A bt B\": vitória do A, placar desconhecido"))
    rsssf.CORRECOES[pagina_rsssf(_t)].append((_wo, None, "W.O. \"1-WO\" / \"WO-1\" (o WO marca quem faltou)"))

# correções de cada página, com o motivo
for _arq, _lista in {
    "mg1921.htm": [(r"^First Division[ \t]*$", "LEAGUE", "a liga depois do torneio eliminatório (sem título de fase na página)")],
    "mg1951.htm": [(r"^( 1\.Villa Nova\s+7\s+)6(\s+1\s+1\s+16- 6\s+11)", r"\g<1>5\2",
                    "1º turno: a linha do Villa Nova traz 6 vitórias (6 + 1 + 1 = 8 jogos em 7); com 11 pontos e 1 empate são 5")],
    "mg1955.htm": [(r"^\[Oct 9\]", "[Oct 9, 1955]",
                    "o 2º turno começa em outubro de 1955 (a data de cima é a de um desempate jogado em abril de 1956)")],
    "mg1959.htm": [(r"^METALLURGIC ZONE", "QUALIFY TOURNAMENTS\nMETALLURGIC ZONE",
                    "a zona metalúrgica é outra chave do torneio de classificação (vinha depois do desempate da zona do sertão)")],
    "mg1972.htm": [(r"^Group C[ \t]*$", "Qualification Tournament\nGroup C",
                    "a chave C é do torneio de classificação (vinha depois do desempate da chave B)")],
    "mg1973.htm": [(r"(First phase[\s\S]*?Round 1\s*\n\s*)\[Mar 25\]", r"\g<1>25/03/1973",
                    "a 1ª fase é de 1973 (o torneio de classificação, logo acima, terminou em dezembro de 1972); a data "
                    "numérica fixa o ano sem a virada de dezembro para março")],
    "mg1982.htm": [(r"(FINAL PHASE[\s\S]*?Round 1\s*\n\s*)\[Oct 20\]", r"\1[Oct 20, 1982]",
                    "a fase final é de outubro de 1982 (a repescagem, listada antes, é de fevereiro de 1983)")],
    "mg1983.htm": [(r"^( 1\. Atlético\s+11\s+7\s+3\s+)2(\s+20- 5\s+17)", r"\g<1>1\2",
                    "1º turno: a linha do Atlético traz 2 derrotas (7 + 3 + 2 = 12 jogos em 11); com 17 pontos é 1 derrota")],
    "mg1984.htm": [(_dois_turnos, None, "dois turnos com subfases de mesmo nome")],
    "mg2005.htm": [(r"^URT(\s+0-4\s+)URT[ \t]*$", r"URT\1Ipatinga",
                    "semifinal: a página escreve \"URT 0-4 URT\"; o adversário era o Ipatinga (ogol; volta Ipatinga 2-2 URT)")],
    "mg2021.htm": [(r"^\[Feb 29\]", "[Feb 27]", "1ª rodada: \"Feb 29\" não existe em 2021; o ogol dá 27/02/2021 para os três jogos")],
}.items():
    rsssf.CORRECOES.setdefault(_arq, []).extend(_lista)

# títulos que o leitor comum não toma por fase: "Qualification Tournament" (1972, 1973), "QUALIFY TOURNAMENTS" (1959),
# "RELEGATION TOURNAMENT" (1982), "LEAGUE" sozinho (1959, 1971: a liga depois do torneio de classificação) e os
# desempates sem outra palavra de fase ("League tiebreak", 1922; "Tie-breaking", 1954)
rsssf.FASE = re.compile(rsssf.FASE.pattern[:-1] + r"|tournament|^league$|tie-?break)", re.I)

# nome da fase em português, por temporada, quando o nome da página não basta (desempates, torneio de classificação,
# turnos): temporada -> nome na página (sem ":" no fim) -> fase. O importador usa o nome como está.
FASE_ANO: dict[str, dict[str, str]] = {
    "1920": {"Second place tiebreak": "Primeira fase - Desempate"},
    "1921": {"Final qualifiers": "Fase classificatória"},   # o torneio eliminatório ("Qualifying Tournament")
    "1922": {"League tiebreak": "Final"},   # desempate do título entre América e Palestra Itália
    "1941": {"THIRD STAGE": "Segunda fase", "TIEBREAK PLAYOFFS": "Final"},   # 3º turno só dos 4 primeiros; desempate do título
    "1952": {"Tie-breaking for First Stage": "Primeira fase - Desempate"},
    "1954": {"Tiebreak playoff": "Primeira fase - Desempate", "THIRD STAGE": "Terceira fase",
             # o desempate do 6º lugar (vaga no 3º turno), logo abaixo da tabela geral
             "Tie-breaking": "Segunda fase - Desempate"},
    "1955": {"Tiebreaking playoff": "Primeira fase - Desempate", "THIRD STAGE - all matches in Belo Horizonte": "Terceira fase"},
    "1956": {"Tie-breaking matches": "Primeira fase - Desempate"},
    "1957": {"Tiebreak playoff": "Segunda fase - Desempate"},
    "1958": {"Qualification Stage Tiebreak": "Fase classificatória - Desempate", "Second stage tiebreak": "Segunda fase - Desempate"},
    "1959": {"\"Sertão\" Zone Tiebreaking Playoff": "Fase classificatória - Desempate",
             "Metallurgic Zone Tiebreaking Playoff": "Fase classificatória - Desempate"},
    "1961": {"Tiebreak playoffs (at neutral venues)": "Primeira fase - Desempate",
             "Tiebreak (neutral venue)": "Torneio de rebaixamento"},   # desempate da repescagem (Bela Vista x Itaú)
    "1971": {"Play-Off": "Fase classificatória - Desempate"},
    "1972": {"Play-off Tournament": "Fase classificatória - Desempate", "Tiebreak": "Fase classificatória - Desempate"},
    "1973": {"Play-off matches": "Fase classificatória - Desempate", "Semifinal Phase": "Segunda fase"},
    "1974": {"Qualifying Phase": "Primeira fase", "Semifinal Phase": "Segunda fase"},   # já com os grandes: não é classificação
    "1975": {"FIRST STAGE": "1º Turno", "Stage finals": "1º Turno - Final"},
    # Taça Minas Gerais (1º turno) e Taça Governador do Estado (2º turno), depois a 2ª fase, a fase final e a decisão
    "1976": {"First Phase": "1º Turno", "Semifinal": "1º Turno - Semifinal", "Final": "1º Turno - Final",
             "First Stage": "2º Turno", "First Stage Finals": "2º Turno - Final", "Second Stage": "Segunda fase",
             "Final Phase": "Fase final", "Championship Finals": "Final"},
    "1979": {"Tie-breaking match of 2nd Stage": "Segunda fase - Desempate"},
    "1983": {"First Stage": "1º Turno", "Second Stage": "2º Turno", "2nd Stage Tie-breaking": "2º Turno - Final",
             "1st Phase Finals": "Primeira fase - Final"},
    "1987": {"FIRST STAGE": "1º Turno", "Semifinals": "1º Turno - Semifinal", "Final": "1º Turno - Final",
             "SECOND STAGE": "2º Turno", "FINALS": "Final"},
}

# torneios à parte: ficam fora (o importador tira os mesmos jogos do ogol). 1976: os Torneios Paralelos I, II e III, de
# consolação para os 11 clubes que não foram à Taça Governador do Estado (estão na página). 2020-2026: o Troféu
# Inconfidência, do 5º ao 8º da 1ª fase (a página só marca quem foi para ele; o calendário do ogol traz os jogos)
ANOS_A_PARTE: set[int] = {1976, *range(2020, 2027)}
A_PARTE = re.compile(r"^Torneio Paralelo", re.I)


def trofeu(temporada: str) -> list:
    """Jogos do torneio à parte da temporada (ANOS_A_PARTE), como estão na página."""
    if ano_de(temporada) not in ANOS_A_PARTE:
        return []
    jogos, _ = rsssf.ler(ano_de(temporada), pagina_rsssf(temporada))
    return [j for j in jogos if A_PARTE.match(j.fase)]


# jogos anulados ou cancelados que a página traz ("[annulled]", "[cancelled]": refeitos depois, ou de clube que desistiu):
# ficam fora; temporada -> jogos tirados (o importador registra no relatório e tira os mesmos do ogol)
ANULADO = re.compile(r"\bannul|\bcancel", re.I)
ANULADOS: dict[str, list] = {}


def tem_pagina(temporada: str) -> bool:
    return (rsssf.PASTA / pagina_rsssf(temporada)).exists()


def _grupo_limpo(g: str) -> str:
    """"Group D   M  W  D  L  GF-GA  Pts": o cabeçalho das colunas sai do nome do grupo."""
    return re.split(r"\s{2,}|Pos(?=Team)", g)[0].strip(" :")


def _casar_tabela(nomes_tab: list[str], nomes_jogos: set[str]) -> dict[str, str]:
    """Nome da tabela -> nome nos jogos: igual; senão o de prefixo comum mais longo; o resto pelo casamento comum."""
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
    """Fase com tabelas de grupo e os jogos misturados: os dois clubes no mesmo grupo -> esse grupo; em grupos diferentes ->
    sem grupo. Mata-mata: "grupo" de dois clubes não é grupo."""
    for fase in {j.fase for j in jogos}:
        tabs = [tb for tb in tabelas if tb.fase == fase and re.match(r"(group|grupo|s[ée]rie)\b", tb.grupo, re.I)]
        if len({tb.grupo for tb in tabs}) < 2:
            continue
        nos_jogos = {x for j in jogos if j.fase == fase for x in (j.mandante, j.visitante)}
        grupo_de = {}
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
                if gm and gv:
                    j.grupo = gm if gm == gv else ""
    clubes: dict[tuple, set] = {}
    for j in jogos:
        clubes.setdefault((j.fase, j.grupo), set()).update((j.mandante, j.visitante))
    for x in [*jogos, *tabelas]:
        if x.grupo and len(clubes.get((x.fase, x.grupo), ())) <= 2 and (not hasattr(x, "linhas") or len(x.linhas) <= 2):
            x.grupo = ""


def _caixa_alta(n: str) -> bool:
    return bool(re.search(r"[A-ZÀ-Ý]{4,}", n)) and n == n.upper()


def sem_sumulas(jogos: list) -> list:
    """Súmula em caixa alta depois do jogo decisivo ("ATLÉTICO 2 x 1 CRUZEIRO"): é o mesmo jogo da lista e sai."""
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
    jogos, tabelas = rsssf.ler(ano_de(temporada), pagina_rsssf(temporada))
    ANULADOS[temporada] = [j for j in jogos if ANULADO.search(j.nota)]
    jogos = [j for j in jogos if j not in ANULADOS[temporada] and not A_PARTE.match(j.fase)]
    tabelas = [tb for tb in tabelas if not A_PARTE.match(tb.fase)]
    for x in [*jogos, *tabelas]:
        x.fase = FASE_ANO.get(temporada, {}).get(x.fase.strip(" :"), x.fase)
        x.grupo = _grupo_limpo(x.grupo)
    for j in jogos:
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
                print("   ", e)
