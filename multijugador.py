import logica
import random

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

def terminar_partida(jugadores, tiempo_inicial, ultimo_arriesgo, palabra_adivinar):
    # Creador: Bogarin Juan
    if ultimo_arriesgo == palabra_adivinar:
        ganador = jugadores[0] if jugadores[0]["gano"] else jugadores[1]
        print("El ganador es {}".format(logica.cambiar_color(ganador["nombre"], ganador["color"])))

        minutos, segundos = logica.calcular_tiempo_total(tiempo_inicial)
        print("Tardaste {} minutos y {} segundos en adivinar la palabra".format(minutos, segundos))
    else:
        print("Perdieron!")