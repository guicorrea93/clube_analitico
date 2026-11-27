"""Textos do relatório do Campeonato Pernambucano (1ª divisão) que não saem do código: introdução, explicações de cada
temporada e o fim."""

INTRO = [
    "Gerado por `python coleta/bra-pe-1/importar.py`. Pacote em `data/coleta/bra-pe-1/pacote/`. Mesmo código do Baiano",
    "(`docs/coleta/bra-ba-1.md`), com as fontes de Pernambuco.",
    "",
    "**Temporadas:** 1915 a 2026, 112 edições (escopo aprovado pelo Guilherme em 27/11/2026). Nenhum título dividido. A",
    "edição 2026/27 (Turno Forró em 2026, Turno Frevo em 2027) fica de fora até terminar. Edições sem página da RSSSF e sem",
    "jogos no ogol (1991-1993) entram só com campeão e vice.",
    "",
    "**Fontes:** RSSSF Brasil (`tablesfq/pe{ano}.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada",
    "edição e o código de cada clube); Wikipédia em português (artigo \"Campeonato Pernambucano de Futebol Masculino\":",
    "campeão e vice de cada ano, segunda fonte).",
    "",
    "**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,",
    "fica a da RSSSF. Os gols da prorrogação entram no placar (o dos 90 minutos fica na observação). W.O. conta como vitória",
    "sem gols (decisão D-15); vitória sem placar conhecido também (como no Mineiro), com o vencedor na observação. Autores dos",
    "gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` ou nos outros pacotes usa o mesmo",
    "nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).",
]

# temporada -> explicações conferidas à mão (contexto das ocorrências listadas logo abaixo de cada temporada)
EXPLICACOES: dict[str, list[str]] = {}

FIM = [
    "## Identidade dos clubes",
    "",
    "- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.",
    "- Nos anos sem jogos no ogol, o clube é casado pelo nome com o das outras temporadas (importar.NOME_CODIGO e NOME_ANO).",
    "- Clube que o ogol não tem entra pela RSSSF, com código \"rs-pe1-<nome>\". Nunca com o nome exato de outro clube.",
    "",
    "## O que não deu para coletar",
    "",
    "- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).",
    "- **Autores dos gols:** só entram quando a soma bate com o placar.",
    "- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;",
    "  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.",
]
