"""Para pares de clubes suspeitos: jogos do par no banco, no Bola na Área, no ogol (json da coleta) e na Wikipédia pt (cache SB).
Uso: python -I revisao/QA/tres_placares.py   (lista fixa abaixo)"""
import json, sys, pathlib, unicodedata, re
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import comum, bna, datas_3fontes

CASOS = [("1971", "Ferroviário-CE", "Itabaiana"), ("1971", "Itabaiana", "Remo"), ("1971", "Villa Nova-MG", "Ponte Preta"),
         ("1972", "Atlético-BA", "Central"), ("1981", "Flamengo-PI", "Remo"), ("1981", "Flamengo-PI", "Rio Negro-AM"),
         ("1981", "Ceará", "Rio Negro-AM"), ("1982", "Tiradentes-PI", "América-RN"), ("1982", "Sampaio Corrêa", "Tiradentes-PI"),
         ("1990", "Botafogo-SP", "Juventude"), ("1991", "Independência", "Paysandu"), ("1992", "Ceará", "Fortaleza"), ("1992", "Central", "CSA"),
         ("1994", "Democrata-GV", "Sergipe"), ("1995", "Bangu", "Athletico-PR"), ("1997", "Remo", "Tuna Luso"),
         ("1998", "Sampaio Corrêa", "Volta Redonda"), ("1998", "Botafogo-SP", "Criciúma"), ("1998", "Botafogo-SP", "Vila Nova-GO"),
         ("1998", "Joinville", "Paysandu")]


def chave(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.split(r"[ \-]", s)[0]


if __name__ == "__main__":
    for ano, a, b in CASOS:
        print(f"### {ano} {a} x {b}")
        for x in comum.jogos_banco("bra-serie-b", ano):
            if {x[9], x[10]} == {a, b}:
                print("   banco:", comum.fmt_b(x), x[8] or "")
        cas = comum.Casador("bra-serie-b", ano)
        ida = {k for k, v in cas.cl.items() if v in (a, b)}
        for j in bna.jogos("bra-serie-b", ano, bna.paginas_edicao("bra-serie-b", ano)):
            if {cas.exato(j["mandante"]), cas.exato(j["visitante"])} == ida:
                print("   BNA:  ", comum.fmt_f(j), "*" if j["asterisco"] else "", (j["gols"] or "")[:80])
        try:
            og = json.load(open(f"data/serie_b/ogol/serie_b_{ano}.json", encoding="utf-8"))
        except FileNotFoundError:
            og = []
        for j in og:
            if {chave(j["mandante"]), chave(j["visitante"])} == {chave(a), chave(b)}:
                print("   ogol: ", j["data"], j["mandante"], j["gols_mandante"], "x", j["gols_visitante"], j["visitante"], j["url"])
        for j in datas_3fontes.pt_jogos(ano):
            if {cas.exato(j["mandante"]) or cas(j["mandante"]), cas.exato(j["visitante"]) or cas(j["visitante"])} == ida:
                print("   pt:   ", comum.fmt_f(j))
