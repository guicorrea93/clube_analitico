"""Textos do relatório do Campeonato Cearense (1ª divisão) que não saem do código: introdução, explicações de cada
temporada e o fim."""

INTRO = [
    "Gerado por `python coleta/bra-ce-1/importar.py`. Pacote em `data/coleta/bra-ce-1/pacote/`. Mesmo código do Paranaense",
    "(`docs/coleta/bra-pr-1.md`), com as fontes do Ceará.",
    "",
    "**Temporadas:** 1915 a 2026, 112 edições (escopo aprovado pelo Guilherme em 25/11/2026; a conta da FCF). Ficam fora 1913",
    "(campeão desconhecido) e 1914 (a FCF não reconhece). 1915-1919 são os torneios da Liga Metropolitana, reconhecidos pela",
    "FCF em 2008 (Ato nº 11/2008). 17 edições sem jogos em nenhuma fonte (1916-1919, 1924-1927, 1929-1932, 1934-1938) entram",
    "só com campeão e vice. 1992 teve título dividido entre Fortaleza, Ceará, Tiradentes e Icasa; em 2004 não houve final",
    "(o STJD deu o título ao Fortaleza).",
    "",
    "**Fontes:** RSSSF Brasil (`tablesae/ce{ano}.htm`: jogos, fases, datas, autores e tabelas; quando o site não respondeu,",
    "a cópia do Internet Archive, listada em `data/coleta/bra-ce-1/rsssfbrasil/origem.json`); ogol (calendário de cada edição",
    "e o código de cada clube); Wikipédia em português (artigo \"Campeonato Cearense de Futebol Masculino\": campeão e vice",
    "de cada ano, segunda fonte). Artilheiros pela lista da RSSSF (`cetops.htm`).",
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
    "- Clube que o ogol não tem entra pela RSSSF, com código \"rs-ce1-<nome>\". Nunca com o nome exato de outro clube.",
    "",
    "## O que não deu para coletar",
    "",
    "- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).",
    "- **Autores dos gols:** só entram quando a soma bate com o placar.",
    "- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;",
    "  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.",
]
