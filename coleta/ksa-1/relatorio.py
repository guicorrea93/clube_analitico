"""Escreve o relatório da coleta (docs/coleta/ksa-1.md) a partir do pacote e de data/coleta/ksa-1/conferencia_detalhe.json.

Uso: python coleta/ksa-1/relatorio.py   (o importar.py já chama)
"""
from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from explicacoes import OGOL_CORRIGE, TABELA_RSSSF  # noqa: E402

RAIZ = AQUI.parent.parent
PACOTE = RAIZ / "data" / "coleta" / "ksa-1" / "pacote"
ARQ = RAIZ / "docs" / "coleta" / "ksa-1.md"

CABECALHO = """# Campeonato Saudita (1ª divisão) — coleta de dados

Gerado por `python coleta/ksa-1/importar.py`. Pacote em `data/coleta/ksa-1/pacote/`.

**Edições:** {n_ed}, as temporadas da lista oficial de campeões, de 1957/58 a 2025/26, como o relatório da federação
saudita de 2025 (reproduzido pela Wikipédia em inglês, página "Saudi Pro League"): Al-Hilal 21 títulos, Al-Ittihad 14,
Al-Nassr 11, Al-Ahli 9. Decisão do Guilherme (24/11/2026): desde 1957, como a federação conta (a RSSSF conta desde
1974/75). Eras: "His Majesty's League" (1957/58-1973/74, mata-mata; os campeões são os da antiga Copa do Rei), Liga de
Classificação (1974/75, dois grupos e final), Premier League (1975/76-2006/07; de 1990/91 a 2006/07 o título era decidido
num playoff dos 4 primeiros, o "Golden Box") e Pro League (2007/08 em diante). 1966/67 (não concluída), 1967/68 (não
disputada), 1969/70 e 1975/76 (canceladas) entram sem campeão. 2026/27 entra quando acabar.

**Fora do pacote:** a Copa do Rei (de 1957 a 1974 só a final, como a edição do campeonato que a federação conta), a Copa do
Príncipe Herdeiro, a Copa da Federação, a Supercopa, a repescagem e a 2ª divisão.

**Fontes:** RSSSF (uma página por temporada, `sauNN.html`, e a lista da Copa do Rei, `saucuphist.html`, em
`data/coleta/ksa-1/rsssf/`: tabela final de todos os anos de 1974/75 em diante, os jogos da fase de liga em 1974/75,
1976/77, 1980/81, 1982/83, 1983/84, 1986/87 e 1997/98-2024/25, os jogos do playoff e os autores dos gols até 2005/06);
ogol (calendário de 1999/00 a 2025/26, só a fase de liga: `data/coleta/ksa-1/ogol/` e `data/cache/ogol-ksa-1/`, para os
escudos); ESPN (liga `ksa.1`, 2022/23 a 2025/26: autores dos gols, cartões, estádio, público e hora,
`data/coleta/ksa-1/espn/`); Wikipédia em inglês (lista oficial de campeões e vices; matrizes de resultados de 2010/11 e
2011/12 nas correções).

**Clubes:** {n_cl}. Nome árabe com hífen; Al-Hilal, Al-Ittihad, Al-Nassr e Al-Shabab com o nome puro (combinado entre os
agentes); os homônimos de clubes de outros países com a cidade (Al-Ahli de Jeddah, Al-Wehda de Meca, Al-Qadsiah de
Khobar, Al-Faisaly de Harmah, Al-Khaleej de Saihat, Al-Nahda de Dammam, Al-Ansar de Medina, Al-Najma de Unaizah,
Al-Orobah de Sakakah, Al-Arabi de Unaizah, Al-Ain de Al-Baha). As grafias de cada fonte estão no `nomes_fonte` do
`clubes.csv` (regras em `coleta/ksa-1/clubes_ksa.py`).

**Regras:** placar oficial, com a prorrogação; jogos decididos fora de campo (`awd`) com o placar dado e o de campo na
observação. Os jogos da fase de liga vêm da RSSSF até 2005/06 quando ela tem a fase completa e do ogol nos outros anos
(1999/00 em diante); o playoff do título vem sempre da RSSSF. Anos sem os jogos na RSSSF nem no ogol (1977/78-1979/80,
1984/85, 1985/86, 1987/88-1996/97): só a tabela final (e os jogos do playoff que a RSSSF tem). Classificação final: a
tabela da fase de liga da RSSSF, com o campeão e o vice oficiais em cima; os números são só da fase de liga (sem o
playoff); nos anos em que a RSSSF dá só jogos e pontos (1977/78-1981/82) ou só a ordem (1985/86), o resto fica vazio.
Pontos por vitória: 2 até 1992/93, 3 de 1993/94 em diante (tirado das tabelas). `ajuste_pontos`: punições e bônus da
tabela da RSSSF. Rebaixado: o marcado na tabela da RSSSF. 1957/58-1973/74: campeão e vice da lista oficial; o jogo da final
da Copa do Rei da RSSSF quando ela tem o mesmo par (o rótulo da temporada às vezes é o anterior). Artilheiro: o da lista da
página da RSSSF; sem ela, a soma dos gols com autor quando ao menos 95% dos gols têm autor.

**Conferência:** a tabela calculada dos jogos contra a tabela da RSSSF (jogos, vitórias, empates, derrotas, gols e pontos
sem o ajuste); os placares da fonte dos jogos contra a outra (RSSSF x ogol) e contra a ESPN; o campeão contra a final do
playoff. Correções do ogol com prova em `coleta/ksa-1/explicacoes.py`.

**Edições sem jogos:** {sem_jogos}.

**Edições com jogos incompletos:** 1976/77 (a RSSSF tem 55 dos 56: o 56º é o awd Al-Ittihad x Al-Ahli, que entra; ver
a edição) e os anos de playoff sem a final na RSSSF (1994/95, 1995/96).

**Resumo:** {n_j} jogos, {n_g} gols com autor, {n_c} cartões.
"""


def ler(nome: str) -> list[dict]:
    with (PACOTE / f"{nome}.csv").open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    ed, part, gols, cart = ler("edicoes"), ler("partidas"), ler("gols"), ler("cartoes")
    clubes, conf, art = ler("clubes"), ler("conferencia"), ler("artilheiros")
    det = {x["temporada"]: x for x in json.loads((PACOTE.parent / "conferencia_detalhe.json").read_text(encoding="utf-8"))}
    por_temp = Counter(p["temporada"] for p in part)
    sem = [e["temporada"] for e in ed if not por_temp[e["temporada"]]]
    out = [CABECALHO.format(n_ed=len(ed), n_cl=len(clubes), n_j=len(part), n_g=len(gols), n_c=len(cart),
                            sem_jogos=f"{len(sem)} ({', '.join(sem)})").strip(), "",
           "| Temporada | Clubes | Jogos | Gols | c/ autor | Fonte dos jogos | Campeão | Vice |", "|---|---|---|---|---|---|---|---|"]
    cf = {c["temporada"]: c for c in conf}
    for e in ed:
        t = e["temporada"]
        out.append(f"| {t} | {e['num_clubes']} | {cf[t]['jogos']} | {cf[t]['gols']} | {cf[t]['gols_com_autor']} | "
                   f"{det[t]['fonte_jogos']} | {e['campeao'] or '—'} | {e['vice'] or '—'} |")
    out += ["", "## Correções do ogol", ""]
    out += [f"- jogo {k} do ogol: {v['motivo']}." for k, v in OGOL_CORRIGE.items()]
    out += ["", "## Conferência e observações, edição a edição", ""]
    arts = {}
    for a in art:
        arts.setdefault(a["temporada"], []).append(a)
    for e in ed:
        t = e["temporada"]
        d = det[t]
        fim = int(t[:4]) + 1
        linhas = [f"### {t}", "", f"- Formato: {d['formato']}.", f"- Jogos: {d['fonte_jogos']}."]
        linhas += [f"- {o}." for o in d["obs"]]
        for fonte, (ok, dif) in d["conf"].items():
            linhas.append(f"- {fonte}: {ok} placares iguais, {dif} diferentes.")
        if d["difs"]:
            linhas.append("- Diferenças: " + "; ".join(d["difs"]) + "." + (f" {TABELA_RSSSF[fim]}" if fim in TABELA_RSSSF else ""))
        if d["gols_dif"]:
            linhas.append("- Jogos sem os autores (a ESPN não fecha com o placar): " + "; ".join(d["gols_dif"]) + ".")
        if t in arts:
            linhas.append("- Artilheiro: " + "; ".join(f"{a['jogador']} ({a['clube']}), {a['gols']} ({a['fonte']})" for a in arts[t]) + ".")
        out += linhas + [""]
    ARQ.write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    main()
