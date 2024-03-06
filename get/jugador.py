import csv
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from urllib.parse import urlparse, unquote

# Lista de temporadas
temporadas = ['2022-2023']

resultados = []
headers = ['#', 'Jugador', 'País', 'Posc', 'Equipo', 'Edad', 'Nacimiento', 'PJ', 'Titular', 'Mín', '90 s', 'Gls.', 'Ass', 'G+A', 'G-TP', 'TP', 'TPint', 'TA', 'TR', 'Gls.90', 'Ast90', 'G+A90', 'G-TP90', 'G+A-TP90', 'Partidos']

for temporada in temporadas:
    url = f'https://fbref.com/es/comps/8/{temporada}/stats/Estadisticas-{temporada}-Champions-League'
    
    # Realizar la solicitud GET y crear el objeto BeautifulSoup
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscar la tabla que corresponde a la clase "wikitable" y estilo "text-align:enter"
        tabla = soup.find_all('table', class_='min_width')
        print(tabla)

        # Verificar si se encontró la tabla
        if tabla:
            # Obtener todas las filas y celdas de la tabla
            rows = tabla[1].find_all('tr')

            # Crear una lista para almacenar las filas de datos
            tabla_data = []

            # Recorrer cada fila y extraer el texto de las celdas
            for i, row in enumerate(rows):
                if i == 0 or i == 1:
                    continue
                cells = row.find_all(['td', 'th'])
                row_data = [cell.get_text(strip=True) for cell in cells]
                tabla_data.append([temporada]+row_data)

            # Agregar los resultados a la lista general
            resultados.extend(tabla_data)
            print(tabulate(tabla_data,  tablefmt='grid'))

        else:
            print('No se encontró la tabla')


'''if len(resultados) > 0:
    resultados.insert(0, headers)
    # Especificar el nombre del archivo CSV donde guardar la tabla
    file_name = './data/Jugador.csv'
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(resultados)
    print(f'Se guardó la tabla en {file_name}')
else:
    print('La tabla no contiene datos.')'''
