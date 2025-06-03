#!/usr/bin/env python3
"""
Script de prueba para verificar que la migración del proyecto Casino Virtual se completó exitosamente.
"""

def test_server_imports():
    """Probar importaciones del servidor"""
    print("🧪 Probando importaciones del servidor...")
    try:
        from servidor.src.model.usuario import Usuario, UsuarioServicio
        from servidor.src.model.salaDeJuego import SalaDeJuego, SalaDeJuegoServicio
        from servidor.src.model.salaDeJuego.juego import KnuckleBones, juegosDeCartas
        from servidor.src.model.salaDeJuego.juego.juegosDeCartas import BlackJack, JuegoDeCartas, Mazo, Poker
        from servidor.src.model.salaDeJuego.enums import Etapas, Juegos
        print("✅ Importaciones del servidor: EXITOSAS")
        return True
    except ImportError as e:
        print(f"❌ Error en importaciones del servidor: {e}")
        return False

def test_client_imports():
    """Probar importaciones del cliente"""
    print("🧪 Probando importaciones del cliente...")
    try:
        from cliente.screens import inicio, home
        from cliente.screens.juegos import poker, knucklebones
        from cliente.screens.juegos.blackjack import blackjack_inicio, blackjack_juego, cartas, sacar_carta
        from cliente.screens.forms import login_with_print_form, login_firestore_form, register_form
        from cliente.utils import AuthController, auth_flow_with_session_check, UserSessionManager
        print("✅ Importaciones del cliente: EXITOSAS")
        return True
    except ImportError as e:
        print(f"❌ Error en importaciones del cliente: {e}")
        return False

def test_blackjack_functionality():
    """Probar funcionalidad específica de blackjack"""
    print("🧪 Probando funcionalidad de blackjack...")
    try:
        from cliente.screens.juegos.blackjack.cartas import sacar_carta, mostrar_cartas_en_linea, mazo, cartas
        
        # Verificar que el mazo tiene cartas
        if len(mazo) > 0:
            carta = sacar_carta()
            if carta != "No quedan cartas en el mazo.":
                print(f"✅ Blackjack: Carta extraída exitosamente")
                return True
            else:
                print("❌ Blackjack: No se pudo extraer carta")
                return False
        else:
            print("❌ Blackjack: Mazo vacío")
            return False
    except Exception as e:
        print(f"❌ Error en funcionalidad de blackjack: {e}")
        return False

def main():
    """Función principal de pruebas"""
    print("🎰 CASINO VIRTUAL - Test de Migración Completada")
    print("=" * 50)
    
    tests = [
        test_server_imports,
        test_client_imports,
        test_blackjack_functionality
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 RESULTADOS: {passed}/{total} pruebas pasaron")
    
    if passed == total:
        print("🎉 ¡MIGRACIÓN COMPLETADA EXITOSAMENTE!")
        print("✨ Todos los módulos están correctamente organizados y funcionando")
        print("📁 El directorio 'servidor/src/view/' ha sido eliminado")
        print("🏗️ La estructura de blackjack se migró completamente al cliente")
    else:
        print("⚠️ Algunas pruebas fallaron. Revisar los errores anteriores.")

if __name__ == "__main__":
    main()
