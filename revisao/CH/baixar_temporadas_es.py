"""Baixa (com cache) as páginas de temporada da Wikipédia em espanhol listadas na seção Historial de
"Primera División de Chile" (data/cache/revisao/CH/es_Primera_Division_de_Chile.txt). Uso: python -I revisao/CH/baixar_temporadas_es.py"""
import re, sys
sys.path.insert(0, "revisao/CH")
import baixar
t = open("data/cache/revisao/CH/es_Primera_Division_de_Chile.txt", encoding="utf-8").read()
sec = t[t.index("== Historial =="):t.index("== Palmarés ==")]
for titulo, rot in re.findall(r"\| align=center \| \[\[([^|\]]+)\|([^\]]+)\]\]", sec):
    if "2026" in rot:
        continue
    nome = "es_temp_" + re.sub(r"[^A-Za-z0-9]+", "_", rot) + ".txt"
    try:
        print(baixar.wiki("es", titulo, nome))
    except Exception as e:
        print("ERRO", titulo, e)
for extra in ["Anexo:Goleadores de la Primera División de Chile", "Anexo:Máximos goleadores de la Primera División de Chile"]:
    try:
        print(baixar.wiki("es", extra))
    except Exception as e:
        print("ERRO", extra, e)
