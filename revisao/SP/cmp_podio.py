"""Bloco A: campeão, vice e 3º de cada edição (banco e painel) contra as listas da Wikipédia en e pt.
Saída: revisao/SP/saida_podio.txt"""
import sys as _s; _s.stdout.reconfigure(encoding="utf-8")
import json, os, re, sqlite3, unicodedata
from collections import defaultdict

AQUI = os.path.dirname(os.path.abspath(__file__))
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
L = json.load(open(os.path.join(AQUI, "listas_campeoes.json"), encoding="utf-8"))
s = open("painel/dados/bra-sp-1.js", encoding="utf-8").read()
P = json.loads(s[s.index("=") + 1:].strip().rstrip(";"))

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nomes import MAPA, chave, norm


def rot(temp):
    return temp


eds = c.execute("""select e.edicao_id, e.temporada, e.ano_inicio, c1.nome, c2.nome from edicao e
  left join clube c1 on c1.clube_id=e.campeao_id left join clube c2 on c2.clube_id=e.vice_id
  where competicao_id=7 order by ano_inicio, temporada""").fetchall()
pos = {}
for eid, *_ in eds:
    pos[eid] = [r[0] for r in c.execute("""select cl.nome from classificacao_final cf join clube cl using(clube_id)
                                          where edicao_id=? order by posicao limit 4""", (eid,))]
LIGA = {"LFP": "LPF"}
def idx(lista):
    d = defaultdict(list)
    for x in lista:
        d[(x["ano"], LIGA.get(x["liga"], x["liga"]))].append(x)
    return d
EN, PT = idx(L["en"]), idx(L["pt"])
painel = {}
for e in P["ED"]:
    painel[(e["ano"], e.get("comp") or "")] = e

out = []
cont = defaultdict(int)
anos_db = set()
for eid, temp, ano, camp, vice in eds:
    liga = temp.split(" ")[1] if " " in temp else ""
    anos_db.add((ano, liga))
    k = (ano, liga) if liga else None
    def pega(D):
        if liga:
            return D.get((ano, liga), [])
        # ano com uma liga só: pega as linhas do ano que não são FPF amadora de 1933/34
        r = [x for (a, l), xs in D.items() if a == ano for x in xs]
        if ano in (1933, 1934):
            r = [x for x in r if x["liga"] == "APEA"]
        return r
    en, pt = pega(EN), pega(PT)
    pe = painel.get((ano, liga)) or painel.get((ano, ""))
    linha = [temp]
    # campeão
    camps_en = {norm(x["campeao"]) for x in en}
    camps_pt = {norm(x["campeao"]) for x in pt if x["campeao"]}
    vices_en = {norm(x["vice"]) for x in en}
    vices_pt = {norm(x["vice"]) for x in pt if x["vice"] not in ("—", "", "–")}
    terc_pt = {norm(x["terceiro"]) for x in pt if x.get("terceiro") not in (None, "", "—", "–")}
    cont["ed"] += 1
    ok_c = camp in camps_en and (not camps_pt or camp in camps_pt)
    if len(camps_en | camps_pt) > 1:
        out.append(f"{temp}\tCAMPEÃO DIVIDIDO\tbanco {camp}\ten {sorted(camps_en)} pt {sorted(camps_pt)}")
    elif not ok_c:
        out.append(f"{temp}\tCAMPEÃO\tbanco {camp}\ten {sorted(camps_en)} pt {sorted(camps_pt)}")
    else:
        cont["camp_ok"] += 1
    ok_v = vice in vices_en or vice in vices_pt
    if not ok_v:
        out.append(f"{temp}\tVICE\tbanco {vice}\ten {sorted(vices_en)} pt {sorted(vices_pt)}")
    else:
        cont["vice_ok"] += 1
        if len(vices_en | vices_pt) > 1:
            out.append(f"{temp}\tVICE (dois na fonte)\tbanco {vice}\ten {sorted(vices_en)} pt {sorted(vices_pt)}")
    t3 = pos[eid][2] if len(pos[eid]) > 2 else None
    if terc_pt:
        cont["terc_conf"] += 1
        if t3 not in terc_pt:
            out.append(f"{temp}\t3º\tbanco {t3}\tpt {sorted(terc_pt)}")
        else:
            cont["terc_ok"] += 1
    # painel x banco
    if pe:
        if pe["campeao"] != camp or pe["vice"] != vice or pe.get("terceiro") != t3:
            out.append(f"{temp}\tPAINEL≠BANCO\tpainel {pe['campeao']}/{pe['vice']}/{pe.get('terceiro')}\tbanco {camp}/{vice}/{t3}")
    else:
        out.append(f"{temp}\tsem linha no painel")
    if pos[eid] and pos[eid][0] != camp:
        out.append(f"{temp}\tcampeão não é 1º na classificação\t{pos[eid][:2]}")
    if pos[eid] and len(pos[eid]) > 1 and pos[eid][1] != vice:
        out.append(f"{temp}\tvice não é 2º na classificação\t{pos[eid][:2]}")

for (a, l), xs in sorted(EN.items()):
    if (a, l) not in anos_db and (a, "") not in anos_db:
        out.append(f"{a} {l}\tEDIÇÃO SÓ NA FONTE\ten {[x['campeao'] for x in xs]}")
open(os.path.join(AQUI, "saida_podio.txt"), "w", encoding="utf-8").write("\n".join(out) + "\n" + str(dict(cont)) + "\n")
print("\n".join(out)); print(dict(cont))
