# Revisão: Campeonato Francês (`fra-1`)

Data: 22/11/2026 (3ª rodada, revisão profunda). Revisor: subagente FR. Achados com prefixo `FR`.

**Resumo.** O pacote é bom nos jogos: de 1948/49 em diante, 27.900 placares batem com o transfermarkt, e 29.087 placares de
todas as épocas batem com a grade da Wikipédia fr, com poucas exceções explicadas. Os erros graves estão nas regras e nos
casos especiais:
- 14 rebaixamentos falsos (1932/33-1938/39 e 1966/67);
- o bônus de 1974/75-1975/76 com a regra errada, que cria 39 punições falsas;
- dois jogos decididos no tribunal tratados como empate (1951/52 e 1955/56);
- 1946/47 com 9 placares trocados pelos do ogol.

**Nada disto está no ar.** O `fra-1` está no banco local, igual ao pacote, mas não há `painel/dados/fra-1.js` e o site não
mostra o Francês.

## Pacote x banco x painel

- **Banco local:** `db/futebol.db` tem o `fra-1` com 88 edições e 30.466 jogos. Jogo a jogo (data, clubes e placar), o pacote e o
  banco são iguais; a classificação final também (posição, pontos e situação). Prova: `revisao/FR/pacote_x_banco.py`.
- **Painel e site:** `painel/dados/fra-1.js` não existe, e `https://clubeanalitico.pages.dev/dados/fra-1.js` devolve a página
  inicial. O bloco F não se aplica.
- **Ficha (seção 1):** os números conferem com o pacote: 88 edições, 30.466 jogos, 22.613 gols com autor, 35.434 cartões e 76
  clubes.

## A. Edições e títulos

- **Lista de edições:** 88 edições (1932/33-2025/26), sem 1939/40-1944/45. É a mesma lista da Wikipédia fr, onde os
  campeonatos de guerra não são oficiais.
- **Nomes e regras de época:** confere o nome de época (Division 1 até 2001/02, Ligue 1 depois). Também conferem os pontos por
  vitória:
  - 2 pontos até 1993/94;
  - 3 pontos em 1988/89 ("victoire à 3 points, qui fait l'objet d'un test");
  - 3 pontos de 1994/95 em diante.
- **Campeões:** os 87 campeões conferem com a Wikipédia fr ("Palmarès" e tabela de cada temporada). 1992/93 fica sem campeão:
  o título foi tirado do Marseille e o PSG o recusou.
- **Vice e 3º:** conferem pelas tabelas, mas o 3º de 1932/33 é o Antibes, excluído da final por suborno, e não existe 3º
  oficial (**FR-020**).
- **Fontes:** https://fr.wikipedia.org/wiki/Palmarès_du_championnat_de_France_de_football e a página
  `https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_<aaaa>-<aaaa>` de cada temporada.

## B. Classificação final, rebaixados e punições

**Tabelas.** Comparei as 87 tabelas da Wikipédia fr (1.666 linhas) com a classificação do pacote. A coleta usou a Wikipédia en
e a RSSSF; a fr não. Script: `revisao/FR/comparar_frwiki.py`. 28 linhas divergem, todas explicadas:
- **1946/47 (FR-005, alta):** 10 linhas.
  - O `reparar` descartou 9 jogos da base e ficou com o placar do ogol.
  - A grade da Wikipédia fr traz os 9 placares da base. Com eles, a tabela da Wikipédia en fecha em 18 clubes.
  - OM e Bordeaux só fecham se OM 0-0 Bordeaux (27/10/1946) foi vitória do OM no tribunal.
  - Hoje o Bordeaux tem 33 pontos e está em 18º, abaixo do Lens com 31.
- **1951/52 (FR-003, alta):** OM x Racing foi "gagné 0-0 sur tapis vert par le RC Paris" (invasão de campo aos 88 min). O OM é
  16º com 27 pontos e jogou o barrage, não 15º com 28.
- **1955/56 (FR-004, alta):** Nancy x OM foi "gagné sur tapis vert par l'OM" (invasão aos 87 min). O OM é 5º com 40 pontos, e
  o Nancy, 12º com 32.
- **Tabela "errada" da Wikipédia:** a coleta marcou a tabela da Wikipédia como errada (WIKI_ERRA) nas três temporadas acima.
  Nas três, a Wikipédia estava certa.
- **1992/93 (FR-006):** a FFF declarou o VA-OM "perdant pour les deux équipes" (0-0; em campo, 0-1). O pacote tem empate e
  -1 ponto de punição para cada um: os pontos batem, mas V-E-D não. Ficam OM 22-9-7 e Valenciennes 9-11-18.
- **1958/59 (FR-008):** a CORRECOES (2-1) muda os gols de Sochaux e Rennes. Base, ogol, transfermarkt e Wikipédia fr dão 4-3.
- **1953/54 (FR-018):** Metz e Nancy estão trocados (12º e 13º). Pela média de gols, que era o critério da época segundo a
  Wikipédia fr, o Nancy fica à frente.
- **2008/09 (FR-010):** a punição de -1 ponto do Le Havre só existe na tabela da RSSSF. As Wikipédias fr e en dão 26 pontos.
- **1937/38 (FR-017, dúvida):** Excelsior x Valenciennes. As tabelas das Wikipédias fr e en contra a RSSSF e o ogol.
- **Sem erro:** 2 linhas com falha de leitura (pontos vazios em 2012/13 Ajaccio e 2019/20 PSG).
- **Confirmações (FR-023):** 1945/46 (Red Star 1-1 Cannes) confere com a Wikipédia fr.

**Bônus de 1973/74-1975/76 (FR-002, alta).** A regra mudou depois do primeiro ano:
- **1973/74:** ponto extra para quem marca 3 gols ou mais. A Wikipédia fr confirma, e o pacote está certo.
- **1974/75 e 1975/76:** ponto extra só por vitória com 3 gols ou mais de diferença. Conferi as 40 linhas: o bônus da Wikipédia fr
  é exatamente esse.
- **Efeito no pacote:** ele usa a regra de 1973/74 nos três anos e fecha a diferença com 39 punições falsas (Monaco -11, OM -9...).
- **Classificação por rodada:** fica errada nesses dois anos, com pontos negativos já na 1ª rodada.
- Prova: `revisao/FR/bonus.py`.

**Rebaixados (FR-001, alta).** Conferi as 88 temporadas contra a cor das tabelas e o infobox "relégué fin" da Wikipédia fr.
**14 marcas "rebaixado" estão erradas:**

| Temporada | Clubes marcados por engano |
|---|---|
| 1932/33 | CA Paris, Excelsior Roubaix, SC Nîmes, SO Montpellier |
| 1933/34 | Excelsior, SC Nîmes, SO Montpellier |
| 1934/35, 1935/36 e 1936/37 | Excelsior |
| 1938/39 | Excelsior, Fives, Olympique Lillois (fusões da guerra) |
| 1966/67 | Toulouse (fusão com o Red Star) |

- **Causa:** nas temporadas seguintes montadas pelo ogol, o código não casa o clube. Está no `importar.py`, linhas 831-843.
- **Barrages:** todos os perdedores estão certos. São 22 casos, entre eles:
  - 1952/53 Rennes e 1953/54 Stade Français;
  - 1955/56 Lille e 1956/57 Rennes;
  - 1963/64 Racing, 1968/69 Monaco e 1978/79 Paris FC;
  - de 1981/82 a 1991/92: Valenciennes, Tours, Saint-Étienne, Rouen, Sochaux, Niort, Strasbourg e Rennes;
  - 2016/17 Lorient, 2021/22 Saint-Étienne, 2023/24 Metz e 2024/25 Reims.
- **Rebaixamentos administrativos:** também estão certos:
  - 1990/91 Bordeaux, Brest e Nice;
  - 1993/94 OM;
  - 2000/01 Toulouse;
  - 2016/17 Bastia.
- **Falta explicação nesses administrativos (FR-015).**

**Textos (FR-014, baixa):**
- 16 observações da classificação estão em inglês, copiadas da Wikipédia en.
- 6 observações são só um código: "OL", "EAR", "OM", "NIC", "BOR", "MET".

**Número de clubes:** confere nas 87 tabelas: 14/16/18/20 clubes, conforme a ficha.

## C. Jogos

- **Total por temporada:** turno e returno completo em todas. As exceções são 1932/33 (181 jogos: 2 grupos de 10 e a final) e
  2019/20 (279 jogos, covid; a ordem é pela média de pontos por jogo, confere).
- **Placares contra a grade da Wikipédia fr:** 29.087 jogos (95%), em todas as décadas. Script:
  `revisao/FR/comparar_frwiki.py`. 61 diferenças:

  | Década | Jogos | Diferenças | O que são |
  |---|---|---|---|
  | 1930s | 1.562 | 4 | FR-017 |
  | 1940s | 1.298 | 13 | 1946/47 (FR-005); 1947/48 (FR-007); 1945/46 (FR-017) |
  | 1950s | 2.901 | 3 | 1958/59 (FR-008); 1950/51 (FR-017) |
  | 1960s | 3.124 | 0 | |
  | 1970s | 3.800 | 0 | |
  | 1980s | 3.800 | 0 | |
  | 1990s | 3.578 | 0 | |
  | 2000s | 3.651 | 0 | |
  | 2010s | 3.315 | 41 | linhas desalinhadas na grade fr (Lyon 2012/13, Nantes 2013/14, Bastia 2016/17) e 4 erros da Wikipédia fr |
  | 2020s | 2.058 | 0 | |

  Nos 41 casos dos anos 2010, o transfermarkt confirma o pacote.
- **Placares e datas contra o transfermarkt:** uma página por temporada (`revisao/FR/comparar_tm.py`).
  - **Placares de 1948/49 em diante:** cerca de 27.900 jogos, 17 diferenças:
    - 1951/52 e 1955/56: FR-003 e FR-004;
    - 1958/59: FR-008;
    - 3 W.O. que o transfermarkt mostra como 0-3;
    - os demais são erros do transfermarkt (a Wikipédia fr confirma o pacote).
  - **Antes de 1948/49:** o transfermarkt não serve (grupos misturados, datas e placares errados).
- **Datas (FR-009, `revisao/FR/datas_tm_ogol.py`):** em 140 jogos, o transfermarkt e o ogol concordam entre si e o pacote (data do
  engsoccerdata) difere.
  - **41 com 3 dias ou mais:**
    - 1969/70 Angers x Saint-Étienne com 160 dias de diferença;
    - 1970/71: 9 jogos com um mês a mais;
    - 1988/89: 10 jogos com dois meses a menos.
  - **99 com 1-2 dias:** quase todos em 1996/97 e 1997/98.
  - Lista em `revisao/FR/datas_tm_ogol_lista.txt`.
- **Mando trocado na base (FR-007):** 1947/48 Racing x Stade Français. O ogol, a RSSSF e a Wikipédia fr concordam entre si.
- **Fontes divididas (FR-017, dúvida):** 1935/36 OM x Valenciennes, 1937/38 Excelsior x Valenciennes, 1945/46 Bordeaux x Sète e
  1950/51 Lille x Toulouse.
- **Jogos decididos no tribunal:**
  - os 6 que estão no pacote estão certos (FR-025);
  - faltam 3: 1951/52 e 1955/56, e provavelmente 1946/47 (FR-003, FR-004 e FR-005);
  - o VA-OM de 1992/93 está tratado errado (FR-006);
  - a observação "o placar de campo fica" está errada em 3 jogos (FR-016).
- **Diferenças da RSSSF:** em 1963/64, 1968/69, 1971/72, 1977/78, 1978/79 e 1991/92, a base está certa e a RSSSF errada
  (FR-024).
- **Varredura** (`revisao/FR/varredura_pacote.py`, adaptada para ler o pacote):
  - nenhum clube contra ele mesmo e nenhum jogo repetido;
  - nenhuma data fora da temporada;
  - 20 casos de clube com 2 jogos no mesmo dia: anos 1930, 1962/63, 1969/70, 1970/71, 1977/78 e 1988/89. Quase todos são os
    dias errados de FR-009 (1969/70, 1970/71, 1977/78 e 1988/89) ou as datas provisórias do ogol (anos 1930); 1962/63 (Nancy,
    30/03/1963) fica para conferir.

## D. Gols e artilheiros

- **Artilheiros:** comparei os 88 com a lista da Wikipédia fr, que cita a ligue1.fr (`revisao/FR/artilheiros.py`). 76 iguais e
  12 diferentes:
  - **3 de número (FR-011):** falta Onnis (21) em 1979/80; falta Garande (21) em 1983/84; Bokšić tem 23 em 1992/93, não 22;
  - **9 de grafia (FR-019):** Cisowski com dois nomes, "Touré Sékou", "Abbeglen"...
- **Gols com autor:** a soma por jogo nunca passa do placar (22.613 gols, 0 casos).

## E. Clubes

- **Nomes:** os 76 nomes são únicos no banco e nos pacotes. A cidade e o país estão certos (o Monaco é `MON`).
- **Identidade:**
  - **FR-012 (decisão):** o Toulouse FC de 1937-1967, que se fundiu ao Red Star, está junto do Toulouse FC de 1970.
  - **FR-013 (decisão):** o Lyon OU de 1945/46 está contado como o Lyon. O SO Montpellier está separado do Montpellier HSC, que a
    Wikipédia fr liga ao SOM.
  - **Sem problema:** RC Paris-Sedan conta como Sedan; Stade Français-Red Star (1948-50) conta como Stade Français; os três
    Troyes estão separados (Troyes-Savinienne, Troyes AF e ESTAC).
- **Exibição (FR-021):** "Evian" sem acento.
- **Escudos:** ainda não há escudo de clube francês no painel, que não tem o Francês. Fica para o banco e painel, sem achado.

## F. Painel

Não se aplica: o Francês não está no painel nem no site.

## Seções 8 e 9 da ficha (o que não deu e pendências)

| Falta | Caminho proposto | Custo | Risco |
|---|---|---|---|
| Autores dos gols e cartões antes de 2001/02; árbitro em todas as épocas (hoje 0%); público e estádio antes de 2001/02 | Ficha de jogo do transfermarkt (`/index/spielbericht/<id>`; o id está no calendário já baixado). Testei 1977/78 Bastia 0-2 Monaco: árbitro Vautrot, público 5.850, gols de Onnis, cartão | ~27 mil páginas jogo a jogo (~16 h a 1 pedido/2 s), em lotes | Conferir a soma dos gols com o placar, como na ESPN |
| Datas de 356 jogos dos anos 1930 e rodada de 224 | footballdatabase.eu (páginas por rodada, com data) ou jornais da Gallica (L'Auto) | ~180 páginas no footballdatabase.eu. O limite é de 50 páginas por dia, por IP, sem conta (compartilhado com os outros revisores), o que dá 4 dias ou uma conta grátis. A Gallica sai jogo a jogo, à mão | Baixo |
| Barrages | Wikipédia fr (seção "Barrages" de cada temporada) | Baixo | Entram melhor com a 2ª divisão |

## Perguntas ao Guilherme

1. **FR-D1 (FR-012):** separar o Toulouse FC de 1937-1967 (fundido ao Red Star em 1967) do Toulouse FC de 1970? Recomendo
   separar.
2. **FR-D2 (FR-013):** o Lyon OU (1945/46) continua junto do Lyon (Olympique Lyonnais) e o SO Montpellier separado do Montpellier
   HSC? Recomendo manter como está.
3. **FR-D3 (FR-001):** em 1938/39 as quedas "não foram levadas em conta" por causa da guerra. O Antibes (15º) e o RC Roubaix
   (16º, que depois virou CORT) ficam como rebaixados? Recomendo o Antibes rebaixado e o RC Roubaix como fusão.
4. **FR-D4 (FR-011):** Bokšić em 1992/93: 23 gols (LFP, contando o jogo anulado) ou 22 (RSSSF)? Recomendo 23, pela contagem
   oficial, como no ES-005.

## Arquivos

- **Achados:** `SCRATCH/achados_FR.csv` (25 linhas), gerado por `revisao/FR/gravar_achados.py`.
- **Fontes, decisões e plano:** `SCRATCH/fontes_FR.md`, `SCRATCH/decisoes_FR.md`, `SCRATCH/plano_FR.md`.
- **Scripts em `revisao/FR/`:**
  - `bonus.py`, `varredura_pacote.py`, `pacote_x_banco.py`, `nomes_unicos.py`;
  - `frwiki.py` e `comparar_frwiki.py`, `comparar_tm.py`, `datas_tm_ogol.py`, `artilheiros.py`, `teste_1946.py`;
  - `baixar.py`, `baixar_frwiki.py`, `baixar_tm.py`, `fdb.py`.
- **Cache:** `data/cache/revisao/FR/`. As saídas ficam em `SCRATCH/FR/`.
