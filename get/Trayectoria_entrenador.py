import csv
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from urllib.parse import urlparse, unquote
import pandas as pd

# Lista de URLs de equipos


import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

class TrayectoriaEntrenador:
    def __init__(self, urls, csv_file):
        self.urls = urls
        self.csv_file = csv_file
        self.resultados = []

    def extraer_datos(self):
        for idx, url in enumerate(self.urls):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            tabla = soup.find('div', {'id': 'traj', 'class': 'scrtraj mt-2'})
            
            if tabla:
                rows = tabla.find_all('tr')
                tabla_data = []
                for i, row in enumerate(rows[:-1]):
                    if i == 0:
                        continue
                    cells = row.find_all(['td', 'th'])
                    tabla_data.append([self.lista_ids_entrenador[idx]] + [cell.get_text(strip=True).replace('⬤', '') for cell in cells])
                
                self.resultados.extend(tabla_data)
            else:
                print('No se encontró la tabla en', url)

    def guardar_csv(self):
        encabezados = ['idEntrenador', 'Temporada', 'Equipo', 'Nun', 'Non', 'División', 'Edad', 'PJ', 'PG', 'PE', 'PP', 'Non']
        if len(self.resultados) > 0:
            self.resultados.insert(0, encabezados)
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(self.resultados)
            print(f'Se guardó la tabla en {self.csv_file}')
        else:
            print('La tabla no contiene datos.')

    def cargar_ids_entrenador(self, csv_path):
        df_entrenador = pd.read_csv(csv_path)
        self.lista_ids_entrenador = df_entrenador['idEntrenador'].tolist()
        self.lista_ids_entrenador.extend(['251', '252'])