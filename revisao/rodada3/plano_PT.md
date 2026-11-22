# Plano de correção — Campeonato Português (`por-1`), 22/11/2026

Nada está no ar (o `por-1` não foi carregado). Ordem = gravidade x tamanho do erro x custo. Depois de tudo: rodar
`python coleta/por-1/importar.py`, `python coleta/comum-europa/testar_carga.py por-1 <scratch>` e
`python coleta/comum-europa/documentar.py` (a ficha em documentacao/ é gerada: não editar à mão).

## coleta-europa

### coleta/comum-europa/clubes_por.py
1. **PT-001 (alta, bloqueia a carga):** renomear "Sanjoanense" para "AD Sanjoanense" (CLUBES, OGOL["2185"], ALIASES). Custo: minutos.
2. **PT-017 / PT-018 (baixa, depois das decisões D4 e D5):** só se o Guilherme mandar separar o Estrela da Amadora ou juntar os Elvas.

### coleta/por-1/importar.py — placares (CORRECOES, TRIBUNAL, CAMPO)
3. **PT-002 (média):** apagar (1994, "Benfica", "Sporting") de CORRECOES (o certo é 1-2); anotar em EXPLICACOES[1994] o erro da RSSSF, do engsoccerdata e do football-data. Fonte nova: artigo da temporada do Benfica (Wikipédia en). Muda os pontos do 2º e do 3º.
4. **PT-004 (alta, depois de D3):** 1986/87 Braga x Benfica: sair de CAMPO e entrar em TRIBUNAL (1, 1, "nenhum", "1-1", motivo com o Diário de Lisboa de 18/07/1987). Muda a ordem do 9º ao 13º.
5. **PT-007 (média):** CORRECOES 1980/81 Benfica 2-1 Espinho e Espinho 2-0 Benfica (Transfermarkt, matrizes pt e en, ficha do ogol com 2 marcadores).
6. **PT-009 (baixa):** 1974/75 CUF x Vitória de Setúbal: abrir a ficha do ogol do jogo de 19/01/1975; corrigir o texto do motivo (a versão da RSSSF também fecha com as tabelas) e, se não houver prova da decisão fora de campo, ficar com 1-2 / 0-2 (RSSSF, Transfermarkt, Wikipédias pt e en).
7. **PT-008 (nao-e-erro):** só anotar em EXPLICACOES[1963] e [1965] que Transfermarkt e Wikipédias divergem e que as fichas do ogol confirmam o pacote.

### coleta/por-1/importar.py — ordem e pontos
8. **PT-003 (alta):** 1944/45 com a ordem da RSSSF (vice Sporting; Olhanense 6º, Estoril 7º). Ex.: conjunto ORDEM_RSSSF = {1944} com o motivo.
9. **PT-005 (média, depois de D2):** 2005/06 com a ordem da RSSSF (Naval 13º, Académica 14º); some a incoerência com a classificação rodada a rodada.
10. **PT-006 (média, depois de D1):** 2007/08 Porto 75 (ajuste 0) com observação; Leiria fica -3 com observação.

### coleta/por-1/importar.py — artilheiros()
11. **PT-012 (média):** Seferović 2018/19 = 23 (erro de digitação da RSSSF). Fonte: Bola de Prata (Wikipédia en) e a própria ESPN do pacote.
12. **PT-013 (baixa):** tirar o "\x96" do fim do nome do Luis Suárez (2025/26).

### coleta/por-1/importar.py — datas (novo dicionário DATAS)
13. **PT-010 (média):** 5 datas impossíveis: 1979/80 Marítimo x Portimonense 16/12/1979; 1993/94 Sporting x Famalicão 25/05/1994; 1997/98 Leça x Boavista 10/05/1998; 1938/39 Belenenses x Sporting (provável 26/02/1939) e 1939/40 Académico do Porto (confirmar na ficha do ogol).
14. **PT-011 (baixa):** 26 jogos de 1995/96 a 2015/16 com a data do football-data + Transfermarkt (lista em revisao/PT/datas_divergentes.txt); regra geral: quando football-data e ESPN/Transfermarkt concordam contra o ogol, fica a data deles.

### coleta/por-1/importar.py — observações (texto)
15. **PT-016 (baixa):** explicação nos rebaixamentos fora da zona: 1997/98 Leça (administrativo, corrupção de 1993; Chaves ficou) — falta até em EXPLICACOES; 1950/51, 1961/62, 1973/74 (liguilha); 2005/06, 2008/09, 2019/20 (só no relatório).
16. **PT-014 / PT-015 (baixa):** observacao da classificação final: tirar os 46 códigos crus ("PAÇ", "BRA"...) e trocar os 50 textos em inglês por observações próprias em português (lista em revisao/PT/observacoes_classificacao.txt). Provável que o mesmo aconteça nas outras ligas que usam wiki_tabela.

### coleta/por-1/baixar.py + importar.py — cobertura (fontes novas)
17. **PT-019 (baixa):** marcadores de 1999/00 a 2005/06 pelas páginas portNN.html da RSSSF (em lote, 7 páginas; port06 já baixada). Depois, 2010/11 (56% com autor) e o resto antes de 2006/07 pela ficha do ogol ou do Transfermarkt (jogo a jogo).
18. **PT-020 (baixa):** árbitro (0%) e público antes de 2006/07 pelo Transfermarkt, página do jogo (jogo a jogo, ~11 mil páginas de 1990/91 em diante, ~6 h a 2 s por pedido).

## banco-painel
- Nada a corrigir agora (o `por-1` não está no banco). Na carga: o PT-001 precisa estar resolvido, senão o carregador recusa o pacote. Se o painel recalcular a tabela pelos gols, os jogos `awd` com vencedor na observação (1960/61, 1974/75 e, se D3 = B, 1986/87 com derrota para os dois) precisam do tratamento especial já pedido em docs/coleta/pedidos-europa.md (seção do Português, item 4).
