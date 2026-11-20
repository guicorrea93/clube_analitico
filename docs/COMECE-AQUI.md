# Clube Analítico: comece aqui

Mapa do projeto para quem chega agora (pessoa ou agente). Leia este arquivo inteiro antes de
mexer em qualquer coisa. Atualizado em 20/11/2026.

O `README.md` é mais antigo e detalhado: ele descreve o painel v1 (`dashboard.html`), o banco
`brasileirao.db` e a Copa do Mundo. Use-o como referência e este arquivo como ponto de partida.

## 1. O que é o projeto

Um acervo pessoal de estatísticas de futebol com um painel para explorar os dados. Todo jogo
fica num banco SQLite, com placar, fase, rodada, data, autores dos gols, cartões e classificação.
O painel é um HTML que abre no navegador.

**Meta do dono (Guilherme):** reunir todos os campeonatos. Primeiro as Séries A, B, C e D, depois
os estaduais, e por fim as ligas nacionais da Europa, América do Sul, África, Ásia e demais.
Nas palavras dele: "estou apenas começando".

**Hoje (20/11/2026):**

| Competição | Edições | Jogos | Onde |
|---|---|---|---|
| Brasileirão Série A (com Taça Brasil, Robertão e 1937) | 70 (1937–2025) | 21.468 | `db/futebol.db` (`bra-serie-a`) |
| Brasileirão Série B (com Taça de Prata) | 44 (1971–2025) | 13.100 | `db/futebol.db` (`bra-serie-b`) |
| Brasileirão Série C (com Taça de Bronze) | 35 (1981–2025) | 7.912 | `db/futebol.db` (`bra-serie-c`), via pacote do agente de coleta |
| Copa do Mundo | 23 | 1.060 | `db/copa_mundo.db` (banco e painel à parte) |
| Copa do Brasil | só finais e participantes | — | `db/brasileirao.db` (fora do banco novo) |

## 2. Como os dados andam

```
fontes (RSSSF, ESPN, ogol, Wikipédia)
   │  coletores: historico/, serie_b/, importar_*.py
   ▼
db/brasileirao.db  ── banco antigo, uma tabela por divisão (Série B em *_serie_b)
   │  futebol/migrar_brasileirao.py   (apaga e refaz o banco novo; confere que nada se perdeu)
   │  + futebol/carregar_pacotes.py   (pacotes do agente de coleta: data/coleta/<slug>/pacote/)
   ▼
db/futebol.db      ── banco genérico: qualquer competição, de qualquer país (futebol/esquema.sql)
   │  gerar_dashboard_v2.py
   ▼
dashboard_v2.html  ── painel novo, com seletor de competição
```

- **Banco genérico** (`futebol/esquema.sql`): país, clube (com estado ou província),
  `clube_nome` (como cada fonte escreve o nome do clube e em que anos), competição (com tipo e
  nível), edição, fase, partida, gol, cartão, estatística, `classificacao_final`,
  `classificacao_rodada`, `tabela_publicada` e artilheiro. Toda linha guarda a `fonte`.
- **Cada clube existe uma vez só.** Quem jogou A e B tem um cadastro só. O nome de exibição segue
  o padrão do painel: "Botafogo", "Atlético-MG", "Brasil de Pelotas". O sufixo "-UF" aparece só
  quando há clubes com o mesmo nome. A tabela `clube_nome` guarda os outros nomes, para reconhecer
  o clube em fontes novas.
- **Competições novas** (Série C em diante) não passam pelo `brasileirao.db`. Elas chegam como
  pacotes de arquivos, descritos em `docs/agente-coleta-COMECE-AQUI.md`, e o banco genérico
  carrega esses pacotes.

## 3. Mapa dos arquivos

| Caminho | O que é |
|---|---|
| `futebol/esquema.sql` | Esquema do banco genérico. |
| `futebol/carregar_pacotes.py` | Carrega os pacotes de `data/coleta/<slug>/pacote/` no `futebol.db` e confere cada edição. |
| `futebol/migrar_brasileirao.py` | Refaz `db/futebol.db` a partir do `brasileirao.db` e confere as contagens. |
| `gerar_dashboard_v2.py` | Gera `dashboard_v2.html` a partir do `futebol.db`. Para pôr uma competição no seletor, basta uma linha em `COMPETICOES`. |
| `baixar_escudos.py` | Escudos em `data/escudos/` (Wikipédia pt). `PAGINAS` é a lista escrita à mão e prevalece; `paginas_auto.json` é a lista achada pela busca. |
| `serie_b/` | Coleta da Série B, o modelo a seguir para uma competição nova. Tem leitor da RSSSF com conferência, ESPN, ogol, Wikipédia, identidade de clubes e casamento de nomes entre fontes. |
| `historico/` | Importador da Série A antiga (1937–2002, RSSSF). |
| `importar_*.py`, `criar_banco_brasileirao.py`, `build.py` | Pipeline do banco antigo e do painel v1. |
| `data/serie_b/` | Fontes guardadas da Série B: `rsssfbrasil/`, `espn/`, `ogol/`, `wikipedia/` e `csv/` (saída). |
| `data/cache/` | Cache bruto de download. Fica fora do git (`.gitignore`). |
| `docs/serie_b_coleta.md` | Relatório da coleta da Série B, ano a ano: fontes, conferências e ocorrências. |
| `docs/manutencao_dados.md` | Comandos de manutenção, backup e reconstrução. |
| `dashboard.html`, `gerar_dashboard_html.py` | Painel v1 (antigo). Continua funcionando, mas não recebe mais novidades. |
| `dashboard_v2.html` | Painel novo. Abas: História, Por campeonato e Por clube. |

## 4. Regras da casa (valem para qualquer agente)

1. **Português sempre.** Respostas curtas, um passo por vez. O Guilherme não gosta de textão
   nem de texto explicativo longo dentro do painel.
2. **Commit e push só com aprovação explícita** do Guilherme. Nunca use `git add -A` nem
   `git add .`: adicione só os caminhos do seu trabalho.
3. **Conta do git:** nesta pasta, o git já usa a conta pessoal `guicorrea93` (configurado por
   `includeIf` no `~/.gitconfig`). Para enviar: `env -u GITHUB_TOKEN GIT_TERMINAL_PROMPT=0 git push origin main`.
   O remoto é `guicorrea93/clube_analitico`. A mensagem de commit termina com a linha de coautoria.
4. **Logs, testes e saídas temporárias vão para o scratchpad da sessão**, nunca soltos na pasta
   `Downloads/Gui/GitHub`.
5. **Backup antes de mexer no `brasileirao.db`:** `python backup.py`. O `futebol.db` é refeito
   por script e não precisa de backup.
6. **Nenhum dado entra sem conferência.** Toda coleta compara a soma dos jogos lidos com a
   tabela publicada pela fonte e registra o resultado num relatório (veja `docs/serie_b_coleta.md`).
   Quando a fonte erra, a correção fica escrita no código, com o motivo.
7. **Downloads educados:** espere entre pedidos, guarde a página baixada, não baixe de novo o que
   já tem e trate o erro 429 (esperar e tentar de novo).
8. **Os arquivos `.db` e `.html` gerados são versionados de propósito.**

## 5. Quem faz o quê (dois agentes)

| | Agente 1: banco e painel | Agente 2: coleta |
|---|---|---|
| Cuida de | `futebol/`, `db/*.db`, `gerar_dashboard_v2.py`, `dashboard_v2.html`, `baixar_escudos.py`, `data/escudos/`, `serie_b/`, `historico/` | `coleta/<competição>/` (scripts) e `data/coleta/<competição>/` (fontes e pacote) |
| Entrega | banco genérico, carregador de pacotes, painel online | pacotes de competição conferidos, mais o relatório da coleta |
| Não mexe em | pastas do agente 2 (só lê) | nada fora das pastas dele, exceto ler o banco (`db/futebol.db`, só leitura) |

O guia do agente 2 está em `docs/agente-coleta-COMECE-AQUI.md`.

Há também dois agentes de coleta internacionais (Europa e América do Sul fora o Brasil). O guia deles, com as
pastas de cada um, está em `docs/agentes-internacionais-COMECE-AQUI.md`.

## 6. Estado e próximos passos (agente 1)

- **20/11, sem commit:** painel com seletor A/B/C; Série C carregada do pacote; Novorizontino separado (GE Novorizontino até
  1999); escudos da Série B corrigidos e dos clubes novos tirados do ogol (`baixar_escudos.py --ogol`); docs de passagem.
- **Pendências:** escudos do Oeste e do União Bandeirante (Wikimedia deu 429, rodar `python baixar_escudos.py` depois);
  no celular a página fica mais larga que a tela.
- **Próximo:** cada competição num arquivo de dados separado, carregado quando escolhida (parte 2); painel online no
  Cloudflare Pages (parte 3).
- **Dúvidas abertas:** "GE Maringá" x "Grêmio Maringá" (separados); Ferroviário-PE junta "Ferroviário Recife" (1971) e
  "Ferroviário do Cabo" (1972); Malutrom e J. Malucelli são o mesmo clube com outro nome (separados).
