from selenium import webdriver
from bs4 import BeautifulSoup

# URL de la página web
url = "https://fbref.com/es/comps/8/1992-1993/stats/Estadisticas-1992-1993-Champions-League"

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Para ejecutar el navegador en segundo plano (sin interfaz gráfica)
driver = webdriver.Chrome(options=options)

# Obtener la página web con Selenium
driver.get(url)

# Esperar a que la página cargue completamente (puedes ajustar el tiempo según sea necesario)
driver.implicitly_wait(10)

# Obtener el contenido HTML después de que la página haya cargado
html = driver.page_source

# Cerrar el navegador
driver.quit()

# Utilizar BeautifulSoup para analizar el HTML
soup = BeautifulSoup(html, 'html.parser')

# Encontrar el contenedor con la clase "table_container" y el ID "div_stats_standard"
container = soup.find('div', {'class': 'table_container', 'id': 'div_stats_standard'})

# Verificar si el contenedor se encontró
if container:
    # Encontrar la tabla dentro del contenedor por la clase "stats_table"
    table = container.find('table', {'class': 'stats_table'})

    # Verificar si la tabla se encontró
    if table:
        # Iterar sobre las filas de la tabla
        for row in table.find_all('tr'):
            # Obtener los datos de cada celda en la fila
            cells = row.find_all(['th', 'td'])
            row_data = [cell.text.strip() for cell in cells]

            # Imprimir los datos de la fila
            print(row_data)
    else:
        print("No se encontró la tabla dentro del contenedor.")
else:
    print("No se encontró el contenedor con la clase 'table_container' y el ID 'div_stats_standard'.")





'''import csv
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
        tabla = soup.find_all('table', {'class':"min_width"})

        # Verificar si se encontró la tabla
        if tabla:
            # Obtener todas las filas y celdas de la tabla
            rows = tabla.find_all('tr')

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


if len(resultados) > 0:
    resultados.insert(0, headers)
    # Especificar el nombre del archivo CSV donde guardar la tabla
    file_name = './data/Jugador.csv'
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(resultados)
    print(f'Se guardó la tabla en {file_name}')
else:
    print('La tabla no contiene datos.')
'''