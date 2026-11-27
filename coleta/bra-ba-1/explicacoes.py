"""Textos do relatório do Campeonato Baiano (1ª divisão) que não saem do código: introdução, explicações de cada
temporada e o fim."""

INTRO = [
    "Gerado por `python coleta/bra-ba-1/importar.py`. Pacote em `data/coleta/bra-ba-1/pacote/`. Mesmo código do Catarinense",
    "(`docs/coleta/bra-sc-1.md`), com as fontes da Bahia.",
    "",
    "**Temporadas:** 1905 a 2026, 122 edições (escopo aprovado pelo Guilherme em 27/11/2026). Em 1915 e 1916 só entra o",
    "campeonato oficial (o da liga rival, a LSB, ninguém reconhece). Títulos divididos: 1938 (o cisma; Bahia e Botafogo) e",
    "1999 (Bahia e Vitória). Edições sem página da RSSSF e sem jogos no ogol entram só com campeão e vice.",
    "",
    "**Fontes:** RSSSF Brasil (`tablesae/ba{ano}.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada",
    "edição e o código de cada clube; jogos a partir de 1999); Wikipédia em português (artigo \"Campeonato Baiano de Futebol",
    "Masculino\": campeão e vice de cada ano, segunda fonte).",
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
    "- Clube que o ogol não tem entra pela RSSSF, com código \"rs-ba1-<nome>\". Nunca com o nome exato de outro clube.",
    "",
    "## O que não deu para coletar",
    "",
    "- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).",
    "- **Autores dos gols:** só entram quando a soma bate com o placar.",
    "- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;",
    "  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.",
]
