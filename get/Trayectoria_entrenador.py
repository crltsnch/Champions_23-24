import csv
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from urllib.parse import urlparse, unquote
import pandas as pd

# Lista de URLs de equipos
urls = ['https://www.bdfutbol.com/es/l/l93816.html',
    'https://www.bdfutbol.com/es/l/l93761.html',
    'https://www.bdfutbol.com/es/l/l95279.html',
    'https://www.bdfutbol.com/es/l/l1566.html',
    'https://www.bdfutbol.com/es/l/l99573.html',
    'https://www.bdfutbol.com/es/l/l3685.html',
    'https://www.bdfutbol.com/es/l/l3787.html',
    'https://www.bdfutbol.com/es/l/l92334.html',
    'https://www.bdfutbol.com/es/l/l581.html',
    'https://www.bdfutbol.com/es/l/l97338.html',
    'https://www.bdfutbol.com/es/l/l4204.html',
    'https://www.bdfutbol.com/es/l/l90180.html',
    'https://www.bdfutbol.com/es/l/l41929.html',
    'https://www.bdfutbol.com/es/l/l4094.html',
    'https://www.bdfutbol.com/es/l/l92445.html',
    'https://www.bdfutbol.com/es/l/l95877.html',
    'https://www.bdfutbol.com/es/l/l96259.html',
    'https://www.bdfutbol.com/es/l/l41916.html',
    'https://www.bdfutbol.com/es/l/l2398.html',
    'https://www.bdfutbol.com/es/l/l7360.html',
    'https://www.bdfutbol.com/es/l/l7442.html',
    'https://www.bdfutbol.com/es/l/l3301.html',
    'https://www.bdfutbol.com/es/l/l3059.html',
    'https://www.bdfutbol.com/es/l/l44856.html',
    'https://www.bdfutbol.com/es/l/l94062.html',
    'https://www.bdfutbol.com/es/l/l70062.html',
    'https://www.bdfutbol.com/es/l/l93315.html',
    'https://www.bdfutbol.com/es/l/l95965.html',
    'https://www.bdfutbol.com/es/l/l5057.html',
    'https://www.bdfutbol.com/es/l/l93049.html',
    'https://www.bdfutbol.com/es/l/l50386.html',
    'https://www.bdfutbol.com/es/l/l3658.html',
    'https://www.bdfutbol.com/es/l/l93678.html',
    'https://www.bdfutbol.com/es/l/l47240.html',
    'https://www.bdfutbol.com/es/l/l4363.html',
    'https://www.bdfutbol.com/es/l/l7443.html',
    'https://www.bdfutbol.com/es/l/l2558.html',
    'https://www.bdfutbol.com/es/l/l83077.html',
    'https://www.bdfutbol.com/es/l/l2664.html',
    'https://www.bdfutbol.com/es/l/l80029.html',
    'https://www.bdfutbol.com/es/l/l4130.html',
    'https://www.bdfutbol.com/es/l/l95974.html',
    'https://www.bdfutbol.com/es/l/l4416.html',
    'https://www.bdfutbol.com/es/l/l46822.html',
    'https://www.bdfutbol.com/es/l/l93130.html',
    'https://www.bdfutbol.com/es/l/l566.html',
    'https://www.bdfutbol.com/es/l/l78784.html',
    'https://www.bdfutbol.com/es/l/l95034.html',
    'https://www.bdfutbol.com/es/l/l90120.html',
    'https://www.bdfutbol.com/es/l/l1734.html',
    'https://www.bdfutbol.com/es/l/l697.html',
    'https://www.bdfutbol.com/es/l/l1953.html',
    'https://www.bdfutbol.com/es/l/l500180.html',
    'https://www.bdfutbol.com/es/l/l92114.html',
    'https://www.bdfutbol.com/es/l/l26120.html',
    'https://www.bdfutbol.com/es/l/l80000.html',
    'https://www.bdfutbol.com/es/l/l20408.html',
    'https://www.bdfutbol.com/es/l/l3033.html',
    'https://www.bdfutbol.com/es/l/l3686.html',
    'https://www.bdfutbol.com/es/l/l95522.html',
    'https://www.bdfutbol.com/es/l/l79598.html',
    'https://www.bdfutbol.com/es/l/l3179.html',
    'https://www.bdfutbol.com/es/l/l46179.html',
    'https://www.bdfutbol.com/es/l/l7445.html',
    'https://www.bdfutbol.com/es/l/l90210.html',
    'https://www.bdfutbol.com/es/l/l1799.html',
    'https://www.bdfutbol.com/es/l/l51756.html',
    'https://www.bdfutbol.com/es/l/l1695.html',
    'https://www.bdfutbol.com/es/l/l57075.html',
    'https://www.bdfutbol.com/es/l/l92019.html',
    'https://www.bdfutbol.com/es/l/l90927.html',
    'https://www.bdfutbol.com/es/l/l95834.html',
    'https://www.bdfutbol.com/es/l/l5282.html',
    'https://www.bdfutbol.com/es/l/l4080.html',
    'https://www.bdfutbol.com/es/l/l90060.html',
    'https://www.bdfutbol.com/es/l/l45571.html',
    'https://www.bdfutbol.com/es/l/l92394.html',
    'https://www.bdfutbol.com/es/l/l96046.html',
    'https://www.bdfutbol.com/es/l/l45675.html',
    'https://www.bdfutbol.com/es/l/l70079.html',
    'https://www.bdfutbol.com/es/l/l92338.html',
    'https://www.bdfutbol.com/es/l/l7433.html',
    'https://www.bdfutbol.com/es/l/l7439.html',
    'https://www.bdfutbol.com/es/l/l93716.html',
    'https://www.bdfutbol.com/es/l/l49254.html',
    'https://www.bdfutbol.com/es/l/l90240.html',
    'https://www.bdfutbol.com/es/l/l93732.html',
    'https://www.bdfutbol.com/es/l/l701769.html',
    'https://www.bdfutbol.com/es/l/l53333.html',
    'https://www.bdfutbol.com/es/l/l45032.html',
    'https://www.bdfutbol.com/es/l/l50395.html',
    'https://www.bdfutbol.com/es/l/l7441.html',
    'https://www.bdfutbol.com/es/l/l42607.html',
    'https://www.bdfutbol.com/es/l/l95542.html',
    'https://www.bdfutbol.com/es/l/l77396.html',
    'https://www.bdfutbol.com/es/l/l92770.html',
    'https://www.bdfutbol.com/es/l/l93802.html',
    'https://www.bdfutbol.com/es/l/l82124.html',
    'https://www.bdfutbol.com/es/l/l2079.html',
    'https://www.bdfutbol.com/es/l/l43496.html',
    'https://www.bdfutbol.com/es/l/l41782.html',
    'https://www.bdfutbol.com/es/l/l7412.html',
    'https://www.bdfutbol.com/es/l/l80744.html',
    'https://www.bdfutbol.com/es/l/l95994.html',
    'https://www.bdfutbol.com/es/l/l50404.html',
    'https://www.bdfutbol.com/es/l/l901.html',
    'https://www.bdfutbol.com/es/l/l98503.html',
    'https://www.bdfutbol.com/es/l/l90519.html',
    'https://www.bdfutbol.com/es/l/l93619.html',
    'https://www.bdfutbol.com/es/l/l91891.html',
    'https://www.bdfutbol.com/es/l/l42540.html',
    'https://www.bdfutbol.com/es/l/l97100.html',
    'https://www.bdfutbol.com/es/l/l700142.html',
    'https://www.bdfutbol.com/es/l/l70156.html',
    'https://www.bdfutbol.com/es/l/l94848.html',
    'https://www.bdfutbol.com/es/l/l59586.html',
    'https://www.bdfutbol.com/es/l/l83850.html',
    'https://www.bdfutbol.com/es/l/l56797.html',
    'https://www.bdfutbol.com/es/l/l72547.html',
    'https://www.bdfutbol.com/es/l/l72173.html',
    'https://www.bdfutbol.com/es/l/l4103.html',
    'https://www.bdfutbol.com/es/l/l45891.html',
    'https://www.bdfutbol.com/es/l/l2921.html',
    'https://www.bdfutbol.com/es/l/l40026.html',
    'https://www.bdfutbol.com/es/l/l99153.html',
    'https://www.bdfutbol.com/es/l/l8440.html',
    'https://www.bdfutbol.com/es/l/l97203.html',
    'https://www.bdfutbol.com/es/l/l5729.html',
    'https://www.bdfutbol.com/es/l/l2198.html',
    'https://www.bdfutbol.com/es/l/l98959.html',
    'https://www.bdfutbol.com/es/l/l90030.html',
    'https://www.bdfutbol.com/es/l/l44657.html',
    'https://www.bdfutbol.com/es/l/l46986.html',
    'https://www.bdfutbol.com/es/l/l48470.html',
    'https://www.bdfutbol.com/es/l/l47452.html',
    'https://www.bdfutbol.com/es/l/l110525.html',
    'https://www.bdfutbol.com/es/l/l96317.html',
    'https://www.bdfutbol.com/es/l/l90000.html',
    'https://www.bdfutbol.com/es/l/l93829.html',
    'https://www.bdfutbol.com/es/l/l98767.html',
    'https://www.bdfutbol.com/es/l/l75630.html',
    'https://www.bdfutbol.com/es/l/l42718.html',
    'https://www.bdfutbol.com/es/l/l89751.html',
    'https://www.bdfutbol.com/es/l/l4230.html',
    'https://www.bdfutbol.com/es/l/l50943.html',
    'https://www.bdfutbol.com/es/l/l70099.html',
    'https://www.bdfutbol.com/es/l/l98404.html',
    'https://www.bdfutbol.com/es/l/l73107.html',
    'https://www.bdfutbol.com/es/l/l8393.html',
    'https://www.bdfutbol.com/es/l/l80460.html',
    'https://www.bdfutbol.com/es/l/l70864.html',
    'https://www.bdfutbol.com/es/l/l99474.html',
    'https://www.bdfutbol.com/es/l/l43576.html',
    'https://www.bdfutbol.com/es/l/l1925.html',
    'https://www.bdfutbol.com/es/l/l3039.html',
    'https://www.bdfutbol.com/es/l/l94144.html',
    'https://www.bdfutbol.com/es/l/l40838.html',
    'https://www.bdfutbol.com/es/l/l78087.html',
    'https://www.bdfutbol.com/es/l/l94597.html',
    'https://www.bdfutbol.com/es/l/l86247.html',
    'https://www.bdfutbol.com/es/l/l44089.html',
    'https://www.bdfutbol.com/es/l/l692.html',
    'https://www.bdfutbol.com/es/l/l79790.html',
    'https://www.bdfutbol.com/es/l/l52447.html',
    'https://www.bdfutbol.com/es/l/l96313.html',
    'https://www.bdfutbol.com/es/l/l95083.html',
    'https://www.bdfutbol.com/es/l/l45492.html',
    'https://www.bdfutbol.com/es/l/l5121.html',
    'https://www.bdfutbol.com/es/l/l2518.html',
    'https://www.bdfutbol.com/es/l/l84336.html',
    'https://www.bdfutbol.com/es/l/l2247.html',
    'https://www.bdfutbol.com/es/l/l73895.html',
    'https://www.bdfutbol.com/es/l/l96253.html',
    'https://www.bdfutbol.com/es/l/l43308.html',
    'https://www.bdfutbol.com/es/l/l29715.html',
    'https://www.bdfutbol.com/es/l/l82962.html',
    'https://www.bdfutbol.com/es/l/l84614.html',
    'https://www.bdfutbol.com/es/l/l80231.html',
    'https://www.bdfutbol.com/es/l/l3936.html',
    'https://www.bdfutbol.com/es/l/l2818.html',
    'https://www.bdfutbol.com/es/l/l79265.html',
    'https://www.bdfutbol.com/es/l/l71268.html',
    'https://www.bdfutbol.com/es/l/l70999.html',
    'https://www.bdfutbol.com/es/l/l57796.html',
    'https://www.bdfutbol.com/es/l/l702156.html',
    'https://www.bdfutbol.com/es/l/l93677.html',
    'https://www.bdfutbol.com/es/l/l98475.html',
    'https://www.bdfutbol.com/es/l/l51865.html',
    'https://www.bdfutbol.com/es/l/l42845.html',
    'https://www.bdfutbol.com/es/l/l50985.html',
    'https://www.bdfutbol.com/es/l/l47134.html',
    'https://www.bdfutbol.com/es/l/l7447.html',
    'https://www.bdfutbol.com/es/l/l43595.html',
    'https://www.bdfutbol.com/es/l/l25665.html',
    'https://www.bdfutbol.com/es/l/l702035.html',
    'https://www.bdfutbol.com/es/l/l93755.html',
    'https://www.bdfutbol.com/es/l/l316.html',
    'https://www.bdfutbol.com/es/l/l93602.html',
    'https://www.bdfutbol.com/es/l/l48813.html',
    'https://www.bdfutbol.com/es/l/l71771.html',
    'https://www.bdfutbol.com/es/l/l80413.html',
    'https://www.bdfutbol.com/es/l/l2096.html',
    'https://www.bdfutbol.com/es/l/l4184.html',
    'https://www.bdfutbol.com/es/l/l90145.html',
    'https://www.bdfutbol.com/es/l/l54215.html',
    'https://www.bdfutbol.com/es/l/l52818.html',
    'https://www.bdfutbol.com/es/l/l613.html',
    'https://www.bdfutbol.com/es/l/l55848.html',
    'https://www.bdfutbol.com/es/l/l967.html',
    'https://www.bdfutbol.com/es/l/l80303.html',
    'https://www.bdfutbol.com/es/l/l92318.html',
    'https://www.bdfutbol.com/es/l/l7497.html',
    'https://www.bdfutbol.com/es/l/l93616.html',
    'https://www.bdfutbol.com/es/l/l96572.html',
    'https://www.bdfutbol.com/es/l/l55205.html',
    'https://www.bdfutbol.com/es/l/l92917.html',
    'https://www.bdfutbol.com/es/l/l42979.html',
    'https://www.bdfutbol.com/es/l/l5598.html',
    'https://www.bdfutbol.com/es/l/l5092.html',
    'https://www.bdfutbol.com/es/l/l55673.html',
    'https://www.bdfutbol.com/es/l/l94699.html',
    'https://www.bdfutbol.com/es/l/l43289.html',
    'https://www.bdfutbol.com/es/l/l5650.html',
    'https://www.bdfutbol.com/es/l/l42360.html',
    'https://www.bdfutbol.com/es/l/l7476.html',
    'https://www.bdfutbol.com/es/l/l50215.html',
    'https://www.bdfutbol.com/es/l/l87412.html',
    'https://www.bdfutbol.com/es/l/l93592.html',
    'https://www.bdfutbol.com/es/l/l54907.html',
    'https://www.bdfutbol.com/es/l/l7862.html',
    'https://www.bdfutbol.com/es/l/l90160.html',
    'https://www.bdfutbol.com/es/l/l1837.html',
    'https://www.bdfutbol.com/es/l/l8444.html',
    'https://www.bdfutbol.com/es/l/l87048.html',
    'https://www.bdfutbol.com/es/l/l1969.html',
    'https://www.bdfutbol.com/es/l/l2650.html',
    'https://www.bdfutbol.com/es/l/l101664.html',
    'https://www.bdfutbol.com/es/l/l42261.html',
    'https://www.bdfutbol.com/es/l/l53797.html',
    'https://www.bdfutbol.com/es/l/l701793.html',
    'https://www.bdfutbol.com/es/l/l80275.html',
    'https://www.bdfutbol.com/es/l/l95067.html',
    'https://www.bdfutbol.com/es/l/l84419.html',
    'https://www.bdfutbol.com/es/l/l43469.html',
    'https://www.bdfutbol.com/es/l/l46238.html',
    'https://www.bdfutbol.com/es/l/l70530.html',
    'https://www.bdfutbol.com/es/l/l95008.html',
    'https://www.bdfutbol.com/es/l/l82969.html',
    'https://www.bdfutbol.com/es/l/l50794.html',
    'https://www.bdfutbol.com/es/l/l7419.html',
    'https://www.bdfutbol.com/es/l/l2026.html',
    'https://www.bdfutbol.com/es/l/l1098.html'
          ]

print(len(urls))

# Carga el archivo CSV en un DataFrame
df_entrenador = pd.read_csv('./data/entrenador.csv')

# Extrae los IDs de la columna idEntrenador
lista_ids_entrenador = df_entrenador['idEntrenador'].tolist()
lista_ids_entrenador.append('251')
lista_ids_entrenador.append('252') 

# Imprime o utiliza la lista según tus necesidades
print(lista_ids_entrenador)

resultados = []
headers = ['idEntrenador', 'Temporada', 'Equipo', 'Nun', 'Non', 'División', 'Edad', 'PJ', 'PG', 'PE', 'PP', 'Non']

for idx, url in enumerate(urls):
    # Realizar la solicitud GET y crear el objeto BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Buscar la tabla que corresponde a la clase "wikitable" y estilo "text-align:enter"
    tabla = soup.find('div', {'id': 'traj', 'class': 'scrtraj mt-2'})

    # Verificar si se encontró la tabla
    if tabla:
        # Obtener todas las filas y celdas de la tabla
        rows = tabla.find_all('tr')

        # Crear una lista para almacenar las filas de datos
        tabla_data = []

        # Recorrer cada fila y extraer el texto de las celdas
        for i, row in enumerate(rows[:-1]):
            if i == 0:
                continue
            cells = row.find_all(['td', 'th'])
            row_data = [lista_ids_entrenador[idx]] + [cell.get_text(strip=True).replace('⬤', '') for cell in cells]
            tabla_data.append(row_data)

        # Agregar los resultados a la lista general
        resultados.extend(tabla_data)
        #print(tabulate(tabla_data,  tablefmt='grid'))

    else:
        print('No se encontró la tabla')
        
if len(resultados) > 0:
    resultados.insert(0, headers)
    # Especificar el nombre del archivo CSV donde guardar la tabla
    file_name = './data/Trayectoria_entrenador.csv'
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(resultados)
    print(f'Se guardó la tabla en {file_name}')
else:
    print('La tabla no contiene datos.')


    