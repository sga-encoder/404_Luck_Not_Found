#!/usr/bin/env python
from asciimatics.screen import Screen

"""
Archivo de desarrollo para el Casino Virtual 404 Luck Not Found
Contiene herramientas de debug y opciones de desarrollo
"""
from cliente.screens.forms.login_form import login_form
from cliente.utils.printers import print_text

def dev(screen):
    """Función que recibe una instancia de screen"""
    result = login_form(screen)
    
    # Mostrar el resultado
    screen.clear()
    screen.print_at(f'Resultado del formulario: {result}', 0, 0, Screen.COLOUR_WHITE)
    screen.refresh()
    screen.wait_for_input(5)  # Espera 5 segundos antes de cerrar
    print("Resultado del formulario:", result)

if __name__ == "__main__":
    # Usar Screen.wrapper() para manejar la inicialización y limpieza
    Screen.wrapper(dev)