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
