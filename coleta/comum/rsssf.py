"""Leitor genérico das páginas de campeonato da RSSSF Brasil (copiado de serie_b/rsssf.py, com a pasta e o
nome do arquivo como parâmetro: PASTA e MODELO, que a coleta de cada competição ajusta).

As páginas seguem, com variações, o mesmo desenho: títulos de fase ("First Phase",
"Semifinals"), de grupo ("Group A", "Zona Norte") e de rodada ("Round 3"); linhas de
data ("[Sep 12]"); jogos ("Ferroviário-CE  1-1  Ferroviário-PE  [nota]"); logo abaixo
de cada jogo, os autores dos gols entre colchetes ("[Alízio 79; Fernando 8]"); e as
tabelas de cada grupo (" 1.Ferroviário-CE   6  4  1  1  12- 7   9").

O leitor devolve os jogos com fase, grupo, rodada e data, e as tabelas publicadas,
e `conferir` compara cada tabela com a soma dos jogos lidos do mesmo grupo: é o que
diz se a página foi lida inteira e certa.

Uso: python coleta/comum/rsssf.py <pasta> <modelo> [ano ...]   (ex.: data/coleta/bra-serie-c/rsssfbrasil br{ano}l3.htm)
"""
from __future__ import annotations

import difflib
import html
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

PASTA = Path(__file__).resolve().parent.parent.parent / "data" / "serie_b" / "rsssfbrasil"   # cada coleta ajusta
MODELO = "br{ano}l2.htm"
MESES = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
MESES.update({"fev": 2, "abr": 4, "mai": 5, "ago": 8, "set": 9, "out": 10, "dez": 12})

# jogo: "Mandante  2-1  Visitante  [nota]"; o placar fica entre espaços (ou tabulação)
# placar "2 x 2" (com espaços) e data na frente do jogo ("26/05/1940 A 2 x 2 B"), como nas páginas do Paulista;
# desligado por padrão (nas outras páginas um "2 x 1" pode estar numa nota de rodapé)
PLACAR_X_ESPACADO = False
JOGO = re.compile(r"^\s*(?P<m>\S.*?)\s+(?P<gm>\d{1,2})(?:\s*-\s*|x)(?P<gv>\d{1,2})\s+(?P<v>\S.*?)\s*(?:\[(?P<nota>.*?)\]?)?\s*$")
# W.O., não jogado, abandonado: "A  awd  B [awarded 1-0]", "A  n/p  B"
ESPECIAL = re.compile(r"^\s*(?P<m>\S.*?)\s+(?P<tipo>awd|dns|w\.o\.|wo-\d|\d-wo|wo|n/p|abd|canc)\s+(?P<v>\S.*?)\s*(?:\[(?P<nota>.*?)\]?)?\s*$", re.I)
SEM_PLACAR = re.compile(r"^\s*(?P<m>[^\[\d].*?)\s{2,}-\s{2,}(?P<v>\S.*?)\s*$")
# "[Sep 12]", "[Sep 12, 1971]", "[Feb 2/72]", e ida e volta "[Feb 2 and 9]" / "[Feb 26 and Mar 2]"
MES_EN = r"(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sep(?:t(?:ember)?)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)"
MES_PT = r"(?:jan(?:eiro)?|fev(?:ereiro)?|mar(?:ço|co)?|abr(?:il)?|mai(?:o)?|jun(?:ho)?|jul(?:ho)?|ago(?:sto)?|set(?:embro)?|out(?:ubro)?|nov(?:embro)?|dez(?:embro)?)"
DATA = re.compile(r"^\s*\[(?:(?:mon|tue|wed|thu|fri|sat|sun)[a-z]*,?\s+)?(?P<mes>" + MES_EN + "|" + MES_PT + r")\.?\s+(?P<dia>\d{1,2})(?:[,/ ]\s*(?P<ano>\d{2,4})(?!\d))?"
                  r"(?:\s*(?:and|e|&|,)\s*(?:(?P<mes2>" + MES_EN + "|" + MES_PT + r")\.?\s+)?(?P<dia2>\d{1,2})(?:/(?P<ano2>\d{2,4}))?)?[^\]]*\]\s*$", re.I)
# ida e volta numa linha: "A  1-0  0-2  B" = A 1-0 B (mando de A) e B 2-0 A (mando de B)
IDA_VOLTA = re.compile(r"^\s*(?P<m>\S.*?)\s+(?P<a1>\d{1,2})-(?P<b1>\d{1,2})\s+(?P<a2>\d{1,2})-(?P<b2>\d{1,2})\s+(?P<v>[^\d\[].*?)\s*(?:\[(?P<nota>.*?)\]?)?\s*$")
# série de três jogos (1997): "ABC  2-2  0-3  1-3  Gama" = 1º jogo com mando do primeiro, os outros dois fora
TRES_JOGOS = re.compile(r"^\s*(?P<m>\S.*?)\s+(?P<a1>\d{1,2})-(?P<b1>\d{1,2})\s+(?P<a2>\d{1,2})-(?P<b2>\d{1,2})\s+(?P<a3>\d{1,2})-(?P<b3>\d{1,2})\s+(?P<v>[^\d\[].*?)\s*(?:\[(?P<nota>.*?)\]?)?\s*$")
# data com o dia antes do mês, em português: "[09 Outubro]", "[2 de novembro]"
DATA_PT = re.compile(r"^\s*\[(?P<dia>\d{1,2})(?:\s+de)?\s+(?P<mes>" + MES_PT + "|" + MES_EN + r")\.?(?:\s+(?:de\s+)?(?P<ano>\d{4}))?\s*\]\s*$", re.I)
DATA_NUM = re.compile(r"^\s*(?:data:\s*)?(?P<dia>\d{1,2})/(?P<mes>\d{1,2})/(?P<ano>\d{2,4})(?:\s*-\s*[A-Za-zÀ-ú\-]+)?\s*$", re.I)
LINHA_TABELA = re.compile(r"^\s*(?P<pos>\d{1,2})\s*[.\-]\s*(?P<nome>\D+?)\s+(?P<j>\d+)\s+(?P<v>\d+)\s+(?P<e>\d+)\s+(?P<d>\d+)\s+(?P<gp>\d+)\s*-\s*(?P<gc>\d+)\s+(?P<pts>-?\d+)")
# 1988 (empate decidido nos pênaltis): " 1-Náutico  10  6  1/ 1  2  12- 5  21" (empates ganhos / perdidos nos pênaltis)
LINHA_TABELA_PEN = re.compile(r"^\s*(?P<pos>\d{1,2})\s*[.\-]\s*(?P<nome>\D+?)\s+(?P<j>\d+)\s+(?P<v>\d+)\s+(?P<e1>\d+)\s*/\s*(?P<e2>\d+)\s+(?P<d>\d+)\s+(?P<gp>\d+)\s*-\s*(?P<gc>\d+)\s+(?P<pts>-?\d+)")
# começa com número de posição ("1.", "12-", "3 ") e não com nome de clube que tem número ("4 de Julho")
COMECA_COM_POSICAO = re.compile(r"^\s*\d+(?!\s+de\s)(?:\s*[.\-]|\s)")
RODADA = re.compile(r"^(?:(?:round|rodada|matchday|jornada)\s*(\d+)\b|(\d+)\s*(?:ª|a|º|o|st|nd|rd|th)\s*(?:rodada|round)\b)", re.I)
GRUPO = re.compile(r"^(?:group|grupo|chave|zone|zona|series|série|section|pool|módulo|modulo)\b|\b(?:zone|zona|group|grupo)\s*\(?[A-Z0-9]?\)?$", re.I)
# fase de copa: "First Round", "Second Round" (Copa do Brasil); "Round 3" é rodada (RODADA)
RODADA_COPA = re.compile(r"^(first|second|third|fourth|fifth|1st|2nd|3rd|4th|5th|preliminary)\s+round\b", re.I)
FASE = re.compile(r"(phase|fase|stage|final|semi|quarter|knockout|play-?off|repescagem|turno|returno|eliminat|round of|octav|oitavas|quartas|decis|triangular|quadrangular|hexagonal|torneio)", re.I)
IGNORAR_TITULO = re.compile(r"^(table|tabela|participants|participantes|moved match|moved matches|first leg|second leg|third leg|about this|ficha|top ?scorer|artilh|notes?|obs)", re.I)


@dataclass
class Jogo:
    fase: str
    grupo: str
    rodada: int | None
    data: str | None
    mandante: str
    visitante: str
    gm: int | None
    gv: int | None
    nota: str = ""
    gols: str = ""          # texto dos autores dos gols, como está na página
    especial: str = ""      # awd, n/p, abd...
    linha: int = 0
    hora: str = ""          # só nas páginas em planilha
    estadio: str = ""
    publico: int | None = None   # quando a página traz ("att: 18.865", 2005)


@dataclass
class Tabela:
    fase: str
    grupo: str
    titulo: str
    linhas: list[dict] = field(default_factory=list)
    linha: int = 0


CABECA_TABELA = re.compile(r"^\s*(?P<pos>\d{1,2})\s*(?:[.\-*)]\s*|\s+|(?=[^\d\s]))(?P<nome>[^\d\s|][^\d|]*?)\s+(?P<nums>-?\d[\d\s\-|]*)")


def linha_tabela(bruta: str) -> dict | None:
    """Linha de tabela em qualquer das ordens que as páginas usam: J V E D GP-GC Pts (a mais comum) ou
    Pts J V E D GP GC (1981, 1995, 2009, 2016 em diante). Fica a ordem em que J = V + E + D."""
    m = LINHA_TABELA_PEN.match(bruta)
    if m:
        lt = {k: (int(v) if k != "nome" else limpar_nome(v)) for k, v in m.groupdict().items()}
        lt["e"] = lt.pop("e1") + lt.pop("e2")
        return lt
    m = CABECA_TABELA.match(bruta)
    if not m:
        return None
    nome = limpar_nome(m["nome"])
    if not nome or len(nome) > 40 or re.search(r"\b(round|rodada|group|grupo)\b", nome, re.I):
        return None
    resto = bruta[m.start("nums"):]
    resto = re.split(r"[|%]|\d+[.,]\d", resto)[0]   # para antes do aproveitamento ("1,500", "58%") e da parte casa/fora
    nums = [int(x) for x in re.findall(r"-?\d+", re.sub(r"(\d)\s*-\s*(\d)", r"\1 \2", resto))]
    nums = [abs(x) if i else x for i, x in enumerate(nums)]
    if len(nums) < 7:
        return None
    opcoes = []
    a = dict(zip("j v e d gp gc pts".split(), nums[:7]))
    b = dict(zip("pts j v e d gp gc".split(), nums[:7]))
    # Série D 2016-2019: "PTS J PE V E D GP GC" (uma coluna a mais entre J e V)
    c = dict(zip("pts j pe v e d gp gc".split(), nums[:8])) if len(nums) >= 8 else None
    if c:
        c.pop("pe")
    for o in (a, b, c):
        if not o:
            continue
        if o["j"] == o["v"] + o["e"] + o["d"] and o["j"] > 0:
            # pontos que fecham com 3 por vitória valem antes dos que fecham com 2 (mata-mata de 2 jogos: "3 2 1 0 1 4 5"
            # é Pts 3, J 2, e não J 3, V 2 com 5 pontos)
            nota = 0 if o["pts"] == 3 * o["v"] + o["e"] else 1 if o["pts"] == 2 * o["v"] + o["e"] else 2
            opcoes.append((nota, o))   # empate: vale a ordem a, b, c (a coluna extra da Série D é a última opção)
    if not opcoes:
        return None
    o = min(opcoes, key=lambda x: x[0])[1]
    obs = re.sub(r"\s+", " ", re.sub(r"[\d.,%|]+|(?<![A-Za-z])-|-(?![A-Za-z])", " ", bruta[m.start("nums"):])).strip()   # "Qualified", "Relegated"
    return {"pos": int(m["pos"]), "nome": nome, **o, "obs": obs}


# página em planilha (Série C 2013-2015, 2020, 2023, 2024): "02/jun/13  19:00 Estádio-Cidade-UF   Mandante   5-1 Visitante   autores"
PLANILHA = re.compile(r"^\s*(?P<dia>\d{1,2})/(?P<mes>[a-z]{3})/(?P<ano>\d{2})\s+(?:(?P<hora>\d{1,2}:\d{2})\s+)?(?P<resto>\S.*)$", re.I)

# correções do texto da página antes da leitura, por arquivo: [(padrão, troca, motivo)] (cada coleta preenche)
CORRECOES: dict[str, list[tuple[str, str, str]]] = {}


def ler_planilha(bruta: str) -> dict | None:
    """Linha de jogo da página em planilha: data, hora, estádio (quando há), mandante, placar, visitante e autores."""
    m = PLANILHA.match(bruta)
    if not m or m["mes"].lower() not in MESES:
        return None
    resto = m["resto"]
    ms = re.search(r"(?<=\s)(\d{1,2})-(\d{1,2})(?=\s|$)", resto)
    if not ms:
        return None
    cols = [c for c in re.split(r"\s{2,}", resto[:ms.start()].strip()) if c]
    dm = re.match(r"\s*(\S.*?)(?:\s{2,}(.*))?\s*$", resto[ms.end():])
    if not cols or not dm:
        return None
    uf = lambda n: re.sub(r"\s+-\s+([A-Z]{2})$", r"-\1", n.strip())   # "Paysandu - PA" -> "Paysandu-PA"
    a = int(m["ano"])
    return {"data": f"{2000 + a if a < 50 else 1900 + a:04d}-{MESES[m['mes'].lower()]:02d}-{int(m['dia']):02d}", "hora": m["hora"] or "",
            "estadio": "  ".join(cols[:-1]), "mandante": uf(cols[-1]), "visitante": uf(dm[1]), "gm": int(ms[1]), "gv": int(ms[2]),
            "gols": (dm[2] or "").strip()}


def texto(ano: int, arquivo: str | None = None) -> str:
    """Texto puro da página (tira as tags e as entidades; tabulação vira espaços)."""
    arquivo = arquivo or MODELO.format(ano=ano)
    bruto = (PASTA / arquivo).read_bytes()
    try:
        t = bruto.decode("utf-8")
    except UnicodeDecodeError:
        t = bruto.decode("latin-1")
    t = re.sub(r"(?is)<(script|style)\b.*?</\1>", "", t)
    t = re.sub(r"(?i)<br\s*/?>", "\n", t)
    t = re.sub(r"(?i)</t[dh]>", "  ", t)   # tabela HTML (2016 em diante): a célula vira espaço e a linha vira quebra
    t = re.sub(r"(?i)</tr>", "\n", t)
    t = html.unescape(re.sub(r"<[^>]+>", "", t)).replace("\xa0", " ").replace("\r", "").replace("﻿", "")
    t = t.expandtabs(8)
    for padrao, troca, _motivo in CORRECOES.get(arquivo, []):
        t = padrao(t) if callable(padrao) else re.sub(padrao, troca, t, flags=re.M)   # função: reescreve a página inteira
    return costurar(t)


def costurar(t: str) -> str:
    """Junta linhas que a página quebrou no meio (1988): colchete ou parêntese aberto, jogo sem o
    visitante ("Treze   1-1" / "Fluminense [pen 3-2]") e linha de tabela sem os números do fim."""
    for _ in range(3):
        t = re.sub(r"\[([^\]\n]*)\n\s*(?!\[)", r"[\1 ", t)   # sem engolir a próxima linha que já abre colchete (a data)
        t = re.sub(r"\(([^)\n]*)\n\s*", r"(\1 ", t)
    linhas, saida, i = t.split("\n"), [], 0
    while i < len(linhas):
        l = linhas[i]
        jogo_sem_visitante = re.match(r"^\s*[^\d\s\[].*?\s\d{1,2}-\d{1,2}\s*$", l)
        # linha de tabela sem os números do fim (não a lista de participantes, que tem "(Cidade-UF)")
        tabela_cortada = re.match(r"^\s*\d{1,2}-[^\d\s]", l) and "(" not in l and not re.search(r"\d+-\s*\d+\s+\d+", l)
        if (jogo_sem_visitante or tabela_cortada) and i + 1 < len(linhas):
            j = i + 1
            while j < len(linhas) and not linhas[j].strip():
                j += 1
            if tabela_cortada and not jogo_sem_visitante and (j >= len(linhas) or not re.match(r"^\s*\d", linhas[j])):
                j = len(linhas)   # a próxima não continua a tabela: não junta
            if j < len(linhas):
                linhas[j] = l.rstrip() + "  " + linhas[j].strip()
                i = j
                continue
        saida.append(l)
        i += 1
    return "\n".join(saida)


def limpar_nome(nome: str) -> str:
    if "Ã" in nome:   # acento quebrado (texto em UTF-8 lido como Latin-1): "CriciÃºma"
        try:
            nome = nome.encode("latin-1").decode("utf-8")
        except UnicodeError:
            pass
    nome = re.sub(r"\s*\((?![A-Z]{2}\))[^)]*\)\s*$", "", nome)   # "(Fortaleza campeão)", "(Encerrado aos 82min)"; fica "(SP)"
    nome = re.sub(r"(?<=[A-Za-zÀ-ÿ])\d+$", "", nome)   # "Bragantino0" (erro de digitação da fonte)
    return re.sub(r"\s{2,}", " ", nome).strip(" .:*")


def nome_valido(nome: str) -> bool:
    """Descarta o que só tem cara de jogo: médias de tabela ("0,593 0,111"), linha de tabela colada
    ("10Avaí/SC 37 27"), notas de rodapé com placar no meio do texto."""
    if not 2 <= len(nome) <= 32 or "," in nome or nome[0] in "[(":
        return False
    if re.search(r"\d", nome) and not re.match(r"^\d+ de ", nome):
        return False
    return not re.search(r"\b(the|due|partida|between|match|originally|awarded|abandoned|result)\b", nome, re.I)


def inverter_pen(nota: str) -> str:
    """A nota de pênaltis da linha "A  0-0  0-0  B  [pen 2-3]" segue a ordem da linha (A-B); no jogo de volta, com B
    mandante, ela vira "pen 3-2" (mandante-visitante)."""
    return re.sub(r"(pen\w*\s*)(\d+)\s*-\s*(\d+)", lambda m: f"{m[1]}{m[3]}-{m[2]}", nota or "", flags=re.I)


def aplicar_tribunal(jogo: "Jogo") -> None:
    """Resultado dado no tribunal (awd / W.O.): "awarded 2-0 to Sta.Cruz" (placar do vencedor),
    "awarded 0-1" (mandante-visitante) ou "victory awarded to Uberaba" (sem placar)."""
    m = re.search(r"awarded\s+(\d+)-(\d+)(?:\s+to\s+([^;,\]]+))?", jogo.nota, re.I)
    if m:
        a, b, quem = int(m[1]), int(m[2]), (m[3] or "").strip()
        if quem:   # placar visto pelo vencedor
            vis = chave(quem)[:4] in chave(jogo.visitante) or chave(jogo.visitante)[:4] in chave(quem)
            jogo.gm, jogo.gv = (min(a, b), max(a, b)) if vis else (max(a, b), min(a, b))
        else:
            jogo.gm, jogo.gv = a, b


def ler(ano: int, arquivo: str | None = None) -> tuple[list[Jogo], list[Tabela]]:
    t = texto(ano, arquivo)
    linhas = t.splitlines()
    # começa depois da lista de participantes (o primeiro título de fase/grupo/rodada com jogo logo depois)
    fase, grupo, rodada, data, data2 = "Fase única", "", None, None, None
    ano_data, mes_ant = ano, 0
    jogos: list[Jogo] = []
    tabelas: list[Tabela] = []
    tab: Tabela | None = None
    ultimo: Jogo | None = None
    iniciou = False
    ficha = False   # dentro da ficha técnica de um jogo ("First leg (Dec 16, 1989):"): o placar ali repete o jogo

    def ler_data(txt: str) -> bool:
        """Aplica a data de "[Sep 12]", "[Nov 04, 12]" (ida e volta), "[09 Outubro]", "[16 Oct]" ou "[xx Oct]"."""
        nonlocal data, data2, ano_data, mes_ant, iniciou
        m = DATA.match(txt)
        if m:
            mes, dia, mes2_txt, dia2 = MESES.get(m["mes"].lower()[:3]), m["dia"], m["mes2"], m["dia2"]
            if m["ano"] and int(m["ano"]) > 31:   # "[Sep 12, 1971]" / "[Feb 2/72]" (e não o 2º dia "[Nov 04, 12]")
                a = int(m["ano"])
                ano_data = a + (1900 if 30 < a < 100 else 2000 if a < 100 else 0)
            elif m["ano"]:
                dia2, mes2_txt = m["ano"], None
        elif (mn := DATA_NUM.match(txt)):
            d_, m_, a_ = int(mn["dia"]), int(mn["mes"]), int(mn["ano"])
            if not (1 <= d_ <= 31 and 1 <= m_ <= 12):
                return False
            ano_data = a_ + (1900 if 30 < a_ < 100 else 2000 if a_ < 100 else 0)
            mes_ant, iniciou, data2 = m_, True, None
            data = f"{ano_data:04d}-{m_:02d}-{d_:02d}"
            return True
        else:
            m = DATA_PT.match(txt) or re.match(r"^\s*\[(?P<dia>\d{1,2}|xx)\s+(?P<mes>" + MES_EN + r")\]\s*$", txt, re.I)
            if not m:
                return False
            mes, dia, mes2_txt, dia2 = MESES.get(m["mes"].lower()[:3]), m["dia"], None, None
            if m.groupdict().get("ano"):
                ano_data = int(m["ano"])
        if not mes:
            return False
        # virou o ano (temporada que entra em janeiro): só de out-dez para jan-mar, e uma vez
        if mes_ant >= 10 and mes <= 3 and ano_data == ano:
            ano_data += 1
        mes_ant, iniciou = mes, True
        data = f"{ano_data:04d}-{mes:02d}-{int(dia):02d}" if dia.isdigit() and 1 <= int(dia) <= 31 else None   # "[Mar 77]": não é dia
        data2 = None
        if dia2 and 1 <= int(dia2) <= 31:
            mes2 = MESES.get((mes2_txt or m["mes"]).lower()[:3], mes)
            data2 = f"{ano_data + (1 if mes2 < mes - 4 else 0):04d}-{mes2:02d}-{int(dia2):02d}"
        return True

    for n, bruta in enumerate(linhas):
        s = bruta.strip()
        if not s:
            continue
        if re.match(r"^(first|second|third)\s+leg\s*\(|^jogo\s+(de\s+)?(ida|volta)\b|^(1st|2nd)\s+leg\s*\(", s, re.I):
            ficha = True   # ficha técnica: os placares abaixo repetem o confronto já lido
            continue
        if tab is not None and (re.match(r"^[-=_\s]+$", s) or re.match(r"^(qualified|relegated|promoted|classificad|rebaixad|eliminad)\w*\.?$", s, re.I)):
            continue   # separador ou marca dentro da tabela: a tabela continua
        if tab is not None and tab.linhas and not linha_tabela(bruta):
            tab = None   # acabou a tabela
        if s.lower().startswith("about this document"):
            break
        if re.match(r"^\s*\[(unknown|\?+|date unknown|data desconhecida)\]\s*$", s, re.I):   # data desconhecida
            data, data2, ultimo, ficha = None, None, None, False
            continue
        if ler_data(bruta):   # linha só com a data
            ultimo, ficha = None, False
            continue
        # data na mesma linha do jogo: "[16 Oct] Moto Club  2-2  Santa Cruz" (1994), "[Nov 04, 12]  A  1-1  1-1  B" (1989)
        md = re.match(r"^\s*(?P<d>\[[^\]]{3,22}\])\s+(?P<resto>\S.*\d\s*-\s*\d.*)$", bruta)
        if md and ler_data(md["d"]):
            bruta, ficha = " " + md["resto"], False
            s = bruta.strip()
        if PLACAR_X_ESPACADO:   # Paulista: "26/05/1940 Palestra Itália 2 x 2 Comercial (SP)"
            mn = re.match(r"^\s*(?P<d>\d{1,2}/\d{1,2}/\d{2,4})\s+(?P<resto>\S.*\d\s*[x-]\s*\d.*)$", bruta)
            if mn and ler_data(mn["d"]):
                bruta, ficha = " " + mn["resto"], False
                s = bruta.strip()
            bruta = re.sub(r"(?<=\s)(\d{1,2}) x (\d{1,2})(?=\s)", r"\1-\2", bruta)
        if s.startswith("[") and ultimo is not None:   # autores dos gols (podem ocupar mais de uma linha)
            ultimo.gols = (ultimo.gols + " " + s).strip()
            continue
        if ultimo is not None and ultimo.gols.startswith("[") and not ultimo.gols.endswith("]") and not JOGO.match(bruta):
            ultimo.gols += " " + s   # continuação do colchete
            continue
        if re.match(r"^(moved|postponed|rescheduled) match", s, re.I) or re.match(r"^jogos? adiados?", s, re.I):
            rodada, ultimo = None, None   # jogos adiados: são de rodadas anteriores (o importador descobre qual)
            continue
        r = RODADA.match(s)
        if r and len(s) <= 60:   # "Round 3 [Aug 12-17]": o período tem cara de placar
            rodada, ultimo, iniciou = int(r.group(1) or r.group(2)), None, True
            if (dr := re.search(r"\[[^\]]+\]", s)) and not re.search(r"\d-\d", dr[0]):   # "Round 1 [set 18]": a data vem junto
                ler_data(dr[0])
            continue
        lt = linha_tabela(bruta) if COMECA_COM_POSICAO.match(bruta) or re.match(r"^\s*\d{1,2}[^\d\s]", bruta) else None
        if lt:   # linha de tabela começa com a posição ("1." / "12-"): vale antes de jogo
            if tab is None:
                tab = Tabela(fase, grupo, "Table", linha=n)
                tabelas.append(tab)
            tab.linhas.append(lt)
            ultimo = None
            continue
        pub = None   # público no fim da linha do jogo (2005): "att: 18.865", "att: 16.194 (L1)" (L1 = jogo de ida)
        ma = re.search(r"\s+att:\s*([\d.,]+)\s*(?:\((L\d)\))?\s*$", bruta)
        if ma:
            pub = (int(re.sub(r"\D", "", ma[1])), ma[2])
            bruta = bruta[:ma.start()]
            s = bruta.strip()
        if ficha and (JOGO.match(bruta) or IDA_VOLTA.match(bruta)):
            continue   # placar repetido na ficha técnica
        me = ESPECIAL.match(bruta)   # antes do placar: a nota do tribunal ("awarded 2-0") tem cara de placar
        if me and iniciou and nome_valido(limpar_nome(me["m"])) and nome_valido(limpar_nome(me["v"])):
            ultimo = Jogo(fase, grupo, rodada, data, limpar_nome(me["m"]), limpar_nome(me["v"]), None, None,
                          (me["nota"] or "").strip(), especial=me["tipo"].lower(), linha=n)
            aplicar_tribunal(ultimo)
            if ultimo.gm is None and re.fullmatch(r"\d-wo|wo-\d", ultimo.especial):   # "0-WO": W.O. a favor do visitante
                ultimo.gm, ultimo.gv = (0, 3) if ultimo.especial.endswith("wo") else (3, 0)
                ultimo.nota = (ultimo.nota + "; " if ultimo.nota else "") + "W.O. (placar de 3-0, como na tabela publicada)"
            jogos.append(ultimo)
            continue
        m3 = TRES_JOGOS.match(bruta)
        if m3 and iniciou and not COMECA_COM_POSICAO.match(bruta):
            a, b, nota = limpar_nome(m3["m"]), limpar_nome(m3["v"]), (m3["nota"] or "").strip()
            if nome_valido(a) and nome_valido(b):
                jogos.append(Jogo(fase, grupo, rodada, data, a, b, int(m3["a1"]), int(m3["b1"]), "", linha=n))
                jogos.append(Jogo(fase, grupo, rodada, None, b, a, int(m3["b2"]), int(m3["a2"]), "", linha=n))
                ultimo = Jogo(fase, grupo, rodada, None, b, a, int(m3["b3"]), int(m3["a3"]), inverter_pen(nota), linha=n)
                jogos.append(ultimo)
                continue
        mi = IDA_VOLTA.match(bruta)
        if mi and iniciou and not COMECA_COM_POSICAO.match(bruta):
            a, b, nota = limpar_nome(mi["m"]), limpar_nome(mi["v"]), (mi["nota"] or "").strip()
            if nome_valido(a) and nome_valido(b):
                jogos.append(Jogo(fase, grupo, rodada, data, a, b, int(mi["a1"]), int(mi["b1"]), "", linha=n))
                ultimo = Jogo(fase, grupo, rodada, data2, b, a, int(mi["b2"]), int(mi["a2"]), inverter_pen(nota), linha=n)
                jogos.append(ultimo)
                if pub:
                    jogos[-2 if pub[1] != "L2" else -1].publico = pub[0]
                continue
        pl = ler_planilha(bruta)
        if pl:
            ultimo = Jogo(fase, grupo, rodada, pl["data"], limpar_nome(pl["mandante"]), limpar_nome(pl["visitante"]), pl["gm"], pl["gv"],
                          gols=pl["gols"], linha=n, hora=pl["hora"], estadio=pl["estadio"])
            jogos.append(ultimo)
            iniciou = True
            continue
        mj = JOGO.match(bruta)
        if mj and iniciou and not COMECA_COM_POSICAO.match(bruta):
            a, b = limpar_nome(mj["m"]), limpar_nome(mj["v"])
            if nome_valido(a) and nome_valido(b):
                ultimo = Jogo(fase, grupo, rodada, data, a, b, int(mj["gm"]), int(mj["gv"]), (mj["nota"] or "").strip(), linha=n)
                ultimo.publico = pub[0] if pub else None
                jogos.append(ultimo)
                continue
        if SEM_PLACAR.match(bruta) and iniciou:
            ultimo = None   # jogo ainda sem resultado na página
            continue
        ultimo = None
        # título? (curto, sem cara de frase)
        if len(s) <= 60 and not s.endswith(".") and not s.startswith(("[", "(")) and not IGNORAR_TITULO.match(s):
            r = RODADA.match(s)
            if r:
                rodada = int(r.group(1) or r.group(2)); iniciou = True
                continue
            if GRUPO.search(s):
                # "Table:" seguido do título do grupo: a tabela aberta (ainda vazia ou do grupo anterior) fecha aqui
                grupo, rodada, data, tab = s, None, None, None; iniciou = True
                continue
            if (FASE.search(s) or RODADA_COPA.search(s)) and not re.search(r"\(.*-[A-Z]{2}\)", s):
                fase, grupo, rodada, ficha, data = s, "", None, False, None; iniciou = True
                if (dt := re.search(r"\[\s*([^\]]+?)\s*\]", s)):   # "First Round [ Jul 19 and Jul 22 ]": a data vem junto
                    ler_data(f"[{dt.group(1)}]")
                    fase = s[:dt.start()].strip() or s
                continue
        if re.match(r"^(table|tabela|classifica)", s, re.I):
            tab = Tabela(fase, grupo, s, linha=n)
            tabelas.append(tab)
    return jogos, tabelas


def somar(jogos: list[Jogo]) -> dict[str, list[int]]:
    """Campanha de cada clube nos jogos, [J, V, E, D, GP, GC], com as grafias do mesmo clube juntas
    ("Moto Club" e "Moto Clube" na mesma página): a chave é o nome mais usado."""
    usos: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for j in jogos:
        for nome in (j.mandante, j.visitante):
            usos[chave(nome, estado=True)][nome] += 1
    # o mesmo clube com e sem o estado na mesma página ("Juventus-SP" no grupo, "Juventus" no mata-mata):
    # junta quando, sem o estado, só há um estado para aquele nome
    por_base: dict[str, set[str]] = defaultdict(set)
    for k in usos:
        por_base[chave(k)].add(k)
    apelido = {k: k for k in usos}
    for a in list(usos):   # "União Bandeirante" no mata-mata e "U. Bandeirante" nos grupos
        par = [b for b in usos if b != a and abreviado(chave(a, estado=True), chave(b, estado=True))]
        if len(par) == 1 and len(a) < len(par[0]) and apelido[par[0]] == par[0]:
            apelido[a] = par[0]
            for nome, n in usos[a].items():
                usos[par[0]][nome] += n
    for base, ks in por_base.items():
        com_uf = [k for k in ks if k != base]
        if base in ks and len(com_uf) == 1:
            apelido[base] = com_uf[0]
            for nome, n in usos[base].items():
                usos[com_uf[0]][nome] += n
    nome_de = {k: max(usos[apelido[k]], key=usos[apelido[k]].get) for k in apelido}
    c: dict[str, list[int]] = defaultdict(lambda: [0] * 6)
    for j in jogos:
        if j.gm is None:
            continue
        for eu, a, b in ((j.mandante, j.gm, j.gv), (j.visitante, j.gv, j.gm)):
            x = c[nome_de[chave(eu, estado=True)]]
            x[0] += 1; x[4] += a; x[5] += b
            x[1 if a > b else 2 if a == b else 3] += 1
    return c


def chave(nome: str, estado: bool = False) -> str:
    """'Atlético-GO' -> 'atletico' ('atletico go' com estado=True); 'Moto Clube' -> 'moto'
    (para casar grafias do mesmo clube na mesma página)."""
    import unicodedata
    n = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().lower()
    if not estado:
        n = re.sub(r"(?:[-/ ]+|\s*\()(?:[a-z]{2})\)?$", "", n)   # sufixo do estado ("-GO", "/GO", " GO", "(GO)")
    n = re.sub(r"[^a-z0-9]+", " ", n).strip()
    n = re.sub(r"^(?:aa|ec|sc|ac|ad|cs|ca|se|ge|fc|cr|ae|aec)\s+(?=\w{3})", "", n)   # "AA Cabofriense" -> "cabofriense"
    return re.sub(r"\s+(?:clube|club|fc|ec|sc|ac|futebol clube|esporte clube)$", "", n)


def abreviado(a: str, b: str) -> bool:
    """'u araguainense' x 'uniao araguainense', 'atl sorocaba' x 'atletico sorocaba': palavra a palavra, uma começa a outra."""
    pa, pb = a.split(), b.split()
    return len(pa) == len(pb) > 1 and pa != pb and all(x.startswith(y) or y.startswith(x) for x, y in zip(pa, pb))


def casar(nomes_tabela: list[str], nomes_jogos: set[str]) -> dict[str, str]:
    """Nome da tabela -> nome usado nos jogos, quando só um combina (igual, sem o estado, ou um começa com o outro)."""
    saida, livres = {}, set(nomes_jogos)
    for nt in nomes_tabela:
        if nt in nomes_jogos:
            saida[nt] = nt; livres.discard(nt)
    for nt in nomes_tabela:
        if nt in saida:
            continue
        k = chave(nt)
        cands = [nj for nj in livres if chave(nj) == k] or \
                [nj for nj in livres if chave(nj).startswith(k) or k.startswith(chave(nj)) or k.split()[0] == chave(nj).split()[0]] or \
                [nj for nj in livres if abreviado(k, chave(nj))] or                 [nj for nj in livres if difflib.SequenceMatcher(None, k, chave(nj)).ratio() >= 0.85]
        if len(cands) == 1:
            saida[nt] = cands[0]; livres.discard(cands[0])
    return saida


def conferir(jogos: list[Jogo], tabelas: list[Tabela]) -> list[str]:
    """Compara cada tabela publicada com os jogos lidos do mesmo grupo (ou da fase, se a tabela não tem grupo)."""
    erros = []
    for tb in tabelas:
        if not tb.linhas:
            continue
        bloco = [j for j in jogos if j.fase == tb.fase and (j.grupo == tb.grupo or not tb.grupo)]
        # tabela parcial (no meio da página) soma só os jogos de antes dela; a final pode vir antes dos jogos
        # ... e a classificação final geral soma a edição inteira
        candidatas = [somar([j for j in bloco if j.linha < tb.linha]), somar(bloco), somar(jogos)]
        melhor = None
        for soma in candidatas:
            e = []
            alias = casar([r["nome"] for r in tb.linhas], set(soma))
            for r in tb.linhas:
                x = soma.get(alias.get(r["nome"], r["nome"]))
                esperado = [r["j"], r["v"], r["e"], r["d"], r["gp"], r["gc"]]
                if x != esperado:
                    e.append(f"{tb.fase} / {tb.grupo or '-'}: {r['nome']} tabela {esperado} jogos {x}")
            if melhor is None or len(e) < len(melhor):
                melhor = e
        gp, gc = sum(r["gp"] for r in tb.linhas), sum(r["gc"] for r in tb.linhas)
        jv = (sum(r["v"] for r in tb.linhas), sum(r["d"] for r in tb.linhas))
        if melhor and (gp != gc or jv[0] != jv[1]):   # a própria tabela não fecha (gols pró x contra, vitórias x derrotas)
            melhor = [f"{x} (a tabela não fecha: GP {gp} x GC {gc}, V {jv[0]} x D {jv[1]})" for x in melhor]
        erros += melhor
    return erros


def resumo(ano: int) -> tuple[int, int, int, list[str]]:
    jogos, tabelas = ler(ano)
    erros = conferir(jogos, tabelas)
    return len(jogos), len(tabelas), sum(len(t.linhas) for t in tabelas), erros


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    PASTA, MODELO = Path(sys.argv[1]), sys.argv[2]
    anos = [int(a) for a in sys.argv[3:]] or sorted(int(re.search(r"\d{4}", p.name)[0]) for p in PASTA.glob(MODELO.replace("{ano}", "*")))
    for a in anos:
        nj, nt, nl, erros = resumo(a)
        print(f"{a}: {nj} jogos, {nt} tabelas ({nl} linhas), {len(erros)} divergências")
        if len(anos) == 1:
            for e in erros[:80]:
                print("   ", e)
