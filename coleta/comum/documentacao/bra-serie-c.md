# Campeonato Brasileiro Série C (`bra-serie-c`) — documentação

Gerado por `python coleta/comum/documentar.py` a partir do pacote `data/coleta/bra-serie-c/pacote/` e dos módulos de `coleta/bra-serie-c/`. O relatório da importação, com as ocorrências temporada a temporada, está em `docs/coleta/bra-serie-c.md`.

## 1. O que temos

- **Edições:** 39, de 1981 a 2026.
- **Jogos:** 8705; **gols:** 21235; **gols com autor:** 6051 (28%); **cartões:** 0.
- **Clubes:** 379; **artilheiros:** 34 temporadas com artilheiro (46 linhas, com empates).
- **Classificação final:** 39 temporadas; **rodada a rodada:** 0 temporadas.
- **Tabelas publicadas guardadas para conferência:** 2117 linhas.
- **No banco (`db/futebol.db`):** sim (36 edições, 8123 jogos).
- **Observação da competição:** Inclui a Taça de Bronze (1981) e, como edições não oficiais (coluna oficial = não em edicoes.csv; decisão D-10), 1987 (Módulos Azul e Branco da Copa União) e 2000 (Módulos Verde e Branco da Copa João Havelange), que a CBF, a RSSSF e a Wikipédia não contam como Série C.

## 2. Fontes e regras

**Fontes:** RSSSF Brasil (`br{ano}l3.htm`, base de jogos, fases, grupos, datas e autores; as tabelas publicadas são a conferência); ogol (calendário de todas as edições e o código de cada clube, que dá a identidade entre anos e mudanças de nome; completa os jogos que faltam na RSSSF e é a base de 2019); ESPN (liga `bra.3`, 2017 em diante: hora e estádio; a ESPN não traz gols, cartões nem público da Série C); Wikipédia (punições de pontos e lista de campeões).

**Regras:** placar diferente entre RSSSF e ogol fica com a versão que fecha com a tabela publicada pela RSSSF; sem tabela, fica a da RSSSF. Autores dos gols só entram quando a soma bate com o placar. Clube que já está no `futebol.db` usa o nome de lá.

## 3. Conferência

- Cada temporada é comparada com as tabelas publicadas (RSSSF): 418 tabelas fecham com os jogos e 30 divergem (cada divergência é explicada no relatório, na temporada).
- Temporadas com alguma tabela divergente: 1988, 1992, 1994, 1995, 1996, 1997, 1999, 2002, 2003, 2005, 2006, 2007, 2008, 2010, 2011.
- Temporadas sem tabela para conferir: 2019, 2026.
- Temporadas com menos jogos do que o ogol: nenhuma.

## 4. Cobertura de cada campo, por década

Porcentagem dos jogos com o campo preenchido (gols com autor: porcentagem dos gols).

| Década | Jogos | data | hora | rodada | estádio | cidade | público | gols c/ autor | cartões/jogo |
|---|---|---|---|---|---|---|---|---|---|
| 1980s | 438 | 100% | 5% | 0% | 10% | 0% | 1% | 7% | 0.0 |
| 1990s | 1859 | 100% | 64% | 28% | 0% | 0% | 0% | 5% | 0.0 |
| 2000s | 3144 | 100% | 25% | 78% | 0% | 0% | 0% | 7% | 0.0 |
| 2010s | 1772 | 100% | 100% | 51% | 55% | 53% | 0% | 69% | 0.0 |
| 2020s | 1492 | 100% | 100% | 68% | 43% | 43% | 0% | 69% | 0.0 |

**Fonte de cada jogo:** RSSSF Brasil: 7688; Bola n@ Área: 582; ogol: 435.

## 5. Formato ao longo do tempo

**Número de clubes:**

- 1981 a 1987 Branco: 24 clubes
- 1988: 43 clubes
- 1990: 30 clubes
- 1992: 31 clubes
- 1994: 41 clubes
- 1995: 107 clubes
- 1996: 59 clubes
- 1997: 64 clubes
- 1998: 65 clubes
- 1999: 36 clubes
- 2000: 53 clubes
- 2001: 65 clubes
- 2002: 61 clubes
- 2003: 93 clubes
- 2004: 60 clubes
- 2005 a 2006: 63 clubes
- 2007: 64 clubes
- 2008: 63 clubes
- 2009 a 2012: 20 clubes
- 2013: 21 clubes
- 2014 a 2026: 20 clubes

**Pontos por vitória:**

- 1981 a 1987 Branco: 2
- 1988: 3
- 1990 a 1994: 2
- 1995 a 2026: 3

**Nome oficial:**

- 1981: Taça de Bronze
- 1987 Azul: Copa União - Módulo Azul
- 1987 Branco: Copa União - Módulo Branco
- 1988 a 1999: Campeonato Brasileiro Série C
- 2000: Copa João Havelange - Módulos Verde e Branco
- 2001 a 2026: Campeonato Brasileiro Série C

**Formato de cada edição** (fases na ordem; grupos; mata-mata):

- 1981: mata-mata + 2 grupos + mata-mata
- 1987 Azul a 1987 Branco: 6 grupos + mata-mata + pontos corridos
- 1988: 12 grupos + 6 grupos + 2 grupos + mata-mata
- 1990: 6 grupos + mata-mata
- 1992: 7 grupos + 2 grupos + mata-mata
- 1994: 11 grupos + mata-mata
- 1995: 32 grupos + mata-mata
- 1996: 16 grupos + mata-mata
- 1997: 16 grupos + mata-mata + pontos corridos
- 1998: 11 grupos + mata-mata + pontos corridos
- 1999: 6 grupos + pontos corridos + mata-mata + pontos corridos
- 2000: 8 grupos + 6 grupos + 2 grupos + mata-mata
- 2001: 10 grupos + 4 grupos + pontos corridos
- 2002: 16 grupos + mata-mata + pontos corridos
- 2003: 28 grupos + mata-mata + pontos corridos
- 2004 a 2005: 16 grupos + mata-mata + pontos corridos
- 2006 a 2008: 16 grupos + 8 grupos + 4 grupos + pontos corridos
- 2009 a 2010: 4 grupos + mata-mata
- 2011: 4 grupos + 2 grupos + mata-mata
- 2012 a 2020: 2 grupos + mata-mata
- 2021: pontos corridos + mata-mata
- 2022 a 2026: pontos corridos + 2 grupos + mata-mata

**Fases que aparecem** (número de temporadas): Primeira fase (39); Segunda fase (31); Final (25); Semifinal (15); Quartas de final (15); Terceira fase (14); Fase final (13); Oitavas de final (4); Quarta fase (3); Quinta fase (1).

**Observações das edições:**

- 1987 Azul: edição não oficial: o Módulo Azul da Copa União de 1987 (a CBF disse que nenhum módulo seria a 3ª divisão; decisão D-10); jogos pelo Bola n@ Área
- 1987 Branco: edição não oficial: o Módulo Branco da Copa União de 1987 (a CBF disse que nenhum módulo seria a 3ª divisão; decisão D-10); jogos pelo Bola n@ Área
- 2000: edição não oficial: os Módulos Verde e Branco da Copa João Havelange (equivalente à 3ª divisão, título não reconhecido pela CBF; decisão D-10); jogos pelo Bola n@ Área
- 2019: jogos pelo ogol (a página da RSSSF parou na 1ª rodada)

## 6. Campeões, acessos, rebaixados e punições

**Títulos:**

- Vila Nova-GO: 3
- Atlético-GO: 2
- Ituano: 2
- Olaria: 1
- Americano-RJ: 1
- Operário-MS: 1
- União São João: 1
- Tuna Luso: 1
- GE Novorizontino: 1
- XV de Piracicaba: 1
- Sampaio Corrêa: 1
- Avaí: 1
- Fluminense: 1
- J.Malucelli: 1
- Paulista: 1
- Brasiliense: 1
- União Barbarense: 1
- Remo: 1
- Criciúma: 1
- Bragantino: 1
- América-MG: 1
- ABC: 1
- Joinville: 1
- Oeste: 1
- Santa Cruz: 1
- Macaé: 1
- Boa Esporte: 1
- CSA: 1
- Operário-PR: 1
- Náutico: 1
- Mirassol: 1
- Amazonas: 1
- Volta Redonda: 1
- Ponte Preta: 1
- Maringá: 1

**Acessos:** 79 no total; quem mais teve: ABC (4), Ferroviária-SP (3), Botafogo-SP (3), Paysandu (3), Sampaio Corrêa (3), Londrina (3), Gama (2), Mogi Mirim (2).

**Rebaixamentos:** 71 no total; quem mais teve: Sampaio Corrêa (2), Confiança (2), Campinense (2), Brasil de Pelotas (2), Salgueiro (2), Tupi (2), Treze (2), América-RN (2).

**Punições em pontos:**

- 2005: Nacional-PB -6
- 2006: Ananindeua -6
- 2006: Ceilândia -6
- 2006: Ulbra-RO -6
- 2006: Ypiranga-PE -6
- 2006: Estrela do Norte -18
- 2007: Nacional-PB -6
- 2007: Imperatriz -12
- 2008: Sergipe -6
- 2011: Brasil de Pelotas -6
- 2014: CRAC -3

## 7. Correções e decisões (com o motivo)

Registradas nos módulos de `coleta/bra-serie-c/`; cada uma também aparece no relatório, na temporada.

### Temporadas com o ogol como base dos jogos (`importar.BASE_OGOL`)

- **2019:** a página da RSSSF parou na 1ª rodada (40 jogos): a base dos jogos é o ogol (194 jogos)
- **2026:** a RSSSF ainda não tem a página de 2026: a base dos jogos é o ogol (revisão SC-001)

### Clube trocado pelo ogol numa temporada (código -> código) (`importar.CORRIGE_OGOL`)

- **1981 · 3333:** [2541] o ogol liga o Matsubara de 1981 ao J. Malucelli (fundado em 1994); a RSSSF traz a SE Matsubara, de Cambará
- **2003 · 3307:** [3306] o Ituiutaba EC de 2003 (hoje Boa Esporte) aparece no ogol em dois cadastros (revisão SC-012)
- **2002 · 15723:** [3500] o Tubarão de 2002 é o Tubarão FC (1992-2005); o CA Tubarão do ogol foi fundado em 2005 (revisão CL-002)
- **1981 · 43721:** [238972] Joaçaba EC (1977, extinto nos anos 1980); o Joaçaba AC é de 1997 e não é sucessor (revisão CL-012)
- **1981 · 70071:** [241325] SE São Borja (1977); o EC São Borja é de 2009, outro clube (revisão CL-012)
- **2001 · 15641:** [89206] Guarabira EC (1936, extinto em 2004); a AD Guarabira é outro clube (revisão CL-012)
- **2002 · 237932:** [3461] São Gabriel FC (2000-2013), o mesmo da Copa do Brasil 2004; o EC São Gabriel é de 2013 (revisão CL-005)
- **2003 · 41237:** [3260] Goiatuba EC (1970), o mesmo de hoje; a AA Goiatuba é de 2009 (revisão CL-006)
- **1997 · 3373:** [ec-operario-mt] EC Operário (1996-2001), que substituiu o CEOV; não é o Operário FC Ltda de 2002 (revisão CL-007)
- **1988 · 39060:** [241324] Lagarto EC (1955-1990); o Lagarto FC é de 2009 (revisão CL-008)
- **1990 · 39060:** [241324] Lagarto EC (1955-1990); o Lagarto FC é de 2009 (revisão CL-008)
- **1988 · 3161:** [71868] AA Cabofriense (1955); a AD Cabofriense é de 1997 (revisão CL-009)
- **1998 · 3326:** [115862] EC Limoeiro (1942); a AD Limoeiro é de 2001 (revisão CL-011)
- **1995 · 11647:** [214025] o Ariquemes de 1995 é a SE Ariquemes (1981); o Ariquemes FC do ogol foi fundado em 1996 (revisão CL-004)

### Clube trocado pelo ogol num jogo (`importar.CORRIGE_OGOL_JOGO`)

- **7437399:** [3224, 15766] 1988, 2ª fase, grupo 18: o ogol põe a Desportiva Ferroviária no lugar da Ferroviária-SP (revisão SC-008)
- **7437402:** [3224, 15766] 1988, 2ª fase, grupo 18: o ogol põe a Desportiva Ferroviária no lugar da Ferroviária-SP (revisão SC-008)
- **7437404:** [3224, 15766] 1988, 2ª fase, grupo 18: o ogol põe a Desportiva Ferroviária no lugar da Ferroviária-SP (revisão SC-008)
- **7437405:** [3224, 15766] 1988, 2ª fase, grupo 18: o ogol põe a Desportiva Ferroviária no lugar da Ferroviária-SP (revisão SC-008)
- **7437408:** [3224, 15766] 1988, 2ª fase, grupo 18: o ogol põe a Desportiva Ferroviária no lugar da Ferroviária-SP (revisão SC-008)
- **7437410:** [3224, 15766] 1988, 2ª fase, grupo 18: o ogol põe a Desportiva Ferroviária no lugar da Ferroviária-SP (revisão SC-008)

### Nome da página casado à mão com o clube (`importar.NOME_MANUAL`)

- **1995 · Intercap:** [3293] o Intercap, de Paraíso do Tocantins, é o 'Paraíso' do ogol (mesmos jogos e placares)
- **1995 · INTERCAP(TO):** [3293] o Intercap, de Paraíso do Tocantins, é o 'Paraíso' do ogol (mesmos jogos e placares)
- **1995 · Intercap(TO):** [3293] o Intercap, de Paraíso do Tocantins, é o 'Paraíso' do ogol (mesmos jogos e placares)
- **1995 · Intercap-TO:** [3293] o Intercap, de Paraíso do Tocantins, é o 'Paraíso' do ogol (mesmos jogos e placares)
- **1995 · ARAGUAINENSE(TO):** [276477] União Atlética Araguainense, como no ogol
- **1995 · Araguainense:** [276477] União Atlética Araguainense, como no ogol
- **1995 · OPERARIO(MT):** [36613] o Operário de Várzea Grande de 1995 é o 'CEOV Operário' do ogol
- **1995 · Operário-MT:** [36613] o Operário de Várzea Grande de 1995 é o 'CEOV Operário' do ogol
- **1995 · Lousano Paulista(SP):** [3388] Lousano Paulista era o nome do Paulista de Jundiaí em 1995
- **1995 · Roraima:** [3440] o 'Roraima' dos jogos é o 'ATL.RORAIMA' da tabela do grupo 21 (Atlético Roraima)
- **2001 · Atl.Cajazeirense:** [3130] Atlético Cajazeirense é o 'Atlético-PB' (Cajazeiras) do ogol
- **2002 · Atl.Cajazeirense:** [3130] Atlético Cajazeirense é o 'Atlético-PB' (Cajazeiras) do ogol
- **2007 · Atl.Cajazeirense:** [3130] Atlético Cajazeirense é o 'Atlético-PB' (Cajazeiras) do ogol
- **2003 · Ituiatuba:** [3306] erro de digitação da RSSSF: Ituiutaba (hoje Boa Esporte)
- **1999 · Serra (SE):** [3474] erro de digitação da RSSSF: é o Serra (ES), representante do Espírito Santo
- **2002 · São Gabriel:** [3461] São Gabriel FC (revisão CL-005)
- **1981 · Joaçaba:** [238972] Joaçaba EC (revisão CL-012)
- **1981 · São Borja:** [241325] SE São Borja (revisão CL-012)
- **2001 · Guarabira:** [89206] Guarabira EC (revisão CL-012)
- **2003 · Goiatuba:** [3260] Goiatuba EC (revisão CL-006)
- **1997 · Operário(MT):** [ec-operario-mt] EC Operário, de Várzea Grande (revisão CL-007)
- **1988 · Lagarto:** [241324] Lagarto EC (revisão CL-008)
- **1990 · Lagarto:** [241324] Lagarto EC (revisão CL-008)
- **1988 · Cabofriense:** [71868] AA Cabofriense (revisão CL-009)
- **1998 · Limoeiro:** [115862] EC Limoeiro (revisão CL-011)
- **2003 · Ituiutaba:** [3306] Ituiutaba EC, hoje Boa Esporte: um clube só em 2003 (revisão SC-012)
- **2002 · Tubarão:** [3500] Tubarão FC (1992-2005), como nos participantes da RSSSF (revisão CL-002)
- **1995 · Ariquemes:** [214025] SE Ariquemes (1981), a mesma da Copa do Brasil de 1994 (revisão CL-004)
- **1995 · ARIQUEMES(RO):** [214025] SE Ariquemes (1981), a mesma da Copa do Brasil de 1994 (revisão CL-004)

### Nome da página casado à mão, por grupo (`importar.NOME_MANUAL_GRUPO`)

- **2007 · Imperatriz · Grupo 17:** [3285] o ogol anula os jogos do Imperatriz no grupo 17 e os votos levavam o nome ao Tuna Luso (revisão SC-009, CL-001)
- **2004 · Atlético · Grupo 13:** [3125] o 'Atlético' do grupo 13 é o Atlético Sorocaba (revisão SC-011)

### Jogos que ficam fora (`importar.JOGOS_FORA`)

- **2011 · CRB · Rio Branco · 0 · 0 · SECOND STAGE::** Rio Branco-AC eliminado pelo STJD: os jogos da 2ª fase não contam (revisão SC-013)
- **2011 · Rio Branco · Paysandu · 1 · 2 · SECOND STAGE::** Rio Branco-AC eliminado pelo STJD: os jogos da 2ª fase não contam (revisão SC-013)
- **2011 · América · Rio Branco · 3 · 0 · SECOND STAGE::** Rio Branco-AC eliminado pelo STJD: os jogos da 2ª fase não contam (revisão SC-013)
- **2008 · Inter/SM · Engenheiro Beltrão · 3 · 2 · FIRST STAGE::** jogo repetido na página (o grupo 15 fica com 7 jogos por clube; a tabela fecha com o 3-0 de 17/08) (revisão SC-010)
- **2008 · Toledo CW · Marcílio Dias · 1 · 1 · FIRST STAGE::** o mesmo jogo da 2ª fase (24/08), repetido na 1ª (revisão SC-010)

### Clubes com todos os jogos fora (`importar.RSSSF_FORA`)

- **1998 · Itumbiara:** eliminado por não pagar a taxa de arbitragem; todos os seus jogos foram anulados (nota da RSSSF; o ogol e a tabela do grupo 5 não os trazem)

### Jogos do ogol ignorados (`importar.OGOL_IGNORAR`)

- **6939419:** 1995, grupo 12: Botafogo-PB x Coríntians foi cancelado (nota da RSSSF: '*x*'); o ogol traz 0-0, e a tabela do grupo não conta o jogo
- **6939420:** 1995, grupo 12: Santa Cruz-PB x ABC foi cancelado (nota da RSSSF: '*x*'); o ogol traz 0-0, e a tabela do grupo não conta o jogo
- **5111115:** 1998, grupo 10: o ogol tem União Bandeirante 5-0 Figueirense em 27/09; a RSSSF traz União Bandeirante 3-0 São José-RS, e as tabelas de Figueirense e São José só fecham com a RSSSF
- **6953693:** 1997, 2ª fase: o ogol tem Operário-MS 0-0 Itumbiara na volta; o confronto foi com o Ji-Paraná (ida 1-0 no ogol e na RSSSF); o Itumbiara já tinha caído na 1ª fase

### Placares e jogos corrigidos à mão (`importar.PLACAR_MANUAL`)

- **2007 · ABC · Vera Cruz · 2007-07-14:** [ABC, Vera Cruz, 4, 0, ] ogol, Bola n@ Área, Futebol Nacional e a tabela do grupo 6 na Wikipédia pt: 4-0 (revisão QC-011)
- **1988 · Internacional · Figueirense · 1988-11-03:** [Internacional, Figueirense, 2, 0, ] ogol e Wikipédia: 2-0 (revisão SC-014)
- **1992 · Rio Branco-MG · São Bento · 1992-03-29:** [Rio Branco-MG, São Bento, 2, 1, ] ogol e Wikipédia: 2-1 (revisão SC-014)
- **1992 · Nacional-AM · Ji-Paraná · 1992-04-01:** [Nacional-AM, Ji-Paraná, 1, 0, ] ogol e Wikipédia: 1-0 (revisão SC-014)
- **1992 · Nacional-AM · Macapá · 1992-04-16:** [Macapá, Nacional-AM, 0, 2, ] ogol e Wikipédia: Macapá 0-2 Nacional-AM (revisão SC-014)
- **1992 · Nacional-AM · Auto Esporte · 1992-05-24:** [Nacional-AM, Auto Esporte, 3, 0, ] ogol e Wikipédia (Placar): 3-0 (revisão SC-014)
- **2003 · Atlético Roraima · Rio Branco-AC · 2003-10-16:** [Atlético Roraima, Rio Branco-AC, 1, 2, ] ogol e Wikipédia: 1-2 (revisão SC-014)
- **1995 · Itumbiara · Gama · 1995-09-02:** [Itumbiara, Gama, 1, 0, awd] em campo 1-2; o jogo foi dado ao Itumbiara (1-0): a tabela do grupo 8 na RSSSF e na Wikipédia fecha assim (revisão SC-015)

### Punições em pontos (`importar.AJUSTE_MANUAL`)

- **2007:** Nacional-PB → -6

### Punições que não valem (`importar.AJUSTE_FORA`)

- **2007 · Araguaina-TO:** a perda de 12 pontos do Araguaína foi revertida (Wikipédia pt)
- **2006 · Ituiutaba:** punição com '?' na própria fonte

### Ocorrências explicadas, por temporada (`explicacoes.EXPLICACOES`)

- **1987 Branco:** a colocação final da página principal do Bola não fecha com a lista de jogos do próprio site (o Sobradinho com 5 jogos e 6 resultados; a prorrogação do Moto Club x Tuna Luso fora, a do Uberlândia dentro); valem os jogos, que fecham com as 7 tabelas de grupo do Bola
- **2000:** o Malutrom, campeão, é o J. Malucelli de hoje (o mesmo clube do banco); o Internacional do grupo H é o de Santa Maria ("Internacional-SM" nos jogos), e o Etti Jundiaí é o Paulista de Jundiaí
- **2026:** a RSSSF ainda não tem a página de 2026: os jogos, as fases e os grupos vêm do ogol, e o campeão, os acessos e os rebaixados da Wikipédia (revisão SC-001). Sem autores de gols
- **1981:** o ogol liga o Matsubara (Cambará-PR) ao J. Malucelli, fundado em 1994; corrigido no código (CORRIGE_OGOL): fica a SE Matsubara, como na RSSSF
- **1988:** a final (Esportivo-MG x União São João, 1-1 e 2-2) foi decidida pela campanha (número de vitórias): campeão pela lista oficial / vitória valia 3 pontos e o empate ia para os pênaltis: 2 para quem vencia, 1 para quem perdia (revisão SC-007). No grupo 18 da 2ª fase o ogol põe a Desportiva Ferroviária no lugar da Ferroviária-SP; corrigido (revisão SC-008)
- **1994:** Caldas x Vila Nova-GO (2ª fase, 23/10): fontes divididas como em 1992; fica o placar do pacote (D-13, SC-016) / nas oitavas, o 'Vitória' sem estado da página é o Vitória-ES (o Vitória-PE caiu para o ABC na mesma fase); corrigido no texto da página / o ogol põe o Vitória-ES contra o ABC no jogo de volta das oitavas; a RSSSF e a classificação final mostram o Vitória-PE (fica a RSSSF)
- **1995:** página com 108 clubes e a 2ª e a 3ª fases em confrontos colados uns nos outros; o leitor separa cada jogo (rsssf_c.py, _1995) / erros de digitação da página corrigidos no código: 'Coríntians 3x1 3x1 Santa Cruz-PB' (placar repetido) e 'Ypranga'
- **1996:** a página traz 'GAS 2-3 GAS' no grupo 2; é GAS 2-3 Baré (ogol e tabela do grupo); corrigido no texto da página
- **1999:** a página traz, antes da Série C, as seletivas estaduais (RS, PR, MG, PB, PE, PI); esse trecho fica de fora / 226 jogos, 2 a mais que a Wikipédia e o Bola n@ Área (224): o pacote conta os 2 jogos-desempate, que existiram (revisão SC-021)
- **2001:** 1.124 gols, a soma dos 412 jogos (igual à soma dos jogos do Bola n@ Área); o 1.127 do resumo do Bola, copiado pela Wikipédia, não fecha com os jogos (revisão SC-021)
- **2002:** 595 gols, 6 a mais que o Bola n@ Área (589): a diferença está nos placares em que a RSSSF e o Bola divergem, que ficam com a RSSSF até uma 4ª fonte (revisão QC-012 e SC-021) / dúvida em aberto: o ogol liga o 'SER São Gabriel' da RSSSF ao 'EC São Gabriel', que a ficha do ogol diz fundado em 2013; pode ser erro do ogol. Fica como está (decisão do agente principal, 20/11/2026)
- **2005:** a página traz o público no fim da linha dos jogos das fases finais ('att: 18.865'); o leitor lê o público (12 jogos)
- **2011:** o Rio Branco-AC foi eliminado pelo STJD depois de recorrer à Justiça comum; a RSSSF mantém 3 jogos dele na 2ª fase, que o ogol não tem (ficam, com a fonte RSSSF) / sem os 3 jogos do Rio Branco-AC na 2ª fase (eliminado pelo STJD; o grupo E recomeçou com o Luverdense), o 3º é o Ipatinga, como na Wikipédia (revisão SC-003, SC-013). A edição fica com 106 jogos; o infobox da Wikipédia diz 105 (diferença não achada, revisão SC-021)
- **1992:** Nacional-AM x Tuna Luso (2ª fase, 27/05) e Rio Branco-MG x Marília: a RSSSF e o ogol dão o placar do pacote; o Bola n@ Área e a Wikipédia (que cita o Bola), outro; fica o do pacote até um jornal da época (decisão D-13, revisão SC-016) / 5 placares da página trocados pelos do ogol e da Wikipédia (revisão SC-014); as tabelas publicadas pela RSSSF seguem os placares antigos da página e por isso não fecham nos grupos 1 e 6 e no grupo A da 2ª fase. Com os placares novos o 3º é o Nacional-AM, como na Wikipédia. Dois jogos do grupo B vêm na página depois do título da final e voltam para a 2ª fase
- **2013:** o Rio Branco-AC entrou na competição por decisão judicial; a página da RSSSF não traz os 20 jogos dele no grupo A, que entram pelo ogol (a tabela do grupo fecha)
- **2015:** a página da RSSSF trocou dia e mês em 37 datas ('06/jan/15' em vez de 02/06); vale a data do ogol
- **2017:** Mogi Mirim x Ypiranga-RS (grupo B) foi W.O. ('0-WO' na página): entra 0-3, como conta a tabela do grupo
- **2019:** a página da RSSSF parou na 1ª rodada (40 jogos): a base dos jogos é o ogol (194), sem autores de gols
- **2024:** a página da RSSSF traz os autores dos gols sem dizer de que time é cada um ('18' (25-Pedro Henrique)'): ficam só no texto (gols_texto)

### Clube do ogol casado à mão com o nome do banco (`clubes_c.MANUAL_DB`)

- **3333:** [J.Malucelli] o ogol escreve 'JMalucelli'; é o J. Malucelli do banco (Série A 2000)
- **24836:** [Novorizontino] Grêmio Novorizontino (2010-); o banco separou o GE Novorizontino (1973-1999) em 20/11/2026

### Nome de exibição de clube novo, dado à mão (`clubes_c.MANUAL_NOVO`)

- **3422:** [Santo Amaro-PE] Santo Amaro de Recife, vice de 1981: só jogou a Série C com este nome (RSSSF, ogol e Bola n@ Área); "Manchete" é nome posterior. Nome da época no cadastro (decisão D-03, achado QC-009)
- **238972:** [Joaçaba EC] Joaçaba Esporte Clube (1977): não é o Joaçaba AC de 1997 (revisão CL-012)
- **241325:** [SE São Borja] Sociedade Esportiva São Borja (1977): não é o EC São Borja de 2009 (revisão CL-012)
- **89206:** [Guarabira EC] Guarabira Esporte Clube (1936-2004): não é a AD Guarabira (revisão CL-012)
- **241324:** [Lagarto EC] Lagarto Esporte Clube (1955-1990): não é o Lagarto FC de 2009 (revisão CL-008)
- **71868:** [AA Cabofriense] Associação Atlética Cabofriense (1955): não é a AD Cabofriense de 1997 (revisão CL-009)
- **115862:** [EC Limoeiro] Esporte Clube Limoeiro (1942): não é a AD Limoeiro de 2001 (revisão CL-011)
- **ec-operario-mt:** [EC Operário-MT] Esporte Clube Operário (1996-2001), de Várzea Grande; sem ficha no ogol (revisão CL-007)
- **68358:** [Corinthians Prudente] EC Corinthians de Presidente Prudente (1996): não é o Corinthians paulistano do banco
- **45210:** [Maringá] Maringá FC fundado em 2010 (Série C 2025): não é o GE Maringá do banco
- **241210:** [Maringá FC 1995] Maringá FC fundado em 1995 (Série C 1997): outro clube, nome como no ogol
- **60858:** [GE Novorizontino] Grêmio Esportivo Novorizontino (1973-1999, campeão de 1994): outro clube; o 'Novorizontino' do banco fica com o Grêmio Novorizontino, fundado em 2010 (decisão do Guilherme, 20/11/2026)
- **20122:** [Linhares EC] dois clubes de Linhares-ES: o EC (anos 1990) e o FC (anos 2000); o sufixo já distingue
- **9783:** [Linhares FC] dois clubes de Linhares-ES: o EC (anos 1990) e o FC (anos 2000); o sufixo já distingue

### Páginas da RSSSF corrigidas na leitura (`rsssf.CORRECOES`, registradas em `coleta/bra-serie-c/rsssf_*.py`)

- **br1981l3.htm:** duas colunas, confrontos numa linha e final só em ficha técnica
- **br1990l3.htm:** linhas de jogo e de autores partidas no meio; data colada no nome
- **br1994l3.htm:** oitavas: o 'Vitória' sem estado é o Vitória-ES (o Vitória-PE caiu para o ABC na mesma fase); mata-mata com os dois jogos do confronto numa linha só
- **br1995l3.htm:** 2ª e 3ª fases em confrontos colados; placar repetido e nome com erro de digitação
- **br1996l3.htm:** grupo 2: 'GAS 2-3 GAS' é GAS 2-3 Baré (o ogol e a tabela do grupo confirmam)
- **br1999l3.htm:** seletivas estaduais no começo da página (não são jogos da Série C)
- **br2003l3.htm:** confronto em linha só, com a volta abandonada ('abd'): vira dois jogos; o placar da volta vem do ogol
- **br2015l3.htm:** pênaltis em linha própria, colada no título seguinte ('PK: 4-3  GRUPO H')
- **br2024l3.htm:** linhas da tabela da 1ª fase coladas umas nas outras ('... 43  11-Figueirense  24  19 ...'); estádio de nome longo colado no nome do mandante ('.../São João del Rei Athletic')

## 8. O que não deu para coletar

- **Cartões:** nenhuma das fontes lidas traz cartões da Série C (a RSSSF não traz; a ESPN não tem lances da Série C).
  O ogol tem cartões e autores dos gols na página de cada jogo, mas seriam uns 8 mil pedidos (cerca de 3 horas);
  fica como próximo passo, se aprovado.
- **Autores dos gols:** só onde a RSSSF traz e a soma fecha com o placar. Faltam (quase) todos em 1994-2001, 2008, 2011,
  2012, 2019 e 2024.
- **Público:** a ESPN traz 0 na Série C e a RSSSF só em poucas fichas de final.
- **Hora e estádio:** RSSSF (2013-2015, 2020, 2023, 2024), ogol (hora) e ESPN (2017 em diante).
- **Classificação final:** a ordem oficial existe só quando a RSSSF publica a classificação geral (7 edições); nas outras ela é
  calculada (fase alcançada, pontos, vitórias, saldo, gols pró), com campeão e vice em cima.
- **Acesso:** marcado quando o clube jogou a Série B no ano seguinte (pelo `futebol.db`) ou está nos "promovidos" do infobox
  da Wikipédia. **Rebaixamento:** marcas "Relegated" das tabelas da RSSSF e "rebaixados" do infobox.

## 9. Pendências e próximos passos

- Achados da revisão SC-001 a SC-023 e CL-002/CL-004/CL-005/CL-012: tratados (docs/coleta/pedidos.md, partes 2 e 4, edições de 2026 e identidade). A revisão ainda não reconferiu (docs/revisao/achados.csv segue com 'aberto').
- Autores dos gols antes de 2012 e cartões: só jogo a jogo, pela ficha do ogol (~8 mil pedidos, ~3 h). Prioridade baixa (cartões, mais baixa ainda), decisão do Guilherme (20/11/2026).

## 10. Arquivos e comandos

| Arquivo | O que faz |
|---|---|
| `coleta/bra-serie-c/baixar_bola.py` | Baixa do Bola n@ Área (bolanaarea.com) as páginas das Séries C não oficiais de 1987 (Módulos Azul e Branco da Copa União) e 2000 (Módulos Verde e Branco da Copa João Havelange), para data/coleta/bra-serie-c/bola/ (decisã |
| `coleta/bra-serie-c/baixar_espn_wiki.py` | Baixa as fontes complementares da Série C: - ESPN (liga "bra.3"), 2016 em diante: data e hora, estádio e cidade de cada jogo -> data/coleta/bra-serie-c/espn/serie_c_{ano}.json. A ESPN não traz gols, cartões nem público d |
| `coleta/bra-serie-c/baixar_ogol.py` | Baixa o calendário de cada edição da Série C no ogol para data/coleta/bra-serie-c/ogol/serie_c_{ano}.json. |
| `coleta/bra-serie-c/baixar_ogol_clubes.py` | Baixa a ficha no ogol de cada clube que aparece nos calendários da Série C (nome completo, cidade, UF) e grava data/coleta/bra-serie-c/ogol/clubes.json. As páginas ficam em data/cache/ogol_equipes/. |
| `coleta/bra-serie-c/baixar_rsssf.py` | Baixa as páginas da Série C da RSSSF Brasil para data/coleta/bra-serie-c/rsssfbrasil/. |
| `coleta/bra-serie-c/bola_c.py` | Leitor das páginas do Bola n@ Área (data/coleta/bra-serie-c/bola/, de baixar_bola.py) das Séries C não oficiais de 1987 e 2000 (decisão D-10, achado SC-029). A página é lida célula a célula (o mesmo jeito de revisao/QC/b |
| `coleta/bra-serie-c/clubes_c.py` | Identidade dos clubes da Série C. |
| `coleta/bra-serie-c/edicoes.py` | Edições da Série C: anos, nomes oficiais e campeões (conferidos em duas fontes). |
| `coleta/bra-serie-c/explicacoes.py` | Textos do relatório da Série C que não saem do código: introdução e explicações de cada edição (divergências que ficaram, depois de conferidas à mão). |
| `coleta/bra-serie-c/importar.py` | Junta as fontes da Série C e grava o pacote em data/coleta/bra-serie-c/pacote/ e o relatório em docs/coleta/bra-serie-c.md. |
| `coleta/bra-serie-c/pacote.py` | Grava o pacote da Série C (data/coleta/bra-serie-c/pacote/) e o relatório (docs/coleta/bra-serie-c.md), no formato de docs/agente-coleta-COMECE-AQUI.md, seção 4. Chamado por importar.py. |
| `coleta/bra-serie-c/rsssf_c.py` | Leitura das páginas da Série C da RSSSF Brasil (data/coleta/bra-serie-c/rsssfbrasil/br{ano}l3.htm). |

- Fontes baixadas: `data/coleta/bra-serie-c/` (bola, espn, ogol, rsssfbrasil, wikipedia). Pacote: `data/coleta/bra-serie-c/pacote/`. Relatório: `docs/coleta/bra-serie-c.md`.
- Código comum: `coleta/comum/` (`rsssf.py` leitor das páginas da RSSSF Brasil, `ogol.py` calendários e fichas, `gols.py` autores dos gols, `registro.py` cadastro comum de nomes `data/coleta/comum/clubes_ogol.json`, `baixar.py` download educado).
- Refazer do zero (da raiz do `clube_analitico`, logs no scratchpad):

  - `python coleta/bra-serie-c/baixar_bola.py` (ver o docstring)
  - `python coleta/bra-serie-c/baixar_espn_wiki.py` (ver o docstring)
  - `python coleta/bra-serie-c/baixar_ogol.py` (ver o docstring)
  - `python coleta/bra-serie-c/baixar_ogol_clubes.py` (ver o docstring)
  - `python coleta/bra-serie-c/baixar_rsssf.py` (ver o docstring)
  - `python coleta/bra-serie-c/importar.py` (grava o pacote e o relatório; `importar.py <ano>` só mostra, sem gravar)
  - `python coleta/comum/testar_carga.py bra-serie-c <pasta temporária>` (deve terminar com `-> OK`)
  - `python coleta/comum/documentar.py`

