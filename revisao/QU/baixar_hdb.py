"""Baixa as campanhas do Boca Juniors (historiadeboca.com.ar) dos anos pedidos, para conferir datas e placares do arg-1.

Uso: python -I revisao/QU/baixar_hdb.py 1919 1924 ...   (só baixa o que não está no cache)
Cache: data/cache/revisao/QU/hdb/  (anios_<ano>.html, camp_<ano>_<id>.html, url_<ano>_<id>.txt)
Educado: 1 pedido a cada 2,5 s, User-Agent identificável, 429 -> espera 60 s.
"""
import re, sys, time, urllib.request, urllib.parse
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = Path(__file__).resolve().parent.parent.parent
CACHE = RAIZ / "data" / "cache" / "revisao" / "QU" / "hdb"
CACHE.mkdir(parents=True, exist_ok=True)
UA = "clube-analitico-revisao/1.0 (uso pessoal)"
BASE = "https://historiadeboca.com.ar/"
ESPERA = 2.5
_ult = [0.0]

# torneios de liga (o resto: copas, amistosos, internacionais, fica de fora)
FORA = re.compile(r"Amistos|Libertadores|Sudamericana|Recopa|Intercontinental|Supercopa|Copa Argentina|Copa de la Liga|"
                  r"Copa Competencia|Copa Ibarguren|Mundial|Conmebol|Master|Merconorte|Mercosur|Copa Escobar|Copa Dr|"
                  r"Copa Adri|Copa Beccar|Copa Estimulo|Copa Est.mulo|Copa Uruguaya|Copa Rio|Copa Jockey|Copa Montevideo|"
                  r"Pre ?Libertadores|Liguilla|Copa de Oro|Copa Suruga|Copa Campe.n|Trofeo|Copa Centenario|Campeonato Sudamericano|"
                  r"Copa Aldao|Copa Chevallier|Copa Bullrich|Copa Ganador|Copa Hospital|Copa Presidente", re.I)


def pedir(url: str, dados: bytes | None = None, seguir: bool = True) -> tuple[int, bytes, str]:
    for tentativa in range(3):
        espera = ESPERA - (time.time() - _ult[0])
        if espera > 0:
            time.sleep(espera)
        _ult[0] = time.time()
        req = urllib.request.Request(url, data=dados, headers={"User-Agent": UA})
        if not seguir:
            class SemRedir(urllib.request.HTTPRedirectHandler):
                def redirect_request(self, *a, **k):
                    return None
            op = urllib.request.build_opener(SemRedir)
        else:
            op = urllib.request.build_opener()
        try:
            r = op.open(req, timeout=40)
            return r.status, r.read(), r.geturl()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(60)
                continue
            return e.code, e.read() if e.fp else b"", e.headers.get("Location", "") or ""
    return 429, b"", ""


def torneios(ano: int) -> list[tuple[str, str]]:
    f = CACHE / f"anios_{ano}.html"
    if not f.exists():
        st, b, _ = pedir(f"{BASE}anios-campeonatos.php?anios={ano}")
        f.write_bytes(b)
    t = f.read_bytes().decode("utf-8", "replace")
    return re.findall(r"<option value='(\d+)'>([^<]+)</option>", t)


def campanha(ano: int, tid: str) -> Path | None:
    f = CACHE / f"camp_{ano}_{tid}.html"
    if f.exists():
        return f
    fu = CACHE / f"url_{ano}_{tid}.txt"
    if not fu.exists():
        st, _, loc = pedir(f"{BASE}validarcamp.php", urllib.parse.urlencode({"anios": ano, "comboCampeonato": tid}).encode(), seguir=False)
        if not loc:
            print("sem redirecionamento", ano, tid, st)
            return None
        fu.write_text(urllib.parse.urljoin(BASE, loc), encoding="utf-8")
    url = fu.read_text(encoding="utf-8").strip()
    st, b, _ = pedir(urllib.parse.quote(url, safe=":/%"))
    if st != 200:
        print("erro", st, url)
        return None
    f.write_bytes(b)
    return f


if __name__ == "__main__":
    for a in sys.argv[1:]:
        ano = int(a)
        for tid, nome in torneios(ano):
            if FORA.search(nome):
                continue
            f = campanha(ano, tid)
            print(ano, tid, nome, "ok" if f else "falhou")
