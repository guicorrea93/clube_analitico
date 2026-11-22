"""ogol: lê a ficha de jogo (autores dos gols, árbitro, estádio, público quando houver).

Uso: python -I revisao/QA/ogol.py <url da ficha> [...]
"""
import html, io, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import baixar


def texto(t):
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    return re.sub(r"\n\s*\n+", "\n", html.unescape(re.sub(r"<[^>]+>", "\n", t)))


def ficha(url):
    t = baixar.baixar(url).decode("utf-8", "replace")
    r = {"url": url}
    # árbitro: link /arbitro/...
    m = re.search(r'href="/arbitro/[^"]*"[^>]*>([^<]+)</a>', t)
    r["arbitro"] = html.unescape(m.group(1)).strip() if m else None
    m = re.search(r'href="/estadio/[^"]*"[^>]*>([^<]+)</a>', t)
    r["estadio"] = html.unescape(m.group(1)).strip() if m else None
    m = re.search(r"(?:Público|Espectadores|Assistência)\D{0,40}?([\d][\d\. ]{2,})", texto(t))
    r["publico"] = int(re.sub(r"\D", "", m.group(1))) if m else None
    # gols: na ficha, os eventos de gol aparecem com ícone 'icn_goal' perto do nome do jogador
    gols = re.findall(r'<a href="/jogador/[^"]*"[^>]*>([^<]+)</a>\s*</div>\s*<div[^>]*>\s*<span[^>]*>\s*(\d+)\'', t)
    r["gols_html"] = gols
    return r, texto(t)


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    for u in sys.argv[1:]:
        r, tx = ficha(u)
        print(r)
        i = tx.find("Resumo")
        print(tx[i:i + 1500].replace("\n", " | "))
