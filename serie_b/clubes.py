"""Identifica os clubes da Série B: cada nome que aparece numa página vira um clube (nome + estado).

Ordem para achar o estado de um nome naquele ano:
1. o próprio nome traz o estado ("América-RN", "Atlético/GO", "Comercial MS");
2. a lista de participantes da página (nome completo com cidade e estado) tem um só clube que combina;
3. a tabela do mesmo grupo traz o nome com o estado;
4. MANUAL (decidido olhando a página);
5. o mesmo nome em outros anos sempre foi do mesmo estado.

O nome de exibição segue o da Série A quando o clube já está lá (um clube só nas duas divisões).

Uso: python serie_b/clubes.py     (lista o que não foi resolvido e os nomes ambíguos)
"""
from __future__ import annotations

import re
import sqlite3
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rsssf  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
UFS = set("AC AL AM AP BA CE DF ES GO MA MG MS MT PA PB PE PI PR RJ RN RO RR RS SC SE SP TO".split())

# (ano, nome) ou nome -> estado (ou (estado, nome de exibição) quando há dois clubes do mesmo nome no estado),
# decidido olhando a página: adversários do grupo (regional), Série A do ano, Wikipédia
MANUAL: dict = {
    "Brasília": "DF", "Taguatinga": "DF", "Ceilândia": "DF", "Cascavel": "PR", "Foz do Iguaçu": "PR", "Ubiratan": "MS",
    "Douradense": "MS", "Fast Club": "AM", "Galícia": "BA", "Guarapari": "ES", "Serra": "ES", "Itaperuna": "RJ",
    "Cabofriense": "RJ", "D. de Caxias": "RJ", "Capelense": "AL", "Lagarto": "SE", "Marcílio Dias": "SC",
    "Catanduvense": "SP", "XV De Novembro/Pirac": "SP", "XV de Novembro/Pir": "SP", "XV de Piracicaba": "SP",
    "União Barbarense": "SP", "4 de Julho": "PI", "Barra do Garças": "MT", "Internacional/SM": "RS", "Internacional SM": "RS",
    "Op. Ferroviário": "PR", "Glória": "RS", "São Domingos": "AL",
    "Central": "PE",            # Central de Caruaru: grupos do Nordeste (1981-83, 1989, 1995); 1990 pela Wikipédia
    "Santa Cruz": "PE",         # grupos do Nordeste; 2002 turno único com o Santa Cruz do Recife
    "Atlético": "GO",           # 2015, 2016 e 2019: Atlético Goianiense
    "Brasil": "RS",             # 2016 e 2021: Brasil de Pelotas
    (1981, "Vitória"): "ES", (1983, "Vitória"): "ES",   # grupos do Sudeste, com Guarapari e Volta Redonda
    (1982, "Vitória"): "BA", (1982, "Ferroviário"): "CE", (1982, "Nacional"): "AM",   # vieram da Taça de Ouro (Série A do ano)
    (1983, "Ferroviário"): "CE", (1983, "Rio Branco"): "ES", (1989, "Ferroviário"): "CE",
    (1983, "Esportivo"): "RS",  # grupo do Sul: Esportivo de Bento Gonçalves
    (1989, "Democrata"): ("MG", "Democrata-SL"), (1994, "Democrata"): ("MG", "Democrata-GV"), (1995, "Democrata"): ("MG", "Democrata-GV"),
}

# grafias do mesmo clube (nome sem acento e sem estado -> nome-base)
ALIAS = {
    "athletico": "atletico", "vasco da gama": "vasco", "sport recife": "sport", "ponte": "ponte preta", "boa": "boa esporte",
    "op ferroviario": "operario", "operario ferroviario": "operario", "gremio barueri": "barueri", "d de caxias": "duque de caxias",
    "moto clube": "moto club", "fast": "fast club", "xv de novembro pirac": "xv de piracicaba", "xv de novembro pir": "xv de piracicaba",
    "internacional sm": "inter de santa maria", "internacional/sm": "inter de santa maria", "mogi mirim": "mogi mirim",
    "xv de novembro": "xv de piracicaba",   # 1989 e 2002: EC XV de Novembro (Piracicaba)
    "jundiai": "paulista",   # o Paulista de Jundiaí jogou como Etti Jundiaí de 1999 a 2002 (mesmo clube)
}
# nome de exibição de clube só da Série B, quando o nome sozinho confunde
EXIBIR = {("brasil", "AL"): "Brasil-AL", ("uniao", "MT"): "União-MT"}
# grafias que dependem do estado (nome-base, estado) -> nome-base do mesmo clube na Série A
ALIAS_UF = {
    ("brasil", "RS"): "brasil de pelotas", ("brasilia", "DF"): "brasilia ec", ("internacional", "SP"): "inter de limeira",
    ("central", "PE"): "central", ("auto esporte", "PB"): "auto esporte",
}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def separar_estado(nome: str) -> tuple[str, str | None]:
    """'América-RN' -> ('América', 'RN'); 'Comercial MS' -> ('Comercial', 'MS'); 'XV De Novembro/Pirac' -> sem estado."""
    m = re.match(r"^(.*?)[\s\-/]+([A-Z]{2})$", nome.strip())
    if m and m.group(2) in UFS:
        return m.group(1).strip(), m.group(2)
    return nome.strip(), None


def participantes(ano: int) -> list[tuple[str, str]]:
    """[(texto do participante, estado)] da lista no começo da página."""
    t = rsssf.texto(ano)
    i = max(t.find("Participants"), t.find("Participantes"), 0)
    trecho = t[i:i + 6000]
    fim = re.search(r"\n\s*\[[A-Za-z0-9 ,/]+\]\s*\n|\n\s*(First Phase|Round 1|1st Phase|First Stage|Primeira Fase)\b", trecho)
    trecho = trecho[:fim.start()] if fim else trecho
    saida = []
    for m in re.finditer(r"([^()\[\]\n]{2,90}?)\s*\(([^()\n]{2,60})\)", trecho):
        uf = re.search(r"(?:^|[\s\-/])([A-Z]{2})\s*$", m.group(2))
        if uf and uf.group(1) in UFS:
            texto = re.sub(r"^\s*\d+\s*[-.]\s*", "", m.group(1)).strip()
            saida.append((texto, uf.group(1)))
    return saida


def bate(base: str, texto: str) -> bool:
    """O nome curto aparece no texto do participante (palavra inteira, sem acento; ou a parte em maiúsculas)."""
    b, t = norm(base), norm(texto)
    if not b:
        return False
    # a RSSSF marca o nome curto em maiúsculas ("Grêmio Esportivo BRASIL", "Clube de Regatas Brasil - CRB"):
    # quando a marca existe, só ela vale (senão "Brasil" casaria com o CRB)
    generico = {"FC", "EC", "AC", "SC", "CA", "AA", "SE", "CR", "AD", "FL", "ADRC", "AO", "AS", "GE", "CE", "SER", "AE", "AEC", "FBC",
                "FBPA", "SAF", "ESC", "CF", "AF", "EFC", "SEP", "CEC", "ADC", "AAC", "SA", "FBPA", "ECP", "ACF", "FR", "SAD", "CAP"}
    marcadas = [w for w in re.findall(r"\b[A-ZÀ-Ú][A-ZÀ-Ú\.]{1,}\b", re.sub(r"\([^)]*\)", "", texto)) if w.strip(".") not in generico]
    maius = norm(" ".join(marcadas))
    if maius:
        return maius == b or maius.startswith(b + " ") or b.startswith(maius + " ") or b == maius.replace(" ", "")
    return bool(re.search(rf"(^| ){re.escape(b)}( |$)", t))


def resolver_ano(ano: int) -> dict[str, tuple[str, str | None, str]]:
    """nome na página -> (base, estado, como foi achado)."""
    jogos, tabelas = rsssf.ler(ano)
    nomes = sorted({j.mandante for j in jogos} | {j.visitante for j in jogos})
    parts = participantes(ano)
    # nomes de tabela com estado, casados com os nomes dos jogos do mesmo grupo
    pela_tabela: dict[str, str] = {}
    for tb in tabelas:
        bloco = {j.mandante for j in jogos if j.fase == tb.fase and j.grupo == tb.grupo} | \
                {j.visitante for j in jogos if j.fase == tb.fase and j.grupo == tb.grupo}
        for nt, nj in rsssf.casar([r["nome"] for r in tb.linhas], bloco).items():
            uf = separar_estado(nt)[1]
            if uf:
                pela_tabela[nj] = uf
    saida = {}
    for n in nomes:
        base, uf = separar_estado(n)
        como = "nome"
        if not uf:
            ufs = {u for texto, u in parts if bate(base, texto)}
            if len(ufs) == 1:
                uf, como = ufs.pop(), "participantes"
        if not uf and n in pela_tabela:
            uf, como = pela_tabela[n], "tabela"
        manual = MANUAL.get((ano, n)) or MANUAL.get(n)
        if manual and (not uf or isinstance(manual, tuple)):
            uf, como = (manual[0], "manual") if isinstance(manual, tuple) else (manual, "manual")
            if isinstance(manual, tuple):
                base = manual[1]
        saida[n] = (base, uf, como)
    return saida


def resolver_todos() -> dict[int, dict[str, tuple[str, str | None, str]]]:
    anos = sorted(int(p.name[2:6]) for p in rsssf.PASTA.glob("br*l2.htm"))
    por_ano = {a: resolver_ano(a) for a in anos}
    # 5. o mesmo nome em outros anos, quando sempre foi do mesmo estado
    visto: dict[str, set] = defaultdict(set)
    for a, d in por_ano.items():
        for n, (base, uf, _) in d.items():
            if uf:
                visto[norm(base)].add(uf)
    for a, d in por_ano.items():
        for n, (base, uf, como) in list(d.items()):
            if not uf and len(visto[norm(base)]) == 1:
                d[n] = (base, next(iter(visto[norm(base)])), "outros anos")
    return por_ano


def chave_base(base: str, uf: str | None = None) -> str:
    """Nome-base comparável: sem acento, sem estado, com as grafias do mesmo clube juntas (ALIAS, ALIAS_UF)."""
    n = norm(base)
    n = ALIAS.get(n, n)
    return ALIAS_UF.get((n, uf), n)


def serie_a() -> tuple[dict, dict]:
    """Clubes que já estão no histórico da Série A: (nome-base, estado) -> (clube_id, nome de exibição), e
    nome-base -> [(clube_id, nome)] dos que estão lá sem estado."""
    sys.path.insert(0, str(RAIZ))
    from gerar_dashboard_v2 import nome as exibir
    con = sqlite3.connect(RAIZ / "db" / "brasileirao.db")
    com_uf, sem_uf = {}, defaultdict(list)
    for cid, bruto, uf in con.execute("""SELECT DISTINCT c.clube_id, c.nome, c.uf FROM fato_classificacao_final_nacional f
                                         JOIN dim_clube c USING (clube_id)"""):
        disp = exibir(bruto)
        base, uf_nome = separar_estado(disp)
        uf = uf_nome or uf
        if uf:
            com_uf[(chave_base(base, uf), uf)] = (cid, disp)
        else:
            sem_uf[chave_base(base)].append((cid, disp))
    con.close()
    return com_uf, sem_uf


def canonicos(por_ano: dict) -> dict[tuple[int, str], dict]:
    """(ano, nome na página) -> {clube: nome de exibição, uf, clube_id (da Série A, se já está lá)}."""
    sa, sa_sem_uf = serie_a()
    ufs_da_base: dict[str, set] = defaultdict(set)
    grafia: dict[tuple[str, str], Counter] = defaultdict(Counter)
    for a, d in por_ano.items():
        for n, (base, uf, _) in d.items():
            if uf:
                ufs_da_base[chave_base(base, uf)].add(uf)
                grafia[(chave_base(base, uf), uf)][base] += 1
    for (b, uf) in sa:
        ufs_da_base[b].add(uf)
    saida = {}
    for a, d in por_ano.items():
        for n, (base, uf, como) in d.items():
            k = (chave_base(base, uf), uf)
            unico = sa_sem_uf.get(k[0], [])
            explicito = (ALIAS.get(norm(base), norm(base)), uf) in ALIAS_UF
            if k in sa:
                cid, disp = sa[k]
            elif len(unico) == 1 and (len(ufs_da_base[k[0]]) == 1 or explicito):   # na Série A sem estado: nome sem homônimo, ou ligação explícita
                cid, disp = unico[0]
            elif k in EXIBIR:
                cid, disp = None, EXIBIR[k]
            else:
                cid, disp = None, grafia[k].most_common(1)[0][0] if grafia[k] else base
                if uf and len(ufs_da_base[k[0]]) > 1 and not disp.endswith(f"-{uf}"):
                    disp = f"{disp}-{uf}"   # homônimo de outro estado: "Comercial-MS"
            saida[(a, n)] = {"clube": disp, "uf": uf, "clube_id": cid, "como": como}
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    por_ano = resolver_todos()
    can = canonicos(por_ano)
    clubes = defaultdict(set)
    for (a, n), c in can.items():
        clubes[(c["clube"], c["uf"], c["clube_id"])].add(n)
    print("clubes:", len(clubes), " já na Série A:", sum(1 for k in clubes if k[2]))
    for (disp, uf, cid), nomes in sorted(clubes.items(), key=lambda x: x[0][0]):
        print(f"   {disp:24} {uf or '??'} {'A' if cid else ' '}  {sorted(nomes)}")
    sem = [(a, n) for a, d in por_ano.items() for n, (b, uf, c) in d.items() if not uf]
    print("pares ano-nome:", sum(len(d) for d in por_ano.values()), " sem estado:", len(sem))
    print(Counter(c for d in por_ano.values() for (_, _, c) in d.values()))
    for a, n in sem:
        print(f"   {a} {n}")
    # mesma base com estados diferentes (conferir: clubes homônimos de verdade ou erro)
    ufs = defaultdict(set)
    for a, d in por_ano.items():
        for n, (b, uf, c) in d.items():
            if uf:
                ufs[norm(b)].add(uf)
    print("bases com mais de um estado:", {b: sorted(u) for b, u in ufs.items() if len(u) > 1})
