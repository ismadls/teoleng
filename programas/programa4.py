import re
import sys

def prog(texto):
    er_p4 = r'#?#?#(.*?)\\n'
    match = re.findall(er_p4, texto)

    unique_matches = list(dict.fromkeys(match))

    ret = "\n".join(f"{header}" for header in unique_matches)
    return ret

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