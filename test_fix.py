#!/usr/bin/env python3
"""
Script para probar que la corrección del método from_dict funciona correctamente
"""

import sys
import os

# Agregar el directorio servidor al path para imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'servidor'))

try:
    from servidor.src.model.salaDeJuego.juego.KnuckleBones import KnuckleBones
    from servidor.src.model.usuario import Usuario
    
    print("✅ Imports exitosos")
    
    # Crear un juego de KnuckleBones usando el constructor normal
    print("\n🧪 Probando constructor normal...")
    juego = KnuckleBones()
    print(f"✅ Constructor normal: _capacidadMinima = {juego._capacidadMinima}")
    
    # Crear un diccionario de prueba para from_dict
    print("\n🧪 Probando método from_dict...")
    data_test = {
        'id': 'test_sala_123',
        'capacidad': 2,
        'capacidad_minima': 2,
        'jugadores': [],
        'turnoActivo': None,
        'historial': [],
        'fechaHoraInicio': '2025-06-04T10:00:00',
        'listaDeEspera': [],
        'apuestas': []
    }
    
    # Probar el método from_dict
    juego_from_dict = KnuckleBones.from_dict(data_test)
    print(f"✅ from_dict exitoso: _capacidadMinima = {juego_from_dict._capacidadMinima}")
    print(f"✅ Tipo de _capacidadMinima: {type(juego_from_dict._capacidadMinima)}")
    
    # Probar inicializar_juego sin jugadores (debe fallar graciosamente)
    print("\n🧪 Probando inicializar_juego sin jugadores...")
    try:
        resultado = juego_from_dict.inicializar_juego('KnuckleBones')
        print(f"✅ inicializar_juego sin jugadores: {resultado}")
    except TypeError as e:
        print(f"❌ Error en inicializar_juego: {e}")
      # Agregar jugadores y probar
    print("\n🧪 Probando con jugadores...")
    usuario1 = Usuario("jugador1", "Jugador", "Primero", "jugador1@test.com", "password123")
    usuario2 = Usuario("jugador2", "Jugador", "Segundo", "jugador2@test.com", "password123")
    
    juego_from_dict._jugadores = [usuario1, usuario2]
    
    print(f"✅ Jugadores agregados: {len(juego_from_dict._jugadores)}")
    print(f"✅ _capacidadMinima sigue siendo: {juego_from_dict._capacidadMinima}")
    
    # Ahora probar inicializar_juego (esta vez debería funcionar hasta la verificación)
    print("\n🧪 Probando inicializar_juego con jugadores...")
    try:
        # Solo verificar que no hay TypeError en la comparación
        if len(juego_from_dict._jugadores) < juego_from_dict._capacidadMinima:
            print("❌ No debería llegar aquí con 2 jugadores")
        else:
            print("✅ Comparación len(jugadores) < capacidadMinima funciona correctamente")
    except TypeError as e:
        print(f"❌ Error en la comparación: {e}")
        
    print("\n🎉 ¡Todas las pruebas completadas!")
    print("✅ La corrección del método from_dict parece estar funcionando correctamente")
    
except ImportError as e:
    print(f"❌ Error de import: {e}")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
    import traceback
    traceback.print_exc()
