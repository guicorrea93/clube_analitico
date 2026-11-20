#!/bin/sh
# uso: telas.sh <saida_dir> <largura> <nome> <rota> [altura]
S="$1"; W="$2"; N="$3"; R="$4"; H="${5:-900}"
"C:/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --disable-gpu --user-data-dir="$S/chrome-perfil" --window-size=$W,$H --virtual-time-budget=8000 --hide-scrollbars --screenshot="$S/tela_$N.png" "file:///C:/Users/guilhermecorrea/Downloads/Gui/GitHub/clube_analitico/painel/index.html?c=bra-serie-a#$R" 2>/dev/null
