#!/usr/bin/env python
"""
Archivo de desarrollo para el Casino Virtual 404 Luck Not Found
Contiene herramientas de debug y opciones de desarrollo
"""
import os
import sys
import asyncio
from asciimatics.screen import Screen

# Agregar directorios al path de Python
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)
sys.path.append(os.path.join(ROOT_DIR, 'cliente'))
sys.path.append(os.path.join(ROOT_DIR, 'servidor'))
sys.path.append(os.path.join(ROOT_DIR, 'servidor', 'src'))

# Importaciones directas
from cliente.screens.inicio import main as cliente_main

# Importaciones del servidor para debug
try:
    from servidor.src import (
        Usuario, UsuarioServicio, SalaDeJuego, SalaDeJuegoServicio,
        Poker, BlackJack, KnuckleBones, Firestore, generador_random
    )
    
    CLASES_SERVIDOR = {
        'Usuario': Usuario,
        'UsuarioServicio': UsuarioServicio,
        'SalaDeJuego': SalaDeJuego,
        'SalaDeJuegoServicio': SalaDeJuegoServicio,
        'Poker': Poker,
        'BlackJack': BlackJack, 
        'KnuckleBones': KnuckleBones,
        'Firestore': Firestore,
        'generador_random': generador_random
    }
except ImportError as e:
    print(f"Error al importar clases del servidor: {e}")
    import traceback
    traceback.print_exc()
    CLASES_SERVIDOR = {}

def dev():
    """
    Función de desarrollo con opciones de debug
    Permite elegir entre cliente y servidor para testing
    """
    try:
        print("=== MODO DESARROLLO - Casino Virtual 404 Luck Not Found ===")
        print("1. Modo Cliente")
        print("2. Modo Servidor (solo debug)")
        print("=" * 50)
        opcion = input("Seleccione una opción (1-2): ")
        
        if opcion == "1":
            print("Iniciando cliente en modo desarrollo...")
            # Iniciar el cliente
            Screen.wrapper(cliente_main)
            
        elif opcion == "2":
            print("Iniciando servidor en modo depuración...")
            # Mostrar información de depuración del servidor
            print("Clases disponibles:")
            if CLASES_SERVIDOR:
                for nombre, clase in CLASES_SERVIDOR.items():
                    print(f"- {nombre}: {clase}")
                print(f"\nTotal de clases cargadas: {len(CLASES_SERVIDOR)}")
            else:
                print("No se pudieron cargar las clases del servidor.")
                
        else:
            print("Opción no válida. Por favor seleccione 1 o 2.")
            
    except KeyboardInterrupt:
        print("\nDesarrollo interrumpido por el usuario.")
    except Exception as e:
        print(f"Error en modo desarrollo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    dev()