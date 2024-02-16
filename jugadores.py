import csv
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

#Tabla de datos de los jugadores de cada equipo de octavos de la UEFA

url = 'https://fbref.com/es/equipos/054efa67/Estadisticas-de-Bayern-Munich'

#Realizamos la petición a la web
req = requests.get(url)
#Extraigo el html
html = req.text

#Objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

#Busco en el html el elemento que quiero
jugadores_data = soup.find('table', {'class': 'stats_table', 'id': 'stats_standard_20'})
filas = jugadores_data.find_all('tr')

datos = []

#Iteramos sobre las filas y obtenemos los dato sde cada celda
for fila in filas:
    #Obtenemos las celdas de cada fila
    celdas = fila.find_all(['th', 'td'])
    datos_fila = [celda.get_text(strip=True) for celda in celdas]
    if datos_fila:
        datos.append(datos_fila)

tabla = tabulate(datos, headers=datos[0], tablefmt='fancy_grid')
print(tabla)

# Guardamos los datos en un archivo CSV
ruta_csv = 'jugadores.csv'
with open(ruta_csv, 'a', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(datos)