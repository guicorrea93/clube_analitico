# Campeonato Sul-Africano (`rsa-1`) — documentação

Gerado por `python coleta/comum-africa/documentar.py` a partir do pacote `data/coleta/rsa-1/pacote/`, do código `coleta/rsa-1/` e do relatório `docs/coleta/rsa-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 55, de 1971 a 2025/26; 22 sem jogos.
- **Jogos:** 8108 (8057 com placar); **gols:** 18432; **gols com autor:** 4721 (26%); **cartões:** 0.
- **Clubes:** 89; **artilheiros:** 5 edições com artilheiro (5 linhas, com empates).
- **Classificação final:** 55 edições; **tabelas publicadas guardadas para conferência:** 878 linhas.
- **No banco:** ainda não; **último commit do pacote:** nenhum (pacote ainda não commitado).
- **Observação da competição:** 1ª divisão sul-africana na linha que a RSSSF e a imprensa contam: NPSL (1971 a 1984), NSL (1985 a 1995) e Premier Soccer League (desde 1996/97). Sem as ligas separadas por raça do apartheid (NFL dos brancos, SASL/FPL), a NPSL paralela depois de 1985 e o torneio de transição de 1996. Pontos 2-1-0 (vitória, empate, derrota) até 1994 e 3-1-0 desde 1995.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão sul-africana (rsa-1): NPSL (1971 a 1984), NSL (1985 a 1995) e PSL (1996/97 a 2025/26).

Escopo (pesquisa de 24/11/2026, aprovada pelo Guilherme; registrada em coleta/comum-africa/COMECE-AQUI.md): a linha do
futebol profissional que a RSSSF ("NPSL/NSL/PSL championships, 55, since 1971") e a imprensa contam (Mamelodi Sundowns 18,
Kaizer Chiefs 12, Orlando Pirates 10). Ficam de fora as ligas separadas por raça do apartheid (NFL dos brancos, 1959-1977;
SASL/FPL dos "coloured"), a NPSL que seguiu em paralelo depois de 1985, as NPSL amadoras de 1968 e 1969 e o torneio de
transição de 1996 ("Coca-Cola Challenge"), que ninguém conta como título.

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)]; página zafAA (ou zafAAAA desde 2009/10): a do ano (1971 a
  1996) ou do ano em que a temporada termina (zaf97 = 1996/97; zaf2010 = 2009/10). Linha inicial 0: logo depois do
  cabeçalho; linha final None: a primeira copa ou outra divisão (FIM_PADRAO).
- tabelas: anos em que a RSSSF só tem a tabela final.
- ogol: o calendário do ogol (liga-sul-africana, desde 1996/97), quando a RSSSF não tem os jogos.
Pontos: 2-1-0 (vitória, empate, derrota) até 1994 e 3-1-0 desde 1995, como as tabelas da RSSSF contam.
```

**Edições:** 55: NPSL de 1971 a 1984, NSL de 1985 a 1995 e PSL de 1996/97 a 2025/26, como a lista de campeões da RSSSF (`zafchamp.html`, "NPSL/NSL/PSL championships, 55, since 1971") e a imprensa contam (pesquisa de 24/11/2026, aprovada pelo Guilherme). Ficam de fora as ligas separadas por raça do apartheid (NFL dos brancos, SASL/FPL), a NPSL que seguiu em paralelo depois de 1985, as NPSL amadoras de 1968 e 1969 e o torneio de transição de 1996.

**Fontes:** RSSSF (páginas por temporada, `data/coleta/rsa-1/rsssf/`: a tabela final de 1971 a 1995, com parte dos jogos em 1987, 1992 e 1993; jogos de 1996/97 a 2024/25, completos desde 1997/98); ogol (jogos de 2005/06 em diante: base de 2025/26, conferência, rodada e data nos outros anos); Wikipédia em inglês (a tabela de cada temporada, terceira fonte). A ESPN não tem a liga.

**Clubes:** o nome pelo qual o clube é conhecido; nome que já existe em outro país leva "(África do Sul)" (Santos, Rangers, Dynamos, Leeds United...); clube refundado com o nome de um antigo, o ano do antigo (Durban City (1959), Cape Town City (1962), Highlands Park (1959)). Mesmo clube com outro nome é um só (Zulu Royals = AmaZulu; Pretoria City = SuperSport United; Ajax Cape Town = Cape Town Spurs). Regras em `coleta/rsa-1/clubes_rsa.py`.

**Regras:** o placar é o da RSSSF (ou do ogol em 2025/26). A classificação é a tabela publicada (ordem oficial e pontos). Pontos 2-1-0 (vitória, empate, derrota) até 1994 e 3-1-0 desde 1995.

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 28.
- **Edições com alguma tabela divergente** (1; motivo no relatório, na edição): 1999/00.
- **Edições sem tabela para conferir** (26): 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996/97.
- **Edições com menos jogos que o esperado:** nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970s | 9 | 0 | — | — | — | — | — | — | — | — |
| 1980s | 10 | 196 | 0% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 10 | 1519 | 65% | 0% | 87% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 10 | 2548 | 100% | 0% | 64% | 0% | 0% | 0% | 68% | 0.0 |
| 2010s | 10 | 2402 | 100% | 0% | 100% | 0% | 0% | 0% | 13% | 0.0 |
| 2020s | 6 | 1443 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na África: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1971: 13 clubes
- 1972 a 1973: 1 clubes
- 1974: 15 clubes
- 1975: 1 clubes
- 1976: 15 clubes
- 1977: 1 clubes
- 1978: 24 clubes
- 1979 a 1982: 18 clubes
- 1983: 19 clubes
- 1984 a 1987: 18 clubes
- 1988: 17 clubes
- 1989: 18 clubes
- 1990: 17 clubes
- 1991: 24 clubes
- 1992: 22 clubes
- 1993: 20 clubes
- 1994: 18 clubes
- 1995: 17 clubes
- 1996/97 a 2001/02: 18 clubes
- 2002/03 a 2025/26: 16 clubes

**Pontos por vitória:**

- 1971 a 1994: 2
- 1995 a 2025/26: 3

**Nome oficial:**

- 1971 a 1984: NPSL (National Professional Soccer League)
- 1985 a 1995: NSL (National Soccer League)
- 1996/97 a 2025/26: Premier Soccer League (Premiership)

**Formato** (fases na ordem, do edicoes.csv):

- 1971: sem jogos (só a tabela final)
- 1972 a 1973: sem jogos (só o campeão)
- 1974: sem jogos (só a tabela final)
- 1975: sem jogos (só o campeão)
- 1976: sem jogos (só a tabela final)
- 1977: sem jogos (só o campeão)
- 1978 a 1986: sem jogos (só a tabela final)
- 1987: jogos incompletos (só os resultados que a página traz)
- 1988 a 1991: sem jogos (só a tabela final)
- 1992 a 1993: jogos incompletos (só os resultados que a página traz)
- 1994 a 1995: sem jogos (só a tabela final)
- 1996/97: jogos incompletos (só os resultados que a página traz)
- 1997/98 a 2025/26: pontos corridos

**Fases e grupos de cada edição com mais de uma fase:**

- nenhuma

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 51 edições
- lista de campeões da RSSSF: 4 edições

**Observações das edições:**

- 1971: a RSSSF só traz a tabela final
- 1972: a RSSSF só traz o campeão da NPSL (a página do ano é da NFL)
- 1973: a RSSSF só traz o campeão da NPSL (a página do ano é da NFL)
- 1974: a RSSSF só traz a tabela final
- 1975: a RSSSF só traz o campeão da NPSL (a página do ano é da NFL)
- 1976: a RSSSF só traz a tabela final
- 1977: a RSSSF só traz o campeão da NPSL (a página do ano é da NFL)
- 1978: a RSSSF só traz a tabela final
- 1979: a RSSSF só traz a tabela final
- 1980: a RSSSF só traz a tabela final
- 1981: a RSSSF só traz a tabela final
- 1982: a RSSSF só traz a tabela final
- 1983: a RSSSF só traz a tabela final
- 1984: a RSSSF só traz a tabela final
- 1985: a RSSSF só traz a tabela final
- 1986: a RSSSF só traz a tabela final
- 1988: a RSSSF só traz a tabela final
- 1989: a RSSSF só traz a tabela final
- 1990: a RSSSF só traz a tabela final
- 1991: a RSSSF só traz a tabela final
- 1994: a RSSSF só traz a tabela final
- 1995: a RSSSF só traz a tabela final
- 2025/26: os jogos vêm do calendário do ogol (a RSSSF só traz a tabela)

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Mamelodi Sundowns: 18
- Kaizer Chiefs: 12
- Orlando Pirates: 10
- SuperSport United: 3
- Durban City (1959): 2
- AmaZulu: 1
- Lusitano: 1
- Highlands Park (1959): 1
- Durban Bush Bucks: 1
- Rangers (África do Sul): 1
- Jomo Cosmos: 1
- Cape Town Spurs: 1
- Manning Rangers: 1
- Santos (África do Sul): 1
- Wits University: 1

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1971 | Orlando Pirates | Kaizer Chiefs |
| 1972 | AmaZulu | — |
| 1973 | Orlando Pirates | — |
| 1974 | Kaizer Chiefs | Moroka Swallows |
| 1975 | Orlando Pirates | — |
| 1976 | Orlando Pirates | Kaizer Chiefs |
| 1977 | Kaizer Chiefs | — |
| 1978 | Lusitano | Wits University |
| 1979 | Kaizer Chiefs | Arcadia Shepherds |
| 1980 | Highlands Park (1959) | Kaizer Chiefs |
| 1981 | Kaizer Chiefs | Highlands Park (1959) |
| 1982 | Durban City (1959) | Wits University |
| 1983 | Durban City (1959) | Arcadia Shepherds |
| 1984 | Kaizer Chiefs | Moroka Swallows |
| 1985 | Durban Bush Bucks | Rangers (África do Sul) |
| 1986 | Rangers (África do Sul) | Durban Bush Bucks |
| 1987 | Jomo Cosmos | Kaizer Chiefs |
| 1988 | Mamelodi Sundowns | Jomo Cosmos |
| 1989 | Kaizer Chiefs | Orlando Pirates |
| 1990 | Mamelodi Sundowns | Kaizer Chiefs |
| 1991 | Kaizer Chiefs | Mamelodi Sundowns |
| 1992 | Kaizer Chiefs | Hellenic |
| 1993 | Mamelodi Sundowns | Moroka Swallows |
| 1994 | Orlando Pirates | Cape Town Spurs |
| 1995 | Cape Town Spurs | Mamelodi Sundowns |
| 1996/97 | Manning Rangers | Kaizer Chiefs |
| 1997/98 | Mamelodi Sundowns | Kaizer Chiefs |
| 1998/99 | Mamelodi Sundowns | Kaizer Chiefs |
| 1999/00 | Mamelodi Sundowns | Orlando Pirates |
| 2000/01 | Orlando Pirates | Kaizer Chiefs |
| 2001/02 | Santos (África do Sul) | SuperSport United |
| 2002/03 | Orlando Pirates | SuperSport United |
| 2003/04 | Kaizer Chiefs | Cape Town Spurs |
| 2004/05 | Kaizer Chiefs | Orlando Pirates |
| 2005/06 | Mamelodi Sundowns | Orlando Pirates |
| 2006/07 | Mamelodi Sundowns | Platinum Stars |
| 2007/08 | SuperSport United | Cape Town Spurs |
| 2008/09 | SuperSport United | Orlando Pirates |
| 2009/10 | SuperSport United | Mamelodi Sundowns |
| 2010/11 | Orlando Pirates | Cape Town Spurs |
| 2011/12 | Orlando Pirates | Moroka Swallows |
| 2012/13 | Kaizer Chiefs | Platinum Stars |
| 2013/14 | Mamelodi Sundowns | Kaizer Chiefs |
| 2014/15 | Kaizer Chiefs | Mamelodi Sundowns |
| 2015/16 | Mamelodi Sundowns | Wits University |
| 2016/17 | Wits University | Mamelodi Sundowns |
| 2017/18 | Mamelodi Sundowns | Orlando Pirates |
| 2018/19 | Mamelodi Sundowns | Orlando Pirates |
| 2019/20 | Mamelodi Sundowns | Kaizer Chiefs |
| 2020/21 | Mamelodi Sundowns | AmaZulu |
| 2021/22 | Mamelodi Sundowns | Cape Town City |
| 2022/23 | Mamelodi Sundowns | Orlando Pirates |
| 2023/24 | Mamelodi Sundowns | Orlando Pirates |
| 2024/25 | Mamelodi Sundowns | Orlando Pirates |
| 2025/26 | Orlando Pirates | Mamelodi Sundowns |

**Rebaixados marcados na classificação:** 105 em 48 edições (só onde a tabela publicada marca a queda); quem mais caiu: African Wanderers (8), AmaZulu (5), Jomo Cosmos (5), Bloemfontein Celtic (4), Cape Town Spurs (4).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1974: Benoni United -1
- 1976: Leeds United (África do Sul) +6
- 1980: Hellenic -2
- 1990: Kaizer Chiefs +2
- 1990: Giant Blackpool +1
- 1994: Orlando Pirates +1
- 1994: Vaal Professionals -1
- 1996/97: Hellenic +1
- 2000/01: Bloemfontein Celtic -3
- 2003/04: Platinum Stars -3
- 2003/04: Hellenic -1
- 2018/19: AmaZulu -6

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/rsa-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Erros de digitação da página da RSSSF corrigidos antes da leitura (`CONSERTA_TEXTO`, 5)

- **zaf82 · 22:** «34  15  9  0» → «34  15  9 10»: Arcadia: 15+9+0 não dá 34 jogos; 39 pontos = 15 vitórias e 9 empates, logo 10 derrotas
- **zaf82 · 23:** «34  16  7  1» → «34  16  7 11»: Dynamos: 16+7+1 não dá 34 jogos; 39 pontos = 16 vitórias e 7 empates, logo 11 derrotas
- **zaf86 · 28:** «34   5  14  14» → «34   5  14  15»: Durban City: 5+14+14 não dá 34 jogos; 24 pontos = 5 vitórias e 14 empates, logo 15 derrotas
- **zaf93 · 29:** «38  13 10 13» → «38  13 10 15»: Witbank Aces: 13+10+13 não dá 38 jogos; 36 pontos = 13 vitórias e 10 empates, logo 15 derrotas
- **zaf93 · 356:** «38  13  10  13» → «38  13  10  15»: Witbank Aces (a tabela repetida no fim da temporada): o mesmo erro

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 1)

- **2001/02 · zaf02:49:** [oficial = (1, 0), nota = abandonado aos 85' com 1-0 (jogadores do Orlando Pirates agrediram o árbitro); 1-0 dado ao Ajax Cape Town] 1-0 dado ao Ajax Cape Town (nota da página, na linha de baixo)

### Tabelas da página que não são da edição (`TABELAS_FORA`, 2)

- **2024/25 · zaf2025:42:** campanha do Royal AM até a exclusão (resultados anulados), não é tabela da edição
- **2024/25 · zaf2025:473:** campanha do Royal AM até a exclusão (repetida no fim da página)

### Divergências entre fontes já explicadas (`EXPLICACOES`, 9)

- **1987:** a RSSSF só traz parte dos jogos da temporada; a classificação é a tabela publicada
- **1992:** a RSSSF só traz parte dos jogos da temporada; a classificação é a tabela publicada
- **1993:** a RSSSF só traz parte dos jogos da temporada; a classificação é a tabela publicada
- **1993:** quatro clubes mudaram de nome no meio da temporada (notas da página): Score Stars = Qwa Qwa Stars, Ratanang = Chatsworth Rangers, Albany City = Pretoria City, Highlands Park = Welkom Eagles
- **1996/97:** a RSSSF só traz parte dos jogos da temporada; a classificação é a tabela publicada
- **1999/00:** a lista de jogos da página não fecha com a tabela em seis clubes (a Wikipédia confirma a tabela da RSSSF); nenhum placar foi mudado e o relatório aponta o jogo provável
- **2001/02:** Ajax Cape Town x Orlando Pirates: abandonado aos 85' com 1-0 e dado ao Ajax Cape Town por 1-0 (nota da página)
- **2007/08:** o Benoni Premier United mudou de nome para Thanda Royal Zulu no meio da temporada: é um clube só
- **2024/25:** o Royal AM foi excluído e todos os seus resultados anulados; o Cape Town City perdeu o desempate de acesso

### Identidade dos clubes

Regras em `coleta/rsa-1/clubes_rsa.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes sul-africanos: cada grafia de cada fonte -> nome de exibição único no mundo.

Regras do guia internacional (docs/agentes-internacionais-COMECE-AQUI.md, seção 4):
- nome pelo qual o clube é conhecido ("Kaizer Chiefs", "Orlando Pirates", "Mamelodi Sundowns");
- nome que já existe em outro país leva o país ("Santos (África do Sul)", "Rangers (África do Sul)", "Dynamos (África do
  Sul)", "Leeds United (África do Sul)", "Vasco da Gama (África do Sul)"); clube refundado com o nome de um antigo, o ano
  de fundação do antigo ("Durban City (1959)", "Cape Town City (1962)", "Highlands Park (1959)");
- o mesmo clube com outro nome é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - AmaZulu = Zulu Royals; Bloemfontein Celtic = Frasers Celtic; SuperSport United = Pretoria City (comprado e renomeado
    em 1994); Jomo Cosmos = Dion Cosmos; Free State Stars = Qwa Qwa Stars; Platinum Stars = Silver Stars; Mpumalanga Black
    Aces = Witbank (Black) Aces; Wits University = Bidvest Wits; Tembisa Classic = Thembisa Classic;
  - Cape Town Spurs = Ajax Cape Town (fusão do Cape Town Spurs com o Seven Stars em 1999; voltou ao nome Cape Town Spurs
    em 2020);
  - 1993 (notas da página): Score Stars = Qwa Qwa Stars (Free State Stars); Ratanang (Mahlosians) = "Rangers" =
    Chatsworth Rangers; Albany City = Pretoria City (SuperSport United); Welkom Eagles = Highlands Park (1959), que mudou de
    dono e foi para Welkom no meio da temporada;
  - Thanda Royal Zulu = Benoni Premier United (mudou de nome no meio de 2007/08); "Rangers" nos jogos de 1996/97 em
    diante é o Manning Rangers (o Rangers de Joanesburgo, campeão de 1986, só até 1995);
  - Bush Bucks: o "Bush Bucks" de Durban (campeão de 1985) até 1987 é o Durban Bush Bucks; de 1988 em diante, o Bush Bucks
    de Umtata ("Umtata Bucks").
- clubes que compraram a vaga de outro (Marumo Gallants, Royal AM, TS Galaxy, Cape Town City de 2016, Siwelele) são clubes
  próprios, com o nome deles.

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
```

## 8. O que não deu para coletar

- **Fora do pacote:** as copas (Nedbank, MTN 8, Telkom/Carling Knockout), a 2ª divisão e os jogos de acesso.
- **Edições sem jogos** (22): 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1988, 1989, 1990, 1991, 1994, 1995.
- **Décadas com menos da metade dos gols com autor:** 1980s, 1990s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1980s, 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- Ainda não carregado no banco (pacote pronto em 24/11/2026; teste de carga OK).
- 1971 a 1995: só a tabela final (a RSSSF não tem os jogos), fora 1987, 1992 e 1993 (parte dos jogos); 1972, 1973, 1975 e 1977: só o campeão (a página do ano é da NFL). 1996/97: parte dos jogos. O ogol só tem jogos de 2005/06 em diante. Fonte que resolveria: jornais sul-africanos (The World, Sowetan, Rand Daily Mail) ou o arquivo da PSL.
- Rebaixamento pelos desempates de acesso (2004/05 a 2025/26) marcado à mão (o 15º que não está na 1ª divisão do ano seguinte); clubes que saíram por venda da vaga, fusão ou redução da liga ficam sem marca.
- Autores dos gols só onde a RSSSF traz; artilheiros de poucas temporadas (contagem dos gols com autor). Fonte que resolveria: o ogol jogo a jogo (2005/06 em diante).
- Identidade a conferir: Cape Town Spurs = Ajax Cape Town (fusão de 1999 e volta ao nome em 2020); SuperSport United = Pretoria City = Albany City; Free State Stars = Qwa Qwa Stars = Score Stars; Highlands Park (1959) = Welkom Eagles (1993); Durban Bush Bucks (até 1987) x Bush Bucks de Umtata (desde 1988); Mpumalanga Black Aces = Witbank Aces = Total Aces.

## 10. Arquivos e comandos

Código em `coleta/rsa-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_ogol.py` | Baixa o calendário de cada edição da 1ª divisão sul-africana no ogol para data/coleta/rsa-1/ogol/<id>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão sul-africana para data/coleta/rsa-1/rsssf/: a lista de campeões (zafchamp.html) |
| `baixar_wikipedia.py` | Baixa da Wikipédia em inglês (wikitexto, pela API) o artigo da liga ("South African Premiership", com a lista de |
| `clubes_rsa.py` | Identidade dos clubes sul-africanos: cada grafia de cada fonte -> nome de exibição único no mundo. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão sul-africana (rsa-1): NPSL (1971 a 1984), NSL (1985 a 1995) e PSL (1996/97 a 2025/26). |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão sul-africana, edição a edição (entram no relatório). |
| `importar.py` | Junta as fontes da 1ª divisão sul-africana e grava o pacote em data/coleta/rsa-1/pacote/ e o relatório em docs/coleta/rsa-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/rsa-1/rsssf/) com o leitor comum (rsssf_africa), |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol (copiado de coleta/chi-1/outras_fontes.py, sem a ESPN, que não tem a liga egípcia). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |
| `wiki_tabelas.py` | Tabelas finais dos artigos de temporada da Wikipédia em inglês (data/coleta/rsa-1/wikipedia/en_<temporada>.txt). A lista de campeões e a de artilheiros ficam vazias: o artigo da |

- Fontes baixadas: `data/coleta/rsa-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-africa/`, do ogol em `data/cache/ogol-rsa-1/`.
- Pacote: `data/coleta/rsa-1/pacote/`; relatório: `docs/coleta/rsa-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/rsa-1/baixar_ogol.py
python coleta/rsa-1/baixar_rsssf.py
python coleta/rsa-1/baixar_wikipedia.py
python coleta/rsa-1/importar.py
python coleta/rsa-1/conferir.py [-v temporada]   # divergências
python coleta/comum-africa/testar_carga.py rsa-1 <scratchpad>
python coleta/comum-africa/documentar.py
```

