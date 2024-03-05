import csv
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from urllib.parse import urlparse, unquote
import time

#Lista de temporadas
temporadas = [
    '1992-1993', '1993-1994', '1994-1995', '1995-1996', '1996-1997',
    '1997-1998', '1998-1999', '1999-2000', '2000-2001', '2001-2002',
    '2002-2003', '2003-2004', '2004-2005', '2005-2006', '2006-2007',
    '2007-2008', '2008-2009', '2009-2010', '2010-2011', '2011-2012',
    '2012-2013', '2013-2014', '2014-2015', '2015-2016', '2016-2017']

#A partir del 16-17 la tabla cambia
'''    '2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022',
    '2022-2023', '2023-2024'
]
'''



resultados = []
headers = ['#', 'Jugador', 'País', 'Posc', 'Equipo', 'Edad', 'Nacimiento', 'PJ', 'Titular', 'Mín', '90 s', 'Gls.', 'Ass', 'G+A', 'G-TP', 'TP', 'TPint', 'TA', 'TR', 'Gls.90', 'Ast90', 'G+A90', 'G-TP90', 'G+A-TP90', 'Partidos']


for temporada in temporadas:
    url = f'https://fbref.com/es/comps/8/{temporada}/stats/Estadisticas-{temporada}-Champions-League'
    # Realizar la solicitud GET y crear el objeto BeautifulSoup
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscar la tabla que corresponde a la clase "wikitable" y estilo "text-align:enter"
        tabla = soup.find('table', {'class': 'min_width', 'id': 'stats_standard'})

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
