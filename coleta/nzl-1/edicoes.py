"""Edições da 1ª divisão neozelandesa (nzl-1): uma por título, como na lista de campeões nacionais da RSSSF (nzchamp.html),
de 1970 a 2025. Escopo aprovado pelo Guilherme em 23/11/2026:
- começa em 1970, com a primeira liga nacional (os campeonatos das províncias, 1892-1969, ficam de fora);
- campeão = o da lista oficial: 1970-1992 o 1º da liga; desde 1993 o vencedor da final (Grand Final), com o 1º da fase de
  liga na observação; 2019/20 parou pela covid e o Auckland City foi declarado campeão sem final;
- 2004 (finais canceladas, só ligas regionais) e 2021 (só a "South Central Series", sem título) ficam de fora;
- as ligas regionais que classificam para a fase nacional (1993-1995, 1999 e 2022-2025) entram como 1ª fase da edição,
  um grupo por região;
- o time reserva do Wellington Phoenix (e o do Auckland FC, 2025) leva "Reserves" no nome.

Eras (o que a RSSSF traz):
- 1970-1992 National Soccer League: tabela final e matriz de resultados (sem data nem autor); 1987 também as rodadas 1-14;
- 1993-1995 Superclub: ligas regionais (tabela e matriz), fase nacional (rodadas; 1994 só a tabela) e mata-mata;
- 1996, 1996/97, 1997/98 Summer Soccer League: rodadas e mata-mata (placar com o do intervalo entre parênteses; empate decidido
  nos pênaltis valendo ponto extra em 1996 e 1996/97);
- 1999: North Island e South Island Soccer League e a final entre os campeões;
- 2000-2003 National Club Championship / National League: rodadas (com data e autores) e mata-mata dos 4 primeiros;
- 2004/05-2020/21 NZFC / Premiership: rodadas e mata-mata (2010/11 e 2011/12: a RSSSF só tem as tabelas e o mata-mata;
  os jogos da fase de liga vêm do ogol);
- 2022-2025 National League: ligas regionais (só as tabelas na RSSSF), fase nacional (rodadas) e final.

Cada trecho é (página da RSSSF, linha inicial, linha final, fase, grupo), em linhas do texto puro (rsssf_oce.texto). O trecho
termina antes da Chatham Cup (copa) e dos playoffs de acesso.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "nzl-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

LIGA = "Fase de liga"
UNICA = "Fase única"
REGIONAL = "Fase regional"
NACIONAL = "Fase nacional"
SEMI = "Semifinal"
PRELIM = "Final preliminar"
ELIM = "Rodada eliminatória"
FINAL = "Final"


@dataclass
class Edicao:
    temporada: str
    ano_inicio: int
    ano_fim: int
    nome_oficial: str
    trechos: list[tuple[str, int, int, str, str]]
    pontos_vitoria: int
    ogol: bool = False            # jogos da fase de liga vêm do ogol (a RSSSF só tem as tabelas)
    obs: str = ""
    incompleta: str = ""          # o que falta nos jogos (entra no formato e na observação)


def _p(ano: int) -> str:
    return f"nz{ano % 100:02d}" if ano < 2010 else f"nz{ano}"


# fim da liga em cada página de 1970-1992 (início da Chatham Cup)
_FIM_NSL = {1970: 46, 1971: 62, 1972: 55, 1973: 63, 1974: 63, 1975: 63, 1976: 44, 1977: 47, 1978: 44, 1979: 47, 1980: 45,
            1981: 43, 1982: 44, 1983: 44, 1984: 43, 1985: 50, 1986: 48, 1987: 181, 1988: 59, 1989: 53, 1990: 52, 1991: 54,
            1992: 53}

EDICOES: list[Edicao] = []
for _a in range(1970, 1993):
    EDICOES.append(Edicao(str(_a), _a, _a, f"National Soccer League {_a}", [(_p(_a), 0, _FIM_NSL[_a], UNICA, "")],
                          3 if _a >= 1983 else 2))

_SUPERCLUB = "Superclub Competition {a} (National Championship)"
EDICOES += [
    Edicao("1993", 1993, 1993, _SUPERCLUB.format(a=1993), [
        ("nz93", 16, 42, REGIONAL, "Norte"), ("nz93", 42, 68, REGIONAL, "Centro"), ("nz93", 68, 95, REGIONAL, "Sul"),
        ("nz93", 95, 208, NACIONAL, ""), ("nz93", 208, 219, SEMI, ""), ("nz93", 219, 222, PRELIM, ""), ("nz93", 222, 230, FINAL, "")], 3),
    Edicao("1994", 1994, 1994, _SUPERCLUB.format(a=1994), [
        ("nz94", 18, 45, REGIONAL, "Norte"), ("nz94", 45, 72, REGIONAL, "Centro"), ("nz94", 72, 100, REGIONAL, "Sul"),
        ("nz94", 100, 116, NACIONAL, ""), ("nz94", 116, 120, SEMI, ""), ("nz94", 120, 122, PRELIM, ""), ("nz94", 122, 127, FINAL, "")], 3,
        incompleta="a fase nacional só tem a tabela final na RSSSF (os 28 jogos ficam de fora)"),
    Edicao("1995", 1995, 1995, _SUPERCLUB.format(a=1995), [
        ("nz95", 16, 44, REGIONAL, "Norte"), ("nz95", 44, 74, REGIONAL, "Centro"), ("nz95", 74, 107, REGIONAL, "Sul"),
        ("nz95", 107, 189, NACIONAL, ""), ("nz95", 189, 198, SEMI, ""), ("nz95", 198, 204, PRELIM, ""), ("nz95", 204, 211, FINAL, "")], 3),
    Edicao("1996", 1996, 1996, "Summer Soccer League 1996", [
        ("nz96", 80, 223, LIGA, ""), ("nz96", 240, 258, SEMI, ""), ("nz96", 258, 270, PRELIM, ""), ("nz96", 270, 281, FINAL, "")], 4,
        obs="temporada de transição (janeiro a maio); 4 pontos por vitória e, no empate, 1 ponto para cada um e disputa de "
            "pênaltis valendo 1 ponto extra"),
    Edicao("1996/97", 1996, 1997, "National Summer Soccer League 1996/97", [
        ("nz97", 13, 383, LIGA, ""), ("nz97", 383, 397, SEMI, ""), ("nz97", 397, 404, PRELIM, ""), ("nz97", 404, 414, FINAL, "")], 4,
        obs="4 pontos por vitória e, no empate, 1 ponto para cada um e disputa de pênaltis valendo 1 ponto extra"),
    Edicao("1997/98", 1997, 1998, "National Summer Soccer League 1997/98", [
        ("nz98", 12, 224, LIGA, ""), ("nz98", 224, 229, SEMI, ""), ("nz98", 229, 236, FINAL, "")], 3),
    Edicao("1999", 1999, 1999, "National Club Championship 1999", [
        ("nz99", 25, 280, REGIONAL, "Ilha Norte"), ("nz99", 280, 425, REGIONAL, "Ilha Sul"), ("nz99", 425, 437, FINAL, "")], 3,
        obs="North Island Soccer League e South Island Soccer League; o título se decide na final entre os dois campeões"),
    Edicao("2000", 2000, 2000, "Ansett National Club Championship 2000", [
        ("nz00", 12, 312, LIGA, ""), ("nz00", 312, 325, SEMI, ""), ("nz00", 325, 340, FINAL, "")], 3,
        obs="ponto extra por 4 ou mais gols num jogo"),
    Edicao("2001", 2001, 2001, "National League 2001", [
        ("nz01", 12, 300, LIGA, ""), ("nz01", 300, 315, SEMI, ""), ("nz01", 315, 322, PRELIM, ""), ("nz01", 322, 338, FINAL, "")], 3),
    Edicao("2002", 2002, 2002, "National League 2002", [
        ("nz02", 12, 306, LIGA, ""), ("nz02", 306, 321, SEMI, ""), ("nz02", 321, 327, PRELIM, ""), ("nz02", 327, 346, FINAL, "")], 3),
    Edicao("2003", 2003, 2003, "National League 2003", [
        ("nz03", 12, 329, LIGA, ""), ("nz03", 329, 341, SEMI, ""), ("nz03", 341, 346, PRELIM, ""), ("nz03", 346, 362, FINAL, "")], 3),
]

# NZFC / Premiership: (página, início da liga, início do mata-mata, início da final, fim)
_NZFC = {
    2004: ("nz05", 15, 323, 329, 337), 2005: ("nz06", 12, 294, 315, 340), 2006: ("nz07", 12, 313, 318, 326),
    2007: ("nz08", 12, 226, 229, 235), 2008: ("nz09", 12, 151, 165, 171), 2009: ("nz2010", 20, 152, 166, 172),
    2010: ("nz2011", 20, 36, 50, 56), 2011: ("nz2012", 20, 36, 48, 53), 2012: ("nz2013", 20, 147, 161, 166),
    2013: ("nz2014", 20, 155, 172, 178), 2014: ("nz2015", 20, 220, 232, 239), 2015: ("nz2016", 20, 170, 176, 182),
    2016: ("nz2017", 20, 218, 226, 232), 2017: ("nz2018", 21, 215, 223, 229), 2018: ("nz2019", 20, 209, 217, 224),
    2019: ("nz2020", 19, 220, 220, 220), 2020: ("nz2021", 19, 181, 189, 200),
}
for _a, (_pg, _ini, _semi, _fin, _fim) in _NZFC.items():
    _t = f"{_a}/{(_a + 1) % 100:02d}"
    _nome = ("Premiership " if _a >= 2016 else "New Zealand Football Championship ") + _t
    _tr = [(_pg, _ini, _semi, LIGA, "")]
    if _a == 2005:   # 2005/06: seis clubes no mata-mata, em três rodadas (eliminatória, semifinal e final preliminar)
        _tr += [(_pg, 294, 302, ELIM, ""), (_pg, 302, 310, SEMI, ""), (_pg, 310, 315, PRELIM, ""), (_pg, 315, 340, FINAL, "")]
    elif _fin > _semi:
        _tr += [(_pg, _semi, _fin, SEMI, ""), (_pg, _fin, _fim, FINAL, "")]
    EDICOES.append(Edicao(_t, _a, _a + 1, _nome, _tr, 3, ogol=_a in (2010, 2011),
                          obs="temporada interrompida em 18 de março de 2020 pela covid-19; sem mata-mata, o Auckland City "
                              "(1º da tabela) foi declarado campeão" if _a == 2019 else ""))

# National League: (página, Norte, Centro, Sul, fase nacional, final, fim)
_NL = {2022: ("nz2022", 26, 45, 68, 87, 203, 208), 2023: ("nz2023", 29, 48, 68, 88, 202, 210),
       2024: ("nz2024", 29, 59, 78, 98, 214, 222), 2025: ("nz2025", 29, 50, 69, 86, 230, 238)}
for _a, (_pg, _n, _c, _s, _nac, _fin, _fim) in _NL.items():
    _fim_n = 49 if _a == 2024 else _c   # 2024: o playoff de acesso/rebaixamento da Northern League fica de fora
    EDICOES.append(Edicao(str(_a), _a, _a, f"National League {_a}", [
        (_pg, _n, _fim_n, REGIONAL, "Norte"), (_pg, _c, _s, REGIONAL, "Centro"), (_pg, _s, _nac, REGIONAL, "Sul"),
        (_pg, _nac, _fin, NACIONAL, ""), (_pg, _fin, _fim, FINAL, "")], 3,
        incompleta="Central League e Southern League pelo ogol: falta 1 jogo da Central (Petone x Wellington Phoenix Reserves) "
                   "e, na Southern, Coastal Spirit e Dunedin City Royals têm um jogo a mais e Nelson Suburbs e Wanaka um a menos "
                   "do que na tabela da RSSSF" if _a == 2025 else ""))
