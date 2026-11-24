"""Junta as fontes do Campeonato Paulista (1ª divisão) e grava o pacote em data/coleta/bra-sp-1/pacote/ e o relatório em
docs/coleta/bra-sp-1.md. Mesmo método da Série C (docs/coleta/bra-serie-c.md).

Fontes: RSSSF Brasil (tablessz/sp{ano}.htm: jogos, fases, grupos, datas e autores; as tabelas publicadas são a conferência);
ogol (calendário de cada edição e o código de cada clube, que dá a identidade; confere placares e completa jogos);
Wikipédia (lista de campeões, segunda fonte do campeão).

A edição é a temporada ("1950" ou, nos anos de duas ligas, "1913 LPF"); o ano sai de temporada[:4].

Uso: python coleta/bra-sp-1/importar.py [temporada ...]     (sem temporada: todas; com temporada, só confere e não grava)
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from difflib import SequenceMatcher
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
import clubes_sp1  # noqa: E402
import fpf_sp1  # noqa: E402
import gols as gols_rsssf  # noqa: E402
import rsssf_sp1  # noqa: E402
import wiki  # noqa: E402
from edicoes import ANOS, NOME_OFICIAL, NOME_PADRAO, PACOTE, PASTA_DADOS, RELATORIO, SLUG  # noqa: E402
from rsssf_sp1 import rsssf  # noqa: E402

wiki.PASTA = PASTA_DADOS / "wikipedia"
OGOL = PASTA_DADOS / "ogol"
ESPN = PASTA_DADOS / "espn"
FONTE_RSSSF = "https://rsssfbrasil.com/tablessz/sp{ano}.htm"


# --------------------------------------------------------------------------------------------- partidas

@dataclass
class Partida:
    ano: int
    fase: str                 # nome da fase como na fonte (normalizado depois por fase_pt)
    grupo: str
    rodada: int | None
    data: str | None
    mandante: str             # código do clube no ogol
    visitante: str
    gm: int | None
    gv: int | None
    hora: str | None = None
    pen_m: int | None = None
    pen_v: int | None = None
    especial: str = ""
    estadio: str | None = None
    cidade: str | None = None
    publico: int | None = None
    fonte: str = ""
    fonte_id: str = ""
    gols_texto: str = ""
    obs: str = ""
    gols: list[dict] = field(default_factory=list)
    linha: int = 0
    ogol_fase: str = ""
    ogol_placar: tuple | None = None   # placar do mesmo jogo no ogol (conferência)


def _dia(d: str | None) -> int | None:
    try:
        return datetime.strptime(d, "%Y-%m-%d").toordinal() if d else None
    except ValueError:   # "0000-00-00": jogo sem data no ogol
        return None


def _trocar_dia_mes(d: str | None) -> str | None:
    """'2015-01-06' -> '2015-06-01' (a página de 2015 trocou dia e mês quando o dia era até 12)."""
    if not d or not re.match(r"^\d{4}-\d{2}-\d{2}$", d) or int(d[8:]) > 12:
        return None
    return f"{d[:4]}-{d[8:]}-{d[5:7]}"


def _dist(a: str | None, b: str | None) -> int:
    """Dias entre duas datas; 0 quando uma delas falta (não desempata)."""
    x, y = _dia(a), _dia(b)
    return abs(x - y) if x and y else 0


def _sim(a: str, b: str) -> float:
    a, b = clubes_sp1.chave(a), clubes_sp1.chave(b)
    if not a or not b:
        return 0.0
    if a == b:
        return 1.0
    if a.startswith(b) or b.startswith(a):
        return 0.85
    if rsssf.abreviado(a, b) or rsssf.abreviado(a.replace(".", " "), b):   # "eng beltrao" x "engenheiro beltrao"
        return 0.85
    return SequenceMatcher(None, a, b).ratio()


# código de clube errado no calendário do ogol: (ano, código errado) -> (código certo, motivo)
CORRIGE_OGOL: dict[tuple[int, str], tuple[str, str]] = {}


def ler_ogol(ano: int) -> list[dict]:
    f = OGOL / f"sp1_{str(ano).replace(" ", "_")}.json"
    js = json.loads(f.read_text(encoding="utf-8")) if f.exists() else []
    for o in js:
        for lado in ("mandante", "visitante"):
            if (ano, o.get(f"{lado}_id")) in CORRIGE_OGOL:
                o[f"{lado}_id"] = CORRIGE_OGOL[(ano, o[f"{lado}_id"])][0]
    return [o for o in js if o["id"] not in OGOL_IGNORAR]


def nomes_ogol(ano: int, og: list[dict]) -> dict[str, set[str]]:
    """Código do clube -> nomes que o ogol usa para ele (no calendário do ano e na ficha)."""
    fs = clubes_sp1.fichas()
    saida: dict[str, set[str]] = defaultdict(set)
    for o in og:
        for lado in ("mandante", "visitante"):
            i = o.get(f"{lado}_id")
            if i:
                saida[i].add(o[lado])
                if i in fs:
                    saida[i] |= {fs[i]["curto"], fs[i].get("nome_completo") or ""}
    return saida


# nomes da RSSSF que o casamento automático não acerta (ano, nome) -> código do ogol, com o motivo
NOME_MANUAL: dict[tuple[str, str], tuple[str, str]] = {
    ("1927 APEA", "Corinthians de Santo André"): ("81207", "\"Corinthians (SBC)\" na página; o ogol tem os 13 jogos dele (SP-009)"),
}
# jogos do calendário do ogol que estão errados (a RSSSF e a tabela publicada mostram outro jogo): código do jogo -> motivo
OGOL_IGNORAR: dict[str, str] = {
    "2591655": "1928 LAF: Paulista 127-0 LAF não é jogo (linha de resumo do ogol, sem data e contra um clube \"LAF\" que não "
               "existe; o Futebol Nacional dá 133 jogos sem ele; achado SP-011)",
}
# jogos da RSSSF que ficam de fora: (ano, nome do clube) -> motivo
RSSSF_FORA: dict[tuple[int, str], str] = {
    (1988, "Ponte Preta"): "perdeu a vaga na 1ª divisão e todos os jogos dela foram cancelados (nota da página; FN \"Cancelado\"; "
                           "o ogol não os tem; achado SP-014)",
    (1988, "Bandeirante"): "perdeu a vaga na 1ª divisão e todos os jogos dele foram cancelados (nota da página; FN \"Cancelado\"; "
                           "o ogol não os tem; achado SP-014)",
}
# jogos da RSSSF anulados: (ano, mandante, visitante, gols, gols) como na página -> motivo
JOGOS_ANULADOS: dict[tuple, str] = {
    (1956, "Taubaté", "Corinthians", 2, 2): "21/11/1956: a tabela da própria página dá 18 jogos ao Taubaté e ao Corinthians, o "
                                            "que só fecha sem ele; o ogol e o FN só têm o 0-2 de 23/12 (achado QS-013)",
}

# Correções da revisão de 22/11 (docs/revisao/plano-coleta-brasil.md), aplicadas depois de juntar RSSSF e ogol, com os
# clubes pelo nome de exibição. Fonte: Futebol Nacional (FN), edição de cada ano:
FN = ("https://futebolnacional.com.br/siteapp/controller.jsp?module=summary&lang=pt-br&name=A27437D2CE0894275C03A3BAEDA49F41"
      "A9C63F1F39F7FF7572315985555EFA80&state=SP&country=BR")
# clube que abandonou ou saiu da liga: os jogos dele foram cancelados e não contam (achados QS-001 e SP-010)
CLUBES_FORA: dict[tuple[str, str], str] = {
    ("1913 LPF", "Santos"): "abandonou a competição; jogos cancelados (FN)",
    ("1914 LPF", "Germânia"): "retirou-se da competição; jogos cancelados (FN)",
    ("1914 LPF", "Hydecroft"): "retirou-se da competição; jogos cancelados (FN)",
    ("1923", "Paulistano-SP"): "abandonou a competição; jogos cancelados (FN)",
    ("1924", "Palmeiras"): "o Palestra Itália abandonou a competição; jogos cancelados (FN)",
    ("1925", "AA das Palmeiras"): "abandonou a competição; jogos cancelados (FN)",
    ("1928 APEA", "Comercial-RP"): "jogos cancelados (FN; a tabela da RSSSF não os conta)",
    ("1935 APEA", "Independente de Limeira"): "abandonou a competição; jogos cancelados (FN)",
    ("1938", "Estudantes de São Paulo"): "abandonou a competição e juntou-se ao São Paulo; jogo cancelado (FN)",
    ("1927 LAF", "Corinthians"): "deixou a LAF e foi para a APEA; jogos cancelados (FN; SP-010)",
    ("1927 LAF", "Independência-SP"): "deixou a LAF e foi para a APEA; jogos cancelados (FN; SP-010)",
    ("1927 LAF", "EC Sírio"): "deixou a LAF e foi para a APEA; jogos cancelados (FN; SP-010)",
    ("1927 LAF", "Sílex"): "deixou a LAF e foi para a APEA; jogos cancelados (FN; SP-010)",
    ("1927 LAF", "Taubaté"): "deixou a LAF e foi para a APEA; jogos cancelados (FN; SP-010)",
}
# jogo avulso cancelado: (temporada, data, mandante, visitante) -> motivo
JOGOS_FORA: dict[tuple[str, str, str, str], str] = {
    ("1906", "1906-08-05", "São Paulo Athletic", "SC Internacional-SP"):
        "o SPAC desistiu depois deste jogo e a LPF o cancelou, dando os pontos dos seguintes aos adversários (FN; QS-005)",
    ("1916 APEA", "1916-10-29", "Ypiranga-SP", "Mackenzie-SP"):
        "3º jogo do par, fora da tabela publicada (RSSSF e FN; QS-006)",
    ("1916 APEA", "1916-12-03", "AA das Palmeiras", "Palmeiras"):
        "3º jogo do par, fora da tabela publicada (RSSSF e FN; QS-006)",
    ("1928 APEA", "1928-07-29", "Palmeiras", "Portuguesa"):
        "3º jogo Palestra x Portuguesa na página; o ogol não o tem e, sem ele, as campanhas dos dois fecham com a tabela "
        "da RSSSF (8 vitórias e 45 gols pró do Palestra); vice: Santos (pódio da Wikipédia; SP-003)",
}
# pontos dados fora de campo: (temporada, data, mandante, visitante) -> (quem ganhou os pontos, motivo). O jogo conta
# como vitória sem gols (decisão D-15); o placar de campo vai na observação (achados QS-015 e SP-013)
PONTOS_FORA_DE_CAMPO: dict[tuple[str, str, str, str], tuple[str, str]] = {
    ("1915 APEA", "1915-06-06", "AA São Bento", "Scottish Wanderers"): ("AA São Bento", "FN"),
    ("1919", "1919-11-30", "Minas Gerais FC", "Santos"): ("Minas Gerais FC", "FN"),
    ("1921", "1921-10-09", "Ypiranga-SP", "Paulistano-SP"): ("Ypiranga-SP", "FN"),
    ("1925", "1925-06-07", "Palmeiras", "Germânia"): ("Germânia", "FN"),
    ("1930", "1930-04-27", "EC Sírio", "Ypiranga-SP"): ("Ypiranga-SP", "FN"),
    ("1930", "1930-05-04", "Palmeiras", "Corinthians"):
        ("Corinthians", "os jogadores do Palestra saíram de campo depois da anulação de um gol (FN; SP-013)"),
    ("1935 APEA", "1935-08-04", "Estudantes de São Paulo", "Ypiranga-SP"): ("Ypiranga-SP", "FN"),
    ("1935 APEA", "1936-01-05", "Portuguesa", "Ypiranga-SP"): ("Portuguesa", "FN"),
    ("1968", "1968-06-29", "Guarani", "Palmeiras"): ("Palmeiras", "o Guarani escalou jogador irregular (FN)"),
    ("1984", "1984-09-09", "Palmeiras", "São Paulo"): ("São Paulo", "doping de jogador do Palmeiras (FN)"),
    ("1986", "1986-03-19", "Palmeiras", "Santo André"): ("Palmeiras", "FN"),
    ("1990", "1990-08-05", "Botafogo-SP", "Corinthians"): ("Corinthians", "W.O. 0-2 dado ao Corinthians (FN)"),
}
# jogos que faltam, com os pontos dados fora de campo (sem placar): (temporada, data, mandante, visitante, vencedor, motivo)
JOGOS_EXTRA_WO: list[tuple[str, str, str, str, str, str]] = [
    *[("1906", "1906-08-09", m, v, w, "o SPAC desistiu e a LPF deu os pontos ao adversário (FN; QS-005)") for m, v, w in (
        ("Mackenzie-SP", "São Paulo Athletic", "Mackenzie-SP"), ("São Paulo Athletic", "Paulistano-SP", "Paulistano-SP"),
        ("São Paulo Athletic", "AA das Palmeiras", "AA das Palmeiras"))],
    *[("1906", "1906-09-09", m, v, w, "o Mackenzie desistiu e a LPF deu os pontos ao adversário (FN; QS-005)") for m, v, w in (
        ("AA das Palmeiras", "Mackenzie-SP", "AA das Palmeiras"), ("Mackenzie-SP", "AA das Palmeiras", "AA das Palmeiras"),
        ("Mackenzie-SP", "Paulistano-SP", "Paulistano-SP"), ("Mackenzie-SP", "Germânia", "Germânia"))],
    ("1927 LAF", "1927-10-30", "SC Internacional-SP", "Paulista", "SC Internacional-SP",
     "W.O. (\"0 x WO\" na página, que o leitor não pega; \"WO-0\" no FN); com ele as campanhas fecham com a tabela da RSSSF"),
]
# títulos divididos (decisão D-07): temporada -> (campeões, vice); o campeão da classificação fica em campeao e o outro
# na coluna co_campeao de edicoes.csv (formato do agente 1, 23/11)
CAMPEOES_DIVIDIDOS: dict[str, tuple[list[str], str]] = {"1973": (["Portuguesa", "Santos"], "Palmeiras")}
# observação de cada edição (coluna "observacao" de edicoes.csv)
OBS_EDICAO: dict[str, list[str]] = {
    "1973": ["título dividido entre Portuguesa e Santos: a final terminou 0-0 e o árbitro encerrou os pênaltis com 2-0 para "
             "o Santos quando a Portuguesa ainda podia empatar; a FPF declarou os dois campeões (o Santos só chega aos 22 "
             "títulos da lista oficial com este) e o Palmeiras herdou o vice (D-07, SP-001)"],
}
# vice que a ordem calculada não dá: temporada -> (clube, motivo)
VICE_OFICIAL: dict[str, tuple[str, str]] = {
    "1906": ("SC Internacional-SP", "a AA das Palmeiras, com mais pontos, foi eliminada pela LPF em 22/10/1906 (irregularidades "
             "na venda de ingressos); vice pela RSSSF, pelo FN e pela Wikipédia (QS-005)"),
}
# jogo com placar ou data errados no pacote: (temporada, data gravada ou "", mandante, visitante) -> (campos novos, motivo).
# Placar: 2 fontes contra 1 (FN e ogol, o mesmo jogo pelo código; achado QS-012)
JOGO_CORRIGIDO: dict[tuple[str, str, str, str], tuple[dict, str]] = {
    ("1952", "1953-01-25", "Radium", "Palmeiras"): ({"placar": (3, 2)}, "FN e ogol (QS-012)"),
    ("1952", "1953-02-01", "Ypiranga-SP", "Nacional-SP"): ({"placar": (3, 1)}, "FN e ogol (QS-012)"),
    ("1981", "1981-06-18", "XV de Jaú", "São Paulo"): ({"placar": (1, 1)}, "FN e ogol (QS-012)"),
    ("1995", "1995-03-20", "Santos", "Ponte Preta"): ({"placar": (4, 1)}, "FN e ogol (QS-012)"),
    ("1999", "1999-01-31", "Rio Branco-SP", "São José-SP"): ({"placar": (2, 1)}, "FN e ogol (QS-012)"),
    ("2014", "2014-02-26", "XV de Piracicaba", "São Paulo"):
        ({"placar": (1, 3)}, "FN, ogol e FPF (jogo 103); os 3 autores do São Paulo já estão na página (QS-012)"),
    # 1998: o 2-4 do torneio do descenso (22/03) casou com o jogo de 11/02 do ogol (2-1 da 1ª fase, que na página vem sem
    # data); cada um volta ao seu dia (FN e ogol; QS-012)
    ("1998", "1998-02-11", "Portuguesa Santista", "Juventus-SP"):
        ({"data": "1998-03-22", "fonte_id": ""}, "jogo do torneio do descenso, rodada 2 [Mar 22] na página e no FN (QS-012)"),
    ("1998", "", "Portuguesa Santista", "Juventus-SP"):
        ({"data": "1998-02-11", "fonte_id": "ogol:2535435"}, "jogo da 1ª fase, rodada 7 [Feb 11,12]; dia pelo FN e o ogol (QS-012)"),
}
# jogos que faltam, com a fase já em português: (temporada, data, mandante, visitante, placar "g-g" ou "wo-m"/"wo-v", fase,
# grupo, motivo). Fonte: Futebol Nacional (achados QS-007 e SP-018)
JOGOS_EXTRA: list[tuple[str, str, str, str, str, str, str, str]] = [
    *[("1916 LPF", d, m, "Ruggerone", "wo-m", "Fase única", "", "W.O. do Ruggerone (\"WO-0\" no FN)") for d, m in (
        ("1916-07-30", "Vicentino"), ("1916-08-14", "Corinthians"), ("1916-10-15", "Minas Gerais FC"), ("1916-11-19", "Paysandu-SP"))],
    ("1920", "1920-08-08", "Santos", "Minas Gerais FC", "wo-v", "Fase única", "", "o Santos não compareceu (FN)"),
    ("1920", "1920-08-15", "Santos", "Portuguesa", "wo-v", "Fase única", "",
     "o Santos abandonou a competição (FN; a página escreve \"Santos WO x 0 Mack-Port\")"),
    ("1929 LAF", "1929-04-28", "AA das Palmeiras", "Atlético Santista", "3-2", "Fase única", "", "FN (SP-018)"),
    ("1957", "1957-10-19", "São Bento de SCS", "Linense", "1-0", "Fase de Classificação", "Série Branca",
     "1ª rodada do torneio do rebaixamento (FN)"),
    ("1966", "1966-12-22", "Guarani", "Noroeste", "3-1", "Desempate", "", "desempate do rebaixamento; o Noroeste caiu (FN)"),
]


def correcoes_revisao(ano, partidas: list[Partida], log: list[str]) -> list[Partida]:
    """Aplica CLUBES_FORA, JOGOS_FORA, PONTOS_FORA_DE_CAMPO e JOGOS_EXTRA_WO; e o W.O. sem placar da RSSSF ("victory awarded
    to X") passa a contar como vitória sem gols de quem ganhou os pontos (achado SP-016)."""
    t = str(ano)
    usados = set()
    def chave(p):
        return (t, p.data, nome(p.mandante), nome(p.visitante))
    fora = {c for (tt, c) in CLUBES_FORA if tt == t}
    saida = []
    tirados = Counter()
    for p in partidas:
        if fora & {nome(p.mandante), nome(p.visitante)}:
            for c in fora & {nome(p.mandante), nome(p.visitante)}:
                usados.add(("clube", c))
                tirados[c] += 1
            continue
        if abandonado(p) and p.gm is not None:
            log.append(f"{t}: jogo abandonado sem valor fica sem placar: {nome(p.mandante)} {p.gm}-{p.gv} {nome(p.visitante)} ({p.data})")
            p.gm = p.gv = None
            p.gols = []
        k = (t, p.data or "", nome(p.mandante), nome(p.visitante))
        if k in JOGO_CORRIGIDO:
            campos, motivo = JOGO_CORRIGIDO[k]
            usados.add(k)
            if "placar" in campos:
                velho = f"{p.gm}-{p.gv}"
                p.gm, p.gv = campos["placar"]
                p.obs = "; ".join(x for x in (p.obs, f"placar {velho} da RSSSF trocado por {p.gm}-{p.gv}: {motivo}") if x)
                log.append(f"{t}: placar corrigido — {nome(p.mandante)} {velho} -> {p.gm}-{p.gv} {nome(p.visitante)} ({p.data}): {motivo}")
            if "data" in campos:
                log.append(f"{t}: data corrigida — {nome(p.mandante)} {p.gm}-{p.gv} {nome(p.visitante)}: {p.data or 'sem data'} -> "
                           f"{campos['data']}: {motivo}")
                p.data = campos["data"]
            if "fonte_id" in campos:
                p.fonte_id = campos["fonte_id"]
        if chave(p) in JOGOS_FORA:
            usados.add(chave(p))
            log.append(f"{t}: jogo cancelado fica de fora: {nome(p.mandante)} {p.gm}-{p.gv} {nome(p.visitante)} — {JOGOS_FORA[chave(p)]}")
            continue
        if chave(p) in PONTOS_FORA_DE_CAMPO:
            usados.add(chave(p))
            venc, motivo = PONTOS_FORA_DE_CAMPO[chave(p)]
            campo = f"{p.gm}-{p.gv}" if p.gm is not None else "sem placar"
            p.especial = "wo-m" if venc == nome(p.mandante) else "wo-v"
            p.obs = "; ".join(x for x in (p.obs, f"pontos dados ao {venc} fora de campo ({motivo}); placar de campo {campo}") if x)
            p.gm = p.gv = None
            p.gols = []
            log.append(f"{t}: {nome(p.mandante)} {campo} {nome(p.visitante)} — pontos para o {venc} ({motivo})")
        elif p.gm is None and p.especial == "awd":
            m = re.search(r"awarded(?:\s+[\d-]+)?\s+to\s+(.+?)(?:,|$)", p.obs or "")
            if m:
                alvo = m.group(1).strip()
                sm, sv = _sim(alvo, nome(p.mandante)), _sim(alvo, nome(p.visitante))
                if max(sm, sv) >= 0.5 and sm != sv:
                    p.especial = "wo-m" if sm > sv else "wo-v"
        saida.append(p)
    for c in sorted(fora):
        log.append(f"{t}: {tirados[c]} jogos do {c} ficam de fora — {CLUBES_FORA[(t, c)]}")
    por_nome = {nome(x): x for p in saida for x in (p.mandante, p.visitante)}
    fase = saida[0].fase if saida else ""
    for tt, d, m, v, w, motivo in JOGOS_EXTRA_WO:
        if tt != t:
            continue
        if m not in por_nome or v not in por_nome:
            raise ValueError(f"{t}: clube do jogo extra não está na edição: {m} x {v}")
        saida.append(Partida(ano, fase, "", None, d, por_nome[m], por_nome[v], None, None, especial="wo-m" if w == m else "wo-v",
                             fonte="Futebol Nacional", fonte_id="fn", obs=f"pontos dados ao {w} fora de campo: {motivo}"))
        usados.add((tt, d, m, v))
        log.append(f"{t}: jogo que faltava, sem placar: {m} x {v} ({d}), pontos para o {w} — {motivo}")
    faltou = [k for k in [*JOGOS_FORA, *PONTOS_FORA_DE_CAMPO, *JOGO_CORRIGIDO] if k[0] == t and k not in usados] + \
             [c for (tt, c) in CLUBES_FORA if tt == t and ("clube", c) not in usados]
    if faltou:
        raise ValueError(f"{t}: correção da revisão sem jogo correspondente: {faltou}")
    return saida


def jogos_extra(ano, partidas: list[Partida], log: list[str]) -> None:
    """Acrescenta os JOGOS_EXTRA da temporada (depois das fases em português)."""
    t = str(ano)
    por_nome = {nome(x): x for p in partidas for x in (p.mandante, p.visitante)}
    for tt, d, m, v, placar, fase, grupo, motivo in JOGOS_EXTRA:
        if tt != t:
            continue
        if m not in por_nome or v not in por_nome:
            raise ValueError(f"{t}: clube do jogo extra não está na edição: {m} x {v}")
        if any(p.data == d and {nome(p.mandante), nome(p.visitante)} == {m, v} for p in partidas):
            raise ValueError(f"{t}: o jogo extra já está no pacote: {m} x {v} ({d})")
        if placar.startswith("wo"):
            gm = gv = None
            w = m if placar == "wo-m" else v
            obs, especial = f"pontos dados ao {w} fora de campo: {motivo}", placar
        else:
            gm, gv = map(int, placar.split("-"))
            obs, especial = f"jogo que falta na RSSSF e no ogol: {motivo}", None
        partidas.append(Partida(ano, fase, grupo, None, d, por_nome[m], por_nome[v], gm, gv, especial=especial,
                                fonte="Futebol Nacional", fonte_id="fn", obs=obs))
        log.append(f"{t}: jogo que faltava: {m} {placar} {v} ({d}, {fase}{' / ' + grupo if grupo else ''}) — {motivo}")


def mapear_nomes(ano: int, rs: list, og: list[dict], log: list[str]) -> dict:
    """Nome na RSSSF -> código do ogol, por grupo: a mesma página às vezes usa o mesmo nome curto para clubes
    diferentes em grupos diferentes ("Esportivo" de Bento Gonçalves e de Passos em 1988).
    Cada jogo da RSSSF vota nos jogos do ogol de mesmo placar e data próxima (o voto pesa mais quando os nomes
    parecem); depois, dentro de cada grupo, um para um, do par mais votado para o menos.
    Devolve chaves (nome, fase, grupo) e, para as tabelas gerais, o nome sozinho."""
    noms = nomes_ogol(ano, og)
    fs = clubes_sp1.fichas()
    cache: dict[tuple, float] = {}
    def sim(n, i):
        """Parecença do nome; a UF escrita no nome da RSSSF ("São José(RS)") desempata homônimos."""
        if (n, i) not in cache:
            s = max((_sim(n, x) for x in noms.get(i, ()) if x), default=0)
            uf_n, uf_i = clubes_sp1.separar_uf(n.replace("(", " (").strip())[1], fs.get(i, {}).get("uf")
            if uf_n and uf_i:
                s = s * 0.6 if uf_n != uf_i else min(1.0, s + 0.05)
            cache[(n, i)] = s
        return cache[(n, i)]
    nomes_todos = {x for j in rs for x in (j.mandante, j.visitante)}
    sem_uf = lambda n: re.sub(r"\s*\([A-Z]{2}\)$", "", n).strip()   # "Betim (MG)" vale como "Betim"
    por_base = {sem_uf(n): v[0] for (a, n), v in NOME_MANUAL.items() if a == ano}
    manual = {n: por_base[sem_uf(n)] for n in nomes_todos if sem_uf(n) in por_base}
    nomes_rs = {x for j in rs for x in (j.mandante, j.visitante)}
    # 1ª etapa: nomes inequívocos (um só clube do ogol com nome igual ou quase)
    ancora: dict[str, str] = dict(manual)
    for n in nomes_rs - set(ancora):
        cands = sorted(((sim(n, i), i) for i in noms), reverse=True)
        if cands and cands[0][0] >= 0.85 and (len(cands) == 1 or cands[1][0] < cands[0][0]):
            ancora[n] = cands[0][1]
    # 2ª etapa: votos dos jogos de mesmo placar e data próxima; o voto vale muito quando o adversário já está ancorado
    # e bate com o do ogol, e pouco quando não
    v_nome: dict[tuple, float] = defaultdict(float)
    v_ctx: dict[tuple, float] = defaultdict(float)
    for j in rs:
        if j.gm is None:
            continue
        dj = _dia(j.data)
        for o in og:
            if (o["gols_mandante"], o["gols_visitante"]) != (j.gm, j.gv) or not o.get("mandante_id"):
                continue
            do = _dia(o["data"])
            if dj and do and abs(dj - do) > 4:
                continue
            base = 1.0 if dj and do else 0.3
            for n, i, adv, adv_i in ((j.mandante, o["mandante_id"], j.visitante, o["visitante_id"]),
                                     (j.visitante, o["visitante_id"], j.mandante, o["mandante_id"])):
                if adv in ancora:
                    peso = 6.0 * base if ancora[adv] == adv_i else 0.0
                else:
                    peso = 0.3 * base * (1 + 2 * sim(adv, adv_i))
                if peso:
                    v_nome[(n, i)] += peso
                    v_ctx[(n, j.fase, j.grupo, i)] += peso
    saida: dict = {}
    # nome sozinho (tabelas gerais e reserva): âncoras primeiro, depois o resto, um para um
    pontos = [(v_nome.get((n, i), 0) + 6 * sim(n, i), n, i) for n in nomes_rs for i in noms if v_nome.get((n, i)) or sim(n, i) >= 0.6]
    usados: set[str] = set()
    for n, i in ancora.items():
        saida[n] = i; usados.add(i)
    for _, n, i in sorted(pontos, reverse=True):
        if n not in saida and i not in usados:
            saida[n] = i; usados.add(i)
    for n in nomes_rs - set(saida):   # duas grafias do mesmo clube na página ("Juventus" e "Juventus-SP")
        cands = [(sim(n, i), i) for i in usados]
        if cands and max(cands)[0] >= 0.85:
            saida[n] = max(cands)[1]
    # por grupo
    ctxs: dict[tuple, set] = defaultdict(set)
    for j in rs:
        ctxs[(j.fase, j.grupo)] |= {j.mandante, j.visitante}
    for (f, g), ns in ctxs.items():
        # vale o clube do nome; o grupo só troca quando os jogos dele apontam outro clube com folga
        for n in ns:
            base = manual.get(n) or saida.get(n)
            votos = {i: v for (n2, f2, g2, i), v in v_ctx.items() if (n2, f2, g2) == (n, f, g)}
            melhor = max(votos, key=votos.get) if votos else None
            if melhor and melhor != base and n not in manual and votos[melhor] >= 4 and votos[melhor] >= 3 * votos.get(base, 0):
                saida[(n, f, g)] = melhor
            elif base:
                saida[(n, f, g)] = base
    sem = sorted(n for n in nomes_rs if n not in saida)
    for n in sem:
        log.append(f"{ano}: nome da RSSSF sem clube no ogol (jogos dele ficam de fora): {n}")
    return saida


def penaltis(nota: str) -> tuple[int | None, int | None]:
    m = re.search(r"(?:pen(?:alties|altis)?|on penalties|nos pênaltis)\D{0,4}(\d{1,2})\s*[-x]\s*(\d{1,2})|(\d{1,2})-(\d{1,2}) on penalties", nota or "", re.I)
    if not m:
        return None, None
    a, b = (m[1], m[2]) if m[1] else (m[3], m[4])
    return int(a), int(b)


def ler_rsssf(ano: int, mapa: dict[str, str], rs: list) -> list[Partida]:
    saida = []
    for j in rs:
        m, v = mapa.get((j.mandante, j.fase, j.grupo)) or mapa.get(j.mandante), mapa.get((j.visitante, j.fase, j.grupo)) or mapa.get(j.visitante)
        if not (m and v):
            continue
        p = Partida(ano, j.fase, j.grupo, j.rodada, j.data, m, v, j.gm, j.gv, hora=j.hora or None, especial=j.especial,
                    estadio=j.estadio or None, publico=j.publico, fonte=FONTE_RSSSF.format(ano=str(ano)[:4]), gols_texto=j.gols, obs=j.nota, linha=j.linha)
        p.pen_m, p.pen_v = penaltis(f"{j.nota} {j.gols}")
        txt = re.sub(r"\[pen \d+-\d+\]", "", j.gols or "").strip()   # pênaltis que vieram junto dos autores (2015)
        p.gols_texto = txt
        if txt:
            lidos = gols_rsssf.ler_planilha(txt, j.gm, j.gv) if j.hora or j.estadio else None
            if lidos is None and txt.startswith("["):
                lidos = gols_rsssf.ler(txt, j.gm, j.gv, j.mandante, j.visitante)
            if lidos is not None and (lidos or (j.gm == 0 and j.gv == 0)):
                p.gols = [{**g, "fonte": "RSSSF"} for g in lidos]
        if j.estadio:
            p.estadio = re.sub(r"[-/][^-/]*-[A-Z]{2}$|[-/][A-Za-zÀ-ú .]+$", "", j.estadio).strip() or j.estadio
            mc = re.search(r"[-/]([^-/]+?)(?:-[A-Z]{2})?$", j.estadio)
            p.cidade = mc.group(1).strip() if mc else None
        saida.append(p)
    return saida


def abandonado(p: Partida) -> bool:
    """Jogo abandonado que não vale (sem "result stands" na nota): fica sem placar e fora da campanha (achado QS-009)."""
    return p.especial == "abd" and "result stands" not in (p.obs or "").lower()


def campanha(partidas: list[Partida], so: set | None = None) -> dict[str, list[int]]:
    c: dict[str, list[int]] = defaultdict(lambda: [0] * 6)
    for p in partidas:
        if abandonado(p):
            continue
        if p.gm is None and p.especial in ("wo-m", "wo-v"):   # pontos dados fora de campo: vitória sem gols (D-15, SP-016)
            venc, perd = (p.mandante, p.visitante) if p.especial == "wo-m" else (p.visitante, p.mandante)
            c[venc][0] += 1; c[venc][1] += 1
            c[perd][0] += 1; c[perd][3] += 1
            continue
        if p.gm is None:
            continue
        for eu, a, b in ((p.mandante, p.gm, p.gv), (p.visitante, p.gv, p.gm)):
            x = c[eu]
            x[0] += 1; x[4] += a; x[5] += b
            x[1 if a > b else 2 if a == b else 3] += 1
    return c


def tabelas_por_clube(tabelas: list, mapa: dict[str, str], rs: list) -> list[tuple]:
    """[(tabela, {código: [J, V, E, D, GP, GC]})] com os nomes da tabela trocados pelo código do clube."""
    saida = []
    for tb in tabelas:
        if not tb.linhas:
            continue
        nomes_fase = {x for j in rs if j.fase == tb.fase and (not tb.grupo or j.grupo == tb.grupo) for x in (j.mandante, j.visitante)}
        alias = rsssf.casar([r["nome"] for r in tb.linhas], nomes_fase or {x for j in rs for x in (j.mandante, j.visitante)})
        if len(alias) < len(tb.linhas):
            alias.update(rsssf.casar([r["nome"] for r in tb.linhas if r["nome"] not in alias], {x for j in rs for x in (j.mandante, j.visitante)}))
        linhas, nome_id = {}, {}
        for r in tb.linhas:
            nr = alias.get(r["nome"], "")
            c = mapa.get((nr, tb.fase, tb.grupo)) or mapa.get(nr)
            if c:
                linhas[c] = [r["j"], r["v"], r["e"], r["d"], r["gp"], r["gc"]]
                nome_id[r["nome"]] = c
        saida.append((tb, linhas, nome_id))
    return saida


def bloco_da_tabela(tb, partidas: list[Partida]) -> list[Partida]:
    b = [p for p in partidas if p.fase == tb.fase and (p.grupo == tb.grupo or not tb.grupo)]
    if not tb.grupo and len({p.fase for p in partidas}) > 1 and re.search(r"final standings|classifica|overall|geral|^table$", tb.titulo or "", re.I):
        return partidas
    return b


def decidir_placar(p: Partida, alt: tuple[int, int], partidas: list[Partida], tabs: list[tuple]) -> bool:
    """True se o placar alternativo fecha melhor com as tabelas publicadas (dos dois clubes) que o atual."""
    def erros(lista):
        n = 0
        for tb, linhas, _ in tabs:
            if p.mandante not in linhas and p.visitante not in linhas:
                continue
            bl = bloco_da_tabela(tb, lista)
            if p not in bl and not any(q is p for q in bl):
                continue
            camp = campanha(bl)
            n += sum(camp.get(c) != linhas[c] for c in (p.mandante, p.visitante) if c in linhas)
        return n
    antes = erros(partidas)
    velho = (p.gm, p.gv)
    p.gm, p.gv = alt
    depois = erros(partidas)
    p.gm, p.gv = velho
    return depois < antes


def juntar_ogol(ano: int, partidas: list[Partida], og: list[dict], tabs: list[tuple], rs_ok: bool, log: list[str]) -> list[Partida]:
    """Casa cada jogo da RSSSF com o do ogol (mesmo par de clubes, data mais próxima); confere o placar; traz a hora,
    a data que falta e a rodada oficial ("R12"); inclui o que só o ogol tem."""
    usados: set[str] = set()
    datas_trocadas: list[Partida] = []
    datas_dif: list[tuple] = []
    por_par: dict[tuple, list[dict]] = defaultdict(list)
    for o in og:
        por_par[(o.get("mandante_id"), o.get("visitante_id"))].append(o)
    # antes: o mesmo jogo com o mando invertido, no mesmo dia e com o placar espelhado. Nas finais a RSSSF escreve as
    # partidas com o mesmo clube na frente ("[Dec 08] São Paulo 3-0 Corinthians", "[Dec 15] São Paulo 0-0 Corinthians"):
    # quando o mesmo par aparece assim mais de uma vez na fase, vale o mando do ogol
    for p in partidas:
        if p.gm is None or not _dia(p.data):
            continue
        if any(_dist(o["data"], p.data) <= 1 and (o["gols_mandante"], o["gols_visitante"]) == (p.gm, p.gv)
               for o in por_par.get((p.mandante, p.visitante), []) if o["id"] not in usados):
            continue
        inv = [o for o in por_par.get((p.visitante, p.mandante), []) if o["id"] not in usados and _dia(o["data"])
               and _dist(o["data"], p.data) <= 1 and (o["gols_mandante"], o["gols_visitante"]) == (p.gv, p.gm)]
        if len(inv) != 1:
            continue
        o = inv[0]
        usados.add(o["id"])
        repetido = sum((q.fase, q.mandante, q.visitante) == (p.fase, p.mandante, p.visitante) for q in partidas) > 1
        if repetido:
            log.append(f"{ano}: mando da RSSSF trocado pelo do ogol (a página escreve as partidas de {nome(p.mandante)} x "
                       f"{nome(p.visitante)} na {p.fase} sempre na mesma ordem) — ogol {nome(o['mandante_id'])} "
                       f"{o['gols_mandante']}-{o['gols_visitante']} {nome(o['visitante_id'])} ({o['data']})")
            p.mandante, p.visitante, p.gm, p.gv = p.visitante, p.mandante, p.gv, p.gm
            p.pen_m, p.pen_v = p.pen_v, p.pen_m
            p.gols = [{**g, "lado": "visitante" if g.get("lado") == "mandante" else "mandante"} for g in p.gols]
        else:
            log.append(f"{ano}: mando invertido no ogol — RSSSF {nome(p.mandante)} {p.gm}-{p.gv} {nome(p.visitante)}, ogol "
                       f"{nome(o['mandante_id'])} {o['gols_mandante']}-{o['gols_visitante']} {nome(o['visitante_id'])} "
                       f"({o['data']}); fica a RSSSF")
        p.fonte_id, p.ogol_fase, p.data = f"ogol:{o['id']}", o["fase"], o["data"]
        p.hora = p.hora or o.get("hora")
        p.rodada = p.rodada or o.get("rodada")
    for p in sorted(partidas, key=lambda p: (p.data is None, p.data or "")):
        if p.fonte_id or abandonado(p):   # o jogo abandonado não pega o placar do jogo refeito (QS-009)
            continue
        cands = [o for o in por_par.get((p.mandante, p.visitante), []) if o["id"] not in usados]
        if not cands:
            continue
        trocada = _trocar_dia_mes(p.data)
        dist = lambda o: min(_dist(o["data"], p.data), _dist(o["data"], trocada) if trocada else 999)
        cands.sort(key=lambda o: (dist(o), (o["gols_mandante"], o["gols_visitante"]) != (p.gm, p.gv)))
        o = cands[0]
        mesmo_placar = (o["gols_mandante"], o["gols_visitante"]) == (p.gm, p.gv)
        if dist(o) > 40 and not (mesmo_placar and dist(o) <= 120):   # data do título da fase nos jogos (1991, 1994)
            continue
        usados.add(o["id"])
        if p.data and o["data"] and _dia(o["data"]) and _dist(o["data"], p.data) > 3:
            if trocada and _dist(o["data"], trocada) <= 3:
                datas_trocadas.append(p)
            else:
                datas_dif.append((p, o["data"]))
            p.data = o["data"]   # a do ogol (a da RSSSF fica no relatório)
        p.fonte_id = f"ogol:{o['id']}"
        p.ogol_fase = o["fase"]
        p.ogol_placar = (o["gols_mandante"], o["gols_visitante"])
        p.hora = p.hora or o.get("hora")
        if not p.data:
            p.data = o["data"]
        if o.get("rodada") and not p.rodada:
            p.rodada = o["rodada"]
        alt = (o["gols_mandante"], o["gols_visitante"])
        if alt[0] is not None and p.gm is not None and alt != (p.gm, p.gv) and not p.especial:
            if decidir_placar(p, alt, partidas, tabs):
                log.append(f"{ano}: placar corrigido pelo ogol — {nome(p.mandante)} x {nome(p.visitante)} ({p.data}): "
                           f"RSSSF {p.gm}-{p.gv}, ogol {alt[0]}-{alt[1]}; fica o do ogol, que fecha com a tabela publicada")
                p.obs = (p.obs + "; " if p.obs else "") + f"placar da RSSSF {p.gm}-{p.gv} corrigido pelo ogol (fecha com a tabela publicada)"
                p.gm, p.gv = alt
                if p.gols and len(p.gols) != p.gm + p.gv:
                    p.gols = []
            else:
                log.append(f"{ano}: placar diferente no ogol — {nome(p.mandante)} x {nome(p.visitante)} ({p.data}): "
                           f"RSSSF {p.gm}-{p.gv}, ogol {alt[0]}-{alt[1]}; fica o da RSSSF")
        elif p.gm is None and alt[0] is not None:
            p.gm, p.gv = alt
    if datas_trocadas:
        log.append(f"{ano}: data com dia e mês trocados na RSSSF em {len(datas_trocadas)} jogos (ex.: {nome(datas_trocadas[0].mandante)} x "
                   f"{nome(datas_trocadas[0].visitante)}); fica a data do ogol")
    if datas_dif:
        p, d = datas_dif[0]
        log.append(f"{ano}: data diferente entre RSSSF e ogol (mais de 3 dias) em {len(datas_dif)} jogos (ex.: {nome(p.mandante)} x "
                   f"{nome(p.visitante)}, ogol {d}); fica a do ogol")
    # o que sobrou nas duas fontes e é o mesmo jogo: mando invertido (placar espelhado) ou um dos clubes diferente
    # no mesmo dia e com o mesmo placar. Fica o da RSSSF (base), e a diferença vai para o relatório.
    sobra = [p for p in partidas if not p.fonte_id and not abandonado(p)]
    ano_ed = int(str(ano)[:4])
    no_ano = lambda d: bool(d) and ano_ed <= int(d[:4]) <= ano_ed + 1   # edições que acabam no ano seguinte (1952, 1978)
    for o in og:
        if o["id"] in usados or o["gols_mandante"] is None:
            continue
        m, v, gm, gv = o.get("mandante_id"), o.get("visitante_id"), o["gols_mandante"], o["gols_visitante"]
        perto = lambda p: _dia(p.data) and _dia(o["data"]) and _dist(p.data, o["data"]) <= 4
        inv = [p for p in sobra if (p.mandante, p.visitante) == (v, m) and (p.gm, p.gv) == (gv, gm) and _dist(p.data, o["data"]) <= 3]
        inv_placar = [p for p in sobra if (p.mandante, p.visitante) == (v, m) and perto(p)]
        mesmo_par = [p for p in sobra if (p.mandante, p.visitante) == (m, v) and perto(p)]
        outro = [p for p in sobra if perto(p) and (p.gm, p.gv) == (gm, gv) and (p.mandante == m) != (p.visitante == v)]
        # mesmo jogo, mesmo dia e mês, ano diferente (1979: "19.08.78" num jogo de agosto de 1979)
        ano_errado = [p for p in sobra if (p.mandante, p.visitante) == (m, v) and (p.gm, p.gv) == (gm, gv) and p.data
                      and o["data"] and p.data[4:] == o["data"][4:] and p.data[:4] != o["data"][:4]]
        if len(ano_errado) == 1:
            p = ano_errado[0]
            usados.add(o["id"]); sobra.remove(p)
            # fica a data cujo ano é o da edição (o ogol às vezes copia o erro da página: 1929 LAF, 1979; QS-002, QS-003)
            fica = "da RSSSF" if no_ano(p.data) and not no_ano(o["data"]) else "do ogol"
            log.append(f"{ano}: ano errado numa das datas — {nome(m)} {gm}-{gv} {nome(v)}: RSSSF {p.data}, ogol {o['data']}; "
                       f"fica a {fica}")
            p.data = p.data if fica == "da RSSSF" else o["data"]
            p.fonte_id, p.ogol_fase = f"ogol:{o['id']}", o["fase"]
            p.hora = p.hora or o.get("hora")
            continue
        for lista, texto in ((inv, "mando invertido"), (inv_placar, "mando invertido e placar diferente"),
                             (mesmo_par, "placar diferente (jogo não achado pela data)"), (outro, "adversário diferente")):
            if len(lista) == 1:
                p = lista[0]
                usados.add(o["id"]); sobra.remove(p)
                p.fonte_id = f"ogol:{o['id']}"
                p.hora = p.hora or o.get("hora")
                log.append(f"{ano}: {texto} no ogol — RSSSF {nome(p.mandante)} {p.gm}-{p.gv} {nome(p.visitante)}, ogol {nome(m)} {gm}-{gv} "
                           f"{nome(v)} ({o['data']}); fica a RSSSF")
                break
    novos = []
    # 2007-2013 e 2017-2023: o calendário do ogol traz junto o Troféu do Interior (2023: a Taça Independência), torneio à parte entre clubes já eliminados, que a
    # leitura da RSSSF deixa de fora. Depois da 1ª fase, jogo só do ogol fica de fora quando é um jogo do Troféu na página
    # da RSSSF, quando os dois clubes jogaram o Troféu (a página às vezes não traz todos os jogos dele) ou quando nenhum
    # dos dois está no mata-mata do campeonato
    fim_1a, mata = None, set()
    trof_pares, trof_clubes = TROFEU.get(str(ano), (set(), set()))
    if rs_ok and int(str(ano)[:4]) in rsssf_sp1.ANOS_A_PARTE and partidas:
        com_data = sorted((p for p in partidas if p.data), key=lambda p: p.data)
        primeira = com_data[0].fase
        fim_1a = max(p.data for p in com_data if p.fase == primeira)
        mata = {x for p in partidas if p.fase != primeira for x in (p.mandante, p.visitante)}
    for o in og:
        if o["id"] in usados or o["gols_mandante"] is None or not (o.get("mandante_id") and o.get("visitante_id")):
            continue
        m, v = o["mandante_id"], o["visitante_id"]
        if fim_1a and o["data"] > fim_1a and (frozenset((m, v)) in trof_pares or {m, v} <= trof_clubes
                                              or not (m in mata or v in mata)):
            log.append(f"{ano}: jogo {'da Taça Independência' if str(ano) == '2023' else 'do Troféu do Interior'} no ogol "
                       f"(torneio à parte), fica de fora: "
                       f"{nome(m)} {o['gols_mandante']}-{o['gols_visitante']} {nome(v)} ({o['data']})")
            continue
        fase, grupo = fase_do_ogol(o, partidas)
        q = Partida(ano, fase, grupo, o.get("rodada"), o["data"], m, v, o["gols_mandante"], o["gols_visitante"], hora=o.get("hora"),
                    fonte="ogol", fonte_id=f"ogol:{o['id']}", ogol_fase=o["fase"])
        if re.search(r"\(\s*\d+\s*-\s*\d+\s*\)|pen", o.get("resultado") or "", re.I):
            mp = re.search(r"\(\s*(\d+)\s*-\s*(\d+)\s*\)", o["resultado"])
            if mp:
                q.pen_m, q.pen_v = int(mp[1]), int(mp[2])
        novos.append(q)
        if rs_ok:
            log.append(f"{ano}: jogo só no ogol, incluído em {fase}{' / ' + grupo if grupo else ''}: "
                       f"{nome(m)} {q.gm}-{q.gv} {nome(v)} ({q.data})")
    if rs_ok:
        for p in partidas:
            if not p.fonte_id and og:
                log.append(f"{ano}: só na RSSSF (não achado no ogol): {nome(p.mandante)} {p.gm}-{p.gv} {nome(p.visitante)} ({p.data})")
    return partidas + novos


OGOL_FASE = {"1F": "Primeira fase", "2F": "Segunda fase", "3F": "Terceira fase", "4F": "Quarta fase", "1/16": "Primeira fase eliminatória",
             "1/8": "Oitavas de final", "QF": "Quartas de final", "SF": "Semifinal", "F": "Final"}


def fase_do_ogol(o: dict, partidas: list[Partida]) -> tuple[str, str]:
    """Fase e grupo de um jogo que só o ogol tem: a fase e o grupo em que os dois clubes jogaram juntos, perto da data;
    senão, pelo código de fase do ogol."""
    m, v, d = o["mandante_id"], o["visitante_id"], _dia(o["data"])
    grupos = agrupar(partidas)
    if d:
        perto, cobre = [], []
        for (f, g), ps in grupos.items():
            ds = [x for x in (_dia(p.data) for p in ps) if x]
            if not ds:
                continue
            cl = {x for p in ps for x in (p.mandante, p.visitante)}
            if m in cl and v in cl and min(ds) - 3 <= d <= max(ds) + 3:
                perto.append((min(abs(x - d) for x in ds), f, g))
            if min(ds) - 1 <= d <= max(ds) + 1:
                cobre.append(f)
        if perto:
            _, f, g = min(perto)
            return f, g
        # jogo que falta na página (o confronto todo): a única fase jogada naqueles dias (2022: quartas de final)
        if len(set(cobre)) == 1:
            return cobre[0], ""
    juntos = []
    for (f, g), ps in grupos.items():
        cl = {x for p in ps for x in (p.mandante, p.visitante)}
        if m in cl and v in cl:
            ds = [x for x in (_dia(p.data) for p in ps) if x]
            dist = min((abs(x - d) for x in ds), default=99) if d else 50
            juntos.append((dist, f, g))
    if juntos:
        _, f, g = min(juntos)
        return f, g
    f = o.get("fase") or ""
    if f in OGOL_FASE:
        return OGOL_FASE[f], ""
    if re.match(r"^R\d+$", f):
        return "Primeira fase", ""
    return "Primeira fase", f"Grupo {f}" if f else ""


def agrupar(partidas: list[Partida]) -> dict[tuple, list[Partida]]:
    d: dict[tuple, list[Partida]] = defaultdict(list)
    for p in partidas:
        d[(p.fase, p.grupo)].append(p)
    return d


def ler_espn(ano: int) -> list[dict]:
    f = ESPN / f"sp1_{str(ano).replace(" ", "_")}.json"
    return [j for j in json.loads(f.read_text(encoding="utf-8")) if j["situacao"] in ("STATUS_FULL_TIME", "STATUS_FINAL", "STATUS_FINAL_PEN",
                                                                                      "STATUS_FINAL_AET")] if f.exists() else []


def juntar_espn(ano: int, partidas: list[Partida], log: list[str]) -> None:
    """ESPN: hora local, estádio e cidade. O nome da ESPN vira código do ogol pelos jogos de mesmo placar no mesmo dia."""
    es = ler_espn(ano)
    if not es:
        return
    votos: dict[tuple, int] = defaultdict(int)
    por_dia: dict[str, list[Partida]] = defaultdict(list)
    for p in partidas:
        if p.data:
            por_dia[p.data].append(p)
    def local(e):
        utc = datetime.strptime(e["data_hora"][:16], "%Y-%m-%dT%H:%M")
        return utc - timedelta(hours=3)
    for e in es:
        l = local(e)
        for dia in (l.strftime("%Y-%m-%d"), (l - timedelta(days=1)).strftime("%Y-%m-%d"), (l + timedelta(days=1)).strftime("%Y-%m-%d")):
            for p in por_dia.get(dia, []):
                if (p.gm, p.gv) == (int(e["gols_mandante"]), int(e["gols_visitante"])):
                    votos[(e["mandante_id"], p.mandante)] += 1
                    votos[(e["visitante_id"], p.visitante)] += 1
    mapa, usados = {}, set()
    for (eid, cid), n in sorted(votos.items(), key=lambda x: -x[1]):
        if eid not in mapa and cid not in usados and n >= 2:
            mapa[eid] = cid; usados.add(cid)
    casados = 0
    for e in es:
        m, v = mapa.get(e["mandante_id"]), mapa.get(e["visitante_id"])
        l = local(e)
        cands = [p for p in partidas if (p.mandante, p.visitante) == (m, v) and _dia(p.data) and abs(_dia(p.data) - l.toordinal()) <= 2]
        if len(cands) != 1:
            continue
        p = cands[0]
        casados += 1
        if (p.gm, p.gv) != (int(e["gols_mandante"]), int(e["gols_visitante"])):
            log.append(f"{ano}: placar diferente na ESPN — {nome(m)} x {nome(v)} ({p.data}): aqui {p.gm}-{p.gv}, "
                       f"ESPN {e['gols_mandante']}-{e['gols_visitante']}; fica o daqui")
        p.hora = l.strftime("%H:%M")
        p.estadio = p.estadio or e.get("estadio")
        p.cidade = p.cidade or e.get("cidade")
        if e.get("publico"):
            p.publico = e["publico"]
        p.fonte_id = (p.fonte_id + ";" if p.fonte_id else "") + f"espn:{e['id']}"
    if casados < len(es):
        log.append(f"{ano}: ESPN — {casados} de {len(es)} jogos casados (hora e estádio)")


# --------------------------------------------------------------------------------------------- fases e nomes

FASES_PT = [
    # Paulista: turnos (com as grafias das páginas) e fases com outro nome
    (r"^final table", "Primeira fase"),   # 1996: os jogos do 1º turno vêm sob o título da tabela final
    (r"^(1º|1o\.?|1ª|primeiro)\s*turno\s*-\s*qualifying", "1º Turno - Classificatória"),
    (r"^(2º|2o\.?|segundo)\s*turno\s*-\s*qualifying", "2º Turno - Classificatória"),
    (r"^(2º|2o\.?|segundo)\s*turno\s*-\s*1st phase", "2º Turno - 1ª fase"),
    (r"^(2º|2o\.?|segundo)\s*turno\s*-\s*2nd phase", "2º Turno - 2ª fase"),
    (r"^(1º|1o\.?|1ª|primeiro)\s*turno", "1º Turno"), (r"^(2º|2o\.?|segundo)\s*turno", "2º Turno"),
    (r"^phase 1$", "Primeira fase"), (r"^phase 2$", "Segunda fase"), (r"^phase 3$", "Terceira fase"),
    (r"^repescagem", "Repescagem"), (r"relegation", "Torneio de rebaixamento"),
    (r"decide which team would be eliminated", "Desempate"), (r"1995 - final fase", "Fase final"),
    (r"^semfinals?$", "Semifinal"), (r"^final playoff", "Final"), (r"^classifica[çc][ãa]o final", "Fase final"),
    # 1977: três turnos, os dois primeiros com semifinal e final próprias
    (r"^first stage - first phase", "1º Turno"), (r"^first stage - semi", "1º Turno - Semifinal"),
    (r"^first stage - final", "1º Turno - Final"), (r"^second stage - first phase", "2º Turno"),
    (r"^second stage - semi", "2º Turno - Semifinal"), (r"^second stage - final", "2º Turno - Final"),
    (r"^third stage$", "3º Turno"),
    (r"^(fase única|first stage|first phase|1st phase|1a fase|1ª fase|primeira fase|grupo único|group stage)", "Primeira fase"),
    (r"^(second (phase|stage|round)|2nd phase|2a fase|2ª fase|segunda fase)", "Segunda fase"),
    (r"^(third (phase|stage)|3rd phase|3a fase|terceira fase)(?!.*(semi|final))", "Terceira fase"),
    (r"^(fourth (phase|stage)|4th phase|quarta fase)(?!.*(semi|final))", "Quarta fase"),
    (r"serie c\s*-\s*-\s*fourth phase", "Quarta fase"),
    (r"round of 32", "Segunda fase"), (r"^(round of 16|1/8|eighth|oitavas)", "Oitavas de final"),
    (r"(quarter|quartas)", "Quartas de final"), (r"(semi)", "Semifinal"),
    (r"(final phase|final stage|quadrangular final|final standings)", "Fase final"),
    (r"(^|\W)finals?\W*$|final$|^final", "Final"), (r"knockout", "Mata-mata"),
]


def grupo_pt(g: str) -> str:
    """"Group A" -> "Grupo A"; "Green Group" -> "Grupo Verde"; "Série Branca (Torneio de Rebaixamento)" -> "Série Branca";
    "teams of Group 1 against teams of Group 2" (jogos entre os grupos) -> sem grupo."""
    g = (g or "").strip(" :")
    if re.match(r"teams\b", g, re.I):
        return ""
    g = re.sub(r"\s*\(.*\)$", "", g)
    cores = {"green": "Verde", "yellow": "Amarelo", "blue": "Azul", "white": "Branco", "red": "Vermelho", "black": "Preto",
             "gold": "Dourado", "silver": "Prata"}
    if (m := re.match(r"^(\w+) group$|^group (\w+)$", g, re.I)) and (m[1] or m[2]).lower() in cores:
        return f"Grupo {cores[(m[1] or m[2]).lower()]}"
    return re.sub(r"^group\b", "Grupo", g, flags=re.I)


def fase_pt(nome_fase: str) -> str:
    n = nome_fase.strip(" :")
    for padrao, pt in FASES_PT:
        if re.search(padrao, n, re.I):
            return pt
    return n


# nome da RSSSF -> código do ogol, de todas as temporadas já lidas (o mesmo clube em anos sem calendário no ogol)
JA_CASADOS: dict[str, str] = {}
# temporada -> (pares de clubes, clubes) dos jogos do Troféu do Interior na página da RSSSF (2017-2022)
TROFEU: dict[str, tuple[set, set]] = {}


def completar_sem_ogol(ano, mapa: dict, rs: list, og: list, log: list[str]) -> None:
    """Nomes da RSSSF sem clube no ogol daquela temporada: usa o clube do mesmo nome em outra temporada do Paulista;
    se nunca apareceu, vira clube só da RSSSF ("rs-..."), com o nome da página."""
    for n, i in list(mapa.items()):
        if isinstance(n, str):
            JA_CASADOS.setdefault(clubes_sp1.norm(n), i)
    sem = sorted({x for j in rs for x in (j.mandante, j.visitante)} - {n for n in mapa if isinstance(n, str)})
    fs = clubes_sp1.fichas()
    for n in sem:
        i = JA_CASADOS.get(clubes_sp1.norm(n))
        if not i:   # o mesmo nome numa ficha do ogol (clube de temporadas lidas mais adiante: Atlético Sorocaba em 2003)
            achados = [k for k, f in fs.items() if not k.startswith("rs-") and clubes_sp1.norm(n) in
                       {clubes_sp1.norm(x) for x in (f.get("curto"), *f.get("nomes_ogol", [])) if x}]
            i = achados[0] if len(achados) == 1 else None
        if i:
            mapa[n] = i
            log.append(f"{ano}: {n} — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas ({nome(i)})")
        else:
            mapa[n] = clubes_sp1.sem_ogol(n)
            JA_CASADOS[clubes_sp1.norm(n)] = mapa[n]
            log.append(f"{ano}: {n} — clube que o ogol não tem; entra só pela RSSSF")
    for j in rs:   # chaves por grupo, como as de mapear_nomes
        for n in (j.mandante, j.visitante):
            mapa.setdefault((n, j.fase, j.grupo), mapa.get(n))


def nome(cid: str) -> str:
    return clubes_sp1.exibicao().get(cid, {}).get("clube", cid)


# --------------------------------------------------------------------------------------------- classificação

def pontos_vitoria(ano) -> int:
    return 3 if int(str(ano)[:4]) >= 1995 else 2


def ajustes_wiki(ano: int, ids_do_ano: set[str]) -> dict[str, int]:
    """Punições de pontos na Wikipédia em inglês (adjust_points), com o nome casado ao código do ogol."""
    saida = {}
    fs = clubes_sp1.exibicao()
    for nome_w, v in wiki.ajustes(ano).items():
        cands = sorted(((_sim(nome_w, fs[i]["clube"]), i) for i in ids_do_ano if i in fs), reverse=True)
        if cands and cands[0][0] >= 0.75 and v:
            saida[cands[0][1]] = v
    return saida


def classificacao(ano: int, partidas: list[Partida], tabs: list[tuple], ajustes: dict[str, int], campeao: str | None,
                  log: list[str]) -> list[dict]:
    """Fase alcançada, depois pontos (com punições), vitórias, saldo e gols pró; o campeão e o vice da final em cima.
    Quando a RSSSF publica a classificação geral com todos os clubes e ela fecha com os jogos, vale a ordem dela."""
    camp = campanha(partidas)
    pv = pontos_vitoria(ano)
    sem_nivel = sorted({p.fase for p in partidas} - set(ORDEM))
    if sem_nivel:   # fase nova sem nível: antes caía num padrão 50, acima da Final (achado SP-002)
        raise ValueError(f"{ano}: fase sem nível no ORDEM: {sem_nivel}")
    alcance: dict[str, int] = defaultdict(int)
    for p in partidas:
        for c in (p.mandante, p.visitante):
            alcance[c] = max(alcance[c], ORDEM[p.fase])
    final = [p for p in partidas if p.fase == "Final"]
    vice = None
    if campeao and final:
        fin = {x for p in final for x in (p.mandante, p.visitante)} - {campeao}
        if len(fin) == 1:
            vice = next(iter(fin))
        elif fin:   # quadrangular/triangular final (1997): o vice é o 2º do grupo final
            cf = campanha(final)
            vice = max(fin, key=lambda c: (pv * cf[c][1] + cf[c][2], cf[c][1], cf[c][4] - cf[c][5], cf[c][4]))
    if str(ano) in VICE_OFICIAL:
        alvo, motivo = VICE_OFICIAL[str(ano)]
        vice = next(c for c in camp if nome(c) == alvo)
        log.append(f"{ano}: vice {alvo} — {motivo}")
    # liga decisiva de um grupo só ("Fase final", 1957): quem chegou a ela desempata pelos pontos dela antes dos totais
    ff = [p for p in partidas if p.fase == "Fase final"]
    cff = campanha(ff) if ff and len({p.grupo for p in ff}) == 1 else {}
    def pts(c):
        x = camp[c]
        return pv * x[1] + x[2] + ajustes.get(c, 0)
    def chave(c):
        x, y = camp[c], cff.get(c, [0] * 6)
        return (c != campeao, c != vice, -alcance[c], -(pv * y[1] + y[2]), -pts(c), -x[1], -(x[4] - x[5]), -x[4], nome(c))
    # classificação geral publicada pela RSSSF (todos os clubes da edição)
    geral = [(tb, linhas) for tb, linhas, _ in tabs if len(linhas) >= len(camp) and len(tb.linhas) >= len(camp)]
    fonte = "calculada (fase alcançada, pontos, vitórias, saldo, gols pró)"
    ordem = sorted(camp, key=chave)
    if geral:
        tb, linhas = geral[-1]
        bate = sum(camp.get(c) == v for c, v in linhas.items())
        if bate >= 0.9 * len(camp):   # a ordem das linhas é a ordem da tabela
            ordem = list(linhas) + [c for c in ordem if c not in linhas]
            fonte = "RSSSF (classificação geral publicada)"
    saida = []
    for i, c in enumerate(ordem, 1):
        x = camp[c]
        saida.append({"pos": i, "clube": c, "j": x[0], "v": x[1], "e": x[2], "d": x[3], "gp": x[4], "gc": x[5], "pts": pts(c),
                      "ajuste": ajustes.get(c, 0), "fonte": fonte})
    return saida


ORDEM = {"Primeira fase": 1, "Segunda fase": 2, "Terceira fase": 3, "Quarta fase": 4, "Mata-mata": 5, "Primeira fase eliminatória": 5,
         "Oitavas de final": 6, "Quartas de final": 7, "Semifinal": 8, "Fase final": 9, "Final": 10,
         # turnos e fases de classificação: o nível da 1ª fase (as decisões de cada turno não são a decisão do campeonato)
         "Fase única": 1, "1º Turno": 1, "2º Turno": 1, "3º Turno": 1, "Fase de Classificação": 1, "Torneio de Classificação": 1,
         "1º Turno - Classificatória": 1, "2º Turno - Classificatória": 1, "2º Turno - 1ª fase": 1, "2º Turno - 2ª fase": 1,
         "1º Turno - Quartas de final": 1, "1º Turno - Semifinal": 1, "1º Turno - Final": 1, "2º Turno - Semifinal": 1,
         "2º Turno - Final": 1,
         # repescagem, torneio de rebaixamento e desempate de eliminação não decidem o pódio (achado SP-007)
         "Repescagem": 0, "Torneio de rebaixamento": 0, "Desempate": 0}

# fase errada na fonte, por temporada inteira: (temporada, fase gravada) -> (fase certa, motivo)
FASE_ANO: dict[tuple[str, str], tuple[str, str]] = {
    ("1976", "2º Turno"): ("Fase final", "o \"2º turno\" de 1976 é a fase final com os 12 melhores (achado SP-008)"),
}
# fase errada por jogo, pela data: (temporada, fase gravada, data de, data até, fase certa, motivo); o par de clubes da
# decisão de verdade fica fora (2003: Corinthians x São Paulo, a final de março)
FASE_JOGO: list[tuple[str, str, str, str, str, str]] = [
    ("1978", "Quartas de final", "1978-11-01", "1978-11-30", "1º Turno - Quartas de final", "decisão do 1º turno (SP-008)"),
    ("1978", "Semifinal", "1978-11-01", "1978-11-30", "1º Turno - Semifinal", "decisão do 1º turno (SP-008)"),
    ("1978", "Final", "1978-11-01", "1978-11-30", "1º Turno - Final", "decisão do 1º turno (SP-008)"),
    ("1978", "Primeira fase", "1979-06-20", "1979-06-30", "Final", "a final Santos x São Paulo de junho de 1979 (SP-008)"),
    ("1981", "Final", "1981-04-01", "1981-04-30", "1º Turno - Final", "decisão do 1º turno (SP-008)"),
    ("1981", "Final", "1981-08-01", "1981-08-31", "2º Turno - Final", "decisão do 2º turno (SP-008)"),
    ("1998", "Final", "1998-02-01", "1998-04-30", "Torneio de rebaixamento", "quadrangular do rebaixamento (SP-007)"),
    ("2003", "Final", "2003-03-01", "2003-03-31", "Torneio de rebaixamento", "torneio da morte (SP-007)"),
    ("2002", "Fase única", "2002-06-01", "2002-06-10", "Repescagem",
     "Francana x Portuguesa Santista, playoff contra a A2 (SP-019; são os 2 únicos jogos de junho de 2002)"),
]
FASE_JOGO_FORA = {("2003", frozenset({"Corinthians", "São Paulo"}))}


def fase_certa(ano, p: Partida) -> str:
    t = str(ano)
    if (t, p.fase) in FASE_ANO:
        return FASE_ANO[(t, p.fase)][0]
    if (t, frozenset({nome(p.mandante), nome(p.visitante)})) in FASE_JOGO_FORA:
        return p.fase
    for tt, f, de, ate, nova, _ in FASE_JOGO:
        if t == tt and p.fase == f and p.data and de <= p.data <= ate:
            return nova
    return p.fase


# --------------------------------------------------------------------------------------------- uma edição

def campeoes() -> tuple[dict[str, str], dict[str, str]]:
    """Campeões pela RSSSF (spcamp.htm): temporada -> nome; nos anos de duas ligas a linha traz "[LPF]" / "[APEA]" / "[LAF]".
    E pela Wikipédia (artigo do Campeonato Paulista, quadro de títulos por clube): temporada -> nomes do ano, separados por " / "
    (nos anos de duas ligas a Wikipédia não diz qual título é de qual liga)."""
    rs: dict[str, str] = {}
    t = rsssf.texto(0, "spcamp.htm")
    ano = None
    for l in t.splitlines():
        m = re.match(r"^\s*(\d{4}) - (.+?)\s*$", l) or (ano and re.match(r"^\s{4,}()(\S.+?)\s*$", l))
        if not m:
            continue
        if m.group(1):
            ano = m.group(1)
        nome = m.group(2)
        if "Superchampionship" in nome:   # 2002: o Supercampeonato é outra competição; o campeão paulista é o Ituano
            continue
        liga = re.search(r"\[(LPF|APEA|LAF)\]", nome)
        nome = re.sub(r"\s*\(.*$", "", nome).strip()
        rs[f"{ano} {liga.group(1)}" if liga else ano] = nome
    wk: dict[str, str] = {}
    f = PASTA_DADOS / "wikipedia" / "pt_lista.txt"
    if f.exists():
        # quadro ano a ano: "|[[Campeonato Paulista de Futebol de 1990|1990]]", "|<small>FPF</small>", "|'''{{Futebol Bragantino}}'''";
        # nos anos de duas ligas, a linha seguinte começa direto pela liga ("|<small>APEA</small>")
        ultimo = None
        for linha in f.read_text(encoding="utf-8").split("\n|-"):
            cel = [c for c in linha.split("\n|")[1:] if c.strip()]   # o 1º pedaço é o resto da linha "|- align=center"
            if len(cel) < 2:
                continue
            ano_wk = re.search(r"\b(19\d{2}|20\d{2})\b", re.sub(r"\{\{nre.*", "", cel[0]))
            liga = re.search(r"<small>\s*(?:\[\[[^\]|]*\|)?(LPF|APEA|LAF)(?:\]\])?\s*</small>", " ".join(cel[:2]))
            if ano_wk and "Campeonato Paulista" not in cel[0] and not cel[0].lstrip("| ").startswith(("rowspan", "1", "2")):
                continue   # quadro de títulos por clube (o ano não é o primeiro campo)
            if not ano_wk and not (liga and ultimo):
                continue
            y = ano_wk.group(1) if ano_wk else ultimo
            ultimo = y
            negrito = next((c for c in cel[1:] if "'''" in c), "")   # o campo do ano pode ter nota com negrito
            nm = (re.search(r"'''\s*\{\{\s*[Ff]utebol\s+([^}|]+)", negrito)
                  or re.search(r"'''\s*\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", negrito))
            if not nm:
                continue
            campeao = re.sub(r"\s*\(.*?\)\s*$", "", nm.group(1)).strip()
            chave_wk = f"{y} {liga.group(1)}" if liga else y
            wk[chave_wk] = campeao
            if chave_wk != y and y in wk:   # ano de duas ligas: "Americano / Paulistano"
                wk[y] = f"{wk[y]} / {campeao}"
            else:
                wk[y] = campeao
    return rs, wk


def montar_edicao(ano: int, log: list[str], rs_campeoes: dict, wk_campeoes: dict) -> dict:
    try:
        rs, tabelas = rsssf_sp1.ler(ano)
    except FileNotFoundError:
        if str(ano) not in BASE_OGOL:
            raise
        rs, tabelas = [], []   # sem página da RSSSF: base no ogol
    for (a, n), motivo in RSSSF_FORA.items():
        if str(a) == str(ano):
            fora = [j for j in rs if n in (j.mandante, j.visitante)]
            rs = [j for j in rs if j not in fora]
            log.append(f"{ano}: {len(fora)} jogos do {n} ficam de fora: {motivo}")
    for (a, m, v, gm, gv), motivo in JOGOS_ANULADOS.items():
        if str(a) == str(ano):
            fora = [j for j in rs if (j.mandante, j.visitante, j.gm, j.gv) == (m, v, gm, gv)]
            rs = [j for j in rs if j not in fora]
            log.append(f"{ano}: jogo anulado fica de fora ({len(fora)}): {m} {gm}-{gv} {v} — {motivo}")
    for i, motivo in OGOL_IGNORAR.items():
        if motivo.startswith(str(ano)):
            log.append(f"{ano}: jogo do ogol ignorado — {motivo[6:]}")
    og = ler_ogol(ano)
    rs_ok = ano not in BASE_OGOL
    if not rs_ok:
        log.append(f"{ano}: {BASE_OGOL[ano]}")
        rs_usado, tabelas = [], []
    else:
        rs_usado = rs
    if ano in TABELAS_PARCIAIS:
        log.append(f"{ano}: {TABELAS_PARCIAIS[ano]}")
        tabelas = []
    de_um_jogo = [tb for tb in tabelas if tb.linhas and max(r["j"] for r in tb.linhas) <= 1]
    if de_um_jogo:   # "Standings" depois da 1ª rodada do mata-mata (2020): retrato parcial, não é conferência
        log.append(f"{ano}: {len(de_um_jogo)} tabelas da página com um jogo por clube (retrato parcial de mata-mata) ficam fora da conferência")
        tabelas = [tb for tb in tabelas if tb not in de_um_jogo]
    mapa = mapear_nomes(ano, rs_usado, og, log) if rs_usado else {}
    completar_sem_ogol(ano, mapa, rs_usado, og, log)
    partidas = ler_rsssf(ano, mapa, rs_usado)
    partidas = [p for p in partidas if p.gm is not None or p.especial]
    tabs = tabelas_por_clube(tabelas, mapa, rs_usado)
    if int(str(ano)[:4]) in rsssf_sp1.ANOS_A_PARTE:   # jogos do Troféu do Interior / Taça Independência, para tirar do ogol
        tj = rsssf_sp1.trofeu(str(ano))
        cod = lambda n: mapa.get(n) or JA_CASADOS.get(clubes_sp1.norm(n))
        TROFEU[str(ano)] = ({frozenset((cod(j.mandante), cod(j.visitante))) for j in tj},
                            {c for j in tj for c in (cod(j.mandante), cod(j.visitante)) if c})
    partidas = juntar_ogol(ano, partidas, og, tabs, rs_ok, log)
    juntar_espn(ano, partidas, log)   # sem arquivo da ESPN, não faz nada
    partidas = correcoes_revisao(ano, partidas, log)
    # fases em português, nos jogos e nas tabelas (as tabelas já estão ligadas aos códigos dos clubes)
    for p in partidas:
        p.fase = fase_pt(p.fase) if rs_ok else fase_pt(OGOL_FASE.get(p.ogol_fase, p.fase))
        p.grupo = grupo_pt(p.grupo) if not p.grupo.lower().startswith(("grupo único", "grupo unico")) else ""
    for tb in tabelas:
        tb.fase = fase_pt(tb.fase)
        tb.grupo = grupo_pt(tb.grupo)
    if len({p.fase for p in partidas}) == 1 and not any(p.grupo for p in partidas):
        for x in [*partidas, *tabelas]:
            x.fase = "Fase única"
    # fases erradas na fonte (decisões de turno gravadas como "Final", torneio de rebaixamento dentro da "Final"...)
    mudou = Counter()
    for p in partidas:
        nova = fase_certa(ano, p)
        if nova != p.fase:
            mudou[(p.fase, nova)] += 1
            p.fase = nova
    for tb in tabelas:
        tb.fase = FASE_ANO.get((str(ano), tb.fase), (tb.fase,))[0]
    for (de, para), n in sorted(mudou.items()):
        log.append(f"{ano}: {n} jogos da fase \"{de}\" passam para \"{para}\" (FASE_ANO/FASE_JOGO)")
    jogos_extra(ano, partidas, log)
    fpf_sp1.aplicar(ano, partidas, nome, log)   # data oficial 2007+; fase e grupo de 2024-2026 (QS-008, SP-008)
    # autores: só quando fecham com o placar
    for p in partidas:
        if p.gols and p.gm is not None and len(p.gols) != p.gm + p.gv:
            p.gols = []
    ids = {x for p in partidas for x in (p.mandante, p.visitante)}
    ajustes = {}   # Paulista: sem punições lidas da Wikipédia
    # campeão: vencedor da final; conferido com a RSSSF e a Wikipédia (final empatada sem pênaltis: vale a lista oficial)
    campeao = vencedor_final(partidas)
    oficial = campeao_oficial(ano, partidas, rs_campeoes, wk_campeoes)
    tem_final = any(p.fase in ("Final", "Fase final") for p in partidas)
    if campeao is None and oficial and not tem_final:
        # sem final (pontos corridos, ou finais com outro nome): confere com o 1º da campanha da última fase
        lider = lider_ultima_fase(ano, partidas)
        campeao = oficial
        if lider != oficial:
            log.append(f"{ano}: campeão pela lista oficial, {nome(oficial)}; o 1º pela soma dos jogos da última fase é "
                       f"{nome(lider) if lider else '?'} (desempate, jogo extra ou pontos tirados fora de campo)")
    elif campeao is None and oficial:
        campeao = oficial
        log.append(f"{ano}: final sem vencedor nos placares (decidida por campanha ou fora de campo): campeão pela lista oficial, {nome(oficial)}")
    elif oficial and campeao != oficial:
        log.append(f"{ano}: vencedor da final pelos jogos ({nome(campeao)}) diferente do campeão oficial ({nome(oficial)}); fica o oficial")
        campeao = oficial
    final = classificacao(ano, partidas, tabs, ajustes, campeao, log)
    conf = conferir(ano, partidas, tabs)
    return {"partidas": partidas, "tabelas": tabelas, "tabs": tabs, "final": final, "conf": conf, "rs": rs, "og": og,
            "mapa": mapa, "campeao": campeao, "ajustes": ajustes}


def campeao_oficial(ano: int, partidas: list[Partida], rs_c: dict, wk_c: dict) -> str | None:
    """O clube da edição cujo nome bate com o campeão da lista da Wikipédia (ou, sem ela, da RSSSF)."""
    alvo = rs_c.get(ano) or (wk_c.get(str(ano)) or wk_c.get(str(ano)[:4], "")).split(" / ")[0]
    if not alvo:
        return None
    fs = clubes_sp1.fichas()
    ids = {x for p in partidas for x in (p.mandante, p.visitante)}
    def nota(i):
        nomes = {nome(i), *(fs.get(i, {}).get("nomes_ogol") or []), fs.get(i, {}).get("nome_completo") or "", fs.get(i, {}).get("curto", "")}
        uf = clubes_sp1.separar_uf(alvo)[1]   # "Botafogo-PB" x "Botafogo-SP": a UF desempata
        # "Associação Atlética São Bento" (nome completo na lista da RSSSF): também sem a sigla por extenso
        curto = re.sub(r"^(Associa[çc][ãa]o|Sport|Clube|Club|Esporte|Sociedade|Gr[eê]mio|Athletic|Atl[eé]tica|Atl[eé]tico|"
                       r"Esportiva|Esportivo|Recreativa|Recreativo|Club[e]?|de|Futebol|Football|Paulista|\s)+\b", "", alvo, flags=re.I).strip()
        cheio = max(_sim(alvo, x) for x in nomes if x)
        # o nome completo desempata ("Internacional": o SC da capital e o CA de Santos, em 1907)
        return (max(cheio, max(_sim(curto, x) for x in nomes if x) if curto else 0) + 0.05 * cheio
                + (0.1 if uf and fs.get(i, {}).get("uf") == uf else 0))
    melhor = sorted(((nota(i), i) for i in ids), reverse=True)
    return melhor[0][1] if melhor and melhor[0][0] >= 0.8 and (len(melhor) == 1 or melhor[1][0] < melhor[0][0]) else None


# edições em que a RSSSF não serve de base (o ogol é a base dos jogos)
BASE_OGOL: dict[str, str] = {
    "2026": "a RSSSF ainda não tem a página de 2026 (SP-004, D-01): os jogos vêm do ogol, e a fase e o grupo da FPF",
}
# edições em que as tabelas publicadas pela RSSSF são parciais (a página parou no meio): não servem de conferência
TABELAS_PARCIAIS: dict[str, str] = {"2025": "a página da RSSSF parou na 6ª rodada da 1ª fase: as tabelas dela são parciais e não servem de conferência; os outros jogos vêm do ogol"}


def lider_ultima_fase(ano, partidas: list[Partida]) -> str | None:
    """O 1º pela soma dos jogos da fase do último jogo (pontos, vitórias, saldo, gols pró)."""
    com_data = [p for p in partidas if p.data and p.gm is not None]
    if not com_data:
        return None
    fase = max(com_data, key=lambda p: p.data).fase
    camp = campanha([p for p in partidas if p.fase == fase])
    pv = pontos_vitoria(ano)
    return max(camp, key=lambda c: (pv * camp[c][1] + camp[c][2], camp[c][1], camp[c][4] - camp[c][5], camp[c][4])) if camp else None


def vencedor_final(partidas: list[Partida]) -> str | None:
    final = [p for p in partidas if p.fase == "Final"]
    if not final:
        final = [p for p in partidas if p.fase == "Fase final"]
        if not final:
            return None
        camp = campanha(final)
        return max(camp, key=lambda c: (3 * camp[c][1] + camp[c][2], camp[c][4] - camp[c][5], camp[c][4]))
    gols, pen = Counter(), Counter()
    for p in final:
        gols[p.mandante] += p.gm or 0; gols[p.visitante] += p.gv or 0
        if p.pen_m is not None:
            pen[p.mandante] += p.pen_m; pen[p.visitante] += p.pen_v
    times = list(gols)
    if len(times) != 2:
        return None
    a, b = times
    if gols[a] != gols[b]:
        return a if gols[a] > gols[b] else b
    if pen[a] != pen[b]:
        return a if pen[a] > pen[b] else b
    return None


def motivo_divergencia(c: str, tabela: list, jogos: list | None, bloco: list[Partida]) -> str:
    """Por que a linha da tabela publicada não bate com os jogos do clube."""
    ps = [p for p in bloco if c in (p.mandante, p.visitante)]
    if jogos is None or not ps:
        return "o clube não aparece nos jogos desse bloco (tabela de outra fase ou grupo da página)"
    if tabela[0] != jogos[0]:
        return f"a tabela conta {tabela[0]} jogos e as fontes trazem {jogos[0]}"
    sem_ogol = [p for p in ps if p.ogol_placar is None]
    difere = [p for p in ps if p.ogol_placar is not None and p.ogol_placar != (p.gm, p.gv)]
    if difere:
        p = difere[0]
        return (f"placar diverge entre RSSSF e ogol em {nome(p.mandante)} x {nome(p.visitante)} ({p.gm}-{p.gv} x "
                f"{p.ogol_placar[0]}-{p.ogol_placar[1]}) e nenhuma das versões fecha com a tabela; fica a RSSSF")
    if sem_ogol:
        return "há jogo do clube sem conferência no ogol"
    return "RSSSF e ogol trazem os mesmos placares para todos os jogos do clube: o erro é da tabela publicada"


def conferir(ano: int, partidas: list[Partida], tabs: list[tuple]) -> dict:
    """Cada tabela publicada pela RSSSF contra a soma dos jogos do pacote, do mesmo grupo (ou da edição inteira,
    na classificação geral)."""
    ok, dif, linhas_dif = 0, 0, []
    for tb, linhas, _ in tabs:
        if not linhas:
            continue
        # o bloco da tabela; a fase dela; cada fase (a "Standings" de 2015, no fim da página, é a da 1ª fase); a edição
        cands = [bloco_da_tabela(tb, partidas), [p for p in partidas if p.fase == tb.fase],
                 [p for p in partidas if p.linha and p.linha < tb.linha],   # tabela que soma os turnos de antes
                 *[[p for p in partidas if p.fase == f] for f in {p.fase for p in partidas}], partidas]
        melhor, bloco = None, []
        for bl in cands:
            camp = campanha(bl)
            e = [(c, v, camp.get(c)) for c, v in linhas.items() if camp.get(c) != v]
            if melhor is None or len(e) < len(melhor):
                melhor, bloco = e, bl
        if melhor:
            dif += 1
            linhas_dif += [f"{tb.fase} / {tb.grupo or '-'}: {nome(c)} tabela {v} jogos {x} — {motivo_divergencia(c, v, x, bloco)}"
                           for c, v, x in melhor]
        else:
            ok += 1
    return {"ok": ok, "dif": dif, "linhas": linhas_dif}


# --------------------------------------------------------------------------------------------- saída

def main(anos: list[int], gravar: bool) -> None:
    log: list[str] = []
    rs_c, wk_c = campeoes()
    edicoes = {}
    for ano in anos:
        e = montar_edicao(ano, log, rs_c, wk_c)
        edicoes[ano] = e
        ps = e["partidas"]
        print(f"{ano}: {len(ps)} jogos (RSSSF {len(e['rs'])}, ogol {len(e['og'])}), tabelas ok {e['conf']['ok']} / divergentes "
              f"{e['conf']['dif']}, gols c/ autor {sum(len(p.gols) for p in ps)} de {sum((p.gm or 0) + (p.gv or 0) for p in ps)}, "
              f"campeão {nome(e['campeao']) if e['campeao'] else '?'} (RSSSF: {rs_c.get(ano, '-')}; Wikipédia: {wk_c.get(ano, '-')})", flush=True)
        if len(anos) == 1:
            for l in e["conf"]["linhas"]:
                print("   !", l)
    if len(anos) == 1:
        for l in log:
            print("   ", l)
    if gravar:
        import pacote
        pacote.gravar(edicoes, log, rs_c, wk_c)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    anos = [a for a in sys.argv[1:] if a[:4].isdigit()]
    main(anos or ANOS, gravar=not anos)
