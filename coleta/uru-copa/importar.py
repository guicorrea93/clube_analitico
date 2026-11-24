"""Copa AUF Uruguay (uru-copa): copa nacional aberta da AUF desde 2022, com os clubes profissionais, os amadores da AUF e os
do interior (OFI). Decisão do Guilherme (24/11/2026): as sete copas da América do Sul, contagem da Wikipédia, das menores
às maiores; esta é a primeira (coleta/comum-sulamerica/copas-nacionais.md).

Fonte: RSSSF, seção "Copa AUF Uruguay" das páginas do ano (uru2022 ... uru2025, já baixadas pelo uru-1); campeão conferido
com a Wikipédia em espanhol ("Copa AUF Uruguay", guardada em data/coleta/uru-copa/wikipedia/es_copa_auf.txt). O importador é
o comum das copas (coleta/comum-sulamerica/copa_rsssf.py); aqui ficam as edições, as fases e os clubes (clubes_copa.py).

Formatos: 2022 com quatro fases regionais (Norte, Centro-Litoral, Este, Sur-Metropolitano: preliminar, rodadas, semifinal e
final regional) e o "Final Four" (semifinais em ida e volta e final); 2023 com preliminar da Divisional D, rodadas 1 a 3
(OFI x AUF), oitavas, quartas, semifinais e final (maio de 2024); 2024 e 2025 com rodadas 1 e 2, quartas, semifinais e
final. A 2026 ainda está em andamento.

Uso: python coleta/uru-copa/importar.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
sys.path.insert(1, str(AQUI.parent / "uru-1"))
import autores  # noqa: E402  (o do uru-1)
from clubes_copa import CLUBES, clube  # noqa: E402
from copa_rsssf import Copa, EdicaoCopa, importar  # noqa: E402
from ler_rsssf import linhas  # noqa: E402  (o do uru-1: páginas em data/coleta/uru-1/rsssf)

SLUG = "uru-copa"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

# fases na ordem de importância (a última é a final); "Final" sozinho é a final nacional
FASES = [
    (r"^Preliminary Round", "Fase preliminar"),
    (r"^Round 1\b", "Primeira fase"),
    (r"^Round 2\b", "Segunda fase"),
    (r"^Round 3\b", "Terceira fase"),
    (r"^Regional Semifinals", "Semifinal regional"),
    (r"^Regional Final", "Final regional"),
    (r"^1/8 Finals", "Oitavas de final"),
    (r"^Quarterfinals", "Quartas de final"),
    (r"^Semifinals", "Semifinal"),
    (r"^Final\b", "Final"),
]
REGIOES = [(r"^Regional Norte$", "Norte"), (r"^Regional Centro-Litoral$", "Centro-Litoral"), (r"^Regional Este$", "Este"),
           (r"^Regional Sur-Metropolitano$", "Sur-Metropolitano")]


def _inicio(pagina: str) -> int:
    """Linha do título da seção (a última "Copa AUF Uruguay" da página: a primeira é o índice)."""
    return [i for i, l in enumerate(linhas(pagina)) if re.match(r"^Copa AUF Uruguay", l.strip())][-1]


EDICOES = [
    EdicaoCopa("2022", 2022, 2022, "Copa AUF Uruguay 2022", [("uru2022", _inicio("uru2022"), None)], regioes=REGIOES,
               fim_regiao=r"^Final Four$",
               obs="76 clubes em quatro regiões (Norte, Centro-Litoral, Este, Sur-Metropolitano); os quatro campeões "
                   "regionais jogam o Final Four (semifinais em ida e volta, final em jogo único)"),
    EdicaoCopa("2023", 2023, 2024, "Copa AUF Uruguay 2023", [("uru2023", _inicio("uru2023"), None)],
               obs="a RSSSF a chama de 2023/24: a final foi em 22 de maio de 2024"),
    EdicaoCopa("2024", 2024, 2024, "Copa AUF Uruguay 2024", [("uru2024", _inicio("uru2024"), None)],
               obs="32 clubes: 16 profissionais, 6 amadores da AUF e 10 do interior (OFI); sem prorrogação"),
    EdicaoCopa("2025", 2025, 2025, "Copa AUF Uruguay 2025", [("uru2025", _inicio("uru2025"), None)],
               obs="32 clubes: 16 profissionais, 6 amadores da AUF e 10 do interior (OFI); sem prorrogação"),
]

COMPETICAO = {
    "slug": SLUG, "nome": "Copa AUF Uruguay", "nome_curto": "Copa AUF", "tipo": "copa", "nivel": None, "pais": "URU",
    "pais_nome": "Uruguai", "regiao": None, "confederacao": "CONMEBOL", "rotulo_painel": "Copa AUF Uruguay",
    "menu_painel": "Uruguai · Copa AUF", "do_painel": "da Copa AUF Uruguay", "o_painel": "a Copa AUF Uruguay",
    "observacao": "Copa nacional aberta da AUF desde 2022: clubes profissionais, amadores da AUF e do interior (OFI). Antes "
                  "dela não houve copa nacional regular (o Torneo de Copa de 1969 e a Copa de Uruguay de 1996 não contam)."}

# Wikipédia em espanhol, "Copa AUF Uruguay" (Finales): campeão de cada edição
CAMPEOES_WIKI = {"2022": "Defensor Sporting", "2023": "Defensor Sporting", "2024": "Defensor Sporting", "2025": "Peñarol"}

COPA = Copa(slug=SLUG, competicao=COMPETICAO, edicoes=EDICOES, fases=FASES, linhas=linhas, clube=clube, clubes=CLUBES,
            autores=autores, campeoes_wiki=CAMPEOES_WIKI, fonte_pagina="https://www.rsssf.org/tablesu/{pagina}.html",
            ignorar=[r"\[enter in round"])

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    importar(COPA, RELATORIO)
