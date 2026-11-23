"""Lê os jogos de cada edição nas páginas da RSSSF (data/coleta/per-1/rsssf/) com o leitor comum (rsssf_sul). Nos anos sem
jogos, lê só a tabela: a completa, quando a página a traz, ou a parcial (posição e pontos: "1.Cerro Porteño   28"), da seção
do ano em parahist.html ou da página do ano.

Uso como biblioteca: ler(edicao) -> (jogos, tabelas); campeoes() e vices() -> {temporada: nome como na página}.
Uso direto: python coleta/per-1/ler_rsssf.py [temporada ...]   (resumo de jogos e tabelas por edição)
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
from edicoes import EDICOES, FIM_PADRAO, PASTA_DADOS, Edicao, secao_hist  # noqa: E402
import wikipedia_jogos  # noqa: E402

PASTA = PASTA_DADOS / "rsssf"

# fases reconhecidas pelo título (a primeira é a fase de partida); vale para todas as edições
FASES = [
    (r"^(Relegation (Group|Round|Liguilla)|Liguilla (de |del |por el )?(No )?Descenso|Final Table \(No descenso\))",
     "Grupo do rebaixamento"),
    (r"^(Second Stage( \(Liguillas?\)| - Liguillas)?|Liguillas)$", "Liguillas"),
    (r"^(Championship (Group|Round|Liguilla)|Liguilla Final(?! Regional)|Final Table \(Liguilla Final\)|Final (Group|Round|Stage)\b|"
     r"Hexagonal|Octogonal|Cuadrangular|Liguilla \[in Lima\]|Liguilla$|"
     r"Descentralised Final)", "Fase final"),   # PE-012: a "Descentralised Final" de 1988 é uma liguilla de 6
    (r"^(First Stage|First Phase|Regular (Season|Stage)|Group Stage)", ""),
    (r"^(Round of 16|Octavos de final)\b", "Oitavas de final"),
    (r"^(Quarter[- ]?finals?|Cuartos de final)\b", "Quartas de final"),
    (r"^(Regional Tournament\s*[-–]\s*)?(Semi[- ]?finals?|Championship Semifinals?)\b", "Semifinal"),
    (r"^Playoffs?$", "Semifinal"),   # "Playoffs" abre as semifinais (2015 em diante)
    (r"^(Regional Tournament\s*[-–]\s*Final|Final(?!\s*(Table|Tournament|Group|Standing|phase|stage|Aggregate|Tables))|"
     r"Championship (Final|Match)|National (Final|Championship Playoff)|Finals$)", "Final"),
    (r"^((Apertura|Clausura) Playoff|Championship [Pp]layoffs?|Definition Playoff|First place playoff|"
     r"Regional Championship (playoff|Match)|Playoff Regional Final|Extra match|Desempate|"
     r"(Apertura|Clausura) (Championship Playoff|Final)|Phase \d Final)", "Desempate do título"),
    (r"^(Second [Pp]lace [Pp]layoffs?|National Second Place Playoffs|Third Place)", "Desempate do 2º lugar"),
    (r"^(Relegation [Pp]lay-?offs?)", "Desempate do rebaixamento"),
    (r"^(Repechaje|Repesca|Qualification Playoffs)", "Repechaje"),
]

# título que abre o campeonato numa página que começa por outra competição
INICIO = r"^NUNCA$"

# torneios dentro da edição anual: a fase dos jogos vira o torneio ("Apertura"; "Final do Regional")
TORNEIOS: list[tuple[str, str]] = [
    (r"^(Regional (Tournament|\d{4})|Regional I( Tournament.*)?|Liguilla Final Regional I)$", "Regional"),
    (r"^(Regional II|Liguilla Final Regional II)$", "Regional II"),
    (r"^(Torneo |First Stage \()?Apertura( Tournament| \d{4})?\)?$", "Apertura"),
    (r"^(Torneo |Second Stage \()?Clausura( Tournament| \d{4})?\)?$", "Clausura"),
    (r"^Torneo de Verano$", "Torneo de Verano"),
    (r"^Phase 1$", "Fase 1"),
    (r"^Phase 2$", "Fase 2"),
]
# título que volta ao campeonato (fim do torneio em vigor)
FECHA = (r"^(Decentrali[sz]ed Tournament|Descentrali[sz]ed Tournament|Descentralizado Tournament|Campeonato Descentralizado|"
         r"Aggregate|Agreggate|Combined Table|Overall Table|Tabla Anual|Playoffs$|Championship (Playoff|Final|Match)|"
         r"National (Final|Championship)|Finals$|Final$|Descentralised Final|Liguillas$|Second Stage)")


ZONAS = {"Metropolitan": "Metropolitana", "Northern": "Norte", "North": "Norte", "Central": "Centro", "Centre": "Centro",
         "Southern": "Sul", "South": "Sul", "Oriental": "Oriente", "Eastern": "Oriente"}

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
    if pagina in ("peru31", "peru32", "peru33", "peru34"):   # "... - 33 - 5.75 - 38.75": pontos, bônus da liga de reservas e total
        ls = [re.sub(r"(\s[-–]\s*\d{1,2})\s*[-–]\s*\d{1,2}(?:\.\d+)?\s*[-–]\s*\d{1,2}(?:\.\d+)?(?=\s*(?:\[|$))", r"\1", l) for l in ls]
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
            ult_fase, grupo = i, ""   # fase nova: o grupo da fase anterior não vale mais
        if m := re.match(r"^(?:Grupo|Group|Serie|Liguilla)\s+[“\"]?([A-Z])\b(?!\s*\()", s):
            grupo = m.group(1)
        elif m := re.match(r"^(Metropolitan|Northern|North|Central|Centre|Southern|South|Oriental|Eastern)\s+(Zone|Group)\b", s):
            grupo = ZONAS[m.group(1)] + (f" {m2.group(1)}" if (m2 := re.search(r"Group ([AB])$", s)) else "")
        por_linha[i], grupos[i], velha[i] = torneio, grupo, ult_fase < ini_t
    return por_linha, grupos, velha


def _vitoria_dada(x: rsssf_sul.Jogo) -> None:
    """"[awarded 1-1 win to Progreso because ...; goals stood]": pontos para um lado, os gols do campo contam na tabela.
    Vira W.O. (wo_m/wo_v) com o placar de campo, como a tabela conta."""
    if x.gm_of is None and x.especial == "awd" and (m := re.match(r"^\s*(\d{1,2})\s*-\s*(\d{1,2}) to \w", x.nota)):
        x.gm_of, x.gv_of = int(m.group(1)), int(m.group(2))   # "Sud América Awd Wanderers [0-2 to Wanderers]"
        return
    if x.gm_of is None and x.especial == "awd" and (m := re.match(r"^\s*(?:\(\*+\))?\s*\[?\s*(\d{1,2})\s*-\s*(\d{1,2})\s*\]", x.nota)):
        x.gm_of, x.gv_of = int(m.group(1)), int(m.group(2))   # "Cusco FC  awd Sport Huancayo  (*)[0-3][Estádio]"
        return
    if re.search(r"award(ed)? of (a )?win to .{2,40}? annulled", x.nota, re.I):   # a decisão caiu: vale o placar de campo
        x.especial = "" if x.gm is not None else x.especial
        return
    m = re.search(r"(?:awarded (?:(\d{1,2})\s*-\s*(\d{1,2}) )?(?:a )?win to|win awarded to)\s+(.+?)"
                  r"(?:\s+(?:as|because|since|for|after|due|with)\b|\s*\(|[;,.\]]|$)", x.nota, re.I)
    # "[Universitario were declared winners]", "[... Alianza Lima won 3 pts, ...]" (páginas peruanas dos anos 1930)
    m = m or re.search(r"(?:^|[,;]\s*|but\s+)()()([A-Z][\w .'-]+?)\s+(?:were|was) declared winners?", x.nota) or \
        re.search(r"(?:^|[,;]\s*)()()([A-Z][\w .'-]+?)\s+won \d\s*pts?", x.nota)
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
    do = "da" if torneio.startswith("Fase") else "do"
    if base in ("Final", "Desempate do título"):
        return f"Final {do} {torneio}"
    if base == "Semifinal":
        return f"Semifinal {do} {torneio}"
    return base


# fases em que o título "Group A" / "Northern Zone" marca o grupo dos jogos e das tabelas que vêm depois
COM_GRUPO = ("", "Regional", "Regional II", "Liguillas", "Torneo de Verano", "Fase 1", "Fase 2", "Fase final", "Segunda fase")


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
        tor, gru, velha = _torneios(ls, ini, fim)
        for x in j:
            x.texto = f"{pagina}:{x.linha}"
            _vitoria_dada(x)
            x.fase = _fase("" if velha.get(x.linha) else x.fase, tor.get(x.linha, ""))
            if not x.grupo and gru.get(x.linha) and x.fase in COM_GRUPO:
                x.grupo = gru[x.linha]
        for x in t:
            x.fase = _fase("" if velha.get(x.linha) else x.fase, tor.get(x.linha, ""))
            x.grupo = x.grupo or (gru.get(x.linha, "") if x.fase in COM_GRUPO else "")
        jogos += j
        tabelas += t
    for pagina, ini, fim in e.tabelas:   # página que só tem a tabela final
        ls = linhas(pagina)
        tabelas += rsssf_sul.ler([""] * ini + list(ls[ini:fim]), e.ano_inicio, e.ano_fim, fases=e.fases + FASES)[1]
    if e.sem_jogos and not tabelas:   # sem tabela completa: a parcial (posição e pontos), quando há
        if (t := tabela_parcial(e.ano_inicio)) is not None:
            tabelas.append(t)
    if e.wiki is not None:
        jogos += wikipedia_jogos.jogos(e.wiki)
    if externos:   # a ESPN também traz os mata-matas que a página tem: dela, só os jogos de antes do primeiro da página
        corte = min((x.data for x in jogos if x.data), default="9999")
        jogos = [x for x in externos if x.data < corte] + jogos
    return jogos, tabelas


def _lista() -> list[tuple[str, str, str]]:
    """peruchamp.html: [(temporada, campeão, vice)]. Vice: o 2º da tabela final de peruhist.html, quando há (a lista de
    campeões não traz o vice)."""
    saida = []
    for l in linhas("peruchamp"):
        m = re.match(r"^(\d{4})\s+(\S.*?)\s*$", l)
        if not m or re.search(r"no official|not held", l, re.I) or not 1900 < int(m.group(1)) < 2100:
            continue
        saida.append((m.group(1), m.group(2).strip(), ""))
    return saida


def campeoes() -> dict[str, str]:
    return {t: c for t, c, _ in _lista()}


def vices() -> dict[str, str]:
    """(A lista de campeões do Peru não traz o vice.)"""
    return {}


def secao_do_ano(ano: int) -> tuple[str, int, int] | None:
    """(página, início, fim) da seção do ano em peruhist.html."""
    return secao_hist(ano)


def tabela_parcial(ano: int) -> rsssf_sul.Tabela | None:
    """(O Peru não tem tabelas só com posição e pontos: as de peruhist.html são completas.)"""
    return None


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
        f = PASTA_DADOS / "espn" / f"per1_{a}.json"
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


def ranking_liga(ano: int) -> list[tuple[int | None, str]]:
    """Liga Peruana (1912-1921, D-06 A): a ordem da 1ª divisão na página do ano ("Final Ranking:" / "Top Final Ranking:",
    " 1.Sport Alianza") e os outros participantes ("Participants (8):", "Other participants (12, ...)"), sem posição.
    [(posição ou None, nome como na página)]; para no primeiro título de outra divisão, rodada ou nota."""
    saida: list[tuple[int | None, str]] = []
    lendo = False
    for l in linhas(f"peru{ano}")[12:]:
        s = l.strip()
        if re.match(r"^Segunda|^Second", s):   # a 2ª divisão da mesma página fica de fora
            break
        if re.match(r"^(Top )?Final Ranking|^(Other )?[Pp]articipants|^Reported Final Standings", s):
            lendo = True
            continue
        if not s:
            continue
        if re.match(r"^(Round|NB|Promoted|Relegated|Segunda|Second|Division|list of|\d{4}$|\[)", s):
            lendo = False
            continue
        if lendo:   # (1912: " 1.Lima Cricket   12", " -.Escuela Militar": o número de pontos sai; "-." é sem posição)
            m = re.match(r"^(?:(\d+|-)\.)?\s*(.+?)(?:\s{2,}\d[\d\s-]*)?\s*$", s)
            saida.append((int(m.group(1)) if m.group(1) and m.group(1) != "-" else None, m.group(2)))
    # a ordem vem antes dos participantes sem posição; cada clube uma vez (1912 lista os participantes e depois a tabela)
    from clubes_per import clube
    vistos, ordem = set(), []
    for pos, n in sorted(saida, key=lambda x: (x[0] is None, x[0] or 0)):
        c = clube(n, ano) or n
        if c not in vistos:
            vistos.add(c)
            ordem.append((pos, n))
    return ordem
