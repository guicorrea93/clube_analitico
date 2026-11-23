"""Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/egy-1/rsssf/) com o leitor comum (rsssf_africa)
e, nos anos em que a RSSSF só tem a tabela final, o calendário do ogol (1964/65 a 1996/97, 2010/11, 2011/12, 2025/26).

Uso como biblioteca: ler(edicao) -> (jogos, tabelas); campeoes() -> {temporada: campeão como na página}.
Uso direto: python coleta/egy-1/ler_rsssf.py [temporada ...]   (resumo de jogos e tabelas por edição)
"""
from __future__ import annotations

import json
import re
import sys
from functools import lru_cache
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-africa"))
sys.path.insert(0, str(AQUI))
import rsssf_africa  # noqa: E402
from edicoes import EDICOES, FIM_PADRAO, PASTA_DADOS, Edicao  # noqa: E402

PASTA = PASTA_DADOS / "rsssf"

# fases reconhecidas pelo título (a primeira é a fase de partida); vale para todas as edições
FASES = [
    (r"^(Relegation (Group|Round|Stage)|Relegation Playoff Stage)\b", "Grupo do rebaixamento"),
    (r"^Relegation Play-?offs?(\s*:|\s*\[|\s*$)", "Desempate do rebaixamento"),
    (r"^(Championship (Group|Round|Stage|Play-?off)|Final (Group|Round|Stage|Tournament))\b", "Fase final"),
    (r"^(First Stage|First Phase|Regular (Season|Stage)|Group Stage)\b", ""),
    (r"^(Second Place (Match|Play-?off)|Play-?off for (second|2nd) place)", "Desempate do 2º lugar"),
    (r"^(Championship Final|Final(?!\s*(Table|Tournament|Group|Standing|phase|stage|Round))\b)", "Final"),
    (r"^(Title Play-?off|Play-?off for (the )?(title|championship))", "Desempate do título"),
]


@lru_cache(maxsize=None)
def linhas(pagina: str) -> tuple[str, ...]:
    """Texto puro da página, com os erros de digitação corrigidos (explicacoes.CONSERTA_TEXTO, cada um com o motivo)."""
    from explicacoes import CONSERTA_TEXTO
    # travessão no placar ("2–0") em parte das páginas: vira hífen
    ls = [l.replace("–", "-").replace("—", "-") for l in rsssf_africa.texto(PASTA / f"{pagina}.html")]
    # nome de clube com apóstrofo perto do fim ("Razja'h", "Ala'ab"): o leitor comum recusa a linha (protege de "58' Kempes")
    # e o jogo some; sem o apóstrofo, a linha é lida (2013/14, 2014/15 e 2017/18 perdiam 10 a 38 jogos)
    ls = [l.replace("Razja'h", "Razjah").replace("Ala'ab", "Alaab") for l in ls]
    # cidade entre colchetes logo depois do nome, na tabela ("8.Al Qanat [Suez]  26 7 9 10 ..."): o leitor comum não lê a
    # linha e a tabela se parte em duas (1991/92 a 1995/96); vira parênteses, como nas outras páginas
    ls = [re.sub(r"^(\s*\d+\.\S.*?)\s\[([A-Z][A-Za-z ]+)\](\s+\d)", r"\1 (\2)\3", l) for l in ls]
    for (pg, n), (antes, depois, _motivo) in CONSERTA_TEXTO.items():
        if pg == pagina:
            assert antes in ls[n], f"{pagina}:{n} mudou: {ls[n]!r}"
            ls[n] = ls[n].replace(antes, depois)
    return tuple(ls)


def inicio(ls: tuple[str, ...]) -> int:
    """Nas páginas de 2009/10 em diante, o índice do topo ("First Level", "Egypt Cup", "Second Level") repete os títulos:
    o campeonato começa no segundo "First Level"."""
    vistos = [i for i, l in enumerate(ls) if l.strip() == "First Level"]
    return vistos[1] if len(vistos) >= 2 else 0


def fim_padrao(ls: tuple[str, ...], ini: int) -> int:
    """Primeira linha, depois da primeira tabela ou jogo do trecho, que abre outra competição."""
    viu = False
    for i in range(ini, len(ls)):
        s = ls[i].strip()
        if not viu:
            viu = bool(rsssf_africa._jogo(ls[i]) or rsssf_africa.linha_tabela(ls[i]))
            continue
        if re.match(FIM_PADRAO, s, re.I):
            return i
    return len(ls)


# "Results Ahly:" e a lista dos resultados de um clube (ida e volta na mesma linha, sem data e sem dizer quem era o
# mandante): ficam de fora, como os "Known Results" do par-1
_RESULTADOS = re.compile(r"^(Group )?Results \w+:?\s*$")
_IDA_VOLTA = re.compile(r"^\S.*?\s+(\d+-\s*\d+|unknown|ann\b.*?)\s*(\[\*\])?\s+(\d+-\s*\d+|unknown|ann\b.*?)\s*(\[.*)?$")


def _sem_resultados(ls: list[str]) -> list[str]:
    saida, dentro = [], False
    for l in ls:
        s = l.strip()
        if _RESULTADOS.match(s):
            dentro = True
            saida.append("")
            continue
        if dentro and (not s or _IDA_VOLTA.match(s) or re.match(r"^Results \w+", s)):
            saida.append("")
            continue
        dentro = False
        # linha de tabela cruzada ("Ismaily  xxx 0-1 0-1"): os jogos entram à mão (explicacoes.EXTRAS)
        saida.append("" if re.search(r"\bxxx\b", s, re.I) else l)
    # autores que continuam na linha de baixo ("  [Moustafa Gaafar 6, ...;" / "   Mohamed Abd Rabbou "Felix" 22]"): a
    # continuação vai para a linha de cima (sozinha, "Abd" era lido como jogo abandonado)
    for k in range(1, len(saida)):
        s = saida[k].strip()
        if s and "[" not in s and s.endswith("]"):
            ant = next((i for i in range(k - 1, max(k - 4, -1), -1) if saida[i].strip()), None)
            if ant is not None and saida[ant].strip().startswith("[") and "]" not in saida[ant]:
                saida[ant] = saida[ant].rstrip() + " " + s
                saida[k] = ""
    return saida


def _trecho(pagina: str, ini: int, fim: int | None) -> tuple[list[str], int, int]:
    ls = linhas(pagina)
    if ini == 0:
        ini = inicio(ls)
    fim = fim if fim is not None else fim_padrao(ls, ini)
    return [""] * ini + _sem_resultados(list(ls[ini:fim])), ini, fim   # mantém o número da linha da página


def ler(e: Edicao) -> tuple[list[rsssf_africa.Jogo], list[rsssf_africa.Tabela]]:
    jogos, tabelas = [], []
    if e.ogol is not None:
        jogos += ogol_jogos(e)
    for pagina, ini, fim in e.trechos:
        trecho, ini, fim = _trecho(pagina, ini, fim)
        j, t = rsssf_africa.ler(trecho, e.ano_inicio, e.ano_fim, fases=e.fases + FASES)
        for x in j:
            x.texto = f"{pagina}:{x.linha}"
        jogos += j
        tabelas += t
    for pagina, ini, fim in e.tabelas:   # página que só tem a tabela final (os jogos vêm do ogol, ou não há)
        trecho, ini, fim = _trecho(pagina, ini, fim)
        tabelas += rsssf_africa.ler(trecho, e.ano_inicio, e.ano_fim, fases=e.fases + FASES)[1]
    return jogos, tabelas


def campeoes() -> dict[str, str]:
    """egychamp.html (seção "National League"): temporada do pacote -> campeão como na página ("" = sem campeão)."""
    saida: dict[str, str] = {}
    ls = linhas("egychamp")
    ini = next(i for i, l in enumerate(ls) if l.strip() == "National League")
    for l in ls[ini:]:
        m = re.match(r"^(\d{4}(?:/\d{2})?)\s+(\S.*?)\s*$", l)
        if not m:
            continue
        temp = "2012/13" if m.group(1) == "2013" else "1971/72" if m.group(1) == "1970/71" else m.group(1)
        saida[temp] = "" if re.match(r"^not (held|finished)", m.group(2)) else m.group(2)
    return saida


# ------------------------------------------------------------------------------------------------ ogol

def _ogol_por_ano() -> dict[int, list[dict]]:
    pasta = PASTA_DADOS / "ogol"
    saida: dict[int, list[dict]] = {}
    for ed in json.loads((pasta / "edicoes.json").read_text(encoding="utf-8")):
        f = pasta / f"{ed['id']}.json"
        if f.exists():
            saida.setdefault(ed["ano_inicio"], []).extend(json.loads(f.read_text(encoding="utf-8")))
    return saida


_OG: dict[int, list[dict]] | None = None
# fases do calendário do ogol além das rodadas ("R12")
OGOL_FASES = {"POff": "Desempate do título","POut": "Desempate do rebaixamento", "F": "Final", "RF": "Fase final"}
# temporadas em que a 1ª fase (turno único) é seguida de um grupo do título e de um grupo do rebaixamento (o ogol recomeça a
# contar as rodadas: "R1"): o segundo encontro de um par de clubes, na ordem das datas, já é da 2ª fase; os grupos saem de
# quem joga com quem nela, e o do título é o do clube indicado
DIVIDE_DEPOIS: dict[str, str] = {"2025/26": "Zamalek"}


def ogol_jogos(e: Edicao) -> list[rsssf_africa.Jogo]:
    """Calendário do ogol do ano como jogos (texto "ogol:<id do jogo>"). A fase "R12" é a 12ª rodada."""
    global _OG
    if _OG is None:
        _OG = _ogol_por_ano()
    saida = []
    for k, g in enumerate(sorted(_OG.get(e.ogol, []), key=lambda g: (g["data"], g["id"]))):
        if g["gols_mandante"] is None:
            continue
        f = g.get("fase") or ""
        rod = re.fullmatch(r"R(\d+)", f)
        fase = "" if rod or not f else OGOL_FASES.get(f, f)
        saida.append(rsssf_africa.Jogo(linha=k, mandante=g["mandante"], visitante=g["visitante"], gm=g["gols_mandante"],
                                       gv=g["gols_visitante"], rodada=int(rod.group(1)) if rod else g.get("rodada"),
                                       data=g["data"] if g["data"][:4] != "0000" else None, fase=fase, texto=f"ogol:{g['id']}"))
    if e.temporada in DIVIDE_DEPOIS:
        lider, vistos, depois = DIVIDE_DEPOIS[e.temporada], set(), []
        for j in sorted(saida, key=lambda j: (j.data or "9999", j.linha)):
            par = frozenset((j.mandante, j.visitante))
            (depois.append(j) if par in vistos else vistos.add(par))
        grupo = {next(x for j in depois for x in (j.mandante, j.visitante) if lider.lower() in x.lower())}
        mudou = True
        while mudou:
            n = len(grupo)
            grupo |= {x for j in depois if {j.mandante, j.visitante} & grupo for x in (j.mandante, j.visitante)}
            mudou = len(grupo) != n
        for j in depois:
            j.fase = "Fase final" if j.mandante in grupo else "Grupo do rebaixamento"
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    alvo = set(sys.argv[1:])
    for e in EDICOES:
        if alvo and e.temporada not in alvo:
            continue
        js, ts = ler(e)
        fases = {}
        for j in js:
            fases[j.fase] = fases.get(j.fase, 0) + 1
        print(f"{e.temporada:10s} {len(js):4d} jogos  {len(ts):2d} tabelas {[len(t.linhas) for t in ts]}  fases {fases}")
