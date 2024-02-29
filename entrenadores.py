import csv
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from urllib.parse import urlparse, unquote

# Lista de URLs de equipos
url = '''https://www.bdfutbol.com/es/t/trcompCHA.html?p=coaches'''

# Realizar la solicitud GET y crear el objeto BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#Buscar la tabla que corresponde a la clase "wikitable" y estilo "text-align:enter"
tabla = soup.find('div', {'style': 'overflow: auto', 'class': 'w-100'})

#Verificamos si esta
if tabla:
    #Obtener todas las filas y celdas de la tabla
	rows = tabla.find_all('tr')

	#Crear una lista para almacenas las filas de datos
	tabla_data = []

	#Recorrer cada fila y extraer el texto de las celdas
	for i, row in enumerate(rows):
		# Omitir la primera iteración (i == 0) para evitar la primera fila de nombres de columnas
		if i == 0:
			continue
		cells = row.find_all(['td', 'th'])
		row_data = [cell.get_text(strip=True) for cell in cells]
			
		tabla_data.append(row_data)
		print(tabla_data)

'''	#Especicificar nombre del csv donde guardar la tabla
	file_name = 'data/octavos.csv'
	with open(file_name, 'a', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerows(tabla_data)
	print(f'Se guardó la tabla en {file_name}')'''

