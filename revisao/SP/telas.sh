#!/bin/sh
# Prints do painel publicado. Uso: sh revisao/SP/telas.sh <pasta_saida> <largura> rota1 rota2 ...
OUT="$1"; W="$2"; shift 2
SCR="C:/Users/GUILHE~1/AppData/Local/Temp/claude/c--Users-guilhermecorrea-Downloads-Gui-GitHub/a75361b9-f474-4b01-be59-ef64c90aa262/scratchpad/SP"
for r in "$@"; do
  n=$(echo "$r" | sed 's#[/ %]#_#g')
  "C:/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --disable-gpu --user-data-dir="$SCR/chrome-perfil" \
    --window-size=$W,1800 --virtual-time-budget=10000 --hide-scrollbars --screenshot="$OUT/${W}_$n.png" \
    "https://clubeanalitico.pages.dev/?c=bra-sp-1#$r" 2>/dev/null
done
