"""Correções e explicações da coleta da 1ª divisão camaronesa, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha" ou "ogol:<id>").
- ANULA_CLUBE: clube que desistiu ou foi excluído no meio do campeonato (jogos anulados).
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

import json
from pathlib import Path

EXTRAS: dict[str, list[dict]] = {}
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("kam95", 16): ("30 12 12  4", "30 12 12  6", "Unisport Bafang: 12+12+4 não dá 30 jogos; 48 pontos = 12 vitórias e 12 "
                    "empates, logo 6 derrotas"),
}

_R21 = ("a página repete a rodada 22 como rodada 21 (os mesmos 8 confrontos, com o mesmo mandante, 4 com o mesmo placar); "
        "fica a rodada 22, que tem data. A rodada 21 verdadeira não está na página")
_UNION = ("o ogol põe o Union e o Caïman Douala com o mesmo nome e o mesmo id (2482): não dá para saber de qual dos dois é "
          "o jogo")


def _union_2010_11() -> list[str]:
    p = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "cmr-1" / "ogol" / "75522.json"
    if not p.exists():
        return []
    return [g["id"] for g in json.loads(p.read_text(encoding="utf-8")) if "Union Douala" in (g["mandante"], g["visitante"])]


def _tribunal(venc: str, campo: str, esp: str = "wo_v") -> dict:
    """\"awarded 0-0 win\": vitória dada fora de campo, sem gols (a tabela conta a vitória e nenhum gol)."""
    return {"esp": esp, "gm": None, "gv": None, "motivo": f"vitória dada ao {venc} sem gols (\"awarded 0-0 win\"); a "
            f"tabela conta a vitória e nenhum gol", "nota": f"vitória dada ao {venc} sem gols; em campo, {campo}"}


_DADO = "\"n/p\" com \"awarded {}\" (o Bamboutos, excluído, não foi a campo): W.O. que a tabela conta"


CORRIGE: dict[tuple[str, str], dict] = {
    **{("2000", f"kam00:{n}"): {"descartar": True, "motivo": _R21} for n in range(238, 246)},
    ("2005", "kam05:320"): {"gm": 1, "gv": 2, "esp": "", "nota": "o 3-0 dado ao Les Astres foi revogado depois",
                            "motivo": "\"temporarily awarded 3-0, later revoked\": vale o 1-2 de campo (a tabela confirma)"},
    ("2006", "kam06:305"): {"oficial": (3, 0), "nota": "1-0 em campo, abandonado aos 75' pelo Impôts",
                            "motivo": "\"awarded 3-0; 1-0 abd by Impôts at 75'\": não é abandono sem valer; a tabela "
                            "conta o 3-0"},
    ("2007", "kam07:235"): {"esp": "wo_v", "gm": 1, "gv": 0, "motivo": "\"match finished 1-0 but Canon used suspended "
                            "coach; win awarded to University\": a tabela conta a vitória da University e o 1-0 de campo"},
    ("2007", "kam07:496"): {"oficial": (3, 0), "motivo": _DADO.format("3-0")},
    ("2007", "kam07:510"): {"oficial": (0, 3), "motivo": _DADO.format("0-3")},
    ("2007", "kam07:514"): {"oficial": (3, 0), "motivo": _DADO.format("3-0")},
    ("2007/08", "kam08:249"): {"esp": "wo_v", "gm": 0, "gv": 0, "motivo": "\"original score (0-0) stood but points awarded "
                               "to Unisport\" (o Caïman escalou jogador suspenso): a tabela conta a vitória do Unisport e o "
                               "0-0"},
    ("2009/10", "kam2010:246"): _tribunal("Les Astres", "1-0 para o Coton Sport (ogol)"),
    ("2009/10", "kam2010:250"): _tribunal("Union Douala", "2-0 para o Sable Batié (ogol)"),
    ("2009/10", "kam2010:269"): _tribunal("Renaissance Ngoumou", "2-1 para o Fovu Baham (ogol)"),
    **{("2010/11", f"ogol:{i}"): {"descartar": True, "motivo": _UNION} for i in _union_2010_11()},
    ("2023/24", "kam2024:364"): _tribunal("Victoria United", "1-0 para o UMS de Loum"),
    ("2023/24", "kam2024:372"): _tribunal("APEJES Academy", "0-0", "wo_m"),
    ("2023/24", "kam2024:376"): _tribunal("Victoria United", "1-1", "wo_m"),
    ("2024/25", "kam2025:333"): {"esp": "", "nota": "", "motivo": "jogo válido: a nota \"award of 3-0 annulled, match "
                                 "refixtured\" continua a do Dynamo Douala x Aigle Royal, da linha de cima"},
}
ANULA_CLUBE: dict[str, tuple[str, str]] = {}
TABELAS_FORA: dict[tuple[str, str], str] = {}
EXPLICACOES: dict[str, list[str]] = {
    "1999": ["Jogos incompletos: a página traz muitos jogos sem placar (\"-\"). A classificação é a tabela da RSSSF, que "
             "a Wikipédia confirma."],
    "2000": ["A página avisa que a tabela não foi conferida com os placares (\"Table (not checked with scores)\"); a "
             "Wikipédia confirma a tabela, que é a classificação. Os placares ficam como a página traz.",
             "Jogos incompletos: " + _R21 + "."],
    "2001": ["A página traz duas tabelas: uma montada pelos resultados conhecidos e a oficial da FECAFOOT. A classificação "
             "é a oficial (pontos e ordem da federação); a dos resultados conhecidos fica como conferência."],
    "2007": ["O Bamboutos foi excluído no fim do campeonato (a tabela o põe à parte, sem posição); os jogos que não fez "
             "contam como W.O. para os adversários."],
    "2014": ["Douala AC x Coton Sport: os dois clubes se recusaram a jogar; a federação deu derrota por 0-0 aos dois e "
             "tirou 3 pontos de cada (\"both clubs refused to play, both had 3 points deducted and the match awarded a "
             "0-0 loss against them\"). O jogo fica sem placar; a tabela conta uma derrota para cada um."],
    "2020/21": ["A liga da LFPC (\"Ligue 2020/21\") parou na 1ª rodada, em 4/11/2020, quando a FECAFOOT proibiu a LFPC de "
                "organizá-la (só Panthère 0-2 Coton Sport foi jogado). A edição é a \"Ligue 2021\", da FECAFOOT."],
    "2010/11": ["A RSSSF só traz a tabela final (a classificação); os jogos vêm do ogol, menos os do Union e do Caïman "
                "Douala (" + _UNION + "). Jogos incompletos."],
}
