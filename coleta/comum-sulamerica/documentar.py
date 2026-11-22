"""Gera a documentação completa da coleta América do Sul em coleta/comum-sulamerica/documentacao/.

Uma ficha por competição (<slug>.md) e o índice (README.md). Tudo sai do que existe de fato:
- do pacote (data/coleta/<slug>/pacote/): o que cada campo cobre, década a década; formato do campeonato ao longo do
  tempo; campeões, vices, rebaixados e ajustes de pontos; artilheiros; conferência com as tabelas publicadas;
- do código (coleta/<slug>/): como as edições foram definidas (docstring de edicoes.py), identidade dos clubes (docstring
  de clubes_<pais>.py) e todas as correções e decisões com o motivo (explicacoes.py: EXTRAS, CONSERTA_TEXTO, CORRIGE,
  TABELAS_FORA, EXPLICACOES);
- do relatório da importação (docs/coleta/<slug>.md): fontes, regras e o que ficou de fora;
- dos achados da revisão (docs/revisao/achados.csv, quem_corrige = coleta-sulamerica) ainda abertos;
- de PENDENCIAS, abaixo: o que falta, mantido à mão.

Rode depois de cada importação ou correção: python coleta/comum-sulamerica/documentar.py
"""
from __future__ import annotations

import ast
import csv
import importlib.util
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
SAIDA = AQUI / "documentacao"
LIGAS = ["arg-1", "uru-1", "chi-1", "col-1", "par-1", "per-1", "ecu-1"]
PAIS = {"arg-1": "arg", "uru-1": "uru", "chi-1": "chi", "col-1": "col", "par-1": "par", "per-1": "per", "ecu-1": "ecu"}

# o que falta em cada competição (manter à mão; os achados abertos da revisão entram sozinhos; a ordem geral está em
# COMECE-AQUI.md)
PENDENCIAS: dict[str, list[str]] = {
    "arg-1": [
        "Achados da revisão em aberto (36, prefixo AR; lista na seção 9): vices errados em 12 edições, campeão de 1913 "
        "Federación, datas com ano errado (~3.920 jogos), fases, artilheiros e clubes. Corrigir e citar os ids em "
        "docs/coleta/pedidos-sulamerica.md.",
        "Decisões do Guilherme pedidas pela revisão: título de 1891 (só Saint Andrew's ou dividido), Apertura 2026, Quilmes "
        "de 1893-1895, fusões de 1934, Copa de Oro de 1936.",
    ],
    "uru-1": [
        "Achados da revisão em aberto (19, prefixo UY; lista na seção 9): a classificação final de 1994-2025 é a tabela do "
        "Apertura (UY-006, que puxa vice e 3º errados), Supercopa dentro da Final, datas das decisões, artilheiros. Corrigir "
        "e citar os ids em docs/coleta/pedidos-sulamerica.md.",
        "Decisões do Guilherme pedidas pela revisão: títulos da FUF (1923, 1924) e do Consejo Provisorio (1926); Atlético "
        "Wanderers da FUF = Montevideo Wanderers?; vice de 1954.",
    ],
    "chi-1": [],
    "col-1": [
        "1987 e 1991-1995 sem jogos: nenhuma fonte pública tem (só tabela final e campeão).",
    ],
    "par-1": [
        "76 edições sem jogos (1906-1959, 1968-1980, 1982-1995 sem fonte pública): campeão, vice e tabela parcial quando há.",
        "Pacote reimportado em 21/11 (leitor comum: clubes com nome de data): +55 jogos de 2005-2014 e ids das partidas "
        "mudados; o agente 1 precisa recarregar o pacote inteiro (recado de 21/11, seção do ecu-1).",
    ],
    "per-1": [
        "Decisão para o agente 1/Guilherme: 1912-1921 (Liga Peruana) entraram como 10 edições só com campeão e vice (conta "
        "da Wikipédia); se valer a conta da RSSSF, tirar essas edições.",
        "18 edições sem jogos (1912-1921, 1970-1974, 1976, 1977, 1979) e jogos incompletos em 1926, 1982, 1984, 1986, "
        "1988-1991 e 2003: nenhuma fonte pública tem o resto.",
        "Ainda não carregado no banco.",
    ],
    "ecu-1": [
        "Ainda não carregado no banco (commit pendente do ok do Guilherme).",
        "ESPN sem lances de 2014 a 2020: gols com minuto e cartões desses anos só jogo a jogo (outra fonte).",
    ],
}

# rótulo de cada dicionário de explicacoes.py
DICIONARIOS = {
    "CONSERTA_TEXTO": "Erros de digitação da página da RSSSF corrigidos antes da leitura",
    "CORRIGE": "Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados)",
    "EXTRAS": "Jogos acrescentados à mão (a página traz em texto corrido)",
    "TABELAS_FORA": "Tabelas da página que não são da edição",
    "EXPLICACOES": "Divergências entre fontes já explicadas",
}

CAMPOS_COBERTURA = [("data", "data"), ("hora", "hora"), ("rodada", "rodada"), ("estadio", "estádio"), ("cidade", "cidade"),
                    ("publico", "público")]


def ler(slug: str, nome: str) -> list[dict]:
    arq = RAIZ / "data" / "coleta" / slug / "pacote" / f"{nome}.csv"
    if not arq.exists():
        return []
    with arq.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def modulo(slug: str, nome: str):
    """Carrega coleta/<slug>/<nome>.py com nome único (os módulos das ligas têm o mesmo nome)."""
    caminho = RAIZ / "coleta" / slug / f"{nome}.py"
    if not caminho.exists():
        return None
    sys.path.insert(0, str(AQUI))
    spec = importlib.util.spec_from_file_location(f"{slug.replace('-', '_')}_{nome}", caminho)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def docstring(slug: str, nome: str) -> str:
    caminho = RAIZ / "coleta" / slug / f"{nome}.py"
    return (ast.get_docstring(ast.parse(caminho.read_text(encoding="utf-8"))) or "") if caminho.exists() else ""


def pct(a: int, b: int) -> str:
    return "—" if not b else f"{100 * a / b:.0f}%"


def num(x: str) -> int:
    return int(x) if x not in ("", None) else 0


def texto_chave(k) -> str:
    return " · ".join(str(x) for x in k) if isinstance(k, tuple) else str(k)


def texto_correcao(v) -> str:
    """Valor de CONSERTA_TEXTO ((antes, depois, motivo)) ou de CORRIGE ({esp, gm_of, descartar, motivo})."""
    if isinstance(v, tuple) and len(v) == 3:
        return f"«{v[0].strip()}» → «{v[1].strip()}»: {v[2]}"
    if isinstance(v, dict):
        o_que = []
        if v.get("descartar"):
            o_que.append("descartado")
        if "esp" in v:
            o_que.append({"": "vale o placar de campo", "awd": "decidido fora de campo", "n/p": "não jogado",
                          "anulado": "anulado", "abd": "abandonado"}.get(v["esp"], v["esp"]))
        if "gm_of" in v:
            o_que.append(f"placar oficial {v['gm_of']}-{v['gv_of']}")
        outros = {k: x for k, x in v.items() if k not in ("descartar", "esp", "gm_of", "gv_of", "motivo")}
        o_que += [f"{k} = {x}" for k, x in outros.items()]
        return (f"[{', '.join(o_que)}] " if o_que else "") + str(v.get("motivo", ""))
    return str(v)


def decada(ano: str) -> str:
    return f"{ano[:3]}0s"


def paragrafos(rel: str) -> dict[str, str]:
    """Parágrafos "**Rótulo:** texto" do cabeçalho do relatório (antes da tabela de edições)."""
    cab = rel.split("\n| Temporada")[0]
    saida = {}
    for p in re.split(r"\n\s*\n", cab):
        if m := re.match(r"\*\*(.+?):?\*\*:?\s*(.*)", p.strip(), re.S):
            saida[m.group(1).rstrip(":")] = re.sub(r"\s*\n\s*", " ", m.group(2)).strip()
    return saida


def faixas(ed: list[dict], chave_fn) -> list[list]:
    res, atual = [], None
    for e in ed:
        v = chave_fn(e)
        if atual and atual[0] == v:
            atual[2] = e["temporada"]
        else:
            atual = [v, e["temporada"], e["temporada"]]
            res.append(atual)
    return res


def achados_abertos(slug: str) -> list[dict]:
    arq = RAIZ / "docs" / "revisao" / "achados.csv"
    if not arq.exists():
        return []
    with arq.open(encoding="utf-8") as f:
        return [x for x in csv.DictReader(f) if x["competicao"] == slug and x["quem_corrige"] == "coleta-sulamerica"
                and x["situacao"] == "aberto"]


def ficha(slug: str, no_banco: set[str], commits: dict[str, str]) -> tuple[str, dict]:
    comp = json.loads((RAIZ / "data" / "coleta" / slug / "pacote" / "competicao.json").read_text(encoding="utf-8"))
    ed, part, gols, cart = ler(slug, "edicoes"), ler(slug, "partidas"), ler(slug, "gols"), ler(slug, "cartoes")
    clf, fases, art, conf = ler(slug, "classificacao_final"), ler(slug, "fases"), ler(slug, "artilheiros"), ler(slug, "conferencia")
    clubes, pub = ler(slug, "clubes"), ler(slug, "tabelas_publicadas")
    ano_de = {e["temporada"]: e["ano_inicio"] for e in ed}
    temporada_de = {p["id"]: p["temporada"] for p in part}
    com_placar = [p for p in part if p["gols_mandante"] != ""]
    total_gols = sum(num(p["gols_mandante"]) + num(p["gols_visitante"]) for p in com_placar)
    sem_jogos = [c["temporada"] for c in conf if num(c["jogos"]) == 0]
    rel = (RAIZ / "docs" / "coleta" / f"{slug}.md").read_text(encoding="utf-8")
    par = paragrafos(rel)

    out = [f"# {comp['nome']} (`{slug}`) — documentação", "",
           f"Gerado por `python coleta/comum-sulamerica/documentar.py` a partir do pacote `data/coleta/{slug}/pacote/`, do "
           f"código `coleta/{slug}/` e do relatório `docs/coleta/{slug}.md` (que tem o detalhe edição a edição).", ""]

    # ---- 1. visão geral
    out += ["## 1. O que temos", "",
            f"- **Edições:** {len(ed)}, de {ed[0]['temporada']} a {ed[-1]['temporada']}; {len(sem_jogos)} sem jogos.",
            f"- **Jogos:** {len(part)} ({len(com_placar)} com placar); **gols:** {total_gols}; **gols com autor:** {len(gols)} "
            f"({pct(len(gols), total_gols)}); **cartões:** {len(cart)}.",
            f"- **Clubes:** {len(clubes)}; **artilheiros:** {len({a['temporada'] for a in art})} edições com artilheiro "
            f"({len(art)} linhas, com empates).",
            f"- **Classificação final:** {len({c['temporada'] for c in clf})} edições; **tabelas publicadas guardadas para "
            f"conferência:** {len(pub)} linhas.",
            f"- **No banco:** {'sim' if slug in no_banco else 'ainda não'}; **último commit do pacote:** "
            f"{commits.get(slug) or 'nenhum (pacote ainda não commitado)'}.",
            f"- **Observação da competição:** {comp.get('observacao') or '—'}", ""]

    # ---- 2. definição das edições, fontes e regras
    out += ["## 2. Edições, fontes e regras", "", "**Como as edições foram definidas** (docstring de `edicoes.py`):", "",
            "```", docstring(slug, "edicoes"), "```", ""]
    for rot in par:
        if rot in ("Fontes", "Regras", "Clubes", "Edições") or rot.startswith(("Até", "Tabela anual", "1912")):
            out += [f"**{rot}:** {par[rot]}", ""]

    # ---- 3. conferência
    ok = [c["temporada"] for c in conf if num(c["tabelas_conferidas"]) > 0 and num(c["tabelas_divergentes"]) == 0]
    div = [c["temporada"] for c in conf if num(c["tabelas_divergentes"]) > 0]
    sem_conf = [c["temporada"] for c in conf if c["temporada"] not in ok and c["temporada"] not in div]
    incompletas = [f"{c['temporada']} ({c['jogos']} de {c['jogos_esperados']})" for c in conf
                   if num(c["jogos"]) and c["jogos_esperados"] and c["jogos"] != c["jogos_esperados"]]
    out += ["## 3. Conferência", "",
            "Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a "
            "lista de campeões da Wikipédia.", "",
            f"- **Edições em que todas as tabelas fecham com os jogos:** {len(ok)}.",
            f"- **Edições com alguma tabela divergente** ({len(div)}; motivo no relatório, na edição): {', '.join(div) or 'nenhuma'}.",
            f"- **Edições sem tabela para conferir** ({len(sem_conf)}): {', '.join(sem_conf) or 'nenhuma'}.",
            f"- **Edições com menos jogos que o esperado:** {', '.join(incompletas) or 'nenhuma'}.", ""]

    # ---- 4. cobertura por década
    por_dec = defaultdict(list)
    for p in part:
        por_dec[decada(ano_de[p["temporada"]])].append(p)
    gols_dec, golsaut_dec, cart_dec = Counter(), Counter(), Counter()
    for p in com_placar:
        gols_dec[decada(ano_de[p["temporada"]])] += num(p["gols_mandante"]) + num(p["gols_visitante"])
    for g in gols:
        golsaut_dec[decada(ano_de[temporada_de[g["partida_id"]]])] += 1
    for c in cart:
        cart_dec[decada(ano_de[temporada_de[c["partida_id"]]])] += 1
    ed_dec = Counter(decada(e["ano_inicio"]) for e in ed)
    out += ["## 4. Cobertura de cada campo, por década", "",
            "Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início "
            "da edição.", "",
            "| Década | Edições | Jogos | " + " | ".join(r for _, r in CAMPOS_COBERTURA) + " | gols c/ autor | cartões/jogo |",
            "|" + "---|" * (len(CAMPOS_COBERTURA) + 5)]
    for d in sorted(ed_dec):
        ps = por_dec.get(d, [])
        cel = [pct(sum(1 for p in ps if p[c]), len(ps)) for c, _ in CAMPOS_COBERTURA]
        out.append(f"| {d} | {ed_dec[d]} | {len(ps)} | " + " | ".join(cel) + f" | {pct(golsaut_dec[d], gols_dec[d])} | "
                   + (f"{cart_dec[d] / len(ps):.1f}" if ps else "—") + " |")
    out += ["", "Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na América do Sul: nenhuma fonte em "
            "lote tem.", ""]

    # ---- 5. formato
    out += ["## 5. Formato do campeonato ao longo do tempo", "", "**Número de clubes:**", ""]
    out += [f"- {a if a == b else a + ' a ' + b}: {v} clubes" for v, a, b in faixas(ed, lambda e: e["num_clubes"])]
    out += ["", "**Pontos por vitória:**", ""]
    out += [f"- {a if a == b else a + ' a ' + b}: {v}" for v, a, b in faixas(ed, lambda e: e["pontos_vitoria"])]
    out += ["", "**Nome oficial:**", ""]
    out += [f"- {a if a == b else a + ' a ' + b}: {v}" for v, a, b in faixas(ed, lambda e: re.sub(r"\d{4}(/\d{2,4})?", "<ano>", e["nome_oficial"]))]
    out += ["", "**Formato** (fases na ordem, do edicoes.csv):", ""]
    out += [f"- {a if a == b else a + ' a ' + b}: {v}" for v, a, b in faixas(ed, lambda e: e["formato"])]
    por_t = defaultdict(list)
    for f in fases:
        por_t[f["temporada"]].append(f)
    out += ["", "**Fases e grupos de cada edição com mais de uma fase:**", ""]
    out += [f"- {t}: " + "; ".join(f"{f['fase']} ({f['tipo']}" + (f", {f['num_grupos']} grupos" if f["num_grupos"] else "")
                                   + (f", {f['formato_serie']}" if f["tipo"] == "mata_mata" else "") + ")" for f in fs)
            for t, fs in por_t.items() if len(fs) > 1] or ["- nenhuma"]
    out += ["", "**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos "
            "os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` "
            "do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.", ""]
    fonte_clf = Counter(re.sub(r"\(.*", "", c["fonte"]).strip() for c in clf if c["posicao"] == "1")
    out += [f"- {f}: {n} edições" for f, n in fonte_clf.most_common()]
    obs = [(e["temporada"], e["observacao"]) for e in ed if e["observacao"]]
    out += ["", "**Observações das edições:**", ""]
    out += [f"- {t}: {o}" for t, o in obs] or ["- nenhuma"]
    out.append("")

    # ---- 6. campeões, rebaixados e ajustes
    camp = Counter(e["campeao"] for e in ed if e["campeao"])
    sem_campeao = [e["temporada"] for e in ed if not e["campeao"]]
    reb = [(c["temporada"], c["clube"]) for c in clf if c["situacao"] == "rebaixado"]
    ajuste = [(c["temporada"], c["clube"], c["ajuste_pontos"]) for c in clf if c["ajuste_pontos"] not in ("", "0")]
    out += ["## 6. Campeões, rebaixados e ajustes de pontos", "", "**Títulos:**", ""]
    out += [f"- {c}: {n}" for c, n in camp.most_common()]
    if sem_campeao:
        out += [f"- Sem campeão: {', '.join(sem_campeao)}"]
    out += ["", "**Campeão e vice de cada edição:**", "", "| Edição | Campeão | Vice |", "|---|---|---|"]
    out += [f"| {e['temporada']} | {e['campeao'] or '—'} | {e['vice'] or '—'} |" for e in ed]
    rb = Counter(c for _, c in reb)
    out += ["", f"**Rebaixados marcados na classificação:** {len(reb)} em {len({t for t, _ in reb})} edições (só onde a "
            "tabela publicada marca a queda)" + (("; quem mais caiu: " + ", ".join(f"{c} ({n})" for c, n in rb.most_common(5)))
                                                if rb else "") + ".", "",
            "**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de "
            "pênaltis):", ""]
    out += [f"- {t}: {c} {'+' if not a.startswith('-') else ''}{a}" for t, c, a in ajuste] or ["- nenhum"]
    out.append("")

    # ---- 7. correções e decisões
    exp = modulo(slug, "explicacoes")
    out += ["## 7. Correções e decisões (com o motivo)", "",
            f"Registradas em `coleta/{slug}/explicacoes.py`; cada uma também aparece no relatório, na edição.", ""]
    for nome, rotulo in DICIONARIOS.items():
        v = getattr(exp, nome, None)
        if not v:
            continue
        out += [f"### {rotulo} (`{nome}`, {sum(len(x) if isinstance(x, list) else 1 for x in v.values())})", ""]
        for k, x in v.items():
            if isinstance(x, list):
                for i in x:
                    out.append(f"- **{texto_chave(k)}:** " + (f"{i['mandante']} {i['gm']}-{i['gv']} {i['visitante']} "
                                                              f"({i.get('fase', '')}, {i.get('fonte_id', '')}) {i.get('obs', '')}"
                                                              if isinstance(i, dict) else str(i)))
            else:
                out.append(f"- **{texto_chave(k)}:** {texto_correcao(x)}")
        out.append("")
    clu = docstring(slug, f"clubes_{PAIS[slug]}")
    out += ["### Identidade dos clubes", "", f"Regras em `coleta/{slug}/clubes_{PAIS[slug]}.py` (docstring abaixo; os nomes de "
            "cada fonte estão na coluna `nomes_fonte` do clubes.csv).", "", "```", clu, "```", ""]

    # ---- 8. o que não deu para coletar
    out += ["## 8. O que não deu para coletar", ""]
    for rot in par:
        if rot.startswith(("Edições sem jogos", "Edições com jogos incompletos", "Fora do pacote")):
            out += [f"- **{rot}:** {par[rot]}"]
    sem_aut = [d for d in sorted(ed_dec) if gols_dec[d] and golsaut_dec[d] < 0.5 * gols_dec[d]]
    sem_cart = [d for d in sorted(ed_dec) if por_dec.get(d) and cart_dec[d] == 0]
    out += [f"- **Edições sem jogos** ({len(sem_jogos)}): {', '.join(sem_jogos) or 'nenhuma'}.",
            f"- **Décadas com menos da metade dos gols com autor:** {', '.join(sem_aut) or 'nenhuma'}.",
            f"- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): {', '.join(sem_cart) or 'nenhuma'}.",
            "- Árbitro e estatísticas de jogo: nenhuma fonte em lote.", ""]

    # ---- 9. pendências
    ach = achados_abertos(slug)
    out += ["## 9. Pendências e próximos passos", ""]
    out += [f"- {p}" for p in PENDENCIAS.get(slug, [])] or ["- nenhuma"]
    if ach:
        out += ["", f"**Achados da revisão em aberto** (`docs/revisao/achados.csv`, provas em `docs/revisao/{slug}.md`):", ""]
        out += [f"- {x['id']} ({x['gravidade']}) {x['item']} — {x['edicao']}: {x['o_que_a_fonte_diz'][:220]}" for x in ach]
    out.append("")

    # ---- 10. arquivos e comandos
    arquivos = sorted(p.name for p in (RAIZ / "coleta" / slug).glob("*.py"))
    baixar = [a for a in arquivos if a.startswith("baixar")]
    out += ["## 10. Arquivos e comandos", "", f"Código em `coleta/{slug}/`:", "", "| Arquivo | O que faz |", "|---|---|"]
    for a in arquivos:
        d = docstring(slug, a[:-3]).split("\n")[0]
        out.append(f"| `{a}` | {d} |")
    out += ["", f"- Fontes baixadas: `data/coleta/{slug}/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); "
            "cache da ESPN em `data/cache/espn-sulamerica/`" + (f", do ogol em `data/cache/ogol-{slug}/`" if (RAIZ / "data" / "cache" / f"ogol-{slug}").exists() else "") + ".",
            f"- Pacote: `data/coleta/{slug}/pacote/`; relatório: `docs/coleta/{slug}.md`.",
            "- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):", "", "```"]
    out += [f"python coleta/{slug}/{a}" for a in baixar]
    out += [f"python coleta/{slug}/importar.py", f"python coleta/{slug}/conferir.py [-v temporada]   # divergências",
            f"python coleta/comum-sulamerica/testar_carga.py {slug} <scratchpad>", "python coleta/comum-sulamerica/documentar.py",
            "```", ""]
    resumo = {"slug": slug, "nome": comp["nome"], "edicoes": len(ed), "de": ed[0]["temporada"], "ate": ed[-1]["temporada"],
              "sem_jogos": len(sem_jogos), "jogos": len(part), "gols_autor": len(gols), "cartoes": len(cart),
              "clubes": len(clubes), "ok": len(ok), "div": len(div), "pendencias": len(PENDENCIAS.get(slug, [])),
              "achados": len(ach), "banco": slug in no_banco, "commit": commits.get(slug, "")}
    return "\n".join(out) + "\n", resumo


def main() -> None:
    import sqlite3
    import subprocess
    sys.stdout.reconfigure(encoding="utf-8")
    SAIDA.mkdir(exist_ok=True)
    con = sqlite3.connect(f"file:{RAIZ / 'db' / 'futebol.db'}?mode=ro", uri=True)
    no_banco = {r[0] for r in con.execute("select slug from competicao")}
    commits = {}
    for slug in LIGAS:
        r = subprocess.run(["git", "log", "-1", "--format=%h", "--", f"data/coleta/{slug}/pacote"], cwd=RAIZ,
                           capture_output=True, text=True)
        commits[slug] = r.stdout.strip()
    resumos = []
    for slug in LIGAS:
        txt, r = ficha(slug, no_banco, commits)
        (SAIDA / f"{slug}.md").write_text(txt, encoding="utf-8")
        resumos.append(r)
        print(f"{slug}: {r['edicoes']} edições, {r['jogos']} jogos", flush=True)
    idx = ["# Coleta América do Sul — documentação", "",
           "Gerado por `python coleta/comum-sulamerica/documentar.py`. Uma ficha por competição, com tudo o que o pacote "
           "tem, como as edições foram definidas, fontes e regras, a conferência, a cobertura de cada campo década a década, "
           "o formato ao longo do tempo, campeões e vices, ajustes de pontos, todas as correções e decisões com o motivo, o "
           "que não deu para coletar e as pendências.", "",
           "Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum-sulamerica/COMECE-AQUI.md`. "
           "Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-sulamerica.md`. Achados da revisão: "
           "`docs/revisao/achados.csv` (`quem_corrige` = `coleta-sulamerica`).", "",
           "| Competição | Edições | Sem jogos | Jogos | Gols c/ autor | Cartões | Clubes | Edições ok / div. | No banco | "
           "Commit | Achados abertos | Ficha |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in resumos:
        idx.append(f"| {r['nome']} | {r['edicoes']} ({r['de']}–{r['ate']}) | {r['sem_jogos']} | {r['jogos']} | {r['gols_autor']} | "
                   f"{r['cartoes']} | {r['clubes']} | {r['ok']} / {r['div']} | {'sim' if r['banco'] else 'não'} | "
                   f"{r['commit'] or '—'} | {r['achados']} | [{r['slug']}]({r['slug']}.md) |")
    idx += ["", "## Pendências de todas as competições", ""]
    for slug in LIGAS:
        for p in PENDENCIAS.get(slug, []):
            idx.append(f"- **{slug}:** {p}")
    idx += ["", "## Próximas competições", "",
            "- `bol-1` (Bolívia), depois `ven-1` (Venezuela), uma por vez e só com o ok do Guilherme. Como fazer: "
            "`COMECE-AQUI.md`, seção 4.", ""]
    (SAIDA / "README.md").write_text("\n".join(idx), encoding="utf-8")


if __name__ == "__main__":
    main()
