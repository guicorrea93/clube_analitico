"""Nome de exibição dos jogadores da K League.

As fontes: o portal dá o nome em hangul (todas as épocas) e o código do jogador nos gols; o site oficial dá o nome em
inglês pelo código (jogadores com jogo de 2013 em diante, ler_oficial.nomes()); a RSSSF dá os autores dos gols em
alfabeto latino em muitos anos (ligados pelo minuto do gol, nomes_rsssf).

- Coreano (o hangul começa por sobrenome e o nome em inglês, quando há, tem esse sobrenome): romanização revisada com o
  sobrenome de costume ("정동복" -> "Jeong Dong-bok"; comum-asia/romanizar.py). Assim todos ficam na mesma grafia; o
  inglês do site oficial varia ("Jongkook KIM", "LEE Jeho", "HWANG, In Ho").
- Estrangeiro com nome em inglês: o hangul é o nome de jogo ("호벨손" Roberson) e o inglês é o nome civil inteiro
  ("ROBERSON DE ARRUDA ALVES"); fica a parte do nome civil que mais se parece com o hangul ("Roberson"). Se o inglês tem
  só nome e sobrenome ("Ikromjon ALIBAEV", "YUKI Kobayashi"), fica o nome todo ("Ikromjon Alibaev", "Yuki Kobayashi").
- Estrangeiro sem nome em inglês (só antes de 2013): o nome da RSSSF, se houver; se não, o hangul romanizado (aproximação,
  listada no relatório).
"""
from __future__ import annotations

import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum-asia"))
from romanizar import SOBRENOMES, _palavra, coreano, romanizar  # noqa: E402

VARIANTES = {
    "이": "LEE YI RHEE RI I", "정": "JEONG JUNG CHUNG JOUNG JEUNG CHEONG", "고": "KO KOH GO", "안": "AHN AN",
    "조": "CHO JO JOE", "윤": "YOON YUN YOUN", "임": "LIM IM LYM", "신": "SHIN SIN", "유": "YOO YU RYU", "류": "RYU YOO YU",
    "금": "KEUM GEUM KUM", "노": "NOH ROH NO", "오": "OH O", "최": "CHOI CHOE", "강": "KANG GANG", "권": "KWON KWEON GWON KOUEN KWOUN",
    "구": "KOO KU GU", "김": "KIM GIM", "박": "PARK BAK PAK", "서": "SEO SUH", "설": "SEOL SUL", "우": "WOO U",
    "주": "JOO JU CHU", "전": "JEON JUN CHUN", "문": "MOON MUN", "손": "SON SOHN", "배": "BAE BAI", "백": "BAEK BAIK PAIK",
    "허": "HEO HUH HUR HER", "심": "SHIM SIM", "곽": "KWAK GWAK", "성": "SUNG SEONG", "진": "JIN CHIN", "지": "JI CHI GI",
    "엄": "EOM UM EUM", "천": "CHEON CHUN", "공": "KONG GONG", "현": "HYUN HYEON", "변": "BYUN BYEON", "염": "YEOM YUM",
    "추": "CHOO CHU", "도": "DO DOH", "석": "SEOK SUK", "길": "GIL KIL", "위": "WI WEE", "명": "MYUNG MYEONG",
    "기": "KI GI", "육": "YOOK YUK", "국": "KOOK GUK", "경": "KYUNG GYEONG", "부": "BOO BU", "라": "RA NA", "나": "NA RA",
    "시": "SI SHI", "여": "YEO YE YOE", "선": "SUN SEON", "남궁": "NAMGOONG NAMGUNG", "선우": "SUNWOO SEONU",
}


# estrangeiros com apelido que não está no nome civil em inglês (o hangul é o apelido): nome de jogo à mão
NOME_DE_JOGO = {"세징야": "Cesinha", "하피냐": "Rafinha", "제카": "Zeca", "찌아구": "Tiago", "룰리냐": "Lulinha", "지쿠": "Zicu",
                "믹스": "Mix Diskerud", "까이끼": "Caíque", "마라냥": "Maranhão", "바그닝요": "Wagninho",
                # antes de 2013, sem nome em inglês nem autor na RSSSF
                "피아퐁": "Piyapong", "슈바": "Chuva", "알미르": "Almir", "루이지뉴": "Luizinho", "뽀뽀": "Popó"}


def _sobrenome(h: str) -> str | None:
    for tam in (2, 1):
        if h[:tam] in SOBRENOMES and 2 <= len(h) - tam + 1 <= 3 and len(h) > tam:
            return h[:tam]
    return None


def _tokens(en: str) -> list[str]:
    return [t for t in re.split(r"[\s,]+", en.strip()) if t]


def eh_coreano(h: str, en: str = "") -> bool:
    h = re.sub(r"\d+$", "", h.strip())
    if not coreano(h) or " " in h:
        return False
    s = _sobrenome(h)
    if not s and en and len(h) == 4 and h[0] in SOBRENOMES:   # nome dado de 3 sílabas ("윤빛가람"): só com o inglês
        s = h[0]
    if not s:
        return False
    if not en:
        return True
    var = set(VARIANTES.get(s, "").split()) | {SOBRENOMES[s].upper(), _palavra(s).upper()}
    toks = [t.upper().strip(".") for t in _tokens(en)]
    if any(t in var for t in toks):
        return True
    # grafias soltas do sobrenome ("BACK" Baek, "YOU" Yoo, "KWOUN" Kwon): o sobrenome parecido e o nome dado também
    dado = _simples(_palavra(h[len(s):]))
    for i, t in enumerate(toks):
        if max(SequenceMatcher(None, _simples(v), _simples(t)).ratio() for v in var) >= 0.6:
            resto = _simples("".join(toks[:i] + toks[i + 1:]))
            if resto and SequenceMatcher(None, dado, resto).ratio() >= 0.5:
                return True
    return False


def _titulo(t: str) -> str:
    return "-".join(p[:1].upper() + p[1:].lower() for p in t.split("-"))


def _simples(s: str) -> str:
    """Forma grosseira para comparar grafias (ㄱ g/k, ㄷ d/t, ㅂ b/p, ㅈ j/ch, ㄹ r/l, 어 eo/o/u...)."""
    s = re.sub(r"[^a-z]", "", s.lower())
    for a, b in (("ph", "b"), ("ch", "j"), ("eo", "o"), ("eu", "u"), ("ou", "u"), ("oo", "u"), ("ae", "e"), ("k", "g"),
                 ("t", "d"), ("p", "b"), ("f", "b"), ("v", "b"), ("r", "l"), ("w", ""), ("y", ""), ("h", "")):
        s = s.replace(a, b)
    return s


def estrangeiro(h: str, en: str) -> str:
    toks = _tokens(en)
    if not toks:
        return romanizar(h)
    alvo = _simples(_palavra(re.sub(r"[\d\s]+", "", h)))
    melhor, nota = None, 0.0
    for i in range(len(toks)):
        for k in (1, 2):
            cand = " ".join(toks[i:i + k])
            r = SequenceMatcher(None, alvo, _simples(cand)).ratio()
            if r > nota + 0.05:
                melhor, nota = cand, r
    if melhor and nota >= 0.6:
        return " ".join(_titulo(t) for t in melhor.split())
    return " ".join(_titulo(t) for t in toks)


def coreano_en(h: str, en: str) -> str | None:
    """Coreano com a grafia oficial em inglês, no formato "Sobrenome Nome-dado": "Donggook LEE" (이동국) -> "Lee Dong-gook";
    "HWANG, In Ho" -> "Hwang In-ho". O nome dado é cortado nas sílabas do hangul (3 sílabas, "Bitgaram YOON" -> "Yoon
    Bitgaram", vai sem corte). None se não der para cortar."""
    s = _sobrenome(h) or h[0]
    var = set(VARIANTES.get(s, "").split()) | {SOBRENOMES[s].upper(), _palavra(s).upper()}
    toks = _tokens(en)
    i = next((k for k, t in enumerate(toks) if t.upper().strip(".") in var), None)
    if i is None:
        i = max(range(len(toks)), key=lambda k: max(SequenceMatcher(None, _simples(v), _simples(toks[k])).ratio() for v in var))
    sob = _titulo(toks[i])
    partes = [x.lower() for x in toks[:i] + toks[i + 1:]]
    dado = "".join(partes)
    sil = [_palavra(c) for c in h[len(s):]]
    if not dado or not sil:
        return None
    if len(sil) == 1:
        return f"{sob} {dado.capitalize()}"
    if len(sil) == 3:
        return f"{sob} {dado.capitalize()}"
    if len(sil) != 2:
        return None
    if len(partes) == 1 and partes[0].count("-") == 1:   # já com hífen ("Eun-joong KIM")
        partes = partes[0].split("-")
    if len(partes) == 2:   # o inglês já separa as sílabas ("Kim, Young Ou", "HEE JUN PARK")
        return f"{sob} {partes[0].capitalize()}-{partes[1]}"
    if len(re.findall(r"[aeiouy]+", dado)) < 2:   # o inglês tem sílabas de menos ("Dae LEE" para 이대광): fica o hangul
        return None
    alvo = _simples(sil[0])
    consoante = sil[1][:1] not in "aeiouwy"   # a 2ª sílaba começa por consoante: o corte também

    def nota(k: int) -> tuple:
        a_, b_ = dado[:k], dado[k:]
        tamanho_ok = len(a_) >= len(sil[0]) - 2 and len(b_) >= len(sil[1]) - 2
        semelhanca = sum(SequenceMatcher(None, x, y).ratio() for x, y in ((sil[0], a_), (sil[1], b_))) +             sum(SequenceMatcher(None, _simples(x), _simples(y)).ratio() for x, y in ((sil[0], a_), (sil[1], b_)))
        vogais_ok = bool(re.search(r"[aeiouy]", a_)) and bool(re.search(r"[aeiou]", b_)) and a_[-1] not in "wy"
        return (vogais_ok, tamanho_ok, not consoante or b_[:1] not in "aeiouwy", semelhanca)

    corte = max(range(1, len(dado)), key=nota)
    return f"{sob} {dado[:corte].capitalize()}-{dado[corte:]}"


def nome(h: str, en: str = "", rsssf: str = "") -> tuple[str, str]:
    """(nome de exibição, de onde veio)."""
    h = re.sub(r"\d+$", "", (h or "").strip())
    if not h:
        return (_titulo(en) if en else "", "inglês")
    if h in NOME_DE_JOGO:
        return NOME_DE_JOGO[h], "apelido (à mão)"
    if not en and rsssf and not re.match(r"^[A-Z][a-z]+ [A-Z][a-z]+-[A-Za-z]+$", rsssf):
        return rsssf, "RSSSF"   # a RSSSF não escreve como nome coreano ("Piyapong", 피아퐁): é estrangeiro
    if eh_coreano(h, en):
        if en:
            c = coreano_en(h, en)
            if c:
                return c, "inglês (grafia oficial)"
        return romanizar(h), "hangul"
    if en:
        return estrangeiro(h, en), "inglês"
    if rsssf:
        return rsssf, "RSSSF"
    return romanizar(h), "hangul (estrangeiro, aproximação)"
