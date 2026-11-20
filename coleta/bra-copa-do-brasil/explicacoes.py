"""Textos do relatório da Copa do Brasil que não saem do código: introdução, explicações de cada edição e o fim."""

INTRO = [
    "Gerado por `python coleta/bra-copa-do-brasil/importar.py`. Pacote em `data/coleta/bra-copa-do-brasil/pacote/`. Método e",
    "código iguais aos da Série C (`docs/coleta/bra-serie-c.md`).",
    "",
    "**Edições:** 37, de 1989 a 2025, conferidas na RSSSF Brasil (cbrcamp.htm) e na Wikipédia em português (artigo da Copa do",
    "Brasil). A Taça Brasil (1959-1968) não entra: já está no banco como parte da Série A.",
    "",
    "**Fontes:** RSSSF Brasil (`cbr{ano}.htm`: jogos, fases, datas e autores; tabelas, quando há fase de grupos); ogol",
    "(calendário de todas as edições e o código de cada clube; confere placares e completa jogos); Wikipédia (lista de campeões).",
    "",
    "**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,",
    "fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` ou nos pacotes",
    "das Séries C e D usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).",
]

# ano -> explicações conferidas à mão (contexto das ocorrências listadas logo abaixo de cada ano)
EXPLICACOES: dict[int, list[str]] = {
    1991: ["o Grêmio venceu o Auto Esporte e o Fluminense de Feira pelos mesmos placares; o Fluminense(BA) da página é ligado à mão "
           "ao Fluminense de Feira do ogol"],
    1994: ["vários jogos da página vêm com a data do título da fase (março), quando foram jogados em maio; casados com o ogol pelo "
           "par de clubes e pelo placar, e vale a data do ogol"],
    2000: ["as oitavas vêm com uma letra antes de cada confronto ('E ABC (RN) x Palmeiras (SP)'); a letra sai"],
    2001: ["a página começa com a seletiva do Espírito Santo, que não é Copa do Brasil; esse trecho fica de fora"],
    2003: ["a página começa com o jogo seletivo Paraná x Coritiba, que não é Copa do Brasil; fica de fora"],
    2015: ["nesta página o primeiro clube de cada confronto manda o jogo de volta (e não o de ida); o ogol e os autores dos gols "
           "confirmam, e o leitor inverte o mando"],
    2016: ["mesmo caso de 2015: o primeiro clube de cada confronto manda o jogo de volta"],
}

FIM = [
    "## Identidade dos clubes",
    "",
    "- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.",
    "- Clube do `futebol.db` usa o nome de lá; clube das Séries C e D usa o nome daqueles pacotes; os outros seguem o nome curto",
    "  do ogol, com \"-UF\" só quando outro clube de outro estado tem o mesmo nome.",
    "",
    "## O que não deu para coletar",
    "",
    "- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade, combinado com o Guilherme).",
    "- **Autores dos gols:** só onde a RSSSF traz e a soma fecha com o placar.",
    "- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com campeão e vice em cima.",
]
