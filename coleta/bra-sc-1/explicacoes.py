"""Textos do relatório do Campeonato Catarinense (1ª divisão) que não saem do código: introdução, explicações de cada
temporada e o fim."""

INTRO = [
    "Gerado por `python coleta/bra-sc-1/importar.py`. Pacote em `data/coleta/bra-sc-1/pacote/`. Mesmo código do Goiano",
    "(`docs/coleta/bra-go-1.md`), com as fontes de Santa Catarina.",
    "",
    "**Temporadas:** 1924 a 2026, 102 edições (escopo aprovado pelo Guilherme em 27/11/2026). Fica fora 1946, que não foi",
    "disputado. 1924-1926 e 1934-1936 eram os campeonatos da capital, homologados como estaduais pela FCF. 1933 não terminou",
    "e fica sem campeão. Em 1935 só entra o campeonato da FCD (o da ACD, de Joinville, a FCF não reconhece).",
    "",
    "**Fontes:** RSSSF Brasil (`tablessz/sc{ano}.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada",
    "edição e o código de cada clube; jogos a partir dos anos 2000); Wikipédia em português (artigo \"Campeonato Catarinense",
    "de Futebol Masculino\": campeão e vice de cada ano, segunda fonte).",
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
    "- Clube que o ogol não tem entra pela RSSSF, com código \"rs-sc1-<nome>\". Nunca com o nome exato de outro clube.",
    "",
    "## O que não deu para coletar",
    "",
    "- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).",
    "- **Autores dos gols:** só entram quando a soma bate com o placar.",
    "- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;",
    "  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.",
]
