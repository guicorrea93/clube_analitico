"""Baixa as fontes complementares da Série D:
- ESPN: a liga "bra.4" existe, mas não tem jogos da Série D (conferido em 2019, 2023 e 2025); não é usada.
- Wikipédia em português e em inglês, uma página por edição -> data/coleta/bra-serie-d/wikipedia/{pt,en}_{ano}.txt.

Uso: python coleta/bra-serie-d/baixar_espn_wiki.py [espn|wiki] [ano ...]
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
import espn  # noqa: E402
from edicoes import ANOS, PASTA_DADOS  # noqa: E402
from wikipedia import wikitexto  # noqa: E402

JANELA = {2020: (date(2020, 7, 15), date(2021, 2, 28))}   # 2020 foi de agosto a janeiro (pandemia)
TITULOS = {
    "pt": ["Campeonato Brasileiro de Futebol de {a} - Série D", "Campeonato Brasileiro de Futebol de {a} – Série D"],
    "en": ["{a} Campeonato Brasileiro Série D"],
}

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    qual = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].isdigit() else "tudo"
    anos = [int(a) for a in sys.argv[1:] if a.isdigit()]
    if qual in ("espn", "tudo"):
        pasta = PASTA_DADOS / "espn"
        pasta.mkdir(parents=True, exist_ok=True)
        for ano in anos or [a for a in ANOS if a >= 2016]:
            destino = pasta / f"serie_d_{ano}.json"
            if destino.exists():
                continue
            ini, fim = JANELA.get(ano, (date(ano, 3, 15), date(ano, 12, 31)))
            js = espn.baixar("bra.3", ini, fim)
            destino.write_text(json.dumps(js, ensure_ascii=False, indent=0), encoding="utf-8")
            print(f"espn {ano}: {len(js)} jogos", flush=True)
    if qual in ("wiki", "tudo"):
        pasta = PASTA_DADOS / "wikipedia"
        pasta.mkdir(parents=True, exist_ok=True)
        for ano in anos or ANOS:
            for lingua, modelos in TITULOS.items():
                destino = pasta / f"{lingua}_{ano}.txt"
                if destino.exists():
                    continue
                for m in modelos:
                    txt = wikitexto(lingua, m.format(a=ano))
                    if txt:
                        destino.write_text(txt, encoding="utf-8")
                        print(f"wiki {lingua} {ano}: {len(txt)} caracteres", flush=True)
                        break
                else:
                    print(f"wiki {lingua} {ano}: sem página", flush=True)
