"""Baixa o placar diário da ESPN de uma copa nacional para data/coleta/<slug>/espn/<liga>_<ano>.json (D5b: datas).

Ligas da ESPN com copa: chi.copa_chi (Copa Chile), col.copa (Copa Colômbia), arg.copa (Copa Argentina). A Copa
Venezuela não está na ESPN. Cada dia fica guardado em data/cache/espn-sulamerica/<liga>/<AAAAMMDD>.json (rodar de novo
não baixa outra vez).

Cada jogo leva também "temporada", o ano da edição para a ESPN (a Copa Chile 2014/15 começa em maio de 2014; o
importador só casa com a edição desse ano de início).

Uso: python coleta/comum-sulamerica/baixar_espn_copa.py <liga> <slug> <ano> [ano ...]
"""
from __future__ import annotations

import json
import sys
from datetime import date, timedelta
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from baixar import pegar  # noqa: E402
from espn import URL, resumir  # noqa: E402

RAIZ = AQUI.parent.parent

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    liga, slug, anos = sys.argv[1], sys.argv[2], [int(a) for a in sys.argv[3:]]
    cache = RAIZ / "data" / "cache" / "espn-sulamerica" / liga
    pasta = RAIZ / "data" / "coleta" / slug / "espn"
    pasta.mkdir(parents=True, exist_ok=True)
    for ano in anos:
        jogos, vistos, dia = [], set(), date(ano, 1, 1)
        while dia <= date(ano, 12, 31):
            bruto = pegar(URL.format(liga=liga, dia=dia.strftime("%Y%m%d")), cache / f"{dia:%Y%m%d}.json", espera=0.25)
            for ev in json.loads(bruto or b"{}").get("events", []):
                if ev["id"] not in vistos:
                    vistos.add(ev["id"])
                    jogos.append({**resumir(ev), "temporada": ev.get("season", {}).get("year")})   # ano da edição na ESPN
            dia += timedelta(days=1)
        jogos.sort(key=lambda j: j["data_hora"])
        (pasta / f"{liga}_{ano}.json").write_text(json.dumps(jogos, ensure_ascii=False, indent=0), encoding="utf-8")
        print(ano, len(jogos), "jogos", flush=True)
