"""Identidade dos clubes da 1ª divisão japonesa (JSL 1965-1991/92 e J1 1993-2025).

Um cadastro por clube, com o nome atual pelo qual é conhecido no Brasil (o do ogol, quase sempre). Os clubes de
empresa da JSL que viraram clubes da J.League são o mesmo clube com outro nome (a J.League e os clubes contam a
história assim, e a lista de campeões da RSSSF também): os nomes antigos ficam no nomes_fonte.

- Toyo Industries / Toyo Kogyo / Mazda -> Sanfrecce Hiroshima; Mitsubishi (Heavy Industries, depois Motors) -> Urawa Reds;
  Furukawa (Electric, depois JR East Furukawa) -> JEF United Chiba (JEF United Ichihara até 2004); Hitachi -> Kashiwa Reysol;
  Yanmar Diesel -> Cerezo Osaka; Towa Estate Agent / Fujita -> Shonan Bellmare (Bellmare Hiratsuka até 1999);
  Toyota (Motor) -> Nagoya Grampus (Nagoya Grampus Eight até 2008); Fujitsu -> Kawasaki Frontale; Nissan -> Yokohama
  F. Marinos (Yokohama Marinos até 1998); Yomiuri -> Tokyo Verdy (Verdy Kawasaki até 2000); Sumitomo (Metal) -> Kashima
  Antlers; All Nippon Airways -> Yokohama Flügels; Matsushita -> Gamba Osaka; Yamaha (Motors) -> Júbilo Iwata;
  Toshiba -> Consadole Sapporo (o Toshiba de Kawasaki mudou para Sapporo em 1996 e virou o Consadole).
- Yokohama F. Marinos x Yokohama Flügels: em 1999 o Flügels fechou e o Marinos ganhou o "F." no nome. São dois clubes: o
  Flügels fica com a história dele (1993-1998, e o ANA na JSL).
- Clubes da JSL que não chegaram à J.League ficam com o último nome da JSL: Nippon Steel Yawata (Yawata Steel até 1969),
  NKK (Nippon Kokan até 1988), Honda FC, Nagoya Bank, Toyoda ALW (Toyoda Automatic Loom Works), Tanabe Pharmaceuticals,
  Eidai Industries.

REGRAS: (regex sobre a chave do nome, nome de exibição). A chave é o nome em minúsculas, só letras e números.
"""
from __future__ import annotations

import re
import unicodedata

# nome de exibição -> (cidade, província)
CLUBES: dict[str, tuple[str, str]] = {
    "Kashima Antlers": ("Kashima", "Ibaraki"),
    "Urawa Reds": ("Saitama", "Saitama"),
    "JEF United Chiba": ("Chiba", "Chiba"),
    "Kashiwa Reysol": ("Kashiwa", "Chiba"),
    "Tokyo Verdy": ("Tóquio", "Tóquio"),
    "FC Tokyo": ("Tóquio", "Tóquio"),
    "Machida Zelvia": ("Machida", "Tóquio"),
    "Kawasaki Frontale": ("Kawasaki", "Kanagawa"),
    "Yokohama F. Marinos": ("Yokohama", "Kanagawa"),
    "Yokohama Flügels": ("Yokohama", "Kanagawa"),
    "Yokohama FC": ("Yokohama", "Kanagawa"),
    "Shonan Bellmare": ("Hiratsuka", "Kanagawa"),
    "Shimizu S-Pulse": ("Shizuoka", "Shizuoka"),
    "Júbilo Iwata": ("Iwata", "Shizuoka"),
    "Nagoya Grampus": ("Nagoya", "Aichi"),
    "Gamba Osaka": ("Suita", "Osaka"),
    "Cerezo Osaka": ("Osaka", "Osaka"),
    "Vissel Kobe": ("Kobe", "Hyogo"),
    "Kyoto Sanga": ("Kyoto", "Kyoto"),
    "Sanfrecce Hiroshima": ("Hiroshima", "Hiroshima"),
    "Avispa Fukuoka": ("Fukuoka", "Fukuoka"),
    "Sagan Tosu": ("Tosu", "Saga"),
    "Oita Trinita": ("Oita", "Oita"),
    "Consadole Sapporo": ("Sapporo", "Hokkaido"),
    "Vegalta Sendai": ("Sendai", "Miyagi"),
    "Montedio Yamagata": ("Tendo", "Yamagata"),
    "Omiya Ardija": ("Saitama", "Saitama"),
    "Albirex Niigata": ("Niigata", "Niigata"),
    "Ventforet Kofu": ("Kofu", "Yamanashi"),
    "Matsumoto Yamaga": ("Matsumoto", "Nagano"),
    "Tokushima Vortis": ("Tokushima", "Tokushima"),
    "V-Varen Nagasaki": ("Nagasaki", "Nagasaki"),
    "Fagiano Okayama": ("Okayama", "Okayama"),
    "Nippon Steel Yawata": ("Kitakyushu", "Fukuoka"),
    "NKK": ("Kawasaki", "Kanagawa"),
    "Honda FC": ("Hamamatsu", "Shizuoka"),
    "Nagoya Bank": ("Nagoya", "Aichi"),
    "Toyoda ALW": ("Kariya", "Aichi"),
    "Tanabe Pharmaceuticals": ("Osaka", "Osaka"),
    "Eidai Industries": ("Osaka", "Osaka"),
}

REGRAS: list[tuple[str, str]] = [
    # JSL (RSSSF) e artilheiros (siglas de clube)
    (r"^(toyoindustries|toyokogyo|toyo|mazda(fc|auto)?)$", "Sanfrecce Hiroshima"),
    (r"^(yawatasteel|yawata|nipponsteel(yawata)?(sc)?)$", "Nippon Steel Yawata"),
    (r"^(furukawa(electric)?|jreastfurukawa(fc)?|eastfurukawa)$", "JEF United Chiba"),
    (r"^hitachi$", "Kashiwa Reysol"),
    (r"^mitsubishi(motors(fc)?)?$", "Urawa Reds"),
    (r"^yanmar(diesel)?$", "Cerezo Osaka"),
    (r"^(towaestate(agent)?|fujita(industries)?)$", "Shonan Bellmare"),
    (r"^toyota(motors?)?(fc)?$", "Nagoya Grampus"),
    (r"^fujitsu$", "Kawasaki Frontale"),
    (r"^nissan(motors)?(fc)?$", "Yokohama F. Marinos"),
    (r"^yomiuri(club|nippon(fc)?)?$", "Tokyo Verdy"),
    (r"^sumitomo(metal)?$", "Kashima Antlers"),
    (r"^(allnipponairways(sato)?|ana)$", "Yokohama Flügels"),
    (r"^(matsushita|matshushita)(electric)?$", "Gamba Osaka"),
    (r"^(yamaha|yamada)(motors)?(fc)?$", "Júbilo Iwata"),
    (r"^toshiba(kawasaki)?$", "Consadole Sapporo"),
    (r"^(nipponkokan|nkk)(sc)?$", "NKK"),
    (r"^honda(fc|motors)?$", "Honda FC"),
    (r"^nagoyabank$", "Nagoya Bank"),
    (r"^toyodaalw$", "Toyoda ALW"),
    (r"^tanabe(pharma(ceuticals)?)?$", "Tanabe Pharmaceuticals"),
    (r"^eidai(industries)?$", "Eidai Industries"),
    # J.League (nomes completos da página do jogo, da RSSSF, do ogol e da ESPN)
    (r"^kashima(antlers)?$", "Kashima Antlers"),
    (r"^urawa(reds|reddiamonds)?$", "Urawa Reds"),
    (r"^jefunited(ichihara|chiba|ichiharachiba)?$|^chiba$|^ichihara$", "JEF United Chiba"),
    (r"^kashiwa(reysol)?$", "Kashiwa Reysol"),
    (r"^(verdykawasaki|tokyoverdy(1969)?|vkawasaki|tokyov)$", "Tokyo Verdy"),
    (r"^f(c)?tokyo$", "FC Tokyo"),
    (r"^(fc)?machida(zelvia)?$", "Machida Zelvia"),
    (r"^kawasaki(frontale|f)$", "Kawasaki Frontale"),
    (r"^yokohama(f?marinos|fmarinos|m|fm)$|^yokahamam$", "Yokohama F. Marinos"),
    (r"^yokohama(flugels|flügels|f)$|^yokahamaf$", "Yokohama Flügels"),
    (r"^yokohamafc$", "Yokohama FC"),
    (r"^(bellmarehiratsuka|shonanbellmare|shonan|hiratsuka)$", "Shonan Bellmare"),
    (r"^shimizu(spulse)?$", "Shimizu S-Pulse"),
    (r"^(jubilo|júbilo)?iwata$|^jubiloiwata$|^júbiloiwata$", "Júbilo Iwata"),
    (r"^nagoya(grampus(eight)?)?$", "Nagoya Grampus"),
    (r"^(gamba(osaka)?|gosaka)$", "Gamba Osaka"),
    (r"^(cerezo(osaka)?|cosaka)$", "Cerezo Osaka"),
    (r"^(visselkobe|kobe)$", "Vissel Kobe"),
    (r"^kyoto(purple)?sanga(fc)?$|^kyoto$", "Kyoto Sanga"),
    (r"^(sanfrecce)?hiroshima$|^sanfreccehiroshima$", "Sanfrecce Hiroshima"),
    (r"^(avispa)?fukuoka$|^avispafukuoka$", "Avispa Fukuoka"),
    (r"^(sagan)?tosu$|^sagantosu$", "Sagan Tosu"),
    (r"^(oita(trinita)?|oitatrinity)$", "Oita Trinita"),
    (r"^(hokkaido)?consadolesapporo$|^sapporo$", "Consadole Sapporo"),
    (r"^(vegalta)?sendai$|^vegaltasendai$", "Vegalta Sendai"),
    (r"^(montedio)?yamagata$|^montedioyamagata$", "Montedio Yamagata"),
    (r"^(omiya(ardija)?|rbomiyaardija)$", "Omiya Ardija"),
    (r"^(albirex)?niigata$|^albirexniigata$", "Albirex Niigata"),
    (r"^(ventforet)?kofu$|^ventforetkofu$", "Ventforet Kofu"),
    (r"^matsumoto(yamaga)?(fc)?$", "Matsumoto Yamaga"),
    (r"^(tokushima(vortis)?)$", "Tokushima Vortis"),
    (r"^v?varennagasaki$|^nagasaki$", "V-Varen Nagasaki"),
    (r"^(fagiano)?okayama$|^fagianookayama$", "Fagiano Okayama"),
]


def chave(nome: str) -> str:
    n = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", n)


_COMP = [(re.compile(r), c) for r, c in REGRAS]


def clube(nome: str) -> str | None:
    """Nome de exibição do clube para um nome de qualquer fonte; None se nenhuma regra serve."""
    k = chave(nome)
    for r, c in _COMP:
        if r.search(k):
            return c
    return None


assert all(c in CLUBES for _, c in REGRAS), [c for _, c in REGRAS if c not in CLUBES]
