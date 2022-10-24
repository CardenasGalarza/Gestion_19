import base64
import mysql.connector
from mysql.connector import Error
#import pyodbc
import pandas as pd
import streamlit as st
############################################ OCULTAR INFROMACION NO IMPORTANTE
import warnings
warnings.filterwarnings('ignore')

##########################
import time
from datetime import datetime
from datetime import timedelta
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
 
cnxn = mysql.connector.connect( host="us-cdbr-east-06.cleardb.net",
                                port="3306",
                                user="b550dc65be0b71",
                                passwd="a3fa9457",
                                db="heroku_af31a2d889c5388"
                                )
cursor = cnxn.cursor()

#print("listo")
sql = """
SELECT * FROM bduser
"""
dfuser = pd.read_sql(sql, cnxn)


namesbd = dfuser['names'].tolist()
usernamesbd = dfuser['usernames'].tolist()
passwordsbd = dfuser['passwords'].tolist()



print(passwordsbd)