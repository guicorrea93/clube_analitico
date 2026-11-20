"""Correções e explicações da coleta da 1ª divisão argentina, edição a edição (entram no relatório).

- EXTRAS: jogos que a página da RSSSF traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {
    "1936 Copa de Oro": [
        {"mandante": "River Plate", "visitante": "San Lorenzo", "gm": 4, "gv": 2, "data": "1936-12-20", "fase": "Final",
         "estadio": "Estádio do Independiente", "cidade": "Avellaneda", "fonte_id": "rsssf:arg-oro36:9",
         "gols": [("River Plate", "Renato Cesarini", 39, "normal"), ("San Lorenzo", "Miguel Pantó", 55, "normal"),
                  ("River Plate", "Bernabé Ferreyra", 73, "normal"), ("River Plate", "Adolfo Pedernera", 76, "normal"),
                  ("San Lorenzo", "Rubén Cavadini", 81, "normal"), ("River Plate", "Renato Cesarini", 86, "normal")],
         "obs": "jogo único; o 2-1 de Bernabé Ferreyra desviou em Chividini; o 3-2 é de Cavadini (outras fontes: Canteli)"},
    ],
}

# erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo)
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("arg66", 396): ("0 6 Racing", "0:6 Racing", "placar sem os dois-pontos ('0 6'); 0-6 fecha com a tabela publicada"),
}

# (temporada, "página:linha") -> {campo: valor, "motivo": texto}
CORRIGE: dict[tuple[str, str], dict] = {
    ("1936 Copa de Oro", "arg-oro36:17"): {"descartar": True, "motivo": "a linha do texto corrido vira o jogo escrito à mão "
                                                                       "(EXTRAS), com data, local e autores dos gols"},
    ("1965", "arg65:198"): {"esp": "abd", "motivo": "Independiente 2-2 Racing Club suspenso aos 68' e não continuado; a tabela "
                                                    "publicada não conta o jogo (33 jogos para os dois)"},
}

EXPLICACOES: dict[str, list[str]] = {
    "1891": ["a liga da época deu o título dividido entre Saint Andrew's e Caledonians (empatados); Saint Andrew's venceu o "
             "desempate pelas medalhas. A AFA cita só o Saint Andrew's, que fica como campeão no pacote"],
    "1936 Copa de Oro": ["jogo único entre os campeões da Copa de Honor (San Lorenzo) e da Copa Campeonato (River Plate), "
                         "lido à mão da página arg-oro36 da RSSSF (texto corrido)"],
}
