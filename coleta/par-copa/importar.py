"""Copa Paraguay (par-copa): copa nacional da APF desde 2018 (sem 2020), com a Primera, a Intermedia, as Primeras B e C e
clubes do interior (UFI). Segunda das sete copas da América do Sul (decisões do Guilherme de 24/11/2026 em
coleta/comum-sulamerica/copas-nacionais.md).

Fonte: RSSSF, seção "Copa Paraguay" das páginas do ano (para2018 ... para2025, já baixadas pelo par-1); campeão conferido com
a Wikipédia em espanhol ("Copa Paraguay", guardada em data/coleta/par-copa/wikipedia/es_copa_paraguay.txt). Importador comum
das copas: coleta/comum-sulamerica/copa_rsssf.py; aqui ficam as edições, as fases e os clubes (clubes_copa.py).

Formatos: 2018, 2019 e 2021 com rodadas 1 a 3, quartas, semifinais e final; 2022 com uma 1ª fase de zonas (só as tabelas)
e uma 2ª fase de mata-mata antes das oitavas; 2023 desde a 1/16, com disputa de 3º lugar; 2024 e 2025: a RSSSF só traz das
oitavas em diante (as fases anteriores, com os clubes das divisões de acesso, faltam). Em 2018 e 2019, a página segue com
outra competição depois da final ("Final Table"): o trecho acaba ali.

Uso: python coleta/par-copa/importar.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
sys.path.insert(1, str(AQUI.parent / "par-1"))
import autores  # noqa: E402  (o do par-1)
from clubes_copa import CLUBES, clube  # noqa: E402
from copa_rsssf import Copa, EdicaoCopa, importar  # noqa: E402
from ler_rsssf import linhas  # noqa: E402  (o do par-1: páginas em data/coleta/par-1/rsssf)

SLUG = "par-copa"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

FASES = [
    (r"^(Round 1|First Stage)\b", "Primeira fase"),
    (r"^(Round 2|Second Stage)\b", "Segunda fase"),
    (r"^(Round 3|Third Stage)\b", "Terceira fase"),
    (r"^1/16 Finals", "Dezesseis-avos de final"),
    (r"^1/8 Finals", "Oitavas de final"),
    (r"^Quarterfinals", "Quartas de final"),
    (r"^Semifinals", "Semifinal"),
    (r"^Third Place Playoff", "Disputa do 3º lugar"),
    (r"^Final\b(?! Table)", "Final"),
]


def _trecho(ano: int) -> tuple[str, int, int]:
    """Da última "Copa Paraguay" da página (a primeira é o índice) até a "Final Table" de outra competição (2018, 2019) ou
    a lista de links do fim ("list of champions")."""
    ls = linhas(f"para{ano}")
    ini = [i for i, l in enumerate(ls) if re.match(r"^Copa Paraguay", l.strip())][-1]
    fim = next(i for i in range(ini, len(ls)) if re.match(r"^(Final Table:|list of champions)", ls[i].strip()))
    return f"para{ano}", ini, fim


_OBS = {2018: "rodadas 1 a 3 com clubes de todas as divisões e do interior", 2019: "", 2021: "", 2022:
        "1ª fase em zonas (só as tabelas: os jogos não estão na página) e 2ª fase de mata-mata antes das oitavas",
        2023: "com disputa de 3º lugar", 2024: "a RSSSF só traz das oitavas em diante (faltam as fases anteriores)",
        2025: "a RSSSF só traz das oitavas em diante (faltam as fases anteriores)"}
EDICOES = [EdicaoCopa(str(a), a, a, f"Copa Paraguay {a}", [_trecho(a)], obs=_OBS[a]) for a in (2018, 2019, 2021, 2022, 2023, 2024, 2025)]

COMPETICAO = {
    "slug": SLUG, "nome": "Copa Paraguay", "nome_curto": "Copa Paraguay", "tipo": "copa", "nivel": None, "pais": "PAR",
    "pais_nome": "Paraguai", "regiao": None, "confederacao": "CONMEBOL", "rotulo_painel": "Copa Paraguay",
    "menu_painel": "Paraguai · Copa Paraguay", "do_painel": "da Copa Paraguay", "o_painel": "a Copa Paraguay",
    "observacao": "Copa nacional da APF desde 2018 (não houve em 2020), com clubes de todas as divisões e do interior (UFI). "
                  "Em 2024 e 2025 a fonte só traz das oitavas de final em diante."}

# Wikipédia em espanhol, "Copa Paraguay" (Palmarés e ficha): campeão de cada edição
CAMPEOES_WIKI = {"2018": "Guaraní", "2019": "Libertad", "2021": "Olimpia", "2022": "Sportivo Ameliano", "2023": "Libertad",
                 "2024": "Libertad", "2025": "General Caballero JLM"}

COPA = Copa(slug=SLUG, competicao=COMPETICAO, edicoes=EDICOES, fases=FASES, linhas=linhas, clube=clube, clubes=CLUBES,
            autores=autores, campeoes_wiki=CAMPEOES_WIKI, fonte_pagina="https://www.rsssf.org/tablesp/{pagina}.html")

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    importar(COPA, RELATORIO)
