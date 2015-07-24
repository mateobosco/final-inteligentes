def formatear_salida():
	archivo = open('distances.dat')
	salida = open('output.csv', 'w+')
	for fila in archivo:
		fila = fila[0:-2]
		salida.write(fila)
		salida.write('\n')
	archivo.close()
	salida.close()

formatear_salida()