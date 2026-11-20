"""Campeão, vice e semifinalistas de cada edição (Wikipédia pt/en: infobox, chaves e quadros das finais) x painel."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from painel import carregar
sys.stdout.reconfigure(encoding='utf-8')
# ano: (campeão, vice, outros dois semifinalistas) — conferidos nas páginas pt/en de cada edição
OF = {
 1989: ('Grêmio', 'Sport', 'Flamengo', 'Goiás'), 1990: ('Flamengo', 'Goiás', 'Náutico', 'Criciúma'),
 1991: ('Criciúma', 'Grêmio', 'Coritiba', 'Remo'), 1992: ('Internacional', 'Fluminense', 'Palmeiras', 'Sport'),
 1993: ('Cruzeiro', 'Grêmio', 'Vasco', 'Flamengo'), 1994: ('Grêmio', 'Ceará', 'Vasco', 'Linhares EC'),
 1995: ('Corinthians', 'Grêmio', 'Vasco', 'Flamengo'), 1996: ('Cruzeiro', 'Palmeiras', 'Flamengo', 'Grêmio'),
 1997: ('Grêmio', 'Flamengo', 'Corinthians', 'Palmeiras'), 1998: ('Palmeiras', 'Cruzeiro', 'Santos', 'Vasco'),
 1999: ('Juventude', 'Botafogo', 'Palmeiras', 'Internacional'), 2000: ('Cruzeiro', 'São Paulo', 'Santos', 'Atlético-MG'),
 2001: ('Grêmio', 'Corinthians', 'Coritiba', 'Ponte Preta'), 2002: ('Corinthians', 'Brasiliense', 'São Paulo', 'Atlético-MG'),
 2003: ('Cruzeiro', 'Flamengo', 'Goiás', 'Sport'), 2004: ('Santo André', 'Flamengo', '15 de Novembro', 'Vitória'),
 2005: ('Paulista', 'Fluminense', 'Cruzeiro', 'Ceará'), 2006: ('Flamengo', 'Vasco', 'Fluminense', 'Ipatinga'),
 2007: ('Fluminense', 'Figueirense', 'Botafogo', 'Brasiliense'), 2008: ('Sport', 'Corinthians', 'Vasco', 'Botafogo'),
 2009: ('Corinthians', 'Internacional', 'Coritiba', 'Vasco'), 2010: ('Santos', 'Vitória', 'Grêmio', 'Atlético-GO'),
 2011: ('Vasco', 'Coritiba', 'Avaí', 'Ceará'), 2012: ('Palmeiras', 'Coritiba', 'Grêmio', 'São Paulo'),
 2013: ('Flamengo', 'Athletico-PR', 'Goiás', 'Grêmio'), 2014: ('Atlético-MG', 'Cruzeiro', 'Flamengo', 'Santos'),
 2015: ('Palmeiras', 'Santos', 'Fluminense', 'São Paulo'), 2016: ('Grêmio', 'Atlético-MG', 'Cruzeiro', 'Internacional'),
 2017: ('Cruzeiro', 'Flamengo', 'Grêmio', 'Botafogo'), 2018: ('Cruzeiro', 'Corinthians', 'Palmeiras', 'Flamengo'),
 2019: ('Athletico-PR', 'Internacional', 'Grêmio', 'Cruzeiro'), 2020: ('Palmeiras', 'Grêmio', 'São Paulo', 'América-MG'),
 2021: ('Atlético-MG', 'Athletico-PR', 'Flamengo', 'Fortaleza'), 2022: ('Flamengo', 'Corinthians', 'Fluminense', 'São Paulo'),
 2023: ('São Paulo', 'Flamengo', 'Corinthians', 'Grêmio'), 2024: ('Flamengo', 'Atlético-MG', 'Corinthians', 'Vasco'),
 2025: ('Corinthians', 'Vasco', 'Cruzeiro', 'Fluminense'),
}
d = carregar()
ED = {e['ano']: e for e in d['ED']}
camp = vice = semi = terc = 0
for e in d['EDS']:
    a = e['ano']; c, v, s1, s2 = OF[a]; ed = ED[a]
    top4 = [r[0] for r in e['tab'][:4]]
    pos = {r[0]: r[1] for r in e['tab']}
    erros = []
    if ed['campeao'] != c: erros.append(f'campeão {ed["campeao"]} (é {c})')
    else: camp += 1
    if ed['vice'] != v: erros.append(f'vice {ed["vice"]} (é {v})')
    else: vice += 1
    if ed['terceiro'] not in (s1, s2): erros.append(f'3º {ed["terceiro"]} não foi semifinalista eliminado')
    else: terc += 1
    fora = [x for x in (s1, s2) if x not in top4]
    if fora: erros.append('semifinalista fora do top 4: ' + ', '.join(f'{x} ({pos.get(x)}º)' for x in fora))
    else: semi += 1
    print(a, 'OK' if not erros else '; '.join(erros))
print(f'campeão certo {camp}/37 · vice certo {vice}/37 · 3º é semifinalista {terc}/37 · os 2 semifinalistas no top 4 {semi}/37')
