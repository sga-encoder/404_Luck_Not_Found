#!/usr/bin/env python
"""
Archivo principal del Casino Virtual 404 Luck Not Found
Gestor de pantallas y punto de entrada principal
"""
import os
import sys
from asciimatics.screen import Screen

# Agregar directorios al path de Python
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)
sys.path.append(os.path.join(ROOT_DIR, 'cliente'))

# Importaciones directas
from cliente.screens.inicio import inicio
from cliente.screens.home import home
from cliente.screens.juegos.poker import poker
from cliente.screens.juegos.blackjack.blackjack_inicio import blackjack_inicio
from cliente.screens.juegos.blackjack.blackjack_juego import blackjack_juego
from cliente.screens.juegos.knucklebones.knucklebones import knucklebones

def dev(screen):
    """
    Gestor principal de pantallas del Casino Virtual
    Controla el flujo entre login, home y juegos
    """

    blackjack_juego(screen)

if __name__ == "__main__":
    print("Iniciando Casino Virtual 404 Luck Not Found...")
    Screen.wrapper(dev)