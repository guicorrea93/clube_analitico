"""Textos do relatório do Paulista Série A2 (2ª divisão) que não saem do código: introdução, explicações de cada temporada
e o fim."""

INTRO = [
    "Gerado por `python coleta/bra-sp-2/importar.py`. Pacote em `data/coleta/bra-sp-2/pacote/`. Mesmo código do Paulista",
    "(`docs/coleta/bra-sp-1.md`), com as fontes da 2ª divisão.",
    "",
    "**Temporadas:** as que têm os jogos em alguma fonte: 1979, 1985-1988 e 1995-2026. Nome oficial de cada época na",
    "lista da RSSSF (Segunda Divisão, Divisão Intermediária, Divisão Especial; Série A2 desde 1994). Campeões conferidos",
    "na lista da RSSSF (`sp2camp.htm`).",
    "",
    "**Fontes:** RSSSF Brasil (`sp{ano}l2.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada edição,",
    "de 1998 em diante, e o código de cada clube; confere placares, traz a rodada e completa os jogos que a página não traz).",
    "Artilheiros pela lista da RSSSF (`sp2tops.htm`). 2026 vem só do ogol (a RSSSF ainda não tem a página).",
    "",
    "**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,",
    "fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` ou nos",
    "outros pacotes usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`). Acesso: o clube que joga a 1ª",
    "divisão do ano seguinte (pacote `bra-sp-1`).",
    "",
    "**Ficam de fora** (decisão pendente com o Guilherme) as temporadas sem os jogos: 1947-1966 (a RSSSF traz só a",
    "classificação final em pontos e os jogos do campeão), 1989 (só a 1ª fase; a final está no ogol), 1991 (só a 2ª fase),",
    "1992-1994 (só a classificação), os anos sem página (1965, 1967-1978, 1980-1984, 1990) e a fase amadora (1916-1946,",
    "só a lista de campeões).",
]

# temporada -> explicações conferidas à mão (contexto das ocorrências listadas logo abaixo de cada temporada)
EXPLICACOES: dict[str, list[str]] = {
    "1985": ["Nacional x São Bernardo (31/08): a vitória foi dada ao São Bernardo no tribunal, sem placar (o jogo terminou 0 a 0 "
             "e o Nacional escalou jogador irregular); Barretos x Sãocarlense (18/08): vitória dada ao Barretos (1 a 1 em campo)"],
    "1988": ["69 jogos vêm na página só com o resultado (\"venceu\", \"empatou\", \"perdeu\" ou \"-\"), sem placar, e ficam fora "
             "do pacote; por isso as tabelas da 1ª fase não fecham. O ogol não tem esses jogos"],
    "1995": ["a página não tem a lista de participantes: Internacional (de Limeira), Botafogo (de Ribeirão Preto), Nacional "
             "(da capital) e Catanduva (o GE Catanduvense, que mudou de nome em 1994) foram casados à mão"],
    "1997": ["Ferroviária 1x1 Noroeste (23/02): jogo inacabado; a FPF deu a vitória à Ferroviária, e a tabela conta 1 a 0. "
             "A 1ª fase vai do jogo entre grupos (8 rodadas) ao turno e returno dentro dos grupos (14 rodadas), como nas "
             "tabelas da página (22 jogos por clube)"],
    "2000": ["a 1ª fase tem semifinal e final próprias: o Botafogo venceu e subiu para a 1ª divisão no meio do ano (não joga "
             "a 2ª fase); o título da A2 é do vencedor da 2ª fase em diante"],
    "2001": ["campeão: Etti Jundiaí, nome do Paulista FC de 1999 a 2001 (patrocínio)"],
}

FIM = [
    "## Identidade dos clubes",
    "",
    "- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.",
    "- Antes de 1998 o ogol não tem os jogos: o nome da página é casado com as fichas do ogol (da A2 e da A1) pela **cidade**",
    "  da lista de participantes da mesma página (\"AA Portuguesa (Santos)\" é a Portuguesa Santista; \"EC Corinthians",
    "  (Presidente Prudente)\" é o Corinthians Prudente). Ficha de clube fundado depois da edição não vale (a AA",
    "  Votuporanguense dos anos 1980 não é o CA Votuporanguense, de 2009; o EC Lemense não é o Lemense FC, de 2005).",
    "- Clube que o ogol não tem entra pela RSSSF, com código \"rs-<nome>-<cidade>\". Nunca com o nome exato de outro clube",
    "  (regra 6b): \"Palmeiras (São João da Boa Vista)\", \"Internacional de Bebedouro\", \"União Mogi\", \"EC Lemense\".",
    "- Ferroviário Atlético Ituano é o Ituano de hoje (mesmo clube, nome antigo).",
    "",
    "## O que não deu para coletar",
    "",
    "- **Edições sem os jogos:** veja \"Ficam de fora\" acima.",
    "- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).",
    "- **Autores dos gols:** só onde a RSSSF traz (a partir de 2013) e a soma fecha com o placar.",
    "- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;",
    "  torneio de rebaixamento e repescagem não contam como fase alcançada.",
]
