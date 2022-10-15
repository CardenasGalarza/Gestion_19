import base64
import mysql.connector
#import pyodbc
import pandas as pd
import streamlit as st
from datetime import datetime

cnxn = mysql.connector.connect( host="us-cdbr-east-06.cleardb.net",
                                port="3306",
                                user="b550dc65be0b71",
                                passwd="a3fa9457",
                                db="heroku_af31a2d889c5388"
                                )
cursor = cnxn.cursor()
#print("listo")

print("listo")
### EXTARER DATOS
sql = """
SELECT GESTOR, codreq, FEC_CERRAR FROM bdtickets WHERE  ESTADO="CERRAR" ;
"""
df = pd.read_sql(sql, cnxn)
df = df[df['GESTOR'] == 'Giancarlos Cardenas']
date = datetime.now()
tcanti = (date.strftime("%Y-%m-%d"))

df['FEC_CERRAR'] = pd.to_datetime(df['FEC_CERRAR']).dt.date
df['FEC_CERRAR'] = pd.to_datetime(df['FEC_CERRAR'], format='%Y-%m-%d')
canti = len(df[df['FEC_CERRAR'] == tcanti])
print(canti)