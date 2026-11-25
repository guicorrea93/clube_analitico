"""Identidade dos clubes do Campeonato Goiano (mesmo método do Paulista, coleta/bra-sp-1/clubes_sp1.py; clube já
nomeado em outra coleta usa o mesmo nome, pelo cadastro comum data/coleta/comum/clubes_ogol.json).

Cada clube é o código dele no ogol (o mesmo em todas as edições, mesmo quando o clube muda de nome).
Da ficha do ogol saem o nome curto, a cidade e a UF. O nome de exibição é:
1. o `clube.nome` do db/futebol.db, quando o clube já está lá (mesma UF e um dos nomes de `clube_nome` igual);
2. senão, o nome curto do ogol, com "-UF" só quando outro clube tem o mesmo nome.
Exceções decididas à mão ficam em MANUAL, com o motivo.

Uso: python coleta/bra-go-1/clubes_go1.py     (lista os casamentos com o banco e os clubes novos)
"""
from __future__ import annotations

import json
import re
import sqlite3
import sys
import unicodedata
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(AQUI.parent / "comum"))
import registro  # noqa: E402
from edicoes import PASTA_DADOS, RAIZ  # noqa: E402

UFS = set("AC AL AM AP BA CE DF ES GO MA MG MS MT PA PB PE PI PR RJ RN RO RR RS SC SE SP TO".split())
GENERICOS = r"(?:ec|fc|sc|ac|aa|ad|cs|ca|se|ge|cr|ae|aec|ser|sad|saf|esporte clube|futebol clube|atletico clube|clube|club|ltda)"

# código do ogol -> nome de exibição no futebol.db (quando o nome do ogol não basta para achar), com o motivo
MANUAL_DB: dict[str, tuple[str, str]] = {
    "3333": ("J.Malucelli", "o ogol escreve 'JMalucelli'; é o J. Malucelli do banco (Série A 2000)"),
    "24836": ("Novorizontino", "Grêmio Novorizontino (2010-); o banco separou o GE Novorizontino (1973-1999) em 20/11/2026"),
}
# código do ogol -> nome de exibição de clube novo (quando o nome curto do ogol não serve ou confunde), com o motivo
MANUAL_NOVO: dict[str, tuple[str, str]] = {
    "68358": ("Corinthians Prudente", "EC Corinthians de Presidente Prudente (1996): não é o Corinthians paulistano do banco"),
    "45210": ("Maringá", "Maringá FC fundado em 2010 (Copa do Brasil 2025): não é o GE Maringá do banco"),
    "241210": ("Maringá FC 1995", "Maringá FC fundado em 1995 (Copa do Brasil 1997): outro clube, nome como no ogol"),
    "60858": ("GE Novorizontino", "Grêmio Esportivo Novorizontino (1973-1999, campeão de 1994): outro clube; o 'Novorizontino' "
                                  "do banco fica com o Grêmio Novorizontino, fundado em 2010 (decisão do Guilherme, 20/11/2026)"),
    "20122": ("Linhares EC", "dois clubes de Linhares-ES: o EC (anos 1990) e o FC (anos 2000); o sufixo já distingue"),
    "9783": ("Linhares FC", "dois clubes de Linhares-ES: o EC (anos 1990) e o FC (anos 2000); o sufixo já distingue"),
}
# grafias do mesmo clube (chave -> chave), como em serie_b/clubes.py
ALIAS = {
    "athletico": "atletico", "athletico paranaense": "atletico", "atletico paranaense": "atletico", "atletico goianiense": "atletico",
    "atletico mineiro": "atletico", "america mineiro": "america", "vasco da gama": "vasco", "sport recife": "sport",
    "gremio barueri": "barueri", "red bull bragantino": "bragantino", "rb bragantino": "bragantino",
    "operario ferroviario": "operario", "brasil de pelotas": "brasil", "inter de limeira": "internacional",
    "inter de santa maria": "internacional", "boa": "boa esporte", "ituiutaba": "boa esporte", "moto clube": "moto club",
    "fast clube": "fast", "fast club": "fast", "gremio novorizontino": "novorizontino", "brasilia ec": "brasilia",
}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def separar_uf(nome: str) -> tuple[str, str | None]:
    """'América-RN' -> ('América', 'RN'); 'Vitória (ES)' -> ('Vitória', 'ES'); 'Botafogo/PB' -> ('Botafogo', 'PB')."""
    m = re.match(r"^(.*?)(?:\s*[-/]\s*|\s*\(|\s+)([A-Z]{2})\)?$", (nome or "").strip())
    if m and m.group(2) in UFS:
        return m.group(1).strip(), m.group(2)
    return (nome or "").strip(), None


def chave(nome: str) -> str:
    """Nome comparável: sem acento, sem UF, sem siglas genéricas ("EC", "FC"), com as grafias do mesmo clube juntas."""
    base, _ = separar_uf(nome)
    n = norm(base)
    n = re.sub(rf"^{GENERICOS}\s+(?=\w{{3}})", "", n)
    n = re.sub(rf"\s+{GENERICOS}$", "", n)
    return ALIAS.get(n, n)


@lru_cache(maxsize=1)
def banco() -> dict[str, dict]:
    """Clubes do futebol.db (só leitura): nome de exibição -> {uf, cidade, chaves}."""
    con = sqlite3.connect(f"file:{RAIZ / 'db' / 'futebol.db'}?mode=ro", uri=True)
    saida: dict[str, dict] = {}
    ids = {}
    for cid, nome, uf, cidade in con.execute("SELECT clube_id, nome, regiao, cidade FROM clube"):
        saida[nome] = {"uf": uf, "cidade": cidade, "chaves": {chave(nome)}}
        ids[cid] = nome
    for cid, nome in con.execute("SELECT clube_id, nome FROM clube_nome"):
        if cid in ids:
            saida[ids[cid]]["chaves"].add(chave(nome))
    con.close()
    return saida


@lru_cache(maxsize=1)
def fichas() -> dict[str, dict]:
    """Fichas do ogol (data/coleta/bra-go-1/ogol/clubes.json), com o nome curto tirado do título da página."""
    d = json.loads((PASTA_DADOS / "ogol" / "clubes.json").read_text(encoding="utf-8"))
    for f in d.values():
        f["curto"] = (f.get("titulo") or "").split(" - ")[0].strip() or (f["nomes_ogol"][0] if f["nomes_ogol"] else f["id"])
        if not f.get("uf"):   # clube antigo sem cidade na ficha: é um clube goiano
            f["uf"] = "GO"
        if not str(f["id"]).isdigit() and f["nomes_ogol"]:
            # código-apelido ("americano", "espanha"): o ogol às vezes manda para outro clube ou para a seleção;
            # vale o nome do calendário, e a ficha só se for do mesmo clube
            nome_cal = f["nomes_ogol"][0]
            if norm(f["curto"]) != norm(nome_cal):
                f.update({"curto": nome_cal, "uf": "GO", "cidade": None, "nome_completo": None})
    for f in d.values():
        registro.corrigir_ficha(f)   # cidade e UF corrigidas para todas as coletas (registro.FICHA_COMUM)
    for i, certo in FICHA_CORRIGIDA.items():
        if i in d:
            d[i].update(certo)
    reg = registro.ler()
    for i in DE_OUTRAS_COLETAS:   # ficha que a lista do ogol desta coleta não traz: vem do cadastro comum
        if i not in d and i in reg:
            r = reg[i]
            d[i] = {"id": i, "curto": r["clube"], "nomes_ogol": [], "uf": r["uf"], "cidade": r["cidade"], "nome_completo": None}
    d.update(SEM_OGOL)
    return d


# clubes de outra coleta (já no cadastro comum) que as tabelas de nomes do importador usam: código -> motivo
DE_OUTRAS_COLETAS: dict[str, str] = {
    "3330": "Luziânia EC, no cadastro comum por outra coleta",
}

FICHA_CORRIGIDA: dict[str, dict] = {}   # as correções ficam em registro.FICHA_COMUM (valem para todas as coletas)


# clubes que só a RSSSF tem (anos sem calendário no ogol): código "rs-<nome>" -> ficha mínima; o importador preenche
SEM_OGOL: dict[str, dict] = {}


def sem_ogol(nome_rsssf: str, inteiro: bool = False) -> str:
    """Código de um clube que o ogol não tem, pelo nome da RSSSF ("rs-sc-internacional"). inteiro: o nome dado à mão
    (importar.NOME_CODIGO, "Guarany (Cachoeira do Sul)") fica inteiro, com a cidade dos parênteses."""
    base = nome_rsssf.strip() if inteiro else re.sub(r"\s*\([^)]*\)\s*$", "", nome_rsssf).strip()
    cidade = re.search(r"\(([^)]{3,})\)$", base) if inteiro else None
    # "rs-go1-...": o código leva a coleta, porque o cadastro comum já tem "rs-..." de outras coletas (o "rs-cruzeiro" é um
    # Cruzeiro de São Paulo, da A2)
    i = "rs-go1-" + norm(base).replace(" ", "-")
    SEM_OGOL.setdefault(i, {"id": i, "curto": base, "nomes_ogol": [], "uf": "GO", "cidade": cidade.group(1) if cidade else None,
                            "nome_completo": None})
    fichas.cache_clear()
    exibicao.cache_clear()
    return i


def _no_banco(f: dict) -> str | None:
    if f["id"] in MANUAL_DB:
        return MANUAL_DB[f["id"]][0]
    if f["id"] in MANUAL_NOVO:
        return None
    uf = f.get("uf")
    nomes = {f["curto"], *f["nomes_ogol"]}
    ks = {chave(n) for n in nomes} | {chave(f.get("nome_completo") or "")}
    cands = [n for n, c in banco().items() if c["uf"] == uf and c["chaves"] & ks]
    if len(cands) == 1:
        return cands[0]
    if len(cands) > 1:   # mais de um com a mesma chave na UF: fica o de nome igual a um nome do ogol
        exatos = [n for n in cands if n in nomes]
        if len(exatos) == 1:
            return exatos[0]
        iguais = [n for n in cands if chave(n) == chave(f["curto"]) and separar_uf(n)[1] in (None, uf)]
        return iguais[0] if len(iguais) == 1 else None
    return None


@lru_cache(maxsize=1)
def exibicao() -> dict[str, dict]:
    """Código do ogol -> {clube: nome de exibição, uf, cidade, no_banco: bool, nome_completo}."""
    fs = fichas()
    reg = registro.ler()
    saida: dict[str, dict] = {}
    novos: dict[str, str] = {}
    # um nome do banco é de um clube só: do que já está no cadastro comum ou, entre os candidatos, do que tem o nome igual
    tomados = {r["clube"] for r in reg.values()}
    pretendentes: dict[str, list[str]] = defaultdict(list)
    for i, f in fs.items():
        if i not in reg and (nb := _no_banco(f)):
            pretendentes[nb].append(i)
    dono = {}
    for nb, ids in pretendentes.items():
        if nb in tomados:
            continue
        iguais = [i for i in ids if nb in {fs[i]["curto"], *fs[i]["nomes_ogol"]}]
        dono[nb] = (iguais or ids)[0] if len(iguais) == 1 or len(ids) == 1 else None
    for i, f in fs.items():
        if i in reg and i not in MANUAL_DB and i not in MANUAL_NOVO:   # nome já dado antes (em qualquer coleta): não muda mais
            r = reg[i]
            saida[i] = {"clube": r["clube"], "uf": r["uf"], "cidade": r["cidade"], "no_banco": r["clube"] in banco(),
                        "nome_completo": f.get("nome_completo")}
            continue
        nb = _no_banco(f)
        dono_reg = {r["clube"]: k for k, r in reg.items()}
        if nb and i not in MANUAL_DB and dono.get(nb) != i and dono_reg.get(nb) != i:   # o nome do banco é de outro clube
            nb = None                                                                     # ("Santa Cruz-RN" x Santa Cruz de Natal)
        if nb:
            saida[i] = {"clube": nb, "uf": f.get("uf") or banco()[nb]["uf"], "cidade": f.get("cidade") or banco()[nb]["cidade"],
                        "no_banco": True, "nome_completo": f.get("nome_completo")}
        else:
            novos[i] = MANUAL_NOVO[i][0] if i in MANUAL_NOVO else f["curto"]
    # homônimos: o nome-base já usado por outro clube (do banco ou novo) ganha "-UF"; o nome do ogol que já traz
    # a UF ("Botafogo-DF", "Real-GO") fica como está
    usados: dict[str, set] = defaultdict(set)
    for n in banco():
        usados[chave(n)].add(n)
    for r in reg.values():
        usados[chave(r["clube"])].add(r["clube"])
    for i, base in novos.items():
        usados[chave(base)].add(i)
    for i, base in novos.items():
        f = fs[i]
        uf = f.get("uf")
        # "-UF" só quando o homônimo é de outro estado ("FC Cascavel" e "Cascavel", os dois do PR, já se distinguem)
        uf_reg = {r["clube"]: r["uf"] for r in reg.values()}
        ufs_outros = {banco()[n]["uf"] if n in banco() else uf_reg[n] if n in uf_reg else fs.get(n, {}).get("uf")
                      for n in usados[chave(base)] if n != i}
        unico = (len(usados[chave(base)]) == 1 or i in MANUAL_NOVO or separar_uf(base)[1] or ufs_outros <= {uf})
        nome = base if unico else f"{base}-{uf}"
        saida[i] = {"clube": nome, "uf": uf, "cidade": f.get("cidade"), "no_banco": False, "nome_completo": f.get("nome_completo")}
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    ex = exibicao()
    fs = fichas()
    print(len(ex), "clubes;", sum(c["no_banco"] for c in ex.values()), "já no futebol.db")
    repetidos = defaultdict(list)
    for i, c in ex.items():
        repetidos[c["clube"]].append(i)
    print("nomes repetidos:", {n: v for n, v in repetidos.items() if len(v) > 1})
    print("sem UF:", [(i, fs[i]["curto"]) for i, c in ex.items() if not c["uf"]])
    for i, c in sorted(ex.items(), key=lambda x: x[1]["clube"]):
        print(f"   {'B' if c['no_banco'] else ' '} {c['clube']:28} {c['uf'] or '??'} {c['cidade'] or '':22} ogol {i}: {fs[i]['nomes_ogol']}")
