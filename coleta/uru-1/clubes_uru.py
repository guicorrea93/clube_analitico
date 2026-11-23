"""Identidade dos clubes uruguaios: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido no Brasil ("Peñarol", "Nacional", "Defensor Sporting", "Montevideo Wanderers");
- homônimo de clube do banco ou de outro pacote leva a cidade: "Liverpool de Montevideo", "Racing de Montevideo",
  "River Plate de Montevideo", "Colón de Montevideo", "Belgrano de Montevideo", "Universal de Montevideo",
  "Albion de Montevideo"; o mesmo para nomes genéricos que outros países do continente têm ("Libertad de Montevideo",
  "Olimpia de Montevideo", "Juventud de Las Piedras", "Atenas de San Carlos");
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  Central -> Central Español; Defensor -> Defensor Sporting (fusão com o Sporting em 1989, que manteve a história do
  Defensor); Atlético Wanderers, Lito e Charley da FUF (1923-1924) ficam à parte dos clubes da AUF
  ("Atlético Wanderers", "Lito (FUF)", "Charley (FUF)": um clube não joga duas ligas rivais no mesmo ano; D-25 f, por Edicao.nomes); Deutscher -> Teutonia -> Montevideo FC; Torque -> Montevideo City Torque; C.U.R.C.C. -> Peñarol (como a RSSSF
  conta: a seção de futebol do C.U.R.C.C. virou o Peñarol em 1913-1914; o Nacional contesta, ver o relatório).
- fusões que criaram clube novo ficam separadas: Miramar e Misiones (até 1979) e Miramar Misiones (1980 em diante).
- o River Plate amador (River Plate FC, 1897-1929) não é o River Plate atual (fusão de Olimpia e Capurro em 1932).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano). A chave é o nome sem acento, em
minúsculas, com pontuação trocada por espaço (rsssf_sul.chave). Vale a primeira regra que casa com o começo da chave no ano
da edição; por isso as mais específicas vêm antes.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "comum-sulamerica"))
from rsssf_sul import chave  # noqa: E402

MVD = ("Montevideo", "Montevideo")

# nome de exibição -> (cidade, departamento)
CLUBES: dict[str, tuple[str, str]] = {
    # profissionais
    "Peñarol": MVD, "Nacional": MVD, "Defensor Sporting": MVD, "Danubio": MVD, "Montevideo Wanderers": MVD,
    "Liverpool de Montevideo": MVD, "River Plate de Montevideo": MVD, "Cerro": MVD, "Fénix": MVD, "Rampla Juniors": MVD,
    "Central Español": MVD, "Bella Vista": MVD, "Racing de Montevideo": MVD, "Sud América": MVD, "Progreso": MVD,
    "Rentistas": MVD, "Huracán Buceo": MVD, "Basáñez": MVD, "Miramar Misiones": MVD, "Cerrito": MVD, "Villa Española": MVD,
    "El Tanque Sisley": MVD, "Boston River": MVD, "Montevideo City Torque": MVD, "Villa Teresa": MVD, "La Luz": MVD,
    "Juventud de Las Piedras": ("Las Piedras", "Canelones"), "Plaza Colonia": ("Colonia del Sacramento", "Colonia"),
    "Deportivo Colonia": ("Juan Lacaze", "Colonia"), "Cerro Largo": ("Melo", "Cerro Largo"),
    "Tacuarembó": ("Tacuarembó", "Tacuarembó"), "Frontera Rivera": ("Rivera", "Rivera"), "Rocha FC": ("Rocha", "Rocha"),
    "Deportivo Maldonado": ("Maldonado", "Maldonado"), "Atenas de San Carlos": ("San Carlos", "Maldonado"),
    "Paysandú Bella Vista": ("Paysandú", "Paysandú"), "Paysandú FC": ("Paysandú", "Paysandú"),
    "Albion de Montevideo": MVD, "Miramar": MVD, "Misiones": MVD, "Colón de Montevideo": MVD, "Alto Perú": MVD,
    # amadorismo (1900-1931) e a liga dissidente (FUF, 1923-1924)
    "Uruguay Athletic": MVD, "Montevideo FC": MVD, "Triunfo": MVD, "Intrépido": MVD, "French": MVD, "Bristol": MVD,
    "Dublin": MVD, "Oriental": MVD, "River Plate FC": MVD, "Libertad de Montevideo": MVD, "Independencia": MVD,
    "Reformers": MVD, "Universal de Montevideo": MVD, "Charley": MVD, "Charley (FUF)": MVD, "Lito (FUF)": MVD, "Atlético Wanderers": MVD, "Belgrano de Montevideo": MVD, "Lito": MVD,
    "Uruguay Onward": MVD, "Nacional B": MVD, "Capurro": MVD, "Uruguay Club": MVD, "Olimpia de Montevideo": MVD,
    "Peñarol del Plata": MVD, "Rosarino Central": MVD, "Roberto Chery": MVD, "Roland Moor": MVD,
    "Las Piedras": ("Las Piedras", "Canelones"), "Uruguayo": MVD, "Oriental Pocitos": MVD, "Solferino": MVD,
    "Bequelo": MVD, "Sayago": MVD, "San Carlos Taurino": MVD, "Triumph Juniors": MVD, "Treinta y Tres": MVD,
    "Miguelete": MVD, "Belvedere": MVD, "Firestone": MVD, "Livingstone": MVD, "Sportivo Aguada": MVD,
    "Uruguay Forever": MVD,
}

REGRAS: list[tuple[str, str, int, int]] = [
    # grandes
    (r"(ca |club atletico )?penarol del plata", "Peñarol del Plata", 1900, 1930),
    (r"(ca |club atletico )?penarol", "Peñarol", 1900, 2100),
    (r"c u r c c|curcc|central uruguay railway", "Peñarol", 1900, 1913),
    (r"nacional b\b", "Nacional B", 1900, 1910),
    (r"(c |club )?nacional( df| de football)?", "Nacional", 1900, 2100),
    (r"defensor( sp(orting)?( club)?)?|ca defensor", "Defensor Sporting", 1900, 2100),
    (r"danubio( fc)?", "Danubio", 1930, 2100),
    (r"(montevideo |m |atletico )wanderers|wanderers", "Montevideo Wanderers", 1900, 2100),
    (r"liverpool( fc| montevideo)?", "Liverpool de Montevideo", 1915, 2100),
    (r"(ca )?river plate fc|river plate", "River Plate FC", 1897, 1929),
    (r"(ca )?river( plate)?", "River Plate de Montevideo", 1932, 2100),
    (r"(ca )?cerro largo", "Cerro Largo", 1990, 2100),
    (r"(ca )?cerro\b(?! largo)", "Cerro", 1920, 2100),
    (r"(ca )?fenix", "Fénix", 1915, 2100),
    (r"rampla( jrs| juniors)?", "Rampla Juniors", 1915, 2100),
    (r"central espanol|central( fc)?$|central\b(?! uruguay)", "Central Español", 1905, 2100),
    (r"rosarino central", "Rosarino Central", 1920, 1930),
    # interior e homônimos
    (r"bella vista paysandu|paysandu (bella vista|bv)|bella vista \(?paysandu", "Paysandú Bella Vista", 1990, 2010),
    (r"paysandu( fc)?", "Paysandú Bella Vista", 1990, 2002),
    (r"paysandu( fc)?", "Paysandú FC", 2003, 2100),
    (r"(ca )?bella vista", "Bella Vista", 1915, 2100),
    (r"racing( club)?( cm| de sayago| sayago| club montevideo| montevideo| \(montevideo\))?|racing", "Racing de Montevideo", 1915, 2100),
    (r"(ia )?sud america", "Sud América", 1915, 2100),
    (r"(ca )?progreso", "Progreso", 1930, 2100),
    (r"(ca )?rentistas", "Rentistas", 1930, 2100),
    (r"(ca )?basanez", "Basáñez", 1930, 2100),
    (r"huracan b(uceo)?|h b(uceo)?\b|huracan|huaracan", "Huracán Buceo", 1937, 2100),
    (r"(cs )?miramar misiones( fc)?", "Miramar Misiones", 1980, 2100),
    (r"(cs )?miramar", "Miramar", 1900, 1979),
    (r"(cs )?miramar", "Miramar Misiones", 1980, 2100),
    (r"misiones", "Misiones", 1900, 1979),
    (r"(cs )?cerrito", "Cerrito", 1930, 2100),
    (r"(csyd )?villa esp(anola)?", "Villa Española", 1930, 2100),
    (r"(ccyd )?el tanque( sisley)?", "El Tanque Sisley", 1960, 2100),
    (r"(ca )?boston river", "Boston River", 1930, 2100),
    (r"montevideo city( torque)?|(ca )?torque", "Montevideo City Torque", 2007, 2100),
    (r"(ca )?villa teresa", "Villa Teresa", 1990, 2100),
    (r"la luz( fc)?", "La Luz", 1990, 2100),
    (r"(ca )?juventud( \(?las piedras\)?| lp)?", "Juventud de Las Piedras", 1990, 2100),
    (r"(ca )?plaza( colonia| \(colonia\))?", "Plaza Colonia", 1990, 2100),
    (r"(cd |dep |deportivo )?colonia", "Deportivo Colonia", 1990, 2100),
    (r"(deportivo )?(tacuarembo|tacauarembo|tacaurembo)( fc)?", "Tacuarembó", 1990, 2100),
    (r"frontera( rivera)?", "Frontera Rivera", 1990, 2100),
    (r"rocha( fc)?", "Rocha FC", 1990, 2100),
    (r"(cd |club deportivo |dep |deportivo )?maldonado", "Deportivo Maldonado", 1990, 2100),
    (r"(ca )?atenas", "Atenas de San Carlos", 1990, 2100),
    (r"alto peru", "Alto Perú", 1960, 1980),
    (r"albion( fc)?", "Albion de Montevideo", 1890, 2100),
    (r"colon", "Colón de Montevideo", 1900, 1990),
    # amadorismo
    (r"uruguay athletic", "Uruguay Athletic", 1890, 1930),
    (r"deutscher|teutonia|montevideo$", "Montevideo FC", 1890, 1915),
    (r"triunfo", "Triunfo", 1890, 1915),
    (r"intrepido", "Intrépido", 1890, 1915),
    (r"french", "French", 1890, 1915),
    (r"bristol", "Bristol", 1890, 1920),
    (r"dublin", "Dublin", 1890, 1930),
    (r"oriental pocitos", "Oriental Pocitos", 1920, 1930),
    (r"oriental", "Oriental", 1890, 1915),
    (r"libertad", "Libertad de Montevideo", 1890, 1920),
    (r"independencia", "Independencia", 1890, 1920),
    (r"reformers", "Reformers", 1890, 1930),
    (r"universal", "Universal de Montevideo", 1890, 1935),
    (r"charley", "Charley", 1890, 1930),
    (r"belgrano", "Belgrano de Montevideo", 1890, 1935),
    (r"lito", "Lito", 1890, 1935),
    (r"uruguay onward", "Uruguay Onward", 1890, 1935),
    (r"capurro", "Capurro", 1890, 1935),
    (r"uruguay club", "Uruguay Club", 1890, 1935),
    (r"olimpia", "Olimpia de Montevideo", 1890, 1935),
    (r"roberto chery", "Roberto Chery", 1920, 1930),
    (r"roland moor", "Roland Moor", 1920, 1930),
    (r"las piedras", "Las Piedras", 1920, 1930),
    (r"uruguayo", "Uruguayo", 1920, 1930),
    (r"solferino", "Solferino", 1920, 1930),
    (r"bequelo", "Bequelo", 1920, 1930),
    (r"sayago", "Sayago", 1920, 1930),
    (r"san carlos taurino", "San Carlos Taurino", 1920, 1930),
    (r"triumph juniors", "Triumph Juniors", 1920, 1930),
    (r"treinta y tres", "Treinta y Tres", 1920, 1930),
    (r"miguelete", "Miguelete", 1920, 1930),
    (r"belvedere", "Belvedere", 1920, 1930),
    (r"firestone", "Firestone", 1920, 1930),
    (r"livingstone", "Livingstone", 1920, 1930),
    (r"sportivo aguada", "Sportivo Aguada", 1920, 1930),
    (r"uruguay forever", "Uruguay Forever", 1920, 1930),
]


def _regra(k: str, ano: int) -> str | None:
    for kk in (k, re.sub(r"^(club|c) ", "", k)):
        for rx, exib, a0, a1 in REGRAS:
            if a0 <= ano <= a1 and re.match(rx + r"(?:\b|$)", kk):
                return exib
    return None


def clube(nome: str, ano: int, cidade: str | None = None) -> str | None:
    """Nome de exibição do clube para a grafia `nome` numa edição de `ano` (None: não reconhecido).
    `cidade` (a sede que a tabela mostra entre parênteses) desfaz homônimos: Bella Vista (Paysandú)."""
    if cidade:
        x = _regra(f"{chave(nome)} {chave(cidade)}", ano)
        if x:
            return x
    return _regra(chave(nome), ano)


assert all(e in CLUBES for _, e, _, _ in REGRAS), [e for _, e, _, _ in REGRAS if e not in CLUBES]
