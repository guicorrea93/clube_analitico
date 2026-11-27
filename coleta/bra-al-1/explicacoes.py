"""Textos do relatório do Campeonato Alagoano (1ª divisão) que não saem do código: introdução, explicações de cada
temporada e o fim."""

INTRO = [
    "Gerado por `python coleta/bra-al-1/importar.py`. Pacote em `data/coleta/bra-al-1/pacote/`. Mesmo código do",
    "Pernambucano (`docs/coleta/bra-pe-1.md`), com as fontes de Alagoas.",
    "",
    "**Temporadas:** 1918 a 2026, 105 edições (escopo aprovado pelo Guilherme em 27/11/2026; a conta da FAF): 1918-1926 são",
    "os campeonatos da Liga, reconhecidos pela CBF em 2026. Ficam de fora 1931, 1932 e 1934 (suspensos), 1943 (não terminou)",
    "e o Torneio Centenário de 1922. Título dividido: 1953 (ASA e Ferroviário). Edições sem página da RSSSF e sem jogos no",
    "ogol entram só com campeão e vice.",
    "",
    "**Fontes:** RSSSF Brasil (`tablesae/al{ano}.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada",
    "edição, jogos a partir de 1995, e o código de cada clube); Wikipédia em português (artigo \"Campeonato Alagoano de",
    "Futebol Masculino\": campeão e vice de cada ano, segunda fonte); lista de campeões da FAF.",
    "",
    "**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,",
    "fica a da RSSSF. Os gols da prorrogação entram no placar (o dos 90 minutos fica na observação). W.O. conta como vitória",
    "sem gols (decisão D-15). Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db`",
    "ou nos outros pacotes usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).",
]

# temporada -> explicações conferidas à mão (contexto das ocorrências listadas logo abaixo de cada temporada)
EXPLICACOES: dict[str, list[str]] = {}

FIM = [
    "## Identidade dos clubes",
    "",
    "- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.",
    "- Nos anos sem jogos no ogol, o clube é casado pelo nome com o das outras temporadas (importar.NOME_CODIGO e NOME_ANO).",
    "- Clube que o ogol não tem entra pela RSSSF, com código \"rs-al1-<nome>\". Nunca com o nome exato de outro clube.",
    "",
    "## O que não deu para coletar",
    "",
    "- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).",
    "- **Autores dos gols:** só entram quando a soma bate com o placar.",
    "- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;",
    "  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.",
]
