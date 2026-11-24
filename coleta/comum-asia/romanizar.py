"""Romanização de nomes coreanos (hangul) para o alfabeto latino, pela romanização revisada do coreano, com o sobrenome na
grafia de costume (김 Kim, 이 Lee, 박 Park, 정 Jeong...), como a K League e a imprensa escrevem.

- Nome coreano (o 1º caractere, ou os 2 primeiros, é um sobrenome da lista): "정동복" -> "Jeong Dong-bok".
- Nome que não começa por sobrenome coreano é, quase sempre, de jogador estrangeiro escrito em hangul ("데얀"): as
  sílabas vão juntas, sem hífen ("Deyan"). É só uma aproximação; o nome original (em inglês) vem de outra fonte quando há.

Uso como biblioteca: romanizar("정동복") -> "Jeong Dong-bok"
"""
from __future__ import annotations

INICIAIS = ["g", "kk", "n", "d", "tt", "r", "m", "b", "pp", "s", "ss", "", "j", "jj", "ch", "k", "t", "p", "h"]
VOGAIS = ["a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae", "oe", "yo", "u", "wo", "we", "wi", "yu", "eu",
          "ui", "i"]
FINAIS = ["", "k", "k", "k", "n", "n", "n", "t", "l", "k", "m", "l", "l", "l", "p", "l", "m", "p", "p", "t", "t", "ng", "t",
          "t", "k", "t", "p", "t"]

SOBRENOMES = {
    "황보": "Hwangbo", "남궁": "Namgoong", "선우": "Sunwoo", "제갈": "Jegal", "독고": "Dokgo", "사공": "Sagong",
    "김": "Kim", "이": "Lee", "박": "Park", "최": "Choi", "정": "Jeong", "강": "Kang", "조": "Cho", "윤": "Yoon", "장": "Jang",
    "임": "Lim", "한": "Han", "오": "Oh", "서": "Seo", "신": "Shin", "권": "Kwon", "황": "Hwang", "안": "Ahn", "송": "Song",
    "류": "Ryu", "유": "Yoo", "홍": "Hong", "전": "Jeon", "고": "Ko", "문": "Moon", "양": "Yang", "손": "Son", "배": "Bae",
    "백": "Baek", "허": "Heo", "노": "Noh", "남": "Nam", "심": "Shim", "하": "Ha", "곽": "Kwak", "성": "Sung", "차": "Cha",
    "주": "Joo", "우": "Woo", "구": "Koo", "민": "Min", "진": "Jin", "나": "Na", "지": "Ji", "엄": "Eom", "채": "Chae",
    "원": "Won", "천": "Cheon", "방": "Bang", "공": "Kong", "현": "Hyun", "변": "Byun", "염": "Yeom", "여": "Yeo", "추": "Choo",
    "도": "Do", "소": "So", "석": "Seok", "선": "Sun", "설": "Seol", "마": "Ma", "길": "Gil", "연": "Yeon", "위": "Wi",
    "표": "Pyo", "명": "Myung", "기": "Ki", "반": "Ban", "왕": "Wang", "금": "Keum", "옥": "Ok", "육": "Yook", "인": "In",
    "맹": "Maeng", "제": "Je", "모": "Mo", "탁": "Tak", "국": "Kook", "어": "Eo", "은": "Eun", "편": "Pyeon", "용": "Yong",
    "예": "Ye", "경": "Kyung", "봉": "Bong", "부": "Boo", "형": "Hyung", "범": "Beom", "피": "Pi", "함": "Ham", "태": "Tae",
    "라": "Ra", "승": "Seung", "호": "Ho", "갈": "Gal", "동": "Dong", "온": "On", "견": "Gyeon", "시": "Si", "옹": "Ong", "빈": "Bin",
}


def silaba(c: str) -> str:
    n = ord(c) - 0xAC00
    if not 0 <= n < 11172:
        return c
    return INICIAIS[n // 588] + VOGAIS[(n % 588) // 28] + FINAIS[n % 28]


def _palavra(s: str) -> str:
    return "".join(silaba(c) for c in s)


def coreano(nome: str) -> bool:
    return any(0xAC00 <= ord(c) < 0xAC00 + 11172 for c in nome)


def romanizar(nome: str) -> str:
    nome = nome.strip()
    if not coreano(nome):
        return nome
    if " " in nome:   # já separado em partes
        return " ".join(romanizar(p) for p in nome.split())
    for tam in (2, 1):
        sob = nome[:tam]
        if sob in SOBRENOMES and 2 <= len(nome) - tam + 1 <= 3 and len(nome) > tam:
            dado = "-".join(_palavra(c) for c in nome[tam:])
            return f"{SOBRENOMES[sob]} {dado[:1].upper()}{dado[1:]}"
    p = _palavra(nome)
    return p[:1].upper() + p[1:]


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for n in sys.argv[1:] or ["정동복", "이준택", "김동훈", "데얀", "황보관", "에닝요", "박지성"]:
        print(n, "->", romanizar(n))
