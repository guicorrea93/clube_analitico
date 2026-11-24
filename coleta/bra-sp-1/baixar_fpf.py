"""Baixa da API pública do site da FPF (futebolpaulista.com.br) os jogos da Série A1 (IdCampeonato 73, categoria 39)
de cada ano, rodada a rodada, e a artilharia oficial. Grava data/coleta/bra-sp-1/fpf/jogos_{ano}.json e
artilharia_{ano}.json; as respostas cruas ficam em data/cache/fpf_sp1/ (não baixa de novo).
É a fonte oficial de data, hora, fase e grupo de 2007 em diante (achados QS-008, SP-008, SP-004 e SP-023 da revisão).
Uso: python coleta/bra-sp-1/baixar_fpf.py [ano ...]   (sem ano: 2007 a 2026)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "comum"))
sys.path.insert(0, str(AQUI))
from baixar import pegar  # noqa: E402
from edicoes import PASTA_DADOS, RAIZ  # noqa: E402

PASTA = PASTA_DADOS / "fpf"
CACHE = RAIZ / "data" / "cache" / "fpf_sp1"
API = "https://futebolpaulista.com.br/Handlers/Competicoes"
CAMPOS = ("IdJogo", "Numero", "Data", "Horario", "Rodada", "Fase", "NumFase", "Grupo", "NomePopularMandante",
          "ResultadoMandante", "ResultadoVisitante", "NomePopularVisitante", "NomePopularEstadio", "Municipio", "Adiado")


def api(url: str, nome: str):
    dados = pegar(url, CACHE / f"{nome}.json")
    if not dados:
        return None
    d = json.loads(dados.decode("utf-8-sig"))
    return d.get("Retorno") if d.get("Sucesso") else None


def baixar(ano: int) -> None:
    rodadas = api(f"{API}/ListarRodadas.ashx?IdCampeonato=73&Ano={ano}", f"rodadas_{ano}") or []
    jogos = []
    for r in rodadas:
        ret = api(f"{API}/ListarTabela.ashx?IdCampeonato=73&Ano={ano}&Rodada={r['Rodada']}&IdClube=0&IdCategoria=39",
                  f"tabela_{ano}_{r['Rodada']}") or {}
        jogos += [{k: j.get(k) for k in CAMPOS} for j in ret.get("listTabela", [])]
    art = api(f"{API}/ListarArtilharia.ashx?idCampeonato=73&IdClube=&exercicio={ano}&idCategoria=39&pagina=0&tipoGol=",
              f"artilharia_{ano}") or []
    art = [{k: x.get(k) for k in ("AtletaApelido", "AtletaNomeCompleto", "ClubeNomePopular", "Gols", "Ranking")} for x in art]
    PASTA.mkdir(parents=True, exist_ok=True)
    (PASTA / f"jogos_{ano}.json").write_text(json.dumps(jogos, ensure_ascii=False, indent=0), encoding="utf-8")
    (PASTA / f"artilharia_{ano}.json").write_text(json.dumps(art, ensure_ascii=False, indent=0), encoding="utf-8")
    print(f"{ano}: {len(rodadas)} rodadas, {len(jogos)} jogos, {len(art)} na artilharia", flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for a in [int(x) for x in sys.argv[1:]] or range(2007, 2027):
        baixar(a)
