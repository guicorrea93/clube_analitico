"""Grava SCRATCH/sugestoes_QE.csv (id,sugestao) para os achados abertos de eng-1 e esp-1 sem SUGESTÃO."""
import csv, sys
SCRATCH = sys.argv[1]
BDF = "https://www.bdfutbol.com/es/p/p.php?id="
S = {
"ES-011": "Nota curta na edição (o banco já tem o texto em edicao.observacao): 1979/80 'CD Málaga perdeu 3 pontos (W.O. contra o AD Almería em 30/03/1980).'; 2003/04 'Racing Santander perdeu 1 ponto.'; 2014/15 'Almería perdeu 3 pontos (punição da FIFA). O Elche (13º) foi rebaixado por dívidas com o fisco e o Eibar (18º) ficou.'; 1994/95 'Albacete (17º) e Valladolid (19º) ficaram com a ampliação para 22 clubes (caso Celta e Sevilla).'; 1986/87 'Fase final em 3 grupos; liguilla de rebaixamento entre Osasuna, Cádiz e Racing, que caiu.' Fonte: edicao.observacao do banco (vem de coleta/esp-1/importar.py, EXPLICACOES/LIGUILLA) e https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_de_Espa%C3%B1a_2014-15 (notas da tabela). Mexer em: gerar_dashboard_v2.py, notas() e NOTAS (linhas ~186-197): além de NOTAS, transformar edicao.observacao 'punições: X -N pontos' em 'X perdeu N pontos.' para ligas estrangeiras; o painel já mostra e.nota no Pódio (cp-nota).",
"ES-012": f"Escudos da época: CD Málaga = https://www.bdfutbol.com/i/eg/175f.png (escudo 'C.D.M.', 200 px) e AD Almería = https://www.bdfutbol.com/i/eg/174.png (escudo 'A.D. Almería', 200 px), conferidos à vista (prints em SCRATCH/QE/cdmalaga_175f.png e adalmeria_174.png); páginas da temporada 1979/80 do BDFutbol (https://www.bdfutbol.com/es/t/t1979-80.html). pt.wikipedia não tem as páginas; es.wikipedia tem, mas sem imagem. Mexer em: baixar_escudos.py, OUTRAS_FONTES (linha ~156) com 'CD Málaga' e 'AD Almería', e ERRADOS/ogol_auto para o --ogol não voltar a pôr o do Málaga e da UD Almería; apagar data/escudos/ dos dois e rodar de novo.",
"ES-013": "decisão: ver decisoes (SCRATCH/decisoes_QE.md, ES-013)",
"EN-009": "Mostrar '↓ caiu' em 'No ano seguinte' para quem tem classificacao_final.situacao='rebaixado' (2 a 4 por temporada; ex.: 1987/88 Chelsea, Portsmouth, Watford e Oxford United) e '↑ subiu' em 'Chegou' para quem não estava na edição anterior (menos a 1ª edição). Fonte: banco (classificacao_final.situacao, conferida nas 126 temporadas pela 2ª rodada). Mexer em: gerar_dashboard_v2.py: levar os rebaixados de cada edição para EDS (campo novo, ex.: 'rb', ao lado do 'ac' da linha ~693) e, no JS de Participantes (função seta, ~linha 1996), quando v===0 e o clube estiver em e.rb escrever '↓ caiu' (sem nome de divisão); idem '↑ subiu' quando veio===0 e há edição anterior. Vale para todas as ligas estrangeiras (sem 2ª divisão no banco).",
"EN-010": "Nota curta na edição: 1890/91 'Sunderland perdeu 2 pontos (jogador sem registro).'; 1990/91 'Arsenal perdeu 2 pontos e Manchester United 1 (briga em campo, 20/10/1990).'; 1996/97 'Middlesbrough perdeu 3 pontos (não compareceu ao jogo com o Blackburn, 21/12/1996).'; 2009/10 'Portsmouth perdeu 9 pontos (administração judicial).'; 2023/24 'Everton perdeu 8 pontos e Nottingham Forest 4 (regras de lucro e sustentabilidade).' Fonte: edicao.observacao do banco e https://en.wikipedia.org/wiki/2023%E2%80%9324_Premier_League (notas da tabela). Mexer em: gerar_dashboard_v2.py, notas()/NOTAS (linhas ~186-197), como no ES-011.",
"EN-013": "Texto dentro do cartão: quebrar a linha dos escudos (CSS .cu-um{flex-wrap:wrap} ou mostrar no máximo 4 escudos e '+N'). Fonte: print SCRATCH/EN/cur/campeoes.png (7 escudos em 1 linha). Mexer em: gerar_dashboard_v2.py, CSS da linha ~1208 (.cu-jogo,.cu-um) e a função varios (linha ~1803). Conferir também no celular (420 px) depois do RC-003, que muda a lista.",
"EN-016": ("Autores dos 12 jogos pelo BDFutbol (ficha de cada jogo; todas fecham com o placar): "
  f"2002/03 West Bromwich 1-0 Southampton (14/09/2002): Sean Gregan 80' ({BDF}610818); "
  f"2002/03 Sunderland 1-3 Charlton (01/02/2003): Kevin Phillips 81'; Stephen Wright 24' (contra), Michael Proctor 29' e 32' (contra), os 3 a favor do Charlton ({BDF}611018); "
  f"2002/03 Fulham 2-1 Aston Villa (08/02/2003): Steed Malbranque 14', Jon Harley 36'; Gareth Barry 3' ({BDF}611026); "
  f"2003/04 Leeds 2-1 Manchester City (22/03/2004): Stephen McPhail 23', Mark Viduka 76'; Nicolas Anelka 44' ({BDF}611432); "
  f"2004/05 Tottenham 2-3 Charlton (06/11/2004): Robbie Keane 69', Jermain Defoe 79'; Shaun Bartlett 17' e 39', Jerome Thomas 50' ({BDF}611643); "
  f"2006/07 West Ham 0-2 Wigan (06/12/2006): David Cotterill 51', Jonathan Spector 58' (contra) ({BDF}612435); "
  f"2010/11 Everton 1-4 West Bromwich (27/11/2010): Tim Cahill 42'; Paul Scharner 16', Chris Brunt 26', Somen Tchoyi 76', Youssuf Mulumbu 87' ({BDF}613952); "
  f"2011/12 Everton 2-0 West Bromwich (31/03/2012): Leon Osman 18', Victor Anichebe 68' ({BDF}614493); "
  f"2013/14 Manchester City 4-1 Manchester United (22/09/2013): Sergio Agüero 16' e 47', Yaya Touré 45', Samir Nasri 50'; Wayne Rooney 87' ({BDF}614998); "
  f"2014/15 Manchester City 1-0 Manchester United (02/11/2014): Sergio Agüero 63' ({BDF}618794; com ele a artilharia calculada de 2014/15 fica Agüero 26, a oficial); "
  f"2016/17 Liverpool 2-2 West Ham (11/12/2016): Adam Lallana 5', Divock Origi 48'; Dimitri Payet 27', Michail Antonio 39' ({BDF}619637); "
  f"2016/17 Stoke City 1-1 Everton (01/02/2017): Peter Crouch 7'; Ryan Shawcross 39' (contra, a favor do Everton) ({BDF}619717). "
  "Lista em revisao/QE/amostra_fichas_saida.txt (linhas EN-016). Mexer em: coleta/eng-1/importar.py, dicionário novo GOLS_MANUAIS {(ano, mandante, visitante): [(lado, jogador, minuto, tipo)]} usado no ramo em que a ESPN não fecha (linhas ~563-577, 'gols da ESPN não batem'), com fonte 'BDFutbol'. Os cartões desses jogos também estão nas fichas."),
}
with open(f"{SCRATCH}/sugestoes_QE.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f); w.writerow(["id", "sugestao"])
    for k, v in S.items(): w.writerow([k, v])
print(len(S))
