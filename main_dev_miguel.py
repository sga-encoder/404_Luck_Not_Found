from servidor.src.model.salaDeJuego.juego.juegosDeCartas.BlackJack import BlackJack

def main():
    print("Iniciando el programa...")
    self = BlackJack("222222", 10, 5, 10, False, 1)
    BlackJack.inicializar_juego(self)




if __name__ == "__main__":
    # Usar Screen.wrapper() para manejar la inicialización y limpieza
    # Screen.wrapper(dev)
    main()