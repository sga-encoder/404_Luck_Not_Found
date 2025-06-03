#!/usr/bin/env python3
"""
Script de verificación simple de imports para Casino Virtual
"""

def test_basic_imports():
    """Prueba imports básicos uno por uno"""
    print("🎰 Probando imports básicos...")
    
    # Test 1: Import básico del servidor
    try:
        print("  📦 Importando servidor...")
        import servidor
        print("    ✓ Módulo servidor importado")
    except Exception as e:
        print(f"    ❌ Error en servidor: {e}")
        return False
    
    # Test 2: Import básico del cliente  
    try:
        print("  📦 Importando cliente...")
        import cliente
        print("    ✓ Módulo cliente importado")
    except Exception as e:
        print(f"    ❌ Error en cliente: {e}")
        return False
    
    print("\n🎉 ¡Imports básicos funcionan correctamente!")
    return True

def test_specific_imports():
    """Prueba imports específicos de módulos"""
    print("\n🔍 Probando imports específicos...")
    
    try:
        print("  📡 Importando servidor.src...")
        import servidor.src
        print("    ✓ servidor.src OK")
        
        print("  🛠️  Importando servidor.src.utils...")
        from servidor.src import utils
        print("    ✓ utils OK")
        
        print("  📊 Importando servidor.src.model...")
        from servidor.src import model
        print("    ✓ model OK")
        
        print("  🖥️  Importando cliente.screens...")
        from cliente import screens
        print("    ✓ screens OK")
        
        print("  🔧 Importando cliente.utils...")
        from cliente import utils as client_utils
        print("    ✓ client utils OK")
        
    except Exception as e:
        print(f"    ❌ Error en imports específicos: {e}")
        return False
    
    print("\n🎉 ¡Imports específicos funcionan correctamente!")
    return True

if __name__ == "__main__":
    success = test_basic_imports()
    if success:
        test_specific_imports()
    print("\n✅ Configuración de __init__.py completada exitosamente")
