"""Textos do relatório do Campeonato Carioca (1ª divisão) que não saem do código: introdução, explicações de cada
temporada e o fim."""

INTRO = [
    "Gerado por `python coleta/bra-rj-1/importar.py`. Pacote em `data/coleta/bra-rj-1/pacote/`. Mesmo código do Paulista",
    "(`docs/coleta/bra-sp-1.md`), com as fontes do Rio.",
    "",
    "**Temporadas:** 1906 a 2026. Até 1959 é o campeonato do Distrito Federal (a cidade do Rio de Janeiro); de 1960 a 1974,",
    "o do estado da Guanabara; de 1975 em diante, o do estado do Rio de Janeiro. Nos anos de ligas rivais cada torneio",
    "reconhecido é uma edição: 1912 (AFRJ e LMSA), 1924 (LMDT e AMEA), 1933 e 1934 (AMEA e LCF), 1935 e 1936 (FMD e LCF),",
    "1937 (LFRJ, a liga da pacificação, na temporada \"1937\"; e o torneio inacabado da FMD, \"1937 FMD\", título homologado",
    "pela FERJ em 2023).",
    "1979 teve dois campeonatos reconhecidos: o Especial (fevereiro a abril) e o normal (maio a setembro). O campeonato do",
    "antigo estado do Rio (interior, até 1978) é outra competição e fica de fora.",
    "",
    "**Fontes:** RSSSF Brasil (`tablesr/rj{ano}.htm`: jogos, fases, datas, autores e tabelas; `rj1979s.htm`: o Especial de",
    "1979; não há página de 2025 nem de 2026); ogol (calendário de cada edição, de 1906 a 2026, e o código de cada clube;",
    "confere placares, traz a rodada e completa os jogos que a página não traz); Wikipédia em português (artigo do",
    "Campeonato Carioca: campeões e vices de cada ano, segunda fonte do campeão). Artilheiros pela lista da RSSSF",
    "(`rjtops.htm`).",
    "",
    "**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,",
    "fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` ou nos",
    "outros pacotes usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).",
]

# temporada -> explicações conferidas à mão (contexto das ocorrências listadas logo abaixo de cada temporada)
EXPLICACOES: dict[str, list[str]] = {
    "1907": ["título dividido entre Fluminense e Botafogo: terminaram empatados (Botafogo 10 pontos e Fluminense 8 na tabela "
             "da RSSSF, os dois com 2 pontos perdidos), não houve acordo sobre o desempate e a LMSA acabou sem declarar campeão; "
             "em 1996 a FERJ declarou os dois campeões (RSSSF; Lance; Wikipédia). O pacote tem o Fluminense no campo campeao, o "
             "vice vazio e o Botafogo na observação até o banco aceitar dois campeões numa edição (D-07, como o Paulista 1973)"],
    "1921": ["o desempate Flamengo x América foi 1-1 no tempo normal e 1-0 na prorrogação: fica 2-1 para o Flamengo"],
    "1937": ["torneio da LFRJ (a liga da pacificação: FMD e LCF juntas), campeão o Fluminense. O torneio da FMD, disputado "
             "antes, é a edição \"1937 FMD\""],
    "1937 FMD": ["torneio da FMD, que parou na 8ª rodada (26 jogos, de 02/05 a 11/07) com a pacificação entre a FMD e a LCF; "
                 "os jogos não foram anulados. A FMD proclamou o São Cristóvão campeão em 03/09/1937 (invicto, 7 vitórias em 7 "
                 "jogos); o título ficou esquecido e a FERJ o homologou em dezembro de 2023, depois do dossiê do jornalista André "
                 "Luiz Pereira Nunes (cerimônia em 13/01/2024; Super Rádio Tupi, 09/01/2024). A lista de campeões da RSSSF é de "
                 "antes e ainda diz \"unfinished\": o campeão vem de importar.CAMPEOES_MANUAIS. O ogol não tem essa edição; os "
                 "jogos vêm só da RSSSF"],
    "1979": ["artilheiro: a RSSSF dá Zico 26 no campeonato normal e 34 no Especial; a Wikipédia, o contrário. Fica a RSSSF"],
}

FIM = [
    "## Identidade dos clubes",
    "",
    "- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.",
    "- Clube que o ogol não tem entra pela RSSSF, com código \"rs-<nome>\". Nunca com o nome exato de outro clube (regra 6b).",
    "- Mesmo clube com outro nome fica com o nome de hoje (Botafogo Football Club e Botafogo de Futebol e Regatas, depois da",
    "  fusão de 1942).",
    "",
    "## O que não deu para coletar",
    "",
    "- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).",
    "- **Autores dos gols:** 3.383 gols com autor, quase todos de 2010 em diante (74% dos gols dos anos 2010). Nas outras",
    "  décadas a RSSSF não traz os autores ou traz num formato que o leitor ainda não junta ao jogo (\"Gols: ...\" na linha de",
    "  baixo, nos anos 1900); só entram quando a soma bate com o placar (pendência).",
    "- **W.O. sem vencedor:** o ogol traz cerca de 66 W.O. (1908-1935) sem dizer quem venceu; o vencedor sai da tabela",
    "  publicada, e o W.O. conta como vitória sem gols. Sem como decidir pela tabela, fica fora (ver as temporadas).",
    "- **Torneios à parte:** os de consolação entre os turnos (2009-2012) e as séries de subúrbio (1928-1930) ficam fora.",
    "- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima.",
]
