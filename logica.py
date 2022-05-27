import random
import utils
import time
import math

def procesar_intento(palabra_adivinar, arriesgo):
    # Analiza el arriesgo para devolver el color en el que va a ir cada letra
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
    return utils.obtener_color(color) + texto + utils.obtener_color("Defecto")

def mostrar_letras_adivinadas(palabra, adivinado):
    # Muesta las letras advinadas
    LARGO_PALABRA = 5
    print("PALABRA A ADIVINAR: ", end="")
    for i in range(LARGO_PALABRA):
        if i in adivinado:
            print(cambiar_color(palabra[i], "Verde"), end="")
        else:
            print("?", end="")
    
    print(" ")

def mostrar_arriesgos(arriesgos):
    CANTIDAD_MAXIMA_ARRIESGOS = 5

    for i in range(CANTIDAD_MAXIMA_ARRIESGOS):
        print(arriesgos[i] if i < len(arriesgos)  else "?????")

def terminar_partida(arriesgos, gano, tiempo_inicial, veces_jugadas, puntos_acumulados):
    resultado = "Ganaste! " if gano else "Perdiste!"
    if gano:
        tiempo_final = time.time()
        tiempo_total = tiempo_final - tiempo_inicial
        minutos = math.floor(tiempo_total / 60)
        segundos = round(tiempo_total % 60)
        resultado += "Tardaste {} minutos y {} segundos en adivinar la palabra".format(minutos, segundos)
    
    print(resultado)
    nuevos_puntos = calcular_puntos(arriesgos, gano, veces_jugadas, puntos_acumulados)
    comenzar_otra_partida(veces_jugadas, nuevos_puntos)
    


def mostrar_partida(palabra, adivinado, arriesgos, tiempo_inicial, veces_jugadas, puntos_acumulados):
    mostrar_letras_adivinadas(palabra, adivinado)
    
    mostrar_arriesgos(arriesgos)
    
    if len(adivinado) == 5:
        terminar_partida(arriesgos, True, tiempo_inicial, veces_jugadas, puntos_acumulados)
    elif len(arriesgos) < 5:
        arriesgo = pedir_arriesgo()
        resultado = procesar_arriesgo(palabra, arriesgo, adivinado)
        arriesgos.append(resultado)
        mostrar_partida(palabra, adivinado, arriesgos, tiempo_inicial, veces_jugadas, puntos_acumulados)
    else:
        terminar_partida(arriesgos, False, tiempo_inicial, veces_jugadas, puntos_acumulados)

def pedir_arriesgo():
    arriesgo_valido = False
    arriesgo = ""
    while not arriesgo_valido:
        arriesgo = normalize(input("Arriesgo: "))
        if validar_arriesgo(arriesgo):
            arriesgo_valido = True
    
    return arriesgo

def calcular_puntos_ganados(arriesgos, gano):
    puntos = {
        1: 50,
        2: 40,
        3: 30,
        4: 20,
        5: 10,
    }

    return -100 if not gano else puntos[len(arriesgos)]

def calcular_puntos(arriesgos, gano, veces_jugadas, puntos_acumulados):
    print("")
    puntos_ganados = calcular_puntos_ganados(arriesgos, gano)
    puntos_totales = puntos_acumulados + puntos_ganados

    resultado = ("Perdiste " if not gano else "Obtuviste ") + "un total de {} puntos".format(puntos_ganados)

    if veces_jugadas > 0:
        resultado += ", tenes acumulados {} puntos.".format(puntos_totales)  

    print(resultado)
    return puntos_totales

def comenzar_otra_partida(veces_jugadas, puntos_acumulados):
    respuesta = input("Desea jugar otra partida? (S/N): ")
    if respuesta.upper() == "S":
        print("EMpeza de nuevo")
        #main(veces_jugadas + 1, puntos_acumulados)  
    elif respuesta.upper() != "N":
        print("Respuesta invalida")
        comenzar_otra_partida(veces_jugadas, puntos_acumulados)  

def procesar_arriesgo(palabra, arriesgo, adivinado):
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

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a, b)

    return s.upper()

def conseguir_palabra_adivinar():
    arr = utils.obtener_palabras_validas()
    return arr[round(random.random() * len(arr))].upper()

def conseguir_datos_iniciales():
    palabra_adivinar = conseguir_palabra_adivinar()
    adivinado = []
    arriesgos = []
    tiempo_inicial = time.time()
    veces_jugadas = 0
    puntos_acumulados = 0
    return palabra_adivinar, adivinado, arriesgos, tiempo_inicial, veces_jugadas, puntos_acumulados
