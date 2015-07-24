import googlemaps
import csv
import simplejson
import urllib

from geopy.distance import great_circle


MAX_DISTANCE = 9999999

def googleDistance(sourceCoordinates, destinationCoordinates):
	url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=walking&language=en-EN&sensor=false".format(str(sourceCoordinates),str(destinationCoordinates))
	result= simplejson.load(urllib.urlopen(url))
	print result
	try:
		resulting_distance = result['rows'][0]['elements'][0]['distance']['text']
		resulting_distance = float(resulting_distance[0:-3])
	except:
		resulting_distance = MAX_DISTANCE
	print "calculo distancia entre " + str(sourceCoordinates) + " y " + str(destinationCoordinates) + " que dio " + str(resulting_distance)
	return resulting_distance

def geopyDistance(sourceCoordinates, destinationCoordinates):
	try:
		resulting_distance = great_circle(sourceCoordinates,destinationCoordinates).meters
	except:
		resulting_distance = MAX_DISTANCE
	print "calculo distancia entre " + str(sourceCoordinates) + " y " + str(destinationCoordinates) + " que dio " + str(resulting_distance)
	return resulting_distance

def minimo(vector, propiedad, output):
	minimo = MAX_DISTANCE
	for elem in vector:
		distancia = geopyDistance(propiedad, elem)
		if distancia < minimo: minimo = distancia
	output.write(str(minimo))
	output.write(',')

def get_vector(archivo, nLatitud, nLongitud):
	csv_file = open(archivo)

	registros = csv.reader(csv_file, delimiter=';')
	vector = []
	for reg in registros:
		vector.append((float(reg[nLatitud]), float(reg[nLongitud])))
	return vector

def get_estaciones():
	return get_vector('datos/estaciones.csv', 4, 3)

def get_propiedades():
	return get_vector('datos/precio-terrenos-2014.csv', 1, 0)

def get_hospitales():
	return get_vector('datos/hospitales.csv', 17, 16)

def get_metrobus():
	return get_vector('datos/metrobus-estaciones.csv', 7, 6)

def get_universidades():
	return get_vector('datos/universidades.csv', 13, 12)

def get_escuelas_publicas():
	return get_vector('datos/establecimientos-publicos.csv', 21, 20)

def get_escuelas_privadas():
	return get_vector('datos/establecimientos-privados.csv', 21, 20)

def get_centros_de_salud():
	return get_vector('datos/centros-salud-no-dependientes-GCBA.csv', 1, 0)

def get_bomberos():
	return get_vector('datos/cuarteles-destacamentos-bomberos-policia-federal.csv', 12, 11)

def get_comisarias():
	return get_vector('datos/comisarias-policia-federal.csv', 7, 6)

def main():
	output = open('distances.dat', 'w+')

	propiedades = get_propiedades()

	estaciones = get_estaciones()
	hospitales = get_hospitales()
	metrobuses = get_metrobus()
	universidades = get_universidades()
	escuelas_publicas = get_escuelas_publicas()
	escuelas_privadas = get_escuelas_privadas()
	centros_de_salud = get_centros_de_salud()
	bomberos = get_bomberos()
	comisarias = get_comisarias()

	for prop in propiedades:
		minimo(estaciones, prop, output)
		minimo(hospitales, prop, output)
		minimo(metrobuses, prop, output)
		minimo(universidades, prop, output)
		minimo(escuelas_publicas, prop, output)
		minimo(escuelas_privadas, prop, output)
		minimo(centros_de_salud, prop, output)
		minimo(bomberos, prop, output)
		minimo(comisarias, prop, output)

		output.write('\n')
		output.flush()

	output.close()

def test():
	t_file = open("apitoken")
	for l in file:
		token = l
	client = googlemaps.Client(token)

	terreno = (-34.553169236899983, -58.455626942116282)
	estacion = (-34.6357419968607, -58.3989485118757)
	response = client.directions(str(terreno), str(estacion), mode="walking", units="metric")
	print response
	
	# print calculateDistance(terreno, estacion)


# test()
main()
