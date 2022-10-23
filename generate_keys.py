import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import mysql.connector
#import pyodbc
import pandas as pd
############################################ OCULTAR INFROMACION NO IMPORTANTE
import warnings
warnings.filterwarnings('ignore')
 
cnxn = mysql.connector.connect( host="us-cdbr-east-06.cleardb.net",
                                port="3306",
                                user="b70d451b4ff985",
                                passwd="68b102d9",
                                db="heroku_9ca78643f8fb80d"
                                )
cursor = cnxn.cursor()


#print("listo")
sql = """
SELECT * FROM bduser
"""
dfuser = pd.read_sql(sql, cnxn)

names = dfuser['names'].tolist()
usernames = dfuser['usernames'].tolist()
passwords = dfuser['passwords'].tolist()

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)





