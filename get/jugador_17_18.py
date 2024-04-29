from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

class Jugadores2Extractor:
    def __init__(self, temporadas):
        self.temporadas = temporadas
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
        self.datos_grandes = []

    def scrape_data(self):
        for temporada in self.temporadas:
            url = f'https://fbref.com/es/comps/8/{temporada}/stats/Estadisticas-{temporada}-Champions-League'
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            container = soup.find('div', {'class': 'table_container', 'id': 'div_stats_standard'})

            if container:
                table = container.find('table', {'class': 'stats_table'})
                if table:
                    for i, row in enumerate(table.find_all('tr')):
                        if i < 2:
                            continue
                        cells = row.find_all(['th', 'td'])
                        row_data = [temporada] + [cell.get_text(strip=True) for cell in cells]
                        self.datos_grandes.append(row_data)
                else:
                    print(f"No se encontró la tabla para la temporada {temporada}.")
            else:
                print(f"No se encontró el contenedor para la temporada {temporada}.")

    def save_to_csv(self, filename):
        encabezado = ['Temporada', '#', 'Jugador', 'País', 'Posc', 'Equipo', 'Edad', 'Nacimiento',
                      'PJ', 'Titular', 'Mín', '90 s', 'Gls.', 'Ass', 'G+A', 'G-TP', 'TP', 'TPint',
                      'TA', 'TR', 'xG', 'npxG', 'xAG', 'npxG+xAG', 'PrgC', 'PrgP', 'PrgR', 'Gls90.', 'Ast90',
                      'G+A90', 'G-TP90', 'G+A-TP90', 'xG90', 'xAG90', 'xG+xAG90', 'npxG90', 'npxG+xAG90', 'Partidos']
        df = pd.DataFrame(self.datos_grandes, columns=encabezado)
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"Datos grandes guardados en {filename}")

    def close_driver(self):
        self.driver.quit()