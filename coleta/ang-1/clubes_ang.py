"""Identidade dos clubes angolanos: cada grafia de cada fonte (RSSSF, ogol, Wikipédia) -> um nome de exibição.

- nome pelo qual o clube é conhecido no Brasil, como na memória dos lusófonos: "1º de Agosto", "Petro de Luanda",
  "Benfica de Luanda", "1º de Maio";
- nome que já existe em outro país leva primeiro a cidade ("Benfica de Luanda", "Santos de Luanda") e, sem cidade que
  resolva, o país entre parênteses;
- clubes com data no nome: o leitor troca o número pelo extenso ("Primeiro de Agosto"); a regra casa o extenso e a
  exibição volta ao número ("1º de Agosto", "4 de Abril");
- o mesmo clube com outro nome, na mesma cidade, é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - Petro de Luanda = Atlético Petróleos de Luanda; Petro do Huambo = Atlético Petróleos do Huambo;
  - ASA de Luanda = Atlético Sport Aviação ("ASA" já é o de Arapiraca, do Brasil); Interclube = GD Interclube = Inter Clube Angola;
  - 1º de Maio = Estrela Clube Primeiro de Maio (Benguela); Desportivo da Huíla = Desportivo Militar da Huíla;
  - Atlético do Namibe = Atlético Petróleos do Namibe = Desportivo Sonangol do Namibe (o clube da petrolífera no
    Namibe, rebatizado);
  - Bravos do Maqui = Onze Bravos do Maqui (Luena); Recreativo do Libolo = GD e Recreativo do Libolo (Calulo);
  - Académica do Lobito = Académica Petróleos do Lobito; Académica do Soyo = Académica Petróleos do Kwanda;
  - Sporting de Cabinda = Sporting Clube Petróleos de Cabinda; Kabuscorp = Kabuscorp do Palanca;
  - JGM = JGM/Académica do Huambo; Saneamentos Rangol = Rangol;
  - Santa Rita do Namibe = GD Welwitschia (Moçâmedes; "Born as Santa Rita, later renamed Grupo Desportivo Welwitschia
    and later renamed again Santa Rita", 1979); o Santa Rita de Cássia (Uíge, 2017 em diante) é outro clube;
- "Progresso" sozinho é o do Sambizanga (Luanda), menos onde a tabela diz o da Lunda Sul (2015 a 2017, os dois na
  liga: regra pelo nome completo).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-africa"))
from rsssf_africa import chave  # noqa: E402

LUA = ("Luanda", "Luanda")
BEN = ("Benguela", "Benguela")
HUA = ("Huambo", "Huambo")
LUB = ("Lubango", "Huíla")
CAB = ("Cabinda", "Cabinda")
NAM = ("Moçâmedes", "Namibe")
UIG = ("Uíge", "Uíge")
MAL = ("Malanje", "Malanje")

# nome de exibição -> regex (sobre a chave do nome, com as datas por extenso), cidade e região, primeiro e último ano
_DADOS: list[tuple[str, str, tuple[str, str], int, int]] = [
    ("1º de Agosto", r"(cd |clube desportivo |deportivo )?primeiro( de)? agosto( luanda)?$", LUA, 1900, 2100),
    ("Petro de Luanda", r"petro( atletico)?( de)? luanda$|atletico petroleos( de)? luanda( luanda)?$|petro atletico$",
     LUA, 1900, 2100),
    ("Petro do Huambo", r"petro( atletico)?( do)? huambo$|atletico petroleos do huambo$", HUA, 1900, 2100),
    ("Atlético do Namibe", r"atletico( desportivo)?( do)? namibe$|atletico petroleos do namibe$|petro namibe$|"
     r"(desportivo |deportivo )?sonangol( do| namibe)?( namibe)?$", NAM, 1900, 2100),
    ("ASA de Luanda", r"asa( luanda)?$|(as|atletico sport) aviacao( asa| luanda)?$", LUA, 1900, 2100),
    ("Interclube", r"(gd |grupo desportivo |cd )?inter( ?clube)?( angola)?( de)?( luanda)?$", LUA, 1900, 2100),
    ("Inter da Huíla", r"inter da huila$", LUB, 1900, 2100),
    ("Inter da Lunda Sul", r"inter da lunda sul$", ("Saurimo", "Lunda Sul"), 1900, 2100),
    ("Inter do Namibe", r"inter do namibe$", NAM, 1900, 2100),
    ("1º de Maio", r"((ec|estrela clube) )?primeiro( de)? maio( de)?( benguela)?$", BEN, 1900, 2100),
    ("Sagrada Esperança", r"(gd |grupo desportivo )?sag(rada)?\.? ?esp(eran[cç]?a)?( dundo| lunda norte)?$|"
     r"sagrada esperana$", ("Dundo", "Lunda Norte"), 1900, 2100),
    ("Desportivo da Huíla", r"(clube |c )?(cd |desp |desportivo )(militar )?(da )?huila( lubango)?$|cd huila$", LUB,
     1900, 2100),
    ("Recreativo do Libolo", r"(c recreativo d do |cdr |gdr |gd e recreativo do |rec |recreativo )?(do )?libolo"
     r"( calulo)?$", ("Calulo", "Cuanza Sul"), 1900, 2100),
    ("Recreativo da Caála", r"((c |cr )?rec(reativo)?( da)? )?ca[aá]la( caala)?$|cr caala$", ("Caála", "Huambo"),
     1900, 2100),
    ("Kabuscorp", r"kabuscorp( sc| fc| sport clube)?( do)?( palanca)?( luanda)?$", LUA, 1900, 2100),
    ("Bravos do Maqui", r"((fc|futebol clube) )?(onze |11 )?bravos( do)?( maquis?)?( de moxico)?( luena)?$", ("Luena",
     "Moxico"), 1900, 2100),
    ("Académica do Soyo", r"ac(ad|ademica)?\.? (do )?soyo$|academica( petroleos?)? do kwanda( soyo)?$|"
     r"academica do kwanda( soyo)?$|academica soyo$", ("Soyo", "Zaire"), 1900, 2100),
    ("Académica do Lobito", r"ac(ad|ademica)?\.? ?(do )?lobito$|academica( petroleos( clube)?)?( do)?( lobito)?$",
     ("Lobito", "Benguela"), 1900, 2100),
    ("Benfica de Luanda", r"(sport luanda e )?benfica( de)? luanda( luanda)?$|benfica$|sport luanda e benfica( luanda)?$", LUA, 1900, 2100),
    ("Benfica do Lubango", r"(sport lubango e )?benfica( petroleos)?( do)? lubango( lubango)?$|sport lubango e benfica( lubango)?$", LUB, 1900, 2100),
    ("Benfica do Huambo", r"benfica do huambo$", HUA, 1900, 2100),
    ("Benfica de Cabinda", r"benfica de cabinda$", CAB, 1900, 2100),
    ("Sporting de Cabinda", r"sp(orting)?\.?( clube)?( petroleos)?( de)? cabinda( cabinda)?$|sporting$", CAB, 1900,
     2100),
    ("Sporting do Bié", r"sporting( clube petroleos)?( do)? bie$", ("Cuíto", "Bié"), 1900, 2100),
    ("Sporting de Benguela", r"sporting( de)? benguela$", BEN, 1900, 2100),
    ("Sporting de Luanda", r"sporting de luanda$", LUA, 1900, 2100),
    ("Sporting do Lubango", r"sporting do lubango$", LUB, 1900, 2100),
    ("Progresso da Lunda Sul", r"progresso( associacao)?( da)? lunda sul$", ("Saurimo", "Lunda Sul"), 1900, 2100),
    ("Progresso do Sambizanga", r"progresso( associacao)?( do)?( sambizanga)?( luanda)?$", LUA, 1900, 2100),
    ("Nacional de Benguela", r"nacional( sport clube)?( de)?( benguela)?$", BEN, 1900, 2100),
    ("FC Cabinda", r"fc( de)? cabinda( cabinda)?$", CAB, 1900, 2100),
    ("Santos de Luanda", r"santos( fc)?( de angola)?( luanda)?$", LUA, 1900, 2100),
    ("Santa Rita do Namibe", r"santa rita$|(gd )?welwitschia$", NAM, 1900, 1999),
    ("Santa Rita de Cássia", r"santa rita( de cassia)?( fc)?$", UIG, 2000, 2100),
    ("Wiliete", r"wiliete( sc| sport clube)?( de)?( benguela)?$", BEN, 1900, 2100),
    ("Domant", r"domant( fc)?( bula atumba)?$", ("Bula Atumba", "Bengo"), 1900, 2100),
    ("Porcelana", r"porcelana( fc)?( ndalatando)?$", ("Ndalatando", "Cuanza Norte"), 1900, 2100),
    ("JGM", r"(clube desportivo )?jgm( academica sc do huambo| do huambo)?$", HUA, 1900, 2100),
    ("Ferrovia do Huambo", r"(cd )?ferrovia do huambo$", HUA, 1900, 2100),
    ("Ferroviário da Huíla", r"ferr(oviario)?\.?( da)? huila$", LUB, 1900, 2100),
    ("Desportivo da Lunda Sul", r"desportivo( da)? lunda sul$", ("Saurimo", "Lunda Sul"), 1900, 2100),
    ("Desportivo da Chela", r"desp(ortivo)?\.?( da)? chela$", LUB, 1900, 2100),
    ("Desportivo da TAAG", r"desp(ortivo)?\.?( da)? taag$", LUA, 1900, 2100),
    ("Desportivo da Cuca", r"desportivo da cuca$", LUA, 1900, 2100),
    ("Desportivo da EKA", r"desportivo da eka$", ("Dondo", "Cuanza Norte"), 1900, 2100),
    ("Desportivo da Nocal", r"desportivo da nocal$", LUA, 1900, 2100),
    ("Desportivo de Benguela", r"desportivo de benguela$", BEN, 1900, 2100),
    ("Desportivo do Xangongo", r"desportivo do xangongo$", ("Xangongo", "Cunene"), 1900, 2100),
    ("Sassamba", r"(desp(ortivo)?\.? )?sassamba( da lunda sul)?$", ("Saurimo", "Lunda Sul"), 1900, 2100),
    ("4 de Abril", r"quatro de abril( do cuando cubango)?$", ("Menongue", "Cuando Cubango"), 1900, 2100),
    ("Cuando Cubango", r"cuando cubango( fc)?$", ("Menongue", "Cuando Cubango"), 1900, 2100),
    ("Ginásio do Cuando Cubango", r"ginasio( do)? cuando cubango$", ("Menongue", "Cuando Cubango"), 1900, 2100),
    ("14 de Abril", r"catorze de abril$", LUA, 1900, 2100),
    ("Construção e Habitação", r"const(rucao)?\.? e habitacao$", LUA, 1900, 2100),
    ("Construtores de Malanje", r"construtores de malanje$", MAL, 1900, 2100),
    ("Makotas de Malanje", r"makotas de malan[gj]e$", MAL, 1900, 2100),
    ("Ritondo", r"ritondo( sport clube)?( de)?( malanje)?$", MAL, 1900, 2100),
    ("União de Malanje", r"(cr )?uniao de malanje$", MAL, 1900, 2100),
    ("Baixa de Cassanje", r"baixa de [ck]assanje$", MAL, 1900, 2100),
    ("Diabos Negros", r"diabos negros$", ("Saurimo", "Lunda Sul"), 1900, 2100),
    ("Diabos Verdes", r"diabos verdes$", ("Huambo", "Huambo"), 1900, 2100),
    ("Dínamo do Cuanza Sul", r"dinamo do kwanza sul$", ("Sumbe", "Cuanza Sul"), 1900, 2100),
    ("Escolinha Isaac", r"(gd )?escolinha isaac$|isaac de benguela$", BEN, 1900, 2100),
    ("Estrela Vermelha", r"estrela vermelha$", HUA, 1900, 2100),
    ("Fabril do Uíge", r"fabril do uige$", UIG, 1900, 2100),
    ("Chicoil", r"(fc )?chicoil$", LUA, 1900, 2100),
    ("FC M'banza Congo", r"fc m ?banza congo$", ("M'banza Congo", "Zaire"), 1900, 2100),
    ("FC Uíge", r"fc uige$", UIG, 1900, 2100),
    ("Gaiatos de Benguela", r"gaiatos de benguela$", BEN, 1900, 2100),
    ("Independente do Tômbwa", r"independente( do tombwa)?$", ("Tômbwa", "Namibe"), 1900, 2100),
    ("Juventude do Kunje", r"juventude do kunje$", ("Cuíto", "Bié"), 1900, 2100),
    ("Juventude do Moxico", r"juventude( do)? moxico$", ("Luena", "Moxico"), 1900, 2100),
    ("Leões de Luanda", r"leoes de luanda$", LUA, 1900, 2100),
    ("Leões do Planalto", r"leoes do planalto$", HUA, 1900, 2100),
    ("Luanda City", r"luanda city( fc)?$", LUA, 1900, 2100),
    ("Luta", r"luta( sc)?$", LUA, 1900, 2100),
    ("Mambroa do Huambo", r"mambroa( do huambo)?$", HUA, 1900, 2100),
    ("Naval de Porto Amboim", r"naval de porto amboim$", ("Porto Amboim", "Cuanza Sul"), 1900, 2100),
    ("Palancas do Huambo", r"palancas( do)? huambo$", HUA, 1900, 2100),
    ("Rangol", r"(saneamentos? )?rangol$", LUA, 1900, 2100),
    ("Redonda", r"redonda( fc)?$", LUA, 1900, 2100),
    ("Guelson", r"(rsd )?guelson( fc)?$", LUA, 1900, 2100),
    ("Saurimo", r"saurimo( fc)?$", ("Saurimo", "Lunda Sul"), 1900, 2100),
    ("Sécil Marítima", r"secil( maritima)?$", ("Lobito", "Benguela"), 1900, 2100),
    ("União do Bié", r"uniao do bie$", ("Cuíto", "Bié"), 1900, 2100),
    ("União do Uíge", r"uniao( sport( clube)?)?( do)? uige$", UIG, 1900, 2100),
    ("Vitória AC", r"vitoria ac$", LUA, 1900, 2100),
    ("ARA da Gabela", r"ara( da)?( gabela)?$", ("Gabela", "Cuanza Sul"), 1900, 2100),
    ("Andorinhas do Sumbe", r"andorinhas do sumbe$", ("Sumbe", "Cuanza Sul"), 1900, 2100),
    ("ASK Dragão", r"ask dragao( do uige)?$", UIG, 1900, 2100),
    ("Cambondo", r"cambondo( sc)?$", MAL, 1900, 2100),
    ("Carmona", r"carmona( sc)?$", UIG, 1900, 2100),
    ("São Salvador", r"(cd )?sao salvador$", ("M'banza Congo", "Zaire"), 1900, 2100),
]

CLUBES: dict[str, tuple[str, str]] = {nome: lugar for nome, _, lugar, _, _ in _DADOS}
REGRAS: list[tuple[str, str, int, int]] = [(rx, nome, a0, a1) for nome, rx, _, a0, a1 in _DADOS]

_MESES = "Janeiro|Fevereiro|Março|Abril|Maio|Junho|Julho|Agosto|Setembro|Outubro|Novembro|Dezembro"
_RE_DATA = re.compile(rf"(?<![\w-])(\d{{1,2}})(?:[ºo°]? de|[º°]) ({_MESES})\b")
_EXTENSO = {1: "Primeiro", 4: "Quatro", 10: "Dez", 11: "Onze", 14: "Catorze", 15: "Quinze", 17: "Dezassete",
            21: "Vinte-e-Um", 22: "Vinte-e-Dois"}


def _regra(k: str, ano: int) -> str | None:
    for rx, exib, a0, a1 in REGRAS:
        if a0 <= ano <= a1 and re.match(rx + r"(?:\b|$)", k):
            return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido). O parêntese do fim
    ("Petro Atlético (Huambo)") vale primeiro como parte do nome; sem regra assim, sai."""
    if not nome:
        return None
    nome = _RE_DATA.sub(lambda m: f"{_EXTENSO.get(int(m.group(1)), m.group(1))} de {m.group(2)}", nome)
    nome = re.sub(r"[*]+$", "", nome).strip()
    if cidade:
        if (r := _regra(chave(f"{nome} {cidade}"), ano)):
            return r
    if "(" in nome and (r := _regra(chave(re.sub(r"\s+(FC|SC)\b", "", nome)), ano)):
        return r
    nome = re.sub(r"\s*\([^)]*\)\s*$", "", nome)
    nome = re.sub(r"\s+(FC|SC)$", "", nome)
    return _regra(chave(nome), ano)
