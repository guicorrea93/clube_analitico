import unicodedata, re
def chave(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return " ".join("".join(c if c.isalnum() else " " for c in s).split())
MAPA = {
 "atletico paranaense": "Athletico-PR", "athletico paranaense": "Athletico-PR", "atletico pr": "Athletico-PR", "athletico pr": "Athletico-PR",
 "atletico mineiro": "Atlético-MG", "atletico mg": "Atlético-MG", "atletico goianiense": "Atlético-GO", "atletico go": "Atlético-GO",
 "vasco da gama": "Vasco", "america mineiro": "América-MG", "america mg": "América-MG", "gremio barueri": "Barueri",
 "gremio prudente": "Barueri", "red bull bragantino": "Bragantino", "sport recife": "Sport", "sport": "Sport",
 "paysandu": "Paysandu", "botafogo": "Botafogo", "santo andre": "Santo André", "sao caetano": "São Caetano",
 "america rj": "América-RJ", "america": "América-RJ", "bangu": "Bangu", "bahia": "Bahia",
 "internacional": "Internacional", "juventude": "Juventude", "nautico": "Náutico", "criciuma": "Criciúma",
}
def casar(nome, alvos):
    """devolve o nome do painel em `alvos` que casa com `nome`."""
    k = chave(nome)
    if k in MAPA and MAPA[k] in alvos: return MAPA[k]
    por = {chave(a): a for a in alvos}
    if k in por: return por[k]
    regras = [("atletico mineiro", "Atlético-MG"), ("atletico paranaense", "Athletico-PR"), ("athletico paranaense", "Athletico-PR"),
              ("atletico goianiense", "Atlético-GO"), ("america mineiro", "América-MG"), ("america futebol clube mg", "América-MG"),
              ("vasco", "Vasco"), ("sport club do recife", "Sport"), ("sport recife", "Sport"), ("corinthians", "Corinthians"),
              ("internacional", "Internacional"), ("gremio foot", "Grêmio"), ("barueri", "Barueri"), ("prudente", "Barueri"),
              ("bragantino", "Bragantino"), ("sao caetano", "São Caetano"), ("santo andre", "Santo André"), ("ponte preta", "Ponte Preta"),
              ("santa cruz", "Santa Cruz"), ("sao paulo", "São Paulo"), ("nautico", "Náutico")]
    for r, a in regras:
        if r in k and a in alvos: return a
    for a in alvos:
        ka = chave(a)
        if ka.split()[0] == k.split()[0] and (ka.startswith(k) or k.startswith(ka)): return a
    ws = set(k.split())
    cand = [a for a in alvos if set(chave(a).split()) <= ws]
    if len(cand) == 1: return cand[0]
    return None
