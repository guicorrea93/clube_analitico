"""Textos do relatório do Campeonato Paranaense (1ª divisão) que não saem do código: introdução, explicações de cada
temporada e o fim."""

INTRO = [
    "Gerado por `python coleta/bra-pr-1/importar.py`. Pacote em `data/coleta/bra-pr-1/pacote/`. Mesmo código do Gaúcho",
    "(`docs/coleta/bra-rs-1.md`), com as fontes do Paraná.",
    "",
    "**Temporadas:** 1915 a 2026 (escopo aprovado pelo Guilherme em 25/11/2026). Em 2002 são duas edições: \"2002\", o",
    "campeonato oficial da FPF, e \"2002 Supercampeonato\", com os clubes da Copa Sul-Minas (não oficial). 1980 teve título",
    "dividido (Colorado e Cascavel). De 1935 a 1941, depois do campeonato de Curitiba, há a fase estadual com os campeões das",
    "ligas do interior.",
    "",
    "**Fontes:** RSSSF Brasil (`tablesfq/pr{ano}.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada",
    "edição e o código de cada clube; não tem jogos de 1915 a 2000, salvo 1965 e 1967); Wikipédia em português (artigo do",
    "Campeonato Paranaense: campeão e vice de cada ano, segunda fonte). Artilheiros pela lista da RSSSF (`prtops.htm`).",
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
    "- De 1915 a 2000 o ogol não tem os jogos: o clube é casado pelo nome (importar.NOME_CODIGO e NOME_ANO).",
    "- Clube que o ogol não tem entra pela RSSSF, com código \"rs-pr1-<nome>\". Nunca com o nome exato de outro clube.",
    "",
    "## O que não deu para coletar",
    "",
    "- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).",
    "- **Autores dos gols:** só entram quando a soma bate com o placar.",
    "- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;",
    "  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.",
]
