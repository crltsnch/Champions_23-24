from selenium import webdriver
from bs4 import BeautifulSoup
import csv
from tabulate import tabulate

# Lista de temporadas
temporadas = ['1992-1993', '1993-1994', '1994-1995', '1995-1996', '1996-1997',
              '1997-1998', '1998-1999', '1999-2000', '2000-2001', '2001-2002',
              '2002-2003', '2003-2004', '2004-2005', '2005-2006', '2006-2007',
              '2007-2008', '2008-2009', '2009-2010', '2010-2011', '2011-2012',
              '2012-2013', '2013-2014', '2014-2015', '2015-2016', '2016-2017']

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Para ejecutar el navegador en segundo plano (sin interfaz gráfica)
driver = webdriver.Chrome(options=options)

# Lista para almacenar todas las tablas
tabla_grande = []

encabezado = ['Temporada', '#', 'Jugador', 'País', 'Posc', 'Equipo', 'Edad', 'Nacimiento',
              'PJ', 'Titular', 'Mín', '90 s', 'Gls.', 'Ass', 'G+A', 'G-TP', 'TP', 'TPint',
              'TA', 'TR', 'Gls.90', 'Ast90', 'G+A90', 'G-TP90', 'G+A-TP90', 'Partidos']

# Iterar sobre las temporadas
for temporada in temporadas:
    # Construir la URL para la temporada actual
    url = f'https://fbref.com/es/comps/8/{temporada}/stats/Estadisticas-{temporada}-Champions-League'

    # Obtener la página web con Selenium
    driver.get(url)

    # Esperar a que la página cargue completamente (puedes ajustar el tiempo según sea necesario)
    driver.implicitly_wait(10)

    # Obtener el contenido HTML después de que la página haya cargado
    html = driver.page_source

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
            # Lista para almacenar los datos de una tabla
            tabla_temporada = []

            # Iterar sobre las filas de la tabla
            for i, row in enumerate(table.find_all('tr')):
                # Ignorar las primeras 2 filas (encabezados)
                if i <2:
                    continue
                # Obtener los datos de cada celda en la fila
                cells = row.find_all(['th', 'td'])
                row_data = [temporada]+[cell.get_text(strip=True) for cell in cells]
                tabla_temporada.append(row_data)

            # Almacenar la tabla de la temporada en la tabla grande
            tabla_grande.append(tabla_temporada)

        else:
            print(f"No se encontró la tabla para la temporada {temporada}.")
    else:
        print(f"No se encontró el contenedor para la temporada {temporada}.")

# Cerrar el navegador al final del script
driver.quit()
print(tabulate(tabla_grande, headers='firstrow', tablefmt='grid'))

'''# Guarda la fila de encabezado en un archivo CSV
if len(tabla_grande) > 0:
    tabla_grande.insert(0, encabezado)
    archivo_csv = './data/jugador.csv'
    print(tabulate(tabla_grande, headers='firstrow', tablefmt='grid'))
    with open(archivo_csv, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Escribe las filas de datos
        csv_writer.writerows(tabla_grande)

print(f"Tabla grande guardada en {archivo_csv}")'''


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