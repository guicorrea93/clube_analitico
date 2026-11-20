"""Casa nomes da Wikipédia com os clubes de uma edição da Série B no banco (só leitura)."""
import os, re, sqlite3, unicodedata

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
con = sqlite3.connect("file:" + os.path.join(RAIZ, "db", "futebol.db").replace("\\", "/") + "?mode=ro", uri=True)

EXTRA = {  # apelidos comuns na Wikipédia pt -> nome no banco
    "atleticopr": "Athletico-PR", "atleticoparanaense": "Athletico-PR", "athleticoparanaense": "Athletico-PR",
    "americadenatal": "América-RN", "americamineiro": "América-MG", "guaranisp": "Guarani", "vilanova": "Vila Nova-GO",
    "portuguesasp": "Portuguesa", "desportiva": "Desportiva-ES", "desportivaferroviaria": "Desportiva-ES",
    "redbullbragantino": "Bragantino", "atleticogoianiense": "Atlético-GO", "atleticomineiro": "Atlético-MG",
    "vascodagama": "Vasco", "barra": "Barra do Garças", "nacional": "Nacional-AM", "river": "River-PI", "riverpi": "River-PI",
    "juventus": "Juventus-SP", "saojose": "São José-SP", "americano": "Americano-RJ", "americasjrp": "América-SP",
    "riodenegro": "Rio Negro-AM", "rionegro": "Rio Negro-AM", "botafogorj": "Botafogo", "uniaorondonopolis": "União Rondonópolis",
    "uniaobarbarense": "União Barbarense", "saoraimundoam": "São Raimundo", "goias": "Goiás", "brasilia": "Brasília EC",
}


def chave(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z]", "", s)


def clubes_edicao(ano):
    rows = con.execute("""SELECT DISTINCT c.clube_id, c.nome FROM partida p JOIN edicao e USING(edicao_id)
                          JOIN clube c ON c.clube_id IN (p.mandante_id, p.visitante_id)
                          WHERE e.competicao_id=2 AND e.temporada=?""", (str(ano),)).fetchall()
    return dict(rows)


def resolvedor(ano):
    cl = clubes_edicao(ano)
    alias = {}
    for cid, nome in cl.items():
        alias.setdefault(chave(nome), cid)
        alias.setdefault(chave(nome.split("-")[0]), cid)
        for (n,) in con.execute("SELECT nome FROM clube_nome WHERE clube_id=?", (cid,)):
            alias.setdefault(chave(n), cid)
    por_nome = {v: k for k, v in cl.items()}

    def r(nome):
        k = chave(nome)
        if k in EXTRA and EXTRA[k] in por_nome:
            return por_nome[EXTRA[k]]
        if k in alias:
            return alias[k]
        cands = [cid for a, cid in alias.items() if a.startswith(k) or k.startswith(a)]
        cands = list(dict.fromkeys(cands))
        if len(cands) == 1:
            return cands[0]
        return None
    return r, cl
