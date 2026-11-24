"""Identidade dos clubes da K League: um clube por código do portal oficial (K01, K04...), que é o mesmo ao longo das
mudanças de nome e de cidade, como a própria K League conta a história. Nome de exibição: o pelo qual o clube é conhecido
no Brasil (o do ogol, por extenso).

- K04: Yukong Elephants (1983) -> Puchon Yukong -> Bucheon SK -> Jeju United (2006; Jeju SK desde 2025);
- K06: Daewoo Royals -> Pusan Daewoo -> Pusan/Busan Icons -> Busan IPark;
- K08: Ilhwa Chunma (Seul) -> Chunan Ilhwa -> Seongnam Ilhwa Chunma -> Seongnam FC;
- K09: Lucky-Goldstar Hwangso -> LG Cheetahs -> Anyang LG Cheetahs -> FC Seoul (2004);
- K01: Hyundai Horang-i -> Ulsan Hyundai -> Ulsan HD; K03: POSCO Dolphins/Atoms -> Pohang Steelers;
- os clubes militares têm códigos diferentes no portal e ficam separados: Gwangju Sangmu (K14), Sangju Sangmu (K23) e
  Gimcheon Sangmu (K35); o Sangmu de 1985 (K24, time do Exército, sem sede fixa: cidade em branco) também;
- K16: Chonbuk Buffalo (1994, fechou no fim do ano; não é o Jeonbuk Hyundai, K05).

CLUBES: código -> (nome de exibição, cidade, província). Código que falta aqui para a importação (erro de propósito).
"""
from __future__ import annotations

CLUBES: dict[str, tuple[str, str, str]] = {
    "K01": ("Ulsan Hyundai", "Ulsan", "Ulsan"),
    "K02": ("Suwon Samsung Bluewings", "Suwon", "Gyeonggi"),
    "K03": ("Pohang Steelers", "Pohang", "Gyeongbuk"),
    "K04": ("Jeju United", "Seogwipo", "Jeju"),
    "K05": ("Jeonbuk Hyundai Motors", "Jeonju", "Jeonbuk"),
    "K06": ("Busan IPark", "Busan", "Busan"),
    "K07": ("Jeonnam Dragons", "Gwangyang", "Jeonnam"),
    "K08": ("Seongnam FC", "Seongnam", "Gyeonggi"),
    "K09": ("FC Seoul", "Seul", "Seul"),
    "K10": ("Daejeon Hana Citizen", "Daejeon", "Daejeon"),
    "K11": ("Hallelujah FC", "Seul", "Seul"),
    "K12": ("Kookmin Bank", "Seul", "Seul"),
    "K13": ("Hanil Bank", "Seul", "Seul"),
    "K14": ("Gwangju Sangmu", "Gwangju", "Gwangju"),
    "K16": ("Chonbuk Buffalo", "Jeonju", "Jeonbuk"),
    "K17": ("Daegu FC", "Daegu", "Daegu"),
    "K24": ("Sangmu", "", ""),
    "K18": ("Incheon United", "Incheon", "Incheon"),
    "K20": ("Gyeongnam FC", "Changwon", "Gyeongnam"),
    "K21": ("Gangwon FC", "Chuncheon", "Gangwon"),
    "K22": ("Gwangju FC", "Gwangju", "Gwangju"),
    "K23": ("Sangju Sangmu", "Sangju", "Gyeongbuk"),
    "K27": ("FC Anyang", "Anyang", "Gyeonggi"),
    "K29": ("Suwon FC", "Suwon", "Gyeonggi"),
    "K35": ("Gimcheon Sangmu", "Gimcheon", "Gyeongbuk"),
}


def clube(codigo: str) -> str:
    if codigo not in CLUBES:
        raise SystemExit(f"código de clube sem cadastro: {codigo!r} (acrescente em clubes_kor.py)")
    return CLUBES[codigo][0]
