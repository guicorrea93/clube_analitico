"""Pacote por-1 x Transfermarkt (fonte que a coleta NÃO usou): placar e data jogo a jogo, todas as temporadas.
Jogo casado por temporada + mandante + visitante (par único no turno e returno).
Uso (na raiz): python -I revisao/PT/cmp_tm.py > SCRATCH/PT/cmp_tm.txt"""
import sys, pathlib, json
from collections import defaultdict, Counter
from datetime import date
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding="utf-8")
import tm, ptw
from comum import partidas

TM_NOMES = {  # título do Transfermarkt -> chave (o que o cadastro não resolve)
    "SL Benfica": "Benfica", "FC Porto": "Porto", "Sporting CP": "Sporting", "CF Os Belenenses": "Belenenses",
    "Vitória Setúbal FC": "Vitória de Setúbal", "Vitória Guimarães SC": "Vitória de Guimarães", "Académica Coimbra": "Académica",
    "Académico FC": "Académico do Porto", "Boavista FC": "Boavista", "Leixões SC": "Leixões", "FC Barreirense": "Barreirense",
    "Casa Pia AC": "Casa Pia", "SC Olhanense": "Olhanense", "Leça FC": "Leça", "GD CUF Barreiro": "CUF", "Atlético CP": "Atlético CP",
    "SC Salgueiros": "Salgueiros", "GD Estoril Praia": "Estoril", "UD Oliveirense": "Oliveirense", "FC Famalicão": "Famalicão",
    "AD Sanjoanense": "Sanjoanense", "SC Braga": "Braga", "O Elvas CAD": "O Elvas", "Lusitano FC VRSA": "Lusitano VRSA",
    "Lusitano GC Évora": "Lusitano de Évora", "SC Covilhã": "Sporting da Covilhã", "Clube Oriental de Lisboa": "Oriental de Lisboa",
    "SCU Torreense": "Torreense", "Caldas SC": "Caldas SC", "SC Beira-Mar": "Beira-Mar", "CD Feirense": "CD Feirense",
    "Varzim SC": "Varzim", "Seixal FC": "Seixal", "FC Tirsense": "Tirsense", "União de Tomar": "União de Tomar", "SC Farense": "Farense",
    "CD Montijo": "Montijo", "União Coimbra": "União de Coimbra", "SC Espinho": "Espinho", "Portimonense SC": "Portimonense",
    "GD Riopele": "Riopele", "CS Marítimo": "Marítimo", "Rio Ave FC": "Rio Ave", "União Leiria": "União de Leiria", "Amora FC": "Amora",
    "FC Penafiel": "Penafiel", "GC Alcobaça": "Ginásio de Alcobaça", "RD Águeda": "Recreio de Águeda", "FC Vizela": "Vizela",
    "CD Aves": "Desportivo das Aves", "GD Chaves": "Chaves", "CD Nacional": "Nacional da Madeira", "CF Estrela Amadora": "Estrela da Amadora",
    "AD Fafe": "Fafe", "CF União Madeira": "União da Madeira", "Gil Vicente FC": "Gil Vicente", "FC Paços de Ferreira": "Paços de Ferreira",
    "FC Felgueiras": "Felgueiras", "SC Campomaiorense": "Campomaiorense", "FC Alverca": "Alverca", "CD Santa Clara": "Santa Clara",
    "Moreirense FC": "Moreirense", "Naval 1º de Maio": "Naval 1º de Maio", "CD Trofense": "Trofense", "FC Arouca": "Arouca",
    "CD Tondela": "Tondela", "AVS Futebol SAD": "AVS", "Belenenses SAD": "Belenenses SAD", "B SAD": "Belenenses SAD",
    "Uniao Foot-Ball Lissabon": "União de Lisboa", "CF Unidos": "Unidos de Lisboa", "Lusitano FC Vila Real de Santo António": "Lusitano VRSA",
    "Clube Oriental Lissabon": "Oriental de Lisboa", "Lusitano Évora GC": "Lusitano de Évora", "SC União Torreense": "Torreense",
    "União FCI de Tomar": "União de Tomar",
}


def chave(nome, a):
    # erros de identidade do Transfermarkt (anotados em SCRATCH/fontes_PT.md)
    if nome == "Vitória Guimarães SC" and a in (1935, 1936):
        return "Vitória de Setúbal"      # o TM põe o Vitória de Guimarães no lugar do de Setúbal
    if nome == "O Elvas CAD" and a <= 1946:
        return "SL Elvas"                # o TM junta o SL Elvas (1945-47) ao O Elvas
    if nome == "Académico FC" and a == 1941:
        return None                      # o TM junta Académica e Académico do Porto em 1941/42
    if nome in TM_NOMES:
        c = TM_NOMES[nome]
        if c == "Belenenses" and 2018 <= a <= 2021:
            return "Belenenses SAD"
        return c
    return ptw.chave_clube([nome], a)


if __name__ == "__main__":
    P = defaultdict(dict)
    for j in partidas():
        P[j["a"]][(j["mandante"], j["visitante"])] = j
    sem = Counter(); tot = Counter(); dec = defaultdict(Counter); lista_datas = []
    for a in sorted(P):
        T = next(iter(P[a].values()))["temporada"]
        url = tm.URL.format(a=a)
        js = tm.jogos(a)
        vistos = set()
        for x in js:
            m, v = chave(x["m"], a), chave(x["v"], a)
            if m is None or v is None:
                sem[(x["m"] if m is None else x["v"])] += 1; continue
            j = P[a].get((m, v))
            if j is None:
                print(f"{T}\tSEM PAR\t{m} x {v} {x['placar']} {x['data']}\t{url}"); continue
            vistos.add((m, v))
            d = f"{j['a'] // 10 * 10}s"
            tot["jogos"] += 1; dec[d]["jogos"] += 1
            if x["gm"] is None:
                print(f"{T}\tTM SEM PLACAR\t{m} x {v}: pacote {j['gm']}-{j['gv']}, TM '{x['placar']}'\t{url}")
            elif (x["gm"], x["gv"]) == (j["gm"], j["gv"]):
                tot["placar_ok"] += 1; dec[d]["placar_ok"] += 1
            else:
                print(f"{T}\tPLACAR\t{m} x {v} ({j['data']}): pacote {j['gm']}-{j['gv']}{' [' + j['resultado_especial'] + ']' if j['resultado_especial'] else ''}, TM {x['gm']}-{x['gv']}\t{url}")
            if x["data"] and j["data"]:
                dd = (date.fromisoformat(x["data"]) - date.fromisoformat(j["data"])).days
                tot["com_data"] += 1; dec[d]["com_data"] += 1
                if dd == 0:
                    tot["data_ok"] += 1; dec[d]["data_ok"] += 1
                else:
                    lista_datas.append((T, m, v, j["data"], x["data"], dd))
        faltam = set(P[a]) - vistos
        if faltam:
            print(f"{T}\tFALTA NO TM\t{len(faltam)} jogos (ex.: {sorted(faltam)[:2]})\t{url}")
    for T, m, v, dp, dt, dd in lista_datas:
        print(f"{T}\tDATA\t{m} x {v}: pacote {dp}, TM {dt} ({dd:+d} dias)\t{tm.URL.format(a=int(T[:4]))}")
    print("sem cadastro:", dict(sem), file=sys.stderr)
    print(dict(tot), file=sys.stderr)
    for d in sorted(dec):
        print(d, dict(dec[d]), file=sys.stderr)
