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

def manejador_de_pantalla(screen):
    """
    Gestor principal de pantallas del Casino Virtual
    Controla el flujo entre login, home y juegos
    """
    try:
        # Iniciar con pantalla de login/inicio
        resultado = inicio(screen)
        
        if resultado:
            # Si el login fue exitoso, mostrar home y gestionar navegación
            card = home(screen)
            
            # Navegar según la selección del usuario
            if card == 'poker':
                poker(screen)
            elif card == 'blackjack':
                resultado= blackjack_inicio(screen)
                if resultado == 'iniciar blackjack':
                    blackjack_juego(screen)
                
            elif card == 'knucklebones':
                knucklebones(screen)
                
    except Exception as e:
        print(f"Error en el gestor de pantallas: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("Iniciando Casino Virtual 404 Luck Not Found...")
    Screen.wrapper(manejador_de_pantalla)
