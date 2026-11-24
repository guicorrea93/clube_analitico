"""Copa Argentina (arg-copa): copa nacional da AFA. Quinta das sete copas da América do Sul (decisões do Guilherme de
24/11/2026 em coleta/comum-sulamerica/copas-nacionais.md): contagem da Wikipédia em espanhol, que conta 1969, 1970
(inacabada: a final de volta nunca foi jogada, sem campeão) e de 2011/12 em diante (2021 não houve: a de 2019/20 terminou
em dezembro de 2021). Das edições modernas entra só a fase final (decisão de 24/11): dos 32-avos de final em diante; as
fases regionais e preliminares do interior ficam de fora (2012/13 e 2013/14 entram como a RSSSF chama a "Final phase",
com uma fase preliminar e uma primeira fase antes dos 16-avos).

Fontes (um importador comum: coleta/comum-sulamerica/copa_rsssf.py):
- RSSSF: argcup69.html e argcup70.html (em data/coleta/arg-copa/rsssf/) e a seção da copa nas páginas do ano do arg-1
  (arg2012 ... arg2025, em data/coleta/arg-1/rsssf/);
- campeão conferido com a Wikipédia em espanhol ("Copa Argentina"); as páginas de 2016-17, 2022, 2024 e 2025 (em
  data/coleta/arg-copa/wikipedia/) desfazem homônimos (clubes_copa.py).

Uso: python coleta/arg-copa/importar.py
"""
from __future__ import annotations

import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(AQUI.parent / "comum-sulamerica"))
sys.path.insert(1, str(AQUI.parent / "arg-1"))
import autores  # noqa: E402  (o do arg-1)
import ler_rsssf  # noqa: E402  (o do arg-1: páginas em data/coleta/arg-1/rsssf)
import rsssf_sul  # noqa: E402
from clubes_copa import CLUBES, clube  # noqa: E402
from copa_rsssf import Copa, EdicaoCopa, importar  # noqa: E402

SLUG = "arg-copa"
RELATORIO = RAIZ / "docs" / "coleta" / f"{SLUG}.md"
PASTA = RAIZ / "data" / "coleta" / SLUG / "rsssf"


def linhas(pagina: str) -> tuple[str, ...]:
    return tuple(rsssf_sul.texto(PASTA / f"{pagina}.html")) if pagina.startswith("argcup") else ler_rsssf.linhas(pagina)


T32, T24, T16 = "Trinta-e-dois-avos de final", "Vinte-e-quatro-avos de final", "Dezesseis-avos de final"
OIT, QUA, SEM, FIN = "Oitavas de final", "Quartas de final", "Semifinal", "Final"
# ordem geral das fases (a última é a final); os títulos de cada página estão nas listas por edição, abaixo
FASES = [(r"^NUNCA$", f) for f in ("Fase regional", "Fase preliminar", "Primeira fase", "Segunda fase", T32, T24, T16, OIT, QUA, SEM)]
FASES.append((r"^Final\b", FIN))
F_1969 = [(r"^Region [B-D]:", "Fase regional"), (r"^Group [A-H]:", "Segunda fase"), (r"^Quarter-finals", QUA),
          (r"^Semi-finals", SEM), (r"^Final:", FIN)]
F_1970 = [(r"^1st Round", "Primeira fase"), (r"^2nd Round", "Segunda fase"), (r"^Quarterfinals", QUA), (r"^Semifinals", SEM),
          (r"^Final:", FIN)]
F_PAG = {
    "arg2012": [(r"^32° Final", T32), (r"^16° Final", T16), (r"^8° Final", OIT), (r"^Quarterfinals", QUA), (r"^Semifinals", SEM),
                (r"^Final$", FIN)],
    "arg2013": [(r"^Preliminary round", "Fase preliminar"), (r"^1/24 final", T24), (r"^1/16 final", T16), (r"^1/8 final", OIT),
                (r"^Quarterfinal", QUA), (r"^Semifinal", SEM), (r"^Final$", FIN)],
    "arg2014": [(r"^I Round", "Primeira fase"), (r"^II Round", "Segunda fase"), (r"^16ths final", T16), (r"^8ths final", OIT),
                (r"^Quarter finals", QUA), (r"^Semi finals", SEM), (r"^Final \[", FIN)],
    "arg2015": [(r"^1/32 Finals", T32), (r"^1/16 Finals", T16), (r"^1/8 finals", OIT), (r"^Quarterfinals", QUA),
                (r"^Semi-finals", SEM), (r"^Final\.", FIN)],
    "arg2016": [(r"^Round 3:", T32), (r"^Round 4:", T16), (r"^Round 5:", OIT), (r"^Round 6:", QUA), (r"^Round 7", SEM),
                (r"^Round 8", FIN)],
    "arg2017": [(r"^3\.1\.", T32), (r"^3\.2\.", T16), (r"^3\.3\.", OIT), (r"^3\.4\.", QUA), (r"^3\.5\.", SEM), (r"^3\.6\.", FIN)],
    "arg2018": [(r"^32nd-finals", T32), (r"^16th-finals", T16), (r"^8th-finals", OIT), (r"^Quarter ?-finals", QUA),
                (r"^Semi-finals", SEM), (r"^Final$", FIN)],
}
F_ROUND = [(r"^Round of 64", T32), (r"^Round of 32", T16), (r"^Round of 16", OIT), (r"^Quarter[- ]?finals", QUA),
           (r"^Semi[- ]?finals", SEM), (r"^Final:?$", FIN)]

# (página, 1ª linha (título da 1ª fase), linha final (exclusiva: antes das escalações da final ou das tabelas), título esperado)
TRECHOS = {
    "arg2012": (1017, 1130, "32° Final"), "arg2013": (1037, 1161, "Preliminary round"), "arg2014": (1226, 1326, "I Round"),
    "arg2015": (1001, 1188, "1/32 Finals"), "arg2016": (807, 929, "Round 3:"), "arg2017": (981, 1097, "3.1. Round of 64"),
    "arg2018": (805, 929, "32nd-finals"), "arg2019": (788, 908, "Round of 64"), "arg2020": (1206, 1335, "Round of 64"),
    "arg2022": (1112, 1228, "Round of 64"), "arg2023": (1200, 1317, "Round of 64"), "arg2024": (1162, 1285, "Round of 64"),
    "arg2025": (1111, 1232, "Round of 64"),
}


def _trecho(pagina: str) -> tuple[str, int, int]:
    ini, fim, titulo = TRECHOS[pagina]
    assert linhas(pagina)[ini].strip().startswith(titulo), (pagina, linhas(pagina)[ini])
    return pagina, ini, fim


def _ate(pagina: str, fim: str) -> tuple[str, int, int]:
    ls = linhas(pagina)
    return pagina, 0, next(i for i, l in enumerate(ls) if l.strip().startswith(fim))


def _partes_69() -> list[tuple[str, int, int]]:
    """1969 em trechos: cada região volta a dezembro (a página não está em ordem de data) e o leitor só vira o ano para
    a frente; lidas em separado, dezembro fica em 1969 e janeiro em 1970."""
    _, _, fim = _ate("argcup69", "Atlanta, as runner-up")
    ls = linhas("argcup69")
    cortes = [0] + [next(i for i, l in enumerate(ls) if l.strip() == t) for t in ("Region B:", "Region C:", "Region D:", "Group A:")]
    return [("argcup69", a, b) for a, b in zip(cortes, cortes[1:] + [fim])]


_SO_FINAL = "só a fase final (dos 32-avos em diante); as fases regionais e preliminares do interior ficam de fora"
_REGIOES_69 = [(r"^Argentina - Copa", "A"), (r"^Region B:", "B"), (r"^Region C:", "C"), (r"^Region D:", "D")] + [
    (rf"^Group {g}:", g) for g in "ABCDEFGH"]
EDICOES = [
    EdicaoCopa("1969", 1969, 1970, "Copa Argentina 1969", _partes_69(), fases=F_1969,
               regioes=_REGIOES_69, fim_regiao=r"^Quarter-finals", fase_padrao="Fase regional",
               obs="vaga na Recopa Sudamericana 1970; sem os três clubes da Libertadores de 1969 (Estudiantes, River Plate e "
                   "Vélez Sarsfield); fase regional do interior (regiões A a D) e segunda fase em chaves A a H, todas em mata-mata"),
    EdicaoCopa("1970", 1970, 1971, "Copa Argentina 1970", [_ate("argcup70", "This cup was disputed")], fases=F_1970,
               anos_leitura=(1970, 1970),
               obs="inacabada: a final de volta (San Lorenzo x Vélez Sarsfield) nunca foi jogada; sem campeão"),
]
for _p, (_a, _ob) in {"arg2012": (2011, ""), "arg2013": (2012, "a fase final da RSSSF começa com uma fase preliminar e "
                                                         "os 24-avos de final"),
                      "arg2014": (2013, "a fase final da RSSSF começa com duas rodadas antes dos 16-avos de final"),
                      "arg2015": (2014, ""), "arg2016": (2015, ""), "arg2017": (2016, ""), "arg2018": (2017, ""),
                      "arg2019": (2018, ""), "arg2020": (2019, "jogada de fevereiro de 2020 a dezembro de 2021 (parada pela "
                                                              "pandemia); não houve edição de 2021")}.items():
    EDICOES.append(EdicaoCopa(f"{_a}/{(_a + 1) % 100:02d}", _a, _a + 1 if _a != 2019 else 2021,
                              f"Copa Argentina {_a}-{(_a + 1) % 100:02d}", [_trecho(_p)], fases=F_PAG.get(_p, F_ROUND),
                              obs="; ".join(o for o in (_SO_FINAL, _ob) if o),
                              anos_leitura=(2019, 2020) if _a == 2019 else None))
for _a in (2022, 2023, 2024, 2025):
    EDICOES.append(EdicaoCopa(str(_a), _a, _a, f"Copa Argentina {_a}", [_trecho(f"arg{_a}")], fases=F_ROUND, obs=_SO_FINAL))

COMPETICAO = {
    "slug": SLUG, "nome": "Copa Argentina", "nome_curto": "Copa Argentina", "tipo": "copa", "nivel": None, "pais": "ARG",
    "pais_nome": "Argentina", "regiao": None, "confederacao": "CONMEBOL", "rotulo_painel": "Copa Argentina",
    "menu_painel": "Argentina · Copa Argentina", "do_painel": "da Copa Argentina", "o_painel": "a Copa Argentina",
    "observacao": "Copa nacional da AFA: 1969, 1970 (inacabada, sem campeão) e de 2011/12 em diante. Das edições modernas "
                  "só a fase final (dos 32-avos de final em diante), sem as fases regionais do interior."}

# Wikipédia em espanhol, "Copa Argentina" (Palmarés)
CAMPEOES_WIKI = {"1969": "Boca Juniors", "2011/12": "Boca Juniors", "2012/13": "Arsenal de Sarandí", "2013/14": "Huracán",
                 "2014/15": "Boca Juniors", "2015/16": "River Plate", "2016/17": "River Plate", "2017/18": "Rosario Central",
                 "2018/19": "River Plate", "2019/20": "Boca Juniors", "2022": "Patronato", "2023": "Estudiantes",
                 "2024": "Central Córdoba (Santiago del Estero)", "2025": "Independiente Rivadavia"}

COPA = Copa(slug=SLUG, competicao=COMPETICAO, edicoes=EDICOES, fases=FASES, linhas=linhas, clube=clube, clubes=CLUBES,
            autores=autores, campeoes_wiki=CAMPEOES_WIKI, fonte_pagina="https://www.rsssf.org/tablesa/{pagina}.html",
            trocas=[(r"^\[(\w{3} \d{1,2}),? (?:Mo|Tu|We|Th|Fr|Sa|Su)\]\s*$", r"[\1]")])   # "[Mar 18 We]" (arg2015)

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    importar(COPA, RELATORIO)
