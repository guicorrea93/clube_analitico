# Plano de correção: Campeonato Francês (fra-1), revisor FR, 22/11/2026

Ordem: gravidade x tamanho x custo. Nada disto está no ar; o Francês ainda não está no painel. Corrigir antes de pôr no painel.

## coleta-europa

### `coleta/fra-1/importar.py` (quase tudo)

1. **FR-001 (alta):** rebaixados.
   - Nas linhas 831-843, montar `prox_clubes` com `clube_ogol(o, lado, mapa_ogol, prox)`, e não com `mapa_ogol.get(código)`.
   - Criar `FUSOES` para 1938/39 (Olympique Lillois, Fives, Excelsior e, se FR-D3 = a, RC Roubaix) e para 1966/67 (Toulouse), com
     `situacao` vazia e `observacao` "fusão".
   - A faixa da classificação por rodada se corrige junto.
   - Custo baixo. Fonte: Wikipédia fr, por temporada.
2. **FR-002 (alta):** bônus.
   - `BONUS = {1973: "gols", 1974: "diferenca", 1975: "diferenca"}`.
   - Usar a regra em `calcular()` (linha 388), no desconto do ajuste (linha 703) e no texto da observação (linha 958).
   - Somem as 39 punições falsas, e a classificação por rodada de 1974/75 e 1975/76 fica certa.
   - Custo baixo. Fonte: Wikipédia fr 1974-75 e 1975-76.
3. **FR-003 e FR-004 (alta):** dois jogos decididos no tribunal.
   - `TRIBUNAL`: 1951/52 Olympique Marseille x Racing Club de France (0-0, "v", campo 2-3).
   - `TRIBUNAL`: 1955/56 AS Nancy x Olympique Marseille (0-0, "v", campo 2-4).
   - Tirar `WIKI_ERRA` de `EXPLICACOES` em 1951; rever 1955.
   - Custo baixo. Fonte: Wikipédia fr (notas da grade) e transfermarkt.
4. **FR-005 (alta):** 1946/47.
   - Em `reparar()` (linhas 437-451), quando o par existe na base com outro placar, ficar com o placar da base e a data do ogol.
   - Depois, OM x Bordeaux de 27/10/1946 em `TRIBUNAL` ("m", 0-0), só depois de conferir num jornal (Gallica).
   - Rodar `revisao/FR/teste_1946.py` para ver as tabelas fecharem.
   - Custo baixo, mais uma consulta ao jornal.
5. **FR-006 (média):** VA-OM de 1992/93.
   - Novo vencedor "nenhum" em `TRIBUNAL` e `calcular()`, com derrota para os dois.
   - Ignorar o ajuste -1 da Wikipédia en para OM e Valenciennes; campo 0-1.
   - Custo baixo.
6. **FR-008 (média):** tirar a `CORRECOES` de 1958/59 (Sochaux x Rennes volta a 4-3) e anotar em `EXPLICACOES`. Custo mínimo.
7. **FR-007 (média):** `CORRECOES` de 1947/48: Racing 5-1 Stade Français e Stade Français 1-0 Racing. Custo mínimo.
8. **FR-009 (média):** novo dicionário `DATAS`, aplicado em `carregar_base`.
   - Os 41 jogos de 3 dias ou mais vêm de `revisao/FR/datas_tm_ogol_lista.txt`.
   - Os 99 de 1-2 dias (1996/97 e 1997/98) só depois de conferir uma rodada num jornal: o football-data repete a data da base.
9. **FR-010 (média):** Le Havre 2008/09.
   - Não aplicar a punição que só a RSSSF tem (linhas 733-738) sem uma prova.
   - Melhor ainda: a regra geral só aceita punição da RSSSF quando a Wikipédia também tem nota.
10. **FR-011 (média) e FR-019 (baixa):** artilheiros.
    - Em `artilheiros()`, acrescentar Onnis (1979/80) e Garande (1983/84).
    - Bokšić conforme FR-D4.
    - Dicionário de nomes usuais da Wikipédia fr.
11. **FR-014 (baixa):** linha 857. Usar só a nota, traduzida, e nunca o `hth`.
12. **FR-015 (baixa):** dicionário `ADMINISTRATIVOS` com a observação:
    - 1990/91 Bordeaux, Brest e Nice;
    - 1993/94 OM;
    - 2000/01 Toulouse;
    - 2016/17 Bastia.
13. **FR-016 (baixa):** linhas 895-897. O texto da observação deve dizer o placar dado no tribunal e o de campo.
14. **FR-018 (baixa):** critério de desempate por época, e não "o que reproduz". Antes, achar quando a FFF trocou a média de gols
    pelo saldo (Wikipédia fr de cada temporada, seção "Résultats et classements").
15. **FR-020 (baixa):** observação do Antibes em 1932/33.
16. **FR-022 (baixa):** docstring e `relatorio()`: o football-data não traz árbitro.
17. **FR-017 (baixa):** quatro dúvidas para conferir na Gallica: 1935/36, 1937/38, 1945/46 e 1950/51. Só anotar em `EXPLICACOES`.

### `coleta/comum-europa/clubes_fra.py`

18. **FR-012 (média):** clube "Toulouse FC (1937)" se FR-D1 = a.
19. **FR-013 (baixa):** anotar Lyon OU e SO Montpellier conforme FR-D2.
20. **FR-021 (baixa):** "Évian".

### Depois de corrigir

- Rodar `python coleta/fra-1/importar.py`, `testar_carga.py fra-1 <scratch>` e `documentar.py`.
- Conferir de novo com `revisao/FR/comparar_frwiki.py`, `bonus.py`, `varredura_pacote.py` e `artilheiros.py`. Os scripts leem o
  pacote.

### Buracos de cobertura (sem achado; fonte nova)

- **Árbitro (0%), e antes de 2001/02 gols com autor, cartões, público e estádio:** ficha de jogo do transfermarkt
  (`spielbericht`), em lotes. Cerca de 27 mil páginas.
- **Datas e rodadas dos anos 1930:** footballdatabase.eu (limite de 50 páginas por dia; conta grátis) ou a Gallica.

## banco-painel

- Nada a corrigir agora: o `fra-1` no banco é igual ao pacote.
- Depois da nova importação:
  - recarregar o banco;
  - gerar `painel/dados/fra-1.js`;
  - baixar os escudos (calendários do ogol em `data/cache/ogol-fra-1/`);
  - o painel deve usar o vencedor da `observacao` nos jogos `awd` com o placar mantido (o pacote já avisa no item 6 do recado).
