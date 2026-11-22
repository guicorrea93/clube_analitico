# Decisões do Guilherme: Campeonato Paulista (bra-sp-1), revisor QS, 22/11/2026

Pedidas na 2ª rodada (21/11) e ainda sem resposta em `docs/coleta/pedidos.md` nem em `coleta/comum/COMECE-AQUI.md` (seção 7). Mais uma nova (QS-011).

### SP-001 Título de 1973: dois campeões (Santos e Portuguesa) ou só a Portuguesa?
- opções: (a) dois campeões em 1973, vice Palmeiras, como a FPF; (b) só a Portuguesa, com nota.
- prova: lista oficial da FPF (Tableau do site da federação, https://public.tableau.com/static/images/Ca/CampeesSrieA1/Dashboard1/1.png, ligado em https://futebolpaulista.com.br/Clubes/TodosCampeoes.aspx): Santos com 22 títulos até 2019, o que só fecha contando 1973; Futebol Nacional: "1973 Portuguesa Santos (*) Dividido" (https://futebolnacional.com.br/siteapp/controller.jsp?module=summary&lang=pt-br&name=A27437D2CE0894275C03A3BAEDA49F41A9C63F1F39F7FF7572315985555EFA80&state=SP&country=BR); Wikipédia pt e en (https://pt.wikipedia.org/wiki/Campeonato_Paulista_de_Futebol).
- recomendação: (a). É a contagem oficial da federação e de todas as fontes. Exige o painel aceitar dois campeões numa edição (pedido já feito ao agente 1).

### SP-004 Edição de 2026: entra?
- opções: (a) entra agora (Palmeiras campeão, Novorizontino vice); (b) espera.
- prova: o Guilherme já decidiu em 21/11 que as edições de 2026 da C, da D e da A2 entram (COMECE-AQUI da coleta, seção 7). Fonte pronta e oficial: API da FPF (https://futebolpaulista.com.br/Handlers/Competicoes/ListarTabela.ashx?IdCampeonato=73&Ano=2026&Rodada=1&IdClube=0&IdCategoria=39; artilharia: ListarArtilharia.ashx?idCampeonato=73&IdClube=&exercicio=2026&idCategoria=39&pagina=0&tipoGol=), além do ogol e do Futebol Nacional.
- recomendação: (a), pela mesma regra da C, D e A2. Usar a FPF como base (traz fase e grupo, que faltam no ogol: ver SP-008 em 2025).

### SP-005 Campeonatos amadores da FPF de 1933 (Albion) e 1934 (Fiorentino): reconhecer?
- opções: (a) não reconhecer (só os da APEA, Palestra Itália 1933 e 1934); (b) reconhecer como edições à parte ("1933 FPF", "1934 FPF").
- prova: a lista oficial da FPF (Tableau acima) não dá título a Albion nem a Fiorentino/Juventus e conta 22 títulos do Palmeiras até 2019, com 1933 e 1934 da APEA. O Futebol Nacional lista as duas edições, mas "com pendências" e sem nenhum jogo (0 registrados). As Wikipédias pt/en listam as duas.
- recomendação: (a). Não há jogos em fonte nenhuma e a federação não conta esses títulos.

### SP-006 "Paulistinha" (fase preliminar) de 1970 e 1972-1974: entra na edição?
- opções: (a) não entra (como hoje: só a fase principal); (b) entra como fase da edição, sem peso na classificação (nível 0 no ORDEM); (c) entra como edição à parte.
- prova: o Futebol Nacional tem todos os jogos da preliminar de 1970 (110 do "Torneio de Classificação" + 3 do "Triangular de Acesso"), 1971 (110) e 1972 (132), disputados no ano anterior (set.-dez.); não tem de 1973 e 1974. A Wikipédia pt conta os clubes da preliminar como participantes (16/18/18/21). O pacote também não tem 1971 (o Futebol Nacional tem).
- recomendação: (a) por agora. A fonte só cobre 1970-1972 e a preliminar foi um torneio classificatório com clubes que não jogaram o Paulistão. Se ele quiser os jogos, (b) com 1970-1972 pelo Futebol Nacional.

### SP-026 AA São Bento (1914-1932) e "São Bento de São Paulo" (1933): juntar?
- opções: (a) juntar num clube só, "AA São Bento"; (b) manter separados.
- prova: o Futebol Nacional escreve "AA São Bento" de 1914 a 1933 (1933 APEA: https://futebolnacional.com.br/siteapp/controller.jsp?module=summary&lang=pt-br&name=A27437D2CE0894275C03A3BAEDA49F41A9C63F1F39F7FF7572315985555EFA80&state=SP&country=BR, edição 1933 APEA); a RSSSF também ("AA São Bento" em sp1933.htm, guardado em `rsssf:AA São Bento:1933` no próprio clubes.csv). O cadastro separado vem só do código do ogol 233382.
- recomendação: (a). Mexer: `CORRIGE_OGOL[("1933", "233382")] = ("39622", "o ogol tem um código só para 1933; é a AA São Bento da capital")` em coleta/bra-sp-1/importar.py e tirar a sobra 233382 de data/coleta/comum/clubes_ogol.json.

### SP-027 CA Paulista (1934, 1936) e "ECPaulista" (1935 LPF, São Carlos): juntar?
- opções: (a) juntar em "CA Paulista" (São Paulo); (b) manter separados.
- prova: o Futebol Nacional escreve "CA Paulista" em 1934 APEA, 1935 LPF e 1936 LPF; a RSSSF escreve "EC Paulista" em 1935 (o clube já guarda esse nome em clube_nome). Um clube de São Carlos não jogou a LPF da capital em 1935; o código do ogol 81019 é de outro clube.
- recomendação: (a). Mexer: `CORRIGE_OGOL[("1935 LPF", "81019")] = ("275483", "o ogol liga o jogo a um EC Paulista de São Carlos; é o CA Paulista da capital")` em coleta/bra-sp-1/importar.py e tirar a sobra 81019 do cadastro comum.

### QS-011 Lista de artilheiros: qual é a base?
- opções: (a) RSSSF (sptops.htm, 1902-2021) + FPF (2022-2026), com a Wikipédia pt só para faltas; (b) Wikipédia pt (o que a revisão sugeriu no SP-024); (c) mostrar as duas quando divergem.
- prova: em 17 edições a Wikipédia pt diverge (1906, 1908, 1909, 1911, 1912, 1917, 1919, 1937, 1943, 1947, 1956, 1959, 1960, 1967, 1975, 1990, 1994); nelas a RSSSF (https://rsssfbrasil.com/tablessz/sptops.htm) e o Futebol Nacional batem entre si (ex.: 1937 Teleco 24 nas duas, 15 na pt; 1943 Mário Milani 20, pt Hércules 19; 1990 Volnei 10, pt Alberto/Rubem/Vônei 12; 1994 Evair 22, pt 23). Lista em `revisao/QS/cmp_artilheiros_saida.txt`.
- recomendação: (a). Duas fontes independentes contra uma; o `pacote.py` já foi escrito para ler a sptops.htm (só a expressão regular está errada: QS-010).
