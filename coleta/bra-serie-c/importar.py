"""Junta as fontes da Série C e grava o pacote em data/coleta/bra-serie-c/pacote/ e o relatório em docs/coleta/bra-serie-c.md.

Fontes, na ordem em que entram:
- RSSSF Brasil (rsssf_c.py): base de jogos, fases, grupos, rodadas, datas e autores dos gols; as tabelas publicadas
  servem de conferência.
- ogol (baixar_ogol.py): calendário completo de todas as edições, com o código de cada clube (identidade). Confere
  o placar, completa os jogos que faltam na RSSSF e é a base de 2019 (a página da RSSSF parou na 1ª rodada).
- ESPN (liga bra.3), 2017 em diante: hora, estádio e cidade.
- Wikipédia: punições de pontos (adjust_points) e a lista de campeões (segunda fonte do campeão).

Placar diferente entre RSSSF e ogol: fica o que fecha com a tabela publicada pela RSSSF (os dois clubes);
sem tabela para decidir, fica o da RSSSF. Tudo fica registrado no relatório.

Uso: python coleta/bra-serie-c/importar.py [ano ...]     (sem ano: todas as edições; com ano, só confere e não grava)
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
import clubes_c  # noqa: E402
import datas_corrigidas  # noqa: E402
import gols as gols_rsssf  # noqa: E402
from observacao import penaltis_da_nota  # noqa: E402
import rsssf_c  # noqa: E402
import wiki  # noqa: E402
from edicoes import ANOS, NOME_OFICIAL, NOME_PADRAO, PACOTE, PASTA_DADOS, RELATORIO, SLUG  # noqa: E402
from rsssf_c import rsssf  # noqa: E402

wiki.PASTA = PASTA_DADOS / "wikipedia"
OGOL = PASTA_DADOS / "ogol"
ESPN = PASTA_DADOS / "espn"
FONTE_RSSSF = "https://rsssfbrasil.com/tablesae/br{ano}l3.htm"


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
    a, b = clubes_c.chave(a), clubes_c.chave(b)
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
CORRIGE_OGOL = {
    (1981, "3333"): ("2541", "o ogol liga o Matsubara de 1981 ao J. Malucelli (fundado em 1994); a RSSSF traz a SE Matsubara, de Cambará"),
    (2003, "3307"): ("3306", "o Ituiutaba EC de 2003 (hoje Boa Esporte) aparece no ogol em dois cadastros (revisão SC-012)"),
    (2002, "15723"): ("3500", "o Tubarão de 2002 é o Tubarão FC (1992-2005); o CA Tubarão do ogol foi fundado em 2005 (revisão CL-002)"),
    (1981, "43721"): ("238972", "Joaçaba EC (1977, extinto nos anos 1980); o Joaçaba AC é de 1997 e não é sucessor (revisão CL-012)"),
    (1981, "70071"): ("241325", "SE São Borja (1977); o EC São Borja é de 2009, outro clube (revisão CL-012)"),
    (2001, "15641"): ("89206", "Guarabira EC (1936, extinto em 2004); a AD Guarabira é outro clube (revisão CL-012)"),
    (2002, "237932"): ("3461", "São Gabriel FC (2000-2013), o mesmo da Copa do Brasil 2004; o EC São Gabriel é de 2013 (revisão CL-005)"),
    (2003, "41237"): ("3260", "Goiatuba EC (1970), o mesmo de hoje; a AA Goiatuba é de 2009 (revisão CL-006)"),
    (1997, "3373"): ("ec-operario-mt", "EC Operário (1996-2001), que substituiu o CEOV; não é o Operário FC Ltda de 2002 (revisão CL-007)"),
    (1988, "39060"): ("241324", "Lagarto EC (1955-1990); o Lagarto FC é de 2009 (revisão CL-008)"),
    (1990, "39060"): ("241324", "Lagarto EC (1955-1990); o Lagarto FC é de 2009 (revisão CL-008)"),
    (1988, "3161"): ("71868", "AA Cabofriense (1955); a AD Cabofriense é de 1997 (revisão CL-009)"),
    (1998, "3326"): ("115862", "EC Limoeiro (1942); a AD Limoeiro é de 2001 (revisão CL-011)"),
    (1995, "11647"): ("214025", "o Ariquemes de 1995 é a SE Ariquemes (1981); o Ariquemes FC do ogol foi fundado em 1996 (revisão CL-004)"),
}
# código de clube errado em jogos do ogol: código do jogo -> (código errado, código certo, motivo)
_G18 = "1988, 2ª fase, grupo 18: o ogol põe a Desportiva Ferroviária no lugar da Ferroviária-SP (revisão SC-008)"
CORRIGE_OGOL_JOGO: dict[str, tuple[str, str, str]] = {
    j: ("3224", "15766", _G18) for j in ("7437399", "7437402", "7437404", "7437405", "7437408", "7437410")}


def ler_ogol(ano: int) -> list[dict]:
    f = OGOL / f"serie_c_{ano}.json"
    js = json.loads(f.read_text(encoding="utf-8")) if f.exists() else []
    for o in js:
        for lado in ("mandante", "visitante"):
            if (ano, o.get(f"{lado}_id")) in CORRIGE_OGOL:
                o[f"{lado}_id"] = CORRIGE_OGOL[(ano, o[f"{lado}_id"])][0]
                o[f"{lado}_corrigido"] = True
            errado, certo, _m = CORRIGE_OGOL_JOGO.get(o["id"], (None, None, None))
            if errado and o.get(f"{lado}_id") == errado:
                o[f"{lado}_id"] = certo
                o[f"{lado}_corrigido"] = True
    return [o for o in js if o["id"] not in OGOL_IGNORAR]


def nomes_ogol(ano: int, og: list[dict]) -> dict[str, set[str]]:
    """Código do clube -> nomes que o ogol usa para ele (no calendário do ano e na ficha)."""
    fs = clubes_c.fichas()
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
_INTERCAP = ("3293", "o Intercap, de Paraíso do Tocantins, é o 'Paraíso' do ogol (mesmos jogos e placares)")
NOME_MANUAL: dict[tuple[int, str], tuple[str, str]] = {
    (1995, "Intercap"): _INTERCAP, (1995, "INTERCAP(TO)"): _INTERCAP, (1995, "Intercap(TO)"): _INTERCAP, (1995, "Intercap-TO"): _INTERCAP,
    (1995, "ARAGUAINENSE(TO)"): ("276477", "União Atlética Araguainense, como no ogol"),
    (1995, "Araguainense"): ("276477", "União Atlética Araguainense, como no ogol"),
    (1995, "OPERARIO(MT)"): ("36613", "o Operário de Várzea Grande de 1995 é o 'CEOV Operário' do ogol"),
    (1995, "Operário-MT"): ("36613", "o Operário de Várzea Grande de 1995 é o 'CEOV Operário' do ogol"),
    (1995, "Lousano Paulista(SP)"): ("3388", "Lousano Paulista era o nome do Paulista de Jundiaí em 1995"),
    (1995, "Roraima"): ("3440", "o 'Roraima' dos jogos é o 'ATL.RORAIMA' da tabela do grupo 21 (Atlético Roraima)"),
    **{(a, "Atl.Cajazeirense"): ("3130", "Atlético Cajazeirense é o 'Atlético-PB' (Cajazeiras) do ogol") for a in (2001, 2002, 2007)},
    (2003, "Ituiatuba"): ("3306", "erro de digitação da RSSSF: Ituiutaba (hoje Boa Esporte)"),
    (1999, "Serra (SE)"): ("3474", "erro de digitação da RSSSF: é o Serra (ES), representante do Espírito Santo"),
    (2002, "São Gabriel"): ("3461", "São Gabriel FC (revisão CL-005)"),
    (1981, "Joaçaba"): ("238972", "Joaçaba EC (revisão CL-012)"),
    (1981, "São Borja"): ("241325", "SE São Borja (revisão CL-012)"),
    (2001, "Guarabira"): ("89206", "Guarabira EC (revisão CL-012)"),
    (2003, "Goiatuba"): ("3260", "Goiatuba EC (revisão CL-006)"),
    (1997, "Operário(MT)"): ("ec-operario-mt", "EC Operário, de Várzea Grande (revisão CL-007)"),
    (1988, "Lagarto"): ("241324", "Lagarto EC (revisão CL-008)"),
    (1990, "Lagarto"): ("241324", "Lagarto EC (revisão CL-008)"),
    (1988, "Cabofriense"): ("71868", "AA Cabofriense (revisão CL-009)"),
    (1998, "Limoeiro"): ("115862", "EC Limoeiro (revisão CL-011)"),
    (2003, "Ituiutaba"): ("3306", "Ituiutaba EC, hoje Boa Esporte: um clube só em 2003 (revisão SC-012)"),
    (2002, "Tubarão"): ("3500", "Tubarão FC (1992-2005), como nos participantes da RSSSF (revisão CL-002)"),
    (1995, "Ariquemes"): ("214025", "SE Ariquemes (1981), a mesma da Copa do Brasil de 1994 (revisão CL-004)"),
    (1995, "ARIQUEMES(RO)"): ("214025", "SE Ariquemes (1981), a mesma da Copa do Brasil de 1994 (revisão CL-004)"),
}
# nome da RSSSF num grupo só: (ano, nome, grupo da página) -> (código do ogol, motivo). Vale sobre os votos do grupo
# (o ogol erra o clube nesses grupos)
NOME_MANUAL_GRUPO: dict[tuple[int, str, str], tuple[str, str]] = {
    (2007, "Imperatriz", "Grupo 17"): ("3285", "o ogol anula os jogos do Imperatriz no grupo 17 e os votos levavam o nome ao "
                                               "Tuna Luso (revisão SC-009, CL-001)"),
    (2004, "Atlético", "Grupo 13"): ("3125", "o 'Atlético' do grupo 13 é o Atlético Sorocaba (revisão SC-011)"),
}
# jogos da RSSSF que ficam de fora: (ano, mandante, visitante, gols, gols, fase da página ou "") -> motivo
JOGOS_FORA: dict[tuple, str] = {
    (2011, "CRB", "Rio Branco", 0, 0, "SECOND STAGE:"): "Rio Branco-AC eliminado pelo STJD: os jogos da 2ª fase não contam (revisão SC-013)",
    (2011, "Rio Branco", "Paysandu", 1, 2, "SECOND STAGE:"): "Rio Branco-AC eliminado pelo STJD: os jogos da 2ª fase não contam (revisão SC-013)",
    (2011, "América", "Rio Branco", 3, 0, "SECOND STAGE:"): "Rio Branco-AC eliminado pelo STJD: os jogos da 2ª fase não contam (revisão SC-013)",
    (2008, "Inter/SM", "Engenheiro Beltrão", 3, 2, "FIRST STAGE:"): "jogo repetido na página (o grupo 15 fica com 7 jogos por clube; "
                                                                     "a tabela fecha com o 3-0 de 17/08) (revisão SC-010)",
    (2008, "Toledo CW", "Marcílio Dias", 1, 1, "FIRST STAGE:"): "o mesmo jogo da 2ª fase (24/08), repetido na 1ª (revisão SC-010)",
}
# placar corrigido na página da RSSSF (ogol e Wikipédia dizem o mesmo): (ano, mandante, visitante, data da página) ->
# (mandante, visitante, gols, gols, resultado especial, motivo)
PLACAR_MANUAL: dict[tuple, tuple] = {
    (2007, "ABC", "Vera Cruz", "2007-07-14"): ("ABC", "Vera Cruz", 4, 0, "", "ogol, Bola n@ Área, Futebol Nacional e a tabela "
                                                "do grupo 6 na Wikipédia pt: 4-0 (revisão QC-011)"),
    (1988, "Internacional", "Figueirense", "1988-11-03"): ("Internacional", "Figueirense", 2, 0, "", "ogol e Wikipédia: 2-0 (revisão SC-014)"),
    (1992, "Rio Branco-MG", "São Bento", "1992-03-29"): ("Rio Branco-MG", "São Bento", 2, 1, "", "ogol e Wikipédia: 2-1 (revisão SC-014)"),
    (1992, "Nacional-AM", "Ji-Paraná", "1992-04-01"): ("Nacional-AM", "Ji-Paraná", 1, 0, "", "ogol e Wikipédia: 1-0 (revisão SC-014)"),
    (1992, "Nacional-AM", "Macapá", "1992-04-16"): ("Macapá", "Nacional-AM", 0, 2, "", "ogol e Wikipédia: Macapá 0-2 Nacional-AM (revisão SC-014)"),
    (1992, "Nacional-AM", "Auto Esporte", "1992-05-24"): ("Nacional-AM", "Auto Esporte", 3, 0, "", "ogol e Wikipédia (Placar): 3-0 (revisão SC-014)"),
    (2003, "Atlético Roraima", "Rio Branco-AC", "2003-10-16"): ("Atlético Roraima", "Rio Branco-AC", 1, 2, "", "ogol e Wikipédia: 1-2 (revisão SC-014)"),
    (1995, "Itumbiara", "Gama", "1995-09-02"): ("Itumbiara", "Gama", 1, 0, "awd", "em campo 1-2; o jogo foi dado ao Itumbiara (1-0): a "
                                                "tabela do grupo 8 na RSSSF e na Wikipédia fecha assim (revisão SC-015)"),
}
# punições que a Wikipédia em inglês não traz certo: (ano) -> {nome de exibição: ajuste}; e as que ficam de fora
AJUSTE_MANUAL: dict[int, dict[str, int]] = {2007: {"Nacional-PB": -6}}
AJUSTE_FORA: dict[tuple[int, str], str] = {(2007, "Araguaina-TO"): "a perda de 12 pontos do Araguaína foi revertida (Wikipédia pt)",
                                           (2006, "Ituiutaba"): "punição com '?' na própria fonte"}
# jogos do calendário do ogol que estão errados (a RSSSF e a tabela publicada mostram outro jogo): código do jogo -> motivo
OGOL_IGNORAR = {
    "6939419": "1995, grupo 12: Botafogo-PB x Coríntians foi cancelado (nota da RSSSF: '*x*'); o ogol traz 0-0, e a tabela do grupo não conta o jogo",
    "6939420": "1995, grupo 12: Santa Cruz-PB x ABC foi cancelado (nota da RSSSF: '*x*'); o ogol traz 0-0, e a tabela do grupo não conta o jogo",
    "5111115": "1998, grupo 10: o ogol tem União Bandeirante 5-0 Figueirense em 27/09; a RSSSF traz União Bandeirante 3-0 São José-RS, "
               "e as tabelas de Figueirense e São José só fecham com a RSSSF",
    "6953693": "1997, 2ª fase: o ogol tem Operário-MS 0-0 Itumbiara na volta; o confronto foi com o Ji-Paraná (ida 1-0 no ogol e na "
               "RSSSF); o Itumbiara já tinha caído na 1ª fase",
}
# jogos da RSSSF que ficam de fora: (ano, nome do clube) -> motivo
RSSSF_FORA = {
    (1998, "Itumbiara"): "eliminado por não pagar a taxa de arbitragem; todos os seus jogos foram anulados (nota da RSSSF; "
                         "o ogol e a tabela do grupo 5 não os trazem)",
}


def mapear_nomes(ano: int, rs: list, og: list[dict], log: list[str]) -> dict:
    """Nome na RSSSF -> código do ogol, por grupo: a mesma página às vezes usa o mesmo nome curto para clubes
    diferentes em grupos diferentes ("Esportivo" de Bento Gonçalves e de Passos em 1988).
    Cada jogo da RSSSF vota nos jogos do ogol de mesmo placar e data próxima (o voto pesa mais quando os nomes
    parecem); depois, dentro de cada grupo, um para um, do par mais votado para o menos.
    Devolve chaves (nome, fase, grupo) e, para as tabelas gerais, o nome sozinho."""
    noms = nomes_ogol(ano, og)
    fs = clubes_c.fichas()
    cache: dict[tuple, float] = {}
    def sim(n, i):
        """Parecença do nome; a UF escrita no nome da RSSSF ("São José(RS)") desempata homônimos."""
        if (n, i) not in cache:
            s = max((_sim(n, x) for x in noms.get(i, ()) if x), default=0)
            uf_n, uf_i = clubes_c.separar_uf(n.replace("(", " (").strip())[1], fs.get(i, {}).get("uf")
            if uf_n and uf_i:
                s = s * 0.6 if uf_n != uf_i else min(1.0, s + 0.05)
            cache[(n, i)] = s
        return cache[(n, i)]
    manual = {n: i for (a, n), (i, _m) in NOME_MANUAL.items() if a == ano}
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
            if (ano, n, g) in NOME_MANUAL_GRUPO:
                saida[(n, f, g)] = NOME_MANUAL_GRUPO[(ano, n, g)][0]
            elif melhor and melhor != base and n not in manual and votos[melhor] >= 4 and votos[melhor] >= 3 * votos.get(base, 0):
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
                    estadio=j.estadio or None, publico=j.publico, fonte=FONTE_RSSSF.format(ano=ano), gols_texto=j.gols, obs=j.nota, linha=j.linha)
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


def campanha(partidas: list[Partida], so: set | None = None) -> dict[str, list[int]]:
    c: dict[str, list[int]] = defaultdict(lambda: [0] * 6)
    for p in partidas:
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
    data_rs = {id(p): p.data for p in partidas}   # a data da página, antes de trocar pela do ogol
    datas_trocadas: list[Partida] = []
    datas_dif: list[tuple] = []
    por_par: dict[tuple, list[dict]] = defaultdict(list)
    for o in og:
        por_par[(o.get("mandante_id"), o.get("visitante_id"))].append(o)
    for p in sorted(partidas, key=lambda p: (p.data is None, p.data or "")):
        cands = [o for o in por_par.get((p.mandante, p.visitante), []) if o["id"] not in usados]
        if not cands:
            continue
        trocada = _trocar_dia_mes(p.data)
        dist = lambda o: min(_dist(o["data"], p.data), _dist(o["data"], trocada) if trocada else 999)
        cands.sort(key=lambda o: (dist(o), (o["gols_mandante"], o["gols_visitante"]) != (p.gm, p.gv)))
        o = cands[0]
        if dist(o) > 40:
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
    sobra = [p for p in partidas if not p.fonte_id]
    for o in og:
        if o["id"] in usados or o["gols_mandante"] is None:
            continue
        m, v, gm, gv = o.get("mandante_id"), o.get("visitante_id"), o["gols_mandante"], o["gols_visitante"]
        perto = lambda p: _dia(p.data) and _dia(o["data"]) and _dist(p.data, o["data"]) <= 4
        inv = [p for p in sobra if (p.mandante, p.visitante) == (v, m) and (p.gm, p.gv) == (gv, gm) and _dist(p.data, o["data"]) <= 3]
        inv_placar = [p for p in sobra if (p.mandante, p.visitante) == (v, m) and perto(p)]
        mesmo_par = [p for p in sobra if (p.mandante, p.visitante) == (m, v) and perto(p)]
        outro = [p for p in sobra if perto(p) and (p.gm, p.gv) == (gm, gv) and (p.mandante == m) != (p.visitante == v)]
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
    for o in og:
        if o["id"] in usados or o["gols_mandante"] is None or not (o.get("mandante_id") and o.get("visitante_id")):
            continue
        m, v = o["mandante_id"], o["visitante_id"]
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
    datas_do_confronto(ano, partidas, og, data_rs, log)
    return partidas + novos


def penaltis_faltando(ano, partidas: list[Partida], og: list[dict], log: list[str]) -> None:
    """Disputa de pênaltis que não está nos campos (revisão CB-008): do placar do ogol ("2-1 (4-3 Pen.)", na ordem do jogo
    do ogol) ou da nota da página ("Rio Negro 4-3 on pen", "3-5pen")."""
    og_por_id = {o["id"]: o for o in og}
    n = 0
    for p in partidas:
        if p.pen_m is not None or p.gm is None:
            continue
        pen = None
        o = og_por_id.get(p.fonte_id.split("ogol:")[-1].split(";")[0]) if "ogol:" in p.fonte_id else None
        m = re.search(r"\((\d+)\s*-\s*(\d+)\s*Pen", (o or {}).get("resultado") or "")
        if m:
            a, b = int(m[1]), int(m[2])
            pen = (a, b) if o.get("mandante_id") == p.mandante else (b, a)
        if pen is None:
            pen = penaltis_da_nota(p.obs, nome(p.mandante), nome(p.visitante))
        if pen:
            p.pen_m, p.pen_v = pen
            n += 1
    if n:
        log.append(f"{ano}: {n} disputas de pênaltis tiradas do placar do ogol ou da nota da página (revisão CB-008)")


def datas_do_confronto(ano, partidas: list[Partida], og: list[dict], data_rs: dict, log: list[str]) -> None:
    """Ida e volta do mesmo confronto com a mesma data (revisão SC-020): a página dá aos dois jogos a data do título da
    rodada (1994, 2003) ou o ogol dá a mesma data aos dois (1998). Vale a fonte que separa as duas datas: o ogol, senão
    a página."""
    data_og = {o["id"]: o["data"] for o in og}
    grupos = defaultdict(list)
    for p in partidas:
        grupos[(p.fase, frozenset((p.mandante, p.visitante)), p.data)].append(p)
    for (f, par, d), ps in grupos.items():
        if len(ps) < 2 or not d:
            continue
        og_d = [data_og.get(p.fonte_id.split("ogol:")[-1].split(";")[0]) if "ogol:" in p.fonte_id else None for p in ps]
        rs_d = [data_rs.get(id(p)) for p in ps]
        novas = og_d if all(og_d) and len(set(og_d)) == len(ps) else rs_d if all(rs_d) and len(set(rs_d)) == len(ps) else None
        if novas:
            for p, n in zip(ps, novas):
                p.data = n
            log.append(f"{ano}: ida e volta de {nome(ps[0].mandante)} x {nome(ps[0].visitante)} vinham com a mesma data ({d}); "
                       f"ficam {', '.join(novas)} ({'do ogol' if novas == og_d else 'da página'})")


OGOL_FASE = {"1F": "Primeira fase", "2F": "Segunda fase", "3F": "Terceira fase", "4F": "Quarta fase", "1/16": "Primeira fase eliminatória",
             "1/8": "Oitavas de final", "QF": "Quartas de final", "SF": "Semifinal", "F": "Final"}


def fase_do_ogol(o: dict, partidas: list[Partida]) -> tuple[str, str]:
    """Fase e grupo de um jogo que só o ogol tem: a fase e o grupo em que os dois clubes jogaram juntos, perto da data;
    senão, pelo código de fase do ogol."""
    m, v, d = o["mandante_id"], o["visitante_id"], _dia(o["data"])
    juntos = []
    for (f, g), ps in agrupar(partidas).items():
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
    f = ESPN / f"serie_c_{ano}.json"
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
    (r"^(fase única|first stage|first phase|1st phase|1a fase|1ª fase|primeira fase|grupo único|group stage)", "Primeira fase"),
    (r"^(second (phase|stage|round)|2nd phase|2a fase|2ª fase|segunda fase)", "Segunda fase"),
    (r"^(third (phase|stage)|3rd phase|3a fase|terceira fase)(?!.*(semi|final))", "Terceira fase"),
    (r"^(fourth (phase|stage)|4th phase|quarta fase)(?!.*(semi|final))", "Quarta fase"),
    (r"^(fifth (phase|stage)|5th phase|quinta fase)(?!.*(semi|final))", "Quinta fase"),   # 2003
    (r"serie c\s*-\s*-\s*fourth phase", "Quarta fase"),
    (r"round of 32", "Segunda fase"), (r"^(round of 16|1/8|eighth|oitavas)", "Oitavas de final"),
    (r"(quarter|quartas)", "Quartas de final"), (r"(semi)", "Semifinal"),
    (r"(final phase|final stage|quadrangular final|final standings)", "Fase final"),
    (r"(^|\W)finals?\W*$|final$|^final", "Final"), (r"knockout", "Mata-mata"),
]


def fase_pt(nome_fase: str) -> str:
    n = nome_fase.strip(" :")
    for padrao, pt in FASES_PT:
        if re.search(padrao, n, re.I):
            return pt
    return n


def nome(cid: str) -> str:
    return clubes_c.exibicao().get(cid, {}).get("clube", cid)


# --------------------------------------------------------------------------------------------- classificação

def pontos_vitoria(ano: int) -> int:
    return 3 if ano >= 1995 or ano == 1988 else 2


def pontos_jogos(ano: int, jogos: list[Partida]) -> dict[str, int]:
    """Pontos de cada clube nos jogos. Em 1988 (revisão SC-007) a vitória valia 3 e o empate ia para os pênaltis: quem
    vencia levava 2, quem perdia, 1 (empate sem pênaltis na fonte: 1 para cada)."""
    pv = pontos_vitoria(ano)
    saida: dict[str, int] = defaultdict(int)
    for p in jogos:
        if p.gm is None:
            continue
        for eu, a, b, pa, pb in ((p.mandante, p.gm, p.gv, p.pen_m, p.pen_v), (p.visitante, p.gv, p.gm, p.pen_v, p.pen_m)):
            if a != b:
                saida[eu] += pv if a > b else 0
            elif ano == 1988 and pa is not None and pb is not None and pa != pb:
                saida[eu] += 2 if pa > pb else 1
            else:
                saida[eu] += 1
    return saida


def ajustes_wiki(ano: int, ids_do_ano: set[str]) -> dict[str, int]:
    """Punições de pontos na Wikipédia em inglês (adjust_points), com o nome casado ao código do ogol."""
    saida = {}
    fs = clubes_c.exibicao()
    for nome_w, v in wiki.ajustes(ano).items():
        if (ano, nome_w) in AJUSTE_FORA:
            continue
        cands = sorted(((_sim(nome_w, fs[i]["clube"]), i) for i in ids_do_ano if i in fs), reverse=True)
        if cands and cands[0][0] >= 0.75 and v:
            saida[cands[0][1]] = v
    for nome_c, v in AJUSTE_MANUAL.get(ano, {}).items():
        saida.update({i: v for i in ids_do_ano if fs.get(i, {}).get("clube") == nome_c})
    return saida


def classificacao(ano: int, partidas: list[Partida], tabs: list[tuple], ajustes: dict[str, int], campeao: str | None,
                  log: list[str]) -> list[dict]:
    """Fase alcançada, depois pontos (com punições), vitórias, saldo e gols pró; o campeão e o vice da final em cima.
    Quando a RSSSF publica a classificação geral com todos os clubes e ela fecha com os jogos, vale a ordem dela."""
    camp = campanha(partidas)
    pv = pontos_vitoria(ano)
    ordem_fase: dict[str, int] = {}
    for p in partidas:
        ordem_fase.setdefault(p.fase, ORDEM.get(p.fase, 50))
    alcance: dict[str, int] = defaultdict(int)
    for p in partidas:
        for c in (p.mandante, p.visitante):
            alcance[c] = max(alcance[c], ordem_fase[p.fase])
    final = [p for p in partidas if p.fase == "Final"]
    vice = None
    if campeao and final:
        fin = {x for p in final for x in (p.mandante, p.visitante)} - {campeao}
        vice = next(iter(fin)) if len(fin) == 1 else None
    P = pontos_jogos(ano, partidas)
    def pts(c):
        return P.get(c, 0) + ajustes.get(c, 0)
    # na fase alcançada: a posição no grupo (ou no quadrangular/octogonal final) e os pontos nela
    fase_de = {}
    for c in camp:
        fs = [p for p in partidas if c in (p.mandante, p.visitante) and ordem_fase[p.fase] == alcance[c]]
        g = Counter((p.fase, p.grupo) for p in fs).most_common(1)[0][0] if fs else None
        fase_de[c] = g
    no_grupo = defaultdict(list)
    for c, g in fase_de.items():
        no_grupo[g].append(c)
    pos_grupo, pts_fase = {}, {}
    for (f, g), cs in ((k, v) for k, v in no_grupo.items() if k):
        bl = [p for p in partidas if (p.fase, p.grupo) == (f, g)]
        cg = campanha(bl)
        pg = pontos_jogos(ano, bl)
        mata = all(n == 1 for n in Counter(x for par in {frozenset((p.mandante, p.visitante)) for p in bl} for x in par).values())
        chave_g = lambda c: (-(pg.get(c, 0) + ajustes.get(c, 0)), -cg[c][1], -(cg[c][4] - cg[c][5]), -cg[c][4])
        for i, c in enumerate(sorted(cs, key=chave_g), 1):
            pos_grupo[c] = 0 if mata else i   # mata-mata: sem posição de grupo
            pts_fase[c] = pg.get(c, 0)
    # a posição no grupo só vale na última fase de liga (a que leva à final); quem caiu antes se ordena pela fase alcançada
    # e pelos pontos da campanha toda, como a "Classificação geral" da Wikipédia (decisão D-02 A; achado SC-018)
    nivel_liga = [alcance[c] for c in camp if pos_grupo.get(c)]
    ultima_liga = max(nivel_liga) if nivel_liga else None
    pos_grupo = {c: v for c, v in pos_grupo.items() if alcance[c] == ultima_liga}
    def chave(c):
        x = camp[c]
        # mesma posição no grupo (os 2º dos grupos da 2ª fase): a campanha toda, como na Wikipédia (2023: Operário-PR 3º)
        return (c != campeao, c != vice, -alcance[c], pos_grupo.get(c, 0), -pts(c), -x[1], -(x[4] - x[5]), -x[4], nome(c))
    # classificação geral publicada pela RSSSF (todos os clubes da edição)
    geral = [(tb, linhas) for tb, linhas, _ in tabs if len(linhas) >= len(camp) and len(tb.linhas) >= len(camp)]
    fonte = "calculada (fase alcançada, pontos, vitórias, saldo, gols pró)"
    ordem = sorted(camp, key=chave)
    if geral:
        tb, linhas = geral[-1]
        bate = sum(camp.get(c) == v for c, v in linhas.items())
        if bate >= 0.9 * len(camp):   # a ordem das linhas desempata dentro da mesma fase alcançada (campeão e vice em cima)
            rank = {c: i for i, c in enumerate(linhas)}
            ordem = sorted(camp, key=lambda c: (c != campeao, c != vice, -alcance[c], rank.get(c, 999), chave(c)))
            fonte = "RSSSF (classificação geral publicada)"
    saida = []
    for i, c in enumerate(ordem, 1):
        x = camp[c]
        saida.append({"pos": i, "clube": c, "j": x[0], "v": x[1], "e": x[2], "d": x[3], "gp": x[4], "gc": x[5], "pts": pts(c),
                      "ajuste": ajustes.get(c, 0), "fonte": fonte})
    return saida


ORDEM = {"Primeira fase": 1, "Segunda fase": 2, "Terceira fase": 3, "Quarta fase": 4, "Quinta fase": 4.5, "Mata-mata": 5,
         "Primeira fase eliminatória": 5,
         "Oitavas de final": 6, "Quartas de final": 7, "Semifinal": 8, "Fase final": 9, "Final": 10}


def _ordem_fases(partidas: list[Partida]) -> list[str]:
    por = defaultdict(list)
    for p in partidas:
        por[p.fase].append(p)
    return sorted(por, key=lambda f: (ORDEM.get(f, 0), min(p.data or "9999" for p in por[f])))


def final_entre_grupos(ano, partidas: list[Partida], log: list[str]) -> None:
    """Final gravada dentro de um grupo (2020: Vila Nova x Remo como "Segunda fase / Grupo D"): na última fase de grupos,
    os jogos entre clubes de grupos diferentes, depois de todos os jogos dos grupos, viram a Final."""
    fases = _ordem_fases(partidas)
    if not fases:
        return
    # o contrário (1992): jogos com o grupo de uma fase anterior gravados na Final voltam para essa fase
    if fases[-1] == "Final" and len(fases) > 1:
        grupos_ant = {p.grupo for p in partidas if p.fase == fases[-2] and p.grupo}
        volta = [p for p in partidas if p.fase == "Final" and p.grupo in grupos_ant]
        for p in volta:
            p.fase = fases[-2]
        if volta:
            log.append(f"{ano}: {len(volta)} jogos do {volta[0].grupo} da {fases[-2]} vêm na página depois do título da Final; "
                       f"voltam para a {fases[-2]}")
        fases = _ordem_fases(partidas)
    ult = [p for p in partidas if p.fase == fases[-1]]
    if len({p.grupo for p in ult if p.grupo}) < 2:
        return
    grupo_de = {}
    for c in {x for p in ult for x in (p.mandante, p.visitante)}:
        g = Counter(p.grupo for p in ult if c in (p.mandante, p.visitante))
        grupo_de[c] = g.most_common(1)[0][0]
    cruz = [p for p in ult if grupo_de[p.mandante] != grupo_de[p.visitante]]
    resto = [p for p in ult if p not in cruz]
    if cruz and len({frozenset((p.mandante, p.visitante)) for p in cruz}) == 1 and \
            min(p.data or "" for p in cruz) > max(p.data or "" for p in resto):
        for p in cruz:
            p.fase, p.grupo = "Final", ""
        log.append(f"{ano}: a final ({nome(cruz[0].mandante)} x {nome(cruz[0].visitante)}) vem na página dentro de um grupo da "
                   f"{fases[-1]}; vira a fase Final")


def nomes_do_mata_mata(ano, partidas: list[Partida], tabelas: list, log: list[str]) -> None:
    """As últimas fases de mata-mata levam o nome pelo número de confrontos: 1 = Final, 2 = Semifinal, 4 = Quartas de final,
    8 = Oitavas de final (2009: "Segunda/Terceira/Quarta fase"; 2023: a final como "Terceira fase")."""
    nomes = {1: "Final", 2: "Semifinal", 4: "Quartas de final", 8: "Oitavas de final"}
    for f in reversed(_ordem_fases(partidas)):
        ps = [p for p in partidas if p.fase == f]
        pares = {frozenset((p.mandante, p.visitante)) for p in ps}
        clubes = Counter(x for par in pares for x in par)
        if any(p.grupo for p in ps) or not all(n == 1 for n in clubes.values()) or len(pares) not in nomes:
            break
        novo = nomes[len(pares)]
        if novo != f:
            for x in [*ps, *(tb for tb in tabelas if tb.fase == f)]:
                x.fase = novo
            log.append(f"{ano}: a fase \"{f}\" é mata-mata com {len(pares)} confronto(s): vira \"{novo}\"")


# --------------------------------------------------------------------------------------------- uma edição

def campeoes() -> tuple[dict[int, str], dict[int, str]]:
    """Campeões pela RSSSF (br3camp.htm) e pela Wikipédia (pt_lista.txt): ano -> nome como a fonte escreve."""
    rs = {}
    t = rsssf.texto(0, "br3camp.htm")
    for a, n in re.findall(r"^(\d{4}) - (?!\s*not)(.+?)\s*(?:\(|$)", t, re.M):
        rs[int(a)] = n.strip()
    wk = {}
    txt = (PASTA_DADOS / "wikipedia" / "pt_lista.txt").read_text(encoding="utf-8")
    a, b = txt.find("=== Por clube"), txt.find("=== Por cidade")
    for r in txt[a:b].split("\n|-")[2:]:
        cel = [c for c in r.split("\n|") if c.strip()]
        if len(cel) < 2:
            continue
        nm = re.findall(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", cel[0])
        for y in re.findall(r"\d{4}", cel[1]):
            wk[int(y)] = nm[0] if nm else cel[0]
    return rs, wk


def montar_edicao(ano: int, log: list[str], rs_campeoes: dict, wk_campeoes: dict) -> dict:
    try:
        rs, tabelas = rsssf_c.ler(ano)
    except FileNotFoundError:   # sem a página da RSSSF (2026): o ogol é a base (BASE_OGOL)
        if ano not in BASE_OGOL:
            raise
        rs, tabelas = [], []
    for (a, n), motivo in RSSSF_FORA.items():
        if a == ano:
            fora = [j for j in rs if n in (j.mandante, j.visitante)]
            rs = [j for j in rs if j not in fora]
            log.append(f"{ano}: {len(fora)} jogos do {n} ficam de fora: {motivo}")
    for (a, m, v, gm, gv, f), motivo in JOGOS_FORA.items():
        if a == ano:
            fora = [j for j in rs if (j.mandante, j.visitante, j.gm, j.gv) == (m, v, gm, gv) and (not f or j.fase == f)]
            rs = [j for j in rs if j not in fora]
            log.append(f"{ano}: jogo da página que fica de fora ({len(fora)}): {m} {gm}-{gv} {v} — {motivo}")
    for j in rs:
        corr = PLACAR_MANUAL.get((ano, j.mandante, j.visitante, j.data))
        if corr:
            m, v, gm, gv, esp, motivo = corr
            log.append(f"{ano}: placar da página corrigido — {j.mandante} {j.gm}-{j.gv} {j.visitante} ({j.data}) vira {m} {gm}-{gv} {v}"
                       f"{' (resultado dado no tribunal)' if esp else ''}: {motivo}")
            j.nota = (j.nota + "; " if j.nota else "") + motivo
            j.mandante, j.visitante, j.gm, j.gv = m, v, gm, gv
            j.especial = esp or j.especial
            j.gols = ""   # os autores da página são do placar antigo
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
    mapa = mapear_nomes(ano, rs_usado, og, log) if rs_usado else {}
    partidas = ler_rsssf(ano, mapa, rs_usado)
    partidas = [p for p in partidas if p.gm is not None or p.especial]
    tabs = tabelas_por_clube(tabelas, mapa, rs_usado)
    partidas = juntar_ogol(ano, partidas, og, tabs, rs_ok, log)
    if ano >= 2016:
        juntar_espn(ano, partidas, log)
    if not rs_ok:   # base ogol: grupos por letra depois da 1ª fase de pontos corridos (rodadas "R") são a 2ª fase (2026)
        rodadas = [p for p in partidas if p.fase == "Primeira fase" and not p.grupo]
        grupos = [p for p in partidas if p.fase == "Primeira fase" and p.grupo]
        if rodadas and grupos and min(p.data or "" for p in grupos) > max(p.data or "" for p in rodadas):
            for p in grupos:
                p.fase = "Segunda fase"
    penaltis_faltando(ano, partidas, og, log)
    # fases em português, nos jogos e nas tabelas (as tabelas já estão ligadas aos códigos dos clubes)
    for p in partidas:
        p.fase = fase_pt(p.fase) if rs_ok else fase_pt(OGOL_FASE.get(p.ogol_fase, p.fase))
        p.grupo = p.grupo if not p.grupo.lower().startswith(("grupo único", "grupo unico")) else ""
    for tb in tabelas:
        tb.fase = fase_pt(tb.fase)
    if len({p.fase for p in partidas}) == 1 and not any(p.grupo for p in partidas):
        for x in [*partidas, *tabelas]:
            x.fase = "Fase única"
    final_entre_grupos(ano, partidas, log)
    nomes_do_mata_mata(ano, partidas, tabelas, log)
    # autores: só quando fecham com o placar
    for p in partidas:
        if p.gols and p.gm is not None and len(p.gols) != p.gm + p.gv:
            p.gols = []
    datas_corrigidas.aplicar(PASTA_DADOS, ano, partidas, nome, log)   # jogo noturno do ogol com o dia seguinte (QC-002)
    ids = {x for p in partidas for x in (p.mandante, p.visitante)}
    ajustes = ajustes_wiki(ano, ids) if ano >= 2003 else {}
    # campeão: vencedor da final; conferido com a RSSSF e a Wikipédia (final empatada sem pênaltis: vale a lista oficial)
    campeao = vencedor_final(partidas)
    oficial = campeao_oficial(ano, partidas, rs_campeoes, wk_campeoes)
    if campeao is None and oficial:
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
    alvo = wk_c.get(ano) or rs_c.get(ano)
    if not alvo:
        return None
    fs = clubes_c.fichas()
    ids = {x for p in partidas for x in (p.mandante, p.visitante)}
    def nota(i):
        nomes = {nome(i), *(fs.get(i, {}).get("nomes_ogol") or []), fs.get(i, {}).get("nome_completo") or "", fs.get(i, {}).get("curto", "")}
        uf = clubes_c.separar_uf(alvo)[1]   # "Botafogo-PB" x "Botafogo-SP": a UF desempata
        return max(_sim(alvo, x) for x in nomes if x) + (0.1 if uf and fs.get(i, {}).get("uf") == uf else 0)
    melhor = sorted(((nota(i), i) for i in ids), reverse=True)
    return melhor[0][1] if melhor and melhor[0][0] >= 0.8 and (len(melhor) == 1 or melhor[1][0] < melhor[0][0]) else None


# edições em que a RSSSF não serve de base (o ogol é a base dos jogos)
BASE_OGOL = {2019: "a página da RSSSF parou na 1ª rodada (40 jogos): a base dos jogos é o ogol (194 jogos)",
             2026: "a RSSSF ainda não tem a página de 2026: a base dos jogos é o ogol (revisão SC-001)"}


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
    anos = [int(a) for a in sys.argv[1:] if a.isdigit()]
    main(anos or ANOS, gravar=not anos)
