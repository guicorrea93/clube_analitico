"""Artilheiros oficiais da Série A, de 1937 a 2025 (pedido do agente 1; revisão SA-019 a SA-023).

Fonte: Wikipédia em inglês, "List of Campeonato Brasileiro Série A top scorers", seção "Scoring by season" (uma tabela
por competição: Copa dos Campeões Estaduais 1937, Taça Brasil 1959-1968, Torneio Roberto Gomes Pedrosa 1967-1970 e
Série A 1971 em diante). Conferida com a lista da Wikipédia em português ("Lista de artilheiros do Campeonato Brasileiro
de Futebol"), que fica em data/coleta/bra-serie-a-artilheiros/wikipedia/ junto com a outra.

O clube é o nome do futebol.db (aberto só para leitura), entre os clubes daquela edição. Jogador que marcou por dois
clubes (Fred em 2016) vira uma linha só, com o total e o clube em que fez mais gols.

Saída: data/coleta/bra-serie-a-artilheiros/artilheiros.csv (temporada,jogador,clube,gols,fonte), com a temporada como a
chave da edição no banco ("1967_robertao", "1967_taca_brasil", "2019").

Uso: python coleta/bra-serie-a-artilheiros/montar.py
"""
from __future__ import annotations

import csv
import re
import sqlite3
import sys
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
PASTA = RAIZ / "data" / "coleta" / "bra-serie-a-artilheiros"
FONTE = "Wikipédia (en), List of Campeonato Brasileiro Série A top scorers"

# seção da página -> como vira a chave da edição no banco
SECOES = {"Copa dos Campeões Estaduais": "{a}", "Taça Brasil": "{a}_taca_brasil", "Roberto Gomes Pedrosa": "{a}_robertao",
          "Série A": "{a}"}
# nome de jogo pedido pelo agente 1 e pela revisão (SA-021, SA-023), quando a fonte escreve outro
NOME_DE_JOGO = {"Josiel da Rocha": "Josiel", "Fernandao": "Fernandão", "Andre Felipe": "André Felipe",
                "Luciano da Rocha Neves": "Luciano", "Alerrandro Barra Mansa Realino de Souza": "Alerrandro"}


def _texto(celula: str) -> str:
    """'[[Dadá Maravilha|Dario]] (2)' -> 'Dario'; tira rowspan, negrito, refs e o número de títulos entre parênteses."""
    c = re.sub(r"^\s*(?:rowspan\s*=\s*\"?\d+\"?\s*\|)", "", celula.strip())
    c = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>|\{\{[^}]*\}\}", "", c)
    m = re.search(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", c)
    c = m.group(1) if m else c
    return re.sub(r"\s*\(\d+\)\s*$", "", c.replace("'''", "")).strip()


def _rowspan(celula: str) -> int:
    m = re.match(r"^\s*rowspan\s*=\s*\"?(\d+)\"?\s*\|", celula.strip())
    return int(m.group(1)) if m else 1


def ler_wikipedia() -> list[dict]:
    t = (PASTA / "wikipedia" / "en_artilheiros.txt").read_text(encoding="utf-8")
    ini, fim = t.index("==Scoring by season=="), t.index("==Top Scorer by player==")
    saida = []
    for m in re.finditer(r"^===([^=]+)===\s*$(.*?)(?=^===|\Z)", t[ini:fim], re.M | re.S):
        secao, tabela = m.group(1).strip(), m.group(2)
        modelo = SECOES.get(secao)
        if not modelo:
            continue
        ano, resta = None, {"jogador": 0, "clube": 0, "gols": 0}
        atual = {"jogador": None, "clube": None, "gols": None}
        for linha in tabela.split("\n|-")[1:]:
            celulas = [c for c in re.split(r"\n(?=[|!])", linha.strip()) if c.strip() and not c.startswith("|}")]
            dados = []
            for c in celulas:
                if c.startswith("!"):
                    y = re.search(r"\|(\d{4})\]\]", c) or re.search(r"\b(\d{4})\b", c)
                    if y:
                        ano = y.group(1)
                else:
                    dados.append(c[1:])
            if not dados:
                continue
            # as colunas sem rowspan em curso recebem as células da linha, na ordem
            livres = [k for k in ("jogador", "clube", "gols") if resta[k] == 0]
            for k in ("jogador", "clube", "gols"):
                if resta[k] > 0:
                    resta[k] -= 1
            for k, c in zip(livres, dados):
                atual[k] = c
                resta[k] = _rowspan(c) - 1
            gols = re.search(r"\d+", _texto(atual["gols"] or ""))
            clube_txt = atual["clube"] or ""
            gols_clube = re.search(r"\((\d+)\)\s*$", clube_txt.strip())
            # só 1967 e 1968 têm as duas competições no banco ("1967_taca_brasil", "1967_robertao"); as outras, só o ano
            chave = modelo.format(a=ano) if ano in ("1967", "1968") else ano
            saida.append({"temporada": chave, "jogador": _texto(atual["jogador"] or ""), "clube_fonte": _texto(clube_txt),
                          "gols": int(gols.group()) if gols else None, "gols_clube": int(gols_clube.group(1)) if gols_clube else None})
    return saida


def _chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"\b(fc|ec|sc|cr|ac|se|fr|clube|club|de|do|da|futebol|regatas|esporte|esportiva|atletico|sport)\b|[^a-z0-9 ]", " ", s)


def clubes_da_edicao(con) -> dict[str, list[tuple[str, set[str]]]]:
    """Chave da edição -> [(nome no banco, nomes conhecidos)] dos clubes que jogaram a edição."""
    saida: dict[str, list] = {}
    for chave, cid, nome in con.execute("""SELECT e.chave, c.clube_id, c.nome FROM classificacao_final f JOIN edicao e USING (edicao_id)
                                           JOIN competicao k USING (competicao_id) JOIN clube c USING (clube_id)
                                           WHERE k.slug = 'bra-serie-a'"""):
        outros = {n for (n,) in con.execute("SELECT nome FROM clube_nome WHERE clube_id = ?", (cid,))}
        saida.setdefault(chave, []).append((nome, {nome, *outros}))
    return saida


# nome do clube na Wikipédia em inglês -> nome do banco, quando a semelhança de texto não basta
CLUBE_EN = {"Atlético Mineiro": "Atlético-MG", "Atlético Paranaense": "Athletico-PR", "Athletico Paranaense": "Athletico-PR",
            "Sport Recife": "Sport", "Vasco da Gama": "Vasco", "Bahia": "Bahia", "Goiás": "Goiás", "Atlético Goianiense": "Atlético-GO"}


def casar_clube(txt: str, cands: list[tuple[str, set[str]]]) -> str | None:
    alvo = CLUBE_EN.get(txt, txt)
    for nome, nomes in cands:
        if alvo in nomes:
            return nome
    nota = lambda nomes: max(SequenceMatcher(None, _chave(alvo).split() and " ".join(_chave(alvo).split()),
                                             " ".join(_chave(n).split())).ratio() for n in nomes)
    melhor = sorted(((nota(nomes), nome) for nome, nomes in cands), reverse=True)
    return melhor[0][1] if melhor and melhor[0][0] >= 0.75 and (len(melhor) == 1 or melhor[1][0] < melhor[0][0]) else None


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    con = sqlite3.connect(f"file:{RAIZ / 'db' / 'futebol.db'}?mode=ro", uri=True)
    edicoes = {k for (k,) in con.execute("SELECT e.chave FROM edicao e JOIN competicao k USING (competicao_id) WHERE k.slug = 'bra-serie-a'")}
    cands = clubes_da_edicao(con)
    linhas = ler_wikipedia()
    # o mesmo jogador por dois clubes na mesma edição (Fred, 2016): uma linha, com o clube em que fez mais gols
    juntas: dict[tuple, dict] = {}
    for x in linhas:
        k = (x["temporada"], x["jogador"])
        if k in juntas:
            if (x["gols_clube"] or 0) > (juntas[k]["gols_clube"] or 0):
                juntas[k]["clube_fonte"], juntas[k]["gols_clube"] = x["clube_fonte"], x["gols_clube"]
            juntas[k]["dois_clubes"] = True
        else:
            juntas[k] = dict(x)
    saida, problemas = [], []
    for (temporada, jogador), x in juntas.items():
        if temporada not in edicoes:
            problemas.append(f"{temporada}: edição que não está no banco ({jogador})")
            continue
        clube = casar_clube(x["clube_fonte"], cands.get(temporada, []))
        if not clube:
            problemas.append(f"{temporada}: clube '{x['clube_fonte']}' de {jogador} não casou com o banco")
        fonte = FONTE + ("; gols somados de dois clubes" if x.get("dois_clubes") else "")
        saida.append([temporada, NOME_DE_JOGO.get(jogador, jogador), clube or x["clube_fonte"], x["gols"], fonte])
    with open(PASTA / "artilheiros.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["temporada", "jogador", "clube", "gols", "fonte"])
        w.writerows(saida)
    faltam = sorted(edicoes - {s[0] for s in saida})
    print(len(saida), "linhas;", len({s[0] for s in saida}), "edições de", len(edicoes), "; sem artilheiro:", faltam)
    for p in problemas:
        print("  !", p)


if __name__ == "__main__":
    main()
