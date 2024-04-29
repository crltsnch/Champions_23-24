from get.entrenadores import EntrenadorExtractor
from get.equipo import EquipoExtractor
from get.jugador import JugadoresExtractor

def main():
     # Extracción y guardado de datos de entrenadores
    entrenador_url = 'https://www.bdfutbol.com/es/t/trcompCHA.html?p=coaches&t=T'
    entrenador_extractor = EntrenadorExtractor(entrenador_url)
    entrenador_tabla_data = entrenador_extractor.extraer_datos()
    if entrenador_tabla_data:
        entrenador_file_name = './data/entrenador.csv'
        entrenador_extractor.guardar_datos_csv(entrenador_tabla_data, entrenador_file_name)

    # Extracción y guardado de datos de equipos
    equipo_url = 'https://www.bdfutbol.com/es/t/trcompCHA.html'
    equipo_extractor = EquipoExtractor(equipo_url)
    equipo_tabla_data = equipo_extractor.extraer_datos()
    if equipo_tabla_data:
        equipo_file_name = './data/equipo.csv'
        equipo_extractor.guardar_datos(equipo_tabla_data, equipo_file_name)

    temporadas = ['2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022', '2022-2023', '2023-2024']
    scraper = JugadoresExtractor(temporadas)
    scraper.scrape_data()
    archivo_csv = './data/jugador2.csv'
    scraper.save_to_csv(archivo_csv)
    scraper.close_driver()

    
    
if __name__ == "__main__":
    main()
