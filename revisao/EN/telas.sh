#!/bin/bash
# Prints do painel publicado (eng-1), computador e celular. Uso: bash revisao/EN/telas.sh <pasta de saída>
OUT="$1"; mkdir -p "$OUT"
CH="C:/Program Files/Google/Chrome/Application/chrome.exe"
BASE="https://clubeanalitico.pages.dev/?c=eng-1#"
ROTAS="historia/corrida historia/participacoes historia/jogos historia/gols historia/pontos historia/podio historia/curiosidades
campeonato/resumo/2024/25 campeonato/classificacao/2024/25 campeonato/corrida/2024/25 campeonato/jogos/2024/25 campeonato/participantes/2024/25 campeonato/artilharia/2024/25
campeonato/resumo/1888/89 campeonato/classificacao/1888/89 campeonato/participantes/1888/89 campeonato/artilharia/1888/89 campeonato/jogos/1888/89 campeonato/corrida/1888/89
campeonato/classificacao/2023/24 campeonato/classificacao/1990/91 campeonato/classificacao/1890/91 campeonato/participantes/1914/15 campeonato/participantes/1938/39 campeonato/participantes/1946/47 campeonato/participantes/1987/88 campeonato/participantes/1889/90 campeonato/resumo/1939/40 campeonato/resumo/1956/57 campeonato/corrida/2023/24
clube/resumo/arsenal clube/campanhas/arsenal clube/confrontos/arsenal clube/jogos/arsenal clube/artilharia/arsenal clube/resumo/birmingham clube/campanhas/manchester-united clube/resumo/cardiff clube/artilharia/accrington"
i=0
for r in $ROTAS; do
  i=$((i+1)); n=$(printf "%02d" $i)_$(echo "$r" | tr '/' '_')
  "$CH" --headless=new --disable-gpu --user-data-dir="$OUT/../chrome-perfil" --window-size=1400,2400 --virtual-time-budget=9000 --hide-scrollbars --screenshot="$OUT/pc_$n.png" "$BASE$r" 2>/dev/null
  "$CH" --headless=new --disable-gpu --user-data-dir="$OUT/../chrome-perfil" --window-size=420,2400 --virtual-time-budget=9000 --hide-scrollbars --screenshot="$OUT/cel_$n.png" "$BASE$r" 2>/dev/null
done
echo fim
