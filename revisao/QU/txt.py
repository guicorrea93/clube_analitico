"""Mostra o texto de uma página HTML do cache (uso: python -I revisao/QU/txt.py arquivo [termo] [n])."""
import re, html, sys
sys.stdout.reconfigure(encoding="utf-8")
f = sys.argv[1]; termo = sys.argv[2] if len(sys.argv) > 2 else ""; n = int(sys.argv[3]) if len(sys.argv) > 3 else 3000
b = open(f, "rb").read()
try: t = b.decode("utf-8")
except UnicodeDecodeError: t = b.decode("latin-1")
t = re.sub(r"(?s)<script.*?</script>", "", t); t = re.sub(r"(?s)<style.*?</style>", "", t)
s = re.sub(r"<[^>]+>", " ", t); s = html.unescape(s); s = re.sub(r"\s+", " ", s)
i = s.find(termo) if termo else 0
print(s[max(i, 0):max(i, 0) + n])
