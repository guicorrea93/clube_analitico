"""Correções e explicações da coleta da 1ª divisão peruana, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations


def _ida_volta(a: str, b: str, ida: tuple[int, int], volta: tuple[int, int], fase: str, fonte: str) -> list[dict]:
    """"A - B 3-0 / 2-3": os dois placares com os gols de A primeiro; o mando da volta (B) é presumido."""
    obs = "confronto de ida e volta numa linha só (\"A - B 3-0 / 2-3\"); mando da volta presumido"
    return [{"mandante": a, "visitante": b, "gm": ida[0], "gv": ida[1], "fase": fase, "fonte_id": f"rsssf:{fonte}", "obs": obs},
            {"mandante": b, "visitante": a, "gm": volta[1], "gv": volta[0], "fase": fase, "fonte_id": f"rsssf:{fonte}", "obs": obs}]


EXTRAS: dict[str, list[dict]] = {
    "1991": [
        *_ida_volta("Unión Huayllaspanca", "Universitario", (0, 0), (0, 4), "Quartas de final do Regional", "peru91:83"),
        *_ida_volta("Melgar", "Alianza Lima", (3, 0), (2, 3), "Quartas de final do Regional", "peru91:84"),
        *_ida_volta("Alianza Atlético", "Universitario", (1, 3), (1, 4), "Quartas de final do Regional II", "peru91:194"),
        *_ida_volta("Melgar", "Sporting Cristal", (3, 1), (0, 5), "Quartas de final do Regional II", "peru91:195"),
        *_ida_volta("Sport Boys", "León de Huánuco", (1, 0), (3, 2), "Quartas de final do Regional II", "peru91:196"),
        *_ida_volta("CNI", "Defensor Lima", (1, 1), (1, 2), "Quartas de final do Regional II", "peru91:197"),
    ],
}

# "December 16   Lima     Sporting Cristal - Alianza Lima   1-0": data e cidade antes dos clubes
_DATA_CIDADE = "data e cidade antes dos clubes (\"December 16  Lima  A - B  1-0\"): a linha vira \"Dec 16  A  1-0  B\""
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("peru98", 701): ("December 16   Lima     Sporting Cristal - Alianza Lima              1-0",
                      "Dec 16  Sporting Cristal  1-0  Alianza Lima", _DATA_CIDADE),
    ("peru98", 737): ("December 20   Lima     Sporting Cristal - Universitario             2-1",
                      "Dec 20  Sporting Cristal  2-1  Universitario", _DATA_CIDADE),
    ("peru98", 739): ("December 23   Lima     Universitario - Sporting Cristal             2-1  [4-2 pen]",
                      "Dec 23  Universitario  2-1  Sporting Cristal  [4-2 pen]", _DATA_CIDADE),
    ("peru2025", 1058): ("35 -  9 - 20 - 16", "35 -  9 - 10 - 16", "Comerciantes Unidos com 20 empates na tabela acumulada "
                         "(9+20+16 não dá 35 jogos); são 10, como na soma do Apertura e do Clausura"),
    ("peru75", 406): ("Union Huaraz", "Unión Huaral", "\"Union Huaraz\" não está na tabela de 1975; é o Unión Huaral, o único "
                                                      "clube da tabela sem esse jogo contra o Juan Aurich"),
}

CORRIGE: dict[tuple[str, str], dict] = {
    ("2021", "peru2021:542"): {"esp": "", "gm": 2, "gv": 2, "motivo": "Cusco FC 2-2 Cienciano: o TAS (21/01/2022) anulou a vitória "
                                                               "dada ao Cusco (PE-007)"},
    **{("2017", f"peru2017:{n}"): {"fase": "Final do Torneo de Verano", "motivo": "final do Torneo de Verano (maio), não a do "
                                                                              "campeonato (PE-013)"} for n in (396, 400)},
    **{("2018", f"peru2018:{n}"): {"fase": "Final do Torneo de Verano", "motivo": "final do Torneo de Verano (abril), não a do "
                                                                              "campeonato (PE-013)"} for n in (393, 397)},
    **{("1991", f"peru91:{n}"): {"descartar": True, "motivo": "confronto de ida e volta numa linha só: entra como dois jogos "
                                                              "(EXTRAS)"} for n in (83, 84, 194, 195, 196, 197)},
    ("1988", "peru88:640"): {"descartar": True, "motivo": "linha da tabela de confrontos do Descentralizado \"B\" (não é jogo)"},
    ("1988", "peru88:641"): {"descartar": True, "motivo": "linha da tabela de confrontos do Descentralizado \"B\" (não é jogo)"},
    **{("1935", f"peru35:{n}"): {"esp": "n/p", "motivo": "vitória dada fora de campo que a FPF não validou: a tabela só conta "
                                                         "os jogos disputados (nota da página)"} for n in (56, 58, 65)},
    **{("1929", f"wiki-es_1929:{n}"): {"esp": "anulado", "motivo": "jogo do Alianza Lima, desclassificado depois da 7ª rodada por "
                                                                 "não ceder jogadores à seleção (Wikipédia); a tabela final não "
                                                                 "conta seus jogos"} for n in (365, 375, 388, 402, 416, 436, 449)},
    ("1997", "peru97:349"): {"descartar": True, "motivo": "nota (\"Teams 2-7 qualify for Liguilla Pre-Libertadores\"), não é jogo"},
    ("1999", "peru99:640"): {"descartar": True, "motivo": "nota sobre o jogo anterior (Cienciano 2-0 Sporting Cristal), não é jogo"},
    **{("2025", f"peru2025:{n}"): {"esp": "anulado", "motivo": "jogo do Binacional no Clausura: o clube foi desfiliado pela FPF por "
                                                               "ordem judicial e todos os seus jogos do Clausura foram anulados "
                                                               "(nota da página)"} for n in (605, 632, 666, 686, 702)},
    **{("2003", f"peru03:{n}"): {"esp": "anulado", "motivo": "rodadas 16 e 17 do Clausura, jogadas com sub-20 e amadores durante "
                                                             "a greve dos profissionais; o campeonato foi encerrado no fim de "
                                                             "novembro e as tabelas publicadas não contam esses jogos"}
       for n in (672, 674, 676, 679, 687, 689, 693, 696, 699)},
    ("2021", "peru2021:79"): {"esp": "anulado", "motivo": "jogo anulado pela FPF: o FC Carlos Stein foi rebaixado por decisão do "
                                                       "CAS (nota da página)"},
    ("2025", "peru2025:978"): {"esp": "awd", "gm_of": 0, "gv_of": 3,
                               "motivo": "Ayacucho 1-0 Comerciantes Unidos em campo; as tabelas publicadas (Clausura e acumulada) "
                                         "contam 0-3, vitória dada ao Comerciantes Unidos (a página não traz a nota)"},
}
TABELAS_FORA: dict[tuple[str, str], str] = {}
EXPLICACOES: dict[str, list[str]] = {
    "1914": ["vice Jorge Chávez N°1 pela página peru1914; a Wikipédia dá o Sport Alianza (2 fontes x 1: fica a RSSSF) (PE-026)"],
    "2022": ["ajustes de pontos da tabela publicada (Alianza Lima +2, Ayacucho +1, César Vallejo -2) sem terceira fonte que "
             "explique a origem; ficam os da tabela (PE-018)"],
    "1977": ["artilheiros pela lista da RSSSF (perutops), igual à Wikipédia em inglês; a es diverge em alguns anos (1934, 1977, "
             "1980, 1981, 1986-1988): fica a RSSSF até uma 3ª fonte (PE-016)"],
    "1929": ["a página da Wikipédia traz os jogos duas vezes (lista das rodadas 1-9 e tabela de confrontos); em três "
             "confrontos os placares das duas não batem (Universitario x Ciclista Lima, Universitario x Unión Buenos Aires, "
             "Hidroaviación x Ciclista Lima) e os dois jogos ficam; falta um jogo do Atlético Chalaco"],
    "1931": ["a tabela publicada soma pontos de bônus da liga de reservas (um quarto dos pontos dela); a conferência usa só "
             "J V E D GP GC"],
}
