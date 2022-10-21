import base64
import mysql.connector
from mysql.connector import Error
#import pyodbc
import pandas as pd
import streamlit as st
############################################ OCULTAR INFROMACION NO IMPORTANTE
import warnings
warnings.filterwarnings('ignore')
#########################################3333
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
import database as db
##########################
import time
from datetime import datetime
from datetime import timedelta
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
 
names = ["Luis Llerena Lagunes", "Rebecca Miller", 'Giancarlos Cardenas', "Mauro Arturo Garcia", "John Jairo Bravo", "Alfredo", "Eber Efrain Hinostroza", "Jose Ricardo", "Genesis Medrano"]
usernames = ["LLLERENAL", "rmiller","Cardenas", "mgarciab", "jbravob", "amedinav", "ehinostrozam", "jargomedos", "Genesis"]
passwords = ["Smnz$1304$La", "def456", "cardenas10", "Gaddiel$14", "48557917", "Gaddiel$14", "capricornio28", "S3gunda_L", "medrano10"]
 
hashed_passwords = stauth.Hasher(passwords).generate()
authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
'AdLeS_cookie','AdLeS_key',cookie_expiry_days=30)
 

name, authentication_status, username = authenticator.login('Login', 'main')
 
if authentication_status:
    st.title('Welcome *%s* to Pakistan' % (name))
    st.write("Our first Streamlit App")
 
    cnxn = mysql.connector.connect( host="us-cdbr-east-06.cleardb.net",
                                    port="3306",
                                    user="b550dc65be0b71",
                                    passwd="a3fa9457",
                                    db="heroku_af31a2d889c5388"
                                    )
    cursor = cnxn.cursor()






    
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')