#!/bin/sh
# Prints do painel LOCAL (ecu-1 ainda não está no site) no Chrome sem janela. Uso: sh revisao/EC/telas.sh <pasta_saida>
OUT="$1"; mkdir -p "$OUT"
CH="C:/Program Files/Google/Chrome/Application/chrome.exe"
PERFIL="$OUT/chrome-perfil"
BASE="file:///C:/Users/guilhermecorrea/Downloads/Gui/GitHub/clube_analitico/painel/index.html?c=ecu-1"
tira() {  # nome rota largura
  "$CH" --headless=new --disable-gpu --user-data-dir="$PERFIL" --window-size="$3",2400 --virtual-time-budget=12000 \
    --hide-scrollbars --screenshot="$OUT/$1.png" "$BASE#$2" >/dev/null 2>&1
}
for s in corrida podio participacoes jogos gols pontos curiosidades; do tira "h_$s" "historia/$s" 1400; done
for e in 1957 1966 1975 1997 1999 2000 2005%20Apertura 2014 2025; do
  n=$(echo "$e" | sed 's/%20/_/')
  for s in resumo classificacao participantes jogos artilharia; do tira "c_${n}_$s" "campeonato/$s/$e" 1400; done
done
for cl in barcelona-de-guayaquil ldu-de-quito; do
  for s in resumo campanhas confrontos jogos artilharia; do tira "cl_${cl}_$s" "clube/$s/$cl" 1400; done
done
for r in historia/podio campeonato/classificacao/2025 clube/resumo/emelec; do
  n=$(echo "$r" | tr '/' '_'); tira "cel_$n" "$r" 420
done
echo fim
