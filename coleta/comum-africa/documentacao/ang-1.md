# Campeonato Angolano (`ang-1`) — documentação

Gerado por `python coleta/comum-africa/documentar.py` a partir do pacote `data/coleta/ang-1/pacote/`, do código `coleta/ang-1/` e do relatório `docs/coleta/ang-1.md` (que tem o detalhe edição a edição).

## 1. O que temos

- **Edições:** 48, de 1979 a 2025/26; 17 sem jogos.
- **Jogos:** 6488 (6398 com placar); **gols:** 13984; **gols com autor:** 440 (3%); **cartões:** 0.
- **Clubes:** 93; **artilheiros:** 0 edições com artilheiro (0 linhas, com empates).
- **Classificação final:** 48 edições; **tabelas publicadas guardadas para conferência:** 710 linhas.
- **No banco:** ainda não; **último commit do pacote:** nenhum (pacote ainda não commitado).
- **Observação da competição:** 1ª divisão angolana: o Girabola de 1979 a 2025/26, como a federação o numera (2025/26 é o XLVIII Girabola); sem o Campeonato Provincial da era colonial (1941 a 1974). 2019/20 abandonado (Covid-19), sem campeão. Pontos 2-1-0 (vitória, empate, derrota) até 1994 e 3-1-0 desde 1995.

## 2. Edições, fontes e regras

**Como as edições foram definidas** (docstring de `edicoes.py`):

```
Edições da 1ª divisão angolana (ang-1): o Girabola, de 1979 a 2025/26.

Escopo (pesquisa de 25/11/2026, aprovada pelo Guilherme; registrada em coleta/comum-africa/COMECE-AQUI.md): o Girabola
desde o primeiro, em 1979, como a federação o numera (2025/26 é o "XLVIII Girabola") e os clubes contam os títulos. A
temporada 2019/20, abandonada pela pandemia de Covid-19, entra sem campeão. Fica de fora o Campeonato Provincial da era
colonial (1941 a 1974; 1975 abandonado), que a federação não conta, e as copas (Taça e Supertaça).

Temporadas: ano civil de 1979 a 2018; duas metades de 2018/19 em diante (as páginas da RSSSF e o ogol rotulam igual).

Fontes dos jogos por edição:
- trechos: [(página da RSSSF, linha inicial, linha final)]; linha inicial 0: logo depois do cabeçalho; linha final None:
  a Taça, a Supertaça ou outra divisão (FIM_PADRAO).
- tabelas: anos em que a página só tem a tabela.
- ogol: o calendário do ogol (liga-angolana), quando a RSSSF não tem os jogos (`ogol` = id da edição no ogol).
Pontos: como as tabelas da RSSSF contam (Edicao.pontos).
```

**Edições:** 48, de 1979 a 2025/26: o Girabola, como a federação o numera (2025/26 é o "XLVIII Girabola") e os clubes contam os títulos. Ano civil até 2018; duas metades de 2018/19 em diante. 2019/20 foi abandonado pela pandemia de Covid-19 e entra sem campeão. Pesquisa de 25/11/2026, aprovada pelo Guilherme.

**Fontes:** RSSSF (lista de campeões `angochamp.html`; páginas por ano: a tabela de 1981 a 1997, os jogos em 1979, 1980 e de 1998 em diante); ogol (jogos de 1999 em diante: conferência, rodada e data). A Wikipédia ficou para depois (a API recusou o download em 25/11/2026). A ESPN não tem a liga.

**Clubes:** o nome pelo qual o clube é conhecido no Brasil (1º de Agosto, Petro de Luanda, Benfica de Luanda...). Mesmo clube com outro nome na mesma cidade é um só (ASA de Luanda = Atlético Sport Aviação; Atlético do Namibe = Desportivo Sonangol do Namibe). Regras em `coleta/ang-1/clubes_ang.py`.

**Regras:** o placar é o da RSSSF. A classificação é a tabela publicada (ordem oficial e pontos). Pontos 2-1-0 (vitória, empate, derrota) até 1994 e 3-1-0 desde 1995 ("introduction of 3-1-0 point system in 1995", RSSSF).

## 3. Conferência

Cada edição é comparada com as tabelas publicadas da RSSSF (e da Wikipédia, quando há); campeão e vice, com a lista de campeões da Wikipédia.

- **Edições em que todas as tabelas fecham com os jogos:** 27.
- **Edições com alguma tabela divergente** (3; motivo no relatório, na edição): 1980, 2000, 2007.
- **Edições sem tabela para conferir** (18): 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998.
- **Edições com menos jogos que o esperado:** nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols). Década pelo ano de início da edição.

| Década | Edições | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970s | 1 | 126 | 100% | 0% | 100% | 0% | 0% | 0% | 3% | 0.0 |
| 1980s | 10 | 182 | 23% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 10 | 374 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 10 | 1821 | 100% | 0% | 100% | 0% | 0% | 0% | 11% | 0.0 |
| 2010s | 11 | 2577 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0.0 |
| 2020s | 6 | 1408 | 100% | 0% | 100% | 2% | 0% | 0% | 0% | 0.0 |

Árbitro e estatísticas (chutes, faltas, escanteios) não são coletados na África: nenhuma fonte em lote tem.

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1979: 24 clubes
- 1980 a 1981: 14 clubes
- 1982: 13 clubes
- 1983 a 1989: 14 clubes
- 1990: 13 clubes
- 1991 a 1992: 16 clubes
- 1993 a 1994: 12 clubes
- 1995: 14 clubes
- 1996: 13 clubes
- 1997: 14 clubes
- 1998: 16 clubes
- 1999: 15 clubes
- 2000 a 2009: 14 clubes
- 2010 a 2022/23: 16 clubes
- 2023/24: 15 clubes
- 2024/25 a 2025/26: 16 clubes

**Pontos por vitória:**

- 1979 a 1994: 2
- 1995 a 2025/26: 3

**Nome oficial:**

- 1979 a 2025/26: Girabola

**Formato** (fases na ordem, do edicoes.csv):

- 1979: 4 grupos + fase final + mata-mata
- 1980: pontos corridos
- 1981 a 1997: sem jogos (só a tabela final)
- 1998: jogos incompletos (só os resultados que a página traz)
- 1999 a 2018/19: pontos corridos
- 2019/20: temporada não terminada
- 2020/21 a 2025/26: pontos corridos

**Fases e grupos de cada edição com mais de uma fase:**

- 1979: Primeira fase (grupos, 4 grupos); Fase final (liga); Final (mata_mata, jogo_unico)

**Critério de desempate:** a classificação final é a tabela publicada (ordem oficial) quando ela traz todos os clubes e fecha com os jogos; senão é calculada por fase alcançada, pontos, saldo e gols pró (coluna `fonte` do classificacao_final.csv). O campeão e o vice da lista oficial ficam em 1º e 2º.

- RSSSF: 48 edições

**Observações das edições:**

- 1981: a RSSSF só traz a tabela final
- 1982: a RSSSF só traz a tabela final
- 1983: a RSSSF só traz a tabela final
- 1984: a RSSSF só traz a tabela final
- 1985: a RSSSF só traz a tabela final
- 1986: a RSSSF só traz a tabela final
- 1987: a RSSSF só traz a tabela final
- 1988: a RSSSF só traz a tabela final
- 1989: a RSSSF só traz a tabela final
- 1990: a RSSSF só traz a tabela final
- 1991: a RSSSF só traz a tabela final
- 1992: a RSSSF só traz a tabela final
- 1993: a RSSSF só traz a tabela final
- 1994: a RSSSF só traz a tabela final
- 1995: a RSSSF só traz a tabela final
- 1996: a RSSSF só traz a tabela final
- 1997: a RSSSF só traz a tabela final
- 2019/20: abandonado em 14/05/2020 (pandemia de Covid-19), sem campeão

## 6. Campeões, rebaixados e ajustes de pontos

**Títulos:**

- Petro de Luanda: 20
- 1º de Agosto: 13
- Recreativo do Libolo: 4
- ASA de Luanda: 3
- 1º de Maio: 2
- Sagrada Esperança: 2
- Interclube: 2
- Kabuscorp: 1
- Sem campeão: 2019/20

**Campeão e vice de cada edição:**

| Edição | Campeão | Vice |
|---|---|---|
| 1979 | 1º de Agosto | Nacional de Benguela |
| 1980 | 1º de Agosto | Desportivo da TAAG |
| 1981 | 1º de Agosto | Desportivo da TAAG |
| 1982 | Petro de Luanda | 1º de Agosto |
| 1983 | 1º de Maio | 1º de Agosto |
| 1984 | Petro de Luanda | Interclube |
| 1985 | 1º de Maio | Interclube |
| 1986 | Petro de Luanda | Interclube |
| 1987 | Petro de Luanda | 1º de Agosto |
| 1988 | Petro de Luanda | Ferroviário da Huíla |
| 1989 | Petro de Luanda | 1º de Maio |
| 1990 | Petro de Luanda | 1º de Maio |
| 1991 | 1º de Agosto | Sagrada Esperança |
| 1992 | 1º de Agosto | ASA de Luanda |
| 1993 | Petro de Luanda | 1º de Maio |
| 1994 | Petro de Luanda | 1º de Maio |
| 1995 | Petro de Luanda | ASA de Luanda |
| 1996 | 1º de Agosto | Petro de Luanda |
| 1997 | Petro de Luanda | Sagrada Esperança |
| 1998 | 1º de Agosto | Petro de Luanda |
| 1999 | 1º de Agosto | Académica do Lobito |
| 2000 | Petro de Luanda | ASA de Luanda |
| 2001 | Petro de Luanda | ASA de Luanda |
| 2002 | ASA de Luanda | 1º de Agosto |
| 2003 | ASA de Luanda | Petro de Luanda |
| 2004 | ASA de Luanda | Sagrada Esperança |
| 2005 | Sagrada Esperança | ASA de Luanda |
| 2006 | 1º de Agosto | Petro de Luanda |
| 2007 | Interclube | 1º de Agosto |
| 2008 | Petro de Luanda | 1º de Agosto |
| 2009 | Petro de Luanda | Recreativo do Libolo |
| 2010 | Interclube | Recreativo da Caála |
| 2011 | Recreativo do Libolo | Kabuscorp |
| 2012 | Recreativo do Libolo | 1º de Agosto |
| 2013 | Kabuscorp | 1º de Agosto |
| 2014 | Recreativo do Libolo | Kabuscorp |
| 2015 | Recreativo do Libolo | 1º de Agosto |
| 2016 | 1º de Agosto | Petro de Luanda |
| 2017 | 1º de Agosto | Petro de Luanda |
| 2018 | 1º de Agosto | Petro de Luanda |
| 2018/19 | 1º de Agosto | Petro de Luanda |
| 2019/20 | — | — |
| 2020/21 | Sagrada Esperança | Petro de Luanda |
| 2021/22 | Petro de Luanda | 1º de Agosto |
| 2022/23 | Petro de Luanda | 1º de Agosto |
| 2023/24 | Petro de Luanda | Sagrada Esperança |
| 2024/25 | Petro de Luanda | Wiliete |
| 2025/26 | Petro de Luanda | Wiliete |

**Rebaixados marcados na classificação:** 132 em 45 edições (só onde a tabela publicada marca a queda); quem mais caiu: 1º de Maio (7), Progresso do Sambizanga (6), Sporting de Cabinda (6), FC Cabinda (5), Académica do Lobito (5).

**Ajustes de pontos** (pontos publicados menos os da conta V/E/D: punições, bônus de fase anterior, pontos de pênaltis):

- 1998: Chicoil +3
- 2018: Kabuscorp -12
- 2018: Progresso do Sambizanga -6
- 2018/19: 1º de Agosto -3
- 2018/19: Desportivo da Huíla -3
- 2018/19: Bravos do Maqui -3
- 2021/22: Kabuscorp -9

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/ang-1/explicacoes.py`; cada uma também aparece no relatório, na edição.

### Jogos lidos e corrigidos (placar dado, descartados, anulados, não jogados) (`CORRIGE`, 1)

- **1999 · ango99:235:** [descartado] a linha repete o Sporting de Cabinda 2-1 Sagrada Esperança da linha 232 (colada na continuação da nota do jogo de cima)

### Tabelas da página que não são da edição (`TABELAS_FORA`, 17)

- **1998 · ango98:122:** tabela do meio da temporada (a final vem depois)
- **1998 · ango98:196:** tabela do meio da temporada (a final vem depois)
- **1998 · ango98:266:** tabela do meio da temporada (a final vem depois)
- **1998 · ango98:388:** tabela do meio da temporada (a final vem depois)
- **1998 · ango98:392:** tabela do meio da temporada (a final vem depois)
- **1998 · ango98:395:** tabela do meio da temporada (a final vem depois)
- **1998 · ango98:399:** tabela do meio da temporada (a final vem depois)
- **1998 · ango98:403:** tabela do meio da temporada (a final vem depois)
- **2018 · ango2018:64:** linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- **2018 · ango2018:318:** linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- **2018 · ango2018:547:** linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- **2019/20 · ango2020:69:** linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- **2019/20 · ango2020:319:** linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- **2019/20 · ango2020:476:** linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- **2022/23 · ango2023:68:** linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- **2022/23 · ango2023:318:** linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)
- **2022/23 · ango2023:530:** linha da campanha anulada de um clube que desistiu ou foi excluído (não conta na classificação)

### Identidade dos clubes

Regras em `coleta/ang-1/clubes_ang.py` (docstring abaixo; os nomes de cada fonte estão na coluna `nomes_fonte` do clubes.csv).

```
Identidade dos clubes angolanos: cada grafia de cada fonte (RSSSF, ogol, Wikipédia) -> um nome de exibição.

- nome pelo qual o clube é conhecido no Brasil, como na memória dos lusófonos: "1º de Agosto", "Petro de Luanda",
  "Benfica de Luanda", "1º de Maio";
- nome que já existe em outro país leva primeiro a cidade ("Benfica de Luanda", "Santos de Luanda") e, sem cidade que
  resolva, o país entre parênteses;
- clubes com data no nome: o leitor troca o número pelo extenso ("Primeiro de Agosto"); a regra casa o extenso e a
  exibição volta ao número ("1º de Agosto", "4 de Abril");
- o mesmo clube com outro nome, na mesma cidade, é um só, com o nome atual; os nomes antigos ficam no nomes_fonte:
  - Petro de Luanda = Atlético Petróleos de Luanda; Petro do Huambo = Atlético Petróleos do Huambo;
  - ASA de Luanda = Atlético Sport Aviação ("ASA" já é o de Arapiraca, do Brasil); Interclube = GD Interclube = Inter Clube Angola;
  - 1º de Maio = Estrela Clube Primeiro de Maio (Benguela); Desportivo da Huíla = Desportivo Militar da Huíla;
  - Atlético do Namibe = Atlético Petróleos do Namibe = Desportivo Sonangol do Namibe (o clube da petrolífera no
    Namibe, rebatizado);
  - Bravos do Maqui = Onze Bravos do Maqui (Luena); Recreativo do Libolo = GD e Recreativo do Libolo (Calulo);
  - Académica do Lobito = Académica Petróleos do Lobito; Académica do Soyo = Académica Petróleos do Kwanda;
  - Sporting de Cabinda = Sporting Clube Petróleos de Cabinda; Kabuscorp = Kabuscorp do Palanca;
  - JGM = JGM/Académica do Huambo; Saneamentos Rangol = Rangol;
  - Santa Rita do Namibe = GD Welwitschia (Moçâmedes; "Born as Santa Rita, later renamed Grupo Desportivo Welwitschia
    and later renamed again Santa Rita", 1979); o Santa Rita de Cássia (Uíge, 2017 em diante) é outro clube;
- "Progresso" sozinho é o do Sambizanga (Luanda), menos onde a tabela diz o da Lunda Sul (2015 a 2017, os dois na
  liga: regra pelo nome completo).

REGRAS: (regex sobre a chave do nome, nome de exibição, primeiro ano, último ano), a primeira que casa vale. O ano é o
ano_inicio da temporada.
```

## 8. O que não deu para coletar

- **Fora do pacote:** o Campeonato Provincial da era colonial (1941 a 1974; 1975 abandonado), que a federação não conta; a Taça e a Supertaça; as divisões de baixo.
- **Edições sem jogos** (17): 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997.
- **Décadas com menos da metade dos gols com autor:** 1970s, 1980s, 1990s, 2000s, 2010s, 2020s.
- **Décadas sem cartões** (a ESPN só cobre do meio dos anos 2000 em diante): 1970s, 1980s, 1990s, 2000s, 2010s, 2020s.
- Árbitro e estatísticas de jogo: nenhuma fonte em lote.

## 9. Pendências e próximos passos

- 1981 a 1997: só a tabela final (a RSSSF não tem os jogos); 1998: parte dos jogos. O ogol só tem jogos de 1999 em diante. Fonte que resolveria: o Jornal de Angola ou o arquivo da FAF.
- 1980, 2000 e 2007: um placar diferente da tabela em dois clubes, sem terceira fonte (o provável jogo está no relatório).
- 2009: o desempate do rebaixamento com a 2ª divisão ficou fora da edição; os rebaixados (1º de Maio e Académica do Lobito) foram marcados à mão.
- Autores dos gols só em poucos anos (2001, 2005 e alguns jogos de outros); artilheiros e cartões, nenhum. Fonte que resolveria: o ogol jogo a jogo (1999 em diante).
- Wikipédia (terceira fonte) não baixada: a API recusou por excesso de pedidos em 25/11/2026. Rodar `coleta/ang-1/baixar_wikipedia.py` de novo e reimportar.
- Identidade a conferir: Atlético do Namibe = Desportivo Sonangol do Namibe = Atlético Petróleos do Namibe; Santa Rita do Namibe = GD Welwitschia; "Progresso" sozinho como o do Sambizanga; Bravos do Maqui = Onze Bravos.

## 10. Arquivos e comandos

Código em `coleta/ang-1/`:

| Arquivo | O que faz |
|---|---|
| `autores.py` | Autores dos gols como a RSSSF escreve -> lista de gols por lado. |
| `baixar_ogol.py` | Baixa o calendário de cada edição da 1ª divisão angolana no ogol para data/coleta/ang-1/ogol/<id>.json. |
| `baixar_rsssf.py` | Baixa as páginas da RSSSF da 1ª divisão angolana (Girabola) para data/coleta/ang-1/rsssf/: a lista de campeões |
| `baixar_wikipedia.py` | Baixa da Wikipédia em inglês (wikitexto, pela API) o artigo da liga ("Girabola") e o de cada temporada ("2015 |
| `clubes_ang.py` | Identidade dos clubes angolanos: cada grafia de cada fonte (RSSSF, ogol, Wikipédia) -> um nome de exibição. |
| `conferir.py` | Conferência de cada edição: nomes reconhecidos e soma dos jogos x tabelas publicadas pela RSSSF. |
| `edicoes.py` | Edições da 1ª divisão angolana (ang-1): o Girabola, de 1979 a 2025/26. |
| `explicacoes.py` | Correções e explicações da coleta da 1ª divisão angolana, edição a edição (entram no relatório). |
| `importar.py` | Junta as fontes da 1ª divisão angolana e grava o pacote em data/coleta/ang-1/pacote/ e o relatório em docs/coleta/ang-1.md. |
| `ler_rsssf.py` | Lê os jogos de cada edição: trechos das páginas da RSSSF (data/coleta/ang-1/rsssf/) com o leitor comum (rsssf_africa), |
| `outras_fontes.py` | Casa os jogos da RSSSF com o ogol (copiado de coleta/chi-1/outras_fontes.py, sem a ESPN, que não tem a liga egípcia). |
| `ver.py` | Ajuda da conferência: mostra os jogos entre dois clubes numa edição, com a linha da página e o texto em volta. |
| `wiki_tabelas.py` | Tabelas finais dos artigos de temporada da Wikipédia em inglês (data/coleta/ang-1/wikipedia/en_<temporada>.txt). A lista de campeões e a de artilheiros ficam vazias: o artigo da |

- Fontes baixadas: `data/coleta/ang-1/` (uma pasta por fonte: `rsssf/`, `espn/`, `ogol/`, `wikipedia/`); cache da ESPN em `data/cache/espn-africa/`, do ogol em `data/cache/ogol-ang-1/`.
- Pacote: `data/coleta/ang-1/pacote/`; relatório: `docs/coleta/ang-1.md`.
- Refazer do zero (da raiz do clube_analitico, logs no scratchpad):

```
python coleta/ang-1/baixar_ogol.py
python coleta/ang-1/baixar_rsssf.py
python coleta/ang-1/baixar_wikipedia.py
python coleta/ang-1/importar.py
python coleta/ang-1/conferir.py [-v temporada]   # divergências
python coleta/comum-africa/testar_carga.py ang-1 <scratchpad>
python coleta/comum-africa/documentar.py
```

