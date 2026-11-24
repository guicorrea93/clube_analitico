"""Lê a linha do tempo dos jogos de 2013 em diante baixada do site oficial da K League (baixar_oficial.py), em coreano e
em inglês, para:
- conferir o placar e os gols do boletim do portal (homeGoal/awayGoal, eventos 득점 gol e 자책골 gol contra);
- dar o nome em inglês dos jogadores (o mesmo código de jogador, playerId, nas duas línguas), que é o único jeito de
  escrever direito os estrangeiros (no portal eles vêm em hangul: "데얀" é o montenegrino Dejan Damjanović).

O minuto do site é contado do começo de cada tempo (timeMin 0 a 45+): 1º tempo = timeMin + 1 até 45 e depois acréscimo;
2º tempo = 45 + timeMin + 1 até 90 e depois acréscimo. O "time" do resumo de gols (homeScorer) é 45 × (tempo - 1) +
timeMin, um a menos que o minuto de costume; a conferência compara pelo mesmo critério.

Uso como biblioteca: jogo(ano, meet, game) -> dict ou None; nomes() -> {playerId: (nome em coreano, nome em inglês)}.
"""
from __future__ import annotations

import gzip
import json
from functools import lru_cache
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CACHE = AQUI.parent.parent / "data" / "cache" / "kleague-asia" / "oficial"
TEMPOS = ("firstHalf", "secondHalf", "EfirstHalf", "EsecondHalf")


def _ler(ano, meet, game, lingua) -> dict | None:
    arq = CACHE / f"{ano}_{meet}_{game}_{lingua}.json.gz"
    if not arq.exists():
        return None
    return json.loads(gzip.decompress(arq.read_bytes())).get("data")


def jogo(ano, meet, game) -> dict | None:
    ko = _ler(ano, meet, game, "ko")
    if not ko:
        return None
    gols = []
    for t in TEMPOS:
        for e in ko.get(t) or []:
            if e["eventName"] in ("득점", "자책골"):
                gols.append({"time": e["teamId"], "lado": "m" if e["homeOrAway"] == "HOME" else "v", "jogador": e["playerName"],
                             "player_id": e["playerId"], "tempo": e["halfType"], "min": e["timeMin"],
                             "contra": e["eventName"] == "자책골"})
    return {"gm": ko.get("homeGoal"), "gv": ko.get("awayGoal"), "situacao": ko.get("gameStatus"), "gols": gols}


@lru_cache(maxsize=1)
def nomes() -> dict[str, tuple[str, str]]:
    ko_n, en_n = {}, {}
    for arq in sorted(CACHE.glob("*.json.gz")):
        d = json.loads(gzip.decompress(arq.read_bytes())).get("data") or {}
        alvo = en_n if arq.name.endswith("_en.json.gz") else ko_n
        for t in TEMPOS:
            for e in d.get(t) or []:
                for pid, nome in ((e.get("playerId"), e.get("playerName")), (e.get("playerId2"), e.get("playerName2"))):
                    if pid and nome:
                        alvo.setdefault(str(pid), nome.strip())
    return {pid: (ko_n.get(pid, ""), en_n.get(pid, "")) for pid in set(ko_n) | set(en_n)}
