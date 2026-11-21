"""Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/uru-1/rsssf/) com o leitor comum (rsssf_sul) e,
nos anos sem página, a Wikipédia em espanhol (wikipedia_jogos.py).

Fases: o torneio em vigor na página (título "Torneo Apertura", "Torneo Intermedio", "Clausura", "Clasificatorio 2004",
"Torneo Uruguay Especial") vira a fase dos jogos; o desempate ou a final de um torneio leva o nome dele ("Final do
Apertura", "Final do Intermedio"). Títulos de tabela anual e das finais do campeonato ("Aggregate Table", "Tabla Anual",
"Championship Playoff") encerram o torneio: dali em diante as fases são as do campeonato (semifinal, final).

Uso como biblioteca: ler(edicao) -> (jogos, tabelas); campeoes() -> {temporada: campeão como na página}.
Uso direto: python coleta/uru-1/ler_rsssf.py [temporada ...]   (resumo de jogos e tabelas por edição)
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
import wikipedia_jogos  # noqa: E402
from edicoes import EDICOES, FIM_PADRAO, PASTA_DADOS, Edicao  # noqa: E402

PASTA = PASTA_DADOS / "rsssf"

# fases reconhecidas pelo título (a primeira é a fase de partida); vale para todas as edições
FASES = [
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

# torneio do ano: abre com o título; os títulos de FECHA encerram (fase do campeonato daí em diante)
TORNEIOS = [
    (r"^(Torneo )?Apertura(\s+\d{4}(/\d{2})?)?\s*$", "Apertura"),
    (r"^(Torneo )?Intermedio(\s+\d{4}(/\d{2})?)?\s*$", "Intermedio"),
    (r"^(Torneo )?Clausura(\s+\d{4}(/\d{2})?)?\s*$", "Clausura"),
    (r"^Clasificatorio \d{4}", "Clasificatorio"),
]
FECHA = r"^(Aggregate Table|Overall Table|Annual Table|Tabla Anual|Championship (Playoff|Final|Semifinals?)|Final de la Liga|" \
        r"Relegation (Playoff|Table)|Final \(Aggregate|Group A \(Grupo)"


# páginas de colunas fixas: (início da coluna do visitante, início da coluna do placar)
COLUNAS = {"uru95": (18, 38)}


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
    for pagina, ini, fim in e.trechos:
        ls = linhas(pagina)
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
    return jogos, tabelas


def campeoes() -> dict[str, str]:
    """uruchamp.html: temporada do pacote ("1923 FUF", "2005/06", "2020") -> campeão como na página."""
    saida: dict[str, str] = {}
    liga = ""
    for l in linhas("uruchamp"):
        s = l.strip()
        if s.startswith("Federaci"):
            liga = "FUF"
        elif s.startswith(("Asociaci", "Consejo", "Liga Uruguaya", "Uruguay Association")):
            liga = "AUF"
        if s.startswith("Amateur Titles"):        # contagem de títulos entre as duas listas: pula até a era profissional
            liga = "pula"
        elif s.startswith("The Professional Era"):
            liga = "AUF"
        if s.startswith(("Professional Titles", "Total Championships")):
            break
        if liga == "pula":
            continue
        m = re.match(r"^(\d{4}(?:/\d{2})?)\s+(\S.*?)(?:\s{2,}\(.*)?$", s)
        if not m or re.search(r"not (played|finished|completed)", m.group(2)):
            continue
        temp = m.group(1)
        if temp in ("1923", "1924"):
            temp = f"{temp} {liga}"
        elif temp == "2020/21":
            temp = "2020"
        saida.setdefault(temp, re.sub(r"\s*\(.*\)\s*$", "", m.group(2)).strip())
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
