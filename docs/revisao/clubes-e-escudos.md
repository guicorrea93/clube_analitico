# Revisão: clubes e escudos (bloco E, todas as competições)

Revisor CL, 20/11/2026. Competições: Série A, Série B, Série C, Série D e Copa do Brasil.

**Resumo.** Conferi os 599 clubes do banco (1.442 presenças nas 5 competições) e olhei, um a um, os 1.431 escudos que o painel mostra.
Achei 31 problemas (1 alto, 13 médios, 17 baixos) e confirmei 3 casos suspeitos que estão certos (CL-032 a CL-034). O mais grave:
na Série C 2007 os jogos do Imperatriz estão com o Tuna Luso. Há também 6 clubes "fênix" ou trocados de ano, 5 pares de cadastros
duplicados e 7 escudos de outro clube.

Achados: `SCRATCH/achados_CL.csv` (ids CL-001 a CL-034). Listas longas: `revisao/CL/listas.txt`. Scripts: `revisao/CL/`.

## Como foi feito

- `revisao/CL/mestre.py`: tabela de todos os clubes do `futebol.db` (nome, UF, cidade, anos por competição, nomes de fonte) e o
  escudo que o painel mostra de fato (`ESCUDOS` em `painel/index.html`, nome de exibição -> `painel/escudos/<arquivo>.webp`, gerado
  por `gerar_dashboard_v2.escudos()` a partir de `data/escudos/` e de `baixar_escudos.py`).
- `revisao/CL/duplicados.py`: mesma chave de nome e UF; mesma cidade com anos que nunca se cruzam; buracos de 15+ anos; nomes de
  fonte diferentes do nome de exibição; sufixo "-UF".
- `revisao/CL/ogol_fichas.py`: cruza com as fichas do ogol guardadas pela coleta (fundação, nome completo, cidade). Pegou 15 clubes
  com fundação **depois** do primeiro ano em que jogam no painel (lista em `revisao/CL/listas.txt`).
- `revisao/CL/nomes_cruzados.py`: nome de fonte de um clube que é o nome de outro clube (achou o Tuna Luso/Imperatriz e o Operário).
- Arquivos iguais: o mesmo escudo em dois clubes (hash e imagem reduzida).
- `revisao/CL/folhas.py`: folhas de contato por competição (60 por tela, escudo + nome + UF + cidade) e print com o Chrome sem janela.
- Conferência na Wikipédia pt (API) e nas páginas da RSSSF Brasil; cache em `data/cache/revisao/CL/`.

## E1. Mesmo clube com dois cadastros

| Caso | Resultado |
|---|---|
| Americana x Guaratinguetá | mesmo clube (mudou de cidade em 2011) — **CL-013**, pergunta |
| Malutrom x J.Malucelli | mesmo clube; em 2001 a Série B está num cadastro e a Copa no outro — **CL-014**, pergunta |
| GE Maringá x Grêmio Maringá | FPF e Wikipédia unificam; mesmo escudo — **CL-015**, pergunta |
| Goiatuba x Goiatuba EC | o "Goiatuba" do banco é o Goiatuba EC (a AA Goiatuba é de 2009) — **CL-006**, pergunta |
| EC São Gabriel x São Gabriel | Série C 2002 e Copa 2004 são do São Gabriel FC (o EC é de 2013) — **CL-005**, pergunta |
| Operário-MT x CEOV Operário | o Operário tradicional (CEOV) está nos dois; 2003 e 2006 são de outro clube — **CL-007**, pergunta |
| Ariquemes x SE Ariquemes | a separação está certa, mas 1995 está no Ariquemes FC (fundado em 1996) — **CL-004** |

Os outros pares da mesma cidade com anos sem cruzar (cerca de 100) são clubes diferentes, conferidos pela ficha do ogol
(fundação e nome completo diferentes). Exemplos: Linhares EC x Linhares FC, Vitória-PE x Vitória das Tabocas, Dom Pedro x Real
Brasília, Kaburé x Colinas e Serrano-PE x Serra Talhada.

## E2. Clubes diferentes juntados num cadastro

- **CL-001 (alta)**: Série C 2007, grupo 17 da 2ª fase. Os 6 jogos do Imperatriz foram gravados como Tuna Luso, com jogos
  "Tuna Luso x Tuna Luso". A classificação do Tuna Luso (24 jogos) e a do Imperatriz (6) ficam erradas.
- **CL-002**: Série C 2002 dada ao Atlético Tubarão, fundado em 2005; o certo é o Tubarão FC.
- **CL-003**: Copa do Brasil 2007, Operário-MS no lugar do Operário de Várzea Grande (MT).
- Clubes fênix ou antecessores juntados com o clube novo, como no Novorizontino: **CL-008** Lagarto (Lagarto EC 1955-1990 x
  Lagarto FC 2009), **CL-009** Cabofriense (AA 1955 x AD 1997), **CL-010** Foz do Iguaçu (Foz do Iguaçu EC 1989 x Foz do Iguaçu FC
  1995), **CL-011** Limoeiro (EC Limoeiro 1998 x AD Limoeiro 2001) e **CL-007** Operário-MT.
- **CL-012**: Joaçaba e São Borja (1981) e Desportiva Guarabira (2001) aparecem com nome, ficha e escudo de clubes fundados depois.
- **Novorizontino**: a separação está certa (**CL-032**, Wikipédia: GE Novorizontino na B em 1989, 1991 e 1995 e na C em 1988 e
  1994). Sobrou o período 1989-2024 nos nomes de fonte do Novorizontino novo (**CL-030**).
- **"Não casar pela chave do nome"** (docs/coleta/pedidos.md): Maringá, FC Cascavel, Santa Cruz de Natal, Rio Branco de Venda
  Nova e Prudentópolis EC estão certos (**CL-033**). Goiatuba, Ariquemes e São Gabriel, não (CL-006, CL-004 e CL-005).
- Nomes de fonte que pareciam de outro clube, mas estão certos: Sobradinho em 1996 ("Botafogo Sobradinho"), Juventus de Jaraguá em
  1996 ("Jaraguá AC") e Barra do Garças ("Barra EC", 1998-2005) — **CL-034**.

## E3. Estado, cidade e nome de exibição

- Nenhuma UF do banco difere da ficha do ogol. Pontos a acertar no **CL-028**: Botafogo-DF está com UF GO, mas nos anos em que
  jogou era do Guará (DF); a AA Araguaia é de Água Boa, não de Cuiabá; há grafias a corrigir.
- **CL-029**: 42 clubes do banco sem cidade. **CL-016**: Ferroviário-PE com o nome "Ferroviário do Cabo" em 1972 (a RSSSF diz
  "Clube Ferroviário (Recife-PE)").
- **CL-025**: "Brasília EC" é o Brasília Futebol Clube.
- Sufixo "-UF" sem homônimo: 25 clubes do banco (**CL-026**) e 30 dos pacotes, mais nomes fora do padrão, como "Maringá FC 1995" e
  "São Francisco FC-AC" (**CL-027**). Homônimos sem sufixo: só o "dono" do nome fica sem sufixo (Botafogo, Santa Cruz, São
  Raimundo, Guarany, Auto Esporte...). Está coerente.
- **CL-031**: o Matsubara ainda tem o nome do ogol "JMalucelli" (1981) no `clubes.csv`.

## E4. Escudos

Para saber qual imagem aparece, segui o caminho do painel: `ESCUDOS[nome de exibição]` -> `painel/escudos/*.webp`. Esse arquivo
vem de `data/escudos/<nome>.png`, baixado pela lista à mão (`PAGINAS`), pela busca automática (`paginas_auto.json`), pelo ogol
(`ogol_auto.json`) ou por `OUTRAS_FONTES`. Nenhuma imagem está quebrada ou pequena demais.

| Competição | Clubes conferidos | Escudos olhados | Sem escudo | Escudos errados vistos nesta competição |
|---|---|---|---|---|
| Série A | 161 | 161 | 0 | Potiguar, América-CE, Desportiva-ES, Estrela do Mar-PB, Tiradentes-PI, Água Verde |
| Série B | 200 | 194 | 6 | Desportiva-ES |
| Série C | 371 | 369 | 2 | Potiguar, Desportiva-ES, Tiradentes-PI; clubes de CL-004 e CL-012 |
| Série D | 312 | 311 | 1 | Potiguar, Desportiva-ES, Rive A.C. |
| Copa do Brasil | 398 | 396 | 2 | Potiguar, Desportiva-ES |
| **Total** | **1.442 (599 clubes)** | **1.431** | **11** | |

- Escudo de outro clube: **CL-017** Potiguar (ABC), **CL-018** América-CE (América-RN), **CL-019** Desportiva-ES (Vitória-ES),
  **CL-020** Estrela do Mar-PB (Esporte de Patos) e **CL-021** Tiradentes-PI (Atlético Piauiense, de 2019). Os 5 vêm da busca
  automática (`paginas_auto.json`).
- **CL-022**: Água Verde com o escudo do Pinheiros (a página redireciona). **CL-023**: Rive A.C. com o escudo "Gálatas EC".
- **CL-024**: 6 sem escudo. Oeste e União Bandeirante são pendência já conhecida; Central-RJ, Ferroviário-PE, Rodoviária e Serrano
  estão em `SEM_ESCUDO`.
- Escudo repetido por ser o mesmo clube: Americana/Guaratinguetá, Malutrom/J.Malucelli e GE Maringá/Grêmio Maringá. Depende das
  perguntas abaixo.
- Escudo de baixa resolução, mas do clube certo: Matsubara, Atlético Pernambucano e Rioverdense. Escudo duvidoso, não registrado:
  Canoas (coroa de louros do ogol; não consegui confirmar).

## Fontes

- Wikipédia pt: artigos de cada clube citado no CSV (Goiatuba EC, AA Goiatuba, CEOV, Várzea Grande EC, Lagarto EC, Lagarto FC,
  AA e AD Cabofriense, Foz do Iguaçu FC, CA Tubarão, Tubarão FC, Ariquemes FC, São Gabriel FC, EC São Gabriel, Grêmio de Esportes
  Maringá, J.Malucelli, Guaratinguetá Futebol, Clube Ferroviário do Recife, GE Novorizontino, Sobradinho EC, GE Juventus, Barra do
  Garças FC, Estrela do Mar EC, Clube Atlético Piauiense, Associação Botafogo FC, AA Araguaia) e as edições da Copa do Brasil 2007,
  Série B 1971, 1972 e 1989 e Série C 1988.
- RSSSF Brasil (`https://rsssfbrasil.com/tablesae/`): br1981l3, br1995l3, br1996l3, br1998l3, br2001l3, br2002l3, br2004l3,
  br2007l3, br1989l2, br1972l2 e cbr2007 (listas de participantes).
- Fichas do ogol guardadas pela coleta (`data/coleta/*/ogol/clubes.json`): usadas só para achar suspeitos; a prova vem das duas
  fontes acima.

## Perguntas ao Guilherme

1. **GE Maringá x Grêmio Maringá**: juntar? A Federação Paranaense e a Wikipédia contam os títulos de 1963 e 1964 para o Grêmio
   Maringá atual, e o painel já usa o mesmo escudo nos dois. Opinião: juntar. (CL-015)
2. **Ferroviário-PE (1971 e 1972)**: é um clube só, o Ferroviário do Recife? A RSSSF e a Wikipédia dizem que sim; "Ferroviário do
   Cabo" em 1972 parece engano do ogol. Opinião: um clube só, com cidade Recife. (CL-016)
3. **Malutrom x J.Malucelli**: juntar? É o mesmo clube, que mudou de nome. Hoje, em 2001, a Série B está num cadastro e a Copa do
   Brasil no outro. Opinião: juntar. (CL-014)
4. **EC São Gabriel na Série C 2002**: o clube de 2002 é o São Gabriel FC, o mesmo da Copa 2004. Juntar os dois cadastros?
   Opinião: sim. (CL-005)
5. **Americana x Guaratinguetá**: juntar? Foi o mesmo clube, que se mudou em 2011. Barueri/Grêmio Prudente e Ipatinga/Betim já
   estão num cadastro só. (CL-013)
6. **Goiatuba x Goiatuba EC**: juntar? A Série B de 1989 a 1997 é do Goiatuba EC. Opinião: sim. (CL-006)
7. **Operário de Várzea Grande**: o Operário-MT até 1998 e o CEOV Operário são o mesmo clube? A Copa 2003 e a Série C 2006 ficam
   com o Operário FC Ltda (hoje Várzea Grande EC)? Opinião: sim, para as duas. (CL-007)
8. **Clubes fênix**: separar Lagarto, Cabofriense, Foz do Iguaçu e Limoeiro, como foi feito com o Novorizontino? Opinião: sim, pela
   coerência. (CL-008 a CL-011)
9. **Sufixo "-UF"**: vale a regra "só com homônimo no banco" ou mantemos os nomes consagrados (Americano-RJ, Fast-AM,
   Ferroviária-SP...)? (CL-026 e CL-027)

## 3ª rodada (22/11/2026): clubes da Série C, Série D e Copa do Brasil (revisor QC)

- **CL-005 a CL-012:** todos corrigidos e reconferidos em 22/11 (`docs/revisao/reconferencia-2026-11-22.md`). Do CL-007 sobra só o
  escudo trocado dos três Operário de Várzea Grande (RC-002, banco-painel: `baixar_escudos.py`).
- **Fonte nova para identidade e cidade:** o Bola n@ Área (https://www.bolanaarea.com/) lista os participantes de cada edição com
  a cidade (ex.: `serie_c_1981_tab.htm`, `serie_c_2007_partic.htm`, `copa_do_brasil_2008_fase1.htm`) e escreve o nome da época. Serve
  para o CL-029 (cidades vazias) e para conferir homônimos. O Futebol Nacional (https://futebolnacional.com.br/) também dá o nome
  da época por edição.
- **CL-028 (aberto):** sugestão completada: AA Araguaia (Série D 2016) é a Associação Atlética Araguaia, fundada em 2014 para
  substituir o Barra do Garças FC, hoje em Água Boa-MT; não confundir com o "Araguaia" (Alto Araguaia-MT, Série D 2009 e Copa
  2010), que está certo. O Bola da Série D 2010 lista "Botafogo (DF)", o que confirma a UF DF do Botafogo-DF.
- **CL-023 (aberto):** o "Rive A.C." foi o Espírito Santo FC (fundado em 2006 em Anchieta-ES) em todos os jogos do banco (Série D
  2016-2018); virou Gálatas EC em 2025 e Rive AC (Alegre) em 2026 (https://pt.wikipedia.org/wiki/Rive_Atl%C3%A9tico_Clube).
- **QC-009 (novo, baixa):** o vice da Série C 1981 aparece como "Manchete"; RSSSF, ogol de 1981, Bola e Futebol Nacional dizem
  "Santo Amaro (PE)". Junto com o CL-023, pede uma regra para clube que só jogou com outro nome (decisão QC-D1).
- Sugestões e decisões: `SCRATCH/sugestoes_QC.csv`, `SCRATCH/decisoes_QC.md` (QC-D1).
