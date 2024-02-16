import csv
import requests
from bs4 import BeautifulSoup

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

