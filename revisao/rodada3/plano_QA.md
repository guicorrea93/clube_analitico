# Plano de correção: Séries A e B (revisor QA, 22/11/2026)

Todos os abertos das duas competições são do agente 1 (**banco-painel**). Nenhum aberto é de gravidade alta, então não há item [NO AR] de gravidade alta. Os placares e datas abaixo estão no ar: `painel/dados/bra-serie-a.js` e `bra-serie-b.js` são iguais aos publicados em https://clubeanalitico.pages.dev/dados/ (mesmo md5 em 22/11).

Ordem: gravidade x tamanho do erro x custo. Fontes novas: TM = Transfermarkt (página da temporada e ficha), BNA = Bola na Área, pt = Wikipédia pt, Hemeroteca = memoria.bn.gov.br.

## 1. Série A, `futebol/migrar_brasileirao.py`, `corrigir_serie_a` (placares e mando; custo baixo)
1. **QA-001** (média): 2001 Bahia 3x2 Ponte Preta (rodada 18) e Fluminense 3x2 Ponte Preta (quartas). TM + BNA; fecha a tabela com a en (resto do SA-012).
2. **QA-002** (média): Taça Brasil 1959: Atlético-MG 2x1 Rio Branco-ES; final em 29/03/1960; data do desempate Ceará x ABC; mando/data de 6 jogos da 1ª fase. pt + BNA.
3. **SA-017** (média): 1979 Central 0x1 Vasco (BNA + tabelas en/pt). 1984 Portuguesa 0x1 Botafogo (BNA + tabelas en/pt; confiança média). River-PI 1979 fica para a Hemeroteca.
4. **SA-024** (baixa): Brasiliense 0x1 Vasco 2005 com 'awd' e observação (sugestão já no CSV).
5. **SA-009** (média): marcar nao-e-erro (a BNA dá a ordem do banco); só mexer se o Guilherme escolher a en.

## 2. Série A, `futebol/migrar_brasileirao.py`, `datas_serie_a` (datas; custo baixo, 1 CSV)
6. **QA-003** (média): 1995 (81 sem data + 12), 1991 (18), 1999 (14), 1988, 1993, 1994; 1974 só com BNA (conferir). TM + BNA, listas em `revisao/QA/saida/datas_bra-serie-a_<ano>.csv`.
7. **SA-025** (baixa): 1996 (41), 1997 (21), 1998 (33): mesma fonte e mesmo mecanismo.
8. **TL-002** (média): fecha junto com 6 e 7; 2008-2010 marcar como resolvidos; 1963 e 1989 sem fonte nova.

## 3. Série A, outros arquivos
9. **SA-016** (média, decisão QA-D3): `historico/edicoes.py`, `EDICOES['1986']`: grupos E a H da RSSSF (braz86); Joinville x Sergipe conforme a decisão.
10. **QA-004** (baixa): 1988, pênaltis da observação para `penaltis_mandante/visitante` (`migrar_brasileirao.py` ou `historico/base.py`).
11. **SA-023** (baixa): nomes da tabela gol (sugestão já no CSV; `migrar_brasileirao.py`).
12. **CL-025** (baixa): 'Brasília EC' -> 'Brasília' (`migrar_brasileirao.py`, renomeação; `baixar_escudos.py`, chave).
13. **CL-029** (baixa): 35 cidades (`migrar_brasileirao.py`, `CIDADES`; `UF_MANUAL` do Foz do Iguaçu EC); 3 a conferir no ogol.

## 4. Série B, `serie_b/importar.py`, `CORRECOES` e afins (placares; custo baixo)
14. **QA-007** (média): 1981 Flamengo-PI 2x2 Remo em 03/02/1981 (hoje 'n/p'). BNA + pt + ogol.
15. **QA-006** (média): 1972 Atlético-BA 3x1 Central. BNA + pt + ogol.
16. **QA-010** (média): 1994 Democrata-GV 0x0 Sergipe. BNA + ogol.
17. **QA-011** (baixa): 1982 América-MG 0x1 Uberaba e Criciúma 0x1 Athletico-PR, 'awd' com placar.
18. **QA-009** (baixa): 1992 Ceará x Fortaleza, mando dos dois jogos da 1ª fase (dicionário novo `MANDO_INVERTIDO`).
19. **QA-005** (média, decisão QA-D1): 1971 Grupo A, 12 x 10 jogos; Hemeroteca antes.
20. **QA-008** (média, decisão QA-D2): 5 placares com fontes 2 x 2 (1971, 1981, 1991); Hemeroteca antes.

## 5. Série B, `serie_b/importar.py`, datas (`aplicar_ogol` + `DATAS_REVISADAS`; custo médio)
21. **RC-001** e **RV-003** (média): 1990 (35 jogos, conflitos 19 -> 0) e 1991 (388 jogos, conflitos 35 -> 11) com BNA = pt; 1998 só BNA, onde não criar conflito. Sugestões já no CSV; listas em `revisao/QA/saida/datas_bra-serie-b_<ano>.csv`.
22. **QA-012** (média) e **TL-003** (média): 2009 (54 jogos, TM = BNA); 1981 (13) e 1982 (3), BNA = pt; 1989 grupo J pelo ogol com o nome 'Esportivo Passense' (`serie_b/clubes.py`).
23. **SB-017** (baixa): 1985 (21 sem data), 1994 (22 sem data), 1997 (31), 1971 (4) só com BNA, sem criar conflito.

## 6. Série B, outros arquivos
24. **SB-013** (baixa): artilheiros 1971, 1988-1990, 2004 e 2016 (`serie_b/importar.py`, `artilheiros_rsssf` + dicionário revisado). BNA + Campeões do Futebol + en.
25. **CL-024** (baixa): escudos (Oeste: rodar `baixar_escudos.py`; União Bandeirante em `PAGINAS`; Central-RJ, Rodoviária e Serrano pelo ogol em `OUTRAS_FONTES`).

## 7. Coleta de buracos (seção 4 da ficha), quando o Guilherme mandar
- Autores dos gols da Série A 1985-2002: fichas do TM (~5.600 páginas, ~3 h). 1971-1984: ogol (parcial) e BNA (parcial); custo alto, ganho parcial.
- Árbitro das Séries A e B (o banco não tem nenhum): fichas do TM de 2009 em diante (~12.500 páginas); antes disso, só Hemeroteca.
- Público da Série A (o banco não tem nenhum): fichas do TM (2009+), BNA por edição (2008, 2015), ESPN (já usada pela coleta da B, 2010+). Série B antes de 2010: BNA (1985 quase inteira) e Hemeroteca.
- Datas da Série B 1988-1999 sem segunda fonte (BNA sozinha cria conflitos em 1988, 1989, 1992, 1994, 1995): Hemeroteca ou RSSSF Brasil quando voltar a responder.
