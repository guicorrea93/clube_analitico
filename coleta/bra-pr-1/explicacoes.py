"""Textos do relatório do Campeonato Paranaense (1ª divisão) que não saem do código: introdução, explicações de cada
temporada e o fim."""

INTRO = [
    "Gerado por `python coleta/bra-pr-1/importar.py`. Pacote em `data/coleta/bra-pr-1/pacote/`. Mesmo código do Mineiro",
    "(`docs/coleta/bra-mg-1.md`), com as fontes do Rio Grande do Sul.",
    "",
    "**Temporadas:** 1919 a 2026 (escopo aprovado pelo Guilherme em 25/11/2026). 1918, 1923 e 1924 não foram disputados.",
    "Até 1960 o campeonato era por regiões: os campeões das cidades disputavam os regionais e os campeões regionais, a fase",
    "estadual. Entram a fase estadual e as decisões de zona e região que a página da RSSSF traz (\"Fase regional\"), não os",
    "campeonatos das cidades. A Divisão Especial, com clubes de todo o estado, começou em 1961. 1930 foi organizado pela",
    "FAGET, no lugar da FRGD.",
    "",
    "**Fontes:** RSSSF Brasil (`tablesfq/pr{ano}.htm`, 1919-2024: jogos, fases, datas, autores e tabelas); ogol (calendário",
    "de cada edição e o código de cada clube; não tem jogos de 1925 a 1976, salvo 1965; 2025 e 2026 só nele); Wikipédia em",
    "português (artigo do Campeonato Paranaense: campeão e vice de cada ano, segunda fonte). Artilheiros pela lista da RSSSF",
    "(`prtops.htm`), menos 1940-1960, em que ela traz os do campeonato de Porto Alegre.",
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
    "- De 1925 a 1976 o ogol não tem os jogos: o clube é casado pelo nome com o das outras temporadas.",
    "- Clube que o ogol não tem entra pela RSSSF, com código \"rs-<nome>\". Nunca com o nome exato de outro clube (regra 6b).",
    "",
    "## O que não deu para coletar",
    "",
    "- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).",
    "- **Autores dos gols:** só entram quando a soma bate com o placar.",
    "- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;",
    "  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.",
]
