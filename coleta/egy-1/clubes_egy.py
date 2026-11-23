"""Identidade dos clubes egípcios: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4) e do recado do agente 1 (23/11/2026):
- nomes árabes sempre com hífen; fica com o nome puro o clube mais conhecido no Brasil (Al-Ahly); os outros levam a cidade
  quando há outro igual no mundo: "Al-Ittihad de Alexandria" (o Al-Ittihad é o da Arábia Saudita), "Al-Ittihad de Suez",
  "Al-Nasr do Cairo" (o Al-Nassr é o saudita), "El-Merreikh de Port Said" (o Al-Merrikh é o do Sudão);
- a grafia segue o nome mais usado em inglês (Wikipédia), com hífen no artigo: "Ghazl El-Mahalla", "Haras El-Hodoud",
  "El-Gouna", "Al-Mokawloon Al-Arab";
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - Farouk Club / King Farouk Club (até 1952) e El-Mokhtalat -> Zamalek;
  - Sawahel (Guarda Costeira, 1963-1964) -> Haras El-Hodoud (Guarda de Fronteira; o ogol trata como o mesmo clube);
  - Al-Assiouty Sport (2014-2017) -> Pyramids (comprado e renomeado em 2018; o ogol trata como o mesmo clube);
  - Ittihad Othman (até 1996/97) -> Dina Farms (a RSSSF de 1997/98: "new name for Ittihad Othman");
  - Al-Ma'aden (até 2000/01) -> Goldy (a RSSSF de 2001/02: "changed name to Goldy");
  - FC Masr (2019) -> ZED (renomeado em 2022; o ogol trata como o mesmo clube);
  - Future FC / Modern Future (2021-2023) -> Modern Sport (o ogol trata como o mesmo clube);
  - Itesalat (2007-2008) -> Telecom Egypt; Al-Shourta (1975/76, "aka Police") -> Ittihad El-Shorta (o clube da polícia);
  - Suez El-Riyadi -> Suez; Qanah / Canal / Qanat (Port Said) -> El-Qanah (o ogol tem um só código de 1964 a 2013);
  - Ala'ab Damanhour (2013/14) -> Damanhour (o ogol trata como o mesmo clube);
  - Tersana também aparece como "Arsenal" (1990/91); El-Gaish (Tala'ea El-Gaish, o clube do Exército) como "Al-Jaish" e
    "Army Club".
- "Mahala"/"Mehalla"/"Al Mehalla" sozinho é o Ghazl El-Mahalla; o Baladiyat El-Mahalla vem sempre com "Baladeya",
  "Baladia" ou "Baladiyyat" (ou "B Mehalla").

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-africa"))
from rsssf_africa import chave  # noqa: E402

CAI = ("Cairo", "Cairo")
GIZ = ("Gizé", "Gizé")
ALX = ("Alexandria", "Alexandria")
PSD = ("Port Said", "Port Said")
SUE = ("Suez", "Suez")
ISM = ("Ismailia", "Ismailia")

# nome de exibição -> (cidade, província)
CLUBES: dict[str, tuple[str, str]] = {
    "Al-Ahly": CAI, "Zamalek": GIZ, "Tersana": GIZ, "Al-Mokawloon Al-Arab": CAI, "El-Sekka El-Hadid": CAI,
    "El-Tayaran": CAI, "Al-Nasr do Cairo": CAI, "Naseeg Helwan": CAI, "Factory 36": CAI, "El-Shams": CAI,
    "Wadi Degla": CAI, "ENPPI": CAI, "Petrojet": CAI, "El-Dakhleya": CAI, "El-Entag El-Harby": CAI, "Ittihad El-Shorta": CAI,
    "Pyramids": CAI, "Ceramica Cleopatra": CAI, "National Bank of Egypt": CAI, "ZED": CAI, "Modern Sport": CAI,
    "Nogoom": CAI, "El-Gaish": CAI, "Telecom Egypt": CAI, "Eastern Company": CAI, "Dina Farms": CAI,
    "Olympic Club": ALX, "Al-Ittihad de Alexandria": ALX, "Younan": ALX, "Teram": ALX, "El-Koroum": ALX,
    "Haras El-Hodoud": ALX, "Smouha": ALX, "Pharco": ALX, "Bahareya": ALX,
    "Al-Masry": PSD, "Port Fouad": ("Port Fouad", "Port Said"), "El-Qanah": PSD, "El-Merreikh de Port Said": PSD,
    "Ismaily": ISM, "Kahraba Ismailia": ISM,
    "Suez": SUE, "Al-Ittihad de Suez": SUE, "Ghazl El-Suez": SUE, "Suez Cement": SUE, "Suez Petrol": SUE,
    "Ghazl El-Mahalla": ("El-Mahalla El-Kubra", "Gharbia"), "Baladiyat El-Mahalla": ("El-Mahalla El-Kubra", "Gharbia"),
    "Tanta": ("Tanta", "Gharbia"), "Maleyat Kafr El-Zayat": ("Kafr El-Zayat", "Gharbia"),
    "El-Mansoura": ("Mansoura", "Dakahlia"), "Belqas": ("Belqas", "Dakahlia"), "Beni Ebeid": ("Beni Ebeid", "Dakahlia"),
    "Damietta": ("Damietta", "Damietta"), "Ghazl Domiat": ("Damietta", "Damietta"),
    "El-Sharkia": ("Zagazig", "Sharqia"), "Belbeis": ("Belbeis", "Sharqia"),
    "Plastic": ("Shubra El-Kheima", "Qalyubia"), "Esco": ("Shubra El-Kheima", "Qalyubia"),
    "Damanhour": ("Damanhour", "Beheira"), "Kafr El-Sheikh": ("Kafr El-Sheikh", "Kafr El-Sheikh"),
    "Gomhoriat Shebin": ("Shebin El-Kom", "Menofia"),
    "Goldy": ("Faiyum", "Faiyum"), "Misr Lel Makkasa": ("Faiyum", "Faiyum"),
    "Beni Suef": ("Beni Suef", "Beni Suef"), "Telephonat Beni Suef": ("Beni Suef", "Beni Suef"),
    "El-Minya": ("Minya", "Minya"), "Asyut Petroleum": ("Asyut", "Asyut"), "Assiut Cement": ("Asyut", "Asyut"),
    "Sohag": ("Sohag", "Sohag"), "Aluminium": ("Nag Hammadi", "Qena"), "Aswan": ("Aswan", "Aswan"),
    "Al-Nasr Lel Taadin": ("", ""), "El-Gouna": ("El-Gouna", "Mar Vermelho"), "Al-Raja": ("Marsa Matruh", "Matruh"),
}

REGRAS: list[tuple[str, str, int, int]] = [
    # Cairo e Gizé
    (r"(al |el )?ahl[iy]( cairo)?$", "Al-Ahly", 1948, 2100),
    (r"(bank al ahly|national bank)", "National Bank of Egypt", 1948, 2100),
    (r"(zamalek|zamalak|farouk|king farouk|mokhtalat)", "Zamalek", 1948, 2100),
    (r"(al |el )?tersana|arsenal", "Tersana", 1948, 2100),
    (r"(al |el )?mo[kq]a(w|ou)l(oo|ee|ou|u)n|arab contractors", "Al-Mokawloon Al-Arab", 1948, 2100),
    (r"(al |el |tala ?ea el )?(jaish|gaish|geish)|army club", "El-Gaish", 1948, 2100),
    (r"(al |el )?sekka( al| el)?( hadid)?( cairo)?$|sekka hadid|sekka al hadid", "El-Sekka El-Hadid", 1948, 2100),
    (r"(al |el )?tayaran|aviation", "El-Tayaran", 1948, 2100),
    (r"(al |el )?nasr (lel )?taa?d[ei]+n|nasr lel taa", "Al-Nasr Lel Taadin", 1948, 2100),
    (r"(al |el )?nasr( sc| cairo)?$", "Al-Nasr do Cairo", 1948, 2100),
    (r"(helwan textiles|naseeg helwan)", "Naseeg Helwan", 1948, 2100),
    (r"factory 36", "Factory 36", 1948, 2100),
    (r"(al |el )?shams( sc)?$", "El-Shams", 1948, 2100),
    (r"wadi degla", "Wadi Degla", 1948, 2100),
    (r"en+p+i+|enbe|petroleum$", "ENPPI", 1948, 2100),
    (r"petrojet", "Petrojet", 1948, 2100),
    (r"(al |el )?dakhleya", "El-Dakhleya", 1948, 2100),
    (r"(al |el )?(intag|entag) (el )?harby|military production", "El-Entag El-Harby", 1948, 2100),
    (r"(ittihad )?(al |el )?sho?u?rta|police", "Ittihad El-Shorta", 1948, 2100),
    (r"pyramids|(al )?assiouty", "Pyramids", 1948, 2100),
    (r"ceramica", "Ceramica Cleopatra", 1948, 2100),
    (r"zed|fc masr|masr( cairo)?$", "ZED", 2019, 2100),
    (r"modern|future", "Modern Sport", 2021, 2100),
    (r"nogoom|n mostaqbal", "Nogoom", 1948, 2100),
    (r"telecom egypt|itesalat", "Telecom Egypt", 1948, 2100),
    (r"(el |al )?sharkeyah leldukhan|(al )?sharquia|sharkeyah ld|eastern company", "Eastern Company", 2020, 2100),
    (r"dina|mazarea dina|ittihad o(th|s)man|itt othman|(al )?ittihad othman", "Dina Farms", 1948, 2100),
    # Alexandria
    (r"(al |el )?olymp|olimpic", "Olympic Club", 1948, 2100),
    (r"(al |el )?ittihad( alexandria| alex)?$|itt alex|ittihad a$|(al |el )?it+i?h?a?d (al |el )?i?s[a]?kand[ae]?ry", "Al-Ittihad de Alexandria", 1948, 2100),
    (r"younan", "Younan", 1948, 2100),
    (r"teram", "Teram", 1948, 2100),
    (r"(al |el )?k[o]?roum|chrome", "El-Koroum", 1948, 2100),
    (r"(haras|h) (al |el )?h[oe]d[ou]+d|(el )?sawahel", "Haras El-Hodoud", 1948, 2100),
    (r"s[e]?mouha", "Smouha", 1948, 2100),
    (r"pharco", "Pharco", 1948, 2100),
    (r"(el )?bahar(eya|ia)", "Bahareya", 1948, 2100),
    # Port Said, Ismailia e Suez
    (r"(al |el )?masr[iy]", "Al-Masry", 1948, 2100),
    (r"port f[o]?uad|port foad", "Port Fouad", 1948, 2100),
    (r"(al |el )?(qan+ah|qanat|canal)", "El-Qanah", 1948, 2100),
    (r"(al |el )?(ma?reekh|marikh|merreikh)", "El-Merreikh de Port Said", 1948, 2100),
    (r"kahraba+", "Kahraba Ismailia", 1948, 2100),
    (r"(al )?ismail[iy]", "Ismaily", 1948, 2100),
    (r"it+i?had s(uez)?$", "Al-Ittihad de Suez", 1948, 2100),
    # o ogol tem um só "Suez Club" de 1964 a 1999; em 1965/66 ele é o Ittihad Suez da RSSSF e da Wikipédia (em 1962/63 a
    # RSSSF mostra o Ittihad Suez e o Suez El-Riyadi, cada um num grupo); nos outros anos, o Suez El-Riyadi
    (r"suez club$", "Al-Ittihad de Suez", 1965, 1965),
    (r"ghazl (al |el )?suez|g suez", "Ghazl El-Suez", 1948, 2100),
    (r"suez cement|asmant suez|asmant$|asmant (el )?suweis", "Suez Cement", 1948, 2100),
    (r"suez petrol(eum)?", "Suez Petrol", 1948, 2100),
    (r"(al )?suez( el riyadi| riyadi| club| suez)?$", "Suez", 1948, 2100),
    # Delta e Alto Egito
    (r"(baladeya|baladia|baladiyyat|baladiyat|baladeyet|bal)( al| el)?( m| mahalla| mehalla)?$|b mehalla", "Baladiyat El-Mahalla", 1948, 2100),
    (r"(ghazl|gh|g)( al| el)? m[ae]hall?a|(al |el )?m[ae]hall?a( f| fillery)?$", "Ghazl El-Mahalla", 1948, 2100),
    (r"tanta", "Tanta", 1948, 2100),
    (r"maleyat", "Maleyat Kafr El-Zayat", 1948, 2100),
    (r"(el |al )?ma[n]?s[o]?ura(h)?", "El-Mansoura", 1948, 2100),
    (r"belquas|belqas|belkas", "Belqas", 1948, 2100),
    (r"bani eb[ae]i?d|beni ebeid", "Beni Ebeid", 1948, 2100),
    (r"gazl domiat|gazl domyat|ghazl domiat", "Ghazl Domiat", 1948, 2100),
    (r"domiat|demiat|domyat|damietta", "Damietta", 1948, 2100),
    (r"(al |el )?shar(qeya|qiya|kya|kia)( sc)?$|sharqiya zaqaziq", "El-Sharkia", 1948, 2019),
    (r"(gut |jute )?b[ie]lb[ae]i?s", "Belbeis", 1948, 2100),
    (r"plastic|shobra el khema", "Plastic", 1948, 2100),
    (r"esco", "Esco", 1948, 2100),
    (r"(al |ala ab |alaab )?damanhour|alaab$", "Damanhour", 1948, 2100),
    (r"kafr el shaikh|kafr el sheikh", "Kafr El-Sheikh", 1948, 2100),
    (r"gomhuriat shebin|gomhoreyat shebin|gomhoriat shebin|sheb[ei]+n( al kom)?$", "Gomhoriat Shebin", 1948, 2100),
    (r"gold[iy]|(al )?ma ?aden", "Goldy", 1948, 2100),
    (r"misr (al |el |lel )?ma[qk]+a[sk]+ah?", "Misr Lel Makkasa", 1948, 2100),
    (r"(tele(fonad|phonat)|tele) (beni|bani) (suef+|sweif)|telefonad bs", "Telephonat Beni Suef", 1948, 2100),
    (r"(bani|beni) suef( club)?$", "Beni Suef", 1948, 2100),
    (r"(al |el )?(menya|minya|menia)( sc)?$", "El-Minya", 1948, 2100),
    (r"as[s]?[iy]o?u?t petrol(eum)?|petrol as[s]?[iy]u?t", "Asyut Petroleum", 1948, 2100),
    (r"assiou?t cement|assiut cement|asmant as[s]?[iy]u?t", "Assiut Cement", 1948, 2100),
    (r"sohag( railways| r)?$", "Sohag", 1948, 2100),
    (r"aluminium", "Aluminium", 1948, 2100),
    (r"as[s]?[uw]an( fc)?$", "Aswan", 1948, 2100),
    (r"gouna[h]?|(al |el )?gouna", "El-Gouna", 1948, 2100),
    (r"(al )?raja|razja ?h", "Al-Raja", 1948, 2100),
]


def _regra(k: str, ano: int) -> str | None:
    for kk in (k, re.sub(r"\s+(sc|fc|club)$", "", k)):
        for rx, exib, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.match(rx + r"(?:\b|$)", kk):
                return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    if not nome or nome.strip() == "Team":   # "Team": o ogol não identifica o clube (1999-2002)
        return None
    k = chave(nome)
    if cidade:
        k2 = chave(f"{nome} {cidade}")
        if (r := _regra(k2, ano)):
            return r
    return _regra(k, ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
