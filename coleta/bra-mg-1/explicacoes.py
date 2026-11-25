"""Textos do relatório do Campeonato Mineiro (1ª divisão) que não saem do código: introdução, explicações de cada
temporada e o fim."""

INTRO = [
    "Gerado por `python coleta/bra-mg-1/importar.py`. Pacote em `data/coleta/bra-mg-1/pacote/`. Mesmo código do Carioca",
    "(`docs/coleta/bra-rj-1.md`), com as fontes de Minas Gerais.",
    "",
    "**Temporadas:** 1915 a 2026. Até os anos 1940 é o campeonato dos clubes de Belo Horizonte e arredores; o interior entra",
    "aos poucos (1958-1959 com os torneios de classificação; de 1970 em diante, o campeonato estadual). Em 1932 houve duas",
    "ligas e a FMF reconhece os dois títulos: cada torneio é uma edição (\"1932 LMDT\" e \"1932 AMEG\"). 1956 teve título",
    "dividido (Atlético e Cruzeiro). 1925 é a edição que a liga considerou inexistente na época e a FMF homologou em 2012",
    "(campeão o América). Em 2002 Atlético, Cruzeiro e América (Copa Sul-Minas) não jogaram; o campeão foi a Caldense.",
    "",
    "**Fontes:** RSSSF Brasil (`tablesfq/mg{ano}.htm`: jogos, fases, datas, autores e tabelas; `mg1926l.htm`,",
    "`mg1932l.htm` e `mg1932a.htm` com a letra da liga); ogol (calendário de cada edição e o código de cada clube; confere",
    "placares, traz a rodada e completa os jogos que a página não traz); Wikipédia em português (artigo do Campeonato",
    "Mineiro: tabela de resultados ano a ano, segunda fonte do campeão e do vice). Artilheiros pela lista da RSSSF",
    "(`mgtops.htm`).",
    "",
    "**Fases:** os torneios de classificação (1921, 1958-1959, 1970-1973) entram como \"Fase classificatória\"; os",
    "desempates como \"<fase> - Desempate\"; os turnos com semifinal e final próprias (1975-1987) como \"1º Turno\",",
    "\"1º Turno - Final\" etc. Jogos anulados ou cancelados (\"[annulled]\", \"[cancelled]\") ficam fora. A repescagem contra o",
    "campeão da 2ª divisão fica só na observação da edição (decisão D-04). Os Torneios Paralelos de 1976 (consolação) ficam fora.",
    "",
    "**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela,",
    "fica a da RSSSF. W.O. conta como vitória sem gols (decisão D-15). Autores dos gols só entram quando a soma bate com o",
    "placar. Clube que já está no `futebol.db` ou nos outros pacotes usa o mesmo nome (cadastro comum",
    "`data/coleta/comum/clubes_ogol.json`).",
]

# temporada -> explicações conferidas à mão (contexto das ocorrências listadas logo abaixo de cada temporada)
EXPLICACOES: dict[str, list[str]] = {
    "1956": ["título dividido entre Atlético e Cruzeiro: o pacote tem o Atlético em campeao, o Cruzeiro em co_campeao e o vice "
             "vazio (D-07, como o Carioca 1907 e o Paulista 1973)"],
    "1976": ["Torneios Paralelos I, II e III: consolação para os 11 clubes que não foram à Taça Governador do Estado; ficam fora "
             "(rsssf_mg1.ANOS_A_PARTE), como os torneios à parte do Carioca"],
    **{str(a): ["Troféu Inconfidência (do 5º ao 8º da 1ª fase): torneio à parte, fica fora; o calendário do ogol traz os "
                "jogos dele junto com os do campeonato (rsssf_mg1.ANOS_A_PARTE)"] for a in range(2020, 2027)},
}

FIM = [
    "## Identidade dos clubes",
    "",
    "- Cada clube é o código dele no ogol; nome, cidade e UF vêm da ficha do clube no ogol.",
    "- Clube que o ogol não tem entra pela RSSSF, com código \"rs-<nome>\". Nunca com o nome exato de outro clube (regra 6b).",
    "- Mesmo clube com outro nome fica com o nome de hoje (Palestra Itália, depois Palestra Mineiro, é o Cruzeiro).",
    "",
    "## O que não deu para coletar",
    "",
    "- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade).",
    "- **Autores dos gols:** só entram quando a soma bate com o placar.",
    "- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com o campeão em cima;",
    "  quando a RSSSF publica a classificação geral e ela fecha com os jogos, vale a dela.",
]
