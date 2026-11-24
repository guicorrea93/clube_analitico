"""Monta o pacote da 1ª divisão turca (tur-1), 1959 a 2025/26, e o relatório docs/coleta/tur-1.md.

Base dos jogos: o calendário do ogol, com data e rodada; o clube é casado pelo código do ogol (clubes_tur.OGOL), porque os
nomes do calendário não são confiáveis nas temporadas antigas. Jogo decidido fora de campo ("DA", "WO" ou "SUSP" no ogol,
sem placar) fica com o placar oficial da matriz da Wikipédia ou do football-data, marcado `awd`.
Formatos especiais:
  1959      dois grupos (Vermelho e Branco) e final entre os primeiros (Fenerbahçe x Galatasaray);
  1962/63   dois grupos, grupo final com os 6 primeiros de cada e grupo de classificação com os 7º a 9º (este sem os jogos:
            nem o ogol nem a Wikipédia os têm; entra a tabela);
  2011/12   fase regular e play-offs (o do título começa com a metade dos pontos da fase regular).
Conferência: tabela final da RSSSF (turkhist.html, até 1996/97) e tabelas da Wikipédia; matriz de resultados da Wikipédia
jogo a jogo.
Outras fontes: engsoccerdata e football-data (1994/95+, placar; hora, árbitro e estatísticas do football-data); ESPN (hora,
estádio, público, gols e cartões, casada pelo código da ESPN, por votação); RSSSF (lista de campeões e de artilheiros).

Uso: python coleta/tur-1/importar.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-europa"))
sys.path.insert(0, str(AQUI))
import clubes_tur as clubes  # noqa: E402
from edicoes import DADOS, RAIZ, TEMPORADAS, nome_oficial, temporada, wiki_titulo  # noqa: E402
from pacote import gravar  # noqa: E402
import notas_wiki  # noqa: E402
from rsssf_tur import ler as ler_hist, texto as texto_rsssf  # noqa: E402
from wiki_tabela import _fecha, _partes, resultados as wiki_resultados, tabelas as wiki_tabelas  # noqa: E402

LONDRES = ZoneInfo("Europe/London")
ISTAMBUL = ZoneInfo("Europe/Istanbul")
PACOTE = DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / "tur-1.md"
URL_RSSSF = "https://www.rsssf.org/tablest/turkhist.html"
FD = range(1994, 2026)
GRUPOS = {1958, 1962}
PLAYOFFS = {2011}
# fase do ogol -> (fase, grupo)
FASES_OGOL = {"Kirmizi Grup": ("Grupos", "Grupo Vermelho"), "Beyaz Grup": ("Grupos", "Grupo Branco"), "F": ("Final", None),
              "": ("Grupo final", None), "POff": ("Play-off", None)}

# clube que não está na temporada seguinte sem ter caído: (ano, clube) -> motivo
NAO_REBAIXADOS: dict[tuple, str] = {}
# explicação de cada divergência que sobra entre fontes (vai para o relatório, antes das ocorrências da temporada)
EXPLICACOES: dict[int, list[str]] = {
    1958: ["a matriz de resultados da Wikipédia de 1959 difere do ogol em 16 pares (parece ter mandos trocados); o ogol fecha "
           "com as tabelas dos grupos, menos 1 gol do Beşiktaş e 1 do Hacettepe na RSSSF"],
    1959: ["o ogol e a matriz da Wikipédia concordam jogo a jogo; as tabelas da RSSSF e da Wikipédia (que a copia) têm 1 ou 2 "
           "gols a mais ou a menos em 6 clubes, sem mudar pontos nem posições"],
    1960: ["a tabela da RSSSF de 1960/61 tem erros em 8 clubes (números de um clube em outro); a da Wikipédia fecha com os jogos, "
           "menos os gols contra do Feriköy e os gols do Altınordu (17-31 em vez de 31-53, erro de digitação), e dá a ordem"],
    1962: ["o ogol tem alguns jogos dos grupos com o mando trocado em relação à matriz da Wikipédia (os totais dos grupos fecham "
           "com as tabelas, menos 1 gol do Ankara Demirspor e 1 do Beykoz); no grupo final, as tabelas da RSSSF e da "
           "Wikipédia diferem dos jogos em 6 clubes, sem outra fonte para decidir: ficam os jogos do ogol",
           "o grupo de classificação (7º a 9º de cada grupo) não tem os jogos no ogol nem na Wikipédia: entra a tabela"],
    1965: ["Altay (gols pró) e Şekerspor (gols contra): 2 gols a mais nas tabelas que nos jogos do ogol e da matriz"],
    1977: ["Samsunspor e Mersin İdmanyurdu: 1 gol de diferença nas tabelas (o ogol e a matriz concordam)"],
    1988: ["a RSSSF separa o Samsunspor em duas linhas: os 18 jogos disputados e os 18 dados por 0-3 depois do acidente; os "
           "jogos e a Wikipédia somam os 36"],
    2002: ["İstanbulspor: 1 gol contra a mais na tabela da Wikipédia (o ogol e a matriz concordam)"],
    2011: ["Trabzonspor x Gaziantepspor (10/02/2012): a matriz e a tabela da Wikipédia dão 4-0; o ogol, o football-data e o "
           "engsoccerdata, 4-1: fica 4-1"],
    2016: ["Adanaspor x Kasımpaşa (30/01/2017): a matriz e a tabela da Wikipédia dão 3-0; o ogol, o football-data e o "
           "engsoccerdata, 2-0: fica 2-0"],
}
# jogo do ogol corrigido (placar e, se preciso, mando), pelo id do jogo no ogol: id -> (mandante, visitante, gols, gols,
# motivo)
F2001 = "football-data e engsoccerdata; com os três jogos corrigidos, as linhas de Samsunspor, Gençlerbirliği e Kocaelispor "         "na tabela da Wikipédia fecham"
CORRECOES: dict[str, tuple] = {
    "1199753": ("Samsunspor", "Gençlerbirliği", 2, 2, f"o ogol dá 0-2; {F2001}"),
    "1199833": ("Kocaelispor", "Samsunspor", 0, 1, f"o ogol dá Samsunspor 0-0 Kocaelispor; {F2001}"),
    "1199908": ("Gençlerbirliği", "Samsunspor", 2, 0, f"o ogol dá Samsunspor 0-2 Gençlerbirliği (mando invertido); {F2001}"),
    "196346": ("Trabzonspor", "Diyarbakırspor", 3, 0, "o ogol dá 2-1; matriz da Wikipédia, football-data e engsoccerdata dão "
                                                      "3-0, e a tabela da Wikipédia fecha"),
    "196378": ("Gaziantepspor", "Malatyaspor", 1, 0, "o ogol dá 0-1; matriz da Wikipédia, football-data e engsoccerdata dão "
                                                     "1-0, e a tabela da Wikipédia fecha"),
    "196380": ("Samsunspor", "Diyarbakırspor", 1, 0, "o ogol dá 0-1; matriz da Wikipédia, football-data e engsoccerdata dão "
                                                     "1-0, e a tabela da Wikipédia fecha"),
}
# jogos dados pela federação a partir de uma data, com placar no ogol: (ano, clube) -> (data, motivo)
DADOS_FORA = {(1988, "Samsunspor"): ("1989-01-01", "o ônibus do Samsunspor sofreu um acidente grave em 20/01/1989 e o "
                                                   "clube não pôde jogar o resto da temporada: os 18 jogos que faltavam "
                                                   "foram dados por 3-0 aos adversários, e o Samsunspor não caiu"),
              (2009, "Ankaraspor"): ("2009-01-01", "a federação rebaixou o Ankaraspor em 07/10/2009, com efeito imediato, pela "
                                                   "ligação dos dirigentes com os do Ankaragücü; todos os 34 jogos dele valeram "
                                                   "3-0 para os adversários")}
# ajuste de pontos da tabela da Wikipédia que não vale
IGNORAR_AJUSTE: set = set()
# nome do artilheiro corrigido
NOMES_ARTILHEIRO: dict[str, str] = {}

COMPETICAO = {
    "slug": "tur-1", "nome": "Campeonato Turco", "nome_curto": "Turco", "tipo": "liga", "nivel": 1,
    "pais": "TUR", "pais_nome": "Turquia", "regiao": None, "confederacao": "UEFA",
    "rotulo_painel": "Turco", "menu_painel": "Turquia · 1ª divisão",
    "do_painel": "do Campeonato Turco", "o_painel": "o Campeonato Turco",
    "observacao": "1ª divisão turca desde a criação da liga nacional (1959): Millî Lig, 1. Lig (1963/64) e Süper Lig "
                  "(2001/02). Em 1959, dois grupos e final; em 1962/63, dois grupos, grupo final e grupo de classificação; "
                  "em 2011/12, fase regular e play-offs. Os campeonatos anteriores (Türkiye Futbol Şampiyonası, 1924-1951, "
                  "e Millî Küme, 1937-1950) não são contados pela federação e ficam de fora.",
}


def ler_csv(arq: Path) -> list[dict]:
    with arq.open(encoding="utf-8-sig", errors="replace") as f:
        return list(csv.DictReader(f))


def data_fd(s: str) -> str:
    d, m, y = s.split("/")
    y = int(y) + (2000 if len(y) == 2 and int(y) < 50 else 1900 if len(y) == 2 else 0)
    return f"{y:04d}-{int(m):02d}-{int(d):02d}"


def minuto(s: str | None) -> tuple[int | None, int | None]:
    m = re.match(r"^(\d+)'?(?:\+(\d+)'?)?", s or "")
    return (int(m.group(1)), int(m.group(2)) if m.group(2) else None) if m else (None, None)


def faixa(anos) -> str:
    a = sorted(anos)
    return f"{a[0]}-{a[-1]}" if a[0] != a[-1] else f"{a[0]}"


def chave(nome: str, a: int, fonte: str) -> str:
    c = clubes.esd(nome, a)
    if c is None:
        raise SystemExit(f"{temporada(a)}: nome do {fonte} sem cadastro: {nome}")
    return c


# ------------------------------------------------------------------ fontes
def texto_wiki(a: int) -> str:
    arqs = sorted((DADOS / "wikipedia").glob(f"{wiki_titulo(a)}*.wiki"))
    return "\n".join(x.read_text(encoding="utf-8") for x in arqs)


def tabelas_wiki(a: int) -> list[dict]:
    res = []
    for tb in wiki_tabelas(texto_wiki(a)):
        for x in tb["times"]:
            x["clube"] = clubes.esd(x["nome"], a)
        res.append(tb)
    return res


def sem_notas(texto: str) -> str:
    """Tira as notas de rodapé ({{efn|...}}, {{refn|...}}, {{#tag:ref|...}}): dentro de uma célula da matriz, um placar
    citado na nota viraria outro jogo."""
    while True:
        m = re.search(r"\{\{\s*(?:efn|refn|#tag:ref)", texto, re.I)
        if not m:
            return texto
        texto = texto[:m.start()] + texto[_fecha(texto, m.start()):]


def matriz_wiki(a: int, tbs: list[dict]) -> dict[tuple, list]:
    """Placares da matriz de resultados da Wikipédia: (mandante, visitante) -> [(g, g), ...]. Candidatos de cada código: o
    alvo do link em name_XXX, o nome visível e o código na tabela do mesmo artigo; vale o primeiro que joga a temporada e
    ainda não foi usado por outro código da mesma matriz (como no Belga)."""
    res: dict[tuple, list] = defaultdict(list)
    cod_tab = {x["codigo"]: x["clube"] for tb in tbs for x in tb["times"] if x["clube"]}
    texto = re.sub(r"(?i)#invoke:\s*sports table", "#invoke:sports results", sem_notas(texto_wiki(a)))
    alvos = []
    for m in re.finditer(r"\{\{\s*#invoke:\s*sports results\s*\|", texto, flags=re.I):
        # os mesmos parâmetros de nível de cima que wiki_tabela.resultados lê (um bloco mal fechado engole o seguinte)
        fim = _fecha(texto, m.start())
        corpo = re.sub(r"<!--.*?-->", "", texto[m.start() + 2:fim - 2], flags=re.S)
        params = dict(p.split("=", 1) for p in _partes(corpo)[1:] if "=" in p)
        params = {k.strip(): v.strip() for k, v in params.items()}
        if any(re.match(r"^match_([^_]+)_([^_]+)$", k) and re.search(r"\d+\s*[–-]\s*\d+", re.sub(r"<ref.*?(?:/>|</ref>)", "", v))
               for k, v in params.items()):
            alvos.append({k[5:]: mm.group(1) for k, v in params.items()
                          if k.startswith("name_") and (mm := re.match(r"\[\[([^\]|]+)", v))})
    grupos = wiki_resultados(texto)
    if len(alvos) != len(grupos):
        raise SystemExit(f"{temporada(a)}: {len(grupos)} matrizes na Wikipédia e {len(alvos)} lidas à parte")
    temporada_set = set(cod_tab.values())
    for g, alvo in zip(grupos, alvos):
        cod, usados = {}, set()
        for k, v in g["nomes"].items():
            cands = [c for c in (clubes.esd(alvo.get(k, ""), a), clubes.esd(v, a), cod_tab.get(k), clubes.esd(k, a)) if c]
            boas = [c for c in cands if c in temporada_set and c not in usados] if temporada_set else cands
            cod[k] = (boas or cands or [None])[0]
            usados.add(cod[k])
        for (c1, c2), placares in g["jogos"].items():
            if cod.get(c1) is None or cod.get(c2) is None:
                raise SystemExit(f"{temporada(a)}: clube da matriz da Wikipédia sem cadastro: {g['nomes'].get(c1, c1)} x "
                                 f"{g['nomes'].get(c2, c2)}")
            res[(cod[c1], cod[c2])] += placares
    return res


def carregar_ogol(a: int) -> list[dict]:
    res = []
    for o in json.loads((DADOS / "ogol" / f"tur1_{a}.json").read_text(encoding="utf-8")):
        if o["resultado"] in ("ADI", "ANU", "vs"):
            continue
        m = clubes.ogol(o["mandante_id"], a)
        v = clubes.ogol(o["visitante_id"], a)
        if m is None or v is None:
            raise SystemExit(f"{temporada(a)}: clube do ogol sem cadastro: {o['mandante']} ({o['mandante_id']}) x "
                             f"{o['visitante']} ({o['visitante_id']})")
        r = re.match(r"^R(\d+)$", o["fase"] or "")
        fase, grupo = ("Liga", None) if r else FASES_OGOL[o["fase"] or ""]
        res.append({"data": o["data"], "m": m, "v": v, "nm": o["mandante"], "nv": o["visitante"], "gm": o["gols_mandante"],
                    "gv": o["gols_visitante"], "rodada": int(r.group(1)) if r else None, "fonte": "ogol", "ogol": o,
                    "fase": fase, "grupo": grupo})
    return res


def carregar_fd() -> dict[int, list]:
    res = {}
    for a in FD:
        arq = DADOS / "football-data" / f"T1_{str(a)[-2:]}{str(a + 1)[-2:]}.csv"
        if arq.exists():
            res[a] = [(chave(x["HomeTeam"], a, "football-data"), chave(x["AwayTeam"], a, "football-data"), data_fd(x["Date"]), x)
                      for x in ler_csv(arq) if x.get("HomeTeam") and x.get("FTHG")]
    return res


def carregar_esd() -> dict[int, list]:
    res = defaultdict(list)
    for x in ler_csv(DADOS / "engsoccerdata" / "turkey_tier1.csv"):
        a = int(x["Season"])
        res[a].append((chave(x["home"], a, "engsoccerdata"), chave(x["visitor"], a, "engsoccerdata"), x["Date"], x))
    return res


def carregar_espn() -> dict[int, list[dict]]:
    res = {}
    for arq in sorted((DADOS / "espn").glob("tur1_*.json")):
        a = int(arq.stem[5:9])
        jogos = []
        for j in json.loads(arq.read_text(encoding="utf-8")):
            if j["situacao"] not in ("STATUS_FULL_TIME", "STATUS_FINAL"):
                continue
            utc = datetime.fromisoformat(j["data_hora"].replace("Z", "+00:00"))
            jogos.append(dict(j, data=utc.astimezone(ISTAMBUL).date().isoformat(), utc=utc, gm=int(j["gols_mandante"]),
                              gv=int(j["gols_visitante"])))
        if jogos:
            res[a] = jogos
    return res


class Mapa(dict):
    """Código do clube na outra fonte -> chave. `get(cod, ano)` usa o voto da temporada quando há."""
    def __init__(self, geral: dict, por_ano: dict):
        super().__init__(geral)
        self.por_ano = por_ano

    def get(self, cod, ano=None):
        return self.por_ano.get((cod, ano)) or super().get(cod)


def votar(base: dict[int, list[dict]], outra: dict[int, list[dict]], campo_m: str, campo_v: str) -> Mapa:
    votos: dict[str, Counter] = defaultdict(Counter)
    votos_ano: dict[tuple, Counter] = defaultdict(Counter)
    for a, jogos in outra.items():
        por_dia = defaultdict(list)
        for b in base.get(a, []):
            if b["data"] and b["gm"] is not None:
                por_dia[(b["data"], b["gm"], b["gv"])].append(b)
        for j in jogos:
            d = date.fromisoformat(j["data"])
            cand = [b for k in (-1, 0, 1) for b in por_dia.get(((d + timedelta(days=k)).isoformat(), j["gm"], j["gv"]), [])]
            if len(cand) == 1:
                for campo, lado in ((campo_m, "m"), (campo_v, "v")):
                    votos[j[campo]][cand[0][lado]] += 1
                    votos_ano[(j[campo], a)][cand[0][lado]] += 1
    return Mapa({k: c.most_common(1)[0][0] for k, c in votos.items()},
                {k: c.most_common(1)[0][0] for k, c in votos_ano.items()})


def casar(jogos: list[dict], usados: set, m: str, v: str, d: str, dias: int = 20) -> dict | None:
    cand = [j for j in jogos if (j["m"], j["v"]) == (m, v) and id(j) not in usados and j["data"]]
    if not cand:
        return None
    j = min(cand, key=lambda j: abs((date.fromisoformat(j["data"]) - date.fromisoformat(d)).days))
    if abs((date.fromisoformat(j["data"]) - date.fromisoformat(d)).days) > dias and len(cand) > 1:
        return None
    usados.add(id(j))
    return j


def campeoes_rsssf() -> dict[int, str]:
    """turkchamp.html, seção da Süper Lig: "1959     Fenerbahçe", "1959/60  Beşiktaş"."""
    res = {}
    t = texto_rsssf(DADOS / "rsssf" / "turkchamp.html")
    t = t[t.index("Süper Lig (professional"):]
    for m in re.finditer(r"^(\d{4})(?:/(\d{2}))?\s+(\S.*?)\s*$", t, re.M):
        a = int(m.group(1)) - (0 if m.group(2) else 1)
        if a in TEMPORADAS:
            res[a] = clubes.esd(m.group(3), a) or m.group(3)
    return res


# ------------------------------------------------------------------ tabela
def calcular(jogos: list[dict], pv: int) -> dict[str, list[int]]:
    t = defaultdict(lambda: [0, 0, 0, 0, 0, 0, 0])   # J V E D GP GC Pts
    for j in jogos:
        if j["gm"] is None:
            continue
        for c, gp, gc in ((j["m"], j["gm"], j["gv"]), (j["v"], j["gv"], j["gm"])):
            x = t[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            if gp > gc:
                x[1] += 1; x[6] += pv
            elif gp == gc:
                x[2] += 1; x[6] += 1
            else:
                x[3] += 1
    return t


def ordenar(t: dict[str, list[int]], ajuste: dict[str, int], criterio: str, jogos: list[dict] | None = None, pv: int = 2) -> list[str]:
    """criterio: "vitorias" (pontos, vitórias, saldo, gols pró), "saldo" (pontos, saldo, gols pró), "media" (pontos, média
    de gols) ou "confronto" (pontos; entre os empatados, pontos e saldo nos jogos entre eles; depois saldo e gols pró)."""
    def pts(c):
        return t[c][6] + ajuste.get(c, 0)

    def geral(c):
        j, v, e, d, gp, gc, p = t[c]
        if criterio == "media":
            return (-(gp / gc if gc else float("inf")), -gp)
        if criterio == "vitorias":
            return (-v, -(gp - gc), -gp)
        return (-(gp - gc), -gp)
    if criterio != "confronto":
        return sorted(t, key=lambda c: (-pts(c), *geral(c)))
    grupos = defaultdict(list)
    for c in t:
        grupos[pts(c)].append(c)
    res = []
    for p in sorted(grupos, reverse=True):
        g = grupos[p]
        if len(g) > 1 and jogos is not None:
            mini = calcular([j for j in jogos if j["m"] in g and j["v"] in g], pv)
            g.sort(key=lambda c: (-mini[c][6], -(mini[c][4] - mini[c][5]), *geral(c)))
        else:
            g.sort(key=geral)
        res += g
    return res


def conferir(T: str, linhas: list[dict], calc: dict, ajuste: dict, fonte: str, url: str, fase: str, grupo: str | None,
             tab, ocorr_a: list, rotulo: str) -> bool:
    """Compara uma tabela publicada com a calculada dos jogos e grava a tabela publicada. Devolve True se fecha."""
    erro = []
    for x in linhas:
        c = calc.get(x["clube"])
        pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]
        meu = (c[:6] + [c[6] + ajuste.get(x["clube"], 0)]) if c else None
        if pub != meu:
            erro.append(f"{x['clube']} tabela {pub} jogos {meu}")
        tab["tabelas_publicadas"].append({
            "temporada": T, "fase": fase, "grupo": grupo, "posicao": x["posicao"], "nome_fonte": x["nome"],
            "clube": clubes.exibicao(x["clube"]), "jogos": x["jogos"], "vitorias": x["vitorias"], "empates": x["empates"],
            "derrotas": x["derrotas"], "gols_pro": x["gols_pro"], "gols_contra": x["gols_contra"], "pontos": x["pontos"],
            "fonte": url})
    for e_ in erro[:8]:
        ocorr_a.append(f"{rotulo} ({fonte}) x jogos — {e_}")
    return not erro


def linhas_wiki(tb: dict, pv: int) -> list[dict]:
    return [dict(x, jogos=sum(x[k] or 0 for k in ("vitorias", "empates", "derrotas")),
                 pontos=pv * (x["vitorias"] or 0) + (x["empates"] or 0) + x["ajuste"]) for x in tb["times"]]


def linhas_rsssf(tb: dict, a: int) -> list[dict]:
    res = []
    for x in tb["linhas"]:
        c = clubes.esd(x["nome"], a)
        if c is None:
            continue   # linha de nota ("* Balance of Samsunspor")
        res.append(dict(x, clube=c))
    return res


# ------------------------------------------------------------------ temporadas de grupos (1959 e 1962/63)
def temporada_grupos(a: int, jogos: list[dict], tbs: list[dict], rs: list[dict], camp: dict, tab, nomes, ocorr) -> tuple:
    """1959: grupos Vermelho e Branco, final de ida e volta. 1962/63: grupos Vermelho e Branco, grupo final (6 primeiros
    de cada) e grupo de classificação (7º a 9º, só a tabela). Classificação final: o campeão, depois o grupo final (ou o
    vice da final), o grupo de classificação, e os outros pela posição no grupo; números somados de todas as fases."""
    T = temporada(a)
    pv = 2
    conferidas = divergentes = 0
    url_w = f"https://en.wikipedia.org/wiki/{wiki_titulo(a).replace(' ', '_')}"
    nome_tb = {"red": ("Grupos", "Grupo Vermelho"), "white": ("Grupos", "Grupo Branco"), "play-off": ("Grupo final", None),
               "championship": ("Grupo final", None), "classification": ("Grupo de classificação", None)}

    def fase_de(titulo):
        t = (titulo or "").lower()
        return next((v for k, v in nome_tb.items() if k in t), (None, None))
    calc_fase = {}
    for (fase, grupo) in {(j["fase"], j["grupo"]) for j in jogos}:
        calc_fase[(fase, grupo)] = calcular([j for j in jogos if (j["fase"], j["grupo"]) == (fase, grupo)], pv)
    soma: dict[str, list[int]] = defaultdict(lambda: [0] * 7)
    for c, x in calcular(jogos, pv).items():
        soma[c] = list(x)
    posicao_grupo: dict[str, tuple] = {}
    tabela_classif = None
    for fonte, url, lista in (("RSSSF", URL_RSSSF, [(tb["titulo"], linhas_rsssf(tb, a)) for tb in rs]),
                              ("Wikipédia", url_w, [(tb["secao"], linhas_wiki(tb, pv)) for tb in tbs])):
        for titulo, linhas in lista:
            fase, grupo = fase_de(titulo)
            if fase is None:
                continue
            for x in linhas:
                if x["clube"] is None:
                    raise SystemExit(f"{T}: nome da {fonte} sem cadastro: {x['nome']}")
                nomes[x["clube"]][f"{fonte.lower().replace('é', 'e')}:{x['nome']}"].add(a)
                if fase == "Grupos":
                    posicao_grupo.setdefault(x["clube"], (x["posicao"], grupo))
            if fase == "Grupo de classificação":
                if fonte == "RSSSF":
                    tabela_classif = linhas
                    for x in linhas:   # sem os jogos: entram os números da tabela
                        for i, k in enumerate(("jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra", "pontos")):
                            soma[x["clube"]][i] += x[k]
                for x in linhas:
                    tab["tabelas_publicadas"].append({
                        "temporada": T, "fase": fase, "grupo": grupo, "posicao": x["posicao"], "nome_fonte": x["nome"],
                        "clube": clubes.exibicao(x["clube"]), "jogos": x["jogos"], "vitorias": x["vitorias"],
                        "empates": x["empates"], "derrotas": x["derrotas"], "gols_pro": x["gols_pro"],
                        "gols_contra": x["gols_contra"], "pontos": x["pontos"], "fonte": url})
                continue
            ok = conferir(T, linhas, calc_fase.get((fase, grupo), {}), {}, fonte, url, fase, grupo, tab, ocorr[a],
                          f"tabela do {fase}{' ' + grupo if grupo else ''}")
            conferidas += ok
            divergentes += not ok
    campeao = camp[a]
    if a == 1958:
        finais = [j for j in jogos if j["fase"] == "Final"]
        vice = next(c for j in finais for c in (j["m"], j["v"]) if c != campeao)
        topo = [campeao, vice]
    else:
        final = [tb for tb in rs if "play-off" in (tb["titulo"] or "").lower()][0]
        topo = [chave(x["nome"], a, "RSSSF") for x in final["linhas"]]
        topo += [x["clube"] for x in (tabela_classif or [])]
    resto = sorted((c for c in posicao_grupo if c not in topo),
                   key=lambda c: (posicao_grupo[c][0], -soma[c][6], -(soma[c][4] - soma[c][5])))
    ordem = topo + resto
    jogos_campeao = soma[campeao][0]
    for pos, c in enumerate(ordem, 1):
        j_, v_, e_, d_, gp, gc, p = soma[c]
        tab["classificacao_final"].append({
            "temporada": T, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
            "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": p, "ajuste_pontos": 0,
            "situacao": "campeao" if c == campeao else None,
            "fonte": "RSSSF (campeão; " + ("vice pela final" if a == 1958 else "grupo final e grupo de classificação") +
                     "; depois a posição no grupo)",
            "observacao": "soma de todas as fases" + ("" if a == 1958 else " (grupo de classificação pela tabela, sem os jogos)")
                          + "; sem classificação oficial além " + ("do campeão e do vice" if a == 1958 else
                                                                    "do grupo final e do grupo de classificação")})
    n = len(ordem)
    formato = ("dois grupos (Vermelho e Branco) e final de ida e volta entre os primeiros" if a == 1958 else
               "dois grupos (Vermelho e Branco), grupo final com os 6 primeiros de cada e grupo de classificação")
    tab["edicoes"].append({"temporada": T, "ano_inicio": a + (1 if a == 1958 else 0), "ano_fim": a + 1,
                           "nome_oficial": nome_oficial(a), "num_clubes": n, "pontos_vitoria": pv, "formato": formato,
                           "campeao": clubes.exibicao(campeao), "vice": clubes.exibicao(ordem[1]),
                           "fontes": "ogol + RSSSF + Wikipédia",
                           "observacao": None if a == 1958 else "grupo de classificação sem os jogos (só a tabela)"})
    fases = [("Grupos", "grupos", 2, "pontos_corridos")]
    fases += [("Final", "mata_mata", None, "ida_volta")] if a == 1958 else \
        [("Grupo final", "grupos", 1, "pontos_corridos"), ("Grupo de classificação", "grupos", 1, "pontos_corridos")]
    for i, (f, tp, ng, fs) in enumerate(fases, 1):
        tab["fases"].append({"temporada": T, "ordem": i, "fase": f, "tipo": tp, "num_grupos": ng, "formato_serie": fs,
                             "criterio": "pontos, média de gols" if f != "Final" else "pontos, saldo"})
    gols = sum(j["gm"] + j["gv"] for j in jogos)
    tab["conferencia"].append({"temporada": T, "jogos": len(jogos), "jogos_esperados": None, "tabelas_conferidas": conferidas,
                               "tabelas_divergentes": divergentes, "gols": gols, "gols_com_autor": 0,
                               "observacao": f"campeão {clubes.exibicao(campeao)} (RSSSF)"})
    return T, n, gols, conferidas, divergentes, clubes.exibicao(campeao), jogos_campeao


# ------------------------------------------------------------------ principal
def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    rs_hist = ler_hist(DADOS / "rsssf" / "turkhist.html")
    fd = carregar_fd()
    esd = carregar_esd()
    espn = carregar_espn()
    camp = campeoes_rsssf()
    ogol = {a: carregar_ogol(a) for a in TEMPORADAS}
    mapa_espn = votar(ogol, espn, "mandante_id", "visitante_id")
    prox_2026 = {j[k] for j in carregar_ogol(TEMPORADAS[-1] + 1) for k in ("m", "v")}

    nomes = defaultdict(lambda: defaultdict(set))
    ocorr = defaultdict(list)
    tab = defaultdict(list)
    linhas_rel = []
    criterios = {}

    for a in TEMPORADAS:
        ocorr[a].extend(EXPLICACOES.get(a, []))
        T = temporada(a)
        pv = 3 if a >= 1987 else 2
        tbs = tabelas_wiki(a)
        mz = matriz_wiki(a, tbs)
        jogos = ogol[a]
        for j in jogos:
            nomes[j["m"]][f"ogol:{j['nm']}"].add(a)
            nomes[j["v"]][f"ogol:{j['nv']}"].add(a)
        regular = [j for j in jogos if j["fase"] == "Liga"]
        resto = [j for j in jogos if j["fase"] == "Play-off"]
        reg_ids = {id(j) for j in regular}

        # ---- jogo decidido fora de campo, sem placar no ogol
        for j in jogos:
            if j["gm"] is not None:
                continue
            o = j["ogol"]
            cand = mz.get((j["m"], j["v"]), [])
            fd_j = next((x for m, v, d, x in fd.get(a, []) if (m, v) == (j["m"], j["v"])), None)
            if cand:
                j["gm"], j["gv"] = cand[0] if id(j) in reg_ids or len(cand) == 1 else cand[-1]
                origem = "matriz da Wikipédia"
            elif fd_j:
                j["gm"], j["gv"] = int(fd_j["FTHG"]), int(fd_j["FTAG"])
                origem = "football-data"
            else:
                raise SystemExit(f"{T}: jogo sem placar no ogol ({o['resultado']}) e sem outra fonte: {j['m']} x {j['v']} "
                                 f"({j['data']})")
            j["especial"] = "awd"
            j["obs"] = (f"resultado decidido fora de campo (no ogol: \"{o['resultado']}\", sem placar); placar oficial pela "
                        f"{origem}")
            ocorr[a].append(f"{j['m']} x {j['v']} ({j['data']}): {o['resultado']} no ogol; fica {j['gm']}-{j['gv']} pela {origem}")
        for (b_, c_), (desde, motivo) in DADOS_FORA.items():
            if b_ != a:
                continue
            dados = [j for j in jogos if c_ in (j["m"], j["v"]) and j["data"] >= desde]
            for j in dados:
                j["especial"] = "awd"
                j["obs"] = f"resultado dado pela federação: {motivo}"
            ocorr[a].append(f"{c_}: {len(dados)} jogos marcados `awd` — {motivo}")
        for j in jogos:
            if j["ogol"]["id"] not in CORRECOES:
                continue
            m_, v_, g1, g2, motivo = CORRECOES[j["ogol"]["id"]]
            if {m_, v_} != {j["m"], j["v"]}:
                raise SystemExit(f"{T}: correção do jogo {j['ogol']['id']} com outros clubes: {m_} x {v_}")
            j["m"], j["v"], j["gm"], j["gv"] = m_, v_, g1, g2
            j["obs"] = ("resultado decidido fora de campo; " if j.get("especial") else "") + f"placar corrigido: {motivo}"
            ocorr[a].append(f"{m_} x {v_} ({j['data']}): placar corrigido para {g1}-{g2} ({motivo})")

        # ---- conferência jogo a jogo com a matriz da Wikipédia
        if mz:
            por_par = defaultdict(list)
            for j in jogos:
                por_par[(j["m"], j["v"])].append(j)
            dif = []
            for par, pl in mz.items():
                nossos = sorted((j["gm"], j["gv"]) for j in por_par.get(par, []))
                if sorted(pl) != nossos and not (len(pl) < len(nossos) and set(pl) <= set(nossos)):
                    outras = [f"{f_} {', '.join(f'{x[cm]}-{x[cv]}' for m, v, d, x in dados_.get(a, []) if (m, v) == par)}"
                              for f_, dados_, cm, cv in (("engsoccerdata", esd, "hgoal", "vgoal"), ("football-data", fd, "FTHG", "FTAG"))
                              if any((m, v) == par for m, v, d, x in dados_.get(a, []))]
                    dif.append(f"{par[0]} x {par[1]}: ogol {', '.join(f'{x}-{y}' for x, y in nossos) or '—'}; Wikipédia "
                               f"{', '.join(f'{x}-{y}' for x, y in sorted(pl))}" + "".join(f"; {o}" for o in outras))
            for d in dif[:15]:
                ocorr[a].append(f"placar diferente na matriz da Wikipédia — {d}")
            if len(dif) > 15:
                ocorr[a].append(f"... e mais {len(dif) - 15} pares com placar diferente na matriz da Wikipédia")

        if a in GRUPOS:
            T_, n, gols, ok, dv, campeao_g, _ = temporada_grupos(a, jogos, tbs, rs_hist.get(a, []), camp, tab, nomes, ocorr)
            gravar_partidas(a, jogos, tab, 0)
            linhas_rel.append((T, "ogol + RSSSF + Wikipédia", n, len(jogos), gols, 0, ok, dv, campeao_g, ""))
            print(f"{T}: {len(jogos)} jogos (grupos), tabelas {ok} ok / {dv} div, campeão {campeao_g}", flush=True)
            continue

        clubes_ano = sorted({j["m"] for j in regular} | {j["v"] for j in regular})
        n = len(clubes_ano)
        esperados = n * (n - 1)
        if len(regular) != esperados:
            ocorr[a].append(f"fase regular com {len(regular)} jogos de {esperados}")
        fase_reg = "Fase regular" if resto else "Liga"
        for j in regular:
            j["fase"] = fase_reg

        # ---- engsoccerdata e football-data (casados pelo par e pela data mais próxima)
        for fonte, dados_, cm, cv in (("engsoccerdata", esd, "hgoal", "vgoal"), ("football-data", fd, "FTHG", "FTAG")):
            if a not in dados_:
                continue
            usados = set()
            for m, v, d, x in dados_[a]:
                nomes[m][f"{fonte}:{x['home' if fonte == 'engsoccerdata' else 'HomeTeam']}"].add(a)
                b = casar(jogos, usados, m, v, d)
                if b is None:
                    ocorr[a].append(f"jogo do {fonte} sem par no ogol: {m} x {v} ({d})")
                    continue
                if fonte == "football-data":
                    b["fd"] = x
                if (int(x[cm]), int(x[cv])) != (b["gm"], b["gv"]) and not b.get("especial"):
                    ocorr[a].append(f"placar diferente no {fonte} — {m} x {v} ({b['data']}): ogol {b['gm']}-{b['gv']}, "
                                    f"{fonte} {x[cm]}-{x[cv]}")

        # ---- ESPN
        usados = set()
        for e in espn.get(a, []):
            m, v = mapa_espn.get(e["mandante_id"], a), mapa_espn.get(e["visitante_id"], a)
            if m is None or v is None:
                continue
            b = casar(jogos, usados, m, v, e["data"], 3)
            if b is None:
                continue
            nomes[m][f"espn:{e['mandante']}"].add(a)
            b["espn"] = e
            if (e["gm"], e["gv"]) != (b["gm"], b["gv"]) and not b.get("especial"):
                ocorr[a].append(f"placar diferente na ESPN — {m} x {v} ({b['data']}): ogol {b['gm']}-{b['gv']}, ESPN {e['gm']}-{e['gv']}")

        # ---- fase regular: tabelas publicadas e ordem
        ref = calcular(regular, pv)
        w_reg = max((tb for tb in tbs if len(tb["times"]) >= n - 2), default=None,
                    key=lambda tb: len({x["clube"] for x in tb["times"]} & set(clubes_ano)))
        if w_reg and len({x["clube"] for x in w_reg["times"]} & set(clubes_ano)) < n - 2:
            w_reg = None
        ajuste: dict[str, int] = {}
        if w_reg:
            for x in w_reg["times"]:
                if x["clube"] is None:
                    raise SystemExit(f"{T}: nome da Wikipédia sem cadastro: {x['nome']}")
                nomes[x["clube"]][f"wikipedia:{x['nome']}"].add(a)
                if x["ajuste"] and (a, x["clube"]) not in IGNORAR_AJUSTE:
                    ajuste[x["clube"]] = x["ajuste"]
        rs = None
        if rs_hist.get(a):
            linhas = linhas_rsssf(rs_hist[a][0], a)
            for x in linhas:
                nomes[x["clube"]][f"rsssf:{x['nome']}"].add(a)
            if {x["clube"] for x in linhas} == set(clubes_ano):
                rs = linhas
            else:
                ocorr[a].append(f"tabela da RSSSF com outros clubes: {sorted({x['clube'] for x in linhas} ^ set(clubes_ano))}")
        if rs:
            for x in rs:   # punição que só a RSSSF traz
                c = ref.get(x["clube"])
                if c and [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"]] == c[:6] \
                        and x["pontos"] < c[6] and x["clube"] not in ajuste:
                    ajuste[x["clube"]] = x["pontos"] - c[6]
                    ocorr[a].append(f"punição tirada da tabela da RSSSF: {x['clube']} {x['pontos'] - c[6]:+d} pontos")
        conferidas = divergentes = 0
        confere = {}
        url_w = f"https://en.wikipedia.org/wiki/{wiki_titulo(a).replace(' ', '_')}"
        for fonte, url, linhas in (("RSSSF", URL_RSSSF, rs), ("Wikipédia", url_w, linhas_wiki(w_reg, pv) if w_reg else None)):
            if not linhas:
                continue
            ok = conferir(T, linhas, ref, ajuste, fonte, url, fase_reg, None, tab, ocorr[a], "tabela publicada")
            confere[fonte] = ok
            conferidas += ok
            divergentes += not ok
        if not confere:
            ocorr[a].append("sem tabela publicada legível (RSSSF e Wikipédia)")
        if w_reg and (confere.get("Wikipédia") or not confere.get("RSSSF")):
            ordem = [x["clube"] for x in w_reg["times"]]
            fonte_ordem = "Wikipédia (ordem oficial)"
        elif rs:
            ordem = [x["clube"] for x in sorted(rs, key=lambda x: x["posicao"])]
            fonte_ordem = "RSSSF (ordem oficial)"
            if w_reg:
                ocorr[a].append("a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF")
        else:
            ordem = ordenar(ref, ajuste, "vitorias", regular, pv)
            fonte_ordem = "calculada"
        if set(ordem) != set(clubes_ano):
            ocorr[a].append(f"ordem oficial com outros clubes ({sorted(set(ordem) ^ set(clubes_ano))}): fica a calculada")
            ordem = ordenar(ref, ajuste, "confronto", regular, pv)
            fonte_ordem = "calculada"
        tentativas = {cr: ordenar(ref, ajuste, cr, regular, pv) for cr in ("confronto", "saldo", "vitorias", "media")}
        ok_cr = [cr for cr, o in tentativas.items() if o == ordem]
        criterio = ok_cr[0] if ok_cr else min(tentativas, key=lambda cr: sum(x != y for x, y in zip(tentativas[cr], ordem)))
        if not ok_cr:
            dif = [c for c, d in zip(ordem, tentativas[criterio]) if c != d]
            ocorr[a].append(f"nenhum critério calculado reproduz a ordem oficial; o mais próximo ({criterio}) difere em "
                            f"{len(dif)} posições (ex.: {dif[:2]})")
        criterios[a] = (criterio, bool(ok_cr))

        # ---- play-offs (2011/12): cada grupo de play-off casa com a tabela da Wikipédia de mesmos clubes
        fases_po = []
        pontos_po: dict[str, int] = {}
        ajuste_po: dict[str, int] = {}
        if resto:
            for tb in tbs:
                conj = {x["clube"] for x in tb["times"]}
                if tb is w_reg or len(conj) >= n or tb["secao"] == "":
                    continue
                comp = [j for j in resto if {j["m"], j["v"]} <= conj]
                if not comp:
                    continue
                fase = "Play-off do título" if ordem[0] in conj else "Play-off europeu"
                for j in comp:
                    j["fase"] = fase
                fases_po.append((fase, comp, tb))
                calc_po = calcular(comp, pv)
                ok = conferir(T, linhas_wiki(tb, pv), calc_po, {x["clube"]: x["ajuste"] for x in tb["times"]}, "Wikipédia",
                              url_w, fase, None, tab, ocorr[a], f"tabela do {fase}")
                conferidas += ok
                divergentes += not ok
                if fase == "Play-off do título":
                    for x in tb["times"]:
                        pontos_po[x["clube"]] = calc_po[x["clube"]][6] + x["ajuste"]
                        ajuste_po[x["clube"]] = x["ajuste"]
            sobra = [j for j in resto if j["fase"] == "Play-off"]
            if sobra:
                ocorr[a].append(f"{len(sobra)} jogos de play-off sem tabela na Wikipédia")

        # ---- classificação final
        po_titulo = next((tb for f, comp, tb in fases_po if f == "Play-off do título"), None)
        if po_titulo:
            topo = [x["clube"] for x in po_titulo["times"]]
            ordem_final = topo + [c for c in ordem if c not in topo]
            fonte_final = "Wikipédia (play-off do título; depois a fase regular)"
        else:
            ordem_final, fonte_final = ordem, fonte_ordem
        total = calcular(jogos, pv)
        prox = a + 1
        prox_clubes = {j[k] for j in ogol[prox] for k in ("m", "v")} if prox in ogol else prox_2026
        rebaixados = {c for c in clubes_ano if c not in prox_clubes and (a, c) not in NAO_REBAIXADOS}
        for (b_, c), motivo in NAO_REBAIXADOS.items():
            if b_ == a:
                ocorr[a].append(f"{c} não está na temporada seguinte, mas não caiu: {motivo}")
        campeao = ordem_final[0]
        if camp.get(a) and camp[a] != campeao:
            ocorr[a].append(f"campeão diferente na lista de campeões da RSSSF: {camp[a]} (classificação: {campeao})")
        for pos, c in enumerate(ordem_final, 1):
            j_, v_, e_, d_, gp, gc, p = total[c]
            if c in pontos_po:
                pts = pontos_po[c]
                obs = (f"pontos do play-off do título: {ajuste_po[c]} de partida (a metade dos pontos da fase regular) mais "
                       f"os do play-off")
            else:
                pts = ref[c][6] + ajuste.get(c, 0)
                obs = None
            nota = (w_reg and next((notas_wiki.traduzir(x["nota"] or x["hth"]) for x in w_reg["times"] if x["clube"] == c), None))
            tab["classificacao_final"].append({
                "temporada": T, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
                "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": pts, "ajuste_pontos": pts - p,
                "situacao": "campeao" if pos == 1 else "rebaixado" if c in rebaixados else None, "fonte": fonte_final,
                "observacao": "; ".join(x for x in (obs, nota) if x) or None})

        # ---- partidas, gols, cartões, estatísticas
        gols_ano, autor_ano = gravar_partidas(a, jogos, tab, 1)

        # ---- classificação rodada a rodada (fase regular)
        if regular and all(j["rodada"] for j in regular):
            pos_reb = {p for p, c in enumerate(ordem, 1) if c in rebaixados}
            for r in sorted({j["rodada"] for j in regular}):
                ate = [j for j in regular if j["rodada"] <= r]
                parcial = calcular(ate, pv)
                for pos, c in enumerate(ordenar(parcial, ajuste, criterio, ate, pv), 1):
                    jj, v_, e_, d_, gp, gc, p = parcial[c]
                    tab["classificacao_rodada"].append({
                        "temporada": T, "rodada": r, "clube": clubes.exibicao(c), "posicao": pos, "pontos": p + ajuste.get(c, 0),
                        "jogos": jj, "vitorias": v_, "empates": e_, "derrotas": d_, "gols_pro": gp, "gols_contra": gc,
                        "zona": "titulo" if pos == 1 else "rebaixamento" if pos in pos_reb else "meio"})

        # ---- edição, fases, conferência
        fontes_ed = ["ogol"] + (["engsoccerdata"] if a in esd else []) + (["football-data"] if a in fd else []) \
            + (["ESPN"] if a in espn else []) + (["RSSSF"] if rs else []) + (["Wikipédia"] if w_reg or mz else [])
        pun = "; ".join(f"{c} {v:+d} pontos" for c, v in ajuste.items())
        formato = ("fase regular em turno e returno e play-offs (o do título começa com a metade dos pontos da fase regular)"
                   if fases_po else "pontos corridos (turno e returno)")
        tab["edicoes"].append({"temporada": T, "ano_inicio": a, "ano_fim": a + 1, "nome_oficial": nome_oficial(a), "num_clubes": n,
                               "pontos_vitoria": pv, "formato": formato, "campeao": clubes.exibicao(campeao),
                               "vice": clubes.exibicao(ordem_final[1]), "fontes": " + ".join(dict.fromkeys(fontes_ed)),
                               "observacao": "; ".join(x for x in (f"punições: {pun}" if pun else "",
                                                                    "; ".join(m for (b_, c_), (d_, m) in DADOS_FORA.items()
                                                                              if b_ == a)) if x) or None})
        crit_txt = {"vitorias": "pontos, vitórias, saldo de gols, gols pró", "saldo": "pontos, saldo de gols, gols pró",
                    "confronto": "pontos, confronto direto, saldo de gols, gols pró",
                    "media": "pontos, média de gols (goal average)"}[criterio]
        tab["fases"].append({"temporada": T, "ordem": 1, "fase": fase_reg, "tipo": "liga", "num_grupos": None,
                             "formato_serie": "pontos_corridos", "criterio": crit_txt})
        for i, (fase, comp, tb) in enumerate(fases_po, 2):
            tab["fases"].append({"temporada": T, "ordem": i, "fase": fase, "tipo": "grupos", "num_grupos": 1,
                                 "formato_serie": "pontos_corridos",
                                 "criterio": "pontos, com a metade dos pontos da fase regular de partida" if fase == "Play-off do título"
                                 else "pontos"})
        tab["conferencia"].append({"temporada": T, "jogos": len(jogos), "jogos_esperados": esperados,
                                   "tabelas_conferidas": conferidas, "tabelas_divergentes": divergentes, "gols": gols_ano,
                                   "gols_com_autor": autor_ano,
                                   "observacao": f"campeão {clubes.exibicao(campeao)} (RSSSF, lista de campeões: "
                                                 f"{clubes.exibicao(camp[a]) if camp.get(a) in clubes.CLUBES else camp.get(a, '—')})"})
        linhas_rel.append((T, " + ".join(dict.fromkeys(fontes_ed)), n, len(jogos), gols_ano, autor_ano, conferidas, divergentes,
                           clubes.exibicao(campeao), pun))
        print(f"{T}: {len(jogos)} jogos ({len(regular)} da fase regular), tabelas {conferidas} ok / {divergentes} div, "
              f"gols {gols_ano} ({autor_ano} c/ autor), critério {criterio}{'' if criterios[a][1] else ' (aprox.)'}, "
              f"campeão {clubes.exibicao(campeao)}", flush=True)

    # era antiga (antes de 1959): Türkiye Futbol Şampiyonası, Millî Küme e Federasyon Kupası (coleta/tur-1/antigo.py)
    import antigo
    linhas_rel = antigo.montar(tab, nomes, ocorr) + linhas_rel

    # ---- clubes
    for c, (cidade, pais) in sorted(clubes.CLUBES.items()):
        if c not in nomes:
            continue
        nf = "|".join(f"{k}:{faixa(v)}" for k, v in sorted(nomes[c].items()))
        tab["clubes"].append({"clube": clubes.exibicao(c), "regiao": None, "cidade": cidade, "pais": pais, "nomes_fonte": nf})
    tab["paises"] = [{"codigo": "TUR", "nome": "Turquia", "confederacao": "UEFA"}]
    tab["artilheiros"] = artilheiros(ocorr)
    gravar(PACOTE, COMPETICAO, tab)
    relatorio(linhas_rel, ocorr, tab, mapa_espn, criterios)


def gravar_partidas(a: int, jogos: list[dict], tab, _) -> tuple[int, int]:
    """Partidas, gols e cartões (ESPN) e estatísticas (football-data) de uma temporada."""
    T = temporada(a)
    jogos.sort(key=lambda j: (j["data"] or "9999", j["rodada"] or 0, j["m"]))
    gols_ano = autor_ano = 0
    for i, j in enumerate(jogos, 1):
        pid = f"{a}-{i:04d}"
        o, e, x = j.get("ogol"), j.get("espn"), j.get("fd")
        hora = None
        if x and x.get("Time"):
            hora = datetime.fromisoformat(f"{data_fd(x['Date'])}T{x['Time']}").replace(tzinfo=LONDRES).astimezone(ISTAMBUL).strftime("%H:%M")
        elif e:
            local = e["utc"].astimezone(ISTAMBUL)
            if local.date().isoformat() == j["data"]:
                hora = local.strftime("%H:%M")
        ids = ([f"ogol:{o['id']}"] if o else []) + ([f"espn:{e['id']}"] if e else [])
        fontes = [j["fonte"]] + (["football-data"] if x else []) + (["ESPN"] if e else [])
        tab["partidas"].append({
            "id": pid, "temporada": T, "fase": j["fase"], "grupo": j["grupo"], "rodada": j["rodada"], "data": j["data"],
            "hora": hora, "mandante": clubes.exibicao(j["m"]), "visitante": clubes.exibicao(j["v"]),
            "gols_mandante": j["gm"], "gols_visitante": j["gv"], "penaltis_mandante": None, "penaltis_visitante": None,
            "resultado_especial": j.get("especial"), "estadio": (e or {}).get("estadio"), "cidade": (e or {}).get("cidade"),
            "publico": (e or {}).get("publico") or None, "fonte": " + ".join(fontes), "fonte_id": "|".join(ids),
            "gols_texto": None, "observacao": j.get("obs"), "arbitro": (x or {}).get("Referee") or None})
        gols_ano += j["gm"] + j["gv"]
        if e and e["lances"] and not j.get("especial"):
            vistos_l = set()   # a ESPN repete lances (mesmo minuto, lado e jogador): repetidos saem
            lances = [l for l in e["lances"] if not ((k_ := (l["tipo"], l["minuto"], l["lado"], tuple(l["jogadores"] or ()),
                                                             l["gol"], l["amarelo"], l["vermelho"])) in vistos_l
                                                     or vistos_l.add(k_))]
            gl = [l for l in lances if l["gol"]]
            if len(gl) > j["gm"] + j["gv"]:   # repetidos com 1 minuto de diferença
                gl2 = []
                for l in gl:
                    if not any((k["lado"], k["tipo"], k["jogadores"]) == (l["lado"], l["tipo"], l["jogadores"])
                               and abs((minuto(k["minuto"])[0] or 0) - (minuto(l["minuto"])[0] or 0)) <= 1 for k in gl2):
                        gl2.append(l)
                if len(gl2) == j["gm"] + j["gv"]:
                    gl = gl2
            lado = {"home": j["m"], "away": j["v"]}
            if all(l["lado"] in lado for l in gl) and \
                    (sum(l["lado"] == "home" for l in gl), sum(l["lado"] == "away" for l in gl)) == (j["gm"], j["gv"]):
                for l in gl:
                    mi, ac = minuto(l["minuto"])
                    tab["gols"].append({"partida_id": pid, "clube": clubes.exibicao(lado[l["lado"]]),
                                        "jogador": (l["jogadores"] or [None])[0], "minuto": mi, "acrescimo": ac,
                                        "tipo": "contra" if l["contra"] else "penalti" if l["penalti"] else
                                        "falta" if "free-kick" in (l["tipo"] or "").lower() else "normal", "fonte": "ESPN"})
                autor_ano += len(gl)
            for l in lances:
                if (l["amarelo"] or l["vermelho"]) and l["lado"] in lado:
                    mi, ac = minuto(l["minuto"])
                    tab["cartoes"].append({"partida_id": pid, "clube": clubes.exibicao(lado[l["lado"]]),
                                           "jogador": (l["jogadores"] or [None])[0], "minuto": mi, "acrescimo": ac,
                                           "cor": "vermelho" if l["vermelho"] else "amarelo", "fonte": "ESPN"})
        if x and x.get("HS"):
            def num(k):
                v_ = x.get(k)
                return int(float(v_)) if v_ not in (None, "") else None
            for c, s in ((j["m"], "H"), (j["v"], "A")):
                tab["estatisticas"].append({"partida_id": pid, "clube": clubes.exibicao(c), "chutes": num(f"{s}S"),
                                            "chutes_alvo": num(f"{s}ST"), "faltas": num(f"{s}F"), "escanteios": num(f"{s}C"),
                                            "amarelos": num(f"{s}Y"), "vermelhos": num(f"{s}R"), "fonte": "football-data.co.uk"})
    return gols_ano, autor_ano


def artilheiros(ocorr) -> list[dict]:
    """Artilheiro(s) de cada temporada pela lista da RSSSF (tablest/turktops.html, seção da Süper Lig: "1959-60   Metin
    Oktay   Galatasaray   33"; empate na linha seguinte, sem temporada; "Kasimpasa/Galatas." = jogou nos dois)."""
    t = texto_rsssf(DADOS / "rsssf" / "turktops.html")
    t = t[t.index("\nSüper Lig"):]
    res, ano = [], None
    for l in t.split("\n"):
        m = re.match(r"^(?:(\d{4})(?:-(\d{2}))?)?\s+(\S.*?)\s{2,}(\S.*?)\s{2,}(\d+)\s*$", l)
        if not m:
            if l.strip() and not l.startswith(" "):
                ano = None
            continue
        if m.group(1):
            ano = int(m.group(1)) - (0 if m.group(2) else 1)
        if ano not in TEMPORADAS:
            continue
        nome, clube_txt, gols = m.group(3).strip(), m.group(4).strip(), int(m.group(5))
        c = None if "/" in clube_txt else clubes.esd(clube_txt, ano)
        res.append({"temporada": temporada(ano), "jogador": NOMES_ARTILHEIRO.get(nome, nome),
                    "clube": clubes.exibicao(c) if c else None, "gols": gols,
                    "fonte": "RSSSF (tablest/turktops.html)" + (f"; jogou em dois clubes ({clube_txt})" if "/" in clube_txt else "")})
        if c is None and "/" not in clube_txt:
            ocorr[ano].append(f"artilheiro com clube sem cadastro: {nome} ({clube_txt})")
    return res


def relatorio(linhas, ocorr, tab, mapa_espn, criterios) -> None:
    jogos = len(tab["partidas"])
    gols = sum(int(x["gols_mandante"]) + int(x["gols_visitante"]) for x in tab["partidas"])
    cr = Counter(c for c, _ in criterios.values())
    out = [
        "# Campeonato Turco (1ª divisão) — coleta de dados", "",
        "Gerado por `python coleta/tur-1/importar.py`. Pacote em `data/coleta/tur-1/pacote/`.", "",
        f"**Edições:** {len(linhas)}, de 1959 a 2025/26 (a liga nacional; os campeonatos anteriores a 1959 não são contados "
        "pela federação e ficam de fora).", "",
        f"**Total:** {jogos} jogos, {gols} gols, {len(tab['gols'])} gols com autor (ESPN), {len(tab['cartoes'])} cartões, "
        f"{len(tab['clubes'])} clubes.", "",
        "**Fontes:**",
        "- ogol (zerozero): base dos jogos, com data e rodada; o clube pelo código do ogol (os nomes do calendário não são "
        "confiáveis nas temporadas antigas); calendários em `data/cache/ogol-tur-1/` para os escudos;",
        "- RSSSF: tabelas finais de 1959 a 1996/97 (turkhist.html, com os grupos de 1959 e 1962/63), lista de campeões e de "
        "artilheiros;",
        "- Wikipédia (en): tabelas e matriz de resultados de cada temporada (conferência jogo a jogo);",
        "- engsoccerdata e football-data: conferência de placar de 1994/95 em diante; hora, árbitro e estatísticas do "
        "football-data;",
        "- ESPN (liga `tur.1`): hora, estádio, público, gols e cartões com minuto, nas temporadas que ela cobre.", "",
        "**Regras:** cada tabela publicada é comparada com a tabela calculada dos jogos. A ordem da classificação final é a "
        "oficial (Wikipédia; sem ela, RSSSF). 2 pontos por vitória até 1986/87, 3 a partir de 1987/88. Rebaixado = clube que "
        "não está na 1ª divisão na temporada seguinte.", "",
        f"**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em "
        f"{cr['confronto']}, saldo em {cr['saldo']}, vitórias em {cr['vitorias']}, média de gols em {cr['media']}).", "",
        "| Temporada | Fontes | Clubes | Jogos | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for T, f, n, j, g, au, ok, dv, camp, pun in linhas:
        out.append(f"| {T} | {f} | {n} | {j} | {g} | {au} | {ok} / {dv} | {camp} | {pun or '—'} |")
    out += ["", "## Conferência e ocorrências, temporada a temporada", ""]
    for T, *_ in linhas:
        a = 1958 if T == "1959" else int(T[:4])
        out.append(f"### {T}")
        out.append("")
        for o in ocorr.get(T, []) or ocorr.get(a, []) or ["sem ocorrências"]:
            out.append(f"- {o}")
        out.append("")
    out += [
        "## Identidade dos clubes", "",
        "- Cadastro em `coleta/comum-europa/clubes_tur.py`, pela linhagem legal do clube (como na Wikipédia). Kayseri: o "
        "Kayserispor de 1966 (1ª divisão de 1973/74 a 1997/98) trocou de nome, escudo e cores com o Erciyesspor em 2004 e "
        "virou o Kayseri Erciyesspor; o Kayserispor de 2004/05 em diante é o antigo Erciyesspor.",
        f"- A ESPN é casada por votação jogo a jogo (mesma data e placar): {len(mapa_espn)} códigos.",
        "- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.", "",
        "## O que não deu para coletar", "",
        "- **Jogos do grupo de classificação de 1962/63:** nem o ogol nem a Wikipédia têm; entra a tabela.",
        "- **Autores dos gols antes da ESPN:** nenhuma fonte em lote (ficha do ogol, jogo a jogo).",
        "- **Campeonatos anteriores a 1959** (Türkiye Futbol Şampiyonası e Millî Küme): fora do escopo; a federação não os "
        "conta.",
    ]
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
