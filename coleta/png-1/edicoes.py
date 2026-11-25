"""Edições da 1ª divisão de Papua-Nova Guiné (png-1): a National Soccer League (2006-2022), rebatizada Premier Soccer League
em 2023, uma edição por título, como na lista de campeões da RSSSF (pngchamp.html). Escopo aprovado pelo Guilherme em
24/11/2026, depois de pesquisa a fundo:
- só a NSL/PSL, desde 2006 (o campeonato amador de clubes de 1976-2005 fica de fora; continuou depois, abaixo da NSL);
- 2021 fica de fora (abandonada, sem campeão; o playoff que houve valeu só a vaga na OFC); a "National Premier League"
  rebelde de 2017-2018 (federação FFPNG, dissolvida na reunificação) também;
- 2008/09 e 2017: a final não foi jogada, o campeão é o 1º da fase regular; 2014: a final foi abandonada com 3-0 para o
  Hekari, que ficou com o título; 2026: sem playoff (o 1º da fase regular é o campeão).

A RSSSF tem uma página por temporada (a lista de campeões não liga quase nenhuma): fase regular (ou conferências regionais
em 2015/16, 2019 e 2022) e o mata-mata dos primeiros; 2011/12 só a tabela e o mata-mata. Pontuação 3-1-0.

Cada trecho é (página, linha inicial, linha final, fase, grupo), em linhas do texto puro (rsssf_oce.texto).
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
SLUG = "png-1"
PASTA_DADOS = RAIZ / "data" / "coleta" / SLUG
PACOTE = PASTA_DADOS / "pacote"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"

UNICA = "Fase única"
LIGA = "Fase regular"
REGIONAL = "Fase regional"
GRUPOS = "Fase de grupos"
TITULO = "Grupo do título"
REBAIX = "Grupo do rebaixamento"
PLAYOFF_CONF = "Playoff da conferência"
QUARTAS = "Quartas de final"
SEMI = "Semifinal"
TERCEIRO = "Disputa do 3º lugar"
FINAL = "Final"


@dataclass
class Edicao:
    temporada: str
    ano_inicio: int
    ano_fim: int
    nome_oficial: str
    trechos: list[tuple[str, int, int, str, str]]
    pontos: tuple[int, int, int] | None
    obs: str = ""
    incompleta: str = ""
    acumula: bool = False


def _mm(pg: str, liga: tuple[int, int], semi: int, ter: int | None, fin: int, fim: int) -> list:
    """Fase regular e o mata-mata dos 4 primeiros (semifinais, 3º lugar, final)."""
    tr = [(pg, liga[0], liga[1], LIGA, ""), (pg, liga[1], ter or fin, SEMI, "")]
    if ter:
        tr.append((pg, ter, fin, TERCEIRO, ""))
    return tr + [(pg, fin, fim, FINAL, "")]


_ED: list[tuple] = [
    ("2006", 2006, 2006, _mm("png06", (71, 169), 169, 176, 179, 183), ""),
    ("2007/08", 2007, 2008, _mm("png07", (16, 193), 193, 199, 202, 211), ""),
    ("2008/09", 2008, 2009, _mm("png08", (16, 153), 153, 159, 162, 172),
     "a final (Hekari Souths United x CMSS Rapatona Tigers) não foi jogada: o Hekari, 1º da fase regular, foi declarado campeão"),
    ("2009/10", 2009, 2010, _mm("png09", (20, 224), 224, 233, 237, 242), ""),
    ("2010/11", 2010, 2011, _mm("png2011", (20, 158), 158, 164, 167, 175), ""),
    ("2011/12", 2011, 2012, _mm("png2012", (20, 39), 39, 46, 49, 56), ""),
    ("2013", 2013, 2013, _mm("png2012a", (20, 166), 166, 176, 180, 190), ""),
    ("2014", 2014, 2014, _mm("png2014", (20, 137), 137, 148, 151, 160),
     "a final foi abandonada aos 70' com 3-0 para o Hekari United (violência da torcida); o título ficou com o Hekari"),
    ("2015", 2015, 2015, _mm("png2015", (20, 153), 153, 159, 162, 169), ""),
    ("2015/16", 2015, 2016, [("png2016", 24, 104, REGIONAL, "Northern Zone"), ("png2016", 104, 195, REGIONAL, "Southern Zone"),
                             ("png2016", 195, 238, TITULO, ""), ("png2016", 238, 247, FINAL, "")],
     "duas zonas de 6; os 2 primeiros de cada zona num grupo de 4 (\"National Champions League\") e depois a final"),
    ("2017", 2017, 2017, [("png2017", 26, 125, LIGA, ""), ("png2017", 125, 137, SEMI, ""), ("png2017", 137, 149, FINAL, "")],
     "a final (Lae City Dwellers x Madang FC) foi cancelada: o Lae City Dwellers, 1º da fase regular, foi declarado campeão"),
    ("2018", 2018, 2018, _mm("png2018", (28, 172), 172, 178, 181, 190),
     "em 3 de maio os jogos restantes da fase regular viraram W.O. (só 4 clubes tinham pago a taxa)"),
    ("2019", 2019, 2019, [("png2019", 32, 159, REGIONAL, "Southern Conference"), ("png2019", 159, 287, REGIONAL, "Northern Conference"),
                          ("png2019", 287, 369, REGIONAL, "Highlands Conference"), ("png2019", 369, 463, REGIONAL, "New Guinea Islands Conference"),
                          ("png2019", 463, 478, QUARTAS, ""), ("png2019", 478, 490, SEMI, ""), ("png2019", 490, 493, TERCEIRO, ""),
                          ("png2019", 493, 499, FINAL, "")], "quatro conferências regionais e o mata-mata"),
    ("2019/20", 2019, 2020, _mm("png2020", (28, 311), 311, 319, 323, 330), "parada de 19/03 a 08/08/2020 (covid-19)"),
    ("2022", 2022, 2023, [("png2022", 36, 120, REGIONAL, "Southern Conference"), ("png2022", 120, 196, REGIONAL, "Northern Conference"),
                          ("png2022", 196, 276, REGIONAL, "Highlands Conference"),
                          ("png2022", 276, 348, REGIONAL, "New Guinea Islands Central Conference"),
                          ("png2022", 348, 355, PLAYOFF_CONF, "New Guinea Islands Central Conference"),
                          ("png2022", 355, 439, REGIONAL, "New Guinea Islands Eastern Conference"),
                          ("png2022", 439, 446, PLAYOFF_CONF, "New Guinea Islands Eastern Conference"),
                          ("png2022", 446, 456, QUARTAS, ""), ("png2022", 456, 460, SEMI, ""), ("png2022", 460, 463, TERCEIRO, ""),
                          ("png2022", 463, 470, FINAL, "")], "cinco conferências regionais (nas duas das ilhas, playoff entre o 1º e o 2º pela vaga) e o mata-mata (de outubro de 2022 a fevereiro de 2023)"),
    ("2023", 2023, 2023, _mm("png2023", (28, 177), 177, 183, 186, 192), "a liga passa a se chamar Premier Soccer League"),
    ("2024", 2024, 2024, _mm("png2024", (28, 175), 175, 181, 184, 207), ""),
    ("2025", 2025, 2025, _mm("png2025", (26, 284), 284, 290, 293, 312), ""),
    ("2026", 2026, 2026, [("png2026", 23, 314, UNICA, "")], "sem playoff: o 1º da fase regular é o campeão"),
]

EDICOES: list[Edicao] = []
for _t, _i, _f, _tr, _obs in _ED:
    _nome = ("Premier Soccer League " if _i >= 2023 else "National Soccer League ") + _t
    EDICOES.append(Edicao(_t, _i, _f, _nome, _tr, (3, 1, 0), obs=_obs,
                          incompleta="a RSSSF só tem a tabela da fase regular e o mata-mata" if _t == "2011/12" else ""))
