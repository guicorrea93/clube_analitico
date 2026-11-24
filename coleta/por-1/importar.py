"""Monta o pacote da 1ª divisão portuguesa (por-1), 1934/35 a 2025/26, e o relatório docs/coleta/por-1.md.

Base dos jogos: o calendário do ogol (zerozero), com a rodada oficial e o código de cada clube. Cada jogo é casado pelo
par mandante x visitante, que é único na temporada (turno e returno), com:
  RSSSF          tabela final e matriz de resultados de 1934/35 a 2004/05 (porthist*.html: conferência jogo a jogo); tabela
                 final das temporadas seguintes; listas de campeões e de artilheiros;
  engsoccerdata  1994/95-2024/25: conferência de placar;
  football-data  1994/95-2025/26: conferência de placar; hora (2019/20+), árbitro e estatísticas por time;
  ESPN           2006/07+: hora, estádio, público, gols e cartões com minuto (clubes casados pelo código da ESPN);
  Wikipédia      tabela final de cada temporada (ordem oficial, punições, marca de rebaixamento).

Regras: o placar é o do ogol; jogo decidido fora de campo entra com o resultado oficial (TRIBUNAL, com o motivo da ficha do
ogol). Os gols da ESPN só entram quando a soma bate com o placar.

Uso: python coleta/por-1/importar.py
"""
from __future__ import annotations

import csv
import html
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
import clubes_por as clubes  # noqa: E402
from edicoes import DADOS, RAIZ, TEMPORADAS, nome_oficial, rsssf_url, temporada, wiki_titulo  # noqa: E402
from pacote import gravar  # noqa: E402
import notas_wiki  # noqa: E402
import ogol_ficha  # noqa: E402
import rsssf_gols  # noqa: E402
from rsssf_por import ler as ler_hist  # noqa: E402
from wiki_tabela import limpar, tabelas as wiki_tabelas  # noqa: E402

LONDRES = ZoneInfo("Europe/London")
LISBOA = ZoneInfo("Europe/Lisbon")
ACORES = ZoneInfo("Atlantic/Azores")   # jogos em casa do Santa Clara (Ponta Delgada): hora local dos Açores
PACOTE = DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / "por-1.md"
FD = range(1994, 2026)
ESD = range(1994, 2025)

# placar corrigido no ogol: (ano, mandante, visitante) -> (gols, gols, motivo). Chaves de clubes_por.
CORRECOES: dict[tuple, tuple] = {
    # revisão PT-007: a ficha do ogol do jogo de Espinho lista só 2 gols; transfermarkt e as matrizes das Wikipédias pt e en
    (1980, "Benfica", "Espinho"): (2, 1, "o ogol e a matriz da RSSSF trazem 2-0; o transfermarkt e as matrizes das Wikipédias pt "
                                         "e en, 2-1 (os totais não mudam)"),
    (1980, "Espinho", "Benfica"): (2, 0, "o ogol e a matriz da RSSSF trazem 3-0; a ficha do ogol lista só 2 gols (Vitorino "
                                         "Belinha 2', Carlos Coelho 59'), como o transfermarkt e as Wikipédias pt e en"),
    (1995, "Leça", "Boavista"): (0, 3, "o ogol traz 0-2; a matriz e a tabela da RSSSF, a tabela da Wikipédia, o engsoccerdata e o "
                                       "football-data trazem 0-3"),
}

# jogo sem placar no ogol ("DA") cujo resultado de campo valeu: (ano, mandante, visitante) -> (gols, gols, motivo)
CAMPO: dict[tuple, tuple] = {}

# resultado dado fora de campo: (ano, mandante, visitante) -> (gols, gols, vencedor, placar de campo, motivo). Fica `awd`.
# gols None = fica o placar do ogol; vencedor "m"/"v" = vitória dada com o placar mantido; "nenhum" = derrota para os dois
TRIBUNAL: dict[tuple, tuple] = {
    (1960, "Atlético CP", "Leixões"): (
        0, 0, "v", "0-0", "o resultado não foi homologado e os pontos da vitória foram dados ao Leixões (ficha do ogol: \"derrota "
                          "administrativa (0-0)\"). A matriz da RSSSF traz 0-3 neste jogo e 3-1 no Leixões x Atlético (o ogol, 6-1); "
                          "as duas versões dão os mesmos totais, e as tabelas da RSSSF e da Wikipédia fecham com elas. Fica o ogol"),
    (1974, "CUF", "Vitória de Setúbal"): (
        1, 1, "m", "1-1", "derrota administrativa do Vitória de Setúbal (ficha do ogol: \"Vitória FC: derrota administrativa "
                          "(0-0)\", 1-1 no intervalo). A matriz da RSSSF, o transfermarkt e as Wikipédias trazem outra versão "
                          "dos dois jogos (CUF 0-2 Vitória e Vitória 1-2 CUF), que dá os mesmos totais e também fecha com as tabelas. "
                          "Fica o ogol, que registra a decisão (revisão PT-009)"),
    (1986, "Braga", "Benfica"): (
        1, 1, "nenhum", "1-1", "interrompido aos 86 minutos por invasão de campo; a Federação deu derrota aos dois clubes "
                               "(Diário de Lisboa, 18/07/1987; ficha do ogol; Wikipédia pt). O Benfica é campeão nos dois casos "
                               "(revisão PT-004, decisão D-20 b)"),
    (1975, "Atlético CP", "Sporting"): (
        3, 0, None, None, "derrota do Sporting por invasão de campo (ficha do ogol: 3-0); a matriz da RSSSF traz 3-0"),
    (1986, "Belenenses", "Marítimo"): (
        0, 3, None, "1-0", "o Belenenses escalou irregularmente o jogador Mapuata e perdeu por 0-3 (ficha do ogol; matriz da RSSSF)"),
    (1989, "Nacional da Madeira", "Belenenses"): (
        3, 0, None, "1-1", "o Belenenses escalou irregularmente o avançado Macaé e perdeu por 3-0 (ficha do ogol; matriz da RSSSF)"),
    (2007, "Belenenses", "Naval 1º de Maio"): (
        0, 3, None, "2-1", "o Belenenses escalou um jogador irregular (16ª rodada): derrota por 0-3 (ficha do ogol; RSSSF: \"awarded "
                           "0-3; originally 2-1\") e mais 3 pontos descontados (RSSSF e Wikipédia)"),
}

# jogo que falta no ogol: (ano, mandante, visitante) -> (data, gols, gols, rodada, motivo)
ACRESCIMOS: dict[tuple, tuple] = {
    (2013, "Benfica", "Sporting"): (
        "2014-02-11", 2, 0, 18, "falta no calendário do ogol; o football-data e o engsoccerdata trazem 2-0 em 11/02/2014 (o jogo da "
                                "18ª rodada, adiado); as tabelas da RSSSF e da Wikipédia só fecham com ele"),
}

# temporada com a ordem oficial da RSSSF (e da Wikipédia pt), e não a da Wikipédia en: ano -> motivo
ORDEM_RSSSF: dict[int, str] = {
    1944: "2º Sporting e 3º Belenenses (27 pontos), 6º Olhanense e 7º Estoril (16): confronto direto, como na RSSSF (lista de "
          "campeões: \"runners-up: Sporting CP\") e na Wikipédia pt (revisão PT-003)",
    2005: "13º Naval e 14º Académica (39 pontos, com o Belenenses): confronto direto entre os três (Naval 7, Académica 5, "
          "Belenenses 4), como na RSSSF e na Wikipédia pt (revisão PT-005, decisão D-19 c)",
}
# posições que mudam com uma decisão de tribunal que a tabela da Wikipédia en não conta: ano -> {posição: clube}
ORDEM_FIXA: dict[int, dict] = {
    1986: {9: "Académica", 10: "Portimonense", 11: "Braga", 12: "Rio Ave", 13: "Marítimo"},   # Wikipédia pt (PT-004)
}
# ajuste de pontos que vale hoje, diferente do da tabela publicada: (ano, clube) -> (ajuste, observação) (PT-006, D-20 a)
AJUSTES: dict[tuple, tuple] = {
    (2007, "Porto"): (0, "6 pontos descontados em 2008 (caso Apito Final) e devolvidos em 2017 pelo Conselho de Justiça da FPF"),
}
# observação na classificação final (revisão PT-016, PT-017, PT-018 e PT-006)
OBS_CLASSIF: dict[tuple, str] = {
    (1950, "Vitória de Setúbal"): "rebaixado em 12º; a Wikipédia pt confirma a queda (o Vitória de Guimarães, 13º, ficou)",
    (1961, "Beira-Mar"): "rebaixado em 11º; a Wikipédia pt confirma a queda (o Lusitano de Évora, 12º, ficou)",
    (1973, "Beira-Mar"): "rebaixado em 13º; a Wikipédia pt confirma a queda (o Leixões, 14º, ficou)",
    (1997, "Leça"): "rebaixado administrativamente (corrupção num jogo da 2ª Divisão B em 1993); o Chaves, 16º, ficou no lugar",
    (1997, "Chaves"): "16º, ficou na 1ª divisão no lugar do Leça, rebaixado administrativamente",
    (2005, "Gil Vicente"): "rebaixado no lugar do Belenenses (caso Mateus, jogador inscrito irregularmente)",
    (2005, "Belenenses"): "15º, ficou na 1ª divisão: o Gil Vicente caiu no lugar (caso Mateus)",
    (2007, "Boavista"): "rebaixado pelo caso Apito Final (terminou em 9º)",
    (2007, "União de Leiria"): "3 pontos a menos (caso Apito Final)",
    (2008, "Estrela da Amadora"): "rebaixado por dívidas (terminou em 11º); o Belenenses, 15º, ficou",
    (2019, "Vitória de Setúbal"): "rebaixado por não cumprir as regras de licenciamento; o Portimonense, 17º, ficou",
    (2019, "Desportivo das Aves"): "rebaixado por não cumprir as regras de licenciamento",
    (2023, "Estrela da Amadora"): "Club Football Estrela da Amadora (da fusão de 2020), contado junto do CF Estrela da Amadora de "
                                  "1932, como no ogol (decisão D-24 c)",
    (1946, "SL Elvas"): "fundiu-se em 1947 com o Elvas FC no O Elvas CAD, que ficou com o lugar na 1ª divisão (decisão D-24 d)",
}
# datas corrigidas (revisão PT-010 e PT-011): data/coleta/por-1/correcoes/datas.csv
CORRECOES_DIR = DADOS / "correcoes"
DATAS: dict[str, list] = {}
# artilheiro com o número errado na lista da RSSSF: (ano, jogador) -> (gols, motivo) (revisão PT-012)
GOLS_ARTILHEIRO = {(2018, "Haris Seferovic"): (23, "a RSSSF dá 33 (erro de digitação); a Bola de Prata, a Wikipédia pt e os "
                                                   "gols da ESPN dão 23")}
FICHAS = RAIZ / "data" / "cache" / "ogol-por-1" / "fichas"

# 1934/35 a 1944/45: os participantes saíam dos campeonatos regionais (não havia acesso e rebaixamento)
SEM_REBAIXAMENTO = set(range(1934, 1945))
# clube que não está na temporada seguinte sem ter sido rebaixado: (ano, clube) -> motivo
NAO_REBAIXADOS = {
    (1946, "SL Elvas"): "terminou em 10º; em 1947 fundiu-se com o Elvas FC no O Elvas CAD, que ficou com o lugar na 1ª divisão",
    (2017, "Belenenses"): "a SAD separou-se do clube em 2018 e seguiu na 1ª divisão como Belenenses SAD (clube à parte); o CF Os "
                          "Belenenses recomeçou nas divisões distritais, sem ter sido rebaixado em campo",
}

# explicação de cada divergência que sobra entre fontes (vai para o relatório, antes das ocorrências da temporada)
WIKI_ERRA = "a tabela da Wikipédia erra gols, vitórias ou empates de algum clube; a da RSSSF fecha com os jogos"
EXPLICACOES: dict[int, list[str]] = {
    1938: ["Belenenses x Sporting (6ª rodada) em 06/02/1939, um dia depois de os dois jogarem a 5ª: a data é do ogol, o "
           "transfermarkt repete e não há terceira fonte (revisão PT-010). Fica a data do ogol"],
    1939: ["Académico do Porto com dois jogos em 04/02/1940 (x Sporting, 2ª rodada, e Porto x Académico, 3ª): as datas são do "
           "ogol, o transfermarkt repete e não há terceira fonte (revisão PT-010). Ficam as do ogol"],
    1947: [WIKI_ERRA + " (Atlético CP)"],
    1986: ["Braga x Benfica (31/05/1987): derrota para os dois no tribunal; as tabelas da RSSSF e da Wikipédia en contam o 1-1 "
           "de campo e não fecham nesses dois clubes; a da Wikipédia pt conta a decisão (Benfica 48, Braga 25 e 11º)"],
    1990: ["a tabela da Wikipédia troca os números do Marítimo e do Farense; a da RSSSF fecha com os jogos",
           "a matriz da RSSSF traz trocadas as colunas 13 e 14 (Gil Vicente e Famalicão): desfeita a troca, os 380 placares batem "
           "com o ogol"],
    1992: [WIKI_ERRA + " (Porto: 57 gols pró; os jogos dão 59)"],
    1994: ["Benfica 1-2 Sporting (30/04/1995): o ogol, o transfermarkt, a Wikipédia pt e o artigo da temporada do Benfica (\"perdeu "
           "os dois jogos contra o Sporting\") dão 1-2; a matriz e a tabela da RSSSF, o engsoccerdata e o football-data, 2-0. "
           "Fica o 1-2 (revisão PT-002)"],
    1995: [WIKI_ERRA + " (Benfica)"],
    1998: [WIKI_ERRA + " (Académica: 70 gols contra; os jogos dão 71)"],
    2005: ["Académica, Naval e Belenenses terminaram com 39 pontos; a Wikipédia (e os sites que a repetem) põe a Académica em 13º "
           "e o Naval em 14º, a RSSSF o contrário (que é o que dá o confronto direto entre os três). Fica a da RSSSF",
           "o Belenenses terminou em 15º, na zona de rebaixamento, e ficou na 1ª divisão: o Gil Vicente foi rebaixado no lugar "
           "dele (caso Mateus, jogador inscrito irregularmente)"],
    2007: ["Porto com 75 pontos: os 6 descontados em 2008 (caso Apito Final) foram devolvidos em 2017 pelo Conselho de Justiça "
           "da FPF, como nas Wikipédias pt e en (decisão D-20 a); União de Leiria com 3 pontos a menos, como na RSSSF (sem fonte "
           "da devolução). A ordem é a mesma nos dois casos",
           "Boavista rebaixado pelo caso Apito Final (terminou em 9º); o Paços de Ferreira, 15º, ficou na 1ª divisão"],
    2008: ["a tabela da RSSSF dá 46 pontos ao Leixões (os jogos dão 45, como na Wikipédia)",
           "Estrela da Amadora rebaixado por dívidas (terminou em 11º); o Belenenses, 15º, ficou na 1ª divisão"],
    2019: ["a tabela da Wikipédia dá um gol pró e um contra a menos ao Gil Vicente e ao Paços de Ferreira; os jogos fecham com a "
           "RSSSF, o football-data e o engsoccerdata",
           "Vitória de Setúbal e Desportivo das Aves rebaixados por não cumprirem as regras de licenciamento; o Portimonense, 17º, "
           "ficou na 1ª divisão"],
}

COMPETICAO = {
    "slug": "por-1", "nome": "Campeonato Português", "nome_curto": "Português", "tipo": "liga", "nivel": 1,
    "pais": "POR", "pais_nome": "Portugal", "regiao": None, "confederacao": "UEFA",
    "rotulo_painel": "Português", "menu_painel": "Portugal · 1ª divisão",
    "do_painel": "do Campeonato Português", "o_painel": "o Campeonato Português",
    "observacao": "1ª divisão portuguesa desde o Campeonato da Liga (1934/35 a 1937/38, experimental; os títulos contam entre "
                  "os da 1ª divisão): Primeira Divisão de 1938/39 a 1998/99 e Primeira Liga depois. Até 1944/45 os "
                  "participantes saíam dos campeonatos regionais. Não inclui os play-offs de manutenção contra clubes da 2ª "
                  "divisão.",
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
def carregar_ogol(a: int) -> list[dict]:
    res = []
    for o in json.loads((DADOS / "ogol" / f"por1_{a}.json").read_text(encoding="utf-8")):
        m, v = clubes.ogol(o["mandante_id"]), clubes.ogol(o["visitante_id"])
        if m is None or v is None:
            raise SystemExit(f"{temporada(a)}: código do ogol sem cadastro: {o['mandante']} ({o['mandante_id']}) x "
                             f"{o['visitante']} ({o['visitante_id']})")
        res.append({"data": o["data"], "m": m, "v": v, "nm": o["mandante"], "nv": o["visitante"], "gm": o["gols_mandante"],
                    "gv": o["gols_visitante"], "rodada": o["rodada"], "fase": "Liga", "grupo": None, "fonte": "ogol", "ogol": o})
    return res


def carregar_base() -> dict[int, list[dict]]:
    base = {a: carregar_ogol(a) for a in TEMPORADAS}
    for (a, m, v), (d, gm, gv, r, motivo) in ACRESCIMOS.items():
        base[a].append({"data": d, "m": m, "v": v, "nm": m, "nv": v, "gm": gm, "gv": gv, "rodada": r, "fase": "Liga",
                        "grupo": None, "fonte": "football-data", "acrescimo": motivo})
    return base


def carregar_fd() -> dict[int, dict]:
    res = {}
    for a in FD:
        cod = f"{str(a)[-2:]}{str(a + 1)[-2:]}"
        jogos = {}
        for x in ler_csv(DADOS / "football-data" / f"P1_{cod}.csv"):
            if not x.get("HomeTeam") or not x.get("FTHG"):
                continue
            jogos[(chave(x["HomeTeam"], a, "football-data"), chave(x["AwayTeam"], a, "football-data"))] = x
        res[a] = jogos
    return res


def carregar_esd() -> dict[int, dict]:
    res = defaultdict(dict)
    for x in ler_csv(DADOS / "engsoccerdata" / "portugal_tier1.csv"):
        a = int(x["Season"])
        res[a][(chave(x["home"], a, "engsoccerdata"), chave(x["visitor"], a, "engsoccerdata"))] = x
    return res


class Mapa(dict):
    """Código do clube na outra fonte -> chave. `get(cod, ano)` usa o voto da temporada quando há."""
    def __init__(self, geral: dict, por_ano: dict):
        super().__init__(geral)
        self.por_ano = por_ano

    def get(self, cod, ano=None):
        return self.por_ano.get((cod, ano)) or super().get(cod)


def votar(base: dict[int, list[dict]], outra: dict[int, list[dict]], campo_m: str, campo_v: str) -> Mapa:
    """Código do clube na outra fonte -> chave, por votação: jogo de mesma data (±1 dia) e mesmo placar, quando só um
    jogo da base serve."""
    votos: dict[str, Counter] = defaultdict(Counter)
    votos_ano: dict[tuple, Counter] = defaultdict(Counter)
    for a, jogos in outra.items():
        por_dia = defaultdict(list)
        for b in base.get(a, []):
            por_dia[(b["data"], b["gm"], b["gv"])].append(b)
        for j in jogos:
            if j.get("gm") is None:
                continue
            d = date.fromisoformat(j["data"])
            cand = [b for k in (-1, 0, 1) for b in por_dia.get(((d + timedelta(days=k)).isoformat(), j["gm"], j["gv"]), [])]
            if len(cand) == 1:
                for campo, lado in ((campo_m, "m"), (campo_v, "v")):
                    votos[j[campo]][cand[0][lado]] += 1
                    votos_ano[(j[campo], a)][cand[0][lado]] += 1
    return Mapa({k: c.most_common(1)[0][0] for k, c in votos.items()},
                {k: c.most_common(1)[0][0] for k, c in votos_ano.items()})


def carregar_espn() -> dict[int, list[dict]]:
    res = {}
    for a in range(2001, 2026):
        arq = DADOS / "espn" / f"por1_{a}.json"
        if not arq.exists():
            continue
        jogos = []
        for j in json.loads(arq.read_text(encoding="utf-8")):
            if j["situacao"] not in ("STATUS_FULL_TIME", "STATUS_FINAL"):
                continue
            utc = datetime.fromisoformat(j["data_hora"].replace("Z", "+00:00"))
            jogos.append(dict(j, data=utc.astimezone(LISBOA).date().isoformat(), utc=utc, gm=int(j["gols_mandante"]),
                              gv=int(j["gols_visitante"])))
        if jogos:
            res[a] = jogos
    return res


def carregar_wiki() -> dict[int, list[dict]]:
    res = {}
    for a in TEMPORADAS:
        arq = DADOS / "wikipedia" / f"{wiki_titulo(a)}.wiki"
        if not arq.exists():
            continue
        txt = arq.read_text(encoding="utf-8")
        modelo = arq.with_name(f"{wiki_titulo(a)} (tabela).wiki")   # tabela num modelo à parte (temporadas recentes)
        if modelo.exists():
            txt += "\n" + modelo.read_text(encoding="utf-8")
        tabs = wiki_tabelas(txt)
        if tabs:
            res[a] = tabs
    return res


def texto_rsssf(nome: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", (DADOS / "rsssf" / nome).read_bytes().decode("latin-1"))).replace("\r", "")


def campeoes_rsssf() -> dict[int, str]:
    """Campeão de cada temporada pela lista da RSSSF (portchamp.html): "1938/39  FC Porto  (runners-up: ...)" e, na
    seção do Campeonato da Liga, "1934/35  FC Porto"."""
    t = texto_rsssf("portchamp.html")
    t = t[t.find("Campeonato da Ia Liga 1934-1938 (unofficial)"):]
    res = {}
    for m in re.finditer(r"^(\d{4})/\d{2}\s+(.+?)\s*(?:\(runners-up|$)", t, re.M):
        a = int(m.group(1))
        if a in TEMPORADAS and a not in res:
            res[a] = clubes.esd(m.group(2).strip(), a)
    return res


# ------------------------------------------------------------------ RSSSF: tabela final das páginas por temporada
LINHA_A = re.compile(r"^\s*(\d+)\s*\.?\s*(\S.*?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*-\s*(\d+)\s+(-?\d+)\b(.*)$")   # J V E D GP-GC Pts
LINHA_B = re.compile(r"^\s*(\d+)\s*\.?\s*(\S.*?)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\b(.*)$")         # Pts J V E D GP GC


def tabela_rsssf(a: int, clubes_ano: set) -> list[dict] | None:
    """Primeiro bloco de linhas de tabela cujos clubes são os da temporada, em um dos dois formatos comuns da RSSSF.
    A linha só vale se J = V + E + D."""
    arq = DADOS / "rsssf" / rsssf_url(a).rsplit("/", 1)[1]
    if not arq.exists():
        return None
    linhas = texto_rsssf(arq.name).split("\n")
    for regex, ordem in ((LINHA_A, "jvedgp"), (LINHA_B, "pjvedgg")):
        bloco: list[dict] = []
        for l in linhas + [""]:
            m = regex.match(l)
            x = None
            if m:
                g = [int(v) for v in m.groups()[2:9]]
                if ordem == "jvedgp":
                    j, v, e, d, gp, gc, p = g
                else:
                    p, j, v, e, d, gp, gc = g
                if j == v + e + d and j > 0:
                    x = {"posicao": int(m.group(1)), "nome": re.sub(r"\s*\(\d\)\s*$", "", m.group(2)).strip(), "jogos": j,
                         "vitorias": v, "empates": e, "derrotas": d, "gols_pro": gp, "gols_contra": gc, "pontos": p}
            if x:
                bloco.append(x)
                continue
            if bloco and re.match(r"^\s*([-\s]{5,})?$", l) and len(bloco) < len(clubes_ano):
                continue   # linha de separação dentro da tabela ("-----" ou "- - - -")
            if bloco:
                for b in bloco:
                    b["clube"] = clubes.esd(b["nome"], a) or clubes.esd(re.sub(r"\s*\(.*?\)", "", b["nome"]), a)
                if len(bloco) == len(clubes_ano) and {b["clube"] for b in bloco} == clubes_ano:
                    return bloco
                bloco = []
    return None


# ------------------------------------------------------------------ tabela
def calcular(jogos: list[dict], pv: int) -> dict[str, list[int]]:
    t = defaultdict(lambda: [0, 0, 0, 0, 0, 0, 0])   # J V E D GP GC Pts
    for j in jogos:
        for lado, c, gp, gc in (("m", j["m"], j["gm"], j["gv"]), ("v", j["v"], j["gv"], j["gm"])):
            x = t[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            if j.get("vencedor"):   # resultado dado fora de campo com o placar mantido; "nenhum": derrota para os dois
                if j["vencedor"] == lado:
                    x[1] += 1; x[6] += pv
                else:
                    x[3] += 1
            elif gp > gc:
                x[1] += 1; x[6] += pv
            elif gp == gc:
                x[2] += 1; x[6] += 1
            else:
                x[3] += 1
    return t


def ordenar(t: dict[str, list[int]], ajuste: dict[str, int], criterio: str, jogos: list[dict] | None = None, pv: int = 2) -> list[str]:
    """criterio: "media" (pontos, média de gols), "saldo" (pontos, saldo, gols pró) ou "confronto" (pontos; entre os
    empatados, pontos e saldo nos jogos entre eles; depois saldo e gols pró)."""
    def pts(c):
        return t[c][6] + ajuste.get(c, 0)

    def geral(c):
        j, v, e, d, gp, gc, p = t[c]
        if criterio == "media":
            return (-(gp / gc if gc else float("inf")), -gp)
        return (-(gp - gc), -gp)
    if criterio in ("confronto_fora", "confronto_geral"):
        # pontos nos jogos entre os empatados, aplicado de novo entre os que seguem empatados; depois, em "confronto_fora",
        # saldo e gols fora de casa nesses jogos; por fim saldo e gols pró no campeonato
        def rank(g: list[str]) -> list[str]:
            if len(g) == 1 or jogos is None:
                return sorted(g, key=geral)
            jg = [j for j in jogos if j["m"] in g and j["v"] in g]
            mini = calcular(jg, pv)
            fora = Counter()
            for j in jg:
                fora[j["v"]] += j["gv"]
            sub = defaultdict(list)
            for c in g:
                sub[mini[c][6]].append(c)
            res_ = []
            for p in sorted(sub, reverse=True):
                s = sub[p]
                if len(s) < len(g):
                    res_ += rank(s)
                elif criterio == "confronto_fora":
                    res_ += sorted(s, key=lambda c: (-(mini[c][4] - mini[c][5]), -fora[c], *geral(c)))
                else:
                    res_ += sorted(s, key=geral)
            return res_
        por_pts = defaultdict(list)
        for c in t:
            por_pts[pts(c)].append(c)
        return [c for p in sorted(por_pts, reverse=True) for c in rank(por_pts[p])]
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


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    base = carregar_base()
    fd = carregar_fd()
    esd = carregar_esd()
    espn = carregar_espn()
    wiki = carregar_wiki()
    camp_rs = campeoes_rsssf()
    for x in ler_csv(CORRECOES_DIR / "datas.csv"):
        DATAS.setdefault(x["temporada"], []).append(x)
    pendentes = set()
    mapa_espn = votar(base, espn, "mandante_id", "visitante_id")
    prox_2026 = {clubes.ogol(o[k]) for o in json.loads((DADOS / "ogol" / f"por1_{TEMPORADAS[-1] + 1}.json").read_text(encoding="utf-8"))
                 for k in ("mandante_id", "visitante_id")}

    nomes = defaultdict(lambda: defaultdict(set))   # chave -> "fonte:nome" -> anos
    ocorr = defaultdict(list)
    tab = defaultdict(list)
    linhas_rel = []
    criterios = {}

    for a in TEMPORADAS:
        T = temporada(a)
        ocorr[a].extend(EXPLICACOES.get(a, []))
        jogos = base[a]
        clubes_ano = sorted({j["m"] for j in jogos} | {j["v"] for j in jogos})
        n = len(clubes_ano)
        pares = Counter((j["m"], j["v"]) for j in jogos)
        assert all(k == 1 for k in pares.values()), (a, [p for p, k in pares.items() if k > 1])
        if len(jogos) != n * (n - 1):
            ocorr[a].append(f"temporada com {len(jogos)} jogos de {n * (n - 1)}")
        por_par = {(j["m"], j["v"]): j for j in jogos}
        pv = 3 if a >= 1995 else 2
        for j in jogos:
            nomes[j["m"]][f"{j['fonte']}:{j['nm']}"].add(a)
            nomes[j["v"]][f"{j['fonte']}:{j['nv']}"].add(a)
            if j.get("acrescimo"):
                ocorr[a].append(f"jogo acrescentado: {j['m']} {j['gm']}-{j['gv']} {j['v']} ({j['data']}) — {j['acrescimo']}")
            k = (a, j["m"], j["v"])
            if k in CORRECOES:
                gm, gv, motivo = CORRECOES[k]
                ocorr[a].append(f"placar corrigido: {j['m']} x {j['v']} de {j['gm']}-{j['gv']} para {gm}-{gv} — {motivo}")
                j["gm"], j["gv"] = gm, gv
            if k in TRIBUNAL:
                gm, gv, venc, campo, motivo = TRIBUNAL[k]
                orig = j["ogol"]["resultado"] if j.get("ogol") else f"{j['gm']}-{j['gv']}"
                gm, gv = (j["gm"], j["gv"]) if gm is None else (gm, gv)
                ocorr[a].append(f"resultado decidido fora de campo: {j['m']} x {j['v']} fica {gm}-{gv}"
                                f"{' com vitória do ' + j[venc] if venc in ('m', 'v') else ' com derrota para os dois' if venc == 'nenhum' else ''}"
                                f" (ogol {orig}) — {motivo}")
                j.update(gm=gm, gv=gv, especial="awd", campo=campo, vencedor=venc)
            if k in CAMPO:
                gm, gv, motivo = CAMPO[k]
                ocorr[a].append(f"jogo sem placar no ogol ({j['ogol']['resultado']}): {j['m']} x {j['v']} fica {gm}-{gv} — {motivo}")
                j.update(gm=gm, gv=gv, campo_valeu=True)
            if j["gm"] is None:
                raise SystemExit(f"{T}: jogo sem placar no ogol ({j['ogol']['resultado']}) e fora de TRIBUNAL: {j['m']} x {j['v']} "
                                 f"({j['data']}, {j['ogol']['url']})")

        n_datas = 0
        for x in DATAS.get(T, []):
            m_, v_ = clubes.esd(x["mandante"], a), clubes.esd(x["visitante"], a)
            j = next((j for j in jogos if (j["m"], j["v"], j["data"]) == (m_, v_, x["data_errada"])), None)
            if j is None:
                raise SystemExit(f"{T}: jogo da correção de data não encontrado: {x}")
            j["data"], j["data_errada"] = x["data_certa"], x["data_errada"]
            n_datas += 1
        if n_datas:
            ocorr[a].append(f"{n_datas} datas corrigidas: o football-data e o transfermarkt concordam contra o ogol (lista em "
                            f"data/coleta/por-1/correcoes/datas.csv)")

        # ---- RSSSF: matriz de resultados (até 2004/05)
        rs_hist = ler_hist(DADOS / "rsssf" / rsssf_url(a).rsplit("/", 1)[1]) if a <= 2004 else None
        dif_mz = []
        if rs_hist:
            for aviso in rs_hist["avisos"]:
                ocorr[a].append(f"matriz da RSSSF: {aviso}")
            for (nm, nv), (g1, g2) in rs_hist["matriz"].items():
                m, v = clubes.esd(nm, a), clubes.esd(nv, a)
                nomes[m][f"rsssf:{nm}"].add(a)
                b = por_par.get((m, v))
                if b is None:
                    ocorr[a].append(f"matriz da RSSSF com jogo sem par no ogol: {nm} x {nv}")
                elif (g1, g2) != (b["gm"], b["gv"]):
                    dif_mz.append((b, (g1, g2)))
            # par em que a RSSSF troca os placares dos dois jogos (mando trocado): fica o do ogol, só anotado
            for b, (g1, g2) in dif_mz:
                volta = por_par.get((b["v"], b["m"]))
                troca = volta is not None and rs_hist["matriz"].get(next(((x, y) for (x, y) in rs_hist["matriz"]
                                                                          if clubes.esd(x, a) == b["v"] and clubes.esd(y, a) == b["m"]), None)) == (b["gv"], b["gm"]) \
                    and (volta["gm"], volta["gv"]) == (g2, g1)
                ocorr[a].append(f"placar diferente na matriz da RSSSF — {b['m']} x {b['v']} ({b['data']}): ogol {b['gm']}-{b['gv']}, "
                                f"RSSSF {g1}-{g2}{' (a RSSSF troca o mando dos dois jogos do par)' if troca else ''}")
            if len(rs_hist["matriz"]) != len(jogos):
                ocorr[a].append(f"matriz da RSSSF com {len(rs_hist['matriz'])} placares (ogol {len(jogos)} jogos)")

        # ---- engsoccerdata e football-data
        for fonte, dados, cm, cv in (("engsoccerdata", esd, "hgoal", "vgoal"), ("football-data", fd, "FTHG", "FTAG")):
            if a not in dados:
                continue
            for (m, v), x in dados[a].items():
                nomes[m][f"{fonte}:{x['home' if fonte == 'engsoccerdata' else 'HomeTeam']}"].add(a)
                b = por_par.get((m, v))
                if b is None:
                    ocorr[a].append(f"jogo do {fonte} sem par no ogol: {m} x {v}")
                    continue
                if fonte == "football-data":
                    b["fd"] = x
                if (int(x[cm]), int(x[cv])) != (b["gm"], b["gv"]) and not b.get("especial"):
                    ocorr[a].append(f"placar diferente no {fonte} — {m} x {v} ({b['data']}): ogol {b['gm']}-{b['gv']}, "
                                    f"{fonte} {x[cm]}-{x[cv]}")
            if len(dados[a]) != len(jogos):
                ocorr[a].append(f"{fonte} com {len(dados[a])} jogos (ogol {len(jogos)})")

        # ---- ESPN (entre eventos do mesmo par fica o de placar igual e com os gols fechando)
        es_ok = 0
        cand = defaultdict(list)
        for e in espn.get(a, []):
            m, v = mapa_espn.get(e["mandante_id"], a), mapa_espn.get(e["visitante_id"], a)
            if (m, v) not in por_par:
                ocorr[a].append(f"jogo da ESPN sem par no ogol: {e['mandante']} {e['gm']}-{e['gv']} {e['visitante']} ({e['data']})")
                continue
            cand[(m, v)].append(e)
        descartados = 0
        for (m, v), es in cand.items():
            b = por_par[(m, v)]
            iguais = [e for e in es if (e["gm"], e["gv"]) == (b["gm"], b["gv"])]

            def fecha(e):
                g = [l for l in e["lances"] if l["gol"]]
                return all(l["lado"] in ("home", "away") for l in g) and \
                    (sum(l["lado"] == "home" for l in g), sum(l["lado"] == "away" for l in g)) == (b["gm"], b["gv"])
            e = sorted(iguais or es, key=lambda e: (not fecha(e), int(e["id"])))[0]
            descartados += len(es) - 1
            nomes[m][f"espn:{e['mandante']}"].add(a)
            b["espn"] = e
            es_ok += 1
            if not iguais and not b.get("especial"):
                ocorr[a].append(f"placar diferente na ESPN — {m} x {v} ({b['data']}): ogol {b['gm']}-{b['gv']}, ESPN {e['gm']}-{e['gv']}")
        if descartados:
            ocorr[a].append(f"{descartados} eventos repetidos da ESPN descartados (fica o evento com o placar do ogol)")
        if a in espn and es_ok != len(jogos):
            falta = [j for j in jogos if "espn" not in j]
            ocorr[a].append(f"ESPN com {es_ok} de {len(jogos)} jogos (ex. sem ESPN: {falta[0]['m']} x {falta[0]['v']}, {falta[0]['data']})")

        # ---- tabelas publicadas e conferência
        ref = calcular(jogos, pv)
        clubes_tab = sorted(ref)
        ajuste: dict[str, int] = {}
        w = max(wiki.get(a, []), key=lambda tb: len({clubes.esd(x["nome"], a) for x in tb["times"]} & set(clubes_tab)), default=None)
        if w:
            for x in w["times"]:
                c = clubes.esd(x["nome"], a)
                if c is None:
                    raise SystemExit(f"{T}: nome da Wikipédia sem cadastro: {x['nome']}")
                x["clube"] = c
                nomes[c][f"wikipedia:{x['nome']}"].add(a)
                if x["ajuste"]:
                    ajuste[c] = x["ajuste"]
            if w["pontos_vitoria"] != pv:
                ocorr[a].append(f"Wikipédia com {w['pontos_vitoria']} pontos por vitória (aqui {pv})")
        if rs_hist:
            rs, url_rs = None, rsssf_url(a)
            tb = rs_hist["tabela"]
            for x in tb:
                x["clube"] = clubes.esd(x["nome"], a)
            if len(tb) == len(clubes_tab) and {x["clube"] for x in tb} == set(clubes_tab):
                rs = tb
            elif tb:
                ocorr[a].append(f"tabela da RSSSF com outros clubes: {sorted({x['clube'] for x in tb} ^ set(clubes_tab), key=str)}")
        else:
            rs, url_rs = tabela_rsssf(a, set(clubes_tab)), rsssf_url(a)
        if rs:
            for x in rs:   # punição que só a RSSSF traz (ponto a mais é erro de digitação: fica só anotado)
                c = ref.get(x["clube"])
                if c and [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"]] == c[:6] \
                        and x["pontos"] < c[6] and x["clube"] not in ajuste:
                    ajuste[x["clube"]] = x["pontos"] - c[6]
                    ocorr[a].append(f"punição tirada da tabela da RSSSF: {x['clube']} {x['pontos'] - c[6]:+d} pontos")
        for (ano, c), (v_aj, motivo) in AJUSTES.items():
            if ano == a:
                ocorr[a].append(f"ajuste de pontos de {c}: {v_aj:+d} (tabela publicada {ajuste.get(c, 0):+d}) — {motivo}")
                ajuste[c] = v_aj
        conferidas, divergentes, confere = 0, 0, {}
        publicadas = []
        if rs:
            publicadas.append(("RSSSF", url_rs, rs))
        if w:
            publicadas.append(("Wikipédia", f"https://en.wikipedia.org/wiki/{wiki_titulo(a).replace(' ', '_')}",
                               [dict(x, jogos=sum(x[k] or 0 for k in ("vitorias", "empates", "derrotas")),
                                     pontos=pv * (x["vitorias"] or 0) + (x["empates"] or 0) + x["ajuste"]) for x in w["times"]]))
        if not publicadas:
            ocorr[a].append("sem tabela publicada legível (RSSSF e Wikipédia)")
        for fonte, url, linhas in publicadas:
            erro = []
            if sorted(x["clube"] for x in linhas) != clubes_tab:
                erro.append(f"clubes diferentes: {sorted(set(x['clube'] for x in linhas) ^ set(clubes_tab), key=str)}")
            for x in linhas:
                c = ref.get(x["clube"])
                if c is None:
                    continue
                pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]
                meu = c[:6] + [c[6] + ajuste.get(x["clube"], 0)]
                if pub != meu:
                    erro.append(f"{x['clube']} tabela {pub} jogos {meu}")
                tab["tabelas_publicadas"].append({
                    "temporada": T, "fase": "Liga", "grupo": None, "posicao": x["posicao"], "nome_fonte": x["nome"],
                    "clube": clubes.exibicao(x["clube"]), "jogos": x["jogos"], "vitorias": x["vitorias"],
                    "empates": x["empates"], "derrotas": x["derrotas"], "gols_pro": x["gols_pro"], "gols_contra": x["gols_contra"],
                    "pontos": x["pontos"], "fonte": url})
            confere[fonte] = not erro
            if erro:
                divergentes += 1
                for e in erro:
                    ocorr[a].append(f"tabela publicada x jogos ({fonte}) — {e}")
            else:
                conferidas += 1

        if dif_mz and not divergentes:
            ocorr[a].append(f"as tabelas publicadas (RSSSF e Wikipédia) fecham com o ogol: nos {len(dif_mz)} jogos em que a matriz da "
                            f"RSSSF difere, fica o ogol")

        # ordem oficial: Wikipédia; se ela não fecha e a RSSSF fecha, a da RSSSF; sem nenhuma, calculada
        if a in ORDEM_RSSSF and rs:
            ordem = [x["clube"] for x in rs]
            fonte_ordem = "RSSSF (ordem oficial)"
            ocorr[a].append(f"fica a ordem da RSSSF: {ORDEM_RSSSF[a]}")
        elif w and (confere.get("Wikipédia") or not confere.get("RSSSF")):
            ordem = [x["clube"] for x in w["times"]]
            fonte_ordem = "Wikipédia (ordem oficial)"
        elif rs:
            ordem = [x["clube"] for x in rs]
            fonte_ordem = "RSSSF (ordem oficial)"
            if w:
                ocorr[a].append("a tabela da Wikipédia não fecha com os jogos e a da RSSSF fecha: fica a ordem da RSSSF")
        else:
            ordem = ordenar(ref, ajuste, "saldo", jogos, pv)
            fonte_ordem = "calculada"
        if a in ORDEM_FIXA:
            fixos = ORDEM_FIXA[a]
            resto = [c for c in ordem if c not in fixos.values()]
            ordem = [fixos.get(p_) or resto.pop(0) for p_ in range(1, len(ordem) + 1)]
            fonte_ordem = "Wikipédia pt (ordem oficial, com a decisão do tribunal)"
            ocorr[a].append("ordem da Wikipédia pt nas posições " + ", ".join(f"{p_}º {c}" for p_, c in sorted(fixos.items()))
                            + ": a derrota dada a Braga e Benfica muda os pontos do Braga")
        if rs and w and fonte_ordem.startswith("Wikipédia") and [x["clube"] for x in rs] != ordem:
            dif = [(r["clube"], c) for r, c in zip(rs, ordem) if r["clube"] != c]
            ocorr[a].append(f"ordem diferente entre RSSSF e Wikipédia em {len(dif)} posições (ex.: RSSSF {dif[0][0]}, Wikipédia "
                            f"{dif[0][1]}); fica a da Wikipédia")
        tentativas = {cr: ordenar(ref, ajuste, cr, jogos, pv) for cr in ("confronto", "confronto_geral", "confronto_fora", "saldo", "media")}
        ok = [cr for cr, o in tentativas.items() if o == ordem]
        # a tabela que não fecha pode errar só nos gols de um clube e trazer a ordem certa: se a ordem escolhida não sai de
        # nenhum critério e a da outra tabela sai, fica a outra
        outra = ([x["clube"] for x in w["times"]], "Wikipédia (ordem oficial)") if fonte_ordem.startswith("RSSSF") and w else \
            ([x["clube"] for x in rs], "RSSSF (ordem oficial)") if fonte_ordem.startswith("Wikipédia") and rs else None
        if not ok and outra and not (fonte_ordem.startswith("Wikipédia") and confere.get("Wikipédia")) and any(o == outra[0] for o in tentativas.values()):
            ocorr[a].append(f"a ordem da {fonte_ordem.split(' ')[0]} não sai de nenhum critério de desempate e a da "
                            f"{outra[1].split(' ')[0]} sai: fica a da {outra[1].split(' ')[0]}")
            ordem, fonte_ordem = outra
            ok = [cr for cr, o in tentativas.items() if o == ordem]
        criterio = ok[0] if ok else min(tentativas, key=lambda cr: sum(x != y for x, y in zip(tentativas[cr], ordem)))
        if not ok:
            dif = [c for c, d in zip(ordem, tentativas[criterio]) if c != d]
            ocorr[a].append(f"nenhum critério calculado reproduz a ordem oficial; o mais próximo ({criterio}) difere em "
                            f"{len(dif)} posições (ex.: {dif[:2]})")
        criterios[a] = (criterio, bool(ok))

        # rebaixados: quem não está na 1ª divisão no ano seguinte (até 1944/45 não havia rebaixamento)
        prox_clubes = {j[k] for j in base[a + 1] for k in ("m", "v")} if a + 1 in base else prox_2026
        if a in SEM_REBAIXAMENTO:
            rebaixados = set()
        else:
            rebaixados = {c for c in clubes_ano if c not in prox_clubes and (a, c) not in NAO_REBAIXADOS}
        for (b_, c), motivo in NAO_REBAIXADOS.items():
            if b_ == a:
                ocorr[a].append(f"{c} não está na temporada seguinte, mas não foi rebaixado: {motivo}")
        if w:
            textos = {k[5:]: limpar(v).lower() for k, v in w["params"].items() if k.startswith("text_")}
            marca = {x["clube"] for x in w["times"] if "relegat" in textos.get(x["resultado"], "")
                     and not re.search(r"play|spared", textos.get(x["resultado"], ""))}
            playoff = {x["clube"] for x in w["times"] if "play" in textos.get(x["resultado"], "")
                       and "releg" in textos.get(x["resultado"], "")}
            for c in sorted(playoff & rebaixados):
                ocorr[a].append(f"{c} perdeu o play-off de manutenção (contra um clube da 2ª divisão) e foi rebaixado")
            dif = (rebaixados ^ marca) - playoff
            if a not in SEM_REBAIXAMENTO and dif and (marca or a != TEMPORADAS[-1]):
                ocorr[a].append(f"rebaixados: pela temporada seguinte {sorted(rebaixados)}; marca da Wikipédia {sorted(marca)}")
        campeao, vice = ordem[0], ordem[1]
        if camp_rs.get(a) and camp_rs[a] != campeao:
            ocorr[a].append(f"campeão diferente na lista de campeões da RSSSF: {camp_rs[a]} (tabela: {campeao})")
        pos_reb = {p for p, c in enumerate(ordem, 1) if c in rebaixados}
        for pos, c in enumerate(ordem, 1):
            j_, v_, e_, d_, gp, gc, p = ref[c]
            tab["classificacao_final"].append({
                "temporada": T, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
                "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": p + ajuste.get(c, 0), "ajuste_pontos": ajuste.get(c, 0),
                "situacao": "campeao" if pos == 1 else "rebaixado" if c in rebaixados else None,
                "fonte": fonte_ordem,
                "observacao": OBS_CLASSIF.get((a, c)) or (AJUSTES[(a, c)][1] if (a, c) in AJUSTES else None) or
                ((w and next((notas_wiki.traduzir(x["nota"] or x["hth"]) for x in w["times"] if x["clube"] == c), None)) or None)})

        # ---- partidas, gols, cartões, estatísticas
        rs_gols = gols_rsssf(a, jogos) if 1999 <= a <= 2005 else {}
        jogos.sort(key=lambda j: (j["data"] or "9999", j["rodada"] or 0, j["m"]))
        gols_ano = autor_ano = 0
        for i, j in enumerate(jogos, 1):
            pid = f"{a}-{i:04d}"
            o, e, x = j.get("ogol"), j.get("espn"), j.get("fd")
            fuso = ACORES if j["m"] == "Santa Clara" else LISBOA
            hora = None
            if x and x.get("Time"):   # o football-data dá a hora do Reino Unido
                d = datetime.fromisoformat(f"{data_fd(x['Date'])}T{x['Time']}").replace(tzinfo=LONDRES).astimezone(fuso)
                hora = d.strftime("%H:%M")
            elif e:
                local = e["utc"].astimezone(fuso)
                if local.date().isoformat() == j["data"]:
                    hora = local.strftime("%H:%M")
            ids = [f"ogol:{o['id']}"] if o else []
            if e:
                ids.append(f"espn:{e['id']}")
            fontes = [j["fonte"]] + (["football-data"] if x and j["fonte"] != "football-data" else []) + (["ESPN"] if e else [])
            obs = None
            if j.get("especial"):
                obs = (f"vitória do {j[j['vencedor']]} dada fora de campo; o placar registrado ({j['campo']}) fica"
                       if j.get("vencedor") in ("m", "v") else
                       f"derrota para os dois clubes dada fora de campo; em campo, {j['campo']}" if j.get("vencedor") == "nenhum" else
                       f"resultado dado fora de campo; em campo, {j['campo']}" if j.get("campo") else "resultado dado fora de campo")
            elif j.get("campo_valeu"):
                obs = "jogo interrompido aos 86 minutos por invasão de campo; as tabelas publicadas contam o 1-1 de campo"
            tab["partidas"].append({
                "id": pid, "temporada": T, "fase": j["fase"], "grupo": j["grupo"], "rodada": j["rodada"], "data": j["data"],
                "hora": hora, "mandante": clubes.exibicao(j["m"]), "visitante": clubes.exibicao(j["v"]),
                "gols_mandante": j["gm"], "gols_visitante": j["gv"], "penaltis_mandante": None, "penaltis_visitante": None,
                "resultado_especial": "awd" if j.get("especial") else None,
                "estadio": (e or {}).get("estadio"), "cidade": (e or {}).get("cidade"),
                "publico": (e or {}).get("publico") or None, "fonte": " + ".join(fontes), "fonte_id": "|".join(ids),
                "gols_texto": None, "observacao": obs, "arbitro": (x or {}).get("Referee") or None})
            gols_ano += j["gm"] + j["gv"]
            com_autor = False
            if e and e["lances"] and not j.get("especial"):
                gl = [l for l in e["lances"] if l["gol"]]
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
                    com_autor = bool(gl)
                elif gl:
                    ocorr[a].append(f"gols da ESPN não batem com o placar — {j['m']} {j['gm']}-{j['gv']} {j['v']}: "
                                    f"ESPN {sum(l['lado'] == 'home' for l in gl)}-{sum(l['lado'] == 'away' for l in gl)}"
                                    f"{' e gol sem clube' if not all(l['lado'] in lado for l in gl) else ''} (descartados)")
                for l in e["lances"]:
                    if (l["amarelo"] or l["vermelho"]) and l["lado"] in lado:
                        mi, ac = minuto(l["minuto"])
                        tab["cartoes"].append({"partida_id": pid, "clube": clubes.exibicao(lado[l["lado"]]),
                                               "jogador": (l["jogadores"] or [None])[0], "minuto": mi, "acrescimo": ac,
                                               "cor": "vermelho" if l["vermelho"] else "amarelo", "fonte": "ESPN"})
            if not com_autor and j["gm"] + j["gv"] > 0 and not j.get("especial") and a >= 1999:
                # sem os gols da ESPN: a RSSSF (1999/00-2005/06, revisão PT-019) ou a ficha do ogol
                lista, fonte_g = None, None
                r_ = rs_gols.get((j["m"], j["v"]))
                if r_ and (r_[0], r_[1]) == (j["gm"], j["gv"]):
                    lista, fonte_g = [(l_, n_, mi_, None, t_) for l_, n_, mi_, t_ in r_[2]], "RSSSF"
                elif o:
                    arq_f = FICHAS / f"{o['id']}.html"
                    if arq_f.exists():
                        g_ = ogol_ficha.gols(arq_f.read_text(encoding="utf-8", errors="replace"))
                        if (sum(l_[0] == "m" for l_ in g_), sum(l_[0] == "v" for l_ in g_)) == (j["gm"], j["gv"]):
                            lista, fonte_g = g_, f"ogol (ficha {o['id']})"
                    else:
                        pendentes.add(o["id"])
                if lista:
                    for l_, n_, mi_, ac_, t_ in lista:
                        tab["gols"].append({"partida_id": pid, "clube": clubes.exibicao(j[l_]), "jogador": n_, "minuto": mi_,
                                            "acrescimo": ac_, "tipo": t_, "fonte": fonte_g})
                    autor_ano += len(lista)
            if x and x.get("HS"):
                def num(k):
                    v_ = x.get(k)
                    return int(float(v_)) if v_ not in (None, "") else None
                for c, s in ((j["m"], "H"), (j["v"], "A")):
                    tab["estatisticas"].append({"partida_id": pid, "clube": clubes.exibicao(c), "chutes": num(f"{s}S"),
                                                "chutes_alvo": num(f"{s}ST"), "faltas": num(f"{s}F"), "escanteios": num(f"{s}C"),
                                                "amarelos": num(f"{s}Y"), "vermelhos": num(f"{s}R"), "fonte": "football-data.co.uk"})

        # ---- classificação rodada a rodada
        sem_rodada = [j for j in jogos if not j["rodada"]]
        if sem_rodada:
            ocorr[a].append(f"{len(sem_rodada)} jogos sem rodada no ogol (ex.: {sem_rodada[0]['m']} x {sem_rodada[0]['v']})")
        else:
            for r in sorted({j["rodada"] for j in jogos}):
                ate = [j for j in jogos if j["rodada"] <= r]
                parcial = calcular(ate, pv)
                for pos, c in enumerate(ordenar(parcial, ajuste, criterio, ate, pv), 1):
                    jj, v_, e_, d_, gp, gc, p = parcial[c]
                    tab["classificacao_rodada"].append({
                        "temporada": T, "rodada": r, "clube": clubes.exibicao(c), "posicao": pos, "pontos": p + ajuste.get(c, 0),
                        "jogos": jj, "vitorias": v_, "empates": e_, "derrotas": d_, "gols_pro": gp, "gols_contra": gc,
                        "zona": "titulo" if pos == 1 else "rebaixamento" if pos in pos_reb else "meio"})

        fontes_ed = ["ogol"] + (["engsoccerdata"] if a in esd else []) + (["football-data"] if a in fd else []) \
            + (["ESPN"] if a in espn else []) + (["RSSSF"] if rs else []) + (["Wikipédia"] if w else [])
        pun = "; ".join(f"{c} {v:+d} pontos" for c, v in ajuste.items())
        tab["edicoes"].append({"temporada": T, "ano_inicio": a, "ano_fim": a + 1, "nome_oficial": nome_oficial(a), "num_clubes": n,
                               "pontos_vitoria": pv, "formato": "pontos corridos (turno e returno)",
                               "campeao": clubes.exibicao(campeao), "vice": clubes.exibicao(vice),
                               "fontes": " + ".join(fontes_ed),
                               "observacao": "; ".join(x for x in (
                                   "Campeonato da Liga, experimental (o campeão nacional ainda era o do Campeonato de Portugal); o "
                                   "título conta hoje entre os da 1ª divisão" if a < 1938 else "",
                                   "participantes classificados pelos campeonatos regionais, sem rebaixamento" if a in SEM_REBAIXAMENTO else "",
                                   f"punições: {pun}" if pun else "") if x) or None})
        crit_txt = {"confronto": "pontos, confronto direto, saldo de gols, gols pró",
                    "confronto_geral": "pontos, pontos no confronto direto (de novo entre os que seguem empatados), saldo de gols, gols pró",
                    "confronto_fora": "pontos, pontos no confronto direto (de novo entre os que seguem empatados), saldo e gols fora de "
                                      "casa no confronto direto, saldo de gols, gols pró",
                    "saldo": "pontos, saldo de gols, gols pró",
                    "media": "pontos, média de gols (goal average)"}[criterio]
        tab["fases"].append({"temporada": T, "ordem": 1, "fase": "Liga", "tipo": "liga", "num_grupos": None,
                             "formato_serie": "pontos_corridos", "criterio": crit_txt})
        obs = [f"campeão {clubes.exibicao(campeao)} (RSSSF, lista de campeões: {camp_rs.get(a) or '—'})"]
        if divergentes:
            obs.append("divergências explicadas no relatório")
        tab["conferencia"].append({"temporada": T, "jogos": len(jogos), "jogos_esperados": n * (n - 1),
                                   "tabelas_conferidas": conferidas, "tabelas_divergentes": divergentes, "gols": gols_ano,
                                   "gols_com_autor": autor_ano, "observacao": "; ".join(obs)})
        linhas_rel.append((T, " + ".join(fontes_ed), n, len(jogos), gols_ano, autor_ano, conferidas, divergentes,
                           clubes.exibicao(campeao), pun))
        print(f"{T}: {len(jogos)} jogos, tabelas {conferidas} ok / {divergentes} div, gols {gols_ano} ({autor_ano} c/ autor), "
              f"critério {criterio}{'' if criterios[a][1] else ' (aprox.)'}, campeão {clubes.exibicao(campeao)}", flush=True)

    (DADOS / "fichas_pendentes.json").write_text(json.dumps(sorted(pendentes)), encoding="utf-8")
    if pendentes:
        print(f"{len(pendentes)} fichas do ogol a baixar: python coleta/por-1/baixar.py fichas", flush=True)

    # ---- clubes
    for c, (cidade, pais) in sorted(clubes.CLUBES.items()):
        if c not in nomes:
            continue
        nf = "|".join(f"{k}:{faixa(v)}" for k, v in sorted(nomes[c].items()))
        tab["clubes"].append({"clube": clubes.exibicao(c), "regiao": None, "cidade": cidade, "pais": pais, "nomes_fonte": nf})
    tab["paises"] = []
    tab["artilheiros"] = artilheiros(ocorr)
    gravar(PACOTE, COMPETICAO, tab)
    relatorio(linhas_rel, ocorr, tab, mapa_espn, criterios)


def gols_rsssf(a: int, jogos: list[dict]) -> dict[tuple, tuple]:
    """Autores dos gols pela página da RSSSF da temporada (tablesp/port00.html ... port06.html; revisão PT-019): os nomes da
    RSSSF ("Vitoria G") viram clubes por votação (mesma rodada e mesmo placar, quando só um jogo serve)."""
    arq = DADOS / "rsssf" / f"port{str(a + 1)[-2:]}.html"
    if not arq.exists():
        return {}
    rs = rsssf_gols.jogos(arq)
    votos = defaultdict(Counter)
    for r in rs:
        cand = [j for j in jogos if j.get("rodada") == r["rodada"] and (j["gm"], j["gv"]) == (r["gm"], r["gv"])]
        if len(cand) == 1:
            votos[r["nm"]][cand[0]["m"]] += 1
            votos[r["nv"]][cand[0]["v"]] += 1
    mapa = {k: c.most_common(1)[0][0] for k, c in votos.items()}
    return {(mapa[r["nm"]], mapa[r["nv"]]): (r["gm"], r["gv"], r["gols"]) for r in rs
            if r["nm"] in mapa and r["nv"] in mapa and r["gols"]}


def artilheiros(ocorr) -> list[dict]:
    """Artilheiro(s) de cada temporada pela lista da RSSSF (tablesp/porttops.html: "1934/35 Manuel Soeiro (Sporting CP) -
    14 goals / 14 rounds"; empate nas linhas seguintes, que começam com espaço)."""
    res, ano = [], None
    for l in texto_rsssf("porttops.html").split("\n"):
        m = re.match(r"^(\d{4})/\d{2}\s+(.*)$", l)
        if m:
            ano, resto = int(m.group(1)), m.group(2)
        elif ano is not None and re.match(r"^\s+\S", l) and "goals" in l:
            resto = l.strip()
        else:
            if not l.strip() or not l.startswith(" "):
                ano = None if l.strip() else ano
            continue
        x = re.match(r"^(.*?)\s*\(([^()]+)\)\s*[-\x96–]?\s*(\d+)\s*goals", resto.replace("\t", " "))
        if not x or ano not in TEMPORADAS:
            continue
        nome, clube_txt, gols = x.group(1).strip().rstrip("\x96–- ").strip(), x.group(2).strip(), int(x.group(3))   # PT-013
        c = clubes.esd(clube_txt, ano)
        fonte_a = "RSSSF (tablesp/porttops.html)"
        if (ano, nome) in GOLS_ARTILHEIRO:
            gols, motivo = GOLS_ARTILHEIRO[(ano, nome)]
            fonte_a += f"; {motivo}"
        res.append({"temporada": temporada(ano), "jogador": nome, "clube": clubes.exibicao(c) if c else None, "gols": gols,
                    "fonte": fonte_a})
        if c is None:
            ocorr[ano].append(f"artilheiro com clube sem cadastro: {nome} ({clube_txt})")
    faltam = sorted(set(TEMPORADAS) - {int(x["temporada"][:4]) for x in res})
    for a in faltam:
        ocorr[a].append("artilheiro: a lista da RSSSF não traz esta temporada")
    return res


def relatorio(linhas, ocorr, tab, mapa_espn, criterios) -> None:
    jogos = len(tab["partidas"])
    gols = sum(int(x["gols_mandante"]) + int(x["gols_visitante"]) for x in tab["partidas"])
    cr = Counter(c for c, _ in criterios.values())
    out = [
        "# Campeonato Português (1ª divisão) — coleta de dados", "",
        "Gerado por `python coleta/por-1/importar.py`. Pacote em `data/coleta/por-1/pacote/`.", "",
        f"**Edições:** {len(linhas)}, de 1934/35 a 2025/26: Campeonato da Liga (1934/35 a 1937/38, experimental; os títulos "
        "contam hoje entre os da 1ª divisão), Primeira Divisão (1938/39 a 1998/99) e Primeira Liga.", "",
        f"**Total:** {jogos} jogos, {gols} gols, {len(tab['gols'])} gols com autor (ESPN), {len(tab['cartoes'])} cartões, "
        f"{len(tab['clubes'])} clubes.", "",
        "**Fontes:**",
        "- ogol (zerozero): base dos jogos de todas as temporadas, com a rodada oficial; ficha dos jogos decididos fora de campo; "
        "calendários guardados em `data/cache/ogol-por-1/` para os escudos;",
        "- RSSSF: tabela final e matriz de resultados de 1934/35 a 2004/05 (conferência jogo a jogo), tabela final das temporadas "
        "seguintes, lista de campeões e de artilheiros (com o clube);",
        "- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): conferência de placar de 1994/95 a 2024/25;",
        "- football-data.co.uk: de 1994/95 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;",
        "- ESPN (liga `por.1`): hora, estádio, público, gols e cartões com minuto e jogador, nas temporadas que ela cobre;",
        "- Wikipédia (en): tabela final de cada temporada (ordem oficial, punições e marca de rebaixamento).", "",
        "**Regras:** o placar é o do ogol; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols "
        "pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando "
        "a soma bate com o placar. Hora local (Lisboa; Açores nos jogos em casa do Santa Clara). Rebaixado = clube que não está na "
        "1ª divisão na temporada seguinte (até 1944/45 não havia rebaixamento: os participantes saíam dos campeonatos "
        "regionais). 2 pontos por vitória até 1994/95, 3 a partir de 1995/96. Placar diferente em outra fonte numa temporada "
        "em que as tabelas publicadas fecham com o ogol é erro da outra fonte e fica só anotado; quando a outra fonte e as "
        "tabelas publicadas concordam contra o ogol, o placar é corrigido (CORRECOES e TRIBUNAL em `importar.py`, com o motivo).", "",
        f"**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em "
        f"{cr['confronto']}, confronto direto aplicado de novo entre os que seguem empatados em {cr['confronto_geral']}, o "
        f"mesmo com saldo e gols fora de casa no confronto em {cr['confronto_fora']}, saldo de gols em {cr['saldo']}, média de "
        f"gols em {cr['media']}); é ele que ordena a classificação "
        "rodada a rodada.", "",
        "| Temporada | Fontes | Clubes | Jogos | Gols | Gols c/ autor | Tabelas ok / div. | Campeão | Punições |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for T, f, n, j, g, au, ok, dv, camp, pun in linhas:
        out.append(f"| {T} | {f} | {n} | {j} | {g} | {au} | {ok} / {dv} | {camp} | {pun or '—'} |")
    out += ["", "## Conferência e ocorrências, temporada a temporada", ""]
    for T, *_ in linhas:
        a = int(T[:4])
        out.append(f"### {T}")
        out.append("")
        for o in ocorr.get(a, []) or ["sem ocorrências"]:
            out.append(f"- {o}")
        out.append("")
    out += [
        "## Identidade dos clubes", "",
        "- Cadastro em `coleta/comum-europa/clubes_por.py` (serve para todas as divisões portuguesas): nome de exibição como o "
        "clube é conhecido no Brasil, cidade e país. Nomes únicos no mundo: \"Nacional da Madeira\", \"Oriental de Lisboa\", "
        "\"CD Feirense\", \"Caldas SC\" e \"AD Sanjoanense\" (há Nacional e Oriental no Uruguai, Feirense, Caldas e "
        "Sanjoanense no Brasil).",
        "- Clubes à parte: Belenenses (CF Os Belenenses, até 2017/18) e Belenenses SAD (2018/19 a 2021/22); AVS (2024/25 em "
        "diante) e Desportivo das Aves; SL Elvas e O Elvas. O Estrela da Amadora de hoje fica com a história do antigo, como no ogol.",
        f"- O ogol entra pelo código do clube (tabela `OGOL` do cadastro); a ESPN é casada por votação jogo a jogo (mesma data e "
        f"placar): {len(mapa_espn)} códigos.",
        "- Os nomes de cada fonte, com os anos, estão em `nomes_fonte` do `clubes.csv`.",
        "",
        "## O que não deu para coletar", "",
        "- **Autores dos gols e cartões antes da ESPN:** nenhuma fonte em lote traz.",
        "- **Público e estádio antes da ESPN:** nenhuma fonte em lote.",
        "- **Play-offs de manutenção (contra clubes da 2ª divisão):** ficam de fora (entram com a 2ª divisão).",
        "- **Campeonato de Portugal (1921/22 a 1937/38, em mata-mata):** é outra competição; fica de fora.",
        "- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.",
    ]
    RELATORIO.parent.mkdir(parents=True, exist_ok=True)
    RELATORIO.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
