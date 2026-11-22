"""Textos do relatório do Paulista Série A2 (2ª divisão) que não saem do código: introdução, explicações de cada temporada
e o fim."""

INTRO = [
    "Gerado por `python coleta/bra-sp-2/importar.py`. Pacote em `data/coleta/bra-sp-2/pacote/`. Mesmo código do Paulista",
    "(`docs/coleta/bra-sp-1.md`), com as fontes da 2ª divisão.",
    "",
    "**Temporadas:** 1947-1966, 1979 e 1985-2026 (63 edições). Com os jogos: 1979, 1985-1988 e 1995-2026; com parte",
    "dos jogos: 1989 e 1991, e várias de 1948-1966, 1990 e 1992 (os jogos que a Wikipédia em português traz); sem jogo",
    "nenhum: 1947, 1993 e 1994 (só a tabela ou a ordem final). Nome oficial de cada época na lista da RSSSF (Segunda",
    "Divisão, Primeira Divisão, Divisão Intermediária, Divisão Especial; Série A2 desde 1994). Campeões conferidos na lista",
    "da RSSSF (`sp2camp.htm`).",
    "",
    "**Fontes:** RSSSF Brasil (`sp{ano}l2.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada edição,",
    "de 1998 em diante, e o código de cada clube; confere placares, traz a rodada e completa os jogos que a página não traz).",
    "Artilheiros pela lista da RSSSF (`sp2tops.htm`). 2026 vem só do ogol (a RSSSF ainda não tem a página).",
    "Wikipédia em português (`data/coleta/bra-sp-2/wikipedia/`: o código das páginas de cada edição e os jogos transcritos",
    "delas em `jogos_pt.csv`, cada um conferido no código da página): 1965 e 1990 (sem página da RSSSF), os jogos que a",
    "RSSSF não traz (finais e fases finais de 1948-1966, a 4ª fase de 1990, a 2ª fase e o quadrangular de 1992, as",
    "semifinais de 1989). Lista de participantes da RSSSF (`sp2list.htm`): a cidade de cada clube de 1947 a 1966.",
    "",
    "**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,",
    "fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` ou nos",
    "outros pacotes usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`). Acesso: o clube que joga a 1ª",
    "divisão do ano seguinte (pacote `bra-sp-1`).",
    "",
    "**Edições sem os jogos** (decisão do Guilherme, 21/11/2026: incluir tudo o que existir), como as do `uru-1` e do",
    "`par-1`: a classificação final vem das tabelas publicadas. Campeão pela lista da RSSSF; vice, o outro finalista (o 1º",
    "do outro grupo da última fase, ou o 2º da tabela única); depois a fase alcançada, a posição no grupo e os pontos da",
    "última fase. Pontos, vitórias, empates e derrotas só quando a edição tem uma tabela só; nas outras, os pontos de cada",
    "fase vão na observação da linha. 1992 e 1993: a página dá só faixas (\"eliminados na 2ª fase, do 5º ao 12º\"), e os",
    "clubes da faixa ficam empatados na posição do começo dela. 1990: os eliminados antes da 4ª fase ficam empatados em 7º.",
    "Os jogos dos campeões listados nas páginas da RSSSF de 1947-1966 não entraram (só os de um clube; a Wikipédia traz as",
    "finais).",
    "",
    "**Ficam de fora** os anos sem 2ª divisão ou sem nenhuma fonte (1967-1978, 1980-1984) e a fase amadora (1916-1946,",
    "só a lista de campeões).",
]

# temporada -> explicações conferidas à mão (contexto das ocorrências listadas logo abaixo de cada temporada)
EXPLICACOES: dict[str, list[str]] = {
    "1985": ["Nacional x São Bernardo (31/08): a vitória foi dada ao São Bernardo no tribunal, sem placar (o jogo terminou 0 a 0 "
             "e o Nacional escalou jogador irregular); Barretos x Sãocarlense (18/08): vitória dada ao Barretos (1 a 1 em campo)"],
    "1948": ["a Internacional da Série Branca é a de Bebedouro (Wikipédia); a página da RSSSF repete \"(Limeira)\""],
    "1954": ["2ª fase: a página traz uma tabela calculada dos jogos (Taubaté 16, Comercial 11) e a classificação oficial "
             "(Taubaté 14, Comercial 13); vale a oficial. Os 30 jogos da Wikipédia fecham com a calculada"],
    "1988": ["69 jogos vêm na página só com o resultado (\"venceu\", \"empatou\", \"perdeu\" ou \"-\"), sem placar, e ficam fora "
             "do pacote; por isso as tabelas da 1ª fase não fecham. O ogol e a Wikipédia não têm esses jogos"],
    "1991": ["campeão: Araçatuba, empatado em pontos com o Lemense no quadrangular e na frente pelo saldo. A página da RSSSF "
             "diz \"Campeão: Lemense\", mas a lista de campeões da RSSSF, a Wikipédia e o Futebol Interior dão o Araçatuba"],
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
    "- 1947-1966: a cidade vem da própria tabela (\"AA Ferroviária (Botucatu)\") ou da lista de participantes da RSSSF;",
    "  o casamento com a ficha do ogol exige a mesma cidade e o nome igual ou contido (\"XV de Novembro\" em \"Esporte Clube",
    "  XV de Novembro\"), de clube já fundado. O Barretos FC (até 1960) não é o Barretos EC (1960); o Catanduva EC dos anos",
    "  1950 não é o GE Catanduvense (1970); a AA Osvaldo Cruz não é o Osvaldo Cruz FC (2004); o Araçatuba FC de 1954 não é",
    "  a AE Araçatuba (1972). Homônimos levam a cidade: \"Ferroviária (Botucatu)\", \"São Paulo (Araçatuba)\",",
    "  \"Comercial (Lins)\", \"Paulista (Araraquara)\", \"São Bento (Marília)\".",
    "",
    "## O que não deu para coletar",
    "",
    "- **Jogos que faltam:** 1947-1966 (fora o que a Wikipédia traz), 1989 (2ª e 3ª fases), 1990 (1ª a 3ª fases), 1991",
    "  (1ª fase), 1992 (1ª fase e 6 jogos só com o resultado), 1993 e 1994 (todos), 1988 (69 sem placar). Só há esses",
    "  jogos em jornais da época (Hemeroteca Digital, acervos do Estadão e da Folha), em imagem.",
    "- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).",
    "- **Autores dos gols:** só onde a RSSSF traz (a partir de 2013) e a soma fecha com o placar.",
    "- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;",
    "  torneio de rebaixamento e repescagem não contam como fase alcançada.",
]
