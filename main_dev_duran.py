from servidor.src.model.salaDeJuego.juego.juegosDeCartas.Poker import Poker
from cliente.utils.user_session import UserSessionManager
from servidor.src.model.usuario import Usuario

def main():
    print("Iniciando el programa de desarrollo para Poker...")
    data_user = UserSessionManager().load_user_session()
    user_local = Usuario.from_dict(data_user)
    bot1 = Usuario.crear_usuario_local('bot1', 'poker')
    bot2 = Usuario.crear_usuario_local('bot2', 'poker')
    bot3 = Usuario.crear_usuario_local('bot3', 'poker')

    juego = Poker("mesa_poker_1", 7, 2, 100)
    juego._jugadores = [bot1, bot2, bot3]
    juego.inicializar_juego()
    # Si quieres simular una partida CLI, puedes llamar a juego.jugar_partida() si está implementado
    if hasattr(juego, 'jugar_partida'):
        juego.jugar_partida()
    else:
        print("Poker inicializado, pero no se encontró método jugar_partida().")

if __name__ == "__main__":
    main()

# python main_dev_duran.py