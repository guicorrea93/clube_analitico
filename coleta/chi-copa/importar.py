"""Copa Chile (chi-copa): copa nacional da ANFP. Sexta das sete copas da América do Sul (decisões do Guilherme de
24/11/2026 em coleta/comum-sulamerica/copas-nacionais.md): contagem da Wikipédia em espanhol, 45 edições de 1958 em diante
(sem 1963-73, 1976, 1997, 1999, 2001-07 e 2020). Entra tudo o que a RSSSF traz de cada edição.

Fontes (um importador comum: coleta/comum-sulamerica/copa_rsssf.py):
- RSSSF: a seção da copa nas páginas do ano do chi-1 (data/coleta/chi-1/rsssf: chile58 ... chile2025, chilecup84-86) e
  chilecup08.html (Copa Chile 2008-09, em data/coleta/chi-copa/rsssf/); a lista de finais (chilecuphist.html) para conferir;
- campeão conferido com a Wikipédia em espanhol ("Copa Chile").

Formatos que mudam por época:
- 1979-1982 a copa é o "Campeonato de Apertura" (Copa Polla-Gol), só da 1ª divisão: grupos e mata-mata (1982: quadrangular
  final, campeão pela tabela); 1983 é a "Copa República";
- 1984 e 1985 só trazem a tabela dos grupos (jogos e pontos) e o mata-mata em linhas "A-B 3-1"; 1986, só a final;
- 1990-1996 os jogos vêm com siglas ("NAV-UC 2-1 [público, árbitro]"), trocadas aqui pelos nomes (SIGLAS em clubes_copa.py).

Uso: python coleta/chi-copa/importar.py
"""
from __future__ import annotations

import re
import sys
from datetime import timedelta
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
sys.path.insert(1, str(AQUI.parent / "chi-1"))
import autores  # noqa: E402  (o do chi-1)
import ler_rsssf  # noqa: E402  (o do chi-1: páginas em data/coleta/chi-1/rsssf)
import rsssf_sul  # noqa: E402
from clubes_copa import CLUBES, SIGLAS, clube  # noqa: E402
from copa_rsssf import Copa, EdicaoCopa, espn_arquivos, importar  # noqa: E402
import wiki_copas  # noqa: E402

SLUG = "chi-copa"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"
PASTA = RAIZ / "data" / "coleta" / SLUG / "rsssf"


def linhas(pagina: str) -> tuple[str, ...]:
    if pagina == "chilecup08":
        return tuple(rsssf_sul.texto(PASTA / f"{pagina}.html"))
    ls = ler_rsssf.linhas(pagina)
    return _junta_suspensos(ls) if re.fullmatch(r"chile9[0-6]", pagina) else ls


def _junta_suspensos(ls: tuple[str, ...]) -> tuple[str, ...]:
    """Jogos de 1990-1996 suspensos e completados: "CC-PAL  *suspended" com o placar final na linha de baixo ("0-0  [8051,
    Silva]") vira uma linha só, na linha do placar; "U-EV  4-3*[...]" com "Final: 4-4" logo abaixo fica com o placar final."""
    ls = list(ls)
    for i, l in enumerate(ls):
        if m := re.match(r"^\s*([A-Za-zÑñ]{1,4}-[A-Za-zÑñ]{1,4})\s+\*suspended", l):
            for k in range(i + 1, min(i + 4, len(ls))):
                if mm := re.match(r"^\s*(\d{1,2}-\s*\d{1,2})\s*(.*)$", ls[k]):
                    ls[k], ls[i] = f"{m.group(1)}  {mm.group(1)} {mm.group(2)}", ""
                    break
        elif m := re.match(r"^(\s*[A-Za-zÑñ]{1,4}-[A-Za-zÑñ]{1,4}\s+)\d{1,2}-\s*\d{1,2}\*", l):
            for k in range(i + 1, min(i + 6, len(ls))):
                if mm := re.match(r"^\s*Final:\s*(\d{1,2}-\d{1,2})", ls[k]):
                    ls[i], ls[k] = m.group(1) + mm.group(1) + " " + l[m.end():], ""
                    break
    return tuple(ls)


PRE, GRU, GR2, DES = "Fase preliminar", "Fase de grupos", "Segunda fase de grupos", "Fase de grupos (desempate)"
P1, P2, P3, P4, P5 = "Primeira fase", "Segunda fase", "Terceira fase", "Quarta fase", "Quinta fase"
REG = "Fase regional"
OIT, QUA, SEM, TER, FIN = "Oitavas de final", "Quartas de final", "Semifinal", "Disputa do 3º lugar", "Final"
FFIN = "Fase final (quadrangular)"
# ordem geral das fases (a última é a final); os títulos de cada página estão nas listas por edição, abaixo
FASES = [(r"^NUNCA$", f) for f in (PRE, "Primeira fase preliminar", "Segunda fase preliminar", REG, GRU, DES, GR2, P1, P2, P3, P4, P5,
                                   OIT, QUA, SEM, FFIN, TER)] + [(r"^NUNCA$", FIN)]
KO = [(r"^(1/8 [Ff]inals?|Octaves Final|Second Round \(1/8)", OIT), (r"^Quarter[- ]?[Ff]inals?|^Quarter Final|^Quarterfinal:", QUA),
      (r"^Semi[- ]?[Ff]inals?|^Semifinal", SEM), (r"^Third Place", TER), (r"^Finals?\b(?! Tables?| Table)(?!:?\s*\d)", FIN)]
RODADAS = [(r"^Round 1\b", P1), (r"^Round 2\b", P2), (r"^Round 3\b", P3)]


def _secao(pagina: str, ini: str, fim: str, ultima: bool = False, depois: int = 0) -> tuple[str, int, int]:
    """Trecho da página: da linha que começa com `ini` (a última, se `ultima`; a 1ª depois de `depois`) até a que casa `fim`."""
    ls = linhas(pagina)
    achados = [i for i, l in enumerate(ls) if i >= depois and re.match(ini, l.strip())]
    a = achados[-1] if ultima else achados[0]
    b = next((i for i in range(a + 1, len(ls)) if re.match(fim, ls[i].strip())), len(ls))
    return pagina, a, b


def _grupos(pagina: str, ini: str, fim: str, ano: int, depois: str = "") -> dict[str, str]:
    """{clube: grupo} pelas tabelas finais dos grupos ("Group A" / "GROUP 1" e linhas " 1: COBRELOA  15  10 ..." ou
    " 1.D. Iquique  10 ..."), para os jogos de 1991-1995 que vêm sem o título do grupo. `depois`: começar a procurar
    depois dessa linha (a segunda fase de grupos de 1993)."""
    ls = linhas(pagina)
    d = next(i for i, l in enumerate(ls) if re.match(depois, l.strip())) if depois else 0
    pagina, a, b = _secao(pagina, ini, fim, depois=d)
    grupo, saida = "", {}
    for l in ls[a:b]:
        if mg := re.match(r"^\s*group\s+([A-Z0-9])\b", l, re.I):
            grupo = mg.group(1).upper()
        elif grupo and (mc := re.match(r"^\s*\d{1,2}[.:]\s*(.+?)\s*\*?\s{2,}\d", l)):
            if c := clube(mc.group(1), ano):
                saida[c] = grupo
    return saida


_FIM_MODERNO = (r"^(Torneo|Campeonato|Primera B( \d|$)|Penalties:|Segunda División \d|Liguilla|Copa Sudamericana|"
                r"Copa Libertadores|list of|About|Second Level|Supercopa|Chile Second|Promotion|Topscorers|20\d\d$)")


def _moderna(pagina: str, titulo: str) -> tuple[str, int, int]:
    return _secao(pagina, re.escape(titulo), _FIM_MODERNO, ultima=True)


# siglas de 1990-1996: "NAV-UC  2-1 [4079, Torrens]" -> "Naval de Talcahuano   2-1   Universidad Católica"
_SIGLA = re.compile(r"^\s*([A-Za-zÑñ]{1,4})-([A-Za-zÑñ]{1,4})\s+(\d{1,2})-\s*(\d{1,2})\*?(?:\s+IG)?\s*"
                    r"(?:\?|(?:\[(?!pen )[^\]]*\]+\s*)*)(?:\[pen (\d{1,2})-(\d{1,2})\])?\s*$")


def _troca_sigla(m: re.Match) -> str:
    a, b = SIGLAS.get(m.group(1).upper()), SIGLAS.get(m.group(2).upper())
    if not a or not b:
        return m.group(0)
    pen = f"   [{m.group(5)}-{m.group(6)} pen]" if m.group(5) else ""   # "[pen 6-5]" -> "[6-5 pen]"
    return f"{a:<30}{m.group(3)}-{m.group(4)}   {b}{pen}"


SIGLA = [(_SIGLA.pattern, _troca_sigla)]
# 1984-1985: "Colo Colo Santiago-Cobresal El Salvador 3-1" e "Green Cross-Universidad Catolica 0-0 and 2-3"
_HIFEN = r"^([A-Za-zÀ-ÿ\.' ]+?)-([A-Za-zÀ-ÿ\.' ]+?)\s+(\d{1,2})-(\d{1,2})(?:\s*aet)?(?:\s+and\s+(\d{1,2})-(\d{1,2}))?(\s*\(.*\))?\s*$"


def _troca_hifen(m: re.Match) -> str:
    ida = f"{m.group(1).strip():<32}{m.group(3)}-{m.group(4)}"
    if m.group(5):   # ida e volta na mesma linha: o leitor comum só aceita "A  0-0 2-3 B" (um espaço antes de B)
        return f"{ida} {m.group(5)}-{m.group(6)} {m.group(2).strip()}" + (f"   [{m.group(7).strip(' ()')}]" if m.group(7) else "")
    return f"{ida}   {m.group(2).strip()}" + (f"   [{m.group(7).strip(' ()')}]" if m.group(7) else "")


HIFEN = [(_HIFEN, _troca_hifen)]


WIKI = RAIZ / "data" / "coleta" / SLUG / "wikipedia"
_GRUPOS_WIKI = ("jogos dos grupos pela Wikipédia em espanhol (a RSSSF só traz as tabelas, que conferem com eles); "
                "mata-mata pela RSSSF")


def _grupos_wiki(edicao: str, ano: int):
    """Jogos da fase de grupos na Wikipédia em espanhol ("Copa Chile 2013-14" ...; pendência D5)."""
    return lambda: wiki_copas.tabela_jogos(WIKI / f"es_{edicao}.txt", edicao, r"^Fase de grupos", r"^Fase final", GRU, (ano, ano))


def _wiki_2022():
    """Copa Chile 2022 antes das quartas: fases 1 e 2 (tabelas da página da edição), 3ª fase e oitavas (anexos)."""
    return (wiki_copas.tabela_jogos(WIKI / "es_2022.txt", "2022", r"^Fase 1$", r"^Fase 2$", P1, (2022, 2022), grupos=False)
            + wiki_copas.tabela_jogos(WIKI / "es_2022.txt", "2022", r"^Fase 2$", r"^Eliminatorias", P2, (2022, 2022), grupos=False)
            + wiki_copas.partidos(WIKI / "es_2022_tercera.txt", "2022_tercera", P3)
            + wiki_copas.partidos(WIKI / "es_2022_octavos.txt", "2022_octavos", OIT))


def _wiki_2023():
    """Copa Chile 2023 antes das finais zonais: fase previa (anexo "Fase 1") e oitavas a semifinais de cada zona (anexo
    "Fase Regional"; a final de cada zona vem da RSSSF)."""
    z = "Fase regional"
    return (wiki_copas.partidos(WIKI / "es_2023_fase1.txt", "2023_fase1", "Segunda fase preliminar")
            + wiki_copas.partidos(WIKI / "es_2023_regional.txt", "2023_regional", None,
                                  {r"^Octavos": f"{z}: oitavas", r"^Cuartos": f"{z}: quartas", r"^Semifinales": f"{z}: semifinal",
                                   r"^Final Regional": None, r"^Clasificado": None}))


def ed(temporada: str, a0: int, a1: int, trechos: list, fases: list | None = None, **kw) -> EdicaoCopa:
    return EdicaoCopa(temporada, a0, a1, f"Copa Chile {temporada}", trechos, fases=fases, **kw)


_F58 = [(r"^First Round", P1), (r"^Second Round", P2)] + KO
_F61 = [(r"^First Round", P1), (r"^Second Round", P2), (r"^Third Round", P3)] + KO
_SEG = r"^Second Division"
EDICOES = [
    ed("1958", 1958, 1958, [_secao("chile58", r"^Copa Chile$", _SEG)], _F58, campeao_fonte="Colo Colo",
       obs="final empatada (2-2): Colo Colo campeão nos pênaltis segundo a RSSSF (outras fontes: pelo saldo de gols do torneio)"),
    ed("1959", 1959, 1959, [_secao("chile59", r"^Copa Chile$", _SEG)], _F58),
    ed("1960", 1960, 1960, [_secao("chile60", r"^Copa Chile$", _SEG)], [(r"^Group Stage", GRU), (r"^Playoff Winners", DES)] + KO,
       obs="com seleções de cidades (amadoras) além dos clubes da 1ª e da 2ª divisão"),
    ed("1961", 1961, 1961, [_secao("chile61", r"^Copa Chile$", _SEG)], _F61),
    ed("1962", 1962, 1962, [_secao("chile62", r"^Copa Chile$", _SEG)], _F61),
    ed("1974", 1974, 1974, [_secao("chile74", r"^Copa Chile$", _SEG)], [(r"^Tables:", GRU)] + KO,
       regioes=[(r"^Northern Group", "Norte"), (r"^Central Group", "Centro"), (r"^Southern Group", "Sul")],
       fim_regiao=r"^Quarterfinals",
       obs="fase de grupos regional (Norte, Centro e Sul); empate decidido nos pênaltis vale um ponto ao vencedor"),
    ed("1975", 1975, 1975, [_secao("chile75", r"^Copa Chile$", _SEG)], [(r"^Preliminary Round", PRE), (r"^First Round", P1)] + KO),
    ed("1977/78", 1977, 1978, [_secao("chile78", r"^Copa Chile$", _SEG)], [(r"^First Stage", GRU)] + KO,
       obs="a Wikipédia chama de 1977; a RSSSF põe na página de 1978"),
    ed("1979", 1979, 1979, [_secao("chile79", r"^First Division\. Campeonato de Apertura", r"^Campeonato Oficial")],
       [(r"^First Phase", GRU)] + KO, obs="Campeonato de Apertura (Copa Polla-Gol), só da 1ª divisão"),
]
for _a in (1980, 1981):
    EDICOES.append(ed(str(_a), _a, _a, [_secao(f"chile{_a % 100}", r"^First Division\.$", r"^Campeonato Oficial")],
                      [(r"^First Phase", GRU)] + KO, obs="Campeonato de Apertura (Copa Polla-Gol), só da 1ª divisão"))
EDICOES += [
    ed("1982", 1982, 1982, [_secao("chile82", r"^First Division\.$", r"^Campeonato Oficial")],
       [(r"^First Phase", GRU), (r"^Second Phase", P2), (r"^Third Phase", FFIN)] + KO, campeao_tabela=True,
       obs="Campeonato de Apertura (Copa Polla-Gol), só da 1ª divisão; quadrangular final, campeão pela tabela"),
    ed("1983", 1983, 1983, [_secao("chile83", r"^Copa República", r"^Campeonato Oficial")],
       [(r"^First Phase", P1), (r"^Second Phase", P2), (r"^Third Phase", P3)] + KO, obs="Copa República"),
    ed("1984", 1984, 1984, [_secao("chilecup84", r"^POLLA GOL", r"^Segunda División")], [(r"^Group 1", GRU)] + KO,
       trocas=HIFEN, obs="Copa Polla Gol; a RSSSF só traz a tabela dos grupos (jogos e pontos) e o mata-mata"),
    ed("1985", 1985, 1985, [_secao("chilecup85", r"^POLLA GOL", r"^Segunda División")], [(r"^Group 1", GRU)] + KO,
       trocas=HIFEN, obs="Copa Polla Gol; a RSSSF só traz os grupos (sem jogos) e o mata-mata"),
    ed("1986", 1986, 1986, [_secao("chilecup86", r"^FINAL TABLES TORNEO APERTURA", r"^Liguilla Pre-Libertadores")],
       [(r"^North", GRU)] + KO, trocas=HIFEN,
       obs="Torneo Apertura; a RSSSF só traz as tabelas dos grupos e um jogo da final (a lista de finais dá 0-1, 2-0 e 3-0)"),
]
for _a in (1987, 1988, 1989):
    EDICOES.append(ed(str(_a), _a, _a, [_secao(f"chile{_a % 100}", rf"^Copa Chile {_a}", r"^Liguilla Pre-Libertadores")],
                      [(r"^Group Stage", GRU)] + KO))
EDICOES += [
    ed("1990", 1990, 1990, [_secao("chile90", r"^Points System", r"^Segunda División")], [(r"^Round 1$", GRU)] + KO, trocas=SIGLA,
       obs="fase de grupos em pontos corridos (os 16 da 1ª divisão) e final"),
    ed("1991", 1991, 1991, [_secao("chile91", r"^Copa de Chile 1991", r"^Segunda División")], [(r"^Group Stage", GRU)] + KO,
       trocas=SIGLA, grupos_clubes={GRU: _grupos("chile91", r"^Final Tables:", r"^Second Round", 1991)}),
    ed("1992", 1992, 1992, [_secao("chile92", r"^Copa de Chile 1992", r"^FINAL TABLE 2nd")], [(r"^First Stage", GRU)] + KO,
       trocas=SIGLA, grupos_clubes={GRU: _grupos("chile92", r"^Final Tables:", r"^Second Round", 1992)}),
    ed("1993", 1993, 1993, [_secao("chile93", r"^Copa Chile 1993", r"^Second Level")],
       [(r"^First Stage", GRU), (r"^SECOND STAGE", GR2)] + KO, trocas=SIGLA,
       grupos_clubes={GRU: _grupos("chile93", r"^GROUP 1 ", r"^SECOND STAGE", 1993),
                      GR2: _grupos("chile93", r"^GROUP 1 ", r"^\* Qualify to Semifinals", 1993, depois=r"^SECOND STAGE")}),
    ed("1994", 1994, 1994, [_secao("chile94", r"^Copa Chile 1994", r"^Second Level")], [(r"^Round 1$", GRU)] + KO, trocas=SIGLA),
    ed("1995", 1995, 1995, [_secao("chile95", r"^Cup 1995", r"^Second Level")],
       [(r"^Primera División:", GRU), (r"^Second Round:", P2)] + KO, trocas=SIGLA,
       grupos_clubes={GRU: _grupos("chile95", r"^Final Tables:", r"^Round 1$", 1995)}),
    ed("1996", 1996, 1996, [_secao("chile96", r"^Chile Cup 1996", r"^Chile Second Division")],
       [(r"^FIRST DIVISION", GRU), (r"^\* Qualified for next round with the winners for First", QUA)] + KO, trocas=SIGLA,
       obs="as quartas de final vêm sem título na página (depois das tabelas da 2ª divisão)"),
    ed("1998", 1998, 1998, [_secao("chile98", r"^NB: Primera B teams refused", r"^Chile Second Level")],
       [(r"^Primera A:", GRU)] + KO, obs="sem os clubes da Primera B, que se recusaram a jogar"),
    ed("2000", 2000, 2000, [_secao("chile00", r"^COPA CARRANZA", r"^TORNEO NACIONAL")], [(r"^Tables:", GRU)] + KO,
       obs="Copa Carranza; os vencedores dos grupos jogam o mata-mata do \"Torneo de Apertura\""),
    ed("2008/09", 2008, 2009, [_secao("chilecup08", r"^\"Copa Chile 2008", r"^20\d\d$")],
       [(r"^Preliminary Round", PRE), (r"^First Phase", P1), (r"^Second Phase", P2), (r"^Third Phase", P3)] + KO),
    ed("2009", 2009, 2009, [_moderna("chile09", "Copa Chile 2009")],
       [(r"^Preliminary Round", PRE), (r"^First Phase", P1), (r"^Second Phase", P2), (r"^Third Round", P3),
        (r"^Fourth Round", P4), (r"^Fifth Round", P5)] + KO),
]
_p, _a10, _b10 = _moderna("chile2010", "Copa Chile")
_m10 = next(i for i in range(_a10, _b10) if linhas("chile2010")[i].strip().startswith("- 14 Primera B"))
EDICOES += [
    ed("2010", 2010, 2010, [(_p, _a10, _m10, [(r"^Preliminary Round", PRE), (r"^First Phase", "Primeira fase preliminar"),
                                              (r"^Second Phase", "Segunda fase preliminar")]),
                            (_p, _m10, _b10, [(r"^First Phase", P1), (r"^Second Phase", P2)] + KO)]),
    ed("2011", 2011, 2011, [_moderna("chile2011", "Copa Chile 2011")],
       [(r"^First Phase", PRE), (r"^Second Phase", "Primeira fase preliminar"), (r"^Third Phase", "Segunda fase preliminar")]
       + RODADAS + KO),
    ed("2012/13", 2012, 2013, [_moderna("chile2013", "Copa Chile 2012/13")], [(r"^First Phase", P1), (r"^Group Stage", GRU)] + KO,
       anos_leitura=(2012, 2012)),
    ed("2013/14", 2013, 2014, [_moderna("chile2014", "Copa Chile 2013/14")], [(r"^Group Stage", GRU)] + KO,
       extras=_grupos_wiki("2013-14", 2013), obs=_GRUPOS_WIKI),
    ed("2014/15", 2014, 2015, [_moderna("chile2015", "Copa Chile 2014/15")], [(r"^Group Stage", GRU), (r"^Round 2", OIT)] + KO,
       extras=_grupos_wiki("2014-15", 2014), obs=_GRUPOS_WIKI),
    ed("2015", 2015, 2016, [_moderna("chile2016", "Copa Chile 2015")], [(r"^Group Stage", GRU)] + KO,
       extras=_grupos_wiki("2015", 2015), obs=_GRUPOS_WIKI),
    ed("2016", 2016, 2016, [_moderna("chile2017", "Copa Chile 2016")], [(r"^Round 1\b", P1)] + KO),
    ed("2017", 2017, 2017, [_moderna("chile2017a", "Copa Chile 2017")], RODADAS + KO),
    ed("2018", 2018, 2018, [_moderna("chile2018", "Copa Chile 2018")], RODADAS + KO),
    ed("2019/20", 2019, 2020, [_moderna("chile2019", "Copa Chile 2019/20")], RODADAS + KO,
       anos_leitura=(2019, 2019), obs="a Wikipédia chama de 2019; final em janeiro de 2020"),
    ed("2021", 2021, 2021, [_moderna("chile2021", "Copa Chile 2021")], RODADAS + KO),
    ed("2022", 2022, 2022, [_moderna("chile2022", "Copa Chile 2022")], KO, extras=_wiki_2022,
       obs="das quartas de final em diante pela RSSSF; fases 1 a 3 e oitavas pela Wikipédia em espanhol (página da edição "
           "e anexos da 3ª fase e das oitavas)"),
    ed("2023", 2023, 2023, [_moderna("chile2023", "Copa Chile 2023")], [(r"^Fase Regional", "Fase regional: final")] + KO,
       regioes=[(r"^Zona Norte", "Norte"), (r"^Zona Centro Norte", "Centro Norte"), (r"^Zona Centro Sur", "Centro Sur"),
                (r"^Zona Sur", "Sur")], fim_regiao=r"^Fase Nacional", extras=_wiki_2023,
       obs="finais zonais em diante pela RSSSF; fase previa e fase regional (oitavas a semifinais de cada zona) pelos anexos "
           "da Wikipédia em espanhol; ficam de fora as preliminares amadoras de Aysén e Magallanes (só em chave, sem mando)"),
]
_p, _a24, _b24 = _moderna("chile2024", "Copa Chile 2024")
_m24 = next(i for i in range(_b24 - 1, _a24, -1) if linhas("chile2024")[i].strip().startswith("Semifinals"))
_Z = "Fase regional"
EDICOES += [
    ed("2024", 2024, 2024, [(_p, _a24, _m24, [(r"^Fase Inaugural", PRE), (r"^Fase Preliminar", "Primeira fase preliminar"),
                                              (r"^Fase Previa", "Segunda fase preliminar"), (r"^1/8 Finals", f"{_Z}: oitavas"),
                                              (r"^Quarterfinals", f"{_Z}: quartas"), (r"^Semifinals", f"{_Z}: semifinal"),
                                              (r"^Final\b", f"{_Z}: final")]),
                            (_p, _m24, _b24, KO)],
       regioes=[(r"^Región de", "Aysén"), (r"^Previa", ""), (r"^Zona Norte", "Norte"), (r"^Zona Centro Norte", "Centro Norte"),
                (r"^Zona Centro Sur", "Centro Sur"), (r"^Zona Sur", "Sur")],
       obs="fases regionais por zona (Norte, Centro Norte, Centro Sur, Sur); os campeões zonais jogam as semifinais"),
    ed("2025", 2025, 2025, [_moderna("chile2025", "Copa Chile 2025")], KO,
       extras=lambda: wiki_copas.partidos(WIKI / "es_2025_zonal.txt", "2025_zonal", GRU),
       obs="das oitavas de final em diante pela RSSSF; fase zonal (8 grupos) pelo anexo da Wikipédia em espanhol"),
]
_k = FASES.index((r"^NUNCA$", REG)) + 1   # as fases zonais de 2024 vêm logo depois da fase regional
FASES[_k:_k] = [(r"^NUNCA$", f"{_Z}: {x}") for x in ("oitavas", "quartas", "semifinal", "final")]

COMPETICAO = {
    "slug": SLUG, "nome": "Copa Chile", "nome_curto": "Copa Chile", "tipo": "copa", "nivel": None, "pais": "CHI",
    "pais_nome": "Chile", "regiao": None, "confederacao": "CONMEBOL", "rotulo_painel": "Copa Chile",
    "menu_painel": "Chile · Copa Chile", "do_painel": "da Copa Chile", "o_painel": "a Copa Chile",
    "observacao": "Copa nacional da ANFP, de 1958 em diante (sem 1963-73, 1976, 1997, 1999, 2001-07 e 2020). Em 1979-1982 é o "
                  "Campeonato de Apertura (Copa Polla-Gol) e em 1983 a Copa República. Os jogos de 1984-1986 são parciais."}

# lista de finais da RSSSF (chilecuphist.html), que bate com a da Wikipédia em espanhol ("Copa Chile") salvo os rótulos
# 1977/78 (Wikipédia: 1977) e 2019/20 (Wikipédia: 2019), pela pesquisa em copas-nacionais.md
CAMPEOES_WIKI = {
    "1958": "Colo Colo", "1959": "Santiago Wanderers", "1960": "Deportes La Serena", "1961": "Santiago Wanderers",
    "1962": "Luis Cruz Martínez", "1974": "Colo Colo", "1975": "Palestino", "1977/78": "Palestino", "1979": "Universidad de Chile",
    "1980": "Deportes Iquique", "1981": "Colo Colo", "1982": "Colo Colo", "1983": "Universidad Católica", "1984": "Everton",
    "1985": "Colo Colo", "1986": "Cobreloa", "1987": "Cobresal", "1988": "Colo Colo", "1989": "Colo Colo", "1990": "Colo Colo",
    "1991": "Universidad Católica", "1992": "Unión Española", "1993": "Unión Española", "1994": "Colo Colo",
    "1995": "Universidad Católica", "1996": "Colo Colo", "1998": "Universidad de Chile", "2000": "Universidad de Chile",
    "2008/09": "Universidad de Concepción", "2009": "Unión San Felipe", "2010": "Deportes Iquique", "2011": "Universidad Católica",
    "2012/13": "Universidad de Chile", "2013/14": "Deportes Iquique", "2014/15": "Universidad de Concepción",
    "2015": "Universidad de Chile", "2016": "Colo Colo", "2017": "Santiago Wanderers", "2018": "Palestino", "2019/20": "Colo Colo",
    "2021": "Colo Colo", "2022": "Magallanes", "2023": "Colo Colo", "2024": "Universidad de Chile", "2025": "Huachipato"}

COPA = Copa(slug=SLUG, competicao=COMPETICAO, edicoes=EDICOES, fases=FASES, linhas=linhas, clube=clube, clubes=CLUBES,
            autores=autores, campeoes_wiki=CAMPEOES_WIKI, fonte_pagina="https://www.rsssf.org/tablesc/{pagina}.html",
            fases_pontos=[GRU, GR2, FFIN],
            # D5b: data, hora, estádio, cidade e público da ESPN (chi.copa_chi); Chile UTC-3 no verão (set-mar), UTC-4 no inverno
            espn=espn_arquivos(SLUG, "chi.copa_chi"), espn_corrige=True,
            fuso=lambda utc: utc - timedelta(hours=3 if utc.month in (9, 10, 11, 12, 1, 2, 3) else 4),
            # cobranças de pênaltis da final de 2010 ("1-0 Miguel Ayala;   1-1 Hamilton Ricard;")
            ignorar=[r"^\d{1,2}-\d{1,2}\s+\D+[;,]\s+\d{1,2}-\d{1,2}\s+\D+"])

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    importar(COPA, RELATORIO)
