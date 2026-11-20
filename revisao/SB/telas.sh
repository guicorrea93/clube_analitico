#!/bin/sh
# Prints do painel da Série B (Chrome sem janela). Uso: sh revisao/SB/telas.sh PASTA_SAIDA LARGURA rota1 rota2 ...
OUT="$1"; W="$2"; shift 2
CH="C:/Program Files/Google/Chrome/Application/chrome.exe"
for r in "$@"; do
  n=$(echo "$r" | tr '/#' '__')
  "$CH" --headless=new --disable-gpu --user-data-dir="$OUT/../chrome-perfil" --window-size=$W,1800 --virtual-time-budget=8000 \
    --screenshot="$OUT/${W}_$n.png" "file:///C:/Users/guilhermecorrea/Downloads/Gui/GitHub/clube_analitico/painel/index.html?c=bra-serie-b#$r" 2>/dev/null
done
