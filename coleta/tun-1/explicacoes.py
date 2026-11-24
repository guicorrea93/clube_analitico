"""Correções e explicações da coleta da 1ª divisão tunisiana, edição a edição (entram no relatório).

- EXTRAS: jogos que a página traz em texto corrido (o leitor não pega) e entram à mão, com a fonte.
- CONSERTA_TEXTO: erros de digitação da página da RSSSF: (página, linha) -> (trecho, troca, motivo).
- CORRIGE: jogo lido -> correção, com o motivo. Chave: (temporada, "página:linha" ou "ogol:<id>").
- ANULA_CLUBE: clube que desistiu no meio do campeonato (jogos anulados).
- TABELAS_FORA: tabelas da página que não são da edição: (temporada, "página:linha") -> motivo.
- EXPLICACOES: o que o relatório diz de cada edição (divergências que ficam, decisões).
"""
from __future__ import annotations

def _wo(pagina: str, mandante: str, visitante: str, vencedor: str, nb: str) -> dict:
    """Célula "awd" da tabela de confrontos (o leitor da matriz pula): vitória dada, sem gols, como a tabela conta."""
    return {"mandante": mandante, "visitante": visitante, "gm": None, "gv": None,
            "esp": "wo_m" if vencedor == mandante else "wo_v",
            "fonte_id": f"{pagina}: tabela de confrontos (célula \"awd\"; \"{nb}\")",
            "obs": f"nota da página: \"{nb}\""}


EXTRAS: dict[str, list[dict]] = {
    "1968/69": [_wo("tun69", "Sfax Railways Sports", "AS Marsa", "AS Marsa", "NB: SRS-ASM was awarded a win to ASM")],
    "1970/71": [_wo("tun71", "US Monastir", "Étoile du Sahel", "US Monastir", "NB: USMo-ESS was awarded a win to USMo")],
    "1977/78": [_wo("tun78", "CO Transports", "SA Menzel Bourguiba", "CO Transports",
                    "NB: COT-SAMB was awarded a win to COT")],
    "1980/81": [_wo("tun81", "CS Sfaxien", "US Monastir", "CS Sfaxien", "NB: CSS-USMo was awarded a win to CSS")],
    # 2025/26: o ogol traz o jogo sem placar ("DA", decisão administrativa); a Wikipédia (nota da tabela de confrontos) dá
    # 2-0 para o CS Sfaxien por tumulto da torcida do US Monastir, e a tabela da RSSSF fecha com isso
    "2025/26": [{"mandante": "US Monastirienne", "visitante": "CS Sfaxien", "gm": 0, "gv": 2, "esp": "awd",
                 "rodada": 23, "data": "2026-03-07", "base": "ogol",
                 "fonte_id": "ogol:12087988 (sem placar, \"DA\"); resultado dado: Wikipédia (en, 2025–26 Tunisian Ligue "
                             "Professionnelle 1)",
                 "obs": "resultado dado fora de campo: 2-0 para o CS Sfaxien (tumulto da torcida do US Monastir)"}],
}
CONSERTA_TEXTO: dict[tuple[str, int], tuple[str, str, str]] = {
    ("tun06", 20): (" 12  9  3 37-19 47", " 12 11  3 37-19 47", "Club Africain: 12+9+3 dá 24 jogos (são 26) e 47 pontos só "
                    "fecham com 11 empates; a linha não era lida e a tabela se partia em duas"),
}
CORRIGE: dict[tuple[str, str], dict] = {
    # a nota da página vem antes do placar e quebrada em duas linhas ("[2-0 awarded; originally 0-0; / Monastir fielded
    # ineligible player]"): o leitor não pega o 2-0
    ("2006/07", "tun07:186"): {"oficial": (2, 0),
                               "nota": "2-0 dado ao CS Hammam-Lif: o US Monastir escalou jogador irregular",
                               "motivo": "2-0 dado ao CS Hammam-Lif (jogador irregular do US Monastir); em campo 0-0"},
    # 2025/26: resultados dados fora de campo (notas da tabela de confrontos da Wikipédia; a tabela da RSSSF fecha com eles)
    ("2025/26", "ogol:11155620"): {"oficial": (0, 2),
                                   "nota": "2-0 dado ao Club Africain por tumulto da torcida do CA Bizertin",
                                   "motivo": "2-0 dado ao Club Africain por tumulto da torcida do CA Bizertin (Wikipédia); "
                                             "em campo 0-1"},
    ("2025/26", "ogol:12046043"): {"oficial": (0, 2),
                                   "nota": "2-0 dado ao Olympique Béja: o Stade Tunisien pôs 5 estrangeiros em campo ao "
                                           "mesmo tempo",
                                   "motivo": "2-0 dado ao Olympique Béja porque o Stade Tunisien pôs 5 estrangeiros em campo "
                                             "ao mesmo tempo (Wikipédia); em campo 3-2"},
}
ANULA_CLUBE: dict[str, tuple[str, str]] = {}
TABELAS_FORA: dict[tuple[str, str], str] = {}
_MATRIZ = ("a tabela de confrontos da página e a tabela final não fecham num par de jogos (vitória e derrota trocadas, ou "
           "um gol a mais); sem terceira fonte para esses anos (a Wikipédia não tem tabela), nenhum placar foi mudado e a "
           "classificação é a tabela publicada")
EXPLICACOES: dict[str, list[str]] = {
    **{t: [_MATRIZ] for t in ("1968/69", "1977/78", "1980/81", "1982/83", "1987/88", "1988/89", "1989/90", "1990/91",
                              "1993/94")},
    "1994/95": ["a tabela de confrontos da página não fecha com a tabela final em 13 dos 14 clubes (somada à parte, sem o "
                "leitor, dá os mesmos números): erro da própria página, sem terceira fonte; nenhum placar foi mudado e a "
                "classificação é a tabela publicada"],
    "2025/26": ["três resultados dados fora de campo (2-0), pelas notas da tabela de confrontos da Wikipédia; com eles a "
                "tabela da RSSSF fecha"],
    "1909/10": ["a Wikipédia lista um título do Racing Club de Tunis, que a RSSSF não traz (para ela, não houve "
                "campeonato): a temporada fica de fora"],
}
