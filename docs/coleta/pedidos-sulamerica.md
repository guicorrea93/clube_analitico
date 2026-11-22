# Pedidos do agente de coleta América do Sul

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
