#!/usr/bin/env python3
"""
Script para probar el flujo completo de KnuckleBones
"""

import sys
import os
import asyncio

# Agregar el directorio servidor al path para imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'servidor'))

async def test_knucklebones_flow():
    try:
        from servidor.src.model.salaDeJuego.juego.KnuckleBones import KnuckleBones
        from servidor.src.model.usuario import Usuario
        
        print("✅ Imports exitosos")
        
        # Crear un usuario de prueba
        print("\n🧪 Creando usuario de prueba...")
        usuario = Usuario("test123", "Usuario", "Prueba", "test@test.com", "password123")
        print(f"✅ Usuario creado: {usuario.get_nombre()}")
        
        # Crear una instancia de KnuckleBones
        print("\n🧪 Creando instancia de KnuckleBones...")
        juego = KnuckleBones()
        print(f"✅ KnuckleBones creado: _capacidadMinima = {juego._capacidadMinima}")
        
        # Intentar entrar a la sala de juego (simulando el flujo real)
        print("\n🧪 Probando entrar a sala de juego...")
        
        # Simular el diccionario que se pasa
        diccionario_juego = {
            'tipo_juego': 'KnuckleBones',
            'capacidad': 2,
            'capacidad_minima': 2
        }
        
        # Esta es la línea que está causando el error en el flujo real
        try:
            resultado = await juego.entrar_sala_de_juego(usuario, diccionario_juego)
            print(f"✅ Entrada a sala exitosa: {resultado}")
        except Exception as e:
            print(f"❌ Error en entrar_sala_de_juego: {e}")
            import traceback
            traceback.print_exc()
            
        print("\n🎉 Prueba del flujo completa!")
        
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_knucklebones_flow())
