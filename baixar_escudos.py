"""Baixa os escudos dos clubes para data/escudos/ (usados pelo dashboard v2).

Fonte: a imagem principal da página do clube na Wikipédia em português
(API pageimages), em PNG de TAMANHO px (250: nítido no pódio, com sobra). Rodar de novo só baixa o que falta;
--pequenos baixa de novo os que estão menores que isso (de quando eram 120 px); --todos baixa tudo outra vez.
A Wikipédia limita o ritmo (429): o script espera, tenta de novo e segue para o próximo se não der.

Páginas: PAGINAS (escritas à mão, nome de exibição -> título na Wikipédia) e
data/escudos/paginas_auto.json (achadas por --descobrir: para cada clube do
banco sem página, busca "nome + clube de futebol + estado" e fica com o
primeiro resultado que a Wikipédia descreve como clube/time de futebol).
Clube sem escudo na Wikipédia: endereço da imagem em OUTRAS_FONTES (ogol, Commons...).
Achou errado? Escreva o certo em PAGINAS (vale mais que o automático) e rode
com --todos, ou apague o arquivo do escudo e rode de novo.

Clubes dos pacotes do agente de coleta (data/coleta/<slug>/pacote/) que seguem sem escudo: --ogol procura o
escudo nos calendários do ogol guardados em data/cache/ogol*/ (ao lado de cada nome há o escudo do clube) e grava
em data/escudos/ogol_auto.json; o nome do ogol vira clube pelos nomes_fonte do clubes.csv do pacote, com os anos.

Uso: python baixar_escudos.py [--descobrir] [--ogol] [--pequenos | --todos]
"""
from __future__ import annotations

import json
import re
import sqlite3
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent
PASTA = ROOT / "data" / "escudos"
AUTO = PASTA / "paginas_auto.json"
OGOL_AUTO = PASTA / "ogol_auto.json"   # clube -> escudo no ogol, achado por --ogol
OGOL_IMG = "https://cdn-img.staticzz.com/img/"
DB = ROOT / "db" / "futebol.db"   # todas as competições do banco genérico
API = "https://pt.wikipedia.org/w/api.php"
UA = {"User-Agent": "clube-analitico/1.0 (projeto pessoal; dashboard de futebol)"}

PAGINAS = {
    "Palmeiras": "Sociedade Esportiva Palmeiras",
    "Santos": "Santos Futebol Clube",
    "Flamengo": "Clube de Regatas do Flamengo",
    "Corinthians": "Sport Club Corinthians Paulista",
    "São Paulo": "São Paulo Futebol Clube",
    "Cruzeiro": "Cruzeiro Esporte Clube",
    "Vasco": "Club de Regatas Vasco da Gama",
    "Fluminense": "Fluminense Football Club",
    "Internacional": "Sport Club Internacional",
    "Atlético-MG": "Clube Atlético Mineiro",
    "Botafogo": "Botafogo de Futebol e Regatas",
    "Grêmio": "Grêmio Foot-Ball Porto Alegrense",
    "Bahia": "Esporte Clube Bahia",
    "Guarani": "Guarani Futebol Clube",
    "Athletico-PR": "Club Athletico Paranaense",
    "Coritiba": "Coritiba Foot Ball Club",
    "Sport": "Sport Club do Recife",
    "São Caetano": "Associação Desportiva São Caetano",
    "Fortaleza": "Fortaleza Esporte Clube",
    "Náutico": "Clube Náutico Capibaribe",
    "Vitória": "Esporte Clube Vitória",
    "Bragantino": "Red Bull Bragantino",
    "Portuguesa": "Associação Portuguesa de Desportos",
    "Bangu": "Bangu Atlético Clube",
    "América-RJ": "America Football Club (Rio de Janeiro)",
    "Brasil de Pelotas": "Grêmio Esportivo Brasil",
    "Ceará": "Ceará Sporting Club",
    "Goiás": "Goiás Esporte Clube",
    "Operário-MS": "Operário Futebol Clube",
    "Ponte Preta": "Associação Atlética Ponte Preta",
    "Rio Branco-ES": "Rio Branco Atlético Clube",
    # 30 que mais participaram (bloco de participações)
    "Paysandu": "Paysandu Sport Club",
    "Santa Cruz": "Santa Cruz Futebol Clube",
    "Juventude": "Esporte Clube Juventude",
    "América-MG": "América Futebol Clube (Belo Horizonte)",
    "CSA": "Centro Sportivo Alagoano",
    "Figueirense": "Figueirense Futebol Clube",
    # a busca automática (--descobrir) não achou
    "Cuiabá": "Cuiabá Esporte Clube",
    "Uberaba": "Uberaba Sport Club",
    # a busca automática achou o clube errado (conferido na folha de contato de 19/11/2026)
    "ASA": "Agremiação Sportiva Arapiraquense",
    "América-SP": "América Futebol Clube (São José do Rio Preto)",
    "Botafogo-SP": "Botafogo Futebol Clube (Ribeirão Preto)",
    "Brasília EC": "Brasília Futebol Clube",
    "CRB": "Clube de Regatas Brasil",
    "Campo Grande-RJ": "Campo Grande Atlético Clube",
    "Caxias": "Sociedade Esportiva e Recreativa Caxias do Sul",
    "Chapecoense": "Associação Chapecoense de Futebol",
    "Colorado-PR": "Colorado Esporte Clube",
    "Comercial-MS": "Esporte Clube Comercial",
    "Fast-AM": "Fast Clube",
    "Ferroviária-SP": "Associação Ferroviária de Esportes",
    "Ferroviário-MA": "Ferroviário Esporte Clube",
    "Fluminense-BA": "Fluminense de Feira Futebol Clube",
    "Fonseca-RJ": "Fonseca Atlético Clube",
    "GE Maringá": "Grêmio de Esportes Maringá",
    "Guará": "Clube de Regatas Guará",
    "Internacional-SC": "Esporte Clube Internacional (Lages)",
    "Joinville": "Joinville Esporte Clube",
    "Juventus-SP": "Clube Atlético Juventus",
    "Leônico-BA": "Associação Desportiva Leônico",
    "Olaria": "Olaria Atlético Clube",
    "Olímpico-AM": "Olímpico Clube",
    "Operário-MT": "Clube Esportivo Operário Várzea-Grandense",
    "Paula Ramos-SC": "Paula Ramos Esporte Clube",
    "Santa Cruz-SE": "Sport Clube Santa Cruz (Estância)",
    "Santo André": "Esporte Clube Santo André",
    "Sergipe": "Club Sportivo Sergipe",
    "São José-SP": "São José Esporte Clube",
    "São Paulo-RS": "Sport Club São Paulo",
    "Taguatinga": "Taguatinga Esporte Clube",
    "Tuna Luso": "Tuna Luso Brasileira",
    "Villa Nova-MG": "Villa Nova Atlético Clube",
    "XV de Piracicaba": "Esporte Clube XV de Novembro (Piracicaba)",
    "Água Verde": "Esporte Clube Água Verde",
    # Série B (20/11/2026): a busca automática tinha achado o clube errado
    "Amazonas": "Amazonas Futebol Clube",
    "Americana": "Guaratinguetá Futebol Ltda.",
    "Baraúnas": "Associação Cultural Esporte Clube Baraúnas",
    "Botafogo-BA": "Botafogo Sport Club",
    "Cascavel": "Cascavel Esporte Clube",
    "Democrata-GV": "Esporte Clube Democrata",
    "Democrata-SL": "Democrata Futebol Clube",
    "Esportivo-RS": "Clube Esportivo Bento Gonçalves",
    "Glória": "Grêmio Esportivo Glória",
    "Guarany": "Guarany Sporting Club",
    "Malutrom": "J.Malucelli Futebol S/A",
    "Novorizontino": "Grêmio Novorizontino",
    "Parnaíba": "Parnahyba Sport Club",
    "Pelotas": "Esporte Clube Pelotas",
    "Picos": "Sociedade Esportiva de Picos",
    "Princesa": "Princesa do Solimões Esporte Clube",
    "Salgueiro": "Salgueiro Atlético Clube",
    "São Raimundo": "São Raimundo Esporte Clube (Amazonas)",
    "Tombense": "Tombense Futebol Clube",
    "Tupi": "Tupi Football Club",
    "Ubiratan": "Ubiratan Esporte Clube",
    "Valeriodoce": "Valeriodoce Esporte Clube",
}
# sem página (ou sem escudo) na Wikipédia: a busca automática não procura (o escudo vem de OUTRAS_FONTES)
SEM_ESCUDO = {"Eletrovapo-RJ", "Guanabara-DF", "Perdigão", "Rio Branco-RJ", "Liga da Marinha", "CEUB", "Colatina", "Inter de Santa Maria", "Manufatora",
              # Série B: escudo do ogol (abaixo) ou nenhuma fonte segura (ficam com a bolinha de cor)
              "Atlético-BA", "Estudantes", "Maguari", "Nacional-GO", "Nacional-PB", "Santa Cruz-RS", "São Domingos", "Tiradentes-CE", "Oeste", "Central-RJ", "Douradense", "Esportivo-MG", "Ferroviário-PE", "Rio Branco-MG", "Rodoviária", "Serrano", "Tiradentes-DF"}
# escudo achado fora da Wikipédia (conferido em 19/11/2026): ogol.com.br, Wikimedia Commons e SeekLogo
OUTRAS_FONTES = {
    "Eletrovapo-RJ": "https://cdn-img.staticzz.com/img/logos/equipas/69/39769_logo_eletrovapo.jpg",            # ogol: AE Eletrovapo, Niterói
    "Manufatora": "https://cdn-img.staticzz.com/img/logos/equipas/58/39358_logo_manufatora_rj.gif",            # ogol: Manufatora AC, Niterói
    "Guanabara-DF": "https://cdn-img.staticzz.com/img/logos/equipas/70/39770_logo_guanabara_df.png",           # ogol: AA Guanabara, Brasília
    "Liga da Marinha": "https://cdn-img.staticzz.com/img/logos/equipas/75/297975_logo_liga_da_marinha.png",    # ogol
    "Rio Branco-RJ": "https://cdn-img.staticzz.com/img/logos/equipas/29/3429_logo_rio_branco_rj.gif",          # ogol: CE Rio Branco, Campos
    "Colatina": "https://cdn-img.staticzz.com/img/logos/equipas/18516_imgbank.png",                            # ogol: AA Colatina (1978-1996)
    "Inter de Santa Maria": "https://cdn-img.staticzz.com/img/logos/equipas/3292_imgbank.png",                 # ogol: Inter SM
    "Perdigão": "https://images.seeklogo.com/logo-png/12/1/sociedade-esportiva-perdigao-de-videira-sc-logo-png_seeklogo-128734.png",  # SE Perdigão, Videira-SC
    "CEUB": "https://upload.wikimedia.org/wikipedia/commons/6/6d/CEUB.png",                                   # Commons: CEUB Esporte Clube
    "Oeste": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Oeste_FC_Badge.svg/250px-Oeste_FC_Badge.svg.png",   # Commons: escudo do Oeste (a página virou Osasco Sporting)
    # Série B (20/11/2026): ogol, escudo do calendário da edição
    "Atlético-BA": "https://cdn-img.staticzz.com/img/logos/equipas/3128_imgbank_1683641721.png",
    "Estudantes": "https://cdn-img.staticzz.com/img/logos/equipas/16/18916_logo_estudantes.jpg",
    "Maguari": "https://cdn-img.staticzz.com/img/logos/equipas/44/42244_logo_maguary.png",
    "Nacional-GO": "https://cdn-img.staticzz.com/img/logos/equipas/95/53095_logo_nacional_go_20250522110433.png",
    "Nacional-PB": "https://cdn-img.staticzz.com/img/logos/equipas/9786_imgbank_1685115286.png",
    "Santa Cruz-RS": "https://cdn-img.staticzz.com/img/logos/equipas/46/3446_logo_santa_cruz_rs.gif",
    "São Domingos": "https://cdn-img.staticzz.com/img/logos/equipas/59/3459_logo_sao_domingos.jpg",
    "Tiradentes-CE": "https://cdn-img.staticzz.com/img/logos/equipas/3490_imgbank_1677772260.png",
}


TAMANHO = 250   # um dos tamanhos-padrão de miniatura da Wikipédia


def arquivo(clube: str) -> Path:
    """'São Paulo' -> data/escudos/sao-paulo.png"""
    s = unicodedata.normalize("NFKD", clube).encode("ascii", "ignore").decode().lower()
    return PASTA / ("".join(c if c.isalnum() else "-" for c in s).strip("-") + ".png")


def pegar(url: str) -> bytes:
    """GET com nova tentativa quando a Wikipédia pede para esperar (429)."""
    for tentativa in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code != 429 or tentativa == 5:
                raise
            time.sleep(max(int(e.headers.get("Retry-After") or 0), 20 * (tentativa + 1)))
    raise RuntimeError("não deveria chegar aqui")


def miniatura(titulo: str) -> str | None:
    q = urllib.parse.urlencode({"action": "query", "titles": titulo, "prop": "pageimages", "pithumbsize": TAMANHO,
                                "redirects": 1, "format": "json"})
    paginas = json.loads(pegar(f"{API}?{q}"))["query"]["pages"]
    return next((p["thumbnail"]["source"] for p in paginas.values() if "thumbnail" in p), None)


UF = {"AC": "Acre", "AL": "Alagoas", "AM": "Amazonas", "AP": "Amapá", "BA": "Bahia", "CE": "Ceará", "DF": "Distrito Federal",
      "ES": "Espírito Santo", "GO": "Goiás", "MA": "Maranhão", "MG": "Minas Gerais", "MS": "Mato Grosso do Sul", "MT": "Mato Grosso",
      "PA": "Pará", "PB": "Paraíba", "PE": "Pernambuco", "PI": "Piauí", "PR": "Paraná", "RJ": "Rio de Janeiro", "RN": "Rio Grande do Norte",
      "RO": "Rondônia", "RR": "Roraima", "RS": "Rio Grande do Sul", "SC": "Santa Catarina", "SE": "Sergipe", "SP": "São Paulo", "TO": "Tocantins",
      "RP": "Ribeirão Preto"}
EH_CLUBE = re.compile(r"clube|futebol|time|agremia|associa|esporte|sport", re.I)
NAO_CLUBE = re.compile(r"est[aá]dio|munic[ií]pio|cidade|bairro|campeonato|torneio|jogador|treinador", re.I)


def paginas() -> dict[str, str]:
    auto = json.loads(AUTO.read_text(encoding="utf-8")) if AUTO.exists() else {}
    return {**auto, **PAGINAS}   # as escritas à mão valem mais


def descobrir() -> None:
    """Procura a página dos clubes do banco que ainda não têm uma e grava em paginas_auto.json."""
    from gerar_dashboard_v2 import nome   # nome de exibição (com acento) do clube
    con = sqlite3.connect(DB)
    try:
        clubes = con.execute("SELECT DISTINCT c.nome, c.regiao FROM classificacao_final f JOIN clube c USING (clube_id)").fetchall()
    finally:
        con.close()
    auto = json.loads(AUTO.read_text(encoding="utf-8")) if AUTO.exists() else {}
    for bruto, uf in sorted(clubes):
        c = nome(bruto)
        if c in PAGINAS or c in auto or c in SEM_ESCUDO:
            continue
        base = re.sub(r"-[A-Z]{2}$", "", bruto)
        estado = UF.get(uf or "") or (UF.get(bruto[-2:]) if re.search(r"-[A-Z]{2}$", bruto) else "") or ""   # da tabela ou do sufixo do nome
        q = f"{base} clube de futebol {estado or 'brasileiro'}"
        par = urllib.parse.urlencode({"action": "query", "generator": "search", "gsrsearch": q, "gsrlimit": 6, "prop": "pageimages|description",
                                      "pithumbsize": TAMANHO, "format": "json"})
        res = sorted(json.loads(pegar(f"{API}?{par}")).get("query", {}).get("pages", {}).values(), key=lambda x: x.get("index", 99))
        achou = next((x["title"] for x in res if "thumbnail" in x and EH_CLUBE.search(x.get("description", "") + " " + x["title"])
                      and not NAO_CLUBE.search(x.get("description", ""))), None)
        print(f"{c:24} -> {achou or 'NÃO ACHOU'}   ({q})")
        if achou:
            auto[c] = achou
            AUTO.write_text(json.dumps(auto, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        time.sleep(1.5)


def descobrir_ogol() -> None:
    """Escudo do ogol para os clubes dos pacotes de coleta que não têm escudo (nem página na lista à mão)."""
    import csv
    ogol: dict[str, list] = {}   # nome no ogol -> [(ano inicial, ano final, clube)]
    for f in sorted((ROOT / "data" / "coleta").glob("*/pacote/clubes.csv")):
        for r in csv.DictReader(f.open(encoding="utf-8")):
            for item in filter(None, (r.get("nomes_fonte") or "").split("|")):
                fonte, resto = item.split(":", 1)
                if fonte == "ogol":
                    nome_o, anos = resto.rsplit(":", 1)
                    a1, _, a2 = anos.partition("-")
                    ogol.setdefault(nome_o, []).append((int(a1), int(a2 or a1), r["clube"]))
    achados: dict[str, dict] = {}
    for f in sorted((ROOT / "data" / "cache").glob("ogol*/calendario_*.html")):
        ano = int(f.name.split("_")[1])
        texto = f.read_text(encoding="utf-8", errors="replace")
        for nome_o, img in re.findall(r'<img alt="([^"]+)" title="[^"]*" src="/img_icon/\d+x\d+/(logos/equipas/[^"]+)"', texto):
            nome_o = nome_o.strip()
            donos = {c for a1, a2, c in ogol.get(nome_o, []) if a1 <= ano <= a2}
            if len(donos) == 1:
                cont = achados.setdefault(donos.pop(), {})
                cont[img] = cont.get(img, 0) + 1
    auto = json.loads(OGOL_AUTO.read_text(encoding="utf-8")) if OGOL_AUTO.exists() else {}
    for c, imgs in sorted(achados.items()):
        if c in paginas() or c in OUTRAS_FONTES or c in auto or arquivo(c).exists():
            continue
        auto[c] = OGOL_IMG + max(imgs, key=imgs.get)   # o escudo que mais aparece (o clube pode ter trocado de escudo)
    OGOL_AUTO.write_text(json.dumps(auto, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"ogol: {len(auto)} clubes com escudo achado")


def main() -> None:
    PASTA.mkdir(parents=True, exist_ok=True)
    if "--descobrir" in sys.argv:
        descobrir()
    if "--ogol" in sys.argv:
        descobrir_ogol()
    todos, pequenos = "--todos" in sys.argv, "--pequenos" in sys.argv

    def pular(destino: Path) -> bool:
        if not destino.exists() or todos:
            return False
        if pequenos:
            from PIL import Image
            return max(Image.open(destino).size) >= TAMANHO * 0.9
        return True

    for clube, titulo in paginas().items():
        destino = arquivo(clube)
        if pular(destino):
            continue
        try:
            url = miniatura(titulo)
            if not url:
                print(f"SEM IMAGEM: {clube} ({titulo})")
                continue
            destino.write_bytes(pegar(url))
            print(f"ok: {clube} -> {destino.name}")
        except urllib.error.HTTPError as e:
            print(f"ERRO {e.code}: {clube} (fica o escudo que já tinha; rode de novo depois)")
        time.sleep(5)   # a Wikipédia limita o ritmo (429)
    ogol_auto = json.loads(OGOL_AUTO.read_text(encoding="utf-8")) if OGOL_AUTO.exists() else {}
    for clube, url in {**ogol_auto, **OUTRAS_FONTES}.items():
        destino = arquivo(clube)
        if pular(destino):
            continue
        dados = pegar(url)
        try:   # jpg/gif viram png (o dashboard lê .png)
            import io
            from PIL import Image
            img = Image.open(io.BytesIO(dados)).convert("RGBA")
            img.thumbnail((TAMANHO, TAMANHO))
            buf = io.BytesIO()
            img.save(buf, "PNG")
            dados = buf.getvalue()
        except ImportError:
            pass
        destino.write_bytes(dados)
        print(f"ok: {clube} -> {destino.name} ({url.split('/')[2]})")
        time.sleep(1)


if __name__ == "__main__":
    main()
