#!/bin/sh
# uso: sh revisao/RC/tela.sh <nome> "<rota depois de ?c=>" [largura]   (site publicado)
S=C:/Users/GUILHE~1/AppData/Local/Temp/claude/c--Users-guilhermecorrea-Downloads-Gui-GitHub/a75361b9-f474-4b01-be59-ef64c90aa262/scratchpad/RC
mkdir -p $S/telas
W=${3:-1400}
CH="C:/Program Files/Google/Chrome/Application/chrome.exe"
URL="https://clubeanalitico.pages.dev/?c=$2"
"$CH" --headless=new --disable-gpu --user-data-dir=$S/chrome-perfil --window-size=$W,1800 --virtual-time-budget=9000 --screenshot=$S/telas/$1.png "$URL" >/dev/null 2>&1
"$CH" --headless=new --disable-gpu --user-data-dir=$S/chrome-perfil --window-size=$W,1800 --virtual-time-budget=9000 --dump-dom "$URL" > $S/telas/$1.html 2>/dev/null
echo "$1 $(wc -c < $S/telas/$1.html)"
