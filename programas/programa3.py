# -*- coding: utf-8 -*-
import re
import sys

# " timestamp ": "T 2023:03:15 10:30:00" ,



def obtener_nombre_mes(numero):
    meses = {
        "01": "enero",
        "02": "febrero",
        "03": "marzo",
        "04": "abril",
        "05": "mayo",
        "06": "junio",
        "07": "julio",
        "08": "agosto",
        "09": "septiembre",
        "10": "octubre",
        "11": "noviembre",
        "12": "diciembre"
    }
    
    # Devuelve el nombre del mes correspondiente al número proporcionado
    return meses.get(numero, "Mes inválido")




def prog(texto):

    matchAnio = re.findall(r'"timestamp": "T (\d{4}):', texto)
    matchMes = re.findall(r'"timestamp": "T \d{4}:(\d{2}):', texto) 
    matchDia = re.findall(r'"timestamp": "T \d{4}:\d{2}:(\d{2}) \d{2}:', texto) 
    matchHora = re.findall(r'"timestamp": "T \d{4}:\d{2}:\d{2} (.*):\d{2}",', texto) 


    #15 de marzo del 2023 a las 08:00 hs

    ret = ""
    var = 0
    print(len(matchAnio))
    for anio in matchAnio:
        
        ret += f"{matchDia[var]} de {obtener_nombre_mes(matchMes[var])} del {anio} a las {matchHora[var]} hs.\n"
        var += 1
        
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