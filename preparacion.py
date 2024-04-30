import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from difflib import get_close_matches


'''Entrenador.csv'''
class Entrenador:
    def __init__(self, ruta):
        self.ruta = ruta
    
    def cargar_entrandores(self):
        df1= pd.read_csv(self.ruta)

        df1.drop(['Pais'], axis=1, inplace=True)

        #Diccionario entrenadores
        diccionario_entrenadores = df1.set_index('Apodo')['idEntrenador'].to_dict()
        return df1, diccionario_entrenadores


entrenador = Entrenador('data/entrenador.csv')
df1, diccionario_equipos = entrenador.cargar_entrandores()



'''Equipo.csv'''
class Equipo:
    def __init__(self, ruta):
        self.ruta = ruta

    def cargar_equipos(self):
        df2 = pd.read_csv(self.ruta)

        df2.drop(['Escudo'], axis=1, inplace=True)

        #Diccionario equipos
        diccionario_equipos = df2.set_index('Nombre')['idEquipo'].to_dict()
        dic_equipos_original = diccionario_equipos.copy()

        return df2, diccionario_equipos, dic_equipos_original

equipo = Equipo('data/equipo.csv')
df2, diccionario_equipos, dic_equipos_original = equipo.cargar_equipos()


'''Partido.csv'''

# - Eliminar filas duplicadas
# - Añadir id por partido
# - Eliminar columnas que no nos sirven
# - Añadir id en local y visitante en vez de el nombre del equipo
# - Añadir columnas bool victoria local, victoria visitante, empate

class Partido:
    def __init__(self, ruta, diccionario_equipos):
        self.ruta = ruta
        self.diccionario_equipos = diccionario_equipos

    def cargar_partido(self):
        df3 = pd.read_csv(self.ruta)
        #Eliminar filas duplicadas
        df3 = df3[df3['Local'] != 'Home']
        df3.reset_index(drop=True, inplace=True)
        df3.drop_duplicates()

        #Columnas que no necesito
        columnas_a_eliminar = ['Wk', 'Dia', 'Fecha', 'Hora', 'Reporte', 'Notas', 'Público', 'Arbitro']
        df3 = df3.drop(columns=columnas_a_eliminar)
        return df3
    
    
    def obtener_id_equipo(self, nombre_equipo):

        #Para que coincidan los nombres de los equipos con el diccionario
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
                self.diccionario_equipos[clave_nueva] = self.diccionario_equipos.pop(clave_antigua)


        # Buscar coincidencia exacta
        if nombre_equipo in self.diccionario_equipos:
            return self.diccionario_equipos[nombre_equipo]
        
        # Buscar coincidencias cercanas
        matches = get_close_matches(nombre_equipo, self.diccionario_equipos.keys(), n=1, cutoff=0.8)
        if matches:
            return self.diccionario_equipos[matches[0]]
        
        # Si no hay coincidencia, devolver el nombre original
        return nombre_equipo
    

    def preparar_partido(self, df3):
        df3['Local'] = df3['Local'].astype(str)
        df3['Visitante'] = df3['Visitante'].astype(str)

        # Aplicar la función a las columnas 'Local' y 'Visitante'
        df3['Local'] = df3['Local'].apply(self.obtener_id_equipo)
        df3['Visitante'] = df3['Visitante'].apply(self.obtener_id_equipo)

        df3 = df3.dropna(subset=['Ronda'])
        df3 = df3.reset_index(drop=True)

        # Añadir una nueva columna 'idPartido' con valores únicos
        df3['idPartido'] = range(1, len(df3) + 1)

        # Reorganizar las columnas para que 'idPartido' sea la primera
        df3 = df3[['idPartido'] + [col for col in df3.columns if col != 'idPartido']]

        #Los valores nulos de los futuros partidos que se van a jugar voy a reemplazarlos por '0-0'
        df3['Resultado'] = df3['Resultado'].fillna('0–0')

        #Goles de local y visitante en diferentes columnas
        df3[['GolesLocal','GolesVisitante']] = df3['Resultado'].str.split('–',expand=True)
        df3 = df3.drop(columns=['Resultado'])

        #Columnas booleanas para saber si el equipo local o visitante ganó, empató o perdió
        df3['VictoriaLocal'] = (df3['GolesLocal'] > df3['GolesVisitante']).astype(int)
        df3['Empate'] = (df3['GolesLocal'] == df3['GolesVisitante']).astype(int)
        df3['VictoriaVisitante'] = (df3['GolesLocal'] < df3['GolesVisitante']).astype(int)

        return df3

partido = Partido('data/partido.csv', diccionario_equipos)
df3 = partido.cargar_partido()
df3 = partido.preparar_partido(df3)


'''Trayectoria_entrenador.csv'''

# - IdEquipo en vez de el nombre
# - Eliminar columnas que no nos sirven

#Cambiar a id del equipo
def id_equipo(equipo, dic_equipos_original):
    equipo_lower = equipo.lower()  # Convertir a minúsculas para comparación insensible a mayúsculas y minúsculas
    
    if equipo_lower in dic_equipos_original:
        return dic_equipos_original[equipo_lower]

    # Buscar coincidencias cercanas
    matches = get_close_matches(equipo_lower, dic_equipos_original.keys(), n=1, cutoff=0.8)
    if matches:
        return dic_equipos_original[matches[0]]
    
    # Si no hay coincidencia, devolver el nombre original
    return 0

class TrayectoriaEntrenador:
    def __init__(self, ruta, dic_equipos_original):
        self.ruta = ruta
        self.dic_equipos_original = dic_equipos_original

    def cargar_trayectoria(self):
        df4 = pd.read_csv(self.ruta)
        return df4

    def preparar_trayectoria(self, df4):
        #Eliminar columnas que no necesito
        columns_to_drop = ['Nun', 'Non', 'Non.1', 'División', 'Edad']
        df4 = df4.drop(columns=columns_to_drop)

        #Voy a eliminar ya las filas que estan vacías para no tener problemas con las otras preparaciones
        df4.replace('-', pd.NA, inplace=True)
        df4 = df4.dropna()
        df4 = df4.reset_index(drop=True)

        # Aplicar la función a la columna 'Equipo' de tu DataFrame
        df4['Equipo'] = df4['Equipo'].astype(str)
        df4['Equipo'] = df4['Equipo'].apply(lambda x: id_equipo(x, self.dic_equipos_original))

        return df4


trayectoria_entrenador = TrayectoriaEntrenador('data/Trayectoria_entrenador.csv', dic_equipos_original)
df4 = trayectoria_entrenador.cargar_trayectoria()
df4 = trayectoria_entrenador.preparar_trayectoria(df4)


'''#Jugador.csv

# - Juntar las dos tablas
# - Eliminar columnas no necesarias
# - Cambiar idEquipo y poner idJugadores teniendo en cuenta que algunos se repiten
# - Añadir columna valoracion de jugadores y calcularla con valores estadísticos

# In[49]:


df5 = pd.read_csv('data/jugador.csv')
df5.head(20)


# In[50]:


df6 = pd.read_csv('data/jugador2.csv')
df6.head(20)


# In[51]:


#Unir las dos tablas de jugadores
jugadores = pd.concat([df5, df6], ignore_index=True)

# Imprimir las columnas de jugadores
print(jugadores.columns)
jugadores.head(20000)


# In[52]:


#Eliminar columnas que no necesito
colum_eliminar = ['#', 'Nacimiento', '90 s', 'G+A', 'G-TP', 'Gls.90', 'Ast90', 'G+A90', 'G-TP90',
       'G+A-TP90', 'Partidos', 'xG90', 'xAG90', 'xG+xAG90', 'npxG90', 'npxG+xAG90', 'Gls90.', 'xAG', 'npxG+xAG']

jugadores = jugadores.drop(columns=colum_eliminar)
jugadores.head(20000)


# In[53]:


#Eliminar filas que se me han guardado de los encabezados
jugadores = jugadores[jugadores['Equipo'] != 'Equipo']
jugadores.reset_index(drop=True, inplace=True)
jugadores.head(37)


# In[54]:


jugadores_temporada_equipo = jugadores[(jugadores['Equipo'] == 'hrDinamo Zagreb')]
jugadores_temporada_equipo


# In[55]:


#Diccionario con los id de los jugadores
def asignar_ids(df, columna_jugador):
    # Obtén la lista única de jugadores
    jugadores_unicos = df[columna_jugador].unique()

    # Inicializa un diccionario para almacenar los IDs
    jugadores_id = {}

    # Asigna un ID único a cada jugador
    for idx, jugador in enumerate(jugadores_unicos):
        jugadores_id[jugador] = idx + 1  # Suma 1 para comenzar los IDs desde 1

    return jugadores_id

# Llama a la función para asignar IDs a los jugadores
ids_jugadores = asignar_ids(jugadores, 'Jugador')

# Imprime el diccionario de jugadores con sus IDs
print(ids_jugadores)


# In[56]:


#Sustituir en el data por los ids
def reemplazar_con_ids(df, columna_jugador):
    # Llama a la función para asignar IDs a los jugadores
    diccionario_ids = asignar_ids(df, columna_jugador)

    # Crea una nueva columna 'ID_Jugador' en el DataFrame
    df['idJugador'] = df[columna_jugador].map(diccionario_ids)

    # Elimina la columna original de jugadores
    #df.drop(columna_jugador, axis=1, inplace=True)

    columnas_ordenadas = ['Temporada', 'idJugador', columna_jugador] + [col for col in df.columns if col not in ['Temporada', 'idJugador', columna_jugador]]
    df = df[columnas_ordenadas]

    return df

jugadores = reemplazar_con_ids(jugadores, 'Jugador')
jugadores.head(20000)


# In[57]:


#Cambiar a id equipos
#Para que coincidan los nombres de los equipos con el diccionario
claves_cambiadas = {'Dinamo Zagreb': 'Croatia Zagreb','PSV': 'PSV Eindhoven', 'Shakhtar Donetsk': 'Shakhtar',
                    'Linfield': 'Linfield FC', 'Cork City': 'Cork City FC', 'Budapest Honvéd': 'Honvéd',
                    'AIK Solna': 'AIK Stockholm', 'Blackburn Rovers': 'Blackburn', 'Newcastle': 'Newcastle Utd',
                    'Hertha Berliner': 'Hertha BSC', 'Royal Antwerp': 'Antwerp', 'Glentoran': 'Glentoran FC',
                    'Leeds': 'Leeds United', 'Skonto': 'Skonto FC', 'Tavriya': 'Tavriya Simferopol'}

for clave_antigua, clave_nueva in claves_cambiadas.items():
    if clave_antigua in diccionario_equipos:
        diccionario_equipos[clave_nueva] = diccionario_equipos.pop(clave_antigua)


jugadores['Equipo'] = jugadores['Equipo'].astype(str)
jugadores['Equipo'] = jugadores['Equipo'].apply(obtener_id_equipo)
jugadores['Equipo'].replace({'nlPSV': '21'}, inplace=True)
jugadores['Equipo'].replace({'hrDinamo Zagreb': '235'}, inplace=True)
jugadores['Equipo'].replace({'uaShakhtar Donetsk': '92'}, inplace=True)

# Imprimir el DataFrame actualizado
jugadores.head(37)


# In[58]:


jugadores['Equipo'].unique()


# In[59]:


#Elimino las filas que no tengan los equipos id asignados, nos dan igual
condicion = ~jugadores['Equipo'].isin(['fiLahti', 'isKV', 'isÍþróttabandalag Akraness', 'mtFloriana FC', 'atAustria Salzburg'])
jugadores = jugadores[condicion]
jugadores.reset_index(drop=True, inplace=True)
jugadores.head(37)


# In[60]:


# Definir las columnas a convertir a tipo numérico
columnas_numericas = ['Edad', 'PJ', 'Titular', 'Mín', 'Gls.', 'Ass', 'TP', 'TPint', 'TA', 'TR', 'xG', 'npxG', 'PrgC', 'PrgP', 'PrgR', 'Equipo']

# Convertir las columnas a tipo numérico, tratando los errores como NaN
jugadores[columnas_numericas] = jugadores[columnas_numericas].apply(pd.to_numeric, errors='coerce')

# Supongamos que tu DataFrame se llama df
columnas_categoricas = ['Jugador', 'País', 'Posc']

# Convierte las columnas categóricas al tipo de dato category
jugadores[columnas_categoricas] = jugadores[columnas_categoricas].astype('category')

jugadores.info()
jugadores.head(15)


# In[61]:


filas_filtradas = jugadores[(jugadores['Temporada'] == '2021-2022') & (jugadores['Equipo'] == 1)]

filas_filtradas


# In[62]:


# Reemplazar NaN en la columna 'Ass' con 0
jugadores['Ass'] = jugadores['Ass'].fillna(0)

# Reemplazar NaN en la columna 'TPint' con 0
jugadores['TP'] = jugadores['TP'].fillna(0)

# Reemplazar NaN en la columna 'TPint' con 0
jugadores['TPint'] = jugadores['TPint'].fillna(0)

jugadores['Mín'].fillna(jugadores['PJ'] * 90, inplace=True)

# Lista de columnas a las que quieres aplicar el reemplazo de NaN con la media
columnas_a_reemplazar = ['xG', 'npxG', 'PrgC', 'PrgP', 'PrgR', 'Edad']

for columna in columnas_a_reemplazar:
    media_columna = jugadores[columna].mean()
    jugadores[columna] = jugadores[columna].fillna(media_columna)

jugadores.head(37)


# In[63]:


jugadores.info()


# In[64]:


# Asigna pesos a cada métrica
pesos = {'Mín': 0.05,
         'PJ': 0.15,
         'Gls.': 0.40,
         'Ass': 0.2,
         'TR': -0.15,
         'PrgP': 0.15,
         'PrgR': 0.15}

# Calcula la valoración para cada jugador
jugadores['V'] = (jugadores['Mín'] * pesos['Mín'] +
                            jugadores['PJ'] * pesos['PJ'] +
                            jugadores['Gls.'] * pesos['Gls.'] +
                            jugadores['Ass'] * pesos['Ass'] +
                            jugadores['TR'] * pesos['TR'] +
                            jugadores['PrgP'] * pesos['PrgP'] +
                            jugadores['PrgR'] * pesos['PrgR'])

# Normaliza la valoración a un rango 0 a 100
max_valoracion = jugadores['V'].max()
min_valoracion = jugadores['V'].min()
jugadores['Valoracion'] = 100 * (jugadores['V'] - min_valoracion) / (max_valoracion - min_valoracion)
jugadores.drop(columns=['V'], inplace=True)

jugadores.head(10)


# In[65]:


filas_filtradas = jugadores[(jugadores['Temporada'] == '2022-2023') & (jugadores['Equipo'] == 1)]

# Seleccionar las columnas 'Jugador' y 'Valoracion_Normalizada' de las filas filtradas
columnas_seleccionadas = filas_filtradas[['Jugador', 'Valoracion']]

# Imprimir las columnas seleccionadas
columnas_seleccionadas


#Champions.csv

# Crear un data recopilación de la inforamción de nuestors datas partido de la tabla partidos.csv

# In[66]:


df3.info()


# In[67]:


import re

# Patrones a buscar y reemplazar
patrones_reemplazo = {
    r'\((\d+)\)(\d+)': r'\2',  # (n)k => k
    r'(\d+)\((\d+)\)': r'\1'   # k(n) => k
}

# Aplicar reemplazo en la columna 'GolesLocal'
for patron, reemplazo in patrones_reemplazo.items():
    df3['GolesLocal'] = df3['GolesLocal'].replace(to_replace=patron, value=reemplazo, regex=True)

# Aplicar reemplazo en la columna 'GolesVisitante'
for patron, reemplazo in patrones_reemplazo.items():
    df3['GolesVisitante'] = df3['GolesVisitante'].replace(to_replace=patron, value=reemplazo, regex=True)


df3['GolesLocal'].unique()


# In[68]:


# Convertir columnas de goles a tipo int
df3['GolesLocal'] = df3['GolesLocal'].astype(int)
df3['GolesVisitante'] = df3['GolesVisitante'].astype(int)

# Convertir columnas de evento
df3['Evento'] = df3['Evento'].astype(str)

# Convertir columnas de local y visitante a tipo int
df3['Local'] = df3['Local'].astype(int)
df3['Visitante'] = df3['Visitante'].astype(int)

# Convertir columna de temporada a tipo string
df3['Temporada'] = df3['Temporada'].astype(str)

# Convertir columna de ronda a tipo string
df3['Ronda'] = df3['Ronda'].astype(str)

df3.info()


# ##### Estadísticas de los dos equipos habiendo jugado entre ellos

# In[69]:


# Función para calcular el porcentaje de victorias locales
def calcular_porcentaje_victorias_local(row):
    # Obtener los equipos de la fila actual
    equipo_local = row['Local']
    equipo_visitante = row['Visitante']

    # Excluir la fila actual del DataFrame
    df_sin_fila_actual = df3.drop(row.name)
    
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

# Aplicar la función a cada fila y crear la nueva columna
df3['%_Victorias_Local'] = df3.apply(calcular_porcentaje_victorias_local, axis=1).round(2)

df3.head(10)


# In[70]:


# Función para calcular el porcentaje de empates
def calculo_porcentaje_empate(row):
    equipo_local = row['Local']
    equipo_visitante = row['Visitante']

    # Excluir la fila actual del DataFrame
    df_sin_fila_actual = df3.drop(row.name)
    
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

# Aplicar la función a cada fila y crear la nueva columna
df3['%_Empate'] = df3.apply(calculo_porcentaje_empate, axis=1).round(2)

df3.head(10)


# In[71]:


# Función para calcular el porcentaje de ganados por el visitante
def calculo_porcentaje_victoria_visitante(row):
    equipo_local = row['Local']
    equipo_visitante = row['Visitante']

    # Excluir la fila actual del DataFrame
    df_sin_fila_actual = df3.drop(row.name)
    
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

# Aplicar la función a cada fila y crear la nueva columna
df3['%_Victoria_Visitante'] = df3.apply(calculo_porcentaje_victoria_visitante, axis=1).round(2)

df3.head(10)


# In[72]:


#Porcentaje que el equipo1 que es el local ha ganado al equipo2 (visitante) en todas las disputas que han tenido esos dos equipos,
independientemente de si el equipo1 es local o visitante

def calcular_porcentaje_equipo1_ganado(row):
    equipo_local = row['Local']
    equipo_visitante = row['Visitante']
    
    # Excluir la fila actual del DataFrame
    df_sin_fila_actual = df3.drop(row.name)
    
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

# Aplicar la función a cada fila y crear la nueva columna
df3['%_Equipo1_Ganado'] = df3.apply(calcular_porcentaje_equipo1_ganado, axis=1).round(2)

df3.head(10)


# In[73]:


def equipo2_ganado(row):
    equipo_local = row['Local']
    equipo_visitante = row['Visitante']
    
    # Excluir la fila actual del DataFrame
    df_sin_fila_actual = df3.drop(row.name)
    
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

# Aplicar la función a cada fila y crear la nueva columna
df3['%_Equipo2_Ganado'] = df3.apply(equipo2_ganado, axis=1).round(2)

df3.head(10)


# ##### Estadísticas equipo 1

# In[74]:


#Partidos ganados por el equipo1 en esa temporada

def calcular_porcentaje_equipo1_ganado_temporada(row):
    # Obtener el equipo 1 de la fila actual y la temporada correspondiente
    equipo1 = row['Local']
    temporada = row['Temporada']
    
    # Excluir la fila actual del DataFrame
    df_sin_fila_actual = df3.drop(row.name)
    
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

# Aplicar la función a cada fila y crear la nueva columna
df3['%_1_G_Temporada'] = df3.apply(calcular_porcentaje_equipo1_ganado_temporada, axis=1).round(2)

df3.head(10)


# In[75]:


#Partidos ganados por el equipo1 en esa temporada pero solo como local

def equipo1_ganado_temporada_local(row):
    # Obtener el equipo 1 de la fila actual y la temporada correspondiente
    equipo1 = row['Local']
    temporada = row['Temporada']
    
    # Excluir la fila actual del DataFrame
    df_sin_fila_actual = df3.drop(row.name)
    
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

# Aplicar la función a cada fila y crear la nueva columna
df3['%_1_G_Temporada_L'] = df3.apply(equipo1_ganado_temporada_local, axis=1).round(2)

df3.head(10)


# In[76]:


#Partidos empatado esa temporada pero solo jugando como local

def equipo1_empatado_temporada_local(row):
    # Obtener el equipo 1 de la fila actual y la temporada correspondiente
    equipo1 = row['Local']
    temporada = row['Temporada']
    
    # Excluir la fila actual del DataFrame
    df_sin_fila_actual = df3.drop(row.name)
    
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

# Aplicar la función a cada fila y crear la nueva columna
df3['%_1_E_Temporada_L'] = df3.apply(equipo1_empatado_temporada_local, axis=1).round(2)

df3.head(10)


# In[77]:


#Partidos perdido esa temporada pero solo jugando como local

def equipo1_perdido_temporada_local(row):
    # Obtener el equipo 1 de la fila actual y la temporada correspondiente
    equipo1 = row['Local']
    temporada = row['Temporada']
    
    # Excluir la fila actual del DataFrame
    df_sin_fila_actual = df3.drop(row.name)
    
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

# Aplicar la función a cada fila y crear la nueva columna
df3['%_1_P_Temporada_L'] = df3.apply(equipo1_perdido_temporada_local, axis=1).round(2)

df3.head(10)


# In[78]:


#Media de partidos ganados

df3['1_Media_G'] =( df3.apply(calcular_porcentaje_equipo1_ganado_temporada, axis=1) / 100).round(2)
df3['1_Media_G_Local'] = (df3.apply(equipo1_ganado_temporada_local, axis=1) / 100).round(2)


df3.head(10)


# In[79]:


#Media de goles del equipo 1 por partidos jugados en cada temporada

def media_goles_equipo1(row):
    # Obtener el equipo 1 (equipo local) de la fila actual y la temporada correspondiente
    equipo1 = row['Local']
    temporada = row['Temporada']
    
    # Excluir la fila actual del DataFrame
    df_sin_fila_actual = df3.drop(row.name)
    
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

# Aplicar la función a cada fila y crear la nueva columna
df3['1_Media_Goles_PP'] = df3.apply(media_goles_equipo1, axis=1).round(2)

df3.head(10)



# In[80]:


#Transformamos la columna que vamos a usar
jugadores.tail(10)


# In[81]:


#Valor total de los jugadores para el equipo local en esa temporada

for index, row in df3.iterrows():
    temporada_actual = row['Temporada']
    equipo_local = row['Local']
    
    # Filtrar jugadores por temporada y equipo local
    jugadores_temporada_equipo = jugadores[(jugadores['Temporada'] == temporada_actual) & (jugadores['Equipo'] == equipo_local)]
    
    # Sumar las valoraciones de los jugadores
    valor_total_equipo_local = jugadores_temporada_equipo['Valoracion'].sum()
    
    # Asignar el valor total al DataFrame de partidos
    df3.at[index, '1_ValorJugadores'] = valor_total_equipo_local

df3.head(10)


# In[82]:


#Media del valor de los jugadores del equipo local en esa temporada

for index, row in df3.iterrows():
    temporada_actual = row['Temporada']
    equipo_local = row['Local']
    
    # Filtrar jugadores por temporada y equipo local
    jugadores_temporada_equipo = jugadores[(jugadores['Temporada'] == temporada_actual) & (jugadores['Equipo'] == equipo_local)]
    
    # Sumar las valoraciones de los jugadores
    valor_total_equipo_local = jugadores_temporada_equipo['Valoracion'].mean()
    
    # Asignar el valor total al DataFrame de partidos
    df3.at[index, '1_MediaJugadores'] = valor_total_equipo_local

df3.head(10)


# #### Estadísticas quipo 2, equipo visitante

# In[83]:


#Partidos ganados por el equipo2 en esa temporada

def calcular_porcentaje_equipo2_ganado_temporada(row):
    # Obtener el equipo 2 (equipo visitante) de la fila actual y la temporada correspondiente
    equipo2 = row['Visitante']
    temporada = row['Temporada']
    
    # Excluir la fila actual del DataFrame
    df_sin_fila_actual = df3.drop(row.name)
    
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

# Aplicar la función a cada fila y crear la nueva columna
df3['%_2_G_Temporada'] = df3.apply(calcular_porcentaje_equipo2_ganado_temporada, axis=1).round(2)

df3.head(10)



# In[84]:


#Partidos ganados por el equipo2 en esa temporada pero solo como local

def equipo2_ganado_temporada_local(row):
    # Obtener el equipo 1 de la fila actual y la temporada correspondiente
    equipo2 = row['Visitante']
    temporada = row['Temporada']

    # Excluir la fila actual del DataFrame
    df_sin_fila_actual = df3.drop(row.name)
    
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

# Aplicar la función a cada fila y crear la nueva columna
df3['%_2_G_Temporada_L'] = df3.apply(equipo2_ganado_temporada_local, axis=1).round(2)

df3.head(10)


# In[85]:


#Partidos empatado por el equipo2 esa temporada pero solo jugando como local
def equipo2_empatado_temporada_local(row):
    # Obtener el equipo 1 de la fila actual y la temporada correspondiente
    equipo2 = row['Visitante']
    temporada = row['Temporada']

    df_sin_fila_actual = df3.drop(row.name)
    
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

# Aplicar la función a cada fila y crear la nueva columna
df3['%_2_E_Temporada_L'] = df3.apply(equipo2_empatado_temporada_local, axis=1).round(2)


# In[86]:


#Partidos perido esa temporada pero solo jugando como local
def equipo2_perdido_temporada_local(row):
    # Obtener el equipo 2 de la fila actual y la temporada correspondiente
    equipo2 = row['Visitante']
    temporada = row['Temporada']
    
    df_sin_fila_actual = df3.drop(row.name)

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

# Aplicar la función a cada fila y crear la nueva columna
df3['%_2_P_Temporada_L'] = df3.apply(equipo2_perdido_temporada_local, axis=1).round(2)


# In[87]:


#Media de partidos ganados

df3['2_Media_G'] =( df3.apply(calcular_porcentaje_equipo2_ganado_temporada, axis=1) / 100).round(2)
df3['2_Media_G_Local'] = (df3.apply(equipo2_ganado_temporada_local, axis=1) / 100).round(2)


# In[88]:


#Media de goles del equipo 2 por partidos jugados en cada temporada

def media_goles_equipo2(row):
    # Obtener el equipo 2 (equipo visitante) de la fila actual y la temporada correspondiente
    equipo2 = row['Visitante']
    temporada = row['Temporada']
    
    # Excluir la fila actual del DataFrame
    df_sin_fila_actual = df3.drop(row.name)
    
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

# Aplicar la función a cada fila y crear la nueva columna
df3['2_Media_Goles_PP'] = df3.apply(media_goles_equipo2, axis=1).round(2)

df3.head(10)


# In[89]:


#Valor total de los jugadores para el equipo visitante en esa temporada
for index, row in df3.iterrows():
    temporada_actual = row['Temporada']
    equipo2 = row['Visitante']
    
    # Filtrar jugadores por temporada y equipo local
    jugadores_temporada_equipo = jugadores[(jugadores['Temporada'] == temporada_actual) & (jugadores['Equipo'] == equipo2)]
    
    # Sumar las valoraciones de los jugadores
    valor_total_equipo2 = jugadores_temporada_equipo['Valoracion'].sum()
    
    # Asignar el valor total al DataFrame de partidos
    df3.at[index, '2_ValorJugadores'] = valor_total_equipo2


# In[90]:


#Media del valor de los jugadores del equipo viistante en esa temporada
for index, row in df3.iterrows():
    temporada_actual = row['Temporada']
    equipo2 = row['Visitante']
    
    # Filtrar jugadores por temporada y equipo local
    jugadores_temporada_equipo = jugadores[(jugadores['Temporada'] == temporada_actual) & (jugadores['Equipo'] == equipo2)]
    
    # Sumar las valoraciones de los jugadores
    valor_total_equipo2 = jugadores_temporada_equipo['Valoracion'].mean()
    
    # Asignar el valor total al DataFrame de partidos
    df3.at[index, '2_MediaJugadores'] = valor_total_equipo2


# In[91]:


df3.head(10)


# In[92]:


df3.info()


# #### Comprobar que mis nuevos datas no tengan valores nulos y su formato sea correcto

# In[93]:


import csv
import json


# In[94]:


#De entrenadores
df1.info()


# In[95]:


# Guardar el DataFrame en un archivo CSV
df1.to_csv('dataframe/df_entrenador.csv', index=False)

# Nombre del archivo donde se guardará el JSON
nombre_archivo = 'dataframe/id_entrenador.json'

# Guardar el diccionario en el archivo JSON
with open(nombre_archivo, 'w', encoding="utf-8") as archivo:
    json.dump(diccionario_entrenadores, archivo, ensure_ascii=False)

print("Diccionario id entrenadores guardado")


# In[96]:


#Entrenador trayectoria
df4.info()


# In[97]:


df4['PJ'] = pd.to_numeric(df4['PJ'])
df4['PG'] = pd.to_numeric(df4['PG'])
df4['PE'] = pd.to_numeric(df4['PE'])
df4['PP'] = pd.to_numeric(df4['PP'])
df4.info()


# In[98]:


df4.to_csv('dataframe/df_entrenador_trayectoria.csv', index=False)


# In[99]:


#Df equipo
df2.info()


# In[100]:


df2.to_csv('dataframe/df_equipo.csv', index=False)

# Nombre del archivo donde se guardará el JSON
nombre_archivo = 'dataframe/id_equipo.json'

# Guardar el diccionario en el archivo JSON
with open(nombre_archivo, 'w', encoding="utf-8") as archivo:
    json.dump(dic_equipos_original, archivo, ensure_ascii=False)

print("Diccionario id equipos guardado")


# In[101]:


#Dataframe partidos
df3.info()


# In[102]:


# Dividir la columna Temporada en dos columnas separadas de año inicial y año final
df3[['Año Inicial', 'Año Final']] = df3['Temporada'].str.split('-', expand=True)

# Convertir las columnas de año inicial y año final a tipo entero
df3['Año Inicial'] = df3['Año Inicial'].astype(int)
df3['Año Final'] = df3['Año Final'].astype(int)

# Calcular el año medio entre el año inicial y el año final
df3['Temporada'] = df3[['Año Inicial', 'Año Final']].mean(axis=1)

# Convertir la temporada a tipo datetime
df3['Temporada'] = pd.to_datetime(df3['Temporada'], format='%Y')

# Eliminar las columnas de año inicial y año final si es necesario
del df3['Año Inicial']
del df3['Año Final']

# Verificar el cambio
print(df3.info())


# In[103]:


# Filtrar las filas para la temporada 2023-01-01
champions_23_24 = df3.loc[df3['Temporada'] == '2023-01-01']

# Filtrar las filas para el resto de temporadas
champions = df3.loc[df3['Temporada'] != '2023-01-01']


# In[104]:


champions.to_csv('dataframe/champions.csv', index=False)
champions_23_24.to_csv('dataframe/champions_23_24.csv', index=False)


# In[105]:


#Jugadores
jugadores.info()


# In[106]:


# Dividir la columna Temporada en dos columnas separadas de año inicial y año final
jugadores[['Año Inicial', 'Año Final']] = jugadores['Temporada'].str.split('-', expand=True)

# Convertir las columnas de año inicial y año final a tipo entero
jugadores['Año Inicial'] = jugadores['Año Inicial'].astype(int)
jugadores['Año Final'] = jugadores['Año Final'].astype(int)

# Calcular el año medio entre el año inicial y el año final
jugadores['Temporada'] = jugadores[['Año Inicial', 'Año Final']].mean(axis=1)

# Convertir la temporada a tipo datetime
jugadores['Temporada'] = pd.to_datetime(jugadores['Temporada'], format='%Y')

# Eliminar las columnas de año inicial y año final si es necesario
del jugadores['Año Inicial']
del jugadores['Año Final']

pais_moda = jugadores['País'].mode()[0]
jugadores['País'].fillna(pais_moda, inplace=True)

pais_moda = jugadores['Posc'].mode()[0]
jugadores['Posc'].fillna(pais_moda, inplace=True)

# Verificar el cambio
print(jugadores.info())


# In[107]:


jugadores.to_csv('dataframe/df_jugadores.csv', index=False)


# In[108]:


# Nombre del archivo donde se guardará el JSON
nombre_archivo = 'dataframe/id_jugador.json'

# Guardar el diccionario en el archivo JSON
with open(nombre_archivo, 'w', encoding="utf-8") as archivo:
    json.dump(ids_jugadores, archivo, ensure_ascii=False)

print("Diccionario id jugadores guardado")
'''