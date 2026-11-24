"""Cadastro dos clubes da 1ª divisão turca (tur-1): chave única, cidade e país, mais os nomes de cada fonte.

Identidade (pela linhagem legal do clube, como na Wikipédia):
- o mesmo clube com nomes de época vira uma chave só: Karagümrük e Fatih Karagümrük; PTT Ankara e Türk Telekomspor;
  İstanbul B.B. e Başakşehir; Ankaraspor e Osmanlıspor (2014-2020); Şeker Hilal, Şekerspor e Beypazarı Şekerspor;
  Hacettepe e Gençlerbirliği OFTAŞ (2007/08, mesmo artigo na Wikipédia); Akhisar Belediyespor e Akhisarspor;
- Kayseri: o Kayserispor fundado em 1966 (1ª divisão de 1973/74 a 1997/98) trocou de nome, escudo e cores com o
  Erciyesspor em julho de 2004 e virou o Kayseri Erciyesspor; o Kayserispor de 2004/05 em diante é o antigo Erciyesspor
  (artigos "Kayseri Erciyesspor" e "Kayserispor" da Wikipédia);
- clubes diferentes com nome parecido ficam separados: Malatyaspor e Yeni Malatyaspor; Gaziantepspor e Gaziantep FK;
  Erzurumspor (1998-2001) e BB Erzurumspor (2018-2021); Ankaragücü e MKE Kırıkkalespor; Ankara Demirspor e Adana
  Demirspor; Ankaraspor (1978) e Şekerspor (1947).

OGOL: código do clube no ogol -> chave. Os nomes do calendário do ogol não são confiáveis nas temporadas antigas
("Yuksekova Belediyespor" em 1961/62 é o Yeşildirek, "Eskisehir Demirspor" é o Eskişehirspor); os códigos foram
identificados pelos números da campanha de cada temporada, iguais aos das tabelas da RSSSF e da Wikipédia.
OGOL_POR_ANO: códigos que o ogol usa para mais de um clube. ALIASES: grafias das fontes -> chave. POR_ANO: nomes que
dependem da época ("Kayserispor", "Ankaraspor").
"""
from __future__ import annotations

import re
import unicodedata

CLUBES: dict[str, tuple[str, str]] = {
    "Galatasaray": ("Istambul", "TUR"), "Fenerbahçe": ("Istambul", "TUR"), "Beşiktaş": ("Istambul", "TUR"),
    "Trabzonspor": ("Trabzon", "TUR"), "Gençlerbirliği": ("Ancara", "TUR"), "Ankaragücü": ("Ancara", "TUR"),
    "Ankara Demirspor": ("Ancara", "TUR"), "Hacettepe": ("Ancara", "TUR"), "Şekerspor": ("Ancara", "TUR"),
    "Türk Telekomspor": ("Ancara", "TUR"), "Petrol Ofisi": ("Ancara", "TUR"), "Ankaraspor": ("Ancara", "TUR"),
    "Göztepe": ("Esmirna", "TUR"), "Karşıyaka": ("Esmirna", "TUR"), "Altay": ("Esmirna", "TUR"),
    "İzmirspor": ("Esmirna", "TUR"), "Altınordu": ("Esmirna", "TUR"), "Bucaspor": ("Esmirna", "TUR"),
    "Vefa": ("Istambul", "TUR"), "Adalet": ("Istambul", "TUR"), "Karagümrük": ("Istambul", "TUR"),
    "Beykoz": ("Istambul", "TUR"), "İstanbulspor": ("Istambul", "TUR"), "Feriköy": ("Istambul", "TUR"),
    "Kasımpaşa": ("Istambul", "TUR"), "Yeşildirek": ("Istambul", "TUR"), "Beyoğluspor": ("Istambul", "TUR"),
    "Sarıyer": ("Istambul", "TUR"), "Zeytinburnuspor": ("Istambul", "TUR"), "Bakırköyspor": ("Istambul", "TUR"),
    "İstanbul Başakşehir": ("Istambul", "TUR"), "Ümraniyespor": ("Istambul", "TUR"), "Pendikspor": ("Istambul", "TUR"),
    "Eyüpspor": ("Istambul", "TUR"), "Adana Demirspor": ("Adana", "TUR"), "Adanaspor": ("Adana", "TUR"),
    "Eskişehirspor": ("Eskişehir", "TUR"), "Mersin İdmanyurdu": ("Mersin", "TUR"), "Bursaspor": ("Bursa", "TUR"),
    "Samsunspor": ("Samsun", "TUR"), "Boluspor": ("Bolu", "TUR"), "Giresunspor": ("Giresun", "TUR"),
    "Kayserispor": ("Kayseri", "TUR"), "Kayseri Erciyesspor": ("Kayseri", "TUR"), "Zonguldakspor": ("Zonguldak", "TUR"),
    "Orduspor": ("Ordu", "TUR"), "Balıkesirspor": ("Balıkesir", "TUR"), "Diyarbakırspor": ("Diyarbakır", "TUR"),
    "Çaykur Rizespor": ("Rize", "TUR"), "Gaziantepspor": ("Gaziantep", "TUR"), "Kocaelispor": ("İzmit", "TUR"),
    "Sakaryaspor": ("Adapazarı", "TUR"), "Antalyaspor": ("Antália", "TUR"), "Denizlispor": ("Denizli", "TUR"),
    "Malatyaspor": ("Malatya", "TUR"), "Kahramanmaraşspor": ("Kahramanmaraş", "TUR"), "Konyaspor": ("Kônia", "TUR"),
    "Aydınspor": ("Aydın", "TUR"), "Karabükspor": ("Karabük", "TUR"), "Vanspor": ("Van", "TUR"),
    "Dardanelspor": ("Çanakkale", "TUR"), "Erzurumspor": ("Erzurum", "TUR"), "Yozgatspor": ("Yozgat", "TUR"),
    "Siirtspor": ("Siirt", "TUR"), "Elazığspor": ("Elazığ", "TUR"), "Akçaabat Sebatspor": ("Akçaabat", "TUR"),
    "Sivasspor": ("Sivas", "TUR"), "Manisaspor": ("Manisa", "TUR"), "Akhisarspor": ("Akhisar", "TUR"),
    "Alanyaspor": ("Alanya", "TUR"), "Yeni Malatyaspor": ("Malatya", "TUR"), "BB Erzurumspor": ("Erzurum", "TUR"),
    "Gaziantep FK": ("Gaziantep", "TUR"), "Hatayspor": ("Antioquia", "TUR"), "Bodrum FK": ("Bodrum", "TUR"),
    "MKE Kırıkkalespor": ("Kırıkkale", "TUR"), "Amedspor": ("Diyarbakır", "TUR"), "Çorum FK": ("Çorum", "TUR"),
}

OGOL: dict[str, str] = {
    "36840": "Ankara Demirspor", "galatasaray": "Galatasaray", "1107": "Gençlerbirliği", "82827": "Adalet",
    "fenerbahce": "Fenerbahçe", "5355": "Altay", "besiktas": "Beşiktaş", "2149": "İstanbulspor", "8698": "Hacettepe",
    "9049": "Hacettepe", "73993": "Vefa", "84935": "Karagümrük", "8703": "Karşıyaka", "9050": "Göztepe",
    "108826": "Feriköy", "8695": "Kasımpaşa", "36912": "Altınordu", "78490": "Şekerspor", "105641": "Şekerspor",
    "8694": "Türk Telekomspor", "999999": "Türk Telekomspor", "25814": "Adana Demirspor", "85590": "Yeşildirek",
    "358789": "Yeşildirek", "109756": "Beyoğluspor", "2150": "Ankaragücü", "96409": "Ankaraspor",
    "101245": "Eskişehirspor", "8699": "Eskişehirspor", "10840": "Mersin İdmanyurdu", "2154": "Bursaspor",
    "2148": "Samsunspor", "9070": "Boluspor", "2155": "Adanaspor", "9919": "Giresunspor", "96412": "Zonguldakspor",
    "trabzonspor": "Trabzonspor", "8696": "Orduspor", "37057": "Balıkesirspor", "2147": "Diyarbakırspor",
    "86717": "Çaykur Rizespor", "1113": "Gaziantepspor", "3875": "Kocaelispor", "4183": "Sakaryaspor",
    "7882": "Antalyaspor", "37029": "Sarıyer", "2146": "Denizlispor", "1127": "Malatyaspor",
    "37200": "Kahramanmaraşspor", "konyaspor": "Konyaspor", "26359": "Zeytinburnuspor", "37035": "Bakırköyspor",
    "8733": "Aydınspor", "6010": "Kayseri Erciyesspor", "12221": "Karabükspor", "250744": "Vanspor", "61252": "Vanspor",
    "61952": "Petrol Ofisi", "9077": "Dardanelspor", "8947": "Erzurumspor", "6198": "Yozgatspor", "37039": "Siirtspor",
    "2156": "Elazığspor", "4180": "Akçaabat Sebatspor", "sivasspor": "Sivasspor", "5739": "Manisaspor",
    "basaksehir": "İstanbul Başakşehir", "31028": "Bucaspor", "37060": "Akhisarspor", "alanyaspor": "Alanyaspor",
    "53464": "Yeni Malatyaspor", "81741": "BB Erzurumspor", "8697": "Gaziantep FK", "52102": "Hatayspor",
    "66817": "Ümraniyespor", "27771": "Pendikspor", "24502": "Eyüpspor", "105310": "Bodrum FK", "105430": "Amedspor",
    "81400": "Çorum FK",
}

OGOL_POR_ANO: dict[str, list[tuple[int, int, str]]] = {
    # o ogol põe o MKE Kırıkkalespor de 1978/79 no código do Ankaragücü (o Ankaragücü estava na 2ª divisão)
    "41246": [(1958, 1977, "Ankaragücü"), (1978, 1978, "MKE Kırıkkalespor"), (1979, 9999, "Ankaragücü")],
    # o Kayserispor de 1966 até 2004 (hoje Kayseri Erciyesspor) e o de 2004 em diante (antigo Erciyesspor)
    "4181": [(1958, 2003, "Kayseri Erciyesspor"), (2004, 9999, "Kayserispor")],
    # Şekerspor (Beypazarı) até os anos 1990; Ankaraspor (outro clube, de 1978) de 2004 em diante
    "4182": [(1958, 1999, "Şekerspor"), (2000, 9999, "Ankaraspor")],
    # 1964/65: o ogol troca os códigos do İzmirspor e do Beykoz (os números de cada um estão no código do outro)
    "9051": [(1958, 1963, "İzmirspor"), (1964, 1964, "Beykoz"), (1965, 9999, "İzmirspor")],
    "81504": [(1958, 1963, "Beykoz"), (1964, 1964, "İzmirspor"), (1965, 9999, "Beykoz")],
}

ALIASES: dict[str, str] = {
    # RSSSF (nome + cidade)
    "Galatasaray Istanbul": "Galatasaray", "Fenerbahçe Istanbul": "Fenerbahçe", "Beşiktaş Istanbul": "Beşiktaş",
    "Ankara Gençlerbirliği": "Gençlerbirliği", "Adalet Istanbul": "Adalet", "Vefa Istanbul": "Vefa",
    "Karagümrük Istanbul": "Karagümrük", "Karşıyaka İzmir": "Karşıyaka", "Göztepe İzmir": "Göztepe",
    "Altay İzmir": "Altay", "Beykoz Istanbul": "Beykoz", "Istanbulspor": "İstanbulspor", "Hacettepe Ankara": "Hacettepe",
    "Feriköy Istanbul": "Feriköy", "Kasımpaşa Istanbul": "Kasımpaşa", "Altınordu İzmir": "Altınordu",
    "Şeker Hilal Ankara": "Şekerspor", "PTT Ankara": "Türk Telekomspor", "Yeşildirek Istanbul": "Yeşildirek",
    "Beyoğluspor Istanbul": "Beyoğluspor", "Şekerspor Ankara": "Şekerspor", "Mersin İdmanyurdu": "Mersin İdmanyurdu",
    "Kırıkkalespor": "MKE Kırıkkalespor", "Rizespor": "Çaykur Rizespor", "Kocaelispor İzmit": "Kocaelispor",
    "Sakaryaspor Adapazarı": "Sakaryaspor", "Sarıyer Istanbul": "Sarıyer", "Kahraman Maraşspor": "Kahramanmaraşspor",
    "Zeytinburnu Istanbul": "Zeytinburnuspor", "Bakırköyspor Istanbul": "Bakırköyspor", "DÇ Karabükspor": "Karabükspor",
    "Petrol Ofisi Ankara": "Petrol Ofisi", "Çanakkale Dardanelspor": "Dardanelspor",
    # Wikipédia
    "Fatih Karagümrük": "Karagümrük", "Göztepe A.Ş.": "Göztepe", "MKE Ankaragücü": "Ankaragücü",
    "Hacettepe Spor": "Hacettepe", "Gençlerbirliği OFTAŞ": "Hacettepe", "Altınordu A.Ş.": "Altınordu",
    "Şeker Hilal": "Şekerspor", "Şekerhilâl": "Şekerspor", "PTT": "Türk Telekomspor", "Yesildirek": "Yeşildirek",
    "Beyoğlu": "Beyoğluspor", "Beypazarı Şekerspor": "Şekerspor", "Mersin İdman Yurdu": "Mersin İdmanyurdu",
    "Kahramanmaraşspor A.Ş.": "Kahramanmaraşspor", "Kardemir Karabükspor": "Karabükspor",
    "Siirt Jet-PA Spor": "Siirtspor", "Yimpaş Yozgatspor": "Yozgatspor", "Vestel Manisaspor": "Manisaspor",
    "İstanbul B.B.": "İstanbul Başakşehir", "Başakşehir": "İstanbul Başakşehir", "Akhisar Belediyespor": "Akhisarspor",
    "Osmanlıspor": "Ankaraspor", "Erzurum BB": "BB Erzurumspor", "Bodrum": "Bodrum FK",
    # football-data e engsoccerdata
    "A. Sebatspor": "Akçaabat Sebatspor", "Ad. Demirspor": "Adana Demirspor", "Ankaragucu": "Ankaragücü",
    "Antalya": "Antalyaspor", "Besiktas": "Beşiktaş", "Bodrumspor": "Bodrum FK", "Buyuksehyr": "İstanbul Başakşehir",
    "Diyarbakirspor": "Diyarbakırspor", "Elazigspor": "Elazığspor", "Erciyesspor": "Kayseri Erciyesspor",
    "Eskisehirspor": "Eskişehirspor", "Eyupspor": "Eyüpspor", "Fenerbahce": "Fenerbahçe",
    "Gaziantep": "Gaziantep FK", "Genclerbirligi": "Gençlerbirliği", "Goztep": "Göztepe", "Hacettepespor": "Hacettepe",
    "Karabukspor": "Karabükspor", "Karagumruk": "Karagümrük", "Karagumruk SK": "Karagümrük", "Karsiyaka": "Karşıyaka",
    "Kasimpasa": "Kasımpaşa", "Kayseri": "Kayseri Erciyesspor", "Mersin Idman Yurdu": "Mersin İdmanyurdu",
    "Oftasspor": "Hacettepe", "Osmanlispor": "Ankaraspor", "P. Ofisi": "Petrol Ofisi", "Sariyer": "Sarıyer",
    "Sekerspor": "Şekerspor", "Siirt Jet-PA": "Siirtspor", "Umraniyespor": "Ümraniyespor", "Zeytinburnu": "Zeytinburnuspor",
    "Balikesirspor": "Balıkesirspor", "Gençlerbirligi": "Gençlerbirliği",
    # ESPN e ogol
    "Istanbul Basaksehir": "İstanbul Başakşehir", "Caykur Rizespor": "Çaykur Rizespor", "Goztepe": "Göztepe",
    "Istanbulspor AS": "İstanbulspor", "Kasimpasa SK": "Kasımpaşa", "Fatih Karagumruk": "Karagümrük",
}

# nomes que dependem da época: [(ano inicial, ano final, chave)]
POR_ANO: dict[str, list[tuple[int, int, str]]] = {
    "Kayserispor": [(1958, 2003, "Kayseri Erciyesspor"), (2004, 9999, "Kayserispor")],
    "Erzurumspor": [(1958, 2004, "Erzurumspor"), (2005, 9999, "BB Erzurumspor")],
    "Erzurum": [(1958, 2004, "Erzurumspor"), (2005, 9999, "BB Erzurumspor")],
    "Ankaraspor": [(1958, 1999, "Şekerspor"), (2000, 9999, "Ankaraspor")],
}


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.replace("ı", "i").replace("İ", "I")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s.replace("&", "and"))


_INDICE: dict[str, str] = {chave(k): k for k in CLUBES}
_INDICE.update({chave(k): v for k, v in ALIASES.items()})
_POR_ANO = {chave(k): v for k, v in POR_ANO.items()}


def esd(nome: str, ano: int | None = None) -> str | None:
    """Nome de qualquer fonte -> chave (None se não conhecer). `ano` (início da temporada) resolve os nomes que dependem
    da época."""
    nome = re.sub(r"\s+", " ", nome.replace("&nbsp;", " ").replace("\xa0", " ").strip().rstrip("*").strip())
    nome = re.sub(r"\s*\((?:[CLN](?:,\s*[CLN])*)\)$", "", nome)
    k = chave(nome)
    if k in _POR_ANO:
        return next((c for ini, fim, c in _POR_ANO[k] if ano is not None and ini <= ano <= fim), None)
    return _INDICE.get(k)


def ogol(codigo: str, ano: int | None = None) -> str | None:
    if codigo in OGOL_POR_ANO:
        return next((c for ini, fim, c in OGOL_POR_ANO[codigo] if ano is not None and ini <= ano <= fim), None)
    return OGOL.get(codigo)


def exibicao(chave_clube: str) -> str:
    return chave_clube
