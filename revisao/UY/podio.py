"""Bloco A: pódio (campeão, vice, 3º) do banco e do painel x Wikipédia en (lista de campeões, com 3º) e es (AUF).
Uso: python -I revisao/UY/podio.py > SCRATCH/UY/podio.txt"""
import json, re, sqlite3

ALIAS = {
    "CURCC": "Peñarol", "Peñarol": "Peñarol", "Nacional": "Nacional", "Albion": "Albion de Montevideo",
    "Montevideo Wanderers": "Montevideo Wanderers", "River Plate": "River Plate FC", "Universal": "Universal de Montevideo",
    "Rampla Juniors": "Rampla Juniors", "Bella Vista": "Bella Vista", "Cerro": "Cerro", "Defensor Sporting": "Defensor Sporting",
    "Defensor": "Defensor Sporting", "Danubio": "Danubio", "Central Español": "Central Español", "Progreso": "Progreso",
    "CA River Plate": "River Plate de Montevideo", "Liverpool": "Liverpool de Montevideo", "Rentistas": "Rentistas",
    "Racing": "Racing de Montevideo", "Rocha": "Rocha FC", "Plaza Colonia": "Plaza Colonia", "Cerrito": "Cerrito",
    "Uruguay Athletic": "Uruguay Athletic", "Deutscher": "Montevideo FC", "Cerro Largo": "Cerro Largo",
    "Deportivo Maldonado": "Deportivo Maldonado", "Boston River": "Boston River", "Fénix": "Fénix",
    "Sud América": "Sud América", "Huracán Buceo": "Huracán Buceo", "Lito": "Lito", "Charley": "Charley",
}


def nm(cel):
    cel = re.sub(r"\{\{small\|[^}]*\}\}|\{\{flagicon[^}]*\}\}|<ref.*?(</ref>|/>)|\{\{Refn.*", "", cel)
    m = re.search(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", cel)
    t = (m.group(2) or m.group(1)) if m else re.sub(r"'''|''", "", cel)
    t = t.strip()
    return ALIAS.get(t, t)


def en_lista():
    txt = open("data/coleta/uru-1/wikipedia/en_campeoes.txt", encoding="utf-8").read()
    t = txt[txt.index("===List of champions (1900–present)==="):txt.index("==Titles by club==")]
    out = {}
    for ln in re.split(r"\n\|-[^\n]*", t):
        cels = [c.strip() for c in re.split(r"\n\||\|\|", "\n" + ln.strip()) if c.strip()]
        for i, c in enumerate(cels):
            m = re.search(r"\[\[(\d{4}(?:–\d{2})?) Uruguayan Primera División[^|]*\|([^\]]+)\]\]", c)
            if m and i + 3 < len(cels):
                out[m.group(2).replace("–", "/")] = (nm(cels[i + 1]), nm(cels[i + 2]), nm(cels[i + 3]))
                break
            m = re.search(r"\[\[(2025|2026) Liga AUF Uruguaya\|", c)
            if m and i + 3 < len(cels):
                out[m.group(1)] = (nm(cels[i + 1]), nm(cels[i + 2]), nm(cels[i + 3]))
                break
    return out


def es_lista():
    import importlib.util, io, contextlib
    spec = importlib.util.spec_from_file_location("ce", "revisao/UY/campeoes_es.py")
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return {k.replace("-", "/"): v for k, v in mod.es.items()}


if __name__ == "__main__":
    EN, ES = en_lista(), es_lista()
    c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
    s = open("painel/dados/uru-1.js", encoding="utf-8").read()
    ED = json.loads(s[s.index("=") + 1:].strip().rstrip(";"))["ED"]
    eds = c.execute("""select temporada from edicao e join competicao co using(competicao_id)
                       where co.slug='uru-1' order by ano_inicio, temporada""").fetchall()
    tot = {"c": [0, 0], "v": [0, 0], "t": [0, 0]}
    for (temp,), p in zip(eds, ED):
        k = temp.split()[0] if temp.split()[-1] in ("AUF",) else temp
        en = EN.get(k)
        es = ES.get(k)
        if temp.endswith("FUF") or temp == "1926":
            en = es = None
        linha = [temp, p["campeao"], p["vice"], p["terceiro"]]
        marca = []
        if en:
            for j, (a, b) in enumerate(zip((p["campeao"], p["vice"], p["terceiro"]), en)):
                key = "cvt"[j]
                tot[key][1] += 1
                if a == b:
                    tot[key][0] += 1
                else:
                    marca.append(f"{key}:en={b}")
        if es and es[0] not in ("?", "—"):
            if es[0] != p["campeao"]:
                marca.append(f"c:es={es[0]}")
            if es[1] != p["vice"]:
                marca.append(f"v:es={es[1]}")
        print("\t".join(str(x) for x in linha), "\t", ("OK" if not marca else " ".join(marca)) if (en or es) else "sem fonte (FUF/1926 não estão na lista da AUF)")
    print("acertos x en (campeão, vice, 3º):", tot)
