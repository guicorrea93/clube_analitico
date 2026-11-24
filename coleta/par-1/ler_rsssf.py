"""Lê os jogos de cada edição nas páginas da RSSSF (data/coleta/par-1/rsssf/) com o leitor comum (rsssf_sul). Nos anos sem
jogos, lê só a tabela: a completa, quando a página a traz, ou a parcial (posição e pontos: "1.Cerro Porteño   28"), da seção
do ano em parahist.html ou da página do ano.

Uso como biblioteca: ler(edicao) -> (jogos, tabelas); campeoes() e vices() -> {temporada: nome como na página}.
Uso direto: python coleta/par-1/ler_rsssf.py [temporada ...]   (resumo de jogos e tabelas por edição)
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
    (r"^Playoff against 11th Place", "Desempate do rebaixamento"),   # PY-006 (1961, 1963)
    (r"^Triangular de Desempate", "Triangular de desempate"),   # PY-008 (1981): quem vai à final do ano contra o campeão do 1º turno
    (r"^Overall Final", "Final"),   # PY-008 (1981): a final do ano
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
    (r"^Liguilla Pre-Libertadores", "Liguilla pré-Libertadores"),   # PY-008 (2003): vaga na Libertadores, não título
    (r"^Playoff for Third", "Desempate do 3º lugar"),   # PY-008 (1999): 3ª vaga na Libertadores
    (r"^((Apertura|Intermedio|Clausura) Playoff|(\d{4} )?Championship Playoff|Playoff:?\s*$|Playoff \[|First Playoff|Desempate)",
     "Desempate do título"),
    (r"^(Second place playoffs?|Second Place Playoff)", "Desempate do 2º lugar"),
    (r"^(Relegation playoff|Relegation Play-?off)", "Desempate do rebaixamento"),
    (r"^(Final Tournament|Championship Round)", "Fase final"),
    (r"^Repechaje", "Repechaje"),
]

# título que abre o campeonato numa página que começa por outra competição (Copa Chile, Copa Apertura)
INICIO = r"^NUNCA$"   # as páginas colombianas abrem pelo campeonato

# PY-008: de 1996 a 2007 o Apertura e o Clausura são torneios dentro da edição anual; as fases de dentro levam o nome do
# torneio ("Final do Apertura") e a final do ano volta ao campeonato. De 2008 em diante cada torneio é uma edição (sem isso).
TORNEIOS: list[tuple[str, str]] = [
    (r"^(Torneo |First Stage \()?Apertura( \d{4})?\)?$", "Apertura"),
    (r"^(Torneo |Second Stage \()?Clausura( \d{4})?\)?$", "Clausura"),
]
FECHA = (r"^(Final Apertura v Clausura|(\d{4} )?Championship (Playoff|Final)|Aggregate Table|Overall Table|Cuadrangulares$|"
         r"Second Place Playoff|Liguilla Pre-Libertadores|Playoff for Third)")
ANOS_TORNEIOS = range(1996, 2008)


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


def _torneios(ls: tuple[str, ...], ini: int, fim: int, fases: list | None = None) -> tuple[dict[int, str], dict[int, str]]:
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
        if any(re.search(rx, s, re.I) for rx, _ in (fases or FASES)):   # as fases da edição também ("Liguilla", 1998)
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
    # PY-010: também "awarded as a win to" (1960, Tembetary 2-2 Libertad)
    m = re.search(r"(?:awarded (?:(\d{1,2})\s*-\s*(\d{1,2}) )?(?:as )?(?:a )?win to|win awarded to)\s+(.+?)"
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
    if base in ("", "Fase final", torneio):
        return torneio
    if base in ("Final", "Desempate do título"):
        return f"Final do {torneio}"
    return f"{base} do {torneio}"   # "Semifinal do Apertura", "Liguilla do Clausura", "Segunda fase do Apertura"


def ler(e: Edicao) -> tuple[list[rsssf_sul.Jogo], list[rsssf_sul.Tabela]]:
    jogos, tabelas = [], []
    externos = espn_jogos(*e.espn) if e.espn is not None else []
    for pagina, ini, fim in e.trechos:
        ls = linhas(pagina)
        if ini == 0:   # a página abre com a copa do começo do ano: o campeonato começa no título dele
            ini = next((i for i, l in enumerate(ls) if re.match(INICIO, l.strip())), 0)
        fim = fim if fim is not None else fim_padrao(ls, ini)
        trecho = [""] * ini + list(ls[ini:fim])   # mantém o número da linha da página
        j, t = rsssf_sul.ler(trecho, e.ano_inicio, e.ano_fim, fases=e.fases + FASES)
        tor, gru, velha = _torneios(ls, ini, fim, e.fases + FASES)
        if e.ano_inicio not in ANOS_TORNEIOS:
            tor = {}
        for x in j:
            x.texto = f"{pagina}:{x.linha}"
            _vitoria_dada(x)
            base = "" if velha.get(x.linha) else x.fase
            if e.ano_inicio >= 2002 and x.grupo and not base:   # grupo sem fase é dos quadrangulares (abaixo), também no torneio
                base = "Quadrangulares semifinais"
            x.fase = _fase(base, tor.get(x.linha, ""))
            if not x.grupo and gru.get(x.linha) and x.fase in ("Intermedio", "Clasificatorio", ""):
                x.grupo = gru[x.linha]
        for x in t:
            x.fase = _fase("" if velha.get(x.linha) else x.fase, tor.get(x.linha, ""))
            x.grupo = x.grupo or (gru.get(x.linha, "") if x.fase in ("Intermedio",) else "")
        jogos += j
        tabelas += t
    for pagina, ini, fim in e.tabelas:   # página que só tem a tabela final
        ls = linhas(pagina)
        tabelas += rsssf_sul.ler([""] * ini + list(ls[ini:fim]), e.ano_inicio, e.ano_fim, fases=e.fases + FASES)[1]
    if e.sem_jogos and not tabelas:   # sem tabela completa: a parcial (posição e pontos), quando há
        if (t := tabela_parcial(e.ano_inicio)) is not None:
            tabelas.append(t)
    if e.ano_inicio >= 2002:   # de 2002 em diante a liga não tem grupos: jogo ou tabela com grupo e sem fase é dos quadrangulares
        for x in [*jogos, *tabelas]:
            if x.grupo and not x.fase:
                x.fase = "Quadrangulares semifinais"
    if externos:   # a ESPN também traz os mata-matas que a página tem: dela, só os jogos de antes do primeiro da página
        corte = min((x.data for x in jogos if x.data), default="9999")
        jogos = [x for x in externos if x.data < corte] + jogos
    return jogos, tabelas


def _lista() -> list[tuple[str, str, str]]:
    """parachamp.html: [(temporada, campeão, vice)]. "2008 Libertad (Apertura) Nacional" -> "2008 Apertura"."""
    saida = []
    for l in linhas("parachamp"):
        m = re.match(r"^(\d{4})\s+(\S.*?)\s*(?:\((Apertura|Clausura)\)\s+|\s{2,})(\S.*?)\s*$", l)
        if not m or re.search(r"no championship|not held", l, re.I):
            continue
        temp = f"{m.group(1)} {m.group(3)}" if m.group(3) else m.group(1)
        saida.append((temp, m.group(2).strip(), m.group(4).strip()))
    return saida


def campeoes() -> dict[str, str]:
    return {t: c for t, c, _ in _lista()}


def vices() -> dict[str, str]:
    """Vice(s) de cada temporada como na página ("River Plate and Sol de América" = dois vices empatados)."""
    return {t: v for t, _, v in _lista()}


def secao_do_ano(ano: int) -> tuple[str, int, int] | None:
    """(página, início, fim) da seção do ano em parahist.html (1906-1959) ou da página do ano."""
    ls = linhas("parahist")
    ini = next((i for i, l in enumerate(ls) if l.strip() == str(ano)), None)
    if ini is not None:
        fim = next((i for i in range(ini + 1, len(ls)) if re.fullmatch(r"\d{4}", ls[i].strip())), len(ls))
        return "parahist", ini, fim
    pg = f"para{ano % 100:02d}"
    return (pg, 0, len(linhas(pg))) if (PASTA / f"{pg}.html").exists() else None


# PY-003: aceita texto depois dos pontos ("Playoff", "Relegated", "[inferred]") e a linha do clube empatado, sem número
# (" 1.Olimpia  15" / "   Cerro Porteño  15"), que herda a posição de cima
_PARCIAL = re.compile(r"^\s*(\d{1,2}|l)\s*\.\s*([^\d\s].*?)\s{2,}(\d{1,3})(?:\s*pts?)?(?:\s+(?:\[.*\]|\(.*\)|[A-Za-z].*))?\s*$", re.I)
_PARCIAL_EMPATE = re.compile(r"^\s{2,}()([^\d\s\[(].*?)\s{2,}(\d{1,3})(?:\s*pts?)?(?:\s+(?:\[.*\]|\(.*\)|[A-Za-z].*))?\s*$", re.I)


def tabela_parcial(ano: int) -> rsssf_sul.Tabela | None:
    """Tabela só com posição e pontos ("Final Table:" / "Top Final Table:" da seção do ano). Havendo mais de uma, vale a que
    vem depois de um título com "Final"; senão, a última."""
    sec = secao_do_ano(ano)
    if not sec:
        return None
    pg, ini, fim = sec
    ls = linhas(pg)
    tabelas: list[tuple[bool, rsssf_sul.Tabela]] = []
    atual, final_antes, titulo_final = None, False, False
    for i in range(ini, fim):
        s = ls[i].strip()
        m = _PARCIAL.match(ls[i]) or (_PARCIAL_EMPATE.match(ls[i]) if atual is not None else None)
        if m and not rsssf_sul._jogo(ls[i]):
            if atual is None:
                atual = rsssf_sul.Tabela(i, pg, "")   # secao = página da tabela parcial (vai para a fonte)
                tabelas.append((titulo_final, atual))
            pos = (atual.linhas[-1]["pos"] if not m.group(1) else 1 if m.group(1).lower() == "l" else int(m.group(1)))
            # nome até o primeiro número; o último número são os pontos, os anteriores (quando há) J V E D GP GC
            nome = re.match(r"^([^\d]+?)\s*(\d.*)?$", m.group(2) + " " + m.group(3))
            nums = [int(x) for x in re.findall(r"\d+", nome.group(2) or "")]
            campos = dict(zip(("j", "v", "e", "d", "gp", "gc"), nums[:-1]))
            linha = {"pos": pos, "nome": nome.group(1).strip(), "cidade": None, "j": None, "v": None, "e": None, "d": None,
                     "gp": None, "gc": None, "pts": nums[-1], "obs": "parcial"}
            linha.update(campos)
            atual.linhas.append(linha)
            continue
        if s:
            atual = None
            titulo_final = bool(re.search(r"final", s, re.I)) and len(s) < 50
    if not tabelas:
        return None
    finais = [t for f, t in tabelas if f]
    return (finais or [t for _, t in tabelas])[-1]


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
        f = PASTA_DADOS / "espn" / f"par1_{a}.json"
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
