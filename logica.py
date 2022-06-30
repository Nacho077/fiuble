import random
import utiles
import time
import math

def procesar_intento(palabra_adivinar, arriesgo):
    # Analiza el arriesgo para devolver el color en el que va a ir cada letra
    # Creador: Gimenez Ignacio
    palabra_adivinar_arr = [*palabra_adivinar]
    arriesgo_arr = [*arriesgo]
    letras_sin_adivinar = []
    letras_sin_procesar = []
    resultado = {
        "Verde": [],
        "Amarillo": [],
        "GrisOscuro": [],
    }

    for index in range(len(arriesgo_arr)):
        if palabra_adivinar_arr[index] == arriesgo_arr[index]:
            resultado["Verde"].append(index)
        else:
            letras_sin_adivinar.append(palabra_adivinar_arr[index])
            letras_sin_procesar.append(arriesgo_arr[index])

    if len(letras_sin_procesar) > 0:
        for index in range(len(letras_sin_procesar.copy())):
            if letras_sin_procesar[index] in letras_sin_adivinar:
                resultado["Amarillo"].append(letras_sin_procesar[index])
                letras_sin_adivinar.remove(letras_sin_procesar[index])
            else:
                resultado["GrisOscuro"].append(letras_sin_procesar[index])

    return resultado

def cambiar_color(texto, color):
    # Creador: Gimenez Ignacio
    return (utiles.obtener_color(color) + texto + utiles.obtener_color("Defecto")) if texto != "" else ""

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
        arriesgo = normalizar_palabra(input("Arriesgo: "))
        if validar_arriesgo(arriesgo):
            arriesgo_valido = True
    
    return arriesgo

def calcular_puntos_ganados(arriesgos, gano):
    # Creador: Gimenez Ignacio
    puntos = {
        1: 50,
        2: 40,
        3: 30,
        4: 20,
        5: 10,
    }

    return -100 if not gano else puntos[len(arriesgos)]


def preguntar_otra_partida():
    # Creador: Bogarin Juan
    respuesta = input("Desea jugar otra partida? (S/N): ")

    while not respuesta.upper() in ("S", "N"):
        print("respuesta invalida")
        respuesta = input("Desea jugar otra partida? (S/N): ")

    return True if respuesta.upper() == "S" else False

def procesar_arriesgo(palabra, arriesgo, adivinado):
    # Creador: Gimenez Ignacio
    resultado = procesar_intento(palabra, arriesgo)
    mostrar = ""

    for i in range(len(arriesgo)):
        letra = arriesgo[i]

        if(i in resultado["Verde"]):
            mostrar += cambiar_color(letra, "Verde")
            if not i in adivinado:
                adivinado.append(i)
        elif(letra in resultado["Amarillo"]):
            resultado["Amarillo"].remove(letra)

            mostrar += cambiar_color(letra, "Amarillo")
        elif(letra in resultado["GrisOscuro"]):
            resultado["GrisOscuro"].remove(letra)

            mostrar += cambiar_color(letra, "GrisOscuro")
    
    return mostrar

def validar_arriesgo(arriesgo):
    #Creador: Guzmán Leonel
    valido = False
    len_correcto = True
    LEN_CORRECTO = 5

    if len(arriesgo) != LEN_CORRECTO:
        print("El arriesgo debe tener 5 caracteres")
        len_correcto = False

    if len_correcto:
        if arriesgo.isalpha():
            valido = True
        else:
            print("El arriesgo debe contener solo letras")
    
    return valido

def normalizar_palabra(palabra):
    palabra = palabra.upper()
    letras_reemplazar = (
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
        ("À", "A"),
        ("È", "E"),
        ("Ì", "I"),
        ("Ò", "O"),
        ("Ù", "U"),
    )

    for letra_acentuada, letra_sin_acento in letras_reemplazar:
        palabra = palabra.replace(letra_acentuada, letra_sin_acento)

    return palabra

def conseguir_palabra_adivinar():
    # Creador: Bogarin Juan
    arr = utiles.obtener_palabras_validas()
    return arr[round(random.random() * len(arr))].upper()

def conseguir_datos_iniciales():
    # Creador: Bogarin Juan
    palabra_adivinar = conseguir_palabra_adivinar()
    adivinado = []
    arriesgos = []
    tiempo_inicial = time.time()
    return palabra_adivinar, adivinado, arriesgos, tiempo_inicial
