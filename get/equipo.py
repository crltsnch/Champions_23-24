import csv
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from urllib.parse import urlparse, unquote

# Lista de URLs de equipos
url = '''https://www.bdfutbol.com/es/t/trcompCHA.html'''

# Realizar la solicitud GET y crear el objeto BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Buscar la tabla que corresponde a la clase "wikitable" y estilo "text-align:enter"
tabla = soup.find('div', style='width:100%;overflow: auto;')

# Verificar si se encontró la tabla
if tabla:
    # Obtener todas las filas y celdas de la tabla
    rows = tabla.find_all('tr')

    # Crear una lista para almacenar las filas de datos
    tabla_data = []

    # Recorrer cada fila y extraer el texto de las celdas
    for i, row in enumerate(rows):
        if i == 0:
            continue
        cells = row.find_all(['td', 'th'])
        row_data = [cell.get_text(strip=True) for cell in cells]
        tabla_data.append(row_data)

    # Encabezados de las columnas
    column_headers = ['idEquipo', 'Nombre', 'Pais', 'T', 'PJ', 'PG', 'PE', 'PP', '%', 'Títulos', 'F', '1/2', '1/4', '1/8', '1/16', 'GF', 'GC', 'TA', 'TR']

    # Añadir encabezados a la tabla de datos solo si hay datos en la tabla
    if len(tabla_data) > 0:
        tabla_data.insert(0, column_headers)
        print(tabulate(tabla_data, headers='firstrow', tablefmt='grid'))
        # Especificar el nombre del archivo CSV donde guardar la tabla
        file_name = './data/equipo.csv'
        with open(file_name, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(tabla_data)
        print(f'Se guardó la tabla en {file_name}')
    else:
        print('La tabla no contiene datos.')

else:
    print('No se encontró la tabla')