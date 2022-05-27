import logica

def comenzar_juego():
    palabra_adivinar, adivinado, arriesgos, tiempo_inicial, veces_jugadas, puntos_acumulados = logica.conseguir_datos_iniciales()
    print(palabra_adivinar)
    logica.mostrar_partida(palabra_adivinar, adivinado, arriesgos, tiempo_inicial, veces_jugadas, puntos_acumulados)