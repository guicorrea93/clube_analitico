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
    trocas: list[tuple[str, str]] = field(default_factory=list)   # (regex, troca) nas linhas antes de ler: "[Mar 18 We]" -> "[Mar 18]"


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
    for pagina, ini, fim in ed.trechos:
        ls = list(copa.linhas(pagina))
        fim = len(ls) if fim is None else fim
        # "Cúcuta  o/w Tolima  [awarded 0-3]" (Copa Colombia 2020): o leitor comum só conhece "w/o"; vira "awd"
        trecho = [re.sub(r"(?<=\S)\s+o/w\s+(?=\S)", "  awd ", l) for l in ls[ini:fim]]
        for rx, troca in copa.trocas:
            trecho = [re.sub(rx, troca, l) for l in trecho]
        a0, a1 = ed.anos_leitura or (ed.ano_inicio, ed.ano_fim)
        j, t = rsssf_sul.ler([""] * ini + trecho, a0, a1, fases=ed.fases or copa.fases, ignorar=copa.ignorar)
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
        fase_tab = {t.fase or padrao for t in tabs}
        fases_pontos: set[str] = set()   # a rodada só vale nelas (no mata-mata, o "Round 3" herdado não é rodada)
        # fases dos jogos e das tabelas (a 1ª fase de 2022 da Copa Paraguay só tem as tabelas das zonas)
        fases = sorted({j["fase"] for j in jogos} | fase_tab, key=lambda f: (ordem_fase.get(f, 0), min(
            [j["x"].linha for j in jogos if j["fase"] == f] + [t.linha for t in tabs if (t.fase or padrao) == f])))
        for k, f in enumerate(fases, 1):
            js = [j for j in jogos if j["fase"] == f]
            grupos = sorted({j["grupo"] for j in js if j["grupo"]} | {t.grupo for t in tabs if (t.fase or padrao) == f and t.grupo})
            pares = Counter(frozenset((j["m"], j["v"])) for j in js) or Counter({frozenset(): 1})
            liga = f in fase_tab or ed.pontos   # fase com tabela publicada é de pontos (grupos); sem tabela, mata-mata
            tipo = ("grupos" if len(grupos) >= 2 else "liga") if liga else "mata_mata"
            serie = "pontos_corridos" if liga else ("ida_volta" if max(pares.values()) > 1 else "jogo_unico")
            L["fases"].append([ed.temporada, k, f, tipo, len(grupos) if tipo == "grupos" else None, serie, ""])
            if liga:
                fases_pontos.add(f)
        # campeão e vice: a final
        final = [j for j in jogos if j["fase"] == "Final"]
        campeao, vice = _vencedor(final) if final else (None, None)
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
                    sep = copa.autores.separar(x.gols_texto, j["gm"], j["gv"])
            if sep:
                for lado, gs in ((j["m"], sep[0]), (j["v"], sep[1])):
                    for g in gs:
                        L["gols"].append([pid, lado, g["jogador"], g["minuto"], g["acrescimo"], g["tipo"], "RSSSF"])
                        autor_ed += 1
            obs = [j["obs"]] + ([x.nota] if x.nota and not j["obs"] and not re.search(r"\bpen\b", x.nota) else [])
            L["partidas"].append([pid, ed.temporada, j["fase"], j["grupo"], x.rodada if j["fase"] in fases_pontos else None, x.data, None, j["m"], j["v"], j["gm"],
                                  j["gv"], j["pm"], j["pv"], j["esp"], None, None, None, *_fonte(x.texto),
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
        if ed.pontos and not final:   # edição de pontos corridos: campeão e vice pela classificação
            campeao, vice = (linhas + [None, None])[:2]
        for c in (vice, campeao):
            if c in linhas:
                linhas.remove(c)
                linhas.insert(0, c)
        for k, c in enumerate(linhas, 1):
            r = camp[c]
            L["classificacao_final"].append([ed.temporada, k, c, r[0], r[1], r[2], r[3], r[4], r[5], r[6], 0,
                                             "campeao" if c == campeao else "vice" if c == vice else "",
                                             "calculada (fase alcançada, pontos, vitórias, saldo, gols pró)", ""])
        # tabelas publicadas (fases de grupos)
        for t in tabs:
            for r in t.linhas:
                c = copa.clube(r["nome"], ed.ano_inicio) if r.get("nome") else None
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
        L["edicoes"].append([ed.temporada, ed.ano_inicio, ed.ano_fim, ed.nome_oficial, len(clubes), 3,
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
            "gols com autor quando ao menos 95% dos gols têm autor. Sem cartões, público e estádio (a RSSSF não traz)."]
    if sem_nome:
        rel += ["", "**Linhas sem clube reconhecido (fora do pacote):**", ""] + [f"- {s}" for s in sem_nome]
    relatorio.write_text("\n".join(rel) + "\n", encoding="utf-8")
    print(f"{copa.slug}: {len(copa.edicoes)} edições, {len(L['partidas'])} jogos, {len(L['clubes'])} clubes; "
          f"{len(sem_nome)} linhas sem clube")
    for s in sem_nome[:40]:
        print("  sem clube:", s)
