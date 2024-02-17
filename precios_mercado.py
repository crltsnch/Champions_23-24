import csv
import requests
from bs4 import BeautifulSoup

# URL base de la paginación
base_url = 'https://www.transfermarkt.es/spieler-statistik/wertvollstespieler/marktwertetop?land_id=0&ausrichtung=alle&spielerposition_id=alle&altersklasse=alle&jahrgang=0&kontinent_id=6'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Verificar si la petición fue exitosa (código de estado 200)
response = requests.get(base_url, headers=headers)
if response.status_code == 200:
    # Obtener el contenido HTML de la página
    html = response.text

    # Crear un objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Buscar la tabla que corresponde a la clase "items"
    tabla = soup.find('table', {'class': 'items'})

    # Verificar si se encontró la tabla
    if tabla:
        # Crear una lista para almacenar las filas de datos
        tabla_data = []

        # Recorrer cada página
        current_page = 1
        while True:
            # Obtener todas las filas de la tabla
            rows = tabla.find_all('tr')

            # Recorrer cada fila y extraer el texto de las celdas
            for i, row in enumerate(rows):
                # Omitir la fila de encabezados
                if i == 0:
                    continue

                # Agregar solo las filas cuyos índices son múltiplos de 3 (1, 4, 7, 10, etc.)
                if i % 3 == 1:
                    cells = row.find_all(['td', 'th'])
                    row_data = [cell.get_text(strip=True) for cell in cells]
                    tabla_data.append(row_data)

            # Intentar encontrar el enlace a la siguiente página
            next_page_link = soup.find('a', {'class': 'next'})
            if next_page_link:
                # Construir la URL de la siguiente página
                current_page += 1
                next_page_url = f'{base_url}&page={current_page}'

                # Realizar una nueva solicitud para la siguiente página
                response = requests.get(next_page_url, headers=headers)
                if response.status_code == 200:
                    # Obtener el contenido HTML de la siguiente página
                    html = response.text
                    soup = BeautifulSoup(html, 'html.parser')
                else:
                    break
            else:
                # No hay más páginas, salir del bucle
                break

        # Añadir el encabezado personalizado
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
