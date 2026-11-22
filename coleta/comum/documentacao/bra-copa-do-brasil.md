# Copa do Brasil (`bra-copa-do-brasil`) — documentação

Gerado por `python coleta/comum/documentar.py` a partir do pacote `data/coleta/bra-copa-do-brasil/pacote/` e dos módulos de `coleta/bra-copa-do-brasil/`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/bra-copa-do-brasil.md`.

## 1. O que temos

- **Edições:** 37, de 1989 a 2025.
- **Jogos:** 4009; **gols:** 10639; **gols com autor:** 5718 (54%); **cartões:** 0.
- **Clubes:** 399; **artilheiros:** 37 temporadas com artilheiro (62 linhas, com empates).
- **Classificação final:** 37 temporadas; **rodada a rodada:** 0 temporadas.
- **Tabelas publicadas guardadas para conferência:** 122 linhas.
- **No banco (`db/futebol.db`):** sim (37 edições, 4009 jogos).
- **Observação da competição:** Copa nacional disputada desde 1989. A Taça Brasil (1959-1968) já está no banco como parte da Série A.

## 2. Fontes e regras

**Fontes:** RSSSF Brasil (`cbr{ano}.htm`: jogos, fases, datas e autores; tabelas, quando há fase de grupos); ogol (calendário de todas as edições e o código de cada clube; confere placares e completa jogos); Wikipédia (lista de campeões).

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela, fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` ou nos pacotes das Séries C e D usa o mesmo nome (cadastro comum `data/coleta/comum/clubes_ogol.json`).

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF): 61 tabelas fecham com os jogos e 0 divergem (cada divergência é explicada no relatório, na temporada).
- Temporadas com alguma tabela divergente: nenhuma.
- Temporadas sem tabela para conferir: 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2020, 2021, 2022, 2023, 2024.
- Temporadas com menos jogos do que o ogol: 1989 (61 de 62), 1995 (69 de 70), 1996 (70 de 78), 1997 (78 de 86), 1998 (75 de 82), 1999 (116 de 126), 2000 (129 de 136), 2001 (117 de 126), 2002 (117 de 126), 2003 (117 de 126), 2004 (114 de 126), 2005 (117 de 126), 2006 (113 de 126), 2007 (115 de 126), 2008 (110 de 126), 2009 (115 de 126), 2010 (116 de 126), 2011 (111 de 126), 2012 (112 de 126), 2013 (158 de 172), 2014 (159 de 172), 2015 (158 de 172), 2016 (162 de 170).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|
| 1980s | 61 | 100% | 100% | 0% | 0% | 0% | 0% | 5% | 0.0 |
| 1990s | 718 | 100% | 53% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 1164 | 100% | 53% | 0% | 0% | 0% | 0% | 46% | 0.0 |
| 2010s | 1336 | 100% | 100% | 0% | 0% | 0% | 0% | 72% | 0.0 |
| 2020s | 730 | 100% | 100% | 0% | 72% | 72% | 0% | 98% | 0.0 |

**Fonte de cada jogo:** RSSSF Brasil: 3907; ogol: 102.

## 5. Formato ao longo do tempo

**Número de clubes:**

- 1989 a 1994: 32 clubes
- 1995: 36 clubes
- 1996: 40 clubes
- 1997: 44 clubes
- 1998: 41 clubes
- 1999: 64 clubes
- 2000: 69 clubes
- 2001 a 2012: 64 clubes
- 2013 a 2015: 87 clubes
- 2016: 86 clubes
- 2017 a 2020: 91 clubes
- 2021 a 2025: 92 clubes

**Pontos por vitória:**

- 1989 a 1994: 2
- 1995 a 2025: 3

**Nome oficial:**

- 1989 a 2025: Copa do Brasil

**Formato de cada edição** (fases na ordem; grupos; mata-mata):

- 1989 a 2025: mata-mata

**Fases que aparecem** (número de temporadas): Primeira fase (37); Oitavas de final (37); Quartas de final (37); Semifinal (37); Final (37); Segunda fase (30); Terceira fase (14); Fase preliminar (4); Quarta fase (4).

**Observações das edições:**

- nenhuma

## 6. Campeões, acessos, rebaixados e punições

**Títulos:**

- Cruzeiro: 6
- Grêmio: 5
- Flamengo: 5
- Corinthians: 4
- Palmeiras: 4
- Atlético-MG: 2
- Criciúma: 1
- Internacional: 1
- Juventude: 1
- Santo André: 1
- Paulista: 1
- Fluminense: 1
- Sport: 1
- Santos: 1
- Vasco: 1
- Athletico-PR: 1
- São Paulo: 1

**Punições em pontos:**

- nenhuma

## 7. Correções e decisões (com o motivo)

Registradas nos módulos de `coleta/bra-copa-do-brasil/`; cada uma também aparece no relatório, na temporada.

### Clube trocado pelo ogol numa temporada (código -> código) (`importar.CORRIGE_OGOL`)

- **2007 · 3374:** [3373] o Operário de 2007 é o Operário FC Ltda (2002, hoje Várzea Grande EC), campeão mato-grossense de 2006; o ogol põe o Operário-MS (revisão CL-003; pesquisa de 21/11/2026)
- **1995 · 3373:** [36613] em 1995 o Operário de Várzea Grande era o CEOV (revisão CL-007)
- **1996 · 3373:** [36613] em 1996 o Operário de Várzea Grande era o CEOV (revisão CL-007)
- **1998 · 3373:** [ec-operario-mt] EC Operário (1996-2001), que substituiu o CEOV (revisão CL-007)

### Nome da página casado à mão com o clube (`importar.NOME_MANUAL`)

- **1991 · Fluminense(BA):** [3247] Fluminense de Feira; o Grêmio venceu ele e o Auto Esporte pelos mesmos placares (1-0 e 2-0), e o casamento pelo placar confundia os dois
- **1996 · Linhares:** [20122] Linhares EC, o de 1996 (o Linhares FC é dos anos 2000)
- **2003 · CF Amazônia:** [3190] Clube de Futebol Amazônia, o 'CFA' de Porto Velho no ogol
- **2011 · Prudente (SP):** [5229] Grêmio Prudente, nome do Grêmio Barueri em 2010-2011 (hoje 'Barueri' no banco)
- **2013 · Resende (PA):** [12036] erro da RSSSF: é o Resende (RJ), como no ogol (jogos contra o Caxias)
- **2013 · Betim:** [3297] Betim Esporte Clube, ex-Ipatinga (o mesmo clube no ogol)
- **2017 · Sete de Setembro:** [15589] 7 de Setembro de Dourados (MS), como no ogol
- **2018 · Tubarão:** [15723] Atlético Tubarão (SC), como no ogol
- **2023 · Mutum-MT:** [240425] Nova Mutum (MT), como no ogol
- **2007 · Operário(MT):** [3373] Operário FC Ltda (2002), campeão mato-grossense de 2006 (revisão CL-003; pesquisa de 21/11/2026)
- **1996 · Operario-MT:** [36613] CEOV (revisão CL-007)
- **1998 · Operario(MT):** [ec-operario-mt] EC Operário (revisão CL-007)

### Jogos anulados (`importar.JOGOS_ANULADOS`)

- **2007 · Rio Branco(PR) · Villa Nova(MG) · 3 · 0:** erro da página: na 2ª fase o Villa Nova enfrentou o Avaí (revisão CB-007)
- **2019 · Aparecidense/GO · Ponte Preta/SP · 1 · 0:** jogo anulado pelo STJD; vale o 2-0 de 03/04 (revisão CB-007)

### Placares e jogos corrigidos à mão (`importar.PLACAR_MANUAL`)

- **2021 · CRB-AL · Cuiabá-MT · 2021-03-16:** [Sergipe-SE, Cuiabá-MT, 0, 0] o jogo foi Sergipe 0-0 Cuiabá, como no ogol; o CRB jogou a 1ª fase com o Goianésia (revisão CB-007)

### Jogos corrigidos (placar, data, mando) (`importar.CORRECAO_JOGO`)

- **1990 · Goiás · Flamengo · 1990-11-08:** [data=1990-11-07] o ogol dá o dia seguinte (jogo à noite no Brasil); data da Wikipédia pt e en (revisão CB-010)
- **2014 · Atlético-MG · Cruzeiro · 2014-11-13:** [data=2014-11-12] o ogol dá o dia seguinte (jogo à noite no Brasil); data da Wikipédia pt e en (revisão CB-010)
- **2014 · Cruzeiro · Atlético-MG · 2014-11-27:** [data=2014-11-26] o ogol dá o dia seguinte (jogo à noite no Brasil); data da Wikipédia pt e en (revisão CB-010)
- **2015 · Santos · Palmeiras · 2015-11-26:** [data=2015-11-25] o ogol dá o dia seguinte (jogo à noite no Brasil); data da Wikipédia pt e en (revisão CB-010)
- **2015 · Palmeiras · Santos · 2015-12-03:** [data=2015-12-02] o ogol dá o dia seguinte (jogo à noite no Brasil); data da Wikipédia pt e en (revisão CB-010)

### Ocorrências explicadas, por temporada (`explicacoes.EXPLICACOES`)

- **1991:** o Grêmio venceu o Auto Esporte e o Fluminense de Feira pelos mesmos placares; o Fluminense(BA) da página é ligado à mão ao Fluminense de Feira do ogol
- **1994:** vários jogos da página vêm com a data do título da fase (março), quando foram jogados em maio; casados com o ogol pelo par de clubes e pelo placar, e vale a data do ogol
- **2000:** as oitavas vêm com uma letra antes de cada confronto ('E ABC (RN) x Palmeiras (SP)'); a letra sai
- **2001:** a página começa com a seletiva do Espírito Santo, que não é Copa do Brasil; esse trecho fica de fora
- **2003:** a página começa com o jogo seletivo Paraná x Coritiba, que não é Copa do Brasil; fica de fora
- **2015:** nesta página o primeiro clube de cada confronto costuma mandar a volta, mas não sempre (na final, Santos mandou a ida); o leitor inverte o mando, e onde o ogol tem o mesmo jogo com o mando ao contrário vale o ogol (quartas, semifinal e final)
- **2016:** mesmo caso de 2015; na final, a volta vem na página em 30/11 e no ogol em 07/12 (Grêmio 1-1 Atlético-MG): vale o ogol

### Clube do ogol casado à mão com o nome do banco (`clubes_cb.MANUAL_DB`)

- **3333:** [J.Malucelli] o ogol escreve 'JMalucelli'; é o J. Malucelli do banco (Série A 2000)
- **24836:** [Novorizontino] Grêmio Novorizontino (2010-); o banco separou o GE Novorizontino (1973-1999) em 20/11/2026

### Nome de exibição de clube novo, dado à mão (`clubes_cb.MANUAL_NOVO`)

- **ec-operario-mt:** [EC Operário-MT] Esporte Clube Operário (1996-2001), de Várzea Grande; sem ficha no ogol (revisão CL-007)
- **68358:** [Corinthians Prudente] EC Corinthians de Presidente Prudente (1996): não é o Corinthians paulistano do banco
- **45210:** [Maringá] Maringá FC fundado em 2010 (Copa do Brasil 2025): não é o GE Maringá do banco
- **241210:** [Maringá FC 1995] Maringá FC fundado em 1995 (Copa do Brasil 1997): outro clube, nome como no ogol
- **60858:** [GE Novorizontino] Grêmio Esportivo Novorizontino (1973-1999, campeão de 1994): outro clube; o 'Novorizontino' do banco fica com o Grêmio Novorizontino, fundado em 2010 (decisão do Guilherme, 20/11/2026)
- **20122:** [Linhares EC] dois clubes de Linhares-ES: o EC (anos 1990) e o FC (anos 2000); o sufixo já distingue
- **9783:** [Linhares FC] dois clubes de Linhares-ES: o EC (anos 1990) e o FC (anos 2000); o sufixo já distingue

### Páginas da RSSSF corrigidas na leitura (`rsssf.CORRECOES`, registradas em `coleta/bra-copa-do-brasil/rsssf_*.py`)

- **cbr1989.htm:** título 'Semifinals' colado no primeiro confronto da fase; espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr1990.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr1991.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr1992.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr1993.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr1994.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr1995.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr1996.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr1997.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr1998.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr1999.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2000.htm:** oitavas com uma letra na frente de cada jogo ('E ABC (RN)  3-3  Palmeiras (SP)'); espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2001.htm:** seletiva do Espírito Santo no começo da página (não é Copa do Brasil); espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2002.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2003.htm:** jogo seletivo Paraná x Coritiba no começo da página (não é Copa do Brasil); espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2004.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2005.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2006.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2007.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2008.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2009.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2010.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2011.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2012.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2013.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2014.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2015.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta; nesta edição o primeiro da linha manda a volta (ogol e autores confirmam)
- **cbr2016.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta; nesta edição o primeiro da linha manda a volta (ogol e autores confirmam)
- **cbr2017.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2018.htm:** espaço antes do '(UF)' tirado; volta não jogada ('A  1-4 n/p  B'): o 'n/p' sai, fica a ida; confrontos numerados numa linha só, com as datas da ida e da volta
- **cbr2019.htm:** espaço antes do '(UF)' tirado
- **cbr2020.htm:** espaço antes do '(UF)' tirado; jogos com a data entre colchetes e o estádio depois do visitante
- **cbr2021.htm:** espaço antes do '(UF)' tirado; jogos com a data entre colchetes e o estádio depois do visitante
- **cbr2022.htm:** espaço antes do '(UF)' tirado; jogos com a data entre colchetes e o estádio depois do visitante
- **cbr2023.htm:** espaço antes do '(UF)' tirado; jogos com a data entre colchetes e o estádio depois do visitante
- **cbr2024.htm:** espaço antes do '(UF)' tirado; data em linha própria e autores separados por ';' (mandante; visitante)
- **cbr2025.htm:** espaço antes do '(UF)' tirado

## 8. O que não deu para coletar

- **Cartões:** a RSSSF não traz; o ogol tem na página de cada jogo (baixa prioridade, combinado com o Guilherme).
- **Autores dos gols:** só onde a RSSSF traz e a soma fecha com o placar.
- **Classificação final:** calculada (fase alcançada, depois pontos, vitórias, saldo e gols pró), com campeão e vice em cima.

## 9. Pendências e próximos passos

- Achados da revisão CB-001 a CB-015: tratados (docs/coleta/pedidos.md, partes 1 e 4). A revisão ainda não reconferiu.
- Jogo preliminar de 1999 (Santa Cruz 1-0 Náutico, CB-007): entrou sem data; nenhuma fonte achada dá o dia.
- Autores dos gols antes de 2013 e cartões: jogo a jogo, pela ficha do ogol (prioridade baixa).

## 10. Arquivos e comandos

| Arquivo | O que faz |
|---|---|
| `coleta/bra-copa-do-brasil/baixar_espn_wiki.py` | Baixa as fontes complementares da Copa do Brasil: - ESPN: não usada nesta coleta. - Wikipédia em português e em inglês, uma página por edição -> data/coleta/bra-copa-do-brasil/wikipedia/{pt,en}_{ano}.txt. |
| `coleta/bra-copa-do-brasil/baixar_ogol.py` | Baixa o calendário de cada edição da Copa do Brasil no ogol para data/coleta/bra-copa-do-brasil/ogol/copa_brasil_{ano}.json. |
| `coleta/bra-copa-do-brasil/baixar_ogol_clubes.py` | Baixa a ficha no ogol de cada clube que aparece nos calendários da Copa do Brasil (nome completo, cidade, UF) e grava data/coleta/bra-copa-do-brasil/ogol/clubes.json. As páginas ficam em data/cache/ogol_equipes/. |
| `coleta/bra-copa-do-brasil/baixar_rsssf.py` | Baixa as páginas da Copa do Brasil da RSSSF Brasil para data/coleta/bra-copa-do-brasil/rsssfbrasil/. |
| `coleta/bra-copa-do-brasil/clubes_cb.py` | Identidade dos clubes da Copa do Brasil (mesmo método da Série C; clube já nomeado na Série C usa o mesmo nome). |
| `coleta/bra-copa-do-brasil/edicoes.py` | Edições da Copa do Brasil: anos e nomes oficiais. |
| `coleta/bra-copa-do-brasil/explicacoes.py` | Textos do relatório da Copa do Brasil que não saem do código: introdução, explicações de cada edição e o fim. |
| `coleta/bra-copa-do-brasil/importar.py` | Junta as fontes da Copa do Brasil (mesmo método da Série C) e grava o pacote em data/coleta/bra-copa-do-brasil/pacote/ e o relatório em docs/coleta/bra-copa-do-brasil.md. |
| `coleta/bra-copa-do-brasil/pacote.py` | Grava o pacote da Copa do Brasil (data/coleta/bra-copa-do-brasil/pacote/) e o relatório (docs/coleta/bra-copa-do-brasil.md), no formato de docs/agente-coleta-COMECE-AQUI.md, seção 4. Chamado por importar.py. |
| `coleta/bra-copa-do-brasil/rsssf_cb.py` | Leitura das páginas da Copa do Brasil da RSSSF Brasil (data/coleta/bra-copa-do-brasil/rsssfbrasil/cbr{ano}.htm). |

- Fontes baixadas: `data/coleta/bra-copa-do-brasil/` (ogol, rsssfbrasil, wikipedia). Pacote: `data/coleta/bra-copa-do-brasil/pacote/`. Relatório: `docs/coleta/bra-copa-do-brasil.md`.
- Código comum: `coleta/comum/` (`rsssf.py` leitor das páginas da RSSSF Brasil, `ogol.py` calendários e fichas, `gols.py` autores dos gols, `registro.py` cadastro comum de nomes `data/coleta/comum/clubes_ogol.json`, `baixar.py` download educado).
- Refazer do zero (da raiz do `clube_analitico`, logs no scratchpad):

  - `python coleta/bra-copa-do-brasil/baixar_espn_wiki.py` (ver o docstring)
  - `python coleta/bra-copa-do-brasil/baixar_ogol.py` (ver o docstring)
  - `python coleta/bra-copa-do-brasil/baixar_ogol_clubes.py` (ver o docstring)
  - `python coleta/bra-copa-do-brasil/baixar_rsssf.py` (ver o docstring)
  - `python coleta/bra-copa-do-brasil/importar.py` (grava o pacote e o relatório; `importar.py <ano>` só mostra, sem gravar)
  - `python coleta/comum/testar_carga.py bra-copa-do-brasil <pasta temporária>` (deve terminar com `-> OK`)
  - `python coleta/comum/documentar.py`

