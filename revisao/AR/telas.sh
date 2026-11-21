#!/bin/sh
# Prints do painel publicado (arg-1). Uso: sh revisao/AR/telas.sh <pasta_saida> <largura> <lista de rotas...>
OUT="$1"; W="$2"; shift 2
CH="C:/Program Files/Google/Chrome/Application/chrome.exe"
PERFIL="C:/Users/GUILHE~1/AppData/Local/Temp/claude/c--Users-guilhermecorrea-Downloads-Gui-GitHub/a75361b9-f474-4b01-be59-ef64c90aa262/scratchpad/AR/chrome-perfil"
for r in "$@"; do
  f=$(echo "$r" | sed 's#[/ %]#_#g')
  "$CH" --headless=new --disable-gpu --user-data-dir="$PERFIL" --window-size=$W,1800 --virtual-time-budget=9000 --hide-scrollbars \
    --screenshot="$OUT/${W}_$f.png" "https://clubeanalitico.pages.dev/?c=arg-1#$r" 2>/dev/null
  echo "$OUT/${W}_$f.png"
done
