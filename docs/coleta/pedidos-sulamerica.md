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
