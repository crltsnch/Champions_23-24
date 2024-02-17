import csv
import requests
from bs4 import BeautifulSoup

# URL del sitio web
url = 'https://www.transfermarkt.es/spieler-statistik/wertvollstespieler/marktwertetop?land_id=0&ausrichtung=alle&spielerposition_id=alle&altersklasse=alle&jahrgang=0&kontinent_id=6'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)
'''# Realizar la petición HTTP
response = requests.get(url)'''

# Verificar si la petición fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener el contenido HTML de la página
    html = response.text

    # Crear un objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Buscar la tabla que corresponde a la clase "wikitable" y estilo "text-align:center"
    tabla = soup.find('table', {'class': 'items'})

    # Verificar si se encontró la tabla
    if tabla:
        # Obtener todas las filas de la tabla
        rows = tabla.find_all('tr')

        # Crear una lista para almacenar las filas de datos
        tabla_data = []

        for i, row in enumerate(rows):
            # Omitir la fila de encabezados
            if i == 0:
                continue

            # Agregar solo las filas cuyos índices son múltiplos de 3 (1, 4, 7, 10, etc.)
            if i % 3 == 1:
                cells = row.find_all(['td', 'th'])
                row_data = [cell.get_text(strip=True) for cell in cells]
                row_data.pop(1)
                tabla_data.append(row_data)
    
        
    #print(tabla_data)
        header = ['#', 'null', 'jugador', 'posicion', 'edad', 'null', 'null', 'valor']
        tabla_data.insert(0, header)
    # Especificar el nombre del archivo CSV donde guardar la tabla
        file_name = 'valor_jugadores.csv'
        with open(file_name, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(tabla_data)
        print(f'Se guardó la tabla en {file_name}')

    else:
        print('No se encontró la tabla')
else:
    print(f"Error al realizar la solicitud. Código de estado: {response.status_code}")
