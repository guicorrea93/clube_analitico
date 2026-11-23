"""Correções e explicações da coleta da 1ª divisão colombiana, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {}
_FINAL_AP = "final do Apertura (julho), não decide o título do ano: nível 0 (CO-014)"
CORRIGE: dict[tuple[str, str], dict] = {
    ("1974", "wiki:es_1974:935"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1974", "wiki:es_1974:941"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1976", "wiki:es_1976:409"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1976", "wiki:es_1976:415"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1979", "wiki:es_1979:1375"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1979", "wiki:es_1979:1381"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1980", "wiki:es_1980:400"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1980", "wiki:es_1980:406"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1982", "wiki:es_1982:1375"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1982", "wiki:es_1982:1381"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1999", "col99:675"): {"fase": "Final do Finalización", "motivo": "final do Clausura (Medellín x Nacional), não a do ano (CO-014)"},
    ("1999", "col99:678"): {"fase": "Final do Finalización", "motivo": "final do Clausura (Medellín x Nacional), não a do ano (CO-014)"},
    ("2008 Apertura", "col08:328"): {"descartar": True, "motivo": "jogo suspenso e completado depois: fica a linha do jogo completo (CO-021)"},
    ("2013 Finalización", "col2013:795"): {"descartar": True, "motivo": "jogo suspenso pela chuva e completado depois (CO-021)"},
}
TABELAS_FORA: dict[tuple[str, str], str] = {}
EXPLICACOES: dict[str, list[str]] = {}
