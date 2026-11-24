"""Textos do relatório da Série D que não saem do código: introdução, explicações de cada edição e o fim."""

INTRO = [
    "Gerado por `python coleta/bra-serie-d/importar.py`. Pacote em `data/coleta/bra-serie-d/pacote/`. Método e código iguais aos",
    "da Série C (`docs/coleta/bra-serie-c.md`).",
    "",
    "**Edições:** 18, de 2009 a 2026, conferidas na RSSSF Brasil (lista de campeões da 4ª divisão, até 2023) e na Wikipédia em",
    "português (artigo da Série D, até 2025). Os campeões de 2009 a 2023 são os mesmos nas duas. Nome oficial: Campeonato",
    "Brasileiro Série D.",
    "",
    "**Fontes:** RSSSF Brasil (`br{ano}l4.htm`: base de jogos, fases, grupos, datas e autores; as tabelas publicadas são a",
    "conferência); ogol (calendário de todas as edições e o código de cada clube, que dá a identidade; completa os jogos que faltam",
    "na RSSSF); Wikipédia (punições de pontos, lista de campeões, promovidos e artilheiros). A ESPN não tem a Série D.",
    "",
    "**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,",
    "fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` usa o nome de lá;",
    "clube que já apareceu na Série C usa o mesmo nome do pacote da Série C (cadastro comum `data/coleta/comum/clubes_ogol.json`).",
    "",
    "**Fases e grupos (revisão SD-004 a SD-009):** saem do código de cada jogo no ogol, que tem a estrutura completa da Série D",
    "(grupos numerados; FP, 2F, 3F, 1/8, QF, SF e F para o mata-mata). As páginas da RSSSF perdem grupos (2018, 2020, 2022),",
    "juntam fases (2011) e põem jogos de mata-mata em grupos (2021). O nome do grupo é o da RSSSF quando ela o dá certo.",
    "",
    "**Classificação final (revisão SD-002, SD-003):** campeão e vice em cima; depois a fase alcançada; na mesma fase, a",
    "posição no grupo dela e a campanha toda. A ordem geral da RSSSF, quando existe, só desempata dentro da mesma fase.",
]

# ano -> explicações conferidas à mão (contexto das ocorrências listadas logo abaixo de cada ano)
EXPLICACOES: dict[int, list[str]] = {
    2026: ["a RSSSF ainda não tem a página de 2026: os jogos, as fases e os grupos vêm do ogol (revisão SD-001). Os perdedores "
           "das quartas jogaram uma repescagem pelas duas últimas vagas de acesso (Nacional-AM e Goiatuba subiram). Sem autores de gols"],
    2011: ["dois jogos da página foram anulados e ficam de fora (motivo abaixo); com isso, jogos e tabelas batem com o ogol"],
    2012: ["a página da RSSSF não traz os autores dos gols"],
    2016: ["as tabelas desta página (e de 2017 a 2019) têm uma coluna a mais ('PTS J PE V E D'); o leitor reconhece essa ordem"],
    2020: ["a página da RSSSF parou no meio da 2ª fase (472 dos 518 jogos); o resto vem do ogol"],
    2021: ["clubes, grupos e jogos que faltam vêm do ogol; os autores dos gols só existem nos 103 jogos da página"],
    2023: ["a página da RSSSF não publica tabelas e parou antes do fim (478 dos 510 jogos): conferência só pelo ogol, que tem o mesmo "
           "placar em todos os jogos em comum"],
}

FIM = [
    "## Identidade dos clubes",
    "",
    "- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol (`data/coleta/bra-serie-d/ogol/clubes.json`).",
    "- Clube do `futebol.db` usa o nome de lá; clube da Série C usa o nome do pacote da Série C; os outros seguem o nome curto do",
    "  ogol, com \"-UF\" só quando outro clube tem o mesmo nome. Os nomes de cada fonte e ano estão em `clubes.csv` (`nomes_fonte`).",
    "- O Espírito Santo FC (Alegre-ES, 2016-2018) aparece com o nome com que jogou, e não com o posterior \"Rive A.C.\" (D-03).",
    "  Botafogo-DF no Guará (DF), onde jogava em 2007-2010, e AA Araguaia em Água Boa (MT) (revisão CL-028).",
    "",
    "## O que não deu para coletar",
    "",
    "- **Cartões:** nenhuma das fontes lidas traz cartões da Série D. O ogol tem na página de cada jogo (fica para depois, se aprovado).",
    "- **Autores dos gols:** só onde a RSSSF traz e a soma fecha com o placar.",
    "- **Hora, estádio e público:** a ESPN não tem a Série D; hora pelo ogol e estádio só nas páginas da RSSSF que trazem.",
    "- **Classificação final:** calculada (fase alcançada, pontos, vitórias, saldo, gols pró) quando a RSSSF não publica a geral.",
]
