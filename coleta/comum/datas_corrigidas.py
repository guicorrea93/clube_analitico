"""Datas corrigidas por jogo, com a fonte, em data/coleta/<slug>/datas_corrigidas.csv (temporada, data_pacote, mandante,
visitante, placar, data_certa, fonte). Caso típico: o ogol grava o jogo noturno com o dia seguinte, e o Bola n@ Área e o
transfermarkt (linhagens diferentes) dão a mesma data, um dia antes (achados QC-002, QC-003 e QC-004 da revisão).

Uso no importador: aplicar(PASTA_DADOS, ano, partidas, nome, log), depois de juntar as fontes. Linha que não acha o
jogo faz o importador parar (a lista foi feita sobre o pacote; se o jogo mudou, a linha precisa ser revista).
Para refazer os arquivos a partir das listas da revisão: python coleta/comum/datas_corrigidas.py
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

CAMPOS = ["temporada", "data_pacote", "mandante", "visitante", "placar", "data_certa", "fonte"]


def ler(pasta: Path) -> list[dict]:
    f = pasta / "datas_corrigidas.csv"
    return list(csv.DictReader(open(f, encoding="utf-8"))) if f.exists() else []


def aplicar(pasta: Path, ano, partidas: list, nome, log: list[str]) -> None:
    linhas = [r for r in ler(pasta) if r["temporada"] == str(ano)]
    if not linhas:
        return
    por_chave = {(r["data_pacote"], r["mandante"], r["visitante"]): r for r in linhas}
    usados = set()
    for p in partidas:
        k = (p.data, nome(p.mandante), nome(p.visitante))
        r = por_chave.get(k)
        if not r or k in usados:
            continue
        if r["placar"] and r["placar"] != f"{p.gm}-{p.gv}":
            raise ValueError(f"{ano}: data corrigida com placar diferente no pacote: {k} {p.gm}-{p.gv} x {r['placar']}")
        usados.add(k)
        p.data = r["data_certa"]
    faltam = [k for k in por_chave if k not in usados]
    if faltam:
        raise ValueError(f"{ano}: datas_corrigidas.csv sem jogo correspondente no pacote: {faltam[:5]}")
    log.append(f"{ano}: {len(usados)} datas corrigidas (datas_corrigidas.csv; ex.: {linhas[0]['mandante']} x "
               f"{linhas[0]['visitante']} {linhas[0]['data_pacote']} -> {linhas[0]['data_certa']}, {linhas[0]['fonte']})")


# listas da revisão (revisao/QC/, só leitura) e os anos que o plano manda corrigir (docs/revisao/plano-coleta-brasil.md)
PLANO = {"bra-serie-c": {"2010", "2013", "2015", "2019", "2026"}, "bra-serie-d": {"2010", "2021", "2026"},
         "bra-copa-do-brasil": {"2008", "2014", "2015", "2018", "2024"}}
ACHADO = {"bra-serie-c": "QC-002", "bra-serie-d": "QC-003", "bra-copa-do-brasil": "QC-004"}


def gerar(raiz: Path) -> None:
    saida: dict[str, list[list]] = {s: [] for s in PLANO}
    tres = re.compile(r"^(\S+) (\d{4}) \| pacote (\d{4}-\d\d-\d\d) (.+?) (\d+)-(\d+) (.+?) \(fonte [^)]*\) \| bola e tm: (\d{4}-\d\d-\d\d)")
    for l in open(raiz / "revisao" / "QC" / "saida_datas_3fontes.txt", encoding="utf-8"):
        m = tres.match(l)
        if m and m[1] in PLANO and m[2] in PLANO[m[1]]:
            saida[m[1]].append([m[2], m[3], m[4], m[7], f"{m[5]}-{m[6]}", m[8],
                                f"Bola n@ Área e transfermarkt ({ACHADO[m[1]]})"])
    tm = re.compile(r"^(\S+) (2026) \| pacote (\d{4}-\d\d-\d\d) (.+?) (\d+)-(\d+) (.+?) \d\d:\d\d \| tm (\d{4}-\d\d-\d\d)")
    for l in open(raiz / "revisao" / "QC" / "saida_tm_2026.txt", encoding="utf-8"):
        m = tm.match(l)
        if m and m[1] in PLANO:
            saida[m[1]].append([m[2], m[3], m[4], m[7], f"{m[5]}-{m[6]}", m[8],
                                f"transfermarkt e Futebol Nacional, jogo noturno ({ACHADO[m[1]]})"])
    for slug, linhas in saida.items():
        f = raiz / "data" / "coleta" / slug / "datas_corrigidas.csv"
        with open(f, "w", encoding="utf-8", newline="") as arq:
            w = csv.writer(arq)
            w.writerow(CAMPOS)
            w.writerows(sorted(linhas))
        print(slug, len(linhas), "datas")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    gerar(Path(__file__).resolve().parents[2])
