import csv
import requests
from bs4 import BeautifulSoup

# Encabezados de las columnas
encabezados = ['Temporada','Ronda','Wk','Dia','Fecha','Hora','Local','Resultado','Visitante','Público','Evento','Arbitro','Reporte','Notas']

# URLs de diferentes temporadas de UEFA Champions League
urls = [
    'https://fbref.com/en/comps/8/2022-2023/schedule/2022-2023-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2021-2022/schedule/2021-2022-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2020-2021/schedule/2020-2021-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2019-2020/schedule/2019-2020-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2018-2019/schedule/2018-2019-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2017-2018/schedule/2017-2018-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2016-2017/schedule/2016-2017-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2015-2016/schedule/2015-2016-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2014-2015/schedule/2014-2015-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2013-2014/schedule/2013-2014-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2012-2013/schedule/2012-2013-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2011-2012/schedule/2011-2012-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2010-2011/schedule/2010-2011-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2009-2010/schedule/2009-2010-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2008-2009/schedule/2008-2009-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2007-2008/schedule/2007-2008-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2006-2007/schedule/2006-2007-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2005-2006/schedule/2005-2006-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2004-2005/schedule/2004-2005-Champions-League-Scores-and-Fixtures',
    'https://fbref.com/en/comps/8/2003-2004/schedule/2003-2004-Champions-League-Scores-and-Fixtures',
]

# Función para eliminar la columna de la posición 2 en las filas que cumplen la condición
def eliminar_columna_group_stage(datos_tabla):
    indices_a_eliminar = [i for i, fila in enumerate(datos_tabla[1:], start=1) if fila[2] == 'group stage']
    for i in indices_a_eliminar:
        if len(datos_tabla[i]) > 2:
            del datos_tabla[i][2]
        else:
            datos_tabla[i].insert(2, '')  # Agregar una cadena vacía si la columna no existe
    return datos_tabla

# Creamos una lista para almacenar los datos de todas las temporadas
datos_totales = []

# Iteramos sobre los URLs
for url in urls:

    # Realizamos una solicitud GET a la URL
    r = requests.get(url)
    # Extraemos el HTML de la respuesta
    html = r.text
    # Creamos un objeto BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Buscamos la sección de texto que contiene la información de las fases eliminatorias
    table = soup.find('table', {'class': 'stats_table', 'id': 'sched_all'})

    # Obtenemos las filas de la tabla
    filas = table.find_all('tr')

    # Iteramos sobre las filas y obtenemos los datos de cada celda
    datos_tabla = []
    for fila in filas:
        # Obtenemos las celdas de la fila
        celdas = fila.find_all(['th', 'td'])
        # Eliminamos las celdas que contienen 'xg' en el atributo 'data-stat' ya que no están en todas las temporadas
        celdas = [celda for celda in celdas if 'xg' not in celda.get('data-stat') and 'wk' not in celda.get('data-stat')]
        # Extraemos el texto de cada celda y lo agregamos a la lista de datos, eliminando los espacios en blanco
        datos_fila = [celda.get_text(strip=True) if celda.get_text(strip=True) else '' for celda in celdas]
        # Agregamos la temporada como la primera columna en cada fila, extrayéndola de la URL directamente
        temporada = url.split('/')[-3]
        datos_fila.insert(0, temporada)
        datos_tabla.append(datos_fila)

    # Aplicamos la función para eliminar la columna de la posición 2 en las filas que cumplen la condición
    datos_tabla = eliminar_columna_group_stage(datos_tabla)

    # Cambiamos el encabezado de la primera columna
    datos_tabla[0][0] = 'Temporada'

    # Agregamos los datos de la tabla a la lista general
    datos_totales.extend(datos_tabla)

# Imprimir la lista final
print(datos_totales)

# Escribimos los datos en un archivo CSV
datos_totales.insert(0, encabezados)
ruta_csv = './data/partido.csv'
with open(ruta_csv, 'w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    for fila in datos_totales:
        escritor_csv.writerow(fila)

# Imprimimos un mensaje de éxito
print(f"El archivo CSV '{ruta_csv.split('/')[-1]}' ha sido creado exitosamente.")
