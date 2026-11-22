# Revisão: comece aqui

Estado da revisão do Clube Analítico para a próxima sessão. Atualizado em 22/11/2026.
Leia antes: `docs/COMECE-AQUI.md` (projeto) e `docs/agente-revisao-COMECE-AQUI.md` (o que conferir e como registrar).

## 1. O que já foi revisado

| Rodada | Data | O que | Prefixos dos ids |
|---|---|---|---|
| 1ª | 20/11 | Séries A, B, C, D, Copa do Brasil e clubes/escudos | SA, SB, SC, SD, CB, CL |
| 2ª | 21/11 | Reconferência do agente 1, varredura de tela, Paulista, Argentino, Uruguaio, Espanhol, Inglês | RV, TL, SP, AR, UY, ES, EN |
| 3ª | 22/11 | Reconferência dos corrigidos | RC |
| 3ª | 22/11 | Revisão profunda das novas: Italiano, Alemão, Francês, Português, Paulista A2, Chileno, Colombiano, Paraguaio, Peruano, Equatoriano | IT, DE, FR, PT, A2, CH, CO, PY, PE, EC |
| 3ª | 22/11 | Aprofundamento das já revisadas: Séries A e B; C, D e Copa; Paulista; Argentino e Uruguaio; Inglês e Espanhol | QA, QC, QS, QU, QE |

A 3ª rodada deixou a correção pronta: sugestão em cada achado, um plano por agente, as decisões num arquivo só e um
catálogo de fontes. Decisão do Guilherme (22/11): as coletas só coletam campeonatos novos; as correções começam quando
ele mandar.

## 2. Arquivos de `docs/revisao/`

| Arquivo | Para que serve |
|---|---|
| `achados.csv` | Todos os achados (formato no guia da revisão). Os abertos têm "SUGESTÃO:" em `o_que_a_fonte_diz`. |
| `decisoes-guilherme.md` | "ERRADO NO AR" (altos visíveis no site) e as 25 decisões pendentes (D-01 a D-25). |
| `plano-coleta-brasil.md` | Ids da coleta Brasil, em ordem, por arquivo do código. |
| `plano-coleta-europa.md` | Ids da coleta Europa. |
| `plano-coleta-sulamerica.md` | Ids da coleta América do Sul. |
| `plano-banco-painel.md` | Ids do agente 1 (banco, painel, escudos, Séries A e B). |
| `fontes.md` | Catálogo das fontes testadas (25), descartadas e bloqueadas. |
| `<slug>.md` | Relatório de cada competição (blocos A a F, amostras, provas). |
| `clubes-e-escudos.md` | Clubes e escudos das Séries A a D e Copa (1ª rodada). |
| `reconferencia-2026-11-21.md`, `-22.md` | Reconferências dos achados dados como corrigidos. |
| `pedidos-painel.md` | Recados da revisão ao agente 1 (e as decisões de 20/11). |

Fora daqui: `revisao/rodada3/` guarda as entregas brutas da 3ª rodada (achados_, sugestoes_, plano_, fontes_ e
decisoes_ de cada revisor). Os recados às coletas ficam em `docs/coleta/pedidos.md`, `pedidos-europa.md` e
`pedidos-sulamerica.md`.

## 3. Ferramentas

- `revisao/ferramentas/briefing-subagentes.md`: briefing comum dos subagentes. Leia a seção "3ª rodada" (vale por cima
  do resto).
- `revisao/ferramentas/tarefa-aprofundar.md`: tarefa para aprofundar uma competição já revisada.
- `revisao/ferramentas/atualizar_achados.py`: junta as entregas no `achados.csv`. Uso, na raiz do projeto:
  `python revisao/ferramentas/atualizar_achados.py <pasta> achados_XX.csv sugestoes_XX.csv reconferencia_XX.csv`.
  - `achados_*`: acrescenta os novos (ou atualiza o mesmo id);
  - `sugestoes_*` (id,sugestao): acrescenta "SUGESTÃO:" (ou "COMPLEMENTO (22/11):");
  - `reconferencia_*` (id,situacao_nova,nota): muda a situação.
- `revisao/tela/varredura.py`: o que salta aos olhos por edição (vice que não jogou a final, fases em inglês, clube
  contra ele mesmo, jogo repetido...). `revisao/tela/datas_repetidas.py`: clube com 2 jogos no mesmo dia. Copie para
  `revisao/<prefixo>/`, troque a lista de competições e rode com `python -I` na raiz.

- Decisões D-01 a D-25 respondidas pelo Guilherme em 22/11 (ver `decisoes-guilherme.md`, "Respostas do Guilherme").

## 4. Números do `achados.csv` (22/11/2026)

- 630 achados: 406 abertos, 155 corrigidos, 69 `nao-e-erro` (22/11, depois das respostas às decisões). Os planos cobrem os 406.
- Abertos por gravidade: 87 altos, 171 médios, 148 baixos.
- Abertos por quem corrige: coleta América do Sul 174, coleta Brasil 87, coleta Europa 79, banco e painel 66.
- Altos abertos já visíveis no site: 52 + 23 das competições publicadas em 22/11 às 11:18 (A2, Português, Peruano, Equatoriano; ver decisoes-guilherme.md); os 52 são (Paulista 13, Argentino 14, Chileno 9, Colombiano 6, Paraguaio 5,
  Uruguaio 3, Italiano 1, Espanhol 1).
- Mais abertos por competição: Paulista e Argentino 43 cada, A2 e Paraguaio 29, Chileno 27.

## 5. Regras aprendidas

- **Celular:** o Chrome sem janela não desce de 504 px. O corte que aparece em `--window-size=420` é do método. Para
  conferir 420 px de verdade, ponha o site num iframe de 420 px (reconferência de 21/11, SA-030, ES-020).
- **footballdatabase.eu:** limite de 50 páginas por dia por IP (os revisores dividem o IP) e página "Adblocker
  detected" depois de ~40 seguidas.
- **Bloqueiam (403):** worldfootball, weltfussball, livefutbol, fbref, kicker, fussballdaten, zerozero. Não tente contornar.
- **Fontes que copiam outras:** a Wikipédia pt cita o Bola n@ Área (Copa e Série C); muitas páginas da Wikipédia copiam a
  RSSSF. Bola + pt contra RSSSF + ogol é uma linhagem contra outra, não duas contra duas.
- **A tela só mostra parte do banco:** a marca "rebaixado" não aparece no painel (só "acesso" e "campeão"). Erro só de
  "rebaixado" está no banco, não na tela.
- **ogol:** grava o dia seguinte em jogo noturno; na Itália repete as datas da base (não serve para conferir data).
- **Jogos:** identifique por competição + data + clubes, nunca pelo `partida_id` (muda quando a coleta reimporta).
- **Wikipédia:** a API dá muito 429 quando há vários revisores; use o HTML ou espere 45 s.
- **Não reabrir** decisão do Guilherme sem prova nova (as já tomadas estão no fim de `decisoes-guilherme.md`).

## 6. Fila

1. **Competições novas para revisar** (estão no banco e em LIBERADAS, ainda sem revisão). Leia antes o "Recado de fim de
   coleta" de cada uma:
   - `ned-1` (Holanda): `docs/coleta/pedidos-europa.md`, "Recado de fim de coleta — ned-1 — 22/11/2026";
   - `sco-1` (Escócia): `docs/coleta/pedidos-europa.md`, "Recado de fim de coleta — sco-1 — 22/11/2026"
     (conferir se já está no banco);
   - `bol-1` (Bolívia): `docs/coleta/pedidos-sulamerica.md`, "Recado de fim de coleta — bol-1";
   - `ven-1` (Venezuela): `docs/coleta/pedidos-sulamerica.md`, "Recado de fim de coleta — ven-1".
   Fique de olho nos arquivos de pedidos: vêm as eras antigas de `ned-1` e `ger-1`, `bel-1`, `tur-1` e as 2ªs divisões.
2. **Quando o Guilherme responder** a `decisoes-guilherme.md`: escrever a resposta no plano do agente e no arquivo de
   pedidos.
3. **Quando um agente corrigir:** reconferir pelos ids que ele citar (pacote, banco e site) e atualizar o `achados.csv`
   com `atualizar_achados.py` (arquivo `reconferencia_*`).
4. **Fechar sem correção** (a revisão mesmo, com `reconferencia_*`): PT-001 (o pacote já tem "AD Sanjoanense" e o
   `por-1` está no banco), SP-020 e SA-009 (a 3ª fonte confirma o banco), DE-016 (falso alarme dos 504 px) e a parte
   `nao-e-erro` do SC-016 e do SC-021.
