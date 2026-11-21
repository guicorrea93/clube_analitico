"""Artilheiro de cada edição do arg-1 (banco) x 'List of Argentine Primera División top scorers' (Wikipédia en).
Compara o número de gols do artilheiro e o sobrenome. Saída: revisao/AR/cmp_artilheiros_saida.txt"""
import re, sys, sqlite3, unicodedata
sys.path.insert(0, "revisao/AR"); import baixar
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
def sem(x): return unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode().lower()
t = baixar.wikitext("en", "List of Argentine Primera División top scorers")
def rotulo_para_temporada(lab):
    lab = re.sub(r"<[^>]*>", "", lab).strip()
    m = re.match(r"(\d{4})\s*(.*)$", lab); y = int(m.group(1)); r = m.group(2).strip()
    if re.match(r"[-–]\d\d", r): return f"{y}/{r[-2:]}"
    if 1912 <= y <= 1914: return f"{y} Federación" if r == "FAF" else f"{y} Asociación"
    if 1919 <= y <= 1926: return f"{y} Amateurs" if r.startswith("AAm") else f"{y} Asociación"
    if 1931 <= y <= 1934: return f"{y} Liga" if r == "LAF" else f"{y} Asociación"
    if y == 1936: return "1936 Copa de Honor" if "CH" in r else "1936 Campeonato"
    if r == "Met": return f"{y} Metropolitano"
    if r == "Nac": return f"{y} Nacional"
    if r == "Ap": return f"{y}/{str(y + 1)[-2:]} Apertura" if y < 2025 else f"{y} Apertura"
    if r == "Cl": return f"{y - 1}/{str(y)[-2:]} Clausura"
    if r == "In": return f"{y}/{str(y + 1)[-2:]} Inicial"
    if r == "Fi": return f"{y - 1}/{str(y)[-2:]} Final"
    return str(y)
en = {}
for r in re.split(r"\n\|-[^\n]*", t):
    m = re.match(r"\s*\|\s*(?:rowspan=\d+\s*\|)?\s*\[\[[^\]|]*\|([^\]]*)\]\]", r)
    if not m: continue
    try: temp = rotulo_para_temporada(m.group(1))
    except Exception: continue
    corpo = re.sub(r"\{\{refn.*?\}\}(?=\s*\|\|)", "", r[m.end():], flags=re.S)
    cel = [x.strip() for x in corpo.split("||")]
    cel = [x for x in cel if x != ""]
    if len(cel) < 3: continue
    jog = [re.sub(r"\{\{[^}]*\}\}|\[\[[^\]|]*\||\]\]|\[\[|\(\d+\)|<[^>]*>", "", x).strip() for x in re.split(r"<br\s*/?>", cel[0])]
    gols = re.findall(r"\b(\d{1,2})\b", re.sub(r"\{\{[^}]*\}\}", lambda k: k.group(0) if "center" not in k.group(0) else k.group(0), cel[2]))
    if not gols: continue
    if temp in en and temp == "1982 Metropolitano": temp = "1982 Nacional"
    en[temp] = (jog, int(gols[0]))
eds = c.execute("""select e.edicao_id, e.temporada from edicao e join competicao co using(competicao_id) where slug='arg-1' order by ano_inicio, edicao_id""").fetchall()
ok = 0; dif = []; sem_en = []; n = 0
for eid, temp in eds:
    art = c.execute("select a.jogador, a.gols, cl.nome from artilheiro a left join clube cl using(clube_id) where edicao_id=? order by gols desc", (eid,)).fetchall()
    if temp not in en:
        sem_en.append(temp); continue
    jog, g = en[temp]
    if not art:
        dif.append(f"{temp}\tbanco: sem artilheiro\ten: {', '.join(jog)} {g}"); continue
    n += 1
    top = [a for a in art if a[1] == art[0][1]]
    sob = lambda x: sem(x).replace(".", " ").split()[-1] if x.strip() else ""
    nomes_ok = any(sob(a[0]) in [sob(j) for j in jog] for a in top)
    if top[0][1] == g and nomes_ok: ok += 1
    else: dif.append(f"{temp}\tbanco: {'; '.join(f'{a[0]} ({a[2]}) {a[1]}' for a in top)}\ten: {', '.join(jog)} {g}")
out = [f"artilheiros conferidos: {n}; iguais (gols e sobrenome): {ok}", "Diferenças:"] + dif + ["Edições sem linha na en: " + ", ".join(sem_en)]
open("revisao/AR/cmp_artilheiros_saida.txt", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out))
