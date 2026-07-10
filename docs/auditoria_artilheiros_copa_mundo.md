# Auditoria de artilheiros da Copa do Mundo

Fonte externa: RSSSF, `World Cup 1930-2022 - Final Tournaments - Top-100 Goal Scorers`.

Recorte auditado: gols em fases finais de Copas do Mundo ate 2022. A Copa de 2026 fica fora desta auditoria por estar em andamento no payload local.

- Registros RSSSF comparados: 161
- Batimentos com mesmo total de gols: 161
- Divergencias de gols: 0
- Sem correspondencia automatica: 0

## Divergencias

Nenhuma divergencia de gols nos registros com correspondencia automatica.

## Sem correspondencia automatica

Todos os registros RSSSF tiveram correspondencia automatica no banco.

## Observacao

A auditoria usa `identidade_pessoa` para evitar separar o mesmo jogador por alias. Gols contra sao excluidos do total de artilharia. Quando a RSSSF usa nome completo e o banco usa nome esportivo, a rotina tenta bater por alias e, em seguida, por combinacao unica de selecao e total de gols.
