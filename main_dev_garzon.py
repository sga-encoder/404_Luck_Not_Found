#!/usr/bin/env python
from asciimatics.screen import Screen

from servidor.src.model.salaDeJuego.juego import KnuckleBones
from servidor.src.model.usuario import Usuario

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
    juego.set_jugadores([user_local, bot])
    opcion = input('dame un numero')
    if opcion == '1':
        juego_json = juego.to_dict()
        print("Datos del juego:", juego_json)
    elif opcion == '2':
        ordenar_jugadores()

def dev(screen):
    knucklebones_juego(screen)


if __name__ == "__main__":
    # Usar Screen.wrapper() para manejar la inicialización y limpieza
    # Screen.wrapper(dev)
    import asyncio
    asyncio.run(dev_debug())