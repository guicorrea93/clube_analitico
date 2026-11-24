"""Campeonato italiano antes da Serie A (1898 a 1928/29), no mesmo pacote ita-1 (IT-017; decisão D-05 do Guilherme,
22/11/2026: as 29 edições oficiais, com grupos regionais e finais).

Formatos: torneio em eliminatórias num fim de semana (1898-1904); grupos regionais e grupo final ou final (1905-1909);
grupo único (1909/10); grupos regionais do Norte e do Centro-Sul, semifinais e final nacional (1910/11-1925/26); dois
grupos e grupo final da Divisione Nazionale (1926/27-1928/29). Em 1921/22 houve dois campeonatos (FIGC e CCI), os dois
oficiais; o de 1914/15 foi interrompido pela guerra e dado ao Genoa depois; o de 1926/27 teve o título revogado (Torino).

Fonte: Wikipédia em italiano, artigo de cada edição (coleta/ita-1/wiki_antigo.py): classificação de cada grupo (o modelo
{{Calcio X}} identifica o clube), "Calendario" (jogos com data e rodada) ou, sem ele, "Tabellone" (matriz, sem data), e as
fichas {{Incontro di club}} (finais e mata-mata, com estádio, público, árbitro e gols). O campeão é o do albo d'oro
oficial. A classificação de cada grupo é conferida com os jogos.

Uso: montar(tab, nomes, ocorr) acrescenta as edições ao `tab` do importador (importar.py chama antes do cadastro de clubes)
e devolve as linhas do resumo do relatório.
"""
from __future__ import annotations

import re
import unicodedata
from collections import defaultdict

import clubes_ita as clubes
import wiki_antigo as w
from edicoes import DADOS

PASTA = DADOS / "wikipedia-it-antigo"
URL = "https://it.wikipedia.org/wiki/"
# (artigo, temporada, ano inicial, ano final, campeão (modelo {{Calcio X}}), observação da edição)
EDICOES = [
    ("Campionato Italiano di Football 1898", "1898", 1898, 1898, "Genoa", None),
    ("Campionato Italiano di Football 1899", "1899", 1899, 1899, "Genoa", None),
    ("Campionato Italiano di Football 1900", "1900", 1900, 1900, "Genoa", None),
    ("Campionato Italiano di Football 1901", "1901", 1901, 1901, "Milan", None),
    ("Campionato Italiano di Football 1902", "1902", 1902, 1902, "Genoa", None),
    ("Campionato Italiano di Football 1903", "1903", 1903, 1903, "Genoa", None),
    ("Prima Categoria 1904", "1904", 1904, 1904, "Genoa", None),
    ("Prima Categoria 1905", "1905", 1905, 1905, "Juventus", None),
    ("Prima Categoria 1906", "1906", 1906, 1906, "Milan", None),
    ("Prima Categoria 1907", "1907", 1907, 1907, "Milan", None),
    ("Campionato Italiano di Prima Categoria 1908", "1908", 1908, 1908, "Pro Vercelli",
     "o Campionato Italiano (só com jogadores italianos), o que vale o título; o Campionato Federale do mesmo ano, aberto a "
     "estrangeiros, não é contado"),
    ("Campionato Federale di Prima Categoria 1909", "1909", 1909, 1909, "Pro Vercelli",
     "o Campionato Federale, que passou a valer o título; o Campionato Italiano do mesmo ano não é contado"),
    ("Prima Categoria 1909-1910", "1909/10", 1909, 1910, "Inter", None),
    ("Prima Categoria 1910-1911", "1910/11", 1910, 1911, "Pro Vercelli", None),
    ("Prima Categoria 1911-1912", "1911/12", 1911, 1912, "Pro Vercelli", None),
    ("Prima Categoria 1912-1913", "1912/13", 1912, 1913, "Pro Vercelli", None),
    ("Prima Categoria 1913-1914", "1913/14", 1913, 1914, "Casale", None),
    ("Prima Categoria 1914-1915", "1914/15", 1914, 1915, "Genoa",
     "interrompido em 23/05/1915 pela entrada da Itália na Primeira Guerra Mundial, antes do fim do grupo final do Norte e "
     "da final nacional; a federação deu o título ao Genoa (líder do grupo final do Norte) depois da guerra"),
    ("Prima Categoria 1919-1920", "1919/20", 1919, 1920, "Inter", None),
    ("Prima Categoria 1920-1921", "1920/21", 1920, 1921, "Pro Vercelli", None),
    ("Prima Categoria 1921-1922", "1921/22 (FIGC)", 1921, 1922, "Novese",
     "temporada com dois campeonatos, depois da cisão dos grandes clubes: o da FIGC (Prima Categoria, Novese) e o da CCI "
     "(Prima Divisione, Pro Vercelli); os dois títulos são oficiais"),
    ("Prima Divisione 1921-1922", "1921/22 (CCI)", 1921, 1922, "Pro Vercelli",
     "temporada com dois campeonatos, depois da cisão dos grandes clubes: o da CCI (Prima Divisione, Pro Vercelli) e o da "
     "FIGC (Prima Categoria, Novese); os dois títulos são oficiais"),
    ("Prima Divisione 1922-1923", "1922/23", 1922, 1923, "Genoa", None),
    ("Prima Divisione 1923-1924", "1923/24", 1923, 1924, "Genoa", None),
    ("Prima Divisione 1924-1925", "1924/25", 1924, 1925, "Bologna", None),
    ("Prima Divisione 1925-1926", "1925/26", 1925, 1926, "Juventus", None),
    ("Divisione Nazionale 1926-1927", "1926/27", 1926, 1927, None,
     "título revogado: o Torino ganhou o grupo final, mas a federação tirou o título em 03/11/1927 (caso Allemandi, "
     "suborno de um jogador da Juventus); o título não foi dado a ninguém"),
    ("Divisione Nazionale 1927-1928", "1927/28", 1927, 1928, "Torino", None),
    ("Divisione Nazionale 1928-1929", "1928/29", 1928, 1929, "Bologna", None),
]
# títulos de seção que não são fase nem grupo
GENERICOS = {"risultati", "calendario", "tabellone", "classifica finale", "classifica", "verdetti", "squadre partecipanti",
             "squadra campione", "statistiche", "note", "bibliografia", "collegamenti esterni", "voci correlate",
             "formula", "stagione", "novità", "avvenimenti", "squadre", "capoliste solitarie", "classifica in divenire",
             "classifiche di rendimento", "rendimento andata-ritorno", "rendimento casa-trasferta", "primati stagionali",
             "marcatori", "classifica marcatori", "dettagli"}
TRADUCAO = [(r"\bGironi\b", "Grupos"), (r"\bGirone\b", "Grupo"), (r"\bSemifinali\b", "Semifinais"),
            (r"\bSemifinale\b", "Semifinal"), (r"\bFinali\b", "Finais"), (r"\bFinale\b", "Final"), (r"\bfinale\b", "final"),
            (r"\bFinalissima\b", "Final nacional"), (r"\bQualificazioni\b", "Eliminatórias"), (r"\bEliminatorie\b", "Eliminatórias"),
            (r"\bSezione\b", "Seção"), (r"\bTorneo\b", "Torneio"), (r"\bCampionati\b", "Campeonatos"),
            (r"\bCampionato\b", "Campeonato"), (r"\bSpareggi(o)?\b", "Desempate"), (r"\binterregionali\b", "inter-regionais"),
            (r"\binterregionale\b", "inter-regional"), (r"\bregionali\b", "regionais"), (r"\bregionale\b", "regional"),
            (r"\bnazionali\b", "nacionais"), (r"\bnazionale\b", "nacional"), (r"\bdi qualificazione\b", "de qualificação"),
            (r"\bdi classificazione\b", "de classificação"), (r"\bQuarti di finale\b", "Quartas de final"),
            (r"\bOttavi di finale\b", "Oitavas de final"), (r"\bTurno\b", "Fase"), (r"\bmaggiore\b", "principal"),
            (r"\b[Ss]ettentrionale\b", "do Norte"), (r"\bcentro-meridionale\b", "do Centro-Sul"), (r"\bmeridionale\b", "do Sul"),
            (r"\bpeninsulare\b", "peninsular"), (r"\bnordoccidentale\b", "do Noroeste"), (r"\bemiliano-veneto\b", "emiliano-vêneto"),
            (r"\bpiemontes[ei]\b", "piemontesa"), (r"\blombard[aei]\b", "lombarda"), (r"\bligure\b", "lígure"),
            (r"\bvenet[ao]\b", "vêneta"), (r"\btoscan[ao]\b", "toscana"), (r"\blaziale\b", "do Lácio"),
            (r"\bcampana\b", "da Campânia"), (r"\bpugliese\b", "da Apúlia"), (r"\bsiciliana\b", "siciliana"),
            (r"\bmarchigiana\b", "das Marcas"), (r"\bemiliana\b", "emiliana"), (r"\bLega Nord\b", "Liga Norte"),
            (r"\bLega Sud\b", "Liga Sul"), (r"\bdi Lega\b", "da Liga"), (r"\bdell'Italia centrale\b", "da Itália Central"),
            (r"\bItalia\b", "Itália")]
SIGLAS = {"fc", "us", "ac", "fbc", "sc", "ssc", "calcio", "foot", "ball", "club", "football", "cfc", "sg", "as", "ss", "gs"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s)


def tokens(s: str) -> set[str]:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return {t for t in re.findall(r"[a-z0-9]+", s) if t not in SIGLAS}


def traduzir(s: str) -> str:
    for a, b in TRADUCAO:
        s = re.sub(a, b, s)
    return s


def resolver(nome: str, cands: list[str]) -> str | None:
    """Nome curto do calendário ("US Milanese", "Ado") -> modelo {{Calcio X}} entre os candidatos (os clubes do grupo ou do
    artigo). Exato, depois contido, depois por palavras."""
    n = norm(nome)
    if not n:
        return None
    exato = [c for c in cands if norm(c) == n or norm(re.sub(r"\s*\(.*\)", "", c)) == n]
    if len(exato) == 1:
        return exato[0]
    prefixo = [c for c in cands if norm(c).startswith(n)]   # "Firenze" -> Firenze FBC (e não Libertas Firenze)
    if len(prefixo) == 1:
        return prefixo[0]
    cont = [c for c in cands if n in norm(c) or norm(re.sub(r"\s*\(.*\)", "", c)) in n]
    if len(cont) == 1:
        return cont[0]
    tk = tokens(nome)
    por = [c for c in cands if tk and tk <= tokens(c)] or [c for c in cands if tk and tokens(c) and tokens(c) <= tk]
    if len(por) == 1:
        return por[0]
    if len(n) <= 4:   # abreviação de 3-4 letras ("Ado" = Andrea Doria)
        ab = [c for c in cands if norm(c).startswith(n[:3]) or "".join(t[0] for t in tokens(c)) == n]
        if len(ab) == 1:
            return ab[0]
    return None


# nomes de época e abreviações do calendário e das fichas -> modelo {{Calcio X}}; "Hellas" depende do ano
APELIDOS = {"Alba Audace": "Alba Roma", "Ambrosiana": "Inter", "Genova 1893": "Genoa", "Bentegodi Verona": "Bentegodi",
            "Legnago": "Legnaghese", "Liguria": "Liguria FBC", "A.Doria": "Andrea Doria", "A. Doria": "Andrea Doria",
            "Lucca": "Lucchese", "Naz. Lombardia": "Nazionale Lombardia", "Naz.Lombardia": "Nazionale Lombardia",
            "Stabia": "Stabiese", "G.C. Grifone": "Giovani Calciatori Grifone", "Ausonia P.G.": "Ausonia Pro Gorla",
            "AC Milanese": "A.M.C. Milanese"}


# apelido que depende da seção: (nome, trecho do título da seção) -> modelo
APELIDOS_SECAO = {("Vigor", "sicilian"): "Vigor Trapani"}
CONTEXTO = [""]   # título da seção em leitura (edicao() atualiza)


def achar(nome: str, cands: list[str], todos: list[str], ano: int) -> str | None:
    """Modelo do clube: entre os clubes do grupo, depois do artigo, depois pelos apelidos de época e pelo nome exato de
    qualquer modelo do cadastro."""
    nome = nome.strip()
    if nome == "Hellas":
        return "Hellas (1907-1918)" if ano <= 1918 else "Hellas Verona"
    if nome == "Firenze" and not resolver(nome, cands):   # Firenze FBC até 1915; Club Sportivo Firenze depois da guerra
        return "Firenze FBC" if ano <= 1915 else "C.S. Firenze"
    if nome in APELIDOS:
        return APELIDOS[nome]
    for (n_, trecho), m_ in APELIDOS_SECAO.items():
        if nome == n_ and trecho in CONTEXTO[0]:
            return m_
    r = resolver(nome, cands) or resolver(nome, todos)
    if r:
        return r
    exato = [m for m in clubes.MODELOS_IT if norm(m) == norm(nome)]
    return exato[0] if len(exato) == 1 else None


def separar(casa_fora: str, cands: list[str], todos: list[str], ano: int) -> tuple[str, str] | None:
    """"Pro Vercelli-Casale" -> (modelo, modelo), testando cada hífen."""
    partes = re.split(r"\s*[-–]\s*", casa_fora)
    for i in range(1, len(partes)):
        a, b = "-".join(partes[:i]).strip(), "-".join(partes[i:]).strip()
        ra, rb = achar(a, cands, todos, ano), achar(b, cands, todos, ano)
        if ra and rb and ra != rb:
            return ra, rb
    return None


def chave_modelo(modelo: str) -> str:
    c = clubes.MODELOS_IT.get(modelo)
    if c is None:
        raise SystemExit(f"era antiga: modelo {{{{Calcio {modelo}}}}} sem cadastro em clubes_ita.MODELOS_IT")
    return c


def nome_fase(caminho: list[str]) -> tuple[str, str | None]:
    """Caminho de títulos da seção -> (fase, grupo). O último título que é grupo ("Girone A", "Sezione ligure") vira o grupo."""
    cam = [c for c in caminho if c.lower() not in GENERICOS]
    if not cam:
        return "Fase única", None
    if len(cam) == 1 and re.match(r"(?i)girone [a-z]$", cam[0]):   # Divisione Nazionale: "Girone A" e "Girone B"
        return "Primeira fase", traduzir(cam[0])
    if len(cam) >= 2 and re.match(r"(?i)(girone|sezione|gruppo|lega)\b", cam[-1]) and not re.search(r"(?i)final", cam[-1]):
        return traduzir(" · ".join(cam[:-1])), traduzir(cam[-1])
    return traduzir(" · ".join(cam)), None


def calcular(jogos: list[dict]) -> dict[str, list[int]]:
    t = defaultdict(lambda: [0] * 7)
    for j in jogos:
        if j["gm"] is None:
            continue
        for c, gp, gc in ((j["m"], j["gm"], j["gv"]), (j["v"], j["gv"], j["gm"])):
            x = t[c]
            x[0] += 1; x[4] += gp; x[5] += gc
            if gp > gc:
                x[1] += 1; x[6] += 2
            elif gp == gc:
                x[2] += 1; x[6] += 1
            else:
                x[3] += 1
    return t


def edicao(artigo: str, T: str, a1: int, a2: int, tab, nomes, ocorr) -> tuple:
    texto = (PASTA / f"{artigo.replace(chr(39), '_')}.wiki").read_text(encoding="utf-8")
    url = URL + artigo.replace(" ", "_")
    todos = sorted({m.strip() for m in re.findall(r"\{\{Calcio ([^|}]+)", texto)} & set(clubes.MODELOS_IT))
    secs = [(caminho, corpo, *nome_fase(caminho)) for caminho, corpo in w.secoes(texto)]
    # 1ª passada: classificações (e os clubes de cada grupo, para reconhecer os nomes curtos do calendário)
    tabelas, cands_fg = [], defaultdict(set)
    for caminho, corpo, fase, grupo in secs:
        for cl in w.classifiche(corpo):
            tabelas.append((fase, grupo, cl))
            cands_fg[(fase, grupo)] |= {x["modelo"] for x in cl if x["modelo"] in clubes.MODELOS_IT}
    # 2ª passada: jogos
    jogos, fases_ordem, sem_par, nao_jogados = [], [], [], []
    for caminho, corpo, fase, grupo in secs:
        CONTEXTO[0] = " > ".join(caminho).lower()
        cands = sorted(cands_fg.get((fase, grupo), set()))
        ult = caminho[-1].lower() if caminho else ""
        lst = []
        if ult in ("calendario", "risultati"):
            lst += [(x, separar(x["casa_fora"], cands, todos, a1)) for x in w.calendario(corpo, a1, a2)]
        if ult == "tabellone":
            for x in w.tabellone(corpo):
                m_, v_ = achar(x["mandante"], cands, todos, a1), achar(x["visitante"], cands, todos, a1)
                lst.append((dict(x, data=None, rodada=None, nota="", lado="tab"), (m_, v_) if m_ and v_ else None))
        for x, par in lst:
            if x["placar"] is None:   # jogo sem placar no calendário (não disputado)
                nao_jogados.append(x.get("casa_fora") or "?")
                continue
            if par is None:
                sem_par.append(x.get("casa_fora") or f"{x.get('mandante')}-{x.get('visitante')}")
                continue
            gm, gv, extra = x["placar"]
            jogos.append({"fase": fase, "grupo": grupo, "m": par[0], "v": par[1], "gm": gm, "gv": gv, "data": x["data"],
                          "rodada": x["rodada"], "fonte": "tab" if x["lado"] == "tab" else "cal", "nota": extra or x.get("nota"),
                          "detalhe": None})
        if lst and (fase, grupo) not in fases_ordem:
            fases_ordem.append((fase, grupo))
        for x in w.incontros(corpo):   # fichas de jogo: completam o jogo do calendário ou entram sozinhas
            m_, v_ = achar(x["m"], cands, todos, a1), achar(x["v"], cands, todos, a1)
            if not m_ or not v_ or x["gm"] is None:
                sem_par.append(f"{x['m']}-{x['v']} (ficha)")
                continue
            ja = next((j for j in jogos if {j["m"], j["v"]} == {m_, v_} and j["fonte"] != "ficha"
                       and (j["data"] in (x["data"], None))
                       and (j["m"], j["gm"], j["gv"]) in ((m_, x["gm"], x["gv"]), (v_, x["gv"], x["gm"]))), None)
            if ja:
                ja["detalhe"] = x
                ja["data"] = ja["data"] or x["data"]
                continue
            f_, g_ = (fase, grupo) if fase != "Fase única" or not x["turno"] else (traduzir(x["turno"]), None)
            jogos.append({"fase": f_, "grupo": g_, "m": m_, "v": v_, "gm": x["gm"], "gv": x["gv"], "data": x["data"],
                          "rodada": None, "fonte": "ficha", "nota": x["nota"], "detalhe": x})
            if (f_, g_) not in fases_ordem:
                fases_ordem.append((f_, g_))
    # um grupo com "Calendario" e "Tabellone" fica com o calendário (que tem data)
    com_cal = {(j["fase"], j["grupo"]) for j in jogos if j["fonte"] == "cal"}
    jogos = [j for j in jogos if not (j["fonte"] == "tab" and (j["fase"], j["grupo"]) in com_cal)]
    for j in jogos:
        j["m"], j["v"] = chave_modelo(j["m"]), chave_modelo(j["v"])
        nomes[j["m"]]["wikipedia-it"].add(a1)
        nomes[j["v"]]["wikipedia-it"].add(a1)
    if nao_jogados:
        ocorr[T].append(f"{len(nao_jogados)} jogos do calendário sem placar (não disputados): {'; '.join(nao_jogados[:8])}")
    if sem_par:
        ocorr[T].append(f"{len(sem_par)} jogos do artigo sem clube reconhecido (ficam de fora): {'; '.join(sem_par[:8])}")
    return url, jogos, tabelas, fases_ordem


def montar(tab: dict, nomes: dict, ocorr: dict) -> list[tuple]:
    linhas = []
    for artigo, T, a1, a2, campeao_m, obs in EDICOES:
        url, jogos, tabelas, fases_ordem = edicao(artigo, T, a1, a2, tab, nomes, ocorr)
        if obs:
            ocorr[T].append(obs)
        campeao = chave_modelo(campeao_m) if campeao_m else None
        # ---- conferência: classificação de cada grupo x jogos do mesmo grupo
        conferidas = divergentes = 0
        pos_fase: dict[tuple, dict[str, int]] = defaultdict(dict)
        for fase, grupo, cl in tabelas:
            linhas_cl = [dict(x, clube=chave_modelo(x["modelo"])) for x in cl if x["modelo"] in clubes.MODELOS_IT]
            if not linhas_cl:
                continue
            for x in linhas_cl:
                pos_fase[(fase, grupo)].setdefault(x["clube"], x["posicao"] or 99)
                nomes[x["clube"]]["wikipedia-it"].add(a1)
            js = [j for j in jogos if (j["fase"], j["grupo"]) == (fase, grupo)]
            calc = calcular(js)
            erro = []
            for x in linhas_cl:
                pub = [x["jogos"], x["vitorias"], x["empates"], x["derrotas"], x["gols_pro"], x["gols_contra"], x["pontos"]]
                tab["tabelas_publicadas"].append({
                    "temporada": T, "fase": fase, "grupo": grupo, "posicao": x["posicao"], "nome_fonte": x["modelo"],
                    "clube": clubes.exibicao(x["clube"]), "jogos": x["jogos"], "vitorias": x["vitorias"], "empates": x["empates"],
                    "derrotas": x["derrotas"], "gols_pro": x["gols_pro"], "gols_contra": x["gols_contra"], "pontos": x["pontos"],
                    "fonte": url})
                if js and x["clube"] in calc and pub != calc[x["clube"]]:
                    erro.append(f"{clubes.exibicao(x['clube'])} tabela {pub} jogos {calc[x['clube']]}")
            if not js:
                continue
            if erro:
                divergentes += 1
                for e_ in erro[:5]:
                    ocorr[T].append(f"classificação do {fase}{' · ' + grupo if grupo else ''} x jogos — {e_}")
            else:
                conferidas += 1
        # ---- classificação final: campeão; depois quem foi mais longe (mais fases), a posição na última e os pontos
        total = calcular(jogos)
        fases_clube: dict[str, list[tuple]] = defaultdict(list)
        for j in jogos:
            for c in (j["m"], j["v"]):
                if (j["fase"], j["grupo"]) not in fases_clube[c]:
                    fases_clube[c].append((j["fase"], j["grupo"]))
        for (fase, grupo), d in pos_fase.items():
            for c in d:
                if (fase, grupo) not in fases_clube[c]:
                    fases_clube[c].append((fase, grupo))
        ordem_f = {fg: i for i, fg in enumerate(fases_ordem)}

        def chave_ord(c):
            fs = fases_clube[c]
            ultima = max(fs, key=lambda fg: ordem_f.get(fg, -1)) if fs else None
            return (0 if c == campeao else 1, -len({f for f, _ in fs}), -ordem_f.get(ultima, -1),
                    pos_fase.get(ultima, {}).get(c, 99), -total[c][6], -(total[c][4] - total[c][5]))
        clubes_ed = sorted(sorted(set(fases_clube) | set(total)), key=chave_ord)  # empate total: ordem alfabética
        if campeao and campeao not in clubes_ed:
            ocorr[T].append(f"o campeão ({clubes.exibicao(campeao)}) não aparece nos jogos nem nas classificações")
        for pos, c in enumerate(clubes_ed, 1):
            j_, v_, e_, d_, gp, gc, p = total[c] if c in total else [0] * 7
            tab["classificacao_final"].append({
                "temporada": T, "posicao": pos, "clube": clubes.exibicao(c), "jogos": j_, "vitorias": v_, "empates": e_,
                "derrotas": d_, "gols_pro": gp, "gols_contra": gc, "pontos": p, "ajuste_pontos": 0,
                "situacao": "campeao" if c == campeao else None,
                "fonte": "Wikipédia it (campeão do albo d'oro; depois a fase alcançada e a posição no grupo)",
                "observacao": "soma de todas as fases; sem classificação oficial além do campeão"
                              + ("" if j_ else "; só na classificação do grupo (sem os jogos)")})
        # ---- partidas e gols
        jogos.sort(key=lambda j: (j["data"] or "9999", ordem_f.get((j["fase"], j["grupo"]), 99), j["rodada"] or 0))
        a_id = f"{a1}c" if "CCI" in T else a1
        autor = 0
        for i, j in enumerate(jogos, 1):
            pid = f"{a_id}-{i:04d}"
            d = j["detalhe"] or {}
            nota = j["nota"]
            esp = "awd" if re.search(r"(?i)tavolino|\btav\.|forfait|rinuncia", nota or "") else None
            tab["partidas"].append({
                "id": pid, "temporada": T, "fase": j["fase"], "grupo": j["grupo"], "rodada": j["rodada"], "data": j["data"],
                "hora": None, "mandante": clubes.exibicao(j["m"]), "visitante": clubes.exibicao(j["v"]),
                "gols_mandante": j["gm"], "gols_visitante": j["gv"], "penaltis_mandante": None, "penaltis_visitante": None,
                "resultado_especial": esp, "estadio": d.get("estadio"), "cidade": d.get("cidade"), "publico": d.get("publico"),
                "fonte": "Wikipédia it" + (" (tabellone, sem data)" if j["fonte"] == "tab" else ""), "fonte_id": None,
                "gols_texto": None, "observacao": ("resultado dado fora de campo: " + nota) if esp else (nota or None),
                "arbitro": d.get("arbitro")})
            gl = d.get("gols") or []
            if gl and (sum(g["lado"] == "1" for g in gl), sum(g["lado"] == "2" for g in gl)) == (j["gm"], j["gv"]):
                for g in gl:
                    tab["gols"].append({"partida_id": pid, "clube": clubes.exibicao(j["m"] if g["lado"] == "1" else j["v"]),
                                        "jogador": g["jogador"], "minuto": g["minuto"], "acrescimo": None, "tipo": g["tipo"],
                                        "fonte": "Wikipédia it"})
                autor += len(gl)
        # ---- edição, fases, conferência
        fases_unicas = list(dict.fromkeys(f for f, _ in fases_ordem))
        for i, f in enumerate(fases_unicas, 1):
            gs = {g for f2, g in fases_ordem if f2 == f and g}
            n_j = [j for j in jogos if j["fase"] == f]
            mata = len(gs) == 0 and len({(j["m"], j["v"]) for j in n_j}) <= 2 and len({c for j in n_j for c in (j["m"], j["v"])}) == 2
            tab["fases"].append({"temporada": T, "ordem": i, "fase": f, "tipo": "mata_mata" if mata else "grupos",
                                 "num_grupos": len(gs) or (None if mata else 1),
                                 "formato_serie": "ida_volta" if mata and len(n_j) == 2 else "jogo_unico" if mata else "pontos_corridos",
                                 "criterio": "pontos" if not mata else "resultado"})
        gols = sum((j["gm"] or 0) + (j["gv"] or 0) for j in jogos)
        vice = clubes_ed[1] if len(clubes_ed) > 1 else None
        tab["edicoes"].append({"temporada": T, "ano_inicio": a1, "ano_fim": a2, "nome_oficial": artigo.rsplit(" ", 1)[0],
                               "num_clubes": len(clubes_ed), "pontos_vitoria": 2,
                               "formato": " → ".join(fases_unicas) if fases_unicas else None,
                               "campeao": clubes.exibicao(campeao) if campeao else None,
                               "vice": clubes.exibicao(vice) if vice and campeao else None,
                               "fontes": "Wikipédia it", "observacao": obs})
        tab["conferencia"].append({"temporada": T, "jogos": len(jogos), "jogos_esperados": None, "tabelas_conferidas": conferidas,
                                   "tabelas_divergentes": divergentes, "gols": gols, "gols_com_autor": autor,
                                   "observacao": f"campeão {clubes.exibicao(campeao) if campeao else '— (revogado)'} (albo d'oro)"})
        linhas.append((T, "Wikipédia it", len(clubes_ed), len(jogos), 0, gols, autor, conferidas, divergentes,
                       clubes.exibicao(campeao) if campeao else "— (revogado)", ""))
        print(f"{T}: {len(jogos)} jogos, {len(clubes_ed)} clubes, classificações {conferidas} ok / {divergentes} div, "
              f"campeão {clubes.exibicao(campeao) if campeao else '—'}", flush=True)
    return linhas
