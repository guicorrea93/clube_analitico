"""Futebol Nacional: baixa a página de cada edição do Campeonato Paulista (códigos em fn_resumo.json) e lê os jogos
(fase, data, mandante, placar, visitante, nota) e o cabeçalho (total de jogos, fonte, artilheiro).
Grava revisao/QS/fn_jogos.json. Uso: python -I revisao/QS/fn_jogos.py [--so-ler]"""
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from baixar import baixar  # noqa: E402

AQUI = Path(__file__).resolve().parent
URL = "https://futebolnacional.com.br/siteapp/controller.jsp?module=championship&code={code}&lang=pt-br"


def conserta(s: str) -> str:
    """A página mistura UTF-8 (cabeçalho) e Latin-1 (jogos): o texto é lido como Latin-1 e cada trecho volta a UTF-8 quando dá."""
    try:
        return s.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return s


def limpo(s: str) -> str:
    return conserta(re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip())


def ler(t: str) -> dict:
    cab = limpo(t.split('<table class="table table-striped break">')[0])
    info = {}
    for chave, rx in [("jogos_registrados", r"Total de Jogos Registrados: (\d+)"),
                      ("jogos_com_resultado", r"Total de Jogos com Resultados: (\d+)"),
                      ("gols", r"Núm\. de Gols: (\d+)"), ("completude", r"Completude: ([\d.]+)%"),
                      ("artilheiro", r"Artilheiro\(s\) (.*?) Observações"), ("observacoes", r"Observações (.*?)$")]:
        m = re.search(rx, cab)
        info[chave] = m[1] if m else None
    jogos = []
    fase = data = None
    for pedaco in re.split(r"(?=<thead>|<tr>)", t):
        if pedaco.startswith("<thead>"):
            x = limpo(pedaco)
            if re.match(r"\d\d/\d\d/\d{4}", x):
                data = x[:10]
            elif x and "Col." not in x and "Equipe" not in x:
                fase, data = x, None
            continue
        if 'class="td-item"><b>' in pedaco and "matchdetails" in pedaco:
            tds = re.split(r"<td[^>]*>", pedaco)
            cel = [limpo(c) for c in tds]
            # [.., mandante, img, placar, img, visitante, ...]
            try:
                i = next(k for k, c in enumerate(tds) if c.startswith("<b>"))
            except StopIteration:
                continue
            code = re.search(r"matchdetails&code=([0-9A-F]+)", pedaco)
            jogos.append({"fase": fase, "data": data, "mandante": cel[i - 2], "placar": cel[i],
                          "visitante": cel[i + 2], "code": code[1] if code else None, "nota": ""})
        elif pedaco.startswith("<tr><td><td colspan=\"7\">") and jogos:
            jogos[-1]["nota"] = limpo(pedaco)
    info["jogos"] = jogos
    return info


def main():
    resumo = [r for r in json.loads((AQUI / "fn_resumo.json").read_text(encoding="utf-8"))
              if r["competicao"] == "Campeonato Paulista" and r["code"]]
    saida = {}
    for r in resumo:
        a, s = baixar(URL.format(code=r["code"]))
        if not a:
            print("falhou", r["temporada"], s)
            continue
        t = a.read_bytes().decode("latin-1")
        info = ler(t)
        info["url"] = URL.format(code=r["code"])
        saida[r["temporada"]] = info
        print(r["temporada"], s, len(info["jogos"]), info["jogos_registrados"], flush=True)
    (AQUI / "fn_jogos.json").write_text(json.dumps(saida, ensure_ascii=False, indent=0), encoding="utf-8")


if __name__ == "__main__":
    main()
