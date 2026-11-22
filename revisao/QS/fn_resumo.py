"""Futebol Nacional (futebolnacional.com.br): lê o 'Resumo de Competições | São Paulo' (todas as edições do Campeonato
Paulista, com o código de cada uma, campeão, vice e artilheiro) e grava revisao/QS/fn_resumo.json.
Uso: python -I revisao/QS/fn_resumo.py"""
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from baixar import baixar  # noqa: E402

URL = ("https://futebolnacional.com.br/siteapp/controller.jsp?module=summary&lang=pt-br&name="
       "A27437D2CE0894275C03A3BAEDA49F41A9C63F1F39F7FF7572315985555EFA80&state=SP&country=BR")


def limpo(s: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def main():
    a, _ = baixar(URL)
    t = a.read_text(encoding="utf-8", errors="replace")
    # só a primeira tabela (Campeonato Paulista); as seguintes são outras competições de SP
    blocos = re.split(r"<h5>", t)
    saida = []
    for bl in blocos[1:]:
        comp = limpo(bl.split("</h5>")[0])
        for linha in re.split(r"<tr>", bl)[1:]:
            tds = re.split(r"<td[^>]*>", linha)[1:]
            if len(tds) < 6:
                continue
            m = re.search(r"module=championship&code=([0-9A-F]+)", tds[1])
            status = re.search(r'title="([^"]*)"', tds[0])
            saida.append({"competicao": comp, "temporada": limpo(tds[1]), "code": m[1] if m else None,
                          "campeao": limpo(tds[2]), "vice": limpo(tds[3]), "inicio": limpo(tds[4]),
                          "artilheiro": limpo(tds[5]), "status": status[1] if status else ""})
    Path(__file__).with_name("fn_resumo.json").write_text(json.dumps(saida, ensure_ascii=False, indent=1), encoding="utf-8")
    comps = {}
    for r in saida:
        comps[r["competicao"]] = comps.get(r["competicao"], 0) + 1
    print(comps)


if __name__ == "__main__":
    main()
