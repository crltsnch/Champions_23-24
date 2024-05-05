import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Reshape, Conv1D, MaxPooling1D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam, SGD, RMSprop
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import os


# Clase para cargar y preparar los datos
class LoadDataGoles:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        data = pd.read_csv(self.file_path)
        return data

    def prepare_data(self, data):
        # Convertir la columna "Ronda" en variables dummy
        data = pd.get_dummies(data, columns=['Ronda'], drop_first=True)
        
        # Eliminar columnas irrelevantes
        data = data.drop(['idPartido', 'Temporada', 'Evento'], axis=1)

        # Separar características y etiquetas
        X = data.drop(['VictoriaLocal', 'Empate', 'VictoriaVisitante', 'GolesLocal', 'GolesVisitante'], axis=1)
        y = data[['GolesLocal', 'GolesVisitante']]  # Seleccionar goles locales y visitantes como etiquetas

        # Escalar características
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Dividir los datos en conjuntos de entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
        
        # Convertir los datos a tensores
        X_train = tf.convert_to_tensor(X_train, dtype=tf.float32)
        X_test = tf.convert_to_tensor(X_test, dtype=tf.float32)
        y_train = tf.convert_to_tensor(y_train.values, dtype=tf.float32)
        y_test = tf.convert_to_tensor(y_test.values, dtype=tf.float32)
        
        return X_train, X_test, y_train, y_test, scaler, X, y




# Clase para entrenar y evaluar el modelo de predicción de goles locales y visitantes
class GoalsPredictionModel:
    def __init__(self, configurations):
        self.configurations = configurations
        self.best_model = None
        self.best_config = None
        self.best_mae = float('inf')

    def train_or_load_model(self, configurations, X_train, y_train, X_test, y_test, model_path):
        if os.path.exists(model_path):
            # Cargar el modelo pre-entrenado
            self.best_model = cargar_modelo(model_path)
        else:
            # Entrenar un nuevo modelo
            self.train_model(configurations, X_train, y_train, X_test, y_test)
            guardar_modelo(self.best_model, model_path)

    def train_model(self, X_train, y_train, X_test, y_test):
        tf.random.set_seed(42)
        for config in self.configurations:
            input_layer = Input(shape=(X_train.shape[1],))
            dense_layer1 = Dense(config['units'], activation='relu')(input_layer)
            dropout_layer1 = Dropout(config['dropout'])(dense_layer1)
            dense_layer2 = Dense(config['units'], activation='relu')(dropout_layer1)
            dropout_layer2 = Dropout(config['dropout'])(dense_layer2)

            # Salida para la predicción de goles locales
            local_goals_output = Dense(1, name='local_goals_output')(dropout_layer2)
            # Salida para la predicción de goles visitantes
            visitor_goals_output = Dense(1, name='visitor_goals_output')(dropout_layer2)
            
            model = Model(inputs=input_layer, outputs=[local_goals_output, visitor_goals_output])

            optimizer = Adam(learning_rate=config['learning_rate'])
            model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mae'])
            
            history = model.fit(X_train, [y_train[:, 0], y_train[:, 1]], epochs=config['epochs'], batch_size=config['batch_size'], validation_split=0.1)
            
            self.history = history
            _, local_mae, visitor_mae = model.evaluate(X_test, [y_test[:, 0], y_test[:, 1]])
            total_mae = (local_mae + visitor_mae) / 2
            
            if total_mae < self.best_mae:
                self.best_mae = total_mae
                self.best_model = model
                self.best_config = config
            
        return history
    
    def get_best_model(self):
        return self.best_model
    
    def get_best_config(self):
        return self.best_config

    


class ModelEvaluation:
    def __init__(self, model):
        self.model = model
    
    def evaluate_model(self, X_test, y_test):
        # Evaluar el modelo
        local_goals_pred, visitor_goals_pred = self.model.predict(X_test)

        # Calcular y mostrar el MAE para cada tipo de predicción
        local_mae = mean_absolute_error(y_test[:, 0], local_goals_pred)
        visitor_mae = mean_absolute_error(y_test[:, 1], visitor_goals_pred)
        
        print("MAE para la predicción de goles del local:", local_mae)
        print("MAE para la predicción de goles del visitante:", visitor_mae)

        # Graficar los resultados
        labels = ['Goles Local', 'Goles Visitante']
        mae_values = [local_mae, visitor_mae]

        plt.bar(labels, mae_values, width=0.5,  color=['royalblue', 'darkorange'])
        plt.ylabel('MAE')
        plt.title('MAE Predicción de Goles para local y visitante')
        plt.tight_layout()
        plt.savefig('resultados/mae_redes_goles.png')
        plt.show()
    



# Guardar el modelo
def guardar_modelo(modelo, ruta_archivo):
    tf.keras.models.save_model(modelo, ruta_archivo)



def cargar_modelo(ruta_archivo):
    return tf.keras.models.load_model(ruta_archivo)


def data_usuario(ruta_df, ruta_data):
    # Cargar los datos
    df = pd.read_csv(ruta_df)
    data = pd.read_csv(ruta_data)
    df = pd.concat([df, data], ignore_index=True)

    # Suponiendo que tu DataFrame se llama df
    df = df.sort_values(by=['Temporada', 'Ronda'], ascending=[True, True])
    df = pd.get_dummies(df, columns=['Ronda'], drop_first=True)

    return df



def datos_usuario(df, equipo_local, equipo_visitante):
    # Filtrar el DataFrame para obtener la última fila donde el equipo local y visitante coincidan con los ingresados por el usuario
    filtro_ultimo_partido = ((df['Local'] == equipo_local) & (df['Visitante'] == equipo_visitante)) | ((df['Local'] == equipo_visitante) & (df['Visitante'] == equipo_local))

    # Obtener el último partido entre los equipos ingresados por el usuario
    ultimo_partido_entre_equipos = df[filtro_ultimo_partido].iloc[-1]

    # Obtener los valores para las columnas %_Victorias_Local, %_Empate, %_Victoria_Visitante
    valores_prediccion = ultimo_partido_entre_equipos[['%_Victorias_Local', '%_Empate', '%_Victoria_Visitante', 'Ronda_Group stage', 'Ronda_Quarter-finals',	'Ronda_Round of 16', 'Ronda_Semi-finals']]

    if ultimo_partido_entre_equipos['Local'] == equipo_local and ultimo_partido_entre_equipos['Visitante'] == equipo_visitante:
        porcentajes_de_los_dos = ultimo_partido_entre_equipos[['%_Equipo1_Ganado', '%_Equipo2_Ganado']]

    elif ultimo_partido_entre_equipos['Local'] == equipo_visitante and ultimo_partido_entre_equipos['Visitante'] == equipo_local:
        porcentajes_de_los_dos = ultimo_partido_entre_equipos[['%_Equipo1_Ganado', '%_Equipo2_Ganado']]
        porcentajes_de_los_dos = porcentajes_de_los_dos.rename({'%_Equipo1_Ganado': '%_Equipo2_Ganado', '%_Equipo2_Ganado': '%_Equipo1_Ganado'})


    # 3. Filtrar el DataFrame para obtener las estadísticas del equipo local
    filtro_local = (df['Local'] == equipo_local) | (df['Visitante'] == equipo_local)
    ultima_aparicion_local = df[filtro_local].iloc[-1]
    if ultima_aparicion_local['Local'] == equipo_local:
        estadisticas_equipo_local = ultima_aparicion_local[['%_1_G_Temporada', '%_1_G_Temporada_L', '%_1_E_Temporada_L', '%_1_P_Temporada_L', '1_Media_G', '1_Media_G_Local', '1_Media_Goles_PP', '1_ValorJugadores', '1_MediaJugadores']]
    elif ultima_aparicion_local['Visitante'] == equipo_local:
        estadisticas_equipo_local = ultima_aparicion_local[['%_2_G_Temporada', '%_2_G_Temporada_L', '%_2_E_Temporada_L', '%_2_P_Temporada_L', '2_Media_G', '2_Media_G_Local', '2_Media_Goles_PP', '2_ValorJugadores', '2_MediaJugadores']]
        #Cambiar el numero del nombre de las columnas porque si es el local del usuario pasara a ser las columnas con 1 en vez de 2
        estadisticas_equipo_local.index = ['%_1_G_Temporada', '%_1_G_Temporada_L', '%_1_E_Temporada_L', '%_1_P_Temporada_L', '1_Media_G', '1_Media_G_Local', '1_Media_Goles_PP', '1_ValorJugadores', '1_MediaJugadores']

    # 4. Filtrar el DataFrame para obtener las estadísticas del equipo visitante
    filtro_visitante = (df['Local'] == equipo_visitante) | (df['Visitante'] == equipo_visitante)
    ultima_aparicion_visitante = df[filtro_visitante].iloc[-1]
    if ultima_aparicion_visitante['Local'] == equipo_visitante:
        estadisticas_equipo_visitante = ultima_aparicion_visitante[['%_1_G_Temporada', '%_1_G_Temporada_L', '%_1_E_Temporada_L', '%_1_P_Temporada_L', '1_Media_G', '1_Media_G_Local', '1_Media_Goles_PP', '1_ValorJugadores', '1_MediaJugadores']]
        estadisticas_equipo_visitante = estadisticas_equipo_visitante.rename({'%_1_G_Temporada': '%_2_G_Temporada', '%_1_G_Temporada_L': '%_2_G_Temporada_L', '%_1_E_Temporada_L': '%_2_E_Temporada_L', '%_1_P_Temporada_L': '%_2_P_Temporada_L', '1_Media_G': '2_Media_G', '1_Media_G_Local': '2_Media_G_Local', '1_Media_Goles_PP': '2_Media_Goles_PP', '1_ValorJugadores': '2_ValorJugadores', '1_MediaJugadores': '2_MediaJugadores'})
    elif ultima_aparicion_visitante['Visitante'] == equipo_visitante:
        estadisticas_equipo_visitante = ultima_aparicion_visitante[['%_2_G_Temporada', '%_2_G_Temporada_L', '%_2_E_Temporada_L', '%_2_P_Temporada_L', '2_Media_G', '2_Media_G_Local', '2_Media_Goles_PP', '2_ValorJugadores', '2_MediaJugadores']]


    # Combinar las estadísticas de ambos equipos para predecir el resultado del partido
    datos_partido = pd.concat([estadisticas_equipo_local, estadisticas_equipo_visitante, valores_prediccion, porcentajes_de_los_dos])

    # Crear un nuevo DataFrame vacío con las columnas especificadas en el orden deseado
    nuevo_dataframe = pd.DataFrame(columns=['Local', 'Visitante', '%_Victorias_Local', '%_Empate', '%_Victoria_Visitante',
                                            '%_Equipo1_Ganado', '%_Equipo2_Ganado', '%_1_G_Temporada', '%_1_G_Temporada_L',
                                            '%_1_E_Temporada_L', '%_1_P_Temporada_L', '1_Media_G', '1_Media_G_Local', '1_Media_Goles_PP',
                                            '1_ValorJugadores', '1_MediaJugadores', '%_2_G_Temporada', '%_2_G_Temporada_L',
                                            '%_2_E_Temporada_L', '%_2_P_Temporada_L', '2_Media_G', '2_Media_G_Local', '2_Media_Goles_PP',
                                            '2_ValorJugadores', '2_MediaJugadores', 'Ronda_Group stage', 'Ronda_Quarter-finals', 'Ronda_Round of 16', 'Ronda_Semi-finals'])

    # Agregar una fila con los valores proporcionados al nuevo DataFrame
    nuevo_dataframe.loc[0] = [equipo_local, equipo_visitante, datos_partido['%_Victorias_Local'], datos_partido['%_Empate'],
                            datos_partido['%_Victoria_Visitante'], datos_partido['%_Equipo1_Ganado'], datos_partido['%_Equipo2_Ganado'],
                            datos_partido['%_1_G_Temporada'], datos_partido['%_1_G_Temporada_L'], datos_partido['%_1_E_Temporada_L'],
                            datos_partido['%_1_P_Temporada_L'], datos_partido['1_Media_G'], datos_partido['1_Media_G_Local'],
                            datos_partido['1_Media_Goles_PP'], datos_partido['1_ValorJugadores'], datos_partido['1_MediaJugadores'],
                            datos_partido['%_2_G_Temporada'], datos_partido['%_2_G_Temporada_L'], datos_partido['%_2_E_Temporada_L'],
                            datos_partido['%_2_P_Temporada_L'], datos_partido['2_Media_G'], datos_partido['2_Media_G_Local'],
                            datos_partido['2_Media_Goles_PP'], datos_partido['2_ValorJugadores'], datos_partido['2_MediaJugadores'],
                            datos_partido['Ronda_Group stage'], datos_partido['Ronda_Quarter-finals'], datos_partido['Ronda_Round of 16'], datos_partido['Ronda_Semi-finals']]


    return nuevo_dataframe




# Cargar los datos
data_loader = LoadDataGoles('dataframe/champions.csv')
data_goles = data_loader.load_data()
X_train, X_test, y_train, y_test, scaler, X, y = data_loader.prepare_data(data_goles)

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

goals_model_trainer = GoalsPredictionModel(configurations)
goals_model_trainer.train_model(X_train, y_train, X_test, y_test)

goals_model = goals_model_trainer.get_best_model()
best_config = goals_model_trainer.get_best_config()

model_evaluator = ModelEvaluation(goals_model)
model_evaluator.evaluate_model(X_test, y_test)

guardar_modelo(goals_model, 'modelos/modelo_dnn_goals.keras')
model2 = cargar_modelo('modelos/modelo_dnn_goals.keras')

df = data_usuario('dataframe/champions_23_24.csv', 'dataframe/champions.csv')

# 1. Pedir al usuario que ingrese el equipo local
print("Seleccione el equipo local:")
equipos_disponibles = df['Local'].unique()
print(equipos_disponibles)

equipo_local = int(input("Ingrese el nombre del equipo local: "))
equipo_visitante = int(input("Ingrese el nombre del equipo visitante: "))

nuevo_dataframe = datos_usuario(df, equipo_local, equipo_visitante)

X_prediccion = scaler.transform(nuevo_dataframe)
class_probabilities_prediccion = model2.predict(X_prediccion)

print(f"Probabilidades de clase predichas para el partido {equipo_local} VS. {equipo_visitante}:")
print("Goles locales:", class_probabilities_prediccion[0])
print("Goles visitantes:", class_probabilities_prediccion[1])




