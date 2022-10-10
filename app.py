import mysql.connector
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

except Exception as e:
    pass
