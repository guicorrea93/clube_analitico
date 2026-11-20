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
3. **Nomes:** 170 clubes, nenhum com nome de clube do banco ou de outro pacote. Homônimos argentinos levam a cidade:
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
