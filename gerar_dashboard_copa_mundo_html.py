"""Gera dashboard autocontido de Copas do Mundo usando somente Wikipedia PT."""
from __future__ import annotations

import base64
import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen, urlretrieve

import pandas as pd
from lxml import html as lxml_html

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data" / "worldcup_wikipedia"
OUT = ROOT / "dashboard_copa_mundo.html"
BASE = "https://pt.wikipedia.org/wiki/"
MAIN_TITLE = "Copa_do_Mundo_FIFA"
PLOTLY_URL = "https://cdn.plot.ly/plotly-2.35.2.min.js"
PLOTLY_FILE = DATA_DIR / "plotly-2.35.2.min.js"
FLAGS_DIR = DATA_DIR / "flags"
POSTERS_DIR = DATA_DIR / "posters"
TROFEUS_DIR = DATA_DIR / "trofeus"
GOLS_DETALHADOS_FILE = DATA_DIR / "gols_detalhados_statsbomb.json"
GOLS_ANALITICOS_FILE = DATA_DIR / "gols_analiticos.json"

YEARS = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022, 2026]
PAGE_TITLES = {
    year: f"Copa_do_Mundo_FIFA_de_{year}" for year in YEARS
}


def clean_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, float) and pd.isna(value):
        return ""
    text = str(value)
    text = re.sub(r"\[[^\]]+\]", "", text)
    text = text.replace("\xa0", " ").replace("−", "-").replace("–", "-").replace("—", "-")
    text = text.replace("−", "-").replace("–", "-").replace("—", "-")
    text = re.sub(r"\s+", " ", text).strip()
    return "" if text.lower() in {"nan", "none"} else text


def clean_team(value) -> str:
    text = clean_text(value)
    text = re.sub(r"\s*\([^)]*\)", "", text)
    aliases = {
        "Alemanha Ocidental": "Alemanha",
        "Alemanha[nota 4]": "Alemanha",
        "Tchecoslováquia": "Tchecoslováquia",
        "Checoslováquia": "Tchecoslováquia",
        "Reino de Itália": "Itália",
        "Países Baixos": "Países Baixos",
        "Holanda": "Países Baixos",
        "Coreia do Sul": "Coreia do Sul",
        "Coréia do Sul": "Coreia do Sul",
        "Estados Unidos da América": "Estados Unidos",
        "Sérvia e Montenegro": "Sérvia e Montenegro",
        "União Soviética": "União Soviética",
        "Rússia": "Rússia",
        "Zaire": "República Democrática do Congo",
        "RD Congo": "República Democrática do Congo",
        "Polónia": "Polônia",
        "Trindade e Tobago": "Trinidad e Tobago",
    }
    return aliases.get(text, text)


def is_valid_team_name(team: str) -> bool:
    team = clean_team(team)
    if not team:
        return False
    invalid_terms = ["Decisão", "Disputa", "Final", "Semifinal", "Quartas", "Oitavas", "Grupo ", "Fase", "3º lugar", "4º lugar"]
    return not any(term.lower() in team.lower() for term in invalid_terms)


def to_int(value) -> int:
    text = clean_text(value)
    if not text or text in {"-", "–", "—"}:
        return 0
    digits = re.sub(r"[^\d-]", "", text)
    if not digits or digits == "-":
        return 0
    try:
        return int(digits)
    except ValueError:
        return 0


def extract_years(text: str) -> list[int]:
    return [int(y) for y in re.findall(r"(19\d{2}|20\d{2})", clean_text(text))]


def score_goals(score: str) -> tuple[int, int] | None:
    text = clean_text(score)
    match = re.search(r"(\d+)\s*[-x]\s*(\d+)", text)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def fetch_page(title: str) -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    path = DATA_DIR / f"{title}.html"
    if path.exists() and path.stat().st_size > 10_000:
        return path
    url = BASE + quote(title)
    print(f"Baixando Wikipedia: {title}")
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=60) as response:
        path.write_bytes(response.read())
    return path


def fetch_optional_page(title: str) -> Path | None:
    try:
        return fetch_page(title)
    except Exception as exc:
        print(f"Pagina opcional nao carregada: {title} ({exc})")
        return None


def read_tables(path: Path) -> list[pd.DataFrame]:
    try:
        return pd.read_html(path)
    except ValueError:
        return []


def flatten_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if isinstance(out.columns, pd.MultiIndex):
        out.columns = [" ".join(clean_text(x) for x in col if clean_text(x) and not clean_text(x).startswith("Unnamed")) for col in out.columns]
    else:
        out.columns = [clean_text(c) for c in out.columns]
    return out


def columns_text(df: pd.DataFrame) -> list[str]:
    """Rotulos de coluna achatados e limpos (lida com MultiIndex)."""
    if isinstance(df.columns, pd.MultiIndex):
        return [clean_text(" ".join(str(x) for x in col)) for col in df.columns]
    return [clean_text(c) for c in df.columns]


def has_header_cells(df: pd.DataFrame, terms: list[str], scan_rows: int = 3) -> bool:
    """True se cada termo aparecer em alguma celula das primeiras linhas.

    Necessario para tabelas cujo cabecalho real esta nas primeiras linhas de
    dados (ex.: a tabela de edicoes, com colunas numericas e 'Ano'/'Campeao'
    nas duas primeiras linhas).
    """
    cells = {clean_text(c) for c in df.head(scan_rows).astype(str).values.flatten()}
    return all(any(term in c for c in cells) for term in terms)


def find_table(tables: list[pd.DataFrame], predicate, descricao: str) -> pd.DataFrame:
    """Primeira tabela que casa o predicado; falha alto se nenhuma casar.

    Selecionar por conteudo (e nao por indice fixo) evita quebra silenciosa
    quando a Wikipedia reordena/insere tabelas na pagina.
    """
    for df in tables:
        try:
            if predicate(df):
                return df
        except Exception:
            continue
    raise ValueError(
        f"Tabela nao encontrada na pagina principal da Wikipedia: {descricao}. "
        "O layout da pagina pode ter mudado; revise os predicados em parse_main()."
    )


def parse_main() -> dict:
    path = fetch_page(MAIN_TITLE)
    tables = read_tables(path)

    def cols_superset(*req):
        return lambda df: set(req).issubset(set(columns_text(df)))

    def cols_any(term):
        return lambda df: any(term in c for c in columns_text(df))

    editions_tbl = find_table(
        tables, lambda df: has_header_cells(df, ["Campeão", "Vice-campeão"]),
        "edicoes (campeoes por ano)")
    podium_tbl = find_table(
        tables, cols_superset("Seleção", "Títulos", "Vices"), "podio por selecao")
    confeds_tbl = find_table(
        tables, cols_any("Confedera"), "titulos por confederacao")
    blowouts_tbl = find_table(
        tables, cols_superset("Time 1", "Placar", "Time 2"), "maiores goleadas")
    historical_tbl = find_table(
        tables, cols_superset("Pos.", "Pts", "GP", "GC"), "ranking historico de selecoes")
    attendance_tbl = find_table(
        tables, cols_any("Público Total"), "publico por edicao")
    finals_tbl = find_table(
        tables, cols_any("Público pagante"), "publico das finais")

    return {
        "editions": parse_editions_table(editions_tbl),
        "podium": parse_podium_table(podium_tbl),
        "confeds": dataframe_records(confeds_tbl),
        "blowouts": dataframe_records(blowouts_tbl),
        "historical_ranking": dataframe_records(historical_tbl),
        "attendance": dataframe_records(attendance_tbl),
        "finals_attendance": dataframe_records(finals_tbl),
        "totals": {},  # recalculado em build_payload a partir das 22 edicoes
        "source_url": BASE + MAIN_TITLE,
    }


def parse_editions_table(df: pd.DataFrame) -> list[dict]:
    rows = []
    data = df.iloc[2:].copy()
    for _, r in data.iterrows():
        year_text = clean_text(r.iloc[0])
        year_match = re.search(r"\d{4}", year_text)
        if not year_match:
            continue
        year = int(year_match.group(0))
        if year not in YEARS or year == 2026:  # 2026 em andamento: fora da tabela de campeoes
            continue
        rows.append({
            "ano": year,
            "sede": clean_team(r.iloc[1]),
            "campeao": clean_team(r.iloc[3]),
            "placar_final": clean_text(r.iloc[4]),
            "vice": clean_team(r.iloc[5]),
            "terceiro": clean_team(r.iloc[7]),
            "placar_terceiro": clean_text(r.iloc[8]),
            "quarto": clean_team(r.iloc[9]),
            "url": BASE + PAGE_TITLES[year],
        })
    return rows


def parse_podium_table(df: pd.DataFrame) -> list[dict]:
    out = []
    for _, row in df.iterrows():
        team = clean_team(row.get("Seleção"))
        if not team:
            continue
        out.append({
            "selecao": team,
            "titulos": len(extract_years(row.get("Títulos"))),
            "anos_titulos": extract_years(row.get("Títulos")),
            "vices": len(extract_years(row.get("Vices"))),
            "anos_vices": extract_years(row.get("Vices")),
            "terceiros": len(extract_years(row.get("3º lugar"))),
            "anos_terceiros": extract_years(row.get("3º lugar")),
            "quartos": len(extract_years(row.get("4º lugar"))),
            "anos_quartos": extract_years(row.get("4º lugar")),
        })
    return out


def dataframe_records(df: pd.DataFrame) -> list[dict]:
    out = flatten_columns(df)
    return [{clean_text(k): clean_text(v) for k, v in row.items()} for row in out.to_dict("records")]


def _scorer_side(cell) -> str:
    text = clean_text(cell)
    if not text or re.search(r"(Público|Publico|Árbitro|Arbitro|Relatório|Relatorio)", text, re.I):
        return ""
    return text


def scorer_index_from_tables(tables: list[pd.DataFrame]) -> dict:
    """Indexa marcadores das caixas 2x5 do cache por (time1, gols1, gols2, time2).

    A chave e gravada nas duas ordens de times; a string ja rotula cada lado com
    o nome da selecao, entao o front-end atribui certo independente da ordem.
    """
    idx = {}
    for df in tables:
        dff = flatten_columns(df)
        if dff.shape[0] < 2 or dff.shape[1] < 5:
            continue
        row0 = [clean_text(dff.iloc[0, j]) for j in range(dff.shape[1])]
        row1 = [clean_text(dff.iloc[1, j]) for j in range(dff.shape[1])]
        goals = score_goals(row0[2])
        t1, t2 = clean_team(row0[1]), clean_team(row0[3])
        if not goals or not t1 or not t2:
            continue
        s1, s2 = _scorer_side(row1[1]), _scorer_side(row1[3])
        segs = []
        if s1:
            segs.append(f"{t1}: {s1}")
        if s2:
            segs.append(f"{t2}: {s2}")
        if not segs:
            continue
        combined = " | ".join(segs)
        idx.setdefault((t1, goals[0], goals[1], t2), combined)
        idx.setdefault((t2, goals[1], goals[0], t1), combined)
    return idx


def enrich_scorers(matches: list[dict], idx: dict) -> None:
    """Preenche marcadores vazios a partir do indice do cache (nao sobrescreve)."""
    for p in matches:
        if (p.get("marcadores") or "").strip():
            continue
        goals = score_goals(p.get("placar"))
        if not goals:
            continue
        found = idx.get((clean_team(p.get("time1")), goals[0], goals[1], clean_team(p.get("time2"))))
        if found:
            p["marcadores"] = found


# Melhor jogador cuja bandeira nao aparece na infobox (fallback curado).
MELHOR_JOGADOR_SELECAO = {1954: "Hungria"}


def parse_melhor_jogador(path: Path, year: int) -> tuple[str, str]:
    """(nome, selecao) do melhor jogador, direto da linha da infobox (HTML).

    Mais confiavel que o DataFrame: pega o nome pelo texto e a selecao pelo alt
    da bandeira. Se a bandeira faltar, usa o fallback curado.
    """
    fallback = MELHOR_JOGADOR_SELECAO.get(year, "")
    try:
        doc = lxml_html.fromstring(path.read_text(encoding="utf-8"))
    except Exception:
        return "", fallback
    for box in doc.xpath('//table[contains(@class,"infobox")]'):
        for tr in box.xpath(".//tr"):
            th = tr.xpath("./th")
            label = clean_text(th[0].text_content()).lower() if th else ""
            if "melhor jogador" in label and "jovem" not in label:
                td = tr.xpath("./td")
                if td:
                    nome = clean_text(td[0].text_content())
                    pais = ""
                    for im in td[0].xpath(".//img"):
                        if im.get("alt"):
                            pais = clean_team(im.get("alt"))
                            break
                    return nome, (pais or fallback)
    return "", fallback


# --- Copa de 2026 (48 selecoes, 12 grupos) — edicao em andamento ------
# Formato novo que o parser generico nao cobre: extracao dedicada a partir
# do cache. Os 12 grupos ficam em tabelas [12,19,...,89] (standings + 6 jogos
# cada); o mata-mata vem por titulo de secao (Dezesseis avos, Oitavas, ...).
def _scorer_2026(s: str) -> str:
    s = clean_text(s)
    return "" if not s or re.search(r"Público|Publico|Árbitro|Arbitro|Relatório|Relatorio", s, re.I) else s


def _box_scorers_2026(dff: pd.DataFrame, t1: str, t2: str) -> str:
    if dff.shape[0] < 2:
        return ""
    row1 = [clean_text(dff.iloc[1, j]) for j in range(dff.shape[1])]
    s1 = _scorer_2026(row1[1] if len(row1) > 1 else "")
    s2 = _scorer_2026(row1[3] if len(row1) > 3 else "")
    segs = []
    if s1:
        segs.append(f"{t1}: {s1}")
    if s2:
        segs.append(f"{t2}: {s2}")
    return " | ".join(segs)


def parse_2026_knockout(path: Path) -> list[dict]:
    """Jogos de mata-mata de 2026, com a fase pelo titulo (h3/h4) da secao."""
    doc = lxml_html.fromstring(path.read_text(encoding="utf-8"))
    out, phase, seen = [], "", False
    for el in doc.iter():
        if el.tag in ("h2", "h3", "h4"):
            t = clean_text(el.text_content())
            if "Fase final" in t:
                seen = True
            if seen and el.tag in ("h3", "h4"):
                phase = t
        if not seen or el.tag != "table":
            continue
        rows = el.xpath("./tr") + el.xpath("./tbody/tr")
        if not rows:
            continue
        r0 = [html_cell_text(c) for c in rows[0].xpath("./th|./td")]
        r1 = [html_cell_text(c) for c in rows[1].xpath("./th|./td")] if len(rows) > 1 else []
        if len(r0) < 5:
            continue
        goals = score_goals(r0[2])
        t1, t2 = clean_team(r0[1]), clean_team(r0[3])
        if not goals or not is_valid_team_name(t1) or not is_valid_team_name(t2):
            continue
        s1 = _scorer_2026(r1[1] if len(r1) > 1 else "")
        s2 = _scorer_2026(r1[3] if len(r1) > 3 else "")
        segs = ([f"{t1}: {s1}"] if s1 else []) + ([f"{t2}: {s2}"] if s2 else [])
        out.append({
            "fase": phase, "grupo": "", "data": clean_text(r0[0]), "time1": t1,
            "placar": clean_text(r0[2]), "time2": t2, "gols": sum(goals),
            "estadio": clean_text(r0[4]), "detalhes": "", "marcadores": " | ".join(segs),
        })
    return out


def parse_2026_info(path: Path) -> dict:
    doc = lxml_html.fromstring(path.read_text(encoding="utf-8"))
    info = {"ano": 2026, "sede": "Canadá, EUA e México", "campeao": "Em andamento"}
    boxes = doc.xpath('//table[contains(@class,"infobox")]')
    if not boxes:
        return info
    for tr in boxes[0].xpath(".//tr"):
        th, td = tr.xpath("./th"), tr.xpath("./td")
        if not th or not td:
            continue
        key = clean_text(th[0].text_content()).lower()
        val = clean_text(td[0].text_content())
        if "participantes" in key:
            info["participantes"] = to_int(val)
        elif "partidas" in key:
            info["jogos"] = to_int(val)
        elif key.startswith("gol"):
            info["gols"] = to_int(val.split("(")[0])
        elif "melhor marcador" in key or "artilheiro" in key:
            info["artilheiro"] = val
    return info


def _ficha_2026_franca_inglaterra() -> dict:
    return {
        "data": "18 de julho",
        "hora": "18:00",
        "estadio": "Hard Rock Stadium, Miami",
        "publico": "64 478",
        "arbitro": "Jesús Valenzuela Sáez",
        "arbitro_pais": "Venezuela",
        "t1": {
            "nome": "França",
            "tec": "Didier Deschamps",
            "xi": [
                ["", "GOL", "Mike Maignan"],
                ["", "LD", "Malo Gusto"],
                ["", "ZAG", "Ibrahima Konaté"],
                ["", "ZAG", "Maxence Lacroix"],
                ["", "LE", "Theo Hernández"],
                ["", "MC", "Warren Zaïre-Emery"],
                ["", "MC", "Adrien Rabiot"],
                ["", "MEI", "Michael Olise"],
                ["", "MEI", "Rayan Cherki"],
                ["", "MEI", "Désiré Doué"],
                ["", "ATA", "Kylian Mbappé"],
            ],
            "res": [
                ["", "46'", "Dayot Upamecano"],
                ["", "46'", "Lucas Digne"],
                ["", "46'", "Ousmane Dembélé"],
                ["", "46'", "Bradley Barcola"],
                ["", "90+1'", "Jules Koundé"],
            ],
        },
        "t2": {
            "nome": "Inglaterra",
            "tec": "Thomas Tuchel",
            "xi": [
                ["", "GOL", "Dean Henderson"],
                ["", "LD", "Jarell Quansah"],
                ["", "ZAG", "Ezri Konsa"],
                ["", "ZAG", "Marc Guéhi"],
                ["", "LE", "Djed Spence"],
                ["", "MC", "Declan Rice"],
                ["", "MC", "Eberechi Eze"],
                ["", "MEI", "Morgan Rogers"],
                ["", "ATA", "Marcus Rashford"],
                ["", "ATA", "Bukayo Saka"],
                ["", "ATA", "Ivan Toney"],
            ],
            "res": [
                ["", "46'", "Ollie Watkins"],
                ["", "79'", "Jude Bellingham"],
                ["", "79'", "Elliot Anderson"],
                ["", "83'", "Reece James"],
                ["", "90+2'", "Trevoh Chalobah"],
            ],
        },
    }


def apply_2026_completed_updates(matches: list[dict], info: dict) -> None:
    """Complementa jogos de 2026 concluídos após o cache local da Wikipedia.

    O cache evita downloads repetidos, mas a edição está em andamento. Esta
    camada mantém o dashboard coerente quando a página online avança.
    """
    def m(phase: str, date: str, t1: str, score: str, t2: str, stadium: str, winner: str = "", scorers: str = "", details: str = "", ficha: dict | None = None) -> dict:
        goals = score_goals(score)
        out = {
            "fase": phase,
            "grupo": "",
            "data": date,
            "time1": t1,
            "placar": score,
            "time2": t2,
            "gols": sum(goals) if goals else 0,
            "estadio": stadium,
            "detalhes": details,
            "marcadores": scorers,
            "vencedor": winner,
        }
        if ficha:
            out["ficha"] = ficha
        return out

    updates = [
        m("Oitavas de final", "5 de julho", "Brasil", "1 - 2", "Noruega", "MetLife Stadium, East Rutherford", "Noruega", "Brasil: Neymar 90+10' (pen) | Noruega: Haaland 79', 90'"),
        m("Oitavas de final", "5 de julho", "México", "2 - 3", "Inglaterra", "Estádio Azteca, Cidade do México", "Inglaterra", "México: Julián Quiñones 42' (voleio); Raúl Jiménez 69' (pen) | Inglaterra: Jude Bellingham 36' (cab), 38'; Harry Kane 60' (pen)"),
        m("Oitavas de final", "6 de julho", "Portugal", "0 - 1", "Espanha", "AT&T Stadium, Arlington", "Espanha", "Espanha: Merino 90+1'"),
        m("Oitavas de final", "6 de julho", "Estados Unidos", "1 - 4", "Bélgica", "Lumen Field, Seattle", "Bélgica", "Estados Unidos: Malik Tillman 31' (falta) | Bélgica: Charles De Ketelaere 9', 33' (cab); Hans Vanaken 57'; Romelu Lukaku 90+3'"),
        m("Oitavas de final", "7 de julho", "Argentina", "3 - 2", "Egito", "Mercedes-Benz Stadium, Atlanta", "Argentina", "Argentina: Cristian Romero 79' (cab); Lionel Messi 83'; Enzo Fernández 90+2' (cab) | Egito: Yasser Ibrahim 15' (cab); Mostafa Ziko 67'"),
        m("Oitavas de final", "7 de julho", "Suíça", "0 - 0 (pen 4 - 3)", "Colômbia", "BC Place, Vancouver", "Suíça", details="Penalidades: Suíça 4 - 3 Colômbia"),
        m("Quartas de final", "9 de julho", "França", "2 - 0", "Marrocos", "Estádio Boston, Foxborough", "França", "França: Kylian Mbappé 60'; Ousmane Dembélé 66'"),
        m("Quartas de final", "10 de julho", "Espanha", "2 - 1", "Bélgica", "Los Angeles Stadium, Inglewood", "Espanha", "Espanha: Fabián Ruiz 30'; Mikel Merino 88' | Bélgica: Charles De Ketelaere 41' (cab)"),
        m("Quartas de final", "11 de julho", "Noruega", "1 - 2 (pro)", "Inglaterra", "Estádio Boston, Foxborough", "Inglaterra", "Noruega: Andreas Schjelderup 36' | Inglaterra: Jude Bellingham 45+2', 93'"),
        m("Quartas de final", "11 de julho", "Argentina", "3 - 1 (pro)", "Suíça", "Kansas City Stadium, Kansas City", "Argentina", "Argentina: Alexis Mac Allister 10' (cab); Julián Álvarez 112'; Lautaro Martínez 120+1' | Suíça: Dan Ndoye 67'"),
        m("Semifinal", "14 de julho", "França", "0 - 2", "Espanha", "AT&T Stadium, Arlington", "Espanha", "Espanha: Mikel Oyarzabal 22' (pen); Pedro Porro 58'"),
        m("Semifinal", "15 de julho", "Inglaterra", "1 - 2", "Argentina", "Mercedes-Benz Stadium, Atlanta", "Argentina", "Inglaterra: Anthony Gordon 55' | Argentina: Enzo Fernández 85'; Lautaro Martínez 90+2'"),
        m("Terceiro lugar", "18 de julho", "França", "4 - 6", "Inglaterra", "Hard Rock Stadium, Miami", "Inglaterra", "França: Kylian Mbappé 48', 66'; Bradley Barcola 54'; Ousmane Dembélé 90+6' | Inglaterra: Declan Rice 3'; Ezri Konsa 18' (cab); Bukayo Saka 37', 45+1', 87' (pen); Jude Bellingham 90+8'", ficha=_ficha_2026_franca_inglaterra()),
    ]
    seen = {(p.get("fase"), p.get("data"), p.get("time1"), p.get("placar"), p.get("time2")) for p in matches}
    for item in updates:
        key = (item["fase"], item["data"], item["time1"], item["placar"], item["time2"])
        if key not in seen:
            matches.append(item)
            seen.add(key)
    info.update({
        "jogos": max(to_int(info.get("jogos")), 103),
        "gols": max(to_int(info.get("gols")), 307),
        "artilheiro": "10 gols: Kylian Mbappé",
    })


def apply_2026_ranking_updates(ranking: list[dict], groups: list[dict], matches: list[dict]) -> None:
    """Atualiza posicoes ja definidas em 2026 enquanto a final nao foi jogada."""
    stats: dict[str, dict] = {}
    for gr in groups:
        team = gr.get("selecao")
        if not is_valid_team_name(team):
            continue
        stats[team] = {
            "grupo": gr.get("grupo", ""),
            "pts": to_int(gr.get("pts")),
            "j": to_int(gr.get("j")),
            "v": to_int(gr.get("v")),
            "e": to_int(gr.get("e")),
            "d": to_int(gr.get("d")),
            "gp": to_int(gr.get("gp")),
            "gc": to_int(gr.get("gc")),
        }
    for p in matches:
        if p.get("fase") == "Fase de grupos":
            continue
        goals = score_goals(p.get("placar"))
        if not goals:
            continue
        for team, gf, ga in ((p.get("time1"), goals[0], goals[1]), (p.get("time2"), goals[1], goals[0])):
            if not is_valid_team_name(team):
                continue
            row = stats.setdefault(team, {"grupo": "", "pts": 0, "j": 0, "v": 0, "e": 0, "d": 0, "gp": 0, "gc": 0})
            row["j"] += 1
            row["gp"] += gf
            row["gc"] += ga
            if gf > ga:
                row["v"] += 1
            elif gf < ga:
                row["d"] += 1
            else:
                row["e"] += 1
    by_team = {r.get("selecao"): r for r in ranking if r.get("selecao")}
    for pos, team in ((3, "Inglaterra"), (4, "França")):
        row = by_team.get(team)
        if not row:
            row = {"selecao": team}
            ranking.append(row)
        s = stats.get(team, {})
        row.update({
            "pos": pos,
            "selecao": team,
            "grupo": s.get("grupo", ""),
            "pts": s.get("pts", 0),
            "j": s.get("j", 0),
            "v": s.get("v", 0),
            "e": s.get("e", 0),
            "d": s.get("d", 0),
            "gp": s.get("gp", 0),
            "gc": s.get("gc", 0),
            "sg": f"{s.get('gp', 0) - s.get('gc', 0):+d}",
        })
    ranking.sort(key=lambda r: to_int(r.get("pos")) or 999)


def parse_2026(title: str, path: Path, tables: list[pd.DataFrame]) -> dict:
    letters = "ABCDEFGHIJKL"
    groups: list[dict] = []
    matches: list[dict] = []
    for gi in range(12):
        sti = 12 + gi * 7
        gname = f"Grupo {letters[gi]}"
        dff = flatten_columns(tables[sti])
        for _, r in dff.iterrows():
            vals = [clean_text(r.iloc[j]) for j in range(dff.shape[1])]
            pos, team = to_int(vals[0]), clean_team(vals[1])
            if not pos or not team or team in {"Equipe", "Seleção"}:
                continue
            classif = (vals[10] if len(vals) > 10 else "").lower()
            groups.append({
                "grupo": gname, "pos": pos, "selecao": team, "pts": to_int(vals[2]),
                "j": to_int(vals[3]), "v": to_int(vals[4]), "e": to_int(vals[5]),
                "d": to_int(vals[6]), "gp": to_int(vals[7]), "gc": to_int(vals[8]),
                "sg": clean_text(vals[9]), "classificado": "sim" if "final" in classif else "eliminado",
            })
        for ti in range(sti + 1, sti + 7):
            d = flatten_columns(tables[ti])
            m = parse_knockout_match(d, "Fase de grupos")
            if not m:
                continue
            m["grupo"] = gname
            m["marcadores"] = _box_scorers_2026(d, m["time1"], m["time2"])
            matches.append(m)
    matches += parse_2026_knockout(path)
    info = parse_2026_info(path)
    apply_2026_completed_updates(matches, info)
    final_ranking = parse_final_ranking(tables)
    apply_2026_ranking_updates(final_ranking, groups, matches)
    return {
        "ano": 2026, "titulo_pagina": title.replace("_", " "), "url": BASE + title,
        "info": info, "grupos": groups, "partidas": matches,
        "classificacao_final": final_ranking,
        "premios": parse_awards(tables), "estadios": parse_stadiums(tables, info),
    }


def parse_worldcup_page(year: int) -> dict:
    title = PAGE_TITLES[year]
    path = fetch_page(title)
    tables = read_tables(path)
    if year == 2026:
        return parse_2026(title, path, tables)
    info = parse_infobox(tables[0] if tables else pd.DataFrame(), year)
    nome_mj, sel_mj = parse_melhor_jogador(path, year)
    if nome_mj:
        info["melhor_jogador"] = nome_mj
    info["melhor_jogador_selecao"] = sel_mj
    groups = parse_groups(tables)
    matches = parse_matches(tables)
    apply_group_scorers(year, groups, matches)
    final_ranking = parse_final_ranking(tables)
    awards = parse_awards(tables)
    stadiums = parse_stadiums(tables, info)
    groups, matches = apply_edition_overrides(year, groups, matches)
    # Enriquece marcadores vazios (ex.: mata-mata das Copas modernas, cujas caixas
    # 2x5 existem no cache mas nao sao lidas pelo parser de chaveamento) a partir do
    # indice do cache. Nao sobrescreve marcadores ja preenchidos, entao e seguro p/ todas.
    enrich_scorers(matches, scorer_index_from_tables(tables))
    if year == 1930:
        info.update({"jogos": 18, "gols": 70, "participantes": 13})
    return {
        "ano": year,
        "titulo_pagina": title.replace("_", " "),
        "url": BASE + title,
        "info": info,
        "grupos": groups,
        "partidas": matches,
        "classificacao_final": final_ranking,
        "premios": awards,
        "estadios": stadiums,
    }


def parse_infobox(df: pd.DataFrame, year: int) -> dict:
    info = {"ano": year}
    if df.empty or df.shape[1] < 2:
        return info
    for _, row in df.iterrows():
        key = clean_text(row.iloc[0]).lower()
        val = clean_text(row.iloc[1])
        if not key or not val:
            continue
        if "organização" in key:
            info["organizacao"] = val
        elif "participantes" in key:
            info["participantes"] = to_int(val)
        elif "anfitri" in key or "país-sede" in key or "sede" == key:
            info["sede"] = clean_team(val)
        elif "campeão" in key:
            info["campeao"] = clean_team(val)
        elif "vice" in key:
            info["vice"] = clean_team(val)
        elif "jogos" in key or "partidas" in key:
            info["jogos"] = to_int(val)
        elif "golos" in key or "gols" in key:
            info["gols"] = to_int(val)
        elif "público" in key:
            info["publico"] = to_int(val)
        elif "melhor jogador" in key and "jovem" not in key:
            info["melhor_jogador"] = val
        elif "artilheiro" in key:
            info["artilheiro"] = val
        elif "mascote" in key:
            info["mascote"] = val
        elif "bola" in key:
            info["bola"] = val
    return info


def apply_edition_overrides(year: int, groups: list[dict], matches: list[dict]) -> tuple[list[dict], list[dict]]:
    if year == 1950:
        groups_1950 = [
            {"grupo": "Grupo A", "pos": 1, "selecao": "Brasil", "pts": 5, "j": 3, "v": 2, "e": 1, "d": 0, "gp": 8, "gc": 2, "sg": "+6", "classificado": "sim"},
            {"grupo": "Grupo A", "pos": 2, "selecao": "Iugoslávia", "pts": 4, "j": 3, "v": 2, "e": 0, "d": 1, "gp": 7, "gc": 3, "sg": "+4", "classificado": "eliminado"},
            {"grupo": "Grupo A", "pos": 3, "selecao": "Suíça", "pts": 3, "j": 3, "v": 1, "e": 1, "d": 1, "gp": 4, "gc": 6, "sg": "-2", "classificado": "eliminado"},
            {"grupo": "Grupo A", "pos": 4, "selecao": "México", "pts": 0, "j": 3, "v": 0, "e": 0, "d": 3, "gp": 2, "gc": 10, "sg": "-8", "classificado": "eliminado"},
            {"grupo": "Grupo B", "pos": 1, "selecao": "Espanha", "pts": 6, "j": 3, "v": 3, "e": 0, "d": 0, "gp": 6, "gc": 1, "sg": "+5", "classificado": "sim"},
            {"grupo": "Grupo B", "pos": 2, "selecao": "Inglaterra", "pts": 2, "j": 3, "v": 1, "e": 0, "d": 2, "gp": 2, "gc": 2, "sg": "0", "classificado": "eliminado"},
            {"grupo": "Grupo B", "pos": 3, "selecao": "Chile", "pts": 2, "j": 3, "v": 1, "e": 0, "d": 2, "gp": 5, "gc": 6, "sg": "-1", "classificado": "eliminado"},
            {"grupo": "Grupo B", "pos": 4, "selecao": "Estados Unidos", "pts": 2, "j": 3, "v": 1, "e": 0, "d": 2, "gp": 4, "gc": 8, "sg": "-4", "classificado": "eliminado"},
            {"grupo": "Grupo C", "pos": 1, "selecao": "Suécia", "pts": 3, "j": 2, "v": 1, "e": 1, "d": 0, "gp": 5, "gc": 4, "sg": "+1", "classificado": "sim"},
            {"grupo": "Grupo C", "pos": 2, "selecao": "Itália", "pts": 2, "j": 2, "v": 1, "e": 0, "d": 1, "gp": 4, "gc": 3, "sg": "+1", "classificado": "eliminado"},
            {"grupo": "Grupo C", "pos": 3, "selecao": "Paraguai", "pts": 1, "j": 2, "v": 0, "e": 1, "d": 1, "gp": 2, "gc": 4, "sg": "-2", "classificado": "eliminado"},
            {"grupo": "Grupo D", "pos": 1, "selecao": "Uruguai", "pts": 2, "j": 1, "v": 1, "e": 0, "d": 0, "gp": 8, "gc": 0, "sg": "+8", "classificado": "sim"},
            {"grupo": "Grupo D", "pos": 2, "selecao": "Bolívia", "pts": 0, "j": 1, "v": 0, "e": 0, "d": 1, "gp": 0, "gc": 8, "sg": "-8", "classificado": "eliminado"},
            {"grupo": "Quadrangular final", "pos": 1, "selecao": "Uruguai", "pts": 5, "j": 3, "v": 2, "e": 1, "d": 0, "gp": 7, "gc": 5, "sg": "+2", "classificado": "sim"},
            {"grupo": "Quadrangular final", "pos": 2, "selecao": "Brasil", "pts": 4, "j": 3, "v": 2, "e": 0, "d": 1, "gp": 14, "gc": 4, "sg": "+10", "classificado": "eliminado"},
            {"grupo": "Quadrangular final", "pos": 3, "selecao": "Suécia", "pts": 2, "j": 3, "v": 1, "e": 0, "d": 2, "gp": 6, "gc": 11, "sg": "-5", "classificado": "eliminado"},
            {"grupo": "Quadrangular final", "pos": 4, "selecao": "Espanha", "pts": 1, "j": 3, "v": 0, "e": 1, "d": 2, "gp": 4, "gc": 11, "sg": "-7", "classificado": "eliminado"},
        ]

        def m(phase: str, group: str, date: str, t1: str, score: str, t2: str, stadium: str, winner: str = "", scorers: str = "") -> dict:
            goals = score_goals(score)
            return {
                "fase": phase,
                "grupo": group,
                "data": date,
                "time1": t1,
                "placar": score,
                "time2": t2,
                "gols": sum(goals) if goals else 0,
                "estadio": stadium,
                "detalhes": "",
                "marcadores": scorers,
                "vencedor": winner,
            }

        return groups_1950, [
            m("Fase de grupos", "Grupo A", "24 de junho", "Brasil", "4 - 0", "México", "Maracanã, Rio de Janeiro", "Brasil"),
            m("Fase de grupos", "Grupo A", "25 de junho", "Iugoslávia", "3 - 0", "Suíça", "Estádio Independência, Belo Horizonte", "Iugoslávia"),
            m("Fase de grupos", "Grupo A", "28 de junho", "Brasil", "2 - 2", "Suíça", "Estádio do Pacaembu, São Paulo"),
            m("Fase de grupos", "Grupo A", "28 de junho", "Iugoslávia", "4 - 1", "México", "Estádio dos Eucaliptos, Porto Alegre", "Iugoslávia"),
            m("Fase de grupos", "Grupo A", "1 de julho", "Brasil", "2 - 0", "Iugoslávia", "Maracanã, Rio de Janeiro", "Brasil"),
            m("Fase de grupos", "Grupo A", "2 de julho", "Suíça", "2 - 1", "México", "Estádio dos Eucaliptos, Porto Alegre", "Suíça"),
            m("Fase de grupos", "Grupo B", "25 de junho", "Inglaterra", "2 - 0", "Chile", "Maracanã, Rio de Janeiro", "Inglaterra"),
            m("Fase de grupos", "Grupo B", "25 de junho", "Espanha", "3 - 1", "Estados Unidos", "Arena da Baixada, Curitiba", "Espanha"),
            m("Fase de grupos", "Grupo B", "29 de junho", "Espanha", "2 - 0", "Chile", "Maracanã, Rio de Janeiro", "Espanha"),
            m("Fase de grupos", "Grupo B", "29 de junho", "Estados Unidos", "1 - 0", "Inglaterra", "Estádio Independência, Belo Horizonte", "Estados Unidos"),
            m("Fase de grupos", "Grupo B", "2 de julho", "Espanha", "1 - 0", "Inglaterra", "Maracanã, Rio de Janeiro", "Espanha"),
            m("Fase de grupos", "Grupo B", "2 de julho", "Chile", "5 - 2", "Estados Unidos", "Ilha do Retiro, Recife", "Chile"),
            m("Fase de grupos", "Grupo C", "25 de junho", "Suécia", "3 - 2", "Itália", "Estádio do Pacaembu, São Paulo", "Suécia"),
            m("Fase de grupos", "Grupo C", "29 de junho", "Suécia", "2 - 2", "Paraguai", "Arena da Baixada, Curitiba"),
            m("Fase de grupos", "Grupo C", "2 de julho", "Itália", "2 - 0", "Paraguai", "Estádio do Pacaembu, São Paulo", "Itália"),
            m("Fase de grupos", "Grupo D", "2 de julho", "Uruguai", "8 - 0", "Bolívia", "Estádio Independência, Belo Horizonte", "Uruguai"),
            m("Fase final", "Quadrangular final", "9 de julho", "Brasil", "7 - 1", "Suécia", "Maracanã, Rio de Janeiro", "Brasil"),
            m("Fase final", "Quadrangular final", "9 de julho", "Espanha", "2 - 2", "Uruguai", "Estádio do Pacaembu, São Paulo"),
            m("Fase final", "Quadrangular final", "13 de julho", "Brasil", "6 - 1", "Espanha", "Maracanã, Rio de Janeiro", "Brasil"),
            m("Fase final", "Quadrangular final", "13 de julho", "Uruguai", "3 - 2", "Suécia", "Estádio do Pacaembu, São Paulo", "Uruguai"),
            m("Fase final", "Quadrangular final", "16 de julho", "Suécia", "3 - 1", "Espanha", "Estádio do Pacaembu, São Paulo", "Suécia"),
            m("Fase final", "Quadrangular final", "16 de julho", "Uruguai", "2 - 1", "Brasil", "Maracanã, Rio de Janeiro", "Uruguai", "Uruguai: Schiaffino 66'; Ghiggia 79' | Brasil: Friaça 47'"),
        ]
    if year == 1938:
        def m(phase: str, date: str, t1: str, score: str, t2: str, stadium: str, winner: str = "", details: str = "", scorers: str = "") -> dict:
            goals = score_goals(score)
            return {
                "fase": phase,
                "grupo": "",
                "data": date,
                "time1": t1,
                "placar": score,
                "time2": t2,
                "gols": sum(goals) if goals else 0,
                "estadio": stadium,
                "detalhes": details,
                "marcadores": scorers,
                "vencedor": winner,
            }

        return groups, [
            m("Oitavas de final", "5 de junho", "Itália", "2 - 1 (pro)", "Noruega", "Stade Vélodrome, Marselha", "Itália", scorers="Itália: Ferraris 2'; Piola 94' | Noruega: Brustad 83'"),
            m("Oitavas de final", "5 de junho", "França", "3 - 1", "Bélgica", "Estádio Olímpico de Colombes, Paris", "França", scorers="França: Veinante 1'; Nicolas 16', 69' | Bélgica: Isemborghs 38'"),
            m("Oitavas de final", "5 de junho", "Brasil", "6 - 5 (pro)", "Polônia", "Stade de la Meinau, Estrasburgo", "Brasil", scorers="Brasil: Leônidas 18', 93', 104'; Romeu 25'; Perácio 44', 71' | Polônia: Scherfke 23' (pen.); Wilimowski 53', 59', 89', 118'"),
            m("Oitavas de final", "5 de junho", "Tchecoslováquia", "3 - 0 (pro)", "Países Baixos", "Stade Municipal, Le Havre", "Tchecoslováquia", scorers="Tchecoslováquia: Košťálek 93'; Nejedlý 111'; Zeman 118'"),
            m("Oitavas de final", "5 de junho", "Hungria", "6 - 0", "Índias Orientais Neerlandesas", "Vélodrome Municipal, Reims", "Hungria", scorers="Hungria: Kohut 14'; Toldi 16'; Sárosi 25', 88'; Zsengellér 30', 67'"),
            m("Oitavas de final", "4 de junho", "Suíça", "1 - 1 (pro)", "Alemanha", "Parc des Princes, Paris", "Suíça", "Jogo-desempate em 9 de junho: Alemanha 2 - 4 Suíça", "Suíça: Abegglen 43' | Alemanha: Gauchel 29'"),
            m("Oitavas de final", "9 de junho", "Alemanha", "2 - 4", "Suíça", "Parc des Princes, Paris", "Suíça", "Jogo-desempate", "Alemanha: Hahnemann 8'; Lörtscher 22' (g.c.) | Suíça: Walaschek 42'; Bickel 64'; Abegglen 75', 78'"),
            m("Oitavas de final", "5 de junho", "Suécia", "W.O.", "Áustria", "Stade de Gerland, Lyon", "Suécia", "A Suécia avançou por W.O. após a desistência da Áustria."),
            m("Oitavas de final", "5 de junho", "Cuba", "3 - 3 (pro)", "Romênia", "Stade Chapou, Toulouse", "Cuba", "Jogo-desempate em 9 de junho: Cuba 2 - 1 Romênia", "Cuba: Socorro 44', 103'; Magriñá 69' | Romênia: Bindea 35'; Barátky 88'; Dobay 105'"),
            m("Oitavas de final", "9 de junho", "Cuba", "2 - 1", "Romênia", "Stade Chapou, Toulouse", "Cuba", "Jogo-desempate", "Cuba: Socorro 51'; Fernández 57' | Romênia: Dobay 35'"),
            m("Quartas de final", "12 de junho", "Itália", "3 - 1", "França", "Estádio Olímpico de Colombes, Paris", "Itália", scorers="Itália: Colaussi 9'; Piola 51', 72' | França: Heisserer 10'"),
            m("Quartas de final", "12 de junho", "Brasil", "1 - 1 (pro)", "Tchecoslováquia", "Parc Lescure, Bordeaux", "Brasil", "Jogo-desempate em 14 de junho: Brasil 2 - 1 Tchecoslováquia", "Brasil: Leônidas 30' | Tchecoslováquia: Nejedlý 65' (pen.)"),
            m("Quartas de final", "14 de junho", "Brasil", "2 - 1", "Tchecoslováquia", "Parc Lescure, Bordeaux", "Brasil", "Jogo-desempate", "Brasil: Leônidas 57'; Roberto 62' | Tchecoslováquia: Kopecký 25'"),
            m("Quartas de final", "12 de junho", "Hungria", "2 - 0", "Suíça", "Stade Victor Boucquey, Lille", "Hungria", scorers="Hungria: Sárosi 40'; Zsengellér 89'"),
            m("Quartas de final", "12 de junho", "Suécia", "8 - 0", "Cuba", "Stade du Fort Carré, Antibes", "Suécia", scorers="Suécia: H. Andersson 9', 81', 90'; Wetterström 32', 37', 44'; Keller 80'; Nyberg 84'"),
            m("Semifinal", "16 de junho", "Itália", "2 - 1", "Brasil", "Stade Vélodrome, Marselha", "Itália", scorers="Itália: Colaussi 51'; Meazza 60' (pen.) | Brasil: Romeu 87'"),
            m("Semifinal", "16 de junho", "Hungria", "5 - 1", "Suécia", "Parc des Princes, Paris", "Hungria", scorers="Hungria: Jacobsson 19' (g.c.); Titkos 37'; Zsengellér 39', 85'; Sárosi 65' | Suécia: Nyberg 1'"),
            m("Terceiro lugar", "19 de junho", "Brasil", "4 - 2", "Suécia", "Parc Lescure, Bordeaux", "Brasil", scorers="Brasil: Romeu 44'; Leônidas 63', 74'; Perácio 80' | Suécia: Jonasson 28'; Nyberg 38'"),
            m("Final", "19 de junho", "Itália", "4 - 2", "Hungria", "Estádio Olímpico de Colombes, Paris", "Itália", scorers="Itália: Colaussi 6', 35'; Piola 16', 82' | Hungria: Titkos 8'; Sárosi 70'"),
        ]
    if year == 1934:
        def m(phase: str, date: str, t1: str, score: str, t2: str, stadium: str, winner: str = "", details: str = "", scorers: str = "") -> dict:
            goals = score_goals(score)
            return {
                "fase": phase,
                "grupo": "",
                "data": date,
                "time1": t1,
                "placar": score,
                "time2": t2,
                "gols": sum(goals) if goals else 0,
                "estadio": stadium,
                "detalhes": details,
                "marcadores": scorers,
                "vencedor": winner,
            }

        return groups, [
            m("Oitavas de final", "27 de maio", "Itália", "7 - 1", "Estados Unidos", "Stadio Nazionale PNF, Roma", "Itália"),
            m("Oitavas de final", "27 de maio", "Espanha", "3 - 1", "Brasil", "Stadio Luigi Ferraris, Gênova", "Espanha"),
            m("Oitavas de final", "27 de maio", "Áustria", "3 - 2 (pro)", "França", "Stadio Benito Mussolini, Turim", "Áustria"),
            m("Oitavas de final", "27 de maio", "Hungria", "4 - 2", "Egito", "Estádio Giorgio Ascarelli, Nápoles", "Hungria"),
            m("Oitavas de final", "27 de maio", "Tchecoslováquia", "2 - 1", "Romênia", "Stadio Littorio, Trieste", "Tchecoslováquia"),
            m("Oitavas de final", "27 de maio", "Suíça", "3 - 2", "Países Baixos", "Stadio San Siro, Milão", "Suíça"),
            m("Oitavas de final", "27 de maio", "Alemanha", "5 - 2", "Bélgica", "Stadio Giovanni Berta, Florença", "Alemanha"),
            m("Oitavas de final", "27 de maio", "Suécia", "3 - 2", "Argentina", "Stadio Littorale, Bolonha", "Suécia"),
            m("Quartas de final", "31 de maio", "Itália", "1 - 1", "Espanha", "Stadio Giovanni Berta, Florença", "Itália", "Jogo-desempate em 1 de junho: Itália 1 - 0 Espanha"),
            m("Quartas de final", "31 de maio", "Áustria", "2 - 1", "Hungria", "Stadio Littorale, Bolonha", "Áustria"),
            m("Quartas de final", "31 de maio", "Tchecoslováquia", "3 - 2", "Suíça", "Stadio Benito Mussolini, Turim", "Tchecoslováquia"),
            m("Quartas de final", "31 de maio", "Alemanha", "2 - 1", "Suécia", "Stadio San Siro, Milão", "Alemanha"),
            m("Semifinal", "3 de junho", "Itália", "1 - 0", "Áustria", "Estádio San Siro, Milão", "Itália"),
            m("Semifinal", "3 de junho", "Tchecoslováquia", "3 - 1", "Alemanha", "Stadio Nazionale PNF, Roma", "Tchecoslováquia"),
            m("Terceiro lugar", "7 de junho", "Alemanha", "3 - 2", "Áustria", "Estádio Giorgio Ascarelli, Nápoles", "Alemanha"),
            m("Final", "10 de junho", "Itália", "2 - 1 (pro)", "Tchecoslováquia", "Stadio Nazionale PNF, Roma", "Itália"),
        ]
    if year == 1954:
        # A Wikipedia mistura a fase de grupos (com playoffs de desempate) e o
        # mata-mata em tabelas de 4 colunas parecidas. O parser generico:
        # (1) atribui as fases eliminatorias como "Oitavas de final", mas 1954
        #     NAO teve oitavas (grupos -> quartas direto); e
        # (2) puxa a quartas "Austria 7-5 Suica" (Batalha de Lausanne) para
        #     dentro do Grupo D, deixando o chaveamento so com 3 quartas.
        # Os grupos vem corretos do parser; aqui removemos a quartas vazada e
        # reconstruimos o mata-mata com as fases certas.
        def m(phase: str, date: str, t1: str, score: str, t2: str, stadium: str, winner: str = "", scorers: str = "") -> dict:
            goals = score_goals(score)
            return {
                "fase": phase,
                "grupo": "",
                "data": date,
                "time1": t1,
                "placar": score,
                "time2": t2,
                "gols": sum(goals) if goals else 0,
                "estadio": stadium,
                "detalhes": "",
                "marcadores": scorers,
                "vencedor": winner,
            }

        group_matches = [
            p for p in matches
            if p.get("fase") == "Fase de grupos"
            and {clean_team(p.get("time1")), clean_team(p.get("time2"))} != {"Áustria", "Suíça"}
        ]
        knockout = [
            m("Quartas de final", "26 de junho", "Áustria", "7 - 5", "Suíça", "Stade Olympique de la Pontaise, Lausanne", "Áustria"),
            m("Quartas de final", "26 de junho", "Uruguai", "4 - 2", "Inglaterra", "St. Jakob-Park, Basileia", "Uruguai"),
            m("Quartas de final", "26 de junho", "Hungria", "4 - 2", "Brasil", "Wankdorf, Berna", "Hungria"),
            m("Quartas de final", "26 de junho", "Alemanha", "2 - 0", "Iugoslávia", "Charmilles, Genebra", "Alemanha"),
            m("Semifinal", "30 de junho", "Alemanha", "6 - 1", "Áustria", "St. Jakob-Park, Basileia", "Alemanha"),
            m("Semifinal", "30 de junho", "Hungria", "4 - 2 (pro)", "Uruguai", "Stade Olympique de la Pontaise, Lausanne", "Hungria"),
            m("Terceiro lugar", "3 de julho", "Áustria", "3 - 1", "Uruguai", "Hardturm, Zurique", "Áustria"),
            m("Final", "4 de julho", "Alemanha", "3 - 2", "Hungria", "Wankdorf, Berna", "Alemanha", "Alemanha: Morlock 10'; Rahn 18', 84' | Hungria: Puskás 6'; Czibor 8'"),
        ]
        return groups, group_matches + knockout
    if year == 1958:
        groups_1958 = [
            {'grupo': 'Grupo A', 'pos': 1, 'selecao': 'Irlanda do Norte', 'pts': 5, 'j': 4, 'v': 2, 'e': 1, 'd': 1, 'gp': 6, 'gc': 6, 'sg': '0', 'classificado': 'sim'},
            {'grupo': 'Grupo A', 'pos': 2, 'selecao': 'Alemanha', 'pts': 4, 'j': 3, 'v': 1, 'e': 2, 'd': 0, 'gp': 7, 'gc': 5, 'sg': '+2', 'classificado': 'sim'},
            {'grupo': 'Grupo A', 'pos': 3, 'selecao': 'Tchecoslováquia', 'pts': 3, 'j': 4, 'v': 1, 'e': 1, 'd': 2, 'gp': 9, 'gc': 6, 'sg': '+3', 'classificado': 'eliminado'},
            {'grupo': 'Grupo A', 'pos': 4, 'selecao': 'Argentina', 'pts': 2, 'j': 3, 'v': 1, 'e': 0, 'd': 2, 'gp': 5, 'gc': 10, 'sg': '-5', 'classificado': 'eliminado'},
            {'grupo': 'Grupo B', 'pos': 1, 'selecao': 'França', 'pts': 4, 'j': 3, 'v': 2, 'e': 0, 'd': 1, 'gp': 11, 'gc': 7, 'sg': '+4', 'classificado': 'sim'},
            {'grupo': 'Grupo B', 'pos': 2, 'selecao': 'Iugoslávia', 'pts': 4, 'j': 3, 'v': 1, 'e': 2, 'd': 0, 'gp': 7, 'gc': 6, 'sg': '+1', 'classificado': 'sim'},
            {'grupo': 'Grupo B', 'pos': 3, 'selecao': 'Paraguai', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 9, 'gc': 12, 'sg': '-3', 'classificado': 'eliminado'},
            {'grupo': 'Grupo B', 'pos': 4, 'selecao': 'Escócia', 'pts': 1, 'j': 3, 'v': 0, 'e': 1, 'd': 2, 'gp': 4, 'gc': 6, 'sg': '-2', 'classificado': 'eliminado'},
            {'grupo': 'Grupo C', 'pos': 1, 'selecao': 'Suécia', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 5, 'gc': 1, 'sg': '+4', 'classificado': 'sim'},
            {'grupo': 'Grupo C', 'pos': 2, 'selecao': 'País de Gales', 'pts': 5, 'j': 4, 'v': 1, 'e': 3, 'd': 0, 'gp': 4, 'gc': 3, 'sg': '+1', 'classificado': 'sim'},
            {'grupo': 'Grupo C', 'pos': 3, 'selecao': 'Hungria', 'pts': 3, 'j': 4, 'v': 1, 'e': 1, 'd': 2, 'gp': 7, 'gc': 5, 'sg': '+2', 'classificado': 'eliminado'},
            {'grupo': 'Grupo C', 'pos': 4, 'selecao': 'México', 'pts': 1, 'j': 3, 'v': 0, 'e': 1, 'd': 2, 'gp': 1, 'gc': 8, 'sg': '-7', 'classificado': 'eliminado'},
            {'grupo': 'Grupo D', 'pos': 1, 'selecao': 'Brasil', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 5, 'gc': 0, 'sg': '+5', 'classificado': 'sim'},
            {'grupo': 'Grupo D', 'pos': 2, 'selecao': 'União Soviética', 'pts': 3, 'j': 4, 'v': 2, 'e': 1, 'd': 1, 'gp': 5, 'gc': 4, 'sg': '+1', 'classificado': 'sim'},
            {'grupo': 'Grupo D', 'pos': 3, 'selecao': 'Inglaterra', 'pts': 3, 'j': 4, 'v': 0, 'e': 3, 'd': 1, 'gp': 4, 'gc': 5, 'sg': '-1', 'classificado': 'eliminado'},
            {'grupo': 'Grupo D', 'pos': 4, 'selecao': 'Áustria', 'pts': 1, 'j': 3, 'v': 0, 'e': 1, 'd': 2, 'gp': 2, 'gc': 7, 'sg': '-5', 'classificado': 'eliminado'},
        ]
        matches_1958 = [
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '8 de junho', 'time1': 'Alemanha', 'placar': '3 - 1', 'time2': 'Argentina', 'estadio': 'Malmö, Malmö Stadion', 'gols': 4, 'detalhes': '', 'marcadores': "Alemanha: Rahn 32', 79' Seeler 40' | Argentina: Corbatta 10'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '8 de junho', 'time1': 'Irlanda do Norte', 'placar': '1 - 0', 'time2': 'Tchecoslováquia', 'estadio': 'Halmstad, Örjans Vall', 'gols': 1, 'detalhes': '', 'marcadores': "Irlanda do Norte: Cush 16'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '11 de junho', 'time1': 'Argentina', 'placar': '3 - 1', 'time2': 'Irlanda do Norte', 'estadio': 'Halmstad, Örjans Vall', 'gols': 4, 'detalhes': '', 'marcadores': "Argentina: Corbatta 38' (pen) Menendez 55' Avio 59' | Irlanda do Norte: McParland 3'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '11 de junho', 'time1': 'Alemanha', 'placar': '2 - 2', 'time2': 'Tchecoslováquia', 'estadio': 'Helsingborg, Olympiastadion', 'gols': 4, 'detalhes': '', 'marcadores': "Alemanha: Schafer 59' Rahn 70' | Tchecoslováquia: Dvořák 24' (pen) Zikán 43'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '15 de junho', 'time1': 'Alemanha', 'placar': '2 - 2', 'time2': 'Irlanda do Norte', 'estadio': 'Malmö, Malmö Stadion', 'gols': 4, 'detalhes': '', 'marcadores': "Alemanha: Rahn 20' Seeler 79' | Irlanda do Norte: McParland 17', 58'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '15 de junho', 'time1': 'Tchecoslováquia', 'placar': '6 - 1', 'time2': 'Argentina', 'estadio': 'Helsingborg, Olympiastadion', 'gols': 7, 'detalhes': '', 'marcadores': "Tchecoslováquia: Dvořák 8' Zikán 17', 40' Feureisl 69' Hovorka 82', 89' | Argentina: Corbatta 65' (pen)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '17 de junho', 'time1': 'Irlanda do Norte', 'placar': '2 - 1 (pro)', 'time2': 'Tchecoslováquia', 'estadio': 'Malmö, Malmö Stadion', 'gols': 3, 'detalhes': '', 'marcadores': "Irlanda do Norte: McParland 44', 91' | Tchecoslováquia: Zikán 19'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '8 de junho', 'time1': 'França', 'placar': '7 - 3', 'time2': 'Paraguai', 'estadio': 'Norrköping, Idrottsparken', 'gols': 10, 'detalhes': '', 'marcadores': "França: Fontaine 25', 30', 67' Piantoni 52' Wisniewski 61' Kopa 70' Vincent 83' | Paraguai: Amarilla 20', 44' (pen) Romero 50'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '8 de junho', 'time1': 'Iugoslávia', 'placar': '1 - 1', 'time2': 'Escócia', 'estadio': 'Västerås, Arosvallen', 'gols': 2, 'detalhes': '', 'marcadores': "Iugoslávia: Petaković 13' | Escócia: Murray 48'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '11 de junho', 'time1': 'Iugoslávia', 'placar': '3 - 2', 'time2': 'França', 'estadio': 'Västerås, Arosvallen', 'gols': 5, 'detalhes': '', 'marcadores': "Iugoslávia: Petaković 16' Veselinović 65', 87' | França: Fontaine 5', 85'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '11 de junho', 'time1': 'Paraguai', 'placar': '3 - 2', 'time2': 'Escócia', 'estadio': 'Norrköping, Idrottsparken', 'gols': 5, 'detalhes': '', 'marcadores': "Paraguai: Aguero 4' Ré 44' Parodi 74' | Escócia: Mudie 23' (pen) Collins 76'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '15 de junho', 'time1': 'França', 'placar': '2 - 1', 'time2': 'Escócia', 'estadio': 'Örebro, Eyravallen', 'gols': 3, 'detalhes': '', 'marcadores': "França: Kopa 22' Fontaine 45' | Escócia: Baird 66'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '15 de junho', 'time1': 'Paraguai', 'placar': '3 - 3', 'time2': 'Iugoslávia', 'estadio': 'Eskilstuna, Tunavallen', 'gols': 6, 'detalhes': '', 'marcadores': "Paraguai: Parodi 21' Agüero 49' Romero 90' | Iugoslávia: Ognjanovic 12' Veselinović 29' Rajkov 74'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '8 de junho', 'time1': 'Suécia', 'placar': '3 - 0', 'time2': 'México', 'estadio': 'Estádio Råsunda, Estocolmo', 'gols': 3, 'detalhes': '', 'marcadores': "Suécia: Simonsson 17', 64' Liedholm 58' (pen)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '8 de junho', 'time1': 'Hungria', 'placar': '1 - 1', 'time2': 'País de Gales', 'estadio': 'Sandviken, Järnvallen', 'gols': 2, 'detalhes': '', 'marcadores': "Hungria: Bozsik 4' | País de Gales: J. Charles 26'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '11 de junho', 'time1': 'México', 'placar': '1 - 1', 'time2': 'País de Gales', 'estadio': 'Estocolmo, Estádio Råsunda', 'gols': 2, 'detalhes': '', 'marcadores': "México: Belmonte 69' | País de Gales: I. Allchurch 32'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '12 de junho', 'time1': 'Suécia', 'placar': '2 - 1', 'time2': 'Hungria', 'estadio': 'Estocolmo, Estádio Råsunda', 'gols': 3, 'detalhes': '', 'marcadores': "Suécia: Hamrin 34', 55' | Hungria: Tichy 78'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '15 de junho', 'time1': 'Suécia', 'placar': '0 - 0', 'time2': 'País de Gales', 'estadio': 'Estocolmo, Estádio Råsunda', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '15 de junho', 'time1': 'Hungria', 'placar': '4 - 0', 'time2': 'México', 'estadio': 'Sandviken, Järnvallen', 'gols': 4, 'detalhes': '', 'marcadores': "Hungria: Tichy 19', 46' Sándor 54' Bencsis 69'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '17 de junho', 'time1': 'País de Gales', 'placar': '2 - 1', 'time2': 'Hungria', 'estadio': 'Estocolmo, Estádio Råsunda', 'gols': 3, 'detalhes': '', 'marcadores': "País de Gales: I. Allchurch 55' Medwin 76' | Hungria: Tichy 33'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '8 de junho', 'time1': 'Brasil', 'placar': '3 - 0', 'time2': 'Áustria', 'estadio': 'Rimnersvallen, Uddevalla', 'gols': 3, 'detalhes': '', 'marcadores': "Brasil: Mazzola 38', 89' Nílton Santos 49'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '8 de junho', 'time1': 'União Soviética', 'placar': '2 - 2', 'time2': 'Inglaterra', 'estadio': 'Nya Ullevi, Gotemburgo', 'gols': 4, 'detalhes': '', 'marcadores': "União Soviética: Simonyan 13' A. Ivanov 55' | Inglaterra: Kevan 66' Finney 85' (pen)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '11 de junho', 'time1': 'Brasil', 'placar': '0 - 0', 'time2': 'Inglaterra', 'estadio': 'Nya Ullevi, Gotemburgo', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '11 de junho', 'time1': 'União Soviética', 'placar': '2 - 0', 'time2': 'Áustria', 'estadio': 'Rimnersvallen, Uddevalla', 'gols': 2, 'detalhes': '', 'marcadores': "União Soviética: Ilyin 15' V. Ivanov 63'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '15 de junho', 'time1': 'Inglaterra', 'placar': '2 - 2', 'time2': 'Áustria', 'estadio': 'Borås, Ryavallen', 'gols': 4, 'detalhes': '', 'marcadores': "Inglaterra: Haynes 56' Kevan 74' | Áustria: Koller 15' Körner 71'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '15 de junho', 'time1': 'Brasil', 'placar': '2 - 0', 'time2': 'União Soviética', 'estadio': 'Nya Ullevi, Gotemburgo', 'gols': 2, 'detalhes': '', 'marcadores': "Brasil: Vavá 3', 77'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '17 de junho', 'time1': 'União Soviética', 'placar': '1 - 0', 'time2': 'Inglaterra', 'estadio': 'Gotemburgo, Estádio Ullevi', 'gols': 1, 'detalhes': '', 'marcadores': "União Soviética: Ilyin 68'", 'vencedor': ''},
            {'fase': 'Quartas de final', 'grupo': '', 'data': '19 de junho', 'time1': 'França', 'placar': '4 - 0', 'time2': 'Irlanda do Norte', 'estadio': 'Norrköping, Idrottsparken', 'gols': 4, 'detalhes': '', 'marcadores': "França: Wisnieski 22' Fontaine 55', 63' Piantoni 68'", 'vencedor': ''},
            {'fase': 'Quartas de final', 'grupo': '', 'data': '19 de junho', 'time1': 'Suécia', 'placar': '2 - 0', 'time2': 'União Soviética', 'estadio': 'Estocolmo, Estádio Råsunda', 'gols': 2, 'detalhes': '', 'marcadores': "Suécia: Hamrin 49' Simonsson 88'", 'vencedor': ''},
            {'fase': 'Quartas de final', 'grupo': '', 'data': '19 de junho', 'time1': 'Brasil', 'placar': '1 - 0', 'time2': 'País de Gales', 'estadio': 'Gotemburgo, Estádio Ullevi', 'gols': 1, 'detalhes': '', 'marcadores': "Brasil: Pelé 66'", 'vencedor': ''},
            {'fase': 'Quartas de final', 'grupo': '', 'data': '19 de junho', 'time1': 'Alemanha', 'placar': '1 - 0', 'time2': 'Iugoslávia', 'estadio': 'Malmö, Malmö Stadion', 'gols': 1, 'detalhes': '', 'marcadores': "Alemanha: Rahn 12'", 'vencedor': ''},
            {'fase': 'Semifinal', 'grupo': '', 'data': '24 de junho', 'time1': 'Brasil', 'placar': '5 - 2', 'time2': 'França', 'estadio': 'Estádio Råsunda, Suécia', 'gols': 7, 'detalhes': '', 'marcadores': "Brasil: Vavá 2' Didi 39' Pelé 52', 64', 75' | França: Fontaine 9' Piantoni 83'", 'vencedor': ''},
            {'fase': 'Semifinal', 'grupo': '', 'data': '24 de junho', 'time1': 'Suécia', 'placar': '3 - 1', 'time2': 'Alemanha', 'estadio': 'Gotemburgo, Estádio Ullevi', 'gols': 4, 'detalhes': '', 'marcadores': "Suécia: Skoglund 32' Gren 81' Hamrin 88' | Alemanha: Schäfer 24'", 'vencedor': ''},
            {'fase': 'Terceiro lugar', 'grupo': '', 'data': '28 de junho', 'time1': 'França', 'placar': '6 - 3', 'time2': 'Alemanha', 'estadio': 'Gotemburgo, Estádio Ullevi', 'gols': 9, 'detalhes': '', 'marcadores': "França: Fontaine 16', 36', 78', 89' Kopa 27' (pen) Douis 50' | Alemanha: Cieslarczyk 18' Rahn 52' Schäfer 84'", 'vencedor': ''},
            {'fase': 'Final', 'grupo': '', 'data': '29 de junho', 'time1': 'Brasil', 'placar': '5 - 2', 'time2': 'Suécia', 'estadio': 'Estádio Råsunda, Suécia', 'gols': 7, 'detalhes': '', 'marcadores': "Brasil: Vavá 9', 32' Pelé 55', 90' Zagallo 68' | Suécia: Liedholm 4' Simonsson 80'", 'vencedor': ''},
        ]
        return groups_1958, matches_1958
    if year == 1962:
        groups_1962 = [
            {'grupo': 'Grupo A', 'pos': 1, 'selecao': 'União Soviética', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 8, 'gc': 5, 'sg': '+3', 'classificado': 'sim'},
            {'grupo': 'Grupo A', 'pos': 2, 'selecao': 'Iugoslávia', 'pts': 4, 'j': 3, 'v': 2, 'e': 0, 'd': 1, 'gp': 8, 'gc': 3, 'sg': '+5', 'classificado': 'sim'},
            {'grupo': 'Grupo A', 'pos': 3, 'selecao': 'Uruguai', 'pts': 2, 'j': 3, 'v': 1, 'e': 0, 'd': 2, 'gp': 4, 'gc': 6, 'sg': '-2', 'classificado': 'eliminado'},
            {'grupo': 'Grupo A', 'pos': 4, 'selecao': 'Colômbia', 'pts': 1, 'j': 3, 'v': 0, 'e': 1, 'd': 2, 'gp': 5, 'gc': 11, 'sg': '-6', 'classificado': 'eliminado'},
            {'grupo': 'Grupo B', 'pos': 1, 'selecao': 'Alemanha', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 4, 'gc': 1, 'sg': '+3', 'classificado': 'sim'},
            {'grupo': 'Grupo B', 'pos': 2, 'selecao': 'Chile', 'pts': 4, 'j': 3, 'v': 2, 'e': 0, 'd': 1, 'gp': 5, 'gc': 3, 'sg': '+2', 'classificado': 'sim'},
            {'grupo': 'Grupo B', 'pos': 3, 'selecao': 'Itália', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 3, 'gc': 2, 'sg': '+1', 'classificado': 'eliminado'},
            {'grupo': 'Grupo B', 'pos': 4, 'selecao': 'Suíça', 'pts': 0, 'j': 3, 'v': 0, 'e': 0, 'd': 3, 'gp': 2, 'gc': 8, 'sg': '-6', 'classificado': 'eliminado'},
            {'grupo': 'Grupo C', 'pos': 1, 'selecao': 'Brasil', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 4, 'gc': 1, 'sg': '+3', 'classificado': 'sim'},
            {'grupo': 'Grupo C', 'pos': 2, 'selecao': 'Tchecoslováquia', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 2, 'gc': 3, 'sg': '-1', 'classificado': 'sim'},
            {'grupo': 'Grupo C', 'pos': 3, 'selecao': 'México', 'pts': 2, 'j': 3, 'v': 1, 'e': 0, 'd': 2, 'gp': 3, 'gc': 4, 'sg': '-1', 'classificado': 'eliminado'},
            {'grupo': 'Grupo C', 'pos': 4, 'selecao': 'Espanha', 'pts': 2, 'j': 3, 'v': 1, 'e': 0, 'd': 2, 'gp': 2, 'gc': 3, 'sg': '-1', 'classificado': 'eliminado'},
            {'grupo': 'Grupo D', 'pos': 1, 'selecao': 'Hungria', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 8, 'gc': 2, 'sg': '+6', 'classificado': 'sim'},
            {'grupo': 'Grupo D', 'pos': 2, 'selecao': 'Inglaterra', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 4, 'gc': 3, 'sg': '+1', 'classificado': 'sim'},
            {'grupo': 'Grupo D', 'pos': 3, 'selecao': 'Argentina', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 2, 'gc': 3, 'sg': '-1', 'classificado': 'eliminado'},
            {'grupo': 'Grupo D', 'pos': 4, 'selecao': 'Bulgária', 'pts': 1, 'j': 3, 'v': 0, 'e': 1, 'd': 2, 'gp': 1, 'gc': 7, 'sg': '-6', 'classificado': 'eliminado'},
        ]
        matches_1962 = [
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '30 de maio', 'time1': 'Uruguai', 'placar': '2 - 1', 'time2': 'Colômbia', 'estadio': 'Arica, Estadio Carlos Dittborn', 'gols': 3, 'detalhes': '', 'marcadores': "Uruguai: Sasía 56' Cubilla 75' | Colômbia: Zuluaga 19' (pen)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '31 de maio', 'time1': 'União Soviética', 'placar': '2 - 0', 'time2': 'Iugoslávia', 'estadio': 'Arica, Estadio Carlos Dittborn', 'gols': 2, 'detalhes': '', 'marcadores': "União Soviética: Ivanov 51' Ponedelnik 83'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '2 de junho', 'time1': 'Iugoslávia', 'placar': '3 - 1', 'time2': 'Uruguai', 'estadio': 'Arica, Estadio Carlos Dittborn', 'gols': 4, 'detalhes': '', 'marcadores': "Iugoslávia: Skoblar 25' (pen) Galić 29' Jerković 49' | Uruguai: Cabrera 19'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '3 de junho', 'time1': 'União Soviética', 'placar': '4 - 4', 'time2': 'Colômbia', 'estadio': 'Arica, Estadio Carlos Dittborn', 'gols': 8, 'detalhes': '', 'marcadores': "União Soviética: Ivanov 8', 11' Chislenko 10' Ponedelnik 56' | Colômbia: Aceros 21' Coll 68' gol olímpico Rada 72' Klinger 86'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '6 de junho', 'time1': 'União Soviética', 'placar': '2 - 1', 'time2': 'Uruguai', 'estadio': 'Arica, Estadio Carlos Dittborn', 'gols': 3, 'detalhes': '', 'marcadores': "União Soviética: Mamykin 38' Ivanov 89' | Uruguai: Sasía 54'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '7 de junho', 'time1': 'Iugoslávia', 'placar': '5 - 0', 'time2': 'Colômbia', 'estadio': 'Arica, Estadio Carlos Dittborn', 'gols': 5, 'detalhes': '', 'marcadores': "Iugoslávia: Galić 20', 61' Jerković 25', 87' Melić 82'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '30 de maio', 'time1': 'Chile', 'placar': '3 - 1', 'time2': 'Suíça', 'estadio': 'Santiago - (Ñuñoa), Estádio Nacional de Chile', 'gols': 4, 'detalhes': '', 'marcadores': "Chile: Sánchez 44', 51' Ramírez 55' | Suíça: Wüthrich 6'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '31 de maio', 'time1': 'Alemanha', 'placar': '0 - 0', 'time2': 'Itália', 'estadio': 'Santiago - (Ñuñoa), Estádio Nacional de Chile', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '2 de junho', 'time1': 'Chile', 'placar': '2 - 0', 'time2': 'Itália', 'estadio': 'Santiago - (Ñuñoa), Estádio Nacional de Chile', 'gols': 2, 'detalhes': '', 'marcadores': "Chile: Ramírez 73' Toro 87'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '3 de junho', 'time1': 'Alemanha', 'placar': '2 - 1', 'time2': 'Suíça', 'estadio': 'Santiago - (Ñuñoa), Estádio Nacional de Chile', 'gols': 3, 'detalhes': '', 'marcadores': "Alemanha: Brülls 45' Seeler 59' | Suíça: Schneiter 73'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '6 de junho', 'time1': 'Alemanha', 'placar': '2 - 0', 'time2': 'Chile', 'estadio': 'Santiago - (Ñuñoa), Estádio Nacional de Chile', 'gols': 2, 'detalhes': '', 'marcadores': "Alemanha: Szymaniak 21' (pen) Seeler 82'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '7 de junho', 'time1': 'Itália', 'placar': '3 - 0', 'time2': 'Suíça', 'estadio': 'Santiago - (Ñuñoa), Estádio Nacional de Chile', 'gols': 3, 'detalhes': '', 'marcadores': "Itália: Mora 1' Bulgarelli 65', 67'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '30 de maio', 'time1': 'Brasil', 'placar': '2 - 0', 'time2': 'México', 'estadio': 'Viña del Mar, Estádio Sausalito', 'gols': 2, 'detalhes': '', 'marcadores': "Brasil: Zagallo 56' Pelé 73'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '31 de maio', 'time1': 'Tchecoslováquia', 'placar': '1 - 0', 'time2': 'Espanha', 'estadio': 'Viña del Mar, Estádio Sausalito', 'gols': 1, 'detalhes': '', 'marcadores': "Tchecoslováquia: Štibrányi 80'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '2 de junho', 'time1': 'Brasil', 'placar': '0 - 0', 'time2': 'Tchecoslováquia', 'estadio': 'Viña del Mar, Estádio Sausalito', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '3 de junho', 'time1': 'Espanha', 'placar': '1 - 0', 'time2': 'México', 'estadio': 'Viña del Mar, Estádio Sausalito', 'gols': 1, 'detalhes': '', 'marcadores': "Espanha: Peiró 90'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '6 de junho', 'time1': 'Brasil', 'placar': '2 - 1', 'time2': 'Espanha', 'estadio': 'Viña del Mar, Estádio Sausalito', 'gols': 3, 'detalhes': '', 'marcadores': "Brasil: Amarildo 72', 86' | Espanha: Rodríguez 35'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '7 de junho', 'time1': 'México', 'placar': '3 - 1', 'time2': 'Tchecoslováquia', 'estadio': 'Viña del Mar, Estádio Sausalito', 'gols': 4, 'detalhes': '', 'marcadores': "México: Díaz 12' Del Águila 29' Hernández 90' (pen) | Tchecoslováquia: Mašek 1'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '30 de maio', 'time1': 'Argentina', 'placar': '1 - 0', 'time2': 'Bulgária', 'estadio': 'Rancagua, Estadio El Teniente', 'gols': 1, 'detalhes': '', 'marcadores': "Argentina: Facundo 4'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '31 de maio', 'time1': 'Hungria', 'placar': '2 - 1', 'time2': 'Inglaterra', 'estadio': 'Rancagua, Estadio El Teniente', 'gols': 3, 'detalhes': '', 'marcadores': "Hungria: Tichy 17' Albert 61' | Inglaterra: Flowers 60' (pen)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '2 de junho', 'time1': 'Inglaterra', 'placar': '3 - 1', 'time2': 'Argentina', 'estadio': 'Rancagua, Estadio El Teniente', 'gols': 4, 'detalhes': '', 'marcadores': "Inglaterra: Flowers 17' (pen) Charlton 42' Greaves 67' | Argentina: Sanfilippo 81'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '3 de junho', 'time1': 'Hungria', 'placar': '6 - 1', 'time2': 'Bulgária', 'estadio': 'Rancagua, Estadio El Teniente', 'gols': 7, 'detalhes': '', 'marcadores': "Hungria: Albert 1', 6', 53' Tichy 8', 70' Solymosi 12' | Bulgária: Sokolov 64'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '6 de junho', 'time1': 'Hungria', 'placar': '0 - 0', 'time2': 'Argentina', 'estadio': 'Rancagua, Estadio El Teniente', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '7 de junho', 'time1': 'Inglaterra', 'placar': '0 - 0', 'time2': 'Bulgária', 'estadio': 'Rancagua, Estadio El Teniente', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Quartas de final', 'grupo': '', 'data': '10 de junho', 'time1': 'Chile', 'placar': '2 - 1', 'time2': 'União Soviética', 'estadio': 'Arica, Estadio Carlos Dittborn', 'gols': 3, 'detalhes': '', 'marcadores': "Chile: Sánchez 11' Rojas 29' | União Soviética: Chislenko 26'", 'vencedor': ''},
            {'fase': 'Quartas de final', 'grupo': '', 'data': '10 de junho', 'time1': 'Tchecoslováquia', 'placar': '1 - 0', 'time2': 'Hungria', 'estadio': 'Rancagua, Estadio El Teniente', 'gols': 1, 'detalhes': '', 'marcadores': "Tchecoslováquia: Scherer 13'", 'vencedor': ''},
            {'fase': 'Quartas de final', 'grupo': '', 'data': '10 de junho', 'time1': 'Brasil', 'placar': '3 - 1', 'time2': 'Inglaterra', 'estadio': 'Viña del Mar, Estádio Sausalito', 'gols': 4, 'detalhes': '', 'marcadores': "Brasil: Garrincha 31', 59' Vavá 53' | Inglaterra: Hitchens 38'", 'vencedor': ''},
            {'fase': 'Quartas de final', 'grupo': '', 'data': '10 de junho', 'time1': 'Iugoslávia', 'placar': '1 - 0', 'time2': 'Alemanha', 'estadio': 'Santiago - (Ñuñoa), Estádio Nacional de Chile', 'gols': 1, 'detalhes': '', 'marcadores': "Iugoslávia: Radaković 85'", 'vencedor': ''},
            {'fase': 'Semifinal', 'grupo': '', 'data': '13 de junho', 'time1': 'Tchecoslováquia', 'placar': '3 - 1', 'time2': 'Iugoslávia', 'estadio': 'Viña del Mar, Estádio Sausalito', 'gols': 4, 'detalhes': '', 'marcadores': "Tchecoslováquia: Kadraba 48' Scherer 80', 84' (pen) | Iugoslávia: Jerković 69'", 'vencedor': ''},
            {'fase': 'Semifinal', 'grupo': '', 'data': '13 de junho', 'time1': 'Brasil', 'placar': '4 - 2', 'time2': 'Chile', 'estadio': 'Santiago - (Ñuñoa), Estádio Nacional de Chile', 'gols': 6, 'detalhes': '', 'marcadores': "Brasil: Garrincha 9', 32' Vavá 47', 78' | Chile: Toro 42' Sánchez 61'(pen)", 'vencedor': ''},
            {'fase': 'Terceiro lugar', 'grupo': '', 'data': '16 de junho', 'time1': 'Chile', 'placar': '1 - 0', 'time2': 'Iugoslávia', 'estadio': 'Santiago - (Ñuñoa), Estádio Nacional de Chile', 'gols': 1, 'detalhes': '', 'marcadores': "Chile: Rojas 90'", 'vencedor': ''},
            {'fase': 'Final', 'grupo': '', 'data': '17 de junho', 'time1': 'Brasil', 'placar': '3 - 1', 'time2': 'Tchecoslováquia', 'estadio': 'Estádio Nacional de Chile, Santiago', 'gols': 4, 'detalhes': '', 'marcadores': "Brasil: Amarildo 17' Zito 69' Vavá 78' | Tchecoslováquia: Masopust 15'", 'vencedor': ''},
        ]
        return groups_1962, matches_1962
    if year == 1966:
        groups_1966 = [
            {'grupo': 'Grupo A', 'pos': 1, 'selecao': 'Inglaterra', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 4, 'gc': 0, 'sg': '+4', 'classificado': 'sim'},
            {'grupo': 'Grupo A', 'pos': 2, 'selecao': 'Uruguai', 'pts': 4, 'j': 3, 'v': 1, 'e': 2, 'd': 0, 'gp': 2, 'gc': 1, 'sg': '+1', 'classificado': 'sim'},
            {'grupo': 'Grupo A', 'pos': 3, 'selecao': 'México', 'pts': 2, 'j': 3, 'v': 0, 'e': 2, 'd': 1, 'gp': 1, 'gc': 3, 'sg': '-2', 'classificado': 'eliminado'},
            {'grupo': 'Grupo A', 'pos': 4, 'selecao': 'França', 'pts': 1, 'j': 3, 'v': 0, 'e': 1, 'd': 2, 'gp': 2, 'gc': 5, 'sg': '-3', 'classificado': 'eliminado'},
            {'grupo': 'Grupo B', 'pos': 1, 'selecao': 'Alemanha', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 7, 'gc': 1, 'sg': '+6', 'classificado': 'sim'},
            {'grupo': 'Grupo B', 'pos': 2, 'selecao': 'Argentina', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 4, 'gc': 1, 'sg': '+3', 'classificado': 'sim'},
            {'grupo': 'Grupo B', 'pos': 3, 'selecao': 'Espanha', 'pts': 2, 'j': 3, 'v': 1, 'e': 0, 'd': 2, 'gp': 4, 'gc': 5, 'sg': '-1', 'classificado': 'eliminado'},
            {'grupo': 'Grupo B', 'pos': 4, 'selecao': 'Suíça', 'pts': 0, 'j': 3, 'v': 0, 'e': 0, 'd': 3, 'gp': 1, 'gc': 9, 'sg': '-8', 'classificado': 'eliminado'},
            {'grupo': 'Grupo C', 'pos': 1, 'selecao': 'Portugal', 'pts': 6, 'j': 3, 'v': 3, 'e': 0, 'd': 0, 'gp': 9, 'gc': 2, 'sg': '+7', 'classificado': 'sim'},
            {'grupo': 'Grupo C', 'pos': 2, 'selecao': 'Hungria', 'pts': 4, 'j': 3, 'v': 2, 'e': 0, 'd': 1, 'gp': 7, 'gc': 5, 'sg': '+2', 'classificado': 'sim'},
            {'grupo': 'Grupo C', 'pos': 3, 'selecao': 'Brasil', 'pts': 2, 'j': 3, 'v': 1, 'e': 0, 'd': 2, 'gp': 4, 'gc': 6, 'sg': '-2', 'classificado': 'eliminado'},
            {'grupo': 'Grupo C', 'pos': 4, 'selecao': 'Bulgária', 'pts': 0, 'j': 3, 'v': 0, 'e': 0, 'd': 3, 'gp': 1, 'gc': 8, 'sg': '-7', 'classificado': 'eliminado'},
            {'grupo': 'Grupo D', 'pos': 1, 'selecao': 'União Soviética', 'pts': 6, 'j': 3, 'v': 3, 'e': 0, 'd': 0, 'gp': 6, 'gc': 1, 'sg': '+5', 'classificado': 'sim'},
            {'grupo': 'Grupo D', 'pos': 2, 'selecao': 'Coreia do Norte', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 2, 'gc': 4, 'sg': '-2', 'classificado': 'sim'},
            {'grupo': 'Grupo D', 'pos': 3, 'selecao': 'Itália', 'pts': 2, 'j': 3, 'v': 1, 'e': 0, 'd': 2, 'gp': 2, 'gc': 2, 'sg': '0', 'classificado': 'eliminado'},
            {'grupo': 'Grupo D', 'pos': 4, 'selecao': 'Chile', 'pts': 1, 'j': 3, 'v': 0, 'e': 1, 'd': 2, 'gp': 2, 'gc': 5, 'sg': '-3', 'classificado': 'eliminado'},
        ]
        matches_1966 = [
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '11 de julho', 'time1': 'Inglaterra', 'placar': '0 - 0', 'time2': 'Uruguai', 'estadio': 'Estádio de Wembley, Londres', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '13 de julho', 'time1': 'França', 'placar': '1 - 1', 'time2': 'México', 'estadio': 'Estádio de Wembley, Londres', 'gols': 2, 'detalhes': '', 'marcadores': "França: Hausser 62' | México: Borja 48'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '15 de julho', 'time1': 'Uruguai', 'placar': '2 - 1', 'time2': 'França', 'estadio': 'White City, Londres', 'gols': 3, 'detalhes': '', 'marcadores': "Uruguai: Rocha 26' Cortés 31' | França: De Bourgoing 15' (pen.)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '16 de julho', 'time1': 'Inglaterra', 'placar': '2 - 0', 'time2': 'México', 'estadio': 'Estádio de Wembley, Londres', 'gols': 2, 'detalhes': '', 'marcadores': "Inglaterra: Charlton 37' Hunt 75'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '19 de julho', 'time1': 'México', 'placar': '0 - 0', 'time2': 'Uruguai', 'estadio': 'Estádio de Wembley, Londres', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '20 de julho', 'time1': 'Inglaterra', 'placar': '2 - 0', 'time2': 'França', 'estadio': 'Estádio de Wembley, Londres', 'gols': 2, 'detalhes': '', 'marcadores': "Inglaterra: Hunt 38', 75'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '12 de julho', 'time1': 'Alemanha', 'placar': '5 - 0', 'time2': 'Suíça', 'estadio': 'Hillsborough, Sheffield', 'gols': 5, 'detalhes': '', 'marcadores': "Alemanha: Held 15' Haller 20', 77' (pen.) Beckenbauer 39', 52'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '13 de julho', 'time1': 'Argentina', 'placar': '2 - 1', 'time2': 'Espanha', 'estadio': 'Villa Park, Birmingham', 'gols': 3, 'detalhes': '', 'marcadores': "Argentina: Artime 65', 79' | Espanha: Pirri 71'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '15 de julho', 'time1': 'Espanha', 'placar': '2 - 1', 'time2': 'Suíça', 'estadio': 'Hillsborough, Sheffield', 'gols': 3, 'detalhes': '', 'marcadores': "Espanha: Sanchís 57' Amancio 75' | Suíça: Quentin 28'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '16 de julho', 'time1': 'Alemanha', 'placar': '0 - 0', 'time2': 'Argentina', 'estadio': 'Villa Park, Birmingham', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '19 de julho', 'time1': 'Argentina', 'placar': '2 - 0', 'time2': 'Suíça', 'estadio': 'Hillsborough, Sheffield', 'gols': 2, 'detalhes': '', 'marcadores': "Argentina: Artime 53' Onega 81'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '20 de julho', 'time1': 'Alemanha', 'placar': '2 - 1', 'time2': 'Espanha', 'estadio': 'Villa Park, Birmingham', 'gols': 3, 'detalhes': '', 'marcadores': "Alemanha: Emmerich 38' Seeler 84' | Espanha: Fusté 22'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '12 de julho', 'time1': 'Brasil', 'placar': '2 - 0', 'time2': 'Bulgária', 'estadio': 'Goodison Park, Liverpool', 'gols': 2, 'detalhes': '', 'marcadores': "Brasil: Pelé 15' Garrincha 63'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '13 de julho', 'time1': 'Portugal', 'placar': '3 - 1', 'time2': 'Hungria', 'estadio': 'Old Trafford, Manchester', 'gols': 4, 'detalhes': '', 'marcadores': "Portugal: José Augusto 2', 67' José Torres 90' | Hungria: Bene 60'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '15 de julho', 'time1': 'Hungria', 'placar': '3 - 1', 'time2': 'Brasil', 'estadio': 'Goodison Park, Liverpool', 'gols': 4, 'detalhes': '', 'marcadores': "Hungria: Bene 2' Farkas 64' Mészöly 73' (pen.) | Brasil: Tostão 14'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '16 de julho', 'time1': 'Portugal', 'placar': '3 - 0', 'time2': 'Bulgária', 'estadio': 'Old Trafford, Manchester', 'gols': 3, 'detalhes': '', 'marcadores': "Portugal: Vutsov 17' (g.c.) Eusébio 38' José Torres 81'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '19 de julho', 'time1': 'Portugal', 'placar': '3 - 1', 'time2': 'Brasil', 'estadio': 'Goodison Park, Liverpool', 'gols': 4, 'detalhes': '', 'marcadores': "Portugal: António Simões 15' Eusébio 27', 85' | Brasil: Rildo 73'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '20 de julho', 'time1': 'Hungria', 'placar': '3 - 1', 'time2': 'Bulgária', 'estadio': 'Old Trafford, Manchester', 'gols': 4, 'detalhes': '', 'marcadores': "Hungria: Davidov 43' (g.c.) Mészöly 45' Bene 54' | Bulgária: Asparuhov 15'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '12 de julho', 'time1': 'União Soviética', 'placar': '3 - 0', 'time2': 'Coreia do Norte', 'estadio': 'Ayresome Park, Middlesbrough', 'gols': 3, 'detalhes': '', 'marcadores': "União Soviética: Malafeyew 31', 88' Banişevski 33'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '13 de julho', 'time1': 'Itália', 'placar': '2 - 0', 'time2': 'Chile', 'estadio': 'Roker Park, Sunderland', 'gols': 2, 'detalhes': '', 'marcadores': "Itália: Mazzola 8' Barison 88'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '15 de julho', 'time1': 'Chile', 'placar': '1 - 1', 'time2': 'Coreia do Norte', 'estadio': 'Ayresome Park, Middlesbrough', 'gols': 2, 'detalhes': '', 'marcadores': "Chile: Marcos 26' (pen.) | Coreia do Norte: Pak Seung-zin 88'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '16 de julho', 'time1': 'União Soviética', 'placar': '1 - 0', 'time2': 'Itália', 'estadio': 'Roker Park, Sunderland', 'gols': 1, 'detalhes': '', 'marcadores': "União Soviética: Chislenko 57'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '19 de julho', 'time1': 'Itália', 'placar': '0 - 1', 'time2': 'Coreia do Norte', 'estadio': 'Ayresome Park, Middlesbrough', 'gols': 1, 'detalhes': '', 'marcadores': "Coreia do Norte: Pak Doo-ik 42'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '20 de julho', 'time1': 'União Soviética', 'placar': '2 - 1', 'time2': 'Chile', 'estadio': 'Roker Park, Sunderland', 'gols': 3, 'detalhes': '', 'marcadores': "União Soviética: Porkuyan 28', 85' | Chile: Marcos 32'", 'vencedor': ''},
            {'fase': 'Quartas de final', 'grupo': '', 'data': '23 de julho', 'time1': 'Inglaterra', 'placar': '1 - 0', 'time2': 'Argentina', 'estadio': 'Estádio de Wembley, Londres', 'gols': 1, 'detalhes': '', 'marcadores': "Inglaterra: Hurst 78'", 'vencedor': ''},
            {'fase': 'Quartas de final', 'grupo': '', 'data': '23 de julho', 'time1': 'Alemanha', 'placar': '4 - 0', 'time2': 'Uruguai', 'estadio': 'Hillsborough, Sheffield', 'gols': 4, 'detalhes': '', 'marcadores': "Alemanha: Haller 11', 83' Beckenbauer 70' Seeler 75'", 'vencedor': ''},
            {'fase': 'Quartas de final', 'grupo': '', 'data': '23 de julho', 'time1': 'União Soviética', 'placar': '2 - 1', 'time2': 'Hungria', 'estadio': 'Roker Park Ground, Sunderland', 'gols': 3, 'detalhes': '', 'marcadores': "União Soviética: Chislenko 5' Porkuyan 46' | Hungria: Bene 57'", 'vencedor': ''},
            {'fase': 'Quartas de final', 'grupo': '', 'data': '23 de julho', 'time1': 'Portugal', 'placar': '5 - 3', 'time2': 'Coreia do Norte', 'estadio': 'Goodison Park, Liverpool', 'gols': 8, 'detalhes': '', 'marcadores': "Portugal: Eusébio 27', 43' (pen.), 56', 59' (pen.) José Augusto 80' | Coreia do Norte: Pak 1' Li 22' Yang 25'", 'vencedor': ''},
            {'fase': 'Semifinal', 'grupo': '', 'data': '25 de julho', 'time1': 'Alemanha', 'placar': '2 - 1', 'time2': 'União Soviética', 'estadio': 'Goodison Park, Liverpool', 'gols': 3, 'detalhes': '', 'marcadores': "Alemanha: Haller 43' Beckenbauer 67' | União Soviética: Porkuyan 88'", 'vencedor': ''},
            {'fase': 'Semifinal', 'grupo': '', 'data': '26 de julho', 'time1': 'Inglaterra', 'placar': '2 - 1', 'time2': 'Portugal', 'estadio': 'Estádio de Wembley, Londres', 'gols': 3, 'detalhes': '', 'marcadores': "Inglaterra: Charlton 30', 80' | Portugal: Eusébio 82' (pen.)", 'vencedor': ''},
            {'fase': 'Terceiro lugar', 'grupo': '', 'data': '28 de julho', 'time1': 'Portugal', 'placar': '2 - 1', 'time2': 'União Soviética', 'estadio': 'Estádio de Wembley, Londres', 'gols': 3, 'detalhes': '', 'marcadores': "Portugal: Eusébio 12' (pen.) José Torres 89' | União Soviética: Malofeyev 43'", 'vencedor': ''},
            {'fase': 'Final', 'grupo': '', 'data': '30 de julho', 'time1': 'Inglaterra', 'placar': '4 - 2 (pro.)', 'time2': 'Alemanha', 'estadio': 'Estádio de Wembley, Londres', 'gols': 6, 'detalhes': '', 'marcadores': "Inglaterra: Hurst 18', 101', 120' Peters 78' | Alemanha: Haller 12' Weber 89'", 'vencedor': ''},
        ]
        return groups_1966, matches_1966
    if year == 1970:
        groups_1970 = [
            {'grupo': 'Grupo A', 'pos': 1, 'selecao': 'União Soviética', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 6, 'gc': 1, 'sg': '+5', 'classificado': 'sim'},
            {'grupo': 'Grupo A', 'pos': 2, 'selecao': 'México', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 5, 'gc': 0, 'sg': '+5', 'classificado': 'sim'},
            {'grupo': 'Grupo A', 'pos': 3, 'selecao': 'Bélgica', 'pts': 2, 'j': 3, 'v': 1, 'e': 0, 'd': 2, 'gp': 4, 'gc': 5, 'sg': '-1', 'classificado': 'eliminado'},
            {'grupo': 'Grupo A', 'pos': 4, 'selecao': 'El Salvador', 'pts': 0, 'j': 3, 'v': 0, 'e': 0, 'd': 3, 'gp': 0, 'gc': 9, 'sg': '-9', 'classificado': 'eliminado'},
            {'grupo': 'Grupo B', 'pos': 1, 'selecao': 'Itália', 'pts': 4, 'j': 3, 'v': 1, 'e': 2, 'd': 0, 'gp': 1, 'gc': 0, 'sg': '+1', 'classificado': 'sim'},
            {'grupo': 'Grupo B', 'pos': 2, 'selecao': 'Uruguai', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 2, 'gc': 1, 'sg': '+1', 'classificado': 'sim'},
            {'grupo': 'Grupo B', 'pos': 3, 'selecao': 'Suécia', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 2, 'gc': 2, 'sg': '0', 'classificado': 'eliminado'},
            {'grupo': 'Grupo B', 'pos': 4, 'selecao': 'Israel', 'pts': 2, 'j': 3, 'v': 0, 'e': 2, 'd': 1, 'gp': 1, 'gc': 3, 'sg': '-2', 'classificado': 'eliminado'},
            {'grupo': 'Grupo C', 'pos': 1, 'selecao': 'Brasil', 'pts': 6, 'j': 3, 'v': 3, 'e': 0, 'd': 0, 'gp': 8, 'gc': 3, 'sg': '+5', 'classificado': 'sim'},
            {'grupo': 'Grupo C', 'pos': 2, 'selecao': 'Inglaterra', 'pts': 4, 'j': 3, 'v': 2, 'e': 0, 'd': 1, 'gp': 2, 'gc': 1, 'sg': '+1', 'classificado': 'sim'},
            {'grupo': 'Grupo C', 'pos': 3, 'selecao': 'Romênia', 'pts': 2, 'j': 3, 'v': 1, 'e': 0, 'd': 2, 'gp': 4, 'gc': 5, 'sg': '-1', 'classificado': 'eliminado'},
            {'grupo': 'Grupo C', 'pos': 4, 'selecao': 'Tchecoslováquia', 'pts': 0, 'j': 3, 'v': 0, 'e': 0, 'd': 3, 'gp': 2, 'gc': 7, 'sg': '-5', 'classificado': 'eliminado'},
            {'grupo': 'Grupo D', 'pos': 1, 'selecao': 'Alemanha', 'pts': 6, 'j': 3, 'v': 3, 'e': 0, 'd': 0, 'gp': 10, 'gc': 4, 'sg': '+6', 'classificado': 'sim'},
            {'grupo': 'Grupo D', 'pos': 2, 'selecao': 'Peru', 'pts': 4, 'j': 3, 'v': 2, 'e': 0, 'd': 1, 'gp': 7, 'gc': 5, 'sg': '+2', 'classificado': 'sim'},
            {'grupo': 'Grupo D', 'pos': 3, 'selecao': 'Bulgária', 'pts': 1, 'j': 3, 'v': 0, 'e': 1, 'd': 2, 'gp': 5, 'gc': 9, 'sg': '-4', 'classificado': 'eliminado'},
            {'grupo': 'Grupo D', 'pos': 4, 'selecao': 'Marrocos', 'pts': 1, 'j': 3, 'v': 0, 'e': 1, 'd': 2, 'gp': 2, 'gc': 6, 'sg': '-4', 'classificado': 'eliminado'},
        ]
        matches_1970 = [
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '31 de maio', 'time1': 'México', 'placar': '0 - 0', 'time2': 'União Soviética', 'estadio': 'Estádio Azteca, Cidade do México', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '3 de junho', 'time1': 'Bélgica', 'placar': '3 - 0', 'time2': 'El Salvador', 'estadio': 'Estádio Azteca, Cidade do México', 'gols': 3, 'detalhes': '', 'marcadores': "Bélgica: Van Moer 12', 54' Lambert 79' (pen)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '6 de junho', 'time1': 'União Soviética', 'placar': '4 - 1', 'time2': 'Bélgica', 'estadio': 'Estádio Azteca, Cidade do México', 'gols': 5, 'detalhes': '', 'marcadores': "União Soviética: Byshovets 14', 63' Asatiani 57' Khmelnytskyi 76' | Bélgica: Lambert 86'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '7 de junho', 'time1': 'México', 'placar': '4 - 0', 'time2': 'El Salvador', 'estadio': 'Estádio Azteca, Cidade do México', 'gols': 4, 'detalhes': '', 'marcadores': "México: Valdivia 45' Fragoso 58' Basaguren 83'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '10 de junho', 'time1': 'União Soviética', 'placar': '2 - 0', 'time2': 'El Salvador', 'estadio': 'Estádio Azteca, Cidade do México', 'gols': 2, 'detalhes': '', 'marcadores': "União Soviética: Byshovets 51', 74'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo A', 'data': '11 de junho', 'time1': 'México', 'placar': '1 - 0', 'time2': 'Bélgica', 'estadio': 'Estádio Azteca, Cidade do México', 'gols': 1, 'detalhes': '', 'marcadores': "México: Peña 14' (pen)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '2 de junho', 'time1': 'Uruguai', 'placar': '2 - 0', 'time2': 'Israel', 'estadio': 'Estádio Cuauhtémoc, Puebla', 'gols': 2, 'detalhes': '', 'marcadores': "Uruguai: Maneiro 23' Mujica 81'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '3 de junho', 'time1': 'Itália', 'placar': '1 - 0', 'time2': 'Suécia', 'estadio': 'Luis Dosal, Toluca', 'gols': 1, 'detalhes': '', 'marcadores': "Itália: Domenghini 11'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '6 de junho', 'time1': 'Uruguai', 'placar': '0 - 0', 'time2': 'Itália', 'estadio': 'Estádio Cuauhtémoc, Puebla', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '7 de junho', 'time1': 'Israel', 'placar': '1 - 1', 'time2': 'Suécia', 'estadio': 'Luis Dosal, Toluca', 'gols': 2, 'detalhes': '', 'marcadores': "Israel: Spiegler 56' | Suécia: Turesson 53'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '10 de junho', 'time1': 'Suécia', 'placar': '1 - 0', 'time2': 'Uruguai', 'estadio': 'Estádio Cuauhtémoc, Puebla', 'gols': 1, 'detalhes': '', 'marcadores': "Suécia: Grahn 90'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo B', 'data': '11 de junho', 'time1': 'Itália', 'placar': '0 - 0', 'time2': 'Israel', 'estadio': 'Luis Dosal, Toluca', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '2 de junho', 'time1': 'Inglaterra', 'placar': '1 - 0', 'time2': 'Romênia', 'estadio': 'Jalisco, Guadalajara', 'gols': 1, 'detalhes': '', 'marcadores': "Inglaterra: Hurst 65'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '3 de junho', 'time1': 'Brasil', 'placar': '4 - 1', 'time2': 'Tchecoslováquia', 'estadio': 'Jalisco, Guadalajara', 'gols': 5, 'detalhes': '', 'marcadores': "Brasil: Rivelino 24' Pelé 59' Jairzinho 61', 83' | Tchecoslováquia: Petráš 11'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '6 de junho', 'time1': 'Romênia', 'placar': '2 - 1', 'time2': 'Tchecoslováquia', 'estadio': 'Jalisco, Guadalajara', 'gols': 3, 'detalhes': '', 'marcadores': "Romênia: Neagu 52' Dumitrache 75' (pen) | Tchecoslováquia: Petráš 5'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '7 de junho', 'time1': 'Brasil', 'placar': '1 - 0', 'time2': 'Inglaterra', 'estadio': 'Jalisco, Guadalajara', 'gols': 1, 'detalhes': '', 'marcadores': "Brasil: Jairzinho 59'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '10 de junho', 'time1': 'Brasil', 'placar': '3 - 2', 'time2': 'Romênia', 'estadio': 'Jalisco, Guadalajara', 'gols': 5, 'detalhes': '', 'marcadores': "Brasil: Pelé 19', 67' Jairzinho 22' | Romênia: Dumitrache 34' Dembrovschi 84'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo C', 'data': '11 de junho', 'time1': 'Inglaterra', 'placar': '1 - 0', 'time2': 'Tchecoslováquia', 'estadio': 'Jalisco, Guadalajara', 'gols': 1, 'detalhes': '', 'marcadores': "Inglaterra: Clarke 50' (pen)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '2 de junho', 'time1': 'Peru', 'placar': '3 - 2', 'time2': 'Bulgária', 'estadio': 'Estádio Nou Camp, León', 'gols': 5, 'detalhes': '', 'marcadores': "Peru: Gallardo 51' Chumpitaz 55' Cubillas 73' | Bulgária: Dermendzhiev 12' Bonev 50'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '3 de junho', 'time1': 'Alemanha', 'placar': '2 - 1', 'time2': 'Marrocos', 'estadio': 'Estádio Nou Camp, León', 'gols': 3, 'detalhes': '', 'marcadores': "Alemanha: Seeler 55' Müller 80' | Marrocos: Houmane 20'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '6 de junho', 'time1': 'Peru', 'placar': '3 - 0', 'time2': 'Marrocos', 'estadio': 'Estádio Nou Camp, León', 'gols': 3, 'detalhes': '', 'marcadores': "Peru: Cubillas 65', 75' Challe 68'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '7 de junho', 'time1': 'Alemanha', 'placar': '5 - 2', 'time2': 'Bulgária', 'estadio': 'Estádio Nou Camp, León', 'gols': 7, 'detalhes': '', 'marcadores': "Alemanha: Libuda 20' Müller 28', 52' (pen.), 87' Seeler 68' | Bulgária: Nikodimov 12' Kolev 88'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '10 de junho', 'time1': 'Alemanha', 'placar': '3 - 1', 'time2': 'Peru', 'estadio': 'Estádio Nou Camp, León', 'gols': 4, 'detalhes': '', 'marcadores': "Alemanha: Müller 20', 25', 39' | Peru: Cubillas 44'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo D', 'data': '11 de junho', 'time1': 'Marrocos', 'placar': '1 - 1', 'time2': 'Bulgária', 'estadio': 'Estádio Nou Camp, León', 'gols': 2, 'detalhes': '', 'marcadores': "Marrocos: Ghazouani 60' | Bulgária: Zhechev 40'", 'vencedor': ''},
            {'fase': 'Quartas de final', 'grupo': '', 'data': '14 de junho', 'time1': 'Itália', 'placar': '4 - 1', 'time2': 'México', 'estadio': 'Luis Dosal, Toluca', 'gols': 5, 'detalhes': '', 'marcadores': "Itália: Guzmán 25' Riva 63', 76' Rivera 70' | México: González 13'", 'vencedor': ''},
            {'fase': 'Quartas de final', 'grupo': '', 'data': '14 de junho', 'time1': 'Alemanha', 'placar': '3 - 2 (pro)', 'time2': 'Inglaterra', 'estadio': 'Nou Camp, León', 'gols': 5, 'detalhes': '', 'marcadores': "Alemanha: Beckenbauer 68' Seeler 82' Müller 108' | Inglaterra: Mullery 31' Peters 49'", 'vencedor': ''},
            {'fase': 'Quartas de final', 'grupo': '', 'data': '14 de junho', 'time1': 'Brasil', 'placar': '4 - 2', 'time2': 'Peru', 'estadio': 'Jalisco, Guadalajara', 'gols': 6, 'detalhes': '', 'marcadores': "Brasil: Rivellino 11' Tostão 15', 52' Jairzinho 75' | Peru: Gallardo 28' Cubillas 70'", 'vencedor': ''},
            {'fase': 'Quartas de final', 'grupo': '', 'data': '14 de junho', 'time1': 'União Soviética', 'placar': '0 - 1 (pro)', 'time2': 'Uruguai', 'estadio': 'Estádio Azteca, Cidade do México', 'gols': 1, 'detalhes': '', 'marcadores': "Uruguai: Espárrago 117'", 'vencedor': ''},
            {'fase': 'Semifinal', 'grupo': '', 'data': '17 de junho', 'time1': 'Uruguai', 'placar': '1 - 3', 'time2': 'Brasil', 'estadio': 'Jalisco, Guadalajara', 'gols': 4, 'detalhes': '', 'marcadores': "Uruguai: Cubilla 19' | Brasil: Clodoaldo 44' Jairzinho 76' Rivellino 89'", 'vencedor': ''},
            {'fase': 'Semifinal', 'grupo': '', 'data': '17 de junho', 'time1': 'Itália', 'placar': '4 - 3 (pro)', 'time2': 'Alemanha', 'estadio': 'Estádio Azteca, Cidade do México', 'gols': 7, 'detalhes': '', 'marcadores': "Itália: Boninsegna 8' Burgnich 98' Riva 104' Rivera 111' | Alemanha: Schnellinger 90' Müller 94', 110'", 'vencedor': ''},
            {'fase': 'Terceiro lugar', 'grupo': '', 'data': '20 de junho', 'time1': 'Uruguai', 'placar': '0 - 1', 'time2': 'Alemanha', 'estadio': 'Estádio Azteca, Cidade do México', 'gols': 1, 'detalhes': '', 'marcadores': "Alemanha: Overath 26'", 'vencedor': ''},
            {'fase': 'Final', 'grupo': '', 'data': '21 de junho', 'time1': 'Brasil', 'placar': '4 - 1', 'time2': 'Itália', 'estadio': 'Estádio Azteca, Cidade do México', 'gols': 5, 'detalhes': '', 'marcadores': "Brasil: Pelé 18' Gérson 66' Jairzinho 71' Carlos Alberto 86' | Itália: Boninsegna 37'", 'vencedor': ''},
        ]
        return groups_1970, matches_1970
    if year == 1974:
        groups_1974 = [
            {'grupo': 'Grupo 1', 'pos': 1, 'selecao': 'Alemanha Oriental', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 4, 'gc': 1, 'sg': '+3', 'classificado': 'sim'},
            {'grupo': 'Grupo 1', 'pos': 2, 'selecao': 'Alemanha', 'pts': 4, 'j': 3, 'v': 2, 'e': 0, 'd': 1, 'gp': 4, 'gc': 1, 'sg': '+3', 'classificado': 'sim'},
            {'grupo': 'Grupo 1', 'pos': 3, 'selecao': 'Chile', 'pts': 2, 'j': 3, 'v': 0, 'e': 2, 'd': 1, 'gp': 1, 'gc': 2, 'sg': '-1', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 1', 'pos': 4, 'selecao': 'Austrália', 'pts': 1, 'j': 3, 'v': 0, 'e': 1, 'd': 2, 'gp': 0, 'gc': 5, 'sg': '-5', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 2', 'pos': 1, 'selecao': 'Iugoslávia', 'pts': 4, 'j': 3, 'v': 1, 'e': 2, 'd': 0, 'gp': 10, 'gc': 1, 'sg': '+9', 'classificado': 'sim'},
            {'grupo': 'Grupo 2', 'pos': 2, 'selecao': 'Brasil', 'pts': 4, 'j': 3, 'v': 1, 'e': 2, 'd': 0, 'gp': 3, 'gc': 0, 'sg': '+3', 'classificado': 'sim'},
            {'grupo': 'Grupo 2', 'pos': 3, 'selecao': 'Escócia', 'pts': 4, 'j': 3, 'v': 1, 'e': 2, 'd': 0, 'gp': 3, 'gc': 1, 'sg': '+2', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 2', 'pos': 4, 'selecao': 'República Democrática do Congo', 'pts': 0, 'j': 3, 'v': 0, 'e': 0, 'd': 3, 'gp': 0, 'gc': 14, 'sg': '-14', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 3', 'pos': 1, 'selecao': 'Países Baixos', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 6, 'gc': 1, 'sg': '+5', 'classificado': 'sim'},
            {'grupo': 'Grupo 3', 'pos': 2, 'selecao': 'Suécia', 'pts': 4, 'j': 3, 'v': 1, 'e': 2, 'd': 0, 'gp': 3, 'gc': 0, 'sg': '+3', 'classificado': 'sim'},
            {'grupo': 'Grupo 3', 'pos': 3, 'selecao': 'Bulgária', 'pts': 2, 'j': 3, 'v': 0, 'e': 2, 'd': 1, 'gp': 2, 'gc': 5, 'sg': '-3', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 3', 'pos': 4, 'selecao': 'Uruguai', 'pts': 1, 'j': 3, 'v': 0, 'e': 1, 'd': 2, 'gp': 1, 'gc': 6, 'sg': '-5', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 4', 'pos': 1, 'selecao': 'Polônia', 'pts': 6, 'j': 3, 'v': 3, 'e': 0, 'd': 0, 'gp': 12, 'gc': 3, 'sg': '+9', 'classificado': 'sim'},
            {'grupo': 'Grupo 4', 'pos': 2, 'selecao': 'Argentina', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 7, 'gc': 5, 'sg': '+2', 'classificado': 'sim'},
            {'grupo': 'Grupo 4', 'pos': 3, 'selecao': 'Itália', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 5, 'gc': 4, 'sg': '+1', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 4', 'pos': 4, 'selecao': 'Haiti', 'pts': 0, 'j': 3, 'v': 0, 'e': 0, 'd': 3, 'gp': 2, 'gc': 14, 'sg': '-12', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo A', 'pos': 1, 'selecao': 'Países Baixos', 'pts': 6, 'j': 3, 'v': 3, 'e': 0, 'd': 0, 'gp': 8, 'gc': 0, 'sg': '+8', 'classificado': 'sim'},
            {'grupo': '2ª Fase - Grupo A', 'pos': 2, 'selecao': 'Brasil', 'pts': 4, 'j': 3, 'v': 2, 'e': 0, 'd': 1, 'gp': 3, 'gc': 3, 'sg': '0', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo A', 'pos': 3, 'selecao': 'Alemanha Oriental', 'pts': 1, 'j': 3, 'v': 0, 'e': 1, 'd': 2, 'gp': 1, 'gc': 4, 'sg': '-3', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo A', 'pos': 4, 'selecao': 'Argentina', 'pts': 1, 'j': 3, 'v': 0, 'e': 1, 'd': 2, 'gp': 2, 'gc': 7, 'sg': '-5', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo B', 'pos': 1, 'selecao': 'Alemanha', 'pts': 6, 'j': 3, 'v': 3, 'e': 0, 'd': 0, 'gp': 7, 'gc': 2, 'sg': '+5', 'classificado': 'sim'},
            {'grupo': '2ª Fase - Grupo B', 'pos': 2, 'selecao': 'Polônia', 'pts': 4, 'j': 3, 'v': 2, 'e': 0, 'd': 1, 'gp': 3, 'gc': 2, 'sg': '+1', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo B', 'pos': 3, 'selecao': 'Suécia', 'pts': 2, 'j': 3, 'v': 1, 'e': 0, 'd': 2, 'gp': 4, 'gc': 6, 'sg': '-2', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo B', 'pos': 4, 'selecao': 'Iugoslávia', 'pts': 0, 'j': 3, 'v': 0, 'e': 0, 'd': 3, 'gp': 2, 'gc': 6, 'sg': '-4', 'classificado': 'eliminado'},
        ]
        matches_1974 = [
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '14 de junho', 'time1': 'Alemanha', 'placar': '1 - 0', 'time2': 'Chile', 'estadio': 'Olympiastadion, Berlim Ocidental', 'gols': 1, 'detalhes': '', 'marcadores': "Alemanha: Breitner 18'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '14 de junho', 'time1': 'Alemanha Oriental', 'placar': '2 - 0', 'time2': 'Austrália', 'estadio': 'Volksparkstadion, Hamburgo', 'gols': 2, 'detalhes': '', 'marcadores': "Alemanha Oriental: Curran 58' (g.c.) Streich 72'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '18 de junho', 'time1': 'Austrália', 'placar': '0 - 3', 'time2': 'Alemanha', 'estadio': 'Volksparkstadion, Hamburgo', 'gols': 3, 'detalhes': '', 'marcadores': "Alemanha: Overath 12' Cullmann 34' Müller 53'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '18 de junho', 'time1': 'Chile', 'placar': '1 - 1', 'time2': 'Alemanha Oriental', 'estadio': 'Olympiastadion, Berlim Ocidental', 'gols': 2, 'detalhes': '', 'marcadores': "Chile: Ahumada 69' | Alemanha Oriental: Hoffman 55'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '22 de junho', 'time1': 'Austrália', 'placar': '0 - 0', 'time2': 'Chile', 'estadio': 'Olympiastadion, Berlim Ocidental', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '22 de junho', 'time1': 'Alemanha Oriental', 'placar': '1 - 0', 'time2': 'Alemanha', 'estadio': 'Volksparkstadion, Hamburgo', 'gols': 1, 'detalhes': '', 'marcadores': "Alemanha Oriental: Sparwasser 77'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '13 de junho', 'time1': 'Brasil', 'placar': '0 - 0', 'time2': 'Iugoslávia', 'estadio': 'Waldstadion, Frankfurt', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '14 de junho', 'time1': 'República Democrática do Congo', 'placar': '0 - 2', 'time2': 'Escócia', 'estadio': 'Westfalenstadion, Dortmund', 'gols': 2, 'detalhes': '', 'marcadores': "Escócia: Lorimer 26' Jordan 34'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '18 de junho', 'time1': 'Iugoslávia', 'placar': '9 - 0', 'time2': 'República Democrática do Congo', 'estadio': 'Parkstadion, Gelsenkirchen', 'gols': 9, 'detalhes': '', 'marcadores': "Iugoslávia: Bajević 8', 30', 81' Džajić 14' Šurjak 18' Katalinski 22' Bogićević 35' Oblak 61' Petković 65'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '18 de junho', 'time1': 'Escócia', 'placar': '0 - 0', 'time2': 'Brasil', 'estadio': 'Waldstadion, Frankfurt', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '22 de junho', 'time1': 'Escócia', 'placar': '1 - 1', 'time2': 'Iugoslávia', 'estadio': 'Waldstadion, Frankfurt', 'gols': 2, 'detalhes': '', 'marcadores': "Escócia: Jordan 88' | Iugoslávia: Karasi 81'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '22 de junho', 'time1': 'República Democrática do Congo', 'placar': '0 - 3', 'time2': 'Brasil', 'estadio': 'Parkstadion, Gelsenkirchen', 'gols': 3, 'detalhes': '', 'marcadores': "Brasil: Jairzinho 12' Rivelino 66' Valdomiro 79'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '15 de junho', 'time1': 'Uruguai', 'placar': '0 - 2', 'time2': 'Países Baixos', 'estadio': 'Niedersachsenstadion, Hanôver', 'gols': 2, 'detalhes': '', 'marcadores': "Países Baixos: Rep 16', 86'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '15 de junho', 'time1': 'Suécia', 'placar': '0 - 0', 'time2': 'Bulgária', 'estadio': 'Rheinstadion, Düsseldorf', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '19 de junho', 'time1': 'Uruguai', 'placar': '1 - 1', 'time2': 'Bulgária', 'estadio': 'Niedersachsenstadion, Hanôver', 'gols': 2, 'detalhes': '', 'marcadores': "Uruguai: Pavoni 87' | Bulgária: Bonev 75'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '19 de junho', 'time1': 'Países Baixos', 'placar': '0 - 0', 'time2': 'Suécia', 'estadio': 'Westfalenstadion, Dortmund', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '23 de junho', 'time1': 'Bulgária', 'placar': '1 - 4', 'time2': 'Países Baixos', 'estadio': 'Westfalenstadion, Dortmund', 'gols': 5, 'detalhes': '', 'marcadores': "Bulgária: Krol 78' (g.c.) | Países Baixos: Neeskens 5' (pen.), 44' (pen.) Rep 71' de Jong 88'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '23 de junho', 'time1': 'Suécia', 'placar': '3 - 0', 'time2': 'Uruguai', 'estadio': 'Rheinstadion, Düsseldorf', 'gols': 3, 'detalhes': '', 'marcadores': "Suécia: Edström 46', 77' Sandberg 74'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '15 de junho', 'time1': 'Itália', 'placar': '3 - 1', 'time2': 'Haiti', 'estadio': 'Olympiastadion, Munique', 'gols': 4, 'detalhes': '', 'marcadores': "Itália: Gianni Rivera 52' Romeo Benetti 64' Pietro Anastasi 78' | Haiti: Sanon 46'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '15 de junho', 'time1': 'Polônia', 'placar': '3 - 2', 'time2': 'Argentina', 'estadio': 'Neckarstadion, Estugarda', 'gols': 5, 'detalhes': '', 'marcadores': "Polônia: Grzegorz Lato 7', 62' Andrzej Szarmach 8' | Argentina: Ramón Heredia 60' Carlos Babington 66'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '19 de junho', 'time1': 'Argentina', 'placar': '1 - 1', 'time2': 'Itália', 'estadio': 'Neckarstadion, Estugarda', 'gols': 2, 'detalhes': '', 'marcadores': "Argentina: René Houseman 19' | Itália: Roberto Perfumo 35' (g.c.)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '19 de junho', 'time1': 'Haiti', 'placar': '0 - 7', 'time2': 'Polônia', 'estadio': 'Olympiastadion, Munique', 'gols': 7, 'detalhes': '', 'marcadores': "Polônia: Lato 17', 87' Kazimierz Deyna 18' Andrzej Szarmach 30', 34', 50' Jerzy Gorgoń 31'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '23 de junho', 'time1': 'Argentina', 'placar': '4 - 1', 'time2': 'Haiti', 'estadio': 'Olympiastadion, Munique', 'gols': 5, 'detalhes': '', 'marcadores': "Argentina: Hector Yazalde 15', 68' René Houseman 18' Rubén Ayala 55' | Haiti: Sanon 63'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '23 de junho', 'time1': 'Polônia', 'placar': '2 - 1', 'time2': 'Itália', 'estadio': 'Neckarstadion, Estugarda', 'gols': 3, 'detalhes': '', 'marcadores': "Polônia: Andrzej Szarmach 38' Kazimierz Deyna 44' | Itália: Fabio Capello 85'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo A', 'data': '26 de junho', 'time1': 'Brasil', 'placar': '1 - 0', 'time2': 'Alemanha Oriental', 'estadio': 'Niedersachsenstadion, Hanôver', 'gols': 1, 'detalhes': '', 'marcadores': "Brasil: Rivelino 60'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo A', 'data': '26 de junho', 'time1': 'Países Baixos', 'placar': '4 - 0', 'time2': 'Argentina', 'estadio': 'Parkstadion, Gelsenkirchen', 'gols': 4, 'detalhes': '', 'marcadores': "Países Baixos: Cruyff 10', 90' Krol 25' Rep 73'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo A', 'data': '30 de junho', 'time1': 'Argentina', 'placar': '1 - 2', 'time2': 'Brasil', 'estadio': 'Niedersachsenstadion, Hanôver', 'gols': 3, 'detalhes': '', 'marcadores': "Argentina: Brindisi 35' | Brasil: Rivelino 32' Jairzinho 49'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo A', 'data': '30 de junho', 'time1': 'Alemanha Oriental', 'placar': '0 - 2', 'time2': 'Países Baixos', 'estadio': 'Parkstadion, Gelsenkirchen', 'gols': 2, 'detalhes': '', 'marcadores': "Países Baixos: Neeskens 7' Rensenbrink 59'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo A', 'data': '3 de julho', 'time1': 'Países Baixos', 'placar': '2 - 0', 'time2': 'Brasil', 'estadio': 'Westfalenstadion, Dortmund', 'gols': 2, 'detalhes': '', 'marcadores': "Países Baixos: Neeskens 50' Cruyff 65'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo A', 'data': '3 de julho', 'time1': 'Argentina', 'placar': '1 - 1', 'time2': 'Alemanha Oriental', 'estadio': 'Parkstadion, Gelsenkirchen', 'gols': 2, 'detalhes': '', 'marcadores': "Argentina: Houseman 20' | Alemanha Oriental: Streich 14'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo B', 'data': '26 de junho', 'time1': 'Iugoslávia', 'placar': '0 - 2', 'time2': 'Alemanha', 'estadio': 'Rheinstadion, Düsseldorf', 'gols': 2, 'detalhes': '', 'marcadores': "Alemanha: Paul Breitner 39' Gerd Müller 82'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo B', 'data': '26 de junho', 'time1': 'Suécia', 'placar': '0 - 1', 'time2': 'Polônia', 'estadio': 'Neckarstadion, Estugarda', 'gols': 1, 'detalhes': '', 'marcadores': "Polônia: Grzegorz Lato 43'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo B', 'data': '30 de junho', 'time1': 'Polônia', 'placar': '2 - 1', 'time2': 'Iugoslávia', 'estadio': 'Waldstadion, Frankfurt', 'gols': 3, 'detalhes': '', 'marcadores': "Polônia: Kazimierz Deyna 24' (pen.) Grzegorz Lato 62' | Iugoslávia: Stanislav Karasi 43'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo B', 'data': '30 de junho', 'time1': 'Alemanha', 'placar': '4 - 2', 'time2': 'Suécia', 'estadio': 'Rheinstadion, Düsseldorf', 'gols': 6, 'detalhes': '', 'marcadores': "Alemanha: Wolfgang Overath 51' Rainer Bonhof 52' Jürgen Grabowski 76' Uli Hoeneß 89' (pen.) | Suécia: Ralf Edström 24' Roland Sandberg 53'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo B', 'data': '3 de julho', 'time1': 'Polônia', 'placar': '0 - 1', 'time2': 'Alemanha', 'estadio': 'Waldstadion, Frankfurt', 'gols': 1, 'detalhes': '', 'marcadores': "Alemanha: Gerd Müller 76'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo B', 'data': '3 de julho', 'time1': 'Suécia', 'placar': '2 - 1', 'time2': 'Iugoslávia', 'estadio': 'Rheinstadion, Düsseldorf', 'gols': 3, 'detalhes': '', 'marcadores': "Suécia: Ralf Edström 29' Conny Torstensson 85' | Iugoslávia: Ivica Šurjak 27'", 'vencedor': ''},
            {'fase': 'Terceiro lugar', 'grupo': '', 'data': '6 de julho', 'time1': 'Brasil', 'placar': '0 - 1', 'time2': 'Polônia', 'estadio': 'Olympiastadion, Munique', 'gols': 1, 'detalhes': '', 'marcadores': "Polônia: Grzegorz Lato 76'", 'vencedor': ''},
            {'fase': 'Final', 'grupo': '', 'data': '7 de julho', 'time1': 'Países Baixos', 'placar': '1 - 2', 'time2': 'Alemanha', 'estadio': 'Olympiastadion, Munique', 'gols': 3, 'detalhes': '', 'marcadores': "Países Baixos: Neeskens 2' (pen) | Alemanha: Breitner 25' (pen) Müller 43'", 'vencedor': ''},
        ]
        return groups_1974, matches_1974
    if year == 1978:
        groups_1978 = [
            {'grupo': 'Grupo 1', 'pos': 1, 'selecao': 'Itália', 'pts': 6, 'j': 3, 'v': 3, 'e': 0, 'd': 0, 'gp': 6, 'gc': 2, 'sg': '+4', 'classificado': 'sim'},
            {'grupo': 'Grupo 1', 'pos': 2, 'selecao': 'Argentina', 'pts': 4, 'j': 3, 'v': 2, 'e': 0, 'd': 1, 'gp': 4, 'gc': 3, 'sg': '+1', 'classificado': 'sim'},
            {'grupo': 'Grupo 1', 'pos': 3, 'selecao': 'França', 'pts': 2, 'j': 3, 'v': 1, 'e': 0, 'd': 2, 'gp': 5, 'gc': 5, 'sg': '0', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 1', 'pos': 4, 'selecao': 'Hungria', 'pts': 0, 'j': 3, 'v': 0, 'e': 0, 'd': 3, 'gp': 3, 'gc': 8, 'sg': '-5', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 2', 'pos': 1, 'selecao': 'Polônia', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 4, 'gc': 1, 'sg': '+3', 'classificado': 'sim'},
            {'grupo': 'Grupo 2', 'pos': 2, 'selecao': 'Alemanha', 'pts': 4, 'j': 3, 'v': 1, 'e': 2, 'd': 0, 'gp': 6, 'gc': 0, 'sg': '+6', 'classificado': 'sim'},
            {'grupo': 'Grupo 2', 'pos': 3, 'selecao': 'Tunísia', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 3, 'gc': 2, 'sg': '+1', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 2', 'pos': 4, 'selecao': 'México', 'pts': 0, 'j': 3, 'v': 0, 'e': 0, 'd': 3, 'gp': 2, 'gc': 12, 'sg': '-10', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 3', 'pos': 1, 'selecao': 'Áustria', 'pts': 4, 'j': 3, 'v': 2, 'e': 0, 'd': 1, 'gp': 3, 'gc': 2, 'sg': '+1', 'classificado': 'sim'},
            {'grupo': 'Grupo 3', 'pos': 2, 'selecao': 'Brasil', 'pts': 4, 'j': 3, 'v': 1, 'e': 2, 'd': 0, 'gp': 2, 'gc': 1, 'sg': '+1', 'classificado': 'sim'},
            {'grupo': 'Grupo 3', 'pos': 3, 'selecao': 'Espanha', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 2, 'gc': 2, 'sg': '0', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 3', 'pos': 4, 'selecao': 'Suécia', 'pts': 1, 'j': 3, 'v': 0, 'e': 1, 'd': 2, 'gp': 1, 'gc': 3, 'sg': '-2', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 4', 'pos': 1, 'selecao': 'Peru', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 7, 'gc': 2, 'sg': '+5', 'classificado': 'sim'},
            {'grupo': 'Grupo 4', 'pos': 2, 'selecao': 'Países Baixos', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 5, 'gc': 3, 'sg': '+2', 'classificado': 'sim'},
            {'grupo': 'Grupo 4', 'pos': 3, 'selecao': 'Escócia', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 5, 'gc': 6, 'sg': '-1', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 4', 'pos': 4, 'selecao': 'Irã', 'pts': 1, 'j': 3, 'v': 0, 'e': 1, 'd': 2, 'gp': 2, 'gc': 8, 'sg': '-6', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo A', 'pos': 1, 'selecao': 'Países Baixos', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 9, 'gc': 4, 'sg': '+5', 'classificado': 'sim'},
            {'grupo': '2ª Fase - Grupo A', 'pos': 2, 'selecao': 'Itália', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 2, 'gc': 2, 'sg': '0', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo A', 'pos': 3, 'selecao': 'Alemanha', 'pts': 2, 'j': 3, 'v': 0, 'e': 2, 'd': 1, 'gp': 4, 'gc': 5, 'sg': '-1', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo A', 'pos': 4, 'selecao': 'Áustria', 'pts': 2, 'j': 3, 'v': 1, 'e': 0, 'd': 2, 'gp': 4, 'gc': 8, 'sg': '-4', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo B', 'pos': 1, 'selecao': 'Argentina', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 8, 'gc': 0, 'sg': '+8', 'classificado': 'sim'},
            {'grupo': '2ª Fase - Grupo B', 'pos': 2, 'selecao': 'Brasil', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 6, 'gc': 1, 'sg': '+5', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo B', 'pos': 3, 'selecao': 'Polônia', 'pts': 2, 'j': 3, 'v': 1, 'e': 0, 'd': 2, 'gp': 2, 'gc': 5, 'sg': '-3', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo B', 'pos': 4, 'selecao': 'Peru', 'pts': 0, 'j': 3, 'v': 0, 'e': 0, 'd': 3, 'gp': 0, 'gc': 10, 'sg': '-10', 'classificado': 'eliminado'},
        ]
        matches_1978 = [
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '2 de junho', 'time1': 'Itália', 'placar': '2 - 1', 'time2': 'França', 'estadio': 'Estádio José María Minella, Mar del Plata', 'gols': 3, 'detalhes': '', 'marcadores': "Itália: Paolo Rossi 29' Zaccarelli 52' | França: Lacombe 1'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '2 de junho', 'time1': 'Argentina', 'placar': '2 - 1', 'time2': 'Hungria', 'estadio': 'Estádio Monumental de Núñez, Buenos Aires', 'gols': 3, 'detalhes': '', 'marcadores': "Argentina: Luque 15' Bertoni 83' | Hungria: Csapó 10'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '6 de junho', 'time1': 'Itália', 'placar': '3 - 1', 'time2': 'Hungria', 'estadio': 'Estádio José María Minella, Mar del Plata', 'gols': 4, 'detalhes': '', 'marcadores': "Itália: Rossi 34' Bettega 36' Benetti 60' | Hungria: A. Tóth 81' (pen.)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '6 de junho', 'time1': 'Argentina', 'placar': '2 - 1', 'time2': 'França', 'estadio': 'Estádio Monumental de Núñez, Buenos Aires', 'gols': 3, 'detalhes': '', 'marcadores': "Argentina: Passarella 45' (pen.) Luque 73' | França: Platini 60'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '10 de junho', 'time1': 'França', 'placar': '3 - 1', 'time2': 'Hungria', 'estadio': 'Estádio José María Minella, Mar del Plata', 'gols': 4, 'detalhes': '', 'marcadores': "França: Lopez 22' Berdoll 37' Rocheteau 42' | Hungria: Zombori 41'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '10 de junho', 'time1': 'Argentina', 'placar': '0 - 1', 'time2': 'Itália', 'estadio': 'Estádio Monumental de Núñez, Buenos Aires', 'gols': 1, 'detalhes': '', 'marcadores': "Itália: Bettega 67'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '1 de junho', 'time1': 'Alemanha', 'placar': '0 - 0', 'time2': 'Polônia', 'estadio': 'Estádio Monumental de Núñez, Buenos Aires', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '2 de junho', 'time1': 'Tunísia', 'placar': '3 - 1', 'time2': 'México', 'estadio': 'Estádio Gigante de Arroyito, Rosário', 'gols': 4, 'detalhes': '', 'marcadores': "Tunísia: Kaabi 55' Ghommidh 79' Dhouieb 87' | México: Vázquez Ayala 45' (pen.)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '6 de junho', 'time1': 'Alemanha', 'placar': '6 - 0', 'time2': 'México', 'estadio': 'Estádio Chateau Carreras, Córdoba', 'gols': 6, 'detalhes': '', 'marcadores': "Alemanha: D. Müller 15' H. Müller 30' Rummenigge 38', 73' Flohe 44', 89'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '6 de junho', 'time1': 'Polônia', 'placar': '1 - 0', 'time2': 'Tunísia', 'estadio': 'Estádio Gigante de Arroyito, Rosário', 'gols': 1, 'detalhes': '', 'marcadores': "Polônia: Lato 43'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '10 de junho', 'time1': 'Alemanha', 'placar': '0 - 0', 'time2': 'Tunísia', 'estadio': 'Estádio Chateau Carreras, Córdoba', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '10 de junho', 'time1': 'Polônia', 'placar': '3 - 1', 'time2': 'México', 'estadio': 'Estádio Gigante de Arroyito, Rosário', 'gols': 4, 'detalhes': '', 'marcadores': "Polônia: Boniek 43', 84' Deyna 56' | México: Rangel 52'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '3 de junho', 'time1': 'Áustria', 'placar': '2 - 1', 'time2': 'Espanha', 'estadio': 'Estádio José Amalfitani, Buenos Aires', 'gols': 3, 'detalhes': '', 'marcadores': "Áustria: Schachner 9' Krankl 76' | Espanha: Dani 21'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '3 de junho', 'time1': 'Brasil', 'placar': '1 - 1', 'time2': 'Suécia', 'estadio': 'Estádio José María Minella, Mar del Plata', 'gols': 2, 'detalhes': '', 'marcadores': "Brasil: Reinaldo 45' | Suécia: Sjöberg 37'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '7 de junho', 'time1': 'Suécia', 'placar': '0 - 1', 'time2': 'Áustria', 'estadio': 'Estádio José Amalfitani, Buenos Aires', 'gols': 1, 'detalhes': '', 'marcadores': "Áustria: Krankl 42' (pen.)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '7 de junho', 'time1': 'Brasil', 'placar': '0 - 0', 'time2': 'Espanha', 'estadio': 'Estádio José María Minella, Mar del Plata', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '11 de junho', 'time1': 'Suécia', 'placar': '0 - 1', 'time2': 'Espanha', 'estadio': 'Estádio José Amalfitani, Buenos Aires', 'gols': 1, 'detalhes': '', 'marcadores': "Espanha: Asensi 75'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '11 de junho', 'time1': 'Brasil', 'placar': '1 - 0', 'time2': 'Áustria', 'estadio': 'Estádio José María Minella, Mar del Plata', 'gols': 1, 'detalhes': '', 'marcadores': "Brasil: Roberto Dinamite 40'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '3 de junho', 'time1': 'Peru', 'placar': '3 - 1', 'time2': 'Escócia', 'estadio': 'Estádio Olímpico Chateau Carreras, Córdoba', 'gols': 4, 'detalhes': '', 'marcadores': "Peru: Cueto 43' Cubillas 72', 77' | Escócia: Jordan 14'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '3 de junho', 'time1': 'Países Baixos', 'placar': '3 - 0', 'time2': 'Irã', 'estadio': 'Estádio Ciudad de Mendoza, Mendoza', 'gols': 3, 'detalhes': '', 'marcadores': "Países Baixos: Rensenbrink 40' (pen.), 62', 79' (pen.)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '7 de junho', 'time1': 'Escócia', 'placar': '1 - 1', 'time2': 'Irã', 'estadio': 'Estádio Olímpico Chateau Carreras, Córdoba', 'gols': 2, 'detalhes': '', 'marcadores': "Escócia: Eskandarian 43' (g.c.) | Irã: Danaeifard 60'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '7 de junho', 'time1': 'Países Baixos', 'placar': '0 - 0', 'time2': 'Peru', 'estadio': 'Estádio Ciudad de Mendoza, Mendoza', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '11 de junho', 'time1': 'Peru', 'placar': '4 - 1', 'time2': 'Irã', 'estadio': 'Estádio Olímpico Chateau Carreras, Córdoba', 'gols': 5, 'detalhes': '', 'marcadores': "Peru: Velásquez 2' Cubillas 36' (pen.), 39' (pen.), 79' | Irã: Rowshan 41'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '11 de junho', 'time1': 'Escócia', 'placar': '3 - 2', 'time2': 'Países Baixos', 'estadio': 'Estádio Ciudad de Mendoza, Mendoza', 'gols': 5, 'detalhes': '', 'marcadores': "Escócia: Dalglish 44' Gemmill 47' (pen.), 68' | Países Baixos: Rensenbrink 34' (pen.) Rep 71'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo A', 'data': '14 de junho', 'time1': 'Países Baixos', 'placar': '5 - 1', 'time2': 'Áustria', 'estadio': 'Estádio Olímpico Chateau Carreras, Córdoba', 'gols': 6, 'detalhes': '', 'marcadores': "Países Baixos: Brandts 6' Rensenbrink 35' (pen.) Rep 36', 53' W. van de Kerkhof 82' | Áustria: Obermayer 79'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo A', 'data': '14 de junho', 'time1': 'Alemanha', 'placar': '0 - 0', 'time2': 'Itália', 'estadio': 'Estádio Monumental de Núñez, Buenos Aires', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo A', 'data': '18 de junho', 'time1': 'Alemanha', 'placar': '2 - 2', 'time2': 'Países Baixos', 'estadio': 'Estádio Olímpico Chateau Carreras, Córdoba', 'gols': 4, 'detalhes': '', 'marcadores': "Alemanha: Abramczik 3' D. Müller 70' | Países Baixos: Haan 27' R. van de Kerkhof 84'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo A', 'data': '18 de junho', 'time1': 'Itália', 'placar': '1 - 0', 'time2': 'Áustria', 'estadio': 'Estádio Monumental de Núñez, Buenos Aires', 'gols': 1, 'detalhes': '', 'marcadores': "Itália: Paolo Rossi 14'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo A', 'data': '21 de junho', 'time1': 'Áustria', 'placar': '3 - 2', 'time2': 'Alemanha', 'estadio': 'Estádio Olímpico Chateau Carreras, Córdoba', 'gols': 5, 'detalhes': '', 'marcadores': "Áustria: Vogts 59' (g.c.) Krankl 66', 87' | Alemanha: Rummenigge 19' Hölzenbein 72'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo A', 'data': '21 de junho', 'time1': 'Países Baixos', 'placar': '2 - 1', 'time2': 'Itália', 'estadio': 'Estádio Monumental de Núñez, Buenos Aires', 'gols': 3, 'detalhes': '', 'marcadores': "Países Baixos: Brandts 18' Haan 75' | Itália: Brandts 10' (g.c.)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo B', 'data': '14 de junho', 'time1': 'Brasil', 'placar': '3 - 0', 'time2': 'Peru', 'estadio': 'Estádio Ciudad de Mendoza, Mendoza', 'gols': 3, 'detalhes': '', 'marcadores': "Brasil: Dirceu 15', 28' Zico 73' (pen.)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo B', 'data': '14 de junho', 'time1': 'Argentina', 'placar': '2 - 0', 'time2': 'Polônia', 'estadio': 'Estádio Gigante de Arroyito, Rosário', 'gols': 2, 'detalhes': '', 'marcadores': "Argentina: Kempes 16', 71'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo B', 'data': '18 de junho', 'time1': 'Polônia', 'placar': '1 - 0', 'time2': 'Peru', 'estadio': 'Estádio Ciudad de Mendoza, Mendoza', 'gols': 1, 'detalhes': '', 'marcadores': "Polônia: Szarmach 65'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo B', 'data': '18 de junho', 'time1': 'Argentina', 'placar': '0 - 0', 'time2': 'Brasil', 'estadio': 'Estádio Gigante de Arroyito, Rosário', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo B', 'data': '21 de junho', 'time1': 'Brasil', 'placar': '3 - 1', 'time2': 'Polônia', 'estadio': 'Estádio Ciudad de Mendoza, Mendoza', 'gols': 4, 'detalhes': '', 'marcadores': "Brasil: Nelinho 12' Roberto Dinamite 57', 63' | Polônia: Lato 45'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo B', 'data': '21 de junho', 'time1': 'Argentina', 'placar': '6 - 0', 'time2': 'Peru', 'estadio': 'Estádio Gigante de Arroyito, Rosário', 'gols': 6, 'detalhes': '', 'marcadores': "Argentina: Kempes 21', 49' Tarantini 43' Luque 50', 72' Houseman 67'", 'vencedor': ''},
            {'fase': 'Terceiro lugar', 'grupo': '', 'data': '24 de junho', 'time1': 'Itália', 'placar': '1 - 2', 'time2': 'Brasil', 'estadio': 'Estádio Monumental de Núñez, Buenos Aires', 'gols': 3, 'detalhes': '', 'marcadores': "Itália: Causio 38' | Brasil: Nelinho 64' Dirceu 72'", 'vencedor': ''},
            {'fase': 'Final', 'grupo': '', 'data': '25 de junho', 'time1': 'Argentina', 'placar': '3 - 1', 'time2': 'Países Baixos', 'estadio': 'Estádio Monumental de Núñez, Buenos Aires', 'gols': 4, 'detalhes': '', 'marcadores': "Argentina: Bertoni 116' Kempes 38', 105' | Países Baixos: Nanninga 82'", 'vencedor': ''},
        ]
        return groups_1978, matches_1978
    if year == 1982:
        groups_1982 = [
            {'grupo': 'Grupo 1', 'pos': 1, 'selecao': 'Polônia', 'pts': 4, 'j': 3, 'v': 1, 'e': 2, 'd': 0, 'gp': 5, 'gc': 1, 'sg': '+4', 'classificado': 'sim'},
            {'grupo': 'Grupo 1', 'pos': 2, 'selecao': 'Itália', 'pts': 3, 'j': 3, 'v': 0, 'e': 3, 'd': 0, 'gp': 2, 'gc': 2, 'sg': '0', 'classificado': 'sim'},
            {'grupo': 'Grupo 1', 'pos': 3, 'selecao': 'Camarões', 'pts': 3, 'j': 3, 'v': 0, 'e': 3, 'd': 0, 'gp': 1, 'gc': 1, 'sg': '0', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 1', 'pos': 4, 'selecao': 'Peru', 'pts': 2, 'j': 3, 'v': 0, 'e': 2, 'd': 1, 'gp': 2, 'gc': 6, 'sg': '-4', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 2', 'pos': 1, 'selecao': 'Alemanha', 'pts': 4, 'j': 3, 'v': 2, 'e': 0, 'd': 1, 'gp': 6, 'gc': 3, 'sg': '+3', 'classificado': 'sim'},
            {'grupo': 'Grupo 2', 'pos': 2, 'selecao': 'Áustria', 'pts': 4, 'j': 3, 'v': 2, 'e': 0, 'd': 1, 'gp': 3, 'gc': 1, 'sg': '+2', 'classificado': 'sim'},
            {'grupo': 'Grupo 2', 'pos': 3, 'selecao': 'Argélia', 'pts': 4, 'j': 3, 'v': 2, 'e': 0, 'd': 1, 'gp': 5, 'gc': 5, 'sg': '0', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 2', 'pos': 4, 'selecao': 'Chile', 'pts': 0, 'j': 3, 'v': 0, 'e': 0, 'd': 3, 'gp': 3, 'gc': 8, 'sg': '-5', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 3', 'pos': 1, 'selecao': 'Bélgica', 'pts': 5, 'j': 3, 'v': 2, 'e': 1, 'd': 0, 'gp': 3, 'gc': 1, 'sg': '+2', 'classificado': 'sim'},
            {'grupo': 'Grupo 3', 'pos': 2, 'selecao': 'Argentina', 'pts': 4, 'j': 3, 'v': 2, 'e': 0, 'd': 1, 'gp': 6, 'gc': 2, 'sg': '+4', 'classificado': 'sim'},
            {'grupo': 'Grupo 3', 'pos': 3, 'selecao': 'Hungria', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 12, 'gc': 6, 'sg': '+6', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 3', 'pos': 4, 'selecao': 'El Salvador', 'pts': 0, 'j': 3, 'v': 0, 'e': 0, 'd': 3, 'gp': 1, 'gc': 13, 'sg': '-12', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 4', 'pos': 1, 'selecao': 'Inglaterra', 'pts': 6, 'j': 3, 'v': 3, 'e': 0, 'd': 0, 'gp': 6, 'gc': 1, 'sg': '+5', 'classificado': 'sim'},
            {'grupo': 'Grupo 4', 'pos': 2, 'selecao': 'França', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 6, 'gc': 5, 'sg': '+1', 'classificado': 'sim'},
            {'grupo': 'Grupo 4', 'pos': 3, 'selecao': 'Tchecoslováquia', 'pts': 2, 'j': 3, 'v': 0, 'e': 2, 'd': 1, 'gp': 2, 'gc': 4, 'sg': '-2', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 4', 'pos': 4, 'selecao': 'Kuwait', 'pts': 1, 'j': 3, 'v': 0, 'e': 1, 'd': 2, 'gp': 2, 'gc': 6, 'sg': '-4', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 5', 'pos': 1, 'selecao': 'Irlanda do Norte', 'pts': 4, 'j': 3, 'v': 1, 'e': 2, 'd': 0, 'gp': 2, 'gc': 1, 'sg': '+1', 'classificado': 'sim'},
            {'grupo': 'Grupo 5', 'pos': 2, 'selecao': 'Espanha', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 3, 'gc': 3, 'sg': '0', 'classificado': 'sim'},
            {'grupo': 'Grupo 5', 'pos': 3, 'selecao': 'Iugoslávia', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 2, 'gc': 2, 'sg': '0', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 5', 'pos': 4, 'selecao': 'Honduras', 'pts': 2, 'j': 3, 'v': 0, 'e': 2, 'd': 1, 'gp': 2, 'gc': 3, 'sg': '-1', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 6', 'pos': 1, 'selecao': 'Brasil', 'pts': 6, 'j': 3, 'v': 3, 'e': 0, 'd': 0, 'gp': 10, 'gc': 2, 'sg': '+8', 'classificado': 'sim'},
            {'grupo': 'Grupo 6', 'pos': 2, 'selecao': 'União Soviética', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 6, 'gc': 4, 'sg': '+2', 'classificado': 'sim'},
            {'grupo': 'Grupo 6', 'pos': 3, 'selecao': 'Escócia', 'pts': 3, 'j': 3, 'v': 1, 'e': 1, 'd': 1, 'gp': 8, 'gc': 8, 'sg': '0', 'classificado': 'eliminado'},
            {'grupo': 'Grupo 6', 'pos': 4, 'selecao': 'Nova Zelândia', 'pts': 0, 'j': 3, 'v': 0, 'e': 0, 'd': 3, 'gp': 2, 'gc': 12, 'sg': '-10', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo A', 'pos': 1, 'selecao': 'Polônia', 'pts': 3, 'j': 2, 'v': 1, 'e': 1, 'd': 0, 'gp': 3, 'gc': 0, 'sg': '+3', 'classificado': 'sim'},
            {'grupo': '2ª Fase - Grupo A', 'pos': 2, 'selecao': 'União Soviética', 'pts': 3, 'j': 2, 'v': 1, 'e': 1, 'd': 0, 'gp': 1, 'gc': 0, 'sg': '+1', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo A', 'pos': 3, 'selecao': 'Bélgica', 'pts': 0, 'j': 2, 'v': 0, 'e': 0, 'd': 2, 'gp': 0, 'gc': 4, 'sg': '-4', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo B', 'pos': 1, 'selecao': 'Alemanha', 'pts': 3, 'j': 2, 'v': 1, 'e': 1, 'd': 0, 'gp': 2, 'gc': 1, 'sg': '+1', 'classificado': 'sim'},
            {'grupo': '2ª Fase - Grupo B', 'pos': 2, 'selecao': 'Inglaterra', 'pts': 2, 'j': 2, 'v': 0, 'e': 2, 'd': 0, 'gp': 0, 'gc': 0, 'sg': '0', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo B', 'pos': 3, 'selecao': 'Espanha', 'pts': 1, 'j': 2, 'v': 0, 'e': 1, 'd': 1, 'gp': 1, 'gc': 2, 'sg': '-1', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo C', 'pos': 1, 'selecao': 'Itália', 'pts': 4, 'j': 2, 'v': 2, 'e': 0, 'd': 0, 'gp': 5, 'gc': 3, 'sg': '+2', 'classificado': 'sim'},
            {'grupo': '2ª Fase - Grupo C', 'pos': 2, 'selecao': 'Brasil', 'pts': 2, 'j': 2, 'v': 1, 'e': 0, 'd': 1, 'gp': 5, 'gc': 4, 'sg': '+1', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo C', 'pos': 3, 'selecao': 'Argentina', 'pts': 0, 'j': 2, 'v': 0, 'e': 0, 'd': 2, 'gp': 2, 'gc': 5, 'sg': '-3', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo D', 'pos': 1, 'selecao': 'França', 'pts': 4, 'j': 2, 'v': 2, 'e': 0, 'd': 0, 'gp': 5, 'gc': 1, 'sg': '+4', 'classificado': 'sim'},
            {'grupo': '2ª Fase - Grupo D', 'pos': 2, 'selecao': 'Áustria', 'pts': 1, 'j': 2, 'v': 0, 'e': 1, 'd': 1, 'gp': 2, 'gc': 3, 'sg': '-1', 'classificado': 'eliminado'},
            {'grupo': '2ª Fase - Grupo D', 'pos': 3, 'selecao': 'Irlanda do Norte', 'pts': 1, 'j': 2, 'v': 0, 'e': 1, 'd': 1, 'gp': 3, 'gc': 6, 'sg': '-3', 'classificado': 'eliminado'},
        ]
        matches_1982 = [
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '14 de junho', 'time1': 'Itália', 'placar': '0 - 0', 'time2': 'Polônia', 'estadio': 'Estádio de Balaídos, Vigo', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '15 de junho', 'time1': 'Peru', 'placar': '0 - 0', 'time2': 'Camarões', 'estadio': 'Estádio de Riazor, Corunha', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '18 de junho', 'time1': 'Itália', 'placar': '1 - 1', 'time2': 'Peru', 'estadio': 'Estádio Balaídos, Vigo', 'gols': 2, 'detalhes': '', 'marcadores': "Itália: Conti 18' | Peru: Díaz 83'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '19 de junho', 'time1': 'Polônia', 'placar': '0 - 0', 'time2': 'Camarões', 'estadio': 'Estádio de Riazor, Corunha', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '22 de junho', 'time1': 'Polônia', 'placar': '5 - 1', 'time2': 'Peru', 'estadio': 'Estádio de Riazor, Corunha', 'gols': 6, 'detalhes': '', 'marcadores': "Polônia: Smolarek 55' Lato 58' Boniek 61' Buncol 68' Ciołek 76' | Peru: La Rosa 83'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 1', 'data': '23 de junho', 'time1': 'Itália', 'placar': '1 - 1', 'time2': 'Camarões', 'estadio': 'Estádio Balaídos, Vigo', 'gols': 2, 'detalhes': '', 'marcadores': "Itália: Graziani 60' | Camarões: M'Bida 61'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '16 de junho', 'time1': 'Alemanha', 'placar': '1 - 2', 'time2': 'Argélia', 'estadio': 'El Molinón, Gijón', 'gols': 3, 'detalhes': '', 'marcadores': "Alemanha: Rummenigge 67' | Argélia: Madjer 54' Belloumi 68'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '17 de junho', 'time1': 'Chile', 'placar': '0 - 1', 'time2': 'Áustria', 'estadio': 'Estádio Carlos Tartiere, Oviedo', 'gols': 1, 'detalhes': '', 'marcadores': "Áustria: Schachner 21'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '20 de junho', 'time1': 'Alemanha', 'placar': '4 - 1', 'time2': 'Chile', 'estadio': 'El Molinón, Gijón', 'gols': 5, 'detalhes': '', 'marcadores': "Alemanha: Rummenigge 9', 57', 66' Reinders 81' | Chile: Moscoso 90'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '21 de junho', 'time1': 'Argélia', 'placar': '0 - 2', 'time2': 'Áustria', 'estadio': 'Estádio Carlos Tartiere, Oviedo', 'gols': 2, 'detalhes': '', 'marcadores': "Áustria: Schachner 55' Krankl 67'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '24 de junho', 'time1': 'Argélia', 'placar': '3 - 2', 'time2': 'Chile', 'estadio': 'Estádio Carlos Tartiere, Oviedo', 'gols': 5, 'detalhes': '', 'marcadores': "Argélia: Assad 7', 31' Bensaoula 35' | Chile: Neira 59' (pen) Letelier 73'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 2', 'data': '25 de junho', 'time1': 'Alemanha', 'placar': '1 - 0', 'time2': 'Áustria', 'estadio': 'El Molinón, Gijón', 'gols': 1, 'detalhes': '', 'marcadores': "Alemanha: Hrubesch 10'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '13 de junho', 'time1': 'Argentina', 'placar': '0 - 1', 'time2': 'Bélgica', 'estadio': 'Camp Nou, Barcelona', 'gols': 1, 'detalhes': '', 'marcadores': "Bélgica: Vandenbergh 62'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '15 de junho', 'time1': 'Hungria', 'placar': '10 - 1', 'time2': 'El Salvador', 'estadio': 'Nuevo Estadio, Elche', 'gols': 11, 'detalhes': '', 'marcadores': "Hungria: Nyilasi 4', 83' Pölöskei 11' Fazekas 23', 54' Tóth 50' Kiss 69', 72', 76' Szentes 72' | El Salvador: Ramírez 64'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '18 de junho', 'time1': 'Argentina', 'placar': '4 - 1', 'time2': 'Hungria', 'estadio': 'Estádio José Rico Pérez, Alicante', 'gols': 5, 'detalhes': '', 'marcadores': "Argentina: Bertoni 26' Maradona 28', 57' Ardiles 60' | Hungria: Pölöskei 76'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '19 de junho', 'time1': 'Bélgica', 'placar': '1 - 0', 'time2': 'El Salvador', 'estadio': 'Nuevo Estadio, Elche', 'gols': 1, 'detalhes': '', 'marcadores': "Bélgica: Coeck 19'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '22 de junho', 'time1': 'Bélgica', 'placar': '1 - 1', 'time2': 'Hungria', 'estadio': 'Nuevo Estadio, Elche', 'gols': 2, 'detalhes': '', 'marcadores': "Bélgica: Czerniatynski 76' | Hungria: Varga 27'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 3', 'data': '23 de junho', 'time1': 'Argentina', 'placar': '2 - 0', 'time2': 'El Salvador', 'estadio': 'Estádio José Rico Pérez, Alicante', 'gols': 2, 'detalhes': '', 'marcadores': "Argentina: Passarella 22' (pen) Bertoni 52'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '16 de junho', 'time1': 'Inglaterra', 'placar': '3 - 1', 'time2': 'França', 'estadio': 'Estádio de San Mamés, Bilbau', 'gols': 4, 'detalhes': '', 'marcadores': "Inglaterra: Robson 1', 67' Mariner 83' | França: Soler 24'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '17 de junho', 'time1': 'Tchecoslováquia', 'placar': '1 - 1', 'time2': 'Kuwait', 'estadio': 'Estádio José Zorrilla, Valladolid', 'gols': 2, 'detalhes': '', 'marcadores': "Tchecoslováquia: Panenka 21' (pen) | Kuwait: Al-Dakhil 57'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '20 de junho', 'time1': 'Inglaterra', 'placar': '2 - 0', 'time2': 'Tchecoslováquia', 'estadio': 'Estádio de San Mamés, Bilbau', 'gols': 2, 'detalhes': '', 'marcadores': "Inglaterra: Francis 62' Barmoš 66' (g.c.)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '21 de junho', 'time1': 'França', 'placar': '4 - 1', 'time2': 'Kuwait', 'estadio': 'Estádio José Zorrilla, Valladolid', 'gols': 5, 'detalhes': '', 'marcadores': "França: Genghini 31' Platini 43' Six 48' Bossis 89' | Kuwait: Al-Buloushi 75'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '24 de junho', 'time1': 'França', 'placar': '1 - 1', 'time2': 'Tchecoslováquia', 'estadio': 'Estádio José Zorrilla, Valladolid', 'gols': 2, 'detalhes': '', 'marcadores': "França: Six 66' | Tchecoslováquia: Panenka 84' (pen)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 4', 'data': '25 de junho', 'time1': 'Inglaterra', 'placar': '1 - 0', 'time2': 'Kuwait', 'estadio': 'Estádio de San Mamés, Bilbau', 'gols': 1, 'detalhes': '', 'marcadores': "Inglaterra: Francis 27'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 5', 'data': '16 de junho', 'time1': 'Espanha', 'placar': '1 - 1', 'time2': 'Honduras', 'estadio': 'Estádio Luis Casanova, Valência', 'gols': 2, 'detalhes': '', 'marcadores': "Espanha: López Ufarte 65' (pen) | Honduras: Zelaya 8'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 5', 'data': '17 de junho', 'time1': 'Iugoslávia', 'placar': '0 - 0', 'time2': 'Irlanda do Norte', 'estadio': 'Estádio de La Romareda, Saragoça', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 5', 'data': '20 de junho', 'time1': 'Espanha', 'placar': '2 - 1', 'time2': 'Iugoslávia', 'estadio': 'Estádio Luis Casanova, Valência', 'gols': 3, 'detalhes': '', 'marcadores': "Espanha: Juanito 14' (pen) Saura 66' | Iugoslávia: Gudelj 10'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 5', 'data': '21 de junho', 'time1': 'Honduras', 'placar': '1 - 1', 'time2': 'Irlanda do Norte', 'estadio': 'Estádio de La Romareda, Saragoça', 'gols': 2, 'detalhes': '', 'marcadores': "Honduras: Laing 60' | Irlanda do Norte: Armstrong 10'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 5', 'data': '24 de junho', 'time1': 'Honduras', 'placar': '0 - 1', 'time2': 'Iugoslávia', 'estadio': 'Estádio de La Romareda, Saragoça', 'gols': 1, 'detalhes': '', 'marcadores': "Iugoslávia: Petrović 87' (pen)", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 5', 'data': '25 de junho', 'time1': 'Espanha', 'placar': '0 - 1', 'time2': 'Irlanda do Norte', 'estadio': 'Estádio Luis Casanova, Valência', 'gols': 1, 'detalhes': '', 'marcadores': "Irlanda do Norte: Armstrong 47'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 6', 'data': '14 de junho', 'time1': 'Brasil', 'placar': '2 - 1', 'time2': 'União Soviética', 'estadio': 'Estádio Ramón Sánchez Pizjuán, Sevilha', 'gols': 3, 'detalhes': '', 'marcadores': "Brasil: Sócrates 75' Éder 88' | União Soviética: Bal' 34'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 6', 'data': '15 de junho', 'time1': 'Escócia', 'placar': '5 - 2', 'time2': 'Nova Zelândia', 'estadio': 'Estádio La Rosaleda, Málaga', 'gols': 7, 'detalhes': '', 'marcadores': "Escócia: Dalglish 18' Wark 29', 32' Robertson 73' Archibald 79' | Nova Zelândia: Sumner 54' Wooddin 64'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 6', 'data': '18 de junho', 'time1': 'Brasil', 'placar': '4 - 1', 'time2': 'Escócia', 'estadio': 'Estádio Benito Villamarín, Sevilha', 'gols': 5, 'detalhes': '', 'marcadores': "Brasil: Zico 33' Oscar 48' Éder 63' Falcão 87' | Escócia: Narey 18'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 6', 'data': '19 de junho', 'time1': 'União Soviética', 'placar': '3 - 0', 'time2': 'Nova Zelândia', 'estadio': 'Estádio La Rosaleda, Málaga', 'gols': 3, 'detalhes': '', 'marcadores': "União Soviética: Gavrilov 24' Blokhin 48' Baltacha 68'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 6', 'data': '22 de junho', 'time1': 'União Soviética', 'placar': '2 - 2', 'time2': 'Escócia', 'estadio': 'Estádio La Rosaleda, Málaga', 'gols': 4, 'detalhes': '', 'marcadores': "União Soviética: Chivadze 59' Shengelia 84' | Escócia: Jordan 15' Souness 86'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': 'Grupo 6', 'data': '23 de junho', 'time1': 'Brasil', 'placar': '4 - 0', 'time2': 'Nova Zelândia', 'estadio': 'Estádio Benito Villamarín, Sevilha', 'gols': 4, 'detalhes': '', 'marcadores': "Brasil: Zico 28', 31' Falcão 55' Serginho Chulapa 70'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo A', 'data': '28 de junho', 'time1': 'Polônia', 'placar': '3 - 0', 'time2': 'Bélgica', 'estadio': 'Camp Nou, Barcelona', 'gols': 3, 'detalhes': '', 'marcadores': "Polônia: Boniek 4', 26', 53'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo A', 'data': '1 de julho', 'time1': 'Bélgica', 'placar': '0 - 1', 'time2': 'União Soviética', 'estadio': 'Camp Nou, Barcelona', 'gols': 1, 'detalhes': '', 'marcadores': "União Soviética: Oganesyan 48'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo A', 'data': '4 de julho', 'time1': 'União Soviética', 'placar': '0 - 0', 'time2': 'Polônia', 'estadio': 'Camp Nou, Barcelona', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo B', 'data': '29 de junho', 'time1': 'Alemanha', 'placar': '0 - 0', 'time2': 'Inglaterra', 'estadio': 'Estádio Santiago Bernabéu, Madrid', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo B', 'data': '2 de julho', 'time1': 'Alemanha', 'placar': '2 - 1', 'time2': 'Espanha', 'estadio': 'Estádio Santiago Bernabéu, Madrid', 'gols': 3, 'detalhes': '', 'marcadores': "Alemanha: Littbarski 50' Fischer 75' | Espanha: Zamora 82'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo B', 'data': '5 de julho', 'time1': 'Espanha', 'placar': '0 - 0', 'time2': 'Inglaterra', 'estadio': 'Estádio Santiago Bernabéu, Madrid', 'gols': 0, 'detalhes': '', 'marcadores': '', 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo C', 'data': '29 de junho', 'time1': 'Itália', 'placar': '2 - 1', 'time2': 'Argentina', 'estadio': 'Sarrià, Barcelona', 'gols': 3, 'detalhes': '', 'marcadores': "Itália: Tardelli 55' Cabrini 67' | Argentina: Passarella 83'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo C', 'data': '2 de julho', 'time1': 'Argentina', 'placar': '1 - 3', 'time2': 'Brasil', 'estadio': 'Sarrià, Barcelona', 'gols': 4, 'detalhes': '', 'marcadores': "Argentina: Díaz 89' | Brasil: Zico 11' Serginho Chulapa 66' Júnior 75'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo C', 'data': '5 de julho', 'time1': 'Itália', 'placar': '3 - 2', 'time2': 'Brasil', 'estadio': 'Sarrià, Barcelona', 'gols': 5, 'detalhes': '', 'marcadores': "Itália: Rossi 5', 25', 74' | Brasil: Sócrates 12' Falcão 68'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo D', 'data': '28 de junho', 'time1': 'Áustria', 'placar': '0 - 1', 'time2': 'França', 'estadio': 'Estádio Vicente Calderón, Madrid', 'gols': 1, 'detalhes': '', 'marcadores': "França: Genghini 39'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo D', 'data': '1 de julho', 'time1': 'Áustria', 'placar': '2 - 2', 'time2': 'Irlanda do Norte', 'estadio': 'Estádio Vicente Calderón, Madrid', 'gols': 4, 'detalhes': '', 'marcadores': "Áustria: Pezzey 50' Hintermaier 68' | Irlanda do Norte: Hamilton 27', 75'", 'vencedor': ''},
            {'fase': 'Fase de grupos', 'grupo': '2ª Fase - Grupo D', 'data': '4 de julho', 'time1': 'França', 'placar': '4 - 1', 'time2': 'Irlanda do Norte', 'estadio': 'Estádio Vicente Calderón, Madrid', 'gols': 5, 'detalhes': '', 'marcadores': "França: Giresse 33', 80' Rocheteau 46', 68' | Irlanda do Norte: Armstrong 75'", 'vencedor': ''},
            {'fase': 'Semifinal', 'grupo': '', 'data': '8 de julho', 'time1': 'Polônia', 'placar': '0 - 2', 'time2': 'Itália', 'estadio': 'Camp Nou, Barcelona', 'gols': 2, 'detalhes': '', 'marcadores': "Itália: Rossi 22', 73'", 'vencedor': ''},
            {'fase': 'Semifinal', 'grupo': '', 'data': '8 de julho', 'time1': 'Alemanha', 'placar': '3 - 3 (pro)', 'time2': 'França', 'estadio': 'Estádio Ramón Sánchez Pizjuán, Sevilha', 'gols': 6, 'detalhes': 'Alemanha venceu nos pênaltis por 5 a 4', 'marcadores': "Alemanha: Littbarski 17' Rummenigge 102' Fischer 108' | França: Platini 26' (pen.) Trésor 92' Giresse 98'", 'vencedor': 'Alemanha'},
            {'fase': 'Terceiro lugar', 'grupo': '', 'data': '10 de julho', 'time1': 'Polônia', 'placar': '3 - 2', 'time2': 'França', 'estadio': 'Estádio José Rico Pérez, Alicante', 'gols': 5, 'detalhes': '', 'marcadores': "Polônia: Szarmach 40' Majewski 44' Kupcewicz 46' | França: Girard 13' Couriol 72'", 'vencedor': ''},
            {'fase': 'Final', 'grupo': '', 'data': '11 de julho', 'time1': 'Itália', 'placar': '3 - 1', 'time2': 'Alemanha', 'estadio': 'Estádio Santiago Bernabéu, Madrid', 'gols': 4, 'detalhes': '', 'marcadores': "Itália: Rossi 57' Tardelli 69' Altobelli 81' | Alemanha: Breitner 83'", 'vencedor': ''},
        ]
        return groups_1982, matches_1982
    if year != 1930:
        return groups, matches
    groups_1930 = [
        {"grupo": "Grupo A", "pos": 1, "selecao": "Argentina", "pts": 6, "j": 3, "v": 3, "e": 0, "d": 0, "gp": 10, "gc": 4, "sg": "+6", "classificado": "sim"},
        {"grupo": "Grupo A", "pos": 2, "selecao": "Chile", "pts": 4, "j": 3, "v": 2, "e": 0, "d": 1, "gp": 5, "gc": 3, "sg": "+2", "classificado": "eliminado"},
        {"grupo": "Grupo A", "pos": 3, "selecao": "França", "pts": 2, "j": 3, "v": 1, "e": 0, "d": 2, "gp": 4, "gc": 3, "sg": "+1", "classificado": "eliminado"},
        {"grupo": "Grupo A", "pos": 4, "selecao": "México", "pts": 0, "j": 3, "v": 0, "e": 0, "d": 3, "gp": 4, "gc": 13, "sg": "-9", "classificado": "eliminado"},
        {"grupo": "Grupo B", "pos": 1, "selecao": "Iugoslávia", "pts": 4, "j": 2, "v": 2, "e": 0, "d": 0, "gp": 6, "gc": 1, "sg": "+5", "classificado": "sim"},
        {"grupo": "Grupo B", "pos": 2, "selecao": "Brasil", "pts": 2, "j": 2, "v": 1, "e": 0, "d": 1, "gp": 5, "gc": 2, "sg": "+3", "classificado": "eliminado"},
        {"grupo": "Grupo B", "pos": 3, "selecao": "Bolívia", "pts": 0, "j": 2, "v": 0, "e": 0, "d": 2, "gp": 0, "gc": 8, "sg": "-8", "classificado": "eliminado"},
        {"grupo": "Grupo C", "pos": 1, "selecao": "Uruguai", "pts": 4, "j": 2, "v": 2, "e": 0, "d": 0, "gp": 5, "gc": 0, "sg": "+5", "classificado": "sim"},
        {"grupo": "Grupo C", "pos": 2, "selecao": "Romênia", "pts": 2, "j": 2, "v": 1, "e": 0, "d": 1, "gp": 3, "gc": 5, "sg": "-2", "classificado": "eliminado"},
        {"grupo": "Grupo C", "pos": 3, "selecao": "Peru", "pts": 0, "j": 2, "v": 0, "e": 0, "d": 2, "gp": 1, "gc": 4, "sg": "-3", "classificado": "eliminado"},
        {"grupo": "Grupo D", "pos": 1, "selecao": "Estados Unidos", "pts": 4, "j": 2, "v": 2, "e": 0, "d": 0, "gp": 6, "gc": 0, "sg": "+6", "classificado": "sim"},
        {"grupo": "Grupo D", "pos": 2, "selecao": "Paraguai", "pts": 2, "j": 2, "v": 1, "e": 0, "d": 1, "gp": 1, "gc": 3, "sg": "-2", "classificado": "eliminado"},
        {"grupo": "Grupo D", "pos": 3, "selecao": "Bélgica", "pts": 0, "j": 2, "v": 0, "e": 0, "d": 2, "gp": 0, "gc": 4, "sg": "-4", "classificado": "eliminado"},
    ]
    def group_match(group: str, date: str, t1: str, score: str, t2: str, stadium: str = "Estádio Centenário, Montevidéu", scorers: str = "") -> dict:
        return {"fase": "Fase de grupos", "grupo": group, "data": date, "time1": t1, "placar": score, "time2": t2, "gols": score_goals(score), "estadio": stadium, "detalhes": "", "marcadores": scorers}
    matches_1930 = [
        group_match("Grupo A", "13 de julho", "França", "4 - 1", "México", "Estádio Pocitos, Montevidéu", "França: L. Laurent 19'; Langiller 40'; Maschinot 43', 87' | México: Carreño 70'"),
        group_match("Grupo A", "15 de julho", "Argentina", "1 - 0", "França", "Estádio Parque Central, Montevidéu", "Argentina: Monti 81'"),
        group_match("Grupo A", "16 de julho", "Chile", "3 - 0", "México", "Estádio Parque Central, Montevidéu", "Chile: Carlos Vidal 3', 65'; M. Rosas 52' (g.c.)"),
        group_match("Grupo A", "19 de julho", "Chile", "1 - 0", "França", "Estádio Centenário, Montevidéu", "Chile: Subiabre 67'"),
        group_match("Grupo A", "19 de julho", "Argentina", "6 - 3", "México", "Estádio Centenário, Montevidéu", "Argentina: Stábile 8', 17', 80'; Zumelzú 12', 55'; Varallo 53' | México: M. Rosas 42' (pen.), 65'; Gayón 75'"),
        group_match("Grupo A", "22 de julho", "Argentina", "3 - 1", "Chile", "Estádio Centenário, Montevidéu", "Argentina: Stábile 12', 13'; M. Evaristo 51' | Chile: Subiabre 15'"),
        group_match("Grupo B", "14 de julho", "Iugoslávia", "2 - 1", "Brasil", "Estádio Parque Central, Montevidéu", "Iugoslávia: Tirnanić 21'; Bek 30' | Brasil: Preguinho 62'"),
        group_match("Grupo B", "17 de julho", "Iugoslávia", "4 - 0", "Bolívia", "Estádio Parque Central, Montevidéu", "Iugoslávia: Bek 60', 67'; Marjanović 65'; Vujadinović 85'"),
        group_match("Grupo B", "20 de julho", "Brasil", "4 - 0", "Bolívia", "Estádio Centenário, Montevidéu", "Brasil: Moderato 37', 73'; Preguinho 57', 83'"),
        group_match("Grupo C", "14 de julho", "Romênia", "3 - 1", "Peru", "Estádio Pocitos, Montevidéu", "Romênia: Deșu 1'; Stanciu 79'; Kovács 89' | Peru: Souza Ferreira 75'"),
        group_match("Grupo C", "18 de julho", "Uruguai", "1 - 0", "Peru", "Estádio Centenário, Montevidéu", "Uruguai: Castro 65'"),
        group_match("Grupo C", "21 de julho", "Uruguai", "4 - 0", "Romênia", "Estádio Centenário, Montevidéu", "Uruguai: Dorado 7'; Scarone 26'; Anselmo 31'; Cea 35'"),
        group_match("Grupo D", "13 de julho", "Estados Unidos", "3 - 0", "Bélgica", "Estádio Parque Central, Montevidéu", "Estados Unidos: McGhee 23'; Florie 45'; Patenaude 69'"),
        group_match("Grupo D", "17 de julho", "Estados Unidos", "3 - 0", "Paraguai", "Estádio Parque Central, Montevidéu", "Estados Unidos: Patenaude 10', 15', 50'"),
        group_match("Grupo D", "20 de julho", "Paraguai", "1 - 0", "Bélgica", "Estádio Centenário, Montevidéu", "Paraguai: Vargas Peña 40'"),
        {"fase": "Semifinal", "grupo": "", "data": "26 de julho", "time1": "Argentina", "placar": "6 - 1", "time2": "Estados Unidos", "gols": 7, "estadio": "Estádio Centenário, Montevidéu", "detalhes": "", "marcadores": "Argentina: Monti 20'; Scopelli 56'; Stábile 69', 87'; Peucelle 80', 85' | Estados Unidos: Brown 89'"},
        {"fase": "Semifinal", "grupo": "", "data": "27 de julho", "time1": "Uruguai", "placar": "6 - 1", "time2": "Iugoslávia", "gols": 7, "estadio": "Estádio Centenário, Montevidéu", "detalhes": "", "marcadores": "Uruguai: Cea 18', 67', 72'; Anselmo 20', 31'; Iriarte 61' | Iugoslávia: Vujadinović 4'"},
        {"fase": "Final", "grupo": "", "data": "30 de julho", "time1": "Uruguai", "placar": "4 - 2", "time2": "Argentina", "gols": 6, "estadio": "Estádio Centenário, Montevidéu", "detalhes": "", "marcadores": "Uruguai: Dorado 12'; Cea 57'; Iriarte 68'; Castro 89' | Argentina: Peucelle 20'; Stábile 37'"},
    ]
    return groups_1930, matches_1930


def parse_groups(tables: list[pd.DataFrame]) -> list[dict]:
    groups = []
    idx = 0
    for df in tables:
        dff = flatten_columns(df)
        if is_group_standings_table(dff):
            idx += 1
            group_name = f"Grupo {chr(64 + idx)}" if idx <= 8 else f"Grupo {idx}"
            for _, r in dff.iterrows():
                team = clean_team(row_get(r, "Equipe", "Seleção"))
                if not team or team in {"Equipe", "Seleção"}:
                    continue
                groups.append({
                    "grupo": group_name,
                    "pos": to_int(row_get(r, "Pos", "Pos.")),
                    "selecao": team,
                    "pts": to_int(row_get(r, "Pts")),
                    "j": to_int(row_get(r, "J")),
                    "v": to_int(row_get(r, "V")),
                    "e": to_int(row_get(r, "E")),
                    "d": to_int(row_get(r, "D")),
                    "gp": to_int(row_get(r, "GP")),
                    "gc": to_int(row_get(r, "GC")),
                    "sg": clean_text(row_get(r, "SG")),
                    "classificado": clean_text(row_get(r, "Classificado")),
                })
    return groups


def row_get(row, *names):
    for name in names:
        if name in row:
            return row.get(name)
    return ""


def is_group_standings_table(df: pd.DataFrame) -> bool:
    cols = set(clean_text(c) for c in df.columns)
    has_team = "Equipe" in cols or "Seleção" in cols
    has_pos = "Pos" in cols or "Pos." in cols
    has_stats = {"Pts", "J", "V", "E", "D", "GP", "GC", "SG"}.issubset(cols)
    return has_team and has_pos and has_stats and len(df) == 4


def parse_matches(tables: list[pd.DataFrame]) -> list[dict]:
    matches = []
    group_idx = 0
    current_group = ""
    pending_group_matches = 0
    saw_group_standings = False
    knockout_names = ["Oitavas de final", "Oitavas de final", "Oitavas de final", "Oitavas de final", "Oitavas de final", "Oitavas de final", "Oitavas de final", "Oitavas de final",
                     "Quartas de final", "Quartas de final", "Quartas de final", "Quartas de final",
                     "Semifinal", "Semifinal", "Terceiro lugar", "Final"]
    knockout_idx = 0
    for df in tables:
        dff = flatten_columns(df)
        cols = list(dff.columns)
        if is_group_standings_table(dff):
            saw_group_standings = True
            group_idx += 1
            current_group = f"Grupo {chr(64 + group_idx)}" if group_idx <= 8 else f"Grupo {group_idx}"
            pending_group_matches = 6
            continue
        if pending_group_matches and len(cols) == 4 and all(str(c).startswith("Unnamed") or str(c).isdigit() for c in cols):
            if dff.shape[0] >= 3:
                matches.extend(parse_group_match_table(dff, current_group))
                pending_group_matches = 0
            continue
        if pending_group_matches and len(cols) == 5 and dff.shape[0] == 2:
            item = parse_group_matchbox(dff, current_group)
            if item:
                matches.append(item)
                pending_group_matches -= 1
            continue
        if not saw_group_standings and len(cols) == 4 and all(str(c).startswith("Unnamed") or str(c).isdigit() for c in cols):
            if dff.shape[0] >= 3:
                group_idx += 1
                phase = f"Grupo {chr(64 + group_idx)}" if group_idx <= 8 else "Fase de grupos"
                matches.extend(parse_group_match_table(dff, phase))
        elif len(cols) == 5 and dff.shape[0] == 2:
            phase = knockout_names[knockout_idx] if knockout_idx < len(knockout_names) else "Mata-mata"
            item = parse_knockout_match(dff, phase)
            if item:
                matches.append(item)
                knockout_idx += 1
    return matches


def parse_group_matchbox(df: pd.DataFrame, group: str) -> dict | None:
    item = parse_knockout_match(df, "Fase de grupos")
    if not item:
        return None
    item["grupo"] = group
    if item.get("detalhes"):
        item["marcadores"] = item["detalhes"]
    return item


def parse_group_match_table(df: pd.DataFrame, phase: str) -> list[dict]:
    out = []
    date = ""
    for _, row in df.iterrows():
        vals = [clean_text(row.iloc[i]) if i < len(row) else "" for i in range(4)]
        if vals[0] and not vals[1] and not vals[2]:
            date = vals[0]
            continue
        if vals[0] and vals[1] and vals[2]:
            goals = score_goals(vals[1])
            if not goals:
                continue
            out.append({
                "fase": "Fase de grupos",
                "grupo": phase,
                "data": date,
                "time1": clean_team(vals[0]),
                "placar": vals[1],
                "time2": clean_team(vals[2]),
                "estadio": vals[3],
                "gols": sum(goals) if goals else 0,
                "detalhes": "",
            })
    return out


def parse_knockout_match(df: pd.DataFrame, phase: str) -> dict | None:
    row0 = [clean_text(df.iloc[0, i]) for i in range(5)]
    row1 = [clean_text(df.iloc[1, i]) for i in range(5)] if df.shape[0] > 1 else [""] * 5
    if not row0[1] or not row0[2] or not row0[3]:
        return None
    goals = score_goals(row0[2])
    if not goals:
        return None
    return {
        "fase": phase,
        "grupo": "",
        "data": row0[0],
        "time1": clean_team(row0[1]),
        "placar": row0[2],
        "time2": clean_team(row0[3]),
        "estadio": row0[4],
        "gols": sum(goals) if goals else 0,
        "detalhes": " | ".join(x for x in [row1[1], row1[3], row1[4]] if x),
    }


def group_page_titles(year: int, group: str) -> list[str]:
    suffix = clean_text(group).replace("Grupo ", "")
    titles = [
        f"Copa_do_Mundo_FIFA_de_{year}_–_Grupo_{suffix}",
        f"Copa_do_Mundo_FIFA_de_{year}_-_Grupo_{suffix}",
    ]
    return list(reversed(titles)) if year == 2006 else titles


def match_key(time1: str, placar: str, time2: str) -> tuple[str, str, str]:
    return clean_team(time1), clean_text(placar).replace(" ", ""), clean_team(time2)


def html_cell_text(cell) -> str:
    for br in cell.xpath(".//br"):
        br.tail = "; " + (br.tail or "")
    return clean_text(cell.text_content()).replace("; ;", ";")


def parse_group_page_scorers(path: Path) -> dict[tuple[str, str, str], str]:
    doc = lxml_html.fromstring(path.read_text(encoding="utf-8"))
    out = {}
    for table in doc.xpath("//table"):
        rows = table.xpath(".//tr")
        if len(rows) < 2:
            continue
        first = [html_cell_text(cell) for cell in rows[0].xpath("./th|./td")]
        second = [html_cell_text(cell) for cell in rows[1].xpath("./th|./td")]
        if len(first) < 5 or len(second) < 4:
            continue
        time1, placar, time2 = clean_team(first[1]), clean_text(first[2]), clean_team(first[3])
        if not is_valid_team_name(time1) or not is_valid_team_name(time2) or not score_goals(placar):
            continue
        s1 = clean_text(second[1] if len(second) > 1 else "")
        s2 = clean_text(second[3] if len(second) > 3 else "")
        parts = []
        if s1:
            parts.append(f"{time1}: {s1}")
        if s2:
            parts.append(f"{time2}: {s2}")
        out[match_key(time1, placar, time2)] = " | ".join(parts) if parts else "-"
    return out


def apply_group_scorers(year: int, groups: list[dict], matches: list[dict]) -> None:
    if year < 2006:
        return
    group_names = sorted({g["grupo"] for g in groups if str(g.get("grupo", "")).startswith("Grupo ")})
    for group in group_names:
        path = next((p for title in group_page_titles(year, group) if (p := fetch_optional_page(title))), None)
        if not path:
            continue
        scorers = parse_group_page_scorers(path)
        if not scorers:
            continue
        for match in matches:
            if match.get("fase") != "Fase de grupos" or match.get("grupo") != group:
                continue
            marcador = scorers.get(match_key(match.get("time1"), match.get("placar"), match.get("time2")))
            if marcador:
                match["marcadores"] = marcador


def parse_final_ranking(tables: list[pd.DataFrame]) -> list[dict]:
    candidates = []
    for df in tables:
        dff = flatten_columns(df)
        cols = set(dff.columns)
        if {"Pos.", "Seleção", "J", "V", "E", "D", "GP", "GC", "SG"}.issubset(cols) and len(dff) > 8:
            candidates.append(dff)
    if not candidates:
        return []
    df = candidates[-1]
    out = []
    for _, r in df.iterrows():
        pos = to_int(r.get("Pos."))
        team = clean_team(r.get("Seleção"))
        if not pos or not is_valid_team_name(team):
            continue
        out.append({
            "pos": pos,
            "selecao": team,
            "grupo": clean_text(r.get("Gr")),
            "pts": to_int(r.get("Pts")),
            "j": to_int(r.get("J")),
            "v": to_int(r.get("V")),
            "e": to_int(r.get("E")),
            "d": to_int(r.get("D")),
            "gp": to_int(r.get("GP")),
            "gc": to_int(r.get("GC")),
            "sg": clean_text(r.get("SG")),
        })
    return out


def parse_awards(tables: list[pd.DataFrame]) -> list[dict]:
    awards = []
    for df in tables:
        dff = flatten_columns(df)
        text_cols = " ".join(dff.columns)
        if "Prêmio FIFA" not in text_cols and "Chuteira" not in text_cols and "Bola de Ouro" not in text_cols:
            continue
        for _, row in dff.iterrows():
            for col, val in row.items():
                award = clean_text(col)
                winner = clean_text(val)
                if award and winner and not award.startswith("Unnamed"):
                    awards.append({"premio": award, "vencedor": winner})
    return awards


def parse_stadiums(tables: list[pd.DataFrame], info: dict) -> list[dict]:
    stadiums = []
    for df in tables:
        dff = flatten_columns(df)
        if dff.shape[1] >= 3 and any("Capacidade" in clean_text(x) for x in dff.astype(str).values.flatten()[:20]):
            # Indexacao por posicao (.iloc[:, i]) e nao por rotulo: paginas com
            # colunas de mesmo nome fazem dff[col] virar DataFrame em algumas
            # versoes do pandas (sem .tolist()). Por posicao sempre vem Series.
            labels = columns_text(dff)
            for i in range(dff.shape[1]):
                vals = [clean_text(v) for v in dff.iloc[:, i].dropna().tolist()]
                if vals:
                    stadiums.append({"cidade": labels[i], "estadio": vals[0], "detalhe": " | ".join(vals[1:3])})
    return stadiums[:20]


def aggregate_selection_stats(main: dict, editions_detail: list[dict]) -> list[dict]:
    stats: dict[str, dict] = {}

    def row(team: str) -> dict:
        team = clean_team(team)
        if team not in stats:
            stats[team] = {
                "selecao": team, "participacoes": set(), "titulos": 0, "vices": 0, "terceiros": 0, "quartos": 0,
                "j": 0, "v": 0, "e": 0, "d": 0, "gp": 0, "gc": 0, "melhor_pos": None,
            }
        return stats[team]

    for item in main["editions"]:
        for key, field in [("campeao", "titulos"), ("vice", "vices"), ("terceiro", "terceiros"), ("quarto", "quartos")]:
            if item.get(key) and is_valid_team_name(item[key]):
                row(item[key])[field] += 1

    for cup in editions_detail:
        year = cup["ano"]
        if year == 2026:
            # Em andamento: a classificacao final ainda esta incompleta, entao
            # agrega o que ja foi jogado — grupos (todas as 48) + mata-mata.
            for gr in cup.get("grupos", []):
                if not is_valid_team_name(gr.get("selecao")):
                    continue
                s = row(gr["selecao"])
                s["participacoes"].add(year)
                for k in ("j", "v", "e", "d", "gp", "gc"):
                    s[k] += gr.get(k, 0)
            for p in cup.get("partidas", []):
                if p.get("fase") == "Fase de grupos":
                    continue
                goals = score_goals(p.get("placar"))
                if not goals:
                    continue
                for team, gf, ga in ((p["time1"], goals[0], goals[1]), (p["time2"], goals[1], goals[0])):
                    s = row(team)
                    s["j"] += 1
                    s["gp"] += gf
                    s["gc"] += ga
                    s["v" if gf > ga else "d" if gf < ga else "e"] += 1
            continue
        for r in cup.get("classificacao_final", []):
            if not is_valid_team_name(r.get("selecao")):
                continue
            s = row(r["selecao"])
            s["participacoes"].add(year)
            s["j"] += r["j"]
            s["v"] += r["v"]
            s["e"] += r["e"]
            s["d"] += r["d"]
            s["gp"] += r["gp"]
            s["gc"] += r["gc"]
            pos = r["pos"]
            s["melhor_pos"] = pos if s["melhor_pos"] is None else min(s["melhor_pos"], pos)

    out = []
    for s in stats.values():
        s = s.copy()
        s["participacoes"] = len(s["participacoes"])
        s["sg"] = s["gp"] - s["gc"]
        s["pts"] = s["v"] * 3 + s["e"]
        s["aproveitamento"] = round((s["pts"] / (s["j"] * 3) * 100), 1) if s["j"] else 0
        out.append(s)
    return sorted(out, key=lambda x: (-x["titulos"], -x["vices"], -x["terceiros"], -x["participacoes"], x["selecao"]))


def ensure_plotly() -> str:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not PLOTLY_FILE.exists() or PLOTLY_FILE.stat().st_size == 0:
        print("Baixando Plotly...")
        urlretrieve(PLOTLY_URL, PLOTLY_FILE)
    return PLOTLY_FILE.read_text(encoding="utf-8")


def collect_flag_codes() -> list[str]:
    """Codigos de bandeira usados pelo template (unica fonte da verdade: o JS).

    Extrai os valores do mapa FLAG_CODES direto do HTML para nao duplicar a
    lista nome->codigo em Python. Os codigos sao 'br', 'gb-eng' etc.
    """
    codes: set[str] = set()
    for line in re.findall(r"FLAG_CODES[^\n]*", HTML):
        codes.update(re.findall(r'"([a-z]{2}(?:-[a-z]{3})?)"', line))
    return sorted(codes)


def ensure_flags(codes: list[str]) -> dict[str, str]:
    """Baixa/cacheia cada bandeira e devolve {codigo: data URI base64}.

    Deixa o HTML final offline: as bandeiras ficam embutidas em vez de
    apontar para flagcdn.com. Codigo sem download (sem rede e sem cache) e
    simplesmente omitido; o front-end cai para a sigla da selecao.
    """
    FLAGS_DIR.mkdir(parents=True, exist_ok=True)
    out: dict[str, str] = {}
    for code in codes:
        path = FLAGS_DIR / f"{code}.png"
        if not path.exists() or path.stat().st_size == 0:
            url = f"https://flagcdn.com/w320/{code}.png"
            try:
                req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
                with urlopen(req, timeout=60) as response:
                    path.write_bytes(response.read())
            except Exception as exc:
                print(f"Bandeira nao baixada: {code} ({exc})")
                continue
        data = path.read_bytes()
        if data:
            out[code] = "data:image/png;base64," + base64.b64encode(data).decode("ascii")
    return out


def poster_url(year: int) -> str | None:
    """URL do cartaz/emblema da edicao: a primeira imagem grande da infobox.

    As demais imagens da infobox sao bandeiras pequenas (~22px); o cartaz e a
    unica com largura/altura significativas.
    """
    path = DATA_DIR / f"{PAGE_TITLES[year]}.html"
    if not path.exists():
        return None
    doc = lxml_html.fromstring(path.read_text(encoding="utf-8"))
    boxes = doc.xpath('//table[contains(@class,"infobox")]')
    if not boxes:
        return None
    for im in boxes[0].xpath(".//img"):
        try:
            w, h = int(im.get("width") or 0), int(im.get("height") or 0)
        except ValueError:
            w = h = 0
        if w >= 60 or h >= 100:
            src = im.get("src") or ""
            return ("https:" + src) if src.startswith("//") else src
    return None


def ensure_posters() -> dict[str, str]:
    """Baixa/cacheia o cartaz de cada edicao e devolve {ano: data URI base64}."""
    POSTERS_DIR.mkdir(parents=True, exist_ok=True)
    out: dict[str, str] = {}
    for year in YEARS:
        url = poster_url(year)
        if not url:
            print(f"Cartaz nao encontrado na infobox: {year}")
            continue
        ext = ".png" if ".png" in url.lower() else ".jpg"
        path = POSTERS_DIR / f"{year}{ext}"
        if not path.exists() or path.stat().st_size == 0:
            try:
                req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
                with urlopen(req, timeout=60) as response:
                    path.write_bytes(response.read())
            except Exception as exc:
                print(f"Cartaz nao baixado: {year} ({exc})")
                continue
        data = path.read_bytes()
        if data:
            mime = "image/png" if ext == ".png" else "image/jpeg"
            out[str(year)] = f"data:{mime};base64," + base64.b64encode(data).decode("ascii")
    return out


# As duas tacas oficiais que a Copa do Mundo ja teve, como FOTOS REAIS com o
# fundo removido (recorte por IA). O PNG transparente fica cacheado em
# TROFEUS_DIR; so precisa de rembg para (re)gerar quando o cache nao existe.
TROFEUS = [
    {"id": "jules_rimet", "label": "Jules Rimet", "periodo": "1930–1970",
     "fonte": "La_Coupe_Jules_Rimet_(cropped).jpg"},
    {"id": "fifa", "label": "Taça FIFA", "periodo": "1974–hoje",
     "fonte": "FIFA_World_Cup_Trophy_photo_by_Djuradj_Vujcic.jpg"},
]


def _recortar_trofeu(fonte: str, dest: Path) -> None:
    """Baixa a foto da taca no Commons e remove o fundo com rembg.

    rembg e uma dependencia opcional (pesada): so e importada aqui, quando o
    PNG transparente ainda nao esta no cache. Instale com:
        python -m pip install rembg onnxruntime
    """
    from io import BytesIO

    import numpy as np
    from PIL import Image
    from rembg import remove

    url = "https://commons.wikimedia.org/wiki/Special:FilePath/" + quote(fonte)
    raw = urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=90).read()
    src = Image.open(BytesIO(raw)).convert("RGB")
    if src.height > 440:  # limita p/ recorte rapido e PNG leve
        src = src.resize((round(src.width * 440 / src.height), 440), Image.LANCZOS)
    buf = BytesIO()
    src.save(buf, "PNG")
    cut = Image.open(BytesIO(remove(buf.getvalue()))).convert("RGBA")
    arr = np.array(cut)
    arr[arr[:, :, 3] < 40, 3] = 0  # zera residuos semitransparentes do recorte
    cut = Image.fromarray(arr)
    bbox = cut.getbbox()  # apara a moldura transparente
    if bbox:
        cut = cut.crop(bbox)
    # centraliza pelo EIXO DA BASE (parte de baixo da taca), para o rotulo
    # ficar alinhado com a taca mesmo quando a foto tem leve tombamento.
    alpha = np.array(cut)[:, :, 3]
    h, w = alpha.shape
    cols = np.where(alpha[int(h * 0.80):, :].sum(axis=0) > 3)[0]
    if len(cols):
        axis = (cols.min() + cols.max()) / 2
        pad = int(round(abs(2 * axis - w)))
        if pad:
            left = pad if axis < w / 2 else 0
            canvas = Image.new("RGBA", (w + pad, h), (0, 0, 0, 0))
            canvas.paste(cut, (left, 0))
            cut = canvas
    cut.save(dest)


def ensure_trofeus() -> list[dict]:
    """Devolve [{label, periodo, img(dataURI)}] das tacas recortadas (PNG)."""
    TROFEUS_DIR.mkdir(parents=True, exist_ok=True)
    out = []
    for t in TROFEUS:
        path = TROFEUS_DIR / f"{t['id']}.png"
        if not path.exists() or path.stat().st_size == 0:
            try:
                _recortar_trofeu(t["fonte"], path)
            except Exception as exc:
                print(f"Taca nao gerada (precisa de rembg + rede): {t['id']} ({exc})")
                continue
        data = path.read_bytes()
        if data:
            out.append({
                "label": t["label"], "periodo": t["periodo"],
                "img": "data:image/png;base64," + base64.b64encode(data).decode("ascii"),
            })
    return out


def ensure_favicon() -> str:
    """Favicon (data URI) com a taca da FIFA em canvas quadrado transparente."""
    path = TROFEUS_DIR / "favicon.png"
    src = TROFEUS_DIR / "fifa.png"
    if (not path.exists() or path.stat().st_size == 0) and src.exists():
        try:
            from io import BytesIO

            from PIL import Image

            im = Image.open(src).convert("RGBA")
            side = max(im.size)
            canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
            canvas.paste(im, ((side - im.width) // 2, (side - im.height) // 2))
            canvas.resize((128, 128), Image.LANCZOS).save(path)
        except Exception as exc:
            print(f"Favicon nao gerado: {exc}")
    if path.exists() and path.stat().st_size:
        return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode("ascii")
    return ""


# --- Dados curados da Wikipedia ---------------------------------------
# Estas tres tabelas NAO aparecem nas tabelas que o pandas extrai das
# paginas (foram conferidas manualmente): artilharia historica, artilheiro
# por edicao e os marcadores das partidas de fase de grupos de 2022 (as
# paginas listam marcadores so no mata-mata). Ficam aqui, na camada de
# dados, e sao injetadas no payload como DATA.curados — o template apenas
# renderiza. Para estender marcadores de outras edicoes, some chaves no
# formato "ano|Grupo X|Time1|placar|Time2": "marcadores".
# Artilharia parcial de 2026 em andamento: Mbappe chegou a 10 gols na edicao
# apos a disputa de terceiro lugar, passando a 22 no historico das Copas.
ARTILHEIROS_HISTORICO = [["Kylian Mbappé",22],["Lionel Messi",21],["Miroslav Klose",16],["Ronaldo",15],["Gerd Müller",14],["Just Fontaine",13],["Pelé",12],["Sándor Kocsis",11],["Jürgen Klinsmann",11],["Helmut Rahn",10],["Gary Lineker",10],["Gabriel Batistuta",10],["Teófilo Cubillas",10],["Grzegorz Lato",10],["Thomas Müller",10]]
ARTILHEIROS_EDICAO = [["1930","Guillermo Stábile",8,"Argentina"],["1934","Oldřich Nejedlý",5,"Tchecoslováquia"],["1938","Leônidas",7,"Brasil"],["1950","Ademir",9,"Brasil"],["1954","Sándor Kocsis",11,"Hungria"],["1958","Just Fontaine",13,"França"],["1962","Garrincha, Vavá, L. Sánchez, D. Jerković, F. Albert e V. Ivanov",4,"Brasil, Chile, Iugoslávia, Hungria e União Soviética"],["1966","Eusébio",9,"Portugal"],["1970","Gerd Müller",10,"Alemanha"],["1974","Grzegorz Lato",7,"Polônia"],["1978","Mario Kempes",6,"Argentina"],["1982","Paolo Rossi",6,"Itália"],["1986","Gary Lineker",6,"Inglaterra"],["1990","Salvatore Schillaci",6,"Itália"],["1994","Hristo Stoichkov e Oleg Salenko",6,"Bulgária e Rússia"],["1998","Davor Šuker",6,"Croácia"],["2002","Ronaldo",8,"Brasil"],["2006","Miroslav Klose",5,"Alemanha"],["2010","Thomas Müller",5,"Alemanha"],["2014","James Rodríguez",6,"Colômbia"],["2018","Harry Kane",6,"Inglaterra"],["2022","Kylian Mbappé",8,"França"],["2026","Kylian Mbappé",10,"França"]]
MARCADORES_GRUPOS = {
  "2022|Grupo A|Catar|0 - 2|Equador":"Enner Valencia 16' (pên.), 31'",
  "2022|Grupo A|Senegal|0 - 2|Países Baixos":"Cody Gakpo 84'; Davy Klaassen 90+9'",
  "2022|Grupo A|Catar|1 - 3|Senegal":"Mohammed Muntari 78'; Boulaye Dia 41', Famara Diédhiou 48', Bamba Dieng 84'",
  "2022|Grupo A|Países Baixos|1 - 1|Equador":"Cody Gakpo 6'; Enner Valencia 49'",
  "2022|Grupo A|Países Baixos|2 - 0|Catar":"Cody Gakpo 26'; Frenkie de Jong 49'",
  "2022|Grupo A|Equador|1 - 2|Senegal":"Moisés Caicedo 67'; Ismaïla Sarr 44' (pên.), Kalidou Koulibaly 70'",
  "2022|Grupo B|Inglaterra|6 - 2|Irã":"Jude Bellingham 35'; Bukayo Saka 43', 62'; Raheem Sterling 45+1'; Marcus Rashford 71'; Jack Grealish 90'; Mehdi Taremi 65', 90+13' (pên.)",
  "2022|Grupo B|Estados Unidos|1 - 1|País de Gales":"Timothy Weah 36'; Gareth Bale 82' (pên.)",
  "2022|Grupo B|País de Gales|0 - 2|Irã":"Roozbeh Cheshmi 90+8'; Ramin Rezaeian 90+11'",
  "2022|Grupo B|Inglaterra|0 - 0|Estados Unidos":"-",
  "2022|Grupo B|País de Gales|0 - 3|Inglaterra":"Marcus Rashford 50', 68'; Phil Foden 51'",
  "2022|Grupo B|Irã|0 - 1|Estados Unidos":"Christian Pulisic 38'",
  "2022|Grupo C|Argentina|1 - 2|Arábia Saudita":"Lionel Messi 10' (pên.); Saleh Al-Shehri 48'; Salem Al-Dawsari 53'",
  "2022|Grupo C|México|0 - 0|Polônia":"-",
  "2022|Grupo C|Polônia|2 - 0|Arábia Saudita":"Piotr Zieliński 39'; Robert Lewandowski 82'",
  "2022|Grupo C|Argentina|2 - 0|México":"Lionel Messi 64'; Enzo Fernández 87'",
  "2022|Grupo C|Polônia|0 - 2|Argentina":"Alexis Mac Allister 46'; Julián Álvarez 67'",
  "2022|Grupo C|Arábia Saudita|1 - 2|México":"Salem Al-Dawsari 90+5'; Henry Martín 47'; Luis Chávez 52'",
  "2022|Grupo D|Dinamarca|0 - 0|Tunísia":"-",
  "2022|Grupo D|França|4 - 1|Austrália":"Adrien Rabiot 27'; Olivier Giroud 32', 71'; Kylian Mbappé 68'; Craig Goodwin 9'",
  "2022|Grupo D|Tunísia|0 - 1|Austrália":"Mitchell Duke 23'",
  "2022|Grupo D|França|2 - 1|Dinamarca":"Kylian Mbappé 61', 86'; Andreas Christensen 68'",
  "2022|Grupo D|Austrália|1 - 0|Dinamarca":"Mathew Leckie 60'",
  "2022|Grupo D|Tunísia|1 - 0|França":"Wahbi Khazri 58'",
  "2022|Grupo E|Alemanha|1 - 2|Japão":"İlkay Gündoğan 33' (pên.); Ritsu Doan 75'; Takuma Asano 83'",
  "2022|Grupo E|Espanha|7 - 0|Costa Rica":"Dani Olmo 11'; Marco Asensio 21'; Ferran Torres 31' (pên.), 54'; Gavi 74'; Carlos Soler 90'; Álvaro Morata 90+2'",
  "2022|Grupo E|Japão|0 - 1|Costa Rica":"Keysher Fuller 81'",
  "2022|Grupo E|Espanha|1 - 1|Alemanha":"Álvaro Morata 62'; Niclas Füllkrug 83'",
  "2022|Grupo E|Japão|2 - 1|Espanha":"Ritsu Doan 48'; Ao Tanaka 51'; Álvaro Morata 11'",
  "2022|Grupo E|Costa Rica|2 - 4|Alemanha":"Yeltsin Tejeda 58'; Juan Pablo Vargas 70'; Serge Gnabry 10'; Kai Havertz 73', 85'; Niclas Füllkrug 89'",
  "2022|Grupo F|Marrocos|0 - 0|Croácia":"-",
  "2022|Grupo F|Bélgica|1 - 0|Canadá":"Michy Batshuayi 44'",
  "2022|Grupo F|Bélgica|0 - 2|Marrocos":"Romain Saïss 73'; Zakaria Aboukhlal 90+2'",
  "2022|Grupo F|Croácia|4 - 1|Canadá":"Andrej Kramarić 36', 70'; Marko Livaja 44'; Lovro Majer 90+4'; Alphonso Davies 2'",
  "2022|Grupo F|Croácia|0 - 0|Bélgica":"-",
  "2022|Grupo F|Canadá|1 - 2|Marrocos":"Nayef Aguerd 40' (contra); Hakim Ziyech 4'; Youssef En-Nesyri 23'",
  "2022|Grupo G|Suíça|1 - 0|Camarões":"Breel Embolo 48'",
  "2022|Grupo G|Brasil|2 - 0|Sérvia":"Richarlison 62', 73'",
  "2022|Grupo G|Camarões|3 - 3|Sérvia":"Jean-Charles Castelletto 29'; Vincent Aboubakar 63'; Eric Maxim Choupo-Moting 66'; Strahinja Pavlović 45+1'; Sergej Milinković-Savić 45+3'; Aleksandar Mitrović 53'",
  "2022|Grupo G|Brasil|1 - 0|Suíça":"Casemiro 83'",
  "2022|Grupo G|Sérvia|2 - 3|Suíça":"Aleksandar Mitrović 26'; Dušan Vlahović 35'; Xherdan Shaqiri 20'; Breel Embolo 44'; Remo Freuler 48'",
  "2022|Grupo G|Camarões|1 - 0|Brasil":"Vincent Aboubakar 90+2'",
  "2022|Grupo H|Uruguai|0 - 0|Coreia do Sul":"-",
  "2022|Grupo H|Portugal|3 - 2|Gana":"Cristiano Ronaldo 65' (pên.); João Félix 78'; Rafael Leão 80'; André Ayew 73'; Osman Bukari 89'",
  "2022|Grupo H|Coreia do Sul|2 - 3|Gana":"Cho Gue-sung 58', 61'; Mohammed Salisu 24'; Mohammed Kudus 34', 68'",
  "2022|Grupo H|Portugal|2 - 0|Uruguai":"Bruno Fernandes 54', 90+3' (pên.)",
  "2022|Grupo H|Gana|0 - 2|Uruguai":"Giorgian de Arrascaeta 26', 32'",
  "2022|Grupo H|Coreia do Sul|2 - 1|Portugal":"Kim Young-gwon 27'; Hwang Hee-chan 90+1'; Ricardo Horta 5'"
}


# --- Artilheiros por selecao em cada Copa (derivado dos marcadores das partidas) ---
_SC_JUNK = re.compile(r"(P[uú]blico|[AÁ]rbitro|Relat[oó]rio|Assist[eê]ncia|Est[aá]dio)", re.I)
_SC_OWNGOAL = re.compile(r"contra|gol\s*contra|g\.?\s*c\.?|\bog\b|autogol|auto-gol", re.I)
_SC_MIN_TOK = re.compile(r"^\d{1,3}(?:\+\d+)?['’](?:\([^)]*\))?[,;]?$")
_SC_MIN_QUAL = re.compile(r"['’]\(([^)]*)\)")
_SC_ALIASES = {"Rivellino": "Rivelino"}   # variantes de grafia da Wikipedia-PT


def _sc_norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z]", "", s.lower())


def _sc_merge_into(dst: dict, src: dict) -> None:
    for k, v in src.items():
        dst[k] = dst.get(k, 0) + v


def _sc_players(seg: str):
    """(gols, gols_contra) de um segmento de uma selecao — baseado em eventos.

    'gols' = {jogador: n} da propria selecao; 'gols_contra' = {autor: n} de gols
    contra a favor (marcados por adversario). Um minuto conta para o nome anterior;
    se vier antes de qualquer nome (formato invertido "67', 79' Ronaldo"), conta
    para o proximo.
    """
    m = _SC_JUNK.search(seg)
    seg = (seg[:m.start()] if m else seg).strip()
    if not seg:
        return {}, {}
    seg = seg.replace("<", " ").replace(">", " ")     # lixo da fonte (ex.: "25'<")
    seg = re.sub(r"\(([^)]*)\)", lambda m: "(" + re.sub(r"\s+", "", m.group(1)) + ")", seg)  # "(g. c.)" -> "(g.c.)"
    seg = re.sub(r"['’]{2,}", "'", seg)                # "73''" -> "73'"
    seg = re.sub(r"(\d)['’]\+(\d)", r"\1+\2", seg)     # "90'+4'" -> "90+4'"
    seg = re.sub(r"\s*\+\s*", "+", seg)
    seg = re.sub(r"['’]\s*\(", "'(", seg)              # cola qualificador ao minuto
    events, cur = [], []
    for tok in seg.split():
        if _SC_MIN_TOK.match(tok):
            if cur:
                events.append(("name", " ".join(cur).strip(" ,;.-"))); cur = []
            q = _SC_MIN_QUAL.search(tok)
            events.append(("min", bool(q and _SC_OWNGOAL.search(q.group(1)))))
            continue
        clean = tok.strip(" ,;.-")
        if clean.startswith("(") or not clean:
            continue
        cur.append(clean)
    if cur:
        events.append(("name", " ".join(cur).strip(" ,;.-")))
    players, own, lead, lead_og, last = {}, {}, 0, 0, None
    for kind, val in events:
        if kind == "name":
            name = _SC_ALIASES.get(val, val)
            players.setdefault(name, 0)
            if lead:
                players[name] += lead; lead = 0
            if lead_og:
                own[name] = own.get(name, 0) + lead_og; lead_og = 0
            last = name
        elif val:                    # gol contra (a favor desta selecao)
            if last is not None:
                own[last] = own.get(last, 0) + 1
            else:
                lead_og += 1
        else:                        # gol normal
            if last is not None:
                players[last] += 1
            else:
                lead += 1
    return ({k: v for k, v in players.items() if v > 0},
            {k: v for k, v in own.items() if v > 0})


def _sc_attribute(marc: str, t1: str, t2: str, placar):
    """({t1: gols, t2: gols}, {t1: golsContra, t2: golsContra}) por selecao."""
    n1, n2 = _sc_norm(t1), _sc_norm(t2)
    out_p = {t1: {}, t2: {}}
    out_og = {t1: {}, t2: {}}
    goals = score_goals(placar)
    g1, g2 = (goals[0], goals[1]) if goals else (None, None)
    unassigned = []
    for seg in (s.strip() for s in marc.split("|")):
        if not seg:
            continue
        tgt = None
        if ":" in seg:
            pref, rest = seg.split(":", 1)
            np = _sc_norm(pref)
            if np and (np == n1 or (len(np) > 3 and (np in n1 or n1 in np))):
                tgt = t1
            elif np and (np == n2 or (len(np) > 3 and (np in n2 or n2 in np))):
                tgt = t2
            if tgt:
                pl, og = _sc_players(rest)
                _sc_merge_into(out_p[tgt], pl); _sc_merge_into(out_og[tgt], og)
                continue
        pl, og = _sc_players(seg)
        if pl or og:
            unassigned.append((pl, og))
    if unassigned:
        if g1 == 0 and g2:
            targets = [t2] * len(unassigned)
        elif g2 == 0 and g1:
            targets = [t1] * len(unassigned)
        else:                       # ordem: 1o segmento -> t1, restante -> t2
            targets = [t1 if i == 0 else t2 for i in range(len(unassigned))]
        for (pl, og), tgt in zip(unassigned, targets):
            _sc_merge_into(out_p[tgt], pl); _sc_merge_into(out_og[tgt], og)
    return out_p, out_og


def _sc_merge_variants(d: dict) -> dict:
    """Mescla nomes que sao prefixo-de-palavra de EXATAMENTE um outro nome do grupo
    (ex.: 'Ronaldinho' -> 'Ronaldinho Gaúcho'), mantendo a forma mais completa."""
    names = list(d.keys())
    words = {n: n.split() for n in names}
    merged = dict(d)
    for a in names:
        if a not in merged:
            continue
        wa = words[a]
        supersets = [b for b in names if b != a and len(words[b]) > len(wa)
                     and words[b][:len(wa)] == wa]
        if len(supersets) == 1:
            merged[supersets[0]] = merged.get(supersets[0], 0) + merged.pop(a)
    return merged


# Gols de partidas que faltam no cache da Wikipedia PT (desempates/replays de 1934 e
# 1938, que nem constam na lista de jogos) e gols sem autor citado, complementados de
# outras fontes (Wikipedia EN / RSSSF / FIFA). {(selecao, ano): [[jogador, gols], ...]}
SCORERS_SUPPLEMENT: dict = {
    # 1934 — replay Itália 1-0 Espanha (1 jun): gol de Meazza
    ("Itália", 1934): [["Meazza", 1]],
    # 1970 — 2o gol de Valdivia (46') em México 4-0 El Salvador, ausente do marcador
    ("México", 1970): [["Valdivia", 1]],
}

# Gols contra a favor que a Wikipedia PT nao registrou de forma parseavel.
# {(selecao, ano): [[autor_adversario, gols], ...]}
OWNGOALS_SUPPLEMENT: dict = {
    ("Inglaterra", 2006): [["Gamarra", 1]],   # Gamarra (PAR); marcador malformado na fonte
}

# Gols contra que a Wikipedia PT listou SEM o marcador "(g.c.)" — o parser os contou
# como gol do jogador (que na verdade e adversario). Reclassificados para gol contra
# conforme a lista oficial de gols contra em Copas. (ano, selecao_beneficiada, autor).
RECLASSIFY_OWNGOALS = [
    (1954, "Bélgica", "Dickinson"), (1954, "França", "Cárdenas"),
    (1954, "Alemanha", "Horvat"), (1954, "Áustria", "Cruz"),
    (1970, "Itália", "Guzmán"), (1986, "União Soviética", "Dajka"),
    (2014, "Croácia", "Marcelo"), (2014, "França", "Valladares"),
    (2014, "Argentina", "Kolašinac"), (2014, "Portugal", "Boye"),
    (2014, "França", "Yobo"),
]


def build_team_scorers(cups: list[dict]):
    """({sel: {ano: [[jogador, gols]]}}, {sel: {ano: [[autor_gc, gols]]}}).

    O primeiro dict e a artilharia da selecao por Copa; o segundo, os gols contra
    a favor (marcados por adversarios) — creditados a selecao, mas nao a um artilheiro.
    """
    acc: dict = {}
    acc_og: dict = {}
    for cup in cups:
        ano = cup["ano"]
        for p in cup["partidas"]:
            marc = (p.get("marcadores") or "").strip()
            if not marc or marc == "-":
                continue
            out_p, out_og = _sc_attribute(marc, p.get("time1"), p.get("time2"), p.get("placar"))
            for team, players in out_p.items():
                if team and players:
                    _sc_merge_into(acc.setdefault(team, {}).setdefault(ano, {}), players)
            for team, og in out_og.items():
                if team and og:
                    _sc_merge_into(acc_og.setdefault(team, {}).setdefault(ano, {}), og)
    for ano, team, autor in RECLASSIFY_OWNGOALS:   # move gol contra mal-rotulado
        d = acc.get(team, {}).get(ano)
        if not d:
            continue
        ns = _sc_norm(autor)
        key = next((k for k in d if _sc_norm(k) == ns or ns in _sc_norm(k) or _sc_norm(k) in ns), None)
        if key is None:
            continue
        d[key] -= 1
        if d[key] <= 0:
            del d[key]
        dg = acc_og.setdefault(team, {}).setdefault(ano, {})
        dg[key] = dg.get(key, 0) + 1
    for (team, ano), extra in SCORERS_SUPPLEMENT.items():
        d = acc.setdefault(team, {}).setdefault(ano, {})
        for name, n in extra:
            d[name] = d.get(name, 0) + n
    for (team, ano), extra in OWNGOALS_SUPPLEMENT.items():
        d = acc_og.setdefault(team, {}).setdefault(ano, {})
        for name, n in extra:
            d[name] = d.get(name, 0) + n
    scorers: dict = {}
    for team, byyear in acc.items():
        scorers[team] = {}
        for ano in sorted(byyear):
            rows = sorted(_sc_merge_variants(byyear[ano]).items(), key=lambda kv: (-kv[1], kv[0].lower()))
            scorers[team][str(ano)] = [[k, v] for k, v in rows]
    owngoals: dict = {}
    for team, byyear in acc_og.items():
        owngoals[team] = {}
        for ano in sorted(byyear):
            rows = sorted(byyear[ano].items(), key=lambda kv: (-kv[1], kv[0].lower()))
            owngoals[team][str(ano)] = [[k, v] for k, v in rows]
    return scorers, owngoals


def _cup_team_stats(cup: dict) -> dict:
    """{selecao: {gp, gc, j, pos}} de uma edicao. Copas concluidas: da classificacao
    final; 2026 (em andamento): agregado dos jogos ja disputados."""
    out: dict = {}
    if cup["ano"] != 2026:
        for r in cup.get("classificacao_final") or []:
            t = r.get("selecao")
            if t:
                out[t] = {"gp": to_int(r.get("gp")), "gc": to_int(r.get("gc")),
                          "j": to_int(r.get("j")), "pos": to_int(r.get("pos")) or None}
        return out
    for p in cup["partidas"]:
        goals = score_goals(p.get("placar"))
        if not goals:
            continue
        for t, gf, ga in ((p.get("time1"), goals[0], goals[1]), (p.get("time2"), goals[1], goals[0])):
            if not t:
                continue
            s = out.setdefault(t, {"gp": 0, "gc": 0, "j": 0, "pos": None})
            s["gp"] += gf; s["gc"] += ga; s["j"] += 1
    return out


def build_best_atk_def(cups: list[dict]) -> dict:
    """{ano: {ataque:{selecao,gp}, defesa:{selecao,gc,j}}}: melhor ataque = seleção que
    mais marcou; melhor defesa = menor media de gols sofridos por jogo, entre as que
    passaram da fase de grupos (>= 4 jogos)."""
    out: dict = {}
    for cup in cups:
        stats = [(t, s) for t, s in _cup_team_stats(cup).items() if s["j"] > 0]
        if not stats:
            continue
        atk = max(stats, key=lambda ts: (ts[1]["gp"], -ts[1]["gc"], -(ts[1]["pos"] or 99)))
        elig = [ts for ts in stats if ts[1]["j"] >= 4] or stats
        dfn = min(elig, key=lambda ts: (ts[1]["gc"] / ts[1]["j"], ts[1]["gc"], -ts[1]["j"], ts[1]["pos"] or 99))
        out[str(cup["ano"])] = {
            "ataque": {"selecao": atk[0], "gp": atk[1]["gp"]},
            "defesa": {"selecao": dfn[0], "gc": dfn[1]["gc"], "j": dfn[1]["j"]},
        }
    return out


# --- Detalhes das partidas (escalacoes, tecnicos, arbitro, publico) -----------------
_DET_POS_RE = re.compile(r"^[A-Za-z]{1,3}$")


def _det_pages_for_year(year: int) -> list[str]:
    if year == 1930:
        return [
            "Copa_do_Mundo_FIFA_de_1930",
            "Copa_do_Mundo_FIFA_de_1930_-_Grupo_1",
            "Copa_do_Mundo_FIFA_de_1930_-_Grupo_2",
            "Copa_do_Mundo_FIFA_de_1930_-_Grupo_4",
            "Copa_do_Mundo_FIFA_de_1930_-_Fase_final",
            "Final_da_Copa_do_Mundo_FIFA_de_1930",
        ]
    if year in {1934, 1938}:
        return [f"Copa_do_Mundo_FIFA_de_{year}", f"Final_da_Copa_do_Mundo_FIFA_de_{year}"]
    sep = "-" if year <= 2006 else "–"
    if year in {1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002}:
        return [f"Copa_do_Mundo_FIFA_de_{year}", f"Final_da_Copa_do_Mundo_FIFA_de_{year}"]
    if year == 2006:
        return [
            "Copa_do_Mundo_FIFA_de_2006",
            *[f"Copa_do_Mundo_FIFA_de_2006_-_Grupo_{letter}" for letter in "ABCDEFGH"],
            "Final_da_Copa_do_Mundo_FIFA_de_2006",
            "Copa_do_Mundo_FIFA_de_2006_–_Fase_final",
        ]
    pages = []
    pages += [f"Copa_do_Mundo_FIFA_de_{year}_{sep}_Grupo_{letter}" for letter in "ABCDEFGH"]
    if year in {1998, 2002, 2006, 2010, 2014, 2018, 2022}:
        pages.append(f"Copa_do_Mundo_FIFA_de_{year}_{sep}_Fase_final")
    if year == 2022:
        pages.append("Final_da_Copa_do_Mundo_FIFA_de_2022")
    return pages


def _det_txt(el) -> str:
    return re.sub(r"\s+", " ", el.text_content()).strip()


def _det_count_player_rows(t) -> int:
    n = 0
    for tr in t.xpath("./tbody/tr | ./tr"):
        tds = tr.xpath("./td")
        if len(tds) >= 3 and _det_txt(tds[1]).isdigit() and _DET_POS_RE.match(_det_txt(tds[0])):
            n += 1
    return n


def _det_parse_lineup(table) -> dict:
    team = {"tec": "", "xi": [], "res": []}
    mode = "xi"; expect_coach = False
    for tr in table.xpath("./tbody/tr | ./tr"):
        cells = [_det_txt(c) for c in tr.xpath("./td")]
        if expect_coach:
            full = " ".join(c for c in cells if c).strip()
            if full:
                team["tec"] = full; expect_coach = False
            continue
        if not cells:
            continue
        if len(cells) == 1 and "Substi" in cells[0]:      # aceita typo "Substiuições"
            mode = "res"; continue
        if "Treinador" in " ".join(cells):
            expect_coach = True; continue
        if len(cells) >= 3 and cells[1].isdigit() and _DET_POS_RE.match(cells[0]):
            nome = re.sub(r"\s+\d{1,3}(?:\+\d+)?'.*$", "", cells[2]).strip()
            team["xi" if mode == "xi" else "res"].append([cells[1], cells[0], nome])
    return team


def _det_known_teams() -> set[str]:
    teams = set()
    for line in re.findall(r"FLAG_CODES[^\n]*", HTML):
        for name in re.findall(r'"([^"]+)":"[a-z]{2}(?:-[a-z]{3})?"', line):
            teams.add(clean_team(name))
    return teams


def _det_parse_scorebox(t) -> dict:
    txt = _det_txt(t)
    known = _det_known_teams()
    link_teams = []
    for a in t.xpath(".//a"):
        name = clean_team(_det_txt(a))
        if name in known and name not in link_teams:
            link_teams.append(name)
    alts = [img.get("alt") for img in t.xpath(".//img") if img.get("alt")]
    flags = [a for a in alts if not a.lower().startswith("gol") and "cart" not in a.lower()]
    teams = link_teams[:2] if len(link_teams) >= 2 else [clean_team(x) for x in flags[:2]]
    def _find(pat, grp=0):
        m = re.search(pat, txt)
        return (m.group(grp) if m else "").strip()
    pub = re.search(r"P[uú]blico:\s*([\d\s.]+?)(?:[A-ZÁ]|$)", txt)
    arb = re.search(r"[AÁ]rbitro:\s*(?:[A-Z]{2,3}\s+)?(.+?)(?:\s*\(|$)", txt)
    est = re.search(r"(Est[aá]dio[^\d]+?)(?:\d|Relat|P[uú]blico|$)", txt)
    sc = re.search(r"(\d+)\s*[–\-]\s*(\d+)", txt)
    sc = score_goals(txt)
    return {
        "times": teams, "arbitro_pais": clean_team(flags[-1]) if len(flags) > 2 else "",
        "data": _find(r"\d{1,2}(?:º)?\s+de\s+\w+"), "hora": _find(r"\b(\d{1,2}:\d{2})\b", 1),
        "estadio": est.group(1).strip(" ,") if est else "",
        "publico": re.sub(r"\s+", " ", pub.group(1)).strip() if pub else "",
        "arbitro": arb.group(1).strip() if arb else "",
        "score": list(sc) if sc else None,
    }


def _det_parse_page(path) -> list:
    doc = lxml_html.parse(str(path)).getroot()
    seq = []
    for t in doc.iter("table"):
        pr = _det_count_player_rows(t)
        data_mw = (t.get("data-mw") or "").lower()
        if pr >= 8:
            seq.append(("lineup", t))
        elif pr == 0 and ("Público:" in t.text_content() or "footballbox" in data_mw) and re.search(r"\d{1,2}(?:º)?\s+de\s+\w+", t.text_content()):
            seq.append(("score", t))
    groups, cur = [], None
    for kind, t in seq:
        if kind == "score":
            cur = {"sb": t, "lus": []}; groups.append(cur)
        elif cur is not None and len(cur["lus"]) < 2:
            cur["lus"].append(t)
    out = []
    for gm in groups:
        sb = _det_parse_scorebox(gm["sb"])
        lus = gm["lus"]
        sb["t1"] = _det_parse_lineup(lus[0]) if len(lus) >= 1 else {"tec": "", "xi": [], "res": []}
        sb["t2"] = _det_parse_lineup(lus[1]) if len(lus) >= 2 else {"tec": "", "xi": [], "res": []}
        out.append(sb)
    return out


def _det_keyn(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return "".join(ch for ch in s.lower() if ch.isalnum())


def det_pair_key(a: str, b: str, score) -> str:
    tk = "~".join(sorted([_det_keyn(clean_team(a)), _det_keyn(clean_team(b))]))
    sk = "-".join(str(x) for x in sorted(score)) if score else "?"
    return f"{tk}|{sk}"


def _det_empty_team(name: str) -> dict:
    return {"nome": clean_team(name), "tec": "", "xi": [], "res": []}


def _det_entry_from_match(match: dict) -> dict:
    return {
        "data": match.get("data", ""),
        "hora": "",
        "estadio": match.get("estadio", ""),
        "publico": "",
        "arbitro": "",
        "arbitro_pais": "",
        "t1": _det_empty_team(match.get("time1", "")),
        "t2": _det_empty_team(match.get("time2", "")),
    }


def _build_match_details_for_year(year: int) -> dict:
    det: dict = {}
    for title in _det_pages_for_year(year):
        try:
            path = fetch_page(title)
        except Exception as exc:  # noqa: BLE001
            print(f"Detalhes: pagina nao carregada {title} ({exc})")
            continue
        for m in _det_parse_page(path):
            tms = m.get("times") or []
            if len(tms) < 2:
                continue
            m["t1"]["nome"], m["t2"]["nome"] = tms[0], tms[1]
            entry = {k: m[k] for k in ("data", "hora", "estadio", "publico", "arbitro", "arbitro_pais")}
            entry["t1"], entry["t2"] = m["t1"], m["t2"]
            k = det_pair_key(tms[0], tms[1], m.get("score"))
            old = det.get(k)
            if old and len(old["t1"]["xi"]) >= len(m["t1"]["xi"]) and old.get("arbitro"):
                for f in ("publico", "arbitro", "arbitro_pais", "hora", "estadio"):
                    if not old.get(f) and entry.get(f):
                        old[f] = entry[f]
                continue
            det[k] = entry
    for match in parse_worldcup_page(year)["partidas"]:
        key = det_pair_key(match.get("time1"), match.get("time2"), score_goals(match.get("placar")))
        det.setdefault(key, _det_entry_from_match(match))
    coach = {}
    for e in det.values():
        for side in ("t1", "t2"):
            if e[side]["tec"]:
                coach[_det_keyn(clean_team(e[side]["nome"]))] = e[side]["tec"]
    for e in det.values():
        for side in ("t1", "t2"):
            if not e[side]["tec"]:
                e[side]["tec"] = coach.get(_det_keyn(clean_team(e[side]["nome"])), "")
    return det


def build_match_details() -> dict:
    """{ano: {pair_key: detalhe}} — escalacoes/tecnicos/arbitro/publico por partida."""
    return {str(year): _build_match_details_for_year(year) for year in (1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022)}


def load_detailed_goals() -> dict:
    if GOLS_DETALHADOS_FILE.exists():
        return json.loads(GOLS_DETALHADOS_FILE.read_text(encoding="utf-8"))
    return {
        "fonte": {
            "nome": "StatsBomb Open Data",
            "url": "https://github.com/statsbomb/open-data",
            "observacao": "Execute gerar_gols_detalhados_statsbomb.py para gerar a base detalhada de gols.",
        },
        "cobertura": [],
        "gols": [],
    }


def load_analytic_goals() -> dict:
    if GOLS_ANALITICOS_FILE.exists():
        return json.loads(GOLS_ANALITICOS_FILE.read_text(encoding="utf-8"))
    return {"metadata": {"descricao": "Execute gerar_base_analitica_gols.py para gerar a base analitica de gols."}, "gols": [], "auditoria": []}


def build_payload() -> dict:
    main = parse_main()
    cups = [parse_worldcup_page(year) for year in YEARS]
    total_matches = sum(len(cup["partidas"]) for cup in cups)
    total_goals = sum(sum(to_int(match.get("gols")) for match in cup["partidas"]) for cup in cups)
    main["totals"] = {
        "Total de jogos": f"{total_matches:,}".replace(",", "."),
        "Total de gols": f"{total_goals:,}".replace(",", "."),
        "Média": f"{(total_goals / total_matches):.2f}".replace(".", ",") + " gols por partida" if total_matches else "0",
        "Observação": "Totais recalculados a partir das páginas das 22 edições realizadas (1930-2022).",
    }
    # detalhes de partidas (escalacoes etc.) anexados diretamente em cada partida
    detalhes = build_match_details()
    for cup in cups:
        dd = detalhes.get(str(cup["ano"]))
        if not dd:
            continue
        for p in cup["partidas"]:
            key = det_pair_key(p.get("time1"), p.get("time2"), score_goals(p.get("placar")))
            if key in dd:
                p["ficha"] = dd[key]
    selections = aggregate_selection_stats(main, cups)
    scorers, owngoals = build_team_scorers(cups)
    return {
        "fonte": {
            "principal": BASE + MAIN_TITLE,
            "acesso": "Wikipedia em português; HTML em cache local no momento da geração.",
        },
        "geral": main,
        "copas": cups,
        "selecoes": selections,
        "artilheiros_selecao": scorers,
        "gols_contra_selecao": owngoals,
        "gols_detalhados": load_detailed_goals(),
        "gols_analiticos": load_analytic_goals(),
        "melhor_ataque_defesa": build_best_atk_def(cups),
        "curados": {
            "artilheiros_historico": ARTILHEIROS_HISTORICO,
            "artilheiros_edicao": ARTILHEIROS_EDICAO,
            "marcadores_grupos": MARCADORES_GRUPOS,
        },
    }


HTML = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Copa do Mundo FIFA</title>
<link rel="icon" type="image/png" href="__FAVICON_PAYLOAD__" />
<script>__PLOTLY_PAYLOAD__</script>
<style>
:root{--bg:#07130f;--panel:#0e2119;--panel2:#132c21;--line:#254536;--text:#f4fff8;--muted:#9eb8a8;--grass:#22c55e;--gold:#f5c451;--blue:#38bdf8;--red:#fb7185;--shadow:0 18px 50px rgba(0,0,0,.32)}
*{box-sizing:border-box} body{margin:0;min-height:100vh;color:var(--text);font-family:Inter,Segoe UI,Roboto,Arial,sans-serif;background:linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px) 0 0/82px 82px,radial-gradient(circle at 18% 0%,rgba(34,197,94,.16),transparent 36%),linear-gradient(180deg,#06100d,#081812 44%,#06100d)}
a{color:var(--blue)} .hero{min-height:245px;border-bottom:1px solid rgba(255,255,255,.12);display:grid;grid-template-columns:minmax(0,1.25fr) minmax(310px,.75fr);gap:22px;align-items:end;padding:34px 28px;background:linear-gradient(135deg,rgba(7,19,15,.96),rgba(7,19,15,.76)),repeating-linear-gradient(90deg,rgba(34,197,94,.24) 0 70px,rgba(16,185,129,.11) 70px 140px)}
.hero h1{margin:0;font-size:clamp(34px,5vw,66px);line-height:.96;letter-spacing:0}.hero p{margin:14px 0 0;max-width:880px;color:var(--muted);font-size:17px;line-height:1.55}.hero-meta{display:grid;gap:9px;padding:0}#hero-cartaz{display:grid;gap:8px;justify-items:center}#cartaz-img{max-height:210px;max-width:100%;border-radius:6px;border:1px solid rgba(255,255,255,.16);background:#fff;padding:6px}#cartaz-legenda{text-align:center}
#hero-trofeus{display:grid;gap:10px}.trofeus-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;align-items:end}.trofeus-grid figure{margin:0;display:grid;gap:6px;justify-items:center}.trofeus-grid img{height:185px;width:auto;max-width:100%;filter:drop-shadow(0 6px 12px rgba(0,0,0,.4))}.trofeus-grid figcaption{text-align:center;font-size:11px;color:var(--muted);line-height:1.3}.trofeus-grid figcaption b{display:block;color:var(--text);font-size:13px}
#hero-bandeira{display:grid;gap:9px;justify-items:center}.hero-flag-img{width:160px;max-width:100%;border:1px solid rgba(255,255,255,.22);border-radius:5px;box-shadow:0 6px 16px rgba(0,0,0,.45)}#hero-bandeira strong,#hero-trofeus strong{justify-self:start}
#hero-trofeus.hidden,#hero-cartaz.hidden,#hero-bandeira.hidden{display:none}.pill-row{display:flex;gap:8px;flex-wrap:wrap;margin-top:18px}.pill{border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.07);padding:7px 10px;border-radius:999px;font-size:12px}
.nav{position:sticky;top:0;z-index:20;display:flex;gap:8px;flex-wrap:wrap;padding:14px 28px;background:rgba(7,19,15,.94);backdrop-filter:blur(14px);border-bottom:1px solid rgba(255,255,255,.1)}.nav button{color:var(--text);background:#10251c;border:1px solid var(--line);border-radius:8px;padding:10px 13px;cursor:pointer}.nav button.active{background:var(--grass);color:#03140b;border-color:var(--grass);font-weight:800}
.shell{max-width:1480px;margin:0 auto;padding:22px}.toolbar{display:grid;grid-template-columns:repeat(4,minmax(170px,1fr));gap:12px;margin-bottom:18px}label{display:grid;gap:6px;color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.08em}select,input{width:100%;min-height:40px;color:var(--text);background:#0b1b15;border:1px solid var(--line);border-radius:8px;padding:0 10px;outline:none}
.kpis{display:grid;grid-template-columns:repeat(6,minmax(130px,1fr));gap:12px;margin:0 0 14px}.kpi{background:linear-gradient(180deg,rgba(19,44,33,.98),rgba(11,27,21,.98));border:1px solid var(--line);border-radius:8px;padding:14px;box-shadow:var(--shadow)}.kpi b{display:block;font-size:27px;line-height:1.1}.kpi span{display:block;color:var(--muted);font-size:12px;margin-top:6px}
.grid{display:grid;grid-template-columns:repeat(12,1fr);gap:14px}.card{background:linear-gradient(180deg,rgba(19,44,33,.96),rgba(9,23,18,.96));border:1px solid var(--line);border-radius:8px;padding:14px;box-shadow:var(--shadow);min-width:0}.span-3{grid-column:span 3}.span-4{grid-column:span 4}.span-5{grid-column:span 5}.span-6{grid-column:span 6}.span-7{grid-column:span 7}.span-8{grid-column:span 8}.span-12{grid-column:span 12}.card h2,.card h3{margin:0 0 12px;font-size:16px;letter-spacing:0}.chart{width:100%;height:380px}.chart.small{height:295px}.chart.ranking-all{height:1480px}.chart-scroll{height:440px;overflow-y:auto;overflow-x:hidden;border:1px solid var(--line);border-radius:8px;background:rgba(7,19,15,.35)}.chart-scroll-x{overflow-x:auto;overflow-y:hidden}.card-head{display:flex;justify-content:space-between;align-items:center;gap:10px;margin:0 0 12px}.card-head h2{margin:0}.rank-toggle{color:var(--text);background:#10251c;border:1px solid var(--line);border-radius:6px;padding:5px 10px;font-size:11px;cursor:pointer;white-space:nowrap}.rank-toggle:hover{border-color:var(--grass)}.rank-list{display:grid;gap:6px;padding:6px 6px 6px 4px}.rank-row{display:grid;grid-template-columns:142px 1fr 48px;align-items:center;gap:9px;font-size:13px}.rank-label{min-width:0;overflow:hidden}.rank-label .inline-flag{width:26px;height:18px}.rank-bar-wrap{height:18px;background:rgba(255,255,255,.06);border-radius:4px;overflow:hidden}.rank-bar{height:100%;border-radius:4px;min-width:2px}.rank-val{text-align:right;font-variant-numeric:tabular-nums;color:var(--text)}.rank-row:hover{background:rgba(255,255,255,.05);border-radius:4px}.goal-rank{height:100%}.goal-rank .rank-row{grid-template-columns:minmax(160px,1.4fr) minmax(120px,2fr) 48px}.goal-rank .rank-label{white-space:nowrap;text-overflow:ellipsis}.rank-tip{position:fixed;z-index:60;pointer-events:none;background:#0b1b15;border:1px solid var(--line);border-radius:6px;padding:6px 10px;font-size:12px;color:var(--text);box-shadow:var(--shadow);white-space:nowrap;opacity:0;transition:opacity .08s;left:0;top:0}.rank-tip.show{opacity:1}.podium-legend{display:flex;flex-wrap:wrap;gap:12px;margin:0 0 10px;font-size:11px;color:var(--muted)}.podium-legend span{display:inline-flex;align-items:center;gap:5px}.podium-legend i{width:11px;height:11px;border-radius:2px;display:inline-block}.podium-bar{display:flex;height:100%;border-radius:4px;overflow:hidden;min-width:2px}.podium-seg{height:100%}
.timeline{--row-h:242px;--line-y:112px;position:relative;display:grid;gap:0;overflow:visible;padding:0 48px}.timeline-desktop{position:relative}.timeline-mobile{display:none}.timeline-path{position:absolute;left:48px;right:48px;top:0;height:100%;width:calc(100% - 96px);z-index:1;overflow:visible;pointer-events:none}.timeline-path path{fill:none;stroke:var(--gold);stroke-width:8;stroke-linecap:round;stroke-linejoin:round}.timeline-row{position:relative;display:grid;grid-template-columns:repeat(8,minmax(108px,1fr));min-height:var(--row-h);overflow:visible;z-index:2}.cup-card{position:relative;min-height:230px;padding:0 7px;cursor:pointer}.cup-card::before{content:"";position:absolute;left:50%;top:var(--line-y);width:13px;height:13px;transform:translate(-50%,-4px);border-radius:50%;background:var(--text);box-shadow:0 0 0 5px rgba(245,196,81,.24);z-index:4}.cup-card.active::before{background:var(--grass);box-shadow:0 0 0 6px rgba(34,197,94,.28)}.cup-card.active .event-box{border-color:var(--grass);background:rgba(34,197,94,.1)}.event-box{position:absolute;left:5px;right:5px;border:1px solid rgba(255,255,255,.11);background:rgba(11,27,21,.96);border-radius:8px;padding:8px 9px;min-height:58px;z-index:5}.cup-card.above .event-box{bottom:150px}.cup-card.below .event-box{top:154px}.event-year,.event-winner{display:block;font-size:14px;font-weight:400;color:var(--text);line-height:1.22}.event-host{display:block;color:var(--muted);font-size:11px;margin-top:3px;line-height:1.25}.event-stem{position:absolute;left:50%;top:calc(var(--line-y) + 8px);width:2px;height:34px;background:var(--gold);opacity:.78;z-index:3}.cup-card.above .event-stem{top:auto;bottom:142px;height:34px}
.table-wrap{overflow:auto;max-height:360px;border:1px solid var(--line);border-radius:8px}table{width:100%;border-collapse:collapse;font-size:13px}th,td{padding:9px 10px;border-bottom:1px solid rgba(255,255,255,.08);text-align:left;white-space:nowrap}th{position:sticky;top:0;z-index:1;background:#10251c;color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.07em}td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}.hidden{display:none}.note{color:var(--muted);font-size:12px;line-height:1.45;margin-top:10px}.scorers-wrap{display:grid;gap:2px}.ts-cup{display:grid;grid-template-columns:154px 1fr;gap:14px;align-items:start;padding:11px 2px;border-top:1px solid var(--line)}.ts-cup:first-child{border-top:0}.ts-head{display:flex;flex-direction:column;gap:4px}.ts-year{font-size:19px;font-weight:800;line-height:1}.ts-fin{font-size:11px;font-weight:700;color:var(--muted)}.ts-fin.r1{color:var(--gold)}.ts-fin.r2{color:#cbd5e1}.ts-fin.r3{color:#cd7f32}.ts-total{font-size:11px;color:var(--muted);font-variant-numeric:tabular-nums}.ts-body{display:grid;gap:7px;min-width:0}.ts-players{display:flex;flex-wrap:wrap;gap:6px;padding-top:1px}.ts-chip{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.06);border:1px solid var(--line);border-radius:999px;padding:4px 11px;font-size:12.5px}.ts-chip b{color:var(--gold);font-variant-numeric:tabular-nums}.ts-chip.top{border-color:rgba(245,196,81,.55);background:rgba(245,196,81,.12)}.ts-none{color:var(--muted);font-style:italic;font-size:12.5px}.ts-og{font-size:11.5px;color:var(--muted);line-height:1.4;border-left:2px solid rgba(251,113,133,.5);padding-left:9px}.ts-og b{color:#fca5b5;font-weight:700}.ts-og span{opacity:.8}.ad-num{font-weight:700;font-variant-numeric:tabular-nums;white-space:nowrap;margin-left:5px}.ad-atk{color:var(--gold)}.ad-def{color:var(--blue)}#tbl-atkdef td{white-space:nowrap}.phase-stack{display:grid;gap:12px}.phase-title{display:flex;justify-content:space-between;gap:12px;color:var(--gold);font-weight:800}.groups-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.group-block{border:1px solid var(--line);border-radius:8px;padding:12px;background:rgba(7,19,15,.36);min-width:0}.group-block .table-wrap{max-height:none}.group-section-title{margin:12px 0 8px;color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.07em}.qualified-row{background:rgba(34,197,94,.13)}.qualified-row td:nth-child(2){color:var(--grass);font-weight:800}.knockout-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.match-card{border:1px solid var(--line);border-radius:8px;background:rgba(7,19,15,.42);padding:12px;display:grid;gap:9px;cursor:pointer}.match-meta{display:flex;justify-content:space-between;gap:10px;color:var(--muted);font-size:12px}.scoreline{display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);gap:10px;align-items:center}.scoreline strong{font-size:15px;line-height:1.25}.scoreline .right{text-align:right}.score{color:var(--gold);font-size:18px;font-weight:800;font-variant-numeric:tabular-nums}.winner{color:var(--grass)}.match-detail{color:var(--muted);font-size:12px;line-height:1.45;white-space:normal}.format-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}.format-card{border:1px solid var(--line);border-radius:8px;padding:12px;background:rgba(7,19,15,.42)}.format-card strong{display:block;font-size:18px;margin-bottom:6px}.format-card span{display:block;color:var(--muted);font-size:12px;line-height:1.35}.format-note{border:1px solid rgba(245,196,81,.38);background:rgba(245,196,81,.08);border-radius:8px;padding:12px;color:#ffe49a;line-height:1.45}.legacy-groups{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.match-card.selected-match{border-color:var(--gold);background:rgba(245,196,81,.1)}.match-row{cursor:pointer}.match-row.selected-match td{background:rgba(245,196,81,.11)}.match-detail-panel{display:grid;gap:14px}.detail-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}.detail-card{border:1px solid var(--line);border-radius:8px;padding:12px;background:rgba(7,19,15,.42)}.detail-card b{display:block;font-size:20px}.detail-card span{display:block;color:var(--muted);font-size:12px;margin-top:5px}.selected-game{border:1px solid rgba(245,196,81,.42);border-radius:8px;padding:14px;background:rgba(245,196,81,.07)}.selected-game .scoreline{margin:8px 0}.scorers-box{border-top:1px solid rgba(255,255,255,.09);padding-top:10px;color:var(--muted);line-height:1.5;white-space:normal}
.game-scoreboard{border:1px solid rgba(255,255,255,.12);border-radius:8px;padding:18px 20px;background:linear-gradient(180deg,rgba(20,20,22,.96),rgba(16,16,18,.96));box-shadow:var(--shadow)}.game-top{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:14px;color:#d1d5db;font-size:15px}.game-status{color:#f4fff8;font-weight:800}.game-main{display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);gap:28px;align-items:center;margin:22px 0 12px}.game-team{text-align:center;display:grid;gap:10px;justify-items:center}.team-badge{width:58px;height:40px;border:2px solid rgba(255,255,255,.72);border-radius:5px;display:grid;place-items:center;background:linear-gradient(90deg,rgba(255,255,255,.2),rgba(255,255,255,.06));font-weight:900;color:#fff;overflow:hidden}.flag-img{width:100%;height:100%;object-fit:cover;display:block}.team-label{display:inline-flex;align-items:center;gap:7px;min-width:0}.inline-flag{width:22px;height:15px;object-fit:cover;border:1px solid rgba(255,255,255,.35);border-radius:2px;flex:0 0 auto}.game-team b{font-size:19px}.game-score{display:grid;grid-template-columns:auto auto auto;gap:26px;align-items:center;font-size:42px;font-weight:800;font-variant-numeric:tabular-nums}.game-score span:nth-child(2){color:#9ca3af;font-size:30px}.game-phase{text-align:center;color:#aeb7c2;margin-bottom:20px}.goal-timeline{display:grid;gap:8px;color:#b8c2cc}.goal-event{display:grid;grid-template-columns:minmax(0,1fr) 66px minmax(0,1fr);gap:12px;align-items:center}.goal-event .minute{text-align:center;color:var(--gold);font-weight:800;font-variant-numeric:tabular-nums}.goal-event .left{text-align:left}.goal-event .right{text-align:right}.goal-event .blank{min-height:1px}.group-match-detail{margin-top:12px}.group-match-detail .game-scoreboard{box-shadow:none}.game-extra{border-top:1px solid rgba(255,255,255,.1);margin-top:16px;padding-top:10px;color:#9ca3af;font-size:12px;line-height:1.45}
.game-detailbar{display:flex;justify-content:center;margin:14px 0 0}.game-details-btn{cursor:pointer;border:1px solid var(--grass);background:rgba(34,197,94,.14);color:#eafff2;font-weight:700;font-size:13px;padding:8px 20px;border-radius:999px;transition:background .12s}.game-details-btn:hover{background:rgba(34,197,94,.3)}
.modal-overlay{position:fixed;inset:0;z-index:100;background:rgba(3,8,6,.74);backdrop-filter:blur(4px);display:flex;align-items:flex-start;justify-content:center;padding:40px 16px;overflow-y:auto}.modal-overlay.hidden{display:none}.modal-box{position:relative;width:min(920px,100%);background:linear-gradient(180deg,#12241c,#0b1712);border:1px solid var(--line);border-radius:12px;box-shadow:0 30px 80px rgba(0,0,0,.6);padding:22px 24px 26px}.modal-close{position:absolute;top:10px;right:14px;background:none;border:none;color:#9eb8a8;font-size:30px;line-height:1;cursor:pointer;padding:0 6px}.modal-close:hover{color:#fff}
.mm-head{text-align:center;border-bottom:1px solid var(--line);padding-bottom:16px;margin-bottom:16px}.mm-teams{display:grid;grid-template-columns:1fr auto 1fr;gap:20px;align-items:center}.mm-team{display:grid;gap:8px;justify-items:center}.mm-team b{font-size:18px}.mm-team .team-badge,.mm-team .flag-img{width:56px;height:38px}.mm-score{font-size:34px;font-weight:800;font-variant-numeric:tabular-nums;display:flex;gap:12px;align-items:center}.mm-score span{color:#9ca3af;font-size:24px}.mm-sub{color:var(--muted);font-size:13px;margin-top:10px}
.mm-meta{display:grid;grid-template-columns:repeat(auto-fit,minmax(128px,1fr));gap:10px;margin-bottom:20px}.mm-meta-item{background:rgba(255,255,255,.05);border:1px solid var(--line);border-radius:8px;padding:9px 12px}.mm-meta-item span{display:block;color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.05em;margin-bottom:2px}.mm-meta-item b{font-size:14px}.mm-h3{margin:0 0 12px;font-size:15px;color:var(--gold)}
.mm-lineups{display:grid;grid-template-columns:1fr 1fr;gap:18px}.lu-team{min-width:0}.lu-head{font-weight:800;margin-bottom:10px;padding-bottom:8px;border-bottom:1px solid var(--line)}.lu-head .inline-flag{width:26px;height:18px}.lu-list{list-style:none;margin:0;padding:0;display:grid;gap:2px}.lu-list li{display:grid;grid-template-columns:26px 34px 1fr;gap:8px;align-items:center;padding:4px 6px;border-radius:4px;font-size:13px}.lu-list li:hover{background:rgba(255,255,255,.05)}.lu-num{text-align:right;color:var(--gold);font-variant-numeric:tabular-nums;font-weight:700}.lu-pos{color:var(--muted);font-size:11px;font-weight:700}.lu-name{display:inline;min-width:0}.goal-balls{display:inline-flex;gap:2px;align-items:center;margin-left:6px;vertical-align:-1px}.goal-ball{font-size:12px;line-height:1}.lu-res{opacity:.82}.lu-subhead{margin:11px 0 4px;color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.05em}.lu-coach{margin-top:12px;padding-top:10px;border-top:1px solid var(--line);display:flex;justify-content:space-between;gap:10px;font-size:13px}.lu-coach span{color:var(--muted)}
.goals-toolbar{grid-template-columns:repeat(2,minmax(180px,260px))}.goals-table{max-height:520px}
@media(max-width:720px){.mm-lineups{grid-template-columns:1fr}.mm-teams{gap:8px}.mm-team b{font-size:15px}}
.bracket-board{position:relative;overflow-x:auto;border:1px solid rgba(255,255,255,.15);border-radius:8px;padding:20px;background:radial-gradient(circle at 18% 72%,rgba(245,196,81,.18),transparent 24%),radial-gradient(circle at 82% 30%,rgba(34,197,94,.14),transparent 26%),linear-gradient(135deg,#123e8f,#162fa4 48%,#0d286e);box-shadow:inset 0 0 55px rgba(255,255,255,.06)}.bracket-head{text-align:center;margin-bottom:18px}.bracket-head b{display:block;font-size:clamp(28px,4vw,54px);line-height:.9;letter-spacing:.04em;text-transform:uppercase}.bracket-head span{display:block;margin-top:6px;color:#dbeafe;font-size:16px;font-weight:800;letter-spacing:.18em;text-transform:uppercase}.bracket-stage{display:grid;grid-template-columns:minmax(132px,1fr) minmax(132px,1fr) minmax(132px,1fr) minmax(150px,.86fr) minmax(132px,1fr) minmax(132px,1fr) minmax(132px,1fr);gap:18px;align-items:center;min-width:1080px}.bracket-col{display:grid;gap:16px}.bracket-col.r16{gap:9px}.bracket-col.qf{gap:54px}.bracket-col.sf{gap:126px}.bracket-col.right .bracket-match::before,.bracket-col.left .bracket-match::after{content:"";position:absolute;top:50%;width:18px;border-top:2px solid rgba(226,241,255,.72)}.bracket-col.left .bracket-match::after{right:-19px}.bracket-col.right .bracket-match::before{left:-19px}.bracket-center{display:grid;gap:14px;align-items:center;justify-items:center}.bracket-trophy{width:54px;height:54px;border-radius:50%;display:grid;place-items:center;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.25);font-size:13px;font-weight:900;letter-spacing:.04em}.bracket-final-label{color:#dbeafe;font-size:11px;text-transform:uppercase;letter-spacing:.14em}.bracket-match{position:relative;border:1px solid rgba(255,255,255,.22);border-radius:7px;background:rgba(5,17,48,.76);padding:7px;display:grid;gap:5px;cursor:pointer;min-height:64px}.bracket-match.selected-match{border-color:var(--gold);box-shadow:0 0 0 2px rgba(245,196,81,.25);background:rgba(9,31,78,.92)}.bracket-team{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:6px;align-items:center;font-size:12px;line-height:1.2}.bracket-team b{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.bracket-team span{color:var(--gold);font-weight:800;font-variant-numeric:tabular-nums}.bracket-team.winner b{color:#86efac}.bracket-meta{color:#dbeafe;font-size:10px;line-height:1.3;opacity:.82;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.bracket-third{width:100%;border-top:1px solid rgba(255,255,255,.14);padding-top:12px}.bracket-empty{min-height:28px}
@media(max-width:1100px){.hero,.toolbar{grid-template-columns:1fr 1fr}.kpis{grid-template-columns:repeat(3,1fr)}.span-3,.span-4,.span-5,.span-6,.span-7,.span-8{grid-column:span 12}.groups-grid,.legacy-groups,.knockout-grid{grid-template-columns:1fr}.format-grid,.detail-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.bracket-board{padding:16px}.bracket-stage{min-width:980px}}@media(max-width:720px){.hero,.toolbar{grid-template-columns:1fr;padding-left:14px;padding-right:14px}.shell{padding:14px}.kpis{grid-template-columns:1fr 1fr}.chart{height:330px}.format-grid,.detail-grid{grid-template-columns:1fr}.scoreline{grid-template-columns:1fr;gap:5px}.scoreline .right{text-align:left}.game-top{grid-template-columns:1fr}.game-main{grid-template-columns:1fr;gap:14px}.game-score{justify-content:center;font-size:34px}.game-scorers{grid-template-columns:1fr}.scorer-list.right{text-align:left}.scorer-ball{display:none}.bracket-head b{font-size:30px}.bracket-head span{font-size:12px}.timeline{--row-h:154px;--line-y:78px;padding:0 8px}.timeline-desktop{display:none}.timeline-mobile{display:block;position:relative;padding:8px 0 18px;overflow:visible}.timeline-mobile::before{display:none}.timeline-mobile-path{position:absolute;inset:8px 8px 18px 8px;width:calc(100% - 16px);height:calc(100% - 26px);z-index:1;overflow:visible;pointer-events:none}.timeline-mobile-path path{fill:none;stroke:var(--gold);stroke-width:7;stroke-linecap:round;stroke-linejoin:round}.timeline-mobile .timeline-row{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));min-height:var(--row-h);position:relative;z-index:2}.timeline-mobile .cup-card{min-height:var(--row-h);padding:0 5px}.timeline-mobile .cup-card::before{top:var(--line-y);left:50%;width:13px;height:13px;transform:translate(-50%,-50%)}.timeline-mobile .event-box{left:5px;right:5px;width:auto;min-height:48px;padding:7px 8px}.timeline-mobile .cup-card.above .event-box{bottom:96px}.timeline-mobile .cup-card.below .event-box{top:96px}.timeline-mobile .event-stem{left:50%;width:2px;height:16px;background:var(--gold);opacity:.9}.timeline-mobile .cup-card.above .event-stem{top:calc(var(--line-y) - 18px);bottom:auto}.timeline-mobile .cup-card.below .event-stem{top:calc(var(--line-y) + 8px)}.event-year,.event-winner{font-size:13px}.timeline-mobile .inline-flag{width:20px;height:14px}}
</style>
</head>
<body>
<header class="hero">
  <div>
    <h1>Copas do Mundo FIFA</h1>
    <p>Do primeiro apito em 1930 ao Catar 2022: quase um século de Copas do Mundo em um só lugar. Craques, gols e taças — mergulhe em cada edição, na história de cada seleção ou no panorama completo do maior espetáculo do futebol.</p>
  </div>
  <aside class="hero-meta"><div id="hero-trofeus"></div><div id="hero-cartaz" class="hidden"><img id="cartaz-img" alt="Cartaz da edição" /></div><div id="hero-bandeira" class="hidden"></div></aside>
</header>
<nav class="nav" id="nav"><button data-view="geral" class="active">Geral das Copas</button><button data-view="gols">Gols</button><button data-view="copa">Por Copa</button><button data-view="selecao">Por Seleção</button></nav>
<main class="shell">
  <section id="view-geral">
    <div class="kpis" id="kpis-geral"></div>
    <div class="grid">
      <article class="card span-12"><h2>Linha do tempo das edições</h2><div id="timeline-geral" class="timeline"></div></article>
      <article class="card span-12"><h2>Títulos por seleção</h2><div id="ch-titulos"></div></article>
      <article class="card span-12"><h2>Top 4 histórico</h2><div class="podium-legend" id="podium-legend"></div><div class="chart-scroll"><div id="ch-podium"></div></div></article>
      <article class="card span-4"><div class="card-head"><h2>Vitórias por seleção</h2><button class="rank-toggle" data-rank-toggle>Ver %</button></div><div class="chart-scroll"><div id="ch-ranking-vitorias"></div></div></article>
      <article class="card span-4"><div class="card-head"><h2>Empates por seleção</h2><button class="rank-toggle" data-rank-toggle>Ver %</button></div><div class="chart-scroll"><div id="ch-ranking-empates"></div></div></article>
      <article class="card span-4"><div class="card-head"><h2>Derrotas por seleção</h2><button class="rank-toggle" data-rank-toggle>Ver %</button></div><div class="chart-scroll"><div id="ch-ranking-derrotas"></div></div></article>
      <article class="card span-6"><h2>Gols e jogos por edição</h2><div id="ch-edicoes" class="chart"></div></article>
      <article class="card span-6"><h2>Público por edição</h2><div id="ch-publico" class="chart"></div></article>
      <article class="card span-12"><h2>Todas as edições</h2><div class="table-wrap"><table id="tbl-edicoes"></table></div></article>
      <article class="card span-12"><h2>Melhor ataque e defesa por edição</h2><div class="table-wrap"><table id="tbl-atkdef"></table></div><span class="note">Melhor ataque = seleção que mais marcou na edição. Melhor defesa = menor média de gols sofridos por jogo, entre as que passaram da fase de grupos (4+ jogos).</span></article>
      <article class="card span-6"><h2>Maiores artilheiros em Copas</h2><div id="ch-artilheiros-historico" class="chart"></div><span class="note">Inclui a Copa de 2026 em andamento: Mbappé (12&rarr;22) e Messi (13&rarr;21). Lista parcial &mdash; outros jogadores ativos podem subir até o fim do torneio.</span></article>
      <article class="card span-6"><h2>Artilheiro por edição</h2><div id="ch-artilheiros-edicao" class="chart"></div></article>
      <article class="card span-12"><h2>Maiores goleadas</h2><div class="table-wrap"><table id="tbl-goleadas"></table></div></article>
    </div>
  </section>

  <section id="view-gols" class="hidden">
    <div class="toolbar goals-toolbar">
      <label>Ano<select id="goal-year"></select></label>
      <label>Seleção<select id="goal-team"></select></label>
    </div>
    <div class="kpis" id="kpis-gols"></div>
    <div class="grid">
      <article class="card span-6"><h2>Gols por edição</h2><div id="ch-goals-edicao" class="chart small"></div></article>
      <article class="card span-6"><h2>Gols por seleção</h2><div class="chart-scroll chart-scroll-x"><div id="ch-goals-teams" class="chart"></div></div></article>
      <article class="card span-6"><h2>Gols por fase</h2><div id="ch-goals-phase" class="chart small"></div></article>
      <article class="card span-6"><h2>Gols/jogo por fase</h2><div id="ch-goals-phase-rate" class="chart small"></div></article>
      <article class="card span-6"><h2>Gols marcados, sofridos e saldo</h2><div class="chart-scroll"><div id="ch-goals-team-balance" class="chart"></div></div></article>
      <article class="card span-6"><h2>Médias por seleção</h2><div class="chart-scroll"><div id="ch-goals-team-averages" class="chart"></div></div></article>
      <article class="card span-6"><h2>Maiores artilheiros</h2><div class="chart-scroll"><div id="ch-goals-players" class="goal-rank"></div></div><span class="note">Lista todos os jogadores com pelo menos um gol na base filtrada.</span></article>
      <article class="card span-6"><h2>Artilheiro por Copa</h2><div class="chart-scroll"><div id="ch-goals-topscorers-edicao" class="goal-rank"></div></div><span class="note">Quando houve empate na artilharia, a edição aparece com todos os nomes consolidados na mesma barra.</span></article>
      <article class="card span-6"><h2>Gols em mata-mata por seleção</h2><div class="chart-scroll"><div id="ch-goals-ko-teams" class="goal-rank"></div></div></article>
      <article class="card span-6"><h2>Gols em mata-mata por jogador</h2><div class="chart-scroll"><div id="ch-goals-ko-players" class="goal-rank"></div></div></article>
      <article class="card span-6"><h2>Gols por faixa de minuto</h2><div id="ch-goals-minute" class="chart small"></div></article>
      <article class="card span-6"><h2>Todos os gols</h2><div class="table-wrap goals-table"><table id="tbl-goals"></table></div></article>
    </div>
  </section>

  <section id="view-copa" class="hidden">
    <div class="toolbar"><label>Escolher Copa<select id="cup-select"></select></label></div>
    <div class="kpis" id="kpis-copa"></div>
    <div class="grid">
      <article class="card span-5"><h2>Resumo executivo da edição</h2><div class="table-wrap"><table id="tbl-copa-resumo"></table></div></article>
      <article class="card span-7"><h2>Classificação final</h2><div class="table-wrap"><table id="tbl-copa-ranking"></table></div></article>
      <article class="card span-12"><h2 id="copa-grupos-title">Fase de grupos</h2><div id="copa-grupos" class="phase-stack"></div></article>
      <article class="card span-12"><h2>Mata-mata e jogos decisivos</h2><div id="copa-mata" class="phase-stack"></div></article>
      <article class="card span-12"><h2>Detalhe do jogo selecionado</h2><div id="copa-jogo-detalhe" class="match-detail-panel"></div></article>
      <article class="card span-12"><h2>Todos os jogos da edição</h2><div class="table-wrap"><table id="tbl-copa-jogos"></table></div></article>
      <article class="card span-6"><h2>Prêmios e destaques</h2><div class="table-wrap"><table id="tbl-copa-premios"></table></div></article>
      <article class="card span-6"><h2>Estádios registrados</h2><div class="table-wrap"><table id="tbl-copa-estadios"></table></div></article>
    </div>
  </section>

  <section id="view-selecao" class="hidden">
    <div class="toolbar"><label>Seleção<select id="team-select"></select></label></div>
    <div class="kpis" id="kpis-selecao"></div>
    <div class="grid">
      <article class="card span-8"><h2>Trajetória nas Copas</h2><div id="ch-team-traj" class="chart"></div></article>
      <article class="card span-4"><h2>Vezes em cada posição</h2><div id="ch-team-pos" class="chart"></div></article>
      <article class="card span-7"><h2>Gols por edição</h2><div id="ch-team-gols" class="chart"></div></article>
      <article class="card span-5"><h2>Distribuição de resultados</h2><div id="ch-team-ved" class="chart"></div></article>
      <article class="card span-6"><h2>Adversários mais enfrentados</h2><div class="table-wrap"><table id="tbl-team-adv"></table></div></article>
      <article class="card span-6"><h2>Campanha por edição</h2><div class="table-wrap"><table id="tbl-team-camp"></table></div></article>
      <article class="card span-12"><h2>Quem fez os gols em cada Copa</h2><div id="team-scorers" class="scorers-wrap"></div></article>
      <article class="card span-12"><h2>Todos os jogos da seleção</h2><div class="table-wrap"><table id="tbl-team-jogos"></table></div></article>
    </div>
  </section>
</main>
<div id="rank-tip" class="rank-tip"></div>
<div id="match-modal" class="modal-overlay hidden"><div class="modal-box"><button class="modal-close" id="modal-close" aria-label="Fechar">&times;</button><div id="modal-content"></div></div></div>
<script>
const DATA = __DATA_PAYLOAD__;
const GOLS_DET = ((DATA.gols_detalhados && DATA.gols_detalhados.gols) || []).filter(g=>g.periodo!==5);
let ALL_GOALS = [];
const nf = new Intl.NumberFormat("pt-BR");
const num = v => Number(String(v ?? "0").replace(/[^\d.-]/g,"")) || 0;
const fmt = v => nf.format(num(v));
const esc = v => String(v ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const COLORS = ["#22c55e","#f5c451","#38bdf8","#fb7185","#a78bfa","#f97316","#14b8a6","#eab308"];
const PCFG = {responsive:true, displaylogo:false};
const layout = extra => ({paper_bgcolor:"rgba(0,0,0,0)",plot_bgcolor:"rgba(0,0,0,0)",font:{color:"#f4fff8",family:"Inter,Segoe UI,Arial"},margin:{l:60,r:20,t:10,b:55},xaxis:{gridcolor:"rgba(255,255,255,.1)",zerolinecolor:"rgba(255,255,255,.2)"},yaxis:{gridcolor:"rgba(255,255,255,.1)",zerolinecolor:"rgba(255,255,255,.2)",automargin:true},legend:{orientation:"h",y:-.18},...extra});
const ARTILHEIROS_HIST = DATA.curados.artilheiros_historico;
const ARTILHEIROS_EDICAO = DATA.curados.artilheiros_edicao;
const MARCADORES_GRUPOS = DATA.curados.marcadores_grupos;
const FLAGS = {"Alemanha":"🇩🇪","Arábia Saudita":"🇸🇦","Argentina":"🇦🇷","Austrália":"🇦🇺","Áustria":"🇦🇹","Bélgica":"🇧🇪","Brasil":"🇧🇷","Bulgária":"🇧🇬","Camarões":"🇨🇲","Canadá":"🇨🇦","Catar":"🇶🇦","Chile":"🇨🇱","Colômbia":"🇨🇴","Coreia do Sul":"🇰🇷","Costa Rica":"🇨🇷","Croácia":"🇭🇷","Dinamarca":"🇩🇰","Egito":"🇪🇬","Equador":"🇪🇨","Escócia":"🏴󠁧󠁢󠁳󠁣󠁴󠁿","Eslováquia":"🇸🇰","Eslovênia":"🇸🇮","Espanha":"🇪🇸","Estados Unidos":"🇺🇸","França":"🇫🇷","Gana":"🇬🇭","Grécia":"🇬🇷","Holanda":"🇳🇱","Honduras":"🇭🇳","Hungria":"🇭🇺","Inglaterra":"🏴󠁧󠁢󠁥󠁮󠁧󠁿","Irã":"🇮🇷","Irlanda":"🇮🇪","Irlanda do Norte":"🇬🇧","Itália":"🇮🇹","Japão":"🇯🇵","Marrocos":"🇲🇦","México":"🇲🇽","Nigéria":"🇳🇬","Noruega":"🇳🇴","Nova Zelândia":"🇳🇿","País de Gales":"🏴󠁧󠁢󠁷󠁬󠁳󠁿","Países Baixos":"🇳🇱","Paraguai":"🇵🇾","Peru":"🇵🇪","Polônia":"🇵🇱","Portugal":"🇵🇹","República Tcheca":"🇨🇿","Romênia":"🇷🇴","Rússia":"🇷🇺","Senegal":"🇸🇳","Sérvia":"🇷🇸","Suécia":"🇸🇪","Suíça":"🇨🇭","Tunísia":"🇹🇳","Turquia":"🇹🇷","Ucrânia":"🇺🇦","Uruguai":"🇺🇾"};
const FLAG_CODES = {"Alemanha":"de","Arábia Saudita":"sa","Argentina":"ar","Austrália":"au","Áustria":"at","Bélgica":"be","Brasil":"br","Bulgária":"bg","Camarões":"cm","Canadá":"ca","Catar":"qa","Chile":"cl","Colômbia":"co","Coreia do Sul":"kr","Costa Rica":"cr","Croácia":"hr","Dinamarca":"dk","Egito":"eg","Equador":"ec","Escócia":"gb-sct","Eslováquia":"sk","Eslovênia":"si","Espanha":"es","Estados Unidos":"us","França":"fr","Gana":"gh","Grécia":"gr","Holanda":"nl","Honduras":"hn","Hungria":"hu","Inglaterra":"gb-eng","Irã":"ir","Irlanda":"ie","Irlanda do Norte":"gb-nir","Itália":"it","Japão":"jp","Marrocos":"ma","México":"mx","Nigéria":"ng","Noruega":"no","Nova Zelândia":"nz","País de Gales":"gb-wls","Países Baixos":"nl","Paraguai":"py","Peru":"pe","Polônia":"pl","Portugal":"pt","República Tcheca":"cz","Romênia":"ro","Rússia":"ru","Senegal":"sn","Sérvia":"rs","Suécia":"se","Suíça":"ch","Tunísia":"tn","Turquia":"tr","Ucrânia":"ua","Uruguai":"uy"};
Object.assign(FLAG_CODES,{"África do Sul":"za","Argélia":"dz","Bolívia":"bo","Bósnia e Herzegovina":"ba","China":"cn","Costa do Marfim":"ci","Cuba":"cu","El Salvador":"sv","Emirados Árabes Unidos":"ae","Haiti":"ht","Indonésia":"id","Iraque":"iq","Islândia":"is","Israel":"il","Jamaica":"jm","Kuwait":"kw","Panamá":"pa","República Democrática do Congo":"cd","Zaire":"cd","Tchecoslováquia":"cz","Tchequia":"cz","União Soviética":"ru","Iugoslávia":"rs","Sérvia e Montenegro":"rs","Trinidad e Tobago":"tt","Coreia do Norte":"kp","Angola":"ao","Togo":"tg","Curaçau":"cw","Cabo Verde":"cv","Uzbequistão":"uz","Jordânia":"jo","Tchéquia":"cz"});
const FLAG_IMG = __FLAGS_PAYLOAD__;
const POSTERS = __POSTERS_PAYLOAD__;
const TROFEUS = __TROFEUS_PAYLOAD__;
function flagSrc(name){const code=FLAG_CODES[name]; return code ? (FLAG_IMG[code] || `https://flagcdn.com/w320/${code}.png`) : "";}
const FORMATOS_EDICAO = {
  1930:"Primeira fase em grupos, seguida de semifinal e final.",
  1934:"Torneio eliminatório direto desde a primeira rodada.",
  1938:"Torneio eliminatório direto, com jogos de desempate quando necessário.",
  1950:"Primeira fase em grupos, seguida de quadrangular final.",
  1954:"Fase de grupos com regulamento especial, seguida de mata-mata.",
  1958:"Fase de grupos, seguida de quartas, semifinais e finais.",
  1962:"Fase de grupos, seguida de quartas, semifinais e finais.",
  1966:"Fase de grupos, seguida de quartas, semifinais e finais.",
  1970:"Fase de grupos, seguida de quartas, semifinais e finais.",
  1974:"Primeira fase em grupos, segunda fase em grupos e finais.",
  1978:"Primeira fase em grupos, segunda fase em grupos e finais.",
  1982:"Primeira fase em grupos, segunda fase em grupos e mata-mata final."
};
let state = {view:"geral", cup:2022, q:"", phase:"", cupTeam:"", selectedMatch:"", team:"Brasil", teamQ:"", teamSort:"titulos", teamLimit:25, rankMode:"total", goalYear:"", goalTeam:"", goalType:"", goalBody:"", goalZone:""};

function init(){
  ALL_GOALS = buildGoalDataset();
  document.getElementById("nav").onclick = e => { if(e.target.tagName!=="BUTTON") return; state.view=e.target.dataset.view; switchView(); };
  fillSelect("cup-select", DATA.copas.map(c=>[c.ano, `${c.ano} - ${editionHost(c.ano)}`]));
  document.getElementById("cup-select").value = state.cup;
  document.getElementById("cup-select").onchange = e => { state.cup=+e.target.value; state.selectedMatch=""; renderCopa(); };
  fillSelect("team-select", DATA.selecoes.map(s=>s.selecao).sort((a,b)=>a.localeCompare(b,"pt-BR")).map(s=>[s,s]));
  document.getElementById("team-select").value = state.team;
  document.getElementById("team-select").onchange = e => { state.team=e.target.value; renderSelecao(); };
  initGoalFilters();
  document.querySelectorAll("[data-rank-toggle]").forEach(b=>b.onclick=()=>{state.rankMode=state.rankMode==="pct"?"total":"pct"; renderRankings();});
  initRankTips();
  renderTrofeus(); renderGeral(); renderGols(); renderCopa(); renderSelecao();
}
function switchView(){document.querySelectorAll(".nav button").forEach(b=>b.classList.toggle("active",b.dataset.view===state.view));["geral","gols","copa","selecao"].forEach(v=>document.getElementById("view-"+v).classList.toggle("hidden",v!==state.view)); document.getElementById("hero-trofeus").classList.toggle("hidden",state.view!=="geral"); document.getElementById("hero-cartaz").classList.toggle("hidden",state.view!=="copa"); document.getElementById("hero-bandeira").classList.toggle("hidden",state.view!=="selecao"); setTimeout(()=>{ if(state.view==="geral") renderGeral(); if(state.view==="gols") renderGols(); if(state.view==="copa") renderCopa(); if(state.view==="selecao") renderSelecao(); window.dispatchEvent(new Event("resize")); },20);}
function renderTrofeus(){document.getElementById("hero-trofeus").innerHTML=`<div class="trofeus-grid">${TROFEUS.map(t=>`<figure><img src="${t.img}" alt="${esc(t.label)}"><figcaption><b>${esc(t.label)}</b>${esc(t.periodo)}</figcaption></figure>`).join("")}</div>`;}
function updateHeroCartaz(c){const img=document.getElementById("cartaz-img"), src=POSTERS[c.ano]||""; img.alt=`Cartaz da Copa de ${c.ano}`; if(src){img.src=src; img.classList.remove("hidden");}else{img.removeAttribute("src"); img.classList.add("hidden");}}
function updateHeroBandeira(){const host=document.getElementById("hero-bandeira"), t=state.team, src=t&&flagSrc(t); host.innerHTML= src ? `<img class="hero-flag-img" src="${src}" alt="${esc(t)}"><span class="note">${esc(t)}</span>` : `<span class="note">Escolha uma seleção acima para ver a bandeira.</span>`;}
function fillSelect(id, rows){document.getElementById(id).innerHTML=rows.map(([v,l])=>`<option value="${esc(v)}">${esc(l)}</option>`).join("");}
function editionChampion(year){return (DATA.geral.editions.find(e=>e.ano===year)||{}).campeao || "";}
function editionRow(year){return DATA.geral.editions.find(e=>e.ano===year)||{};}
function editionHost(year){const c=DATA.copas.find(x=>x.ano===year)||{}; return editionRow(year).sede || (c.info||{}).sede || "";}
function editionTopScorer(year){const row=ARTILHEIROS_EDICAO.find(r=>+r[0]===+year); return row ? `${row[1]} (${row[2]} gols)` : "-";}
function countryTag(pais){return pais && FLAG_CODES[pais] ? teamLabelHtml(pais) : esc(pais||"");}
function scorerCell(year){const row=ARTILHEIROS_EDICAO.find(r=>+r[0]===+year); if(!row) return "-"; const pais=row[3]; return `${esc(row[1])} (${esc(row[2])} gols)${pais?` · ${countryTag(pais)}`:""}`;}
function playerCell(c){const nome=c.info.melhor_jogador||"-"; if(nome==="-") return "-"; const pais=c.info.melhor_jogador_selecao; return `${esc(nome)}${pais?` · ${countryTag(pais)}`:""}`;}
function renderResumo(c,e){
  const rows=[["Ano",esc(c.ano)],["Sede",cellHtml(e.sede||c.info.sede||"-")],["Campeão",cellHtml(e.campeao||c.info.campeao||"-")],["Vice",cellHtml(e.vice||c.info.vice||"-")],["Terceiro",cellHtml(e.terceiro||"-")],["Quarto",cellHtml(e.quarto||"-")],["Final",esc(e.placar_final||"-")],["Artilheiro",scorerCell(c.ano)],["Melhor jogador",playerCell(c)]];
  document.getElementById("tbl-copa-resumo").innerHTML=`<thead><tr><th>Item</th><th>Valor</th></tr></thead><tbody>${rows.map(([k,v])=>`<tr><td>${esc(k)}</td><td>${v}</td></tr>`).join("")}</tbody>`;
}
function cup(){return DATA.copas.find(c=>c.ano===state.cup) || DATA.copas[DATA.copas.length-1];}

function buildGoalDataset(){
  const analytic=(DATA.gols_analiticos&&DATA.gols_analiticos.gols)||[];
  if(analytic.length){
    return analytic.map(g=>{
      const s=scoreParts(g.placar||"");
      const official=g.tipo_oficial==="penalti"?"Pênalti":(g.tipo_oficial==="gol_contra"?"Gol contra":(g.tipo_oficial==="indefinido"?"Não identificado":"Não detalhado"));
      return {
        ano:g.edicao,
        fase:g.fase,
        grupo:g.grupo,
        mandante:g.time_1,
        visitante:g.time_2,
        placar_mandante:s[0],
        placar_visitante:s[1],
        data:g.data,
        estadio:g.estadio,
        selecao:g.selecao,
        jogador:g.jogador,
        minuto:g.minuto,
        minuto_label:g.minuto_texto,
        texto_original:g.texto_original,
        situacao:g.situacao||"Não informado",
        fonte_situacao:g.fonte_situacao||"",
        tipo_chute_pt:g.tipo_tecnico&&g.tipo_tecnico!=="Não detalhado"?g.tipo_tecnico:official,
        eh_penalti:!!g.eh_penalti,
        fonte_tecnica:g.fonte_tecnica||g.fonte_oficial||"",
      };
    });
  }
  const techByKey={};
  GOLS_DET.forEach(g=>{
    const k=goalTechKey(g.ano,g.selecao,g.minuto);
    (techByKey[k] ||= []).push(g);
  });
  const out=[];
  DATA.copas.forEach(c=>{
    c.partidas.forEach(p=>{
      goalEvents(rawScorersForMatch(c,p),p).forEach(ev=>{
        const minute=Math.floor(goalMinute(ev.text));
        if(minute>=999) return;
        const jogador=goalScorerName(ev.text) || "Não informado";
        const own=/g\.?c\.?|contra|own goal/i.test(ev.text);
        const pen=/pen|pênalti|penalti/i.test(ev.text);
        const tech=(techByKey[goalTechKey(c.ano,ev.team,minute)]||[]).shift();
        out.push({
          ano:c.ano,
          fase:p.fase||"",
          grupo:p.grupo||"",
          mandante:p.time1,
          visitante:p.time2,
          placar_mandante:scoreParts(p.placar)[0],
          placar_visitante:scoreParts(p.placar)[1],
          data:p.data||"",
          estadio:p.estadio||"",
          selecao:ev.team,
          jogador,
          minuto:minute,
          minuto_label:goalMinuteLabel(ev.text),
          texto_original:ev.text,
          situacao: tech ? (tech.situacao||"Não informado") : (own ? "Gol contra" : (pen ? "Pênalti" : "Não informado")),
          fonte_situacao: tech ? "StatsBomb Open Data" : "",
          tipo_chute_pt: tech ? tech.tipo_chute_pt : (own ? "Gol contra" : (pen ? "Pênalti" : "Não detalhado")),
          parte_corpo_pt: tech ? tech.parte_corpo_pt : "Não detalhado",
          zona: tech ? tech.zona : "Não detalhado",
          xg: tech ? tech.xg : null,
          distancia_m: tech ? tech.distancia_m : null,
          eh_penalti: tech ? tech.eh_penalti : pen,
          eh_falta: tech ? tech.eh_falta : false,
          eh_cabeca: tech ? tech.eh_cabeca : false,
          fonte_tecnica: tech ? "StatsBomb" : "Wikipedia",
        });
      });
    });
  });
  return out.sort((a,b)=>a.ano-b.ano || a.minuto-b.minuto);
}
function goalTechKey(year,team,minute){return `${year}|${detNorm(team)}|${Math.floor(num(minute))}`;}

function initGoalFilters(){
  fillGoalSelect("goal-year", [["","Todos os anos"], ...uniq(ALL_GOALS.map(g=>g.ano)).sort((a,b)=>b-a).map(y=>[y,y])], "goalYear");
  fillGoalSelect("goal-team", [["","Todas as seleções"], ...uniq(ALL_GOALS.map(g=>g.selecao)).sort((a,b)=>a.localeCompare(b,"pt-BR")).map(t=>[t,t])], "goalTeam");
}
function fillGoalSelect(id, rows, key){
  fillSelect(id, rows);
  document.getElementById(id).value = state[key] || "";
  document.getElementById(id).onchange = e => { state[key]=e.target.value; renderGols(); };
}
function filteredDetailedGoals(){
  return ALL_GOALS.filter(g=>
    (!state.goalYear || String(g.ano)===String(state.goalYear)) &&
    (!state.goalTeam || g.selecao===state.goalTeam)
  );
}
function renderGols(){
  const rows=filteredDetailedGoals();
  const total=rows.length;
  const pen=rows.filter(g=>g.eh_penalti||g.situacao==="Pênalti").length;
  const og=rows.filter(g=>g.situacao==="Gol contra").length;
  const teams=uniq(rows.map(g=>g.selecao)).length;
  const players=uniq(rows.map(g=>g.jogador).filter(j=>j&&j!=="Não informado"&&j!=="Não identificado na fonte")).length;
  document.getElementById("kpis-gols").innerHTML=kpis([
    ["Gols na visão", total],
    ["Pênaltis", pen],
    ["Gols contra", og],
    ["Seleções", teams],
    ["Jogadores", players]
  ]);
  const minuteBins=["0-15","16-30","31-45","46-60","61-75","76-90","90+"];
  const minuteRows=minuteBins.map(b=>[b,rows.filter(g=>minuteBucket(g.minuto)===b).length]);
  Plotly.react("ch-goals-minute",[{type:"bar",x:minuteRows.map(r=>r[0]),y:minuteRows.map(r=>r[1]),marker:{color:COLORS[1],cornerradius:4},hovertemplate:"<b>%{x}</b><br>Gols: %{y}<extra></extra>"}],layout({hovermode:"closest",xaxis:{type:"category"},yaxis:{title:"Gols"}}),PCFG);
  renderGoalEditionCombo(rows);
  renderGoalTeamCombo(rows);
  renderGoalPhaseCharts(rows);
  renderGoalTeamBalanceCharts();
  renderGoalPlayersAll(rows);
  renderGoalsTopScorers();
  renderGoalKnockoutRankings(rows);
  table("tbl-goals",["Ano","Fase","Jogo","Min","Seleção","Jogador"],rows.slice().reverse().map(g=>[g.ano,g.fase,`${g.mandante} ${g.placar_mandante} x ${g.placar_visitante} ${g.visitante}`,goalMinuteText(g),g.selecao,g.jogador]),[0]);
}
function filteredGoalMatches(){
  const out=[];
  DATA.copas.forEach(c=>{
    if(state.goalYear && String(c.ano)!==String(state.goalYear)) return;
    c.partidas.forEach(p=>{
      if(state.goalTeam && p.time1!==state.goalTeam && p.time2!==state.goalTeam) return;
      if(!scoreParts(p.placar).join("")) return;
      out.push({...p,ano:c.ano});
    });
  });
  return out;
}
function goalGamesByEdition(){
  const out={};
  DATA.copas.forEach(c=>{
    if(state.goalYear && String(c.ano)!==String(state.goalYear)) return;
    const matches=c.partidas.filter(p=>!state.goalTeam || p.time1===state.goalTeam || p.time2===state.goalTeam);
    if(matches.length) out[c.ano]=matches.length;
  });
  return out;
}
function goalGamesByTeam(){
  const out={};
  DATA.copas.forEach(c=>{
    if(state.goalYear && String(c.ano)!==String(state.goalYear)) return;
    c.partidas.forEach(p=>{
      [p.time1,p.time2].forEach(t=>{
        if(!t || (state.goalTeam && t!==state.goalTeam)) return;
        out[t]=(out[t]||0)+1;
      });
    });
  });
  return out;
}
function goalTeamMatchStats(){
  const stats={};
  filteredGoalMatches().forEach(p=>{
    const s=scoreParts(p.placar);
    if(s[0]==="" || s[1]==="") return;
    const g1=num(s[0]), g2=num(s[1]);
    [[p.time1,g1,g2],[p.time2,g2,g1]].forEach(([team,gp,gc])=>{
      if(!team || (state.goalTeam && team!==state.goalTeam)) return;
      const row=stats[team] ||= {team,jogos:0,gp:0,gc:0};
      row.jogos+=1; row.gp+=gp; row.gc+=gc;
    });
  });
  return Object.values(stats).map(r=>({...r,sg:r.gp-r.gc,gpj:r.jogos?+(r.gp/r.jogos).toFixed(2):0,gcj:r.jogos?+(r.gc/r.jogos).toFixed(2):0,sgj:r.jogos?+((r.gp-r.gc)/r.jogos).toFixed(2):0}));
}
function phaseLabel(phase){
  const p=String(phase||"").trim();
  if(!p) return "Não informado";
  if(p.toLowerCase().includes("grupo")) return "Fase de grupos";
  if(p.toLowerCase().includes("terceiro")) return "Terceiro lugar";
  return p;
}
function phaseSort(a,b){
  const order=phase=>phase==="Fase de grupos" ? 0 : phaseRank(phase)+1;
  return order(a)-order(b) || a.localeCompare(b,"pt-BR");
}
function isKnockoutPhase(phase){
  const p=String(phase||"").toLowerCase();
  return p.includes("oitavas") || p.includes("quartas") || p.includes("semifinal") || p==="final" || p.includes("terceiro");
}
function goalPhaseRows(rows){
  const goals=countBy(rows,g=>phaseLabel(g.fase));
  const games=countBy(filteredGoalMatches(),p=>phaseLabel(p.fase));
  return Object.keys({...games,...goals}).filter(k=>goals[k]||games[k]).sort(phaseSort).map(label=>({label,gols:goals[label]||0,jogos:games[label]||0,gpg:games[label]?+(goals[label]/games[label]).toFixed(2):0}));
}
function renderGoalPhaseCharts(rows){
  const phaseRows=goalPhaseRows(rows);
  Plotly.react("ch-goals-phase",[{type:"bar",x:phaseRows.map(r=>r.label),y:phaseRows.map(r=>r.gols),marker:{color:COLORS[0],cornerradius:4},text:phaseRows.map(r=>r.gols),textposition:"outside",cliponaxis:false,hovertemplate:"<b>%{x}</b><br>Gols: %{y}<extra></extra>"}],layout({hovermode:"closest",margin:{l:44,r:18,t:10,b:70},xaxis:{type:"category",tickangle:-20,automargin:true},yaxis:{title:"Gols"}}),PCFG);
  Plotly.react("ch-goals-phase-rate",[{type:"bar",x:phaseRows.map(r=>r.label),y:phaseRows.map(r=>r.gpg),marker:{color:COLORS[1],cornerradius:4},text:phaseRows.map(r=>r.gpg.toFixed(2).replace(".",",")),textposition:"outside",cliponaxis:false,hovertemplate:"<b>%{x}</b><br>Gols/jogo: %{y:.2f}<extra></extra>"}],layout({hovermode:"closest",margin:{l:44,r:18,t:10,b:70},xaxis:{type:"category",tickangle:-20,automargin:true},yaxis:{title:"Gols/jogo",tickformat:".2f"}}),PCFG);
}
function renderGoalTeamBalanceCharts(){
  const rows=goalTeamMatchStats().sort((a,b)=>b.gp-a.gp || a.team.localeCompare(b.team,"pt-BR"));
  renderTeamMetricGrouped("ch-goals-team-balance", rows, [
    {key:"gp",name:"Marcados",color:COLORS[0]},
    {key:"gc",name:"Sofridos",color:COLORS[3]},
    {key:"sg",name:"Saldo",color:COLORS[1]},
  ], "Gols");
  renderTeamMetricGrouped("ch-goals-team-averages", rows.sort((a,b)=>b.gpj-a.gpj || a.team.localeCompare(b.team,"pt-BR")), [
    {key:"gpj",name:"Marcados/jogo",color:COLORS[0]},
    {key:"gcj",name:"Sofridos/jogo",color:COLORS[3]},
    {key:"sgj",name:"Saldo/jogo",color:COLORS[1]},
  ], "Média");
}
function renderTeamMetricGrouped(id, rows, metrics, title){
  const host=document.getElementById(id);
  host.style.height=`${Math.max(260, rows.length*28+90)}px`;
  const rev=rows.slice().reverse();
  const traces=metrics.map(m=>({type:"bar",orientation:"h",name:m.name,y:rev.map(r=>r.team),x:rev.map(r=>r[m.key]),marker:{color:m.color,cornerradius:3},hovertemplate:"<b>%{y}</b><br>%{fullData.name}: %{x}<extra></extra>"}));
  Plotly.react(id,traces,layout({barmode:"group",hovermode:"closest",margin:{l:118,r:28,t:10,b:58},xaxis:{title,zeroline:true,zerolinecolor:"rgba(255,255,255,.35)",automargin:true},yaxis:{automargin:true,tickfont:{size:11}},legend:{orientation:"h",y:-.16}}),PCFG);
}
function renderGoalEditionCombo(rows){
  const games=goalGamesByEdition();
  const goals=countBy(rows,g=>g.ano);
  const years=Object.keys(games).map(Number).filter(y=>goals[y]).sort((a,b)=>a-b);
  const chartRows=years.map(y=>({label:String(y),gols:goals[y]||0,gpg:games[y]?+(goals[y]/games[y]).toFixed(2):0}));
  renderGoalComboV("ch-goals-edicao", chartRows, "Edição");
}
function renderGoalTeamCombo(rows){
  const games=goalGamesByTeam();
  const goals=countBy(rows,g=>g.selecao);
  const chartRows=Object.keys(goals).map(team=>({label:team,gols:goals[team],gpg:games[team]?+(goals[team]/games[team]).toFixed(2):0}))
    .sort((a,b)=>b.gols-a.gols || a.label.localeCompare(b.label,"pt-BR"));
  const host=document.getElementById("ch-goals-teams");
  host.style.height="390px";
  host.style.width=`${Math.max(560, chartRows.length*46+120)}px`;
  renderGoalComboV("ch-goals-teams", chartRows);
}
function renderGoalPlayersAll(rows){
  const playerRows=countRows(rows.filter(g=>g.jogador&&g.jogador!=="Não informado"&&g.jogador!=="Não identificado na fonte"),g=>g.jogador);
  renderGoalRankList("ch-goals-players", playerRows, COLORS[1]);
}
function renderGoalsTopScorers(){
  let rows=ARTILHEIROS_EDICAO.slice();
  if(state.goalYear) rows=rows.filter(r=>String(r[0])===String(state.goalYear));
  if(state.goalTeam) rows=rows.filter(r=>String(r[3]||"").split(",").map(x=>x.trim()).includes(state.goalTeam));
  rows=rows.sort((a,b)=>+a[0]-+b[0]);
  const chartRows=rows.map(r=>[`${r[0]} - ${r[1]}${r[3]?` (${r[3]})`:""}`, r[2]]);
  if(!chartRows.length){
    document.getElementById("ch-goals-topscorers-edicao").innerHTML=`<p class="note">Nenhum artilheiro encontrado para os filtros selecionados.</p>`;
    return;
  }
  renderGoalRankList("ch-goals-topscorers-edicao", chartRows, COLORS[1]);
}
function renderGoalKnockoutRankings(rows){
  const ko=rows.filter(g=>isKnockoutPhase(g.fase));
  renderGoalRankList("ch-goals-ko-teams", countRows(ko,g=>g.selecao), COLORS[0]);
  renderGoalRankList("ch-goals-ko-players", countRows(ko.filter(g=>g.jogador&&g.jogador!=="Não informado"&&g.jogador!=="Não identificado na fonte"),g=>g.jogador), COLORS[1]);
}
function renderGoalComboV(id, rows){
  const isTeamChart=id==="ch-goals-teams";
  const xaxis={type:"category",tickangle:-25,automargin:true};
  if(isTeamChart) xaxis.range=[-.15, rows.length-.5];
  Plotly.react(id,[
    {type:"bar",x:rows.map(r=>r.label),y:rows.map(r=>r.gols),name:"Gols",marker:{color:COLORS[0],cornerradius:4},text:rows.map(r=>r.gols),textposition:"outside",cliponaxis:false,hovertemplate:"<b>%{x}</b><br>Gols: %{y}<extra></extra>"},
    {type:"scatter",mode:"lines+markers",x:rows.map(r=>r.label),y:rows.map(r=>r.gpg),yaxis:"y2",name:"Gols/jogo",line:{color:COLORS[1],width:3},marker:{size:6},hovertemplate:"<b>%{x}</b><br>Gols/jogo: %{y:.2f}<extra></extra>"}
  ],layout({hovermode:"closest",margin:{l:isTeamChart?12:44,r:52,t:10,b:70},bargap:.18,xaxis,yaxis:{title:isTeamChart?"":"Gols",showline:!isTeamChart},yaxis2:{title:"Gols/jogo",overlaying:"y",side:"right",gridcolor:"rgba(0,0,0,0)",tickformat:".2f"},legend:{orientation:"h",y:-.2}}),PCFG);
}
function renderGoalComboH(id, rows){
  const rev=rows.slice().reverse();
  Plotly.react(id,[
    {type:"bar",orientation:"h",y:rev.map(r=>r.label),x:rev.map(r=>r.gols),name:"Gols",marker:{color:COLORS[0],cornerradius:4},text:rev.map(r=>r.gols),textposition:"outside",cliponaxis:false,hovertemplate:"<b>%{y}</b><br>Gols: %{x}<extra></extra>"},
    {type:"scatter",mode:"lines+markers",y:rev.map(r=>r.label),x:rev.map(r=>r.gpg),xaxis:"x2",name:"Gols/jogo",line:{color:COLORS[1],width:3},marker:{size:6},hovertemplate:"<b>%{y}</b><br>Gols/jogo: %{x:.2f}<extra></extra>"}
  ],layout({hovermode:"closest",margin:{l:124,r:44,t:10,b:55},xaxis:{title:"Gols",showspikes:false,automargin:true},xaxis2:{title:"Gols/jogo",overlaying:"x",side:"top",gridcolor:"rgba(0,0,0,0)",tickformat:".2f"},yaxis:{showspikes:false,automargin:true,tickfont:{size:11}},legend:{orientation:"h",y:-.15}}),PCFG);
}
function renderGoalRankList(id, rows, color){
  const host=document.getElementById(id);
  if(!rows.length){host.innerHTML=`<p class="note">Nenhum registro encontrado para os filtros selecionados.</p>`;return;}
  const max=Math.max(...rows.map(r=>r[1]),1);
  host.innerHTML=`<div class="rank-list">${rows.map(([label,val])=>`<div class="rank-row" title="${esc(label)}: ${esc(val)}"><span class="rank-label" title="${esc(label)}">${esc(label)}</span><div class="rank-bar-wrap"><div class="rank-bar" style="width:${(val/max*100).toFixed(1)}%;background:${color}"></div></div><span class="rank-val">${esc(val)}</span></div>`).join("")}</div>`;
}
function renderGoalBar(id, rows, title, color){
  Plotly.react(id,[{type:"bar",x:rows.map(r=>r[0]),y:rows.map(r=>r[1]),marker:{color,cornerradius:4},text:rows.map(r=>r[1]),textposition:"outside",cliponaxis:false,hovertemplate:`<b>%{x}</b><br>${title}: %{y}<extra></extra>`}],layout({hovermode:"closest",margin:{l:44,r:18,t:10,b:70},xaxis:{type:"category",tickangle:-25,automargin:true},yaxis:{title}}),PCFG);
}
function countBy(rows, fn){return rows.reduce((acc,row)=>{const k=fn(row)||"Não informado"; acc[k]=(acc[k]||0)+1; return acc;},{});}
function countRows(rows, fn){return Object.entries(countBy(rows,fn)).sort((a,b)=>b[1]-a[1] || a[0].localeCompare(b[0],"pt-BR"));}
function uniq(rows){return [...new Set(rows.filter(v=>v!==undefined && v!==null && v!==""))];}
function minuteBucket(m){m=num(m); if(m<=15)return"0-15"; if(m<=30)return"16-30"; if(m<=45)return"31-45"; if(m<=60)return"46-60"; if(m<=75)return"61-75"; if(m<=90)return"76-90"; return"90+";}
function goalMinuteText(g){if(g.minuto_label) return g.minuto_label; const m=g.minuto ?? ""; const s=num(g.segundo); return `${m}'${s?` ${String(s).padStart(2,"0")}s`:""}`;}

function renderGeral(){
  const ed=DATA.geral.editions, sel=DATA.selecoes, totalJogos=edSum("jogos"), totalGols=edSum("gols");
  document.getElementById("kpis-geral").innerHTML = kpis([["Edições",DATA.copas.length],["Seleções campeãs",new Set(ed.map(e=>e.campeao)).size],["Jogos",totalJogos],["Gols",totalGols],["Gols/jogo",totalJogos?(totalGols/totalJogos).toFixed(2).replace(".",","):"-"],["Seleções na base",sel.length]]);
  renderTimeline("timeline-geral", [...ed, {ano:2026, campeao:"Em andamento", sede:"Canadá, EUA e México", futuro:true}, {ano:2030, campeao:"Em aberto", futuro:true}], false);
  renderTitulos();
  renderPodium();
  renderRankings();
  const cupStats=DATA.copas.map(c=>({ano:c.ano,jogos:c.info.jogos||c.partidas.length,gols:c.info.gols||c.partidas.reduce((a,b)=>a+num(b.gols),0)})).map(r=>({...r,golsJogo:r.jogos?+(r.gols/r.jogos).toFixed(2):0}));
  Plotly.react("ch-edicoes", [{type:"bar",x:cupStats.map(r=>String(r.ano)),y:cupStats.map(r=>r.gols),name:"Gols",marker:{color:COLORS[0]}},{type:"scatter",mode:"lines+markers",x:cupStats.map(r=>String(r.ano)),y:cupStats.map(r=>r.golsJogo),yaxis:"y2",name:"Gols/jogo",line:{color:COLORS[1],width:3}}], layout({xaxis:{type:"category",categoryorder:"array",categoryarray:cupStats.map(r=>String(r.ano)),tickangle:-35},yaxis:{title:"Gols"},yaxis2:{title:"Gols/jogo",overlaying:"y",side:"right",gridcolor:"rgba(0,0,0,0)",tickformat:".2f"}}), PCFG);
  const att=DATA.geral.attendance.map(r=>({ano:num(r["Edição"]), publico:num(r["Público Total"]), media:num(r["Média de público"])})).filter(r=>r.ano);
  Plotly.react("ch-publico", [{type:"bar",x:att.map(r=>String(r.ano)),y:att.map(r=>r.publico),name:"Público total",marker:{color:COLORS[2]}},{type:"scatter",mode:"lines+markers",x:att.map(r=>String(r.ano)),y:att.map(r=>r.media),yaxis:"y2",name:"Média",line:{color:COLORS[3],width:3}}], layout({xaxis:{type:"category",categoryorder:"array",categoryarray:att.map(r=>String(r.ano)),tickangle:-35},yaxis:{title:"Público"},yaxis2:{title:"Média",overlaying:"y",side:"right",gridcolor:"rgba(0,0,0,0)"}}), PCFG);
  table("tbl-edicoes",["Ano","Sede","Campeão","Vice","3º","4º","Final"],ed.map(e=>[e.ano,e.sede,e.campeao,e.vice,e.terceiro,e.quarto,e.placar_final]),[0]);
  renderAtaqueDefesa();
  barH("ch-artilheiros-historico", ARTILHEIROS_HIST, "Gols", COLORS[1]);
  barH("ch-artilheiros-edicao", ARTILHEIROS_EDICAO.map(r=>[`${r[0]} - ${r[1]}`,r[2]]), "Gols", COLORS[1]);
  table("tbl-goleadas",["#","Time 1","Placar","Time 2","Estádio","Sede","Ano"],DATA.geral.blowouts.map(r=>[r["Nº"],r["Time 1"],r["Placar"],r["Time 2"],r["Estádio"],editionRow(num(r["Ano"])).sede||"-",r["Ano"]]),[0,6]);
}
function edSum(field){return DATA.copas.reduce((a,c)=>a+num(c.info[field] || (field==="jogos"?c.partidas.length:(field==="gols"?c.partidas.reduce((s,p)=>s+num(p.gols),0):0))),0)}

function renderCopa(){
  const c=cup(), e=editionRow(c.ano), jogos=filteredCupMatches(c);
  updateHeroCartaz(c);
  document.getElementById("cup-select").value = c.ano;
  document.getElementById("kpis-copa").innerHTML=kpis([["Edição",c.ano],["Sede",e.sede||c.info.sede||"-"],["Campeão",e.campeao||c.info.campeao||"-"],["Jogos",c.info.jogos||c.partidas.length],["Gols",c.info.gols||c.partidas.reduce((a,b)=>a+num(b.gols),0)],["Seleções",c.info.participantes||new Set(c.partidas.flatMap(p=>[p.time1,p.time2])).size]]);
  renderResumo(c,e);
  table("tbl-copa-ranking",["Pos","Seleção","Gr","Pts","J","V","E","D","GP","GC","SG"],c.classificacao_final.map(r=>[r.pos,r.selecao,r.grupo,r.pts,r.j,r.v,r.e,r.d,r.gp,r.gc,r.sg]),[0,3,4,5,6,7,8,9]);
  renderMatchDetail(c);
  renderGroups(c);
  renderKnockout(c);
  table("tbl-copa-jogos",["Fase","Grupo","Data","Time 1","Placar","Time 2","Estádio","Detalhes"],jogos.map(p=>[p.fase,p.grupo,p.data,p.time1,p.placar,p.time2,p.estadio,p.detalhes]));
  table("tbl-copa-premios",["Prêmio","Vencedor"],(c.premios||[]).map(p=>[p.premio,p.vencedor]));
  table("tbl-copa-estadios",["Cidade","Estádio","Detalhe"],(c.estadios||[]).map(s=>[s.cidade,s.estadio,s.detalhe]));
}
function filteredCupMatches(c){return c.partidas;}
function renderKnockout(c){
  const host=document.getElementById("copa-mata");
  if(+c.ano===1950){host.innerHTML=`<p class="note">A Copa de 1950 não teve mata-mata. O campeão foi definido no quadrangular final, exibido junto aos grupos acima.</p>`;return;}
  const rows=c.partidas.filter(p=>p.fase!=="Fase de grupos");
  if(!rows.length){host.innerHTML=`<p class="note">Esta edição não tem jogos decisivos separados na base extraída.</p>`;return;}
  const by=groupBy(rows,p=>p.fase||"Jogos decisivos");
  const bracket=bracketRows(by);
  const hasBracket=[...bracket.r16,...bracket.qf,...bracket.sf,bracket.final].filter(Boolean).length;
  if(hasBracket<3){
    const phases=Object.keys(by).sort((a,b)=>phaseRank(a)-phaseRank(b));
    host.innerHTML=phases.map(phase=>`<section class="group-block"><div class="phase-title"><span>${esc(phase)}</span><span>${by[phase].length} jogos</span></div><div class="knockout-grid">${by[phase].map(p=>matchCard(c,p)).join("")}</div></section>`).join("");
  }else{
    const r16=splitBracket(bracket.r16), qf=splitBracket(bracket.qf), sf=splitBracket(bracket.sf);
    host.innerHTML=`<div class="bracket-board"><div class="bracket-head"><b>Chaveamento</b><span>${esc(c.ano)} | mata-mata</span></div><div class="bracket-stage"><div class="bracket-col left r16">${bracketColumn(c,r16.left)}</div><div class="bracket-col left qf">${bracketColumn(c,qf.left)}</div><div class="bracket-col left sf">${bracketColumn(c,sf.left)}</div><div class="bracket-center"><div class="bracket-final-label">Final</div>${bracket.final?bracketMatch(c,bracket.final):`<div class="bracket-empty"></div>`}<div class="bracket-trophy">FIFA</div>${bracket.third?`<div class="bracket-third"><div class="bracket-final-label">3º lugar</div>${bracketMatch(c,bracket.third)}</div>`:""}</div><div class="bracket-col right sf">${bracketColumn(c,sf.right)}</div><div class="bracket-col right qf">${bracketColumn(c,qf.right)}</div><div class="bracket-col right r16">${bracketColumn(c,r16.right)}</div></div></div>`;
  }
  host.onclick=e=>{const card=e.target.closest("[data-match-id]"); if(!card)return; selectMatch(c,card.dataset.matchId);};
}
function bracketRows(by){
  const get=name=>Object.entries(by).find(([phase])=>phase.toLowerCase().includes(name))?.[1] || [];
  return {r16:get("oitavas"),qf:get("quartas"),sf:get("semifinal"),third:get("terceiro")[0]||null,final:(by["Final"]||[])[0]||get("final").find(p=>p.fase==="Final")||null};
}
function splitBracket(rows){const mid=Math.ceil(rows.length/2); return {left:rows.slice(0,mid),right:rows.slice(mid).reverse()};}
function bracketColumn(c,rows){return rows.length ? rows.map(p=>bracketMatch(c,p)).join("") : `<div class="bracket-empty"></div>`;}
function bracketMatch(c,p){
  const winner=matchWinner(c,p), id=matchUid(c,p), s=scoreParts(p.placar);
  return `<article class="bracket-match ${state.selectedMatch===id?"selected-match":""}" data-match-id="${esc(id)}"><div class="bracket-meta">${esc(p.fase||"-")} | ${esc(p.data||"-")}</div><div class="bracket-team ${winner===p.time1?"winner":""}"><b>${teamLabelHtml(p.time1)}</b><span>${esc(s[0])}</span></div><div class="bracket-team ${winner===p.time2?"winner":""}"><b>${teamLabelHtml(p.time2)}</b><span>${esc(s[1])}</span></div></article>`;
}
function scoreParts(score){const text=String(score||""); if(text.toLowerCase().includes("w.o")) return ["W.O.",""]; const m=text.match(/(\d+)\s*[-x]\s*(\d+)/); return m?[m[1],m[2]]:["",""];}
function phaseRank(phase){
  const p=String(phase||"").toLowerCase();
  if(p.includes("avos")) return 0;
  if(p.includes("oitavas")) return 1;
  if(p.includes("quartas")) return 2;
  if(p.includes("semifinal")) return 3;
  if(p.includes("terceiro")) return 4;
  if(p==="final" || p.includes("final")) return 5;
  if(p.includes("mata")) return 6;
  return 9;
}
function matchCard(c,p){
  const winner=matchWinner(c,p);
  const detail=[p.estadio, finalDecision(c,p), p.detalhes].filter(Boolean).join(" | ");
  const id=matchUid(c,p);
  return `<article class="match-card ${state.selectedMatch===id?"selected-match":""}" data-match-id="${esc(id)}"><div class="match-meta"><span>${esc(p.data||"-")}</span><span>${esc(p.grupo||"")}</span></div><div class="scoreline"><strong class="${winner===p.time1?"winner":""}">${teamLabelHtml(p.time1)}</strong><span class="score">${esc(p.placar)}</span><strong class="right ${winner===p.time2?"winner":""}">${teamLabelHtml(p.time2)}</strong></div>${detail?`<div class="match-detail">${esc(detail)}</div>`:""}</article>`;
}
function matchUid(c,p){return [c.ano,p.fase,p.grupo,p.data,p.time1,p.placar,p.time2,p.estadio].map(v=>String(v||"")).join("|");}
function usesModalDetail(c){return true;}
function selectMatch(c,id){
  state.selectedMatch=id;
  renderMatchDetail(c);
  renderGroups(c);
  renderKnockout(c);
  if(usesModalDetail(c)) openMatchModal(id);
}
function matchWinner(c,p){
  if(p.vencedor) return p.vencedor;
  const score=String(p.placar||"");
  const m=score.match(/(\d+)\s*[-x]\s*(\d+)/);
  if(!m) return "";
  const a=+m[1], b=+m[2];
  if(a>b) return p.time1;
  if(b>a) return p.time2;
  const pen=score.match(/(\d+)\s*[-x]\s*(\d+)\s*\(pen/i) || score.match(/\(pen\).*?(\d+)\s*[-x]\s*(\d+)/i);
  if(!pen) return "";
  const pa=+pen[1], pb=+pen[2];
  if(pa>pb) return p.time1;
  if(pb>pa) return p.time2;
  const e=editionRow(c.ano);
  if(p.fase==="Final") return e.campeao || "";
  if(p.fase==="Terceiro lugar") return e.terceiro || "";
  return "";
}
function finalDecision(c,p){
  if(p.fase!=="Final") return "";
  const finalScore=editionRow(c.ano).placar_final || "";
  return finalScore && finalScore!==p.placar ? `Decisão: ${finalScore}` : "";
}
function renderMatchDetail(c){
  const host=document.getElementById("copa-jogo-detalhe");
  if(!host) return;
  if(usesModalDetail(c)){host.innerHTML=`<p class="note">Selecione um jogo para abrir os detalhes em modal.</p>`;return;}
  let p=c.partidas.find(row=>matchUid(c,row)===state.selectedMatch);
  if(!p){
    p=c.partidas.find(row=>row.fase==="Final") || c.partidas.find(row=>row.fase!=="Fase de grupos") || c.partidas[0];
    state.selectedMatch=p ? matchUid(c,p) : "";
  }
  if(!p){host.innerHTML=`<p class="note">Nenhum jogo encontrado para esta edição.</p>`;return;}
  const winner=matchWinner(c,p);
  const scorers=rawScorersForMatch(c,p);
  const decision=finalDecision(c,p);
  const detail=matchExtraDetail(p,decision);
  const s=scoreParts(p.placar), events=goalEvents(scorers,p);
  host.innerHTML=`<article class="game-scoreboard"><div class="game-top"><span>Copa do Mundo FIFA ${esc(c.ano)} · ${esc(p.data||"-")} · ${esc(p.estadio||"-")}</span><span class="game-status">${esc(matchStatus(p))}</span></div>${p.ficha?`<div class="game-detailbar"><button class="game-details-btn" data-uid="${esc(matchUid(c,p))}">Detalhes da partida</button></div>`:""}<div class="game-main"><div class="game-team ${winner===p.time1?"winner":""}"><span class="team-badge">${teamFlagHtml(p.time1)}</span><b>${esc(p.time1)}</b></div><div class="game-score"><span>${esc(s[0])}</span><span>×</span><span>${esc(s[1])}</span></div><div class="game-team ${winner===p.time2?"winner":""}"><span class="team-badge">${teamFlagHtml(p.time2)}</span><b>${esc(p.time2)}</b></div></div><div class="game-phase">${esc(p.grupo||p.fase||"-")}</div>${goalTimelineHtml(events)}${detail?`<div class="game-extra">${esc(detail)}</div>`:""}</article>`;
}
function matchScoreboardHtml(c,p, showDetailsButton=true){
  const winner=matchWinner(c,p);
  const scorers=rawScorersForMatch(c,p);
  const decision=finalDecision(c,p);
  const detail=matchExtraDetail(p,decision);
  const s=scoreParts(p.placar), events=goalEvents(scorers,p);
  return `<article class="game-scoreboard"><div class="game-top"><span>Copa do Mundo FIFA ${esc(c.ano)} · ${esc(p.data||"-")} · ${esc(p.estadio||"-")}</span><span class="game-status">${esc(matchStatus(p))}</span></div>${showDetailsButton&&p.ficha?`<div class="game-detailbar"><button class="game-details-btn" data-uid="${esc(matchUid(c,p))}">Detalhes da partida</button></div>`:""}<div class="game-main"><div class="game-team ${winner===p.time1?"winner":""}"><span class="team-badge">${teamFlagHtml(p.time1)}</span><b>${esc(p.time1)}</b></div><div class="game-score"><span>${esc(s[0])}</span><span>×</span><span>${esc(s[1])}</span></div><div class="game-team ${winner===p.time2?"winner":""}"><span class="team-badge">${teamFlagHtml(p.time2)}</span><b>${esc(p.time2)}</b></div></div><div class="game-phase">${esc(p.grupo||p.fase||"-")}</div>${goalTimelineHtml(events)}${detail?`<div class="game-extra">${esc(detail)}</div>`:""}</article>`;
}
function detNorm(s){return String(s||"").normalize("NFKD").replace(/[\u0300-\u036f]/g,"").toLowerCase().replace(/[^a-z0-9]/g,"");}
function lineupCol(team,flagName,goalCounts={}){
  if(!team) return "";
  const goalBalls=name=>{
    const n=goalsForPlayer(name,goalCounts);
    return n ? `<span class="goal-balls" title="${n} ${n>1?"gols":"gol"}">${Array.from({length:n},()=>`<span class="goal-ball">⚽</span>`).join("")}</span>` : "";
  };
  const rows=arr=>arr.map(pl=>`<li><span class="lu-num">${esc(pl[0])}</span><span class="lu-pos">${esc(pl[1])}</span><span class="lu-name">${esc(pl[2])}${goalBalls(pl[2])}</span></li>`).join("");
  const res=(team.res&&team.res.length)?`<div class="lu-subhead">Entraram</div><ol class="lu-list lu-res">${rows(team.res)}</ol>`:"";
  return `<div class="lu-team"><div class="lu-head">${teamLabelHtml(flagName)}</div><ol class="lu-list">${rows(team.xi||[])}</ol>${res}<div class="lu-coach"><span>Treinador</span><b>${esc(team.tec||"—")}</b></div></div>`;
}
function matchModalHtml(c,p, includeHead=true){
  const f=p.ficha, s=scoreParts(p.placar);
  let a=f.t1,b=f.t2;
  if(a&&b&&detNorm(a.nome)!==detNorm(p.time1)&&detNorm(b.nome)===detNorm(p.time1)){a=f.t2;b=f.t1;}
  const goalCounts=lineupGoalCounts(c,p);
  const meta=[["Data",f.data],["Horário",f.hora],["Estádio",f.estadio],["Público",f.publico?f.publico+" torcedores":""],["Árbitro",f.arbitro?(f.arbitro+(f.arbitro_pais?" ("+f.arbitro_pais+")":"")):""],["Fase",p.grupo||p.fase]].filter(r=>r[1]);
  const head=includeHead ? `<div class="mm-head"><div class="mm-teams"><div class="mm-team">${teamFlagHtml(p.time1)}<b>${esc(p.time1)}</b></div><div class="mm-score">${esc(s[0])}<span>×</span>${esc(s[1])}</div><div class="mm-team">${teamFlagHtml(p.time2)}<b>${esc(p.time2)}</b></div></div><div class="mm-sub">Copa do Mundo FIFA ${esc(c.ano)} — ${esc(p.grupo||p.fase||"")}</div></div>` : "";
  return head+
    `<div class="mm-meta">${meta.map(r=>`<div class="mm-meta-item"><span>${esc(r[0])}</span><b>${esc(r[1])}</b></div>`).join("")}</div>`+
    `<h3 class="mm-h3">Escalações</h3><div class="mm-lineups">${lineupCol(a,p.time1,goalCounts.left)}${lineupCol(b,p.time2,goalCounts.right)}</div>`;
}
function combinedMatchModalHtml(c,p){
  const details=p.ficha ? `<section class="modal-details-section"><h3 class="mm-h3">Detalhes da partida</h3>${matchModalHtml(c,p,false)}</section>` : `<p class="note">Ficha detalhada ainda não disponível para esta partida.</p>`;
  return `<div class="modal-score-section">${matchScoreboardHtml(c,p,false)}</div>${details}`;
}
function openMatchModal(uid){
  const c=DATA.copas.find(x=>x.ano===state.cup); if(!c) return;
  const p=c.partidas.find(row=>matchUid(c,row)===uid); if(!p) return;
  if(!p.ficha && !usesModalDetail(c)) return;
  document.getElementById("modal-content").innerHTML=usesModalDetail(c) ? combinedMatchModalHtml(c,p) : matchModalHtml(c,p);
  document.getElementById("modal-content").scrollTop=0;
  document.getElementById("match-modal").classList.remove("hidden");
  document.body.style.overflow="hidden";
}
function closeMatchModal(){document.getElementById("match-modal").classList.add("hidden");document.body.style.overflow="";}
function rawScorersForMatch(c,p){return p.fase==="Fase de grupos" ? groupScorers(c,p) : (p.marcadores || scorerTextFromDetails(p.detalhes,p) || "-");}
function scorerTextFromDetails(details,p){
  const parts=String(details||"").split("|").map(x=>x.trim()).filter(Boolean);
  const goals=parts.filter(x=>/\d+(?:\+\d+)?'/.test(x) && !/(Público|Publico|Árbitro|Arbitro)/i.test(x));
  if(goals.length>=2) return `${p.time1}: ${goals[0]} | ${p.time2}: ${goals[1]}`;
  return goals[0] || "";
}
function matchExtraDetail(p,decision){
  const parts=String(p.detalhes||"").split("|").map(x=>x.trim()).filter(Boolean);
  const extra=parts.filter(x=>!(/\d+(?:\+\d+)?'/.test(x) && !/(Público|Publico|Árbitro|Arbitro)/i.test(x)));
  return [decision,...extra].filter(Boolean).join(" | ");
}
function splitScorersByTeam(raw,p){
  const text=String(raw||"").trim();
  if(!text || text==="-") return {left:"-",right:"-"};
  if(text.includes("|") && !text.toLowerCase().includes((p.time1+":").toLowerCase()) && !text.toLowerCase().includes((p.time2+":").toLowerCase())){
    const parts=text.split("|").map(x=>x.trim());
    return {left:parts[0]||"-",right:parts[1]||"-"};
  }
  const find=name=>text.toLowerCase().indexOf((name+":").toLowerCase());
  const i1=find(p.time1), i2=find(p.time2);
  if(i1>=0 && i2>=0){
    const first=i1<i2?{idx:i1,name:p.time1,side:"left"}:{idx:i2,name:p.time2,side:"right"};
    const second=i1<i2?{idx:i2,name:p.time2,side:"right"}:{idx:i1,name:p.time1,side:"left"};
    const out={left:"-",right:"-"};
    out[first.side]=text.slice(first.idx+first.name.length+1, second.idx).replace(/[;|\s]+$/,"").trim() || "-";
    out[second.side]=text.slice(second.idx+second.name.length+1).trim() || "-";
    return out;
  }
  if(i1>=0) return {left:text.slice(i1+p.time1.length+1).trim()||"-",right:"-"};
  if(i2>=0) return {left:"-",right:text.slice(i2+p.time2.length+1).trim()||"-"};
  return {left:text,right:"-"};
}
function goalEvents(raw,p){
  const split=splitScorersByTeam(raw,p);
  const left=splitGoalEvents(split.left).filter(x=>x!=="-").map(text=>({side:"left",team:p.time1,text,minute:goalMinute(text)}));
  const right=splitGoalEvents(split.right).filter(x=>x!=="-").map(text=>({side:"right",team:p.time2,text,minute:goalMinute(text)}));
  return [...left,...right].sort((a,b)=>a.minute-b.minute);
}
function lineupGoalCounts(c,p){
  const out={left:{},right:{}};
  goalEvents(rawScorersForMatch(c,p),p).forEach(e=>{
    const name=goalScorerName(e.text);
    if(!name) return;
    const key=detNorm(name);
    out[e.side][key]=(out[e.side][key]||0)+1;
  });
  return out;
}
function goalScorerName(text){
  return String(text||"")
    .replace(/\d+(?:\+\d+)?'.*$/,"")
    .replace(/\([^)]*\)/g,"")
    .replace(/\b(gol|gols|pen|pênalti|penalti)\b/gi,"")
    .replace(/[,:;|]+$/g,"")
    .trim();
}
function goalsForPlayer(player,counts){
  const pn=detNorm(player);
  if(!pn) return 0;
  let total=0;
  Object.entries(counts||{}).forEach(([scorer,n])=>{
    if(!scorer) return;
    if(pn===scorer || pn.endsWith(scorer) || scorer.endsWith(pn)) total+=n;
  });
  return total;
}
function goalMinute(text){const m=String(text||"").match(/(\d+)(?:\+(\d+))?'/); return m ? (+m[1])+(m[2]?+m[2]/100:0) : 999;}
function goalTimelineHtml(events){
  if(!events.length) return `<div class="goal-timeline"><div class="goal-event"><div class="blank"></div><div class="minute">-</div><div class="blank"></div></div></div>`;
  return `<div class="goal-timeline">${events.map(e=>`<div class="goal-event"><div class="${e.side==="left"?"left":"blank"}">${e.side==="left"?esc(e.text):""}</div><div class="minute">${esc(goalMinuteLabel(e.text))}</div><div class="${e.side==="right"?"right":"blank"}">${e.side==="right"?esc(e.text):""}</div></div>`).join("")}</div>`;
}
function goalMinuteLabel(text){const m=String(text||"").match(/(\d+(?:\+\d+)?)'/); return m ? `${m[1]}'` : "";}
function scorerListHtml(text){return splitGoalEvents(text).map(x=>`<div>${esc(x)}</div>`).join("") || "<div>-</div>";}
function splitGoalEvents(text){
  const raw=String(text||"-").trim();
  if(!raw || raw==="-") return ["-"];
  const normalized=raw.replace(/\s*\|\s*/g,"; ").replace(/\s*;\s*/g,"; ");
  if(normalized.includes(";")) return normalized.split(";").map(x=>x.trim()).filter(Boolean).flatMap(splitGoalEvents);
  const re=/([^,;]*?\d+(?:\+\d+)?'(?:\s*\([^)]*\))?)/g;
  const matches=[...normalized.matchAll(re)].map(m=>m[1].trim().replace(/^,\s*/,"")).filter(Boolean);
  if(matches.length<=1) return [normalized];
  let lastName="";
  return matches.map(item=>{
    if(/^[\d\s+']/.test(item) && lastName) return `${lastName} ${item}`.replace(/\s+/g," ");
    const name=item.replace(/\d+(?:\+\d+)?'.*$/,"").trim();
    if(name) lastName=name;
    return item;
  });
}
function matchStatus(p){const score=String(p.placar||"").toLowerCase(); if(score.includes("pen")) return "Pênaltis"; if(score.includes("pro")) return "Após prorrogação"; return p.fase==="Fase de grupos" ? "Tempo normal" : (p.fase||"Tempo normal");}
function teamAbbr(name){return String(name||"-").split(/\s+/).filter(Boolean).slice(0,3).map(w=>w[0]).join("").toUpperCase();}
function teamFlagHtml(name){const src=flagSrc(name); return src ? `<img class="flag-img" src="${src}" alt="${esc(name)}">` : esc(teamAbbr(name));}
function teamLabelHtml(name){const src=flagSrc(name); return src ? `<span class="team-label"><img class="inline-flag" src="${src}" alt="">${esc(name)}</span>` : esc(name);}
function cellHtml(v){return FLAG_CODES[v] ? teamLabelHtml(v) : esc(v);}
function renderTimeline(id, ed, selectable){
  const counts = {}, items = [], mobileItems = [];
  ed.forEach((e, idx)=>{
    const isOpen = e.futuro || !e.campeao || e.campeao === "Em aberto";
    if(!isOpen) counts[e.campeao] = (counts[e.campeao] || 0) + 1;
    const winner = isOpen ? esc(e.campeao && e.campeao !== "Em aberto" ? e.campeao : "Em aberto") : `${teamLabelHtml(e.campeao)} (${counts[e.campeao]})`;
    const active = selectable&&e.ano===state.cup ? "active" : "";
    const content = `<span class="event-stem"></span><div class="event-box"><span class="event-year">${e.ano}</span><span class="event-winner">${winner}</span>${selectable?`<span class="event-host">${esc(e.sede)}</span>`:""}</div>`;
    items.push(`<div class="cup-card ${idx%2===0?"above":"below"} ${active}" data-year="${e.ano}">${content}</div>`);
    mobileItems.push(`<div class="cup-card ${idx%2===0?"above":"below"} ${active}" data-year="${e.ano}">${content}</div>`);
  });
  const rows = [];
  const perRow = 8;
  for(let i=0;i<items.length;i+=perRow){
    const chunk = items.slice(i,i+perRow);
    const reverse = Math.floor(i/perRow)%2===1;
    rows.push(`<div class="timeline-row ${reverse?"reverse":""}">${(reverse?[...chunk].reverse():chunk).join("")}</div>`);
  }
  const mobileRows = [];
  const perMobileRow = 2;
  for(let i=0;i<mobileItems.length;i+=perMobileRow){
    const chunk = mobileItems.slice(i,i+perMobileRow);
    const reverse = Math.floor(i/perMobileRow)%2===1;
    mobileRows.push(`<div class="timeline-row ${reverse?"reverse":""}">${(reverse?[...chunk].reverse():chunk).join("")}</div>`);
  }
  const rowCount = rows.length;
  const mobileRowCount = mobileRows.length;
  document.getElementById(id).innerHTML=`<div class="timeline-desktop"><svg class="timeline-path" viewBox="0 0 1000 ${rowCount*242}" preserveAspectRatio="none" aria-hidden="true"><path d="${timelinePath(rowCount)}"></path></svg>${rows.join("")}</div><div class="timeline-mobile"><svg class="timeline-mobile-path" viewBox="0 0 1000 ${mobileRowCount*154}" preserveAspectRatio="none" aria-hidden="true"><path d="${timelineMobilePath(mobileRowCount)}"></path></svg>${mobileRows.join("")}</div>`;
  if(selectable){document.getElementById(id).onclick=e=>{const card=e.target.closest(".cup-card"); if(!card)return; state.cup=+card.dataset.year; state.selectedMatch=""; renderCopa();};}
}
function timelinePath(rowCount){
  const w=1000, rowH=242, y0=112, r=52;
  let d=`M 0 ${y0}`;
  for(let row=0; row<rowCount; row++){
    const y=y0+row*rowH, nextY=y+rowH, forward=row%2===0;
    if(forward){
      d+=` H ${row===rowCount-1?w:w-r}`;
      if(row<rowCount-1) d+=` Q ${w} ${y} ${w} ${y+r} V ${nextY-r} Q ${w} ${nextY} ${w-r} ${nextY}`;
    }else{
      d+=` H ${row===rowCount-1?0:r}`;
      if(row<rowCount-1) d+=` Q 0 ${y} 0 ${y+r} V ${nextY-r} Q 0 ${nextY} ${r} ${nextY}`;
    }
  }
  return d;
}
function timelineMobilePath(rowCount){
  const rowH=154, y0=78, left=250, right=750, edgePad=78, r=38;
  let d=`M ${left} ${y0}`;
  for(let row=0; row<rowCount; row++){
    const y=y0+row*rowH, nextY=y+rowH, forward=row%2===0;
    if(forward){
      d+=` H ${right}`;
      if(row<rowCount-1) d+=` Q ${1000-edgePad} ${y} ${1000-edgePad} ${y+r} V ${nextY-r} Q ${1000-edgePad} ${nextY} ${right} ${nextY}`;
    }else{
      d+=` H ${left}`;
      if(row<rowCount-1) d+=` Q ${edgePad} ${y} ${edgePad} ${y+r} V ${nextY-r} Q ${edgePad} ${nextY} ${left} ${nextY}`;
    }
  }
  return d;
}
function renderGroups(c){
  document.getElementById("copa-grupos-title").textContent=+c.ano===1950 ? "Fase inicial e quadrangular final" : "Fase de grupos";
  const by={}; c.grupos.forEach(r=>{(by[r.grupo] ||= []).push(r)});
  const entries=Object.entries(by);
  if(!entries.length){renderEditionFormat(c);return;}
  const host=document.getElementById("copa-grupos");
  host.innerHTML=`<div class="groups-grid">${entries.map(([g,rows])=>{
    const games=c.partidas.filter(p=>p.grupo===g);
    const selected=games.find(p=>matchUid(c,p)===state.selectedMatch);
    return `<section class="group-block"><div class="phase-title"><span>${esc(g)}</span><span>${games.length} jogos</span></div><div class="table-wrap"><table><thead><tr><th>#</th><th>Seleção</th><th>Pts</th><th>J</th><th>V</th><th>E</th><th>D</th><th>GP</th><th>GC</th><th>SG</th></tr></thead><tbody>${rows.map(r=>`<tr class="${isQualifiedGroupRow(r,rows)?"qualified-row":""}"><td class="num">${r.pos}</td><td>${teamLabelHtml(r.selecao)}</td><td class="num">${r.pts}</td><td class="num">${r.j}</td><td class="num">${r.v}</td><td class="num">${r.e}</td><td class="num">${r.d}</td><td class="num">${r.gp}</td><td class="num">${r.gc}</td><td>${esc(r.sg)}</td></tr>`).join("")}</tbody></table></div><div class="group-section-title">Jogos do grupo</div><div class="table-wrap"><table><thead><tr><th>Time 1</th><th>Placar</th><th>Time 2</th></tr></thead><tbody>${games.map(p=>{const id=matchUid(c,p); return `<tr class="match-row ${state.selectedMatch===id?"selected-match":""}" data-match-id="${esc(id)}"><td>${teamLabelHtml(p.time1)}</td><td>${esc(p.placar)}</td><td>${teamLabelHtml(p.time2)}</td></tr>`;}).join("")}</tbody></table></div>${selected&&!usesModalDetail(c)?`<div class="group-match-detail">${matchScoreboardHtml(c,selected)}</div>`:""}</section>`;
  }).join("")}</div>`;
  host.onclick=e=>{const row=e.target.closest("[data-match-id]"); if(!row)return; selectMatch(c,row.dataset.matchId);};
}
function renderEditionFormat(c){
  document.getElementById("copa-grupos-title").textContent="Formato da edição";
  const host=document.getElementById("copa-grupos");
  const phaseRows=Object.entries(groupBy(c.partidas,p=>p.fase||"Jogos")).map(([fase,rows])=>({fase,jogos:rows.length,gols:rows.reduce((a,p)=>a+num(p.gols),0)}));
  const groupGames=c.partidas.filter(p=>p.fase==="Fase de grupos");
  const legacyGroups=Object.entries(groupBy(groupGames,p=>p.grupo||"Primeira fase"));
  const format=FORMATOS_EDICAO[c.ano] || "Formato histórico diferente do modelo moderno de grupos; os jogos estão preservados nas tabelas da edição.";
  const cards=`<div class="format-grid">${phaseRows.map(r=>`<div class="format-card"><strong>${esc(r.fase)}</strong><span>${r.jogos} jogos</span><span>${r.gols} gols</span></div>`).join("")}</div>`;
  const note=`<div class="format-note">${esc(format)} A Wikipédia não trouxe uma tabela de classificação de grupos padronizada para esta edição no mesmo formato das Copas modernas; por isso esta área prioriza o regulamento e os jogos extraídos.</div>`;
  const games=legacyGroups.length ? `<div class="legacy-groups">${legacyGroups.map(([g,rows])=>`<section class="group-block"><div class="phase-title"><span>${esc(g)}</span><span>${rows.length} jogos</span></div><div class="table-wrap"><table>${tableHtml(["Data","Time 1","Placar","Time 2","Estádio"],rows.map(p=>[p.data,p.time1,p.placar,p.time2,p.estadio]))}</table></div></section>`).join("")}</div>` : "";
  host.innerHTML=`${note}${cards}${games}`;
}
function groupBy(rows, fn){return rows.reduce((acc,row)=>{const k=fn(row); (acc[k] ||= []).push(row); return acc;},{});}
function isQualifiedGroupRow(r, rows){const status=String(r.classificado||"").toLowerCase(); if(status.includes("eliminado")) return false; if(status) return true; return rows.length===4 && num(r.pos)<=2;}
function groupScorers(c,p){return p.marcadores || MARCADORES_GRUPOS[`${c.ano}|${p.grupo}|${p.time1}|${p.placar}|${p.time2}`] || "-";}

function renderSelecao(){
  updateHeroBandeira();
  const t=state.team||"Brasil", sel=DATA.selecoes.find(s=>s.selecao===t);
  const tsel=document.getElementById("team-select"); if(tsel) tsel.value=t;
  if(!sel){document.getElementById("kpis-selecao").innerHTML=kpis([["Seleção",t],["Sem dados","—"]]);return;}
  const camp=DATA.copas.map(c=>({ano:c.ano,...(c.classificacao_final.find(r=>r.selecao===t)||{})})).filter(r=>r.selecao).sort((a,b)=>a.ano-b.ano);
  const games=DATA.copas.flatMap(c=>c.partidas.filter(p=>p.time1===t||p.time2===t).map(p=>({ano:c.ano,...p})));
  if(!camp.some(r=>+r.ano===2026)){ // 2026 em andamento: se o time segue vivo (fora da classificação), deriva dos jogos
    const g26=games.filter(p=>+p.ano===2026);
    if(g26.length){
      const b={ano:2026,j:0,v:0,e:0,d:0,gp:0,gc:0,selecao:t};
      g26.forEach(p=>{const m=String(p.placar).match(/(\d+)\s*[-x]\s*(\d+)/); if(!m)return; const gf=p.time1===t?+m[1]:+m[2],ga=p.time1===t?+m[2]:+m[1]; b.j++;b.gp+=gf;b.gc+=ga;b[gf>ga?"v":gf<ga?"d":"e"]++;});
      b.pts=b.v*3+b.e; b.sg=(b.gp-b.gc>=0?"+":"")+(b.gp-b.gc);
      camp.push(b); camp.sort((a,b)=>a.ano-b.ano);
    }
  }
  document.getElementById("kpis-selecao").innerHTML=kpis([["Participações",sel.participacoes],["Melhor resultado",teamBest(sel)],["Títulos",sel.titulos],["Top 4",num(sel.titulos)+num(sel.vices)+num(sel.terceiros)+num(sel.quartos)],["Jogos",sel.j],["Aproveitamento",`${sel.aproveitamento}%`]]);
  renderTeamTraj(t,camp);
  renderTeamPositions(camp);
  renderTeamGols(camp);
  renderTeamVED(sel);
  renderTeamAdversarios(t,games);
  renderTeamScorers(t,camp);
  table("tbl-team-camp",["Ano","Resultado","Pts","J","V","E","D","GP","GC","SG"],camp.slice().reverse().map(r=>[r.ano,teamFinish(r.ano,t).label,r.pts,r.j,r.v,r.e,r.d,r.gp,r.gc,r.sg]),[0,2,3,4,5,6,7,8]);
  table("tbl-team-jogos",["Ano","Fase","Data","Time 1","Placar","Time 2","Estádio"],games.slice().reverse().map(p=>[p.ano,p.fase,p.data,p.time1,p.placar,p.time2,p.estadio]),[0]);
}
function renderAtaqueDefesa(){
  const host=document.getElementById("tbl-atkdef"); if(!host) return;
  const data=DATA.melhor_ataque_defesa||{};
  const anos=Object.keys(data).map(Number).sort((a,b)=>b-a);
  const body=anos.map(ano=>{
    const d=data[String(ano)], gc=d.defesa.gc, j=d.defesa.j;
    return `<tr><td class="num">${ano}</td>`+
      `<td>${teamLabelHtml(d.ataque.selecao)} <span class="ad-num ad-atk">${d.ataque.gp} gols</span></td>`+
      `<td>${teamLabelHtml(d.defesa.selecao)} <span class="ad-num ad-def">${gc} ${gc===1?"gol":"gols"} em ${j} jogos</span></td></tr>`;
  }).join("");
  host.innerHTML=`<thead><tr><th class="num">Ano</th><th>Melhor ataque</th><th>Melhor defesa</th></tr></thead><tbody>${body}</tbody>`;
}
function teamBest(sel){return num(sel.titulos)>0?"Campeão":num(sel.vices)>0?"Vice":num(sel.terceiros)>0?"3º lugar":num(sel.quartos)>0?"4º lugar":(sel.melhor_pos?num(sel.melhor_pos)+"º lugar":"—");}
function teamFinish(ano,team){const e=editionRow(ano); if(e.campeao===team)return{label:"Campeão",rank:1}; if(e.vice===team)return{label:"Vice",rank:2}; if(e.terceiro===team)return{label:"3º lugar",rank:3}; if(e.quarto===team)return{label:"4º lugar",rank:4}; const c=DATA.copas.find(x=>x.ano===ano), r=c&&c.classificacao_final.find(x=>x.selecao===team); return r?{label:`${num(r.pos)}º lugar`,rank:num(r.pos)}:{label:(+ano===2026?"Em andamento":"Participou"),rank:null};}
function trajColor(p){return p===1?COLORS[1]:p===2?"#cbd5e1":p===3?"#cd7f32":p===4?COLORS[3]:COLORS[2];}
function renderTeamTraj(t,camp){
  const pts=camp.filter(r=>num(r.pos)>0);
  Plotly.react("ch-team-traj",[{type:"scatter",mode:"lines+markers+text",x:pts.map(r=>String(r.ano)),y:pts.map(r=>num(r.pos)),text:pts.map(r=>String(num(r.pos))),textposition:"top center",textfont:{size:10,color:"#9eb8a8"},line:{color:"rgba(255,255,255,.28)",width:2},marker:{size:13,color:pts.map(r=>trajColor(num(r.pos))),line:{color:"#0b1b15",width:1.5}},hovertext:pts.map(r=>`${r.ano} — ${teamFinish(r.ano,t).label}`),hoverinfo:"text"}],layout({margin:{l:54,r:20,t:18,b:48},yaxis:{title:"Posição final",autorange:"reversed",gridcolor:"rgba(255,255,255,.08)"},xaxis:{type:"category",tickangle:-35}}),PCFG);
}
function renderTeamPositions(camp){
  const cnt={};
  camp.forEach(r=>{const p=num(r.pos); if(p>0) cnt[p]=(cnt[p]||0)+1;});
  const pos=Object.keys(cnt).map(Number).sort((a,b)=>a-b);
  Plotly.react("ch-team-pos",[{type:"bar",x:pos.map(p=>p+"º"),y:pos.map(p=>cnt[p]),marker:{color:pos.map(p=>trajColor(p)),cornerradius:3},text:pos.map(p=>cnt[p]),textposition:"outside",cliponaxis:false,hovertext:pos.map(p=>`${p}º lugar: ${cnt[p]}x`),hoverinfo:"text"}],layout({margin:{l:34,r:12,t:18,b:42},xaxis:{title:"Posição final",type:"category"},yaxis:{title:"Vezes",dtick:1,gridcolor:"rgba(255,255,255,.08)",rangemode:"tozero"}}),PCFG);
}
function renderTeamGols(camp){
  const x=camp.map(r=>String(r.ano));
  Plotly.react("ch-team-gols",[{type:"bar",x,y:camp.map(r=>num(r.gp)),name:"Gols pró",marker:{color:COLORS[0],cornerradius:3}},{type:"bar",x,y:camp.map(r=>num(r.gc)),name:"Gols contra",marker:{color:COLORS[3],cornerradius:3}}],layout({barmode:"group",xaxis:{type:"category",tickangle:-35},yaxis:{title:"Gols"},legend:{orientation:"h",y:-.28}}),PCFG);
}
function renderTeamVED(sel){
  Plotly.react("ch-team-ved",[{type:"pie",hole:.55,labels:["Vitórias","Empates","Derrotas"],values:[num(sel.v),num(sel.e),num(sel.d)],marker:{colors:[COLORS[0],COLORS[2],COLORS[3]]},textinfo:"label+value",hoverinfo:"label+value+percent",sort:false}],layout({showlegend:false,margin:{l:12,r:12,t:12,b:12}}),PCFG);
}
function renderTeamAdversarios(t,games){
  const rec={};
  games.forEach(p=>{const opp=p.time1===t?p.time2:p.time1; if(!opp)return; const m=String(p.placar||"").match(/(\d+)\s*[-x]\s*(\d+)/); if(!m)return; const gf=p.time1===t?+m[1]:+m[2], ga=p.time1===t?+m[2]:+m[1]; const r=rec[opp]||(rec[opp]={j:0,v:0,e:0,d:0}); r.j++; if(gf>ga)r.v++; else if(gf<ga)r.d++; else r.e++;});
  const rows=Object.entries(rec).map(([opp,r])=>[opp,r.j,r.v,r.e,r.d]).sort((a,b)=>b[1]-a[1]||b[2]-a[2]||a[0].localeCompare(b[0],"pt-BR"));
  table("tbl-team-adv",["Adversário","J","V","E","D"],rows,[1,2,3,4]);
}
function renderTeamScorers(t,camp){
  const host=document.getElementById("team-scorers"); if(!host) return;
  const data=(DATA.artilheiros_selecao&&DATA.artilheiros_selecao[t])||{};
  const ogData=(DATA.gols_contra_selecao&&DATA.gols_contra_selecao[t])||{};
  const anos=camp.map(r=>+r.ano).filter((v,i,a)=>a.indexOf(v)===i).sort((a,b)=>b-a);
  if(!anos.length){host.innerHTML=`<p class="ts-none">Sem dados de gols para esta seleção.</p>`;return;}
  host.innerHTML=anos.map(ano=>{
    const list=data[String(ano)]||[];
    const og=ogData[String(ano)]||[];
    const fin=teamFinish(ano,t);
    const cls=fin.rank&&fin.rank<=4?`r${fin.rank}`:"r0";
    const badge=`<span class="ts-fin ${cls}">${esc(fin.label)}</span>`;
    const ogTotal=og.reduce((a,b)=>a+b[1],0);
    const total=list.reduce((a,b)=>a+b[1],0)+ogTotal;
    const max=list.length?list[0][1]:0;
    const chips=list.map(([nome,g])=>`<span class="ts-chip${g===max?" top":""}">${esc(nome)}<b>${g}</b></span>`).join("");
    const ogNote=ogTotal?`<div class="ts-og"><b>${ogTotal>1?ogTotal+" gols contra":"1 gol contra"} a favor</b>: ${og.map(o=>esc(o[0])+(o[1]>1?` (${o[1]})`:"")).join(", ")} <span>— marcado por adversário; conta para a seleção, mas não para um artilheiro</span></div>`:"";
    const players=chips||(ogTotal?"":`<span class="ts-none">Não marcou gols nesta edição</span>`);
    return `<div class="ts-cup"><div class="ts-head"><span class="ts-year">${ano}</span>${badge}${total?`<span class="ts-total">${total} ${total>1?"gols":"gol"}</span>`:""}</div><div class="ts-body"><div class="ts-players">${players}</div>${ogNote}</div></div>`;
  }).join("");
}

function kpis(rows){return rows.map(([l,v])=>`<div class="kpi"><b>${esc(v)}</b><span>${esc(l)}</span></div>`).join("")}
function barH(id, rows, title, color){Plotly.react(id,[{type:"bar",orientation:"h",y:rows.map(r=>r[0]).reverse(),x:rows.map(r=>r[1]).reverse(),marker:{color,cornerradius:4},text:rows.map(r=>r[1]).reverse(),textposition:"outside",cliponaxis:false,hovertemplate:`<b>%{y}</b><br>${title}: %{x}<extra></extra>`}],layout({hovermode:"closest",margin:{l:132,r:42,t:10,b:45},xaxis:{title,showspikes:false,automargin:true},yaxis:{showspikes:false,automargin:true,tickfont:{size:11}}}),PCFG)}
const RANKS=[{id:"vitorias",key:"v",color:COLORS[0],nome:"vitórias"},{id:"empates",key:"e",color:COLORS[2],nome:"empates"},{id:"derrotas",key:"d",color:COLORS[3],nome:"derrotas"}];
function renderRankings(){
  const pct=state.rankMode==="pct";
  document.querySelectorAll("[data-rank-toggle]").forEach(b=>b.textContent = pct ? "Ver total" : "Ver %");
  const base=DATA.selecoes.filter(r=>r.selecao && num(r.j)>0);
  RANKS.forEach(rk=>{
    const rows=base.map(r=>{const tot=num(r[rk.key]), j=num(r.j); return {team:r.selecao, tot, j, val: pct ? tot/j*100 : tot};})
                   .sort((a,b)=>b.val-a.val || a.team.localeCompare(b.team,"pt-BR"));
    const max=Math.max(...rows.map(r=>r.val),1);
    document.getElementById("ch-ranking-"+rk.id).innerHTML=`<div class="rank-list">${rows.map(r=>{
      const w=(r.val/max*100).toFixed(1);
      const label=pct?`${r.val.toFixed(1)}%`:String(r.tot);
      const tip=`${r.team} — ${r.tot} ${rk.nome} em ${r.j} jogos`;
      return `<div class="rank-row" data-tip="${esc(tip)}"><span class="rank-label">${teamLabelHtml(r.team)}</span><div class="rank-bar-wrap"><div class="rank-bar" style="width:${w}%;background:${rk.color}"></div></div><span class="rank-val">${esc(label)}</span></div>`;
    }).join("")}</div>`;
  });
}
function initRankTips(){
  const tip=document.getElementById("rank-tip");
  ["ch-titulos","ch-podium",...RANKS.map(rk=>"ch-ranking-"+rk.id)].forEach(id=>{
    const host=document.getElementById(id);
    if(!host) return;
    host.addEventListener("mousemove",e=>{
      const row=e.target.closest(".rank-row");
      if(!row){tip.classList.remove("show");return;}
      tip.textContent=row.dataset.tip; tip.classList.add("show");
      let x=e.clientX+14, y=e.clientY+16;
      if(x+tip.offsetWidth>window.innerWidth-8) x=e.clientX-tip.offsetWidth-14;
      if(y+tip.offsetHeight>window.innerHeight-8) y=e.clientY-tip.offsetHeight-16;
      tip.style.left=x+"px"; tip.style.top=y+"px";
    });
    host.addEventListener("mouseleave",()=>tip.classList.remove("show"));
  });
}
function renderTitulos(){
  const rows=DATA.geral.podium.map(r=>[r.selecao,num(r.titulos)]).filter(r=>r[1]>0).sort((a,b)=>b[1]-a[1]||a[0].localeCompare(b[0],"pt-BR"));
  const max=Math.max(...rows.map(r=>r[1]),1);
  document.getElementById("ch-titulos").innerHTML=`<div class="rank-list">${rows.map(([team,val])=>{
    const tip=`${team} — ${val} ${val>1?"títulos":"título"}`;
    return `<div class="rank-row" data-tip="${esc(tip)}"><span class="rank-label">${teamLabelHtml(team)}</span><div class="rank-bar-wrap"><div class="rank-bar" style="width:${(val/max*100).toFixed(1)}%;background:${COLORS[1]}"></div></div><span class="rank-val">${val}</span></div>`;
  }).join("")}</div>`;
}
const PODIUM_SEGS=[["titulos",COLORS[1],"Títulos"],["vices",COLORS[2],"Vices"],["terceiros",COLORS[0],"3º lugares"],["quartos",COLORS[3],"4º lugares"]];
function renderPodium(){
  document.getElementById("podium-legend").innerHTML=PODIUM_SEGS.map(([k,c,n])=>`<span><i style="background:${c}"></i>${n}</span>`).join("");
  const rows=DATA.geral.podium.map(r=>{const o={team:r.selecao,titulos:num(r.titulos),vices:num(r.vices),terceiros:num(r.terceiros),quartos:num(r.quartos)}; o.total=o.titulos+o.vices+o.terceiros+o.quartos; return o;})
    .filter(r=>r.total>0).sort((a,b)=>b.total-a.total||b.titulos-a.titulos||b.vices-a.vices||b.terceiros-a.terceiros||b.quartos-a.quartos||a.team.localeCompare(b.team,"pt-BR"));
  const max=Math.max(...rows.map(r=>r.total),1);
  document.getElementById("ch-podium").innerHTML=`<div class="rank-list">${rows.map(r=>{
    const tip=`${r.team} — ${r.titulos} título(s), ${r.vices} vice(s), ${r.terceiros} 3º, ${r.quartos} 4º`;
    const segs=PODIUM_SEGS.map(([k,c])=>r[k]>0?`<div class="podium-seg" style="width:${(r[k]/r.total*100).toFixed(2)}%;background:${c}"></div>`:"").join("");
    return `<div class="rank-row" data-tip="${esc(tip)}"><span class="rank-label">${teamLabelHtml(r.team)}</span><div class="rank-bar-wrap"><div class="podium-bar" style="width:${(r.total/max*100).toFixed(1)}%">${segs}</div></div><span class="rank-val">${r.total}</span></div>`;
  }).join("")}</div>`;
}
function table(id, headers, rows, numeric=[]){document.getElementById(id).innerHTML=tableHtml(headers,rows,numeric)}
function tableHtml(headers, rows, numeric=[]){return `<thead><tr>${headers.map((h,i)=>`<th class="${numeric.includes(i)?"num":""}">${esc(h)}</th>`).join("")}</tr></thead><tbody>${rows.map(r=>`<tr>${r.map((c,i)=>`<td class="${numeric.includes(i)?"num":""}">${cellHtml(c)}</td>`).join("")}</tr>`).join("")}</tbody>`}
document.addEventListener("click",e=>{const b=e.target.closest(".game-details-btn"); if(b){openMatchModal(b.dataset.uid);return;} if(e.target.id==="match-modal") closeMatchModal();});
document.getElementById("modal-close").addEventListener("click",closeMatchModal);
document.addEventListener("keydown",e=>{if(e.key==="Escape")closeMatchModal();});
init();
</script>
</body>
</html>
"""


def main() -> None:
    payload = json.dumps(build_payload(), ensure_ascii=False, separators=(",", ":"))
    plotly = ensure_plotly()
    flags = json.dumps(ensure_flags(collect_flag_codes()), ensure_ascii=False, separators=(",", ":"))
    posters = json.dumps(ensure_posters(), ensure_ascii=False, separators=(",", ":"))
    trofeus = json.dumps(ensure_trofeus(), ensure_ascii=False, separators=(",", ":"))
    favicon = ensure_favicon()
    html = (
        HTML.replace("__DATA_PAYLOAD__", payload)
        .replace("__PLOTLY_PAYLOAD__", plotly)
        .replace("__FLAGS_PAYLOAD__", flags)
        .replace("__POSTERS_PAYLOAD__", posters)
        .replace("__TROFEUS_PAYLOAD__", trofeus)
        .replace("__FAVICON_PAYLOAD__", favicon)
    )
    OUT.write_text(html, encoding="utf-8")
    print(f"Dashboard gerado: {OUT}")


if __name__ == "__main__":
    main()
