# Plano de correção — ita-1 (revisão de 22/11/2026)

Ordem: gravidade x tamanho x custo. Ids em `achados_IT.csv`; decisões em `decisoes_IT.md`.

## coleta-europa

### coleta/ita-1/importar.py — classificação e rebaixados (alto efeito, custo baixo)
1. **IT-001 (alta)** 1945/46: dicionário `NAO_REBAIXADOS = {1945: {"Andrea Doria": "fundiu-se na Sampdoria (1946)", "Sampierdarenese": idem, "Ancona Calcio"/"US Palermo"/"Pescara Calcio"/"Salernitana Calcio 1919"/"AC Siena": "clube da Serie B no torneio misto; voltou à Serie B"}}`, aplicado no bloco "rebaixados: quem não está na 1ª divisão no ano seguinte". Fonte: Wiki it Divisione_Nazionale_1945-1946.
2. **IT-002 (alta)** 1947/48: `DECLASSADOS = {1947: ("SSC Napoli", "declassado ao último lugar por tentativa de corrupção")}` move o Napoli para 21º depois de ler a ordem oficial. Fonte: Wiki it Serie_A_1947-1948.
3. **IT-012 (baixa, D-IT-03)** `READMITIDOS` com observacao em 1942/43 (Bari, Sampierdarenese), 1954/55 (SPAL, Pro Patria), 2005/06 (Messina).
4. **IT-016 (baixa)** 1945/46: números do grupo final para os 8 finalistas (bloco `if a == DIVISIONE`, `calc_final`).
5. **IT-014 (baixa, D-IT-05)** ordem da Wiki it (classifica avulsa) em 1982/83, 1986/87, 1987/88, 1988/89, 1989/90, 1991/92, 1993/94 (`python -I revisao/IT/inversoes.py`).

### coleta/ita-1/importar.py — placares (TRIBUNAL e CORRECOES)
6. **IT-003** `TRIBUNAL[(1929, "US Cremonese", "AC Milan")] = (0, 2, ...)` (em campo 0-3).
7. **IT-004** `TRIBUNAL[(1930, "Legnano", "Lazio Roma")] = (0, 2, ...)` (em campo 0-1).
8. **IT-005** `TRIBUNAL[(1963, "AS Bari", "Genoa CFC")] = (0, 2, ...)` (em campo 1-2).
9. **IT-006** `CORRECOES[(1952, "Torino FC", "US Palermo")] = (3, 1, ...)`.
10. **IT-007** `CORRECOES[(1962, "SSC Napoli", "US Palermo")] = (3, 1, ...)`.
    - Em todos: tirar a explicação "a Wikipédia erra gols" de `EXPLICACOES` para esses clubes (1929, 1930, 1952, 1962, 1963). Depois disso as tabelas da Wiki en devem fechar nessas temporadas.
11. **IT-010 (baixa)** marcar `awd` nos 31 jogos de `revisao/IT/tavolino_sem_awd.txt` (placar já certo; só a marca e o motivo).

### coleta/ita-1/importar.py — datas (maior volume)
12. **IT-008** 622 jogos: ler `revisao/IT/datas_corrigir.csv` (copiar para `data/coleta/ita-1/` como `correcoes_datas.csv`) e trocar a data em `carregar_base`, depois de `INVERTIDOS`; em 1947/48 também em `reparar` (hoje põe a data do ogol, que tem o mesmo erro). Alternativa mais geral: ler as datas da RSSSF (`revisao/IT/rsssf_datas.py` mostra como) e trocar quando a RSSSF e a Wiki it concordam contra a base. Importante: o ogol NÃO serve para conferir data (repete a base em 606 dos 622).
13. **IT-009** 1945/46 (14 jogos do Centro-Sul, `python -I revisao/IT/datas_1945.py`) e 2001/02 Brescia x Lecce (16/09/2001): mesmo mecanismo.
    - Conferir depois com `python -I revisao/IT/varredura.py` (não pode sobrar "clube 2 jogos no mesmo dia").

### Decisões antes de mexer
14. **IT-017 (D-IT-01)** campeonatos 1898-1929: `edicoes.py` e `importar.py`, só se aprovado.
15. **IT-018 (D-IT-04)** spareggi: fase "Desempate", só se aprovado.

## banco-painel
1. **IT-013 (média)** `gerar_dashboard_v2.py` + `painel/index.html`: mostrar o ajuste de pontos na Classificação ("58 (-30)") e a `observacao` da edição na nota (punições, "Juventus rebaixada ao último lugar"). Vale para todas as ligas com punição.
2. **IT-011 (média, D-IT-02)** participações/estreantes/"volta" sem os clubes da Serie B de 1945/46, se aprovado (precisa de marca no pacote).
3. **IT-015 (baixa)** publicar o ita-1 com 2025/26 (site está com 94 edições).
4. Recarregar o ita-1 depois das correções da coleta.

## Fontes novas a usar
- Wikipédia it por temporada (Calendario, Tabellone, Note, Spareggi): leitor pronto em `revisao/IT/itwiki.py`.
- RSSSF por temporada (já no cache da coleta) para datas e motivos de "a tavolino": `revisao/IT/rsssf_datas.py`.
- Páginas de clube da Wiki it e transfermarkt como terceira opinião de placar.
