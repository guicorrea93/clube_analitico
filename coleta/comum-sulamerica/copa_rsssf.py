"""Importador comum das copas nacionais da América do Sul (decisão do Guilherme, 24/11/2026: as sete copas, contagem da
Wikipédia, das menores às maiores; pesquisa em copas-nacionais.md). Cada copa (coleta/<pais>-copa/) só configura:

- as edições (EdicaoCopa: página da RSSSF e trecho, nomes de fase, títulos de região/grupo);
- os clubes (função clube(nome, ano) -> nome de exibição, e CLUBES com a cidade), em geral os da liga do país mais os
  amadores e do interior que só jogam a copa;
- o separador de autores dos gols (o autores.py da liga do país).

Daqui sai o pacote no formato das ligas (data/coleta/<slug>/pacote/): competicao.json, edicoes, fases, partidas, gols,
cartoes (vazio: a RSSSF não traz), classificacao_final, clubes, artilheiros, conferencia e tabelas_publicadas (as das fases
de grupos, quando há).

Regras (as mesmas da Copa do Brasil, coleta/bra-copa-do-brasil):
- fase de mata-mata: jogo único ou ida e volta (pelo par de clubes); fase com tabela ou grupo: grupos/liga;
- W.O. ("X awd Y [awarded 3-0, Y forfeited]"): resultado "wo", placar dado, observação com quem não compareceu;
- pênaltis ("[4-2 pen]") nos campos de pênaltis; o jogo fica empatado;
- campeão: vencedor da final (placar agregado, depois pênaltis); conferido com a lista da Wikipédia;
- classificação: calculada (fase alcançada, pontos, vitórias, saldo, gols pró), campeão em 1º e vice em 2º.
"""
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path

import rsssf_sul

RAIZ = Path(__file__).resolve().parent.parent.parent

COLUNAS_PARTIDAS = ["id", "temporada", "fase", "grupo", "rodada", "data", "hora", "mandante", "visitante", "gols_mandante",
                    "gols_visitante", "penaltis_mandante", "penaltis_visitante", "resultado_especial", "estadio", "cidade",
                    "publico", "fonte", "fonte_id", "gols_texto", "observacao"]


@dataclass
class EdicaoCopa:
    temporada: str                       # "2024"
    ano_inicio: int
    ano_fim: int
    nome_oficial: str
    trechos: list[tuple[str, int, int | None]]   # (página da RSSSF sem .html, linha inicial, linha final ou None)
    regioes: list[tuple[str, str]] = field(default_factory=list)   # (regex do título, grupo): "Regional Norte" -> "Norte"
    fim_regiao: str = r"^NUNCA$"         # título que encerra as regiões (volta ao grupo vazio)
    obs: str = ""
    fase_padrao: str = ""                # fase dos jogos sem título de fase (vazio: a 1ª da lista da copa)
    pontos: bool = False                 # edição de pontos corridos (Copa Ecuador 1970): campeão e vice pela classificação
    datas: bool = True                   # False: a página só dá o mês ("Jan 1970"), a data lida não vale
    fases: list | None = None            # (regex, fase) desta edição, quando os títulos mudam de sentido (Copa Colombia: "Round 1")
    extras: object = None                # função() -> [Jogo] de outra fonte (Wikipédia), com texto "wiki-..."; somam-se à RSSSF
    trocas: list = field(default_factory=list)   # (regex, troca ou função) só desta edição, depois das da copa
    grupos_clubes: dict = field(default_factory=dict)   # {fase: {clube: grupo}} quando os jogos vêm sem o título do grupo
    # (Copa Chile 1991-1995: só traços entre os grupos; o grupo sai das tabelas finais da página)
    campeao_fonte: str = ""              # campeão quando os jogos não o decidem: final empatada sem o placar dos pênaltis
    # ("(Colo Colo on pen)", Copa Chile 1958), edição sem final ou sem jogos (Copa Venezuela); nome da fonte, passa pelo clube()
    vice_fonte: str = ""                 # vice nesses casos (sem ele, o outro finalista)
    final_desempate: bool = False        # final com jogos de desempate ("Replay", Copa Venezuela 1966 e 1968): decide o
    # último jogo, não o placar somado
    campeao_tabela: bool = False         # a última fase é de pontos (quadrangular final, Copa Chile 1982): campeão e vice
    # pela classificação, sem tornar as outras fases de pontos (o que `pontos` faz)
    anos_leitura: tuple[int, int] | None = None   # (ano_ini, ano_fim) para datar os jogos, quando diferem da edição
    # (Copa Argentina 2019/20: começa em fev/2020 e vira para 2021 pelo "Dec -> Jan"; com ano_fim 2021 o fev iria para 2021)


@dataclass
class Copa:
    slug: str
    competicao: dict                     # competicao.json
    edicoes: list[EdicaoCopa]
    fases: list[tuple[str, str]]         # (regex do título, nome da fase), na ordem de importância crescente
    linhas: object                       # função(pagina) -> tuple[str, ...] (o linhas() do ler_rsssf da liga)
    clube: object                        # função(nome, ano) -> nome de exibição ou None
    clubes: dict[str, tuple[str, str]]   # nome de exibição -> (cidade, região)
    autores: object                      # módulo autores da liga (eh_autores, separar, publico)
    campeoes_wiki: dict[str, str]        # temporada -> campeão pela Wikipédia (conferência)
    fonte_pagina: str = "https://www.rsssf.org/tablesu/{pagina}.html"
    ignorar: list[str] = field(default_factory=list)   # regex de linhas que não são jogo
    fases_pontos: list[str] = field(default_factory=list)   # fases sempre de pontos, mesmo sem tabela legível na página
    trocas: list[tuple[str, str]] = field(default_factory=list)   # (regex, troca) nas linhas antes de ler: "[Mar 18 We]" -> "[Mar 18]"
    espn: object = None                  # função(edição) -> jogos da ESPN (espn.resumir) da edição: data, hora, estádio,
    # cidade e público dos jogos que casam (mesmos clubes, mando e placar; com data na fonte, até 1 dia de diferença)
    fuso: object = None                  # função(datetime UTC) -> datetime local (horário do país)
    espn_corrige: bool = False           # True: nos jogos ligados, o mando e a data da ESPN valem mais que os da fonte
    # (Copa Chile e Colômbia, onde o estádio da ESPN confirma; não na Argentina, com muitos jogos em campo neutro)


_FIM_ESPN = ("STATUS_FULL_TIME", "STATUS_FINAL", "STATUS_FINAL_AET", "STATUS_FINAL_PEN")


def espn_arquivos(slug: str, liga: str):
    """Para Copa.espn: os jogos da ESPN dos anos da edição, de data/coleta/<slug>/espn/<liga>_<ano>.json
    (coleta/comum-sulamerica/baixar_espn_copa.py)."""
    lidos: dict[int, list[dict]] = {}

    def jogos(ed: EdicaoCopa) -> list[dict]:
        a0, a1 = ed.anos_leitura or (ed.ano_inicio, ed.ano_fim)
        out = []
        for a in range(min(a0, ed.ano_inicio), max(a1, ed.ano_fim) + 1):
            if a not in lidos:
                p = RAIZ / "data" / "coleta" / slug / "espn" / f"{liga}_{a}.json"
                lidos[a] = json.loads(p.read_text(encoding="utf-8")) if p.exists() else []
            out += lidos[a]
        return out
    return jogos


def _casar_espn(copa: Copa, ed: EdicaoCopa, jogos: list[dict], sem_nome_espn: Counter, pontos: set[str]) -> int:
    """Liga cada jogo a um jogo da ESPN (j["espn"] = (data local, hora, estádio, cidade, público, id)); cada jogo da ESPN
    serve a um só e só casa com um único candidato. 1ª passada: mesmos clubes, mando e placar (com data na fonte, até 1
    dia de diferença). 2ª passada, só com data na fonte: mando invertido (campo neutro) ou um só clube reconhecido pela
    ESPN (nome que as regras não pegam), sempre com o placar e a data até 1 dia."""
    es = []
    todos = copa.espn(ed)
    # a ESPN diz de que temporada é cada jogo; os anos da edição podem trazer duas (Copa Chile 2013/14 e 2014/15 em 2014;
    # a Copa Argentina "2015/16" é a temporada 2016 da ESPN): fica a que tem mais jogos iguais aos da fonte, com ao menos
    # 10% dos jogos da edição (mínimo 3); sem isso, nenhuma (a 2013/14 do Chile só acha jogos da temporada seguinte)
    temporadas = {g.get("temporada") for g in todos}
    if todos:
        chaves = Counter((j["m"], j["v"], j["gm"], j["gv"]) for j in jogos)

        def iguais(t) -> int:
            return sum(1 for g in todos if g.get("temporada") == t and g["gols_mandante"] not in (None, "") and chaves[(
                copa.clube(g["mandante"], ed.ano_inicio), copa.clube(g["visitante"], ed.ano_inicio),
                int(g["gols_mandante"]), int(g["gols_visitante"]))])
        conta = {t: iguais(t) for t in temporadas}
        melhor = max(conta, key=conta.get)
        todos = [g for g in todos if g.get("temporada") == melhor] if conta[melhor] >= max(3, 0.1 * len(jogos)) else []
    # com datas na fonte, só os jogos da ESPN no período da edição (30 dias de folga): o mesmo ano pode ter duas edições
    # (só com datas em 80% dos jogos: com poucas, as da final, o período cortaria o resto)
    datas = sorted(date.fromisoformat(j["x"].data) for j in jogos if j["x"].data)
    if len(datas) < 0.8 * len(jogos):
        datas = []
    for g in todos:
        dia = date.fromisoformat(g["data_hora"][:10])
        if datas and not (datas[0] - timedelta(days=30) <= dia <= datas[-1] + timedelta(days=30)):
            continue
        if g["situacao"] not in _FIM_ESPN or g["gols_mandante"] in (None, ""):
            continue
        m, v = copa.clube(g["mandante"], ed.ano_inicio), copa.clube(g["visitante"], ed.ano_inicio)
        for nome, c in ((g["mandante"], m), (g["visitante"], v)):
            if not c:
                sem_nome_espn[nome] += 1
        loc = copa.fuso(datetime.fromisoformat(g["data_hora"].replace("Z", "+00:00")))
        hora = loc.strftime("%H:%M") if g["data_hora"][11:16] != "00:00" else None   # 00:00 UTC = hora desconhecida
        estadio = g.get("estadio") if g.get("estadio") not in ("Sin confirmar", "A confirmar", "TBD") else None
        es.append({"m": m, "v": v, "gm": int(g["gols_mandante"]), "gv": int(g["gols_visitante"]), "dia": loc.date(),
                   "info": (loc.date(), hora, estadio or None, g.get("cidade") or None, g.get("publico") or None, g["id"])})

    def bate(g: dict, j: dict, passo: int) -> bool:
        if passo == 1:
            return (g["m"], g["v"], g["gm"], g["gv"]) == (j["m"], j["v"], j["gm"], j["gv"])
        if passo == 3:   # os dois clubes reconhecidos, os gols de cada um iguais; mando invertido só no mata-mata (num
            # turno e returno, o jogo da volta com o placar espelhado pegaria o lugar do da ida)
            return ((g["m"], g["v"], g["gm"], g["gv"]) == (j["m"], j["v"], j["gm"], j["gv"]) or j["fase"] not in pontos and
                    (g["v"], g["m"], g["gv"], g["gm"]) == (j["m"], j["v"], j["gm"], j["gv"]))
        return any(a in (None, j["m"]) and b in (None, j["v"]) and (a or b) and (ga, gb) == (j["gm"], j["gv"])
                   for a, b, ga, gb in ((g["m"], g["v"], g["gm"], g["gv"]), (g["v"], g["m"], g["gv"], g["gm"])))

    # 3ª passada: mesmo par de clubes e mesmos gols de cada um, com a data da fonte até 15 dias (a fonte dá a data do
    # começo da rodada) ou sem data (ida e volta com o mando trocado na fonte: Copa Chile 2016-2018)
    usados, n = set(), 0
    for passo, folga in ((1, 1), (2, 1), (3, 15)):
        for j in jogos:
            if j.get("espn") or j["gm"] is None or j["esp"] or (passo == 2 and not j["x"].data):
                continue
            d = date.fromisoformat(j["x"].data) if j["x"].data else None
            cs = [g for g in es if g["info"][5] not in usados and (d is None or abs((g["dia"] - d).days) <= folga) and bate(g, j, passo)]
            if len(cs) == 1:
                j["espn"] = cs[0]["info"]
                j["espn_invertido"] = cs[0]["m"] is not None and cs[0]["m"] != j["m"] or cs[0]["v"] is not None and cs[0]["v"] != j["v"]
                usados.add(cs[0]["info"][5])
                n += 1
    return n


def _wo(x: rsssf_sul.Jogo) -> tuple[int, int, str] | None:
    """W.O. "[awarded 3-0, Peñarol forfeited]": (gols do mandante, do visitante, observação)."""
    if x.especial not in ("awd", "wo"):
        return None
    m = re.search(r"award(?:ed)?\s+(\d{1,2})\s*-\s*(\d{1,2})", x.nota, re.I)
    quem = re.search(r"(?:^|[,;]\s*)([^,;\[]+?)\s+(?:forfeited|withdrew|did not (?:show|appear|turn up))", x.nota, re.I)
    if not m:
        return None
    obs = f"W.O.: {quem.group(1).strip()} não compareceu" if quem else f"W.O. (nota da fonte: {x.nota})"
    return int(m.group(1)), int(m.group(2)), obs


def _autores_inteiros(ls: list[str], linha: int) -> str:
    """Autores dos gols quando o colchete continua nas linhas seguintes ("[Gabriel Ifrán 9og, Esteban Rodríguez 68;" e
    "   Oscar Cruz 87]"): o leitor comum só pega a 1ª linha. Junta até o "]" e devolve o texto, ou "" se não há bloco."""
    k = linha + 1
    while k < len(ls) and k <= linha + 2 and not ls[k].strip().startswith("["):
        if ls[k].strip() and rsssf_sul._jogo(ls[k]):
            return ""
        k += 1
    if k >= len(ls) or not ls[k].strip().startswith("["):
        return ""
    partes = [ls[k].strip()]
    while "]" not in partes[-1] and k + 1 < len(ls) and ls[k + 1].startswith(" ") and ls[k + 1].strip():
        k += 1
        partes.append(ls[k].strip())
    bloco = " ".join(partes)
    a = rsssf_sul._autores(bloco) if "]" in bloco else ""
    return a or ""


def _fonte(texto: str) -> tuple[str, str]:
    """(fonte, fonte_id) do jogo: RSSSF ("col2020:551") ou Wikipédia em espanhol ("wiki-es_2013:420")."""
    if texto.startswith("wiki"):
        return "Wikipédia (es)", "wikipedia:" + texto.split("-", 1)[1]
    return "RSSSF", f"rsssf:{texto}"


def _ida_e_volta(x: rsssf_sul.Jogo) -> list[rsssf_sul.Jogo]:
    """Ida e volta na mesma linha ("Huila  0-2 4-0 Llaneros FC  [4-1 pen]", Copa Colombia 2020-2023): o leitor comum põe o
    2º placar no nome do visitante. Vira dois jogos: a ida (A x B) e a volta (B x A); o 2º placar e os pênaltis vêm do
    ponto de vista de A ("Huila 0-2 4-0 Llaneros" = 4-2 no agregado para o Huila)."""
    m = re.match(r"^(\d{1,2})-(\d{1,2})\s+(\S.*)$", x.visitante or "")
    if not m or x.gm is None:
        return [x]
    a, b = x.mandante, m.group(3).strip()
    volta = rsssf_sul.Jogo(linha=x.linha, mandante=b, visitante=a, gm=int(m.group(2)), gv=int(m.group(1)), rodada=x.rodada,
                           secao=x.secao, fase=x.fase, grupo=x.grupo, nota=x.nota,
                           pen_m=x.pen_v, pen_v=x.pen_m, texto=x.texto)
    x.visitante, x.pen_m, x.pen_v, x.nota = b, None, None, ""
    volta.volta = True   # a linha é a da ida: os autores (se houver) não são da volta
    return [x, volta]


def ler_edicao(copa: Copa, ed: EdicaoCopa) -> tuple[list[rsssf_sul.Jogo], list[rsssf_sul.Tabela]]:
    jogos, tabelas = [], []
    for tr in ed.trechos:
        pagina, ini, fim = tr[:3]
        fases = tr[3] if len(tr) > 3 else (ed.fases or copa.fases)   # fases do trecho (títulos repetidos na página)
        ls = list(copa.linhas(pagina))
        fim = len(ls) if fim is None else fim
        # "Cúcuta  o/w Tolima  [awarded 0-3]" (Copa Colombia 2020): o leitor comum só conhece "w/o"; vira "awd"
        trecho = [re.sub(r"(?<=\S)\s+o/w\s+(?=\S)", "  awd ", l) for l in ls[ini:fim]]
        for rx, troca in copa.trocas + ed.trocas:
            trecho = [re.sub(rx, troca, l) for l in trecho]
        a0, a1 = ed.anos_leitura or (ed.ano_inicio, ed.ano_fim)
        j, t = rsssf_sul.ler([""] * ini + trecho, a0, a1, fases=fases, ignorar=copa.ignorar)
        regiao, por_linha = "", {}
        for i in range(ini, fim):
            s = ls[i].strip()
            if re.match(ed.fim_regiao, s):
                regiao = ""
            for rx, g in ed.regioes:
                if re.match(rx, s):
                    regiao = g
            por_linha[i] = regiao
        j = [y for x in j for y in _ida_e_volta(x)]
        for x in j:
            x.texto = f"{pagina}:{x.linha}"
            if por_linha.get(x.linha):
                x.grupo = por_linha[x.linha]
            if not getattr(x, "volta", False):
                x.gols_texto = _autores_inteiros(ls, x.linha) or x.gols_texto
        for x in t:
            x.fonte = pagina
            if por_linha.get(x.linha):
                x.grupo = x.grupo or por_linha[x.linha]
        jogos += j
        tabelas += t
    if ed.extras:
        jogos += ed.extras()
    return jogos, tabelas


def _vencedor(js: list[dict]) -> tuple[str | None, str | None]:
    """(vencedor, perdedor) de um confronto de 1 ou 2 jogos: placar agregado, depois pênaltis do último jogo e, sem eles,
    o gol fora (Copa Ecuador 2018/19: "LDU de Quito winners on away goals rule")."""
    if not js:
        return None, None
    a, b = js[0]["m"], js[0]["v"]
    ga = sum((j["gm"] if j["m"] == a else j["gv"]) or 0 for j in js)
    gb = sum((j["gv"] if j["m"] == a else j["gm"]) or 0 for j in js)
    if ga != gb:
        return (a, b) if ga > gb else (b, a)
    ult = js[-1]
    if ult["pm"] is not None and ult["pv"] is not None and ult["pm"] != ult["pv"]:
        venc = ult["m"] if ult["pm"] > ult["pv"] else ult["v"]
        return venc, (b if venc == a else a)
    if len(js) == 2:   # gol fora
        fora_a = sum((j["gv"] or 0) for j in js if j["v"] == a)
        fora_b = sum((j["gv"] or 0) for j in js if j["v"] == b)
        if fora_a != fora_b:
            return (a, b) if fora_a > fora_b else (b, a)
    return None, None


def importar(copa: Copa, relatorio: Path) -> None:
    pacote = RAIZ / "data" / "coleta" / copa.slug / "pacote"
    pacote.mkdir(parents=True, exist_ok=True)
    (pacote / "competicao.json").write_text(json.dumps(copa.competicao, ensure_ascii=False, indent=1), encoding="utf-8")
    ordem_fase = {nome: k for k, (_, nome) in enumerate(copa.fases)}
    L: dict[str, list] = defaultdict(list)
    nomes_fonte: dict[str, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
    sem_nome: list[str] = []
    sem_nome_espn: Counter = Counter()   # nomes da ESPN sem clube (o jogo não casa)
    casados_espn: list[str] = []
    datas_espn = datas_corrigidas = mandos_corrigidos = 0
    rel = [f"# {copa.competicao['nome']} ({copa.slug})", "",
           "Gerado por coleta/comum-sulamerica/copa_rsssf.py (configuração em coleta/" + copa.slug + "/importar.py).", "",
           "| Temporada | Jogos | Fases | Campeão | Vice | Wikipédia | Gols com autor |", "|---|---|---|---|---|---|---|"]
    for ed in copa.edicoes:
        xs, tabs = ler_edicao(copa, ed)
        padrao = ed.fase_padrao or copa.fases[0][1]   # fase dos jogos e tabelas sem título de fase
        jogos = []
        for x in xs:
            m, v = copa.clube(x.mandante, ed.ano_inicio), copa.clube(x.visitante, ed.ano_inicio)
            if not m or not v:
                sem_nome.append(f"{ed.temporada} {x.texto}: {x.mandante!r} x {x.visitante!r}")
                continue
            nomes_fonte[m][f"rsssf:{x.mandante}"].append(ed.ano_inicio)
            nomes_fonte[v][f"rsssf:{x.visitante}"].append(ed.ano_inicio)
            wo = _wo(x)
            gm, gv = (wo[0], wo[1]) if wo else (x.gm, x.gv)
            jogos.append({"x": x, "m": m, "v": v, "gm": gm, "gv": gv, "pm": x.pen_m, "pv": x.pen_v,
                          "esp": "wo" if wo else ("" if x.gm is not None else (x.especial or "n/p")),
                          "obs": wo[2] if wo else "", "fase": x.fase or padrao, "grupo": x.grupo or ""})
            if not ed.datas:
                x.data = None
            gc = ed.grupos_clubes.get(jogos[-1]["fase"], {})
            if gc.get(m) and gc.get(m) == gc.get(v):   # vale mais que o grupo herdado de um título anterior
                jogos[-1]["grupo"] = gc[m]
        if copa.espn:
            # fases de pontos (as mesmas da classificação abaixo): nelas o mando da fonte não é trocado
            pontos_ed = {j["fase"] for j in jogos} if ed.pontos else {t.fase or padrao for t in tabs} | set(copa.fases_pontos)
            n_espn = _casar_espn(copa, ed, jogos, sem_nome_espn, pontos_ed)
            if n_espn:
                casados_espn.append(f"{ed.temporada}: {n_espn} de {len(jogos)}")
            for j in jogos:
                if not j.get("espn"):
                    continue
                if not j["x"].data:
                    j["x"].data = j["espn"][0].isoformat()
                    datas_espn += 1
                elif copa.espn_corrige and abs((j["espn"][0] - date.fromisoformat(j["x"].data)).days) > 1:
                    j.setdefault("obs_espn", []).append(f"data pela ESPN (a fonte dá {j['x'].data})")
                    j["x"].data = j["espn"][0].isoformat()
                    datas_corrigidas += 1
                # o mando só muda com o estádio da ESPN para confirmar (jogo único em campo neutro vem sem estádio)
                if copa.espn_corrige and j.get("espn_invertido") and j["fase"] not in pontos_ed and j["espn"][2]:
                    j["m"], j["v"], j["gm"], j["gv"], j["pm"], j["pv"] = j["v"], j["m"], j["gv"], j["gm"], j["pv"], j["pm"]
                    j.setdefault("obs_espn", []).append("mando pela ESPN (a fonte dá o jogo invertido)")
                    j["trocado"] = True
                    mandos_corrigidos += 1
        fase_tab = {t.fase or padrao for t in tabs}
        fases_pontos: set[str] = set()   # a rodada só vale nelas (no mata-mata, o "Round 3" herdado não é rodada)
        # fases dos jogos e das tabelas (a 1ª fase de 2022 da Copa Paraguay só tem as tabelas das zonas)
        fases = sorted({j["fase"] for j in jogos} | fase_tab, key=lambda f: (ordem_fase.get(f, 0), min(
            [j["x"].linha for j in jogos if j["fase"] == f] + [t.linha for t in tabs if (t.fase or padrao) == f])))
        for k, f in enumerate(fases, 1):
            js = [j for j in jogos if j["fase"] == f]
            grupos = sorted({j["grupo"] for j in js if j["grupo"]} | {t.grupo for t in tabs if (t.fase or padrao) == f and t.grupo})
            pares = Counter(frozenset((j["m"], j["v"])) for j in js) or Counter({frozenset(): 1})
            # fase com tabela publicada é de pontos (grupos); sem tabela, mata-mata, salvo as declaradas na copa
            liga = f in fase_tab or ed.pontos or f in copa.fases_pontos
            tipo = ("grupos" if len(grupos) >= 2 else "liga") if liga else "mata_mata"
            serie = "pontos_corridos" if liga else ("ida_volta" if max(pares.values()) > 1 else "jogo_unico")
            L["fases"].append([ed.temporada, k, f, tipo, len(grupos) if tipo == "grupos" else None, serie, ""])
            if liga:
                fases_pontos.add(f)
        # campeão e vice: a final
        final = [j for j in jogos if j["fase"] == "Final"]
        campeao, vice = _vencedor(final[-1:] if ed.final_desempate else final) if final else (None, None)
        if campeao is None and ed.campeao_fonte:   # os jogos não decidem (sem placar dos pênaltis, sem final, sem jogos)
            campeao = copa.clube(ed.campeao_fonte, ed.ano_inicio)
            vice = (copa.clube(ed.vice_fonte, ed.ano_inicio) if ed.vice_fonte else
                    next((c for c in (final[0]["m"], final[0]["v"]) if c != campeao), None) if final else None)
        # partidas e gols
        gols_ed = autor_ed = 0
        eid = re.sub(r"[^0-9a-z]+", "-", rsssf_sul.chave(ed.temporada))
        for n, j in enumerate(sorted(jogos, key=lambda j: (fases.index(j["fase"]), j["x"].data or "9999", j["x"].linha)), 1):
            x = j["x"]
            pid = f"{eid}-{n:04d}"
            sep = None
            if j["esp"] == "" and j["gm"] is not None:
                gols_ed += j["gm"] + j["gv"]
                if x.gols_texto and copa.autores.eh_autores(x.gols_texto):
                    if j.get("trocado"):   # o texto dos autores segue o mando da fonte
                        sep = copa.autores.separar(x.gols_texto, j["gv"], j["gm"])
                        sep = (sep[1], sep[0]) if sep else None
                    else:
                        sep = copa.autores.separar(x.gols_texto, j["gm"], j["gv"])
            if sep:
                for lado, gs in ((j["m"], sep[0]), (j["v"], sep[1])):
                    for g in gs:
                        L["gols"].append([pid, lado, g["jogador"], g["minuto"], g["acrescimo"], g["tipo"], "RSSSF"])
                        autor_ed += 1
            obs = [j["obs"]] + ([x.nota] if x.nota and not j["obs"] and not re.search(r"\bpen\b", x.nota) else []) + j.get("obs_espn", [])
            fonte, fonte_id = _fonte(x.texto)
            hora = estadio = cidade = publico = None
            if j.get("espn"):
                _, hora, estadio, cidade, publico, eid_espn = j["espn"]
                fonte_id += f" espn:{eid_espn}"
            L["partidas"].append([pid, ed.temporada, j["fase"], j["grupo"], x.rodada if j["fase"] in fases_pontos else None, x.data, hora, j["m"], j["v"], j["gm"],
                                  j["gv"], j["pm"], j["pv"], j["esp"], estadio, cidade, publico, fonte, fonte_id,
                                  "" if sep or not x.gols_texto else x.gols_texto, "; ".join(o for o in obs if o)])
        # classificação: fase alcançada, pontos, vitórias, saldo, gols pró
        camp: dict[str, list[int]] = defaultdict(lambda: [0] * 7)   # j v e d gp gc pts
        alcance: dict[str, int] = defaultdict(int)
        for j in jogos:
            for c in (j["m"], j["v"]):
                alcance[c] = max(alcance[c], fases.index(j["fase"]))
            if j["gm"] is None:
                continue
            for c, a, b in ((j["m"], j["gm"], j["gv"]), (j["v"], j["gv"], j["gm"])):
                r = camp[c]
                r[0] += 1
                r[4] += a
                r[5] += b
                k = 1 if a > b else 2 if a == b else 3
                r[k] += 1
                r[6] += 3 if a > b else 1 if a == b else 0
        clubes = sorted(alcance)
        linhas = sorted(clubes, key=lambda c: (-alcance[c], -camp[c][6], -camp[c][1], -(camp[c][4] - camp[c][5]), -camp[c][4], c))
        if campeao is None and (ed.pontos or ed.campeao_tabela) and not final:   # pontos corridos ou quadrangular final
            campeao, vice = (linhas + [None, None])[:2]
        for c, nome in ((vice, ed.vice_fonte), (campeao, ed.campeao_fonte)):
            if not c:
                continue
            if c in linhas:
                linhas.remove(c)
            linhas.insert(0, c)   # campeão e vice da lista (Wikipédia) entram mesmo sem jogo na fonte
            if c not in nomes_fonte or not any(ed.ano_inicio in a for a in nomes_fonte[c].values()):
                nomes_fonte[c][f"wikipedia:{nome or c}"].append(ed.ano_inicio)
        for k, c in enumerate(linhas, 1):
            r = camp[c]
            L["classificacao_final"].append([ed.temporada, k, c, r[0], r[1], r[2], r[3], r[4], r[5], r[6], 0,
                                             "campeao" if c == campeao else "vice" if c == vice else "",
                                             "calculada (fase alcançada, pontos, vitórias, saldo, gols pró)", ""])
        # tabelas publicadas (fases de grupos)
        for t in tabs:
            for r in t.linhas:
                c = copa.clube(r["nome"], ed.ano_inicio) if r.get("nome") else None
                if c:   # clube só da tabela (sem jogo na fonte, Copa Venezuela antiga) também vai para o clubes.csv
                    nomes_fonte[c][f"rsssf:{r['nome']}"].append(ed.ano_inicio)
                L["tabelas_publicadas"].append([ed.temporada, t.fase or padrao, t.grupo, r.get("pos"), r.get("nome"), c,
                                                r.get("j"), r.get("v"), r.get("e"), r.get("d"), r.get("gp"), r.get("gc"), r.get("pts"),
                                                f"RSSSF ({t.fonte}, linha {t.linha})"])
        # artilheiros: contagem dos gols com autor (quando quase todos os gols têm autor)
        if gols_ed and autor_ed >= 0.95 * gols_ed:
            cont = Counter((g[2], g[1]) for g in L["gols"] if g[0].startswith(eid + "-") and g[5] != "contra")
            topo = max(cont.values(), default=0)
            for (jog, c), ng in sorted(cont.items()):
                if ng == topo:
                    L["artilheiros"].append([ed.temporada, jog, c, ng, "contagem dos gols com autor (RSSSF)"])
        wiki = copa.campeoes_wiki.get(ed.temporada)
        wiki_c = copa.clube(wiki, ed.ano_inicio) if wiki else None
        obs_conf = f"campeão {campeao} (RSSSF: final; Wikipédia: {wiki or '—'})" + ("" if not wiki or wiki_c == campeao else
                                                                                   " — DIVERGE")
        L["conferencia"].append([ed.temporada, len(jogos), len(jogos), 0, 0, gols_ed, autor_ed, obs_conf])
        L["edicoes"].append([ed.temporada, ed.ano_inicio, ed.ano_fim, ed.nome_oficial, len(linhas), 3,
                             "mata-mata" if all(r[3] == "mata_mata" for r in L["fases"] if r[0] == ed.temporada) else
                             "fase de grupos e mata-mata", campeao or "", vice or "", " + ".join(dict.fromkeys(_fonte(j["x"].texto)[0] for j in jogos)) or "RSSSF", ed.obs])
        rel.append(f"| {ed.temporada} | {len(jogos)} | {', '.join(fases)} | {campeao or '—'} | {vice or '—'} | "
                   f"{wiki or '—'}{'' if not wiki or wiki_c == campeao else ' (DIVERGE)'} | {autor_ed} de {gols_ed} |")
    # clubes
    for c in sorted(nomes_fonte):
        cidade, regiao = copa.clubes.get(c, ("", ""))
        nf = "|".join(f"{k}:{min(a)}-{max(a)}" if min(a) != max(a) else f"{k}:{min(a)}"
                      for k, a in sorted(nomes_fonte[c].items()))
        L["clubes"].append([c, regiao, cidade, copa.competicao["pais"], nf])
    cab = {
        "edicoes.csv": ["temporada", "ano_inicio", "ano_fim", "nome_oficial", "num_clubes", "pontos_vitoria", "formato", "campeao",
                        "vice", "fontes", "observacao"],
        "fases.csv": ["temporada", "ordem", "fase", "tipo", "num_grupos", "formato_serie", "criterio"],
        "partidas.csv": COLUNAS_PARTIDAS,
        "gols.csv": ["partida_id", "clube", "jogador", "minuto", "acrescimo", "tipo", "fonte"],
        "cartoes.csv": ["partida_id", "clube", "jogador", "minuto", "acrescimo", "cor", "fonte"],
        "classificacao_final.csv": ["temporada", "posicao", "clube", "jogos", "vitorias", "empates", "derrotas", "gols_pro",
                                    "gols_contra", "pontos", "ajuste_pontos", "situacao", "fonte", "observacao"],
        "clubes.csv": ["clube", "regiao", "cidade", "pais", "nomes_fonte"],
        "artilheiros.csv": ["temporada", "jogador", "clube", "gols", "fonte"],
        "conferencia.csv": ["temporada", "jogos", "jogos_esperados", "tabelas_conferidas", "tabelas_divergentes", "gols",
                            "gols_com_autor", "observacao"],
        "tabelas_publicadas.csv": ["temporada", "fase", "grupo", "posicao", "nome_fonte", "clube", "jogos", "vitorias", "empates",
                                   "derrotas", "gols_pro", "gols_contra", "pontos", "fonte"],
    }
    for arq, colunas in cab.items():
        with open(pacote / arq, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(colunas)
            for l in L[arq[:-4]]:
                w.writerow(["" if x is None else x for x in l])
    rel += ["", f"**Sobre a competição:** {copa.competicao.get('observacao', '')}", "", "**Observações por edição:**", ""]
    rel += [f"- {ed.temporada}: {ed.obs}" for ed in copa.edicoes if ed.obs]
    rel += ["", "**Regras do pacote:** W.O. com o placar dado e `resultado_especial` \"wo\"; pênaltis nos campos de pênaltis "
            "(o jogo fica empatado); campeão = vencedor da final (agregado, depois pênaltis), conferido com a Wikipédia; "
            "classificação calculada (fase alcançada, pontos, vitórias, saldo, gols pró); artilheiros pela contagem dos "
            "gols com autor quando ao menos 95% dos gols têm autor. Sem cartões; público e estádio só nos jogos ligados à "
            "ESPN (a RSSSF não traz)."]
    if casados_espn:
        rel += ["", f"**ESPN:** jogos ligados a um jogo da ESPN (mesmos clubes, mando e placar; data até 1 dia), de onde vêm "
                f"hora, estádio, cidade e público; {datas_espn} jogos sem data na RSSSF ou na Wikipédia ganharam a da ESPN"
                + (f"; {datas_corrigidas} datas e {mandos_corrigidos} mandos trocados pelos da ESPN (o estádio confirma; "
                   "nota na observação)" if copa.espn_corrige else "") + ". "
                "Por edição: " + "; ".join(casados_espn) + "."]
    if sem_nome_espn:
        rel += ["", "**Nomes da ESPN sem clube (esses jogos não casam):** " +
                ", ".join(f"{n} ({k})" for n, k in sorted(sem_nome_espn.items()))]
    if sem_nome:
        rel += ["", "**Linhas sem clube reconhecido (fora do pacote):**", ""] + [f"- {s}" for s in sem_nome]
    relatorio.write_text("\n".join(rel) + "\n", encoding="utf-8")
    print(f"{copa.slug}: {len(copa.edicoes)} edições, {len(L['partidas'])} jogos, {len(L['clubes'])} clubes; "
          f"{len(sem_nome)} linhas sem clube")
    for s in sem_nome[:40]:
        print("  sem clube:", s)
    if copa.espn:
        print(f"  ESPN: {sum(int(c.split(': ')[1].split(' ')[0]) for c in casados_espn)} jogos casados, {datas_espn} datas novas, "
              f"{datas_corrigidas} datas e {mandos_corrigidos} mandos trocados; "
              f"{len(sem_nome_espn)} nomes da ESPN sem clube")
