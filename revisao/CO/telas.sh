#!/bin/sh
# Prints do painel publicado (col-1) no Chrome sem janela. Uso: sh revisao/CO/telas.sh <pasta_saida>
OUT="$1"; mkdir -p "$OUT"
CH="C:/Program Files/Google/Chrome/Application/chrome.exe"
PERFIL="$OUT/chrome-perfil"
BASE="https://clubeanalitico.pages.dev/?c=col-1"
tira() {  # nome rota largura
  "$CH" --headless=new --disable-gpu --user-data-dir="$PERFIL" --window-size="$3",2400 --virtual-time-budget=12000 \
    --hide-scrollbars --screenshot="$OUT/$1.png" "$BASE#$2" >/dev/null 2>&1
}
for s in corrida podio participacoes jogos gols pontos curiosidades; do tira "h_$s" "historia/$s" 1400; done
for e in 2025%20Finalizaci%C3%B3n 2002%20Apertura 1964 1976 1995 1989 1960; do
  n=$(echo "$e" | sed 's/%20/_/; s/%C3%B3/o/')
  for s in resumo classificacao participantes jogos artilharia; do tira "c_${n}_$s" "campeonato/$s/$e" 1400; done
done
for cl in atletico-nacional millonarios once-caldas; do
  for s in resumo campanhas; do tira "cl_${cl}_$s" "clube/$s/$cl" 1400; done
done
for r in historia/podio campeonato/classificacao/2002%20Apertura; do
  n=$(echo "$r" | tr '/%' '__'); tira "cel_$n" "$r" 420
done
echo fim
