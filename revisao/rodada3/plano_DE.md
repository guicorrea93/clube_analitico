# Plano de correção — Campeonato Alemão (`ger-1`), revisão de 22/11/2026

Achados: `SCRATCH/achados_DE.csv`. Decisões: `SCRATCH/decisoes_DE.md`. Fontes: `SCRATCH/fontes_DE.md`.

Nenhum achado de gravidade alta: campeões, vices e rebaixados estão certos nas 63 temporadas, e todos os placares batem
com o transfermarkt (19.220) e com a Wikipédia de (17.962).

Ordem: gravidade x tamanho do erro x custo.

## coleta-europa

### `coleta/ger-1/importar.py` (tudo num commit só; depois rodar `testar_carga.py` e `documentar.py`)

1. **DE-003 (média, 102 jogos): datas erradas.**
   - Fazer um dicionário `DATAS` {(ano, mandante_esd, visitante_esd): (data, motivo)}, aplicado em `carregar_base()`
     como o `INVERTIDOS`.
   - Os 102 jogos estão em `revisao/DE/datas_corrigir.csv` (veredito que começa com "corrigir").
   - As chaves são nomes de exibição: converter para as chaves do `clubes_ger`.
   - Fonte nova: transfermarkt gesamtspielplan. Já baixado em `data/cache/revisao/DE/` (63 páginas); a coleta pode
     copiar para `data/coleta/ger-1/transfermarkt/`.
   - Custo: baixo (dicionário gerado por script).
   - Risco: baixo (2 fontes concordam em todos).
   - Depois, rodar de novo `revisao/DE/cmp_tm.py`: devem sobrar só as 11 "manter" e as 3 "dúvida".
2. **DE-002 (média, 1.555 posições da Corrida em 15 temporadas): critério de desempate.**
   - Em `main()`, trocar a escolha automática (`tentativas` / `ok[0]`, linhas ~672-679) por um critério fixo por época:
     `"media"` até 1968/69 e `"saldo"` desde 1969/70.
   - Manter a conferência de que ele reproduz a ordem oficial (1979/80 e 1999/00 têm empate total; 1999/00 se resolve
     pelo confronto direto).
   - Ajustar `crit_txt`.
   - Custo: baixo. Risco: baixo.
   - Avisar o agente 1: muda `classificacao_rodada` (Corrida) e `fases.criterio`.
   - **Olhar as outras ligas:** `esp-1`, `fra-1`, `ita-1`, `ned-1` e `por-1` usam a mesma ordem de tentativas
     ("confronto" primeiro). Isso só está certo onde o regulamento é mesmo o confronto direto (Espanha, Itália, Portugal
     em certas épocas). Na França e na Holanda (saldo), a Corrida pode ter o mesmo erro.
3. **DE-001 (média): Arminia 1971/72 com 0 pontos.**
   - Fazer um dicionário `PUNICOES` {(1971, "Arminia Bielefeld"): (-19, "perdeu todos os pontos (escândalo de 1971)")},
     somado ao `ajuste` antes da conferência.
   - Ponto delicado: as tabelas da RSSSF e da Wikipédia en mostram 19 pontos. A conferência vai acusar divergência
     nelas: explicar em `EXPLICACOES[1971]`.
   - Fonte: Wikipédia de 1971/72 (Abzug=19).
4. **DE-005 (baixa, 5 jogos): marcar `awd` e o placar de campo.**
   - Jogos: 1970/71 M'gladbach x Werder (1-1); 1976/77 Kaiserslautern x Düsseldorf (0-1); 1992/93 Uerdingen x Frankfurt
     (2-5); 1994/95 Frankfurt x Bayern (2-5); 2010/11 St. Pauli x Schalke (0-2, mantido).
   - O `TRIBUNAL` precisa aceitar o placar de campo, porque a base já traz o oficial.
   - De quebra, pôr observação nos jogos repetidos: 1988/89 Karlsruhe x M'gladbach e 1993/94 Bayern x Nuremberg
     ("Phantomtor").
5. **DE-006, DE-012, DE-013 (baixa): notas da edição** (`edicoes.observacao`).
   - Rebaixamentos fora de campo: 1964/65 Hertha, 1971/72 Arminia, 1994/95 Dresden.
   - Relegation: depende de DE-D2; recomendado só a nota, nas 28 temporadas.
   - 3º lugar dividido em 1979/80: DE-D3.
   - Um dicionário de textos por temporada.
6. **DE-007 (baixa):** trocar a `observacao` em inglês da `classificacao_final` (hth/nota da Wikipédia en, linha ~715) por
   um dicionário em português; tirar o "S04".
7. **DE-008 (baixa):** `NOMES_ARTILHEIRO` em `artilheiros()`, com os 8 nomes da lista da Wikipédia de (Aílton, Márcio
   Amoroso, Giovane Élber, Thomas Christiansen, Luca Toni, Grafite, Mario Gómez, Harry Kane).
8. **DE-009 (baixa):** `NOMES_ESPN` + `nome_espn()`, como em `coleta/esp-1/importar.py`, com os pares de
   `revisao/DE/nomes_espn.txt`. Confira o caso Leandro, que podem ser dois jogadores.

### `coleta/ger-1/baixar.py` + `importar.py` (coleta nova, quando o Guilherme mandar)

9. **DE-011 (baixa, cobertura): autores dos gols de 1963/64 a 1998/99 pela RSSSF**, já baixada.
   - Leitor dos parênteses (autor, minuto, "p", "o"); grava só quando a soma fecha com o placar.
   - Custo: médio (leitor + nomes de jogador). Ganho: cerca de 9.000 jogos com autores.
   - 1999/00 e 2000/01: spielbericht do transfermarkt, jogo a jogo (612 páginas). Custo: alto, em tempo.
10. **DE-010 (baixa, 36 jogos):** autores pela ficha do transfermarkt (spielbericht), jogo a jogo. Lista em
    `revisao/DE/jogos_sem_autor.txt`.
11. **DE-004 (baixa, 3 jogos):** conferir as 3 datas em dúvida na ficha do transfermarkt antes de mexer.

### Nova importação (depende de DE-D1)

12. **DE-014 / DE-D1:**
    - Se o Guilherme escolher B, importar a fase final de 1902/03 a 1962/63 como edições do `ger-1`. Fontes: RSSSF
      ("Germany - Championships 1902-1945 / 1947-1963", a partir de `duitchamp.html`) e a Wikipédia de ("Deutsche
      Fußballmeisterschaft AAAA").
    - Se escolher A, mudar `COMPETICAO["nome"]` e a `observacao`.

## banco-painel

1. **DE-015 (baixa):** publicar o painel. Banco e `painel/dados/ger-1.js` já estão com 2025/26 e batem com o pacote.
2. **DE-016 (baixa, já conhecido):** largura no celular (`painel/index.html`).
3. Depois das correções da coleta: recarregar o `ger-1`. Mudam datas, `classificacao_rodada` (Corrida), pontos do
   Arminia 1971/72, `awd` e observações.
