# Decisões para o Guilherme — Inglês (eng-1) e Espanhol (esp-1), revisor QE, 22/11/2026

Já decididas e aplicadas (não reabrir): EN-001 (2025/26 entra), EN-006 (5-0), EN-007 (rodada vazia), EN-018 (não
reeleitos), ES-001 (Atlético 1935/36 rebaixado), ES-005 (contagem oficial da LFP). Abaixo, as que seguem sem resposta.

### ES-013 Nome de época dos clubes: mostrar "Atlético Aviación", "Madrid FC", "Woolwich Arsenal"... ou sempre o nome atual?
- **Opções:**
  1. manter como está: sempre o nome atual ("Atlético de Madrid" campeão de 1939/40 e 1940/41);
  2. nome da época só onde o painel fala de uma edição (Pódio, Classificação, Jogos, Corrida), com o nome atual ao passar o
     mouse; nas contagens e em Por clube, o nome atual;
  3. nome atual com o da época entre parênteses nas edições: "Atlético de Madrid (Atlético Aviación)".
- **Prova:** https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_de_Espa%C3%B1a_1939-40 (campeão "Athletic-Aviación de
  Madrid"); o banco já guarda os nomes com os anos (`clube_nome`, vindo do `nomes_fonte` dos pacotes: Atlético Aviación,
  Atlético de Bilbao 1941-1972, Madrid FC 1931-1941, Español; no Inglês, Small Heath, Woolwich Arsenal, The Wednesday, Newton
  Heath, Leicester Fosse). Vale para todas as ligas.
- **Recomendação:** opção 2. É a mais fiel à história e não quebra a identidade do clube (um cadastro só). Custo: uma função
  `nome_na_epoca(clube, ano)` no `gerar_dashboard_v2.py` lendo `clube_nome` (só nomes de fonte "oficial" — RSSSF/Wikipédia —,
  não as grafias do ogol/ESPN).

### EN-004 Artilheiro de 1905/06: Albert Shepherd ou Walter White (os dois do Bolton)?
- **Opções:**
  1. Albert Shepherd, 26 gols (está no painel; lista de artilheiros da Wikipédia en, usada pela coleta);
  2. Walter White, 26 gols (RSSSF engtops e a página "1905–06 Football League" da Wikipédia en);
  3. Albert Shepherd, 25 gols (biografia dele na Wikipédia en, citando "The History of the English Football League");
  4. ficar com Shepherd e anotar a divergência na `fonte` do artilheiro, como o Pichichi no Espanhol (ES-005).
- **Prova:** https://www.rsssf.org/tablese/engtops.html (1906: W.White, Bolton Wand, 26);
  https://en.wikipedia.org/wiki/1905%E2%80%9306_Football_League; https://en.wikipedia.org/wiki/Albert_Shepherd_(footballer)
  ("netting 25 times as he finished as the league's top goalscorer"). Nenhuma fonte de jogo a jogo cobre a temporada inteira: o
  transfermarkt tem 58 dos 380 jogos de 1905/06; o BDFutbol começa em 1960/61.
- **Recomendação:** opção 4. Duas fontes independentes (a lista e a biografia) apontam Shepherd como artilheiro; só o número
  diverge (25 ou 26). Anotar "RSSSF: Walter White 26; biografia: Shepherd 25" na `fonte`. Mexer em `coleta/eng-1/importar.py`
  (`GOLS_ARTILHEIRO` ou a fonte da linha de artilheiros).

### QE-002 Ordem de 1960/61 (6º e 7º): seguir a Wikipédia (Betis 6º) ou a RSSSF (Athletic 6º)?
- **Opções:**
  1. manter a ordem da Wikipédia en/es (Betis 6º, Athletic 7º), como manda a regra geral da coleta ("ordem oficial = Wikipédia");
  2. trocar para a ordem da RSSSF e do BDFutbol (Athletic 6º, Betis 7º).
- **Prova:** https://www.rsssf.org/tabless/spanhist5969.html#6061; https://www.bdfutbol.com/es/t/t1960-61.html;
  https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_de_Espa%C3%B1a_1960-61. Triangular em 30 pontos: Betis 5, Athletic 5,
  Real Sociedad 2; entre Betis e Athletic: 0-0 em Bilbao e 1-3 em Sevilha. O confronto direto aplicado de novo entre os que
  seguem empatados (a regra que reproduz as outras 92 temporadas, QE-001) dá Athletic 6º; a Wikipédia usa o saldo do triangular
  (Betis +3, Athletic +2), que não reproduz 1963/64.
- **Recomendação:** opção 2, por ser a única ordem coerente com a regra de todas as outras temporadas. Não muda título
  nem rebaixamento. Se quiser certeza, uma 4ª fonte (jornal de 01/05/1961) desempata.
