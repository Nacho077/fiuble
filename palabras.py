import os
import re

CARPETA_ARCHIVOS = "./textos"
CANTIDAD_LETRAS_PALABRAS = 5

def procesar_linea(archivo):
    linea = archivo.readline()
    if linea != "":
        linea = re.sub('[^a-zA-Z\s]', '', linea).split()
    
    return linea

diccionario = {}
numero_archivo = 1

for nombre_archivo in os.listdir(CARPETA_ARCHIVOS):
    with open(os.path.join(CARPETA_ARCHIVOS, nombre_archivo)) as archivo:
        numero_archivo += 1
        linea = procesar_linea(archivo)
        while linea != "":
            for palabra in linea:
                if len(palabra) == CANTIDAD_LETRAS_PALABRAS:
                    diccionario.setdefault(palabra, [0, 0, 0])
                    diccionario[palabra][numero_archivo] += 1
            linea = procesar_linea(archivo)

print(diccionario)
