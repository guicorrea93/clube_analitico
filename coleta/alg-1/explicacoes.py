"""Correções e explicações da coleta da 1ª divisão argelina, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha" ou "ogol:<id>").
- ANULA_CLUBE: clube que desistiu no meio do campeonato (jogos anulados).
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("alg99", 65): ("Teams 7-11", "Teams 7 to 11", "nota sobre a temporada seguinte; \"7-11\" era lido como placar"),
    ("alg99", 909): ("Teams 7-11", "Teams 7 to 11", "nota sobre a temporada seguinte; \"7-11\" era lido como placar"),
    ("alg03", 345): ("temporarily awarded 0-3", "temporarily given to RC Kouba", "o 0-3 foi revogado depois (\"later "
                     "revoked\"): vale o 1-0 de campo, como a tabela conta"),
}


def _copia(pagina: str, linhas: range, motivo: str) -> dict[tuple[str, str], dict]:
    return {f"{pagina}:{n}": {"descartar": True, "motivo": motivo} for n in linhas}


_C1973 = "a página repete os oito jogos da rodada 10 logo abaixo (cópia): fica a primeira lista"
_C1975 = ("a rodada 4 da página é cópia da rodada 3 (mesmos jogos e placares): os jogos verdadeiros da rodada 4 não são "
          "conhecidos")
_C1976 = ("a rodada 18 da página é cópia da rodada 17 (mesmos jogos e placares): os jogos verdadeiros da rodada 18 não são "
          "conhecidos")
CORRIGE: dict[tuple[str, str], dict] = {
    **{("1972/73", k): v for k, v in _copia("alg73", range(151, 159), _C1973).items()},
    **{("1974/75", k): v for k, v in _copia("alg75", range(79, 87), _C1975).items()},
    **{("1975/76", k): v for k, v in _copia("alg76", range(220, 228), _C1976).items()},
    ("1969/70", "alg70:123"): {"descartar": True, "motivo": "USM Bel-Abbès 0-0 NA Hussein Dey aparece duas vezes na rodada 10"},
    ("1988/89", "alg89:204"): {"descartar": True, "motivo": "MC Alger 2-1 MO Constantine aparece duas vezes na rodada 16"},
    # 2025/26: o ogol, a tabela da RSSSF e a da Wikipédia concordam; a lista de jogos da RSSSF erra o placar
    ("2025/26", "alg2026:93"): {"gm": 0, "gv": 1, "motivo": "Olympique Akbou 0-1 MC Alger (ogol; as tabelas da RSSSF e da "
                                                             "Wikipédia só fecham assim); a lista da RSSSF dá 1-0"},
    ("2025/26", "alg2026:310"): {"gm": 2, "gv": 0, "motivo": "CS Constantine 2-0 ES Sétif (ogol; as tabelas da RSSSF e da "
                                                              "Wikipédia só fecham assim); a lista da RSSSF dá 1-0"},
}
ANULA_CLUBE: dict[str, tuple[str, str]] = {}
TABELAS_FORA: dict[tuple[str, str], str] = {}
_LISTA = ("a lista de jogos da página não fecha com a tabela final da mesma página em alguns clubes (placar ou resultado "
          "trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a tabela da Wikipédia "
          "quase sempre confirma a da RSSSF: nenhum placar foi mudado, a classificação é a tabela publicada e o relatório "
          "aponta o jogo provável")
EXPLICACOES: dict[str, list[str]] = {
    **{f"{a}/{(a + 1) % 100:02d}": [_LISTA] for a in range(1964, 1999)},
    "1962/63": ["a 1ª fase das ligas regionais não está na página; a ordem dos quatro primeiros é a da fase final"],
    "1963/64": ["ligas regionais só com os resultados conhecidos (\"Known Results\") e o grupo Leste da Liga de Constantine "
                "sem números; os jogos de acesso à 1ª divisão do ano seguinte ficam de fora; dois jogos com siglas que não "
                "deu para identificar (\"R.S.O\" e \"C.S.S\", da Liga de Orã) ficam de fora"],
    "1972/73": [_LISTA, "a rodada 10 aparece duas vezes na página: a cópia foi descartada"],
    "1974/75": [_LISTA, "a rodada 4 da página é cópia da rodada 3: os oito jogos verdadeiros da rodada 4 faltam"],
    "1975/76": [_LISTA, "a rodada 18 da página é cópia da rodada 17: os oito jogos verdadeiros da rodada 18 faltam"],
    "1996/97": [_LISTA, "\"US Constantine\" (rodadas 15 e 22) é o US Chaouia (erro de digitação da página)"],
    "1997/98": [_LISTA, "ninguém caiu: os desempates de rebaixamento não valeram, porque a 1ª divisão de 1998/99 passou a "
                "dois grupos de 14"],
    "2000/01": ["USM Blida x CS Constantine: a página corrigiu o placar para 1-0 (\"correction from 2-0\"), mas a tabela "
                "ainda conta o 2-0; fica o 1-0 corrigido"],
    "2001/02": ["a tabela da RSSSF (e a da Wikipédia) não fecha com os jogos em quatro clubes; nenhum placar foi mudado"],
    "2009/10": ["CA Bordj Bou Arréridj x MC Alger (14/08/2009): abandonado aos 72' com 1-0 e \"awarded loss to both\" "
                "(derrota dada aos dois); a tabela da RSSSF conta derrota para os dois, a da Wikipédia a vitória do CA "
                "Bordj Bou Arréridj; o jogo fica sem placar e a classificação é a tabela publicada"],
    "2020/21": ["a tabela da RSSSF, a da Wikipédia e os jogos não fecham entre si em três clubes; nenhum placar foi mudado"],
    "2025/26": ["dois placares da lista da RSSSF corrigidos pelo ogol (as tabelas da RSSSF e da Wikipédia só fecham com "
                "eles)"],
}
