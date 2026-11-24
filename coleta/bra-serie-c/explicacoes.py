"""Textos do relatório da Série C que não saem do código: introdução e explicações de cada edição
(divergências que ficaram, depois de conferidas à mão)."""

INTRO = [
    "Gerado por `python coleta/bra-serie-c/importar.py`. Pacote em `data/coleta/bra-serie-c/pacote/`.",
    "",
    "**Edições:** 36 oficiais, de 1981 a 2026 (1981, 1988, 1990, 1992, 1994-1999 e 2001-2026), conferidas na RSSSF Brasil",
    "(lista de campeões da 3ª divisão) e na Wikipédia em português (artigo da Série C). As duas trazem os mesmos anos e os mesmos",
    "campeões. Ficam de fora 1987 (módulos Azul e Branco da Copa União: a CBF disse que nenhum módulo seria a 3ª divisão) e 2000",
    "(Módulo Verde e Branco da Copa João Havelange, equivalente à 3ª divisão, mas sem título oficial). Nome oficial: Taça de Bronze",
    "em 1981; Campeonato Brasileiro Série C nas outras.",
    "",
    "**Fontes:** RSSSF Brasil (`br{ano}l3.htm`, base de jogos, fases, grupos, datas e autores; as tabelas publicadas são a conferência);",
    "ogol (calendário de todas as edições e o código de cada clube, que dá a identidade entre anos e mudanças de nome; completa os",
    "jogos que faltam na RSSSF e é a base de 2019); ESPN (liga `bra.3`, 2017 em diante: hora e estádio; a ESPN não traz gols,",
    "cartões nem público da Série C); Wikipédia (punições de pontos e lista de campeões).",
    "",
    "**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,",
    "fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` usa o nome de lá.",
    "",
    "**Classificação final (revisão SC-002, SC-003):** campeão e vice em cima; depois a fase alcançada; na mesma fase, a posição",
    "no grupo dela (ou no quadrangular/octogonal final) e a campanha toda (pontos, vitórias, saldo, gols pró). A ordem geral da RSSSF,",
    "quando existe, só desempata dentro da mesma fase. As últimas fases de mata-mata levam o nome pelo número de confrontos",
    "(1 = Final, 2 = Semifinal, 4 = Quartas de final).",
    "",
    "**Acesso e rebaixamento (revisão SC-004, SC-005):** acesso = promovidos da Wikipédia e quem jogou a Série B do ano seguinte",
    "(em 1981 só o Olaria; em 1988, 1990 e 1992 ninguém, porque a Série B seguinte foi por convite; em 1999 Fluminense e São",
    "Raimundo). Rebaixado = rebaixados da RSSSF e da Wikipédia e, desde 2009, quem jogou a Série D do ano seguinte (mais",
    "Guaratinguetá em 2016 e Luverdense em 2019, que não jogaram a D).",
]

# ano -> explicações conferidas à mão (contexto das ocorrências listadas logo abaixo de cada ano)
EXPLICACOES: dict[int, list[str]] = {
    2026: ["a RSSSF ainda não tem a página de 2026: os jogos, as fases e os grupos vêm do ogol, e o campeão, os acessos e os "
           "rebaixados da Wikipédia (revisão SC-001). Sem autores de gols"],
    1981: ["o ogol liga o Matsubara (Cambará-PR) ao J. Malucelli, fundado em 1994; corrigido no código (CORRIGE_OGOL): fica a SE Matsubara, como na RSSSF"],
    1988: ["a final (Esportivo-MG x União São João, 1-1 e 2-2) foi decidida pela campanha (número de vitórias): campeão pela lista oficial",
           "vitória valia 3 pontos e o empate ia para os pênaltis: 2 para quem vencia, 1 para quem perdia (revisão SC-007). "
           "No grupo 18 da 2ª fase o ogol põe a Desportiva Ferroviária no lugar da Ferroviária-SP; corrigido (revisão SC-008)"],
    1994: ["Caldas x Vila Nova-GO (2ª fase, 23/10): fontes divididas como em 1992; fica o placar do pacote (D-13, SC-016)",
           "nas oitavas, o 'Vitória' sem estado da página é o Vitória-ES (o Vitória-PE caiu para o ABC na mesma fase); corrigido no texto da página",
           "o ogol põe o Vitória-ES contra o ABC no jogo de volta das oitavas; a RSSSF e a classificação final mostram o Vitória-PE (fica a RSSSF)"],
    1995: ["página com 108 clubes e a 2ª e a 3ª fases em confrontos colados uns nos outros; o leitor separa cada jogo (rsssf_c.py, _1995)",
           "erros de digitação da página corrigidos no código: 'Coríntians 3x1 3x1 Santa Cruz-PB' (placar repetido) e 'Ypranga'"],
    1996: ["a página traz 'GAS 2-3 GAS' no grupo 2; é GAS 2-3 Baré (ogol e tabela do grupo); corrigido no texto da página"],
    1999: ["a página traz, antes da Série C, as seletivas estaduais (RS, PR, MG, PB, PE, PI); esse trecho fica de fora",
           "226 jogos, 2 a mais que a Wikipédia e o Bola n@ Área (224): o pacote conta os 2 jogos-desempate, que existiram "
           "(revisão SC-021)"],
    2001: ["1.124 gols, a soma dos 412 jogos (igual à soma dos jogos do Bola n@ Área); o 1.127 do resumo do Bola, copiado pela "
           "Wikipédia, não fecha com os jogos (revisão SC-021)"],
    2002: ["595 gols, 6 a mais que o Bola n@ Área (589): a diferença está nos placares em que a RSSSF e o Bola divergem, que "
           "ficam com a RSSSF até uma 4ª fonte (revisão QC-012 e SC-021)",
           "dúvida em aberto: o ogol liga o 'SER São Gabriel' da RSSSF ao 'EC São Gabriel', que a ficha do ogol diz fundado em 2013; "
           "pode ser erro do ogol. Fica como está (decisão do agente principal, 20/11/2026)"],
    2005: ["a página traz o público no fim da linha dos jogos das fases finais ('att: 18.865'); o leitor lê o público (12 jogos)"],
    2011: ["o Rio Branco-AC foi eliminado pelo STJD depois de recorrer à Justiça comum; a RSSSF mantém 3 jogos dele na 2ª fase, que o ogol não tem (ficam, com a fonte RSSSF)",
           "sem os 3 jogos do Rio Branco-AC na 2ª fase (eliminado pelo STJD; o grupo E recomeçou com o Luverdense), o 3º é o "
           "Ipatinga, como na Wikipédia (revisão SC-003, SC-013). A edição fica com 106 jogos; o infobox da Wikipédia diz 105 "
           "(diferença não achada, revisão SC-021)"],
    1992: ["Nacional-AM x Tuna Luso (2ª fase, 27/05) e Rio Branco-MG x Marília: a RSSSF e o ogol dão o placar do pacote; o Bola n@ "
           "Área e a Wikipédia (que cita o Bola), outro; fica o do pacote até um jornal da época (decisão D-13, revisão SC-016)",
           "5 placares da página trocados pelos do ogol e da Wikipédia (revisão SC-014); as tabelas publicadas pela RSSSF "
           "seguem os placares antigos da página e por isso não fecham nos grupos 1 e 6 e no grupo A da 2ª fase. Com os placares "
           "novos o 3º é o Nacional-AM, como na Wikipédia. Dois jogos do grupo B vêm na página depois do título da final e voltam "
           "para a 2ª fase"],
    2013: ["o Rio Branco-AC entrou na competição por decisão judicial; a página da RSSSF não traz os 20 jogos dele no grupo A, que entram pelo ogol (a tabela do grupo fecha)"],
    2015: ["a página da RSSSF trocou dia e mês em 37 datas ('06/jan/15' em vez de 02/06); vale a data do ogol"],
    2017: ["Mogi Mirim x Ypiranga-RS (grupo B) foi W.O. ('0-WO' na página): entra 0-3, como conta a tabela do grupo"],
    2019: ["a página da RSSSF parou na 1ª rodada (40 jogos): a base dos jogos é o ogol (194), sem autores de gols"],
    2024: ["a página da RSSSF traz os autores dos gols sem dizer de que time é cada um ('18' (25-Pedro Henrique)'): ficam só no texto (gols_texto)"],
}

FIM = [
    "## Identidade dos clubes",
    "",
    "- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol (`data/coleta/bra-serie-c/ogol/clubes.json`).",
    "- 168 clubes já estavam no `futebol.db` e usam o nome de lá; os outros seguem o nome curto do ogol, com \"-UF\" só quando outro",
    "  clube tem o mesmo nome. Clubes que mudaram de nome aparecem com o nome atual (Intercap = Paraíso;",
    "  Ituiutaba = Boa Esporte), menos o Santo Amaro-PE, vice de 1981, que só jogou com esse nome e fica com ele, e não com o",
    "  posterior \"Manchete\" (D-03); os nomes de cada fonte e ano estão em `clubes.csv` (`nomes_fonte`).",
    "- Decisões à mão (em `clubes_c.py` e `importar.py`, com o motivo): EC Corinthians de Presidente Prudente não é o Corinthians",
    "  do banco (vira \"Corinthians Prudente\"); o Maringá FC de 2010 e o de 1995 não são o GE Maringá do banco; \"JMalucelli\" é o",
    "  J.Malucelli do banco.",
    "- Novorizontino separado em dois (decisão do Guilherme, 20/11/2026): \"GE Novorizontino\" (1973-1999, campeão da Série C de",
    "  1994; Série C 1988 e 1994) e \"Novorizontino\" (Grêmio Novorizontino, fundado em 2010; Série C 2021). O banco ainda junta os",
    "  dois; o pedido para separar está em `docs/coleta/pedidos.md`.",
    "",
    "## O que não deu para coletar",
    "",
    "- **Cartões:** nenhuma das fontes lidas traz cartões da Série C (a RSSSF não traz; a ESPN não tem lances da Série C).",
    "  O ogol tem cartões e autores dos gols na página de cada jogo, mas seriam uns 8 mil pedidos (cerca de 3 horas);",
    "  fica como próximo passo, se aprovado.",
    "- **Autores dos gols:** só onde a RSSSF traz e a soma fecha com o placar. Faltam (quase) todos em 1994-2001, 2008, 2011,",
    "  2012, 2019 e 2024.",
    "- **Público:** a ESPN traz 0 na Série C e a RSSSF só em poucas fichas de final.",
    "- **Hora e estádio:** RSSSF (2013-2015, 2020, 2023, 2024), ogol (hora) e ESPN (2017 em diante).",
    "- **Classificação final:** a ordem oficial existe só quando a RSSSF publica a classificação geral (7 edições); nas outras ela é",
    "  calculada (fase alcançada, pontos, vitórias, saldo, gols pró), com campeão e vice em cima.",
    "- **Acesso:** marcado quando o clube jogou a Série B no ano seguinte (pelo `futebol.db`) ou está nos \"promovidos\" do infobox",
    "  da Wikipédia. **Rebaixamento:** marcas \"Relegated\" das tabelas da RSSSF e \"rebaixados\" do infobox.",
]
