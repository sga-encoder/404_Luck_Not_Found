#!/usr/bin/env python3
"""Test simple import"""

try:
    print("Intentando importar Screen...")
    from asciimatics.screen import Screen
    print("✓ Screen importado")
    
    print("Intentando importar UserSessionManager...")
    from cliente.utils.user_session import UserSessionManager
    print("✓ UserSessionManager importado")
    
    print("Intentando importar KnuckleBones...")
    from servidor.src.model.salaDeJuego.juego import KnuckleBones
    print("✓ KnuckleBones importado")
    
    print("Intentando importar Usuario...")
    from servidor.src.model.usuario import Usuario
    print("✓ Usuario importado")
    
    print("Intentando importar utilities...")
    from cliente.utils.events import add_key_listener
    from cliente.utils.printers import print_button, print_text
    print("✓ Utilities importadas")
    
    print("Definiendo función async...")
    async def test_function(screen):
        print("Test function works")
        return True
    print("✓ Función async definida")
    
    print("Importando knucklebones_inicio...")
    from cliente.screens.juegos.knucklebones.knucklebones_inicio import knucklebones_inicio
    print("✓ knucklebones_inicio importado exitosamente!")
    
except ImportError as e:
    print(f"❌ Error de importación: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
