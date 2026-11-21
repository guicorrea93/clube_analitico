#!/bin/sh
# Prints do painel publicado (uru-1) no Chrome sem janela. Uso: sh revisao/UY/telas.sh <pasta_saida>
OUT="$1"; mkdir -p "$OUT"
CH="C:/Program Files/Google/Chrome/Application/chrome.exe"
PERFIL="$OUT/chrome-perfil"
BASE="https://clubeanalitico.pages.dev/?c=uru-1"
tira() {  # nome rota largura
  "$CH" --headless=new --disable-gpu --user-data-dir="$PERFIL" --window-size="$3",2400 --virtual-time-budget=12000 \
    --hide-scrollbars --screenshot="$OUT/$1.png" "$BASE#$2" >/dev/null 2>&1
}
for s in corrida podio participacoes jogos gols pontos curiosidades; do tira "h_$s" "historia/$s" 1400; done
for e in 2025 1948 1923%20FUF 1977 1994 1908 2005 2024 2013/14; do
  n=$(echo "$e" | sed 's/%20/_/; s#/#-#')
  for s in resumo classificacao participantes jogos artilharia; do tira "c_${n}_$s" "campeonato/$s/$e" 1400; done
done
for cl in penarol nacional montevideo-wanderers river-plate-fc; do
  for s in resumo campanhas confrontos jogos artilharia; do tira "cl_${cl}_$s" "clube/$s/$cl" 1400; done
done
for r in historia/corrida historia/podio campeonato/resumo/2025 campeonato/classificacao/1977 clube/resumo/penarol; do
  n=$(echo "$r" | tr '/' '_'); tira "cel_$n" "$r" 420
done
echo fim
