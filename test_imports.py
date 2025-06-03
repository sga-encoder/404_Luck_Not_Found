#!/usr/bin/env python3
"""
Script de verificación de imports para Casino Virtual
Prueba que todas las configuraciones de __init__.py funcionan correctamente
"""

def test_imports():
    """Prueba todas las importaciones principales del proyecto"""
    print("🎰 Verificando imports del Casino Virtual...")
    
    try:
        # Test imports del servidor
        print("  📡 Probando servidor...")
        import servidor
        print("    ✓ Módulo servidor OK")
        
        import servidor.src
        print("    ✓ Módulo servidor.src OK")
        
        from servidor.src import utils, model, view
        print("    ✓ Submódulos del servidor OK")
        
        # Test imports del cliente
        print("  🖥️  Probando cliente...")
        import cliente
        print("    ✓ Módulo cliente OK")
        
        from cliente import screens, utils
        print("    ✓ Submódulos del cliente OK")
        
        # Test imports específicos
        print("  🃏 Probando imports específicos...")
        from servidor.src.model import Usuario, SalaDeJuego
        print("    ✓ Clases de modelo OK")
        
        from cliente.screens import forms, juegos
        print("    ✓ Pantallas del cliente OK")
        
        print("\n🎉 ¡Todos los imports funcionan correctamente!")
        print("✅ Configuración de __init__.py completada exitosamente")
        
    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False
    
    return True

if __name__ == "__main__":
    test_imports()
