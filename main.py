import json
from get.entrenadores import EntrenadorExtractor
from get.equipo import EquipoExtractor
from get.jugador_17_18 import Jugadores2Extractor
from get.jugador import JugadoresExtractor
from get.partido import PartidoScraper
from get.Trayectoria_entrenador import TrayectoriaEntrenadorExtractor
from preparacion import *
from DeepLearning.dnn_1x2 import LoadData1x2, Model1x2, data_usuario, datos_usuario
from DeepLearning.dnn_goles import LoadDataGoles, GoalsPredictionModel
from DeepLearning.dnn_marcanambos import LoadData, ModelMarcanAmbos


def main():
    var = input("(A) Mete A para hacer la extracción de datos\n"
      "(B) Mete B para hacer la preparación de datos\n"
      "(C) Mete C para hacer las predicciones del resultado, los goles y si/no marcan ambos: ")

    if var == 'A':
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
        scraper = Jugadores2Extractor(temporadas)
        scraper.scrape_data()
        archivo_csv = 'data/jugador2.csv'
        scraper.save_to_csv(archivo_csv)
        scraper.close_driver()

        temporadas = ['1992-1993', '1993-1994', '1994-1995', '1995-1996', '1996-1997',
                    '1997-1998', '1998-1999', '1999-2000', '2000-2001', '2001-2002',
                    '2002-2003', '2003-2004', '2004-2005', '2005-2006', '2006-2007',
                    '2007-2008', '2008-2009', '2009-2010', '2010-2011', '2011-2012',
                    '2012-2013', '2013-2014', '2014-2015', '2015-2016', '2016-2017']
        
        scraper = JugadoresExtractor(temporadas)
        scraper.scrape_data()
        archivo_csv = 'data/jugador.csv'
        scraper.save_to_csv(archivo_csv)
        scraper.close_driver()

        temporadas = [
        '2023-2024', '2022-2023', '2021-2022', '2020-2021', '2019-2020',
        '2018-2019', '2017-2018', '2016-2017', '2015-2016', '2014-2015',
        '2013-2014', '2012-2013', '2011-2012', '2010-2011', '2009-2010',
        '2008-2009', '2007-2008', '2006-2007', '2005-2006', '2004-2005',
        '2003-2004']
        scraper = PartidoScraper()
        scraper.scrape_data(temporadas)
        scraper.guardar_datos_csv('data/partido.csv')
    
    if var=='B':
        urls = ['https://www.bdfutbol.com/es/l/l93816.html', 'https://www.bdfutbol.com/es/l/l93761.html', 'https://www.bdfutbol.com/es/l/l95279.html',
        'https://www.bdfutbol.com/es/l/l1566.html', 'https://www.bdfutbol.com/es/l/l99573.html', 'https://www.bdfutbol.com/es/l/l3685.html',
        'https://www.bdfutbol.com/es/l/l3787.html', 'https://www.bdfutbol.com/es/l/l92334.html', 'https://www.bdfutbol.com/es/l/l581.html',
        'https://www.bdfutbol.com/es/l/l97338.html', 'https://www.bdfutbol.com/es/l/l4204.html', 'https://www.bdfutbol.com/es/l/l90180.html',
        'https://www.bdfutbol.com/es/l/l41929.html', 'https://www.bdfutbol.com/es/l/l4094.html', 'https://www.bdfutbol.com/es/l/l92445.html',
        'https://www.bdfutbol.com/es/l/l95877.html', 'https://www.bdfutbol.com/es/l/l96259.html', 'https://www.bdfutbol.com/es/l/l41916.html',
        'https://www.bdfutbol.com/es/l/l2398.html', 'https://www.bdfutbol.com/es/l/l7360.html', 'https://www.bdfutbol.com/es/l/l7442.html',
        'https://www.bdfutbol.com/es/l/l3301.html', 'https://www.bdfutbol.com/es/l/l3059.html', 'https://www.bdfutbol.com/es/l/l44856.html',
        'https://www.bdfutbol.com/es/l/l94062.html', 'https://www.bdfutbol.com/es/l/l70062.html', 'https://www.bdfutbol.com/es/l/l93315.html',
        'https://www.bdfutbol.com/es/l/l95965.html', 'https://www.bdfutbol.com/es/l/l5057.html', 'https://www.bdfutbol.com/es/l/l93049.html',
        'https://www.bdfutbol.com/es/l/l50386.html', 'https://www.bdfutbol.com/es/l/l3658.html', 'https://www.bdfutbol.com/es/l/l93678.html',
        'https://www.bdfutbol.com/es/l/l47240.html', 'https://www.bdfutbol.com/es/l/l4363.html', 'https://www.bdfutbol.com/es/l/l7443.html',
        'https://www.bdfutbol.com/es/l/l2558.html', 'https://www.bdfutbol.com/es/l/l83077.html', 'https://www.bdfutbol.com/es/l/l2664.html',
        'https://www.bdfutbol.com/es/l/l80029.html', 'https://www.bdfutbol.com/es/l/l4130.html', 'https://www.bdfutbol.com/es/l/l95974.html',
        'https://www.bdfutbol.com/es/l/l4416.html', 'https://www.bdfutbol.com/es/l/l46822.html', 'https://www.bdfutbol.com/es/l/l93130.html',
        'https://www.bdfutbol.com/es/l/l566.html', 'https://www.bdfutbol.com/es/l/l78784.html', 'https://www.bdfutbol.com/es/l/l95034.html',
        'https://www.bdfutbol.com/es/l/l90120.html', 'https://www.bdfutbol.com/es/l/l1734.html', 'https://www.bdfutbol.com/es/l/l697.html',
        'https://www.bdfutbol.com/es/l/l1953.html', 'https://www.bdfutbol.com/es/l/l500180.html', 'https://www.bdfutbol.com/es/l/l92114.html',
        'https://www.bdfutbol.com/es/l/l26120.html', 'https://www.bdfutbol.com/es/l/l80000.html', 'https://www.bdfutbol.com/es/l/l20408.html',
        'https://www.bdfutbol.com/es/l/l3033.html', 'https://www.bdfutbol.com/es/l/l3686.html', 'https://www.bdfutbol.com/es/l/l95522.html',
        'https://www.bdfutbol.com/es/l/l79598.html', 'https://www.bdfutbol.com/es/l/l3179.html', 'https://www.bdfutbol.com/es/l/l46179.html',
        'https://www.bdfutbol.com/es/l/l7445.html', 'https://www.bdfutbol.com/es/l/l90210.html', 'https://www.bdfutbol.com/es/l/l1799.html',
        'https://www.bdfutbol.com/es/l/l51756.html', 'https://www.bdfutbol.com/es/l/l1695.html', 'https://www.bdfutbol.com/es/l/l57075.html',
        'https://www.bdfutbol.com/es/l/l92019.html', 'https://www.bdfutbol.com/es/l/l90927.html', 'https://www.bdfutbol.com/es/l/l95834.html',
        'https://www.bdfutbol.com/es/l/l5282.html', 'https://www.bdfutbol.com/es/l/l4080.html', 'https://www.bdfutbol.com/es/l/l90060.html',
        'https://www.bdfutbol.com/es/l/l45571.html', 'https://www.bdfutbol.com/es/l/l92394.html', 'https://www.bdfutbol.com/es/l/l96046.html',
        'https://www.bdfutbol.com/es/l/l45675.html', 'https://www.bdfutbol.com/es/l/l70079.html', 'https://www.bdfutbol.com/es/l/l92338.html',
        'https://www.bdfutbol.com/es/l/l7433.html', 'https://www.bdfutbol.com/es/l/l7439.html', 'https://www.bdfutbol.com/es/l/l93716.html',
        'https://www.bdfutbol.com/es/l/l49254.html', 'https://www.bdfutbol.com/es/l/l90240.html', 'https://www.bdfutbol.com/es/l/l93732.html',
        'https://www.bdfutbol.com/es/l/l701769.html', 'https://www.bdfutbol.com/es/l/l53333.html', 'https://www.bdfutbol.com/es/l/l45032.html',
        'https://www.bdfutbol.com/es/l/l50395.html', 'https://www.bdfutbol.com/es/l/l7441.html', 'https://www.bdfutbol.com/es/l/l42607.html',
        'https://www.bdfutbol.com/es/l/l95542.html', 'https://www.bdfutbol.com/es/l/l77396.html', 'https://www.bdfutbol.com/es/l/l92770.html',
        'https://www.bdfutbol.com/es/l/l93802.html', 'https://www.bdfutbol.com/es/l/l82124.html', 'https://www.bdfutbol.com/es/l/l2079.html',
        'https://www.bdfutbol.com/es/l/l43496.html', 'https://www.bdfutbol.com/es/l/l41782.html', 'https://www.bdfutbol.com/es/l/l7412.html',
        'https://www.bdfutbol.com/es/l/l80744.html', 'https://www.bdfutbol.com/es/l/l95994.html', 'https://www.bdfutbol.com/es/l/l50404.html',
        'https://www.bdfutbol.com/es/l/l901.html', 'https://www.bdfutbol.com/es/l/l98503.html', 'https://www.bdfutbol.com/es/l/l90519.html',
        'https://www.bdfutbol.com/es/l/l93619.html', 'https://www.bdfutbol.com/es/l/l91891.html', 'https://www.bdfutbol.com/es/l/l42540.html',
        'https://www.bdfutbol.com/es/l/l97100.html', 'https://www.bdfutbol.com/es/l/l700142.html', 'https://www.bdfutbol.com/es/l/l70156.html',
        'https://www.bdfutbol.com/es/l/l94848.html', 'https://www.bdfutbol.com/es/l/l59586.html', 'https://www.bdfutbol.com/es/l/l83850.html',
        'https://www.bdfutbol.com/es/l/l56797.html', 'https://www.bdfutbol.com/es/l/l72547.html', 'https://www.bdfutbol.com/es/l/l72173.html',
        'https://www.bdfutbol.com/es/l/l4103.html', 'https://www.bdfutbol.com/es/l/l45891.html', 'https://www.bdfutbol.com/es/l/l2921.html',
        'https://www.bdfutbol.com/es/l/l40026.html', 'https://www.bdfutbol.com/es/l/l99153.html', 'https://www.bdfutbol.com/es/l/l8440.html',
        'https://www.bdfutbol.com/es/l/l97203.html', 'https://www.bdfutbol.com/es/l/l5729.html', 'https://www.bdfutbol.com/es/l/l2198.html',
        'https://www.bdfutbol.com/es/l/l98959.html', 'https://www.bdfutbol.com/es/l/l90030.html', 'https://www.bdfutbol.com/es/l/l44657.html',
        'https://www.bdfutbol.com/es/l/l46986.html', 'https://www.bdfutbol.com/es/l/l48470.html', 'https://www.bdfutbol.com/es/l/l47452.html',
        'https://www.bdfutbol.com/es/l/l110525.html', 'https://www.bdfutbol.com/es/l/l96317.html', 'https://www.bdfutbol.com/es/l/l90000.html',
        'https://www.bdfutbol.com/es/l/l93829.html', 'https://www.bdfutbol.com/es/l/l98767.html', 'https://www.bdfutbol.com/es/l/l75630.html',
        'https://www.bdfutbol.com/es/l/l42718.html', 'https://www.bdfutbol.com/es/l/l89751.html', 'https://www.bdfutbol.com/es/l/l4230.html',
        'https://www.bdfutbol.com/es/l/l50943.html', 'https://www.bdfutbol.com/es/l/l70099.html', 'https://www.bdfutbol.com/es/l/l98404.html',
        'https://www.bdfutbol.com/es/l/l73107.html', 'https://www.bdfutbol.com/es/l/l8393.html', 'https://www.bdfutbol.com/es/l/l80460.html',
        'https://www.bdfutbol.com/es/l/l70864.html', 'https://www.bdfutbol.com/es/l/l99474.html', 'https://www.bdfutbol.com/es/l/l43576.html',
        'https://www.bdfutbol.com/es/l/l1925.html', 'https://www.bdfutbol.com/es/l/l3039.html', 'https://www.bdfutbol.com/es/l/l94144.html',
        'https://www.bdfutbol.com/es/l/l40838.html', 'https://www.bdfutbol.com/es/l/l78087.html', 'https://www.bdfutbol.com/es/l/l94597.html',
        'https://www.bdfutbol.com/es/l/l86247.html', 'https://www.bdfutbol.com/es/l/l44089.html', 'https://www.bdfutbol.com/es/l/l692.html',
        'https://www.bdfutbol.com/es/l/l79790.html', 'https://www.bdfutbol.com/es/l/l52447.html', 'https://www.bdfutbol.com/es/l/l96313.html',
        'https://www.bdfutbol.com/es/l/l95083.html', 'https://www.bdfutbol.com/es/l/l45492.html', 'https://www.bdfutbol.com/es/l/l5121.html',
        'https://www.bdfutbol.com/es/l/l2518.html', 'https://www.bdfutbol.com/es/l/l84336.html', 'https://www.bdfutbol.com/es/l/l2247.html',
        'https://www.bdfutbol.com/es/l/l73895.html', 'https://www.bdfutbol.com/es/l/l96253.html', 'https://www.bdfutbol.com/es/l/l43308.html',
        'https://www.bdfutbol.com/es/l/l29715.html', 'https://www.bdfutbol.com/es/l/l82962.html', 'https://www.bdfutbol.com/es/l/l84614.html',
        'https://www.bdfutbol.com/es/l/l80231.html', 'https://www.bdfutbol.com/es/l/l3936.html', 'https://www.bdfutbol.com/es/l/l2818.html',
        'https://www.bdfutbol.com/es/l/l79265.html', 'https://www.bdfutbol.com/es/l/l71268.html', 'https://www.bdfutbol.com/es/l/l70999.html',
        'https://www.bdfutbol.com/es/l/l57796.html', 'https://www.bdfutbol.com/es/l/l702156.html', 'https://www.bdfutbol.com/es/l/l93677.html',
        'https://www.bdfutbol.com/es/l/l98475.html', 'https://www.bdfutbol.com/es/l/l51865.html', 'https://www.bdfutbol.com/es/l/l42845.html',
        'https://www.bdfutbol.com/es/l/l50985.html', 'https://www.bdfutbol.com/es/l/l47134.html', 'https://www.bdfutbol.com/es/l/l7447.html',
        'https://www.bdfutbol.com/es/l/l43595.html', 'https://www.bdfutbol.com/es/l/l25665.html', 'https://www.bdfutbol.com/es/l/l702035.html',
        'https://www.bdfutbol.com/es/l/l93755.html', 'https://www.bdfutbol.com/es/l/l316.html', 'https://www.bdfutbol.com/es/l/l93602.html',
        'https://www.bdfutbol.com/es/l/l48813.html', 'https://www.bdfutbol.com/es/l/l71771.html', 'https://www.bdfutbol.com/es/l/l80413.html',
        'https://www.bdfutbol.com/es/l/l2096.html', 'https://www.bdfutbol.com/es/l/l4184.html', 'https://www.bdfutbol.com/es/l/l90145.html',
        'https://www.bdfutbol.com/es/l/l54215.html', 'https://www.bdfutbol.com/es/l/l52818.html', 'https://www.bdfutbol.com/es/l/l613.html',
        'https://www.bdfutbol.com/es/l/l55848.html', 'https://www.bdfutbol.com/es/l/l967.html', 'https://www.bdfutbol.com/es/l/l80303.html',
        'https://www.bdfutbol.com/es/l/l92318.html', 'https://www.bdfutbol.com/es/l/l7497.html', 'https://www.bdfutbol.com/es/l/l93616.html',
        'https://www.bdfutbol.com/es/l/l96572.html', 'https://www.bdfutbol.com/es/l/l55205.html', 'https://www.bdfutbol.com/es/l/l92917.html',
        'https://www.bdfutbol.com/es/l/l42979.html', 'https://www.bdfutbol.com/es/l/l5598.html', 'https://www.bdfutbol.com/es/l/l5092.html',
        'https://www.bdfutbol.com/es/l/l55673.html', 'https://www.bdfutbol.com/es/l/l94699.html', 'https://www.bdfutbol.com/es/l/l43289.html',
        'https://www.bdfutbol.com/es/l/l5650.html', 'https://www.bdfutbol.com/es/l/l42360.html', 'https://www.bdfutbol.com/es/l/l7476.html',
        'https://www.bdfutbol.com/es/l/l50215.html', 'https://www.bdfutbol.com/es/l/l87412.html', 'https://www.bdfutbol.com/es/l/l93592.html',
        'https://www.bdfutbol.com/es/l/l54907.html', 'https://www.bdfutbol.com/es/l/l7862.html', 'https://www.bdfutbol.com/es/l/l90160.html',
        'https://www.bdfutbol.com/es/l/l1837.html', 'https://www.bdfutbol.com/es/l/l8444.html', 'https://www.bdfutbol.com/es/l/l87048.html',
        'https://www.bdfutbol.com/es/l/l1969.html', 'https://www.bdfutbol.com/es/l/l2650.html', 'https://www.bdfutbol.com/es/l/l101664.html',
        'https://www.bdfutbol.com/es/l/l42261.html', 'https://www.bdfutbol.com/es/l/l53797.html', 'https://www.bdfutbol.com/es/l/l701793.html',
        'https://www.bdfutbol.com/es/l/l80275.html', 'https://www.bdfutbol.com/es/l/l95067.html', 'https://www.bdfutbol.com/es/l/l84419.html',
        'https://www.bdfutbol.com/es/l/l43469.html', 'https://www.bdfutbol.com/es/l/l46238.html', 'https://www.bdfutbol.com/es/l/l70530.html',
        'https://www.bdfutbol.com/es/l/l95008.html', 'https://www.bdfutbol.com/es/l/l82969.html', 'https://www.bdfutbol.com/es/l/l50794.html',
        'https://www.bdfutbol.com/es/l/l7419.html', 'https://www.bdfutbol.com/es/l/l2026.html', 'https://www.bdfutbol.com/es/l/l1098.html'
            ]
    
        trayectoria = TrayectoriaEntrenadorExtractor(urls, 'data/Trayectoria_entrenador.csv')
        trayectoria.cargar_ids_entrenador('data/entrenador.csv') 
        trayectoria.extraer_datos()
        trayectoria.guardar_csv()


        # Crear instancia de Entrenador
        entrenador = Entrenador('data/entrenador.csv')
        diccionario_entrenadores = entrenador.diccionario_entrenadores()  #guardar
        df_entrenador = entrenador.procesar()  #guardar

        # Crear instancia de Equipo
        df_equipo = Equipo('data/equipo.csv')
        diccionario_equipos = df_equipo.diccionario_equipos()  #guardar 
        print(diccionario_equipos)
        guardar_diccionario(diccionario_equipos, 'dataframe/id_equipo.json')
        df_equipo = df_equipo.procesar()  #guardar

        # Crear instancia de TrayectoriaEntrenador
        df_trayectoria_entrenador = TrayectoriaEntrenador('data/trayectoria_entrenador.csv')
        df_trayectoria_entrenador.procesar()
        df_trayectoria_entrenador.id_equipo(diccionario_equipos)
        df_trayectoria_entrenador = df_trayectoria_entrenador.procesar2()   #guardar

        # Crear instancia de Partido
        df_partido = Partido('data/partido.csv')
        df_partido.procesar1()
        df_partido.procesar_diccionario_equipos(diccionario_equipos)
        df_partido = df_partido.procesar2()

        # Crear instancia de Jugador
        df_jugadores = Jugador('data/jugador.csv', 'data/jugador2.csv')
        df_jugadores.un_data()
        df_jugadores.procesar()
        df_jugadores.id_jugador()
        # Obtener el diccionario de IDs de los jugadores
        diccionario_ids_jugadores = df_jugadores.asignar_ids('Jugador')  #guardar

        df_jugadores.id_equipo(diccionario_equipos)
        df_jugadores.procesar2()
        df_jugadores.procesar3()
        df_jugadores = df_jugadores.valoracion()  #guardar
        

        # Crear instancia de Champions
        df_champions = Champions(df_partido, df_jugadores)
        df_champions.goles()
        df_champions.aplicar_porcentaje_victorias_local()
        df_champions.aplicar_porcentaje_empate()
        df_champions.aplicar_porcentaje_victoria_visitante()
        df_champions.aplicar_porcentaje_equipo1_ganado()
        df_champions.aplicar_porcentaje_equipo2_ganado()
        df_champions.aplicar_porcentaje_equipo1_ganado_temporada()
        df_champions.aplicar_equipo1_ganado_temporada_local()
        df_champions.aplicar_equipo1_empatado_temporada_local()
        df_champions.aplicar_equipo1_perdido_temporada_local()
        df_champions.aplicar_media_ganado()
        df_champions.aplicar_media_goles_equipo1()
        df_champions.valoracion_jugadores()
        df_champions.valoracion_media_jugadores()
        df_champions.aplicar_porcentaje_equipo2_ganado_temporada()
        df_champions.aplicar_equipo2_ganado_temporada_local()
        df_champions.aplicar_equipo2_empatado_temporada_local()
        df_champions.aplicar_equipo2_perdido_temporada_local()
        df_champions.aplicar_media_ganado2()
        df_champions.aplicar_media_goles_equipo2()
        df_champions.valor_jugadores_equipo2()
        df_champions.valoracion_media_jugadores2()
        champions, champions_23_24 = df_champions.procesar()   #guardar los dos

        guardar_diccionario(diccionario_entrenadores, 'dataframe/id_entrenador.json')
        guardar_diccionario(diccionario_ids_jugadores, 'dataframe/id_jugador.json')

        guardar_data('dataframe/df_entrenador.csv', df_entrenador)
        guardar_data('dataframe/df_equipo.csv', df_equipo)
        guardar_data('dataframe/champions.csv', champions)
        guardar_data('dataframe/champions_23_24.csv', champions_23_24)
        guardar_data('dataframe/df_jugadores.csv', df_jugadores)
        guardar_data('dataframe/df_entrenador_trayectoria.csv', df_trayectoria_entrenador)

    if var == 'C':
        configurations = [
            {'units': 64, 'filters': 32, 'kernel_size': 3, 'learning_rate': 0.001, 'batch_size': 32, 'epochs': 10, 'dropout': 0.2},
            {'units': 128, 'filters': 64, 'kernel_size': 3, 'learning_rate': 0.01, 'batch_size': 64, 'epochs': 15, 'dropout': 0.1},
            {'units': 256, 'filters': 128, 'kernel_size': 5, 'learning_rate': 0.0001, 'batch_size': 16, 'epochs': 10, 'dropout': 0.3},
            {'units': 128, 'filters': 64, 'kernel_size': 5, 'learning_rate': 0.001, 'batch_size': 32, 'epochs': 15, 'dropout': 0.2},
            {'units': 256, 'filters': 128, 'kernel_size': 3, 'learning_rate': 0.0005, 'batch_size': 32, 'epochs': 10, 'dropout': 0.1},
            {'units': 64, 'filters': 32, 'kernel_size': 5, 'learning_rate': 0.001, 'batch_size': 64, 'epochs': 10, 'dropout': 0.1},
            {'units': 128, 'filters': 64, 'kernel_size': 3, 'learning_rate': 0.001, 'batch_size': 32, 'epochs': 20, 'dropout': 0.2},
            {'units': 256, 'filters': 128, 'kernel_size': 5, 'learning_rate': 0.0005, 'batch_size': 32, 'epochs': 15, 'dropout': 0.2},
            {'units': 64, 'filters': 32, 'kernel_size': 3, 'learning_rate': 0.001, 'batch_size': 64, 'epochs': 20, 'dropout': 0.3},
            {'units': 128, 'filters': 64, 'kernel_size': 5, 'learning_rate': 0.001, 'batch_size': 32, 'epochs': 10, 'dropout': 0.2},
            {'units': 256, 'filters': 128, 'kernel_size': 3, 'learning_rate': 0.001, 'batch_size': 16, 'epochs': 15, 'dropout': 0.1},
            {'units': 64, 'filters': 32, 'kernel_size': 3, 'learning_rate': 0.01, 'batch_size': 64, 'epochs': 10, 'dropout': 0.1},
            {'units': 128, 'filters': 64, 'kernel_size': 5, 'learning_rate': 0.001, 'batch_size': 32, 'epochs': 10, 'dropout': 0.1}
        ]
        
        # Load Data
        data_loader = LoadData1x2('/Users/carlotasanchezgonzalez/Documents/class/Champions_23-24/dataframe/champions.csv')
        data = data_loader.load_data()
        X_train, X_test, y_train, y_test, scaler, X, y = data_loader.prepare_data(data)

        df = data_usuario('dataframe/champions_23_24.csv', 'dataframe/champions.csv')

        model = Model1x2()
        model.train_or_load_model(configurations, X_train, y_train, X_test, y_test, 'modelos/dnn_1x2.keras')

        # Cargar el archivo JSON que contiene los nombres de los equipos y sus IDs
        with open('dataframe/id_equipo.json') as f:
            equipos_dict = json.load(f)

        equipos_dict_invertido = {v: k for k, v in equipos_dict.items()}

        # Obtener los equipos únicos de la columna 'Local' de tu DataFrame
        equipos_disponibles = df['Local'].unique()
        equipos_disponibles = np.sort(equipos_disponibles)

        # Imprimir los nombres de los equipos únicos junto con sus IDs correspondientes
        print("Equipos disponibles para enfrentar:")
        for equipo_id in equipos_disponibles:
            equipo_nombre = equipos_dict_invertido.get(equipo_id)
            if equipo_nombre is not None:
                print(f"{equipo_nombre}, {equipo_id}")


        equipo_local = int(input("Ingrese el ID del equipo local: "))
        equipo_visitante = int(input("Ingrese el ID del equipo visitante: "))

        nombre_equipo_local = equipos_dict_invertido.get(equipo_local)
        nombre_equipo_visitante = equipos_dict_invertido.get(equipo_visitante)

        nuevo_dataframe = datos_usuario(df, equipo_local, equipo_visitante)

        X_prediccion = scaler.transform(nuevo_dataframe)


        class_probabilities_prediccion = model.predict(X_prediccion)

        print(f"Probabilidades de clase predichas para el partido {nombre_equipo_local} VS. {nombre_equipo_visitante}:")
        for i, prob in enumerate(class_probabilities_prediccion[0]):
            print(f"{y.columns[i]}: {prob*100:.3f}%")



        #------------------ Goles ------------------

        # Cargar los datos
        data_loader = LoadDataGoles('dataframe/champions.csv')
        data_goles = data_loader.load_data()
        X_train, X_test, y_train, y_test, scaler, X, y = data_loader.prepare_data(data_goles)

        
        model2 = GoalsPredictionModel()
        model2.train_or_load_model(configurations, X_train, y_train, X_test, y_test, 'modelos/modelo_dnn_goals.keras')
        class_probabilities_prediccion_goals = model2.predict(X_prediccion)

        print(f"Goles {nombre_equipo_local}:", class_probabilities_prediccion_goals[0])
        print(f"Goles {nombre_equipo_visitante}:", class_probabilities_prediccion_goals[1])



        #------------------ Marcan Ambos ------------------

        # Cargar los datos
        data_loader = LoadData('/Users/carlotasanchezgonzalez/Documents/class/Champions_23-24/dataframe/champions.csv')
        data = data_loader.load_data()
        X_train, X_test, y_train, y_test, scaler, X, y = data_loader.prepare_data(data)

        model3 = ModelMarcanAmbos()
        model3.train_or_load_model(configurations, X_train, y_train, X_test, y_test, 'modelos/dnn_ambos_marcan.keras')
        class_probabilities_prediccion_marcan = model3.predict(X_prediccion)

        for i, pred in enumerate(class_probabilities_prediccion_marcan):
            if pred == 1:
                print("Ambos equipos marcan")
            else:
                print("No marcan ambos")