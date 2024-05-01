import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import json



#Entrenador.csv

class Entrenador:
    def __init__(self, ruta):
        self.df = pd.read_csv(ruta)
    
    def diccionario_entrenadores(self):
        diccionario_entrenadores = self.df.set_index('Apodo')['idEntrenador'].to_dict()
        return diccionario_entrenadores
    
    def procesar(self):
        self.df.drop(['Pais'], axis=1, inplace=True)
        self.df.head(10)
        return self.df





#----------------------------------------------------------------------------------------------------------------------------
#Equipo.csv

class Equipo:
    def __init__(self, ruta):
        self.df = pd.read_csv(ruta)
    
    def diccionario_equipos(self):
        diccionario_equipos = self.df.set_index('Nombre')['idEquipo'].to_dict()
        return diccionario_equipos
    
    def procesar(self):
        self.df = self.df.drop(['Escudo'], axis=1)
        return self.df
    



#----------------------------------------------------------------------------------------------------------------------------
#Partido.csv

# - Eliminar filas duplicadas
# - Añadir id por partido
# - Eliminar columnas que no nos sirven
# - Añadir id en local y visitante en vez de el nombre del equipo
# - Añadir columnas bool victoria local, victoria visitante, empate
from difflib import get_close_matches

class Partido:
    def __init__(self, ruta):
        self.df = pd.read_csv(ruta)
    
    def procesar1(self):
        self.df = self.df[self.df['Local'] != 'Home']
        self.df.reset_index(drop=True, inplace=True)
        self.df = self.df.drop_duplicates()
        columnas_a_eliminar = ['Wk', 'Dia', 'Fecha', 'Hora', 'Reporte', 'Notas', 'Público', 'Arbitro']
        self.df = self.df.drop(columns=columnas_a_eliminar)
        return self.df
    
    def procesar_diccionario_equipos(self, diccionario_equipos):
        claves_cambiadas = {'Borussia Dortmund': 'Dortmund', 'Deportivo de La Coruña': 'La Coruña', 'København': 'FC Copenhagen',
                    'Sporting de Portugal': 'Sporting CP', 'Olympique de Marseille': 'Marseille', 'Olympique Lyonnais': 'Lyon',
                    'Bayern München': 'Bayern Munich', 'Bayer Leverkusen': 'Leverkusen', 'Brugge': 'Club Brugge',
                    'Red Bull Salzburg': 'RB Salzburg', 'PSG': 'Paris S-G', 'Lokomotiv Moskva': 'Loko Moscow',
                    'Borussia Mönchengladbach': "M'Gladbach", 'Slavia Praha': 'Slavia Prague', 'Crvena Zvezda': 'Red Star',
                    'PSV': 'PSV Eindhoven', 'AEK': 'AEK Athens', 'CSKA Moskva': 'CSKA Moscow', 'Qarabağ': 'Qarabağ FK',
                    'Spartak Moskva': 'Spartak Moscow', 'APOEL': 'APOEL FC', 'Maribor': 'NK Maribor', 'Leicester': 'Leicester City',
                    'Astana': 'FC Astana', 'FCSB': 'Steaua', 'Cluj': 'CFR Cluj', 'Žilina': 'MŠK Žilina',
                    'Girondins de Bordeaux': 'Bordeaux', 'Hamburger': 'Hamburger SV', 'Sparta Praha': 'Sparta Prague',
                    'Petržalka': 'Artmedia', 'Manchester United': 'Manchester Utd', 'Shakhtar Donetsk': 'Shakhtar', 'B68': 'B68 Toftir',
                    'Royal Antwerp': 'Antwerp', 'Newcastle':'Newcastle Utd'}

        for clave_antigua, clave_nueva in claves_cambiadas.items():
            if clave_antigua in diccionario_equipos:
                diccionario_equipos[clave_nueva] = diccionario_equipos.pop(clave_antigua)

        def obtener_id_equipo(nombre_equipo):
            # Buscar coincidencia exacta
            if nombre_equipo in diccionario_equipos:
                return diccionario_equipos[nombre_equipo]
            
            # Buscar coincidencias cercanas
            matches = get_close_matches(nombre_equipo, diccionario_equipos.keys(), n=1, cutoff=0.8)
            if matches:
                return diccionario_equipos[matches[0]]
            
            # Si no hay coincidencia, devolver el nombre original
            return nombre_equipo

        self.df['Local'] = self.df['Local'].astype(str)
        self.df['Visitante'] = self.df['Visitante'].astype(str)

        # Aplicar la función a las columnas 'Local' y 'Visitante'
        self.df['Local'] = self.df['Local'].apply(obtener_id_equipo)
        self.df['Visitante'] = self.df['Visitante'].apply(obtener_id_equipo)

        return self.df

    def procesar2(self):                
        #Eliminar filas que se guardaron como nulas
        print("Cantidad de filas con valores NaN:", self.df['Ronda'].isnull().sum())
        self.df = self.df.dropna(subset=['Ronda'])
        self.df = self.df.reset_index(drop=True)

        # Añadir una nueva columna 'idPartido' con valores únicos
        self.df['idPartido'] = range(1, len(self.df) + 1)

        # Reorganizar las columnas para que 'idPartido' sea la primera
        self.df = self.df[['idPartido'] + [col for col in self.df.columns if col != 'idPartido']]

        num_filas_nan = self.df['Resultado'].isna().sum()
        print("Número de filas con valores NaN en la columna 'Resultado':", num_filas_nan)

        #Los valores nulos de los futuros partidos que se van a jugar voy a reemplazarlos por '0-0'
        self.df['Resultado'] = self.df['Resultado'].fillna('0–0')

        #Goles de local y visitante en diferentes columnas
        self.df[['GolesLocal','GolesVisitante']] = self.df['Resultado'].str.split('–',expand=True)
        self.df = self.df.drop(columns=['Resultado'])


        #Columnas booleanas para saber si el equipo local o visitante ganó, empató o perdió
        self.df['VictoriaLocal'] = (self.df['GolesLocal'] > self.df['GolesVisitante']).astype(int)
        self.df['Empate'] = (self.df['GolesLocal'] == self.df['GolesVisitante']).astype(int)
        self.df['VictoriaVisitante'] = (self.df['GolesLocal'] < self.df['GolesVisitante']).astype(int)

        return self.df
    




#----------------------------------------------------------------------------------------------------------------------------
#Trayectoria_entrenador.csv

# - IdEquipo en vez de el nombre
# - Eliminar columnas que no nos sirven

class TrayectoriaEntrenador:
    def __init__(self, ruta):
        self.df = pd.read_csv(ruta)
    
    def procesar(self):
        columns_to_drop = ['Nun', 'Non', 'Non.1', 'División', 'Edad']
        self.df = self.df.drop(columns=columns_to_drop)
        self.df.replace('-', pd.NA, inplace=True)
        self.df = self.df.dropna()
        self.df = self.df.reset_index(drop=True)

        return self.df
    
    def id_equipo(self, dic_equipos_original):
        #Cambiar a id del equipo
        def id_equipo(equipo):
            equipo_lower = equipo.lower()  # Convertir a minúsculas para comparación insensible a mayúsculas y minúsculas
            
            if equipo_lower in dic_equipos_original:
                return dic_equipos_original[equipo_lower]

            # Buscar coincidencias cercanas
            matches = get_close_matches(equipo_lower, dic_equipos_original.keys(), n=1, cutoff=0.8)
            if matches:
                return dic_equipos_original[matches[0]]
            
            # Si no hay coincidencia, devolver el nombre original
            return 0

        # Aplicar la función a la columna 'Equipo' de tu DataFrame
        self.df['Equipo'] = self.df['Equipo'].astype(str)
        self.df['Equipo'] = self.df['Equipo'].apply(id_equipo)
        
        return self.df

    def procesar2(self):
        self.df['PJ'] = pd.to_numeric(self.df['PJ'])
        self.df['PG'] = pd.to_numeric(self.df['PG'])
        self.df['PE'] = pd.to_numeric(self.df['PE'])
        self.df['PP'] = pd.to_numeric(self.df['PP'])
        
        return self.df






#----------------------------------------------------------------------------------------------------------------------------
#Jugador.csv

# - Juntar las dos tablas
# - Eliminar columnas no necesarias
# - Cambiar idEquipo y poner idJugadores teniendo en cuenta que algunos se repiten
# - Añadir columna valoracion de jugadores y calcularla con valores estadísticos

class Jugador:
    def __init__(self, ruta1, ruta2):
        self.df1 = pd.read_csv(ruta1)
        self.df2 = pd.read_csv(ruta2)
        self.df = None

    def un_data(self):
        self.df = pd.concat([self.df1, self.df2], ignore_index=True)
        return self.df
    
    def procesar(self):
        #Eliminar columnas que no necesito
        colum_eliminar = ['País', 'Posc', '#', 'Nacimiento', '90 s', 'G+A', 'G-TP', 'Gls.90', 'Ast90', 'G+A90', 'G-TP90',
            'G+A-TP90', 'Partidos', 'xG90', 'xAG90', 'xG+xAG90', 'npxG90', 'npxG+xAG90', 'Gls90.', 'xAG', 'npxG+xAG']

        self.df = self.df.drop(columns=colum_eliminar)

        #Eliminar filas que se me han guardado de los encabezados
        self.df = self.df[self.df['Equipo'] != 'Equipo']
        self.df.reset_index(drop=True, inplace=True)

        return self.df

    def asignar_ids(self, columna_jugador):
        # Obtener la lista única de jugadores
        jugadores_unicos = self.df[columna_jugador].unique()

        # Inicializar un diccionario para almacenar los IDs
        jugadores_id = {}

        # Asignar un ID único a cada jugador
        for idx, jugador in enumerate(jugadores_unicos):
            jugadores_id[jugador] = idx + 1  # Sumar 1 para comenzar los IDs desde 1

        return jugadores_id

    def id_jugador(self):
        # Asignar IDs a los jugadores
        diccionario_ids = self.asignar_ids('Jugador')

        # Crear una nueva columna 'idJugador' en el DataFrame
        self.df['idJugador'] = self.df['Jugador'].map(diccionario_ids)

        # Reordenar las columnas
        columnas_ordenadas = ['Temporada', 'idJugador', 'Jugador'] + [col for col in self.df.columns if col not in ['Temporada', 'idJugador', 'Jugador']]
        self.df = self.df[columnas_ordenadas]

        return self.df
    
    def id_equipo(self, diccionario_equipos):
        claves_cambiadas = {'Dinamo Zagreb': 'Croatia Zagreb','PSV': 'PSV Eindhoven', 'Shakhtar Donetsk': 'Shakhtar',
                    'Linfield': 'Linfield FC', 'Cork City': 'Cork City FC', 'Budapest Honvéd': 'Honvéd',
                    'AIK Solna': 'AIK Stockholm', 'Blackburn Rovers': 'Blackburn', 'Newcastle': 'Newcastle Utd',
                    'Hertha Berliner': 'Hertha BSC', 'Royal Antwerp': 'Antwerp', 'Glentoran': 'Glentoran FC',
                    'Leeds': 'Leeds United', 'Skonto': 'Skonto FC', 'Tavriya': 'Tavriya Simferopol'}

        for clave_antigua, clave_nueva in claves_cambiadas.items():
            if clave_antigua in diccionario_equipos:
                diccionario_equipos[clave_nueva] = diccionario_equipos.pop(clave_antigua)

        def obtener_id_equipo(nombre_equipo):
            # Buscar coincidencia exacta
            if nombre_equipo in diccionario_equipos:
                return diccionario_equipos[nombre_equipo]
            
            # Buscar coincidencias cercanas
            matches = get_close_matches(nombre_equipo, diccionario_equipos.keys(), n=1, cutoff=0.8)
            if matches:
                return diccionario_equipos[matches[0]]
            
            # Si no hay coincidencia, devolver el nombre original
            return nombre_equipo

        self.df['Equipo'] = self.df['Equipo'].astype(str)
        self.df['Equipo'] = self.df['Equipo'].apply(obtener_id_equipo)
        self.df['Equipo'].replace({'nlPSV': '21'}, inplace=True)
        self.df['Equipo'].replace({'hrDinamo Zagreb': '235'}, inplace=True)
        self.df['Equipo'].replace({'uaShakhtar Donetsk': '92'}, inplace=True)


        #Elimino las filas que no tengan los equipos id asignados, nos dan igual
        condicion = ~self.df['Equipo'].isin(['fiLahti', 'isKV', 'isÍþróttabandalag Akraness', 'mtFloriana FC', 'atAustria Salzburg'])
        self.df = self.df[condicion]
        self.df.reset_index(drop=True, inplace=True)

        return self.df
    
    def procesar2(self):
        # Definir las columnas a convertir a tipo numérico
        columnas_numericas = ['Edad', 'PJ', 'Titular', 'Mín', 'Gls.', 'Ass', 'TP', 'TPint', 'TA', 'TR', 'xG', 'npxG', 'PrgC', 'PrgP', 'PrgR', 'Equipo']

        # Convertir las columnas a tipo numérico, tratando los errores como NaN
        self.df[columnas_numericas] = self.df[columnas_numericas].apply(pd.to_numeric, errors='coerce')

        # Supongamos que tu DataFrame se llama df
        columnas_categoricas = ['Jugador']

        # Convierte las columnas categóricas al tipo de dato category
        self.df[columnas_categoricas] = self.df[columnas_categoricas].astype('category')


        # Reemplazar NaN en la columna 'Ass' con 0
        self.df['Ass'] = self.df['Ass'].fillna(0)

        # Reemplazar NaN en la columna 'TPint' con 0
        self.df['TP'] = self.df['TP'].fillna(0)

        # Reemplazar NaN en la columna 'TPint' con 0
        self.df['TPint'] = self.df['TPint'].fillna(0)

        self.df['Mín'].fillna(self.df['PJ'] * 90, inplace=True)

        # Lista de columnas a las que quieres aplicar el reemplazo de NaN con la media
        columnas_a_reemplazar = ['xG', 'npxG', 'PrgC', 'PrgP', 'PrgR', 'Edad']

        for columna in columnas_a_reemplazar:
            media_columna = self.df[columna].mean()
            self.df[columna] = self.df[columna].fillna(media_columna)

        return self.df
    
    def valoracion(self):
        # Asigna pesos a cada métrica
        pesos = {'Mín': 0.05,
                'PJ': 0.15,
                'Gls.': 0.40,
                'Ass': 0.2,
                'TR': -0.15,
                'PrgP': 0.15,
                'PrgR': 0.15}

        # Calcula la valoración para cada jugador
        self.df['V'] = (self.df['Mín'] * pesos['Mín'] +
                                    self.df['PJ'] * pesos['PJ'] +
                                    self.df['Gls.'] * pesos['Gls.'] +
                                    self.df['Ass'] * pesos['Ass'] +
                                    self.df['TR'] * pesos['TR'] +
                                    self.df['PrgP'] * pesos['PrgP'] +
                                    self.df['PrgR'] * pesos['PrgR'])

        # Normaliza la valoración a un rango 0 a 100
        max_valoracion = self.df['V'].max()
        min_valoracion = self.df['V'].min()
        self.df['Valoracion'] = 100 * (self.df['V'] - min_valoracion) / (max_valoracion - min_valoracion)
        self.df.drop(columns=['V'], inplace=True)

        return self.df
    
    def procesar3(self):
        # Dividir la columna Temporada en dos columnas separadas de año inicial y año final
        self.df[['Año Inicial', 'Año Final']] = self.df['Temporada'].str.split('-', expand=True)

        # Convertir las columnas de año inicial y año final a tipo entero
        self.df['Año Inicial'] = self.df['Año Inicial'].astype(int)
        self.df['Año Final'] = self.df['Año Final'].astype(int)

        # Calcular el año medio entre el año inicial y el año final
        self.df['Temporada'] = self.df[['Año Inicial', 'Año Final']].mean(axis=1)

        # Convertir la temporada a tipo datetime
        self.df['Temporada'] = pd.to_datetime(self.df['Temporada'], format='%Y')

        # Eliminar las columnas de año inicial y año final si es necesario
        del self.df['Año Inicial']
        del self.df['Año Final']

        return self.df
    





#----------------------------------------------------------------------------------------------------------------------------

#Champions.csv

# Crear un data recopilación de la inforamción de nuestors datas partido de la tabla partidos.csv


import re

class Champions:
    def __init__(self, df1, df2):
        self.df1 = df1
        self.df2 = df2
    
    def goles(self):
        # Patrones a buscar y reemplazar
        patrones_reemplazo = {
            r'\((\d+)\)(\d+)': r'\2',  # (n)k => k
            r'(\d+)\((\d+)\)': r'\1'   # k(n) => k
        }

        # Aplicar reemplazo en la columna 'GolesLocal'
        for patron, reemplazo in patrones_reemplazo.items():
            self.df1['GolesLocal'] = self.df1['GolesLocal'].replace(to_replace=patron, value=reemplazo, regex=True)

        # Aplicar reemplazo en la columna 'GolesVisitante'
        for patron, reemplazo in patrones_reemplazo.items():
            self.df1['GolesVisitante'] = self.df1['GolesVisitante'].replace(to_replace=patron, value=reemplazo, regex=True)


        # Convertir columnas de goles a tipo int
        self.df1['GolesLocal'] = self.df1['GolesLocal'].astype(int)
        self.df1['GolesVisitante'] = self.df1['GolesVisitante'].astype(int)

        # Convertir columnas de evento
        self.df1['Evento'] = self.df1['Evento'].astype(str)

        # Convertir columnas de local y visitante a tipo int
        self.df1['Local'] = self.df1['Local'].astype(int)
        self.df1['Visitante'] = self.df1['Visitante'].astype(int)

        # Convertir columna de temporada a tipo string
        self.df1['Temporada'] = self.df1['Temporada'].astype(str)

        # Convertir columna de ronda a tipo string
        self.df1['Ronda'] = self.df1['Ronda'].astype(str)

        return self.df1
    

    #Estadísticas de los dos equipos habiendo jugado entre ellos
    def calcular_porcentaje_victorias_local(self, row):
        # Obtener los equipos de la fila actual
        equipo_local = row['Local']
        equipo_visitante = row['Visitante']

        # Excluir la fila actual del DataFrame
        df_sin_fila_actual = self.df1.drop(row.name)
        
        # Filtrar filas donde aparezcan estos dos equipos, independientemente del orden
        rows_con_equipos = df_sin_fila_actual[((df_sin_fila_actual['Local'] == equipo_local) & (df_sin_fila_actual['Visitante'] == equipo_visitante)) |
                                            ((df_sin_fila_actual['Local'] == equipo_visitante) & (df_sin_fila_actual['Visitante'] == equipo_local))]
        
        # Contar las filas donde la victoria es local
        victorias_local = rows_con_equipos['VictoriaLocal'].sum()
        
        # Calcular el porcentaje de victorias locales
        total_partidos = len(rows_con_equipos)
        if total_partidos != 0:
            porcentaje_victorias_local = (victorias_local / total_partidos) * 100
        else:
            porcentaje_victorias_local = 0
        
        return porcentaje_victorias_local

    def aplicar_porcentaje_victorias_local(self):
        # Aplicar la función a cada fila y crear la nueva columna
        self.df1['%_Victorias_Local'] = self.df1.apply(self.calcular_porcentaje_victorias_local, axis=1).round(2)

        return self.df1
    
    def calcular_porcentaje_empate(self, row):
        equipo_local = row['Local']
        equipo_visitante = row['Visitante']

        # Excluir la fila actual del DataFrame
        df_sin_fila_actual = self.df1.drop(row.name)
        
        # Filtrar filas donde aparezcan estos dos equipos, independientemente del orden
        rows_con_equipos = df_sin_fila_actual[((df_sin_fila_actual['Local'] == equipo_local) & (df_sin_fila_actual['Visitante'] == equipo_visitante)) |
                                           ((df_sin_fila_actual['Local'] == equipo_visitante) & (df_sin_fila_actual['Visitante'] == equipo_local))]
        
        # Contar las filas donde es empate
        empate = rows_con_equipos['Empate'].sum()
        
        # Porcentaje de empate
        total_partidos = len(rows_con_equipos)
        if total_partidos != 0:
            porcentaje_empate = (empate / total_partidos) * 100
        else:
            porcentaje_empate = 0
        
        return porcentaje_empate


    def aplicar_porcentaje_empate(self):
        # Aplicar la función a cada fila y crear la nueva columna
        self.df1['%_Empate'] = self.df1.apply(self.calcular_porcentaje_empate, axis=1).round(2)

        return self.df1


    def calcular_porcentaje_victoria_visitante(self, row):
        equipo_local = row['Local']
        equipo_visitante = row['Visitante']

        # Excluir la fila actual del DataFrame
        df_sin_fila_actual = self.df1.drop(row.name)
        
        # Filtrar filas donde aparezcan estos dos equipos, independientemente del orden
        rows_con_equipos = df_sin_fila_actual[((df_sin_fila_actual['Local'] == equipo_local) & (df_sin_fila_actual['Visitante'] == equipo_visitante)) |
                                           ((df_sin_fila_actual['Local'] == equipo_visitante) & (df_sin_fila_actual['Visitante'] == equipo_local))]
        
        # Contar las filas donde es victoria visitante
        victoria_visitante = rows_con_equipos['VictoriaVisitante'].sum()
        
        # Porcentaje de victoria visitante
        total_partidos = len(rows_con_equipos)
        if total_partidos != 0:
            porcentaje_victoria_visitante = (victoria_visitante / total_partidos) * 100
        else:
            porcentaje_victoria_visitante = 0
        
        return porcentaje_victoria_visitante

    def aplicar_porcentaje_victoria_visitante(self):
        # Aplicar la función a cada fila y crear la nueva columna
        self.df1['%_Victoria_Visitante'] = self.df1.apply(self.calcular_porcentaje_victoria_visitante, axis=1).round(2)

        return self.df1


    def calcular_porcentaje_equipo1_ganado(self, row):
        equipo_local = row['Local']
        equipo_visitante = row['Visitante']
        
        # Excluir la fila actual del DataFrame
        df_sin_fila_actual = self.df1.drop(row.name)
        
        # Filtrar filas donde aparezcan estos dos equipos, independientemente del orden
        rows_con_equipos = df_sin_fila_actual[((df_sin_fila_actual['Local'] == equipo_local) & (df_sin_fila_actual['Visitante'] == equipo_visitante)) |
                                               ((df_sin_fila_actual['Local'] == equipo_visitante) & (df_sin_fila_actual['Visitante'] == equipo_local))]
        
        # Contar las filas donde el equipo1 ha ganado
        equipo1_gana = rows_con_equipos[((rows_con_equipos['Local'] == row['Local']) & (rows_con_equipos['VictoriaLocal'] == 1)) |
                                        ((rows_con_equipos['Visitante'] == row['Local']) & (rows_con_equipos['VictoriaVisitante'] == 1))]
        
        # Calcular el porcentaje de veces que el equipo1 ha ganado
        total_partidos = len(rows_con_equipos)
        if total_partidos != 0:
            porcentaje_equipo1_ganado = (len(equipo1_gana) / total_partidos) * 100
        else:
            porcentaje_equipo1_ganado = 0
        
        return porcentaje_equipo1_ganado

    def aplicar_porcentaje_equipo1_ganado(self):
        # Aplicar la función a cada fila y crear la nueva columna
        self.df1['%_Equipo1_Ganado'] = self.df1.apply(self.calcular_porcentaje_equipo1_ganado, axis=1).round(2)

        return self.df1

    def equipo2_ganado(self, row):
        equipo_local = row['Local']
        equipo_visitante = row['Visitante']
        
        # Excluir la fila actual del DataFrame
        df_sin_fila_actual = self.df1.drop(row.name)
        
        # Filtrar filas donde aparezcan estos dos equipos, independientemente del orden
        rows_con_equipos = df_sin_fila_actual[((df_sin_fila_actual['Local'] == equipo_local) & (df_sin_fila_actual['Visitante'] == equipo_visitante)) |
                                            ((df_sin_fila_actual['Local'] == equipo_visitante) & (df_sin_fila_actual['Visitante'] == equipo_local))]
        
        # Contar las filas donde el equipo2 ha ganado
        equipo2_gana = rows_con_equipos[((rows_con_equipos['Local'] == row['Visitante']) & (rows_con_equipos['VictoriaLocal'] == 1)) |
                                        ((rows_con_equipos['Visitante'] == row['Visitante']) & (rows_con_equipos['VictoriaVisitante'] == 1))]
        
        # Calcular el porcentaje de veces que el equipo2 ha ganado
        total_partidos = len(rows_con_equipos)
        if total_partidos != 0:
            porcentaje_equipo2_ganado = (len(equipo2_gana) / total_partidos) * 100
        else:
            porcentaje_equipo2_ganado = 0
        
        return porcentaje_equipo2_ganado
    
    def aplicar_porcentaje_equipo2_ganado(self):
        # Aplicar la función a cada fila y crear la nueva columna
        self.df1['%_Equipo2_Ganado'] = self.df1.apply(self.equipo2_ganado, axis=1).round(2)

        return self.df1
    
    def calcular_porcentaje_equipo1_ganado_temporada(self, row):
        # Obtener el equipo 1 de la fila actual y la temporada correspondiente
        equipo1 = row['Local']
        temporada = row['Temporada']
        
        # Excluir la fila actual del DataFrame
        df_sin_fila_actual = self.df1.drop(row.name)
        
        # Filtrar filas de la temporada donde aparezca el equipo 1, independientemente de si es local o visitante
        partidos_equipo1 = df_sin_fila_actual[((df_sin_fila_actual['Local'] == equipo1) | (df_sin_fila_actual['Visitante'] == equipo1)) & (df_sin_fila_actual['Temporada'] == temporada)]
        
        # Contar las filas donde el equipo 1 ha ganado
        victorias = partidos_equipo1[((partidos_equipo1['Local'] == equipo1) & (partidos_equipo1['VictoriaLocal'] == 1)) |
                                    ((partidos_equipo1['Visitante'] == equipo1) & (partidos_equipo1['VictoriaVisitante'] == 1))]
        num_victorias_equipo1 = len(victorias)
        
        # Calcular el porcentaje de partidos ganados por el equipo 1 en la temporada
        total_partidos_temporada = len(partidos_equipo1)
        if total_partidos_temporada != 0:
            porcentaje_equipo1_ganado = (num_victorias_equipo1 / total_partidos_temporada) * 100
        else:
            porcentaje_equipo1_ganado = 0
        
        return porcentaje_equipo1_ganado

    def aplicar_porcentaje_equipo1_ganado_temporada(self):
        # Aplicar la función a cada fila y crear la nueva columna
        self.df1['%_1_G_Temporada'] = self.df1.apply(self.calcular_porcentaje_equipo1_ganado_temporada, axis=1).round(2)

        return self.df1
    
    
    def equipo1_ganado_temporada_local(self, row):
        # Obtener el equipo 1 de la fila actual y la temporada correspondiente
        equipo1 = row['Local']
        temporada = row['Temporada']
        
        # Excluir la fila actual del DataFrame
        df_sin_fila_actual = self.df1.drop(row.name)
        
        # Filtrar filas de la temporada donde aparezca el equipo 1, independientemente de si es local o visitante
        partidos_equipo1_local = df_sin_fila_actual[(df_sin_fila_actual['Local'] == equipo1) & (df_sin_fila_actual['Temporada'] == temporada)]
        
        # Contar las filas donde el equipo 1 ha ganado
        victorias_l = partidos_equipo1_local[(partidos_equipo1_local['Local'] == equipo1) & (partidos_equipo1_local['VictoriaLocal'] == 1)]
                                            
        victorias_equipo1_l = len(victorias_l)
        
        # Calcular el porcentaje de partidos ganados por el equipo 1 en la temporada
        partidos_temporada_local = len(partidos_equipo1_local)
        if partidos_temporada_local != 0:
            porcentaje_ganado_local = (victorias_equipo1_l / partidos_temporada_local) * 100
        else:
            porcentaje_ganado_local = 0
        
        return porcentaje_ganado_local

    def aplicar_equipo1_ganado_temporada_local(self):
        # Aplicar la función a cada fila y crear la nueva columna
        self.df1['%_1_G_Temporada_L'] = self.df1.apply(self.equipo1_ganado_temporada_local, axis=1).round(2)

        return self.df1
    

    def equipo1_empatado_temporada_local(self, row):
        # Obtener el equipo 1 de la fila actual y la temporada correspondiente
        equipo1 = row['Local']
        temporada = row['Temporada']
        
        # Excluir la fila actual del DataFrame
        df_sin_fila_actual = self.df1.drop(row.name)
        
        # Filtrar filas de la temporada donde aparezca el equipo 1, independientemente de si es local o visitante
        partidos_equipo1_local = df_sin_fila_actual[(df_sin_fila_actual['Local'] == equipo1) & (df_sin_fila_actual['Temporada'] == temporada)]
        
        # Contar las filas donde el equipo 1 ha empatado
        empates_l = partidos_equipo1_local[(partidos_equipo1_local['Local'] == equipo1) & (partidos_equipo1_local['Empate'] == 1)]
                                            
        empates_equipo1_l = len(empates_l)
        
        # Calcular el porcentaje de partidos empatados por el equipo 1 en la temporada
        partidos_temporada_local = len(partidos_equipo1_local)
        if partidos_temporada_local != 0:
            porcentaje_empatado_local = (empates_equipo1_l / partidos_temporada_local) * 100
        else:
            porcentaje_empatado_local = 0
        
        return porcentaje_empatado_local

    def aplicar_equipo1_empatado_temporada_local(self):
        # Aplicar la función a cada fila y crear la nueva columna
        self.df1['%_1_E_Temporada_L'] = self.df1.apply(self.equipo1_empatado_temporada_local, axis=1).round(2)

        return self.df1


    def equipo1_perdido_temporada_local(self, row):
        # Obtener el equipo 1 de la fila actual y la temporada correspondiente
        equipo1 = row['Local']
        temporada = row['Temporada']
        
        # Excluir la fila actual del DataFrame
        df_sin_fila_actual = self.df1.drop(row.name)
        
        # Filtrar filas de la temporada donde aparezca el equipo 1, independientemente de si es local o visitante
        partidos_equipo1_local = df_sin_fila_actual[(df_sin_fila_actual['Local'] == equipo1) & (df_sin_fila_actual['Temporada'] == temporada)]
        
        # Contar las filas donde el equipo 1 ha perdido
        perdidos_l = partidos_equipo1_local[(partidos_equipo1_local['Local'] == equipo1) & (partidos_equipo1_local['VictoriaVisitante'] == 1)]
                                            
        perdidos_equipo1_l = len(perdidos_l)
        
        # Calcular el porcentaje de partidos perdidos por el equipo 1 en la temporada
        partidos_temporada_local = len(partidos_equipo1_local)
        if partidos_temporada_local != 0:
            porcentaje_perdido_local = (perdidos_equipo1_l / partidos_temporada_local) * 100
        else:
            porcentaje_perdido_local = 0
        
        return porcentaje_perdido_local

    def aplicar_equipo1_perdido_temporada_local(self):
        # Aplicar la función a cada fila y crear la nueva columna
        self.df1['%_1_P_Temporada_L'] = self.df1.apply(self.equipo1_perdido_temporada_local, axis=1).round(2)

        return self.df1

    def aplicar_media_ganado(self):
        #Media de partidos ganados
        self.df1['1_Media_G'] =(self.df1.apply(self.calcular_porcentaje_equipo1_ganado_temporada, axis=1) / 100).round(2)
        self.df1['1_Media_G_Local'] = (self.df1.apply(self.equipo1_ganado_temporada_local, axis=1) / 100).round(2)

        return self.df1

    def media_goles_equipo1(self, row):
        # Obtener el equipo 1 (equipo local) de la fila actual y la temporada correspondiente
        equipo1 = row['Local']
        temporada = row['Temporada']
        
        # Excluir la fila actual del DataFrame
        df_sin_fila_actual = self.df1.drop(row.name)
        
        # Filtrar filas de la temporada donde aparezca el equipo 1 (equipo local), independientemente de si es local o visitante
        partidos_equipo1_temporada = df_sin_fila_actual[((df_sin_fila_actual['Local'] == equipo1) | (df_sin_fila_actual['Visitante'] == equipo1)) & 
                                                        (df_sin_fila_actual['Temporada'] == temporada)]
        
        # Calcular el total de goles metidos por el equipo 1 (equipo local) en esa temporada
        goles_local = partidos_equipo1_temporada[partidos_equipo1_temporada['Local'] == equipo1]['GolesLocal'].sum()
        goles_visitante = partidos_equipo1_temporada[partidos_equipo1_temporada['Visitante'] == equipo1]['GolesVisitante'].sum()
        total_goles = goles_local + goles_visitante
        
        # Contar el total de partidos jugados por el equipo 1 (equipo local) en esa temporada
        partidos = len(partidos_equipo1_temporada)

        # Calcular la media de goles por partido jugado en esa temporada
        if partidos != 0:
            media = total_goles / partidos
        else:
            media = 0
        
        return media

    def aplicar_media_goles_equipo1(self):
        # Aplicar la función a cada fila y crear la nueva columna
        self.df1['1_Media_Goles_PP'] = self.df1.apply(self.media_goles_equipo1, axis=1).round(2)

        return self.df1

    def valoracion_jugadores(self):
        for index, row in self.df1.iterrows():
            temporada_actual = row['Temporada']
            equipo_local = row['Local']
            
            # Filtrar jugadores por temporada y equipo local
            jugadores_temporada_equipo = self.df2[(self.df2['Temporada'] == temporada_actual) & (self.df2['Equipo'] == equipo_local)]
            
            # Sumar las valoraciones de los jugadores
            valor_total_equipo_local = jugadores_temporada_equipo['Valoracion'].sum()
            
            # Asignar el valor total al DataFrame de partidos
            self.df1.at[index, '1_ValorJugadores'] = valor_total_equipo_local

        return self.df1
    
    def valoracion_media_jugadores(self):
        for index, row in self.df1.iterrows():
            temporada_actual = row['Temporada']
            equipo_local = row['Local']
            
            # Filtrar jugadores por temporada y equipo local
            jugadores_temporada_equipo = self.df2[(self.df2['Temporada'] == temporada_actual) & (self.df2['Equipo'] == equipo_local)]
            
            # Sumar las valoraciones de los jugadores
            valor_total_equipo_local = jugadores_temporada_equipo['Valoracion'].mean()
            
            # Asignar el valor total al DataFrame de partidos
            self.df1.at[index, '1_MediaJugadores'] = valor_total_equipo_local
        
        return self.df1
    
    def calcular_porcentaje_equipo2_ganado_temporada(self, row):
        # Obtener el equipo 2 (equipo visitante) de la fila actual y la temporada correspondiente
        equipo2 = row['Visitante']
        temporada = row['Temporada']
        
        # Excluir la fila actual del DataFrame
        df_sin_fila_actual = self.df1.drop(row.name)
        
        # Filtrar filas de la temporada donde aparezca el equipo 2, independientemente de si es local o visitante
        partidos_equipo2 = df_sin_fila_actual[((df_sin_fila_actual['Local'] == equipo2) | (df_sin_fila_actual['Visitante'] == equipo2)) & (df_sin_fila_actual['Temporada'] == temporada)]
        
        # Contar las filas donde el equipo 2 ha ganado
        victorias = partidos_equipo2[((partidos_equipo2['Local'] == equipo2) & (partidos_equipo2['VictoriaLocal'] == 1)) |
                                    ((partidos_equipo2['Visitante'] == equipo2) & (partidos_equipo2['VictoriaVisitante'] == 1))]
        num_victorias_equipo2 = len(victorias)
        
        # Calcular el porcentaje de partidos ganados por el equipo 2 en la temporada
        total_partidos_temporada = len(partidos_equipo2)
        if total_partidos_temporada != 0:
            porcentaje_equipo2_ganado = (num_victorias_equipo2 / total_partidos_temporada) * 100
        else:
            porcentaje_equipo2_ganado = 0
        
        return porcentaje_equipo2_ganado


    def aplicar_porcentaje_equipo2_ganado_temporada(self):
        # Aplicar la función a cada fila y crear la nueva columna
        self.df1['%_2_G_Temporada'] = self.df1.apply(self.calcular_porcentaje_equipo2_ganado_temporada, axis=1).round(2)

        return self.df1


    def equipo2_ganado_temporada_local(self, row):
        # Obtener el equipo 2 (equipo visitante) de la fila actual y la temporada correspondiente
        equipo2 = row['Visitante']
        temporada = row['Temporada']

        # Excluir la fila actual del DataFrame
        df_sin_fila_actual = self.df1.drop(row.name)
        
        # Filtrar filas de la temporada donde aparezca el equipo 1, independientemente de si es local o visitante
        partidos_equipo2_local = df_sin_fila_actual[(df_sin_fila_actual['Local'] == equipo2) & (df_sin_fila_actual['Temporada'] == temporada)]
        
        # Contar las filas donde el equipo 1 ha ganado
        victorias_l = partidos_equipo2_local[(partidos_equipo2_local['Local'] == equipo2) & (partidos_equipo2_local['VictoriaLocal'] == 1)]
                                            
        victorias_equipo2_l = len(victorias_l)
        
        # Calcular el porcentaje de partidos ganados por el equipo z en la temporada
        partidos_temporada_local = len(partidos_equipo2_local)
        if partidos_temporada_local != 0:
            porcentaje_ganado_local = (victorias_equipo2_l / partidos_temporada_local) * 100
        else:
            porcentaje_ganado_local = 0
        
        return porcentaje_ganado_local


    def aplicar_equipo2_ganado_temporada_local(self):
        # Aplicar la función a cada fila y crear la nueva columna
        self.df1['%_2_G_Temporada_L'] = self.df1.apply(self.equipo2_ganado_temporada_local, axis=1).round(2)

        return self.df1


    def equipo2_empatado_temporada_local(self, row):
        # Obtener el equipo 2 (equipo visitante) de la fila actual y la temporada correspondiente
        equipo2 = row['Visitante']
        temporada = row['Temporada']

        df_sin_fila_actual = self.df1.drop(row.name)
        
        # Filtrar filas de la temporada donde aparezca el equipo 1, independientemente de si es local o visitante
        partidos_equipo2_local = df_sin_fila_actual[(df_sin_fila_actual['Local'] == equipo2) & (df_sin_fila_actual['Temporada'] == temporada)]
        
        # Contar las filas donde el equipo 1 ha ganado
        empates_l = partidos_equipo2_local[(partidos_equipo2_local['Local'] == equipo2) & (partidos_equipo2_local['Empate'] == 1)]
                                            
        empates_equipo2_l = len(empates_l)
        
        # Calcular el porcentaje de partidos ganados por el equipo 1 en la temporada
        partidos_temporada_local = len(partidos_equipo2_local)
        if partidos_temporada_local != 0:
            porcentaje_empatado_local = (empates_equipo2_l / partidos_temporada_local) * 100
        else:
            porcentaje_empatado_local = 0
        
        return porcentaje_empatado_local


    def aplicar_equipo2_empatado_temporada_local(self):
        # Aplicar la función a cada fila y crear la nueva columna
        self.df1['%_2_E_Temporada_L'] = self.df1.apply(self.equipo2_empatado_temporada_local, axis=1).round(2)

        return self.df1


    def equipo2_perdido_temporada_local(self, row):
        # Obtener el equipo 2 (equipo visitante) de la fila actual y la temporada correspondiente
        equipo2 = row['Visitante']
        temporada = row['Temporada']
        
        df_sin_fila_actual = self.df1.drop(row.name)

        # Filtrar filas de la temporada donde aparezca el equipo 2, independientemente de si es local o visitante
        partidos_equipo2_local = df_sin_fila_actual[(df_sin_fila_actual['Local'] == equipo2) & (df_sin_fila_actual['Temporada'] == temporada)]
        
        # Contar las filas donde el equipo 2 ha ganado
        perdidos_l = partidos_equipo2_local[(partidos_equipo2_local['Local'] == equipo2) & (partidos_equipo2_local['VictoriaVisitante'] == 1)]
                                            
        perdidos_equipo2_l = len(perdidos_l)
        
        # Calcular el porcentaje de partidos ganados por el equipo 2 en la temporada
        partidos_temporada_local = len(partidos_equipo2_local)
        if partidos_temporada_local != 0:
            porcentaje_perdido_local = (perdidos_equipo2_l / partidos_temporada_local) * 100
        else:
            porcentaje_perdido_local = 0
        
        return porcentaje_perdido_local

    def aplicar_equipo2_perdido_temporada_local(self):
        # Aplicar la función a cada fila y crear la nueva columna
        self.df1['%_2_P_Temporada_L'] = self.df1.apply(self.equipo2_perdido_temporada_local, axis=1).round(2)

        return self.df1
    
    
    def aplicar_media_ganado2(self):
        self.df1['2_Media_G'] =(self.df1.apply(self.calcular_porcentaje_equipo2_ganado_temporada, axis=1) / 100).round(2)
        self.df1['2_Media_G_Local'] = (self.df1.apply(self.equipo2_ganado_temporada_local, axis=1) / 100).round(2)

    
    def media_goles_equipo2(self, row):
        # Obtener el equipo 2 (equipo visitante) de la fila actual y la temporada correspondiente
        equipo2 = row['Visitante']
        temporada = row['Temporada']
        
        # Excluir la fila actual del DataFrame
        df_sin_fila_actual = self.df1.drop(row.name)
        
        # Filtrar filas de la temporada donde aparezca el equipo 2 (equipo visitante), independientemente de si es local o visitante
        partidos_equipo2_temporada = df_sin_fila_actual[((df_sin_fila_actual['Local'] == equipo2) | (df_sin_fila_actual['Visitante'] == equipo2)) & 
                                                        (df_sin_fila_actual['Temporada'] == temporada)]
        
        # Calcular el total de goles metidos por el equipo 2 (equipo visitante) en esa temporada
        goles_local = partidos_equipo2_temporada[partidos_equipo2_temporada['Local'] == equipo2]['GolesLocal'].sum()
        goles_visitante = partidos_equipo2_temporada[partidos_equipo2_temporada['Visitante'] == equipo2]['GolesVisitante'].sum()
        total_goles = goles_local + goles_visitante
        
        # Contar el total de partidos jugados por el equipo 2 (equipo visitante) en esa temporada
        partidos = len(partidos_equipo2_temporada)

        # Calcular la media de goles por partido jugado en esa temporada
        if partidos != 0:
            media = total_goles / partidos
        else:
            media = 0
        
        return media

    def aplicar_media_goles_equipo2(self):
        # Aplicar la función a cada fila y crear la nueva columna
        self.df1['2_Media_Goles_PP'] = self.df1.apply(self.media_goles_equipo2, axis=1).round(2)

        return self.df1

    def valor_jugadores_equipo2(self):
        #Valor total de los jugadores para el equipo visitante en esa temporada
        for index, row in self.df1.iterrows():
            temporada_actual = row['Temporada']
            equipo2 = row['Visitante']
            
            # Filtrar jugadores por temporada y equipo local
            jugadores_temporada_equipo = self.df2[(self.df2['Temporada'] == temporada_actual) & (self.df2['Equipo'] == equipo2)]
            
            # Sumar las valoraciones de los jugadores
            valor_total_equipo2 = jugadores_temporada_equipo['Valoracion'].sum()
            
            # Asignar el valor total al DataFrame de partidos
            self.df1.at[index, '2_ValorJugadores'] = valor_total_equipo2

        return self.df1
    
    def valoracion_media_jugadores2(self):
        #Media del valor de los jugadores del equipo viistante en esa temporada
        for index, row in self.df1.iterrows():
            temporada_actual = row['Temporada']
            equipo2 = row['Visitante']
            
            # Filtrar jugadores por temporada y equipo local
            jugadores_temporada_equipo = self.df2[(self.df2['Temporada'] == temporada_actual) & (self.df2['Equipo'] == equipo2)]
            
            # Sumar las valoraciones de los jugadores
            valor_total_equipo2 = jugadores_temporada_equipo['Valoracion'].mean()
            
            # Asignar el valor total al DataFrame de partidos
            self.df1.at[index, '2_MediaJugadores'] = valor_total_equipo2

        return self.df1
    
    def procesar(self):
        # Dividir la columna Temporada en dos columnas separadas de año inicial y año final
        self.df1[['Año Inicial', 'Año Final']] = self.df1['Temporada'].str.split('-', expand=True)

        # Convertir las columnas de año inicial y año final a tipo entero
        self.df1['Año Inicial'] = self.df1['Año Inicial'].astype(int)
        self.df1['Año Final'] = self.df1['Año Final'].astype(int)

        # Calcular el año medio entre el año inicial y el año final
        self.df1['Temporada'] = self.df1[['Año Inicial', 'Año Final']].mean(axis=1)

        # Convertir la temporada a tipo datetime
        self.df1['Temporada'] = pd.to_datetime(self.df1['Temporada'], format='%Y')

        # Eliminar las columnas de año inicial y año final si es necesario
        del self.df1['Año Inicial']
        del self.df1['Año Final']

        # Filtrar las filas para la temporada 2023-01-01
        champions_23_24 = self.df1.loc[self.df1['Temporada'] == '2023-01-01']

        # Filtrar las filas para el resto de temporadas
        champions = self.df1.loc[self.df1['Temporada'] != '2023-01-01']

        return champions, champions_23_24




def guardar_diccionario(diccionario, nombre_archivo):
    # Guardar el diccionario en el archivo JSON
    with open(nombre_archivo, 'w', encoding="utf-8") as archivo:
        json.dump(diccionario, archivo, ensure_ascii=False)


def guardar_data(ruta_archiuvo, nombre):
    nombre.to_csv(ruta_archiuvo, index=False)



def main():
    # Crear instancia de Entrenador
    entrenador = Entrenador('data/entrenador.csv')
    diccionario_entrenadores = entrenador.diccionario_entrenadores()  #guardar
    df_entrenador = entrenador.procesar()  #guardar

    # Crear instancia de Equipo
    df_equipo = Equipo('data/equipo.csv')
    diccionario_equipos = df_equipo.diccionario_equipos()  #guardar 
    df_equipo = df_equipo.procesar()  #guardar

    # Crear instancia de Partido
    df_partido = Partido('data/partido.csv')
    df_partido.procesar1()
    df_partido.procesar_diccionario_equipos(diccionario_equipos)
    df_partido = df_partido.procesar2()

    # Crear instancia de TrayectoriaEntrenador
    df_trayectoria_entrenador = TrayectoriaEntrenador('data/trayectoria_entrenador.csv')
    df_trayectoria_entrenador.procesar()
    df_trayectoria_entrenador.id_equipo(diccionario_equipos)
    df_trayectoria_entrenador = df_trayectoria_entrenador.procesar2()   #guardar

    # Crear instancia de Jugador
    df_jugadores = Jugador('data/jugador.csv', 'data/jugador2.csv')
    df_jugadores.un_data()
    df_jugadores.procesar()
    df_jugadores.id_jugador()
    # Obtener el diccionario de IDs de los jugadores
    diccionario_ids_jugadores = df_jugadores.asignar_ids('Jugador')  #guardar

    # Ahora, puedes usar diccionario_ids_jugadores como desees en tu programa
    print(diccionario_ids_jugadores)
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
    print(champions.head(10))

    guardar_diccionario(diccionario_entrenadores, 'cosas/id_entrenador.json')
    guardar_diccionario(diccionario_equipos, 'cosas/id_equipo.json')
    guardar_diccionario(diccionario_ids_jugadores, 'cosas/id_jugador.json')

    guardar_data('cosas/df_entrenador.csv', df_entrenador)
    guardar_data('cosas/df_equipo.csv', df_equipo)
    guardar_data('cosas/champions.csv', champions)
    guardar_data('cosas/champions_23_24.csv', champions_23_24)
    guardar_data('cosas/df_jugadores.csv', df_jugadores)
    guardar_data('cosas/df_entrenador_trayectoria.csv', df_trayectoria_entrenador)


if __name__ == '__main__':
    main()