"""Lê os jogos de cada edição nas páginas da RSSSF (data/coleta/ecu-1/rsssf/) com o leitor comum (rsssf_sul) e, de 1960 a
1974, as tabelas de confrontos ("Cross-Table": mandante na linha, visitante na coluna) com confrontos(). Em 2011, 2012 e
2025 a página só traz as tabelas e as finais: os outros jogos vêm da ESPN.

Uso como biblioteca: ler(edicao) -> (jogos, tabelas); campeoes() e vices() -> {temporada: nome como na página}.
Uso direto: python coleta/ecu-1/ler_rsssf.py [temporada ...]   (resumo de jogos e tabelas por edição)
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timedelta
from functools import lru_cache
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
sys.path.insert(0, str(AQUI))
import rsssf_sul  # noqa: E402

from edicoes import EDICOES, FIM_PADRAO, PASTA_DADOS, Edicao  # noqa: E402

PASTA = PASTA_DADOS / "rsssf"

# fases reconhecidas pelo título (a primeira que casa vale); vale para todas as edições
# fim de título de fase de liga: a linha inteira (a nota que quebra a linha, "...qualified for" / "Octogonal Final.", não vale)
_FIM = r"\s*:?\s*(\[[^\]]*\])?$"
FASES = [
    (r"^(Relegation (Group|Round|Liguilla|Table)|Liguilla (de |del |por el )?(No )?Descenso|Hexagonal (por|para) el no descenso"
     r"( de categor[ií]a)?|Cuadrangular del No-Descenso|Liguilla No Descenso)" + _FIM, "Grupo do rebaixamento"),
    (r"^(Liguillas|Liguilla Pre Libertadores|Cuadrangular (Libertadores|Pre-Conmebol)|Hexagonal para Copa Libertadores( de America)?|"
     r"Liguilla [ABC] \(.*\))" + _FIM, "Liguillas"),
    (r"^Hexagonal 2" + _FIM, "Hexagonal 2"),
    (r"^(Championship (Group|Round|Liguilla)|Liguilla Final|Final Liguilla|Final (Group|Round|Stage)|Hexagonal Final|Hexagonal 1|"
     r"Cuadrangular [Ff]inal|Octogonal Final|Liguilla)" + _FIM, "Fase final"),
    (r"^(First Stage|First Phase|Phase 1|Regular (Season|Stage)|Primera Etapa)( \((First Stage|Torneo Apertura|Apertura)\))?" + _FIM, ""),
    (r"^(Second (Stage|Phase)|Segunda Etapa|Octogonal)( \(Second Stage\))?" + _FIM, "Segunda fase"),
    (r"^((Third|Thirth) (Stage|Phase)|Tercera Etapa)( \(Third Stage\))?" + _FIM, "Terceira fase"),
    (r"^(Round of 16|Octavos de final|1/8 Finals)\b", "Oitavas de final"),
    (r"^(Quarter[- ]?finals?|Cuartos de final)\b", "Quartas de final"),
    (r"^(Semi[- ]?finals?)\b", "Semifinal"),
    (r"^(Final(?!\s*(Table|Tournament|Group|Standing|phase|stage|Aggregate|Tables|Round|Liguilla))|Championship (Final|Match)|"
     r"Finals$)", "Final"),
    (r"^Definition of (the )?champions?" + _FIM, "Final"),   # 1980: melhor de três pelo título, com "Round 1/2/3"
    (r"^Extra match for definition of runners-up", "Desempate do 2º lugar"),
    (r"^Extra seri(e|es) for relegation", "Desempate do rebaixamento"),
    # "Championship Playoff" (2020-2024): a final entre os vencedores das duas etapas, como o "Championship Final" de 2014
    (r"^Championship [Pp]layoffs?" + _FIM, "Final"),
    (r"^(Playoff$|First place playoff|Extra match|Desempate)", "Desempate do título"),
    (r"^Definition of (runners?[- ]up|third place)" + _FIM, "Desempate do 2º lugar"),
    # EC-003: disputa de 3º e de 4º lugar (2009-2012) é fase própria, não desempate do 2º lugar
    (r"^Third Place (Playoffs?|Matches)", "Disputa do 3º lugar"),
    (r"^Fourth Place (Playoffs?|Matches)", "Disputa do 4º lugar"),
    (r"^(Playoff (for|to decide) [Ss]econd [Pp]lace|Second [Pp]lace (Playoffs?|Matches))", "Desempate do 2º lugar"),
    (r"^(Playoff Descenso|Relegation [Pp]lay-?offs?)", "Desempate do rebaixamento"),
]

# título que abre o campeonato numa página que começa por outra competição
INICIO = r"^NUNCA$"

# torneios dentro da edição anual: a fase dos jogos vira o torneio ("Apertura"; "Final do Apertura")
TORNEIOS: list[tuple[str, str]] = [
    (r"^(Torneo |First Stage \(Torneo |First Stage \()?Apertura\)?$", "Apertura"),
    (r"^(Torneo |Second Stage \(Torneo |Second Stage \()?Clausura\)?$", "Clausura"),
    (r"^(Torneo |Second Stage \(Torneo |Second Stage \()?Finalizaci[oó]n\)?$", "Finalización"),
]
# título que volta ao campeonato (fim do torneio em vigor)
# (vale a linha inteira: ler_rsssf._torneios junta _FIM)
FECHA = (r"^(Aggregate( Table)?|Agreggate( Table)?|Combined Table|Overall Table|Tabla Anual|Playoffs?|Championship (Playoff|Final|Match)|"
         r"Finals?|Liguilla Final|Final Liguilla|Hexagonal Final|Cuadrangular final|Liguilla|Second Stage|Playoff Stage|"
         r"Relegation Group|Relegation Table|Hexagonal (por|para) .*|Liguilla de no descenso)")

# grupos marcados por título ("Liguilla B (5,7,9,11 of first stage)", "Group A")
_GRUPO = r"^(?:Grupo|Group|Liguilla)\s+[“\"]?([A-Z])\b(?!\s*\()"

# páginas de colunas fixas: (início da coluna do visitante, início da coluna do placar)
COLUNAS: dict[str, tuple[int, int]] = {}


_CP437 = str.maketrans({"‚": "é", "¢": "ó", "¡": "í", "£": "ú", "¤": "ñ", "": "é", "¢": "ó"})


@lru_cache(maxsize=None)
def linhas(pagina: str) -> tuple[str, ...]:
    """Texto puro da página, com os erros de digitação corrigidos (explicacoes.CONSERTA_TEXTO, cada um com o motivo)."""
    from explicacoes import CONSERTA_TEXTO
    # travessão no placar ("2–0") em parte das páginas: vira hífen
    ls = [l.replace("–", "-").replace("—", "-") for l in rsssf_sul.texto(PASTA / f"{pagina}.html")]
    # páginas com acentos da página de código 437 ("Am‚rica", "Cat¢lica"): voltam ao acento
    ls = [l.translate(_CP437) for l in ls]
    if pagina == "ecua96":   # "LDU Quito-Barcelona 0-1": hífen entre os clubes; vira "LDU Quito  0-1  Barcelona"
        ls = [re.sub(r"^([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ. ]*?)-([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ. ]*?)\s+(\d{1,2}-\d{1,2})[,.]?(\s*\[.*)?\s*$",
                      r"\1  \3  \2\4", l) for l in ls]
    if pagina == "ecua98":   # empate decidido nos pênaltis: "5/1" = 5 vencidos (2 pontos) e 1 perdido (1 ponto); vira 6 empates
        ls = [re.sub(r"(?<=\s)(\d{1,2})/(\d{1,2})(?=\s)", lambda m: str(int(m.group(1)) + int(m.group(2))), l)
              if re.match(r"^\s*\d{1,2}\.\S", l) else l for l in ls]
    if pagina in COLUNAS:
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
            viu_jogo = bool(rsssf_sul._jogo(ls[i])) or bool(_CELULAS.search(ls[i]))
            continue
        if re.match(FIM_PADRAO, s, re.I):
            return i
    return len(ls)


_CELULA = r"(?:xxx|\d{1,2}[-*]\d{1,2}|---)"
_CELULAS = re.compile(rf"^(?P<nome>\S.*?|)\s+(?P<cel>{_CELULA}(?:\s+{_CELULA}){{1,}})\s*$")


def confrontos(ls: list[str], ini: int, fim: int) -> tuple[list[tuple[int, str, str, int, int, bool]], set[int]]:
    """Tabelas de confrontos do trecho: [(linha, mandante, visitante, gm, gv, dado)] e as linhas que fazem parte delas.
    Cabeçalho "Cross-Table", linha de siglas e uma linha por clube (mandante) com uma célula por adversário, na ordem das
    linhas (a diagonal é "xxx"). Linha sem nome: segundo turno do clube de cima, em casa de novo. "0*2": placar dado fora
    de campo (dado=True)."""
    jogos, usadas = [], set()
    i = ini
    while i < fim:
        if not re.match(r"^\s*Cross-?Table", ls[i], re.I):
            i += 1
            continue
        usadas.add(i)
        k = i + 1
        while k < fim and not ls[k].strip():
            k += 1
        usadas.add(k)   # linha das siglas
        k += 1
        linhas_m: list[tuple[int, str, list[str]]] = []
        while k < fim and (m := _CELULAS.match(ls[k].replace("\t", "    "))):
            nome = m.group("nome").strip() or (linhas_m[-1][1] if linhas_m else "")
            linhas_m.append((k, nome, m.group("cel").split()))
            usadas.add(k)
            k += 1
        clubes = list(dict.fromkeys(n for _, n, _ in linhas_m))
        for linha, casa, cels in linhas_m:
            assert len(cels) == len(clubes), f"tabela de confrontos com {len(cels)} colunas e {len(clubes)} clubes: linha {linha}"
            for fora, c in zip(clubes, cels):
                if (mm := re.fullmatch(r"(\d{1,2})([-*])(\d{1,2})", c)) and fora != casa:
                    jogos.append((linha, casa, fora, int(mm.group(1)), int(mm.group(3)), mm.group(2) == "*"))
        i = k
    return jogos, usadas


def _torneios(ls: tuple[str, ...], ini: int, fim: int, fases: list[tuple[str, str]]
              ) -> tuple[dict[int, str], dict[int, str], dict[int, bool], dict[int, str]]:
    """Por linha: o torneio em vigor ("" = campeonato), o grupo marcado em título, se a fase de mata-mata lida antes ficou
    velha (título de fase anterior ao começo do torneio em vigor) e a fase do último título."""
    torneio, grupo, fase = "", "", ""
    ini_t, ult_fase = -1, -1
    por_linha, grupos, velha, ult = {}, {}, {}, {}
    for i in range(ini, fim):
        s = ls[i].strip()
        if re.match(FECHA + _FIM, s, re.I):   # a linha inteira (não a nota "...qualify for / Hexagonal Final.")
            torneio, grupo, ini_t = "", "", i
        else:
            for rx, nome in TORNEIOS:
                if re.match(rx, s, re.I):
                    torneio, grupo, ini_t = nome, "", i
                    break
        if (f := next((nome for rx, nome in fases if re.search(rx, s, re.I)), None)) is not None:
            ult_fase, grupo, fase = i, "", f   # fase nova: o grupo da fase anterior não vale mais
        if m := re.match(_GRUPO, s):
            grupo = m.group(1)
        por_linha[i], grupos[i], velha[i], ult[i] = torneio, grupo, ult_fase < ini_t, fase
    return por_linha, grupos, velha, ult


def _vitoria_dada(x: rsssf_sul.Jogo) -> None:
    """"[awarded 3-0 win to Barcelona because ...]": pontos para um lado. Vira W.O. (wo_m/wo_v) com o placar de campo, como a
    tabela conta."""
    if x.gm_of is None and x.especial == "awd" and (m := re.match(r"^\s*(\d{1,2})\s*-\s*(\d{1,2}) to \w", x.nota)):
        x.gm_of, x.gv_of = int(m.group(1)), int(m.group(2))
        return
    if x.gm_of is None and x.especial == "awd" and (m := re.match(r"^\s*(?:\(\*+\))?\s*\[?\s*(\d{1,2})\s*-\s*(\d{1,2})\s*\]", x.nota)):
        x.gm_of, x.gv_of = int(m.group(1)), int(m.group(2))
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
    if base in ("", "Fase final", "Segunda fase"):
        return torneio
    if base in ("Final", "Desempate do título"):
        return f"Final do {torneio}"
    if base == "Semifinal":
        return f"Semifinal do {torneio}"
    if base in ("Liguillas", "Grupo do rebaixamento"):   # 1998: quadrangulares do Apertura e do Clausura
        return f"{base} do {torneio}"
    return base


# fases em que o título "Liguilla B" / "Group A" marca o grupo dos jogos e das tabelas que vêm depois
COM_GRUPO = ("", "Apertura", "Clausura", "Finalización", "Liguillas", "Fase final", "Segunda fase", "Terceira fase",
             "Grupo do rebaixamento")


def ler(e: Edicao) -> tuple[list[rsssf_sul.Jogo], list[rsssf_sul.Tabela]]:
    jogos, tabelas = [], []
    externos = espn_jogos(*e.espn) if e.espn is not None else []
    for pagina, ini, fim in e.trechos:
        ls = linhas(pagina)
        if ini == 0:   # a página abre com outra competição: o campeonato começa no título dele
            ini = next((i for i, l in enumerate(ls) if re.match(INICIO, l.strip())), 0)
        fim = fim if fim is not None else fim_padrao(ls, ini)
        cruz, usadas = confrontos(list(ls), ini, fim)
        trecho = [""] * ini + ["" if i in usadas else l for i, l in enumerate(ls[ini:fim], ini)]   # mantém o número da linha
        j, t = rsssf_sul.ler(trecho, e.ano_inicio, e.ano_fim, fases=e.fases + FASES)
        for linha, casa, fora, gm, gv, dado in cruz:   # fase e grupo: os da tabela que vem logo depois da tabela de confrontos
            tab = next((x for x in t if x.linha > linha), None)
            x = rsssf_sul.Jogo(linha, casa, fora, gm, gv, None, None, "", tab.fase if tab else "", tab.grupo if tab else "",
                               "", "", None, texto=ls[linha].strip())
            if dado:   # placar dado fora de campo; o de campo, quando a nota da página diz, entra em explicacoes.CORRIGE
                x.gm = x.gv = None
                x.gm_of, x.gv_of, x.especial = gm, gv, "awd"
            j.append(x)
        j.sort(key=lambda x: x.linha)
        tor, gru, velha, ult = _torneios(ls, ini, fim, e.fases + FASES)
        for x in j:
            x.texto = f"{pagina}:{x.linha}"
            _vitoria_dada(x)
            if not x.fase and ult.get(x.linha, "").startswith("Desempate"):
                x.fase = ult[x.linha]   # desempate com "Round 1", "Round 2": o leitor comum volta à fase de liga a cada rodada
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
    if externos:   # a ESPN também traz os jogos finais que a página tem: dela, só os jogos de antes do primeiro da página
        corte = min((x.data for x in jogos if x.data), default="9999")
        externos = [x for x in externos if x.data < corte]
        from clubes_ecu import clube
        for x in externos:
            for d0, f in e.espn_fases:
                if x.data >= d0 and f != "*":
                    x.fase = f
                elif x.data >= d0:   # a fase da tabela da página que tem os dois clubes (Hexagonal 1 e 2, rebaixamento)
                    dupla = {clube(x.mandante, e.ano_inicio), clube(x.visitante, e.ano_inicio)}
                    t = next((t for t in tabelas if t.fase and dupla <= {clube(r["nome"], e.ano_inicio) for r in t.linhas}), None)
                    x.fase = t.fase if t else x.fase
        jogos = externos + jogos
    return jogos, tabelas


def _lista() -> list[tuple[str, str, str]]:
    """ecuachamp.html: [(temporada, campeão, vice)]. "2005 Ap" e "2005 Fi" são o Apertura e o Clausura de 2005."""
    saida = []
    for l in linhas("ecuachamp"):
        m = re.match(r"^(\d{4})( Ap| Fi)?\s+(\S.*?)(?:\s{2,}(\S.*?))?\s*$", l)
        if not m or re.search(r"no championship", l, re.I) or not 1900 < int(m.group(1)) < 2026:
            continue
        t = m.group(1) + {" Ap": " Apertura", " Fi": " Clausura", None: ""}[m.group(2)]
        saida.append((t, m.group(3).strip(), (m.group(4) or "").strip()))
    return saida


def campeoes() -> dict[str, str]:
    return {t: c for t, c, _ in _lista()}


def vices() -> dict[str, str]:
    return {t: v for t, _, v in _lista() if v}


def secao_do_ano(ano: int) -> tuple[str, int, int] | None:
    """(Não usado: todas as edições têm página própria.)"""
    return None


def tabela_parcial(ano: int) -> rsssf_sul.Tabela | None:
    """(Não usado: as tabelas do Equador são completas.)"""
    return None


def espn_jogos(ini: str, fim: str) -> list[rsssf_sul.Jogo]:
    """Jogos encerrados da ESPN (liga ecu.1) entre as datas, no horário de Guayaquil e Quito (UTC-5) (texto "espn:<id>")."""
    saida = []
    for a in range(int(ini[:4]), int(fim[:4]) + 1):
        f = PASTA_DADOS / "espn" / f"ecu1_{a}.json"
        for g in json.loads(f.read_text(encoding="utf-8")) if f.exists() else []:
            d = (datetime.fromisoformat(g["data_hora"].replace("Z", "+00:00")) - timedelta(hours=5)).date().isoformat()
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
        print(f"{e.temporada:14s} {len(js):4d} jogos  {len(ts):2d} tabelas  fases {fases}")
