from get.entrenadores import EntrenadorExtractor

def main():
    url = '''https://www.bdfutbol.com/es/t/trcompCHA.html?p=coaches&t=T'''
    extractor = EntrenadorExtractor(url)
    tabla_data = extractor.extraer_datos()
    if tabla_data:
        file_name = './data/entrenador.csv'
        extractor.guardar_datos_csv(tabla_data, file_name)

    