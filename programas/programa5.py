import re
import sys

def prog(texto):
    
    # Conversión encabezados
    texto = re.sub(r'(###)(.*?)(\\n)', r'<h3>\2</h3>\\n', texto)
    texto = re.sub(r'(##)(.*?)(\\n)', r'<h2>\2</h2>\\n', texto)
    texto = re.sub(r'(#)(.*?)(\\n)', r'<h1>\2</h1>\\n', texto)

    # Conversión curisva y negrita
    texto = re.sub(r'(\*\*\*|___)(.*?)(\*\*\*|___)', r'<strong><em>\2</em></strong>', texto)
    texto = re.sub(r'(\*\*|__)(.*?)(\*\*|__)', r'<strong>\2</strong>', texto)
    texto = re.sub(r'(\*|_)(.*?)(\*|_)', r'<em>\2</em>', texto)

    # Conversión tachado
    texto = re.sub(r'(~+)(.*?)(~+)', r'<s>\2</s>', texto)

    return texto


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