import csv
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from urllib.parse import urlparse, unquote

# Lista de URLs de equipos
url = 'https://fbref.com/es/equipos/e2d8892c/Estadisticas-de-Paris-Saint-Germain'

''' [
    'https://fbref.com/es/equipos/054efa67/Estadisticas-de-Bayern-Munich',
    'https://fbref.com/es/equipos/18050b20/Estadisticas-de-FC-Copenhagen',
    'https://fbref.com/es/equipos/7213da33/Estadisticas-de-Lazio',
    'https://fbref.com/es/equipos/b8fd03ef/Estadisticas-de-Manchester-City',
    'https://fbref.com/es/equipos/18bb7c10/Estadisticas-de-Arsenal',
    'https://fbref.com/es/equipos/5e876ee6/Estadisticas-de-Porto',
    'https://fbref.com/es/equipos/206d90db/Estadisticas-de-Barcelona',
    'https://fbref.com/es/equipos/d48ad4ff/Estadisticas-de-Napoli',
    'https://fbref.com/es/equipos/53a2f082/Estadisticas-de-Real-Madrid',
    'https://fbref.com/es/equipos/acbb6a5b/Estadisticas-de-RB-Leipzig',
    'https://fbref.com/es/equipos/add600ae/Estadisticas-de-Dortmund',
    'https://fbref.com/es/equipos/e334d850/Estadisticas-de-PSV-Eindhoven',
    'https://fbref.com/es/equipos/d609edc0/Estadisticas-de-Internazionale',
    'https://fbref.com/es/equipos/db3b9613/Estadisticas-de-Atletico-Madrid',
    'https://fbref.com/es/equipos/1e1c0fbb/Estadisticas-de-Paris-Saint-Germain',
]'''

  # Realizamos la petición a la web
req = requests.get(url)
# Extraemos el HTML
html = req.text

# Obtener el path de la URL y dividirlo en partes usando '/'
path_parts = urlparse(url).path.split('/')

# Buscar la parte que contiene el nombre del equipo
nombre_equipo_part = next((part for part in reversed(path_parts) if part), None)

# Decodificar el nombre del equipo (reemplazar guiones con espacios)
nombre_equipo = unquote(nombre_equipo_part).replace('-', ' ')

# Validar si el nombre del equipo se obtuvo correctamente
if not nombre_equipo:
    print(f"No se pudo obtener el nombre del equipo del URL: {url}")
    exit()

# Verificar si la parte "Estadisticas-de-" está presente y quitarla del nombre del equipo
if "Estadisticas de " in nombre_equipo:
    nombre_equipo = nombre_equipo.replace("Estadisticas de ", "")

print(f"\nProcesando datos para: {nombre_equipo}")

# Objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Buscar en el HTML el elemento que se quiere
jugadores_data = soup.find('table', {'class': 'stats_table', 'id': 'stats_standard_13'})

# Verificar si se encontró la tabla
if jugadores_data:
    filas = jugadores_data.find_all('tr')
    datos = []

    # Iterar sobre las filas y obtener los datos de cada celda
    for idx, fila in enumerate(filas):
        # Obtener las celdas de cada fila
        celdas = fila.find_all(['th', 'td'])
        datos_fila = [celda.get_text(strip=True) for celda in celdas]
        if idx == 0:
            continue  # Saltar la primera fila (encabezados)
        elif datos_fila:
            datos_fila.append(nombre_equipo)
            datos.append(datos_fila)

    # Imprimir la tabla utilizando tabulate
    tabla = tabulate(datos[1:], headers=datos[0], tablefmt='fancy_grid')
    print(tabla)

    # Guardar los datos en un archivo CSV
    ruta_csv = 'data/jugadores.csv'
    with open(ruta_csv, 'a', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(datos)

else:
    print("No se encontró la tabla con las clases e ID especificados.")