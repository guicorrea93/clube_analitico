"""Wikipédia pt (HTML da API parse, já em cache): classificação e matriz de resultados de cada temporada.
Fonte que a coleta NÃO usou (ela usou a Wikipédia en)."""
import json, re, sys, pathlib
from html.parser import HTMLParser
AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI)); sys.path.append(str(AQUI.parents[1] / "coleta" / "comum-europa"))
import baixar
import clubes_por as CP
TIT = {int(k): v for k, v in json.load(open(AQUI / "ptwiki_titulos.json", encoding="utf-8")).items()}

# artigo da Wikipédia pt / texto -> chave do cadastro (só o que o cadastro não resolve sozinho)
MANUAL = {
    "Sport Lisboa e Benfica": "Benfica", "Futebol Clube do Porto": "Porto", "Sporting Clube de Portugal": "Sporting",
    "Clube de Futebol Os Belenenses": "Belenenses", "Os Belenenses": "Belenenses", "Vitória Futebol Clube": "Vitória de Setúbal",
    "Vitória Sport Clube": "Vitória de Guimarães", "Vitória Sport Clube (Guimarães)": "Vitória de Guimarães",
    "Associação Académica de Coimbra - Organismo Autónomo de Futebol": "Académica",
    "Associação Académica de Coimbra – Organismo Autónomo de Futebol": "Académica", "Académica de Coimbra": "Académica",
    "Académico Futebol Clube": "Académico do Porto", "Académico FC": "Académico do Porto", "Académico do Porto": "Académico do Porto",
    "Clube Académico de Futebol": "Académico de Viseu", "Académico de Viseu Futebol Clube": "Académico de Viseu",
    "Boavista Futebol Clube": "Boavista", "Leixões Sport Club": "Leixões", "Futebol Clube Barreirense": "Barreirense",
    "Casa Pia Atlético Clube": "Casa Pia", "Sporting Clube Olhanense": "Olhanense", "Leça Futebol Clube": "Leça",
    "Grupo Desportivo da CUF": "CUF", "Grupo Desportivo CUF": "CUF", "Atlético Clube de Portugal": "Atlético CP",
    "Sport Comércio e Salgueiros": "Salgueiros", "Grupo Desportivo Estoril Praia": "Estoril", "Estoril Praia": "Estoril",
    "União Desportiva Oliveirense": "Oliveirense", "Futebol Clube de Famalicão": "Famalicão", "Associação Desportiva Sanjoanense": "Sanjoanense",
    "Sporting Clube de Braga": "Braga", "Sporting Braga": "Braga", "SC Braga": "Braga", "O Elvas Clube Alentejano de Desportos": "O Elvas",
    "Lusitano Futebol Clube": "Lusitano VRSA", "Lusitano Ginásio Clube": "Lusitano de Évora", "Sporting Clube da Covilhã": "Sporting da Covilhã",
    "Sporting Covilhã": "Sporting da Covilhã", "Clube Oriental de Lisboa": "Oriental de Lisboa", "Sport Clube União Torreense": "Torreense",
    "Caldas Sport Clube": "Caldas SC", "Sport Clube Beira-Mar": "Beira-Mar", "Clube Desportivo Feirense": "CD Feirense", "Feirense": "CD Feirense",
    "Varzim Sport Club": "Varzim", "Seixal Futebol Clube": "Seixal", "Futebol Clube Tirsense": "Tirsense",
    "União Futebol Comércio e Indústria de Tomar": "União de Tomar",
    "Sporting Clube Farense": "Farense", "Clube Desportivo de Montijo": "Montijo", "Clube de Futebol União de Coimbra": "União de Coimbra",
    "Sporting Clube de Espinho": "Espinho", "Portimonense Sporting Clube": "Portimonense", "Grupo Desportivo Riopele": "Riopele",
    "Club Sport Marítimo": "Marítimo", "Rio Ave Futebol Clube": "Rio Ave", "União Desportiva de Leiria": "União de Leiria",
    "União de Leiria": "União de Leiria",
    "Amora Futebol Clube": "Amora", "Futebol Clube Penafiel": "Penafiel", "Ginásio Clube de Alcobaça": "Ginásio de Alcobaça",
    "Recreio Desportivo de Águeda": "Recreio de Águeda", "Futebol Clube de Vizela": "Vizela", "Clube Desportivo das Aves": "Desportivo das Aves",
    "Grupo Desportivo de Chaves": "Chaves", "Clube Desportivo Nacional": "Nacional da Madeira", "Nacional da Madeira": "Nacional da Madeira",
    "Clube de Futebol Estrela da Amadora": "Estrela da Amadora", "Club Football Estrela da Amadora": "Estrela da Amadora",
    "Estrela da Amadora": "Estrela da Amadora",
    "Associação Desportiva de Fafe": "Fafe", "Clube de Futebol União": "União da Madeira", "Clube de Futebol União da Madeira": "União da Madeira",
    "Gil Vicente Futebol Clube": "Gil Vicente", "Futebol Clube Paços de Ferreira": "Paços de Ferreira", "Paços de Ferreira": "Paços de Ferreira",
    "Futebol Clube de Felgueiras": "Felgueiras", "Sporting Clube Campomaiorense": "Campomaiorense", "Futebol Clube de Alverca": "Alverca",
    "Clube Desportivo Santa Clara": "Santa Clara", "Moreirense Futebol Clube": "Moreirense", "Associação Naval 1º de Maio": "Naval 1º de Maio",
    "Associação Naval 1.º de Maio": "Naval 1º de Maio", "Naval 1º de Maio": "Naval 1º de Maio", "Clube Desportivo Trofense": "Trofense",
    "Futebol Clube de Arouca": "Arouca", "Clube Desportivo de Tondela": "Tondela", "AVS Futebol SAD": "AVS", "AVS Futebol": "AVS",
    "Belenenses SAD": "Belenenses SAD", "B-SAD": "Belenenses SAD", "Os Belenenses SAD": "Belenenses SAD",
    "Sport Lisboa e Elvas": "SL Elvas", "União Futebol Clube de Lisboa": "União de Lisboa", "Carcavelinhos Football Clube": "Carcavelinhos",
    "Clube de Futebol Os Unidos": "Unidos de Lisboa", "Lusitano de Évora": "Lusitano de Évora", "FC Porto": "Porto", "Sporting CP": "Sporting",
    "CS Marítimo": "Marítimo", "Vitória de Guimarães": "Vitória de Guimarães", "Vitória de Setúbal": "Vitória de Setúbal", "Boavista FC": "Boavista",
}


def limpa(t):
    return re.sub(r"\s*\(.*?\)\s*$", "", t.replace("\xa0", " ")).strip().rstrip("*").strip()


def chave_clube(textos, a):
    for t in textos:
        t = limpa(t)
        if t in MANUAL:
            return MANUAL[t]
    for t in textos:
        t = limpa(t)
        if not t:
            continue
        try:
            c = CP.esd(t, a)
        except Exception:
            c = None
        if c:
            return c
    return None


class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.tabs = []; s.pilha = []; s.cel = None

    def handle_starttag(s, tag, at):
        at = dict(at)
        if tag == "table":
            s.pilha.append([])
        elif tag == "tr" and s.pilha:
            s.pilha[-1].append([])
        elif tag in ("td", "th") and s.pilha and s.pilha[-1] is not None:
            if not s.pilha[-1]:
                s.pilha[-1].append([])
            s.cel = {"t": "", "links": [], "th": tag == "th", "style": (at.get("style") or "") + (at.get("bgcolor") or ""),
                     "span": int(re.sub(r"\D", "", at.get("colspan") or "1") or 1)}
            s.pilha[-1][-1].append(s.cel)
        elif tag == "a" and s.cel is not None:
            s.cel["links"].append(at.get("title") or "")
        elif tag == "br" and s.cel is not None:
            s.cel["t"] += " "

    def handle_endtag(s, tag):
        if tag == "table" and s.pilha:
            s.tabs.append(s.pilha.pop()); s.cel = None
        elif tag in ("td", "th"):
            s.cel = None

    def handle_data(s, d):
        if s.cel is not None:
            s.cel["t"] += d


_cache = {}


def tabelas(a):
    if a not in _cache:
        p = P(); p.feed(baixar.html_wiki("pt", TIT[a])); _cache[a] = p.tabs
    return _cache[a]


def num(t):
    t = t.strip().replace("−", "-").replace("–", "-").replace("+", "").strip("'")
    return int(t) if re.fullmatch(r"-?\d+", t) else None


CAMPOS = (("j", ("j", "pj", "jogos", "jg")), ("v", ("v",)), ("e", ("e",)), ("d", ("d",)),
          ("gp", ("gm", "gp", "gf", "golosmarcados")), ("gc", ("gs", "gc", "ga", "golossofridos")), ("pts", ("pts", "pontos", "pt")))


def classificacao(a, n):
    """Lista de dicts (ordem da página) com clube, j, v, e, d, gp, gc, pts."""
    for tab in tabelas(a):
        cab = None; res = []
        for row in tab:
            txt = [re.sub(r"\s+", "", c["t"]).lower() for c in row]
            if cab is None and any(x in ("pts", "pontos", "pt") for x in txt) and any(x in ("j", "pj", "jogos", "jg") for x in txt):
                cab = []
                for c, x in zip(row, txt):
                    cab += [x] * c["span"]
                continue
            if cab is None:
                continue
            cl, ci = None, None
            for i, c in enumerate(row):
                if c["links"] or (num(c["t"]) is None and re.search(r"[A-Za-zÀ-ú]{3}", c["t"])):
                    cl = chave_clube(c["links"] + [c["t"]], a)
                    if cl:
                        ci = i; break
            if cl is None:
                continue
            vals = []
            for c in row:
                vals += [c["t"]] * c["span"]
            # a coluna do clube no cabeçalho pode ter span 2 (escudo + nome): alinha pela posição do clube
            hci = next((i for i, h in enumerate(cab) if h in ("equipa", "equipas", "clube", "time", "equipe")), None)
            desloc = (ci - hci) if hci is not None else 0
            d = {"clube": cl}
            for i, h in enumerate(cab):
                k = next((k for k, pats in CAMPOS if h in pats), None)
                if k and 0 <= i + desloc < len(vals) and k not in d:
                    d[k] = num(vals[i + desloc])
            if all(d.get(k) is not None for k, _ in CAMPOS):
                res.append(d)
        if len(res) == n:
            return res
    return None


PLACAR = re.compile(r"^\s*(\d+)\s*[-–—:x]\s*(\d+)\s*(\[.*\])?\s*$")


def matriz(a, n):
    """{(mandante, visitante): (g, g)} pela matriz de resultados da página (linha = mandante)."""
    for tab in tabelas(a):
        linhas = []
        cab = None
        for row in tab:
            if not row:
                continue
            ls = [chave_clube(c["links"], a) if c["links"] else None for c in row]
            if cab is None and sum(1 for x in ls if x) >= n and not any(PLACAR.match(c["t"]) for c in row):
                cab = [x for x in ls if x]
                continue
            cl = chave_clube(row[0]["links"] + [row[0]["t"]], a)
            if cl and sum(1 for c in row[1:] if PLACAR.match(c["t"])) >= n - 3:
                vals = []
                for c in row[1:]:
                    vals += [c["t"].strip()] * c["span"]
                linhas.append((cl, vals))
        if len(linhas) != n:
            continue
        ordem = cab if cab and len(cab) == n and len(set(cab)) == n else [l[0] for l in linhas]
        if len(set(ordem)) != n:
            continue
        r = {}
        for cl, vals in linhas:
            if len(vals) < n:
                continue
            for j, v in enumerate(vals[:n]):
                m = PLACAR.match(v)
                if m and ordem[j] != cl:
                    r[(cl, ordem[j])] = (int(m.group(1)), int(m.group(2)))
        if len(r) >= n * (n - 1) * 0.9:
            return r
    return None
