from servidor.src.model.salaDeJuego.juego.juegosDeCartas.BlackJack import BlackJack
from cliente.utils.user_session import UserSessionManager
from servidor.src.model.usuario import Usuario
def main():
    print("Iniciando el programa...")
    data_user = UserSessionManager().load_user_session()
    user_local = Usuario.from_dict(data_user)
    bot1 = Usuario.crear_usuario_local('bot1', 'ktob')
    bot2= Usuario.crear_usuario_local('bot2', 'ktob')
    bot3 = Usuario.crear_usuario_local('bot3', 'ktob')
    
    
    juego = BlackJack("222222", 10, 5, 10, False, 1)
    juego.set_jugadores([bot1, bot2, bot3, user_local])
    juego.inicializar_juego()




if __name__ == "__main__":
    # Usar Screen.wrapper() para manejar la inicialización y limpieza
    # Screen.wrapper(dev)
    main()