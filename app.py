import mysql.connector
#import pyodbc
import pandas as pd
import streamlit as st
############################################ OCULTAR INFROMACION NO IMPORTANTE
import warnings
warnings.filterwarnings('ignore')
#########################################3333
st.set_page_config(layout="wide")
st.title("GESTION bdtickets CUADRO PENDIENTES💻")



#######
## TODO CONECTION A LA BASE DE DATOS MYSQL
#######


cnxn = mysql.connector.connect( host="us-cdbr-east-06.cleardb.net",
                                port="3306",
                                user="b550dc65be0b71",
                                passwd="a3fa9457",
                                db="heroku_af31a2d889c5388"
                                )
cursor = cnxn.cursor()
#cursor.execute("SELECT  * FROM bdtickets WHERE fec_regist = (SELECT MIN(fec_regist )  FROM bdtickets where ESTADO = 'PENDIENTE' )")
#data = cursor.fetchall()
#df = pd.DataFrame(data)

try:

    genre = st.radio(
        "What's your favorite movie genre",
        ('Desnsar', 'Cerrar y Descansar', 'Programar'))

    if  genre == 'Programar':

        sql = """
        SELECT  *
        FROM bdtickets
        WHERE fec_regist = (SELECT MIN(fec_regist )  FROM bdtickets where ESTADO = 'PENDIENTE' );
        """
        df = pd.read_sql(sql, cnxn)
        print(df)
        st.info(df)
        cnxn.commit()

        col1, col2, col3 = st.columns(3)



        with col1:
            st.markdown("**Numero de tickets**")
            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">edwed</p>', unsafe_allow_html=True)

            #filter_page_or_query = st.markdown("Dimension to filter #1"), st.markdown("<P style='text-align: center; color: BLUE;'>Some title</P>", unsafe_allow_html=True)

        with col2:
            st.markdown("**Codigo de cliente**")
            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">weeeew</p>', unsafe_allow_html=True)

            

        with col3:
            st.markdown("**Fecha de Ticket**")
            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">wedeede</p>', unsafe_allow_html=True)


except Exception as e:
    pass


