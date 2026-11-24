"""Correções e decisões da coleta do Campeonato Japonês (jpn-1), sempre com o motivo.

- CONSERTA_JSL: erros de digitação das páginas da RSSSF da JSL, corrigidos antes da leitura:
  {ano da página: {(número da linha, texto errado): (texto certo, motivo)}}.
- AWD: jogos com o resultado decidido fora de campo (id do jogo na J.League -> motivo): entram como "awd", com o placar
  oficial; o de campo e os autores dos gols ficam na observação e em gols_texto (os gols não entram em gols.csv, porque
  não fecham com o placar oficial).
- ARTILHEIRO_GOLS: gols do artilheiro corrigidos na lista da Wikipédia: {temporada: (gols, motivo)}.
- EXPLICACOES: divergências e casos especiais de cada edição, já explicados (vão para a observação da edição e para o
  relatório): {temporada: texto}.
"""
from __future__ import annotations

CONSERTA_JSL: dict[int, dict[tuple[int, str], tuple[str, str]]] = {}

EXPLICACOES: dict[str, str] = {
    "1966": "a tabela de confrontos da RSSSF dá 4 gols a menos ao Yawata (Nippon Steel Yawata) contra o Hitachi (Kashiwa "
            "Reysol) do que a tabela final (33-16 e 24-28, iguais na Wikipédia em japonês, que cita o livro oficial da JSL): "
            "um dos dois jogos entre eles (Yawata 2-1 Hitachi ou Hitachi 1-2 Yawata) deveria ter 4 gols a mais do Yawata, sem "
            "mudar o vencedor. Nenhuma fonte pública tem o placar; os jogos ficam como a RSSSF escreve e a classificação é a "
            "tabela final",
    "1971": "a tabela de confrontos da RSSSF tem 2 gols a menos que a tabela final: um do Furukawa (JEF United Chiba) e um do "
            "Nippon Kokan (NKK), sofridos pelo Yanmar (Cerezo Osaka) e pelo Hitachi (Kashiwa Reysol), um cada. Há dois jeitos "
            "de encaixar (Furukawa x Yanmar e Nippon Kokan x Hitachi, ou Furukawa x Hitachi e Nippon Kokan x Yanmar), sem mudar "
            "vencedor; nenhuma fonte pública tem o placar. Os jogos ficam como a RSSSF escreve e a classificação é a tabela final",
    "1973": "a tabela de confrontos da RSSSF tem 1 gol a menos para o Yanmar (Cerezo Osaka) e 1 a menos para o Furukawa (JEF "
            "United Chiba) do que a tabela final: um dos jogos entre os dois (Furukawa 0-0 Yanmar ou Yanmar 1-2 Furukawa) deveria "
            "ter um gol a mais de cada lado, sem mudar o resultado. Nenhuma fonte pública tem o placar; os jogos ficam como a "
            "RSSSF escreve e a classificação é a tabela final",
}

AWD: dict[str, str] = {
    "25153": "placar de campo 2-3; a J.League registra 0-3 para o Shonan (a tabela oficial conta 0-3, e o ogol marca o jogo "
             "como decisão administrativa)",
}

ARTILHEIRO_GOLS: dict[str, tuple[int, str]] = {
    "2001": (24, "a lista de campeões da Wikipédia dá 20 gols ao Will (Consadole Sapporo); os jogos oficiais da J.League "
                 "somam 24, como a página da temporada na Wikipédia em inglês e a ficha dele na Wikipédia em japonês"),
}
