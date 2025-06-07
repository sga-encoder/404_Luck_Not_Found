#!/usr/bin/env python
from pprint import PrettyPrinter
from asciimatics.screen import Screen

from servidor.src.model.salaDeJuego.juego import KnuckleBones
from servidor.src.model.usuario import Usuario
from servidor.src.utils.firestore import add_realtime_listener

"""
Archivo de desarrollo para el Casino Virtual 404 Luck Not Found
Contiene herramientas de debug y opciones de desarrollo
"""
from cliente.screens.forms.login_form import login_form
from cliente.screens.juegos.knucklebones.knucklebones_juego import knucklebones_juego
from cliente.utils.user_session import UserSessionManager
def ordenar_jugadores(diccionario_jugadores):
    print("Ordenando jugadores por nombre...")
    
async def dev_debug():
    """Función que recibe una instancia de screen"""
    # knucklebones_juego(screen)
    juego = KnuckleBones()
    data_user = await UserSessionManager().load_user_session()
    user_local = Usuario.from_dict(data_user)
    bot = Usuario.crear_usuario_local('botk', 'ktob')
    await juego.entrar_sala_de_juego(user_local, juego.to_dict())
    await juego.entrar_sala_de_juego(bot, juego.to_dict())
    opcion = input('dame un numero')
    if opcion == '1':
        juego_json = juego.to_dict()
        print("Datos del juego:", juego_json)
    elif opcion == '2':
        ordenar_jugadores()

async def dev_debug_with_listener():
    """Función de desarrollo que incluye escucha en tiempo real"""
    print("=== Desarrollo KnuckleBones con Listener ===")
    
    # Crear el juego y configurar usuarios
    juego = KnuckleBones()
    data_user = await UserSessionManager().load_user_session()
    user_local = Usuario.from_dict(data_user)
    bot = Usuario.crear_usuario_local('botk', 'ktob')
    
    # Crear la sala y obtener el ID
    sala_data = juego.to_dict()
    print(f"Datos de la sala: {sala_data}")
    
    # Entrar a la sala de juego
    await juego.entrar_sala_de_juego(user_local, sala_data)
    await juego.entrar_sala_de_juego(bot, sala_data)
    
    # Obtener el ID de la sala creada (esto debería venir del servicio)
    from servidor.src.model.salaDeJuego.SalaDeJuegoServicio import SalaDeJuegoServicio
    servicio = SalaDeJuegoServicio()
    salas = await servicio.obtener_collection_salas_de_juego()
    
    if salas:
        sala_id = salas[-1].get('id')  # Tomar la última sala creada
        print(f"ID de la sala: {sala_id}")
        
        # Iniciar la escucha asíncrona
        def on_update(doc_snapshot, changes, read_time):
            if doc_snapshot.exists:
                estado = doc_snapshot.to_dict()
                print(f"¡Cambio detectado en la sala!")
                print(f"Jugadores: {estado.get('jugadores', [])}")
                print(f"Estado: {estado.get('estado', 'desconocido')}")
        
        listener_unsubscribe = servicio.iniciar_listener_sala_especifica(
            sala_id,
            on_update,
            lambda error: print(f"Error: {error}")
        )
        
        print("Listener iniciado. Escuchando cambios...")
        print("Presiona Enter para continuar o 'q' para salir")
        
        try:
            while True:
                opcion = input("Opción (1=ver datos, 2=simular cambio, q=salir): ").strip()
                
                if opcion.lower() == 'q':
                    break
                elif opcion == '1':
                    sala_actual = await servicio.obtener_sala_activa(sala_id)
                    print(f"Estado actual: {sala_actual}")
                elif opcion == '2':
                    # Simular un cambio en la sala
                    import time
                    nuevo_jugador = Usuario.crear_usuario_local(f'test_{int(time.time())}', 'password')
                    await servicio.entrar_sala_de_juego(sala_id, nuevo_jugador)
                    print("Jugador simulado agregado")
                    
        except KeyboardInterrupt:
            print("\nInterrumpido por el usuario")
        finally:
            if listener_unsubscribe:
                listener_unsubscribe()
                print("Listener detenido")
    else:
        print("No se encontraron salas activas")

async def async_main():	
    """
    Función principal asíncrona para ejecutar el desarrollo
    """
    def mi_callback(doc_data, changes, read_time):
        """Callback que se ejecuta cuando hay cambios"""
        if doc_data:
            
            print("📡 Documento actualizado:")
            PrettyPrinter.print_dynamic_data(doc_data, indent="      ")

        else:
            print("📡 Documento eliminado o no existe")
    
    def mi_error_callback(error):
        """Callback para manejar errores"""
        print(f"❌ Error en listener: {error}")
    
    # ✅ USO CORRECTO
    unsubscribe = add_realtime_listener(
        'salas_de_juego_activas', 
        'AVioyi1rrG4IKRcpCQ2i',
        mi_callback,
        mi_error_callback
    )
    
    print("🎧 Listener iniciado. Presiona Enter para detener...")
    input()
    
    # Detener el listener
    unsubscribe()
    print("🛑 Listener detenido")
def dev(screen):
    knucklebones_juego(screen)


if __name__ == "__main__":
    print("=== Opciones de desarrollo ===")
    print("1. Desarrollo normal")
    print("2. Desarrollo con listener en tiempo real")
    print("3. Juego visual")
    print("4. async_main()")
    
    opcion = input("Selecciona una opción (1-3): ").strip()
    
    if opcion == "1":
        # Desarrollo normal
        import asyncio
        asyncio.run(dev_debug())
    elif opcion == "2":
        # Desarrollo con listener
        import asyncio
        asyncio.run(dev_debug_with_listener())
    elif opcion == "3":
        # Juego visual
        Screen.wrapper(dev)
    elif opcion == "4":
        # async_main()
        import asyncio
        asyncio.run(async_main())
    else:
        print("Opción no válida")