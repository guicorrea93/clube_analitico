"""Gera a documentação completa da coleta África em coleta/comum-africa/documentacao/.

Uma ficha por competição (<slug>.md) e o índice (README.md). Tudo sai do que existe de fato:
- do pacote (data/coleta/<slug>/pacote/): o que cada campo cobre, década a década; formato do campeonato ao longo do
  tempo; campeões, vices, rebaixados e ajustes de pontos; artilheiros; conferência com as tabelas publicadas;
- do código (coleta/<slug>/): como as edições foram definidas (docstring de edicoes.py), identidade dos clubes (docstring
  de clubes_<pais>.py) e todas as correções e decisões com o motivo (explicacoes.py: EXTRAS, CONSERTA_TEXTO, CORRIGE,
  TABELAS_FORA, EXPLICACOES);
- do relatório da importação (docs/coleta/<slug>.md): fontes, regras e o que ficou de fora;
- dos achados da revisão (docs/revisao/achados.csv, quem_corrige = coleta-africa) ainda abertos;
- de PENDENCIAS, abaixo: o que falta, mantido à mão.

Rode depois de cada importação ou correção: python coleta/comum-africa/documentar.py
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
LIGAS: list[str] = ["egy-1", "mar-1", "tun-1", "alg-1", "rsa-1", "nga-1", "gha-1"]
PAIS: dict[str, str] = {"egy-1": "egy", "mar-1": "mar", "tun-1": "tun", "alg-1": "alg", "rsa-1": "rsa", "nga-1": "nga", "gha-1": "gha"}

# o que falta em cada competição (manter à mão; os achados abertos da revisão entram sozinhos; a ordem geral está em
# COMECE-AQUI.md)
PENDENCIAS: dict[str, list[str]] = {
    "egy-1": [
        "1948/49 a 1963/64 sem jogos (nenhuma fonte pública tem): só a tabela final, e a final ou o desempate do título quando "
        "a página da RSSSF traz (1948/49, 1957/58, 1962/63, 1963/64, 1975/76). As listas \"Results Ahly\" (só os jogos do "
        "Al-Ahly, sem data nem mando) ficaram de fora. Fonte que resolveria: o site do Dr. Tarek Said (drtareksaid.net, "
        "arquivado) ou jornais egípcios da época.",
        "1954/55, 1971/72 e 1973/74 (não terminadas): nenhuma fonte tem jogos nem tabela; entram só com a observação.",
        "Autores dos gols só onde a RSSSF traz (1998/99 a 2006/07, nem sempre a temporada inteira); de 2007/08 em diante a "
        "página não tem autores e a ESPN não cobre a liga. Fonte que resolveria: o ogol jogo a jogo (página de cada partida).",
        "Divergências entre a tabela da RSSSF e os jogos do ogol sem terceira fonte (1979/80, 1980/81) e as que a Wikipédia "
        "confirma a tabela (1977/78 Zamalek, 1991/92 Damanhour 0-0 Zamalek = 1-2?, 2010/11): o jogo provável está no "
        "relatório; nenhum placar foi mudado.",
        "Identidade a conferir: o \"Sohag Railways\" de 2000/01 e o \"Sohag\" de 2001/02 entraram como um clube só; o "
        "Al-Shourta de 1975/76 entrou como Ittihad El-Shorta; o \"Suez Club\" do ogol é o Ittihad Suez só em 1965/66.",
    ],
    "mar-1": [
        "Ainda não carregado no banco (pacote pronto em 24/11/2026; teste de carga OK).",
        "Era colonial (1915/16 a 1954/55): 9 anos sem página da RSSSF (só o campeão); nos outros, jogos incompletos (ligas "
        "regionais com os resultados conhecidos e o mata-mata nacional) ou só a classificação (1949/50 a 1953/54, a maioria "
        "dos clubes só com os pontos). Fonte que resolveria: os jornais da época (Le Petit Marocain, La Vigie Marocaine) na "
        "Gallica (BnF).",
        "1968/69 a 1994/95 (fora 1980/81, 1989/90 e 1990/91): só a tabela final; o ogol só tem os jogos de 2004/05 em diante. "
        "1970/71, 1973/74 e 1981/82 sem página da RSSSF: só o campeão e o vice.",
        "Tabelas de confrontos (1956/57 a 1967/68, 1980/81, 1989/90): os jogos não têm data nem rodada, e vários resultados "
        "não batem com a tabela final da página (vitórias e empates trocados com os mesmos gols); sem terceira fonte.",
        "Autores dos gols quase nenhum (a RSSSF do Marrocos não traz) e nenhum cartão. Fonte que resolveria: o ogol jogo a jogo "
        "(2004/05 em diante).",
        "Identidade a conferir: Racing Casablanca (colonial) = Racing AC = ADM Casablanca (como a RSSSF conta); AS Salé = SA "
        "Salé = Sporting Salé; JS Massira = Forces Auxiliaires (a página de 1994/95 diz que o clube mudou para El Ayoun); "
        "\"ASM\" (1957/58) sem nome completo; \"US Casablanca\" = USA Casablanca.",
        "1946/47: campeão USA Casablanca (página da temporada e Wikipédia); a lista de campeões da RSSSF põe a US Marocaine "
        "(erro da lista; avisar a RSSSF?).",
    ],
    "tun-1": [
        "Ainda não carregado no banco (pacote pronto em 24/11/2026; teste de carga OK).",
        "Era colonial (1907 a 1954/55): só 9 anos têm jogos na RSSSF, e só a final ou o mata-mata (1949/50: os resultados "
        "conhecidos); os outros, só o campeão. 1951/52 (abandonado) tem só a tabela do abandono. Fonte que resolveria: os "
        "jornais da época (La Dépêche tunisienne, Le Petit Matin) na Gallica (BnF).",
        "1955/56 a 1995/96: só a tabela final (lista de tabelas finais da RSSSF), fora os anos da tabela de confrontos "
        "(1968/69, 1970/71, 1977/78, 1980/81, 1982/83 e 1987/88 a 1995/96), que não têm data nem rodada. O ogol só tem jogos "
        "de 2005/06 em diante.",
        "Tabelas de confrontos que não fecham com a tabela final da página: um par de jogos em 1968/69, 1977/78, 1980/81, "
        "1982/83, 1987/88 a 1990/91 e 1993/94; 1994/95 em 13 dos 14 clubes. Sem terceira fonte; nenhum placar mudado (jogo "
        "provável no relatório).",
        "Autores dos gols quase só em 2004/05 e 2010/11 (a RSSSF da Tunísia quase não traz) e nenhum cartão. Fonte que "
        "resolveria: o ogol jogo a jogo (2005/06 em diante).",
        "Identidade a conferir: Railway Sports de Sfax (colonial) = Sfax Railways Sports; US Ferryville = USM Bourguiba; "
        "Olympique Tunis = US Musulmane Olympique; \"ES\" de 1949/50 lido como Espérance de Tunis.",
        "1909/10: a Wikipédia dá um título ao Racing Club de Tunis; a RSSSF diz que não houve campeonato (ficou de fora).",
    ],
    "alg-1": [
        "Ainda não carregado no banco (pacote pronto em 24/11/2026; teste de carga OK).",
        "1964/65 a 1998/99: a lista de jogos da RSSSF não fecha com a tabela da mesma página em vários clubes por ano "
        "(placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a "
        "Wikipédia quase sempre confirma a tabela. Nenhum placar mudado; jogo provável no relatório. Fonte que resolveria: "
        "jornais argelinos da época (El Moudjahid) ou o arquivo da federação.",
        "1974/75 e 1975/76: uma rodada inteira copiada na página (os jogos verdadeiros das rodadas 4 e 18 faltam); 1972/73: "
        "rodada 10 repetida (cópia descartada).",
        "Mando provavelmente trocado: o mesmo mandante x visitante duas vezes na temporada, com placares diferentes (1964/65, "
        "1966/67, 1973/74, 1976/77, 1979/80, 1980/81, 1983/84, 1986/87, 1988/89...): ficou como na página.",
        "1962/63 e 1963/64: ligas regionais incompletas (1962/63 sem a 1ª fase; 1963/64 só os resultados conhecidos, grupo "
        "Leste de Constantine sem números).",
        "2009/10: CA Bordj Bou Arréridj x MC Alger com \"derrota para os dois\" (o formato do pacote não representa; jogo sem "
        "placar).",
        "Identidade a conferir: DNC Alger = OC Alger = CS DNC Alger = JH Djazaïr (nome de exibição \"DNC Alger\"); WKF Collo "
        "= Entente Collo; o USM Annaba até 1979 é o Hamra Annaba; \"US Constantine\" de 1996/97 = US Chaouia; MB Rouissat = "
        "Olympique Rouissat (2025/26).",
    ],
    "rsa-1": [
        "Ainda não carregado no banco (pacote pronto em 24/11/2026; teste de carga OK).",
        "1971 a 1995: só a tabela final (a RSSSF não tem os jogos), fora 1987, 1992 e 1993 (parte dos jogos); 1972, 1973, "
        "1975 e 1977: só o campeão (a página do ano é da NFL). 1996/97: parte dos jogos. O ogol só tem jogos de 2005/06 em "
        "diante. Fonte que resolveria: jornais sul-africanos (The World, Sowetan, Rand Daily Mail) ou o arquivo da PSL.",
        "Rebaixamento pelos desempates de acesso (2004/05 a 2025/26) marcado à mão (o 15º que não está na 1ª divisão do ano "
        "seguinte); clubes que saíram por venda da vaga, fusão ou redução da liga ficam sem marca.",
        "Autores dos gols só onde a RSSSF traz; artilheiros de poucas temporadas (contagem dos gols com autor). Fonte que "
        "resolveria: o ogol jogo a jogo (2005/06 em diante).",
        "Identidade a conferir: Cape Town Spurs = Ajax Cape Town (fusão de 1999 e volta ao nome em 2020); SuperSport United "
        "= Pretoria City = Albany City; Free State Stars = Qwa Qwa Stars = Score Stars; Highlands Park (1959) = Welkom "
        "Eagles (1993); Durban Bush Bucks (até 1987) x Bush Bucks de Umtata (desde 1988); Mpumalanga Black Aces = Witbank "
        "Aces = Total Aces.",
    ],
    "nga-1": [
        "Ainda não carregado no banco (pacote pronto em 24/11/2026; teste de carga OK).",
        "1972 a 1997: só a tabela final (1972, 1989, 1991 a 1997) ou só o campeão (1973 a 1988 e 1990); faltam as páginas de "
        "1980 a 1982. 1998 a 2003, 2007/08 e 2019/20: só parte dos jogos. Fonte que resolveria: jornais nigerianos (Daily "
        "Times, The Guardian, Complete Sports) ou o arquivo da NPFL.",
        "2009/10 a 2011/12: os jogos do ogol não fecham com a tabela da RSSSF em vários clubes (placar de campo de jogos "
        "decididos de outro jeito?); nenhum placar mudado.",
        "Rebaixamento marcado só onde a página diz (tabela ou nota); nos anos 1970 e 1980, sem informação.",
        "Autores dos gols quase nenhum; artilheiros, nenhum. Fonte que resolveria: o ogol jogo a jogo (2008/09 em diante).",
        "Identidade a conferir: Heartland = Iwuanyanwu Nationale; Dolphin = Eagle Cement; Ifeanyi Ubah = Gabros "
        "International; ABS = Bukola Babes; NITEL Vasco = P&T Vasco da Gama; o \"Akwa Star...\" do ogol de 2011/12 = Akwa "
        "United.",
    ],
    "gha-1": [
        "Ainda não carregado no banco (pacote pronto em 24/11/2026; teste de carga OK).",
        "1958 a 1996/97: só a tabela final (lista de tabelas finais até 1987; página do ano de 1989/90 a 1996/97); 1988/89 "
        "só o campeão (\"Final table missing\"); 1989/90 só posição, jogos e pontos. 1997/98 e 2006/07: parte dos jogos; "
        "2011/12: só a tabela. O ogol só tem jogos de 2008/09 a 2010/11 e de 2015 em diante. Fonte que resolveria: jornais "
        "ganeses (Daily Graphic) ou o arquivo da GFA.",
        "2010/11: os jogos do ogol não fecham com a tabela da RSSSF em sete clubes; nenhum placar mudado.",
        "Rebaixamento marcado onde a tabela ou a nota diz; em vários anos dos 1960 e 1970 a lista não diz.",
        "Autores dos gols quase nenhum; artilheiros e cartões, nenhum.",
        "Identidade a conferir: Ashanti Gold = Goldfields; Ebusua Dwarfs = Mysterious Dwarfs; Swedru All Blacks = Gamba All "
        "Blacks; Wa All Stars = All Stars (2007-2011); Holy Stars de Techiman (1986) x Basake Holy Stars (2024/25).",
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
        return [x for x in csv.DictReader(f) if x["competicao"] == slug and x["quem_corrige"] == "coleta-africa"
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
           f"Gerado por `python coleta/comum-africa/documentar.py` a partir do pacote `data/coleta/{slug}/pacote/`, do "
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
    out += ["", "Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na África: nenhuma fonte em "
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
            "cache da ESPN em `data/cache/espn-africa/`" + (f", do ogol em `data/cache/ogol-{slug}/`" if (RAIZ / "data" / "cache" / f"ogol-{slug}").exists() else "") + ".",
            f"- Pacote: `data/coleta/{slug}/pacote/`; relatório: `docs/coleta/{slug}.md`.",
            "- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):", "", "```"]
    out += [f"python coleta/{slug}/{a}" for a in baixar]
    out += [f"python coleta/{slug}/importar.py", f"python coleta/{slug}/conferir.py [-v temporada]   # divergências",
            f"python coleta/comum-africa/testar_carga.py {slug} <scratchpad>", "python coleta/comum-africa/documentar.py",
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
    idx = ["# Coleta África — documentação", "",
           "Gerado por `python coleta/comum-africa/documentar.py`. Uma ficha por competição, com tudo o que o pacote "
           "tem, como as edições foram definidas, fontes e regras, a conferência, a cobertura de cada campo década a década, "
           "o formato ao longo do tempo, campeões e vices, ajustes de pontos, todas as correções e decisões com o motivo, o "
           "que não deu para coletar e as pendências.", "",
           "Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum-africa/COMECE-AQUI.md`. "
           "Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-africa.md`. Achados da revisão: "
           "`docs/revisao/achados.csv` (`quem_corrige` = `coleta-africa`).", "",
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
            "- 2ªs divisões, na ordem do guia geral, só quando o Guilherme pedir. Como fazer: "
            "`COMECE-AQUI.md`, seção 4.", ""]
    (SAIDA / "README.md").write_text("\n".join(idx), encoding="utf-8")


if __name__ == "__main__":
    main()
