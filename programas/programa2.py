# -*- coding: utf-8 -*-
import re
import sys
from collections import Counter

def prog(texto):

    match = re.findall(r'"user": "(.*)",', texto)

    # Contar ocurrencias de cada usuario
    contador = Counter(match)

    # Eliminar duplicados y preservar el orden
    unique_matches = list(dict.fromkeys(match))

    ret = ""
    for usuario in unique_matches:
        ret += f"{usuario}: {contador[usuario]}\n"
        
    return ret.strip()


if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    f = open(entrada, 'r') # abrir archivo entrada
    datos = f.read()       # leer archivo entrada
    f.close()              # cerrar archivo entrada
    
    ret = prog(datos)      # ejecutar er
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
