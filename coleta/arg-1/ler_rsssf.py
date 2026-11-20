"""Lê o trecho de cada edição nas páginas da RSSSF (data/coleta/arg-1/rsssf/) com o leitor comum (rsssf_sul).

Uso como biblioteca: ler(edicao) -> (jogos, tabelas); campeoes() -> {(ano, ordem): nome}.
Uso direto: python coleta/arg-1/ler_rsssf.py [temporada ...]   (resumo de jogos e tabelas por edição)
"""
from __future__ import annotations

import re
import sys
from functools import lru_cache
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
sys.path.insert(0, str(AQUI))
import rsssf_sul  # noqa: E402
from edicoes import EDICOES, FIM_PADRAO, PASTA_DADOS, Edicao  # noqa: E402

PASTA = PASTA_DADOS / "rsssf"

# fases reconhecidas pelo título (a primeira é a fase de partida); vale para todas as edições
FASES = [
    (r"^(Round of 16|Octavos de final|1/8 Final|Eighth[- ]?finals?)\b", "Oitavas de final"),
    (r"^(Quarter[- ]?finals?|Quarterfinal round|Cuartos de final|Quarter Final)\b", "Quartas de final"),
    (r"^(Semi[- ]?finals?|Semifinal round|Semifinales)\b", "Semifinal"),
    (r"^(Final(?!\s*(Table|Tournament|Group|Standing|phase|stage))|Grand Final|Finals?\s*[–-]\s*(first|second) leg|Final matches|Championship Final|Final \[)", "Final"),
    (r"^(Championship Playoff|First place playoffs?|Playoff to define the first|First stage winner playoff|Badgets playoff|"
     r"Final between|Desempate|Playoff \[|Playoffs?:?$|CHAMPIONSHIP PLAYOFF)", "Desempate do título"),
    (r"^(Second place playoffs?|Runner-up playoff|Playoff to define the runner-up)", "Desempate do 2º lugar"),
    (r"^(\d+(st|nd|rd|th)\.? place playoffs?|Relegation playoff|Playoff against (\d+|relegation)|Against relegation playoff|Relegation match|"
     r"Desempate por el)", "Desempate do rebaixamento"),
    (r"^(Final Tournament|Final Group|Championship Group|Petit)", "Fase final"),
    (r"^(Relegation Group)", "Grupo do rebaixamento"),
]


@lru_cache(maxsize=None)
def linhas(pagina: str) -> tuple[str, ...]:
    """Texto puro da página, com os erros de digitação corrigidos (explicacoes.CONSERTA_TEXTO, cada um com o motivo)."""
    from explicacoes import CONSERTA_TEXTO
    ls = rsssf_sul.texto(PASTA / f"{pagina}.html")
    for (pg, n), (antes, depois, _motivo) in CONSERTA_TEXTO.items():
        if pg == pagina:
            assert antes in ls[n], f"{pagina}:{n} mudou: {ls[n]!r}"
            ls[n] = ls[n].replace(antes, depois)
    return tuple(ls)


def fim_padrao(ls: tuple[str, ...], ini: int) -> int:
    """Primeira linha, depois do primeiro jogo do trecho, que abre outra competição."""
    viu_jogo = False
    for i in range(ini, len(ls)):
        s = ls[i].strip()
        if not viu_jogo:
            viu_jogo = bool(rsssf_sul._jogo(ls[i]))
            continue
        if re.match(FIM_PADRAO, s, re.I):
            return i
    return len(ls)


def ler(e: Edicao) -> tuple[list[rsssf_sul.Jogo], list[rsssf_sul.Tabela]]:
    jogos, tabelas = [], []
    for pagina, ini, fim in e.trechos:
        ls = linhas(pagina)
        fim = fim if fim is not None else fim_padrao(ls, ini)
        trecho = [""] * ini + list(ls[ini:fim])   # mantém o número da linha da página
        j, t = rsssf_sul.ler(trecho, e.ano_inicio, e.ano_fim, fases=e.fases + FASES)
        for x in j:
            x.texto = f"{pagina}:{x.linha}"
        jogos += j
        tabelas += t
    return jogos, tabelas


def campeoes() -> dict[str, list[str]]:
    """argchamp.html: temporada ("1931", "1991/92") -> [campeões na ordem da página]."""
    saida: dict[str, list[str]] = {}
    for l in linhas("argchamp"):
        m = re.match(r"^(\d{4}(?:/\d{2})?)\s+(?:Asociación|Federación|Amateurs|Liga)?\s*(.+?)\s{2,}(.+?)(?:\s{2,}(.+))?$", l)
        if not m:
            continue
        resto = re.split(r"\s{2,}", l[len(m.group(1)):].strip())
        if len(resto) >= 2:
            saida.setdefault(m.group(1), []).append(resto[1] if len(resto) >= 3 else resto[0])
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    alvo = set(sys.argv[1:])
    for e in EDICOES:
        if alvo and e.temporada not in alvo:
            continue
        js, ts = ler(e)
        fases = sorted({j.fase for j in js})
        print(f"{e.temporada:22s} {len(js):4d} jogos  {len(ts):2d} tabelas {[len(t.linhas) for t in ts][:8]}  fases {fases}")
