"""Identidade dos clubes argelinos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4) e do recado do agente 1:
- nome pelo qual o clube é conhecido, com a sigla francesa ("MC Alger", "USM Alger", "JS Kabylie", "ES Sétif");
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte. As tabelas da RSSSF
  trazem o nome atual e o da época entre colchetes ("[as Mouloudia Pétroliers d'Alger]"); os da reforma esportiva de
  1977 (nomes de empresas estatais) voltaram aos antigos por volta de 1989:
  - MC Alger = MP Alger; MC Oran = MP Oran; CR Belouizdad = CR Belcourt = CM Belcourt; JS Kabylie = JS Kawkabi = JE (JET)
    Tizi Ouzou; ES Sétif = EP Sétif; USM Alger = USK Alger; NA Hussein Dey = NAA Hussein Dey = MA Hussein Dey;
    RC Kouba = CCS (CSS) Kouba = RS Kouba; USM El Harrach = USM Maison-Carrée; CS Constantine = CM Constantine;
  - ASO Chlef = AS Orléansville (1962-64) = ASTO El Asnam = DNC Asnam = Chlef SO = CSO Chlef (a cidade mudou de nome);
  - RC Kouba é o "NAR Alger" (Naphte Riadhi Alger) dos jogos de 1972/73; ES Sétif é o "WR Sétif" de 1971/72 e 1972/73
    (a tabela dá ES Sétif e nenhum WR Sétif); o "IRB Relizane" dos jogos de 1985/86 é o RCM Relizane da tabela;
  - ASM Oran = ASC Oran; CA Batna = CN Batna; ES Guelma = ESM Guelma; GC Mascara = GCR Mascara; WA Boufarik = WO Boufarik;
    WA Tlemcen = WM Tlemcen; USM Bel-Abbès = ESM Bel-Abbès; USM Aïn Beïda = ISM Aïn Beïda; RC Relizane = RCM Relizane;
    MC Saïda = MB Saïda; AS Aïn M'lila = AM Aïn M'lila; WKF Collo = Entente Collo; OMR El Annasser = OM Ruisseau;
  - DNC Alger = OC Alger = CS DNC Alger = JH Djazaïr (1985: "JH Djazaïr aka DNC Alger"): o nome mais usado;
  - o USM Annaba dos anos 1960 e 1970 é o atual Hamra Annaba ("Team founded in 1944 now known as HAMR Annaba. Not to be
    confused with the current USM Annaba ... founded in 1983"): até 1979 é "Hamra Annaba".

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-africa"))
from rsssf_africa import chave  # noqa: E402

ALG = ("Argel", "Argel")
ORA = ("Orã", "Orã")
CON = ("Constantine", "Constantine")
SET = ("Sétif", "Sétif")
BEJ = ("Béjaïa", "Béjaïa")
OEB = "Oum El Bouaghi"

# nome de exibição -> (cidade, província)
CLUBES: dict[str, tuple[str, str]] = {
    "MC Alger": ALG, "USM Alger": ALG, "CR Belouizdad": ALG, "NA Hussein Dey": ("Hussein Dey", "Argel"),
    "RC Kouba": ("Kouba", "Argel"), "USM El Harrach": ("El Harrach", "Argel"), "DNC Alger": ALG,
    "Paradou AC": ("Hydra", "Argel"), "OMR El Annasser": ALG, "ES Ben Aknoun": ("Ben Aknoun", "Argel"),
    "ASPTT Alger": ALG, "OM Saint-Eugène": ("Bologhine", "Argel"), "Stade Guyotville": ("Aïn Benian", "Argel"),
    "JS El Biar": ("El Biar", "Argel"),
    "MC Oran": ORA, "ASM Oran": ORA, "SCM Oran": ORA, "RCG Oran": ORA, "RC Oran": ORA, "EM Oran": ORA, "RC Cité Petit": ORA,
    "CA Planteurs": ORA, "OM Arzew": ("Arzew", "Orã"),
    "CS Constantine": CON, "MO Constantine": CON, "USH Constantine": CON, "AS Khroub": ("El Khroub", "Constantine"),
    "ES Sétif": SET, "USM Sétif": SET, "MC El Eulma": ("El Eulma", "Sétif"),
    "JS Kabylie": ("Tizi Ouzou", "Tizi Ouzou"), "JS Bordj Ménaïel": ("Bordj Ménaïel", "Boumerdès"),
    "USM Blida": ("Blida", "Blida"), "WA Boufarik": ("Boufarik", "Blida"), "RC Arbaâ": ("Larbaâ", "Blida"),
    "IRB Hadjout": ("Hadjout", "Tipaza"), "USM Marengo": ("Hadjout", "Tipaza"),
    "ASO Chlef": ("Chlef", "Chlef"), "RC Relizane": ("Relizane", "Relizane"), "Olympique Médéa": ("Médéa", "Médéa"),
    "ES Sour El Ghozlane": ("Sour El Ghozlane", "Bouira"),
    "JSM Béjaïa": BEJ, "MO Béjaïa": BEJ, "USM Béjaïa": BEJ, "Olympique Akbou": ("Akbou", "Béjaïa"),
    "USM Annaba": ("Annaba", "Annaba"), "Hamra Annaba": ("Annaba", "Annaba"), "ES Guelma": ("Guelma", "Guelma"),
    "JSM Skikda": ("Skikda", "Skikda"), "WKF Collo": ("Collo", "Skikda"), "JS Djijel": ("Jijel", "Jijel"),
    "CA Batna": ("Batna", "Batna"), "MSP Batna": ("Batna", "Batna"), "US Biskra": ("Biskra", "Biskra"),
    "USM Khenchela": ("Khenchela", "Khenchela"), "JSM Tébessa": ("Tébessa", "Tébessa"),
    "US Chaouia": (OEB, OEB), "AS Aïn M'lila": ("Aïn M'lila", OEB), "USM Aïn Beïda": ("Aïn Beïda", OEB),
    "CRB Aïn Fakroun": ("Aïn Fakroun", OEB),
    "HB Chelghoum Laïd": ("Chelghoum Laïd", "Mila"), "DRB Tadjenant": ("Tadjenant", "Mila"),
    "CA Bordj Bou Arréridj": ("Bordj Bou Arréridj", "Bordj Bou Arréridj"), "NC Magra": ("Magra", "M'Sila"),
    "USM Bel-Abbès": ("Sidi Bel Abbès", "Sidi Bel Abbès"), "WA Tlemcen": ("Tlemcen", "Tlemcen"),
    "GC Mascara": ("Mascara", "Mascara"), "SA Mohammadia": ("Mohammadia", "Mascara"),
    "SC Perrégaux": ("Mohammadia", "Mascara"), "GS Perrégaux": ("Mohammadia", "Mascara"), "CC Sig": ("Sig", "Mascara"),
    "MC Saïda": ("Saïda", "Saïda"), "JSM Tiaret": ("Tiaret", "Tiaret"), "ES Mostaganem": ("Mostaganem", "Mostaganem"),
    "WA Mostaganem": ("Mostaganem", "Mostaganem"), "CR Témouchent": ("Aïn Témouchent", "Aïn Témouchent"),
    "JS Saoura": ("Méridja", "Béchar"), "MC El Bayadh": ("El Bayadh", "El Bayadh"),
    "MB Rouissat": ("Rouissat", "Ouargla"), "US Souf": ("El Oued", "El Oued"), "IR Saha": ("", ""),
}

REGRAS: list[tuple[str, str, int, int]] = [
    (r"(mc|mp|m) alager|(mc|mp) alger|mouloudia( (chaabia|club|petroliers))? d ?alger", "MC Alger", 1962, 2100),
    (r"(mc|mp) oran(ran| 1)?$|^m oran$|mouloudia( (chaabia|club|petroliers))? d ?oran", "MC Oran", 1962, 2100),
    (r"(cr|cm|chabab) (belcourt|beouizdad|belouizd[ae]d)|cmbelcourt|chabab riadhi( de)? belouizdad", "CR Belouizdad", 1962, 2100),
    (r"(js|jet|je|jsk) (kabylie|kaylie|kawkabi|tizi ouzou)|^s kabylie|jeunesse sportive de kabylie", "JS Kabylie", 1962, 2100),
    (r"(es|ep|wr) setif|entente( sportive)?( de)? setif", "ES Sétif", 1962, 2100),
    (r"(usm|usk) alger|union sportive madinet d ?alger", "USM Alger", 1962, 2100),
    (r"(na|naa|ma) hus+ein dey|nahd$|nasr athletic de hussein dey", "NA Hussein Dey", 1962, 2100),
    (r"(rc|rs|ccs|css) kouba|nar alger", "RC Kouba", 1962, 2100),
    (r"usm (el |e )?harra(ch|h)|usmh$|usm maison carree", "USM El Harrach", 1962, 2100),
    (r"(aso|cso) chlef|asto el as[nb]am|asnam sto|el asnam [st]o|chlef s ?o$|dnc asnam|as orleansville|a chlef$|"
     r"association sportive olympique de chlef", "ASO Chlef", 1962, 2100),
    (r"as[mc] oran(ran)?$|association sportive madinet d ?oran", "ASM Oran", 1962, 2100),
    (r"(cs|cm) constan?ti(ne|n|nois)$|club sportif de constantine", "CS Constantine", 1962, 2100),
    (r"mo (constantine|cosntantine|costantine)", "MO Constantine", 1962, 2100),
    (r"ush constantine", "USH Constantine", 1962, 2100),
    (r"usm (sidi )?bel ?abbes|esm (sidi )?bel ?abb[ea]s|u bel abbes", "USM Bel-Abbès", 1962, 2100),
    (r"(wa|wm) tlemce[nm]|wm tlemcenlemcen|widad athletic de tlemcen", "WA Tlemcen", 1962, 2100),
    (r"usm blida|union sportive madinet de blida", "USM Blida", 1962, 2100),
    (r"(ca|cn) bata?na$|chaba aures de batna", "CA Batna", 1962, 2100),
    (r"msp batna", "MSP Batna", 1962, 2100),
    (r"esm? guelma(uelma)?", "ES Guelma", 1962, 2100),
    (r"gcr? masc?a?ra|ghali club de mascara", "GC Mascara", 1962, 2100),
    (r"w[ao] boufarik", "WA Boufarik", 1962, 2100),
    (r"j[sc]m tiaret", "JSM Tiaret", 1962, 2100),
    (r"usm an+ab+a?$|hamra? annaba|hamr annaba", "Hamra Annaba", 1962, 1979),
    (r"usm an+ab+a?$|u annaba|union sportive madinet de annaba", "USM Annaba", 1980, 2100),
    (r"(as|am|a) a?in mlila|as in mlila", "AS Aïn M'lila", 1962, 2100),
    (r"(usm|ism|u) ain beida|ismba$|union d ?ain beida", "USM Aïn Beïda", 1962, 2100),
    (r"j s? ?bordj men\w*|js bordj men\w*", "JS Bordj Ménaïel", 1962, 2100),
    (r"(rcm?|r|rc rc|irb) relizane", "RC Relizane", 1962, 2100),
    (r"m[cb] saida(aida)?|mouloudia club saida", "MC Saïda", 1962, 2100),
    (r"(wkf|wfk|wk|es) collo|(entente )?collo$", "WKF Collo", 1962, 2100),
    (r"(cs )?dnc algers?|oc alger|jh ?djazair", "DNC Alger", 1962, 2100),
    (r"(ca|cab|cabb)( b| bb| bordj)?( bou)? arr|cab bordj|as bordj bou arreridj|^bordj bou arreridj$|chabab ahly de bordj bou arreridj",
     "CA Bordj Bou Arréridj", 1962, 2100),
    (r"jsm beja[iy]a|jeunesse sportive madinet de bejaia", "JSM Béjaïa", 1962, 2100),
    (r"mo bejaia", "MO Béjaïa", 1962, 2100),
    (r"usm bejaia", "USM Béjaïa", 1962, 2100),
    (r"(us|aso) cha?ouia|union sportive des chaouia", "US Chaouia", 1962, 2100),
    (r"paradou", "Paradou AC", 1962, 2100),
    (r"js saoura", "JS Saoura", 1962, 2100),
    (r"om r(ou|u)is+eau|omr el an+as+er|olympic mostakbel ruisseau", "OMR El Annasser", 1962, 2100),
    (r"usm khenchela", "USM Khenchela", 1962, 2100),
    (r"us biskra|union sportive de biskra", "US Biskra", 1962, 2100),
    (r"mc el eulma", "MC El Eulma", 1962, 2100),
    (r"as (el )?khroub|association sportive khroub", "AS Khroub", 1962, 2100),
    (r"nc magra", "NC Magra", 1962, 2100),
    (r"rc arba+", "RC Arbaâ", 1962, 2100),
    (r"o(lympique|l)? medea", "Olympique Médéa", 1962, 2100),
    (r"(drb )?tadjenane?t", "DRB Tadjenant", 1962, 2100),
    (r"crb ain fakroun", "CRB Aïn Fakroun", 1962, 2100),
    (r"(hb )?chelghoum laid", "HB Chelghoum Laïd", 1962, 2100),
    (r"mc ?e(l)? bayadh", "MC El Bayadh", 1962, 2100),
    (r"(es|ac|us) ben aknoun|^ben aknoun$", "ES Ben Aknoun", 1962, 2100),
    (r"o(lympique)? akbou", "Olympique Akbou", 1962, 2100),
    (r"(mb|olympique) rouissat", "MB Rouissat", 1962, 2100),
    (r"us souf", "US Souf", 1962, 2100),
    (r"jsm skikda", "JSM Skikda", 1962, 2100),
    (r"js dji?d?jel+i?$|js jijel|jijel sd", "JS Djijel", 1962, 2100),
    (r"es mostaganem", "ES Mostaganem", 1962, 2100),
    (r"wa mostaganem", "WA Mostaganem", 1962, 2100),
    (r"sa moha?m+[ae]dia", "SA Mohammadia", 1962, 2100),
    (r"irb hadjout", "IRB Hadjout", 1962, 2100),
    (r"e?s? ?sour (el )?ghozlane", "ES Sour El Ghozlane", 1962, 2100),
    (r"jsm tebessa", "JSM Tébessa", 1962, 2100),
    (r"usm setif", "USM Sétif", 1962, 2100),
    (r"rcg oran", "RCG Oran", 1962, 2100),
    (r"ir saha", "IR Saha", 1962, 2100),
    # ligas regionais de 1962/63 e 1963/64
    (r"om saint eugene", "OM Saint-Eugène", 1962, 1963),
    (r"cr temouchent", "CR Témouchent", 1962, 2100),
    (r"perregaux sc", "SC Perrégaux", 1962, 1963),
    (r"perregau\w* gs", "GS Perrégaux", 1962, 1963),
    (r"rc cite petit", "RC Cité Petit", 1962, 1963),
    (r"scm oran", "SCM Oran", 1962, 2100),
    (r"c[cs] sig", "CC Sig", 1962, 1963),
    (r"em oran", "EM Oran", 1962, 1963),
    (r"om arzew", "OM Arzew", 1962, 1963),
    (r"rc oran", "RC Oran", 1962, 1963),
    (r"asptt alger", "ASPTT Alger", 1962, 1963),
    (r"s ?guyotville|guyotville", "Stade Guyotville", 1962, 1963),
    (r"usm marengo", "USM Marengo", 1962, 1963),
    (r"js el biar", "JS El Biar", 1962, 1963),
    (r"ca planteurs", "CA Planteurs", 1962, 1963),
]


def _regra(k: str, ano: int) -> str | None:
    for rx, exib, a0, a1 in REGRAS:
        if a0 <= ano <= a1 and re.match(rx + r"(?:\b|$)", k):
            return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    if not nome:
        return None
    nome = re.sub(r"\s*\((\d+ ag|[^)]*)\)\s*$", lambda m: "" if "ag" in m.group(1) else "", nome)   # "(Algiers)", "(0 ag)"
    nome = re.sub(r"\s+b\)\s*$", "", nome)
    k = chave(nome)
    if cidade:
        if (r := _regra(chave(f"{nome} {cidade}"), ano)):
            return r
    return _regra(k, ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
