"""Edições do Campeonato Japonês (1ª divisão), uma por título, como na lista de campeões da RSSSF (japchamp.html) e da
Wikipédia em inglês (List of Japanese football champions): 60 edições.

- 1965 a 1984: Japan Soccer League (JSL; a partir de 1972, JSL Division 1), amadora, em ano fechado.
- 1985/86 a 1991/92: JSL Division 1 no calendário europeu (outono a primavera).
- 1992: sem liga. A JSL acabou em 1991/92; a J.League começou em 1993 (em 1992 só houve a Copa da J.League).
- 1993 a 2025: J.League (J1). Nos anos de dois turnos (1993-1995, 1997-2004, 2015 e 2016) o campeão é o vencedor
  da final entre os campeões dos turnos ("Championship"); em 2002 e 2003 o mesmo clube ganhou os dois turnos e não houve
  final; em 2015 e 2016 a final teve semifinal. Os turnos entram como fases; a repescagem contra a J2 (1998, 2004-2008,
  2018, 2019, 2022) fica de fora, como no Alemão (entra com a 2ª divisão).

Pontos por vitória (a classificação vem sempre da tabela publicada):
- JSL: 2 até 1976, 4 de 1977 a 1979 (empate decidido nos pênaltis: 2 para quem ganha, 1 para quem perde), 2 de 1980 a
  1987/88 e 3 de 1988/89 a 1991/92 (conferido na tabela de cada ano);
- J1: 1993 e 1994 sem pontos (sem empate: prorrogação com morte súbita e pênaltis; a tabela ordena por vitórias);
  1995 e 1996: 3 por vitória (no tempo normal, na prorrogação ou nos pênaltis), 1 pela derrota nos pênaltis; 1997 e 1998: 3 no tempo normal, 2 na
  prorrogação, 1 nos pênaltis; 1999 a 2002: 3 no tempo normal, 2 na prorrogação, 1 o empate (sem pênaltis);
  2003 em diante: 3, 1 e 0, sem prorrogação.
"""
from __future__ import annotations

from dataclasses import dataclass

TURNOS = {1993, 1994, 1995, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2015, 2016}


@dataclass
class Edicao:
    temporada: str
    ano_inicio: int
    ano_fim: int
    era: str            # "jsl" ou "j1"
    pagina: int | None  # ano da página da RSSSF da JSL (jap<ano>.html)
    nome_oficial: str


def _jsl() -> list[Edicao]:
    eds = []
    for a in range(1965, 1985):
        nome = "Japan Soccer League" if a <= 1971 else "Japan Soccer League Division 1"
        eds.append(Edicao(str(a), a, a, "jsl", a, f"{nome} {a}"))
    for a in range(1985, 1992):
        t = f"{a}/{(a + 1) % 100:02d}"
        eds.append(Edicao(t, a, a + 1, "jsl", a + 1, f"Japan Soccer League Division 1 {t}"))
    return eds


def _j1() -> list[Edicao]:
    eds = []
    for a in range(1993, 2026):
        nome = "J.League" if a <= 1998 else "J.League Division 1" if a <= 2014 else "J1 League"
        eds.append(Edicao(str(a), a, a, "j1", None, f"{nome} {a}"))
    return eds


EDICOES: list[Edicao] = _jsl() + _j1()
