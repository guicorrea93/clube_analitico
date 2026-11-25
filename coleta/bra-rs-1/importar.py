"""Junta as fontes do Campeonato Gaúcho (1ª divisão) e grava o pacote em data/coleta/bra-rs-1/pacote/ e o relatório em
docs/coleta/bra-rs-1.md. Mesmo método do Mineiro (coleta/bra-mg-1/importar.py, de onde este foi copiado).

Fontes: RSSSF Brasil (tablesr/rs{ano}.htm, 1919-2024: jogos, fases, grupos, datas e autores; as tabelas publicadas são a
conferência); ogol (calendário de cada edição e o código de cada clube, que dá a identidade; confere placares e completa
jogos; 2025 e 2026 só nele); Wikipédia (lista de campeões, segunda fonte do campeão e do vice).

A edição é a temporada ("1950"); o ano sai de temporada[:4].

Uso: python coleta/bra-rs-1/importar.py [temporada ...]     (sem temporada: todas; com temporada, só confere e não grava)
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
import clubes_rs1  # noqa: E402
import gols as gols_rsssf  # noqa: E402
import rsssf_rs1  # noqa: E402
import wiki  # noqa: E402
from edicoes import ANOS, NOME_OFICIAL, NOME_PADRAO, PACOTE, PASTA_DADOS, RELATORIO, SLUG  # noqa: E402
from rsssf_rs1 import rsssf  # noqa: E402

wiki.PASTA = PASTA_DADOS / "wikipedia"
OGOL = PASTA_DADOS / "ogol"
ESPN = PASTA_DADOS / "espn"
FONTE_RSSSF = "https://rsssfbrasil.com/tablesr/{pagina}"


def fonte_rsssf(temporada) -> str:
    from edicoes import pagina_rsssf
    return FONTE_RSSSF.format(pagina=pagina_rsssf(str(temporada)))


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
    a, b = clubes_rs1.chave(a), clubes_rs1.chave(b)
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
CORRIGE_OGOL: dict[tuple[str, str], tuple[str, str]] = {
    ("1981", "999999"): ("3468", "o calendário do ogol de 1981 traz o São Paulo de Rio Grande com um código provisório"),
    # ficha do ogol fundada depois da edição (regra da casa: clube refundado ou fusão é outro cadastro). Santo Ângelo: a
    # SER Santo Ângelo nasceu em 1989 da fusão de Santoangelense, Tamoio e Elite; antes jogava a Associação Esportiva Santo
    # Ângelo ("AE Santo Ângelo" na RSSSF de 1975; Wikipédia). São Borja: a ficha (AE São Borja) é de 2009; antes, a
    # Sociedade Esportiva São Borja (Wikipédia; as fontes discordam se é a mesma linhagem da AE: fica para a revisão)
    **{(str(_a), "3453"): ("rs:AE Santo Ângelo", "Associação Esportiva Santo Ângelo (antes da fusão de 1989)")
       for _a in range(1919, 1989)},
    **{(str(_a), "70071"): ("241325", "Sociedade Esportiva São Borja (ficha 241325 do ogol, já no cadastro pela Série C); a "
                                      "ficha que o calendário usa é a da AE São Borja, de 2009")
       for _a in range(1919, 2009)},
}


def ler_ogol(ano: int) -> list[dict]:
    f = OGOL / f"rs1_{str(ano).replace(" ", "_")}.json"
    js = json.loads(f.read_text(encoding="utf-8")) if f.exists() else []
    for o in js:
        for lado in ("mandante", "visitante"):
            if (ano, o.get(f"{lado}_id")) in CORRIGE_OGOL:
                novo = CORRIGE_OGOL[(ano, o[f"{lado}_id"])][0]
                o[f"{lado}_id"] = clubes_rs1.sem_ogol(novo[3:], inteiro=True) if novo.startswith("rs:") else novo
    return [o for o in js if o["id"] not in OGOL_IGNORAR]


def nomes_ogol(ano: int, og: list[dict]) -> dict[str, set[str]]:
    """Código do clube -> nomes que o ogol usa para ele (no calendário do ano e na ficha)."""
    fs = clubes_rs1.fichas()
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
    # anos em que o calendário do ogol tem só parte dos jogos (1987, 1988, 1996, 1999): os votos de placar e data casavam
    # o nome com outro clube
    ("1996", "GUARANY/GAR"): ("61591", "GA Guarany, de Garibaldi (\"GUARANY(GAR)\" na página)"),
    ("1999", "São José/PA"): ("3463", "EC São José, de Porto Alegre"),
    ("1988", "Internacional SM"): ("3292", "EC Internacional, de Santa Maria"),
    ("1987", "Glória"): ("3257", "GE Glória, de Vacaria"),
    ("1987", "Uruguaiana"): ("85473", "EC Uruguaiana"),
    ("1987", "Elite"): (clubes_rs1.sem_ogol("Elite"), "Elite Clube Desportivo, de Santo Ângelo (o ogol não tem)"),
}


def _nomes(destino: str, *nomes: str) -> dict[str, str]:
    return {n: destino for n in nomes}


# nomes da página -> clube, para os nomes que o casamento pelo calendário do ogol não resolve (de 1925 a 1976 o ogol não
# tem os jogos). Valor: código do ogol, ou "rs:<nome>" para um clube que o ogol não tem (todas as grafias dele num nome
# só). Mesmo clube com outro nome na mesma cidade é o mesmo clube (plano de coleta, 2.2).
NOME_CODIGO: dict[str, str] = {
    **_nomes("3365", "Floriano", "NH"),   # EC Floriano, Novo Hamburgo até 1968; "NH" nas páginas de 1937-1941 e 1987
    **_nomes("3240", "9º RI", "Grêmio 9º RI", "GA 9º RI"),   # Grêmio Atlético Farroupilha, o clube do 9º Regimento (RSSSF)
    **_nomes("3264", "Grêmio Bagé"),   # Grêmio Esportivo Bagé
    **_nomes("3280", "Guarany Bagé", "Guarany B", "Guarany/B", "Guarany de Bagé", "GUARANI BAGE", "Guarani Bagé", "Guarany (BA)",
             "Guarani(BA)", "Guarani-ba"),
    **_nomes("98375", "Guarany/CA", "Guarany CA", "Guarany (CA)", "GUARANY(CA)", "Guarani CA"),   # SC Guarany, Cruz Alta
    **_nomes("385809", "Guarani Alegrete", "Guarani/Al"),
    **_nomes("3277", "Guarani (VA)", "GUARANI (VA)", "GUARANI(VA)", "Guarani VA", "Guarani(VA)", "Guarani/VA"),
    **_nomes("61591", "Guarany/GA", "Guarani-ga", "Guarany/G"),   # GA Guarany, Garibaldi
    **_nomes("15856", "Riograndense SM", "Riograndense (SM)"),   # Riograndense FC, Santa Maria
    **_nomes("71957", "Riograndense RG", "Riograndense (RG)", "Riograndense(RG)"),   # FC Riograndense, Rio Grande
    **_nomes("3292", "Internacional (SM)", "Internacional SM", "Internacional(SM)", "Inter/SM", "Inter-sm", "Internacional/SM"),
    **_nomes("52409", "Santanense", "Grêmio Santanense", "GREMIO SANTANENSE", "Grêmio SANTANENSE", "Gremio SL", "Grêmio/SL"),
    **_nomes("gremio", "Gremio PA", "Grêmio/PA", "GRÊMIO (RS)"),
    **_nomes("internacional", "Internacional/PA", "INTERNACIONAL (RS)"),
    **_nomes("15853", "Cruzeiro-poa", "CRUZEIRO - POA"),   # EC Cruzeiro, de Porto Alegre (hoje em Cachoeirinha)
    **_nomes("24898", "XIV DE JULHO", "XIV de Julho"),
    **_nomes("3081", "XV DE NOVEMBRO", "XV de Novembro"),
    **_nomes("3157", "Brasil-P", "Brasil/P", "Brasil/PE", "BRASIL PELOTAS", "BRASIL/PEL"),
    **_nomes("11646", "Brasil F", "Brasil/F", "Brasil/FA", "BRASIL/FAR"),
    **_nomes("61591", "GUARANY/GAR"),
    **_nomes("3507", "Ulbra", "Universidade"),
    **_nomes("100771", "Torrense"), **_nomes("54506", "U. Frederiquense"), **_nomes("85473", "Uruguaiana"),
    **_nomes("2246", "Juventude de Caxias"), **_nomes("24902", "Atlético-ca"), **_nomes("36602", "Estrela"),
    **_nomes("3463", "São José-poa", "São José/PA", "São José/PoA", "São José"),   # EC São José, de Porto Alegre
    **_nomes("227344", "São José/CS"),
    # clubes só da RSSSF, com as grafias da página num nome só
    **_nomes("rs:Guarany (Cachoeira do Sul)", "Guarani Cachoeira", "Guarany Cachoeira", "Guarany Cachoeira do",
             "Guarany Cachoeira do Sul", "Guarany de Cachoeira do Sul", "Guarani Cachoeira do Sul"),
    **_nomes("rs:Riograndense (Cruz Alta)", "Riograndense CA", "Grêmio Riograndense CA"),
    **_nomes("rs:Riograndense (Passo Fundo)", "Riograndense PF"),
    **_nomes("rs:Ferro Carril", "Ferro Carril", "Ferrocarril"),
    **_nomes("rs:Tamandaré (Cachoeira do Sul)", "Tamandaré", "Tamandaré Cachoeira", "Tamandaré Cachoeira do Sul"),
    **_nomes("rs:Guarani (Minas de São Jerônimo)", "Guarani - MSJ", "Guarani MSJ", "Guarani - Minas de São Jerônimo"),
    **_nomes("rs:Couto", "Couto", "Couto FC"), **_nomes("rs:Arranca", "Arranca", "Arranca CA"),
    **_nomes("rs:Guarany (Rosário do Sul)", "Guarany de Rosário", "Guarany Rosário"),
    **_nomes("rs:General Osório", "Gen. Osório", "GS Gen. Osório"),
    **_nomes("rs:Internacional (São Borja)", "Inter-sb", "Internacional/SB"),
    **_nomes("rs:Tupy", "Tupi", "Tupy"),
    **_nomes("internacional", "Inter"),   # "Inter" (1962-1976): o Internacional; os do interior vêm com a cidade (Inter-sm, Inter-sb)
    **_nomes("3541", "Ypiranga"),   # Ypiranga FC, de Erechim
    **_nomes("24899", "Flamengo"), **_nomes("24902", "Atlético"), **_nomes("3446", "Santa Cruz"),
    **_nomes("3529", "Vec"),   # Veranópolis Esporte Clube (1995)
    **_nomes("rs:Encantado", "Encantado"), **_nomes("rs:Pratense", "Pratense"),
    **_nomes("rs:AE Santo Ângelo", "AE Santo Ângelo"),
}
# os nomes da RSSSF dos clubes separados em CORRIGE_OGOL, nos anos sem ogol
NOME_ANO_SEPARADOS = {
    **{(str(_a), _n): ("rs:AE Santo Ângelo", "antes da fusão de 1989") for _a in range(1919, 1989)
       for _n in ("Santo Ângelo", "Santo Angelo", "SANTO ÂNGELO")},
    **{(str(_a), _n): ("241325", "SE São Borja, antes da AE São Borja (2009)") for _a in range(1919, 2009)
       for _n in ("São Borja", "SÃO BORJA", "Sao Borja")},
}
# nome ambíguo numa temporada: (temporada, nome da página) -> clube (código do ogol ou "rs:<nome>"), com o motivo
NOME_ANO: dict[tuple[str, str], tuple[str, str]] = {
    # "Riograndense" sem cidade: até 1960, o FC Riograndense de Rio Grande (zona litoral; vice em 1937, 1938 e 1946 e campeão
    # em 1939 pela Wikipédia, "Rio-Grandense-RG"); de 1961 a 1976, o Riograndense de Santa Maria (a página escreve o de
    # Rio Grande "Riograndense(RG)", como em 1968)
    **{(str(_a), _n): ("71957", "FC Riograndense, de Rio Grande") for _a in range(1919, 1961)
       for _n in ("Riograndense", "RIOGRANDENSE")},
    **{(str(_a), _n): ("15856", "Riograndense FC, de Santa Maria") for _a in range(1961, 1977)
       for _n in ("Riograndense", "RIOGRANDENSE")},
    # "Guarany" sem cidade, até 1960: o de Bagé; em 1943, o de Cachoeira do Sul (vice pela Wikipédia, "Guarany-CS")
    **{(str(_a), _n): ("3280", "Guarany FC, de Bagé") for _a in range(1919, 1961) for _n in ("Guarany", "GUARANY")},
    ("1943", "Guarany"): ("rs:Guarany (Cachoeira do Sul)", "vice de 1943 pela Wikipédia: Guarany-CS"),
    **{(str(_a), "Guarani"): ("385809", "Guarani FC, de Alegrete (vice em 1931 pela Wikipédia)") for _a in range(1919, 1961)},
    **{(str(_a), "Nacional"): ("rs:Nacional (São Leopoldo)", "Nacional de São Leopoldo (\"Nacional - São Leopoldo\" em 1926)")
       for _a in range(1919, 1961)},
    ("1926", "Nacional - São Leopoldo"): ("rs:Nacional (São Leopoldo)", "Nacional de São Leopoldo"),
    # "Cruzeiro" sem cidade: o de Porto Alegre, menos nos anos em que é o EC Cruzeiro de São Gabriel (participantes da RSSSF
    # em 1955 e 1959; em 1956, o mesmo clube da zona da fronteira)
    **{(_a, _n): ("rs:Cruzeiro (São Gabriel)", "EC Cruzeiro, de São Gabriel (participantes da RSSSF)")
       for _a in ("1955", "1956", "1959") for _n in ("Cruzeiro", "CRUZEIRO")},
    **{(str(_a), _n): ("15853", "EC Cruzeiro, de Porto Alegre") for _a in range(1919, 1977) for _n in ("Cruzeiro", "CRUZEIRO")
       if str(_a) not in ("1955", "1956", "1959")},
}
NOME_ANO.update(NOME_ANO_SEPARADOS)
# jogos do calendário do ogol que estão errados (a RSSSF e a tabela publicada mostram outro jogo): código do jogo -> motivo
OGOL_IGNORAR: dict[str, str] = {}
# jogos da RSSSF que ficam de fora: (ano, nome do clube) -> motivo
RSSSF_FORA: dict[tuple[str, str], str] = {}
# jogos da RSSSF anulados: (ano, mandante, visitante, gols, gols) como na página -> motivo
JOGOS_ANULADOS: dict[tuple, str] = {}


def mapear_nomes(ano: int, rs: list, og: list[dict], log: list[str]) -> dict:
    """Nome na RSSSF -> código do ogol, por grupo: a mesma página às vezes usa o mesmo nome curto para clubes
    diferentes em grupos diferentes ("Esportivo" de Bento Gonçalves e de Passos em 1988).
    Cada jogo da RSSSF vota nos jogos do ogol de mesmo placar e data próxima (o voto pesa mais quando os nomes
    parecem); depois, dentro de cada grupo, um para um, do par mais votado para o menos.
    Devolve chaves (nome, fase, grupo) e, para as tabelas gerais, o nome sozinho."""
    noms = nomes_ogol(ano, og)
    fs = clubes_rs1.fichas()
    cache: dict[tuple, float] = {}
    def sim(n, i):
        """Parecença do nome; a UF escrita no nome da RSSSF ("São José(RS)") desempata homônimos."""
        if (n, i) not in cache:
            s = max((_sim(n, x) for x in noms.get(i, ()) if x), default=0)
            uf_n, uf_i = clubes_rs1.separar_uf(n.replace("(", " (").strip())[1], fs.get(i, {}).get("uf")
            if uf_n and uf_i:
                s = s * 0.6 if uf_n != uf_i else min(1.0, s + 0.05)
            cache[(n, i)] = s
        return cache[(n, i)]
    nomes_todos = {x for j in rs for x in (j.mandante, j.visitante)}
    sem_uf = lambda n: re.sub(r"\s*\([A-Z]{2}\)$", "", n).strip()   # "Betim (MG)" vale como "Betim"
    por_base = {sem_uf(n): v[0] for (a, n), v in NOME_MANUAL.items() if a == ano}
    manual = {n: por_base[sem_uf(n)] for n in nomes_todos if sem_uf(n) in por_base}
    # as tabelas de nomes dadas à mão (NOME_ANO, NOME_CODIGO) valem antes do casamento pelo ogol ("Grêmio/SL" de 1995 é
    # o Grêmio Santanense, não o Grêmio)
    por_norma = {clubes_rs1.norm(k): v for k, v in NOME_CODIGO.items()}
    for n in nomes_todos - set(manual):
        destino = (NOME_ANO.get((str(ano), n)) or (None,))[0] or por_norma.get(clubes_rs1.norm(n))
        if destino:
            manual[n] = clubes_rs1.sem_ogol(destino[3:], inteiro=True) if destino.startswith("rs:") else destino
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
            # nome igual ao de um clube só do calendário (âncora quase exata) não troca por voto: em 1977 as datas da
            # página estão uma semana antes das do ogol, e os votos de placar e data casavam nomes errados
            palavras = lambda s: set(clubes_rs1.norm(s).split()) - {"ec", "fc", "sc", "ac", "ge", "ga", "de", "do", "da"}
            firme = n in ancora and sim(n, ancora[n]) >= 0.95 and not any(
                palavras(n) & palavras(fs.get(i, {}).get("curto") or "") for i in noms if i != ancora[n])
            if melhor and melhor != base and n not in manual and not firme and votos[melhor] >= 4 and \
                    votos[melhor] >= 3 * votos.get(base, 0):
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
                    estadio=j.estadio or None, publico=j.publico, fonte=fonte_rsssf(ano), gols_texto=j.gols, obs=j.nota, linha=j.linha)
        p.pen_m, p.pen_v = penaltis(f"{j.nota} {j.gols}")
        if j.gm is None and j.especial in ("awd", "dns"):
            # W.O. sem placar ("A awd B [W.O.: victory awarded to A]"): vitória sem gols (D-15), pelo nome da própria página
            mw = re.search(r"awarded(?:\s+[\d-]+)?\s+to\s+(.+?)(?:[;,\]]|$)", j.nota or "")
            if mw:
                sm, sv = _sim(mw.group(1).strip(), j.mandante), _sim(mw.group(1).strip(), j.visitante)
                if max(sm, sv) >= 0.5 and sm != sv:
                    p.especial = "wo-m" if sm > sv else "wo-v"
                    venc = nome(m if sm > sv else v)
                    resto = [x.strip() for x in re.split(r";", re.sub(r"(?:W\.O\.:\s*)?(?:score unknown;\s*)?victory awarded to [^;\]]+",
                                                                      "", j.nota)) if x.strip(" ;")]
                    p.obs = "; ".join([f"placar desconhecido: vitória do {venc} (a página diz só quem venceu; conta como "
                                       f"vitória sem gols, como o W.O.)" if "score unknown" in j.nota else f"W.O.: vitória do {venc}",
                                       *resto])
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
        if p.gm is None and p.especial in ("wo-m", "wo-v"):   # W.O. sem placar: vitória sem gols (wo_do_ogol)
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


def wo_do_ogol(ano, partidas: list[Partida], og: list[dict], tabs: list[tuple], log: list[str]) -> None:
    """Jogos que o ogol traz como "WO", sem placar e sem dizer quem venceu (anos antigos e de ligas rivais), e que a RSSSF
    não tem. O vencedor sai da tabela publicada: o clube com vitórias a mais na tabela do que nos jogos, contra o clube com
    derrotas a mais. Conta como vitória sem gols (como na tabela). Sem como decidir, o jogo fica fora (e vai para o log)."""
    wos = []
    for o in og:
        if o.get("resultado") != "WO" or not (o.get("mandante_id") and o.get("visitante_id")):
            continue
        m, v = o["mandante_id"], o["visitante_id"]
        if any({p.mandante, p.visitante} == {m, v} and p.data and o["data"] and abs(_dia(p.data) - _dia(o["data"])) <= 3
               for p in partidas):
            continue
        wos.append(o)
    if not wos:
        return
    # a tabela publicada com mais clubes da edição (a classificação geral)
    geral = max(tabs, key=lambda x: len(x[1]), default=None)
    linhas = geral[1] if geral else {}
    camp = campanha(partidas)
    falta_v = {c: x[1] - camp[c][1] for c, x in linhas.items()}
    falta_d = {c: x[3] - camp[c][3] for c, x in linhas.items()}
    pendentes = list(wos)
    while pendentes:
        decididos = []
        for o in pendentes:
            m, v = o["mandante_id"], o["visitante_id"]
            ganha_m = falta_v.get(m, 0) > 0 and falta_d.get(v, 0) > 0
            ganha_v = falta_v.get(v, 0) > 0 and falta_d.get(m, 0) > 0
            if ganha_m == ganha_v:
                continue
            venc, perd = (m, v) if ganha_m else (v, m)
            falta_v[venc] -= 1
            falta_d[perd] -= 1
            fase, grupo = fase_do_ogol(o, partidas)
            partidas.append(Partida(ano, fase, grupo, o.get("rodada"), o["data"], m, v, None, None, especial="wo-m" if ganha_m else "wo-v",
                                    fonte="ogol", fonte_id=f"ogol:{o['id']}", ogol_fase=o["fase"],
                                    obs=f"W.O.: vitória do {nome(venc)} (o ogol não diz o vencedor; vencedor pela tabela publicada)"))
            log.append(f"{ano}: W.O. do ogol incluído: {nome(m)} x {nome(v)} ({o['data']}), vitória do {nome(venc)} pela tabela publicada")
            decididos.append(o)
        if not decididos:
            break
        pendentes = [o for o in pendentes if o not in decididos]
    for o in pendentes:
        log.append(f"{ano}: W.O. do ogol sem vencedor que a tabela publicada decida, fica de fora: {o['mandante']} x {o['visitante']} ({o['data']})")


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
        if p.fonte_id:
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
        elif p.gm is None and alt[0] is not None and p.especial not in ("wo-m", "wo-v"):
            p.gm, p.gv = alt   # W.O. (e "bt", vitória sem placar conhecido) fica sem gols (D-15); o ogol grava 1-0
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
        # mesmo jogo, mesmo dia e mês, ano diferente (1979: "19.08.78" num jogo de agosto de 1979)
        ano_errado = [p for p in sobra if (p.mandante, p.visitante) == (m, v) and (p.gm, p.gv) == (gm, gv) and p.data
                      and o["data"] and p.data[4:] == o["data"][4:] and p.data[:4] != o["data"][:4]]
        if len(ano_errado) == 1:
            p = ano_errado[0]
            usados.add(o["id"]); sobra.remove(p)
            log.append(f"{ano}: ano errado na data da RSSSF — {nome(m)} {gm}-{gv} {nome(v)}: RSSSF {p.data}, ogol {o['data']}; "
                       f"fica a do ogol")
            p.data, p.fonte_id, p.ogol_fase = o["data"], f"ogol:{o['id']}", o["fase"]
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
    # anos com torneio à parte que o calendário do ogol traz junto (rsssf_rs1.ANOS_A_PARTE; no Gaúcho, nenhum por ora):
    # depois da 1ª fase, jogo só do ogol fica de fora quando é um jogo do torneio na página da RSSSF, quando os dois
    # clubes jogaram o torneio ou quando nenhum dos dois está no mata-mata do campeonato
    fim_1a, mata = None, set()
    # disputa do 3º lugar (só no ogol): jogo entre os dois clubes que perderam as semifinais
    na_semi = {x for p in partidas if fase_pt(p.fase) == "Semifinal" for x in (p.mandante, p.visitante)}
    na_final = {x for p in partidas if fase_pt(p.fase) == "Final" for x in (p.mandante, p.visitante)}
    perdedores_semi = na_semi - na_final if len(na_semi - na_final) == 2 and len(na_final) == 2 else set()
    trof_pares, trof_clubes = TROFEU.get(str(ano), (set(), set()))
    if rs_ok and int(str(ano)[:4]) in rsssf_rs1.ANOS_A_PARTE and partidas:
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
            log.append(f"{ano}: jogo do torneio à parte no ogol "
                       f"(torneio à parte), fica de fora: "
                       f"{nome(m)} {o['gols_mandante']}-{o['gols_visitante']} {nome(v)} ({o['data']})")
            continue
        fase, grupo = fase_do_ogol(o, partidas)
        if {m, v} == perdedores_semi:   # 2022: Caldense x Athletic, que a página não traz
            fase, grupo = "Disputa do 3º lugar", ""
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
    f = ESPN / f"rs1_{str(ano).replace(" ", "_")}.json"
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
    # turnos (com as grafias das páginas) e fases com outro nome (vindos do Paulista; os do Mineiro, abaixo)
    (r"^final table", "Primeira fase"),   # 1996: os jogos do 1º turno vêm sob o título da tabela final
    (r"^(1º|1o\.?|1ª|primeiro)\s*turno\s*-\s*qualifying", "1º Turno - Classificatória"),
    (r"^(2º|2o\.?|segundo)\s*turno\s*-\s*qualifying", "2º Turno - Classificatória"),
    (r"^(2º|2o\.?|segundo)\s*turno\s*-\s*1st phase", "2º Turno - 1ª fase"),
    (r"^(2º|2o\.?|segundo)\s*turno\s*-\s*2nd phase", "2º Turno - 2ª fase"),
    (r"^(1º|1o\.?|1ª|primeiro)\s*turno", "1º Turno"), (r"^(2º|2o\.?|segundo)\s*turno", "2º Turno"),
    (r"^phase 1$", "Primeira fase"), (r"^phase 2$", "Segunda fase"), (r"^phase 3$", "Terceira fase"),
    (r"^repescagem", "Repescagem"), (r"relegation", "Torneio de rebaixamento"),
    # Mineiro: torneio de classificação (1958-1973), a liga depois dele ("LEAGUE"), "1st Stage" / "2nd Stage" (1951, 1995-2000)
    (r"^qualif\w* stage tiebreak", "Fase classificatória - Desempate"), (r"^qualif", "Fase classificatória"),
    (r"^league$", "Primeira fase"), (r"^1st stage", "Primeira fase"), (r"^2nd stage", "Segunda fase"),
    (r"^third stage", "Terceira fase"),
    (r"^preliminary", "Fase preliminar"),
    # Gaúcho: títulos em português das páginas antigas
    (r"^fase preliminar", "Fase preliminar"), (r"^(turno único|quadrangular em turno único)", "Primeira fase"),
    (r"^1\.?\s*fase", "Primeira fase"), (r"^(triangular|quadrangular)( final)?$", "Fase final"),
    (r"^decis[ãa]o$", "Final"),
    (r"^jogo e.tra/final primeiro turno", "1º Turno - Final"), (r"^terceiro turno", "3º Turno"),
    (r"^(1|10|1\.|1º|1a|1o|1\*|1\"|primeiro)\s*\.?\s*\"?\s*turno$|^turno$", "1º Turno"),
    (r"^(2|20|2\.|2º|2\"|2a|2o|2Â°|segundo)\s*\.?\s*\"?\s*turno$|^returno$", "2º Turno"),
    (r"^\"miss[õo]es\" group first place playoff", "Primeira fase - Desempate"),
    (r"^-?\s*série a - segunda fase|^2 fase$", "Segunda fase"), (r"^(championship tournament)$", "Fase final"),
    (r"^championship playoff$", "Final"), (r"^(classification phase|fase constitutiva)$", "Primeira fase"),
    (r"^decis[ãa]o da quarta vaga$", "Desempate da vaga"), (r"^decagonal", "Segunda fase"),
    (r"^decis[ãa]o do segundo lugar$", "Desempate do vice"), (r"^decis[ãa]o do terceiro lugar$", "Disputa do 3º lugar"),
    (r"^(first place decision|first stage decision)$", "Primeira fase - Final"),
    (r"torneio da morte|^losers group - repescagem", "Torneio de rebaixamento"),
    (r"^(todos contra todos|resultados - primeira fase|geral primeira fase|first round - first phase|first round$|"
     r"first sub-stage)", "Primeira fase"),
    (r"^first round - second phase", "Segunda fase"), (r"^preliminar phase", "Fase preliminar"),
    (r"^hexagonal", "Fase final"),
    (r"tie-?break.*second stage", "Segunda fase - Desempate"), (r"tie-?break.*third stage", "Terceira fase - Desempate"),
    (r"second place playoff", "Desempate do vice"),
    (r"decide which team would be eliminated", "Desempate"), (r"1995 - final fase", "Fase final"),
    (r"^semfinals?$", "Semifinal"), (r"^final playoff", "Final"), (r"^classifica[çc][ãa]o final", "Fase final"),
    # 1977: três turnos, os dois primeiros com semifinal e final próprias
    (r"^first stage - first phase", "1º Turno"), (r"^first stage - semi", "1º Turno - Semifinal"),
    (r"^first stage - final", "1º Turno - Final"), (r"^second stage - first phase", "2º Turno"),
    (r"^second stage - semi", "2º Turno - Semifinal"), (r"^second stage - final", "2º Turno - Final"),
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
    if n in ORDEM:   # já em português (rsssf_rs1.FASE_ANO)
        return n
    for padrao, pt in FASES_PT:
        if re.search(padrao, n, re.I):
            return pt
    return n


# nome da RSSSF -> código do ogol, de todas as temporadas já lidas (o mesmo clube em anos sem calendário no ogol)
JA_CASADOS: dict[str, str] = {}
# temporada -> (pares de clubes, clubes) dos jogos do Troféu do Interior na página da RSSSF (2017-2022)
TROFEU: dict[str, tuple[set, set]] = {}


def completar_sem_ogol(ano, mapa: dict, rs: list, og: list, log: list[str]) -> None:
    """Nomes da RSSSF sem clube no ogol daquela temporada: usa o clube do mesmo nome em outra temporada do Gaúcho;
    se nunca apareceu, vira clube só da RSSSF ("rs-..."), com o nome da página."""
    base = lambda s: re.sub(r"\b(?:f c|e c|a c|s c|g s|aa|ec|fc|ac|sc|cr|ge|rj)\b", " ", clubes_rs1.norm(s)).split()
    for n, i in list(mapa.items()):
        if isinstance(n, str):
            JA_CASADOS.setdefault(clubes_rs1.norm(n), i)
            JA_CASADOS.setdefault(" ".join(base(n)), i)   # "PALMEIRAS" e "Palmeiras"; "Barra Mansa FC" e "Barra Mansa"
    sem = sorted({x for j in rs for x in (j.mandante, j.visitante)} - {n for n in mapa if isinstance(n, str)})
    fs = clubes_rs1.fichas()
    # clubes do calendário do ogol deste ano ainda sem nome da RSSSF: o nome da página parecido, quando é um só
    usados = {i for k, i in mapa.items() if isinstance(k, str)}
    noms = nomes_ogol(ano, og)
    # nomes da página já casados com cada código (segunda grafia do mesmo clube na página: "RIACHUELO F. C" e "Riachuelo")
    for k, i in mapa.items():
        if isinstance(k, str) and i in noms:
            noms[i] = noms[i] | {k}
    def bate(a: str, b: str) -> bool:
        """As palavras do nome mais curto (sem siglas) estão todas no outro: "Riachuelo" e "Riachuelo-RJ" sim; "Americano FC" e
        "América" não."""
        ta, tb = set(base(a)), set(base(b))
        return bool(ta and tb) and (ta <= tb or tb <= ta)
    for n in list(sem):
        cands = [i for i, ns in noms.items() if any(bate(n, x) for x in ns if x)]
        livres = [i for i in cands if i not in usados]
        # um só clube do calendário com esse nome: o que ainda não tem nome da página, senão a segunda grafia do mesmo clube
        i = livres[0] if len(livres) == 1 else cands[0] if len(cands) == 1 else None
        if i:
            mapa[n] = i
            usados.add(i)
            sem.remove(n)
            log.append(f"{ano}: {n} — casado pelo nome com o clube do calendário do ogol deste ano ({nome(i)})")
    por_norma = {clubes_rs1.norm(k): v for k, v in NOME_CODIGO.items()}
    for n in list(sem):   # tabelas de nomes dadas à mão (NOME_ANO, NOME_CODIGO)
        destino = (NOME_ANO.get((str(ano), n)) or (None,))[0] or por_norma.get(clubes_rs1.norm(n))
        if destino:
            mapa[n] = clubes_rs1.sem_ogol(destino[3:], inteiro=True) if destino.startswith("rs:") else destino
            sem.remove(n)
            log.append(f"{ano}: {n} — casado à mão ({nome(mapa[n])})")
    for n in sem:
        i = JA_CASADOS.get(clubes_rs1.norm(n)) or JA_CASADOS.get(" ".join(base(n)))
        if not i:   # o mesmo nome numa ficha do ogol (clube de temporadas lidas mais adiante: Atlético Sorocaba em 2003)
            achados = [k for k, f in fs.items() if not k.startswith("rs-") and clubes_rs1.norm(n) in
                       {clubes_rs1.norm(x) for x in (f.get("curto"), *f.get("nomes_ogol", [])) if x}]
            if not achados:   # sem as siglas e a caixa alta ("PALMEIRAS" de 1919 = "Palmeiras-RJ", que o ogol tem de 1920 em diante)
                achados = [k for k, f in fs.items() if not k.startswith("rs-") and base(n) and " ".join(base(n)) in
                           {" ".join(base(x)) for x in (f.get("curto"), *f.get("nomes_ogol", [])) if x}]
            i = achados[0] if len(achados) == 1 else None
        if i:
            mapa[n] = i
            log.append(f"{ano}: {n} — sem calendário no ogol nesta temporada; é o clube do mesmo nome em outras temporadas ({nome(i)})")
        else:
            mapa[n] = clubes_rs1.sem_ogol(n)
            JA_CASADOS[clubes_rs1.norm(n)] = mapa[n]
            JA_CASADOS.setdefault(" ".join(base(n)), mapa[n])   # "Paduano EC" (1992) = "Paduano" (1991)
            log.append(f"{ano}: {n} — clube que o ogol não tem; entra só pela RSSSF")
    for j in rs:   # chaves por grupo, como as de mapear_nomes
        for n in (j.mandante, j.visitante):
            mapa.setdefault((n, j.fase, j.grupo), mapa.get(n))


def nome(cid: str) -> str:
    return clubes_rs1.exibicao().get(cid, {}).get("clube", cid)


# --------------------------------------------------------------------------------------------- classificação

def pontos_vitoria(ano) -> int:
    return 3 if int(str(ano)[:4]) >= 1995 else 2


def ajustes_wiki(ano: int, ids_do_ano: set[str]) -> dict[str, int]:
    """Punições de pontos na Wikipédia em inglês (adjust_points), com o nome casado ao código do ogol."""
    saida = {}
    fs = clubes_rs1.exibicao()
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
    ordem_fase: dict[str, int] = {}
    for p in partidas:
        ordem_fase.setdefault(p.fase, 0 if p.fase in FORA_DO_ALCANCE else TURNO_ALCANCE.get(p.fase, ORDEM.get(p.fase, 50)))
    alcance: dict[str, int] = defaultdict(int)
    for p in partidas:
        for c in (p.mandante, p.visitante):
            alcance[c] = max(alcance[c], ordem_fase[p.fase])
    final = [p for p in partidas if p.fase == "Final"]
    vice = None
    if campeao and final:
        fin = {x for p in final for x in (p.mandante, p.visitante)} - {campeao}
        vice = next(iter(fin)) if len(fin) == 1 else None
    if campeao and vice is None and VICES_WIKI.get(str(ano)):
        # sem final de dois clubes, o vice segue a Wikipédia (a RSSSF não traz o vice do Gaúcho); a soma dos pontos de
        # fases diferentes não dá o vice oficial
        oficial = campeao_oficial(ano, partidas, {}, VICES_WIKI)
        if oficial and oficial != campeao:
            vice = oficial
            log.append(f"{ano}: vice pela Wikipédia (sem final de dois clubes): {nome(vice)}")
    def pts(c):
        x = camp[c]
        return pv * x[1] + x[2] + ajustes.get(c, 0)
    # pontos sem a fase classificatória e o torneio de rebaixamento (que só parte dos clubes jogou): desempatam antes do
    # total (1921: o Luzitano, que jogou o torneio eliminatório, passava o Atlético, vice)
    camp_nivel = campanha([p for p in partidas if ordem_fase[p.fase] >= 1])
    def pts_nivel(c):
        x = camp_nivel.get(c)
        return pv * x[1] + x[2] if x else 0
    def chave(c):
        x = camp[c]
        return (c != campeao, c != vice, -alcance[c], -pts_nivel(c), -pts(c), -x[1], -(x[4] - x[5]), -x[4], nome(c))
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
         # os turnos e as suas semifinais e finais ficam juntos na 1ª fase (do 3º lugar em diante vale a soma dos pontos);
         # a fase preliminar vem antes
         "Fase preliminar": 0.5, "1º Turno": 1, "1º Turno - Semifinal": 1.3, "1º Turno - Final": 1.6, "2º Turno": 2,
         "2º Turno - Semifinal": 2.3, "2º Turno - Final": 2.6, "3º Turno": 3, "Primeira fase - Desempate": 1.5,
         "Torneio de rebaixamento": 2.8,
         # Mineiro: o torneio de classificação (1958-1973) vem antes de tudo; desempates logo depois da sua fase; a final
         # entre os vencedores dos turnos de 1983 depois dos turnos
         "Fase classificatória": 0.5, "Fase classificatória - Desempate": 0.6, "Segunda fase - Desempate": 2.5,
         "Primeira fase - Final": 2.9, "Disputa do 3º lugar": 8.5,
         # Gaúcho até 1960: as decisões de zona e região vêm antes da fase estadual; 2009-2013: quartas de cada turno
         "Fase regional": 0.4, "1º Turno - Quartas de final": 1.2, "2º Turno - Quartas de final": 2.2,
         "Repescagem": 2.7, "Terceira fase - Desempate": 3.5,
         # desempate do 2º lugar, fora da tabela (plano de coleta, 2.2: o nome começa por "Desempate")
         "Desempate do vice": 9.5, "Desempate da vaga": 1.5}
# fases que não são avanço na classificação: quem as joga fica com a fase anterior (o torneio de rebaixamento)
FORA_DO_ALCANCE = {"Torneio de rebaixamento", "Repescagem"}
# turnos: valem como a 1ª fase para a fase alcançada (a ordem entre eles sai dos pontos)
TURNO_ALCANCE = {"1º Turno": 1, "1º Turno - Semifinal": 1, "1º Turno - Final": 1, "2º Turno": 1, "2º Turno - Semifinal": 1,
                 "2º Turno - Final": 1, "3º Turno": 1, "Primeira fase - Desempate": 1,
                 "Fase classificatória - Desempate": 0.5, "Segunda fase - Desempate": 2, "Primeira fase - Final": 1,
                 "Fase regional": 0.4, "1º Turno - Quartas de final": 1, "2º Turno - Quartas de final": 1,
                 "Terceira fase - Desempate": 3, "Desempate do vice": 9, "Desempate da vaga": 1}


# --------------------------------------------------------------------------------------------- uma edição

# temporada -> vice pela Wikipédia (tabela de resultados), para a conferência do vice; campeoes() preenche
VICES_WIKI: dict[str, str] = {}
# temporada -> vice pela lista da RSSSF (o Gaúcho não tem); campeoes() preenche
VICES_RSSSF: dict[str, str] = {}

# campeão que a lista da RSSSF não traz: temporada -> (nome, motivo)
CAMPEOES_MANUAIS: dict[str, tuple[str, str]] = {}
# títulos divididos (D-07): temporada -> clubes campeões; o 1º fica em campeao e o outro na coluna co_campeao de
# edicoes.csv (formato do agente 1, 23/11)
CAMPEOES_DIVIDIDOS: dict[str, list[str]] = {}
# edição sem vice (vazio em edicoes.csv): temporada -> motivo
SEM_VICE: dict[str, str] = {}
# observação de cada edição (coluna "observacao" de edicoes.csv)
OBS_EDICAO: dict[str, list[str]] = {
    "1930": ["organizado pela FAGET (Federação Atlética Gaúcha de Esportes Terrestres): a FRGD não conseguiu organizar o "
             "seu campeonato"],
}


def _sem_cidade(n: str) -> str:
    """"Grêmio Foot-ball Porto Alegrense (Porto Alegre)" -> "Grêmio Foot-ball Porto Alegrense"."""
    return re.sub(r"\s*[\(\[].*$", "", n).strip()


def campeoes() -> tuple[dict[str, str], dict[str, str]]:
    """Campeões pela RSSSF (rscamp.htm): temporada -> nome completo ("1919 - Grêmio Esportivo Brasil (Pelotas)"; 1923 e
    1924 "Não foi disputado"). E pela Wikipédia (artigo do Campeonato Gaúcho, "Lista de campeões": edição, ano, campeão,
    vice, 3º, 4º, artilheiro, gols; os clubes em predefinições "{{Futebol Grêmio|cidade=antes}}"): temporada -> campeão;
    o vice vai em VICES_WIKI. A RSSSF não traz o vice."""
    rs: dict[str, str] = {}
    for l in rsssf.texto(0, "rscamp.htm").splitlines():
        m = re.match(r"^\s*(\d{4})\s*-\s*(.+?)\s*$", l)
        if m and not re.search(r"(?i)n[ãa]o foi disputado", m.group(2)):
            rs.setdefault(m.group(1), _sem_cidade(m.group(2)))
    rs.update({t_: n for t_, (n, _) in CAMPEOES_MANUAIS.items()})
    wk: dict[str, str] = {}
    f = PASTA_DADOS / "wikipedia" / "pt_lista.txt"
    if f.exists():
        tab = f.read_text(encoding="utf-8").split("== Lista de campeões ==", 1)
        corpo = tab[1].split("\n|}", 1)[0] if len(tab) > 1 else ""
        def limpa(c):
            c = re.sub(r"^[^|\[{]*=[^|\[{]*\|", "", c)   # atributo da célula ('bgcolor="#ADD8E6"|Grêmio')
            c = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>|<small>.*?</small>|\[\[(?:Imagem|Ficheiro|File):[^\]]*\]\]|'{2,}|"
                       r"\{\{\s*Ref[_ ]label[^}]*\}\}", "", c)
            c = re.sub(r"\{\{\s*[Ff]utebol\s+([^}|]+?)\s*(?:\|[^}]*)?\}\}", r"\1", c)
            return re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", c).strip()
        for linha in corpo.split("\n|-"):
            cel = [c.strip() for c in linha.split("\n|")[1:]]
            if len(cel) < 4:
                continue
            ano = re.match(r"(\d{4})$", limpa(cel[1]))
            if not ano or ano.group(1) not in ANOS:
                continue
            wk[ano.group(1)] = limpa(cel[2].split("<br")[0])
            vice = limpa(cel[3].split("<br")[0])
            if vice and not re.match(r"(?i)não houve|—|-$", vice):
                VICES_WIKI[ano.group(1)] = vice
    return rs, wk


def montar_edicao(ano: int, log: list[str], rs_campeoes: dict, wk_campeoes: dict) -> dict:
    rs, tabelas = rsssf_rs1.ler(ano) if rsssf_rs1.tem_pagina(ano) else ([], [])
    fora_total = []   # tirados aqui também saem do ogol (mesmo_jogo_tirado)
    for (a, n), motivo in RSSSF_FORA.items():
        if a == ano:
            fora = [j for j in rs if n in (j.mandante, j.visitante)]
            rs = [j for j in rs if j not in fora]
            fora_total += fora
            log.append(f"{ano}: {len(fora)} jogos do {n} ficam de fora: {motivo}")
    for (a, m, v, gm, gv), motivo in JOGOS_ANULADOS.items():
        if a == ano:
            fora = [j for j in rs if (j.mandante, j.visitante, j.gm, j.gv) == (m, v, gm, gv)]
            rs = [j for j in rs if j not in fora]
            fora_total += fora
            log.append(f"{ano}: jogo anulado fica de fora ({len(fora)}): {m} {gm}-{gv} {v} — {motivo}")
    for i, motivo in OGOL_IGNORAR.items():
        if motivo.startswith(str(ano)):
            log.append(f"{ano}: jogo do ogol ignorado — {motivo[6:]}")
    # jogos anulados ou cancelados (rsssf_rs1.ANULADOS): já saíram da leitura; ficam no relatório
    tirados = list(rsssf_rs1.ANULADOS.get(str(ano), []))
    for j in tirados:
        log.append(f"{ano}: jogo anulado ou cancelado fica de fora: {j.mandante} {j.gm if j.gm is not None else ''}-"
                   f"{j.gv if j.gv is not None else ''} {j.visitante} ({j.data}) [{j.nota}]")
    # D-04 a: repescagem contra clube de fora da divisão (o campeão da 2ª divisão) fica só na observação da edição
    tirados += repescagem_fora(ano, rs, log) + fora_total
    rs = [j for j in rs if j not in tirados]
    og = [o for o in ler_ogol(ano) if not mesmo_jogo_tirado(o, tirados, ano, log)]
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
    # o mesmo nome curto para os dois clubes do jogo ("Inter 2-3 Inter" em 1987, "Grêmio 7-0 Grêmio" em 1995): valem os
    # dois clubes do jogo do ogol de mesma data (até 1 dia) e mesmo placar, quando um dos dois é o clube casado
    for p in partidas:
        if p.mandante != p.visitante:
            continue
        achados = [o for o in og if o.get("mandante_id") and o.get("visitante_id") and p.mandante in (o["mandante_id"], o["visitante_id"])
                   and (o["gols_mandante"], o["gols_visitante"]) == (p.gm, p.gv) and _dist(o["data"], p.data) <= 1]
        if len(achados) == 1:
            p.mandante, p.visitante = achados[0]["mandante_id"], achados[0]["visitante_id"]
            log.append(f"{ano}: a página dá o mesmo nome aos dois clubes; vale o jogo do ogol: {nome(p.mandante)} {p.gm}-{p.gv} "
                       f"{nome(p.visitante)} ({p.data})")
        else:
            log.append(f"{ano}: AVISO a página dá o mesmo nome aos dois clubes e o ogol não resolve: {nome(p.mandante)} "
                       f"{p.gm}-{p.gv} ({p.data})")
    partidas = [p for p in partidas if p.gm is not None or p.especial]
    tabs = tabelas_por_clube(tabelas, mapa, rs_usado)
    if int(str(ano)[:4]) in rsssf_rs1.ANOS_A_PARTE:   # jogos do torneio à parte, para tirar do ogol
        tj = rsssf_rs1.trofeu(str(ano))
        cod = lambda n: mapa.get(n) or JA_CASADOS.get(clubes_rs1.norm(n))
        TROFEU[str(ano)] = ({frozenset((cod(j.mandante), cod(j.visitante))) for j in tj},
                            {c for j in tj for c in (cod(j.mandante), cod(j.visitante)) if c})
    partidas = juntar_ogol(ano, partidas, og, tabs, rs_ok, log)
    wo_do_ogol(ano, partidas, og, tabs, log)   # W.O. do ogol sem placar: vencedor pela tabela publicada
    juntar_espn(ano, partidas, log)   # sem arquivo da ESPN, não faz nada
    # fases em português, nos jogos e nas tabelas (as tabelas já estão ligadas aos códigos dos clubes)
    for p in partidas:
        p.fase = fase_pt(p.fase) if rs_ok else fase_pt(OGOL_FASE.get(p.ogol_fase, p.fase))
        p.grupo = grupo_pt(p.grupo) if not p.grupo.lower().startswith(("grupo único", "grupo unico")) else ""
    for tb in tabelas:
        tb.fase = fase_pt(tb.fase)
        tb.grupo = grupo_pt(tb.grupo)
    for f_ in sorted({p.fase for p in partidas} - set(ORDEM) - {"Fase única"}):
        log.append(f"{ano}: AVISO fase sem ordem (importar.ORDEM): {f_}")
    # "Final" com mais de dois clubes é uma fase final de pontos (o título da página termina em "final": "FINAL PHASE",
    # "Octogonal Final"...)
    if len({x for p in partidas if p.fase == "Final" for x in (p.mandante, p.visitante)}) > 2:
        for x in [*partidas, *tabelas]:
            if x.fase == "Final":
                x.fase = "Fase final"
    if len({p.fase for p in partidas}) == 1 and not any(p.grupo for p in partidas):
        for x in [*partidas, *tabelas]:
            x.fase = "Fase única"
    # autores: só quando fecham com o placar
    for p in partidas:
        if p.gols and p.gm is not None and len(p.gols) != p.gm + p.gv:
            p.gols = []
    ids = {x for p in partidas for x in (p.mandante, p.visitante)}
    ajustes = {}   # sem punições lidas da Wikipédia
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


def repescagem_fora(ano, rs: list, log: list[str]) -> list:
    """Jogos do torneio de rebaixamento em que um dos dois clubes só aparece nele (o campeão da 2ª divisão): saem da
    edição e vão para a observação (decisão D-04 a, como o Paulista A2). Com os dois clubes fora do resto da edição
    (grafia diferente), fica e vai para o log."""
    noutras = {x for j in rs if fase_pt(j.fase) != "Torneio de rebaixamento" for x in (j.mandante, j.visitante)}
    fora = []
    for j in rs:
        if fase_pt(j.fase) != "Torneio de rebaixamento":
            continue
        de_fora = [x for x in (j.mandante, j.visitante)
                   if not any(_sim(x.replace("/", "-"), y.replace("/", "-")) >= 0.85 for y in noutras)]
        if len(de_fora) == 1:
            fora.append(j)
        elif de_fora:
            log.append(f"{ano}: repescagem com os dois clubes fora do resto da edição (conferir): {j.mandante} {j.gm}-{j.gv} {j.visitante}")
    if fora:
        jogos = "; ".join(f"{j.mandante} {j.gm}-{j.gv} {j.visitante}"
                          + (f" ({datetime.strptime(j.data, '%Y-%m-%d').strftime('%d/%m/%Y')})" if j.data else "") for j in fora)
        clubes = sorted({x for j in fora for x in (j.mandante, j.visitante)
                         if not any(_sim(x.replace("/", "-"), y.replace("/", "-")) >= 0.85 for y in noutras)})
        OBS_EDICAO.setdefault(str(ano), []).append(f"repescagem contra {' e '.join(clubes)}, de fora da 1ª divisão: {jogos} "
                                                    f"(fica só na observação, decisão D-04)")
        log.append(f"{ano}: {len(fora)} jogos de repescagem contra clube de fora da divisão ficam fora (D-04): {jogos}")
    return fora


def mesmo_jogo_tirado(o: dict, tirados: list, ano, log: list[str]) -> bool:
    """Jogo do ogol que é um dos jogos tirados da RSSSF (anulado ou repescagem): mesma data e mesmo placar."""
    if o.get("gols_mandante") is None:
        return False
    for j in tirados:
        if j.data == o["data"] and j.gm is not None and {(j.gm, j.gv), (j.gv, j.gm)} & {(o["gols_mandante"], o["gols_visitante"])}:
            log.append(f"{ano}: jogo do ogol tirado junto com o da RSSSF: {o['mandante']} {o['gols_mandante']}-{o['gols_visitante']} "
                       f"{o['visitante']} ({o['data']})")
            return True
    return False


def campeao_oficial(ano: int, partidas: list[Partida], rs_c: dict, wk_c: dict) -> str | None:
    """O clube da edição cujo nome bate com o campeão da lista da Wikipédia (ou, sem ela, da RSSSF)."""
    alvo = rs_c.get(ano) or (wk_c.get(str(ano)) or wk_c.get(str(ano)[:4], "")).split(" / ")[0]
    if not alvo:
        return None
    fs = clubes_rs1.fichas()
    ids = {x for p in partidas for x in (p.mandante, p.visitante)}
    def nota(i):
        nomes = {nome(i), *(fs.get(i, {}).get("nomes_ogol") or []), fs.get(i, {}).get("nome_completo") or "", fs.get(i, {}).get("curto", "")}
        uf = clubes_rs1.separar_uf(alvo)[1]   # "Botafogo-PB" x "Botafogo-SP": a UF desempata
        # "Associação Atlética São Bento" (nome completo na lista da RSSSF): também sem a sigla por extenso
        curto = re.sub(r"^(Associa[çc][ãa]o|Sport|Clube|Club|Esporte|Sociedade|Gr[eê]mio|Athletic|Atl[eé]tica|Atl[eé]tico|"
                       r"Esportiva|Esportivo|Recreativa|Recreativo|Club[e]?|de|Futebol|Football|Porto|Alegrense|\s)+\b", "", alvo, flags=re.I).strip()
        cheio = max(_sim(alvo, x) for x in nomes if x)
        # o nome completo desempata ("Internacional": o SC da capital e o CA de Santos, em 1907)
        return (max(cheio, max(_sim(curto, x) for x in nomes if x) if curto else 0) + 0.05 * cheio
                + (0.1 if uf and fs.get(i, {}).get("uf") == uf else 0))
    melhor = sorted(((nota(i), i) for i in ids), reverse=True)
    return melhor[0][1] if melhor and melhor[0][0] >= 0.8 and (len(melhor) == 1 or melhor[1][0] < melhor[0][0]) else None


# edições em que a RSSSF não serve de base (o ogol é a base dos jogos)
BASE_OGOL: dict[str, str] = {
    "2025": "sem página da RSSSF (a lista de campeões ainda não tem o link): os jogos vêm do ogol",
    "2026": "sem página da RSSSF: os jogos vêm do ogol",
}
# edições em que as tabelas publicadas pela RSSSF são parciais (a página parou no meio): não servem de conferência
TABELAS_PARCIAIS: dict[str, str] = {}


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
