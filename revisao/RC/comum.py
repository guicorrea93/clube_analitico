"""Funções comuns da reconferência RC (22/11/2026). Só leitura.
Banco: cópia do db/futebol.db de 22/11 09:13 no scratchpad (o agente 1 refaz o banco durante o dia).
Site: cópias de https://clubeanalitico.pages.dev/dados/<slug>.js em data/cache/revisao/RC/site/."""
import csv, json, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
SCR = r"C:\Users\GUILHE~1\AppData\Local\Temp\claude\c--Users-guilhermecorrea-Downloads-Gui-GitHub\a75361b9-f474-4b01-be59-ef64c90aa262\scratchpad"
DB = os.path.join(SCR, "RC", "futebol.db")
c = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
NOME = dict(c.execute("select clube_id, nome from clube"))
_js = {}
def js(slug, onde="site"):
    k = (slug, onde)
    if k not in _js:
        p = f"data/cache/revisao/RC/site/{slug}.js" if onde == "site" else f"painel/dados/{slug}.js"
        t = open(p, encoding="utf-8").read()
        _js[k] = json.loads(t[t.index("=") + 1:].strip().rstrip(";"))
    return _js[k]
def eds(slug, onde="site"):
    return {str(x["id"]): x for x in js(slug, onde)["EDS"]}
def ed_lista(slug, onde="site"):
    return js(slug, onde)["ED"]
def pac(slug, arq):
    return list(csv.DictReader(open(f"data/coleta/{slug}/pacote/{arq}.csv", encoding="utf-8")))
def q(sql, *a):
    return c.execute(sql, a).fetchall()
def eid(slug, temp):
    r = q("select e.edicao_id from edicao e join competicao co using(competicao_id) where co.slug=? and (e.temporada=? or e.chave=?)", slug, temp, temp)
    return r[0][0] if r else None
def jogos(slug, temp, clubes=None):
    r = q("""select e.temporada, f.nome, p.grupo, p.rodada, p.data, m.nome, p.gols_mandante, p.gols_visitante, v.nome,
           p.penaltis_mandante, p.penaltis_visitante, p.resultado_especial, p.observacao
           from partida p join edicao e using(edicao_id) join competicao co using(competicao_id) left join fase f using(fase_id)
           join clube m on m.clube_id=p.mandante_id join clube v on v.clube_id=p.visitante_id
           where co.slug=? and (e.temporada=? or e.chave=?) order by p.data, p.partida_id""", slug, temp, temp)
    if clubes:
        clubes = set(clubes)
        r = [x for x in r if (x[5] in clubes and x[8] in clubes)] if len(clubes) > 1 else [x for x in r if x[5] in clubes or x[8] in clubes]
    return r
def cf(slug, temp, cond="1=1"):
    return q(f"""select cf.posicao, cl.nome, cf.jogos, cf.vitorias, cf.empates, cf.derrotas, cf.gols_pro, cf.gols_contra, cf.pontos,
               cf.ajuste_pontos, cf.situacao from classificacao_final cf join clube cl using(clube_id) join edicao e using(edicao_id)
               join competicao co using(competicao_id) where co.slug=? and (e.temporada=? or e.chave=?) and {cond} order by cf.posicao""", slug, temp, temp)
def edicao(slug, temp):
    r = q("""select e.temporada, e.chave, cc.nome, vv.nome, e.num_clubes, e.pontos_vitoria, e.observacao from edicao e join competicao co using(competicao_id)
             left join clube cc on cc.clube_id=e.campeao_id left join clube vv on vv.clube_id=e.vice_id where co.slug=? and (e.temporada=? or e.chave=?)""", slug, temp, temp)
    return r[0] if r else None
def pac_jogos(slug, temp, clubes=None):
    r = [x for x in pac(slug, "partidas") if x["temporada"] == temp]
    if clubes:
        clubes = set(clubes)
        r = [x for x in r if (x["mandante"] in clubes and x["visitante"] in clubes)] if len(clubes) > 1 else [x for x in r if x["mandante"] in clubes or x["visitante"] in clubes]
    return r
def pj(x):
    return f"{x['data']} {x['fase']}/{x['grupo']} {x['mandante']} {x['gols_mandante']}x{x['gols_visitante']} {x['visitante']} {x.get('resultado_especial','')} pen={x.get('penaltis_mandante','')}-{x.get('penaltis_visitante','')}"
