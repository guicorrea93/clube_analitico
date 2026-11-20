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

Uso: python baixar_escudos.py [--descobrir] [--pequenos | --todos]
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
DB = ROOT / "db" / "brasileirao.db"
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
}
# sem página (ou sem escudo) na Wikipédia: a busca automática não procura (o escudo vem de OUTRAS_FONTES)
SEM_ESCUDO = {"Eletrovapo-RJ", "Guanabara-DF", "Perdigão", "Rio Branco-RJ", "Liga da Marinha", "CEUB", "Colatina", "Inter de Santa Maria", "Manufatora"}
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
        clubes = con.execute("SELECT DISTINCT cl.nome, cl.uf FROM fato_classificacao_final_nacional f JOIN dim_clube cl USING (clube_id)").fetchall()
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


def main() -> None:
    PASTA.mkdir(parents=True, exist_ok=True)
    if "--descobrir" in sys.argv:
        descobrir()
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
    for clube, url in OUTRAS_FONTES.items():
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
