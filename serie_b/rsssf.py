"""Leitor das páginas da Série B da RSSSF Brasil (data/serie_b/rsssfbrasil/br{ano}l2.htm).

As páginas seguem, com variações, o mesmo desenho: títulos de fase ("First Phase",
"Semifinals"), de grupo ("Group A", "Zona Norte") e de rodada ("Round 3"); linhas de
data ("[Sep 12]"); jogos ("Ferroviário-CE  1-1  Ferroviário-PE  [nota]"); logo abaixo
de cada jogo, os autores dos gols entre colchetes ("[Alízio 79; Fernando 8]"); e as
tabelas de cada grupo (" 1.Ferroviário-CE   6  4  1  1  12- 7   9").

O leitor devolve os jogos com fase, grupo, rodada e data, e as tabelas publicadas,
e `conferir` compara cada tabela com a soma dos jogos lidos do mesmo grupo: é o que
diz se a página foi lida inteira e certa.

Uso: python serie_b/rsssf.py [ano ...]      (sem ano: todas, com o resumo da conferência)
"""
from __future__ import annotations

import html
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

PASTA = Path(__file__).resolve().parent.parent / "data" / "serie_b" / "rsssfbrasil"
MESES = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
MESES.update({"fev": 2, "abr": 4, "mai": 5, "ago": 8, "set": 9, "out": 10, "dez": 12})

# jogo: "Mandante  2-1  Visitante  [nota]"; o placar fica entre espaços (ou tabulação)
JOGO = re.compile(r"^\s*(?P<m>\S.*?)\s+(?P<gm>\d{1,2})\s*-\s*(?P<gv>\d{1,2})\s+(?P<v>\S.*?)\s*(?:\[(?P<nota>.*?)\]?)?\s*$")
# W.O., não jogado, abandonado: "A  awd  B [awarded 1-0]", "A  n/p  B"
ESPECIAL = re.compile(r"^\s*(?P<m>\S.*?)\s+(?P<tipo>awd|w\.o\.|wo-\d|\d-wo|wo|n/p|abd|canc)\s+(?P<v>\S.*?)\s*(?:\[(?P<nota>.*?)\]?)?\s*$", re.I)
SEM_PLACAR = re.compile(r"^\s*(?P<m>[^\[\d].*?)\s{2,}-\s{2,}(?P<v>\S.*?)\s*$")
# "[Sep 12]", "[Sep 12, 1971]", "[Feb 2/72]", e ida e volta "[Feb 2 and 9]" / "[Feb 26 and Mar 2]"
MES_EN = r"(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sep(?:t(?:ember)?)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)"
MES_PT = r"(?:jan(?:eiro)?|fev(?:ereiro)?|mar(?:ço|co)?|abr(?:il)?|mai(?:o)?|jun(?:ho)?|jul(?:ho)?|ago(?:sto)?|set(?:embro)?|out(?:ubro)?|nov(?:embro)?|dez(?:embro)?)"
DATA = re.compile(r"^\s*\[(?P<mes>" + MES_EN + r")\.?\s+(?P<dia>\d{1,2})(?:[,/ ]\s*(?P<ano>\d{2,4})(?!\d))?"
                  r"(?:\s*(?:and|e|&|,)\s*(?:(?P<mes2>" + MES_EN + r")\.?\s+)?(?P<dia2>\d{1,2})(?:/(?P<ano2>\d{2,4}))?)?[^\]]*\]\s*$", re.I)
# ida e volta numa linha: "A  1-0  0-2  B" = A 1-0 B (mando de A) e B 2-0 A (mando de B)
IDA_VOLTA = re.compile(r"^\s*(?P<m>\S.*?)\s+(?P<a1>\d{1,2})-(?P<b1>\d{1,2})\s+(?P<a2>\d{1,2})-(?P<b2>\d{1,2})\s+(?P<v>[^\d\[].*?)\s*(?:\[(?P<nota>.*?)\]?)?\s*$")
# série de três jogos (1997): "ABC  2-2  0-3  1-3  Gama" = 1º jogo com mando do primeiro, os outros dois fora
TRES_JOGOS = re.compile(r"^\s*(?P<m>\S.*?)\s+(?P<a1>\d{1,2})-(?P<b1>\d{1,2})\s+(?P<a2>\d{1,2})-(?P<b2>\d{1,2})\s+(?P<a3>\d{1,2})-(?P<b3>\d{1,2})\s+(?P<v>[^\d\[].*?)\s*(?:\[(?P<nota>.*?)\]?)?\s*$")
# data com o dia antes do mês, em português: "[09 Outubro]", "[2 de novembro]"
DATA_PT = re.compile(r"^\s*\[(?P<dia>\d{1,2})(?:\s+de)?\s+(?P<mes>" + MES_PT + "|" + MES_EN + r")\.?(?:\s+(?:de\s+)?(?P<ano>\d{4}))?\s*\]\s*$", re.I)
LINHA_TABELA = re.compile(r"^\s*(?P<pos>\d{1,2})\s*[.\-]\s*(?P<nome>\D+?)\s+(?P<j>\d+)\s+(?P<v>\d+)\s+(?P<e>\d+)\s+(?P<d>\d+)\s+(?P<gp>\d+)\s*-\s*(?P<gc>\d+)\s+(?P<pts>-?\d+)")
# 1988 (empate decidido nos pênaltis): " 1-Náutico  10  6  1/ 1  2  12- 5  21" (empates ganhos / perdidos nos pênaltis)
LINHA_TABELA_PEN = re.compile(r"^\s*(?P<pos>\d{1,2})\s*[.\-]\s*(?P<nome>\D+?)\s+(?P<j>\d+)\s+(?P<v>\d+)\s+(?P<e1>\d+)\s*/\s*(?P<e2>\d+)\s+(?P<d>\d+)\s+(?P<gp>\d+)\s*-\s*(?P<gc>\d+)\s+(?P<pts>-?\d+)")
# começa com número de posição ("1.", "12-", "3 ") e não com nome de clube que tem número ("4 de Julho")
COMECA_COM_POSICAO = re.compile(r"^\s*\d+(?!\s+de\s)(?:\s*[.\-]|\s)")
RODADA = re.compile(r"^(?:round|rodada|matchday|jornada)\s*(\d+)\b", re.I)
GRUPO = re.compile(r"^(?:group|grupo|chave|zone|zona|series|série|section|pool|módulo|modulo)\b|\b(?:zone|zona|group|grupo)\s*\(?[A-Z0-9]?\)?$", re.I)
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


@dataclass
class Tabela:
    fase: str
    grupo: str
    titulo: str
    linhas: list[dict] = field(default_factory=list)
    linha: int = 0


def texto(ano: int, arquivo: str | None = None) -> str:
    """Texto puro da página (tira as tags e as entidades; tabulação vira espaços)."""
    bruto = (PASTA / (arquivo or f"br{ano}l2.htm")).read_bytes()
    try:
        t = bruto.decode("utf-8")
    except UnicodeDecodeError:
        t = bruto.decode("latin-1")
    t = re.sub(r"(?is)<(script|style)\b.*?</\1>", "", t)
    t = re.sub(r"(?i)<br\s*/?>", "\n", t)
    t = html.unescape(re.sub(r"<[^>]+>", "", t)).replace("\xa0", " ").replace("\r", "")
    return costurar(t.expandtabs(8))


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
        if tab is not None and tab.linhas and not (LINHA_TABELA.match(bruta) or LINHA_TABELA_PEN.match(bruta)):
            tab = None   # acabou a tabela
        if s.lower().startswith("about this document"):
            break
        if ler_data(bruta):   # linha só com a data
            ultimo, ficha = None, False
            continue
        # data na mesma linha do jogo: "[16 Oct] Moto Club  2-2  Santa Cruz" (1994), "[Nov 04, 12]  A  1-1  1-1  B" (1989)
        md = re.match(r"^\s*(?P<d>\[[^\]]{3,22}\])\s+(?P<resto>\S.*\d\s*-\s*\d.*)$", bruta)
        if md and ler_data(md["d"]):
            bruta, ficha = " " + md["resto"], False
            s = bruta.strip()
        if s.startswith("[") and ultimo is not None:   # autores dos gols (podem ocupar mais de uma linha)
            ultimo.gols = (ultimo.gols + " " + s).strip()
            continue
        if ultimo is not None and ultimo.gols and not ultimo.gols.endswith("]") and not JOGO.match(bruta):
            ultimo.gols += " " + s   # continuação do colchete
            continue
        if re.match(r"^(moved|postponed|rescheduled) match", s, re.I) or re.match(r"^jogos? adiados?", s, re.I):
            rodada, ultimo = None, None   # jogos adiados: são de rodadas anteriores (o importador descobre qual)
            continue
        r = RODADA.match(s)
        if r and len(s) <= 60:   # "Round 3 [Aug 12-17]": o período tem cara de placar
            rodada, ultimo, iniciou = int(r.group(1)), None, True
            continue
        mt = LINHA_TABELA.match(bruta) or LINHA_TABELA_PEN.match(bruta)
        if mt:   # linha de tabela começa com a posição ("1." / "12-"): vale antes de jogo
            if tab is None:
                tab = Tabela(fase, grupo, "Table", linha=n)
                tabelas.append(tab)
            lt = {k: (int(v) if k != "nome" else limpar_nome(v)) for k, v in mt.groupdict().items()}
            if "e1" in lt:   # 1988: empates ganhos e perdidos nos pênaltis
                lt["e"] = lt.pop("e1") + lt.pop("e2")
            tab.linhas.append(lt)
            ultimo = None
            continue
        if ficha and (JOGO.match(bruta) or IDA_VOLTA.match(bruta)):
            continue   # placar repetido na ficha técnica
        me = ESPECIAL.match(bruta)   # antes do placar: a nota do tribunal ("awarded 2-0") tem cara de placar
        if me and iniciou and nome_valido(limpar_nome(me["m"])) and nome_valido(limpar_nome(me["v"])):
            ultimo = Jogo(fase, grupo, rodada, data, limpar_nome(me["m"]), limpar_nome(me["v"]), None, None,
                          (me["nota"] or "").strip(), especial=me["tipo"].lower(), linha=n)
            aplicar_tribunal(ultimo)
            jogos.append(ultimo)
            continue
        m3 = TRES_JOGOS.match(bruta)
        if m3 and iniciou and not COMECA_COM_POSICAO.match(bruta):
            a, b, nota = limpar_nome(m3["m"]), limpar_nome(m3["v"]), (m3["nota"] or "").strip()
            if nome_valido(a) and nome_valido(b):
                jogos.append(Jogo(fase, grupo, rodada, data, a, b, int(m3["a1"]), int(m3["b1"]), "", linha=n))
                jogos.append(Jogo(fase, grupo, rodada, None, b, a, int(m3["b2"]), int(m3["a2"]), "", linha=n))
                ultimo = Jogo(fase, grupo, rodada, None, b, a, int(m3["b3"]), int(m3["a3"]), nota, linha=n)
                jogos.append(ultimo)
                continue
        mi = IDA_VOLTA.match(bruta)
        if mi and iniciou and not COMECA_COM_POSICAO.match(bruta):
            a, b, nota = limpar_nome(mi["m"]), limpar_nome(mi["v"]), (mi["nota"] or "").strip()
            if nome_valido(a) and nome_valido(b):
                jogos.append(Jogo(fase, grupo, rodada, data, a, b, int(mi["a1"]), int(mi["b1"]), "", linha=n))
                ultimo = Jogo(fase, grupo, rodada, data2, b, a, int(mi["b2"]), int(mi["a2"]), nota, linha=n)
                jogos.append(ultimo)
                continue
        mj = JOGO.match(bruta)
        if mj and iniciou and not COMECA_COM_POSICAO.match(bruta):
            a, b = limpar_nome(mj["m"]), limpar_nome(mj["v"])
            if nome_valido(a) and nome_valido(b):
                ultimo = Jogo(fase, grupo, rodada, data, a, b, int(mj["gm"]), int(mj["gv"]), (mj["nota"] or "").strip(), linha=n)
                jogos.append(ultimo)
                continue
        if SEM_PLACAR.match(bruta) and iniciou:
            ultimo = None   # jogo ainda sem resultado na página
            continue
        ultimo = None
        # título? (curto, sem cara de frase)
        if len(s) <= 60 and not s.endswith(".") and not s.startswith("[") and not IGNORAR_TITULO.match(s):
            r = RODADA.match(s)
            if r:
                rodada = int(r.group(1)); iniciou = True
                continue
            if GRUPO.search(s):
                grupo, rodada = s, None; iniciou = True
                continue
            if FASE.search(s) and not re.search(r"\(.*-[A-Z]{2}\)", s):
                fase, grupo, rodada, ficha = s, "", None, False; iniciou = True
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
    nome_de = {k: max(v, key=v.get) for k, v in usos.items()}
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
        n = re.sub(r"[-/ ]+(?:[a-z]{2})$", "", n)   # sufixo do estado
    n = re.sub(r"[^a-z0-9]+", " ", n).strip()
    return re.sub(r"\s+(?:clube|club|fc|ec|sc|ac|futebol clube|esporte clube)$", "", n)


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
                [nj for nj in livres if chave(nj).startswith(k) or k.startswith(chave(nj)) or k.split()[0] == chave(nj).split()[0]]
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
        erros += melhor
    return erros


def resumo(ano: int) -> tuple[int, int, int, list[str]]:
    jogos, tabelas = ler(ano)
    erros = conferir(jogos, tabelas)
    return len(jogos), len(tabelas), sum(len(t.linhas) for t in tabelas), erros


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    anos = [int(a) for a in sys.argv[1:]] or sorted(int(p.name[2:6]) for p in PASTA.glob("br*l2.htm"))
    for a in anos:
        nj, nt, nl, erros = resumo(a)
        print(f"{a}: {nj} jogos, {nt} tabelas ({nl} linhas), {len(erros)} divergências")
        if len(anos) == 1:
            for e in erros[:60]:
                print("   ", e)
