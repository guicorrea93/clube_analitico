"""esp-1: critério de desempate (DE-002 no Espanhol).

1) Para cada temporada, quais critérios reproduzem a ordem final oficial (classificacao_final.csv do pacote):
   confronto (o da coleta), saldo, média.
2) Classificação rodada a rodada (Corrida): o pacote aplica o confronto direto com os jogos disputados até a rodada,
   mesmo quando os empatados ainda não se enfrentaram nos dois turnos. A regra espanhola (Wikipédia en, class_rules
   desde 2017/18; regulamento da RFEF) só usa o confronto direto depois de jogados todos os jogos entre eles; antes,
   saldo e gols pró. Conta as posições de rodada que mudam com essa regra.

Uso: python -I revisao/QE/desempate_esp.py  (na raiz do projeto)
"""
import csv
import sys
from collections import defaultdict

P = "data/coleta/esp-1/pacote/"


def ler(n):
    return list(csv.DictReader(open(P + n, encoding="utf-8")))


def tabela(jogos, pv):
    t = defaultdict(lambda: [0, 0, 0, 0, 0, 0, 0])
    for j in jogos:
        m, v, gm, gv = j["mandante"], j["visitante"], int(j["gols_mandante"]), int(j["gols_visitante"])
        if j.get("resultado_especial") == "wo":
            gm_, gv_ = (gm, gv)
        for c, gp, gc in ((m, gm, gv), (v, gv, gm)):
            x = t[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            x[6] += pv if gp > gc else 1 if gp == gc else 0
            x[1 if gp > gc else 2 if gp == gc else 3] += 1
    return t


def ordenar(t, aj, jogos, pv, modo):
    """modo: 'pacote' (confronto com o que houver), 'regra' (confronto só se completo), 'saldo', 'media'."""
    pts = lambda c: t[c][6] + aj.get(c, 0)
    geral = lambda c: (-(t[c][4] - t[c][5]), -t[c][4])
    if modo in ("saldo", "media"):
        if modo == "media":
            return sorted(t, key=lambda c: (-pts(c), -(t[c][4] / t[c][5] if t[c][5] else 9e9), -t[c][4]))
        return sorted(t, key=lambda c: (-pts(c), *geral(c)))
    g = defaultdict(list)
    for c in t:
        g[pts(c)].append(c)
    res = []
    for p in sorted(g, reverse=True):
        gr = g[p]
        if len(gr) > 1:
            entre = [j for j in jogos if j["mandante"] in gr and j["visitante"] in gr]
            completo = len(entre) >= len(gr) * (len(gr) - 1)
            if modo == "pacote" or completo:
                mini = tabela(entre, pv)
                gr.sort(key=lambda c: (-mini[c][6], -(mini[c][4] - mini[c][5]), *geral(c)))
            else:
                gr.sort(key=geral)
        res += gr
    return res


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ed = {e["temporada"]: e for e in ler("edicoes.csv")}
    part = defaultdict(list)
    for j in ler("partidas.csv"):
        if j["fase"] == "Liga":
            part[j["temporada"]].append(j)
    fin = defaultdict(list)
    for r in ler("classificacao_final.csv"):
        fin[r["temporada"]].append(r)
    crit = {f["temporada"]: f["criterio"] for f in ler("fases.csv") if f["ordem"] == "1"}
    rod = defaultdict(dict)
    for r in ler("classificacao_rodada.csv"):
        rod[r["temporada"]][(int(r["rodada"]), r["clube"])] = (int(r["posicao"]), r["zona"])

    print("== 1) critérios que reproduzem a ordem final oficial ==")
    for T in ed:
        if T == "1986/87":
            continue
        pv = int(ed[T]["pontos_vitoria"])
        js = part[T]
        aj = {r["clube"]: int(r["ajuste_pontos"] or 0) for r in fin[T]}
        t = tabela(js, pv)
        oficial = [r["clube"] for r in sorted(fin[T], key=lambda r: int(r["posicao"]))]
        ok = [m for m in ("pacote", "saldo", "media") if ordenar(t, aj, js, pv, m) == oficial]
        if ok != ["pacote", "saldo", "media"]:
            print(T, "reproduzem:", ok or "nenhum", "| pacote usa:", crit.get(T))

    print("\n== 2) Corrida: posições de rodada que mudam com a regra (confronto só depois dos dois jogos) ==")
    tot = 0
    tot_zona = 0
    exemplos = []
    por_temp = {}
    for T in ed:
        pv = int(ed[T]["pontos_vitoria"])
        js = part[T]
        aj = {r["clube"]: int(r["ajuste_pontos"] or 0) for r in fin[T]}
        nr = max(int(j["rodada"]) for j in js if j["rodada"])
        if T == "1986/87":
            nr = 34
        modo_final = "media" if "média" in crit.get(T, "") else "regra"
        n = 0
        nz = 0
        for r in range(1, nr + 1):
            ate = [j for j in js if j["rodada"] and int(j["rodada"]) <= r]
            t = tabela(ate, pv)
            nova = ordenar(t, aj, ate, pv, modo_final)
            for pos, c in enumerate(nova, 1):
                antes = rod[T].get((r, c))
                if antes and antes[0] != pos:
                    n += 1
                    if pos == 1 or antes[0] == 1:
                        nz += 1
                    exemplos.append(f"{T} rodada {r}: {c} pacote {antes[0]}º, regra {pos}º")
        if n:
            por_temp[T] = (n, nz)
        tot += n
        tot_zona += nz
    for T, (n, nz) in por_temp.items():
        print(f"{T}: {n} posições (líder trocado em {nz})")
    print(f"TOTAL {tot} posições de rodada em {len(por_temp)} temporadas; {tot_zona} envolvem o 1º lugar")
    with open("revisao/QE/desempate_esp_saida.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(exemplos))


if __name__ == "__main__":
    main()


def ordenar_esp(t, aj, jogos, pv, fora_ok=False, gm_ok=False, so_completo=False):
    """Confronto direto à espanhola: pontos entre os empatados, de novo entre os que seguem empatados (recursivo);
    depois saldo entre eles, gols fora entre eles (fora_ok) ou gols pró entre eles (gm_ok); por fim saldo e gols pró.
    so_completo: confronto só quando todos os jogos entre os empatados já foram jogados (classificação de rodada)."""
    pts = lambda c: t[c][6] + aj.get(c, 0)
    geral = lambda c: (-(t[c][4] - t[c][5]), -t[c][4])

    def rank(g):
        if len(g) == 1:
            return g
        jg = [j for j in jogos if j["mandante"] in g and j["visitante"] in g]
        if so_completo and len(jg) < len(g) * (len(g) - 1):
            return sorted(g, key=geral)
        mini = tabela(jg, pv)
        fora = defaultdict(int)
        for j in jg:
            fora[j["visitante"]] += int(j["gols_visitante"])
        sub = defaultdict(list)
        for c in g:
            sub[mini[c][6]].append(c)
        res = []
        for p in sorted(sub, reverse=True):
            s = sub[p]
            if len(s) < len(g):
                res += rank(s)
            else:
                res += sorted(s, key=lambda c: (-(mini[c][4] - mini[c][5]),
                                                -(fora[c] if fora_ok else mini[c][4] if gm_ok else 0), *geral(c)))
        return res
    g = defaultdict(list)
    for c in t:
        g[pts(c)].append(c)
    return [c for p in sorted(g, reverse=True) for c in rank(g[p])]
