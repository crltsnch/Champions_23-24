from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

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

# Lista para almacenar todas las filas de datos
datos_grandes = []

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
            # Iterar sobre las filas de la tabla
            for i, row in enumerate(table.find_all('tr')):
                # Ignorar las primeras 2 filas (encabezados)
                if i < 2:
                    continue
                # Obtener los datos de cada celda en la fila
                cells = row.find_all(['th', 'td'])
                row_data = [temporada] + [cell.get_text(strip=True) for cell in cells]
                datos_grandes.append(row_data)

        else:
            print(f"No se encontró la tabla para la temporada {temporada}.")
    else:
        print(f"No se encontró el contenedor para la temporada {temporada}.")

# Cerrar el navegador al final del script
driver.quit()

# Convertir la lista de datos a un DataFrame de pandas
df = pd.DataFrame(datos_grandes, columns=encabezado)

# Guardar el DataFrame en un archivo CSV
archivo_csv = './data/jugador.csv'
df.to_csv(archivo_csv, index=False, encoding='utf-8')

print(f"Datos grandes guardados en {archivo_csv}")