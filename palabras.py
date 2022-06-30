import os
import re
import logica

CARPETA_ARCHIVOS = "./textos"

def procesar_linea(archivo):
    # Función para obtener las palabras de una linea de un archivo
    # Creador: Gimenez Ignacio
    linea = archivo.readline()
    if linea != "":
        linea = re.sub('[^a-zA-Z\s]', '', linea).split()
    
    return linea

def obtener_palabras_desde_archivos(cantidad_letras_palabras):
    # Función para obtener todas las palabras de x cantidad de letras
    # Creador: Gimenez Ignacio
    diccionario = {}
    numero_archivo = -1

    for nombre_archivo in os.listdir(CARPETA_ARCHIVOS):
        with open(os.path.join(CARPETA_ARCHIVOS, nombre_archivo)) as archivo:
            numero_archivo += 1
            linea = procesar_linea(archivo)

            while linea != "":
                for palabra in linea:
                    palabra = logica.normalizar_palabra(palabra)
                    if len(palabra) == cantidad_letras_palabras:
                        diccionario.setdefault(palabra, [0, 0, 0])
                        diccionario[palabra][numero_archivo] += 1
                linea = procesar_linea(archivo)

    return diccionario

def escribir_archivo_posibles_palabras(diccionario_palabras):
    # Función para guardar las palabras dentro del archivo "palabras.csv" en orden alfabetico
    # Creador: Gimenez Ignacio
    palabras = sorted(list(diccionario_palabras.keys()))

    with open("palabras.csv", "w") as archivo:
        for palabra in palabras:
            archivo.write("{},{},{},{}\n".format(palabra, diccionario_palabras[palabra][0], diccionario_palabras[palabra][1], diccionario_palabras[palabra][2]))
