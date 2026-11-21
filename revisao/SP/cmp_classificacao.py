"""Bloco B: classificação final do banco contra a tabela "Classificação final/geral" das páginas da Wikipédia pt.
Uso: python -I revisao/SP/cmp_classificacao.py 1909 1919 ... (temporadas do banco). Saída: revisao/SP/saida_classificacao.txt"""
import sys as _s; _s.stdout.reconfigure(encoding="utf-8")
import json, os, re, sqlite3, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baixar import wikitext
from listas_campeoes import limpa
from nomes import norm  # mapa de nomes
AQUI = os.path.dirname(os.path.abspath(__file__))
INFO = json.load(open(os.path.join(AQUI, "infobox.json"), encoding="utf-8"))
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)

from tabelas_wiki import tabelas


if __name__ == "__main__":
    out = []
    tot = {"edicoes": 0, "linhas": 0, "iguais": 0}
    for temp in sys.argv[1:]:
        k = temp if temp in INFO else temp.split(" ")[0]
        txt = wikitext(INFO[k]["titulo"], "pt")
        for pre in re.findall(r"\{\{(Tabela do Campeonato Paulista[^}|]*)\}\}", txt):
            txt += "\n== Classificação final ==\n" + wikitext("Predefinição:" + pre.strip(), "pt")
        tbs = tabelas(txt)
        # escolhe a tabela "final/geral" ou a maior
        cand = [t for t in tbs if re.search(r"(?i)classifica..o (final|geral)|geral", t[0])] or [t for t in tbs if re.search(r"(?i)final|geral|classifica", t[0])] or tbs
        if not cand:
            out.append(f"{temp}\tsem tabela lida"); continue
        tit, rows = max(cand, key=lambda t: (bool(re.search(r"(?i)geral|final", t[0])), len(t[1])))
        eid = c.execute("select edicao_id from edicao where competicao_id=7 and temporada=?", (temp,)).fetchone()[0]
        db = {r[1]: r for r in c.execute("""select posicao, cl.nome, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, pontos
                                          from classificacao_final join clube cl using(clube_id) where edicao_id=?""", (eid,))}
        tot["edicoes"] += 1
        out.append(f"== {temp}  (tabela wiki: '{tit}', {len(rows)} linhas; banco {len(db)} clubes)")
        for i, r in enumerate(rows, 1):
            nm = norm(r["nome"])
            b = db.get(nm)
            w = (i, r.get("j"), r.get("v"), r.get("e"), r.get("d"), r.get("gp"), r.get("gc"), r.get("pts"))
            tot["linhas"] += 1
            if not b:
                out.append(f"   {i:>2} {r['nome']:<24} wiki {w[1:]}  banco: NÃO ACHADO ({nm})"); continue
            bb = (b[0], b[2], b[3], b[4], b[5], b[6], b[7], b[8])
            ok = bb[1:7] == w[1:7] and bb[0] == i
            if ok: tot["iguais"] += 1
            out.append(f" {'  ' if ok else '≠ '}{i:>2} {nm:<24} wiki {w}  banco {bb}")
    out.append(str(tot))
    open(os.path.join(AQUI, "saida_classificacao.txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\n".join(out))
