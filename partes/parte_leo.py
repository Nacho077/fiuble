import time
import math
import logica
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
            "gano": False,
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

def calcular_puntos(arriesgos, veces_jugadas, jugadores, ultimo_turno):
    # Creador: Guzmán Leonel
    print("")
    puntos_ganados = logica.calcular_puntos_ganados(arriesgos, jugadores[ultimo_turno]["gano"])

    for jugador in jugadores:
        puntos = jugador["puntos"]
        gano = jugador["gano"]
        puntos_totales = 0
        if puntos_ganados == -100:
            puntos_totales = (puntos + puntos_ganados) if jugador["empezo_ultima_partida"] else (puntos + (puntos_ganados / 2))
        else:
            puntos_totales = (puntos + puntos_ganados) if gano else (puntos - puntos_ganados)

        jugador["puntos"] = puntos_totales
        nombre = logica.cambiar_color(jugador["nombre"], jugador["color"])
        ganador = "ganó" if gano else "perdió"

        if puntos_ganados == -100:
            puntos_mostrar = abs(puntos_ganados) if jugador["empezo_ultima_partida"] else abs(round(puntos_ganados / 2))
            resultado = "{} {} un total de {} puntos".format(nombre, ganador, puntos_mostrar)
        else:
            resultado = "{} {} un total de {} puntos".format(nombre, ganador, puntos_ganados)

        if veces_jugadas > 0:
            resultado += ", tiene acumulados {} puntos.".format(round(puntos_totales))

        print(resultado)

def validar_juego_termino(arriesgos, palabra, ultimo_arriesgo):
    # Creador: Guzmán Leonel
    return (ultimo_arriesgo == palabra) or (len(arriesgos) == 5)

def calcular_tiempo_total(tiempo_inicial):
    # Creador: Guzmán Leonel
    tiempo_final = time.time()
    tiempo_total = tiempo_final - tiempo_inicial
    minutos = math.floor(tiempo_total / 60)
    segundos = round(tiempo_total % 60)

    return minutos, segundos
    
def pedir_arriesgo(jugador):
    # Creador: Guzmán Leonel
    arriesgo_valido = False
    arriesgo = ""
    if jugador["nombre"] != "":
        print("Es el turno de " + cambiar_color(jugador["nombre"], jugador["color"]))
    while not arriesgo_valido:
        arriesgo = normalize(input("Arriesgo: "))
        if validar_arriesgo(arriesgo):
            arriesgo_valido = True
    
    return arriesgo