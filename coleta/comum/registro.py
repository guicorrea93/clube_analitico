"""Cadastro comum de clubes das coletas: código do clube no ogol -> nome de exibição, UF e cidade.

Garante que o mesmo clube tenha o mesmo nome em todos os pacotes (Série C, Série D, estaduais...).
Fica em data/coleta/comum/clubes_ogol.json. Cada coleta lê o cadastro antes de dar nome a um clube e,
ao gravar o pacote, acrescenta os clubes novos.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent.parent.parent / "data" / "coleta" / "comum" / "clubes_ogol.json"


# grafias de cidade da ficha do ogol que a regra de cidade_pt não resolve (achado CL-028)
CIDADE_GRAFIA = {"Divinopolis": "Divinópolis", "Alegre - Espirito Santo": "Alegre"}


def cidade_pt(cidade: str | None) -> str | None:
    """Cidade como se escreve em português: "de/do/da/dos/das" minúsculos no meio do nome ("Limoeiro Do Norte" ->
    "Limoeiro do Norte"; a ficha do ogol põe maiúscula) e as grafias de CIDADE_GRAFIA (achado CL-028)."""
    if not cidade:
        return cidade
    cidade = re.sub(r"(?<=\s)(De|Do|Da|Dos|Das)(?=\s)", lambda m: m.group(1).lower(), cidade.strip())
    return CIDADE_GRAFIA.get(cidade, cidade)


# ficha do ogol corrigida para todas as coletas: código -> (campos certos, motivo) (achado CL-028)
FICHA_COMUM: dict[str, tuple[dict, str]] = {
    "3272": ({"uf": "DF", "cidade": "Guará"}, "Botafogo-DF (ex-Esportivo Guará): sediado no Guará (DF) nos anos em que jogou "
                                              "(2007-2010; Bola n@ Área: 'Botafogo (DF)'); só depois foi para Novo Gama (GO)"),
    "94274": ({"cidade": "Água Boa"}, "AA Araguaia (2014, substituta do Barra do Garças FC): Água Boa (MT), não Cuiabá"),
    "44231": ({"cidade": "Nova Serrana"}, "Nacional Esporte Clube Ltda, de Nova Serrana (RSSSF, Mineiro 2012); a ficha do ogol "
                                          "diz Muriaé, a cidade do Nacional Atlético Clube, outro clube"),
    "86201": ({"uf": "MG", "cidade": "Belo Horizonte"},
              "Grêmio Ludopédio Calafate, de Belo Horizonte (Mineiro 1932 AMEG); a ficha do ogol é a do Grêmio Calafate de "
              "Rio Branco (AC)"),
}


def corrigir_ficha(f: dict) -> dict:
    """Aplica FICHA_COMUM e a grafia da cidade (cidade_pt) a uma ficha do ogol (com "id")."""
    f.update(FICHA_COMUM.get(str(f.get("id")), ({}, ""))[0])
    f["cidade"] = cidade_pt(f.get("cidade"))
    return f


def ler() -> dict[str, dict]:
    return json.loads(ARQUIVO.read_text(encoding="utf-8")) if ARQUIVO.exists() else {}


def acrescentar(clubes: dict[str, dict], slug: str) -> None:
    """clubes: código -> {clube, uf, cidade}. Não troca o nome de quem já está no cadastro."""
    reg = ler()
    for i, c in clubes.items():
        atual = reg.setdefault(i, {"clube": c["clube"], "uf": c.get("uf"), "cidade": c.get("cidade"), "competicoes": []})
        atual.update(FICHA_COMUM.get(i, ({}, ""))[0])
        atual["cidade"] = cidade_pt(atual.get("cidade"))
        if slug not in atual["competicoes"]:
            atual["competicoes"].append(slug)
    ARQUIVO.parent.mkdir(parents=True, exist_ok=True)
    ARQUIVO.write_text(json.dumps(dict(sorted(reg.items())), ensure_ascii=False, indent=1), encoding="utf-8")
