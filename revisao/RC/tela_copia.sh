#!/bin/sh
# Print da CÓPIA do site (index.html e dados/*.js baixados do site, em SCRATCH/RC/sitecopia), com clique na parte das curiosidades.
# uso: sh revisao/RC/tela_copia.sh <nome> <slug> <parte> [rota]
S=C:/Users/GUILHE~1/AppData/Local/Temp/claude/c--Users-guilhermecorrea-Downloads-Gui-GitHub/a75361b9-f474-4b01-be59-ef64c90aa262/scratchpad/RC
CH="C:/Program Files/Google/Chrome/Application/chrome.exe"
URL="file:///$S/sitecopia/index.html?c=$2&parte=$3#${4:-historia/curiosidades}"
"$CH" --headless=new --disable-gpu --user-data-dir=$S/chrome-perfil --window-size=1400,1800 --virtual-time-budget=9000 --allow-file-access-from-files --screenshot=$S/telas/$1.png "$URL" >/dev/null 2>&1
"$CH" --headless=new --disable-gpu --user-data-dir=$S/chrome-perfil --window-size=1400,1800 --virtual-time-budget=9000 --allow-file-access-from-files --dump-dom "$URL" > $S/telas/$1.html 2>/dev/null
echo "$1 $(wc -c < $S/telas/$1.html)"
