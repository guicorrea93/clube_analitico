# Campeonato Holandês (`ned-1`) — documentação

Gerado por `python coleta/comum-europa/documentar.py` a partir do pacote `data/coleta/ned-1/pacote/` e do importador `coleta/ned-1/importar.py`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/ned-1.md`.

## 1. O que temos

- **Edições:** 138, de 1888/89 a 2025/26.
- **Jogos:** 21878; **gols:** 68087; **gols com autor:** 23019 (34%); **cartões:** 24431; **jogos com estatísticas** (chutes, faltas, escanteios): 2680.
- **Clubes:** 93; **artilheiros:** 70 temporadas com artilheiro (78 linhas, com empates).
- **Classificação final:** 135 temporadas; **rodada a rodada:** 70 temporadas.
- **Tabelas publicadas guardadas para conferência:** 2791 linhas, de 205 tabelas.
- **Observação da competição:** Campeonato holandês desde 1888/89: até 1955/56, ligas regionais e fase final entre os campeões regionais (no pacote, a fase final e o campeão oficial); desde 1956/57, a Eredivisie. Não inclui os play-offs de vaga europeia e de rebaixamento (nacompetitie). 2019/20 foi cancelada pela covid-19, sem campeão.

## 2. Fontes e regras

**Fontes:**

- engsoccerdata (GitHub jalapic/engsoccerdata, licença GPL >= 2): base dos jogos, 1956/57-2024/25;
- football-data.co.uk: de 1993/94 em diante confere o placar; hora (2019/20+), árbitro e estatísticas por time;
- ogol: rodada oficial de cada jogo e conferência de placar (só os jogos de rodada: os play-offs da mesma edição ficam de fora); base de 2025/26, que o engsoccerdata não traz; calendários guardados em `data/cache/ogol-ned-1/` para os escudos (com 2026/27, baixado só para saber quem caiu em 2025/26);
- ESPN (liga `ned.1`, 2001/02+): hora, estádio, público, gols e cartões com minuto e jogador;
- RSSSF: matriz de resultados e tabela final de 1956/57 a 2003/04 (conferência jogo a jogo), tabela final das temporadas seguintes, lista de campeões e de artilheiros (com o clube);
- Wikipédia (en): tabela final de cada temporada (ordem oficial e punições).

**Regras da importação:** o placar é o da base; cada tabela publicada é comparada com a tabela calculada dos jogos (jogos, V, E, D, gols pró e contra, pontos com a punição). A ordem da classificação final é a oficial (Wikipédia). Gols da ESPN só entram quando a soma bate com o placar. Hora local (Amsterdã). Rebaixado = clube que não está na 1ª divisão na temporada seguinte (inclui quem caiu na nacompetitie). 2 pontos por vitória até 1994/95, 3 a partir de 1995/96. Placar diferente no ogol, no football-data ou na ESPN numa temporada em que as tabelas publicadas fecham com a base é erro da outra fonte e fica só anotado; quando a outra fonte e a tabela publicada concordam contra a base, o placar é corrigido (CORRECOES, TRIBUNAL e INVERTIDOS em `importar.py`, com o motivo).

**Desempate:** para cada temporada, o critério calculado que reproduz a ordem oficial (confronto direto em 18, saldo de gols em 52, média de gols em 0); é ele que ordena a classificação rodada a rodada.

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF, Wikipédia): 191 tabelas fecham com os jogos e 3 divergem (divergência sempre explicada no relatório).
- Temporadas em que nenhuma tabela publicada fecha: 1888/89, 1889/90, 1890/91, 1891/92, 1892/93, 1893/94, 1894/95, 1895/96, 1896/97, 1897/98, 1898/99, 1899/00, 1906/07, 1914/15, 1922/23, 1923/24.
- Temporadas com alguma tabela divergente: 1906/07, 1922/23, 1923/24.
- Temporadas com número de jogos diferente do turno e returno completo: 2019/20 (232 de 306).

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | público | árbitro | estatísticas | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1900s | 28 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1910s | 82 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1920s | 176 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1930s | 200 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1940s | 230 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1950s | 1304 | 96% | 0% | 94% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1960s | 2796 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1970s | 3060 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1980s | 3060 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 1990s | 3060 | 100% | 0% | 100% | 0% | 0% | 0% | 0% | 0% | 0.0 |
| 2000s | 3060 | 100% | 90% | 100% | 90% | 85% | 0% | 0% | 89% | 2.8 |
| 2010s | 2986 | 100% | 100% | 100% | 100% | 100% | 0% | 28% | 99% | 3.4 |
| 2020s | 1836 | 100% | 100% | 100% | 100% | 81% | 0% | 100% | 100% | 3.1 |

## 5. Formato do campeonato ao longo do tempo

**Número de clubes:**

- 1956/57 a 1961/62: 18 clubes
- 1962/63 a 1965/66: 16 clubes
- 1966/67 a 2025/26: 18 clubes
- 1888/89 a 1889/90: 0 clubes
- 1890/91 a 1891/92: 5 clubes
- 1892/93: 4 clubes
- 1893/94 a 1894/95: 6 clubes
- 1895/96 a 1899/00: 7 clubes
- 1900/01 a 1901/02: 2 clubes
- 1902/03 a 1903/04: 3 clubes
- 1904/05 a 1912/13: 2 clubes
- 1913/14: 3 clubes
- 1914/15: 2 clubes
- 1915/16: 3 clubes
- 1916/17: 4 clubes
- 1917/18 a 1918/19: 5 clubes
- 1919/20 a 1922/23: 4 clubes
- 1923/24 a 1943/44: 5 clubes
- 1944/45:  clubes
- 1945/46 a 1949/50: 6 clubes
- 1950/51: 5 clubes
- 1951/52 a 1955/56: 4 clubes

**Pontos por vitória:**

- 1956/57 a 1994/95: 2
- 1995/96 a 2025/26: 3
- 1888/89 a 1955/56: 2

**Nome oficial:**

- 1956/57 a 2025/26: Eredivisie
- 1888/89 a 1955/56: Campeonato Holandês

**Temporadas com mais de uma fase ou fora dos pontos corridos:**

- nenhuma

**Critério de desempate** (o que reproduz a ordem oficial em cada temporada):

- pontos (desempate em jogo extra): 67 temporadas
- pontos, saldo de gols, gols pró: 52 temporadas
- pontos, confronto direto, saldo de gols, gols pró: 18 temporadas

**Observações das edições** (formato, punições, casos especiais):

- 2010/11: punições: NAC Breda -1 pontos
- 2014/15: punições: Twente -6 pontos
- 2015/16: punições: Twente -3 pontos
- 2019/20: título não atribuído; temporada cancelada em abril de 2020 pela pandemia de covid-19, depois de 25 ou 26 rodadas (232 de 306 jogos): sem campeão, sem rebaixamento e sem acesso; a classificação é a do momento da parada
- 2023/24: punições: Vitesse -18 pontos
- 1892/93: sem campeão declarado
- 1896/97: sem campeão declarado
- 1900/01: campeões regionais: HVV; Victoria (Wageningen)
- 1901/02: campeões regionais: HVV; Victoria (Wageningen)
- 1902/03: campeões regionais: HVV and Volharding (Amsterdam); Vitesse
- 1903/04: campeões regionais: HBS and Velocitas (Breda); PW
- 1904/05: campeões regionais: HVV; PW
- 1905/06: campeões regionais: HBS; PW
- 1906/07: campeões regionais: HVV; PW
- 1907/08: campeões regionais: Quick (Den Haag); UD
- 1908/09: campeões regionais: Sparta; Wilhelmina
- 1909/10: campeões regionais: HVV; Quick (Nĳmegen)
- 1910/11: campeões regionais: Sparta; GVC
- 1911/12: campeões regionais: Sparta; GVC
- 1912/13: campeões regionais: Sparta; Vitesse
- 1913/14: campeões regionais: HVV; Vitesse; Willem II
- 1914/15: edição não oficial na época (Primeira Guerra Mundial); contada hoje entre os títulos; campeões regionais: Sparta; Vitesse
- 1915/16: campeões regionais: Sparta; Go Ahead; Willem II
- 1916/17: campeões regionais: UVV; Go Ahead; Willem II; Be Quick (Groningen)
- 1917/18: campeões regionais: Ajax, AFC; Go Ahead; Willem II; Be Quick (Groningen)
- 1918/19: campeões regionais: Ajax, AFC; Go Ahead; NAC; Be Quick (Groningen)
- 1919/20: campeões regionais: VOC; Go Ahead; MVV; Be Quick (Groningen)
- 1920/21: campeões regionais: Ajax; Go Ahead; NAC; Be Quick (Groningen)
- 1921/22: campeões regionais: Blauw-Wit; Go Ahead; NAC; Be Quick (Groningen)
- 1922/23: campeões regionais: RCH; Go Ahead; Willem II; Be Quick (Groningen)
- 1923/24: campeões regionais: Feyenoord (West I), Stormvogels (West II); SC Enschede; NAC; Be Quick (Groningen)
- 1924/25: campeões regionais: Sparta (West I), HBS (West II); Go Ahead; NAC; Frisia
- 1925/26: campeões regionais: Stormvogels (West I), Feyenoord (West II); SC Enschede; MVV; Be Quick (Groningen)
- 1926/27: campeões regionais: Ajax (West I), Feyenoord (West II); Heracles; NAC; Velocitas
- 1927/28: campeões regionais: Ajax (West I), Feyenoord (West II); ZAC; NOAD; Velocitas
- 1928/29: campeões regionais: Sparta (West I), Feyenoord (West II); Go Ahead; PSV; Velocitas
- 1929/30: campeões regionais: Ajax (West I), Blauw-Wit (West II); Go Ahead; Willem II; Velocitas
- 1930/31: campeões regionais: Ajax (West I), Feyenoord (West II); Go Ahead; PSV; Velocitas
- 1931/32: campeões regionais: Ajax (West I), Feyenoord (West II); SC Enschede ; PSV; Veendam
- 1932/33: campeões regionais: Feyenoord (West I), Stormvogels (West II); Go Ahead; PSV; Velocitas
- 1933/34: campeões regionais: Ajax (West I), KFC (West II); Heracles; Willem II; Velocitas
- 1934/35: campeões regionais: Ajax (West I), DWS (West II); Go Ahead; PSV; Velocitas
- 1935/36: campeões regionais: Ajax (West I), Feyenoord (West II); SC Enschede; NAC; Be Quick (Groningen)
- 1936/37: campeões regionais: Ajax (West I), Feyenoord (West II); Go Ahead; PSV; Be Quick (Groningen)
- 1937/38: campeões regionais: DWS (West I), Feyenoord (West II); Heracles; PSV; Be Quick (Groningen)
- 1938/39: campeões regionais: DWS (West I), Ajax (West II); NEC; Eindhoven; Achilles (Assen)
- 1939/40: campeonato de emergência (Segunda Guerra Mundial); contado hoje entre os títulos; campeões regionais: Blauw-Wit (West I), Feyenoord (West II); Heracles; Juliana; GVAV
- 1940/41: campeões regionais: ADO (West I), VSV (West II); Heracles; PSV; Be Quick (Groningen)
- 1941/42: campeões regionais: ADO (West I), Blauw-Wit (West II); AGOVV; Eindhoven; Heerenveen
- 1942/43: campeões regionais: ADO (West I), Feyenoord (West II); SC Enschede; Willem II; Heerenveen
- 1943/44: campeões regionais: De Volewĳckers (West I), VUC (West II); Heracles; LONGA; Heerenveen
- 1944/45: sem campeonato (Segunda Guerra Mundial)
- 1945/46: campeões regionais: Ajax (West I), Haarlem (West II); NEC; NAC (Zuid I), Limburgia (Zuid II); Heerenveen
- 1946/47: campeões regionais: Ajax (West I), Blauw-Wit (West II); NEC; BVV (Zuid I), MVV (Zuid II); Heerenveen
- 1947/48: campeões regionais: Haarlem (West I), EDO (West II); Go Ahead; BVV (Zuid I), PSV (Zuid II); Heerenveen
- 1948/49: campeões regionais: SVV (West I), VSV (West II); AGOVV; BVV (Zuid I), NOAD (Zuid II); Heerenveen
- 1949/50: campeões regionais: Blauw-Wit (West I), Ajax (West II); Enschedese Boys; Limburgia (Zuid I), Maurits (Zuid II); Heerenveen
- 1950/51: campeões regionais: Heerenveen; DWS; Blauw-Wit ; Willem II; PSV
- 1951/52: campeões regionais: Haarlem; Ajax; Willem II; Hermes DVS
- 1952/53: campeões regionais: RCH; Vitesse; Sparta; Eindhoven
- 1953/54: campeões regionais: DWS; DOS; PSV; Eindhoven

## 6. Campeões, rebaixados e punições

**Títulos:**

- Ajax: 36
- PSV: 27
- Feyenoord: 16
- HVV Den Haag: 10
- Sparta Rotterdam: 6
- RAP Amsterdam: 4
- Go Ahead Eagles: 4
- HBS Den Haag: 3
- Willem II: 3
- AZ Alkmaar: 2
- RCH Heemstede: 2
- Heracles Almelo: 2
- ADO Den Haag: 2
- DOS Utrecht: 1
- DWS Amsterdam: 1
- Twente: 1
- Koninklijke HFC: 1
- Quick Den Haag: 1
- Be Quick Groningen: 1
- NAC Breda: 1
- SC Enschede: 1
- De Volewijckers: 1
- Haarlem: 1
- BVV: 1
- SVV Schiedam: 1
- Limburgia: 1
- SC Eindhoven: 1
- Rapid JC Heerlen: 1
- Sem campeão: 2019/20, 1888/89, 1889/90, 1892/93, 1896/97, 1944/45

**Rebaixamentos:** 154 no total; quem mais caiu: Volendam (11), Excelsior Rotterdam (9), De Graafschap (9), Willem II (8), VVV-Venlo (8).

**Punições em pontos:**

- 2010/11: NAC Breda -1
- 2014/15: Twente -6
- 2015/16: Twente -3
- 2023/24: Vitesse -18
- 1922/23: Willem II -2

## 7. Correções e decisões (com o motivo)

Registradas em `coleta/ned-1/importar.py`; cada uma também aparece no relatório, na temporada.

### Placares corrigidos (`CORRECOES`)

- **1969/70 · Sparta Rotterdam · ADO Den Haag:** [1, 2] a base traz 1-3; o ogol e a matriz da RSSSF trazem 1-2, e as tabelas da RSSSF e da Wikipédia só fecham com 1-2
- **1999/00 · Heerenveen · Willem II:** [2, 4] a base traz 2-3; o football-data e a matriz da RSSSF trazem 2-4, e as tabelas da RSSSF e da Wikipédia só fecham com 2-4

### Fora da temporada seguinte sem ter sido rebaixado (`NAO_REBAIXADOS`)

- **1964/65 · SC Enschede:** fundiu-se com o Enschedese Boys no FC Twente (1965), que ficou com o lugar na Eredivisie
- **1967/68 · Fortuna '54:** fundiu-se com o Sittardia no Fortuna SC (1968), que ficou com o lugar na Eredivisie; ninguém caiu em 1967/68 (Wikipédia)
- **1967/68 · Sittardia:** fundiu-se com o Fortuna '54 no Fortuna SC (1968); ninguém caiu em 1967/68 (Wikipédia)
- **1967/68 · Xerxes:** o Xerxes/DHC faliu ao fim da temporada; ninguém caiu em 1967/68 (Wikipédia)
- **1969/70 · DOS Utrecht:** fundiu-se com o Elinkwijk e o Velox no FC Utrecht (1970), que ficou com o lugar na Eredivisie
- **1970/71 · Holland Sport:** fundiu-se com o ADO no FC Den Haag (1971), que ficou com o lugar na Eredivisie
- **1971/72 · DWS Amsterdam:** fundiu-se com o Blauw-Wit e o De Volewijckers no FC Amsterdam (1972), que ficou com o lugar na Eredivisie
- **1990/91 · SVV Schiedam:** fundiu-se com o Dordrecht '90 (SVV/Dordrecht '90, 1991), que ficou com o lugar na Eredivisie

### Temporadas interrompidas (`INTERROMPIDAS`)

- **2019/20:** cancelada em abril de 2020 pela pandemia de covid-19, depois de 25 ou 26 rodadas (232 de 306 jogos): sem campeão, sem rebaixamento e sem acesso; a classificação é a do momento da parada

### Divergências entre fontes já explicadas (`EXPLICACOES`)

- **1957/58:** o título foi decidido num jogo extra (DOS e Ajax empatados em pontos), e o último lugar também (Elinkwijk 2-1 GVAV, em campo neutro): os jogos extras ficam de fora, como os play-offs; a ordem é a oficial (Wikipédia)
- **1959/60:** o título foi decidido num jogo extra (Ajax 5-1 Feyenoord, empatados em pontos): fica de fora, como os play-offs; a ordem é a oficial (Wikipédia)

### Edições sem título oficial (`SEM_TITULO`)

- **2019/20:** temporada cancelada (covid-19): a federação não deu o título

## 8. O que não deu para coletar

- **Autores dos gols e cartões antes de 2001/02:** nenhuma fonte em lote traz.
- **Público e estádio antes de 2001/02:** nenhuma fonte em lote.
- **Nacompetitie e play-offs de vaga europeia:** ficam de fora (entram com a 2ª divisão e as copas).
- **Campeonatos de antes da Eredivisie (1888/89-1955/56):** ficam de fora, à espera de decisão do Guilherme.
- **Zonas europeias:** a classificação rodada a rodada marca só título e rebaixamento.

## 9. Pendências

- nenhuma em aberto na coleta.

**Limites de fonte (fechados):** nenhuma fonte em lote tem o dado; só volta com uma fonte nova.

- Era antiga (1888/89-1955/56, em antigo.py): de 1888/89 a 1896/97 e nas temporadas sem a fase final legível na RSSSF, só o campeão e a tabela da Eerste Klasse, sem jogos; os jogos da fase final vêm da matriz da RSSSF, sem data (datados só em 1954/55 e 1955/56). As ligas regionais ficam de fora.
- Era antiga: tabelas da fase final que não fecham com os jogos por erro de digitação da RSSSF (1906/07, 1922/23, 1923/24); ficam anotadas no relatório.
- Autores dos gols e cartões antes de 2001/02: jogo a jogo (ficha do ogol).

**Com o agente de revisão:** decisões da coleta que ele confere.

- Identidade de clubes em fusões (GVAV x FC Groningen, SC Enschede x FC Twente, Rapid JC x Roda JC, Alkmaar '54 x AZ, BVV x FC Den Bosch): separados como clubes diferentes, contra o ogol, que junta alguns na ficha do sucessor.

## 10. Arquivos

- Código: `coleta/ned-1/` (`edicoes.py`, `baixar.py`, `importar.py`, leitor da RSSSF); cadastro dos clubes em `coleta/comum-europa/clubes_ned.py`.
- Fontes baixadas: `data/coleta/ned-1/` (uma pasta por fonte); calendários do ogol (escudos) em `data/cache/ogol-ned-1/`.
- Pacote: `data/coleta/ned-1/pacote/`; relatório: `docs/coleta/ned-1.md`.
- Refazer do zero: `python coleta/ned-1/baixar.py ...` (ver o docstring), `python coleta/ned-1/importar.py`, `python coleta/comum-europa/testar_carga.py ned-1 <pasta temporária>` e `python coleta/comum-europa/documentar.py`.

