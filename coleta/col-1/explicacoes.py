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
    # CO-013 (1957, Wikipédia em espanhol): octogonal cancelado, hexagonais com grupo, desempate do grupo A e final dos hexagonais
    **{("1957", f"wiki-es_1957:{n}"): {"esp": "anulado", "fase": "Octogonal (cancelado)",
                                        "motivo": "octogonal cancelado depois de 3 rodadas (\"Octogonal (Cancelado)\") (CO-013)"}
       for n in (1090, 1094, 1114, 1118, 1122, 1126, 1140, 1144)},
    **{("1957", f"wiki-es_1957:{n}"): {"grupo": g, "motivo": f"hexagonal do grupo {g} (CO-013)"}
       for g, ns in (("A", (1312, 1316, 1320, 1332, 1336, 1340, 1354, 1358, 1362, 1374, 1378, 1382, 1396, 1400, 1404, 1416, 1420, 1424, 1438, 1442, 1446, 1458, 1462, 1466, 1480, 1484, 1488, 1500, 1504, 1508)),
                     ("B", (1713, 1717, 1721, 1733, 1737, 1741, 1755, 1759, 1763, 1775, 1779, 1783, 1797, 1801, 1805, 1817, 1821, 1825, 1839, 1843, 1847, 1859, 1863, 1867, 1881, 1885, 1889, 1901, 1905, 1909))) for n in ns},
    **{("1957", f"wiki-es_1957:{n}"): {"fase": "Desempate do grupo", "grupo": "A",
                                        "motivo": "desempate do grupo A (Medellín, Pereira e Tolima), não do título (CO-013)"}
       for n in (1650, 1655, 1660)},
    **{("1957", f"wiki-es_1957:{n}"): {"fase": "Final dos hexagonais", "grupo": "",
                                        "motivo": "final entre os vencedores dos hexagonais (Cúcuta x Tolima) (CO-013)"}
       for n in (1992, 1998, 2004)},
    ("1974", "wiki-es_1974:935"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1974", "wiki-es_1974:941"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1976", "wiki-es_1976:409"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1976", "wiki-es_1976:415"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1979", "wiki-es_1979:1375"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1979", "wiki-es_1979:1381"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1980", "wiki-es_1980:400"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1980", "wiki-es_1980:406"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1982", "wiki-es_1982:1375"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1982", "wiki-es_1982:1381"): {"fase": "Final do Apertura", "motivo": _FINAL_AP},
    ("1999", "col99:675"): {"fase": "Final do Finalización", "motivo": "final do Clausura (Medellín x Nacional), não a do ano (CO-014)"},
    ("1999", "col99:678"): {"fase": "Final do Finalización", "motivo": "final do Clausura (Medellín x Nacional), não a do ano (CO-014)"},
    ("2008 Apertura", "col08:328"): {"descartar": True, "motivo": "jogo suspenso e completado depois: fica a linha do jogo completo (CO-021)"},
    ("2013 Finalización", "col2013:795"): {"descartar": True, "motivo": "jogo suspenso pela chuva e completado depois (CO-021)"},
}
TABELAS_FORA: dict[tuple[str, str], str] = {}
_SEM_FONTE = ("{o_que}: nem a RSSSF nem a Wikipédia em espanhol (baixada de novo em 24/11/2026, igual) trazem os jogos que "
              "faltam, e a pesquisa por uma 3ª fonte não achou outra ({id})")
EXPLICACOES: dict[str, list[str]] = {
    "1966": [_SEM_FONTE.format(o_que="350 dos 364 jogos", id="CO-004")],
    "1986": [_SEM_FONTE.format(o_que="só 21 jogos do octogonal e 8 dos 14 clubes na classificação", id="CO-006")],
    "1988": [_SEM_FONTE.format(o_que="Finalización com 12 jogos por clube (de 28)", id="CO-006")],
    "2001": ["América de Cali 2-2 Once Caldas (1ª rodada dos quadrangulares, 18/11): a Wikipédia em espanhol dá 0-0; fica o "
             "2-2 da RSSSF, confirmado por uma 3ª fonte (arquivo da FutbolRed: 2-2 no Pascual Guerrero, gols de David Ferreira "
             "e Julián Vásquez) (CO-015)"],
}
