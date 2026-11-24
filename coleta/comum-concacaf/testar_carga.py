"""Testa a carga de um pacote numa CÓPIA do banco (o db/futebol.db não é tocado: só leitura).

Copia o banco para a pasta temporária, carrega o pacote com futebol/carregar_pacotes.py e mostra a conferência do
carregador ("mex-1: N edições, N jogos, ... -> OK").

Uso (da raiz do clube_analitico): python coleta/comum-concacaf/testar_carga.py mex-1 <pasta temporária, ex. o scratchpad>
"""
from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(RAIZ / "futebol"))


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    slug, pasta = sys.argv[1], Path(sys.argv[2])
    pasta.mkdir(parents=True, exist_ok=True)
    origem = sqlite3.connect(f"file:{RAIZ / 'db' / 'futebol.db'}?mode=ro", uri=True)
    copia = sqlite3.connect(pasta / f"teste_{slug}.db")
    origem.backup(copia)
    origem.close()
    import carregar_pacotes
    carregar_pacotes.carregar(copia, slug)
    copia.commit()
    copia.close()


if __name__ == "__main__":
    main()
