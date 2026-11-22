#!/bin/sh
# Prints do painel PUBLICADO do Alemão (Chrome sem janela). Uso: sh revisao/ES/telas.sh PASTA_SAIDA LARGURA ALTURA rota1 rota2 ...
OUT="$1"; W="$2"; H="$3"; shift 3
CH="C:/Program Files/Google/Chrome/Application/chrome.exe"
mkdir -p "$OUT"
for r in "$@"; do
  n=$(echo "$r" | tr '/#' '__')
  "$CH" --headless=new --disable-gpu --user-data-dir="$OUT/../chrome-perfil" --window-size=$W,$H --virtual-time-budget=10000 \
    --screenshot="$OUT/${W}_$n.png" "https://clubeanalitico.pages.dev/?c=ger-1#$r" 2>/dev/null
done
