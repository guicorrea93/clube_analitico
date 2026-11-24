"""Cadastro dos clubes do campeonato da Alemanha Oriental (gdr-1).

Identidade pela linhagem do clube (como na Wikipédia), através das mudanças de nome e de cidade impostas na RDA:
- Hansa Rostock: Empor Lauter, levado para Rostock em 1954 (SC Empor Rostock), Hansa em 1965;
- Union Berlin: Union Oberschöneweide, Motor Oberschöneweide (1. FC Union Berlin desde 1966);
- Dynamo Dresden: Volkspolizei Dresden, SG Dynamo Dresden (campeã de 1952/53), 1. FC Dynamo Dresden;
- BFC Dynamo: SC Dynamo Berlin (1954), Berliner FC Dynamo (1966), FC Berlin (1990);
- Vorwärts Frankfurt/Oder: KVP Leipzig, ASK/ZASK Vorwärts Berlin, FC Vorwärts Berlin, levado a Frankfurt/Oder em 1971,
  FC Viktoria 91;
- VfB Leipzig: SC Lokomotive Leipzig, SC Leipzig (1963), 1. FC Lokomotive Leipzig (1966), VfB Leipzig desde 1991 (o
  mesmo clube do ger-1);
- Chemie Leipzig: ZSG Industrie Leipzig, BSG Chemie Leipzig (1950-1954 e de novo em 1963), FC Sachsen Leipzig (1990);
- Hallescher FC: Union Halle, Turbine Halle, SC Chemie Halle(-Leuna), Hallescher FC Chemie;
- Rot-Weiß Erfurt: KWU Erfurt, Turbine Erfurt, SC Turbine Erfurt;
- Chemnitzer FC: Chemie Karl-Marx-Stadt, SC Motor Karl-Marx-Stadt, SC Karl-Marx-Stadt, FC Karl-Marx-Stadt;
- Erzgebirge Aue: Wismut Aue (SC Wismut Karl-Marx-Stadt de 1954 a 1963, mas jogando em Aue);
- FSV Zwickau: Horch Zwickau, Motor Zwickau, Sachsenring Zwickau;
- Carl Zeiss Jena: Motor Jena, SC Motor Jena; 1. FC Magdeburg: SC Aufbau Magdeburg;
- Einheit Dresden: Rotation Dresden (SC Einheit Dresden em 1954); Rotation Leipzig fica separado (entrou no SC Leipzig em
  1963, fusão).

Os clubes que também jogaram a Bundesliga usam a chave e o nome de exibição do cadastro alemão (clubes_ger): Hansa
Rostock, Union Berlin, Dynamo Dresden, Energie Cottbus, Carl Zeiss Jena e VfB Leipzig.

esd(nome) -> chave (None se não conhecer). exibicao(chave) -> nome do painel. CLUBES: só os clubes deste cadastro (os
do cadastro alemão vêm de clubes_ger.CLUBES).
"""
from __future__ import annotations

import re
import unicodedata

import clubes_ger

DO_GER = {"Hansa Rostock", "1. FC Union Berlin", "Dynamo Dresden", "Energie Cottbus", "Carl Zeiss Jena", "VfB Leipzig"}

# chave -> (exibição, cidade, país)
CLUBES: dict[str, tuple[str, str | None, str]] = {
    "BFC Dynamo": ("BFC Dynamo", "Berlim", "GER"), "1. FC Magdeburg": ("1. FC Magdeburg", "Magdeburgo", "GER"),
    "Hallescher FC": ("Hallescher FC", "Halle", "GER"), "Rot-Weiß Erfurt": ("Rot-Weiß Erfurt", "Erfurt", "GER"),
    "Chemnitzer FC": ("Chemnitzer FC", "Chemnitz", "GER"), "Erzgebirge Aue": ("Erzgebirge Aue", "Aue", "GER"),
    "FSV Zwickau": ("FSV Zwickau", "Zwickau", "GER"),
    "Vorwärts Frankfurt/Oder": ("Vorwärts Frankfurt/Oder", "Frankfurt (Oder)", "GER"),
    "Chemie Leipzig": ("Chemie Leipzig", "Leipzig", "GER"), "Rotation Leipzig": ("Rotation Leipzig", "Leipzig", "GER"),
    "Einheit Ost Leipzig": ("Einheit Ost Leipzig", "Leipzig", "GER"), "Einheit Dresden": ("Einheit Dresden", "Dresden", "GER"),
    "SG Friedrichstadt": ("SG Friedrichstadt", "Dresden", "GER"),
    "Aktivist Brieske-Senftenberg": ("Aktivist Brieske-Senftenberg", "Senftenberg", "GER"),
    "Franz Mehring Marga": ("Franz Mehring Marga", "Senftenberg", "GER"),
    "Rotation Babelsberg": ("Rotation Babelsberg", "Potsdam", "GER"), "Lokomotive Stendal": ("Lokomotive Stendal", "Stendal", "GER"),
    "Motor Dessau": ("Motor Dessau", "Dessau", "GER"), "Stahl Altenburg": ("Stahl Altenburg", "Altenburg", "GER"),
    "Fortschritt Meerane": ("Fortschritt Meerane", "Meerane", "GER"), "Motor Gera": ("Motor Gera", "Gera", "GER"),
    "Wismut Gera": ("Wismut Gera", "Gera", "GER"), "Motor Wismar": ("Motor Wismar", "Wismar", "GER"),
    "Vorwärts Schwerin": ("Vorwärts Schwerin", "Schwerin", "GER"), "Stahl Thale": ("Stahl Thale", "Thale", "GER"),
    "Turbine Weimar": ("Turbine Weimar", "Weimar", "GER"), "SG Lichtenberg 47": ("SG Lichtenberg 47", "Berlim", "GER"),
    "VfB Pankow": ("VfB Pankow", "Berlim", "GER"), "Fortschritt Weißenfels": ("Fortschritt Weißenfels", "Weißenfels", "GER"),
    "SC Neubrandenburg": ("SC Neubrandenburg", "Neubrandenburg", "GER"), "Motor Steinach": ("Motor Steinach", "Steinach", "GER"),
    "Motor Suhl": ("Motor Suhl", "Suhl", "GER"), "Chemie Zeitz": ("Chemie Zeitz", "Zeitz", "GER"),
    "Chemie Böhlen": ("Chemie Böhlen", "Böhlen", "GER"), "Chemie Buna Schkopau": ("Chemie Buna Schkopau", "Schkopau", "GER"),
    "Fortschritt Bischofswerda": ("Fortschritt Bischofswerda", "Bischofswerda", "GER"),
    "Stahl Brandenburg": ("Stahl Brandenburg", "Brandenburg an der Havel", "GER"),
    "Stahl Eisenhüttenstadt": ("Stahl Eisenhüttenstadt", "Eisenhüttenstadt", "GER"),
    "Stahl Riesa": ("Stahl Riesa", "Riesa", "GER"), "Vorwärts Stralsund": ("Vorwärts Stralsund", "Stralsund", "GER"),
    # só no campeonato da zona soviética (1948 e 1949)
    "Fortuna Babelsberg": ("Fortuna Babelsberg", "Potsdam", "GER"),
    "Mecklenburg Schwerin": ("FC Mecklenburg Schwerin", "Schwerin", "GER"),
    "SG Cottbus-Ost": ("SG Cottbus-Ost", "Cottbus", "GER"), "Sportfreunde Burg": ("Sportfreunde Burg", "Burg", "GER"),
    "SG Sömmerda": ("SG Sömmerda", "Sömmerda", "GER"), "SG Weimar-Ost": ("SG Weimar-Ost", "Weimar", "GER"),
}

# grafia (sem siglas de forma BSG/SG/ZSG/SC/FC; ver chave()) -> chave
NOMES: dict[str, str] = {
    # cadastro alemão
    "Empor Lauter": "Hansa Rostock", "Empor Rostock": "Hansa Rostock", "Hansa Rostock": "Hansa Rostock",
    "Union Oberschöneweide": "1. FC Union Berlin", "Motor Oberschöneweide": "1. FC Union Berlin",
    "Motor Oberschöneweide Berlin": "1. FC Union Berlin", "Union Berlin": "1. FC Union Berlin",
    "Volkspolizei Dresden": "Dynamo Dresden", "Dynamo Dresden": "Dynamo Dresden",
    "Energie Cottbus": "Energie Cottbus", "Motor Jena": "Carl Zeiss Jena", "Carl Zeiss Jena": "Carl Zeiss Jena",
    "Lokomotive Leipzig": "VfB Leipzig", "Leipzig": "VfB Leipzig",
    # este cadastro
    "Dynamo Berlin": "BFC Dynamo", "Berliner FC Dynamo": "BFC Dynamo", "Berlin": "BFC Dynamo", "BFC Dynamo": "BFC Dynamo",
    "Aufbau Magdeburg": "1. FC Magdeburg", "Magdeburg": "1. FC Magdeburg",
    "Union Halle": "Hallescher FC", "Turbine Halle": "Hallescher FC", "Chemie Halle-Leuna": "Hallescher FC",
    "Chemie Halle": "Hallescher FC", "Hallescher FC Chemie": "Hallescher FC",
    "KWU Erfurt": "Rot-Weiß Erfurt", "Turbine Erfurt": "Rot-Weiß Erfurt", "Rot-Weiß Erfurt": "Rot-Weiß Erfurt",
    "Chemie Karl-Marx-Stadt": "Chemnitzer FC", "Motor Karl-Marx-Stadt": "Chemnitzer FC", "Karl-Marx-Stadt": "Chemnitzer FC",
    "Chemnitzer FC": "Chemnitzer FC",
    "Wismut Aue": "Erzgebirge Aue", "Wismut Karl-Marx-Stadt": "Erzgebirge Aue",
    "Wismut Karl-Marx-Stadt (Aue)": "Erzgebirge Aue",
    "Horch Zwickau": "FSV Zwickau", "Motor Zwickau": "FSV Zwickau", "Sachsenring Zwickau": "FSV Zwickau",
    "Vorwärts KVP Leipzig": "Vorwärts Frankfurt/Oder", "Vorwärts der KVP Leipzig": "Vorwärts Frankfurt/Oder",
    "ASK Vorwärts Berlin": "Vorwärts Frankfurt/Oder", "ZASK Vorwärts Berlin": "Vorwärts Frankfurt/Oder",
    "Vorwärts Berlin": "Vorwärts Frankfurt/Oder", "Vorwärts Frankfurt/Oder": "Vorwärts Frankfurt/Oder",
    "Vorwarts Frankfurt/Oder": "Vorwärts Frankfurt/Oder", "Viktoria 91 Frankfurt/Oder": "Vorwärts Frankfurt/Oder",
    "Industrie Leipzig": "Chemie Leipzig", "Chemie Leipzig": "Chemie Leipzig", "Chemie Leipzi": "Chemie Leipzig",
    "Sachsen Leipzig": "Chemie Leipzig", "Rotation Leipzig": "Rotation Leipzig", "Einheit Ost Leipzig": "Einheit Ost Leipzig",
    "Rotation Dresden": "Einheit Dresden", "Einheit Dresden": "Einheit Dresden",
    "Friedrichstadt": "SG Friedrichstadt", "Dresden-Friedrichstadt": "SG Friedrichstadt",
    "Aktivist Brieske-Ost": "Aktivist Brieske-Senftenberg", "Aktivist Brieske-Senftenberg": "Aktivist Brieske-Senftenberg",
    "Franz Mehring Marga": "Franz Mehring Marga",
    "MV Babelsberg": "Rotation Babelsberg", "Märkische Volkstimme Babelsberg": "Rotation Babelsberg",
    "Märkische Volksstimme Babelsberg": "Rotation Babelsberg", "Rotation Babelsberg": "Rotation Babelsberg",
    "Hans Wendler Stendal": "Lokomotive Stendal", "Eintracht Hans Wendler Stendal": "Lokomotive Stendal",
    "Lokomotive Stendal": "Lokomotive Stendal",
    "Waggonbau Dessau": "Motor Dessau", "Motor Dessau": "Motor Dessau",
    "Altenburg": "Stahl Altenburg", "Stahl Altenburg": "Stahl Altenburg",
    "Einheit Meerane": "Fortschritt Meerane", "Fortschritt Meerane": "Fortschritt Meerane",
    "Gera Süd": "Motor Gera", "Motor Gera": "Motor Gera", "Wismut Gera": "Wismut Gera",
    "Anker Wismar": "Motor Wismar", "Motor Wismar": "Motor Wismar", "Vorwärts Schwerin": "Vorwärts Schwerin",
    "Stahl Thale": "Stahl Thale", "Turbine Weimar": "Turbine Weimar",
    "Lichtenberg 1947": "SG Lichtenberg 47", "Lichtenberg 1947 Berlin": "SG Lichtenberg 47",
    "Pankow": "VfB Pankow", "Pankow Berlin": "VfB Pankow", "Einheit Pankow": "VfB Pankow", "Einheit Pankow Berlin": "VfB Pankow",
    "Fortschritt Weißenfels": "Fortschritt Weißenfels", "Neubrandenburg": "SC Neubrandenburg",
    "Motor Steinach": "Motor Steinach", "Motor Suhl": "Motor Suhl", "Chemie Zeitz": "Chemie Zeitz",
    "Chemie Böhlen": "Chemie Böhlen", "Chemie Buna Schkopau": "Chemie Buna Schkopau",
    "Fortschritt Bischofswerda": "Fortschritt Bischofswerda",
    "Stahl Brandenburg": "Stahl Brandenburg", "Stahl Eisenhüttenstadt": "Stahl Eisenhüttenstadt",
    "Eisenhüttenstädter FC Stahl": "Stahl Eisenhüttenstadt", "Stahl Riesa": "Stahl Riesa",
    "Vorwärts Stralsund": "Vorwärts Stralsund",
    # grafias da Wikipédia
    "Einheit Ost": "Einheit Ost Leipzig", "Eisenhüttenstädter Stahl": "Stahl Eisenhüttenstadt",
    "F.C. Hansa Rostock": "Hansa Rostock", "Rot-Weiss Erfurt": "Rot-Weiß Erfurt", "Rot-Weiß Erfurtni": "Rot-Weiß Erfurt",
    "Viktoria 91 Frankfurt": "Vorwärts Frankfurt/Oder", "Vorwärts Frankfurt": "Vorwärts Frankfurt/Oder",
    "Viktoria Frankfurt (Oder)": "Vorwärts Frankfurt/Oder", "FSV Zwickau": "FSV Zwickau", "HFC Chemie": "Hallescher FC",
    "Lichtenberg 47": "SG Lichtenberg 47", "Deutsche Volkspolizei Dresden": "Dynamo Dresden",
    "Vorwärts der HVA Leipzig": "Vorwärts Frankfurt/Oder", "Vorwärts HVA Leipzig": "Vorwärts Frankfurt/Oder",
    "Vorwärts der KVP Berlin": "Vorwärts Frankfurt/Oder", "Vorwärts KVP Berlin": "Vorwärts Frankfurt/Oder",
    "ZSK Vorwärts Berlin": "Vorwärts Frankfurt/Oder",
    # 1948 e 1949 (pela linhagem; o alvo do link da Wikipédia decide quando há)
    "Planitz": "FSV Zwickau", "Zwickau-Planitz": "FSV Zwickau", "Freiimfelde Halle": "Hallescher FC",
    "Fortuna Erfurt": "Rot-Weiß Erfurt", "Eintracht Stendal": "Lokomotive Stendal", "Meerane": "Fortschritt Meerane",
    "Babelsberg": "Fortuna Babelsberg", "Fortuna Babelsberg": "Fortuna Babelsberg", "Schwerin": "Mecklenburg Schwerin",
    "Mecklenburg Schwerin": "Mecklenburg Schwerin", "Wismar-Süd": "Motor Wismar", "Wismar Süd": "Motor Wismar",
    "Anker Wismar": "Motor Wismar", "Friedrichstadt Dresden": "SG Friedrichstadt", "Altenburg-Nord": "Stahl Altenburg",
    "Cottbus-Ost": "SG Cottbus-Ost", "Sportfreunde Burg": "Sportfreunde Burg", "Sömmerda": "SG Sömmerda",
    "Weimar-Ost": "SG Weimar-Ost",
}

FORMAS = r"(?:1\.\s*FC|BSG|ZSG|SG|SC|FC|ASG|BSV|SV|VfB|ZASK)"


def chave(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s)


def _sem_forma(nome: str) -> str:
    """"BSG Chemie Leipzig" -> "Chemie Leipzig"; "1. FC Magdeburg" -> "Magdeburg"; "SG Lichtenberg 1947" fica."""
    n = re.sub(r"\s+", " ", nome.replace("\xa0", " ")).strip()
    n = re.sub(r"\s+BSG$", "", n)   # "BSG Chemie Leipzig BSG" (erro da página)
    return re.sub(rf"^{FORMAS}\s+", "", n).strip()


_INDICE = {chave(k): v for k, v in NOMES.items()}


def esd(nome: str, ano: int | None = None) -> str | None:
    if not nome:
        return None
    for n in (nome, _sem_forma(nome), _sem_forma(_sem_forma(nome))):
        if chave(n) in _INDICE:
            return _INDICE[chave(n)]
    return None


def exibicao(k: str) -> str:
    if k in CLUBES:
        return CLUBES[k][0]
    return clubes_ger.CLUBES[k][0]


def cidade_pais(k: str) -> tuple[str | None, str]:
    v = CLUBES.get(k) or clubes_ger.CLUBES[k]
    return v[-2], v[-1]
