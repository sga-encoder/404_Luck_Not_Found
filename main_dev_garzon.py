#!/usr/bin/env python
from asciimatics.screen import Screen

"""
Archivo de desarrollo para el Casino Virtual 404 Luck Not Found
Contiene herramientas de debug y opciones de desarrollo
"""
from cliente.screens.forms.login_form import login_form
from cliente.screens.juegos.knucklebones.knucklebones_juego import knucklebones_juego
def dev(screen):
    """Función que recibe una instancia de screen"""
    knucklebones_juego(screen)

if __name__ == "__main__":
    # Usar Screen.wrapper() para manejar la inicialización y limpieza
    Screen.wrapper(dev)