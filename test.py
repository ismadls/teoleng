# -*- coding: utf-8 -*-
import re
import sys
import os
import glob



if __name__ == '__main__':

	# CHEQUEAR VERSION DE PYTHON
	if (sys.version_info.major != 3 ) or (sys.version_info.minor < 7):
		print("Está usando la versión de Python: "+str(sys.version))
		sys.exit("Pero debe usar una versión de Python mayor a igual a la 3.7.X")
	
	# DIRECTORIO DE SALIDAS
	try:
		os.stat("salidas")
	except:
		os.mkdir("salidas")
	
	# ITERAR SOBRE LOS PROGRAMAS Y ENTRADAS
	errores = 0
	total = 0
	for archPrograma in sorted(glob.glob('programas'+os.sep+'*.py')):
		numPrograma = archPrograma[len(archPrograma) - 4]
		for archEntrada in sorted(glob.glob('entradas'+os.sep+'*.json')):
			total += 1
			# OBTENER LOS NOMBRES DE ARCHIVOS
			s = re.search(r"(\w+).py", archPrograma, flags=0)
			programa = s.group(1)
			s = re.search(r"(\d+)", archEntrada, flags=0)
			entrada = s.group(1)
			archSalida = "salidas" + os.sep + programa + '_' + entrada + ".txt"
			archSalidaOficial = "salidas_esperadas" + os.sep + programa + '_' + entrada + ".txt"

			# EJECUTAR EL PROGRAMA
			print("\nPrograma: "+programa+".py")
			print("Entrada: "+entrada+".json\n")
			ejecutar = '{0} {1} {2} {3}'.format(sys.executable, archPrograma, archEntrada, archSalida)
			print(ejecutar)
			x = os.system(ejecutar)
			if x != 0:
				print("ERROR: al ejecutar "+programa+" para la entrada "+entrada)
				errores += 1
			else:
				# COMPARAR LAS SALIDAS
				diferencias = "diff --strip-trailing-cr " + archSalida + " " + archSalidaOficial 
				print(diferencias+"\n")
				x = os.system(diferencias)		
				if x != 0:
					print("RESULTADO: ERROR (la salida no es la esperada).")
					errores += 1
				else:
					print("RESULTADO: OK")
				print("_________\n")
	
	# MOSTRAR RESULTADO
	t_error = 'error' if errores == 1 else 'errores'
	t_total = 'ejecución' if total == 1 else 'ejecuciones'
	print("\nResultado final: {0} {1} de {2} {3}.".format(errores,t_error,total,t_total))
	  
