# Pedidos da revisão ao agente 1 (banco e painel)

Achados em `docs/revisao/achados.csv` (coluna `quem_corrige` = `banco-painel`). Relatórios com as provas em
`docs/revisao/<slug>.md` e `docs/revisao/clubes-e-escudos.md`.

## 20/11/2026: primeira revisão (Séries A, B, C e D e Copa do Brasil)

São 80 achados abertos para você. Abaixo, agrupados pela causa provável.

1. **Punições e tribunal fora da classificação (alta).** A classificação da Série A recalcula os pontos sem o
   `ajuste_pontos` e sem as decisões do STJD.
   - Série A: SA-001 (2013, Portuguesa 12º, mas foi rebaixada), SA-002 (2004, São Caetano), SA-003 (2003), SA-004 (2005),
     SA-005 (2018), SA-006 (2010) e SA-014 (1999, Sandro Hiroshi; aguarda decisão do Guilherme).
   - Série B: a coluna Pts da sub-aba Classificação também ignora o ajuste (SB-014). A Corrida aplica.
2. **Ordem final calculada pela soma de todas as fases, em vez da fase final (alta).**
   - Série B: SB-001 (1999), SB-002 (2001) e SB-004 (2004) têm o vice errado.
   - Série B: SB-003 (2001, os 4 da repescagem do rebaixamento aparecem em 9º a 12º) e SB-005 (2009, dois clubes em 16º).
   - Série A: SA-007 (Robertão 1968, o vice é o Internacional) e SA-008 (1992, 3º lugar; aguarda decisão).
   - Classificação antiga: SA-009, SA-015, SA-016, SA-017 e SA-018 (aguarda decisão sobre tabela oficial x soma de todos os jogos).
3. **Artilharia só com os gols que têm autor (média).** O cartão "Artilheiro" e a sub-aba Artilharia ignoram a tabela
   `artilheiro` do banco. O erro aparece nas 5 competições: SA-019, SB-012, SC-024, SD-019 e CB-012.
   Artilheiros do banco: SA-020, SA-021, SA-022, SA-023 e SB-013.
4. **Jogos e placares no banco (média):**
   - SB-006: 7 jogos duplicados;
   - placares: SB-007 a SB-010 e SA-010 a SA-013;
   - SB-011: 4 gols contra gravados do lado errado (2013);
   - especiais e datas: SA-024, SA-025 e SB-017;
   - datas impossíveis, com o mesmo clube jogando 2 vezes no mesmo dia: TL-002 (Série A 1999 e 2008 a 2010) e TL-003 (Série B 2009, 1989 e outros);
   - SB-015 e SB-016: erros copiados da RSSSF e Brusque 2021.
5. **Clubes e escudos (média e baixa):**
   - cadastros a juntar ou separar: CL-013 (Americana x Guaratinguetá), CL-014 (Malutrom x J.Malucelli), CL-015 (GE Maringá x
     Grêmio Maringá) e CL-016 (Ferroviário-PE). Todos aguardam decisão do Guilherme;
   - escudos de outro clube, quase todos do `paginas_auto.json`: CL-017 a CL-023;
   - escudos faltando: CL-024;
   - nomes de exibição e cidades: CL-025, CL-026 e CL-029 (a regra do sufixo "-UF" aguarda decisão);
   - nome de fonte que sobrou no Novorizontino: CL-030.
6. **Textos e telas (baixa):**
   - "GRUPO GRUPO A" no cabeçalho dos grupos da sub-aba Jogos, nas Séries B, C e D: TL-001 (o mesmo do CB-014);
   - SA-026 a SA-029, SB-018 a SB-020, SC-006, SC-025, CB-009 e CB-013;
   - página mais larga que a tela no celular (já conhecido): SA-030, SB-021, SC-026, SD-020 e CB-016.

Quando corrigir, avise aqui citando os ids. A revisão confere de novo e muda a `situacao` no CSV.

## Resposta do agente 1 (20/11/2026): primeira leva corrigida

Banco refeito (`futebol/migrar_brasileirao.py`) e painel gerado de novo; ainda não publicado no site.

- **Punições e ordem oficial da Série A, 2003-2025:** SA-001 a SA-006. A tabela oficial com `adjust_points` vem da
  Wikipédia en, em `futebol/oficial_serie_a.py`, com as páginas em `data/serie_a/wikipedia/`. A coluna Pts desconta a
  punição em todas as competições (SB-014).
- **Série B, em `serie_b/importar.py`:**
  - vices de 1999, 2001 e 2004 pela pontuação do grupo final (SB-001, SB-002, SB-004);
  - repescagem de 2001 nas 4 últimas posições (SB-003);
  - 2009, Juventude em 17º (SB-005);
  - 7 jogos repetidos retirados (SB-006);
  - placares corrigidos em `CORRECOES` (SB-007 a SB-010; SB-002: Figueirense 1-0 Caxias pelo STJD);
  - gol contra sem time atribuído ao lado certo, e autores descartados quando os lados não fecham (SB-011);
  - números da tabela final pelos jogos nas edições de turno único (SB-015).
- **Artilharia:** o cartão e a sub-aba usam a tabela `artilheiro` quando existe; sem ela, a sub-aba avisa quando os gols
  com autor cobrem menos de 90% (SB-012, SC-024, SD-019, CB-012). O cartão do clube virou "Maior artilheiro" (SB-019).
  A Série A não tem lista oficial no banco; isso foi pedido à coleta (SA-019).
- **"Grupo Grupo A":** corrigido (TL-001, CB-014).
- **Copa do Brasil** (CB-013):
  - classificação sem Pts;
  - cartão "Fases" no lugar de "Pontos por vitória";
  - sem lanterna nem melhor mandante e visitante;
  - sub-aba Corrida escondida quando nenhuma edição tem rodada.
- **Pênaltis:** aparecem no placar, nos Jogos da edição e do clube (CB-009).
- **Campeões invictos:** contam campanhas de 10 jogos ou mais (SC-025).
- **Temporadas seguidas:** contadas por ano, e não por edição (SA-029).
- **Subiram para a divisão de cima:** só com acesso oficial, quando o pacote traz `situacao` (SC-006).
- **Celular:** já resolvido antes (SA-030, SB-021, SC-026, SD-020, CB-016).

### Segunda leva (20/11/2026)

- **Série A, em `corrigir_serie_a` (`futebol/migrar_brasileirao.py`):**
  - SA-007: Robertão 1968 com vice Internacional, 3º Vasco e 4º Palmeiras;
  - SA-010: mando de Flamengo 2-2 Botafogo em 2009;
  - SA-011: ida da final de 1987, 1-1 em 30/01/1988;
  - SA-012: prorrogação de 2001, 2-1;
  - SA-013: desempate de 1959, Ceará 2-1 ABC, com os autores;
  - SA-027: Copa João Havelange 2000;
  - SA-028: "Copa União" com acento.
- **Escudos:**
  - CL-017, CL-019 e CL-021: Potiguar, Desportiva e Tiradentes-PI agora com o escudo do ogol;
  - CL-018, CL-020 e CL-022: América-CE, Estrela do Mar e Água Verde ficam sem escudo, porque não há fonte segura;
  - CL-023: Rive A.C. sem escudo. O nome do clube fica com a coleta.
- **Nomes de fonte do Novorizontino** divididos no ano da separação (CL-030).
- **Varreduras rodadas:** `varredura.py` e `datas_repetidas.py`.

**Ainda abertos comigo** (próxima leva):
- datas impossíveis: TL-002, TL-003, SB-017 e SA-025. Os jogos "repetidos" de 1997 na Série B que a varredura acha são ida e volta com a mesma data;
- jogos especiais: SA-024;
- faixas da tabela por ano: SA-026;
- fases em inglês e quadrangular chamado de mata-mata: SB-018;
- artilheiros da Série B que faltam: SB-013;
- escudos que faltam: CL-024. O do Oeste espera a Wikimedia liberar;
- cidades: CL-029.

**Com a coleta Brasil:**
- artilheiros da Série A: SA-019 a SA-023 (pedido em `docs/coleta/pedidos.md`);
- nomes: CL-023 e CL-025.

**Esperando decisão do Guilherme:**
- SA-008, SA-014, SA-015 a SA-018 e SB-016;
- CL-013 a CL-016;
- CL-026.

### Decisões do Guilherme (20/11/2026)

- **SA-008, 3º lugar de 1992:** fica o Bragantino em 3º e o Vasco em 4º, como já está e como diz a Wikipédia pt. Só muda
  se aparecer uma fonte oficial dizendo o contrário. Pode marcar como `nao-e-erro`.
- **SA-014, caso Sandro Hiroshi (1999):** vale a decisão do STJD. São Paulo x Botafogo e São Paulo x Internacional ficam
  0-1 com `resultado_especial` `awd`, e o placar de campo (6-1 e 2-2) fica na observação (`corrigir_serie_a`).
  Números: São Paulo 13V 1E 12D 45-35, Botafogo 8V 2E 11D 23-37, Internacional 7V 3E 11D 18-26.
- **SA-015 a SA-018, classificação antiga:** fica a soma de todos os jogos da edição (o que os jogos do banco dizem), com a
  posição final oficial. Nas edições de várias fases (e no mata-mata) a coluna Pts sai, porque essa soma não é a
  pontuação oficial. Pode marcar como `nao-e-erro`. SA-016 (1986, jogos que faltam nos grupos E a H) e SA-017
  (placares de 1979 e 1984) continuam como erro de dado.
- **SB-016, Brusque 2021:** sem punição. O Pleno do STJD devolveu os 3 pontos em 18/11/2021 (O Povo, NSC Total, Correio
  Braziliense). O Brusque fica com 48 pontos, em 13º (`AJUSTE_FALSO` em `serie_b/importar.py`).
- **CL-013 (e SB-020), Americana e Guaratinguetá:** um clube só, "Guaratinguetá", com "Americana" no `clube_nome`
  (`MESCLAR` em `futebol/migrar_brasileirao.py`). Agora a Série B fica 2010 a 2013 seguida.
- **CL-014, Malutrom e J.Malucelli:** um clube só, "J.Malucelli", com "Malutrom" no `clube_nome` (`MESCLAR`).
- **CL-015, GE Maringá e Grêmio Maringá:** um clube só, "Grêmio Maringá", como a Federação Paranaense e o ogol
  (`MESCLAR`). O "Maringá" (Maringá FC, 2010) continua à parte.
- **CL-016, Ferroviário-PE:** um clube só, renomeado "Ferroviário do Recife", com cidade Recife e escudo da Wikipédia. O
  nome de fonte "Ferroviário do Cabo" (1972), que está errado, saiu do `clube_nome` (`NOME_ERRADO` e `CIDADES` no migrar).
- **CL-024:** Ferroviário do Recife já tem escudo. Oeste e União Bandeirante ainda esperam a Wikimedia, que limita os pedidos.
- **CL-026, sufixo "-UF":** fica como está. Os 25 nomes não mudam, e a regra dos guias passou a dizer que o sufixo
  só é exigido para clube novo com homônimo (`docs/COMECE-AQUI.md`, `docs/agente-coleta-COMECE-AQUI.md`). Pode marcar
  como `nao-e-erro`.
