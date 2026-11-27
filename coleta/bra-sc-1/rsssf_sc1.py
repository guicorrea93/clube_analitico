"""Leitura das páginas do Campeonato Catarinense da RSSSF Brasil (data/coleta/bra-sc-1/rsssfbrasil/sc{ano}.htm).

Usa o leitor comum (coleta/comum/rsssf.py), como o Gaúcho (coleta/bra-rs-1/rsssf_rs1.py), de onde vêm as correções
genéricas: a data "dd/Mon" na frente do jogo, as súmulas em caixa alta que repetem o jogo da lista, o grupo de cada jogo
pelas tabelas da fase, a linha de tabela de clube empatado sem a posição, o público "Att:" e as frases "X are
qualified". As correções de cada página ficam em CORRECOES, com o motivo; o nome em português das fases estranhas, em
FASE_ANO.

Uso: python coleta/bra-sc-1/rsssf_sc1.py [temporada ...]     (sem temporada: todas; com uma, lista as divergências)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
import rsssf  # noqa: E402
from observacao import penaltis_da_nota  # noqa: E402
from edicoes import PASTA_DADOS, TEMPORADAS, ano_de, pagina_rsssf  # noqa: E402

rsssf.PASTA = PASTA_DADOS / "rsssfbrasil"
rsssf.MODELO = "sc{ano}.htm"
rsssf.QUEBRA_BLOCOS = True   # <P>/<PRE>/<H2> sem <br>: o título ficava colado no jogo


def _data_mes(t: str) -> str:
    """"13/Aug  Grêmio 5-0 Cruzeiro": a data com o mês por extenso na frente do jogo vai para o formato "[Aug 13]"
    que o leitor comum entende; também com o ano ("02/Jan/1955 ...": "[Jan 02, 1955]")."""
    return re.sub(r"^([ \t]*)(\d{1,2})/([A-Za-z]{3})(?:/(\d{4}))?\b\.?[ \t]+",
                  lambda m: f"{m[1]}[{m[3].capitalize()} {m[2]}{', ' + m[4] if m[4] else ''}] ", t, flags=re.M)


def _dia_mes(t: str) -> str:
    """Páginas antigas (até 1960): a data sem colchete na frente do jogo ("09 Oct   Cachoeira 2-1 Cruzeiro",
    "13 Oct 1946  Guarany Bagé 2-3 Grêmio Santanense") ou sozinha na linha ("07 Dec"): vira "[Oct 09] ..." /
    "[Oct 13, 1946] ...", que o leitor comum entende."""
    def troca(m) -> str:
        return f"{m[1]}[{m[3][:3].capitalize()} {m[2]}{', ' + m[4] if m[4] else ''}]{' ' if m[5] else ''}{m[5] or ''}"
    return re.sub(rf"^([ \t]*)(\d{{1,2}})[ \t]+({rsssf.MES_EN}|{rsssf.MES_PT})\.?(?:[ \t]+(\d{{4}}))?,?[ \t]*(?:[ \t]+(\S[^\n]*))?$",
                  troca, t, flags=re.M | re.I)


def _data_tracos(t: str) -> str:
    """1959: vários jogos na mesma linha, cada um com a data "10-Abr-1960" na frente: cada jogo vai para uma linha, com a
    data no formato "[Abr 10, 1960]" (1960: "22-Jan-61", ano com dois dígitos). Também a data sozinha na linha, sem
    colchete, com o mês na frente ("Jan 19", 2013)."""
    ano = lambda a: a if len(a) == 4 else f"19{a}" if int(a) > 30 else f"20{a}"
    t = re.sub(r"[ \t]*\b(\d{1,2})-([A-Za-z]{3})-(\d{4}|\d{2})\b[ \t]*", lambda m: f"\n[{m[2]} {m[1]}, {ano(m[3])}] ", t)
    return re.sub(rf"(?m)^[ \t]*({rsssf.MES_EN})[ \t]+(\d{{1,2}})[ \t]*$", r"[\1 \2]", t, flags=re.I)


def _prorrogacao(t: str) -> str:
    """Páginas antigas: a prorrogação numa linha depois do jogo ("Prorrogação: Gaúcho 2-0", "Prorrogação (20 Minutos):
    0-0", "Primeira Prorrogação: 0-0  Segunda Prorrogação: 1-0"), às vezes com o título seguinte colado ("Prorrogação: 1-0
    FINAL"): o placar da prorrogação vira nota do jogo de cima ("[prorrogação: Gaúcho 2-0]") e o resto da linha fica na
    linha de baixo."""
    pro = r"(?:Primeira |Segunda )?Prorroga[çc][ãa]o[^:\n]*:\s*((?:[\wÀ-úº.]+(?: [\wÀ-úº.]+)*? )?\d+\s*-\s*\d+)"
    def troca(m) -> str:
        notas = "".join(f"  [prorrogação: {re.sub(r'\s+', ' ', x)}]" for x in re.findall(pro, m[2]))
        resto = re.sub(rf"\s*{pro}\s*", " ", m[2]).strip()
        return f"{m[1].rstrip()}{notas}" + (f"\n{resto}" if resto else "")
    # duas prorrogações em linhas seguidas ("Primeira Prorrogação: 0-0" / "Segunda Prorrogação: 1-0"): numa linha só
    t = re.sub(r"(?m)^([ \t]*(?:Primeira |Segunda )?Prorroga[^\n]*)\n(?:[ \t]*\n)*(?=[ \t]*(?:Primeira |Segunda )?Prorroga)",
               r"\1  ", t)
    return re.sub(rf"(?m)^([^\n]*\d\s*[-x]\s*\d[^\n]*)\n(?:[ \t]*\n)*[ \t]*((?:{pro}[ \t]*)+[^\n]*)$", troca, t)


def _somar_prorrogacao(jogos: list) -> None:
    """Gols da prorrogação somados ao placar (como no Carioca de 1921): "[aet 1-0]", "[prorrogação: Gaúcho 2-0]",
    "(extra time: 3-0)", "[X win 2-0 in extra time]". Sem clube, o placar está na ordem da linha da página (no jogo de
    volta de "A 0-0 1-1 B [aet 0-1]", a ordem é A-B, ao contrário do jogo). O placar dos 90 minutos fica na nota."""
    pad = re.compile(r"(?i)(?:\baet|prorroga[çc][ãa]o|extra time)\s*:?\s*(?:([A-Za-zÀ-ú.]+(?: [A-Za-zÀ-ú.]+)*?)\s+)?(\d+)\s*-\s*(\d+)"
                     r"|\b([A-Za-zÀ-ú.]+(?: [A-Za-zÀ-ú.]+)*?)\s+win\s+(\d+)\s*-\s*(\d+)\s+in extra time")
    for k, j in enumerate(jogos):
        if j.gm is None:
            continue
        achados = pad.findall(j.nota or "")
        if not achados:
            continue
        volta = k > 0 and jogos[k - 1].linha == j.linha and (jogos[k - 1].mandante, jogos[k - 1].visitante) == (j.visitante, j.mandante)
        a_m = a_v = 0
        for c1, x1, y1, c2, x2, y2 in achados:
            clube, x, y = (c1, x1, y1) if x1 else (c2, x2, y2)
            x, y = int(x), int(y)
            if clube and rsssf.chave(clube)[:4] in (rsssf.chave(j.visitante)[:4],) and rsssf.chave(clube)[:4] != rsssf.chave(j.mandante)[:4]:
                a_m, a_v = a_m + y, a_v + x
            elif clube or not volta:
                a_m, a_v = a_m + x, a_v + y
            else:
                a_m, a_v = a_m + y, a_v + x
        if a_m or a_v:
            j.nota = f"{j.nota}; 90 minutos: {j.gm}-{j.gv}; prorrogação: {a_m}-{a_v}".strip("; ")
            j.gm, j.gv = j.gm + a_m, j.gv + a_v


ORDINAIS = {i: n for i, n in enumerate("Zero Primeiro Segundo Terceiro Quarto Quinto Sexto Sétimo Oitavo Nono Décimo".split())}
ORDINAL_DE = {n: i for i, n in ORDINAIS.items()}

MESES_EN = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def _data_barra(t: str) -> str:
    """1976, 1989...: jogos em duas colunas, cada um com a data "26/02/89-" colada na frente ("26/02/89-Caxias 0x2
    Esportivo      01/03/89-Juventude 2x1 São Paulo(rg)"): cada jogo vai para uma linha, com a data "[Feb 26, 1989]";
    os pênaltis colados ao nome ("Juventude(4x5)") viram "[pen 4-5]"."""
    def data(m) -> str:
        a = int(m[3])
        return f"\n[{MESES_EN[int(m[2]) - 1]} {int(m[1])}, {a + 1900 if a > 30 else a + 2000}] "
    t = re.sub(r"[ \t]*\b(\d{1,2})/(\d{1,2})/(\d{2})\s*-\s*(?=\S)", data, t)
    t = re.sub(r"\(\s*(\d+)\s*x\s*(\d+)\s*\)[ \t]*$", r"  [pen \1-\2]", t, flags=re.M)
    # placar "1x2" -> "1-2" (com a data na mesma linha, o leitor comum só reconhece o placar com traço)
    return re.sub(r"(?m)^(\[[^\]\n]+\][^\n]*?\s)(\d{1,2})x(\d{1,2})(?=\s|$)", r"\1\2-\3", t)


def _empatados(t: str) -> str:
    """Linha de tabela de clube empatado sem o número da posição ("  .Renascença  15  6  4  5  27-24  16"): ganha a
    posição da linha de cima (o leitor comum só lê linha de tabela que começa com o número)."""
    saida, pos = [], None
    for l in t.splitlines():
        m = re.match(r"^\s*(\d{1,2})\s*\.\s*\D", l)
        if m:
            pos = m.group(1)
        elif pos and re.match(r"^\s+\.[^\s.]", l):
            l = re.sub(r"^\s+\.", f" {pos}.", l, count=1)
        saida.append(l)
    return "\n".join(saida)


_MESES_EN = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


def _data_ano_na_frente(t: str) -> str:
    """Catarinense (páginas do livro do Nirez, 1939-1999): "23/04/39 Penarol 5-3 Ferroviário" e "27/01/90 Tiradentes 1 x 0
    Ferroviário", a data com o ano na frente de cada jogo -> "[Apr 23, 1939] Penarol 5-3 Ferroviário". O ano de dois
    dígitos é do século do ano da página (o leitor só aceita a data de outro ano quando ela traz o ano)."""
    def troca(m):
        d, mes, a = int(m[1]), int(m[2]), m[3]
        if not 1 <= mes <= 12 or not 1 <= d <= 31:
            return m[0]
        ano = int(a) if len(a) == 4 else (1900 if int(a) > 30 else 2000) + int(a)
        jogo = re.sub(r"(\S)[ \t]+(\d{1,2})[ \t]*[xX×][ \t]*(\d{1,2})[ \t]+(?=\S)", r"\1 \2-\3 ", m[4])
        return f"[{_MESES_EN[mes - 1]} {d}, {ano}] {jogo}"
    return re.sub(r"(?m)^[ \t]*(\d{1,2})[/.](\d{1,2})[/.](\d{2}|\d{4})[ \t]+(\S[^\n]*)$", troca, t)



def _data_pontos(t: str) -> str:
    """"26.01.69" sozinha na linha, com o jogo "Ferroviário 1 x 0 Tiradentes" embaixo (1941-1992) -> "[Jan 26, 1969]" e
    "Ferroviário 1-0 Tiradentes"; e "05.03-Ceará 2x1 Ferroviário   08.03-Fortaleza 4x0 Calouros do ar" (1995, duas
    colunas, sem o ano) -> um jogo por linha, com "[Mar 5]"."""
    def data(m):
        d, mes = int(m[1]), int(m[2])
        if not 1 <= mes <= 12 or not 1 <= d <= 31:
            return m[0]
        if not m[3]:
            return f"[{_MESES_EN[mes - 1]} {d}]"
        ano = int(m[3]) if len(m[3]) == 4 else (1900 if int(m[3]) > 30 else 2000) + int(m[3])
        return f"[{_MESES_EN[mes - 1]} {d}, {ano}]"
    t = re.sub(r"[ \t]{3,}(?=\d{2}\.\d{2}-\S)", "\n", t)   # duas colunas
    t = re.sub(r"(?m)^[ \t]*(\d{2})\.(\d{2})-(?=\S)", lambda m: data((m[0], m[1], m[2], "")) + " ", t)
    t = re.sub(r"(?m)^[ \t]*(\d{2})\.(\d{2})\.(\d{2}|\d{4})[ \t]*$", data, t)
    # placar "1 x 0" / "2x1" numa linha de jogo (nome, placar, nome)
    return re.sub(r"(?m)^([ \t]*(?:\[[^\]\n]*\][ \t]*)?[A-Za-zÀ-ú][^\n\d]*?[A-Za-zÀ-ú.)])[ \t]*(\d{1,2})[ \t]*[xX×][ \t]*(\d{1,2})"
                  r"[ \t]*(?=[A-ZÀ-Ýa-zà-ý])", r"\1 \2-\3 ", t)


for _t in TEMPORADAS:
    _arq = pagina_rsssf(_t)
    rsssf.CORRECOES.setdefault(_arq, []).append((_data_ano_na_frente, None, "data \"23/04/39\" na frente de cada jogo"))
    rsssf.CORRECOES[_arq].append((_data_pontos, None, "data \"26.01.69\" sozinha na linha e placar \"1 x 0\""))
    rsssf.CORRECOES.setdefault(_arq, []).append((_data_mes, None, "data com o mês por extenso na frente do jogo"))
    rsssf.CORRECOES[_arq].append((_dia_mes, None, "data \"09 Oct\" sem colchete na frente do jogo (páginas antigas)"))
    rsssf.CORRECOES[_arq].append((_data_tracos, None, "data \"10-Abr-1960\" na frente de cada jogo, vários na mesma linha"))
    rsssf.CORRECOES[_arq].append((_data_barra, None, "jogos em duas colunas com a data \"26/02/89-\" colada"))
    rsssf.CORRECOES[_arq].append((r"(?<![\dº])(\d{1,2})\s*\.\s*(?:RI\b|R\.\s?I\.|Regimento\b|Reg\.)",
                                  lambda m: f"{ORDINAIS[int(m[1])]} RI",
                                  "\"9. RI\" / \"9.Regimento\" (o clube do 9º Regimento de Infantaria): o leitor comum recusa "
                                  "nome com número; lê \"Nono RI\" e ler() devolve \"9º RI\""))
    rsssf.CORRECOES[_arq].append((r"\b14 Livramento\b", "14 de Julho", "\"14 Livramento\": o 14 de Julho de Livramento"))
    rsssf.CORRECOES[_arq].append((r"(?<=[A-Za-zÀ-ú])\s?\(([A-Z]{3,4}|[a-z]{2,4})[)}]", lambda m: f"/{m[1].upper()}",
                                  "cidade de três letras entre parênteses (\"BRASIL(PEL)\", \"BRASIL(FAR)\", \"GUARANY(GAR)\"): o "
                                  "leitor comum tira o parêntese do fim do nome; vira \"BRASIL/PEL\""))
    rsssf.CORRECOES[_arq].append((r"(?m)^[ \t]*Note\(s\):\s*Pk:[^\n]*$", "", "pênaltis repetidos na súmula (o jogo da lista já tem)"))
    rsssf.CORRECOES[_arq].append((r"(?m)^([^\n\[]*\d\s*-\s*\d[^\n]*)(\n[ \t]*\[[^\n]*\])?\n[ \t]*Pk:\s*(.+?)\s+(\d+)\s*-\s*(\d+)[ \t]*",
                                  r"\1  [\3 \4-\5 on pen]\2\n",
                                  "pênaltis numa linha depois do jogo (\"Pk: Cruzeiro 5-4\"): vira nota do jogo de cima"))
    rsssf.CORRECOES[_arq].append((_prorrogacao, None, "linha \"Prorrogação: ...\" depois do jogo vira nota dele"))
    rsssf.CORRECOES[_arq].append((r"^(\[[^\]\n]{3,14}\])(?=[^\s\d])", r"\1 ", "data colada ao nome (\"[Fev 27]São Luiz\")"))
    rsssf.CORRECOES[_arq].append((r"^(\[[A-Za-z]{3} \d{1,2}\])[ \t]+(\d{2})[ \t]+", lambda m: f"{m[1][:-1]}, 19{m[2]}] ",
                                  "ano com dois dígitos depois da data (\"[Dez 28] 52 ...\")"))
    rsssf.CORRECOES[_arq].append((r"(\d)[ \t]*–[ \t]*(\d)", r"\1-\2", "placar com travessão (\"1–2\")"))
    rsssf.CORRECOES[_arq].append((r"^([A-ZÀ-Ý][^\n(\[]*\bare (?:qualified|relegated|promoted)\b[^\n]*)$", r"(\1)",
                                  "frase (\"X are qualified ...\"), não título de fase"))
    rsssf.CORRECOES[_arq].append((r"[ \t]+Att:[ \t]*([\d.,]+)[ \t]*$", r"  att: \1", "público \"Att: 535\" (o leitor lê \"att:\")"))
    rsssf.CORRECOES[_arq].append((r"^([ \t]*\d{1,2})[ \t]*[°º][ \t]*", r"\1. ", "posição na tabela com \"°\" / \"º\" (\"1° Grêmio\")"))
    rsssf.CORRECOES[_arq].append((r"^[ \t]*(Classifica[çc][ãa]o\b[^\n]*)$", r"Tabela - \1",
                                  "\"Classificação Final - Primeira Fase:\" é o título da tabela, não uma fase nova"))
    rsssf.CORRECOES[_arq].append((_empatados, None, "linha de tabela de clube empatado sem o número da posição"))

MESES_PT = "jan fev mar abr mai jun jul ago set out nov dez".split()


def _data_barra_mes(t: str) -> str:
    """"[12/mai]" (dia/mês por extenso): vira "[mai 12]", que o leitor comum entende."""
    return re.sub(r"\[(\d{1,2})/([a-zç]{3})\]", r"[\2 \1]", t, flags=re.I)


def _data_traco_mes(t: str) -> str:
    """1917, 1980, 1985: vários jogos na mesma linha, cada um com a data "29-abr" na frente: um jogo por linha, com a data
    "[abr 29]"."""
    return re.sub(rf"[ \t]*\b(\d{{1,2}})-({'|'.join(MESES_PT)})\b[ \t]*", lambda m: f"\n[{m[2]} {m[1]}] ", t, flags=re.I)


def _datas_na_linha(t: str) -> str:
    """1932: vários jogos na mesma linha, cada um com a data "[May 22]" na frente: um jogo por linha."""
    return re.sub(r"(?<=\S)[ \t]+(\[[A-Z][a-z]{2} \d{1,2}(?:, \d{4})?\])", r"\n\1", t)


def _placar_depois_do_nome(t: str) -> str:
    """1994: "Apucarana 0 x Grêmio Maringá 0" (o placar depois de cada nome) e a data "2/2" sozinha na linha: viram
    "Apucarana  0-0  Grêmio Maringá" e "[Feb 2]"."""
    t = re.sub(r"(?m)^[ \t]*(\S.*?)\s+(\d{1,2})\s+x\s+(\S.*?)\s+(\d{1,2})[ \t]*$", r"\1  \2-\4  \3", t)
    return re.sub(r"(?m)^[ \t]*(\d{1,2})/(\d{1,2})[ \t]*$", lambda m: f"[{MESES_EN[int(m[2]) - 1]} {int(m[1])}]", t)


def _planilha_ano(ano: int):
    """2026: "06/01   20:00   São Joseense   2-0   Galo Maringá" (dia/mês e hora na frente): vira "[Jan 6, 2026] São
    Joseense  2-0  Galo Maringá"."""
    def f(t: str) -> str:
        return re.sub(r"(?m)^[ \t]*(\d{1,2})/(\d{1,2})[ \t]+\d{1,2}:\d{2}[ \t]+",
                      lambda m: f"[{MESES_EN[int(m[2]) - 1]} {int(m[1])}, {ano}] ", t)
    return f


def _wo_traco(t: str) -> str:
    """"Água Verde  W-O  Coritiba": W.O. sem dizer quem venceu; vira "awd" (o vencedor sai da tabela publicada, como no
    Carioca)."""
    return re.sub(r"(?m)^([ \t]*\S[^\n]*?)[ \t]+W-O[ \t]+(\S[^\n\[]*?)[ \t]*$", r"\1  awd  \2  [W.O.]", t)


MESES_EN = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


def _data_pontos(t: str) -> str:
    """"13.03.1938" (ou "16.04.1939 Guarany 1-4 Operário") no começo da linha -> "[Mar 13, 1938]", que o leitor entende."""
    return re.sub(r"(?m)^[ \t]*(\d{2})\.(\d{2})\.(\d{4})[ \t]*",
                  lambda m: f"[{MESES_EN[int(m[2]) - 1]} {int(m[1])}, {m[3]}] " if 1 <= int(m[2]) <= 12 else m[0], t)


def _planilha_2026(t: str) -> str:
    """Semifinais e final de 2026: "14/02/26 16:00 Operário-PR 2x2 Coritiba" -> "[Feb 14, 2026] Operário-PR 2-2 Coritiba"."""
    return re.sub(r"(?m)^(\d{2})/(\d{2})/26[ \t]+\d{1,2}:\d{2}[ \t]+(.+?)[ \t]+(\d+)[ \t]*[x-][ \t]*(\d+)[ \t]+(.+?)[ \t]*$",
                  lambda m: f"[{MESES_EN[int(m[2]) - 1]} {int(m[1])}, 2026] {m[3]}  {m[4]}-{m[5]}  {m[6]}", t)


# correções de cada página, com o motivo (a mesma página pode estar em mais de um grupo: as listas se somam)
_POR_PAGINA: list[tuple[str, list]] = [
]
for _arq, _lista in _POR_PAGINA:
    rsssf.CORRECOES.setdefault(_arq, []).extend(_lista)

_MESES_PT_CURTO = {"jan": "Jan", "fev": "Feb", "mar": "Mar", "abr": "Apr", "mai": "May", "jun": "Jun", "jul": "Jul",
                   "ago": "Aug", "set": "Sep", "out": "Oct", "nov": "Nov", "dez": "Dec"}


def _duas_colunas(t: str) -> str:
    """Catarinense (anos 1940): dois jogos lado a lado, com as duas datas na linha de cima ("[07 Jan 1945]     [14 Jan 1945]"
    / "Palmeiras 3-0 Caxias       Caxias 4-6 Palmeiras") -> um jogo por linha, cada um com a sua data."""
    return re.sub(r"(?m)^[ \t]*(\[[^\]\n]+\])[ \t]{3,}(\[[^\]\n]+\])[ \t]*\n(?:[ \t]*\n)*[ \t]*([^\n]*?\d-\d[^\n]*?)[ \t]{3,}(\S[^\n]*?\d-\d[^\n]*)$",
                  r"\1\n\3\n\2\n\4", t)


def _mes_pt_colchete(t: str) -> str:
    """"[11 Fev 1945]" (mês em português, com ou sem o ano e o local) -> "[Feb 11, 1945]"."""
    def troca(m):
        mes = _MESES_PT_CURTO.get(m[2][:3].lower())
        return f"[{mes} {int(m[1])}{', ' + m[3] if m[3] else ''}]" if mes else m[0]
    return re.sub(r"\[(\d{1,2})[ /-]([A-Za-zç]{3})[a-zç]*[ /-]?(\d{4})?[^\]\n]*\]", troca, t)


def _jogo_quebrado(t: str) -> str:
    """Páginas dos anos 1920-1930: o jogo quebrado em duas linhas ("04.01.31 Marcílio Dias 1-0" / "Brasil")."""
    return re.sub(r"(?m)^([^\n]*[A-Za-zÀ-ú.)][ \t]+\d{1,2}[ \t]*-[ \t]*\d{1,2})[ \t]*\n[ \t]*(?![\[\d(])([A-ZÀ-Ý][^\n]*)$",
                  r"\1 \2", t)


for _t in TEMPORADAS:
    rsssf.CORRECOES[pagina_rsssf(_t)][0:0] = [
        (_jogo_quebrado, None, "jogo quebrado em duas linhas"),
        (_mes_pt_colchete, None, "data com o mês em português (\"[11 Fev 1945]\")"),
        (_duas_colunas, None, "dois jogos lado a lado, com as duas datas em cima"),
    ]
_MESES_PT = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro",
             "dezembro")


def _data_extenso(t: str) -> str:
    """1996: "25.fevereiro.1996.domingo" sozinha na linha -> "[Feb 25, 1996]"."""
    def troca(m):
        mes = m[2].lower().replace("ç", "c").replace("marco", "março")
        return f"[{_MESES_EN[_MESES_PT.index(mes)]} {int(m[1])}, {m[3]}]" if mes in _MESES_PT else m[0]
    return re.sub(r"(?m)^[ \t]*(\d{1,2})\.([A-Za-zçÇ]+)\.(\d{4})(?:\.[A-Za-zá-ú-]+)?[ \t]*$", troca, t)


# notas da página que vêm depois do jogo, na coluna do nome: viram nota entre colchetes (o "jogo anulado" sai, como os
# "[annulled]"); antes de tudo, para a data do começo da linha ver o jogo limpo
_NOTAS_DEPOIS = [
    (r"(?m)[ \t]+jogo anulado[ \t]*$", "  [jogo anulado]", "\"jogo anulado\" depois do jogo (1939): o jogo sai"),
    (r"(?m)[ \t]+este jogo não terminou[ \t]*$", "  [jogo não terminado]", "\"este jogo não terminou\" depois do jogo (1939)"),
    (r"(?m)[ \t]+jogo decisivo[ \t]*$", "  [jogo decisivo]", "\"jogo decisivo\" depois do jogo (1928)"),
    (r"(?m)^---[ \t]*\?[ \t]*---[ \t]*", "[unknown] ", "jogo sem data (\"--- ? ---\", 1928)"),
]
for _t in TEMPORADAS:
    rsssf.CORRECOES[pagina_rsssf(_t)][0:0] = list(_NOTAS_DEPOIS)

# títulos que o leitor comum não toma por fase ("Jogo Desempate", "LEAGUE", "... Tournament", "Tie-break")
rsssf.FASE = re.compile(rsssf.FASE.pattern[:-1] + r"|tournament|^league$|tie-?break|desempate|^ta[çc]a |^finais$|"
                                                 r"^campeonato estadual$|eliminat[óo]ria)", re.I)

# nome da fase em português, por temporada, quando o nome da página não basta: temporada -> nome na página (sem ":" no
# fim) -> fase. O importador usa o nome como está.
# "fase|grupo": a fase e o grupo. Anos 1980: os turnos tinham nome de taça (Copa Governador do Estado, Taça J. A. Rebelo...)
# e o título saía de um quadrangular ou hexagonal decisivo ("Fase final")
FASE_ANO: dict[str, dict[str, str]] = {
    "1930": {"Fase": "Primeira fase"},
    "1935": {"Turno: Returno": "Primeira fase"},
    "1956": {"Decision": "Final"},
    "1965": {"FASE ESTADUAL": "Segunda fase", "Second Place tie-break": "Desempate do vice"},
    "1967": {"Returno (Grupo 1 x Grupo 2)       Local": "Primeira fase"},
    "1971": {"Turno (Jogos de ida)": "1º Turno", "Turno (Jogos de volta)": "2º Turno"},
    "1976": {"Fase": "Segunda fase"},
    "1977": {"Ferroviário apparently abandoned the tournament afterwards": "Primeira fase",
             "Bottom teams qualified to Third Phase repescagem": "Segunda fase", "Final Phase (Pentagonal Final)": "Fase final"},
    "1980": {"Stage": "Primeira fase"},   # a 1ª fase só com os jogos do Joinville (a página não traz os outros)
    "1981": {"PRIMEIRO TURNO": "1º Turno", "SEGUNDO TURNO": "2º Turno",
             "QUADRANGULAR FINAL DA COPA GOVERNADOR DO ESTADO": "1º Turno - Fase final", "Stage": "Segunda fase"},
    "1982": {"PRIMEIRA FASE": "1º Turno", "RETURNO": "1º Turno", "OCTOGONAL SEMIFINAL": "1º Turno - Fase final",
             "QUADRANGULAR DECISIVO": "1º Turno - Fase final", "Primeira Fase": "2º Turno", "SEMIFINAIS": "1º Turno - Semifinal",
             "FINAL": "1º Turno - Final", "Joinville campeao do primeiro turno": "1º Turno - Final",
             "REPESCAGEM - DEFINICAO DOS CABECAS DE CHAVE": "Repescagem", "SEGUNDO TURNO - PRIMEIRA FASE": "2º Turno",
             "QUARTAS DA SEGUNDA FASE": "Turnos - Segunda fase", "SEMIFINAL DA SEGUNDA FASE": "Turnos - Semifinal",
             "FINAIS DA SEGUNDA FASE": "2º Turno - Final", "CHAMPIONSHIP FINALS": "Final"},
    "1983": {"COPA GOVERNADOR DO ESTADO (Primeira Fase do Campeonato)": "1º Turno", "Segunda Fase": "1º Turno",
             "Returno": "1º Turno", "Semifinais": "1º Turno - Semifinal", "Finais": "1º Turno - Final", "1. TURNO": "2º Turno",
             "Final": "2º Turno - Final", "TAÇA JOSÉ ELIAS GIULIARI": "3º Turno", "Decisão da 4ª vaga": "Desempate da vaga",
             "QUADRANGULAR DECISIVO": "Fase final"},
    "1984": {"PRIMEIRA FASE": "1º Turno", "FASE SEMIFINAL": "1º Turno - Fase final", "SEMIFINAIS": "Turnos - Semifinal",
             "TAÇA J. A. REBELO": "2º Turno", "QUARTAS DE FINAL": "Turnos - Segunda fase", "FINAIS": "Turnos - Final",
             "TAÇA ALDO ALMEIDA": "3º Turno", "QUADRANGULAR FINAL DO CAMPEONATO": "Fase final"},
    "1985": {"PRIMEIRA FASE": "1º Turno", "SEGUNDA FASE": "1º Turno - Fase final",
             "AVAÍ classificado para as Semifinais": "1º Turno - Fase final", "SEMIFINAIS": "Turnos - Semifinal",
             "FINAIS": "Turnos - Final", "TAÇA JOSÉ LEAL MEIRELLES": "2º Turno", "TAÇA DITE FREITAS": "3º Turno",
             "HEXAGONAL DE DESCENSO": "Torneio de rebaixamento", "HEXAGONAL DECISIVO": "Fase final"},
    "1986": {"PRIMEIRA FASE": "1º Turno", "JOINVILLE e FIGUEIRENSE classificados para as Semifinais": "1º Turno",
             "SEMIFINAIS": "Turnos - Semifinal", "FINAL": "Turnos - Final", "TAÇA UNIVERSIDADE FEDERAL DE SANTA CATARINA": "2º Turno",
             "TAÇA PLÍNIO DE NES": "3º Turno", "HEXAGONAL DECISIVO - TAÇA PEDRO LOPES": "Fase final"},
    "1988": {"1. TURNO - 1ª FASE": "1º Turno", "2ª FASE": "1º Turno - Fase final", "1. TURNO - SEMIFINAL": "1º Turno - Fase final",
             "2. TURNO - 2ª FASE": "2º Turno", "2. TURNO - SEMIFINAIS": "2º Turno - Semifinal", "2. TURNO - FINAL": "2º Turno - Final",
             "DECISÃO - 1ª FASE -  HEXAGONAL FINAL": "Fase final", "HEXAGONAL DECISIVO - 2º TURNO": "Fase final"},
    "1989": {"PRIMEIRO TURNO": "1º Turno", "SEGUNDO TURNO": "2º Turno", "FINAIS": "Segunda fase", "SEMIFINAIS": "Semifinal",
             "QUADRANGULAR SELETIVO DE REPESCAGEM": "Repescagem", "QUADRANGULAR SELETIVO DE DESCENSO": "Torneio de rebaixamento",
             "QUADRANGULAR FINAL": "Fase final"},
    "1990": {"DECISÃO TAÇA GOVERNADOR": "1º Turno - Final", "Turno": "Fase final", "HEXAGONAL SECUNDÁRIO": "Torneio extra"},
    "1991": {"First Phase - First Stage": "Primeira fase", "First Phase - Second Stage": "Primeira fase",
             "First Phase Playoff": "Primeira fase - Desempate", "Second Phase - First Stage": "Segunda fase",
             "Second Phase - Second Stage": "Segunda fase", "Second Phase - Final": "Primeira fase - Final",
             "Main Quadrangular": "Fase final", "Secondary Quadrangular": "Torneio extra",
             "Relegation Hexagonal": "Torneio de rebaixamento", "Championship Semifinals": "Semifinal",
             "Championship Final": "Final"},
    "1994": {"Primeiro Turno (Taça Governador do Estado)": "Primeira fase", "QUADRANGULAR DE REPESCAGEM": "Repescagem",
             "3ª fase": "Terceira fase"},
    "2007": {"Championship Finals (between stage winners)": "Final"},
    "2014": {"Taça Santa Catarina": "Torneio extra"},   # dos eliminados na 1ª fase, junto da 2ª fase
    "2017": {"Stage": "1º Turno", "Returno": "2º Turno"},
}

# grafias erradas da página (as páginas dos anos 1960-1990 vêm de texto escaneado): nome na página -> nome certo
GRAFIAS: dict[str, str] = {
    # nomes partidos (o jogo quebrado em duas linhas antes do placar) e siglas das páginas
    "Carlos": "Carlos Renaux", "Renaux": "Carlos Renaux", "Luz": "Hercílio Luz", "Hercílio": "Hercílio Luz",
    "HERCÍLIO": "Hercílio Luz", "HL": "Hercílio Luz", "Dias": "Marcílio Dias", "DIAS": "Marcílio Dias",
    "Marcílio": "Marcílio Dias", "MARCÍLIO": "Marcílio Dias", "Marcilio": "Marcílio Dias", "MD": "Marcílio Dias",
    "Barroso": "Almirante Barroso", "Almirante": "Almirante Barroso", "Ramos": "Paula Ramos", "Paulo": "São Paulo",
    "Cruz": "Santa Cruz", "DO SUL": "Rio do Sul", "Rio": "Rio do Sul", "Bom": "Bom Retiro", "Telegráfico": "Postal Telegráfico",
    "Joinvile": "Joinville", "FEROVIÁRIO": "Ferroviário", "Ferrovíario": "Ferroviário", "Sport Brusquense": "Brusquense",
    "Konder": "Adolpho Konder", "Ararangua": "Araranguá", "JOINVILLE/XXXX": "Joinville",
}
# nota colada ao nome na página ("Londrina   Played in Rolândia", "Esperança  It did not finish", o estádio ou os
# autores dos gols na mesma coluna): sai do nome
NOTA_NO_NOME = re.compile(r"\s+(?:Played in .*|It did not finish.*)$|\s+-\s+Gols?:.*$|\s+-$|\s+Estádio\s.*$|"
                          r"\s*\((?:[^()]|\([^()]*\))*\([^()]*\)(?:[^()]|\([^()]*\))*\)$|^\?\s*|"
                          r"\s*\([A-ZÀ-Ý][a-zà-ú]{3,}[^()]*\)$")
# (autores do gol ou estádio na coluna do nome: "Blumenau - Gol: Zé Humberto" (1989), "AVAÍ (Nardela (J) e Passos (A))"
# (1983), "Metropol Estádio Vidal Ramos" (1967); "? Figueirense" (1941))
# jogos que não são do campeonato: clube de outro estado ou seleção estrangeira (amistosos nas páginas de 1941 e as tabelas
# lidas como jogo) e linhas de nota lidas como jogo ("terminando 3-2 para o Avaí", "extra time: Brusque 0-1 Avai")
FORA_DO_CAMPEONATO = re.compile(r"\((?:[^()]*-)?(?:PR|RS|SP|RJ|MT)\)|Romania|^\?|\?$|^(?:terminando|extra time|a favor|para o)\b|"
                                r"\bx\b.*–")
# "INTERNACIONAL(SM)" com as letras trocadas pelo escaneamento ("INTERNACfONAL(SM)", "ÍNTERNACIGNAL{SM)", "INTERNACIONAMSM)")
INTER_SM = re.compile(r"$^")   # (no Gaúcho: o Internacional de Santa Maria escaneado)


def _grafia(n: str) -> str:
    n = NOTA_NO_NOME.sub("", n)
    n = GRAFIAS.get(n, n)
    return n


# até 1960: primeira fase estadual (os jogos antes dela que falam em zona ou região são a fase regional)
ESTADUAL = re.compile(r"(?i)^(primeira fase|1\.? fase|segunda fase|fase preliminar|quartas|semi|final$|finals?$|turno|"
                      r"quadrangular|triangular)")
REGIONAL = re.compile(r"(?i)\bzona\b|regi[ãa]o|regionais|^final serra")


def _fase_regional(jogos: list) -> None:
    """Até 1960 (campeonato por regiões): os jogos das decisões de zona e região que a página traz antes da fase estadual
    ("Final Zona Serra", "Decisão da Zona Centro", grupo "Zona Litoral") ficam na "Fase regional", com a zona no grupo
    (escopo aprovado em 25/11: entram as decisões de zona e região, não os campeonatos das cidades)."""
    if not any(REGIONAL.search(f"{j.fase} {j.grupo}") for j in jogos):
        return
    for j in jogos:
        if ESTADUAL.match(j.fase.strip(" :")):
            break
        zona = re.search(r"(?i)\bzona\s+([A-Za-zÀ-ú/]+)", j.grupo) or re.search(r"(?i)\bzona\s+([A-Za-zÀ-ú/]+)", j.fase) or \
            re.search(r"(?i)final (serra)", j.fase)
        j.fase = "Fase regional"
        j.grupo = f"Zona {zona.group(1).strip().title()}" if zona else ""


# turnos com mata-mata próprio (2009-2013): título de turno e as fases eliminatórias dentro dele
TURNO = re.compile(r"(?i)(primeiro|segundo|1º|2º|first|second)\s*(turno|stage)|^ta[çc]a (piratini|farroupilha)")
ELIMINATORIA = re.compile(r"(?i)^(stage\s+)?(quart|semi|final(?!\s*(phase|stage|standings)))")
FINAL_CAMPEONATO = re.compile(r"(?i)^(league|championship)\s+finals?|^final do campeonato|^finais$")
NOMES_ELIM = (("quart", "Quartas de final"), ("semi", "Semifinal"), ("final", "Final"))


def _turnos(jogos: list) -> None:
    """2009-2013: o 1º e o 2º turno (Taça Piratini, Taça Farroupilha, Taça Fernando Carvalho, Taça Fabio Koff) têm
    quartas, semifinal e final próprias ("Stage quarterfinals", "QUARTAS-DE-FINAL", "FINAL DO SEGUNDO TURNO"); viram
    "1º Turno - Quartas de final", "2º Turno - Final" etc. A final do campeonato ("LEAGUE FINALS", "CHAMPIONSHIP FINALS")
    fica "Final"."""
    n, vistos = 0, []
    for j in jogos:
        f = j.fase.strip(" :")
        if f not in vistos:
            vistos.append(f)
            if TURNO.search(f) and not ELIMINATORIA.match(f):
                n += 1
        if not n or FINAL_CAMPEONATO.match(f):
            continue
        if TURNO.search(f) and not ELIMINATORIA.match(f):
            j.fase = f"{min(n, 2)}º Turno"
            continue
        m = ELIMINATORIA.match(re.sub(r"(?i)^ta[çc]a \w+\s*-\s*", "", f))
        if m:
            nome = next(x for k, x in NOMES_ELIM if m.group(2).lower().startswith(k))
            turno = 2 if re.search(r"(?i)segundo|second", f) else min(n, 2)
            j.fase = f"{turno}º Turno - {nome}"


# 3º jogo de uma série eliminatória, com título próprio na página
DESEMPATE_SERIE = re.compile(r"(?i)^(primeiro |segundo |first |second )?(jogo[- ]?desempate|desempate|tie-?breaking match)$")

# torneios à parte que a página traz junto: ficam fora (o importador tira os mesmos jogos do ogol)
# a "Final do Interior" (2015 e 2016) é um título à parte, como o Troféu do Interior do Gaúcho: os jogos ficam fora
ANOS_A_PARTE: set[int] = set()
# fora do pacote: o Torneio Início (1935 e outros anos, na mesma página do campeonato)
A_PARTE = re.compile(r"(?i)^torneio in[íi]cio")
# jogo lido sob o título da tabela final (linhas da classificação lidas como jogo); a tabela fica
JOGO_FORA = re.compile(r"(?i)^(final standings|final classification|elenco)")


def trofeu(temporada: str) -> list:
    """Jogos do torneio à parte da temporada (ANOS_A_PARTE), como estão na página."""
    if ano_de(temporada) not in ANOS_A_PARTE:
        return []
    jogos, _ = rsssf.ler(ano_de(temporada), pagina_rsssf(temporada))
    return [j for j in jogos if A_PARTE.match(j.fase)]


# jogos anulados ou cancelados que a página traz ("[annulled]", "[cancelled]"): ficam fora; temporada -> jogos tirados
# (o importador registra no relatório e tira os mesmos do ogol)
ANULADO = re.compile(r"\bannul|\bcancel|\banulad", re.I)
ANULADOS: dict[str, list] = {}


def tem_pagina(temporada: str) -> bool:
    return (rsssf.PASTA / pagina_rsssf(temporada)).exists()


def _grupo_limpo(g: str) -> str:
    """"Group D   M  W  D  L  GF-GA  Pts": o cabeçalho das colunas sai do nome do grupo."""
    return re.split(r"\s{2,}|Pos(?=Team)", g)[0].strip(" :")


def _casar_tabela(nomes_tab: list[str], nomes_jogos: set[str]) -> dict[str, str]:
    """Nome da tabela -> nome nos jogos: igual; senão o de prefixo comum mais longo; o resto pelo casamento comum."""
    saida = {nt: nt for nt in nomes_tab if nt in nomes_jogos}
    for nt in nomes_tab:
        if nt in saida:
            continue
        k = rsssf.chave(nt)
        cands = [(len(rsssf.chave(nj)), nj) for nj in nomes_jogos - set(saida.values())
                 if k.startswith(rsssf.chave(nj)) or rsssf.chave(nj).startswith(k)]
        if cands:
            cands.sort(reverse=True)
            if len(cands) == 1 or cands[0][0] != cands[1][0]:
                saida[nt] = cands[0][1]
    resto = [nt for nt in nomes_tab if nt not in saida]
    if resto:
        saida.update(rsssf.casar(resto, nomes_jogos - set(saida.values())))
    return saida


def _grupos_pelas_tabelas(jogos: list, tabelas: list) -> None:
    """Fase com tabelas de grupo e os jogos misturados: os dois clubes no mesmo grupo -> esse grupo; em grupos diferentes ->
    sem grupo. Mata-mata: "grupo" de dois clubes não é grupo."""
    for fase in {j.fase for j in jogos}:
        tabs = [tb for tb in tabelas if tb.fase == fase and re.match(r"(group|grupo|s[ée]rie)\b", tb.grupo, re.I)]
        if len({tb.grupo for tb in tabs}) < 2:
            continue
        nos_jogos = {x for j in jogos if j.fase == fase for x in (j.mandante, j.visitante)}
        grupo_de = {}
        for tb in sorted(tabs, key=lambda tb: -len(tb.linhas)):
            for nt, nj in _casar_tabela([r["nome"] for r in tb.linhas], nos_jogos).items():
                grupo_de[nj] = tb.grupo
        menor = min(len(tb.linhas) for tb in tabs if tb.linhas) if any(tb.linhas for tb in tabs) else 0
        for tb in tabs:
            if menor and len(tb.linhas) >= 2 * menor:   # a tabela geral
                tb.grupo = ""
        for j in jogos:
            if j.fase == fase:
                gm, gv = grupo_de.get(j.mandante), grupo_de.get(j.visitante)
                if gm and gv:
                    j.grupo = gm if gm == gv else ""
    # fase em que cada clube só enfrenta os do outro grupo (2009-2012): nenhum jogo tem grupo; a tabela de cada grupo
    # é conferida com todos os jogos da fase
    for fase in {tb.fase for tb in tabelas if tb.grupo}:
        if any(j.fase == fase for j in jogos) and not any(j.grupo for j in jogos if j.fase == fase):
            for tb in tabelas:
                if tb.fase == fase:
                    tb.grupo = ""
    clubes: dict[tuple, set] = {}
    for j in jogos:
        clubes.setdefault((j.fase, j.grupo), set()).update((j.mandante, j.visitante))
    for x in [*jogos, *tabelas]:
        if x.grupo and x.fase != "Fase regional" and len(clubes.get((x.fase, x.grupo), ())) <= 2 and \
                (not hasattr(x, "linhas") or len(x.linhas) <= 2):
            x.grupo = ""


def _caixa_alta(n: str) -> bool:
    return bool(re.search(r"[A-ZÀ-Ý]{4,}", n)) and n == n.upper()


def sem_sumulas(jogos: list) -> list:
    """Súmula em caixa alta depois do jogo decisivo ("ATLÉTICO 2 x 1 CRUZEIRO"): é o mesmo jogo da lista e sai."""
    chave = lambda s: re.sub(r"[^a-z]", "", rsssf.chave(s).lower())[:6]
    normais = [j for j in jogos if not (_caixa_alta(j.mandante) and _caixa_alta(j.visitante))]
    saida = []
    for j in jogos:
        if _caixa_alta(j.mandante) and _caixa_alta(j.visitante) and any(
                {chave(k.mandante), chave(k.visitante)} == {chave(j.mandante), chave(j.visitante)}
                and (k.gm, k.gv) in ((j.gm, j.gv), (j.gv, j.gm)) for k in normais):
            continue
        saida.append(j)
    return saida


def ler(temporada: str):
    from edicoes import SEM_JOGOS
    if temporada in SEM_JOGOS:   # a página só traz jogos soltos: a edição entra só com o pódio
        return [], []
    jogos, tabelas = rsssf.ler(ano_de(temporada), pagina_rsssf(temporada))
    ANULADOS[temporada] = [j for j in jogos if ANULADO.search(j.nota)]
    jogos = [j for j in jogos if j not in ANULADOS[temporada] and not A_PARTE.match(j.fase) and not JOGO_FORA.match(j.fase)]
    jogos = [j for j in jogos if not (FORA_DO_CAMPEONATO.search(j.mandante.strip()) or FORA_DO_CAMPEONATO.search(j.visitante.strip()))]
    tabelas = [tb for tb in tabelas if not A_PARTE.match(tb.fase)]
    for x in [*jogos, *tabelas]:
        x.fase = FASE_ANO.get(temporada, {}).get(x.fase.strip(" :"), x.fase)
        if "|" in x.fase:
            x.fase, x.grupo = x.fase.split("|")
        x.grupo = _grupo_limpo(x.grupo)
    for j in jogos:
        j.mandante, j.visitante = j.mandante.lstrip("-– ").strip(), j.visitante.lstrip("-– ").strip()
    _somar_prorrogacao(jogos)
    for j in jogos:   # "[Cruzeiro 5-4 on pen]": pênaltis com o vencedor nomeado -> "pen 4-5" (mandante-visitante)
        if "on pen" in (j.nota or ""):
            pen = penaltis_da_nota(j.nota, j.mandante, j.visitante)
            if pen:
                j.nota = "; ".join(x for x in (re.sub(r"[^;\[\]]*\bon pen\b[^;\[\]]*", "", j.nota).strip(" ;[]"),
                                                f"pen {pen[0]}-{pen[1]}") if x)
    if ano_de(temporada) <= 1960:
        _fase_regional(jogos)

    for j in jogos:   # "Nono RI" -> "9º RI"; grafias erradas da página
        j.mandante, j.visitante = (_grafia(re.sub(r"\b(\w+) RI\b", lambda m: f"{ORDINAL_DE[m[1]]}º RI" if m[1] in ORDINAL_DE
                                                  else m[0], x)) for x in (j.mandante, j.visitante))
    for tb in tabelas:
        for r in tb.linhas:
            r["nome"] = _grafia(r["nome"])
    # "Jogo-desempate" de uma série eliminatória (o 3º jogo) e frase da página tomada por título ("with the top 2 of
    # Losers group...", "mau tempo, sendo finalizada...", "da Fase Constitutiva"): ficam na fase do jogo de cima
    frase = lambda f: bool(re.match(r"[a-zà-ú]", f)) or len(f.split()) > 7 or \
        bool(re.search(r"(?i)\b(sera|será|sendo|nessa)\b|^combined table", f))
    for k, j in enumerate(jogos):
        f = j.fase.strip(" :")
        if k and (DESEMPATE_SERIE.match(f) or frase(f)):
            j.fase, j.grupo = jogos[k - 1].fase, jogos[k - 1].grupo
    jogos = sem_sumulas(jogos)
    _grupos_pelas_tabelas(jogos, tabelas)
    return jogos, tabelas


def conferir(temporada: str):
    jogos, tabelas = ler(temporada)
    return jogos, tabelas, rsssf.conferir(jogos, tabelas)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    alvo = sys.argv[1:] or [t for t in TEMPORADAS if tem_pagina(t)]
    for t in alvo:
        jogos, tabelas, erros = conferir(t)
        print(f"{t}: {len(jogos)} jogos, {len(tabelas)} tabelas ({sum(len(x.linhas) for x in tabelas)} linhas), {len(erros)} divergências")
        if len(alvo) == 1:
            for e in erros[:60]:
                print("   ", e)
