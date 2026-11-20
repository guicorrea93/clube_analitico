"""Revisão Série D (SD): baixa páginas da Wikipédia (wikitexto) para data/cache/revisao/SD/.
Uso: python revisao/SD/baixar.py <lingua> "<titulo>" [arquivo]   (ou sem argumentos: todas as edições pt/en/es)
"""
import json, sys, time, re, urllib.request, urllib.parse, pathlib
RAIZ = pathlib.Path(__file__).resolve().parents[2]
CACHE = RAIZ / "data/cache/revisao/SD"
CACHE.mkdir(parents=True, exist_ok=True)
UA = "clube-analitico-revisao/1.0 (uso pessoal)"
_ult = [0.0]

def get(url):
    for tent in range(5):
        espera = 2.1 - (time.time() - _ult[0])
        if espera > 0: time.sleep(espera)
        _ult[0] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print('429, esperando', flush=True); time.sleep(60); continue
            if e.code in (404, 403): return None
            raise
    return None

def wikitexto(lingua, titulo, arq=None):
    nome = arq or (lingua + "_" + re.sub(r"[^\w]+", "_", titulo) + ".txt")
    dest = CACHE / nome
    if dest.exists():
        return dest.read_text(encoding="utf-8")
    url = f"https://{lingua}.wikipedia.org/w/index.php?title={urllib.parse.quote(titulo.replace(' ', '_'))}&action=raw"
    txt = get(url)
    if not txt:
        print("sem página:", lingua, titulo, flush=True); return None
    m = re.match(r"#(?:REDIRECT|REDIRECIONAMENTO|REDIRECCIÓN)\s*\[\[([^\]]+)\]\]", txt.strip(), re.I)
    if m:
        return wikitexto(lingua, m.group(1), arq)
    dest.write_text(f"<!-- {url} -->\n" + txt, encoding="utf-8")
    print("ok", lingua, titulo, len(txt), flush=True)
    return txt

TIT = {
    "pt": ["Campeonato Brasileiro de Futebol de {a} - Série D", "Campeonato Brasileiro de Futebol de {a} – Série D"],
    "en": ["{a} Campeonato Brasileiro Série D"],
}
if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) > 2:
        wikitexto(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    else:
        wikitexto("pt", "Campeonato Brasileiro de Futebol - Série D", "pt_principal.txt")
        wikitexto("en", "Campeonato Brasileiro Série D", "en_principal.txt")
        wikitexto("es", "Campeonato Brasileño de Serie D", "es_principal.txt")
        for a in range(2009, 2027):
            for lg, ms in TIT.items():
                if (CACHE / f"{lg}_{a}.txt").exists(): continue
                for m in ms:
                    if wikitexto(lg, m.format(a=a), f"{lg}_{a}.txt"): break
        for a in range(2009, 2027):
            wikitexto("pt", f"Predefinição:Tabela do Campeonato Brasileiro da Série D - {a}", f"pt_tabela_{a}.txt")
            wikitexto("pt", f"Predefinição:Campeonato Brasileiro de Futebol de {a} - Série D (fase final)", f"pt_fasefinal_{a}.txt")
        wikitexto("pt", "Predefinição:Campeões do Campeonato Brasileiro de Futebol - Série D", "pt_campeoes.txt")
