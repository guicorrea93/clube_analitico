# Marca do Clube Analítico

Escudo escolhido em 22/11/2026: **Y2** (moldura com louros, CLUBE no alto, fita ANALÍTICO, bola-gráfico no centro e quatro barras subindo).

Arquivos publicados (em `painel/marca/`, vão para o site junto com o painel):

| arquivo | uso |
|---|---|
| `escudo.svg` | escudo completo; marca da lateral do painel |
| `icone.svg` | versão simples (escudo, faixa e bola) para tamanhos pequenos; ícone da aba |
| `favicon-32.png`, `favicon-48.png` | ícone da aba para navegadores sem SVG |
| `apple-touch-icon.png` (180 px) | atalho na tela do celular |
| `icone-512.png` | imagem grande, para redes sociais ou app |

Cores: verde `#1ecb74`, ouro `#fbbf24` → `#d9950a`, fundo `#06140c`. Fonte das letras: Barlow Condensed ExtraBold (as letras estão convertidas em desenho nos SVGs, não dependem da fonte instalada).

## Como refazer

Os scripts em `gerador/` são os das rodadas de escolha (3ª e 4ª):

- `escudos3.py`: desenhos base (louros, faixa, bola, estrelas) e a vitrine da 3ª rodada;
- `escudos4.py`: misturas e a vitrine da 4ª rodada (o Y2 está aqui, função `y2`);
- `marca.py <pasta de saída>`: gera `escudo.svg` e `icone.svg` com as letras em desenho. Precisa da fonte em `../fonte_barlow/` (BarlowCondensed-ExtraBold.ttf e -Bold.ttf, do repositório google/fonts) e do `fonttools`.

Rodar numa pasta temporária, fora do repositório: os scripts gravam vitrines em `../logo/`. Os PNGs saem de um print do Chrome em 768 px reduzido com o Pillow.
