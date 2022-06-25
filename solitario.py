import logica

def comenzar_juego(jugador, veces_jugadas):
    # Función que maneja la logica para el modo de un jugador
    # Creador: Guzmán Leonel
    palabra_adivinar, adivinado, arriesgos, tiempo_inicial = logica.conseguir_datos_iniciales()
    print(palabra_adivinar)

    partida_terminada = False
    ultimo_arriesgo = ""

    while not partida_terminada:
        logica.mostrar_partida(palabra_adivinar, adivinado, arriesgos)
        if logica.validar_juego_termino(arriesgos, palabra_adivinar, ultimo_arriesgo):
            partida_terminada = True
            jugador["gano"] = (ultimo_arriesgo == palabra_adivinar)
        else:
            arriesgo = logica.pedir_arriesgo(jugador)
            resultado = logica.procesar_arriesgo(palabra_adivinar, arriesgo, adivinado)
            arriesgos.append(resultado)
            ultimo_arriesgo = arriesgo
    
    terminar_partida(jugador, tiempo_inicial)
    calcular_puntos(arriesgos, veces_jugadas, jugador)

    if logica.preguntar_otra_partida():
        palabra_adivinar, adivinado, arriesgos, tiempo_inicial = logica.conseguir_datos_iniciales()
        comenzar_juego(jugador, veces_jugadas + 1)

def calcular_puntos(arriesgos, veces_jugadas, jugador):
    # Creador: Gimenez Ignacio
    print("")
    puntos_ganados = logica.calcular_puntos_ganados(arriesgos, jugador["gano"])

    puntos = jugador["puntos"]
    gano = jugador["gano"]
    puntos_totales = puntos + puntos_ganados

    jugador["puntos"] = puntos_totales
    ganador = "Ganaste" if gano else "Perdiste"

    resultado = "{} un total de {} puntos".format(ganador, puntos_ganados)

    if veces_jugadas > 0:
        resultado += ", tenes acumulados {} puntos.".format(puntos_totales)

    print(resultado)

def terminar_partida(jugador, tiempo_inicial):
    # Creador: Bogarin Juan
    resultado = "Ganaste! " if jugador["gano"] else "Perdiste!"

    minutos, segundos = logica.calcular_tiempo_total(tiempo_inicial)
    resultado += "Tardaste {} minutos y {} segundos en adivinar la palabra".format(minutos, segundos)
    
    print(resultado)