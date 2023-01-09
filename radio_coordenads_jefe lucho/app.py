import streamlit as st
import numpy as np
import pandas as pd

st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,white, white);color:navy;font-size:24px;border-radius:2%;"><b>ENVIAR MENSAJE GESTION</b></p>', unsafe_allow_html=True)

with st.form(key='my_form', clear_on_submit=True):
    age = st.slider('How old are you?', 0, 130, 25)
    st.write("I'm ", age, 'years old')

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

    col1, col2 = st.columns(2)

    with col1:
        lon_ref = st.number_input(label="lon_ref",step=1.,format="%.2f")

    with col2:
        lat_ref = st.number_input(label="lat_ref",step=1.,format="%.2f")


    st.balloons()
# Every form must have a submit button.
    submitted = st.form_submit_button("✉️Enviar")

    if submitted == True:
        with st.spinner('Enviado mensaje...'):
            #Inicializar la distancia máxima metros
            distancia_maxima = 100

            #Cargar los datos de los puntos que quieres comparar con los puntos de referencia
            df1 = pd.read_csv('Bachero CMS con xy 2022 12 19.csv', sep=';')

            # Crear una nueva columna en df1 con la distancia en metros entre el punto de referencia y cada punto de df1
            df1['distancia'] = df1.apply(lambda row: haversine(lat_ref, lon_ref, row['latitude'], row['longitude']), axis=1)

            # Redondear la columna "distancia" a dos decimales
            # Filtrar df1 y obtener solo las filas cuyo valor de la columna 'distancia' sea menor o igual a la distancia máxima
            df1_filtered = df1[df1['distancia'] <= distancia_maxima]
            #ordenar por rango
            df1_filtered = df1_filtered.sort_values('distancia')

            #redondear truco es str
            df1_filtered['distancia'] = df1_filtered['distancia'].apply(lambda x: str(round(x, 2)))

            # Mostrar el resultado
            st.dataframe(df1_filtered)


