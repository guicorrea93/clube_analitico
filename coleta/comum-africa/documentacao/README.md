# Coleta África — documentação

Gerado por `python coleta/comum-africa/documentar.py`. Uma ficha por competição, com tudo o que o pacote tem, como as edições foram definidas, fontes e regras, a conferência, a cobertura de cada campo década a década, o formato ao longo do tempo, campeões e vices, ajustes de pontos, todas as correções e decisões com o motivo, o que não deu para coletar e as pendências.

Regras de trabalho, ordem das pendências e como fazer uma competição nova: `coleta/comum-africa/COMECE-AQUI.md`. Recados ao agente do banco e respostas dele: `docs/coleta/pedidos-africa.md`. Achados da revisão: `docs/revisao/achados.csv` (`quem_corrige` = `coleta-africa`).

| Competição | Edições | Sem jogos | Jogos | Gols c/ autor | Cartões | Clubes | Edições ok / div. | No banco | Commit | Achados abertos | Ficha |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Campeonato Egípcio | 73 (1948/49–2025/26) | 13 | 11574 | 3068 | 0 | 74 | 42 / 12 | sim | 06635c89 | 0 | [egy-1](egy-1.md) |
| Campeonato Marroquino | 110 (1915/16–2025/26) | 41 | 11736 | 18 | 0 | 100 | 35 / 20 | sim | 786998de | 0 | [mar-1](mar-1.md) |
| Campeonato Tunisiano | 109 (1907–2025/26) | 56 | 8092 | 771 | 0 | 74 | 34 / 10 | sim | 786998de | 0 | [tun-1](tun-1.md) |
| Campeonato Argelino | 64 (1962/63–2025/26) | 0 | 15210 | 3829 | 0 | 81 | 22 / 39 | sim | b09bbaa5 | 0 | [alg-1](alg-1.md) |
| Campeonato Sul-Africano | 55 (1971–2025/26) | 22 | 8108 | 4721 | 0 | 89 | 28 / 1 | sim | b7555945 | 0 | [rsa-1](rsa-1.md) |
| Campeonato Nigeriano | 55 (1972–2025/26) | 26 | 8906 | 73 | 0 | 82 | 13 / 8 | sim | bc5287a6 | 0 | [nga-1](nga-1.md) |
| Campeonato Ganês | 65 (1958–2025/26) | 39 | 6069 | 294 | 0 | 137 | 20 / 4 | sim | cd02564c | 0 | [gha-1](gha-1.md) |
| Campeonato Camaronês | 66 (1961–2026) | 37 | 6804 | 1138 | 0 | 85 | 22 / 3 | sim | e7f2bfa8 | 0 | [cmr-1](cmr-1.md) |
| Campeonato Tanzaniano | 62 (1965–2025/26) | 32 | 5929 | 1299 | 0 | 82 | 21 / 1 | não | — | 0 | [tan-1](tan-1.md) |

## Pendências de todas as competições

- **egy-1:** 1948/49 a 1963/64 sem jogos (nenhuma fonte pública tem): só a tabela final, e a final ou o desempate do título quando a página da RSSSF traz (1948/49, 1957/58, 1962/63, 1963/64, 1975/76). As listas "Results Ahly" (só os jogos do Al-Ahly, sem data nem mando) ficaram de fora. Fonte que resolveria: o site do Dr. Tarek Said (drtareksaid.net, arquivado) ou jornais egípcios da época.
- **egy-1:** 1954/55, 1971/72 e 1973/74 (não terminadas): nenhuma fonte tem jogos nem tabela; entram só com a observação.
- **egy-1:** Autores dos gols só onde a RSSSF traz (1998/99 a 2006/07, nem sempre a temporada inteira); de 2007/08 em diante a página não tem autores e a ESPN não cobre a liga. Fonte que resolveria: o ogol jogo a jogo (página de cada partida).
- **egy-1:** Divergências entre a tabela da RSSSF e os jogos do ogol sem terceira fonte (1979/80, 1980/81) e as que a Wikipédia confirma a tabela (1977/78 Zamalek, 1991/92 Damanhour 0-0 Zamalek = 1-2?, 2010/11): o jogo provável está no relatório; nenhum placar foi mudado.
- **egy-1:** Identidade a conferir: o "Sohag Railways" de 2000/01 e o "Sohag" de 2001/02 entraram como um clube só; o Al-Shourta de 1975/76 entrou como Ittihad El-Shorta; o "Suez Club" do ogol é o Ittihad Suez só em 1965/66.
- **mar-1:** Era colonial (1915/16 a 1954/55): 9 anos sem página da RSSSF (só o campeão); nos outros, jogos incompletos (ligas regionais com os resultados conhecidos e o mata-mata nacional) ou só a classificação (1949/50 a 1953/54, a maioria dos clubes só com os pontos). Fonte que resolveria: os jornais da época (Le Petit Marocain, La Vigie Marocaine) na Gallica (BnF).
- **mar-1:** 1968/69 a 1994/95 (fora 1980/81, 1989/90 e 1990/91): só a tabela final; o ogol só tem os jogos de 2004/05 em diante. 1970/71, 1973/74 e 1981/82 sem página da RSSSF: só o campeão e o vice.
- **mar-1:** Tabelas de confrontos (1956/57 a 1967/68, 1980/81, 1989/90): os jogos não têm data nem rodada, e vários resultados não batem com a tabela final da página (vitórias e empates trocados com os mesmos gols); sem terceira fonte.
- **mar-1:** Autores dos gols quase nenhum (a RSSSF do Marrocos não traz) e nenhum cartão. Fonte que resolveria: o ogol jogo a jogo (2004/05 em diante).
- **mar-1:** Identidade a conferir: Racing Casablanca (colonial) = Racing AC = ADM Casablanca (como a RSSSF conta); AS Salé = SA Salé = Sporting Salé; JS Massira = Forces Auxiliaires (a página de 1994/95 diz que o clube mudou para El Ayoun); "ASM" (1957/58) sem nome completo; "US Casablanca" = USA Casablanca.
- **mar-1:** 1946/47: campeão USA Casablanca (página da temporada e Wikipédia); a lista de campeões da RSSSF põe a US Marocaine (erro da lista; avisar a RSSSF?).
- **tun-1:** Era colonial (1907 a 1954/55): só 9 anos têm jogos na RSSSF, e só a final ou o mata-mata (1949/50: os resultados conhecidos); os outros, só o campeão. 1951/52 (abandonado) tem só a tabela do abandono. Fonte que resolveria: os jornais da época (La Dépêche tunisienne, Le Petit Matin) na Gallica (BnF).
- **tun-1:** 1955/56 a 1995/96: só a tabela final (lista de tabelas finais da RSSSF), fora os anos da tabela de confrontos (1968/69, 1970/71, 1977/78, 1980/81, 1982/83 e 1987/88 a 1995/96), que não têm data nem rodada. O ogol só tem jogos de 2005/06 em diante.
- **tun-1:** Tabelas de confrontos que não fecham com a tabela final da página: um par de jogos em 1968/69, 1977/78, 1980/81, 1982/83, 1987/88 a 1990/91 e 1993/94; 1994/95 em 13 dos 14 clubes. Sem terceira fonte; nenhum placar mudado (jogo provável no relatório).
- **tun-1:** Autores dos gols quase só em 2004/05 e 2010/11 (a RSSSF da Tunísia quase não traz) e nenhum cartão. Fonte que resolveria: o ogol jogo a jogo (2005/06 em diante).
- **tun-1:** Identidade a conferir: Railway Sports de Sfax (colonial) = Sfax Railways Sports; US Ferryville = USM Bourguiba; Olympique Tunis = US Musulmane Olympique; "ES" de 1949/50 lido como Espérance de Tunis.
- **tun-1:** 1909/10: a Wikipédia dá um título ao Racing Club de Tunis; a RSSSF diz que não houve campeonato (ficou de fora).
- **alg-1:** 1964/65 a 1998/99: a lista de jogos da RSSSF não fecha com a tabela da mesma página em vários clubes por ano (placar ou resultado trocado, jogo repetido ou faltando); o ogol (desde 1985/86) repete os placares da RSSSF e a Wikipédia quase sempre confirma a tabela. Nenhum placar mudado; jogo provável no relatório. Fonte que resolveria: jornais argelinos da época (El Moudjahid) ou o arquivo da federação.
- **alg-1:** 1974/75 e 1975/76: uma rodada inteira copiada na página (os jogos verdadeiros das rodadas 4 e 18 faltam); 1972/73: rodada 10 repetida (cópia descartada).
- **alg-1:** Mando provavelmente trocado: o mesmo mandante x visitante duas vezes na temporada, com placares diferentes (1964/65, 1966/67, 1973/74, 1976/77, 1979/80, 1980/81, 1983/84, 1986/87, 1988/89...): ficou como na página.
- **alg-1:** 1962/63 e 1963/64: ligas regionais incompletas (1962/63 sem a 1ª fase; 1963/64 só os resultados conhecidos, grupo Leste de Constantine sem números).
- **alg-1:** 2009/10: CA Bordj Bou Arréridj x MC Alger com "derrota para os dois" (o formato do pacote não representa; jogo sem placar).
- **alg-1:** Identidade a conferir: DNC Alger = OC Alger = CS DNC Alger = JH Djazaïr (nome de exibição "DNC Alger"); WKF Collo = Entente Collo; o USM Annaba até 1979 é o Hamra Annaba; "US Constantine" de 1996/97 = US Chaouia; MB Rouissat = Olympique Rouissat (2025/26).
- **rsa-1:** 1971 a 1995: só a tabela final (a RSSSF não tem os jogos), fora 1987, 1992 e 1993 (parte dos jogos); 1972, 1973, 1975 e 1977: só o campeão (a página do ano é da NFL). 1996/97: parte dos jogos. O ogol só tem jogos de 2005/06 em diante. Fonte que resolveria: jornais sul-africanos (The World, Sowetan, Rand Daily Mail) ou o arquivo da PSL.
- **rsa-1:** Rebaixamento pelos desempates de acesso (2004/05 a 2025/26) marcado à mão (o 15º que não está na 1ª divisão do ano seguinte); clubes que saíram por venda da vaga, fusão ou redução da liga ficam sem marca.
- **rsa-1:** Autores dos gols só onde a RSSSF traz; artilheiros de poucas temporadas (contagem dos gols com autor). Fonte que resolveria: o ogol jogo a jogo (2005/06 em diante).
- **rsa-1:** Identidade a conferir: Cape Town Spurs = Ajax Cape Town (fusão de 1999 e volta ao nome em 2020); SuperSport United = Pretoria City = Albany City; Free State Stars = Qwa Qwa Stars = Score Stars; Highlands Park (1959) = Welkom Eagles (1993); Durban Bush Bucks (até 1987) x Bush Bucks de Umtata (desde 1988); Mpumalanga Black Aces = Witbank Aces = Total Aces.
- **nga-1:** 1972 a 1997: só a tabela final (1972, 1989, 1991 a 1997) ou só o campeão (1973 a 1988 e 1990); faltam as páginas de 1980 a 1982. 1998 a 2003, 2007/08 e 2019/20: só parte dos jogos. Fonte que resolveria: jornais nigerianos (Daily Times, The Guardian, Complete Sports) ou o arquivo da NPFL.
- **nga-1:** 2009/10 a 2011/12: os jogos do ogol não fecham com a tabela da RSSSF em vários clubes (placar de campo de jogos decididos de outro jeito?); nenhum placar mudado.
- **nga-1:** Rebaixamento marcado só onde a página diz (tabela ou nota); nos anos 1970 e 1980, sem informação.
- **nga-1:** Autores dos gols quase nenhum; artilheiros, nenhum. Fonte que resolveria: o ogol jogo a jogo (2008/09 em diante).
- **nga-1:** Identidade a conferir: Heartland = Iwuanyanwu Nationale; Dolphin = Eagle Cement; Ifeanyi Ubah = Gabros International; ABS = Bukola Babes; NITEL Vasco = P&T Vasco da Gama; o "Akwa Star..." do ogol de 2011/12 = Akwa United.
- **gha-1:** 1958 a 1996/97: só a tabela final (lista de tabelas finais até 1987; página do ano de 1989/90 a 1996/97); 1988/89 só o campeão ("Final table missing"); 1989/90 só posição, jogos e pontos. 1997/98 e 2006/07: parte dos jogos; 2011/12: só a tabela. O ogol só tem jogos de 2008/09 a 2010/11 e de 2015 em diante. Fonte que resolveria: jornais ganeses (Daily Graphic) ou o arquivo da GFA.
- **gha-1:** 2010/11: os jogos do ogol não fecham com a tabela da RSSSF em sete clubes; nenhum placar mudado.
- **gha-1:** Rebaixamento marcado onde a tabela ou a nota diz; em vários anos dos 1960 e 1970 a lista não diz.
- **gha-1:** Autores dos gols quase nenhum; artilheiros e cartões, nenhum.
- **gha-1:** Identidade a conferir: Ashanti Gold = Goldfields; Ebusua Dwarfs = Mysterious Dwarfs; Swedru All Blacks = Gamba All Blacks; Wa All Stars = All Stars (2007-2011); Holy Stars de Techiman (1986) x Basake Holy Stars (2024/25).
- **cmr-1:** 1961 a 1998: só o campeão (1961 a 1977/78, 1984/85, 1986/87 e 1992), só os primeiros colocados ou só posição, jogos e pontos (1978/79 a 1985/86, 1993 e 1996) ou só a tabela final (os outros anos); 1987/88, 1999 e 2000: parte dos jogos. Fonte que resolveria: jornais camaroneses (Cameroon Tribune) ou o arquivo da FECAFOOT.
- **cmr-1:** 2010/11: a RSSSF só traz a tabela; os jogos vêm do ogol, que junta o Union e o Caïman Douala num clube só (os jogos dos dois ficam de fora).
- **cmr-1:** 2001: a classificação é a tabela oficial da FECAFOOT, que não fecha com os jogos (a página traz também a tabela pelos resultados conhecidos).
- **cmr-1:** Autores dos gols só em 2004 e 2005; artilheiros só desses dois anos; cartões, nenhum. Fonte que resolveria: o ogol jogo a jogo (2005 em diante, fora 2013 a 2016).
- **cmr-1:** Identidade a conferir: os dois Aigle Royal ("Aigle" sozinho até 2004 = o do Moungo, de Nkongsamba; de 2005 a 2023 = o da Menoua, de Dschang; 2024/25 = o do Moungo); PWD Bamenda x PWD Kumba; Unisport du Haut-Nkam = Unisport de Bafang.
- **tan-1:** 1965 a 1998: só o campeão (1966 a 1982 e 1990 a 1995), só os primeiros colocados (1965, 1983, 1995/96) ou só a tabela (1985 a 1987, 1989, 1996/97, 1998); 1988 e 2000 a 2006: parte dos jogos. Fonte que resolveria: jornais tanzanianos (Daily News, Mwananchi) ou o arquivo da TFF.
- **tan-1:** 2011/12: os jogos vêm do ogol (a RSSSF só tem a tabela); um gol de diferença em 4 clubes, sem terceira fonte.
- **tan-1:** Rebaixamento: 2000 (cancelado), 2001, 2002, 2004 e 2007 marcados à mão pelas notas da página; 2004 "seem to have been" (a página não tem certeza); 2006 sem informação.
- **tan-1:** Autores dos gols só em parte (2004 a 2010/11 e alguns anos depois de 2020); artilheiros e cartões, nenhum. Fonte que resolveria: o ogol jogo a jogo (2007/08 em diante).
- **tan-1:** Identidade a conferir: Moro United = Kajumulo = Sigara (a RSSSF registra as trocas de nome, mas o clube parece ter mudado de cidade); JKT Tanzania = JKT Ruvu; Kahama United = KJ82 Rangers; Pamba = Pamba Jiji; Singida Fountain Gate = Singida Big Stars; o Singida Black Stars ficou separado do Ihefu.

## Próximas competições

- 2ªs divisões, na ordem do guia geral, só quando o Guilherme pedir. Como fazer: `COMECE-AQUI.md`, seção 4.
