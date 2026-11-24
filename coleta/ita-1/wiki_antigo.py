"""Leitor dos artigos da Wikipédia em italiano dos campeonatos de 1898 a 1928/29 (IT-017).

Cada artigo é dividido em seções pelo título (== ... ==); cada seção traz, conforme o caso:
  - "Classifica finale": wikitable com Pos., Squadra ({{Calcio X}}, que identifica o clube sem ambiguidade), Pt, G, V, N,
    P, GF, GS;
  - "Calendario": um bloco por rodada, com '''andata (Nª)''' e '''ritorno (Mª)''' no cabeçalho e linhas
    "| 24 ott. || 0-5 || Reggiana-Modena || 0-6 || 12 dic." (a data vale para as linhas seguintes até aparecer outra);
  - "Tabellone": matriz de resultados (linha = mandante, coluna = visitante, na mesma ordem das linhas), sem data;
  - {{Incontro di club}}: ficha do jogo (data, fase, estádio, público, árbitro, gols com minuto), nas finais e nos
    jogos de mata-mata.

Uso: secoes(texto) -> [(caminho, corpo)]; calendario(corpo, ano_ini, ano_fim); tabellone(corpo); incontros(texto, anos);
classifiche(corpo).
"""
from __future__ import annotations

import re

MESES = {"gen": 1, "feb": 2, "mar": 3, "apr": 4, "mag": 5, "giu": 6, "lug": 7, "ago": 8, "set": 9, "ott": 10, "nov": 11,
         "dic": 12}
DATA = re.compile(r"(\d{1,2})\s*º?\s*(gen|feb|mar|apr|mag|giu|lug|ago|set|ott|nov|dic)[a-z]*\.?", re.I)
PLACAR = re.compile(r"^(\d+)\s*[-–]\s*(\d+)(.*)$")


def _fecha(t: str, i: int) -> int:
    n, k = 0, i
    while k < len(t):
        if t.startswith("{{", k):
            n += 1; k += 2; continue
        if t.startswith("}}", k):
            n -= 1; k += 2
            if n == 0:
                return k
            continue
        k += 1
    return len(t)


def sem_refs(s: str) -> str:
    s = re.sub(r"<ref[^>]*/>", "", s)
    s = re.sub(r"<ref[^>]*>.*?</ref>", "", s, flags=re.S)
    return re.sub(r"<!--.*?-->", "", s, flags=re.S)


def notas_em_marcas(corpo: str) -> str:
    """Notas <ref> (que podem ter várias linhas) viram marcas de uma linha só, "⟦texto⟧"; a nota com nome reaproveitada
    (<ref name=x/>) recebe o texto da definição."""
    defs = {n.strip(): c for n, c in re.findall(r'<ref name\s*=\s*"?([^">/]+)"?\s*>(.*?)</ref>', corpo, flags=re.S)}
    corpo = re.sub(r'<ref name\s*=\s*"?([^">/]+)"?\s*/>',
                   lambda m: "⟦" + re.sub(r"\s+", " ", defs.get(m.group(1).strip(), "")) + "⟧", corpo)
    return re.sub(r"<ref[^>/]*>(.*?)</ref>", lambda m: "⟦" + re.sub(r"\s+", " ", m.group(1)) + "⟧", corpo, flags=re.S)


def limpar(s: str) -> str:
    """Texto visível de uma célula: tira refs, negrito, links e modelos de formatação."""
    s = re.sub(r"⟦[^⟧]*⟧", "", sem_refs(s))
    s = re.sub(r"\{\{(?:Calcio|Bandiera|simbolo|Sfondo)[^{}]*\}\}", lambda m: _modelo(m.group(0)), s)
    s = re.sub(r"\{\{[^{}]*\}\}", "", s)
    s = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s).replace("{{", "").replace("}}", "")
    return re.sub(r"\s+", " ", s.replace("'''", "").replace("''", "")).strip()


def _modelo(m: str) -> str:
    """{{Calcio Pro Vercelli}} -> "Pro Vercelli"; {{Calcio Inter|N}} -> "Inter"; os outros somem."""
    x = re.match(r"\{\{Calcio ([^|}]+)", m)
    return x.group(1).strip() if x else ""


def modelo_clube(s: str) -> str | None:
    """Nome do modelo {{Calcio X}} numa célula (a identidade do clube), ou None."""
    x = re.search(r"\{\{Calcio ([^|}]+)", s)
    return x.group(1).strip() if x else None


def secoes(texto: str) -> list[tuple[list[str], str]]:
    res, pilha = [], []
    partes = re.split(r"^(=+)\s*(.*?)\s*=+\s*$", texto, flags=re.M)
    corpo = partes[0]
    res.append(([], corpo))
    for i in range(1, len(partes), 3):
        nivel, titulo, corpo = len(partes[i]), limpar(partes[i + 1]), partes[i + 2]
        pilha = [p for p in pilha if p[0] < nivel] + [(nivel, titulo)]
        res.append(([t for _, t in pilha], corpo))
    return res


def data_iso(d: str, ano_ini: int, ano_fim: int) -> str | None:
    m = DATA.search(d or "")
    if not m:
        return None
    mes = MESES[m.group(2).lower()[:3]]
    ano = ano_ini if mes >= 8 else ano_fim
    return f"{ano:04d}-{mes:02d}-{int(m.group(1)):02d}"


def _celulas(linha: str) -> list[str]:
    """Células de uma linha de tabela wiki ("| a || b || c"), sem os atributos ("bgcolor=... | 24 ott.")."""
    linha = linha.strip()
    if linha.startswith("||"):   # primeira célula vazia
        linha = linha[2:]
    elif linha.startswith("|"):
        linha = linha[1:]
    res = []
    for c in sem_refs(linha).split("||"):
        if "|" in c and not re.search(r"\[\[[^\]]*\|", c) and re.match(r"^\s*[\w-]+\s*=", c):
            c = c.rsplit("|", 1)[1]
        res.append(c.strip())
    return res


def _placar(c: str) -> tuple[int, int, str] | None:
    x = PLACAR.match(limpar(c))
    if not x:
        return None
    return int(x.group(1)), int(x.group(2)), x.group(3).strip()


def calendario(corpo: str, ano_ini: int, ano_fim: int) -> list[dict]:
    """Jogos de um "Calendario": [{data, rodada, casa_fora ("A-B" como escrito), gm, gv, nota}]."""
    res = []
    ida = volta = None
    d_ida = d_volta = None
    for linha in notas_em_marcas(corpo).split("\n"):
        cab = re.findall(r"(andata|ritorno)\s*\((\d+)\s*ª?\)", linha, re.I)
        if cab:
            for tipo, n in cab:
                if tipo.lower() == "andata":
                    ida = int(n)
                else:
                    volta = int(n)
            if not any(t.lower() == "ritorno" for t, _ in cab) and "andata" in linha.lower():
                pass
            continue
        g = re.search(r"'''\s*(?:\d+)?\s*([A-Za-zàèéìòù]+ giornata|Giornata \d+)\s*'''", linha)
        if not linha.strip().startswith("|") or linha.strip().startswith(("|-", "|}", "{|", "|+")) or "||" not in linha:
            continue
        cels = _celulas(linha)
        idx_time = next((i for i, c in enumerate(cels) if re.search(r"[A-Za-zÀ-ÿ].*[-–].*[A-Za-zÀ-ÿ]", limpar(c))
                         and not DATA.fullmatch(limpar(c)) and not re.search(r"riposa", c, re.I)), None)
        if idx_time is None:
            continue
        placares = [(i, _placar(c)) for i, c in enumerate(cels)]
        esq = next((p for i, p in reversed(placares[:idx_time]) if p), None)
        dir_ = next((p for i, p in placares[idx_time + 1:] if p), None)
        for i, c in enumerate(cels):
            if DATA.search(limpar(c)) and not _placar(c):
                if i < idx_time:
                    d_ida = data_iso(limpar(c), ano_ini, ano_fim)
                else:
                    d_volta = data_iso(limpar(c), ano_ini, ano_fim)
        times = limpar(cels[idx_time])
        nota = " ".join(limpar(x) for x in re.findall(r"⟦([^⟧]*)⟧", linha) if x.strip())
        if esq or not dir_:
            res.append({"data": d_ida, "rodada": ida, "casa_fora": times, "placar": esq, "lado": "ida", "nota": nota})
        if dir_:
            res.append({"data": d_volta, "rodada": volta, "casa_fora": times, "placar": dir_, "lado": "volta", "nota": nota})
    return res


def tabellone(corpo: str) -> list[dict]:
    """Matriz de resultados: [{mandante, visitante (nomes das linhas), gm, gv}]."""
    i = corpo.find("{|")
    if i < 0:
        return []
    linhas_tab = re.split(r"\n\|-[^\n]*", corpo[i:corpo.find("\n|}", i) if corpo.find("\n|}", i) > 0 else len(corpo)])
    times, celulas = [], []
    for bloco in linhas_tab[1:]:
        cels = []
        for l in bloco.strip().split("\n"):
            if l.startswith("|") and not l.startswith("|}"):
                cels += _celulas(l)
        if not cels:
            continue
        times.append(limpar(cels[0]))
        celulas.append(cels[1:])
    res = []
    for r, (m, cels) in enumerate(zip(times, celulas)):
        cels = [c for c in cels if c.strip() or True]
        for k, c in enumerate(cels):
            if k >= len(times) or k == r:
                continue
            p = _placar(c)
            if p:
                res.append({"mandante": m, "visitante": times[k], "placar": p})
    return res


def incontros(texto: str) -> list[dict]:
    """Fichas {{Incontro di club}}: data, fase, clubes, placar, estádio, cidade, público, árbitro, gols."""
    res = []
    for m in re.finditer(r"\{\{\s*Incontro di club", texto):
        corpo = texto[m.start():_fecha(texto, m.start())]
        params = {}
        for p in re.split(r"\n\s*\|", corpo):
            if "=" in p:
                k, v = p.split("=", 1)
                params[k.strip()] = v.strip()
        ano = re.search(r"\d{4}", params.get("Anno", ""))
        dm = DATA.search(params.get("Giornomese", "").replace("maggio", "mag").replace("giugno", "giu").replace("aprile", "apr")
                         .replace("marzo", "mar").replace("febbraio", "feb").replace("gennaio", "gen").replace("luglio", "lug")
                         .replace("settembre", "set").replace("ottobre", "ott").replace("novembre", "nov").replace("dicembre", "dic")
                         .replace("agosto", "ago"))
        data = f"{int(ano.group(0)):04d}-{MESES[dm.group(2).lower()[:3]]:02d}-{int(dm.group(1)):02d}" if ano and dm else None
        try:
            gm, gv = int(limpar(params.get("Punteggio 1", ""))), int(limpar(params.get("Punteggio 2", "")))
        except ValueError:
            gm = gv = None
        gols = []
        for lado in ("1", "2"):
            for x in re.finditer(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]\s*((?:\{\{Goal[^}]*\}\}\s*,?\s*)+)", params.get(f"Marcatori {lado}", "")):
                for g in re.findall(r"\{\{Goal\|?([^}]*)\}\}", x.group(2)):
                    mi = re.match(r"\d+", g or "")
                    gols.append({"lado": lado, "jogador": x.group(1).strip(), "minuto": int(mi.group(0)) if mi else None,
                                 "tipo": "penalti" if "rig" in g.lower() else "contra" if "aut" in g.lower() else "normal"})
        esp = re.sub(r"\D", "", limpar(params.get("Spettatori", "")))
        res.append({"data": data, "turno": limpar(params.get("Turno", "")), "m": limpar(params.get("Squadra 1", "")),
                    "v": limpar(params.get("Squadra 2", "")), "gm": gm, "gv": gv,
                    "cidade": limpar(params.get("Città", "")) or None, "estadio": limpar(params.get("Stadio", "")) or None,
                    "publico": int(esp) if esp else None, "arbitro": limpar(params.get("Arbitro", "")) or None,
                    "gols": gols, "nota": limpar(params.get("Note", ""))})
    return res


def classifiche(corpo: str) -> list[list[dict]]:
    """Tabelas de classificação de uma seção: [[{posicao, modelo, nome, pontos, jogos, vitorias, empates, derrotas,
    gols_pro, gols_contra}]]."""
    res = []
    for m in re.finditer(r"\{\|[^\n]*wikitable", corpo):
        fim = corpo.find("\n|}", m.start())
        tab = corpo[m.start():fim if fim > 0 else len(corpo)]
        cab = " ".join(re.findall(r"^!.*$", tab, re.M))
        if "Pt" not in cab or not re.search(r"Squadra", cab):
            continue
        linhas = []
        for bloco in re.split(r"\n\|-[^\n]*", tab)[1:]:
            cels = []
            for l in sem_refs(bloco).strip().split("\n"):
                l = l.strip()
                if not l or l.startswith("!"):
                    continue
                l = l[2:] if l.startswith("||") else l[1:] if l.startswith("|") else l
                cels += [c.strip() for c in l.split("||")]
            idx = next((i for i, c in enumerate(cels) if modelo_clube(c) or re.search(r"\[\[", c)), None)
            if idx is None:
                continue
            nums = []
            for c in cels[idx + 1:]:
                c2 = limpar(c).replace("−", "-")
                if re.fullmatch(r"[+-]?\d+", c2) and abs(int(c2)) < 1000:   # um ano de link na célula não é número
                    nums.append(int(c2))
            if len(nums) < 7:
                continue
            pos = next((int(x.group(1)) for c in cels[:idx] if (x := re.search(r"(\d+)\.", limpar(c)))), None)
            pts, j, v, e, d, gp, gc = nums[:7]
            linhas.append({"posicao": pos, "modelo": modelo_clube(cels[idx]), "nome": limpar(cels[idx]), "pontos": pts,
                           "jogos": j, "vitorias": v, "empates": e, "derrotas": d, "gols_pro": gp, "gols_contra": gc})
        if linhas:
            res.append(linhas)
    return res
