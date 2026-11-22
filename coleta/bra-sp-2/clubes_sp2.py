"""Identidade dos clubes da Copa do Brasil (mesmo método da Série C; clube já nomeado na Série C usa o mesmo nome).

Cada clube é o código dele no ogol (o mesmo em todas as edições, mesmo quando o clube muda de nome).
Da ficha do ogol saem o nome curto, a cidade e a UF. O nome de exibição é:
1. o `clube.nome` do db/futebol.db, quando o clube já está lá (mesma UF e um dos nomes de `clube_nome` igual);
2. senão, o nome curto do ogol, com "-UF" só quando outro clube tem o mesmo nome.
Exceções decididas à mão ficam em MANUAL, com o motivo.

Uso: python coleta/bra-sp-2/clubes_sp2.py     (lista os casamentos com o banco e os clubes novos)
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
    # A2: clubes que só a RSSSF tem (antes de 1998), com nome que confundiria
    "rs-uniao-mogi-das-cruzes": ("União Mogi", "União FC de Mogi das Cruzes; \"União-SP\" não diz qual União paulista é"),
    "rs-internacional-bebedouro": ("Internacional de Bebedouro", "AA Internacional de Bebedouro; o cadastro já tem "
                                   "\"SC Internacional-SP\" e \"CA Internacional-SP\", e o Inter de Limeira"),
    "rs-lemense-leme": ("EC Lemense", "Esporte Clube Lemense (anos 1980): não é o Lemense FC, fundado em 2005 (ogol 24586)"),
    "rs-palmeiras-sao-joao-da-boa-vista": ("Palmeiras (São João da Boa Vista)", "Palmeiras FC de São João da Boa Vista: "
                                           "nunca o nome exato do Palmeiras do banco (regra 6b)"),
    # A2 de 1947 a 1966 (edições sem os jogos): clubes antigos homônimos de outros, com a cidade ou o nome completo
    "rs-barretos": ("Barretos FC", "Barretos Futebol Clube (até 1960); o Barretos EC, fundado em 1960, é o 24576 do ogol"),
    "rs-aracatuba": ("Araçatuba FC", "Araçatuba Futebol Clube (1954-1955); a AE Araçatuba (ogol 19365) é de 1972"),
    "rs-sao-paulo-aracatuba": ("São Paulo (Araçatuba)", "São Paulo FC de Araçatuba; \"São Paulo-SP\" seria o tricolor"),
    "rs-ferroviaria-botucatu": ("Ferroviária (Botucatu)", "AA Ferroviária de Botucatu; a Ferroviária do banco é a de Araraquara"),
    "rs-comercial-limeira": ("Comercial (Limeira)", "Comercial FC de Limeira"),
    "rs-comercial-lins": ("Comercial (Lins)", "Comercial FC de Lins"),
    "rs-fortaleza-barretos": ("Fortaleza (Barretos)", "Fortaleza EC de Barretos"),
    "rs-avenida-salto": ("Avenida (Salto)", "AA Avenida de Salto"),
    "rs-rio-pardo-sao-jose-do-rio-pardo": ("Rio Pardo FC", "Rio Pardo FC de São José do Rio Pardo"),
    "rs-osvaldo-cruz": ("AA Osvaldo Cruz", "AA Osvaldo Cruz (1959-1966); o Osvaldo Cruz FC (ogol 15768) é de 2004"),
    "rs-estrada-de-ferro-sorocaba": ("Estrada de Ferro Sorocabana", "Estrada de Ferro Sorocabana FC, de Sorocaba"),
    "rs-estrela-piquete": ("Estrela (Piquete)", "EC Estrela de Piquete"),
    "rs-derac-araraquara": ("Derac (Araraquara)", "EC D.E.R. de Araraquara; o \"DERAC\" dos anos 1980 é o de Itapetininga"),
    "rs-palestra-sao-bernardo-do-campo": ("Palestra São Bernardo", "Palestra FC de São Bernardo do Campo"),
    "rs-catanduva": ("Catanduva EC", "Catanduva EC (1955-1963); o GE Catanduvense (ogol 15767) é de 1970"),
    "rs-atletico-brasil-clube-paraguacu-paulista": ("Atlético Brasil", "Atlético Brasil Clube de Paraguaçu Paulista"),
    "rs-sao-joao-jundiai": ("São João (Jundiaí)", "São João FC de Jundiaí"),
    "rs-bauru": ("Bauru AC", "Bauru Atlético Clube"),
    "rs-ferroviaria-assis": ("Ferroviária (Assis)", "AA Ferroviária de Assis; a Ferroviária do banco é a de Araraquara"),
    "rs-comercial-araras": ("Comercial (Araras)", "Comercial FC de Araras"),
    "rs-comercial-mogi-das-cruzes": ("Comercial (Mogi das Cruzes)", "Comercial FC de Mogi das Cruzes"),
    "rs-ferroviaria-pindamonhangaba": ("Ferroviária (Pindamonhangaba)", "AA Ferroviária de Pindamonhangaba"),
    "rs-sao-paulo-araraquara": ("São Paulo (Araraquara)", "São Paulo FC de Araraquara; \"São Paulo-SP\" seria o tricolor"),
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
    """Fichas do ogol (data/coleta/bra-sp-2/ogol/clubes.json e, para os clubes que a A2 não tem no ogol, as do Paulista,
    data/coleta/bra-sp-1/ogol/clubes.json), com o nome curto tirado do título da página."""
    d = json.loads((PASTA_DADOS.parent / "bra-sp-1" / "ogol" / "clubes.json").read_text(encoding="utf-8"))
    if (PASTA_DADOS / "ogol" / "clubes.json").exists():
        d.update(json.loads((PASTA_DADOS / "ogol" / "clubes.json").read_text(encoding="utf-8")))
    for f in d.values():
        f["curto"] = (f.get("titulo") or "").split(" - ")[0].strip() or (f["nomes_ogol"][0] if f["nomes_ogol"] else f["id"])
        if not f.get("uf"):   # clube antigo sem cidade na ficha: é um clube paulista
            f["uf"] = "SP"
        if not str(f["id"]).isdigit() and f["nomes_ogol"]:
            # código-apelido ("americano", "espanha"): o ogol às vezes manda para outro clube ou para a seleção;
            # vale o nome do calendário, e a ficha só se for do mesmo clube
            nome_cal = f["nomes_ogol"][0]
            if norm(f["curto"]) != norm(nome_cal):
                f.update({"curto": nome_cal, "uf": "SP", "cidade": None, "nome_completo": None})
    for i, certo in FICHA_CORRIGIDA.items():
        if i in d:
            d[i].update(certo)
    d.update(SEM_OGOL)
    return d


# fichas do ogol com cidade/estado de outro clube (conferido na RSSSF e na Wikipédia)
FICHA_CORRIGIDA: dict[str, dict] = {
    "39622": {"cidade": "São Paulo", "uf": "SP"},   # AA São Bento (campeão de 1914 APEA e 1925), da capital; a ficha diz Marília
    "59514": {"cidade": "São Paulo", "uf": "SP", "estado": "São Paulo", "nome_completo": None, "fundacao": None},
    # Jardim América do Paulista de 1935 (APEA), da capital; a ficha é a do Jardim América de Morrinhos (GO), de 1960
}


# clubes que só a RSSSF tem (anos sem calendário no ogol): código "rs-<nome>" -> ficha mínima; o importador preenche
SEM_OGOL: dict[str, dict] = {}


def sem_ogol(nome_rsssf: str, cidade: str | None = None) -> str:
    """Código de um clube que o ogol não tem, pelo nome da RSSSF e a cidade da lista de participantes da página
    ("rs-internacional-bebedouro"): o mesmo nome em cidades diferentes são clubes diferentes."""
    base = re.sub(r"\s*\([^)]*\)\s*$", "", nome_rsssf).strip()
    if cidade:   # "Aparecida Do Norte" -> "Aparecida do Norte"
        cidade = re.sub(r"(?<=\s)(Do|Da|De|Dos|Das|D')(?=\s|\b)", lambda m: m.group(1).lower(), cidade.strip())
    i = "rs-" + norm(base).replace(" ", "-") + (f"-{norm(cidade).replace(' ', '-')}" if cidade and norm(cidade) != norm(base) else "")
    SEM_OGOL.setdefault(i, {"id": i, "curto": base, "nomes_ogol": [], "uf": "SP", "cidade": cidade, "nome_completo": None})
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
        # nunca o nome exato de outro clube (do banco, do cadastro comum ou já dado aqui): clube paulista homônimo leva a
        # cidade ("Palmeiras (São João da Boa Vista)"); regra 6b de docs/agente-coleta-COMECE-AQUI.md
        tomados_aqui = {s["clube"] for k, s in saida.items() if k != i}
        if i not in MANUAL_NOVO and (nome in banco() or nome in {r["clube"] for k, r in reg.items() if k != i} or nome in tomados_aqui):
            nome = f"{base} ({f.get('cidade')})" if f.get("cidade") else f"{base}-{uf}"
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
