"""Bloco B: classificação final do banco x tabelas das páginas da Wikipédia es de cada edição.
Lê as páginas guardadas pela coleta (data/coleta/uru-1/wikipedia/es_<ano>.txt, até 1993) e as baixadas pela revisão
(data/cache/revisao/UY/es_<ano>.txt, 1994 em diante). Para cada edição, acha a tabela es com os mesmos clubes e diz
(a) se alguma tabela es é igual à do banco e (b) a diferença para a tabela "anual"/geral (a de mais jogos).
Uso: python -I revisao/UY/tabelas_es.py > SCRATCH/UY/tabelas_es.txt"""
import os, re, sqlite3, unicodedata

c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
nome = dict(c.execute("select clube_id, nome from clube"))


def chave(t):
    t = unicodedata.normalize("NFD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", t)


# nomes das fontes -> clube do banco
ALIAS = {}
for cid, n in c.execute("""select distinct cl.clube_id, cl.nome from clube cl join classificacao_final cf using(clube_id)
                          join edicao e using(edicao_id) join competicao co using(competicao_id) where slug='uru-1'"""):
    ALIAS[chave(n)] = n
for cid, n in c.execute("""select cn.clube_id, cn.nome from clube_nome cn where clube_id in (select clube_id from classificacao_final cf
                          join edicao e using(edicao_id) join competicao co using(competicao_id) where slug='uru-1')"""):
    ALIAS.setdefault(chave(n), nome[cid])
MAN = {"curcc": "Peñarol", "centraluruguayrailwaycricketclub": "Peñarol", "defensor": "Defensor Sporting",
       "riverplate": None, "liverpool": "Liverpool de Montevideo", "racing": "Racing de Montevideo",
       "albion": "Albion de Montevideo", "universal": "Universal de Montevideo", "wanderers": "Montevideo Wanderers",
       "juventud": "Juventud de Las Piedras", "rocha": "Rocha FC", "torque": "Montevideo City Torque",
       "montevideocity": "Montevideo City Torque", "montevideocitytorque": "Montevideo City Torque",
       "atenas": "Atenas de San Carlos", "maldonado": "Deportivo Maldonado", "cerrolargo": "Cerro Largo",
       "tanquesisley": "El Tanque Sisley", "eltanquesisley": "El Tanque Sisley", "colon": "Colón de Montevideo",
       "belgrano": "Belgrano de Montevideo", "olimpia": "Olimpia de Montevideo", "libertad": "Libertad de Montevideo",
       "deutscher": "Montevideo FC", "teutonia": "Montevideo FC", "plaza": "Plaza Colonia", "plazacolonia": "Plaza Colonia",
       "bostonriver": "Boston River", "sudamerica": "Sud América", "miramarmisiones": "Miramar Misiones",
       "huracanbuceo": "Huracán Buceo", "paysandubellavista": "Paysandú Bella Vista", "fronterarivera": "Frontera Rivera",
       "deportivocolonia": "Deportivo Colonia", "paysandu": "Paysandú FC", "villaespanola": "Villa Española",
       "centralespanol": "Central Español", "central": "Central Español", "dublin": "Dublin", "uruguayonward": "Uruguay Onward",
       "laluz": "La Luz", "villateresa": "Villa Teresa", "cerrito": "Cerrito", "rentistas": "Rentistas",
       "tacuarembo": "Tacuarembó", "montevideo": "Montevideo FC", "uruguayathletic": "Uruguay Athletic",
       "rivera": "Frontera Rivera", "riverplatefc": "River Plate FC", "riverplatefootballclub": "River Plate FC"}


def clube(link, texto, ano):
    alvo = link or texto
    k = chave(texto)
    if "River Plate" in alvo:
        if "Football Club" in alvo or "F.C." in alvo or "FC" in texto or ano < 1930:
            return "River Plate FC"
        return "River Plate de Montevideo"
    if k in MAN and MAN[k]:
        return MAN[k]
    if k in ALIAS:
        return ALIAS[k]
    kl = chave(link or "")
    for a, b in MAN.items():
        if b and a and a in kl:
            return b
    return ALIAS.get(kl, texto)


def limpa(s):
    s = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", s, flags=re.S)
    s = re.sub(r"\[\[(Archivo|File|Imagen):[^\]]*\]\]", "", s)
    s = re.sub(r"\{\{(salió|subió|bajó|descendió|ascendió|Bandera[^}]*|bandera[^}]*|Escudo[^}]*)\}\}", "", s)
    return s


def tabelas(txt, ano):
    """devolve [(titulo, [(pos, clube, j, v, e, d, gp, gc, pts)])]"""
    txt = limpa(txt)
    out = []
    titulo = ""
    for bloco in re.split(r"(\n=+[^=\n]+=+\s*\n)", txt):
        if re.match(r"\n=+", bloco):
            titulo = bloco.strip().strip("=").strip()
            continue
        for tab in re.findall(r"\{\|.*?\n\|\}", bloco, flags=re.S):
            linhas = []
            for row in re.split(r"\n\|-[^\n]*", tab):
                m = re.search(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", row)
                if not m:
                    continue
                apos = row[m.end():]
                nums = re.findall(r"(?:^|\|\||\n\|)\s*(?:align=\w+\s*\|)?\s*'*([+\-−]?\d+)'*\s*(?=\|\||\n|$)", apos)
                nums = [int(x.replace("−", "-")) for x in nums]
                if len(nums) < 7:
                    continue
                pm = re.search(r"(\d+)\s*[º°]?", row[:m.start()].replace("'''", ""))
                pos = int(pm.group(1)) if pm else None
                j, v, e, d, gp, gc = nums[:6]
                pts = nums[7] if len(nums) >= 8 else nums[6]
                if v + e + d != j:
                    # formato com os pontos antes dos jogos: Pts PJ PG PE PP GF GC Dif
                    pts, j, v, e, d, gp, gc = nums[:7]
                    if v + e + d != j:
                        continue
                linhas.append((pos, clube(m.group(1), m.group(2) or m.group(1), ano), j, v, e, d, gp, gc, pts))
            if len(linhas) >= 4:
                out.append((titulo, linhas))
        # módulo {{#invoke:Football table}} (2021 em diante)
        for mod in re.findall(r"\{\{#invoke:Football table.*?\n\}\}", bloco, flags=re.S):
            nomes = {}
            for k, v in re.findall(r"\|nombre_(\w+)=([^\n]+)", mod):
                m2 = re.search(r"\{\{AUF\|([^}|]+)", v) or re.search(r"\[\[(?:[^\]|]+\|)?([^\]]+)\]\]", v)
                nomes[k] = m2.group(1).strip() if m2 else v.strip()
            ordem = re.search(r"\|orden_equipo=([^\n]+)", mod)
            if not ordem:
                continue
            linhas = []
            for k, cod in enumerate([x.strip() for x in ordem.group(1).split(",") if x.strip()], 1):
                g = lambda campo: int((re.search(rf"\|{campo}_{cod}=\s*(-?\d+)", mod) or [0, 0])[1])
                v, e, d, gp, gc = g("ganados"), g("empates"), g("perdidos"), g("gf"), g("gc")
                aj = re.search(rf"\|ajustar_puntos_{cod}=\s*([+-]?\d+)", mod)
                linhas.append((k, clube(None, nomes.get(cod, cod), ano), v + e + d, v, e, d, gp, gc,
                               v * 3 + e + (int(aj.group(1)) if aj else 0)))
            out.append((titulo + " (módulo)", linhas))
    return out


def pagina(temp):
    k = temp.replace("/", "-")
    for p in (f"data/coleta/uru-1/wikipedia/es_{k}.txt", f"data/cache/revisao/UY/es_{k}.txt"):
        if os.path.exists(p):
            return p, f"https://es.wikipedia.org/wiki/Campeonato_Uruguayo_de_Primera_Divisi%C3%B3n_{k}"
    return None, None


if __name__ == "__main__":
    eds = c.execute("""select edicao_id, temporada, ano_inicio from edicao e join competicao co using(competicao_id)
                       where slug='uru-1' order by ano_inicio, temporada""").fetchall()
    resumo = []
    for eid, temp, ano in eds:
        p, url = pagina(temp.split()[0] if temp.endswith("AUF") else temp)
        if temp.endswith("FUF") or temp == "1926" or not p:
            resumo.append((temp, "sem página es"))
            continue
        db = [(pos, nome[cid], j, v, e, d, gp, gc, pts) for pos, cid, j, v, e, d, gp, gc, pts in c.execute(
            """select posicao, clube_id, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, pontos
               from classificacao_final where edicao_id=? order by posicao""", (eid,))]
        clubes_db = {r[1] for r in db}
        tabs = [(t, l) for t, l in tabelas(open(p, encoding="utf-8").read(), ano) if {r[1] for r in l} == clubes_db]
        if not tabs:
            resumo.append((temp, f"nenhuma tabela es com os mesmos clubes ({url})"))
            continue
        igual = [t for t, l in tabs if [r[1:] for r in l] == [r[1:] for r in db]]
        igual_num = [t for t, l in tabs if {r[1:] for r in l} == {r[1:] for r in db}]
        geral = max(tabs, key=lambda x: (max(r[2] for r in x[1]), "anual" in x[0].lower() or "acumulad" in x[0].lower()))
        gt, gl = geral
        dif = []
        dpos = {r[1]: r for r in db}
        for k, r in enumerate(gl, 1):
            b = dpos.get(r[1])
            if b is None or b[2:] != r[2:] or b[0] != k:
                dif.append(f"{r[1]}: es {k}º {list(r[2:])} / banco {b[0] if b else '-'}º {list(b[2:]) if b else ''}")
        st = ("IGUAL à tabela es '" + igual[0] + "'") if igual else (
            "mesmos números, ordem diferente da tabela es '" + igual_num[0] + "'") if igual_num else "diferente de todas as tabelas es"
        resumo.append((temp, f"{st}; tabela es de mais jogos: '{gt}' (J={max(r[2] for r in gl)}), {len(dif)} linhas diferentes ({url})"))
        for x in dif:
            resumo.append((temp, "   " + x))
    for t, s in resumo:
        print(t, "|", s)
