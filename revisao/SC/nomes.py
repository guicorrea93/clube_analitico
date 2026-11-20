"""Revisão Série C (SC): casa o nome de um time na Wikipédia com o clube do pacote, dentro de uma edição."""
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from comum import banco, ler_csv  # noqa: E402

# nomes da Wikipédia que não casam sozinhos (wiki -> pacote)
MANUAL = {
    "etti jundiai": "Paulista", "jundiai": "Paulista", "paulista": "Paulista",
    "ituiutaba": "Boa Esporte", "boa": "Boa Esporte",
    "santo amaro": "Manchete", "fluminense de feira": "Fluminense-BA", "fluminense-ba": "Fluminense-BA",
    "fluminense": "Fluminense", "america mineiro": "América-MG", "america de natal": "América-RN",
    "esportivo de passos": "Esportivo-MG", "novorizontino": None, "gremio barueri": "Barueri",
    "atletico goianiense": "Atlético-GO", "atletico-go": "Atlético-GO", "athletic": "Athletic Club",
    "operario ferroviario": "Operário-PR", "operario-pr": "Operário-PR", "sao jose-poa": "São José-RS",
    "sao jose": "São José-RS", "globo": "Globo FC", "retro": "Retrô FC", "manaus": "Manaus FC",
    "ypiranga de erechim": "Ypiranga-RS", "aguia de maraba": "Águia", "aguia": "Águia",
    "guarany de sobral": "Guarany", "guarany-ce": "Guarany", "campinense-pb": "Campinense",
    "salgueiro-pe": "Salgueiro", "sao raimundo-pa": "São Raimundo-PA", "atletico acreano": "Atlético-AC",
    "ferroviaria": "Ferroviária-SP", "ferroviario": "Ferroviário-CE", "ferroviario-ce": "Ferroviário-CE",
    "atletico cajazeirense": "Atlético-PB", "lousano paulista": "Lousano Paulista", "independente-ba": "Independente-BA",
    "internacional de limeira": "Inter de Limeira", "corinthians de presidente prudente": "Corinthians Prudente",
    "atletico soroacaba": "Atlético Sorocaba", "inter-sm": "Inter de Santa Maria", "internacional de santa maria": "Inter de Santa Maria",
    "internacional": "Inter de Santa Maria", "uniao agricola barbarense": "União Barbarense", "iuiutaba": "Boa Esporte",
    "gremio barueri-sp": "Barueri", "brasil": "Brasil de Pelotas", "adap/galo maringa": "Adap Galo Maringá",
    "adap galo maringa-pr": "Adap Galo Maringá", "atletico hermann aichinger": "Hermann Aichinger",
    "atletico de ibirama": "Hermann Aichinger", "ulbra-rs": "Ulbra", "roma-pr": "Roma", "jaciara-mt": "Jaciara",
    "linhares-es": "Linhares", "atletico tres coracoes": "Atlético Três Corações", "atletico de tres coracoes": "Atlético Três Corações",
    "america de esperanca": "América-PB", "america de esperanca-pb": "América-PB", "uniao araguainense": "União Araguainense",
    "barra de teresopolis": "Barra-RJ", "botafogo sobradinho": "Sobradinho", "vila nova": "Vila Nova-GO", "vila nova-go": "Vila Nova-GO", "river-pi": "River-PI", "river": "River-PI",
}


def chave(n):
    n = unicodedata.normalize("NFKD", n or "").encode("ascii", "ignore").decode().lower()
    n = re.sub(r"\s*\(([a-z]{2})\)", r"-\1", n)
    n = re.sub(r"/([a-z]{2})\b", r"-\1", n)
    n = re.sub(r"\s*\([^)]*\)", "", n)
    n = re.sub(r"^(?:se|ec|aa|sc|fc|ad|a\.d\.|ser|cr|ac|gr)\s+", "", n)
    return re.sub(r"\s+", " ", n).strip()


def _apelidos():
    ap = {}
    for r in ler_csv("clubes.csv"):
        ap.setdefault(chave(r["clube"]), set()).add(r["clube"])
        for p in (r["nomes_fonte"] or "").split("|"):
            partes = p.split(":")
            if len(partes) >= 2:
                ap.setdefault(chave(partes[1]), set()).add(r["clube"])
    con = banco()
    for n, c in con.execute("select cn.nome, c.nome from clube_nome cn join clube c using (clube_id)"):
        ap.setdefault(chave(n), set()).add(c)
    return ap


AP = _apelidos()


def casar(nome_wiki, clubes_edicao, ano=None):
    """Clube do pacote para o nome da Wikipédia, entre os clubes da edição; None se não achar."""
    k = chave(nome_wiki)
    cands = set(clubes_edicao)
    if k in MANUAL and MANUAL[k] in cands:
        return MANUAL[k]
    if k == "novorizontino":
        for c in ("GE Novorizontino", "Novorizontino"):
            if c in cands:
                return c
    for c in cands:
        if chave(c) == k:
            return c
    achou = AP.get(k, set()) & cands
    if len(achou) == 1:
        return achou.pop()
    base = re.sub(r"-[a-z]{2}$", "", k)
    pref = [c for c in cands if chave(c) == base or re.sub(r"-[a-z]{2}$", "", chave(c)) == base]
    if len(pref) == 1:
        return pref[0]
    pref = [c for c in cands if chave(c).startswith(base) or base.startswith(re.sub(r"-[a-z]{2}$", "", chave(c)))]
    if len(pref) == 1:
        return pref[0]
    # parecido: difflib entre os nomes (e apelidos) dos clubes da edição
    import difflib
    alvo = {}
    for c in cands:
        alvo[chave(c)] = c
        for a, cs in AP.items():
            if c in cs:
                alvo.setdefault(a, c)
    m = difflib.get_close_matches(k, list(alvo), n=2, cutoff=0.85)
    if m and (len(m) == 1 or alvo[m[0]] == alvo[m[1]]):
        return alvo[m[0]]
    return None
