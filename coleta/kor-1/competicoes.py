"""Quais competições do portal da K League são a 1ª divisão de cada ano.

O calendário do portal mistura a liga com a copa da liga (아디다스컵, 리그컵, 프로스펙스컵, 대한화재컵, 하우젠컵, 피스컵,
포스코컵, 러시앤캐시컵, 1986 프로축구선수권대회), a repescagem contra a K League 2 (승강PO), a K League 2 e os torneios de
base. Cuidado: o patrocínio pôs "copa" no nome da própria liga em vários anos (96-97 라피도컵 프로축구대회, 98 현대컵 K-리그,
99 바이코리아컵 K-리그): o que vale é o número da competição no ano (meet_seq).

- meet_seq 1 é sempre a liga do ano (com os playoffs do título dentro, de 1998 a 2012);
- a final do título foi uma competição à parte em 1984 (2), 1986 (3), 1995 (3) e 1996 (3);
- o resto fica de fora.
"""
from __future__ import annotations

FINAIS = {("1984", "2"), ("1986", "3"), ("1995", "3"), ("1996", "3")}


def eh_primeira(j: dict) -> bool:
    return j["meet_seq"] == "1" or (j["ano"], j["meet_seq"]) in FINAIS
