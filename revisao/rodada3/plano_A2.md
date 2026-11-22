# Plano de correção — Paulista Série A2 (bra-sp-2), revisão de 22/11/2026

Ordem: gravidade x tamanho do erro x custo. Depois de cada bloco: rodar `python coleta/bra-sp-2/importar.py`,
`python coleta/comum/testar_carga.py bra-sp-2 <scratch>`, `python coleta/comum/documentar.py` e a varredura
`python -I revisao/A2/varredura_pacote.py`. A A2 já está no banco local e em painel/dados/bra-sp-2.js (não publicada):
o agente 1 recarrega depois.

## coleta-brasil

### 1. coleta/bra-sp-2/importar.py — ordem da classificação final (A2-002, A2-003, A2-004, A2-005, A2-006, A2-018 parte, A2-024)
- Usar a tabela da última fase (pontos, depois saldo) para ordenar os clubes que chegaram a ela, antes dos pontos totais.
  Corrige os vices de 1979 (Santo André), 1986 (Noroeste), 1996 (Portuguesa Santista), 1997 (Ituano) e o 3º/4º de 2004.
- Quando a classificação vem da "classificação geral publicada" (2008, 2011, 2013, 2015), pôr o finalista derrotado em 2º (2013: Rio Claro).
- 3º/4º: semifinalistas; conferir contra a predefinição de campeões da Wikipédia (fonte nova).
- O mesmo ajuste vale no bra-sp-1 (SP-002, SP-007, SP-008): fazer os dois juntos.

### 2. coleta/bra-sp-2/pacote.py — acesso e rebaixamento (A2-007, A2-008, A2-009, A2-026)
- acesso: não contar clube cujos únicos jogos na A1 do ano seguinte são de repescagem/playoff (1950 XV de Jaú, 1979 Catanduvense,
  2001 Francana, 2002 Atlético Sorocaba).
- rebaixados: a regex "relegat" pega "Relegation Playoff" (1999 Juventus e Paraguaçuense); exigir "Relegated".
- infobox(): hoje lê pt_{ano}.txt (não existe). Baixar as páginas da Wikipédia pt de 1994-2026 para data/coleta/bra-sp-2/wikipedia/
  e ler o campo "rebaixados" (e "artilheiro", A2-021). Lista pronta no achado A2-007 e em revisao/A2/rebaixados_wiki.py.
- 1998 XV de Piracicaba: manter "rebaixado" e pôr a observação (mantido pelo licenciamento do Novorizontino).

### 3. coleta/bra-sp-2/importar.py — identidade e playoffs (A2-010, A2-012)
- NOME_MANUAL[("2002", "Portuguesa")] = 3406 (Portuguesa Santista).
- Playoffs A1 x A2 de 1979, 2002 e 2003: tirar da A2, como a repescagem de 1951 (decisão em decisoes_A2.md).

### 4. coleta/bra-sp-2/rsssf_sp2.py — leitura da página de 2001 (A2-011, A2-017)
- CORRECOES de sp2001l2.htm para ler a tabela (colunas "6/ 1/ 0" dos pênaltis); usar a tabela publicada como classificação
  (pontos da regra de 2001) e ajuste_pontos -5 do Sãocarlense; Nacional-SP 0x1 Ituano (03/03), que fecha com a tabela.

### 5. coleta/bra-sp-2/baixar_rsssf.py, edicoes.py, antigas_sp2.py, wikipedia_sp2.py — edições 1967-1978 e 1980-1984 (A2-001)
- Maior custo, maior ganho (17 edições; títulos por clube hoje errados no painel local).
- Baixar sp{ano}l2.htm de todos os anos (existem 1968, 1969, 1971, 1976, 1980, 1984) e as páginas da Wikipédia pt de 1967-1984
  (fontes novas); campeão pela FPF (lista oficial). Mesmo formato de 1947-1966 ("jogos incompletos"/"sem jogos").
- Antes: decisão EC São José x São José EC (decisoes_A2.md).

### 6. coleta/comum/rsssf.py e importar.py — datas (A2-015, A2-016)
- Data da coluna da direita nas páginas em duas colunas (1998 rodada 14), "[Feb 20)" (2010), não herdar a data da rodada anterior
  quando a página não dá (1987).
- Com 2+ dias de diferença e o ogol na mesma rodada, ficar com o ogol (1999, 2011, 2025).
- 2021 rodada 7 = 24/04 (FPF; a página da RSSSF diz 26/04): CORRECOES de sp2021l2.htm.
- Fonte nova para desempatar datas de 2007 em diante: FPF ListarTabela.ashx.
- Mudou coleta/comum: rodar de novo C, D, Copa, Paulista e A2 e comparar os totais.

### 7. coleta/bra-sp-2/rsssf_sp2.py / importar.py — jogos (A2-013, A2-014, A2-019, A2-020)
- 2006: juntar o jogo interrompido e os 45 minutos restantes (Bandeirante 0x1 União São João).
- 2008: tirar o Mogi Mirim 0x0 Oeste anulado pelo TJD (3/5).
- 2023: pênaltis 3-2 da final (Ponte Preta).
- 1961/1962: prorrogação das finais (jogos_pt.csv, coluna nota).

### 8. coleta/bra-sp-2/pacote.py — artilheiros (A2-021)
- 1998, 2003 e 2026 pela Wikipédia (junto com o item 2).

### 9. Baixos e decisões (A2-022, A2-023, A2-024 resto, A2-025, A2-027, A2-028)
- Identidades Catanduvense e Barueri/Grêmio Prudente: esperar o Guilherme.
- Grafias de cidade (FICHA_CORRIGIDA 80977 e 34451).
- Datas impossíveis vindas da própria RSSSF (1985-1988) e pênaltis de 2011: só anotar.

## banco-painel

### gerar_dashboard_v2.py / painel/index.html (A2-029)
- Antes de publicar a A2: aceitar posição repetida (1990, 1992, 1993) e colunas vazias nas edições antigas (pedido da coleta de 22/11).
- Recarregar a A2 depois das correções da coleta (o banco local e painel/dados/bra-sp-2.js já têm os erros acima).
