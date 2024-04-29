import csv
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from urllib.parse import urlparse, unquote

class EntrenadorExtractor:
    def __init__(self, url):
        self.url = url

    def extraer_datos(self):
        # Realizar la solicitud GET y crear el objeto BeautifulSoup
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscar la tabla que corresponde a la clase "wikitable" y estilo "text-align:enter"
        tabla = soup.find('div', {'style': 'overflow: auto', 'class': 'w-100'})

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
            column_headers = ['idEntrenador', 'Pais', 'Apodo', 'Nombre', 'T', 'PJ', 'PG', 'PE', 'PP', '%']

            # Añadir encabezados a la tabla de datos solo si hay datos en la tabla
            if len(tabla_data) > 0:
                tabla_data.insert(0, column_headers)
                return tabla_data
            else:
                return None
        else:
            return None

    def guardar_datos_csv(self, tabla_data, file_name):
        if tabla_data:
            with open(file_name, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(tabla_data)
            print(f'Se guardó la tabla en {file_name}')
        else:
            print('No se encontraron datos para guardar.')
