import csv
import requests
from bs4 import BeautifulSoup

class PartidoScraper:
    def __init__(self):
        self.datos_totales = []

    def eliminar_columna_group_stage(self, datos_tabla):
        indices_a_eliminar = [i for i, fila in enumerate(datos_tabla[1:], start=1) if fila[2] == 'group stage']
        for i in indices_a_eliminar:
            if len(datos_tabla[i]) > 2:
                del datos_tabla[i][2]
            else:
                datos_tabla[i].insert(2, '')  # Agregar una cadena vacía si la columna no existe
        return datos_tabla

    def scrape_data(self, temporadas):
        for temporada in temporadas:
            url = f"https://fbref.com/en/comps/8/{temporada}/schedule/{temporada}-Champions-League-Scores-and-Fixtures"
            r = requests.get(url)
            html = r.text
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.find('table', {'class': 'stats_table', 'id': 'sched_all'})

            if table:
                filas = table.find_all('tr')
                datos_tabla = []
                for fila in filas:
                    celdas = fila.find_all(['th', 'td'])
                    celdas = [celda for celda in celdas if 'xg' not in celda.get('data-stat') and 'wk' not in celda.get('data-stat')]
                    datos_fila = [celda.get_text(strip=True) if celda.get_text(strip=True) else '' for celda in celdas]
                    datos_fila.insert(0, temporada)
                    datos_tabla.append(datos_fila)

                datos_tabla = self.eliminar_columna_group_stage(datos_tabla)
                datos_tabla[0][0] = 'Temporada'
                self.datos_totales.extend(datos_tabla)
            else:
                print(f"No se encontró la tabla para la temporada {temporada}")

    def guardar_datos_csv(self, filename):
        encabezados = ['Temporada', 'Ronda', 'Wk', 'Dia', 'Fecha', 'Hora', 'Local', 'Resultado', 'Visitante', 'Público', 'Evento', 'Árbitro', 'Reporte', 'Notas']
        self.datos_totales.insert(0, encabezados)
        with open(filename, 'w', newline='', encoding='utf-8') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            for fila in self.datos_totales:
                escritor_csv.writerow(fila)
        print(f"Datos de partidos guardados en {filename}")
