"""Edições do Campeonato Saudita: as 69 temporadas da lista oficial (relatório da federação de 2025, como a Wikipédia em
inglês o reproduz: campeoes_wiki.py), de 1957/58 a 2025/26. Decisão do Guilherme (24/11/2026): desde 1957.

Eras:
- 1957/58 a 1973/74, "His Majesty's League": torneio mata-mata (os campeões são os da antiga Copa do Rei). Entra o
  campeão e o vice; o jogo da final quando a lista da Copa do Rei da RSSSF (saucuphist.html) tem o mesmo par de clubes.
  1966/67 não concluída, 1967/68 não disputada, 1969/70 cancelada: edições sem campeão.
- 1974/75, Liga de Classificação: dois grupos de 8 e final entre os primeiros.
- 1975/76: liga abandonada no meio (cancelada; edição sem campeão, com os jogos que a RSSSF tem).
- 1976/77 em diante, Premier League / Pro League: pontos corridos. 1981/82: dois grupos de 10 e playoff (semifinais,
  3º lugar e final). 1985/86: dois grupos de 6 e grupos finais (título, classificação, rebaixamento). 1990/91 a 2006/07
  ("Golden Box"): liga e playoff dos 4 primeiros; até 2000/01 semifinais (ida e volta até 1999/00) e final; de 2001/02 em
  diante escadinha (3º x 4º, o vencedor x o 2º, o vencedor x o 1º na final).

Fontes dos jogos: RSSSF (sauNN.html; jogos da liga em 1974/75, 1976/77, 1980/81, 1982/83, 1983/84, 1986/87 e
1997/98-2006/07, com autores até 2005/06; playoffs de todos os anos que têm), ogol (fase de liga de 1999/00 em diante:
a fonte dos jogos de 2006/07 em diante e das temporadas que a RSSSF não tem completas), ESPN (2022/23 em diante: autores,
cartões, estádio, público e hora).
"""
from __future__ import annotations

import re

GRUPOS = {1975: 2, 1982: 2, 1986: 2}


def nome_oficial(fim: int) -> str:
    t = f"{fim - 1}/{fim % 100:02d}"
    if fim <= 1974:
        return f"His Majesty's League {t}"
    if fim == 1975:
        return f"Saudi Categorization League {t}"
    if fim <= 2007:
        return f"Saudi Premier League {t}"
    return f"Saudi Pro League {t}"


def fase_playoff(secao: str) -> str | None:
    """Nome da fase de um jogo de playoff pela seção da página da RSSSF; None = não é do playoff do título."""
    s = secao.lower()
    if "relegation" in s or "promotion" in s:
        return None
    if "fourth place" in s:
        return "Primeira fase"
    if "against third" in s:
        return "Segunda fase"
    if "third place" in s:
        return "Disputa do 3º lugar"
    if re.search(r"semi|first leg|second leg|championship playoff", s):
        return "Semifinal"
    if "final" in s:
        return "Final"
    return None
