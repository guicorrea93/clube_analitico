"""Copa Ecuador (ecu-copa): 1970 (El Nacional; torneio de 3 clubes) e a copa nacional da FEF de 2018/19 em diante (2020 e
2021 canceladas, 2023 não disputada). Terceira das sete copas da América do Sul (decisões do Guilherme de 24/11/2026 em
coleta/comum-sulamerica/copas-nacionais.md; a contagem da Wikipédia inclui 1970).

Fonte: RSSSF, seção "Copa Ecuador" das páginas do ano (ecua70, ecua2019, ecua2022, ecua2024, ecua2025, já baixadas pelo
ecu-1); campeão conferido com a Wikipédia em espanhol ("Copa Ecuador", guardada em data/coleta/ecu-copa/wikipedia/).
Importador comum das copas: coleta/comum-sulamerica/copa_rsssf.py; aqui ficam as edições, as fases e os clubes.

Formatos: 2018/19 com duas preliminares, 1/16, oitavas, quartas, semifinais e final em ida e volta; 2022 com preliminar,
1/16, oitavas, quartas, semifinal em grupo de 4 (pontos corridos) e final; 2024 e 2025: a RSSSF só traz das oitavas em
diante (faltam as fases anteriores).

Uso: python coleta/ecu-copa/importar.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
sys.path.insert(1, str(AQUI.parent / "ecu-1"))
import autores  # noqa: E402  (o do ecu-1)
from clubes_copa import CLUBES, clube  # noqa: E402
from copa_rsssf import Copa, EdicaoCopa, importar  # noqa: E402
from ler_rsssf import linhas  # noqa: E402  (o do ecu-1: páginas em data/coleta/ecu-1/rsssf)

SLUG = "ecu-copa"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

FASES = [
    (r"^First Preliminary Round", "Primeira fase preliminar"),
    (r"^(Second Preliminary Round|Preliminary Round)", "Fase preliminar"),
    (r"^1/16 Finals", "Dezesseis-avos de final"),
    (r"^1/8 Finals", "Oitavas de final"),
    (r"^Quarterfinals", "Quartas de final"),
    (r"^Semifinal", "Semifinal"),
    (r"^Final\b(?! Phase| Table)", "Final"),
]


def _trecho(pagina: str) -> tuple[str, int, int]:
    """Da última "Copa Ecuador" da página (a primeira é o índice) até a lista de links do fim ("list of champions")."""
    ls = linhas(pagina)
    ini = [i for i, l in enumerate(ls) if re.match(r"^Copa Ecuador", l.strip())][-1]
    fim = next(i for i in range(ini, len(ls)) if ls[i].strip().startswith("list of champions"))
    return pagina, ini, fim


EDICOES = [
    EdicaoCopa("1970", 1970, 1970, "Copa Ecuador 1970", [_trecho("ecua70")],
               obs="torneio de 3 clubes em janeiro de 1970 (vaga na Recopa Sudamericana de Clubes), Barcelona x Everest não "
                   "disputado; conta como edição pela Wikipédia", fase_padrao="Fase única", pontos=True, datas=False),
    EdicaoCopa("2018/19", 2018, 2019, "Copa Ecuador 2018-19", [_trecho("ecua2019")],
               obs="duas fases preliminares com clubes da Segunda Categoría e amadores"),
    EdicaoCopa("2022", 2022, 2022, "Copa Ecuador 2022", [_trecho("ecua2022")], obs="semifinal em grupo de 4 (pontos corridos)"),
    EdicaoCopa("2024", 2024, 2024, "Copa Ecuador 2024", [_trecho("ecua2024")],
               obs="a RSSSF só traz das oitavas em diante (faltam as fases anteriores)"),
    EdicaoCopa("2025", 2025, 2025, "Copa Ecuador 2025", [_trecho("ecua2025")],
               obs="a RSSSF só traz das oitavas em diante (faltam as fases anteriores)"),
]

COMPETICAO = {
    "slug": SLUG, "nome": "Copa Ecuador", "nome_curto": "Copa Ecuador", "tipo": "copa", "nivel": None, "pais": "ECU",
    "pais_nome": "Equador", "regiao": None, "confederacao": "CONMEBOL", "rotulo_painel": "Copa Ecuador",
    "menu_painel": "Equador · Copa Ecuador", "do_painel": "da Copa Ecuador", "o_painel": "a Copa Ecuador",
    "observacao": "Copa nacional da FEF: 1970 (torneio de 3 clubes) e de 2018/19 em diante (2020 e 2021 canceladas, 2023 não "
                  "disputada). Em 2024 e 2025 a fonte só traz das oitavas de final em diante."}

# Wikipédia em espanhol, "Copa Ecuador" (Palmarés); 1970 pela pesquisa de 23/11 (copas-nacionais.md)
CAMPEOES_WIKI = {"1970": "El Nacional", "2018/19": "LDU de Quito", "2022": "Independiente del Valle", "2024": "El Nacional",
                 "2025": "Universidad Católica"}

COPA = Copa(slug=SLUG, competicao=COMPETICAO, edicoes=EDICOES, fases=FASES, linhas=linhas, clube=clube, clubes=CLUBES,
            autores=autores, campeoes_wiki=CAMPEOES_WIKI, fonte_pagina="https://www.rsssf.org/tablese/e/{pagina}.html")

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    importar(COPA, RELATORIO)
