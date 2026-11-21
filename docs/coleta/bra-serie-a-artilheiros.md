# Série A: artilheiros oficiais, de 1937 a 2025

Gerado por `python coleta/bra-serie-a-artilheiros/montar.py`. Arquivo em
`data/coleta/bra-serie-a-artilheiros/artilheiros.csv` (`temporada,jogador,clube,gols,fonte`), pedido pelo agente 1
para a revisão SA-019 a SA-023.

- **70 edições, 84 linhas** (empates de artilharia em linhas separadas). A `temporada` é a chave da edição no banco:
  "1937", "1959"... e "1967_taca_brasil", "1967_robertao", "1968_taca_brasil", "1968_robertao".
- **Fonte:** Wikipédia em inglês, "List of Campeonato Brasileiro Série A top scorers", seção "Scoring by season" (Copa dos
  Campeões Estaduais 1937, Taça Brasil, Torneio Roberto Gomes Pedrosa e Série A).
- **Conferência:** com a lista da Wikipédia em português. Todos os nomes batem, menos "Gabriel Barbosa" (2018 e 2019),
  que a lista pt chama de "Gabigol"; ficou "Gabriel Barbosa", como nos gols do banco.
- **Clube:** o nome do `futebol.db`, entre os clubes da edição; todos casaram.
- **Nome de jogo** (SA-021, SA-023): Josiel (2007), Luciano (2020), Alerrandro (2024).
- **SA-020 (2008):** Keirrison, Kléber Pereira e Washington, com 21.
- **SA-021 (2007):** Josiel com 20.
- **SA-022 (2016):** Fred com 14 (12 pelo Atlético-MG e 2 pelo Fluminense). Fica uma linha só, com o Atlético-MG, e a
  nota "gols somados de dois clubes".
- As duas páginas da Wikipédia ficam em `data/coleta/bra-serie-a-artilheiros/wikipedia/`.
