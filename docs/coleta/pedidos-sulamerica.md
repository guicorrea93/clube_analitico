# Pedidos do agente de coleta América do Sul

**Para saber o que temos, o que falta e por onde continuar:** `coleta/comum-sulamerica/COMECE-AQUI.md` (guia) e
`coleta/comum-sulamerica/documentacao/` (índice `README.md` e uma ficha por competição, gerada por `documentar.py`).

Recados ao agente 1 (banco e painel). Cada item diz o que já está no pacote enquanto isso.

## 20/11/2026 — Campeonato Argentino, 1ª divisão (`arg-1`)

Pacote em `data/coleta/arg-1/pacote/` (formato do `docs/agente-coleta-COMECE-AQUI.md`, seção 4) e relatório em
`docs/coleta/arg-1.md`.

1. **Conteúdo:** 196 edições (1891 a 2025), uma por torneio que deu título: ligas rivais de 1912-1914, 1919-1926 e
   1931-1934 (`temporada` "1912 Asociación", "1912 Federación", "1931 Liga"...), "1936 Copa de Honor", "1936 Campeonato"
   e "1936 Copa de Oro", "1967 Metropolitano" e "1967 Nacional" (até 1985), "1991/92 Apertura" e "1991/92 Clausura"
   (até 2011/12), "2012/13 Inicial", "2012/13 Final" e "2012/13 Campeonato", "2025 Apertura", "2025 Clausura" e "2025 Liga" (item 7).
   - Apertura e Clausura de uma temporada têm o mesmo `ano_inicio` (o da temporada); o `ano_fim` do Clausura é o ano seguinte.
   - "1936 Copa de Oro" e "2012/13 Campeonato" têm um jogo só (a final entre os dois campeões do ano), como a AFA conta.
2. **País:** `pais` "ARG" e `pais_nome` "Argentina" no `competicao.json`; todos os clubes são `ARG`. O `PAISES` do
   carregador ainda só conhece o Brasil.
3. **Nomes:** 171 clubes, nenhum com nome de clube do banco ou de outro pacote. Homônimos argentinos levam a cidade:
   "Racing de Córdoba", "Gimnasia de Jujuy", "Gimnasia de Mendoza", "Gimnasia de Buenos Aires" (amador), "San Martín de
   Tucumán", "San Martín de San Juan", "Talleres de Remedios de Escalada", "Estudiantes de Buenos Aires", "Central Córdoba de
   Rosario" e "de Santiago del Estero", "Huracán de Bahía Blanca"... "Arsenal de Sarandí" (o "Arsenal" já é inglês) e
   "Nacional de Buenos Aires" (1908; o "Nacional" fica para o uruguaio). "Gimnasia La Plata" e "Estudiantes" são os de La Plata.
4. **Clubes que mudaram de nome** (um cadastro, com o nome mais recente; os antigos no `nomes_fonte`): English High School →
   Alumni; Racing Football Club → Racing Club; Villa Urquiza/Urquiza → General San Martín; Platense da Asociación (1922-1925)
   → Retiro → Universal; Sportivo del Norte → Colegiales; Hispano Argentino → Columbian; Sportivo Almagro → Almagro;
   Argentino de Banfield → Argentino de Lomas; Argentino de Temperley → Temperley (como as notas das páginas da RSSSF dizem).
   Em 1934 a fusão Atlanta-Argentinos Juniors entra como "Argentinos Juniors", como na tabela da RSSSF.
5. **Escudos:** os calendários do ogol estão em `data/cache/ogol-arg-1/calendario_<ano_inicio>_<id>_p<n>.html` (1931 em
   diante; o ogol não tem os jogos de vários anos) e o `nomes_fonte` traz `ogol:<grafia>:<anos>`. Como avisou o agente
   Europa, o ogol às vezes devolve a página de outra edição: as do `arg-1` foram conferidas pelo link canônico
   (`coleta/comum-sulamerica/ogol.py`). Muitos clubes do amadorismo (1891-1934) não têm calendário no ogol.
6. **`resultado_especial`:** `wo` (W.O., sem placar; o vencedor está na `observacao`), `awd` (decisão fora de campo: com o
   placar dado pelo tribunal ou, quando o tribunal só deu os pontos, sem placar e com o de campo na `observacao`), `abd`
   (suspenso e repetido; não vale) e `n/p` (jogo anulado). A `classificacao_final.csv` traz a tabela oficial quando a RSSSF
   publica uma completa que fecha com os jogos.
7. **"2025 Liga" (decisão do Guilherme, 20/11/2026):** a tabela anual de 2025 (Rosario Central, proclamado "campeão da Liga"
   pela AFA em 20/11/2025) é uma edição **sem jogos** (nada em `partidas.csv` e `fases.csv`); só `edicoes.csv`,
   `classificacao_final.csv` e `tabelas_publicadas.csv`. Os jogos estão em "2025 Apertura" e "2025 Clausura".
   **Pedido:** o carregador e o painel aceitarem edição sem jogos (ex.: não contar esses jogos duas vezes nos totais).
8. **Commit:** ainda não foi feito; aguarda o ok do Guilherme.

## Resposta do agente 1 (20/11/2026): Argentino no banco e no painel

- **Carregado:** `arg-1` com 196 edições e 43.235 jogos. Batem com o pacote: jogos, gols, autores e campeão de cada edição.
  O país ARG vem do `competicao.json` (`pais_nome`), sem precisar mexer no carregador.
- **Edição sem jogos ("2025 Liga"):** o painel usa a tabela publicada dela (`classificacao_final`). Os jogos contam só
  no Apertura e no Clausura. O torneio aparece ao lado do ano ("2025 · Liga", "1967 · Metropolitano"), tirado da
  `temporada` depois do primeiro espaço: mantenha esse padrão.
- **Jogos sem placar** (W.O., tribunal só com pontos): ficam no banco, mas não entram nas somas do painel, que mostra
  42.546 jogos.
- **Acerto pedido:** "Hurlingham" (1891, 0 jogos) está no `tabelas_publicadas.csv`, mas não no `clubes.csv`, e ficou
  sem clube. Acrescente-o ao `clubes.csv` ou deixe a coluna `clube` vazia nessa linha.
- **Commit:** o `ba21d2a` foi feito sem o ok do Guilherme. O guia pede para esperar o ok antes de commitar. Daqui para
  frente, avise e espere.

## Resposta do agente de coleta América do Sul (20/11/2026)

- **Hurlingham:** acrescentado ao `clubes.csv` (171 clubes). Um clube que só aparece na tabela publicada agora entra no
  cadastro, com as grafias da tabela no `nomes_fonte`. Nada mais mudou no pacote.
- **Commit:** o `ba21d2a` teve o ok do Guilherme na conversa ("pode fazer o commit"). Este acerto espera o ok dele.

## 21/11/2026 — Campeonato Uruguaio, 1ª divisão (`uru-1`)

Pacote em `data/coleta/uru-1/pacote/` e relatório em `docs/coleta/uru-1.md`. Commit ainda não feito: aguarda o ok do Guilherme.

1. **Conteúdo:** 126 edições (1900 a 2025), uma por título: "1923 AUF" e "1923 FUF", "1924 AUF" e "1924 FUF" (cisma), "1926"
   (Torneo del Consejo Provisorio), "2005" (Torneo Especial) e "2005/06" a "2015/16" (calendário europeu), "2016" (Transición).
   "1948" não tem campeão (abandonado na greve). "2020" vai até abril de 2021 (`ano_fim` 2021). 12.464 jogos, 81 clubes.
2. **45 edições sem jogos** (1902-1931 fora 1905, 1908 e 1916; 1975-1993): como a "2025 Liga", só `edicoes.csv`,
   `classificacao_final.csv` (a tabela final da RSSSF) e `tabelas_publicadas.csv`; `formato` = "sem jogos (só a tabela final)".
   Nenhuma fonte pública tem os jogos desses anos. **Pedido:** o painel mostrar a classificação delas sem esperar jogos.
3. **Fases:** Apertura, Intermedio e Clausura não dão título; são fases da edição ("Apertura", "Final do Apertura",
   "Intermedio" com grupos A e B, "Final do Intermedio", "Clausura"...), depois "Semifinal" e "Final" do campeonato.
4. **País:** `pais` "URU" e `pais_nome` "Uruguai" no `competicao.json`; todos os clubes são `URU`.
5. **Nomes:** nenhuma colisão com o banco ou com outro pacote. Homônimos levam a cidade: "Liverpool de Montevideo", "Racing de
   Montevideo", "River Plate de Montevideo" (o atual, de 1932) e "River Plate FC" (o amador, até 1929), "Colón de Montevideo",
   "Belgrano de Montevideo", "Universal de Montevideo", "Albion de Montevideo", "Libertad de Montevideo", "Olimpia de
   Montevideo", "Juventud de Las Piedras", "Atenas de San Carlos". "Nacional" é o uruguaio. C.U.R.C.C. (1900-1913) entra como
   "Peñarol", como a RSSSF conta (o `nomes_fonte` guarda "rsssf:C.U.R.C.C."). Defensor = "Defensor Sporting"; Deutscher/Teutonia
   = "Montevideo FC"; Torque = "Montevideo City Torque".
6. **Escudos:** calendários do ogol em `data/cache/ogol-uru-1/calendario_<ano_inicio>_<id>_p<n>.html` (2005/06 em diante; as
   edições anteriores do ogol vêm vazias), conferidos pelo link canônico; `nomes_fonte` com `ogol:<grafia>:<anos>`.
7. **Jogos da Wikipédia:** 1900, 1901, 1905, 1908, 1916, 1960-1964 e 1966-1974 vêm da Wikipédia em espanhol (`fonte`
   "Wikipédia (es)", `fonte_id` "wikipedia:es_<ano>:<linha>"), sem autores dos gols.
8. **`resultado_especial`:** como no `arg-1`. Vitória dada pelo tribunal com os gols de campo mantidos ("awarded win to X;
   goal records unchanged") fica `awd` sem placar, com o placar de campo e o vencedor na `observacao`.

## Resposta do agente 1 (21/11/2026): Uruguaio no banco e no painel

- **Carregado:** `uru-1` com 126 edições e 12.464 jogos. Títulos: Peñarol 54 e Nacional 50.
- **1948 sem campeão:** a conferência acusava diferença ("vazio" contra "nenhum"); corrigido no carregador.
- **Edições sem jogos (45):** o painel mostra a tabela publicada, como na "2025 Liga". Elas ficam fora de "Edição com
  menos jogos" e do gráfico de gols por jogo.
- **Escudos:** os clubes de 2005 em diante têm escudo. Faltam 47 clubes da era amadora, que o ogol não cobre.
- **Lista do painel:** o painel só mostra a competição que está em `LIBERADAS` (`gerar_dashboard_v2.py`), com o ok do
  Guilherme.

## 21/11/2026 — Campeonato Chileno, 1ª divisão (`chi-1`)

Pacote em `data/coleta/chi-1/pacote/` e relatório em `docs/coleta/chi-1.md`. Commit ainda não feito: aguarda o ok do Guilherme.

1. **Conteúdo:** 109 edições (1933 a 2025), uma por torneio que deu título: anuais até 1996, 1998-2001, 2010 e 2018-2025;
   "1997 Apertura" e "1997 Clausura"; "2002 Apertura" a "2012 Clausura" (sem 2010); "2013 Transición"; "2013/14 Apertura" a
   "2016/17 Clausura"; "2017 Transición". "2020" vai até fevereiro de 2021 (`ano_fim` 2021). Como no `arg-1`, o torneio aparece
   depois do primeiro espaço da `temporada`. 22.601 jogos, 53 clubes.
2. **Fontes dos jogos:** RSSSF (1933-1983, 1996-2024); ogol (1984-1995 e 2025, `fonte` "ogol", `fonte_id` "ogol:<id>");
   ESPN (fase de pontos corridos do Clausura 2011 e de 2012, `fonte` "ESPN", `fonte_id` "espn:<id>"). Gols com minuto e
   cartões da ESPN de 2005 a 2025.
3. **País:** `pais` "CHI" e `pais_nome` "Chile" no `competicao.json`; todos os clubes são `CHI`.
4. **Nomes:** nenhuma colisão com o banco ou com outro pacote. Homônimos levam a cidade: "Everton de Viña del Mar" (o Everton
   do eng-1), "Rangers de Talca", "Naval de Talcahuano", "Metropolitano de Santiago". Green Cross (Santiago), Green Cross-Temuco
   e Deportes Temuco são um cadastro só ("Deportes Temuco"), como a RSSSF conta o título de 1945.
5. **Escudos:** calendários do ogol em `data/cache/ogol-chi-1/calendario_<ano>_<id>_p<n>.html` (1933-2001, 2010, 2018-2025;
   o ogol não tem Apertura e Clausura de 2002-2017 no menu da liga), conferidos pelo link canônico.
6. **Fases novas:** "Metropolitano", "Provincial", "Promocional" e "Nacional" (1968-1970), "Segunda fase", "Terceira fase",
   "Repechaje", "Fase final", "Grupo do rebaixamento". Zonas de 1984 em `grupo` ("Norte", "Sul").
7. **`resultado_especial`:** como no `arg-1` e no `uru-1`.

## Pedidos da revisão (21/11/2026): Uruguaio (`uru-1`)

A revisão conferiu o pacote contra a Wikipédia (es e en), a RSSSF e a ESPN. Os achados estão em `docs/revisao/achados.csv`
(prefixo UY, `quem_corrige` = `coleta-sulamerica`) e as provas em `docs/revisao/uru-1.md`.

1. **Classificação final de 1994 a 2025 (alta):** UY-006. Em 28 edições, a classificação é só a tabela do Apertura, com o campeão
   puxado para o 1º lugar. Exemplos: em 2025 o Peñarol, finalista, aparece em 4º; em 2023 o Racing aparece em 14º e foi 6º na
   tabela anual. Por isso o vice está errado em 14 edições (UY-004) e o 3º em 19 (UY-005).
2. **1948 (média):** UY-003. A edição não tem campeão, mas tem o Peñarol como vice.
3. **Jogos e datas (média):**
   - UY-013: 8 jogos da Supercopa AUF (2018 a 2025) entraram como "Final" do campeonato;
   - UY-014: as decisões herdam a data do jogo anterior (a final de 2025 aparece em 16/11, mas foi jogada em 23/11 e 30/11);
   - UY-015: em 2020, o Apertura e o Intermedio estão em 2021;
   - UY-010: o W.O. de 1908 foi dado ao Intrépido;
   - UY-011 (1951) e UY-016 (31 placares).
4. **Vices e tabelas antigas:** UY-007 (1954, aguarda decisão), UY-008 (1947) e UY-012.
5. **Artilheiros:** UY-017 (de 2013/14 a 2025 vêm só dos gols com autor), UY-018 e UY-019.
6. **Aguardam decisão do Guilherme:**
   - UY-001: 1923 FUF, 1924 FUF e 1926 contam como título? A AUF não os reconhece;
   - UY-020: o "Atlético Wanderers" da FUF é o Montevideo Wanderers? A mesma pergunta vale para Lito e Charley;
   - UY-007: o vice de 1954.
7. **Nome:** UY-023, um nome de clube com texto de jogador grudado ("Peñarol (59' Juan Martín Parodi...").

Quando corrigir, cite os ids aqui. A revisão confere de novo.

## Pedidos da revisão (21/11/2026): Argentino (`arg-1`)

A revisão conferiu o pacote contra a Wikipédia (es e en). Os achados estão em `docs/revisao/achados.csv` (prefixo AR,
`quem_corrige` = `coleta-sulamerica`) e as provas em `docs/revisao/arg-1.md`.

1. **Campeão errado no painel (alta):** AR-001. Em 1913 Federación, os jogos do Estudiantes de La Plata estão gravados como
   Estudiantes de Buenos Aires. O clube errado sai campeão, o cartão diz "29 campeões" (são 28) e o Estudiantes de La Plata fica
   com 6 títulos (são 7).
2. **Vice errado em 12 edições (alta):** AR-002 a AR-013. Casos:
   - 1976 Nacional: aparece o Talleres; foi o River, que jogou a final;
   - 1987/88: San Lorenzo, não Racing;
   - 1989/90: Independiente, não Rosario Central (faltam punições);
   - 2008/09 Apertura: Tigre, não San Lorenzo;
   - amadorismo, em tabelas calculadas sem os W.O., com jogos anulados ou faltando: 1895, 1896, 1912, 1913 Federación, 1919 (as
     duas ligas) e 1926 (as duas). O 1926 Amateurs tem só 43 dos 325 jogos.
3. **Classificação e jogos (alta e média):**
   - AR-016: em 1949 há um jogo "Gimnasia La Plata 1-0 Gimnasia La Plata";
   - AR-014 e AR-018: jogos que faltam (1997/98 Apertura; 2016/17, onde há 446 de 450);
   - AR-015, AR-017 (1988/89 com 3 pontos por vitória), AR-019, AR-020 e AR-021 (rebaixados que faltam).
4. **Datas (média):**
   - AR-022: cerca de 3.920 jogos de 26 edições estão com o ano errado. O 2018/19 vai de 10/08/2019 a 10/12/2020, mas foi
     jogado de agosto de 2018 a abril de 2019; o 1931 Liga cai em 1932; metade de 1937 cai em 1939. A lista está em
     `revisao/AR/datas_ano_lista.txt`;
   - AR-023: data copiada de outro jogo, com ida e volta no mesmo dia;
   - AR-024: datas que não existem (2005-09-31 e 2021-02-29).
5. **Fases (média):** AR-025 ("Desempate do título" errado) e AR-026 ("Final" com jogos de outra disputa).
6. **Artilheiros:** AR-027 a AR-030.
7. **Clubes:** AR-031 (Atlético Cipolletti duplicado com o Cipolletti) e AR-034 (nomes colados no `nomes_fonte`).
8. **Aguardam decisão do Guilherme:**
   - AR-044: o título de 1891 (só o Saint Andrew's ou dividido com o Old Caledonians);
   - AR-043: o Apertura 2026;
   - AR-032: o Quilmes de 1893 a 1895;
   - AR-033: as fusões de 1934;
   - a Copa de Oro de 1936.

Quando corrigir, cite os ids aqui. A revisão confere de novo.

## 21/11/2026 — Campeonato Colombiano, 1ª divisão (`col-1`)

Pacote em `data/coleta/col-1/pacote/` e relatório em `docs/coleta/col-1.md`. Commit ainda não feito: aguarda o ok do Guilherme.

1. **Conteúdo:** 101 edições (1948 a 2025): anuais até 2001 ("1995/96" e "1996/97" no calendário europeu; "1989" sem
   campeão, fase final suspensa), depois "2002 Apertura" e "2002 Finalización" até "2025 Finalización" (em 2020 só o
   Apertura). 22.788 jogos, 42 clubes. Até 2001 o Apertura, o Finalización, os quadrangulares e os hexagonais/octogonais
   finais são fases da edição anual.
2. **6 edições sem jogos** (1987, 1991-1995), como no `uru-1`: só `edicoes.csv`, `classificacao_final.csv` e
   `tabelas_publicadas.csv`.
3. **Fontes:** RSSSF (1995/96 em diante, menos 2011, 2012 e 2025); Wikipédia em espanhol (1948-1986, 1988-1990, 2011, 2012
   e 2025: `fonte` "Wikipédia (es)", `fonte_id` "wikipedia:es_<chave>:<linha>"); ESPN (gols com minuto e cartões, 2005 em
   diante).
4. **País:** `pais` "COL" e `pais_nome` "Colômbia" no `competicao.json`; todos os clubes são `COL`.
5. **Nomes:** nenhuma colisão. Homônimos levam a cidade: "Libertad de Barranquilla", "Universidad Nacional de Bogotá",
   "Boca Juniors de Cali", "Huracán de Medellín". Deportes Caldas (campeão de 1950) entra como "Once Caldas", como a RSSSF;
   Atlético Municipal = "Atlético Nacional"; Cristal Caldas = "Once Caldas"; Itagüí = "Águilas Doradas"; La Equidad =
   "Internacional de Bogotá"; Alianza Petrolera = "Alianza FC".
6. **Escudos:** o ogol tem as edições colombianas vazias (sem calendário de jogos): não há páginas de calendário para os
   escudos. A ESPN (`data/cache/espn-sulamerica/col.1/`) traz os ids dos clubes de 2005 em diante.
7. **Fases novas:** "Quadrangulares semifinais" (grupos A e B), "Quadrangular final", "Hexagonal final", "Octogonal final",
   "Pentagonais", "Triangulares", "Finalísima", "Copa Mustang I/II", "Torneo Mustang I/II", "Copa de la Paz", "Torneo Nacional".

## 21/11/2026 — Campeonato Paraguaio, 1ª divisão (`par-1`)

Pacote em `data/coleta/par-1/pacote/` e relatório em `docs/coleta/par-1.md`. Commit ainda não feito: aguarda o ok do Guilherme.

1. **Conteúdo:** 133 edições (1906 a 2025): anuais até 2007 (sem 1908, 1922, 1932-1934; de 1996 a 2007 Apertura e Clausura
   são fases), depois "2008 Apertura" e "2008 Clausura" até "2025 Clausura". 7.810 jogos, 41 clubes.
2. **76 edições sem jogos** (1906-1959, 1968-1980, 1982-1995): nenhuma fonte pública tem os jogos. Decisão do Guilherme:
   entram só com campeão, vice e tabela quando há. **Novidade para o painel:** a `classificacao_final.csv` dessas edições
   pode ser **parcial**: só `posicao`, `clube` e `pontos` (às vezes parte da campanha), com `fonte` "RSSSF (parahist, tabela
   parcial)"; sem tabela nenhuma (19 edições), só o campeão (1º) e o vice (2º), com `fonte` "lista de campeões e vices da
   RSSSF (parachamp.html)" e as colunas numéricas vazias. `num_clubes` nessas edições é o número de linhas conhecidas.
   **Pedido:** o painel aceitar colunas vazias na classificação e não somar essas edições nos totais de jogos e gols.
3. **País:** `pais` "PAR" e `pais_nome` "Paraguai"; todos os clubes são `PAR`.
4. **Nomes:** nenhuma colisão (conferido também sem acentos). "Nacional de Asunción" (o Nacional é o uruguaio), "River
   Plate de Asunción", "Sportivo San Lorenzo", "Independiente de Campo Grande", "Universal de Encarnación" e "Guaraní de
   Asunción" (para não se confundir com o Guarani de Campinas). "Olimpia" fica sem cidade.
5. **Escudos:** não há calendários do ogol (o ogol só tem jogos paraguaios de 2005 em diante e não entrou); a ESPN
   (`data/cache/espn-sulamerica/par.1/`) traz os ids dos clubes de 2005 em diante.
6. **Fases novas:** "Liguilla" (fecho do Apertura/Clausura em 1998-1999).

## Resposta do agente 1 (21/11/2026): Chileno, Colombiano e Paraguaio no banco e no painel

- `chi-1`, `col-1` e `par-1` carregados e liberados no seletor (América do Sul). Os três no site.
- Edições sem jogos (`uru-1`, `col-1`, `par-1`): o painel mostra a classificação sem esperar jogos; jogos, gols e
  média ficam com "—".
- Tabela parcial do `par-1`: as linhas sem campanha mostram os pontos publicados e "—" nas demais colunas; o pódio
  mostra os pontos no lugar de V/E/D. Essas linhas não somam jogos nem gols.
- Escudos da Colômbia e do Paraguai: `baixar_escudos.py --ogol` agora procura também na ESPN (nomes `espn:` do
  nomes_fonte e os placares em `data/cache/espn-*/`), gravando em `data/escudos/espn_auto.json`.
- Aviso do carregador no `par-1`: o artilheiro de 1979 Edgar Ozuna joga pelo "Capitan Figari", que não está no
  clubes.csv, e ficou sem clube. Se quiser, inclua o clube no cadastro (ele não precisa ter jogos).

## 21/11/2026 — Campeonato Peruano, 1ª divisão (`per-1`)

- Pacote em `data/coleta/per-1/pacote/`, relatório em `docs/coleta/per-1.md`, código em `coleta/per-1/`.
- **109 edições**, uma por título, de 1912 a 2025 (sem campeonato de 1922 a 1925 e em 1936). Apertura, Clausura,
  Torneo de Verano, Regional, liguillas e finais são fases da edição anual. 17.316 jogos, 147 clubes, 20.222 gols com
  autor, 20.999 cartões, 100 artilheiros, 2.551 linhas de tabelas publicadas.
- **Decisão para o agente 1: 1912-1921 (Liga Peruana de Football).** A RSSSF lista esses campeões à parte e não os soma;
  a Wikipédia em inglês os conta como títulos nacionais (numera a partir de 1912). Entraram como 10 edições só com campeão
  e vice (da Wikipédia). Se preferir a contagem da RSSSF, basta tirar essas edições.
- **Sem jogos (18 edições):** 1912-1921, 1970-1974, 1976, 1977 e 1979. De 1970 em diante entram com a tabela final da
  RSSSF (`peruhist.html`), marcada como sem conferência (como no `uru-1`).
- **Jogos incompletos** (dito na observação da edição): 1926 (torneio suspenso), 1982, 1984, 1986, 1988-1991 (anos de
  Regional + Descentralizado, a RSSSF tem só tabelas de parte das fases) e 2003 (rodadas 16 e 17 do Clausura, jogadas
  com sub-20 na greve, anuladas como nas tabelas).
- **Fontes:** RSSSF é a base (1930-1942, 1968-1969, 1975, 1978, 1980-1981, 1983-1984 e 1986 em diante); Wikipédia em
  espanhol dá os jogos de 1926-1929, 1943-1967, 1982 e 1985 (fonte `Wikipédia (es)`, `fonte_id` `wikipedia:es_<ano>:<linha>`;
  quase sempre tabela de confrontos, sem rodada nem data); ESPN (`per.1`, 2005 em diante) casou 6.418 jogos (hora,
  estádio, gols com minuto, cartões). O ogol não tem jogos peruanos.
- **Conferência:** 52 edições batem com as tabelas publicadas, 38 têm divergência explicada no relatório (quase sempre
  placar ou gols que a própria página não fecha) e 19 não têm com o que conferir. Campeões e vices batem com a
  Wikipédia em inglês nas 109 edições.
- **Clubes:** sem homônimos no banco nem nos outros pacotes. Mesmo clube com nome antigo fica com o atual: Federación
  Universitaria = Universitario, Sport Alianza = Alianza Lima, Real Garcilaso = Cusco FC, Inti Gas = Ayacucho, Total Clean =
  Total Chalaco, Grau-Estudiantes (2004) = Estudiantes de Medicina. Aurich-Cañaña (fusão 1994-1996) é clube à parte.
  Deportivo Bancos (1991, um jogo) está sem cidade: a fonte não diz.
- **Pontos:** 2 por vitória até 1994, 3 depois; de 1931 a 1942 era 3-2-1 (vitória, empate, derrota) e de 1931 a 1934 a
  tabela soma bônus da liga de reservas. `pontos_vitoria` no edicoes.csv fica 2 nesses anos; a classificação traz os
  pontos publicados.
- **Mudança no leitor comum** (`coleta/comum-sulamerica/rsssf_sul.py`): jogo com sigla no nome ("U.T.C.", "A.D.T") era
  descartado; agora entra. Reimportei Argentina, Uruguai, Chile e Colômbia: pacotes idênticos.
- **Paraguai (`par-1`) atualizado:** (1) o pacote do commit anterior saiu antes de a ESPN de 2016 e 2025 terminar de
  baixar; agora 527 jogos ganham hora, estádio e cidade (nenhum placar muda); (2) o clube do artilheiro de 1979 (Capitán
  Figari, Lambaré) entrou no clubes.csv, como pedido.

## 21/11/2026 — Campeonato Equatoriano, 1ª divisão (`ecu-1`)

- Pacote em `data/coleta/ecu-1/pacote/`, relatório em `docs/coleta/ecu-1.md`, código em `coleta/ecu-1/`.
- **68 edições**, uma por título, de 1957 a 2025 (sem campeonato em 1958 e 1959; em 2005, Apertura e Clausura, uma
  edição cada: `2005 Apertura`, `2005 Clausura`). 14.195 jogos, 63 clubes, 9.240 gols com autor, 15.824 cartões,
  72 artilheiros, 2.069 linhas de tabelas publicadas. Nenhuma edição sem jogos.
- **Até 1967** o nacional era um torneio curto entre os melhores dos regionais (Interandino e Guayaquil); os regionais
  ficaram de fora, como a Serie B, a Copa Ecuador e a Supercopa de 1969.
- **Fontes:** RSSSF é a base de todos os anos (de 1960 a 1974 parte das fases vem em tabela de confrontos, sem rodada nem
  data); ESPN (`ecu.1`) dá os jogos de 2011, 2012 e 2025 (a RSSSF só tem as tabelas e as finais; fonte `ESPN`,
  `fonte_id` `espn:<id>`) e casou 5.145 jogos ao todo (hora, estádio, gols com minuto, cartões; de 2014 a 2020 a ESPN
  quase não tem lances).
- **Conferência:** 47 edições batem com todas as tabelas publicadas; 21 têm divergência, quase sempre de um gol ou de um
  resultado que a própria página não fecha (explicado no relatório). Jogos lidos = jogos esperados nas 68. Campeões e
  vices batem com a Wikipédia em inglês (LigaPro Serie A) nas 68.
- **Clubes:** sem homônimos no banco nem nos outros pacotes. Com cidade: Barcelona de Guayaquil, Universidad Católica de
  Quito, River Plate de Manta (1963, 1966) e River Plate de Riobamba (1987, 1988), que são dois clubes, Libertad de Loja,
  Santos de El Guabo, Juventus de Esmeraldas, Santa Rita de Vinces, América de Quito/Ambato/Manta. Nome atual para o mesmo
  clube: Independiente José Terán = Independiente del Valle, River Ecuador = Guayaquil City, Cuniburo = Vinotinto.
- **Pontos:** 2 por vitória até 1994, 3 depois. As liguillas finais começam com pontos de bônus (`ajuste_pontos`). Em 1998
  o empate ia para os pênaltis (2 pontos para quem ganhava, 1 para quem perdia); a tabela soma os dois tipos de empate.
- **Mudança no leitor comum** (`coleta/comum-sulamerica/rsssf_sul.py`), dois erros antigos: (1) linha de tabela de clube
  com nome que começa por número ("9 de Octubre", "3 de Febrero", "12 de Octubre") não era lida; (2) jogo entre dois
  clubes com nome de data ("3 de Febrero 2-0 12 de Octubre") era lido como linha de data e sumia.
- **Paraguai (`par-1`) e Peru (`per-1`) reimportados por causa disso.** Paraguai: +55 jogos (2005-2014, os jogos entre
  3 de Febrero, 12 de Octubre e 2 de Mayo) e as tabelas publicadas agora trazem esses clubes; as 36 edições que fechavam
  continuam fechando. Os `id` das partidas do par-1 mudaram a partir dos jogos novos (se já estiver no banco, reimportar
  o pacote inteiro). Peru: mesmos jogos (8 jogos de 1991 trocaram de ordem e de `id`) e 1988 com uma divergência a menos.
  Argentina, Uruguai, Chile e Colômbia: pacotes idênticos.
- **Teste de carga (22/11), numa cópia do banco, com `coleta/comum-sulamerica/testar_carga.py`:** os sete pacotes dão
  "-> OK". Ele achou dois erros, já corrigidos:
  - no `per-1`, os clubes das edições de 1912-1921, que só estão na classificação, faltavam no `clubes.csv`. Agora são 153
    clubes;
  - no `par-1`, o "8 de Diciembre" (Caacupé), de 1994, que só aparece em tabela, não tinha cadastro e ficava sem clube.
- **Documentação nova:** `coleta/comum-sulamerica/COMECE-AQUI.md` e `coleta/comum-sulamerica/documentacao/`.

## Recado de fim de coleta — bol-1 — 22/11/2026

Para o agente 1 (banco e painel) e o agente de revisão.

1. **O que foi feito:**
   - 94 edições (1950-2025): os 93 títulos e o Clausura 2022, abandonado e sem campeão;
   - 8.563 jogos, 77 clubes, 13.666 gols com autor, 4.970 cartões, 91 artilheiros;
   - fontes:
     - RSSSF: páginas por ano de 1971, 1977 e 1990 em diante, mais a lista de tabelas finais `bolhist.html` de 1950-1990;
     - Wikipédia em espanhol: 542 jogos de 1950, 1953, 1990, 1991 e das fases finais de outros anos;
     - ESPN `bol.1`: 4.814 jogos casados, de 2005 em diante;
     - Wikipédia em inglês: lista de campeões, vices de 1977 em diante e artilheiros.
   - O ogol não tem jogos bolivianos antigos.
2. **Commit:** `9ed3dcd` (enviado ao GitHub em 22/11).
3. **Teste de carga:** `bol-1: 94 edições, 8563 jogos, 77 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar o `bol-1` (país BOL, Bolívia);
   - temporadas com torneio: "2003 Apertura", "2011/12 Adecuación", "2016/17 Clausura"... e "1957 Mixto" (o Certamen Nacional Mixto 1957/58, título à parte do Torneo Integrado 1957);
   - 22 edições sem jogos e 19 com jogos incompletos:
     - a classificação delas é a tabela da RSSSF;
     - nelas, campeão e vice da lista podem entrar no topo sem campanha (colunas vazias, fonte "lista de campeões");
     - de 1960 a 1964 só há campeão e vice;
   - "2022 Clausura" não tem campeão nem vice;
   - 10 jogos decididos fora de campo (`awd`), 2 não disputados e 1 abandonado.
5. **Decisões:**
   - **escopo de 1950 em diante**, como a Wikipédia (Bolívar com 31 títulos) e os 93 campeonatos da RSSSF. A contagem "84 títulos desde 1958" da RSSSF tiraria 1950-1957. Fica para o Guilherme confirmar;
   - **vice de 1961, 1963, 1964 e 1968:** RSSSF e Wikipédia divergem; ficou o da RSSSF, e em 1968 a tabela dela confirma;
   - **ida e volta numa linha só (1992, 1994):** vira dois jogos, com o mando da volta presumido;
   - **"awarded to X (originally 0-0)":** vira vitória dada a X, com os gols do campo.
6. **O que não deu para coletar:**
   - jogos de 22 anos (1952, 1954-1959, 1961, 1963-1965, 1967, 1969, 1970, 1972-1975, 1980, 1981, 1984): nenhuma fonte pública tem. Poderiam vir de jornais da época ou de um almanaque boliviano (historiadelfutbolboliviano.com);
   - tabela do nacional de 1960-1964;
   - a tabela de confrontos parcial de 1992, que tem células vazias e precisaria de leitura por coluna;
   - lances da ESPN: quase nenhum de 2014 a 2020 e de 2022 a 2025 (nesses anos, os autores dos gols vêm do texto da RSSSF).
7. **Onde a revisão deve olhar primeiro:**
   - a classificação das edições incompletas (1951-1994);
   - os nomes que dependem do ano: "Universitario" sozinho de 1971 a 1994 = Universitario de Potosí; "Litoral" de 1992 (a RSSSF diz [Oruro]) = Litoral de La Paz; "Internacional" de Oruro (1957) e de La Paz (1958-1960);
   - as 10 edições com tabela divergente (1950, 1953, 1977, 1995-1999, 2001, 2002), cada uma explicada no relatório;
   - o vice de 1961, 1963, 1964 e 1968.
8. **Próxima competição:** `ven-1` (Venezuela).

Documentação: `coleta/comum-sulamerica/documentacao/bol-1.md`; relatório: `docs/coleta/bol-1.md`. O leitor comum não mudou.

## 22/11 — agente 1: per-1, ecu-1, par-1 e bol-1 no banco e no painel

- Carregados: per-1, ecu-1, par-1 (recarregado inteiro) e bol-1. Todos "-> OK". Os quatro liberados no seletor (vão ao site
  com o ok do Guilherme). per-1 1912-1921 entrou como está no pacote (decisão do Guilherme ainda em aberto).
- Edições com só parte dos jogos: o painel agora usa a tabela da fonte sempre que ela traz números para algum clube; as
  linhas sem números mostram "—" (só posição e, se houver, pontos). Vale para o bol-1 (1976, 1978, 1979, 1986) e para o
  bra-sp-2.
- Jogos "awd": conferi. Todas as edições com eles trazem a tabela oficial completa, que é a que o painel usa. Nada a mudar.
- **Pedido (bol-1, quando o Guilherme mandar revisar; não para agora):** em 5 edições há clubes com jogos que não estão
  na classificacao_final: 1960 (6 clubes: Internacional de La Paz, San José, Always Ready, Municipal de La Paz, Bolívar,
  Chaco Petrolero), 1976 (Guabirá, Jorge Wilstermann, The Strongest), 1990 (7), 1993 (8) e 1994 (San José, Always Ready,
  Independiente Petrolero). O painel põe esses clubes no fim da tabela, sem posição ("—") e sem números. Melhor seria a
  classificação trazer todos os participantes, como no bra-sp-2 (eliminados com a posição repetida da fase em que caíram).
  O gerador avisa esses casos no log ("aviso: ... fora da classificação final").

## Recado de fim de coleta — ven-1 — 22/11

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul).

1. **O que foi feito:** 1ª divisão venezuelana completa, `ven-1`.
   - **Edições:** 106, uma por título de 1921 (temporada 1920/21) a 2025, como na lista de campeões da RSSSF
     (`venezchamp.html`). O Torneo de Adecuación 2015 entra (a RSSSF conta; a Wikipédia em inglês não).
   - **Pacote:** 13.582 jogos, 108 clubes, 34.193 gols (6.390 com autor), 6.729 cartões e 74 artilheiros.
   - **Fontes:** RSSSF como base; ESPN para hora, estádio, público e lances de 2005 em diante, e para os jogos do
     Clausura 2011, de 2011/12 e de 2025.
   - **Conferência:** 48 edições fecham com as tabelas publicadas; 23 divergem, com explicação no relatório; 35 não têm
     o que conferir (7 sem jogos e 28 incompletas).
   - Os 106 campeões batem com a Wikipédia. Os vices também, menos 1966 e 1975 (ficou o da RSSSF).
   - **Documentação:** `coleta/comum-sulamerica/documentacao/ven-1.md` e o README atualizados; COMECE-AQUI atualizado
     (inclui as armadilhas da Venezuela); relatório em `docs/coleta/ven-1.md`.
2. **Commits:** `35dc0a2` (pacote, código, documentação e este recado) e o commit seguinte, com o hash no guia.
   - O leitor comum (`rsssf_sul.py`) **não mudou**: nenhuma outra liga muda e nenhum id de partida muda.
   - No `documentar.py`, só saíram das pendências as linhas "ainda não carregado" (per-1, ecu-1, bol-1) e o "recarregar"
     do par-1, como no recado do agente 1 de 22/11.
3. **Teste de carga:** `ven-1: 106 edições, 13582 jogos, 108 clubes novos -> OK`. Na primeira rodada, dois artilheiros com
   dois clubes ("Estudiantes/Carabobo FC") ficaram sem clube; agora fica o último clube e os dois vão na fonte.
4. **Pedidos ao banco e ao painel:**
   - Carregar o `ven-1`.
   - **Edições incompletas:** a era amadora e 1993/94 e 1994/95. Na era amadora, a classificação costuma ser só campeão e
     vice; em 1993/94 e 1994/95, é a tabela da liga. Há clubes com jogos fora da classificação (o mesmo caso do pedido
     de 22/11 para o `bol-1`); trato junto quando o Guilherme mandar.
   - **Nomes com o ano entre parênteses:** "Anzoátegui FC (1967)" e "Aragua FC (1966)". São clubes extintos com o mesmo
     nome de clubes atuais.
5. **Decisões:**
   - **Tomadas por mim (explicadas no relatório e em `clubes_ven.py`):**
     - Adecuación 2015 conta como edição.
     - Clube que muda de cidade fica separado, salvo quando a lista de campeões da RSSSF junta. Por isso Nacional Táchira
       e UD Lara são clubes diferentes, e Atlético Monagas e Monagas SC também.
     - Mesmo clube: Unión Atlético Táchira = Deportivo Táchira; ItalChacao e Deportivo Petare = Deportivo Italia;
       Internacional de Lara (1998/99) = Trujillanos.
     - 1940: um quarto Español x Loyola foi descartado (a tabela fecha sem ele).
     - Dois placares da ESPN corrigidos pela tabela da RSSSF: o "15-0" de 2011 vira 3-0, e um 0-0 vira W.O. de 3-0.
   - **Para o Guilherme:** o Atlético Zulia (1996/97 e 1997/98) entrou como **Universidad de Los Andes**, como na lista de
     campeões da RSSSF. A página da temporada 1996/97 diz que ele era o **Unicol**. A escolha muda de dono o título de
     1997/98.
6. **O que não deu para coletar:**
   - **Era amadora:** 7 anos sem página (1922, 1924, 1931, 1938, 1939, 1949 e 1950) e 26 com jogos parciais ou só o
     campeão. Fontes que resolveriam: jornais de Caracas (El Universal, La Esfera) ou o livro de Eliézer Pérez, autor das
     páginas da RSSSF.
   - **1993/94 e 1994/95:** o Apertura (Copa Venezuela) de 1993/94 e o Torneo Iniciación de 1994/95 só têm tabelas. Faltam
     ainda 8 placares da liga de 1993/94 e 5 "drw" (empate sem placar) de 1994/95.
   - **Quatro jogos que nenhuma fonte traz:** 1992/93 Lara x Zamora; Clausura 2011 Caroní x Zulia; Apertura 2011 Mineros x
     Zamora e Carabobo x Aragua. A tabela final da RSSSF dá o resultado de cada um; as páginas das temporadas na
     Wikipédia em espanhol podem confirmar.
   - **Artilheiro de 2015:** a lista da RSSSF vai até 2007/08, e a Wikipédia não tem a linha da Adecuación.
7. **Onde a revisão deve olhar primeiro:**
   - a identidade dos clubes em `clubes_ven.py`: Atlético Zulia, as três "Lara", as quatro "Anzoátegui", Monagas;
   - 2000/01: "Monagas" trocado por "Atl Monagas" só na 1ª fase, em `linhas()`;
   - as fases de 1994/95 (Apertura, Iniciación, Torneo Nacional e Finalización);
   - "Championship Playoff", que vira grupo final ou final conforme tenha "Final Table";
   - as temporadas da ESPN (2010/11, 2011/12 e 2025): fase por data, em `espn_fases`;
   - o corte da era amadora no primeiro título "Copa ...".
8. **Próxima competição:** as 1ªs divisões da América do Sul acabaram. Depois vêm as 2ªs divisões, na ordem do guia geral,
   quando o Guilherme pedir.

Documentação: `coleta/comum-sulamerica/documentacao/ven-1.md`; relatório: `docs/coleta/ven-1.md`.

## Revisão profunda (22/11/2026)

- **174 ids abertos** para a coleta América do Sul; **52 altos**; **37 no ar** (Argentino 14, Chileno 9, Colombiano 6,
  Paraguaio 5, Uruguaio 3).
- Competições: Argentino 41, Chileno 26, Paraguaio 24, Colombiano 22, Peruano 22, Uruguaio 21, Equatoriano 18.
- Plano pronto, em ordem e por arquivo do código: `docs/revisao/plano-coleta-sulamerica.md`. Começar só quando o
  Guilherme mandar.
- Decisões que esperam o Guilherme: `docs/revisao/decisoes-guilherme.md`. Fontes: `docs/revisao/fontes.md`.

## Decisões do Guilherme (22/11/2026), da revisão profunda

O Guilherme respondeu às decisões D-01 a D-25 de `docs/revisao/decisoes-guilherme.md`:
- **D-01:** opção A. Tudo o que já terminou entra agora, inclusive o Paulista 2026 e os Aperturas 2026 da Argentina e do
  Paraguai.
- **D-10:** opção B. As edições não oficiais das Séries B e C entram com aviso, sem contar título (SB-026, SC-029, TL-005).
- **As outras:** vale a recomendação de cada uma.

Os ids que esperavam essas decisões estão liberados no seu plano. As correções continuam esperando a largada do Guilherme.

## 23/11 — Correções da revisão: Argentino (`arg-1`)

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul), por ordem do Guilherme (23/11).

- **Corrigidos:**
  - **Campeão e pódio:** AR-001, AR-002 a AR-013 (vice e 3º pela lista oficial; tabela publicada onde os jogos não
    fecham), QU-001, AR-014, AR-015, AR-016, AR-017.
  - **Datas:** AR-022 (3.487 das 3.495 datas da lista da revisão, mais o desempate de 1937 em 1939 pelo QU-002) e AR-024.
  - **Fases:** AR-025 e AR-026.
  - **Jogos:** AR-018 (4 jogos da ESPN em 2016/17) e AR-034. A página de 1926 tinha um `<PRE>` por linha; o 1926 Amateurs
    passou de 43 para 325 jogos, e o 1926 Asociación também ganhou jogos.
  - **Artilheiros:** AR-027 a AR-030.
  - **Clubes:** AR-031 (Atlético Cipolletti = Cipolletti), AR-032 (Quilmes Club e Quilmes Rovers à parte) e AR-033
    (Atlanta-Argentinos Juniors à parte).
  - **Edição nova:** AR-043, o Apertura 2026 (Belgrano campeão, River vice).
  - **Sem mudança:** AR-019 (a es conta os gols de campo de dois jogos com placar dado) e AR-044 (o pacote já tinha só o
    Saint Andrew's em 1891).
- **Abertos:**
  - AR-020: 1929, W.O. que dão pontos na tabela do grupo;
  - AR-021: rebaixados por lista;
  - AR-023: leitor comum, junto com as outras ligas no fim;
  - QU-003: ESPN pelo par de clubes nos jogos adiados;
  - QU-005: datas do Boca, que só se resolvem com uma 3ª fonte.
- **Números:** 197 edições, 43.726 jogos, 173 clubes. Teste de carga: `arg-1: 197 edições, 43726 jogos, 3 clubes novos -> OK`.
  - Mais gols com minuto e cartões da ESPN: com as datas certas, mais jogos casaram.
  - 146 edições fecham com as tabelas.
- **Pedido ao agente 1:** recarregar o `arg-1` inteiro. Os ids das partidas mudam: há jogos novos em 1926 e 2016/17,
  jogos que saíram em 1913, 1919 e 1929, e outra ordem em várias edições. Os 3 clubes novos são Quilmes Club, Quilmes
  Rovers e Atlanta-Argentinos Juniors.
- **Commit:** `30f0b00`.
- **O leitor comum (`rsssf_sul.py`) não mudou.**
- **Também neste commit:** a pesquisa das copas nacionais (`coleta/comum-sulamerica/copas-nacionais.md`). As copas são o
  próximo trabalho depois das correções, por pedido do Guilherme.

## 23/11 — Correções da revisão: Uruguaio (`uru-1`)

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul).

- **Corrigidos:**
  - **Classificação e pódio:**
    - UY-006: de 1994 em diante, a classificação é a tabela anual (ex.: 2025 Nacional 79, Peñarol 78, Liverpool 65).
    - UY-004 e UY-005: vice e 3º pela lista da AUF (Wikipédia em inglês).
    - UY-003 e UY-008: 1948 e 1947 sem vice (D-22 c).
    - UY-011: 1951 pela tabela publicada.
    - UY-001: 1923 FUF, 1924 FUF e 1926 ficam sem campeão, com nota (D-09).
    - UY-007: o vice de 1954 fica Nacional (D-22 b).
  - **Jogos:**
    - UY-013: os 8 jogos da Supercopa saíram da "Final".
    - UY-010: W.O. de 1908 para o Bristol.
    - UY-015: 2020 no ano certo (o Apertura começa em 15/02/2020).
    - QU-006: mês trocado no Clausura de 2006.
  - **Clubes:**
    - UY-020: Atlético Wanderers, Lito e Charley da FUF à parte dos da AUF (D-25 f).
    - UY-023: o nome do Peñarol com os autores de 1996.
  - **Artilheiros:**
    - UY-017 e QU-008: artilharia oficial da AUF, 2013/14-2025.
    - UY-018: 1900-1931 pela coluna "Goleador" da es (novo `coleta/uru-1/goleadores_es.py`).
    - UY-019: três grafias.
  - **Só registrados (sem mudança):** UY-012 e UY-016 (fica a RSSSF), UY-028 e QU-007 (não são erro).
- **Aberto:** UY-014, a data das decisões no título da fase. A mudança é no leitor comum e fica para o fim, junto com as
  outras ligas.
- **Números:** 126 edições, 12.456 jogos, 84 clubes. Teste de carga: `uru-1: 126 edições, 12456 jogos, 3 clubes novos -> OK`.
- **Pedido ao agente 1:** recarregar o `uru-1` inteiro.
  - Os ids das partidas mudam: saíram os 8 jogos da Supercopa, e as datas de 2020 e de 2006 mudaram.
  - Os 3 clubes novos são Atlético Wanderers, Lito (FUF) e Charley (FUF).
  - Peñarol passa a 52 títulos e Wanderers a 3: as três edições sem campeão.
- **Commit:** `31c14b0`.
- **O leitor comum (`rsssf_sul.py`) não mudou.**

## 23/11 — Correções da revisão: Chileno (`chi-1`)

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul).

- **Corrigidos:**
  - **CH-001:** a coluna de bônus (1979-1983, 1988, 1989) era lida como pontos ou gols. O leitor do Chile põe o bônus numa
    nota, e o pacote fica com os pontos certos e o bônus em `ajuste_pontos` (ex.: 1981 Colo Colo 48, ajuste +2).
  - **Vice pela lista oficial:** CH-002 a CH-008 (1944 Audax, 1955 e 1982 Colo Colo, 1968 U. Católica, 1984 Cobresal, 1985
    Everton, 2016/17 Ap Iquique).
  - **Tabela publicada como classificação em 14 edições:** CH-003 (1954 e 1955, grupo final + grupo do rebaixamento),
    CH-004 (1968, Nacional), CH-005, CH-007, CH-009, CH-015, CH-016 e CH-019.
  - **Jogos:**
    - CH-002: clube trocado em 1943, 1944, 1953 e 1972;
    - CH-013: 7 placares de 1990-1995;
    - CH-014: 1988, Naval 1-1 O'Higgins no lugar do jogo repetido;
    - CH-015: 2011 Ap, Ñublense 2-0 Wanderers, decisão revogada.
  - **Fases:**
    - CH-008: as liguillas Pré-Sul-Americana/Libertadores de 2015/16 a 2017 saíram;
    - CH-009: desempates do título de 1997 Ap e 2013/14 Ap;
    - CH-016: desempates do rebaixamento de 1971 e 1977.
  - **Outros:**
    - CH-010: "rebaixado" só com "Relegated";
    - CH-011: 2020 no ano certo, com a ESPN casada de novo;
    - CH-018: artilheiros de 1936, 1937 e 1947;
    - CH-024: cidade La Serena;
    - CH-025: clube sem jogo fora da classificação.
  - **Clubes (D-25):**
    - Green Cross de Santiago (1933-1964, campeão de 1945) à parte do Deportes Temuco. O nome leva a cidade por causa do
      Green Cross de Manta, do Equador.
    - Deportes Arica = San Marcos de Arica.
  - **Bug antigo:** no `coleta/chi-1/ler_rsssf.py`, três `\b` tinham virado o caractere de backspace. Os títulos "Second
    Stage" e "Third Stage" nunca eram reconhecidos; agora são.
- **Abertos:**
  - CH-006: 3º e 4º de 1984;
  - CH-012: datas dos mata-matas, no leitor comum, no fim;
  - CH-017: gols com autor a mais;
  - CH-022: grupos herdados;
  - CH-023: 7 datas do ogol de 1969;
  - CH-028: baixar de novo o calendário do ogol;
  - CH-014 (parte de 1986): precisa de uma 3ª fonte.
- **Números:** 109 edições, 22.586 jogos (15 a menos: as liguillas), 53 clubes. Teste de carga: `chi-1: 109 edições,
  22586 jogos, 1 clubes novos -> OK`.
- **Pedido ao agente 1:** recarregar o `chi-1` inteiro.
  - Os ids mudam: saem as liguillas, e as datas de 2020 mudam.
  - O clube novo é o Green Cross de Santiago, com o título de 1945; o Deportes Temuco perde esse título.
  - O "Deportes Arica" vira San Marcos de Arica.
- **Commit:** `209641e`.
- **O leitor comum (`rsssf_sul.py`) não mudou.**

## 23/11 — Correções da revisão: Colombiano (`col-1`)

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul).

- **Corrigidos:**
  - **Classificação e pódio:**
    - CO-001: vice pela coluna "Runners Up" da colchamp; os 101 batem;
    - CO-002 (D-02 A): com fase final, a ordem é a da fase alcançada e, dentro dela, os pontos da campanha toda;
    - CO-003 e CO-019: 1987 e 1991-1995 pela tabela final da página, só com a Primera A (1995 com 16 clubes);
    - CO-007: 43 rebaixados pela Wikipédia em espanhol (novo `coleta/col-1/rebaixados_es.py`). O Pereira de 1997 fica
      marcado no 1996/97 (D-18 b).
  - **Jogos:**
    - CO-005: 1964 sem a matriz repetida (311 jogos);
    - CO-021: dois jogos suspensos repetidos.
  - **Fases:**
    - CO-011: Finalización e quadrangulares como fases de pontos, não mata-mata;
    - CO-014: as finais do Apertura (1974, 1976, 1979, 1980, 1982) e a do Clausura de 1999 em nível 0.
  - **Datas:** CO-010, a final de 1957 em 1958 e o desempate de 1971 em 1972.
  - **Artilheiros:** CO-017 (parte), 1971 (Lóndero e Paniagua), 1977 e 1978.
- **Abertos:**
  - CO-004 e CO-006: ler as 4 voltas e as listas "Fecha N" da Wikipédia (1955-1966, 1976, 1986, 1988, 1989). É uma
    mudança grande no leitor da Wikipédia.
  - CO-008: datas dos mata-matas, no leitor comum, no fim.
  - Também: CO-009, CO-012, CO-013, CO-015, CO-016, CO-017 (2008 em diante), CO-018, CO-020 e CO-022.
- **Números:** 101 edições, 22.512 jogos, 42 clubes. Teste de carga: `col-1: 101 edições, 22512 jogos, 0 clubes novos -> OK`.
- **Pedido ao agente 1:** recarregar o `col-1` inteiro. Os ids mudam: saem os jogos repetidos de 1964 e os suspensos.
- **Commit:** `b8d739d`.
- **O leitor comum (`rsssf_sul.py`) não mudou.**

## 23/11 — Correções da revisão: Paraguaio (`par-1`)

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul).

- **Corrigidos:**
  - **Pódio:**
    - PY-001 e PY-002: campeão e vice da lista sempre em 1º e 2º, com a linha inserida, sem campanha, quando faltam
      (1917, 1928, 1936, 1991...);
    - PY-028 (D-22 a): nos anos com dois vices na lista fica o da es (1926 River Plate; 1927, 1952 e 1953 Libertad; 1964
      Nacional).
  - **Tabelas e classificação:**
    - PY-003: as tabelas parciais de parahist vêm inteiras (antes paravam no 1º clube empatado), com 8 clubes antigos
      novos no cadastro;
    - PY-004: em 1982-1995, só 1986 e 1994 têm a tabela da temporada; nos outros anos, campeão e vice (não mais a tabela
      de uma fase).
  - **Jogos:**
    - PY-005: os torneios de pré-temporada de 1962-1966 saíram (152 jogos);
    - PY-007: o que não é do campeonato em 2000, 2004 e 2005 também saiu (inclusive a final da Intermedia de 2005);
    - PY-029: General Caballero x Libertad de 2005 (W.O. com os gols de campo);
    - PY-010: o "awarded as a win to" de 1960.
  - **Fases e situação:**
    - PY-006: desempate do 11º lugar como "Desempate do rebaixamento";
    - PY-011: "Relegation Playoff" não é queda.
  - **Clubes:**
    - PY-013 (D-25 c): Pettirossi de Encarnación à parte do Silvio Pettirossi;
    - PY-014 (D-25 d): Cerro Porteño de Ciudad del Este = Cerro Porteño PF;
    - PY-015: 8 de Diciembre em Caaguazú.
  - **ESPN:**
    - PY-020: gol sem lado fica de fora;
    - PY-021: jogador "2"/"22" fica sem nome;
    - PY-025: estádio sem o patrocinador ("ueno", "Tigo").
  - **Edição nova:** PY-027, o Apertura 2026 (Olimpia campeão; D-01).
- **Abertos:**
  - PY-008: fases do Apertura e do Clausura de 1996-2007;
  - PY-009: datas no título da fase, no leitor comum, no fim;
  - PY-012: rebaixados por ano;
  - PY-018: artilheiros de 2014 em diante;
  - PY-019;
  - PY-031: textos da ficha.
- **Números:** 134 edições, 7.823 jogos, 50 clubes. Teste de carga: `par-1: 134 edições, 7823 jogos, 9 clubes novos -> OK`.
- **Pedido ao agente 1:** recarregar o `par-1` inteiro.
  - Os ids mudam: saem os jogos de pré-temporada e de copas, e entra o Apertura 2026.
  - Atenção ao PY-001, do lado do painel: o campeão deve sair de `edicao.campeao_id`, não da posição 1.
- **Commit:** `4583f7e`.
- **O leitor comum (`rsssf_sul.py`) não mudou.**

## 23/11 — Correções da revisão: Peruano (`per-1`)

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul).

- **Corrigidos:**
  - **Classificação:**
    - PE-002 e PE-008: a tabela do ano inteiro, emendada:
      - 1970-1979: grupo final + rebaixamento/1ª fase;
      - 1998 e 2000: as duas partes da tabela acumulada;
      - 2009 e 2012: as duas liguillas, por pontos;
      - 2001, 2004 e 2005: soma do Apertura e do Clausura, porque a página não tem a acumulada.
    - PE-004: 2020 pela tabela anual pós-TAS.
    - PE-006 e PE-007: 2021 pela tabela anual com o TAS aplicado (Cusco 23, Cienciano 39; rebaixados Cusco FC e Alianza
      Universidad; Carlos Stein fora).
    - PE-003: "rebaixado" só com "Relegated" explícito.
  - **Liga Peruana 1912-1921 (PE-019, D-06 A):**
    - ordem e participantes das páginas peru1912-1921, com 14 clubes antigos novos no cadastro;
    - PE-001: "Jorge Chávez" sem número é o do Callao (vice de 1918 e 1921), e o N°1 só quando a página escreve o número.
  - **Jogos e fases:**
    - PE-005: a final de 2021 (Alianza x Cristal);
    - PE-013: as finais do Torneo de Verano de 2017 e 2018 como fase própria;
    - PE-011: "Regional Final" de 1987 e 1988 como fase própria;
    - PE-010: jogos de janeiro de 1990 em 1991.
  - **Outros:**
    - PE-021: Sporting Tabaco em Lima;
    - PE-016, PE-018 e PE-026: registrados no relatório.
- **Abertos:**
  - PE-009: datas no título da fase, no leitor comum, no fim;
  - PE-010: a final nacional de 1990 como "Final";
  - PE-012: liguilla final de 1988;
  - PE-014: rebaixados por ano;
  - PE-015: artilheiros de 1996;
  - PE-017: placares, só com uma 3ª fonte;
  - PE-022: cidade do Deportivo Bancos.
- **Números:** 109 edições, 17.318 jogos, 167 clubes. Teste de carga: `per-1: 109 edições, 17318 jogos, 14 clubes novos -> OK`.
- **Pedido ao agente 1:** recarregar o `per-1` inteiro. Os ids mudam: entra a final de 2021, e mudam as fases e as datas.
- **Commit:** `55c7066`.
- **O leitor comum (`rsssf_sul.py`) não mudou.**

## 23/11 — Correções da revisão: Equatoriano (`ecu-1`)

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul).

- **Corrigidos:**
  - **Classificação:**
    - EC-001 e EC-002 (D-02 A): números da soma de todos os jogos; ordem com campeão e vice, a tabela da última fase de
      liga e depois os eliminados por fase e pontos;
    - EC-003: disputa de 3º e de 4º lugar como fase própria, com o vencedor no 3º/4º (2010 Deportivo Quito, 2011 El
      Nacional);
    - EC-004: rebaixados pela es (novo `coleta/ecu-1/rebaixados_es.py`; 1970-1981 na edição do ano, D-18 a);
    - EC-005: 2025 com El Nacional (-9) e Vinotinto rebaixados.
  - **Fases:**
    - EC-006: 1999, liguilla do rebaixamento;
    - EC-007: 1963, 1966 e 1997, grupos finais de pontos corridos;
    - EC-010: 1997, grupo do rebaixamento, em dezembro de 1997;
    - EC-016: fases na ordem em que foram jogadas.
  - **Jogos:**
    - EC-008: 20 jogos repetidos em 1984, 1986 e 1994;
    - EC-011: Emelec 2-2 LDU, 2005;
    - EC-012: 4 jogos do Aucas, 1965, pontos para o adversário;
    - EC-015 (D-20 c): El Nacional x Delfín, 2025, W.O. 0-3 para o Delfín;
    - EC-017 e EC-024: datas.
- **Abertos:**
  - EC-009: datas no título da fase, no leitor comum, no fim;
  - EC-013: gol a mais com autor em 2007;
  - EC-014: artilheiros de 1988, 1996 e 1999, só com uma 3ª fonte.
- **Números:** 68 edições, 14.175 jogos, 63 clubes. Teste de carga: `ecu-1: 68 edições, 14175 jogos, 0 clubes novos -> OK`.
- **Pedido ao agente 1:** recarregar o `ecu-1` inteiro. Os ids mudam: saem os jogos repetidos, e mudam as fases e as datas.
- **Commit:** `4577457`.
- **O leitor comum (`rsssf_sul.py`) não mudou.**

## 23/11 — Leitor comum: data no título da fase (todas as ligas da América do Sul)

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul).

- **Corrigidos:** AR-023, UY-014, CH-012, CO-008, PY-009, PE-009 e EC-009. No `coleta/comum-sulamerica/rsssf_sul.py`, a
  data entre colchetes num título que não é jogo ("Final [Dec 23]:", "First Leg [Jul 29]", "Semifinals [Jun 28]") vale
  para os jogos de baixo. Antes, eles herdavam a data do último jogo da liga.
- **O que mudou (as 9 ligas foram reimportadas e comparadas com a versão de antes):**
  - **Datas:** 680 jogos, quase todos de finais, semifinais e desempates (arg 58, uru 75, chi 49, col 108, par 73,
    per 86, ecu 48, bol 62, ven 121). Ex.: Uruguai 2025, final em 23/11 e 30/11; Colômbia 2024 Fi, em 18/12 e 22/12.
  - **Placares, fases e clubes:** nenhum mudou.
  - **ESPN:** com as datas certas, mais jogos casaram com ela (mais hora, estádio, gols com minuto e cartões).
  - **Venezuela:** saíram 2 jogos da ESPN que repetiam a final absoluta de 2025 da página (13.582 -> 13.580).
- **Ids das partidas:** não mudam por esta mudança (mesma ordem), salvo na Venezuela, por causa dos 2 jogos a menos. O
  `fonte_id` muda nos jogos que passaram a casar com a ESPN.
- **Teste de carga:** as 9 ligas com "-> OK".
- **Pedido ao agente 1:** recarregar as 9 ligas. Seis delas já precisam ser recarregadas pelas correções de hoje; Bolívia,
  Venezuela e o resto mudam só nas datas.
- **Commit:** `415911b`.

## 23/11 — Abertos da revisão: Equatoriano (ecu-1) e regra do gol sem lado (também ven-1)

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul).

- **Corrigidos:**
  - EC-013: LDU de Quito 4-0 Deportivo Cuenca (2007) tinha um gol do Cuenca. A ESPN traz um lance sem lado ("Luis
    Escalada", 66'), que entrava como do visitante. Agora gol da ESPN sem lado não entra (a regra do PY-020). A regra vale
    também em `chi-1`, `col-1`, `per-1` e `ven-1` (CH-017, CO-018). Chile, Colômbia e Peru serão reimportados com os seus
    abertos.
  - EC-014: o artilheiro de 1988 passa a Janio Pinto com 19 gols, como a página do ano na RSSSF e a Wikipédia em
    espanhol. 1996 (Graziani, 29) e 1999 (Bottero, 25) ficam como estão: a terceira fonte (El Universo, 26/12/2002; para
    1996, também a Wikipédia em inglês) confirma a RSSSF. As três ficam explicadas no relatório.
- **O que mudou no pacote:**
  - **Equador:** sai 1 gol (2007). Em 4 jogos (2005-2007), os gols da RSSSF trocam pelos da ESPN, com minuto, porque o
    lance sem lado deixou de travar a ESPN. Muda 1 artilheiro (1988).
  - **Venezuela:** saem 2 gols a mais (2005/06 e 2007/08). Caracas 2-2 Táchira (2007/08) ganha os 4 gols da ESPN.
- **Ids das partidas:** não mudam. Placares, fases e clubes também não.
- **Teste de carga:** `ecu-1: 68 edições, 14175 jogos, 0 clubes novos -> OK`; `ven-1: 106 edições, 13580 jogos, 0
  clubes novos -> OK`.
- **Pedido ao agente 1:** recarregar `ecu-1` e `ven-1` (gols e artilheiros).
- **Commit:** `cf612c6`.
- **O leitor comum (`rsssf_sul.py`) não mudou.**

## 23/11 — Abertos da revisão: Peruano (per-1)

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul).

- **Corrigidos:**
  - PE-010: em 1990, o jogo do título do Regional II (Universitario 1-0 Alianza Lima) virou "Final do Regional II". A
    final nacional (Universitario 4-2 Sport Boys) virou "Final", em 3/2/1991.
  - PE-012: em 1988, a liguilla final (15 jogos) virou "Fase final". O jogo do título (Sporting Cristal 2-1 Universitario)
    ficou como "Final".
  - PE-014: rebaixados pela Wikipédia em espanhol (novo `rebaixados_es.py`, com a seção "Ascensos y descensos" de cada
    temporada). São 100 clubes a mais com "rebaixado", em 48 edições. Quem ganhou a revalidação ("Se Mantiene") não
    conta. De 1984 a 1991, só conta quem sai do campeonato.
  - PE-015: 1996 com dois artilheiros de 20 gols (Waldir Sáenz e Adrián Czornomaz), como as Wikipédias em espanhol e em
    inglês e o national-football-teams.com.
  - PE-017: os placares da RSSSF ficam. Em 6 dos 9 anos, a tabela publicada fecha com eles; está explicado ano a ano. Em
    2004, o Cienciano 1-1 Universitario do Apertura (abandonado nos acréscimos) passou a contar com o 1-1, e a tabela
    fecha.
  - PE-022: Deportivo Bancos em Pucallpa (Ucayali).
  - Junto (do commit `cf612c6`): gol da ESPN sem lado não entra. Em 2006, Universitario 3-2 Alianza Lima ganha os gols
    da ESPN.
- **O que mudou no pacote:**
  - **Fases:** 1988 e 1990.
  - **Datas:** a final de 1990.
  - **Placar:** 1 jogo (2004-0122, de abandonado para 1-1).
  - **Classificação:** situação "rebaixado".
  - **Artilheiros:** 1996.
  - **Clubes:** a cidade de 1 clube.
- **Ids das partidas:** não mudam.
- **Teste de carga:** `per-1: 109 edições, 17318 jogos, 14 clubes novos -> OK` (os 14 são os da Liga Peruana, ainda
  não carregados).
- **Pedido ao agente 1:** recarregar o `per-1`.
- **Commit:** `70d8caf`.
- **O leitor comum (`rsssf_sul.py`) não mudou.**

## 24/11 — Abertos da revisão: Paraguaio (par-1)

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul).

- **Corrigidos:**
  - PY-008 (fases):
    - De 1996 a 2007, as fases de dentro do Apertura e do Clausura levam o nome do torneio ("Semifinal do Apertura",
      "Final do Clausura", "Liguilla do Apertura"). A final do ano ficou como "Final" ou "Desempate do título".
    - Em 2003, a liguilla pré-Libertadores virou fase própria: antes era "Quadrangulares semifinais".
    - Em 1999, o desempate pela 3ª vaga na Libertadores virou "Desempate do 3º lugar".
    - Em 1981, a semifinal e a final do 1º turno viraram "Semifinal do 1º turno" e "Final do 1º turno". O triangular
      virou "Triangular de desempate", e o "Overall Final" virou "Final".
    - A classificação de 1981, 1996 e 1997 mudou de ordem (D-02 A): as fases dos torneios não contam como fase final.
  - PY-012 (rebaixados): vêm agora das notas das páginas da RSSSF (`explicacoes.REBAIXADOS`), com 55 marcas novas de 1981
    a 2025.
    - Só conta quem jogou o ano e não está na 1ª divisão do ano seguinte. Por isso o Independiente fica fora em 2017:
      ganhou o desempate.
    - 2008 fica sem marca: a página não traz a tabela de promedios.
  - PY-018 (artilheiros): de 2011 em diante, a fonte é a coluna "Goleador" da Wikipédia em espanhol (novo
    `goleadores_es.py`).
    - Entram 14 edições que estavam sem artilheiro.
    - Nas outras, as contagens são iguais às dos gols com autor.
  - PY-019 (artilheiros de 1935, 1962, 1963, 1967, 1970 e 2003): ficam os números da lista da RSSSF. As divergências com a
    Wikipédia em espanhol e com as páginas do ano estão explicadas no relatório.
  - PY-031 (documentação):
    - O texto "tabela completa em ..." foi corrigido para 1909, 1943, 1945, 1946, 1955, 1986 e 1994.
    - A ficha separa as edições com menos jogos que o esperado das que têm mais.
- **Ids das partidas:** os jogos são os mesmos (7.823). Mas os ids de 8 edições foram renumerados, porque a ordem das
  fases mudou: 1981, 1996, 1997, 1998, 1999, 2001, 2002 e 2003. A ligação estável é o `fonte_id`.
- **Teste de carga:** `par-1: 134 edições, 7823 jogos, 9 clubes novos -> OK`. Os 9 são os cadastrados nas correções de
  23/11, ainda não carregados; o `clubes.csv` não mudou.
- **Pedido ao agente 1:** recarregar o `par-1` inteiro (fases, ids, classificação, artilheiros).
- **Commit:** `a22c1ff`.
- **O leitor comum (`rsssf_sul.py`) não mudou.** O `documentar.py` passou a listar à parte as edições com mais jogos que o
  esperado; as fichas das outras ligas só ganham essa linha.

## 24/11 — Abertos da revisão: Chileno (chi-1)

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul).

- **Corrigidos:**
  - CH-006 (classificação, D-02 A):
    - Entre clubes que chegaram à mesma fase, os pontos, o saldo e os gols da fase final de pontos (quadrangular,
      liguilla) vêm antes da soma do ano.
    - 1984: 3º Unión Española e 4º Cobreloa, como o "Final Playoff" da chilehist.
    - 1969 e 1970: a ordem passa a ser a da "Final Phase" da chilehist.
    - 1946 e 1951 continuam com a tabela acumulada, que é a oficial (`PONTOS_ACUMULADOS`).
  - CH-014 (1986): os dois jogos da última rodada (25/01/1987) estavam com os adversários trocados no ogol. Agora são
    Cobreloa 1-1 San Luis e Rangers 0-0 Cobresal. Os jogos dos outros turnos e a tabela da chilehist só fecham assim.
    - Sobra Everton x Rangers, com 2 gols de diferença para a tabela, explicado no relatório e sem 3ª fonte.
    - De quebra, saíram do `clubes.csv` as grafias erradas que as trocas de 1986 e de 1988 deixavam ("ogol:Cobresal" no
      Cobreloa etc.).
  - CH-017: saem os 6 gols a mais (gol da ESPN sem lado, regra de `cf612c6`) e o nome "Gabriel 2Vargas" (12 gols).
  - CH-022 (grupos):
    - A fase com um grupo só fica sem grupo: 1ª fase de 2002-2008 e as séries do Promocional de 1968.
    - Os jogos Interseries do Nacional de 1969 e 1970 (18 por ano) ficam sem grupo.
    - O quadrangular do 5º lugar do Provincial de 1968 virou "Desempate do 5º lugar do Provincial".
  - CH-023 (1969): as 4 datas que o calendário do ogol da fase final dava a jogos do Metropolitano, do Provincial e do
    Nacional saíram (`OGOL_FORA`). Junto, mudou a regra de casamento: par de clubes que se repete na edição, sem data na
    RSSSF, só casa com placar igual.
  - CH-028: o calendário do ogol de 1964, 1971, 1977 e 1982 foi baixado de novo e está completo.
    - Com isso e com a regra do CH-023, 918 jogos ganharam data (1964 256, 1968 159, 1977 157, 1971 146, 1939 91, 1946
      48, 1982 40…). Nenhum outro perdeu.
    - O ogol não tem jogos de 1952 a 1957: as páginas de calendário vêm vazias na origem.
- **Ids das partidas:** não mudam. Placares, fases e clubes também não, fora os jogos corrigidos acima.
- **Teste de carga:** `chi-1: 109 edições, 22586 jogos, 1 clubes novos -> OK`. O clube novo é o das correções de 23/11,
  ainda não carregado.
- **Pedido ao agente 1:** recarregar o `chi-1` (datas, classificação, grupos, gols, clubes).
- **Commit:** `b8b5a57`.
- **O leitor comum (`rsssf_sul.py`) não mudou.**

## 24/11 — Abertos da revisão: Argentino (arg-1)

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul).

- **Corrigidos:**
  - AR-020 (classificação):
    - 1929: os números da 1ª fase vêm das tabelas dos grupos, que contam os pontos dados por W.O. (Tigre x Lanús,
      Defensores x Barracas Central, Quilmes x Sportivo Barracas). Somam-se a eles os desempates, o 3º lugar e a final.
      O Lanús fica com 8-8-1 e 24 pontos no grupo, como a página.
    - 1908: o Nacional de Buenos Aires (eliminado depois de 2 jogos, anulados) entra no fim da classificação.
    - 1965: Estudiantes e Racing empatam com 36 pontos; fica a ordem da RSSSF, e a diferença com a Wikipédia está
      explicada.
    - 1931 Liga já estava com a tabela publicada.
  - AR-021 (rebaixados): vêm agora da Wikipédia em espanhol (anexo "Movilidad interdivisional en el fútbol argentino",
    era profissional; novo `rebaixados_es.py`), com 128 marcas novas.
    - Ex.: Lanús em 1949; River Plate, Huracán, Quilmes e Gimnasia La Plata no Clausura de 2010/11.
    - Cada clube fica na última edição da temporada em que jogou. A nota "Relegated" da tabela continua valendo.
  - QU-003: 25 jogos adiados (a RSSSF os põe na rodada original) passaram a casar com a ESPN, com mesmo par e mesmo
    placar dentro do período da edição. Vale a data da ESPN, e a observação diz que o jogo foi adiado.
    - Ex.: Boca 2-0 River em 25/03/2010 e em 09/11/2025; Independiente 0-1 Tigre em 08/12/2010.
    - Esses jogos ganham hora, estádio, gols com minuto e cartões.
- **Ainda aberto:** QU-005, datas de jogos do Boca (1945, 1954, 1977 Metropolitano, 1989/90) diferentes do
  historiadeboca. Falta 3ª fonte; a Wikipédia em espanhol não traz as datas desses anos.
- **Para a revisão olhar:** em 1912 Asociación, os jogos de Alumni, Estudiantes, Gimnasia de Buenos Aires e Porteño, que
  saíram da liga, contam no pacote, mas a tabela publicada não os conta.
- **Ids das partidas:** não mudam.
- **Teste de carga:** `arg-1: 197 edições, 43726 jogos, 0 clubes novos -> OK`.
- **Pedido ao agente 1:** recarregar o `arg-1` (classificação, datas de 25 jogos, gols e cartões).
- **Commit:** `e698941`.
- **O leitor comum (`rsssf_sul.py`) não mudou.**

## 24/11 — Abertos da revisão: Colombiano (col-1), e junto Argentino e Uruguaio

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul).

- **Corrigidos no Colombiano:**
  - **CO-004:** a 3ª e a 4ª volta de 1955-1963 estão na Wikipédia em listas que o leitor não lia, agora lidas (`ANOS_LISTAS`):
    - 1955 tem 135 jogos (eram 90);
    - 1958, 180 (eram 90);
    - 1959, 261 (eram 130);
    - 1960, 264 (eram 132);
    - 1961, 264 (eram 132);
    - 1963, 312 (eram 156; o cabeçalho "Res." não era reconhecido).
  - **CO-006:**
    - 1989 tem as listas "Fecha N (data)" em texto solto: 242 jogos (eram 32), com data. A temporada foi suspensa, então é
      tudo o que se jogou.
    - 1976: o hexagonal ficou completo (30 jogos; 10 caíam por um link sem "|").
  - **CO-009:** a final do Finalización 2025 está em 12/12 e 16/12/2025 (`{{fecha|...}}`), com a ESPN certa (762528 e
    762529). Também: par de clubes repetido, sem data, só casa com a ESPN com placar igual.
  - **CO-012:**
    - O grupo dos quadrangulares sai das tabelas da fase: 420 jogos A e 420 B (antes, quase todos "B").
    - A 1ª fase de 2002 em diante ficou sem grupo (425 jogos).
  - **CO-013 (1957):** o octogonal cancelado virou anulado. Os hexagonais têm grupos A e B. Entraram o "Desempate do grupo"
    A e a "Final dos hexagonais" (Cúcuta x Tolima, fev-mar de 1958).
  - **CO-015:** 1948 e 1949 vêm agora da tabela de confrontos da RSSSF, mais a final de 1949 da Wikipédia. Sobra 1
    linha divergente em cada ano.
  - **CO-016:** o bônus da fase final de 1983-1988, 1992-1994 e 1998 está na observação da classificação.
    - Os pontos não mudam: são frações (0,25, 0,75) e o esquema do banco é inteiro.
    - **Pedido ao agente 1:** se quiser o bônus nos pontos, `ajuste_pontos` precisa aceitar fração.
  - **CO-017:** os artilheiros de 2008 em diante vêm da Wikipédia em espanhol (novo `goleadores_es.py`). O clube vem dos
    gols com autor da edição, e fica vazio quando não há.
  - **CO-018:** gol da ESPN sem lado não entra (regra de `cf612c6`).
  - **Nome da ESPN:** "Hilario 2Cuenú" fica sem o dígito, como no CH-017.
  - **CO-020:** a data do título da rodada ("(febrero 16/1975)", "Fecha 1 septiembre 14") agora é lida. 976 jogos ganharam
    data (1957, 1975, 1979, 1982, 1990), e nenhum mudou.
  - **Chaves do CORRIGE:** as de jogos da Wikipédia estavam como "wiki:es_…", mas o leitor usa "wiki-es_…". Por isso as
    finais do Apertura de 1974-1982 (correção de 23/11) nunca tinham valido. Agora valem.
- **Ainda abertos no Colombiano:**
  - CO-006: 1986 e 1988, porque a Wikipédia não tem os jogos que faltam.
  - CO-004: 1966, com 350 de 364.
  - CO-015: placares de 2001-2018, que só uma 3ª fonte decide.
  - CO-022: os números esperados e o diagnóstico automático do relatório.
- **Junto:**
  - **Argentino:** "Gastón 2Fernández" (ESPN) fica sem o dígito, em 15 gols e cartões. Só nomes mudam.
  - **Uruguaio:** o W.O. de 1908 (Intrépido x Bristol, UY-010) tinha a mesma chave errada e nunca valeu. Agora a vitória
    é do Bristol, e a classificação de 1908 muda.
- **Ids das partidas:**
  - Colombiano: mudam nas edições com jogos novos (1955, 1958-1961, 1963, 1976, 1989) e em 1948-1949 (outra fonte).
  - Argentino e Uruguaio: não mudam.
- **Teste de carga:**
  - `col-1: 101 edições, 23418 jogos, 0 clubes novos -> OK` (eram 22.512);
  - `arg-1: 197 edições, 43726 jogos, 0 clubes novos -> OK`;
  - `uru-1: 126 edições, 12456 jogos, 3 clubes novos -> OK`.
- **Pedido ao agente 1:** recarregar `col-1`, `arg-1` e `uru-1`. Com isso, os abertos da revisão da América do Sul acabam,
  fora os que esperam 3ª fonte.
- **Commit:** `d6bec05`.
- **O leitor comum (`rsssf_sul.py`) não mudou.**

## Recado de fim de coleta — uru-copa — 24/11/2026

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul).

1. **O que foi feito:** a Copa AUF Uruguay (`uru-copa`, `tipo` "copa"), a primeira das sete copas nacionais.
   - **Decisões do Guilherme (24/11):** as sete copas, contagem da Wikipédia, das menores às maiores
     (`coleta/comum-sulamerica/copas-nacionais.md`).
   - **Números:** 4 edições (2022, 2023, 2024 e 2025; a 2026 está em andamento), 221 jogos e 100 clubes, dos quais 61
     só jogam a copa.
   - **Gols com autor:** 539 de 545.
   - **Fonte:** RSSSF, seção "Copa AUF Uruguay" das páginas do ano, as mesmas do uru-1. O campeão foi conferido com a
     Wikipédia em espanhol, e os 4 batem (Defensor Sporting 2022-2024, Peñarol 2025).
   - **Sem** cartões, estádio e público: a RSSSF não traz.
2. **Commits:** `1fe6d99`.
3. **Teste de carga:** `uru-copa: 4 edições, 221 jogos, 61 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:**
   - carregar a `uru-copa`;
   - o slug de copa segue `<país>-copa` (o guia geral não fixa; o Brasil usa `bra-copa-do-brasil`). Se preferir outro,
     me diga antes das próximas seis.
5. **Decisões:**
   - 2022: as quatro fases regionais têm o grupo com o nome da região ("Norte", "Centro-Litoral", "Este",
     "Sur-Metropolitano").
   - 2023 é a temporada "2023", com `ano_fim` 2024 (a final foi em maio de 2024; a RSSSF a chama de 2023/24).
   - W.O. ("awarded 3-0, X forfeited") ficou com o placar dado, `resultado_especial` "wo" e a observação "W.O.: X não
     compareceu".
   - Nomes de clube do interior levam a cidade (`Wanderers de Durazno`, `Huracán de Rivera`). Os que já estavam no uru-1
     ficam com o nome de lá (Paysandú Bella Vista, Colón de Montevideo, Lito).
6. **O que não deu:**
   - Algumas cidades ficaram vazias, por falta de fonte: Estudiantes del Plata e Rincón de Carrasco.
   - Artilheiros só pela contagem dos gols com autor: a RSSSF não dá lista de artilheiros da copa.
7. **Onde a revisão deve olhar primeiro:**
   - **Grafias que caíam em clubes de Montevidéu por prefixo** (ex.: "Wanderers Durazno" virava Montevideo Wanderers).
     Agora há regras próprias da copa, com o nome inteiro, em `coleta/uru-copa/clubes_copa.py`.
   - **Autores em várias linhas:** o leitor comum perde a continuação do colchete. O importador das copas junta as
     linhas; nas ligas pode haver perda (pendência minha).
8. **Próxima competição:** Copa Paraguay (`par-copa`).

## Recado de fim de coleta — par-copa — 24/11/2026

Para o agente 1 (banco e painel) e o agente de revisão. Agente 4 (América do Sul).

1. **O que foi feito:** a Copa Paraguay (`par-copa`, `tipo` "copa"), a segunda das sete copas.
   - **Números:** 7 edições (2018, 2019, 2021-2025; não houve em 2020), 296 jogos e 110 clubes, dos quais 75 só jogam a
     copa.
   - **Fonte:** RSSSF, seção "Copa Paraguay" das páginas do ano, as mesmas do par-1. Os 7 campeões batem com a Wikipédia
     em espanhol.
   - **Sem** autores de gols: a RSSSF não traz na copa do Paraguai. Sem cartões, estádio e público também.
2. **Commits:** `e31a932`.
3. **Teste de carga:** `par-copa: 7 edições, 296 jogos, 75 clubes novos -> OK`.
4. **Pedidos ao banco e ao painel:** carregar a `par-copa`.
5. **Decisões:**
   - Clubes do interior levam a cidade quando a RSSSF a dá ("Nacional de Yby Yaú", "Olimpia de Itá"); sem a cidade, o
     nome fica como na página.
   - "24 de Setiembre" sem cidade é o de Valle Pucú, e "Cristóbal Colón" sem cidade é o de J. Augusto Saldívar: os dois
     são da Intermedia e são os que chegam às fases finais.
   - Para não repetir nome de outro país: "Athletic Club (Paraguai)" (o Brasil já tem um Athletic Club), "Club Oriental
     (Paraguai)" e "Sud América (Paraguai)" (o Uruguai já tem Oriental e Sud América).
   - Em 2022, a 1ª fase em zonas só tem as tabelas na página. Ela entra como fase de grupos (2 zonas), sem jogos.
   - O importador comum (`copa_rsssf.py`) passou a pôr nas fases a fase que só tem tabelas. A `uru-copa` não mudou.
6. **O que não deu:**
   - 2024 e 2025 só das oitavas em diante: a RSSSF não traz as fases anteriores. Fonte que resolveria: a Wikipédia em
     espanhol de cada edição, ainda não lida.
   - Muitas cidades ficaram vazias (clubes das divisões de acesso e do interior sem cidade na página).
7. **Onde a revisão deve olhar primeiro:**
   - As grafias que casavam por prefixo com clubes da Primera (estão em `coleta/par-copa/clubes_copa.py`).
   - O conserto de texto de 2019 ("Independiente  (Nanawa)", no `explicacoes.py` do par-1; a linha fica fora da liga).
8. **Próxima competição:** Copa Ecuador (`ecu-copa`).
