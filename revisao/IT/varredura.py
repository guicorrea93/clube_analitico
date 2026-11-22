"""Varredura de coerência por edição: o que o painel mostra e salta aos olhos.
Só leitura do futebol.db. Uso: python -I revisao/tela/varredura.py > saida.txt"""
import re, sqlite3, sys
from collections import Counter, defaultdict

c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
ING = re.compile(r"\b(round|stage|phase|group|relegation|playoffs?|first|second|third|fourth|fifth|sixth|final round|quarter|semi-?finals?\b(?!.*fase)|to \d)", re.I)
COMPS = ["ita-1"]
nome = dict(c.execute("select clube_id, nome from clube"))
out = []
def acha(slug, ano, tipo, txt):
    out.append((slug, ano, tipo, txt))

for slug in COMPS:
    eds = c.execute("""select e.edicao_id, e.temporada, coalesce(e.chave,''), e.campeao_id, e.vice_id from edicao e
                       join competicao co using(competicao_id) where co.slug=? order by e.ano_inicio, e.chave""", (slug,)).fetchall()
    for eid, ano, chave, camp, vice in eds:
        rot = ano + ("" if chave in ("", ano) else f" ({chave})")
        fases = c.execute("select fase_id, ordem, nome, tipo from fase where edicao_id=? order by ordem", (eid,)).fetchall()
        jogos = c.execute("""select partida_id, fase_id, coalesce(grupo,''), data, mandante_id, visitante_id, gols_mandante, gols_visitante,
                             penaltis_mandante, penaltis_visitante, coalesce(resultado_especial,'') from partida where edicao_id=?""", (eid,)).fetchall()
        por_fase = defaultdict(list)
        for j in jogos: por_fase[j[1]].append(j)
        cf = c.execute("select posicao, clube_id from classificacao_final where edicao_id=? order by posicao", (eid,)).fetchall()
        top = [cid for _, cid in cf[:4]]
        pos = {cid: p for p, cid in cf}
        # 1. nomes de fase e grupo
        for fid, o, fn, ft in fases:
            if ING.search(fn) and not re.search(r"fase|final$|semifinal|quartas|oitavas", fn, re.I):
                acha(slug, rot, "fase em inglês", fn)
            gr = {j[2] for j in por_fase[fid] if j[2]}
            if any(g.lower().startswith("grupo") for g in gr):
                acha(slug, rot, "'Grupo Grupo'", f"{fn}: {sorted(gr)[:3]}...")
            if ft == "mata_mata" and len(gr) > 0 and not re.search(r"grupo", fn, re.I):
                pass
        # 2. ordem das fases x datas
        ini = []
        for fid, o, fn, ft in fases:
            ds = [j[3] for j in por_fase[fid] if j[3]]
            if ds: ini.append((o, fn, min(ds), max(ds)))
        for a, b in zip(ini, ini[1:]):
            if b[2] < a[2] and b[3] < a[3]:
                acha(slug, rot, "fase fora de ordem", f"'{b[1]}' ({b[2]}..{b[3]}) vem depois de '{a[1]}' ({a[2]}..{a[3]})")
        # 3. fase chamada Final
        for fid, o, fn, ft in fases:
            if re.fullmatch(r"(?i)\s*(grande\s+)?final(\s+.*)?", fn) and "fase" not in fn.lower():
                js = por_fase[fid]; cl = {x for j in js for x in (j[4], j[5])}
                if len(js) > 3 or len(cl) > 2:
                    acha(slug, rot, "Final com jogos demais", f"'{fn}': {len(js)} jogos, {len(cl)} clubes")
        # 4. decisão: jogos da última data da edição
        datas = sorted(j[3] for j in jogos if j[3])
        if datas and len(fases) > 1:
            ult_fase = max(fases, key=lambda f: max([j[3] or "" for j in por_fase[f[0]]] or [""]))
            js = por_fase[ult_fase[0]]
            cl = {x for j in js for x in (j[4], j[5])}
            if len(cl) == 2:
                if camp not in cl or (vice and vice not in cl):
                    acha(slug, rot, "pódio x final", f"última fase '{ult_fase[2]}' = {sorted(nome[x] for x in cl)}; campeão {nome.get(camp)}, vice {nome.get(vice)}")
                if top[:2] and set(top[:2]) != cl:
                    acha(slug, rot, "classificação x final", f"1º-2º {[nome[x] for x in top[:2]]}, final {sorted(nome[x] for x in cl)}")
            elif len(cl) == 4 and ult_fase[3] != "mata_mata":
                if set(top) != cl:
                    acha(slug, rot, "classificação x fase final", f"1º-4º {[nome[x] for x in top]}, fase final '{ult_fase[2]}' {sorted(nome[x] for x in cl)}")
        # 5. semifinal (copa e mata-mata): semifinalistas em 3º-4º
        for fid, o, fn, ft in fases:
            if re.fullmatch(r"(?i)semi-?finais?|semifinal", fn.strip()):
                cl = {x for j in por_fase[fid] for x in (j[4], j[5])}
                fora = [f"{nome[x]} ({pos.get(x)}º)" for x in cl if pos.get(x, 99) > 4]
                if len(cl) == 4 and fora:
                    acha(slug, rot, "semifinalista fora do top 4", ", ".join(fora))
        # 6. jogos estranhos
        for j in jogos:
            if j[4] == j[5]:
                acha(slug, rot, "clube contra ele mesmo", f"{nome[j[4]]} {j[6]}x{j[7]} em {j[3]}")
        dup = Counter((j[3], j[4], j[5]) for j in jogos if j[3])
        for (d, m, v), n in dup.items():
            if n > 1: acha(slug, rot, "jogo repetido", f"{nome[m]} x {nome[v]} em {d} ({n}x)")
        dia = Counter((j[3], x) for j in jogos if j[3] for x in (j[4], j[5]))
        for (d, x), n in dia.items():
            if n > 1: acha(slug, rot, "clube 2 jogos no mesmo dia", f"{nome[x]} em {d} ({n} jogos)")
        # 7. classificação x quem jogou
        jogaram = {x for j in jogos for x in (j[4], j[5])}
        noclass = set(pos)
        if jogaram - noclass: acha(slug, rot, "jogou e não está na classificação", ", ".join(sorted(nome[x] for x in jogaram - noclass))[:200])
        if noclass - jogaram: acha(slug, rot, "na classificação sem jogar", ", ".join(sorted(nome[x] for x in noclass - jogaram))[:200])
        if cf and camp and pos.get(camp) != 1: acha(slug, rot, "campeão não é 1º", f"{nome[camp]} em {pos.get(camp)}º")
        ps = [p for p, _ in cf]
        if ps and (len(set(ps)) != len(ps)): acha(slug, rot, "posição repetida", str([p for p, n in Counter(ps).items() if n > 1]))
        # 8. empate em mata-mata de jogo único sem pênaltis
        for fid, o, fn, ft in fases:
            if ft == "mata_mata":
                for j in por_fase[fid]:
                    pass

for slug, ano, tipo, txt in out:
    print(f"{slug}\t{ano}\t{tipo}\t{txt}")
print(Counter((s, t) for s, _, t, _ in out), file=sys.stderr)
