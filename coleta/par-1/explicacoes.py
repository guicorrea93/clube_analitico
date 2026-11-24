"""Correções e explicações da coleta da 1ª divisão paraguaia, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha").
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

EXTRAS: dict[str, list[dict]] = {}
_NOTA05 = "nota quebrada em três linhas (o fim dela ia para o jogo seguinte e o placar de campo para os autores) (PY-029)"
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("para2019", 943): ("Independiente  (Nanawa)", "Independiente Nanawa",
                        "Copa Paraguay 2019 (par-copa): os dois espaços antes do parêntese partiam o nome do mandante"),
    ("para05", 572): ("[awarded to Libertad; originally", "[awarded to Libertad; originally 2-1, Gral. Caballero used suspended player]",
                      _NOTA05),
    ("para05", 573): ("]      2-1, Gral. Caballero", "]", _NOTA05),
    ("para05", 574): ("used suspended player]", "", _NOTA05),
}
CORRIGE: dict[tuple[str, str], dict] = {
    **{("1981", f"para81:{n}"): {"fase": f, "motivo": "decisão do 1º turno (dava vaga na final do ano), não a final do "
                                                     "campeonato (PY-008)"}
       for n, f in ((118, "Semifinal do 1º turno"), (119, "Semifinal do 1º turno"), (122, "Final do 1º turno"))},
    ("2005", "para05:572"): {"esp": "wo_v", "gm": 2, "gv": 1, "motivo": "General Caballero 2-1 em campo; pontos para o Libertad "
                                                                  "(jogador suspenso); a tabela conta os gols de campo (PY-029)"},
}
TABELAS_FORA: dict[tuple[str, str], str] = {}
EXPLICACOES: dict[str, list[str]] = {
    "1935": ['artilheiro pela lista da RSSSF (paratops); '
             'Pedro Osorio (Cerro Porteño) com 18 gols; a Wikipédia em espanhol dá 17. Sem 3ª fonte: fica a RSSSF (PY-019)'],
    "1962": ['artilheiro pela lista da RSSSF (paratops); '
             'Cecilio Martínez (Nacional) com 19 gols; a página do ano na RSSSF dá 18 e a Wikipédia em espanhol, 17 pelo Libertad (ela troca clube e gols com 1963). Três números diferentes: fica a lista da RSSSF (PY-019)'],
    "1963": ['artilheiro pela lista da RSSSF (paratops); '
             'Juan Cabañas (Libertad) com 17 gols; a Wikipédia em espanhol dá 19 pelo Nacional (troca clube e gols com 1962). Fica a RSSSF (PY-019)'],
    "1967": ['artilheiro pela lista da RSSSF (paratops); '
             'Sebastián Fleitas (Libertad) com 18 gols, como a Wikipédia em espanhol; a página do ano na RSSSF dá 16 (PY-019)'],
    "1970": ['artilheiro pela lista da RSSSF (paratops); '
             'Saturnino Arrúa (Cerro Porteño) com 19 gols; a Wikipédia em espanhol dá 11. Fica a RSSSF (PY-019)'],
    "2003": ['artilheiro pela lista da RSSSF (paratops); '
             'Erwin Ávalos (Cerro Porteño) com 17 gols; a Wikipédia em espanhol dá 16. Sem 3ª fonte: fica a RSSSF (PY-019)'],
}

# PY-012: rebaixados de cada ano pelas notas das páginas da RSSSF ("Relegated: ...", "relegated on points average", tabela de
# promedios); vão para a última edição do ano (o Clausura de 2008 em diante). O importar.py só marca quem jogou o ano e não
# joga a 1ª divisão do ano seguinte (salva quem ganhou o desempate). Sem fonte: 2008 (a página não traz a tabela de promedios)
# e os anos antes de 1981.
REBAIXADOS: dict[int, tuple[list[str], str]] = {
    1981: (["Resistencia"], "para81:281"),
    1984: (["Atlético Tembetary"], "para84:75"),
    1985: (["River Plate de Asunción"], "para85:64"),
    1988: (["Nacional de Asunción"], "para88:99"),
    1990: (["Atlético Tembetary"], "para90:97"),
    1991: (["Sport Colombia"], "para91:98"),
    1994: (["River Plate de Asunción", "Sportivo Trinidense", "Guaraní de Coronel Oviedo", "Deportivo Boquerón", "12 de Octubre",
            "Cerro Porteño PF", "8 de Diciembre", "Pettirossi de Encarnación"],
           "para94:85-100 (os dois piores de Asunción e, pela reestruturação de 1995, mais seis)"),
    1995: (["Cerro Corá"], "para95:72"),
    1996: (["Deportivo Humaitá"], "para96:327"),
    1997: (["Atlético Tembetary", "Sport Colombia"], "para97:402"),
    1998: (["Nacional de Asunción", "Libertad"], "para98:432"),
    1999: (["Presidente Hayes", "Resistencia"], "para99:419"),
    2000: (["Universal de Encarnación"], "para00:754"),
    2002: (["Deportivo Recoleta"], "para02:550"),
    2003: (["Sportivo San Lorenzo"], "para03:575"),
    2004: (["Sport Colombia", "Sol de América"], "para04:626"),
    2005: (["General Caballero"], "para05:655"),
    2006: (["Fernando de la Mora"], "para06:800"),
    2007: (["Sportivo Trinidense"], "para07:745"),
    2009: (["2 de Mayo", "12 de Octubre"], "para09:930-931 (o 12 de Octubre foi ao desempate)"),
    2010: (["Sport Colombia", "Sportivo Trinidense"], "para2010:907-908"),
    2011: (["General Caballero", "3 de Febrero"], "para2011:845-846"),
    2012: (["Tacuary", "Independiente de Campo Grande"], "para2012:844-845"),
    2013: (["Cerro Porteño PF", "Sportivo Carapeguá"], "para2013:851"),
    2014: (["3 de Febrero", "12 de Octubre"], "para2014:866"),
    2015: (["Deportivo Santaní", "Sportivo San Lorenzo"], "para2015:889"),
    2016: (["River Plate de Asunción", "General Caballero"], "para2016:894"),
    2017: (["Sportivo Trinidense", "Independiente de Campo Grande", "Rubio Ñu"], "para2017:863 (Independiente e Rubio Ñu foram ao desempate)"),
    2018: (["Independiente de Campo Grande", "3 de Febrero"], "para2018:893"),
    2019: (["Deportivo Capiatá", "Deportivo Santaní"], "para2019:908"),
    2020: (["Sportivo San Lorenzo", "General Díaz"], "para2020:728"),
    2021: (["River Plate de Asunción"], "para2021:660"),
    2022: (["Sol de América", "12 de Octubre"], "para2022:881"),
    2023: (["Guaireña", "Resistencia"], "para2023:899"),
    2024: (["Sol de América", "Tacuary"], "para2024:851"),
    2025: (["General Caballero JLM", "Atlético Tembetary"], "para2025:858"),
}
