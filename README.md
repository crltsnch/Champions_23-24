# Champions_23-24

El link a mi repositorio es: [GitHub](https://github.com/crltsnch/Champions_23-24)
La idea de este trabajo es hacer unas predicciones sobre la UEFA Champions League 2023/2024

## getdatos
En esta carpeta están los ficheros que he usado para conseguir los datos de los csv de la carpeta data.

## data
En esta carpeta está toda la información que he conseguido hasta el momento. 
  - jugadores : En este tabla están los jugadores que están actualmente en la fase de octavos de la champions con sus estadísticas.
  - octavos_df : Este es el DataFrame que he sacado con la exploración y limpieza de datos en el archivo exploracion.py.
  - octavos_id : Es el mismo data que octavos_df, pero para hacer regresión he pasado los nombres a un id.
  - equipos_id : Aquí están los ids de los equipos para saber cual es cada equipo de nuestro data octavos_id.
  - partidos : Este csv contiene todos los partidos de la UEFA Champions League desde 2003
  - valores_jugadores : Aquí tenemos el valor de mercado de los jugadores

## octavos.csv
En este primer tramo del trabajo, dado que está actualmente disputándose la fase de octavos de final, he decido hacer un analisis de los partidos de octavos de los últimos 11 años. Los demás datos que he conseguido serán útiles para analizarlos próximamente. 

## exploracion.ipynb
En este fichero he hecho una exploración de los datos, limpieza y organización de algunas columnas para que sea más comodo de manejar. El nuevo data después de estas modificaciones es el fichero octavos_df.csv.

## visualizacion.ipynb
El siguiente paso ha sido la visualización de datos, representar información de manera gráfica y comprensible, facilitando así la interpretación de conjuntos. Esto permite una comprensión rápida y la identificación de tendencias y patrones. Las visualizaciones también ayudan a detectar anomalías y ofrecen exploración interactiva. Facilita la toma de decisiones al proporcionar contexto visual.
En mi caso he realizado 4 gráficas:
  · Los goles totales por cada equipo en los últimos 11 años.
  · Los goles totale de los últimos 11 años en la ida y en la vuelta de cada equipo.
  · Los goles de los tres equipos con más champions en las últimas 11 temporadas.
  · El número de apariciones de cada equipo en 11 temporadas.

## analisis.ipynb
En el análisis hemos realizado una regresión lineal donde nuestra evaluación ha sido:


