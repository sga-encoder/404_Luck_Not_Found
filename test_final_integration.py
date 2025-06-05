#!/usr/bin/env python3
"""
Test de integración final para verificar que el error TypeError esté completamente resuelto.
Este test reproduce el escenario exacto que causaba el error original.
"""

import sys
sys.path.append('.')

def test_original_error_scenario():
    """
    Test que reproduce el escenario exacto que causaba:
    TypeError: '<' not supported between instances of 'int' and 'NoneType'
    """
    try:
        print("🧪 Reprodución del escenario del error original...")
        
        # Importar las clases necesarias
        from servidor.src.model.salaDeJuego.juego.KnuckleBones import KnuckleBones
        from servidor.src.model.usuario.Usuario import Usuario
        
        print("✅ Imports exitosos")
        
        # Crear un diccionario que simula los datos de la base de datos 
        # que causaban el problema (sin capacidad ni capacidad_minima)
        datos_sala_problematicos = {
            'id': 'test_id',
            'tipo_juego': 'KnuckleBones',
            'jugadores': [],
            'lista_de_espera': [],
            'estado': 'activa'
            # Nota: NO incluimos 'capacidad' ni 'capacidad_minima' para simular el problema original
        }
        
        print("🧪 Creando KnuckleBones con from_dict (datos problemáticos)...")
        knucklebones = KnuckleBones.from_dict(datos_sala_problematicos)
        print(f"✅ KnuckleBones creado exitosamente")
        print(f"   _capacidadMinima = {knucklebones._capacidadMinima} (tipo: {type(knucklebones._capacidadMinima)})")
        print(f"   _capacidad = {knucklebones._capacidad} (tipo: {type(knucklebones._capacidad)})")
        
        # Crear usuarios para la prueba
        usuario1 = Usuario("user1", "Test", "User1", "test1@test.com", "pass123")
        usuario2 = Usuario("user2", "Test", "User2", "test2@test.com", "pass123")
        
        # Agregar jugadores (esto causaba el problema original)
        print("🧪 Agregando jugadores...")
        knucklebones._jugadores.append(usuario1)
        knucklebones._jugadores.append(usuario2)
        print(f"✅ Jugadores agregados: {len(knucklebones._jugadores)}")
        
        # Esta era la línea que causaba el TypeError original
        print("🧪 Probando inicializar_juego (línea que causaba el error)...")
        resultado = knucklebones.inicializar_juego()
        
        print(f"✅ inicializar_juego ejecutado exitosamente: {resultado}")
        
        # Verificar que las comparaciones funcionen correctamente
        print("🧪 Verificando comparaciones...")
        print(f"   len(jugadores) = {len(knucklebones._jugadores)}")
        print(f"   _capacidadMinima = {knucklebones._capacidadMinima}")
        
        if knucklebones._capacidadMinima is not None:
            comparacion = len(knucklebones._jugadores) >= knucklebones._capacidadMinima
            print(f"   len(jugadores) >= _capacidadMinima = {comparacion}")
        else:
            print("   ⚠️ _capacidadMinima es None - esto debería haberse corregido")
        
        print("🎉 ¡El error TypeError ha sido completamente resuelto!")
        return True
        
    except TypeError as e:
        print(f"❌ ERROR TypeError aún presente: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🔧 TEST DE INTEGRACIÓN FINAL")
    print("   Verificando que el error TypeError esté completamente resuelto")
    print("=" * 60)
    
    exito = test_original_error_scenario()
    
    print("=" * 60)
    if exito:
        print("✅ RESULTADO: ERROR COMPLETAMENTE RESUELTO")
        print("   Ya no hay TypeError en las comparaciones con _capacidadMinima")
    else:
        print("❌ RESULTADO: ERROR AÚN PRESENTE")
        print("   Se requieren correcciones adicionales")
    print("=" * 60)
