import pandas as pd
from geopy.distance import geodesic

# df es el punto de referencia
df = pd.read_excel('TT.xlsx', engine="openpyxl", skiprows=3)
df = df[['ACOORD_X_TOA__c', 'ACOORD_Y_TOA__c', 'Incident Number', 'Company']]
df.columns = ['latitude', 'longitude', 'tick', 'Company']

# df1 es el dataframe con los puntos a comparar con el punto de referencia
df1 = pd.read_excel('Bachero CMS con xy 2022 12 19.xlsx')

# Filtra los valores de la columna "latitude" que están fuera del rango permitido
df = df[(df['latitude'] >= -90) & (df['latitude'] <= 90)]
df1 = df1[(df1['latitude'] >= -90) & (df1['latitude'] <= 90)]

# Obtiene el punto de referencia (único punto en el dataframe "df")
reference_point = (df['latitude'].iloc[0], df['longitude'].iloc[0])

# Calcula la distancia en metros entre cada punto en df1 y el punto de referencia
df1['radius'] = df1.apply(lambda row: geodesic((row['latitude'], row['longitude']), reference_point).m, axis=1)


df_result = pd.concat([df1, df['tick']], axis=1)
print(df_result)
# Muestra el dataframe df1 con la nueva columna "radius"
#print(df1)

df_result.to_csv('esperoedt.csv', index=False)