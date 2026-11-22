#!/bin/sh
# Prints do painel publicado (par-1) no Chrome sem janela. Uso: sh revisao/PY/telas.sh <pasta_saida>
OUT="$1"; mkdir -p "$OUT"
CH="C:/Program Files/Google/Chrome/Application/chrome.exe"
PERFIL="$OUT/chrome-perfil"
BASE="https://clubeanalitico.pages.dev/?c=par-1"
tira() {  # nome rota largura
  "$CH" --headless=new --disable-gpu --user-data-dir="$PERFIL" --window-size="$3",2000 --virtual-time-budget=12000 \
    --hide-scrollbars --screenshot="$OUT/$1.png" "$BASE#$2" >/dev/null 2>&1
}
for s in podio corrida participacoes curiosidades; do tira "h_$s" "historia/$s" 1400; done
for e in 1917 1928 1989 1991 1962 1999 2020%20Clausura 2025%20Clausura; do
  n=$(echo "$e" | sed 's/%20/_/')
  for s in resumo classificacao jogos; do tira "c_${n}_$s" "campeonato/$s/$e" 1400; done
done
for r in historia/podio campeonato/classificacao/1917 campeonato/resumo/2025%20Clausura; do
  n=$(echo "$r" | tr '/' '_' | sed 's/%20/_/'); tira "cel_$n" "$r" 420
done
echo fim
