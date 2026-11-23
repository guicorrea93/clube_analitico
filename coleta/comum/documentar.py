"""Gera a documentação completa da coleta Brasil (agente 2) em coleta/comum/documentacao/.

Uma ficha por competição (<slug>.md) e o índice (README.md). Tudo sai do que existe de fato:
- do pacote (data/coleta/<slug>/pacote/): o que cada campo cobre, década a década; formato ao longo do tempo (clubes,
  pontos por vitória, nome oficial, fases e grupos); campeões, acessos, rebaixados, punições; artilheiros; conferência
  com as tabelas publicadas;
- dos módulos da competição (coleta/<slug>/: importar.py, explicacoes.py, rsssf_*.py, clubes_*.py e os leitores extras):
  todas as correções e decisões, com o motivo (CORRIGE_OGOL, NOME_MANUAL, JOGOS_ANULADOS, AJUSTE_MANUAL, EXPLICACOES,
  MANUAL_NOVO, as correções das páginas da RSSSF...);
- do relatório (docs/coleta/<slug>.md): fontes, regras e o que não deu para coletar;
- do banco (db/futebol.db, só leitura): se a competição já está carregada;
- de PENDENCIAS, abaixo: o que falta, mantido à mão.

Rode depois de cada importação ou correção: python coleta/comum/documentar.py
"""
from __future__ import annotations

import csv
import importlib
import json
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
SAIDA = AQUI / "documentacao"
COMPETICOES = ["bra-serie-c", "bra-serie-d", "bra-copa-do-brasil", "bra-sp-1", "bra-sp-2", "bra-rj-1"]

# o que falta em cada competição (manter à mão; a ordem geral está em COMECE-AQUI.md)
PENDENCIAS: dict[str, list[str]] = {
    "bra-serie-c": [
        "Achados da revisão SC-001 a SC-023 e CL-002/CL-004/CL-005/CL-012: tratados (docs/coleta/pedidos.md, partes 2 e 4, "
        "edições de 2026 e identidade). A revisão ainda não reconferiu (docs/revisao/achados.csv segue com 'aberto').",
        "Autores dos gols antes de 2012 e cartões: só jogo a jogo, pela ficha do ogol (~8 mil pedidos, ~3 h). Prioridade "
        "baixa (cartões, mais baixa ainda), decisão do Guilherme (20/11/2026).",
    ],
    "bra-serie-d": [
        "Achados da revisão SD-001 a SD-021: tratados (docs/coleta/pedidos.md, parte 3, parte 4 e edições de 2026). A "
        "revisão ainda não reconferiu.",
        "Cartões: só jogo a jogo, pela ficha do ogol (prioridade baixa).",
    ],
    "bra-copa-do-brasil": [
        "Achados da revisão CB-001 a CB-015: tratados (docs/coleta/pedidos.md, partes 1 e 4). A revisão ainda não reconferiu.",
        "Jogo preliminar de 1999 (Santa Cruz 1-0 Náutico, CB-007): entrou sem data; nenhuma fonte achada dá o dia.",
        "Autores dos gols antes de 2013 e cartões: jogo a jogo, pela ficha do ogol (prioridade baixa).",
    ],
    "bra-sp-1": [
        "Corrigidos em 23/11 (\"ERRADO NO AR\" do plano docs/revisao/plano-coleta-brasil.md): SP-011 (jogo falso de 1928 "
        "LAF), SP-002, SP-007 e SP-008 (ORDEM completo, FASE_ANO e FASE_JOGO, vice do quadrangular final, desempate pela "
        "Fase final; menos 2024 e 2025, que esperam as fases da FPF), QS-001 e SP-010 (CLUBES_FORA), QS-006 e QS-005 "
        "(JOGOS_FORA, JOGOS_EXTRA_WO, VICE_OFICIAL), QS-015 e SP-013 (PONTOS_FORA_DE_CAMPO; W.O. conta na campanha, "
        "SP-016), SP-009 (Corinthians de Santo André) e SP-012 (1942). SP-001: 1973 com co_campeao Santos e vice "
        "Palmeiras (D-07).",
        "Resto do plano (docs/revisao/plano-coleta-brasil.md, seção do Paulista): SP-003 (3º lugar à mão), SP-004 (2026), "
        "SP-008 em 2024 e 2025 (fases pela API da FPF), SP-014, SP-015 (rebaixados), SP-017 a SP-024, QS-002 a QS-014, "
        "SP-026 e SP-027 (D-23). Só quando o Guilherme mandar.",
        "Autores dos gols e cartões nos anos sem RSSSF com autores: jogo a jogo, pela ficha do ogol (prioridade baixa).",
    ],
    "bra-sp-2": [
        "Commit das edições antigas e da documentação (22/11/2026): pedir o ok do Guilherme. Depois, o agente 1 carregar a A2 "
        "no banco (recados no fim de docs/coleta/pedidos.md).",
        "Jogos que faltam (1947-1966 fora o que a Wikipédia traz; 1988: 69 sem placar; 1989: 2ª e 3ª fases; 1990: 1ª a 3ª; "
        "1991: 1ª fase; 1992: 1ª fase; 1993 e 1994): só em jornais da época (Hemeroteca Digital, acervos do Estadão e da "
        "Folha), em imagem. Só se o Guilherme pedir.",
        "Os mesmos achados de vice e ordem final do Paulista (SP-002, SP-007, SP-008) podem valer na A2: conferir quando "
        "tratar o bra-sp-1 (o importador é cópia do dele).",
    ],
    "bra-rj-1": [
        "Autores dos gols: só 3.383 (quase todos de 2010 em diante). Nas outras décadas a página não traz os autores ou traz "
        "num formato que o leitor ainda não junta ao jogo (\"Gols: ...\" na linha de baixo, nos anos 1900).",
        "127 tabelas divergentes a explicar (ou corrigir) uma a uma no relatório; jogos avulsos do fim das páginas (súmulas sem "
        "par na lista: 1915, 1917-1919, 1924 AMEA, 1925, 1938, 1944, 1959, 1976) a conferir.",
        "Artilheiros de 2015 em diante: a lista da RSSSF (rjtops.htm) parou em 2014; a Wikipédia em português tem a tabela "
        "ano a ano (pt_lista.txt), ainda não lida.",
        "Mesma correção dos artilheiros no Paulista: lá a lista da RSSSF nunca era usada (chave pelo ano em número), o que deve "
        "explicar o SP-024.",
    ],
}

# dicionários de decisões dos módulos de cada competição -> rótulo da seção
DICIONARIOS = {
    "BASE_OGOL": "Temporadas com o ogol como base dos jogos",
    "TABELAS_PARCIAIS": "Tabelas publicadas parciais (fora da conferência)",
    "SO_CLASSIFICACAO": "Temporadas sem os jogos na RSSSF (só as tabelas)",
    "WIKI_JUNTAR": "Temporadas completadas com jogos da Wikipédia",
    "FORMATO_INCOMPLETO": "Temporadas com parte dos jogos",
    "OBS_EDICAO": "Observações das edições",
    "CORRIGE_OGOL": "Clube trocado pelo ogol numa temporada (código -> código)",
    "CORRIGE_OGOL_JOGO": "Clube trocado pelo ogol num jogo",
    "NOME_MANUAL": "Nome da página casado à mão com o clube",
    "NOME_MANUAL_GRUPO": "Nome da página casado à mão, por grupo",
    "MANUAL_ANTIGO": "Clube das edições antigas casado à mão",
    "NOME_ANTIGO": "Nome curto das fases seguintes casado à mão (edições antigas)",
    "NOME_WIKI": "Nome da Wikipédia casado à mão",
    "NOME_CORRIGIDO": "Grafias da página corrigidas",
    "CIDADES": "Cidades abreviadas nas tabelas antigas",
    "CIDADE_DO_CLUBE": "Cidade de um clube corrigida",
    "CIDADE_DA_LINHA": "Cidade de uma linha de tabela corrigida",
    "JOGOS_FORA": "Jogos que ficam fora",
    "JOGOS_ANULADOS": "Jogos anulados",
    "RSSSF_FORA": "Clubes com todos os jogos fora",
    "OGOL_IGNORAR": "Jogos do ogol ignorados",
    "PLACAR_MANUAL": "Placares e jogos corrigidos à mão",
    "CORRECAO_JOGO": "Jogos corrigidos (placar, data, mando)",
    "AJUSTE_MANUAL": "Punições em pontos",
    "AJUSTE_FORA": "Punições que não valem",
    "FASE_ANO": "Fases da página renomeadas (por temporada)",
    "GRUPO_ANO": "Grupos montados à mão (por temporada)",
    "FASE": "Seções da Wikipédia -> fase e grupo",
    "EXPLICACOES": "Ocorrências explicadas, por temporada",
    "MANUAL_DB": "Clube do ogol casado à mão com o nome do banco",
    "MANUAL_NOVO": "Nome de exibição de clube novo, dado à mão",
    "FICHA_CORRIGIDA": "Fichas do ogol com cidade ou estado errados",
    "ANOS_A_PARTE": "Anos com torneio à parte na página (fica fora)",
    "TURNOS": "Anos com turnos (Taça Guanabara, Taça Rio) nos títulos das fases",
    "LETRAS": "Letras trocadas na página da RSSSF",
}

CAMPOS_COBERTURA = [("data", "data"), ("hora", "hora"), ("rodada", "rodada"), ("estadio", "estádio"), ("cidade", "cidade"),
                    ("publico", "público")]


def ler(slug: str, nome: str) -> list[dict]:
    arq = RAIZ / "data" / "coleta" / slug / "pacote" / f"{nome}.csv"
    if not arq.exists():
        return []
    with arq.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def modulos(slug: str) -> list:
    """Carrega os módulos de coleta/<slug>/ sem rodar a importação. Os módulos das competições têm os mesmos nomes
    (importar, edicoes, pacote...) e o leitor comum da RSSSF guarda as correções de quem o carregou: limpa entre uma e
    outra."""
    pasta = RAIZ / "coleta" / slug
    nomes = {p.stem for d in COMPETICOES for p in (RAIZ / "coleta" / d).glob("*.py")} | {"rsssf", "gols", "ogol", "registro"}
    for m in [m for m in sys.modules if m in nomes]:
        del sys.modules[m]
    sys.path[:] = [p for p in sys.path if Path(p).name not in COMPETICOES]
    sys.path.insert(0, str(pasta))
    if str(AQUI) not in sys.path:
        sys.path.insert(1, str(AQUI))
    saida = []
    for arq in sorted(pasta.glob("*.py")):
        if arq.stem.startswith("baixar") or arq.stem in ("pacote",):
            continue
        saida.append(importlib.import_module(arq.stem))
    return saida


def pct(a: int, b: int) -> str:
    return "—" if not b else f"{100 * a / b:.0f}%"


def num(x) -> int:
    try:
        return int(x)
    except (TypeError, ValueError):
        return 0


def texto_valor(v) -> str:
    """Valor de um dicionário de decisões: o motivo (texto mais longo) e os códigos/números curtos antes."""
    if isinstance(v, str):
        return v
    if isinstance(v, dict):
        motivo = v.get("motivo", "")
        resto = ", ".join(f"{k}={x}" for k, x in v.items() if k != "motivo")
        return (f"[{resto}] " if resto else "") + str(motivo)
    if isinstance(v, (tuple, list)):
        textos = [x for x in v if isinstance(x, str)]
        motivo = max(textos, key=len) if textos else ""
        outros = [str(x) for x in v if x is not None and not (isinstance(x, str) and x == motivo)]
        return (f"[{', '.join(outros)}] " if outros else "") + motivo
    return str(v)


def texto_chave(k) -> str:
    return " · ".join(str(x) for x in k) if isinstance(k, tuple) else str(k)


def decada(t: str) -> str:
    return f"{t[:3]}0s"


def no_banco(slug: str) -> str:
    """Edições e jogos da competição no db/futebol.db (só leitura)."""
    con = sqlite3.connect(f"file:{RAIZ / 'db' / 'futebol.db'}?mode=ro", uri=True)
    r = con.execute("SELECT (SELECT count(*) FROM edicao e WHERE e.competicao_id = c.competicao_id), (SELECT count(*) FROM partida p "
                    "JOIN edicao e ON p.edicao_id = e.edicao_id WHERE e.competicao_id = c.competicao_id) FROM competicao c "
                    "WHERE c.slug = ?", (slug,)).fetchone()
    con.close()
    return f"sim ({r[0]} edições, {r[1]} jogos)" if r else "não"


def paragrafo(rel: str, rotulo: str) -> str | None:
    m = re.search(rf"\*\*{rotulo}:\*\*\s*(.*?)\n\s*\n", rel, re.S)
    return re.sub(r"\s*\n\s*", " ", m.group(1)).strip() if m else None


def ficha(slug: str) -> tuple[str, dict]:
    mods = modulos(slug)
    comp = json.loads((RAIZ / "data" / "coleta" / slug / "pacote" / "competicao.json").read_text(encoding="utf-8"))
    ed, part, gols, cart = ler(slug, "edicoes"), ler(slug, "partidas"), ler(slug, "gols"), ler(slug, "cartoes")
    clf, fases, art, conf = ler(slug, "classificacao_final"), ler(slug, "fases"), ler(slug, "artilheiros"), ler(slug, "conferencia")
    clubes, pub, rod = ler(slug, "clubes"), ler(slug, "tabelas_publicadas"), ler(slug, "classificacao_rodada")
    temporada_de = {p["id"]: p["temporada"] for p in part}
    gols_por_t = Counter(temporada_de.get(g["partida_id"]) for g in gols)
    cart_por_t = Counter(temporada_de.get(c["partida_id"]) for c in cart)
    total_gols = sum(num(p["gols_mandante"]) + num(p["gols_visitante"]) for p in part)
    jogos_t = Counter(p["temporada"] for p in part)
    copa = comp.get("tipo") == "copa" or "copa" in slug
    banco = no_banco(slug)

    out = [f"# {comp['nome']} (`{slug}`) — documentação", "",
           f"Gerado por `python coleta/comum/documentar.py` a partir do pacote `data/coleta/{slug}/pacote/` e dos módulos de "
           f"`coleta/{slug}/`. O relatório da importação, com as ocorrências temporada a temporada, está em "
           f"`docs/coleta/{slug}.md`.", ""]

    # ---- 1. o que temos
    sem_jogos = [e["temporada"] for e in ed if not jogos_t.get(e["temporada"])]
    incompletas = [e["temporada"] for e in ed if "incomplet" in (e["formato"] or "") and jogos_t.get(e["temporada"])]
    out += ["## 1. O que temos", "",
            f"- **Edições:** {len(ed)}, de {ed[0]['temporada']} a {ed[-1]['temporada']}"
            + (f"; sem nenhum jogo: {', '.join(sem_jogos)}" if sem_jogos else "")
            + (f"; com parte dos jogos: {', '.join(incompletas)}" if incompletas else "") + ".",
            f"- **Jogos:** {len(part)}; **gols:** {total_gols}; **gols com autor:** {len(gols)} ({pct(len(gols), total_gols)}); "
            f"**cartões:** {len(cart)}.",
            f"- **Clubes:** {len(clubes)}; **artilheiros:** {len({a['temporada'] for a in art})} temporadas com artilheiro "
            f"({len(art)} linhas, com empates).",
            f"- **Classificação final:** {len({c['temporada'] for c in clf})} temporadas; **rodada a rodada:** "
            f"{len({r['temporada'] for r in rod})} temporadas.",
            f"- **Tabelas publicadas guardadas para conferência:** {len(pub)} linhas.",
            f"- **No banco (`db/futebol.db`):** {banco}.",
            f"- **Observação da competição:** {comp.get('observacao') or '—'}", ""]

    # ---- 2. fontes e regras (do relatório)
    rel = (RAIZ / "docs" / "coleta" / f"{slug}.md").read_text(encoding="utf-8")
    out += ["## 2. Fontes e regras", ""]
    for rot in ("Temporadas", "Fontes", "Regras", "Desempate", "Edições sem os jogos"):
        if (p := paragrafo(rel, rot)):
            out += [f"**{rot}:** {p}", ""]

    # ---- 3. conferência
    ok = sum(num(c["tabelas_conferidas"]) for c in conf)
    div = sum(num(c["tabelas_divergentes"]) for c in conf)
    com_div = [c["temporada"] for c in conf if num(c["tabelas_divergentes"]) > 0]
    sem_tab = [c["temporada"] for c in conf if not num(c["tabelas_conferidas"]) and not num(c["tabelas_divergentes"])]
    faltam = [f"{c['temporada']} ({c['jogos']} de {c['jogos_esperados']})" for c in conf
              if c["jogos_esperados"] and num(c["jogos"]) < num(c["jogos_esperados"])]
    out += ["## 3. Conferência", "",
            f"- Cada temporada é comparada com as tabelas publicadas ({'RSSSF; Wikipédia em 1965 e 1990' if slug == 'bra-sp-2' else 'RSSSF'}): {ok} tabelas "
            f"fecham com os jogos e {div} divergem (cada divergência é explicada no relatório, na temporada).",
            f"- Temporadas com alguma tabela divergente: {', '.join(com_div) or 'nenhuma'}.",
            f"- Temporadas sem tabela para conferir: {', '.join(sem_tab) or 'nenhuma'}.",
            f"- Temporadas com menos jogos do que o ogol: {', '.join(faltam) or 'nenhuma'}.", ""]

    # ---- 4. cobertura por década
    por_dec = defaultdict(list)
    for p in part:
        por_dec[decada(p["temporada"])].append(p)
    gols_dec, golsaut_dec, cart_dec = Counter(), Counter(), Counter()
    for p in part:
        gols_dec[decada(p["temporada"])] += num(p["gols_mandante"]) + num(p["gols_visitante"])
    for t, n in gols_por_t.items():
        if t:
            golsaut_dec[decada(t)] += n
    for t, n in cart_por_t.items():
        if t:
            cart_dec[decada(t)] += n
    out += ["## 4. Cobertura de cada campo, por década", "",
            "Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).", "",
            "| Década | Jogos | " + " | ".join(r for _, r in CAMPOS_COBERTURA) + " | gols c/ autor | cartões/jogo |",
            "|" + "---|" * (len(CAMPOS_COBERTURA) + 4)]
    for d in sorted(por_dec):
        ps = por_dec[d]
        cel = [pct(sum(1 for p in ps if p.get(c)), len(ps)) for c, _ in CAMPOS_COBERTURA]
        out.append(f"| {d} | {len(ps)} | " + " | ".join(cel) + f" | {pct(golsaut_dec[d], gols_dec[d])} | {cart_dec[d] / len(ps):.1f} |")
    fontes_j = Counter(p["fonte"] for p in part)
    out += ["", "**Fonte de cada jogo:** " + "; ".join(f"{f or '—'}: {n}" for f, n in fontes_j.most_common()) + ".", ""]

    # ---- 5. formato ao longo do tempo
    def faixas(chave_fn):
        res, atual = [], None
        for e in ed:
            v = chave_fn(e)
            if atual and atual[0] == v:
                atual[2] = e["temporada"]
            else:
                atual = [v, e["temporada"], e["temporada"]]
                res.append(atual)
        return res
    out += ["## 5. Formato ao longo do tempo", "", "**Número de clubes:**", ""]
    out += [f"- {a if a == b else a + ' a ' + b}: {v} clubes" for v, a, b in faixas(lambda e: e["num_clubes"])]
    out += ["", "**Pontos por vitória:**", ""]
    out += [f"- {a if a == b else a + ' a ' + b}: {v}" for v, a, b in faixas(lambda e: e["pontos_vitoria"])]
    out += ["", "**Nome oficial:**", ""]
    out += [f"- {a if a == b else a + ' a ' + b}: {v}" for v, a, b in faixas(lambda e: e["nome_oficial"])]
    out += ["", "**Formato de cada edição** (fases na ordem; grupos; mata-mata):", ""]
    out += [f"- {a if a == b else a + ' a ' + b}: {v}" for v, a, b in faixas(lambda e: e["formato"])]
    por_t = defaultdict(list)
    for f in fases:
        por_t[f["temporada"]].append(f)
    nomes_fases = Counter(f["fase"] for f in fases)
    out += ["", "**Fases que aparecem** (número de temporadas): " + "; ".join(f"{f} ({n})" for f, n in nomes_fases.most_common()) + "."]
    crit = Counter(f["criterio"] for f in fases if f["criterio"])
    if crit:
        out += ["", "**Critério de desempate:** " + "; ".join(f"{c} ({n} fases)" for c, n in crit.most_common()) + "."]
    obs = [(e["temporada"], e["observacao"]) for e in ed if e["observacao"]]
    out += ["", "**Observações das edições:**", ""]
    out += [f"- {t}: {o}" for t, o in obs] or ["- nenhuma"]
    out.append("")

    # ---- 6. campeões, acessos, rebaixados e punições
    camp = Counter(e["campeao"] for e in ed if e["campeao"])
    sem_campeao = [e["temporada"] for e in ed if not e["campeao"]]
    sit = defaultdict(Counter)
    for c in clf:
        if c["situacao"]:
            sit[c["situacao"]][c["clube"]] += 1
    puni = [(c["temporada"], c["clube"], c["ajuste_pontos"]) for c in clf if c["ajuste_pontos"] not in ("", "0")]
    out += ["## 6. Campeões, acessos, rebaixados e punições", "", "**Títulos:**", ""]
    out += [f"- {c}: {n}" for c, n in camp.most_common()]
    if sem_campeao:
        out += [f"- Sem campeão: {', '.join(sem_campeao)}"]
    for s, rot in (("acesso", "Acessos"), ("rebaixado", "Rebaixamentos")):
        if sit.get(s):
            out += ["", f"**{rot}:** {sum(sit[s].values())} no total; quem mais teve: "
                    + ", ".join(f"{c} ({n})" for c, n in sit[s].most_common(8)) + "."]
        elif not copa:
            out += ["", f"**{rot}:** nenhum marcado no pacote."]
    out += ["", "**Punições em pontos:**", ""]
    out += [f"- {t}: {c} {a}" for t, c, a in puni] or ["- nenhuma"]
    out.append("")

    # ---- 7. correções e decisões
    out += ["## 7. Correções e decisões (com o motivo)", "",
            f"Registradas nos módulos de `coleta/{slug}/`; cada uma também aparece no relatório, na temporada.", ""]
    achou = False
    for nome, rotulo in DICIONARIOS.items():
        for mod in mods:
            v = getattr(mod, nome, None)
            if not v or not isinstance(v, (dict, set, frozenset, list)):
                continue
            achou = True
            out += [f"### {rotulo} (`{mod.__name__}.{nome}`)", ""]
            if isinstance(v, dict):
                for k, x in v.items():
                    if isinstance(x, list) and all(isinstance(i, str) for i in x):
                        out += [f"- **{texto_chave(k)}:** " + " / ".join(x)]
                    elif isinstance(x, dict) and "motivo" not in x:
                        out += [f"- **{texto_chave(k)}:** " + "; ".join(f"{a} → {b}" for a, b in x.items())]
                    else:
                        out += [f"- **{texto_chave(k)}:** {texto_valor(x)}"]
            else:
                out += [f"- {', '.join(map(str, sorted(v)))}"]
            out.append("")
            break
    rs = sys.modules.get("rsssf")
    if rs is not None and getattr(rs, "CORRECOES", None):
        out += [f"### Páginas da RSSSF corrigidas na leitura (`rsssf.CORRECOES`, registradas em `coleta/{slug}/rsssf_*.py`)", ""]
        for arq, lista in sorted(rs.CORRECOES.items()):
            motivos = list(dict.fromkeys(m for *_, m in lista if m))
            out += [f"- **{arq}:** " + "; ".join(motivos)]
        out.append("")
        achou = True
    if not achou:
        out += ["- nenhuma", ""]

    # ---- 8. limites e pendências
    m = re.search(r"## O que não deu para coletar\s*\n(.*?)(?:\n## |\Z)", rel, re.S)
    out += ["## 8. O que não deu para coletar", "", (m.group(1).strip() if m else "- (ver relatório)"), "",
            "## 9. Pendências e próximos passos", ""]
    out += [f"- {p}" for p in PENDENCIAS.get(slug, [])] or ["- nenhuma"]

    # ---- 10. arquivos e comandos
    pasta = RAIZ / "coleta" / slug
    def doc1(arq: Path) -> str:
        m = re.match(r'\s*(?:from __future__[^\n]*\n\s*)?"""(.*?)(?:\n\n|""")', arq.read_text(encoding="utf-8"), re.S)
        return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    out += ["", "## 10. Arquivos e comandos", "", "| Arquivo | O que faz |", "|---|---|"]
    out += [f"| `coleta/{slug}/{a.name}` | {doc1(a)[:220]} |" for a in sorted(pasta.glob("*.py"))]
    fontes_dir = sorted(p.name for p in (RAIZ / "data" / "coleta" / slug).iterdir() if p.is_dir() and p.name != "pacote")
    baixar = sorted(a.name for a in pasta.glob("baixar*.py"))
    out += ["",
            f"- Fontes baixadas: `data/coleta/{slug}/` ({', '.join(fontes_dir)}). Pacote: `data/coleta/{slug}/pacote/`. "
            f"Relatório: `docs/coleta/{slug}.md`.",
            "- Código comum: `coleta/comum/` (`rsssf.py` leitor das páginas da RSSSF Brasil, `ogol.py` calendários e fichas, "
            "`gols.py` autores dos gols, `registro.py` cadastro comum de nomes `data/coleta/comum/clubes_ogol.json`, `baixar.py` "
            "download educado).",
            "- Refazer do zero (da raiz do `clube_analitico`, logs no scratchpad):",
            ""]
    out += [f"  - `python coleta/{slug}/{b}` (ver o docstring)" for b in baixar]
    out += [f"  - `python coleta/{slug}/importar.py` (grava o pacote e o relatório; `importar.py <ano>` só mostra, sem gravar)",
            f"  - `python coleta/comum/testar_carga.py {slug} <pasta temporária>` (deve terminar com `-> OK`)",
            "  - `python coleta/comum/documentar.py`", ""]
    resumo = {"slug": slug, "nome": comp["nome"], "edicoes": len(ed), "de": ed[0]["temporada"], "ate": ed[-1]["temporada"],
              "jogos": len(part), "gols_autor": len(gols), "cartoes": len(cart), "clubes": len(clubes), "tabelas_ok": ok,
              "tabelas_div": div, "pendencias": len(PENDENCIAS.get(slug, [])), "banco": banco}
    return "\n".join(out) + "\n", resumo


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    SAIDA.mkdir(exist_ok=True)
    resumos = []
    for slug in COMPETICOES:
        txt, r = ficha(slug)
        (SAIDA / f"{slug}.md").write_text(txt, encoding="utf-8")
        resumos.append(r)
        print(f"{slug}: {r['edicoes']} edições, {r['jogos']} jogos", flush=True)
    idx = ["# Coleta Brasil (agente 2) — documentação", "",
           "Gerado por `python coleta/comum/documentar.py`. Uma ficha por competição, com tudo o que o pacote tem, a cobertura "
           "de cada campo década a década, o formato ao longo do tempo, campeões, acessos, rebaixados e punições, todas as "
           "correções e decisões com o motivo, o que não deu para coletar, as pendências e os comandos para refazer.", "",
           "Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum/COMECE-AQUI.md`. "
           "Recados ao agente do banco e respostas dele: `docs/coleta/pedidos.md`. Achados da revisão: "
           "`docs/revisao/achados.csv` (`quem_corrige` = `coleta-brasil`).", "",
           "| Competição | Temporadas | Jogos | Gols c/ autor | Cartões | Clubes | Tabelas ok / div. | No banco | Pendências | Ficha |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for r in resumos:
        idx.append(f"| {r['nome']} | {r['edicoes']} ({r['de']}–{r['ate']}) | {r['jogos']} | {r['gols_autor']} | {r['cartoes']} | "
                   f"{r['clubes']} | {r['tabelas_ok']} / {r['tabelas_div']} | {r['banco']} | {r['pendencias']} | "
                   f"[{r['slug']}]({r['slug']}.md) |")
    idx += ["", "Fora das fichas: `bra-serie-a-artilheiros` (artilheiros oficiais da Série A, 1937-2025, pedido do agente 1; "
            "`coleta/bra-serie-a-artilheiros/montar.py`, relatório `docs/coleta/bra-serie-a-artilheiros.md`). A Série A e a "
            "Série B são do agente 1 (`serie_b/`).", "",
            "## Pendências de todas as competições", ""]
    for slug in COMPETICOES:
        for p in PENDENCIAS.get(slug, []):
            idx.append(f"- **{slug}:** {p}")
    idx += ["", "## Próximas competições", "",
            "- Ordem dada pelo Guilherme (22/11/2026): Mineiro (`bra-mg-1`), Gaúcho (`bra-rs-1`), Paulista A3 (`bra-sp-3`). "
            "Cada uma com o ok dele.", ""]
    (SAIDA / "README.md").write_text("\n".join(idx), encoding="utf-8")


if __name__ == "__main__":
    main()
