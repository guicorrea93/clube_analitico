"""Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/col-1/rsssf/) com o leitor comum (rsssf_sul) e,
nos anos que a RSSSF não tem, a Wikipédia em espanhol (wikipedia_jogos.py). As tabelas das páginas da RSSSF dos anos da
Wikipédia e dos anos sem jogos entram pelos trechos "tabelas" da edição.

Uso como biblioteca: ler(edicao) -> (jogos, tabelas); campeoes() -> {temporada: campeão como na página}.
Uso direto: python coleta/col-1/ler_rsssf.py [temporada ...]   (resumo de jogos e tabelas por edição)
"""
from __future__ import annotations

import re
import sys
from functools import lru_cache
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
sys.path.insert(0, str(AQUI))
import rsssf_sul  # noqa: E402
import json  # noqa: E402
import wikipedia_jogos  # noqa: E402
from datetime import datetime, timedelta  # noqa: E402
from edicoes import EDICOES, FIM_PADRAO, PASTA_DADOS, Edicao  # noqa: E402

PASTA = PASTA_DADOS / "rsssf"

# fases reconhecidas pelo título (a primeira é a fase de partida); vale para todas as edições
FASES = [
    # mata-matas e quadrangulares das páginas colombianas
    (r"(?i)^Playoffs?$", "Quadrangulares semifinais"),   # 2019 em diante: "Playoff" abre os quadrangulares (ou as quartas, que vêm logo)
    (r"(?i)^(Cuadrangulares?( Semifinal(es)?| Mustang)?|Semifinal Cuadrang|Clausura Cuadrangulares)\b(?! Final)", "Quadrangulares semifinais"),
    (r"(?i)^Cuadrangular Final", "Quadrangular final"),
    (r"(?i)^(Torneo )?Finalizaci[oó]n", ""),   # título do torneio (não é a final)
    # campeonatos em duas fases: grupo do título e grupo do rebaixamento depois da fase de todos contra todos
    (r"^(Relegation (Group|Round|Liguilla)|Liguilla (de |del |por el )?Descenso|Grupo de Descenso)", "Grupo do rebaixamento"),
    (r"^(Second Stage|Second Phase)\b", "Segunda fase"),
    (r"^(Third Stage|Third Phase)\b", "Terceira fase"),
    (r"^(Championship (Group|Round|Liguilla)|Liguilla (Final|del Campe[oó]n|de Campeonato|por el T[ií]tulo)|"
     r"Final (Group|Round|Stage|Phase)|Hexagonal|Octagonal|Cuadrangular)", "Fase final"),
    (r"^(First Stage|First Phase|Regular (Season|Stage))", ""),
    (r"^(Tabla Anual Playoff|Annual Table Playoff)", "Desempate da tabela anual"),
    (r"^(Round of 16|Octavos de final)\b", "Oitavas de final"),
    (r"^(Quarter[- ]?finals?|Cuartos de final)\b", "Quartas de final"),
    (r"^(Semi[- ]?finals?|Championship Semifinals?)\b", "Semifinal"),
    (r"^(Final(?!\s*(Table|Tournament|Group|Standing|phase|stage|de la Liga))|Championship Final|Final de la Liga|Third and Final Match)",
     "Final"),
    (r"^((Apertura|Intermedio|Clausura) Playoff|Championship Playoff|Playoff:?\s*$|Playoff \[|First Playoff|Desempate)",
     "Desempate do título"),
    (r"^(Second place playoffs?|Second Place Playoff)", "Desempate do 2º lugar"),
    (r"^(Relegation playoff|Relegation Play-?off)", "Desempate do rebaixamento"),
    (r"^(Final Tournament|Championship Round)", "Fase final"),
    (r"^Repechaje", "Repechaje"),
]

# título que abre o campeonato numa página que começa por outra competição (Copa Chile, Copa Apertura)
INICIO = r"^NUNCA$"   # as páginas colombianas abrem pelo campeonato

# Apertura e Clausura são edições no Chile: sem torneio do ano dentro da edição
TORNEIOS: list[tuple[str, str]] = []
FECHA = r"^\b$"   # nunca casa


# páginas de colunas fixas: (início da coluna do visitante, início da coluna do placar)
COLUNAS: dict[str, tuple[int, int]] = {}


@lru_cache(maxsize=None)
def linhas(pagina: str) -> tuple[str, ...]:
    """Texto puro da página, com os erros de digitação corrigidos (explicacoes.CONSERTA_TEXTO, cada um com o motivo)."""
    from explicacoes import CONSERTA_TEXTO
    # travessão no placar ("2–0") em parte das páginas: vira hífen
    ls = [l.replace("–", "-").replace("—", "-") for l in rsssf_sul.texto(PASTA / f"{pagina}.html")]
    if pagina in COLUNAS:   # colunas fixas com um espaço só entre os times ("Defensor Sporting Wanderers   1-1")
        a, b = COLUNAS[pagina]
        for k, l in enumerate(ls):
            if len(l) > b and re.search(r"\s\d{1,2}-\d{1,2}\s*$", l) and l[a - 1] == " " and l[a] != " " and not rsssf_sul.linha_tabela(l):
                ls[k] = f"{l[:a].rstrip()}  {l[a:b].rstrip()}  {l[b:].strip()}"
    for (pg, n), (antes, depois, _motivo) in CONSERTA_TEXTO.items():
        if pg == pagina:
            assert antes in ls[n], f"{pagina}:{n} mudou: {ls[n]!r}"
            ls[n] = ls[n].replace(antes, depois)
    return tuple(ls)


def fim_padrao(ls: tuple[str, ...], ini: int) -> int:
    """Primeira linha, depois do primeiro jogo do trecho, que abre outra competição."""
    viu_jogo = False
    for i in range(ini, len(ls)):
        s = ls[i].strip()
        if not viu_jogo:
            viu_jogo = bool(rsssf_sul._jogo(ls[i]))
            continue
        if re.match(FIM_PADRAO, s, re.I):
            return i
    return len(ls)


def _torneios(ls: tuple[str, ...], ini: int, fim: int) -> tuple[dict[int, str], dict[int, str]]:
    """Por linha: o torneio em vigor ("" = campeonato) e o grupo marcado em "Grupo A [May 27]"."""
    """Por linha: o torneio em vigor ("" = campeonato), o grupo marcado em "Grupo A [May 27]" e se a fase de mata-mata
    lida antes (uma "Final" do Intermedio) ficou velha: título de fase anterior ao começo do torneio em vigor."""
    torneio, grupo = "", ""
    ini_t, ult_fase = -1, -1
    por_linha, grupos, velha = {}, {}, {}
    for i in range(ini, fim):
        s = ls[i].strip()
        if re.match(FECHA, s, re.I):
            torneio, grupo, ini_t = "", "", i
        else:
            for rx, nome in TORNEIOS:
                if re.match(rx, s, re.I):
                    torneio, grupo, ini_t = nome, "", i
                    break
        if any(re.search(rx, s, re.I) for rx, _ in FASES):
            ult_fase = i
        if m := re.match(r"^(?:Grupo|Group|Serie)\s+([A-Z])\b(?!\s*\()", s):
            grupo = m.group(1)
        por_linha[i], grupos[i], velha[i] = torneio, grupo, ult_fase < ini_t
    return por_linha, grupos, velha


def _vitoria_dada(x: rsssf_sul.Jogo) -> None:
    """"[awarded 1-1 win to Progreso because ...; goals stood]": pontos para um lado, os gols do campo contam na tabela.
    Vira W.O. (wo_m/wo_v) com o placar de campo, como a tabela conta."""
    if x.gm_of is None and x.especial == "awd" and (m := re.match(r"^\s*(\d{1,2})\s*-\s*(\d{1,2}) to \w", x.nota)):
        x.gm_of, x.gv_of = int(m.group(1)), int(m.group(2))   # "Sud América Awd Wanderers [0-2 to Wanderers]"
        return
    if re.search(r"award(ed)? of (a )?win to .{2,40}? annulled", x.nota, re.I):   # a decisão caiu: vale o placar de campo
        x.especial = "" if x.gm is not None else x.especial
        return
    m = re.search(r"(?:awarded (?:(\d{1,2})\s*-\s*(\d{1,2}) )?(?:a )?win to|win awarded to)\s+(.+?)"
                  r"(?:\s+(?:as|because|since|for|after|due|with)\b|\s*\(|[;,.\]]|$)", x.nota, re.I)
    if not m:
        return
    quem = rsssf_sul.chave(m.group(3)).split()
    casa = bool(quem) and quem[0] in rsssf_sul.chave(x.mandante).split()
    fora = bool(quem) and quem[0] in rsssf_sul.chave(x.visitante).split()
    if casa == fora:
        return
    if m.group(1):
        x.gm, x.gv = int(m.group(1)), int(m.group(2))
    elif x.gm is None and (mo := re.search(r"originally (\d{1,2})\s*-\s*(\d{1,2})", x.nota, re.I)):
        x.gm, x.gv = int(mo.group(1)), int(mo.group(2))
    x.gm_of = x.gv_of = None
    x.especial = "wo_m" if casa else "wo_v"


def _fase(base: str, torneio: str) -> str:
    if not torneio:
        return base
    if base in ("", "Fase final"):
        return torneio
    if base in ("Final", "Desempate do título"):
        return f"Final do {torneio}"
    if base == "Semifinal":
        return f"Semifinal do {torneio}"
    return base


def ler(e: Edicao) -> tuple[list[rsssf_sul.Jogo], list[rsssf_sul.Tabela]]:
    jogos, tabelas = [], []
    if e.wiki is not None:
        jogos += wikipedia_jogos.jogos(e.wiki)
    externos = espn_jogos(*e.espn) if e.espn is not None else []
    for pagina, ini, fim in e.trechos:
        ls = linhas(pagina)
        if ini == 0:   # a página abre com a copa do começo do ano: o campeonato começa no título dele
            ini = next((i for i, l in enumerate(ls) if re.match(INICIO, l.strip())), 0)
        fim = fim if fim is not None else fim_padrao(ls, ini)
        trecho = [""] * ini + list(ls[ini:fim])   # mantém o número da linha da página
        j, t = rsssf_sul.ler(trecho, e.ano_inicio, e.ano_fim, fases=e.fases + FASES)
        tor, gru, velha = _torneios(ls, ini, fim)
        for x in j:
            x.texto = f"{pagina}:{x.linha}"
            _vitoria_dada(x)
            x.fase = _fase("" if velha.get(x.linha) else x.fase, tor.get(x.linha, ""))
            if not x.grupo and gru.get(x.linha) and x.fase in ("Intermedio", "Clasificatorio", ""):
                x.grupo = gru[x.linha]
        for x in t:
            x.fase = _fase("" if velha.get(x.linha) else x.fase, tor.get(x.linha, ""))
            x.grupo = x.grupo or (gru.get(x.linha, "") if x.fase in ("Intermedio",) else "")
        jogos += j
        tabelas += t
    for pagina, ini, fim in e.tabelas:   # página que só tem a tabela final (os jogos vêm do ogol)
        ls = linhas(pagina)
        tabelas += rsssf_sul.ler([""] * ini + list(ls[ini:fim]), e.ano_inicio, e.ano_fim, fases=e.fases + FASES)[1]
    if e.ano_inicio >= 2002:   # de 2002 em diante a liga não tem grupos: jogo ou tabela com grupo e sem fase é dos quadrangulares
        for x in [*jogos, *tabelas]:
            if x.grupo and not x.fase:
                x.fase = "Quadrangulares semifinais"
    if externos:   # a ESPN também traz os mata-matas que a página tem: dela, só os jogos de antes do primeiro da página
        corte = min((x.data for x in jogos if x.data), default="9999")
        jogos = [x for x in externos if x.data < corte] + jogos
    return jogos, tabelas


def campeoes() -> dict[str, str]:
    """colchamp.html: temporada do pacote ("1962", "1995/96", "2002 Apertura", "2010 Finalización") -> campeão como na página.
    "Ap" ao lado do ano é o Apertura; "Fi" ou "Cl" na linha de baixo, o Finalización."""
    saida: dict[str, str] = {}
    ano = None
    for l in linhas("colchamp"):
        m = re.match(r"^(\d{4}(?:/\d{2})?)?\s+(Ap|Fi|Cl)?\s*(\S.*?)(?:\s{2,}(\S.*))?\s*$", l)
        if not m or not (m.group(1) or m.group(2)) or l.startswith(" " * 12):
            continue
        if m.group(1):
            ano = m.group(1)
        if not ano or re.search(r"not awarded|cancel", m.group(3), re.I):
            continue
        temp = ano if not m.group(2) else f"{ano} {'Apertura' if m.group(2) == 'Ap' else 'Finalización'}"
        saida.setdefault(temp, m.group(3).strip())
    return saida


def _ogol_por_ano() -> dict[int, list[dict]]:
    pasta = PASTA_DADOS / "ogol"
    saida: dict[int, list[dict]] = {}
    for ed in json.loads((pasta / "edicoes.json").read_text(encoding="utf-8")):
        f = pasta / f"{ed['id']}.json"
        if f.exists():
            saida.setdefault(ed["ano_inicio"], []).extend(json.loads(f.read_text(encoding="utf-8")))
    return saida


# fases do calendário do ogol além das rodadas ("R12") e das zonas ("Zona Norte")
OGOL_FASES = {"A": "Fase final", "POut": "Desempate do rebaixamento", "F": "Final", "MF": "Semifinal", "QF": "Quartas de final"}


def ogol_jogos(ano: int) -> list[rsssf_sul.Jogo]:
    """Calendário do ogol do ano como jogos (texto "ogol:<id do jogo>"). A fase "R12" é a 12ª rodada da fase de pontos
    corridos; as outras fases do ogol (liguillas, finais) entram com o nome que o ogol dá."""
    saida = []
    for k, g in enumerate(sorted(_ogol_por_ano().get(ano, []), key=lambda g: (g["data"], g["id"]))):
        if g["gols_mandante"] is None:
            continue
        f = g.get("fase") or ""
        rod = re.fullmatch(r"R(\d+)", f)
        zona = re.fullmatch(r"Zona (\w+)", f)
        fase = "" if rod or zona or not f else OGOL_FASES.get(f, f)
        saida.append(rsssf_sul.Jogo(linha=k, mandante=g["mandante"], visitante=g["visitante"], gm=g["gols_mandante"],
                                    gv=g["gols_visitante"], rodada=int(rod.group(1)) if rod else g.get("rodada"),
                                    data=g["data"] if g["data"][:4] != "0000" else None, fase=fase,
                                    grupo=zona.group(1) if zona else "", texto=f"ogol:{g['id']}"))
    return saida


def espn_jogos(ini: str, fim: str) -> list[rsssf_sul.Jogo]:
    """Jogos encerrados da ESPN (liga chi.1) entre as datas, no horário de Santiago (texto "espn:<id>")."""
    saida = []
    for a in range(int(ini[:4]), int(fim[:4]) + 1):
        f = PASTA_DADOS / "espn" / f"col1_{a}.json"
        for g in json.loads(f.read_text(encoding="utf-8")) if f.exists() else []:
            d = (datetime.fromisoformat(g["data_hora"].replace("Z", "+00:00")) - timedelta(hours=4)).date().isoformat()
            if not ini <= d <= fim or g["situacao"] not in ("STATUS_FULL_TIME", "STATUS_FINAL") or g["gols_mandante"] in (None, ""):
                continue
            saida.append(rsssf_sul.Jogo(linha=len(saida), mandante=g["mandante"], visitante=g["visitante"],
                                        gm=int(g["gols_mandante"]), gv=int(g["gols_visitante"]), data=d, texto=f"espn:{g['id']}"))
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
        print(f"{e.temporada:10s} {len(js):4d} jogos  {len(ts):2d} tabelas  fases {fases}")
