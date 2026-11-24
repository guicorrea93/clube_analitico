"""Baixa do portal de dados oficial da K League (portal.kleague.com, acesso de convidado) os jogos da 1ª divisão sul-coreana
de 1983 a 2025: o calendário de cada mês e o boletim de cada jogo (autores dos gols com minuto, assistência, gol contra,
cartões, público, estádio, árbitros).

- Calendário (até 2012): POST /view/schedule/list.do (selectYear, selectMonth); cada jogo vem numa chamada
  fn_detailPopup('ano', 'meetSeq', 'nome da competição', 'gameId', 'leagueId', 'terminado').
  Fica em data/coleta/kor-1/portal/calendario_<ano>.json (todas as competições do mês; a escolha da 1ª divisão é feita
  na leitura). De 2013 em diante o calendário esconde jogos nos dias cheios: a lista vem do site oficial (lista_oficial).
- Boletim: POST /common/result/result0051popup.do; a página traz o jogo em JSON (basicMatchInfoJson, jsonResultData).
  Guardado comprimido em data/cache/kleague-asia/jogos/<ano>_<meetSeq>_<gameId>.html.gz (fora do git).

Uso: python coleta/kor-1/baixar_portal.py [ano ...] [--sem-jogos] [--reverso]
"""
from __future__ import annotations

import gzip
import http.cookiejar
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
RAIZ = AQUI.parent.parent
CACHE = RAIZ / "data" / "cache" / "kleague-asia"
PASTA = RAIZ / "data" / "coleta" / "kor-1" / "portal"
BASE = "https://portal.kleague.com"
CONVIDADO = BASE + "/user/loginById.do?portalGuest=rstNE9zxjdkUC9kbUA08XQ=="
ESPERA = 1.0

_op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
_op.addheaders = [("User-Agent", "Mozilla/5.0 (clube-analitico; projeto pessoal de estatisticas)")]
_ultimo = [0.0]
_logado = [False]


def _post(url: str, dados: dict) -> bytes:
    if not _logado[0]:
        _op.open(CONVIDADO, timeout=60).read()
        _logado[0] = True
    corpo = urllib.parse.urlencode(dados).encode()
    for t in range(6):
        falta = ESPERA - (time.time() - _ultimo[0])
        if falta > 0:
            time.sleep(falta)
        _ultimo[0] = time.time()
        try:
            with _op.open(url, data=corpo, timeout=90) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if t == 5:
                raise
            time.sleep(max(int(e.headers.get("Retry-After") or 0), 10 * (t + 1)) if e.code == 429 else 5 * (t + 1))
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            if t == 5:
                raise
            time.sleep(5 * (t + 1))
    raise RuntimeError(url)


def calendario(ano: int) -> list[dict]:
    jogos, vistos = [], set()
    for mes in range(1, 13):
        arq = CACHE / "calendario" / f"{ano}_{mes:02d}.html.gz"
        if arq.exists():
            t = gzip.decompress(arq.read_bytes()).decode("utf-8", "ignore")
        else:
            b = _post(BASE + "/view/schedule/list.do", {"selectYear": str(ano), "selectMonth": str(mes)})
            t = b.decode("utf-8", "ignore")
            if "fn_detailPopup" not in t:   # a sessão caiu: entra de novo
                _logado[0] = False
                b = _post(BASE + "/view/schedule/list.do", {"selectYear": str(ano), "selectMonth": str(mes)})
                t = b.decode("utf-8", "ignore")
            arq.parent.mkdir(parents=True, exist_ok=True)
            arq.write_bytes(gzip.compress(b))
        for args in re.findall(r"fn_detailPopup\(([^)]*)\)", t)[1:]:   # a 1ª é a definição da função
            a = [x.strip().strip("'\"") for x in args.split(",")]
            if len(a) < 6 or not a[3].isdigit():
                continue
            chave = (a[0], a[1], a[3])
            if chave in vistos:
                continue
            vistos.add(chave)
            jogos.append({"ano": a[0], "meet_seq": a[1], "competicao": a[2], "game_id": a[3], "league_id": a[4],
                          "terminado": a[5], "mes": mes})
    return jogos


def lista_oficial(ano: int) -> list[dict]:
    """De 2013 em diante o calendário do portal esconde jogos nos dias cheios (K League 2, base...): a lista vem do site
    oficial (www.kleague.com, /getScheduleList.do, leagueId 1 = K League 1, com a repescagem), com o mesmo meetSeq e
    gameId do portal."""
    import json as _json
    jogos = []
    for mes in range(1, 13):
        arq = CACHE / "lista_oficial" / f"{ano}_{mes:02d}.json.gz"
        if arq.exists():
            b = gzip.decompress(arq.read_bytes())
        else:
            falta = ESPERA - (time.time() - _ultimo[0])
            if falta > 0:
                time.sleep(falta)
            _ultimo[0] = time.time()
            req = urllib.request.Request("https://www.kleague.com/getScheduleList.do",
                                         data=_json.dumps({"year": str(ano), "month": f"{mes:02d}", "leagueId": "1"}).encode(),
                                         headers={"User-Agent": "Mozilla/5.0 (clube-analitico)", "Content-Type": "application/json; charset=utf-8"})
            b = urllib.request.urlopen(req, timeout=60).read()
            arq.parent.mkdir(parents=True, exist_ok=True)
            arq.write_bytes(gzip.compress(b))
        for x in _json.loads(b)["data"]["scheduleList"]:
            jogos.append({"ano": str(x["year"]), "meet_seq": str(x["meetSeq"]), "competicao": x["meetName"],
                          "game_id": str(x["gameId"]), "league_id": "2", "terminado": "1" if x.get("endYn") == "Y" else "0",
                          "mes": mes, "rodada": x.get("roundId"), "fase_oficial": x.get("codeName")})
    return jogos


def boletim(j: dict) -> Path:
    arq = CACHE / "jogos" / f"{j['ano']}_{j['meet_seq']}_{j['game_id']}.html.gz"
    if not arq.exists():
        dados = {"workingTag": "L", "iptMeetYear": j["ano"], "iptMeetSeq": j["meet_seq"], "iptGameid": j["game_id"],
                 "iptMeetName": j["competicao"], "singleIdx": j["game_id"]}
        b = _post(BASE + "/common/result/result0051popup.do", dados)
        if b"basicMatchInfoJson" not in b:
            _logado[0] = False
            b = _post(BASE + "/common/result/result0051popup.do", dados)
        if b"basicMatchInfoJson" not in b:
            raise RuntimeError(f"boletim sem dados: {j}")
        arq.parent.mkdir(parents=True, exist_ok=True)
        arq.write_bytes(gzip.compress(b))
    return arq


def primeira_divisao(j: dict) -> bool:
    """A 1ª divisão: a liga de cada ano e os jogos do título (playoff, final); fora a copa da liga, a K League 2, a
    repescagem contra a 2ª divisão e os torneios de base. A lista de competições de cada ano está no relatório."""
    from competicoes import eh_primeira
    return eh_primeira(j)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    PASTA.mkdir(parents=True, exist_ok=True)
    anos = [int(a) for a in args] or list(range(1983, 2026))
    for ano in (reversed(anos) if "--reverso" in sys.argv else anos):
        js = calendario(ano) if ano < 2013 else lista_oficial(ano)
        (PASTA / f"calendario_{ano}.json").write_text(json.dumps(js, ensure_ascii=False, indent=0), encoding="utf-8")
        print(ano, len(js), "jogos no calendário", flush=True)
        if "--sem-jogos" in sys.argv:
            continue
        sel = [j for j in js if primeira_divisao(j)]
        for j in (reversed(sel) if "--reverso" in sys.argv else sel):
            boletim(j)
        print(ano, len(sel), "boletins ok", flush=True)
