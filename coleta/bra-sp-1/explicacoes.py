"""Textos do relatório do Paulista (1ª divisão) que não saem do código: introdução, explicações de cada temporada e o fim."""

INTRO = [
    "Gerado por `python coleta/bra-sp-1/importar.py`. Pacote em `data/coleta/bra-sp-1/pacote/`. Método e",
    "código iguais aos da Série C (`docs/coleta/bra-serie-c.md`).",
    "",
    "**Temporadas:** 134, de 1902 a 2025. Nos anos de duas ligas (1913-1916 e 1935-1936: LPF e APEA; 1926-1929: APEA e LAF)",
    "cada liga é uma temporada própria (\"1913 LPF\", \"1913 APEA\"), com o mesmo ano. Campeões conferidos na RSSSF Brasil",
    "(spcamp.htm) e na Wikipédia em português (\"Campeonato Paulista de Futebol\").",
    "",
    "**Fontes:** RSSSF Brasil (`sp{ano}.htm`: jogos, fases, datas, autores e tabelas); ogol (calendário de cada edição e o",
    "código de cada clube; confere placares, traz a rodada e completa jogos); Wikipédia (lista de campeões).",
    "",
    "**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,",
    "fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` ou nos pacotes",
    "das Séries C e D e da Copa do Brasil usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).",
    "Palestra Itália e Palmeiras são o mesmo clube (o ogol já os junta). Os homônimos antigos levam \"-SP\" quando o nome",
    "já é de um clube de outro estado (\"Internacional-SP\").",
    "",
    "**Fica de fora** o que a página da RSSSF (ou o calendário do ogol) traz junto e não é o campeonato: a seletiva de 1910;",
    "os 2º e 3º níveis de 1985; o Troféu do Interior (2007-2013 e 2017-2022) e a Taça Independência (2023), torneios à parte",
    "dos clubes já eliminados; e o Supercampeonato de 2002. As repescagens contra clubes da 2ª divisão (1951, 1979, 2003) entram,",
    "como na RSSSF.",
]

# temporada -> explicações conferidas à mão (contexto das ocorrências listadas logo abaixo de cada temporada)
EXPLICACOES: dict[str, list[str]] = {
    "1905": ["Paulistano x AA das Palmeiras não foi jogado e a vitória foi dada ao Paulistano sem placar (\"awarded 0-0\"); "
             "fica 0 a 0 com resultado especial, e por isso a campanha do Paulistano e a da AA das Palmeiras não fecham com a "
             "tabela publicada (que conta a vitória); o ogol registra 1 a 0"],
    "1914 APEA": ["campeão: Associação Atlética São Bento (o São Bento da capital, extinto; não é o de Sorocaba)"],
    "1925": ["campeão: Associação Atlética São Bento (o mesmo de 1914 APEA)"],
    "1979": ["a repescagem Marília x Santo André vem na página depois da final (fevereiro de 1980) só com dia e mês "
             "(\"[Dec 5]\"); ficou dezembro de 1980 pela ordem da página, mas pode ser dezembro de 1979 (o ogol não tem esses jogos)"],
    "2002": ["os clubes do Torneio Rio-São Paulo não jogaram o Paulista; o campeão é o Ituano. O Supercampeonato de 2002 "
             "(vencido pelo São Paulo) é outra competição e não entra"],
}

FIM = [
    "## Identidade dos clubes",
    "",
    "- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol (clube antigo sem cidade na ficha",
    "  é dado como paulista).",
    "- Clube do `futebol.db` usa o nome de lá; clube das Séries C e D e da Copa usa o nome daqueles pacotes; os outros seguem o",
    "  nome curto do ogol, com \"-SP\" só quando outro clube de outro estado tem o mesmo nome.",
    "- Clube que o ogol não tem (temporadas sem calendário no ogol) entra pela RSSSF, com código \"rs-<nome>\"; quando o mesmo",
    "  nome aparece em outra temporada com código do ogol, vale esse código.",
    "- **São Paulo da Floresta (1930-1935) e São Paulo FC:** a RSSSF, o ogol (mesmo código) e a Wikipédia tratam como o mesmo",
    "  clube; o pacote segue as fontes até a decisão do agente principal (pedido em `docs/coleta/pedidos.md`).",
    "",
    "## O que não deu para coletar",
    "",
    "- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade, combinado com o Guilherme).",
    "- **Autores dos gols:** só onde a RSSSF traz e a soma fecha com o placar.",
    "- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima.",
    "- **Classificação por rodada:** só nas fases de pontos corridos em que todos os jogos têm a rodada (vem do ogol).",
]
