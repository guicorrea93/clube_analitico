"""Simula a classificação do importador (coleta/bra-sp-1/importar.py, classificacao()) com o ORDEM de hoje e com o ORDEM
proposto, a partir do pacote (partidas.csv, edicoes.csv), e compara vice e 3º com as listas da Wikipédia pt/en
(revisao/SP/listas_campeoes.json). Não mexe no código da coleta: só reproduz a regra para medir o efeito da correção.
Saída: revisao/QS/sim_ordem_saida.txt. Uso (da raiz): python -I -X utf8 revisao/QS/sim_ordem.py"""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
MODO = 2 if "--modo2" in sys.argv else 3 if ("--modo3" in sys.argv or "--modo4" in sys.argv) else 1
MATA = {"Quartas de final", "Semifinal", "Final", "Oitavas de final", "Mata-mata", "Primeira fase eliminatória"}
# modo 4: o modo 3 + desempate dos eliminados na mesma fase de mata-mata pelos pontos das fases de pontos corridos
SO_LIGA = "--modo4" in sys.argv
# modo 3: ORDEM novo (por nome) + nomes de fase trocados por temporada (proposta FASE_ANO) + desempate pelos pontos
# da 'Fase final' (liga decisiva) para quem chegou a ela
FASE_ANO = {("1976", "2º Turno"): "Fase final"}
# fase trocada por jogo, pela data (proposta FASE_JOGO em importar.py): (temporada, fase gravada, data de, data até) -> fase certa
FASE_DATAS = [("1978", "Quartas de final", "1978-11-01", "1978-11-30", "1º Turno - Quartas de final"),
              ("1978", "Semifinal", "1978-11-01", "1978-11-30", "1º Turno - Semifinal"),
              ("1978", "Final", "1978-11-01", "1978-11-30", "1º Turno - Final"),
              ("1978", "Primeira fase", "1979-06-20", "1979-06-30", "Final"),
              ("1981", "Final", "1981-04-01", "1981-04-30", "1º Turno - Final"),
              ("1981", "Final", "1981-08-01", "1981-08-31", "2º Turno - Final"),
              ("1998", "Final", "1998-02-01", "1998-04-30", "Torneio de rebaixamento"),
              ("2003", "Final", "2003-03-01", "2003-03-31", "Torneio de rebaixamento")]


def fase_certa(t, p):
    for tt, f, de, ate, nova in FASE_DATAS:
        if t == tt and p["fase"] == f and de <= p["data"] <= ate:
            if not (t == "2003" and {p["mandante"], p["visitante"]} == {"Corinthians", "São Paulo"}):
                return nova
    return FASE_ANO.get((t, p["fase"]), p["fase"])
sys.path.insert(0, str(RAIZ / "revisao" / "SP"))
from nomes import norm  # noqa: E402

PAC = RAIZ / "data" / "coleta" / "bra-sp-1" / "pacote"
ORDEM_HOJE = {"Primeira fase": 1, "Segunda fase": 2, "Terceira fase": 3, "Quarta fase": 4, "Mata-mata": 5,
              "Primeira fase eliminatória": 5, "Oitavas de final": 6, "Quartas de final": 7, "Semifinal": 8,
              "Fase final": 9, "Final": 10}
# proposta: toda fase que aparece no pacote tem nível; repescagem, torneio de rebaixamento e desempate de eliminação = 0
ORDEM_NOVO = dict(ORDEM_HOJE, **{
    "Fase única": 1, "1º Turno": 1, "2º Turno": 1, "3º Turno": 1, "Fase de Classificação": 1,
    "Torneio de Classificação": 1, "1º Turno - Classificatória": 1, "2º Turno - Classificatória": 1,
    "2º Turno - 1ª fase": 1, "2º Turno - 2ª fase": 1, "1º Turno - Semifinal": 1, "1º Turno - Final": 1,
    "2º Turno - Semifinal": 1, "2º Turno - Final": 1, "1º Turno - Quartas de final": 1,
    "Repescagem": 0, "Torneio de rebaixamento": 0, "Desempate": 0,
})


def ler(arq):
    return list(csv.DictReader(open(PAC / arq, encoding="utf-8")))


def campanha(ps):
    c = defaultdict(lambda: [0] * 6)
    for p in ps:
        if p["gols_mandante"] == "":
            continue
        gm, gv = int(p["gols_mandante"]), int(p["gols_visitante"])
        for eu, a, b in ((p["mandante"], gm, gv), (p["visitante"], gv, gm)):
            x = c[eu]
            x[0] += 1; x[4] += a; x[5] += b
            x[1 if a > b else 2 if a == b else 3] += 1
    return c


def classificar(ps, campeao, pv, ordem, vice_grupo_final=False, pts_fase_final=False):
    camp = campanha(ps)
    ff = [p for p in ps if p["fase"] == "Fase final"]
    cl = campanha([p for p in ps if p["fase"] not in MATA and ordem.get(p["fase"], 1) > 0])
    cff = campanha(ff) if pts_fase_final and len({p["grupo"] for p in ff}) == 1 else {}
    alc = defaultdict(int)
    faltam = set()
    for p in ps:
        if p["fase"] not in ordem:
            faltam.add(p["fase"])
        n = ordem.get(p["fase"], 50)
        for c in (p["mandante"], p["visitante"]):
            alc[c] = max(alc[c], n)
    fin = [p for p in ps if p["fase"] == "Final"]
    vice = None
    if campeao and fin:
        f = {x for p in fin for x in (p["mandante"], p["visitante"])} - {campeao}
        if len(f) == 1:
            vice = next(iter(f))
        elif vice_grupo_final and f:   # quadrangular/triangular final: o vice é o 2º do grupo final
            cf = campanha(fin)
            vice = max(f, key=lambda c: (pv * cf[c][1] + cf[c][2], cf[c][1], cf[c][4] - cf[c][5], cf[c][4]))
    def chave(c):
        x = camp[c]
        y = cff.get(c, [0] * 6)
        if SO_LIGA:
            x = cl.get(c, [0] * 6)
        return (c != campeao, c != vice, -alc[c], -(pv * y[1] + y[2]), -(pv * x[1] + x[2]), -x[1], -(x[4] - x[5]), -x[4], c)
    return sorted(camp, key=chave), faltam


ZERO = {"Repescagem", "Torneio de rebaixamento", "Desempate"}


def niveis(ps):
    """Proposta 2: nível pela fase de verdade, não pelo nome. Repescagem/rebaixamento/desempate = 0; fase com quase
    todos os clubes da edição (turnos, fase de classificação) = 1; fase com nome de mata-mata conhecido = ORDEM de hoje;
    outra fase só com parte dos clubes (2º Turno de 1976, 'Fase final', 'Terceira fase') = 1 + posição na ordem das datas."""
    todos = {c for p in ps for c in (p["mandante"], p["visitante"]) if p["fase"] not in ZERO}
    clubes, inicio = defaultdict(set), {}
    for p in ps:
        clubes[p["fase"]] |= {p["mandante"], p["visitante"]}
        if p["data"] and p["data"] > "0000":
            inicio[p["fase"]] = min(inicio.get(p["fase"], "9999"), p["data"])
    ordem_datas = sorted((f for f in clubes if f not in ZERO), key=lambda f: inicio.get(f, "9999"))
    niv = {}
    for f in clubes:
        if f in ZERO:
            niv[f] = 0
        elif len(clubes[f]) >= 0.9 * len(todos):
            niv[f] = 1
        elif f in ("Quartas de final", "Semifinal", "Final", "Oitavas de final", "Fase final"):
            niv[f] = ORDEM_HOJE[f]
        else:
            niv[f] = 1 + ordem_datas.index(f)
    return niv


def classificar2(ps, campeao, pv):
    niv = niveis(ps)
    camp = campanha(ps)
    alc = defaultdict(int)
    for p in ps:
        for c in (p["mandante"], p["visitante"]):
            alc[c] = max(alc[c], niv[p["fase"]])
    # campanha só na fase mais alta que o clube alcançou
    topo = {}
    for c in camp:
        topo[c] = campanha([p for p in ps if c in (p["mandante"], p["visitante"]) and niv[p["fase"]] == alc[c]])[c]
    fin = [p for p in ps if p["fase"] == "Final"]
    vice = None
    if campeao and fin:
        f = {x for p in fin for x in (p["mandante"], p["visitante"])} - {campeao}
        if len(f) == 1:
            vice = next(iter(f))
    def chave(c):
        x, y = camp[c], topo[c]
        return (c != campeao, c != vice, -alc[c], -(pv * y[1] + y[2]), -(pv * x[1] + x[2]), -x[1], -(x[4] - x[5]), -x[4], c)
    return sorted(camp, key=chave), niv


def main():
    eds = {e["temporada"]: e for e in ler("edicoes.csv")}
    part = defaultdict(list)
    for p in ler("partidas.csv"):
        part[p["temporada"]].append(p)
    cf = defaultdict(list)
    for r in ler("classificacao_final.csv"):
        cf[r["temporada"]].append(r)
    L = json.load(open(RAIZ / "revisao" / "SP" / "listas_campeoes.json", encoding="utf-8"))
    fonte = defaultdict(lambda: {"vice": set(), "terc": set()})
    for x in L["en"]:
        fonte[(x["ano"], {"LFP": "LPF"}.get(x["liga"], x["liga"]))]["vice"].add(norm(x["vice"]))
    for x in L["pt"]:
        k = (x["ano"], {"LFP": "LPF"}.get(x["liga"], x["liga"]))
        if x.get("vice") not in (None, "", "—", "–"):
            fonte[k]["vice"].add(norm(x["vice"]))
        if x.get("terceiro") not in (None, "", "—", "–"):
            fonte[k]["terc"].add(norm(x["terceiro"]))
    out, cont = [], defaultdict(int)
    for t, e in eds.items():
        ano = int(t[:4]); liga = t.split(" ")[1] if " " in t else ""
        f = fonte.get((ano, liga)) or (fonte.get((ano, "APEA")) if ano in (1933, 1934) else None) \
            or next((v for (a, l), v in fonte.items() if a == ano), None)
        pac = [r["clube"] for r in sorted(cf[t], key=lambda r: int(r["posicao"]))]
        geral = cf[t] and cf[t][0]["fonte"].startswith("RSSSF")
        hoje, _ = classificar(part[t], e["campeao"], int(e["pontos_vitoria"]), ORDEM_HOJE)
        novo, faltam = classificar(part[t], e["campeao"], int(e["pontos_vitoria"]), ORDEM_NOVO, vice_grupo_final=True)
        if MODO == 3:
            ps3 = [dict(p, fase=fase_certa(t, p)) for p in part[t]]
            novo, faltam = classificar(ps3, e["campeao"], int(e["pontos_vitoria"]), ORDEM_NOVO, vice_grupo_final=True, pts_fase_final=True)
        if MODO == 2:
            novo, niv = classificar2(part[t], e["campeao"], int(e["pontos_vitoria"]))
            faltam = set()
        if geral:
            hoje = novo = pac   # ordem da tabela geral da RSSSF: a regra não se aplica
        cont["edicoes"] += 1
        cont["reproduz_pacote"] += hoje[:3] == pac[:3]
        if faltam:
            out.append(f"{t}\tFASE SEM NÍVEL NO ORDEM NOVO\t{sorted(faltam)}")
        if not f:
            continue
        for nome, i, chave in (("vice", 1, "vice"), ("3º", 2, "terc")):
            if not f[chave] or len(pac) <= i:
                continue
            cont[f"{nome}_conf"] += 1
            ok_h, ok_n = pac[i] in f[chave], len(novo) > i and novo[i] in f[chave]
            cont[f"{nome}_ok_hoje"] += ok_h; cont[f"{nome}_ok_novo"] += ok_n
            if ok_h != ok_n or not ok_n:
                out.append(f"{t}\t{nome}\tpacote {pac[i]}\tORDEM novo {novo[i] if len(novo) > i else '-'}\tfonte {sorted(f[chave])}\t"
                           + ("CONSERTA" if ok_n and not ok_h else "PIORA" if ok_h and not ok_n else "segue errado"))
    out.append(json.dumps(cont, ensure_ascii=False))
    (Path(__file__).with_name(f"sim_ordem{('4' if SO_LIGA else MODO) if MODO > 1 else ''}_saida.txt")).write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
