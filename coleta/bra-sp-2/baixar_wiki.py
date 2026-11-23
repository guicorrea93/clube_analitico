"""Baixa o código das páginas da Wikipédia em português de cada edição da A2 para data/coleta/bra-sp-2/wikipedia/pt_{ano}.wiki.

O título muda com o nome da divisão em cada época ("Campeonato Paulista de Futebol de 1970 - Primeira Divisão"). Página
já baixada não é baixada de novo; ano sem página fica sem arquivo.

Uso: python coleta/bra-sp-2/baixar_wiki.py [ano ...]     (sem anos: 1967-1984, as edições do achado A2-001)
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
from edicoes import PASTA_DADOS  # noqa: E402
from wikipedia import wikitexto  # noqa: E402

PASTA = PASTA_DADOS / "wikipedia"


def divisao(a: int) -> str:
    """Nome da divisão no título da página da Wikipédia (o mesmo de edicoes._NOMES, sem a liga)."""
    if a <= 1959:
        return "Segunda Divisão"
    if a <= 1976:
        return "Primeira Divisão"
    if a <= 1979:
        return "Divisão Intermediária"
    if a <= 1986:
        return "Segunda Divisão"
    if a <= 1990:
        return "Divisão Especial"
    if a <= 1993:
        return "Divisão Intermediária"
    return "Série A2"


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA.mkdir(parents=True, exist_ok=True)
    anos = [int(x) for x in sys.argv[1:]] or [a for a in range(1967, 1985) if a != 1979]
    for a in anos:
        destino = PASTA / f"pt_{a}.wiki"
        if destino.exists():
            continue
        texto = wikitexto("pt", f"Campeonato Paulista de Futebol de {a} - {divisao(a)}")
        if texto:
            destino.write_text(texto, encoding="utf-8")
        print(a, f"{len(texto)} caracteres" if texto else "sem página", flush=True)
