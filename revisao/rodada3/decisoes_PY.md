# Decisões para o Guilherme — par-1 (revisor PY, 22/11/2026)

### PY-028 Vice quando a lista oficial dá dois vices (1926, 1927, 1952, 1953, 1964)
- opções:
  1. seguir a Wikipédia es (River Plate 1926, Libertad 1927, Libertad 1952, Libertad 1953, Nacional 1964);
  2. seguir a ordem da tabela (hoje: Olimpia 1926, Nacional 1927, Sol de América 1952, Cerro Porteño 1953, Cerro Porteño 1964 — em 1964 a tabela do pacote está contaminada, PY-005);
  3. o primeiro nome que a RSSSF escreve (River Plate, Libertad, Sol de América, Cerro Porteño, Cerro Porteño).
- prova: https://www.rsssf.org/tablesp/parachamp.html ("1926 Nacional — River Plate and Sol de América" …); https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_de_Paraguay ; em 1926 a tabela de parahist põe Olimpia em 2º com 24 pts (https://www.rsssf.org/tablesp/parahist.html, l.905-914), contradizendo a lista da própria RSSSF.
- recomendação: opção 1 (Wikipédia es), porque ela e a RSSSF concordam em TODOS os outros 128 anos e é a única que escolhe um nome; em 1964 a RSSSF da página do ano põe Cerro e Nacional empatados com 22 pts (Cerro à frente pelo saldo), então ali a opção 2 também é defensável. Registrar a escolha em explicacoes.py.

### PY-013 Pettirossi (Encarnación, 1994) é o Silvio Pettirossi (Asunción)?
- opções: 1. separar ("Pettirossi de Encarnación", só 1994); 2. manter juntos.
- prova: https://es.wikipedia.org/wiki/Campeonato_Paraguayo_de_F%C3%BAtbol_1994 (lista "Club Pettirossi", Encarnación, estádio Carlos Memmel, fundado em 1916); https://es.wikipedia.org/wiki/Club_Silvio_Pettirossi (Asunción, fundado em 1926, "llegó a jugar en la Primera División en dos temporadas en 1970 y en el 2008"); https://www.rsssf.org/tablesp/para94.html ("Pettirossi (Encarnación)").
- recomendação: separar (são clubes diferentes, de cidades e anos de fundação diferentes).

### PY-014 Cerro Porteño (Cd. Este, 1994) é o Cerro Porteño PF (Presidente Franco, 2012-2013)?
- opções: 1. juntar em "Cerro Porteño PF"; 2. manter separados.
- prova: https://es.wikipedia.org/wiki/Club_Cerro_Porte%C3%B1o_(Presidente_Franco) ("En 1994 el equipo fue incluido junto con otros 5 clubes del interior en el nuevo Torneo Nacional"); a página de 1994 da Wikipédia es lista "Club Cerro Porteño (Presidente Franco)" entre os participantes. A RSSSF escreve "Cerro Porteño (Cd. Este)" (Presidente Franco fica colado a Ciudad del Este).
- recomendação: juntar (mesmo clube; a RSSSF só usou a cidade vizinha).

### PY-017 "Olimpia" (PAR) x "Olímpia" (BRA): nome único no mundo?
- opções: 1. aceitar (os nomes diferem pelo acento); 2. renomear o brasileiro para "Olímpia-SP"; 3. renomear o paraguaio para "Olimpia de Asunción".
- prova: tabela clube de db/futebol.db; regra "nome único no mundo" do COMECE-AQUI da coleta América do Sul (a conferência "sem acentos" do relatório da coleta não pegou esta).
- recomendação: opção 2 (o paraguaio é o "Olimpia" conhecido no Brasil, regra do guia internacional; o brasileiro segue o padrão "-UF" dos homônimos).

### PY-027 Incluir o Apertura 2026 (já terminado)?
- opções: 1. incluir agora; 2. esperar o ano fechar (Clausura 2026).
- prova: https://www.rsssf.org/tablesp/parachamp.html ("2026 Olimpia (Apertura) Nacional"); data/coleta/par-1/rsssf/para2026.html já baixada.
- recomendação: esperar o ano fechar, como nas outras ligas (só tirar a dúvida; não é erro).
