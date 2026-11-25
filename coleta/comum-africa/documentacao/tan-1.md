# Campeonato Tanzaniano (`tan-1`) — documentação

Gerado por `python coleta/comum-africa/documentar.py` a partir do pacote `data/coleta/tan-1/pacote/`, do código `coleta/tan-1/` e do relatório `docs/coleta/tan-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 62, de 1965 a 2025/26; 32 sem jogos.
- **Jogos:** 5929 (5817 com placar); **gols:** 12332; **gols com autor:** 1299 (11%); **cartões:** 0.
- **Clubes:** 82; **artilheiros:** 0 edições com artilheiro (0 linhas, com empates).
- **Classificação final:** 62 edições; **tabelas publicadas guardadas para conferência:** 592 linhas.
- **No banco:** sim; **último commit do pacote:** a22036fc.
- **Observação da competição:** 1ª divisão tanzaniana: a liga do continente (hoje Ligi Kuu Tanzania Bara) de 1965 a 2025/26, com o campeão do continente em todos os anos (a lista que a federação e os clubes contam); sem a Union League de 1982 a 2003 (com Zanzibar) e sem a liga de Dar es Salaam (1921 a 1964). Pontos 2-1-0 (vitória, empate, derrota) até 1995 e 3-1-0 desde 1995/96.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão tanzaniana (tan-1): a liga do continente (Tanganica), de 1965 a 2025/26 (hoje Ligi Kuu
Tanzania Bara, a "NBC Premier League").

Escopo (pesquisa de 25/11/2026, aprovada pelo Guilherme; registrada em coleta/comum-africa/COMECE-AQUI.md): a liga
nacional do continente desde 1965, com o campeão do continente em todos os anos. É a lista que a federação (TFF) e os
clubes contam (o título de 2024 foi o "30º" do Young Africans). Ficam de fora a liga de Dar es Salaam (1921 a 1964), a
"Union League" de 1982 a 2003 (o título entre os melhores do continente e de Zanzibar, que a lista da RSSSF dá como
campeão nesses anos), a liga de Zanzibar (membro associado da CAF, com liga própria) e as copas.

Temporadas: ano civil até 2007 (o "1995/96" e o "1996/97" das páginas da RSSSF são os campeonatos que a lista chama de
1996 e 1997); de 2007/08 em diante, duas metades (a lista chama 2007/08 de "2008").

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)]; linha inicial 0: logo depois do cabeçalho; linha final None:
  Zanzibar, a Union League, uma copa ou outra divisão (FIM_PADRAO).
- tabelas: anos em que a página só tem a tabela.
- ogol: o calendário do ogol (liga-tanzaniana), quando a RSSSF não tem os jogos (`ogol` = id da edição no ogol).
Pontos: como as tabelas da RSSSF contam (Edicao.pontos).
```

**Edições:** 62, de 1965 a 2025/26: a liga do continente (Tanganica), hoje Ligi Kuu Tanzania Bara, com o campeão do continente em todos os anos. É a lista que a federação (TFF) e os clubes contam (o título de 2024 foi o "30º" do Young Africans). Ano civil até 2007 (a mini-liga de transição de 2007 incluída); duas metades de 2007/08 em diante. Pesquisa de 25/11/2026, aprovada pelo Guilherme.

**Fontes:** RSSSF (lista de campeões `tanzchamp.html`; páginas por ano de 1965, de 1982 a 1991 e de 1995/96 em diante: os primeiros colocados, a tabela ou parte dos jogos até 1998, os jogos de 1999 em diante); ogol (jogos de 2007/08 em diante: base de 2011/12, conferência, rodada e data nos outros); Wikipédia em inglês (tabela das temporadas que têm artigo). A ESPN não tem a liga.

**Clubes:** o nome pelo qual o clube é conhecido (Young Africans, Simba, Azam...). Mesmo clube com outro nome na mesma cidade é um só (Simba = Sunderland; Moro United = Kajumulo = Sigara; Kahama United = KJ82 Rangers); mudança de cidade gera outro clube (Singida Black Stars não é o Ihefu). Regras em `coleta/tan-1/clubes_tan.py`.

**Regras:** o placar é o da RSSSF (ou do ogol em 2011/12). A classificação é a tabela publicada (ordem oficial e pontos); nos anos de grupos e fase final (2000 a 2004), a tabela da fase final dá as primeiras posições. Pontos 2-1-0 (vitória, empate, derrota) até 1995 (pelas tabelas até 1989) e 3-1-0 desde 1995/96 (pelas tabelas desde 1996/97).

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 21.
- **Edições com alguma tabela divergente** (1; motivo no relatório, na edição): 2011/12.
- **Edições sem tabela para conferir** (40): 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 2000, 2001, 2002, 2003, 2004, 2005, 2006.
- **Edições com menos jogos que o esperado:** nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1960s | 5 | 0 | — | — | — | — | — | — | — | — |
| 1970s | 10 | 0 | — | — | — | — | — | — | — | — |
| 1980s | 10 | 122 | 0% | 0% | 54% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 10 | 236 | 100% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 11 | 1708 | 95% | 0% | 95% | 0% | 0% | 0% | 26% | 0.0 |
| 2010s | 10 | 2346 | 100% | 0% | 100% | 0% | 0% | 0% | 1% | 0.0 |
| 2020s | 6 | 1517 | 100% | 0% | 100% | 0% | 0% | 0% | 9% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na África: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1965: 2 clubes
- 1966 a 1982: 1 clubes
- 1983: 2 clubes
- 1984 a 1985: 8 clubes
- 1986 a 1987: 10 clubes
- 1988: 12 clubes
- 1989: 14 clubes
- 1990 a 1995: 1 clubes
- 1996: 3 clubes
- 1997 a 1998: 12 clubes
- 1999: 16 clubes
- 2000: 20 clubes
- 2001 a 2003: 24 clubes
- 2004: 20 clubes
- 2005 a 2006: 16 clubes
- 2007: 13 clubes
- 2007/08: 14 clubes
- 2008/09 a 2010/11: 12 clubes
- 2011/12 a 2014/15: 14 clubes
- 2015/16 a 2017/18: 16 clubes
- 2018/19 a 2019/20: 20 clubes
- 2020/21: 18 clubes
- 2021/22 a 2025/26: 16 clubes

**Pontos por vitória:**

- 1965 a 1995: 2
- 1996 a 2025/26: 3

**Nome oficial:**

- 1965 a 2025/26: Ligi Kuu Tanzania Bara

**Formato** (fases na ordem, do edicoes.csv):

- 1965: sem jogos (só a classificação incompleta)
- 1966 a 1982: sem jogos (só o campeão)
- 1983: sem jogos (só a classificação incompleta)
- 1984: pontos corridos
- 1985 a 1987: sem jogos (só a tabela final)
- 1988: jogos incompletos (só os resultados que a página traz)
- 1989: sem jogos (só a tabela final)
- 1990 a 1995: sem jogos (só o campeão)
- 1996: sem jogos (só a classificação incompleta)
- 1997 a 1998: sem jogos (só a tabela final)
- 1999: pontos corridos
- 2000: jogos incompletos (três jogos dos grupos sem resultado na página)
- 2001: jogos incompletos (faltam resultados da 1ª fase)
- 2002: jogos incompletos (faltam resultados da 1ª fase e três do "Super 8")
- 2003: jogos incompletos (faltam resultados da 1ª fase e gols do "Super Eight")
- 2004: jogos incompletos (faltam resultados da 1ª fase e do "Super Eight")
- 2005 a 2006: jogos incompletos (só os resultados que a página traz)
- 2007: 3 grupos + fase final + mata-mata
- 2007/08 a 2020/21: pontos corridos
- 2021/22 a 2025/26: pontos corridos + desempate

**Fases e grupos de cada edição com mais de uma fase:**

- 2000: Primeira fase (grupos, 4 grupos); Fase final (liga)
- 2001: Primeira fase (grupos, 2 grupos); Fase final (liga)
- 2002: Primeira fase (grupos, 4 grupos); Fase final (liga)
- 2003: Primeira fase (grupos, 4 grupos); Fase final (liga)
- 2007: Primeira fase (grupos, 3 grupos); Fase final (liga); Final (mata_mata, jogo_unico)
- 2021/22: Primeira fase (liga); Desempate do rebaixamento (mata_mata, ida_volta)
- 2022/23: Primeira fase (liga); Desempate do rebaixamento (mata_mata, ida_volta)
- 2023/24: Primeira fase (liga); Desempate do rebaixamento (mata_mata, ida_volta)
- 2024/25: Primeira fase (liga); Desempate do rebaixamento (mata_mata, ida_volta)
- 2025/26: Primeira fase (liga); Desempate do rebaixamento (mata_mata, ida_volta)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 39 edições
- lista de campeões da RSSSF: 23 edições

**Observações das edições:**

- 1965: a RSSSF só traz os primeiros colocados
- 1966: a RSSSF só traz o campeão
- 1967: a RSSSF só traz o campeão
- 1968: a RSSSF só traz o campeão
- 1969: a RSSSF só traz o campeão
- 1970: a RSSSF só traz o campeão
- 1971: a RSSSF só traz o campeão
- 1972: a RSSSF só traz o campeão
- 1973: a RSSSF só traz o campeão
- 1974: a RSSSF só traz o campeão
- 1975: a RSSSF só traz o campeão
- 1976: a RSSSF só traz o campeão
- 1977: a RSSSF só traz o campeão
- 1978: a RSSSF só traz o campeão
- 1979: a RSSSF só traz o campeão
- 1980: a RSSSF só traz o campeão
- 1981: a RSSSF só traz o campeão
- 1982: a RSSSF só traz o campeão do continente
- 1983: a RSSSF só traz os primeiros colocados
- 1985: a RSSSF só traz a tabela final
- 1986: a RSSSF só traz a tabela final
- 1987: a RSSSF só traz a tabela final
- 1989: a RSSSF só traz a tabela final
- 1990: a RSSSF só traz o campeão do continente
- 1991: a RSSSF só traz o campeão do continente
- 1992: a RSSSF só traz o campeão
- 1993: a RSSSF só traz o campeão
- 1994: a RSSSF só traz o campeão
- 1995: a RSSSF só traz o campeão
- 1996: a RSSSF só traz os primeiros colocados
- 1997: a RSSSF só traz a tabela final
- 1998: a RSSSF só traz a tabela final
- 2007: mini-liga de transição ("Ligi Ndogo") antes da mudança para temporadas de duas metades; a final (Simba x Young Africans, 1-1 e pênaltis) deu as vagas da CAF de 2008

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Young Africans: 32
- Simba: 22
- Mtibwa Sugar: 2
- Cosmopolitans: 1
- Mseto Sports: 1
- Pan African: 1
- Tukuyu Stars: 1
- Coastal Union: 1
- Azam: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1965 | Simba | Young Africans |
| 1966 | Simba | — |
| 1967 | Cosmopolitans | — |
| 1968 | Young Africans | — |
| 1969 | Young Africans | — |
| 1970 | Young Africans | — |
| 1971 | Young Africans | — |
| 1972 | Young Africans | — |
| 1973 | Simba | — |
| 1974 | Young Africans | — |
| 1975 | Mseto Sports | — |
| 1976 | Simba | — |
| 1977 | Simba | — |
| 1978 | Simba | — |
| 1979 | Simba | — |
| 1980 | Simba | — |
| 1981 | Young Africans | — |
| 1982 | Pan African | — |
| 1983 | Young Africans | Simba |
| 1984 | Simba | Pamba |
| 1985 | Young Africans | Maji Maji |
| 1986 | Tukuyu Stars | Maji Maji |
| 1987 | Young Africans | Pamba |
| 1988 | Coastal Union | Young Africans |
| 1989 | Young Africans | Pamba |
| 1990 | Simba | — |
| 1991 | Young Africans | — |
| 1992 | Young Africans | — |
| 1993 | Young Africans | — |
| 1994 | Simba | — |
| 1995 | Simba | — |
| 1996 | Young Africans | Simba |
| 1997 | Young Africans | Simba |
| 1998 | Young Africans | Tanzania Prisons |
| 1999 | Mtibwa Sugar | Young Africans |
| 2000 | Mtibwa Sugar | Young Africans |
| 2001 | Simba | Mtibwa Sugar |
| 2002 | Young Africans | Simba |
| 2003 | Simba | Tanzania Prisons |
| 2004 | Simba | Mtibwa Sugar |
| 2005 | Young Africans | Moro United |
| 2006 | Young Africans | Simba |
| 2007 | Simba | Young Africans |
| 2007/08 | Young Africans | Tanzania Prisons |
| 2008/09 | Young Africans | Simba |
| 2009/10 | Simba | Young Africans |
| 2010/11 | Young Africans | Simba |
| 2011/12 | Simba | Azam |
| 2012/13 | Young Africans | Azam |
| 2013/14 | Azam | Young Africans |
| 2014/15 | Young Africans | Azam |
| 2015/16 | Young Africans | Azam |
| 2016/17 | Young Africans | Simba |
| 2017/18 | Simba | Azam |
| 2018/19 | Simba | Young Africans |
| 2019/20 | Simba | Young Africans |
| 2020/21 | Simba | Young Africans |
| 2021/22 | Young Africans | Simba |
| 2022/23 | Young Africans | Simba |
| 2023/24 | Young Africans | Azam |
| 2024/25 | Young Africans | Simba |
| 2025/26 | Young Africans | Simba |

**Rebaixados marcados na classificação:** 84 em 28 edições (só onde a tabela publicada marca a queda); quem mais caiu: Maji Maji (4), Polisi Morogoro (4), Reli Morogoro (3), Moro United (3), Toto Africans (3).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1988: African Sports -1
- 1999: Kagera Stars -1

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/tan-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 6)

- **tanz01 · 45:** «20 10  2 10» → «20 10  2  8»: Mji: 10+2+10 não dá 20 jogos; 32 pontos = 10 vitórias e 2 empates, logo 8 derrotas
- **tanz01 · 510:** «20 10  2 10» → «20 10  2  8»: Mji: 10+2+10 não dá 20 jogos; 32 pontos = 10 vitórias e 2 empates, logo 8 derrotas (a segunda cópia da tabela)
- **tanz06 · 21:** «30 10 12  7» → «30 10 12  8»: Prisons: 10+12+7 não dá 30 jogos; 42 pontos = 10 vitórias e 12 empates, logo 8 derrotas
- **tanz06 · 31:** «30  6 12 13» → «30  6 12 12»: Bandari: 6+12+13 não dá 30 jogos; 30 pontos = 6 vitórias e 12 empates, logo 12 derrotas
- **tanz06 · 397:** «30 10 12  7» → «30 10 12  8»: Prisons: 10+12+7 não dá 30 jogos; 42 pontos = 10 vitórias e 12 empates, logo 8 derrotas (a segunda cópia da tabela)
- **tanz06 · 407:** «30  6 12 13» → «30  6 12 12»: Bandari: 6+12+13 não dá 30 jogos; 30 pontos = 6 vitórias e 12 empates, logo 12 derrotas (a segunda cópia da tabela)

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 6)

- **2004 · tanz04:61:** [descartado] nota sobre os gols do Moro United, do Mji e do Kahama ("Moro 16-9 goals; Mji 6-11 goals; Kahama 8-7 goals"), lida como jogo
- **2004 · tanz04:491:** [descartado] nota sobre os gols do Moro United, do Mji e do Kahama ("Moro 16-9 goals; Mji 6-11 goals; Kahama 8-7 goals"), lida como jogo
- **1999 · tanz99:168:** [oficial = None, nota = ] a nota diz que o jogo ainda podia ser dado ao Young Africans ("may yet be awarded 2-0"), mas a tabela conta o 1-1 de campo
- **1999 · tanz99:414:** [oficial = (2, 0), nota = abandonado aos 78' com 2-0] "abandoned in 78' at 2-0; awarded 2-0": não é abandono sem valer; a tabela conta o jogo
- **2000 · tanz00:71:4:** [oficial = (0, 2), nota = o Mji não compareceu] "Mji vs Mtibwa awarded 0-2, Mji dns"
- **2000 · tanz00:39:1:** [oficial = (2, 0), nota = abandonado aos 89' com 2-1] "Tukuyu-Majimaji abandoned at 2-1 in 89', awarded 2-0"

### Tabelas da página que não são da edição (`TABELAS_FORA`, 13)

- **2001 · tanz01:35:** linha da campanha anulada de um clube excluído (não conta na classificação)
- **2001 · tanz01:500:** linha da campanha anulada de um clube excluído (não conta na classificação)
- **2004 · tanz04:31:** linha da campanha anulada de um clube excluído (não conta na classificação)
- **2004 · tanz04:51:** linha da campanha anulada de um clube excluído (não conta na classificação)
- **2004 · tanz04:53:** linha da campanha anulada de um clube excluído (não conta na classificação)
- **2004 · tanz04:461:** linha da campanha anulada de um clube excluído (não conta na classificação)
- **2004 · tanz04:481:** linha da campanha anulada de um clube excluído (não conta na classificação)
- **2004 · tanz04:483:** linha da campanha anulada de um clube excluído (não conta na classificação)
- **2005 · tanz05:347:** tabela do meio da temporada (a final vem depois)
- **2005 · tanz05:352:** tabela do meio da temporada (a final vem depois)
- **2005 · tanz05:355:** tabela do meio da temporada (a final vem depois)
- **2005 · tanz05:454:** tabela do meio da temporada (a final vem depois)
- **2005 · tanz05:461:** tabela do meio da temporada (a final vem depois)

### Identidade dos clubes

Regras em `coleta/tan-1/clubes_tan.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes tanzanianos: cada grafia de cada fonte (RSSSF, ogol, Wikipédia) -> um nome de exibição.

- nome pelo qual o clube é conhecido: Young Africans (Yanga), Simba, Azam, Mtibwa Sugar, Coastal Union...;
- nome que já existe em outro país leva primeiro a cidade e, sem cidade que resolva, o país entre parênteses;
- o mesmo clube com outro nome, na mesma cidade, é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - Simba = Sunderland (até 1971; "Sunderland changed name to Simba in 1971");
  - Young Africans = Yanga;
  - Tanzania Prisons = Prisons = Mbeya Prisons;
  - Moro United = Kajumulo World Soccer = Sigara (TCC Sigara): a RSSSF registra as duas trocas ("Kajumulo were formerly
    known as Sigara", 1999; "Kajumulo World Soccer were renamed Moro United", 2001);
  - Singida United = Mto (Singida) ("Mto (Singida) apparently changed name to Singida United", 1999);
  - RTC Mwanza = Biashara (1986/87: "RTC Mwanza also listed as Biashara"); o Biashara United de Musoma (2018 em
    diante) é outro clube;
  - JKT Tanzania = JKT Ruvu = JKT Ruvu Stars = Ruvu JKT (o clube do exército de Ruvu, rebatizado em 2018);
  - Arusha FC = AFC; Tabora United = Kitayosce (rebatizado em 2023); Singida Fountain Gate = Singida Big Stars
    (rebatizado em 2023); Pamba = Pamba Jiji; Dodoma Jiji = "Dodoma"; Azam = Azzam United;
  - os clubes do exército com número: KJ977 (Meru Warriors, de Arusha), KJ44 (Karume Rangers);
  - Kahama United = KJ82 Rangers = Kahama Rangers (em 2003 a tabela do grupo só tem o "Kahama 82 Rangers", e os jogos
    chamam o clube de "Kahama U." e de "Kahama Rangers");
- mudança de cidade, compra de vaga ou refundação geram outro clube: o Singida Black Stars (2024/25 em diante) é o
  Ihefu (de Mbarali) depois de comprado e levado para Singida; o Reli de Kigoma (2004) não é o Reli de Morogoro.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
```

## 8. O que não deu para coletar

- **Fora do pacote:** a liga de Dar es Salaam (1921 a 1964); a "Union League" de 1982 a 2003, que decidia o título entre os melhores do continente e de Zanzibar (é o campeão que a lista da RSSSF dá nesses anos); a liga de Zanzibar (membro associado da CAF); as copas; as divisões de baixo.
- **Edições sem jogos** (32): 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1985, 1986, 1987, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998.
- **Décadas com menos da metade dos gols com autor:** 1980s, 1990s, 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1980s, 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 1965 a 1998: só o campeão (1966 a 1982 e 1990 a 1995), só os primeiros colocados (1965, 1983, 1995/96) ou só a tabela (1985 a 1987, 1989, 1996/97, 1998); 1988 e 2000 a 2006: parte dos jogos. Fonte que resolveria: jornais tanzanianos (Daily News, Mwananchi) ou o arquivo da TFF.
- 2011/12: os jogos vêm do ogol (a RSSSF só tem a tabela); um gol de diferença em 4 clubes, sem terceira fonte.
- Rebaixamento: 2000 (cancelado), 2001, 2002, 2004 e 2007 marcados à mão pelas notas da página; 2004 "seem to have been" (a página não tem certeza); 2006 sem informação.
- Autores dos gols só em parte (2004 a 2010/11 e alguns anos depois de 2020); artilheiros e cartões, nenhum. Fonte que resolveria: o ogol jogo a jogo (2007/08 em diante).
- Identidade a conferir: Moro United = Kajumulo = Sigara (a RSSSF registra as trocas de nome, mas o clube parece ter mudado de cidade); JKT Tanzania = JKT Ruvu; Kahama United = KJ82 Rangers; Pamba = Pamba Jiji; Singida Fountain Gate = Singida Big Stars; o Singida Black Stars ficou separado do Ihefu.

## 10. Arquivos e comandos

Código em `coleta/tan-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_ogol.py` | Baixa o calendário de cada edição da 1ª divisão tanzaniana no ogol para data/coleta/tan-1/ogol/<id>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão tanzaniana para data/coleta/tan-1/rsssf/: a lista de campeões (tanzchamp.html) |
| `baixar_wikipedia.py` | Baixa da Wikipédia em inglês (wikitexto, pela API) o artigo da liga ("Tanzanian Premier League") e o de cada temporada |
| `clubes_tan.py` | Identidade dos clubes tanzanianos: cada grafia de cada fonte (RSSSF, ogol, Wikipédia) -> um nome de exibição. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão tanzaniana (tan-1): a liga do continente (Tanganica), de 1965 a 2025/26 (hoje Ligi Kuu |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão tanzaniana, edição a edição (entram no relatório). |
| `importar.py` | Junta as fontes da 1ª divisão tanzaniana e grava o pacote em data/coleta/tan-1/pacote/ e o relatório em docs/coleta/tan-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/tan-1/rsssf/) com o leitor comum (rsssf_africa), |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol (copiado de coleta/chi-1/outras_fontes.py, sem a ESPN, que não tem a liga egípcia). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |
| `wiki_tabelas.py` | Tabelas finais dos artigos de temporada da Wikipédia em inglês (data/coleta/tan-1/wikipedia/en_<temporada>.txt). A lista de campeões e a de artilheiros ficam vazias: o artigo da |

- Fontes baixadas: `data/coleta/tan-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-africa/`, do ogol em `data/cache/ogol-tan-1/`.
- Pacote: `data/coleta/tan-1/pacote/`; relatório: `docs/coleta/tan-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/tan-1/baixar_ogol.py
python coleta/tan-1/baixar_rsssf.py
python coleta/tan-1/baixar_wikipedia.py
python coleta/tan-1/importar.py
python coleta/tan-1/conferir.py [-v temporada]   # divergências
python coleta/comum-africa/testar_carga.py tan-1 <scratchpad>
python coleta/comum-africa/documentar.py
```

