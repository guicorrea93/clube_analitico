"""Funções comuns da reconferência (RV). Só leitura."""
import json, sqlite3
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
NOME = dict(c.execute("select clube_id, nome from clube"))
def js(slug):
    t = open(f"painel/dados/{slug}.js", encoding="utf-8").read()
    return json.loads(t[t.index("=") + 1:].strip().rstrip(";"))
def eds(slug):
    d = js(slug); return d, {x["id"]: x for x in d["EDS"]}
def edicao(slug, temp):
    return c.execute("""select e.* from edicao e join competicao co using(competicao_id) where co.slug=? and (e.temporada=? or e.chave=?)""", (slug, temp, temp)).fetchall()
def jogos(slug, temp, clubes=None):
    q = """select e.temporada, coalesce(e.chave,''), f.nome, p.grupo, p.rodada, p.data, m.nome, p.gols_mandante, p.gols_visitante, v.nome,
           p.penaltis_mandante, p.penaltis_visitante, p.resultado_especial, p.observacao
           from partida p join edicao e using(edicao_id) join competicao co using(competicao_id) join fase f using(fase_id)
           join clube m on m.clube_id=p.mandante_id join clube v on v.clube_id=p.visitante_id
           where co.slug=? and (e.temporada=? or e.chave=?) order by p.data, p.partida_id"""
    r = c.execute(q, (slug, temp, temp)).fetchall()
    if clubes: r = [x for x in r if x[6] in clubes and x[9] in clubes] if len(clubes) > 1 else [x for x in r if x[6] in clubes or x[9] in clubes]
    return r
def tab(d, id_):
    return d[id_]["tab"]
