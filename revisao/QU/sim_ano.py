"""Simula a correção em lote do ano das datas do arg-1 (AR-022) e mede o resultado. Só leitura.

Regra proposta (regra 3: janela da temporada + data mais perto da anterior), a aplicar em coleta/arg-1/importar.py depois de ler os jogos de cada edição:
  - âncora = ano_fim se a temporada é um Clausura/Final de temporada dividida, senão ano_inicio;
  - início = dia/mês do 1º jogo da edição na ordem da página (rodada 1), com 30 dias de folga;
  - cada jogo recebe o ano da âncora se o dia/mês é >= início-30d, senão âncora+1 (temporadas têm menos de 12 meses);
  - exceções com data escrita à mão (CORRIGE "data"), ex.: 1939 desempate do 2º lugar em 09/11/1941.
Mede: quantas datas mudam; % no fim de semana antes/depois; concordância com as datas do historiadeboca (cmp_hdb_jogos.tsv).
Uso: python -I revisao/QU/sim_ano.py -> revisao/QU/sim_ano_saida.txt e sim_ano_mudancas.tsv
"""
import re, sys, sqlite3, datetime as dt
from pathlib import Path
from collections import defaultdict, Counter

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = Path(__file__).resolve().parent.parent.parent
FOLGA = 30
# edições que passam de 12 meses: ficam como estão (datas conferidas pelo dia da semana na 2ª rodada) ou levam data à mão
EXCECOES = {"1922 Amateurs", "1923 Asociación"}
# só as edições da lista do AR-022 (revisao/AR/datas_ano_lista.txt)
LISTA = {"1919 Asociación", "1919 Amateurs", "1924 Asociación", "1925 Asociación", "1927", "1928", "1929", "1930", "1931 Liga",
         "1937", "1977 Nacional", "1981 Nacional", "1985/86", "1986/87", "1989/90", "1999/00 Apertura", "2003/04 Apertura",
         "2006/07 Apertura", "2007/08 Apertura", "2010/11 Apertura", "2011/12 Apertura", "2012/13 Inicial", "2017/18", "2018/19",
         "2019/20"}
# temporadas de mais de 12 meses: último dia (do historiadeboca: último jogo do Boca + folga)
FIM = {"1927": "1928-01-31", "1928": "1929-07-31", "1930": "1931-04-30", "1937": "1939-02-28"}


def ancora(temp, a0, a1):
    if re.search(r"Clausura|\bFinal$|Campeonato$", temp) and "/" in temp:
        return a1
    return a0


def ordem(fid):
    m = re.match(r"rsssf:([^:]+):(\d+)", fid or "")
    return (m.group(1), int(m.group(2))) if m else ("~", 0)


def main():
    c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
    nome = dict(c.execute("select clube_id, nome from clube"))
    eds = c.execute("""select e.edicao_id, e.temporada, e.ano_inicio, e.ano_fim from edicao e join competicao co using(competicao_id)
                       where co.slug='arg-1' order by e.ano_inicio, e.edicao_id""").fetchall()
    novo = {}
    linhas, mud = [], ["temporada\tdata_banco\tdata_nova\tjogo\tfonte_id"]
    tot = Counter()
    for eid, temp, a0, a1 in eds:
        js = c.execute("select partida_id, data, mandante_id, visitante_id, fonte_id, coalesce(resultado_especial,'') from partida where edicao_id=?", (eid,)).fetchall()
        # ordem da página: a do trecho (as páginas aparecem na ordem dos trechos; dentro, pela linha)
        pags = []
        for r in js:
            p = ordem(r[4])[0]
            if p not in pags:
                pags.append(p)
        js.sort(key=lambda r: (pags.index(ordem(r[4])[0]), ordem(r[4])[1]))
        com = [r for r in js if r[1]]
        if not com or temp in EXCECOES:
            continue
        anc = ancora(temp, a0, a1)
        if temp not in LISTA:
            for pid, d, *_ in com:
                novo[pid] = d
            continue
        d0 = com[0][1]
        ini = dt.date(anc, int(d0[5:7]), int(d0[8:10])) - dt.timedelta(days=FOLGA)
        fim = dt.date.fromisoformat(FIM[temp]) if temp in FIM else ini + dt.timedelta(days=365)
        prev = None
        antes = depois = 0; n = 0; muda = 0
        for pid, d, m, v, fid, esp in com:
            try:
                x = dt.date.fromisoformat(d)
            except ValueError:
                x = None
            mo, di = int(d[5:7]), int(d[8:10])
            cands = []
            for y in range(ini.year, fim.year + 1):
                try:
                    w = dt.date(y, mo, di)
                except ValueError:
                    continue
                if ini <= w <= fim:
                    cands.append(w)
            if not cands:
                z = x
            elif len(cands) == 1 or prev is None:
                z = cands[0]
            else:
                z = min(cands, key=lambda w: (abs((w - prev).days), w.weekday() < 5))
            if z is not None:
                prev = z
            nd = z.isoformat() if z else d
            novo[pid] = nd
            if esp in ("wo", "n/p"):
                continue
            n += 1
            if x: antes += x.weekday() >= 5
            if z: depois += z.weekday() >= 5
            if nd != d:
                muda += 1
                mud.append(f"{temp}\t{d}\t{nd}\t{nome[m]} x {nome[v]}\t{fid}")
        tot["jogos"] += n; tot["muda"] += muda; tot["fds_antes"] += antes; tot["fds_depois"] += depois
        if muda:
            linhas.append(f"{temp:22s} {muda:4d} de {n:4d} mudam | fim de semana antes {antes / n:.0%} depois {depois / n:.0%}")
    # concordância com o historiadeboca
    hdb = (RAIZ / "revisao" / "QU" / "cmp_hdb_jogos.tsv").read_text(encoding="utf-8").splitlines()[1:]
    fid_pid = {}
    for pid, fid in c.execute("select p.partida_id, p.fonte_id from partida p join edicao e using(edicao_id) join competicao co using(competicao_id) where co.slug='arg-1'"):
        fid_pid[fid] = pid
    k = Counter(); difs = []
    for l in hdb:
        temp, dh, jh, db, jb, pl, sd, fid = l.split("\t")
        pid = fid_pid.get(fid)
        if not pid or not dh:
            continue
        k["n"] += 1
        k["antes"] += db == dh
        k["depois"] += novo.get(pid, db) == dh
        if novo.get(pid, db) != dh:
            k["dif_depois"] += 1
            difs.append(f"   {temp}: historiadeboca {dh} | banco {db} | nova {novo.get(pid, db)} | {jh} | {fid}")
    linhas.append(f"\nTOTAL: {tot['muda']} de {tot['jogos']} datas mudam; fim de semana {tot['fds_antes'] / tot['jogos']:.1%} -> {tot['fds_depois'] / tot['jogos']:.1%}")
    linhas.append(f"historiadeboca (jogos do Boca, {k['n']}): data igual antes {k['antes']} ({k['antes'] / k['n']:.1%}), depois {k['depois']} ({k['depois'] / k['n']:.1%})")
    linhas.append("Jogos do Boca que ainda diferem do historiadeboca depois da regra:")
    linhas += difs
    (RAIZ / "revisao" / "QU" / "sim_ano_saida.txt").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    (RAIZ / "revisao" / "QU" / "sim_ano_mudancas.tsv").write_text("\n".join(mud) + "\n", encoding="utf-8")
    print("\n".join(linhas))


if __name__ == "__main__":
    main()
