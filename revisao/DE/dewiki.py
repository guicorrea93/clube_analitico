"""Leitor das páginas da Wikipédia de de cada temporada da Bundesliga: Abschlusstabelle, Farblegende (Abstieg),
Kreuztabelle e Relegation. Nomes dos clubes -> nome de exibição do pacote pelo cadastro da coleta (clubes_ger.esd),
mais alguns nomes alemães que faltam lá (EXTRA)."""
import re, sys, pathlib
AQUI = pathlib.Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "coleta" / "comum-europa"))
sys.path.insert(0, str(AQUI))
import clubes_ger as cg  # noqa: E402
from rev_baixar import wikitext  # noqa: E402

EXTRA = {"MSV Duisburg": "MSV Duisburg", "Meidericher SV": "MSV Duisburg", "KFC Uerdingen 05": "Bayer 05 Uerdingen",
         "FC Bayer 05 Uerdingen": "Bayer 05 Uerdingen", "Tennis Borussia Berlin": "TeBe Berlin", "SC Tasmania 1900 Berlin": "Tasmania 1900 Berlin",
         "Borussia Neunkirchen": "Borussia Neunkirchen", "FC 08 Homburg": "FC 08 Homburg", "FC Homburg": "FC 08 Homburg",
         "SG Wattenscheid 09": "SG Wattenscheid 09", "SpVgg Greuther Fürth": "SpVgg Greuther Furth", "Blau-Weiß 90 Berlin": "Blau-Weiss 90 Berlin",
         "SV Darmstadt 98": "SV Darmstadt 98", "Stuttgarter Kickers": "Stuttgarter Kickers", "1. FC Lokomotive Leipzig": "VfB Leipzig",
         "VfB Leipzig": "VfB Leipzig", "Rot-Weiss Essen": "Rot-Weiss Essen", "Wuppertaler SV": "Wuppertaler SV", "Wuppertaler SV Borussia": "Wuppertaler SV",
         "SSV Ulm 1846": "SSV Ulm 1846", "SSV Ulm 1846 Fußball": "SSV Ulm 1846", "1. FC Heidenheim": "1. FC Heidenheim",
         "1. FC Heidenheim 1846": "1. FC Heidenheim", "Holstein Kiel": "Holstein Kiel", "FC St. Pauli": "FC St. Pauli",
         "Bayer 04 Leverkusen": "Bayer Leverkusen", "TSG 1899 Hoffenheim": "1899 Hoffenheim", "RB Leipzig": "RasenBallsport Leipzig",
         "SC Paderborn 07": "SC Paderborn 07", "FC Ingolstadt 04": "FC Ingolstadt 04", "SpVgg Unterhaching": "SpVgg Unterhaching",
         "FC Energie Cottbus": "Energie Cottbus", "Dynamo Dresden": "Dynamo Dresden", "SG Dynamo Dresden": "Dynamo Dresden",
         "1. FC Dynamo Dresden": "Dynamo Dresden", "FC Hansa Rostock": "Hansa Rostock", "SC Fortuna Köln": "Fortuna Koln",
         "Fortuna Köln": "Fortuna Koln", "SV Waldhof Mannheim": "Waldhof Mannheim", "SV Waldhof Mannheim 07": "Waldhof Mannheim",
         "Kickers Offenbach": "Kickers Offenbach", "Offenbacher FC Kickers": "Kickers Offenbach", "Preußen Münster": "Preussen Munster",
         "SC Preußen Münster": "Preussen Munster", "Borussia VfL 1900 Mönchengladbach": "Bor. Monchengladbach",
         "Eintracht Frankfurt": "Eintracht Frankfurt", "Hannover 96": "Hannover 96", "VfL Bochum": "VfL Bochum",
         "VfL Bochum 1848": "VfL Bochum", "Hamburger SV": "Hamburger SV", "Karlsruher SC": "Karlsruher SC"}


def clube(nome, ano):
    nome = re.sub(r"\s*\(.*?\)\s*$", "", nome).strip()
    k = EXTRA.get(nome) or cg.esd(nome, ano)
    return cg.exibicao(k) if k else None


def titulo(a):
    return f"Fußball-Bundesliga {a}/{str(a+1)[-2:]}" if a != 1999 else "Fußball-Bundesliga 1999/2000"


def link(cel):
    """Primeiro link ou nome de arquivo de uma célula: [[A|B]] -> A; [[Datei:x|22px|Nome]] -> Nome."""
    m = re.search(r"\[\[(?:Datei|File|Bild):[^\]]*\|([^|\]]+)\]\]", cel)
    if m and not re.fullmatch(r"[\dx]+px|mini|links|rechts", m.group(1).strip()):
        return m.group(1).strip()
    m2 = re.search(r"\[\[(?:Datei|File|Bild):[^\]]*\|link=([^|\]]+)", cel)
    if m2:
        return m2.group(1).strip()
    cel = re.sub(r"\[\[(?:Datei|File|Bild):[^\]]*\]\]", "", cel)
    m = re.search(r"\[\[([^|\]]+)(?:\|[^\]]*)?\]\]", cel)
    if m:
        return m.group(1).strip()
    return re.sub(r"\{\{.*?\}\}|'''|''", "", cel).strip()


def tabela(t, a):
    """Abschlusstabelle: lista de dicts (pos, clube, v, e, d, gp, gc, abzug, farbe)."""
    i = t.find("Abschlusstabelle")
    if i < 0:
        i = t.find("Fußballtabelle/Kopf")
    res = []
    for m in re.finditer(r"\{\{Fußballtabelle/Zeile([^\n]*)\}\}", t[i:]):
        z = m.group(1)
        p = dict((k.strip(), v.strip()) for k, v in re.findall(r"\|\s*([A-Za-zäöü]+)\s*=\s*((?:\[\[[^\]]*\]\]|\{\{[^}]*\}\}|[^|])*)", z))
        if "Rang" not in p:
            continue
        r = int(re.sub(r"\D", "", p["Rang"]) or 0)
        if res and r <= res[-1]["pos"] and r == 1:
            break   # outra tabela (Heim/Auswärts)
        nome = link(p.get("Verein", ""))
        n = lambda k: int((re.findall(r"-?\d+", re.sub(r"\{\{0\|[^}]*\}\}", "", p.get(k, "0"))) or [0])[-1])
        res.append({"pos": r, "nome": nome, "clube": clube(nome, a), "v": n("S"), "e": n("U"),
                    "d": n("N"), "gp": n("ET"), "gc": n("GT"),
                    "abzug": int(re.sub(r"[^\d-]", "", p.get("Abzug", "0")) or 0), "farbe": p.get("Farbe", "").lower(),
                    "raw": z})
    return res


def legenda(t):
    """Farblegende: (cor, texto)."""
    return [(c.lower(), x) for c, x in re.findall(r"\{\{Farblegende\|#?([0-9A-Fa-f]{6})\|(.*)\}\}", t)]


def kreuz(t, a):
    """Kreuztabelle: {(mandante, visitante): (gm, gv)} e a lista de células sem placar."""
    i = t.find("Kreuztabelle")
    if i < 0:
        return {}, ["sem Kreuztabelle"]
    j = t.find("{|", i)
    k = t.find("\n|}", j)
    bloco = t[j:k]
    linhas = re.split(r"\n\|-[^\n]*", bloco)
    cab = None
    res, prob = {}, []
    for ln in linhas:
        if cab is None:
            cels = re.findall(r"(?:^|\n)[!|]\s*([^\n]*)", ln)
            nomes = [link(c) for c in cels if "Datei" in c or "File" in c or "Bild" in c or "[[" in c]
            if len(nomes) >= 15:
                cab = [clube(n, a) for n in nomes]
                if None in cab:
                    prob.append(f"cabeçalho sem cadastro: {[n for n, c in zip(nomes, cab) if c is None]}")
            continue
        txt = ln.strip()
        if not txt:
            continue
        # células: separa por || e por quebras com |
        txt = re.sub(r"\{\{0\|[^{}]*(?:\{\{[^{}]*\}\}[^{}]*)*\}\}", "", txt)
        txt = re.sub(r"\{\{FN\|[^{}]*\}\}|<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", txt)
        cels = re.split(r"\|\||\n[|!]", "\n" + txt)
        cels = [c for c in cels if c.strip() != ""]
        cels = [re.sub(r"^\s*[|!]", "", c) for c in cels]
        if not cels:
            continue
        while len(cels) > 1 and "[[" not in cels[0] and not clube(link(cels[0]), a):
            cels = cels[1:]   # coluna da posição ("{{0}}1.")
        m_nome = link(cels[0])
        m = clube(m_nome, a)
        if m is None:
            prob.append(f"linha sem cadastro: {m_nome}")
            continue
        vals = []
        for c in cels[1:]:
            c2 = re.sub(r"^[^|\[]*?(?:style|class|bgcolor|align)=[^|]*\|", "", c).strip()
            mm = re.search(r"(\d+)\s*:\s*(\d+)", c2)
            vals.append((int(mm.group(1)), int(mm.group(2))) if mm else None)
        if len(vals) != len(cab):
            prob.append(f"{m}: {len(vals)} células para {len(cab)} colunas")
            continue
        for v, pl in zip(cab, vals):
            if v == m:
                continue
            if pl is None:
                prob.append(f"{m} x {v}: célula sem placar")
                continue
            res[(m, v)] = pl
    return res, prob


def pagina(a):
    return wikitext("de", titulo(a))



def rebaixados_legenda(t, tb, a):
    """Clubes da legenda "Abstieg/Absteiger" (nomes depois de ':'); sem nomes, as linhas com a cor da legenda."""
    nomes, cores = set(), set()
    for cor, txt in legenda(t):
        if not re.search(r"Abstieg|Absteiger", txt) or re.search(r"Relegation", txt):
            continue
        txt2 = re.sub(r"\{\{0\|[^}]*\}\}", "", txt)
        if False:
            continue
        sem_links = re.sub(r"\[\[[^\]]*\]\]", "L", txt2)
        if ":" in sem_links:
            depois = re.sub(r"\[\[[^\]]*\]\]", lambda m: m.group(0).replace(":", "#DP#"), txt2)
            depois = depois.split(":", 1)[1].replace("#DP#", ":")
            depois = re.sub(r"\([^)]*\)", "", depois)
            for n in re.split(r",|\bund\b", depois):
                n = link(n).strip()
                if n:
                    c = clube(n, a)
                    nomes.add(c or ("?" + n))
        else:
            cores.add(cor)
    return nomes | {x["clube"] for x in tb if x["farbe"] in cores}
