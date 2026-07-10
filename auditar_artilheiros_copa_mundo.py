"""Audita artilheiros da Copa contra RSSSF top-100 (finais 1930-2022)."""
from __future__ import annotations

import csv
import html
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).parent
DB = ROOT / "db" / "copa_mundo.db"
RSSSF = ROOT / "data" / "worldcup_wikipedia" / "rsssf_30all_scor.html"
OUT_CSV = ROOT / "data" / "worldcup_wikipedia" / "auditoria_artilheiros_rsssf.csv"
OUT_MD = ROOT / "docs" / "auditoria_artilheiros_copa_mundo.md"

# Valores sem acento de proposito: a comparacao usa normalizacao.
PAISES = {
    "Argentina": "Argentina",
    "Australia": "Australia",
    "Austria": "Austria",
    "Belgium": "Belgica",
    "Brazil": "Brasil",
    "Bulgaria": "Bulgaria",
    "Cameroon": "Camaroes",
    "Colombia": "Colombia",
    "Costa Rica": "Costa Rica",
    "Croatia": "Croacia",
    "Czechoslovakia": "Tchecoslovaquia",
    "Denmark": "Dinamarca",
    "Ecuador": "Equador",
    "England": "Inglaterra",
    "France": "Franca",
    "Germany": "Alemanha",
    "Ghana": "Gana",
    "Hungary": "Hungria",
    "Italy": "Italia",
    "Mexico": "Mexico",
    "Netherlands": "Paises Baixos",
    "North Ireland": "Irlanda do Norte",
    "Peru": "Peru",
    "Poland": "Polonia",
    "Portugal": "Portugal",
    "Russia": "Russia",
    "Soviet Union": "Uniao Sovietica",
    "Spain": "Espanha",
    "Sweden": "Suecia",
    "Switzerland": "Suica",
    "United States": "Estados Unidos",
    "Uruguay": "Uruguai",
    "Yugoslavia": "Iugoslavia",
    "Scotland": "Escocia",
    "Denamrk": "Dinamarca",
    "Romania": "Romenia",
    "Slovakia": "Eslovaquia",
    "Japan": "Japao",
}

ALIASES_RSSSF_BANCO = {
    ("miroslavklose", "alemanha"): "klose",
    ("ronaldoluisnazariodelima", "brasil"): "ronaldo",
    ("gerhardmuller", "alemanha"): "gerdmuller",
    ("justfontaine", "franca"): "fontaine",
    ("lionelmessi", "argentina"): "messi",
    ("peleedsonarantesdonascimento", "brasil"): "pele",
    ("kylianmbappe", "franca"): "mbappe",
    ("sandorkocsispeter", "hungria"): "kocsis",
    ("jurgenklinsmann", "alemanha"): "klinsmann",
    ("helmutrahn", "alemanha"): "rahn",
    ("teofilocubillasarizaga", "peru"): "cubillas",
    ("grzegorzboleslawlato", "polonia"): "lato",
    ("garywinstonlineker", "inglaterra"): "lineker",
    ("gabrielomarbatistuta", "argentina"): "batistuta",
    ("thomasmuller", "alemanha"): "thomasmuller",
    ("ademirmarquesdemenezes", "brasil"): "ademir",
    ("vavaedvaldoizidioneto", "brasil"): "vava",
    ("eusebiodasilvaferreira", "portugal"): "eusebio",
    ("uweseeler", "alemanha"): "seeler",
    ("jairzinhojairventurafilho", "brasil"): "jairzinho",
    ("paolorossi", "italia"): "rossi",
    ("karlheinzrummenigge", "alemanha"): "rummenigge",
    ("robertobaggio", "italia"): "baggio",
    ("christianvieri", "italia"): "vieri",
    ("davidvilla", "espanha"): "villa",
    ("guillermostabile", "argentina"): "stabile",
    ("leonidasdasilva", "brasil"): "leonidas",
    ("oscaromarmiguez", "uruguai"): "miguez",
    ("diegoarmandomaradona", "argentina"): "maradona",
    ("rudolfvoller", "alemanha"): "voller",
    ("rivaldovictorborbaferreira", "brasil"): "rivaldo",
    ("cristianoronaldodossantosaveiro", "portugal"): "cristianoronaldo",
    ("neymardasilvasantosjunior", "brasil"): "neymar",
    ("harryedwardkane", "inglaterra"): "kane",
    ("helmuthaller", "alemanha"): "haller",
    ("lotharherbertmatthaus", "alemanha"): "matthaus",
    ("davorsuker", "croacia"): "suker",
    ("asamoahgyan", "gana"): "gyan",
    ("arjenrobben", "paisesbaixos"): "robben",
    ("robinvanpersie", "paisesbaixos"): "vanpersie",
    ("ennervalencia", "equador"): "valencia",
    ("valentinkozmichivanov", "uniaosovietica"): "vivanov",
    ("garrinchamanuelfranciscodossantos", "brasil"): "garrincha",
    ("franzbeckenbauer", "alemanha"): "beckenbauer",
    ("zicoarthurantunescoimbra", "brasil"): "zico",
    ("emiliobutraguenosantos", "espanha"): "butragueno",
    ("romariodasousafariafilho", "brasil"): "romario",
    ("marcrobertwilmots", "belgica"): "wilmots",
    ("estanislaobasorabrunet", "espanha"): "basora",
    ("zarratelmozarraonaindiamontoya", "espanha"): "zarra",
    ("ferencpuskasbiro", "hungria"): "puskas",
    ("nandorhidegkuti", "hungria"): "hidegkuti",
    ("kurthamrin", "suecia"): "hamrin",
    ("agnesimonsson", "suecia"): "simonsson",
    ("drazanjerkovic", "iugoslavia"): "djerkovic",
    ("florianalbert", "hungria"): "albert",
    ("leonelsanchezlineros", "chile"): "leonelsanchez",
    ("robertcharlton", "inglaterra"): "charlton",
    ("reneorlandohouseman", "argentina"): "houseman",
    ("josephjordan", "escocia"): "joe jordan",
    ("jorgealbertofranciscovaldano", "argentina"): "valdano",
    ("prebenelkjaerlarsen", "dinamarca"): "elkjaer",
    ("michelmiguelgonzalezmariadelcampo", "espanha"): "michel",
    ("claudiopaulcaniggia", "argentina"): "caniggia",
    ("florinvaleriuraducioiu", "romenia"): "raducioiu",
    ("luisarturohernandezcarreon", "mexico"): "luishernandez",
    ("robertvittek", "eslovaquia"): "vittek",
    ("keisukehonda", "japao"): "honda",
}

DIVERGENCIAS_CONHECIDAS = {
    ("leonidasdasilva", "brasil"): (
        "Mantido como divergencia de criterio: RSSSF lista 8 gols, mas a Wikipedia PT de 1938 "
        "credita a Leônidas 7 gols e informa que a FIFA reatribuiu a Roberto o gol do replay "
        "Brasil 2 x 1 Tchecoslovaquia."
    ),
}


def normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto or "")
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", texto.lower())


def limpar_nome_rsssf(nome: str) -> str:
    nome = nome.replace(" - ", " ")
    nome = re.sub(r"\s+", " ", nome)
    return nome.strip()


def parse_rsssf() -> list[dict]:
    for encoding in ("utf-8", "utf-16", "latin-1"):
        try:
            raw = RSSSF.read_text(encoding=encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise UnicodeDecodeError("rsssf", b"", 0, 1, "encoding nao suportado")
    pre = re.search(r"<PRE>(.*?)</PRE>", raw, re.S | re.I)
    texto = html.unescape(pre.group(1) if pre else raw)
    rows = []
    for line in texto.splitlines():
        line = line.rstrip()
        m = re.match(r"^(.+?)\s*\(([^)]+)\)\s+(\d+)\s+(\d{4}(?:-\d{4})?)\s*$", line)
        if not m:
            continue
        nome, pais, gols, anos = m.groups()
        selecao = PAISES.get(pais, pais)
        rows.append(
            {
                "nome_rsssf": limpar_nome_rsssf(nome),
                "nome_norm_rsssf": normalizar(limpar_nome_rsssf(nome)),
                "selecao": selecao,
                "selecao_norm": normalizar(selecao),
                "gols_rsssf": int(gols),
                "periodo_rsssf": anos,
            }
        )
    return rows


def carregar_banco() -> tuple[dict[tuple[str, str], dict], dict[tuple[str, int], list[dict]]]:
    con = sqlite3.connect(DB)
    rows = con.execute(
        """
        SELECT
            ip.nome_canonico,
            s.nome AS selecao,
            COUNT(*) AS gols,
            MIN(e.ano) AS primeiro_ano,
            MAX(e.ano) AS ultimo_ano
        FROM gol g
        JOIN edicao e ON e.edicao_id = g.edicao_id
        JOIN pessoa p ON p.pessoa_id = g.pessoa_id
        JOIN identidade_pessoa ip ON ip.identidade_pessoa_id = p.identidade_pessoa_id
        JOIN selecao s ON s.selecao_id = COALESCE(g.selecao_autor_id, g.selecao_id)
        WHERE g.tipo <> 'gol_contra' AND e.ano <= 2022
        GROUP BY ip.identidade_pessoa_id, s.nome
        """
    ).fetchall()
    con.close()

    por_nome = {}
    por_selecao_gols = {}
    for nome, selecao, gols, primeiro, ultimo in rows:
        registro = {
            "nome_banco": nome,
            "selecao": selecao,
            "gols_banco": gols,
            "periodo_banco": f"{primeiro}-{ultimo}" if primeiro != ultimo else str(primeiro),
        }
        selecao_norm = normalizar(selecao)
        por_nome[(normalizar(nome), selecao_norm)] = registro
        por_selecao_gols.setdefault((selecao_norm, gols), []).append(registro)
    return por_nome, por_selecao_gols


def escolher_match_por_gols(candidatos: list[dict], periodo_rsssf: str) -> dict | None:
    if len(candidatos) == 1:
        return candidatos[0]
    mesmos_periodos = [c for c in candidatos if c["periodo_banco"] == periodo_rsssf]
    if len(mesmos_periodos) == 1:
        return mesmos_periodos[0]
    return None


def auditar() -> list[dict]:
    ref = parse_rsssf()
    banco, por_selecao_gols = carregar_banco()
    saida = []

    for r in ref:
        chave_alias = (r["nome_norm_rsssf"], r["selecao_norm"])
        nome_match = ALIASES_RSSSF_BANCO.get(chave_alias, r["nome_norm_rsssf"])
        b = banco.get((nome_match, r["selecao_norm"]))
        criterio_match = "nome"

        if not b:
            candidatos = por_selecao_gols.get((r["selecao_norm"], r["gols_rsssf"]), [])
            b = escolher_match_por_gols(candidatos, r["periodo_rsssf"])
            criterio_match = "selecao_e_gols" if b else ""

        status = "sem_match"
        diferenca = ""
        if b:
            diferenca = b["gols_banco"] - r["gols_rsssf"]
            status = "ok" if diferenca == 0 else "divergente"

        saida.append(
            {
                "status": status,
                "nome_rsssf": r["nome_rsssf"],
                "selecao": b["selecao"] if b else r["selecao"],
                "gols_rsssf": r["gols_rsssf"],
                "periodo_rsssf": r["periodo_rsssf"],
                "nome_banco": b["nome_banco"] if b else "",
                "gols_banco": b["gols_banco"] if b else "",
                "periodo_banco": b["periodo_banco"] if b else "",
                "diferenca": diferenca,
                "criterio_match": criterio_match,
                "observacao": DIVERGENCIAS_CONHECIDAS.get((r["nome_norm_rsssf"], r["selecao_norm"]), ""),
            }
        )

    return saida


def escrever(saida: list[dict]) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    campos = [
        "status",
        "nome_rsssf",
        "selecao",
        "gols_rsssf",
        "periodo_rsssf",
        "nome_banco",
        "gols_banco",
        "periodo_banco",
        "diferenca",
        "criterio_match",
        "observacao",
    ]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=campos)
        wr.writeheader()
        wr.writerows(saida)

    total = len(saida)
    ok = sum(1 for r in saida if r["status"] == "ok")
    divergentes = [r for r in saida if r["status"] == "divergente"]
    sem_match = [r for r in saida if r["status"] == "sem_match"]
    linhas_md = [
        "# Auditoria de artilheiros da Copa do Mundo",
        "",
        "Fonte externa: RSSSF, `World Cup 1930-2022 - Final Tournaments - Top-100 Goal Scorers`.",
        "",
        "Recorte auditado: gols em fases finais de Copas do Mundo ate 2022. A Copa de 2026 fica fora desta auditoria por estar em andamento no payload local.",
        "",
        f"- Registros RSSSF comparados: {total}",
        f"- Batimentos com mesmo total de gols: {ok}",
        f"- Divergencias de gols: {len(divergentes)}",
        f"- Sem correspondencia automatica: {len(sem_match)}",
        "",
        "## Divergencias",
        "",
    ]
    if divergentes:
        linhas_md.append("| Jogador RSSSF | Selecao | RSSSF | Banco | Diferenca | Observacao |")
        linhas_md.append("| --- | --- | ---: | ---: | ---: | --- |")
        for r in divergentes:
            linhas_md.append(
                f"| {r['nome_rsssf']} | {r['selecao']} | {r['gols_rsssf']} | {r['gols_banco']} | {r['diferenca']} | {r['observacao']} |"
            )
    else:
        linhas_md.append("Nenhuma divergencia de gols nos registros com correspondencia automatica.")

    linhas_md += ["", "## Sem correspondencia automatica", ""]
    if sem_match:
        linhas_md.append("| Jogador RSSSF | Selecao | Gols | Periodo |")
        linhas_md.append("| --- | --- | ---: | --- |")
        for r in sem_match:
            linhas_md.append(f"| {r['nome_rsssf']} | {r['selecao']} | {r['gols_rsssf']} | {r['periodo_rsssf']} |")
    else:
        linhas_md.append("Todos os registros RSSSF tiveram correspondencia automatica no banco.")

    linhas_md += [
        "",
        "## Observacao",
        "",
        "A auditoria usa `identidade_pessoa` para evitar separar o mesmo jogador por alias. Gols contra sao excluidos do total de artilharia. Quando a RSSSF usa nome completo e o banco usa nome esportivo, a rotina tenta bater por alias e, em seguida, por combinacao unica de selecao e total de gols.",
    ]
    OUT_MD.write_text("\n".join(linhas_md) + "\n", encoding="utf-8")


def main() -> None:
    if not DB.exists():
        raise SystemExit(f"Banco nao encontrado: {DB}")
    if not RSSSF.exists():
        raise SystemExit(f"Referencia RSSSF nao encontrada: {RSSSF}")
    saida = auditar()
    escrever(saida)
    print(f"Auditoria gerada: {OUT_MD}")
    print(f"CSV gerado: {OUT_CSV}")
    print(f"OK: {sum(1 for r in saida if r['status'] == 'ok')} / {len(saida)}")
    print(f"Divergentes: {sum(1 for r in saida if r['status'] == 'divergente')}")
    print(f"Sem match: {sum(1 for r in saida if r['status'] == 'sem_match')}")


if __name__ == "__main__":
    main()
