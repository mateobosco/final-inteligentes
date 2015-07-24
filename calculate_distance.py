import csv
from geopy.distance import vincenty

def main():

	propiedades_csv = open('precio-terrenos-2014.csv')
	estaciones_csv = open('estaciones.csv')

	propiedades = csv.reader(propiedades_csv, delimiter=';')
	estaciones = csv.reader(estaciones_csv, delimiter=';')

	for prop in propiedades:
		ubicacion_propiedad = (prop[0], prop[1])
		print "propiedad"
		for est in estaciones:
			ubicacion_estacion = (est[3],est[4])
			print "estacion"
main()