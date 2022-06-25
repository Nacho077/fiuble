import random
import utils
import time

def jugador_empieza(jugadores):
    # Función para elegir que jugador empieza la partida
    # Creador: Bogarin Juan
    empieza = -1
    
    for i in range(len(jugadores)):
        if jugadores[i]["empezo_ultima_partida"]:
            empieza = i

    return empieza if empieza >= 0 else round(random.random())

def obtener_otro_jugador(indice_ultimo_jugador_empezo):
    # Creador: Bogarin Juan
    return 0 if indice_ultimo_jugador_empezo == 1 else 1

def mostrar_letras_adivinadas(palabra, adivinado):
    # Muesta las letras advinadas
    # Creador: Bogarin Juan
    LARGO_PALABRA = 5
    print("PALABRA A ADIVINAR: ", end="")
    for i in range(LARGO_PALABRA):
        if i in adivinado:
            print(cambiar_color(palabra[i], "Verde"), end="")
        else:
            print("?", end="")
    
    print(" ")


def mostrar_arriesgos(arriesgos):
    # Creador: Bogarin Juan
    CANTIDAD_MAXIMA_ARRIESGOS = 5

    for i in range(CANTIDAD_MAXIMA_ARRIESGOS):
        print(arriesgos[i] if i < len(arriesgos)  else "?????")

def mostrar_partida(palabra, adivinado, arriesgos):
    # Creador: Bogarin Juan
    mostrar_letras_adivinadas(palabra, adivinado)
    mostrar_arriesgos(arriesgos)

def preguntar_otra_partida():
    # Creador: Bogarin Juan
    respuesta = input("Desea jugar otra partida? (S/N): ")

    while not respuesta.upper() in ("S", "N"):
        print("respuesta invalida")
        respuesta = input("Desea jugar otra partida? (S/N): ")

    return True if respuesta.upper() == "S" else False

def conseguir_palabra_adivinar():
    # Creador: Bogarin Juan
    arr = utils.obtener_palabras_validas()
    return arr[round(random.random() * len(arr))].upper()

def conseguir_datos_iniciales():
    # Creador: Bogarin Juan
    palabra_adivinar = conseguir_palabra_adivinar()
    adivinado = []
    arriesgos = []
    tiempo_inicial = time.time()
    return palabra_adivinar, adivinado, arriesgos, tiempo_inicial