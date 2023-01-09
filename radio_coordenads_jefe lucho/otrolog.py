import numpy as np
import pandas as pd

#Función para calcular la distancia en metros entre dos puntos dadas sus coordenadas
def haversine(lat1, lon1, lat2, lon2):
    # Convertir a radianes
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    # Calcular la distancia usando la fórmula de Haversine
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    # Devolver la distancia en metros
    return c * 6371 * 1000

#Inicializar la distancia máxima metros
distancia_maxima = 100

#Cargar los datos de los puntos que quieres comparar con los puntos de referencia
df1 = pd.read_csv('Bachero CMS con xy 2022 12 19.csv', sep=';')

# df es el punto de referencia
df = pd.read_excel('TT.xlsx', engine="openpyxl", skiprows=3)
df_ref = df[['ACOORD_X_TOA__c', 'ACOORD_Y_TOA__c', 'Incident Number', 'Company']]
df_ref.columns = ['lon_ref', 'lat_ref', 'tick', 'Company']

# Crear una nueva columna en df1 para almacenar la distancia de cada fila a cada punto de referencia
df1['distancia'] = np.nan

# Para cada punto de referencia, calcular la distancia en metros entre el punto de referencia y cada punto de df1
for i, row in df_ref.iterrows():
    lat_ref = row['lat_ref']
    lon_ref = row['lon_ref']
    col_name = 'distancia_{}'.format(i)
    df1[col_name] = df1.apply(lambda row: haversine(lat_ref, lon_ref, row['latitude'], row['longitude']), axis=1)

# Seleccionar la distancia mínima para cada fila
df1['distancia'] = df1[['distancia_{}'.format(i) for i in range(df_ref.shape[0])]].min(axis=1)

# Filtrar df1 y obtener solo las filas cuyo valor de la columna 'distancia' sea menor o igual a la distancia máxima correspondiente
df_filtered = df1[df1['distancia'] <= distancia_maxima]
# Ordenar df_filtered por la columna 'distancia'
df_filtered = df_filtered.sort_values('distancia')
# Mostrar el resultado
print(df_filtered)
