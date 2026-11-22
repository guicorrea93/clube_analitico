# Fontes avaliadas — Série C, Série D e Copa do Brasil (revisão QC, 22/11/2026)

Scripts em `revisao/QC/`; páginas em `data/cache/revisao/QC/` (bola/, tm/, cbf/, teste/). Amostra por década: placar e data
de todos os jogos que o script casou (bem mais que 20 por década). "Casados" = jogos da fonte achados no pacote.

### Bola n@ Área (bolanaarea.com) — FONTE NOVA PRINCIPAL
- endereço: https://www.bolanaarea.com/serie_c_1981_tab.htm (Série C: serie_c_<ano>.htm + serie_c_<ano>_tab/fase1/fasefinal...); https://www.bolanaarea.com/serie_d_2013_fasefinal.htm; https://www.bolanaarea.com/copa_do_brasil_1989_tabela.htm (índices: gal_brasileirao_serie_c.htm, gal_brasileirao_serie_d.htm, gal_copa_do_brasil.htm)
- cobre: Série C 1981-2024 (inclui 1987 e 2000, fora do pacote), Série D 2009-2024, Copa do Brasil 1989-2024. Por jogo: data, estádio, placar, pênaltis ("Nos pênaltis: A 4x2 B"); nas fases finais e em muitos anos: hora, público, árbitro e autores dos gols com minuto. Por edição: classificação final, artilheiros, participantes com cidade, regulamento e "números do torneio" (jogos e gols)
- como baixar: em lote; HTML (windows-1252), 2 a 6 páginas por edição; 295 páginas no total (~13 min a 2,5 s). Leitor: `revisao/QC/bola.py`; baixador: `revisao/QC/baixar_bola.py`
- amostra (placar / data iguais ao pacote, jogos casados):
  - Série C: 1980s 242/244 e 237/244; 1990s 1.767/1.793 e 1.387/1.782; 2000s 2.390/2.407 e 1.904/2.335; 2010s 1.556/1.557 e 1.464/1.557; 2020s 1.057/1.059 e 1.031/1.059
  - Série D: 2009 85/85 e 80/85; 2010s 1.883/1.890 e 1.835/1.890; 2020s 1.686/1.690 e 1.641/1.690
  - Copa: 1989 58/59 e 50/59; 1990s 676/685 e 645/685; 2000s 1.073/1.089 e 1.048/1.089; 2010s 1.108/1.110 e 1.063/1.110; 2020s 604/606 e 598/605
  - as diferenças de data dos anos 1990-2000 da Série C são quase todas do Bola (data da rodada): em 1997, 1998, 2003-2006 o ogol concorda com o pacote em 95%; o Bola também erra placar sozinho (ex.: Série D 2014 Guarani-SC 3x4 Cabofriense, que a tabela da Wikipédia confirma, vira 0x0 no Bola; Copa 1995 Vasco 4x1 Nacional-AM vira 4x0)
  - **cuidado:** a Wikipédia pt (e às vezes a en) cita o Bola como fonte (Copa 1990, 1991, 1995, 1999, 2001; Série C 1981, 1990, 1992, 1994...). Bola + Wikipédia pt contra RSSSF + ogol é uma linhagem contra outra, não "duas contra duas" (ver QC-010, SC-016, CB-005)
- cobertura que preenche buracos do pacote: público em 853 jogos da Série C 2010s (pacote 0%), 188 nos 2000s, 649 da Série D 2010s, 865 da Copa 2010s e 351 nos 2000s; árbitro em ~1.300 jogos; autores completos (todos os gols do jogo) que faltam no pacote: Série C 2010s 865 gols, 2000s 419, 1990s 113; Série D 2010s 551; Copa 1989 129, 2000s 258, 2010s 782. Não tem autores da Copa 1990-1999 nem da Série C 1994-2001 (0-5% no Bola também). Pênaltis: 298 disputas (achou as 17 que faltam na Série D, QC-001)
- serve a: coleta-brasil; buscar: pênaltis que faltam (QC-001); terceira opinião de datas com o ogol e o transfermarkt (QC-002 a QC-006); público e árbitro (campos vazios no pacote); autores que faltam nos anos citados; cidade de cada participante e nome da época (QC-009, CL-028, CL-029); totais por edição (SC-021)

### Futebol Nacional (futebolnacional.com.br) — FONTE NOVA (já usada pelo revisor QS no Paulista)
- endereço: resumo de cada competição com o código de todas as edições: Série C https://futebolnacional.com.br/siteapp/controller.jsp?module=summary&lang=pt-br&name=FF88639175B9D71CA5BA0FEB60F782147FD12C6AFF06D23AEBD904AC62E27DA22526449B61B4766C27264E370B4B142A&state=--&country=BR ; Série D: name=FF88639175B9D71CA5BA0FEB60F78214C43668F23AD5E29950385393678F35912526449B61B4766C27264E370B4B142A ; Copa: name=51E612B97CC3E60E6BA884B54CBBEEC7 ; edição: controller.jsp?module=championship&code=<código>&lang=pt-br (ex.: Série C 1999 F72F3DB32A4CD99E31B8247A0C5C2184). Os códigos de `app/championship.jsp` (que a busca acha) NÃO servem no `siteapp`.
- cobre: campeão, vice e artilheiro de todas as edições (Série C 1981-2026, com 1981 "Santo Amaro/PE"); jogos com data, placar e notas: Série C 1998-1999 e 2007-2026 completas; 1981-1997 e 2001-2006 sem jogos (completude ~5%); Série D 2009-2026 completa (2011 metade); Copa 1989-1992, 1996, 1998-2000, 2005, 2007 e 2009-2025 completas (1999 com a preliminar Náutico 0x1 Santa Cruz, 28/01), as outras sem jogos. Autores quase nunca (nota em <40 jogos). Árbitro e público ficam na parte paga
- como baixar: em lote, 1 página por edição (91 páginas, 200 KB a 1,5 MB; o site às vezes devolve página vazia: esperar 30-60 s e repetir). Leitor: `revisao/QC/fn.py` (adaptado de `revisao/QS/fn_jogos.py`)
- amostra (placar / data iguais, jogos casados): Série C 1990s 584/590 e 570/590; 2000s 819/821 e 806/821; 2010s 1.736/1.736 e 1.665/1.736; 2020s 1.492/1.492 e 1.449/1.492. Série D 2009 149/149 e 145/149; 2010s 1.923/1.923 e 1.908/1.923; 2020s 3.538/3.541 e 3.512/3.541. Copa 1989 59/59 e 52/59; 1990s 423/426 e 354/426; 2000s 447/447 e 446/447; 2010s 1.229/1.229 e 1.200/1.229; 2020s 718/718 e 716/718. Saída: `revisao/QC/saida_fn.txt`
- serve a: coleta-brasil; buscar: terceira opinião de placar quando RSSSF e ogol divergem (achou a Série C 2007, QC-011), de data (2007-2026) e o jogo preliminar da Copa 1999 com data (CB-007); campeão, vice e artilheiro de cada edição. Risco: o próprio FN erra placares soltos (Série D 2024 Princesa x Manaus 0x1, já corrigido no pacote para 3x3 pelo SD-010) e não diz de onde tirou cada jogo

### transfermarkt.com.br — calendário completo (gesamtspielplan) e ficha de jogo
- endereço: https://www.transfermarkt.com.br/campeonato-brasileiro-serie-c/gesamtspielplan/pokalwettbewerb/BRA3/saison_id/2018 (saison_id = ano - 1; Série D: BRA4; Copa: https://www.transfermarkt.com.br/copa-do-brasil/gesamtspielplan/pokalwettbewerb/BRC/saison_id/2014); ficha: https://www.transfermarkt.com.br/spielbericht/index/spielbericht/4696369
- cobre: Série C 2009-2026, Série D 2010-2026, Copa do Brasil 1998-2026 (1998 só 14 jogos). Calendário: data, hora, placar (com os pênaltis SOMADOS e a marca "pen."), fase/grupo. Ficha: autores dos gols em ordem (às vezes com o minuto), assistências, árbitro (2010 sim; 2003 "aberto"), estádio; público e cartões não apareceram nas 2 fichas testadas
- como baixar: calendário em lote (1 página por temporada, ~350-560 KB); ficha jogo a jogo (1 página por jogo: ~3.100 Série C 2009+, ~5.000 Série D, ~3.600 Copa 1998+). Leitor: `revisao/QC/tm.py`
- amostra: 30 calendários baixados (C 2010, 2013, 2015, 2019, 2021, 2023, 2025, 2026; D 2010-2016, 2019, 2020, 2021, 2024, 2026; Copa 1998, 2001, 2003, 2008, 2010, 2014, 2015, 2018, 2021, 2024); comparação completa de placar e data em 20 deles (`revisao/QC/compara_tm.py`, saída `saida_tm.txt`). Placar (pênaltis tirados): C 2010s 468/468, 2020s 638/638; D 2010s 840/840, 2020s 956/964 (as 8 diferenças são pênaltis que faltam no pacote, QC-001); Copa 1998 14/14, 2000s 207/207, 2010s 360/360, 2020s 239/241. Data: C 2010s 415/468, 2020s 637/638; D 2010s 819/840, 2020s 960/964; Copa 2000s 137/207 (45 com +1 dia: o transfermarkt grava pelo fuso europeu em parte dos anos 2000), 2010s 332/360, 2020s 238/241. Copa 2001: dá a ida e a volta da 1ª fase no mesmo dia (14/03), como o Bola: não serve para essas datas
- serve a: coleta-brasil; buscar: terceira opinião de datas (com o Bola, QC-002 a QC-004); datas da Série C e D 2026 (o ogol dá o dia seguinte em 37 + 23 jogos noturnos); pênaltis; autores e árbitro 2009+ (jogo a jogo, quando o Bola não tiver)

### CBF — súmulas e borderôs em PDF
- endereço: https://conteudo.cbf.com.br/sumulas/2013/542186se.pdf (padrão: /sumulas/<ano>/<código><nº do jogo>se.pdf; Série C 342, Série D 542, Copa do Brasil 424, Série A 142); borderô: /sumulas/<ano>/<código><nº>b.pdf
- cobre: súmula com data, hora, estádio, árbitro e assistentes, resultado do 1º e 2º tempos, autores dos gols com minuto e tipo (pênalti, contra, falta), cartões com minuto e motivo, escalações. Achadas: Série C 2013-2025, Série D 2013 e 2015-2025 (2014 jogo 1 deu 404), Copa 2014-2025; 2009-2012 deram 404. Borderô (público e renda) é imagem escaneada (sem texto; precisa de OCR)
- como baixar: jogo a jogo (1 PDF por jogo, ~57 KB; texto com PyMuPDF/fitz); o número do jogo é sequencial na edição (Série D 2013: semifinais 185 e 186)
- amostra: 9 súmulas (Série C 2013 jogo 1, Série D 2013 jogos 185-190, Copa 2016 jogo 1): datas e placares iguais ao calendário; resolveu o SD-011
- serve a: coleta-brasil; buscar: CARTÕES (0% no pacote) e autores 2013+, árbitro 2013+; desempate oficial de data/placar 2013+. O site novo (cbf.com.br/futebol-brasileiro/tabelas/...) monta as tabelas no navegador por uma API que pede token (gweb.cbf.com.br responde "Token não fornecido"): não usei

### ogol — ficha de jogo (fonte já usada, uso novo)
- endereço: https://www.ogol.com.br/jogo/1995-04-27-vasco-nacional-am/666997
- cobre: mesmo em jogos antigos (Copa 1995): estádio, árbitro, público ("Torcedores 678"), escalações com o minuto dos gols e cartões
- como baixar: jogo a jogo (~8 mil Série C, ~6 mil Série D, ~4 mil Copa); a coleta já tem o baixador e a regra do canônico
- amostra: 1 ficha (Vasco 4x1 Nacional-AM, Copa 1995): placar, árbitro Paulo César Gomes, público 678, autores Richardson 13', França 32', Valdir Bigode 40', Clóvis 72' e Jorge Veras 89'
- serve a: coleta-brasil; buscar: autores da Copa 1990-1999 e da Série C 1994-2001 (o Bola e o transfermarkt não têm), público e árbitro desses anos. Atenção: o ogol grava o dia seguinte em jogo noturno (QC-002 a QC-004)

### Hemeroteca Digital Brasileira (Biblioteca Nacional)
- endereço: https://memoria.bn.gov.br/hdb/periodico.aspx
- cobre: jornais da época (Jornal do Brasil até 2010, Diario de Pernambuco, Correio Braziliense, entre outros): resultado, data, gols, público e renda do dia seguinte
- como baixar: só jogo a jogo e à mão (busca por palavra no leitor da página, OCR irregular); a página abre por curl (200), mas a busca e o leitor dependem de JavaScript
- amostra: não testada jogo a jogo (viável para uma dúzia de casos, não para lote)
- serve a: coleta-brasil; buscar: os empates de linhagem que nenhuma fonte digital resolve: SC-016 (1992 Nacional-AM x Tuna Luso, Rio Branco-MG x Marília; 1994 Caldas x Vila Nova-GO), CB-005 (1990 Santa Cruz x América-RN, 1991 Vitória x Remo) e a data da preliminar de 1999 (CB-007)

### Soccerway, Futebol Interior, Futpédia
- endereço: https://us.soccerway.com/national/brazil/serie-c/2013/ ; https://www.futebolinterior.com.br/campeonato/brasileiro-serie-c/ ; https://futpedia.globo.com/campeonato/copa-do-brasil/1995
- cobre: —
- como baixar: o Soccerway e o Futebol Interior mandam qualquer endereço antigo para a página inicial (site novo em JavaScript); a Futpédia não respondeu
- amostra: nenhuma
- serve a: — (não usar)
