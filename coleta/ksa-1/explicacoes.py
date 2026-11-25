"""Correções e casos especiais da liga saudita, com a prova de cada um.

- OGOL_CORRIGE: jogos do calendário do ogol com erro, pelo id do jogo no ogol: o que muda e por quê. A prova é a matriz de
  resultados do artigo da temporada na Wikipédia em inglês e a tabela final da RSSSF, que fecham com a correção.
"""
from __future__ import annotations

OGOL_CORRIGE = {
    "1898735": {"mandante": "Hajer",
                "motivo": "o ogol dá Al-Hilal 1-0 Najran em 31/03/2012 (rodada 24), mas o Al-Hilal já jogou na rodada (Al-Fateh "
                          "0-5 Al-Hilal), recebe o Najran outra vez em 09/12/2011 e falta o Hajer x Najran: é Hajer 1-0 Najran "
                          "(Wikipédia, 2011–12 Saudi Professional League: HJR_NAJ 1–0); com isso a tabela da RSSSF fecha"},
    "1415575": {"gm": 0, "gv": 3,
                "motivo": "o ogol dá Najran 3-0 Al-Taawoun em 04/03/2011; a Wikipédia (2010–11 Saudi Professional League: "
                          "NAJ_TWN 0–3) e a tabela da RSSSF dão 0-3"},
}

# diferenças entre a tabela da RSSSF e os jogos que ficam (explicadas), por ano em que a temporada termina
TABELA_RSSSF = {
    2002: "A página da RSSSF não tem o jogo adiado Al-Ettifaq 2-1 Al-Shabab (05/04/2002, no ogol) e a tabela dela conta 21 "
          "jogos para os dois clubes; com o jogo, os dois fecham com 22.",
}
