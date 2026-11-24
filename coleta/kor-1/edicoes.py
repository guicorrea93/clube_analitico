"""Edições do Campeonato Sul-Coreano (K League, 1ª divisão), uma por título, como na lista de campeões da K League, da
RSSSF (skorchamp.html) e da Wikipédia em inglês (List of South Korean football champions): 1983 a 2025, 43 edições.
2026 fica para quando acabar.

Fases: o boletim do portal não traz rodada nem fase, mas o número do jogo (gameId) segue o calendário (conferido nas
datas), então as fases saem da ordem dos jogos: FASES[ano] = lista de (fase, quantos jogos). De 2013 em diante a fase e
a rodada vêm do site oficial (codeName e roundId da lista de jogos).
- 1984, 1986, 1995, 1996, 2004-2006: dois turnos (전기/후기 리그) e a decisão entre os campeões dos turnos (1984, 1986,
  1995, 1996: competição à parte no portal) ou playoff (2004-2006, com os melhores da tabela anual);
- 1998-2000 e 2007-2011: liga e playoff do título;
- 2012 em diante: liga e depois a divisão em grupo do título e grupo de baixo (스플릿), sem playoff (o campeão é o 1º do
  grupo do título; os pontos seguem da 1ª fase).

Pontos (conferidos na tabela de cada ano da RSSSF, skorhist.html, e nas tabelas das páginas de cada ano):
- 1983 e 1985-1992: 2 por vitória, 1 pelo empate;
- 1984: 3 por vitória, 2 pelo empate com gols e 1 pelo 0-0;
- 1993: empate decidido nos pênaltis; 4 pela vitória, 2 pela vitória nos pênaltis, 1 pela derrota nos pênaltis;
- 1994-1997 e 2001 em diante: 3, 1 e 0;
- 1998 e 1999: empate vai à prorrogação com gol de ouro e aos pênaltis; 3 pela vitória no tempo normal, 2 pela vitória na
  prorrogação, 1 pela vitória nos pênaltis;
- 2000: 3 pela vitória no tempo normal ou na prorrogação, 1 pela vitória nos pênaltis.
"""
from __future__ import annotations

ANOS = list(range(1983, 2026))

# fases antes de 2013, na ordem dos jogos: (nome, quantos jogos); None = o resto
FASES: dict[int, list[tuple[str, int | None]]] = {
    1984: [("1º turno", 56), ("2º turno", 56), ("Final", None)],
    1986: [("1º turno", 30), ("2º turno", 30), ("Final", None)],
    1995: [("1º turno", 56), ("2º turno", 56), ("Final", None)],
    1996: [("1º turno", 72), ("2º turno", 72), ("Final", None)],
    1998: [("Liga", 90), ("Playoff", None)],
    1999: [("Liga", 135), ("Playoff", None)],
    2000: [("Liga", 135), ("Playoff", None)],
    2004: [("1º turno", 78), ("2º turno", 78), ("Playoff", None)],
    2005: [("1º turno", 78), ("2º turno", 78), ("Playoff", None)],
    2006: [("1º turno", 91), ("2º turno", 91), ("Playoff", None)],
    2007: [("Liga", 182), ("Playoff", None)],
    2008: [("Liga", 182), ("Playoff", None)],
    2009: [("Liga", 210), ("Playoff", None)],
    2010: [("Liga", 210), ("Playoff", None)],
    2011: [("Liga", 240), ("Playoff", None)],
    2012: [("Liga", 240), ("Grupos finais", None)],
}

# nome oficial da liga em cada época (o patrocínio vai no nome da edição, como a K League escreve)
def nome_oficial(ano: int) -> str:
    if ano <= 1993:
        return f"Korean Super League {ano}" if ano <= 1986 else f"Korean Professional Football League {ano}"
    if ano <= 1997:
        return f"Korean League {ano}"
    if ano <= 2012:
        return f"K League {ano}"
    if ano <= 2017:
        return f"K League Classic {ano}"
    return f"K League 1 {ano}"


def pontos(ano: int, gp: int, gc: int, prorrogacao: bool = False, pp: int | None = None, pc: int | None = None) -> int:
    """Pontos de um jogo para um clube (gp/gc no fim do jogo, prorrogação incluída; pp/pc nos pênaltis)."""
    ganhou = gp > gc or (gp == gc and pp is not None and pp > pc)
    perdeu = gp < gc or (gp == gc and pp is not None and pp < pc)
    if ano == 1984:
        return 3 if ganhou else 0 if perdeu else 2 if gp > 0 else 1
    if ano <= 1992:
        return 2 if ganhou else 0 if perdeu else 1
    if ano == 1993:
        return (2 if pp is not None else 4) if ganhou else (1 if pp is not None else 0) if perdeu else 0
    if ano in (1998, 1999):
        return (1 if pp is not None else 2 if prorrogacao else 3) if ganhou else 0
    if ano == 2000:
        return (1 if pp is not None else 3) if ganhou else 0
    return 3 if ganhou else 0 if perdeu else 1
