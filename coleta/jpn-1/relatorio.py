"""Escreve o relatório da coleta (docs/coleta/jpn-1.md), chamado pelo importar.py."""
from __future__ import annotations

from collections import Counter
from pathlib import Path

CABECALHO = """# Campeonato Japonês (1ª divisão) — coleta de dados

Gerado por `python coleta/jpn-1/importar.py`. Pacote em `data/coleta/jpn-1/pacote/`.

**Edições:** {n_ed}, uma por título, de 1965 a 2025, como na lista de campeões da RSSSF (`japchamp.html`, 60 títulos) e da
Wikipédia em inglês (List of Japanese football champions). Japan Soccer League (JSL, amadora: 1965 a 1984 em ano fechado,
1985/86 a 1991/92 no calendário europeu) e J.League (J1, profissional, de 1993 em diante). Em 1992 não houve liga (só a
Copa da J.League). Nos anos de dois turnos (1993-1995, 1997-2004, 2015 e 2016), o campeão é o vencedor da final entre os
campeões dos turnos (o campeão oficial); os turnos entram como fases.

**Fora do pacote:** a repescagem entre a J1 e a 2ª divisão (JSL: "Promotion/Relegation Playoffs"; J1: 1998, 2004-2008, 2018,
2019 e 2022), como no Alemão: entra com a 2ª divisão. A JSL Division 2, a Copa do Imperador, a Copa da J.League e a
Supercopa.

**Fontes:** RSSSF (uma página por temporada da JSL, `jap65.html` a `jap92.html`, em `data/coleta/jpn-1/rsssf/`: tabela final,
tabela de confrontos com todos os jogos, rodadas com data em 1988/89 e artilheiros); J.League Data Site
(data.j-league.or.jp, o site oficial de dados da J.League, em inglês: lista de jogos de cada ano em
`data/coleta/jpn-1/jleague/lista_<ano>.json`, página de cada jogo, com autores dos gols e minuto, cartões, árbitro, estádio e
público, no cache `data/cache/jleague-asia/`, e as tabelas oficiais de cada turno e anual em `tabelas_<ano>.json`);
Wikipédia em inglês (lista de campeões: campeão, vice e 3º, segunda fonte); ESPN (liga `jpn.1`, 2006 em diante,
`data/coleta/jpn-1/espn/`: conferência dos placares); ogol (calendário da J1, 1993-2025, para os escudos:
`data/cache/ogol-jpn-1/`).

**Clubes:** {n_cl}. Nome pelo qual o clube é conhecido hoje (o do ogol, quase sempre). Os clubes de empresa da JSL que viraram
clubes da J.League são o mesmo clube, como a J.League, os clubes e a lista de campeões da RSSSF contam: Toyo Industries/Mazda =
Sanfrecce Hiroshima, Mitsubishi = Urawa Reds, Furukawa = JEF United Chiba, Hitachi = Kashiwa Reysol, Yanmar = Cerezo Osaka,
Towa Estate/Fujita = Shonan Bellmare, Toyota = Nagoya Grampus, Fujitsu = Kawasaki Frontale, Nissan = Yokohama F. Marinos,
Yomiuri = Tokyo Verdy, Sumitomo = Kashima Antlers, All Nippon Airways = Yokohama Flügels, Matsushita = Gamba Osaka,
Yamaha = Júbilo Iwata, Toshiba = Consadole Sapporo. O Yokohama Flügels (fechado em 1998, fundido ao Marinos) é um clube
separado do Yokohama F. Marinos. Os nomes de cada fonte estão no `nomes_fonte` do `clubes.csv` (regras em
`coleta/jpn-1/clubes_jpn.py`).

**Regras:** placar oficial, com a prorrogação. De 1993 a 1998 não havia empate: prorrogação com gol de ouro e, empatado, pênaltis
(`penaltis_mandante`/`penaltis_visitante`); de 1999 a 2002, prorrogação com gol de ouro e empate se ela terminasse sem gol.
Pontos por vitória: JSL 2 (1965-1976 e 1980-1987/88), 4 (1977-1979, com 2 para a vitória nos pênaltis e 1 para a derrota
nos pênaltis) e 3 (1988/89 em diante); J1 sem pontos em 1993-1994 (ordem por vitórias), 3 por vitória (também nos pênaltis) e 1 pela derrota nos pênaltis em
1995-1996, 3/2/1 (tempo normal, prorrogação, pênaltis) em 1997-1998, 3/2/1 (tempo normal, prorrogação, empate) em
1999-2002, 3/1/0 de 2003 em diante. A classificação final é a tabela oficial (J1: J.League; JSL: RSSSF); nos anos de turnos, a
tabela anual oficial (1999-2004, 2015, 2016) ou a soma das tabelas dos turnos (1993-1998), com o campeão e o vice da final em
1º e 2º. Rebaixado: o clube que não está na edição seguinte (fora os que fecharam: Eidai Industries em 1976, Yokohama
Flügels em 1998) e, na J1, o marcado "J2" na tabela oficial. Em 1991/92 ninguém caiu: a JSL acabou e os clubes foram para a
J.League ou para a nova JFL. Gol contra: a J.League escreve "Own-Goal" sem o nome do jogador (`jogador` vazio, `tipo`
`contra`). A J.League não marca os gols de pênalti (ficam como `normal`). Artilheiro: o da lista de campeões da Wikipédia em inglês (a contagem oficial),
conferido com a RSSSF (JSL) e com a soma dos gols da J.League (J1).

**Conferência:** JSL: soma dos jogos da tabela de confrontos contra a tabela final da RSSSF (pontos pela regra de cada ano);
a tabela final é a mesma da Wikipédia em japonês, que cita o livro oficial da JSL. J1: cada tabela oficial de turno e anual
da J.League contra a soma dos jogos, com jogos, vitórias, empates, derrotas, gols e pontos (pela regra de cada época): todas
fecham. Placares conferidos também com o ogol (1993-1996 e 2004-2025; o ogol não tem os jogos de 1997 a 2003) e com a ESPN
(2006-2025). As diferenças listadas nas edições são erros dessas fontes: a ESPN tem placares parciais (o ogol e a tabela
oficial confirmam a J.League); o ogol de 1996 soma a disputa de pênaltis ao placar; no jogo de 2005 a J.League fecha com a
tabela oficial. Um jogo decidido fora de campo (2021, Urawa Reds x Shonan Bellmare: 2-3 em campo, 0-3 oficial) entra como
`awd`.

**Edições sem jogos:** nenhuma.

**Edições com jogos incompletos:** nenhuma. Na JSL os jogos vêm da tabela de confrontos: sem data, rodada nem autores dos gols
(menos 1988/89, que tem rodada e data); de 1977 a 1979 os empates eram decididos nos pênaltis e a página não diz quem
ganhou cada disputa (os jogos ficam como empate; as vitórias e derrotas nos pênaltis de cada clube estão na classificação).

**Resumo:** {n_j} jogos, {n_g} gols com autor, {n_c} cartões.
"""


def escrever_relatorio(arq: Path, rel, cl_l, pa_l, go_l, ca_l) -> None:
    out = [CABECALHO.format(n_ed=len(rel), n_cl=len(cl_l), n_j=len(pa_l), n_g=len(go_l), n_c=len(ca_l)).strip(), "",
           "| Temporada | Clubes | Jogos (esperados) | Gols | c/ autor | Tabelas ok / div. | Campeão | Classificação |",
           "|---|---|---|---|---|---|---|---|"]
    for e, r, gols, autores, _ in rel:
        div = len({d.split(",")[0] for d in r["difs"]}) if r["difs"] else 0
        div = min(div, r["n_tabelas"])
        out.append(f"| {e.temporada} | {r['num_clubes']} | {len(r['jogos'])} ({r['esperados']}) | {gols} | {autores} | "
                   f"{r['n_tabelas'] - div} / {div} | {r['campeao']} | {r['classificacao']} |")
    out += ["", "## Conferência e correções, edição a edição", ""]
    for e, r, gols, autores, obs_conf in rel:
        linhas = [f"### {e.temporada}", "", f"- {obs_conf}.", f"- Formato: {r['formato']}."]
        linhas += [f"- {o}." for o in r["obs"]]
        if r["difs"]:
            linhas.append("- Divergências com a tabela publicada: " + "; ".join(r["difs"]) + ".")
        if r.get("gols_dif"):
            linhas.append(f"- Jogos com os autores dos gols que não fecham com o placar (gols de fora): " + "; ".join(r["gols_dif"]) + ".")
        if r.get("espn"):
            ok, dif = r["espn"]
            if ok or dif:
                linhas.append(f"- ESPN: {ok} placares iguais" + (f"; diferentes: {'; '.join(dif)}" if dif else "") + ".")
        if r.get("ogol"):
            ok, dif = r["ogol"]
            if ok or dif:
                linhas.append(f"- ogol: {ok} placares iguais" + (f"; diferentes: {'; '.join(dif)}" if dif else "") + ".")
        reb = [c["clube"] for c in r["clf"] if c["situacao"] == "rebaixado"]
        if reb:
            linhas.append(f"- Rebaixados: {', '.join(reb)}.")
        art = r["art"]
        if art:
            linhas.append("- Artilheiro: " + "; ".join(f"{a['jogador']} ({a['clube']}), {a['gols']}" for a in art) + ".")
        if r.get("art_dif"):
            linhas.append(f"- Artilheiro: diferença entre as fontes ({r['art_dif']}); vale a Wikipédia (contagem oficial).")
        out += linhas + [""]
    arq.write_text("\n".join(out), encoding="utf-8")
