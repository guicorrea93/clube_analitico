"""Gera base analitica unica de gols das Copas do Mundo.

Camada oficial: Wikipedia PT ja cacheada pelo dashboard.
Camada tecnica: StatsBomb Open Data, quando houver casamento por ano/selecao/minuto.
"""
from __future__ import annotations

import csv
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

import gerar_dashboard_copa_mundo_html as dash

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data" / "worldcup_wikipedia"
STATS_FILE = DATA_DIR / "gols_detalhados_statsbomb.json"
OUT_JSON = DATA_DIR / "gols_analiticos.json"
OUT_CSV = DATA_DIR / "gols_analiticos.csv"
OUT_AUDIT = DATA_DIR / "gols_analiticos_auditoria.csv"
RELATO_FILE = DATA_DIR / "situacao_relato.json"   # saida da varredura de relatos (fan-out)
FJELSTUL_FILE = DATA_DIR / "fjelstul_goals.csv"   # cache do Fjelstul World Cup Database


def _load_relato() -> dict:
    """{chave: {situacao, fonte, frase}} vindo da varredura de relatos de partida."""
    if not RELATO_FILE.exists():
        return {}
    try:
        return json.loads(RELATO_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


SITUACAO_RELATO = _load_relato()


def relato_key(edicao, selecao, minuto, jogador) -> str:
    return f"{edicao}|{norm(str(selecao))}|{minuto}|{norm(str(jogador))}"

OWN_RE = re.compile(r"contra|gol\s*contra|g\.?\s*c\.?|\bog\b|autogol|auto-gol", re.I)
PEN_RE = re.compile(r"pen|pên|penalti|pênalti", re.I)
OLIMPICO_RE = re.compile(r"gol\s+ol[ií]mpico", re.I)
FREE_KICK_RE = re.compile(r"\b(falta|free\s*kick|tiro\s+livre)\b", re.I)
HEADER_RE = re.compile(r"\b(cab|cabe[cç]a|cabeceio|header)\b", re.I)
OUTSIDE_BOX_RE = re.compile(r"\b(fora\s+da\s+[aá]rea|outside\s+the\s+box|dist[aâ]ncia)\b", re.I)
VOLLEY_RE = re.compile(r"\b(voleio|volei|volley)\b", re.I)
JUNK_RE = re.compile(r"(P[uú]blico|[AÁ]rbitro|Relat[oó]rio|Assist[eê]ncia|Est[aá]dio)", re.I)
MIN_RE = re.compile(r"(\d{1,3})(?:\+(\d{1,2}))?['’]")
ALIASES = {"Rivellino": "Rivelino"}

SUPPLEMENT_MATCH_GOALS = [
    {
        "edicao": 1970,
        "time_1": "México",
        "placar": "4 - 0",
        "time_2": "El Salvador",
        "selecao": "México",
        "jogador": "Valdivia",
        "minuto": 46,
        "acrescimo": None,
        "minuto_texto": "46'",
        "texto_original": "Valdivia 46' (complemento de auditoria)",
    },
]


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]", "", value.lower())


def clean_piece(value: str) -> str:
    value = re.sub(r"\[[^\]]+\]", "", value or "")
    value = value.replace("’", "'").replace("´", "'").replace("`", "'")
    value = re.sub(r"\s+", " ", value)
    return value.strip(" ,;.-")


def split_segments(raw: str, time1: str, time2: str, placar: str) -> list[tuple[str, str]]:
    """Retorna [(selecao_beneficiada, trecho_marcadores)]."""
    raw = clean_piece(raw)
    if not raw or raw == "-":
        return []
    raw = raw.replace("<", " ").replace(">", " ")
    raw = re.sub(r"(\d)['’]\+(\d)", r"\1+\2", raw)
    raw = re.sub(r"\s*\+\s*", "+", raw)
    raw = re.sub(r"['’]\s*\(", "' (", raw)
    n1, n2 = norm(time1), norm(time2)
    goals = dash.score_goals(placar) or (0, 0)
    labeled: list[tuple[str, str]] = []
    unlabeled: list[str] = []
    for seg in [s.strip() for s in raw.split("|") if s.strip()]:
        if ":" in seg:
            prefix, rest = seg.split(":", 1)
            np = norm(prefix)
            if np and (np == n1 or np in n1 or n1 in np):
                labeled.append((time1, rest.strip()))
                continue
            if np and (np == n2 or np in n2 or n2 in np):
                labeled.append((time2, rest.strip()))
                continue
        unlabeled.append(seg)
    if unlabeled:
        g1, g2 = goals
        if g1 == 0 and g2:
            labeled.extend((time2, seg) for seg in unlabeled)
        elif g2 == 0 and g1:
            labeled.extend((time1, seg) for seg in unlabeled)
        else:
            for idx, seg in enumerate(unlabeled):
                labeled.append((time1 if idx == 0 else time2, seg))
    return labeled


def split_goal_events(text: str) -> list[str]:
    text = clean_piece(text)
    if not text or text == "-":
        return []
    junk = JUNK_RE.search(text)
    if junk:
        text = text[: junk.start()].strip()
    text = re.sub(r"(\d{1,3}(?:\+\d{1,2})?)\s+(g\.?\s*c\.?)'", r"\1' (\2)", text, flags=re.I)
    text = re.sub(r"\s*;\s*", "; ", text)
    if ";" in text:
        out: list[str] = []
        for part in text.split(";"):
            out.extend(split_goal_events(part))
        return out
    leading_minutes = re.match(r"^((?:\d{1,3}(?:\+\d{1,2})?['’][,\s]*)+)\s+([^\d]+?)\s+(.+)$", text)
    if leading_minutes:
        name = clean_piece(leading_minutes.group(2))
        rest = clean_piece(leading_minutes.group(3))
        events = [f"{name} {m.group(0)}" for m in MIN_RE.finditer(leading_minutes.group(1))]
        events.extend(split_goal_events(rest))
        return events
    inverted = re.fullmatch(r"((?:\d{1,3}(?:\+\d{1,2})?['’][,\s]*)+)\s+(.+)", text)
    if inverted:
        name = clean_piece(inverted.group(2))
        return [f"{name} {m.group(0)}" for m in MIN_RE.finditer(inverted.group(1))]
    pattern = re.compile(r"([^;]*?\d{1,3}(?:\+\d{1,2})?['’](?:\s*\([^)]*\))?)")
    matches = [clean_piece(m.group(1)) for m in pattern.finditer(text)]
    if not matches:
        return []
    events: list[str] = []
    last_name = ""
    for raw in matches:
        minute = MIN_RE.search(raw)
        if not minute:
            continue
        before = clean_piece(raw[: minute.start()])
        after = clean_piece(raw[minute.end() :])
        name = clean_piece(before)
        if name:
            last_name = name
        else:
            name = last_name
        if not name:
            continue
        events.append(clean_piece(f"{name} {minute.group(0)} {after}"))
    return events


def scorer_name(event_text: str) -> str:
    text = clean_piece(event_text)
    minute = MIN_RE.search(text)
    name = text[: minute.start()] if minute else text
    name = OLIMPICO_RE.sub("", name)
    name = re.sub(r"\([^)]*\)", "", name)
    name = re.sub(r"\b(gol|gols|pen|pênalti|penalti)\b", "", name, flags=re.I)
    name = clean_piece(name)
    return ALIASES.get(name, name) or "Não identificado"


def canonical_player(selecao: str, edicao: int, jogador: str) -> str:
    key = norm(jogador)
    team = norm(selecao)
    if key == "ronaldo" and team == "portugal":
        return "Cristiano Ronaldo"
    if key == "ronaldo" and team == "brasil":
        return "Ronaldo"
    if key in {"muller", "mueller"} and team == "alemanha":
        return "Gerd Müller" if edicao <= 1974 else "Thomas Müller"
    if key == "messi" and team == "argentina":
        return "Lionel Messi"
    if key == "mbappe" and team == "franca":
        return "Kylian Mbappé"
    return jogador


def minute_parts(event_text: str) -> tuple[int | None, int | None, str]:
    m = MIN_RE.search(event_text or "")
    if not m:
        return None, None, ""
    minuto = int(m.group(1))
    acrescimo = int(m.group(2)) if m.group(2) else None
    label = f"{minuto}+{acrescimo}'" if acrescimo is not None else f"{minuto}'"
    return minuto, acrescimo, label


def official_type(event_text: str) -> str:
    if OWN_RE.search(event_text or ""):
        return "gol_contra"
    if PEN_RE.search(event_text or ""):
        return "penalti"
    return "normal"


def technical_hint(event_text: str) -> str:
    if OLIMPICO_RE.search(event_text or ""):
        return "Gol olímpico"
    if FREE_KICK_RE.search(event_text or ""):
        return "Falta"
    if VOLLEY_RE.search(event_text or ""):
        return "Voleio"
    return ""


def inferred_detail(tipo: str, event_text: str) -> dict:
    text = event_text or ""
    hint = technical_hint(text)
    detail = {
        "tipo_tecnico": "Não detalhado",
        "parte_corpo": "Não detalhado",
        "tecnica": "Não detalhado",
        "zona": "Não detalhado",
        "situacao_inferida": "",
        "eh_falta": False,
        "eh_cabeca": False,
        "eh_fora_area": False,
        "fonte_tecnica": "",
    }
    if tipo == "penalti":
        detail.update({"tipo_tecnico": "Pênalti", "tecnica": "Pênalti", "fonte_tecnica": "Wikipedia PT - marcador"})
    elif tipo == "gol_contra":
        detail.update({"tipo_tecnico": "Gol contra", "fonte_tecnica": "Wikipedia PT - marcador"})
    if hint:
        detail["fonte_tecnica"] = "Wikipedia PT - inferido"
        if hint == "Falta":
            detail["tipo_tecnico"] = "Falta"
            detail["tecnica"] = "Falta"
            detail["situacao_inferida"] = "Falta"
            detail["eh_falta"] = True
            detail["zona"] = "Fora da área"
            detail["eh_fora_area"] = True
        elif hint == "Gol olímpico":
            detail["tipo_tecnico"] = "Bola parada"
            detail["tecnica"] = "Gol olímpico"
            detail["situacao_inferida"] = "Escanteio"   # gol olimpico = direto de escanteio
        elif hint == "Voleio":
            detail["tecnica"] = "Voleio"
    if HEADER_RE.search(text):
        detail["parte_corpo"] = "Cabeça"
        detail["eh_cabeca"] = True
        if not detail["fonte_tecnica"]:
            detail["fonte_tecnica"] = "Wikipedia PT - inferido"
    if OUTSIDE_BOX_RE.search(text):
        detail["zona"] = "Fora da área"
        detail["eh_fora_area"] = True
        if not detail["fonte_tecnica"]:
            detail["fonte_tecnica"] = "Wikipedia PT - inferido"
    return detail


def load_statsbomb() -> dict[str, list[dict]]:
    if not STATS_FILE.exists():
        return {}
    payload = json.loads(STATS_FILE.read_text(encoding="utf-8"))
    out: dict[str, list[dict]] = defaultdict(list)
    for goal in payload.get("gols", []):
        if goal.get("periodo") == 5:
            continue
        key = f"{goal.get('ano')}|{norm(str(goal.get('selecao')))}"
        out[key].append(goal)
    for rows in out.values():
        rows.sort(key=lambda g: (g.get("minuto") or 0, g.get("segundo") or 0))
    return out


def pop_tech(stats: dict[str, list[dict]], ano: int, selecao: str, minuto: int | None, acrescimo: int | None) -> dict | None:
    if minuto is None:
        return None
    rows = stats.get(f"{ano}|{norm(str(selecao))}")
    if not rows:
        return None
    alvo = minuto + (acrescimo or 0)
    best_idx, best_delta = None, 999
    for idx, row in enumerate(rows):
        tech_min = int(row.get("minuto") or 0) + 1
        delta = abs(tech_min - alvo)
        if delta < best_delta:
            best_idx, best_delta = idx, delta
    if best_idx is not None and best_delta <= 1:
        return rows.pop(best_idx)
    return None


def _load_fjelstul_penalties() -> list[dict]:
    """Penaltis do Fjelstul World Cup DB: (edicao, minuto, total, sobrenome)."""
    if not FJELSTUL_FILE.exists():
        return []
    out: list[dict] = []
    with FJELSTUL_FILE.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if str(r.get("penalty")).strip() not in ("1", "TRUE", "True", "true", "yes"):
                continue
            m = re.match(r"WC-(\d{4})", r.get("tournament_id", ""))
            if not m:
                continue

            def _int(v):
                try:
                    return int(float(v))
                except (TypeError, ValueError):
                    return 0
            mn = _int(r.get("minute_regulation"))
            out.append({"edicao": int(m.group(1)), "minuto": mn,
                        "total": mn + _int(r.get("minute_stoppage")),
                        "sobrenome": norm(r.get("family_name", ""))})
    return out


def apply_fjelstul(goals: list[dict]) -> int:
    """Marca como Penalti gols que o Fjelstul aponta e que o marcador PT nao pegou."""
    pens = _load_fjelstul_penalties()
    if not pens:
        return 0
    by_ed: dict[int, list[dict]] = defaultdict(list)
    for g in goals:
        if g.get("minuto") is not None:
            by_ed[g["edicao"]].append(g)
    upgraded = 0
    for f in pens:
        for g in by_ed.get(f["edicao"], []):
            if g["situacao"] == "Pênalti":
                continue
            gm = g["minuto"]
            gtot = gm + (g.get("acrescimo") or 0)
            if abs(gtot - f["total"]) > 1 and abs(gm - f["minuto"]) > 1:
                continue
            sob = norm(str(g.get("jogador")))
            if f["sobrenome"] and (f["sobrenome"] in sob or sob in f["sobrenome"]):
                g.update({"situacao": "Pênalti", "tipo_oficial": "penalti", "eh_penalti": True,
                          "fonte_situacao": "Fjelstul WC Database"})
                upgraded += 1
                break
    return upgraded


def parse_match_goals(cup: dict, partida: dict, stats: dict[str, list[dict]]) -> list[dict]:
    ano = cup["ano"]
    time1, time2 = partida.get("time1", ""), partida.get("time2", "")
    placar = partida.get("placar", "")
    expected = dash.score_goals(placar) or (0, 0)
    rows: list[dict] = []
    for selecao, segment in split_segments(partida.get("marcadores") or "", time1, time2, placar):
        for event_text in split_goal_events(segment):
            minuto, acrescimo, minuto_texto = minute_parts(event_text)
            tipo = official_type(event_text)
            tech = pop_tech(stats, ano, selecao, minuto, acrescimo)
            rows.append(build_row(cup, partida, selecao, canonical_player(selecao, ano, scorer_name(event_text)), tipo, minuto, acrescimo, minuto_texto, event_text, tech))
    for extra in SUPPLEMENT_MATCH_GOALS:
        if (
            extra["edicao"] == ano
            and extra["time_1"] == time1
            and extra["placar"] == placar
            and extra["time_2"] == time2
        ):
            tech = pop_tech(stats, ano, extra["selecao"], extra["minuto"], extra["acrescimo"])
            rows.append(build_row(cup, partida, extra["selecao"], extra["jogador"], "normal", extra["minuto"], extra["acrescimo"], extra["minuto_texto"], extra["texto_original"], tech, confianca="media"))
    by_team = Counter(row["selecao"] for row in rows)
    missing = {time1: max(0, expected[0] - by_team[time1]), time2: max(0, expected[1] - by_team[time2])}
    for selecao, qtd in missing.items():
        for _ in range(qtd):
            rows.append(build_row(cup, partida, selecao, "Não identificado na fonte", "indefinido", None, None, "", "", None, confianca="baixa"))
    return rows


def build_row(
    cup: dict,
    partida: dict,
    selecao: str,
    jogador: str,
    tipo: str,
    minuto: int | None,
    acrescimo: int | None,
    minuto_texto: str,
    texto_original: str,
    tech: dict | None,
    confianca: str = "alta",
) -> dict:
    time1, time2 = partida.get("time1", ""), partida.get("time2", "")
    adversario = time2 if selecao == time1 else time1 if selecao == time2 else ""
    inferred = inferred_detail(tipo, texto_original)
    # --- situacao do gol (penalti/gol-contra/falta/escanteio/contra-ataque/bola rolando) ---
    if tipo == "gol_contra":
        situacao, fonte_situacao = "Gol contra", "Wikipedia PT - marcador"
    elif tipo == "penalti" or (tech and tech.get("eh_penalti")):
        situacao, fonte_situacao = "Pênalti", "Wikipedia PT - marcador"
    elif tech and tech.get("situacao"):
        situacao, fonte_situacao = tech["situacao"], "StatsBomb Open Data"
    elif inferred.get("situacao_inferida"):
        situacao, fonte_situacao = inferred["situacao_inferida"], "Wikipedia PT - inferido"
    else:
        situacao, fonte_situacao = "Não informado", ""
    frase_situacao = ""
    if situacao == "Não informado" and minuto is not None:   # completa com a varredura de relatos
        rel = SITUACAO_RELATO.get(relato_key(cup["ano"], selecao, minuto, jogador))
        if rel and rel.get("situacao"):
            situacao = rel["situacao"]
            fonte_situacao = rel.get("fonte", "Relato de partida")
            frase_situacao = rel.get("frase", "")
    return {
        "edicao": cup["ano"],
        "fase": partida.get("fase", ""),
        "grupo": partida.get("grupo", ""),
        "data": partida.get("data", ""),
        "partida": f"{time1} {partida.get('placar', '')} {time2}",
        "time_1": time1,
        "placar": partida.get("placar", ""),
        "time_2": time2,
        "estadio": partida.get("estadio", ""),
        "selecao": selecao,
        "adversario": adversario,
        "jogador": jogador,
        "minuto": minuto,
        "acrescimo": acrescimo,
        "minuto_texto": minuto_texto,
        "tipo_oficial": tipo,
        "tipo_tecnico": tech.get("tipo_chute_pt") if tech else inferred["tipo_tecnico"],
        "parte_corpo": tech.get("parte_corpo_pt") if tech else inferred["parte_corpo"],
        "tecnica": tech.get("tecnica_pt") if tech else inferred["tecnica"],
        "zona": tech.get("zona") if tech else inferred["zona"],
        "xg": tech.get("xg") if tech else None,
        "distancia_m": tech.get("distancia_m") if tech else None,
        "coordenada_x": tech.get("x") if tech else None,
        "coordenada_y": tech.get("y") if tech else None,
        "eh_penalti": tipo == "penalti" or bool(tech and tech.get("eh_penalti")),
        "eh_gol_contra": tipo == "gol_contra",
        "eh_falta": bool(tech and tech.get("eh_falta")) or inferred["eh_falta"],
        "eh_cabeca": bool(tech and tech.get("eh_cabeca")) or inferred["eh_cabeca"],
        "eh_fora_area": bool(tech and tech.get("eh_fora_area")) or inferred["eh_fora_area"],
        "situacao": situacao,
        "fonte_situacao": fonte_situacao,
        "frase_situacao": frase_situacao,
        "fonte_oficial": "Wikipedia PT",
        "fonte_tecnica": "StatsBomb Open Data" if tech else inferred["fonte_tecnica"],
        "nivel_confianca": confianca if jogador == "Não identificado na fonte" else ("alta" if tech or texto_original else "media"),
        "texto_original": texto_original,
    }


def build() -> tuple[list[dict], list[dict]]:
    stats = load_statsbomb()
    goals: list[dict] = []
    audit: list[dict] = []
    goal_id = 1
    for year in dash.YEARS:
        cup = dash.parse_worldcup_page(year)
        for idx, partida in enumerate(cup["partidas"], start=1):
            rows = parse_match_goals(cup, partida, stats)
            expected = sum(dash.score_goals(partida.get("placar")) or (0, 0))
            parsed = len(rows)
            if parsed != expected or any(r["nivel_confianca"] == "baixa" for r in rows):
                low = sum(1 for r in rows if r["nivel_confianca"] == "baixa")
                scope = "edicao_em_andamento" if year == 2026 else "historico"
                audit.append({
                    "edicao": year,
                    "fase": partida.get("fase", ""),
                    "partida": f"{partida.get('time1')} {partida.get('placar')} {partida.get('time2')}",
                    "gols_placar": expected,
                    "gols_base": parsed,
                    "gols_sem_autor": low,
                    "escopo": scope,
                    "observacao": "Marcadores ainda não preenchidos na base local de 2026." if scope == "edicao_em_andamento" else "Revisar marcador histórico.",
                    "marcadores": partida.get("marcadores", ""),
                })
            for row in rows:
                row["gol_id"] = goal_id
                row["partida_id_local"] = f"{year}-{idx:03d}"
                goals.append(row)
                goal_id += 1
    fj = apply_fjelstul(goals)
    print(f"Fjelstul: {fj} penaltis completados")
    return goals, audit


def write_outputs(goals: list[dict], audit: list[dict]) -> None:
    payload = {
        "metadata": {
            "descricao": "Base analitica de gols das Copas do Mundo: camada oficial Wikipedia PT + camada tecnica StatsBomb quando disponivel.",
            "total_gols": len(goals),
            "fontes": ["Wikipedia PT", "StatsBomb Open Data"],
        },
        "gols": goals,
        "auditoria": audit,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    fields = list(goals[0].keys()) if goals else []
    with OUT_CSV.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(goals)
    audit_fields = list(audit[0].keys()) if audit else ["edicao", "fase", "partida", "gols_placar", "gols_base", "gols_sem_autor", "marcadores"]
    with OUT_AUDIT.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=audit_fields)
        writer.writeheader()
        writer.writerows(audit)


def main() -> None:
    goals, audit = build()
    write_outputs(goals, audit)
    by_year = Counter(g["edicao"] for g in goals)
    tech = sum(1 for g in goals if g["fonte_tecnica"] == "StatsBomb Open Data")
    low = sum(1 for g in goals if g["nivel_confianca"] == "baixa")
    print(f"Gols analiticos: {len(goals)}")
    print(f"Com detalhe StatsBomb: {tech}")
    print(f"Sem autor parseavel: {low}")
    print(f"Edicoes: {dict(sorted(by_year.items()))}")
    print(f"JSON: {OUT_JSON}")
    print(f"CSV: {OUT_CSV}")
    print(f"Auditoria: {OUT_AUDIT}")


if __name__ == "__main__":
    main()
