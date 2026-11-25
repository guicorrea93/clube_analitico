"""Temporadas do campeonato da Tchecoslováquia (tch-1), de 1925 a 1992/93, com a liga do Protetorado da Boêmia e Morávia
(1938/39 a 1943/44).

Escopo (Guilherme, 25/11/2026):
- entra a liga desde 1925, primeiro título oficial, até 1992/93;
- entra a liga do Protetorado (Národní liga, 1938/39-1943/44), aqui e não no `cze-1`;
- entra o campeonato de outono de 1948 como edição não oficial (`oficial` = "não");
- ficam de fora: o campeonato da Boêmia Central antes de 1925 (não oficial); o campeonato amador de 1925-1933;
  1944/45 (abandonado); a liga eslovaca da guerra (vai com a Eslováquia).

Chave de cada temporada = ano inicial; nas temporadas de ano civil que dividiriam a chave com a seguinte, a chave é o
ano anterior, como na `gdr-1`: "1925" (primavera) tem a chave 1924 e "1927" (primavera) tem a chave 1926. De 1948 a 1956
a liga seguiu o ano civil (chave = o ano, rótulo "1949").
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DADOS = RAIZ / "data" / "coleta" / "tch-1"
CACHE = RAIZ / "data" / "cache"
TEMPORADAS = [1924, 1925, 1926] + list(range(1927, 1944)) + [1945, 1946, 1947] + list(range(1948, 1957)) \
    + list(range(1957, 1993))
ROTULO_ANO = {1924: "1925", 1926: "1927"}            # primavera, com a chave do ano anterior
ANO_CIVIL = set(range(1948, 1957))                   # 1948 (outono, não oficial) a 1956
PROTETORADO = set(range(1938, 1944))                 # Národní liga (Česko-moravská liga)
NAO_OFICIAL = {1948: "campeonato de outono de 1948, na passagem para o calendário de ano civil; não é título oficial "
                     "(RSSSF: \"fall championship; not official\")"}


def temporada(a: int) -> str:
    if a in ROTULO_ANO:
        return ROTULO_ANO[a]
    if a in ANO_CIVIL:
        return str(a)
    return f"{a}/{str(a + 1)[-2:]}"


def nome_oficial(a: int) -> str:
    if a <= 1933:
        return "Asociační liga"
    if a <= 1937:
        return "Státní liga"
    if a in PROTETORADO:
        return "Národní liga (Česko-moravská liga)"
    return "1. liga"


def wiki_titulo(a: int) -> str:
    if a in ROTULO_ANO or a in ANO_CIVIL:
        return f"{temporada(a)} Czechoslovak First League"
    t = f"{a}–{a + 1}" if (a + 1) % 100 == 0 else f"{a}–{str(a + 1)[-2:]}"
    if a in PROTETORADO and a > 1938:
        return f"{t} Národní liga"
    return f"{t} Czechoslovak First League"
