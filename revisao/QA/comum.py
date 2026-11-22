"""Funções comuns da revisão QA (3ª rodada, 22/11/2026): Séries A e B contra fontes novas. Só leitura no banco."""
import difflib, re, sqlite3, sys, unicodedata
from datetime import date

sys.stdout.reconfigure(encoding="utf-8")
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)


def q(sql, *a):
    return c.execute(sql, a).fetchall()


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(r"\b(fc|ec|sc|cr|se|aa|ca|ad|ac|cd|ce|esporte clube|futebol clube|clube|club|de|do|da|e|regatas|foot ball|football|futebol|associacao|atletica|desportiva|sociedade|esportiva)\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()


# nomes das fontes novas que a normalização não casa sozinha (fonte -> nome de exibição no banco)
ALIAS = {
    "atletico pr": "Athletico-PR", "athletico paranaense": "Athletico-PR", "atletico paranaense": "Athletico-PR",
    "atletico mineiro": "Atlético-MG", "atletico mg": "Atlético-MG", "atletico goianiense": "Atlético-GO", "atletico go": "Atlético-GO",
    "america rj": "América-RJ", "america mineiro": "América-MG", "america mg": "América-MG", "america rn": "América-RN",
    "vasco gama": "Vasco", "vasco gama rio janeiro": "Vasco", "botafogo": "Botafogo", "botafogo rj": "Botafogo", "botafogo fr": "Botafogo",
    "sao paulo": "São Paulo", "palmeiras": "Palmeiras", "internacional": "Internacional", "inter": "Internacional",
    "gremio": "Grêmio", "gremio porto alegrense": "Grêmio", "gremio fbpa": "Grêmio", "red bull bragantino": "Bragantino", "rb bragantino": "Bragantino",
    "bragantino": "Bragantino", "cuiaba": "Cuiabá", "cuiaba ltda": "Cuiabá", "ceara": "Ceará",
    "goias": "Goiás", "avai": "Avaí", "criciuma": "Criciúma", "parana": "Paraná", "parana clube": "Paraná",
    "vitoria": "Vitória", "vitoria ba": "Vitória", "nautico": "Náutico", "nautico capibaribe": "Náutico",
    "sport recife": "Sport", "sport": "Sport", "santa cruz": "Santa Cruz", "juventude": "Juventude",
    "sao caetano": "São Caetano", "portuguesa": "Portuguesa", "portuguesa desportos": "Portuguesa", "guarani": "Guarani",
    "ponte preta": "Ponte Preta", "paysandu": "Paysandu", "paysandu sport": "Paysandu", "remo": "Remo", "clube remo": "Remo",
    "fortaleza": "Fortaleza", "figueirense": "Figueirense", "chapecoense": "Chapecoense", "chapecoense af": "Chapecoense",
    "coritiba": "Coritiba", "coritiba foot ball": "Coritiba", "santos": "Santos", "corinthians": "Corinthians",
    "corinthians paulista": "Corinthians", "flamengo": "Flamengo", "fluminense": "Fluminense", "cruzeiro": "Cruzeiro",
    "cruzeiro esporte": "Cruzeiro", "bahia": "Bahia", "barueri": "Barueri", "gremio barueri": "Barueri",
    "gremio prudente": "Barueri", "ipatinga": "Ipatinga", "brasiliense": "Brasiliense", "mirassol": "Mirassol",
    "abc": "ABC", "crb": "CRB", "csa": "CSA", "asa": "ASA", "oeste": "Oeste", "londrina": "Londrina",
    "operario pr": "Operário-PR", "operario ferroviario": "Operário-PR", "ituano": "Ituano", "novorizontino": "Novorizontino",
    "gremio novorizontino": "Novorizontino", "america gb": "América-RJ", "sampaio correa": "Sampaio Corrêa", "vila nova": "Vila Nova-GO",
    "vila nova go": "Vila Nova-GO", "tombense": "Tombense", "volta redonda": "Volta Redonda", "amazonas": "Amazonas",
    "brusque": "Brusque", "botafogo sp": "Botafogo-SP", "botafogo ribeirao preto": "Botafogo-SP",
    "athletic": "Athletic Club", "ferroviaria": "Ferroviária-SP", "paysandu sc": "Paysandu",
    "uniao sao joao": "União São João", "mixto": "Mixto", "goytacaz": "Goytacaz", "americano": "Americano-RJ",
    "moto club": "Moto Club", "moto clube": "Moto Club", "tuna luso": "Tuna Luso", "rio negro": "Rio Negro-AM",
    "comercial cg": "Comercial-MS", "tiradentes": "Tiradentes-PI", "ceub": "CEUB", "nacional": "Nacional-AM",
    "internacional limeira": "Inter de Limeira", "ser caxias sul": "Caxias", "caxias sul": "Caxias", "macae": "Macaé",
    "varzea grande": "CEOV Operário", "tuna luso brasileira": "Tuna Luso", "malutrom 2017": "J.Malucelli", "malutrom": "J.Malucelli",
}


def clubes_edicao(slug, temporada):
    """{clube_id: nome} dos clubes com jogo na edição (temporada ou chave)."""
    return dict(q("""select distinct cl.clube_id, cl.nome from partida p join edicao e using(edicao_id) join competicao co using(competicao_id)
                     join clube cl on cl.clube_id in (p.mandante_id, p.visitante_id) where co.slug=? and (e.temporada=? or e.chave=?)""",
                  slug, str(temporada), str(temporada)))


_outros = {}


def outros_nomes(cid):
    if cid not in _outros:
        _outros[cid] = [r[0] for r in q("select nome from clube_nome where clube_id=?", cid)]
    return _outros[cid]


class Casador:
    def __init__(self, slug, temporada, extra=None):
        self.cl = clubes_edicao(slug, temporada)
        self.porid = {}
        self.idx = {}
        for cid, nome in self.cl.items():
            for n in [nome] + outros_nomes(cid):
                if norm(n):
                    self.idx.setdefault(norm(n), cid)
        self.alias = dict(ALIAS)
        self.alias.update(extra or {})
        self.log = {}

    def __call__(self, nome):
        if not nome:
            return None
        n = norm(nome)
        if nome in self.log:
            return self.log[nome]
        cid = None
        if n in self.alias:
            alvo = self.alias[n]
            cid = next((k for k, v in self.cl.items() if v == alvo), None)
        if cid is None and n in self.idx:
            cid = self.idx[n]
        if cid is None:
            # tira sufixo de estado (" rj", " sp"...) e tenta de novo
            n2 = re.sub(r"\b(ac|al|am|ap|ba|ce|df|es|go|ma|mg|ms|mt|pa|pb|pe|pi|pr|rj|rn|ro|rr|rs|sc|se|sp|to)$", "", n).strip()
            if n2 in self.idx:
                cid = self.idx[n2]
            else:
                m = difflib.get_close_matches(n, list(self.idx), n=1, cutoff=0.8)
                if m:
                    cid = self.idx[m[0]]
        self.log[nome] = cid
        return cid

    def exato(self, nome):
        """Só casamento exato (nome normalizado, apelido ou sem a sigla do estado), sem aproximação."""
        n = norm(nome)
        if not n:
            return None
        if n in self.idx:
            return self.idx[n]
        if n in self.alias:
            return next((k for k, v in self.cl.items() if v == self.alias[n]), None)
        n2 = re.sub(r" (ac|al|am|ap|ba|ce|df|es|go|ma|mg|ms|mt|pa|pb|pe|pi|pr|rj|rn|ro|rr|rs|sc|se|sp|to|gb)$", "", n).strip()
        if n2 != n and n2 in self.idx:
            return self.idx[n2]
        return None


def jogos_banco(slug, temporada):
    return q("""select p.partida_id, p.data, p.mandante_id, p.visitante_id, p.gols_mandante, p.gols_visitante, f.nome, p.rodada,
                p.resultado_especial, m.nome, v.nome, p.publico, p.arbitro, p.penaltis_mandante, p.penaltis_visitante
                from partida p join edicao e using(edicao_id) join competicao co using(competicao_id) join fase f using(fase_id)
                join clube m on m.clube_id=p.mandante_id join clube v on v.clube_id=p.visitante_id
                where co.slug=? and (e.temporada=? or e.chave=?) order by p.data""", slug, str(temporada), str(temporada))


def _d(s):
    try:
        return date.fromisoformat(s)
    except Exception:
        return None


def comparar(slug, temporada, fonte, extra=None, janela=40):
    """fonte: lista de dicts {data, mandante, visitante, gm, gv}. Devolve resumo e lista de diferenças."""
    cas = Casador(slug, temporada, extra)
    banco = jogos_banco(slug, temporada)
    usados = set()
    res = {"fonte": len(fonte), "casados": 0, "placar_ok": 0, "data_ok": 0, "com_data": 0, "sem_par": [], "placar_dif": [],
           "data_dif": [], "invertido": []}
    for j in fonte:
        h, a = cas(j["mandante"]), cas(j["visitante"])
        if h is None or a is None:
            res["sem_par"].append((j, "clube?", j["mandante"] if h is None else j["visitante"]))
            continue
        cands = [b for b in banco if b[0] not in usados and {b[2], b[3]} == {h, a}]
        if not cands:
            res["sem_par"].append((j, "jogo?", ""))
            continue
        dj = _d(j.get("data"))

        def chave(b):
            mesma = (b[2] == h)
            db = _d(b[1])
            dist = abs((db - dj).days) if (db and dj) else (janela - 1 if dj else 999)
            return (dist > janela, not mesma, dist)
        b = min(cands, key=chave)
        db = _d(b[1])
        if dj and db and abs((db - dj).days) > janela and len(cands) > 0:
            # jogo de outra fase (ida/volta distante): ainda aceita o mais próximo
            pass
        usados.add(b[0])
        res["casados"] += 1
        res.setdefault("pares", []).append((j, b))
        mesma = (b[2] == h)
        gm, gv = (b[4], b[5]) if mesma else (b[5], b[4])
        if not mesma:
            res["invertido"].append((j, b))
        pm, pv = (b[13], b[14]) if mesma else (b[14], b[13])
        if j.get("gm") is not None and (gm, gv) == (j["gm"], j["gv"]):
            res["placar_ok"] += 1
        elif j.get("gm") is not None and pm is not None and (j["gm"], j["gv"]) in ((pm, pv), (gm + pm, gv + pv)):
            res["placar_ok"] += 1
            res.setdefault("com_penaltis", []).append((j, b))
        elif j.get("gm") is not None:
            res["placar_dif"].append((j, b))
        if dj:
            res["com_data"] += 1
            if db == dj:
                res["data_ok"] += 1
            else:
                res["data_dif"].append((j, b))
    res["casador"] = cas
    return res


def fmt_b(b):
    return f"{b[1]} {b[9]} {b[4]}x{b[5]} {b[10]} ({b[6]}, rod. {b[7]})"


def fmt_f(j):
    return f"{j.get('data')} {j['mandante']} {j.get('gm')}x{j.get('gv')} {j['visitante']}"
