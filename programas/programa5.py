import re
import sys

def prog(texto):
    er_p5 = r'(#{1,3})(.*?)(\\n)|(\*\*|\*)(.*?)(\*\*|\*)|(~+)(.*?)(~+)'

    def sustituir(match):
        if match.group(1):
            if len(match.group(1)) == 1:
                return "<h1>" + match.group(2) + "</h1>\\n"
            elif len(match.group(1)) == 2:
                return "<h2>" + match.group(2) + "</h2>\\n"
            elif len(match.group(1)) == 3:
                return "<h3>" + match.group(2) + "</h3>\\n"
        elif match.group(4) and len(match.group(4)) == 2:
            return "<strong>" + match.group(5) + "</strong>"
        elif match.group(4) and len(match.group(4)) == 1:
            return "<em>" + match.group(5) + "</em>"
        elif match.group(7):
            return "<s>" + match.group(8) + "</s>"
        else:
            return match.group(0)

    resultado = re.sub(er_p5, sustituir, texto)

    return resultado


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