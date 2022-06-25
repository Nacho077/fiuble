import logica

def comenzar_juego(jugadores, veces_jugadas):
    # Función que maneja la logica para el modo multijugador
    # Creador: Gimenez Ignacio
    palabra_adivinar, adivinado, arriesgos, tiempo_inicial = logica.conseguir_datos_iniciales()
    print(palabra_adivinar)

    partida_terminada = False
    ultimo_arriesgo = ""
    turno_jugador = jugador_empieza(jugadores)
    jugadores[obtener_otro_jugador(turno_jugador)]["empezo_ultima_partida"] = True
    jugadores[turno_jugador]["empezo_ultima_partida"] = False

    while not partida_terminada:
        logica.mostrar_partida(palabra_adivinar, adivinado, arriesgos)
        if logica.validar_juego_termino(arriesgos, palabra_adivinar, ultimo_arriesgo):
            partida_terminada = True
            jugadores[turno_jugador]["gano"] = True if ultimo_arriesgo == palabra_adivinar else False
            jugadores[obtener_otro_jugador(turno_jugador)]["gano"] = False
        else:
            turno_jugador = obtener_otro_jugador(turno_jugador)
            arriesgo = logica.pedir_arriesgo(jugadores[turno_jugador])
            resultado = logica.procesar_arriesgo(palabra_adivinar, arriesgo, adivinado)
            arriesgos.append(resultado)
            ultimo_arriesgo = arriesgo

    terminar_partida(jugadores, tiempo_inicial, ultimo_arriesgo, palabra_adivinar)
    calcular_puntos(arriesgos, veces_jugadas, jugadores, turno_jugador)
    
    if logica.preguntar_otra_partida():
        palabra_adivinar, adivinado, arriesgos, tiempo_inicial = logica.conseguir_datos_iniciales()
        comenzar_juego(jugadores, veces_jugadas + 1)

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

def normalize(s):
    # Creador: Gimenez Ignacio
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b)

    return s.upper()