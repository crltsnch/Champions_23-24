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

  - Los goles totales por cada equipo en los últimos 11 años.
  - Los goles totale de los últimos 11 años en la ida y en la vuelta de cada equipo.
  - Los goles de los tres equipos con más champions en las últimas 11 temporadas.
  - El número de apariciones de cada equipo en 11 temporadas.

## analisis.ipynb
Mi objetivo era predecir los goles totales que va a meter los equipos de la columna 'equipo1' en la ida y en la vuelta.

En el análisis hemos realizado una regresión lineal donde nuestra evaluación ha sido:

  + Mean Squared Error (MSE): 0.5647731274271107
  + R-squared (R²): 0.8529047481620708
  + Root Mean Squared Error (RMSE): 0.7515138903753614
  + Mean Absolute Error (MAE): 0.5374315500330797
    
Para visualizar mejor los resultados perdichos respuesto los reales. He creado un grafico de dispersión y un histograma de los residuos.
  
También he realizado un árbol de decisión para ver si las predicciones mejoraban:

  + Mean Squared Error (MSE) for Decision Tree: 1.2777777777777777
  + R-squared (R²) for Decision Tree: 0.6672025723472668
  + Mean Absolute Error (MAE) for Decision Tree: 0.7222222222222222

La regresión lineal tiene un rendimiento superior en este conjunto de datos específico, según las métricas evaluadas. La regresión lineal explica una mayor proporción de la variabilidad en la variable objetivo (según R^2) y tiene un MSE más bajo en comparación con el árbol de decisión. Si bien el árbol de decisión puede ser útil, especialmente si hay relaciones no lineales en los datos, en este caso, la regresión lineal parece ser una opción más efectiva.

Después he probado con random forest:

  + Mean Squared Error (MSE) for Random Forest: 1.1426277777777778
  + R-squared (R²) for Random Forest: 0.7024024115755627
  + Mean Absolute Error (MAE) for Random Forest: 0.8061111111111111
  + {'Equipo 1': 0.037121375123763865,
 'Equipo 2': 0.038921409305569823,
 'Temporada': 0.04377090014279057,
 'goles_2': 0.03273337216358079,
 'goles_ida_1': 0.6642245066051174,
 'goles_ida_2': 0.010346474856633814,
 'goles_vuelta_2': 0.07927713471330618,
 'goles_vuelta_1': 0.09360482708923744}

El modelo de Random Forest parece estar haciendo predicciones significativamente mejores que el árbol de decisión original (por el menor MSE y el mayor R^2). La característica más importante para las predicciones del modelo es 'goles_ida_1', lo que sugiere que la cantidad de goles marcados por el Equipo 1 en el partido de ida es un factor crucial en la predicción de los resultados. Estas conclusiones pueden ser útiles para comprender las características más influyentes y para tomar decisiones sobre qué aspectos del modelo mejorar o qué características pueden ser más relevantes para el problema en cuestión.

Eligiendo regresión lienal como nuestro mejor modelo, observando los valores predichos para nuestros valores de x_test (tener en cuenta que el array que devuelve la predicción esta escalada) podríamos decir que en esta fase de octavos, que actualmente se está jugando, pasaría a cuartos de final el Arsenal, el PSG meterá 4 goles (actualmente lleva 2, queda la vuelta),  el Atlético de Madrid anotará 3 goles. 

En futuras entregas podremos hacer análisis detallados en relación con otros datos como los de jugadores.
