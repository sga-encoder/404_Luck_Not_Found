#!/usr/bin/env python
"""
Archivo principal del Casino Virtual 404 Luck Not Found
Gestor de pantallas y punto de entrada principal
"""
import os
import sys
import asyncio
from asciimatics.screen import Screen

from cliente.screens.forms import login_hub, register_form
from cliente.screens.forms.login_form import login_form
from cliente.screens.juegos.knucklebones.knucklebones_juego import knucklebones_juego
from cliente.screens.juegos.knucklebones.knucklebones_inicio import knucklebones_inicio
from cliente.utils.user_session import UserSessionManager
from cliente.utils.async_wrapper import async_screen_wrapper

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

@async_screen_wrapper
async def manejador_de_pantalla(screen):
    """
    Gestor principal de pantallas del Casino Virtual
    Controla el flujo entre login, home y juegos
    """
    try:
        # Iniciar con pantalla de login/inicio
        session_manager = UserSessionManager()
        resultado = False
        while not session_manager.has_active_session():            
            resultado = inicio(screen)
            resultado_login_hub = login_hub(screen)
            if resultado_login_hub == 'registro':
                await register_form(screen)
            elif resultado_login_hub == 'iniciar_sesion':
                await login_form(screen)
                
        if session_manager.has_active_session():
            resultado = inicio(screen)
                
        if resultado and session_manager.has_active_session():
            # Si el login fue exitoso, mostrar home y gestionar navegación
            resultado_home = home(screen)
            
            # Navegar según la selección del usuario
            if resultado_home == 'poker':
                poker(screen)
            elif resultado_home == 'blackjack':
                resultado_blackjack = blackjack_inicio(screen)
                if resultado_blackjack == 'iniciar blackjack':
                    blackjack_juego(screen)
                
            elif resultado_home == 'knucklebones':
                # Para funciones async, las ejecutamos directamente con await
                resultado_knucklebones, id_knucklebones, user_knucklebones, juego_knucklebones = await knucklebones_inicio(screen)
                if resultado_knucklebones and id_knucklebones is not None:
                    knucklebones_juego(screen, id_knucklebones, user_knucklebones, juego_knucklebones)

                    

    except Exception as e:
        print(f"Error en el gestor de pantallas: {e}")
        import traceback
        traceback.print_exc()

def wrapper_asincrono(screen):
    """
    Wrapper para manejar funciones async con asciimatics
    """
    # Crear un nuevo loop de eventos si no existe uno
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    # Ejecutar la función async
    return loop.run_until_complete(manejador_de_pantalla(screen))

if __name__ == "__main__":
    print("Iniciando Casino Virtual 404 Luck Not Found...")
    # Ahora puedes usar directamente el decorador
    Screen.wrapper(manejador_de_pantalla)
