import logica
import solitario

def main():
    cantidad_jugadores = pedir_cantidad_jugadores()
    
    while cantidad_jugadores.isalpha() or int(cantidad_jugadores) > 2:
        print("Opción no valida")
        cantidad_jugadores = pedir_cantidad_jugadores()

    if int(cantidad_jugadores) == 2:
        jugador_1 = {
            "color": "Azul",
            "nombre": "",
        }

        jugador_2 = {
            "color": "Rojo",
            "nombre": "",
        }

        jugador_1["nombre"] = input("Ingrese el nombre del jugador 1: ")
        jugador_2["nombre"] = input("Ingrese el nombre del jugador 2: ")
    else:
        solitario.comenzar_juego()

def pedir_cantidad_jugadores():
    print("Seleccione la cantidad de jugadores")
    print("Presiona 1 para jugar solo")
    print("Persiona 2 para jugar con un amigo")
    return input()

main()