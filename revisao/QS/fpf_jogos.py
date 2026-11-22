"""FPF (futebolpaulista.com.br, API pública do site): jogos da Série A1 (IdCampeonato 73, categoria 39) de cada ano,
rodada a rodada, e a artilharia oficial. Grava revisao/QS/fpf_jogos.json e revisao/QS/fpf_artilharia.json.
Uso: python -I -X utf8 revisao/QS/fpf_jogos.py [ano ...]   (sem ano: 2007 a 2026)"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from baixar import baixar  # noqa: E402

AQUI = Path(__file__).resolve().parent
B = "https://futebolpaulista.com.br/Handlers/Competicoes"


def pega(url):
    a, s = baixar(url)
    if not a:
        print("falhou", s, url, flush=True)
        return None
    d = json.loads(a.read_text(encoding="utf-8-sig"))
    return d.get("Retorno") if d.get("Sucesso") else None


def main(anos):
    jogos, art = {}, {}
    for ano in anos:
        rods = pega(f"{B}/ListarRodadas.ashx?IdCampeonato=73&Ano={ano}") or []
        lista = []
        for r in rods:
            ret = pega(f"{B}/ListarTabela.ashx?IdCampeonato=73&Ano={ano}&Rodada={r['Rodada']}&IdClube=0&IdCategoria=39")
            for j in (ret or {}).get("listTabela", []):
                lista.append({k: j.get(k) for k in ("IdJogo", "Numero", "Data", "Horario", "Rodada", "Fase", "NumFase",
                                                     "Grupo", "NomePopularMandante", "ResultadoMandante",
                                                     "ResultadoVisitante", "NomePopularVisitante", "NomePopularEstadio",
                                                     "Municipio", "LinkSumula", "LinkBoletimFinanceiro", "Adiado")})
        jogos[str(ano)] = lista
        a = pega(f"{B}/ListarArtilharia.ashx?idCampeonato=73&IdClube=&exercicio={ano}&idCategoria=39&pagina=0&tipoGol=") or []
        art[str(ano)] = [{k: x.get(k) for k in ("AtletaApelido", "AtletaNomeCompleto", "ClubeNomePopular", "Gols", "Ranking")}
                         for x in a if x.get("Ranking", 99) <= 5]
        print(ano, len(rods), "rodadas", len(lista), "jogos", flush=True)
    (AQUI / "fpf_jogos.json").write_text(json.dumps(jogos, ensure_ascii=False, indent=0), encoding="utf-8")
    (AQUI / "fpf_artilharia.json").write_text(json.dumps(art, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main([int(x) for x in sys.argv[1:]] or list(range(2007, 2027)))
