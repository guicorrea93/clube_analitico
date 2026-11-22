"""FR: lê as páginas da Wikipédia fr (tabela 'foot classement' e grade 'Foot résultat').
Funções usadas por revisao/FR/comparar_frwiki.py."""
import json, os, re, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "coleta", "comum-europa"))
import clubes_fra as CL  # só leitura (cadastro da coleta)
CACHE = os.path.join(RAIZ, "data", "cache", "revisao", "FR")

MANUAL = {  # links da Wikipédia fr que o cadastro não reconhece -> chave do cadastro
    "Olympique lillois (football)": "Olympique Lillois Lille", "Olympique lillois": "Olympique Lillois Lille",
    "Racing Club de France (football)": "Racing Club de France", "Racing Club de France football": "Racing Club de France",
    "Racing Club de France football Colombes 92": "Racing Club de France", "Racing Club de Paris": "Racing Club de France",
    "Excelsior Athlétic Club de Roubaix": "Excelsior Roubaix", "Sporting Club nîmois": "SC Nimes", "Club français": "Club Francais",
    "Hyères Football Club": "Hyeres FC", "Football Club de Sète 34": "FC Sete", "Football Club de Sète": "FC Sete",
    "Sporting Club de Fives": "SC Fives Lille", "Club athlétique de Paris": "CA Paris (alt)", "Club Athlétique de Paris": "CA Paris (alt)",
    "Club athlétique de Paris-Charenton": "CA Paris (alt)",
    "Stade olympique montpelliérain": "Stade Olympique Montpellierain", "Olympique d'Alès": "Olympique Ales",
    "Olympique d'Alès en Cévennes": "Olympique Ales", "Football Club d'Antibes": "FC Antibes", "Olympique d'Antibes": "FC Antibes",
    "Racing Club de Roubaix": "RC Roubaix",
    "Red Star Football Club 93": "Red Star FC", "Red Star Football Club": "Red Star FC", "Red Star FC": "Red Star FC",
    "Club olympique Roubaix-Tourcoing": "CO Roubaix-Tourcoing", "Stade français (football)": "Stade Francais FC",
    "Stade français": "Stade Francais FC", "Association sportive Troyes-Savinienne": "AS Troyes-Savinienne",
    "Troyes Aube Football": "Troyes AF", "Espérance sportive Troyes Aube Champagne": "ESTAC Troyes",
    "Association sportive aixoise": "AS Aixoise", "Angoulême Charente Football Club": "AS Angouleme",
    "Association sportive de Béziers (football)": "AS Beziers", "Avenir sportif Béziers": "AS Beziers",
    "Sporting Toulon Var": "Sporting Toulon Var", "Toulouse Football Club (1937)": "Toulouse FC", "Toulouse Football Club": "Toulouse FC",
    "Stade lavallois Mayenne Football Club": "Stade Laval", "Stade lavallois": "Stade Laval", "Chamois niortais Football Club": "Chamois Niortais",
    "Limoges Football Club": "Limoges FC", "Tours Football Club": "Tours FC", "Football Club de Rouen 1899": "FC Rouen",
    "Football Club de Rouen": "FC Rouen", "Stade rennais football club": "Stade Rennes", "Stade de Reims": "Stade Reims",
    "Sports réunis Colmar": "SR Colmar", "Club sportif Sedan Ardennes": "CS Sedan", "Avignon Football 84": "Association Sportive Avignonaise",
    "Association sportive Avignon": "Association Sportive Avignonaise", "Le Havre Athletic Club": "Le Havre AC",
    "Le Havre Athletic Club (football)": "Le Havre AC", "Football Club de Gueugnon": "FC Gueugnon", "Football Club de Martigues": "FC Martigues",
    "Football Club d'Istres Ouest Provence": "FC Istres", "Football Club Istres Ouest Provence": "FC Istres",
    "La Berrichonne de Châteauroux": "LB Chateauroux", "Le Mans Football Club": "Le Mans UC 72", "Le Mans Union Club 72": "Le Mans UC 72",
    "Union sportive de Boulogne Côte d'Opale": "US Boulogne", "Athlétic Club Arles-Avignon": "AC Arles-Avignon",
    "Évian Thonon Gaillard Football Club": "Evian Thonon Gaillard", "Gazélec Football Club Ajaccio": "GFC Ajaccio",
    "Athletic Club Ajaccio": "AC Ajaccio", "Athletic Club ajaccien": "AC Ajaccio", "Athletic Club ajaccien football": "AC Ajaccio",
    "Grenoble Foot 38": "Grenoble Foot 38",
    "Football Club de Grenoble": "Grenoble Foot 38", "Clermont Foot 63": "Clermont Foot 63", "Clermont Foot Auvergne 63": "Clermont Foot 63",
    "Dijon Football Côte-d'Or": "Dijon FCO", "En avant Guingamp": "EA Guingamp", "En avant de Guingamp": "EA Guingamp",
    "Amiens Sporting Club": "Amiens SC", "Amiens SC": "Amiens SC", "Football Club Lorient-Bretagne Sud": "FC Lorient",
    "Football Club de Lorient": "FC Lorient", "Stade brestois 29": "Stade Brest", "Stade Malherbe Caen": "SM Caen",
    "Stade Malherbe de Caen": "SM Caen", "Paris Football Club": "Paris FC", "Football Club de Mulhouse": "FC Mulhouse",
    "Nîmes Olympique": "Nimes Olympique", "Montpellier Hérault Sport Club": "Montpellier HSC", "LOSC Lille": "Lille OSC",
    "LOSC Lille Métropole": "Lille OSC", "Lille OSC": "Lille OSC", "Association sportive Nancy-Lorraine": "AS Nancy",
    "Association sportive Nancy Lorraine": "AS Nancy",
    "Football Club de Nancy": "AS Nancy", "Association sportive de Cannes": "AS Cannes", "Association sportive de Cannes football": "AS Cannes",
    "Union athlétique Sedan-Torcy": "CS Sedan", "Racing Club Paris-Sedan": "CS Sedan", "Olympique lyonnais": "Olympique Lyon",
    "Lyon olympique universitaire": "Olympique Lyon", "Lyon Olympique universitaire": "Olympique Lyon",
    "Football Club des Girondins de Bordeaux": "Girondins Bordeaux", "Football Club de Metz": "FC Metz",
    "Racing Club de Strasbourg": "RC Strasbourg", "Racing Club de Strasbourg Alsace": "RC Strasbourg", "Racing Club de Lens": "RC Lens",
    "Sporting Club de Bastia": "SC Bastia", "Association sportive de Monaco football club": "AS Monaco",
    "Association sportive de Monaco Football Club": "AS Monaco", "Association sportive de Saint-Étienne": "AS Saint-Etienne",
    "Football Club de Nantes": "FC Nantes", "Football Club Sochaux-Montbéliard": "FC Sochaux",
    "Olympique Gymnaste Club Nice Côte d'Azur": "OGC Nice", "Olympique gymnaste club Nice Côte d'Azur": "OGC Nice",
    "Olympique Gymnaste Club de Nice": "OGC Nice", "Paris Saint-Germain Football Club": "Paris Saint-Germain",
    "Association de la jeunesse auxerroise": "AJ Auxerre", "Angers sporting club de l'Ouest": "Angers SCO",
    "Angers SCO": "Angers SCO", "Toulouse Football Club (1970)": "Toulouse FC", "Olympique de Marseille": "Olympique Marseille",
    "Stade rennais FC": "Stade Rennes", "Racing Pierrots Strasbourg Meinau": "RC Strasbourg",
    "Valenciennes Football Club": "Valenciennes FC", "Union sportive Valenciennes-Anzin": "Valenciennes FC",
    "Club sportif sedanais": "CS Sedan", "Football Club Lorient": "FC Lorient",
    "Stade français-Red Star": "Stade Francais FC", "Avenir Club Avignonnais": "Association Sportive Avignonaise",
    "Olympique avignonnais": "Association Sportive Avignonaise", "Racing Paris 1": "Racing Club de France",
}

_ESPACO = re.compile(r"[\s ]+")


def chave_link(cel, ano):
    c = _chave_link(cel, ano)
    if c == "Montpellier HSC" and ano < 1974:   # a Wikipédia fr liga o SO Montpellier à página do MHSC
        return "Stade Olympique Montpellierain"
    if c == "Red Star FC" and ano in (1948, 1949):   # Stade Français-Red Star (a coleta conta como Stade Français)
        return "Stade Francais FC"
    if c == "ESTAC Troyes" and ano < 1990:
        return "Troyes AF" if 1970 <= ano <= 1979 else "AS Troyes-Savinienne"
    return c


def _chave_link(cel, ano):
    cel = re.sub(r"\{\{[^{}]*\}\}", "", cel)
    for alvo, txt in re.findall(r"\[\[([^|\]]+)(?:\|([^\]]*))?\]\]", cel):
        alvo, txt = _ESPACO.sub(" ", alvo).strip(), _ESPACO.sub(" ", txt or "").strip()
        for n in (alvo, txt):
            if n in MANUAL:
                return MANUAL[n]
        for n in (alvo, txt):
            if n:
                c = CL.esd(n, ano)
                if c:
                    return c
    t = re.sub(r"\[\[|\]\]|'''|<[^>]+>", "", cel).strip()
    return MANUAL.get(t) or (CL.esd(t, ano) if t else None)


def campos(linha):
    """divide o conteúdo de {{...}} em campos de nível 0"""
    out, nivel, cur, i = [], 0, "", 0
    while i < len(linha):
        ch2 = linha[i:i + 2]
        if ch2 in ("{{", "[["):
            nivel += 1; cur += ch2; i += 2; continue
        if ch2 in ("}}", "]]"):
            nivel -= 1; cur += ch2; i += 2; continue
        if linha[i] == "|" and nivel == 0:
            out.append(cur); cur = ""; i += 1; continue
        cur += linha[i]; i += 1
    out.append(cur)
    return out


def modelos(txt, nome):
    """conteúdo de todas as ocorrências {{nome|...}} (com chaves aninhadas), na ordem"""
    res = []
    for m in re.finditer(r"\{\{\s*" + nome + r"\s*\|", txt, re.I):
        nivel, j = 0, m.start()
        while j < len(txt):
            if txt.startswith("{{", j):
                nivel += 1; j += 2; continue
            if txt.startswith("}}", j):
                nivel -= 1; j += 2
                if nivel == 0:
                    break
                continue
            j += 1
        res.append((m.start(), txt[m.end():j - 2]))
    return res


def num(s):
    s = re.sub(r"<ref.*?(?:/>|</ref>)|<[^>]+>|\{\{[^{}]*\}\}|'''|&nbsp;", "", s or "").strip()
    s = s.replace("−", "-").replace("–", "-")
    m = re.match(r"^-?\s*\d+", s)
    return int(m.group(0).replace(" ", "")) if m else None


NOMEADO = re.compile(r"^\s*[\wéèê ]+\s*=")


def tabelas(txt, ano):
    tabs, atual = [], None
    for ini, corpo in modelos(txt, "foot classement"):
        f = campos(corpo)
        nomeados, pos = {}, []
        for x in f:
            if NOMEADO.match(x) and not x.strip().startswith("[["):
                k, v = x.split("=", 1)
                nomeados[k.strip().lower()] = v
            else:
                pos.append(x)
        if len(pos) < 9:
            continue
        p = num(pos[0])
        if p is None:   # 1961/62: posição escrita com bgcolor dentro da célula
            nums = re.findall(r"\d+", re.sub(r"\{\{[^{}]*\}\}", "", pos[0]))
            if not nums:
                continue
            p = int(nums[-1])
            if "relégué" in pos[0]:
                nomeados["bgcolor"] = "{{fc|relégué}}"
        c = chave_link(pos[1], ano)
        vals = [num(x) for x in pos[2:9]]
        if atual is None or (atual and p <= atual[-1]["pos"]):
            atual = []
            tabs.append(atual)
        cor = nomeados.get("bgcolor", "")
        atual.append({"pos": p, "cel": re.sub(r"\s+", " ", pos[1].strip())[:70], "clube": c, "pts": vals[0], "j": vals[1],
                      "v": vals[2], "e": vals[3], "d": vals[4], "gp": vals[5], "gc": vals[6],
                      "bonus": num(nomeados.get("bonus")) if nomeados.get("bonus") else None,
                      "pen": nomeados.get("pen") or nomeados.get("pénalité") or nomeados.get("pénalités"),
                      "cor": cor.strip(), "relegue": "relégué" in cor and "barrage" not in cor, "ini": ini})
    return tabs


def grades(txt, ano):
    res = []
    partes = re.split(r"\{\{\s*Foot résultat début", txt)
    for bloco in partes[1:]:
        fim = bloco.find("Foot résultat fin")
        bloco = bloco[:fim if fim > 0 else len(bloco)]
        clubes, placares = [], []
        for _, corpo in modelos(bloco, "Foot résultat"):
            f = campos(corpo)
            clubes.append(chave_link(f[0], ano))
            placares.append([re.sub(r"<[^>]+>|\{\{[^{}]*\}\}", "", x).strip() for x in f[1:] if not NOMEADO.match(x)])
        if clubes:
            res.append((clubes, placares))
    return res


def pagina(ano):
    arq = os.path.join(CACHE, f"wiki_fr_Championnat_de_France_de_football_{ano}-{ano + 1}.json")
    if not os.path.exists(arq):
        return None
    j = json.load(open(arq, encoding="utf-8"))
    if "parse" not in j:
        return None
    return j["parse"]["wikitext"]["*"]
