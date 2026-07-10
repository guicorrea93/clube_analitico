"""Cria db/copa_mundo.db a partir do payload atual do dashboard das Copas.

Tabelas e colunas ficam em portugues. O script preserva aliases em tabelas
auditaveis para evitar misturar pessoas diferentes com o mesmo apelido.
"""
from __future__ import annotations

import argparse
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

import gerar_dashboard_copa_mundo_html as copa

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).parent
DB = ROOT / "db" / "copa_mundo.db"
SCHEMA = ROOT / "sql" / "schema_copa_mundo.sql"

FONTES = {
    "Wikipedia PT": ("https://pt.wikipedia.org/wiki/Copa_do_Mundo_FIFA", "primaria", "Fonte usada pelo dashboard e cache local."),
    "RSSSF": ("https://www.rsssf.org/tablesw/worldcup.html", "cruzamento", "Referência independente para placares, rankings, artilheiros e treinadores."),
    "FIFA": ("https://www.fifa.com/en/tournaments/mens/worldcup", "cruzamento", "Fonte oficial da competição."),
    "Wikidata": ("https://www.wikidata.org/", "identidade", "Identificadores estáveis de pessoas e entidades."),
}

# (selecao, alias, papel) -> nome canonico, wikidata, observacao
ALIASES_PESSOA = {
    ("Portugal", "Ronaldo", "jogador"): (
        "Cristiano Ronaldo",
        "Q11571",
        "Em Portugal, o marcador 'Ronaldo' nas Copas de 2006+ se refere a Cristiano Ronaldo.",
    ),
    ("Portugal", "Cristiano Ronaldo", "jogador"): ("Cristiano Ronaldo", "Q11571", "Nome completo."),
    ("Portugal", "C. Ronaldo", "jogador"): ("Cristiano Ronaldo", "Q11571", "Abreviação comum."),
    ("Brasil", "Ronaldinho", "jogador"): ("Ronaldinho Gaúcho", "Q39444", "Evita separar Ronaldinho de Ronaldinho Gaúcho."),
    ("Brasil", "Ronaldinho Gaúcho", "jogador"): ("Ronaldinho Gaúcho", "Q39444", "Nome canônico no dashboard."),
}

# Aliases adicionais validados na auditoria RSSSF x banco.
ALIASES_PESSOA.update({
    ("Polônia", "Lato", "jogador"): ("Grzegorz Lato", None, "Unifica sobrenome e nome completo."),
    ("Polônia", "Grzegorz Lato", "jogador"): ("Grzegorz Lato", None, "Nome completo."),
    ("Inglaterra", "Lineker", "jogador"): ("Gary Lineker", None, "Unifica sobrenome e nome completo."),
    ("Inglaterra", "Gary Lineker", "jogador"): ("Gary Lineker", None, "Nome completo."),
    ("Itália", "Rossi", "jogador"): ("Paolo Rossi", None, "Unifica sobrenome e nome completo."),
    ("Itália", "Paolo Rossi", "jogador"): ("Paolo Rossi", None, "Nome completo."),
    ("Itália", "Baggio", "jogador"): ("Roberto Baggio", None, "Alias usado para Roberto Baggio."),
    ("Itália", "R. Baggio", "jogador"): ("Roberto Baggio", None, "Inicial usada para Roberto Baggio."),
    ("Itália", "Roberto Baggio", "jogador"): ("Roberto Baggio", None, "Nome completo."),
    ("Polônia", "Szarmach", "jogador"): ("Andrzej Szarmach", None, "Unifica sobrenome e nome completo."),
    ("Polônia", "Andrzej Szarmach", "jogador"): ("Andrzej Szarmach", None, "Nome completo."),
    ("Suécia", "Edström", "jogador"): ("Ralf Edström", None, "Unifica sobrenome e nome completo."),
    ("Suécia", "Ralf Edström", "jogador"): ("Ralf Edström", None, "Nome completo."),
    ("Polônia", "Deyna", "jogador"): ("Kazimierz Deyna", None, "Unifica sobrenome e nome completo."),
    ("Polônia", "Kazimierz Deyna", "jogador"): ("Kazimierz Deyna", None, "Nome completo."),
    ("Alemanha", "Breitner", "jogador"): ("Paul Breitner", None, "Unifica sobrenome e nome completo."),
    ("Alemanha", "Paul Breitner", "jogador"): ("Paul Breitner", None, "Nome completo."),
    ("França", "Rocheteau", "jogador"): ("Dominique Rocheteau", None, "Unifica sobrenome e nome completo."),
    ("França", "Dominique Rocheteau", "jogador"): ("Dominique Rocheteau", None, "Nome completo."),
    ("Alemanha", "Brehme", "jogador"): ("Andreas Brehme", None, "Unifica sobrenome e nome completo."),
    ("Alemanha", "Andreas Brehme", "jogador"): ("Andreas Brehme", None, "Nome completo."),
    ("Gana", "Gyan", "jogador"): ("Asamoah Gyan", None, "Unifica sobrenome e nome completo."),
    ("Gana", "A. Gyan", "jogador"): ("Asamoah Gyan", None, "Inicial usada para Asamoah Gyan."),
    ("Gana", "Asamoah Gyan", "jogador"): ("Asamoah Gyan", None, "Nome completo."),
    ("Equador", "Valencia", "jogador"): ("Enner Valencia", None, "Alias usado para Enner Valencia."),
    ("Equador", "E. Valencia", "jogador"): ("Enner Valencia", None, "Inicial usada para Enner Valencia."),
    ("Equador", "Enner Valencia", "jogador"): ("Enner Valencia", None, "Nome completo."),
    ("União Soviética", "V. Ivanov", "jogador"): ("Valentin Ivanov", None, "Inicial usada para Valentin Ivanov."),
    ("União Soviética", "Ivanov", "jogador"): ("Valentin Ivanov", None, "Alias usado para Valentin Ivanov."),
    ("União Soviética", "Valentin Ivanov", "jogador"): ("Valentin Ivanov", None, "Nome completo."),
    ("Argentina", "Houseman", "jogador"): ("René Houseman", None, "Unifica sobrenome e nome completo."),
    ("Argentina", "René Houseman", "jogador"): ("René Houseman", None, "Nome completo."),
    ("Argentina", "Caniggia", "jogador"): ("Claudio Caniggia", None, "Unifica sobrenome e nome completo."),
    ("Argentina", "Claudio Caniggia", "jogador"): ("Claudio Caniggia", None, "Nome completo."),
})

# (selecao, alias, papel, ano) -> nome canonico, wikidata, observacao.
# Resolve aliases curtos que mudam de jogador dentro da mesma selecao.
ALIASES_PESSOA_ANO = {
    ("Alemanha", "Müller", "jogador", 1970): ("Gerd Müller", "Q152871", "Alias Müller na Alemanha de 1970."),
    ("Alemanha", "Müller", "jogador", 1974): ("Gerd Müller", "Q152871", "Alias Müller na Alemanha de 1974."),
    ("Alemanha", "Müller", "jogador", 2010): ("Thomas Müller", "Q15789", "Alias Müller na Alemanha de 2010."),
    ("Alemanha", "Müller", "jogador", 2014): ("Thomas Müller", "Q15789", "Alias Müller na Alemanha de 2014."),
    ("México", "Hernández", "jogador", 1962): ("Héctor Hernández", None, "Alias Hernández no México de 1962."),
    ("México", "Hernández", "jogador", 1998): ("Luis Hernández", None, "Alias Hernández no México de 1998."),
    ("México", "Hernández", "jogador", 2010): ("Javier Hernández", None, "Alias Hernández no México de 2010."),
    ("México", "Hernández", "jogador", 2014): ("Javier Hernández", None, "Alias Hernández no México de 2014."),
    ("México", "Hernández", "jogador", 2018): ("Javier Hernández", None, "Alias Hernández no México de 2018."),
    ("Chile", "Sánchez", "jogador", 1962): ("Leonel Sánchez", None, "Alias Sánchez no Chile de 1962."),
    ("Chile", "Sánchez", "jogador", 2014): ("Alexis Sánchez", None, "Alias Sánchez no Chile de 2014."),
    ("México", "Sánchez", "jogador", 1986): ("Hugo Sánchez", None, "Alias Sánchez no México de 1986."),
    ("Países Baixos", "de Jong", "jogador", 1974): ("Theo de Jong", None, "Alias de Jong nos Países Baixos de 1974."),
    ("Países Baixos", "de Jong", "jogador", 2022): ("Frenkie de Jong", None, "Alias de Jong nos Países Baixos de 2022."),
    ("Escócia", "Collins", "jogador", 1958): ("Bobby Collins", None, "Alias Collins na Escócia de 1958."),
    ("Escócia", "Collins", "jogador", 1998): ("John Collins", None, "Alias Collins na Escócia de 1998."),
    ("Brasil", "Oscar", "jogador", 1982): ("José Oscar Bernardi", None, "Alias Oscar no Brasil de 1982."),
    ("Brasil", "Oscar", "jogador", 2014): ("Oscar", None, "Alias Oscar no Brasil de 2014."),
    ("Dinamarca", "Eriksen", "jogador", 1986): ("John Eriksen", None, "Alias Eriksen na Dinamarca de 1986."),
    ("Dinamarca", "Eriksen", "jogador", 2018): ("Christian Eriksen", None, "Alias Eriksen na Dinamarca de 2018."),
    ("Hungria", "Tóth", "jogador", 1954): ("Mihály Tóth", None, "Alias Tóth na Hungria de 1954."),
    ("Hungria", "Tóth", "jogador", 1982): ("József Tóth", None, "Alias Tóth na Hungria de 1982."),
    ("Espanha", "Juanito", "jogador", 1982): ("Juan Gómez", None, "Alias Juanito na Espanha de 1982."),
    ("Espanha", "Juanito", "jogador", 2006): ("Juan Gutiérrez Moreno", None, "Alias Juanito na Espanha de 2006."),
    ("África do Sul", "Mokoena", "jogador", 2002): ("Aaron Mokoena", None, "Alias Mokoena na África do Sul de 2002."),
    ("África do Sul", "Mokoena", "jogador", 2026): ("Teboho Mokoena", None, "Alias Mokoena na África do Sul de 2026."),
    ("Brasil", "Júnior", "jogador", 1982): ("Leovegildo Júnior", None, "Alias Júnior no Brasil de 1982."),
    ("Brasil", "Júnior", "jogador", 2002): ("Jenílson Ângelo de Souza", None, "Alias Júnior no Brasil de 2002."),
    ("Japão", "Nakamura", "jogador", 2006): ("Shunsuke Nakamura", None, "Alias Nakamura no Japão de 2006."),
    ("Brasil", "Mazzola", "jogador", 1958): ("José Altafini", None, "Alias Mazzola no Brasil de 1958."),
    ("Itália", "Mazzola", "jogador", 1966): ("Sandro Mazzola", None, "Alias Mazzola na Itália de 1966."),
}

# Identidades globais para a mesma pessoa em selecoes diferentes/sucessoras.
# Mantem a estatistica por selecao em `pessoa`, mas permite agregacao global.
IDENTIDADES_GLOBAIS_PESSOA = [
    {
        "chave": "dejan-stankovic",
        "nome": "Dejan Stanković",
        "wikidata": None,
        "observacao": "Mesmo jogador em Sérvia e Montenegro e Sérvia.",
        "pessoas": [
            ("Sérvia e Montenegro", "Dejan Stanković"),
            ("Sérvia", "Dejan Stanković"),
        ],
    },
    {
        "chave": "nikola-zigic",
        "nome": "Nikola Žigić",
        "wikidata": None,
        "observacao": "Mesmo jogador em Sérvia e Montenegro e Sérvia.",
        "pessoas": [
            ("Sérvia e Montenegro", "Nikola Žigić"),
            ("Sérvia", "Nikola Žigić"),
        ],
    },
    {
        "chave": "robert-prosinecki",
        "nome": "Robert Prosinečki",
        "wikidata": None,
        "observacao": "Mesmo jogador em Iugoslávia e Croácia.",
        "pessoas": [
            ("Iugoslávia", "Prosinečki"),
            ("Croácia", "Prosinečki"),
        ],
    },
]

# Eventos pontuais confirmados no proprio gerador do dashboard a partir de
# cruzamento Wikipedia/RSSSF/FIFA, mas ausentes ou malformados no texto bruto.
SUPLEMENTOS_GOL_PARTIDA = {
    (1970, "México", "El Salvador"): {
        "México": ["Valdivia 46'"],
    },
}

GOLS_CONTRA_CURADOS_BRUTO = getattr(copa, "RECLASSIFY_OWNGOALS", [])

MES_PT = {
    "janeiro": "01", "fevereiro": "02", "março": "03", "marco": "03",
    "abril": "04", "maio": "05", "junho": "06", "julho": "07",
    "agosto": "08", "setembro": "09", "outubro": "10",
    "novembro": "11", "dezembro": "12",
}


def normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto or "")
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", texto.lower())


GOLS_CONTRA_CURADOS = {
    (int(ano), copa.clean_team(selecao), normalizar(autor))
    for ano, selecao, autor in GOLS_CONTRA_CURADOS_BRUTO
}


def inteiro(valor) -> int | None:
    if valor is None or valor == "":
        return None
    try:
        return int(str(valor).replace(".", "").replace(" ", ""))
    except ValueError:
        return None


def gols_placar(placar: str) -> tuple[int | None, int | None]:
    gols = copa.score_goals(placar)
    if not gols:
        return None, None
    return int(gols[0]), int(gols[1])


def minuto_evento(texto: str) -> tuple[int | None, int | None, str]:
    texto = re.sub(r"(\d{1,3})['’]\s*(\+\d{1,2}['’])", r"\1\2", texto or "")
    m = re.search(r"(\d{1,3})(?:\+(\d{1,2}))?['’]", texto or "")
    if not m:
        return None, None, ""
    return int(m.group(1)), int(m.group(2) or 0) or None, m.group(0).replace("’", "'")


def tipo_gol(texto: str) -> str:
    t = texto or ""
    if re.search(r"contra|\bg\.?\s*c\.?\b|own goal|autogol|auto-gol", t, re.I):
        return "gol_contra"
    if re.search(r"pen|pên|penalti|pênalti", t, re.I):
        return "penalti"
    return "normal"


def limpar_nome_gol(texto: str) -> str:
    nome = re.sub(r"\d{1,3}(?:\+\d{1,2})?['’].*$", "", texto or "")
    nome = re.sub(r"\([^)]*\)", "", nome)
    nome = re.sub(r"\b(gol|gols|ol[ií]mpico|pen|pênalti|penalti)\b", "", nome, flags=re.I)
    return re.sub(r"\s+", " ", nome).strip(" ,;:-")


def dividir_eventos_gol(texto: str) -> list[str]:
    texto = (texto or "").strip()
    if not texto or texto == "-":
        return []
    texto = re.sub(r"(\d{1,3})['’]\s*(\+\d{1,2}['’])", r"\1\2", texto)
    texto = re.sub(r"\s*\|\s*", "; ", texto)
    texto = re.sub(r"\s*;\s*", "; ", texto)
    if ";" in texto:
        out = []
        for parte in texto.split(";"):
            out.extend(dividir_eventos_gol(parte))
        return out
    invertido = re.match(
        r"^((?:\d{1,3}(?:\+\d{1,2})?['’]\s*,?\s*)+)\s+([^,;|]+?)\s*(?:\([^)]*\))?$",
        texto,
    )
    if invertido:
        minutos = re.findall(r"\d{1,3}(?:\+\d{1,2})?['’]", invertido.group(1))
        nome = invertido.group(2).strip()
        if not re.search(r"\d{1,3}(?:\+\d{1,2})?['’]", nome):
            sufixo = ""
            m_sufixo = re.search(r"(\([^)]*\))\s*$", texto)
            if m_sufixo:
                sufixo = f" {m_sufixo.group(1)}"
            return [f"{nome} {minuto}{sufixo}" for minuto in minutos]
        hibrido = re.match(r"^(.+?)\s+(\d{1,3}(?:\+\d{1,2})?['’])\s+([^,;|]+)$", nome)
        if hibrido:
            nome_primeiro = hibrido.group(1).strip()
            minuto_final = hibrido.group(2)
            nome_final = hibrido.group(3).strip()
            return [f"{nome_primeiro} {minuto}" for minuto in minutos] + [f"{nome_final} {minuto_final}"]
    eventos = [m.group(1).strip().lstrip(", ") for m in re.finditer(r"([^,;]*?\d{1,3}(?:\+\d{1,2})?['’](?:\s*\([^)]*\))?)", texto)]
    if len(eventos) <= 1:
        return [texto] if re.search(r"\d{1,3}(?:\+\d{1,2})?['’]", texto) else []
    ultimo_nome = ""
    saida = []
    for item in eventos:
        item = re.sub(r"\s+(\+\d{1,2}['’])", r" 90\1", item)
        if re.match(r"^[\d\s+']", item) and ultimo_nome:
            item = f"{ultimo_nome} {item}".strip()
        nome = limpar_nome_gol(item)
        if nome:
            ultimo_nome = nome
        saida.append(item)
    return saida


def contar_eventos(texto: str) -> int:
    return len(dividir_eventos_gol(texto))


def separar_marcadores(marcadores: str, time1: str, time2: str, placar: str | None = None) -> dict[str, list[str]]:
    texto = (marcadores or "").strip()
    if not texto or texto == "-":
        return {time1: [], time2: []}
    out = {time1: [], time2: []}
    partes = [p.strip() for p in texto.split("|") if p.strip()]
    gols1, gols2 = gols_placar(placar or "")
    sem_prefixo = []
    for i, parte in enumerate(partes):
        destino = None
        resto = parte
        if ":" in parte:
            prefixo, resto = parte.split(":", 1)
            np = normalizar(prefixo)
            if np == normalizar(time1) or np in normalizar(time1) or normalizar(time1) in np:
                destino = time1
            elif np == normalizar(time2) or np in normalizar(time2) or normalizar(time2) in np:
                destino = time2
        if destino is None:
            sem_prefixo.append((i, resto))
            continue
        out.setdefault(destino, []).extend(dividir_eventos_gol(resto))
    if sem_prefixo:
        if len(sem_prefixo) == 1 and gols1 is not None and gols2 is not None:
            _, resto = sem_prefixo[0]
            qtd = contar_eventos(resto)
            if gols1 == 0 and qtd == gols2:
                out.setdefault(time2, []).extend(dividir_eventos_gol(resto))
            elif gols2 == 0 and qtd == gols1:
                out.setdefault(time1, []).extend(dividir_eventos_gol(resto))
            else:
                out.setdefault(time1, []).extend(dividir_eventos_gol(resto))
        elif len(sem_prefixo) == 2 and gols1 is not None and gols2 is not None:
            primeiro = contar_eventos(sem_prefixo[0][1])
            segundo = contar_eventos(sem_prefixo[1][1])
            if primeiro == gols1 and segundo == gols2:
                destinos = [time1, time2]
            elif primeiro == gols2 and segundo == gols1:
                destinos = [time2, time1]
            else:
                destinos = [time1, time2]
            for (_, resto), destino in zip(sem_prefixo, destinos):
                out.setdefault(destino, []).extend(dividir_eventos_gol(resto))
        else:
            for i, resto in sem_prefixo:
                out.setdefault(time1 if i == 0 else time2, []).extend(dividir_eventos_gol(resto))
    return out


def fonte_id(cur: sqlite3.Cursor, nome: str) -> int:
    return cur.execute("SELECT fonte_id FROM fonte WHERE nome=?", (nome,)).fetchone()[0]


def inserir_fonte(cur: sqlite3.Cursor, nome: str, url: str, tipo: str, observacao: str) -> int:
    cur.execute(
        "INSERT OR IGNORE INTO fonte (nome, url, tipo, observacao) VALUES (?, ?, ?, ?)",
        (nome, url, tipo, observacao),
    )
    return fonte_id(cur, nome)


def obter_selecao(cur: sqlite3.Cursor, nome: str, fonte: int | None = None) -> int | None:
    nome = copa.clean_team(nome or "").strip()
    if not nome or nome == "-":
        return None
    nn = normalizar(nome)
    row = cur.execute("SELECT selecao_id FROM selecao WHERE nome_normalizado=?", (nn,)).fetchone()
    if row:
        return row[0]
    cur.execute("INSERT INTO selecao (nome, nome_normalizado) VALUES (?, ?)", (nome, nn))
    sid = cur.lastrowid
    cur.execute(
        "INSERT OR IGNORE INTO alias_selecao (alias, alias_normalizado, selecao_id, fonte_id) VALUES (?, ?, ?, ?)",
        (nome, nn, sid, fonte),
    )
    return sid


def nome_canonico_pessoa(nome: str, selecao: str | None, papel: str, ano: int | None = None) -> tuple[str, str | None, str | None]:
    chave_ano = (copa.clean_team(selecao or ""), nome.strip(), papel, ano)
    if chave_ano in ALIASES_PESSOA_ANO:
        return ALIASES_PESSOA_ANO[chave_ano]
    chave = (copa.clean_team(selecao or ""), nome.strip(), papel)
    if chave in ALIASES_PESSOA:
        return ALIASES_PESSOA[chave]
    return nome.strip(), None, None


def obter_pessoa(
    cur: sqlite3.Cursor,
    nome: str,
    selecao_contexto_id: int | None,
    selecao_contexto_nome: str | None,
    papel: str,
    fonte: int | None,
    ano: int | None = None,
) -> int | None:
    nome = re.sub(r"\s+", " ", (nome or "").strip())
    if not nome or nome in {"-", "—"}:
        return None
    canonico, wikidata, obs = nome_canonico_pessoa(nome, selecao_contexto_nome, papel, ano)
    nn = normalizar(canonico)
    row = cur.execute(
        "SELECT pessoa_id FROM pessoa WHERE nome_normalizado=? AND COALESCE(selecao_principal_id, -1)=COALESCE(?, -1)",
        (nn, selecao_contexto_id),
    ).fetchone()
    if row:
        pid = row[0]
    else:
        cur.execute(
            "INSERT INTO pessoa (nome, nome_normalizado, selecao_principal_id, wikidata_id, observacao) VALUES (?, ?, ?, ?, ?)",
            (canonico, nn, selecao_contexto_id, wikidata, obs),
        )
        pid = cur.lastrowid
    cur.execute(
        """
        INSERT OR IGNORE INTO alias_pessoa
            (alias, alias_normalizado, pessoa_id, selecao_contexto_id, papel, fonte_id, confianca, observacao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            nome,
            normalizar(nome),
            pid,
            selecao_contexto_id,
            papel,
            fonte,
            "alta" if obs else "media",
            obs,
        ),
    )
    return pid


def obter_identidade_pessoa(
    cur: sqlite3.Cursor,
    chave: str,
    nome: str,
    wikidata: str | None = None,
    observacao: str | None = None,
) -> int:
    row = cur.execute(
        "SELECT identidade_pessoa_id FROM identidade_pessoa WHERE chave_identidade=?",
        (chave,),
    ).fetchone()
    if row:
        return row[0]
    cur.execute(
        """
        INSERT INTO identidade_pessoa
            (chave_identidade, nome_canonico, nome_normalizado, wikidata_id, observacao)
        VALUES (?, ?, ?, ?, ?)
        """,
        (chave, nome, normalizar(nome), wikidata, observacao),
    )
    return cur.lastrowid


def atribuir_identidades_pessoa(cur: sqlite3.Cursor) -> None:
    rows = cur.execute(
        """
        SELECT p.pessoa_id, p.nome, p.nome_normalizado, p.wikidata_id, p.observacao,
               COALESCE(s.nome, 'sem_selecao') AS selecao
        FROM pessoa p
        LEFT JOIN selecao s ON s.selecao_id = p.selecao_principal_id
        WHERE p.identidade_pessoa_id IS NULL
        """
    ).fetchall()
    for pessoa_id, nome, nome_norm, wikidata, observacao, selecao in rows:
        chave = f"contextual:{normalizar(selecao)}:{nome_norm}:{pessoa_id}"
        identidade_id = obter_identidade_pessoa(cur, chave, nome, wikidata, observacao)
        cur.execute(
            "UPDATE pessoa SET identidade_pessoa_id=? WHERE pessoa_id=?",
            (identidade_id, pessoa_id),
        )

    for grupo in IDENTIDADES_GLOBAIS_PESSOA:
        identidade_id = obter_identidade_pessoa(
            cur,
            f"global:{grupo['chave']}",
            grupo["nome"],
            grupo.get("wikidata"),
            grupo.get("observacao"),
        )
        for selecao, nome in grupo["pessoas"]:
            sid = obter_selecao(cur, selecao)
            cur.execute(
                """
                UPDATE pessoa
                SET identidade_pessoa_id=?
                WHERE selecao_principal_id=? AND nome_normalizado=?
                """,
                (identidade_id, sid, normalizar(nome)),
            )


def obter_estadio(cur: sqlite3.Cursor, texto: str | None) -> int | None:
    texto = re.sub(r"\s+", " ", (texto or "").strip())
    if not texto or texto == "-":
        return None
    partes = [p.strip() for p in texto.split(",") if p.strip()]
    nome = partes[0]
    cidade = ", ".join(partes[1:]) if len(partes) > 1 else None
    nn = normalizar(nome)
    row = cur.execute(
        "SELECT estadio_id FROM estadio WHERE nome_normalizado=? AND COALESCE(cidade, '')=COALESCE(?, '')",
        (nn, cidade),
    ).fetchone()
    if row:
        return row[0]
    cur.execute(
        "INSERT INTO estadio (nome, cidade, nome_normalizado) VALUES (?, ?, ?)",
        (nome, cidade, nn),
    )
    return cur.lastrowid


def obter_fase(cur: sqlite3.Cursor, edicao_id: int, nome: str | None) -> int | None:
    nome = (nome or "").strip() or "Sem fase"
    row = cur.execute("SELECT fase_id FROM fase WHERE edicao_id=? AND nome=?", (edicao_id, nome)).fetchone()
    if row:
        return row[0]
    n = normalizar(nome)
    tipo = "grupos" if "grupo" in n else ("mata_mata" if "final" in n or "lugar" in n else "outro")
    ordem = 10 if tipo == "grupos" else 50
    cur.execute(
        "INSERT INTO fase (edicao_id, nome, ordem, tipo) VALUES (?, ?, ?, ?)",
        (edicao_id, nome, ordem, tipo),
    )
    return cur.lastrowid


def obter_grupo(cur: sqlite3.Cursor, edicao_id: int, fase_id: int | None, nome: str | None) -> int | None:
    nome = (nome or "").strip()
    if not nome:
        return None
    row = cur.execute("SELECT grupo_id FROM grupo WHERE edicao_id=? AND nome=?", (edicao_id, nome)).fetchone()
    if row:
        return row[0]
    cur.execute("INSERT INTO grupo (edicao_id, fase_id, nome) VALUES (?, ?, ?)", (edicao_id, fase_id, nome))
    return cur.lastrowid


def carregar_banco(reset: bool = True) -> None:
    DB.parent.mkdir(exist_ok=True)
    if reset and DB.exists():
        DB.unlink()
    con = sqlite3.connect(DB)
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()
    cur.executescript(SCHEMA.read_text(encoding="utf-8"))

    fontes = {nome: inserir_fonte(cur, nome, *dados) for nome, dados in FONTES.items()}
    fonte_wiki = fontes["Wikipedia PT"]
    fonte_wikidata = fontes["Wikidata"]
    cur.execute(
        "INSERT INTO competicao (nome, organizacao, tipo, observacao) VALUES (?, ?, ?, ?)",
        ("Copa do Mundo FIFA", "FIFA", "seleções", "Banco relacional gerado a partir do dashboard das Copas."),
    )
    competicao_id = cur.lastrowid

    payload = copa.build_payload()
    for cup in payload["copas"]:
        ano = int(cup["ano"])
        info = cup.get("info") or {}
        ed = next((e for e in payload["geral"]["editions"] if int(e["ano"]) == ano), {})
        campeao_id = obter_selecao(cur, ed.get("campeao") or info.get("campeao"), fonte_wiki)
        vice_id = obter_selecao(cur, ed.get("vice"), fonte_wiki)
        terceiro_id = obter_selecao(cur, ed.get("terceiro"), fonte_wiki)
        quarto_id = obter_selecao(cur, ed.get("quarto"), fonte_wiki)
        cur.execute(
            """
            INSERT INTO edicao
                (competicao_id, ano, sede, campeao_id, vice_id, terceiro_id, quarto_id,
                 jogos, gols, publico_total, status, fonte_id, url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                competicao_id,
                ano,
                ed.get("sede") or info.get("sede"),
                campeao_id,
                vice_id,
                terceiro_id,
                quarto_id,
                inteiro(info.get("jogos")) or len(cup.get("partidas") or []),
                inteiro(info.get("gols")),
                None,
                "em_andamento" if ano == 2026 else "realizada",
                fonte_wiki,
                cup.get("url") or ed.get("url"),
            ),
        )
        edicao_id = cur.lastrowid

        for r in cup.get("classificacao_final") or []:
            sid = obter_selecao(cur, r.get("selecao"), fonte_wiki)
            if sid is None:
                continue
            cur.execute(
                """
                INSERT OR IGNORE INTO participacao_edicao
                    (edicao_id, selecao_id, posicao_final, grupo, pontos, jogos, vitorias,
                     empates, derrotas, gols_pro, gols_contra, saldo_gols)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    edicao_id, sid, inteiro(r.get("pos")), r.get("grupo"), inteiro(r.get("pts")),
                    inteiro(r.get("j")), inteiro(r.get("v")), inteiro(r.get("e")), inteiro(r.get("d")),
                    inteiro(r.get("gp")), inteiro(r.get("gc")), inteiro(str(r.get("sg", "")).replace("+", "")),
                ),
            )
        for r in cup.get("grupos") or []:
            sid = obter_selecao(cur, r.get("selecao"), fonte_wiki)
            if sid is None:
                continue
            fase_id = obter_fase(cur, edicao_id, "Fase de grupos")
            obter_grupo(cur, edicao_id, fase_id, r.get("grupo"))
            cur.execute(
                """
                INSERT OR IGNORE INTO participacao_edicao
                    (edicao_id, selecao_id, grupo, pontos, jogos, vitorias, empates,
                     derrotas, gols_pro, gols_contra, saldo_gols, classificado)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    edicao_id, sid, r.get("grupo"), inteiro(r.get("pts")), inteiro(r.get("j")),
                    inteiro(r.get("v")), inteiro(r.get("e")), inteiro(r.get("d")), inteiro(r.get("gp")),
                    inteiro(r.get("gc")), inteiro(str(r.get("sg", "")).replace("+", "")), r.get("classificado"),
                ),
            )

        for p in cup.get("partidas") or []:
            fase_id = obter_fase(cur, edicao_id, p.get("fase"))
            grupo_id = obter_grupo(cur, edicao_id, fase_id, p.get("grupo"))
            s1 = obter_selecao(cur, p.get("time1"), fonte_wiki)
            s2 = obter_selecao(cur, p.get("time2"), fonte_wiki)
            gols1, gols2 = gols_placar(p.get("placar"))
            vencedor_id = obter_selecao(cur, p.get("vencedor"), fonte_wiki) if p.get("vencedor") else None
            ficha = p.get("ficha") or {}
            estadio_id = obter_estadio(cur, ficha.get("estadio") or p.get("estadio"))
            arbitro_id = obter_pessoa(cur, ficha.get("arbitro"), None, None, "arbitro", fonte_wiki, ano) if ficha.get("arbitro") else None
            cur.execute(
                """
                INSERT INTO partida
                    (edicao_id, fase_id, grupo_id, data_texto, horario_texto, estadio_id,
                     selecao_1_id, selecao_2_id, gols_selecao_1, gols_selecao_2, placar_texto,
                     teve_prorrogacao, teve_penaltis, vencedor_id, publico, arbitro_id, fonte_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    edicao_id, fase_id, grupo_id, p.get("data"), ficha.get("hora"), estadio_id,
                    s1, s2, gols1, gols2, p.get("placar"),
                    1 if "pro" in str(p.get("placar", "")).lower() else 0,
                    1 if "pen" in str(p.get("placar", "")).lower() else 0,
                    vencedor_id, inteiro(ficha.get("publico")), arbitro_id, fonte_wiki,
                ),
            )
            partida_id = cur.lastrowid

            marcadores = p.get("marcadores") or ""
            eventos_por_time = separar_marcadores(marcadores, p.get("time1"), p.get("time2"), p.get("placar"))
            suplemento = SUPLEMENTOS_GOL_PARTIDA.get((ano, p.get("time1"), p.get("time2"))) or {}
            for nome_time, eventos_extra in suplemento.items():
                eventos_por_time.setdefault(nome_time, []).extend(eventos_extra)
            for nome_time, eventos in eventos_por_time.items():
                sid = obter_selecao(cur, nome_time, fonte_wiki)
                nome_adversario = p.get("time2") if normalizar(nome_time) == normalizar(p.get("time1")) else p.get("time1")
                adversario_id = obter_selecao(cur, nome_adversario, fonte_wiki)
                for evento in eventos:
                    nome_jogador = limpar_nome_gol(evento)
                    tipo = tipo_gol(evento)
                    if (
                        ano == 1950
                        and copa.clean_team(nome_time) == "Brasil"
                        and p.get("time2") == "Espanha"
                        and normalizar(evento).startswith("ademirouparracontra15")
                    ):
                        nome_jogador = "Ademir"
                        tipo = "normal"
                    if (ano, copa.clean_team(nome_time), normalizar(nome_jogador)) in GOLS_CONTRA_CURADOS:
                        tipo = "gol_contra"
                    autor_sid = adversario_id if tipo == "gol_contra" else sid
                    autor_nome_time = nome_adversario if tipo == "gol_contra" else nome_time
                    pid = obter_pessoa(cur, nome_jogador, autor_sid, autor_nome_time, "jogador", fonte_wiki, ano)
                    minuto, acrescimo, minuto_txt = minuto_evento(evento)
                    cur.execute(
                        """
                        INSERT INTO gol
                            (partida_id, edicao_id, selecao_id, selecao_autor_id, pessoa_id, minuto, acrescimo,
                             minuto_texto, tipo, texto_original, fonte_id)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (partida_id, edicao_id, sid, autor_sid, pid, minuto, acrescimo, minuto_txt, tipo, evento, fonte_wiki),
                    )

            for lado, nome_time in (("t1", p.get("time1")), ("t2", p.get("time2"))):
                time = ficha.get(lado) or {}
                sid = obter_selecao(cur, nome_time, fonte_wiki)
                for situacao, lista in (("titular", time.get("xi") or []), ("entrou", time.get("res") or [])):
                    for ordem, jogador in enumerate(lista, 1):
                        numero, posicao, nome = (jogador + ["", "", ""])[:3]
                        pid = obter_pessoa(cur, nome, sid, nome_time, "jogador", fonte_wiki, ano)
                        if pid is None:
                            continue
                        cur.execute(
                            """
                            INSERT OR IGNORE INTO escalacao
                                (partida_id, edicao_id, selecao_id, pessoa_id, numero, posicao, situacao, ordem, fonte_id)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                            """,
                            (partida_id, edicao_id, sid, pid, numero, posicao, situacao, ordem, fonte_wiki),
                        )
                tecnico = time.get("tec")
                pid_tec = obter_pessoa(cur, tecnico, sid, nome_time, "tecnico", fonte_wiki, ano)
                if pid_tec:
                    cur.execute(
                        "INSERT OR IGNORE INTO comando_tecnico (partida_id, edicao_id, selecao_id, pessoa_id, fonte_id) VALUES (?, ?, ?, ?, ?)",
                        (partida_id, edicao_id, sid, pid_tec, fonte_wiki),
                    )

    # Registra aliases manuais mesmo quando ainda nao apareceram no payload.
    for (selecao, alias, papel), (canonico, wikidata, obs) in ALIASES_PESSOA.items():
        sid = obter_selecao(cur, selecao, fonte_wiki)
        pid = obter_pessoa(cur, canonico, sid, selecao, papel, fonte_wikidata)
        cur.execute(
            """
            INSERT OR IGNORE INTO alias_pessoa
                (alias, alias_normalizado, pessoa_id, selecao_contexto_id, papel, fonte_id, confianca, observacao)
            VALUES (?, ?, ?, ?, ?, ?, 'alta', ?)
            """,
            (alias, normalizar(alias), pid, sid, papel, fonte_wikidata, obs),
        )

    atribuir_identidades_pessoa(cur)
    inserir_auditorias(cur, fontes)
    con.commit()
    con.close()


def inserir_auditorias(cur: sqlite3.Cursor, fontes: dict[str, int]) -> None:
    rows = cur.execute(
        """
        SELECT alias_normalizado, COUNT(DISTINCT pessoa_id) AS pessoas,
               GROUP_CONCAT(DISTINCT alias) AS aliases
        FROM alias_pessoa
        GROUP BY alias_normalizado
        HAVING pessoas > 1
        """
    ).fetchall()
    for alias_norm, pessoas, aliases in rows:
        cur.execute(
            """
            INSERT INTO auditoria_identidade
                (tipo_entidade, chave, descricao, severidade, status, fonte_primaria_id, fonte_cruzamento_id, observacao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "pessoa",
                alias_norm,
                f"Mesmo alias normalizado aponta para {pessoas} pessoas: {aliases}",
                "media",
                "revisar",
                fontes["Wikipedia PT"],
                fontes["Wikidata"],
                "Pode ser correto quando seleções/contextos diferentes usam o mesmo apelido, ex.: Ronaldo Brasil x Cristiano Ronaldo Portugal.",
            ),
        )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--reset", action="store_true", default=True)
    args = ap.parse_args()
    print(f"💾 Criando banco em {DB}")
    carregar_banco(reset=args.reset)
    con = sqlite3.connect(DB)
    cur = con.cursor()
    print("✅ Banco criado")
    for tabela in ("edicao", "selecao", "pessoa", "partida", "gol", "escalacao", "auditoria_identidade"):
        n = cur.execute(f"SELECT COUNT(*) FROM {tabela}").fetchone()[0]
        print(f"   {tabela}: {n}")
    con.close()


if __name__ == "__main__":
    main()
