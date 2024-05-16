# Champions_23-24

El link a mi repositorio es: [GitHub](https://github.com/crltsnch/Champions_23-24)

La idea de este trabajo es hacer unas predicciones sobre la UEFA Champions League 2023/2024.

## Casas_de_apuestas.pdf
En este fichero está explicado el desarrollo de este proyecto en profundidad con resultados y conclusiones.


## get
En esta carpeta están los ficheros que he usado para conseguir los datos de los csv de la carpeta data.

## data
En esta carpeta están los datos extraídos. 

  - jugador.csv : En este tabla están todos los jugadores que han jugado la UEFA Champions League desde la temporada 2003/04 hasta 2017/18.
  - jugador2.csv : En este tabla están todos los jugadores que han jugado la UEFA Champions League desde la temporada 2017/18 hasta la temporada actual.
  - entrenador.csv : En este data están todos los entrenadores que han jugado en toda la historia de la UEFA.
  - equipo.csv : En este data están todos los equipos que han participado en toda la historia de la UEFA.
  - partido.csv : Todos los partidos jugados en la Champions.
  - Trayectoria_entrenador.csv : Trayectoria profesional como entrenadores de los entrenadores de entrenador.csv.


## dataframe
Datas de la carpeta 'data' limpios y con la estructura correcta. Además estan los json con los id de los jugadores y de los entrenadores.


## preparacion.ipynb y preparacion.py
El cuaderno jupyter fue el utilizado para hacer la limpieza de los datos inicialmente. Una vez quisimos crear un main.py pasamos el ficheor preparacion.ipynb a .py. Los dos ficheros contienen lo mismo.

## exploracion.ipynb
El siguiente paso ha sido la visualización de datos, representar información de manera gráfica y comprensible, facilitando así la interpretación de conjuntos. 


## Aprendizaje Supervisado
### regresion.ipynb
Análisis con diferentes modelos de regresión.

### clasificacion_multiclase.ipynb
Análisis con diferentes modelos de clasificación.


## Aprendizaje no supervisado
### clustering.ipynb
Análisis de agrupación en clústers con diferentes modelos.


## series_temporales.ipynb
Analisis con series temporales.

## DeepLearning
### dnn_1x2.ipynb y dnn_1x2.py
Los dos ficheros crean una red neuronal profunda para la predicción del resultado de un partido de fútbol. Para el entrenamiento y creación de la red me ha sido más útil hacerlo en cuaderno de jupyter, pero para la hora de hacer un main es mejor .py, por ello lo hice también.

### dnn_goles.ipynv y dnn_goles.py
Nuevamente los dos ficheros hacen lo mismo entrenar una red para predecir los goles de un partido de fútbol. Para crear y entrenar la red utilicé el jupyter pero para el main utilice el .py.

### dnn_marcanambos.ipynb y dnn_marcanambos.py
Igual que los anteriores pero para la predicción de si marcarán ambos o no.

### cnn_logo.ipynb
Creación y entrenamiento de una red neuronal convolucional para la predicción de escudos de fútbol con imágenes.

### aprendizaje_por_transferencia.ipynb
Es lo mismo que cnn_logo.ipynb pero el modelo se entrena con un modelo predeterminado base.

## Aprendizaje por refuerzo
### cadenas_markov.ipynb
Creación de las cadenas de Markov para los equipos de cuartos de final con estados ganar, empatar o perder. 

## modelos
Aquí hemos guardado todos los modelos entrenados.

## Resultados
Gráficas con los resultados de los entrenaminetos de los modelos.

## main.py
Ficheor para que el usuario pueda actualizar los datos y hacer las predicciones del partido que desee.

## run.py

