"""Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/mar-1/rsssf/) com o leitor comum (rsssf_africa),
a tabela de confrontos (matriz) dos anos que a página traz e, nos anos em que a RSSSF só tem a tabela final, o calendário
do ogol.

Uso como biblioteca: ler(edicao) -> (jogos, tabelas); parcial(edicao) -> classificação incompleta; campeoes() ->
{temporada: (campeão, vice) como na página}.
Uso direto: python coleta/mar-1/ler_rsssf.py [temporada ...]   (resumo de jogos e tabelas por edição)
"""
from __future__ import annotations

import json
import re
import sys
from functools import lru_cache
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-africa"))
sys.path.insert(0, str(AQUI))
import rsssf_africa  # noqa: E402
from edicoes import EDICOES, FIM_PADRAO, PASTA_DADOS, Edicao  # noqa: E402

PASTA = PASTA_DADOS / "rsssf"

# fases reconhecidas pelo título (a primeira é a fase de partida); vale para todas as edições
FASES = [
    (r"^(Relegation (Group|Round|Stage|Pool)|Poule de relégation)\b", "Grupo do rebaixamento"),
    (r"^Relegation Play-?offs?(\s*:|\s*\[|\s*$)", "Desempate do rebaixamento"),
    (r"^(Championship (Group|Round|Stage|Pool)|Final (Group|Round|Stage|Tournament)|Poule finale)\b", "Fase final"),
    (r"^(First Stage|First Phase|Regular (Season|Stage)|Group Stage)\b", ""),
    (r"^(Second Place (Match|Play-?off)|Play-?off for (second|2nd) place)", "Desempate do 2º lugar"),
    (r"^(Championship Final|Final(?!\s*(Table|Tournament|Group|Standing|phase|stage|Round))\b)", "Final"),
    (r"^(Title Play-?off|Play-?off for (the )?(title|championship)|Championship Play-?off)", "Desempate do título"),
]


@lru_cache(maxsize=None)
def linhas(pagina: str) -> tuple[str, ...]:
    """Texto puro da página, com os erros de digitação corrigidos (explicacoes.CONSERTA_TEXTO, cada um com o motivo) e
    os formatos marroquinos levados ao do leitor comum."""
    from explicacoes import CONSERTA_TEXTO
    ls = [l.replace("–", "-").replace("—", "-").replace("´", " ") for l in rsssf_africa.texto(PASTA / f"{pagina}.html")]
    saida = []
    for l in ls:
        if not rsssf_africa.linha_tabela(l):
            # "COD Meknes      - SA Sale           5-2" (placar no fim, 1990s): volta ao "A  5-2  B"
            m = re.match(r"^(\S.*?\S)\s+-\s+(\S.*?\S)\s{2,}(\d{1,2}-\d{1,2})(.*)$", l)
            if m:
                l = f"{m.group(1)}  {m.group(3)}  {m.group(2)}{m.group(4)}"
            # "A   bt  B" / "A   lt  B": venceu / perdeu, sem placar conhecido (como no ven-1); a nota "[bt]" fica no jogo
            l = re.sub(r"^(\S.*?)\s+bt\s+(\S.*?)\s*$", r"\1  w-l  \2  [bt]", l)
            l = re.sub(r"^(\S.*?)\s+lt\s+(\S.*?)\s*$", r"\1  l-w  \2  [lt]", l)
        saida.append(l)
    for (pg, n), (antes, depois, _motivo) in CONSERTA_TEXTO.items():
        if pg == pagina:
            assert antes in saida[n], f"{pagina}:{n} mudou: {saida[n]!r}"
            saida[n] = saida[n].replace(antes, depois)
    return tuple(saida)


def inicio(ls: tuple[str, ...]) -> int:
    """Nas páginas de 2009/10 em diante, o índice do topo ("GNF I", "Coupe du Trône", "GNF II") repete os títulos: o
    campeonato começa no segundo "GNF I"."""
    vistos = [i for i, l in enumerate(ls) if re.fullmatch(r"GNF ?(I|1)|Botola( Pro)?( ?1)?", l.strip())]
    return vistos[1] if len(vistos) >= 2 else 0


def fim_padrao(ls: tuple[str, ...], ini: int) -> int:
    """Primeira linha, depois da primeira tabela ou jogo do trecho, que abre outra competição."""
    viu = False
    for i in range(ini, len(ls)):
        s = ls[i].strip()
        if not viu:
            viu = bool(rsssf_africa._jogo(ls[i]) or rsssf_africa.linha_tabela(ls[i]))
            continue
        if re.match(FIM_PADRAO, s, re.I):
            return i
    return len(ls)


def _limpa(ls: list[str]) -> list[str]:
    """Tira as linhas da tabela de confrontos (lida à parte) e junta autores que continuam na linha de baixo."""
    # (e as notas de outra fonte que repetem números: "OC Khouribga   38-21 instead of 40-22")
    saida = ["" if _linha_matriz(l) or re.search(r"\binstead of\b", l) else l for l in ls]
    for k in range(1, len(saida)):
        s = saida[k].strip()
        if s and "[" not in s and s.endswith("]"):
            ant = next((i for i in range(k - 1, max(k - 4, -1), -1) if saida[i].strip()), None)
            if ant is not None and saida[ant].strip().startswith("[") and "]" not in saida[ant]:
                saida[ant] = saida[ant].rstrip() + " " + s
                saida[k] = ""
    return saida


def _linha_matriz(l: str) -> bool:
    return len(re.findall(r"\b\d{1,2}-\d{1,2}\b", l)) >= 5 and not rsssf_africa.linha_tabela(l)


def _trecho(pagina: str, ini: int, fim: int | None) -> tuple[list[str], int, int]:
    ls = linhas(pagina)
    if ini == 0:
        ini = inicio(ls)
    fim = fim if fim is not None else fim_padrao(ls, ini)
    return [""] * ini + _limpa(list(ls[ini:fim])), ini, fim   # mantém o número da linha da página


def ler(e: Edicao) -> tuple[list[rsssf_africa.Jogo], list[rsssf_africa.Tabela]]:
    jogos, tabelas = [], []
    if e.ogol is not None:
        jogos += ogol_jogos(e)
    for pagina, ini, fim in e.trechos:
        trecho, ini, fim = _trecho(pagina, ini, fim)
        j, t = rsssf_africa.ler(trecho, e.ano_inicio, e.ano_fim, fases=e.fases + FASES)
        for x in j:
            x.texto = f"{pagina}:{x.linha}"
        jogos += j
        tabelas += t
    for pagina, ini, fim in e.tabelas:
        trecho, ini, fim = _trecho(pagina, ini, fim)
        tabelas += rsssf_africa.ler(trecho, e.ano_inicio, e.ano_fim, fases=e.fases + FASES)[1]
    if e.matriz:
        jogos += matriz(e.matriz, tabelas)
    return jogos, tabelas


# ------------------------------------------------------------------------------------------------ tabela de confrontos

def matriz(pagina: str, tabelas: list) -> list[rsssf_africa.Jogo]:
    """Tabela de confrontos: cabeçalho de siglas ("WAC KACM MCO ...") e uma linha por clube, mandante na linha e visitante
    na coluna (a diagonal fica em branco). As siglas se repetem (KAC = Kawkab Marrakech e Kénitra), então cada linha é
    ligada ao clube da tabela final pela campanha que a matriz dá (jogos, vitórias, empates, derrotas e gols); sem campanha
    igual, pela ordem (a do cabeçalho é a da tabela). Os jogos vêm sem data e sem rodada (texto "pagina:linha:coluna")."""
    ls = linhas(pagina)
    h = next(i for i, l in enumerate(ls) if len(l.split()) >= 8 and all(re.fullmatch(r"[A-Z][A-Za-z.]{1,7}", x) for x in l.split()))
    cab = [(m.start(), m.end(), m.group()) for m in re.finditer(r"\S+", ls[h])]
    centros = [(a + b) / 2 for a, b, _ in cab]
    linhas_m = []
    for i in range(h + 1, min(h + 3 + 2 * len(cab), len(ls))):
        l = ls[i]
        t = l.split()
        if not t:
            continue
        if not re.fullmatch(r"[A-Z][A-Za-z.]{1,7}", t[0]):   # "LARACHE" (1960/61)
            break
        linhas_m.append(i)
    n = len(cab)
    res: dict[tuple[int, int], tuple[int, int, int, int]] = {}
    for k, i in enumerate(linhas_m[:n]):
        for m in re.finditer(r"(\d{1,2})-(\d{1,2})", ls[i]):
            c = (m.start() + m.end()) / 2
            col = min(range(n), key=lambda x: abs(centros[x] - c))
            if col != k:
                res[(k, col)] = (int(m.group(1)), int(m.group(2)), i, col)
    # campanha de cada índice, sem os jogos do clube que desistiu (linha com vários "n/p": a tabela não os conta)
    fora = {k for k, i in enumerate(linhas_m[:n]) if len(re.findall(r"\bn/p\b", ls[i])) >= 3}
    camp = []
    for k in range(n):
        x = [0] * 6
        for (a, b), (gm, gv, _, _) in res.items():
            if k in (a, b) and not ({a, b} & fora and k not in fora):
                gp, gc = (gm, gv) if k == a else (gv, gm)
                x[0] += 1
                x[1 + (0 if gp > gc else 1 if gp == gc else 2)] += 1
                x[4] += gp
                x[5] += gc
        camp.append(x)
    tab = next((t for t in tabelas if len(t.linhas) >= n - 2), None)
    nomes: dict[int, str] = {}
    if tab:
        # o par (linha da matriz, linha da tabela) de campanha mais parecida primeiro (vitórias, empates, derrotas e gols;
        # a campanha da matriz pode ter jogos que a tabela não conta, como os do clube que desistiu); no empate, a ordem
        dist = lambda k, r: sum(abs(a - b) for a, b in zip(camp[k][1:], [r["v"], r["e"], r["d"], r["gp"], r["gc"]]))
        pares = sorted((dist(k, r), abs(k - p), k, p) for k in range(n) for p, r in enumerate(tab.linhas))
        usados_k, usados_p = set(), set()
        for d, _, k, p in pares:
            if k in usados_k or p in usados_p:
                continue
            nomes[k] = tab.linhas[p]["nome"]
            usados_k.add(k)
            usados_p.add(p)
    jogos = []
    for (a, b), (gm, gv, i, col) in sorted(res.items(), key=lambda x: (x[1][2], x[1][3])):
        jogos.append(rsssf_africa.Jogo(linha=i * 100 + col, mandante=nomes.get(a, cab[a][2]), visitante=nomes.get(b, cab[b][2]),
                                       gm=gm, gv=gv, texto=f"{pagina}:{i}:{col}"))
    return jogos


# ------------------------------------------------------------------------------------------------ classificação parcial

def parcial(e: Edicao) -> list[dict]:
    """Classificação incompleta ("Final Standings" só com posição, ou posição, jogos e pontos): [{pos, nome, j, v, e, d,
    gp, gc, pts, obs}], com None no que a página não traz."""
    if not e.parcial:
        return []
    pagina, ini, fim = e.parcial
    saida = []
    for l in linhas(pagina)[ini:fim]:
        m = re.match(r"^\s*(\d{1,2})\.\s*(\S.*?)(?:\s{2,}(.*))?$", l)
        if not m:
            continue
        cheia = rsssf_africa.linha_tabela(l)
        if cheia:
            saida.append({**cheia, "obs": cheia.get("obs", "")})
            continue
        nome, resto = m.group(2).strip(), (m.group(3) or "")
        if (mn := re.search(r"\s\d", nome)):   # "Olympique Casablanca 30 17 12  1   76": o nome acaba no primeiro número
            nome, resto = nome[:mn.start()].strip(), nome[mn.start():] + "  " + resto
        nome = re.sub(r"\s*\[[^\]]*\]\s*$", "", nome)
        obs = " ".join(re.findall(r"\[[^\]]*\]|[A-Z][a-z]+(?:,? [A-Za-z' ]+)?$", resto))
        nums = re.findall(r"(?<![\d+-])[+-]?\s?\d+", re.sub(r"\[[^\]]*\]", "", resto))
        nums = [int(x.replace(" ", "")) for x in nums]
        j = nums[0] if nums and nums[0] >= 0 else None
        pts = nums[-1] if len(nums) >= 2 else None
        ved = nums[1:4] if len(nums) == 5 and nums[1] + nums[2] + nums[3] == j else [None] * 3   # "30 17 12 1  76"
        saida.append({"pos": int(m.group(1)), "nome": nome, "cidade": None, "j": j, "v": ved[0], "e": ved[1], "d": ved[2],
                      "gp": None, "gc": None, "pts": pts, "obs": obs})
    return saida


# ------------------------------------------------------------------------------------------------ campeões

def campeoes() -> dict[str, tuple[str, str]]:
    """marochamp.html: temporada -> (campeão, vice) como na página ("" quando não houve; o vice só desde 1956/57)."""
    saida: dict[str, tuple[str, str]] = {}
    for l in linhas("marochamp"):
        m = re.match(r"^(\d{4}/\d{2})\s+(\S.*?)\s*$", l)
        if not m:
            continue
        partes = re.split(r"\s{2,}", m.group(2))
        camp = "" if re.match(r"^(abandoned|no competition|not held|not finished)", partes[0], re.I) else partes[0]
        saida[m.group(1)] = (camp, partes[1] if len(partes) > 1 and camp else "")
    return saida


# ------------------------------------------------------------------------------------------------ ogol

def _ogol_por_ano() -> dict[int, list[dict]]:
    pasta = PASTA_DADOS / "ogol"
    saida: dict[int, list[dict]] = {}
    for ed in json.loads((pasta / "edicoes.json").read_text(encoding="utf-8")):
        f = pasta / f"{ed['id']}.json"
        if f.exists():
            saida.setdefault(ed["ano_inicio"], []).extend(json.loads(f.read_text(encoding="utf-8")))
    return saida


_OG: dict[int, list[dict]] | None = None
OGOL_FASES = {"POff": "Desempate do título", "POut": "Desempate do rebaixamento", "F": "Final", "RF": "Fase final"}


def ogol_jogos(e: Edicao) -> list[rsssf_africa.Jogo]:
    """Calendário do ogol do ano como jogos (texto "ogol:<id do jogo>"). A fase "R12" é a 12ª rodada."""
    global _OG
    if _OG is None:
        _OG = _ogol_por_ano()
    saida = []
    for k, g in enumerate(sorted(_OG.get(e.ogol, []), key=lambda g: (g["data"], g["id"]))):
        if g["gols_mandante"] is None:
            continue
        f = g.get("fase") or ""
        rod = re.fullmatch(r"R(\d+)", f)
        fase = "" if rod or not f else OGOL_FASES.get(f, f)
        saida.append(rsssf_africa.Jogo(linha=k, mandante=g["mandante"], visitante=g["visitante"], gm=g["gols_mandante"],
                                       gv=g["gols_visitante"], rodada=int(rod.group(1)) if rod else g.get("rodada"),
                                       data=g["data"] if g["data"][:4] != "0000" else None, fase=fase, texto=f"ogol:{g['id']}"))
    return saida


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    alvo = set(sys.argv[1:])
    for e in EDICOES:
        if alvo and e.temporada not in alvo:
            continue
        js, ts = ler(e)
        fases = {}
        for j in js:
            fases[j.fase] = fases.get(j.fase, 0) + 1
        print(f"{e.temporada:8s} {len(js):4d} jogos  {len(ts):2d} tabelas {[len(t.linhas) for t in ts][:5]}  parcial "
              f"{len(parcial(e))}  fases {fases}")
