#Importar librerías
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

#Inicializar el punto de referencia
lon_ref = -76.9905493249
lat_ref = -12.0989223479

#Inicializar la distancia máxima metros
distancia_maxima = 100

#Cargar los datos de los puntos que quieres comparar con los puntos de referencia
df1 = pd.read_csv('Bachero CMS con xy 2022 12 19.csv', sep=';')

# Crear una nueva columna en df1 con la distancia en metros entre el punto de referencia y cada punto de df1
df1['distancia'] = df1.apply(lambda row: haversine(lat_ref, lon_ref, row['latitude'], row['longitude']), axis=1)

# Redondear la columna "distancia" a dos decimales
df1['distancia'] = df1['distancia'].round(2)
# Filtrar df1 y obtener solo las filas cuyo valor de la columna 'distancia' sea menor o igual a la distancia máxima
df1_filtered = df1[df1['distancia'] <= distancia_maxima]
#ordenar por rango
df1_filtered = df1_filtered.sort_values('distancia')
# Mostrar el resultado
print(df1_filtered)
