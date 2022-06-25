import logica
import utils

def validar_arriesgo(arriesgo):
    #Creador: Mercurio Nicole
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

    
def terminar_partida(jugadores, tiempo_inicial, ultimo_arriesgo, palabra_adivinar):
    # Creador: Mercurio Nicole
    if ultimo_arriesgo == palabra_adivinar:
        ganador = jugadores[0] if jugadores[0]["gano"] else jugadores[1]
        print("El ganador es {}".format(logica.cambiar_color(ganador["nombre"], ganador["color"])))

        minutos, segundos = logica.calcular_tiempo_total(tiempo_inicial)
        print("Tardaste {} minutos y {} segundos en adivinar la palabra".format(minutos, segundos))
    else:
        print("Perdieron!")

def cambiar_color(texto, color):
    # Creador: Mercurio Nicole
    return (utils.obtener_color(color) + texto + utils.obtener_color("Defecto")) if texto != "" else ""

def calcular_puntos_ganados(arriesgos, gano):
    # Creador: Mercurio Nicole
    puntos = {
        1: 50,
        2: 40,
        3: 30,
        4: 20,
        5: 10,
    }

    return -100 if not gano else puntos[len(arriesgos)]