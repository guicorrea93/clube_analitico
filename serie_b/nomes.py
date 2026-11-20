"""Casa os nomes de clube da ESPN e da Wikipédia com os clubes identificados na RSSSF (serie_b/clubes.py).

"América Mineiro" -> América-MG, "Red Bull Bragantino" -> Bragantino, "Atlético Goianiense" -> Atlético-GO.
Procura primeiro entre os clubes daquele ano na RSSSF e depois entre todos; palavras como "Mineiro",
"Goianiense" ou a sigla do estado no fim do nome escolhem entre homônimos. Clube que nunca aparece na
RSSSF (anos em que a página parou no meio) entra por NOVOS.

Uso: python serie_b/nomes.py     (lista os nomes externos que não casaram)
"""
from __future__ import annotations

import json
import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import clubes  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
DICA_UF = {"mineiro": "MG", "goianiense": "GO", "paranaense": "PR", "natal": "RN", "pelotas": "RS", "baiano": "BA",
           "pernambucano": "PE", "alagoano": "AL", "cearense": "CE", "potiguar": "RN", "capixaba": "ES", "riopretano": "SP"}
# nome externo (sem acento) -> nome-base da RSSSF (e estado, quando precisa)
EXTERNO = {
    "red bull bragantino": "bragantino", "rb bragantino": "bragantino", "gremio novorizontino": "novorizontino",
    "operario ferroviario": ("operario", "PR"), "op ferroviario": ("operario", "PR"), "america de natal": ("america", "RN"),
    "vasco da gama": "vasco", "gremio barueri": "barueri", "gremio prudente": "barueri", "sport recife": "sport",
    "botafogo sp": ("botafogo", "SP"), "brasil de pelotas": ("brasil de pelotas", "RS"), "athletico pr": ("atletico", "PR"),
    "atletico pr": ("atletico", "PR"), "atletico mg": ("atletico", "MG"), "atletico go": ("atletico", "GO"),
    "guarani sp": ("guarani", "SP"), "america mg": ("america", "MG"), "america rn": ("america", "RN"), "boa": "boa esporte",
    "luverdense ec": "luverdense", "ponte preta sp": "ponte preta", "sao bento sp": "sao bento", "abc fc": "abc",
    "cuiaba ec": "cuiaba", "paysandu sc": "paysandu", "vila nova fc": ("vila nova", "GO"), "vila nova go": ("vila nova", "GO"),
    "vila nova": ("vila nova", "GO"), "duque de caxias fc": "duque de caxias", "crb al": "crb", "csa al": "csa",
    "esporte clube santo andre": "santo andre",
    "ge brasil": ("brasil de pelotas", "RS"),
    # nomes antigos do ogol
    "aa colatina": "colatina", "colatina se": "colatina", "ad guara": "guara", "cr guara": "guara", "fast clube": "fast club",
    "auto esporte": ("auto esporte", "PB"), "comercial": ("comercial", "SP"),   # o ogol põe o estado só no outro (PI, MS)
    "ferroviario do cabo": ("ferroviario", "PE"), "inter sm": "inter de santa maria", "ituiutaba": "boa esporte",
    "maguary": "maguari", "maguary ce": "maguari", "parnahyba": "parnaiba", "rio branco de andradas": ("rio branco", "MG"),
    "ferroviario recife": ("ferroviario", "PE"), "ferroviario": ("ferroviario", "CE"),   # ogol: o "Ferroviário" sem cidade é o de Fortaleza
    "ituiutaba esporte clube": "boa esporte",   # o Ituiutaba virou Boa Esporte em 2011 (mesmo clube)
    "santa cruz": ("santa cruz", "PE"),          # desde 2010 só o do Recife jogou a Série B
}
# nome externo que depende do ano (ano, nome sem acento) -> nome-base da RSSSF
EXTERNO_ANO = {(2011, "guaratingueta"): "americana", (2010, "americana"): "guaratingueta"}   # o ogol usa o nome de 2011 em 2010   # em 2011 o Guaratinguetá jogou em Americana, com esse nome
# clubes que nunca aparecem nas páginas da RSSSF (temporadas em que a página parou no meio): nome externo -> (nome, estado)
NOVOS: dict[str, tuple[str, str]] = {"nacional pb": ("Nacional-PB", "PB")}   # Nacional de Patos (1989), achado pela tabela de grupo


@lru_cache(maxsize=1)
def _clubes_por_ano() -> tuple[dict, dict]:
    """ano -> {nome de exibição}, e nome de exibição -> (uf, clube_id), a partir da RSSSF."""
    por_ano = clubes.resolver_todos()
    can = clubes.canonicos(por_ano)
    do_ano, todos = {}, {}
    for (a, n), c in can.items():
        do_ano.setdefault(a, set()).add(c["clube"])
        todos[c["clube"]] = (c["uf"], c["clube_id"])
    return do_ano, todos


def _chave(exibicao: str, uf: str | None) -> str:
    base, uf_nome = clubes.separar_estado(exibicao)
    return clubes.chave_base(base, uf_nome or uf)


def casar(nome: str, ano: int) -> str | None:
    """Nome de exibição do clube (o mesmo da RSSSF), ou None."""
    do_ano, todos = _clubes_por_ano()
    n = clubes.norm(nome)
    if n in NOVOS:
        return NOVOS[n][0]
    alvo, uf = EXTERNO_ANO.get((ano, n)) or EXTERNO.get(n, n), None
    if isinstance(alvo, tuple):
        alvo, uf = alvo
    palavras = alvo.split()
    if palavras and palavras[-1].upper() in clubes.UFS and len(palavras) > 1:   # "guarani sp"
        uf, palavras = uf or palavras[-1].upper(), palavras[:-1]
    for p in list(palavras):
        if p in DICA_UF and len(palavras) > 1:   # "america mineiro"
            uf = uf or DICA_UF[p]
            palavras.remove(p)
    nucleo = clubes.ALIAS.get(" ".join(palavras), " ".join(palavras))
    for grupo in (do_ano.get(ano, set()), set(todos)):
        cands = [c for c in grupo if _chave(c, todos[c][0]) == nucleo and (not uf or todos[c][0] == uf)]
        if len(cands) == 1:
            return cands[0]
        cands = [c for c in grupo if (not uf or todos[c][0] == uf) and
                 ((k := _chave(c, todos[c][0])) == nucleo or nucleo.startswith(k + " ") or k.startswith(nucleo + " "))]
        if len(cands) == 1:
            return cands[0]
    return None


def externos() -> dict[int, set[str]]:
    """Nomes que aparecem na ESPN e na Wikipédia, por ano."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import wiki
    saida: dict[int, set[str]] = {}
    for f in sorted((RAIZ / "data" / "serie_b" / "espn").glob("serie_b_*.json")):
        ano = int(f.stem[-4:])
        for j in json.loads(f.read_text(encoding="utf-8")):
            saida.setdefault(ano, set()).update((j["mandante"], j["visitante"]))
    for f in sorted((RAIZ / "data" / "serie_b" / "ogol").glob("serie_b_*.json")):
        ano = int(f.stem[-4:])
        for j in json.loads(f.read_text(encoding="utf-8")):
            saida.setdefault(ano, set()).update((j["mandante"], j["visitante"]))
    for ano in range(1971, 2026):
        for r in wiki.tabela(ano):
            saida.setdefault(ano, set()).add(r["nome"])
        for m, v, _, _ in wiki.resultados(ano):
            saida.setdefault(ano, set()).update((m, v))
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    faltam = {}
    for ano, ns in sorted(externos().items()):
        for n in sorted(ns):
            if casar(n, ano) is None:
                faltam.setdefault(n, []).append(ano)
    print(len(faltam), "nomes sem casar")
    for n, anos in sorted(faltam.items()):
        print(f"   {n:32} {anos}")
