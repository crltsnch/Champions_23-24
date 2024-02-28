import csv
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from urllib.parse import urlparse, unquote

# Lista de URLs de equipos
url = '''https://www.bdfutbol.com/es/t/trcompCHA.html?p=coaches&t=T'''

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