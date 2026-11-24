"""Escreve o relatório da coleta (docs/coleta/kor-1.md), chamado pelo importar.py."""
from __future__ import annotations

from pathlib import Path

CABECALHO = """# Campeonato Sul-Coreano (1ª divisão) — coleta de dados

Gerado por `python coleta/kor-1/importar.py`. Pacote em `data/coleta/kor-1/pacote/`.

**Edições:** {n_ed}, uma por título, de 1983 a 2025, como na lista de campeões da K League, da RSSSF (`skorchamp.html`) e da
Wikipédia em inglês (List of South Korean football champions): K League (Super League em 1983-1986) e, de 2013 em diante,
K League 1 (K League Classic até 2017). 2026 entra quando acabar. A liga semiprofissional de antes de 1983 não entra
(era outra competição, de clubes de empresa e do Exército; a K League conta a sua história a partir de 1983).

**Fora do pacote:** a copa da liga (아디다스컵, 리그컵 etc.; o patrocínio pôs "copa" no nome da própria liga em 1996-1999, mas
essas são a liga), a repescagem contra a K League 2 (승강 플레이오프, 2013 em diante: entra com a 2ª divisão), a Copa da
Coreia (FA Cup) e a Supercopa.

**Fontes:** portal de dados oficial da K League (portal.kleague.com, acesso de convidado): lista de jogos de cada ano
(`data/coleta/kor-1/portal/calendario_<ano>.json`; de 2013 em diante a lista vem do site oficial, www.kleague.com, com
fase e rodada) e o boletim de cada jogo (data, hora, estádio, público, árbitro, autores dos gols com minuto, pênalti, gol
contra, cartões, disputa de pênaltis), no cache `data/cache/kleague-asia/jogos/`; site oficial da K League
(www.kleague.com): linha do tempo de cada jogo de 2013 em diante, em coreano e em inglês (`data/cache/kleague-asia/oficial/`:
conferência do placar e nome dos jogadores em inglês) e a classificação final oficial de 2013 em diante
(`data/coleta/kor-1/oficial/tabela_<ano>.json`); RSSSF (uma página por ano e a `skorhist.html`, com a tabela de cada ano de
1983 a 2009, em `data/coleta/kor-1/rsssf/`: conferência dos placares e das tabelas); Wikipédia em inglês (lista de campeões e
lista de artilheiros, "K League Top Scorer Award", em `data/coleta/kor-1/wikipedia/`) e em coreano (tabela e resultados de
cada ano, consultada nas divergências); ogol (calendário de 2008 a 2025, para os escudos e a conferência:
`data/coleta/kor-1/ogol/` e `data/cache/ogol-kor-1/`).

**Clubes:** {n_cl}. Um clube por código do portal oficial (K01, K04...), que é o mesmo nas mudanças de nome e de cidade, como
a própria K League conta: Yukong Elephants/Bucheon SK = Jeju United; Daewoo Royals = Busan IPark; Ilhwa Chunma = Seongnam
FC; Lucky-Goldstar/LG Cheetahs = FC Seoul; Hyundai Horang-i = Ulsan Hyundai; POSCO = Pohang Steelers. Os times militares
têm códigos diferentes e ficam separados: Sangmu (1985), Gwangju Sangmu (2003-2010), Sangju Sangmu (2011-2020) e Gimcheon
Sangmu (2022 em diante). O Chonbuk Buffalo (1994) não é o Jeonbuk Hyundai. Nome de exibição: o de hoje, como o ogol escreve.
Os nomes de cada fonte estão no `nomes_fonte` do `clubes.csv` (regras em `coleta/kor-1/clubes_kor.py`).

**Regras:** placar oficial, com a prorrogação. O total de gols do boletim do portal não conta o gol contra (em nenhuma
época): o placar é a soma dos gols do boletim, conferida com o total (mais os gols contra), com o site oficial (2013 em
diante), com a RSSSF e com o ogol; quando não batem, vale o que as outras fontes e as tabelas confirmam, e os autores dos
gols do jogo ficam de fora. Pontos: 2 por vitória em 1983 e 1985-1992; em 1984, 3 pela vitória, 2 pelo empate com gols e
1 pelo 0-0; em 1993, empate decidido nos pênaltis (4 pela vitória, 2 pela vitória nos pênaltis, 1 pela derrota nos
pênaltis); 3/1/0 em 1994-1997 e de 2001 em diante; em 1998-1999, prorrogação com gol de ouro e pênaltis (3 no tempo normal,
2 na prorrogação, 1 nos pênaltis); em 2000, 3 no tempo normal ou na prorrogação e 1 nos pênaltis. Fases: dois turnos em
1984, 1986, 1995, 1996 e 2004-2006; decisão do título entre os campeões dos turnos (1984, 1986, 1995, 1996) ou playoff
(1998-2000, 2004-2011); de 2012 em diante a liga se divide em grupo do título (A) e grupo de baixo (B) nas últimas rodadas,
com os pontos acumulados (fase única "Liga", como no Escocês; a observação do jogo diz o grupo). Classificação final: de
2013 em diante, a oficial da K League; antes, a soma dos jogos, com o campeão e o vice da decisão em 1º e 2º, depois os
eliminados do playoff pela fase em que caíram e o resto pela tabela (os números de jogos, vitórias, gols e pontos são só da
liga, sem playoff nem final, como a tabela da RSSSF). Rebaixado: de 2012 em diante, o clube que não está na edição
seguinte (antes de 2012 não havia rebaixamento). Nome dos jogadores: coreanos pela grafia oficial em inglês do site da K
League quando há (2013 em diante: "Lee Dong-gook") e, se não, pela romanização revisada do hangul do portal ("Jeong
Hae-won"); estrangeiros pelo nome de jogo, tirado do nome em inglês do site oficial (o hangul é o nome de jogo: "호벨손"
Roberson); estrangeiros de antes de 2013 sem nome em inglês ficam com o hangul romanizado (aproximação). Cartões de técnico e
comissão (sem número de camisa) ficam de fora. Artilheiro: o da lista da Wikipédia em inglês (contagem oficial),
conferido com a soma dos gols dos boletins.

**Conferência:** placares com a RSSSF (1983-2010; a RSSSF não tem os jogos de 1997, 2011, 2012 e 2025) e o ogol (2008-2025); a
tabela da liga com a da RSSSF (jogos, gols pró, gols contra e pontos de cada clube); de 2013 em diante, a tabela oficial da K
League contra a soma dos jogos; campeão e vice com a Wikipédia. Nas divergências com a RSSSF a Wikipédia em coreano decidiu.

**Edições sem jogos:** nenhuma.

**Edições com jogos incompletos:** nenhuma: todos os jogos da 1ª divisão estão no portal. {n_sem} jogos ficaram sem os autores
dos gols (o boletim não fecha com o placar; lista em cada edição).

**Resumo:** {n_j} jogos, {n_g} gols com autor, {n_c} cartões.
"""


def escrever_relatorio(arq: Path, rel, cl_l, pa_l, go_l, ca_l, explica: dict, aproximados: dict) -> None:
    n_sem = sum(len(r.get("gols_dif") or []) for _, r, *_ in rel)
    out = [CABECALHO.format(n_ed=len(rel), n_cl=len(cl_l), n_j=len(pa_l), n_g=len(go_l), n_c=len(ca_l), n_sem=n_sem).strip(), "",
           "| Temporada | Clubes | Jogos | Gols | c/ autor | Tabela RSSSF (linhas iguais) | Campeão | Classificação |",
           "|---|---|---|---|---|---|---|---|"]
    for a, r, gols, autores, _ in rel:
        out.append(f"| {a} | {r['num_clubes']} | {len(r['jogos'])} | {gols} | {autores} | {r['tab_ok']} de {r['num_clubes']} | "
                   f"{r['campeao']} | {r['classificacao']} |")
    if aproximados:
        out += ["", f"**Estrangeiros com o nome romanizado do hangul** ({len(aproximados)}; antes de 2013, sem nome em inglês no "
                "site oficial nem autor na RSSSF; aproximação, a conferir): " +
                "; ".join(f"{n} ({h}, {min(a)}{'-' + str(max(a)) if max(a) != min(a) else ''})"
                          for (n, h), a in sorted(aproximados.items(), key=lambda x: min(x[1]))) + "."]
    out += ["", "## Conferência e correções, edição a edição", ""]
    for a, r, gols, autores, obs_conf in rel:
        linhas = [f"### {a}", "", f"- {obs_conf}.", f"- Formato: {r['formato']}."]
        linhas += [f"- {o}." for o in r["obs"]]
        if r["tab_difs"]:
            linhas.append("- Tabela: diferenças com a RSSSF: " + "; ".join(r["tab_difs"]) + "." +
                          (f" {explica[a]}" if a in explica else ""))
        if r.get("difs_oficial"):
            linhas.append("- Diferenças com a tabela oficial da K League: " + "; ".join(r["difs_oficial"]) + ".")
        if r.get("ajuste"):
            linhas.append("- Pontos tirados ou dados (tabela oficial): " +
                          "; ".join(f"{c} {v:+d}" for c, v in r["ajuste"].items()) + ".")
        if r["difs_placar"]:
            linhas.append("- Placar do boletim conferido: " + "; ".join(r["difs_placar"]) + ".")
        if r.get("gols_dif"):
            linhas.append("- Jogos sem os autores dos gols (o boletim não fecha com o placar): " + "; ".join(r["gols_dif"]) + ".")
        for fonte in ("RSSSF", "ogol"):
            ok, dif = r["conf"][fonte]
            if ok or dif:
                linhas.append(f"- {fonte}: {ok} placares iguais" + (f"; diferentes: {'; '.join(dif)}" if dif else "") + ".")
        if r["cart_staff"]:
            linhas.append(f"- {r['cart_staff']} cartão(ões) de técnico ou comissão (sem número de camisa) fora do pacote.")
        reb = [c["clube"] for c in r["clf"] if c["situacao"] == "rebaixado"]
        if reb:
            linhas.append(f"- Rebaixados: {', '.join(reb)}.")
        art = r.get("art_oficial") or []
        if art:
            linhas.append("- Artilheiro (Wikipédia): " + "; ".join(f"{x['jogador']} ({x['clube']}), {x['gols']}" for x in art) + ".")
        if r.get("art_dif"):
            linhas.append(f"- Artilheiro: diferença com a soma dos boletins ({r['art_dif']}); vale a Wikipédia.")
        out += linhas + [""]
    arq.write_text("\n".join(out), encoding="utf-8")
