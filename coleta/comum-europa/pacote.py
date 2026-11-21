"""Grava o pacote de uma competição no formato de docs/agente-coleta-COMECE-AQUI.md (seção 4).

Extras deste agente (o carregador ignora colunas e arquivos que não conhece):
- partidas.csv ganha a coluna `arbitro`;
- estatisticas.csv: números de cada clube no jogo (chutes, chutes no alvo, faltas, escanteios, cartões), no molde
  da tabela estatistica_partida do banco.

Uso como biblioteca: gravar(pasta, competicao, tabelas) com tabelas = {"partidas": [dict, ...], ...}
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

CAMPOS = {
    "paises": "codigo,nome,confederacao",
    "clubes": "clube,regiao,cidade,pais,nomes_fonte",
    "edicoes": "temporada,ano_inicio,ano_fim,nome_oficial,num_clubes,pontos_vitoria,formato,campeao,vice,fontes,observacao",
    "fases": "temporada,ordem,fase,tipo,num_grupos,formato_serie,criterio",
    "partidas": "id,temporada,fase,grupo,rodada,data,hora,mandante,visitante,gols_mandante,gols_visitante,penaltis_mandante,"
                "penaltis_visitante,resultado_especial,estadio,cidade,publico,fonte,fonte_id,gols_texto,observacao,arbitro",
    "gols": "partida_id,clube,jogador,minuto,acrescimo,tipo,fonte",
    "cartoes": "partida_id,clube,jogador,minuto,acrescimo,cor,fonte",
    "estatisticas": "partida_id,clube,chutes,chutes_alvo,faltas,escanteios,amarelos,vermelhos,fonte",
    "classificacao_final": "temporada,posicao,clube,jogos,vitorias,empates,derrotas,gols_pro,gols_contra,pontos,ajuste_pontos,"
                           "situacao,fonte,observacao",
    "classificacao_rodada": "temporada,rodada,clube,posicao,pontos,jogos,vitorias,empates,derrotas,gols_pro,gols_contra,zona",
    "tabelas_publicadas": "temporada,fase,grupo,posicao,nome_fonte,clube,jogos,vitorias,empates,derrotas,gols_pro,gols_contra,"
                          "pontos,fonte",
    "artilheiros": "temporada,jogador,clube,gols,fonte",
    "conferencia": "temporada,jogos,jogos_esperados,tabelas_conferidas,tabelas_divergentes,gols,gols_com_autor,observacao",
}


def gravar(pasta: Path, competicao: dict, tabelas: dict[str, list[dict]]) -> None:
    pasta.mkdir(parents=True, exist_ok=True)
    (pasta / "competicao.json").write_text(json.dumps(competicao, ensure_ascii=False, indent=1), encoding="utf-8")
    for nome, campos in CAMPOS.items():
        linhas = tabelas.get(nome)
        if linhas is None:
            continue
        with (pasta / f"{nome}.csv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=campos.split(","), extrasaction="raise")
            w.writeheader()
            for l in linhas:
                w.writerow({k: ("" if v is None else v) for k, v in l.items()})
