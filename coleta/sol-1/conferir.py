"""Confere a soma dos jogos de cada fase (e grupo) com as tabelas publicadas pela RSSSF no mesmo trecho.

Compara jogos, vitórias, empates, derrotas, gols pró e contra (os pontos variam: bônus de 1996-2000, punições). Tabela cujos
clubes não estão todos nos jogos da fase fica de fora; nas edições com parte dos jogos (incompleta) não há conferência.

Uso: python coleta/sol-1/conferir.py [-v] [temporada ...]
"""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from clubes_sol import clube  # noqa: E402
from edicoes import EDICOES, Edicao  # noqa: E402
from ler import J, T, ler  # noqa: E402

CONTA = ("j", "v", "e", "d", "gp", "gc")
TODAS: dict[str, list[T]] = {}


def placar(j: J) -> tuple[int | None, int | None]:
    """Placar que conta na tabela: o oficial (tribunal) quando há."""
    if j.gm_of is not None:
        return j.gm_of, j.gv_of
    return j.gm, j.gv


def soma(jogos: list[J]) -> dict[str, dict[str, int]]:
    s: dict[str, dict[str, int]] = defaultdict(lambda: dict.fromkeys(CONTA, 0))
    for j in jogos:
        if j.especial in ("anulado", "abd"):
            continue   # anulado (e jogado de novo) ou abandonado: não conta
        if j.especial == "derrota_ambos":   # decisão fora de campo: derrota sem gols para os dois
            for c in (j.mandante, j.visitante):
                s[c]["j"] += 1
                s[c]["d"] += 1
                s[c]["gc"] += getattr(j, "gc_ambos", 0)   # "awarded 0-3 against both clubes" (2018): 3 gols contra para cada um
            continue
        gm, gv = placar(j)
        if j.especial in ("wo_m", "wo_v"):
            if getattr(j, "gols_contam", False):   # vitória dada, mas a tabela conta os gols de campo (2007/08)
                for c, a, b, venceu in ((j.mandante, j.gm, j.gv, j.especial == "wo_m"), (j.visitante, j.gv, j.gm, j.especial == "wo_v")):
                    s[c]["j"] += 1
                    s[c]["v" if venceu else "d"] += 1
                    s[c]["gp"] += a
                    s[c]["gc"] += b
                continue
            gm, gv = (1, 0) if j.especial == "wo_m" else (0, 1)
            sem_gols = True
        else:
            sem_gols = False
        if gm is None:
            continue
        for c, a, b in ((j.mandante, gm, gv), (j.visitante, gv, gm)):
            r = s[c]
            r["j"] += 1
            r["v" if a > b else "e" if a == b else "d"] += 1
            if not sem_gols:
                r["gp"] += a
                r["gc"] += b
    return s


def nomes(e: Edicao, jogos: list[J], tabelas: list[T]) -> tuple[list[J], list[T], set[str]]:
    """Troca os nomes da página pelos de exibição; devolve também os que não resolveram."""
    falta = set()
    for j in jogos:
        j.nome_m, j.nome_v = j.mandante, j.visitante
        for campo in ("mandante", "visitante"):
            n = clube(getattr(j, campo), e.ano_inicio)
            if n is None:
                falta.add(getattr(j, campo))
            else:
                setattr(j, campo, n)
    for t in tabelas:
        for r in t.linhas:
            r["clube"] = clube(r["nome"], e.ano_inicio)
            if r["clube"] is None:
                falta.add(r["nome"])
    return jogos, tabelas, falta


def js_fase0(e: Edicao) -> str:
    return e.trechos[0][3]


def conferir(e: Edicao, verbose: bool = False) -> tuple[list[J], list[T], list[tuple], set[str]]:
    """(jogos, tabelas conferidas, divergências [(tabela, clube, campo, tabela, jogos)], nomes sem clube). Todas as tabelas
    ficam em conferir.TODAS[temporada], com t.usada (conferida) e t.sem_jogos (fase sem nenhum jogo, ex.: 1994)."""
    jogos, tabelas, falta = nomes(e, *ler(e))
    TODAS[e.temporada] = tabelas
    usadas, difs = [], []
    for t in tabelas:
        t.usada = False
        t.sem_jogos = not any(j.fase == t.fase and j.grupo == t.grupo for j in jogos)
        js = [j for j in jogos if j.fase == t.fase and j.grupo == t.grupo]
        if e.acumula and t.fase == "Grupo do rebaixamento":   # tabela do grupo do rebaixamento que soma a fase regular
            js = [j for j in jogos if j.fase in (t.fase, js_fase0(e))]
        clubes_jogos = {j.mandante for j in js} | {j.visitante for j in js}
        if not js or any(r["clube"] not in clubes_jogos for r in t.linhas):
            if verbose:
                print(f"  tabela fora da conferência ({t.pagina}:{t.linha}, {t.fase} {t.grupo}): {len(js)} jogos")
            continue
        if "parte dos jogos" in e.incompleta:   # só parte dos jogos: a tabela fica como publicada, sem conferência
            continue
        usadas.append(t)
        t.usada = True
        s = soma(js)
        for r in t.linhas:
            for c in CONTA:
                if r[c] != s[r["clube"]][c]:
                    difs.append((t, r["clube"], c, r[c], s[r["clube"]][c]))
    return jogos, usadas, difs, falta


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    verbose = "-v" in sys.argv
    pedidas = {a for a in sys.argv[1:] if a != "-v"}
    for e in EDICOES:
        if (pedidas and e.temporada not in pedidas) or not e.trechos:
            continue
        jogos, usadas, difs, falta = conferir(e, verbose)
        sem = [t for t in {(j.fase, j.grupo) for j in jogos} if t not in {(u.fase, u.grupo) for u in usadas}]
        print(f"{e.temporada}: {len(jogos)} jogos, {len(usadas)} tabelas conferidas, {len(difs)} divergências"
              + (f", sem tabela: {sorted(sem)}" if sem and verbose else "") + (f", SEM NOME: {sorted(falta)}" if falta else ""))
        if difs and (verbose or pedidas):
            for t, c, campo, vt, vj in difs:
                print(f"   {t.pagina}:{t.linha} {t.fase} {t.grupo} {c}: {campo} tabela {vt} x jogos {vj}")


if __name__ == "__main__":
    main()
