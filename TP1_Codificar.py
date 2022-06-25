import multijugador
import solitario

def main():
    # Función para iniciar la aplicación
    # Creador: Guzmán Leonel
    cantidad_jugadores = pedir_cantidad_jugadores()
    
    while cantidad_jugadores.isalpha() or not int(cantidad_jugadores) in (1, 2):
        print("Opción no valida")
        cantidad_jugadores = pedir_cantidad_jugadores()

    veces_jugadas = 0

    jugador_1 = {
            "color": "Azul",
            "nombre": "",
            "gano": False, # gano_partida
            "puntos": 0,
            "empezo_ultima_partida": False
        }


        

    if int(cantidad_jugadores) == 2:
        jugador_2 = {
            "color": "Rojo",
            "nombre": "",
            "gano": False,
            "puntos": 0,
            "empezo_ultima_partida": False
        }

        jugador_1["nombre"] = input("Ingrese el nombre del jugador 1: ")
        jugador_2["nombre"] = input("Ingrese el nombre del jugador 2: ")

        jugadores = (jugador_1, jugador_2)

        multijugador.comenzar_juego(jugadores, veces_jugadas)
    else:
        solitario.comenzar_juego(jugador_1, veces_jugadas)

def pedir_cantidad_jugadores():
    # Creador: Guzman Leonel
    print("Seleccione la cantidad de jugadores")
    print("Presiona 1 para jugar solo")
    print("Persiona 2 para jugar con un amigo")
    return input()

main()