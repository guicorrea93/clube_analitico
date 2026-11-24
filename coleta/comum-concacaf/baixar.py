"""Download educado, comum a todas as coletas: espera entre pedidos, guarda a página baixada,
não baixa de novo o que já tem e trata o erro 429 (espera e tenta de novo).
Copiado de coleta/comum-sulamerica/baixar.py em 23/11/2026.

Uso como biblioteca: pegar(url, destino) -> bytes
"""
from __future__ import annotations

import time
import urllib.error
import urllib.request
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0 (clube-analitico; projeto pessoal de estatisticas)"}
_ultimo = [0.0]


def pegar(url: str, destino: Path | None = None, espera: float = 1.5, tentativas: int = 6, de_novo: bool = False) -> bytes | None:
    """Conteúdo da URL. Com `destino`, lê de lá se já existe e grava o que baixar. 404 devolve None."""
    if destino is not None and destino.exists() and not de_novo:
        return destino.read_bytes()
    for t in range(tentativas):
        falta = espera - (time.time() - _ultimo[0])
        if falta > 0:
            time.sleep(falta)
        _ultimo[0] = time.time()
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45) as r:
                dados = r.read()
            break
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if t == tentativas - 1:
                raise
            time.sleep(max(int(e.headers.get("Retry-After") or 0), 10 * (t + 1)) if e.code == 429 else 5 * (t + 1))
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            if t == tentativas - 1:
                raise
            time.sleep(5 * (t + 1))
    if destino is not None:
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_bytes(dados)
    return dados
