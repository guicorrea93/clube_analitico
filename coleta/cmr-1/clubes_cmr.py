"""Identidade dos clubes camaroneses: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido, com a cidade quando é o costume ("Canon Yaoundé", "Coton Sport", "Union Douala");
- nome que já existe em outro país leva o país ("Botafogo (Camarões)", "Santos (Camarões)");
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - Union Douala = Union Sportive de Douala; Tonnerre Yaoundé = Tonnerre Kalara Club; Coton Sport = Cotonsport de
    Garoua; Panthère du Ndé = Panthère de Bangangté; Unisport du Haut-Nkam = Unisport de Bafang; University FC de
    Ngaoundéré = Université de Ngaoundéré; Djiko FC = Feutcheu FC ("Feutcheu FC were renamed Djiko FC"); Olympic
    Mvolyé = Olympic de Mvolyé; PWD Bamenda = PWD Cammark Bamenda;
  - Aigle Royal são dois clubes: o do Moungo (Nkongsamba, campeão de 1970/71 e 1994) e o da Menoua (Dschang); "Aigle"
    sozinho até 2004 é o de Nkongsamba; de 2005 a 2023, o de Dschang (a lista de clubes de 2007/08 confirma).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-africa"))
from rsssf_africa import chave  # noqa: E402

YAO = ("Yaoundé", "Centro")
DLA = ("Douala", "Litoral")
GAR = ("Garoua", "Norte")
NGA = ("Ngaoundéré", "Adamaoua")
OES = "Oeste"
NO = "Noroeste"
SO = "Sudoeste"

# nome de exibição -> regex (sobre a chave do nome), cidade e região, primeiro e último ano
_DADOS: list[tuple[str, str, tuple[str, str], int, int]] = [
    ("Coton Sport", r"coton ?sport( fc)?( de)?( garoua)?$|^coton$", GAR, 1960, 2100),
    ("Canon Yaoundé", r"canon( sporti(f|ve))?( de)?( yaounde)?$", YAO, 1960, 2100),
    ("Union Douala", r"union( sporti(f|ve))?( de)?( douala)?$|^us douala$", DLA, 1960, 2100),
    ("Tonnerre Yaoundé", r"tonner+e( kalara)?( club)?( de)?( yaounde)?$", YAO, 1960, 2100),
    ("Oryx Douala", r"oryx( douala)?$", DLA, 1960, 2100),
    ("Caïman Douala", r"caiman( de)?( douala)?$", DLA, 1960, 2100),
    ("Léopard Douala", r"leopards?( de)?( douala)?$", DLA, 1960, 2100),
    ("Diamant Yaoundé", r"diamant( de)?( yaounde)?$", YAO, 1960, 2100),
    ("Racing Bafoussam", r"racing( f)?( club)?( fc)?( de)?( bafoussam)?$", ("Bafoussam", OES), 1960, 2100),
    ("Aigle Royal de la Menoua", r"(as )?aigle( royal| r)?( de la)? menoua$|aigle( royal)? dschang$|eagle royale? casamba$", ("Dschang", OES), 1960, 2100),
    ("Aigle Royal du Moungo", r"aigle( royal| r)?( du)? moungo$|aigle( royal)?( de)? n ?kongsamba$", ("Nkongsamba", "Litoral"), 1960, 2100),
    ("Aigle Royal du Moungo", r"aigle( royal)?$", ("Nkongsamba", "Litoral"), 1960, 2004),
    ("Aigle Royal de la Menoua", r"aigle( royal)?$", ("Dschang", OES), 2005, 2023),
    ("Dynamo Douala", r"(dynamo|din)( de)?( douala)?$", DLA, 1960, 2100),
    ("PWD Bamenda", r"pwd( cammark| social club)?( de)?( bamenda)?$|fc bamenda$", ("Bamenda", NO), 1960, 2100),
    ("PWD Kumba", r"pwd( cammark)?( de)? kumba$", ("Kumba", SO), 1960, 2100),
    ("Cammark Bamenda", r"cam+ark( bamenda)?$", ("Bamenda", NO), 1960, 2100),
    ("Panthère du Ndé", r"panth[ae]re( du nde)?( de)?( bang[a]n?g?t?g?e)?$", ("Bangangté", OES), 1960, 2100),
    ("Unisport du Haut-Nkam", r"unisport( fc)?( du haut nkam| de)?( bafang)?$", ("Bafang", OES), 1960, 2100),
    ("Fovu Baham", r"fovu( club)?( de)?( baham)?$", ("Baham", OES), 1960, 2100),
    ("Sable Batié", r"sable( fc)?( de)?( batie)?$", ("Batié", OES), 1960, 2100),
    ("Stade Bandjoun", r"stade( b[a]?n?djoun)?$|^bandjoun$", ("Bandjoun", OES), 1960, 2100),
    ("Bamboutos Mbouda", r"bamboutos( fc)?( de)?( mbouda)?$", ("Mbouda", OES), 1960, 2100),
    ("Colombe Sportive", r"colombe( sportive)?( du dja et lobo| sangmel[ie]na)?$", ("Sangmélima", "Sul"), 1960, 2100),
    ("Prévoyance Yaoundé", r"prevoyance( fc)?( de)?( yaounde)?$", YAO, 1960, 2100),
    ("Olympic Mvolyé", r"olympics?( mvolye)?$|^mvolye$", YAO, 1960, 2100),
    ("Victoria United", r"victoria( u| united)?( de)?( limbe)?$", ("Limbe", SO), 1960, 2100),
    ("Mount Cameroon", r"(mo?u?n?t|mnt) camero(o|u)n( fc)?( de)?( buea)?$", ("Buea", SO), 1960, 2100),
    ("Kumbo Strikers", r"kumbo( strikers)?$", ("Kumbo", NO), 1960, 2100),
    ("Tiko United", r"tiko( united)?$", ("Tiko", SO), 1960, 2100),
    ("Girondins Ngaoundéré", r"girondins( ngaoundere)?$", NGA, 1960, 2100),
    ("Port FC Douala", r"ports?( fc)?( douala)?$", DLA, 1960, 2100),
    ("Espérance Guider", r"esperance( fc)?( de)?( guider)?$", ("Guider", "Norte"), 1960, 2100),
    ("Cintra Yaoundé", r"cintra( de)?( yaounde)?$", YAO, 1960, 2100),
    ("Kadji Sport Academy", r"ksa( douala)?$|kadji sport academy( de douala)?$", DLA, 1960, 2100),
    ("Les Astres", r"(les )?astres( fc)?( de)?( douala)?$", DLA, 1960, 2100),
    ("Sahel Maroua", r"sahel( fc)?( de)?( maroua)?$", ("Maroua", "Extremo Norte"), 1960, 2100),
    ("Foudre Akonolinga", r"foudre( sportive)?( d)?( ?akonolinga)?$", ("Akonolinga", "Centro"), 1960, 2100),
    ("Fédéral du Noun", r"federal( sporting club du noun| foumban)?$", ("Foumban", OES), 1960, 2100),
    ("University FC Ngaoundéré", r"universit(e|y)( fc)?( de)?( ngaoundere| nagoundere)?( fc)?$|^n(a)?g?a?oundere$", NGA, 1960, 2100),
    ("Impôts FC", r"impots( fc)?( de)?( yaounde)?$", YAO, 1960, 2100),
    ("AS Cetef", r"as cetef", DLA, 1960, 2100),
    ("CPS Bertoua", r"cps( de)? bertoua$|^cpsb$", ("Bertoua", "Leste"), 1960, 2100),
    ("Inter Lion Ngoma", r"(fc )?inter(national)? lion ngoma|^lion ngoma$", ("Ebolowa", "Sul"), 1960, 2100),
    ("AS Matelots", r"(as )?matelots$", DLA, 1960, 2100),
    ("Danay FC", r"danay", ("Yagoua", "Extremo Norte"), 1960, 2100),
    ("Roumdé Adjia", r"roumde adjia", GAR, 1960, 2100),
    ("AS Lausanne", r"lausanne", YAO, 1960, 2100),
    ("Renaissance Ngoumou", r"(fc )?renaissance( fc)?( de)?( ngoumou| ng)?$", ("Ngoumou", "Centro"), 1960, 2100),
    ("New Star Douala", r"new star", DLA, 1960, 2100),
    ("Njalla Quan", r"njalla quan|nqsa$", ("Limbe", SO), 1960, 2100),
    ("YOSA Bamenda", r"yosa( bamenda)?$|yo?u?ng sports academy", ("Bamenda", NO), 1960, 2100),
    ("Douala AC", r"douala (ac|athletic club)", DLA, 1960, 2100),
    ("Scorpion Bey", r"scorpion( fc)?( de)?( bey| be)?$", ("Bey", "Norte"), 1960, 2100),
    ("APEJES Academy", r"apejes", ("Mfou", "Centro"), 1960, 2100),
    ("Cosmos Bafia", r"cosmos( fa| de)?( bafia)?$", ("Bafia", "Centro"), 1960, 2100),
    ("Botafogo (Camarões)", r"botafogo", DLA, 1960, 2100),
    ("Lion Blessé", r"lion blesse", ("Fotouni", OES), 1960, 2100),
    ("Dragon Yaoundé", r"dragon( fc| club)?( yaounde)?$", YAO, 1960, 2100),
    ("UMS de Loum", r"ums( de loum)?$", ("Loum", "Litoral"), 1960, 2100),
    ("Eding Sport", r"eding sport", ("Mfou", "Centro"), 1960, 2100),
    ("Stade Renard", r"stade renard", ("Melong", "Litoral"), 1960, 2100),
    ("Yaoundé II FC", r"yaounde ii|yafoot$", YAO, 1960, 2100),
    ("AS Fortuna", r"(as )?fortuna", ("Mfou", "Centro"), 1960, 2100),
    ("Avion du Nkam", r"avion", ("Douala", "Litoral"), 1960, 2100),
    ("Djiko FC", r"djiko|feutcheu", ("Bandjoun", OES), 1960, 2100),
    ("Fauve Azur", r"fauve azur", YAO, 1960, 2100),
    ("Gazelle FA", r"gazelle", GAR, 1960, 2100),
    ("Ofta Kribi", r"ofta", ("Kribi", "Sul"), 1960, 2100),
    ("Entente Ngaoundéré", r"entente( ngaoundere)?$", NGA, 1960, 2100),
    ("Etoile Filante Garoua", r"etoile filante", GAR, 1960, 2100),
    ("Lion Yaoundé", r"lion yaounde", YAO, 1960, 2100),
    ("Kohi Sport Maroua", r"kohi( sport)?( de)? maroua$", ("Maroua", "Extremo Norte"), 1960, 2100),
    ("Dihep di Nkam", r"dihep di nkam", ("Yabassi", "Litoral"), 1960, 2100),
    ("Rail Douala", r"rail douala", DLA, 1960, 2100),
    ("Unité Douala", r"unite douala", DLA, 1960, 2100),
    ("Santos (Camarões)", r"santos( yaounde)?$", YAO, 1960, 2100),
    ("Elecsport Limbé", r"elecsport", ("Limbe", SO), 1960, 2100),
    ("Maiscam Ngaoundéré", r"maiscam", NGA, 1960, 2100),
    ("Avenir Douala", r"avenir douala", DLA, 1960, 2100),
    ("Djerem Bertoua", r"djerem", ("Bertoua", "Leste"), 1960, 2100),
    ("Free Boys Bamenda", r"free boys", ("Bamenda", NO), 1960, 2100),
    ("Vautour Dschang", r"vautour( de)? dschang", ("Dschang", OES), 1960, 2100),
    ("Océan Kribi", r"ocean( de)? kribi", ("Kribi", "Sul"), 1960, 2100),
    ("Fogabe Yaoundé", r"fogabe", YAO, 1960, 2100),
    ("Union Abong-Mbang", r"(us |union( s)?( d)? ?)abong mbang$", ("Abong-Mbang", "Leste"), 1960, 2100),
    ("AS Mairie de Yaoundé", r"as de la mairie|asmy( 1er)?$", YAO, 1960, 2100),
]

CLUBES: dict[str, tuple[str, str]] = {nome: lugar for nome, _, lugar, _, _ in _DADOS}
REGRAS: list[tuple[str, str, int, int]] = [(rx, nome, a0, a1) for nome, rx, _, a0, a1 in _DADOS]


def _regra(k: str, ano: int) -> str | None:
    for rx, exib, a0, a1 in REGRAS:
        if a0 <= ano <= a1 and re.match(rx + r"(?:\b|$)", k):
            return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido)."""
    if not nome:
        return None
    nome = re.sub(r"\((Moungo|Menoua)\)", r"\1", nome)   # "Aigle Royal (Moungo)": o parêntese diz qual Aigle
    nome = re.sub(r"\s*\((\d+ ag|[^)]*)\)\s*$", lambda m: "" if "ag" in m.group(1) else "", nome)   # "(Garoua)"
    nome = re.sub(r"[*]+$", "", nome).strip()
    nome = re.sub(r"\s+(FC|SC)$", "", nome)
    k = chave(nome)
    if cidade:
        if (r := _regra(chave(f"{nome} {cidade}"), ano)):
            return r
    return _regra(k, ano)
